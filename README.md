# Phone Number Locator

This project is a Python application that allows users to input a phone number with a country code and retrieve information about its location and service provider. It utilizes various libraries for phone number parsing, geocoding, and mapping to provide a comprehensive view of the phone number's details.

## Features

- **Phone Number Parsing:** Uses `phonenumbers` library to parse and validate phone numbers.
- **Location Detection:** Retrieves the geographic location (country) of the phone number using `phonenumbers.geocoder`.
- **Service Provider Information:** Identifies the service provider (carrier) associated with the phone number using `phonenumbers.carrier`.
- **Mapping:** Integrates with `folium` library to generate an interactive map pinpointing the approximate location of the phone number based on its country.
- **Geocoding API:** Uses OpenCage Geocoder API for converting location names into geographic coordinates.

## Technologies Used

- Python
- `phonenumbers` library
- `folium` library
- OpenCage Geocoder API

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/phone-number-locator.git
   cd phone-number-locator
   ```

2. **Install dependencies:**

   Make sure you have Python installed. Then install the required libraries using pip:

   ```bash
   pip install phonenumbers folium opencage
   ```

3. **Get API key:**

   Sign up for an API key at [OpenCage Geocoder](https://opencagedata.com/) and replace `"YOUR_API_KEY"` in the code with your actual API key.

## Usage

1. **Run the application:**

   Execute the Python script `phone_locator.py`:

   ```bash
   python phone_locator.py
   ```

2. **Input a phone number:**

   Enter the phone number with the country code when prompted.

3. **View Results:**

   The application will display:

   - Validity of the phone number.
   - Country location of the phone number.
   - Service provider (carrier) information.
   - Generates an HTML file (`mylocation.html`) with an interactive map showing the approximate location.

## Example

```plaintext
Enter Your number with Country Code: +15551234567
Valid: True
Location: United States
Service Provider: Verizon Wireless
Latitude: 37.7749
Longitude: -122.4194
```

## Contributing

Contributions are welcome! Fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
# Phone-Number-Locater
