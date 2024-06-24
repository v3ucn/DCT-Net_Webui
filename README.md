<div align="center">

Based on https://github.com/menyifang/DCT-Net


</div>

------


### Quick Install with Conda

```bash
conda create -n venv python=3.9
conda activate venv
```


#### Pip Packages

```bash
pip install "modelscope[cv]==1.3.2" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html
pip install "modelscope[multi-modal]==1.3.2" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html
```

```bash

pip install "tensorflow<2.11"
```


#### FFmpeg

##### Conda Users
```bash
conda install ffmpeg
```

##### Ubuntu/Debian Users

```bash
sudo apt install ffmpeg
sudo apt install libsox-dev
conda install -c conda-forge 'ffmpeg<7'
```

##### MacOS Users

```bash
brew install ffmpeg
```

##### Windows Users

```bash
winget install ffmpeg
```

or

```
choco install ffmpeg
```

## how to use

```
python3 app.py
```

![avatar](demo.png)

## Credits

https://github.com/menyifang/DCT-Net



