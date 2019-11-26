def print_lists(listing, params=()):
    # Prints all lists.
    print('\nYour lists:')
    for i in listing.keys():
        print(' ---> ', i)

    return listing


def print_items(listing, params=()):
    # Prints all items in chosen list.
    if not params:
        # Yeah, I know. It is called KOSTYL
        selected = (select_list(listing),) if select_list(listing) else None
    else:
        selected = check_params_list(listing, params, 1)

    if selected:
        for key, value in listing[selected[0]].items():
            print(' ---> {0} : {1}'.format(key, value))

    return listing


def select_list(listing):
    # Returns selected list.
    while listing:
        print_lists(listing)
        selected_list = input('\nChoose list --> ')
        if selected_list in listing:
            return selected_list


def select_item(listing, sel_li):
    # Returns selected item in list.
    if sel_li in listing:
        while listing[sel_li]:
            print_items(listing, (sel_li,))
            selected_item = input('\nChoose item --> ')
            if selected_item in listing[sel_li]:
                return (sel_li, selected_item)


def create_list(listing):
    # Creates list
    while True:
        new_list = input('\nCreate list name. --> ')
        if new_list not in listing:
            return new_list
        print('This name already exists.')


def create_item(listing, selected_list_and_item):
    # Creates items to list
    while selected_list_and_item:
        new_item = input('\nCreate item name. --> ')
        if new_item not in listing[selected_list_and_item[0]]:
            return (selected_list_and_item[0], selected_list_and_item[1],
                    new_item)
        print('This name already exists.')


def check_params_list(listing, params, args):
    # Checks if list is in listing and there is enough arguments
    if (params[0] in listing) and (len(params) >= args):
        return params


def check_params_item(listing, params, args):
    # Checks if item is in list and there is enough arguments
    if (params[0] in listing) and (len(params) >= args):
        if params[1] in listing[params[0]]:
            return params
