from flask_restful import Api, Resource, reqparse



connexion1_post_args = reqparse.RequestParser()
connexion1_post_args.add_argument("param1",type=str,required=True)
connexion1_post_args.add_argument("param2",type=str,required=True)
connexion2_post_args = reqparse.RequestParser()
connexion2_post_args.add_argument("param3",type=int,required=True)
connexion2_post_args.add_argument("param4",type=int,required=True)


class connexion1(Resource):
	def post(self): #s_inscrire
		body = connexion1_post_args.parse_args()
		[param1,param2] = [body[i] for i in body]


		return param1+param2


class connexion2(Resource):
	def post(self): #verifier_son_adresse_mail
		body = connexion2_post_args.parse_args()
		[param3,param4] = [body[i] for i in body]

		return param3+param4


