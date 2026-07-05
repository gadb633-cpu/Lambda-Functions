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

# 