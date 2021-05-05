#1
#def number_of_food_groups():
#    return 5
#print(number_of_food_groups())
#prediction: 5

#2
#def number_of_military_branches():
#    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#prediction: 5
"""
train of thought for prediction: number_of_days_in_a_week_silicon_or_triangle_sides() was undefined, 
so it would be a blank value, plus the defined 5 of the number_of_military_branches() = to 5.
"""

#3
#def number_of_books_on_hold():
#    return 5
#    return 10
#print(number_of_books_on_hold())
#prediction: 10
"""
train of thought for prediction: return was defined twice, 
so thought it would push from 5 -> 10 since that was the most recent return, however, unlike a variable, 
there is no set (=) so my guess is that unless a specific call for the second return occurs, the first return
will override the second since it came first in the sequence.
"""

#4
#def number_of_fingers():
#    return 5
#    print(10)
#print(number_of_fingers())
#prediction: 10, 5
"""
train of thought for prediction: print function called on two separate occasions, so would print both;
however, because the second print is located inside the function rather than out, there is no return command
for it, so it does not print. 
"""

#5
#def number_of_great_lakes():
#    print(5)
#x = number_of_great_lakes()
#print(x)
#prediction: error 
"""
train of thought for prediction: number_of_great_lakes is undefined in the parameter and there is no applied argument 
to the calling. There is no return command for the print statement, and it is located inside the function, so it doesn't apply it. 
"""

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#prediction: 8
"""
train of thought for prediction: arguments defined in print statement. 
I don't understand the error : TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType' - can you go over this error with me?
"""
#7
#def concatenate(b,c):
#    return str(b)+str(c)
#print(concatenate(2,5))
#prediction: 7
"""
train of thought for prediction: arguments defined in print statement for the return
command.
"""

#8
#def number_of_oceans_or_fingers_or_continents():
#    b = 100
#    print(b)
#    if b < 10:
#        return 5
#    else:
#        return 10
#    return 7
#print(number_of_oceans_or_fingers_or_continents())
#prediction: 100, 10

#9
#def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#    if b<c:
#        return 7
#    else:
#        return 14
#    return 3
#print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
#print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#prediction: 7, 14, 7, 14
"""
train of thought for prediction: arguments defined in print statement for the return
command.
"""

#10
#def addition(b,c):
#    return b+c
#    return 10
#print(addition(3,5))
#prediciton: 8


#11
#b = 500
#print(b)
#def foobar():
#    b = 300
#    print(b)
#print(b)
#foobar()
#print(b)
#prediction: 500, 300, 300, error foobar undefined, 300
"""
train of thought for prediction: The value of b was changed from 500 to 300 within 
the function and foobar did not have an argument specifed in the print statement.
"""

#12
#b = 500
#print(b)
#def foobar():
#    b = 300
#    print(b)
#    return b
#print(b)
#foobar()
#print(b)
#prediction: 500, 500, 300, 300, 300 
"""
train of thought for prediction: The value of b was changed from 500 to 300 within 
the function after the second print(b) because of the return command.
"""

#13
#b = 500
#print(b)
#def foobar():
#    b = 300
#    print(b)
#    return b
#print(b)
#b=foobar()
#print(b)
#prediction: 500, 500, 300, 300, 300
"""train of thought for prediction: there's 4 print b's and 1 call for the function
that sets foobar to b
"""

#14
#def foo():
#    print(1)
#    bar()
#    print(2)
#def bar():
#    print(3)
#foo()
#prediction: error
"""train of thought for prediction: neither foo nor bar is defined"""


#15
#def foo():
#    print(1)
#    x = bar()
#    print(x)
#    return 10
#def bar():
#    print(3)
#    return 5
#y = foo()
#print(y)
#prediction: 1, 5, 10, 10
"""
train of thought for prediction: followed order of code lines, starting with def, and only did the returns because 
I thought print didn't occur unless a return statement happened
"""