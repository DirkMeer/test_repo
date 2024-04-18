import requests
from requests.exceptions import RequestException

EXAMPLE_URL = "https://jsonplaceholder.typicode.com/todos"
EXAMPLE_SEARCH_TERM = "per"


def fetch_data(url: str) -> list[dict] | None:
    try:
        result = requests.get(url)
        results: list[dict] = result.json()
        return results
    except RequestException as error:
        print(f"Error: {error}")
        return None


def filter_titles(input_data: list[dict], search_term: str) -> list[str]:
    results_with_search_term = [
        result["title"] for result in input_data if search_term in result["title"]
    ]

    for index, title in enumerate(results_with_search_term):
        if type(title) == int:
            title = str(title)
        cut_sentence = title.split(search_term, 1)
        print(f"{index +1}. {cut_sentence[0]}{search_term.upper()}{cut_sentence[1]}")

    return results_with_search_term


if __name__ == "__main__":
    data = fetch_data(EXAMPLE_URL)
    if data:
        filter_titles(data, EXAMPLE_SEARCH_TERM)
