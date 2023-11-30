def getTotalExecutionTime(n, logs):
    exclusive_times = [0] * n
    stack = []
    prev_timestamp = 0

    for log in logs:
        log_parts = log.split(':')
        function_id, action, timestamp = int(log_parts[0]), log_parts[1], int(log_parts[2])

        if action == "start":
            if stack:
                exclusive_times[stack[-1]] += timestamp - prev_timestamp
            stack.append(function_id)
            prev_timestamp = timestamp
        else:
            exclusive_times[stack.pop()] += timestamp - prev_timestamp + 1
            prev_timestamp = timestamp + 1

    return exclusive_times

# Example usage:
n = 2
logs = ["0:start:0", "1:start:3", "1:end:6", "0:end:10"]
result = getTotalExecutionTime(n, logs)
print(result)