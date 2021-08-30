"""
Django settings for gisweb_1 project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = 이 프로젝트의 경로
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent



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


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accountapp',
    'bootstrap4',
    'profileapp',
    'articleapp',
    'commentapp',
    'projectapp',
    'subscribeapp',
    'likeapp',

]

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gisweb_1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gisweb_1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# 주소창에 경로가 들어왔을때 static이 보이게 한다.
STATIC_URL = '/static/'
# 최상위 BASE_DIR폴더안의 staticfiles파일이 STATIC_ROOT(가장 밑에 파일)이 될것이다.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / "static",
    #'/var/www/static/', #이부분은 필요가 없어서 지워도 된다
]

# profile앱을 만들기 위해 설정하기
MEDIA_URL = '/media/'
# 최상위 BASE_DIR폴더안의 staticfiles파일이 STATIC_ROOT(가장 밑에 파일)이 될것이다.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL  = reverse_lazy('articleapp:list')
LOGOUT_REDIRECT_URL = reverse_lazy('accountapp:login')
