from heapq import heapify, heappush, heappop
from platform import node

class Node:
    def __init__(self,name) -> None:
        self.name = name
        self.parent = False
        self.children = []
        self.depth = 0 # depth of node in tree

    def add_child(self,child,weight,depth=0) -> None:
        #self.depth = depth
        self.children.append((weight,child,depth))
    
    def get_children(self) -> list:
        return self.children

    def __str__(self) -> str:
        return str(self.name)

    def __lt__(self, other):
        return self.name < other.name

def print_nodes_values(nodes) -> None:
    for node in nodes:
        print(node[0],node[1],node[2],sep=', ')

def print_nodes(nodes) -> None:
    print(*nodes, sep=' -> ')

def dijkstra(start,end) -> list:
    unvisited = [(0, start, 0)]
    starting = True
    prev_depth = 0
    curr_depth = 0
    i = 1
    target_found = False
    shortest_path = []
    heapify(unvisited)
    # print("---Unvisited----")
    # print_nodes_values(unvisited)
    visited = []
    while unvisited:
        
        # print(f"Iteration : {i}")
        i += 1
        edge_length, current, curr_depth = heappop(unvisited)
        #prev_depth, curr_depth = curr_depth,
        current.depth = curr_depth
        shortest_path.append(current)
        visited.append(current)
        if len(shortest_path)>=2: 
            prev_depth = shortest_path[-2].depth
        
        if starting:
            prev_depth = -1
            starting = False
        # print("---shortestpath before popping----")
        # print_nodes(shortest_path)
        # print(f"Prev depth : {prev_depth} and curr depth : {curr_depth}")
        
        if curr_depth <= prev_depth:
            for _ in range(prev_depth - curr_depth + 1):
                shortest_path.pop(-2)
                # print("--Popped in Shortest path---")
    
        # print("---shortestpath after popping----")
        # print_nodes(shortest_path)

        if current.name == end.name:
            target_found = True
            print(f"Path between {start.name} and {end.name} exists")
            return shortest_path, edge_length
        
        for (weight,child,_) in current.get_children():
            if child not in visited:
                heappush(unvisited,(weight+edge_length, child, curr_depth+1))
        
        
        # print("---Unvisited----")
        # print_nodes_values(unvisited)            

    if not target_found:
        print(f"There is no path between {start.name} and {end.name}")
        return None,None




if __name__ == "__main__":
    # Creating Nodes
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')
    node_e = Node('e')
    node_f = Node('f')

    # Creating Node dict for future use
    node_dict = {
        'node_a':node_a,
        'node_b':node_b,
        'node_c':node_c,
        'node_d':node_d,
        'node_e':node_e,
        'node_f':node_f
    }

    # Adding children to nodes with edge weights
    node_a.add_child(node_b,2)
    node_a.add_child(node_d,6)
    node_b.add_child(node_c,1)
    node_b.add_child(node_e,3)
    node_b.add_child(node_f,2)
    node_d.add_child(node_b,1)
    node_d.add_child(node_e,0)
    node_e.add_child(node_f,2)  
    node_f.add_child(node_c,1)

    # node_delhi = Node('Delhi')
    # node_mumbai = Node('Mumbai')
    # node_agra = Node('Agra')
    # node_kolkota = Node('Kolkata')
    # node_chennai = Node('Chennai')
    # node_nagpur = Node('Nagpur')

    # node_dict = {
    #     'node_Delhi':node_delhi,
    #     'node_Mumbai':node_mumbai,
    #     'node_Agra':node_agra,
    #     'node_Kolkata':node_kolkota,
    #     'node_Chennai':node_chennai,
    #     'node_Nagpur':node_nagpur
    # }

    # node_delhi.add_child(node_mumbai,17)
    # node_delhi.add_child(node_agra,2)
    # node_delhi.add_child(node_kolkota,17)
    # node_mumbai.add_child(node_chennai,22)
    # node_kolkota.add_child(node_chennai,28)
    # node_agra.add_child(node_nagpur,11.5)
    # node_nagpur.add_child(node_chennai,17)

    # Calling Dijkstra Algorithm
    user_inp = input("Do you want to enter start and end node? (y/n) : ").lower()
    if  user_inp == 'y':
        start_node = input("Enter the starting node (options : a/b/c/d/e/f) : ")
        end_node = input("Enter the ending node (options : a/b/c/d/e/f) : ")

    else:
        start_node = 'Delhi'
        end_node = 'Chennai'
    
    print(f"Finding shortest path between {start_node} and {end_node}")
    start_node = node_dict[f"node_{start_node}"]
    end_node = node_dict[f"node_{end_node}"]
    shortest_path,short_length = dijkstra(start_node,end_node)
    if shortest_path is not None:
            print("Shortest path :  ", end=" ")
            print_nodes(shortest_path)
            print(f"Shortest path length : {short_length}")

