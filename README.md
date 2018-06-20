# AICryptoTrading

This is the example code for "Bitcoin and crypto trading with Artificial Intelligence" hackathon at 
Holberton school https://www.meetup.com/Holberton-School/events/251802757/

The event will take place @HolbertonSchool the weekend of Friday, June 29, 2018, 5:00 PM to Sunday, July 1, 2018, 11:59 AM!

## Getting Started

### Files

The example consists of a jupyter notebook, python code and exchange price csv files for 2 pairs:
 * USD/BTC since 2012 every 5 minutes, high,low,close,open,volume
 * BTC/ETH since 2012 every 5 minutes, high,low,close,open,volume
 
### Dependencies

The easiest way to get all deep learning libraries and dependencies is to use docker, specifically this image:
ufoym/deepo:all-py27-jupyter

To learn more about this image: https://github.com/ufoym/deepo

### Runnning the code on docker

We prebuilt a Docker image based on ufoym/deepo:all-py27-jupyter that contains the code and 
the two exchange history csv files.
