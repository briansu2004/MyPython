# Django REST simple app

Django is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern.

Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.

## Set up

```
py --version
py get-pip.py
py -m pip --version
pip install Django
pip install djangorestframework
pip install markdown
pip install django-filter
django-admin startproject MyProject
python manage.py migrate
python manage.py runserver
python manage.py startapp api_basic
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

## Knowledge Points

- Django REST Framework Introduction
- Django Project Setup
- Django REST Framework Serializer
- REST Framework Modal Serializer
- REST Framework Function Based API Views
- REST Framework api_view() Decorator
- REST Class Based API Views
- REST Generic Views & Mixins
- REST Framework Authentication
- REST Framework Viewsets & Routers
- REST Framework Generic Viewsets
- REST Framework Modal Viewsets

## Screenshot

![01_install_py_django.png](images/01_install_py_django.png)

![02_install_django_rest.png](images/02_install_django_rest.png)

![03_migrate.png](images/03_migrate.png)

![04_runserver.png](images/04_runserver.png)

![05_8000.png](images/05_8000.png)

![05_8000_article.png](images/05_8000_article.png)

![06_startapp+superuser.png](images/06_startapp+superuser.png)

![07_admin.png](images/07_admin.png)

![08_makemigrations.png](images/08_makemigrations.png)

![09_admin_article.png](images/09_admin_article.png)

![10_admin_article_add.png](images/10_admin_article_add.png)

![11_shell1.png](images/11_shell1.png)

![12_shell2.png](images/12_shell2.png)

![13_postman_get_article.png](images/13_postman_get_article.png)

![13_postman_get_article_detail_2.png](images/13_postman_get_article_detail_2.png)

![13_postman_post_article_403.png](images/13_postman_post_article_403.png)

![14_postman_post_article_201.png](images/14_postman_post_article_201.png)

![15_8000_articles.png](images/15_8000_articles.png)

![16_postman_put_article_#2.png](images/16_postman_put_article_#2.png)

![17_postman_delete_article_#2.png](images/17_postman_delete_article_#2.png)

![18_8000_api_view_article.png](images/18_8000_api_view_article.png)

![19_8000_article_post.png](images/19_8000_article_post.png)

![20_8000_article_post_after.png](images/20_8000_article_post_after.png)

![21_8000_article_put.png](images/21_8000_article_put.png)

![22_8000_article_put_after.png](images/22_8000_article_put_after.png)

![23_fields__all__.png](images/23_fields__all__.png)

![24_8000_article_delete.png](images/24_8000_article_delete.png)

![25_8000_article_delete_after.png](images/25_8000_article_delete_after.png)

![26_APIView.png](images/26_APIView.png)

![27_APIView_after.png](images/27_APIView_after.png)

![28_GenericAPIView.png](images/28_GenericAPIView.png)

![29_GenericAPIView_after.png](images/29_GenericAPIView_after.png)

![30_auth.png](images/30_auth.png)

![31_postman_no_auth.png](images/31_postman_no_auth.png)

![32_postman_basic_auth.png](images/32_postman_basic_auth.png)

![33_admin_token_1.png](images/33_admin_token_1.png)

![34_admin_token_2.png](images/34_admin_token_2.png)

![35_admin_token_3.png](images/35_admin_token_3.png)

![36_postman_token_auth.png](images/36_postman_token_auth.png)
