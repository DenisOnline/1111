var_1 = 15
FULL_HD = [1920, 1080]#константа
def fun_1():
    var_1 = 10
    def second():
        nonlocal var_1
        var_1 = 1
        global var_2
        var_2 = 2
    second()
    print(var_1)

# def print(var_1):
#     pass

fun_1()
print(var_1)