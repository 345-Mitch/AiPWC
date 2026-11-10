# AiPWC

Conversion of a 2019 Sea-Doo RXP-X 300 into a remotely operated / autonomous surface vessel (USV).

| Platform | Detail |
|---|---|
| Hull | 2019 Sea-Doo RXP-X 300 |
| Engine | Rotax 1630 ACE, supercharged and intercooled, 300 hp |
| ECU | Bosch ME17.8.5 |
| Throttle | iTC (throttle-by-wire) |
| Reverse / brake | iBR (electronic reverse gate) |
| Steering | Mechanical push-pull cable to the jet nozzle |

## Documents

| Phase | Document |
|---|---|
| 1 | [Systems architecture and technical design](docs/01-architecture.md) |
| 2 | [Bill of materials and sourcing matrix](docs/02-bom.md) |
| 2 | [Parts summary and where to buy](docs/03-sourcing.md) |
| 3 | [Design concept and mock-ups](docs/04-design-concept.md) |

## Status

Design phase. Nothing in these documents has been built or tested on the craft.
Figures marked **(verify)** are engineering estimates or recollections of the
platform that must be confirmed against the BRP shop manual and by measurement
before hardware is ordered or wiring is cut.

## Safety

This is a 300 hp, roughly 65 mph craft with a gasoline engine in a closed hull.
The design rules that everything else follows from:

1. The emergency stop is hardware only and does not depend on the autopilot, the companion computer, or any data link.
2. Every interface fails to the stock state: de-energised means factory throttle lever (idle), factory iBR lever, and engine stopped.
3. Anything that can spark inside the hull is ignition protected (SAE J1171 / ISO 8846) or sealed.
4. A jet craft has no steering without thrust. Stopping the engine is a stop, not a manoeuvre, so speed caps and geofences do the routine work.
