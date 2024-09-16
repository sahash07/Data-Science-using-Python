# a = "I love Nepal"
# print(a[::-1])
# b = input("Enter a word:")
# if b==b[::-1]:
#     print("It is palindrome.")
# else :
#     print("not palindrome.")

i = 0
total = 0
while i<=10:
    i = i+1
    print(f"old total={total}")
    total = i+total
    print(f"new total={total}, i={i}")
print(i)

def factorial(n):
   
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(4)
print("The factorial of 4 is:", result)
