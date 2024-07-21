#!/bin/bash

# Prompt user to enter the device name (e.g., /dev/sdb) of the USB/Drive to overwrite
echo "Enter the device name (e.g., /dev/sdb) of the drive to overwrite:"
read device_name

# Verify that the device name provided exists
if [ ! -b "$device_name" ]; then
    echo "Device $device_name does not exist or is not accessible."
    exit 1
fi

# Prompt user for confirmation
echo -n "WARNING: This will irreversibly overwrite all data on $device_name. Proceed? (yes/no): "
read confirm

if [[ "$confirm" == "yes" || "$confirm" == "Yes" || "$confirm" == "YES" ]]; then
    echo "Overwriting drive $device_name with random data (Pass 1)..."

    # First pass overwrite with random data (1s and 0s)
    dd if=/dev/urandom of="$device_name" bs=4M status=progress

    echo "Overwriting drive $device_name with random data (Pass 2)..."

    # Second pass overwrite with random data (1s and 0s)
    dd if=/dev/urandom of="$device_name" bs=4M status=progress

    echo "Overwriting drive $device_name with random data (Pass 3)..."

    # Third pass overwrite with random data (1s and 0s)
    dd if=/dev/urandom of="$device_name" bs=4M status=progress

    echo "Overwriting complete."

else
    echo "Operation cancelled."
    exit 0
fi
