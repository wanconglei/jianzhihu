from django.contrib import admin
from .models import Issue, Topic, Answer, Comment


# Register your models here.
admin.site.register(Issue)
admin.site.register(Topic)
admin.site.register(Answer)
admin.site.register(Comment)

