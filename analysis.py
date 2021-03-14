# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    #the noise affects the prob of jumping into the pits and V values.
    #the current settings of discount=0.9 noise=0.2 cannot lead the agent
    #to crossing the bridge.If the noise decreases to be 0 or close to 0,
    #then the search of agent is treated as a deterministic problem.
    #the V values from left to right will be:[5.9, 6.56, 7.29, 8.1, 9].
    #theoretically, the agent will cross the bridge from left to right. 
    answerDiscount = 0.9
    answerNoise = 0
    return answerDiscount, answerNoise

def question3a():
    #if the living reward is a big penalty, the agent tends to end the game quickly
    #small noise mean more likely to risk
    answerDiscount = 1#0.9
    answerNoise = 0.01#0.01
    answerLivingReward = -5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    #low discount encourages the agent to get reward earlier(+1) than later (+10)
    #positive living reward makes the agent want to live longer
    #dont want to risk of jumping into pits
    answerDiscount = 0.2#0.2
    answerNoise = 0.01
    answerLivingReward =0 #0.5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    #if there's no living penalty,then the agent would prefer (+10)
    #small noise lets the agent not worried about pits
    #reasonable discount will make the agent find a shortcut
    answerDiscount = 0.5#0.7,0.5 works
    answerNoise = 0.01
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    #no discount and low living penalty make the agent prefer (+10)
    #large noise increases the risk of jumping into pits
    answerDiscount = 1
    answerNoise = 0.3
    answerLivingReward = -0.2
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    #since living reward is very large, living longer brings more rewards
    answerDiscount = 1
    answerNoise = 0
    answerLivingReward = 100
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print 'Answers to analysis questions:'
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print '  Question %s:\t%s' % (q, str(response))
