
from pathlib import Path
from .const import *  #把常量文件的全部常量导进来


BASE_DIR = Path(__file__).resolve().parent.parent
import sys
import os.path

sys.path.insert(0, str(BASE_DIR))  # 把当前的helloword_backend小文件添加到环境变量
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))
# 把当前的apps文件夹添加到环境变量



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l#-rs(!y@uu9fdi%h2bf*4*4vd7vr0@t^u7rin3=h@ck8lrp-0'

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django',  # 这个是django自带的
    'rest_framework',# 这个是django-rest-framework自带的
    'corsheaders',
    'django_filters',
    # 'study',
    # 'user',
    # 'tools',
    # 'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'  # 把cors模块的中间件导入
]

ROOT_URLCONF = 'helloword_backend.urls'

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

WSGI_APPLICATION = 'helloword_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 日志配置
# 真实项目上线后，日志文件打印级别不能过低，因为一次日志记录就是一次文件io操作
LOGGING = {
    'version': 1,  # 版本号
    'disable_existing_loggers': False,     #
    'formatters': { # 用k，v的形式写格式名：格式类型
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },    # 这是一种叫verbose的格式
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        }, # 这是一种叫simple的格式
    },  # 日志记录的格式
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {   # 什么时候打印到终端
            # 实际开发建议使用WARNING
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {   # 存放到日志文件的情况
            # 实际开发建议使用ERROR
            'level': 'ERROR',   # 哪个错误级别开始存
            'class': 'logging.handlers.RotatingFileHandler',   # 这个是可以到了300m就给自动轮转切换的
            # 日志位置,日志文件名,日志保存目录必须手动创建，注：这里的文件路径要注意BASE_DIR代表的是小luffyapi
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "luffy.log"),   # !!!!最需要关注的，每次存在luffyapi前的根目录下的logs文件夹下，取名叫luffy.log
            # 日志文件的最大值,这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 10,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True, # 是否让日志信息继续冒泡给其他的日志处理系统
        },    # 建了一个叫django的日志
    }
}


# 配置跨域资源共享配置
CORS_ORIGIN_ALLOW_ALL = False
# 是否开放所有域

# 开放的请求方式
CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT',
	'VIEW',
)

# 允许的请求头
CORS_ALLOW_HEADERS = (
	'authorization',
	'content-type',
)

import datetime
JWT_AUTH={
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7), # 手动配置过期时间
}