from HashTable import HashTable

idtable = HashTable(20, "Identifiers table")
consttable = HashTable(20, "Constants table")

print("Identifiers table operations:")
print(idtable.add("a"))
print(idtable.add("b"))
print(idtable.add("u"))
print(idtable.add("getName"))
print(idtable.contains("a"))
print(idtable.contains("e"))
print("\n")
print(idtable.__str__())

print("Constants table operations:")
print(consttable.add("1"))
print(consttable.add("2"))
print(consttable.add("3"))
print(consttable.add("ion"))
print(consttable.contains("2"))
print(consttable.contains("false"))
print("\n")
print(consttable.__str__())



