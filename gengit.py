import os,sys,time
os.system("rm -rf .git")
pid = int(sys.argv[1])
msg = ["init","alloc 1K","access 1K","alloc 1M","access 1M","alloc mm","access 1m","free"]
os.system("git init")
for i in msg:
    os.system("echo %s > now"%i)
    os.system("cat /proc/%d/maps > procmaps"%pid)
    os.system("pmap %d > pmap"%pid)
    os.system("ps -p %d -o pid,cmd,sz,min_flt,maj_flt,rssize,size,vsize,pmem > ps"%pid)
    os.system("git add procmaps pmap ps now")
    os.system("git commit -m '%s'"%i)
    print("%s OK"%i)
    time.sleep(5)
    