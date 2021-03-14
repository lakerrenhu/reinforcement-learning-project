# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

#import csv
Qvector=[]

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        self.Qvalues = util.Counter()

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        #the initial value should be zero
        return self.Qvalues[(state,action)]
    
       # util.raiseNotDefined()


    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        #print(state)
        def largest(array,N):
            larg = array[0] # Initialial value 
            i=1 # compare every element with   
            while i<N: 
                if array[i] > larg: 
                    larg = array[i] # current max
                i=i+1
            return larg
        Qvalue=[]
        sets=self.getLegalActions(state)
        if state!='TERMINAL_STATE':
            ts=0
            while ts<len(sets):
                t=sets[ts]
            #for  t in sets:
                #Qvalue.append(self.getQValue(state,act))
                Qvalue.insert(len(Qvalue),self.getQValue(state,t))
                ts=ts+1
            if state==(1, 2):
               #print(state)
               #print((Qvalue))
               Qvector.append(Qvalue) #store Q-value for visualize the evolution
               #print(Qvector)
            return largest(Qvalue,len(Qvalue))
        else:
            #Qvalue.insert(len(Qvalue),0)
            #Qvector.append(Qvalue)
            #print(state)
            #print(Qvector)
            return 0
        
       # util.raiseNotDefined()

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        def largest(array,N):#find the largest one
            larg = array[0] # Initial value 
            i=1 # compare every element with   
            while i<N: 
                if array[i] > larg: 
                    larg = array[i] # current max
                i=i+1
            return larg
        opt_policy= None
        if state!='TERMINAL_STATE':# if it's not terminal state  
            sets=self.getLegalActions(state)
            Q_value=[]
            #get all Qvalue
            t1=0
            while t1<len(sets):
                ct=sets[t1] #get each state
                Q_value.insert(len(Q_value),self.getQValue(state,ct))
                t1=t1+1
                #Q_value.append(self.getQValue(state,act))
            t2=0
            while t2<len(sets):#get opt_policy=argmax(Qvalue)
                ct=sets[t2] #get each state
                tt=self.getQValue(state,ct)
                if tt==largest(Q_value,len(Q_value)):
                    opt_policy=ct
                t2=t2+1
            return opt_policy
        else:
            return opt_policy
        
        #util.raiseNotDefined()

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        s1=self.computeActionFromQValues(state)
        s2=random.choice(self.getLegalActions(state))
        s=util.flipCoin(self.epsilon)
        if state!='TERMINAL_STATE': # not terminal state
           action=s1 if s==False else s2
                #action=s
                #action=self.getPolicy(state)
            #else:
                #action=s2
                #action=random.choice(legalActions)
           return action
        else:
            return action  # if terminal state
        
        #util.raiseNotDefined()

        #return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
         
        s2= self.getValue(nextState)
        sample=self.discount*s2+reward
        s1= self.getQValue(state,action)
        self.Qvalues[(state,action)] = (1-self.alpha)*s1 + self.alpha*sample
        #self.Qvalues[(state,action)] = S1 + self.alpha*(sample-S1)
        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        
        util.raiseNotDefined()

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
