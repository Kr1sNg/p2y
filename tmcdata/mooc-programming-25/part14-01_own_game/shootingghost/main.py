# This is a point and click shooter where you move your robot around
# with arrow keys and use your mouse to shoot at the ghosts.
# Shooting ghosts yields points while being hit by one negates points.
# As you gather points you move to next levels making the game harder
# by spawning ghosts faster and making them move faster.
# Gather 100 points to win the game!

import pygame
from random import randint, choice
from math import sqrt

robot = pygame.image.load("robot.png")
coin = pygame.image.load("coin.png")
monster = pygame.image.load("monster.png")
clock = pygame.time.Clock()

class RobotVsGhosts:
    def __init__(self):
        pygame.init()

        self.new_game()

        self.window = pygame.display.set_mode((800, 650))

        pygame.display.set_caption("Robot versus Ghosts")
        
        self.game_font = pygame.font.SysFont("Arial", 24)
        
        self.main_loop()
    
    def new_game(self):
        self.player = Robot()
        self.direction = [False, False, False, False]
        self.spawntimer = 0
        self.ghosts = []
        self.points = 0
        self.shots = 5
        self.bullets = []
        self.reloadtimer = 0
        self.mx = 0
        self.my = 0
        self.difficulty = 0
        self.pause = False

    def main_loop(self):
        while True:
            self.check_events()
            self.spawn_ghost()
            self.move()
            self.player.contain()
            self.move_ghosts()
            self.move_bullets()
            self.hitboxcheck()
            self.reload()
            self.level_up()
            self.draw()
            self.game_over()
            clock.tick(60)

    def draw(self):
        self.window.fill((69, 69, 69))
        if self.pause:
            if self.points > 0:
                self.text5 = self.game_font.render("                    Congratualtions!", True, (0, 0, 0))
                self.window.blit(self.text5, (230, 200))
                self.text5 = self.game_font.render("You have 100 points and won the game!", True, (0, 0, 0))
                self.window.blit(self.text5, (230, 240))
                self.text5 = self.game_font.render("               Press N for New Game", True, (0, 0, 0))
                self.window.blit(self.text5, (230, 280))
            else:
                self.text5 = self.game_font.render("               Oh no, Game Over!", True, (0, 0, 0))
                self.window.blit(self.text5, (230, 200))
                self.text5 = self.game_font.render("You ran out of points and blacked out!", True, (0, 0, 0))
                self.window.blit(self.text5, (230, 240))
                self.text5 = self.game_font.render("            Press N for New Game", True, (0, 0, 0))
                self.window.blit(self.text5, (230, 280))
        else:
            self.window.blit(robot, (self.player.x, self.player.y))
            if len(self.ghosts) > 0:
                for ghost in self.ghosts:
                    self.window.blit(monster, (ghost.x, ghost.y))
            if len(self.bullets) > 0:
                for bullet in self.bullets:
                    self.window.blit(coin, (bullet.x, bullet.y))
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(0, 600, 800, 50))
        self.text1 = self.game_font.render(f"Points: {self.points}", True, (0, 0, 0))
        self.window.blit(self.text1, (650, 599))
        self.text2 = self.game_font.render(f"Ammo: {self.shots}", True, (0, 0, 0))
        self.window.blit(self.text2, (500, 600))
        self.text3 = self.game_font.render(f"Level: {self.difficulty}", True, (0, 0, 0))
        self.window.blit(self.text3, (650, 620))
        self.text4 = self.game_font.render(f"Arrow Keys = Move, Mouse = Shoot, N = New Game", True, (0, 0, 0))
        self.window.blit(self.text4, (25, 610))
        pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(500, 625, 135 - self.reloadtimer * 3, 20))
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction[0] = True
                if event.key == pygame.K_RIGHT:
                    self.direction[1] = True
                if event.key == pygame.K_UP:
                    self.direction[2] = True
                if event.key == pygame.K_DOWN:
                    self.direction[3] = True
                if event.key == pygame.K_n:
                    self.new_game()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.direction[0] = False
                if event.key == pygame.K_RIGHT:
                    self.direction[1] = False
                if event.key == pygame.K_UP:
                    self.direction[2] = False
                if event.key == pygame.K_DOWN:
                    self.direction[3] = False
            if event.type == pygame.MOUSEMOTION:
                self.mx = event.pos[0]
                self.my = event.pos[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.shoot()
            if event.type == pygame.QUIT:
                exit()

    def move(self):
        if self.direction[0]:
            self.player.x -= 4
        if self.direction[1]:
            self.player.x += 4
        if self.direction[2]:
            self.player.y -= 4
        if self.direction[3]:
            self.player.y += 4

    def spawn_ghost(self):
        self.spawntimer += 1
        if self.spawntimer >= 60 - self.difficulty * 2.5:
            self.ghosts.append(Ghost())
            self.spawntimer = 0

    def move_ghosts(self):
        for ghost in self.ghosts:
            if ghost.x > self.player.x:
                ghost.x -= 1 + self.difficulty * 0.2
            if ghost.x < self.player.x:
                ghost.x += 1 + self.difficulty * 0.2
            if ghost.y > self.player.y:
                ghost.y -= 1 + self.difficulty * 0.2
            if ghost.y < self.player.y:
                ghost.y += 1 + self.difficulty * 0.2

    def hitboxcheck(self):
        robobox = pygame.Rect(self.player.x, self.player.y, robot.get_width(), robot.get_height())
        for ghost in self.ghosts:
            ghostbox = pygame.Rect(ghost.x, ghost.y, monster.get_width(), monster.get_height())
            if robobox.colliderect(ghostbox):
                self.points -= 5
                self.ghosts.remove(ghost)
                continue
            for bullet in self.bullets:
                if ghostbox.colliderect(pygame.Rect(bullet.x, bullet.y, coin.get_width(), coin.get_height())):
                    self.points += 1
                    self.ghosts.remove(ghost)
                    self.bullets.remove(bullet)

    def shoot(self):
        if self.shots > 0:
            self.shots -= 1
            self.bullets.append(Bullet(self.player.x, self.player.y, self.mx, self.my))

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.x += 5 * bullet.vx
            bullet.y += 5 * bullet.vy
            if abs(bullet.x) > 800 or abs(bullet.y) > 600:
                self.bullets.remove(bullet)

    def reload(self):
        if self.shots < 5:
            self.reloadtimer += 1
            if self.reloadtimer >= 45:
                self.reloadtimer = 0
                self.shots += 1

    def level_up(self):
        if self.points // 10 > self.difficulty:
            self.difficulty += 1

    def game_over(self):
        if self.points >= 100 or self.points < 0:
            self.bullets = []
            self.ghosts = []
            self.pause = True

class Robot:
    def __init__(self):
        self.x = (800 - robot.get_width()) / 2
        self.y = (600 - robot.get_height()) / 2

    def contain(self):
        if self.x < 0:
            self.x = 0
        if self.x > 800 - robot.get_width():
            self.x = 800 - robot.get_width()
        if self.y < 0:
            self.y = 0
        if self.y > 600 - robot.get_height():
            self.y = 600 - robot.get_height()

class Ghost:
    def __init__(self):
        self.location = self.spawn()
        self.x = self.location[0]
        self.y = self.location[1]

    def spawn(self):
        side = randint(1, 3)
        if side == 1:
            return (-monster.get_width(), randint(0, 600 - monster.get_height()))
        if side == 2:
            return (randint(0, 800 - monster.get_width()), -monster.get_height())
        if side == 3:
            return (800, randint(0, 600 - monster.get_height()))

class Bullet:
    def __init__(self, x1, y1, x2, y2):
        self.x = x1
        self.y = y1
        self.vx = self.trajectory(x1, y1, x2, y2)[0]
        self.vy = self.trajectory(x1, y1, x2, y2)[1]

    def trajectory(self, x1, y1, x2, y2):
        hypo = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return ((x2 - x1) / hypo, (y2 - y1) / hypo)
    
RobotVsGhosts()