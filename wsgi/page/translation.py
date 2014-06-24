from modeltranslation.translator import translator, TranslationOptions
from page.models import Page, FirstPage


class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
    required_languages = ('en', 'fa')


class FirstPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
    required_languages = ('en', 'fa')


translator.register(Page, PageTranslationOptions)
translator.register(FirstPage, FirstPageTranslationOptions)
