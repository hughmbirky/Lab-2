def polygon(n):
    import turtle
    wn = turtle.Screen()
    wn.title("Lab 2 turt")

    WeLit = turtle.Turtle()
    WeLit.color("pink")
    WeLit.pensize(5)

    for i in range(n):
        WeLit.forward(100)
        WeLit.left(360/n)

    wn.mainloop()

polygon(25)