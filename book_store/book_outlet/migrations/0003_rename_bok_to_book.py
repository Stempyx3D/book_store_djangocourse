from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_alter_bok_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bok',
            new_name='Book',
        ),
    ]