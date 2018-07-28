import React, { Component } from 'react';
import axios from 'axios';
import SubredditList from './SubredditList';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';

export default class Subreddit extends Component {
	constructor(props) {
		super(props);
		this.state = {
			subreddits: []
		}
	}

	componentDidMount() {
		axios.get('/api/content_list').then(res => {
			this.setState({ subreddits: res.data })
		}).catch(err => {
			console.log('err in getting list', err)
		})
	}

	render() {
		const { subreddits } = this.state;
		const { match } = this.props;
		console.log('match in subreddit ', match)
		return (
			<div>
				{subreddits.map(subreddit => (
					<SubredditList match={match} key={subreddit.id} id={subreddit.id} title={subreddit.title} subreddit={subreddit.subreddit.name}/>))}
			</div>
		)
	}
}