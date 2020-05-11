/*
A KBase module: test_callbackserver
*/

module test_callbackserver {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_test_callbackserver(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
