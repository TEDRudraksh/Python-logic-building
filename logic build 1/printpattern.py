# *
# **
# ***
# ****
# *****


def pattern():
    for i in range(1,6):
        print("*"*i)
# pattern()

# 1
# 12
# 123
# 1234
# 12345

def pattern2():
    for i in range(1,6):
        for j in range(1,i +1):
            print(j, end=" ")
        print()
# pattern2()


# *****
# ****
# ***
# **
# *  


def pattern3():
    # rows = int(input("enter the row"))
    for i in range(5,0,-1):
        print("*"*i)

# pattern3()


#     *
#    ***
#   *****
#  *******
# *********

def pattern4():
    for i in range(1,6):
        spaces = 6 - i
        stars = 2*i - 1
        print(" " * spaces + "*"* stars)
# pattern4()



# Input: 4
# Output:
# 1234
# 123
# 12
# 1

def pattern5():
    # rows = int(input("enter the rows"))
    for i in range(5,0,-1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()
# pattern5()


# Input: 4
# Output:
# 1234
# 1234
# 1234
# 1234

def pattern6():
    for i in range(1,5):
        for j in range(1,5):
            print(j,end=" ")
        print()
# pattern6()



# Input: 5
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def pattern7():
    num = 1
    for i in range(1,5):
        for j in range(1,i+1):
            print(num,end=" ")
            num += 1
        print()
# pattern7()


# def pattern8():
#     n = 5
#     for i in range(5):
#         for j in range(i+1):
#             print(" ", end=" ")
#         for j in range(i,n):
#             print("*", end=" ")

#         print()
# pattern8()

def pattern9():
    n = 6
    for i in range(1,n):
        space = i
        star = n - i
        print(" "*space + "*"*star)

# pattern9()




#diamond pattern

def pattern10():
    n = 5
    for i in range(n):
        space = n - i
        star = 2*i + 1
        print(" "*space + "*"*star)
    for i in range(n-2,-1,-1):
        star= 2*i + 1
        space = n - i
        print(" "*space + "*"*star)
    
        

pattern10()