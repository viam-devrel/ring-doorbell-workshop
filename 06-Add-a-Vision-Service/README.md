# Step 6: Add a Vision Service

The vision service connects your ML model to your camera. It takes frames from the camera, runs them through the model, and returns detection results (bounding boxes with labels and confidence scores).

## Add a Vision Service

1. In the Viam app, navigate to your machine's **CONFIGURE** tab.
2. Click **+** (Add Configuration Block).
3. Search for `mlmodel`.
4. Select **Vision / mlmodel**.
5. Name it `person-detector`.
6. Click **Add Component**.

## Configure the Vision Service

In the `person-detector` configuration panel:

1. Set **ML Model** to `mlmodel-1`.
2. Set **Default camera** to `camera-1`.
3. Click **Save**.

## How It Works

The vision service sits between the camera and the automation logic:

```
USB Webcam (camera-1)
       ↓
Vision Service (person-detector)
       ↓  runs frames through:
ML Model (mlmodel-1 / EfficientDet-COCO)
       ↓  returns:
Detections: [{ class: "Person", confidence: 0.87, bounding_box: {...} }, ...]
```

In Step 7, our automation code will ask `person-detector` for detections and check if any have the class `"Person"`.

## Test the Vision Service

On the **CONFIGURE** tab, expand the `person-detector` card and use the built-in test panel. Stand in front of the camera — you should see a bounding box with the label **"Person"**. Step away and it should disappear.

---

**Next step:** [Automate the Doorbell](../07-Automate-the-Doorbell/)
