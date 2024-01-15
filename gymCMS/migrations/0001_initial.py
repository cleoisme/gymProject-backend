# Generated by Django 4.2.7 on 2024-01-14 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("street", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("province", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="AppointmentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Promotion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=255)),
                ("discount", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("is_admin", models.BooleanField()),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("gender", models.CharField(default="Unknown", max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("birth_date", models.DateTimeField(null=True)),
                (
                    "address",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        primary_key=True,
                        serialize=False,
                        to="gymCMS.address",
                    ),
                ),
                (
                    "membership",
                    models.CharField(
                        choices=[("B", "Bronze"), ("S", "Silver"), ("G", "Gold")],
                        default="B",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(default="Default Subject", max_length=255),
                ),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_update", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="gymCMS.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=255, null=True)),
                ("description", models.TextField()),
                ("last_update", models.DateTimeField(auto_now=True)),
                ("start_datetime", models.DateTimeField()),
                ("end_datetime", models.DateTimeField()),
                (
                    "appointment_type",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="gymCMS.appointmenttype",
                    ),
                ),
                (
                    "promotions",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="appointments",
                        to="gymCMS.promotion",
                    ),
                ),
                (
                    "trainee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="trainee_appointments",
                        to="gymCMS.user",
                    ),
                ),
                (
                    "trainer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="trainer_appointments",
                        to="gymCMS.user",
                    ),
                ),
            ],
        ),
    ]
