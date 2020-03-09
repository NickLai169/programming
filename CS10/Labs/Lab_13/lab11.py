import turtle


def exponent(num, power):
    return num**power

def reverse_string(str):
    return str[::-1]

def palindrome(string):
    if string == '':
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return palindrome(string[1:-1])

def draw_c_curve(lv, length):
    turtle.pendown()
    if lv == 1:
        turtle.forward(length)
    else:
        turtle.left(45)
        draw_c_curve(lv-1, length/(2**(1/2)))
        turtle.right(90)
        draw_c_curve(lv-1, length/(2**(1/2)))
        turtle.left(45)
