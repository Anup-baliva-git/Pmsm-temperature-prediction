# PMSM magnet temperature regression

## Demo

`pip install -r requirements.txt`, then `streamlit run app.py` (http://127.0.0.1:8509, or double-click `Launch-Demo.bat`). The page explains the pipeline and does not predict a temperature.


Predict `pm`, the permanent-magnet temperature, from the electric-motor bench table `Electric_cars` in the capstone database. The notebook reads `u_q`, `coolant`, `u_d`, `motor_speed`, `i_d`, `i_q`, `ambient`, `pm`, and `profile_id`.

The database and `pmsm_model.pkl` were not in the files that arrived, so this repo documents the pipeline and does not pretend to serve predictions.

## Note

`notebook/Regression_cap.ipynb` is the original analysis: EDA, cleaning, the train/test split, and the model pipelines. The Spyder `.py` files from `d:\PMSM regression capstone 1` and `Database.db` were never transferred, so they are not in this repo. The notebook still points at `D:\Data science Inttruvu.ai\Capstone projects for data science (extracted)\Database.db` and will not rerun until that file is present. `app.py` is only the explainer page, not the training pipeline.

## Pipeline the notebook builds

1. Load the table through SQLite, with a 100,000-row sample and a smaller sample used for exploration.
2. Coerce the sensor columns to numeric and impute medians.
3. Cap `i_q` and `coolant` with winsorization instead of deleting those rows.
4. Add current magnitude and a few products of the electrical readings.
5. Fit several regressors in scikit-learn pipelines, rank them by MAE, tune the top three with `RandomizedSearchCV`.
6. The notebook intends SHAP and LIME on the chosen model, then `joblib.dump(best_model, "pmsm_model.pkl")`.
7. A Streamlit form is pasted at the bottom of the notebook. It is not a separate app, and it needs the pickle that was not uploaded.

## What was wrong

- The database path is hardcoded to `D:\Data science Inttruvu.ai\...`.
- Empty cells and repeated blocks for the sample frame and the full frame make the "best model" easy to overwrite. One later cell does `best_model = tuned_models[results_f[0]]`, and `results_f` is a list of result rows, not model names.
- `profile_id` is filled with `Series.mode()`, which is a Series, not a scalar.
- No held-out MAE was left in a form that should be quoted. This page does not invent a score.

## System design

```
Electric_cars
  -> numeric cleanup and median impute
  -> winsorize i_q and coolant
  -> engineered current features
  -> Pipeline(imputer, scaler, model)
  -> MAE ranking and a randomized search
  -> pickle and a Streamlit form, once the database is available
```

## Subject

Regression on a physical sensor target, with the motor profile held in mind so rows from the same run are not treated as independent without saying so.

## Still needed

`Database.db`, or a public export of `Electric_cars`, plus the saved pickle if the Streamlit form should answer live inputs.

## Windows

Double-click `Launch-Demo.bat` in this folder. It starts the pipeline page at http://127.0.0.1:8509. There is no model and no `Database.db`, so the page does not predict a temperature.
