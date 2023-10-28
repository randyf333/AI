# import sys; args = sys.argv[1:]
# file = open(args[0],'r')
file = open('weights.txt','r')
args = ['weights.txt','T3','5','2','3','1','4']
# # file = open(args[0],'r')
import math

def transfer(t_funct,input):
    if t_funct=='T1': return input
    if t_funct=='T2':
        if input > 0:
            return input
        else:
            return 0
    if t_funct=='T3':
        return 1/(1+math.exp(-input))
    if t_funct=='T4':
        return -1+(2/(1+math.exp(-input)))
def dot_product(input,weights,stage):
    sum = 0
    for i in range(len(input)):
        sum+=input[i]*weights[i]
    return sum
def dot(l1, l2):
    d=[]
    for x in range(len(l1)):
        d.append(l1[x]*l2[x])
    return d


def evaluate(file,input_vals,t_funct):
    weightslist = [line.rstrip('\n').split() for line in file]
    weights = []
    for i in weightslist:
        weight = []
        for j in i:
            weight.append(float(j))
        weights.append(weight)
    layers = [input_vals]
    level = len(weights)
    for x in weights:
        nextlayer = []
        for s in range(len(x)//len(layers[-1])):
            if level > 1:
                sum = dot_product(layers[-1],x[s*len(layers[-1]):s*len(layers[-1])+len(layers[-1])],level)
                nextlayer.append(transfer(t_funct,sum))
            else:
                nextlayer.append(dot(layers[-1],x[s*len(layers[-1]):s*len(layers[-1])+len(layers[-1])]))
        layers.append(nextlayer)
        level = level-1
    return layers[-1]



def main():
    inputs,t_funct,transfer_found = [],'T1',False
    for arg in args[1:]:
        if not transfer_found:
            t_funct,transfer_found = arg,True
        else:
            inputs.append(float(arg))
    li = (evaluate(file,inputs,t_funct))#ff
    for x in li:
        print (x,end = ' ')#final outputs
        
if __name__=='__main__':main()

#Randy Fu, Period 5, 2023