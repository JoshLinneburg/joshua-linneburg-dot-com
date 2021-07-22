import markdown
from markupsafe import Markup
import pytz


def datetime_filter(value, format="%I:%M %p", timezone="US/Eastern"):
    tz = pytz.timezone(timezone)  # timezone you want to convert to from UTC
    utc = pytz.timezone('UTC')
    value = utc.localize(value, is_dst=None).astimezone(pytz.utc)
    local_dt = value.astimezone(tz)
    return local_dt.strftime(format)


def render_markdown(raw_markdown):
    stringOfMarkdown = markdown.markdown(raw_markdown,
                                         extensions=['markdown.extensions.attr_list', 'markdown.extensions.codehilite',
                                                     'markdown.extensions.fenced_code']
                                         )

    return Markup(stringOfMarkdown)