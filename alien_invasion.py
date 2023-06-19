import sys

import pygame

class AlienInvasion:
    """Класс дял управления ресурсами и поведением игры"""
    
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        #Назначение цвета фона
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Запуск основоного цикла инры"""
        while True:
            #Отслеживание событий клавиатуры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.bg_color)        
            #Отображение последнего проресованного экрана
            pygame.display.flip()
            
if __name__ == '__main__':
    #Создание экземплара и запуск игры
    ai = AlienInvasion()
    ai.run_game()