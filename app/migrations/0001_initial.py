# Generated by Django 2.0.3 on 2018-05-19 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.BooleanField(default=None, verbose_name='Правильно')),
                ('timeAnswer', models.DateTimeField(default=None, verbose_name='Время когда ответил')),
            ],
            options={
                'verbose_name_plural': 'Ответы пользователя',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('сategorie', models.CharField(default=None, max_length=255, verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='GropUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gropUser', models.CharField(default=None, max_length=255, verbose_name='Группа пользователей')),
            ],
            options={
                'verbose_name_plural': 'Группа пользователей',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(default=None, verbose_name='Ответ')),
                ('boolean', models.BooleanField(default=None, verbose_name='Правильно')),
            ],
            options={
                'verbose_name_plural': 'Варианты ответа',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=None, max_length=255, verbose_name='Ключ')),
                ('expires', models.DateTimeField(default=None, verbose_name='Время сессии')),
            ],
            options={
                'verbose_name_plural': 'Сессия',
            },
        ),
        migrations.CreateModel(
            name='StartTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStartTest', models.DateTimeField(default=None, verbose_name='Время начала теста ')),
                ('timeFinishTest', models.DateTimeField(default=None, null=True, verbose_name='Время завершения теста ')),
                ('rezult', models.IntegerField(default=0, verbose_name='Результат')),
            ],
            options={
                'verbose_name_plural': 'Старт теста',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='Название теста')),
                ('dateStart', models.DateTimeField(default=None, verbose_name='Начало теста')),
                ('fullInfo', models.TextField(default=None, verbose_name='Полная информация')),
                ('shortInfo', models.TextField(default=None, verbose_name='Краткая информация')),
                ('colQuition', models.IntegerField(default=None, verbose_name='Количество вопросов')),
                ('timeTest', models.IntegerField(default=None, verbose_name='Время на прохождение')),
            ],
            options={
                'verbose_name_plural': 'Тест',
            },
        ),
        migrations.CreateModel(
            name='TextQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textQuestion', models.TextField(default=None, verbose_name='Текст вопроса')),
                ('typeQuestion', models.CharField(default=None, max_length=10, verbose_name='Тип вопроса')),
                ('test', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Test', verbose_name='Тест')),
            ],
            options={
                'verbose_name_plural': 'Текст вопроса',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='Имя')),
                ('lastname', models.CharField(default=None, max_length=255, verbose_name='Фамилия')),
                ('login', models.CharField(default=None, max_length=255, verbose_name='Логин')),
                ('password', models.CharField(default=None, max_length=255, verbose_name='Пароль')),
                ('email', models.EmailField(default=None, max_length=255, verbose_name='email')),
            ],
            options={
                'verbose_name_plural': 'Пользователь',
            },
        ),
        migrations.AddField(
            model_name='test',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='test',
            name='gropUser',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.GropUser', verbose_name='Группа пользователей'),
        ),
        migrations.AddField(
            model_name='test',
            name='сategorie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Categorie', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='starttest',
            name='test',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Test', verbose_name='Тест'),
        ),
        migrations.AddField(
            model_name='starttest',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='Кто проходит'),
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.TextQuestion', verbose_name='Текст вопроса'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.Test', verbose_name='Тест'),
        ),
        migrations.AddField(
            model_name='answer',
            name='startTest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StartTest', verbose_name='Старт_тест'),
        ),
    ]
