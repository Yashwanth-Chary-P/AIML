def is_consistent(assignment, variable, value, constraints):
    for constraint in constraints:
        if not constraint(assignment, variable, value):
            return False
    return True


def backtrack(assignment, variables, domains, constraints):
    # If all variables assigned → solution found
    if len(assignment) == len(variables):
        return assignment.copy()

    # Select unassigned variable
    variable = select_unassigned_variable(variables, assignment)

    for value in domains[variable]:
        if is_consistent(assignment, variable, value, constraints):

            # Assign value
            assignment[variable] = value

            # Recursive call
            result = backtrack(assignment, variables, domains, constraints)

            if result:
                return result   # stop at first solution

            # Backtrack (undo)
            assignment.pop(variable)

    return None


def select_unassigned_variable(variables, assignment):
    for variable in variables:
        if variable not in assignment:
            return variable


# Constraint: all values must be different
def example_constraint(assignment, variable, value):
    for var, val in assignment.items():
        if val == value:
            return False
    return True


if __name__ == "__main__":
    variables = ['X1', 'X2', 'X3']

    domains = {
        'X1': [1, 2, 4, 5],
        'X2': [1, 2, 3, 4],
        'X3': [1, 2]
    }

    constraints = [example_constraint]
    assignment = {}

    solution = backtrack(assignment, variables, domains, constraints)

    print("Solution:", solution)