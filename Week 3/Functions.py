#define the function
def calculate_discount ( price, discount_price):
    #Calculate 
    if discount_price >= 20:
        discount_amount = (discount_percent /100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price 
    
#prompt user input 
price = float(input("Enter the original price:"))
discount_percent = float(input("Enter the percentage discount:"))

final_price = calculate_discount(price, discount_percent)

#Show notofications
if discount_percent >= 20: 
    print(f"Discount applied! Your final price is: Ksh {final_price :.2f}")
else:
    print(f"Sorry! No discount applied! Your price remains: Ksh{final_price: .2f}")
