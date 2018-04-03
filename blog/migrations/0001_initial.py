# Generated by Django 2.0.3 on 2018-04-03 16:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='広告名')),
                ('html', models.TextField(blank=True, verbose_name='広告HTML')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='アナリティクス')),
                ('html', models.TextField(blank=True, verbose_name='アナリティクスHTML')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリ名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名無し', max_length=255, verbose_name='名前')),
                ('text', models.TextField(verbose_name='コメント')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='com_icon/', verbose_name='サムネイル')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('src', models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='ファイル')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(help_text='送信後、一度保存してください。', upload_to='uploads/%Y/%m/%d/', verbose_name='画像')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='リンク名')),
                ('adrs', models.CharField(max_length=255, verbose_name='アドレス')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='PopularPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('page_view', models.IntegerField(verbose_name='ページビュー数')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='本文')),
                ('thumnail', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='サムネイル')),
                ('is_publick', models.BooleanField(default=True, verbose_name='公開可能か?')),
                ('description', models.TextField(blank=True, verbose_name='記事の説明')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Category', verbose_name='カテゴリ')),
                ('friend_posts', models.ManyToManyField(blank=True, related_name='_post_friend_posts_+', to='blog.Post', verbose_name='関連記事')),
            ],
        ),
        migrations.CreateModel(
            name='ReComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名無し', max_length=255, verbose_name='名前')),
                ('text', models.TextField(verbose_name='コメント')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='com_icon/', verbose_name='サムネイル')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Comment', verbose_name='対象コメント')),
            ],
        ),
        migrations.CreateModel(
            name='SiteDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='サンプルのタイトル', max_length=255, verbose_name='タイトル')),
                ('header_text', models.TextField(default='このブログはDjangoとBootstrap4で作成されました\n[filter url]https://github.com/naritotzawa/django-torina-blog<split>Githubのソースコード[end]', max_length=255, verbose_name='ヘッダーのテキスト')),
                ('description', models.CharField(default='サンプルの説明', max_length=255, verbose_name='サイトの説明')),
                ('author', models.CharField(default='サンプルの管理者', max_length=255, verbose_name='管理者')),
                ('author_mail', models.EmailField(default='your_mail@gmail.com', max_length=255, verbose_name='管理者アドレス')),
                ('color', models.CharField(choices=[('primary', '青色'), ('secondary', '灰色'), ('success', '緑色'), ('info', '水色'), ('warning', '黄色'), ('danger', '赤'), ('dark', '黒')], default='primary', max_length=30, verbose_name='サイトテーマ色')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sites.Site', verbose_name='Site')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='タグ名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='タグ'),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post', verbose_name='記事'),
        ),
        migrations.AddField(
            model_name='file',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post', verbose_name='記事'),
        ),
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='対象記事'),
        ),
    ]
