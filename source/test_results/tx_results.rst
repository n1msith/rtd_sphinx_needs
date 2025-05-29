==========
Tx Results
==========
..    :result_file: somefile.csv
..    :margin: [calculated from the results file somehow using a custom fucntion]

.. test_result:: Tx power
    :id: result_tx_power_1
    :layout: result
    :tags: tx
    :validates: test_tx_power_1

    The transmitter should have an output power of 23dBm over all frequencies.

    .. plotly::
    
       from plot_helpers import go, np, pd, plot_tx_results
       plot_tx_results()
        
