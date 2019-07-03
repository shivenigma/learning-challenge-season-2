# 
length = input("Enter the number you want to generate fibbonacci for?")

a, b = 0, 1;

while a <= length:
	print a
	a,b = b, a+b;

#using for loops

ages = [24, 21, 20];
names = ["Vignesh", "Bhavana", "Arshin"];
for i in range(len(ages)):
	print (names[i], " is ", ages[i], " years old");