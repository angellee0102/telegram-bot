import urllib.request as req
import bs4
import yfinance as yf
import json
def tickerValidation(ticker):
    # https://stackoverflow.com/questions/32899143/yahoo-finance-api-stock-ticker-lookup-only-allowing-exact-match/32943831#32943831  
    url='http://d.yimg.com/aq/autoc?query='+ticker+'&region=US&lang=en-US'
    request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    obj = json.loads(data)
    if len(obj['ResultSet']['Result'])==0:
        return('NO TICKER')

def stock_result(stock_ticker):
    if stock_ticker == "" or stock_ticker is None:
        stock='MMM'
    stock=" ".join(stock_ticker.split())
    tickerValidation(stock)
    # print('\nStock', stock)
    if tickerValidation(stock)!='NO TICKER':
        target = yf.Ticker(stock)
        try:
            # print(target.info)
            return('Ticker: '+stock+'\nPrevious Close: '+str(target.info['previousClose'])+
            '\nDay High: '+str(target.info['dayHigh'])+
            '\nDay Low: '+str(target.info['dayLow'])+
            '\n52 Week Change: '+str(100*target.info['52WeekChange'])[:5]+'%')
        except:
            return ('TICKER not valid')
    else:
        return ('TICKER not valid')
# print(stock_result('aapl'))
# stock_result('mmm')
# stock_result('goog')
# stock_result('tsmc')
# stock_result('2330.TW')
# stock_result('hahah')