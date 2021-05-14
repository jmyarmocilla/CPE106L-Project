CREATE TABLE IF NOT EXISTS tweets_users_join AS
SELECT * from tweets
	inner join users
	on tweets.user=users.id;

CREATE TABLE IF NOT EXISTS tweets_users_normalized AS
SELECT id, user, screen_name, created_at, full_text,
source, text, is_quote_status, quote_count,
reply_count, retweet_count, favorite_count FROM tweets_users_join;