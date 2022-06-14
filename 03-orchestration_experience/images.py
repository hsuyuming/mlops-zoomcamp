from SpannerExecutor  import SpannerExecutor 
from GCSUtil import GCSUtil
from argparse import Namespace
import base64, re
import pandas as pd
from .image import Image


class Images:

    # Constructor
    def __init__(self, **kwargs):
        self.gcpenv = kwargs.get('gcpenv', '')
        self.image_ids = kwargs.get('image_ids', '')
        self.ns = kwargs.get('ns', '')
        self.envConfigFile=kwargs.get('envConfigFile', '')
        self.env=kwargs.get('env', '')

        self.project = 'gdw-{}-data'.format(self.gcpenv)

        self._blob_inst = None
        self._meta_inst = None
        self._query_data = None



    @property
    def tablename(self):
        return 'image'

    @property
    def image_ids_str(self):
        rs = ','.join(self.image_ids)
        return rs


    @property
    def sql_str(self):
        return '''
select * from {} where image_id in ( {} )
        '''.format(self.tablename, self.image_ids_str)

    def query(self):
        se = SpannerExecutor(ns=self.ns, envConfigFile=self.envConfigFile, env=self.env)     
        with se.getConnection() as conn:
            streamed_resultset = conn.executeQuery(self.sql_str)
            df = se.toPandasDF(streamed_resultset)
        return df

    @property
    def query_data(self):
        if self._query_data is not None:
            return self._query_data

        df = self.query()
        self._query_data = pd.DataFrame()
        if not df.empty:
            self._query_data = df
        return self._query_data

    # @property
    # def image_insts(self):
    #     rs = []
    #     for index, row in self.query_data.iterrows():
    #         rs.append(Image(
    #             gcpenv=self.gcpenv,
    #             ns=self.ns,
    #             envConfigFile=self.envConfigFile,
    #             env=self.env,
    #             query_data=row

    #         ))

    #     return rs    


        


    