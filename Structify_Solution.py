#Main function that takes in the two input lists
def intersectingChords(chordRadians, chordPoints):
    
    startPointsdict1 = {}
    endPointsdict2 = {}
    
    # Populate dictionaries with indices of "s" and "e" labels in chordPoints
    for index, val in enumerate(chordPoints):
        if 's' in val:
            startPointsdict1[val] = index
            
        elif 'e' in val:
            endPointsdict2[val] = index

    # Sort the dictionaries based on keys (labels)
    myKeys1 = list(startPointsdict1.keys())
    myKeys1.sort()
    sorted_dict1 = {i: startPointsdict1[i] for i in myKeys1}
     
    # Create a new list 'sortedChords' by interleaving values from chordRadians
    myKeys2 = list(endPointsdict2.keys())
    myKeys2.sort()
    sorted_dict2 = {i: endPointsdict2[i] for i in myKeys2}
    
    
    sortedChords = [0] * len(chordRadians)
    
    ptr = 0
    
    for val in sorted_dict1.values():
        sortedChords[ptr] = chordRadians[val]
        ptr += 2
        
    ptr = 1
        
    for val in sorted_dict2.values():
        sortedChords[ptr] = chordRadians[val]
        ptr += 2
        
    remembered = set()
    output = 0
    
    # Count the number of intersecting chords
    for i in range(0, len(sortedChords), 2):
        for j in range(0, len(sortedChords), 2):
            if i == j:
                continue
            
            
            
            if (sortedChords[i] >= sortedChords[j] and sortedChords[i] <= sortedChords[j+1]) or (sortedChords[i+1] >= sortedChords[j] and sortedChords[i+1] <= sortedChords[j+1]):
                intersectingChords = ""
                intersectingChords += str(sortedChords[i] + sortedChords[i+1] + sortedChords[j] + sortedChords[j+1])
    
                if (intersectingChords not in remembered):
                
                    output += 1
                    remembered.add(intersectingChords)
            
            
                
    return f"Total Number of Intersections - {output}"
    
print(intersectingChords([0.78, 1.47, 1.77, 3.92], ["s_1", "s_2", "e_1", "e_2"]))
print(intersectingChords([0.9, 1.3, 1.70, 2.92], ["s1", "e1", "s2", "e2"]))
