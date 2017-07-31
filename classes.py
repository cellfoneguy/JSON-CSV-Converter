# Alex Bai
# define the classes to hold data

import json

class Session:
	#Holds each Line from the log.

	def __init__(self):
		self.timeStamp = -1
		self.sessionId = -1
		self.type = ""
		self.callsNow = -1
		self.vmrs = []

	def __repr__(self):
		openString = "\nTimestamp: {ts}\nSession: {s}\nType: {t}"\
			"\nCallsNow: {cn}\nVmrs: {v}"
		
		#build a list of string representations of vmrs
		vmrsF = []
		for room in self.vmrs:
			vmrsF.append(room.__repr__())

		return (openString.format(ts=self.timeStamp, s=self.sessionId,
			t=self.type, cn=self.callsNow, v="\n".join(vmrsF)))


class VMR:
	#Holds each vmr.

	def __init__(self):
		self.id = ""
		self.name = ""
		self.Alias = -1
		self.StartTime = ""
		self.Presenting = False
		self.Participants = []

	def __repr__(self):
		openString = "\n  VID: {id}\n  Name: {n}\n  Alias: {a}\n  StartTime: {st}"\
			"\n  Presenting: {p}\n  Participants: {pa}"
		return (openString.format(id=self.id, n=self.name, a=self.Alias,
			st=self.StartTime, p=self.Presenting, pa=self.Participants))


class Participant:
	#Holds each participant.

	def __init__(self):
		self.id = ""
		self.name = ""
		self.RemoteAddress = ""
		self.Protocol = ""
		self.StartTime = ""
		self.Encryption = ""
		self.CallType = ""
		self.Presentation = ""
		self.TxAudio = {}
		self.RxAudio = {}
		self.TxVideo = {}
		self.RxVideo = {}
		self.TxPresentation = {}
		self.RxPresentation = {}

	def __repr__(self):
		#too lazy to build a formatted string with all that stuff in it
		return "\n    PID: {id}".format(id=self.id)