n_p_d = input().split()
#處理第一行
n = int(n_p_d[0])
p = int(n_p_d[1])
d = int(n_p_d[2])

#處理輸入的x,y,人數
data = {} #先創一個dictionary存資料
for i in range(1,n+1):
    x_y_p = input().split()
    data[str(i)] = x_y_p #因為數字不能當dict的key所以要先轉成str
    #print(data)

#先判斷每個地方建基地台會涵蓋到哪些城市
import math
distance_dict = {}
for j in range(1,n+1):
    my_dist_x = int(data[str(j)][0]) #取出x
    my_dist_y = int(data[str(j)][1]) #取出y
    distance_dict[str(j)] = [str(j)]
    for k in range(1,n+1):
        dist_x = int(data[str(k)][0]) #別人的x
        dist_y = int(data[str(k)][1]) #別人的y
        distance = ((my_dist_x-dist_x)**2+(my_dist_y-dist_y)**2)**0.5
        #print(distance)
        if distance <= d and distance != 0:
            distance_dict[str(j)].append(str(k))
print(distance_dict)

#設立一個函數去找出當下涵蓋做多人的基地台設置點
totalpeople = 0
ans_list = []
def people_num():
    max_p = 0
    for ct in distance_dict:
        pnum=0
        for value in distance_dict[ct]:
            pnum += int(data[value][2])
        if pnum > max_p:
            max_city = ct
            max_p = pnum
    return [max_p, max_city] #回傳地點&涵蓋人數

#做p次
for l in range(1,p+1):
    result = people_num()
    totalpeople += result[0]
    ans_list += result[1]
    #print(totalpeople,ans_list)
    for cts in distance_dict[result[1]]: #去除已涵蓋的地點的人口
        data[cts][2] = 0

ans_str = " ".join(ans_list)
ans_str += " " 
ans_str += str(totalpeople)
print(ans_str)


