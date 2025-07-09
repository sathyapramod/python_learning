def split_and_join(line):
    # write your code here
    split_line_join = "-".join(line.split(" "))
    return split_line_join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)