# Generated by Django 4.0.1 on 2022-01-09 22:18

from django.db import migrations, models
import django.db.models.deletion
import lib.postaladdress.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_code', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='codice nazione')),
            ],
            options={
                'verbose_name': 'nazione',
                'verbose_name_plural': 'nazioni',
                'ordering': ['country_code'],
            },
        ),
        migrations.CreateModel(
            name='PostalAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=5, validators=[lib.postaladdress.validators.validate_zip_code], verbose_name='codice postale')),
                ('street', models.CharField(max_length=100, verbose_name='strada')),
                ('adm_level_1', models.CharField(blank=True, max_length=100, verbose_name='livello amministrativo 1')),
                ('adm_level_2', models.CharField(blank=True, max_length=100, verbose_name='livello amministrativo 2')),
                ('adm_level_3', models.CharField(blank=True, max_length=100, verbose_name='livello amministrativo 3')),
                ('adm_level_4', models.CharField(blank=True, max_length=100, verbose_name='livello amministrativo 4')),
                ('adm_level_5', models.CharField(blank=True, max_length=100, verbose_name='livello amministrativo 5')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postaladdress.country', verbose_name='nazione')),
            ],
            options={
                'verbose_name': 'indirizzo postale',
                'verbose_name_plural': 'indirizzi postali',
            },
        ),
        migrations.CreateModel(
            name='CountryAdminLevelMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrative_level_1_mandatory', models.BooleanField(verbose_name='adm. Lvl. 1 mandatory')),
                ('administrative_level_1_endonym', models.CharField(blank=True, max_length=50, null=True, verbose_name='adm. Lvl. 1 endonym')),
                ('administrative_level_2_mandatory', models.BooleanField(verbose_name='adm. Lvl. 2 mandatory')),
                ('administrative_level_2_endonym', models.CharField(blank=True, max_length=50, null=True, verbose_name='adm. Lvl. 2 endonym')),
                ('administrative_level_3_mandatory', models.BooleanField(verbose_name='adm. Lvl. 3 mandatory')),
                ('administrative_level_3_endonym', models.CharField(blank=True, max_length=50, null=True, verbose_name='adm. Lvl. 3 endonym')),
                ('administrative_level_4_mandatory', models.BooleanField(verbose_name='adm. Lvl. 4 mandatory')),
                ('administrative_level_4_endonym', models.CharField(blank=True, max_length=50, null=True, verbose_name='adm. Lvl. 4 endonym')),
                ('administrative_level_5_mandatory', models.BooleanField(verbose_name='adm. Lvl. 5 mandatory')),
                ('administrative_level_5_endonym', models.CharField(blank=True, max_length=50, null=True, verbose_name='adm. Lvl. 5 endonym')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postaladdress.country')),
            ],
            options={
                'ordering': ['country'],
            },
        ),
    ]
