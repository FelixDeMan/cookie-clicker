import pygame 

pygame.init()



class Cookie():
    def __init__(self, x = 0, y = 0, speedX = 1, speedY = 1,  image_path= 'cookie.png'):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.image = image_path
   

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cookie Clicker")

cookie_image = pygame.image.load("cookie.png")
cookie_image = pygame.transform.scale(cookie_image, (50, 50))

cookie = Cookie()

screen.blit(cookie_image, (cookie.x, cookie.y))
pygame.display.update()

fps = 0.10

while True:
    cookie.x += fps * cookie.speedX
    cookie.y += fps * cookie.speedY
    #screen.blit(cookie_image, (cookie.x, cookie.y))
    pygame.display.update()



points = 0  # initialize points counter to zero

while True:  # game loop
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if cookie_rect.collidepoint(mouse_pos):
                points += 1  # increment points counter when cookie is clicked
    
    # Draw code here...

    # Create a text surface with the current points counter
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Points: {points}", True, (255, 255, 255))
    
    # Draw the text surface onto the screen
    screen.blit(text_surface, (10, 10))
    
    pygame.display.update()




