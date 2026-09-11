# Review Policy

- All data PRs require: CI `validate.py --all` passes + 1 reviewer approval (reviewer ≠ author)
- Sensitive/political/defamation risk → 2 reviewers
- Reviewer checks: source exists & supports claim, verbatim_quote present, dates precision correct, role/value not conflated, geo precision honest, duplicate check, license ok
- Automated checks: required fields, ISO codes, EDTF, date order, coords in Africa bbox, value without currency, missing source link, enum validity
- Rejection: explain in review, keep `unverified` if needed, schedule re-check
- No auto-publish from automation - human gate always
