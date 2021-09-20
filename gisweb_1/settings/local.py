# 기본적으로 공통적인건 .base.py에서 모두 불러오고 그외의 개발 단만 local.py에 넣는다.
from .base import *

# os = 운영체제에서 제공하는 통일된 모듈(windows, linux등)
# path = 경로
# join = (BASE_DIR)와 연결시키겠다
local_env = open(os.path.join(BASE_DIR, '.env'))

# 빈 딕셔너리 만들기
env_list = dict()

while True:
    line = local_env.readline() # 한줄씩 읽기
    if not line: # 끝까지 다 읽으면 while문 나가기
        break
    line = line.replace('/n', '') #라인을 다 읽고나면 마지막 줄바꿈 문장을 공백으로 치환
    start = line.find('=') # '='문자가 나타나는 첫번째 인덱스 찾기 secret_key = 키넘버에서 =을 먼저 찾아야 하니까
    key = line[:start] # =이전의 값까지가 key가 될것이고
    value = line[start+1:] # =이후의 값부터가 value가 될것이다
    env_list[key] = value # 키 값에 value값 합치기



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY는 따로 분리함으로써 GIT에 올릴때 보안을 지키면서도 실행시킬 수 있다
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
