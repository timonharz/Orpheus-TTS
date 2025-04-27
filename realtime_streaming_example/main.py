from flask import Flask, Response, request
import struct
from orpheus_tts import OrpheusModel
<<<<<<< HEAD
=======
import os
>>>>>>> 46b08f7 (feat(docker): add Docker deployment support)

app = Flask(__name__)
engine = OrpheusModel(model_name="canopylabs/orpheus-tts-0.1-finetune-prod")

def create_wav_header(sample_rate=24000, bits_per_sample=16, channels=1):
    byte_rate = sample_rate * channels * bits_per_sample // 8
    block_align = channels * bits_per_sample // 8

    data_size = 0

    header = struct.pack(
        '<4sI4s4sIHHIIHH4sI',
        b'RIFF',
        36 + data_size,       
        b'WAVE',
        b'fmt ',
        16,                  
        1,             
        channels,
        sample_rate,
        byte_rate,
        block_align,
        bits_per_sample,
        b'data',
        data_size
    )
    return header

@app.route('/tts', methods=['GET'])
def tts():
    prompt = request.args.get('prompt', 'Hey there, looks like you forgot to provide a prompt!')
<<<<<<< HEAD
=======
    voice = request.args.get('voice', 'tara')
>>>>>>> 46b08f7 (feat(docker): add Docker deployment support)

    def generate_audio_stream():
        yield create_wav_header()

        syn_tokens = engine.generate_speech(
            prompt=prompt,
<<<<<<< HEAD
            voice="tara",
=======
            voice=voice,
>>>>>>> 46b08f7 (feat(docker): add Docker deployment support)
            repetition_penalty=1.1,
            stop_token_ids=[128258],
            max_tokens=2000,
            temperature=0.4,
            top_p=0.9
        )
        for chunk in syn_tokens:
            yield chunk

    return Response(generate_audio_stream(), mimetype='audio/wav')

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=8080, threaded=True)
=======
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port, threaded=True)
>>>>>>> 46b08f7 (feat(docker): add Docker deployment support)
