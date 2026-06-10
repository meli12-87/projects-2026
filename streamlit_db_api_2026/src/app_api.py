import requests

def get_movie_Info_By_ID(movie_id):
    url= f"http://moviesapi.ir/api/v1/movies/{movie_id}"

    response = requests.get(url)
    if response.status_code != 200:
        return 'ERROR'

    else:
        response = response.json()
        movie_name = response['title']
        country = response['country']
        year = response['year']
        rate = response['imdb_rating']

        return (movie_name, country, year, rate)
    
if __name__ == "__main__":
    movie_id = input('enter movie by id:')
    result = get_movie_Info_By_ID(movie_id)
    print(f'result : {result}')


