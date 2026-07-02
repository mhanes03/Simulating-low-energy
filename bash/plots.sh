
[ -d zntuples ]  && mv Z* zntuples
[ ! -d zntuples ] && mkdir zntuples && mv Z* zntuples

gnuplot ~/gpls/energy_distributions/energy_distr.gpl

gnuplot ~/gpls/gifs/stills.gpl

bash ~/bash/low_energy_muons_2.sh