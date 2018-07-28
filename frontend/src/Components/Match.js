import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { ModalRoute } from 'react-router-modal';
import Test from './Test';
// const Example = ({ match }) => {
// 	return (
// 		<div>
// 			<div>
// 				<ul>
// 					<Link to={`${match.url}/users/42`}>User 42</Link>
// 				</ul>
// 			</div>
// 		<ModalRoute path={`${match.url}/users/:userid`} parentPath={match.url} component={Test} />
// 		</div>
// 	)
// }

// export default Example

export default class Example extends Component {

	render() {
		const { match } = this.props
		console.log(' match ', match)
		return (
			<div>
				<div>
					<ul>
						<Link to={`${match.url}/users/42`}>User 42</Link>
					</ul>
				</div>
				<ModalRoute path={`${match.url}/users/:userid`} parentPath={match.url} component={Test} />
			</div>
		)
	}
}