
import requests
import time


# api-endpoint
#URL = "http://15.236.22.86:5000/api/jobirl/list2"  # AWS EC2
URL = "http://15.236.22.86:5000/api/jobirl/reco?majeur=S&mineur=C"
#URL = "http://15.236.22.86:5000/api/jobirl/reco?majeur=S"
#URL = "http://35.181.31.116:5000/api/jobirl/reco?majeur=S&mineur=C"
#URL = "http://jobirl-equilib-335900729.eu-west-3.elb.amazonaws.com:5000/api/jobirl/list"

#URL = "http://92.222.68.188:5000/api/jobirl/list2" # OVH
#URL = "http://bibliotec.fr:5000/api/jobirl/list2" # OVH
ITER = 10

#payload = {'key1': 'value1', 'key2': 'value2'}
#r = requests.get("http://httpbin.org/get", params=payload)

print("Itérations : " + str(ITER) + " / Starting...")

tic = time.perf_counter()

for i in range(ITER):
    #print("Itération " + str(i))
    r = requests.get(url=URL)
    #print(r.json)

toc = time.perf_counter()
#print(r.status_code)
#print(r.text)
#print(r.json)

print("Itérations : " + str(i+1))
print(f"Avg call time API in {(toc - tic)/ITER:0.3f} seconds")
print(f"Total call time {(toc - tic):0.3f} seconds")



