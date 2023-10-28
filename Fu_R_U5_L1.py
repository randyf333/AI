from pomegranate import *

#Cancer = DiscreteDistribution({'cancer':0.01, 'no-cancer':0.99})

#Tester = ConditionalProbabilityTable([
#   ['cancer', 'positive', 0.9],
#   ['cancer', 'negative', 0.1], 
#   ['no-cancer', 'positive', 0.2],
#   ['no-cancer', 'negative', 0.8]], [Cancer])

#s_cancer = State(Cancer, 'disease')
#s_tester_1 = State(Tester, 'tester_1')
#s_tester_2 = State(Tester, 'tester_2')

#model = BayesianNetwork('disease')

#model.add_states(s_cancer, s_tester_1, s_tester_2)

#model.add_transition(s_cancer, s_tester_1)
#model.add_transition(s_cancer, s_tester_2)

#model.bake() # finalize the topology of the model

#print ('The number of nodes:', model.node_count())
#print ('The number of elges:', model.edge_count())

## predict_proba(Given factors)
## P(pos | c) and P(neg | c)
#print (model.predict_proba({'disease':'cancer'})[1].parameters) 

## P(c | + +) and P(~c | + +)
#print (model.predict_proba({'tester_1':'positive', 
#   'tester_2':'positive'})[0].parameters)

## P(c | + -) and P(~c | + -)
#print (model.predict_proba({'tester_1':'positive', 
#   'tester_2':'negative'})[0].parameters)

## P(t2 = pos | t1 = pos) and P(t2 = neg | t1 = pos)
#print (model.predict_proba({'tester_1':'positive'})[2].parameters)

Graduate = DiscreteDistribution({'graduate':0.9,'no-graduate':0.1})
Tester = ConditionalProbabilityTable([['graduate','co1',0.5],['no-graduate','co1',0.05],['graduate','co2',0.75],['no-graduate','co2',0.25]])
s_graduate = State(Tester,'graduate')
s_tester_1 = State(Tester,'tester_1')
s_tester_2 = State(Tester,'tester_2')

model = BayesianNetwork('graduate')

model.add_states(s_graduate,s_tester_1,s_tester_2)

model.add_transition(s_graduate,s_tester_1)
model.add_transition(s_graduate,s_tester_2)

model.bake()
#P(o2|g,~o1)
print(model.predict_proba({'tester_1':'positive','tester_2':'negative'}))