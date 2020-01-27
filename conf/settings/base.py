"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
CONF_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(CONF_DIR))

BASE_DIR = os.environ.get("BASE_DIR") or BASE_DIR

# sys.path.insert(0, BASE_DIR)
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    # 'sorl.thumbnail',
    'captcha',
    'django_global_request',

    'qapi',
    'quser',
    'qcache',
    'qsmstoken',
    #
    'apps.qfile',
    'wxapp',
    'apps.account',
    'apps.config',
    'apps.goods',
    'apps.group_buy',
    'apps.refund',
    'apps.trade',
    'apps.count',
    'apps.shop',
    'apps.user',
    'wx_pay',
    'apps.feedback',
    'apps.homepage',
    'apps.sms',
    'apps.tools',
    'apps.cloud',
    'apps.wx_logistics',
    'apps.short_video',
    'apps.utils',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'apps.utils.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_global_request.middleware.GlobalRequestMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/api/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/api/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#朋友圈分享海报
POSTER_ROOT = os.path.join(MEDIA_ROOT, 'poster')

if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)

if not os.path.exists(POSTER_ROOT):
    os.mkdir(POSTER_ROOT)

FILE_UPLOAD_MAX_MEMORY_SIZE = 26214400
FILE_UPLOAD_PERMISSIONS = 0o644


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'wxapp.authentication.WxSessionAuthentication'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'qapi.pagination.PageSizePagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'EXCEPTION_HANDLER': 'qapi.handler.exception_handler',
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'cancel_order': '2/minutes',
        'confirm_receipt': '2/hours',
        'daily_remind': '1/hours',
        'calc': '1/hours',
    }
}

AUTH_USER_MODEL = 'user.User'

#后台管理配置
IS_CAPTCHA_ENABLE = True
DEFAULT_ADMIN_PASSWORD = 'awegawefawgaw'  # 默认的管理员密码
USER_MODEL_VERBOSE_NAME = '管理员'  # 重写 Django get_user_model() 的 verbose_name 和 verbose_name_plural
USER_MODEL_VERBOSE_NAME_PLURAL = '管理员'
GROUP_MODEL_VERBOSE_NAME = '角色'  # 重写 Django auth.models.Group 的 verbose_name 和 verbose_name_plural
GROUP_MODEL_VERBOSE_NAME_PLURAL = '角色'
USER_JUST_ONE_GROUP = True  # 限定一个用户只能有一个角色

# 可用于后台用户编辑的权限
EDITABLE_PERMISSIONS = (
    'account.RechargeRecord:view',
    'config.FaqContent:view|add|change|delete',
    'config.Level:view|add|change|delete',
    'config.RechargeType:view|add|change|delete',
    'config.Notice:view|add|change|delete',
    'count.Count:view|view_total_count',
    'qfile.File:view|add|change|delete',
    'qfile.Tag:view|add|change|delete',
    'goods.City:view|add|change|delete',
    'goods.GoodsCategory:view|add|change|delete',
    'goods.Goods:view|add|change|delete|create_template',
    'goods.GoodType:view|add|change|delete|change_rebate_bonus',
    'goods.Banner:view|add|change|delete',
    'goods.OrdGoods:view|add|change|delete',
    'goods.SubGoodsType:view|add|change|delete',
    'goods.SubGoods:view|add|change|delete',
    'godos.Attach:view|add|change|delete',
    'group_buy.PtGroup:view|change',
    'group_buy.GroupBuyInfo:view|add|change|delete',
    'feedback.FeedBack:view|change',
    'trade.OrderInfo:view|change|',
    'trade.Order:view|change',
    'trade.GoodsItems:view|change|send',
    'shop.Shop:view|add|change|delete|view_all_shop',
    'user.User:view|add|change|delete|can_reset_password|view_all_user',
    'auth.User:view|add|change|delete|can_reset_password',
    'auth.Group:view|add|change|delete',
)

PERMISSION_ACTIONS = {
    'reset': '重置',
}

# 给 admin 用户添加自定义权限
USER_CUSTOM_PERMISSIONS = [
]

SHOP_NAME = '骆驼小店'
SHOP_SITE = 'luotuoxiaodian'
NUMBER_OF_SHOP = 1    # 店铺数量


# code: apps.tools.apps ready func
# allow modify host
USE_X_FORWARDED_HOST = True


# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': '/var/tmp/django_cache',
        'TIMEOUT': 1 * 60 * 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        },
    },
    'qcache': {
        'BACKEND': 'qcache.no_pickle_cache_backend.NoPickleLocMemCache',
        'LOCATION': 'qcache-only',
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        },
    },
}
