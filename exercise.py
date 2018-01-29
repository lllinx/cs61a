from random import randint
def shuffle(list):
    n=len(list)
    if n<=1:
        return list
    else:
        i=randint(0,n)
        l=list[:n-1]
        return shuffle(l)[:i] + [list[n-1]] + shuffle(l)[i:]
        
s=[1,2,3,4]
shuffle(s)

def distinct(list):
	result=[]
	for element in list:
		if element not in result:
			result.append(element)
	return result

a=[1,2,3,4,2,3,5,7]
distinct(a)

def get_mode(list):
    a={}
    for element in list:
        if element not in a:
            a[element]=1
        else:
            a[element]+=1
    return max(a)

#partition tree#
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
        return not branches(tree)

def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if root(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(root(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


