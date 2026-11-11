from turtle import \
    fillcolor, begin_fill, end_fill, \
    forward, right, pos

fillcolor("red")
begin_fill()

while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break

end_fill()
