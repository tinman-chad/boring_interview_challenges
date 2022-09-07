#given a tree, find out if the left and right side match.

def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)


#given a tree take the first left node as root1 and right node as root2 and call are_symmetric