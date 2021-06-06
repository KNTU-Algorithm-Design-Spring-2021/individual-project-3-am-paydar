from turtle import *
from time import *


def number_to_point(n):
    x = (n % 5 * 50 + 25) - 125
    y = (n // 5 * 50) - 125
    return x, y


def point_to_number(x, y):
    row = (y + 125) // 50
    col = (x + 125) // 50
    n = int(row * 5 + col)


def show_number(n):
    lt(90)
    fd(12.5)
    write(n)
    bk(12.5)
    rt(90)


def draw_circle(n):
    if n != 1:
        pensize(2)
        color("purple")
        pendown()
    else:
        pu()
    goto(number_to_point(n))
    pensize(6)
    color("black")

    pu()
    show_number(n)
    pendown()
    circle(18)
    penup()


def graphic_routing(result):
    draw_circle(1)
    for i in result:
        draw_circle(i)


def get_data():
    data = [[False for i in range(21)]
            for j in range(21)]
    visited = [False for i in range(21)]
    visited[1] = True
    end_point = int(input())
    while True:
        a, b = input().split()
        a = int(a)
        b = int(b)
        if a == 0 and b == 0:
            break
        data[a][b] = True
        data[b][a] = True
    return data, end_point, visited


def reach_end_point(begin_point, end_point):
    if begin_point == end_point:
        print("1 ", end="")
        print(*result, sep=" ")
        graphic_routing(result)
        sleep(5)
        clear()
        return
    for source in range(1, 21):
        # print(data[begin_point][source])
        # print("***********************")
        if way[begin_point][source] and (not visited[source]):
            result.append(source)
            visited[source] = True
            # print("Append")
            # print(*result)
            reach_end_point(source, end_point)
            result.remove(source)
            visited[source] = False
            # print("Remove")
            # print(*result)


def main():
    pu()
    speed(10)
    pensize(6)
    global way, visited, result
    while True:
        way, end_point, visited = get_data()
        result = []
        reach_end_point(1, end_point)


if __name__ == "__main__":
    main()
