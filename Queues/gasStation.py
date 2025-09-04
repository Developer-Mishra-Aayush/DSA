"""
Title: Gas Station (Circular Route)
Approach: Single pass tracking current balance and total deficit; when balance drops below 0, move start to i+1 and reset balance. Feasible if total gas >= total cost.
Time: O(n)
Space: O(1)
"""

def canCompleteCircuit(gas,cost):
    balance = 0
    start = 0
    defifict = 0
    for i in range(len(gas)):
        balance = balance + gas[i] - cost[i]
        # If Balance is Positive then don't worry
        if balance<0:
            start = i + 1
            defifict+=abs(balance)
            balance = 0
    if balance-defifict>=0:
        return start
    else:
        return -1

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
ans = canCompleteCircuit(gas,cost)
print("Starting Location of Car : ",ans)