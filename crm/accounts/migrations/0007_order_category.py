# Generated by Django 4.2.2 on 2023-06-19 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=200, null=True),
        ),
    ]
