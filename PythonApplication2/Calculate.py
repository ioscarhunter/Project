

import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class My_calcu():
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.result = 0
        self.price_size = 0
        self.price_side = 0
        self.price_topping =0

        

    def step_1(self):
        if(self.value1[2] == 7):
            if(self.value1[0]== 0):
                self.price_size = 149

            elif(self.value1[0] == 1):
                self.price_size = 249

            else:
                self.price_size = 349
        
        else:
            if(self.value1[0]== 0):
                self.price_size = 199

            elif(self.value1[0] == 1):
                self.price_size = 299

            else:
                self.price_size = 399
        
    def step_2(self):
        if(self.value1[1] == 0):
            self.price_side = 0

        else:
            self.price_side = 50

    def step_3(self):
        if(self.value1[2] != 7):
            self.price_topping = 0

        elif(self.value1[2] == 7):
            for i in range(0,19):
                if(self.value2[i] == 1):
                    self.price_topping += 20



    def step_4(self):
        self.result = self.price_side + self.price_size + self.price_topping

    def step_5(self):
        self.result = self.result*self.value1[3]
        print(self.result)


n = [0,1,2,1]
extra = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
k = My_calcu(n,extra)

