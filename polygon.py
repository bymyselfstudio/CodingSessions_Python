import turtle as t


def draw_polygon(side_amount: int, side_length: int) -> None:

    angle = 360 / side_amount
    start_x = -100
    start_y = -100

    def turtlePause(duration: int) -> None:
        t.penup()
        t.hideturtle()
        for i in range(duration):
            t.speed(1)
            t.left(1)

    t.pensize(2)
    t.pencolor("black")
    t.speed(2)

    t.hideturtle()
    t.penup()
    t.goto(start_x, start_y)

    t.showturtle()
    t.pendown()

    for _ in range(side_amount):
        t.forward(side_length)
        t.left(angle)

    turtlePause(100)


def main() -> None:
    draw_polygon(10, 100)


if __name__ == "__main__":
    main()
