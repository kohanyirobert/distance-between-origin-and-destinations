# About

Script that reads

- an origin location (city name, address, etc.),
- a distance limit given in kilometers,
- and an arbitrary number of destination locations

from `stdin`, in *this* order and prints destinations to `stdout` that are located closer to the origin than the given limit.

**Note**: use the `API_KEY` environment variable to provide Google API key.

## Example

```
cat a.txt
```

```
Budapest
200
Miskolc
New York
```

```
API_KEY=<your-key> python3 main.py < a.txt > b.txt
```

```
cat b.txt
```

```
Miskolc
```
