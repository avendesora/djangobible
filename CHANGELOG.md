# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### [0.2.1] - 2024-05-24

- Added support for Django 5.0
- Added full support for Python 3.12
  - Added automated functional testing now that there is a version of greenlet that supports Python 3.12
- ~~Added automated testing for Python 3.13-beta~~ (not yet supported by greenlet)
- Added automated testing for Django 5.1-alpha

### Changed

- Require the latest version of pythonbible (0.13.1)

### Removed

- Removed official support for Django 3.2 (due to end of life on 2024-04-01)
- Removed official support for Django 4.1 (due to end of life on 2023-12-01)

## [0.2.0] - 2023-10-04

### Added

- Added support for Python 3.12
- Added automated testing for Python 3.8 - 3.12; Django 3.2, 4.1, 4.2; and Ubuntu, macOS, and Windows

### Changed

- Require the latest version of pythonbible (0.12.0)

### Removed

- Removed official support for Django 4.0 (due to end of life on 2023-04-01)

## [0.1.1] - 2023-10-02

### Changed

- Require the latest version of pythonbible (0.11.1)

## 0.1.0 - 2023-07-03

### Added

- Added this changelog

### Removed

- Removed Python 3.7 support (due to end of life on 2023-06-27)

[unreleased]: https://github.com/avendesora/djangobible/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/avendesora/djangobible/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/avendesora/djangobible/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/avendesora/djangobible/releases/tag/v0.1.1
