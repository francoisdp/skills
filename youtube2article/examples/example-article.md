---
type: study
title: "How a Kalman Filter Works"
date: 2026-06-13
source: youtube
status: complete
channel: Example Engineering Channel
video_url: https://www.youtube.com/watch?v=EXAMPLE
tags:
  - estimation
  - kalman-filter
  - full-transcript
---

# How a Kalman Filter Works

**Channel:** Example Engineering Channel
**Video:** [YouTube Link](https://www.youtube.com/watch?v=EXAMPLE)
**Duration:** 12:34

> Note on this example: a real run of the skill captures screenshots from the video and places them inline at their timestamps, shown as `![](images/frame_0153.jpg)`. This sample uses text only, since it ships without a video, so picture a captured frame at each point where the narration refers to the diagram.

A **Kalman filter** estimates the state of a system from noisy measurements, so it answers a practical question, which is where the system actually is when every sensor reading is imperfect. The filter keeps a running estimate together with a measure of how uncertain that estimate is, then updates both every time a new measurement arrives.

## The two steps

The filter runs two steps in a loop. The first step is the prediction, where the filter uses a model of how the system moves to project the current estimate forward in time, which also grows the uncertainty because the model is not perfect. The second step is the update, where a new measurement is folded in, which pulls the estimate toward the measurement and shrinks the uncertainty.

The balance between the two is central to the method. When the measurement is trusted more than the model, the estimate moves a long way toward it. When the model is trusted more, the estimate barely moves. That balance is set by the **Kalman gain**, which the filter recomputes on every step from the two uncertainties.

## Why it works

The filter is the best linear estimator when the noise is well behaved, which means it produces the estimate with the smallest expected error among all linear combinations of the measurements. That property is why it became the standard tool in navigation and control, from spacecraft attitude estimation to the position fix in a phone.

## Connections

- [[State estimation]]
- [[Sensor fusion]]
