# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table('core_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Image'])

        # Adding model 'Page'
        db.create_table('core_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Page'])

        # Adding M2M table for field images on 'Page'
        db.create_table('core_page_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['core.page'], null=False)),
            ('image', models.ForeignKey(orm['core.image'], null=False))
        ))
        db.create_unique('core_page_images', ['page_id', 'image_id'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('core_image')

        # Deleting model 'Page'
        db.delete_table('core_page')

        # Removing M2M table for field images on 'Page'
        db.delete_table('core_page_images')


    models = {
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.page': {
            'Meta': {'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Image']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']