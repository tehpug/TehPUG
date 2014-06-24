# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Repository.address_fa'
        db.add_column(u'projects_repository', 'address_fa',
                      self.gf('django.db.models.fields.CharField')(max_length=265, null=True),
                      keep_default=False)

        # Adding field 'Repository.address_en'
        db.add_column(u'projects_repository', 'address_en',
                      self.gf('django.db.models.fields.CharField')(max_length=265, null=True),
                      keep_default=False)

        # Adding field 'Project.name_fa'
        db.add_column(u'projects_project', 'name_fa',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True),
                      keep_default=False)

        # Adding field 'Project.name_en'
        db.add_column(u'projects_project', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=64, null=True),
                      keep_default=False)

        # Adding field 'Project.version_fa'
        db.add_column(u'projects_project', 'version_fa',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True),
                      keep_default=False)

        # Adding field 'Project.version_en'
        db.add_column(u'projects_project', 'version_en',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True),
                      keep_default=False)

        # Adding field 'Project.license_fa'
        db.add_column(u'projects_project', 'license_fa',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True),
                      keep_default=False)

        # Adding field 'Project.license_en'
        db.add_column(u'projects_project', 'license_en',
                      self.gf('django.db.models.fields.CharField')(max_length=16, null=True),
                      keep_default=False)

        # Adding field 'Project.desc_fa'
        db.add_column(u'projects_project', 'desc_fa',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'Project.desc_en'
        db.add_column(u'projects_project', 'desc_en',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Repository.address_fa'
        db.delete_column(u'projects_repository', 'address_fa')

        # Deleting field 'Repository.address_en'
        db.delete_column(u'projects_repository', 'address_en')

        # Deleting field 'Project.name_fa'
        db.delete_column(u'projects_project', 'name_fa')

        # Deleting field 'Project.name_en'
        db.delete_column(u'projects_project', 'name_en')

        # Deleting field 'Project.version_fa'
        db.delete_column(u'projects_project', 'version_fa')

        # Deleting field 'Project.version_en'
        db.delete_column(u'projects_project', 'version_en')

        # Deleting field 'Project.license_fa'
        db.delete_column(u'projects_project', 'license_fa')

        # Deleting field 'Project.license_en'
        db.delete_column(u'projects_project', 'license_en')

        # Deleting field 'Project.desc_fa'
        db.delete_column(u'projects_project', 'desc_fa')

        # Deleting field 'Project.desc_en'
        db.delete_column(u'projects_project', 'desc_en')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_en': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'desc_fa': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'downloadlink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'home': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kproject': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'license_en': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'license_fa': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'maintainers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'projects_project_related'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'name_fa': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'vcs': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'version_en': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'version_fa': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '40'})
        },
        u'projects.repository': {
            'Meta': {'object_name': 'Repository'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '265'}),
            'address_en': ('django.db.models.fields.CharField', [], {'max_length': '265', 'null': 'True'}),
            'address_fa': ('django.db.models.fields.CharField', [], {'max_length': '265', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '40'})
        }
    }

    complete_apps = ['projects']