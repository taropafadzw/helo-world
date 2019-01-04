import turtle

my_turtle=turtle.Turtle()
my_turtle.speed(0)

def square(n ,x):

       for i in range(4): 
        my_turtle.forward(n)
        my_turtle.right(x)

def triangle(b,z):
        my_turtle.forward(b)
        my_turtle.right(z)
        
for i in range(400):
     square(100,90)
     my_turtle.right(11)

     triangle(100,60)
    

    

