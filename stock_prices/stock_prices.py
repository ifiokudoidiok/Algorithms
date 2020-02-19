#!/usr/bin/python
'''
 For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

 So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 

 For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

loop through the array of numbers
store the first number in the lowest number  variable
store the second number in the highest number variable

if you find a number higher than the previous max number, as far as the max number has an index greater than the index of the lowest number,
swap the value for the higest number

if you find a number lower than the previous number, that is also not before the largest number(by index)
swap the values for the lowest number
return the result of max - min

save first value as max profit/num
if next number - max profit is bigger than our max profit,
next number = max num

'''
import argparse
def find_max_profit(prices):
  # create variable for max profit
  max_profit = prices[1] - prices[0]
  # create a variable for the min price
  min_price = prices[0]
  # for loop which loops in the range of 1 and the length of array/prices
  for i in range(1, len(prices)):
    # if max profit is less than current price - min price
    if max_profit < prices[i] - min_price:
      # change the variable max profit to current price - min price
      max_profit = prices[i] - min_price
    # if min price is greater than current price:
    if min_price > prices[i]:
      # update variable min price to current price
      min_price = prices[i]
  # return max profit 
  return max_profit
# O(n)
# def find_max_profit(prices):
    # use arr[:largest] to find the lowest number before the largest
# loop through the array of numbers
    # max_profit_so_far = prices[0]
    # for i in range(len(prices)):
    #         # print(prices[i])
    #         # i = 1
    #         if prices[i] > max_profit_so_far and i > 1:
    #             current_min_price_so_far = prices[i-1]
    #             max_profit_so_far = prices[i]
    #             print(max_profit_so_far , current_min_price_so_far)
    #             return max_profit_so_far - current_min_price_so_far
    #         else:
    #             max_profit_so_far = prices[0]
    #             current_min_price_so_far = prices[i+1]
    #             print(max_profit_so_far , current_min_price_so_far)
    #             return max_profit_so_far - current_min_price_so_far

                # [100, 500, 400, 200]

        

# store the first number in the lowest number  variable
# store the second number in the highest number variable

# if you find a number higher than the previous max number, as far as the max number has an index greater than the index of the lowest number,
# swap the value for the higest number

# if you find a number lower than the previous number, that is also not before the largest number(by index)
# swap the values for the lowest number
# return the result of max - min
print(find_max_profit([7,2,9,3,6,8]))


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))