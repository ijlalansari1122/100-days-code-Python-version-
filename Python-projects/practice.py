# python practical applications

http_status = int(input('please enter your server status'))


def check_http_status(x):
    match x:
        case 200:
            print('OK')

        case 400:
            print('not a valid')

        case 500:
            print('not found')


# check_http_status(http_status)


list =[1,2,3,4]

for i in list:
    list.append(12)
    print(list)
