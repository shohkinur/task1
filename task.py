list_of_apples = [12,4,7,9,-12,-5,10]
list_of_eggs = [1,4,5,12,19]
list_of_flour = [12,4,-5,1]

sum_of_apples=sum(list_of_apples)
sum_of_egg=sum(list_of_eggs)
sum_of_flour=sum(list_of_flour)

apple_count_pies=int(sum_of_apples/4)
egg_count_pies= int(sum_of_egg/2)
flour_count_pies=int(sum_of_flour/0.5)


if apple_count_pies<egg_count_pies<flour_count_pies:
    print(apple_count_pies, "pies can be cooked")
elif egg_count_pies<flour_count_pies<apple_count_pies:
    print (egg_count_pies, "pies can be cooked")
else:
    print(flour_count_pies, "pies can be cooked")



if apple_count_pies>egg_count_pies>flour_count_pies:
    print("As", apple_count_pies, "pies can be cooked according to number of apples")
    number_ofegg=(apple_count_pies-egg_count_pies)*2
    number_offlour = (apple_count_pies-flour_count_pies)*0.5
    print("We need", number_offlour, " more flour and ", number_ofegg, "more eggs to cook", apple_count_pies, "pies")
elif egg_count_pies>flour_count_pies>apple_count_pies:
    print("As", egg_count_pies, "pies can be cooked according to number of eggs")
    number_ofapp=(egg_count_pies-apple_count_pies)*4
    number_offlour = (egg_count_pies-flour_count_pies)*0.5
    print("We need", number_offlour, " more flour and ", number_ofapp, "more eggs to cook", egg_count_pies, "pies")
else:
    print("As", flour_count_pies, "pies can be cooked according to number of flour")
    number_ofapp = (flour_count_pies-apple_count_pies)*4
    number_ofegg=(flour_count_pies-egg_count_pies)*2
    print("We need", number_ofapp, " more apples and ", number_ofegg, "more eggs to cook", flour_count_pies, "pies")

   


