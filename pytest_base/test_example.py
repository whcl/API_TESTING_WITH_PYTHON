import requests
import pytest

class TestAPI:

    names = [
        ("John"),
        ("Ivan"),
        ("")
    ]

    @pytest.mark.parametrize('name', names) #параметризация
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}
        response = requests.get(url, params=data)
        assert response.status_code == 200, f'' \
                                             f'Wrong result status code'
        response_dict = response.json()
        assert "answer" in response_dict, f'There is no field name "answer"'

        if len(name) == 0:
            expected_response_text = f"Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]

        assert expected_response_text == actual_response_text, f'' \
                                                              f'Actual text is {response_dict["answer"]}'