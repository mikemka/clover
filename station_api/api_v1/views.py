import api_v1.models
import datetime
import django.http.response
import django.shortcuts


def json_base() -> dict:
    return {
        'datetime': datetime.datetime.now(),
    }


def get_flight_by_token(token: str):
    return token == '123'


def get_station_by_token(token: str) -> api_v1.models.Station | None:
    try:
        return api_v1.models.Station.objects.get(token=token)
    except api_v1.models.Station.DoesNotExist:
        return None


def ping(request) -> django.http.response.JsonResponse:
    data = {'error': 'invalid token'}
    _token = request.GET.get('token')
    if any((
        get_flight_by_token(_token),
        get_station_by_token(_token),
    )):
        data = {'text': 'pong'}
    return django.http.response.JsonResponse(data=json_base() | data)


def get_station(request) -> django.http.response.JsonResponse:
    try:
        station = api_v1.models.Station.objects.get(
            name=request.GET.get('name')
        )
        data = {
            'name': station.name,
            'status': station.status,
            'charging': station.charging,
            'aruco_marker': station.aruco_marker,
        }
    except api_v1.models.Station.DoesNotExist:
        data = {'error': 'invalid station name'}
    return django.http.response.JsonResponse(data=json_base() | data)
