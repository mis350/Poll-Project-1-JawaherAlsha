from django.contrib import admin

# Register your models here.
from .models import Poll, Option, Response
#from .models import Option
#from .models import Response

class PollAdmin(admin.ModelAdmin):
  list_display = ("title","question", "active_until","status", )
  list_filter = ("status",)
  search_fields = ("question",)

class OptionAdmin(admin.ModelAdmin):
  list_display = ("title",)



class ResponseAdmin(admin.ModelAdmin):
  list_display = ("name","response_time")


class PollInline(admin.TabularInline):
  model = Poll


class OptionAdmin2(admin.ModelAdmin):
  inline = (PollInline)


admin.site.register(Poll, PollAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Response, ResponseAdmin)