from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # true_forms = ArticleTag.objects.filter(is_main=True).count()
            # if true_forms == 1:
            if form.is_valid:
                form.cleaned_data
                # form.save()
            else:
                raise ValidationError('Тут всегда ошибка')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]
    list_display = ['title', 'image', 'text', 'published_at']
    ordering = ['-published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
