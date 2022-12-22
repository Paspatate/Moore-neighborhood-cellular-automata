
import random as rand
def create_random_list(size:tuple, threashold:int, seed):
    rand.seed(seed)
    M = [[1 if rand.random() < threashold else 0 for i in range(size[0])] for j in range(size[1])]
    return M

def ca_moore_neighborhood(tab:list, num_max_neighbor:int):
    newtab = [[0 for i in range(len(tab[j]))] for j in range(len(tab))]
    for y in range(len(tab)):
        for x in range(len(tab[y])):
            wall = get_num_surr_wall(tab, x, y)
            if wall > num_max_neighbor:
                newtab[y][x] = 1
            elif wall < num_max_neighbor:
                newtab[y][x] = 0
            else:
                newtab[y][x] = tab[y][x]
    return newtab

def get_num_surr_wall(tab:list, gridx:int, gridy:int):
    wall_count = 0

    for y in range(gridy-1,gridy+2):
        for x in range(gridx-1, gridx+2):
            if y >= 0 and y < len(tab) and x >= 0 and x < len(tab[y]):
                wall_count += tab[y][x]
            else:
                wall_count += 1
    return wall_count

if __name__ == "__main__":
    test = create_random_list((20,10), .5, 'lkdj')
    print(test)
    print(get_num_surr_wall(test,4,0))
