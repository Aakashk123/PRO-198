
while True: 
    Total=0 
    Customer_name=input("Name of customer :")
   
   
    while True:
        print("Enter cost of items and quantity")
        Cost=float(input("Item cost :"))
        Quantity=int(input("Quantity :"))

        Total+=Cost*Quantity                
        repeat=input("Do you want to add more items?(y/Y/n/N)")
        if repeat=='n' or repeat=='N':
            break
   
    print("_"*50)
    print("Name :",Customer_name)
    print("Total bill cost : ",Total)
    print()
    print("*****Thankyou shopping with us*****")
    print("_"*50)
   
    new_customer=input("Go to next person?(y/Y/n/N)")
    if new_customer=='n' or new_customer=='N':
        break 