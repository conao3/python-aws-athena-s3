# python-aws-athena-s3

An AWS Athena Federated Query connector for S3 data sources, implemented as an AWS Lambda function in Python.

## Overview

This project provides a custom data source connector for Amazon Athena, enabling federated queries against S3-based datasets. It implements the Athena Query Federation SDK protocol and supports the standard connector request types.

### Supported Operations

- **PingRequest** - Health check and connectivity verification
- **ListSchemasRequest** - Enumerate available schemas/databases
- **ListTablesRequest** - List tables within a schema
- **GetTableRequest** - Retrieve table metadata and schema definitions
- **GetTableLayoutRequest** - Get table partitioning information

## Requirements

- Python 3.11 or later
- Poetry for dependency management
- AWS credentials with appropriate permissions

## Installation

```bash
# Clone the repository
git clone https://github.com/conao3/python-aws-athena-s3.git
cd python-aws-athena-s3

# Install dependencies
poetry install
```

## Deployment

Deploy to AWS using the provided deployment script:

```bash
./deploy/sh/090_application --env dev --prefix athena-s3 --profile <your-aws-profile>
```

## Project Structure

```
python-aws-athena-s3/
├── app/
│   └── function/
│       └── m1/
│           └── src/
│               ├── main/        # Lambda handler entry point
│               ├── method/      # Request type handlers
│               └── subr/        # Utility functions
├── deploy/
│   ├── cfn/                     # CloudFormation templates
│   └── sh/                      # Deployment scripts
└── pyproject.toml
```

## Dependencies

- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK for Python
- [PyArrow](https://arrow.apache.org/docs/python/) - Apache Arrow for columnar data
- [AWS Lambda Powertools](https://docs.powertools.aws.dev/lambda/python/latest/) - Utilities for Lambda functions
- [Pydantic](https://docs.pydantic.dev/) - Data validation and settings management

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

## Author

Naoya Yamashita ([@conao3](https://github.com/conao3))
