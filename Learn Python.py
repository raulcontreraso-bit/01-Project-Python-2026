 
#  #
# # Learn Python
# #

# #
# # Print Statement and Programflow
# #
# print('Welcome to Python 101!2')
# print('Welcome to Python 101!')
# print("Create nails")
# print("Create hammer")
# print("Use hammer and nails")
# print()

# #
# # Variables
# #
# failed_subjects="2"
# name='John'
# print('Dear Mrs Badger')
# print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
# print(name + '  will need to redo ' + failed_subjects + '  courses.')
# name="Eric"
# print(name + '  is doing well in geography.')



# # Datatypes & Typecasting
# # Integer fload boolean

# failed_subjects=2.45  
# name='John'
# #Boolean True or False
# a="it's"
# b='it\'s'
# print('Dear Mrs Badger')
# #print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
# #print(name + '  will need to redo ' + failed_subjects + '  courses.')
# name="Eric"
# print(name + '  is doing well in geography.')




# print()
# print('# Datatypes & Typecasting:___________________  ') 
# failed_subjects=2.56
# name='John'
# print('Dear Mrs Badger')
# print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')
# print(name + '  will need to redo ' + str(failed_subjects) + '  courses.')
# name="Eric"
# print(name + '  is doing well in geography.')
# print(type('hello'))
# print(type(1))
# print(type(1.64))
# print(type(True))

# #
# # Variables & Datatypes - Exercise
# #
# print('Variables & Datatypes - Exercise')
# #Create appropriate Variables for Item name, the price 
# #and how many you have in stock

# item_name = 'widget'
# price = 23.5
# inventory = 100
# is_in_inventory = True
# print(item_name, price, inventory)





# # 
# # Learn Python
# # Arcade Day Pass Challenge
# #

# # 🕹️ Arcade Day Pass Tracker — Challenge Steps
# #
# # 1) Create variables to store:
# #    - customer name
# #    - number of passes
# #    - tokens per pass
# #    - price per pass
# #    - tokens required per game
# #
# # 2) Calculate:
# #    - total tokens
# #    - total cost
# #    - games available  (use 'floor division' to get a whole number)
# #
# # 3) Print a summary with:
# #    - customer name
# #    - passes bought
# #    - total tokens
# #    - total cost
# #    - games available


# # Variables
# customer_name = "Guil"
# passes_bought = 3
# tokens_per_pass = 30
# pass_price = 15.00
# tokens_per_game = 3

# # Calculations
# total_tokens = passes_bought * tokens_per_pass
# total_cost = passes_bought * pass_price
# games_available = total_tokens // tokens_per_game

# print("===== ARCADE DAY PASS =====")
# print("Customer:", customer_name)
# print("Passes:", passes_bought)
# print("Tokens:", total_tokens)
# print(f"Total Cost: ${total_cost:.2f}")
# print("Games Available: " + str(games_available))







# #
# # Learn Python
# # User Input

# name= input('What is your name?: ')
# age=input('What is your age?: ')
# print('Hello '+ name + '! You are '+ age + ' years old.')

# num1=input('Enter a digit: ')
# num2=input('Enter a second number:')
# answer=float(num1)+float(num2)
# print(answer)



# #
# # 
# # User Input - Exercise
# #

# # - Create a distance converter converting Km to miles
# # - Take two inputs from user: Their first name and the distance in km
# # - Print: Greet user by name and show km, and mile values
# # - 1 mile is 1.609 kilometers
# # - hint: use correct types for calculating and print
# # - Did you capitalize the name

 

# # - Create a distance converter converting Km to miles
# # - Take two inputs from user: Their first name and the distance in km
# # - Print: Greet user by name and show km, and mile values
# # - 1 mile is 1.609 kilometers
# # - hint: use correct types for calculating and print
# # - Did you capitalize the name
# name = input('Enter your name: ')
# distance_km = input('Enter distance in km: ')
# distance_mi = float(distance_km)/1.609
# print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')





# #
# # Learn Python Arithmetic operations
# #
# a=6
# b=2

# a=10
# b=3


# print('Addition : ', a + b)
# print('Subtraction : ', a - b)
# print('Multiplication : ', a * b)
# print('Division (float) : ', a / b)
# print('Division (floor) : ', a // b)
# print('Modulus : ', a % b)
# print('Exponent : ', a ** b)


# #
# # Learn Python  Strings -Basics / Slicing
# #

# msg='welcome to Python 101: Strings'
# print(msg)
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())



# msg='welcome to it\'s Python 101: Strings'
# print(msg)
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())


# msg='welcome to Python 101: Strings'
# print(msg)
# print(len(msg))


# msg='welcome to Python 101: Strings'
# print(msg)
# print(len(msg))
# print(msg.count('o'))



# msg='welcome to Python 101: Strings'
#     #012345678
# print(msg)
# #slicing
# print(msg[-1])
# print(msg[2:])
# #slicing
# print(msg[2:7])


 
# # Learn Python
# # Exercise- Strings - Basics / Slicing

# msg='welcome to Python 101: Strings'
# msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
# print(msg1.title())
# print(msg1[::-1].title())



# #
# # Strings-2 Find/replace, string formatting
# #

# #msg="""Dear Terry,,
# #You must cut down the mightiest 
# #tree in the forest with…
# #a herring! <3"""
# #print(msg)

# msg='Welcome to Python 101: Strings'
# print(msg.replace('Python','C'))
# msg1=msg.replace('Python','C')
# print(msg1)


# msg='Welcome to Python 101: Strings'
# print('Python' in msg)

# msg='Welcome to Python 101: Strings'
# print('Python' not in msg)


# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color + '!'
# print(msg)


# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color + '!'
# msg1 = f'[{name}] loves the color {color.lower()}!'
# print(msg)



# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)


# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)

 
 




#
# Learn Python Pit Stop Timing Optimizer Challenge

# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"





# # 🏁 Pit Stop Timing Optimizer 🔧
# #
# # 1. Ask the user for the total race time in seconds.
# # 2. Ask how many pit stops were made.
# # 3. Ask for the average pit stop duration (in seconds).
# #
# # Then:
# # - Calculate the total pit stop time.
# # - Calculate the percentage of the race spent in the pits.
# # - Round the percentage to 2 decimal places.
# #
# # Finally, print all of the following:
# # - Total pit stop time in seconds
# # - Percentage of race time spent in pits
# # - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

# # Collect inputs
# total_race_time = float(input("Enter total race time (in seconds): "))
# num_pit_stops = int(input("Enter number of pit stops: "))
# avg_pit_duration = float(input("Enter average pit stop duration (in seconds): "))

# # Calculate total pit time
# total_pit_time = num_pit_stops * avg_pit_duration

# # Calculate pit time percentage
# pit_percentage = (total_pit_time / total_race_time) * 100
# pit_percentage = round(pit_percentage, 2)

# # Print results
# print("\n--- Pit Stop Summary ---")
# print(f"Total pit stop time: {total_pit_time} seconds")
# print(f"Percentage of race in pits: {pit_percentage}%")

# # Optional feedback
# if pit_percentage > 5:
#     print("You need a new pit crew. 🛠️")



# #   
# # Learn Python  Lists- Basics
# #
# friends = ['John','Michael','Terry','Eric','Graham']
# #            0       1           2
# print(friends)

# friends = ['John','Michael','Terry','Eric','Graham']

# print(friends[1],friends[4])
# print(friends[-1])

# friends = ['John','Michael','Terry','Eric','Graham']

# print(friends[1],friends[4])
# print(friends[2:4])
# print(friends[:4])
# print(friends[:])

# print(len(friends))
# print(friends.index('Eric'))
# print(friends.count('Eric'))

# print(friends[1],friends[4])
# print(len(friends))
# print(friends.index('Eric'))





#
# Learn Python Lists- continued
# # 

# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# print(friends)
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()
# print(friends)



# print('-.......................')
# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# print(friends)
# cars.sort()
# print(cars)
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()
# print(friends)

# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# print(friends)
# print(sum(cars)) # min  . Max  


# friends = ['John','Michael','Terry','Eric','Graham']
# cars = [911,130,328,535,740,308]
# #friends.append('TerryG')
# #friends.insert(1,'TerryG')
# #friends[2]='TerryG'
# friends.extend(cars)
# friends.remove('Terry')
# friends.pop(-1)
# #friends.clear()
# #del friends
# #del friends[2]
# print(friends)
# #new_friends = friends[:]
# #new_friends = friends.copy()
# new_friends = list(friends)
# print(new_friends)




# Learn Python Lists - Exercise


# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# new_day = input('Enter #of lemonades for new day: ')
# sales_w2.append(int(new_day))
# #sales.extend(sales_w1)
# #sales.extend(sales_w2)
# sales = sales_w1 + sales_w2
# #sales.sort()
# worst_day_prof = min(sales) * 1.5
# best_day_prof = max(sales) * 1.5
# print(f'Worst day profit:$ {worst_day_prof}')
# print(f'Best day profit:$ {best_day_prof}')
# print(f'Combined profit:$ {worst_day_prof + best_day_prof}')





# # Learn Python Split and Join


# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(msg.split())


# msg ='Welcome  to  Python  101: Split  and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(msg.split())
# print(msg.split(' '))
# print(msg.split(' '), type(msg.split(' ')))
# print(csv.split(','))
# print('-'.join(friends_list))
# print(''.join(msg.split()))

# # print(msg.replace(' ', ''))




# # Learn Python
# # Split and Join - Exercise


# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'


# friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
# print(friends_list)


# print('replace', csv.replace(';',',').replace(':',',').split(','))
# # From the list above fill a list(friends_list) properly
# # with the names of all the friends. One per "slot"
# # you may need to run same command several times
# # use print() statements to work your way through the exercise




# Learn Python Tuples

#Tuples - faster Lists you can't change
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends[2:4])
print(friends_tuple[2:4])



# Learn Python Sets

#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends)
print(friends_tuple)
print(friends_set)




#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.intersection(my_friends_set))

print(friends_set.union(my_friends_set))

print(friends_set.intersection(my_friends_set))

print(friends_set.difference(my_friends_set))

print(friends_set.union(my_friends_set))


#Sets - blazingly fast unordered Lists 
#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()





# Learn Python Sets-Exercises
friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends

print('Eric' in friends and 'John' in friends)


#2. combine or add the two sets 
print(friends.union(my_friends))
print(friends | my_friends)




#3. Find names that are in both sets
print(friends.intersection(my_friends))
print(friends & my_friends)



#4. find names that are only in friends
print(friends.difference(my_friends))
print(friends - my_friends)


#5. Show only the names who only appear in one of the lists
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)





#6. Create a new cars-list without duplicates
cars_no_dupl =set(cars)
print(cars_no_dupl)



# # Learn Python Comments

# #Entry form for Ministry applications
# #to-do: fix it! it doesn’t work  
# name = "Default"
# name = input(Enter your silly name: )
# print("Thank you " + name + "!")
# print("for applying to")
# print("the Minstry of Silly Walks")

 



# Learn Python Functions - Calling ,parameters, arguments, defaults

def greeting(name,age=28):
    print("Hello " + name + ", you are " + str(age) + "!")
    print(f"Hello {name}, you are {age}!")

#name = input("Enter your name: ")    
name = 'Luis'
greeting(name,32)
greeting("Judith")