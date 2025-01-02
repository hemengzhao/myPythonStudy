import pygame
import random
import sys

# 初始化 Pygame
pygame.init()
# 初始化和常量定义

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 设置游戏窗口
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20  # 蛇身和食物的大小
GAME_SPEED = 15  # 游戏速度

# 创建游戏窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('贪吃蛇游戏')

# 蛇类
class Snake:
    def __init__(self):
        # 初始化蛇的身体和方向，起始位置在屏幕中央
        self.body = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = "RIGHT" # 初始移动方向
        self.change_to = self.direction # 准备改变的方向

    def change_direction(self):
        # 改变方向的逻辑，防止蛇直接向反方向移动
        # 例如：向右移动时不能直接向左转
        if self.change_to == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif self.change_to == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif self.change_to == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif self.change_to == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"

    def move(self, grow=False):
        # 根据当前方向移动蛇头
        x, y = self.body[0]
        if self.direction == "RIGHT":
            x += BLOCK_SIZE
        elif self.direction == "LEFT":
            x -= BLOCK_SIZE
        elif self.direction == "UP":
            y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            y += BLOCK_SIZE

        self.body.insert(0, (x, y)) # 在头部插入新位置
        if not grow:
            self.body.pop() # 如果没有吃到食物，删除尾部

    def check_collision(self):
        x, y = self.body[0]
        # 检查是否撞墙
        if x < 0 or x >= WINDOW_WIDTH or y < 0 or y >= WINDOW_HEIGHT:
            return True
        # 检查是否撞到自己
        if (x, y) in self.body[1:]:
            return True
        return False

# 食物类
class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        # 随机生成食物位置，位置必须对齐网格
        x = random.randrange(0, WINDOW_WIDTH, BLOCK_SIZE)
        y = random.randrange(0, WINDOW_HEIGHT, BLOCK_SIZE)
        return (x, y)

    def respawn(self):
        # 重新生成食物位置
        self.position = self.generate_position()

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0

    while True:
        # 1. 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 处理退出事件
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 处理键盘输入
                # 更新蛇的移动方向
                if event.key == pygame.K_RIGHT:
                    snake.change_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    snake.change_to = "LEFT"
                elif event.key == pygame.K_UP:
                    snake.change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    snake.change_to = "DOWN"

        # 2. 游戏逻辑更新
        snake.change_direction()
        # 检查是否吃到食物
        grow = False
        if snake.body[0] == food.position:
            grow = True
            score += 1
            food.respawn()
        snake.move(grow)

        # 3. 碰撞检测
        if snake.check_collision():
            pygame.quit()
            sys.exit()

        # 4. 绘制游戏画面
        screen.fill(BLACK)  # 清空屏幕
        # 绘制食物
        pygame.draw.rect(screen, RED, (food.position[0], food.position[1], 
                                     BLOCK_SIZE, BLOCK_SIZE))
        # 绘制蛇
        for pos in snake.body:
            pygame.draw.rect(screen, GREEN, (pos[0], pos[1], 
                                          BLOCK_SIZE, BLOCK_SIZE))
        # 显示分数
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'得分: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()  # 更新显示
        clock.tick(GAME_SPEED)  # 控制游戏速度

if __name__ == "__main__":
    main()