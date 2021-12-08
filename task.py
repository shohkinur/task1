list_of_apples = [12,4,7,9,-12,-5,10]
list_of_eggs = [1,4,5,12,19]
list_of_flour = [12,4,-5,1]

sum1=0
for i in list_of_apples:
    sum1+=i
print("Sum of apples is ", sum1)

sum2=0
for j in list_of_eggs:
    sum2+=j
print("Sum of eggs is ",sum2)

sum3=0
for y in list_of_flour:
    sum3+=y
print("Sum of flour is ",sum3)

number1=int(sum1/4)
number2= int(sum2/2)
number3=int(sum3/0.5)


print( number1, " pies can be cooked from apples")
print(number2, "pies can be cooked from eggs")
print(number3, "pies can be cooked from flour")


if number1<number2<number3:
    print(number1, "pies can be cooked")
elif number2<number3<number1:
    print (number2, "pies can be cooked")
else:
    (number3, "pies can be cooked")



if number1>number2>number3:
    print("As", number1, "pies can be cooked according to number of apples")
    number_ofegg=(number1-number2)*2
    number_offlour = (number1-number3)*0.5
    print("We need", number_offlour, " more flour and ", number_ofegg, "more eggs to cook", number1, "pies")
elif number2>number3>number1:
    print("As", number2, "pies can be cooked according to number of eggs")
    number_ofapp=(number2-number1)*4
    number_offlour = (number2-number3)*0.5
    print("We need", number_offlour, " more flour and ", number_ofapp, "more eggs to cook", number2, "pies")
else:
    print("As", number3, "pies can be cooked according to number of flour")
    number_ofapp = (number3-number1)*4
    number_ofegg=(number3-number2)*2
    print("We need", number_ofapp, " more apples and ", number_ofegg, "more eggs to cook", number3, "pies")

   

