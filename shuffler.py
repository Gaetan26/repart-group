from random import shuffle


def run(inputs:list, step:int) -> list:

    groups = list()
    shuffle(inputs)

    while len(inputs) > 0:

        if len(inputs) >= step:
            new_group = list()
            for i in range(0, step): 
                new_group.append(inputs[i])
            for student in new_group:
                inputs.remove(student)
            groups.append(new_group)
        
        else:
            length = len(inputs)
            new_group = list()
            for i in range(0, length): 
                new_group.append(inputs[i])
            for student in new_group:
                inputs.remove(student)
            
            groups.append(new_group)
    
    return groups