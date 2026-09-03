# Failure taxonomy from Season 1 runs

The categories below are assigned from persisted raw run fields, not invented
from a desired narrative.

| Category | Evidence rule | Observed evidence |
| --- | --- | --- |
| Verify Failure | self-report true and external test false | 5 cases in `eval_minimal.jsonl` and `eval_explore.jsonl` |
| Context Failure | no targeted exploration action | minimal version, 5 cases |
| Wrong Patch | first patch's test fails before replan | verify/managed versions, 5 cases each |
| Tool Failure | non-zero tool action | verify: 5; managed: 10 |
| Permission Boundary | policy-denied action | managed: 5 |
| Recovery Success | failure action followed by final external pass | verify/managed: 5 cases each |
| Timeout | return code 124 | 0 in this bounded dataset |
| Recovery Failure | final external test fails after failure | 0 in final managed run |

The baseline and explore failures are not proof that context was the only
cause; they are evidence that neither version edited and verified the fixture.

