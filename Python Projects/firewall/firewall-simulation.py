import random 

# For the purpose of the simulation, we indicate 6 IP addresses with packets that will 
# be dropped and not allowed by the firewall

firewall_rules : dict = { 
    "192.168.1.1" : "block",
    "192.168.1.4" : "block",
    "192.168.1.10" : "block",
    "192.168.1.18" : "block",
    "192.168.1.22" : "block",
    "192.168.1.24" : "block"
}

def generate_random_ip():
    return f"192.168.1.{random.randint(1,30)}"

def check_firewall_rules(ip_address,firewall_rules):
    if (ip_address in firewall_rules.keys()):
        return "block"
    else:
        return "allowed"
def main():  #Simulation data traffic through generation of 20 random IP addresses 
    for i in range(5):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address,firewall_rules)
        id = random.randint(1,9999)
        print(f"IP: {ip_address}, Action: {action}, Identifier : {id}")
        print("---------------------------------------------------------")
        
## ----------------------------------- MAIN ----------------------------------- ## 
if __name__ == "__main__":
    main()