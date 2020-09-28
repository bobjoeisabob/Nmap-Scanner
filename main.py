import nmap3

print("Nmap Multi Scanner")
print("<---------------->")

ip = input("please input IP or domain: ")
type = input("please choose type of scan 1)Top port 2)list 3)ping :")

print("scanning", ip, "now; output in JSON")

nmap = nmap3.NmapScanTechniques()
nmap3 = nmap3.Nmap()
if type == 1:
	results = nmap3.scan_top_ports(ip)
	print(results)

if type == 2:
	results1 = nmap.nmap_list_scan(ip)
	print(results1)

if type == 3:
	 results2 = nmap.nmap_ping_scan(ip)
	 print(results2)