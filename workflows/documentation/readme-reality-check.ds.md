---
{
  "schema_version": "1.0.0",
  "title": "README Reality Check",
  "version": "1.0.0",
  "status": "stable",
  "objective": "Compare what the README promises versus what's actually implemented in the codebase",
  "category": ["documentation", "analysis"],
  "tags": ["readme", "documentation", "audit"],
  "estimated_duration": {
    "min_minutes": 1,
    "max_minutes": 5
  },
  "inputs": {
    "optional": [
      {
        "name": "project_path",
        "description": "Path to the project root",
        "type": "string",
        "default": "."
      }
    ]
  },
  "validation": {
    "success_criteria": [
      "All README claims have been verified against code",
      "Output includes specific file:line references"
    ]
  }
}
---
# README Reality Check

Analyze the gap between documentation promises and actual implementation.

## Steps

1. **Read the README**
   - Extract all claimed features, capabilities, and instructions
   - Note any setup steps, CLI commands, API examples
   - Identify version numbers and compatibility claims

2. **Verify Against Code**
   - Check if claimed features actually exist
   - Verify CLI commands/flags work as documented
   - Validate example code actually runs
   - Check if setup instructions are complete and accurate

3. **Find Hidden Gems**
   - Identify features that exist in code but aren't documented
   - Look for useful utilities, flags, or capabilities not mentioned

4. **Assess Impact**
   - Which gaps are critical (block new users)?
   - Which are minor (cosmetic inconsistencies)?
   - Which undocumented features should be highlighted?

## Output Format

### Executive Summary
[One paragraph: overall state of README accuracy, biggest gaps]

### Promises Kept
- Feature X works as documented (verified in `file.ts:123`)
- Setup step Y is accurate

### Promises Broken
- **Claim**: [quote from README]
- **Reality**: [evidence from code with file:line]
- **Impact**: [who this affects]

### Undocumented Features
- Feature X exists but not mentioned (see `feature.ts:200`)
  - What it does: [brief description]

### Recommendations
1. [Most critical fix needed]
2. [Second priority]
3. [Nice-to-have]

## Notes

- Be specific with file paths and line numbers
- Quote exact text from README when showing discrepancies
- Focus on impact to users, not minor wording issues
