# Incident Log

## Build #2 - Failed (08:09 UTC / 1:39 PM IST)
- Stage: Install and Test
- Failing test: test_main.py::test_health (line 10)
- Error: AssertionError - the app returned {'status': 'ok'} but the test expected {'status': 'bad'}
- Test summary: 1 failed, 1 passed
- Cause: I changed the expected value in the test to "bad" on purpose to trigger a failure
- Effect: the pipeline stopped at the test stage, so the Build Image and Deploy stages did not run and the previous version stayed live
- Fix: changed the expected value back to "ok" in test_main.py and pushed
- Result: Build #3 passed (08:13 UTC) and the app was redeployed