from collections import deque
from pprint import pprint
from typing import List, Dict, Set, Tuple


def levenshtein_distance(token1: str, token2: str):
    distances = [[0 for i in range(len(token2) + 1)] for j in range(len(token1) + 1)]

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if a <= b and a <= c:
                    distances[t1][t2] = a + 1
                elif b <= a and b <= c:
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]


def construct_graph(str_list: List[str]):
    graph: Dict[str, List[str]] = {s: [] for s in str_list}

    for i, string in enumerate(str_list):
        other_strings = str_list[:i] + str_list[i + 1:]
        for other in other_strings:
            if levenshtein_distance(string, other) == 1:
                graph[string].append(other)

    return graph


PATH_DOES_NOT_EXIST = -1


def bfs(graph: Dict[str, List[str]], node_from: str, node_to: str) -> int:
    distances: Dict[str, int] = {k: PATH_DOES_NOT_EXIST for k in graph.keys()}
    distances[node_from] = 0

    nodes_queue = deque()
    nodes_queue.append(node_from)

    while len(nodes_queue):
        node: str = nodes_queue.popleft()
        for neighbour in graph[node]:
            if distances[neighbour] == PATH_DOES_NOT_EXIST:
                distances[neighbour] = distances[node] + 1
                nodes_queue.append(neighbour)

    return distances[node_to]


def transform(start_str: str, end_str: str, str_list: List[str]):
    if end_str not in str_list:
        return 0

    return bfs(construct_graph(str_list + [start_str]), start_str, end_str) + 1
