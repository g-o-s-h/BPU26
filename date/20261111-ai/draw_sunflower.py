from turtle import \
    color, begin_fill, end_fill, \
    forward, left, pos, done

color("red", "yellow")
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
done()
