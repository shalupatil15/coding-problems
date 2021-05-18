def my_First_function():
    str = "my name is khaan".split()
    str2 = [1,2]
    str3 = 1
    my_list = [n[0] for n in str ]
    print(type(my_list))
    print(type(str2))
    print(type(str3))
    return(my_list)
    




my_return = my_First_function()
print(type(my_return))
print(my_return)