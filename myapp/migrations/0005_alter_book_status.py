
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_nos_book_no_of_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='C', max_length=2),
        ),
    ]
