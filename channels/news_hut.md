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
<img src="https://cdn4.telesco.pe/file/rmhR-pt7VCOseGnZ-LR0iqqbVHRRFxKFBsTqTSrdsQHr3ZV0eQ1F_796uf17-MaPAPxa5KnEdtYxfDsW8xtQ0dGNgTV3XDE8BHSPeKUgH0JuYI6RNNJzZdIXIRkK83QA81LZL57maFFSVYVnNSSls1dJB89sD0AzERFZ8i-Fl9aUikDRgGgEJhoQv-43Lu10Y5tJkSFRSgbNDg29LTX8l1J7-FG4O22MthhdzmmYm-nSQ76x8S1GLcbB38DEJmDxwZ9efmqB9GhKj6Jj3CsXQ-Y5ksJ9DcOnZJX7JWtn8OzGa_TC2qR62n2cjvgziYbX1Zebh7QtDT83PKEIsIgNtQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 22:22:59</div>
<hr>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/afGFBusJx8UNBcKESX3zNFv1lIx5DwHbgGUX-SU0oDLF9sgGtMT_VhpbhjvgeAw9bzCrlnnztS5Q-Hw7WaRX7OLaFBiJkm8dTTvNF4KKCiz0AcPMTbq46ysNYC92zDkk2gRlSn-MZt5YFZPGG1iFujrgDs91yjrFjV-c_U9VGM-lY1Hlw9YN09bdieEd-wydW3VgEdPpLV2fqstiNnaSyVlioeLYWqAjx3FxrBJUPA7LdLT-B_gSNsvmsHagnMV5y1CsPRIz6R1-QAM59CYHkxd5k2JoxGoa7DMPENAkKz7rTaJxdFNaJ-dOuq0m1QDdw0mFDL3Eva-_JdSKlo9r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AgKw4HvxKuTN1fCQ_gFgii0tX4YTujibBYKq635RGKNTfYDBANynFiLpEx0IwI2TXIbiffZx6f_4v5YCFgId3x-r4yQiZm65ZehlX7ubcI0Py_rXHYSMlpbvJmK90XNlR14CZ2p3vHBLL6lwkPgJLmbdAIUcXDk7VlJLTo9XpQUTyJ7bvppIwL1N_Hu2XCSUCP-OeEYuicGgL_2D6CWM7C4PkhBKVDQK2s1S9FEIbQCuK633eHIus8jUl6vQhq4NEuEM12kyxJEc-VoKS_Bfo2Y5gDaCCFb2sBnhlNywTcrcTeFb_Wtofh1lOU-kcBnoa-jn_HVHFvQXU8HzjAdkvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzZgDyVNU6yw33GxO4OIl0OIT7jNI1GWZdcZQ52j5-wbxN4v05b735-tZFYo_JWhUHt61oULmecpVKCcvICF6Mf9eKRVD3HXVRTAW5EjphGfoJUeOuCd2aqaHWOPoVm3gRQUTbAD3Kvl5mTQ32ahSoGLHSItS9xe0Ex7rxG-BaoMgVCOpefU5uCcdeBAuE7RTJ5F-FY7HvadlKsvFc2ubAMx6raXpYSIIEv0netOyTwQ44ev5bTJNYWdsjLDYcNA2epXWVnEWSIl18YrbgyGN3B4KLje4nsY4R3390GolztinwDRz5PvASyMNBouzOxdg2FRoIrDv6AwMQkCzJwSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKf2iyvXACN3Q3_3pFmYwxQEpN4GlJhrVGpYcX9csdqeOyhKRWpgsG9CS03BLqUPHLppucnD_R7qHDFbh8l4zGr-kGdzlzjrjpN6QACLx-H7SfEcDl9s4jRsYXLWxKE8tLfLMsux1kNKxkgYIWll4glOrnhK2RfFRygcyAKYXSgLvVENmuqrJMzvsBo47PLdydCJt1icOkTmrafHeQdi5Uq6bPvZ-QaVw9PJtFmUSq9AjGatNqogK1DIC7IDgOnloDz3Xyv2TW4QmUuTuX6LsUhAouij9GNzmtAiq-TUr6uaE_y1EYxbmtofTomOxrbFkR59mlnvTJZBVj77opJP4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ikcy5UWeG-HIdYc0o225sepRfC6H8NZnMOvU4aALaPcPPZ7VFe-xB68u-iESP7E77RnmC0Pp7OKnkwAKx16yVMMsd8JYZG85b6eCVtYDHWybEfKTOxQviL_7ERunUcbQ2EfEX8X--WAmHw1QJnhtBHUCq5v7daYpet4hJqKi5HKQdAGk_HeqgP28iCXwy0m4cHQNgaEZy4LwysT74yUOsYWNxRNRmcDWCot5EHu-hOuNDwmnko0De6I7Lrl9R4LKFwehU4xs-ty6AYFILcFGyz4266yUudM6h5Mrs_67uRVUAVf3TjMQOZj3ry93Cz0p6P-ycxETSVTW2DzryAga0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HvhHtmQQsGmGyGMxSPaIKlbxo9OxNfkGPO1zhmbTDCMgdc-YKG_7MUCtGWZAJgG5EnORy8hZGZCUbGXhNzixbJlkl-hoA9Hb02jkiMG-dLGb3hkjl3PKGMr6wSATMXDnUfk1U5UphXORtJ-40z1bsx3b2_GDAni-shtzLzYSbuVSzOzMn5kIeAbmPp6SwdzM0nRlJ5JjVRaHWS5RssLjlx5LlvWbNHP6O4Vyv91XjIj4WgXujbs9CFH83IyYO0VbSkIKp3VOKM2wfMsWBMBlZir_raTNEVYGlMtjuFVt-d3ocEB2YX8YuESWRSOoh7rAWcjxaKYhX3atJj-TkoDm2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBveMzQQG-7ue1eg_7sPCS9Gs1lDfp1UQvbUtiJaqhs43XfEx9y68bl8L1BaewzQ8IDTBZY7xspLfcBETvX2eQIVbsbGe1jC98oZnsW9e3EBYO2urI8wLCPtiA65TfSsuCxonCjBmQdlPi_6KQINGSSM_Dw4Kxd3GGBBfmfd-9stHp5w-WZGhwdVwNLHFcfvzVb6wX0URXyo7XMSfGedTEqiN0QioMsI99sGrLsYQUNtpexLansJqzD_8Q17uKdYuB3ZcuvtrDULhx-HRJQ1xTRV0rLQGD_h86QOBChun0H154SWEiJUeoAE-P5qtDyMFdFVeVY8f0v_wLedR2UL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCl37Rq-iUihOSONMLsxd7cvd3-iX40m-HOEQJMExfKD5nSNdcGBhKVfOS5awT_TqEpkLFQz5cyyRkYW6YjDgezFrG1mzdbICC4s3PWsTuS9ctdWlwNnqd93LZX3KwNhjjGP5UBV52HWTfBARQIQzNL_pbzvYC7FfedDY7hYl81IiC_ncR4YGwTqhLoNUCFgG0pDp1FUq-YY2Sr0R_Jctt6kBLNIpAi00Lh9Nj1Je7KOXtOHGMGnimIzLSL7rH1d1o4OKNTMEO_yB4MbtB8g16BRZpOWgltScoGfXEXl0RVs5BeyRjDVs__RpqTFiDEuQ7bybPSFQbUyAlIXeF4rvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQysQHinqsomKPqVYfoXclJPvQYYuRTAjiLI8QzM8dW0ejgAvbrgk3A1PTOcc0vn5K6vaD2LsPhg3_y3WkW74JmVXAUmDPMWRvtEMG8m8qNsjw4IOMsCmz3xmtiB1eFXEz-m3zzapXX3AAdxKmF2fHl44u1NJd2cL5rjjaFOYlTT-4jKPOX7HW_yr2V7uuAiChw4p48XMUYTvTj4DAzqpPxLa6VDPSKWCmganQcu5n2rFzj6EQk-fLhHRsZYMgBFRFi_xY9ltEktiFgjatJDzb_hbHZ4kLtrIK-IjnHe_4CnTrEVTQlrxHglFd5PaEjpzihwQj9qI7hWtLhHaNer4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLpPWhm9496ltama2WgI919X2ESMNLyIXsikV69ZUF7z0R52xeBaeu0y-sFMNDJoHGu8AK-05SXFSWtfxOYwLBE8W_uhyWdByZ3WHFRBfqJ_Pv7Y-LC8oTS_gGlqCZIgQy8X6d3dQhGF5UqIidhKel8X9KdHjh-jKzijW-kQBvCcEben7_d2GhGOKFf0dD98zP54gMu0rSdfxwBfdJ9Zc2oQStKOqpk2Ndhlto9sK59bgqBgRRb6JlpS1GQxut6CiZUnxUR5h6jN0MKh9TT1CJ6b3DrtgLhUxAQL-6gSynT3WfvETv92VZ5sqvXktbVlKLcz4IVQDZnQopkK6dzqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64887">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmdwetqA5fieyb8X9GhmInVez8gRMX5JFqpTvogz6tn04O4wi2cZPet3nacORnnG5YDYUA9OHbDmREGpwy8hIcPt3zKo45by1OWTnRmMacEeh8epWBn-DSpZE8AdVax1gWc1oqWoZvyklItAV_7Qrv3U9FOXK9UHDf3AHUtJ8f_oEdr-C8sWvtzFi5CEnwGc1GIKStpuQID30khvvR0S24aXe9C_daUX3zIZ8VBntIIQO62GxFA238vVrDQPOHedmrt1vhti8D645klDRJWGIDxuhvKjOOsa5_9N5pq4NObhoKSZlSMoS8Q1mHYhz48vaRgHDCCRZ7uANvx6Bym6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnOaP2beaJ8DC1ZilaPqBNwydMsPA7oMOP0K5hsMZ3IatRfkFfv-4MimT7QDotz0SeJHBsbGhMgG2SH2B-NF4R3bc2za1ln8j3w5gLfHE2NWtzBOGG5hEcoqfcemKHA3h9xLXn9Lr4B101uFH8Xg_uL5YkftoVY-JArR1scn1hqtc8AluD3faH-u6dimRQZHHSW43dOWcGY1sIet4eQCm4CNPs-eEN-9PbfO_M-FFirc9rGSBpilKd2_W7BqntfL8fWGy9h27sSe2QT084DruCkSLv2xbXSDf02vqQN8sHsyipCStwMvR80ag3JDzT3-xV_d0ePVSFNI37JXkhL2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAru_dVso4z627I_Rd2oQgDDAxh_AfmkOYJHZGrKELuf7dtpp_nN6ure4r9Mm0aIy7l0vFxBIhH-HMGb35tSXCWxh6WdGGArIkhq6D6JsVOR1ROp8g2K1aRJLULjL1yVURJXL9QbKHKbQ_3t8O9Zs-BxzgAEr4hdRBhIi72kg28wiD6Tr7bD7IIxTpzoRaxgCKChJh6-DrPYjohWuqAAPiQsEMwN5QXdCWM-7OfLBoCZuvugCRUd4enqwMn6N2sUBf57XvHGXFktkLkoA4Yd8YbFUq912jBYNM0AaZmWlR85tJTNrCM73jaHMJdClAaWijFiQWVjtO0WBurD-4K1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=fq9sW069OQXrfc7CbZ2avoMRvButLuRWhpKiHrQ-RDB4FZ7sPspUtfKeJNodHvZtsXU_qv3BFIiVH__Ma1dH7Ge6-QMF4GHgRlITkQNsTkjjpDHSPft7iRujOucuxDc15Yt1vDnzNSrQzvf18bGp1QSzI0Zm2wRC460RsulPNxujifgcyBhfDptc2Mu3c4eRRN5Lj2zDxyWcz7nsYHFAH5CviPbP8aItas2inFvPBKNacfHTY_OxAHOIpuqIencDaf1Gjm_TDKKKMORrLYN1_d01WHIVa6AKnC0Gr8Kj1J-TuXZ9r42fssH0NAVaiN2fX118yEqkZ5rDfCBKH1DYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=fq9sW069OQXrfc7CbZ2avoMRvButLuRWhpKiHrQ-RDB4FZ7sPspUtfKeJNodHvZtsXU_qv3BFIiVH__Ma1dH7Ge6-QMF4GHgRlITkQNsTkjjpDHSPft7iRujOucuxDc15Yt1vDnzNSrQzvf18bGp1QSzI0Zm2wRC460RsulPNxujifgcyBhfDptc2Mu3c4eRRN5Lj2zDxyWcz7nsYHFAH5CviPbP8aItas2inFvPBKNacfHTY_OxAHOIpuqIencDaf1Gjm_TDKKKMORrLYN1_d01WHIVa6AKnC0Gr8Kj1J-TuXZ9r42fssH0NAVaiN2fX118yEqkZ5rDfCBKH1DYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=TD5iHzNJGEo80JsOXvhSIUFEnDhejeEDlovH4ZhzNaMUKVhclA4V5uzdv-YKynvjBvlXnjSmefxgilXdsMQfcdRsv6aVcy93B49VuKMdHvIJsrA_Zu__PBXJGeDI8qpVCI-ObSsVZNJkRfcR3Vh4OdeRNWjEYV0-ByyqqlstDW2rsSazbViHMMG7HAr5DO6bAlT73g5kRjhbv7EOsxc79zqSRcZdp7f8VeokKtKIEHeDlpolxmy3tkemu5aF5Aqv3SVnlSOqXQQNyg14GzWEaE6e3Mlm3bAtDQBcvberuKyTWgB3j2xwcqPAmz_PKbLO61utqAKSG07Barl39ayr1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=TD5iHzNJGEo80JsOXvhSIUFEnDhejeEDlovH4ZhzNaMUKVhclA4V5uzdv-YKynvjBvlXnjSmefxgilXdsMQfcdRsv6aVcy93B49VuKMdHvIJsrA_Zu__PBXJGeDI8qpVCI-ObSsVZNJkRfcR3Vh4OdeRNWjEYV0-ByyqqlstDW2rsSazbViHMMG7HAr5DO6bAlT73g5kRjhbv7EOsxc79zqSRcZdp7f8VeokKtKIEHeDlpolxmy3tkemu5aF5Aqv3SVnlSOqXQQNyg14GzWEaE6e3Mlm3bAtDQBcvberuKyTWgB3j2xwcqPAmz_PKbLO61utqAKSG07Barl39ayr1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o39Q5maefucikrpewjaMZJLwwfdK1MMkXP2u_faPmadv0jqo3UD6Opk35mbskjNLSQfxLD1Oukz_mwL_ICVgglD4d74h29s-RKk-hm80bfqvdrwCTB-Z2yH8NbMbWMmkpzdDcpvP0LpIylsDPZJZKlLHYe6YUhuY08FVHjKT12Ph6frJjHZUfYpsgh8nqiVoR4JMQXAQafwLfldl__pC8s-EyH1PRw83vOPYm-zG90KovD0QWuFvcRtiCWoiQRI8ZSwwj3sLRkCMV1Ot5CgnYPlcWmGfi-nImeLdPdyViIDxfNcwtkxgMvdAXaZND0G8HK-ZViaUr1X3Pwk0k5ml2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rbzFemye1kiy9Q0c9IN4gXnMj9AcmHtpo1ZoFIeGLHOD0Xyh5eaaqqBcB4MxUJUSH_hnG_iKA7ZspEThkqKQ07ZzeXqoMyTgW34Kenzl0b7X8RVoI_o0P3vDSEI4M4QQGmYlUudAZQtrQ-AgGfZGYmYRqIbm0Kg2t7uBEAEl-GaJEkKVIfuSZb2MoX0sOW4LtOgcYWvow4Hm1IrDR_JaFK3IFLiLijVaLH9Dxo7qL3ycqzgLXItw85CUP7Uzde0m4sveFFozWKN0b7TCY0ShCGroAWwcFFKyrESXgfWgmWsgQ0CLu5_s5DB8WbTT_fVuT7a6Lh71-lVLPcek85aMSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGMoZNVDBS_mMPOi8gnRBOc-miobuPlbr5_RbepbSj891UIBH4O9e0q4PvZYJ43NUFINpu9cyu_jK5y8hJn4xb1aWycQkLRtbOCTumVxLBpPuIn9TwgWdmgoy9Tm2-GAUv7jzR_UzOCfmpSd5x6pjs-b-pEkKx0eHEVQPOGwloSKQ7RTum5XQiYLZYLeHG3EIMhSrgtwMgSi30uQ2SrN_yYmPspLAeqFgyX_MaHDW6SEsRjuoohf8GpIEdYBy-hHoyPyhBJUlYLLxAtW2wdn_kl0AGcHaeozLn9ZVcvfquvSiSZ1bjG6il7Nkv6Wj-uqQRAo9JGnP4nyL4dhGha24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRa5NVWalaLvwA5hfxlPNkHhOlPhzWAZPPoOjkEM71M4UGYnZ4TMkMbz7oDm2qvbW4Y3PspBWW-R52gMhclqjHxYpGZfMXd56pEMc-NSHmvPh5-5R_O5fqFJ5FiVh5AZxZjE8pDFx1LYZsHpvQp2caeDJbSX4hGeoP667_z0eMV4nYgcoTSRwx_WWGL0w2hTM4iW4bMjrQOFZt36IC9_STezW1lfwBmNxlgmjMXAsRZXKlgxOMFnFpt0al5LwxVUul0pWzRnLb9-JYs5Ac1pvoft7ApYNtGAH3ZSUcBctQjRHGU6JNbB2oRvSy9vE0AMlCBJM8TbpdKEYmNMWd5aZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=V7659D_FbgO73Rsr6wi-sA0682R7scLUmmX26DkDSX8IHS9cmV2a_nrs6owEzuOdejnuBpJAG7mQk7w3AhbqQx_Q7al605EvpR7y42gJZoxkEqmbHBCUcFSPNNMJbGL_8lDCWqLvYQA45Yp3QbgeuTn4XTijHG_xO_IOdXH69jV3eZ8S7eayJ3Mqrw9f_mm0Qqwsu7Fiy-eyO78mB7fUnrkk-UVPDz0qnhxUbVnyXMv7mVLcv_qkjDkE0jAdzZ3SHtYkiO0CiMEaNrgLdTMkL6Ff6C1IYeXMRdBVkcaR6tE1fvj24IhdseqP0CmQiLhvJU7VI1Jm4BhjcBW5fEQDMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=V7659D_FbgO73Rsr6wi-sA0682R7scLUmmX26DkDSX8IHS9cmV2a_nrs6owEzuOdejnuBpJAG7mQk7w3AhbqQx_Q7al605EvpR7y42gJZoxkEqmbHBCUcFSPNNMJbGL_8lDCWqLvYQA45Yp3QbgeuTn4XTijHG_xO_IOdXH69jV3eZ8S7eayJ3Mqrw9f_mm0Qqwsu7Fiy-eyO78mB7fUnrkk-UVPDz0qnhxUbVnyXMv7mVLcv_qkjDkE0jAdzZ3SHtYkiO0CiMEaNrgLdTMkL6Ff6C1IYeXMRdBVkcaR6tE1fvj24IhdseqP0CmQiLhvJU7VI1Jm4BhjcBW5fEQDMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONAgvTBhu1OENczD3RD5ZUqFFBeeAppdT-rEoltxwag9GXWP3xSY9nHiVbN_qDBrRHwc_WrJMXnEzErJHANN8Y5BV6bW4kzGMsY1chMDX_yzlp2nBRQ5h6OodIDAppgqc5gN96dFBKFtdpMS9ERI5Yoq02UoJWvWfy3IMCy4sk2GZUHtgG2GTPCi8QWuafjyjkpvgz89qaeoVxFJ1YDWeGU8qflepXk0BpWN6SSnE_wHLeDzMDhb3gqVyohPzIM0rUCfl-GTBhDIbt3ZPKBWY7jJ6KzBgpffVz-BQrTJJmrrJav2N1xOJ-3FoW11ETN0xWeAEKT_PfK_2FPVfaUjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=L3Ej5WYXC946ysVlLiuLjWrfQfKQUuvFuhnH6ML1LuCYk-aVSbQU84-vcNC7L_OhJt80Wic1nJ_lv35NbLyBr7IsR07ElNXi8kip5ivBj7eRm8GmdEahduMMSr_-VaqHAuIkoO-E7_BOiwCVUbLZ3OPqbFmkOWJsQWfxpFp-lw-cMhPqaHT_2uXxIEcCsvfZqVhcjASikeDPc8mBKzQhqj9-1YWKENprO1y7sdgNfugGkmLmXyMHsjgmnEHNvz56l7XzG9zEBqaufKJUx7g0XA1hnB_x2gVioNXOEs6Sd5VgE8eJI5NPsxdbrW-9HMugXm0ORXJrirYoAHq6MUY55Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=L3Ej5WYXC946ysVlLiuLjWrfQfKQUuvFuhnH6ML1LuCYk-aVSbQU84-vcNC7L_OhJt80Wic1nJ_lv35NbLyBr7IsR07ElNXi8kip5ivBj7eRm8GmdEahduMMSr_-VaqHAuIkoO-E7_BOiwCVUbLZ3OPqbFmkOWJsQWfxpFp-lw-cMhPqaHT_2uXxIEcCsvfZqVhcjASikeDPc8mBKzQhqj9-1YWKENprO1y7sdgNfugGkmLmXyMHsjgmnEHNvz56l7XzG9zEBqaufKJUx7g0XA1hnB_x2gVioNXOEs6Sd5VgE8eJI5NPsxdbrW-9HMugXm0ORXJrirYoAHq6MUY55Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=orPgVyAt2jvkkhIX385TcfH2ELGG1TSv-unEWwPN8Rg5bIpLPwUY680d_V00PxWPkCNUN2eLSkSbV2OhQMLjFWE01wJ-RM2Pi2GiNWYZMx7nqUK2a0mDV3-rmaWZyaoERPAREKH-zBZuhN4PJerCqtIyKrWiIBkA2BrBItpbLz2rWD_OCrsCImcN5nL4YZf2Uvu04rKFyPCzA8qx7nz3DP5PjB8OR5dTlvQZFcfqGfsoRp44wwcMmAr8qvKligu66UOPNgTzSiBSkCcJJO5DMQCAVSLERLTtvez7-Lao2qfxjr64Gh8SgfO8phlwdCqR4RFzZf_6nXJ2TI0HsOUTkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=orPgVyAt2jvkkhIX385TcfH2ELGG1TSv-unEWwPN8Rg5bIpLPwUY680d_V00PxWPkCNUN2eLSkSbV2OhQMLjFWE01wJ-RM2Pi2GiNWYZMx7nqUK2a0mDV3-rmaWZyaoERPAREKH-zBZuhN4PJerCqtIyKrWiIBkA2BrBItpbLz2rWD_OCrsCImcN5nL4YZf2Uvu04rKFyPCzA8qx7nz3DP5PjB8OR5dTlvQZFcfqGfsoRp44wwcMmAr8qvKligu66UOPNgTzSiBSkCcJJO5DMQCAVSLERLTtvez7-Lao2qfxjr64Gh8SgfO8phlwdCqR4RFzZf_6nXJ2TI0HsOUTkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvOwLg9EGTQxp-hmd2n0Vxp5tmAF2F5ByYGY1sM_puHirASuIOr5jlym42lqs2KLAQRaX0EjmaA1byFS4mj7rAJwNFeMRdLfcUaqXyk988KOyThsfLts504tEx2KfKaEY5KoV2PNYtKj1lR2Pnbv1Bvj4VpAUFFsJ4gtOlTp-TgyqBJPDpWVupKnDGjs4nQKMaRY0FEKsFAKwYnx-T-0pDUuO2G1JzzA2RZBU6u1X5y_MBm3MCr1jWhW1KpvrbbSN-uvF-ZRpOq0esVvos-1Lw4lF7LiNsieGARh8sDA8VJgq_8U8h5vhgTvdF0Sj45qy8AmvKnzLqioq3cP40nkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mLmJEQriLwG2C7UG2fRjKj4DDRwmX4ZUwpZ1mrjUGNVdvNtL-fysP4eYPgc2jT2y5HLHwgxvZBW6BOq4tP2K_DhCGdDKj0PwnDzt_WX-vkZ2-yBZ6szDwmqhNJjriPtRFW8QchdsX7hTR42yLjRjs_dN9QiYXIaCkkvP3jabLsw4oIoWP_GQHM91WvVoo-D8VLWU4SChQ-S9VsadtC87PJWF0wou1AzEBsLmfG8jR0zP7rOhp4eq5j_blPxXZSFprg5zHSZ4DrV_vbIMeH-EV1zXOc6RwaWzKggDAZSdyQz3v6leJRXVUWnPHA8nT7cYMsSMPd1ZD_tbrOSLm2-vAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=HoBzuEKpBNRNXRtVqRH4rVtY9mR_uECf6j3WZIbm2YUj5Ssz_rVip96qv2pQGfC3JzQXT5heEuMPgy-qru_yVC5aiHZGNJUzV6cLCk2jAQcUaJAx5qUW--QfEllPnwi42VN3HRIxw3GggulSV-UJVYhLbOvhz34ivbHCAFaoHwAo0rDiEYQ232XzMmEuCGv0ut5_XRh6ALfdV18IvYoLd_4gYp1d9dvozxtLG9Apm9MVaRCZLtmwFoRxW1raWFr3zPJ8orf1tKhCb6g-DfIDN8_akKuJLrVctmVWJWolt4uJ1iovb3_Xk1mD4NOZr57L42YflUM4t-30m2LQsyUZUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=HoBzuEKpBNRNXRtVqRH4rVtY9mR_uECf6j3WZIbm2YUj5Ssz_rVip96qv2pQGfC3JzQXT5heEuMPgy-qru_yVC5aiHZGNJUzV6cLCk2jAQcUaJAx5qUW--QfEllPnwi42VN3HRIxw3GggulSV-UJVYhLbOvhz34ivbHCAFaoHwAo0rDiEYQ232XzMmEuCGv0ut5_XRh6ALfdV18IvYoLd_4gYp1d9dvozxtLG9Apm9MVaRCZLtmwFoRxW1raWFr3zPJ8orf1tKhCb6g-DfIDN8_akKuJLrVctmVWJWolt4uJ1iovb3_Xk1mD4NOZr57L42YflUM4t-30m2LQsyUZUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=S7tIRAOunPGtloocSW2wFDa7WA01nSkjYYB7voEc0JoVb0uAAxDVYry3WA0S7V7ymJCw7GMwaUvRFanSapgDXDxo99Dc20eh3qyQJ-w99fEwCsy2eCT3iUT0tKO5IUZ9X66p0kZgtEV3c_V6Q018Vkucee7NChYKOhqFmZa5RcCauZkNyQHarj2PRT36SOUhUFiaanuL5zkMoOMUVZQa4oNmy6XV9PO8p-J4WtfG3Udl0yljTeEg7k0RGpV6yNMVIuOYWe75pklKSKCf28YizQ_HoEJucdGx7U2cRLad3j0LyhRHolD9Tloq0V79wd832LWY8eMAMqnKvXPWsvaOSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=S7tIRAOunPGtloocSW2wFDa7WA01nSkjYYB7voEc0JoVb0uAAxDVYry3WA0S7V7ymJCw7GMwaUvRFanSapgDXDxo99Dc20eh3qyQJ-w99fEwCsy2eCT3iUT0tKO5IUZ9X66p0kZgtEV3c_V6Q018Vkucee7NChYKOhqFmZa5RcCauZkNyQHarj2PRT36SOUhUFiaanuL5zkMoOMUVZQa4oNmy6XV9PO8p-J4WtfG3Udl0yljTeEg7k0RGpV6yNMVIuOYWe75pklKSKCf28YizQ_HoEJucdGx7U2cRLad3j0LyhRHolD9Tloq0V79wd832LWY8eMAMqnKvXPWsvaOSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_n9DOJz5iQTIB_N7HDolQZOfY2_HbXTE8HT87OU98-NDUQMGndOkKAxmp2XKistpwsmDgsENLZZI3ca1mHR3t6UcjEyIHJFpprhmgQLNDjNi6GTiax_-jOwHRd9x1j2ndCA3dG2AgXqLVeVtPd1hxaYYEKT88WdxXQxlfJQVKMDOrIfEUbJ_-yq0AMMqJJngWWLZjyZwjPGaQ0faqucSWXo4l_8QUBYreSNwUM7Rf9t3stIS5I8CS4QP6B_7ML9mVCWaOTXaEL5Y1sAtqYUn8-o0voVtdNG7QcCD7_7Rx8zADhQO11AQkrXSa46MSTEHuAvFUi8Gm_Uh8UF2wXOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rp5sNnzWXEtDZlgsFLaC_vp-rym6-iNvhZKNR-4xVSwxsngzquH00ezHcJvyjmkCbOOfD4CfH4OlOUIbZJXC0h6WNn90lTP1lv8vqCCmIVON57hRaXubVqy2SeHMUEmGMkuVaZ0KqKlrOIInDbxcF20oU3Dsf-VRKeBt5rXNcfPnEn81Zfm312xMPpv0lwK17bmzGHkXwYWCotsDhJEthHB9JeG2z7SDuqtVUOL7wV9wWae36-NAEBMgiOoLHCAM-O0kirwn-L1C9mGdmKRuOzZi34KQKpR3oMquzWKiywLWFTVgy80e6gnLjKlOcGfxwShWl8sp0588p3pHSF49aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IS9qRAvH8NMu1vaGfK_nLwUbfmbBiMll3hQfEsoVYRWg4B8LnVduEr9KfA5eFG7ZK2HRrrR19gTxa9lpPxxSFlAd8clXyNYynAFXQC84QuRrA2Ck15r_P3hO8fm8gDmA-3fkLW7ke4NWfiwCyWU-M8FrKI-sHuDQKR4ZYWn6q9zMHq3Smb80d7shgd-_p07Xzj_EGgSMGcF29IoNKy2V_lK_VVJlGtHKFRZpr80BVh1jKZem3SG6kX_0dqL18-NFAgDxVHUO4lg3ideBKfo2R117w4fXm4kZTEutcVKd13lUU9zFeY4gcSf0sP9caUdeMsyKYfOPnISiiSr7SBZLyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twvTRnkPm3BqJUvpyVFYCFHERNmGDZNdhZ83IxPV6WVdq593cv9fpNW08lA4hyyl1Cuts_TgA-hx4_v6sCrq_Rb3di11J8qA8X-_JyLh0Sg0zCov9er9t9sAJJPENd2MjdBotQIdabLTlEm6vE-VjuK8zj8lp69vt5ZCCpgi3ZQkNplPrO6usPi8Tu-MmGDDCzXnpK36T9OAWWeGnxIq-8NkYf40_KyoEkIS1K8tz79GgdXwAe5YXU4QThF0RzjFmoQ7RnW6vPMC_XMeQ5OW8Y1B_IZmFOp-WA7ZzpUiPtIHs5AXOy-q8qWIUxhyi83QjL5gOojyStrI3TXmgya2_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=MxvNMiBBAW5GN9xthh4w4A0cWSYh8oQdSuHS3Zo1dcfZr3GFmqaX_kzkQZ3ckGts2qEAftn82CvCrLsWfco5BZyp7yCjiCZBxxOq07oFn_6jj0_68YkNuQfuRswQZROzxjyPK5ZyR0pK6vUYSi8O6qFHUQ_e8F2jXXGFGAWT7dBzJIIBmSXuTOytk6x7qr6MEzR5yIAVQh1ANfhvkm_W8NQYKRwKU35xqzKFon6YTGvV7BCMs4PtWc7FOYyI-Lg9YKP2w3ideyTRI45UVkzMAHIFbvMyOBSB6GTyrSNjzaolBG088y0Ctx4k8Ng6tmBQkuv45CpEkvdeRhgESesrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=MxvNMiBBAW5GN9xthh4w4A0cWSYh8oQdSuHS3Zo1dcfZr3GFmqaX_kzkQZ3ckGts2qEAftn82CvCrLsWfco5BZyp7yCjiCZBxxOq07oFn_6jj0_68YkNuQfuRswQZROzxjyPK5ZyR0pK6vUYSi8O6qFHUQ_e8F2jXXGFGAWT7dBzJIIBmSXuTOytk6x7qr6MEzR5yIAVQh1ANfhvkm_W8NQYKRwKU35xqzKFon6YTGvV7BCMs4PtWc7FOYyI-Lg9YKP2w3ideyTRI45UVkzMAHIFbvMyOBSB6GTyrSNjzaolBG088y0Ctx4k8Ng6tmBQkuv45CpEkvdeRhgESesrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64840">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
مارکو روبیو وزیر امور خارجه آمریکا: ایران به توافق جواب رد داده است
👎
خبر بالا فیکه و روبیو چنین چیزی نگفته
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64840" target="_blank">📅 00:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64839">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کشور عراق، تلگرام رو رفع فیلتر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64839" target="_blank">📅 17:21 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64838">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏ترامپ: ۹ جنگ را به پایان بردم و در زیر دهمی زائیدم
@News_Hut
#Fun</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64838" target="_blank">📅 16:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64837">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJD37oKu4NT3koSnpNKhNsFOgeKQxHOwMQqladBpejtRV25-CLdwVfKKhsWL-UM81WRiTxiLylLR9NTZr287gBC4rNMSeXJlmjj2Nx4EQAB8OPoPUvuO_qhDso2lF77t0DuQMWt3yY9zFk4ktSPKBbbJVKeX-axxLlnNTwH27KJHaUOvgpWg0TpkeyKHtG7uvPArnynFRCvrjlkKt2lBUNaVDxSgBrFBfNSYbuOA3mRpIfNS3tsaXRYY9QRC8NJIsLJn4cuJThveYI4PhJz9lJBUL4VNe_F6V_Ju8s4UBcW8KndJab_WPEJnLdOb9PVnohYM7goBs_8gGD4NxGoxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#مهم
؛ این لکه نفتی اطراف خارک نشان می‌دهد جمهوری اسلامی به‌ناچار نفت استخراج شده را در حجم بالا، به دریا می‌ریزد!!!
اقدامی فاجعه بار برای اکوسیستم خلیج فارس
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/64837" target="_blank">📅 09:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64836">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=MILG02hR8qKQZvyPyBLYXH8eSjmrcEhGh-IyOuM6qrSUuF7phPa8lGvLVSnEX4hfuqHHJLJUc1gQw3cWdf0Yz05niwacJnAt1Lc6zcDOlFNh0rrEmueHY2kgX-q8wCkjQV0JW2wmHIcUFMLNl7DgnZ5JuLC97WCTlKZU2T0V4BZdBekgGC-x7IuzWgQ5X-NnbsxCF1o-gRq4V4ofceZBwOsrRRBo1gCtdDA8sqUVxy8BqmIkKO4knxOdNxge4B3_-YncX6-q45MUqjhBXiztD1FkzsUDeRW1g8NI8_QOsGZQepPuCfCGLIe4pSk18kMKwJNK8OpT3qQ0w-SPMGKqQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=MILG02hR8qKQZvyPyBLYXH8eSjmrcEhGh-IyOuM6qrSUuF7phPa8lGvLVSnEX4hfuqHHJLJUc1gQw3cWdf0Yz05niwacJnAt1Lc6zcDOlFNh0rrEmueHY2kgX-q8wCkjQV0JW2wmHIcUFMLNl7DgnZ5JuLC97WCTlKZU2T0V4BZdBekgGC-x7IuzWgQ5X-NnbsxCF1o-gRq4V4ofceZBwOsrRRBo1gCtdDA8sqUVxy8BqmIkKO4knxOdNxge4B3_-YncX6-q45MUqjhBXiztD1FkzsUDeRW1g8NI8_QOsGZQepPuCfCGLIe4pSk18kMKwJNK8OpT3qQ0w-SPMGKqQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آقای رئیس‌جمهور تقریباْ ۱۰ هفته از اصابت یک موشک به یک مدرسه در میناب می‌گذرد. چه کسی آن موشک را شلیک کرد؟
🇺🇸
ترامپ: این موضوع الان تحت بررسی است و ما به محض اینکه گزارش را دریافت کنیم آن را در اختیار شما قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64836" target="_blank">📅 09:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64835">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
ترامپ: می‌خوام کل ماجرارو تموم کنم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64835" target="_blank">📅 03:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64834">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
ترامپ: خواهیم دید چه می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64834" target="_blank">📅 03:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64833">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مارکو روبیو: متأسفانه، تندروهایی که دیدگاهی آخرالزمانی نسبت به آینده دارند، در ایران قدرت نهایی را در دست دارند.  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64833" target="_blank">📅 00:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64831">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMpXzNViU94JYZd8iMvf9Y2-QKCRagxHe0fO0GQNqSxx2Pdl4cegtUUvrJXgh9OP7YgLkmJgqACsk4Qv3tFNHaj1aYO-TBv_Tp0jvxbOpesLcKO7dTz99thrQRqkEemrISTmjV6wdd0WCViyJmQiiFj_Ei0x6Jnk3LAEwMbbgfVjvLCnygeQyLbg9o2ib2AaXpCM7oHWk1ErvWOnYlcQG02qQfD1bNsViIsvC8e77ngK1kh4mmgrGv87Xy_amNhD47i2ISvqefH2Z8oaCCNasuP0JlOZxQ0KjTD21KqVtADLDbBLbAGfmvNJbyrOD1JvsZNT7CH_Fo_oQYT3veBHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GE779g-X2_fJ0D9sgRm3wxPQkltg6V0B04xZSEbLFJ_22y-HK_3LLSON9YlgS7BosvQAZJJTBYH7AsRyXIOl5Z5ujaEgrOC1C8oJsRnjq1xqRGpJYqsDm3lIohi6DGA550J61mgRePsusVHBQ2eR__MXA9u1Ut4VXXiUfj1en1iHIp9utrus8FUC0iBal3wX7uHeEF_stFoO-XFGLvouMspwcxUwYNrX-nnApo5nnn57EtgFR5_uj4upK732X6JBz9R0yHiaIRbvkHRlw6lPU76tXXJsozSWga_C3CRuc3KjcfpF7GwF-Kvj_h_-1TfjtYdUeynfpt7oDrmnjbduEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ww30hzx91CXGL9SiCShcpCt9SkD_AInsW9u-yeETfMzXorEMTlKGSO9CwOgpIIiM3nmVa2RaewukhonqLtiXCA8LjIOGQ1FO116e92KvbiskRMIxneWLNq1EVE9Hgpnr4N2QY1Em8KvvjokMG-Sc_6hII0pzLT_l6uKtMN7f_RMIekg1GnNMnacEsK6BooXbqpQM9x3hJteae-5-lFLSpfQi3vXsTp736f-MPXqZW9qFtJwLVVoN3pS3NE7kyGTFA1_Unl9NMKfdEdrN5oD1DJshTzoPFMTuqUy14xXTJ7AMtUVyecmEKzgaYGzWb4Jjkai7hPyneGq1LIdSrU1Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1g0K8IYyKxMTeootk7gzX9cvem2824gj73IWGWtbwLG0BmSp9bL8QSGWAlAKAcDWcHk78ZpvqZiNeZNZEUn2kVa1d_6PBIuJHRG0FFLrNDGPnEQ9MIfVuY9aO0h2CAcq8gQqP6-8lX40elFHkYy2h8JUz40d5ZFzidBggaI7_DlxNnPZiFZc6FsFAag6VzC6lnO6rUE4rccD2Aa1mac8XskLCkr9vEnjehizrPWLY5Ms143ifRMnmS7kP5lCwegrXsH19MejHtrvF0O9ExvD9Ow-a4lYStLqqB4XbXnSw66UESIRPJyqD1A89P1Vy0BUy0jpdM-RFVa7oQgSf41Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فشار جنگ کم شه
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64828" target="_blank">📅 00:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64827">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=IMWHv3aajOdu1gRkrcyV523Ns991rjM6eHpBc74ETmO6oP93ur6aBbCr1IksCydm66zXs7ytR_MR95NOKdq3b3IU_dxn54_0a0IbtRfg-4jz4uRHzYdPNLOrja0-N4hNJnUIHkyt0cILTgsMU_eV1PwU18Q3RFPLS1j3N4tQrDdBgWtJ3kUQlPCBrm8fKlU9zMaXxsfAoMuER6zzlH4qir9jHtYrp3NHrggXbKGnC_zdWkfzEzwHIlX0CnQG6M8JUSr9YNEtY7UP2-G0U3GMt3SneQML2jPiMPeoPdZabtUWnD4UOeKh0O_R48EcWlP7W6nMqvl0Gxmwke1tps6A2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=IMWHv3aajOdu1gRkrcyV523Ns991rjM6eHpBc74ETmO6oP93ur6aBbCr1IksCydm66zXs7ytR_MR95NOKdq3b3IU_dxn54_0a0IbtRfg-4jz4uRHzYdPNLOrja0-N4hNJnUIHkyt0cILTgsMU_eV1PwU18Q3RFPLS1j3N4tQrDdBgWtJ3kUQlPCBrm8fKlU9zMaXxsfAoMuER6zzlH4qir9jHtYrp3NHrggXbKGnC_zdWkfzEzwHIlX0CnQG6M8JUSr9YNEtY7UP2-G0U3GMt3SneQML2jPiMPeoPdZabtUWnD4UOeKh0O_R48EcWlP7W6nMqvl0Gxmwke1tps6A2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی مسئول دفتر علی خامنه ایی درباره مجتبی خامنه‌ای:
خونه اقا مجتبی رو زدن ولی ایشون تو راه پله ها داشت میرفت طبقه بالا و فقط موج انفجار بهشون خورد و افتاد زمین.
فقط کشکک پاش و کمرش آسیب دیده که کمرش که خوب شده و یه خراشم پشت گوشش برداشته ولی الان خوب شده
مردم صبر کنید دشمن الان میخاد یه فیلم و عکس ازش بیرون بیاد که کارو تموم کنه به وقتش عاقا خودش میاد باهاتون حرف میزنه
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64827" target="_blank">📅 23:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64826">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVPbo64w5dqOglz42ChrghP3HhpQINC5cDrxJooXuKdkA07CPrFCxUIv2ky3SRkvHFKJGvQTwJ5pXf7MRnYempIYek3WUoAdTQR2acMVpFzrPVh_86hkM7vXJWt9OGrE_YMyGwqF-6e0m3V8IMBr1PWUHGiJ9A4otlzVG-HLkCm9Z2KODBmWhTOLyIUZnismQ2HUqmUsj-4iJvNc8Te4yTu5Wsu9nOGPSFVEKTm7UgqAleuZpYowNYgNyIccPY8Fr9cVlVL0knXQev0F8WfD1hK9Qw7AUCZ1upXpcKt0iK_zThr5Jfvl2PMO0bmLkg36tu3BnA-DgxJ7IVWGjnMccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ ۳ روز آتش‌بس بین روسیه و اوکراین اعلام کرد:
خوشحالم اعلام کنم که آتش‌بس سه روزه‌ای (۹، ۱۰ و ۱۱ مه) در جنگ بین روسیه و اوکراین برقرار خواهد شد. جشن در روسیه به مناسبت روز پیروزی است اما به همین ترتیب در اوکراین نیز، زیرا آن‌ها نیز بخش بزرگی از جنگ جهانی دوم بودند.
این آتش‌بس شامل تعلیق تمام فعالیت‌های نظامی و همچنین تبادل ۱۰۰۰ زندانی از هر کشور خواهد بود. این درخواست مستقیماً توسط من مطرح شده و از موافقت رئیس‌جمهور ولادیمیر پوتین و رئیس‌جمهور ولودیمیر زلنسکی بسیار قدردانی می‌کنم.
امیدوارم این آغاز پایان جنگی بسیار طولانی، مرگبار و سخت باشد. مذاکرات برای پایان دادن به این درگیری بزرگ، بزرگ‌ترین از زمان جنگ جهانی دوم، ادامه دارد و هر روز به هم نزدیک‌تر می‌شویم. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64826" target="_blank">📅 23:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64825">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAknottnErVLj-mdJknHiyOgwWDR2l3kIGDFI61X5v0D_0j2BKghh3xYBttk3ZmcEfq_xM7oy3XceALU-LLBC2R3-kr8jYSrMgrvWTHE-8XaP52KBadq7TloPJ82FIr275h77H__EZnq2RpQ_5COvk91dMuFbybRNBEY_k2effyXmqvqFrooigqzkZymceAKdutS0yDuh9vaClyEP-Rsn7xV0cDRl7DZpbhPRE2llKn_NN-4PNonYYgHv22Rbdq7Lkp_s7EFUS90-4t326gyVwr849RsY-5tXe3qldHcVyAK6y6NKA9WkjmMyXSXikVV53622CyGA7Nx-8Sk5dHzJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
در مورد وعده من به شما، وزارت جنگ اولین دسته از پرونده‌های یوفو/یوآی پی را برای بررسی و مطالعه عمومی منتشر کرده است. در تلاش برای شفافیت کامل و حداکثری، افتخار داشتم که به دولت خود دستور دهم تا پرونده‌های دولتی مربوط به موجودات فضایی و حیات فرازمینی، پدیده‌های هوایی شناسایی‌نشده و اشیاء پروازی شناسایی‌نشده را شناسایی و ارائه دهد.
در حالی که دولت‌های قبلی در این موضوع و با این اسناد و ویدیوها شفاف نبوده‌اند، مردم می‌توانند خودشان تصمیم بگیرند که «دقیقاً چه خبر است؟» لذت ببرید و از آن لذت ببرید!
war.gov/UFO
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64825" target="_blank">📅 22:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
چندین تصویر افشا شده دولتی از اسناد بیگانه‌های فرازمینی، پدیده‌های هوایی ناشناس (UAP) و اشیاء پرنده‌ی ناشناس (UFO):</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64824" target="_blank">📅 22:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=UjjfK92Au9kdDMxcUXljld4YVBNutbh3PrP9LAv4-hsqVJA0L_kymmLTb7qQ9pRSQ6Wl1N7C1vJR4O_jWX6qco9fXtutSg5IhS_1HZt3q3xoUIGWVdltSFwVPedUeDHEyVpUDnHAVqp2ffeNDtQ-7_UOFHLwO7v295vxTSPmzgm-dYB88VMpKXS7vPKYlzRLtXC7cO8JNcmQtTBwGU0Lh-cbCObslruXqpmOtwdL8WzChgo3C6IUvKdUvlyznGY9ZtjDImWS-eNdJgLqfZQ3YlR2i711ukjBvSNpB-9zdU9OqoxM1_W98bhpgNIN2wkGAWHfMoaeQ07aJ_S3-nxiuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=UjjfK92Au9kdDMxcUXljld4YVBNutbh3PrP9LAv4-hsqVJA0L_kymmLTb7qQ9pRSQ6Wl1N7C1vJR4O_jWX6qco9fXtutSg5IhS_1HZt3q3xoUIGWVdltSFwVPedUeDHEyVpUDnHAVqp2ffeNDtQ-7_UOFHLwO7v295vxTSPmzgm-dYB88VMpKXS7vPKYlzRLtXC7cO8JNcmQtTBwGU0Lh-cbCObslruXqpmOtwdL8WzChgo3C6IUvKdUvlyznGY9ZtjDImWS-eNdJgLqfZQ3YlR2i711ukjBvSNpB-9zdU9OqoxM1_W98bhpgNIN2wkGAWHfMoaeQ07aJ_S3-nxiuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیو سنتکام از حمله نیرو دریایی آمریکا به دو نفتکش ایرانی M/T SEA STAR III و M/T Sevda که سعی داشتند از محاصره عبور کنند؛ این دو نفتکش پس ازحمله متوقف شدند.
این دو نفتکش تلاش می‌کردند در یک بندر ایرانی در خلیج عمان پهلو بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64822" target="_blank">📅 21:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64821">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
📰
فاکس نیوز به نقل از یک مسئول آمریکایی: ارتش آمریکا امروز به نفتکش‌های ایرانی که قصد شکستن محاصره را داشتند، حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64821" target="_blank">📅 16:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64820">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: امروز پاسخ ایران را دریافت می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64820" target="_blank">📅 15:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64819">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OncwuMByeLeHnGJ-AC23Kh4ZwGOLdqf7SmOzgKlRF3E6Bha25ZWNGv1W0dIONirIl5SQLamyXYPPXYiAjEeF05NhYQGFiVGNcyFt9nvw26YhLXZpqGqdZoSQiodIUUgooyEK5QntxyK_LAFUzR6lrE-QhG49Y6pcIVBpUfK0VgamivGoBolvYshzw66lyRW_qQF8xZ_KAfZ_KPKzrVhbV0Rc0ft6NtXPt8aYjgGjr5IRVXXtTs2bf4HwR88LRPa886oCwuu1Ev3UTtogBEa-cRDswbvZ174CHAL2WBhigdrQNFjz1VSdXvGTI4lYnz4KLPQST0Cx7OXoZUmxeh3LJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات که نه، حتی اسرائیلو هم بزنن ترامپِ کاکولدزاده وارد جنگ نمی‌شه، چون سفر و دیدارش با اون کیری‌خانِ چینی براش مهم‌تره #hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64819" target="_blank">📅 15:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64818">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64818" target="_blank">📅 14:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64817">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64817" target="_blank">📅 14:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64816">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باورکردنی نیست آخوند ۷۰ روزه که مردم ایران رو از داشتن اینترنت محروم کرده، چقد شما حرومزاده‌این که دارین رکورد می‌زنید
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64816" target="_blank">📅 14:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64815">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=DeAjE5ftfzjkIS4YmeA-fcFn8p0CciDBQXU-LKSlWPXCVEJ715lEveOtTQG6OjIe71eMPIqfCVaoKdiXCuB-8v8kD1_aP2WuPJ2nLEGhwncYQniDauPsth5vXCygn8vBkt9a_cL2qoJM_4qJeJAyfQvsN96KW3tBzvshJf32mZQGKlbJLYiSAqQiAWjQG134n3YJqBKAxFhgLWt62R1tucoP-neST5kEuGBitQYMpC-nioCycyuZ0v0lH9CHc1rGg1-S6rIS82wTccK3yfBDEXGw9085uXjikHLBglJsxqAwumajiQSWRQpyM6VNA35-RgbbbVL_hWwQJt6weBBdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=DeAjE5ftfzjkIS4YmeA-fcFn8p0CciDBQXU-LKSlWPXCVEJ715lEveOtTQG6OjIe71eMPIqfCVaoKdiXCuB-8v8kD1_aP2WuPJ2nLEGhwncYQniDauPsth5vXCygn8vBkt9a_cL2qoJM_4qJeJAyfQvsN96KW3tBzvshJf32mZQGKlbJLYiSAqQiAWjQG134n3YJqBKAxFhgLWt62R1tucoP-neST5kEuGBitQYMpC-nioCycyuZ0v0lH9CHc1rGg1-S6rIS82wTccK3yfBDEXGw9085uXjikHLBglJsxqAwumajiQSWRQpyM6VNA35-RgbbbVL_hWwQJt6weBBdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دلیل اینکه عملیات “پروژه آزادی” را متوقف کردم این بود که رهبری بسیار خوب پاکستان و رهبرانش و فرمانده فیلد مارشال و نخست‌وزیر در این موضوع خیلی عالی عمل کردند.
آن‌ها از ما خواستند که در زمان مذاکرات این کار را انجام ندهیم.
اما اگر لازم باشد، دوباره به آن برمی‌گردیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64815" target="_blank">📅 09:14 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64814">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64814" target="_blank">📅 05:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64813">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64813" target="_blank">📅 04:53 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64812">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64812" target="_blank">📅 04:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64811">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چالم کنید جاکشا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64811" target="_blank">📅 03:03 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64810">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AHWUpZaXFXHw-G2356gAcQYc22X3Dnao8B4zz0hXUWbFRsKyEFeWzPgyMRid3FE-Ll4ScSKKa75gf3SY7PheOLNiih3FBwokd5LMItaGrYLJFt_GEjDSGAzTWM0mgv3J5MPo5gVKERiJ4ukj1-xt5nt5_RU-KuIcJjvH5HD63uZLF3JJLgclMx97E5KtgNoVOO14_z0vjg-Scj2nIbXpZzD-1bK3hCd4I2ciCwLbYp8d4OID6qMfGuq1caA8jZdeQbZSeO3Sn_u1GpbOjkQLWOw13V6HxmGha9Fl0CxJNaO8TdG03HLGFseG5d8IuEn4AIaK9afNQa5PG3MNjKDBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
سه ناوشکن جهانی آمریکایی با موفقیت کامل از تنگه هرمز عبور کردند، در حالی که زیر آتش دشمن بودند. هیچ آسیبی به این سه ناوشکن وارد نشد، اما آسیب بزرگی به مهاجمان ایرانی زده شد.
آن‌ها کاملاً منهدم شدند، همراه با تعداد زیادی قایق کوچک که برای جایگزینی نیروی دریایی کاملاً از پای درآمده ایران استفاده می‌شوند. این قایق‌ها سریع و مؤثر به قعر دریا فرستاده شدند.
موشک‌هایی به سمت ناوشکن‌های ما شلیک شد که به‌راحتی سرنگون گشتند. همچنین پهپادهایی آمدند که در هوا سوختند. آن‌ها بسیار زیبا به سمت اقیانوس سقوط کردند، درست مانند پروانه‌ای که به سمت قبرش فرومی‌رود!
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند، اما ایران یک کشور عادی نیست. آن‌ها توسط دیوانگان رهبری می‌شوند، و اگر فرصت استفاده از سلاح هسته‌ای را داشته باشند، بدون تردید این کار را می‌کنند — اما هرگز آن فرصت را نخواهند یافت و همان‌طور که امروز دوباره آن‌ها را از پا درآوردیم، در آینده خیلی سخت‌تر و خیلی شدیدتر آن‌ها را از پا درخواهیم آورد، اگر قرارداد خود را سریع امضا نکنند! سه ناوشکن ما، با خدمه فوق‌العاده خود، اکنون به محاصره دریایی ما خواهند پیوست، که واقعاً یک «دیوار فولادی» است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64810" target="_blank">📅 02:28 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64809">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cobgecb3poGIaVYxmWtaQISfnIsVOqhN4A9ab_CReZn0OtiWdukD9-MhUV0ehdsuWc0_cxYJV7sv7I-H5sgdBuRdLFryhV6tUG0Ml2HC-58HYk71qAx4bXZCdK2vwqo9A2yZ7DYbpUB1QwBA_MpvsBiSu1MDBbBb70kM1BSqCPzFL1uDqdp_DLtpLUtT-SS98JR0HtucdqyEguSzHwtGIl_3KNlgkLHs3Hxne_o3lTwaA6brOkXo6Q6N8NSNzneqqsPEj2hNgrQcR2Inm5A7lMtFVJqFjldZkYXbTQ4cmnMn-VZFzxNA8L-9edYUawm0NkfCpBRY70kN_aHpg_dudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خلاصه: چند تا ناوی که تو عملیات آزادسازی از تنگه رد شده بودن؛ خواستن برگردن سمت موقعیت قبلیشون که سپاه بهشون شلیک کرده، بلافاصله نیرو های آمریکایی تاسیسات محلِ شلیک رو بمباران کرده و ناو ها هم بدون مشکل رد شدن و قضیه تموم شده!  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64809" target="_blank">📅 01:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64808">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64808" target="_blank">📅 01:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇺🇸
#فوری؛ سنتکام:  نیروهای آمریکایی حملات بی‌دلیل ایران را رهگیری کردند و با حملات دفاع از خود به آن پاسخ دادند، زیرا ناوشکن‌های موشک‌انداز نیروی دریایی ایالات متحده در 7 مه از تنگه هرمز به خلیج عمان عبور کردند. نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64807" target="_blank">📅 01:44 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64806">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64806" target="_blank">📅 01:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64805">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCuiLzpEdcpxsi6GNd6qBrCBePJGy66fqt6iSJPsKmQOneZbg0vbqCQVZ6W7dBaLGPIzLU6_hfdZTXfwI2l8Xv83v2NZHSg37-DFT9uL5bw4e0QgSLqQWG2FRT4dAM64S-nY5gXtb4aaEwHgwSTVU4oSKnK20cCX6AdsEItxCO9YTawBkH0BoGA3rM9DDpRv5wBBqx_kQxHqjNVXNgFFFczaqfKoQBxaVD3tMjCFuxl_IAeIWNNgXBOpWVJugItER5siD_HFMbI3SdspAD1esMbBZMcpDaMr3GcF3dai-HCb5CXZQ3JZBkJT9bMAPfiGRGolSXs7lVtAsfqLeGPSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای جنگنده زیادی مدتی پیش از بریتانیا خارج شدند
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64805" target="_blank">📅 01:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64803">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64803" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64802">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xpf2BaqiMvO_KA7f1k8qN7rmaCABEVoPaDn11jyR5aV4XhLrmobkUrDuuV5qVO62q-32Ta0_F9FldYGPfh0P2s7Rd2sOyx63RPWdB9iKD3kJnXvG0VqishFDlNSabHZsHIwmNuS__jbkW9mBIFmhDuE5nGLxW9yAyJKDPpBERzH0i_Fwo-u8H2RU_TsnZJCejMggEDjSac2LB0C10gUgyDzVEFtNFFkBMVW2aBFajFu69mxr5ikhwi9BLfBJPpD93CEY8oPIfVpeWcMShQizRvsxiHlR6AHf2rrsGby7yD0Nk2xyAy13Oe0T0iB2DXaqiAOx3LIiBzldB9AK52xuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ سنتکام:
نیروهای آمریکایی حملات بی‌دلیل ایران را رهگیری کردند و با حملات دفاع از خود به آن پاسخ دادند، زیرا ناوشکن‌های موشک‌انداز نیروی دریایی ایالات متحده در 7 مه از تنگه هرمز به خلیج عمان عبور کردند.
نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک را در حالی که ناوهای USS Truxtun (DDG 103)، USS Rafael Peralta (DDG 115) و USS Mason (DDG 87) از گذرگاه دریایی بین‌المللی عبور می‌کردند، شلیک کردند. هیچ یک از دارایی‌های ایالات متحده مورد اصابت قرار نگرفت.
فرماندهی مرکزی ایالات متحده (CENTCOM) تهدیدات ورودی را از بین برد و تأسیسات نظامی ایران را که مسئول حمله به نیروهای آمریکایی بودند، از جمله سایت‌های پرتاب موشک و پهپاد؛ مکان‌های فرماندهی و کنترل؛ و گره‌های اطلاعاتی، نظارتی و شناسایی، هدف قرار داد.
سنتکام به دنبال تشدید تنش نیست، اما همچنان در موقعیت خود مستقر و آماده محافظت از نیروهای آمریکایی است
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64802" target="_blank">📅 01:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64801">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇮🇱
#فوری؛ کانال ۱۴ اسرائیل: ایران اعلام کرد آتش‌بس نقض شده است!  @HutNewsPlus</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64801" target="_blank">📅 01:06 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حوصلمون سر رفته، کاش وحیدی چن تا بالستیک سمت برج خلیفه هوا کنه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64800" target="_blank">📅 00:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64799" target="_blank">📅 00:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تسنیم: داریم می‌زنیم
💦
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64798" target="_blank">📅 00:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این جفنگیات [
کصشرات
] رو باور نکنید توروخدا  #hjAly‌</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64797" target="_blank">📅 00:30 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تسنیم: سه تا ناوشکن امریکایی زدیم که سریع فرار کردن به سمت دریای عمان
💦
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64796" target="_blank">📅 00:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
هم‌اکنون گزارش صدای انفجار در بندرعباس و میناب
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64795" target="_blank">📅 00:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hjmQ10frDj7UtLXWiPq0B3NWsj8fsH9mNKRQ4-LaGZKSFma4MdmT33QdrKKBQtkjBlNPZInqKbeKgBa_Mctejc1vudBriPwx9E6XYsj8xGcc47d5hRc3QiGVq_vOJk_b0TFTNn3_nLpBHAuAX5p_k525y3iQxjetCWkIfZBiOfCUIUKv1uqeQe9SP_OXP82n5mM0h50eXPD0E5nig8dZbpoeEiO3IlfZJxCN-ZBbUUiDwgEzMnXj3NP0V7Lr9nAUjz4hsV3dprwwHme5jBfkymENMCOjUqYfS0APRCR8VFQNafakv0y7fmT2I-NsR2It_DWbmwT5Zgn_tYWGzFSlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جفنگیات [
کصشرات
] رو باور نکنید توروخدا
#hjAly‌</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64794" target="_blank">📅 00:21 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
