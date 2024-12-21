from classify import classify_intent
from real_time_info import real_time
from text_summaizer import summarize_text
from weather import weather_search

def pick_fuc(user_input):
    intent = classify_intent(user_input)
    # 의도와 함수 매핑
    intent_to_function = {
        "summary": summarize_text,
        "weather": weather_search, # AcuuWeather api 사용하기 / 함수도 바꿔야 함
        "search": real_time,
        "question": real_time,
        "translation": "",
        "conversation": "",
        "recommand": real_time # 이것도 검색 사용해서 추천해주기 ex) 상품이면 그에 맞게
    }

    # 해당 의도에 맞는 함수 호출
    if intent in intent_to_function:
        return intent_to_function[intent](user_input)
    else:
        return "죄송합니다.. 이해하지 못했습니다."