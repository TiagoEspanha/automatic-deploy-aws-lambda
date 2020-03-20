-include .env
export

deploy:
	serverless config credentials -o --provider aws --key {AWS_ACCESS_KEY_ID} --secret {AWS_SECRET_ACCESS_KEY}
	serverless deploy
