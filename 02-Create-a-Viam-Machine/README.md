# Step 2: Create a Viam Machine

Viam is the platform we'll use to configure and control all of our hardware. In this step, you'll join the workshop organization, then create a machine in the Viam cloud and install the Viam agent on your Pi.

## Join the Workshop Organization

1. Go to [app.viam.com](https://app.viam.com/) and create a free account (or sign in if you already have one).
2. **Share your account email address with the workshop organizer** — they will add you to the workshop organization.
3. Wait for the organizer to confirm you've been added.
4. Refresh the page and select the workshop organization from the organization dropdown in the top right.

## Create a New Machine

1. In the left sidebar, click on the **Location** provided for the workshop.
2. Click **+ New machine**.
3. Give your machine a name that matches your Pi's hostname (e.g. `doorbell-1`, `doorbell-2`).
4. Click **Add machine**.

You'll land on the machine's setup page.

## Install the Viam Agent on the Pi

Follow the setup instructions in the Viam app until you reach the step that shows a `curl` command to copy.

> **Your Pi's credentials:** The workshop organizer will give you a name unique to your Pi (e.g. `doorbell-1`). This name is used as the hostname, username, and password.

SSH into your Pi from your computer's terminal:

```bash
ssh <NAME>@<NAME>.local
```

Enter your name as the password when prompted. Then paste and run the `curl` command from the Viam setup instructions. The script will install the Viam agent and start it automatically.

## Verify the Connection

Back in the Viam app, watch the machine status indicator at the top of the page. Within about 30 seconds it should turn **green** and show **Live**.

Once your machine shows as live, the Pi is connected to the Viam cloud and ready to be configured.

---

**Next step:** [Configure the Camera](../03-Configure-the-Camera/)
