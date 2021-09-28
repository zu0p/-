import torch
import gluonnlp as nlp


def emotion_ext():
    print("gdgd")
    emotion_model = torch.load('../../model/3emotions_model.pt')
    emotion_model.load_state_dict(torch.load(
        '../../model/3emotions_model_state_dict.pt'))

    checkpoint = torch.load('3emotions_all.tar')
    emotion_model.load_state_dict(checkpoint['model'])
    optimizer.load_state_dict(checkpoint['optimizer'])
    tokenizer = get_tokenizer()
    tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)


def main():
    print("gd")
    emotion_ext()


if __name__ == ' __main__':
    main()
