# data_input/serializers.py
from rest_framework import serializers
from .models import (
    BasicTusi,
    BasicXiajing,
    BasicZhiguan,
    BasicZhudi,
    RelationshipTusi,
    RelationshipXiajing,
    RelationshipZhiguan,
    RelationshipZhudi
)

TUSI_TYPE_CHOICES = (
    ('土弁', '土弁'),
    ('土府', '土府'),
    ('土屯', '土屯'),
    ('土县', '土县'),
    ('土巡检', '土巡检'),
    ('土州', '土州'),
    ('长官司', '长官司'),
    ('宣慰使司', '宣慰使司'),
    ('宣抚使司', '宣抚使司'),
    ('安抚使司', '安抚使司'),
    ('招讨使司', '招讨使司'),
    ('指挥使司', '指挥使司'),
)

ZHIGUAN_TYPE_CHOICES = (
    ('土百户', '土百户'),
    ('土千户', '土千户'),
    ('长官', '长官'),
    ('副长官', '副长官'),
    ('指挥使', '指挥使'),
    ('指挥同知', '指挥同知'),
    ('指挥佥事', '指挥佥事'),
)

GENDER_CHOICES = (
    ('男', '男'),
    ('女', '女'),
)

TUSI_RELATIONSHIP_CHOICES = (
    ('所辖','所辖'),
    ('变更','变更'),
    ('拆分','拆分'),
)

XIAJING_RELATIONSHIP_CHOICES = (
    ('扩张','扩张'),
    ('缩小','缩小'),
    ('变更','变更'),
)

ZHIGUAN_RELATIONSHIP_CHOICES = (
    ('父子', '父子'),
    ('兄弟', '兄弟'),
    ('叔侄', '叔侄'),
    ('表兄弟', '表兄弟'),
    ('夫妻', '夫妻'),
    ('母子', '母子'),
    ('母女', '母女'),
    ('父女', '父女'),
    ('爷孙', '爷孙'),
)

ZHUDI_RELATIONSHIP_CHOICES = (
    ('迁移','迁移'),
    ('更名','更名'),
)

# --- 序列化器精确修改 ---

class BasicTusiSerializer(serializers.ModelSerializer):
    tusi_type = serializers.ChoiceField(choices=TUSI_TYPE_CHOICES)

    # 显式定义所有可以为空的字段，并设置 allow_blank=True
    start_date_1 = serializers.CharField(required=False, allow_blank=True)
    start_date_2 = serializers.CharField(required=False, allow_blank=True)
    start_date_3 = serializers.CharField(required=False, allow_blank=True)
    start_date_4 = serializers.IntegerField(required=False, allow_null=True)
    end_date_1 = serializers.CharField(required=False, allow_blank=True)
    end_date_2 = serializers.CharField(required=False, allow_blank=True)
    end_date_3 = serializers.CharField(required=False, allow_blank=True)
    end_date_4 = serializers.IntegerField(required=False, allow_null=True)
    end_reason = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = BasicTusi
        fields = [
            'tusi_id', 'tusi_name', 'tusi_type', 'start_date_1', 'start_date_2',
            'start_date_3', 'start_date_4', 'end_date_1', 'end_date_2',
            'end_date_3', 'end_date_4', 'end_reason', 'belong_state', 'author'
        ]
        read_only_fields = ('author',)

class BasicXiajingSerializer(serializers.ModelSerializer):
    xiajing_text = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = BasicXiajing
        fields = ['xiajing_id', 'tusi', 'xiajing_text', 'author']
        read_only_fields = ('author',)


class BasicZhiguanSerializer(serializers.ModelSerializer):
    zhiguan_type = serializers.ChoiceField(choices=ZHIGUAN_TYPE_CHOICES)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)

    # 显式定义所有可以为空的日期字段，并设置允许为空的选项
    birth_date_1 = serializers.CharField(required=False, allow_blank=True)
    birth_date_2 = serializers.CharField(required=False, allow_blank=True)
    birth_date_3 = serializers.CharField(required=False, allow_blank=True)
    birth_date_4 = serializers.IntegerField(required=False, allow_null=True)
    start_date_1 = serializers.CharField(required=False, allow_blank=True)
    start_date_2 = serializers.CharField(required=False, allow_blank=True)
    start_date_3 = serializers.CharField(required=False, allow_blank=True)
    start_date_4 = serializers.IntegerField(required=False, allow_null=True)
    end_date_1 = serializers.CharField(required=False, allow_blank=True)
    end_date_2 = serializers.CharField(required=False, allow_blank=True)
    end_date_3 = serializers.CharField(required=False, allow_blank=True)
    end_date_4 = serializers.IntegerField(required=False, allow_null=True)
    death_date_1 = serializers.CharField(required=False, allow_blank=True)
    death_date_2 = serializers.CharField(required=False, allow_blank=True)
    death_date_3 = serializers.CharField(required=False, allow_blank=True)
    death_date_4 = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = BasicZhiguan
        fields = [
            'zhiguan_id', 'zhiguan_name', 'zhiguan_type', 'gender',
            'birth_date_1', 'birth_date_2', 'birth_date_3', 'birth_date_4',
            'start_date_1', 'start_date_2', 'start_date_3', 'start_date_4',
            'end_date_1', 'end_date_2', 'end_date_3', 'end_date_4',
            'death_date_1', 'death_date_2', 'death_date_3', 'death_date_4',
            'tusi', 'author'
        ]
        read_only_fields = ('author',)

class BasicZhudiSerializer(serializers.ModelSerializer):
    # 显式定义所有可以为空的日期字段，并设置允许为空的选项
    start_date_1 = serializers.CharField(required=False, allow_blank=True)
    start_date_2 = serializers.CharField(required=False, allow_blank=True)
    start_date_3 = serializers.CharField(required=False, allow_blank=True)
    start_date_4 = serializers.IntegerField(required=False, allow_null=True)
    end_date_1 = serializers.CharField(required=False, allow_blank=True)
    end_date_2 = serializers.CharField(required=False, allow_blank=True)
    end_date_3 = serializers.CharField(required=False, allow_blank=True)
    end_date_4 = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = BasicZhudi
        fields = [
            'zhudi_id', 'zhudi_name', 'tusi', 'start_date_1', 'start_date_2',
            'start_date_3', 'start_date_4', 'end_date_1', 'end_date_2',
            'end_date_3', 'end_date_4', 'location', 'author'
        ]
        read_only_fields = ('author',)

class RelationshipTusiSerializer(serializers.ModelSerializer):
    relationship = serializers.ChoiceField(choices=TUSI_RELATIONSHIP_CHOICES)
    class Meta:
        model = RelationshipTusi
        fields = ['tusi_relationship_id', 'from_tusi', 'to_tusi', 'relationship', 'author']
        read_only_fields = ('author',)

class RelationshipXiajingSerializer(serializers.ModelSerializer):
    relationship_type = serializers.ChoiceField(choices=XIAJING_RELATIONSHIP_CHOICES)
    class Meta:
        model = RelationshipXiajing
        fields = ['xiajing_relationship_id', 'from_xiajing', 'to_xiajing', 'relationship_type', 'belong_tusi', 'author']
        read_only_fields = ('author',)

class RelationshipZhiguanSerializer(serializers.ModelSerializer):
    relationship_type = serializers.ChoiceField(choices=ZHIGUAN_RELATIONSHIP_CHOICES)
    class Meta:
        model = RelationshipZhiguan
        fields = ['zhiguan_relationship_id', 'from_zhiguan', 'to_zhiguan', 'relationship_type', 'belong_tusi', 'author']
        read_only_fields = ('author',)

class RelationshipZhudiSerializer(serializers.ModelSerializer):
    relationship_type = serializers.ChoiceField(choices=ZHUDI_RELATIONSHIP_CHOICES)
    class Meta:
        model = RelationshipZhudi
        fields = ['zhudi_relationship_id', 'from_zhudi', 'to_zhudi', 'relationship_type', 'belong_tusi', 'author']
        read_only_fields = ('author',)