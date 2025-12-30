from .asyncherosms import AsyncHeroSms, AsyncHeroSmsException, NoSMSException
from typing import Coroutine
import logging
from aiohttp.typedefs import StrOrURL

async def testApi(apiName: str, apiRoutine: Coroutine):
    print(apiName)
    try:
        response = await apiRoutine
        print(response)
        return response
    except NoSMSException:
        print("No SMS")
    except AsyncHeroSmsException as e:
        print("AsyncHeroSmsException:", e)
    return None

async def testAsyncHeroSms(apiKey: str, httpProxy: StrOrURL = None, connectionErrorRetries: int = 0,
                               country: str = 'US', service: str = 'mm', max_price: float = 0.08,
                               operator: str = '', phone_exception: str = '', ref: str =''):
    logger = logging.Logger('testHeroSms')

    logger.setLevel(logging.DEBUG)

    log_format = "%(asctime)s [%(levelname)s] %(message)s"
    log_path = './log/test.log'

    logFormatter = logging.Formatter(log_format)
    fileHandler = logging.FileHandler(log_path, encoding='utf8')
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    aherosms = AsyncHeroSms(apiKey, logger=logger, http_or_socks_proxy=httpProxy, connection_error_retries=connectionErrorRetries, ref=ref)

    print('--- aherosms test ---')

    await testApi('getBalance()', aherosms.getBalance())
    await testApi('getCountries()', aherosms.getCountries())
    await testApi('getServicesList()', aherosms.getServicesList())
    cc = aherosms.getCountryCode(country)
    await testApi(f'getPrices("{service}","{cc}")', aherosms.getPrices(service,cc))
    await testApi(f'getOperators("{service}","{cc}")', aherosms.getOperators(service,cc))
    await testApi(f'getTopCountriesByService(""{service}")', aherosms.getTopCountriesByService(service))
    number = await testApi(f'getNumberV2("{service}","{cc}","{max_price}")', aherosms.getNumberV2(service,cc,str(max_price),operator,phone_exception))
    if number:
        await testApi(f'getSMS("{number["id"]}")', aherosms.getSMS(number['id']))
        await testApi(f'setStatus("8", "{number["id"]}")', aherosms.setStatus('8', number['id']))

    print('--- aherosmss test completed ---')