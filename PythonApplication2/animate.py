import sys 
from PySide.QtCore import *
from PySide.QtGui import * 
class MoviePlayer(QWidget): 
    def __init__(self, parent=None): 
        QWidget.__init__(self, parent) 
        # setGeometry(x_pos, y_pos, width, height)
       
        # set up the movie screen on a label
        self.movie_screen = QLabel()
        # expand and center the label 
        #self.movie_screen.setSizePolicy(QSizePolicy.Expanding, 
            #QSizePolicy.Expanding)        
    
        # positin the widgets
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(QMargins(0,0,0,0))
        main_layout.addWidget(self.movie_screen)
        self.setLayout(main_layout)
        self.setContentsMargins(0,0,0,0)
        self.movie_screen.setMargin(0)
        
                
        # use an animated gif file you have in the working folder
        # or give the full file path
        ag_file = "res/ani/travel.gif"
        self.movie = QMovie(ag_file, QByteArray(), self) 
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setScaledSize(QSize(391,250))
        self.movie.setSpeed(150) 
        self.movie_screen.setMovie(self.movie) 
        # optionally display first frame
        self.movie.start()

