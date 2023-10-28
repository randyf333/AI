#import sys; args = sys.argv[1:]
import random
import math

def gen_point(rad):
    x = random.uniform(-1.5, 1.5)
    y = random.uniform(-1.5, 1.5)
    in_circle = point_in_circle(x, y, rad)

    return ((x, y), in_circle)

def gen_network(structure, inputs):
    network = {} #id:[value, [connections], [weights]], except for the input which is just a value
    counter = 0
    for layer in range(len(structure)):
        for i in range(structure[layer]):
            if not counter:
                network[i] = inputs[i] #the inputs have no connections nor weights
            else:
                network[i + counter] = [0, [(counter - structure[layer - 1] + j) for j in range(structure[layer - 1])], [random.uniform(-2, 2) for j in range(structure[layer - 1])]]
        counter += structure[layer]
    return network

def transform(x):
    return 1/(1 + (math.e ** (-x)))

def set_inputs(network, inputs): #sets inputs of network
    for i in range(len(inputs)):
        network[i] = inputs[i]
    return network

def point_in_circle(x, y, r): #x and y are point coords, r is circle rad
    #print('r^2 = ' + str(r ** 2))
    #print('x^2 = ' + str(x ** 2))
    if abs(x) < r:
        y_circ = math.sqrt(r ** 2 - x ** 2)
        if abs(y) < y_circ:
            return True
    return False

def feedfor(network, num_out): #runs feedforward network
    node_val = 0
    for node in network:
        node_val = 0
        if type(network[node]) != list:
            # skip inputs
            continue
        else:
            for i in range(len(network[node][1])):
                pointer = network[node][1][i]
                if type(network[pointer]) != list:
                    # special case for the inputs
                    node_val += network[i] * network[node][2][i]
                else:
                    # nodes that aren't the inputs
                    node_val += network[pointer][0] * network[node][2][i]
            if node < len(network) - num_out: #don't want to run transform on output
                node_val = transform(node_val)
        network[node][0] = node_val
    return network

def backprop(network, num_input, output, a): #hypothetically should work because we're only returning 1 output
    network_err = {}
    for i in network: #make copy of network
        #print(i)
        #print(network[i])
        if type(network[i]) != list:
            network_err[i] = network[i]
        else:
            network_err[i] = [0, network[i][1], [0] * len(network[i][2])]

    for i in reversed(range(len(network))):  # calculate errors + gradients, put them in network_err
        error = 0
        if i <= num_input:
            break
        if i == len(network) - 1:  # if it's the output node
            error = output - network[len(network) - 1][0]  # target output - actual output
            network_err[len(network_err) - 2][0] = error * network[len(network) - 1][2][0] #bruh
        else:
            network_err[i][0] *= network[i][0] * (1 - network[i][0])  #calculating error
            error = network_err[i][0]
            for j in range(len(network[i][2])):  # adding the errors to the next layer
                if type(network_err[network[i][1][j]]) != list: #if its an input we don't need to find error for it
                    continue
                network_err[network[i][1][j]][0] += network[i][2][j] * network_err[i][0]  # weight * error prev
        for j in range(len(network_err[i][2])):  # time to calculate the gradients + put them in the weights, used to be network_err
            if type(network[network[i][1][j]]) != list:
                network_err[i][2][j] = error * network[network[i][1][j]]
            else:
                network_err[i][2][j] = error * network[network[i][1][j]][0]  # E * x_i

    for i in range(len(network)):  # changing weights here
        if type(network[i]) == list:
            for j in range(len(network[i][1])):
                network[i][2][j] += network_err[i][2][j] * a  # gradient * alpha + original weight

    return network

def find_op(op_str):
    if '<=' in op_str:
        return '<='
    elif '>=' in op_str:
        return '>='
    elif '<' in op_str:
        return '<'
    return '>'

def get_weights_str(network):
    weights_str = ''
    for i in network:
        if type(network[i]) != list:
            continue
        if type(network[i - 1]) == list and network[i - 1][1] != network[i][1]:
            weights_str = weights_str[:-2] + '\n'
        #for j in weights_str:
        #    weights_str += j[:j.index('.')]
        weights_str += str(network[i][2])[1:-1] + ', '
    return weights_str[:-2]

def main():
    args = ['x*x+y*y>1.2544203576549504']

    input = args[0]
    op = find_op(input)
    rad = float(input[input.index(op) + len(op):])

    network = gen_network([3, 4, 3, 1, 1], [0, 0, 1]) #3, 4, 3, 1

    # for epoch in range(1000000):
    while True:
        coords, in_circ = gen_point(rad)
        test_out = 0
        if op == '>=' or op == '>':
            test_out = int(not in_circ)
        elif op == '<=' or op == '<':
            test_out = int(in_circ)
        #print('coords: ' + str(coords))
        #print('in circle? ' + str(in_circ))
        network = set_inputs(network, coords)
        network = feedfor(network, 1)
        network = backprop(network, 3, test_out, 0.05) #a seems optimal at 0.1 (not changing)

        weight_str = get_weights_str(network)
        print('Layer counts: [3, 4, 3, 1, 1]')
        print(weight_str)

    #testing
    #print('\n')
    #network = set_inputs(network, (0.75, 0.5))
    #print('result: ' + str(feedfor(network, 1)))

if __name__ == '__main__': main()
#Randy Fu, pd.5, 2023