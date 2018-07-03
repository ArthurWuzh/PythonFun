
import  random

list1 = [i for i in range(20)]
random.shuffle(list1)  # 把一个序列打乱
group_list = [list1[i:i+3] for i in range(0,len(list1),3)]  # 切片为3 ,步长为3
print(group_list)