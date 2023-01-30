0. Parameterize a unit test

Familiarize yourself with the utils.access_nested_map function and understand its purpose. Play with it in the Python console to make sure you understand.


1. Parameterize a unit test

Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand):

2. Mock HTTP calls

Familiarize yourself with the utils.get_json function

3. Parameterize and patch

Read about memoization and familiarize yourself with the utils.memoize decorator.

4. Parameterize and patch as decorators

Familiarize yourself with the client.GithubOrgClient class.

5. Mocking a property

memoize turns methods into properties. Read up on how to mock a property (see resource).

6. More patching

Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.

7. Parameterize

Implement TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.


