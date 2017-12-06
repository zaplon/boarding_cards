# boarding_cards
## How to use
1. cd to the project directory
2. install deps with
```python
pip install -r deps.txt
```
3. run tests by running 
```python
py.test
```
4. use api from python with
```python
from api import calculate_trip
calculate_trip([{'destination': 'point2', 'departure': 'point1', 'seat': 'D12', 'extra': 'baggage will be transfered', 'mean_id': 'flight OZX/325'}, ...])
```
