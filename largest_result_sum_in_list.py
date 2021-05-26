res = -1
my_list = [[1, 2, 3], [2, 3, 3], [1, 3, 3]]
for i in range(len(my_list)):
    total_sum = 0
    for j in range(len(my_list[i])):
        
        total_sum += my_list[i][j]
    #print(sum)
    if res < total_sum:
        res = total_sum
        res_1 = i
print(res_1)
