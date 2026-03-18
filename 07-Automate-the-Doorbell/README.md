# Step 7: Automate the Doorbell

Time to connect detection to the LED! We'll use Viam's **inline module** feature to write the automation logic directly in the Viam app — no terminal, no SDK install, no API keys required.

## How Inline Modules Work

An inline module is a Python (or Go) service you write directly in the Viam browser editor. When you click **Save & Deploy**, Viam builds it in the cloud and deploys it to your machine automatically. We'll use a **Continuous job** to call the module's logic on a loop, checking for people and toggling the LED.

## Create the Inline Module

1. In the Viam app, navigate to your machine's **CONFIGURE** tab.
2. Click **+** → **Control code**.
3. Select **Viam-hosted** as the hosting option.
4. Name the module `doorbell`.
5. Select **Python**.
6. Click **Create module**.

The browser-based code editor will open with a template.

## Paste the Code

Replace all the template code with the contents of [`doorbell.py`](doorbell.py) from this directory.

The code:
- Declares `board-1` and `person-detector` as dependencies
- In `do_command`: gets detections from the camera, checks if any detection has the class `"Person"` with confidence > 0.5, and sets GPIO pin 17 high (LED on) or low (LED off)
- Returns `{"person_detected": true/false}` so you can see the result in the CONTROL tab

## Deploy the Module

1. Click **Save & Deploy** in the browser editor.
2. Viam will build the module in the cloud — this typically takes 2–5 minutes.
3. Watch the build status; if it fails, click **View Logs** to see the error.

## Add Dependencies

Once the module is deployed:

1. Find the `doorbell` service card in the CONFIGURE tab.
2. In the **Depends on** section, add `board-1` and `person-detector`.
3. Click **Save**.

## Add a Continuous Job

To run the detection loop automatically:

1. Click **+** → **Job**.
2. Name it `doorbell-loop`.
3. Click **Create**.
4. Set the schedule to **Continuous**.
5. Set the resource to `doorbell`.
6. Set the DoCommand payload to `{}`.
7. Click **Save**.

The job will call `do_command` continuously in a tight loop, checking for people and updating the LED.

## Test It

Stand in front of the camera — the LED should light up within a second or two.

Step away — the LED should turn off.

You can also test manually:
1. Go to the **CONTROL** tab.
2. Find the `doorbell` card.
3. In the **DoCommand** section, enter `{}` and click **Execute**.
4. The response will show `{"person_detected": true}` or `{"person_detected": false}`.

## Congratulations!

You've built a working smart doorbell! Your Raspberry Pi is now:
- Streaming video from a USB webcam
- Running a person detection ML model on every frame
- Lighting an LED in real time when a person is detected
- All managed through the Viam cloud platform

---
