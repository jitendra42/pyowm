#!/usr/bin/env python

"""
Weather data classes and data structures.
"""

from pyowm.utils import converter

class Weather(object):
    """
    A databox containing raw weather data, such as pressure, temperature, etc.
    """

    def __init__(self, reference_time, sunset_time, sunrise_time, clouds, rain, 
                 snow, wind, humidity, pressure, temperature, status, 
                 detailed_status, weather_code, weather_icon_name):
        """
        reference_time - GMT UNIX time of weather measurement (long)
        sunset_time - GMT UNIX time of sunrise_time (long)
        sunrise_time - GMT UNIX time of sunset_time (long)
        clouds - cloud coverage percentage (int)
        rain - precipitation info (dict)
        snow - snow info (dict)
        wind - wind info (dict)
        humidity - atmospheric humidiy percentage (int) 
        pressure - atmospheric pressure info (dict)
        temperature - temperature info (dict)
        status - short weather status (str)
        detailed_status - detailed weather status (str)
        weather_code - OWM weather condition code (int)
        weather_icon_name - weather-related icon name (str)
        
        For reference about OWM weather codes and icons visit:
          http://bugs.openweathermap.org/projects/api/wiki/Weather_Condition_Codes
        """
        assert type(reference_time) is long or type(reference_time) is int, "'reference_time' must be an int/long"
        if long(reference_time) < 0:
            raise ValueError("'reference_time' must be greater than 0")
        self.__reference_time = long(reference_time)        
        assert type(sunset_time) is long or type(sunset_time) is int, "'sunset_time' must be a int/long"
        if long(sunset_time) < 0:
            raise ValueError("'sunset_time' must be greatear than 0")
        self.__sunset_time = long(sunset_time)
        assert type(sunrise_time) is long or type(sunrise_time) is int, "'sunrise_time' must be a int/long"
        if long(sunrise_time) < 0:
            raise ValueError("'sunrise_time' must be greatear than 0")
        self.__sunrise_time = long(sunrise_time)
        assert type(clouds) is int, "'clouds' must be an int"
        if clouds < 0:
            raise ValueError("'clouds' must be greater than 0")
        self.__clouds = clouds
        assert type(rain) is dict, "'rain' must be a dict"
        self.__rain = rain
        assert type(snow) is dict, "'snow' must be a dict"
        self.__snow = snow
        assert type(wind) is dict, "'wind' must be a dict"
        self.__wind = wind
        assert type(humidity) is int, "'humidity' must be an int"
        if humidity < 0:
            raise ValueError("'humidity' must be greatear than 0")
        self.__humidity = humidity
        assert type(pressure) is dict, "'pressure' must be a dict"
        self.__pressure = pressure
        assert type(temperature) is dict, "'temperature' must be a dict"
        self.__temperature = temperature
        assert type(status) is str, "'status' must be a str"
        self.__status = status
        assert type(detailed_status) is str, "'detailed_status' must be a str"
        self.__detailed_status = detailed_status
        assert type(weather_code) is int, "'weather_code' must be an int"
        self.__weather_code = weather_code
        assert type(weather_icon_name) is str, "'iconName' must be a str"
        self.__weather_icon_name = weather_icon_name

    def get_reference_time(self, timeformat='unix'):
        """
        Returns the GMT UNIX time of weather measurement
            format - how to format the result:
                unix (default) - returns a long
                iso - returns a ISO 8601-formatted str
        """
        if timeformat == 'unix':
            return self.__reference_time
        if timeformat == 'iso':
            return converter.unix_to_ISO8601(self.__reference_time)
        else:
            raise ValueError("Invalid value for parameter 'format'")
        


    def get_sunset_time(self, timeformat='unix'):
        """
        Returns the GMT UNIX time of sunset
            format - how to format the result:
                unix (default) - returns a long
                iso - returns a ISO 8601-formatted str
        """
        if timeformat == 'unix':
            return self.__sunset_time
        if timeformat == 'iso':
            return converter.unix_to_ISO8601(self.__sunset_time)
        else:
            raise ValueError("Invalid value for parameter 'format'")


    def get_sunrise_time(self, timeformat='unix'):
        """
        Returns the GMT UNIX time of sunrise
            format - how to format the result:
                unix (default) - returns a long
                iso - returns a ISO 8601-formatted str
        """
        if timeformat == 'unix':
            return self.__sunrise_time
        if timeformat == 'iso':
            return converter.unix_to_ISO8601(self.__sunrise_time)
        else:
            raise ValueError("Invalid value for parameter 'format'")


    def get_clouds(self):
        """Returns the cloud coverage percentage as an int"""
        return self.__clouds


    def get_rain(self):
        """Returns precipitation info as a dict"""
        return self.__rain


    def get_snow(self):
        """Returns snow info as a dict"""
        return self.__snow


    def get_wind(self):
        """Returns wind info as a dict"""
        return self.__wind


    def get_humidity(self):
        """Returns atmospheric humidity info as a dict"""
        return self.__humidity


    def get_pressure(self):
        """Returns atmospheric pressure info as a dict"""
        return self.__pressure


    def get_temperature(self):
        """Returns temperature info as a dict"""
        return self.__temperature


    def get_status(self):
        """Returns short weather status as a str"""
        return self.__status


    def get_detailed_status(self):
        """Returns detailed weather status as a str"""
        return self.__detailed_status


    def get_weather_code(self):
        """Returns OWM weather condition code as an int"""
        return self.__weather_code


    def get_weather_icon_name(self):
        """Returns weather-related icon name as a str"""
        return self.__weather_icon_name
        
        