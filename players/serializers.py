from rest_framework import serializers


class PlayersResponseScheduleSerializer(serializers.Serializer):
    Name = serializers.CharField(required=True)
    Nationality = serializers.CharField(required=True)

    def to_representation(self, instance):
        data_dict = super(PlayersResponseScheduleSerializer, self).to_representation(instance)
        response_dict = {}
        for key, value in data_dict.iteritems():
            if value == None or value == "":
                value = "N/A"
            response_dict[key] = value
        return response_dict

class PlayerResponseScheduleSerializer(serializers.Serializer):
    Name = serializers.CharField(required=True)
    Age = serializers.IntegerField(required=True)
    Nationality = serializers.CharField(required=True)
    Club = serializers.CharField(required=True)
    Position = serializers.CharField(source='National_Position',required=True)
    Rating = serializers.IntegerField(required=True)
    Height = serializers.CharField()
    Weight = serializers.CharField()
    Preffered_Foot = serializers.CharField()
    Aggression = serializers.IntegerField()
    Freekick_Accuracy = serializers.IntegerField()
    Speed = serializers.IntegerField()
    Jumping = serializers.IntegerField()
    Shot_Power = serializers.IntegerField()
    Agility = serializers.IntegerField()

    def to_representation(self, instance):
        data_dict = super(PlayerResponseScheduleSerializer, self).to_representation(instance)
        response_dict = {}
        for key,value in data_dict.iteritems():
            if value == None or value=="":
                value = "N/A"
            response_dict[key] = value
        return response_dict

class ClubPlayersSerializers(serializers.Serializer):
    Name = serializers.CharField(required=True)
    Rating = serializers.IntegerField(required=True)

    def to_representation(self, instance):
        data_dict = super(ClubPlayersSerializers, self).to_representation(instance)
        response_dict = {}
        for key, value in data_dict.iteritems():
            if value == None or value == "":
                value = "N/A"
            response_dict[key] = value
        return response_dict