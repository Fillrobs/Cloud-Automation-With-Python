#!/bin/bash
 
# Check for root privileges
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi
 
# Check for correct number of arguments
if [[ $# -ne 2 ]]; then
    echo "Usage: $0 <hostname> <static_ip>"
    exit 1
fi
 
# Assign arguments to variables
new_hostname="$1"
static_ip="$2"
dns_server="8.8.8.8"  # Replace with your desired DNS server
 
# Set hostname
echo "$new_hostname" > /etc/hostname
hostname "$new_hostname"
 
# Set static IP address (Debian)
echo -e "auto eth0\niface eth0 inet static\naddress $static_ip\nnetmask 255.255.255.0" > /etc/network/interfaces.d/eth0
 
# Set static IP address (Red Hat)
echo -e "DEVICE=eth0\nBOOTPROTO=static\nIPADDR=$static_ip\nNETMASK=255.255.255.0\nONBOOT=yes" > /etc/sysconfig/network-scripts/ifcfg-eth0
 
# Set DNS server
echo "nameserver $dns_server" > /etc/resolv.conf
 
# Restart networking services (Debian)
if command -v systemctl &>/dev/null; then
    systemctl restart networking
elif command -v service &>/dev/null; then
    service networking restart
fi
 
# Restart networking services (Red Hat)
if command -v systemctl &>/dev/null; then
    systemctl restart network
elif command -v service &>/dev/null; then
    service network restart
fi
 
echo "Defaults set: Hostname to $new_hostname, Static IP to $static_ip, and DNS."
