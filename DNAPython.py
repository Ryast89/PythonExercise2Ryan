

number = input()          # Reading input from STDIN

for x in range(int(number)):
    input()
    sequence = input() 
    if "U" in sequence: 
        print("Error RNA nucleobases found!")
        continue
    sequence = sequence.replace("A", "1").replace("T", "2").replace("C", "3").replace("G", "4")
    sequence = sequence.replace("1", "T").replace("2", "A").replace("3", "G").replace("4", "C")
    print(sequence)
