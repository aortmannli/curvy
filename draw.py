"""from display import *
from matrix import *

import math

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    while (t < 1):
        add_edge(points, int(r * math.cos(2*math.pi*t) + cx),int(r * math.sin(2*math.pi*t) + cy),0, int(r * math.cos(2*math.pi*(t+step)) + cx),int(r * math.sin(2*math.pi*(t+step)) + cy),0)
        t+=step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if curve_type == 'bezier':
        ax = (-1*x0)+(3*x1)-(3*x2)+x3
        bx = (3*x0)-(6*x1)+(3*x2)
        cx = (-3*x0)+(3*x1)
        dx = x0
        ay = (-1*y0)+(3*y1)-(3*y2)+y3
        by = (3*y0)-(6*y1)+(3*y2)
        cy = (-3*y0)+(3*y1)
        dy = y0
    else:
        helper = [[2,-3,0,1],[-2,3,0,0],[1,-2,1,0],[1,-1,0,0]]
        x = [[x0,x1,x2,x3]]
        y = [[y0,y1,y2,y3]]
        matrix_mult(helper, x)
        matrix_mult(helper, y)
        ax = x[0][0]
        bx = x[0][1]
        cx = x[0][2]
        dx = x[0][3]
        ay = y[0][0]
        by = y[0][1]
        cy = y[0][2]
        dy = y[0][3]
    t = 0
    while t < 1:
        xThis = (ax*t*t*t)+(bx*t*t)+(cx*t)+dx
        yThis = (ay*t*t*t)+(by*t*t)+(cy*t)+dy
        xNext = (ax*(t+step)*(t+step)*(t+step))+(bx*(t+step)*(t+step))+(cx*(t+step))+dx
        yNext = (ay*(t+step)*(t+step)*(t+step))+(by*(t+step)*(t+step))+(cy*(t+step))+dy
        add_edge(points, xThis, yThis, 0, xNext, yNext, 0)
        t += step



def bezier():
    ax = (-1*x0)+(3*x1)-(3*x2)+x3
    bx = (3*x0)-(6*x1)+(3*x2)
    cx = (-3*x0)+(3*x1)
    dx = x0
    ay = (-1*y0)+(3*y1)-(3*y2)+y3
    by = (3*y0)-(6*y1)+(3*y2)
    cy = (-3*y0)+(3*y1)
    dy = y0

def hermite(p0,p1,r0,r1):
    helper = [[2,-3,0,1],[-2,3,0,0],[1,-2,1,0],[1,-1,0,0]]
    xVal = [[x0,x1,x2,x3]]
    yVal = [[y0,y1,y2,y3]]
    matrix_mult(helper, xVal)
    matrix_mult(helper, yVal)
    ax = xVal[0][0]
    bx = xVal[0][1]
    cx = xVal[0][2]
    dx = xVal[0][3]
    ay = yVal[0][0]
    by = yVal[0][1]
    cy = yVal[0][2]
    dy = yVal[0][3]

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line"""

from display import *
from matrix import *

import math

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    while (t < 1):
        add_edge(points, int(r * math.cos(2*math.pi*t) + cx),int(r * math.sin(2*math.pi*t) + cy),0, int(r * math.cos(2*math.pi*(t+step)) + cx),int(r * math.sin(2*math.pi*(t+step)) + cy),0)
        t+=step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    coeffs = list()
    if curve_type == 'bezier':
        coeffs = bezier( x0, y0, x1, y1, x2, y2, x3, y3)
    else:
        coeffs = hermite( x0, y0, x1, y1, x2, y2, x3, y3)

    ax = coeffs[0]
    bx = coeffs[1]
    cx = coeffs[2]
    dx = coeffs[3]
    ay = coeffs[4]
    by = coeffs[5]
    cy = coeffs[6]
    dy = coeffs[7]
    t = 0
    while t < 1:
        xThis = (ax*t*t*t)+(bx*t*t)+(cx*t)+dx
        yThis = (ay*t*t*t)+(by*t*t)+(cy*t)+dy
        xNext = (ax*(t+step)*(t+step)*(t+step))+(bx*(t+step)*(t+step))+(cx*(t+step))+dx
        yNext = (ay*(t+step)*(t+step)*(t+step))+(by*(t+step)*(t+step))+(cy*(t+step))+dy
        add_edge(points, xThis, yThis, 0, xNext, yNext, 0)
        t += step



def bezier( x0, y0, x1, y1, x2, y2, x3, y3):
    coeff = list()
    coeff.append((-1*x0)+(3*x1)-(3*x2)+x3) #ax
    coeff.append((3*x0)-(6*x1)+(3*x2)) #bx
    coeff.append((-3*x0)+(3*x1)) #cx
    coeff.append(x0) #dx
    coeff.append((-1*y0)+(3*y1)-(3*y2)+y3) #ay
    coeff.append((3*y0)-(6*y1)+(3*y2)) #by
    coeff.append((-3*y0)+(3*y1)) #cy
    coeff.append(y0) #dy
    return coeff

def hermite( x0, y0, x1, y1, x2, y2, x3, y3):
    crabby = [[2,-3,0,1],[-2,3,0,0],[1,-2,1,0],[1,-1,0,0]]
    x = [[x0,x1,x2,x3]]
    y = [[y0,y1,y2,y3]]
    matrix_mult(crabby, x)
    matrix_mult(crabby, y)
    #ax.bx.cx.dx.ay.by.cy.dx
    return [x[0][0],x[0][1],x[0][2],x[0][3],y[0][0],y[0][1],y[0][2], y[0][3]]
   
def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )




def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
