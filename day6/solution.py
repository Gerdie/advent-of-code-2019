import re

patt = r'(?P<orbitted>\w+)\)(?P<orbitter>\w+)'
node_map = {}


class Node(object):
    def __init__(self, num):
        self.num = num
        self.parent = None
        self.children = []

    def orbits(self, parent_node):
        self.parent = parent_node
        parent_node.children.append(self)

    def count_parents(self):
        if not self.parent:
            return 0
        return 1 + self.parent.count_parents()


def get_node(node_name):
    if node_name in node_map:
        return node_map[node_name]
    new_node = Node(node_name)
    node_map[node_name] = new_node
    return new_node


with open('input.txt') as input_file:
    for line in input_file:
        match = re.search(patt, line)
        orbitted = match.group('orbitted')
        orbitter = match.group('orbitter')
        orbitted_node = get_node(orbitted)
        orbitter_node = get_node(orbitter)
        orbitter_node.orbits(orbitted_node)

total_orbits = 0
for node in node_map:
    total_orbits += node_map[node].count_parents()

print('Part One: {}'.format(total_orbits))


def _get_path(path, node):
    if not path:
        return node.num
    return path + ',' + node.num


def find_path_to_santa(current_node, destination_node_num, seen_nodes, path=''):
    if current_node is None:
        return None

    if current_node.num == destination_node_num:
        return path

    current_children = current_node.children
    current_parent = current_node.parent
    child_path = None
    parent_path = None

    for child in current_children:
        if child.num not in seen_nodes:
            seen_nodes.add(child.num)
            c_path = find_path_to_santa(
                child, destination_node_num, seen_nodes, _get_path(path, child))
            child_path = child_path or c_path
    if current_parent and current_parent.num not in seen_nodes:
        seen_nodes.add(current_parent.num)
        parent_path = find_path_to_santa(
            current_parent, destination_node_num, seen_nodes, _get_path(path, current_parent))

    return child_path or parent_path


your_parent = node_map['YOU'].parent
santa_parent = node_map['SAN'].parent


path = find_path_to_santa(your_parent, santa_parent.num, set([your_parent.num]))
steps_in_path = len(path.split(','))

print('Part Two: {}'.format(steps_in_path))
