import urllib.request as req
import bs4

def search_suggestion(vocab):
    url='https://dictionary.cambridge.org/spellcheck/english-chinese-traditional/?q='+vocab
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    suggestion=root.find("li", class_="lbt lp-5 lpl-20")
    suggesting_vocab=suggestion.text.replace('\n','')
    return(suggesting_vocab)
    # suggestion_link=suggestion.a['href']
    # print(suggestion_link)
    # dictionary_result(suggesting_vocab)

def dictionary_result(vocab):
    base_url="https://dictionary.cambridge.org/dictionary/english-chinese-traditional/"
    if vocab=="":
        return('No result, please try another word')
    vocab=vocab.replace(' ','-')
    url=base_url+vocab
    try:
        request=req.Request(url, headers={
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
        })
        print(url)
        with req.urlopen(request) as response:
            data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        try:
            first_result=root.find("div", class_="def ddef_d db").text
            return (f'{vocab}: {first_result}')
        except:
            result='Do you mean "'+search_suggestion(vocab)+'" ?\n'+dictionary_result(search_suggestion(vocab))
            return result
    except:
        return('No result, please try another search')
        
# print(dictionary_result('pathetic'))
# print(dictionary_result('ubiqutous'))
