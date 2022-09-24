def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, component)

    component.append(node)

nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()]
    graph.append(children)

visited = [False] * nodes

for node in range(nodes):
    if visited[node]:
        continue
    componemt = []
    dfs(node, graph, visited, componemt)
    print(f"Connected component: {' '.join([str(x) for x in componemt])}")
