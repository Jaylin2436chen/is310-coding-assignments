from rich.console import Console
from rich.table import Table
import json
import os

console = Console()
console.print("Here is some initial data:", style="bold cyan")

table = Table(title = "Artist Songs")
table.add_column("Artist", style="cyan", no_wrap=True)
table.add_column("Song Name", style="magenta")
table.add_column("Release Year", justify="right", style="green")

table.add_row("Tame Impala", "Let It Happen", "2015")
table.add_row("Vacations", "Moving Out", "2018")
table.add_row("Travis Scot", "Velour", "2025")
table.add_row("Don Toliver", "Sweet Home", "2026")
table.add_row("Don Toliver", "ATM", "2026")
table.add_row("Don Toliver", "OPPOSITE", "2026")
table.add_row("No Vacation", "Changes", "2019")

console.print(table)
console.print("\n[bold yellow]You can now add your own artist, song name, and its release year: [/bold yellow]")

number_of_songs = int(input("How many songs would you like to add? Enter 1 or more: "))

while number_of_songs < 1:
    print("Please enter at least 1 song.")
    number_of_songs = int(input("How many songs would you like to add? "))

songs = []

for number in range(number_of_songs):
    while True:
        print(f"\nSong {number + 1}")

        song_name = input("Enter the song name: ")
        artist_name = input("Enter the artist name: ")
        release_year = input("Enter the release year: ")

        print("\nYour entry:")
        print("Artist:", artist_name)
        print("Song:", song_name)
        print("Release year:", release_year)

        answer = input("Is this entry correct? (yes/no): ").lower()

        if answer == "yes":
            song = {
                "artist": artist_name,
                "song_name": song_name,
                "release_year": release_year
            }
            songs.append(song)
            break
        else:
            print("Please enter the song again.")

file_name = "python-libraries/artist_songs.json"

with open(file_name, "w") as file:
    json.dump(songs, file, indent=2)

console.print(f"\n[bold green]Your data was saved to:[/bold green]")
console.print(os.path.abspath(file_name))