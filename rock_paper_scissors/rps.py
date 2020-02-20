#!/usr/bin/python

import sys
# n


def rock_paper_scissors(n):
    outcomes = []
    plays = ['rock', 'paper', 'scissors']

    def find_result(rounds_to_go, results=[]):
        # if our rounds to go == 0
        if rounds_to_go == 0:
            # append the result to the outcomes
            outcomes.append(results)
        # then return
            return 

        # iterate over plays
        for item in plays:
            # newresult = concatenate our result and our play resutl and our [plays] newres = result + [play]
            newresult = results + [item]
            # recursive call using roundstogo - 1, newres
            print(newresult)
            print('-------------------------------------')
            find_result(rounds_to_go-1, newresult)  
    # call find_results then pass in n, []
    find_result(n, [])
        # pass
# return the outcomes
    return outcomes
    # pass
# print(rock_paper_scissors(2))

def rock_paper_scissors1(n):
    choices = ["rock", "paper", "scissors"]
    output = []
    def inner_recursive(remaining, result):
        if remaining == 0:
            output.append(result)
            return
        for choice in choices:
            inner_recursive(remaining-1, result + [choice])
    inner_recursive(n, [])
    return output
print(rock_paper_scissors(2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
