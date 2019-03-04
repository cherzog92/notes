import requests
from bs4 import BeautifulSoup

url = "https://cherzog92.pythonanywhere.com"

def test_home_page():
    print("testing home page")
    response = requests.get(url + "/notes")
    assert response.status_code == 200
    assert response.text > ""
    assert "<HTML>" in response.text.upper()

def test_home_page_has_submit_button():
    print()
    response = requests.get(url + "/notes")
    assert response.status_code == 200
    assert "type=\"submit\"" in response.text.lower().replace(" ","")
    soup = BeautifulSoup(response.text, "html.parser")
    inputs = soup.find_all("input")
    for input in inputs:
        print(input, input['type'])
    submit_inputs = [input for input in inputs if input['typ'] == 'submit']
    print(submit_inputs)
    assert len(submit_inputs) > 0
    for input in submit_inputs:
        assert input["value"] == "Submit"