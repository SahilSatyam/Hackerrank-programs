"""
Your task is to design a contacts application that supports two features :

add name where name is a string that denotes the name of the contact. This operation must store a new contact by the name name.

find partial where partial is a string denoting a part of the name to search for in the directory. It must count the number of contacts that start with partial and print the count.

You are given n sequential operations of either type 1 or type 2. You are expected to perform them in the order given.

Input Format

The first line contains a single integer, n , denoting the number of operations to perform. Each line i of the n subsequent lines contains an operation in one of the two forms defined above.

Constraints

1 <= n <= 105
1 <= |name|, |partial| <= 21
It is guaranteed that name and partial contain lowercase english letters only.
Output Format

For each find partial operation, print the number of contact names starting with partial on a new line.

Sample Input 0

4
add hack
add hackerrank
find hac
find hak
Sample Output 0

2
0
"""

N = int(input())

trie = {}

def add_word(trie, word):
    # Base case
    if word == "": return
    
    # TODO: default dict
    if word[0] in trie:
        trie[word[0]]['count'] += 1
    else:
        trie[word[0]] = { 'count': 1 }
    add_word(trie[word[0]], word[1:])
    
def find_word(trie, word):
    if word[0] not in trie:
        return 0
    else:
        # Base case
        if len(word) == 1:
            return trie[word[0]]['count']
        else:
            return find_word(trie[word[0]], word[1:])

for i in range(N):
    line = input()
    command, word = line.split()
    if command == "add":
        add_word(trie, word)
    elif command == "find":
        print(find_word(trie, word))
    else:
        print("pass")
