from collections import deque
import pprint
import json


def reverse_phrase(phrase: str) -> str:
    """Reverses the words in a phrase

    Args:
        phrase (str): input string of words

    Returns:
        str: phrase of reversed words
    """
    
    words = phrase.split(" ")
    words.reverse()
    return " ".join(words)

def is_mango_seller(person):
    if person[-1] == 'm':
        return True
    return False

def breadth_first_search(graph: dict, name_to_find: str) -> bool:
    # Initialize searched hash table O(V)
    searched = {}
    for vertex in graph:
        searched[vertex] = False
    
    # Search the graph O(E)
    search_queue = deque()
    search_queue.extend(graph['you'])

    while search_queue:
        person = search_queue.popleft()
                
        if searched[person] == False:
            if person == name_to_find:
                return True
            else:
                search_queue.extend(graph[person])
                searched[person] = True

    return False

def count_letters(sentence: str) -> dict:
    count = {}
    
    sentence = sentence.lower()
    
    for c in sentence:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
            
    return count


                
##############################################################
# main()
#
def main():
    string = "This is a test"
    reverse  = reverse_phrase(string)
    print(reverse)

    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    to_find = 'peggy'
    if breadth_first_search(graph, to_find) == True:
        print("Found " + to_find)
    else:
        print(to_find + " not found")
        
    count = count_letters("This is a test")
    
    print(json.dumps(count, indent=4))
    
    
if __name__ == "__main__":
    main()
