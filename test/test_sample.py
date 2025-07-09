# test_sample.py
# Basic test structure placeholder

def test_kelvin_to_celsius():
    from weather_app import kelvin_to_celsius
    assert kelvin_to_celsius(273.15) == 0.0
    assert kelvin_to_celsius(300) == 26.85
    assert isinstance(kelvin_to_celsius(280), float)

if __name__ == "__main__":
    print("✅ Running simple test...")
    test_kelvin_to_celsius()
    print("✅ All tests passed!")
