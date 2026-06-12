# Worked example: placement list for a PARA vault

This is the filled-in version of the Step 2 placement list, calibrated to a PARA vault. Copy it into the prompt in Step 2 of `SKILL.md` and edit the folders and descriptions to match your own structure.

> **Where does this study belong?**
> 1. `2_Areas/AI-Augmentation/`: AI, augmentation tools
> 2. `2_Areas/Aerospace/`: Aerospace engineering
> 3. `2_Areas/Training/`: Teaching, courses, learning material
> 4. `4_Resources/Engineering/`: Engineering reference
> 5. `4_Resources/AI-ML/`: AI/ML reference
> 6. `4_Resources/Research/`: General research reference
> 7. `1_Projects/[name]/`: For a specific project
> 8. Other: specify

The matching connection scan for this layout greps the three top-level PARA folders:

```bash
grep -rl "[tag]" 2_Areas/ 4_Resources/ 1_Projects/ --include="*.md" | head -10
```
