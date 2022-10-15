#CS/WebDev #CS/Lang/Python

References
* [the Django Girls Tutorial](https://tutorial.djangogirls.org/) ([or the Chinese translation](https://carolhsu.gitbooks.io/django-girls-tutorial-traditional-chiness/)).
* [The Django Documentation][DjangoDoc]
* [](https://github.com/encode/django-rest-framework/tree/master)

# MTV framework (instead of MVC)

| MVC | MTV | Usage |
|:----:|:----:| ----- |
| Model | Model | Business Logic: The database design. |
| View | Template | HTML template to be filled with data. |
| Controller | View | Based on the `request` form, do some work with databases and return a (filled) html template page. |

The workflow of a `request` is 

```plantuml
start
:Url dispatcher ""urls.py"" 
decides which ""view"" to be the entry point.;
:A function defined ""views.py""
takes ""request"" as its first argument;
note right
    * Access objects defined in ""models.py"".
    * Fill a template with ""HttpResponse"".
end note
:Response a filled HTML;
stop
``` 

## Model

* All syntax could be found in [Model][ModelDoc].
    * Available built-in `Field` types could be found in [Model field reference](https://docs.djangoproject.com/en/dev/ref/models/fields/).

A model is a special class of objects which stores all its member data in a database. A table in database corresponds to a bunch of member data of class instances.

```python
from django.db import models
# Import whatever you need
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ExampleModel(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

Since a table in database is correspond to a model, the features of a database has to be followed:
* **Automatic primary key fields**:  
    By default, `id = models.AutoField(primary_key=True)` is provided unless `primary_key` is explicitily specified.
* Relationships
    * `ForeignKey`: Many-to-one relationship.
    * `ManyToManyField`: Many-to-many relationship.
    * `OneToOneField` : One-to-one relationship.
* Field operations
    * 

### Migration

* Keeps track of the structural change of the database.
* Create new with `python3 manger.py makemigrations`, and a `migrations` directory is created, in which `0001_initial.py` keeps the structure of the first commitment.
* Sync the change in db structure with `python3 manage.py migrate`. The change will be detected automatically and a sort-of change log will be generated in the `migrations` directory.

## Template

### Django template language

* All syntax could be found in [Django Template Language][TemplateDoc], which is based on the [Jinja2 Template](https://jinja.palletsprojects.com/en/master/templates/)
* Remark that templates could be project-wide or app-wide, you could create `templates/` directory under `root` or an app.

## View

```python
from django.shortcuts import render

# Control your views based on templates.
def exampleView(request):
    # Do something here.
    return render(request, 'APPNAME/templates/template.html', locals())
```

# REST framework with [DRF][DRF]

However, to make your life easier, forget about the django template language, we'd better separate frontend from backend. Use [`django-rest-framework`][DRF] to keep only `model` for backend. 

Tutorials:
* [手把手程式實作分享系列：建構 Django REST framework (DRF) API
](https://medium.com/bandai%E7%9A%84%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98/%E6%89%8B%E6%8A%8A%E6%89%8B%E7%A8%8B%E5%BC%8F%E5%AF%A6%E4%BD%9C%E5%88%86%E4%BA%AB%E7%B3%BB%E5%88%97-%E5%BB%BA%E6%A7%8B-django-rest-framework-drf-api-bf7e6e1997e4)
* [Udemy: Master Django by Building Complete RESTful API Project](https://www.udemy.com/course/master-django-by-building-complete-restful-api-project/)

Some known issues of DRF:
* Performance in Serializer
    * https://www.dabapps.com/blog/api-performance-profiling-django-rest-framework/
    * http://ses4j.github.io/2015/11/23/optimizing-slow-django-rest-framework-performance/


# Deploy

## Heroku

Nope, I don't manage to try this section recently.

## Google Cloud

See [Manual](https://cloud.google.com/python/django)

# Cheatsheet

* Run server `python3 manage.py runserver`

## A project

* Create new with `django-admin.py startproject PROJECTNAME .` 
* The hierarchy of a project, those which start with `#` are NOT built automatically.
    ```
    root
    ├── manage.py
    ├── #templates/*.html
    └── PROJECTNAME
        ├───settings.py
        ├───urls.py
        ├───wsgi.py
        └───__init__.py
    ```
* Modify [`settings.py`][settings.py]. There are so many options, usually 
    ```
    LANGUAGE_CODE = 'zh-TW'
    USE_TZ = False
    TIME_ZONE = 'Asia/Taipei'     
    ``` 
  
## An app

* Create new with `python3 manage.py startapp APPNAME`
* The hierarchy of an app, those which start with `#` are NOT built automatically. 

    ```
    root
    ├── manage.py
    ├── PROJECTNAME
    └── APPNAME
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── migrations/*.py
        ├── # templates/*.html
        ├── views.py
        └── tests.py
    ```
* Book the app in `PROJECTNAME/settings.py`

    ```
    INSTALLED_APPS = (
        ...
        'APPNAME',
    )
    ```
* (Optional) Book url dispatch in `PROJECTNAME/urls.py`.
* (Optional) Define application configuration in [`apps.py`][AppDoc].
* Customize [`models.py`][ModelDoc], [`templates/*.html`][TemplateDoc], and `views.py`.
* Don't forget `tests.py`.

## Database Operations

* Initialize database with `python3 manage.py syncdb`

### Migration

* Create new with `python3 manger.py makemigrations`
* Sync the change in db structure with `python3 manage.py migrate`.

# Useful links

* [Django Documentation][DjangoDoc]
    * [Template Language][TemplateDoc]
    * [Model API][ModelDoc]
    * [`settings.py`][settings.py]

[DjangoDoc]: https://docs.djangoproject.com/en/3.1/
[AppDoc]: https://docs.djangoproject.com/en/3.1/ref/applications/
[TemplateDoc]: https://docs.djangoproject.com/en/3.1/ref/templates/
[ModelDoc]: https://docs.djangoproject.com/en/3.1/topics/db/models/
[DRF]: https://github.com/encode/django-rest-framework/tree/master
[settings.py]: https://docs.djangoproject.com/en/3.1/ref/settings/


   
