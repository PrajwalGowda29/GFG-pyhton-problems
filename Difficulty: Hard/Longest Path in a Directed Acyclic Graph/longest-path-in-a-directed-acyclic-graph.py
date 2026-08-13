class Solution:
    def maxDistance(self, V, src, edges):
        from collections import deque

        # Create adjacency list
        adj = [[] for _ in range(V)]

        for u, v, w in edges:
            adj[u].append((v, w))

        # Find indegree
        indegree = [0] * V

        for u in range(V):
            for v, w in adj[u]:
                indegree[v] += 1

        # Topological sort
        q = deque()

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, w in adj[u]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        # Distance array
        dist = [-10**18] * V
        dist[src] = 0

        # Find longest distances
        for u in topo:
            if dist[u] == -10**18:
                continue

            for v, w in adj[u]:
                dist[v] = max(dist[v], dist[u] + w)

        # Unreachable vertices = INT_MIN
        INT_MIN = -2**31

        for i in range(V):
            if dist[i] == -10**18:
                dist[i] = INT_MIN

        return dist