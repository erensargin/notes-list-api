from rest_framework import serializers

from projeler_api import models



class PersonelSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Personel
        fields=('id','personel_adi')


class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = (
            'id','bolge','kod',
        )


class ProjectDetailSerializer(serializers.ModelSerializer):
    proje_personeli=PersonelSerializer(many=True)

    class Meta:
        model=models.Project
        fields=(
            'id','proje_adi','bolge','proje_muduru','kod','proje_personeli',
        )