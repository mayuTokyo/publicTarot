# Generated by Django 3.0.4 on 2022-07-13 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.IntegerField(default=-1)),
                ('content', models.TextField(max_length=1000)),
                ('point', models.IntegerField(default=-1)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('card1', models.IntegerField(default=-1)),
                ('card2', models.IntegerField(default=-1)),
                ('card3', models.IntegerField(default=-1)),
                ('card4', models.IntegerField(default=-1)),
                ('card5', models.IntegerField(default=-1)),
                ('card6', models.IntegerField(default=-1)),
                ('card7', models.IntegerField(default=-1)),
                ('card8', models.IntegerField(default=-1)),
                ('card9', models.IntegerField(default=-1)),
                ('card10', models.IntegerField(default=-1)),
                ('card11', models.IntegerField(default=-1)),
                ('card12', models.IntegerField(default=-1)),
                ('card13', models.IntegerField(default=-1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
