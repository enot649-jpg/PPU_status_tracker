from django.db import models

class Units(models.Model):
    unit = models.CharField(
    max_length = 128,
    verbose_name='Подразделение'
    )

    class Meta:
        verbose_name = 'Подразделения'

    def __str__(self):
        return self.unit


class Departure(models.Model):
    departure = models.CharField(
    max_length = 128,
    verbose_name='Департамент'
    )

    class Meta:
        verbose_name = 'Департамент'
    

    def __str__(self):
        return self.departure


class Act(models.Model):
    needs_act = models.CharField(
    max_length = 128,
    verbose_name='Необходимо Актуализировать',
    )

    class Meta:
        verbose_name = 'Необходимо актуализировать'
    

    def __str__(self):
        return self.needs_act

class History(models.Model):
    date = models.DateTimeField(
    auto_now_add=True,
    auto_now=False,
    verbose_name='Время Изменения',
    )
    status = models.CharField(
    max_length = 128,
    verbose_name='Предыдущий статус',
    help_text='Текущий статус мероприятия, не более 128 символов',
    )
    payed = models.FloatField(
    default=0,
    verbose_name='Оплачено',
    )
    name = models.ForeignKey(
    'Sogl',
    on_delete = models.CASCADE,
    related_name='history',
    )

    class Meta:
        verbose_name = 'История'
        ordering = ('-date',)


class BaseModel(models.Model):
    name = models.CharField(
    default='-',
    max_length = 128,
    verbose_name='Наименование',
    help_text='Название мероприятия, не более 128 символов',
    )
    modified_at = models.DateTimeField(
    auto_now_add=False,
    auto_now=True,
    verbose_name='Время Изменения',
    )
    meropr = models.CharField(
    default='-',
    max_length = 128,
    verbose_name='Номер Мероприятия',
    help_text='Номер мероприятия, не более 128 символов',
    )
    dogovor = models.CharField(
    default='-',
    max_length = 128,
    verbose_name='Номер Договора',
    help_text='Номер Договора, не более 128 символов',
    )
    value = models.FloatField(
    default=0,
    verbose_name='Стоимость',
    )
    payed = models.FloatField(
    default=0,
    verbose_name='Оплачено',
    )
    status = models.CharField(
    default= '-',
    max_length = 128,
    verbose_name='Текущий статус',
    help_text='Текущий статус мероприятия, не более 128 символов',
    )
    unit = models.ForeignKey(
    'Units',
    on_delete = models.CASCADE,
    verbose_name='Подразделение',
    )
    group = models.CharField(
    default= '-',
    max_length = 128,
    verbose_name='Группа мероприятий',
    help_text='Группа мероприятий (аналогично наименованию), справочно для детализации, не более 128 символов',
    )
    departure = models.ForeignKey(
    'Departure',
    on_delete = models.CASCADE,
    verbose_name='Депратамент',
    )
    needs_act = models.ForeignKey(
    'Act',
    on_delete = models.CASCADE, 
    null=True, 
    blank=True,
    verbose_name='Необходимо актуализировать',
    )

    class Meta:
        ordering = ('id',)
        abstract = True

    def __str__(self):
        return self.name


class Sogl(BaseModel):

    class Meta:
        verbose_name = 'Согласованные'







