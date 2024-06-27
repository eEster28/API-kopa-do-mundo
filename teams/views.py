from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict
from teams.models import Team
from utils import data_processing
from exceptions import *


class TeamsView(APIView):
    
  def get(self, request: Request) -> Response:
       teams = Team.objects.all()
       teams_list = []
       
       for teams in teams:
            teams_dict = model_to_dict(teams)
            teams_list.append(teams_dict)
            
       return Response(teams_list, status.HTTP_200_OK)

  def post(self, request: Request) -> Response:
       team_data = request.data
       
       try:
              data_processing(team_data)
       except (NegativeTitlesError, InvalidYearCupError,ImpossibleTitlesError) as erro:
              return Response({"error": str(erro)}, status.HTTP_400_BAD_REQUEST)
         
       teams = Team.objects.create(**team_data)

       teams_dict = model_to_dict(teams)
                   
       return Response(teams_dict, status.HTTP_201_CREATED)


class TeamsDetailView(APIView):
     
     def get(self, request: Request, team_id: int) -> Response:
         
        try:
            teams = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        teams_dict = model_to_dict(teams)

        return Response(teams_dict, status.HTTP_200_OK) 
     
     def patch(self, request: Request, team_id: int) -> None:
         
        try:
            teams = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
 
        for key, value in request.data.items():
            setattr(teams, key, value)

        teams.save()

        teams_dict = model_to_dict(teams)

        return Response(teams_dict, status.HTTP_200_OK)
       
     
     def delete(self, request: Request, team_id: int) -> Response:
         
        try:
            teams = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
      
        teams.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
     
     