shop_name='ELISANMART'
shop_logo='''

 _________
|         |
| ELISAN  | 
|  MART   |
|_________|
'''
cashier_name='NERUBUCHA ELISHAMAH WANJALA'
items={
'Sugar':150.0,
'Salt':75.0,
'Cooking oil':350.0,
'Bread':65.0,
'Egg':20.0,
'Milk':60.0,
'Rice':130.0,
'Maize flour':110.0,
'Tea':30.0,
'Apple':50.0
}

import datetime

def menu_display():
    print(shop_logo)
    print(f'Welcome to {shop_name}.')
    print('Available items')
    for i,(item,price) in enumerate(items.items(),start=1):
        print(f'{i}. {item} : ksh {price:.2f}')
        
def calculate_bill():
    total=0.0
    bill=[]
    while True:
        menu_display()
        choice=input('Enter item number (or type "done " to finish  :')
        if choice.lower()=='done':
            break
            
        try:
            choice=int(choice)
            if 1<= choice <= len(items):
                item=list(items.keys())[choice-1]
                quantity=int(input(f'Enter the quantity of the {item} :'))
                price=items[item]*quantity
                bill.append((item,quantity,price))
                total +=price
                
            else:
                print('INVALID CHOICE. PLEASE TRY AGAIN!')
                
        except ValueError:
                print('INVALID INPUT . PLEASE TRY AGAIN!')
                
    return bill,total
    
    
def print_bill(bill,total):
    current_time=datetime.datetime.now()
    print('\n ' +shop_logo)
    print(f'{shop_name} Bill')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    print(f'Date :{current_time.strftime("%Y-%m-%d  %H:%M:%S") }')
    print(f'Cashier : {cashier_name}')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    for item,quantity,price in bill:
        print(f' {item} × {quantity} : ksh {price:.2f}')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    print(f'Total: ksh {total:.2f}')
    
def main():
    bill,total=calculate_bill()
    print_bill(bill,total)
    
    print(f'\n Thanks for shopping with {shop_name} welcome back.')
    
if __name__ == '__main__':
    main()
