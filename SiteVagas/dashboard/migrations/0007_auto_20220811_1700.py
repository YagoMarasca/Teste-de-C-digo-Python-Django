# Generated by Django 3.2.15 on 2022-08-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20220811_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricoesvagas',
            name='pretensao_salarial',
            field=models.CharField(choices=[('Até 1.000', 'Até 1.000'), ('De 1.000 até 2.000', 'De 1.000 até 2.000'), ('De 2.000 até 3.000', 'De 2.000 até 3.000'), ('Acima de 3.000', 'Acima de 3.000')], max_length=20),
        ),
        migrations.AlterField(
            model_name='inscricoesvagas',
            name='ultima_escolaridade',
            field=models.CharField(choices=[('Ensino Fundamental', 'Ensino Fundamental'), ('Ensino Médio', 'Ensino Médio'), ('Tecnólogo', 'Tecnólogo'), ('Ensino Superior', 'Ensino Superior'), ('Pós/MBA/Mestrado', 'Pós/MBA/Mestrado'), ('Doutorado', 'Doutorado')], max_length=19),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='escolaridade_minima',
            field=models.CharField(choices=[('Ensino Fundamental', 'Ensino Fundamental'), ('Ensino Médio', 'Ensino Médio'), ('Tecnólogo', 'Tecnólogo'), ('Ensino Superior', 'Ensino Superior'), ('Pós/MBA/Mestrado', 'Pós/MBA/Mestrado'), ('Doutorado', 'Doutorado')], default='', max_length=19),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='salario',
            field=models.CharField(choices=[('Até 1.000', 'Até 1.000'), ('De 1.000 até 2.000', 'De 1.000 até 2.000'), ('De 2.000 até 3.000', 'De 2.000 até 3.000'), ('Acima de 3.000', 'Acima de 3.000')], max_length=20),
        ),
    ]