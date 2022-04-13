from __future__ import annotations
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

from .tuyalock import TuyaLock

import logging

DOMAIN = "korich_tuya_lock"
_LOGGER = logging.getLogger(__name__)


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Open Service."""

    access_id = config[DOMAIN]["access_id"]
    access_key = config[DOMAIN]["access_key"]
    device_id = config[DOMAIN]["device_id"]

    tuyalock = TuyaLock(
        apiRegion="us",
        apiKey=access_id,
        apiSecret=access_key)

    def open_service(call: ServiceCall) -> None:
        """Open Service."""
        response = tuyalock.unlock(device_id)

    def close_service(call: ServiceCall) -> None:
        """Close Service"""
        response = tuyalock.lock(device_id)

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'open', open_service)
    hass.services.register(DOMAIN, 'close', close_service)

    # Return boolean to indicate that initialization was successfully.
    return True

