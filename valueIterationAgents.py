# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

#import numpy as np
#import matplotlib.pyplot as plt
#import csv

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        ## three loops: for iteration,for states,for actions
        j=0
        tt=0
        n=self.iterations
        sset=self.mdp.getStates()
        Vvalue=[]
        #print(sset)
        #print(len(sset))
        def largest(array,N):
            larg = array[0] # Initial value 
            i=1 # compare every element with   
            while i<N: 
                if array[i] > larg: 
                    larg = array[i] # current max
                i=i+1
            return larg
        while j<n: #iteration loop
            self.values1=util.Counter()
            ts=0
            while ts<len(sset):#states loop
                st=sset[ts]
            #for st in sset:
                dt=self.mdp.isTerminal(st)
                Qvalue=[]
                if dt==False:
                #if st!='TERMINAL_STATE':
                    sets=self.mdp.getPossibleActions(st)
                    t=0
                    while t<len(sets):#action loop
                        tt=self.computeQValueFromValues(st, sets[t])
                        Qvalue.insert(len(Qvalue),tt)
                        t=t+1
                    #for t in sets:
                        #Qvalue.append(self.computeQValueFromValues(st, act))
                    #    tt=self.computeQValueFromValues(st, t)
                    #    Qvalue.insert(len(Qvalue),tt)
                else:
                    Qvalue.insert(len(Qvalue),0)
                larg=largest(Qvalue,len(Qvalue))
                self.values1[st]=larg
                #observe the evolution of V-value
                if st==(0, 2):
                   #print(st)
                   #print(larg)
                   Vvalue.insert(len(Vvalue),larg) #visualize the evolution of V-value
                ts=ts+1
            self.values=self.values1
            j=j+1
        #check the stored V-value at state of (0,2)
        #print(Vvalue)
        
         # name of csv file  
        #filename = "Vvalues.csv"
              # writing to csv file  
       # with open(filename, 'w') as csvfile:  
             # creating a csv writer object  
       #      csvwriter = csv.writer(csvfile)    
             # writing the data rows  
        #     csvwriter.writerows(Vvalue) 
        #compare the runtimes of two method
        #plt.plot(range(1,len(Vvalue)+1), Vvalue, 'r--')
        #plt.xlabel('the number of iteration')
        #plt.ylabel('V-value')
        #plt.title('The evolution of V-value at (0,2)')
        #plt.text(5, 1.5, 'red:  iterative method')
        #plt.text(5, 1.3, 'green:direct method')
        #plt.show()
        
    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        #get the list of nextstate and prob from mdp.getTransitionStatesAndProbs(state, action)
        #next_state_prob=self.mdp.getTransitionStatesAndProbs(state, action)
        #store each transition result
        Qvalue=[]
        for next_state,prob in self.mdp.getTransitionStatesAndProbs(state, action):
            Qvalue.insert(len(Qvalue),prob*(self.mdp.getReward(state, action, next_state)+
                                self.discount*self.values[next_state]))
        return sum(Qvalue)
    
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        dt=self.mdp.isTerminal(state)
        tt=0
        def largest(array,N): #find the largest one
            larg = array[0] # Initial value
            i=1 
            while i<N: 
                if array[i] > larg: 
                    larg = array[i] # current max
                i=i+1
            #print ("Largest in given array is",maxm)
            return larg
        opt_policy= None
        if dt==False:# if it's not terminal state
            #acts=self.mdp.getPossibleActions(state)
            Q_value=[]
            #get all Qvalue
            sets=self.mdp.getPossibleActions(state)
            #print(len(sets))
            #print(sets[0])
            t1=0
            while t1<len(sets):
                tt=self.computeQValueFromValues(state, sets[t1])
                Q_value.insert(len(Q_value),tt)
                t1=t1+1
            #get opt_policy=argmax(Qvalue)
            t2=0
            while t2<len(sets):
                tt=self.computeQValueFromValues(state, sets[t2])
                if tt==largest(Q_value,len(Q_value)):
                    opt_policy=sets[t2]
                t2=t2+1
            #for t in self.mdp.getPossibleActions(state):
            #    tt=self.computeQValueFromValues(state, t)
            #    if tt==largest(Q_value,len(Q_value)):
            #        opt_policy=t
            return opt_policy
        else:
            return opt_policy
        
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
