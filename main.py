# Must Exercises — 10
# 1. Manager son price
manager_son_price = lambda price,is_manager_son:price *0.80 if is_manager_son == True else price + price*0.17
print(manager_son_price(100,True)) 
print(manager_son_price(100,False)) 

# 2. Final price after discount
final_price = lambda price,discount: price - price/100*discount if 0<discount<100 else None
print(final_price(100,120))
print(final_price(200,10))

# 3. Full name
full_name = lambda first_name, last_name: f"{first_name} {last_name}"
print(full_name("dana","levi")) 

# 4. Grade status
grade_status = lambda grade: "pass" if grade >=55 else "fail"
print(grade_status(80))
print(grade_status(40))

# 5. Larger number
larger = lambda num1,num2: num1 if num1 >= num2 else num2
print(larger(10,7))
print(larger(5,9))
print(larger(4,4))

# 6. Distance from 10
distance_from_10 = lambda num: num - 10 if num > 10 else 10-num
print(distance_from_10(6))
print(distance_from_10(100))

# 7. Get item total
item_total= lambda item: item["price"]*item["amount"]
print(item_total({"name": "Pen", "price": 5, "amount": 10}))

# 8. Turn a regular complex function into a lambda
shipping_cost = lambda weight, express: 50 if express and weight >5 else 30 if express else 25 if weight >5 else 10
print(shipping_cost(3,True))
print(shipping_cost(8,True))
print(shipping_cost(8,False))
print(shipping_cost(2,False))

# 9. Turn a regular complex function into a lambda
access_message = lambda age, has_ticket, is_vip: "vip entrance" if is_vip else "regular entrance" if age >= 18 and has_ticket else "buy ticket" if age >= 18 else "too young"
print(access_message(25,True,False)) 
print(access_message(25,False,False)) 
print(access_message(15,True,False)) 
print(access_message(15,False,True)) 

# 10. Turn a complex lambda into a regular function
def ticket_price(age,is_student):
    if age <12:
        return 20
    elif is_student:
        return 30
    else:
        return 50
print(ticket_price(10, False))
print(ticket_price(20, True))    
print(ticket_price(20, False))    

# Self-Learn Section — Lambda with Sort
# A. Sort numbers normally
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)

# B. Sort tuples by second value
students = [
    ("Dana", 85),
    ("Eli", 92),
    ("Noa", 78)]
students.sort(key=lambda student:student[1])
print(students)

# C. Sort dictionaries by one field
students = [
    {"name": "Dana", "grade": 85},
    {"name": "Eli", "grade": 92},
    {"name": "Noa", "grade": 78}]
students.sort(key=lambda student:student["grade"])
print(students)

# D. Sort dictionaries by calculated value
products = [
    {"name": "Pen", "price": 5, "amount": 10},
    {"name": "Book", "price": 40, "amount": 2},
    {"name": "Bag", "price": 80, "amount": 1}]
products.sort(key=lambda product:product["price"]*product["amount"])
print(products)

