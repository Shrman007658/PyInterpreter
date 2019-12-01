work_to_do={
    "instructions":[
        ("LOAD_DATA",0),
        ("LOAD_DATA",1),
        ("ADD_TWO_VALUES",None),
        ("PRINT_ANSWER",None)],
    "numbers":[7,5]
}
#these are the instrutions that are crucial for understanding the basic working of an interpreter
#However, these instructions need to be fed to functions which understand them perfetly.
#so we design a function to take the input of these instructions.
class Interpreter:
    def __init__(self):
        self.stack=[]
    def LOAD_DATA(self,val):
        self.stack.append(val)
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
            if command is "LOAD_DATA":
                num=numbers[arg]
                self.LOAD_DATA(num)
            if command is "ADD_TWO_VALUES":
                self.ADD2VALUES()
            if command is "PRINT_ANSWER":
                self.printanswer()
interpreter=Interpreter()
interpreter.run_code(work_to_do)
