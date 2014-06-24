from modeltranslation.translator import translator, TranslationOptions
from news.models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
    required_languages = ('en', 'fa')

translator.register(News, NewsTranslationOptions)
