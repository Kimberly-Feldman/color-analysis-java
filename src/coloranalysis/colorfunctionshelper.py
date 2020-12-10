import urllib.request, json

#returns palette dictionary of hosted jpg 
def imgix_json (user_url):

    url_extension = "?w=640&h=320&fit=crop&palette=json"
    url = user_url+url_extension
    data = ""

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

    colors = data["colors"]


    return colors


