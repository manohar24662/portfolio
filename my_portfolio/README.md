# Durga Manohar Bachu — Portfolio

## Run locally

From the project folder in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m streamlit run resume/app.py
```

The `192.168.x.x` address is a local-network address. It only works while the app is running and for devices on the same Wi-Fi/network.

## Publish a public link

1. Create a GitHub repository and upload the project files. Include `resume/app.py`, `resume/style.css`, `resume/dp.jpg`, and `resume/requirements.txt`; do not upload `.venv`.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/) and choose **Create app**.
3. Select that repository, its branch, and `resume/app.py` as the app file.
4. In **Advanced settings**, choose Python 3.14 to match the local project, then deploy.

Streamlit will provide a public `*.streamlit.app` URL. The public deployment runs independently of VS Code and your computer. See the [deployment guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy) for details.
