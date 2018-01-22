car = 'bmw'
print("Is the car == bmw ? I predict True.")
print(car == 'bmw')
print("Is the car == mitsubishi ? I predict False.")
print(car == 'mitsubishi')

idol = 'Shirai'
print("\nIs the idol == shirai ? I predict False.")
print(idol == 'shirai')
print("Is the idol == Shirai ? I predict True.")
print(idol == 'Shirai')

age = 21
print("\nIs the age < 18 ? I predict False.")
print(age < 18)
print("Is the age >= 21 ? I predict True.")
print(age >= 21)

number = 48
print("\nIs the number > 45 ? I predict True.")
print(number > 30)
print("Is the number > 50 ? I predict False.")
print(number > 50)

grade = 100
print("\nIs the grade <= 90 ? I predict False.")
print(grade <= 90)
print("Is the grade == 100 ? I predict True.")
print(grade == 100)

#Assignment 5-2: More Conditional Tests

girl = 'ayami'
print("\nIs the girl != ayami ? I predict False.")
print(girl != 'ayami')
print("Is the girl == ayami ? I predict True.")
print(girl == 'ayami')

brand = 'Microsoft'
print("\nIs the brand == microsoft ? I predict False.")
print(brand == 'microsoft')
print("Is the brand == microsoft ? I predict True, if given a set of proper conditions.")
print(brand.lower() == 'microsoft')

lucky_number = 19
print("\nIs the lucky number != 21 ? I predict True.")
print(lucky_number != 21)
print("Is the lucky number == 19 ? I predict True.")
print(lucky_number == 19)
print("Is the lucky number <= 20 ? I predict True.")
print(lucky_number <= 20)
print("Is the lucky number > 50 ? I predict False.")
print(lucky_number > 50)
print("Is the lucky number >= 19 ? I predict True.")
print(lucky_number >= 19)
print("Is the lucky number < 19 ? I predict False.")
print(lucky_number < 19)

food_0 = 'pizza'
food_1 = 'pasta'
print("\nI think you ordered a pizza and pasta.")
print(food_0 == 'pizza' and food_1 == 'pasta')
print("Or did you order a pizza and a soda ? Wait, that can't be right.")
print(food_0 == 'pizza' and food_1 == 'soda')

amount_0 = 50
amount_1 = 25
print("\nThe condition will be true if the first amount >= 30 or second amount >=26")
print(amount_0 >= 30 or amount_1 >=26)
print("The condition will be false if the first amount < 50 or second amount < 25")
print(amount_0 < 50 or amount_1 < 25)

lottery_winners = [256, 745, 9104]
print("\nMy lottery ticket number is 745. I won the lottery.")
print(745 in lottery_winners)
print("Your lottery ticket number is 4848. You didn't win the lottery.")
print(4848 in lottery_winners)
