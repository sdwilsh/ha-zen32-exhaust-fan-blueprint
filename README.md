# ha-zen32-exhaust-fan-blueprint
A blueprint to use a [Zooz ZEN32 Scene Controller](https://www.getzooz.com/zooz-zen32-scene-controller/) to control an exhaust fan.

[![Import Blueprint in Home Assistant](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fsdwilsh%2Fha-zen32-exhaust-fan-blueprint%2Fmain%2Fzen32_exhaust_fan.yaml)

You can also see the discussion about this Blueprint [in the Home Assistant Community Blueprint Exchange](https://community.home-assistant.io/t/zooz-zen32-scene-controller-for-timed-exhaust-fan-control/452275).

# Requirements
* [Timer](https://www.home-assistant.io/integrations/timer/) entity to track time remaining for the exhaust fan 
* [Switch](https://www.home-assistant.io/integrations/switch/) entity to turn the fan on/off (can be the scene controller if wired that way)
* Device for the scene controller.

# Diagram

```
┌────────────────────────────────────┐
│                                    │
│ ┌─┐ Blue when off                  │
│ └─┘ White w/ time left > 45m       │
│     Green when on w/ no time set   │
│                                    │
│                                    │
│                                    │
│                                    │
│                                    │
│                                    │
│                                    │
│                                    │
│                                    │
│ 60m/off                            │
└────────────────────────────────────┘

┌────────────────┐  ┌────────────────┐
│     White w/   │  │     White w/   │
│ ┌─┐ time left  │  │ ┌─┐ time left  │
│ └─┘ <= 10m     │  │ └─┘ > 20m and  │
│                │  │     <= 30m     │
│                │  │                │
│                │  │                │
│ 10m            │  │ 20m            │
└────────────────┘  └────────────────┘

┌────────────────┐  ┌────────────────┐
│     White w/   │  │     White w/   │
│ ┌─┐ time left  │  │ ┌─┐ time left  │
│ └─┘ > 20m and  │  │ └─┘ > 30m and  │
│     <= 30m     │  │     <= 45m     │
│                │  │                │
│                │  │                │
│ 30m            │  │ 45m            │
└────────────────┘  └────────────────┘
```

# Contributing

## Setup

```
python3.10 -m venv .venv
source .venv/bin/activate

# Install Requirements
pip install -r requirements.txt

# One-Time Install of Commit Hooks
pre-commit install
```

## Testing

Tests are run with `pytest`.
