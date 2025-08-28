from typing import Any, Dict, Optional

from .base import Resource
from ..constants.url import URL
from ..constants.device import DeviceMode
from ..errors import BadRequestError


class DeviceActivity(Resource):
    def __init__(self, client=None):
        super(DeviceActivity, self).__init__(client)
        self.base_url = URL.V1 + URL.DEVICE_ACTIVITY_URL
    
    def _validate_device_mode(self, mode: Optional[str]) -> Optional[str]:
        """
        Validate device communication mode
        
        Args:
            mode: Device communication mode ("wired" or "wireless")
        
        Returns:
            Validated mode or None if mode is None
            
        Raises:
            BadRequestError: If mode is invalid
        """
        if mode is not None:
            if mode not in (DeviceMode.WIRED, DeviceMode.WIRELESS):
                raise BadRequestError("Invalid device mode. Allowed values are 'wired' and 'wireless'.")
            return mode
        return None

    def create(self, data: Dict[str, Any], mode: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Create a new device activity for POS gateway
        
        Args:
            data: Dictionary containing device activity data in the format expected by rzp-pos-gateway
            mode: Device communication mode ("wired" or "wireless")
        
        Returns:
            DeviceActivity object
        """
        validated_mode = self._validate_device_mode(mode)

        url = self.base_url
        return self.post_url(url, data, mode=validated_mode, use_public_auth=True, **kwargs)

    def get_status(self, activity_id: str, mode: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Get the status of a device activity
        
        Args:
            activity_id: Activity ID to fetch status for
            mode: Device communication mode ("wired" or "wireless")
        
        Returns:
            DeviceActivity object with current status
        """
        if not activity_id:
            raise BadRequestError("Activity ID must be provided")

        validated_mode = self._validate_device_mode(mode)

        url = f"{self.base_url}/{activity_id}"
        return self.get_url(url, {}, mode=validated_mode, use_public_auth=True, **kwargs) 