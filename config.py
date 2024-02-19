import yaml


class Config:

    OPENAI_KEY = ''

    def __init__(self, config_path=r'env.yaml') -> None:

        # 1. 讀取 yaml 檔
        config_yml = None
        with open(config_path, 'r', encoding='utf-8') as f:
            config_yml = yaml.safe_load(f)

        # 2. 更新資料
        for key, value in config_yml.items():
            setattr(self, key, value)
