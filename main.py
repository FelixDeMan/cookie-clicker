import pygame 

pygame.init()



class Cookie():
    def __init__(self, x = 0, y = 0, speedX = 5, speedY = 5, image_path= 'cookie.png'):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.image = image_path

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cookie Clicker")

cookie_image = pygame.image.load("cookie.png")

cookie = Cookie()

screen.blit(cookie_image, (cookie.x, cookie.y))
pygame.display.update()

while True:
    cookie.x += cookie.speedX
    cookie.y += cookie.speedY
    pygame.display.update()





