import logging
import whisper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    model = whisper.load_model("medium")  # base / medium / large
    
    try:
        response = model.transcribe("/path/to/inside/container/shared_data/audio.mp3")

        with open("/path/to/inside/container/shared_data/transcricao.txt", "w", encoding="utf-8") as file:
            file.write(response["text"])

        logger.info("Transcrição salva em transcricao.txt")

    except Exception as e:
        logger.error("Ocorreu um erro durante a transcrição: %s", e)

if __name__ == "__main__":
    main()
