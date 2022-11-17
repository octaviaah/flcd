from finiteAutomata import FiniteAutomata


class UI:

    def __readFA(self):
        self.fa = FiniteAutomata.readFromFile('fa.in')

    def __displayFA(self):
        print(self.fa)

    def __displayStates(self):
        print(self.fa.getQ())

    def __displayAlphabet(self):
        print(self.fa.getE())

    def __displayInitialState(self):
        print(self.fa.getq0())

    def __displayFinalStates(self):
        print(self.fa.getF())

    def __displayTransitions(self):
        print(self.fa.getS())

    def __checkIfDFA(self):
        print(self.fa.isDFA())

    def __checkIfAccepted(self):
        sequence = input("Enter sequence: ")
        print(self.fa.isAccepted(sequence))

    def menu(self):
        print("1. Read FA from file")
        print("2. Display FA")
        print("3. Display states of FA")
        print("4. Display alphabet of FA")
        print("5. Display initial state of FA")
        print("6. Display final states of FA")
        print("7. Display transitions of FA")
        print("8. Check if FA is DFA")
        print("9. Check if inputed sequence is accepted")
        print("0. Exit")

    def run(self):
        while True:
            self.menu()
            print("Enter command: ")
            command = int(input())
            if command == 1:
                self.__readFA()
            elif command == 2:
                self.__displayFA()
            elif command == 3:
                self.__displayStates()
            elif command == 4:
                self.__displayAlphabet()
            elif command == 5:
                self.__displayInitialState()
            elif command == 6:
                self.__displayFinalStates()
            elif command == 7:
                self.__displayTransitions()
            elif command == 8:
                self.__checkIfDFA()
            elif command == 9:
                self.__checkIfAccepted()
            elif command == 0:
                break
            else:
                print("Invalid command")
                continue

