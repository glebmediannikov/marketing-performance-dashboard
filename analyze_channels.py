import pandas as pd

df = pd.read_csv("sample_channel_data.csv")
df["session_to_lead_rate"] = df["leads"] / df["sessions"]
df["lead_to_customer_rate"] = df["customers"] / df["leads"]
df["cac"] = df.apply(lambda r: r["spend"] / r["customers"] if r["spend"] else 0, axis=1)
df["roas"] = df.apply(lambda r: r["revenue"] / r["spend"] if r["spend"] else None, axis=1)

cols = ["channel","sessions","leads","customers","session_to_lead_rate","lead_to_customer_rate","cac","roas"]
print(df[cols].round(3).to_string(index=False))

print("\nDecision prompts:")
print("- Scale channels with strong conversion economics, not volume alone.")
print("- Investigate high-traffic channels with weaker downstream conversion.")
print("- Separate owned/earned channels from paid-media efficiency when comparing CAC.")
