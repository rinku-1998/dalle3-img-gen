# dalle3-img-gen
DALL-E 3 圖片生成工具

## 環境
- Python 3.9
- Poetry 1.7.1
- OpenAI 1.12.0

## 使用指南
1. 安裝套件

```
poetry install
```

2. 修改 `env.yaml` 的 `OPENAPI_KEY`
3. 開始生成！

```
python generate.py -p "A Chef is cooking"
```

4. 生成後的圖片放在 `output/` 內

## 參數
可以透過下面的參數調整生成的圖片：

- `-p`: Promp，魔法咒語。
- `-m`: 生成圖片的模型，預設使用 DALL-E 3。
- `-s`: 生成圖片的大小，預設是 1024x1025。
- `-q`: 生成圖片的品質，預設是 standard。
- `-o`: 儲存位置，預設存在 `output/`。


