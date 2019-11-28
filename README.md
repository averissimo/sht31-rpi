## SHT31-D Sensor logging in Raspberry pi model B

This library saves temperature and humidity data in a local Mongo database and generates plots.

### How to use it?

#### Install a virtualenv

```
$ virtualenv -p python3 .
$ source bin/activate
$ pip install -r requirements
```

#### One time run that prints to screen

`$ python one.py`

#### Collect data for a minute

`python sensor.py`

to send a udp packet for the collecting agent. This requires that there's an agent listening and handling the data.

#### To make periodical readings

Create a cron job that runs every minute for the `sensor.py` script.

```
# for readings every minute
# m h dom mon dow user	command
*  *	* * *	root    python /path/to/sensor.py
```

## Dependencies

see `requirements.txt`

## License

GNU General Public License Version 3, 29 June 2007

See `LICENSE` file for more information
