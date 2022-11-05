# Generated by Django 3.2.13 on 2022-11-06 02:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('grade', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('tag', multiselectfield.db.fields.MultiSelectField(choices=[(1, '#별 보기 좋은'), (2, '#시원한 여름'), (3, '#파티가 있는'), (4, '#가족이랑'), (5, '#커플'), (6, '#조용한'), (7, '#애견동반'), (8, '#도심 속 캠핑장'), (9, '#풍경이 좋은'), (10, '#2030인기'), (11, '#바다가 보이는')], max_length=23)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
