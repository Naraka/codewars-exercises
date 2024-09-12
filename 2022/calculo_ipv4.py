# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246





def ips_between(start, end):
    ssplit=start.split(".")
    esplit=end.split(".")


    a=(int(ssplit[0])*255)+int(ssplit[0])+int(ssplit[1])
    b=(a*255)+int(ssplit[2])+a
    c=(b*255)+int(ssplit[3])+b
    
    x=(int(esplit[0])*255)+int(esplit[0])+int(esplit[1])
    y=(x*255)+int(esplit[2])+x
    z=(y*255)+int(esplit[3])+y
    
    print(z-c)














s="20.0.0.10"               
e="20.0.1.0"                
s1="188.119.11.107"
e1="188.133.252.131" 

ips_between(start=s,end=e) #246
ips_between(start=s1,end=e1)#979224













