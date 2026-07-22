numbers =[1,2,3,4,5,6,7,8,9,10]

numbers_com = [x for x in numbers if x>5 ]
print(numbers_com)

dict_com ={ x: (True if x%2==0 else False )for x in numbers }
print(dict_com)
