# Python Juicenet

Access to the Chargepoint EV charger API


## Example

```python
import aiohttp
import asyncio
import pychargepoint

async def main():
  async with aiohttp.ClientSession() as session:
    api = pychargepoint.Api('ACCESS_TOKEN', session)
    devices = await api.get_devices()
    charger = devices[0]
    await charger.update_state()
    print(charger.voltage) # 240
    await charger.set_override(True) # Charge the car now ignoring the schedule

asyncio.run(main())
```
