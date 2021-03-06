# Generated by Django 3.2.5 on 2021-07-27 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_auto_20210720_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pybo.question')),
            ],
        ),
    ]
