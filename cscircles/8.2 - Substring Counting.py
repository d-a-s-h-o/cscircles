def count_substring(sub_string, string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


print(count_substring(input().strip(), input().strip()))