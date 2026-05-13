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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 17:39:47</div>
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
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/afGFBusJx8UNBcKESX3zNFv1lIx5DwHbgGUX-SU0oDLF9sgGtMT_VhpbhjvgeAw9bzCrlnnztS5Q-Hw7WaRX7OLaFBiJkm8dTTvNF4KKCiz0AcPMTbq46ysNYC92zDkk2gRlSn-MZt5YFZPGG1iFujrgDs91yjrFjV-c_U9VGM-lY1Hlw9YN09bdieEd-wydW3VgEdPpLV2fqstiNnaSyVlioeLYWqAjx3FxrBJUPA7LdLT-B_gSNsvmsHagnMV5y1CsPRIz6R1-QAM59CYHkxd5k2JoxGoa7DMPENAkKz7rTaJxdFNaJ-dOuq0m1QDdw0mFDL3Eva-_JdSKlo9r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AgKw4HvxKuTN1fCQ_gFgii0tX4YTujibBYKq635RGKNTfYDBANynFiLpEx0IwI2TXIbiffZx6f_4v5YCFgId3x-r4yQiZm65ZehlX7ubcI0Py_rXHYSMlpbvJmK90XNlR14CZ2p3vHBLL6lwkPgJLmbdAIUcXDk7VlJLTo9XpQUTyJ7bvppIwL1N_Hu2XCSUCP-OeEYuicGgL_2D6CWM7C4PkhBKVDQK2s1S9FEIbQCuK633eHIus8jUl6vQhq4NEuEM12kyxJEc-VoKS_Bfo2Y5gDaCCFb2sBnhlNywTcrcTeFb_Wtofh1lOU-kcBnoa-jn_HVHFvQXU8HzjAdkvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ikcy5UWeG-HIdYc0o225sepRfC6H8NZnMOvU4aALaPcPPZ7VFe-xB68u-iESP7E77RnmC0Pp7OKnkwAKx16yVMMsd8JYZG85b6eCVtYDHWybEfKTOxQviL_7ERunUcbQ2EfEX8X--WAmHw1QJnhtBHUCq5v7daYpet4hJqKi5HKQdAGk_HeqgP28iCXwy0m4cHQNgaEZy4LwysT74yUOsYWNxRNRmcDWCot5EHu-hOuNDwmnko0De6I7Lrl9R4LKFwehU4xs-ty6AYFILcFGyz4266yUudM6h5Mrs_67uRVUAVf3TjMQOZj3ry93Cz0p6P-ycxETSVTW2DzryAga0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LaO28VKf67RHdnwwPvEoOEeWd1C8Kp7swIDr5EMm7rh0XMYBOvPQhwBc7RQo79KXH18BXuQNhz9k5vdagn9jqXbzXVA1NEwWLAtpik_UzH5PlkTX-knbMhWWbpOXqbr2w-YL430PC0ljZgsbxqQKpqDYhZfC51AS2jCJRWmQyrTiCFU3vaHjox5lXZwBnvk4JtG3g9cposau3KKjqHFJ1ab3OFp62nheyQxd_jWz-aV03doM5sYheF7LZwyhkEp9z-V6spJTG6M6VM1jwumWKmaxebRoS6B572vw0nbym4zvfxLipxz3-mjRjJHykO3y9yD2dzzdk_K7fSJx64TD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=RJX4lCMY42g8TQZvrtNXrpXe4X-iRosCsZjfUGoCO_nMM5U2BajoujH4acuj91wY5-4WQgI7oCZfE2D0OwMBoDDvZCjKmXr_tnNJgHqrsyEwtwZ-FW05fm87fwuXwKxpPOXMkXajXMS8_Z7_blULx_MKDynAmgtVksVKa9WsBPlWP0ezXzHo179jcOUKwob-HduxpkWxhv6dM1Qju2u_-Z4BuhUIZZ0epJES1Rh-tIK_SmfcxhJS7k_tkOqRCr4eNRsHr2iPMAq8UFz2xV_nPJILV2o2dvcZXmg_-pzl__KcFADbS5cIU6uMRgUtmwHak9IClUni9qvTuNltZckwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=RJX4lCMY42g8TQZvrtNXrpXe4X-iRosCsZjfUGoCO_nMM5U2BajoujH4acuj91wY5-4WQgI7oCZfE2D0OwMBoDDvZCjKmXr_tnNJgHqrsyEwtwZ-FW05fm87fwuXwKxpPOXMkXajXMS8_Z7_blULx_MKDynAmgtVksVKa9WsBPlWP0ezXzHo179jcOUKwob-HduxpkWxhv6dM1Qju2u_-Z4BuhUIZZ0epJES1Rh-tIK_SmfcxhJS7k_tkOqRCr4eNRsHr2iPMAq8UFz2xV_nPJILV2o2dvcZXmg_-pzl__KcFADbS5cIU6uMRgUtmwHak9IClUni9qvTuNltZckwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBveMzQQG-7ue1eg_7sPCS9Gs1lDfp1UQvbUtiJaqhs43XfEx9y68bl8L1BaewzQ8IDTBZY7xspLfcBETvX2eQIVbsbGe1jC98oZnsW9e3EBYO2urI8wLCPtiA65TfSsuCxonCjBmQdlPi_6KQINGSSM_Dw4Kxd3GGBBfmfd-9stHp5w-WZGhwdVwNLHFcfvzVb6wX0URXyo7XMSfGedTEqiN0QioMsI99sGrLsYQUNtpexLansJqzD_8Q17uKdYuB3ZcuvtrDULhx-HRJQ1xTRV0rLQGD_h86QOBChun0H154SWEiJUeoAE-P5qtDyMFdFVeVY8f0v_wLedR2UL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCl37Rq-iUihOSONMLsxd7cvd3-iX40m-HOEQJMExfKD5nSNdcGBhKVfOS5awT_TqEpkLFQz5cyyRkYW6YjDgezFrG1mzdbICC4s3PWsTuS9ctdWlwNnqd93LZX3KwNhjjGP5UBV52HWTfBARQIQzNL_pbzvYC7FfedDY7hYl81IiC_ncR4YGwTqhLoNUCFgG0pDp1FUq-YY2Sr0R_Jctt6kBLNIpAi00Lh9Nj1Je7KOXtOHGMGnimIzLSL7rH1d1o4OKNTMEO_yB4MbtB8g16BRZpOWgltScoGfXEXl0RVs5BeyRjDVs__RpqTFiDEuQ7bybPSFQbUyAlIXeF4rvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQysQHinqsomKPqVYfoXclJPvQYYuRTAjiLI8QzM8dW0ejgAvbrgk3A1PTOcc0vn5K6vaD2LsPhg3_y3WkW74JmVXAUmDPMWRvtEMG8m8qNsjw4IOMsCmz3xmtiB1eFXEz-m3zzapXX3AAdxKmF2fHl44u1NJd2cL5rjjaFOYlTT-4jKPOX7HW_yr2V7uuAiChw4p48XMUYTvTj4DAzqpPxLa6VDPSKWCmganQcu5n2rFzj6EQk-fLhHRsZYMgBFRFi_xY9ltEktiFgjatJDzb_hbHZ4kLtrIK-IjnHe_4CnTrEVTQlrxHglFd5PaEjpzihwQj9qI7hWtLhHaNer4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLpPWhm9496ltama2WgI919X2ESMNLyIXsikV69ZUF7z0R52xeBaeu0y-sFMNDJoHGu8AK-05SXFSWtfxOYwLBE8W_uhyWdByZ3WHFRBfqJ_Pv7Y-LC8oTS_gGlqCZIgQy8X6d3dQhGF5UqIidhKel8X9KdHjh-jKzijW-kQBvCcEben7_d2GhGOKFf0dD98zP54gMu0rSdfxwBfdJ9Zc2oQStKOqpk2Ndhlto9sK59bgqBgRRb6JlpS1GQxut6CiZUnxUR5h6jN0MKh9TT1CJ6b3DrtgLhUxAQL-6gSynT3WfvETv92VZ5sqvXktbVlKLcz4IVQDZnQopkK6dzqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hfrAH72CDy52Ht9k9YXVopu_XD30XBXY5WVXtswGuYRV7q7OnnMqJ-QmWn4CcdyaGGKD1WENRj6B7IudBnjUOX8VlqnqTrAL72xzgFq3siSFN6qk86mchYDdut6HFgoEqgUtB8pqhcJ69yjiyvOd3EqVXGa2vhGWTeuVcjwAX_9dCFFyDsE8_w0oxotC9q0qTbxxLrqOolt4vaYS80qsNsb-P-wvepAgQCMkWNqMPQIhLJJpxv4jJBj3CKNxiSXxRl2CulBYrGx4ZPTyZV1oImA0UEuTm28cj2h3nx84WnAZyndh4Cx7mdt5LDhHGfn7fiXwWuiEq7PFjRFx-Hz9Iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay29TeUCDf84n7XYecu9WqYi1SjQ7HE5J2ETalUd33E_WRGcmny_IuHvPxCAlnBXBWwpzX0RW42_npO_qGKpctc96NqaFHPVDAAcImTWtfq1dUm2oeTCQtHORPZZaydH8FQsyS1t8m9Oa1thbMddxLSCENq68xUQ6Pnu_WUxMT64oWRNWysYTaXNbN1PGO1V1P8clVVjQSxbGZI5KeTZ2bBsK9awUtbl5CgWzBAinsngwiR5uSb0Q2sID8sXQeUdNF2Am7_CbQfa5qJ2v7DZ-ELv2vbsx_UCC8BsapwmbGm50132vBgOXOTDOFt_10SxOOHvXE1Z44Nxni4bB7phew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H7MZG_kdkPZqpryY2ETD8oMXVQ5hyHMCi-NbUkQPOTVke4a9UWMc9fNiiFcGcQwxVaHapphnQTzSj-hNk3hI0bxBl7eBE-jkx9L5oe1Sw6h28iP1118lH3teMftchAx_HJnhR75nabUuElDfQlABErcbk6CBUTMHFV7bEsiZNL9UE2Ul-aynEoy7LhCDX7fcxqsg2yCS8kmsVmNjG99Kn0Mv9KnL-X7-Zncc7Mj8vZ2hRjsGuhPtEld5pv6SUgWPx95pFPvKX9RucksNk9vLw9QdIxT_oLo8lsADfrZnYuwC1FlI4cJU3vYOrsViT4hL4q6jM8auaNpXp01Ux9HmRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UjEZYYK3WJvEHGnnjMtKejm081Ssb9-e_tztIStKaSuRtDzWVh28cRkIpmfz7ix8aMtmZU8fjbGqVyqLKPMr2RfLD75p2asL3RbufUNH6nrxur0fo77h4p3ffNAZHSmZcc7Bl1uD9NExMkrGUhiscxxAUvYDtuqsn5zq5GM32hpRxFA5PRqjjebZcfxk92Si4FH4O2r45dtCfNav6UtZUTdXFDRRJDQlUd2ICBYL3nbxYQyHXn6I8-RzoIlOBIRcPSgqqHSFVse__p524uy-j_Nk506SuEWyuBLCiDfnaSf0dYAantaFVaJGI7RUbUKCejiBVCfhtVwZCVdZyxmcYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvNQppbpe9IKhIbMSm38ZErmpbYUvXASA3eCybYpYG2gMU7TQ1joaKIj8FPMuvf5JFeLcx7BDxxgU900VSLWON848qZPeH47JMFuHr3WV4l0lX_aj8tgNMhPeNbHNlaOewuorSu1dpYCgsw8d54P4yrqa0ibCB83ilWNO8g9P-wGVlKLdhtb66Ks7yblNp3rgRi-LW-ysJi_XSjBfLVTU9zvgKEuUUPwuxxpmcUgfE1V75TLkOcVKImowAhqWLAMDgOenTliVdAr2ZQo9Yq1OJBlS-1wdKkPN3TeWNLOxTa-2_pw6Ttwrecs4hW8o7MtAElQVMccVNr1zMnrHAZDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ij2pBZHhe0PQyX0v3DyX9Cbr7zDrFhUmbcMEUZBrELrVXlpQHGPQS0ZRg0z_2per3JnZpKHhTQ20UxYzgijJYNxwb4mwL8zdS_YZjpVb_YoqJu-eLImsVQbvq3AFHlb2uh0TM7hSUtO9xHlys557bSikBWkRLT7ce087AjqPx-qnDez5R38NZQJ9K-MK1VcHryU4OdtxxjwYm8EZMrAjW2Iu-760rVUJbJikAu72lmDMB1pCzpAkPqchv2cA4RsXbNmd8be5oJyG5EKEhw__yRTboPNfcmKilsXvz2d0WBm11hCESIKN4NBKiBuLNeS72_fnoAI1JbFUQRMZtLPVRw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=MJWS_4QsDUtGYZXXnXNpKJJ3gN_w0-AI-a29OEkl7SnmZuSAItmwAXQkvLLzlHLWX6P6ZuLsXBMCqRhj8hY9vG5aKAQVDUH3l3LtFJSpeDibslwhxqCxkU69CU1apeAYkn7QmTQc3deXARgubDy36wUk7GN_sJtxIrMXsZ7MfLkYhBq6Bqw3fSrgKwAZNMFTeo2HyfddbP6zCSREJHXb5dDqtW324X9DVt1c2JRGxeB4NdY-6iH5_pPDsNXVSvMozCxdd_Z18wqnI4IbUOtAkHYBEy06EhU9ZBRhv50ekIM13jZeA6ysQhPUQn21qvIfTtbfhwd3DwW7wkgopumr2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=MJWS_4QsDUtGYZXXnXNpKJJ3gN_w0-AI-a29OEkl7SnmZuSAItmwAXQkvLLzlHLWX6P6ZuLsXBMCqRhj8hY9vG5aKAQVDUH3l3LtFJSpeDibslwhxqCxkU69CU1apeAYkn7QmTQc3deXARgubDy36wUk7GN_sJtxIrMXsZ7MfLkYhBq6Bqw3fSrgKwAZNMFTeo2HyfddbP6zCSREJHXb5dDqtW324X9DVt1c2JRGxeB4NdY-6iH5_pPDsNXVSvMozCxdd_Z18wqnI4IbUOtAkHYBEy06EhU9ZBRhv50ekIM13jZeA6ysQhPUQn21qvIfTtbfhwd3DwW7wkgopumr2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unKVzgw7vviy3_0FFddPRmS8H9Q5Bv_viZvwBBDpqZCcBkviY_yWMSiLH78eVcqo6xbV87-d0o1qYfj6SzYqjkjusw-iv1f0Yl2jnvPc9UtrJPTzrR_cpjgdy4VlX7MPihNAb7w-p38gtO0w78Sq-cx2TfdNJ50Ol-dv9gj1L9eycGLO3ujZAVEThPaM9DQJJfRdP5VdPBy_Kdv6GC1sUEppxwkdP6PpHKs2ZqOMrJQb66h7F8A59KQkFXRI5CLukAknw3smlAEqrsxXOhkkd4qDDLWPjo6AriWENCX2P7CcXJsoG5rtvf5IdlqoH77RhaWFz5gzRvz5-X7rneT-9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=QL2M8AuxWd0mj1NzbT-VWOJFtq4OUg1P8XWDgniUV57IfsjCqOBvf8ssq4VuRPeXQf_p2Yf5Eq3TCwgllj7NHphYqCH_vo98ufSlOrLBYZM4keXh-q-NxNsTNJODtBpMRCGl5P3ea70IgMXiOETWNUKAFmG3dEGqP9YsPeO2QR7zUi1hecogYWcttbOtm6ndeQkxqv3oINeSLNasVw9sBmsPdD9xln2RL_iB5az6RrcIxpSfnPHV-ITDwLxMVmryCcTxXzNjJ259MEmF5wS7hxrhj3DCFFbYgzH_BNKokETBcmdkVeT-zKCDZI7tDaFvCv579fa2tvCrZv8ytB6K6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=QL2M8AuxWd0mj1NzbT-VWOJFtq4OUg1P8XWDgniUV57IfsjCqOBvf8ssq4VuRPeXQf_p2Yf5Eq3TCwgllj7NHphYqCH_vo98ufSlOrLBYZM4keXh-q-NxNsTNJODtBpMRCGl5P3ea70IgMXiOETWNUKAFmG3dEGqP9YsPeO2QR7zUi1hecogYWcttbOtm6ndeQkxqv3oINeSLNasVw9sBmsPdD9xln2RL_iB5az6RrcIxpSfnPHV-ITDwLxMVmryCcTxXzNjJ259MEmF5wS7hxrhj3DCFFbYgzH_BNKokETBcmdkVeT-zKCDZI7tDaFvCv579fa2tvCrZv8ytB6K6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=A1YMKq2vdaOltY_QdYkHqxCQQb51DSb-na9uTgbPYulIaxlPaFWJKUbksN2sf_5RY2UWw-Vm8RokHLQB7FGViU4M3yMrBBz0tXq43oE56loMvhJCpKz1D6whyeaqydFh14c6l9KeCKfJUOjxyFSNWH0OIo7YbOhagqTpSp11751uAATAU-89-WpWcW0SiaGJIkaFklKR7EwRaLkct6rXUmBZ-PzNTXxVi-GtkQgqHV0Ih90VbQwxv5EzhDooLFpOKJTXSs6HA627LcTGsC_-9F9cAhofW9F1h3mBJq0-AqxxFBXc7KkEmCqAVlOAVBW664oVMnSCnz2PVnAUftd4Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=A1YMKq2vdaOltY_QdYkHqxCQQb51DSb-na9uTgbPYulIaxlPaFWJKUbksN2sf_5RY2UWw-Vm8RokHLQB7FGViU4M3yMrBBz0tXq43oE56loMvhJCpKz1D6whyeaqydFh14c6l9KeCKfJUOjxyFSNWH0OIo7YbOhagqTpSp11751uAATAU-89-WpWcW0SiaGJIkaFklKR7EwRaLkct6rXUmBZ-PzNTXxVi-GtkQgqHV0Ih90VbQwxv5EzhDooLFpOKJTXSs6HA627LcTGsC_-9F9cAhofW9F1h3mBJq0-AqxxFBXc7KkEmCqAVlOAVBW664oVMnSCnz2PVnAUftd4Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B043d_HZsaqFimC2qQ2ZqHzc75nOty_NpzOX2Hud4j5HgCStehWLlzBYJyrLSNxPrNJUA02qtAGA1Xkvtf86DBrR8th2XCJKvvDUpnD706er4trnWl3n25rQpDRMeYyhfhuTqPqN6ewl98XWooXTJHpABmWoE0mFBZN0y7Bhy0-zSzskiqq1c7a-YZahEaBcQ1e5B_ad9YqTTQ8VAG2Tdxg9YIDosqi2IolmZ7peLrjkVAu1FENs2o-92cq5Ue7hsMjtn6JK0W3w0HeeXHLdR12aX3maZi7811JihJSf1J_tPAgCy5o9ZncVVaGv-c01TwVt86kA-aa1Bht6FI_blA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JoFX4lYZUZc1ZhK4N5ljKsvEempiT21YuCt7VMAqWpkrs0M_5eqLwfhpFsj4vkSAZjNv4ihd26qyUXC0y_5eoZMA-oj-oUjMLC40QiWpag7oor7xJl84dPweF-7yNUOW5SX94eaDPRW7YQsn7pZrV8KAb7xBitwQjEyuazD83IyF3piUJYlUiSU5QI12bxP9cVb9-CREh-XSlrSCMBfTcOzLhcrENnpGwA0YDkSflGQmJCqsody6CNGoUOA3ygfUHpI1nRrkvgkuoI0RK7IvpuLvy1QCx6niUrUN3KacOIL5L5BhfOF7-jB-l3ahZ40XGD_BqTYV3wUZfpVepvUWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=gIKytxyH238USjbp96RgHTm5d8orq04SbI9JB_HPEONwkiawDeADShHVVSnE8ojF_zk34XLiXEGdW6e1Rw7n7XOI1ZPVz0UcJ9Q_WbQpewC5jTX5hOAgI-4fsNvXfqTPPGxldHK5AspckYW3T9xJ1nXK0ad4EI_6J5lzsA9ETFVEtgAL63pQAR42QTC41FQGn2cRkO8rIEqanWXurmOnWzu7QbwXsmC2eWSUw55f4rROCUFdu6VC6Zh3PdcAreVAneFLex4tmIzpbsnaZnPg_PutKU0bYH8YxNhO2vANhsOOem9ole7WEUoEMqCt8tFPoSMPj0zvLWrJ34xpKrD9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=gIKytxyH238USjbp96RgHTm5d8orq04SbI9JB_HPEONwkiawDeADShHVVSnE8ojF_zk34XLiXEGdW6e1Rw7n7XOI1ZPVz0UcJ9Q_WbQpewC5jTX5hOAgI-4fsNvXfqTPPGxldHK5AspckYW3T9xJ1nXK0ad4EI_6J5lzsA9ETFVEtgAL63pQAR42QTC41FQGn2cRkO8rIEqanWXurmOnWzu7QbwXsmC2eWSUw55f4rROCUFdu6VC6Zh3PdcAreVAneFLex4tmIzpbsnaZnPg_PutKU0bYH8YxNhO2vANhsOOem9ole7WEUoEMqCt8tFPoSMPj0zvLWrJ34xpKrD9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=OCeoSBQlbGvye7bXUCBybV0xLYUt1S1T2027KAow-3XB2iZb4dtz0Vix-HksZMfopeJ7vQZq93-I5I322lZPzYhyKwe1Jx0SW77rizxqyEG_LEnOwzL_n69sqgKEpgj6hg0TPivTWgOqhg5kjLt3AlSwUVn_XeySORoeQ11I62o-u6vmi2-n_22okq_3vnbpK3uaSf5FvUzR-fd_wwl0ujJGH94YM5BFqJnkatRpq-2PXuuWnQQrmf95Odxmr1PLvqZJM44B61CSBZUSe2jjnRC7Xxrfyvk5bybm2oQC-gCYZt-OHWkQFX4UNeA36pZ3amOhO_jsXmX-rCmMqqMBng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=OCeoSBQlbGvye7bXUCBybV0xLYUt1S1T2027KAow-3XB2iZb4dtz0Vix-HksZMfopeJ7vQZq93-I5I322lZPzYhyKwe1Jx0SW77rizxqyEG_LEnOwzL_n69sqgKEpgj6hg0TPivTWgOqhg5kjLt3AlSwUVn_XeySORoeQ11I62o-u6vmi2-n_22okq_3vnbpK3uaSf5FvUzR-fd_wwl0ujJGH94YM5BFqJnkatRpq-2PXuuWnQQrmf95Odxmr1PLvqZJM44B61CSBZUSe2jjnRC7Xxrfyvk5bybm2oQC-gCYZt-OHWkQFX4UNeA36pZ3amOhO_jsXmX-rCmMqqMBng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jk9ATeFvcrU8Ja76S5Gd4noZsg3XQmyqmvUyiBXx6fk1HSUNk8pDm82vQ-b91HLb48t3CAa8NGv5WO_GdYUNfDiGHs_W0JpB0XTNJ8U6hx-Y2mQo4ElrIw7Y7pSuYjck_scNI632FKqQzEXVSJeTNaMRBlmiMly7zbscquYA73UITHNUcM6TpE17XEfSw7obuP1v6aWJ_KiyJ0bVPCIYhjECgOZGZFhJ0PNaXdmo3XrFk59BMIxDYKJQZuyE7G0eGd80kO6Mu6n5of1ZWTx9EDDpASKxoxCd6kyGGy329Gd7WjS_tNkR6F7E_jpElptUldmJmJNKfnUJreOB4aaB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8rFxEOG9RCs2lOH0mgDO_37fEDD97eiZuT1yykTjEzk2K5xjbgMlpx-22TCNRJTOfkZ1IjpzUbcPc2fQtHfHxdhufHZJIIA02Hj0kWlbAJV2GWW_R-fec76xkr0hZ8jxsk6vd7AInohz_1a0Gewnjmqb0cm3pwkAd9B3LJM6JmeUg5PFDJ4hWJ7YayJFsXD8M5NjZBjBwG0Ur2iCLOg57si2EOUOltjw0LtiXxfedU2O3mqJXPVUJyT4UrvyttDdoKKstq6RAxv1H22Zqp8CFfFqqp1OyMayyNT0L5XhTo9vawjY_KibgOah9L3yUN-f6L63FKv17--b2bqXud4hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axzoYDt0-lEgQoxWP9aONde1NqeGvBHEptLjM73jqJcrDalaYuOR-9H7KAIwBQiMc9Ojw-zVgpbvNZIDPoiUZc8l8NUXRk6UhX7LpAHxMIH5-U0Aj-GFFzVoPI1ynMZVHhu21kNBtpZHPOqX_GEHkgyW6ga8vN2Tg3xkxoKTawbxx5HGSbHsUASHiu5fQvwVaYDMf-8QaUc5iTNix0b0GtMr9PggIL_tdqiNoJPP6SNw3z_f4Mckps1XOp17m0jvWxCKMPJORyNbv_kJxujWMWWTc3arRB-nplMh9jWjFu2O2DofzVdNMXP7UtgSDHeOikwX1qPwQxlQrpLc_0KYuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzBTykDzfjtH2B7qkjDfW2Xqb5MxUsdlWUmuXm9xhxCaEVe8D38oxEGO6QroY4GiTYtbr_PmLLcYxYRQkn7JnYkXDKIQdPIKQk7HnL7CMszurslktxctVbcmWSliVqgKH68dY4HDjorNoN5iYx_93J-hJRRmAqahyEg65Fn9Go8y_GrMriV9rm_VBGheEJ9CYsACx5ZMHEI6NiwQCLhEiha9EzpeBEVJL2Z9kY5z0kbcRNfiyXy5gqMdc8C428il_jCtc5xxMAcrmahQ_ocE3O6hAi3CogJ0dhc_1ur_LSRbz7WimvmIbbvdDeGxMf9WHP1yjvI8QFX57sH7nKuFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=JLjVAd5SN0aEXUxRfWMDaDaxseRcXgC1B8isxbo1ZnN_pofCwn45IBRdxlnzX9YpZZNxqwKnCqJepVA0RQLCbrW6pWCS9VKt7OjQuifa_TIl67x3Wcb32ftX_rU-upom3ENGoFCl6fyq6THuvjK_RT_sYMy8ApXRscXY4pFzplahjJDCawzF5lh3zMA0bPIDPq4YwV6Ud2sgPdeMgYZrej4eU40SJjqj4s9gP1acKM2FOrRofGXLOZ_KRcGf4oo8C6OBC92AT5gTS7EzGcMbEpszozULo5hBKVFK5Ha_Yu_dZ_ctc6Yl1OpmYt3lNPi9RrAvosKdP_nRAy1rsd4O2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=JLjVAd5SN0aEXUxRfWMDaDaxseRcXgC1B8isxbo1ZnN_pofCwn45IBRdxlnzX9YpZZNxqwKnCqJepVA0RQLCbrW6pWCS9VKt7OjQuifa_TIl67x3Wcb32ftX_rU-upom3ENGoFCl6fyq6THuvjK_RT_sYMy8ApXRscXY4pFzplahjJDCawzF5lh3zMA0bPIDPq4YwV6Ud2sgPdeMgYZrej4eU40SJjqj4s9gP1acKM2FOrRofGXLOZ_KRcGf4oo8C6OBC92AT5gTS7EzGcMbEpszozULo5hBKVFK5Ha_Yu_dZ_ctc6Yl1OpmYt3lNPi9RrAvosKdP_nRAy1rsd4O2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsBYux9euMid2vIBQL8TwJjwc0E_WbrTBIPHSAkgDKnjzlfCZWX2SmDCSQuY1Pw1GPP80aFUGsgABMgTL861cvtoDWWR3ubkDQEsYgmvHcqmdkSHxXmVb-X8C5phfR7YBaaUM1lftQwn2RUCmQTSFPts-EG9FaOh11mJ6LIihqr7nrBT3fwUE6niIWWCxX-7UppREBTTq2zJ-G9nX3t8ASabzEGcb456FoYlPgHCI7pL0oN4hbpdVzKr6nwvRuq4xzp1OVffWEeju9PrmQc-SS3L6Ut5_-9p9UbilAY6_iFQ8gXarJvluDZt9wbdSTChqN-w9WHwfbQNrjTJzeb9DA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=ARXdI63Vn1bPgW2ZB8A5OpPizg-ph8h8cKJYHQL3aTWSevq9Zb-En6-z32WatcC-EJ8UtvKXHRF-ArOR223_iUvbxVn-gc9ldAZyGXgZddsYXTjGBjj2bn5ZLynNKNlT9sOfD_xW2u6dPmm9--kJOdkBWauEIcL_gB6z5Bzt9J8jZ6zA9vb-NExE4jJ5cIXv5Ckhx6Lzu6b0RSk05fRTSTg7I4p1uw56DGA3WWYv51Xp4gSJ0JRfymocOIgw8pVcjQpz9gVEvmdkCwOm7MJocSeen8uIaZH-kFT0wyA3IOJO2jAqHiQJHUAOcUn-xur0nFHBqOjRgrm3bKlQXOiuag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=ARXdI63Vn1bPgW2ZB8A5OpPizg-ph8h8cKJYHQL3aTWSevq9Zb-En6-z32WatcC-EJ8UtvKXHRF-ArOR223_iUvbxVn-gc9ldAZyGXgZddsYXTjGBjj2bn5ZLynNKNlT9sOfD_xW2u6dPmm9--kJOdkBWauEIcL_gB6z5Bzt9J8jZ6zA9vb-NExE4jJ5cIXv5Ckhx6Lzu6b0RSk05fRTSTg7I4p1uw56DGA3WWYv51Xp4gSJ0JRfymocOIgw8pVcjQpz9gVEvmdkCwOm7MJocSeen8uIaZH-kFT0wyA3IOJO2jAqHiQJHUAOcUn-xur0nFHBqOjRgrm3bKlQXOiuag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/InNbc0pybTB29Bl4xmgKnjTqvGm9oSDPVWfAnV_x4zvyPkl1WybiHv1Qo5CCuHc72aXb7cmEMYan-8i2NLF8_MN4wvTbe7XAd5nnVHN2ncrfHABzJXpKcY-e9IyDdfAnoEqllDq_RtlO7MpdnYzAnAefiNxGmwF4rMjWz5AJrP6Dh2QXNTlnAr6BPKQuriVyRaNAY5-NaqXlhowil2aUHj9vww8k7H9Y931HwNML9BAXOM8Dndp70IZCcuKgk2ZbC9FVVs-gbeSVCjjsVPxcBIBciyYWuPIwfciSMuigbZb3zJa35EMnqtbNmtjN3caJ70pqWmPFTjv9VNZhoMyzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gljV1r1h68PNjZcs6goJ3I0830ULj1srXSqe1W7Js-GNVfLV4kauqwdUnaKgz8_urU7MgynrUdvta7eclXb6A-OduduYNncxkamVbTJgmLgVqbQlZumXm_rMapkMvhObJcMNhe5dMYF0vPFQPZuWvhzQ2GioxTJG104Jd77hxIGN6jyuKuYN-OrIfq8haRWa7IFDbpqg3W61UT3pDe4AH0J0nkWSwdgxdNMdXxNd75L6-MXRmr3Gb_tDqtC8nNrsgLeVqLciWtIKcph5K2aHs8tzoyCgazjwmW2ioE-fsmEIJfblJGH7mwuwIB1qv8TkGosl_jhuUhEiSwD-Dj5Z8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgIyFmlxAtG6edJQQZWNROJceC9D_sLfAJiqPm5gW4e8v59Kk_iytr1XIXsdTBKxmTgvsH_EnfxSaxQ4-p-WXj1a4j6Ev1Me63HrV9gw-sO57cbexfo5JgaedEvUjsmobhXfZc84dsoAgGcFsMn8UoveqdVxjGQOx0RXcKDST6plDKpSHyKzeDgR6dhoIL7x2FP3neScVUq86KobGcygbfmLE1LBUZg1iUGIjXqgoJyJ5GErs828z-iPsTp_rqZqIP-93lBsYSXCeTTAyQ7k9NnaEobjwaeBxM33IlHm2jDH5DX6RQf5n9ltil2Igwjwh1IFSgffYDn-KWcXLA-Ngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7sOBmn6mfm7MRey2dUCWTjGt-tNJUfIRz6FPGfsvrUwQcC4WQ63u4kqhNbLutTvOOP07xyLZThlovZRCFw9inC-9cQ4vjNoNXTylLOQtokkxB5T0ktDWWIE5bzaE38shJoGSTmYCiViB-hdFRsK0aL00FD9-htupvBssUJR8IsF7v6aXF3JXEtooVEjuMzTdC9hRFGKchwkFTktmRjzJXHCW9to1VQiS7VrXBEYwokNE5S2ALlAjRyaL2gJd-0ZYQ5bCNfqsXilpmyM-LEZ9bO4q_Mqc0iGrcITVg6RUJLrit4yyO5Ge-WNFDrjYndnerdI5pIegqPmkjrB7N9dtw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=HnGv_LYbEPh-1BEoo1OL5pVzZa_qxhDP6r0YM3rE6Fb7M7EUD30_W7ZGQER9DxLnlPIX-Put2tZvCpqoVr1FPfYtPYkvXzJIpGBDsGlO9HAAm1AmflPxd4WPfPWYKTIC2a4B7zw5xJAWcxbP0eEqoAbvAFzum0uG_M05Ptc0P-i1A-pzgSBrAktf6LftN_OLBpifGs54P262WC_7yQnIg9oUdq_N226cNosy1gJNtAknHaoAYVHLqnGzKzmbgS1NwUP68pJZnyQcUD6ureq_6rAPyVuVsxLpNzMxGVkz78YzlWEcaHId7HRNIyhWygfqTM5sirQUA8iAuV5Cwr1e1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=HnGv_LYbEPh-1BEoo1OL5pVzZa_qxhDP6r0YM3rE6Fb7M7EUD30_W7ZGQER9DxLnlPIX-Put2tZvCpqoVr1FPfYtPYkvXzJIpGBDsGlO9HAAm1AmflPxd4WPfPWYKTIC2a4B7zw5xJAWcxbP0eEqoAbvAFzum0uG_M05Ptc0P-i1A-pzgSBrAktf6LftN_OLBpifGs54P262WC_7yQnIg9oUdq_N226cNosy1gJNtAknHaoAYVHLqnGzKzmbgS1NwUP68pJZnyQcUD6ureq_6rAPyVuVsxLpNzMxGVkz78YzlWEcaHId7HRNIyhWygfqTM5sirQUA8iAuV5Cwr1e1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C74GjNUn8ejaSD_deiUNBD0Tfkw3L0_sKC8Y6Wx1Q-9ni-dWs78HOTf2BjaWK3YQeuFyWiBO-_ccpnavAawJX0pbcYyBiUUNWyJfi4umyquTQjtjbBvUSP6ae1DN2TVL-vs_U_BBfeL23WaRlI0FWUpdw6xbz39X0z1Y7OXrq4Xa0HhgvqBCq_FYSHW01yqZIGD_La00d1InogfscSt5xgh8kc4mYIUubhmbw186n-n18yzT86Mjvf4XOqilQbmg4IP4C6cTYlIBqhz3WsWUFla8sXEws-45mQXEd6v9Cgbjykw6nbfrcIRBfyZivysZZ-JqOBMBx_SRTiI9goD8OA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1q0joIZyQlWR0iVC9F5s-erev2YGyGDSQHremMQoKCeqjk4r9DNyuGekmydf1ki65PkMoNVkrutA4zuacvP4u-nqrSPqLcW7puhVCelxr8iywj641ruV38UQSogt33oNu1YRJ5t7UInlIYTSbDrxhOYedBTU5Zcq5cef32aX4KJzqGt-tRArgnv-09Ru3sgOAlkks2P5Si-LJ2uW-ApZySYUxqTbpWyVkrZ3wMUnDrDHf2qbaoy1g5uQVy5UPJVYpp5p5nORTlh8AruiLVYE1DoFHj-Q8-7mEY8YLqdkmURALGLyf6IrQ8FiHkLHtHs-zbmgy3EwgvoGb_4vN2Xbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
در مورد وعده من به شما، وزارت جنگ اولین دسته از پرونده‌های یوفو/یوآی پی را برای بررسی و مطالعه عمومی منتشر کرده است. در تلاش برای شفافیت کامل و حداکثری، افتخار داشتم که به دولت خود دستور دهم تا پرونده‌های دولتی مربوط به موجودات فضایی و حیات فرازمینی، پدیده‌های هوایی شناسایی‌نشده و اشیاء پروازی شناسایی‌نشده را شناسایی و ارائه دهد.
در حالی که دولت‌های قبلی در این موضوع و با این اسناد و ویدیوها شفاف نبوده‌اند، مردم می‌توانند خودشان تصمیم بگیرند که «دقیقاً چه خبر است؟» لذت ببرید و از آن لذت ببرید!
war.gov/UFO
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64825" target="_blank">📅 22:24 · 18 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=QJHfyEaBASNoo-4VY3IMhJaA8cvqDmXGm0D0_n7ND-1v15qfn0xbUYSHQqWgFCUr2-M9VMvHYi_RA4ZbG45jimBl2zkMz5c5I8yB7IK5lujsD0zX3oaZhr5KvU4ademxM1AvVo-L80pKlUpUsPgv_o9v6j2am4sHXFvATv1pZfwYOGWKrB0JqckSXjPAlo9NofOAZh2TNL55YfiirQsLQv866gaZGWf3F-hL8ZcMpxcm3iUNc5UHdIXP8oPsgzqawRQ06Jix5IfdY3gO_2_Dhz6UV_40a5DowbJh8457x69ZMAc8owK_AEfuI0J087WfBu62ijbOXAJwvWg4h9PjbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=QJHfyEaBASNoo-4VY3IMhJaA8cvqDmXGm0D0_n7ND-1v15qfn0xbUYSHQqWgFCUr2-M9VMvHYi_RA4ZbG45jimBl2zkMz5c5I8yB7IK5lujsD0zX3oaZhr5KvU4ademxM1AvVo-L80pKlUpUsPgv_o9v6j2am4sHXFvATv1pZfwYOGWKrB0JqckSXjPAlo9NofOAZh2TNL55YfiirQsLQv866gaZGWf3F-hL8ZcMpxcm3iUNc5UHdIXP8oPsgzqawRQ06Jix5IfdY3gO_2_Dhz6UV_40a5DowbJh8457x69ZMAc8owK_AEfuI0J087WfBu62ijbOXAJwvWg4h9PjbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64821" target="_blank">📅 16:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64820">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: امروز پاسخ ایران را دریافت می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64820" target="_blank">📅 15:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64819">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9knDdKuJIor74W8B97ZnpL5PA1xdi0KNQdbS8mylbsFlR3guwd1WG7cpBdLNpGFs1poQPbr-KR-0Sd_-43snBpMf1Kjarsx82fbkQgxqlrYVgTWx7c_riqr09ngqBnILYJyuBIQ2ijfprjK5MeDIPWaiFJtKSZKL6V7GGh2xIyLiMf9V-izmybW7DMupIgRdqcxtwGnBJpHIzlHQFWP2VaMkd96K7gSFI4aMqT90QAUrzxb8KHtmsXapCAelKN-0zgGKhmz5-cfPbIGpKSjoNW3Me5ESmg39drAG_q2CVhD4JLjVwbgLjNjBciFUAKJfpPZYX03xPGldrnFTaCy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات که نه، حتی اسرائیلو هم بزنن ترامپِ کاکولدزاده وارد جنگ نمی‌شه، چون سفر و دیدارش با اون کیری‌خانِ چینی براش مهم‌تره #hjAly‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64819" target="_blank">📅 15:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64818">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده  @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64818" target="_blank">📅 14:59 · 18 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=NXBN9ZZc1T3z9_w_p0WwE3Br6KWNGwIqfar0jySWuouLqFGCf8dYaoHDf4j5IncUpLtpkswjYuZFXhbAcDrGO_2u6J6pJqMtSOukqt0ewNWKaJbaIcApTydKOmnqIZkrWBaNeY3EVIrz-9amvX6BqDfOS5WSu8Ay215NYSHfWt1isD43juufwUxonC1d-teCJCo63Gr9aIskyKWZBEUDYvWa7ZfB3k1x2VSiyOUskdTKt5ao62UVcSt5FFvShaEPNdGir4oIUruEjt7gmwBmU74Z-F5g1Pi_4Ya35K9Bxv_RxyAY_RTfgWQO3t4nkBPT1GYNKgCnB6xzfcs_lFp3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=NXBN9ZZc1T3z9_w_p0WwE3Br6KWNGwIqfar0jySWuouLqFGCf8dYaoHDf4j5IncUpLtpkswjYuZFXhbAcDrGO_2u6J6pJqMtSOukqt0ewNWKaJbaIcApTydKOmnqIZkrWBaNeY3EVIrz-9amvX6BqDfOS5WSu8Ay215NYSHfWt1isD43juufwUxonC1d-teCJCo63Gr9aIskyKWZBEUDYvWa7ZfB3k1x2VSiyOUskdTKt5ao62UVcSt5FFvShaEPNdGir4oIUruEjt7gmwBmU74Z-F5g1Pi_4Ya35K9Bxv_RxyAY_RTfgWQO3t4nkBPT1GYNKgCnB6xzfcs_lFp3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ojXshXuD5ytJWyVEP9MvjERFfz-Fs4MVN4psIhDnxsNV69NOXXpIf2OoHBIDJ6_FO2l15nq68TZ-b9j1JbLWTqP_Hf--OkQQKEJXhT9BztcVAhPO7KUCvADx4OisIymZsmGs_jnBXe2-v84e75_f0yGsQD_7vvklcTKRJjzCKGWee9ZH_1vEL4RTRv2Eo5d283-0_9ZFICndsGnVhKKopk81AE7Ht1C3lbZsvwv0wyamvLyC07feT_ExqGBYBRmK3Xk7xtVQSOWTHMcBnaztAKnebsPkr2QjMRCHNtzEhn-jA5U3B7a-LY9VueH-cnO3UJ-PSUoiJRwkFqdVfTKefA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5bkFozo7xyvkcwZDNWyR4iow2rKXj9QQSXzm5WHetiHMXWS_VWdtnHdne9znuPRJgQygwjleMtfR8P3iebs9KYkdtF5so8Xag8P0ojkSxM5W0uAszORr5SQkAP43XGSrAUbwOoymHB9KNSDIdCCpZ6vQZf-xCPpOCg_QxcgpCGSbUl8YVi88rrWu1VUrAqXoYCs3hHh_u-ghr7nLGBQZALV7wlJPUv2N9DdYWRYC_d0L3m-gW2bVhwBBbHod3eJWej4Tr9fU3d8QAgpO1dP9odTelYVkvvat8Ek0-ERtkhbYraE3zsJDurQHSVbUvMS-tu62PkNAvWkJKwaEjrTXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulVRllaQ9A7fKKI9O1eQNcjB31eVExealLGRg-KPoTiXnUBThOMAJCBIN1Lommvs8UDJtCjMSLYXqud8iY1r_1WT9QyiV4C9vDJebW_5PNq2wQlHnGH5EuExmpasL1fMP3JYpB1YXegqkScntNLiIN2hxNwzKSR5ieThHGscYJItCdoyu6EuBxfOewN4wLY1oRj7-ZRlf2-o33lHsu2ARHzBwPn-DOSKhXOUFUZgPiRFK4FLupDqwNWSyvB1WQq2Qk0vIwMM6l05gjaNcAa4HYsvSS-8bteBD5OQD-HO4gKTNgBdtMp9aEg2aYYT9-h_F_KspjrsTTtaOKPmxcfj0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eTGcSlJ5C2iupRL90_aGqvdqaAj-V_z1mEdgUk-dw0YDSHfJmt50JkIIJpuai-Q4V362h7UL0MlOJPtldbMzio2Vvl7s-JRg4ii8xaBmgbaWFnMDxtHmpvOhVHIqVHd-g4bjakLIm5djLbAPgkIv2EUS5eVIA9EpLY1LoHJdUY2HFHlDFHegdXJKVe1TKtCUhlDMcwLh4jhPFfg05IeRn6SW75dP2TotjDoFJs34zzArMA5Ft_Hv9EM7P0M2sy2WoQshrQKeU5nXRQYaPFM6UUJdFu96c0AouzKNIAsav2I20oyQGgdm2tsgBPLqKp4mbbjVOdKYuDl_Rs7BU7r9AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64796" target="_blank">📅 00:24 · 18 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MffjEEbPwTQlqBHo7Z5fu-f19zibeOX0rWbYJYsY7UCgzcE0sFZT29nk5uGbk_OkcgOeNOmITxcGGenIbkB3SidNy8zkU9M9saTfENh1IiCEHp4jZ6gS0RupHnBlUfkmL1aKsFdjT40dUlxF2ZnfLNGdxDIFrzdiRfCXZ9TVzp8oLi7w66pMEN2jiCKNHNn6vYglaLGB0FUB37Ne4jGaE3uUUYI0q6vHFt3VLajhAqoTwtDfM_kJdXMFdw_3AwcfNyQPiCMEIuGhcev4g8aV7A4w_5Z2BSEC887B-6huW0PHeMgiwNLuJ9AAv63y-V4sBNl72Qut6voXEn7jHRmk8w.jpg" alt="photo" loading="lazy"/></div>
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
