---
{
  "schema_version": "1.0.0",
  "title": "Test Coverage Gap Analysis",
  "version": "1.0.0",
  "status": "stable",
  "objective": "Analyze test files against project structure to identify untested code paths, functions, and modules",
  "category": ["development", "testing"],
  "tags": ["testing", "coverage", "gap-analysis", "quality"],
  "estimated_duration": {
    "min_minutes": 5,
    "max_minutes": 15
  },
  "inputs": {
    "optional": [
      {
        "name": "test_directory",
        "description": "Where test files are located",
        "type": "string",
        "default": "tests/ or __tests__/ or src/**/*.test.*"
      },
      {
        "name": "focus",
        "description": "What to focus on (all, unit, integration, e2e)",
        "type": "string",
        "default": "all"
      }
    ]
  },
  "outputs": {
    "format": "markdown",
    "sections": ["Coverage Summary", "Untested Code", "Test Quality Issues", "Recommendations"]
  },
  "validation": {
    "success_criteria": [
      "Test framework identified",
      "All test files discovered",
      "Gaps mapped to specific files and functions",
      "Prioritized recommendations provided"
    ]
  }
}
---
# Test Coverage Gap Analysis

Analyze test files against project structure to identify what's tested and what's not.

## Your Task

1. Identify the test framework and test file locations
2. Map what code exists vs. what tests exist
3. Find gaps where code has no corresponding tests
4. Identify test quality issues (skipped tests, .only, etc.)

## Phase 1: Discover Test Setup

### Identify Test Framework

Check for common test frameworks:

**JavaScript/TypeScript:**
- Jest: `jest` in package.json, `jest.config.*`
- Vitest: `vitest` in package.json, `vitest.config.*`
- Mocha: `mocha` in package.json, `.mocharc.*`

**Python:**
- pytest: `pytest` in requirements, `pytest.ini`, `pyproject.toml [tool.pytest]`
- unittest: `test_*.py` files with `unittest` imports

**Go:**
- Built-in: `*_test.go` files

**Rust:**
- Built-in: `#[test]` attributes, `tests/` directory

### Find Test Files

Common patterns:
- `tests/`, `test/`, `__tests__/`
- `*.test.ts`, `*.spec.ts`, `*.test.js`, `*.spec.js`
- `test_*.py`, `*_test.py`
- `*_test.go`

## Phase 2: Map Project Structure

Identify testable code:

### For API/Backend Projects
- Routes/endpoints
- Controllers/handlers
- Services/business logic
- Models/data access
- Middleware
- Utilities

### For Frontend Projects
- Components
- Hooks
- State management
- API clients
- Utilities

### For Libraries
- Public API functions
- Internal utilities
- Edge cases and error handling

## Phase 3: Cross-Reference

For each piece of testable code, determine:

1. **Covered** - Has dedicated tests that exercise it
2. **Partially Covered** - Some tests exist but don't cover all paths
3. **Not Covered** - No tests reference this code

## Phase 4: Identify Quality Issues

Look for:
- **Skipped tests** (`.skip`, `xit`, `xdescribe`, `@pytest.mark.skip`)
- **Exclusive tests** (`.only`, `fit`, `fdescribe`) - blocks other tests
- **Empty tests** - test blocks with no assertions
- **TODO/FIXME** comments in test files

## Output Format

### Coverage Summary

| Category | Total | Tested | Coverage |
|----------|-------|--------|----------|
| Routes/Endpoints | {n} | {n} | {%} |
| Functions/Methods | {n} | {n} | {%} |
| Components | {n} | {n} | {%} |

**Overall Structural Coverage**: {percentage}%

### Untested Code

#### Critical (Public APIs, Core Logic)

| File | Function/Component | Why Critical |
|------|-------------------|--------------|
| `src/api/users.ts:45` | `deleteUser()` | Destructive operation |
| `src/auth/login.ts:20` | `authenticate()` | Security-critical |

#### High Priority (Business Logic)

| File | Function/Component | Notes |
|------|-------------------|-------|
| `src/services/billing.ts:100` | `calculateTotal()` | Complex calculation |

#### Lower Priority (Utilities, Internal)

| File | Function/Component | Notes |
|------|-------------------|-------|
| `src/utils/format.ts:15` | `formatDate()` | Simple utility |

### Test Quality Issues

#### Skipped Tests ({count})
| File | Line | Test Name | Reason (if stated) |
|------|------|-----------|-------------------|
| `tests/auth.test.ts` | 45 | "should handle expired tokens" | TODO comment |

#### Exclusive Tests ({count})
⚠️ These have `.only` and block other tests from running:
| File | Line | Test Name |
|------|------|-----------|
| `tests/api.test.ts` | 23 | "debug test" |

#### Empty/Incomplete Tests ({count})
| File | Line | Issue |
|------|------|-------|
| `tests/utils.test.ts` | 67 | No assertions |

### Recommendations

**Immediate (before next release):**
1. Add tests for `deleteUser()` - destructive operation without coverage
2. Remove `.only` from `tests/api.test.ts:23`
3. Fix or remove 3 skipped tests

**Short-term:**
1. Add integration tests for authentication flow
2. Increase coverage of billing calculations

**Process improvements:**
1. Add coverage threshold to CI (suggest: 70%)
2. Block PRs that add `.only` or `.skip`

## Notes

- This is structural analysis, not line-level coverage
- For precise line coverage, use native tools (`jest --coverage`, `pytest-cov`)
- Focus on critical paths first: auth, payments, data mutations
- Some code legitimately doesn't need tests (simple pass-through, generated code)
