# pystructures

This is a python package that contains my implementation
of datastructures

### The structures I already implemented

- Stacks:
    - **StaticTypeStack** -> only allow you to add data of a especified type (i.e. int, str, dict).

        ```Python3
        from mystructures import StaticTypeStack

        stack = StaticTypeStack(int)

        stack.push(0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.pop()

        n = 0
        for iten in stack:
            n += 1
            print(f'{n} -> {iten}')
        # 1 -> 0
        # 2 -> 1
        # 3 -> 2
        # 4 -> 3
        ```

- LinkedLinkedList:
    - **CircularLinkedLIst** -> an linked list witch repeat itself.

        ```Python3
        from mystructures import CircularLinkedList

        list = CircularLinkedList()

        list.append('C')
        list.append('C#')
        list.append('D')
        list.append('D#')
        list.append('E')
        list.append('F')
        list.append('F#')
        list.append('G')
        list.append('G#')
        list.append('A')
        list.append('A#')
        list.append('B')
        
        print(list)
        n = 0
        while True:
            print(list[n])
            n += 1
        ```
