import os
import json
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

class CLIConfig(BaseModel):
    api_url: str = "http://localhost:8000"
    access_token: Optional[str] = None
    default_project_id: Optional[str] = None

class ConfigManager:
    APP_NAME = "supalove"
    
    def __init__(self):
        self.config_dir = Path.home() / f".{self.APP_NAME}"
        self.config_file = self.config_dir / "config.json"
        self._ensure_config_dir()
        self.config = self._load_config()

    def _ensure_config_dir(self):
        if not self.config_dir.exists():
            self.config_dir.mkdir(parents=True)

    def _load_config(self) -> CLIConfig:
        if not self.config_file.exists():
            return CLIConfig()
        
        try:
            with open(self.config_file, "r") as f:
                data = json.load(f)
                return CLIConfig(**data)
        except Exception:
            return CLIConfig()

    def save_config(self):
        with open(self.config_file, "w") as f:
            f.write(self.config.model_dump_json(indent=2))

    def set_token(self, token: str):
        self.config.access_token = token
        self.save_config()

    def clear_token(self):
        self.config.access_token = None
        self.save_config()
    
    def set_project(self, project_id: str):
        self.config.default_project_id = project_id
        self.save_config()

config_manager = ConfigManager()
