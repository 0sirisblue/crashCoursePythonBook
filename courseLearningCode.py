# printing and formatting text
firstName = "alex"
lastName = "trebek"
fullName = firstName + " " + lastName
suckItTrebek = "Suck it, " + fullName.title() + "!"
print(suckItTrebek)
print("This\nis testing\nnew line making\n\t(also indentions)")


#removing spaces via strip
testVar = "  Efficiency "
print(testvar + "?")
testVar = testVar.strip()
print(testVar + "!")


#converting integers to strings
age = 23
message = "Happy " + str(age) + "rd birthday, jerk!"
print(message)


#using lists
whArmies = ["space marines", "grey knights", "imperial guard", "eldar", "dark eldar", "tau", "orks", "necrons"]
firstP = "The winner of our tournament today was playing an " + whArmies[2].title() + " army."
secondP = "Our second place player today was playing a " + whArmies[0].title() + " army."
thirdP = "Our third place player today was playing a " + whArmies[3].title() + " and " + whArmies[4].title() + " army."
print(firstP)
print(secondP)
print(thirdP)

#manipulating elements in lists
motorcycles = ["honda", "yamaha", "indian", "suzuki", "kawasaki", "harley"]
print(motorcycles)

motorcycles[3] = "ducati"
print(motorcycles)

motorcycles.append("bmw")
print(motorcycles)

motorcycles.insert(1,"kawasaki")
print(motorcycles)

del motorcycles[3]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print("The last motorcyle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcyle I owned was a " + first_owned.title() + ".")
print(motorcycles)

motorcycles.remove("kawasaki")
print(motorcycles)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive.title() + " is a bit too rich for my blood.")



guestList = ["albert einstein", "bill nye", "carl sagan", "neil degrasse-tyson"]

print("The guest of honor at my Science Dinner for the Ages, would obviously be " + guestList[0].title() + ", one of the greatest minds of all time.")
print(guestList[1].title() + " would obviously sit next to me, as he was the one who stoked the flames of my curiousity in my childhood.")
print("Obviously, the other popular educator and champion of Science of our day, " + guestList[3].title() + ", would be seated at the table.")
print("Finally, no dinner would be complete without " + guestList[2].title() + ", who is the forerunner to which all great science educators aspire.")

uninvitedGuest = guestList.pop() 
print("\nIn light of recent events, I have decided that " + uninvitedGuest.title() + " will not be attending.")
guestList.append("michio kaku")
print("The widely respected " + guestList[3].title() + " will be attending in his stead.")

guestList.insert(4, "ada lovelace")
print("I would like to invite " + guestList[4].title() + " as well, for her undeniable contributions to computing in our modern world.")

print(guestList)
print(sorted(guestList))
print(guestList)
guestList.reverse()
print(guestList)

headCount = len(guestList)
print("There are " + str(headCount) + " guests attending.")



locations = ["cairo", "london", "tokyo", "australia", "paris"]

for location in locations:
	print("I'd love to visit " + location.title() + " someday.")
	print("I hear " + location.title() + " is beautiful.\n")

print("I'll see them all, just you wait.")



pizzas = ["cheese", "white", "pepperoni", "mushroom"]

for pizza in pizzas:
	print("I sure do like " + pizza + " pizza.")

print("\nI guess you could say I really like pizza!\n")
print("\n\n")

animals = ["tigers", "foxes", "falcons"]

for animal in animals:
	print(animal.title() + " are one of my favorite animals.")

print("I'm not sure I could have any of these animals as pets, though.")



for value in range(1,5):
	print(value)

evennumbers = list(range(3,13,3))
print(evennumbers)
for number in evennumbers:
	print(number)

for value in range(1,11):
	print(value**2)

squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))
print(digits[-1])

squares = [value**2 for value in range(1,11)]
print(squares)

numbers = [number*2-1 for number in range(1,11)]
print(numbers)

for num1 in range(1,21):
	print(num1)

millions = list(range(1,1000001))
print(sum(millions))
print(min(millions))
print(max(millions))

oddNums = list(range(1,20,2))
for oddnum in oddNums:
	print(oddnum)

threes = list(range(3,31,3))
for three in threes:
	print(three)

cubes = [cubie**3 for cubie in range(1,11)]
print(cubes)



fruits = ["apples", "grapes", "oranges", "bananas", "pears"]
print(fruits)
print("\n")
print("Here are some of my favorite fruits:")
for fruit in fruits[-3:]:
	print(fruit.title())

juliafruits = fruits[:]
print(fruits)
print(juliafruits)
fruits.append("raspberries")
juliafruits.append("kiwis")
print(fruits)
print(juliafruits)

print("The first three items on the list are:\n" + str(fruits[:3]))
print("The middle items on the list are:\n" + str(fruits[1:4]))
print("The last three items on the list are:\n" + str(fruits[-3:]))


pizzas = ["cheese", "white", "pepperoni", "mushroom"]

for pizza in pizzas:
	print("I sure do like " + pizza + " pizza.")

print("\nI guess you could say I really like pizza!\n")
print("\n\n")

friendspizzas = pizzas[:]
pizzas.append("red pepper")
friendspizzas.append("hawaiian")

for pizza in pizzas:
	print("My favorite pizzas are " + pizza + " pizzas.")

print("\n")

for fpizza in friendspizzas:
	print("My friend's favorite pizzas are " + fpizza + " pizzas.")



#using tuples (much like a list but cannot be changed)
dimensions = (45, 150, 65)

print(dimensions[0])
print(dimensions[1])
print(dimensions[2])

print("Original Dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (25, 130, 100)

print("Updated Dimensions:")
for dimension in dimensions:
	print(dimension)

menuItems = ("steak", "bacon", "eggs", "hash browns", "biscuits")

print("Our current menu consists of the following:")
for menuItem in menuItems:
	print(menuItem.title())

menuItems = ("ham", "bacon", "eggs", "hash browns", "fresh fruit")

print("Our updated menu consitss of the following:")
for menuItem in menuItems:
	print(menuItem.title())

for menuItem in menuItems:



cars = ['audi', 'bmw', 'porsche', 'mercedes']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


myCar = 'Mazda'

if myCar.lower() == 'mazda':
    print('True')
else:
    print('Nope')


wantedCar = 'FordFocusRS'

if wantedCar != 'WRX':
    print('But have you seen the new WRX, bro?')



availableToppings = ['peppers', 'pepperoni', 'mushrooms', 'sausage', 'bacon', 'olives']

requestedToppings = ['peppers', 'bacon', 'feta']

if 'bacon' in availableToppings:
    print('You got it!')

else:
    print("Sorry Mac, we don't got that!")

for topping in requestedToppings:
    if topping in availableToppings:
        print(topping.title() + ", we got that!")
    else:
        print("Sorry Mac, we don't got " + topping + ".")
print("Fry, pizza going out, C'MON!")

#not in would be a valid comparison as well, it's more a structuring thing.

truck = 'Chevy'
van = 'Ford'

print('Is the van a Chevy?')
if van.lower() == 'chevy':
    print('Yep, like a rock.')
else:
    print('Nope, not a Chevy.')

print('Well, is the truck at least a Chevy?')
if truck.lower() == 'chevy':
    print('Yep, like a rock.')
else:
    print('Sorry pal, still not a chevy')



age = 19

print("You are " + str(age) + " years old.")
if age >= 18:
    print("Congratulations, you're old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("We're sorry, you're not old enough to vote yet.")

print('\n')


if age < 18:
    print("Sorry, young'en, you don't get to make any fun decisions yet.")
elif age < 21:
    print("Well, you can smoke now, and that's definitely bad for you. Congrats!")
else:
    print("Whoohoo, you can drink now. Go get 'em sport!")


age2 = 70

if age2 < 4:
    price = 0
elif age2 < 18:
    price = 5
elif age2 < 65:
    price = 10
elif age2 > 65:
    price = 8

print("Your cost of admission is " + str(price) + " dollars.") 



availableToppings = ['peppers', 'pepperoni', 'mushrooms', 'sausage', 'bacon', 'olives']

requestedToppings = ['peppers', 'bacon', 'feta']

for topping in requestedToppings:
    if topping in availableToppings:
        print(topping.title() + ", we got that!")
    else:
        print("Sorry Mac, we don't got " + topping + ".")



alien_color = "yellow"

if alien_color == "green":
    print("You just earned 5 points!")

alien_color = "green"

if alien_color == "green":
    print("You just earned 5 points!")


alien_color = "red"

if alien_color == "green":
    print("You shot down the green alien and got 5 points!")
elif alien_color == "yellow":
    print("You shot down the yellow alien and got 10 points!")
elif alien_color == "red":
    print("You shot down the red alien and got 15 points!")

age3 = 78

if age3 < 2:
    stageOfLife = "baby"
elif age3 < 4:
    stageOfLife = "toddler"
elif age3 < 13:
    stageOfLife = "kid"
elif age3 < 20:
    stageOfLife = "teenager"
elif age3 < 65:
    stageOfLife = "adult"
else:
    stageOfLife = "elder"

print("You are a " + str(stageOfLife) + ".")



faveFruits = ["apples", "bananas", "pears"]

if "apples" in faveFruits:
    print("I really like apples!")
if "oranges" in faveFruits:
    print("I really like oranges!")
if "cherries" in faveFruits:
    print("I really like cherries!")
if "bananas" in faveFruits:
    print("I really like bananas!")
if "pears" in faveFruits:
    print("I really like pears!")



# futurama pizza, final form!
availableToppings = ['peppers', 'pepperoni', 'mushrooms', 'sausage', 'bacon', 'olives']

requestedToppings = ['peppers', 'bacon', 'feta']

if requestedToppings:

    for topping in requestedToppings:
        if topping in availableToppings:
            print(topping.title() + ", we got that!")
        else:
            print("Sorry Mac, we don't got " + topping + ".")
else:
    print("One pie, nothing good on it.")

print("Fry, pizza going out, C'MON!")




usernames = ["admin", "fry", "amy", "leela", "hermes", "bender", "professor"]

if usernames:

    for username in usernames:
        if username == "admin":
            print("Greetings, Admin. System nominal. Logging in with elevated privileges.")
        else:
            print("Good morning, " + str(username.title()) + ". Logging in..." )

else:
    print("No users found. System entering standby.")




current_users = ["fry", "leela", "bender", "professor", "nibbler"]
new_users = ["amy", "hermes", "zoiberg", "bender", "nibbler"]

for potential_user in new_users:  
    if potential_user.lower() in current_users:
        print("We're sorry, the username " + str(potential_user) + " is already in use. Please try again.")
    else:
        print("Thanks, " + str(potential_user.title()) + ". Welcome to Planet Express!")



ordinalList = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for ordinal in ordinalList:
    if ordinal == 1:
        print(str(ordinal) + "st")
    elif ordinal == 2: 
        print(str(ordinal) + "nd")
    elif ordinal == 3:
        print(str(ordinal) + "rd")
    else:
        print(str(ordinal) + "th")



alien0 = {'color': 'green', 'points': 5}
alien1 = {'color': 'yellow', 'points': 10}
alien2 = {'color': 'red', 'points': 15}
alien3 = {'color': 'blue', 'points': 30}

totalPoints = 0
#incrementPoint() = totalPoints + 
#alienDestroyed(alienColor, points) = 


print(alien0['color'])
print(alien0['points'])

print ("You destroyed the " + str(alien0['color']) + " alien!")

totalPoints = totalPoints + alien0['points']
print("You have scored " + str(totalPoints) + " total points")


print(alien0)
alien0['xPosition'] = 0
alien0['yPosition'] = 25
print(alien0)

alien3['points'] = 20
print(alien3)

alien4 = {'xPosition': 0, 'yPosition': 25, 'speed': 'medium'}
print("\nOriginal x-position: " + str(alien4['xPosition']))

#Move the alien to the right.
#Determine how tar to move the alien based on its current speed.
if alien4['speed'] == 'slow':
    xIncrement = 1
elif alien4['speed'] == 'medium':
    xIncrement = 2
elif alien4['speed'] == 'fast':
    xIncrement = 3

#New position equals old position plus the increment
alien4['xPosition'] = alien4['xPosition'] + xIncrement

print("New x-position: " + str(alien4['xPosition']))

del alien0['yPosition']
print(alien0)



favoriteLanguages = {
    'britton': 'python',
    'andrew': 'c',
    'joel': 'ruby',
    'shawn': 'python',
    'james': 'sql',
    }

print("\nShawn's favorite language is " + favoriteLanguages['shawn'].title() + ".")
print("Joel's favorite language is " + favoriteLanguages['joel'].title() + ".")

brittonStats = {'hairColor': 'brown', 'eyeColor': 'green', 'favDessert': 'cheesecake', 'favBook': 'Lord of the Rings'}
print("That's him. The one over there with the " + str(brittonStats['hairColor']) + " hair.")
print("If you want his attention, feed him " + str(brittonStats['favDessert']) + ", and ask him about " + str(brittonStats['favBook']) + ".")

glossary = {
    "variable": "this is a structure for easily naming, storing, and recalling data",
    "function": "this is a series of instructions the program will execute, that can easily be reused",
    "print": "a function that outputs information to the user's screen for display",
    "list": "a function that stores a series of values for manipulation or recall",
    "if": "a crucial function that allows your program to make a decision based on given data"
    }

#this is clunky as hell. do not do this next bit IRL unless REALLY needed
print("variable - " + str(glossary["variable"]))
print("function - " + str(glossary["function"]))



user0 = {
    'callsign': 'maverick',
    'first': 'pete',
    'last': 'mitchell',
    'status': 'active',
}

for key, value in user0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("\n")

for key, value in user0.items():
    print(key.title() + " - " + value.title())


favoriteLanguages = {
    'britton': 'python',
    'andrew': 'powershell',
    'joel': 'ruby',
    'shawn': 'python',
    'james': 'sql',
    }

for name, language in favoriteLanguages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

for name in favoriteLanguages.keys():
    print(name.title())

print("\n")

friends = ['joel', 'james']
for name in favoriteLanguages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + 
            favoriteLanguages[name].title() + "!") 

if 'zach' not in favoriteLanguages.keys():
    print("\nZach, please take my poll.\n")


for name in sorted(favoriteLanguages.keys()):
    print(name.title() + " thank you for taking the poll.")


print("The following languages have been mentioned as favorites:")
for language in favoriteLanguages.values():
    print(language.title())

print("\n")

print("The following languages have been mentioned as favorites:")
for language in set(favoriteLanguages.values()):
    print(language.title())

print("\n")



glossary = {
    "variable": "this is a structure for easily naming, storing, and recalling data",
    "function": "this is a series of instructions the program will execute, that can easily be reused",
    "print": "a function that outputs information to the user's screen for display",
    "list": "a function that stores a series of values for manipulation or recall",
    "if": "a crucial function that allows your program to make a decision based on given data",
    "dictionary": "this is a structure that stores a two pieces of info, keys and values",
    "set": "this is a method that is used to form a unique grouping of values in a dictionary",
    }

for noun in glossary.keys():
    print(noun.title() + " - " + glossary[noun])


for word in sorted(glossary.keys()):
    print(word.title() + " - " + glossary[word] + ".")


print("\n")


riverLoc = {"nile": "egypt", "amazon": "brazil", "mississippi": "us",}

for river in sorted(riverLoc.keys()):
    if river == "mississippi":
        print("The " + river.title() + " runs through the " + riverLoc[river].upper() + ".")
    else:
        print("The " + river.title() + " runs through " + riverLoc[river].title() + ".")

print("\n")


favUnitRegister = {
    "zero": "hacker",
    "grenzer": "sniper",
    "intruder": "lieutenant",
    "iguana": "tag",
}

for unit in favUnitRegister.keys():
    if unit == "iguana":
        print("I really like the " + unit.title() + ", it's a great medium " + favUnitRegister[unit].upper() + ".")
    else:
        print("I really like the " + unit.title() + ", it's got a great " + favUnitRegister[unit].title() + " profile.")

print("\n")

print("Some of my favorite unit types in Infinity are:")
for favUnit in favUnitRegister.values():
    print(favUnit.title() + "s")


favoriteLanguages = {
    'britton': 'python',
    'andrew': 'powershell',
    'joel': 'ruby',
    'shawn': 'python',
    'james': 'sql',
    'bob': 'python',
    }

for language in set(favoriteLanguages.values()):
    print(language.title())

print("\n")


respondents = ['britton', 'zach', 'andrew', 'joel', 'shawn', 'james', 'tyler', 'bob']

for respondent in respondents:
    if respondent in favoriteLanguages.keys():
        print("Thank you, " + respondent.title() + ", for answering " + favoriteLanguages[respondent].title() + " in our poll.")
    else:
        print(respondent.title() + ", please take our poll at your earliest convenience.")



alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alienNumber in range(30):
    newAlien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(newAlien)

for alien in aliens[:5]:
    print(alien)
print('...')

print("The total number of aliens created is " + str(len(aliens)) +".")
print('...')

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print('...')


