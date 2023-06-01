#!/bin/bash

# Set the path to your key file
KEY_FILE=$1

# Set the desired file permissions
PERMISSIONS="400"  # Only the owner has read permission

# Set the owner and group for the key file
OWNER="yourusername"
GROUP="yourgroupname"

# Change the file permissions
sudo chmod "$PERMISSIONS" "$KEY_FILE"

# Change the file owner and group
sudo chown "$OWNER:$GROUP" "$KEY_FILE"
