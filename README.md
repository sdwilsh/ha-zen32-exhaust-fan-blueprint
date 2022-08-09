# ha-zen32-exhaust-fan-blueprint
A blueprint to use a [Zooz ZEN32 Scene Controller](https://www.getzooz.com/zooz-zen32-scene-controller/) to control an exhaust fan.

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
│                                    │
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
