import re

from HashTable import HashTable
from ProgramInternalForm import PIF
from ReadFile import operators, separators, reserved, read_file
from Scanner import Scanner
from finiteAutomata import FiniteAutomata
from ui import UI


class Main:

    def __init__(self):
        self.idtable = HashTable(20, "Identifiers table")
        self.consttable = HashTable(20, "Constants table")
        self.pif = PIF()
        self.scanner = Scanner()

    def testFile(self, filename):
        read_file()
        exceptionMessage = ""
        faConstant = FiniteAutomata.readFromFile("constants.in")
        faIdentifier = FiniteAutomata.readFromFile("identifiers.in")

        with open(filename, 'r') as file:
            lineCount = 0
            for line in file:
                lineCount += 1
                tokens = self.scanner.tokenize(line.strip())
                for i in range(len(tokens)):
                    if tokens[i] in operators + reserved + separators:
                        if tokens[i] == ' ':
                            continue
                        self.pif.add(tokens[i], (-1, -1))
                    elif faIdentifier.isAccepted(tokens[i]):
                        identifier = self.idtable.add(tokens[i])
                        self.pif.add("id", identifier)
                    elif faConstant.isAccepted(tokens[i]):
                        constant = self.consttable.add(tokens[i])
                        self.pif.add("const", constant)
                    else:
                        exceptionMessage += 'lexical error at token - ' + tokens[i] + ' - at line ' + str(
                            lineCount) + "\n"

        with open('st.out', 'w') as writer:
            writer.write(str(self.idtable))
            writer.write("\n")
            writer.write(str(self.consttable))

        with open('pif.out', 'w') as writer:
            writer.write(str(self.pif))

        if exceptionMessage == "":
            print("lexically correct")
        else:
            print(exceptionMessage)

    def testP1(self):
        self.testFile('p1.txt')

    def testP2(self):
        self.testFile('p2.txt')

    def testP3(self):
        self.testFile('p3.txt')

    def testP1Err(self):
        self.testFile('p1err.txt')

    def runFiniteAutomataUI(self):
        ui = UI()
        ui.run()


main = Main()
main.testP1Err()






