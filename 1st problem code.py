def normalize_company_name(company_name):
    """
    Converts company name variations into a standard format:
    'CAF SoftSol India Pvt Ltd.'
    """

    # Handle empty or null values gracefully
    if not company_name or not isinstance(company_name, str):
        return None

    name = company_name.strip().lower()

    # Known CAF variations
    caf_variations = [
        "caf softsol",
        "caf solution",
        "caf softsolution",
        "caf softsolution india pvt limited",
        "caf softsol india"
    ]

    if any(variant in name for variant in caf_variations):
        return "CAF SoftSol India Pvt Ltd."

    # Return formatted value for unknown companies
    return company_name.title()
