import pickle
from copy import deepcopy
from listfuncs import *

listfile = 'listdata.data'
# Functions that don't need select_list select_item


def add_list(listing, params=()):
    # Create list
    tmp_list = deepcopy(listing)

    if not params:
        selected = create_list(listing)
    else:
        selected = params[0]

    tmp_list[selected] = {}
    print('\nList added.')
    return tmp_list


def prog_exit(listing, params=()):
    # Exit the program
    if input('Save lists? [yes/no] ') == 'yes':
        f = open(listfile, 'wb')
        pickle.dump(listing, f)
        f.close()
        print('Lists saved.')
    print('\nBye :*')
    return 'exit'


def load_list(listing, params=()):
    # Loads all lists from listdata.data
    tmp_list = deepcopy(listing)

    f = open(listfile, 'rb')
    to_load = pickle.load(f)
    f.close()

    for l in to_load.keys():
        name = l
        if name in tmp_list:
            print('List "{0}" already exists. Please rename it'.format(name))
            name = create_list(tmp_list)
        tmp_list[name] = to_load[l]
    print('Lists loaded')
    return tmp_list

# Functions that need select_list


def add_item(listing, params=()):
    # Create item in list
    tmp_list = deepcopy(listing)
    selected = None

    if (not params) and listing:
        selected = create_item(tmp_list, (select_list(tmp_list), None))
    elif listing:
        selected = check_params_list(tmp_list, params, 2)
        if selected:
            selected = (selected[0], None, selected[1])

    if selected:
        tmp_list[selected[0]][selected[2]] = '---'
        print('\nItem added.')
    return tmp_list


def copy_list(listing, params=()):
    # Copy list
    tmp_list = deepcopy(listing)
    selected = None

    if (not params) and listing:
        selected = (select_list(tmp_list), create_list(tmp_list))
    elif listing:
        selected = check_params_list(tmp_list, params, 2)

    if selected:
        tmp_list[selected[1]] = tmp_list[selected[0]]
        print('\nCopy created.')
    return tmp_list


def change_list(listing, params=()):
    # Change name of list
    tmp_list = deepcopy(listing)
    selected = None

    if (not params) and listing:
        selected = (select_list(tmp_list), create_list(tmp_list))
    elif listing:
        selected = check_params_list(tmp_list, params, 2)

    if selected:
        tmp_list[selected[1]] = tmp_list.pop(selected[0])
        print('\nList name changed.')
    return tmp_list


def del_list(listing, params=()):
    # Delete list
    tmp_list = deepcopy(listing)
    selected = None

    if (not params) and listing:
        selected = select_list(tmp_list)
    elif listing:
        selected = check_params_list(tmp_list, params, 1)

    if selected:
        tmp_list.pop(selected)
        print('\nList removed')
    return tmp_list


def copy_items(listing, params=()):
    # Copy all items from one list to another
    tmp_list = deepcopy(listing)
    selected = None

    if (not params) and listing:
        selected = (select_list(tmp_list), select_list(tmp_list))
    elif listing:
        selected = check_params_list(tmp_list, params, 2)

    if selected and (selected[0] != selected[1]):
        for i in tmp_list[selected[0]].keys():
            name = i
            if name in tmp_list[selected[1]]:
                print('Item "{0}" already exists. Please rename it'.format(name))
                name = create_item(tmp_list, (selected[1], selected[0]))[2]
            tmp_list[selected[1]][name] = tmp_list[selected[0]][i]

        print('\nItems copied.')
    return tmp_list

# Functions that need selecte_list and select_item


def change_item(listing, params=()):
    # Change name of item
    tmp_list = deepcopy(listing)
    selected = None

    if (not params) and listing:
        selected = create_item(tmp_list, select_item(tmp_list,
                                                     select_list(tmp_list)))
    elif listing:
        selected = check_params_item(tmp_list, params, 3)

    if selected:
        tmp_list[selected[0]][selected[2]] = tmp_list[selected[0]].pop(
                                                                    selected[1])
        print('\nItem name changed.')
    return tmp_list


def change_desc(listing, params=()):
    # Change description to item
    tmp_list = deepcopy(listing)
    selected = None

    if (not params) and listing:
        selected = select_item(tmp_list, select_list(tmp_list))
    elif listing:
        selected = check_params_item(tmp_list, params, 2)

    if selected:
        tmp_list[selected[0]][selected[1]] = input('\nType' +
                                                ' description to item. --> ')
        print('\nDescription changed.')
    return tmp_list


def del_item(listing, params=()):
    # Delete item in list
    tmp_list = deepcopy(listing)
    selected = None

    if (not params) and listing:
        selected = select_item(tmp_list, select_list(tmp_list))
    elif listing:
        selected = check_params_item(tmp_list, params, 2)

    if selected:
        tmp_list[selected[0]].pop(selected[1])
        print('\nItem removed.')
    return tmp_list
