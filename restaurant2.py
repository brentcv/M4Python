'''
1.
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, 
and then change this value and print it again.
2.
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again.
3.
Add a method called increment_number_served() that lets you increment the 
number of customers who’ve been served. 
Call this method with any number you like that could represent how many customers 
were served in, say, a day of business.
4.
Add an attribute called login_attempts to your User class created in the question above. 
Write a method called increment_ login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_ attempts to 0.
5.
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and 
then call reset_login_attempts() . 
Print login_attempts again to make sure it was reset to 0.
'''
# Reorganized - Class, Instance, Start

class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		# instance attributes
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0 # added number served class attribute
		
	def describe_restaurant(self):
		return(f'This is {self.restaurant_name} home of the best {self.cuisine_type}!')
		
	def open_restaurant(self):
		return(f'{self.restaurant_name} is now Open for Buisiness')

	def set_number_served(self):
		served = int(input("Please enter the new number of customers served: "))
		self.number_served = served
		return(f'Now Served: {self.number_served}')
	
	def increment_served(self, count):
		self.number_served += count
		return(f'Now Served: {self.number_served}')
	
class User:
	def __init__(self, first_name, last_name, age, gender, city):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.city = city
		self.login_attempts = 0

    # method called describe_user()
	def describe_user(self):
		return(f'User info:\n First: {self.first_name}\n Last: {self.last_name}\n Age: {self.age}\n Gender: {self.gender}\n City: {self.city}')

    # greet_user()
	def greet_user(self):
		return(f'Welcome, {self.first_name} to {self.restaurant_name}')
	
	# method that increments the value of login_attempts by 1.
	def increment_login_attempts(self,count):
		self.login_attempts += count
		return(f'Login Attempts: {self.login_attempts}')

	# method that resets the value of login_ attempts to 0.
	def reset_login_attempts(self,count):
		self.login_attempts = count
		return(f'Login Attempts Reset: {self.login_attempts}')

# Restaurant instance
restaurant1 = Restaurant("Bobby's Q'", "Bar-B-Q")

# User instance
user1 = User("Kevin","Kramer",35,"male","Houston")

## - Start - #
print(f'Number Served: {restaurant1.number_served}')
# Set number_served. Call this method with a new number and print the value again.
print(restaurant1.set_number_served())
# increments the value of login_attempts by 1
print(restaurant1.increment_served(1))
print(restaurant1.increment_served(2))
# call increment_login_attempts() several times
print(user1.increment_login_attempts(1))
# call increment_login_attempts() several times
print(user1.increment_login_attempts(1))
# then call reset_login_attempts()
print(user1.reset_login_attempts(0))
