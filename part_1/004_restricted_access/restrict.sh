#!/bin/bash

# Step 1: Create a New User
sudo adduser auth_user

# Step 2: Assign appropriate file permissions
sudo chmod 700 $1

# Step 3: Change the owner of the script file
sudo chown auth_user $1

# Step 4: Change the privilege specification
command="pi ALL=(auth_user) NOPASSWD: /usr/bin/python $PWD/$1"
echo $command | sudo tee -a /etc/sudoers.d/010_pi-nopasswd > /dev/null

# Step 5: Remove the no password for the pi user
sudo sed -i '/pi ALL=(ALL) NOPASSWD: ALL/d' /etc/sudoers.d/010_pi-nopasswd

echo "###############################################"
echo "To run your script you must use this command:"
echo "sudo -u auth_user /usr/bin/python $PWD/$1"
echo "###############################################"
