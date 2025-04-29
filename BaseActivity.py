import sys
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import pygame

from sugar3.activity.activity import Activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import StopButton

import sugargame.canvas
import BaseGame

class Base(Activity):
    def __init__(self,handle):
        Activity.__init__(self,handle)

        self.paused=False

        #Create the game instance
        self.game=BaseGame.BaseGame()

        #Build the activity toolbar
        self.build_toolbar()

        self._pygamecanvas=sugargame.canvas.PygameCanvas(self,main=self.game.initialize,modules=[pygame.display])

        self.set_canvas(self._pygamecanvas)
        self._pygamecanvas.grab_focus()

    def build_toolbar(self):
        #It just has the closing button
        toolbar_box=ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        #Make the stop button
        stop_button=StopButton(self)
        toolbar_box.toolbar.insert(stop_button,-1)
        stop_button.show()
        stop_button.connect("clicked",self.stop)
    
    def stop(self):
        self.game.running=False

