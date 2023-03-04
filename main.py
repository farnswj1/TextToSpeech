from gtts import gTTS
from playsound import playsound
from tempfile import NamedTemporaryFile


def read(text: str) -> None:
    with NamedTemporaryFile() as file:
        gTTS(text, lang='en', tld='com.au').write_to_fp(file)
        playsound(file.name)


if __name__ == '__main__':
    text = input('Enter your text:\n')
    read(text)
