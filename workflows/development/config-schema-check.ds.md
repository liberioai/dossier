---
{
  "schema_version": "1.0.0",
  "title": "Config Schema Check",
  "version": "1.0.0",
  "status": "stable",
  "objective": "Check if a configuration system supports a specific option or setting",
  "category": ["development", "analysis"],
  "tags": ["config", "schema", "settings", "options"],
  "estimated_duration": {
    "min_minutes": 2,
    "max_minutes": 5
  },
  "inputs": {
    "required": [
      {
        "name": "option",
        "description": "The configuration option to check",
        "type": "string",
        "example": "Does ESLint support the noUnusedLocals rule?"
      }
    ],
    "optional": [
      {
        "name": "tool",
        "description": "Specific tool or system to check",
        "type": "string",
        "example": "eslint"
      }
    ]
  },
  "outputs": {
    "format": "markdown",
    "sections": ["Answer", "Option Details", "Configuration Example", "Related Options"]
  },
  "validation": {
    "success_criteria": [
      "Option existence confirmed with documentation",
      "Valid configuration example provided",
      "Default value and valid values documented"
    ]
  }
}
---
# Config Schema Check

Check if a tool's configuration system supports a specific option or setting.

## Your Task

Determine if: **{option}**

### 1. Check JSON Schema (if available)

Many tools publish their config schema:
- `{tool}.schema.json` in the repo
- JSON Schema Store (schemastore.org)
- TypeScript types for config

Look for the option name, type, and allowed values.

### 2. Check Documentation

Review configuration docs:
- Official configuration reference
- Option listings with descriptions
- Default values documentation

### 3. Check Source Code

If schema isn't definitive:
- Look at config parsing code
- Find where the option is read and used
- Check for validation logic

### 4. Check Examples

Look for usage in:
- Official examples or starter templates
- Popular open source projects
- Documentation examples

## Output Format

### Answer
**[YES/NO]**: {option}

### Option Details

**Tool**: {name} v{version}+

**Option path**: `{path.to.option}`

**Type**: {string | boolean | number | array | object}

**Default value**: `{default}`

**Valid values**:
- `{value1}` - {description}
- `{value2}` - {description}

### Configuration Example

**JSON** (e.g., `.{tool}rc.json`):
```json
{
  "path": {
    "to": {
      "option": "value"
    }
  }
}
```

**YAML** (if supported):
```yaml
path:
  to:
    option: value
```

**JavaScript** (if supported):
```javascript
module.exports = {
  path: {
    to: {
      option: 'value'
    }
  }
};
```

### Documentation Reference

**Official docs**: {link}

**Added in version**: {version if known}

### Related Options

| Option | Description | Relationship |
|--------|-------------|--------------|
| `{related.option}` | {description} | {conflicts with / requires / see also} |

### Common Mistakes

- {Mistake 1}: {correct approach}
- {Mistake 2}: {correct approach}

## Notes

- Config options may be added in specific versions - check tool version
- Some options only work in certain file formats (JSON vs JS)
- CLI flags may override config file options
- Environment variables may provide alternative configuration
