
from SpannerExecutor  import SpannerExecutor 
from GCSUtil import GCSUtil
from argparse import Namespace
import base64, re
import pandas as pd
#import digger_funcs

class Blob:
    def __init__(self, ns: Namespace, env: str, envConfigFile: str):
        self.ns = ns

        self.env = env
        self.envConfigFile = envConfigFile

        self.project = ns.project
        self.bucketname = ns.bucket
        self.blobname = ns.blob

    @property
    def ns_for_gcsutil(self):
        ns = Namespace(**vars(self.ns))
        for item in ['action', 'file', 'content_type', 'epm_key', 'epm_value', 'delimiter', 'max_result', 'target']:
            setattr(ns, item, 'placeholder')
        
        return ns

    @property
    def gcsutil(self):
        return GCSUtil(self.ns_for_gcsutil, self.env, self.envConfigFile)



    @property
    def signed_url(self):
        rs = self.gcsutil.generateSignedURL(self.blobname, duration=5)
        return rs['sign_url']

    @property
    def image_b64(self):
        data = self.gcsutil.getBlobAsBytes()
        rs = base64.b64encode(data).decode('utf-8')
        return rs

########################################################################

class Meta:
    # Constructor
    def __init__(self, **kwargs):
        self.data = kwargs.get('data', None)
        self.gcpenv = kwargs.get('gcpenv', None)

    @property
    def is_empty(self):
        if self.data.empty:
            return True

        return False

    @property
    def image_id(self):
        return self.data.image_id

    @property
    def facility(self):
        return self.data.facility.lower().replace(' ', '-')

    @property
    def img_type(self):
        return self.data.img_type

    def get_bucketname_by_uri(self, uri):
        path = re.sub('gs://', '', uri)
        eles = path.split('/')
        return eles[0]

    def get_imagepath_by_uri(self, uri):
        path = re.sub('gs://', '', uri)
        eles = path.split('/')
        return '/'.join(eles[1:])



    @property
    def bucketname(self):
        if self.data.storage_location_url.startswith('gs://'):
            return self.get_bucketname_by_uri(self.data.storage_location_url)

        if self.img_type in ['wis', 'wisecam', 'cdsem', 'reviewsem']:
            return 'gdw-{}-data-{}-{}'.format(self.gcpenv, self.facility, self.img_type)

        if self.img_type in ['klarity']:
            return 'gdw-{}-img-analytics-{}-{}-img_data'.format(
                self.gcpenv,
                self.img_type,
                self.facility,
            )

        return ''    


    @property
    def insp_datetime_path(self):
        year = self.data.inspection_datetime.year
        month = self.data.inspection_datetime.month
        day = self.data.inspection_datetime.day
        
        return '{}/{}/{}'.format(year, month, day)

    @property
    def image_name(self):
        return self.data['name']

    @property
    def image_path(self):
        if self.data.storage_location_url.startswith('gs://'):
            return self.get_imagepath_by_uri(self.data.storage_location_url)

        return '{}/{}'.format(self.insp_datetime_path, self.image_name)



########################################################################




class Image:
    # Constructor
    def __init__(self, **kwargs):
        self.gcpenv = kwargs.get('gcpenv', '')
        self.ns = kwargs.get('ns', '')
        self.envConfigFile=kwargs.get('envConfigFile', '')
        self.env=kwargs.get('env', '')
        self.query_data = kwargs.get('query_data', None)
        self.project = 'gdw-{}-data'.format(self.gcpenv)

        self._blob_inst = None
        self._meta_inst = None
        self._query_data = None




    @property
    def meta_inst(self):
        if self._meta_inst:
            return self._meta_inst

        self._meta_inst = Meta(
            gcpenv=self.gcpenv,
            data=self.query_data
        )
        return self._meta_inst

    @property
    def blob_inst(self):
        if self._blob_inst:
            return self._blob_inst

        ns_for_blob = Namespace(
            **vars(self.ns),
            project=self.project,
            bucket=self.meta_inst.bucketname,
            blob=self.meta_inst.image_path

        )
        self._blob_inst = Blob(
            ns=ns_for_blob,
            env=self.env,
            envConfigFile=self.envConfigFile
        )

        return self._blob_inst


    @property
    def signed_url(self):
        return self.blob_inst.signed_url

    @property
    def b64_str(self):
        return self.blob_inst.image_b64


    @property
    def json_output(self):
        output = {
            'imageid': str(self.meta_inst.image_id),
        }

        if self.meta_inst.is_empty:
            output.update({
                'message': 'no data found'
            })
        else:    
            output.update({
                'message': 'success',    
                'bucketname': self.meta_inst.bucketname,
                'image_path': self.meta_inst.image_path,
#                 'signed_url': self.signed_url,     
                'base64_str': self.b64_str,
            })

        return output    


        


    