import sys


def number_of_components(adj):
    global CC
    DFS(adj)
    return CC - 1


def DFS(adj):
    global visited
    global CC
    for i in range(len(adj)):
        if visited[i] == False:
            explore(adj, i)
            CC += 1

def explore(adj, v):
    global visited
    global CCgroup
    global CC
    CCgroup[v] = CC
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
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = [False for i in range(len(adj))]
    CCgroup = [0 for i in range(len(adj))]
    CC = 1
    print(number_of_components(adj))
