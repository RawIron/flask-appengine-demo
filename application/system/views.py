import base64
import datetime
import logging
import time
import urllib

from google.appengine.api import logservice
from flask import render_template


def list_logs():
    return _readLogByBuffer()


# This sample gets the app request logs up to the current time, displays 5 logs
# at a time, including all AppLogs, with a Next link to let the user "page"
# through the results, using the RequestLog offset property.

def _getOffset(request):
    # Get the incoming offset param from the Next link to advance through
    # the logs. (The first time the page is loaded, there won't be any offset.)
    offset = 0
    try:
        offset = request.get('offset') or None
        if offset:
            offset = base64.urlsafe_b64decode(str(offset))
    except TypeError:
        offset = None
    return offset


def _readLogByOffset(request):

    offset = _getOffset(request)

    # Set up end time for our query.
    end_time = time.time()

    # Count specifies the max number of RequestLogs shown at one time.
    # Use a boolean to initially turn off visiblity of the "Next" link.
    count = 5
    show_next = False
    last_offset = None

    # Iterate through all the RequestLog objects, displaying some fields and
    # iterate through all AppLogs beloging to each RequestLog count times.
    # In each iteration, save the offset to last_offset; the last one when
    # count is reached will be used for the link.
    i = 0
    req_logs = []
    for req_log in logservice.fetch(end_time=end_time, offset=offset,
                                    minimum_log_level=logservice.LOG_LEVEL_INFO,
                                    include_app_logs=True):
        last_offset= req_log.offset
        i += 1
        req_logs.append(req_log)

        if i >= count:
            show_next = True
            break

    render_template('list_app_log.html', logged_requests=req_logs)

    # Prepare the offset URL parameters, if any.
    if show_next:
        query = request.GET
        query['offset'] = base64.urlsafe_b64encode(last_offset)
        next_link = urllib.urlencode(query)
        _closePageWithNextInHtml()


def _readLogByBuffer():
    req_logs = logservice.log_buffer_contents()
    return render_template('list_request_log.html', logged_requests=req_logs)
    
