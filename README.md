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

The docker image ufoym/deepo:all-py27-jupyter contains all the libraries needed to run either on CPU or GPU.
To test your code, assuming you checked out the project in your current working directory:

```bash
docker run -it -p 8888:8888 --ipc=host -v $PWD:/root ufoym/deepo:all-jupyter-py27 jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token= --notebook-dir='/root'
```

This will run a deep learning jupyter notebook on your machine, accessible at port 8888.
Use your browser to access http://localhost:8888 and open the file crypto_predict.ipynb to get started.
