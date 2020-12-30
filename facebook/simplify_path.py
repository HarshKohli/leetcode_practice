# Author: Harsh Kohli
# Date created: 12/2/2020

def simplifyPath(path):
    commands = []
    for command in path.split('/'):
        if command != '' and command != '.':
            if command == '..':
                if len(commands) > 0:
                    commands.pop()
            else:
                commands.append(command)

    answer = '/'
    for command in commands:
        answer = answer + command + '/'

    if len(answer) > 1:
        return answer[:len(answer) - 1]
    return answer


path = "/a/./b/../../c/"
print(simplifyPath(path))
