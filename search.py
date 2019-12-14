import urllib.request as req
import bs4

def search_result(search_term):
    print('search term', search_term)
    if search_term=="" or search_term is None:
        search_term="guitar"
    searchTernWithoutSpace=" ".join(search_term.split())
    base_url="https://www.bing.com/search?q="    
    url=base_url+searchTernWithoutSpace
    print('url',url)
    try:
        request=req.Request(url, headers={
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
        })
        with req.urlopen(request) as response:
            data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        first_result=root.find("li", class_="b_algo")
        # print(root)
        print(first_result)
        first_result_title=first_result.find('h2').text
        print(first_result_title)
        first_result_link=first_result.a['href']
        print(first_result_link)
        first_result_description=first_result.find('p').text
        # first_result_description=first_result.find('p', class_="b_paractl").text
        print(first_result_description)
        news_result=first_result_title+"\n"+first_result_description+'\n'+first_result_link
        return news_result
    except:

        print('Sorry, search term not valid, please try another term')
        return('Sorry, search term not valid, please try another term')

search_result("lincoln")
search_result("paper")
search_result("unaccpetable")
search_result("桃園")