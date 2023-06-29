
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'List of Books'},
        ),
        migrations.AlterModelOptions(
            name='bus',
            options={'verbose_name_plural': 'List of Busses'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'List of Users'},
        ),
    ]
