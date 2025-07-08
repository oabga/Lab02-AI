from maps import Map
from problems import RouteProblem
from bfs import breadth_first_search
from dfs import dfs_search
from ucs import ucs_search

if __name__ == "__main__":
    # romania = Map(
    #     {('O', 'Z'): 71, ('O', 'S'): 151, ('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118,
    #      ('L', 'T'): 111, ('L', 'M'): 70, ('D', 'M'): 75, ('C', 'D'): 120, ('C', 'R'): 146,
    #      ('C', 'P'): 138, ('R', 'S'): 80, ('F', 'S'): 99, ('B', 'F'): 211, ('B', 'P'): 101,
    #      ('B', 'G'): 90, ('B', 'U'): 85, ('H', 'U'): 98, ('E', 'H'): 86, ('U', 'V'): 142,
    #      ('I', 'V'): 92, ('I', 'N'): 87, ('P', 'R'): 97},
    #     {'A': (76, 497), 'B': (400, 327), 'C': (246, 285), 'D': (160, 296), 'E': (558, 294),
    #      'F': (285, 460), 'G': (368, 257), 'H': (548, 355), 'I': (488, 535), 'L': (162, 379),
    #      'M': (160, 343), 'N': (407, 561), 'O': (117, 580), 'P': (311, 372), 'R': (227, 412),
    #      'S': (187, 463), 'T': (83, 414), 'U': (471, 363), 'V': (535, 473), 'Z': (92, 539)})

    romania = Map(
        {('O', 'Z'): 71, ('O', 'S'): 151, 
         ('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118},

        {'A': (76, 497),'S': (187, 463), 'T': (83, 414),
          'Z': (92, 539), 'O': (117, 580)})



    # print(romania.neighbors)
    my_route = RouteProblem(initial='O', goal='A', map=romania)
    # print(my_route.actions('O'))
    # print(my_route.initial)
    # print(romania.distances['O', 'Z'])
    print(breadth_first_search(my_route))
    print(dfs_search(my_route))
    print(my_route.action_cost('S', '','O'))
    print(ucs_search(my_route))
    