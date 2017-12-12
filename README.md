# boarding_cards
## How to use
1. use python 3 (tested with python 3.4, 3.5, 3.6)
  * you can also tray different python versions with docker. For example for python 3.5 run (in the project directory):
```bash
docker run -v $PWD:/code -w /code -it python:3.5 bash
```
2. cd to the project directory
3. install deps with
```python
pip3 install -r deps.txt
```
4. run tests from py.test
```python
py.test
```
5. use api from python with
```python
from api import calculate_trip
calculate_trip([{'destination': 'point2', 'departure': 'point1', 'seat': 'D12', 'extra': 'baggage will be transfered', 'mean_id': 'flight OZX/325'}, ...])
```
