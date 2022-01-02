from django.contrib import admin

from .models import Teachers
from .models import Reviews
from .models import Students
from .models import Groups


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','midle_name',
                    'rtgKnow','rtgTeaching_skill','rtgCommunication','rtgFreebie','rtgOverall_score','link')
    search_fields = ('first_name','last_name','midle_name')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id_tg', 'first_name','last_name','midle_name',
                    'Know','Teaching_skill','Communication','Freebie','Overall_score','data')


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('email','id_tg','faculty','group','code','reg_status')


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','midle_name','group')
    fields  =('first_name','last_name','midle_name')