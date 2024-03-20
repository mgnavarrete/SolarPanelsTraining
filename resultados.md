## Modelo 1:
| Class                           | Images | Instances | P     | R        | mAP50  | mAP50-95 |
|---------------------------------|--------|-----------|-------|----------|--------|----------|
| all                             | 23448  | 52514     | 0.49  | 0.277    | 0.209  | 0.12     |
| Tipo I - StringDesconectado     | 23448  | 2660      | 0.466 | 0.322    | 0.307  | 0.19     |
| Tipo II - StringCortoCircuito   | 23448  | 5261      | 1     | 0        | 0.00158| 0.000905 |
| Tipo III - ModuloCircuitoAbierto| 23448  | 4551      | 0.0378| 0.00593  | 0.0148 | 0.00663  |
| Tipo IV - BusBar                | 23448  | 10467     | 0.615 | 0.741    | 0.578  | 0.314    |
| Tipo V - ModuloCortoCircuito    | 23448  | 2287      | 0.342 | 0.629    | 0.362  | 0.252    |
| Tipo VI - CelulaCaliente        | 23448  | 19647     | 0.456 | 0.518    | 0.403  | 0.194    |
| Tipo VIII - PID                 | 23448  | 2         | 1     | 0        | 0.00119| 0.000835 |
| Tipo IX - JunctionBoxCaliente   | 23448  | 7639      | 0     | 0        | 0.0022 | 0.00139  |



## Modelo 2:
| Class                         | Images | Instances | P     | R       | mAP50  | mAP50-95 |
|-------------------------------|--------|-----------|-------|---------|--------|----------|
| all                           | 23448  | 52514     | 0.61  | 0.328   | 0.215  | 0.128    |
| Tipo I - StringDesconectado   | 23448  | 2660      | 1     | 0       | 0.00327| 0.00128  |
| Tipo II - StringCortoCircuito | 23448  | 5261      | 1     | 0       | 0      | 0        |
| Tipo III - ModuloCircuitoAbierto| 23448 | 4551     | 0.131 | 5.78e-05| 0.0197 | 0.00947  |
| Tipo IV - BusBar              | 23448  | 10467     | 0.584 | 0.918   | 0.62   | 0.374    |
| Tipo V - ModuloCortoCircuito  | 23448  | 2287      | 0.263 | 0.933   | 0.431  | 0.339    |
| Tipo VI - CelulaCaliente      | 23448  | 19647     | 0.417 | 0.575   | 0.416  | 0.19     |
| Tipo VIII - PID               | 23448  | 2         | 1     | 0       | 0      | 0        |
| Tipo XX - Tracker fuera de posicion | 23448 | 7639 | 0.485 | 0.195   | 0.228  | 0.111    |

## Modelo 3:
| Class                         | Images | Instances | P     | R       | mAP50  | mAP50-95 |
|-------------------------------|--------|-----------|-------|---------|--------|----------|
| all                           | 23448  | 52514     | 0.61  | 0.328   | 0.215  | 0.128    |
| Tipo I - StringDesconectado   | 23448  | 2660      | 1     | 0       | 0.00327| 0.00128  |
| Tipo II - StringCortoCircuito | 23448  | 5261      | 1     | 0       | 0      | 0        |
| Tipo III - ModuloCircuitoAbierto| 23448 | 4551     | 0.131 | 5.78e-05| 0.0197 | 0.00947  |
| Tipo IV - BusBar              | 23448  | 10467     | 0.584 | 0.918   | 0.62   | 0.374    |
| Tipo V - ModuloCortoCircuito  | 23448  | 2287      | 0.263 | 0.933   | 0.431  | 0.339    |
| Tipo VI - CelulaCaliente      | 23448  | 19647     | 0.417 | 0.575   | 0.416  | 0.19     |
| Tipo VIII - PID               | 23448  | 2         | 1     | 0       | 0      | 0        |
| Tipo XX - Tracker fuera de posicion | 23448 | 7639 | 0.485 | 0.195   | 0.228  | 0.111    |
