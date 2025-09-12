# Simulating-low-energy

## Setting up and cloning the repository

1. Will need to run in the terminal :
   
   ```
   git config --global user.name "Your github Username"
   git config --global user.email "Your GitHub account email address"
   ```
2. Next you will need to authenicate your github either by HTTPS or SSH this can be done : https://docs.github.com/en/get-started/quickstart/set-up-git#authenticating-with-github-from-git
3. To clone this repository you will use the git clone command, and by either HTTPS or SSH
   
   ```
    git clone "URL from code button on main page of Simulating-low-energy"
   ```

## High energy simulations 

The first simulations run were done at high energy so that an optimised gas cell could be set up that can then be used for low energy. The input file that corresponds to these simulations is called 
high_energy.g4bl. These simulations were run using a beam file, BEAM_100K.txt, to run this input file need to make sure the beam file is in the same directory.

## Low energy simulations 

The initial low energy simulations used the same high energy input file with the only change being the physics list was changed to muCool. 
