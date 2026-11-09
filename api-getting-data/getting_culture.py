import requests
import json

try:
    # Getting the show Arcane from the TVmaze API
    response = requests.get(
        "https://api.tvmaze.com/singlesearch/shows",
        params={"q": "Arcane"}, timeout=15)

    if response.status_code == 200:
        show = response.json()
        print(show)
        with open("tvmaze_show.json", "w") as file:
            json.dump(show, file, indent=4)
    
        # Search Wikipedia using the show's name
        wiki_response = requests.get(
            "https://en.wikipedia.org/w/api.php",
            params={
                "action": "query",
                "format": "json",
                "list": "search",
                "srsearch": show["name"],
                "srlimit": 3},
            headers={"User-Agent": "IS310-Homework/1.0 (https://github.com/Jaylin2436chen)"},
            timeout=15)

        if wiki_response.status_code == 200:
            wiki_data = wiki_response.json()
            print(wiki_data["query"]["search"])
            with open("mediawiki_search.json", "w") as file:
                json.dump(wiki_data["query"]["search"], file, indent=4)
        else:
            print("Wikipedia error:", wiki_response.status_code)
    else:
        print("TVmaze error:", response.status_code)

except requests.exceptions.RequestException:
    print("Not responding.")
except ValueError:
    print("The response was not a valid JSON.")