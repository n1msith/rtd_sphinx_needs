==========
Tx Results
==========

.. test_result:: Tx power
    :id: result_tx_power_1
    :tags: tx
    :validates: test_tx_power_1

    The transmitter should have an output power of 23dBm over all frequencies.

    .. plotly::
    
        import plotly.graph_objects as go
        
        # Static test data
        freq = [2.4, 2.41, 2.42, 2.43, 2.44, 2.45, 2.46, 2.47, 2.48, 2.49, 2.5]
        gain = [14.2, 14.5, 14.8, 15.1, 15.0, 14.9, 15.2, 15.1, 14.7, 14.6, 14.3]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(x=freq, y=gain, 
                                name='Measured Gain', 
                                line=dict(color='blue')))
        
        fig.update_layout(
            title="TX Gain vs Frequency",
            xaxis_title="Frequency (GHz)",
            yaxis_title="Gain (dB)"
        )
        
        fig.show()