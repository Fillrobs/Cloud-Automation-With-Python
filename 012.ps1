# Check for administrative privileges
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "This script must be run as an administrator" -ForegroundColor Red
    Exit 1
}
 
# Check for correct number of arguments
if ($args.Count -ne 3) {
    Write-Host "Usage: .\script_name.ps1 <NewHostname> <StaticIPAddress> <DNSServer>" -ForegroundColor Yellow
    Exit 1
}
 
# Assign arguments to variables
$newHostname = $args[0]
$staticIP = $args[1]
$dnsServer = $args[2]
 
# Set hostname
$sysInfo = Get-WmiObject -Class Win32_ComputerSystem
$sysInfo.Rename($newHostname)
 
# Set static IP address and DNS server
$networkAdapter = Get-NetAdapter | Where-Object { $_.Status -eq 'Up' }
$ipConfig = Get-NetIPConfiguration -InterfaceIndex $networkAdapter.InterfaceIndex
$ipConfig | Set-NetIPInterface -Dhcp Disabled
$ipConfig | Set-NetIPAddress -IPAddress $staticIP -PrefixLength 24
Set-DnsClientServerAddress -InterfaceIndex $networkAdapter.InterfaceIndex -ServerAddresses $dnsServer
 
Write-Host "Defaults set: Hostname to $newHostname, Static IP to $staticIP, and DNS to $dnsServer."
