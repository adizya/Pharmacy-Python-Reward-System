
"""
Reward calculation:
This chunk of code calculates the price deduction if the customer has 100 points or more.
Deduciton is calculated based on the amount of reward point the customer has from previous
purchases."if" loop checks if the reward points are equal or greater than 100. for every 100
points, 10 dollars is reduced from total price using simple arithmetic calculations.
"""
def reward_usage(total, reward):
    if reward >= 100:
        deductions = reward // 100
        deduction_amount = deductions * 10
        total -= deduction_amount
        reward -= deductions * 100
    return total, reward

"""
The code block check for reward point and customer name in the customer database.
If the customer has exisitng reward points above 100, they are redeeemed as redeemable
points."If,else" loop has been used to check the reward point.  
"""
def reward_points(customer_name):
    if customer_name in customer_database:
        current_reward_points = customer_database[customer_name]["reward_points"]
        redeemable_points = current_reward_points // 100

        customer_database[customer_name]["reward_points"] -= redeemable_points * 100
        return redeemable_points
    else:
        return 0
"""
Display order History:
This block of code displays the order history of the customer name entered.
First an "If" statement is used to check if the input is present in the customer database. 
when a new customer makes any purchase, their order history also gets stored. A counter is 
added to number the orders. join() method is used to join the different variables storing the
values corresponding to the order. item() method is used to access the key and value in the 
dictionay.
"""    
def display_order_history(customer_name):
    if customer_name in customer_database:
        if customer_database[customer_name]["order_history"]:
            print("This is the order history of ",customer_name)
            print("Products Total Cost Earned Rewards")
            order_number = 1  # Start the order counter at 1 
            for order in customer_database[customer_name]["order_history"]:
                products_str = ", ".join(f"{quantity} x {product}" for product, quantity in order["products"].items())
                print(f"Order {order_number} {products_str} {order['total_cost']} {order['earned_rewards']}")
                order_number += 1  # Increment the counter
        else:
            print({customer_name}, "has no order history.")
    else:
        print("Customer ",{customer_name}," not found.")

"""
Database:
This block of code uses a dictionary to store the values of the inventory and customer database.
some additional data has been added to inventory and customer database for the sake of testing.
"""
# database 
inventory = {
        "vitaminC": {"price": 12.0, "prescription": "n"},
        "vitaminE": {"price": 14.5, "prescription": "n"},
        "coldTablet": {"price": 6.4, "prescription": "n"},
        "fragrance": {"price": 25.0, "prescription": "n"},
        "vaccine": {"price": 32.6, "prescription": "y"},
        "sleepingTablet": {"price": 15.5, "prescription": "y"}
    }
customer_database = {"Kate": {"reward_points": 120,"order_history":[]},
                    "Tom": {"reward_points": 32,"order_history":[{"products": {"vitaminC": 28}, "total_cost": 336.0, "earned_rewards": 336}]},
                    "Alex":{"reward_points":130,"order_history":[{"products": {"sleepingTablet":20},"total_cost":310.0,"earned_rewards": 310}]}
                    }

"""
Menu:
This block of code prints the menu and gets input to choose a menu option.
A while loop has been used to keep the code looping until the conditions are
satisfied
"""
while True:
    print("\n",
          "=" * 50, "\n",
          " " * 15, "MEDICAL SHOP", " " * 15, "\n",
          "=" * 50, "\n",
          "1. Make a purchase \n",
          "2. Add/update information of products \n",
          "3. Display existing customers \n",
          "4. Display existing products \n",
          "5. Display customer order history \n",
          "6. Exit the program \n",
          "=" * 50, "\n")

    choice = input("Please choose an option: ")
    """
    if choice 1 was chosen in the menu, 
      The first block of code gets customer name input and checks 
       if the input contains only alphabets using .isalpha(),while
       loop is used to make the code continue looping until a valid 
       input is entered
    """

    

# query based on user's choice
    if choice == "1":  # Make a Purchase
        while True:
            customer_name = input("Enter customer's name: ") #customer name 
            if customer_name not in customer_database:
                customer_database[customer_name] = {"reward_points": 0, "order_history": [{"products": {}, "total_cost": 0, "earned_rewards": 0}]}
                break
            if customer_name.isalpha():
                break
            else:
                print("Please enter a valid name")

        """ this block of code get input at 'product name' and checks against inventory 
        if the product is valid then its stored at valid products list. split() method
        is used to split the input using a comma because otherwise the code read the input as
        one word and not as individual product .for loop is used to check each product in 
         the input """
        
        valid_products = []  
        while True:
            product_name = input("Enter the Products: ")  # products purchased
            multiple_purchase = product_name.split(',')
            for product_name in multiple_purchase:
                if product_name in inventory:
                    valid_products.append(product_name)
            if not valid_products:
                print("The products entered are invalid! please enter valid products.")
            else:
                break

        """This block checks the quantity of the product purchased, isdigit() method is
        used to verify the input contains only numbers, if,else loop is used to check if 
        input is positive integer second loop is used to check if all the quantites entered 
        all valid in case of multiple qunantites"""
        
        while True:
            quantity_ordered = input("Enter quantities of the products: ") #quantity purchased
            quantities_list = quantity_ordered.split(',')
            valid_quantities = []  # Resets the list for each attempt
            all_quantities_valid = True
        
            for quantity_str in quantities_list:
                if quantity_str.isdigit():
                    quantity = int(quantity_str)
                    if quantity > 0:
                        valid_quantities.append(quantity)
                    else:
                        print("Please enter a positive quantity.")
                        all_quantities_valid = False 
                else:
                    print("Please enter a valid quantity (a positive integer).")
                    all_quantities_valid = False 

            if all_quantities_valid:  
                break  # Exit the loop only if all quantities are valid
            else:
                print("Some quantities were invalid. Please try again.")
         
        """products that have 'prescription' in the inventory dictionary are stored in a list
        if the user chooses 'n' the products without prescription are removed using 'not in'
        method"""

        #prescription check       
        products_with_prescription = []
        for product in valid_products:
            if inventory[product]["prescription"] == "y":
                products_with_prescription.append(product)

        if products_with_prescription:  # Ask about prescription only if needed
            has_prescription = input("Do you have a doctor's prescription for the required products? (y/n): ")
    
            if has_prescription == "y":
                pass
            elif has_prescription == "n":
                valid_products = [product for product in valid_products if product not in products_with_prescription]
            else:
                print("Please choose between 'y' or 'n'.")

        """total cost is set to 0 to reset the value incase of multiple calculations in the same instance
        for loop is utilized to add the cost of every product in the valid product. """

        print(valid_products)
        #total cost calculation 
        total_cost = 0
        for i in range(len(valid_products)):
            product_name = valid_products[i]
            quantity = valid_quantities[i]
            unit_price = inventory[product_name]["price"]
            total_cost += unit_price * quantity
        
        """The redeemable points are used to calcualte the deduction in total price"""
        #redeemable points calculation
        redeemable_points = reward_points(customer_name)       
        total_cost_before_discount = total_cost
        deduction = 0
        if redeemable_points >= 1:
            deduction = redeemable_points * 10
            total_cost -= deduction
            print("\nYou redeemed", redeemable_points * 100, "reward points! (Saved", deduction, "(AUD))")

        print(valid_products)
        print("\nTotal cost before discount: ", round(total_cost_before_discount, 2), "(AUD)")
        print("Total cost after discount:  ", round(total_cost, 2), "(AUD)")


        for i in range(len(valid_products)):
            customer_database[customer_name]["order_history"][0]["products"][valid_products[i]] = valid_quantities[i]


        #This the part where the Total cost is added to the order history
        customer_database[customer_name]["order_history"][0]["total_cost"] += total_cost

        #This the part where the earned rewards are added according to each purchaso
        customer_database[customer_name]["order_history"][0]["earned_rewards"] += total_cost_before_discount

        #This the part where the current reward points are updated
        customer_database[customer_name]["reward_points"] += total_cost_before_discount

        reward_point =  customer_database[customer_name]["reward_points"]
        print("Your reward points are", reward_point, "\n")

        """Receipt is printed with all the data calculated so far"""

        # Display receipt
        print("\n",
              "-" * 50, "\n",
              " " * 15, "Receipt", " " * 15, "\n",
              "-" * 50, "\n",
              "Name: ", customer_name)

        for i in range(len(valid_products)):
            product_name = valid_products[i]
            quantity = valid_quantities[i]
            unit_price = inventory[product_name]["price"]
            print("Product:        " + product_name)
            print("Unit Price:     " + str(round(unit_price, 5)) + " (AUD)")
            print("Quantity:       " + str(quantity))
            print("Total cost:     ", round(total_cost,2), "(AUD)")
            print("Earned reward:  ", round(reward_point))
            print("deduction:      ", deduction)
        order_details = {"products": {}, "total_cost": round(total_cost, 2), "earned_rewards": round(total_cost)}
        for x in range(len(valid_products)):
            order_details["products"][valid_products[x]] = valid_quantities[x] 

        """In this block of code, strip() method has been introduced to remove spaces in the input
         since, the input could contain space and are split with a comma to help the program read the
          input properly. Each input of the (name price dr_prescription) is checked for valid input 
           seperetely. """
    elif choice == "2":  # Add/update information of products
        while True:
            product_info = input("Enter product information (name price dr_prescription): ")
            product_data = [item.strip() for item in product_info.split(',')]  # Strip spaces around commas

            valid_input = True
            for item in product_data:
                details = [detail.strip() for detail in item.split()]  # Strip spaces within elements
                if len(details) != 3:
                    valid_input = False
                    break
                product_name, product_price, dr_prescription = details
                if not product_price.isdigit() or float(product_price) <= 0:
                    valid_input = False
                    break

                if dr_prescription not in ['y', 'n']:
                    valid_input = False
                    break

            if valid_input:
                for item in product_data:
                    details = [detail.strip() for detail in item.split()]
                    product_name, product_price, dr_prescription = details
                    if product_name in inventory:
                        print("Updating product info")
                        inventory[product_name]["price"] = float(product_price)
                        inventory[product_name]["prescription"] = dr_prescription
                    else:
                        inventory[product_name] = {"price": float(product_price), "prescription": dr_prescription}
                break
            else:
                print("Invalid input format. Please enter product information in the correct format.")

        """ choice 3 prints existing customer data and updates automatically when new customer
        data is entered using choice 1 since its under a while loop."""

    elif choice == "3":  # Display existing customers
        print(customer_database)

        """ choice 4 prints existing inventory and updates automatically when new customer
        data is entered using choice 1 since its under a while loop."""

    elif choice == "4":  # Display existing products
        print(inventory)

        """ choice 5 displays customer order history from the customer database """

    elif choice == "5":  #Display order history
        while True:
            customer_name = input("Enter customer's name: ")
            display_order_history(customer_name)
            break    
        
        """Choice 6 exits the program"""

    elif choice == "6":  # Exit the program
        print("Exiting the program. Goodbye!")
        exit()

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")           

   
    """
    Analysis and reflection:

    functionality

    The code implements a basic pharmacy management system, including customer management, product inventory, 
    order processing, and a simple reward point system.
    
    Data Structures

    I strategically chose dictionaries to represent products and customer information. Their flexibility allows 
    me to associate diverse data types (e.g., product name, price, reward points) with a single key.
    Lists were used to handle multiple user inputs, such as product names, quantities, and prescription details. 
    This facilitated the processing of these variable-length entries.
    
    Control Flow

    If-else loops were a natural fit for many binary decisions throughout the code (e.g., checking if a customer exists, 
    verifying if a product requires a prescription).While loops were essential for repeating code blocks until specific 
    conditions were met (e.g., ensuring valid customer name input, obtaining valid quantities).
   
     Challenges and Solutions

    Multiple Inputs: he most challenging parts of the code were adjusting the code from receving just one input 
    to multiple inputs as it required for me to create new lists and find ways to enter the input
    into the list since the dictonary(inventory and customer database) couldn't read multiple inputs
    directly. I overcame this by using lists to temporarily store these inputs before integrating them into the 
    dictionary-based data structures.
    
    Reward System: Implementing the reward calculation logic required careful consideration of how to retrieve existing 
    reward points, apply the calculation, and update the customer database.
    
    Quantity Validation: The block of code checking for valid quantity also posed a challenge as the loop kept crashing 
    the code.In order to stop it from crashing,  I added an additional if-else block to isolate the quantity check, 
    preventing crashes and improving code stability.
    
    Reflection

    This project solidified my understanding of how Python's core data structures and control flow statements can be combined 
    to model real-world systems.In the future, I would explore using file storage or a database to make the customer and product 
    data persistent across program executions.

    Reference:

    The Python Software Foundation, "Built-in Functions," Python 3.12.3 Documentation, 
    The Python Software Foundation, Nov. 16, 2023, https://docs.python.org/3/library/functions.html

    The Python Software Foundation, "Numeric Types — int, float, complex," Python 3.12.3 Documentation, 
    The Python Software Foundation, Nov. 16, 2023, https://docs.python.org/3/library/stdtypes.html
    """