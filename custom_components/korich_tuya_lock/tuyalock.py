"""
Store all the config neeeded
"""

import tinytuya as tuya

class TuyaLock(tuya.Cloud):
    """Gets the lock key from tuya"""
    def _getlockkey(self, deviceid):
        """
        Send a command to the device
        """
        uri = f'devices/{deviceid}/door-lock/password-ticket'
        response_dict = self._tuyaplatform(uri,action='POST')

        return response_dict

    def unlock(self, deviceid):
        """
        Unlock the door
        """
        ticket_id = self._getlockkey(deviceid)['result']['ticket_id']
        uri = f'devices/{deviceid}/door-lock/password-free/open-door'
        response_dict = self._tuyaplatform(uri,action='POST', post={"ticket_id": ticket_id})

        return response_dict

    def lock(self, deviceid):
        """
        Lock the door
        """
        return self.sendcommand(deviceid, {
            "commands":[
                {
                    "code": "manual_lock",
                    "value":True
                }
            ]
        })
