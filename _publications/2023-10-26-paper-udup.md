---
title: "Universal Defensive Underpainting Patch: Making Your Text Invisible to Optical Character Recognition"
collection: publications
category: conferences
permalink: https://arxiv.org/abs/2308.02369
excerpt: 'JiaCheng Deng, Li Dong, Jiahao Chen, Diqun Yan, Rangding Wang, Dengpan Ye, Lingchen Zhao, Jinyu Tian'
date: 2023-10-26
venue: 'ACM MM 2023'
---

Optical Character Recognition (OCR) enables automatic text extraction from scanned or digitized text images, but it also makes it easy to pirate valuable or sensitive text from these images. Previous methods to prevent OCR piracy by distorting characters in text images are impractical in real-world scenarios, as pirates can capture arbitrary portions of the text images, rendering the defenses ineffective. In this work, we propose a novel and effective defense mechanism termed the Universal Defensive Underpainting Patch (UDUP) that modifies the underpainting of text images instead of the characters. UDUP is created through an iterative optimization process to craft a small, fixed-size defensive patch that can generate non-overlapping underpainting for text images of any size. Experimental results show that UDUP effectively defends against unauthorized OCR under the setting of any screenshot range or complex image background. It is agnostic to the content, size, colors, and languages of characters, and is robust to typical image operations such as scaling and compressing. In addition, the transferability of UDUP is demonstrated by evading several off-the-shelf OCRs. The code is available at https://github.com/QRICKDD/UDUP.
