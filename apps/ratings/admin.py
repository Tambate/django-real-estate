from django.contrib import admin

from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    #hien thi danh sach trong truong admin
    list_display = ["rater", "agent", "rating"]

admin.site.register(Rating, RatingAdmin)