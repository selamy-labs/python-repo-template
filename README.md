# example-pkg

<!-- TODO: replace this line with a crisp one-sentence "what + why". -->

[![Test](https://github.com/selamy-labs/example-pkg/actions/workflows/test.yml/badge.svg)](https://github.com/selamy-labs/example-pkg/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

> Selamy Labs Python repository template. Create a repo from this template,
> then rename `example_pkg` everywhere and replace the placeholder logic. It
> starts at the OSS-excellence bar by construction: LICENSE, the shared reusable
> CI (lint + tests + coverage), a `src/` layout, and tests that already pass.

## Use this template

1. Click **Use this template** → create your repo.
2. Rename the package: `src/example_pkg/` → `src/<your_pkg>/`, and update
   `name`, `[tool.hatch.build.targets.wheel] packages`, and
   `[tool.coverage.run] source` in `pyproject.toml`.
3. Replace `core.py` + its tests with your real code, keeping coverage ≥ 90%.
4. Fill in this README (what/why/install/usage) and set the repo description + topics.

## Install

```bash
pip install -e ".[test]"        # local dev
# or, for an MCP/CLI entry point, expose it under [project.scripts]
```

## Usage

```python
from example_pkg import greet

greet("world")  # "Hello, world!"
```

## Develop

```bash
ruff format . && ruff check .
coverage run -m pytest && coverage report --fail-under=90
```

CI runs the same steps via the shared reusable workflow
(`selamy-labs/.github` → `python-ci.yml`), so the repo's check is defined once,
org-wide.

## Standards

This repo meets the [public-repo bar](https://github.com/selamy-labs/.github):
LICENSE, reusable CI with a coverage floor, `src/` layout, and the org-wide
community-health defaults. Keep them.
