# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"




def domain_name(url):
    url = url.replace('www.','').replace('https://','').replace('http://','')
    
    print(url[0:url.find('.')])  # desde la posicion 0 hasta que encuente el "."




    

    
domain_name("http://google.co.jp")
domain_name("https://youtube.com")
domain_name("www.xakep.ru")
domain_name("http://google.com")









