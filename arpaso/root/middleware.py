from django.db import connection
from django.template import Template, Context
import os
import datetime

class SQLLogMiddleware:

    def process_response ( self, request, response ): 
        if connection.queries:
            file = open('./workfile.log', 'a')
            file.write(str(datetime.datetime.now()) + ' \n' + ' \n')
            for sql in connection.queries:
                file.write(sql['sql'] + ' \n' + ' \n')
        file.close()
        return response