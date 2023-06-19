# Generated by Django 4.1.2 on 2023-04-28 08:12

from django.db import migrations, models
import simplepro.editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_alter_tracertresult_delays"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyContent",
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
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="标题"
                    ),
                ),
                (
                    "key_words",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="关键字"
                    ),
                ),
                (
                    "sort",
                    models.CharField(
                        blank=True,
                        default="中药",
                        max_length=50,
                        null=True,
                        verbose_name="类别",
                    ),
                ),
                (
                    "summary",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="摘要"
                    ),
                ),
                (
                    "cover",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="图1"
                    ),
                ),
                (
                    "cover2",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="图2"
                    ),
                ),
                (
                    "cover3",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="图3"
                    ),
                ),
                (
                    "cover4",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="图4"
                    ),
                ),
                (
                    "cover5",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="图5"
                    ),
                ),
                (
                    "cover6",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="图6"
                    ),
                ),
                (
                    "cover7",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="图7"
                    ),
                ),
                (
                    "html",
                    simplepro.editor.fields.UETextField(
                        help_text="实体内容（富文本）",
                        max_length=65535,
                        null=True,
                        verbose_name="实体内容",
                    ),
                ),
                (
                    "release_time",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="发布时间"
                    ),
                ),
                (
                    "update_time",
                    models.DateField(auto_now=True, null=True, verbose_name="更新日期"),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "隐藏"), (1, "正常")], default=1, verbose_name="实体状态"
                    ),
                ),
            ],
            options={"verbose_name": "本草实体", "verbose_name_plural": "本草实体",},
        ),
    ]