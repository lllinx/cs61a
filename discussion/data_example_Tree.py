abcde = {'a':'.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.'}

def morse(code):
	root = Tree(None)
	for letter, signals in sorted(code.items()):
		tree = root
		for signal in signals:
			match = [b for b in tree.branches if b.root==signal] #entry is root
			if match:
				assert len(match) == 1
				tree = match[0]
			else:
				branch = Tree(signal)
				tree.branches.append(branch)
				tree = branch
		tree.branches.append(Tree(letter))
	return root

def decode(signals,tree):
	"""decode signals to letter
	>>> t= morse(abcde)
	>>> [decode(s) for s in ['.-', '-.-.', '-..', '.', '-...']]
	['a', 'c', 'd', 'e', 'b' ]
	"""
	for signal in signals:
		tree = [b for b in tree.branches if b.root==signal][0]
	leaves =  [b for b in tree.branches if not b.branches]
	assert len(leaves) == 1
	return leaves[0].root



### tree class ###
class Tree:
    def __init__(self, root, branches=()):
        for c in branches:
            assert isinstance(c, Tree)
        self.root = root
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.root, branches_str)

    def is_leaf(self):
        return not self.branches

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(Tree(1))
    1
    >>> print_tree(Tree(1, [Tree(2)]))
    1
      2
    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(t.root))
    for b in t.branches:
        print_tree(b, indent + 1)

