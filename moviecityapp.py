import requests
import json

def get_movie_details(movie_name, api_key):
    # TMDb API endpoint to search for movies
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"
    
    # Make the API request
    response = requests.get(search_url)
    
    # Check the response status code
    if response.status_code == 200:
        # Convert the response to JSON
        data = response.json()
        
        # Check if any movies were found
        if data['total_results'] > 0:
            # Extract and print details of the first found movie
            movie = data['results'][0]
            print(f"Title: {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            print(f"Overview: {movie['overview']}")
            print(f"Vote Average: {movie['vote_average']}")
            print(f"Popularity: {movie['popularity']}")
            print(f"Adult: {movie['adult']}")

        else:
            print("No movies found!")
    else:
        print("Failed to retrieve data!")

if __name__ == "__main__":
    # Note: Replace YOUR_API_KEY with the actual API key
    api_key = "7a4ae0188eaa7ed525756d2fad046aa1"
    
    # Get the movie name from the user
    movie_name = input("Enter the name of the movie: ")
    
    # Fetch and display the movie details
    get_movie_details(movie_name, api_key)
