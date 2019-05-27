#enconding:utf-8
import csv
import re
from zejun.init import *
import os
import os
rootdir = r'C:\Users\Administrator\Desktop\1234'
list_file = os.listdir(rootdir)
for list_num in range (0,len(list_file)):
    file_name = os.path.join(rootdir,list_file[list_num])
    print(file_name)
    articles = []
    sum_articles = []
    CpuMinIdles_articles = []
    rxdrops_articles = []
    new_articales = []
    limit_mem_number = need_number.limit_mem_num
    limit_cpu_number = need_number.limit_cpu_num
    limit_rxdrop_number = need_number.limit_rxdrop_numb
    csv_file = csv.reader(open(file_name,'r',))
    for i,rows in enumerate(csv_file):  #i 代表第几行 rows代表行内容
        use_mem_maxs = rows[6].split(':',0) #字符串类型 切割字符串
        CpuMinIdles = rows[4].split(':',0)
        rxdrops = rows[24].split(':',0)
        for rxdrops_list in rxdrops:
            rxdrop = re.findall('\d+\.\d+',rxdrops_list)
            for rxdrops_number in rxdrop:
                if float(rxdrops_number) >= limit_rxdrop_number:
                    max_swap = i
                    rxdrops_articles.append(i)
                    #print(rxdrops_articles)
        for CpuMinIdles_list in CpuMinIdles:
            CpuMinIdle = re.findall('\d+\.\d+',CpuMinIdles_list)
            for CpuMinIdle_number in CpuMinIdle:
                if float(CpuMinIdle_number) <= limit_cpu_number:
                    Cpu_number = i
                    CpuMinIdles_articles.append(i)
                    print(CpuMinIdles_articles)
        for j in use_mem_maxs:
            use_mem_max = re.findall('\d+',j) #提取出数字
            for k in use_mem_max:
                if int(k) > limit_mem_number:
                    mem_num = i
                    articles.append(mem_num)
                sum_articles = list(set(articles + rxdrops_articles + CpuMinIdles_articles ))
                for c in range(0,len(sum_articles)):
                    if i == sum_articles[c]:
                        mem_max = k + '%'
                        use_ip = rows[0]
                        CpuMinIdle = rows[4]
                        MemMaxUseTime = rows[7]
                        MaxSwapPageInMemory = rows[9]
                        DiskReadMax = rows[12]
                        DiskReadMaxTime = rows[13]
                        DiskWriteMax = rows[14]
                        DiskWriteMaxTime = rows[15]
                        NetworkRxTime = rows[16]
                        RxIface = rows[17]
                        MaxRx = rows[18]
                        NetworkTxTime =rows[19]
                        TxIface = rows[20]
                        MaxTx = rows[21]
                        NetworkEDEVRxTime= rows[22]
                        EDEVRxIface = rows[23]
                        rxdrop = rows[24]
                        NetworkEDEVTxTime = rows[25]
                        EDEVTxIface = rows[26]
                        txdrop = rows[27]
                        plist_sz = rows[28]
                        #print(use_ip)
                        new_articales.append([use_ip,mem_max,CpuMinIdle,rxdrop,MemMaxUseTime,MaxSwapPageInMemory,DiskReadMax,DiskReadMaxTime,DiskWriteMax,
                                              DiskWriteMaxTime,NetworkRxTime,RxIface,MaxRx,NetworkTxTime,TxIface,MaxTx,EDEVRxIface,NetworkEDEVTxTime,
                                              EDEVTxIface,txdrop,plist_sz])

    with open('sum_information.csv',"a+",encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['use_ip','mem_max','CpuMinIdle','rxdrop''MemMaxUseTime','MaxSwapPageInMemory','DiskReadMax','DiskReadMaxTime','DiskWriteMax',
                                          'DiskWriteMaxTime','NetworkRxTime','RxIface','MaxRx','NetworkTxTime',
                                          'TxIface','MaxTx','EDEVRxIface','NetworkEDEVTxTime','EDEVTxIface','txdrop','plist_sz'])
        for row in new_articales:
            writer.writerow(row)


