# IS390 API Getting Data

## About:

For this assignment I used TVmaze and Wikipedia's MediaWiki Action API to find the television series Arcane. I chose TVmaze and this specifically because I wanted to explore information about a show I really like.

## Comparison:

For this assignment, both TVmaze and Wikipedia did not require an account or API key to work, however I did use a descriptive User-Agent for my script. This allowed for basic lookups while allowing Wikipedia to identify automated users. TVmaze also allows at least 20 requests every 10 seconds per IP address, while Wikimedia currently lists 200 requests per minute for unauthenticated scripts with a compliant User-Agent, which does limit the repeated lookups. After running the code both of my APIs returned JSON, but TVmaze’s summary and Wikipedia’s search does contained HTML a bit. TVmaze made it easy to retrieve a show’s genres, language, and release dates, while Wikipedia returned the show’s article and two soundtrack articles, so I had to check which one was for what exactly. TVmaze does offer paid subscriptions and API plans, but Wikipedia is ran by a nonprofit Wikimedia Foundation and funded mainly through donations. If either one of these service shut down or restricted information access, this would make collecting data much more difficult. Overall, while this did work on a very big television show like Arcane, this does not show how well it might work on smaller shows. One thing that limits the search still is the English Wikipedia usage which would only search for English languaged articles. This connects to Acker, Kreisberg, and Freelon because researchers depend on APIs to gather information but they can't control what information they are able to collect through availability and access

## Data Files:

- `getting_culture.py`: Gathers the data and saved them from both of my APIs.
- `tvmaze_show.json`: Information collected about Arcane from TVmaze.
- `mediawiki_search.json`: Wikipedia search results.

## How To Run The Code:

Install :

python3 -m pip install requests

python3 getting_culture.py