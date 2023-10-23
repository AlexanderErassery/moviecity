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

            # Constructing the URL for the poster
            base_image_url = "https://image.tmdb.org/t/p/"
            image_size = "w500"
            poster_url = base_image_url + image_size + movie['poster_path']
            print(f"Poster URL: {poster_url}")

            # Fetching actor details
            movie_id = movie['id']
            credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}"
            credits_response = requests.get(credits_url)

            if credits_response.status_code == 200:
                credits_data = credits_response.json()
                cast = credits_data['cast']

                # Extract and print names of the first few actors
                actor_names = [actor['name'] for actor in cast[:5]]
                print(f"Actors: {', '.join(actor_names)}")
            else:
                print("Failed to retrieve actor details!")

        else:
            print("No movies found!")
    else:
        print("Failed to retrieve data!")

if __name__ == "__main__":
    # Note: Replace YOUR_API_KEY with the actual API key
    # Get api_key by registering on https://www.themoviedb.org/login
    api_key = "YOUR_API_KEY"
    
    # Get the movie name from the user
    movie_name = input("Enter the name of the movie: ")
    
    # Fetch and display the movie details
    get_movie_details(movie_name, api_key)
