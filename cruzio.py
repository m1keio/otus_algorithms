import math


def cast(x_axis: int = 25, y_axis: int = 25, formula: str = "", num: str = ""):
    print(f"==== ~*..~*..~*..~*..~ cast number: {num}")
    for x in range(x_axis):
        for y in range(y_axis):
            if eval(formula):
                print("# ", end="")
            else:
                print(". ", end="")
        print("\n")


cast(formula="x<y", num="1")
cast(formula="x==y", num="2")
cast(formula="x+y==24", num="3")
cast(formula="(y < 6 or x < 6 or (y >= 6 and x < 25-(y-6)))", num="4")
cast(formula="y == x*2 or y == x*2+1", num="5")
cast(formula="y < 10 or (y >= 10 and x <=10)", num="6")
cast(formula="y > 15 and x > 15", num="7")
cast(formula="x*y == 0", num="8")
cast(formula="x==1 or x==23 or y == 1 or y == 23", num="11")
cast(formula="((x+y>0) and y == x*y) or ((x+y>0) and x == x*y)", num="18")
cast(formula="x*y==0 or (x==24 or y==24)", num="19")
cast(formula="y % 2 == 0", num="20")
cast(formula="x==y or x+y==24", num="24")
