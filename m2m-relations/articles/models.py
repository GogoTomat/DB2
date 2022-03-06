from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class scope(models.Model):
    tag_name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    titles = models.ManyToManyField(Article, related_name='scopes')

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

    def __str__(self):
        return self.tag_name


class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='is_main')
    scope = models.ForeignKey(scope, on_delete=models.CASCADE, related_name='is_main')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.is_main}'