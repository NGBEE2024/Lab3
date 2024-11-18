#price_info.py
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


#calculates the total cost of all items in the shopping list (quantity_list) using the prices in price_list
def total_cost_shopping():
    total_cost = 0
    for key in price_list.keys():
        if key in quantity_list:
            # complete the implementation below:
             total_cost += price_list[key] * quantity_list[key]  # Multiply price by quantity and add to total_cost
    print("total cost = ", total_cost)
    return total_cost  # Return the total cost

    

#calculates the cost of a specific fruit based on its price and a given quantity.
def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            return cost
    print("cost of ", quantity, fruit, "=", cost)
    return 0  # Return 0 if the fruit is not in the price list
            


def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping()


if __name__ == "__main__":
    main()


'''
cost_of_fruits('apple', 10) Output:

price_list['apple'] = 1.20
cost = 10 * 1.20 = 12.0
Output: cost of 10 apple = 12.0
total_cost_shopping() Output:

Loops through all fruits in price_list.
For each fruit, fetches its quantity from quantity_list and calculates the cost.
Sums up the cost of all fruits
'''