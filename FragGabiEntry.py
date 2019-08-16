from Question import Question
import requests
from bs4 import BeautifulSoup


class FragGabiEntry:
    """
    Scraper for the Frag Gabi Section on maedchen.de
    """
    answer = str()
    question = Question()

    def __init__(self, url):
        """
        On object creation directly initiate scraping of given site
        :param url: URL to a question on maedchen.de (Format like https://www.maedchen.de/love/frag-gabi/<something>)
        """
        self.scrape_site(url)

    def scrape_site(self, url):
        """
        Request site and extract contents
        :param url: URL to a question on maedchen.de (Format like https://www.maedchen.de/love/frag-gabi/<something>)
        :return: True on success
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        question_content_raw = soup.find_all(class_='question-detail')[0].get_text().strip()
        self.question.content = question_content_raw.split('\n\n\n')[0].strip()
        self.question.title = soup.find_all(class_='question-header')[0].get_text().strip()
        author_date = question_content_raw.split('\n\n\n')[1].strip()[4:].split(' / ')
        self.question.author = author_date[0]
        self.question.set_date(author_date[1])
        self.answer = soup.find_all(class_='question-answers__content--expert')[0].get_text(separator='\n')
        return True
