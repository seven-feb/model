# model


scikit-learn:
요약하면, Scikit-learn은 기존 머신러닝 작업을 위한 다재다능하고 사용자 친화적인 라이브러리인 반면, TensorFlow는 딥 러닝에 탁월하고 더 복잡하고 대규모 애플리케이션에 맞게 확장 가능한 강력한 프레임워크입니다.

굳이 텐서플로우를 사용해야하는가?
ㄴㄴ

차피 딥러닝 말고 머신러닝만 하믄 될듯

라이브러리의 구성은 크게 지도 학습, 비지도 학습, 모델 선택 및 평가, 데이터 변환으로 나눌 수 있다
(scikit-learn 사용자 가이드 참조, http://scikit-learn.org/stable/user_guide.html). 지도 학습에는 서포트 벡터 머신, 나이브 베이즈(Naive Bayes), 결정 트리(Decision Tree)등이 있으며 비지도 학습에는 군집화, 이상치 검출 등이 있다. 모델 선택 및 평가에는 교차 검증(cross-validation), 파이프라인(pipeline)등 있으며 마지막으로 데이터 변환에는 속성 추출(Feature Extraction), 전처리(Preprocessing)등이 있다. 클래스별로 보자면, 각 기법들이 공통으로 가지고 있어야 하는 기본 BaseEstimator가 있으며 기법의 공통적인 부분을 모은 ClassifierMixin, RegressorMixin, ClusterMixin들이 있어 기법들은 각각의 기법의 클래스를 상속 받아 구현할 수 있다. 대부분의 클래스는 입력 데이터를 적합화하는 fit 메소드와 새로운 데이터를 예측하는 predict 메소드를 가지고 있다.


 SGD（stochastic gradient descent）
대규모 데이터(10만건 이상)의 경우 추천한다. 선형의 클래스 분류 방법이다.
출처: https://engineer-mole.tistory.com/16 [매일 꾸준히, 더 깊이:티스토리]

(3) Linear SVC
중소규모(10만건 미만)의 경우 추천하며, 선형의 클래스 분류 방법이다.
출처: https://engineer-mole.tistory.com/16 [매일 꾸준히, 더 깊이:티스토리]


(2) LASSO、ElasticNet
중소규모(10만건 미만)으로 ＊설명 변수의 일부가 중요한 경우에 추천하는 회귀 분석 방법이다.
（＊설명 변수란 ? 어떤 원인이 되고 있는 변수이다.）
출처: https://engineer-mole.tistory.com/16 [매일 꾸준히, 더 깊이:티스토리]

*   supervised.

1) 라이브러리 임포트
2) 학습 데이터나 테스트 데이터 준비
3) 알고리즘 지정과 학습 실행
4) 테스트 데이터로 테스트
5) 필요에 따라 정밀도 등을 시각화
출처: https://engineer-mole.tistory.com/16 [매일 꾸준히, 더 깊이:티스토리]


