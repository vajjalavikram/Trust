# Generated by Django 2.2.3 on 2019-08-31 00:07

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='prefs',
            field=picklefield.fields.PickledObjectField(editable=False, null=True),
        ),
    ]