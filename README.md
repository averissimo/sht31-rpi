## SHT31-D Sensor logging in Raspberry pi model B

This library saves temperature and humidity data in a local Mongo database and generates plots.

### How to use it?

run `python sensor.py` to add an entry to a local mongo database named `sensor` in a collection named `readings`.

Run `plot.py` to plot the results

#### To make periodical readings

Create a cron job that runs every X time for the `sensor.py` script

```
# for readings every minute
# m h dom mon dow user	command
*  *	* * *	root    python /path/to/sensor.py
```

## Dependencies

It depends on Python and the following libraries:
- smbus
- pymongo
- matplotlib
- dateutil.parser

## License

GNU General Public License Version 3, 29 June 2007

See `LICENSE` file for more information
