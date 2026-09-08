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
    _0x5c = json.loads(os.environ.get(_b('Wl9TT1VSQ0VT'), _b('Wl '))) # handled fallback
except Exception:
    _0x5c = []

if not _0x5c:
    try:
        _0x5c = json.loads(os.environ.get(_b('Wl9TT1VSQ0VT'), _b('Wl9TT1VSQ0VT') and '[]'))
    except Exception:
        _0x5c = []

_0x1h = {_b('VXNlci1BZ2VudA=='): _0xa1}
_0x9w = 100  
_0x4t = 5

_l1 = Lock()
_l2 = Lock()

_0xdc = os.environ.get(_b('Wl9ESVNDT1JEX1dFQlJPT0s='), "")

def _fn_n(s_c, t_c):
    if not _0xdc:
        return
    try:
        _dat = _fn_l()
        _mx = 0
        _nw = int(time.time())
        
        for _k, _v in _dat.get(_b('ZHluYW1pY19zdGF0ZQ=='), {}).items():
            _cs = _v.get(_b('bGFzdF93b3JraW5nX2Nvb2tpZQ=='), "")
            _m = re.search(r"exp=(\d+)", _cs)
            if _m:
                _ev = int(_m.group(1))
                if _ev > _mx:
                    _mx = _ev
                    
        _ts = _b('VW5rbm93bg==')
        if _mx > _nw:
            _ts = f"VALID (expires in {_fn_t(_mx - _nw)})"
        elif _mx > 0:
            _ts = f"EXPIRED ({_fn_t(_nw - _mx)} ago)"

        _fs = _b('8J+SuCBTVUNDRVNT') if s_c > 0 else _b('8J+QtSBBVFRFTlRJT04=')
        
        _payload = {
            _b('dXNlcm5hbWU='): _b('TWF0cml4IFN5bmNocm9uaXphdGlvbiBCb3Q='),
            _b('ZW1iZWRz'): [{
                _b('dGl0bGU='): f"{_fs} - Sync Process Complete",
                _b('Y29sb3I='): 3066993 if s_c > 0 else 15158332,
                _b('ZmllbGRz'): [
                    {_b('bmFtZQ=='): _b('RXhlY3V0aW9uIFN1bW1hcnk='), _b('dmFsdWU='): f"`{s_c} / {t_c}` target successfully parsed.", _b('aW5saW5l'): True},
                    {_b('bmFtZQ=='): _b('RWNvcnlzdGVtIEJhc2VsaW5l'), _b('dmFsdWU='): f"Latest Window: `{_ts}`", _b('aW5saW5l'): False}
                ],
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

def _fn_e(_node, _burl, _hval):
    _prx_key = _b('aHR0cA==')
    _px = {_prx_key: f"http://{_node}", _b('aHR0cHM=='): f"http://{_node}"}
    _ck_name = _b('aGRudGw=')
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
    _tot = len(_targets)
    _suc = 0

    _current_time = int(time.time())
    _flags_key = _b('ZmxhZ3M=')
    _done_key = _b('ZG9uZQ==')
    _dyn_key = _b('ZHluYW1pY19zdGF0ZQ==')
    _cookie_key = _b('bGFzdF93b3JraW5nX2Nvb2tpZQ==')
    _param_key = _b('X19oZG50bA==')

    _total_pool_size = len(_pool)
    print(f"[*] Total Proxies Loaded into Pool: {_total_pool_size}")

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
            print(f"\n-> Endpoint: {_k} | Source: [INITIAL TARGET URL]")
        else:
            if "=" in _dyn_cookie:
                _hval = _dyn_cookie.split("=", 1)[1]
            else:
                _hval = _dyn_cookie if _dyn_cookie else parse_qs(_parsed.query).get(_param_key, [""])[0]
            print(f"\n-> Endpoint: {_k} | Source: [DYNAMIC STATE COOKIE]")

        _resolved = False
        random.shuffle(_pool)
        _attempted = 0

        with ThreadPoolExecutor(max_workers=_0x9w) as _ex:
            _futs = {
                _ex.submit(_fn_e, _nd, _burl, _hval): _nd 
                for _nd in _pool
            }

            for _f in as_completed(_futs):
                _attempted += 1
                _pct = (_attempted / _total_pool_size) * 100
                try:
                    _res = _f.result()
                    if _res[_b('c3RhdHVz')] == _b('U1VDQ0VTUw=='):
                        print(f"   [OK] [{_attempted}/{_total_pool_size} - {_pct:.1f}%] Node {_res[_b('bg==' )]} bound successfully.")
                        _dat = _fn_l()
                        _cln = _res[_b('Y2s=')].split(";")[0].strip()

                        _dat[_dyn_key][_k] = {
                            _cookie_key: _cln,
                            _b('dXBkYXRlZF9hdA=='): int(time.time())
                        }
                        _dat[_flags_key][_k][_done_key] = "YES"
                        _fn_s(_dat)
                        _suc += 1
                        _resolved = True
                        _ex.shutdown(wait=False, cancel_futures=True)
                        break
                    else:
                        print(f"   [X] [{_attempted}/{_total_pool_size} - {_pct:.1f}%] Node {_futs[_f]} -> Status: {_res[_b('c3RhdHVz')]}", end="\r")
                except Exception:
                    continue

        if _resolved:
            print(f"-> Endpoint {_k} resolved successfully after testing {_attempted}/{_total_pool_size} proxies ({(_attempted/_total_pool_size)*100:.1f}%).")
            break
        else:
            print(f"-> Endpoint {_k} failed across all {_total_pool_size} proxies. Proceeding to secondary target...")

    _fn_n(_suc, _tot)

if __name__ == "__main__":
    main()
