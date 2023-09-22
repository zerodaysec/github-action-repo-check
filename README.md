# GitHub Action: Repository Audit

Organizations often struggle with ensuring that their repositories are compliant and standardized. This can lead to
issues such as inconsistent code quality, security vulnerabilities, and failed compliance audits. In addition, different
teams may have different opinions on what constitutes best practices, making it difficult to enforce a consistent standard
across the organization.

The Audit Repository GitHub action can help organizations address this challenge by providing a simple and automated way
to check for the existence of specified files and actions in a repository. By using this action, teams can ensure that
repositories meet a minimum set of requirements and are compliant with organizational standards. This can lead to
improved code quality, reduced security risks, and increased compliance with regulatory requirements.

## Purpose

The `Repository Audit` action can be used to check if a repository contains the expected files and actions before running a workflow. It can help prevent unexpected errors and ensure that the repository is properly set up before continuing with the workflow.

## Default Setup

To use the `Repository Audit` action with default settings, add the following step to your workflow YAML file:

```yaml
- name: Audit Repository
  uses: zerodaysec/repo-audit-action@v1
  with:
    files: README.md,CODEOWNERS
    actions: terraform-lint.yml,help-wanted.yml
```

This will run the `Repository Audit` action with the default `files` and `actions` settings. The action will check if the specified files and actions exist in the repository and output the result to the workflow log.
<!-- 
## Configuration Overrides

You can override the default `files` and `actions` settings by either creating a `.github/repo_audit_config.yml` file in your repository or by passing in command line arguments to the action.

### Using a Configuration File

To use a configuration file, create a `.github/repo_audit_config.yml` file in your repository with the following format:

```yaml
files:
  - README.md
  - CODEOWNERS
  - docs/index.rst
actions:
  - terraform-lint.yml
  - help-wanted.yml
```

This will supplement the default `files` and `actions` settings with the files and actions listed in the configuration file. -->

### Using Command Line Arguments

You can also pass in command line arguments to the action to override the default `files` and `actions` settings:

```yaml
- name: Audit Repository
  uses: zerodaysec/repo-audit-action@v1
  with:
    files: README.md,CODEOWNERS,docs/index.rst
    actions: terraform-lint.yml,help-wanted.yml,action3.yml
```

This will override the default `files` and `actions` settings with the files and actions specified in the `with` section.

## Output

The `Repository Audit` action outputs the result of the audit to the workflow log. It will print a message for each requested file and action, indicating whether or not it exists in the repository:

```
File README.md exists in the repository.
File CODEOWNERS does not exist in the repository.
File docs/index.rst exists in the repository.
Action terraform-lint.yml exists in the repository.
Action help-wanted.yml does not exist in the repository.
```

This output can help you identify which files or actions are missing and take appropriate action to resolve the issue.
