from musics.models import Music
from musics.serializers import MusicSerializer
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.template.response import TemplateResponse
from django.http.response import HttpResponse
from musics.models import query_musics_by_args


def index(request):
    html = TemplateResponse(request, 'index.html')
    return HttpResponse(html.render())


# Create your views here.
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
            result['recordsTotal'] = music['count']
            result['recordsFiltered'] = music['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

            # [Get] api/music/
            # def list(self, request, **kwargs):
            #     try:
            #         music = Music.objects.all()[0:50000]
            #         serializer = MusicSerializer(music, many=True)
            #
            #         return Response(serializer.data, status=status.HTTP_200_OK, template_name=None, content_type=None)
            #
            #     except Exception as e:
            #         return Response(e.message, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)
            #
