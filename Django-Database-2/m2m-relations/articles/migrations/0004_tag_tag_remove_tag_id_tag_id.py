# Generated by Django 4.2.3 on 2023-07-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_scope_is_main_remove_tag_id_remove_tag_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.article'),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='id',
        ),
        migrations.AddField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
