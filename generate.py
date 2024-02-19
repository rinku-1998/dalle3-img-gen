import httpx
from config import Config
from openai import OpenAI
from pathlib import Path
from urllib.parse import urlparse

config = Config()


def gen_img(prompt: str,
            model: str = 'dall-e-3',
            size: str = '1024x1024',
            quality: str = 'standard',
            output_dir: str = 'output/') -> None:

    # 1. 建立 OpenAI Client
    client = OpenAI(api_key=config.OPENAI_KEY)

    # 2. 生成圖片
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=1,
    )

    # 3. 剖析網址
    url = response.data[0].url
    r = httpx.get(url)
    o = urlparse(url)

    # 4. 存檔Ｆ
    save_name = Path(o.path).name
    save_path = Path(output_dir, save_name)
    with open(save_path, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',
                        '--prompt',
                        type=str,
                        default='a cute cat with a hat on',
                        help='Prompt to generate image')
    parser.add_argument('-m',
                        '--model',
                        type=str,
                        default='dall-e-3',
                        help='Model to generate image')
    parser.add_argument('-s',
                        '--size',
                        type=str,
                        default='1024x1024',
                        help='Image size')
    parser.add_argument('-q',
                        '--quality',
                        type=str,
                        default='standard',
                        help='Image quality')
    parser.add_argument('-o',
                        '--output_dir',
                        type=str,
                        default='output/',
                        help='Directory to output images')

    args = parser.parse_args()

    gen_img(args.prompt, args.model, args.size, args.quality, args.output_dir)
