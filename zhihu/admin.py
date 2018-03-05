from django.contrib import admin
from .models import Issue, Topic, Answer


# Register your models here.
admin.site.register(Issue)
admin.site.register(Topic)
admin.site.register(Answer)
