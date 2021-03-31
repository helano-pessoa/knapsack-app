# imports
import streamlit as st
import pandas as pd
from pulp import *

def knapsack(weights, profits, capacity):
    """ Return resolution of the knapsack problem."""

    # get knapsack size
    size = len(profits)

    # initialize model
    prob = LpProblem("Knapsack problem", LpMaximize)

    # define variable x
    x = LpVariable.dicts('x',range(len(profits)), lowBound=0, cat=LpBinary)

    # constraint 1: Chosen items cannot exceed the capacity of the knapsack
    prob += lpSum([weights[i]*x[i] for i in range(size)]) <= capacity, "c1"

    # objective function: maximize profit
    prob += lpSum([profits[i]*x[i] for i in range(size)]), "obj"
    
    # solve problem
    prob.solve()

    # get outputs
    solution = [v.varValue for v in prob.variables()]
    obj_value = value(prob.objective)

    return solution, obj_value

def main():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.title('Knapsack App')
    file = st.file_uploader('Upload Your file', type = 'csv')

    if file is not None:

        # read file and get parameters
        df = pd.read_csv(file)
        weights = df['Weights'].values.tolist()
        profits = df['Profits'].values.tolist()
        capacity = df['Capacity'].loc[0]


        if weights and profits and capacity:
            if st.button('Optimize'):
                sol, obj_value = knapsack(weights, profits, capacity)
                solution_table = st.table(pd.DataFrame(sol, columns=['Status']))
                
                # show solution and objective value
                st.write('Objective Value: ', obj_value)

# Run app
if __name__ == '__main__':
    main()