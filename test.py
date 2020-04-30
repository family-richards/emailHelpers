def test_import():
  from emailHelpers import Mailer, Email
  assert "Mailer" in globals()
  assert "Email" in globals()
