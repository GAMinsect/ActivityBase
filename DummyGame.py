'''import pygame
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class DummyGame:
    def __init__(self):
        self.clock=pygame.time.Clock()

    def run(self):
        self.running=True
        screen=pygame.display.get_surface()
        width=screen.get_width()
        height=screen.get_height()
        value=0
        player=pygame.Rect(100,100,100,100)

        while self.running:
            screen.fill((94,252,237))

            #Process Gtk messages
            while Gtk.events_pending():
                Gtk.main_iteration()
            if not self.running:
                break
                
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    return
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    mouse_pressed=pygame.mouse.get_pressed()[0]
                    if player.collidepoint(mouse_pos) and mouse_pressed:
                        value+=1
            
            pygame.draw.rect(screen,(value,0,0),player)
            pygame.display.update()
'''
