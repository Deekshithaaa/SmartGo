# Generated by Django 2.2 on 2020-03-10 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=100)),
                ('same_dest', models.CharField(max_length=100)),
                ('par', models.CharField(max_length=100)),
                ('dist', models.CharField(max_length=100)),
                ('sechom', models.CharField(max_length=100)),
                ('ty_sechom', models.CharField(max_length=100)),
                ('of_sechom', models.CharField(max_length=100)),
                ('rea_sechom', models.CharField(max_length=100)),
                ('adv_plan', models.CharField(max_length=100)),
                ('fam_hol', models.CharField(max_length=100)),
                ('worries', models.CharField(max_length=100)),
                ('njoy', models.CharField(max_length=100)),
                ('pet', models.CharField(max_length=100)),
                ('high_cost', models.CharField(max_length=100)),
                ('mul_dest', models.CharField(max_length=100)),
                ('reas', models.CharField(max_length=100)),
                ('trans', models.CharField(max_length=100)),
                ('influ', models.CharField(max_length=100)),
                ('us', models.CharField(max_length=100)),
                ('tim_shr', models.CharField(max_length=100)),
                ('c1', models.CharField(max_length=100)),
                ('c2', models.CharField(max_length=100)),
                ('c3', models.CharField(max_length=100)),
                ('c4', models.CharField(max_length=100)),
                ('p1', models.CharField(max_length=100)),
                ('p2', models.CharField(max_length=100)),
                ('p3', models.CharField(max_length=100)),
                ('p4', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Details',
        ),
    ]
