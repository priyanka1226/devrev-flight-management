
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_flight_delete_bus_alter_book_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='nos',
            new_name='no_of_seats',
        ),
    ]
