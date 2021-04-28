#This Is My First Dictionary App…,

dictionary={

   "shopkeeper":"A Person who sell things from shop",

   "train":"a cheapest way of transport",

   "school":"a place where our parents get looted and we get beated",

   "delhi":"The heart of india",

   "india":"World's Beautiful Country",
  "earth":"a blue planet where intelligent people born",
"corona":"A disease who make Everyone Imprisoned at home"

}

print("This Is a simple Dictionary".title())

print("You can search for ", list(dictionary.keys()))

Word=input("Please Enter Your Word: >>> ")

Meaning=dictionary[Word.lower()];

print("The Word",Word, "Refers To", Meaning)
