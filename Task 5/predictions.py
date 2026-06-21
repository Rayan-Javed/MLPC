# ============================================================
# Generate Predictions for Hidden Test Set (Final Submission)
# ============================================================

import os
import glob
import numpy as np
import pandas as pd
from pathlib import Path

# Paths – adjust if necessary (use the same base_path as before)
# base_path is already defined in your notebook.
test_path = base_path / "test" / "audio_features"
test_files = sorted(glob.glob(str(test_path / "*.npz")))

print(f"Generating predictions for {len(test_files)} hidden test files...")

all_rows = []
for filepath in test_files:
    data = dict(np.load(filepath, allow_pickle=True))
    X = build_feature_matrix(data)                     # all segments (including half-second)
    X_scaled = scaler.transform(X)                     # scale using training scaler
    X_pca = pca.transform(X_scaled)                    # PCA using training PCA
    preds_all = rf_model.predict(X_pca)                # (N_all, 15)
    start_times = data['start_time']
    # Keep only whole‑second segments (t = 0, 1, 2, ...)
    whole_mask = np.isclose(start_times % 1.0, 0.0)
    times_whole = start_times[whole_mask]
    preds_whole = preds_all[whole_mask]
    filename = os.path.basename(filepath).replace('.npz', '.wav')
    rows = predictions_to_intervals(preds_whole, times_whole, filename, class_names)
    all_rows.extend(rows)

pred_df = pd.DataFrame(all_rows)
pred_csv = "predictions_hidden_test.csv"
pred_df.to_csv(pred_csv, index=False)

print(f"Saved predictions to {pred_csv} with {len(pred_df)} event intervals.")
print("First 10 rows:")
print(pred_df.head(10))