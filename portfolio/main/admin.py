from django.contrib import admin

from .models import Header, AboutMe, Education, Skill, Project, Contact

# Register your models here.

admin.site.register(Header)
admin.site.register(AboutMe)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Contact)

