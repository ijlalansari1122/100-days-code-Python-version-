# This program will be used for To-do application



# To-Do List App

todo_list =[]

try:
    while True:
            choose = int( input('please choose your action: 1 = view todo list  2 =add task 3 = mark task as done 4 = remove task 5 = quit  '))

            match choose:
                case 1:
                     for i in todo_list:
                      print('the To-do list is ',i )
                case 2:
                    add_task =input('please enter the new task  ')
                    todo_list.append(add_task)

                    print('the new task has been added in the list and the updated version is ', todo_list)

                case 3:
                    task_done =int(input('please specify which task has been completed '))

                    if 1<= task_done < len(todo_list):
                     todo_list[task_done-1]='Done'
                     print('the updated list is', todo_list)
                    else:print('invalid index')

                    print('the list after completing a task is ', todo_list)

                case 4:
                    remove_task = int(input('please specify which task you want to remove : 1 = first task and so on....'))
                    if 1 <= remove_task < len(todo_list):
                            remove_item = todo_list.pop(remove_task-1)
                            print('the removed item is' , remove_item)
                            print('the list after removing element is ', todo_list)
                    elif remove_task > len(todo_list):
                         todo_list.clear()
                         print('the list  is ', todo_list, 'please add tasks in the list for performing operations..')

                    else:print('invalid element')


                case 5:print('the program will terminate now ',exit() )

                case _:print('please choose valid value')
except ValueError:
    print('please provide proper value!!!!!!')