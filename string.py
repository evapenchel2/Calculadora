#lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#friends2 = friends.copy()

#print(friends2)

#tuple

#coordinates = [(4, 5), (6, 7), (80, 34)]
#coordinates[1] = 10
#print(coordinates[1])

#def say_hi(name, age ):
    #print("Hello " + name, ", you are " + str(age))

#say_hi("Mike", "35")
#say_hi("Steve", "70")

#def cube(num): 
   # return num*num*num

#result = cube(4)
#print(result)

#is_male = False
#is_tall = True

#if is_male and is_tall:
#    print("You are a tall male")
#elif is_male and not (is_tall):
#    print("You are a short male")
#elif not (is_male) and is_tall:
#    print("You are not a male but are tall")
#else:
#    print("You are a not male and not tall")

#def max_num(num1, num2, num3):
    #if num1 >= num2 and num1 >= num3:
    #    return num1
   # elif num2 >= num1 and num2 >= num3:
  #      return num2
 #   else: 
#        return num3
#    print(max_num(300, 40, 5))

#num1 = float(input("Enter first number: "))
#op = input("Enter operator: ")
#num2 = float(input("Enter second number: "))

#if op == "+":
#    print(num1 + num2)
#elif op == "-":
#    print(num1 - num2)
#elif op == "/":
#    print(num1 / num2)
#elif op == "*":
#    print(num1 * num2)
#else: 
#    print("Invalid operator")

#monthConversion = {
   # "Jan": "January",
   # "Feb": "February",
   # "Mar": "March",
   # "Apr": "April",
   # "May": "May",
   # "Jun": "June",
   # "Jul": "July",
   # "Aug": "August",
   # "Sep": "September",
   # "Oct": "October",
    #"Nov": "November,"
    #"Dec": "December"

#}

#print(monthConversion.get("Dec"))

i =1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")