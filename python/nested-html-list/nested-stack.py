import sys
class Heading:
    def __init__(this, weight, text):
        this.weight = weight
        this.text = text

class Node:
    def __init__(this, heading, children):
        this.heading = heading
        this.children = children


h1 = Heading(1, "introduction")
h2 = Heading(2, "overview")
h3 = Heading(3, "object")
h4 = Heading(3, "naming")
h5 = Heading(2, "design")
h6 = Heading(3, "data structure")
h7 = Heading(2, "architecture")
h8 = Heading(3, "components")
h9 = Heading(4, "pilot")
h10 = Heading(4, "mixer")
h11 = Heading(5, "k8s controller")
h12 = Heading(1, "conclusion")

def PrintNode(node):
    for _ in range(node.heading.weight * 2):
        sys.stdout.write(" ")
    print node.heading.text + "\n"
    for c in node.children:
        PrintNode(c)

def Pop(nodes, weight):
    nl = []
    current_node = nodes[-1]
    cur_weight = current_node.heading.weight
    while current_node.heading.weight != weight:
        while current_node.heading.weight == cur_weight:
            last_node = nodes.pop()
            nl.insert(0, last_node)
            current_node = nodes[-1]
        current_node.children = nl
        nl = []
        cur_weight = current_node.heading.weight
    #current_node.children = nl

def generate(headings):
    nodes = [Node(Heading(0, "My Article"), [])]
    for hd in headings:
        current_node = nodes[-1]
        new_node = Node(hd, [])
        if hd.weight >= current_node.heading.weight:
            nodes.append(new_node)
        else:
            Pop(nodes, hd.weight)
            nodes.append(new_node)
    Pop(nodes, 0)
    PrintNode(nodes[0])

generate([h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12])




