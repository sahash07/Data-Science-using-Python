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

def even_numbers(n):
   
    even_num = [i for i in range(0, n+1, 2)]
    return even_num


even_num = even_numbers(100)
print(even_num)

i = 0
while i<=100:
    i = i+1
    if i==50:
        break
    elif i%2==0:
        continue
        
    else:
        print(i)

    
    # i = 0
    # while i<=500:
    #     i = i+1
    #     if i==100:
    #         break
    #     if i%3==0 or i%5==0:
    #         continue
a = "I am superman and  completing quest is my task."
i = 0 
len(a)
# while i<len(a):
#     print(a[i])
#     i = i+1
 
while i<len(a):
    if  a[i]=="q":
        break
    if a[i].lower() not in "aeiou":
        i+=1
        continue
    print(a[i])
    i+=1

# hello I am sahash Rai and i am trying to add push the files into git hub
a = "Functions "
len(a)
i = 0
while i<len(a):
    i += 1
    if a([i]).lower() == t:
        break








