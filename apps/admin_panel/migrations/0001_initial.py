# Generated by Django 4.2.2 on 2023-06-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_avatar', models.ImageField(upload_to='category_icons/')),
                ('category_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
