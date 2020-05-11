/*
A KBase module: test_callbackserver
*/

module test_callbackserver {

    /*
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

    */
    funcdef test_callbackserver(mapping<string,UnspecifiedObject> params) returns (UnspecifiedObject output) authentication required;

};
