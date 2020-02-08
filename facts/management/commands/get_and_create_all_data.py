from django.core.management.base import BaseCommand, CommandError
from pprint import pprint
from bs4 import BeautifulSoup
import requests
from facts.models import Facts, Song, Artist


class Command(BaseCommand):
    help = 'to make the DB first run the command m handle'

    def handle(self, *args, **options):
        Facts.objects.all().delete()
        Song.objects.all().delete()
        Artist.objects.all().delete()
        for page in range(1, 20):
            data = requests.get(f"https://www.mima.co.il/fact_page.php?song_id={page}")
            try:
                data.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print("error getting url: ", e)
            soup = BeautifulSoup(data.text, "html.parser")
            if soup.find("font", {"size": "+2"}).text != '':
                artist_name = soup.find("font", {"size": "+2"}).text
                artist, artist_created = Artist.objects.get_or_create(artist=artist_name)  ##o=artist_name,c=True/False
                song_name = soup.find("font", {"size": "+5"}).text
                song, song_created = Song.objects.get_or_create(id=page, song=song_name,
                                                                artist=artist)  ##o=song_name,c=True/False
                all_facts = soup.find_all('tr', {'bgcolor': ['#CCFFCC', '#EDF3FE']})
                for fact in range(len(all_facts)):
                    one_fact_each_time = all_facts[fact].text.strip().split('נכתב ע"י')
                    fact = one_fact_each_time[0].replace('\r\n', '')
                    try:
                        author = one_fact_each_time[1]
                    except IndexError:
                        author = ''
                    facts, facts_created = Facts.objects.get_or_create(facts=fact, song=song, author=author)
