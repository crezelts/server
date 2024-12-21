# 요약 함수
# 검색 함수 (이게 실시간 데이터가 필요하면 Google&Bing 검색 api, 실시간 데이터X면 위키백키, 날씨 데이터가 필요하면 AccuWeather api 사용하기)
from classify import classify_intent # 의도 파악 함수
from all_fuc import pick_fuc
from flask import Flask, request, jsonify
from flask_cors import CORS
# 유저가 입력한 날씨 질문에서 지역,도시만 가져와서 해당 날씨 데이터 보여주는 함수 
# 자연어 생성 함수 (이것도 의도 파악해서 자연어 생성 시키기)

app = Flask(__name__)
CORS(app)

class Teramo:
    def __init__(self, user_input):
        self.user_input = user_input
    def classify_check(self):
        return classify_intent(self.user_input)
    def pick_all_fuc(self):
        return pick_fuc(self.user_input)

@app.route('/teramo', methods=['POST'])
def handle_request():
    data = request.get_json()

    user_input = data['user_input']
    teramo = Teramo(user_input)
    intent = teramo.classify_check()
    link_title_result_text, description_text_summary = teramo.pick_all_fuc()

    return jsonify({
        "intent": intent,
        "link_title_result_text": link_title_result_text,
        "description_text": description_text_summary
    }), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)


# from classify import classify_intent  # 의도 파악 함수
# from all_fuc import pick_fuc
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# class Teramo:
#     def __init__(self, user_input):
#         self.user_input = user_input

#     def classify_check(self):
#         return classify_intent(self.user_input)

#     def pick_all_fuc(self):
#         return pick_fuc(self.user_input)
        

# @app.route('/teramo', methods=['POST'])
# def handle_request():
#     data = request.get_json()

#     if not data or not data.get('user_input'):
#         return jsonify({"error": "user_input is required"}), 400

#     user_input = data['user_input']
#     teramo = Teramo(user_input)

#     # 클래스 메서드 호출 및 결과 저장
#     intent = teramo.classify_check()
#     response_text = teramo.pick_all_fuc()

#     # 응답 생성
#     return jsonify({
#         "intent": intent,
#         "response_text": response_text
#     }), 200

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000, debug=True)
