import os
import subprocess

from appium.options.android import UiAutomator2Options
from appium import webdriver

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    pass


def _detect_android_udid() -> str | None:
    for key in ("APPIUM_UDID", "ANDROID_UDID", "ANDROID_SERIAL"):
        value = os.getenv(key)
        if value:
            return value

    try:
        output = subprocess.check_output(["adb", "devices"], text=True)
    except Exception:
        return None

    devices: list[str] = []
    for line in output.splitlines():
        line = line.strip()
        if not line or line.startswith("List of devices"):
            continue
        parts = line.split()
        if len(parts) >= 2 and parts[1] == "device":
            devices.append(parts[0])

    for serial in devices:
        if serial.startswith("emulator-"):
            return serial
    return devices[0] if devices else None


def test_google_search():
    udid = _detect_android_udid()
    caps = {"platformName": "Android", "appium:automationName": "UiAutomator2"}
    if udid:
        caps["appium:udid"] = udid
    caps["appium:deviceName"] = os.getenv("APPIUM_DEVICE_NAME", udid or "Android Emulator")

    options = UiAutomator2Options().load_capabilities(caps)

    appium_server_url = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
    driver = webdriver.Remote(appium_server_url, options=options)
    try:
        driver.find_element("xpath", "//android.widget.TextView[@content-desc='Photos']").click()
    finally:
        driver.quit()


# if __name__ == "__main__":
#     test_google_search()
