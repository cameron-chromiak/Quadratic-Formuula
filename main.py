#does quadratic formula
#sqrt = "\u221a"
#+-
    
def calculateDenom(a):
    calc = a*2
    return calc
    
def calculateNum(a, b, c):
    print( a, b, c)
    calc = b**2 - (4*a*c)
    return calc

def main():
    try:
        aValue = int(input("a Value: "))
        bValue = int(input("b Value: "))
        cValue = int(input("c Value: "))
    except ValueError:
        print("Numbers only" "\n")
        main()                 

    numerator = calculateNum(aValue, bValue, cValue)
    #print(numerator)
    denom = calculateDenom(aValue)
    #print(denom)

    print("-",bValue, "+- \u221a(",numerator)
    print("         ----------------")
    print("       ",denom)
        
main()
