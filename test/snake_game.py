"""
贪吃蛇游戏 - 终端版
操作：方向键或 WASD 移动，Q 退出，P 暂停
"""

import curses
import random
import time

# 方向常量
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

OPPOSITE = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}

KEY_MAP = {
    curses.KEY_UP: UP, ord('w'): UP, ord('W'): UP,
    curses.KEY_DOWN: DOWN, ord('s'): DOWN, ord('S'): DOWN,
    curses.KEY_LEFT: LEFT, ord('a'): LEFT, ord('A'): LEFT,
    curses.KEY_RIGHT: RIGHT, ord('d'): RIGHT, ord('D'): RIGHT,
}


def draw_border(win, height, width):
    win.attron(curses.color_pair(3))
    win.border()
    win.attroff(curses.color_pair(3))


def display_width(s):
    """计算字符串在终端中的显示宽度（中文等宽字符占 2 列）"""
    w = 0
    for ch in s:
        w += 2 if ord(ch) > 0x7F else 1
    return w


def place_food(snake_set, height, width):
    # 可用格子数：(height-2) * (width-2)，若蛇占满则返回 None（胜利）
    total = (height - 2) * (width - 2)
    if len(snake_set) >= total:
        return None
    while True:
        pos = (random.randint(1, height - 2), random.randint(1, width - 2))
        if pos not in snake_set:
            return pos


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)   # 蛇身
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)     # 食物
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # 边框
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)    # UI 文字
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)   # 蛇头

    max_y, max_x = stdscr.getmaxyx()
    height, width = min(24, max_y), min(60, max_x)
    start_y = (max_y - height) // 2
    start_x = (max_x - width) // 2

    win = curses.newwin(height, width, start_y, start_x)
    win.keypad(True)
    win.nodelay(True)

    def new_game():
        cy, cx = height // 2, width // 2
        snake = [(cy, cx), (cy, cx - 1), (cy, cx - 2)]
        snake_set = set(snake)
        direction = RIGHT
        food = place_food(snake_set, height, width)
        score = 0
        speed = 0.15
        return snake, snake_set, direction, food, score, speed

    snake, snake_set, direction, food, score, speed = new_game()
    paused = False
    game_over = False
    last_move = time.time()

    while True:
        key = win.getch()

        if key == ord('q') or key == ord('Q'):
            break

        if key == ord('p') or key == ord('P'):
            paused = not paused

        if game_over and key == ord('r'):
            snake, snake_set, direction, food, score, speed = new_game()
            game_over = False
            paused = False
            last_move = time.time()

        if not game_over and not paused:
            new_dir = KEY_MAP.get(key)
            if new_dir and new_dir != OPPOSITE.get(direction):
                direction = new_dir

            now = time.time()
            if now - last_move >= speed:
                last_move = now
                head = snake[0]
                new_head = (head[0] + direction[0], head[1] + direction[1])

                # 碰墙检测
                if (new_head[0] <= 0 or new_head[0] >= height - 1 or
                        new_head[1] <= 0 or new_head[1] >= width - 1):
                    game_over = True
                # 碰自身：排除尾巴（尾巴会移走，不算碰撞）
                elif new_head in snake_set and new_head != snake[-1]:
                    game_over = True
                else:
                    snake.insert(0, new_head)
                    snake_set.add(new_head)
                    if new_head == food:
                        score += 10
                        speed = max(0.05, speed - 0.002)
                        food = place_food(snake_set, height, width)
                        if food is None:  # 蛇填满地图，胜利
                            game_over = True
                    else:
                        tail = snake.pop()
                        snake_set.discard(tail)

        # 绘制
        win.erase()
        draw_border(win, height, width)

        # 食物
        win.attron(curses.color_pair(2) | curses.A_BOLD)
        win.addch(food[0], food[1], '●')
        win.attroff(curses.color_pair(2) | curses.A_BOLD)

        # 蛇身
        win.attron(curses.color_pair(1))
        for seg in snake[1:]:
            win.addch(seg[0], seg[1], '■')
        win.attroff(curses.color_pair(1))

        # 蛇头
        win.attron(curses.color_pair(5) | curses.A_BOLD)
        win.addch(snake[0][0], snake[0][1], '◆')
        win.attroff(curses.color_pair(5) | curses.A_BOLD)

        # 状态栏
        win.attron(curses.color_pair(4))
        status = f" 分数: {score}  长度: {len(snake)}  速度: {int((0.15 - speed) / 0.002 + 1)} "
        try:
            win.addstr(0, 2, status[:width - 4])
        except curses.error:
            pass
        win.attroff(curses.color_pair(4))

        if paused:
            msg = "  Paused - P to continue  "
            win.attron(curses.color_pair(4) | curses.A_BOLD)
            try:
                win.addstr(height // 2, (width - display_width(msg)) // 2, msg)
            except curses.error:
                pass
            win.attroff(curses.color_pair(4) | curses.A_BOLD)

        if game_over:
            win_msg = food is None
            lines = (
                ["  YOU WIN!  ", f"  Score: {score}  ", "  R: Restart  Q: Quit  "]
                if win_msg else
                ["  GAME OVER  ", f"  Score: {score}  ", "  R: Restart  Q: Quit  "]
            )
            color = curses.color_pair(1) if win_msg else curses.color_pair(2)
            win.attron(color | curses.A_BOLD)
            for i, line in enumerate(lines):
                y = height // 2 - 1 + i
                x = (width - display_width(line)) // 2
                try:
                    win.addstr(y, max(0, x), line)
                except curses.error:
                    pass
            win.attroff(color | curses.A_BOLD)

        # 操作提示
        hint = " WASD/方向键移动  P暂停  Q退出 "
        win.attron(curses.color_pair(4))
        try:
            win.addstr(height - 1, 2, hint[:width - 4])
        except curses.error:
            pass
        win.attroff(curses.color_pair(4))

        win.refresh()
        time.sleep(0.01)


if __name__ == '__main__':
    curses.wrapper(main)
