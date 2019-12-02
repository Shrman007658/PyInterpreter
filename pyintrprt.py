work_to_do={
        "instructions": [("LOAD_DATA", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_DATA", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [5, 7],
        "names":   ["a", "b"] }
#
#these are the instrutions that are crucial for understanding the basic working of an interpreter
#However, these instructions need to be fed to functions which understand them perfetly.
#so we design a function to take the input of these instructions.
class Interpreter:
    def __init__(self):
        self.stack=[]
        self.map={} #mapping dictionary to map the values ofthe variables and the repective names of them.
    def LOAD_DATA(self,val):
        self.stack.append(val)
    def STORE_NAME(self,vname):
        val=self.stack.pop()
        self.map[vname]=val
    def LOAD_NAME(self,vname):
        val = self.map[vname]
        self.stack.append(val)
    def parse_argument(self, instruction, argument, work_to_do):
        """ Understand what the argument to each instruction means."""
        numbers = ["LOAD_DATA "]
        names = ["LOAD_NAME", "STORE_NAME"]

        if instruction in numbers:
            argument = work_to_do["numbers"][argument]
        elif instruction in names:
            argument = work_to_do["names"][argument]

        return argument


    def ADD2VALUES(self):
        fno=self.stack.pop()
        sno=self.stack.pop()
        sum=fno+sno
        self.stack.append(sum)
    def printanswer(self):
        print(self.stack.pop())
    def run_code(self,work_to_do):
        instruction=work_to_do["instructions"]
        numbers=work_to_do["numbers"]
        for a in instruction:
            command,arg=a
            arg = self.parse_argument(instruction, arg, work_to_do)
            if command is "LOAD_DATA":
                num=numbers[arg]
                self.LOAD_DATA(num)
            if command is "ADD_TWO_VALUES":
                self.ADD2VALUES()
            if command is "PRINT_ANSWER":
                self.printanswer()
## Now we add support for variables.
#Variables require two functions/instructions
#1. store_name function to store the name of the variable.
#2. load_name function to retrieve the value of the variable.
#3  A mapping function to map the name of the variable and its correspomding value.

#The work_to_do variable has changed accordingly..

interpreter=Interpreter()
interpreter.run_code(work_to_do)
