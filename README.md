# Pharmacy-Python-Reward-System
The code implements a basic pharmacy management system, including customer management, product inventory,      order processing, and a simple reward point system.

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
