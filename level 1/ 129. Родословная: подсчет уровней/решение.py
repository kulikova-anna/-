import sys

def child_level(parent, tree_level, tree):
  try:
     for ch in tree[parent]:
      tree_level[ch] = tree_level[parent]+1
      child_level(ch,tree_level,tree)
  except:
    pass

def main():
    n = sys.stdin.readlines()

    input_data = []
    for i in n:
        input_data.append(i.replace("\n",""))
    input_data.pop(0)

    tree = {}
    child_list = []
    parent_list = []

    for i in input_data:
        child, parent = i.split()
        child_list.append(child)
        parent_list.append(parent)
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]

    child_list = list(set(child_list))
    parent_list = list(set(parent_list))

    tree_level = {}
    for p in parent_list:
        if p not in child_list:
            tree_level[p] = 0
            child_level(p, tree_level, tree)

    for key, value in sorted(tree_level.items()):
        print(f"{key} {value}")


if __name__ == '__main__':
    main()
