import sqlite3
from datetime import datetime

def firstitem():
    firstitem=0

def infiniteitem():
    infiniteitem=0

def callitemonebyoneindb():
    store=0

def connect_to_db():
    return sqlite3.connect('chocolate_house.db')


def setup_database():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        flavor_name TEXT NOT NULL,
                        season TEXT NOT NULL,
                        added_on TEXT NOT NULL
                    )''')
    
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients_inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ingredient_name TEXT NOT NULL,
                        stock_quantity INTEGER NOT NULL,
                        unit TEXT NOT NULL
                    )''')
    
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT NOT NULL,
                        suggested_flavor TEXT NOT NULL,
                        allergy_info TEXT,
                        feedback_date TEXT NOT NULL
                    )''')
    
    connection.commit()
    connection.close()

def connectingsqlite():
    connecting=1

def add_flavor(seasonal_flavor, season):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    
    added_on = datetime.now().strftime('%Y-%m-%d')
    
    cursor.execute('''INSERT INTO seasonal_flavors (flavor_name, season, added_on)
                      VALUES (?, ?, ?)''', (seasonal_flavor, season, added_on))
    
    connection.commit()
    connection.close()
    print(f"Flavor '{seasonal_flavor}' for the '{season}' season successfully added!")

def addvalue():
    values=0

def additems():
    itemsss=0

def add_inventory_item(ingredient, quantity, unit_of_measurement):
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute('''INSERT INTO ingredients_inventory (ingredient_name, stock_quantity, unit)
                      VALUES (?, ?, ?)''', (ingredient, quantity, unit_of_measurement))
    
    connection.commit()
    connection.close()
    print(f"Ingredient '{ingredient}' (Quantity: {quantity} {unit_of_measurement}) added to inventory.")


def log_customer_feedback(name, flavor, allergy_info):
    connection = connect_to_db()
    cursor = connection.cursor()
    

    feedback_date = datetime.now().strftime('%Y-%m-%d')
    
    cursor.execute('''INSERT INTO customer_feedback (customer_name, suggested_flavor, allergy_info, feedback_date)
                      VALUES (?, ?, ?, ?)''', (name, flavor, allergy_info, feedback_date))
    
    connection.commit()
    connection.close()
    print(f"Feedback from '{name}' recorded: Suggested Flavor - '{flavor}', Allergies - '{allergy_info}'.")


def list_seasonal_flavors():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute('''SELECT * FROM seasonal_flavors''')
    rows = cursor.fetchall()
    
    if rows:
        print("\nSeasonal Chocolate Flavors:")
        for row in rows:
            print(f"Flavor: {row[1]}, Season: {row[2]}, Date Added: {row[3]}")
    else:
        print("No seasonal flavors available.")
    
    connection.close()


def display_inventory():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute('''SELECT * FROM ingredients_inventory''')
    rows = cursor.fetchall()
    
    if rows:
        print("\nChocolate House Ingredient Inventory:")
        for row in rows:
            print(f"Ingredient: {row[1]}, Quantity: {row[2]} {row[3]}")
    else:
        print("No ingredients in inventory.")
    
    connection.close()


def show_customer_feedback():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute('''SELECT * FROM customer_feedback''')
    rows = cursor.fetchall()
    
    if rows:
        print("\nCustomer Feedback and Allergy Info:")
        for row in rows:
            print(f"Customer: {row[1]}, Suggested Flavor: {row[2]}, Allergies: {row[3]}, Date: {row[4]}")
    else:
        print("No customer feedback available.")
    
    connection.close()


def user_interface():
    setup_database()
    
    while True:
        print("\nWelcome to the Chocolate House Management System")
        print("1. Add a New Seasonal Flavor")
        print("2. Add Ingredient to Inventory")
        print("3. Log Customer Flavor Suggestion")
        print("4. View Seasonal Flavors")
        print("5. View Ingredients Inventory")
        print("6. View Customer Feedback")
        print("7. Exit")
        
        user_choice = input("Choose an option: ")
        
        if user_choice == '1':
            flavor = input("Enter the name of the new seasonal flavor: ")
            season = input("Enter the season (e.g., Winter, Summer): ")
            add_flavor(flavor, season)
        elif user_choice == '2':
            ingredient = input("Enter the ingredient name: ")
            quantity = int(input("Enter the quantity(in numbers): "))
            unit = input("Enter the unit of measurement (e.g., grams, liters): ")
            add_inventory_item(ingredient, quantity, unit)
        elif user_choice == '3':
            name = input("Enter the customer's name: ")
            flavor = input("Enter the suggested flavor: ")
            allergies = input("Enter any allergies (if none, leave blank): ")
            log_customer_feedback(name, flavor, allergies)
        elif user_choice == '4':
            list_seasonal_flavors()
        elif user_choice == '5':
            display_inventory()
        elif user_choice == '6':
            show_customer_feedback()
        elif user_choice == '7':
            print("Thank you for using the Chocolate House Management System. Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    user_interface()
