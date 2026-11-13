"""Command-line demo with honest, synthetic-only reporting."""
import argparse
import json
from pathlib import Path
from .core import UpdateRule
from .evolution import evolve
from .simulator import aggregate, study


def main():
    parser = argparse.ArgumentParser(description="EvoTeach-RSI synthetic research demo")
    parser.add_argument("--seed", type=int, default=2027)
    parser.add_argument("--generations", type=int, default=3)
    parser.add_argument("--output", type=str)
    args = parser.parse_args()

    baseline = UpdateRule()
    evolved, meta, log = evolve(baseline, generations=args.generations, seed=args.seed)
    test_ids = range(90000, 90300)  # excluded from proposal selection
    static = aggregate(study(test_ids, args.seed + 2000, baseline, "static"))
    adaptive = aggregate(study(test_ids, args.seed + 2000, baseline, "adaptive"))
    revised = aggregate(study(test_ids, args.seed + 2000, evolved, "adaptive"))
    payload = {
        "disclaimer": "ALL RESULTS ARE SYNTHETIC. Not evidence of learning impact on actual students.",
        "data_split": {
            "validation": "separate synthetic IDs per generation",
            "final_test": "90000..90299",
        },
        "fixed_schedule": static,
        "fixed_adaptive_rule": adaptive,
        "evolved_update_rule": revised,
        "final_rule": vars(evolved),
        "final_meta_rule": vars(meta),
        "evolution_log": log,
    }
    result = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(result, encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
