#Implementation of the Button
import pygame

class Button:
    def __init__(self,color,screen,x=100,y=100,width=192,height=180,text=None,font=None):
        self.color=color
        self.screen=screen
        self.button=pygame.Rect(x,y,width,height)
        self.text=text
        self.font=font
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    
    def draw_text(self):
        img=self.font.render(self.text,True,(0,0,0))
        self.screen.blit(img,img.get_rect(center=(self.x+self.width//2,self.y+self.height//2)))

    def draw(self):
        pygame.draw.rect(self.screen,self.color,self.button)
        if self.text: #Also draw the text
            self.draw_text()
    
    

    def is_pressed(self): 
        mouse_pos=pygame.mouse.get_pos()
        mouse_pressed=pygame.mouse.get_pressed()[0]

        if self.button.collidepoint(mouse_pos) and mouse_pressed:
            return True
        return False

    


class ColorSelection:
    def __init__(self,number,colors,screen,x,y,width,height):
        #Create all the buttons
        self.list_button=[ Button(colors[i],screen,x,y+(i)*height,width,height) for i in range(number) ] #Create the list of buttons
        self.screen=screen
        self.colors=colors
        self.number=number
    
    def draw(self): #Draw each button 
        for i in range(self.number):
            pygame.draw.rect(self.screen,self.colors[i],self.list_button[i].button)
    
    def is_pressed(self): #Call for each button the is_pressed method
        for i in range(self.number):
            if self.list_button[i].is_pressed():
                return self.list_button[i].color



