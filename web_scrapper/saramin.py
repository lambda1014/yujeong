import requests
from bs4 import BeautifulSoup

URL = "http://www.saramin.co.kr/zf_user/search/recruit?searchType=auto&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&searchword=PYTHON&recruitPageCount="

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
        last_page = pages[-1]
    return int(last_page)
  
def extract_job(html):
    title = html.find("h2", {"class": "job_tit"}).find("a")["title"]
    company = html.find("div", {"class": "area_corp"}).find("a")["title"]
    loc = html.find("div", {"class": "job_condition"})
    location = loc.find("a").text
    job_id = html["value"]

    return {
        'title':
        title,
        'company':
        company,
        'location':
        location,
        'link':
        f"http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx={job_id}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&recruitPage={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "item_recruit"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
