# Generated by Django 4.0.6 on 2022-07-16 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Btc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=255)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dollar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=255)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Euro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=255)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=255)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_type', models.IntegerField()),
                ('region', models.CharField(max_length=255)),
                ('realestate_type', models.IntegerField()),
                ('period', models.IntegerField()),
                ('relation', models.IntegerField()),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('price', models.CharField(max_length=255)),
                ('img_src', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('real_estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.realestate')),
            ],
        ),
        migrations.AddField(
            model_name='realestate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.realestateowner'),
        ),
        migrations.CreateModel(
            name='PriceStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=255)),
                ('dt', models.DateField(auto_now_add=True)),
                ('real_estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.realestate')),
            ],
        ),
        migrations.CreateModel(
            name='FreelanceAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('real_estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.realestate')),
            ],
        ),
        migrations.CreateModel(
            name='AgentInvestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('real_estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.realestate')),
            ],
        ),
        migrations.CreateModel(
            name='AgencyWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agency')),
            ],
        ),
        migrations.AddField(
            model_name='agency',
            name='real_estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.realestate'),
        ),
    ]
