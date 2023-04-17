import pygame 
import time
import random
pygame.init()

display_width = 800
display_height = 600


class Cookie():
    def __init__(self, x = 0, y = 0, speedX = 1, speedY = 1,  image_path= 'cookie.png'):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY

  
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(cookie_image, (50, 50))

        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(),self.image.get_height())

    def update_cookie(self):
            self.rect = pygame.Rect(self.x, self.y, self.image.get_width(),self.image.get_height())



def cookie_move(cookies, bouncing = False):
    for cookie in cookies:
        if bouncing:    
            if cookie.x < 0:
                cookie.speedX = abs(cookie.speedX)
                cookie.update_cookie()
                screen.blit(bouncing_cookie_image, (cookie.x, cookie.y))
                
            elif cookie.x + 20 > display_width:
                cookie.speedX = -abs(cookie.speedX)
                cookie.update_cookie()
                screen.blit(bouncing_cookie_image, (cookie.x, cookie.y))
                

            if cookie.y < 0:
                cookie.speedY = abs(cookie.speedY)
                cookie.update_cookie()
                screen.blit(bouncing_cookie_image, (cookie.x, cookie.y))
                
            elif cookie.y + 20 > display_height:
                cookie.speedY = -abs(cookie.speedY)
                cookie.update_cookie()
                screen.blit(bouncing_cookie_image, (cookie.x, cookie.y))
            cookie.x += fps * cookie.speedX
            cookie.y += fps * cookie.speedY
            cookie.update_cookie()
            screen.blit(bouncing_cookie_image, (cookie.x, cookie.y))
            continue
                
        else:
            if cookie.x < 0 or cookie.x > display_width:
                #print(len(cookies))
                cookies.remove(cookie)

                print("cookie off screen")
                #print(len(cookies))
                continue
            if cookie.y < 0 or cookie.y > display_height:
                #print(len(cookies))
                cookies.remove(cookie)
                print("cookie off screen")
                #print(len(cookies))
                continue
        cookie.x += fps * cookie.speedX
        cookie.y += fps * cookie.speedY
        cookie.update_cookie()
        screen.blit(cookie_image, (cookie.x, cookie.y))
        #pygame.draw.rect(screen,(255,0,0), cookie.rect, 2)
    return cookies








def spawn_cookie(cookie_img, bouncing = False):
    odd = random.choice(['top', 'bottom'])
    if odd == 'top':
        cookie_x = random.randint(0, display_width - cookie_img.get_width())
        cookie_y = random.randint(0, 1) * display_height
    

    else:
        cookie_x = random.randint(0, 1) * display_width
        
        cookie_y = random.randint(0, display_height - cookie_img.get_width())

    speedY = random.randint(-5, 5)
    speedX = random.randint(-5, 5)
    cookie = Cookie(cookie_x, cookie_y, speedX, speedY)

    if bouncing:
        cookie = Cookie(cookie_x, cookie_y, speedX, speedY, image_path="feelsbadman.jpg")

    return cookie


screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Cookie Clicker")

cookie_image = pygame.image.load("cookie.png")
cookie_image = pygame.transform.scale(cookie_image, (50, 50))

bouncing_cookie_image = pygame.image.load("feelsbadman.jpg")
bouncing_cookie_image = pygame.transform.scale(bouncing_cookie_image, (50, 50))

cookies = []
cookie = Cookie()
cookies.append(cookie)
screen.blit(cookie_image, (cookie.x, cookie.y))

bouncing_cookies = []
bouncing_cookie = Cookie(image_path="feelsbadman.jpg")
bouncing_cookies.append(bouncing_cookie)
screen.blit(bouncing_cookie_image, (bouncing_cookie.x, bouncing_cookie.y))
pygame.display.update()

fps = 0.10

clock = pygame.time.Clock()
# Limit the game to 60 frames per second
clock.tick(60)

font = pygame.font.Font(None, 36)
text_surface = font.render(f"Points: {0}", True, (55, 55, 55))
# Main game loop
game_exit = False
points = 0
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            for cookie in cookies:
                if cookie.rect.collidepoint(mouse_pos):
                    cookies.remove(cookie)
                    print("cookie {} removed".format(cookie))
                    points += 1
                    text_surface = font.render(f"Points: {points}", True, (55, 55, 55))
                    
                    

    # Move and draw the cookies on the game display
    screen.fill((255, 255, 255))

    cookie_move(cookies)
    cookie_move(bouncing_cookies, bouncing=True)
    #pygame.display.update()
    screen.blit(text_surface, (10, 10))
    # Spawn new cookies every 2 seconds
    if pygame.time.get_ticks() % 2000 < 60:
        cookies.append(spawn_cookie(cookie_image))

    if pygame.time.get_ticks() % 5000 < 60:
        bouncing_cookies.append(spawn_cookie(bouncing_cookie_image, bouncing=True))
    

        
    # Create a text surface with the current points counter
    
    #text_surface = font.render(f"Points: {points}", True, (55, 55, 55))
    
    # Draw the text surface onto the screen
    #screen.blit(text_surface, (10, 10))
    
    pygame.display.update()

    # Limit the game to 60 frames per second
    #print(points)
    clock.tick(60)
        # while True:
#     screen.fill((0, 0, 0))
#     cookie_move(cookies)
#     if pygame.time.get_ticks() % 2000 < 60:
#         cookies.append(spawn_cookie(cookie_image))

#     clock.tick(60)








#     pygame.display.update()



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




