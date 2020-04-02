from numpy import *

random.seed(1)

def sigmoid(x,deriv=False):
    if(deriv==True):
        return x * (1-x)
    return 1/(1+exp(-x))

def init_weights(in_,out_):
    return 2*random.random((in_,out_)) - 1
    
X = array(   [[0,0,0,0,0,1],
             [0,0,0,0,1,0],
             [1,0,1,0,0,0],
             [1,1,1,0,0,0],
             [0,1,0,1,0,1],
             [1,0,1,0,1,0],
             [1,0,0,0,0,0],
             [0,1,0,1,0,0],
             [0,0,0,1,1,0],

             [0,1,1,0,0,1],
             [1,1,0,0,1,0],
             [1,1,1,1,1,1],
             [1,1,1,0,0,0],
             [0,1,0,1,0,1],
             [1,0,1,0,1,0],
             [1,1,0,0,0,0],
             [0,1,0,1,0,0],
             [0,0,1,1,1,0],
             [0,0,0,0,0,0],
             [1,0,0,1,1,0]])
                
y = array(  [[0],
			[1],
			[1],
			[0],
            [0],
            [1],
            [1],
            [0],
            [0],
            
            [0],
			[0],
			[0],
			[0],
            [0],
            [1],
            [0],
            [0],
            [0],
            [0],
            [0]])

syn1 = init_weights(6,24)
syn2 = init_weights(24,48)
syn3 = init_weights(48,96)
syn4 = init_weights(96,192)
syn5 = init_weights(192,96)
syn6 = init_weights(96,48)
syn7 = init_weights(48,24)
syn8 = init_weights(24,12)
syn9 = init_weights(12,6)
syn10= init_weights(6,1)

for _ in range(60000):

    layers= dict(
        l0  =  X,                
        l1  =  sigmoid(dot(l0,syn1)),
        l2  =  sigmoid(dot(l1,syn2)),
        l3  =  sigmoid(dot(l2,syn3)),
        l4  =  sigmoid(dot(l3,syn4)),
        l5  =  sigmoid(dot(l4,syn5)),
        l6  =  sigmoid(dot(l5,syn6)),
        l7  =  sigmoid(dot(l6,syn7)),
        l8  =  sigmoid(dot(l7,syn8)),
        l9  =  sigmoid(dot(l8,syn9)),
        l10 =  sigmoid(dot(l9,syn10))
    )


    l10_error = y - layers[10]
    l10_weighted_errors = l10_error*sigmoid(layers[10],deriv=True)
    
    if (_% 10000) == 0:
        print ("Error:" + str(mean(abs(l10_error))))
        

    l9_error = dot(l10_weighted_errors, syn10.T)
    l9_weighted_errors = l9_error * sigmoid(layers[9],deriv=True)

    l8_error = l9_weighted_errors.dot(syn9.T)
    l8_weighted_errors = l8_error * sigmoid(layers[8],deriv=True)

    l7_error = l8_weighted_errors.dot(syn8.T)
    l7_weighted_errors = l7_error * sigmoid(layers[7],deriv=True)

    l6_error = l7_weighted_errors.dot(syn7.T)
    l6_weighted_errors = l6_error * sigmoid(layers[6],deriv=True)

    l5_error = l6_weighted_errors.dot(syn6.T)
    l5_weighted_errors = l5_error * sigmoid(layers[5],deriv=True)

    l4_error = l5_weighted_errors.dot(syn5.T)
    l4_weighted_errors = l4_error * sigmoid(laters[4],deriv=True)

    l3_error = l4_weighted_errors.dot(syn4.T)
    l3_weighted_errors = l3_error * sigmoid(layers[3],deriv=True)

    l2_error = l3_weighted_errors.dot(syn3.T)
    l2_weighted_errors = l2_error * sigmoid(layers[2], deriv=True) 

    l1_error = l2_weighted_errors.dot(syn2.T)
    l1_weighted_errors = l1_error * sigmoid(layers[1], deriv=True)
    
    syn10 += l9.T.dot(l10_weighted_errors)
    syn9 += l8.T.dot(l9_weighted_errors)
    syn8 += l7.T.dot(l8_weighted_errors)
    syn7 += l6.T.dot(l7_weighted_errors)
    syn6 += l5.T.dot(l6_weighted_errors)
    syn5 += l4.T.dot(l5_weighted_errors)
    syn4 += l3.T.dot(l4_weighted_errors)
    syn3 += l2.T.dot(l3_weighted_errors)
    syn2 += l1.T.dot(l2_weighted_errors)
    syn1 += l0.T.dot(l1_weighted_errors)

a=(sigmoid(dot(array([1,1,1,0,1,0]), syn1)))
b=sigmoid(dot(a, syn2))
c=sigmoid(dot(b,syn3))
d=sigmoid(dot(c,syn4))
e=sigmoid(dot(d,syn5))
f=sigmoid(dot(e,syn6))
g=sigmoid(dot(f,syn7))
h=sigmoid(dot(g,syn8))
i=sigmoid(dot(h,syn9))
j=sigmoid(dot(i,syn10))

print(j)