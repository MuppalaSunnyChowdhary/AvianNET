# AvianNET

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Journal Article
% LaTeX Template
% Version 2.0 (February 7, 2023)
%
% This template originates from:
% https://www.LaTeXTemplates.com
%
% Author:
% Vel (vel@latextemplates.com)
%
% License:
% CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
%
% NOTE: The bibliography needs to be compiled using the biber engine.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Modified by:
% Pakorn Wangsuekul (joe@ai.iit.tsukuba.ac.jp)
%
% Version 2.1 (July 9, 2023)
% Version 2.2 by Hiroaki Yano (July 11, 2023) 
% Version 2.3 (July 13, 2023)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%----------------------------------------------------------------------------------------
%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS
%----------------------------------------------------------------------------------------

\documentclass[
	a4paper, % Paper size, use either a4paper or letterpaper
	10pt, % Default font size, can also use 11pt or 12pt, although this is not recommended
	% unnumberedsections, % Uncomment to remove section numbering
	% twoside, % Uncomment to enable two side traditional mode where headers and footers change between odd and even pages
]{LTJournalArticle}

\usepackage{graphicx}
\usepackage{booktabs}

\addbibresource{bibliography.bib} % BibLaTeX bibliography file


\headerright{200483456 Sunny Chowdhary, Muppala} % Right running head: Student ID and Name

\footertext{} % Text to appear in the footer, leave this command empty for no footer text

\setcounter{page}{1} % Page number of the first page, set this to a higher number if the article is to be part of a larger publication

%----------------------------------------------------------------------------------------
%	TITLE SECTION
%----------------------------------------------------------------------------------------

% Report title
\title{AvianNET: Intelligent Bird Species Identification and Diversity Monitoring System} % Article title, max 3 lines recommended

% Author's name
\author{
	Sunny Chowdhary, Muppala \hfill \fontsize{9pt}{12pt}\selectfont M.Sc. Computer Science (Data Science)
}

% Supervisor name and Laboratory name
\date{
        Supervised by: Dr. Howard Hamilton %\hfill Insert Laboratory Name Here
}

% Abstract (approx. 100 words) and keywords (approx 5 words)
\renewcommand{\maketitlehookd}{%
	\begin{abstract}
            \textbf{Abstract:} The sharp decrease in bird numbers all over the world shows we need new and smart ways to keep an eye on bird diversity. This project is about making a new kind of model that can recognize the sounds birds make, taking inspiration from the successful BirdNET project and using the latest in sound analysis and learning from data. By using special kinds of neural networks known as CNNs and a technique called MFCCs, the model will try to figure out which bird is making which sound with a lot of accuracy. It will use a large collection of bird sounds from the Xeno-canto database. This study will tackle the problem of differences in sound data and will include important background information to better identify the birds. The process involves careful preparation of the data, teaching the model, and checking its performance with well-known standards. The expected result is a strong tool for studying nature, which will help in protecting birds and understanding their diversity.

            \textbf{Keywords:} bird sound recognition, biodiversity monitoring, Convolutional Neural Networks, Mel-Frequency Cepstral Coefficients, audio analysis, deep learning, Xeno-canto, acoustic data processing
	\end{abstract}
}

%----------------------------------------------------------------------------------------

\begin{document}

\maketitle % Output the title section

%----------------------------------------------------------------------------------------
%	ARTICLE CONTENTS
%----------------------------------------------------------------------------------------

\section{Introduction}

In this project, I aim to develop a bird sound recognition model inspired by BirdNET, utilizing advanced audio analysis and machine learning techniques to accurately identify bird species from their calls. My research draws upon insights from the paper ``Cognizance of the Action of Humans by Applying Enhanced Techniques,'' addressing the natural language processing challenge of distinguishing bird calls with precision. This involves employing Convolutional Neural Networks (CNNs) for feature extraction from audio inputs, mirroring emotion recognition strategies by converting vocal sounds into visual data for analysis.

I plan to utilize Mel-Frequency Cepstral Coefficients (MFCCs) among other techniques to enhance the model's ability to classify a broad spectrum of bird calls accurately. The primary input for my model will be audio recordings of bird vocalizations, with the output consisting of detailed species classification results. Integrating contextual information is also considered to further improve accuracy.

The remainder of this paper will include a literature review that highlights the foundational work of BirdNET and other critical studies. It will be followed by a detailed discussion of my methodology, experimental approach, results, and the broader implications of my work. Through this exploration, I aim to provide insights into the development and application of the bird sound recognition model, underscoring its potential impact on biodiversity monitoring and ecological research.


\section{Background Work}

In developing a model similar to BirdNET, we can draw inspiration and insights from the paper titled ``Cognizance of the Action of Humans by Applying Enhanced Techniques.'' This paper delves into the realm of emotion recognition using Convolutional Neural Networks (CNNs), providing valuable lessons that can be applied to bird sound recognition.

One key takeaway from the paper is the significance of feature extraction in audio analysis. The authors discuss transforming vocal inputs into visual representations like spectrograms or mel-frequency cepstral coefficients (MFCCs). Similarly, in our endeavor to recognize bird sounds, we can utilize techniques such as MFCCs to extract pertinent features from audio recordings of bird calls.

Furthermore, the paper underscores the importance of meticulous data preparation and effective model training. By following similar strategies for data preprocessing, model architecture selection, and optimization, we can enhance the accuracy and robustness of our bird sound recognition model.

Additionally, the paper highlights the potential of integrating multimodal data for comprehensive analysis. While BirdNET primarily focuses on audio data, incorporating additional contextual information such as location and habitat characteristics could further improve the model's performance.

Moreover, the nuanced pattern recognition capabilities of CNNs discussed in the paper can be instrumental in accurately identifying diverse bird species. Leveraging CNN's ability to capture intricate patterns in audio data, we can develop a model that excels in classifying various bird calls with precision.

In summary, by leveraging the skills and insights gleaned from the paper ``Cognizance the Action of Human by Applying Enhanced Techniques,'' we can create a robust bird sound recognition model akin to BirdNET, capable of accurately identifying bird species through advanced audio analysis techniques and machine learning algorithms.



\section{Literature Review}

BirdNET is a deep learning-based approach for identifying bird species from audio recordings, offering high accuracy and domain-specific data augmentation. This approach addresses limitations in previous solutions, such as lower accuracy, limited species range, and poor performance in diverse environmental conditions. BirdNET's effectiveness in real-world scenarios demonstrates its potential to revolutionize avian biodiversity monitoring, setting a new benchmark for future research and applications in the field.

The Residual Network (ResNet) architecture is used for its scalability and ease of implementation, comprising 157 layers, including 36 weighted ones, to effectively classify bird species from audio spectrograms. \cite{KAHL2021101236} 

The architecture includes a pre-processing block for input transformation, residual stacks for feature extraction, and a classification block for species identification, employing techniques like global log-mean-exponential pooling and sigmoid activation for accurate, multi-class predictions. This design facilitates the model's ability to handle a large dataset of bird sounds, demonstrating the applicability of deep learning in biodiversity monitoring.

The BirdNET system's evaluation employed sample-wise and class-wise mean average precision metrics, reflecting its real-world applicability and balanced measurement across species. The system demonstrated high accuracy in focal recordings, with a notable performance in detecting primary bird species. However, its effectiveness decreased in soundscapes due to challenges in densely vocal environments. Continuous stream data analysis revealed the system's potential to track seasonal avian diversity changes, aligning closely with human observer data for migratory species.

\begin{figure}[htbp]
\centering
\includegraphics[width=\linewidth]{Fig-2.jpg}
\caption{(a) Hotspots and mic location (Google Maps) (b) Lab building and mic location (Robert Barker)}
\label{fig:fig2}
\end{figure}

Fig. \ref{fig:fig2} illustrates eBird observational data collection at designated hotspots, where bird counts are regularly conducted by experts and citizen scientists. The vicinity of the Cornell Lab of Ornithology, marked by dense vegetation and a large pond, falls within the acoustic range of the project's live stream microphone. This setting underscores the project's strategic placement of microphones to capture avian vocalizations for analysis, emphasizing the methodological rigor in evaluating BirdNET's performance against established birdwatching practices.

The discussion highlights BirdNET's capacity to mirror human observer data in identifying bird species across numerous classes, despite challenges like acoustic domain mismatches and variable sound quality. Comparative analysis with other studies underscores BirdNET's competitive edge, while insights gained underscore the importance of model design choices and training strategies for optimizing acoustic event recognition.

The conclusion underscores the growing feasibility of Passive Acoustic Monitoring (PAM) in ecology due to decreasing hardware costs, highlighting its potential for community-level studies beyond targeted species. BirdNET, with its ability to identify a broad array of bird species efficiently, exemplifies the advances in PAM technology.

The paper "Cognizance the Action of Human by Applying Enhanced Techniques" explores the application of Convolutional Neural Networks (CNN) in emotion recognition. The model is used to analyze speech and understand human emotions through voice, transforming vocal inputs into visual representations like spectrograms or mel-frequency cepstral coefficients (MFCCs). \cite{9262419}

This technique, a departure from traditional models like Hidden Markov Models (HMM) and Support Vector Machines (SVM), demonstrates the nuanced capacity of CNNs to capture the intricacies of speech indicative of one's emotional condition. The multifaceted approach, integrating facial recognition and textual analysis alongside speech recognition, provides a comprehensive framework for emotion detection.

The CNN model learns from complex speech patterns, similar to how it learns from images. The audio data is meticulously prepared to train the model effectively. This advanced approach significantly advances the capability to classify and understand emotions from human speech, demonstrating the versatility and power of CNNs in processing not just images but complex audio data as well.

\section{Dataset Information}

For this project, I will be utilizing real-world data from a diverse range of bird sounds. The main source of this data is Xeno-canto \cite{XenocantoDataset}, a community-driven platform that houses a vast collection of bird audio recordings contributed by both amateurs and professionals from around the globe. Given the varied nature of these recordings in terms of duration, quality, and format, a systematic approach to data preparation is essential to ensure the usability of this data for training and testing the model.

\subsection{Data Preparation}

The audio files from Xeno-canto exhibit a wide variety of characteristics, including different sample rates, bit depths, and number of channels. To address these discrepancies, I will standardize the files into two main sets with uniform properties. For the first set, all audio files will be resampled to a standard high fidelity rate of 44.1 kHz, followed by normalization to achieve a consistent maximum signal amplitude of -3 dB, ensuring that the loudness across recordings is relatively uniform.

A second set will undergo a more rigorous preprocessing routine to potentially enhance the model's ability to focus on relevant frequencies. This includes applying a high-pass filter at 2 kHz to remove lower frequency noises, resampling the audio to 22050 Hz to reduce complexity, converting stereo recordings to mono to standardize channel count, and normalizing these files to -3 dB as well.

To augment the training dataset, I will extract additional audio files from the soundscapes provided by Xeno-canto, using metadata annotations to identify specific bird species. This will enrich the variety of bird calls available for the model to learn from.

Further segmentation will be applied to separate the audio content into distinct categories:
\begin{itemize}
    \item \textbf{BirdsOnly}: Segments purely containing bird calls or songs.
    \item \textbf{NoiseOnly}: Segments consisting of background noise without bird calls.
    \item \textbf{AtmosOnly}: A subset of NoiseOnly with longer sequences of ambient sounds, providing a realistic background atmosphere for the model.
    \item \textbf{LowQuality}: To simulate conditions of low-quality or highly compressed recordings, this dataset is created by encoding audio files to a low-bitrate MP3 format and then decoding them back to WAV.
\end{itemize}

This segmentation is achieved through image processing techniques applied to spectrograms of the audio files, allowing for the extraction of specific sound events. Each category serves a different purpose in training, from focusing on bird sounds to understanding and filtering out background noise.

\subsection{Model Evaluation}

The training data will be split into training and validation sets, using stratified folds to ensure a balanced representation of bird species. This approach also considers the individuality of bird calls; audio files that are likely from the same bird (identified by recording author, date, and species) are grouped, ensuring they are all part of either the training or validation set to avoid bias.

By meticulously preparing and segmenting the data from Xeno-canto, I aim to create a robust dataset that will enable the deep learning model to accurately recognize and classify bird calls, even in challenging listening conditions.


\section{Methodology}

In this section, I outline the approach and techniques I plan to employ for developing the bird sound recognition model. The goal is to craft a model that is both accurate and efficient in identifying various bird species from audio recordings.

\subsection{Deep Learning Approach}

For the backbone of my project, I intend to use Convolutional Neural Networks (CNNs), a type of deep learning model renowned for its effectiveness in analyzing visual imagery. Although bird calls are audio data, by transforming these sounds into spectrograms—a visual representation of the sound spectrum over time—we can leverage CNNs for feature extraction. This method has been successfully applied in similar contexts, like emotion recognition from speech, by converting audio inputs into formats that highlight essential characteristics for analysis.

I plan to explore various CNN architectures, such as Residual Networks (ResNets), which are known for their deep structure without losing performance due to vanishing gradients, making them suitable for complex pattern recognition tasks like bird call identification. The rationale behind selecting CNNs and specifically architectures like ResNets is their proven track record in handling audio classification tasks by capturing intricate patterns in data.

\subsection{Data Collection and Preparation}

The primary source for audio recordings of bird calls will be the Xeno-canto database, an extensive online collection of bird sound recordings from around the world. To ensure the model is trained on high-quality and diverse data, I will apply several preprocessing steps:

\begin{itemize}
    \item \textbf{Noise Reduction:} To improve the clarity of the bird calls, background noise will be minimized using audio processing techniques.
    \item \textbf{Segmentation:} Longer recordings will be segmented into shorter clips, ensuring that each segment primarily contains a single bird call.
    \item \textbf{Normalization:} Audio files will be normalized to maintain a consistent volume level across the dataset.
\end{itemize}

For data augmentation, I plan to introduce slight variations in pitch, speed, and background noise to the training data. This step aims to make the model more robust to variations in real-world conditions.

\subsection{Evaluation and Validation}

The model’s performance will be evaluated using standard metrics such as accuracy, precision, recall, and F1 score. These metrics will help in understanding the model's effectiveness in correctly identifying bird species from their calls. To ensure the model's generalizability, I will use a split of the data into training, validation, and test sets, with careful attention to include a diverse representation of species in each set.

For validation and benchmarking, the model will be compared against existing solutions like BirdNET. This comparison aims to gauge the model's performance in real-world scenarios and its improvements over current state-of-the-art solutions. Additionally, I will employ cross-validation techniques to ensure that the model's performance is consistent across different subsets of the data.

Through this methodology, I aim to develop a bird sound recognition model that is not only accurate and reliable but also contributes valuable insights and tools for biodiversity monitoring and conservation efforts.



\section{Schedule}


Here's my plan laid out simply, breaking down the big tasks and when I hope to get them done for our bird sound project.

\begin{enumerate}
    \item \textbf{Discussing the Project Idea:} The project idea will be polished and sent off by January 19, 2024.
    \item \textbf{Gathering Bird Sounds:} After receiving approval, bird call recordings will be collected from Xeno-canto and cleaned up, with this phase concluding by February 10, 2024.
    \item \textbf{Building the Model:} Starting February 13, 2024, the model development will begin, aiming for a basic version operational by March 1, 2024.
    \item \textbf{Initial Testing:} A test run with some data to evaluate the model's performance is planned from March 8 to March 15, 2024.
    \item \textbf{Improving the Model:} Based on initial tests, improvements and potentially more data will be added from March 16 to April 1, 2024.
    \item \textbf{Thorough Check:} The model will undergo a thorough comparison with similar tools between April 8 and April 22, 2024.
    \item \textbf{Wrapping Up:} Final report preparations and project review will be done by April 23, 2024.
    \item \textbf{Show and Tell:} The project, along with findings and learnings, will be presented at the end of April 2024.
\end{enumerate}

This plan is structured to ensure a smooth workflow and comprehensive coverage of all essential stages from inception to completion.

%----------------------------------------------------------------------------------------
%	 REFERENCES
%----------------------------------------------------------------------------------------

\printbibliography % Output the bibliography
%----------------------------------------------------------------------------------------

\end{document}
