#Activity 1
user_input = int(input("Enter a number whose sum you want to find: "))
sum = 0

for i in range(1, user_input + 1):
    sum = sum+i
    print("\nSum =", sum)

#Activity 2
user_input = input("Enter a String: ")

Looper = ('')

for i in user_input:
    Looper = i + Looper

print("\nOriginal String: ", user_input)
print("\nReversed String: ", Looper)

#Activity 3
user_input = int(input("Enter a value: "))

print("Numbers from {} to {} are: ".format(user_input, 1))

for i in range(user_input, 0, -1):
    print(i)