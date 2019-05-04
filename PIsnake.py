#!/usr/bin/python

import random
import curses
i = int(input("Speed in ms (lesser the input greater the speed)="))
s = curses.initscr()
curses.curs_set(0)
sht, sw = s.getmaxyx()
w = curses.newwin(sht, sw, 0, 0)
w.keypad(1)
w.timeout(i)

sk_x = sw/4
sk_y = sht/2
snake = [
    [sk_y, sk_x],
    [sk_y, sk_x-1],
]

food = [sht//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sht] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1

    if key == curses.KEY_UP:
        new_head[0] -= 1

    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
            random.randint(1, sht-1),
            random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

