# domain_math.py

def calculate_carbon_credit(energy_mwh: float, fuel_type: str) -> dict:
    baseline_factor = 0.70  # tCO2/MWh
    co2_emitted = energy_mwh * (0.25 if fuel_type == "biofuel" else baseline_factor)
    co2_avoided = (energy_mwh * baseline_factor) - co2_emitted
    credits_earned = co2_avoided * 1.0  
    
    return {
        "energy_produced_mwh": energy_mwh,
        "co2_avoided_tons": round(co2_avoided, 2),
        "carbon_credits": round(credits_earned, 2)
    }

def optimize_htl_biofuel(feedstock_mass_kg: float, temp_celsius: float) -> dict:
    if 300 <= temp_celsius <= 350:
        efficiency = 0.85
    else:
        efficiency = 0.65
        
    bio_oil_yield_kg = feedstock_mass_kg * 0.35 * efficiency
    green_h2_yield_kg = feedstock_mass_kg * 0.08 * efficiency
    
    return {
        "feedstock_kg": feedstock_mass_kg,
        "optimal_temp_range": "320°C - 340°C",
        "bio_oil_yield_kg": round(bio_oil_yield_kg, 2),
        "green_hydrogen_yield_kg": round(green_h2_yield_kg, 2)
    }