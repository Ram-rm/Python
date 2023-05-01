# TODO challenge number 3,find the area of a tringle

# formula of triangle area=(base*height)/2

def area_of_triangle(base,height):
    area=(base*height)/2
    return area
base=float(input("Enter the base of triangle"))
height=float(input("Enter the height of triangle"))
print(area_of_triangle(base,height))
