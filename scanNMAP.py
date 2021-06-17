import nmap3
import json

scannerObject = nmap3.Nmap()
results = scannerObject.scan_top_ports("localhost")
results = json.dumps(results, indent=1, sort_keys=True)
print(results)

