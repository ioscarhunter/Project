class Pizza:
   
    empCount = 0

    def __init__(self, name):
      self.name = name
      self.size = 0
      self.side = 0 
      self.topping = 0
      self.extra = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      self.amount = 0
      self.name = name
      self.address = " "
      self.number = " "
      self.exchange = 0
      

   
    def getSize(self):
        size = eval(input("Which size do you want? [s,m,l]: "))
        if(size == 's'):
            self.size = 0
        elif(size == 'm'):
             self.size = 1
        else:
            self.size = 2


    def getSide(self):
         side = eval(input("Which side do you want? [0:thin, 1:thick, 2:cheese, 3:sausage]: "))
         self.side = side


    def getTopping(self):
        settopping = ["Hava:1","Seafood:2","Chicken:3","TomYum:4","cheese:5","Mushroom&Ham:6","Veget:7","Freestyle:8"]
        print("Enter num of order you want: ")
        topping = ["Ham","Hotdog","Ground beef","Ground chicken","Ground pork","Bacon","Peperoni","Italian cheese","Blue cheese","Feta cheese","Seafood","Tuna",
                      "Tomato","Onion","Corn","Spinach","Olive","Pineapple","Champignons","Pesto","Egg"]
        settopping = ["Hava:1","Seafood:2","Chicken:3","TomYum:4","cheese:5","Mushroom&Ham:6","Veget:7","Freestyle:8"]
      
        for x in range(8):
           print(settopping[x]+" ")
        print("Enter num of order you want: ")
        q = int(input("Choose?: "))
        if(q == 8):
            print("Enter 0 or 1 for No|Yes")
            for x in range(21):
                a = int(input(topping[x]+"?: "))
                if(a == 1):
                    self.extra[x] = 1
                else:
                    self.extra[x] = 0
        else:
           self.topping = q      


    def getAmount(self):
        x = int(input("How many?: "))
        self.amount = x
        y = str(input("your Name &  your Surname: "))
        self.name = y
        z = str(input("Your phone number: "))
        self.number = z
        o = str(input("Where u want us to delivery: "))
        self.address = o
        x = int(input("No exchange(0) or Exchange(1): "))
        self.exchange = x
        
    def getanswer(self):
        print(self.size)
        print(self.side)
        print(self.topping)
        print(self.name)
        print(self.oderno)
        print(self.extra) 
        print(self.amount)
        print(self.name)
        print(self.address)
        print(self.number)
        print(self.exchange)

    def getstringtext(self):
        
        x = ""
        x+=(str(self.size)+"<>")
        x+=(str(self.side)+"<>")
        x+=(str(self.topping)+"<>")
        x+=(str(self.amount)+"<>")
        x+=(self.name+"<>")
        x+=(self.address+"<>")
        x+=(str(self.number)+"<>")
        x+=(str(self.exchange)+"<>")
        x+=(str(self.side)+"<>")
        #9


        for i in self.extra:
            x+= str(i)+"<>"
        return x

        #21

s = Pizza("Kris")
s.getSize()
s.getSide()
s.getTopping()
print(s.getstringtext())