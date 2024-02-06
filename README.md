# Structify_OA
Algorithm Explanation:
(1) Populate dictionaries startPointsdict1 and endPointsdict2 with indices of "s" and "e" labels in chordPoints.
(2) Sort the dictionaries based on keys.
(3) Create a new list sortedChords by interleaving values from chordRadians based on the sorted order of "s" and "e" labels.
(4) Iterate over pairs of chords in sortedChords and count the number of intersecting chords.
(5) Avoid counting duplicate intersecting chords using a set remembered.
(6) Return the count of intersecting chords.

Time Complexity:
(1) Constructing dictionaries has a time complexity of O(n).
(2) Sorting the dictionaries has a time complexity of O(n * log(n)).
(3) Constructing sortedChords takes O(n) time.
(4) The nested loops for counting intersecting chords have a time complexity of O(n^2).
(5) Therefore, the overall time complexity is dominated by O(n^2).
