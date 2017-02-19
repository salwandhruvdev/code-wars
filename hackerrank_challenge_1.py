def braces(values):
    stack_count = []
    final_list = []
    index = 0
    for value in values:

        for i in value:
            if i in "{[(":
                stack_count.append(i)
            elif i in "}])":
                length_of_stack = len(stack_count)
                compare = stack_count[length_of_stack - 1]
                if i == '}' and compare == '{':
                    stack_count.pop()
                elif i == ']' and compare == '[':
                    stack_count.pop()
                elif i == ')' and compare == '(':
                    stack_count.pop()
                else:
                    final_list.append("No")
                    index = index + 1
        if len(stack_count) == 0:
            final_list.append("Yes")
    return final_list

if __name__ == "__main__":

    save = braces(["[[]]"])
    print save
