# Simulating-low-energy

This git hub contains information on the low energy simulations carried out and details of the tools developed to carry these simulations out. The wiki contains details of how each of these tools work and how they can be used as well as information on the simulations carried out to develop options for low energy muon beamline. 

## Setting up, cloning the repository and pushing to it 

1. Will need to run in the terminal :
   
   ```
   git config --global user.name "Your github Username"
   git config --global user.email "Your GitHub account email address"
   ```
2. If you want to later push then next you will need to authenicate your github either by HTTPS or SSH (recommended) this can be done : https://docs.github.com/en/get-started/quickstart/set-up-git#authenticating-with-github-from-git
   In this you will need to set up an SSH key if you choose to use SSH so that you can push to the repository. If you don't plan to push then you can just clone the repository without setting this up. 
   
3. To clone this repository you will use the git clone command, and by either HTTPS or SSH
   
   ```
    git clone "URL from code button on main page of Simulating-low-energy"
   ```
4. If you want to add to the repository then you must first add, if there is a specific file or folder you can specify it as shown below :
   ```
   git add new.txt
   ```
   Or if you have multiple things to add you can use :

   ```
   git add .
   ```
5. Once you have added then you need to run the commit command and you can add a message using -m 
   ```
   git commit -m 'addding files'
   ```
6. Then to upload these changes use :
   ```
   git push
   ```
7. If you want to get the most up-to-date version of the repository or check that you do you can simply use
   ```
   git pull
   ```
## High energy simulations 

G4Beamline simulations run without the muCool physics list were run with the command shown below using the FTFP_BERT physics list 

```
g4bl high_energy.g4bl > g4_out
```
## Visualising G4Beamline input files

For the set-ups the input files were visualised using the command below 

```
g4bl input.g4bl viewer=best
```

## Low energy simulations 

To run these simulations on Ada you need to make sure that the low energy physics list has been added, if this has been done then you can use the command below to run it using mpi. There may be a problem if the .sif has a different name so make sure it is the same as the one in your home directory, and make sure that you use the name of your input file. 

```
apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl > g4_out
```

## Moving between SRIM/TRIM and G4Beamline

Due to limitations of the muCool physics list muons less than 1 keV have a infinite mean free path when moving through any material other than helium gas so a workflow was developed to simulate muons moving through other materials such as mylar degraders. To carry this out was done using a bash script and a python script 

```bash
bash convert_beam_file.sh
```
The python script was run in the bash script using the command 

```bash
python3 convert_to_BLTrack.py
```

## Differential evolution optimiser 

The Scipy differential evolution optimiser was used details of which can be found at https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html 

To run these scripts ran the command below 

```python
python3 optimise_voltage.py
```

## Using FEMM

To make magnetic and electric field maps to then import into G4Beamline, first created the fields in FEMM and then used lua script to make the fieldmap for G4Beamline. The script was run by loading the file in on the GUI and 


## Calculating breakdown voltage for helium and neon gas 

A python script was made to calculate an estimate for the breakdown voltage this was run as below 

```python
python3 paschen.py
```

## Bash scripts 

Bash scripts were used to run through different parameters using a do loop that runs simulations with new parameter values. 

```bash
bash sample_thickness.sh
```

To change the parameters from the command line in these scripts it was done as shown below for parameters set in the input file using param -unset

```
apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl degrader_thickness=$thickness > g4_out
```

## Outputs 

From the simualtions the timentuples were output as one output file and so to separate the entries into the specific time a bash script was used, run as shown below 

```bash
bash sort_time.sh
```

## Plotting 

To plot the output files both gnuplot and python were used, to run the gnuplot gpl scripts the command below was used, and the python plotting was done in jupyter notebooks. 

```
gnuplot energy_v_time.gpl
```
