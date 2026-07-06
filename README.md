# Simulating-low-energy

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
 
## Outputs

The high energy and low energy simulations output zntuples, beamlossntuple, timentuple for most of the simulations. The zntuples are set to output so that each z position of the cell has its own output file, in the format Z100.txt where 100 is the distance it is recording for, this is to make it easy to pick a certain
z position. All the files are set to non extended or extended ASCII files so that spin polarisation can 
be tracked later. The beamlossntuple has the requirements to record all the muons that fulfill the require statment, and has the filename 'beamloss.txt'. The timentuple samples between two values and is output as one file 'output_t.txt' 

## Running the gpl scripts

If you want to use the gpl scripts need to make sure that you have the nature.journal style file and the .colour file. The scripts that use the zntuple data also have it set that the zntuple data is in a zntuple folder this 
was done to keep the different outputs separate because if the cell is large there can be a lot of Z files, many of the bash scripts made do this when running the simulations so if you use one of them to run the simulations it
should be done for you. 

## High energy simulations 

These simulations did not use the muCool physics list and so can be run using the normal g4bl command as shown below. 

```
g4bl high_energy.g4bl > g4_out
```

## Low energy simulations 

To run these simulations on Ada you need to make sure that the low energy physics list has been added by the team, if this has been done then you can use the command below to run it using mpi. There may be a problem if the .sif has a different name so make sure it is the same as the one in your home directory, and make sure that you use the name of your input file. 

```
apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl > g4_out
```

## Tools that were used 

A differential evolution optimiser was made to optimise parameters for the cell 




