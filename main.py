#!/usr/bin/env python3
# Program created by Valeriy Litkovskyy


from listmanage import *


print('\nList program. To see commands, type "help".')

listing = {}


def help_to_newbie(listing, params=()):
    # Help menu
    print("""This is the list program created by Some Programmer.
You can create lists. It has normal mode and advanced mode. In normal mode
you only input commands. In advanced mode you can give more arguments to
commands, so you can move faster.

Help menu

    Normal mode:
        <command>
        add list    - Create new list to you list collection.
        add item    - Create new item in your lists.
        show lists  - Show all your lists.
        show items  - Show all items in your list.
        copy list   - Make a copy of list.
        copy items  - Copy items from one list to another. First you choose
                      list with items, then you choose the destination list.
        change list - Change the name of list.
        change item - Change the name of item in a list.
        change desc - Change the description of the item in your list.
        del list    - Remove your list, forever.
        del item    - Remove item in your list.
        help        - Show this menu.
        load        - Loads saved lists from listdata.data.
        exit        - Exit the program and saves lists to listdata.data.
        change mode - Change the mode of program.

    Advanced mode: in advanced mode the command looks like the following ->
                   <command> <argument1> <argument2> <argument3> <argumentN>

        add list    - al  <nameOfList>
        add item    - ai  <nameOfList> <nameOfItem>
        show lists  - sl
        show items  - si  <nameOfList>
        copy list   - cpl <nameOfList> <nameOfCopy>
        copy items  - cpi <nameOfList> <destinationList>
        change list - cl  <nameOfList> <newNameOfList>
        change item - ci  <nameOfList> <nameOfItem> <newNameOfItem>
        change desc - cd  <nameOfList> <nameOfItem>
        del list    - dl  <nameOfList>
        del item    - di  <nameOfList> <nameOfItem>
        help        - h
        load        - l
        exit        - e
        change mode - cm

                                                        Some Programmer
    """)
    return listing


def normal_user_command(commands):
    # Command for normal mode
    while True:
        user_cmd = input('\n[norm] Input command. --> ')
        if user_cmd in commands:
            return user_cmd


def advanced_user_command(commands):
    # Command for advanced mode with arguments
    while True:
        user_cmd = input('\n[adv] Input command. --> ')
        user_cmd = user_cmd.split()
        if user_cmd[0] in commands:
            return (user_cmd[0], tuple(user_cmd[1:]))


def change_mode(listing, params=()):
    # Change mode function
    mode = input('Mode? [adv/norm] ')
    if mode == 'adv':
        advanced_main(listing)
    elif mode == 'norm':
        normal_main(listing)
    else:
        return listing

# All the commands
normal_commands = {'add list': add_list,
                   'exit': prog_exit,
                   'load': load_list,
                   'add item': add_item,
                   'copy list': copy_list,
                   'change list': change_list,
                   'del list': del_list,
                   'copy items': copy_items,
                   'change item': change_item,
                   'change desc': change_desc,
                   'del item': del_item,
                   'show lists': print_lists,
                   'show items': print_items,
                   'help': help_to_newbie,
                   'change mode': change_mode
                   }

advanced_commands = {'al': add_list,
                     'e': prog_exit,
                     'l': load_list,
                     'ai': add_item,
                     'cpl': copy_list,
                     'cl': change_list,
                     'dl': del_list,
                     'cpi': copy_items,
                     'ci': change_item,
                     'cd': change_desc,
                     'di': del_item,
                     'sl': print_lists,
                     'si': print_items,
                     'h': help_to_newbie,
                     'cm': change_mode
                     }
# ---- The program ----


def normal_main(listing):
    # We check if listing is a dictionary
    if isinstance(listing, dict):
        # Then we execute command recursively
        normal_main(normal_commands[normal_user_command(normal_commands)](listing))


def advanced_main(listing):
    # We check if listing is a dictionary
    if isinstance(listing, dict):
        cmd = advanced_user_command(advanced_commands)
        # We execute command with arguments recursively
        advanced_main(advanced_commands[cmd[0]](listing, cmd[1]))
# Start program
if __name__ == '__main__':
    normal_main(listing)
