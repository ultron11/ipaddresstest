ip = input("Saisir une adresse IPv4 valide : ")

ip1 = ip.split(sep=".")

ip2 = []

ok = 0

if len(ip1) == 4 : 

    for octet in ip1 : 

        while True:
            try:
                ip2.append(int(octet))
                break
            except ValueError:
                print("Oops!  L'octet contient de valeurs qui ne.  Try again...")
                
                ip = input("Ressaisir une adresse IPv4 valide : ")
  
                ip3 = ip.split(sep=".")

                

                if len(ip3) == 4 :

                    ip4 = []
                    ip2 = []

                    for octet in ip3 :

                        ip4.append(int(octet))

                break
if ip2 != 4 :

    ip2 = ip4

#for octet in ip2 :

#    if octet >= 0 and octet <= 255 :

#        ok = ok + 1 

#if ok == 4 :

#    print("L'adresse ip est valide")

#else :

#    print("L'adresse ip est non  valide")

print(ip2)
