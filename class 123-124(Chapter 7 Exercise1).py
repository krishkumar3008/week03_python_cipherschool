# return a dictionary containing cube of numbers from 1 to n

# example

#cube_finder
#(1:1, 2:8, 3:27)
def cube(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i]=i**3
    return cubes
cube(10)
print(cube(10))