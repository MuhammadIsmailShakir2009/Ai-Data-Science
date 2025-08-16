#---------------- PART#1 FUNCTION -------------------------#
# 1. Greeting function
def Greetings(name):
    print("Welcome to SMIT training center,", name)

# 2. Check positive, negative or zero
def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

# 3. Larger of two numbers
def larger_of_two(a, b):
    if a > b:
        print("Larger is:", a)
    else:
        print("Larger is:", b)

# 4. Largest of three numbers
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        print("Largest is:", a)
    elif b >= a and b >= c:
        print("Largest is:", b)
    else:
        print("Largest is:", c)

# 5. Age category
def age_category(age):
    if age < 18:
        print("Minor")
    elif age >= 18 and age < 60:
        print("Adult")
    else:
        print("Senior Citizen")

# 6. Even or Odd
def even_or_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# 7. Square of number
def square(n):
    print("Square is:", n * n)

# 8. Circle area and circumference
def circle(radius):
    pi = 3.14
    area = pi * radius * radius
    circumference = 2 * pi * radius
    print("Area:", area)
    print("Circumference:", circumference)

# 9. Pass or Fail
def pass_or_fail(score):
    if score > 60:
        print("Pass")
    else:
        print("Fail")

# 10. Prime number
def is_prime(n):
    if n <= 1:
        print("Not Prime")
    else:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            print("Prime")
        else:
            print("Not Prime")

# 11. Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)



#--------------- PART#2 LIST ------

# 1. Student list
student = ["Tahir", 44, "AI and Data Science", True]
for item in student:
    print(item)

# 2. Separate data
strings = []
numbers = []
booleans = []
for item in student:
    if type(item) == str:
        strings.append(item)
    elif type(item) == int:
        numbers.append(item)
    elif type(item) == bool:
        booleans.append(item)

print("Strings:", strings)
print("Numbers:", numbers)
print("Booleans:", booleans)

# 3. Fruits list
fruits = ["apple", "raspberry", "pineapple", "cherry"]

if "apple" in fruits:
    print("Index of apple:", fruits.index("apple"))

fruits[1:3] = ["orange"]
fruits.insert(2, "apricot")
fruits.extend(["car", "bike", "aeroplane"])
print("Updated Fruits:", fruits)

# 4. Best scores
Scores_list = [40, 89, 90, 89, 23, 90, 50]
unique_scores = []
for score in Scores_list:
    if score not in unique_scores:
        unique_scores.append(score)
unique_scores.sort(reverse=True)
print("First Best:", unique_scores[0])
print("Second Best:", unique_scores[1])

# 5. Numbers list
numbers_list = [32,54,66,11,77,10,90]
new_list = []
for n in numbers_list:
    if n >= 20:
        new_list.append(n)

print("Filtered List:", new_list)
new_list.sort()
print("Ascending:", new_list)
new_list.sort(reverse=True)
print("Descending:", new_list)
average = sum(new_list) / len(new_list)
print("Average:", average)

# 6. Gadgets list
Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

string_list = []
number_list = []
for item in Gadgets:
    if type(item) == str:
        string_list.append(item)
    else:
        number_list.append(item)

string_list.sort()
print("Strings Asc:", string_list)
string_list.sort(reverse=True)
print("Strings Desc:", string_list)

string_list.sort(key=len)
print("Strings by Length:", string_list)

number_list.sort()
print("Numbers Asc:", number_list)
number_list.sort(reverse=True)
print("Numbers Desc:", number_list)
