import requests
import pytest
from pytest import mark
from resources.status_codes import *
from resources.main import *
from resources.requiremnents import *


class TestGetTypicodeDemoDb:
    """
    Simple Test of REST API .

    To run all test:
        pytest tests -v

    To run only smoke tests
        pytest tests -v -m smoke

    To run only negative tests
        pytest tests -v -m negatives

    """

    url = f"{BASE_URL}/typicode/demo/db"
    payload = {}
    headers = {}

    @mark.health
    @pytest.fixture()
    def response_data(self):
        """
        This method will run before each test which has response_data in params
        :return:
        """
        response = requests.get(url=self.url, headers=self.headers, data=self.payload)
        assert response.status_code == OK
        return response.json()

    @mark.smoke
    def test_properties_lengths(self, response_data):
        assert len(response_data[POSTS]) > MIN_VALUE
        assert len(response_data[COMMENTS]) > MIN_VALUE
        assert len(response_data[PROFILES]) > MIN_VALUE

    def test_post_titles(self, response_data):
        posts = response_data[POSTS]
        for index in range(len(posts)):
            assert posts[index]["title"] == f"{POSTS_TITLE} {index + 1}"

    def test_whole_body(self, response_data):
        assert response_data == {
            "posts": [
                    {
                        "id": 1,
                        "title": "Post 1"
                    },
                    {
                        "id": 2,
                        "title": "Post 2"
                    },
                    {
                        "id": 3,
                        "title": "Post 3"
                    }
                ],
            "comments": [
                    {
                        "id": 1,
                        "body": "some comment",
                        "postId": 1
                    },
                    {
                        "id": 2,
                        "body": "some comment",
                        "postId": 1
                    }
                ],
            "profile": {
                    "name": "typicode"
                }
            }

    def test_cookies(self, response_data):
        response = requests.get(url=self.url, headers=self.headers, data=self.payload)
        assert len(response.cookies) > MIN_VALUE

    def test_headers(self, response_data):
        response = requests.get(url=self.url, headers=self.headers, data=self.payload)
        assert len(response.headers) > MIN_VALUE

    @mark.negatives
    def test_with_wrong_method(self):
        response = requests.post(url=self.url, headers=self.headers, data=self.payload)
        assert response.status_code == NOT_FOUND
        assert response.json() == EMPTY_BODY

