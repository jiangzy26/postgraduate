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
3
//Migration matrix 0:
0.000 0.000
0.000 0.000
//Migration matrix 1:
0 MIG12
MIG21 0
//Migration matrix 2:
0 MEIG12
MEIG21 0
//historical event: time, source, sink, migrants, new deme size, new growth rate, migration matrix index
5   historical event
Tc 1 0 1 RES_C 0 1
Tc 0 1 1 RES_E 0 1
Tac 1 1 1 RES_AC 0 0
Tac 0 0 1 RES_AE 0 0
TDIV 0 1 1 RESIZE 0 2
//Number of independent loci [chromosome] 
1 0
//Per chromosome: Number of contiguous linkage Block: a block is a set of contiguous loci
1
//per Block:data type, number of loci, per generation recombination and mutation rates and optional parameters
FREQ 1 0 3.3e-9 OUTEXP
