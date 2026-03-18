# Step 5: Add a Person Detection Model

Now we'll add a machine learning model to the Pi. We'll use a pre-trained model from the Viam model registry that can detect people (and many other objects) without requiring any training.

## Add an ML Model Service

1. In the Viam app, navigate to your machine's **CONFIGURE** tab.
2. Click **+** (Add service).
3. Search for `tflite_cpu`.
4. Select **ML model / tflite_cpu**.
5. Keep the default name `mlmodel-1`.
6. Click **Create**.

## Select a Model from the Registry

1. In the `mlmodel-1` configuration panel, click **Select model**.
2. Click the **Registry** tab.
3. Search for `EfficientDet-COCO`.
4. Select the model and click **Choose**.

The **EfficientDet-COCO** model is a lightweight object detection model trained on the COCO dataset. It detects 80 common object types including "Person". Because it uses TensorFlow Lite, it runs efficiently on the Raspberry Pi's CPU without needing a GPU.

5. Click **Save**.

## What Happens Next

After saving, Viam will download the model to your Pi in the background. This may take a minute depending on your internet connection. You can check the machine logs in the **LOGS** tab if you want to confirm the download completes.

---

**Next step:** [Add a Vision Service](../06-Add-a-Vision-Service/)
