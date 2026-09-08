import re
import time
import json
import random
import os
import base64
import requests
from urllib.parse import urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

_0xf1 = "the_c.json"

_0xa1 = os.environ.get(base64.b64decode('Wl9VQQ==').decode(), "Mozilla/5.0")
try:
    _0x5c = json.loads(os.environ.get(base64.b64decode('Wl9TT1VSQ0VT').decode(), "[]"))
except Exception:
    _0x5c = []

_0x1h = {base64.b64decode('VXNlci1BZ2VudA==').decode(): _0xa1}
_0x9w = 100  
_0x4t = 5

_l1 = Lock()
_l2 = Lock()

_0xdc = os.environ.get(base64.b64decode('Wl9ESVNDT1JEX1dFQlJPT0s=').decode(), "")

def _fn_n(s_c, t_c):
    if not _0xdc:
        return
    try:
        _dat = _fn_l()
        _mx = 0
        _nw = int(time.time())
        
        for _k, _v in _dat.get(base64.b64decode('ZHluYW1pY19zdGF0ZQ==').decode(), {}).items():
            _cs = _v.get(base64.b64decode('bGFzdF93b3JraW5nX2Nvb2tpZQ==').decode(), "")
            _m = re.search(r"exp=(\d+)", _cs)
            if _m:
                _ev = int(_m.group(1))
                if _ev > _mx:
                    _mx = _ev
                    
        _ts = "Unknown"
        if _mx > _nw:
            _ts = f"VALID (expires in {_fn_t(_mx - _nw)})"
        elif _mx > 0:
            _ts = f"EXPIRED ({_fn_t(_nw - _mx)} ago)"

        _fs = "🟢 SUCCESS" if s_c > 0 else "🔴 ATTENTION"
        
        _payload = {
            "username": "Matrix Synchronization Bot",
            "embeds": [{
                "title": f"{_fs} - Sync Process Complete",
                "color": 3066993 if s_c > 0 else 15158332,
                "fields": [
                    {"name": "Execution Summary", "value": f"`{s_c} / {t_c}` target successfully parsed.", "inline": True},
                    {"name": "Ecosystem Baseline", "value": f"Latest Window: `{_ts}`", "inline": False}
                ],
                "footer": {"text": f"Event Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}"}
            }]
        }
        requests.post(_0xdc, json=_payload, headers={base64.b64decode('Q29udGVudC1UeXBl').decode(): base64.b64decode('YXBwbGljYXRpb24vanNvbg==').decode()}, timeout=5)
    except Exception:
        pass

def _fn_l():
    if not os.path.exists(_0xf1):
        exit(1)
    try:
        with open(_0xf1, "r") as _f:
            return json.load(_f)
    except Exception:
        exit(1)

def _fn_s(_dat):
    with _l2:
        with open(_0xf1, "w") as _f:
            json.dump(_dat, _f, indent=2)

def _fn_g():
    _res = []
    _pt = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{2,5}\b')
    for _src in _0x5c:
        try:
            _r = requests.get(_src, timeout=6)
            if _r.status_code == 200:
                _res.extend(_pt.findall(_r.text))
        except Exception:
            continue
    return list(dict.fromkeys(_res))

def _fn_e(_node, _burl, _hval):
    _prx_key = base64.b64decode('aHR0cA==').decode()
    _px = {_prx_key: f"http://{_node}", base64.b64decode('aHR0cHM==').decode(): f"http://{_node}"}
    _ck_name = base64.b64decode('aGRudGw=').decode()
    _cks = {_ck_name: _hval} if _hval else {}
    try:
        with requests.Session() as _sess:
            _resp = _sess.get(_burl, headers=_0x1h, cookies=_cks, proxies=_px, timeout=_0x4t)
            if _resp.status_code == 200:
                _cookie_header = base64.b64decode('U2V0LUNvb2tpZQ==').decode()
                _ck = _resp.headers.get(_cookie_header)
                if _ck:
                    return {"status": "SUCCESS", "n": _node, "ck": _ck}
                return {"status": "SUCCESS", "n": _node, "ck": f"{_ck_name}={_hval}"}
            return {"status": "BLOCKED", "n": _node}
    except Exception:
        return {"status": "FAILED", "n": _node}

def _fn_t(_sec):
    _h, _r = divmod(_sec, 3600)
    _m, _rs = divmod(_r, 60)
    _p = []
    if _h > 0: _p.append(f"{_h}h")
    if _m > 0 or _h > 0: _p.append(f"{_m}m")
    _p.append(f"{_rs}s")
    return " ".join(_p)
    
def main():
    _dat = _fn_l()
    _pool = _fn_g()

    if not _pool:
        return

    _targets = _dat.get(base64.b64decode('aW5pdGlhbF90YXJnZXRz').decode(), {})
    _tot = len(_targets)
    _suc = 0

    _current_time = int(time.time())
    _flags_key = base64.b64decode('ZmxhZ3M=').decode()
    _done_key = base64.b64decode('ZG9uZQ==').decode()
    _dyn_key = base64.b64decode('ZHluYW1pY19zdGF0ZQ==').decode()
    _cookie_key = base64.b64decode('bGFzdF93b3JraW5nX2Nvb2tpZQ==').decode()
    _param_key = base64.b64decode('X19oZG50bA==').decode()

    for _k, _tgt in _targets.items():
        _parsed = urlparse(_tgt)
        _burl = f"{_parsed.scheme}://{_parsed.netloc}{_parsed.path}"
        
        _flag_val = _dat.get(_flags_key, {}).get(_k, {}).get(_done_key, "NO")
        _dyn_cookie = _dat.get(_dyn_key, {}).get(_k, {}).get(_cookie_key, "")
        
        _is_expired = True
        _m = re.search(r"exp=(\d+)", _dyn_cookie)
        if _m:
            _exp_val = int(_m.group(1))
            if _exp_val > _current_time:
                _is_expired = False

        if _flag_val == "NO" and (not _dyn_cookie or _is_expired):
            _hval = parse_qs(_parsed.query).get(_param_key, [""])[0]
            print(f"-> Endpoint {_k}: Flag is OFF and cookie is empty/expired. Falling back to initial target query parameter.")
        else:
            if "=" in _dyn_cookie:
                _hval = _dyn_cookie.split("=", 1)[1]
            else:
                _hval = _dyn_cookie if _dyn_cookie else parse_qs(_parsed.query).get(_param_key, [""])[0]
            print(f"-> Endpoint {_k}: Using dynamic state cookie value.")

        _resolved = False
        random.shuffle(_pool)

        with ThreadPoolExecutor(max_workers=_0x9w) as _ex:
            _futs = {
                _ex.submit(_fn_e, _nd, _burl, _hval): _nd 
                for _nd in _pool
            }

            for _f in as_completed(_futs):
                try:
                    _res = _f.result()
                    if _res["status"] == "SUCCESS":
                        print(f"   [OK] Node {_res['n']} bound successfully.")
                        _dat = _fn_l()
                        _cln = _res["ck"].split(";")[0].strip()

                        _dat[_dyn_key][_k] = {
                            _cookie_key: _cln,
                            base64.b64decode('dXBkYXRlZF9hdA==').decode(): int(time.time())
                        }
                        _dat[_flags_key][_k][_done_key] = "YES"
                        _fn_s(_dat)
                        _suc += 1
                        _resolved = True
                        _ex.shutdown(wait=False, cancel_futures=True)
                        break
                except Exception:
                    continue

        if _resolved:
            print(f"-> Endpoint {_k} resolved. Skipping subsequent items.")
            break
        else:
            print(f"-> Endpoint {_k} unresponsive. Moving to next item...")

    _fn_n(_suc, _tot)

if __name__ == "__main__":
    main()
