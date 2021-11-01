from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'updated_at',)

admin.site.register(Article, ArticleAdmin)

# CRUD
# C - Create
# R - Read
# U - Update
# D - Delete

# page - CRUD
# page - index
# page - Create
# page - Read (1개 읽어오기)
# page - Update (1개 업데이트)
# page - Delete (1개 삭제)

# index
# GET /pages/
# GET /pages/1
# POST /pages/
# POST /pages/1/update
# POST /pages/1/delete
