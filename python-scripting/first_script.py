favorite_movies =[
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    }
]

# Printing out favorite movie
print(favorite_movies)

# 1.) Printing out the total number of favorite movies
total_favorite_movies = len(favorite_movies)
print("How many total favorite movies do we have?", total_favorite_movies)

# 2.) Printing out the first favorite movie
print(type(favorite_movies), type(favorite_movies[0]))
print('Enter your favorite movie from the last year:')
# 3.) What the user's favorite movie is from last year
recent_favorite_movie = input()
print('Your favorite movie from the last year is:', recent_favorite_movie)

# STRINGS

# 1.) Adding a long description to the first favorite movie
favorite_movies[0]['long_description'] = "The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano. The Wachowskis created a plot set in a dystopian future where humanity is unknowingly trapped inside a simulated reality, the Matrix, created by intelligent machines to distract humans while using their bodies as an energy source. In the movie, the main character, Neo, is a computer programmer who learns this truth and is drawn into a rebellion against the machines, which involves other people who have been freed from the Matrix."
print(favorite_movies[0])

# Splitting the long description into a list of words
split_description = favorite_movies[0]['long_description'].split(' ')
print(split_description)
print(len(split_description))

# 2.) Joining the list of words back into a single string
print(' '.join(split_description))

# 3.) Replacing "the Wachowskis" with "Lana and Lilly Wachowski" in the long description
edited_description = favorite_movies[0]['long_description'].replace('the Wachowskis', 'Lana and Lilly Wachowski')
print(edited_description)

# Replacing only the first occurrence of "the Wachowskis" with "Lana and Lilly Wachowski" in the long description
edited_description = favorite_movies[0]['long_description'].replace('the Wachowskis', 'Lana and Lilly Wachowski', 1)
print(edited_description)

# 4.) Using string methods to manipulate the long description
print(favorite_movies[0]['long_description'].lower())
print(favorite_movies[0]['long_description'].upper())
print(favorite_movies[0]['long_description'].title())
print(favorite_movies[0]['long_description'].strip()) 