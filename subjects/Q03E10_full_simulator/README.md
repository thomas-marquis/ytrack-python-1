# Full battle simulator

## Instructions

Reuse file `battle_simulator.py` with class `Simulator`. add a constructor and create a method `fight`:

* the constructor should take 2 parameters: 
  * the attacker fleet (a `Fleet` class instance)
  * the defender fleet
* this method:
  * does not accept any parameters
  * returns noting
  * simulate a whole battle (see bellow)

**Specifications:**

There are 3 steps in a battle:

![legend](battle_legend.png)

* **Step 1:** battleships vs battleships

![step 1](battle_phase_1.png)

* **Step 2:** fighters vs fighters

![step 2](battle_phase_2.png)

* **Step 3:** all surviving fighters and battleships

![step 3](battle_phase_3.png)


**Tips**

* Use both previous private methods to simulate each step.


## Usage

Here is a possible `test.py` to test your functions:

```python
import zzzz

if __name__ == '__main__':
    print(zzzz)
```

```bash
$ python test.py
????
```


## Notions

* [xxxx](#)
