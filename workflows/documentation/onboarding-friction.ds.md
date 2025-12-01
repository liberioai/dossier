---
{
  "schema_version": "1.0.0",
  "title": "Onboarding Friction Assessment",
  "version": "1.0.0",
  "status": "stable",
  "objective": "Identify pain points and confusion for new contributors trying to understand and work with the project",
  "category": ["documentation", "development"],
  "tags": ["onboarding", "contributor-experience", "analysis"],
  "estimated_duration": {
    "min_minutes": 2,
    "max_minutes": 5
  },
  "inputs": {
    "optional": [
      {
        "name": "focus_area",
        "description": "Specific area to focus on (setup, testing, architecture, or all)",
        "type": "string",
        "default": "all"
      }
    ]
  },
  "outputs": {
    "format": "markdown",
    "sections": ["Friction Score", "Critical Blockers", "Confusion Points", "Missing Guidance", "Quick Wins"]
  },
  "validation": {
    "success_criteria": [
      "All five journey stages were evaluated",
      "Specific file:line references provided for issues",
      "Actionable recommendations included"
    ]
  }
}
---
# Onboarding Friction Assessment

Evaluate the new contributor experience by simulating a newcomer's journey through the project.

## Your Task

Simulate the journey of a new contributor who wants to:
1. Understand what this project does
2. Set up a development environment
3. Understand the codebase structure
4. Make their first contribution
5. Run tests and verify their changes

For each stage, identify friction points.

## Areas to Investigate

### 1. First Impression (0-2 minutes)
- Is the project purpose clear immediately?
- Is the README welcoming and oriented to newcomers?
- Are there quick examples to understand value?

### 2. Setup Process (2-10 minutes)
- Are dependencies clearly listed?
- Do setup commands actually work?
- Are there multiple conflicting instruction sources?
- Are there hidden system requirements?

### 3. Codebase Navigation (10-30 minutes)
- Is the directory structure intuitive?
- Is there a CONTRIBUTING.md or architecture guide?
- Are naming conventions consistent and clear?
- Can you find where to add a simple feature?

### 4. Development Workflow (30+ minutes)
- How to run tests? Is it documented and does it work?
- Hot reload / fast feedback loops?
- How to debug? Any tooling explained?
- Code style enforcement (linters)? Automatic or manual?

### 5. Contribution Process
- How to submit changes? PR template? Guidelines?
- Are there examples of good PRs to learn from?
- Review process transparent?

## Output Format

### Friction Score
**Overall: [Low/Medium/High]**
- Setup: [score]
- Understanding: [score]
- Contributing: [score]

[One paragraph summary of overall experience]

### Critical Blockers 🚫
[Things that STOP a new contributor]

1. **[Blocker name]**
   - What happens: [specific scenario]
   - Evidence: [file:line or missing file]
   - Impact: [why this is critical]
   - Fix: [specific recommendation]

### Confusion Points 🤔
[Things that SLOW DOWN or CONFUSE contributors]

1. **[Confusion source]**
   - Why it's confusing: [explanation]
   - Where it happens: [context/files]
   - Better approach: [suggestion]

### Missing Guidance 📚
[Documentation gaps that would help newcomers]

- [ ] Missing X explanation (needed in file/doc Y)
- [ ] No examples of Z (would help with understanding W)

### Quick Wins 🎯
[Small changes with high impact on contributor experience]

1. **[Quick win]** - [why it helps] - [where to add it]
   - Effort: [Low/Medium]
   - Impact: [High/Medium]

## Notes

- Think from a beginner's perspective—don't assume expert knowledge
- Be specific about WHERE confusion happens (file paths, doc sections)
- Prioritize based on impact to newcomer success
- Quick wins should be actionable ("add setup example to README:45" not "improve docs")
- If onboarding is smooth, celebrate what works well
