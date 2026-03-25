# Step 3: Configure the Camera

Now that your machine is connected, let's add the USB webcam as a component in Viam.

## Plug In the Webcam

Connect your USB webcam to one of the Raspberry Pi's USB ports.

## Add a Camera Component

1. In the Viam app, navigate to your machine's **CONFIGURE** tab.
2. Click **+** (Add Configuration Block).
3. Search for `webcam`.
4. Select **camera / webcam**.
5. Name it `camera-1`.
6. Click **Create**.

The camera component will appear in your configuration. Leave the `video_path` attribute blank — Viam will auto-detect the webcam.

7. Click **Save** in the top right corner.

## Verify the Camera Feed

On the **CONFIGURE** tab, expand the `camera-1` component card. Expand the built-in test panel at the bottom of the card to stream a live preview and confirm the camera is working.

---

**Next step:** [Configure the LED](../04-Configure-the-LED/)
