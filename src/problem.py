from collections import defaultdict
import random


class Graph:
    """Data structure representing the given problem as a graph."""

    def __init__(self) -> None:
        self.graph: dict[str, dict[str, int]] = defaultdict(dict)

    def __str__(self) -> str:
        """String representation of the graph."""
        return "\n".join(
            [f"{node}: {connections}" for node, connections in self.graph.items()]
        )

    def add(
        self,
        first_node: str,
        second_node: str,
        weight: int = 0,
    ) -> None:
        """Add a node to the graph."""
        self.graph[first_node][second_node] = weight

    def get_nodes(self) -> list[str]:
        """Get all the nodes in the graph."""
        if not self.graph:
            return []
        return list(self.graph.keys())

    def get_neighbors(
        self,
        node: str,
    ) -> list[str]:
        """Get the neighbors of a given node."""
        return list(self.graph.get(node, {}).keys())

    def get_weight(
        self,
        first_node: str,
        second_node: str,
    ) -> int:
        """Get the weight between two nodes."""
        if first_node not in self.graph or second_node not in self.graph[first_node]:
            raise ValueError(f"Nodes {first_node} and {second_node} are not connected.")
        return self.graph[first_node][second_node]

    def evaluate_path(
        self,
        path: list[str],
    ) -> int:
        """Calculate the total weight of a path through the graph."""
        return sum(self.get_weight(path[i], path[i + 1]) for i in range(len(path) - 1))

    def validate_path(
        self,
        path: list[str],
    ) -> bool:
        """Validate a path through the graph."""
        return all(
            path[i + 1] in self.get_neighbors(path[i]) for i in range(len(path) - 1)
        )

    # I like convenience, sue me
    def random_path(self) -> list[str]:
        """Returns a random path through the graph."""
        nodes = self.get_nodes()
        random.shuffle(nodes)
        return nodes

    def remove(
        self,
        node: str,
    ) -> None:
        """Removes a node and all its connections from the graph."""
        if node not in self.graph:
            raise ValueError(f"Node {node} does not exist in the graph.")

        self.graph.pop(node)
        self.graph = {
            key: {k: v for k, v in value.items() if k != node}
            for key, value in self.graph.items()
        }

    @classmethod
    def populate(
        cls,
        nodes: int,
        max_weight: int,
    ) -> "Graph":
        """Populate a graph with the given number of nodes and max weight."""
        graph = cls()
        for node in range(nodes):
            for neighbor in range(node + 1, nodes):
                if random.random() > 0.5:
                    graph.add(
                        chr(65 + node),
                        chr(65 + neighbor),
                        random.randint(1, max_weight),
                    )
        return graph


nodes, maxWeight = random.randint(5, 24), random.randint(1, 15)
graph = Graph.populate(nodes, maxWeight)
print(graph)