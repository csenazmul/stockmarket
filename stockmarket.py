6. Django Admin Area

# > python manage.py makemigrations
# > python manage.py migrate

# $ python manage.py createsuperuser

# $ winpty python manage.py createsuperuser

# $ pip install requests

# $ pip install json

'''
{'symbol': 'AAPL', 'companyName': 'Apple, Inc.', 'primaryExchange': 'NASDAQ', 'calculationPrice': 'tops', 'open': None, 'openTime': None, 'close': None, 'closeTime': None, 'high': None, 'low': None, 'latestPrice': 279.1, 'latestSource': 'IEX real time price', 'latestTime': '9:39:56 AM', 'latestUpdate': 1583159996633, 'latestVolume': None, 'iexRealtimePrice': 279.1, 'iexRealtimeSize': 100, 'iexLastUpdated': 1583159996633, 'delayedPrice': None, 'delayedPriceTime': None, 'oddLotDelayedPrice': None, 'oddLotDelayedPriceTime': None, 'extendedPrice': None, 'extendedChange': None, 'extendedChangePercent': None, 'extendedPriceTime': None, 'previousClose': 273.36, 'previousVolume': 106721230, 'change': 5.74, 'changePercent': 0.021, 'volume': None, 'iexMarketPercent': 0.017722187898996974, 'iexVolume': 140385, 'avgTotalVolume': 38319408, 'iexBidPrice': 275.1, 'iexBidSize': 100, 'iexAskPrice': 288, 'iexAskSize': 200, 'marketCap': 1221196468000, 'peRatio': 21.88, 'week52High': 327.85, 'week52Low': 169.5, 'ytdChange': -0.0562, 'lastTradeTime': 1583159996633, 'isUSMarketOpen': True}
'''


def home(request):
    
    import requests
    import json
    #pk_2129cb94cb934897a82b46f2256f5154
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_2129cb94cb934897a82b46f2256f5154")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})

################### End ##############

# {% if api %}
#     {% if api == "Error..." %}
#       There was a problem with your ticker symbol,
#       please try again...
#     {% else %}
        
#         {% for key, value in api.items  %}
#                 {{ key }}:{{ value }} <br>
#         {% endfor %}

#     {% endif %}
    
# {% endif %}


# 13. Form Part 2
# quotes>views.py
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=pk_2129cb94cb934897a82b46f2256f5154")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api':api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above" })

# 15. Add Stock Page
# Create add_stock.html file

#16. Stock Class Model
class Stock(models.Model):
    ticker = models.CharField(max_length = 10)

    def __str__(self):
        return self.ticker
    
#admin.py
from .models import Stock
# Register your models here.

admin.site.register(Stock)

# views.py
def add_stock(request):
    tricker = Stock.objects.all() #update new
    return render(request, 'add_stock.html', {'tricker':tricker})

# $Add stock
# {% extends 'base.html' %}

# {% block homepage %}
# <h1>Add Stock....</h1>   
# {{tricker}} <br>
# {% for item in tricker %}
#     {{item}} <br>
# {% endfor %}

# {% endblock homepage %}






{% if messages %}
          {% for message in messages  %}
            <div class="alert alert-success alert-dismissible fade show" role="alert">
              {{message}}
              <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
          {% endfor %}
{% endif %}



{% for item in tricker %}

    {{item}} | <a href="{% url 'delete' item.id %}">Delete Stock</a> {{item.id}}  <br>

{% endfor %}




# 27. API Output To Screen
#views.py
def add_stock(request):
    import requests
    import json


    if request.method == 'POST':
        form = StockForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has Been Added"))
            return redirect('add_stock')
    
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_2129cb94cb934897a82b46f2256f5154")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."

        return render(request, 'add_stock.html', {'ticker':ticker, 'output':output})

#add_stock.html
{% for list_item in output  %}
      {{list_item}} <br> <br>
{% endfor %}

#####################
###add_stock.html
{% extends 'base.html' %}

{% block homepage %}


<h1>Add Stock....</h1>   

<form action="{% url 'add_stock' %}" method="POST" class="form-inline my-2 my-lg-0">
    {% csrf_token %}
  <input class="form-control mr-sm-2" type="search" placeholder="Get Stock Quote" aria-label="Search" name="ticker">
  <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Stock Quote</button>
</form>



<br>
<table class="table table-striped table-bordered table-hover">
    <thead class="thead-dark">
      <tr>
        <th scope="col">#</th>
        <th scope="col">Company Name</th>
        <th scope="col">Stock Price</th>
        <th scope="col">Previous Close</th>
        <th scope="col">Market Cap</th>
        <th scope="col">YTD Change</th>
        <th scope="col">52Wk High</th>
        <th scope="col">52Wk Low</th>
        <th scope="col">Delete Stock</th>
      </tr>
    </thead>
    <tbody>
      
      {% if ticker %}
          {% for item in ticker %}
              <tr>
                  <th scope="row">{{item.id}}</th>
                  <td>{{item}}</td>
                  <td>@mdo</td>
                  <td>@mdo</td>
                  <td>@mdo</td>
                  <td>@mdo</td>
                  <td>@mdo</td>
                  <td>@mdo</td>
                  <td><a href="{% url 'delete' item.id %}">Delete Stock</a> </td>
              </tr>
          {% endfor %}
        {% endif %}
    </tbody>
  </table>
  
{% for list_item in output  %}
      {{list_item}} <br> 
{% endfor %}

  {% endblock homepage %}

#####################End of #############
<table class="table table-striped table-bordered table-hover">
    <thead class="thead-dark">
      <tr>
        <th scope="col">Company Name</th>
        <th scope="col">Stock Price</th>
        <th scope="col">Previous Close</th>
        <th scope="col">Market Cap</th>
        <th scope="col">YTD Change</th>
        <th scope="col">52Wk High</th>
        <th scope="col">52Wk Low</th>
        <th scope="col">Delete Stock</th>
      </tr>
    </thead>
    <tbody>
      {% if ticker %}
          {% for list_item in output %}
              <tr>
                  <td>{{list_item.companyName}}</td>
                  <td>${{list_item.latestPrice}}</td>
                  <td>${{list_item.previousClose}}</td>
                  <td>${{list_item.marketCap}}</td>
                  <td>{{list_item.ytdChange}}</td>
                  <td>${{list_item.week52High}}</td>
                  <td>${{list_item.week52Low}}</td>
                  <td><a href="/">Delete Stock</a> </td>
              </tr>
          {% endfor %}
        {% endif %}
    </tbody>
  </table>

# AWS, GCP, Heroku, and Digital Ocean, etc.


# 1. SSH Keys 
 $ cd ~/
 $ pwd
/c/Users/IT-2

$ mkdir .ssh

$ cd .ssh

$ ssh-keygen.exe

$ ls

$ cat id_rsa.pub

# 1. Version Control With Git
#  $ git config --global user.name "Nazmul Sheikh"
# $ git config --global user.email "csenazmul77@gmail.com"

# git hub repository 
# echo "# stockmarket" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin git@github.com:csenazmul/stockmarket.git
# git push -u origin master

# …or push an existing repository from the command line
# git remote add origin git@github.com:csenazmul/stockmarket.git
# git push -u origin master

# Create .gitignore file
# pip freeze > requirements.txt





$ cat ~/.ssh/id_rsa.pub