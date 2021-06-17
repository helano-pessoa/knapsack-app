from pulp import *

def knapsack(weights, profits, capacity):

    size = len(profits)

    prob = LpProblem("Knapsack problem", LpMaximize)

    x = LpVariable.dicts('x',range(len(profits)), lowBound=0, cat=LpBinary)

    prob += lpSum([profits[i]*x[i] for i in range(size)]), "obj"
    prob += lpSum([weights[i]*x[i] for i in range(size)]) <= capacity, "c1"

    prob.solve()

    solution = [v.varValue for v in prob.variables()]
    obj_value = value(prob.objective)

    return solution, obj_value