#Activity 1

Tree_1 = 98
Tree_2 = 94
Tree_3 = 41
Tree_4 = 95
Tree_5 = 11

sum = Tree_1+Tree_2+Tree_3+Tree_4+Tree_5
print("The Sum of all the 5 Tress is: ", sum)

Average = sum/5
print("The Average of all the Tress is: ", Average)

#Activity 2

Amount = int(input("Plese Enter Amount for Withdraw: "))

Note_1 = Amount//100
Note_2 = (Amount%100)//50
Note_3 = ((Amount%100)%50)//10

print("Notes of 100₹", Note_1)
print("Notes of 50₹", Note_2)
print("Notes of 10₹", Note_3)

#Activity 3

print("Enter Marks Optained in 4 Subjects: ")
Maths = int(input("Maths: "))
English = int(input("English: "))
Science = int(input("Science: "))
Hindi = int(input("Hindi: "))

sum = Maths+English+Science+Hindi
perc = (sum/400)*100

print("Perctage Mark = ", perc)