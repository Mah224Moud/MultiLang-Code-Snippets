def has_path(graph, src, dst):
  queue = [src]
  while(len(queue) > 0):
    current = queue[0]
    if current == dst: return True
    queue.pop(0)
    for neigbhor in graph[current]:
      if neigbhor == dst: return True
      queue.append(neigbhor)     
  return False


def main():
  graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
  }

  src = "f"
  dst = "j"
  hasPath = has_path(graph, src, dst)

  if hasPath:
    print(f"{graph} from {src} to {dst} has path")
  else:
    print(f"{graph} from {src} to {dst} has not path")
    
if __name__== "__main__":
  main()