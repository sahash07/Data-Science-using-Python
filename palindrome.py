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




# Factorial of 4

def factorial(n):
   
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(4)
print("The factorial of 4 is:", result)

# Even number generating

def generate_even_numbers(n):
   
    even_numbers = [i for i in range(0, n+1, 2)]
    return even_numbers


even_numbers = generate_even_numbers(100)
print(even_numbers)

i = 0
while i<=100:
    i = i+1
    if i==50:
        break
    elif i%2==0:
        continue
        
    else:
        print(i)
