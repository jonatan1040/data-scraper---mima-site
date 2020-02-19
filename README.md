# MyMima!

By Jonatan Menachem.


## Requirements
* Python 3.7 or 3.8
* pipenv

## Setup Instructions
* Clone the project
* `cd` into your peoject.
* Run:

        pipenv install
        pipenv shell
* Next, Run (will get all data from mima site and put it into DB):

        m get_and_create_all_data

## RUNNING THE SERVER

        python manage.py runserver

## artist page (all artist songs) is at this url:
http://127.0.0.1:8000/artist/400/

## song page (by the first letter of a song) is at this url:
http://127.0.0.1:8000/song/1000/

## fact page (facts about a specific song) is at this url:
http://127.0.0.1:8000/fact/73/

## REVERSE ENGINEERING
Homepage:
https://www.mima.co.il/

artist page:
shows all artist by letter choosen
https://www.mima.co.il/artist_letter.php?let=%D7%9B

artist page:
show all songs of artist
https://www.mima.co.il/artist_page.php?artist_id=149

facts of song of specific artist:
show all facts about the song related to a specific artist/song
https://www.mima.co.il/fact_page.php?song_id=529

all songs of specific letter:
show all songs start with the letter
https://www.mima.co.il/song_letter.php?let=%D7%96

one 2 many artist to song
one 2 many facts to songs

screenshoots:
## artist page
![mima scraper](https://github.com/jonatan1040/data-scraper---mima-site/blob/master/screenshoot_artist.png)

## song page
![mima scraper](https://github.com/jonatan1040/data-scraper---mima-site/blob/master/screenshoot_song.png)

## facts page
![mima scraper](https://github.com/jonatan1040/data-scraper---mima-site/blob/master/screenshoot_facts.png)
