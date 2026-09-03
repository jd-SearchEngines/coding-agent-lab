from coding_agent.permission import CommandPolicy


def test_policy_is_fail_closed_for_known_escape_commands() -> None:
    policy = CommandPolicy()
    assert policy.check("cat /etc/passwd").allowed is False
    assert policy.check("rm -rf /tmp/important").allowed is False
    assert policy.check("python3 -m pytest -q").allowed is True

