//Parameters for the coalescence simulation program : fsimcoal2.exe
2 samples to simulate :
//Population effective sizes (number of genes)
NPOP1
NPOP2
//Samples sizes and samples age 
9
9
//Growth rates	: negative growth implies population expansion
0
0
//Number of migration matrices : 0 implies no migration between demes
2
//Migration matrix 0:
0.000 0.000
0.000 0.000
//Migration matrix 1:
0 MIG21
MIG12 0
//historical event: time, source, sink, migrants, new deme size, new growth rate, migration matrix index
1   historical event
TDIV 0 1 1 RESIZE 0 1
//Number of independent loci [chromosome] 
1 0
//Per chromosome: Number of contiguous linkage Block: a block is a set of contiguous loci
1
//per Block:data type, number of loci, per generation recombination and mutation rates and optional parameters
FREQ 1 0 3.3e-9 OUTEXP
