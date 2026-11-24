import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 5)


def create_sample_churn_data(n: int = 500, seed: int = 42) -> pd.DataFrame:
    """Create a realistic synthetic customer churn dataset with dirty values."""
    rng = np.random.default_rng(seed)

    customer_ids = [f"CUST-{1000 + i}" for i in range(n)]
    gender = rng.choice(["Female", "Male", "female", "MALE "], size=n, p=[0.45, 0.45, 0.05, 0.05])
    senior_citizen = rng.choice([0, 1], size=n, p=[0.84, 0.16])
    tenure_months = rng.integers(0, 73, size=n).astype(float)
    contract = rng.choice(
        ["Month-to-month", "One year", "Two year"],
        size=n,
        p=[0.55, 0.25, 0.20],
    )
    monthly_charges = np.round(rng.uniform(20.0, 115.0, size=n), 2)

    # Total charges roughly correlates with tenure and monthly charges
    total_charges = np.round(tenure_months * monthly_charges * rng.uniform(0.95, 1.05, size=n), 2)

    # Higher churn probability for short tenure and month-to-month contracts
    churn_prob = np.clip(
        0.55
        - 0.006 * tenure_months
        + np.where(contract == "Month-to-month", 0.15, -0.10)
        + 0.002 * (monthly_charges - 60),
        0.05,
        0.90,
    )
    churn = np.where(rng.random(n) < churn_prob, "Yes", "No")

    df = pd.DataFrame(
        {
            "CustomerID": customer_ids,
            "Gender": gender,
            "SeniorCitizen": senior_citizen,
            "TenureMonths": tenure_months,
            "Contract": contract,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges,
            "Churn": churn,
        }
    )

    # Inject realistic data quality issues: missing values, blank strings, and duplicates
    missing_idx = rng.choice(n, size=25, replace=False)
    df.loc[missing_idx[:15], "TotalCharges"] = np.nan
    df.loc[missing_idx[15:20], "TotalCharges"] = " "  # whitespace string
    df.loc[missing_idx[20:], "TenureMonths"] = np.nan

    # Append duplicate rows
    df = pd.concat([df, df.iloc[:5]], ignore_index=True)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean text formatting, remove duplicates, and impute missing values."""
    cleaned = df.copy()

    # 1. Remove exact duplicate rows
    duplicates_count = cleaned.duplicated().sum()
    cleaned = cleaned.drop_duplicates().reset_index(drop=True)
    print(f"Removed {duplicates_count} duplicate rows.")

    # 2. Standardize string columns (strip whitespace, normalize casing)
    cleaned["Gender"] = cleaned["Gender"].astype(str).str.strip().str.title()
    cleaned["Contract"] = cleaned["Contract"].astype(str).str.strip()
    cleaned["Churn"] = cleaned["Churn"].astype(str).str.strip().str.title()

    # 3. Convert numeric columns that may contain blanks/strings using Pandas + NumPy
    cleaned["TotalCharges"] = pd.to_numeric(cleaned["TotalCharges"], errors="coerce")
    cleaned["TenureMonths"] = pd.to_numeric(cleaned["TenureMonths"], errors="coerce")

    print("\nMissing values before imputation:")
    print(cleaned.isna().sum()[cleaned.isna().sum() > 0])

    # 4. Handle missing values:
    # For TenureMonths, fill missing values with median
    cleaned["TenureMonths"] = cleaned["TenureMonths"].fillna(cleaned["TenureMonths"].median())

    # For TotalCharges, estimate via TenureMonths * MonthlyCharges where missing, then fallback to median
    estimated_total = cleaned["TenureMonths"] * cleaned["MonthlyCharges"]
    cleaned["TotalCharges"] = np.where(
        cleaned["TotalCharges"].isna(),
        estimated_total,
        cleaned["TotalCharges"],
    )
    cleaned["TotalCharges"] = cleaned["TotalCharges"].fillna(cleaned["TotalCharges"].median())

    # Add a NumPy-derived feature: Average revenue per active month (safe division)
    cleaned["AvgMonthlySpend"] = np.where(
        cleaned["TenureMonths"] > 0,
        np.round(cleaned["TotalCharges"] / np.maximum(cleaned["TenureMonths"], 1), 2),
        cleaned["MonthlyCharges"],
    )

    print("\nMissing values after imputation:", int(cleaned.isna().sum().sum()))
    return cleaned


def generate_summary_stats(df: pd.DataFrame) -> None:
    """Print dataset overview, numeric summary statistics, and churn breakdowns."""
    print("\n--- Dataset Shape & Types ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print(df.dtypes)

    numeric_cols = ["TenureMonths", "MonthlyCharges", "TotalCharges", "AvgMonthlySpend"]
    print("\n--- Numeric Summary Statistics ---")
    print(df[numeric_cols].describe().T[["count", "mean", "std", "min", "50%", "max"]])

    # NumPy array calculations on MonthlyCharges
    charges_arr = df["MonthlyCharges"].to_numpy()
    p25, p50, p75 = np.percentile(charges_arr, [25, 50, 75])
    iqr = p75 - p25
    print(f"\nMonthlyCharges IQR (NumPy): {iqr:.2f} (25th={p25:.2f}, 75th={p75:.2f})")

    print("\n--- Overall Churn Rate ---")
    print(df["Churn"].value_counts(normalize=True).mul(100).round(2).astype(str) + "%")

    print("\n--- Mean Metrics Grouped by Churn ---")
    grouped = df.groupby("Churn")[["TenureMonths", "MonthlyCharges", "TotalCharges"]].agg(["mean", "median"])
    print(grouped.round(2))

    print("\n--- Churn Rate (%) by Contract Type ---")
    contract_churn = pd.crosstab(df["Contract"], df["Churn"], normalize="index").mul(100).round(2)
    print(contract_churn)


def visualize_patterns(df: pd.DataFrame) -> None:
    """Create visualizations highlighting key churn patterns."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Customer Churn Exploratory Data Analysis", fontsize=16, fontweight="bold")

    # 1. Churn count by contract type
    sns.countplot(data=df, x="Contract", hue="Churn", ax=axes[0, 0], palette="Set2")
    axes[0, 0].set_title("Churn Count by Contract Type")
    axes[0, 0].set_xlabel("Contract Type")
    axes[0, 0].set_ylabel("Number of Customers")

    # 2. Tenure distribution by churn status
    sns.histplot(
        data=df,
        x="TenureMonths",
        hue="Churn",
        bins=20,
        kde=True,
        element="step",
        ax=axes[0, 1],
        palette="Set1",
    )
    axes[0, 1].set_title("Tenure Distribution (Months) by Churn")
    axes[0, 1].set_xlabel("Tenure (Months)")

    # 3. Monthly charges boxplot by churn
    sns.boxplot(data=df, x="Churn", y="MonthlyCharges", ax=axes[1, 0], palette="Pastel1")
    axes[1, 0].set_title("Monthly Charges by Churn Status")
    axes[1, 0].set_xlabel("Churn")
    axes[1, 0].set_ylabel("Monthly Charges ($)")

    # 4. Correlation heatmap of numerical features
    num_df = df[["TenureMonths", "MonthlyCharges", "TotalCharges", "AvgMonthlySpend", "SeniorCitizen"]].copy()
    num_df["ChurnFlag"] = np.where(df["Churn"] == "Yes", 1, 0)
    corr_matrix = num_df.corr(numeric_only=True)
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, ax=axes[1, 1])
    axes[1, 1].set_title("Feature Correlation Matrix")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


def main() -> None:
    # To use a real CSV instead:
    # raw_df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    raw_df = create_sample_churn_data(n=500)
    cleaned_df = clean_data(raw_df)
    generate_summary_stats(cleaned_df)
    visualize_patterns(cleaned_df)


if __name__ == "__main__":
    main()