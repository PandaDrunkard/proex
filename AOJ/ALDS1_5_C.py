import math
def stdinput():
    from sys import stdin
    return stdin.readline().strip()

def main():
    n = int(stdinput())
    nodes = [[0., 0.], [100., 0.]]

    for _ in range(n):
        next_nodes = []
        for s_node, e_node in zip(nodes[:], nodes[1:]):
            next_nodes.append(s_node)
            next_nodes += koch(s_node, e_node)
        next_nodes.append(nodes[-1])
        nodes = next_nodes

    for node in nodes:
        print(*map(lambda a: f'{round(a,8):.8f}', node))

def koch(start, end):
    nodes = []

    dx = (end[0] - start[0]) / 3
    dy = (end[1] - start[1]) / 3
    
    s = [start[0] + dx, start[1] + dy]
    t = [start[0] + 2 * dx, start[1] + 2 * dy]

    nodes.append(s)
    nodes.append(determine_koch(s, t))
    nodes.append(t)
    
    return nodes

def determine_koch(s, t):
    dx = (t[0] - s[0]) * math.sqrt(3) / 2
    dy = (t[1] - s[1]) * math.sqrt(3) / 2

    u0 = [s[0] - dy, s[1] + dx]
    u1 = [t[0] - dy, t[1] + dx]

    return [
        (u0[0] + u1[0]) / 2,
        (u0[1] + u1[1]) / 2
    ]

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')