# Generated by Django 2.2.1 on 2019-05-20 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20190520_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='state',
            field=models.CharField(max_length=256),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('is_moderator', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Card')),
            ],
        ),
    ]