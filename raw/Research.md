• 핵심은 이겁니다.
  Qwen은 “숨겨진 뒷면을 복원”하는 게 아니라, 입력 이미지와 시점 지시를 조건으로 해서 “가장 그럴듯한 뒷면 이미지”를 새로 샘플링합니
  다.
  아래 설명에서 diffusion priors 부분은 공식 문서의 구조 설명을 바탕으로 한 해석입니다.

  1. Diffusion priors
  Qwen-Image는 공식적으로 20B MMDiT 기반 이미지 생성/편집 모델이고, Qwen 팀은 이 모델이 semantic editing과 novel view synthesis까지
  수행한다고 설명합니다. 특히 Qwen-Image-Edit 소개 글에서는 90도 회전뿐 아니라 180도 회전으로 “뒷면을 직접 볼 수 있다”고 예시를 듭니
  다.
  이게 가능한 이유는 모델이 학습 중에 엄청난 양의 이미지에서 “이런 앞면이면 옆면/뒷면은 대체로 이렇게 생긴다”는 시각적 사전지식을 내
  재화했기 때문입니다. 즉, 실제 3D 메쉬를 꺼내서 렌더링하는 게 아니라, 입력 앞면 + 카테고리 + 재질 + 스타일 + 프롬프트를 바탕으로 가
  장 확률이 높은 새 뷰를 생성하는 겁니다.

  2. Identity consistency
  Qwen 공식 설명의 핵심은 여기입니다. 입력 이미지를 동시에

  - Qwen2.5-VL로 넣어 semantic control
  - VAE Encoder로 넣어 visual appearance control
    하게 되어 있습니다.
    또 기술 보고서 초록에서는 T2I + TI2I + I2I reconstruction을 함께 학습해 Qwen2.5-VL과 MMDiT의 latent를 정렬한다고 설명합니다. 이
    덕분에 모델은:
  - “이 물체/인물이 무엇인가”는 유지하고
  - “현재 보이는 픽셀”의 질감, 색, 디테일도 최대한 붙잡으면서
  - 보이지 않던 부분만 새로 그릴 수 있습니다.

  그래서 뒷면을 만들 때도 완전히 새 물체를 만드는 게 아니라,
  원본의 정체성은 고정하고, 가려진 면만 plausibly hallucinate 하는 식으로 동작합니다.

  3. View-conditioned editing
  시점 변화는 사실상 조건부 편집 조건으로 들어갑니다.
  HF Space 코드에서는 슬라이더 값을 바로 프롬프트로 바꿉니다. 예를 들어 Rotate the camera ..., bird's-eye view, close-up 같은 문장을
  만들어 QwenImageEditPlusPipeline에 넣습니다.
  커뮤니티의 multi-angle 노드도 같은 방향입니다. 각도를 front view, back view, high-angle shot, close-up 같은 토큰 조합으로 바꿔 프
  롬프트를 만듭니다.

  즉, 모델 입장에서는

  - 원본 이미지
  - 유지해야 할 identity 정보
  - 목표 시점 토큰
    이 함께 주어지고, diffusion denoising 과정에서 그 조건을 만족하는 이미지로 수렴합니다.
    LoRA는 여기서 특히 “시점 토큰 -> 일관된 뷰 변화” 매핑을 더 잘 배우게 해주는 역할로 보는 게 맞습니다.

  - 비대칭 제품
  - 뒷면 로고/텍스트
  - 숨겨진 구조
  - 독특한 손상/장식
    같은 건 자주 추정해서 그립니다. 앞면은 잘 맞아도 뒷면은 틀릴 수 있습니다.
    즉, single-view novel view synthesis는 잘하지만, strict 3D consistency는 보장하지 않습니다.

  한 줄로 정리하면,

  근거:
  Qwen-Image-Edit blog (https://qwenlm.github.io/blog/qwen-image-edit/)
  Qwen-Image Technical Report abstract (https://huggingface.co/papers/2508.02324)
  Qwen-Image-Edit-2509 notes (https://github.com/QwenLM/Qwen-Image/blob/main/Qwen-Image-Edit-2509.md)
  linoyts HF Space code (https://huggingface.co/spaces/linoyts/Qwen-Image-Edit-Angles/blob/main/app.py)
  ComfyUI multi-angle node (https://github.com/jtydhr88/ComfyUI-qwenmultiangle/blob/master/nodes.py)

  원하면 다음엔 이걸 이어서
  왜 어떤 물체는 180도 회전이 잘 되고 어떤 물체는 망가지는지를 사례별로 설명해드리겠습니다.