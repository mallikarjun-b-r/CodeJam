class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.isEnd = False
        self.value = 0


def addWord(root, word: str):
    temp = root

    i = 0
    for char in word:
        f = 0
        for x in temp.children:
            if x.char == char:
                temp = x
                f = 1
                if i == len(word) - 1:
                    x.isEnd = True
                break
        if f == 0:
            node = TrieNode(char)
            temp.children.append(node)
            temp = node
            if i == len(word) - 1:
                node.isEnd = True
        i += 1


def solution(root):
    if len(root.children) == 0:
        root.value = 1
        return
    for x in root.children:
        solution(x)
        root.value += x.value
    if root.isEnd == True:
        root.value += 1
    if(root.value>=2 and root.char!=''):
        root.value -= 2



t=int(input())
for tt in range (t):
    root = TrieNode('')
    n=int(input())
    for i in range (n):
        k=input()
        addWord(root,k[::-1])

    solution(root)

    print("Case #{}: {}".format(tt+1,n-root.value))



