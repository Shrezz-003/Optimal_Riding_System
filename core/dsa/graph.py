class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, distance, speed_limit=50):
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []

        edge_data = {
            'to': v,
            'distance': distance,
            'speed': speed_limit,
            'traffic_factor': 1.0
        }
        self.adj_list[u].append(edge_data)
        self.adj_list[v].append({**edge_data, 'to': u})

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])