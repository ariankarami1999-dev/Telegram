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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 15:09:06</div>
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
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/afGFBusJx8UNBcKESX3zNFv1lIx5DwHbgGUX-SU0oDLF9sgGtMT_VhpbhjvgeAw9bzCrlnnztS5Q-Hw7WaRX7OLaFBiJkm8dTTvNF4KKCiz0AcPMTbq46ysNYC92zDkk2gRlSn-MZt5YFZPGG1iFujrgDs91yjrFjV-c_U9VGM-lY1Hlw9YN09bdieEd-wydW3VgEdPpLV2fqstiNnaSyVlioeLYWqAjx3FxrBJUPA7LdLT-B_gSNsvmsHagnMV5y1CsPRIz6R1-QAM59CYHkxd5k2JoxGoa7DMPENAkKz7rTaJxdFNaJ-dOuq0m1QDdw0mFDL3Eva-_JdSKlo9r3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AgKw4HvxKuTN1fCQ_gFgii0tX4YTujibBYKq635RGKNTfYDBANynFiLpEx0IwI2TXIbiffZx6f_4v5YCFgId3x-r4yQiZm65ZehlX7ubcI0Py_rXHYSMlpbvJmK90XNlR14CZ2p3vHBLL6lwkPgJLmbdAIUcXDk7VlJLTo9XpQUTyJ7bvppIwL1N_Hu2XCSUCP-OeEYuicGgL_2D6CWM7C4PkhBKVDQK2s1S9FEIbQCuK633eHIus8jUl6vQhq4NEuEM12kyxJEc-VoKS_Bfo2Y5gDaCCFb2sBnhlNywTcrcTeFb_Wtofh1lOU-kcBnoa-jn_HVHFvQXU8HzjAdkvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ikcy5UWeG-HIdYc0o225sepRfC6H8NZnMOvU4aALaPcPPZ7VFe-xB68u-iESP7E77RnmC0Pp7OKnkwAKx16yVMMsd8JYZG85b6eCVtYDHWybEfKTOxQviL_7ERunUcbQ2EfEX8X--WAmHw1QJnhtBHUCq5v7daYpet4hJqKi5HKQdAGk_HeqgP28iCXwy0m4cHQNgaEZy4LwysT74yUOsYWNxRNRmcDWCot5EHu-hOuNDwmnko0De6I7Lrl9R4LKFwehU4xs-ty6AYFILcFGyz4266yUudM6h5Mrs_67uRVUAVf3TjMQOZj3ry93Cz0p6P-ycxETSVTW2DzryAga0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LaO28VKf67RHdnwwPvEoOEeWd1C8Kp7swIDr5EMm7rh0XMYBOvPQhwBc7RQo79KXH18BXuQNhz9k5vdagn9jqXbzXVA1NEwWLAtpik_UzH5PlkTX-knbMhWWbpOXqbr2w-YL430PC0ljZgsbxqQKpqDYhZfC51AS2jCJRWmQyrTiCFU3vaHjox5lXZwBnvk4JtG3g9cposau3KKjqHFJ1ab3OFp62nheyQxd_jWz-aV03doM5sYheF7LZwyhkEp9z-V6spJTG6M6VM1jwumWKmaxebRoS6B572vw0nbym4zvfxLipxz3-mjRjJHykO3y9yD2dzzdk_K7fSJx64TD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2PClXiEqbSsa_uWNN41_BXOSvYVF0ZXVYsG3fmaqUdgaLOwTUIKrbusCjqlHFKOq5DmNd2AOPfcIuNzVlxL-7ovLnn4ConUEfFTPIlVdwkDyPhR2eIxt0GkOW4qUcMuhGpE5TyWqMfP4Nbd9dcgf5sbg7Lo7rc52unwrpBC3m4ybO1n7LdTTT7SGuct-3w95nvAk9odHJEzmTR5pZn49Qf5kW_-PwyXnBKa4iHwByIxGyyxwPtNlgyArhv1ZzuHg7OTijTwEVkMsvCxGedwxcx1btkJa8W_dom8d9yvL9YQuM76O2l5r_LJOAk_j4vC5sEwev3bDsdqUScdz8YAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIPb0qJGxwRNcC7Trz290fARY-JVHJmo0Mb9N6jc2pqI94U6z1AXl7BkPzGV5LwOZnNIfLzCmrnX75aJw2RPMqIuVqYbERhXv-5mU9FAt3sXDYe6cGwqp65qkr0rStgGExx81hbR10e6p0g-L8mva2oaCsoHeeqjw955w-KYZ28MyC_d5zCPKabhyciHsm-Lw9QzHfeaYbfD8UQGf96lsSUafbrlkwbjFG3skOD-pnJpTBkzm6-eeYS4J0Yc8J2nghgMFZrduBfijNmYzLJ-bLmGv2PimvFXAl0xa1bNM9rLIdGTSJC8iQUAScY-9ogSb-JjjTG6H7MOUtlxOUkY7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQysQHinqsomKPqVYfoXclJPvQYYuRTAjiLI8QzM8dW0ejgAvbrgk3A1PTOcc0vn5K6vaD2LsPhg3_y3WkW74JmVXAUmDPMWRvtEMG8m8qNsjw4IOMsCmz3xmtiB1eFXEz-m3zzapXX3AAdxKmF2fHl44u1NJd2cL5rjjaFOYlTT-4jKPOX7HW_yr2V7uuAiChw4p48XMUYTvTj4DAzqpPxLa6VDPSKWCmganQcu5n2rFzj6EQk-fLhHRsZYMgBFRFi_xY9ltEktiFgjatJDzb_hbHZ4kLtrIK-IjnHe_4CnTrEVTQlrxHglFd5PaEjpzihwQj9qI7hWtLhHaNer4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtkRGWsM8dh3EhM79dL8BGgQlYDBrv0HqFao4sjYr3yuQ41T8nNTt1ToluWBmvwihtIV7Dv0Tm2n4qdN8VAM42fxyRd-AwJzpdIwexM8BgB1J0gGMMLqMIeZQj6VXxPjx1lRwoGMQHJcV5BGF5_CFVFEq6fu-lKxGAK7LmQ-7LVHbzFAH2s0dHdqAjJQEbXVE1laAV7YG5xgkIhbNSZhWR-y0ttohVF1u5dUySEdk9CPwYseUBpq6t32Pa765OECYTmjKZUarSdkAPLPlorm4sOskvLEAGaUmElR-KA-p5mCDLiaovzEqdYhNGYcUMa66diOKat_57BXqPveCL7_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieXJWARzSs-0RR53T0UjIZv8PQOe4vIhRQTrw6d1RNyeRHG43vaAPh7Eb75yX4hNdIxyr7A8UJ-ifYwiOoCiwV-9p8HhRbTUhF3949VD_R8ydcrSKfNdhWBxN1uZn9FUiDZB0zZg1vw7tUZJkZZh_FqV8Qe-8OXuWAXd463cZhlfPpvVlJxdC_NQTrrYK84NIVFsCpBFm2mRq_s7nj0eHvtGYh9r1MCmQc1JuWf_MXkA8h18NJ8fxenttysQpO8Dw5Tec40IOqgEUmf9O3khqZIvo-79B5JmhaWI2MamTvX5zIIJNRbxwBnC69KGJ76fWZRL2yYjsUJu0DSUgFBXZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw8UbR3cjNfxekc-j1Q7WM5RpuIEECDQLNIaGRBOODEAiC7Lh4ko_d1Ua1TQ31lN8KOeWoidfDAMhtSGVpSXbX5RfVACV23jeIiyfCoVXlE-IMtvP0OJWceoo5qPoF29w286oE-3zhMkUmOJv-ZIIoglXnOPMjUfO3OR9YK5R9_youvOKskO8e1B3vqN53hCUllZbq5XGLbt7wEj1YZmDkEdBYNUjkrQZaCWgVnQhu3zBJxrl8ujeWtTcdThvM57gA3VujoUmJSFxu4nMEq67KMEBpJ61JZ5gpqSXP9ojac4c2WBiuxqM17ZvIU9-1s0ekoNgSH7atiSpQkiQxoErA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=UDZYeqsTdn2oVMtpRY7J3gY-e-IH6lI-qOkK1GfbmACGVfMta8gyVxYXsju38_NlZWs0P2t-z14brj6QqPau3G2dqxmJ5d0nvR4UOxOLeQi8SS54mNRQzd0KupwKM3qzbB6OVqByveuiF61LUcQ5kGbw7pCcRiCYVdWqJOFhAJjSC6Xs21xRXX_YNc4lPK0gdrpPEePExE0gIOkmxqTcHCpOBO7L0xmcSxdiEEhdpWsgkA-mq1H-AMLz40q2zWYL260DTx4wogzP_dCA7wQpCNYHk7OvGvsdD28tJQMIYFD10D400g-hFhUfLyHoKT88i-sKmEED1RGvyuGzjQgtCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=UDZYeqsTdn2oVMtpRY7J3gY-e-IH6lI-qOkK1GfbmACGVfMta8gyVxYXsju38_NlZWs0P2t-z14brj6QqPau3G2dqxmJ5d0nvR4UOxOLeQi8SS54mNRQzd0KupwKM3qzbB6OVqByveuiF61LUcQ5kGbw7pCcRiCYVdWqJOFhAJjSC6Xs21xRXX_YNc4lPK0gdrpPEePExE0gIOkmxqTcHCpOBO7L0xmcSxdiEEhdpWsgkA-mq1H-AMLz40q2zWYL260DTx4wogzP_dCA7wQpCNYHk7OvGvsdD28tJQMIYFD10D400g-hFhUfLyHoKT88i-sKmEED1RGvyuGzjQgtCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=ePk9eEwRJYoe8O1algMKSAneOKP6-M25lnfz1XEM4cnO-3tjSYnqOMislJDlT_Xh3QU8brvUbpzSltSJIPJi-GB4phIQK18hFChZdPWA1oU4YnxVBpwV-b59G4dzFG6QcYrFYbN5rj-_bOrMmWcETpO4OKDpgEFRKbpgCZT-38yRVnDS2uP0BKIRu0fxm0M9oSCuDdZ8wqjOThEf9jNFR7TI8n8HZ42FjmoFPwefAJgGB6CGwR9RgyrXLvkyJnMr1TLW2Gvv4lHXp2LaTPSB6agrm-heAVxBcsEXQaCDvHThUcU0rlwFQEtxaRjXuC5pOOsTklzzdXs0tS731k_LFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=ePk9eEwRJYoe8O1algMKSAneOKP6-M25lnfz1XEM4cnO-3tjSYnqOMislJDlT_Xh3QU8brvUbpzSltSJIPJi-GB4phIQK18hFChZdPWA1oU4YnxVBpwV-b59G4dzFG6QcYrFYbN5rj-_bOrMmWcETpO4OKDpgEFRKbpgCZT-38yRVnDS2uP0BKIRu0fxm0M9oSCuDdZ8wqjOThEf9jNFR7TI8n8HZ42FjmoFPwefAJgGB6CGwR9RgyrXLvkyJnMr1TLW2Gvv4lHXp2LaTPSB6agrm-heAVxBcsEXQaCDvHThUcU0rlwFQEtxaRjXuC5pOOsTklzzdXs0tS731k_LFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XlpVl6SCrEUgtXsLQJkyn5pNo6DdTw5_KC5lDXXyIssDTpfe-Appv13ixOQFcJfMpgn7MvlmpNa84N53BccxcEkRoYkswvtZ77bDkoXg0HVdQK_txM7_S2UZp0xP_THhXtOi1mjyMvQZqqrlVY06bNCGfUpdrPb1wnwPQFL7rcpornN4Z-GAIDc7kHPKkNA34yrRsqKLMNv73o-UVL9ah9bagVBLlRa8Fm41RKj7ZGMiCB_xR6KBopfs45N3tOc5dY0zFVoRzZlpQwxPYP5GQ41_yglvIWrJQRPCQbKzjjnqh9ynTLzy5X_mLlbxupFOuf5tFpDSmfle7B_Q9Or6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWMrLIz80AgoxSD_r_-vcElkPpIDSb2bRddMYombTDDAqIIvPkaT2KlJELnmNz-pnw5aVr9Xwuz0NsIcWPsNcTC1rOoatzE4NrWKb9STtvc1noKZjbhyDCILg7hr8GRxjAFbsYMW2zfbZV3Ovb1KIWl3agFhRUw0dLtO7Xo2lR66hrD2Pq0yGcOxC6k83ltBcWaC89ojDqzGntcrP-GUOXsMuBschsBOJCpbDTMz5UiHoQudUhu-zDdJ25z2EGoUDcDIaebKKQec4WKG_hYaxVfc-Zhf9pNk6YwHJLIo4clrLKyd0Fcdbn9tJMgBkpTqxx19XGOhbUGi148L6-esEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBu79Zo1A99xIiDbzqVRTlEiBesO34mijn-6SdMuqj4NJsfrLDBHZsxORsWBwOYbSutB7VqQq-8mfKPcFHLUX--MF5S9-4PKRb9d5TYibLdThgyRu7mFbhCsAywKnJ94TRYHWyzq-XhgMx5jiRiBU-qyMPbfZPC3OdUAr_Gj4SeovjPLhf9f9BNA-cP9gYFDXe61mTLTdNUcd7N-HAwC63XVjzo7WCFV0gng9UZpWE4V1Fyq6hP1msOqxoKrk-4b_So5DRTxzppVM7AO22YUAMeGI6EkxqDlJAPx0YyCzV6uPHjN4O0RhZeFutN2TNqI-05qtA1KaS0yOWRKJIUmsg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=FWVyC634XDMRRJuc_iGgXSFo8iBksimettYSuUjcwNcXH7kMd7hPTVQyKQLbzFD_-tKEoR2AUee0mxskRBNDpt7-2tWPnm8BhQC4ciswd-t7N-p6qqQC6KQ-wh1pG2hz_60YxOwBzgDdeeFQ9wTePljryvaZtAKyhzWl8r8TNgffXRPyOAdUIU8lclNyA-KgagxsrbodnXF20XT9glf2pwkmPdaMjH8FGxCAXWbZyT4sxaVMNXNkEqCr8tGZVjd5nxcAi0CCMb_1kIWrkkQU665tEPzOlBj0Ti9HOq6U2TlHOzXs2Ma6ujIMVb8QV5Nao-YrS82MejvolzUiqE3v1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=FWVyC634XDMRRJuc_iGgXSFo8iBksimettYSuUjcwNcXH7kMd7hPTVQyKQLbzFD_-tKEoR2AUee0mxskRBNDpt7-2tWPnm8BhQC4ciswd-t7N-p6qqQC6KQ-wh1pG2hz_60YxOwBzgDdeeFQ9wTePljryvaZtAKyhzWl8r8TNgffXRPyOAdUIU8lclNyA-KgagxsrbodnXF20XT9glf2pwkmPdaMjH8FGxCAXWbZyT4sxaVMNXNkEqCr8tGZVjd5nxcAi0CCMb_1kIWrkkQU665tEPzOlBj0Ti9HOq6U2TlHOzXs2Ma6ujIMVb8QV5Nao-YrS82MejvolzUiqE3v1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tapqf7inMM2JxMfvopD9vHKc8L1F15gzFq6uAr2BwVjj4Aj6fr1PV-diBCOlCg1pV9-VrRrqiT_DY1qy9bflYJckoaodxzUmRZa_6PURs8twBOrB_2oRK8AaZ4qY1wcaMUS3BEOoXHYOsv4QHQ4OKjURsZaWEFJYeWeHoukNMH1bboJOPU8r3mPP4QzyuDPkZrz7nMRQCeEguejLfDopILVphSyUWbwnmdm5mUwQzSmAyuCdSYhno9enClIUGC17T6Nk4OEASCTOsrr6qDOAqqKNEf81BNqSHMNngH6yaMQDCFfE_YCdvjoJBxmmpaEIp6PKxd2lOD0pBPjl1-orEg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=QllNw89weD3GcyBcZiJMndpr4S_IuJrZ7NqGCSYYpSgSPNFKrj1nvfqGh8vGzBuOW-9tQWrn1cIn_zH8WDX4jAVydBEAf9Q8xrDZTPcKeX5hG7GXfGmvUNr5tL5ZUBKt7TYPags7PrcyRfUG_s6Ae4xr-ACle6HEw_Y7YNOhXEuUgydUsoF0VEzHeV05ehsA7VC3gw1AM7MnfqG7z0bdEoBaR0BCjwzQhSbksLxeucGbssjSGDwvrRHX2anbZVYQE8RxGn3ChdMg0990YhawhHujW-_mJndX5zQ0hoh9VJ6zHqvl4Hho5MHW8oH8pfPnDh-7t-tmFKIKGytuoJWcbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=QllNw89weD3GcyBcZiJMndpr4S_IuJrZ7NqGCSYYpSgSPNFKrj1nvfqGh8vGzBuOW-9tQWrn1cIn_zH8WDX4jAVydBEAf9Q8xrDZTPcKeX5hG7GXfGmvUNr5tL5ZUBKt7TYPags7PrcyRfUG_s6Ae4xr-ACle6HEw_Y7YNOhXEuUgydUsoF0VEzHeV05ehsA7VC3gw1AM7MnfqG7z0bdEoBaR0BCjwzQhSbksLxeucGbssjSGDwvrRHX2anbZVYQE8RxGn3ChdMg0990YhawhHujW-_mJndX5zQ0hoh9VJ6zHqvl4Hho5MHW8oH8pfPnDh-7t-tmFKIKGytuoJWcbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=d6nlE46TSAq7bwSnQt3VF-OeAry4ZYz8WiLdzh4i2GM9Arx0l40AZZxgdVy3jn1oXcRKpYmA3Fyvqz0DZiKF-XRc4cyciY4aIRP18HGScBtxKcKcL_4wHZ18Ab02oQvryB0FnlyWcGpQEdtuAIaZo9DyQx6Xb0sellmZia3PNJjj9cAspwGozz_MUy3aWkKR8K95bk3k07-u_Q8HdsH9MoTIFkUGmuD0n6EBKTtAovS1SKsuqn8IiqxWeasKTgVoyIntgStCGTwXqwxy0faCbJcUbhnNJQ91Hu11jR98I6JquSGP4gJqqcu2Upv87nXdP6AxDzXo3yaQ5YMfkv3g7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=d6nlE46TSAq7bwSnQt3VF-OeAry4ZYz8WiLdzh4i2GM9Arx0l40AZZxgdVy3jn1oXcRKpYmA3Fyvqz0DZiKF-XRc4cyciY4aIRP18HGScBtxKcKcL_4wHZ18Ab02oQvryB0FnlyWcGpQEdtuAIaZo9DyQx6Xb0sellmZia3PNJjj9cAspwGozz_MUy3aWkKR8K95bk3k07-u_Q8HdsH9MoTIFkUGmuD0n6EBKTtAovS1SKsuqn8IiqxWeasKTgVoyIntgStCGTwXqwxy0faCbJcUbhnNJQ91Hu11jR98I6JquSGP4gJqqcu2Upv87nXdP6AxDzXo3yaQ5YMfkv3g7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMU8qSaBALzsZRadwsPtBmIpE8e3klP5dP3Avp9sT3bBZgBNsxcfCBiqhb9r66K03U0pkWzFiuwsN5I3HGTu9xMs1jBj09I-ysYilNKD0c8whDXHmocS15Kbo0MjRoAtYWA5YV8gfndWJIqsTdOdv_9qrAX7sBf3Hb6ZFP_eM95BXVTUsN6H8pwFA0HdPxBDadpW5tHi3_5uHqX2IgN5pMyYRQG-XD2A2_yGWMvo0Ovzpm8CmQtNWNQeybetOExlRKRuW40rcrGS3FtnpHyjt9S6kr1YBe__2XeXh3J1VAx0hPozjn1Q1dMfmITXDecUGfu4L96gE8NXQwKbla4l4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-zfvk7vi9kNUBg9UEjWSWw2jk1zjehD8LpvU6ycGdF-_egWRW6hJ9s9lmHiVHFsBKEMlekWBDp-g_A6xubnTBJLsNKGOjBZnxUj3XXwp-vUx9TZhDaAVl37c5QTu4ZCwf780tScQS7sgfYde1HkoYlDxshf_r_hgWNxFDRzYRA0XQwJJkJM8Ap2i3qLC043QwhJdXZA1lo7N4QdeddgoVtCYjce77MPBpUa08nocjlQrlh3pyJqNxlbsw6AwLnIThVHMDcHL9k25qfejl1d_SRbklu3PiMNuJ_DUsUMijui-8qxu_EjQ76nzQKwQ1UiCpDqyo_M_ddpE6E-AdnWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=DStiTYRC_0R-FxqssgmpXSMy8M3B00PANDfjzxbIS6o8KE0Gn6rIJ-r-2cZZM_69VCYtDKVVnK-3Vg89sLMC2VZ5Ocv96oRc4e5WHbC54OeGnTRrV-z8jbwaeHNXWs22UIKQS6inqcxSESlePfeJtuoBhia2LrlVjVziyewEX-5Te9KioNTwpQWe7Z42w_2L57I1S8HEQcSxKd2eiA9x7yh6k5agVxwbRgHMj8NS0hTsDSWSm0fMaoZRbZ-e-txbTH7zx8zAR4dPQ4dBAueBIJ-46KLxYSzLAYIHP_ZAkUYGDs0bIfsTLa8CztaYyuHoCJNknABHaGNcSzVZ7Cvuew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=DStiTYRC_0R-FxqssgmpXSMy8M3B00PANDfjzxbIS6o8KE0Gn6rIJ-r-2cZZM_69VCYtDKVVnK-3Vg89sLMC2VZ5Ocv96oRc4e5WHbC54OeGnTRrV-z8jbwaeHNXWs22UIKQS6inqcxSESlePfeJtuoBhia2LrlVjVziyewEX-5Te9KioNTwpQWe7Z42w_2L57I1S8HEQcSxKd2eiA9x7yh6k5agVxwbRgHMj8NS0hTsDSWSm0fMaoZRbZ-e-txbTH7zx8zAR4dPQ4dBAueBIJ-46KLxYSzLAYIHP_ZAkUYGDs0bIfsTLa8CztaYyuHoCJNknABHaGNcSzVZ7Cvuew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=oYGK82kHHZk373jVberZ0CbCZqPOZ-EAFe7gQTwMeF51FJrDV_uI1eZteUszodH76YL3IH6n9r_UN2HLFWPULVoCciAl92CJ0gMNhJ68Aj_1gZfWGPXCc_vD-4LWxvUwUaBHhNGgSQJ5u10Hu40ImUidc5EDSVca3vcdVZh7M44imLNjdgYuFRwYz5HRTtJ1LlGGZtmz4AxzbhtzsaMHW9WZB6EIq-bhWHYGQD8osWfEHSu2zJcpyxhk1INu0lri5Z3ctan_Abi60u3db2vxa4t47IV7phybCqPV-6UFBFnZ2CVqqTMyMHn_vzLUX2-sED2SMLJN-u5jFc5Diuh8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=oYGK82kHHZk373jVberZ0CbCZqPOZ-EAFe7gQTwMeF51FJrDV_uI1eZteUszodH76YL3IH6n9r_UN2HLFWPULVoCciAl92CJ0gMNhJ68Aj_1gZfWGPXCc_vD-4LWxvUwUaBHhNGgSQJ5u10Hu40ImUidc5EDSVca3vcdVZh7M44imLNjdgYuFRwYz5HRTtJ1LlGGZtmz4AxzbhtzsaMHW9WZB6EIq-bhWHYGQD8osWfEHSu2zJcpyxhk1INu0lri5Z3ctan_Abi60u3db2vxa4t47IV7phybCqPV-6UFBFnZ2CVqqTMyMHn_vzLUX2-sED2SMLJN-u5jFc5Diuh8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXrEqJp06yjxHf-Lep5DNIHtHEsNinbcnwDfpSKzjJGdBZYiAqzi8OCz7ds6Iy_IwTzQe0cEGmcbARQK1bgLoGUz38PWygrGIVH5Zr7RWvfpuWlqnDBg5aIlxwluTcanM7jlwthk2suLHBdBfeT2Ek-MpPnyE-8aWSiBy8P808a7yBlnRCmdya5ONEftvMQWE0-6um5UxqhSMNMEiGPnkTcV8-63_8ZZLRoZNqem2tRXRQciCcjfBgT6WhZhcuO5oUxOpqG7Plf0UJIl1hXiVgf2ZKXxAGFUzyKxAqPg34MZXi5AEB8kSZhdBooj66-84rf6QMBxiMgPtSOQDYNl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ul-JiFcu8quUFacsZ18VAdenER7zjaR0iOAHXIxjCpZ08MxtKpV2Ef4zAveQwMQ0jhZRrH504ijUC4p_sq2u6BXOzgQ_yM4w9OovbKjEhxKKJVjqcNX2IC2d4E3eg3sE6nyEZC25ef4SVdzdvsMABRB7HM-zQzzaU3jZVLhjIpxGzvNzrxUvQlxtCKJHbug35ZwKiff2QhkZJ1oMA4m9WVlIAsNj3UJWxbhOKUU1iASVWFddZTqsCtqpccEIpFY344ilvFp6E-bNklIBfyQAVOsxDQtGO9JSajjtzRwh6d99q-wxCHwFKnyvrcMxz_Ody3-ZhqexLH_0BozWxyMjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpbwjB8KmGPQpfuAFiP3NeA7Kzvi_Le3hUr0IzFuDA5E9-INS4kYcAX5l6nnup6BIQLAp1zNHOfWbEWddYygfeaxYoS__TeXvwUh7f4ZbTOw8yv2ViVbRQagOECksPLL0KJ3MgPDk0RyeieCDUuZeETiVcz3_JI2SafMklVjQHX-s73ONH_Bf6_lSirb3Bt5bHFBQ_BY4VdYjWAkbAp_PpXQzc7WxeBG0z6w08-lgLsCx0Uec8v2qrGSfirrnRZSh7Lox8tKxoaBVgUzJmLyUP8dH6oIy-FN1UcIqWnBFd19hi-J1GynaLonpU3ROohDaQDB0r0zEVIRcwuwfAYFpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RikMCyMpXCXW0JgKVHk7Hyx1J_o5bwJVklzd9CQnQt2lRr-nyYBjMWN8Uyt6wCUcUbnnxSMtr1lXRElCI37MF27PwFQhzACFtdzjkZOomu3RydJ4qKqhHQB6Z-liKYVattMHfDpZDx7HK6xItz-M4lNVoHDa60aT9VaKEsh2uk6xBpOpABqw0runQgcZAmzZ8gWTS5qE03_SDyc2N4U9RE39WYyLT5HQOAMLDALFSUV1wTIsi04cIrkS1UgYpdwpjstYP7yusC4IxGxyLQvupEc8vMKsR892brNT0nLoPKKRr3CMsUstKuOgTZv5iiC5-1llfj-GXR9DAG0lP2WaZA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=cVIS0PbS75lrjCS7xCUv5heRy8MsPEK4TG96ysqvglZ6PJC3riDhLad9-kiNTtoXzrRVtrII2D96tbzS2Nv6ZZaeag8BTB1CeOVwIZe_OThBCZce1mJHGwFuhVP8UMVkQOi0nxZIxF4I8G0uJQbj6Uc_1ICa91Fvb21HVKZywIPpFcr6OJZC9BXoZa9SHeGclSKYNTPLvKNVS-DlHFF0EOIMU_FHW2JPYWBJNQakjMczHxtDhREKeZIGkSi7Sbl1obttYeGIj0ZXMufh6FjIELCQHh1kL8T6777Jc48kOBzIGpYWUSQ6PEeSNtXUn211PUlpsUgWCNwjJyZH_-rapA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=cVIS0PbS75lrjCS7xCUv5heRy8MsPEK4TG96ysqvglZ6PJC3riDhLad9-kiNTtoXzrRVtrII2D96tbzS2Nv6ZZaeag8BTB1CeOVwIZe_OThBCZce1mJHGwFuhVP8UMVkQOi0nxZIxF4I8G0uJQbj6Uc_1ICa91Fvb21HVKZywIPpFcr6OJZC9BXoZa9SHeGclSKYNTPLvKNVS-DlHFF0EOIMU_FHW2JPYWBJNQakjMczHxtDhREKeZIGkSi7Sbl1obttYeGIj0ZXMufh6FjIELCQHh1kL8T6777Jc48kOBzIGpYWUSQ6PEeSNtXUn211PUlpsUgWCNwjJyZH_-rapA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64840" target="_blank">📅 00:30 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgLSpwwaSIZUVNKRT-yBub-FkjkJqZ9RDx7G3qXKSrBYaHnDgLFu53vZ4uOXoy61WbSDO1P4gqzM3htGgLfJDUrHfajCmJQOCiccRwb9hY0hQhU5FbaO_MT7HlfWqCfG6yiraFmerEOfCo0fwQo4KosSGwfph9K9mO_umXOqg3faNOHZcEQl45IQD8jut6dTMZXux13tzA_-8tEkCAz3AaQab2_8Qh7pm9AABJreueQitgDHx0gdKcuvXLixD_lg-Lu5VMrLV_T6djcKIVz6jxTgXYrq7L_YRKObnMqvnAIwgvZaZAZiB9L6tTer2vPyKwhzLWHoY4kZ78Ky3fvHoQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=p12Ay4MwNzwYOtrx9RNvStAvedwDPYEHG1UCobPMc42cn8EvSKflYzxYaqBecT3kCrA6wW1R9IEti9l5IJf4rPvT_Lpq0fgYpnBFRF0pZVvbVhtzrdgsyGQKVEc-0GmdfTGYNKRuP3LZJMBn55K71DEt1-hmzYIevyOKYaawYQ6AmgynXGGe-asEHQKCdR2l4xzX0Lz2Ys_0IQnWL7pds2RV5uHPpJCSL1m_7Lg0HBtsWc-4h42pBEQ82_s5FOkdk9z3eJQXnvW6aV0JaijG-Mu52pzwyWiMz7j9bqRjJVmueb-6LPYbWBYaGDx6f3QtQw3rZNTfOL_p_bm2izY6fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=p12Ay4MwNzwYOtrx9RNvStAvedwDPYEHG1UCobPMc42cn8EvSKflYzxYaqBecT3kCrA6wW1R9IEti9l5IJf4rPvT_Lpq0fgYpnBFRF0pZVvbVhtzrdgsyGQKVEc-0GmdfTGYNKRuP3LZJMBn55K71DEt1-hmzYIevyOKYaawYQ6AmgynXGGe-asEHQKCdR2l4xzX0Lz2Ys_0IQnWL7pds2RV5uHPpJCSL1m_7Lg0HBtsWc-4h42pBEQ82_s5FOkdk9z3eJQXnvW6aV0JaijG-Mu52pzwyWiMz7j9bqRjJVmueb-6LPYbWBYaGDx6f3QtQw3rZNTfOL_p_bm2izY6fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64835" target="_blank">📅 03:09 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvgOTucJKerFKxdcO5qXRMEip-D5mvpi_jQ27UF_P_-xYEScik91X8UrbB-T7HxeGq3zr8PM4W_JsfjXl4q4DwRBJq_6u5Uek8XgKHWvNBlrFdi_aX4rOi-9pNgZLd4zF-ONAYqKz-xPNQo7wo1-eeRYGOGSsODowEuWWlcSJ7BbJw3tlxzrWbsgrUIG7TiWUYbHF5JG5mDfD2USyQzwlThVSIsg8dtbKnrPWNgarkXO2jP2nqoBRMvWbz8E_LGg7WKqan-RS8X6QHrci71_AnWbt_ct_iLfeOBkd8PxJ5V1rX030ZyiZIYmEIyv8wf6SodKoe9YcYVUs0q5htoCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhmZSc_AAfIffJrLkoTBGrrSfqX_QmIm0MUDzCbT3Rn8tzWs3uXRupwjd__iJIOAg38x-f-wGAJFqD17MjdN5WEZKT-tsQ7_Ran7hRU4vU9rXtDEXoTepm-g7x5vWWNp0Vk-Nzhy1VxGYZoITcl0Oo5IjgPkc0VeKcoJLcct1CQHyaGAUJGJh6eQWCPKAfh8WVsbnFtW6HrrLqEFjfyJYABih6575FchKSxKpYKrv0CsEDuv3QxWhod6O-lsy8KQAxUCEgo257YH3mLrO2Wjn0i_N-CpBe1d2y-rU3pwoIz6Eqjj5kyGOSXtf6Gzx_ZPhFcFZ5AEYijcgm11LDaM4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBEMD28y3_kGFVvZf63fNH2ZH5jihb57uHOzqFMHugijkqOEkz3Xh3qeQNIEdJJFhoJSQS0O5PepSq4R8mNozG0C2jiCn8BwkkwQ-3gPcWODD2dmkVNrJ9tC3pgJoiPdWC_KxUinKCAEFSmmKd2T0fM3CHp2pjDqGXciAGyIiff8LrlB4sZqkwDcfMt5zA6xl0bFucKRkbN_VdGjvqkH-2V19psf4SKDcHUWGq6GThuwvUr2_9P4sLtkBrMJamlQlH53NHZGM4xb7WcckAzNRygbgcniLaTmYDBwwDk9yQrrWXOa__wnoBUmY3Kw7tC2juULrBXV_3dmQapn9gmp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/naaMbAz27VP6Jav2Ppp7pritQVI0tkbs2yqTkdckWXyus5JcN6A9bPT0y-HzLksf00JG6cKaYxQ31ZiRsPtKdEQeLwb7m3U365V2TGsMqI2xoLSSYhP7K9J0js37CDgnm5C2v0JyfOPZHRSqtRs1YnrIajtX_1KmysuGXjrr-6jEk-yLFO4hwS_MFPE_d43wa7pr5jm2FdQEVEYA6O8mvmnfKoOEyP7PNqDwjFQiXDBZaaH2PuuIIMNimNJADz8XONAUbLAo964r1o3PM0fZOuO4gNFa0foYmYR-u2I5Y2RvO38nuclPGoPqrKLxQBPpWS4tRgpaF_eECduRf64GEg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=l6x4rJEFKKMNPlP99yjdXWE9hqeAMe8kyX5cLYP3GoOVbK0Zyuz87LbZvKXA6WVG7uvWevKHsp4CCQQfJC0vxoNvuaTRWO0yS8SkQP45IJA0J_4AVj2k8E7w1gm9q_XEpbA1tkZvhyqdE2hfP240l6YupVgko6e1PFTMndjxhvTgEJFFigInYInROUJwoxm23z9VgbnsiEXGr1qPnBhNxNRu04hwKyByL_RLyOWb1Mf5lumtE39AeVK1xS9FggX-85Q264ZV77pNqEY7g7Xoe00QKJ4AdYSh4F3IyipBryqvrkmmS31zqRWxXQ8wX-9o0ljII2tADKpfgA4vlZg2Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=l6x4rJEFKKMNPlP99yjdXWE9hqeAMe8kyX5cLYP3GoOVbK0Zyuz87LbZvKXA6WVG7uvWevKHsp4CCQQfJC0vxoNvuaTRWO0yS8SkQP45IJA0J_4AVj2k8E7w1gm9q_XEpbA1tkZvhyqdE2hfP240l6YupVgko6e1PFTMndjxhvTgEJFFigInYInROUJwoxm23z9VgbnsiEXGr1qPnBhNxNRu04hwKyByL_RLyOWb1Mf5lumtE39AeVK1xS9FggX-85Q264ZV77pNqEY7g7Xoe00QKJ4AdYSh4F3IyipBryqvrkmmS31zqRWxXQ8wX-9o0ljII2tADKpfgA4vlZg2Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh05Tt6oUWHfML-wVJTgZoB6xJfjzwjLrINx7DQmyWBG_TERPK7snUswSiFh-4J7cnDe9OObfx5Bg_ikQISMRUq8YP8JgwL-iO3yDo1p6iZEMreMB2cXeD3zLKwtBDgF0hIkesFdnHIzf8l8qdV1sou_KaYqb9Y0-jrEPef-oAHiE-v5v1zrzwhr7nmJsw1w8xoYYNAd8X61J7360Y6ixr0MCEN_6uJWfZ46qzdKFnB95ufRsi4cSMFa_zSnHwXja4S2fcTkV79GtK8I0j_-J5Ii8Wm1uLAx2FAD1X_rQ5UECCFqhPTYY7ckNmW63ZxVkr7FsMitAp05-IQCX9O1cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akUMr7vn0LVB8cLCcVHbEQXruQPD8zMoLzGlmtzXuoOHKgS1-0fSzhXVLbf8wbrocaviipvPTc76YIG0aqBPRiMBBP0rwd3YVrW6-ZGvO1c2dZup2T729V1F945wzCGlgIle4tGSsanoluwOoP5q_AUrVa25Dva4zLF2Ab6VFBu-FIaIpUcECd5FHJ-2eKMMlQlWczc01bsccCX_ylwDNYiGD-ZH1CEuvJNGYBQE9jKOFMTnFBwQ71sKrRJ0Xd4YHc9yjQHtcg7D7mH4E5uvwFRUKwWeGXUNukgzAyr03bVczaKn7q1G3xpTGpDJph8Qfwrl3Il4qOQrHiy1HlCuvQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=L0MBByV8tP38eAE5VYnEsMoF6XkttDCN2Nm7WZj9ewgCsbgmUdzbcN41JZ53raoqQlCcvpQUiZRP0jh4YSPzFYi1MaTJusJW5ofpgVkOWOZyDfYZcSDy8EoKkj_soCxQBXOqyNoEXnk-bK_2ZcvEhrT9zGjuNG_GU69-UDsstvSOgDU9jYqEN_qXP-u41owXeqP1Xv7JUbmjy8DJPrjrQsRP_3yPtSTH9NFzSqT0eRuFNoqcT5g94RoTrPmZfdAc-NemZqr7lYIKdbLw3SU2Q63PdIG1fVZe6um2mlBeedN86sVFIKTZOzXo20tQSiMLY_uM_AGzWjqPTbERFUt-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=L0MBByV8tP38eAE5VYnEsMoF6XkttDCN2Nm7WZj9ewgCsbgmUdzbcN41JZ53raoqQlCcvpQUiZRP0jh4YSPzFYi1MaTJusJW5ofpgVkOWOZyDfYZcSDy8EoKkj_soCxQBXOqyNoEXnk-bK_2ZcvEhrT9zGjuNG_GU69-UDsstvSOgDU9jYqEN_qXP-u41owXeqP1Xv7JUbmjy8DJPrjrQsRP_3yPtSTH9NFzSqT0eRuFNoqcT5g94RoTrPmZfdAc-NemZqr7lYIKdbLw3SU2Q63PdIG1fVZe6um2mlBeedN86sVFIKTZOzXo20tQSiMLY_uM_AGzWjqPTbERFUt-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZU40Rvd0XL9pQF69V0owXL4RuMnGSl70RXQJ0dXXCjWt4j10Ob5R2214ZkPSye-nE6oi1fb3VB5ZOUPTEWNC40CuOnWKBkjW1JN3De7cE71jCUGD_r7lCyfR6mrMFT35zWeKegSnot-I4WIwG6jzTZzTWDX8QpnEfAeWvb0E9ABEIpcHgafB38NfitLF0DUbE7-AZICmOveaXoPKc_rNjfCtiyaWnMF5c4IHWbZQpTP4_2MrA4o-r1PfWpZG0pCp3lvur2a4RCmhnDj8-l7elxEVA9y-ETPjoVq70vZU21D6lGSkOpfKuHqoz5XGDKdUQBFgbTHIh86sZUT-fBaRA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=cJdTczh1ARniV2S5ekaMv3XeK4UJTXD6KC3167jxrSa6rnBba7xImNQ4phAgCNkhbouynBSfdnLpxtqtDIfXxsEfRWCalqKUmnlEdyX8PoJVwEaDbgMY2mK5f0pZYU7aCChuzUokB2GVAysOdJdufD9LVX9OJnDpkcHpNvJe4yBe_G1pz0H3lEEL-tP3AUcJHFfJN9JH0VhSW9dZtriUZSqbKxJl-xo4V-ZTlkeHJg_sWBj82u3IMqUG3zcTfRKbU6tdT-oa-w8yAcfj5UdzXvSR0LmhnuG1dVHFLe1IdgdRs8vI9093x5Mai3K80OBkaSPwh5vC9ndXFBduoNYqIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=cJdTczh1ARniV2S5ekaMv3XeK4UJTXD6KC3167jxrSa6rnBba7xImNQ4phAgCNkhbouynBSfdnLpxtqtDIfXxsEfRWCalqKUmnlEdyX8PoJVwEaDbgMY2mK5f0pZYU7aCChuzUokB2GVAysOdJdufD9LVX9OJnDpkcHpNvJe4yBe_G1pz0H3lEEL-tP3AUcJHFfJN9JH0VhSW9dZtriUZSqbKxJl-xo4V-ZTlkeHJg_sWBj82u3IMqUG3zcTfRKbU6tdT-oa-w8yAcfj5UdzXvSR0LmhnuG1dVHFLe1IdgdRs8vI9093x5Mai3K80OBkaSPwh5vC9ndXFBduoNYqIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fawedu7xNcoxwD_MUUY1L33vErnoEYRSWdw0-xRp47glx_gR0AvAWOYrCKisk32RB4ADqV2G3leC2zvLkxVKmpmfBiRXvpL-DaH-39bCK4np3ozl4D6GmUI-TZdEquX3qhV-S31tA88J2v7mDZKKOZqk0ZzNl7NGQZ01iEttioSzLCopfeN44__oiHK53H1Vpjj4NgMX6Vm-MxJY5OBkaI_nrX97ZyKf59OUO96NkpMUDM3FAuGrqkkVWC1fg_qqxl-FHRXSqSHPWakJipvGsch8d3Z3itxw8dPxtmdf7tn6i9Q74Nm_GlpymnV8LZHhxA6if_R9SXLJYwxCjhzG6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/huk6s5CewW8PJzrIeSjMcv3ox1cPa8z3rJevJyPWI-UcndZIdr_s6qWc6OVJ-dRfM1IJoR8cBdIVpALqeNKL6fVUmNGZ_P1-O5EvHa1_YReRuI9gjhx0-HEF3z6ZRAa8BHAgf9C-i1aXZex5IQFysLpugFUOZrOB1MhC0QwDahuoiDvN5ooaaNN2cj6AfqKo2rdtaMRRf6eGO4j-L8_nUnWYCYDEz8O8-xk-AQlBCd--0OeHIMNrifqWjjuz9odykSt_GG7Ar3dahFGYUW8iMS6iJT21pqI8Vf7WD0eTX4SBs7NF_hzGt4pSC8ENSsx-PKpykW4bPGB14AMoxOC4qQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V165rSU4c7Qi4FpWFYL1EY4d3KxK8RqhVAvxBerIicpJeTMwB1UrnGMcQfGwAOdHBEi7ZtHu4AuMoA95EYWMybJUVkBC3OhCRMya6RAu1TDbGtD-pz7JZXDaUe2E7xl_wf3GAN3uvjl2NpIw-b8PgYrWdMcaASmZjHK2t5SNY_oFWASt-0uYHfzB7utTWqdwTrYCaqVoiycr-8JNjkhDAc--DF1xqF0TZ3o7fmes4xPkfG4S2MJ0u-MvHZH-rNL7_pZMiEERlSWFTDLPEYk7NfK-lzoahxYqqufPXwTY42YsR_pggOF0s3bOqcrfJn-AflMIf5Z69CgPzm-k2hC2Lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TFD56ipkYyLonqvre8v2lt_G-78SoUJ7ZKrBqhEarPJXqznQbf4DQJCYNl2kDWs9JIUX8BzzBpXj9V2akuyggoLLouU6I5Or_cysqLgvAkIjGZFxcD1O8G_MD3HpKcCGEx5GbWGIyFiAxTPWNQlwvTUbDIltW1oPAGBcDOix8x7SdpZJO3SFdrLXnDSNYPWG5dXTwdOghFLhk102rHF-fVspFKjeLhEtuLP9H2AHJdd1rLuvrfdHqDu0elr4VijNud4IqktjhLuy3h8AW4cM8OB5MSTdAuS3C0ekOrdpUNcmK9j3cYIeZfBnNP85N_HDFLw_C-G74B-b_HOJnNmwXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVMC4DLFULlr3jandk8CAZjtWyBqDAV5FlHz1ADYWLRnjIzGrQ8NdSPUWfJNl-k3R4eRK1QmuCoAIdh9pCkguhkcdMA3oe1ePhJcbAJmkgpXBnfBhchyHNrqyPi2Z014_1sPgY3M5MaLqqSwy67IUZHUaDOLHu_w9CHvUBLsTkDceuDavm-Xa-hlkS6rUjOODa-EwbyuZVpeyk0KOjqVHmpkZ41zymWZdGvBWzllHn2V60aZOsJUkr-8sqXKROBwM6pgSLXQ8ogFDCvlHj9JgCYmd203-5bbXqQrxiuaK4NpzqnaziobJwQ2cjlF_f7zyL6fJDq_fAJep3fbzdD8pQ.jpg" alt="photo" loading="lazy"/></div>
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
