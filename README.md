# Bluepill Concealed Sandbox

### Start the Sandbox
Use Docker to run the container from the working directory

```bash
docker run -it -v `pwd`:/bluepill doughgle/bluepill-sandbox sh
```

### Execute the malware under test (MUT)

```bash
gdb --eval-command=run ./mut
```
