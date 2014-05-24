class account:
    def __init__(self,user):
        self.username = user
        self.info = ['','','']
    def export(self):
        tmp =""
        for i in self.info :
            tmp+=i
            tmp+="<>"
        tmp+=self.username
        return tmp