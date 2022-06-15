1. Sequence_Space.txt
A file containing a list of allowed amino acids at each diversified position.
For example:
	106A	ICHLM
	132A    FL
	271A	LIR
	217A	ML
In the following output files, the name of each mutant relates to the sequence space; and each mutation is represented with 2 digits.
For the sequence space shown above,a mutant with the name 04010202 has the following sequence: I106L, 132 is not mutated (numbered 01), L271I and M217L.
The mutant that contains in its name only .01. symbols (0101010101)  is the WT.	
	
2. Best_clustered_mutants.csv
A csv file (can be opened with Microsoft Excel) with the list of the clustered designs, ordered by Rosetta Energy (the lower is the energy, the more stable the mutant is expected to be). The first sequence is the WT (010101010101.).
 
3. Pdbs
The atomic structures of the top 50 predicted mutants by The algorithm, and the refined WT structure.
 
4. See mutations in PyMol
In order to highlight your mutations in a PyMol session, open the structures of the variants of interest in a PyMol session and the WT structure), then copy and run the Following commands in the PyMol commandline:

select diversified_positions, (chain A and resi 52) or (chain A and resi 77) or (chain A and resi 78) or (chain A and resi 79) or (chain A and resi 81) or (chain A and resi 101) or (chain A and resi 300)
hide all; show cartoon; show sticks, diversified_positions
