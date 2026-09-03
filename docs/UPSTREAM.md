# Upstream lineage

This lab uses the minimal coding-agent shape popularized by
[SWE-agent/mini-SWE-agent](https://github.com/SWE-agent/mini-swe-agent). The
upstream source was inspected at commit `04d809ceab9df28f9adaed044884180159172930`
on 2026-09-04. The upstream project is MIT licensed; its notice is reproduced
in `licenses/mini-swe-agent-LICENSE.md`.

The lab does not copy upstream implementation files into `src/`. The local
agent is a newly written teaching implementation that keeps the same useful
minimal loop (a model emits shell actions, an environment executes them, and
observations are appended to a linear history). Later commits add explicit
exploration, patching, verification, permission, recovery, and evaluation
layers so each capability can be examined independently.

