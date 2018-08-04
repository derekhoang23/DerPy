import React, { Component } from 'react';
import { Jumbotron } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { ModalRoute } from 'react-router-modal';
import Test from './Test';
import PropTypes from 'prop-types';


export default class SubredditList extends Component {
	// static propTypes = {
 //    match: PropTypes.object.isRequired,
 //    location: PropTypes.object.isRequired,
 //    history: PropTypes.object.isRequired
 //  }
	constructor(props) {
		super(props);
		this.state = {
			showModal: false,
			loading: false
		}
	}

	toggleModal(e) {
		e.preventDefault();
		const { showModal } = this.state;
		console.log('reverse ', !showModal)
		this.setState({ showModal: !showModal })
	}
	render() {
		const { subreddit, subredditId, title, contentId } = this.props;
		return (
			<div>
				<Jumbotron>
					<h5>{subreddit}</h5>
					<Link to={`/r/${subreddit}/${subredditId}/subreddit_content/${contentId}`}>{title}</Link>
				</Jumbotron>
			</div>
		)
	}
}