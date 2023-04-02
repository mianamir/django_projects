from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, permissions

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import (
    vary_on_cookie,
    vary_on_headers
)

from commons.db_config import _get_database
from commons.constants import (PROJECTS_TABLE, WTGS_TABLE)


def parse_db_data(data):
    """
    Parse the database res to list of arrays
    :param data:
    :return:
    """
    res = list()

    for row in data:
        res.append({
            "id": row[0],
            "project_name": str(row[1]),
            "project_number": int([2][0]),
            "acquisition_date": int([3][0]),
            "number_3l_code": int([4][0]),
            "project_deal_type_id": str(row[5]),
            "project_group_id": str(row[6]),
            "project_status_id": str(row[7]),
            "company_id": int(row[8])
        })

    return res


class ProjectCreateAPI(APIView):

    # With auth: cache requested url for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization", ))
    def post(self, request):
        req_data = JSONParser().parse(request)

        _conn, _cur = _get_database()
        try:
            insert_query = f""" INSERT INTO {PROJECTS_TABLE}
                     (project_name, 
                     project_number, 
                     acquisition_date, 
                     number_3l_code, 
                     project_deal_type_id, 
                     project_group_id, 
                     project_status_id, 
                     company_id) 
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            record_to_insert = (req_data['project_name'],
                                req_data['project_number'],
                                req_data['acquisition_date'],
                                req_data['number_3l_code'],
                                req_data['project_deal_type_id'],
                                req_data['project_group_id'],
                                req_data['project_status_id'],
                                req_data['company_id'])

            _cur.execute(insert_query, record_to_insert)

            _conn.commit()
            # count = _cur.rowcount
            print(f"Record inserted successfully into {PROJECTS_TABLE} table")

            return JsonResponse({"data": {}}, status=status.HTTP_201_CREATED)

        except Exception as err:
            print(f'An exception has occured: {err}')
            return JsonResponse({"data": list()}, status=status.HTTP_400_BAD_REQUEST)

        finally:
            if _conn:
                _cur.close()
                _conn.close()
                print(f"PostgreSQL connection is closed")


class ProjectUpdateAPI(APIView):

    # With auth: cache requested url for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization", ))
    def put(self, request, project_id=None, format=None):
        req_data = JSONParser().parse(request)

        _conn, _cur = _get_database()

        try:
            print(f"{PROJECTS_TABLE} table before updating record ")
            sql_select_query = f"""select * from {PROJECTS_TABLE} where id = %s"""
            _cur.execute(sql_select_query, (project_id,))
            record = _cur.fetchone()
            print(record)

            # Update single record now
            sql_update_query = f"""UPDATE {PROJECTS_TABLE} SET
                     project_name = %s,  
                     project_number = %s,
                     acquisition_date = %s, 
                     number_3l_code = %s,
                     project_deal_type_id = %s, 
                     project_group_id = %s,
                     project_status_id = %s, 
                     company_id = %s
                     WHERE id = %s"""
            _cur.execute(sql_update_query, (
                req_data['project_name'],
                req_data['project_number'],
                req_data['acquisition_date'],
                req_data['number_3l_code'],
                req_data['project_deal_type_id'],
                req_data['project_group_id'],
                req_data['project_status_id'],
                req_data['company_id'],
                project_id)
                         )

            _conn.commit()

            count = _cur.rowcount

            print(count, "Record Updated successfully ")

            print(f"{PROJECTS_TABLE} table after updating record ")

            sql_select_query = f"""select * from {PROJECTS_TABLE} where id = %s"""

            _cur.execute(sql_select_query, (project_id,))

            record = _cur.fetchone()

            print(record)

            print(f"Record updated successfully for {PROJECTS_TABLE} table")

            return JsonResponse({"data": {}}, status=status.HTTP_202_ACCEPTED)

        except Exception as err:
            print(f'An exception has occured: {err}')
            return JsonResponse({"data": list()}, status=status.HTTP_400_BAD_REQUEST)

        finally:
            if _conn:
                _cur.close()
                _conn.close()
                print(f"PostgreSQL connection is closed")


class ProjectListAPI(APIView):

    # With auth: cache requested url for each user for 2 hours
    # @method_decorator(cache_page(60 * 60 * 2))
    # @method_decorator(vary_on_headers("Authorization", ))
    def get(self, request):
        _conn, _cur = _get_database()
        try:
            _cur.execute(f"SELECT * FROM {PROJECTS_TABLE};")
            res_data = _cur.fetchall()

            res = parse_db_data(res_data)

            return JsonResponse({"projects": res}, status=status.HTTP_200_OK, safe=False)

        except Exception as err:
            print(f'An exception has occured: {err}')
            return JsonResponse({"data": list()}, status=status.HTTP_400_BAD_REQUEST)

        finally:
            _cur.close()


class ProjectDeleteAPI(APIView):

    # With auth: cache requested url for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("Authorization", ))
    def delete(self, request, project_id=None, format=None):
        _conn, _cur = _get_database()
        try:
            sql_delete_query = f"""Delete from {PROJECTS_TABLE} where id = %s"""

            _cur.execute(sql_delete_query, (project_id,))

            _conn.commit()

            count = _cur.rowcount

            print(count, "Record deleted successfully ")

            return JsonResponse({"data": list()}, status=status.HTTP_204_NO_CONTENT)

        except Exception as err:
            print(f'An exception has occured: {err}')
            return JsonResponse({"data": list()}, status=status.HTTP_400_BAD_REQUEST)

        finally:
            if _conn:
                _cur.close()
                _conn.close()
                print(f"PostgreSQL connection is closed")
