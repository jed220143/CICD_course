# Contributing Guide

This repository is a learning project for Cloud, Docker, CI/CD, and safe deployment practice.

## Branch Workflow

Use short-lived feature branches from `main`.

```text
main
└── feature/<short-topic>
```

Examples:

- `feature/bootstrap-api`
- `feature/repository-workflow`
- `fix/docker-compose-healthcheck`

## Commit Guidelines

Use small, focused commits with clear messages that explain the learning intent and verify that each commit contains no secrets.

Good examples:

- `docs: record github remote setup evidence`
- `chore: establish repository workflow and contribution rules`
- `feat: add health check endpoint`
- `test: add api health check test`

## Pull Request Checklist

Before opening a pull request:

- Explain the scope of the change.
- Include test evidence or say why tests are not applicable.
- Check that no secrets, tokens, passwords, private keys, or real account IDs are committed.
- Keep cloud resources local-first unless the AWS free-tier gate has passed.

## Safety Rules

- Do not commit `.env`.
- Do not commit private keys such as `.pem` or `.key`.
- Do not commit Terraform state files.
- Do not create paid cloud resources for the core track.
- Do not send real secrets through public HTTP labs.
