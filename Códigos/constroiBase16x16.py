import yaml
import os.path

injection_rate = []
traffic = []
latency = []
received_packets = []
routers = []

for gen in range(10):
    for file in range(1000):
        if(os.path.isfile('gen'+str(gen)+'/'+str(file)+'.yaml')):
            base = yaml.load(open('gen'+str(gen)+'/'+str(file)+'.yaml'))
            results = open('gen'+str(gen)+'/'+str(file)+'.txt', 'r')
        
            injection_rate.append(base['packet_injection_rate'])

            if(base['traffic_distribution'] == "TRAFFIC_BUTTERFLY"):
                traffic.append(1)
            elif(base['traffic_distribution'] == "TRAFFIC_RANDOM"):
                traffic.append(2)

            elif(base['traffic_distribution'] == "TRAFFIC_SHUFFLE"):
                traffic.append(3)

            router = []
            
            for i in range(64):
                router.append(base['Hubs'][i]['attached_nodes'])

            routers.append(router)

            for linha in results:
                if "Global" in linha.strip().split():
                    latency.append(linha.strip().split()[5])
                if "packets:" in linha.strip().split():
                    received_packets.append(linha.strip().split()[4])

            results.close()

csv_latency = open('../16x16_latency_train.csv', 'a')
for i in range(len(traffic)):
    csv_latency.write(str(injection_rate[i]) + "," + str(traffic[i]) + ",")
    for j in range(64):
        csv_latency.write(str(routers[i][j][0]) + "," + str(routers[i][j][1]) + "," +
              str(routers[i][j][2]) + "," + str(routers[i][j][3]) + ",")
    csv_latency.write(str(latency[i])  + " \n")

csv_latency.close()

csv_packets = open('../16x16_packets_train.csv', 'a')
for i in range(len(traffic)):
    csv_packets.write(str(injection_rate[i]) + "," + str(traffic[i]) + ",")
    for j in range(64):
        csv_packets.write(str(routers[i][j][0]) + "," + str(routers[i][j][1]) + "," +
              str(routers[i][j][2]) + "," + str(routers[i][j][3]) + ",")
    csv_packets.write(str(received_packets[i])  + "\n")

csv_packets.close()

