# datetime: this module supplies classes for manipulating dates and times.
import datetime as dt
# Django is a high-level Python Web framework.
# django.core.mail: this module is provided for fast sending of emails
from django.core.mail import send_mail, BadHeaderError
# django.http: Django uses request and response objects to pass state through the system.
from django.http import HttpRequest, HttpResponse
# django.shortcuts: is a library that collects helper functions and classes that “span” multiple levels of MVC
from django.shortcuts import render
# django.template: Django uses loaders of its html templates
from django.template import loader

from .forms import ContactForm


def __function_name():
    """
    This function will return the caller's function name.
    """
    # Traceback: this module provides a standard interface to extract, format and print stack traces of Python programs
    import traceback

    return traceback.extract_stack(None, 2)[0][2]


def __common_context(title_suffix: str = '') -> dict:
    """
    Create common web context for every view, with a dictionary.
    Template refers to the context's properties using double {}, in this way: {{page_title}}, {{current_day_name}}

    :param title_suffix: string suffix to add to main title

    :return: A web context dict
    """
    now_ = dt.datetime.now()
    day_names_ = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return dict(
        page_title=f'MY DJANGO LEARNING {"" if title_suffix == "" else " - " + title_suffix}',
        current_day_name=day_names_[now_.weekday()],
        day_names=day_names_,
        formatted_now=now_.strftime('%d/%m/%Y %H:%M:%S'),
        now=now_,
    )


def home(request: HttpRequest) -> HttpResponse:
    """
    Create home view with html.

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # To review Built-in template tags and filters
    # Visit: https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

    # Select template
    template_ = 'home.html'

    # Create web context
    context_ = __common_context()

    # return HttpResponse object resulting of render method
    return render(request, template_, context_)


def blog(request: HttpRequest) -> HttpResponse:
    """
    Create blog view with html.

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # To review Built-in template tags and filters
    # Visit: https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

    # Select template
    template_ = 'blog.html'

    # Create web context
    context_ = __common_context()

    # return HttpResponse object resulting of render method
    return render(request, template_, context_)


def contact(request: HttpRequest) -> HttpResponse:
    """
    Create contact view with html.

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # To review Built-in template tags and filters
    # Visit: https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

    # Select template
    template_ = 'contact.html'

    # Flag to identify if the form was submitted
    sent_ = False
    error_ = ''
    if request.method == 'GET':
        # When the method is GET, an empty form should be displayed
        form_ = ContactForm()
    else:
        # Method is POST, if user submitted form
        form_ = ContactForm(request.POST)

        # is_valid() method runs validation and returns a boolean designating whether the data is valid
        # Visit: https://docs.djangoproject.com/en/3.1/ref/forms/api/#django.forms.Form.is_valid
        if form_.is_valid():
            # Once you’ve created a Form instance with a set of data and validated it,
            #   you can access the clean data via its cleaned_data attribute, that is a dictionary
            # Visit: https://docs.djangoproject.com/en/3.1/ref/forms/api/#django.forms.Form.cleaned_data
            name = form_.cleaned_data['name']
            subject = form_.cleaned_data['subject']
            from_email = form_.cleaned_data['email']
            message = form_.cleaned_data['message']

            try:
                # Send mail
                send_mail(subject, message, f'{name} <{from_email}>', ['ndr1970@gmail.com'])
                # Success!
                sent_ = True
            except BadHeaderError:
                error_ = 'Invalid header found.'
            except Exception as e:
                error_ = str(e)

    # Create web context
    context_ = __common_context('Contact me')
    context_['form'] = form_
    context_['sent'] = sent_
    context_['error'] = error_

    # return HttpResponse object resulting of render method
    return render(request, template_, context_)


def video(request: HttpRequest) -> HttpResponse:
    """
    Create video view with html.

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # To review Built-in template tags and filters
    # Visit: https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

    # Select template
    template_ = 'videos.html'

    # Create web context
    video_links_ = ['https://www.youtube.com/embed/BcoPWMtmgJk',
                    'https://www.youtube.com/embed/Opm8KKR99kQ',
                    'https://www.youtube.com/embed/d1-UX6aR_TM']
    context_ = __common_context('Videos')
    context_['video_links'] = video_links_

    # return HttpResponse object resulting of render method
    return render(request, template_, context_)


"""
    Early and old learning functions (which were being replaced)
"""


def hello_world(request: HttpRequest) -> HttpResponse:
    """
    Create hello word view simple string

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    # return HttpResponse object
    return HttpResponse('Hello, World!')


def calculate_age(request: HttpRequest,
                  current_age_: int,
                  future_year_: int) -> HttpResponse:
    """
    Create age calculator

    :param request: HttpRequest object with metadata about the request
    :param current_age_: current age
    :param future_year_: future year for calculate age

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    current_year_ = dt.datetime.now().year
    future_age_ = current_age_ + (future_year_ - current_year_)

    html_document_ = f"""
        <html>
        <body>
        <h1>Age Page</h1>
        <h2>In {future_year_} you will be {future_age_} years old.</h2>
        </body>
        </html>
    """

    # return HttpResponse object
    return HttpResponse(html_document_)


def old_home(request: HttpRequest) -> HttpResponse:
    """
    Create home view with html, without using django.shortcuts

    :param request: HttpRequest object with metadata about the request

    :return: HttpResponse object
    """
    print(f'{__function_name()} request:', request)

    """
        Previously to use template

        html_document_ = 
            <html>
            <body>
            <h1>Home Page</h1>
            <h3>{dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</h3>
            </body>
            </html>
    """

    # To review Built-in template tags and filters
    # Visit: https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

    # Getting our template (load template)
    html_template_ = loader.get_template('home.html')

    # Create web context
    context_ = __common_context()

    # Render document
    html_document_ = html_template_.render(context_)

    # return HttpResponse object
    return HttpResponse(html_document_)
