This is simple python script that help to scan some host for open ports. 
It has 3 modes that can be used:
1. Fast scan - this mode scan for most used ports like 21/22/80/443/8080 and other like that. 

python portscanner.py 192.168.1.1 --mode fast

2. Full scan - this use full range for scanning and it took alot of time and resources of the machine. 

python portscanner.py 192.168.1.1 --mode full

3. Range scan - here you can set some range of ports that you want to scan for like 20 to 1000

python portscanner.py 192.168.1.1 --mode range --start-port 1000 --end-port 2000

4. This scripts allow to save the output in file when adding "--output" flag and give a name of the file 
Here is example:

python portscanner.py 192.168.1.1 --mode fast --output scan_results.txt

You can also run this script only with ./portscanner.py just give executable permission with chmod.

sudo chmod +x portscanner.py

For more information you can use "-h" flag. 
