def second_index(text, some_str):
    count = 0

    for index, char in enumerate(text):

        if text[index:index + len(some_str)] == some_str:
            count += 1
        if count == 2:
            return index
    return None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'

print('ОК')
