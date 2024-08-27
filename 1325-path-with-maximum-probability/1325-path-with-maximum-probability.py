class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Build the adjacency list
        adj_list = {i: [] for i in range(n)}
        for i, (u, v) in enumerate(edges):
            adj_list[u].append((v, succProb[i]))
            adj_list[v].append((u, succProb[i]))

        # Initialize max_prob to track the max probability for each node
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        # Priority queue for BFS-like traversal, initialized with start node
        queue = [(-1.0, start_node)]  # Max heap, so we use negative probabilities

        while queue:
            curr_prob, node = heapq.heappop(queue)
            curr_prob = -curr_prob  # Convert back to positive

            # If we reach the end_node, return the probability
            if node == end_node:
                return curr_prob

            # Traverse all neighbors
            for neighbor, prob in adj_list[node]:
                # Calculate new probability for reaching neighbor
                new_prob = curr_prob * prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(queue, (-new_prob, neighbor))

        # If we can't reach the end_node
        return 0.0