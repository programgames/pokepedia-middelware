# Generated by Django 3.2.23 on 2024-09-04 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pokemon_v2', '0016_typesprites'),
    ]

    operations = [
        migrations.CreateModel(
            name='CacheItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('data', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='PkmAvailabilityForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonMoveAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_default', models.BooleanField(default=True)),
                ('has_pokepedia_page', models.BooleanField(default=True)),
                ('machine', models.BooleanField(default=True)),
                ('level', models.BooleanField(default=True)),
                ('tutor', models.BooleanField(default=True)),
                ('egg', models.BooleanField(default=True)),
                ('forms', models.ManyToManyField(blank=True, related_name='pokemonmoveavailability', to='middleware.PkmAvailabilityForm')),
                ('pokemon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemonmoveavailability', to='pokemon_v2.pokemon')),
                ('version_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemonmoveavailability', to='pokemon_v2.versiongroup')),
            ],
        ),
        migrations.AddField(
            model_name='pkmavailabilityform',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_form', to='middleware.pokemonmoveavailability'),
        ),
        migrations.AddField(
            model_name='pkmavailabilityform',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_form', to='middleware.pokemonmoveavailability'),
        ),
        migrations.AddField(
            model_name='pkmavailabilityform',
            name='version_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_v2.versiongroup'),
        ),
        migrations.CreateModel(
            name='MoveNameChangelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('generation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movenamechangelog', to='pokemon_v2.generation')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movenamechangelog_language', to='pokemon_v2.language')),
                ('move', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movenamechangelog', to='pokemon_v2.move')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movenamechangelog', to='pokemon_v2.type')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='pkmavailabilityform',
            unique_together={('parent', 'child', 'version_group')},
        ),
    ]
