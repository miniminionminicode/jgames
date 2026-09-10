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

def _b(s):
    return base64.b64decode(s.encode()).decode()

_0xf1 = _b('dGhlX2MuanNvbg==')

_0xa1 = os.environ.get(_b('Wl9VQQ=='), _b('TW96aWxsYS81LjA='))
try:
    _0x5c = json.loads(os.environ.get(_b('Wl9TT1VSQ0VT'), _b('Wl ')))
except Exception:
    _0x5c = []

if not _0x5c:
    try:
        _0x5c = json.loads(os.environ.get(_b('Wl9TT1VSQ0VT'), _b('Wl9TT1VSQ0VT') and '[]'))
    except Exception:
        _0x5c = []

_0x_origin = os.environ.get(_b('Wl9PUklHSU4='), '')

_0x1h = {
    _b('VXNlci1BZ2VudA=='): _0xa1
}
if _0x_origin:
    _0x1h[_b('T3JpZ2lu')] = _0x_origin     
    _0x1h[_b('UmVmZXJlcg==')] = f"{_0x_origin}/"
_0x9w = 100  
_0x4t = 5

_l1 = Lock()
_l2 = Lock()

_0xdc = os.environ.get(_b('Wl9ESVNDT1JEX1dFQlJPT0s='), "")

def _fn_n(_dat):
    if not _0xdc:
        return
    try:
        _nw = int(time.time())
        _fields = []
        
        _targets = _dat.get(_b('aW5pdGlhbF90YXJnZXRz'), {})
        _flags = _dat.get(_b('ZmxhZ3M='), {})
        _dyn = _dat.get(_b('ZHluYW1pY19zdGF0ZQ=='), {})
        
        idx = 1
        for _k, _tgt in _targets.items():
            _flag = _flags.get(_k, {}).get(_b('ZG9uZQ=='), "NO")
            _cookie = _dyn.get(_k, {}).get(_b('bGFzdF93b3JraW5nX2Nvb2tpZQ=='), "")
            
            _status_text = "Pending"
            if _cookie:
                _m = re.search(r"exp=(\d+)", _cookie)
                if _m:
                    _ev = int(_m.group(1))
                    if _ev > _nw:
                        _status_text = f"Active (Valid for {_fn_t(_ev - _nw)})"
                    else:
                        _status_text = f"Expired ({_fn_t(_nw - _ev)} ago)"
                else:
                    _status_text = "Active"
            
            if _flag == "YES":
                _status_text += " [Done]"
            else:
                _status_text += " [Expired / Pending]"
            
            _ordinal = f"{idx}st URL" if idx == 1 else (f"{idx}nd URL" if idx == 2 else f"{idx}rd URL" if idx == 3 else f"{idx}th URL")
            _fields.append({
                _b('bmFtZQ=='): f"{_ordinal}: {_k}",
                _b('dmFsdWU='): f"Status: `{_status_text}`",
                _b('aW5saW5l'): False
            })
            idx += 1

        _fs = _b('8J+SuCBTVUNDRVNT')
        
        _payload = {
            _b('dXNlcm5hbWU='): _b('TWF0cml4IFN5bmNocm9uaXphdGlvbiBCb3Q='),
            _b('ZW1iZWRz'): [{
                _b('dGl0bGU='): f"{_fs} - Sync Process Complete",
                _b('Y29sb3I='): 3066993,
                _b('ZmllbGRz'): _fields,
                _b('Zm9vdGVy'): {_b('dGV4dA=='): f"Event Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}"}
            }]
        }
        requests.post(_0xdc, json=_payload, headers={_b('Q29udGVudC1UeXBl'): _b('YXBwbGljYXRpb24vanNvbg==')}, timeout=5)
    except Exception:
        pass

def _fn_l():
    if not os.path.exists(_0xf1):
        exit(1)
    try:
        with open(_0xf1, _b('cg==')) as _f:
            return json.load(_f)
    except Exception:
        exit(1)

def _fn_s(_dat):
    with _l2:
        with open(_0xf1, _b('dz==')) as _f:
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

def _fn_e(_node, _burl, _hval, _ck_name="hdntl"):
    _prx_key = _b('aHR0cA==')
    _px = {_prx_key: f"http://{_node}", _b('aHR0cHM=='): f"http://{_node}"}
    _cks = {_ck_name: _hval} if _hval else {}
    try:
        with requests.Session() as _sess:
            _resp = _sess.get(_burl, headers=_0x1h, cookies=_cks, proxies=_px, timeout=_0x4t)
            if _resp.status_code == 200:
                _cookie_header = _b('U2V0LUNvb2tpZQ==')
                _ck = _resp.headers.get(_cookie_header)
                if _ck:
                    return {_b('c3RhdHVz'): _b('U1VDQ0VTUw=='), _b('bg=='): _node, _b('Y2s='): _ck}
                return {_b('c3RhdHVz'): _b('U1VDQ0VTUw=='), _b('bg=='): _node, _b('Y2s='): f"{_ck_name}={_hval}"}
            return {_b('c3RhdHVz'): _b('QkxPQ0tFRA=='), _b('bg=='): _node}
    except Exception:
        return {_b('c3RhdHVz'): _b('RkFJTEVE'), _b('bg=='): _node}

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
        print(_b('Wy1dIFByb3h5IHBvb2wgaXMgZW1wdHku'))
        return

    _targets = _dat.get(_b('aW5pdGlhbF90YXJnZXRz'), {})
    _current_time = int(time.time())
    _flags_key = _b('ZmxhZ3M=')
    _done_key = _b('ZG9uZQ==')
    _dyn_key = _b('ZHluYW1pY19zdGF0ZQ==')
    _cookie_key = _b('bGFzdF93b3JraW5nX2Nvb2tpZQ==')

    _total_pool_size = len(_pool)
    print(f"[*] Total Proxies Loaded into Pool: {_total_pool_size}")

    for _k, _tgt in _targets.items():
        _parsed = urlparse(_tgt)
        _query_params = parse_qs(_parsed.query)
        
        if "hdnea" in _query_params:
            _ck_name = "hdnea"
        elif "__hdnea" in _query_params:
            _ck_name = "__hdnea"
        elif "hdntl" in _query_params:
            _ck_name = "hdntl"
        else:
            _ck_name = "__hdntl"

        # URL handling logic
        if "Latest" in _k:
            _burl = _tgt  
        else:
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
            _hval = _query_params.get(_ck_name, [""])[0]
            print(f"\n-> Endpoint: {_k} | Source: [INITIAL TARGET URL] | Cookie Type: {_ck_name}")
        else:
            if "=" in _dyn_cookie:
                _hval = _dyn_cookie.split("=", 1)[1]
            else:
                _hval = _dyn_cookie if _dyn_cookie else _query_params.get(_ck_name, [""])[0]
            print(f"\n-> Endpoint: {_k} | Source: [DYNAMIC STATE COOKIE]")

        _resolved = False
        random.shuffle(_pool)
        _attempted = 0

        with ThreadPoolExecutor(max_workers=_0x9w) as _ex:
            _futs = {
                _ex.submit(_fn_e, _nd, _burl, _hval, _ck_name): _nd 
                for _nd in _pool
            }

            for _f in as_completed(_futs):
                _attempted += 1
                _pct = (_attempted / _total_pool_size) * 100
                try:
                    _res = _f.result()
                    if _res[_b('c3RhdHVz')] == _b('U1VDQ0VTUw=='):
                        print(f"    [OK] [{_attempted}/{_total_pool_size} - {_pct:.1f}%] Node {_res[_b('bg==' )]} bound successfully.")
                        _dat = _fn_l()
                        _cln = _res[_b('Y2s=')].split(";")[0].strip()

                        _dat[_dyn_key][_k] = {
                            _cookie_key: _cln,
                            _b('dXBkYXRlZF9hdA=='): int(time.time())
                        }
                        _dat[_flags_key][_k][_done_key] = "YES"
                        _fn_s(_dat)
                        _resolved = True
                        _ex.shutdown(wait=False, cancel_futures=True)
                        break
                    else:
                        print(f"    [X] [{_attempted}/{_total_pool_size} - {_pct:.1f}%] Node {_futs[_f]} -> Status: {_res[_b('c3RhdHVz')]}", end="\r")
                except Exception:
                    continue

        if _resolved:
            print(f"-> Endpoint {_k} resolved successfully after testing {_attempted}/{_total_pool_size} proxies ({(_attempted/_total_pool_size)*100:.1f}%).")
        else:
            print(f"-> Endpoint {_k} failed across all {_total_pool_size} proxies. Proceeding to next target...")
            
    _updated_dat = _fn_l()
    _fn_n(_updated_dat)

if __name__ == "__main__":
    main()
