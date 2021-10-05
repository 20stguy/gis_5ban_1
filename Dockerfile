FROM python:3.9.0

# /home/은 윈도우의 바탕화면 같은 느낌 무조건 있어야 하는것
WORKDIR /home/

# 다시 git에 push할때 필요한듯?
RUN echo 'nothing_meaning5adsf'

# 정원님 여기 master 브랜치로 merge 하신 이후에
# 계속 master 에다가 커밋하고 계신거죠?
# 이전시간에 mater로 merge했고 오늘 수업시간에 처음으로 pycharm에서
# 커밋 했더니 merge하겠냐는 메시지 떠서 ok는 눌렀는데
# 이게 올바른 방법인지는 잘 모르겠습니다.

# 일단 보니까 master 로 계속 커밋을 보내시는 것 같은데,
# 이전에 제가 -b 1 이 부분을 추가해달라고 말씀 드렸던게,
# 저 master 브랜치가 아니라 1 브랜치를 사용하도록 하는 명령어입니다.
# 그런데 지금 다시 master 를 쓰면 해당 명령어를 지워주어야 정상적으로
# 작동할거에요. 그러니까 해당 내용 지우고 다시 이미지 만들어보도록 하겠습니다.
# 넵
# 아이고 안지우고 했네요 ㅋㅋㅋ

# git에 올려둔 소스 코드 불러오기
# RUN git clone -b 1 https://github.com/20stguy/gis_5ban_1.git
RUN git clone https://github.com/20stguy/gis_5ban_1.git

#
WORKDIR /home/gis_5ban_1/

# echo 리눅스에서 print와 같은 명령어, > .env파일 형태로 출력하기
# django에서 .env파일을 RUN echo로 불러왔으나 doker secret로 민감정보를 옮기면서 삭제해도 된다. 이건 deploy.py에서 read_secret함수로 대신 읽어온다.
#RUN echo "SECRET_KEY=django-insecure-5e22sx2ua8fxf!7zv+86d7)=^6f_uhla1bw8l48y^*s%_o1w^o" > .env
# 버전이 바뀜에 따라 RUN echo가 필요하므로 다시 아무거나 적어준다.
RUN echo "no_meaning"

# 깃허브에 올린 환경설정 라이브러리 담긴 requiremnets.txt 설치
RUN pip install -r requirements.txt
#
RUN pip install gunicorn

RUN pip install mysqlclient

RUN python manage.py makemigrations

# migrate뒤에 --settings=gisweb_1.settings.deploy가 없으면 로컬설정으로 돌아가게 된다. deploy설정으로 바꿔준다.
# 개봘환경(pycharm)에 db.sqlite3파일이 있지만 가상 서버에는 없으므로 db생성 작업
#RUN python manage.py migrate --settings=gisweb_1.settings.deploy

# --noinput을 사용하여서 두번이상의 업데이트에도 yes or no창이 뜨지 않고 항상 Image에 업로드 되게 만들기.
#RUN python manage.py collectstatic --noinput --settings=gisweb_1.settigns.deploy

# 우리가 사용할 포트번호를 노출 시켜주기
EXPOSE 8000

# 메인앱 이름(gisweb_1)안에있는 wsgi.py파일을 써라
# &&로 연결된 구문은 ""하나 안에 다 들어가야 된다. 다 들어가게 바꾼뒤에 django부터 다시 만들어봐라.
CMD ["bash", "-c", "python manage.py migrate --settings=gisweb_1.settings.deploy && python manage.py collectstatic --noinput --settings=gisweb_1.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gisweb_1.settings.deploy gisweb_1.wsgi --bind 0.0.0.0:8000"]

# python manage.py같은 명령어를 넣어준다 [""]안에 단어 하나하나를 넣는다.
# == python manage,py runserver 0.0.0.0:8000 과 같은 뜻이다.
# gunicorn을 깔면 아래 명령어를 대신한다.
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]







