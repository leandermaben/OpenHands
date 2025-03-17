from typing import List, Dict, Any

class MLGymConfig:
    def __init__(self):
        self.tasks: List[str] = []
        self.max_steps: int = 100
        self.timeout: int = 300
        self.docker_image: str = "mlgym/mlgym:latest"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tasks": self.tasks,
            "max_steps": self.max_steps,
            "timeout": self.timeout,
            "docker_image": self.docker_image,
        }

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'MLGymConfig':
        config = cls()
        config.tasks = config_dict.get("tasks", [])
        config.max_steps = config_dict.get("max_steps", 100)
        config.timeout = config_dict.get("timeout", 300)
        config.docker_image = config_dict.get("docker_image", "mlgym/mlgym:latest")
        return config
EOF > OpenHands/evaluation/benchmarks/mlgym/mlgym_config.py
from typing import List, Dict, Any

class MLGymConfig:
    def __init__(self):
        self.tasks: List[str] = []
        self.max_steps: int = 100
        self.timeout: int = 300
        self.docker_image: str = "mlgym/mlgym:latest"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tasks": self.tasks,
            "max_steps": self.max_steps,
            "timeout": self.timeout,
            "docker_image": self.docker_image,
        }

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'MLGymConfig':
        config = cls()
        config.tasks = config_dict.get("tasks", [])
        config.max_steps = config_dict.get("max_steps", 100)
        config.timeout = config_dict.get("timeout", 300)
        config.docker_image = config_dict.get("docker_image", "mlgym/mlgym:latest")
        return config
