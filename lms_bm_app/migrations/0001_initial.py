# Generated by Django 4.2.13 on 2024-05-16 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.UUIDField(null=True)),
                ('loan_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('loan_type', models.CharField(max_length=20, null=True)),
                ('aadhar_id', models.CharField(max_length=100)),
                ('interest_rate', models.CharField(max_length=10)),
                ('disbursal_date', models.DateTimeField(null=True)),
                ('user_id', models.UUIDField(null=True)),
                ('due_dates', models.JSONField(max_length=100)),
                ('is_cleared', models.BooleanField(default=False)),
                ('principal', models.FloatField()),
                ('amount_paid', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(max_length=10, null=True)),
                ('amount', models.FloatField(null=True)),
                ('aadhar_uuid', models.UUIDField(null=True)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('loan_id', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user_id', models.UUIDField(primary_key=True, serialize=False)),
                ('adhar_uuid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=40)),
                ('email_id', models.CharField(max_length=100)),
                ('annual_income', models.FloatField()),
                ('account_balance', models.FloatField()),
                ('credit_score', models.IntegerField(null=True)),
                ('loan_created_at', models.DateTimeField(null=True)),
                ('is_debt_cleared', models.BooleanField(null=True)),
                ('current_debt', models.FloatField(null=True)),
            ],
        ),
    ]
