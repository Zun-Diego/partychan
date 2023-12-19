# Generated by Django 4.1.4 on 2023-12-19 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='Votos_en_Contra', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='Votos_a_Favor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_report', models.IntegerField(default=0)),
                ('answer_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.answer')),
            ],
        ),
    ]