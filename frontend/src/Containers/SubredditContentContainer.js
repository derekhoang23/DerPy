import React, { Component } from 'react';
import SubredditContent from '../Components/SubredditContent';
export default class SubredditContainer extends Component {
	render() {
		const { subreddit, id } = this.props.match.params;
		return (
			<SubredditContent subreddit={subreddit} id={id}/>
		)
	}
}

