import re
f = open(file="file\\baidu_x_system.log",mode='r+',encoding="utf-8")
data = f.read()
count={}
num=0
reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
#遍历查看data列表里面的所有ip
for ip in reip.findall(data):
    # print ("ip>>>", ip)
    #列表里相同的ip进行排序+1
    count[ip]=count.get(ip,0)+1
    # print(count[ip])

#获取每天的所有数量
R = count.items()
for i in R:
    if i[1] > 0:  # 提取出现次数大于0的IP
        # print(i)
        num += 1
        print(i)