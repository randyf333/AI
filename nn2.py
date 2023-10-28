# import sys; args = sys.argv[1:]
# file = open(args[0], 'r')
import random
import math

def gen_network(structure, inputs):
    network = {} #id:[value, [connections], [weights]], except for the input which is just a value
    counter = 0
    for layer in range(len(structure)):
        for i in range(structure[layer]):
            if not counter:
                network[i] = inputs[i] #the inputs have no connections nor weights
            else:
                network[i + counter] = [0, [(counter - structure[layer - 1] + j) for j in range(structure[layer - 1])], [random.random() for j in range(structure[layer - 1])]]
        counter += structure[layer]
    #print('network: ' + str(network))
    return network

def transform(x):
    return 1/(1 + (math.e ** (-x)))

def feedfor(network, num_out): #runs feedforward network
    node_val = 0
    for node in network:
        node_val = 0
        if type(network[node]) == int:
            # skip inputs
            continue
        else:
            for i in range(len(network[node][1])):
                pointer = network[node][1][i]
                if type(network[pointer]) == int:
                    # special case for the inputs
                    node_val += network[i] * network[node][2][i]
                else:
                    # nodes that aren't the inputs
                    node_val += network[pointer][0] * network[node][2][i]
            if node < len(network) - num_out: #don't want to run transform on output
                node_val = transform(node_val)
        network[node][0] = node_val
    return network#[len(network) - 1]#[0] #return the whole network

def backprop(network, num_input, output, a): #this will only work with 1 output but with some changes could work with multiple
    network_err = {}
    for i in network: #make copy of network
        #print(i)
        #print(network[i])
        if type(network[i]) == int:
            network_err[i] = network[i]
        else:
            network_err[i] = [0, network[i][1], [0] * len(network[i][2])]

    for i in reversed(range(len(network))):  # calculate errors + gradients, put them in network_err
        #print('i: ' + str(i))
        error = 0
        if i <= num_input:
            break
        if i == len(network) - 1:  # if it's the output node
            error = output[0] - network[len(network) - 1][0]  # target output - actual output
            network_err[len(network_err) - 2][0] = error * network[len(network) - 1][2][0] #bruh
        else:
            network_err[i][0] *= network[i][0] * (1 - network[i][0])  #calculating error
            error = network_err[i][0]
            for j in range(len(network[i][2])):  # adding the errors to the next layer
                if type(network_err[network[i][1][j]]) == int: #if its an input we don't need to find error for it
                    continue
                network_err[network[i][1][j]][0] += network[i][2][j] * network_err[i][0]  # weight * error prev
        for j in range(len(network_err[i][2])):  # time to calculate the gradients + put them in the weights, used to be network_err
            if type(network[network[i][1][j]]) == int:
                network_err[i][2][j] = error * network[network[i][1][j]]
            else:
                network_err[i][2][j] = error * network[network[i][1][j]][0]  # E * x_i
        #print('error for node ' + str(i) + ': ' + str(error))

    for i in range(len(network)):  # changing weights here
        if type(network[i]) != int:
            for j in range(len(network[i][1])):
                network[i][2][j] += network_err[i][2][j] * a  # gradient * alpha + original weight

    #print('\nrunthrough completed\n')

    return network

def set_inputs(network, inputs): #sets inputs of network
    for i in range(len(inputs)):
        network[i] = inputs[i]
    return network

#def copy():
#    pass

def main():
    args = ['nn2test.txt']
    file = open(args[0], 'r')
    input_output = {}
    counter = 0

    for line in file:
        input = line[:line.index(' => ')].split(' ')#input=line.split(" => ")
        output = [int(line[line.index(' => ') + 4:].strip())]
        # if ' ' in line[line.index(' => ') + 4:]:
        #     output = []
        #     for x in line[line.index(' => ')+4:]:
        #         if x.isnumeric():
        #             output.append(int(x))
        #     input_output[counter] = [input_int,output]
        # else:
        #     output = [int(line[line.index(' => ') + 4:])]
        #output = int(line[line.index(' => ') + 4:])
        input_int = [int(i) for i in input]
        # training_set = line.rstrip().split()
        # training_set.remove('=>')
        # input_int = [int(training_set[i]) for i in range(2)]
        # output = int(training_set[-1])
        input_output[counter] = [input_int, output]
        counter += 1
        #print('input: ' + str(input_int))
        #print('output: ' + str(output))

    #print(input_output)
    #print('input output: ' + str(input_output))
    num_inputs = len(input_output[0][0])
    #print('layer counts: ' + str(num_inputs + 1) + ' 2 1 1')

    network = gen_network([num_inputs + 1, 2, 1, 1], input_output[0][0] + [1]) #hardcoded network lol
    #for input in input_output:
    #network = {0: 0, 1: 1, 2: [0, [0, 1], [0.07647, 0.1094]], 3: [0, [0, 1], [0.01749, 0.83799]], 4: [0, [2, 3], [0.42832, 0.65398]], 5: [0, [4], [0]]}
    #network = {0: 1, 1: 1, 2: [0, [0, 1], [1, 1]], 3: [0, [0, 1], [1, 1]], 4: [0, [2, 3], [1, 1]], 5: [0, [4], [1]]}

    counter = 0
    #while True:]
    for epoch in range(50000):
        #for i in range(50): #50 epochs

        inputs = 0
        output = 0
        if num_inputs > len(input_output):
            inputs = input_output[counter % len(input_output)][0]
            output = input_output[counter % len(input_output)][1]
        else:
            inputs = input_output[counter % len(input_output)][0]
            output = input_output[counter % len(input_output)][1]

        #inputs = input_output[1][0]
        #output = input_output[1][1]

        counter += 1
        network = set_inputs(network, inputs)
        network = feedfor(network, 1)
        #if inputs == [0]:
        #    print('input is 0')
        #print('ff net: ' + str(network))

        network = backprop(network, num_inputs, output, 0.5) #network, num_input, output, a

        #err_net = feedfor(network, 1)
        #print('total error: ' + str(0.5 * (output - err_net[len(err_net) - 1][0]) ** 2))
    #this part down is literally just printing + formatting
    weight_str = ''
    for i in network:
        if type(network[i]) != int:
            for j in network[i][2]:
                try:
                    weight_str += str(str(j)[:str(j).index('.') + 6]) + ' '
                except:
                    weight_str += str(j)

    weight_str = []
    for i in range(len(network) - num_inputs - 1): #formatting
        #print('thing: ' + str(network[num_inputs + i + 1][2]))
        temp = [j for j in network[num_inputs + i + 1][2]]
        weight_str.append(temp)

    final_weights = [weight_str[0]]
    final_weights[0] += weight_str[1]
    final_weights.append(weight_str[2])
    final_weights.append(weight_str[3])
    for i in range(len(final_weights)):
        for j in range(len(final_weights[i])):
            temp = str(final_weights[i][j])
            if 'e' not in temp:
                #print('without cut: ' + temp)
                #print('other thing: ' + temp[:str(final_weights[i][j]).index('.') + 6])
                final_weights[i][j] = float(temp[:str(final_weights[i][j]).index('.') + 6])
            else:
                final_weights[i][j] = 0

    #print('weights: ' + str(final_weights))
    weight_str = ''
    for i in final_weights:
        weight_str += str(i)[1:-1] + '\n'
    #print('weight str')
    print('Layer counts: [' + str(num_inputs + 1) + ', 2, 1, 1]') #input ' + str(inputs)) #each layer outputs go on one line
    print(weight_str)

    #print('wegithstr: ' + str(weight_str))


if __name__ == '__main__': main()
# Randy Fu, pd.5, 2023