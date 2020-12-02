import sys


def reach(adj, x, y):
    global visited
    explore(adj, x)
    if visited[y] == True:
        return 1
    return 0


def explore(adj, v):
    global visited
    visited[v] = True
    for w in range(len(adj[v])):
        if visited[adj[v][w]] == False:
            explore(adj, adj[v][w])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    visited = [False for i in range(len(adj))]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
