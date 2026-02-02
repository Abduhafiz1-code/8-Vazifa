



def Accountant(*customer, **menu_service):
    menu = menu_service.get('menu')  
    service_fee = menu_service.get('service_fee')  
    total_price = 0
    menu_no_foods = []
    menu_available_foods = []
    for i in customer:
        if i in menu:
            
            total_price += menu[i]
            menu_available_foods.append(i)
            
        else:
            menu_no_foods.append(i)
    

    return total_price, menu_no_foods, customer, service_fee, menu_available_foods
 
result, result1, result2, result3, result4 = Accountant(
    'HotDog', 'lunch', 'bread', 'soup',
    menu={'osh': 20000, 'tea': 2000, 'bread': 3000, 'cola': 5000, 'lunch': 15000},
    service_fee=10
)
print(f" ______________________________________ \nOrder: {result2}")
print(f"Not Found {result1}")
print(f"Thank you for your order: {result4}")
print(f"{result} from you is sum")
print(f"Fee for our service: {result / result3} ")
print(f"Total price: {result + result / result3} \n ______________________________________")























































customer = input("Check the order: ")

test = customer.split()
# print(type(test))


    
customer_order = customer.split()

def Accountant(*customer, **menu_service):
   
    menu = menu_service.get('menu')  
    service_fee = menu_service.get('service_fee')  
    
    
    total_price = 0
    menu_no_foods = []
    menu_available_foods = []
    for i in customer:
            
        if i in menu:
            total_price += menu[i]
            menu_available_foods.append(i)
        else:
            menu_no_foods.append(i)
            
    return total_price, menu_no_foods, customer,  service_fee, menu_available_foods
    



result, result1, result2, result3, result4 = Accountant(
    *customer_order,
    menu = {
   
    "Burger": 25000,
    "Cheeseburger": 28000,
    "Hot dog": 20000,
    "Pizza": 60000,
    "Sandwich": 22000,
    "Lavash": 30000,
    "Shaurma": 28000,
    "Fries": 15000,


    
    "Osh": 35000,
    "Manti": 30000,
    "Somsa": 12000,
    "Lagman": 32000,
    "Shurva": 28000,
    "Qozon kabob": 45000,
    "Norin": 40000,
    "Dimlama": 38000,


    
    "Tuxum qovurdoq": 18000,
    "Omlet": 20000,
    "Non": 4000,
    "Saryog'li non": 7000,
    "Bo'tqa": 15000,


    
    "Choy": 5000,
    "Qahva": 12000,
    "Coca Cola": 10000,
    "Fanta": 10000,
    "Sharbat": 12000,
    "Suv": 4000,


   
    "Tort": 25000,
    "Pirojniy": 15000,
    "Shokolad": 18000,
    "Muzqaymoq": 12000,
    "Pechenye": 10000,


   
    "Makaron": 22000,
    "Spaghetti": 26000,
    "Palov guruch": 20000,
    "Fried rice": 28000
},
    service_fee=10
)
print(f" ______________________________________ \nOrder: {result2}")
print(f"Not Found {result1}")
print(f"Thank you for your order: {result4}")
print(f"{result} from you is sum")
print(f"Fee for our service: {result / result3} ")
print(f"Total price: {result + result / result3} \n ______________________________________")

