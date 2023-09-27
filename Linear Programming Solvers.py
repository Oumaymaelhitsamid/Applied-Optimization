#Python Linear Programming Solver with PuLP: Maximizing 2x + 3y subject to Constraints
# Import PuLP
import pulp

# Create a linear programming problem
lp_problem = pulp.LpProblem("My_LP_Problem", pulp.LpMaximize)

# Define decision variables
x = pulp.LpVariable("x", lowBound=1, cat='Continuous')
y = pulp.LpVariable("y", lowBound=2, cat='Continuous')

# Objective function to maximize
lp_problem += 2 * x + 3 * y, "Objective"

# Constraints
lp_problem += x + y <= 4, "Constraint 1"
# (Other constraints if needed)

# Solve the LP problem
lp_problem.solve()

# Print the status of the solution
print(f"Status: {pulp.LpStatus[lp_problem.status]}")

# Print the optimal values of the decision variables
print(f"x = {x.varValue}")
print(f"y = {y.varValue}")

# Print the optimal objective value
print(f"Optimal Objective Value = {pulp.value(lp_problem.objective)}")

#############

#Title: Solving the Assignment Problem using Gurobi in Python
import gurobipy as gp
from gurobipy import GRB

# Create a model
model = gp.Model("AssignmentProblem")

# Parameters
num_workers = 4
num_tasks = 4

cost_matrix = [
    [14, 7, 5, 8],
    [2, 12, 6, 5],
    [7, 5, 11, 3],
    [2, 4, 8, 10]
]

# Decision variables
assign = {}
for i in range(num_workers):
    for j in range(num_tasks):
        assign[i, j] = model.addVar(vtype=GRB.BINARY, name=f"assign_{i}_{j}")

# Objective function
model.setObjective(
    gp.quicksum(cost_matrix[i][j] * assign[i, j] for i in range(num_workers) for j in range(num_tasks)),
    GRB.MINIMIZE
)

# Constraints
# Each worker is assigned to exactly one task
for i in range(num_workers):
    model.addConstr(gp.quicksum(assign[i, j] for j in range(num_tasks)) == 1, f"worker_{i}_assignment")

# Each task is assigned to exactly one worker
for j in range(num_tasks):
    model.addConstr(gp.quicksum(assign[i, j] for i in range(num_workers)) == 1, f"task_{j}_assignment")

# Optimize the model
model.optimize()

# Print the optimal solution
if model.status == GRB.OPTIMAL:
    print("Optimal Assignment:")
    for i in range(num_workers):
        for j in range(num_tasks):
            if assign[i, j].x > 0.5:
                print(f"Worker {i} is assigned to Task {j} (Cost {cost_matrix[i][j]})")
    print(f"Total Cost: {model.objVal}")
else:
    print("No optimal solution found.")
