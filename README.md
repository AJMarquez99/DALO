# DALO

DALO is an ambitious project to gather date on, analyze, and predict the stock market using automation, machine learning, and complex formulas. It will allow us to analyze and make prediction on hundreds, to thousands, of companies on the stock market all at once versus an individual view a maximum of a view tens of companies' stocks.

## Technologies Needed:

### To Contribute:

A few things need to be on your computer in order to join and contribute to this project:

- Python 3.5 or newer
- A text editor
- Git installed wherever you're working on this
- Programming Knowledge
- Faith in the project

### For the Project Itself:

The project itself will use a few different programming technologies to allow it to run smoothly, here they are laid out:

- Python 3.5 or newer (Modules following)
  - os
  - shutil
  - datetime
  - csv
  - time
  - sys
  - OpenPyXL
  - Selenium
  - PyMongo
  - SciPy
  - NumPy
  - Matplotlib
  - Django
  - MySqlClient
  - Virtualenv
- HTML5
- CSS3
- SASS (CSS Preprocessor)
- JS (ES5)
- AJAX

## Project Plan:

DALO is quite the project, like stated, super ambitious but if it works it's guaranteed money for anyone involved so here is the plan.

1. Design the backend system thoroughly
    - This is the bread and butter of DALO.
    - Will need to use calculus and statistics to be properly automated.
2. Fine tune analysis formulas
    - The formulas will be what decide whether a stock is worth the risk, this is of utmost importance.
3. Create a system to pull and rank articles based on keywords attached to each company's stock data.
    - This will be utilized in conjunction with the formulas to better predict a stock's movement.
4. Create and populate the DALO database using Mongo
5. Design a front-end interface
    - Must be beautiful and innovative above all else.
    - User-friendly is second to the overall look and feel of the site.
      - New and cool things can be scary at first but if its impressionable then you'll adapt to it.
    - Design must not affect load-time too much
6. Create and program backend system following design
    - Load time is of utmost importance here.
7. Test formulas and analysis without front-end to verify the success rate.
8. Create front-end following design
    - Must be dynamic
9. Testing, testing, and more testing
    - Make sure the front-end and back-end work in perfect unison
    - Offer it to a few people to see how it handles
10. Open it up to the world.

## Structure:

The project will take a bit of time in order to be done correctly but here is the structure so far.

### Data Scraper Class
- Takes String Array input
- Gathers up to 5 years of historical data per company
  - Main data source for market analysis
- Grabs hourly price for each company
  - Stores data for a week, not used in general data analysis

### Event Scraper Class
- Will search Google, Bing, Yahoo, etc for articles
  - Articles will be searched based on keywords
  - Articles will be attached to companies based on their assigned keywords
- Articles will be given a rating based on content of article
  - If article remains neutral, rating can be assigned manually
- Should be running every hour at least
- Article link should only be stored for a maximum of 3 weeks (up for debate)

### Data Management Class
- Can move downloaded CSV data to proper folder
- Converts CSV into Excel for easier data manipulation
  - May be skipped it CSV parser is quicker or easier
- Can delete CSV and Excel files
- Transfers data from Excel to Mongo database
- Can update Monga Database based on parsed Excel data

### Data Manipulation Class
- Will grab data from Mongo Database
- Will run formulas on data such as ( but not limited to ):
  - Finding Standard Deviation of market stock value over a period of time
  - Finding volatility of stock market value over a period of time
  - Finding peaks and troughs from where to begin trend lines
    - Will be found using the 1st and 2nd derivatives of the original graph
  - Deciding whether linear, exponential, or polynomial trend lines are better suited
  - Will use machine learning, multiple trend lines, volatility, and news ranking system to predict stock market value.

### Data Visualization Class
- Will create different graphs for:
  - Regular stock market value
  - Volatility
  - Rate of Change
  - Standard Deviation
  - Prediction Value(s)
- Will allow interactivity on graphs
- Will create graph which allows custom data
  - Will allow for profit/loss predictions based on user inputted data

### Information Communication Class
- Will send text alerts based on:
  - Stock volatility on the rise
  - Stock hits desired price
  - Sharp incline/decline in stock value
  - News events for stocks on watchlist
- Will create emails with useful and concise information on market
  - Users can decide what is included in the email

### AJAX Communicator Class
- Interface to allow easy and quick JS calls to Python
