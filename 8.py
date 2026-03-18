import heapq

class Puzzle:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.n = 3

    # Heuristic: Manhattan Distance
    def manhattan_distance(self, state):
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                value = state[self.n * i + j]
                if value != 0:
                    goal_index = self.goal_state.index(value)
                    goal_i, goal_j = divmod(goal_index, self.n)
                    distance += abs(goal_i - i) + abs(goal_j - j)
        return distance

    # Generate neighboring states
    def get_neighbors(self, state):
        neighbors = []
        zero_index = state.index(0)
        i, j = divmod(zero_index, self.n)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for di, dj in directions:
            new_i, new_j = i + di, j + dj

            if 0 <= new_i < self.n and 0 <= new_j < self.n:
                new_state = state[:]
                new_index = new_i * self.n + new_j

                # Swap
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]

                neighbors.append(new_state)

        return neighbors

    # A* Search Algorithm
    def solve(self):
        start_state = tuple(self.start_state)
        goal_state = tuple(self.goal_state)

        frontier = []
        heapq.heappush(frontier, (self.manhattan_distance(start_state), 0, start_state, []))

        explored = set()

        while frontier:
            f, g, current_state, path = heapq.heappop(frontier)

            if current_state == goal_state:
                return path

            explored.add(current_state)

            for neighbor in self.get_neighbors(list(current_state)):
                neighbor_tuple = tuple(neighbor)

                if neighbor_tuple not in explored:
                    heapq.heappush(
                        frontier,
                        (
                            g + 1 + self.manhattan_distance(neighbor_tuple),  # f = g + h
                            g + 1,
                            neighbor_tuple,
                            path + [neighbor_tuple]
                        )
                    )

        return None


# Example Usage
start = [1, 2, 3,
         4, 5, 6,
         7, 0, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

puzzle = Puzzle(start, goal)

solution_path = puzzle.solve()

if solution_path:
    print("Solution found in", len(solution_path), "steps:\n")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")