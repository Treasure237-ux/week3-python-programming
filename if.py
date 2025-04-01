# temperature = 12

# if temperature >= 20:
#     print("its a hot day")
# elif temperature >= 10:
#     print("its a warm day")
# elif temperature >= 0:
#     print("its a cold day")
# else:
#    print("its a freezing day")

#loop
# count = 1

# while count <= 5:
#     print(count)
#     count += 1

#function
# def add(a, b):
#     sum = a + b
#     print(sum)
# add(108, 335)

li_of_int = [int(input("insert first num:")), int(input("insert second num:")), int(input("insert third num:")), int(input("insert fourth num:")) ]
print(f'your list of intergers include: {li_of_int}')
# list1 = li_of_int[0]
# list2 = li_of_int[1]
# list3 = li_of_int[2]
# list4 = li_of_int[3]
list = li_of_int[0] + li_of_int[1] + li_of_int[2] + li_of_int[3]
print(f'sum of values in list: {list}')
for list1 in li_of_int:
    print(list1)
