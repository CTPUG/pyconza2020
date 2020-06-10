# -*- encoding: utf-8 -*-
import os

from wafer.settings import *

try:
    from localsettings import *
except ImportError:
    pass

from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

pyconzadir = os.path.dirname(__file__)


STATICFILES_DIRS = (os.path.join(pyconzadir, "static"),)

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

TEMPLATES[0]["DIRS"] = (os.path.join(pyconzadir, "templates"),) + TEMPLATES[0]["DIRS"]

WAFER_MENUS += (
    {"menu": "about", "label": _("About"), "items": []},
 #   {
 #       "name": "venue",
 #       "label": _("Venue"),
 #       "url": reverse_lazy("wafer_page", args=("venue",)),
 #   },
 #   {"menu": "tickets", "label": _("Tickets"), "items": []},
 #   {"menu": "sponsors", "label": _("Sponsors"), "items": []},
    {
        "menu": "talks",
        "label": _("Talks"),
        "items": [
 #           {"name": "schedule", "label": _("Schedule"),
 #            "url": reverse_lazy("wafer_full_schedule")},
 #           {
 #               "name": "accepted-talks",
 #               "label": _("Accepted Talks"),
 #               "url": reverse_lazy("wafer_users_talks"),
 #           },
 #           {
 #               "name": "speakers",
 #               "label": _("Speakers"),
 #               "url": reverse_lazy("wafer_talks_speakers"),
 #           },
        ],
    },
    {"menu": "news", "label": _("News"), "items": []},
    {
        "menu": "previous-pycons",
        "label": _("Past PyConZAs"),
        "items": [
            {
                "name": "pyconza2012",
                "label": _("PyConZA 2012"),
                "url": "https://2012.za.pycon.org/",
            },
            {
                "name": "pyconza2013",
                "label": _("PyConZA 2013"),
                "url": "https://2013.za.pycon.org/",
            },
            {
                "name": "pyconza2014",
                "label": _("PyConZA 2014"),
                "url": "https://2014.za.pycon.org/",
            },
            {
                "name": "pyconza2015",
                "label": _("PyConZA 2015"),
                "url": "https://2015.za.pycon.org/",
            },
            {
                "name": "pyconza2016",
                "label": _("PyConZA 2016"),
                "url": "https://2016.za.pycon.org/",
            },
            {
                "name": "pyconza2017",
                "label": _("PyConZA 2017"),
                "url": "https://2017.za.pycon.org/",
            },
            {
                "name": "pyconza2018",
                "label": _("PyConZA 2018"),
                "url": "https://2018.za.pycon.org/",
            },
            {
                "name": "pyconza2019",
                "label": _("PyConZA 2019"),
                "url": "https://2019.za.pycon.org/",
            },
        ],
    },
    {
        "name": "twitter",
        "label": "Twitter",
        "image": "/static/img/twitter.png",
        "url": "https://twitter.com/pyconza",
    },
    {
        "name": "facebook",
        "label": "Facebook",
        "image": "/static/img/facebook.png",
        "url": "https://www.facebook.com/pyconza",
    },
)


def tickets_sold(ticket_types):
    """ Return number of tickets sold. """
    from wafer.tickets.models import Ticket, TicketType
    ticket_type_ids = TicketType.objects.filter(name__in=ticket_types)
    return Ticket.objects.filter(type_id__in=ticket_type_ids).count()


def main_conference_tickets_sold():
    """ Return number of tickets sold for the main conference. """
    from wafer.tickets.models import Ticket, TicketType

    TUTORIAL_TICKET_TYPES = [
    ]
    tutorial_type_ids = TicketType.objects.filter(name__in=TUTORIAL_TICKET_TYPES)

    return Ticket.objects.exclude(type_id__in=tutorial_type_ids).count()


CRISPY_TEMPLATE_PACK = "bootstrap4"
MARKITUP_FILTER = (
    "markdown.markdown",
    {
        "safe_mode": False,
        "extensions": [
            "mdx_outline",
            "attr_list",
            "mdx_attr_cols",
            "markdown.extensions.tables",
            "markdown.extensions.codehilite",
            "mdx_variables",
        ],
        #"extension_configs": {
        #    "mdx_variables": {
        #        "vars": {
        #            "main_conference_tickets_sold": main_conference_tickets_sold,
        #            'tutorial_unknown':
        #                lambda: tickets_sold([]),
        #        }
        #    }
        #},
    },
)

# Talks submissions are open
WAFER_TALKS_OPEN = True

# Set the timezone to the conference timezone
USE_TZ = True
TIME_ZONE = "Africa/Johannesburg"

# Default static and media locations - we rely on apache to redirect accordingly
# These are named to not clash with the repo contents
STATIC_ROOT = os.path.join(pyconzadir, "localstatic")

MEDIA_ROOT = os.path.join(pyconzadir, "localmedia")

# Ticket sales are open
WAFER_REGISTRATION_OPEN = False
WAFER_REGISTRATION_MODE = "ticket"

# Point static mirror away from the default, which is relative to the
# wafer package
BUILD_DIR = os.path.join(pyconzadir, "mirror")

# Will be needed for the static site generation
# WAFER_HIDE_LOGIN = True

# Needed to add pyconza-funding app
# INSTALLED_APPS = ('pyconza.funding', ) + INSTALLED_APPS
# ROOT_URLCONF = 'urls'
