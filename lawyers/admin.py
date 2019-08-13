from django.contrib import admin
from .models import Lawyer, Case, AssignLinks, SeenDetails

# Register your models here.
admin.site.register(Lawyer)
admin.site.register(Case)
admin.site.register(AssignLinks)
admin.site.register(SeenDetails)