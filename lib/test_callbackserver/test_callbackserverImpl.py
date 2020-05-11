# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class test_callbackserver:
    '''
    Module Name:
    test_callbackserver

    Module Description:
    A KBase module: test_callbackserver
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/mrcreosote/test_callbackserver"
    GIT_COMMIT_HASH = "749d89d49bc375c524d6303ad9b18c72e13e7bdc"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def test_callbackserver(self, ctx, params):
        """
        Send an arbitrary JSONRPC mapping to the Callback Service.
        An example mapping that tells the CBS to run the Construct Species tree method:
                {'method': 'SpeciesTreeBuilder.construct_species_tree',
                 'params': [{
                 'new_genomes': ['50118/3/2', '50118/2/2'],
                     'out_workspace': 'gaprice:narrative_1588989318474',
                     'out_tree_id': 'njs_tree',
                     'out_genomeset_ref': 'gaprice:narrative_1588989318474/nts_tree_set',
                     'copy_genomes': 0}],
                 'service_ver': 'dev'
                 }
        :param params: instance of mapping from String to unspecified object
        :returns: instance of unspecified object
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN test_callbackserver
        #END test_callbackserver

        # At some point might do deeper type checking...
        if not isinstance(output, object):
            raise ValueError('Method test_callbackserver return value ' +
                             'output is not type object as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
