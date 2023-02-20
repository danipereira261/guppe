class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, arr=None):
        self.head = None
        self.size = 0
        if arr:
            for item in arr:
                self.push(item)

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            old_head = self.head
            new_node.next = old_head
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            return
        val = self.head.data
        self.head = self.head.next
        self.size -= 1  # reduce the size
        return val

    def top(self):
        return self.head.data

    def as_list(self):
        node = self.head
        res = []
        while node is not None and node.next is not None:
            res.append(node.data)
            node = node.next
        return res


def is_number_valid(num):
    if 0 <= num < 2**20 - 1:
        return True
    else:
        return False


def is_integer(string):
    return all(i.isdigit() for i in string)


def solution(S):
    new_stack = Stack()
    for command in S.split():
        if is_integer(command):
            new_stack.push(int(command))

        elif command == "DUP":
            if new_stack.size > 0:
                x = new_stack.top()
                new_stack.push(x)
            else:
                return -1

        elif command == "POP":
            if new_stack.size > 0:
                x = new_stack.pop()
            else:
                return -1

        elif command == "+":
            if new_stack.size < 2:
                return -1
            else:
                x = new_stack.pop()
                y = new_stack.pop()
                res = x + y
                if is_number_valid(res):
                    new_stack.push(res)
                else:
                    return -1

        elif command == "-":
            if new_stack.size < 2:
                return -1
            else:
                x = new_stack.pop()
                y = new_stack.pop()
                res = x - y
                if is_number_valid(res):
                    new_stack.push(res)
                else:
                    return -1

    if new_stack.size == 0:
        return -1
    else:
        return new_stack.top()


print(solution("10 30 +"))