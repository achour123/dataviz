# Generated by Django 3.1.1 on 2020-09-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('localisation', models.CharField(choices=[('Tunis', 'Tunis'), ('Ariana', 'Ariana'), ('Ben Arous', 'Ben Arous'), ('Manouba', 'Manouba'), ('Nabeul', 'Nabeul'), ('Bizert', 'Bizert'), ('Zaghouan', 'Zaghouan'), ('Sousse', 'Sousse'), ('Monastir', 'Monastir'), ('Mahdia', 'Mahdia'), ('Sfax', 'Sfax'), ('Beja', 'Beja'), ('Jendouba', 'Jendouba'), ('El_kef', 'El kef'), ('Seliana', 'Seliana'), ('Kairouane', 'Kairouane'), ('Sidi_Bouzid', 'Sidi Bouzid'), ('Kasserine', 'Kasserine'), ('Gabes', 'Gabes'), ('Medenine', 'Medenine'), ('Gafsa', 'Gafsa'), ('Tozeur', 'Tozeur'), ('Tataouine', 'Tataouine'), ('kébili', 'kébili')], max_length=30)),
            ],
        ),
    ]
