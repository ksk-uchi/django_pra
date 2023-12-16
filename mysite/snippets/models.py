from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_comment="作成日")
    title = models.CharField(max_length=100, blank=True, default="", db_comment="タイトル")
    code = models.TextField(db_comment="コード")
    linenos = models.BooleanField(default=False, db_comment="行番号表示 true:表示/false:非表示")
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python", max_length=100, db_comment="言語名")
    style = models.CharField(
        choices=STYLE_CHOICES,
        default="friendly",
        max_length=100,
        db_comment="ハイライトスタイル",
    )

    class Meta:
        db_table_comment = "コードスニペット"
        ordering = ("created",)
