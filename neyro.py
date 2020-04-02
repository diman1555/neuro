from numpy import *
from math import sqrt

def sigmoid(x, deriv=False):
        if(deriv==True):
            return x * (1-x)
        return 1/(1+exp(-x))

class Neuro:
    def __init__(self, in_data, way):
        self.in_data = in_data
        self.last_in_data = array([[30,30,60,60]])
        self.way = way
        self.bestq=None

        self.syn1 = 2*random.random((6,16)) - 1
        self.syn2 = 2*random.random((16,16)) - 1
        #self.syn3 = 2*random.random((32,32)) - 1
        #self.syn4 = 2*random.random((32,32)) - 1
        self.syn5 = 2*random.random((16,4)) - 1
        self.syn6 = 2*random.random((4,4)) - 1

        self.l0 = in_data
        self.l1 = None
        self.l2 = None
        self.l3 = None
        self.l4 = None
        self.l5 = None
        self.l6 = None
        

    def train(self):
        """Тренировка нейросети"""            
        self.l1  =  sigmoid(dot(self.l0,self.syn1))
        self.l2  =  sigmoid(dot(self.l1,self.syn2))
        #self.l3  =  sigmoid(dot(self.l2,self.syn3))
        #self.l4  =  sigmoid(dot(self.l3,self.syn4))
        self.l5  =  sigmoid(dot(self.l2,self.syn5))
        self.l6  =  sigmoid(dot(self.l5,self.syn6))

    def errors(self):
        """Вычисление ошибок"""
        l6_error=None
        last_s = sqrt((self.last_in_data[0][0]-self.last_in_data[0][2])**2 + (self.last_in_data[0][1]-self.last_in_data[0][3])**2)
        now_s = sqrt((self.in_data[0][0]-self.in_data[0][2])**2 + (self.in_data[0][1]-self.in_data[0][3])**2)

        L=sqrt((self.last_in_data[0][0]-10-self.last_in_data[0][2])**2 + (self.last_in_data[0][1]-self.last_in_data[0][3])**2)
        U=sqrt((self.last_in_data[0][0]-self.last_in_data[0][2])**2 + (self.last_in_data[0][1]-10-self.last_in_data[0][3])**2)
        R=sqrt((self.last_in_data[0][0]+10-self.last_in_data[0][2])**2 + (self.last_in_data[0][1]-self.last_in_data[0][3])**2)
        D=sqrt((self.last_in_data[0][0]-self.last_in_data[0][2])**2 + (self.last_in_data[0][1]+10-self.last_in_data[0][3])**2)



        if self.way == "L":
            L+=10000
        elif self.way == "U":
            U+=10000
        elif self.way == "R":
            R+=10000
        elif self.way == "D":
            D+=10000

        a=[L,U,R,D]
        best=a.index(min(a))

        self.bestq=None


        if best==0:
            self.best
            q=array([[1,0,0,0]])
        elif best==1:
            self.bestq=array([[0,1,0,0]])
        elif best==2:
            self.bestq=array([[0,0,1,0]])
        elif best==3:
            self.bestq=array([[0,0,0,1]])

        if now_s < last_s:
            if self.l6[0][0] > self.l6[0][1] and self.l6[0][0] > self.l6[0][2] and self.l6[0][0] > self.l6[0][3]:
                l6_error = array([[ 0, self.l6[0][1], self.l6[0][2], self.l6[0][3] ]])
            elif self.l6[0][1] > self.l6[0][0] and self.l6[0][1] > self.l6[0][2] and self.l6[0][1] > self.l6[0][3]:
                l6_error = array([[ self.l6[0][0] , 0 , self.l6[0][2], self.l6[0][3] ]])
            elif self.l6[0][2] > self.l6[0][0] and self.l6[0][2] > self.l6[0][1] and self.l6[0][2] > self.l6[0][3]:
                l6_error = array([[ self.l6[0][0], self.l6[0][1], 0 , self.l6[0][3] ]])
            elif self.l6[0][3] > self.l6[0][0] and self.l6[0][3] > self.l6[0][2] and self.l6[0][3] > self.l6[0][1]:
                l6_error = array([[ self.l6[0][0] , self.l6[0][1], self.l6[0][2], 0 ]])
        else:
            if self.l6[0][0] > self.l6[0][1] and self.l6[0][0] > self.l6[0][2] and self.l6[0][0] > self.l6[0][3]:
                l6_error = array([[ self.l6[0][0], 0, 0, 0 ]])
            elif self.l6[0][1] > self.l6[0][0] and self.l6[0][1] > self.l6[0][2] and self.l6[0][1] > self.l6[0][3]:
                l6_error = array([[ 0, self.l6[0][1] , 0, 0 ]])
            elif self.l6[0][2] > self.l6[0][0] and self.l6[0][2] > self.l6[0][1] and self.l6[0][2] > self.l6[0][3]:
                l6_error = array([[ 0, 0, self.l6[0][2] , 0 ]])
            elif self.l6[0][3] > self.l6[0][0] and self.l6[0][3] > self.l6[0][2] and self.l6[0][3] > self.l6[0][1]:
                l6_error = array([[ 0 , 0, 0, self.l6[0][3] ]])

            if best==0:
                l6_error[0][0]=1-l6_error[0][0]+0.02
            if best==1:
                l6_error[0][1]=1-l6_error[0][1]+0.02
            if best==2:
                l6_error[0][2]=1-l6_error[0][2]+0.02
            if best==3:
                l6_error[0][3]=1-l6_error[0][3]+0.02

        #l6_error=self.bestq - 2*self.l6
        l6_weighted= l6_error * sigmoid(self.l6, deriv = True)


        l5_error= dot(l6_weighted, self.syn6.T)
        l5_weighted= l5_error * sigmoid(self.l5, deriv = True)

        #l4_error= dot(l5_weighted, self.syn5.T)
        #l4_weighted= l4_error * sigmoid(self.l4, deriv = True)

        #l3_error= dot(l4_weighted, self.syn4.T)
        #l3_weighted= l3_error * sigmoid(self.l3, deriv = True)

        l2_error= dot(l5_weighted, self.syn5.T)
        l2_weighted= l2_error * sigmoid(self.l2, deriv = True)

        l1_error= dot(l2_weighted, self.syn2.T)
        l1_weighted= l1_error * sigmoid(self.l1, deriv = True)


        self.syn6 -= dot(self.l5.T, l6_weighted)
        self.syn5 -= self.l2.T.dot(l5_weighted)
        #self.syn4 -= self.l3.T.dot(l4_weighted)
        #self.syn3 -= self.l2.T.dot(l3_weighted)
        self.syn2 -= self.l1.T.dot(l2_weighted)
        self.syn1 -= self.l0.T.dot(l1_weighted)
        
    def lol(self):
        #print(self.l6)
        print(self.syn6)

        
        if self.l6[0][0] > self.l6[0][1] and self.l6[0][0] > self.l6[0][2] and self.l6[0][0] > self.l6[0][3]:
            return "L"
        elif self.l6[0][1] > self.l6[0][0] and self.l6[0][1] > self.l6[0][2] and self.l6[0][1] > self.l6[0][3]:
            return "UP"
        elif self.l6[0][2] > self.l6[0][0] and self.l6[0][2] > self.l6[0][1] and self.l6[0][2] > self.l6[0][3]:
            return "R"
        elif self.l6[0][3] > self.l6[0][0] and self.l6[0][3] > self.l6[0][2] and self.l6[0][3] > self.l6[0][1]:
            return "DOWN"