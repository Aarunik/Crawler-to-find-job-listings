from bs4 import BeautifulSoup
import requests

print('Enter the company name that you want to search jobs for: ')
company_name = input()
print('You have entered:', company_name)

url_txt = requests.get("https://www.iimjobs.com/search/gartner-0-0-0-1.html").content
soap = BeautifulSoup(url_txt, 'html.parser')

jobs = soap.find_all('div', class_='unfollowopt jobRow container table table-hover pdlr0 greybg')
for job in jobs:
    job_name = job.find('a', class_='mrmob5 hidden-xs').text
    if company_name.lower() in job_name.lower():
        job_location = job.find('div', class_='col-lg-7 col-md-7 col-sm-7 ellipsis pdlr0 pdmobl5').span.text
        posted_on = job.find('span', class_='gry_txt txt12 original').text
        job_url = job.find('a', class_='mrmob5 hidden-xs')['href']
        print(job_name, job_location, posted_on, job_url)
