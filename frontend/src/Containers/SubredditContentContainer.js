import React, { Component } from 'react';
import SubredditContent from '../Components/SubredditContent';
export default class SubredditContainer extends Component {
	render() {
		const { subreddit, subredditId, contentId } = this.props.match.params;
		return (
			<SubredditContent subreddit={subreddit} subredditId={subredditId} contentId={contentId}/>
		)
	}
}

