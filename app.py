"""Pipeline page for the PMSM magnet-temperature notebook.

There is no model and no Database.db in this folder, so the page does not predict.

    streamlit run app.py
    python app.py --self-test
"""

from __future__ import annotations

PIPELINE = (
    "Load Electric_cars through SQLite, with a 100,000-row sample and a smaller sample used for exploration.",
    "Coerce the sensor columns to numeric and impute medians.",
    "Cap i_q and coolant with winsorization.",
    "Add current magnitude and a few products of the electrical readings.",
    "Fit several regressors in scikit-learn pipelines, rank them by MAE, and tune the top three with RandomizedSearchCV.",
    "The notebook intends SHAP and LIME on the chosen model, then joblib.dump(best_model, \"pmsm_model.pkl\").",
    "A Streamlit form is pasted at the bottom of the notebook. It needs the pickle that was not uploaded.",
)
COLUMNS = ("u_q", "coolant", "u_d", "motor_speed", "i_d", "i_q", "ambient", "pm", "profile_id")
MISSING = ("Database.db", "pmsm_model.pkl")


def prediction_available() -> bool:
    return False


def _self_test() -> None:
    assert prediction_available() is False
    assert "Database.db" in MISSING
    assert "pmsm_model.pkl" in MISSING
    assert "pm" in COLUMNS
    assert len(PIPELINE) == 7
    assert "MAE" not in "".join(PIPELINE) or "rank them by MAE" in PIPELINE[4]
    print("self-test ok")


def main() -> None:
    import streamlit as st

    st.set_page_config(page_title="PMSM magnet temperature", layout="wide")
    st.title("PMSM magnet temperature")
    st.write(
        "The notebook predicts pm, permanent-magnet temperature, from the Electric_cars bench table. "
        "There is no model in this folder and there is no Database.db, so this page does not predict a temperature."
    )
    st.write("Columns the notebook reads: " + ", ".join(COLUMNS) + ".")
    st.write("Still needed before any live score: " + " and ".join(MISSING) + ".")
    st.subheader("Pipeline")
    for index, step in enumerate(PIPELINE, start=1):
        st.write(f"{index}. {step}")
    st.caption(
        "No held-out MAE was left in a form that should be quoted, so this page does not show a score. "
        "A later cell indexes tuned_models[results_f[0]], and results_f is a list of result rows."
    )


if __name__ == "__main__":
    import sys

    if "--self-test" in sys.argv:
        _self_test()
    else:
        main()
