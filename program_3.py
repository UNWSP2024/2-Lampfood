#Elliott Morris, 1/13/2026, Total and tax calculator
#This program asks for the price of a series of items, adds them together, calculates the tax, and displays the total

def calculate_total_purchase():
    #Get user input on item prices
    item_1 = float(input('What is the price of item 1?: '))
    item_2 = float(input('What is the price of item 2?: '))
    item_3 = float(input('What is the price of item 3?: '))
    item_4 = float(input('What is the price of item 4?: '))
    item_5 = float(input('What is the price of item 5?: '))

    #calculate subtotal
    subtotal = item_1 + item_2 + item_3 + item_4 + item_5
    #calculate sales tax
    sales_tax = subtotal * 0.07
    #calculate total
    total_purchase = subtotal + sales_tax

    #print results using a formatted string
    print(f'The total purchase is: $ {total_purchase:0.2f}')

#runs the calculate function
calculate_total_purchase()
