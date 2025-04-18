import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

def capturar_gestos(gestos):
    dados, rotulos = [], []
    cap = cv2.VideoCapture(0)
    for numero_gesto, nome_gesto in gestos.items():
        print(f"Grave o gesto '{nome_gesto}'. Pressione G para iniciar e ESC para finalizar.")
        gravando = False
        contador_movimentos = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(img_rgb)

            if gravando and result.multi_hand_landmarks:
                for handLms in result.multi_hand_landmarks:
                    pontos = [coord for lm in handLms.landmark for coord in (lm.x, lm.y, lm.z)]
                    if len(pontos) == 63:
                        dados.append(pontos)
                        rotulos.append(numero_gesto)
                        contador_movimentos += 1
                    mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            texto = f"Gravando gesto: {nome_gesto} ({contador_movimentos})" if gravando else "Pressione 'G' para gravar"
            cor = (0, 255, 0) if gravando else (0, 0, 255)
            cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, cor, 2)

            cv2.imshow("Coletando Dados", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('g'):
                gravando = True
            elif key == 27:
                break
    cap.release()
    cv2.destroyAllWindows()
    return dados, rotulos

def capturar_predicoes(modelo, gestos_map):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)

        gesto = "Desconhecido"
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
                pontos = [coord for lm in handLms.landmark for coord in (lm.x, lm.y, lm.z)]

                if len(pontos) == 63:
                    pred = modelo.predict([pontos])[0]
                    gesto = gestos_map.get(int(pred), "Desconhecido")

        cv2.putText(frame, f"Gesto: {gesto}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        cv2.imshow("Reconhecimento de Gestos", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
