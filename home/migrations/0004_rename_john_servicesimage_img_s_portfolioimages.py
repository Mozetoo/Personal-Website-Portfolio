# Generated by Django 4.2.3 on 2023-07-19 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicesimage',
            old_name='john',
            new_name='img_s',
        ),
        migrations.CreateModel(
            name='PortfolioImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_img', models.ImageField(upload_to='images/Portfolio/')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_image', to='home.portfolio')),
            ],
        ),
    ]
