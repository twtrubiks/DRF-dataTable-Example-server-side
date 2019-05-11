from django.shortcuts import render
from musics.models import Music, query_musics_by_args
from musics.serializers import MusicSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response



def index(request):
    return render( request, 'musics/index.html')

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def list(self, request, **kwargs):
        try:
            music = query_musics_by_args(**request.query_params)
            serializer = MusicSerializer(music['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = music['draw']
            result['recordsTotal'] = music['total']
            result['recordsFiltered'] = music['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)