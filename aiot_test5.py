from flask import Flask, request, render_template       # Flask 웹 서버 구축을 위한 라이브러리
                                                        # Flask: 웹 서버 생성, request: 브라우저가 보낸 데이터 수신, render_template: HTML 파일 화면에 표시
from gpiozero import LED                                # 라즈베리파이 GPIO 제어를 위해 LED 클래스 불러오기

app = Flask(__name__)                                   # Flask 애플리케이션 객체 생성 (현재 파일명을 기준으로 설정)

red_led = LED(21)                                       # GPIO 21번 핀에 연결된 LED 객체 생성

@app.route('/')                                         # 기본 경로('/')로 접속했을 때 실행될 함수 지정
def home():                                             # 홈페이지 접속 시 실행되는 함수
   return render_template("index.html")                 # index.html 파일을 웹 브라우저에 표시

@app.route('/data', methods = ['POST'])                 # '/data' 경로로 POST 방식의 데이터가 들어올 때 실행
def data():                                             # 버튼 클릭 시 데이터를 처리하는 함수
    data = request.form['led']                          # HTML 폼(form)에서 'led'라는 이름을 가진 input의 값(on/off)을 가져옴
    
    if(data == 'on'):                                   # 만약 가져온 데이터 값이 'on'이라면
        red_led.on()                                    # GPIO 21번에 연결된 LED를 켬
        return home()                                   # 처리가 끝난 후 다시 홈 화면으로 돌아감

    elif(data == 'off'):                                # 만약 가져온 데이터 값이 'off'라면
        red_led.off()                                   # GPIO 21번에 연결된 LED를 끔
        return home()                                   # 처리가 끝난 후 다시 홈 화면으로 돌아감

if __name__ == '__main__':                              # 이 파일이 직접 실행될 경우에만 아래 코드를 실행
   app.run(host = '0.0.0.0', port = '80')               # 모든 IP로부터 접속을 허용하며 80번 포트로 서버 실행
