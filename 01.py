
def reduceAbility(ability, choose_ability):
    index = ability.index(choose_ability)
    ability[index] = int(choose_ability / 2)


def minimumTime(ability, processes):
    n_processes = len(ability)
    greater_ability = max(ability)
    remaining_processes = processes
    processing_time = 0
    kill_process = True

    while (kill_process):
        if greater_ability not in (1, 2):
            remaining_processes = remaining_processes - greater_ability
            processing_time += 1
            reduceAbility(ability, greater_ability)
            greater_ability = max(ability)
        else:
            remaining_processes = remaining_processes - sum(ability)
            processing_time += n_processes

        if remaining_processes <= 0:
            kill_process = False

    return processing_time


def main():
    ability = [10, 7, 10, 9, 10, 6, 3, 9, 9, 10, 10]
    processes = 122

    print(minimumTime(ability, processes))

if __name__ == '__main__':
    main()