import streamlit as st
from pulp import *
from pandas import read_csv

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

def main():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.title('Knapsack App')
    file = st.file_uploader('Upload Your file', type = 'csv')

    if file is not None:
        df = read_csv(file)
        weights = df['Weights'].values.tolist()
        profits = df['Profits'].values.tolist()
        capacity = df['Capacity'].loc[0]

        if weights and profits and capacity:
            if st.button('Optimize'):
                sol, obj_value = knapsack(weights, profits, capacity)
                st.write('Solution: ', sol)
                st.write('Objective Value: ', obj_value)


if __name__ == '__main__':
    main()