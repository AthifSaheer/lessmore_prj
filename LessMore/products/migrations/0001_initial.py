# Generated by Django 3.1.1 on 2020-10-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('brand', models.CharField(max_length=50)),
                ('offer_upto', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('sub_brand', models.CharField(max_length=50)),
                ('add_to_cart', models.BooleanField(default=False)),
                ('buy_now', models.BooleanField(default=False)),
            ],
        ),
    ]