import React, { Component } from 'react';
import { Jumbotron } from 'react-bootstrap' 
import { Link, Route, Switch, matchPath } from 'react-router-dom';
import { ModalRoute } from 'react-router-modal';
import Test from './Test';
import PropTypes from 'prop-types';

const getParams = pathname => {
  const matchProfile = matchPath(pathname, {
    path: `/r/:subreddit/:id`,
  });
  return (matchProfile && matchProfile.params) || {};
};

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
		const { subreddit, id, title, match } = this.props;
		const { showModal } = this.state;
		console.log('show ', showModal)
		console.log('subreditlist match ', match)
		console.log('subreddit ', subreddit)
		console.log('id ', id)
				// <Route to={`/r/:subreddit/:id`} component={Test}/>
					// <Link onClick={this.toggleModal.bind(this)} to={`/r/${subreddit}/${subreddit.id}`}>{title}</Link>
		return (
			<div>
				<Jumbotron>
					<h5>{subreddit}</h5>
					<Link to={`/r/${subreddit}/${id}`}>{title}</Link>
				</Jumbotron>
			</div>
		)
	}
}