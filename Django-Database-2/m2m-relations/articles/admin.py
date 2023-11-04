from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_tag_is_main = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count_tag_is_main += 1
        if count_tag_is_main == 0:
            raise ValidationError('Выберите основной тег')
        elif count_tag_is_main >= 2:
            raise ValidationError('Может быть только один основной тег')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', ]
    list_filter = ['published_at']
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
