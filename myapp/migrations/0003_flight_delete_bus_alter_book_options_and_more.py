
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_book_options_alter_bus_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('dest', models.CharField(max_length=30)),
                ('no_of_seats', models.DecimalField(decimal_places=0, max_digits=2)),
                ('remaining_seats', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'List of Flights',
            },
        ),
        migrations.DeleteModel(
            name='Bus',
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'List of Bookings'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='busid',
            new_name='flight_id',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='bus_name',
            new_name='flight_name',
        ),
    ]
