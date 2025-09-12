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

## Organisation 

The repository is set up that each part of the project has its own folder and corresponding wiki page to explain the outputs generated, and to store the bash, python and gnuplot scripts that were used to generate
the output. 

## Outputs

The high energy and low energy simulations output zntuples, beamlossntuple, timentuple. The zntuples are set to output so that each z position of the cell has its own output file this is make it easy to pick a certain
z position for plotting such as the beginning and end of the cell, the outputs come out in the format : 'Z100.txt' which would be for z = 100. All the files are set to extended ASCII files so that spin polarisation can 
be tracked later, and to make processing easier. The beamlossntuple has the requirements to record all the muons that are stopped within the cell, and has the filename 'beamloss.txt'. The timentuple samples between 0 and 
1000 ns and is output as one file 'output_t.txt' 

## Running the gpl scripts

If you want to use the gpl scripts need to make sure that you have the nature.journal style file and the .colour file. The scripts that use the zntuple data also have it set that the zntuple data is in a zntuple folder this 
was done to keep the different outputs separate because if the cell is large there can be a lot of Z files, many of the bash scripts made do this when running the simulations so if you use one of them to run the simulations it
should be done for you. 

## High energy simulations 

The first simulations run were done at high energy so that an optimised gas cell could be set up that can then be used for low energy. The input file that corresponds to these simulations is called 
high_energy.g4bl. These simulations were run using a beam file, BEAM_100K.txt, to run this input file need to make sure the beam file is in the same directory. These simulations can be run easily using the command, the '>' means 
that the output that would printed to the screen is written to the file g4_out this means that the parameters run during that simulation can be looked at later if you're unsure what you ran later.

```
g4bl high_energy.g4bl > g4_out
```
If you want to change an unset parameter in the input file such as the thickness of the degrader you can easily change this in the command line when running the input file, this can be done for any of the parameters that have -unset next to 
them in the input file and you can set as many as you want when you run the simulations. 

```
g4bl high_energy.g4bl degrader_thickness=0.5 > g4_out
```
## Low energy simulations 

The initial low energy simulations used the same high energy input file with the only change being the physics list was changed to muCool. These simulations used muCool and so you can't use the command shown above instead 


