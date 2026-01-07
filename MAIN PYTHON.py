#IDENTIFIERS
print("hello world")


#OUTPUT STATEMENTS

#product
#brand
#price
#color
#warranty
#the dell laptop cost rs 55000 is silver
#color and comes with 2 year warranty

product="laptop"
brand="dell"
price=55000
color="silver"
warranty=2
print("the",brand,product,"cost rs",price,"is",color,"color and comes with",warranty,"year warranty")


#INPUT STATEMENTS

#the dell laptop cost rs 55000 is silver color and comes with 2 year warranty.

product=input("enter the product:")
brand=input("enter the brand:")
price=int(input("enter the price:"))
color=input("enter the color:")
warranty=int(input("enter warranty:"))
print(f"the {brand} {product} cost rs {price} is {color} color and comes with {warranty} year warranty.")

#SWAPPING

num1=30
num2=40
print("before swapping")
print("number1:",num1)
print("number2:",num2)
num1,num2=num2,num1
print("after swapping")
print("number1:",num1)
print("number2:",num2)

#FLOW CONTROLS
     #1. CONDITIONAL OR DECISION MAKING STATEMENTS

# Movie Ticket Discount
# Write a Python program to find the ticket price based on a person’s age.
# Ticket price = ₹150
# Below 5 → Free
# 5–12 → Half price
# 13–59 → Full price
# 60 or above 40% discount

age=int(input("enter ur age:"))
ticket_price=150
if age<5:
    price=0
elif age<=12:
    price=ticket_price*0.5
elif age<=59:
    price=ticket_price
else:
    price=ticket_price*0.6
print(f"ticket price is {price}")


# Water Bill Calculator
# Write a Python program to calculate water bill based on usage.
# First 50 liters → ₹2 per liter
# Next 100 liters → ₹3 per liter
# Above 150 liters ₹5 per liter

litre=int(input("amount of water in litres:"))
if litre<=50:
    bill=litre*2
elif litre<=150:
    bill=(50*2)+(litre-50)*3
else:
    bill=(50*2)+(100*3)+(litre-150)*5
print(f"total amount is {bill}")


# Shopping Bill with Membership Discount
# A store gives discounts based on the total amount and membership type.
# amount > ₹2000 and membership = "Gold"	discount - 20%
# amount > ₹1000 and membership = "Silver"	discount 10%
# Otherwise

amount=int(input("enter the amount:"))
membership_type=input("enter the membership type:")
if amount>2000:
    membership_type="gold"
    discount=amount*0.2
elif amount>1000:
    membership_type="silver"
    discount=amount*0.1
else:
    discount=amount*0.05
final_amount=amount-discount
print(f"discount is {discount}")
print(f"final amount is {final_amount}")

   #2. LOOPING ----- WHILE LOOP $ FOR LOOP

#WHILE LOOP

#Sum of numbers from 1 to n

n=int(input("enter n:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i += 1
print(f"sum of numbers from 1 to n is {sum}")

#Reverse of a number

rev=0
num=int(input("enter number:"))
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(f"the reverse is {rev}")


#Odd and Even count

even_count=0
odd_count=0
num=int(input("enter number:"))
while num>0:
    digit=num%10
    if digit%2==0:
       even_count+=1
    else:
       odd_count+=1
    num=num//10
print(f"number of even digits is {even_count}")
print(f"number of odd digits is {odd_count}")


#find the smallest digit in a number

i=1
smallest=10
num=int(input("enter number:"))
while i<=num:
    digit=num%10
    if digit<smallest:
        smallest=digit
    num=num//10
print(smallest)

#FOR LOOP

#count how many vowels are given in a string

word=input("enter a word:")
v_count=0
c_count=0
for letter in word:
    if letter in "aeiou":
        v_count+=1
    else:
        c_count+=1
print(v_count)
print(c_count)

#print all prime numbers between 1 and n

num = int(input("enter the number:"))
for i in range(2, num + 1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)

#print all leap years between two given years

year_1 = int(input("enter first year:"))
year_2 = int(input("enter second year:"))
for i in range(year_1, year_2 + 1):
    if i % 4 == 0 and i %100 != 0 or i %400 == 0:
        print(i)


#Multiplication table of a number

num=int(input("enter the number:"))
for i in range(1,11):
    result=i*num
    print(f"{i}*{num}={result}")


#PATTERN

#Print a square pattern of stars.

for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

#Print an inverted right-angled triangle of stars.

for i in range(1,6):
    for j in range(i,6):
        print("*",end="  ")
    print()

#V shape pattern

n=int(input("enter the number of rows:"))
for i in range(n-1):
    print(" " * i + "*" + " " * 2 * (n - i - 1) + "*")
print(" " * (n-1) + "*")


       #2. JUMPING

#a) break

#Number is prime or not

num = int(input("enter the number:"))
flag = 0
if num<2:
    print("not prime")
else:
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    if flag==1:
        print("not prime")
    else:
        print("prime")

#b) continue

#calculate sum of n numbers,skip 3

n = int(input("enter the number:"))
sum = 0
for i in range(1,n+1):
    if i == 3:
        continue
    sum +=i
print(sum)

#c) pass

for i in "luminar technolab":
    if i == "t":
        pass
    print(i)



#FUNCTIONS

#ATM withrawal

def checking_pin():
    correct_pin = 1234
    attempts = 0
    while attempts < 3:
         pin = int(input())
         if pin == correct_pin:
             amount = int(input())
             return f"{amount} withdrawn successfully!"
         else:
             attempts += 1
             print("incorrect pin")
    return "f card is blocked due to {attempts} attempts"
res = checking_pin()
print(res)

#Bus ticket booking counter

def booking_seats():
    total = 30
    while total > 0:
        seats = int(input())
        if seats <= total:
            total -= seats
            print(f"{seats} seats booked. Seats left: {total}")
        else:
            print(f"cannot book {seats} seats only {total} seats are left")
    return f"Bus Full. No more bookings"
print(booking_seats())


#Employee ever time payment

def payment():
    total_hours = 0
    for i in range(1, 9):
        hours = int(input())
        total_hours += hours
    return total_hours * 200
res = payment()
print(f"total overtime payment to all employees: ₹{res}")


#Festival discount checker

def discount_checker(discount, item):
    if discount > 500:
        return f"Item {item} (₹{discount}) gets a discount"
    else:
        return f"Item {item} (₹{discount}) no discount"
for i in range(1, 11):
    discount = int(input())
    res = discount_checker(discount, i)
    print(res)


#First failing student

def first_fail():
    student = 1
    mark = int(input())
    while mark > 40:
        mark = int(input())
        student += 1
    return mark, student
marks, students = first_fail()
print(f"first failing student is student {students} with marks {marks}")


#longest occuring word in an array

lst1 = ["apple", "orange", "pineapple", "grape", "apple", "apple"]
def word_count(lst):
    max_count = 0
    word = ""
    for i in lst:
        count = 0
        for j in lst:
            if i == j:
                count += 1
        if count > max_count:
            max_count = count
            word = i
    return word
rs = word_count(lst1)
print(rs)


#Simple calculator

def add(num1, num2):
    sum = num1 + num2
    return sum
def sub(num1, num2):
    sub = num1 - num2
    return sub
def mul(num1, num2):
    mul = num1 * num2
    return mul
def div(num1, num2):
    div = num1/num2
    return div
print("1.addition\n2.subtraction\n3.multiplication\n4.division")
choice = int(input("enter the choice(1,2,3,4):"))
num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))
if choice == 1:
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == 2:
    print(f"{num1} - {num2} = {sub(num1, num2)}")
elif choice == 3:
    print(f"{num1} * {num2} = {mul(num1, num2)}")
elif choice == 4:
    print(f"{num1} / {num2} = {div(num1, num2)}")
else:
    print("invalid syntax")

#Language translator

def translate(word, lang):
    if word == "sun" and lang == "ml":
        return "സൂര്യൻ"
    elif word == "sun" and lang == "fr":
        return "Soleil"
    else:
        return "Traslation not available"
word = input()
lang = input()
print(translate(word, lang))


#Fitness app step goal

def step_goal():
    total = 0
    days = 0
    while total < 10000:
        steps = int(input())
        total += steps
        days += 1
    return total, days
tot, dy = step_goal()
print(f"goal reached! total steps: {tot} in {dy} days")


#COLLECTIONS

#1. LIST

#1. Given a list of numbers, create a new list with only even numbers.

lst =[2,9,6,7,4,10,50,5,3,7]
even_lst = []
for i in lst:
    if i % 2 == 0:
        even_lst.append(i)
print(even_lst)


#2. Sum all numbers in a list without using sum().

lst = [20, 90, 40, 60, 10]
sum = 0
for i in lst:
    sum += i
print(sum)


#3. Replace all negative numbers in a list with 0.

lst = [20, 90, 40, 60, 10, -1, -2, -3]
for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0
print(lst)


# 4. Merge two lists without using + operator.

lst = [20, 90, 40, 60, 10]
lst1 = [1,2,3,4,5]
lst.extend(lst1)
print(lst)


#5.  Remove duplicates from a list.

lst = [20, 90, 40, 60, 10, 20, 30, 90]
unique = []
for i in lst:
    if i not in unique :
        unique.append(i)
print(unique)


#6.  Check if a list is sorted or not.

lst = [20, 90, 40, 60, 10]
if lst == sorted(lst):
    print("sorted")
else:
    print("not sorted")


# 7. Given a list, rotate it by 1 element (last becomes first).
lst = [20, 90, 40, 60, 10]
last = lst.pop()
lst.insert(0, last)
print(lst)


# 8. Print the index of all occurrences of a value in a list.

lst = [20, 90, 40, 60, 10, 20, 60]
value = 60
for i in range(len(lst)):
    if lst[i] == value:
        print(i)


# 9. Create a new list containing squares of numbers.

lst = [20, 90, 40, 60, 10]
lst1 = []
for i in lst:
    lst1.append(i**2)
print(lst1)

# Remove all strings from a mixed list (numbers + strings).

lst = [20, "helo", 36, "no"]
lst1 = []
for i in lst:
    if type(i) != str:
        lst1.append(i)
print(lst1)


#2. TUPLE

# Create a tuple with 5 numbers and print it.

tu = (1,2,3,4,9)
print(tu)


# Access the first and last elements of a tuple.

tu = (1,2,3,4,9)
print(tu[0])
print(tu[4])

# Find the length of a tuple.

tu = (1,2,3,4,9)
print(len(tu))


# Check if a value exists in a tuple.

tu = (1,2,3,4,9)
value = 20
if value in tu:
    print("exists")
else:
    print("not exists")


# Concatenate two tuples.

tu = (1,2,3,4,9)
tu1 = (1,2,3,4,9)
sum = tu + tu1
print(sum)


# Repeat a tuple 3 times.

tu = (1,2,3,4,9)
tu_repeated = tu * 3
print(tu_repeated)


# Count how many times a value appears in a tuple.

tu = (20, 90, 30, 60, 20 , 70)
print(tu.count(20))


# Find the index of a value in a tuple.

tu = (20, 90, 30, 60, 20 , 70)
value = 20
index =[]
for i in range(len(tu)):
    if tu[i] == value:
        index.append(i)
print(index)


# Slice a tuple to get the middle elements.

tu = (20, 90, 30, 60, 20 , 70)


# Convert a tuple to a list.

tu = (20, 90, 30, 60, 20 , 70)
print(list(tu))

#3. SET

st = {10, 20, 30, 40}
print(st)
print(type(st))


st = set()
print(type(st))


#heterogeneous
st = {10, "hi", True}
print(st)


#duplicate values are not allowed
st = {10, 20, 20, 90, 80, 80}
print(st)

#insertion order is not preserved
#sets are immutable

st = {10, 20, 20, 90, 80, 80}
print(sum(st))
print(len(st))
print(max(st))
print(min(st))

#union ------combine unique elements

st = {1,2,3,4,5,6,7}
st1 = {5,6,7,8,9,10,11,12}
st3 = st.union(st1)
print(st3)

#intersection--------takes common elements


st3 = st.intersection(st1)
print(st3)

#difference------take element present in one set
st3 = st.difference(st1)
print(st3)


st3 = st1.difference(st)
print(st3)



#4. DICTIONARY

#RECURSIVE

pattern = "ABDFGBIKLMBFOS"
dic = {}
for i in pattern:
    if i  not in dic:
        dic[i] = 1
    else:
        print(f"repeated character is {i}")
        break

#WORD COUNT

values = "cat rat bat cat rat bat cat bat"
data = values.split(" ")
dic = {}
for i in data:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)




#FILE OPERATIONS

#1. READ

f = open(r"C:\Users\Athirakrishnan L\DATA ANALYTICS PYTHON\file operations\read\sample path2","r")

#prof dancer .... fname, lname, age

for i in f:
    data = i.rstrip("\n").split(",")
    prof = data[4]
    if prof == "Dancer":
        print(data[1:4])


#age range 25 to 40 .....fname, lame, age, prof, loc

for i in f:
    data = i.rstrip("\n").split(",")
    age = int(data[3])
    if 25 < age < 40:
        print(data[1:6])


#age above 50..... fname, lname, age

for i in f:
    data = i.rstrip("\n").split(",")
    age = int(data[3])
    if age > 50:
        print(data[1:4])


#loc = india .....fname, lname, age, prof

for i in f:
    data = i.rstrip("\n").split(",")
    loc = data[5]
    if loc == "india":
        print(data[1:5])


#loc = india age above 50 fname age loc

for i in f:
    data = i.rstrip("\n").split(",")
    loc = data[5]
    age = int(data[3])
    if loc == "india" and age > 50:
        print(data[1:6:2])


#loc = uk civil engineers.....fname lname age

for i in f:
    data = i.rstrip("\n").split(",")
    loc = data[5]
    prof = data[4]
    if loc == "uk" and prof == "Civil engineer":
        print(data[1:4])


#prof = pilot .....fname lname age

for i in f:
    data = i.rstrip("\n").split(",")
    prof = data[4]
    if prof == "Pilot":
        print(data[1:4])


#loc = us prof = teacher.....fname age

for i in f:
      data = i.rstrip("\n").split(",")
      loc = data[-1]
      prof = data[4]
      if loc == "us" and prof == "Teacher":
         print(data[1:4:2])


#uk work age above 50 .... all details

for i in f:
    data = i.rstrip("\n").split(",")
    loc = data[-1]
    age = int(data[3])
    if loc == "uk" and age > 50:
        print(data[:6])

#each prof count

dic = {}
for i in f:
    data = i.rstrip("\n").split(",")
    prof = data[4]
    if prof not in dic:
        dic[prof] = 1
    else:
        dic[prof] += 1
print(dic)


#each loc count

dic = {}
for i in f:
    data = i.rstrip("\n").split(",")
    loc = data[-1]
    if loc not in dic:
        dic[loc] = 1
    else:
        dic[loc] += 1
print(dic)


#each age group count

dic = {}
for i in f:
    data = i.rstrip("\n").split(",")
    age = int(data[3])
    if age not in dic:
        dic[age] = 1
    else:
        dic[age] += 1
for k,n in dic.items():
    print(k,",",n)


#2. WRITE

f = open("fruits","r")
f1 = open("fruits_write","w")
for i in f:
    if i != "apple\n":
        f1.write(i)

f = open("test","r")
f1 = open("copy_test","w")
for i in f:
    f1.write(i)


#FUNCTIONAL PROGRAMMING

#1. LAMBDA

#square of a number
sqr = lambda num1: num1 ** 2
print(sqr(20))


#multiply a number by 10

pro = lambda num1: num1 * 10
print(pro(12))

#multiply 3 numbers

mul1 = lambda num1, num2, num3: num1* num2 * num3
print(mul1(2,3,4))


#add 20 to a number

add = lambda num1: num1 + 20
print(add(40))


#2. MAP

#square of a number

lst = [2, 4, 5, 6, 7, 9]
rs1 = list(map(lambda num1: num1 ** 2, lst))
print(rs1)


#find the cube of each element

lst = [2, 4, 5, 6, 7, 9]
rs2 = list(map(lambda num1: num1 ** 3,lst))
print(rs2)


#add 10 to each element

lst = [2, 4, 5, 6, 7, 9]
rs3 = list(map(lambda num1: num1 + 10, lst))
print(rs3)


#3.FILTER

#1. square number less than 5
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num**2,filter(lambda num:num<5,lst)))
print(res)

#2. cube number divisible by 3
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num**3,filter(lambda num:num%3==0,lst)))
print(res)

#3. add 100 to each even number
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num+100,filter(lambda num:num%2==0,lst)))
print(res)

#4. subtrsct 2 from numbers greater than 4
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num-2,filter(lambda num:num>4,lst)))
print(res)

#5. double number less than 6
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num*2,filter(lambda num:num<6,lst)))
print(res)

#6. divide each number by 2
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num/2,lst))
print(res)

#7. subtract 3 from each odd numbers
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num-3,filter(lambda num:num%2!=0,lst)))
print(res)

#8. multiply each number by -1
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num*-1,lst))
print(res)

#9. add 50 to each number less than 10
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num+50,filter(lambda num:num<10,lst)))
print(res)

#10. multiply only numbers greater than 15 by 2
lst = [20, 5, 40, 35, 10, 19,3]
res = list(map(lambda num:num*2,filter(lambda num:num>15,lst)))
print(res)

#11. keep numbers divisible by both 2 and 3
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(filter(lambda num:num%2==0 and num%3==0,lst))
print(res)

#12. subtract 5 from each even number
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num-5,filter(lambda num:num%2==0,lst)))
print(res)


#4. LIST COMPREHENSION

# 1. Create a list 1-1000 elements
lst = [i for i in range(1, 1001)]
print(lst)
#
# 2. find all numbers from 1-500 that are divisible by 7
lst = [i for i in range(1,501) if i % 7 == 0]
print(lst)
#
# 3. find all of the numbers from 1-300 that have 3 in them
lst = [i for i in range(1, 301) if "3" in str(i)]
print(lst)
#
# 4. count number of spaces in a string
#    string = "practice list comprehension problem"

string = "practice list comprehension problem"
lst = [i for i in string if " " in i]
print(len(lst))


# 5.find total number of vowels in a string
string = "practice list comprehension problem"
vowels = "aeiouAEIOU"
lst = [i for i in string if i in vowels]
print(len(lst))


# 6. find all of the words in a string that are less than 4 letters
string = "practice list comprehension problem for a list"
lst = [i for i in string.split() if len(i) < 4]
print(lst)


# 7.weight above 2500 names
dic = {"bike":350,"car":2500,"jeep":3000,"bus":8000,"van":3000}
lst = [(i,dic[i]) for i in dic if dic[i] > 2500]
print(lst)

#13. square number greater than or equal to 9
lst = [9, 5, 10, 20, 15, 6]
res = list(map(lambda num:num**2,filter(lambda num:num>=9,lst)))
print(res)

#14. cube numbers less than 10
lst = [1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda num:num**3,filter(lambda num:num<10,lst)))
print(res)


#OOPS ----POLYMORPHISM, ENCAPSULATION, ABSTRACTION, INHERITANCE

#Library fine tracker

class Values():
    def library_charge(self):
        if days <= 5:
            charge = days * 2
        elif days < 10:
            charge = days * 3
        else:
            charge = days * 5
        return charge
ob = Values()
for i in range(1, 6):
    days = int(input())
    fine = ob.library_charge()
    print(f"member {i} fine: ₹{fine}")


#Movie ticket discount

class Values:
    def ticket_discount(self,age):
        if age < 12:
            discount = 50
        elif age <= 18:
            discount = 30
        elif age > 60:
            discount = 40
        else:
            discount = 0
        return discount
ob = Values()
for i in range(1, 6):
    age = int(input())
    res = ob.ticket_discount(age)
    print(f"customer {i} discount: {res}%")

#Parking charge

class Values:
    def parking_charge(self):
        hours = int(input())
        if hours == 1:
            charge = 20
        elif hours > 1:
            charge = 20 + (hours - 1) * 10
        else:
            return "exiting...."
        return charge
ob = Values()
res = ob.parking_charge()
print(res)



#Prime count and Factorial

class Values:
    def __init__(self,num):
        self.num = num
    def prime(self):
        count = 0
        for i in range(2, self.num + 1):
            for j in range(2, i):
                if i%j==0:
                    break
            else:
                count += 1
        return count
    def factorial(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact *= i
        return fact
num = int(input())
ob = Values(num)
rs = ob.prime()
print(f"prime count {rs}")
rs1 = ob.factorial()
print(f"factorial {rs1}")


#Restaurant order

class Values():
    def vegetarian_item_id(self):
        if id <= 5:
            return id
        return None
ob = Values()
for i in range(1, 8):
    id = int(input())
    res = ob.vegetarian_item_id()
    if res is not None:
        print(f"Vegetarian item ID: {res}")

#Average grade

class Values:
    def average_grade(self):
        total = 0
        n = int(input())
        for i in range(n):
            mark = int(input())
            total += mark
            average = total / n
        return average
ob = Values()
res = ob.average_grade()
print(f"average grade is {res}")


#Bank account system

class Bank_account:
    def __init__(self,name):
        self.account_holder = name
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
        print(f"deposited: {amount}")
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"withdraw: {amount}")
        else:
            print(f"insufficient balance")
    def display_account_details(self):
        print(f"account_holder : {self.account_holder}")
        print(f"balance: {self.balance}")
name = input()
acc = Bank_account(name)
dep = int(input())
acc.deposit(dep)
wd = int(input())
acc.withdraw(wd)
acc.display_account_details()
























































