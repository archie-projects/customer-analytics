import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Generate synthetic realistic data ---
np.random.seed(42)

# Simulate Acquisition Cost (CAC) between $100 and $2000
cac = np.random.uniform(100, 2000, 100)

# Simulate Lifetime Value (CLV) roughly proportional to CAC with variation
clv = cac * np.random.uniform(2, 8, 100) + np.random.normal(0, 500, 100)

# Build dataframe
df = pd.DataFrame({
    "Acquisition Cost (USD)": cac,
    "Customer Lifetime Value (USD)": clv
})

# --- Styling ---
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1)

# --- Plot ---
plt.figure(figsize=(8, 8))  # ensures 512x512 pixels with dpi=64
scatter = sns.scatterplot(
    data=df,
    x="Acquisition Cost (USD)",
    y="Customer Lifetime Value (USD)",
    hue="Acquisition Cost (USD)",
    palette="viridis",
    size="Customer Lifetime Value (USD)",
    sizes=(20, 200),
    alpha=0.8,
    edgecolor="w",
    linewidth=0.5
)

# Titles & labels
plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=16, weight="bold")
plt.xlabel("Acquisition Cost (USD)", fontsize=12)
plt.ylabel("Customer Lifetime Value (USD)", fontsize=12)

# Legend
plt.legend(title="Acquisition Cost", bbox_to_anchor=(1.05, 1), loc="upper left")

# --- Save as PNG (512x512 pixels) ---
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
