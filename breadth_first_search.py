from collections import deque

def person_is_ending_with_t(name):
    return name[-1] == 't'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_ending_with_t(person):
                print("We found that",person,"is the one ending with t")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
