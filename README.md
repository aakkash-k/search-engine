# search-engine

This is a simple search engine built on a REST API using Python Flask. It allows users to search for specific keywords within a collection of documents and retrieve relevant results.

## Features

- Keyword-based search: Users can enter keywords to search for relevant documents.
- Document indexing: The search engine indexes a collection of documents to facilitate efficient searching.
- Relevant search results: The search engine ranks the search results based on relevance to the query.

## Requirements

Make sure you have the following installed:

- Python 3.x
- Flask framework
You can install Flask using the following commands:

```bash
pip install flask
```

## Setup

1. Clone this repository to your local machine:

```bash
git clone https://github.com/aakkash-k/search-engine.git
```

2. Navigate to the project directory:

```bash
cd search-engine/request
```

3. Install the required dependencies:

```bash
pip install -r requirement.txt
```


## Usage

1. Start the Flask server:

```bash
python query_api.py
```

2. Open your web browser and visit `http://localhost:5000` to access the search engine.

3. Enter your search keywords in the search box and click the "Search" button.

4. The search engine will retrieve and display the relevant search results based on your query.

## API Endpoints

The following API endpoints are available:

- `GET /`: Renders the search engine's web interface.
- `GET /search?q=keyword&location=place`: Retrieves search results based on the provided keywords. Returns a JSON response with the search results.
- `GET /previous_user?uid=unique id`: Retrieves result based on previous search history by using the unique id generated during the search results.

## DataBase
This project uses MongoDb as the database
  - It has one database and 3 collection
      search - database
        key_words - collection used for indexing the key words we get for the text 
        s_data    - collection for storing the actual text
        userid    - collection for storing the unque id generated during the search result
          

## Customization

You can customize the search engine by modifying the following files:

- `query_api.py`             : Update the search algorithm or implement additional features as per your requirements.
- `crawler/script_to_db`     : Update the scheme in the database
## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the Flask and Elasticsearch communities for their excellent documentation and resources.
