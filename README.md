# boarding_cards
## How to use
1. use python 3
2. cd to the project directory
3. install deps with
```python
pip install -r deps.txt
```
4. run tests by running 
```python
py.test
```
5. use api from python with
```python
from api import calculate_trip
calculate_trip([{'destination': 'point2', 'departure': 'point1', 'seat': 'D12', 'extra': 'baggage will be transfered', 'mean_id': 'flight OZX/325'}, ...])
```
