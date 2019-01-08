import pygame                   # 导入pygame库
from pygame.locals import *     # 导入pygame库中的一些常量
from sys import exit            # 导入sys库中的exit函数

# 定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
  
# 初始化游戏
pygame.init()                   # 初始化pygame
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])     # 初始化一个用于显示的窗口
pygame.display.set_caption('This is my first pygame-program')       # 设置窗口标题

#事件循环(main loop)
while True:
    
    # 处理游戏退出
    # 从消息队列中循环取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()