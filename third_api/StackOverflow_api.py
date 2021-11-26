import requests
from datetime import datetime
import os 


url = 'https://api.stackexchange.com/2.3/questions?'
path_to_file = os.path.join(os.getcwd(), 'questions.txt')


next_page = 1
def get_data(fromdate, todate):
    global next_page
    params = {'page':str(next_page), 'pagesize': '100',  'fromdate': fromdate, 'todate': todate, 'order': 'desc', 'sort': 'creation',
    'tagged': 'python', 'site': 'stackoverflow'}
    data = requests.get(url=url, params=params).json()
    with open(path_to_file, 'a', encoding='utf-8') as my_file:
        for item in range(len(data['items'])):
            convert_date = datetime.fromtimestamp(int(data['items'][item]['creation_date'])) 
            my_file.write(str(convert_date) + ' ' + data['items'][item]['title'] + '\n')
    if data['has_more'] == True:
        next_page +=1 
        get_data(fromdate, todate)
   

if __name__ == '__main__':
    print('''Welcome to the StackOverFlow Questions.
This function will help to get all questions with tag "Python" by date from StackOverFlow.
Please, Type date range to get txt file with questions.
*(recommended to set up date range, no more than 2 days)\n''')

fromdate = input('Please, Type From Date, Format (YYYY-MM-DD): ')
todate =  input('Please, Type To Date, Format (YYYY-MM-DD): ')
print('(Please, wait a few seconds and check "questions.txt" file to see all questions)')
get_data(fromdate, todate)
print('Successfully Data Gathered')

