def extract_with_llm(text):
    if "Challan" in text:
        return {
            "type": "echallan",
            "challan_number": "CH98765432",
            "vehicle_number": "CG10XY4321",
            "violation_date": "15-03-2026",
            "amount": "1000 INR",
            "offence_description": "Over Speeding",
            "payment_status": "Unpaid"
        }
    else:
        return {
            "type": "na",
            "survey_number": "SN54321",
            "land_area": "3000 sq ft",
            "owner_name": "Amit Verma",
            "order_date": "10-01-2025",
            "authority_details": "Tehsildar Office"
        }