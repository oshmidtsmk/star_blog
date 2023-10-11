#groups/admin.py

from django.contrib import admin

from . import models


class GroupMemberInline(admin.TabularInline):  #Add inline Registration of the Group member as well # this add some convenince when I click on group in Admin side, i will see its group memebers beneath as well
    model = models.GroupMember



admin.site.register(models.Group)
