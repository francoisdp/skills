# Edge AI for Remote Monitoring

Edge AI runs models on local hardware near the sensor rather than sending data to the cloud, so it suits sites with poor connectivity. This note is the input that the example deck was built from, so you can compare the source with `example-deck.pdf`.

## Why it matters

Latency drops because inference happens on site, while bandwidth cost falls because only results travel upstream. Privacy improves too, since raw data need not leave the device. See [[Bandwidth costs]] for the detail.

## Where it fits

Remote monitoring of equipment, agriculture and infrastructure all benefit, because these sites are often far from reliable networks. The trade-off is the limited compute on the device, which caps the model size.

## What to watch

Model drift is the main risk, so a retraining loop matters. Power budget is the second constraint on solar or battery sites. See [[Model drift]].
