import textwrap
ip=input("Enter the IP address : ")
x=ip.split("/")
ip_add=x[0]
num_network_bits=int(x[1])
num_host_bits=32-num_network_bits

ip_split=ip_add.split('.')
ip_split_class=int(ip_split[0])
bin_ip_split=[]
for i in ip_split:
    bin_ip_split.append(format(int(i),'08b'))   
bin_ip=''.join(bin_ip_split)

def bin_to_dotted_decimal(val):
    seg_ip=textwrap.wrap(val,8)
    val_ip_split=[]
    for j in seg_ip:
        val_ip_split.append(int(j,2))
    val_ip='.'.join(map(str,val_ip_split))
    return val_ip  

def network_id(bin_ip,num_network_bits,num_host_bits):
    lhs=bin_ip[:num_network_bits]
    rhs='0'*num_host_bits
    val=lhs+rhs
    print("Network ID : "+bin_to_dotted_decimal(val)+"/"+str(num_network_bits))
    
def direct_broadcast_address(bin_ip,num_network_bits,num_host_bits):
    lhs=bin_ip[:num_network_bits]
    rhs='1'*num_host_bits
    val=lhs+rhs
    print("Direct Broadcast ID : "+bin_to_dotted_decimal(val)+"/"+str(num_network_bits))  

def num_address(num_host_bits):
    print("Number of IP Addresses : "+str(pow(2,num_host_bits)))    
    
i=0
while i<=2:
    n=int(input("Enter 1 to display the first IP Address in the block\nEnter 2 to display the last IP Address in the block\nEnter 3 to display the total number of address in the block\nCHOICE : "))

    if n==1:   
        network_id(bin_ip,num_network_bits,num_host_bits)
    elif n==2:
        direct_broadcast_address(bin_ip, num_network_bits, num_host_bits)
    else:
        num_address(num_host_bits)
    
    i=i+1

    
    