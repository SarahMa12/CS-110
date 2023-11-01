#Sarah Ma
#Lab 5 - Lists and Files

#Read the file and store each piece (name, price, and quantity) of the item into different lists
def read_file():
	file_read = open('inventory.csv', 'r')
	name = []
	price = []
	quantity = []

	file_read.readline()

	for line in file_read:
		line_parts = line.strip().split(',')
		if len(line_parts) == 3:
			name.append(line_parts[0])
			price.append(float(line_parts[1]))
			quantity.append(int(line_parts[2]))

	file_read.close()

	return name, price, quantity

#Iterates through the csv file and prints each line of the file so it's displayed for the user
def display_inventory():
	print('Inventory: ')
	file_read = open('inventory.csv', 'r')
	for line in file_read:
		print(line.strip())
	file_read.close()

#Allows the user to add an item to the current inventory
def add_item(name, price, quantity):
	#Ask user for the name, price, and quantity of the item they want to add
	new_name = input('Enter the name of the item you want to add: ')
	new_price = float(input('Enter the price of the item you want to add: '))
	new_quantity = int(input('Enter the quantity of the item you want to add: '))
	#Append both names to the 3 lists
	name.append(new_name)
	price.append(new_price)
	quantity.append(new_quantity)
	#This function description is described below
	#Write the new item into the file
	write_inventory_to_file(name, price, quantity)
	print('Item added.')
	return name, price, quantity


def delete_item(name, price, quantity):
	#Ask the user what item they want to delete
	item_to_delete = input('Enter the name of the item you want to delete: ')
	#Reference the iventory by the name
	if item_to_delete in name:
		#Find the index of the item they want to update by the name
		item_to_delete_index = name.index(item_to_delete)

		#Use that same index to search the other lists for price and quantity since it should match
		del name[item_to_delete_index]
		del price[item_to_delete_index]
		del quantity[item_to_delete_index]

		#This function description is described below
		write_inventory_to_file(name, price, quantity)
		print('Item deleted.')
	else:
		print('Item not found in inventory.')

def update_item(name, price, quantity):
	#Ask the user what item they want to update
	item_to_update = input('Enter the name of the item you want to update: ')
	#Reference the inventory by the name
	if item_to_update in name:
		#Find the index of the item they want to update by the name
		item_to_update_index = name.index(item_to_update)
		updated_name = input('Enter the updated name: ')
		updated_price = float(input('Enter the updated price: '))
		updated_quantity = int(input('Enter the updated quantity: '))

		#Use that same index to search the other lists for price and quantity since it should match
		name[item_to_update_index] = updated_name
		price[item_to_update_index] = updated_price
		quantity[item_to_update_index] = updated_quantity

		#This function description is described below
		write_inventory_to_file(name, price, quantity)
		print('Item updated.')
	else:
		print('Item not found in inventory.')


def display_total_inventory(quantity):
	#Create a variable to accumulate the quantity
	total_quantity = 0
	#Iterate through the quantity list
	for item in quantity:
		#Add all of the quantities to the variable total_quantity
		total_quantity += item
	return total_quantity

#Writes the inventory to the file to update it with new information
def write_inventory_to_file(name, price, quantity):
	#This part is meant to clear out the file so I can append new information 
	#Opens the file to write
	file_write = open('inventory.csv', 'w')
	#Closes the File
	file_write.close()

	#Open the file to append new informaiton
	file_write = open('inventory.csv', 'a')
	file_write.write('Name,Price,Quantity\n')
	#Iterate through the name index length 
	for i in range(len(name)):
		#Write the name, price, and quantity for each index
		file_write.write(f'{name[i]},{price[i]},{quantity[i]}\n')
	file_write.close()


def main():
	#Set the name, price, quantity to lists in the main function so it can be accessed across each function
	name, price, quantity = read_file()
	cont = 'y'

	#While loop allows user to repeat this program until they want to exit.
	while cont.lower() == 'y':
		print('Menu:')
		print('1. Display inventory.')
		print('2. Add a new item to the inventory.')
		print('3. Delete an item to the inventory.')
		print('4. Update the price or quantity of an item in the inventory.')
		print('5. Display the total inventory value.')
		print('6. Exit.')
		user_choice = int(input('Choose an option (1-7): '))
		if user_choice == 1: 
			display_inventory()
		elif user_choice == 2:
			add_item(name, price, quantity)
		elif user_choice == 3:
			delete_item(name, price, quantity)
		elif user_choice == 4:
			update_item(name, price, quantity)
		elif user_choice == 5:
			print(f'Total inventory value: {display_total_inventory(quantity)}')
		elif user_choice == 6:
			print('Exiting the program.')
		else:
			print('Please enter a valid number (1-7).')

		cont = input('Do you want to continue? (y/n): ')
	else:
		print('Exiting program.')


main()
