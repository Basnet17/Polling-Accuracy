'''
This program determines empirically how large a sample needs to be to reliably represent the sentiments of a large population.
Pritam Basnet
20th October
'''
import random
import matplotlib.pyplot as pyplot
def poll(percentage, pollSize):
    '''
    This function simulates the polling process by iterating over the number of individuals being polled and count them as a "yes" with probablity 0.3
    Parameters:
        Percentage: It is the probablity that the population responds "yes"/ favorably. 
        pollSize: the size of the population involving in the poll
    return: the percentage of pollresult
    '''
    count = 0
    for i in range(pollSize):
        r = random.random()                                             #generates the random number and stores in r
        if r < percentage:
            count = count + 1                                           #increases the value of count by 1 each time the condition is true.
    pollresult = (count/pollSize)* 100
    return pollresult 

def pollExtremes(percentage, pollSize, trials):
    '''
    This function investigates how much variation there can be in a poll of a particular size
    Parameters:
        percentage: It is the probablity that the population responds "yes"/ favorably. 
        pollSize: the size of the population involving in the poll
        trials: It is the number of times the function poll is called.
    return: min(aList): minimum value of the list.
            max(aList): maximum value of the list.
    '''
    aList = []
    for i in range(trials):                                             #creates a loop to call the previous function trials times
        Calling1 = poll(percentage, pollSize)
        aList.append(Calling1)                                          #appends the value of the pollresult in aList.
    return min(aList), max(aList)

def plotResults(percentage, minPollSize, maxPollSize, step, trials, pollSize):
    '''
    This function investigates how increasing poll sizes affect the variation of the poll results
    Parameters:
        percentage: It is the probablity that the population responds "yes"/ favorably.
        minPollSize: It is the maximum value of the population involving in the polling process
        maxPollSize: It is the minimum value of the population involving in the polling process.
        step: It is the increment in every step in the Poll Size. 
        trials: It is the number of times the function poll is called.
        pollSize: the size of the population involving in the poll
    Return: margin_of_error: the error in each poll size
    '''
    lowList = []
    highList = []
    pollsizeList = []
    for pollSize in range(minPollSize, maxPollSize,step):               #increases the pollSize each time with addition of value of step till it reaches maxPollsize
        low, high = pollExtremes(percentage, pollSize, trials)
        lowList.append(low)                                             #the low values are appended in the list
        highList.append(high)
        pollsizeList.append(pollSize)
        Margin_of_error = (high - low)/2                                #the margin of error is calculated


    #the plotting of values graph with pollsizeList in x-axis and low and high list in y-axis
    pyplot.plot(pollsizeList, lowList)
    pyplot.plot(pollsizeList, highList)
    pyplot.xlabel('Poll Size')
    pyplot.ylabel('Poll Extremes')
    pyplot.show()
    return Margin_of_error
    
def main():
    percentage = 0.3
    pollSize = 1000
    trials = 400
    minPollSize = 10
    maxPollSize = 200
    step = 10
    part1 = poll(percentage, pollSize)                                   #first function is called with parameters being given the value
    partMin, partMax = pollExtremes(percentage, pollSize, trials)
    part3 = plotResults(percentage, minPollSize, maxPollSize, step, trials, pollSize)
    print('The poll result is: ', part1,'%')
    print('The minimum value is:', partMin, 'The maximum value is:',partMax)
    print('The Margin of error is:',part3)                              #The margin of error from the third function is printed

 
main()
