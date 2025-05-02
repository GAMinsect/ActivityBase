import pygame
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from Button import *

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
        self.check=Button((188, 223, 145),self.screen,self.width//2-100,self.height//7,200,100,None,pygame.font.SysFont(None,30))
        self.run()

        
    def run(self):
        def change_color(color,shape):
            shape.color=color
    
        
        value=0
        cache_color=self.sq.color

        while self.running:
            

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
            self.screen.fill((180,180,150))
            self.list.draw()
            self.check.draw()
            self.sq.draw()
            
            pygame.display.update()

