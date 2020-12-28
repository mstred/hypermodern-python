from nox import session as nox_session


@nox_session()
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", *(session.posargs or ["--cov", "-m", "not e2e"]))

