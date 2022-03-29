from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import cx_Oracle

class PesquisaView(APIView):
    """
    API pesquisa
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, pk=''):
            if 'produto' in request.GET:            
                produto = request.GET['produto']
                redlakeSearch(produto)
                return Response({"msg": "Pesquisa realizada com sucesso!!"})
#-----------------------------------------------------------------------------------------#
def redlakeSearch(produto):
    connection = cx_Oracle.connect(user="lge1ca", password="Safira2021!leo",dsn="redlake_dwhp.world")
    cursor = connection.cursor()
    sql = """SELECT MARD.MATNR, MARD.LABST, MAKT.MAKTX
    FROM INFM_PSLA_CSC2.V_REPL_MARD_B2 MARD
    inner join INFM_PSLA_CSC2.V_REPL_MAKT_B2 MAKT
    ON MARD.MATNR = MAKT.MATNR
    where MARD.MATNR = :mid
    and MARD.WERKS = '908A'
    and MARD.LABST <> 0"""
    cursor.execute(sql, mid=produto)

    for row in cursor:
        print(row)

