#!/usr/bin/perl -w
use strict;
use List::Util qw(min);
die "perl $0 <in> <out>\n"unless(@ARGV==2);

open( IN, "$ARGV[0]" ) or die "Can't open: tree.nhx\n";
my @arr2 = <IN>;
close IN;
my $treestr = join( "", @arr2 );
$treestr =~ s/[\n\r]+//g;

open( OUT, ">$ARGV[1]" )  or die "Can't open: tree.newick\n";
my $str = $treestr;
$str =~ s/\[.+?\]//g;
print OUT "$str\n";
close OUT;

open( OUT, ">$ARGV[1].4plot" )  or die "Can't open: tree.newick\n";
print OUT "$treestr\n";
close OUT;

system "perl /disk-1/reseqencing/p_major/code/draw_tree.pl $ARGV[1].4plot > $ARGV[1].4plot.svg";
