# Generated by Django 4.1.4 on 2023-04-13 20:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floorplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('length', models.DecimalField(decimal_places=8, max_digits=16)),
                ('width', models.DecimalField(decimal_places=8, max_digits=16)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('X1', models.DecimalField(decimal_places=8, max_digits=16)),
                ('X2', models.DecimalField(decimal_places=8, max_digits=16)),
                ('Y1', models.DecimalField(decimal_places=8, max_digits=16)),
                ('Y2', models.DecimalField(decimal_places=8, max_digits=16)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x1', models.DecimalField(decimal_places=8, max_digits=16)),
                ('y1', models.DecimalField(decimal_places=8, max_digits=16)),
                ('label', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x1', models.DecimalField(decimal_places=8, max_digits=16)),
                ('y1', models.DecimalField(decimal_places=8, max_digits=16)),
                ('x2', models.DecimalField(decimal_places=8, max_digits=16)),
                ('y2', models.DecimalField(decimal_places=8, max_digits=16)),
                ('x3', models.DecimalField(decimal_places=8, max_digits=16)),
                ('y3', models.DecimalField(decimal_places=8, max_digits=16)),
                ('x4', models.DecimalField(decimal_places=8, max_digits=16)),
                ('y4', models.DecimalField(decimal_places=8, max_digits=16)),
                ('type', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500, unique=True)),
                ('password', models.CharField(max_length=500)),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('floorplans', models.ManyToManyField(to='api.floorplan')),
            ],
        ),
        migrations.AddField(
            model_name='floorplan',
            name='joins',
            field=models.ManyToManyField(to='api.join'),
        ),
        migrations.AddField(
            model_name='floorplan',
            name='labels',
            field=models.ManyToManyField(to='api.label'),
        ),
        migrations.AddField(
            model_name='floorplan',
            name='rooms',
            field=models.ManyToManyField(to='api.rooms'),
        ),
    ]
