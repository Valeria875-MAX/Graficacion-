class Algoritmos:
    def __init__(self,x,y,x2,y2):

        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.varx = []
        self.vary = []

    def dda(self):
        self.varx = []
        self.vary = []
        x = self.x
        y = self.y
        x2 = self.x2
        y2 = self.y2
        dx = abs(x2-x)
        dy = abs(y2-y)
        steps = dy
        if dx>dy:
            steps = dx
        incremento_x = dx/steps
        incremento_y = dy/steps

        punto1= x
        punto2= y
        self.varx=[punto1]
        self.vary=[punto2]

        for i in range(steps):
           punto1 += incremento_x
           punto2 += incremento_y

        n = round(punto1)
        n2 = round(punto2)

        self.varx.append(n)
        self.vary.append(n2)

    def brezenham(self):
        x = self.x
        y = self.y
        x2 = self.x2
        y2 = self.y2
        dx=x2-x
        dy=y2-y
        p=2*dy - dx
        self.varx=[]
        self.vary=[]

        while x <= x2:
            self.varx.append(x)
            self.vary.append(y)
            x+=1
            if p<0:
                p=p+2*dy
            else:
                p=p+ (2 *dy)- (2* dx)
                y+=1