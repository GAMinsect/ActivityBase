import pygame
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from Button import *
from Graph_Squares import *
import time

class BaseGame2:
    def __init__(self):
        self.clock=pygame.time.Clock()

    def initialize(self):
        pygame.init()
        self.running=True
        self.screen=pygame.display.get_surface()
        self.width=self.screen.get_width()
        self.height=self.screen.get_height()
        self.colors=[(100,100,100),(10,10,200),(200,10,0),(10,100,200)]
        self.list=ColorSelection(4,self.colors,self.screen,10,10,200,100)
        self.sq=Button((50,100,200),self.screen,10,420,100,100)
        self.font_size=100
        self.font=pygame.font.SysFont(None,self.font_size)
        self.check=Button((188, 223, 145),self.screen,self.width//2-100,self.height//7,200,100,"Check",self.font)

        

        #Add tiles
        self.t1=Square(self.screen,300,300,100,100)
        self.t2=Square(self.screen,400,300,100,100)

        self.Field=PlayField(self.screen)
        self.Field.add(self.t1,self.t2)

        #Run Game
        self.run()

        
        
    def run(self):
        def change_color(color,shape):
            shape.color=color
    
        
        value=0
       

        while self.running:
            cache_color=self.sq.color

            #Process Gtk messages
            while Gtk.events_pending():
                Gtk.main_iteration()
            if not self.running:
                break
                
            
            for event in pygame.event.get(): 
                if event.type==pygame.QUIT:
                    return
            res=self.list.is_pressed() #Were I store the value if any button is pressed
            if res!=None: change_color(res,self.sq)

            res=self.Field.is_pressed() #If any of the Field tile are pressed
            if res!=None: change_color(cache_color,res)

            if self.check.is_pressed():
                if self.Field.win(self.t1):
                    win_text = self.font.render("Solved!", True, (150, 100, 100))
                    self.screen.blit(win_text,win_text.get_rect(center=(self.width//2, self.height//2-20)))
                    pygame.display.update() 
                    time.sleep(3)
                    self.running=False
                else:
                    lose_text = self.font.render("ERROR!", True, (230, 20, 20))
                    self.screen.blit(lose_text,lose_text.get_rect(center=(self.width//2, self.height//2-20)))
                    pygame.display.update() 
                    time.sleep(1)
                    
                    
                
                
                
            
            self.screen.fill((180,180,150))
            self.list.draw()
            self.check.draw()
            self.sq.draw()
            self.Field.draw()
            
            pygame.display.update()

