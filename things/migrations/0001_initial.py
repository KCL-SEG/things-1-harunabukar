from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    
    operations = [
        migrations.CreateModel(
            name='things',
            fields=[
                ('name', models.CharField(max_length=100, unique=True)),
                ('quantity', models.IntegerField()),
                ('description', models.CharField()) 
            ],
            
        ),
    ]

    