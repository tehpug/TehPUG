from modeltranslation.translator import translator, TranslationOptions
from projects.models import Project, Repository


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'version', 'license', 'desc')
    required_languages = ('en', 'fa')


class RepositoryPageTranslationOptions(TranslationOptions):
    fields = ('address',)
    required_languages = ('en', 'fa')


translator.register(Project, ProjectTranslationOptions)
translator.register(Repository, RepositoryPageTranslationOptions)
