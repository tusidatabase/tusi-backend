# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BasicTusi(models.Model):
    tusi_id = models.IntegerField(primary_key=True, db_comment='土司编号')
    tusi_name = models.CharField(unique=True, max_length=255, db_comment='土司中文名字')
    tusi_type = models.CharField(max_length=4, db_collation='utf8mb4_0900_ai_ci', db_comment='土司类型')
    start_date_1 = models.CharField(max_length=255, blank=True, null=True, db_comment='土司成立时间（朝代）')
    start_date_2 = models.CharField(max_length=255, blank=True, null=True, db_comment='土司成立时间(年号）')
    start_date_3 = models.CharField(max_length=255, blank=True, null=True, db_comment='土司成立时间(具体年份-中文）')
    start_date_4 = models.IntegerField(blank=True, null=True, db_comment='土司成立时间(数字时间）')
    end_date_1 = models.CharField(max_length=255, blank=True, null=True, db_comment='土司废除时间（朝代）')
    end_date_2 = models.CharField(max_length=255, blank=True, null=True, db_comment='土司废除时间（年号）')
    end_date_3 = models.CharField(max_length=255, blank=True, null=True, db_comment='土司废除时间（具体年份-中文）')
    end_date_4 = models.IntegerField(blank=True, null=True, db_comment='土司废除时间（数字时间）')
    end_reason = models.CharField(max_length=255, blank=True, null=True, db_comment='土司废除的原因')
    belong_state = models.CharField(max_length=255, db_comment='土司上属行政区划')
    author = models.CharField(max_length=255, db_comment='作者')

    class Meta:
        db_table = 'basic_tusi'
        db_table_comment = '土司基础信息'


class BasicXiajing(models.Model):
    xiajing_id = models.IntegerField(primary_key=True, db_comment='土司辖境释文编号')
    tusi = models.ForeignKey(BasicTusi, models.DO_NOTHING, db_comment='所属土司编号')
    xiajing_text = models.TextField(db_comment='辖境释文编号')

    class Meta:
        db_table = 'basic_xiajing'
        db_table_comment = '土司辖境范围'


class BasicZhiguan(models.Model):
    zhiguan_id = models.IntegerField(primary_key=True, db_comment='土司职官编号')
    zhiguan_name = models.CharField(unique=True, max_length=255, db_comment='就任土司人员名字')
    zhiguan_type = models.CharField(max_length=4, db_comment='土司职官类型')
    gender = models.CharField(max_length=1, db_comment='土司人员性别')
    birth_date_1 = models.CharField(max_length=255, blank=True, null=True, db_comment='出生时间（朝代）')
    birth_date_2 = models.CharField(max_length=255, blank=True, null=True, db_comment='出生时间(年号）')
    birth_date_3 = models.CharField(max_length=255, blank=True, null=True, db_comment='出生时间(具体年份-中文）')
    birth_date_4 = models.IntegerField(blank=True, null=True, db_comment='出生时间(数字时间）')
    start_date_1 = models.CharField(max_length=255, blank=True, null=True, db_comment='就职时间（朝代）')
    start_date_2 = models.CharField(max_length=255, blank=True, null=True, db_comment='就职时间(年号）')
    start_date_3 = models.CharField(max_length=255, blank=True, null=True, db_comment='就职时间(具体年份-中文）')
    start_date_4 = models.IntegerField(blank=True, null=True, db_comment='就职时间(数字时间）')
    end_date_1 = models.CharField(max_length=255, blank=True, null=True, db_comment='卸任时间（朝代）')
    end_date_2 = models.CharField(max_length=255, blank=True, null=True, db_comment='卸任时间(年号）')
    end_date_3 = models.CharField(max_length=255, blank=True, null=True, db_comment='卸任时间(具体年份）')
    end_date_4 = models.IntegerField(blank=True, null=True, db_comment='卸任时间(数字时间）')
    death_date_1 = models.CharField(max_length=255, blank=True, null=True, db_comment='死亡时间（朝代）')
    death_date_2 = models.CharField(max_length=255, blank=True, null=True, db_comment='死亡时间(年号）')
    death_date_3 = models.CharField(max_length=255, blank=True, null=True, db_comment='死亡时间(具体年份-中文）')
    death_date_4 = models.IntegerField(blank=True, null=True, db_comment='死亡时间(数字时间）')
    tusi = models.ForeignKey(BasicTusi, models.DO_NOTHING, db_comment='就任土司')
    author = models.CharField(max_length=255, db_comment='作者')

    class Meta:
        db_table = 'basic_zhiguan'
        db_table_comment = '土司职官信息'


class BasicZhudi(models.Model):
    zhudi_id = models.IntegerField(primary_key=True, db_comment='土司驻地编号')
    zhudi_name = models.CharField(unique=True, max_length=255, db_comment='土司地点名称')
    tusi = models.ForeignKey(BasicTusi, models.DO_NOTHING, db_comment='所属土司编号')
    start_date_1 = models.CharField(max_length=255, blank=True, null=True, db_comment='驻地设立时间（朝代）')
    start_date_2 = models.CharField(max_length=255, blank=True, null=True, db_comment='驻地设立时间（年号）')
    start_date_3 = models.CharField(max_length=255, blank=True, null=True, db_comment='驻地设立时间（具体年份-中文）')
    start_date_4 = models.IntegerField(blank=True, null=True, db_comment='驻地设立时间（数字时间）')
    end_date_1 = models.CharField(max_length=255, blank=True, null=True, db_comment='驻地撤销时间（朝代）')
    end_date_2 = models.CharField(max_length=255, blank=True, null=True, db_comment='驻地撤销时间（年号）')
    end_date_3 = models.CharField(max_length=255, blank=True, null=True, db_comment='驻地撤销时间（具体年份-中文）')
    end_date_4 = models.IntegerField(blank=True, null=True, db_comment='驻地撤销时间（数字时间）')
    location = models.CharField(max_length=255, db_comment='驻地所在地区（精确到府）')
    author = models.CharField(max_length=255, db_comment='作者')

    class Meta:
        db_table = 'basic_zhudi'
        db_table_comment = '土司驻地的相关信息'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RelationshipTusi(models.Model):
    tusi_relationship_id = models.IntegerField(primary_key=True, db_comment='土司关系编号')
    from_tusi = models.ForeignKey(BasicTusi, models.DO_NOTHING, db_comment='土司编号1')
    to_tusi = models.ForeignKey(BasicTusi, models.DO_NOTHING, related_name='relationshiptusi_to_tusi_set', db_comment='土司编号2')
    relationship = models.CharField(max_length=2, db_comment='土司关系')
    author = models.CharField(max_length=255, db_comment='作者')

    class Meta:
        db_table = 'relationship_tusi'
        db_table_comment = '土司相互关系表'


class RelationshipXiajing(models.Model):
    xiajing_relationship_id = models.IntegerField(primary_key=True, db_comment='辖境关系编号')
    from_xiajing = models.ForeignKey(BasicZhudi, models.DO_NOTHING, db_comment='辖境编号1')
    to_xiajing = models.ForeignKey(BasicZhudi, models.DO_NOTHING, related_name='relationshipxiajing_to_xiajing_set', db_comment='辖境编号2')
    relationship_type = models.CharField(max_length=2, db_comment='辖境关系类型')
    belong_tusi = models.ForeignKey(BasicTusi, models.DO_NOTHING, db_comment='所属土司编号')
    author = models.CharField(max_length=255, db_comment='作者')

    class Meta:
        db_table = 'relationship_xiajing'
        db_table_comment = '土司辖境关系表'


class RelationshipZhiguan(models.Model):
    zhiguan_relationship_id = models.IntegerField(primary_key=True, db_comment='职官关系编号')
    from_zhiguan = models.ForeignKey(BasicZhiguan, models.DO_NOTHING, db_comment='职官编号1')
    to_zhiguan = models.ForeignKey(BasicZhiguan, models.DO_NOTHING, related_name='relationshipzhiguan_to_zhiguan_set', db_comment='职官编号2')
    relationship_type = models.CharField(max_length=3, db_comment='关系类型')
    belong_tusi = models.ForeignKey(BasicTusi, models.DO_NOTHING, db_comment='所属土司编号')
    author = models.CharField(max_length=255, db_comment='作者')

    class Meta:
        db_table = 'relationship_zhiguan'
        db_table_comment = '土司职官关系表'


class RelationshipZhudi(models.Model):
    zhudi_relationship_id = models.IntegerField(primary_key=True, db_comment='土司驻地关系编号')
    from_zhudi = models.ForeignKey(BasicZhudi, models.DO_NOTHING, db_comment='土司驻地编号1')
    to_zhudi = models.ForeignKey(BasicZhudi, models.DO_NOTHING, related_name='relationshipzhudi_to_zhudi_set', db_comment='土司驻地编号2')
    relationship_type = models.CharField(max_length=2, db_comment='关系类型')
    belong_tusi = models.ForeignKey(BasicTusi, models.DO_NOTHING, db_comment='所属土司编号')
    author = models.CharField(max_length=255, db_comment='作者')

    class Meta:
        db_table = 'relationship_zhudi'
        db_table_comment = '土司驻地关系'
