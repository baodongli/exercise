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

def generate(headings):
    nodes = [Node(Heading(0, "My Article"), [])]
    while headings:
        current_node = nodes[-1]
        hd = headings[0]
        new_node = Node(hd, [])
        if hd.weight > current_node.heading.weight:
            # update parent
            # push
            # move headings
            current_node.children.append(new_node)
            nodes.append(new_node)
            headings = headings[1:]
        elif hd.weight == current_node.heading.weight:
            # pop
            # update parent
            # push
            # move headings
            nodes.pop()
            current_node = nodes[-1]
            current_node.children.append(new_node)
            nodes.append(new_node)
            headings = headings[1:]
        else:
            # pop
            nodes.pop()
    PrintNode(nodes[0])

generate([h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12])




