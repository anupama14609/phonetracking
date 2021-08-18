from django.shortcuts import render
import phonenumbers 
from phonenumbers import geocoder, carrier
from phonenumbers import timezone
from phonenumbers.phonenumberutil import NumberParseException
import requests
from bs4 import BeautifulSoup
import lxml


# def get_html_content(request):
#     phoneNumber = request.GET.get('phone')
#     session = requests.Session()
#     url = 'https://www.compart.com/en/unicode/U+002B'
#     symbol = session.get(url).text
#     soup = BeautifulSoup(symbol, 'html.parser')

#     num = symbol+phoneNumber   
#     print(symbol)

def home(request):    
    result = None
    numdict = dict()
    phoneNumber = request.GET.get('phone')
    url = 'https://www.compart.com/en/unicode/U+002B'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    symbol = soup.find('span', attrs={'class':'box'}).text
    print(phoneNumber)
    print(symbol)
    numdict['cc'] = str(symbol)
    numdict['nmbr'] = str(phoneNumber)
    print(numdict)
    tracknum = numdict['cc'] + numdict['nmbr']
    tracknum = str(numdict['cc'])+ str(numdict['nmbr'])
    print(tracknum)

    context = {
        'results':numdict
        }
    return render(request, 'trackphone/home.html',context)

