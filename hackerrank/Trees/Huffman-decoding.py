# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    #Enter Your Code Here
    result = ''
    current_node = root
    for c in s:
        if c == '1':
            current_node = current_node.right
        else:
            current_node = current_node.left
        if current_node.left is None and current_node.right is None:
            result = result + current_node.data
            current_node = root
    print(result)   
