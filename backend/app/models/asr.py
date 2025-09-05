from funasr import AutoModel


class Asr:
    def init(self):
        self.model = AutoModel(
            disable_update=True,
            model="models/funasr/paraformer-zh",
            vad_model="models/funasr/fsmn-vad",
            punc_model="models/funasr/ct-punc",
            spk_model="models/funasr/cam++",
        )

    def generate(self, input):
        return self.model.generate(input=input)
