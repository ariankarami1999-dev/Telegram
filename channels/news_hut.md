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
<img src="https://cdn4.telesco.pe/file/e4d0a7S_EFaC5jLDH0-MTzdTrAtGVAiRPTjyNCSDwHhi7uRWj4u08z2NO77aPIH80Id3wEgiRr0fMBf-gTY0ixllEBKP8BvbGAkIbIOmyB-haHvZ0DSZw0xJ0QaRIyKIAf96nMAtFr-jMvrIbWx_r2uj_Y3Rf2WPImf2lxrgt9u1bowIxDPbUgPZ67aZB3_NXIYr18P9A0tZG7lVUoAC4O5yQB250gFyeeSToBFtd5C6J3H9QosbX2kBD0gLTDUNeZeb9obZ9wm3c1eqQSRFqLuDPHAPDRkJJ-4RuMMyzBmRfj5OdTSRk2x0-DOnrN89hQEsx1-j91xBGVl2UGt2gg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 03:29:18</div>
<hr>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNteQoq6g6rfefkr5xXhhIMNPPgddpBMHjun_fTPe0dnJdj0GZXe_jqZ7D13-AZAnHW628FtV8i7qfB6WkHQzTv-jYwPE3d0xTl0wEK3h_RfqeVFPgpq9HO5YB3N5olI7Z7oepcg_9CC8ijFNiv-1OZ0hS5i4MTA_L16JvTz-KIzX3HG4uUjaX5ks4_ajSxXWZwOp3KEIlqgA48yWakEF0l5Y5HNNBO5Zxz3cgh4dmjN79zvtxJ1PCKCK3yamQmW3E94mgbboAiBiV1m-oAJMfSjO_Af0m0tzgrxFd7ZZjz9fksnaPn8Gm9eUm_rowMgIZ3Tzqns3Qqmzu0CWxpcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrTCBew1dAIgzTFSDvpBFv1o5k2jdK99eiyi6jZmki96Icqe0EehX6WRrcy7SWxvk6EVpoBOO_4JDWvXqF6xF1xWc1fa82CHrANl3wpR5OzXGN5qLlsgkAYToOl8g0duT4GuuEOqKZIQV2c-J-lZp4A1i5DBm251L-dbBW4VaNzEa-XVPlvak-nYlj42UE6TEZ_xsYjW-HdKKqq3T0c7leio5bCJDD37bvY74sepsRzKBCv6Qf7OR9bTDVGgC02JhQPzDOb4D1t11q78DKYqLYzaKHE0lXuhLPqwW4fCZfAJ9QoeSmriqINFzu8es58xeJ8BhTTf_QxMH8s7s-HNew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFLVlWaxwxpMMN1Ylt3zYNsNozKvW4jfZNOmsZvFCRGX93MOKvwqWJlduPWbM78hOC-ARdMWPD2X5ULlowizJei8f2twk2NSE_OmdTs4pnGCRI9GRUnm0-tYBJeIpr72npcrU36jPdmoOqeux8uHsq5kLAWE1MBlMHqU8tmaWsQPHJiLhyqWLEur4KLuvA1qocHkl4jLvbKlhpMdgDZNHLcfZW4_UsYvvGACM4FgJqy5QCFmlgqh4PMhNuhSz6i0RKrrhBDXEl8itwf67zXmzVio8XVfrrWbTzVwaJisiEHilI1qTUXzOUwBbVBTLN2UdugwdXNLesdeRVLMAhWeXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=AXngPh8eaw47XexD9_V9Z6n8wtAEyveXGlOCq0qsH6p1zQZRKJ7O02_M1ga49y3uxQOym9gd8Lod7PS3Wo6NcOoyP8ZePRK-dJZZndL5ifS9B190qyLoxaA4qzNhWFujYdIOwla2FWUq0LW8Ol_Nhg8FoUgYxum4lNcNIxL2h8uxHlDsrMz8lpMITr9oKveUdY2gtit4DdUYye7iSXt49Di14v1oKpDLCEtbcKo0XsnmBXXRtCpOnYYJSvAwRyjjkUesSa5vVBHUg2b31X4KumZMIETfE8diO8GMO8TOXDciCTDe-JqCE5badANtOGIpqu3QouS8BIpxa_8BGxXxtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=AXngPh8eaw47XexD9_V9Z6n8wtAEyveXGlOCq0qsH6p1zQZRKJ7O02_M1ga49y3uxQOym9gd8Lod7PS3Wo6NcOoyP8ZePRK-dJZZndL5ifS9B190qyLoxaA4qzNhWFujYdIOwla2FWUq0LW8Ol_Nhg8FoUgYxum4lNcNIxL2h8uxHlDsrMz8lpMITr9oKveUdY2gtit4DdUYye7iSXt49Di14v1oKpDLCEtbcKo0XsnmBXXRtCpOnYYJSvAwRyjjkUesSa5vVBHUg2b31X4KumZMIETfE8diO8GMO8TOXDciCTDe-JqCE5badANtOGIpqu3QouS8BIpxa_8BGxXxtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/afGFBusJx8UNBcKESX3zNFv1lIx5DwHbgGUX-SU0oDLF9sgGtMT_VhpbhjvgeAw9bzCrlnnztS5Q-Hw7WaRX7OLaFBiJkm8dTTvNF4KKCiz0AcPMTbq46ysNYC92zDkk2gRlSn-MZt5YFZPGG1iFujrgDs91yjrFjV-c_U9VGM-lY1Hlw9YN09bdieEd-wydW3VgEdPpLV2fqstiNnaSyVlioeLYWqAjx3FxrBJUPA7LdLT-B_gSNsvmsHagnMV5y1CsPRIz6R1-QAM59CYHkxd5k2JoxGoa7DMPENAkKz7rTaJxdFNaJ-dOuq0m1QDdw0mFDL3Eva-_JdSKlo9r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AgKw4HvxKuTN1fCQ_gFgii0tX4YTujibBYKq635RGKNTfYDBANynFiLpEx0IwI2TXIbiffZx6f_4v5YCFgId3x-r4yQiZm65ZehlX7ubcI0Py_rXHYSMlpbvJmK90XNlR14CZ2p3vHBLL6lwkPgJLmbdAIUcXDk7VlJLTo9XpQUTyJ7bvppIwL1N_Hu2XCSUCP-OeEYuicGgL_2D6CWM7C4PkhBKVDQK2s1S9FEIbQCuK633eHIus8jUl6vQhq4NEuEM12kyxJEc-VoKS_Bfo2Y5gDaCCFb2sBnhlNywTcrcTeFb_Wtofh1lOU-kcBnoa-jn_HVHFvQXU8HzjAdkvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzZgDyVNU6yw33GxO4OIl0OIT7jNI1GWZdcZQ52j5-wbxN4v05b735-tZFYo_JWhUHt61oULmecpVKCcvICF6Mf9eKRVD3HXVRTAW5EjphGfoJUeOuCd2aqaHWOPoVm3gRQUTbAD3Kvl5mTQ32ahSoGLHSItS9xe0Ex7rxG-BaoMgVCOpefU5uCcdeBAuE7RTJ5F-FY7HvadlKsvFc2ubAMx6raXpYSIIEv0netOyTwQ44ev5bTJNYWdsjLDYcNA2epXWVnEWSIl18YrbgyGN3B4KLje4nsY4R3390GolztinwDRz5PvASyMNBouzOxdg2FRoIrDv6AwMQkCzJwSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKf2iyvXACN3Q3_3pFmYwxQEpN4GlJhrVGpYcX9csdqeOyhKRWpgsG9CS03BLqUPHLppucnD_R7qHDFbh8l4zGr-kGdzlzjrjpN6QACLx-H7SfEcDl9s4jRsYXLWxKE8tLfLMsux1kNKxkgYIWll4glOrnhK2RfFRygcyAKYXSgLvVENmuqrJMzvsBo47PLdydCJt1icOkTmrafHeQdi5Uq6bPvZ-QaVw9PJtFmUSq9AjGatNqogK1DIC7IDgOnloDz3Xyv2TW4QmUuTuX6LsUhAouij9GNzmtAiq-TUr6uaE_y1EYxbmtofTomOxrbFkR59mlnvTJZBVj77opJP4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihBlVhBVkw-RGItMFrbVx2Cw6e2uXTKJO0YUyRKyS3TfoajhQ6ifZ7qpfqWe-B4Ex1s8xb3eBYEJW0Vng6XNcq0p7STwcwoCLgwYHhxm-iP6ktw1O0EvW_clqp_SJODj2NAB2YiajmBSdJzcj7BrBeC6z4WVOBLpg6pJ-ET7_4zsDgI7AMmf8rpMHBV1IkcVJd8bh4kIEOKGpdqA5OUbJCe3lRAQ1t8TB9N-50l33na3G68e9w7fFrmVR_6kJmp7SpWZitIP3LXm3i71qBDwCXrN1Ib9auIm_o7BsK1rTnkifI3wQp3wU8keNwcL8oYKL_6rFYtvSiyKJi50LfY_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HvhHtmQQsGmGyGMxSPaIKlbxo9OxNfkGPO1zhmbTDCMgdc-YKG_7MUCtGWZAJgG5EnORy8hZGZCUbGXhNzixbJlkl-hoA9Hb02jkiMG-dLGb3hkjl3PKGMr6wSATMXDnUfk1U5UphXORtJ-40z1bsx3b2_GDAni-shtzLzYSbuVSzOzMn5kIeAbmPp6SwdzM0nRlJ5JjVRaHWS5RssLjlx5LlvWbNHP6O4Vyv91XjIj4WgXujbs9CFH83IyYO0VbSkIKp3VOKM2wfMsWBMBlZir_raTNEVYGlMtjuFVt-d3ocEB2YX8YuESWRSOoh7rAWcjxaKYhX3atJj-TkoDm2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=kvzDo-OUQ2wI4qrJqcBMy_6Tck9EdoHl78iy1hFblyAU3gpbxV6Rk2XcFqDtB-PKASEalfwyXGLDQS5D48JXinljr45wCqnTxa5ynAfZ8jn7cblgoFmUrs2GlxVJlBFC3kb6L_V8-Ww0vxTaUQVba4NrDKTd_dqoPUTEzC0hB8M-uXpqwdZPFP2gN757dPqE-3Y7mB4VXWglWczWwOrVzoII18gu6_dCgoLTM9qIzpbZyzAfYJjy1PJykNyGEqlaatRNpKuun32JZ3Uf4s3LdwZ3R2OruugDCqPmQYZwIYWvak5bR4pMXdNDph2uz7MZB7FAo27Eq7U5YfyHffvH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=kvzDo-OUQ2wI4qrJqcBMy_6Tck9EdoHl78iy1hFblyAU3gpbxV6Rk2XcFqDtB-PKASEalfwyXGLDQS5D48JXinljr45wCqnTxa5ynAfZ8jn7cblgoFmUrs2GlxVJlBFC3kb6L_V8-Ww0vxTaUQVba4NrDKTd_dqoPUTEzC0hB8M-uXpqwdZPFP2gN757dPqE-3Y7mB4VXWglWczWwOrVzoII18gu6_dCgoLTM9qIzpbZyzAfYJjy1PJykNyGEqlaatRNpKuun32JZ3Uf4s3LdwZ3R2OruugDCqPmQYZwIYWvak5bR4pMXdNDph2uz7MZB7FAo27Eq7U5YfyHffvH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBveMzQQG-7ue1eg_7sPCS9Gs1lDfp1UQvbUtiJaqhs43XfEx9y68bl8L1BaewzQ8IDTBZY7xspLfcBETvX2eQIVbsbGe1jC98oZnsW9e3EBYO2urI8wLCPtiA65TfSsuCxonCjBmQdlPi_6KQINGSSM_Dw4Kxd3GGBBfmfd-9stHp5w-WZGhwdVwNLHFcfvzVb6wX0URXyo7XMSfGedTEqiN0QioMsI99sGrLsYQUNtpexLansJqzD_8Q17uKdYuB3ZcuvtrDULhx-HRJQ1xTRV0rLQGD_h86QOBChun0H154SWEiJUeoAE-P5qtDyMFdFVeVY8f0v_wLedR2UL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCl37Rq-iUihOSONMLsxd7cvd3-iX40m-HOEQJMExfKD5nSNdcGBhKVfOS5awT_TqEpkLFQz5cyyRkYW6YjDgezFrG1mzdbICC4s3PWsTuS9ctdWlwNnqd93LZX3KwNhjjGP5UBV52HWTfBARQIQzNL_pbzvYC7FfedDY7hYl81IiC_ncR4YGwTqhLoNUCFgG0pDp1FUq-YY2Sr0R_Jctt6kBLNIpAi00Lh9Nj1Je7KOXtOHGMGnimIzLSL7rH1d1o4OKNTMEO_yB4MbtB8g16BRZpOWgltScoGfXEXl0RVs5BeyRjDVs__RpqTFiDEuQ7bybPSFQbUyAlIXeF4rvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQysQHinqsomKPqVYfoXclJPvQYYuRTAjiLI8QzM8dW0ejgAvbrgk3A1PTOcc0vn5K6vaD2LsPhg3_y3WkW74JmVXAUmDPMWRvtEMG8m8qNsjw4IOMsCmz3xmtiB1eFXEz-m3zzapXX3AAdxKmF2fHl44u1NJd2cL5rjjaFOYlTT-4jKPOX7HW_yr2V7uuAiChw4p48XMUYTvTj4DAzqpPxLa6VDPSKWCmganQcu5n2rFzj6EQk-fLhHRsZYMgBFRFi_xY9ltEktiFgjatJDzb_hbHZ4kLtrIK-IjnHe_4CnTrEVTQlrxHglFd5PaEjpzihwQj9qI7hWtLhHaNer4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=Q7rVk4BJrHc1qLZs6P2jEyExMacIgU_HI6ubft0Ob7YxHNVzRYVZLEKXPDnpeF34mnDsmzk8NxVyANtdUXnnpgj0rIRJKIMy_pPbEoo97s61XrXoeNkHEkocII4uY8y_miDgyy8ymFE-2KdHKIbL-20dQSyVZSixKEx6tMOBmCAcVBzy95s_YGlJaoDf26mkKg5qxC2Yl5U8NPisqMl_5gnE_XYbMmjRpx0Xb2bMIiyiIU8MEgOFLwEyl1WOxYPp4wLkAfdC7911nWdPN83fpsLpFsE_OjTQ8wWF0vt5QjyeNpc5rqR_P7VFftKNwvRewYUVssaXG6za9uHC_gwmyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=Q7rVk4BJrHc1qLZs6P2jEyExMacIgU_HI6ubft0Ob7YxHNVzRYVZLEKXPDnpeF34mnDsmzk8NxVyANtdUXnnpgj0rIRJKIMy_pPbEoo97s61XrXoeNkHEkocII4uY8y_miDgyy8ymFE-2KdHKIbL-20dQSyVZSixKEx6tMOBmCAcVBzy95s_YGlJaoDf26mkKg5qxC2Yl5U8NPisqMl_5gnE_XYbMmjRpx0Xb2bMIiyiIU8MEgOFLwEyl1WOxYPp4wLkAfdC7911nWdPN83fpsLpFsE_OjTQ8wWF0vt5QjyeNpc5rqR_P7VFftKNwvRewYUVssaXG6za9uHC_gwmyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=ejywKr1HLx-qdCSynFjwEsT6CD8uIEzPTlAwbE7c8qDdp8CajAbct_oPlc6LBqG1-KaDHn7GVzEeEbuhzkNrC6FhEVcPNjGUYz0IvUgC5PxESmb0eGSsolyVcgJKQxkGz98849m0Ey5leBRIJP2VO0Rf9VhEjBYxnqqZMgZ1dRQdYx_rv8YUGJdWyp1m8iYFx9oU3NGQe505rFP6YWNUVst3pTO9NTQ6dqWq8cy9hPhmL-q_wo0lBiwlDEBU0BERhrkH8KZJE5tIDBpe465WvBr8vOZWeJCSTrIWYKgchMNP8djk8r3pdZGu47OPAziifviJ6iGhyIrd0uzC-nGrCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=ejywKr1HLx-qdCSynFjwEsT6CD8uIEzPTlAwbE7c8qDdp8CajAbct_oPlc6LBqG1-KaDHn7GVzEeEbuhzkNrC6FhEVcPNjGUYz0IvUgC5PxESmb0eGSsolyVcgJKQxkGz98849m0Ey5leBRIJP2VO0Rf9VhEjBYxnqqZMgZ1dRQdYx_rv8YUGJdWyp1m8iYFx9oU3NGQe505rFP6YWNUVst3pTO9NTQ6dqWq8cy9hPhmL-q_wo0lBiwlDEBU0BERhrkH8KZJE5tIDBpe465WvBr8vOZWeJCSTrIWYKgchMNP8djk8r3pdZGu47OPAziifviJ6iGhyIrd0uzC-nGrCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kc2LpyLaguGV-1CJ4Ce2QItIdYQ98UqbP8LoJUYfd-5T-IufyYe_iA6Wg3cIyyr7UlQQYymsaRlajcxaTKzlaKHYj7Nm-3VQkHtQrTdMH5gJwUJni80QkTqWbmchfBqtjfG9BSCgKtWNzgDRQ2l_5QZiEsHBXhsR3xN6wC6mGCjrBo5HXukq1rRNHy_hr6cU09nq684KWDN13LQOdYaoHlxn5C9-Hcnsc9od92duJ6LY6ZR675x3SK84PFY-AE851ug-F46UTR_O3PpQMxkQCJXWojKAfcpmNHUZ3Wu_4xvq4OuliXlrXgUlKHAV2BGhr2KRTKJ46SljybmgcV02OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرَک | کوتاه فوری</strong></div>
<div class="tg-text">پلن های اقتصادی موجود شد
🔥
10 گیگ => 1,700,000ت
20 گیگ => 3,100,000ت
40 گیگ => ‌5,600,000ت
درسته که این پلن اسمش اقتصادیه، اما کاملا جوابگوی تلگرام و اینستا و یوتیوب هست.
سرویس ها محدودیت زمانی و کاربری ندارند و بدون ضریب هستند.
خرید:
@SorenaVpnRobot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FylPXBX8GO1esUHdTXNZbjEGbpPavj7zfA33v05ekOdJuICuUH2iN0lS3_C9NKKPMjQIDNpvMj0xrIHJ3kWJXBhVWMuiHUN0nn_cskvBay9_Q_D_gmyPckJH6qAgfO17P64Se4HlKOg8V9w034ya2Fss98YaO52U4w_dh3TzlccMozJZph27OVlUvGyLZE06TUPEt8lz2srMiRuDDQo4hgrMKCa7l7GUaS4WtGKZ1PofDO0C7cH4S0VqS6h8vcQywSuAypUOna4gfAuvHw3G0irT1KeVbnb9mrzh2fCjQkJ4zQCzvJ_ywOwmwALJJtbZT-gsW1p6Nmo4GzAscMg4sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmdwetqA5fieyb8X9GhmInVez8gRMX5JFqpTvogz6tn04O4wi2cZPet3nacORnnG5YDYUA9OHbDmREGpwy8hIcPt3zKo45by1OWTnRmMacEeh8epWBn-DSpZE8AdVax1gWc1oqWoZvyklItAV_7Qrv3U9FOXK9UHDf3AHUtJ8f_oEdr-C8sWvtzFi5CEnwGc1GIKStpuQID30khvvR0S24aXe9C_daUX3zIZ8VBntIIQO62GxFA238vVrDQPOHedmrt1vhti8D645klDRJWGIDxuhvKjOOsa5_9N5pq4NObhoKSZlSMoS8Q1mHYhz48vaRgHDCCRZ7uANvx6Bym6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnOaP2beaJ8DC1ZilaPqBNwydMsPA7oMOP0K5hsMZ3IatRfkFfv-4MimT7QDotz0SeJHBsbGhMgG2SH2B-NF4R3bc2za1ln8j3w5gLfHE2NWtzBOGG5hEcoqfcemKHA3h9xLXn9Lr4B101uFH8Xg_uL5YkftoVY-JArR1scn1hqtc8AluD3faH-u6dimRQZHHSW43dOWcGY1sIet4eQCm4CNPs-eEN-9PbfO_M-FFirc9rGSBpilKd2_W7BqntfL8fWGy9h27sSe2QT084DruCkSLv2xbXSDf02vqQN8sHsyipCStwMvR80ag3JDzT3-xV_d0ePVSFNI37JXkhL2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAru_dVso4z627I_Rd2oQgDDAxh_AfmkOYJHZGrKELuf7dtpp_nN6ure4r9Mm0aIy7l0vFxBIhH-HMGb35tSXCWxh6WdGGArIkhq6D6JsVOR1ROp8g2K1aRJLULjL1yVURJXL9QbKHKbQ_3t8O9Zs-BxzgAEr4hdRBhIi72kg28wiD6Tr7bD7IIxTpzoRaxgCKChJh6-DrPYjohWuqAAPiQsEMwN5QXdCWM-7OfLBoCZuvugCRUd4enqwMn6N2sUBf57XvHGXFktkLkoA4Yd8YbFUq912jBYNM0AaZmWlR85tJTNrCM73jaHMJdClAaWijFiQWVjtO0WBurD-4K1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
