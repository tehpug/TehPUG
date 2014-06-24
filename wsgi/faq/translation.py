from modeltranslation.translator import translator, TranslationOptions
from faq.models import FAQ


class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
    required_languages = ('en', 'fa')

translator.register(FAQ, FAQTranslationOptions)
