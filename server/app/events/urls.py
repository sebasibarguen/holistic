from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from events import views

urlpatterns = [
    path('events/', views.event_list),
    path('events/<slug:messageId>/', views.event_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# from events.models import Event
# from events.serializers import EventSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# import json

# data = '''{
#   "anonymousId": "23adfd82-aa0f-45a7-a756-24f2a7a4c895",
#   "context": {
#     "library": {
#       "name": "analytics.js",
#       "version": "2.11.1"
#     },
#     "page": {
#       "path": "/academy/",
#       "referrer": "",
#       "search": "",
#       "title": "Analytics Academy",
#       "url": "https://segment.com/academy/"
#     },
#     "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
#     "ip": "108.0.78.21"
#   },
#   "event": "Course Clicked",
#   "integrations": {},
#   "messageId": "ajs-f8ca1e4de5024d9430b3928bd8ac6b96",
#   "properties": {
#     "title": "Intro to Analytics"
#   },
#   "receivedAt": "2015-12-12T19:11:01.266Z",
#   "sentAt": "2015-12-12T19:11:01.169Z",
#   "timestamp": "2015-12-12T19:11:01.249Z",
#   "type": "track",
#   "userId": "AiUGstSDIg",
#   "originalTimestamp": "2015-12-12T19:11:01.152Z"
# }'''

# serializer = EventSerializer(data=json.loads(data))
# serializer.is_valid()
# serializer.save()