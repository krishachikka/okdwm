# Function to convert an adjacency matrix to an adjacency list
def adjacency_matrix_to_list(adj_matrix):
    graph = {}
    num_nodes = len(adj_matrix)
    for i in range(num_nodes):
        graph[chr(65 + i)] = []  # Using letters A, B, C, ... for node names
        for j in range(num_nodes):
            if adj_matrix[i][j] == 1:  # There is a link from node i to node j
                graph[chr(65 + i)].append(chr(65 + j))
    return graph

# Function to calculate PageRank
def calculate_pagerank(graph, pagerank, beta, iterations):
    num_nodes = len(graph)
    for it in range(iterations):
        new_pagerank = {}
        for node in graph:
            inbound_links = [n for n in graph if node in graph[n]]
            inbound_sum = 0
            
            for in_link in inbound_links:
                # Check if the PageRank of inbound link has been updated
                if in_link in new_pagerank:
                    inbound_sum += new_pagerank[in_link] / len(graph[in_link])
                else:
                    inbound_sum += pagerank[in_link] / len(graph[in_link])

            # Calculate new PageRank using the updated or fallback value
            new_pagerank[node] = (1 - beta) + beta * inbound_sum
        
        # Output the results for the iteration
        print(f"Iteration {it + 1}:")
        for node, pr in new_pagerank.items():
            print(f"PR({node}) = {pr:.4f}")

        # Update pagerank for the next iteration
        pagerank = new_pagerank

# Function to input adjacency matrix manually
def input_adjacency_matrix():
    size = int(input("Enter the number of nodes: "))
    adj_matrix = []
    print("Enter the adjacency matrix row by row (0 or 1):")
    for i in range(size):
        row = list(map(int, input().split()))
        adj_matrix.append(row)
    return adj_matrix

# Input the adjacency matrix manually
adj_matrix = input_adjacency_matrix()

# Convert adjacency matrix to graph
graph = adjacency_matrix_to_list(adj_matrix)

# Initialize constants
beta = 0.8
num_nodes = len(graph)
initial_pr = 1 / num_nodes

# Initialize PageRank values
pagerank = {node: initial_pr for node in graph}

# Perform PageRank calculation for 2 iterations
calculate_pagerank(graph, pagerank, beta, 2)