#Implementation of the Colored_Square Class
#Which works like an undirect Graph
from collections import defaultdict,deque
import pygame

class PlayField: #Graph that holds the relations between each square
    def __init__(self,screen):
        self.Field=defaultdict(list)#Tag->[List of Adjacent Squares]
        self.list=set()
        self.screen=screen
    def add(self,node1,node2):
        self.Field[node1.tag].append(node2)
        self.Field[node2.tag].append(node1)
        
        
    def win(self,start): #BFS that checks if every Square has a different color from the others, and if they are all colored
        #I start with the square start
        q=deque( [(start.tag,start.color)] )
        seen=set()
        seen.add(start.tag)

        while q:
            tag,color=q.popleft()
            
            
            for ngb in self.Field[tag]:
                if ngb.tag in seen:
                    continue
                if color==ngb.color: #I have two adjacent cell with the same color
                    return False
                if ngb.color==(255,255,255) or color==(255,255,255): #The default color is white
                    return False
                
                q.append( (ngb.tag,ngb.color) )
                seen.add(ngb.tag)
            

        return True #We have a valid solution
    
    def draw(self): #I draw the playfield 
        for el in Square._list:
            pygame.draw.rect(self.screen,el.color,el.tile)
            pygame.draw.rect(self.screen,(0,0,0),el.tile,5)
            img=pygame.font.SysFont(None,30).render(el.text,True,(0,0,0))
            self.screen.blit(img,(el.x+20,el.y+20))
    
    def is_pressed(self): #Checks if any of the square are pressed
        for el in Square._list:
            if el.pressed():
                return el

class Square:
    _tag=1
    _list=[] #List of all the node
    def __init__(self,screen,x,y,width,height):
        self.tag=Square._tag
        Square._tag+=1

        self.color=(255,255,255)
        
        Square._list.append(self)#Add this istance to the list square
        self.screen=screen
        self.tile=pygame.Rect(x,y,width,height)
        self.text="."+str(self.tag)
        self.x=x
        self.y=y
    
    def pressed(self): #Method that cheks if the Square is pressed
        mouse_pos=pygame.mouse.get_pos()
        mouse_pressed=pygame.mouse.get_pressed()[0]

        if self.tile.collidepoint(mouse_pos) and mouse_pressed:
            return True
        return False
