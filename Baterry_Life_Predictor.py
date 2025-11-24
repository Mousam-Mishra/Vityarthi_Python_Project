print("========================================")
print("     BATTERY LIFE, CHARGING & HEALTH")
print("========================================")

device = input("Is your device Mobile or Laptop? ").strip().lower()
battery_percent = float(input("Enter current battery percentage (0–100): "))
hours_passed = float(input("How many hours since your device was fully charged? "))
battery_capacity = float(input("Enter battery capacity (mAh): "))
charger_watt = float(input("Enter charger watt rating (W): "))

# ----- Battery Life Estimation -----
drain_rate = (100 - battery_percent) / hours_passed
hours_left = battery_percent / drain_rate
print(f"\nEstimated usage time remaining: {hours_left:.2f} hours")

# Device-based evaluation
if device.startswith('m'):
    if hours_left < 2:
        print("Status: Low for Mobile")
    elif hours_left < 4:
        print("Status: Moderate for Mobile")
    else:
        print("Status: Good Battery Backup for Mobile")
elif device.startswith('l'):
    if hours_left < 2:
        print("Status: Very Low for Laptop")
    elif hours_left < 4:
        print("Status: Low – Plug in charger soon")
    else:
        print("Status: Good for Laptop")

# ----- Battery Health Estimation Using typical degradation -----
# Assume new full-usage hours = battery_capacity/estimated_draw_mA
# We approximate draw_mA using hours_passed & drain
# drain % = (100 - battery_percent) in hours_passed => we compute mAh usage rate
usage_since_full_mAh = battery_capacity * (100 - battery_percent) / 100
usage_rate_mA = usage_since_full_mAh / hours_passed
full_cycle_hours_new = battery_capacity / usage_rate_mA
health_percent = (hours_passed + hours_left) / full_cycle_hours_new * 100
print(f"\nEstimated Battery Health: {health_percent:.2f}%")
if health_percent > 90:
    print("Battery Health: Excellent")
elif health_percent > 80:
    print("Battery Health: Good")
elif health_percent > 70:
    print("Battery Health: Average — consider care")
else:
    print("Battery Health: Weak — consider replacement soon")

# ----- Charging Time Estimation -----
efficiency = 0.85
voltage = 5
remaining_mah = battery_capacity * (battery_percent / 100)
missing_mah = battery_capacity - remaining_mah
charger_ma = (charger_watt * 1000) / voltage
charging_hours = missing_mah / (charger_ma * efficiency) * 1.08
print(f"\nEstimated charging time to full: {charging_hours:.2f} hours")