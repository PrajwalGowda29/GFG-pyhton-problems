class Solution:
    def minEdgesReq(self, n, edges):
        if len(edges) < n - 1:
            return -1

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa != pb:
                parent[pb] = pa
                return True

            return False

        components = n

        for u, v in edges:
            if union(u, v):
                components -= 1

        return components - 1
        