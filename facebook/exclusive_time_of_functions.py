# Author: Harsh Kohli
# Date created: 12/3/2020

def exclusiveTime(n, logs):
    stack, answer = [], []
    size = len(logs)
    if size == 0:
        return answer
    fid, event, tim = logs[0].split(':')
    fid, tim = int(fid), int(tim)
    stack.append((fid, event, tim, 0))
    time_map = {}
    prev_time = tim
    for index in range(1, size):
        log = logs[index]
        fid, event, tim = log.split(':')
        fid, tim = int(fid), int(tim)
        if event == 'end':
            _, _, _, clock_cycles = stack.pop()
            clock_cycles = clock_cycles + tim - prev_time + 1
            if fid in time_map:
                time_map[fid] = time_map[fid] + clock_cycles
            else:
                time_map[fid] = clock_cycles
        else:
            if len(stack) > 0:
                a, b, c, d = stack.pop()
                d = d + tim - prev_time - 1
                stack.append((a, b, c, d))
            stack.append((fid, event, tim, 0))
        prev_time = tim

    for i in range(n):
        answer.append(time_map[i])
    return answer


n = 2
logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
print(exclusiveTime(n, logs))
