noOfItem=int(input("Please enter total number of item "))
i=1
Items=[]
while i <= noOfItem:
     Items.append(input("Item # "+str(i) + ":"))
     i=i+1
print(Items)
Items.sort(key=str.casefold)  
print(f"the sorted list is  {Items}")
