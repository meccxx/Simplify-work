class number:
    def __init__(self,limit,limit_mem_num,limit_cpu_num,limit_rxdrop_num):
        self.limit =  limit                 #初始化
        self.limit_mem_num = limit_mem_num  #初始化变量cpu阀值
        self.limit_cpu_num = limit_cpu_num  #初始化变量men阀值
        self.limit_rxdrop_numb = limit_rxdrop_num

    def print_mem_num(self):
        print( "limit num : " +  self.limit_mem_num)
    def print_cpu_nem(self):
        print("limit num : " +  self.limit_cpu_num)
    def print_rxdrop_num(self):
        print("limit num :" + self.limit_rxdrop_numb)

need_number = number("limit",80,10,1)  #第一个值代表cpu阀值，第二个值代表men阀值