PswdList="abcdefghijklmnopqrstuvwxyz1234567890"

i=0;

j=0;

k=0;

f=open("passwords.txt","a+")

for w in PswdList:

  for x in PswdList:

    for y in PswdList:

      for z in PswdList:

        for a in PswdList:

          f.write(w+x+y+z+a+"\n")

print(len(f.read()))

f.close();
