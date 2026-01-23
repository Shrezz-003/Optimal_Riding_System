from core.dsa.priority_queue import PriorityQueue


def find_path(graph, start_node, end_node, strategy):
    frontier = PriorityQueue()
    frontier.put(start_node, 0)
    came_from = {start_node: None}
    cost_so_far = {start_node: 0}

    while not frontier.empty():
        current_node = frontier.get()

        if current_node == end_node:
            break

        for edge in graph.get_neighbors(current_node):
            next_node = edge['to']
            added_cost = strategy.get_edge_weight(edge)
            new_cost = cost_so_far[current_node] + added_cost

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                frontier.put(next_node, new_cost)
                came_from[next_node] = current_node

    return reconstruct_path(came_from, start_node, end_node)


def reconstruct_path(came_from, start, end):
    current = end
    path = []
    if end not in came_from: return []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path