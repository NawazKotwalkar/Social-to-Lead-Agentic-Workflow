# tools.py

def mock_lead_capture(name: str, email: str, platform: str):
    """
    Mock backend API call to capture a high-intent lead.
    This function should ONLY be called when all required
    details are already collected.
    """
    print(f"Lead captured successfully: {name}, {email}, {platform}")

    return {
        "status": "success",
        "name": name,
        "email": email,
        "platform": platform
    }
