import re
import time
import json
import random
import os
import requests
from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

X_FL = "the_c.json"

X_UA = os.environ.get("Z_UA", "Mozilla/5.0")
try:
    X_SC = json.loads(os.environ.get("Z_SOURCES", "[]"))
except Exception:
    X_SC = []

X_HD = {"User-Agent": X_UA}
X_WK = 100  
X_TM = 5

l_p = Lock()
l_f = Lock()

X_DS = os.environ.get("Z_DISCORD_WEBHOOK", "")

def x_dsc(s_cnt, t_cnt):
    """Failsafe payload delivery agent: ignores errors silently"""
    if not X_DS:
        return
    try:
        dat = x_lod()
        mx_e = 0
        nw = int(time.time())
        
        for k, v in dat.get("dynamic_state", {}).items():
            c_str = v.get("last_working_cookie", "")
            m = re.search(r"exp=(\d+)", c_str)
            if m:
                e_val = int(m.group(1))
                if e_val > mx_e:
                    mx_e = e_val
                    
        t_st = "Unknown"
        if mx_e > nw:
            t_st = f"VALID (expires in {x_fmt(mx_e - nw)})"
        elif mx_e > 0:
            t_st = f"EXPIRED ({x_fmt(nw - mx_e)} ago)"

        flg_st = "🟢 SUCCESS" if s_cnt > 0 else "🔴 ATTENTION"
        
        payload = {
            "username": "Matrix Synchronization Bot",
            "embeds": [{
                "title": f"{flg_st} - Sync Process Complete",
                "color": 3066993 if s_cnt > 0 else 15158332,
                "fields": [
                    {"name": "Execution Summary", "value": f"`{s_cnt} / {t_cnt}` target successfully parsed.", "inline": True},
                    {"name": "Ecosystem Baseline", "value": f"Latest Window: `{t_st}`", "inline": False}
                ],
                "footer": {"text": f"Event Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}"}
            }]
        }
        requests.post(X_DS, json=payload, headers={"Content-Type": "application/json"}, timeout=5)
    except Exception:
        pass

def x_lod():
    if not os.path.exists(X_FL):
        exit(1)
    try:
        with open(X_FL, "r") as f:
            return json.load(f)
    except Exception:
        exit(1)

def x_sav(dat):
    with l_f:
        with open(X_FL, "w") as f:
            json.dump(dat, f, indent=2)

def x_gth():
    res = []
    ptrn = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{2,5}\b')
    for src in X_SC:
        try:
            r = requests.get(src, timeout=6)
            if r.status_code == 200:
                res.extend(ptrn.findall(r.text))
        except Exception:
            continue
    return list(dict.fromkeys(res))

def x_ex(n, b_url, h_val):
    px = {"http": f"http://{n}", "https": f"http://{n}"}
    cks = {"hdntl": h_val} if h_val else {}
    try:
        with requests.Session() as s:
            resp = s.get(b_url, headers=X_HD, cookies=cks, proxies=px, timeout=X_TM)
            if resp.status_code == 200:
                return {"status": "SUCCESS", "n": n}
            return {"status": "BLOCKED", "n": n}
    except Exception:
        return {"status": "FAILED", "n": n}

def x_fmt(s):
    h, r = divmod(s, 3600)
    m, r_s = divmod(r, 60)
    parts = []
    if h > 0: parts.append(f"{h}h")
    if m > 0 or h > 0: parts.append(f"{m}m")
    parts.append(f"{r_s}s")
    return " ".join(parts)
    
def main():
    dat = x_lod()
    pool = x_gth()

    if not pool:
        return

    targets = dat.get("initial_targets", {})
    total_targets = len(targets)
    success_count = 0

    for k, tgt in targets.items():
        parsed = urlparse(tgt)
        b_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        h_val = parse_qs(parsed.query).get("__hdntl", [""])[0]

        print(f"-> Testing Target: {k}")
        target_resolved = False
        random.shuffle(pool)

        with ThreadPoolExecutor(max_workers=X_WK) as ex:
            futures = {
                ex.submit(x_ex, n, b_url, h_val): n 
                for n in pool
            }

            for f in as_completed(futures):
                try:
                    res = f.result()
                    if res["status"] == "SUCCESS":
                        print(f"   [SUCCESS] {res['n']} worked for {k}")
                        dat = x_lod()
                        dat["dynamic_state"][k] = {
                            "when_working": f"hdntl={h_val}",
                            "updated_at": int(time.time())
                        }
                        dat["flags"][k]["done"] = "YES"
                        x_sav(dat)
                        success_count += 1
                        target_resolved = True
                        ex.shutdown(wait=False, cancel_futures=True)
                        break
                except Exception:
                    continue

        if target_resolved:
            print(f"-> Target {k} resolved successfully. Halting subsequent checks.")
            break
        else:
            print(f"-> Target {k} failed or returned non-200. Proceeding to secondary target...")

    x_dsc(success_count, total_targets)

if __name__ == "__main__":
    main()
