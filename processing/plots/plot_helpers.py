from conf import project_root
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import os

def read_tx_results(csv_path):
    """Read frequency and gain from a CSV file."""
    df = pd.read_csv(csv_path)
    freq = df['Frequency'].tolist()
    gain = df['Gain'].tolist()
    return freq, gain

def calc_margins(y_values, spec_min, spec_max):
    """Calculate margins and return both array and minimum"""
    result_array = np.array(y_values)
    spec_min_array = np.array(spec_min) if isinstance(spec_min, list) else np.full_like(result_array, spec_min)
    spec_max_array = np.array(spec_max) if isinstance(spec_max, list) else np.full_like(result_array, spec_max)
    
    margin_to_min = result_array - spec_min_array
    margin_to_max = spec_max_array - result_array
    overall_margin = np.minimum(margin_to_min, margin_to_max)
    
    min_margin = np.min(overall_margin)
    return overall_margin, min_margin

def find_worst_case_point(overall_margin, x_values):
    """Find the x-value and margin at the worst-case point"""
    min_margin_idx = np.argmin(overall_margin)
    worst_x_value = x_values[min_margin_idx]
    worst_margin = overall_margin[min_margin_idx]
    return worst_x_value, worst_margin

def calc_pass_fail(overall_margin):
    """Determine pass/fail status based on margin array"""
    min_margin = np.min(overall_margin)
    return "PASS" if min_margin >= 0 else "FAIL"

def calc_status_and_margins(y_values, spec_min, spec_max):
    """Calculate status and margins for a given set of y-values against spec limits."""
    overall_margin, min_margin = calc_margins(y_values, spec_min, spec_max)
    status = calc_pass_fail(overall_margin)
    return status, overall_margin, min_margin

def plot_tx_results(csv_path='raw_results/tx_power_results.csv', title='TX Results', x_label='Frequency (Hz)', y_label='Gain (dB)'):
    
    csv_full_path = os.path.join(project_root, csv_path)
    freq, gain = read_tx_results(csv_full_path)

    # Spec limits
    spec_min = 14.0
    spec_max = 16.0
    
    # Use generic functions
    overall_margin, min_margin = calc_margins(gain, spec_min, spec_max)
    worst_freq, worst_margin = find_worst_case_point(overall_margin, freq)
    status = calc_pass_fail(overall_margin)  # Add this line
    
    # Find the index for highlighting the critical point
    min_margin_idx = np.argmin(overall_margin)
    
    fig = go.Figure()
    
    # Add measured data
    fig.add_trace(go.Scatter(x=freq, y=gain, 
                            name='Measured Gain', 
                            line=dict(color='blue')))
    
    # Add spec limits
    fig.add_hline(y=spec_min, line_dash="dash", line_color="red", 
                  annotation_text="Min Spec (14 dB)")
    fig.add_hline(y=spec_max, line_dash="dash", line_color="red", 
                  annotation_text="Max Spec (16 dB)")
    
    # Highlight critical point with color based on status
    marker_color = 'green' if status == 'PASS' else 'red'
    fig.add_trace(go.Scatter(x=[worst_freq], y=[gain[min_margin_idx]], 
                            mode='markers', 
                            marker=dict(color=marker_color, size=10),
                            name='Critical Point'))
    
    # Add analysis annotation
    fig.add_annotation(
        x=0.02, y=0.98, xref="paper", yref="paper",
        text=f"<b>Analysis:</b><br>"
                f"Status: {status}<br>"
                f"Min Margin: {min_margin:.1f} dB<br>"
                f"At Frequency: {worst_freq:.2f} GHz",
        showarrow=False, align="left",
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor="black", borderwidth=1
    )
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label
    )
    
    return fig