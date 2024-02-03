import os
import csv
import datetime

if __name__=="__main__":
    fp=os.getcwd()
    outfs=os.path.join('..',f"合并文件_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.csv")
    timer=0
    with open(outfs,encoding='gbk',mode='w+') as wtr:
        for root,dirs,files in os.walk(fp):
            for fs in files:
                if fs.lower().endswith('.csv'):
                    absfp=os.path.join(root,fs)
                    data=csv.reader(open(absfp), delimiter=',')
                    if timer>=1:
                        next(data)
                    for d in data:
                        wtr.write(','.join(d))
                        wtr.write('\n')
                    timer+=1
    wtr.close()
