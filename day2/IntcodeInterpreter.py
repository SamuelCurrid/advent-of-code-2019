class Interpreter:

    def __init__(self):
        self.intcode = []
        self.noun = 1
        self.verb = 1
        self.instructions = 4


    def parseIntcode(self, file):
        """
        Takes intcode from a text file and converts it into a list to be used for this IntcodeInterpreter

        :param file: name of the intcode file to read from
        """
        with open("input.txt") as code:
            self.intcode = code.read().split(",")
            self.intcode = list(map(int, self.intcode))

    def setInstructions(self, number):
        """
        Sets the number of instructions (not really useful yet, hard coded as 4?)

        :param number: number of instructions
        """
        self.instructions = number

    def setNoun(self, number):
        """
        Sets the noun for the program

        :param number: integer to be used for the noun
        """
        self.noun = number

    def setVerb(self, number):
        """
        Sets the verb for the program

        :param number: integer to be used for the verb
        """
        self.verb = number

    def runIntcode(self):
        """
        Runs given intcode with current noun, verb, and instruction settings

        :return: the final integer stored in address 0 of the intcode
        """

        self.intcode[1] = self.noun
        self.intcode[2] = self.verb

        for instructionPointer in range(0, len(self.intcode), self.instructions):
            instruction = self.intcode[instructionPointer]

            if instruction is 99:
                break
            else:
                # Hard coded for now
                parameter1 = self.intcode[instructionPointer + 1]
                parameter2 = self.intcode[instructionPointer + 2]
                parameter3 = self.intcode[instructionPointer + 3]

                if instruction is 1:
                    self.intcode[parameter3] = self.intcode[parameter1] + self.intcode[parameter2]
                elif instruction is 2:
                    self.intcode[parameter3] = self.intcode[parameter1] * self.intcode[parameter2]
                else:
                    print("Bad opcode: " + str(self.intcode[i]))

        return self.intcode[0]