# ghcr-test-project

Minimal project to test pushing a container image to GitHub Container Registry (GHCR).

## What it does

- `app.py` — tiny script that prints a hello message and the current time
- `Dockerfile` — packages `app.py` into a container image
- `.github/workflows/build-push.yml` — GitHub Actions workflow that builds the image!
  and pushes it to `ghcr.io/<owner>/<repo>` on every push to `main`

## How to use

1. Push this repo to GitHub.
2. Go to the **Actions** tab and confirm the workflow runs (or trigger it manually
   via "Run workflow").
3. Once it succeeds, check the **Packages** section in the repo sidebar (or
   `github.com/<your-username>?tab=packages`) — you should see the image listed.
4. Pull it to confirm:

   ```bash
   docker pull ghcr.io/<owner>/<repo>:latest
   docker run ghcr.io/<owner>/<repo>:latest
   ```

## Notes

- No extra secrets needed — `secrets.GITHUB_TOKEN` is auto-provided by GitHub Actions
  and has push rights to GHCR by default.
- By default, a package pushed this way inherits the visibility of the linked repo's
  settings on first publish, but GHCR packages can also be set public/private
  independently afterward under Package settings.
