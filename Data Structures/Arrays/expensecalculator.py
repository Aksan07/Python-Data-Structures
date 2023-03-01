expense=[2200,2350,2600,2130,2190]
month=["January","Febuary","March","April","May"]
#in feb, how many dollars you spent extra compare to January
comparism=expense[1]-expense[0]
print(comparism)
#find out your total expense in first quarter(first three months)of the year.
quarter_expense=0
for i in range(0,4):
    quarter_expense+=expense[i]
print(quarter_expense)
#find out if you spent exactly 2000 dollars in any month
Flag=False
for j in range(len(expense)):
    if expense[j]==2000:
        print(f"Have spent 2000 in {month[j]}")
        Flag=True
        break
if not Flag:
    print("2000 ruppees was not spend in any month")
#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
month.append("June")
print(expense)
print(month)
# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expense[3]=2130-200
print(expense)