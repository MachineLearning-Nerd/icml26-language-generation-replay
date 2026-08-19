#!/usr/bin/env python3
"""Verify the committed publication contract for this repository."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_STATUS = (
    "ALL_SIX_CLAIMS_VERIFIED_SCOPED_LEAN_AND_EXACT_AUDITS_HISTORICAL_SCORE_6_OF_12_NO_CURRENT_SCORE"
)
EXPECTED_BRANCHES = 12
EXPECTED_COMMITS = 30
CANONICAL_IDENTITY = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
CLAIM_IDS = ["C1", "C2", "C3", "C4", "C5", "C6"]


def load(name: str):
    return json.loads((ROOT / name).read_text())


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"verification failed: {message}")


def published_branches() -> list[str]:
    remote = git("for-each-ref", "refs/remotes/origin", "--format=%(refname:short)").splitlines()
    remote = [
        name.removeprefix("origin/")
        for name in remote
        if name.startswith("origin/") and name != "origin/HEAD"
    ]
    if remote:
        return remote
    return git("for-each-ref", "refs/heads", "--format=%(refname:short)").splitlines()


def main() -> None:
    claims = load("claims.json")
    verdicts = load("reproduction_verdicts.json")
    manifest = load("EVIDENCE_MANIFEST.json")
    state = load("AUTONOMOUS_STATE.json")
    certificate = load(".openresearch/artifacts/formal/lean_certificate.json")
    gate = load("outputs/publication_gate.json")

    require(claims["overall_status"] == EXPECTED_STATUS, "claims overall status")
    require(state["overall_status"] == EXPECTED_STATUS, "autonomous state overall status")
    require(verdicts["overall_verdict"] == "PASS_SIX_CLAIM_RELEASE_GATE", "overall verdict")
    require([claim["id"] for claim in claims["claims"]] == CLAIM_IDS, "claim ordering")
    require(
        all(claim["status"] == "VERIFIED_SCOPED" for claim in claims["claims"]),
        "claim statuses",
    )
    require(verdicts["claim_statuses"] == {claim_id: "VERIFIED_SCOPED" for claim_id in CLAIM_IDS}, "verdict statuses")

    required_paths = manifest["required_paths"]
    require(all((ROOT / path).exists() for path in required_paths), "manifest paths")
    require(manifest["controls"]["lean_reusable_core"], "Lean reusable core")
    require(manifest["controls"]["independent_checkers"], "independent checkers")
    require(manifest["controls"]["negative_control_per_claim"], "negative controls")
    require(manifest["controls"]["premise_changing_mutations_rejected"] == 2, "mutation count")

    formal = verdicts["formal_core"]
    require(formal["lean_version"] == "4.32.0", "Lean version")
    require(formal["theorem_statements_checked"] == 27, "theorem count")
    require(formal["premise_changing_mutations_rejected"] == 2, "formal mutation count")
    require(certificate["main_compile_succeeded"], "Lean certificate compilation")
    require(certificate["certificate_sha256"] == formal["certificate_sha256"], "certificate hash")
    require(len(certificate["theorems"]) == 27, "certificate theorem list")
    require(all(item["compile_failed_as_required"] for item in certificate["negative_controls"].values()), "Lean negative controls")

    external = verdicts["external_results"]
    require(external["historical_live_score"] == "6/12", "historical score")
    require(external["current_score_claim"] is False, "current score claim")
    require(external["candidate_publication_gate_passed"] is True, "candidate gate")
    require(verdicts["publication"]["publication_allowed"] is False, "publication state")
    require(verdicts["publication"]["author_endorsement_claimed"] is False, "author endorsement state")
    require(gate["publication_gate_passed"] is True and gate["claim_count"] == 6, "local publication gate")

    branches = published_branches()
    require(len(branches) == EXPECTED_BRANCHES, "branch count")
    require("main" in branches, "main branch")
    require(not any(branch.startswith("orx/") for branch in branches), "legacy orx branch")
    require(int(git("rev-list", "--all", "--count")) == EXPECTED_COMMITS, "reachable commit count")
    identities = git("log", "--all", "--format=%an <%ae>\n%cn <%ce>").splitlines()
    require(identities and all(identity == CANONICAL_IDENTITY for identity in identities), "canonical commit identity")

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(branches)} commits={EXPECTED_COMMITS} "
        "claims=C1:C6_verified_scoped "
        "formal=lean4.32.0_theorem_statements=27_mutations_rejected=2 "
        "historical_score=6/12 current_score_claim=false "
        "publication_allowed=false"
    )


if __name__ == "__main__":
    main()
