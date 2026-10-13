import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bird_counter", "0003_city_location_city"),
    ]

    operations = [
        migrations.CreateModel(
            name="Observer",
            fields=[
                ("badge", models.CharField(max_length=20, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "city",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="observers",
                        to="bird_counter.city",
                    ),
                ),
            ],
        ),
    ]
