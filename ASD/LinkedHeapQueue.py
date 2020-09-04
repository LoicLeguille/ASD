class _Processus:
    def __init__(self, id, prio, pred = None, succ = None):
        self.id = id
        self.prio = prio
        self.pred = pred
        self.succ = succ

class LinkedHeapQueue:
    def __init__(self):
        self.__first = None
        self.__body = list()
        self.__priority = False

    def add(self, id, prio):
        toAdd = _Processus(id, prio)
        if self.__isEmpty():
            self.__first = toAdd
            self.__first.succ = self.__first
            self.__first.pred = self.__first
        else:
            last_element = self.__first.pred
            toAdd.pred = last_element
            toAdd.succ = self.__first
            self.__first.pred = toAdd
            last_element.succ = toAdd
        self.__body.append(toAdd)
        self.__body.sort(key = lambda x: x.prio, reverse = True)

    def __getPriorityMode(self):
        return self.__priority

    def __isEmpty(self):
        if not self.__first:
            return True

    def pop(self):
        if self.__isEmpty():
            return "BasicQueue is empty"
        if self.__first == self.__first.succ:
            processus = self.__first
            self.__first = None
            self.__body = list()
            return processus.id, processus.prio
        if not self.__getPriorityMode():
            processus = self.__first
            self.__body = list(filter(lambda x: x != self.__first, self.__body))
            self.__first.succ.pred = self.__first.pred
            self.__first.pred.succ = self.__first.succ
            self.__first = self.__first.succ
            return processus.id, processus.prio
        if self.__getPriorityMode():
            toRemove = self.__body.pop(0)
            processus = self.__first
            for m in range(len(self.__body) + 1):
                if processus == toRemove:
                    break
                else: processus = processus.succ
            if processus == self.__first:
                self.__first = self.__first.succ
            processus.succ.pred = processus.pred
            processus.pred.succ = processus.succ
            return processus.id, processus.prio

    def setPriorityMode(self, priority):
        self.__priority = priority

queue = LinkedHeapQueue()

print("To change the mode write 'NormalMode' or 'PriorityMode' (by default NormalMode)")
print("To add a Processus write 'add: NameProcessus, Priority'")
print("To delete a Processus from the queue write 'pop'")
print("To exit the program write 'end'")

choice = None

while choice != 'end':
    choice = input('\nyour choice:')

    if choice == 'NormalMode':
        queue.setPriorityMode(False)
        print('Mode set to Normal')

    if choice == 'PriorityMode':
        queue.setPriorityMode(True)
        print('Mode set to Priority')

    if choice[:5] == 'add: ':
        try:
            ProcessusName = choice[5:].split(',', 1)[0]
            ProcessusPriority = float(choice[5:].split(',', 1)[1][1:])
            queue.add(ProcessusName, ProcessusPriority)
            print(f'Processus ({ProcessusName}, {ProcessusPriority}) has been added to the queue')
        except: print('error while adding your Processus to the queue')

    if choice == 'pop':
        print(queue.pop())
