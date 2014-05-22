import Pizza

class My_calcu():
    def __init__(self, pizza):
        self.value1 = pizza.order
        self.value2 = pizza.extra
        self.result = 0
        self.price_size = 0
        self.price_side = 0
        self.price_topping =0
        self.step_1()
        self.step_2()
        self.step_3()
        self.step_4()
        

    def step_1(self):
        #size
        if(self.value1[2] == 8):
            if(self.value1[0]== 1):
                self.price_size = 149

            elif(self.value1[0] == 2):
                self.price_size = 249

            else:
                self.price_size = 349
        
        else:
            if(self.value1[0]== 1):
                self.price_size = 199

            elif(self.value1[0] == 2):
                self.price_size = 299

            else:
                self.price_size = 399
        
    def step_2(self):
        #side
        if(self.value1[1] == 1):
            self.price_side = 0

        else:
            self.price_side = 50

    def step_3(self):
        #topping
        if(self.value1[2] != 8):
            self.price_topping = 0

        elif(self.value1[2] == 8):
            for i in range(0,12):
                if(self.value2[i] == 1):
                    self.price_topping += 20



    def step_4(self):
        #allprice
        self.result = self.price_side + self.price_size + self.price_topping

  
        
    def getPrize(self):
        return self.result


