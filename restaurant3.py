'''
1. An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class.
2. Add an attribute called flavors that stores a list of ice cream flavors.
3. Write a method that displays these flavors.
4. Create an instance of IceCreamStand, and call this method.
5. An administrator is a special kind of user. Write a class called Admin that inherits from the User class previously written.
6. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
7. Write a method called show_privileges() that lists the administrator’s set of privileges.
8. Create an instance of Admin, and call your method.
9. Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings.
10. Move the show_privileges() method to this class.
11. Make a Privileges instance as an attribute in the Admin class.
12. Create a new instance of Admin and use your method to show its privileges.
13. Save your code with the appropriate file name and upload these files in the space below.
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

#Write a class called IceCreamStand that inherits from the Restaurant class
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=None):
        super().__init__(restaurant_name, cuisine_type)
        if flavors is None:
            self.flavors = []
        else:
            self.flavors = flavors

    def display_flavors(self): 
        print(f"Flavors at {self.restaurant_name}:")
        if self.flavors:
            for flavor in self.flavors:
                print(f"- {flavor} -")
        else:
            print("- No flavors -")

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
		return(f'Welcome, {self.first_name} to {Restaurant.restaurant_name}')
	
	# method that increments the value of login_attempts by 1.
	def increment_login_attempts(self,count):
		self.login_attempts += count
		return(f'Login Attempts: {self.login_attempts}')

	# method that resets the value of login_ attempts to 0.
	def reset_login_attempts(self,count):
		self.login_attempts = count
		return(f'Login Attempts Reset: {self.login_attempts}')


# Write a class called Admin that inherits from the User class
# Add an attribute, privileges, that stores a list of strings 
# like "can add post", "can delete post", "can ban user"
class Admin(User):
	def __init__(self, first_name, last_name, age, gender, city, admin_privileges_list=None):
		super().__init__(first_name, last_name, age, gender, city)
		self.privileges = Privileges(admin_privileges_list)

# Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings
class Privileges():
	def __init__(self, privileges=None):
		if privileges is None:
			self.privileges = []
		else:
			self.privileges = list(privileges)

# Write a method called show_privileges() that lists the administrator’s set of privileges
	def show_privileges(self):
		if not self.privileges:
			print('none')
		else:	
			for privilege in self.privileges:
				print(f'User has privilege:- {privilege}')


# Create an instance of Admin, and call your method (show_privileges())
admin_privileges_list = ["can add post","can delete post","can ban user"]
admin_1 = Admin('Brian', 'Sanders', 45, 'male', 'Houston', admin_privileges_list)

# Restaurant instance
restaurant1 = IceCreamStand("I'll be Dipped'", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])

# User instance
user1 = User("Kevin","Kramer",35,"male","Houston")

# call flavors
restaurant1.display_flavors()

# call admin show_privileges
print(admin_1.last_name)
admin_1.privileges.show_privileges()