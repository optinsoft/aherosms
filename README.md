# Async API wrapper for hero-sms.com

## Installation

```bash
pip install git+https://github.com/optinsoft/aherosms.git
```

## Usage

```python
from aherosms import AsyncHeroSms
import asyncio

async def test(apiKey: str):
    aherosms = AsyncHeroSms(apiKey)
    print("getBalance\n", await aherosms.getBalance())    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test('PUT_YOUR_API_KEY_HERE'))
```
