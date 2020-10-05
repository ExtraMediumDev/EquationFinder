def parabola(x1,y1,x2,y2,x3,y3):
    #finding (a,b,c)
    def equation(a1,b1,a2,b2,a3,b3):
        try:
            coefficient = (b1-b2-(a1**2-b2**2))/(a1-b2)
        except ZeroDivisionError:
            coefficient = 0
        try:
            a = (b2 - b3)/(a2**2-a3**2 + coefficient)
        except ZeroDivisionError:
            a = 0
        b = coefficient * a
        c = b1 - a * (a1**2) - b * a1
        #formatting
        if b < 0:
            b_operator = '-'
        else:
            b_operator = '+'
        if c < 0:
            c_operator = '-'
        else:
            c_operator = '+'
        
        return (a,b,c, b_operator, c_operator)

    def format(x,y):
        equation = '{} = {}{}^2 {} {}{} {} {}'.format(y, round(a,2), x, b_operator, abs(round(b,2)), x, c_operator, abs(round(c,2)))
        return equation

    if x1<x2<x3:
        a,b,c,b_operator,c_operator = equation(x1,y1,x2,y2,x3,y3)
        return format('x','y')
    else:
        a,b,c,b_operator,c_operator = equation(y1,x1,y2,x2,y3,x3)
        return format('y','x')


def line(x1,y1,x2,y2):
    #finding m and b
    try:
        m = (y2-y1)/(x2-x1)
    except ZeroDivisionError:
        m = None
    if m == None:
        equation = 'x = {}'.format(x1)
    else:
        b = y1 - m*x1
        equation = 'y = {}x + {}'.format(m,b)

    return equation


def ellipse(cx,cy,a,b):
    equation = "((x-{})/{})^2 + ((y-{})/{})^2 = 1".format(cx, a, cy, b)
    
    return equation

def prompt1():
    equation_type = input("p = parabola equation, l = linear equation, e = ellipse/circle equation. Please type on of the following letters (p,l,e).")
    return equation_type

run = True
equ = prompt1()
while run == True:
    if equ == 'p' or equ == 'l' or equ == 'e':
        try:
            if equ == 'p':
                x1 = float(input("x1:"))
                y1 = float(input('y1:'))
                x2 = float(input('x2:'))
                y2 = float(input('y2:'))
                x3 = float(input('x3:'))
                y3 = float(input('y3:'))
                answer = 'equation: {}'.format(parabola(x1,y1,x2,y2,x3,y3))

            if equ == 'l':
                x1 = float(input('x1:'))
                y1 = float(input('y1:'))
                x2 = float(input('x2:'))
                y2 = float(input('y2:'))
                answer = 'equation: {}'.format(line(x1,y1,x2,y2))

            if equ == 'e':
                cx = float(input('center x='))
                cy = float(input('center y='))
                a = float(input('vertical radius='))
                b = float(input('horizontal radius='))
                answer = 'equation: {}'.format(ellipse(cx,cy,a,b))
            
            key = input('{} | Input x to close or any other key to try again:'.format(answer))
            if key == 'x':
                run = False
            else:
                equ = prompt1()
        except:
            print('An error has occured. Only numbers are allowed as inputs.')
    else:
        equ = input('Please try again. Type out one of the following letters (p,l,e).')
