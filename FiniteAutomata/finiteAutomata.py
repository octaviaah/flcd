class FiniteAutomata:
    def __init__(self, Q, E, q0, F, S):
        self.__Q = Q #set of states
        self.__E = E #alphabet of the language
        self.__q0 = q0 #initial state
        self.__F = F #set of final states
        self.__S = S #set of state transitions kept as HashMap (state, value) -> destinationState

    def getQ(self):
        return self.__Q

    def getE(self):
        return self.__E

    def getq0(self):
        return self.__q0

    def getF(self):
        return self.__F

    def getS(self):
        return self.__S

    @staticmethod
    def validate(Q, E, q0, F, S):
        if q0 not in Q: #if initial state not in states
            return False

        for final in F:
            if final not in Q: #if a final state is not in states
                return False

        for key in S.keys():
            state = key[0]
            symbol = key[1]
            if state not in Q:
                return False
            if symbol not in E:
                return False
            for destinationState in S[key]:
                if destinationState not in Q:
                    return False

        return True

    @staticmethod
    def getValues(line):
        #get the values of each field from the file
        return line.strip().split(' ')[2:]

    @staticmethod
    def readFromFile(fileName):
        with open(fileName) as f:
            Q = FiniteAutomata.getValues(f.readline())
            E = FiniteAutomata.getValues(f.readline())
            q0 = FiniteAutomata.getValues(f.readline())[0]
            F = FiniteAutomata.getValues(f.readline())

            S = {}
            f.readline()

            for line in f:
                source = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                route = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                destination = line.strip().split('->')[1].strip()

                if (source, route) in S.keys():
                    S[(source, route)].append(destination)
                else:
                    S[(source, route)] = [destination]

            if not FiniteAutomata.validate(Q, E, q0, F, S):
                raise Exception('The content does not represent a Finite Automata')

            return FiniteAutomata(Q, E, q0, F, S)


    def isDFA(self):
        for key in self.__S.keys():
            if len(self.__S[key]) > 1:
                return False
        return True

    def isAccepted(self, sequence):
        if self.isDFA():
            current = self.__q0

            for symbol in sequence:
                if symbol == ' ':
                    symbol = '<space>'
                if (current, symbol) in self.__S.keys():
                    current = self.__S[(current, symbol)][0]
                else:
                    return False
            return current in self.__F

        return False

    def __str__(self):
        return "Q = {" + ', '.join(self.__Q) + "}\n" \
            "E = {" + ', '.join(self.__E) + "}\n" \
            "q0 = {" + self.__q0 + "}\n" \
            "F = {" + ', '.join(self.__F) + "}\n" \
            "S = {" + str(self.__S) + "}"
