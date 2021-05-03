"""Create A Upper & Lower Triangle as per your requirement"""
row=input("Enter Number Of Rows >>> ") or 4
row=int(row)

cond=bool(int(input("Enter 1 or 2 for Lower or Upper ∆ >> ")));

#print(cond)

if cond:

  while row>0:

    print("*" * row)

    row=row-1

else:

  start=0;

  while row>=start:

    print("*"*start)

    start=start+1

print("Program End")
