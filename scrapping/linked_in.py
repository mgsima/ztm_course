import requests
from bs4 import BeautifulSoup

link = 'https://www.linkedin.com/jobs/search/?currentJobId=3582103520&distance=25&geoId=101282230&keywords=Desarrollador%20de%20Python&refresh=true'
res = requests.get(link)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.body)