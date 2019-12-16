from IntcodeInterpreter import Interpreter

#Part 1
program1 = Interpreter()
program1.parseIntcode("input.txt")
program1.setNoun(12)
program1.setVerb(2)

print("Part 1: " +str(program1.runIntcode()))

#Part 2
program2 = Interpreter()
noun = 0
verb = 0

while noun < 100:
    program2.parseIntcode("input.txt")
    program2.setNoun(noun)
    program2.setVerb(verb)


    if program2.runIntcode() == 19690720:
        break

    verb += 1

    if verb == 100:
        verb = 0
        noun += 1

print("Part 2: " + str(100 * noun + verb))