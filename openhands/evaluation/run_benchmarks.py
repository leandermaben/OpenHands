from openhands.core.config import Config
from openhands.evaluation.benchmarks.mlgym.mlgym_benchmark import MLGymBenchmark
from openhands.evaluation.benchmarks.mlgym.mlgym_config import MLGymConfig

def run_benchmarks(config: Config):
    # Set up MLGym configuration
    mlgym_config = MLGymConfig()
    mlgym_config.tasks = ["task1", "task2", "task3"]
    config.mlgym = mlgym_config

    # Initialize and run MLGym benchmark
    mlgym_benchmark = MLGymBenchmark(config)
    result = mlgym_benchmark.run()

    print(f"MLGym Benchmark Result:")
    print(f"Score: {result.score}")
    print(f"Metadata: {result.metadata}")

if __name__ == "__main__":
    config = Config()
    run_benchmarks(config)
EOF > OpenHands/evaluation/run_benchmarks.py
from openhands.core.config import Config
from openhands.evaluation.benchmarks.mlgym.mlgym_benchmark import MLGymBenchmark
from openhands.evaluation.benchmarks.mlgym.mlgym_config import MLGymConfig

def run_benchmarks(config: Config):
    # Set up MLGym configuration
    mlgym_config = MLGymConfig()
    mlgym_config.tasks = ["task1", "task2", "task3"]
    config.mlgym = mlgym_config

    # Initialize and run MLGym benchmark
    mlgym_benchmark = MLGymBenchmark(config)
    result = mlgym_benchmark.run()

    print(f"MLGym Benchmark Result:")
    print(f"Score: {result.score}")
    print(f"Metadata: {result.metadata}")

if __name__ == "__main__":
    config = Config()
    run_benchmarks(config)
