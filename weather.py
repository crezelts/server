import requests
import spacy


nlp = spacy.load("en_core_web_sm")

def weather_search(user_input):
    doc = nlp(user_input)

    # 지역/나라를 식별
    for ent in doc.ents:
        if ent.label_ in ["GPE"]:
            location = ent.text
            return location
        
def get_weather_search(loc):
    # certain_loaction = weather_search(user_input)
    ACCUWEATHER_KEY = 'RITjoH2opUczARPvvuelTKlvBY35FsWi'
    url = f'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=${ACCUWEATHER_KEY}&q=${loc}&language=en-us'
    response = requests.get(url)
    data = response.json()
    print(data)
    

# sklearn으로 지역만 뽑아내서 데이터 가져오기
get_weather_search("ulsan")