from flask import Flask
from controller import main, login, user_profile, signup

app = Flask(__name__)

app.secret_key = '4e68e4301a5d8473b81858461e61f9f6'

# 블루프린트 등록 
app.register_blueprint(main.bp)
app.register_blueprint(login.bp)
app.register_blueprint(user_profile.bp)
app.register_blueprint(signup.bp)

if __name__ == '__main__':
    # debug를 True로 세팅하면, 해당 서버 세팅 후에 코드가 바뀌어도 문제없이 실행됨. 
    app.run(host='127.0.0.1', port=8000, debug = True)