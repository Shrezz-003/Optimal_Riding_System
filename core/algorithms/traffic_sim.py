import random


def update_traffic(graph):
    """
    Randomly jams some roads.
    In a real app, this would fetch data from Google Maps API.
    """
    # Loop through every intersection in the city
    for node in graph.adj_list:
        for edge in graph.adj_list[node]:
            # 10% chance a road gets jammed every update
            if random.random() < 0.1:
                edge['traffic_factor'] = 5.0  # JAMMED!

            # 20% chance a road clears up
            elif random.random() < 0.2:
                edge['traffic_factor'] = 1.0  # CLEAR