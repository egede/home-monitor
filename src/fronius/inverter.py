from framework.widget import widget

import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class inverter(widget):
    """Communicate with the Fronius inverter RESTful API and create plots."""

    def __init__(self, geometry, updateinterval, server='http://froniusinverter'):
        super().__init__(geometry, updateinterval)
        reply = self._version(server)
        if reply['APIVersion'] != 1:
            print('No support for Fronius API version different from 1')
            raise ConnectionError
        self._url = server + reply['BaseURL']

    def _version(self, server):
        r = requests.get(server + '/solar_api/GetAPIVersion.cgi')
        r.raise_for_status()
        return r.json()

    def _get(self, script, payload):
        r = requests.get(self._url + script, params=payload)
        r.raise_for_status()
        return r.json()

    @property
    def power(self):
        """The instantaneous power output of the inverter measured in W."""
        reply = self._get('GetInverterRealtimeData.cgi', {'Scope': 'System'})
        return reply['Body']['Data']['PAC']['Values']['1']

    def power_history(self, start=None, end=None):
        """Get a table of average power vs time. Table will start at the beginning of the start date 
        and end at the end of the end date. The start and end times are to be datetime objects
        but only the date (and bot the time part) are taken into account. Default start is yesterday 
        and default end today.

        Example:
        now = datetime.datetime.now()
        week_ago = now - datetime.timedelta(days=7)
        times, power = i.power_history(week_ago, now)

        where times is a list of datetime objects and power a list of the corresponding 
        average power in W.
"""
        now = datetime.now()
        if start is None:
            start = now - timedelta(days=1)
        if end is None:
            end = now

        startdate = start.strftime('%d.%m.%Y')
        enddate = end.strftime('%d.%m.%Y')

        reply = self._get('GetArchiveData.cgi',
                          {'Scope': 'System',
                           'StartDate': startdate,
                           'EndDate': enddate,
                           'Channel': 'EnergyReal_WAC_Sum_Produced'}
                          )

        energies = reply['Body']['Data']['inverter/1']['Data']['EnergyReal_WAC_Sum_Produced']['Values']

        elist = [[int(k), v] for k, v in energies.items()]
        elist.sort()

        interval = elist[1][0] - elist[0][0]
        offset = datetime.strptime(startdate, '%d.%m.%Y')
        times = [offset + timedelta(seconds=p[0]) for p in elist]
        power = [p[1] / interval * 3600 for p in elist]

        return times, power

    def update(self):
        times, power = self.power_history()

        fig, ax = plt.subplots()

        ax.plot(times, power)
        fig.savefig('test.png')
