class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        hm, seen, edges = collections.defaultdict(list), collections.defaultdict(int), set()
        for f, t in redEdges: hm[f].append(tuple([t, 0]))
        for f, t in blueEdges: hm[f].append(tuple([t, 1]))
        ans = [0]
        q = deque()
        q.append([0, -1, 0])
        while q:
            node, prev_colour, prev_dist = q.popleft()
            if node not in seen: seen[node] = prev_dist
            else:
                if prev_dist < seen[node]: seen[node] = prev_dist
            for next_node, next_colour in hm[node]:
                if prev_colour!=next_colour and (node, next_node, next_colour) not in edges:
                    q.append([next_node, next_colour, prev_dist+1])
                    edges.add((node, next_node, next_colour))
        for i in range(1, n):
            if i not in seen: ans.append(-1)
            else: ans.append(seen[i])
        return ans