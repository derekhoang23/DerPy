import React, { Component } from 'react';


export default class Test extends Component {
	render() {
		const { subreddit, id } = this.props.match.params;

		console.log('subreddit', subreddit)
		console.log('id ', id)
		const style = {height: '1000px', width: '1000px'}
		return (
			<div >
				fuck yea
			</div>
		)
	}
}