<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/F8C--9F5toJF6s-p_nAMtdGK3sZs1GV8kAWQuObXBPbRh7XrXbR485BENluvC3Uydk7OrdCboIiQJSuWIaS-WSbqqsri8U7N9k6dENxRb6q2CP-2UOJ7pzfAfU_30ksG3pmy6D0Bfs7XuNLlIaA-ygmcsHyUKvSawDVi154t_BDk3yK2LNz3BiSNeePaVhCx-alM-abJ4BR1DKXxLhoIrRLUduKw4VLVNKcifXqm1zbNzRrYZG_-eINwTxpDJb032YfFE5yHtj4JcSrN5wcEjJWRsSABopSc1IXOnGrGBHL69c7rUlYbkd8IsT2NyzQAk7P-K-Fg1p3bxULcSjYoUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 01:05:01</div>
<hr>

<div class="tg-post" id="msg-85830">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6577c5fe83.mp4?token=Bf9xrBwF6Jtq_f7yP_pvdmyFo2yVGXgLsrEtpB2bas5LkY40a3INk9ySuXXQCyhBq9HKYTbJFGCr17q7xyrsvuiIi9ckh_Au-nkEz7S4xwy7b4Jy2T_tyj1F0BGD6m8lShIr1XkroPCUlw0iigYhw1qQ9ibgyFa12_ctASvxIMj2kVlFJ16OwCBaTSozx602wF8XSd4i1RSg15fOw4q7WEbmiMlWQw-YwkQih6p8qM9Bg45AcrM0uQrpXu4anMgWRu3qnJeh80h9_lH-pZFVCYWwUamjxbSMFgX0PED5CQtJKetZxsQShgDHfJeC6ezyXBkeQEYS9RHUd2zOrMJuDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6577c5fe83.mp4?token=Bf9xrBwF6Jtq_f7yP_pvdmyFo2yVGXgLsrEtpB2bas5LkY40a3INk9ySuXXQCyhBq9HKYTbJFGCr17q7xyrsvuiIi9ckh_Au-nkEz7S4xwy7b4Jy2T_tyj1F0BGD6m8lShIr1XkroPCUlw0iigYhw1qQ9ibgyFa12_ctASvxIMj2kVlFJ16OwCBaTSozx602wF8XSd4i1RSg15fOw4q7WEbmiMlWQw-YwkQih6p8qM9Bg45AcrM0uQrpXu4anMgWRu3qnJeh80h9_lH-pZFVCYWwUamjxbSMFgX0PED5CQtJKetZxsQShgDHfJeC6ezyXBkeQEYS9RHUd2zOrMJuDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الانفجارات العنيفة داخل مقرات المعارضة الكردية الإرهابية في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/naya_foriraq/85830" target="_blank">📅 01:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85829">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875863048f.mp4?token=qJq_TVZ9TyEBrmFTpVE92l_PU-j3zeGe8e5TxiEzXPwFOCQe8_zSe99zQnv0eHjSPKpH4ZGfBnldugYyuh6IG_k7ySiOi1fbJJY1uAEU6TNWfiD4O0OJuQ9cLWqTdvTFOauuNgBBxoovKpQQujO9__38SjeT442Ee1m2pTlXJlLVhN8dsfp4BrkUicvx9Vpn_51dK3RASnBxJ5h_2hzdUOt-OtucdqCigWEuNKLIstiJmlEb3cJXjt2HbXb705Gl4lj8O0lyp_jHb9xn4DuH9e3JPZ7k2GkzhGehfLyhelDN1_o9AoMLuOVLdwQp9MnkeS32fDL2S9hENBghfn7NRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875863048f.mp4?token=qJq_TVZ9TyEBrmFTpVE92l_PU-j3zeGe8e5TxiEzXPwFOCQe8_zSe99zQnv0eHjSPKpH4ZGfBnldugYyuh6IG_k7ySiOi1fbJJY1uAEU6TNWfiD4O0OJuQ9cLWqTdvTFOauuNgBBxoovKpQQujO9__38SjeT442Ee1m2pTlXJlLVhN8dsfp4BrkUicvx9Vpn_51dK3RASnBxJ5h_2hzdUOt-OtucdqCigWEuNKLIstiJmlEb3cJXjt2HbXb705Gl4lj8O0lyp_jHb9xn4DuH9e3JPZ7k2GkzhGehfLyhelDN1_o9AoMLuOVLdwQp9MnkeS32fDL2S9hENBghfn7NRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشوب حرائق واسعة داخل مقرات المعارضة الكردية الإيرانية في محافظة أربيل العراق عقب استهدافها بالطيران المسير الانتحاري.</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/naya_foriraq/85829" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85828">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f8527a49.mp4?token=bSU3VvVu32uSuvKTsC9HUcg5d0u79fSv1hbgqVXTohZZiLfu0z0a2mt0dCrNdHztgGdBBsHungx84bKX4zM6o0q6XtSoA2MJtlnQkyvcX5aAI1gYsx2AOXJcKh1xokl4nl9gyf6Zq4C6QpqMzjnMcxsvd7xDxlwbrmTsxSWqYZEAOJUknkwgFCtQnyhXn_nvWuUvxDf7s6W0DDMQz21j4-m61Sdo0wFaTWzGKLVhHUAOMqLyWcZZ74VBIXFbRFm-xSJ8iGXKLMzzSyEYLUb_ij1SkndxAV8KwlCTbNsj-Ip1t9d4_eNpepSExWxDQCxq3ph691G_e77zvKINpbvGag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f8527a49.mp4?token=bSU3VvVu32uSuvKTsC9HUcg5d0u79fSv1hbgqVXTohZZiLfu0z0a2mt0dCrNdHztgGdBBsHungx84bKX4zM6o0q6XtSoA2MJtlnQkyvcX5aAI1gYsx2AOXJcKh1xokl4nl9gyf6Zq4C6QpqMzjnMcxsvd7xDxlwbrmTsxSWqYZEAOJUknkwgFCtQnyhXn_nvWuUvxDf7s6W0DDMQz21j4-m61Sdo0wFaTWzGKLVhHUAOMqLyWcZZ74VBIXFbRFm-xSJ8iGXKLMzzSyEYLUb_ij1SkndxAV8KwlCTbNsj-Ip1t9d4_eNpepSExWxDQCxq3ph691G_e77zvKINpbvGag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی در مقرهای تجزیه طلبان تروریست در اربیل عراق.</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/naya_foriraq/85828" target="_blank">📅 01:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85827">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a82d562b.mp4?token=T1QCXLvI4xwdr9R_9A9fRr9v52f2LQB5oywS7VMGSjBRGa9uyUK6dlCh67KWpl646tVSGedERedi3SX0-XkOeu-Lzg-X3zXwQ7c_VGLMp4b3ogNOaThenrL-lfOwk5Px6IESQq2aU7jzrABe8qCuKm0L4mfllzV1NMdkwd6Kmsj156l6Ayo-OcsXE4RF7iZpdrySEGwboTR40dzqgAFpx_2s9TQuAgIlLyJllcKw29n4uvMjubGC-TDizQ-1Z3th30YGAQhWWQ56cDW_jWNIYcIOn1iz-pcOGMpYQIUbVcfD62Je-UgD6JupzNNz1ee5vdwHgx68fGEXtoEV_TQLEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a82d562b.mp4?token=T1QCXLvI4xwdr9R_9A9fRr9v52f2LQB5oywS7VMGSjBRGa9uyUK6dlCh67KWpl646tVSGedERedi3SX0-XkOeu-Lzg-X3zXwQ7c_VGLMp4b3ogNOaThenrL-lfOwk5Px6IESQq2aU7jzrABe8qCuKm0L4mfllzV1NMdkwd6Kmsj156l6Ayo-OcsXE4RF7iZpdrySEGwboTR40dzqgAFpx_2s9TQuAgIlLyJllcKw29n4uvMjubGC-TDizQ-1Z3th30YGAQhWWQ56cDW_jWNIYcIOn1iz-pcOGMpYQIUbVcfD62Je-UgD6JupzNNz1ee5vdwHgx68fGEXtoEV_TQLEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملیات لت و پار کردن تروریست‌های تجزیه طلب در شمال عراق ادامه دارد.</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/naya_foriraq/85827" target="_blank">📅 01:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85826">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3b235c206.mp4?token=VcL7fyJ0_R6To0dAB7vkHav-oEzszKC-JhaR5bl01sxOnqKwBP4uPvmdi8s3H3hQdWCrQACjfn_5O2lKytAQ-Hz94aU2OEAMUSWA92X_frebc_5ZhxTSef6qUklhemTgM8F9BPFjcH6TO4VQff6EWbWq0lR-Ts1-iBvJmaWw4HouDuCHOmLBMnf-Om_Zsr6JyV5_T6K1SUAN7O8uJHzuhpC9Ixxw0Xcl4JmE7ZICV38mCkxpu9im5KFFfOxq0LYz5sKCLkeR250fnQG58--CUS0PdaDFoRtS8VGUv_9YGZ0qf2ohx3ImHhZXNcEBfl3aiUNGplrUqm13ysok3iDG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3b235c206.mp4?token=VcL7fyJ0_R6To0dAB7vkHav-oEzszKC-JhaR5bl01sxOnqKwBP4uPvmdi8s3H3hQdWCrQACjfn_5O2lKytAQ-Hz94aU2OEAMUSWA92X_frebc_5ZhxTSef6qUklhemTgM8F9BPFjcH6TO4VQff6EWbWq0lR-Ts1-iBvJmaWw4HouDuCHOmLBMnf-Om_Zsr6JyV5_T6K1SUAN7O8uJHzuhpC9Ixxw0Xcl4JmE7ZICV38mCkxpu9im5KFFfOxq0LYz5sKCLkeR250fnQG58--CUS0PdaDFoRtS8VGUv_9YGZ0qf2ohx3ImHhZXNcEBfl3aiUNGplrUqm13ysok3iDG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق للحظة إستهداف مقر تابع للإنفصاليين في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/naya_foriraq/85826" target="_blank">📅 00:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85825">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/decaacf8b1.mp4?token=PhixCQ-HlO5kNvSy8xVCa9z1mInNXemD9_MEn78ShO8zZZpysPqWcBaxaRZYrVM8UEG6DPpepouCkZvO1iGItdwrMTGTTpyj0MYPLhP1zubyCuCLW_oFjsFcV1BbYhDy2LuGU5kMiR-Ywr9NN9knmcR1bNvJJwkHPKm01efeG6HIXn9in2Hm5doEhFcnRFviOaoFt1hHxxE7-kPtsdg2jkGfhTgv9vmR8cJx5ykkJGuk2gHceQQ-gjWpZJUKcAqppysBakKghvJwCkWo_606pJBDeom1Vosdo4LRqRVqNxZCzmlg0UhcSeAg-o_AUeLd9iAxAbV29wgv_FIEaJVkpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/decaacf8b1.mp4?token=PhixCQ-HlO5kNvSy8xVCa9z1mInNXemD9_MEn78ShO8zZZpysPqWcBaxaRZYrVM8UEG6DPpepouCkZvO1iGItdwrMTGTTpyj0MYPLhP1zubyCuCLW_oFjsFcV1BbYhDy2LuGU5kMiR-Ywr9NN9knmcR1bNvJJwkHPKm01efeG6HIXn9in2Hm5doEhFcnRFviOaoFt1hHxxE7-kPtsdg2jkGfhTgv9vmR8cJx5ykkJGuk2gHceQQ-gjWpZJUKcAqppysBakKghvJwCkWo_606pJBDeom1Vosdo4LRqRVqNxZCzmlg0UhcSeAg-o_AUeLd9iAxAbV29wgv_FIEaJVkpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/naya_foriraq/85825" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85824">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/naya_foriraq/85824" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85823">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a653f7d251.mp4?token=QlBrbwggx8p-ZOEU7iXrW2A9JJ7XJKXsGlMi2T-oNq5n0GSztYm-6aeVr4bWd9OjAvBBDE6KJ96KlrKks5cywAa_sO-Ti3NwcTOq6B3g0byWwUf1dnVhFhJZuKh3QVnYV8_7_6ujCFSykS6g8fxAFk6XdBLbibvWX3HM1CnMYjVkz4ycGU58gW5wa10VegQHdnkyn8cmqdfPWHVqHFZlPknJ_DWzfcnmHRVJ2wievbt7jcIxIvSUaWhymuBao6QBtIpnh9ZposdhWyy_Q7VOHtn6qEjexrqhTXgKsAL6IaBS4CTxhDTh04pssQ6ttNpwNqXaw8_EGW9i9HjGsXO-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a653f7d251.mp4?token=QlBrbwggx8p-ZOEU7iXrW2A9JJ7XJKXsGlMi2T-oNq5n0GSztYm-6aeVr4bWd9OjAvBBDE6KJ96KlrKks5cywAa_sO-Ti3NwcTOq6B3g0byWwUf1dnVhFhJZuKh3QVnYV8_7_6ujCFSykS6g8fxAFk6XdBLbibvWX3HM1CnMYjVkz4ycGU58gW5wa10VegQHdnkyn8cmqdfPWHVqHFZlPknJ_DWzfcnmHRVJ2wievbt7jcIxIvSUaWhymuBao6QBtIpnh9ZposdhWyy_Q7VOHtn6qEjexrqhTXgKsAL6IaBS4CTxhDTh04pssQ6ttNpwNqXaw8_EGW9i9HjGsXO-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرة اخرى استهداف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/naya_foriraq/85823" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85822">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مشاهد اخرى لاستهداف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/naya_foriraq/85822" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85821">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79187ad90d.mp4?token=oU01AFasdMcpJYFeFUwiWJ1dsa6CGpqjDHLb_TOUOlSpyCderRZOcIYuoyGrL0OOTVzCkg4i4XxSBjQxW0fL1E1VE4iTMDqPJjk8DGPNdaHaef0IMsqLGI6vSi-bVcRhhg8Lg6nID3xJQbmGnZIgOK7OnNMw__POJQDtA2bKZyo4tfbfl94r1njSlqZ-fP9xePb-5y79A_fnBDxqrIx_A9MUHsdv8PcsTGsDZ8L3_L_-ZY9vv3gkGVhRfF16nflbV7kPhJbQKz1s6CdXbOy7mU3E0Us9DHcYwRe8fdSn9g6dVcNPwyC4NbS0eXnZEwBJEjKA2KJwV4VebMwGfDLXdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79187ad90d.mp4?token=oU01AFasdMcpJYFeFUwiWJ1dsa6CGpqjDHLb_TOUOlSpyCderRZOcIYuoyGrL0OOTVzCkg4i4XxSBjQxW0fL1E1VE4iTMDqPJjk8DGPNdaHaef0IMsqLGI6vSi-bVcRhhg8Lg6nID3xJQbmGnZIgOK7OnNMw__POJQDtA2bKZyo4tfbfl94r1njSlqZ-fP9xePb-5y79A_fnBDxqrIx_A9MUHsdv8PcsTGsDZ8L3_L_-ZY9vv3gkGVhRfF16nflbV7kPhJbQKz1s6CdXbOy7mU3E0Us9DHcYwRe8fdSn9g6dVcNPwyC4NbS0eXnZEwBJEjKA2KJwV4VebMwGfDLXdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف يستهدف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/naya_foriraq/85821" target="_blank">📅 00:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85820">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af9e5cd42.mp4?token=aw2F5QIRXMJHbaTUU54DIncsiyxZR2MQgS6BTkxx8c315zl3AkW4gEu5ZF8bUjBZeTnnCwOx_tV-DJ_OtjDREGzR7fIBA0owZ4LOOh6SA_VqJKi2rshOJ_XMAbC87zF77aJI1HcfYtyPZZWm5A6LyzdtbbbtGXYwZWxwg3fV5IKAot3kvCbEZviQLr6E4YEeaCxiWrUAFXWG1J_DjRqaUhIMD3L56FCZis7qnbvT_Qf34D0uwLmmt4ptPKfHIbtfOdJuG6KWrRni-pR77yeLnp3kTpVZzQpMhF9ylnkXL1cPOg56O60rFbcvgO1nAhENogJz9ijA8yGV7ms92oJOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af9e5cd42.mp4?token=aw2F5QIRXMJHbaTUU54DIncsiyxZR2MQgS6BTkxx8c315zl3AkW4gEu5ZF8bUjBZeTnnCwOx_tV-DJ_OtjDREGzR7fIBA0owZ4LOOh6SA_VqJKi2rshOJ_XMAbC87zF77aJI1HcfYtyPZZWm5A6LyzdtbbbtGXYwZWxwg3fV5IKAot3kvCbEZviQLr6E4YEeaCxiWrUAFXWG1J_DjRqaUhIMD3L56FCZis7qnbvT_Qf34D0uwLmmt4ptPKfHIbtfOdJuG6KWrRni-pR77yeLnp3kTpVZzQpMhF9ylnkXL1cPOg56O60rFbcvgO1nAhENogJz9ijA8yGV7ms92oJOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار طيران المسير في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/naya_foriraq/85820" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85816">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207797b8fe.mp4?token=iVImswSfPVua3wpM_BpGVhVev7We1o5KllgobKfXqhTUHJ2WUqmBvarkd4n7c5r9tGW3uM2NOrAHOXTadkVcclqjMGBXT7H5uB6tCcMmNssky7wv0uLjpV2JABnp1aAnnm1gJZRXqA_rUJ69WHnlWdh4j7hKKOSn5viYPzYdxb2SqphGhHv0C_h-PhfD2qq-ZKxk51pcSa_wFKjX0Xa-twwUHZudBgmmLn82LtVzcKHoILcq6yt3teojRqosyO7IK4uZ1PO-ZNRqXkjOjab9-NvYJQJSZ37IVu24ypmfTgmZYc24bIC1-krBCqcmG63FCGDtRANRIBBh5BqhHNIw7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207797b8fe.mp4?token=iVImswSfPVua3wpM_BpGVhVev7We1o5KllgobKfXqhTUHJ2WUqmBvarkd4n7c5r9tGW3uM2NOrAHOXTadkVcclqjMGBXT7H5uB6tCcMmNssky7wv0uLjpV2JABnp1aAnnm1gJZRXqA_rUJ69WHnlWdh4j7hKKOSn5viYPzYdxb2SqphGhHv0C_h-PhfD2qq-ZKxk51pcSa_wFKjX0Xa-twwUHZudBgmmLn82LtVzcKHoILcq6yt3teojRqosyO7IK4uZ1PO-ZNRqXkjOjab9-NvYJQJSZ37IVu24ypmfTgmZYc24bIC1-krBCqcmG63FCGDtRANRIBBh5BqhHNIw7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار محاولات الاعتراض والتصدي لمسيرات في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/naya_foriraq/85816" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85814">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4a468f9f.mp4?token=qSoxH-ttpPGfTjhkyj7FbBrzHK8arsN1gaKLBGTiLPJ0lrq-kV6T7on2UihY4LtT5r289iecsOoldohImyQhbu0puzwCIvSITHGwHC0WV4ZWM8J4e--G7pS8sZFElB-hNZx2HkIeCDysBWKeH9MNDtH2RDWDyche-ak5Dj-v_JPxm8K-LQUYIpNJjp_poJfvxj3gDZOat2mvJclMJniQavJJQrBEya6mHWiiyP-DewL5Q9lLlw-HYUqpwatQoRYggdBHQByz2e59xqzEHSU0dcv_6drnVowlAbwkbzQT_DRZ4cYVwScMZaYcsl60fgyCiSEBqocfuw2WEYVU80ZJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4a468f9f.mp4?token=qSoxH-ttpPGfTjhkyj7FbBrzHK8arsN1gaKLBGTiLPJ0lrq-kV6T7on2UihY4LtT5r289iecsOoldohImyQhbu0puzwCIvSITHGwHC0WV4ZWM8J4e--G7pS8sZFElB-hNZx2HkIeCDysBWKeH9MNDtH2RDWDyche-ak5Dj-v_JPxm8K-LQUYIpNJjp_poJfvxj3gDZOat2mvJclMJniQavJJQrBEya6mHWiiyP-DewL5Q9lLlw-HYUqpwatQoRYggdBHQByz2e59xqzEHSU0dcv_6drnVowlAbwkbzQT_DRZ4cYVwScMZaYcsl60fgyCiSEBqocfuw2WEYVU80ZJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء محافظة اربيل تشتعل اثر الهجوم على مقرات الاحزاب المعارضة الايرانية.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/naya_foriraq/85814" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85813">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d950af84df.mp4?token=oHxCGLITYAIwuNOOG7NAo_PBB6jsUWpYOyMdTR0MMBeM2smmELtWxXOwZtMTevbR1XgLwd_wCiL_B6pI8QWvZsU7aqZPraRWMryShFR_Hk0kqDDQw-R8dPsPSiOC2sAFrdpbItZON64z7x7LEfemVS8ExgsQ_UXu3vQ2R_lMv_TnoW09OtEhXTlWaR-fx6cP0E-oQJsNkKk1Im3AQPMumIy5TfLYqephJd9-fNaovTYoXD6vvk8U6Eehd8KXESPCIgBKPk0PINX8ZWvxOQSocLKR5b1Pk_sGBhZuPsPnfpqVKwJN5WNxhbxs7Wvhk9vwJ_r4uulsBBZbW6nZplXEMkdlp5kYvBZEj1b15bCbSEVM4h_Eh47HwskoKNFOHfm7x3KuMdlW1h0pG_y_AWQ8VC-k9hgu3IHDJ1x05LENrErlX6fb8omKJXscS7JWhPooUgCwGN9wTV5QpMp_I1mg1fND6ZV24ddpM33LUzu3bcP9RrgMaw2RDdUMgCxnO_Rk6T_HCkG6e6oNo2YkS49ojhk_M6D3EGQNP_qEJ6ZcwGAYZjjUMiYBkQ1HHcewxSa-pEO0RohMr1DuA3GCpypZID_FR68_cy5elpKPpa4QtbSdcxklMuAGaCnLozmngBk6Cu81mFdBp48pKi9XW3ojI6mtCfoH_zyNKpITSvJpQcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d950af84df.mp4?token=oHxCGLITYAIwuNOOG7NAo_PBB6jsUWpYOyMdTR0MMBeM2smmELtWxXOwZtMTevbR1XgLwd_wCiL_B6pI8QWvZsU7aqZPraRWMryShFR_Hk0kqDDQw-R8dPsPSiOC2sAFrdpbItZON64z7x7LEfemVS8ExgsQ_UXu3vQ2R_lMv_TnoW09OtEhXTlWaR-fx6cP0E-oQJsNkKk1Im3AQPMumIy5TfLYqephJd9-fNaovTYoXD6vvk8U6Eehd8KXESPCIgBKPk0PINX8ZWvxOQSocLKR5b1Pk_sGBhZuPsPnfpqVKwJN5WNxhbxs7Wvhk9vwJ_r4uulsBBZbW6nZplXEMkdlp5kYvBZEj1b15bCbSEVM4h_Eh47HwskoKNFOHfm7x3KuMdlW1h0pG_y_AWQ8VC-k9hgu3IHDJ1x05LENrErlX6fb8omKJXscS7JWhPooUgCwGN9wTV5QpMp_I1mg1fND6ZV24ddpM33LUzu3bcP9RrgMaw2RDdUMgCxnO_Rk6T_HCkG6e6oNo2YkS49ojhk_M6D3EGQNP_qEJ6ZcwGAYZjjUMiYBkQ1HHcewxSa-pEO0RohMr1DuA3GCpypZID_FR68_cy5elpKPpa4QtbSdcxklMuAGaCnLozmngBk6Cu81mFdBp48pKi9XW3ojI6mtCfoH_zyNKpITSvJpQcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاقات دفاعية في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/naya_foriraq/85813" target="_blank">📅 00:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85812">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec823fea58.mp4?token=hfFSfRDbyEzmHn01ZzwaoC4rLSyFiznGfPg8AzpOguQk3eq5n6Nc7eK8ZJehHf-JChfawQh2mgD1-B5gywKBGxnpu4sTtqMO5mEXrvVRF9xsfRYzlWGHinhXIQd7KZduv21zNNNWKaeZWnCshsejNKU3kZQKCqHB5CWezL3p6qlZaE3VuPZKNRjvmdXjodFwSH67Aq_d1ivKWgyJagxNB2cwgcqI0azmQXmhKtW-S6jxAGUol1gagwf8uJRJ_MhHXG9BeMeu4f8FTOVuW31jHVQ63Guk28sqR_EgU2IoPxHCFmvJqHJnfA-zgBX_dRqaX5FEkX1fZZhcxz0jFBphsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec823fea58.mp4?token=hfFSfRDbyEzmHn01ZzwaoC4rLSyFiznGfPg8AzpOguQk3eq5n6Nc7eK8ZJehHf-JChfawQh2mgD1-B5gywKBGxnpu4sTtqMO5mEXrvVRF9xsfRYzlWGHinhXIQd7KZduv21zNNNWKaeZWnCshsejNKU3kZQKCqHB5CWezL3p6qlZaE3VuPZKNRjvmdXjodFwSH67Aq_d1ivKWgyJagxNB2cwgcqI0azmQXmhKtW-S6jxAGUol1gagwf8uJRJ_MhHXG9BeMeu4f8FTOVuW31jHVQ63Guk28sqR_EgU2IoPxHCFmvJqHJnfA-zgBX_dRqaX5FEkX1fZZhcxz0jFBphsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء أربيل تعج بأصوات الطيران الحربي والمسير الإنتحاري في هذه الأثناء</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/naya_foriraq/85812" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85811">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d05b791a.mp4?token=WPSp9jgJp5XPPP6ZNqbB6gOtHFX9n6uSapMQ5Ihr1nq7nsZOKXYRa5BQWm8GGcoXrOweY6s0EnIi6q-zXOwXkmgCybNFZGxEpnHgyKhZBi1R4BgVDHNNaVpPaO96qv_FMhD6HprPPfgKYQ2EjDYh8lrN4ZWB5PbWa118PnMfQg8Tbt9cRXYhEvf53WjQv8A_0bc1s1sBGXG8Mt20PceMABZDDU6uq4ONAGkn6fHbwcAUGq2Mjf6OigX0EfTqwuThzOuH3JxGLl8x4vTaTwVuNSK0TaONvW1g9zzifyuhiUEOlK2y-QEMCY0Lx944OUp2CBc9ldYc_R0-oAD3PAsioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d05b791a.mp4?token=WPSp9jgJp5XPPP6ZNqbB6gOtHFX9n6uSapMQ5Ihr1nq7nsZOKXYRa5BQWm8GGcoXrOweY6s0EnIi6q-zXOwXkmgCybNFZGxEpnHgyKhZBi1R4BgVDHNNaVpPaO96qv_FMhD6HprPPfgKYQ2EjDYh8lrN4ZWB5PbWa118PnMfQg8Tbt9cRXYhEvf53WjQv8A_0bc1s1sBGXG8Mt20PceMABZDDU6uq4ONAGkn6fHbwcAUGq2Mjf6OigX0EfTqwuThzOuH3JxGLl8x4vTaTwVuNSK0TaONvW1g9zzifyuhiUEOlK2y-QEMCY0Lx944OUp2CBc9ldYc_R0-oAD3PAsioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاقات دفاعية في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/naya_foriraq/85811" target="_blank">📅 00:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85810">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c719c4ee4c.mp4?token=tNnL8O_N3ZiODH07pNTB7fzJmEwkjlOqRUD4-2NHdS7GqOLhGPhheDMIE3iZMCvUwyVpRIyta1w87cCiOIs_yQgneNMRlJ9P9SoKkVUHJzs8ki_oddEtjiHpRYMJqmcw7g4YhpFfm2StCzktkRtF7BmPM--zmOIk5mE0FRGKpByWgFCxtRxzp11jPRIgDu8kXED7WgPBXQjtRI0hsay5MpJIaZejwqO8uH0rRGCkxyhKgES7qOzbSguJfu4KI0jNuZF8K7DFigG5Lw-E1WZMaNmkXonYbVtGGVE_PUGF_Jv05M7PJvAC_lAP6UVYleS4aQFHcxMB85tO_v0WuNMA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c719c4ee4c.mp4?token=tNnL8O_N3ZiODH07pNTB7fzJmEwkjlOqRUD4-2NHdS7GqOLhGPhheDMIE3iZMCvUwyVpRIyta1w87cCiOIs_yQgneNMRlJ9P9SoKkVUHJzs8ki_oddEtjiHpRYMJqmcw7g4YhpFfm2StCzktkRtF7BmPM--zmOIk5mE0FRGKpByWgFCxtRxzp11jPRIgDu8kXED7WgPBXQjtRI0hsay5MpJIaZejwqO8uH0rRGCkxyhKgES7qOzbSguJfu4KI0jNuZF8K7DFigG5Lw-E1WZMaNmkXonYbVtGGVE_PUGF_Jv05M7PJvAC_lAP6UVYleS4aQFHcxMB85tO_v0WuNMA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء أربيل تعج بأصوات الطيران الحربي والمسير الإنتحاري في هذه الأثناء</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/naya_foriraq/85810" target="_blank">📅 00:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85809">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/065589ca73.mp4?token=JJ1kjfQUoH1x2uc1emWvgQSIPJ26XN78DTcYkLJ17btDQvnJzRJjXYAoO6lurkwrHbRDd3fjnr2hpsrNuTRFYGkRc7kAX6xe6cSkXL5nHlN0UozeOwk8JVL3mVcdXZki5LaNtiyd86LQuQfZMsGbNwuvOrHGHSpcoClYXN6pXGBDwQ9BiU6Qmd4wvm0GReFH9uxKQ1IS3yHJ1RVkCcpftKBYsEvO2voNZIf1kQBOwcT7FCePTRkHxZNcejlffDOZajZGIN2tWj9Kh3mf-KEE5P0KTGcnGiUzzmRQWx7R3hofbA7LFRTeUVDQDU3zfRAcd5qcL5Z3REWaxH_W9s-wyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/065589ca73.mp4?token=JJ1kjfQUoH1x2uc1emWvgQSIPJ26XN78DTcYkLJ17btDQvnJzRJjXYAoO6lurkwrHbRDd3fjnr2hpsrNuTRFYGkRc7kAX6xe6cSkXL5nHlN0UozeOwk8JVL3mVcdXZki5LaNtiyd86LQuQfZMsGbNwuvOrHGHSpcoClYXN6pXGBDwQ9BiU6Qmd4wvm0GReFH9uxKQ1IS3yHJ1RVkCcpftKBYsEvO2voNZIf1kQBOwcT7FCePTRkHxZNcejlffDOZajZGIN2tWj9Kh3mf-KEE5P0KTGcnGiUzzmRQWx7R3hofbA7LFRTeUVDQDU3zfRAcd5qcL5Z3REWaxH_W9s-wyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اربيل لحظة الاستهداف مقرات احزاب المعارضة</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/naya_foriraq/85809" target="_blank">📅 00:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85808">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8944cda6.mp4?token=rHzIpn7OIlI--SBAJeeMPgE45QFsOLSqo6b0w3iboFw3fpKfxoQJ9ny1vuJhjfpSHFcE27ffCa5EXI2Gq1fQHsylLDvO1nVEw7XUW5SIki_s9rh_YfecU-v0ysn_ib--TLQXSDpPwzumQEmL9LEg4ZMuBzi9Ok7JtLqx5_wAIUJtCnPGlVIXTcwqCzBbHnum4KrfYffZrkBFRZFhpIKFqcSDykvkbMtvP0YRVLppDzPEqPY0wZ-DvIKrzLliqWDkbWsZaJ4W4qplN7q_nnW8MOqzD6CDWFiFT5lZJfWkoIS_nYU5aVjrHHlGpaYqjbHdlI2qoSNnpC4Zva3Un98pBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8944cda6.mp4?token=rHzIpn7OIlI--SBAJeeMPgE45QFsOLSqo6b0w3iboFw3fpKfxoQJ9ny1vuJhjfpSHFcE27ffCa5EXI2Gq1fQHsylLDvO1nVEw7XUW5SIki_s9rh_YfecU-v0ysn_ib--TLQXSDpPwzumQEmL9LEg4ZMuBzi9Ok7JtLqx5_wAIUJtCnPGlVIXTcwqCzBbHnum4KrfYffZrkBFRZFhpIKFqcSDykvkbMtvP0YRVLppDzPEqPY0wZ-DvIKrzLliqWDkbWsZaJ4W4qplN7q_nnW8MOqzD6CDWFiFT5lZJfWkoIS_nYU5aVjrHHlGpaYqjbHdlI2qoSNnpC4Zva3Un98pBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اربيل لحظة الاستهداف مقرات احزاب المعارضة</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/naya_foriraq/85808" target="_blank">📅 00:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85807">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الإطار التنسيقي:
عبرّ الاطار التنسيقي عن موقفه الثابت لدعم الجهات المختصة في محاربة الفساد وتعضيد جهود الحكومة في ملف حصر السلاح بيد الدولة.
وشدد الاطار التنسيقي  على رفضه المستمر لاستخدام اراضي الدول في الاعتداء على الدول الآخرى، واغراق الجميع في صراع لا يخدم اي من الاطراف.</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/naya_foriraq/85807" target="_blank">📅 00:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85806">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
انباء متداولة عن استهداف حقل كورومو في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/naya_foriraq/85806" target="_blank">📅 00:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85805">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
🇺🇸
نشرت صحيفة أميركية تقريرًا يستعرض آثار العدوان الأميركي على إيران والتداعيات الاقتصادية التي انعكست على دول العالم بدءًا من ارتفاع أسعار الوقود والطاقة وصولًا إلى زيادة أسعار المواد الغذائية وسلاسل الإمداد.</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/85805" target="_blank">📅 00:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85804">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef69381f74.mp4?token=Ok_HM_wzAqgNUbZ8uhLNpwKCo3r38NRiX4Sqi0COBFO33T0RrD3zVmCJHDDRB8JcE6SZqd766jEWbAtJTU6QNLEeaBS99D3z7SwbONYdeEuZO8mv5xLJD27-494OnGQrTVL1jZg-FCPAAkNXJebhEJ26Z5FijWQ_EXS-kZDdveQSVJQCMKGbt5_6ukVRUerG_u45A5hS_GnELOw-hHhKRnJLXI7yxbH_4wItET12ux1rKobDab2_oawT1GXioOzCsOMVLZk7GmOF5pLWtujFag8FwXv90v2UJkOA3OgleJGYG7hhtmyhL0eL0bpUUza8obi8JU98AQCegbnAL1MeHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef69381f74.mp4?token=Ok_HM_wzAqgNUbZ8uhLNpwKCo3r38NRiX4Sqi0COBFO33T0RrD3zVmCJHDDRB8JcE6SZqd766jEWbAtJTU6QNLEeaBS99D3z7SwbONYdeEuZO8mv5xLJD27-494OnGQrTVL1jZg-FCPAAkNXJebhEJ26Z5FijWQ_EXS-kZDdveQSVJQCMKGbt5_6ukVRUerG_u45A5hS_GnELOw-hHhKRnJLXI7yxbH_4wItET12ux1rKobDab2_oawT1GXioOzCsOMVLZk7GmOF5pLWtujFag8FwXv90v2UJkOA3OgleJGYG7hhtmyhL0eL0bpUUza8obi8JU98AQCegbnAL1MeHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
What if they come back ?</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/85804" target="_blank">📅 23:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85803">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالمقاومة الاسلامية في العراق</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-JdND6PhuZO37S77yfyor8RFpSqOdUnA6lE7pY--65GqIQjNyLGwZGWULqV3oDrUvQuZJvGOAB7cOkeCgCdBxDuO1cEu-LdfN7415_bOOCSsQCqEDnhk7OQ4D5rVVoss1bg_PBID-QG0lD1IG6DusuzMDefFeT0F6WN_nwqqU8JMMP_mAtUomePQ_5NH0aOUgoTtAqfqnMiHgO-rtvhNwgtX-YSXV6BDrl3Y3AxY0hAgpm6ZShW6PFl0wR7ilmvmyDaUOqgYal0kKgg4BVBw94yCnCR41BZCS_Y-LPDZWLYm59L_RQxjvheY2DHsG-Ck-v6vkR6-f6tLZ5U-w8TWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
(إِنَّمَا يَفْتَرِي الْكَذِبَ الَّذِينَ لَا يُؤْمِنُونَ بِآيَاتِ اللَّهِ ۖ وَأُولَٰئِكَ هُمُ الْكَاذِبُونَ)
بينما يواصل الكيان السعودي رمي الاتهامات نحو العراق، زاعماً أنه المصدر لقصف منشآته البترولية في الشرقية والرياض، فإن هذا الادعاء لا يزيدنا إلا يقيناً بأن العداء للعراق وشعبه سمة لاصقة بهذا النظام.
إن هذه التخرصات ما هي إلا محاولة لتبرير العجز عن الرد على الضربات اليمنية الموجعة التي طالت عمق بُناهم التحتية، خوفاً من طبيعة الرد اليمني القادم.
إننا في المقاومة الإسلامية نُوجه للنظام السعودي تحذيراً واضحاً، نُعلن فيه أن أي فعل سعودي أحمق سيُجابه بردٍّ قاسٍ، يجعلهم يعضون على أصابع الندم.
ونقول لهم، وبكل وضوح: إن كان فيكم رجل رشيد، فأنتم أحوج ما تكونون اليوم إلى رفع الحصار الظالم عن الشعب اليمني، بدلاً من توجيه الاتهامات يميناً وشمالاً، لتبرروا بها فشلكم، وتغطوا بها على جرائمكم.
المقاومة الإسلامية في العراق
27 تموز 2026</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/85803" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85802">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/85802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/naya_foriraq/85802" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85801">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1Gl7Cnmmju1nz52tPNIftPKvVUBAXHA0DbiXDIhBNWM85_csLgywvLuU_4WPwL8RZLqUprSw-AykLx6vlPyp2S1mPYkrV7Opbyl5Qi8bE2PQ4HREF4DWbQVKq6PvckWNnMknhrckPbkZ2IU5_s46RYJK9-RvkRak47lSubW7t1BHOeKqLR-s8qg-4ki1m1JWVhDKWMvkvOBx-tWwuaD887gs7V8PO0ux6Q-1oA-x8WM_PUYiJ5nhi6--YNfFscX2b6jnr8HdtwI8TWEt5QPJdMiKjKMV_YzKqhXr8-n_3glDybam3uUjOh96blBBigL2I7jYhE_DRiSomGpU4Ithw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط طائرة مسيرة أمريكية قرب سد حديثة</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/85801" target="_blank">📅 23:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85800">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سقوط طائرة مسيرة أمريكية قرب سد حديثة</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85800" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85799">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85799" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85798">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed1a8163b.mp4?token=n0I_Ii4jCI0MR1qZAowEOgfVIphkVTeZ6xTsAQGIxs2YYSsFt7cYGElyWDOdfuSqqLbOMysNTiWF7H4k51-4WsfnnJSc7xw8pRHUdZlVzEJ1G4cr22FI6Bk6Fdae27-BcXds7Z1ta3UWZMZZXoOmIEvurjlGYNH2v9xQmhf4n_yVAFcDRx2AFX3zB_U0_Z9_ud8-rWUk5rkgBY42oFiBht8d5mNbRh8-5L8g8ebpA25ID0pL88cdAX7y4qOORssqGbJyonaYQBYZRZL7_4NOBjT_LAX-LDzaFzTvqv2Qn0Z3Dg-WB37SkI5VlUPFsDjdcKbia9JCzsUl6HAA1W1xbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed1a8163b.mp4?token=n0I_Ii4jCI0MR1qZAowEOgfVIphkVTeZ6xTsAQGIxs2YYSsFt7cYGElyWDOdfuSqqLbOMysNTiWF7H4k51-4WsfnnJSc7xw8pRHUdZlVzEJ1G4cr22FI6Bk6Fdae27-BcXds7Z1ta3UWZMZZXoOmIEvurjlGYNH2v9xQmhf4n_yVAFcDRx2AFX3zB_U0_Z9_ud8-rWUk5rkgBY42oFiBht8d5mNbRh8-5L8g8ebpA25ID0pL88cdAX7y4qOORssqGbJyonaYQBYZRZL7_4NOBjT_LAX-LDzaFzTvqv2Qn0Z3Dg-WB37SkI5VlUPFsDjdcKbia9JCzsUl6HAA1W1xbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: لا يمكنك رشوهم. يجب علي هزيمتهم،ونحن نهزمهم بشدة.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/85798" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85797">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98851fe969.mp4?token=C8qoFBYmo7_PJhcmtiqJ8-F1lXxXDhTv3BSDF6ArZEvCQNFjPCprd4WeNpvOZ-9wUhujeGx-yCCLQEcs75je06FCeg4dujNSeWQiIleyYIlYy5m9srThfPWUnJUDdK_-ErmopsvJ4LjCUyww9z6T_IyA8IfWe3j1eqbg2427_ordlEAaxGwzWTWAZ4v8pNHcki434JLfrh9og9BTKE5rj-U6WjMGDEUGI6U4LkB2qoEprrmDoKc3tDSDAtLZzzt3KqszFyPcQ26SFKW68YJpRI_cE9h6ERBHEFWfYtQuac9rtfOM1lS1SrL3FlessLNkhdJUiOLuNxOjhqMxfbN8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98851fe969.mp4?token=C8qoFBYmo7_PJhcmtiqJ8-F1lXxXDhTv3BSDF6ArZEvCQNFjPCprd4WeNpvOZ-9wUhujeGx-yCCLQEcs75je06FCeg4dujNSeWQiIleyYIlYy5m9srThfPWUnJUDdK_-ErmopsvJ4LjCUyww9z6T_IyA8IfWe3j1eqbg2427_ordlEAaxGwzWTWAZ4v8pNHcki434JLfrh9og9BTKE5rj-U6WjMGDEUGI6U4LkB2qoEprrmDoKc3tDSDAtLZzzt3KqszFyPcQ26SFKW68YJpRI_cE9h6ERBHEFWfYtQuac9rtfOM1lS1SrL3FlessLNkhdJUiOLuNxOjhqMxfbN8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏أحدهم يصرخ في وجه ترامب قائلاً: "حامي المتحرشين بالأطفال!"</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/85797" target="_blank">📅 23:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85796">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07efc12575.mp4?token=gpJU_teaQGgrVB4_4doPjpiIYQCrDMVYMkDMBAKX-Fir56Z0WSuIZ1aecpfHhGyqKIR8J-hKP4Yf9f3aIgL4X1oBRERL6MAHQag6TozOgJD04_LXajaHzmLZePmsPLEnX6k6ppyWR9wqU6N0Qp-oZv48DOjsXnm5ArDu4iOEAqKd1wHbLFQ0UNF3HA927jIkFN7d1egWnGNITujp9_qPiGKSFkX-evd_WA1yc6iBrVihYLDxb8EcAgVG0ydsEDVtepdDI1TaO_ZbhZznANycThM-wxCQkYyWQkiDDjiNH97cvxNYOh3ajnTAavw2muaDKHprWoQHKj7yVasgHtrLwRA3Cf9CRf-GnXEKbrrbFKboaaFLksxIyV2rUbcJEnusHKCjTf_Dl-tIcht36Xw_Jap1zA3g07NaROz4uRIGfXd986aF2kaLzFUK6teFg6yd49BJYr9-ZUNu8oA2VgqyvZrmU1lHSbJ-WQoUX9h4YaeDF7e46WJ4E_3viijXbvMQ7oOsrHz63cgBi93pi8cerq6wPPPXJmsl2VxYLu1Vm9GihdKwLYPVPsG8VKMk97eZyFplA4OBTtXh227_7_HRE2WoxSuIxKEigTtq01Ly2Rz9f0FR0fNQ-LUtjPkik7oKn2mppf6fxckl077nGEUE05orq-9ulTpU2eTlUvZ5YxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07efc12575.mp4?token=gpJU_teaQGgrVB4_4doPjpiIYQCrDMVYMkDMBAKX-Fir56Z0WSuIZ1aecpfHhGyqKIR8J-hKP4Yf9f3aIgL4X1oBRERL6MAHQag6TozOgJD04_LXajaHzmLZePmsPLEnX6k6ppyWR9wqU6N0Qp-oZv48DOjsXnm5ArDu4iOEAqKd1wHbLFQ0UNF3HA927jIkFN7d1egWnGNITujp9_qPiGKSFkX-evd_WA1yc6iBrVihYLDxb8EcAgVG0ydsEDVtepdDI1TaO_ZbhZznANycThM-wxCQkYyWQkiDDjiNH97cvxNYOh3ajnTAavw2muaDKHprWoQHKj7yVasgHtrLwRA3Cf9CRf-GnXEKbrrbFKboaaFLksxIyV2rUbcJEnusHKCjTf_Dl-tIcht36Xw_Jap1zA3g07NaROz4uRIGfXd986aF2kaLzFUK6teFg6yd49BJYr9-ZUNu8oA2VgqyvZrmU1lHSbJ-WQoUX9h4YaeDF7e46WJ4E_3viijXbvMQ7oOsrHz63cgBi93pi8cerq6wPPPXJmsl2VxYLu1Vm9GihdKwLYPVPsG8VKMk97eZyFplA4OBTtXh227_7_HRE2WoxSuIxKEigTtq01Ly2Rz9f0FR0fNQ-LUtjPkik7oKn2mppf6fxckl077nGEUE05orq-9ulTpU2eTlUvZ5YxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏أحدهم يصرخ في وجه ترامب قائلاً: "حامي المتحرشين بالأطفال!"</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/85796" target="_blank">📅 22:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85795">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDPsfFNZ42c9-ehC8zanI_JRou3994hKVcjd6RPWWrMR1dWVFieTxrr3lKO-mQ4BpN4FuCco56CSssqegJioV-f6HfxCgV_8EnSSai5UbggkCmLx0V-x5nR3vhH3_ualEJMI2JzoMT6BV6F9XgHAsAk57qyG-rhDIiE1sjsXcrk0yQEtwjqCkRiurGJZJ4ioin6FZNep2VQiY9pkEH34A7aRKVQFnlkayfCXkKT6IZfePbolUTY0FspAs3LJtQCzhVoHOQDd1rCCAdF61zcHo3t-jZna3JeGuBga2K7gUneRMuPwRfP_5ZeJP_jAYi8Z9FxEHciYoDhHQLbaoxS5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ارتفعت صور شهداء ميناب في شوارع مدينة النجف الأشرف، قرب مرقد الإمام علي (ع).</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/85795" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85794">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b09d4680.mp4?token=A_RIYJtyY3NikOtQ6nNpLaDk_CSorennA7N8kWARLkidmUanhFQNS-P5Zqyc2KM2Q4jXeWiSDpDfFRET_mpg8gpMHthJXp9okW8AiVy3cvEDSZc17-_udWt4D0iA3OtTN-mxXfCD_snxpDA63vADW9NhsxfGlu9Z0bZnjhAVH08uHQ_ZIDdUYz4nsxtiNR_5xOzL1ukWEdhje8TLu-UwT5pvInu4pdU_6Fx5VQEUR81HkjUszHGVnhO1FWBYuVOcDiK2qbUsAR44yuCa4od4EVKwcwBWrBSPBoceivm-PX54THoCkra3DJOLiYvV6kPOS2pugPyX7bacNRAvVZRfDIiGLHhBFgfJmYMzACTTjOZ-DjcKV-Z5g0GeoglS2UPpXNB5BqYhdDihSMQQlVp8T8gFzChXlnIwOs7KySqi3xtOf8pA5278xXxWpVtGhxVK_H0Sg0gcfDSWvQXQHcNdt6zI0M-f6E29KVsNDVwauqw6J7yA4jvkmlkFt4BHIeWGHNgH-lvDyI6mEJuTgGsSRSZAG7osbdvMrMDvEKVWdToko7hojqa6sropBZwXqXe6d-Uyk4UeQCHU_007XTmQIqhts_fbhMOaHGymDM3MkRyUFcaNan50Elw-mXLZl_GuKHlSkEpt31aAK9hB-HAC78zKojGQMtNliythb10TmTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b09d4680.mp4?token=A_RIYJtyY3NikOtQ6nNpLaDk_CSorennA7N8kWARLkidmUanhFQNS-P5Zqyc2KM2Q4jXeWiSDpDfFRET_mpg8gpMHthJXp9okW8AiVy3cvEDSZc17-_udWt4D0iA3OtTN-mxXfCD_snxpDA63vADW9NhsxfGlu9Z0bZnjhAVH08uHQ_ZIDdUYz4nsxtiNR_5xOzL1ukWEdhje8TLu-UwT5pvInu4pdU_6Fx5VQEUR81HkjUszHGVnhO1FWBYuVOcDiK2qbUsAR44yuCa4od4EVKwcwBWrBSPBoceivm-PX54THoCkra3DJOLiYvV6kPOS2pugPyX7bacNRAvVZRfDIiGLHhBFgfJmYMzACTTjOZ-DjcKV-Z5g0GeoglS2UPpXNB5BqYhdDihSMQQlVp8T8gFzChXlnIwOs7KySqi3xtOf8pA5278xXxWpVtGhxVK_H0Sg0gcfDSWvQXQHcNdt6zI0M-f6E29KVsNDVwauqw6J7yA4jvkmlkFt4BHIeWGHNgH-lvDyI6mEJuTgGsSRSZAG7osbdvMrMDvEKVWdToko7hojqa6sropBZwXqXe6d-Uyk4UeQCHU_007XTmQIqhts_fbhMOaHGymDM3MkRyUFcaNan50Elw-mXLZl_GuKHlSkEpt31aAK9hB-HAC78zKojGQMtNliythb10TmTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🏴‍☠️
🇮🇶
خلايا اوكرانية تنفذ هجمات في العراق وتُنسب للفصائل.. مستشار الأمني القومي يكشف سراً "لم يسمعه العراقيون" من قبل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85794" target="_blank">📅 22:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85793">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
مقر خاتم الانبياء المركزي:
إن الولايات المتحدة، في استمرارها للشر وانعدام الأمن في المنطقة، وعقب فرضها الحصار البحري غير القانوني على إيران، هددت السفن الإيرانية، والسفن التجارية، وناقلات النفط في المياه الساحلية والإقليمية لبلادنا على مدى الأيام الثلاثة الماضية.
نحذر من أن هذا العمل الأمريكي يُعد امتدادًا للحرب في المنطقة، وكما أثبتت القوات المسلحة للجمهورية الإسلامية الإيرانية على أرض الواقع، فإنها لن تتهاون مع أي تهديد أو شر من جيشها الإرهابي، وستتعامل معه بكل حزم.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85793" target="_blank">📅 22:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85792">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
🇮🇱
سفارة الاحتلال الاميركي في الضفة الغربية تصدر انذار بعدم السفر الى الضفة الغربية نتيجة التصعيد الاخير.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85792" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85791">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f416d3226.mp4?token=DbixzG-olkWWzTvMaLeCJ7-LdDH3TmP8HuArlZPXpO0tnQfemsVyorIPngLqwwsh3MWnv0S_H22-jc6-057luksia_8Du7sRZmGmcvL87dz8zSx_upt-C8Xi1H_F2MaGtWXU_pCClPSZlJFM8NfhmwDelVwzmTkpRkV9sicsQassVce3bwlhDctLaPcv7ExAuV54a51o77KHINLnjHjmAeDQ9p2-bR8ldfTyS_0Qmfp7i3cKVS_7XB5943xnVjLNsGaUS-gv1rxUXDaRmkTntWMqMyB4dY6AmCh0dtIuqjBF_AkQqrVc2PYwguO2MgT3vU7qiO2AtemgylU4o0Y3X4wQkZFa6_BxzrwROOybWcTI7Wh0NGNyr9yzvEvEqi9aO3H03IlajtHQCY8obWc9cROcNx1n2o8Koi7wOJGVQXY8EMMreq_a_ZlBXncUT4jAYMqyVE48qy3pva-PEuLGLEjJDpT0IBNany38MuCfDl3SEf3PzWTh43JoFyKQwWtNDA5L48RuyU5DIu32aKHu8D5Yk7Kw4fJfsgiGPSJx81S9sZecIvI0b92NnV4xxUTxrSkfRwgZL6Ft7OHhOkgt6fCcDKIsYhhvKhy74hLednNvHvpj4Lk64SV3cVf4MZ8BHKFVuVeu5E8TYikBTV7t_Lly2M3yjcC1D6B-qPPACcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f416d3226.mp4?token=DbixzG-olkWWzTvMaLeCJ7-LdDH3TmP8HuArlZPXpO0tnQfemsVyorIPngLqwwsh3MWnv0S_H22-jc6-057luksia_8Du7sRZmGmcvL87dz8zSx_upt-C8Xi1H_F2MaGtWXU_pCClPSZlJFM8NfhmwDelVwzmTkpRkV9sicsQassVce3bwlhDctLaPcv7ExAuV54a51o77KHINLnjHjmAeDQ9p2-bR8ldfTyS_0Qmfp7i3cKVS_7XB5943xnVjLNsGaUS-gv1rxUXDaRmkTntWMqMyB4dY6AmCh0dtIuqjBF_AkQqrVc2PYwguO2MgT3vU7qiO2AtemgylU4o0Y3X4wQkZFa6_BxzrwROOybWcTI7Wh0NGNyr9yzvEvEqi9aO3H03IlajtHQCY8obWc9cROcNx1n2o8Koi7wOJGVQXY8EMMreq_a_ZlBXncUT4jAYMqyVE48qy3pva-PEuLGLEjJDpT0IBNany38MuCfDl3SEf3PzWTh43JoFyKQwWtNDA5L48RuyU5DIu32aKHu8D5Yk7Kw4fJfsgiGPSJx81S9sZecIvI0b92NnV4xxUTxrSkfRwgZL6Ft7OHhOkgt6fCcDKIsYhhvKhy74hLednNvHvpj4Lk64SV3cVf4MZ8BHKFVuVeu5E8TYikBTV7t_Lly2M3yjcC1D6B-qPPACcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
انصار الله:
بيرقدار أكنجي.. سقط الرهان وبقي الحطام.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85791" target="_blank">📅 21:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85790">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
🇸🇦
رئيس الوزراء العراقي يوجّه الجهات الأمنية المختصة بفتح تحقيق بشأن الادعاءات المتعلقة بانطلاق طائرات مسيّرة من الأراضي العراقية لاستهداف السعودية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85790" target="_blank">📅 21:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85789">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇸🇦
بيانات ويندوارد البحرية:
تقدر الخسائر السعودية من هرمز وإغلاق باب المندب بنحو 504 مليون دولار، وهو ما يمثل 90٪ من عائدات النفط.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85789" target="_blank">📅 20:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85787">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b04273ad0.mp4?token=UdGctU8FbC3_5OCGqBo5l4u8TGS4x38lyzhSQkox0pzDT-ZR5nm_mQymBvp-kHxuuj28XT9XXKuFqLQWJk-BVT-hpReQiTipIx3Y_kwS5pyLERGFxG3G7TNLctcub1eHpuxcZG8Rtq96ywVamqki6k1Qkhtzvw1J-OxQXBsTAPkEnUGMZsITDzDgD-YcwLM6LMRdjtx7k9MjkiRuIsemcjBTJzxRwuYoNbj-TOZ-vZkCdUf-WqX5Nv1CEtIGYE9KAkJF1rRcxoKw4DY4n0UeWh64dMwLDizhSA1wJa2rE9ev7JeI-tQvVF3ETKm75CBVAwrIt-o93ZKikKNYFlWzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b04273ad0.mp4?token=UdGctU8FbC3_5OCGqBo5l4u8TGS4x38lyzhSQkox0pzDT-ZR5nm_mQymBvp-kHxuuj28XT9XXKuFqLQWJk-BVT-hpReQiTipIx3Y_kwS5pyLERGFxG3G7TNLctcub1eHpuxcZG8Rtq96ywVamqki6k1Qkhtzvw1J-OxQXBsTAPkEnUGMZsITDzDgD-YcwLM6LMRdjtx7k9MjkiRuIsemcjBTJzxRwuYoNbj-TOZ-vZkCdUf-WqX5Nv1CEtIGYE9KAkJF1rRcxoKw4DY4n0UeWh64dMwLDizhSA1wJa2rE9ev7JeI-tQvVF3ETKm75CBVAwrIt-o93ZKikKNYFlWzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الهجوم الجديد الذي استهدف مقرات المعارضة الايرانية الكردية في قضاء كوية ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85787" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85786">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27556c8a9a.mp4?token=lA9fk0eFUOwjxr-SsfBFzB5EM-W7X3Wc4e9p7TpwBm5Ehl2Oz5-Wz45ZfLCRT5YuCPdAgx1b1Mcjej5dSmlVkjyOd_iB99Uq4L5nCzO8HUQEAeSe0HQ8VP095fhHOKv0Ar8bgGvOyq42veiwI0JY91P-0D2gAIRHksfTmOI1PZlJC1iFwhd3SBkfJVaX67y1xCrs6czdpUehQvz_oVF8Pcl05wo12bOwDlDfAbjIhmdc6zzDlQ7zKpQvrUlO_8I5ItUUMxQnAxCmhcepcA64QlHVv7YlIm8yZtAmTH20AjGDKn8kIehJwgDH9-k1fqYizqJXzRdf7jnx1n2LeTH8Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27556c8a9a.mp4?token=lA9fk0eFUOwjxr-SsfBFzB5EM-W7X3Wc4e9p7TpwBm5Ehl2Oz5-Wz45ZfLCRT5YuCPdAgx1b1Mcjej5dSmlVkjyOd_iB99Uq4L5nCzO8HUQEAeSe0HQ8VP095fhHOKv0Ar8bgGvOyq42veiwI0JY91P-0D2gAIRHksfTmOI1PZlJC1iFwhd3SBkfJVaX67y1xCrs6czdpUehQvz_oVF8Pcl05wo12bOwDlDfAbjIhmdc6zzDlQ7zKpQvrUlO_8I5ItUUMxQnAxCmhcepcA64QlHVv7YlIm8yZtAmTH20AjGDKn8kIehJwgDH9-k1fqYizqJXzRdf7jnx1n2LeTH8Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مواطن عربي يوثق لحظات من التوتر والارتباك داخل الطائرة أثناء عبورها الأجواء الإيرانية وتحديدًا فوق مضيق هرمز.
عبالك راكب MQ9 مو طائرة مدنية
😏</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85786" target="_blank">📅 20:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85785">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇸🇾
سوريا تدين محاولة استهداف منشآت نفطية في السعودية عبر طائرات مسيّرة اطلقت من العراق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85785" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85784">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssfW_7HmvK05-rW5td4CngYhfUJ29vm1yNP_tWiNRF1EY6i_o_o43m-MK_8F5IgAQF-pigzamA9fUj4pjuNg4YvcPvj4-Svu6OQgvPpABUpaoqfDld5JRqlFVw-2bHSuaAapTSJFiAOTnOOr1OzRtNhxX0Pf28RucEaw8tpyfhpQC7FXLbzNUMLrQ-wnQUZ_30X52Zbm_X9la7jWkMWZ0qvXUGahfbBnxkzqbt6NyU6uqJ8oxwxuBwuccZ1PhVVlathwntX4o2dTlrdMpQrUmOdPzuvgy2tFB59F_o2ihaiWl2wKtu8PbJSn8KdrPv9jaV_N9mJ7FSXuOBwRawtiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇺🇸
ترامب إن هناك "فرصة جيدة لحدوث شيء جيد" مع إيران، ولكن إذا لم يطرأ أي تقدم "فيمكننا العودة إلى فعل ما كنا نفعله قبل يومين".</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85784" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85783">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d98c88fdce.mp4?token=HYGWQN0j3G9EHbf_V57YDwVqpu13rmwLBFvIg0o_7qsznlvbqNurjFOC5jOXEjuJsIFbhc9XUYT1Ch11O969PswgHbu-uvoeiZN5yUxOQM-hOBr0RY4L0h-_3QMnTrLz1lRMXeBvGefLeQAODa6AiK-XriDPqIidVGg0xUi-HESfvjlZaH71P67j1FQkuivtzDjdjRIEdc8eSxm4uXNNc-uYomjPrpLG6bsscraGi-0Lpb8LcH2MlveXd4kejDrB4wkU3qkUAIXpGnF7CaawGNPluiobkKWnK5cRzmP5OxnZgAbdleiz9lz_vy8bpaGAxLGuBnWDlq6hZ3Yrdb54dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d98c88fdce.mp4?token=HYGWQN0j3G9EHbf_V57YDwVqpu13rmwLBFvIg0o_7qsznlvbqNurjFOC5jOXEjuJsIFbhc9XUYT1Ch11O969PswgHbu-uvoeiZN5yUxOQM-hOBr0RY4L0h-_3QMnTrLz1lRMXeBvGefLeQAODa6AiK-XriDPqIidVGg0xUi-HESfvjlZaH71P67j1FQkuivtzDjdjRIEdc8eSxm4uXNNc-uYomjPrpLG6bsscraGi-0Lpb8LcH2MlveXd4kejDrB4wkU3qkUAIXpGnF7CaawGNPluiobkKWnK5cRzmP5OxnZgAbdleiz9lz_vy8bpaGAxLGuBnWDlq6hZ3Yrdb54dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: يقول زيلينسكي إن روسيا تزود إيران بصور الأقمار الصناعية للقواعد الأمريكية في الخليج لمساعدتها في تحديد الأهداف. ما الذي يمكنك فعله حيال ذلك؟
🇺🇸
‏ترامب: سنكتشف ما إذا كان ذلك صحيحاً. سأسأل بوتين عن الأمر. لم يكن له تأثير كبير.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85783" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85782">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78581c857c.mp4?token=r9Gyaf4EudRNB1m-YxMB26L5XxmAyK-6jMHcu0VzPri76rkpI2UMjQSWegbc72OSsxsf5tXp4KiE6zpFXCRtNPK3Kboh1jVWFL7mOB78V043K_VRy1Q85aLP9LFaMblgdblw2ot1pvOp_7q9TnW_1APut0yFLANzQScSUSIs60vQwMeVQ9riKWusi_e4pSIu4hNtSf7V194k7SsKMhq57OjHEf1xIaqeh9pVAR6VkYBbJl1zMmT_p47wG3u5lpuKy807qbeWxe0ODZqDBeYl-dnF7hdMUGIjyNIEaGifr3HlqgPSNBgF0anPRATLsyA3Pesb-9FbSGHlYxSnE7fvog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78581c857c.mp4?token=r9Gyaf4EudRNB1m-YxMB26L5XxmAyK-6jMHcu0VzPri76rkpI2UMjQSWegbc72OSsxsf5tXp4KiE6zpFXCRtNPK3Kboh1jVWFL7mOB78V043K_VRy1Q85aLP9LFaMblgdblw2ot1pvOp_7q9TnW_1APut0yFLANzQScSUSIs60vQwMeVQ9riKWusi_e4pSIu4hNtSf7V194k7SsKMhq57OjHEf1xIaqeh9pVAR6VkYBbJl1zMmT_p47wG3u5lpuKy807qbeWxe0ODZqDBeYl-dnF7hdMUGIjyNIEaGifr3HlqgPSNBgF0anPRATLsyA3Pesb-9FbSGHlYxSnE7fvog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: هل تتفق أنت ونتنياهو على موقف واحد بشأن إيران؟
🇺🇸
‏ترامب: لدينا اختلاف بسيط، لكننا متقاربون جداً</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85782" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85781">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75da70ebb2.mp4?token=W35W68UUpjgcCnxZmsOM7ubPs3kqCk-rDYebZiwyR10LQCasntPsICqB5JeT8SKIZA_sa_Pi_lEgKOORqS-Uy3-gTIzlwWpVqOiFwVs0dG9LA-aB0L9_46yjBVW4LhCbSExr0pPX_DNzZ9CDJlw1FLayRJUrl90w_10f98rEl0EO-RrVKxYVoE_F3HZeffrBTefaIM6yNt7gKUefsgjF9ibDZ18w-RH5h9TIcaCCvAhPfTljl9XL9Zh0Ox_GixT8MOYh6mXJ5Dja0uu94t7DT1iICDeBYuh1XhG07DtOKif2KZAoKbN8mTiNyLf2yO0RtCIKCYlDpnxhpfIdlrBXJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75da70ebb2.mp4?token=W35W68UUpjgcCnxZmsOM7ubPs3kqCk-rDYebZiwyR10LQCasntPsICqB5JeT8SKIZA_sa_Pi_lEgKOORqS-Uy3-gTIzlwWpVqOiFwVs0dG9LA-aB0L9_46yjBVW4LhCbSExr0pPX_DNzZ9CDJlw1FLayRJUrl90w_10f98rEl0EO-RrVKxYVoE_F3HZeffrBTefaIM6yNt7gKUefsgjF9ibDZ18w-RH5h9TIcaCCvAhPfTljl9XL9Zh0Ox_GixT8MOYh6mXJ5Dja0uu94t7DT1iICDeBYuh1XhG07DtOKif2KZAoKbN8mTiNyLf2yO0RtCIKCYlDpnxhpfIdlrBXJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏المراسل: هل أنت قلق بشأن مخزونات الأسلحة؟
🇺🇸
‏ترامب: بالنسبة لبعض الأمور الأكثر تعقيداً، نود بالتأكيد الحصول على المزيد. لقد كشف بايدن الكثير منها.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85781" target="_blank">📅 20:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85780">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fffac8ab.mp4?token=WgKSNNuGAKco1kuyJaMOGpsYdm90lbPR5hbmCfJLDGzMt2KpeFztaP3dZFE_QdKdXCuSw0Jol596esr7oI6gyLvD5beZaSvSUP4bZQHBUyeebtVL3KVm93yCEyLd0iDFgb9kRmPwkposF5w6Lfg1G_hxVMxF5_mGpBA5E1V1MGPNqJnZcvbphwNkkNJzYibkr8sbozypapX0JSQS_RIC0QkiA0UDTmEvP9TLzDpiDVJjH7N_JtDCKzfvWScY3CBAuB9rzQnvZqf0KKFHp4-oYu5TOsN0GntITvPaB11h2kA0hO0ajx2c0YAziFuNiMFAQNi3SIriygkxn027pOEN7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fffac8ab.mp4?token=WgKSNNuGAKco1kuyJaMOGpsYdm90lbPR5hbmCfJLDGzMt2KpeFztaP3dZFE_QdKdXCuSw0Jol596esr7oI6gyLvD5beZaSvSUP4bZQHBUyeebtVL3KVm93yCEyLd0iDFgb9kRmPwkposF5w6Lfg1G_hxVMxF5_mGpBA5E1V1MGPNqJnZcvbphwNkkNJzYibkr8sbozypapX0JSQS_RIC0QkiA0UDTmEvP9TLzDpiDVJjH7N_JtDCKzfvWScY3CBAuB9rzQnvZqf0KKFHp4-oYu5TOsN0GntITvPaB11h2kA0hO0ajx2c0YAziFuNiMFAQNi3SIriygkxn027pOEN7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:   نتحدث حاليا مع إيران والمحادثات جيدة، لدينا الكثير من الذخيرة وأود الحصول على المزيد، وأنا ونتنياهو لدينا بعض الاختلافات بشأن إيران، ايضا سأسأل بوتين عما إذا كان يرسل صورًا التقطتها الأقمار الصناعية إلى إيران. سأسأل بوتين عن التكهنات بشأن مساعدة…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85780" target="_blank">📅 20:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85779">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
‏
ترامب
:
نتحدث حاليا مع إيران والمحادثات جيدة، لدينا الكثير من الذخيرة وأود الحصول على المزيد، وأنا ونتنياهو لدينا بعض الاختلافات بشأن إيران، ايضا سأسأل بوتين عما إذا كان يرسل صورًا التقطتها الأقمار الصناعية إلى إيران. سأسأل بوتين عن التكهنات بشأن مساعدة روسيا لإيران، وسنستخدم أموال إيران لدفع التعويضات عن الأضرار التي تسببوا بها، نحن لسنا متورطين مع الحوثيين في الوقت الحالي، ولكن إذا كانوا يمثلون مشكلة، فقد نضطر إلى التدخل.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85779" target="_blank">📅 19:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85778">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16632ab2c2.mp4?token=mMvouEfT0VR2y7evzQ8VfSBZJZMUcO6HvpupBJ0Rk5DWR8h-yxEaBcLZDTeq-9z4dA-NySdObMrbHqYrWIRO0YdiGVes0NDz1PODVncaMlOM9x5cDVE8Eypihp1sUCpu9853KlW6L8WT5KkUR-DZN4S67odSsFqBGFWlAjn4-7FoX0UI5gPen2U6L1eC-ycwAethJaP2RpKsjZv9ZjDWzyuaa8T4HMOC2UnqIcHeWQ54VWkE0sKaTndM7k0QFlVpAzHqeOhB5_JE796DxaB9WAzxVd1ElyWfNHZk_4owoEmscVC1_9m5qf9bsQwpAiXKyI7-4XaeqPLWOeCoDy34yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16632ab2c2.mp4?token=mMvouEfT0VR2y7evzQ8VfSBZJZMUcO6HvpupBJ0Rk5DWR8h-yxEaBcLZDTeq-9z4dA-NySdObMrbHqYrWIRO0YdiGVes0NDz1PODVncaMlOM9x5cDVE8Eypihp1sUCpu9853KlW6L8WT5KkUR-DZN4S67odSsFqBGFWlAjn4-7FoX0UI5gPen2U6L1eC-ycwAethJaP2RpKsjZv9ZjDWzyuaa8T4HMOC2UnqIcHeWQ54VWkE0sKaTndM7k0QFlVpAzHqeOhB5_JE796DxaB9WAzxVd1ElyWfNHZk_4owoEmscVC1_9m5qf9bsQwpAiXKyI7-4XaeqPLWOeCoDy34yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرض طوق امني حول القنصلية الامريكية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85778" target="_blank">📅 19:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85777">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هجوم يستهدف القنصلية الأمريكية في تورنتو</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85777" target="_blank">📅 19:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85776">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هجوم يستهدف القنصلية الأمريكية في تورنتو</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85776" target="_blank">📅 19:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85775">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
🇮🇷
‏
وزير الخارجية الإيراني:
لقد أثبتت الجمهورية الإسلامية أنها لن تخضع للتنمر الأمريكي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85775" target="_blank">📅 19:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/85774" target="_blank">📅 19:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUOTH_aZSjaWkHzbGytjvEfR3hRGeFZL17fhBpTCW6nBCMpJyqquoMtZtGX3av_3Z5Y_KtmoNAF9eNuA_SZ2Ojm1vWWd8mSvW9LOY8sJc5GVvMPa0T7RjqoxTNXfG-E89SmHQvyDjxPh7lqf6G_llJFYXIG1HoKnhHQjpjFJfkxtWJNjryqt161qpNmLr8lRSqo4JX7vrUnl8zk1pvpEWnVV49KHZJBGrH8lPVnEvbZtOZKs-mP0lwFc2VlL-jIC841W9rlirDEtSEE-yqk3AIMpHlzmr5LWPoP3PeW1KHIXch4WIhi8Cg56VF_LUATceSzucwq06K4SMdVpq7CbVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3DFwAyfRrbWGMPGBK5IZpA8AoY4Z4-Eiow44Abrgxp5Zyy_BQ8Js9JDRIooIDV7hw-fbrgGZjhIrijlvh17kZfyHdV-zx4nQ_nUKVQeg--xVRyWFQWeDOVsV_9hUPsGsdPdSRzV5Ij8nkyFLu-YU2hBXmB_E30yQflaLebPDKZrTIKuD0kr3BkAX2aNweS0Hb76UQiJyBTOLPGmkBHiyrNQG_LzJVF9PGHHKIQ6O_SRe2cHkKFqO-9ahEQoJK68xTgeNydqB2E2r5dltZbjbnUPMZ7gXE2jj7E5KjmxqcfrLzlcZGCAYVEkI7I4KFKHRggkFUAfNUNBZMZwI_CjxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد توثق لحظة سقوط الطائرة المسيّرة في محافظة بابل العراقية وما أعقب ذلك من انفجارٍ عنيف في موقع سقوطها</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85772" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85769">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdX8kW8rsK7ptRA5Z9dkwt1LxzA5ja4tdxCbUVhz9NzH6udgcpBjTYwdSD-gwYfY9Kw_MGHMAeWi8ldnLar4soVNMjqA-6RP_xWcUVbEjyEH82nexVkjLhyUDhseagLbtAhlY2qDkYE-VllHDuEIvODqLAzr2yxPVrbquP-KYFU6UzhEn7v0HvYHVj-bDyzxlx4Ka1Y8r35a0eS5x3U7YY4pTaAi9HRYx4XnXoYnnrwNvXy-3Z7_UViXWhfjkl6KuE06Q45i_YvECqAqU03iDuuKM-jijuikJ_e9mppNIuXPgkg_2ngwyzAHtAwCDckB1xR69P0pUY7PdzL7Qd4vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHTSEYfFyLeswwE6zaoxF8iOLXKVoQQxd16SjNnZO38P3sMqoahHsjk0Gv7H-FMzBjnoRhiboQokLUWOBfjD5J8vAjmTOxo3B601OyTGOcP18NAssVClf9Wq1nR5WBJpJcbXbXCYvRg49W-0Caf00b2CN_Y_3yzYntUEGNoUJ-RU6ShN8aReNUXy9noRlUPHEZ1rxtpUSuQ7BnqLVJy8rbm69e-Nu3FIfXvtO7Y7YVdLKdFTB5uG_NsTrQRRwQVuphzQ-gf5d3GxePJxILTVnrbYuM5GBGqq8juYQthffTFWGSZLNAdjuM3G47_mJ9YYRUPzuGM84Ce8WP0acu4s2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTAW6vbcKBQFZ3oT9g2JJLy0su12C62VWWudjY5-mG_FzGwj6wWqQM0eWBsQ2ejR2dC-ZPhSoEKbwHcsw6KAz5tLYfED6U5fTz67yd2v5Ngh_nQVehoS3Wdgv-Xw1mUR1O2oRnpnaW4nSoRFp3rfOa6yLOfD092BumvUzeDP3nIGXmThvvQpjR9-uuFpVSTBeXCLSy_kU58kcN8kihwzPnbskullotDOnBSfuRsKOwwmLeRTc5n5YVUMujG7SorxSoE9rs7aRjsGO8CHTzEQHvI5ApwPKahOEv2Ci3VSSIdKZ8-rNqXba5de3eePW3pbOVgv-BsebO7fZc1yBpmDKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
من السماء إلى تراب
بيرقدار اكانجي تحت اقدام اليمانيون …
انتاج نايا على التلغرام</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85769" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85768">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
🇮🇶
لحظة سقوط الطائرة المسيرة الامريكية في محافظة بابل العراقية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85768" target="_blank">📅 18:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85767">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
‏ترامب: لن أمنحهم وقتاً طويلاً للمفاوضات؛ إذا لم تنجح المحادثات، فسوف نعود إلى عملية عسكرية قوية للغاية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85767" target="_blank">📅 18:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85766">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
‏
ترامب:
لن أمنحهم وقتاً طويلاً للمفاوضات؛ إذا لم تنجح المحادثات، فسوف نعود إلى عملية عسكرية قوية للغاية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/85766" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85763">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJrlSeI10ax10dyO53ijY4QevkySDJcF9Lf3fUpfNfiLZ9LIocMOnaeou-HiYWYJzLWw3z6_gNvg0lLsLVXoOa84pYJwITmY_atEh1P_AOQ5xy7Qjm_gEhXYAvqepqZ6kVu0tm64vP0wNwFuF9DvanIsfgRLMqg1drYq-D-9C7P5oCOl3_ekxwskMLFeR8QJacchBzmtjiNv8XdwUSrxE-amvS7UUlqhOyu3mzupwXBiNt2HQPKSo-DXJ68CU-sa4OQipXUv5-MBzy43UPxkDFJM2VMdI-78ExxFmTuoZWF_xi-3TcZrpcqoe9llB2WlSwufvxn_F3RNwZZTVLy58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0y4jAu0xUhRzQWQDv2jKihOCcHNXeFGl4UPUqpHoiC7qliicL3fXZXNkx5CG56VOXFoMI-8zMDjnpqqOZ9sWpWGzpJsYqbaQmb-ungt_fHnPGfOFwR6AD9LQakQLQxY6XI-x0dLRFrOffQo8q2_HwKk-tp5dF1LdEUKo07ZKBN2RERFTVPhAeB_L4VMzZ429Qm_7vM--Q2ycM4Q0lUmkBMArSvqfOjgHu2JWRvR9uhosN009_qb_ejNxJdv9CmrEkAWKTwk2S_L2BacBBpvWWrshQnFUX8eeHhiu_3tBv8afx38LROcBN1vX5oKtP7w0AX5NkkqyA9raMPnsV9ecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kug_BzfJ8mI1CcDVPLF0-IJX01QsjsMByVjpRI4zAw0h2xbmOpM1WqlesQOYoaEUMnMWey8jjVr4KSr5fMghaon_3SndtjH622IGnZFRtRU9qLw6OzyAQNSP1dMtbFtr_mDuF8jL0mW2yyFdoIASQ5CXgZBRCHsagnBCkLQRG37sVjk6v3vIxY6gmWOo--G0HBE-21X40N2wTwTVKIy4Jg7av5M4_9qkfIm18a3rzarlX0qiPteSqjVXC9rnA9aXsJh-ML3QOzu8ElII-duwHTsp9uW1z5wS8WVUcjYR6rSzHiCDAJvZkuyOQotJ0972PwvQVcTk4eqPmExJrKZ7Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏الاقمار الصناعية تظهر احتراقاً كثيفاً للغاز على طول خط أنابيب المكثفات/الغاز ومواقع الإنتاج في المنبع المؤدية إلى بقيق السعودية. كما نلاحظ أضراراً واضحة في خزانات الضغط في المصفاة. ‏من المرجح أن تتأثر كل من خط أنابيب الشرق والغرب وإمدادات الغاز إلى رأس تنورة بهذه الإضرابات.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85763" target="_blank">📅 18:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85762">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇺🇸
سقوط طائرة مسيرة امريكية في شمال محافظة بابل العراقية بدون اضرار.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85762" target="_blank">📅 18:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85761">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd27e2cef9.mp4?token=iIrW02xoyaCSh9Ob9iwpKUJTfZnTGvjT55dFnALYvBmVN88Fi0TesWLzIqEQJs8hXivXDnj79tIx_uo3g2fEv5F7IkNsuQqyyIjOTjxN0JtsT5an6ssT0YFFGCebyWEm_qzhxQbnrYiTe_7I9HG-Qd69mzxQnmDk9La9L_Bw4SnUBj6EUAlo-wGDU8Yko5I8hMvu_ZYD1JtimRAb3K4cD6xdERigf5_eRC_YSiS8wwf6LpV_Ct8HJi0d05dmUHQ6rwpu0AwfIhscDtpo570hDL5sj-PcvT3J-9wlcIGxUn5bYyhu2UJBGV_MhAA_x1pBAX0ofa83F41BwOke8uVW8rcSF5X2_GW_8vAGoaM6kk1kLoMGMmldP85psevbPQSGVYPSDttl2BmGk163-LnoIZvtz3dmI5yU3Ft0hd4ezzVx36vdLyzOceC5FhD5CqAa7hlZpjRY1ZWdaqsU9JRf-nevQQj1ftemodaSXscKx3n2jd0uAsGzSuODeZkMUlImWe_zHm4I9yOzH2eRZi91YfX0azeD_ozaWJKnoms-B70aiBT48bQV6EEYDhISePtUFK2Ucrc7IIjXFIx2l3gPcFZ2YRXFs09bJ7F9D-L4TuazVtPs3thuO4HdSEmQxW4p4yrQxJNQ9YwfqrFMgvtkFMz5QeDMtmjXbu11_5WKNjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd27e2cef9.mp4?token=iIrW02xoyaCSh9Ob9iwpKUJTfZnTGvjT55dFnALYvBmVN88Fi0TesWLzIqEQJs8hXivXDnj79tIx_uo3g2fEv5F7IkNsuQqyyIjOTjxN0JtsT5an6ssT0YFFGCebyWEm_qzhxQbnrYiTe_7I9HG-Qd69mzxQnmDk9La9L_Bw4SnUBj6EUAlo-wGDU8Yko5I8hMvu_ZYD1JtimRAb3K4cD6xdERigf5_eRC_YSiS8wwf6LpV_Ct8HJi0d05dmUHQ6rwpu0AwfIhscDtpo570hDL5sj-PcvT3J-9wlcIGxUn5bYyhu2UJBGV_MhAA_x1pBAX0ofa83F41BwOke8uVW8rcSF5X2_GW_8vAGoaM6kk1kLoMGMmldP85psevbPQSGVYPSDttl2BmGk163-LnoIZvtz3dmI5yU3Ft0hd4ezzVx36vdLyzOceC5FhD5CqAa7hlZpjRY1ZWdaqsU9JRf-nevQQj1ftemodaSXscKx3n2jd0uAsGzSuODeZkMUlImWe_zHm4I9yOzH2eRZi91YfX0azeD_ozaWJKnoms-B70aiBT48bQV6EEYDhISePtUFK2Ucrc7IIjXFIx2l3gPcFZ2YRXFs09bJ7F9D-L4TuazVtPs3thuO4HdSEmQxW4p4yrQxJNQ9YwfqrFMgvtkFMz5QeDMtmjXbu11_5WKNjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مشاهد للطائرة المسيرة الامريكية التي سقطت في منطقة المويلحه ضمن محافظة بابل العراقية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85761" target="_blank">📅 18:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85760">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004bc022b2.mp4?token=OyrLV84JV2Nn9HLhiItHXowaxPva7TOrskT9wj5RJ1AKa3rTlffy2yAr6af_e-DD575j7duwqnJuCvsQh509Fp0n0IurnWBt-4UqDLxRKMtIwBd9piiF2aMZUAZyaDp8a9lbkAr-tlCrN565mWrSRwUh12BZk8Hpt6OIx9u8_gEJqnmIptCfOQdZhiTc79LqhyWu_DdwSm5xnjkyQDYGwzvBK8cut8d3KE2s44OR51i_JErFZAO8r8oHHesQlN6P_ZSFCeSnTqD0D63bqWzhhr5SC2vVPaa0qBX8vMmCjy5L-e-Dr9qfOFyLfauwDGA8lHwkUVwa3ldDknx2_L1s6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004bc022b2.mp4?token=OyrLV84JV2Nn9HLhiItHXowaxPva7TOrskT9wj5RJ1AKa3rTlffy2yAr6af_e-DD575j7duwqnJuCvsQh509Fp0n0IurnWBt-4UqDLxRKMtIwBd9piiF2aMZUAZyaDp8a9lbkAr-tlCrN565mWrSRwUh12BZk8Hpt6OIx9u8_gEJqnmIptCfOQdZhiTc79LqhyWu_DdwSm5xnjkyQDYGwzvBK8cut8d3KE2s44OR51i_JErFZAO8r8oHHesQlN6P_ZSFCeSnTqD0D63bqWzhhr5SC2vVPaa0qBX8vMmCjy5L-e-Dr9qfOFyLfauwDGA8lHwkUVwa3ldDknx2_L1s6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة مسيرة امريكية في شمال محافظة بابل العراقية بدون اضرار.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85760" target="_blank">📅 17:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85759">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada0a48777.mp4?token=iqHRSvv9yBcdYviLVRsquzuZnPXEWB_A8gHvPFMgUlPICOEXVd0kkXRJ5WUyO6l_MKJigEyuvRaUmd8iVs1d_OCO3RI0p2TLX9DJpcIFvS-CfWI5-EnbH3oNfDE5WZpkzoYlwH4rzP7rlLbBJXiBk2dCded-yz2xmbWJZAmHLCwN0IJsmn3sw7BM09DOpMKkWrapAkHoHk4-vb-UV_kHjn0utdl5a_XoaEp_0kCjMioIKDv9haoRWU0MVHL5N6sUbIOaDSkqSRQLtKEMswYg8z1EMWxVXaBOrJ8gpI6JOaujuoFBE0u_Y0m3pOfnT3_jaU64CQDjvN_twH5Pgptc1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada0a48777.mp4?token=iqHRSvv9yBcdYviLVRsquzuZnPXEWB_A8gHvPFMgUlPICOEXVd0kkXRJ5WUyO6l_MKJigEyuvRaUmd8iVs1d_OCO3RI0p2TLX9DJpcIFvS-CfWI5-EnbH3oNfDE5WZpkzoYlwH4rzP7rlLbBJXiBk2dCded-yz2xmbWJZAmHLCwN0IJsmn3sw7BM09DOpMKkWrapAkHoHk4-vb-UV_kHjn0utdl5a_XoaEp_0kCjMioIKDv9haoRWU0MVHL5N6sUbIOaDSkqSRQLtKEMswYg8z1EMWxVXaBOrJ8gpI6JOaujuoFBE0u_Y0m3pOfnT3_jaU64CQDjvN_twH5Pgptc1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سقوط طائرة مسيرة امريكية في شمال محافظة بابل العراقية بدون اضرار.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85759" target="_blank">📅 17:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85758">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇶🇦
وزارة الخارجية القطرية:
ندين بشدة محاولة استهداف منشآت نفطية سعودية بطائرات مسيرة انطلقت من الأراضي العراقية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85758" target="_blank">📅 17:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85757">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">على عكس اتهامات السعودية للعراق   اليمن تتبنى هجوم على بقيق والرياض</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85757" target="_blank">📅 16:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjxZjMeyBwAaIdwcZiyAenPicIFroKpGtb4s41XNGUn17QVocBzMKt4xkPra45BLR6Ly4JK8NZQLKIH0Wqn7IHux4KZqgWePFfiyNvdfSjofMQ2ike0cAQQInPq-EBNIHZP3cjaY0JJij5BhzXvVJ9boYza9tBCk5IF944lfdDh59jiGX8AkHHqRflB-yUEKvbkLLrIRDI9Atmwsqet5KqOf0U44NurPTtVxq0ByxZsaNzLrf5ZEeiJB_FrT8mroI28nL_f44XKbYqY7u1-FQMYRecTwX_iTlPmQADKcN1EDN2r5fUk0e1QydEb0NWiAjG-kYg2ndBvBMkZR07j-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة مسيرة من طراز Mq-4c تطلق نداء 7600 (طوارئ عالمي) فوق تل ابيب بعدما كانت تعمل قرب حدود ايران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/85756" target="_blank">📅 16:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85755" target="_blank">📅 16:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85754" target="_blank">📅 16:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارة الخارجية السعودية: ندين الاعتداءات بمسيرات أطلقتها المليشيات العراقية ونؤكد عزم المملكة ردع المعتدين.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/85753" target="_blank">📅 16:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
يحيى سريع: تم بحمد الله استهداف عدداً من الأهداف والنقاط الحساسة لإمدادات ونقل النفط الخام من شرق السعودية إلى ينبع بعدد من الطائرات المسيرة وذلك رداً على اختراق المسيرات التابعة للعدو السعودي للأجواء اليمنية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85752" target="_blank">📅 16:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇾🇪
يحيى سريع:
تم بحمد الله استهداف عدداً من الأهداف والنقاط الحساسة لإمدادات ونقل النفط الخام من شرق السعودية إلى ينبع بعدد من الطائرات المسيرة وذلك رداً على اختراق المسيرات التابعة للعدو السعودي للأجواء اليمنية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85751" target="_blank">📅 16:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">استهداف منشآت بترولية بالمنطقتين الشرقية والرياض</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85750" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SstcQYYZI9hYW3YUoShNm3gLpEnO6L9N5BaprdKJ2xjsMfTNRtWjFFCexbgQWctimQsveBWyzo0g0lY24zkTKWmijwFLvnc56CL64FaTEWvVst8Cx08wOe9nvSlyBm_joX6WuAduo1-CossZUdm21L4u1B-TpjCt776RPjHIygdtLfUbYR6LeSUnWe6VyF1WAc4k5q9wafMvGtWJC6emOy5BeAd1CJk2FRePIVDRxAELpC35l131NcTQq8mLhayR5nbqBFTYW6va2ZfLZxobcYPHIeYQZ8jmbx34J4teKIdBNNhm30kTL8e6EO4qp1f1nqYbXrY-UIHozXXW0-YKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاقمار الصناعية تظهر ان هجمات انصار الله على السعودية استهدفت في المقام الأول البنية التحتية النفطية لشركة أرامكو السعودية في جازان، حيث ضربت منشأتين: مصفاة جازان للنفط ومصنع جازان للمواد الخام.  من المرجح أن يكون لحرائق الخزانات الناتجة آثار بيئية كبيرة بسبب تلوث الهواء وانبعاث نواتج الاحتراق الخطرة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85749" target="_blank">📅 16:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FulHpqkFBvndwiEp426kxflz5T40orQHWsw_fkOkcGkXJnmzWU90y0_nEhHQ63SXcHBl9eJhfMtziQnmffm5hz33hPStv1LD44OIkPx1Vg49lgiMtmtd9iUubpzBC_77tCt-Ceg2qCShb5AAcuBR3OGYxw22vWSDgbn3vr5hq8tdyKdWytJ6tcui4WTPVmnNl5x08PR30jAiidEaFxsQb_O1rQUV6QH4qaI32mva39bZvCQ_QAS64bIZIAtX_1eiPGXofyjM6NuvzXa0F0hcnMRjqZrR2ldoGp8AEraXHno9aA5MUXeLyg8Fgy7wT-K9C4g16QGdgFwuir1ayQddZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
This could happen when you choice trump way in Hormuz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85748" target="_blank">📅 16:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزارة الخارجية السعودية:
ندين الاعتداءات بمسيرات أطلقتها المليشيات العراقية ونؤكد عزم المملكة ردع المعتدين.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85747" target="_blank">📅 15:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYfhQbIX1rJcS1dp7lY7xGdPIhgXhqBnjBinOQDmSMujx90wLcpEFOBNiSjaUetpwix0nsN8fKs999H0AMw4OiSjQtZoI_Z-spfdDmCMstG8Cx2JaKAT1nTXmvWx7abOwP4ts45RDuovLwTSx5pZJMPzi5sxQ1_KKDiB0CMcNBBlUBi3UixdVNSfkb2z1Y9sy9WSqIbweNI3eUC7i2ZwQxpZFQLkTdAJpATIr1tUvNDR1PbhUi0rYmEjebBTVH5WjBCq4-6o7vJFMsdWuM3Ex2_FxICu_8POU0flrGerH8zTnp9lKjOHnWPOMPrHffRRaCx4C9NQVX23ZVYhOo8YIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الطلعة الجوية السابعة والعشرون للاقمار الصناعية فوق مصفاة بقيق في السعودية تظهر ان الحريق بلغ قوته 70 ميغاواط بعد الهجوم الايراني. ‏بدأت السعودية عملية حرق طارئة للغاز في مواقع إنتاج متعددة بعد تعرض مصفاة رئيسية لأضرار. وقد تم حرق أكثر من 100 ميغاواط من الغاز في مواقع متعددة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85746" target="_blank">📅 15:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f90e9vXgG8jCC6wgnC1ic8Dqq4HZdBbS5Jt3AGev-5HAIQ1NCEEJaKOYBwduzrgEgf8uZ3FUFo8g-LYsnQ5Kes9a_WsBeGdv_m1NEXg1eZ926uFST6eWsRXmj44K9dlunKs-UQymjRmvHYWoII5MQTZ6u45ljlxaqmejAeJvOGoCmPa_gyf-wgEsvcVAa4ISqsDoYaQl2HEEKFU-2KvkSPylmrQK76ZGJiLxR18kzn2ZHeDQTjJ0l3ka7Spvojncu4Gi2JftIY6butsdmhJdCE14kEYzJ38-0HILq79-wwBzfaHV4LPCaxwvL1rxm-rE4hEnjnqbKRvd1nI7vMEUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Иранский перечень целей для наказания клоуна Евросоюза
Зеленский является европейской прокси-силой, и иранский ответ может затронуть европейские энергетические ресурсы:
1. Нефтепроводы, связанные с Европой:
· Баку – Тбилиси – Джейхан
· Баку – Супса
· Саудовский трубопровод «Восток – Запад»
· Южный газовый коридор
· Транскаспийский трубопровод
· Трубопровод East Med
· Арабский газопровод
· Трубопровод Эль-Ариш – Ашкелон
2. Нефтяные и газовые месторождения, связанные с Европой:
· Месторождение Азери – Чираг – Гюнешли (ACG) в Азербайджане
· Месторождение Шах-Дениз в Азербайджане
· Месторождение Апшерон в Азербайджане
· Месторождение Левиафан в Израиле
· Месторождение Зохр в Египте
· Месторождение Кронос (блок 6) на Кипре
· Проект GGIP в Ираке
3. Заводы по производству сжиженного природного газа, связанные с Европой:
· Завод СПГ Идку (Египет)
· Завод СПГ Сегас в Дамиетте (Египет)
· Завод Ревитуса (Греция)
· Завод Александруполи (Греция)
4. Проекты зелёного водорода в Султанате Оман с европейскими инвестициями.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85745" target="_blank">📅 15:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b07d9f8b2.mp4?token=Ha7fxjgxuw9JCTTPyVkl25v_0vBb-VdqgroCUeMdvv9JXthzVdfwNeKh0HypxpGDhTUJqCmZeBkm-hPIPXLczvipXc1dkSNSmtxlbRvtCcIb5SLzgSvOwtlKL1bZjGOqkypxjDd2WBMCOjX1dZY4wBo_tVd82Kk7OnnlkpwsFxMAx2QLVTgszX8pXDHl7pSqQM0IjkRdushrUbyr4hVv7EQOxMxL0eMDLwqf6LWxOGVJJY5Xv7dc1FDjZuOsBBp9T_lgztAl3pvC4OtWl33wUMB4T8aUDSXaEJiwNeq044zSQSmDdr9g4BqkVq_txXOFnA3mifszvvHOqXir-CoJ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b07d9f8b2.mp4?token=Ha7fxjgxuw9JCTTPyVkl25v_0vBb-VdqgroCUeMdvv9JXthzVdfwNeKh0HypxpGDhTUJqCmZeBkm-hPIPXLczvipXc1dkSNSmtxlbRvtCcIb5SLzgSvOwtlKL1bZjGOqkypxjDd2WBMCOjX1dZY4wBo_tVd82Kk7OnnlkpwsFxMAx2QLVTgszX8pXDHl7pSqQM0IjkRdushrUbyr4hVv7EQOxMxL0eMDLwqf6LWxOGVJJY5Xv7dc1FDjZuOsBBp9T_lgztAl3pvC4OtWl33wUMB4T8aUDSXaEJiwNeq044zSQSmDdr9g4BqkVq_txXOFnA3mifszvvHOqXir-CoJ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
🇮🇶
تهديدات من عصابات الجولاني تطال سواق الصهاريج العراقية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85744" target="_blank">📅 15:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/85743" target="_blank">📅 15:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">استهداف منشآت بترولية بالمنطقتين الشرقية والرياض</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85742" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85741" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/85740" target="_blank">📅 15:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85738">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d1e66237.mp4?token=huOTmliZfOZs1jZaw5GOPTYVpIv9OJ3WtwgNnt34wMSVOwU_xtyIfoavZCF3izSaLt29aYd0Qe6DIr2RL4Qu58qy_hPlKqZ6ca7CMEaIvRpFzA_bK7GkhJ8yoEwJDdoO1IGt5zn8m0kpVRs7pBUu5jv_aUpnEve-I_SGqRMw8A5iVUUfXqRAMnjSOZZ_aL5Hv1xk6uGVSWEgzrIIvAF72_zJ6nvoWSWlBAL_tGpSN5x_hLNWhF4G9HgxxyiqdAxBAgHWmiM90lc8KYMf_AsOJtKnsB49toIFpXjy5Oa9hFGJnhxT2BOnhd-5nIhmBeCJg3LCD0SBuzhLRYBM-E9lyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d1e66237.mp4?token=huOTmliZfOZs1jZaw5GOPTYVpIv9OJ3WtwgNnt34wMSVOwU_xtyIfoavZCF3izSaLt29aYd0Qe6DIr2RL4Qu58qy_hPlKqZ6ca7CMEaIvRpFzA_bK7GkhJ8yoEwJDdoO1IGt5zn8m0kpVRs7pBUu5jv_aUpnEve-I_SGqRMw8A5iVUUfXqRAMnjSOZZ_aL5Hv1xk6uGVSWEgzrIIvAF72_zJ6nvoWSWlBAL_tGpSN5x_hLNWhF4G9HgxxyiqdAxBAgHWmiM90lc8KYMf_AsOJtKnsB49toIFpXjy5Oa9hFGJnhxT2BOnhd-5nIhmBeCJg3LCD0SBuzhLRYBM-E9lyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
خاص لنايا |
مشاهد من سماء مدينة جيزان السعودية حيث لا تزال سحب الدخان تغطي المدينة عقب الهجوم الذي شنه أنصار الله على منشآت ارامكو للطاقة في المدينة قبل أيام.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85738" target="_blank">📅 15:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85737">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇾🇪
انخفاض صادرات النفط السعودية بنسبة تقدر بـ 50% بسبب حصار انصار الله مما أربك حوالي 3 إلى 4 ملايين برميل يوميًا حيث تأخرت الشحنات أو أعيد توجيهها أو لم تتمكن من مغادرة الميناء.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85737" target="_blank">📅 15:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85735">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YK17_59qy1JpmKeWOrDaNi6I4wsek_ZVkfgssEsDWRsKeo00KaWy5Kj7JjojSHZLuVwZVd8TXJ3GRnvJZFr9HFr-uHa63yFNZAG6ibx-pRIJw2EF4YXuOxBd63okrtODehAXMTfeNfQNPLVg2QzKB9I1cYZQifxCHAQ15M-9ycIkTy7Zl_XgNhcHCrocQ2C4MG6BvTf0yaF_CCeSHM0H2VWhxo07z_3sWL7eH5fFpAKudHsYiNj3wC0JQFF4tj9ma7G26epPy_cQPz-REy_cCKmsSjyG5HuT06R0u6l0veOtoKch_wf8yshbTfqY2_p1gej4QftnxeMj0W9hhTTQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4Oa9i9ZyhH1jGz_EjkKGa_bWE2YNl6L8ceBOyeQiMAqLRCYvlJOCcuyT6zl5n5gVJFghrAWaKSBlAa_J_7kppD5lQHU7-obke2V7UniGuXy4XM8G41vlceeeFOw_XTeicF4b4gLuHeHqf3X5DazPpw_vs-mL6JhekU7zNsLa3sxCz_tHz9aA78vIPZT7N1XucdBRvdjRhbdi3xVTLljQZ5kYS3dBErRnnU2dvxZGY5EKhn7ot8CK6gFhy-2QN6YapLhbEZ-nHmWJ-Qz2FQVih6l1-ggAVghaHo5YNiVrQbEooQe0uicT_Z58SlIgVp0E6ZZCz5e5TLSvqaxSHZ0FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الدخان يغطي سماء مدينة جيزان السعودية منذ استهداف انصار الله لمنشأت شركة ارامكو في المدينة قبل ايام</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85735" target="_blank">📅 15:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85734">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزير خارجية النظام الاوكراني:
إيران ونظامها متواطئ بشكل مباشر مع العدوان الروسي على أوكرانيا.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85734" target="_blank">📅 14:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85732">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1ekuTsnUNOnHJY7MUZ6kb79Geoq8LGorhzOdd5mjeJfH4WLWhJdtkizGYNEOln-nV8UD6XKB7MtqljNi1z79TMWl2QsZ_1E4XtCMp7UkAbhn3UNGbDwGrm1CY6ShSbYOsNv8tMhG2u8bPPhRmgKxBVGWAz6wQMkOqxwxo6R_WcDcv6_9fz5qzyKZ6oWS5zpskw-AOcDiOp-DtSxN3M-eNkTBdKq5ij4Hyan4WoTsicmubOZqdVeiNkcWQ71j-oMUshdiTq_AF83qha6rxndZznCpd_KVSrBXjuD7bCw52zCaU6P6HSvf3pXxDf_AYAls6cdqGZ_Bd_S2fv9McPViQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E49nc1-bwPlS_MWI3UU0YylGxgUDPktLU-152ejmQHN64jY8QExqVm_TtLKzB6BLqvUVhfvqZdDdg_2zWZONUqQdvH401zQW-hg-0v04GINAqC8XA1vJjh162NVG4BNndQALGCkp0NWg0-sqIDeXGiw-4UzIE-K9leZCLRSIPh2LAAph6G307IEFkHWZpLTeqK5X_nzVK3mv_QKg8VkQeKB3KD55_aDrMCkECKbeFij-XMCQ41umXq5INprcLnFhqCExKKnDzAy6HJDFBnmW3erFD3ijcPfCq2jNlxP0RsgprnzxM5St4XW-MegWhAO8zB2fzuZPjlQwzt5cYIKbDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من الهجمات التي تعرضت لها منشأت بقيق للطاقة في السعودية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85732" target="_blank">📅 14:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85731">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مشاهد من الهجوم الجديد الذي استهدف مقرات المعارضة الايرانية الكردية في قضاء كوية ضمن محافظة اربيل</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85731" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85729">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجارات وتحذيرات متتالية في الأردن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85729" target="_blank">📅 14:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85728">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc2zwJXIn73w7YRkSH0HB9FX9-rSS3o5aLrDgMJaVWw8CGVMXleae8JsGE_c1_a2xheRn3Np5abSnOmDHJ5oEylU1m4Jz-VFc2QQMrJk7HCHsCdHbbGahSKWx1YrrGK8RX6Yul43qwLvfZs5AD60vU5IDepU-LN-e1FifUNdfnPjFcFElr5M24hk-odUHjQj7_0qXH0dGueHmpw29qexOvJ0zJk2xUh9Cpb1eWHbg2chVoCx5yX6iWI28M2fsnVH_lJnDdKOdgSHEBAJj04PALTjimuNKu0TP2FO0JL3yfqNiMeyvAr_rsxIir1MlMzvt3SUVEYOC06n45N2Tm9Hdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الصناعية حريقًا كبيرًا لا يزال مشتعلًا في مصفاة جازان النفطية التابعة لشركة أرامكو السعودية، حيث يستمر الدخان الأسود الكثيف في التصاعد من خزان تخزين نفط كبير.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85728" target="_blank">📅 14:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85727">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnR374wZRBRGsLhrKTQ7Gihf3N6oBC06MjB2baf4_N90Hj9oKFGB7MDt9EPbHXuuOmPVKdq6fM2luVZpMgQN3ARDu_Mjsv2Kze-abNdxMA-vUPYxgiLsGqVssBTiVqn9XKbZf-xdXOfi6wfnT90s9liqFggyOtyG7Gu4vvz0QVCBySipgP95_KIYTXgSxPwSO4_ILeBzyGshINoKeoJV6z1bzOKs_MmCWbUkfeJGO3AxFeD-PwW_2f22q4HJjQQZIcw6UogoFAtuy39R96gjHxO5XzHYzjxJxiksvyOUIERiY5J1z1-9TDb5hgZM8RRUiaJfHyFjqMz0Wt3iOD-cWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز مدينة الكرك الأردنية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85727" target="_blank">📅 14:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85726">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ff363564.mp4?token=WksN4fU6YRqs087YSsKEhyL7ZSQVApE1Y9hX1MSGGumqwWLBDNOSntaLaogJVlwPOKo909AyQg0z5_hdvrD9-iFRmhiyK_wI79tZ6M7Rud_uZyBmutU4s23lgGbRcYia2_VuFjXC2nStJCTzo3UMZ8coQvWi9697V54bFMtplW_a9ZumW_8mq4hnSEsahL7J7hVW5u-PJcA9weaWtGGEHDEw3XMQln91JVxBk1K2_upm0NlxIMWDPc5G97PF_Wl6p_a8uKdefhauMwzHJxvdBMkbtQIlU540Lv5inoC846x-Xt-WozbY0SeV6j3LeE-7HmpwVWgw5x8kg_m-7Tkjj2qn5hE3Zz080Wv_-6KtKR4DIgrAPmIV04kdSEJ58_2Q_i5atf1VWmAe0aMD6wlfESl0jmPta420x1c42SYYhqL-DtcnA5wJcnhahksWdYzyLl9iIXIaf-upitbdK9haLnXnrD8jIOgqF0_-2b6087agKm9wmii9WCnNPLdGrqupyMQIfAPEeT8jV3g2wfGWgXdzcL6S8FEKr61QHww4yq_ht9Bes-a_vJypRXxx1tzRCIGDC49wa8CDNU9vvqwO3u7_Yl4nyTdWkizyysCjJan3RET_LLlxI8OMSsA0fLzn9LkcKqhQ1a0l22tFEjKg9g4BRafIFGhZEmrfjSo1O34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ff363564.mp4?token=WksN4fU6YRqs087YSsKEhyL7ZSQVApE1Y9hX1MSGGumqwWLBDNOSntaLaogJVlwPOKo909AyQg0z5_hdvrD9-iFRmhiyK_wI79tZ6M7Rud_uZyBmutU4s23lgGbRcYia2_VuFjXC2nStJCTzo3UMZ8coQvWi9697V54bFMtplW_a9ZumW_8mq4hnSEsahL7J7hVW5u-PJcA9weaWtGGEHDEw3XMQln91JVxBk1K2_upm0NlxIMWDPc5G97PF_Wl6p_a8uKdefhauMwzHJxvdBMkbtQIlU540Lv5inoC846x-Xt-WozbY0SeV6j3LeE-7HmpwVWgw5x8kg_m-7Tkjj2qn5hE3Zz080Wv_-6KtKR4DIgrAPmIV04kdSEJ58_2Q_i5atf1VWmAe0aMD6wlfESl0jmPta420x1c42SYYhqL-DtcnA5wJcnhahksWdYzyLl9iIXIaf-upitbdK9haLnXnrD8jIOgqF0_-2b6087agKm9wmii9WCnNPLdGrqupyMQIfAPEeT8jV3g2wfGWgXdzcL6S8FEKr61QHww4yq_ht9Bes-a_vJypRXxx1tzRCIGDC49wa8CDNU9vvqwO3u7_Yl4nyTdWkizyysCjJan3RET_LLlxI8OMSsA0fLzn9LkcKqhQ1a0l22tFEjKg9g4BRafIFGhZEmrfjSo1O34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تُظهر صور الأقمار الصناعية حريقًا كبيرًا لا يزال مشتعلًا في مصفاة جازان النفطية التابعة لشركة أرامكو السعودية، حيث يستمر الدخان الأسود الكثيف في التصاعد من خزان تخزين نفط كبير.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85726" target="_blank">📅 14:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85725">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f63084adb.mp4?token=Lx85zNeISWxsV3pSr1RwJWp88d6--nXhVdJ9t7qiVeP3pRlTan6-g99BJPbddNtupGcia2v1Fk-SUSLXCzXdqsUCMJdF_eS7Df9fcMSSL6Rxlev8B4I1L6BsocshpgE478bZsGJbuM3OW8xsJcQK4l3IXOx-nIl2BPVeScHdLfbr4AEoX9PbmROF4iDFGu8H7kKRUVfQ0yrN0AHL7p49Fpfllji1ih0SisxvlH3B0op21PgDaojfMMmHdRPywaSeKiV_ck-BHNmJN7i1iDsP0efNIs5FyalsErCCKfRV9cfMDfLXIDhuGrwOwSzymcD6jvIKzLDwgmrU5232sMGgdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f63084adb.mp4?token=Lx85zNeISWxsV3pSr1RwJWp88d6--nXhVdJ9t7qiVeP3pRlTan6-g99BJPbddNtupGcia2v1Fk-SUSLXCzXdqsUCMJdF_eS7Df9fcMSSL6Rxlev8B4I1L6BsocshpgE478bZsGJbuM3OW8xsJcQK4l3IXOx-nIl2BPVeScHdLfbr4AEoX9PbmROF4iDFGu8H7kKRUVfQ0yrN0AHL7p49Fpfllji1ih0SisxvlH3B0op21PgDaojfMMmHdRPywaSeKiV_ck-BHNmJN7i1iDsP0efNIs5FyalsErCCKfRV9cfMDfLXIDhuGrwOwSzymcD6jvIKzLDwgmrU5232sMGgdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قضاء كوية مجددا</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85725" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85724">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات عنيفة تهز مدينة الكرك الأردنية</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85724" target="_blank">📅 14:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85723">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpie493zZTnGHgKRVL5Exj_nthGRY-zd5UWwKnTX_6f_QDaXxQZySSzodhGmzYqzcEryuffwANTGGhS_llukobhcWkkfyUSo0LHFeHqJjK3VXz-WXmPUp0p-6juXjBfoy6JAxpt_w_snqq0xQsyrajVD1C2YpA6ffAQdmVbkyBSQSa6SLKMw-ytP9cNuRzM50jlHgR2urHW6PPc-NQ_un8ERrAUwWsmOh6b7ZIhDXbdDFXgLrOGL02UfHso6IL2vBWZfAIiojlJdqS7DKACyoWClOTfQeNMtDBL-Y7pykbAFo-7u2ptv_Wrw1Nqv4WGnugGX5e5Py2IU3di6LgSanA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85723" target="_blank">📅 14:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85722">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85722" target="_blank">📅 14:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85721">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85721" target="_blank">📅 14:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85720">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز اربيل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85720" target="_blank">📅 14:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85719">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT2CVEjSLqMDpyc_rZCrNFOJ9AE3RPz-bOtbqAblaLQXPc_ao7gCdumv9Exdn8GIyy2fiJWM260mDhBIDMPc2JuxCifBAel7k2Xz6P2XVGKFL1aGdi1FWGRrMxFfm2b1NG2CyrNFz51_SnHdNkhgEU_zg35MDHEJOmNQBU92rJPewR1h-maLFdRqc09vIJjmraihlETlry9q-muiBS09x8WXadYVqsXSt9wcCczM0GCHP4RkB5tzyMHPSEH4kWgEweLH1c2Qp7e6lPp-a3zmwJIlaLCRphOJY_f_3em1AhWgGbZrz8etMXrkPdOd-i5Igc-LDg6S3hUADeH2wHg1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرح شاه زوجة شاه ايران المخلوع تعلن حظر الحكومة المصرية إقامة أي مراسم على قبر الشاه والتي تقام سنويا في ذكرى هلاكه.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85719" target="_blank">📅 13:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85718">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇨🇴
الرئيس الكولومبي الجديد:
سألغي خطط إنشاء سفارة فلسطينية في بلادنا وسأقوم بإغلاق عدة سفارات مثل الجزائر وكوبا وجنوب افريقيا.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85718" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85717">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea5c211d7.mp4?token=iHUg0x8-qoRTSQL5DwUNho1KO97wq1-PINHOOb-PhYT-363MVadwumsVmIoSPgHbjhu5CSzAJFVeuAXCTPVs22ZDM4KYky-Joi-p_ew397tISurDDTHBp53pdefpEh_AZzwjDbmX3asWC3tLCG77-VJ9FVFONvdbgz3tHsTxcyu_qU_QCtsmklb2Ydeie7x5pko1ARYXhytYXssvgbioqbVA5Pyq7rFebyb0NvzShfGPEoe78FVbtU4nNKWtQYA_GUVGQH-uPKGXyCOdbz7XbkakIiDH6keIblbqI-KPf8sViDatzPIfOc0dkH9m9HWdyoiJ27vJ-IR61f9PGywM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea5c211d7.mp4?token=iHUg0x8-qoRTSQL5DwUNho1KO97wq1-PINHOOb-PhYT-363MVadwumsVmIoSPgHbjhu5CSzAJFVeuAXCTPVs22ZDM4KYky-Joi-p_ew397tISurDDTHBp53pdefpEh_AZzwjDbmX3asWC3tLCG77-VJ9FVFONvdbgz3tHsTxcyu_qU_QCtsmklb2Ydeie7x5pko1ARYXhytYXssvgbioqbVA5Pyq7rFebyb0NvzShfGPEoe78FVbtU4nNKWtQYA_GUVGQH-uPKGXyCOdbz7XbkakIiDH6keIblbqI-KPf8sViDatzPIfOc0dkH9m9HWdyoiJ27vJ-IR61f9PGywM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قضاء كوية - محافظة اربيل بعد الهجوم المسير الايراني</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85717" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
