import a
import c
import d
from a import makeup
def multiply (n , by=2) :
    return n * by

# print (multiply(1 , 2))
# print (multiply(2 , 2))
# print (multiply(3 , 2))
# print (multiply(4 , 2))
# print (multiply(5 , 2))
# print (multiply(6 , 2))
# print (multiply(7 , 2))
# print (multiply(8 , 2))
# print (multiply(9 , 2))
# print (multiply(10 , 2))
# print (multiply (11 , 2))
#
# n = 2
#
# for i in range(1, 11):
#     print(multiply(n , i))

#a loop

# i = 0
# while i < 10:
#     i = i + 1
#     print(multiply(i, 2))
#
# i = 0
# while i < 10:
#     i = i + 1
#     print(multiply(i , 3))
# for n in [2,20]:
#     for i in [10,9,8]:
#         print(multiply(n , i))
# i = 11
# while i > 0:
#     i = i - 1
#     print(multiply(i , 3))

# for n in range(1 , 21) :
#     if n % 3 == 1:
#         print("-----------")
#         print(n)
#         for i in range(1, 11):
#           print(multiply(n , i))

# i = 1
# while i < 20:
#     i = i + 3
#     print("-----------")
#     for n in range (1, 11):
#         print(multiply(n , i))

def array2():
    a = [1, 4,11]
    print(a)
    print(len(a))
    b = ["beth", "bath", "mohak", "maniac"]
    print(b)
    print(len(b))
    print(b[-1])
    c= []
    print(c)
    print(len(c))

    for s in b:
        print(s)
        print(len(s))
    n=5
    print("222222")
    for i in range (1, 11):
        print(multiply(n , i))
    print("hello")

    i = 2
    while i < 10:
       i = i + 1
       print(multiply(i , 2))

# array
def array1():
    alcohol = ["vodka" , "rum" , "tequilla"]
    print(alcohol)
    print(len(alcohol))

weather_data = ["sunny", "cloudy" , "maybe_some_snow" , "rain"]

def two_day_weather_report(first_day_weater, second_day_weather):
    first_day = "tomorrow will be " + first_day_weater
    second_day = "following day will be " + second_day_weather
    return first_day, second_day



if __name__ == "__main__":
    # print(two_day_weather_report(weather_data[0], weather_data[3]))
    # print(multiply(1, 2))
    # a.makeup()
    # a.hello()
    # makeup()
    #c.main()

    d.dictionary3()
#going to start commits


