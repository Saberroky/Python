 name = input("what is your namr?  ")
 print("hello  sabe"+name)
 brith_year = int(input("enter your birth year: "))
 age =2022 -brith_year
 print(age)
 int()
 float()
 bool()
 str()
 number = float(input("input your 1st number: "))
 number2 = float(input("input your 2nd number: "))
 sum = number+number2
 print(sum)
 temperature= int(input("enter temp: "))
 if temperature > 30:
     print("Its a hot day")
     print("drink water")
 elif temperature > 20:
     print("its a nice day")
 elif temperature < 20:
     print("its a cold day")

 weight = int(input("enter your weight in pounds: "))
 zx = input("(k) for kg or (L) for lbs: ")
 if zx.upper()=="K":
     print(str(weight)+" pounds to kg is: " +str(weight*0.45))
 else:
     print(str(weight)+" kg to pounds: " +str(weight/0.45))
 weight = float(input("Enter your weight in killogram(kg): "))
 height = float(input("Enter your height in meter(m): "))
 bmi = weight/ (height*height)
 if bmi >= 25:
     print("rohan is over weight: ")
 elif bmi<=18:
     print("Under weight: ")
 elif bmi>18 and bmi <25:
     print("bmi is normal") 
 i = 10
 while i<=100:
     print(i* '*')
     i = i+1
 names= ["saber","roky","hossain"]
 names[0] = "sab"
 print(names[0:2])
  
