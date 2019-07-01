print """
 _____       _   _                 
|  __ \     | | | |                
| |__) |   _| |_| |__   ___  _ __  
|  ___/ | | | __| '_ \ / _ \| '_ \ 
| |   | |_| | |_| | | | (_) | | | |
|_|    \__, |\__|_| |_|\___/|_| |_|
        __/ |                      
       |___/                       
  _____      _            _       _             
 / ____|    | |          | |     | |            
| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |___| (_| | | (__| |_| | | (_| | || (_) | |   
 \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

"""

print """
Select an operation
	1. Addition
	2. Subtraction
	3. Multiplication
	4. Division

"""
choice = input("Enter your choice # \n")

num1 = input("Enter first operand \n")
num2 = input("Enter second operand \n")

if choice == 1:
	print num1 + num2;
elif choice == 2:
	print num1-num2;
elif choice == 3:
	print num1*num2;
elif choice == 4:
	print num1//num2;
else:
	print "Invalid choice"
