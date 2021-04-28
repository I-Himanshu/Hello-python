#This is age Verity Program To Test Are You 18+,
age=int(input("Enter Your Real Age >>> "))
if age>18:
   print("Cogratulation 🎉🎊 You Can Drive 👍")
elif age<18:
   print("Oops You are just "+str(age)+" years old, You Can't drive Wait For "+str(18-age)+" years to drive")
else:
   print("We Can't Decide At This Moment, Come to our office then we will decide,You are eligible or not")
