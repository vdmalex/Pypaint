import pygame
import random
import sys

colors = [
(255,0,0),
(0,255,0),
(0,0,255)]
color=colors[0]
colorsLen = len(colors)



def randomRec():
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    width = random.randint(0, 50)
    height = random.randint(0, 100)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return pygame.Rect(x, y, width, height)
    #pygame.draw.rect(surface, (r, g, b), rr)

def handle_keys(r):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:       
                return pygame.Rect.move(r,0,-1)
            elif event.key == pygame.K_DOWN:
                return pygame.Rect.move(r,0,1)
            elif event.key == pygame.K_LEFT:
                return pygame.Rect.move(r,-1,0)
            elif event.key == pygame.K_RIGHT:
                return pygame.Rect.move(r,1,0)
        else:
            return r
    return r
# todo fading rectange multithreading


     
def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)

def generateRectanges():
    width = 5
    list=[]
    for i in range(95+1):
        height=random.randint(50,400)
        r=pygame.Rect((i*width),0,width,random.randint(50,400))
       
        list.append(r)
        

    return list

def drawRectanges(list,surface,screen):
    color = (255,0,0)
    for i in range(95+1):
        r=list[i]
        pygame.draw.rect(surface,color,r)
        #screen.blit(surface, (0, 0))
    



def pypaint_init(surface):
    pygame.init()
    red_select = pygame.Rect(0,0,20,20)
    green_select = pygame.Rect(20,0,20,20)
    blue_select = pygame.Rect(40,0,20,20)
    black_select = pygame.Rect(0,20,20,20)
    white_select = pygame.Rect(20,20,20,20)
    yellow_select = pygame.Rect(40,20,20,20)
    rainbow_left= pygame.Rect(60,20,10,20)
    rainbow_right= pygame.Rect(70,20,10,20)
   

    drawGrid(surface)
    pygame.draw.rect(surface, options_color, pygame.Rect(0,0,screen_width,40))
    pygame.draw.rect(surface, color_red,red_select)
    pygame.draw.rect(surface, color_green,green_select)
    pygame.draw.rect(surface, color_blue,blue_select)
    pygame.draw.rect(surface, color_black,black_select)
    pygame.draw.rect(surface, color_white,white_select)
    pygame.draw.rect(surface, color_yellow,yellow_select)
    gradientRect(surface, color_blue, color_green, rainbow_left ) 
    gradientRect(surface, color_yellow, color_red, rainbow_right )
    font = pygame.font.SysFont('timesnewroman',20)
    reset_text = font.render("reset",0,(0,0,0)) 
    save_text = font.render("save",0,(0,0,0)) 
    surface.blit(reset_text,(430,0))
    surface.blit(save_text,(430,20))
    pygame.draw.rect(surface,color_black,brushsize_1)
    pygame.draw.rect(surface,color_black,brushsize_2)
    pygame.draw.rect(surface,color_black,brushsize_3)
    pygame.draw.rect(surface,color_black,brushsize_4)
    pygame.draw.rect(surface,color_black,brushsize_5)


   


def brush_rainbow(color):
    r=color[0]
    g=color[1]
    b=color[2]
    if ((r==255) & (g < 255) & (b==0)):
        g+=1
    elif((r>0) & (g == 255) & (b==0)):
        r-=1
    elif((r==0) & (g == 255) & (b<255)):
        b+=1
    elif((r==0) & (g > 0) & (b==255)):
        g-=1
    elif((r<255) & (g == 0) & (b==255)):
        r+=1
    elif((r==255) & (g == 0) & (b>0)):
        b-=1
    
    result = (r,g,b)
    return result

def gradientRect( window, left_colour, right_colour, target_rect ): #Kingsley from stackoverflow
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )

    
screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize
pygame.display.set_caption('PyPaint')


options_color=(84,194,205)
color_blue=(0,0,255)
color_green=(0,255,0)
color_red=(255,0,0)
color_white=(255,255,255)
color_black=(0,0,0)
color_yellow=(255,255,0)
rainbow_select = pygame.Rect(60,20,20,20)
brushsize_1 = pygame.Rect(120,5,1,30)
brushsize_2 = pygame.Rect(130,5,2,30)
brushsize_3 = pygame.Rect(140,5,3,30)
brushsize_4 = pygame.Rect(150,5,4,30)
brushsize_5 = pygame.Rect(160,5,5,30)


def main():
    #initialization
    

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    pypaint_init(surface)
    brush_size=3

    rainbow_mode=False
    color=(0,0,0)
    color_rainbow=(255,0,0)
    r=255
    g=0
    b=0
    #rectangles= generateRectanges()
    #drawRectanges(rectangles,surface,screen)
    while(True): #main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(10000)
        test=pygame.mouse.get_pressed()
        coord=pygame.mouse.get_pos()
        #print(coord)

        if test[0]:       
            if coord[1]<20:
                
                if coord[0]<20:
                    color=color_red
                    rainbow_mode=False
                elif coord[0]<40:
                    color=color_green
                    rainbow_mode=False
                elif coord[0]<60:
                    color=color_blue
                    rainbow_mode=False
                elif coord[0]<115:
                    pass
                elif coord[0]<130:
                    brush_size=1
                elif coord[0]<140:
                    brush_size=2                
                elif coord[0]<150:
                    brush_size=3                
                elif coord[0]<160:
                    brush_size=4      
                elif coord[0]<170:
                    brush_size=5  
                elif coord[0]<screen_width and coord[0] > 435:
                    pypaint_init(surface)
            elif coord[1]<40:
                if coord[0]<20:
                    color=color_black
                    rainbow_mode=False
                elif coord[0]<40:
                    color=color_white
                    rainbow_mode=False
                elif coord[0]<60:
                    color=color_yellow
                    rainbow_mode=False
                elif coord[0]<80:
                    rainbow_mode=True
                elif coord[0]<115:
                    pass
                elif coord[0]<130:
                    brush_size=1
                elif coord[0]<140:
                    brush_size=2                
                elif coord[0]<150:
                    brush_size=3                
                elif coord[0]<160:
                    brush_size=4      
                elif coord[0]<170:
                    brush_size=5  


                elif coord[0] < screen_width and coord[0] > 433:
                    pygame.image.save(screen,"screenshot.jpg")
                    print("saved!")
            else: 
                if rainbow_mode:
                    color_rainbow = brush_rainbow(color_rainbow)
                    pygame.draw.circle(surface,color_rainbow,coord,brush_size)          
                else:
                    pygame.draw.circle(surface,(color),coord,brush_size)
        
                 

         
            
     
        #rr=pygame.Rect(430, 460, 50, 50)
        #pygame.draw.rect(surface, (255, 0, 0), rr)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        #pygame.display.flip()
        


main()
