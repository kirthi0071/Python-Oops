numbers =[1,2,3,4,5,6,7,8,9,10]

numbers_com = [x for x in numbers if x>5 ]
print(numbers_com)

dict_com ={ x: (True if x%2==0 else False )for x in numbers }
print(dict_com)

numbers = [10, 15, 20, 25, 30, 35, 40]


key = {}

for x in numbers:
    if x%10==0:
        key[x]=True
    else:
        key[x]=False
print(key)

div ={x: (True if x%10==0 else False) for x in numbers}
print(div)


temps = [15, 22, 28, 33, 10, 40, 25]

result = {}

for temp in temps:
    if temp>25:
        result[temp] ="Hot"
    else:
        result[temp] ="cold"
print(result)

temp_dic = {temp: ("Hot" if temp>25 else "Cold") for temp in temps}
print(temp_dic)
