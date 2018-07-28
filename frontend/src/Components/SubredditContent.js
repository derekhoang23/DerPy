import React, { Component } from 'react';
import axios from 'axios';
import SubredditList from './SubredditList';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';

export default class SubredditContent extends Component {
	constructor(props) {
		super(props);
		this.state = {
			subreddits: []
		}
	}

	componentDidMount() {
		const { subreddit, id } = this.props;
		axios.get(`/api/subreddit_content/${subreddit}/${id}`).then(res => {
			console.log('data ', res.data)
			// this.setState({ subreddits: res.data })
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
				hello
			</div>
		)
	}
}