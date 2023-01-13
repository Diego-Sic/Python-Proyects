Deoxyribonucleic acid, or DNA, is the carrier of genetic information for living things. DNA is structured as a sequence of base pairs, which are abbreviated by the first letter of their names: (A)denine, (C)ytosine, (G)uanine, and (T)hymine. The subtle variations in DNA sequences are numerous enough that they are effectively unique to each person.

Some of the most reliable variations for determining who a sample of DNA belongs to is in Short Tandem Repeats (STRs). These STRs are sections of a DNA sequence which appears repeatedly without interruption.

For example, the sequences below belong to Alice and Bob, respectively: CTAGATAGATAGATAGATGACTA shows 4 x AGAT CTAGATAGATAGATAGATAGATT shows 5 x AGAT
Because these two subsequences show 4 and 5 repetitions of the STR "AGAT", we are able to distinguish Alice's DNA from Bob's. By finding the number of repetitions of several AGATs, we can accurately compare the STR repetition counts to many in a database, until we find a match. This is the principle on which DNA identification in forensics is based. With a database of names, and information about several standard STR sequences, an unknown sequence of DNA can be identified.

The database would contain information like this:
Name	AGAT	AATG	TATC
Alice	5	2	8
Bob	3	7	4
Charlie	6	1	5
The row for Alice indicates that the longest repeated sequences of "AGAT", "AATG", and "TATC" in Alice's DNA are known to be 5, 2, and 8 repeats long, respectively.

Assignment
Implement a program that identifies to whom a sequence of DNA belongs. In particular, the program should:

read a CSV file containing the STR counts for a series of individuals,
read a text file containing the DNA sequence to identify, and then
compute the longest run of consecutive repeats of the STR in the DNA sequence being identified.
If the STR counts match exactly with any of the individuals in the CSV file, your program should print out the name of the matching individual. You may assume that the STR counts will not match more than one individual.
If the STR counts do not match exactly with any of the individuals in the CSV file, your program should print "No match".
