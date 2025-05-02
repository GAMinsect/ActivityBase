import pygame
import gi
import random
gi.require_version("Gtk","3.0")
from gi.repository import Gtk



class BaseGame3:
    def __init__(self):
        self.clock=pygame.time.Clock()
    def initialize(self):
        pygame.init()
        self.running=True
        self.screen=pygame.display.get_surface()
        self.width=self.screen.get_width()
        self.height=self.screen.get_height()
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.gray=(180,180,180)
        self.blue=(0,100,255)
        self.font_size=100
        self.font = pygame.font.SysFont(None,self.font_size)
        self.tile_size=75
        self.grid_size=4
        self.run()
    
    def run(self):
        pygame.display.set_caption("Fifteen Puzzle")
        
        
        board = self.create_solvable_board()
        while self.running():
            self.clock.tick(30)

            #Process Gtk messages
            while Gtk.events_pending():
                Gtk.main_iteration()
            if not self.running:
                break

    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running=False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my = pygame.mouse.get_pos()
                    x,y = mx // self.tile_size, my // self.tile_size
                    self.click_tile(board, x, y)

            self.draw_board(board)
            if self.is_solved(board):
                win_text = self.font.render("Solved!", True, (0, 150, 0))
                self.screen.blit(win_text, win_text.get_rect(center=(self.width//2, self.height//2)))
            
            pygame.display.flip()


    def create_solvable_board(self):
        nums = list(range(1, 16)) + [0]
        while True:
            random.shuffle(nums)
            if self.is_solvable(nums):
                return [nums[i:i+4] for i in range(0, 16, 4)]

    def is_solvable(self,board_flat):
        inv_count = 0
        for i in range(len(board_flat)):
            for j in range(i + 1, len(board_flat)):
                if board_flat[i] and board_flat[j] and board_flat[i] > board_flat[j]:
                    inv_count += 1
        blank_row = 4 - (board_flat.index(0) // 4)
        return (inv_count + blank_row) % 2 == 0

    def draw_board(self,board):
        self.screen.fill(self.white)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                num = board[i][j]
                rect = pygame.Rect(j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(self.screen, self.gray if num else self.white, rect)
                pygame.draw.rect(self.screen, self.black, rect, 2)
                if num:
                    text = self.font.render(str(num), True, self.blue)
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)

    def find_blank(self,board):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if board[i][j] == 0:
                    return i, j

    def click_tile(self,board, x, y):
        bi, bj = self.find_blank(board)
        if (abs(bi - y) == 1 and bj == x) or (abs(bj - x) == 1 and bi == y):
            board[bi][bj], board[y][x] = board[y][x], board[bi][bj]

    def is_solved(self,board):
        flat = sum(board, [])
        return flat == list(range(1, 16)) + [0]




