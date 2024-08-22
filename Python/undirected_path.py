def undirected_path(edges, node_A, node_B):
    graph = generate_graph(edges)
    print(graph)
    visited = set()
    queue = [node_A]
    while(len(queue) > 0):
        current = queue[0]
        queue.pop(0)
        print(f"Current: {current}")
        if current == node_B: return True
        if current not in visited:
            visited.add(current)
            print(f"Visited {visited}")
            for i in graph[current]:
               print(i)
            """visited.add(current)
            for neigbhor in graph[current]:
                print(f"Neigbhor {neigbhor}")
                queue.append(neigbhor)
                print(f"Visited {visited}")
                print(f"Current queue: {queue}")"""
    return False  

def generate_graph(edges: list) -> dict:
  g = {}
  for (a, b) in edges:
    if a in g:
      g[a].append(b)
    else:
      g[a] = [b]
    if b in g:
      g[b].append(a)
    else:
      g[b]= [a]
  return g

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'j', 'm')) # -> True