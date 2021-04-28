"""
A Simple Game In Which You Have To Guess hidden number,
i was restricted to use any module so number is constent for all
"""
hiddenNo = 67

yourNo = int(input("Guess The Number >>>"))

limit = 5

attempt=0

On={

   "correct":"Congratulations You Guessed Correct Number",

   "small":"your number is too small than hidden number",

   "large":"Your Number Is Too Large Than hidden Number",

}

result=False

"""

while yourNo != hiddenNo:

   limit = limit + 1

   if (yourNo>hiddenNo):

      print("Hidded Number Is Less Than Your Number")

   elif (yourNo<hiddenNo):

      print("Hidden Number is Bigger than your number")

   yourNo=int(input("Guess Again >>>"))

print("Finally You Guessed Correct 馃憤")"""

while ~result:

   if attempt>=limit:

      print("Oops Limit Exceed number was",hiddenNo)

      break

   elif yourNo < hiddenNo:

      print(On["small"])

      print("Try Again Only",limit-attempt,"Chance Left")

      yourNo = int(input("Guess The Number >>>"))

   elif yourNo > hiddenNo:

      print(On["large"])

      print("Try Again Only",limit-attempt,"Chance Left")

      yourNo = int(input("Guess The Number >>>"))

   else:

      result=True

      print(On["correct"])

   attempt = attempt+1
