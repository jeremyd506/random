#! /usr/lib/python3.9
import math
from fractions import Fraction

def rectangle(boardLength):    
    goldenRatio = 1.618
    counter = float(boardLength)
    height = 0
    width = 0
    while math.isclose(goldenRatio, round(counter,3)) == False:
        height = float(boardLength)/counter
        counter -= .001

    counter = height  

    while math.isclose(goldenRatio,round(width,3)) == False:
        width = height/counter
        counter -= .001

    width = counter 
    height = round(height/2,2)
    width = round(width/2,2)

    print ("Original Height is: " + str(height))
    print ("Original Width is: " + str(width))
    roundHeight = round(height)
    roundWidth = round(width)
    totalLength = roundHeight*2 + roundWidth*2

    if totalLength <= float(boardLength):
        print("Round measurement will fit in board length")
        print("Round Height is: " + str(roundHeight)) 
        print("Round Width is: " + str(roundWidth))
    else: 
        print("Round measurements will NOT fit in board length, use decimal measurements")
    if height < 1:
        print("Height is: " + str(Fraction(height).limit_denominator(10)))
    else:
        decimal,integer = math.modf(height)
        print("Height is: " + str(round(integer)) + " " + str(Fraction(decimal).limit_denominator(10)))
    if width < 1:
        print("Width is: " + str(Fraction(width).limit_denominator(10)))
    else:
        decimal,integer = math.modf(width)
        print("Width is: " + str(round(integer)) + " " + str(Fraction(decimal).limit_denominator(10)))


boardLength = input("Enter Board Length:")

rectangle(boardLength)
