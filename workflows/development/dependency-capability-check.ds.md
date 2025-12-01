---
{
  "schema_version": "1.0.0",
  "title": "Dependency Capability Check",
  "version": "1.0.0",
  "status": "stable",
  "objective": "Check if a project's dependencies support a specific feature or version requirement",
  "category": ["development", "analysis"],
  "tags": ["dependencies", "compatibility", "versions", "features"],
  "estimated_duration": {
    "min_minutes": 2,
    "max_minutes": 5
  },
  "inputs": {
    "required": [
      {
        "name": "capability",
        "description": "The feature or capability to check",
        "type": "string",
        "example": "Does our version of React support hooks?"
      }
    ],
    "optional": [
      {
        "name": "package",
        "description": "Specific package to check",
        "type": "string",
        "example": "react"
      }
    ]
  },
  "outputs": {
    "format": "markdown",
    "sections": ["Answer", "Current Version", "Required Version", "Upgrade Path"]
  },
  "validation": {
    "success_criteria": [
      "Current dependency version identified",
      "Feature availability determined with evidence",
      "Clear yes/no answer with upgrade path if needed"
    ]
  }
}
---
# Dependency Capability Check

Check if the project's installed dependencies support a specific feature.

## Your Task

Determine if: **{capability}**

### 1. Identify Current Versions

Check the project's dependency files:
- `package.json` / `package-lock.json` (Node.js)
- `requirements.txt` / `pyproject.toml` (Python)
- `go.mod` (Go)
- `Cargo.toml` (Rust)
- `Gemfile` / `Gemfile.lock` (Ruby)

Find the installed version of the relevant package.

### 2. Research Feature Availability

Check when the feature was introduced:
- Package changelog or release notes
- GitHub releases page
- Documentation version history
- Migration guides

### 3. Compare Versions

Determine if current version >= required version for the feature.

### 4. Check for Breaking Changes

If upgrade is needed:
- Are there breaking changes between current and required version?
- What migration steps are needed?
- Are there peer dependency conflicts?

## Output Format

### Answer
**[YES/NO]**: {capability}

### Current State

| Package | Current Version | Required Version | Status |
|---------|-----------------|------------------|--------|
| {name} | {current} | {required} | ✅ Supported / ❌ Upgrade needed |

### Evidence

**Feature introduced in**: v{version} ({date if known})

**Source**: {link to changelog, docs, or release notes}

**Current usage in codebase** (if any):
- `path/to/file.ts:45` - {how it's currently used}

### Upgrade Path (if needed)

**From** {current} **to** {required}:

1. **Breaking changes to address**:
   - {change 1}
   - {change 2}

2. **Peer dependency updates**:
   - {peer} needs to be updated to {version}

3. **Migration steps**:
   ```bash
   npm install {package}@{version}
   ```

4. **Code changes required**:
   - {file}: {what to change}

### Alternatives (if upgrade not feasible)

- {Alternative approach that works with current version}
- {Polyfill or shim option}

## Notes

- Always check lock files for actual installed versions, not just ranges
- Consider transitive dependencies that might conflict
- Check if the feature requires additional peer dependencies
- Look for canary/beta versions if feature is very new
