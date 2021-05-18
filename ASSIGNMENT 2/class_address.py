ip_address=input("Enter the IP ADDRESS : ")
split_ip_address=ip_address.split('.')
ip=int(split_ip_address[0])
if ip>= 1 and ip<=126:
    print("Given IP belongs to Class A")
    print("Network Address : "+split_ip_address[0])
elif ip>=128 and ip<=191:
    print("Given IP belongs to Class B")
    print("Network Address : "+split_ip_address[0]+'.'+split_ip_address[1])
elif ip>=192 and ip<=223:
    print("Given IP belongs to Class C")
    print("Network Address : "+split_ip_address[0]+'.'+split_ip_address[1]+'.'+split_ip_address[2])
elif ip>=224 and ip<=239:
    print("Given IP belongs to Class D")
    print("In this Class, IP address is not divided into Network address")
else:
    print("Given IP belongs to Class E")
    print("In this Class, IP address is not divided into Network address")
    
