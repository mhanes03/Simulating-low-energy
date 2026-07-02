
#[ -d zntuples ]  && mv Z* zntuples
[ ! -d zntuples ] && mkdir zntuples && mv Z* zntuples

cd zntuples
cp *.pdf ..
cd .. 

#gnuplot ~/gpls/energy_distributions/energy_distr.gpl

#gnuplot ~/gpls/gifs/stills.gpl