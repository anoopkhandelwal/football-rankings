# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from players.models import Players, Player
from players.serializers import PlayersResponseScheduleSerializer, PlayerResponseScheduleSerializer, \
    ClubPlayersSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def statusAPI(request):
    return HttpResponse("Hello, world. You're at the football index.")

def status2API(request):
    context = {'message': "Hello, there. You're at the football index."}
    return render(request, 'test.html', context)

class PlayersInfoHtml(APIView):

    def get(self, request):
        response = {}
        error_message = None
        try:
            response['data'] = {}
            players_list = []
            players_records = Player.objects.all()

            for record in players_records:
                serialized_json = PlayerResponseScheduleSerializer(record).data
                players_list.append(serialized_json)

            response['data'] = players_list

        except Players.DoesNotExist as e:
            error_message = e.detail
        except Exception as e:
            error_message = "Internal Server Error : " + str(e)

        context = {'players': response , 'error':error_message}
        return render(request, 'players.html', context)

class PlayersInfo(APIView):

    def get(self, request):
        response = {}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        try:
            response['data'] = {}
            players_list = []
            players_records = Players.objects.all()

            for record in players_records:
                serialized_json = PlayersResponseScheduleSerializer(record).data
                players_list.append(serialized_json)

            response['data'] = players_list
            status_code = status.HTTP_200_OK

        except Players.DoesNotExist as e:
            status_code = e.status_code
            response['detail'] = e.detail
        except Exception as e:
            print(e)
            response['detail'] = "Internal Server Error : " + str(e)

        return Response(response, status_code, content_type="application/json")

class PlayerInfo(APIView):
    def get(self, request , name):
        response = {}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        try:
            response['data'] = {}
            player_record = Players.objects.get(Name__contains=name)
            serialized_json = PlayersResponseScheduleSerializer(player_record).data
            response['data'] = serialized_json

            status_code = status.HTTP_200_OK

        except Players.DoesNotExist as e:
            status_code = status.HTTP_404_NOT_FOUND
            response['detail'] = 'Player not found'
        except Exception as e:
            print(e)
            response['detail'] = "Internal Server Error : " + str(e)

        return Response(response, status_code, content_type="application/json")

class PlayerInfoHtml(APIView):
    def get(self, request , name):
        response = {}
        error_message = None
        try:
            player_record = Player.objects.get(Name=name)
            icons = [
                'http://orig05.deviantart.net/b328/f/2016/302/a/a/visage_cristiano_ronaldo_portugal_by_maxim_shouterden-damkuzy.png',
                'http://cdn.talksport.com/sport-mag/469/469_OverseasIcons2.jpg',
                    'http://orig01.deviantart.net/cc21/f/2014/136/4/3/neymar_by_ha3gfx-d7iluem.png',
                    'https://pbs.twimg.com/profile_images/690965507198029824/3quC3A7L.jpg',
                'https://image.freepik.com/free-photo/zlatan-ibrahimovic-ac-milan-serie-a_26-237.jpg',
                    'http://vectorpage.com/uploads/2015/05/Footballer-silhouette-Free-vector.png'
            ]
            players_map = {
                'Cristiano Ronaldo':0,
                'Lionel Messi':1,
                'Neymar':2,
                'Luis Suárez':3,
                'Zlatan Ibrahimović':4
            }
            serialized_json = PlayerResponseScheduleSerializer(player_record).data
            response['player'] = serialized_json

            clubs_players = Player.objects.filter(Club =
                                                  serialized_json['Club']).exclude(
                                                    Name=name
                                                ).order_by('Rating').reverse()[:9]
            recommendations = []
            response['clubName'] = serialized_json['Club']
            for player in clubs_players:
                club_player = ClubPlayersSerializers(player).data
                recommendations.append(club_player)

            response['clubs'] = recommendations
            player_index = players_map.get(response['player'].get('Name'))
            if player_index is None:
                response['icon'] = icons[-1]
            else:
                response['icon'] = icons[player_index]
        except Players.DoesNotExist as e:
            error_message = e.detail
        except Exception as e:
            error_message = "Internal Server Error : " + str(e)

        context = {'response': response, 'error': error_message}
        return render(request, 'player.html', context)

class PlayersFilteredInfoHtml(APIView):

    def get(self, request , filter_key):
        response = {}
        error_message = None
        try:
            response['data'] = {}
            players_list = []
            players_records = Player.objects.all().order_by(filter_key)

            for record in players_records:
                serialized_json = PlayerResponseScheduleSerializer(record).data
                players_list.append(serialized_json)

            response['data'] = players_list

        except Players.DoesNotExist as e:
            error_message = e.detail
        except Exception as e:
            error_message = "Internal Server Error : " + str(e)

        context = {'players': response , 'error':error_message}
        return render(request, 'players.html', context)

class SearchInfoHtml(APIView):

        def get(self, request, search_key):
            response = {}
            error_message = None
            try:
                response['data'] = {}
                players_list = []
                players_records = Player.objects.filter(Name__icontains=search_key)

                for record in players_records:
                    serialized_json = PlayerResponseScheduleSerializer(record).data
                    players_list.append(serialized_json)

                response['data'] = players_list

            except Players.DoesNotExist as e:
                error_message = e.detail
            except Exception as e:
                error_message = "Internal Server Error : " + str(e)

            context = {'players': response, 'error': error_message}
            return render(request, 'players.html', context)