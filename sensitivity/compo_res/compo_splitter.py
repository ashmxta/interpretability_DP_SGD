import pandas as pd
import os
import sys
import re

def split_compo_csv_by_point(csv_path):
    # Extract run number from filename
    match = re.search(r'compo_res(\d+)', os.path.basename(csv_path))
    if not match:
        print("Filename must be like compo_resX.csv where X is a number")
        sys.exit(1)
    run_number = match.group(1)

    # Read file
    df = pd.read_csv(csv_path)

    # Create output directory
    out_dir = os.path.join(os.path.dirname(__file__), "compo_res_per_point")
    os.makedirs(out_dir, exist_ok=True)

    # Split by point
    for point in df["point"].unique():
        df_point = df[df["point"] == point]
        output_path = os.path.join(out_dir, f"compo_run{run_number}_point{int(point)}.csv")
        df_point.to_csv(output_path, index=False)
        print(f"Saved: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compo_splitter.py <compo_resX.csv>")
        sys.exit(1)
    split_compo_csv_by_point(sys.argv[1])
