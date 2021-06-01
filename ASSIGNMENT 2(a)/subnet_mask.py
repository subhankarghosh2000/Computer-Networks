import math
import itertools
import textwrap
ip=input("Enter the IP ADDRESS : ")
n_subnet=int(input("Enter the number of subnets : "))
fixed_bits=int(math.ceil(math.log(n_subnet)/math.log(2)))
ip_split=ip.split('.')
ip_split_class=int(ip_split[0])
bin_ip_split=[]
for i in ip_split:
    bin_ip_split.append(format(int(i),'08b'))   
bin_ip=''.join(bin_ip_split)
combinations=list(map(list, itertools.product([0, 1], repeat=fixed_bits)))

def Nclass(a,bin_ip,fixed_bits,combinations,out,b):
    lhs=bin_ip[:a]
    rhs='0'*(32-fixed_bits-a)
    out.write(f'Class {b}\n')
    for i,c in enumerate(combinations,1):
        val=lhs+''.join(map(str,c))+rhs
        seg_ip=textwrap.wrap(val,8)
        req_ip='.'.join(seg_ip)
        val_split=req_ip.split('.')
        val_ip_split=[]
        for j in val_split:
            val_ip_split.append(int(j,2))
        val_ip='.'.join(map(str,val_ip_split))
        out.write(f'Subnet {i} ID : {val_ip}\n')
               
def subnet_mask(a,fixed_bits,out,b):
    s_lhs='1'*a
    fixed='1'*fixed_bits
    s_rhs='0'*(32-fixed_bits-a)
    mask=s_lhs+fixed+s_rhs
    seg_mask_ip=textwrap.wrap(mask,8)
    req_mask_ip='.'.join(seg_mask_ip)
    mask_split=req_mask_ip.split('.')
    mask_ip_split=[]
    for i in mask_split:
        mask_ip_split.append(int(i,2))
    mask_ip='.'.join(map(str,mask_ip_split))
    out.write(f'Subnet Mask : {mask_ip}\n')
           
out=open("Output4.txt",'w')  

if ip_split_class>=1 and ip_split_class<=126:
    Nclass(8,bin_ip,fixed_bits,combinations,out,'A')
    subnet_mask(8,fixed_bits,out,'A')
elif ip_split_class>=128 and ip_split_class<=191:
    Nclass(16,bin_ip,fixed_bits,combinations,out,'B')
    subnet_mask(16,fixed_bits,out,'B')
elif ip_split_class>=192 and ip_split_class<=223:
    Nclass(24,bin_ip,fixed_bits,combinations,out,'C')
    subnet_mask(24,fixed_bits,out,'C')
else:
    print("Subnet Mask and Subnetworking are not possible in Class D and Class E network address")
    
     
out.close()   
