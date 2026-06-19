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
<img src="https://cdn4.telesco.pe/file/h8btISsDn1lLBnJInvFEzvG-MizRLxLn-DJYNzR6lCIq1SJ_Gogt9hoksvToT_jpF10XBgH6ZcekQph0q0T6hq5bHDDC_PupLi2N8DlxkBd5gIkBdPgARpBejZJVTFlSgUcib0MEnvPfCNfs1H_qOgKtoxcIckseYIJ6n_H6X8bMLBe-WWeVmbFH9v-8qqmxnOAphMKBMUKvO10JA8x2k9GwJ4u5TYQV8NEe-QiWKY8tK77yusrURvSeh7e-ASoCaIENI4CcP01f9s5NB_A3MpyBwsfyfRcMh3WvuWaCUyb_hxSmpWomh6JqEmlHTVAmTtpLAXvK8GqNPLTRDBvmgw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 310K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 17:23:16</div>
<hr>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF_d9S_bp0M8q5le6Hj9saXiEz3x9g5LwTWasd60ie_ZC4JcvPtGqK-8K__jMcPYGywos_KubooFvj5iRnIZAS2ynpHzAhJW052a9FBfzUoXtwDygOming0GwYoJe-PrZ4UiOR_9QP040PJzJX1VJa6IjoUSGccoJw1va4I2XlV6EtTJEdX5AIl2_1LThTYfnwXDK2QWG2KDCrduhouwlSYRaFdC8dTMqc38mW17_chISth1X9hJavJ1je2Sjw_WhDelnEBZdLnhCJmw43Tg7_gD-aAjwh7bJykp89DWSLhtzwv0uc34yss3nW7RnrD6PDHHMGcJH7xHQU6WcB68kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmakQ0Ue3LIAgHGstBbK5cQcuC4QkTjVXC3GRtoWTa72sog_3Ypoa3y4BCliY4-ep574qNh8vNSFbp8Rt7scWsBC4eE8AkU7YrWQkrS-NBTYOZ1XuY6rQDa82NtL3xs76THR_KRptp0bRso6xGqJHIRVt9qc6Ne_qN4ey-oAwxOpxN7ugWf2x80ijwDfvjhx_jR2Hc_wUk1xzYBzHKz9tPHSQBm6ZUOz-eJERTZ67NJm28SiOYzeZQ8CDimqoG770AlnuQ8C7WugIuUnTieIrllwXczWo_bH3f6RGSWkSk5lBmROnUdm7g0K5twYj5h7orGF8i7b4B2NcO1ZO-Gbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=uXa_0oZ4z2kmWUUc6T19f3d9hZiPHAp5zcorclj9dvIAt1j2Wwy9k-Hzi5o_soHQ8Ezg-C0v0IUNlpX8Q9zggtXRZw7msMZzfTUugXg9fwM2m9pNYQVXVpjAYujdf-9u2PGsYzZXNnvc2K_iqwlfmdrIUJ2MUsRPX9jp8S8RVJ_6BbeupH_8XOw9KVpkrVAO-YObI_r7QDIyK3FqFIaHq89WfS1Vp6n9CrlRvbBzqNLkiSL1tTfC0j6Cm5NkdJeGVFbRF7hzT3VGr_wABoDa728K_wLkLoCQ-4JPQVJlvuTeMFToqyvnOPM0_7L7BwBj5VSQFrKa0N0dzbL0uhhKyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=uXa_0oZ4z2kmWUUc6T19f3d9hZiPHAp5zcorclj9dvIAt1j2Wwy9k-Hzi5o_soHQ8Ezg-C0v0IUNlpX8Q9zggtXRZw7msMZzfTUugXg9fwM2m9pNYQVXVpjAYujdf-9u2PGsYzZXNnvc2K_iqwlfmdrIUJ2MUsRPX9jp8S8RVJ_6BbeupH_8XOw9KVpkrVAO-YObI_r7QDIyK3FqFIaHq89WfS1Vp6n9CrlRvbBzqNLkiSL1tTfC0j6Cm5NkdJeGVFbRF7hzT3VGr_wABoDa728K_wLkLoCQ-4JPQVJlvuTeMFToqyvnOPM0_7L7BwBj5VSQFrKa0N0dzbL0uhhKyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLCncAwV4BzYk3P3-lQhQ-dnRhA6QAZuERUBBMsDDkT-i1spW-EX1ekzDy0iwVw9hzro4CUeLRpRN0N54Y8V9gE0XsrNQb8sk7GWVX17ZPwRsWe0LPCuhwwJkEvlSKEnu2jJZxNZ0M-f5xuZd8acNvSeVaDZ9CdedoTK54h13iy06HFp1CRJtJ9UfPOgwYhBBlHkzSpkO9vcdFgeEGQr0Y8uxwsNFEg1y9x85wD7ufw1zObnjlyBNFqX9XKzplO3onwvB175VvDK4d201lw4oQql_gORlsS3OL8MEhnU0xEQHxBjHQMFQZHt7tLMRtbj1QgF3mxSaUAdE5M6OXZHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zr-z1fdE6MUOoRzBBOZR9yl5tBlqkyZfH-4BqLec-6FmJLGpOJoA2ftAq7zsipKucbRTGWobkv9MKPGLG3GZzM3dTgim4PtJIIqYIdFLxYTsI0msLknV4WoNjJm31AHR0NuQ0pso4L1IgPemGR8ftmO7dW5PUTik6t0rdhHpmeteGnAOHN1nMz-vcHDFK8zBhz4ICwBTqZQY9DlzoqCMjTJb7TlAs585rg0JHwYwly6V38OZRTk--fx0vXTUfkoJ8wKrY0OJKp4W32VAHBwLIr02kMW5HUYC1IgVv632CFyvwzQCOpj24XERpP-aI1baFrf727qy558f81mFoyKVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=mYTkh-Q4XWzX62KnsGMdvSfZihwvUB0RXaFnBFg6XlIo3wb71KAHIN0nA0cNsjYf4frMjLD4j0zlhvqXTFOzCDuFXwHhQmfgLDWWOt6DpuLsAbmq8NOTXTHZXA8uPfnmbsu5YPvLZQ7ijCT4_919rsC-2XtebWCSaaYyDP5RAYt16utvbk8Huk-0jA9TzxsRWwLcIlmc22rcWYpWnUpns1XRBKo8EretC3L8JzBzy8wW6MpvoMKmUil01A5oNyGx2XV3FJVJoPRXm9Q4ociIC0NRQ1yWaSDWuXWay_zE_stsRqHR1IxZWONyPusyiMwPzGqG2dNb8Yo0e7JAEp3w8UBEOp4H5f8PlFfXQlQYSXfBg91E3jQqiVnPzjHLlgEDjlVCla39MFoHWbzQKx5SYlFqhVPDTBpveKUYutWFTBxNSdWmri27KY1gX3qb6VMws8E5uWFzODSTM1iK2iyKC-Zw7pvYFT8WBGZmIuFK5PDPXjrj2QBb5UVUZeoR0hEFWL0Mnw_CI6ia-beDKjm53UA1fBA8lDvTl-Vp4J1TaPFb3gLINEO4MeJUW1oS9n433z6o-wLem2g4UdCFdFshSmi8H3WWPIGtU1fESZrslIkIIoV5fR-SNRiAlhH1AZZLlJI0xCe033XIFTLSykRPdWZPRPqA00ofpB9NX_XnP0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=mYTkh-Q4XWzX62KnsGMdvSfZihwvUB0RXaFnBFg6XlIo3wb71KAHIN0nA0cNsjYf4frMjLD4j0zlhvqXTFOzCDuFXwHhQmfgLDWWOt6DpuLsAbmq8NOTXTHZXA8uPfnmbsu5YPvLZQ7ijCT4_919rsC-2XtebWCSaaYyDP5RAYt16utvbk8Huk-0jA9TzxsRWwLcIlmc22rcWYpWnUpns1XRBKo8EretC3L8JzBzy8wW6MpvoMKmUil01A5oNyGx2XV3FJVJoPRXm9Q4ociIC0NRQ1yWaSDWuXWay_zE_stsRqHR1IxZWONyPusyiMwPzGqG2dNb8Yo0e7JAEp3w8UBEOp4H5f8PlFfXQlQYSXfBg91E3jQqiVnPzjHLlgEDjlVCla39MFoHWbzQKx5SYlFqhVPDTBpveKUYutWFTBxNSdWmri27KY1gX3qb6VMws8E5uWFzODSTM1iK2iyKC-Zw7pvYFT8WBGZmIuFK5PDPXjrj2QBb5UVUZeoR0hEFWL0Mnw_CI6ia-beDKjm53UA1fBA8lDvTl-Vp4J1TaPFb3gLINEO4MeJUW1oS9n433z6o-wLem2g4UdCFdFshSmi8H3WWPIGtU1fESZrslIkIIoV5fR-SNRiAlhH1AZZLlJI0xCe033XIFTLSykRPdWZPRPqA00ofpB9NX_XnP0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا در رختکن این تیم بعدِ پیروزی قاطع ۶ بر ۰ در برابر قطر و سایه مصدومیت شدید اسماعیل کونه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23830" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgIb9tHTz3QXkvt9au0PAx2xWOA_aljJcJi5c5JSbPIpBVyXvH1JOlalrIzoqeEH-Le3r-dk1jRlVRvRC6j6akCgb2wKEwlKC1fDTEQQQfYcNXoVngqM9lvr35gewWnmf70w1uI0KBYE_Jklo5seN-3RWoiPwhm0p17bXRkGSkaFXSXR40oRPBVXVIm9mKpgrz1yf3RX8kao3xPeXEsY2vKoBQ_9N0M8sVNOyCU5bVNMOXzxZHEgRnd94JFhwxguhZ4jTbzed3RhEQtOWf5IT27KzLipJO2VMM6sC8BDnroLRTkZgmPUlCXLFnk1vvXK-AeHikI6APuLkdTsi_5fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
این ویویو مربوط به سال 1401 عه که محمد محبی به احترام‌مهساامینی‌مچ‌بند مشکی به دستش بسته بود و بعداز گلزنی‌اون رو بوسید و حتی به هم تیمی‌هاش‌گفت‌خوشحالی نکنید. به حواشی چرت و پرت و فتوشاپ‌های یه عده مغز مریض توجه نکنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23829" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1UBilSSEuLydW1x6Rck-aTmX_tdoPuc9XRGkhrA6LS3sJWxKMTEDg46sQ1Rm23h3LCfmpE-H1rSpQ7L23hblsZxl8XVANWaOCfgLw5KZscFNh6ehJNmxEoOaz7Ohm7b2Vmb4S0GmTnf7WQoc94vnAXHUGVfR9RnD6l7i7GVa9WQM9ILQtgPBLG6nr21T9hSTBTHbCKo7hQZ6A9cigoY715T2myq-GG7K_eWLcs4_dmNZ8ITDPwrt9fEN727IbdZ7YuLPBjejp3rBKQoJ1mvde5OJzUiWvxp8snGyNhe8PyEDJS4Agvgn6UsxOcjBBaqMFZc_edaWMVl4_AvePf_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWTMRwapRdWCPsKK_H4R5S0KNooaTe-u-TQbStoclmPSp0wh4bS4kJUR7wY_kUp2tomIn0GQnW57WSWgalD4SIDdokQDS0HYQACeNUDg2BFD3pRDgmKvjf5Ce8Y6zY8nZ9lHIvRnLQ0tHXLGzb3Zv1QL31pHmwsJhYW19o-sdUGwic9gt4g21NX9cKky9P1C6Q-ABZae7qR_4KBWQbwDAEd-yDzzomw59ic0LjSrwCLszehH1NR632C3bka89SlV_u8YNRKJauHdyjHmWJnVIRAo2OGvn6Pitb5kXDBSkz1Jv5gDaDkptatA3eVLCE75_fxJvJpDBJVrWjRm_mHFgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه هفته اول لیگ جزیره در فصل جدید اعلام شد + برنامه‌کامل‌ پنج بازی ابتدایی شش باشگاه بزرگ انگلیس در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23827" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np6-1YqDXw4wh1e8YpMj0KAdTPCsX4PHoRvGMyK8DH9E3mgnES2HIXRs_YCGsfz_SzbblnpVqVS8SjJuG46Bxqyrw9ziNauEbLow0Yh92Ou_jfMIDxcl5_lVcUxvQHKPa7YvYU3fDQD7uSnVrjWoovzKoeuwMBxAwXucuUT-i4nTidZ9ny85goT3OynW1YuVIhpp-H2Z0rmP-3xp8Z2Pd9VOIVOl9yTv5uDm2p_oE9WEZnAbvthZpA5klOG0UYPWGrX6LTXAV3JD_T8H2tqyxPWjiw2_TztbJsRsuFZgNvE9pOozeIFxnhrs5YZiKftNmdgK7_fZBJauJLcbszFIPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23826" target="_blank">📅 13:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=EK62__OlJVmwmKBSSHAqYIObv84gBI5crrsShyaW69nNU0Iu5FFtiwrecIJzz4CMJOTMHRCAKCihl4F07Qxanz8hV3NbRNJYYlZsmUKq4j2ioPXA90S0kSxEMVSvZqk0sZyzOXspm9dNMKsYPt-OGnkqUYPYoeOQmgwOqtau3JloT7QA5_7hsIvv1ctaZD9FL5pM3l6dOJiIrLInvKvLR3o3xl-9OpZjO4jN9R614KUhDEcGk4PJ9uxVrS8yCTCGFBhpxxPhmX-s_Ob6dPJu8IJrmyFyN8fkwdoE3g0zT_t5kaLJr17Upz0yDoj6XC2OlqrI4SoWCkJPkjuxWdtwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=EK62__OlJVmwmKBSSHAqYIObv84gBI5crrsShyaW69nNU0Iu5FFtiwrecIJzz4CMJOTMHRCAKCihl4F07Qxanz8hV3NbRNJYYlZsmUKq4j2ioPXA90S0kSxEMVSvZqk0sZyzOXspm9dNMKsYPt-OGnkqUYPYoeOQmgwOqtau3JloT7QA5_7hsIvv1ctaZD9FL5pM3l6dOJiIrLInvKvLR3o3xl-9OpZjO4jN9R614KUhDEcGk4PJ9uxVrS8yCTCGFBhpxxPhmX-s_Ob6dPJu8IJrmyFyN8fkwdoE3g0zT_t5kaLJr17Upz0yDoj6XC2OlqrI4SoWCkJPkjuxWdtwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdkhJMwShptY53miIWd9sUyQLnzcB6CDPedLQKrIlL84trrtYqh4ckrJjm6Y73oXB6W6Aa9_WN-xKcKFwWXqn_pisOMr5-LIGsyAON5UqnTyARCFKmVjUZtIfNBkH5Xj1KJC07LrI-AOpoygXd0digvxaVfF8_eryV4_UnUskgfnA0kGSiMOlZS6NNq6C1VpAIcz-S8AR-0-9JZGQgegpDTUq7ZLpqDktOFPlCfnko468AwzVmnta9GZq_TM_aGrVLIxiQuO7txwieFRlJbgblPnnpCpxOO1T1ogf9PrB-q3SEl7msLWcE2qtZJcngtRT-HZpD8CFU9XgFhkowktRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=TMzqROF2F9MJFXil5FDoksHBKG7bdhilLt5NXnGS7ptINEu68X4VU_bwyKqhJhTw5znNMrCX6sQpsfvrbkZRsLBTTYaFpLqQtZNfSJmz9ue4nGjs6FYs2gopxP4dz8AUpbiLAj89GXAUxsINdkZraBX4FGAZYiVk8JxOjsZKUqh5idZHkf_Nuc7Fe1drKEAUdQ60-f6n7ESqrCrrM2cjQwO-yBA0HRzpuglWwh8069uElE5AouNBR3H3Tc1o7oW61sa-xhE-Cyl4vjFEkbPACOvzu4F9sgw1M7w1qe2xwQcdeAjjBzOZLFyAMtKiT7i0EdX8vntVYmXUikhKL8Tcog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=TMzqROF2F9MJFXil5FDoksHBKG7bdhilLt5NXnGS7ptINEu68X4VU_bwyKqhJhTw5znNMrCX6sQpsfvrbkZRsLBTTYaFpLqQtZNfSJmz9ue4nGjs6FYs2gopxP4dz8AUpbiLAj89GXAUxsINdkZraBX4FGAZYiVk8JxOjsZKUqh5idZHkf_Nuc7Fe1drKEAUdQ60-f6n7ESqrCrrM2cjQwO-yBA0HRzpuglWwh8069uElE5AouNBR3H3Tc1o7oW61sa-xhE-Cyl4vjFEkbPACOvzu4F9sgw1M7w1qe2xwQcdeAjjBzOZLFyAMtKiT7i0EdX8vntVYmXUikhKL8Tcog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOygqNojSISExG2shF5RvF0DspZ0XiJjf2NURHV-U_m_UOeDhsi7lSrke814gwRXL1i6ID3tqb4y8JEDKjjWfRHspxaXC1x_tpqTwMsv8ydEIYl6yKXVW-ZZOa9L5v4Ik6BWed7FwfKAQabf7sN6--EDq2IkRpGhitzZsO_s_P0VtB_hmeEIJGXd18dk_ICSFwbT7NHdfUGLaE3BqCBi3LwmjD7sgJSBfwgsxE34gBs2nQ85Bk1S05u5X2We3frAJ2vD_aJ_bRbLGdr2UocPsf1GEZE55B9cTOABw2eIFA1FaW4mdURshjHtdhTMweuBO7ylZcFaRDKufFuiGrDVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23822" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnT4st_ywiQZy5JwnVJhahl1LS9ReMjz3mHg70TJuZLq-cgT0izYYFnclKBsOF9VxtepIkaCtTdEQ4NOvl78prchUZNiFFqp1w6RrpR4cSbB6osAa287aTPVHaonl0m0nLI1PPHiMvOzSpKU9bzk76Y8-dp69HrkYef8G60vniRkKyPMoApSaCBuh8sDk0kdmez1BO6PCLcSc-EI04t-zbY-1Y2ldNIgquOBhn687fJX5STqaBkbjMQX1odp5umCbUzmUnz3HwXi0ZUpMxTO5W9xzuhjtiQF3N7dTLQBvfC7CvIOj2EVLWPMb-DCtmG4RSfEt7QWkESwEJag6oc87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23821" target="_blank">📅 12:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=tq4RZBFQY6X5pK-Tx06NzKVQJPNil1H-aoEdiLNb86XL-EN1gH-eSOjdUfgOvSrlmTMqEPHO48bRcHsKlb2FIyQ1Vm7UXfUuv5ZhZ9SOcy58uGG7PFKRfVqeuDfaMfw5O4tjDoIKoJBx-sSlf6VD7fcLxXTpdrDOphRFWYfccLGWY6PwLZTDuKlZNWKpvqw4SgtD22BB-mSpUMtSImQ_QKB50T38gTU0Ri460nV9UMU8HWoznuLW67rN0NrR5kfdupLW-kHF_EgPbHSbIiC5arhLAZOAaiDN_QXR4ZpR0xdZskqNwTvm1AoheaCrT7QTt4pjylIuB-OY9fjvTVyu2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=tq4RZBFQY6X5pK-Tx06NzKVQJPNil1H-aoEdiLNb86XL-EN1gH-eSOjdUfgOvSrlmTMqEPHO48bRcHsKlb2FIyQ1Vm7UXfUuv5ZhZ9SOcy58uGG7PFKRfVqeuDfaMfw5O4tjDoIKoJBx-sSlf6VD7fcLxXTpdrDOphRFWYfccLGWY6PwLZTDuKlZNWKpvqw4SgtD22BB-mSpUMtSImQ_QKB50T38gTU0Ri460nV9UMU8HWoznuLW67rN0NrR5kfdupLW-kHF_EgPbHSbIiC5arhLAZOAaiDN_QXR4ZpR0xdZskqNwTvm1AoheaCrT7QTt4pjylIuB-OY9fjvTVyu2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌حنیف‌عمران‌زاده از نحو خداحافظی اش از دنیای فوتبال:
یه‌شب بابرادر خانومم تو باغ بودیم تصمیم گرفتم از فوتبال خداحافظی کنم به‌خانوم هم گفتم یه‌متن‌بنویس‌بذارم تو پیجم، صبح که از خواب بلند شدم از خداحافظی پشیمون شدم ولی دیگه دیر شده بود همه زیرش نوشته بودن تو ادامه مسیرت موفق باشی منم مجبور شدم خداحافظی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23820" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=O7-i8vTu9ifTMQ6-1Qkm-XWmKYD8-BnadgsY-QTLjcHAG29yCnpoRtnkEoeEWU_xQUN7leFyALOpEKFryQoo9gaX4IwlbzTpkMwKxqqs5fgU5R3tmixEhlfHDh-M3A1WHRW-WzVR_lWSQXXuH4LAiLvN7JRaTMLO-Fe_aMz6gYCmjAGRvEMPLJ5Du_9UYtXwe8V0DJJR4M1FGcitaTqVdJJkIrZln0L7GII81DlUXF2LtRmM_Iq0pkeeM592HEYFH10OPf6eAmI8k5eyxsMdCRCShXnw8dT_Oa07lMAC7LpIGibQGwu1N5e1GIYyrmWpKPp9q8_wsqBlX92v9hrVWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=O7-i8vTu9ifTMQ6-1Qkm-XWmKYD8-BnadgsY-QTLjcHAG29yCnpoRtnkEoeEWU_xQUN7leFyALOpEKFryQoo9gaX4IwlbzTpkMwKxqqs5fgU5R3tmixEhlfHDh-M3A1WHRW-WzVR_lWSQXXuH4LAiLvN7JRaTMLO-Fe_aMz6gYCmjAGRvEMPLJ5Du_9UYtXwe8V0DJJR4M1FGcitaTqVdJJkIrZln0L7GII81DlUXF2LtRmM_Iq0pkeeM592HEYFH10OPf6eAmI8k5eyxsMdCRCShXnw8dT_Oa07lMAC7LpIGibQGwu1N5e1GIYyrmWpKPp9q8_wsqBlX92v9hrVWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23819" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23818">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23818" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4dEk4K7U4-PmBowuFlLbq4KFQspdbHtDl69rF5e3eGJ6lyvYKzgwn7W21CY84iHJN55Ofbco_Tea3DKyQNEDXcC1qEoliPJMoBlSY3k54caWLPtl90BN5z9Tf77DvhUccREUOkWvRGkMKjB7_ZJg_LxQ83GXYrNVEwXdoMCTxob-Np6nssKzPDcYuIMOPQOp2rmgOhiWKg6k_u1CvYMJ4V-eHd3IPfM62imbxj_F90EloxbptajRVplGR6evYv1OOFBXniJPh_gaWGU877CNOgxhtl1Wq2UZZirjJ1WN4UFbrOT5zyeBNbXQDFAzqXBzVKcpZVWYU4RNAlcAQjZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23817" target="_blank">📅 11:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=uz6_FiwkjnUX-QnUsI7vNpZnSdLkKHi6nS5BjJxT8ij3chl0fkdlQu2fZZbWHGk7cKu_9GA2YkPPsUPDzkbj3N0nzFNawHHO4eYD6BrbBYjYAEIlSKK6mZbZxdLuXoC3gDkyaeeXRIqnIa8-ilhp2Xvf8Lb0XkH1jIRFFib1R5WlKNedIIyQJ8BHUGQhpe9Ba6xWxUtFSkIdpavtfzwyuIffd-yEvCtrcEcrZtjT2dvwEXtC9vmOaPKexFe-uH3bG_Ono-BQNpmb-7Hgsr6EUNvLFPWZOyL6si921JfSLP96zkBqVDPl5xbk9G-qz660yhH06nmDG8Syh-1x229TNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=uz6_FiwkjnUX-QnUsI7vNpZnSdLkKHi6nS5BjJxT8ij3chl0fkdlQu2fZZbWHGk7cKu_9GA2YkPPsUPDzkbj3N0nzFNawHHO4eYD6BrbBYjYAEIlSKK6mZbZxdLuXoC3gDkyaeeXRIqnIa8-ilhp2Xvf8Lb0XkH1jIRFFib1R5WlKNedIIyQJ8BHUGQhpe9Ba6xWxUtFSkIdpavtfzwyuIffd-yEvCtrcEcrZtjT2dvwEXtC9vmOaPKexFe-uH3bG_Ono-BQNpmb-7Hgsr6EUNvLFPWZOyL6si921JfSLP96zkBqVDPl5xbk9G-qz660yhH06nmDG8Syh-1x229TNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو اسطوره برزیلی فوتبال جهان:
"به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رومال خود کند، اون آدم کسی نیست جز لئو مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23816" target="_blank">📅 10:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=ZU6wqcM77CQI3bjT6tRkRBBhKsQCIDfC__ZjdtYkry1qkKA8GPOz0rxEKxhx_uR1c6BO5MSdZk4bimF4HCvj2ZFl_Lv3RxL-3Bnnb_xPoGNXh_zV-DfZEL3i7zzF551VvkITLke_TZP2Lj4RDjCRz_6cAXKzEGUskKc7-RBe5YpgvNQHV0SDThaTCF_6x8f8O_e3T4e4LadB0bZR9PrUxxli9xMN2Uqvlu3JYD8ZbPKzCiLsC3WinQ7jFnOLfi3MRb6LwLuLJlrTiICyqP9vHVLJ-gyPR66JQ7s--nqAMSdVpNBWGXb7dl0dOldaQY1SwMwQXsxL8r_RB9t60UiV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=ZU6wqcM77CQI3bjT6tRkRBBhKsQCIDfC__ZjdtYkry1qkKA8GPOz0rxEKxhx_uR1c6BO5MSdZk4bimF4HCvj2ZFl_Lv3RxL-3Bnnb_xPoGNXh_zV-DfZEL3i7zzF551VvkITLke_TZP2Lj4RDjCRz_6cAXKzEGUskKc7-RBe5YpgvNQHV0SDThaTCF_6x8f8O_e3T4e4LadB0bZR9PrUxxli9xMN2Uqvlu3JYD8ZbPKzCiLsC3WinQ7jFnOLfi3MRb6LwLuLJlrTiICyqP9vHVLJ-gyPR66JQ7s--nqAMSdVpNBWGXb7dl0dOldaQY1SwMwQXsxL8r_RB9t60UiV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23815" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh6JXTrQf7owuJFzwdNa0Fm3grMdgOUAKFe0WEDvI6_m8VqgyWX9gvyajwyP5pwOjMoDe9729tqcDy_ar2V9R1BN0VJMO3YcZhVmAW9qArinqdYKeraIbuGqjaDTH73WRmgTx9cqlBARX7IjFTzxmclbML-NdeQoFLh5NGbTUEIjoGy4750A7sNnCyF4a3hu40uQxWIdENeH6j__fA7EsuSHUzRj9ksl3kH5qOkezA_BPIhmLXLZLTznZ32JpH2ZjYLw52ku81cxeh17FDEUW8EkVpnnqBMHBZbOkV_0Bs4Ioldna87lLKc2Kiv-uUhUAWR4vY0Ock0BfE8LFvnabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23814" target="_blank">📅 10:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6Uj7m6TAeaEA9RjcoODu34q9x1Q0q3cenc8BrMpoGSTgxYz7Hu9yCAzb3IB9pXt8QZMqcxtqvn0GRuYSMRF5GN7gydqTC1Ev-f8inPwzC6YwqNSPaNv43KSiv1WmohJ0cvsG4LdLbcdvFXi3CJZXIOMueHz8dwYxaaYU6zEOd4LhfEpbhJizG_ABjvo3XfMFlaHWqr7xUtRFl77p9GhcQY23cqHTwh4r7e3Ht2KG2lzciwV83pV79-O014kFKWghyLaTXH_u16kQFl1dKPuRbqoanlWbR57XFGyR4ec6VdgNgFguOr2xPwpfDLWtCbigwvCeBjox5WD8wkpYs05SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23813" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ تحقیر سنگین قطری‌ها مقابل کانادا و پیروزی مکزیک مقابل چشم بادامی‌ها در گام دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23812" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=iGNa8-H4RPQ1wjLaulVQwoZMhv6DNb5U1rovvbFHh-JkoNJt0ScVo_9eEHe_6nKjLgLUs8lRKxskKMQeQLnxcz-CN4JlDULo01kCmkZ1bUU38gIqVlghLdCXv9KLjyw5Hm7zcZ2S0y38naPEupKonQy3vfOWBisrv2pOKlx4swItC7A3B4wVNnyBweETG1jkKU1BkQTVV2G6FuOWrQgysfxLUou-NyQNkiVx4hEsT8OXnGRwW74RX77lRkdzGAFxUOwyqHiOZvctMp02VeP1Mb8WcaGjuBnwVq8eDUrXTk4cg2eLuvLPg37jE5dlVl1HtlrLE9Xp_0PuGd3nwYe3UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=iGNa8-H4RPQ1wjLaulVQwoZMhv6DNb5U1rovvbFHh-JkoNJt0ScVo_9eEHe_6nKjLgLUs8lRKxskKMQeQLnxcz-CN4JlDULo01kCmkZ1bUU38gIqVlghLdCXv9KLjyw5Hm7zcZ2S0y38naPEupKonQy3vfOWBisrv2pOKlx4swItC7A3B4wVNnyBweETG1jkKU1BkQTVV2G6FuOWrQgysfxLUou-NyQNkiVx4hEsT8OXnGRwW74RX77lRkdzGAFxUOwyqHiOZvctMp02VeP1Mb8WcaGjuBnwVq8eDUrXTk4cg2eLuvLPg37jE5dlVl1HtlrLE9Xp_0PuGd3nwYe3UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیک‌امیر رولکس برای‌بازی درهفته‌سوم مقابل مصر؛ صلاح و مرموش روز سختی در انتظارشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23811" target="_blank">📅 09:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0EZUU3cS22uH_N1T22PxF2TBZhUKPWy1MNFoJqeRdNjsI33xNyVTS-ZffjEg_9JJI10y4QbmUWokYbjm-GXHtXaWZR5qlee-nRfCZKd41E_Yb2wwO-sz-Mo9lQqWLcMNnm-PqbXWjV1all05fMmAyenTMa_kg9ilPPjfz_lS27OdzTeElirzb4fxTXEYzU-NkFSYDP-ZV_WhOt7T5MEOsWUl7P2RRT0b7pxtDUd32ymwSROThbRveVGayPNeC8Ji43SvyOXD5zegOXUzGULIgiQeeIyFQug_WspJ7hoZkiKGB8kvkmFNunghqn2nb_3Nj9Ybysx34KBwICocXFcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QM-D8lXKcug7vWZO6pkI1irrbklVK5XAWtjMs6GnFK8kxBwLr85t85bPO5hGMJ6S-1VfazxJPjZIjpCzaPRxiej31aim5NKxUsRhwji7cO1Zs9Exa6yewKBCGBWe5V5Vjw1vwu-vFewDDDybqxY369UmPv0evRRTq1kVnhZv2Jep8BAnVY89SK-U0OsrFcheRYwiWL0pzgRUffnV-hwdyqEH4sCr_vp7UDJnrxoX3V_M_YMEfs8gLOiZLvVMi1h3PP3GWxwQ7jxEs_GDRgyHCLrQj9PzYFvEnfXLYYnCdHzamn8fAxPetVFGE2bl15jbef6H3vrM2M6D4LTQi7lmLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌ @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23809" target="_blank">📅 09:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm5ZD6mxZRaOBOAKHCilwaC4SrCbJpHkE3XkMnak0DQQWzFFvxkTGjXs6vTVca-4L2eth-iAanyQJC3J1IJI2sKYk8anpABGTw7z8oPCl3q8_SjTozgar3EOXWV0lxUajcwIPdwRx_2KQVAT3uo7Z6AeXUiSF1iFzPDYFsua6i5s_RIpYnb3SEye6IhQL-CXI0X7reY1Z5KqoQLtjqodZ7tJFEJJTcVB-qQUZ_8OXSug4GYyqnXT3m5Xfw0B0aHlKFdAFEwXQrRBd0bXdL70LZnzJFBRrT0Xi4TIXXszlFY6O7MIKKblTotkvlg9-EmAUt-6RjX067c92MLGu9PSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23808" target="_blank">📅 02:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=OWevKRI5rAmRRtxNNQbtjwtHujwsQdK5RBE3SHe-tp7XeTK7_UeIDgTyc6SPzVplJ4DXIwiael4AyRoCyeka7FuZiYk8kzx0A8SbIM1FB4QsSmnDHQz5TPKAwti4fdVSjRsxo4NcGc9kSKYqNRFNHWWkFuKqWKEqSfW4G1-8FWRE5QR_thZaBT66rQOZm20Zpq0OaE2c42NwBQYJDeQzLcjaUaAHSMhXaXHPc_cV7LyptM4wfIirqLpzpNFkkyhIMTsf3in9uPxKMhGKcanJTHXzG69ARH6nUnlpP0NTLdziXJhTlvqnhbh2Nekfsp2LBJGyj_RjsidMsGhMQhKg0kzUVOTU9_Z5tgIweOZbD29lp1NdYxMNMin5aUBYOUlycVeOrl5E2cy1_5Oi9HnEmFSVXSAnH_60rL8fTwK7iHrDMvmnSu9XncYWpuzrArZF-wSDMc6L1O9WfGzzscy92P4HaMb3l3biSWlWI_gobxG5IKCehkDfJxOr6JK19mqI9mVSSaZ_M7jRMpSImrUt-2T-OtZjAPn1cNL2PslIrAJUl6zDHAOroMyL_9G_en2wmvs4yF9LaUg-RND0dDL9uJUTQds0tbkPDZUG5VV952tiRDKR10VdHWnoetY6gpLUm8nl6DOuIqWA0__99gZg45BCyNSiCD5frUEutRuQN_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=OWevKRI5rAmRRtxNNQbtjwtHujwsQdK5RBE3SHe-tp7XeTK7_UeIDgTyc6SPzVplJ4DXIwiael4AyRoCyeka7FuZiYk8kzx0A8SbIM1FB4QsSmnDHQz5TPKAwti4fdVSjRsxo4NcGc9kSKYqNRFNHWWkFuKqWKEqSfW4G1-8FWRE5QR_thZaBT66rQOZm20Zpq0OaE2c42NwBQYJDeQzLcjaUaAHSMhXaXHPc_cV7LyptM4wfIirqLpzpNFkkyhIMTsf3in9uPxKMhGKcanJTHXzG69ARH6nUnlpP0NTLdziXJhTlvqnhbh2Nekfsp2LBJGyj_RjsidMsGhMQhKg0kzUVOTU9_Z5tgIweOZbD29lp1NdYxMNMin5aUBYOUlycVeOrl5E2cy1_5Oi9HnEmFSVXSAnH_60rL8fTwK7iHrDMvmnSu9XncYWpuzrArZF-wSDMc6L1O9WfGzzscy92P4HaMb3l3biSWlWI_gobxG5IKCehkDfJxOr6JK19mqI9mVSSaZ_M7jRMpSImrUt-2T-OtZjAPn1cNL2PslIrAJUl6zDHAOroMyL_9G_en2wmvs4yF9LaUg-RND0dDL9uJUTQds0tbkPDZUG5VV952tiRDKR10VdHWnoetY6gpLUm8nl6DOuIqWA0__99gZg45BCyNSiCD5frUEutRuQN_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین حنیف عمران زاده به قیاسی که سانسور شد: امیرحسین پا میشم میام پارت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtXvDSI_-TQnHSwuCoOu6jXZV9_oFwieYTrt24spRbW6o6vA7UsV56ErU4BaRJSHtard5DlvHb1wKQJnpKyl0_9sy7-jAAPLvhWbQ-qi0TpCm_N1YaZUDKOjkajSdOyFpJb9CxVV3OjJlHxwxx-GChI806n14RfwXrdeJdJLqG1RGU9wKFDsZvGh0opIoucZakGUH-uFvU-iW2f7alnhJsMiyhKLvDrCIE9g6zkdKx8UiIcL2fIOzBMxVYxr0UafxhlNKdfhpcWbxr_PkTvHKgL-6ynoP0efBLq8UC2RKaTHAFblHQ-rfas79iYLGQeA9hUWFQ82QGYkf2y4iwdr-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUF0R3I14e6CF5hus2etCJ_IFRJ8SBQ8eI-MrUfh5WDEWSmKsDGfzD__biqU89b6V530aWxN9w9IdBy0A-FXt1WL6Vb8TgoSG5T83M8we1CrELOfUKGkgrvimbZF6wgQs5SWqiOaMtwFu52c2dLY_76vY_A5E5rfOLLouiMtewuLQHRWgJcdfT0gjj4AnMcWo2Ru7hyFGd2xZzVrc3GBTdSI7RkIitTRuffy5kx79DfCqBvl3JUZh2-hYSWzX1yqwoE4hDtDTjPfVRifNt-x_2NOmOLpfiCQQ7zZVreecHgiLHc4IiCUIhtSt8E9b4k3v3XalEkb2sBIk8VIYQM72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=SQRUyIIt-e7RL-v1mYN0luf7tUrZbIWF1tBdSyn5hJcnJ0aiR26mBmGnFld-cO6kjBRLo3f3E7b9nW96lganUBWRJw_xqnOODKALC_OcheGr4Uhp05I7L1n1u9CUqf0hxbTjX6LyOj3y2PmEkabSR3yvSwzRMpsodvJ0SggxC7Kb9X28b-D3HQIaakGPisy_VCPvnOs9DcIfcjMwcLIdScpi3LsPcaCeYiwnlPNmLV8dg4k_CI_mOhKwrqrC1t72bmow9JOzflREKFklTZt9OEdW85XlK2Axnixsarbz0GrQ-lEsr0eazWoB9og9mMETMxAigJGnTQ1AYeY2O-Jhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=SQRUyIIt-e7RL-v1mYN0luf7tUrZbIWF1tBdSyn5hJcnJ0aiR26mBmGnFld-cO6kjBRLo3f3E7b9nW96lganUBWRJw_xqnOODKALC_OcheGr4Uhp05I7L1n1u9CUqf0hxbTjX6LyOj3y2PmEkabSR3yvSwzRMpsodvJ0SggxC7Kb9X28b-D3HQIaakGPisy_VCPvnOs9DcIfcjMwcLIdScpi3LsPcaCeYiwnlPNmLV8dg4k_CI_mOhKwrqrC1t72bmow9JOzflREKFklTZt9OEdW85XlK2Axnixsarbz0GrQ-lEsr0eazWoB9og9mMETMxAigJGnTQ1AYeY2O-Jhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آرزوی‌جالب‌خانمی ۱۰۴ ساله که‌تک‌تک جام جهانی‌ ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست! همه را دیدم و مسی بهترین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJK8C0MQ9TVoYUFD6C5sTXqF84uEyOD4I1_2BjkGXBM37iVOmOoA2n2NJ2GfV_gxohO9V8m75k7B8uItPY5xmY0gaYye8CVlltMrjRntVknBMDML0-vBxCU5b_zo7nHwheL3UfknNDJH1kWTdpOWXXtu8DHnjm_-vLOLRfUdIMsb9rod4_pQsmpD6XOSfnqXsZn32qrbkXEZ9srHa5mu5UNo9cFU9HW2jryrSt_Q1QJ96gjkxvag3gPlQpT446WFVHoWpocz3tJ0qLvGiZTGc5TUYhduJWtZkV0Qty6nfY9ZsUu9Bt1y6ieC_yJmWsi4gcBr_joBZn8ryLvqsvnbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQVNH9no5IZZ32v4-CyhnmlfEfoSkKwmrrwy1-sh968mrsu_IwC5rUtwRS_dRBmWmwrec6k40QGqVXE5C-4I3VPmDQs_i-eB88TKyI3Bs_UrHso_P4Kwfu9oajgsE9xHtJrMSLzRUi-FrYLbVrsjNQSEKfOydy02XmhSWwO_IHOXDPHWT1Mm-947ZldqkEjWNJaax-XH0OSr1O_9NHSFg2QbA7W3ntfvUHVSSyeTfZq9Cc1TDXEgj6tHRTY_ng9wC6gfgPL208GepnS5XMiqa-LKU4E3JYPcdG4ASx86ZeGkPvu_wulHeYfdNmA0aGweoPhyE0Tv0O1paqFGaf62vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی
؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23799" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaVkIvPkAx-1i39_U9z17m2k2i9mxCu2hMhZrxmL47fTKFnAo3mpu-7_0bXBHPuK86xtGFGlCsVVqUsBD0j6vP9q5zL7ZOuDXF9bNw2Hhvk6oeP_yeL2OZwVipHpuVWvNN37_2C2vBMRAula-plG90jjFCxM9h_cpdQOrqJE6fqIzFxh4uN4ZZLBgHijPmhdkkF-NeoS1cP8Rqqwcx2p7531yOkg-hJthPbOh8-TZg2lKb2WH6Rw4m10rAW-2Bu1p5qyinBa2ZtklrievGLgNje5JBJ5OYn5hFVpPOrTFZVPE-J1XZNfAVGM97GBZX7a1Qq2prgOCWuXsZA1ZA8MaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
یادی‌کنیم‌از شبی که ایرانِ مدل کارلوس کی‌روش به این شکل تیم ملی مراکش رو شکست داد. شبی که تموم مردم ایران دوست داشتن ایران در جام جهانی 2018 روسیه موفق شه و از گروهش صعود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23798" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my_uwEai0cpmW_MxZ7-D6N2SB4nvYQrf7YL-yPt_A8xjylFJGm5x6AlCRyVbfHO8XRGZ6aUz69IP44AgnRefi9-d87WgM0JypgQ-arJOlVpL3SfOurhYz-AC0XvDH279d4DeaTuicK9JEUpyIL8I0JS1qXdfR1KLHBjapEHbd4p6LnYqceHSxBKVu3QF0fC8KpLJboEcTW7znWf2ATPVJPdCgZqQpSlXz8sgsiwMWQK5IGjGsYFQsXqQj0wi2FyyT-7OF9taoV3Axqw2iRUfSZcYijQGzWF3qkHRnh5BW9o010Nd2kCT6HwI0H27ojzOgxnjp6TCS1VQzly8VHyhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛سیدحسین حسینی دروازه‌بان 33 ساله سپاهان که پارسال قراردادی دوساله امضا کرد باشگاه به مدیربرنامه‌ هایش اعلام کرده درصورتیکه باشگاهی او رو بخواهد با دریافت 10 میلیارد تومان رضایت‌نامه‌اش رو صادرخواهدکرد. قرارداد حسینی با سپاهان برای فصل جدید 140 میلیارد…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23797" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu3iXK9H_oF_VPKLEDDCsb2qjFFKeSOBuD9nGnbDIGGzidlO6v9PUAweJX23XvPVvR8Ka8vPJ3YI8ebJzIbek5gU6g6miOJ9MLPD6IWDTa3L2h50y6TSZzJQzBwkLJAV71oI6k2z3fG_MJSnwsQymyfikHw_gCWYgtRBQOPqSe0cVCxIrwi3ahHOnDb1n_l1o_YBlw1PZwx9nhFnuGI4F5qdMqeyCyAEDuE7UMcMg2JuESuGGbKsVsDI3TyFEpWFPCyMwnN822N19yFDiE5OuZCHTTYrsX04VfRcsoiTzzuVTz7HG8yzTYaTSOGtH7Dhmbmx1TPblL3rCBF-ZU5zNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23796" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0oUTRNR5256rtKDUQs56Vb7eD9Z3IGooaXxYv0hjTG9i_H18ecVSaYvFdTc_AZp7digzopGNOcn0vQqdg0of8CDtN7TNF9TGm_v-OVUriuDJm00XGfSbEYnhCd1SwLn85AgoeKv0kEkiWlDvpgO3dmykaC8_NvENpHXbS-9TeYW7bR194sCBlNl1YWa3hcVEqAXsVNhiU3VPHVQHPpDL1zlr0x3LO_NI2dvb9ayLGrRYvQIWEyOKNL_Q2TslUhbZRgt8s1nO2S98YAnHAnaQ9vpQTCVfhO1N5k7w_LO74GBhYTEZ9clIqzwW_3i8jNGec9CjJoDGTQFF_UHpOf_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sp48oAhelx1cFzAuQnoTy_2B28O7HxGKXkZ26WfS6TeIpVbj0lnlL20SxYN6Np24hPXkFgs5pD74VN7cSaGGXneP_7BCESTAgmvX4Jaf7xQQmWk2dDnB1Idi-0VU42BGcyQwn1K_3CvpYihZw2XlhhdLpDwq-xSFZX9F4CH0fB1J1AP4Z8qq1aUsqb_fVoyhIrBCBQoi69egOV4dkhL8RYkixlDo3nK8cvJQL2BS5uoWv8p0HzQZe_af7tu2qJonL-yUokltTpdxL9HS6UjpB7fGpyfhEFao1J9EO3r9b2h1e-2T8_8vXlRAJNmTkrOoUHBWq-OfqEcD2ZZKX3677w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYdHr-r0HltAVlottYKDbOP1gLjZGGhpwt8UgIwtUCp8e7d0_L9A4TIxuR2TTAbdgRumyr1vN-reUDXNIwYGbzb_OQD_J_Jo5tjHDB9ApKcpxmGiwY70j7BWxGy8DaPFxAKa7PhBplfZjWCy79WDY-sgMODtQqTeGpQjmWsccZVztUxxaSdhtcEI0FOHXWK1-WAAyt2_luMjjlImOR_t53ctSCh2pGj-87zzSi3r6IMcntWN5fo2gB_mgbMU4mzKEF6oDvA7E1LIcZn3I1XLsV4rTQZk_CpmnkfqD8keDPryjzSk55IibAhYNR-PxmLe3MYV3MHwf9_mfpZ9Um7tDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKumgD4DSznZq2TyTzqjj-Y8dO_doTHo1ZhnekLxobkP2vsssJSaax-Psis3TPXAQ5kwY8-3WiNW8UmZP8T3oUSI5ozV8OPL_a8vNSBTO10nVqhnEFrDEqHqRMvuqrzN_F0V5djiH03uschY3ACV1Hs-nT0ui0tJSAVT5HB_OBVHwo4Xrj6vc1geBiSwE7GQL55YUsRrwDwC2lZ33ZR8_5phbTZOjRSjwe5kd3OGhEZBi6hmuK5Kt0oEtQHiB-JE1S5irrLwfGm4LqDonVJmJ29rTi6k5vtExKpoCxcMeus_lxP0d3x3KYJ1tKainveO1YFOSa0MR-FzBFWM9UphvZTiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKumgD4DSznZq2TyTzqjj-Y8dO_doTHo1ZhnekLxobkP2vsssJSaax-Psis3TPXAQ5kwY8-3WiNW8UmZP8T3oUSI5ozV8OPL_a8vNSBTO10nVqhnEFrDEqHqRMvuqrzN_F0V5djiH03uschY3ACV1Hs-nT0ui0tJSAVT5HB_OBVHwo4Xrj6vc1geBiSwE7GQL55YUsRrwDwC2lZ33ZR8_5phbTZOjRSjwe5kd3OGhEZBi6hmuK5Kt0oEtQHiB-JE1S5irrLwfGm4LqDonVJmJ29rTi6k5vtExKpoCxcMeus_lxP0d3x3KYJ1tKainveO1YFOSa0MR-FzBFWM9UphvZTiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خاطره‌بامزه‌حنیف‌عمران‌زاده‌مدافع‌سابق استقلال از کتک خوردن مقابل بی‌آزار تهرانی؛ حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2f78mQi2sVKM144sGWOyAnHtcQNAt_-afjopXQLVYgZB82GXnc2rfQOv4VGWf3S2IGY-C_ZWhn52RVSX2IMbhYGcHS6NGyom2Gy9sTrv-yeyG2Z_t-QnrntnJ85wqDKqKDBaQcAK3Fq3XQLJ0FBcwvd-rkzJF04TjpCblGAJY0B-AxcZDwttzlfI_i_Ugg5eg8C8733LTDr88MfGLUg7j1HQPHPI5RSSFSnfbJQpAoUOE2xi-KckFn_U_dwg0jL4K6DK8MzFXs0UDmiJBTcp-mQQF3orOMHstUXOwGbL1RpGjC6as4NHXS39Fr2wPZqlr42K0RSp7L6lA0QgZd2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmeWYWXwARW0ITCnT-o1gTjU0zKA8Mr7K9ly3R-HE9hPc45Nw5Y87M5LP68kscAwzWJeSfef0nF11NbC2njgy63YZfjxAl3SekDSoPnJesQ12qc2fM6ZUA4pDQA_GJINLGBxAuOP8Cz8ciK9qBru_i7iWE-BKkXMyEULZ_-c3CksfQCwjELv95ELxcJWDMwlh6ArkiqwyTvPKFRYeG0sBlUuWrLMMyr4biymckphP3sqeoZJbr_erGUpwOsGovd73M-EFFfPe8jX1dv4GRJvGaiKE6W09jIuJ873efQmLsOT5HCUZVuKJkQLxer1LIbnQYTbJOPHcxtn-QeAChNg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23790" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc7gnE3scSu4I8GpukY8Y_nMKrATteo-xG4pfhxXKxIHH2g_Ibwte2-L6vGmmiPhnekOLwHvWqpFT2FmB7C6vCW5r23e_a2-WqGcqFRotPCDp78fGStXPBIcKOKi0__EbqsfTpA56seYbtaFj-zT5b1xmAl3fQ65L_u_rUwkiJdXqjMmvLc2sXp8mkXQpiA-oBkOhafiDKghikxkrdiIA8U0dlCF2Rnv48-fCu0UolLMJNfAI6WgA1yKFiJlc7oGnw_bOqwK6xpoMMEAdij56txo3bZPiNbiEdKn8uY_g3t23dWc06hMAfGY3WpJ8qp_ZjrS-pvn5u8yXWHJVKIfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRygmVLnUsrtxh2WR3kKb1unlG1d6MEQzmadLU3FeAr9T965_KYrQ2xsEe7AHjaUBY5ay3pHITWWGdOEuyeJ0FejBuoMHQl0dMusBEcbJ7iWeDl-QzjNyEjghs6z37VlYhd8kmwi30EA8OmaYtQFs3zVHvFikNJyPNvi2n4lBBtOjAXUSNzs41EokZvmLRtq8kTtwDVMr6jwlmrXuyleKkLEhhGHnAJp2ODE8xIZv_QnsPSKzviHoxi9ImGPv245yIaZLPmEyLSg5eY-mvpTuLXdW9AXzITdXp7xbfgleDem1MlGIx6-G9gKdLmP0vaUORQojs28Gosid4gvSYkN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqVEKgQ8A_0pN-Kd7E6jjzfxJUHsPvJpNbsoR5k4mj8FE42WybyUaOQKriNtcrkTc4aYN3YQ_TgCv27sSACMg0BHomsxdBuSO_XHHdh604uJzSxIT4CKa2SKv4gvj_kGzzEpKW-FZn_I-TNU7Yit87PUDkCapayDzsi-3GsGmbOszsDZNI8eFLzTojqVf2tkM43jjIOJmoi2a3rjp_WipSef3jy5CoChxBG7v4ONgaBXlcPhN7SQJRf5a0c_LiqZ8nVq02Z-uhXf4kavr8hOofZRvHmPbph8rNE9PpdipRMIaQ_3g3w6dBRBCla9Y9KH1pz9BOyBu0bi4sj-Z4Uz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=AM--sl0nfN8o6dRqyFGc0skAm9Ja0jH2meNSBDqDXFrQpUxiErHOUL_N_7NkZaakTytUlv8VD4S8gE__ffF1OGykV9jo2jwNR_Jos1F9xzwBVBW_U3eF1LSCKz7J8GGUsbFQKTAUMHrJpcv51YqrUG1TrLOtKztNt6ghdmDoFUiVZgsKdygY1oXnrjd4HIeAszq78vGBTjLcTj2n7h1Kl36rdS1g63YB1F7epgELto1nl91OGTbC3VIYs8rF32XDGNHwzCJeNlrh4CEwyNURAd8Zip3ytMTlkBJcqPsSHmeV2lbuGML4pePlo3bGmSpreRB9sPCRQcX5T4O5LE1Igg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=AM--sl0nfN8o6dRqyFGc0skAm9Ja0jH2meNSBDqDXFrQpUxiErHOUL_N_7NkZaakTytUlv8VD4S8gE__ffF1OGykV9jo2jwNR_Jos1F9xzwBVBW_U3eF1LSCKz7J8GGUsbFQKTAUMHrJpcv51YqrUG1TrLOtKztNt6ghdmDoFUiVZgsKdygY1oXnrjd4HIeAszq78vGBTjLcTj2n7h1Kl36rdS1g63YB1F7epgELto1nl91OGTbC3VIYs8rF32XDGNHwzCJeNlrh4CEwyNURAd8Zip3ytMTlkBJcqPsSHmeV2lbuGML4pePlo3bGmSpreRB9sPCRQcX5T4O5LE1Igg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌جالب‌ابوطالب از گلر40ساله کیپ‌ورد؛
به تموم دخترایی‌که‌پیجش‌روفالو کردند درجا بک داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23786" target="_blank">📅 21:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whfya5znAZiwFp0h8ZW_t-sYfb2JXFNIB2zKVW85hjlB6plz--h4nvVHkdQvQ1da5wJxR6LHWg-53Kw_1ntrg7HaEaTH8y1Mwz4xKq5wvuldkH-yDxhrYZGJqjOQyvxJHFQ02I7J5_UfE8hl0Y5m2PPfQj8jgVCaLvAtmoMKVVtrh6Igy_g69AC8SZcAq2aL2odI7Q71zzJ2JBhH3BBhR-o55xORSsj_cymCEdzuyFGqeiOL3i1h07XjWVLo9ec9NrG7tH3MpS-SFnqfMBzeppAqwuRGZIlIjI_Rv00S3H_sZ1odab21oSZSZMevcaOBleD5s_wqsJqCltYZ0Ler2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام باشگاه لخ‌ پوزنان؛ اللهیار صیادمنش در تست‌های پزشکی این تیم حاضر شده و در آستانه امضای قرارداد است.  او پس از علی قلی‌زاده دومین ایرانی باشگاه لهستانی لخ‌پوزنان خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23785" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3Jo9Ms5Ozf1QzMmE_K6GXqpDNj_tJfauhmShpiitVRIiJTwrFQspe4SDydrULAXZ5-D1l-n8RpnjpXY2-YB5dJLlyMJio3eqepbTp_-MM-buX0e9RLWDXen5KMuzKmq6UH49Y1GegB9DWwneh2xqQJTY2b_D-CgbOgl3m18MAgrlrKxlkJbyEzU1vZZu1T9HKTglJJzwK04YI2k8GYaAEE8VkHtxILVZPFC-kXOzBjcVDs3-irjQ8jSXfoYtE8u2U_AFOGqxuo4kUvRXCp5IeV89Ma-edU5hNxW0VrgJA_t9t5NyczTN_0U0jlFV4lNzsq1HpHYrpCx_BThB5AZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#لژیونرها؛ پیروزی ارزشمند 2 بر 1 لخ پوزنان مقابل کرونا کیلچه در لیگ لهستانی با گلزنی قلی زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23784" target="_blank">📅 21:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS_W_DyLfSQytBkjNehaVlGAkRmDOoGTqk9r1GoLQ-SwQE4xdFB0Vyee5Lr66CHwx2EzzbgSrqwDY5FJT20pAVgo08653IbZAhj8y1w6mzwo4-9TCfofeeEZnfGBLBhOSbrG0z1dNQDTqEoNBjrRHEcyiYM1yuE75tquWrn8XJucSls3YYQN1dr_kJYSOAwAk7pYHSicBWzSNOTBZJEsRHVa-ClZJzznBhg4KD8C-RykL0PKyUGkAwPkqyJNbeydx_30qlU_Pa_39WZrhNSu75Imng6kj3TQRInPOjWYnanye7HgOTwaGCCO-CNSsHPOpAw-KakbBvH4va_abRXaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ارزش‌طلای‌موجود درکاپ‌قهرمانی جام جهانی از سال ١٩٧۴ تاکنون‌تقریبا ٢٩ برابر شده. البته این ارزش دلاریش‌بوده.ارزش‌ریالی‌بیش از ۶٧٠ هزار برابر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23783" target="_blank">📅 21:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjUEvSkWavMjWVeUeMYLisftwzf0xu2JDhIWe93t3lOAmD18mrNy9pUcX50orJ15_picyZSL3d6gHI0mZjnYdvVlEKVRvlQLYpIPA6yrsM9oQLK75McJcFQBAxtpHI0fB248dzb1gWfm55o_w5wa_K4QR1WiDuaWActie05Rkas2rvB8zjdlfs8lHi71BPmTNdzROYb6zG3TxNvRdm5-jNIPVokgQTIzgQqYZBe2V-iJXB56NKsiIqKIDYNBSXvjwn6DJCA2goEKE_4EGFojkxyWmbf3NcCX01t5AEqPtT6j_YxhR0eubRipVQ43CIrq8QvG3mh4ux-A2gWravDhjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWHSEv_z6ehChgSDznjU0c79J7brvKKW8_VpDGBrCwxOIoLsEZkCWRBKKguSDt-AtsXpSjUpmOE-5sKLhq6hSOx4tPz6RgDyB4ui05HFA-FW3OwfAxWQKD1wNjc0vW2vIPlRfuA-TfQhAWw5nGcGAIYTDmzi7wGSgKQNoBcqDYrwK5IAyRyWVGx1CGbEH2THvrVCTTQFFeitopXTbOUPlvUF-lTe30my1KFoDa-TsuCNrTyKoAg1W5IV9wxzwQYDC-0eq-2BDlqk9tXvY7D60-galsWpElL26hZbfBQd9cOiC-qDkdPCrXSvakRyLOClMqOyAGIpTXr6VmwYu4n7yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRlOaa5NLuoxq_qBOOQtMsH-QE7HF3phb4sWoT83aDNZ-P8yDBWQNlR5boieBPMzmbF1ebLKlafDr4KBU9IvgCMLsNCWMrN4LQ3I8OB4jx8AbQDdelqtrAD7GPfAlDrok63maP__wcm1dDPoeFPz-1mG1YW6oFEvdASnjjvewlmh0jQ_9N3CTEeUReJifw3YeRUajUsATr_4ZAZLcx_ob6tZ-LfgmUCRHikO77leVLpPb2ykF17IdIsdHD2lxduB8lu70__XkIYX-xuMPN49ucHNfAN3bsGPbYRxVgi3LHyjb2O7DpQ3IS0GOXJypIk25tFxBu6rUHNzsFP01tSE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDFd_fu8f8Zb7sI6nbZelqfOsfOuhol-PN1drE1PP82X0ODMqnD5IE8Yim5GSVy7e3CUjNa6bNMg7XUNk39FcMtW3UO_aPbnSm58a6Me3cV7hpH-2rOv6KcDd4OOyLUwXVRFifp5lb5rN9C1iOMScjCMdyAcFFBoXFH0Sr_H7VAIsl0fXEUl_60jpNIXxBiQ-xo2en2fIQJYoQpdMPz2Qi2MLbwbBfcKlSxhV3KO8kQGoF-gdTUkm3XXNM3MnBGyHqKCMWxiLrIxdRqQc2uw9H_7cz7_wE9vGdAhW1T1Ry1CeED2dJCfauy1zuJrtkRzqY5ZfL6wh-6YXHjVRPLXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDDrcONUaYNKvwIERI6vCthEvZoigjICRh2AZ7WyTIvI_qPDPOvuZPL1Mg4w5J52u-D8fI5UlZfkDQWadTesOGv4HLbmxHn1J6V09-MiGSnbCdsLpVAsR8CXlmrDLOQGRzBgCvb4RfzGS98kSuQLkNtbS0dtWzTIIYeM-z7Yf1n7lKD7KJICIPQqMnUAULQkZnWG0JZCmUuQgscUK6TNO8B0ZgChKaymQY4Jn7aT6PruQ7VFMbx_NSwmIJpB1If7VkcOsAqRSl6gGHPi2FExkP4DJ_P6Pvfj6IYRYHRR8q9X0YmujEE3ZIU-IzNp9Pe_Vh9ed_RfiR7Y0ZFKRBI2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23776" target="_blank">📅 20:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=qxCUeCvLoXnkVCcIZyB4vKSa7a93aqrox_MGZu5_Fek6lmYGJGt3jD4jA1aIiQWDkFuJ2QgaWMNpukE3GRS0xQoYoxBRtf-J65U4Og2hd1bOGhCt542PEf3p4ZVzQ1U6XAJnSyfv1HkROwcfWe3K3-rj6fTI13PJghrXs7dcAidmz1u82voT6sDuunT5D5nnMmtpm0Q0Yhdl1iaHDXZtD7oKPrgR4ol2UGMx3kvW5xSI6NhlhkexPjDHqgrg_l18PRvZc4qOEcrJjyDFXsX48GvUt7Pges8wO6euBXMxlDxfKOxahCGqEB9m478ipmYrBUduuqjqn723ar70ZvIA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=qxCUeCvLoXnkVCcIZyB4vKSa7a93aqrox_MGZu5_Fek6lmYGJGt3jD4jA1aIiQWDkFuJ2QgaWMNpukE3GRS0xQoYoxBRtf-J65U4Og2hd1bOGhCt542PEf3p4ZVzQ1U6XAJnSyfv1HkROwcfWe3K3-rj6fTI13PJghrXs7dcAidmz1u82voT6sDuunT5D5nnMmtpm0Q0Yhdl1iaHDXZtD7oKPrgR4ol2UGMx3kvW5xSI6NhlhkexPjDHqgrg_l18PRvZc4qOEcrJjyDFXsX48GvUt7Pges8wO6euBXMxlDxfKOxahCGqEB9m478ipmYrBUduuqjqn723ar70ZvIA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23775" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Li6tRJjt3MCge3DFxPTwpQj7txjzjSLJWWKk5xZ1rK-FHshMR5ezNGdwykC5gPXwzjG-GtFmCVjFYb2GWPVko5gXPFbikplX8su7Kj4dFXOp4Zou3NYZlDzl3RjZZ4aRVozLNmAuS5tle9KbD-rTSctuqqcj1x6vHZ9Xderj5iCJYmYtmXAH_nyuZ4IVh9m4p-1x9fJ7O_gfIVGbe9E6FOMkOkQjPJBDa7R2o-wkkVzDNLBaJkljWR2J2puTTjZ2E-5N0pBtWAr7ZXOezGytVYlGvCrkRamGjlp60fFauwKbFjYrfjhfnploi2KOfJRRZ--Aj39Hf-1FvrGNySYazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23774" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVfVThXe_edIpdzNim4CDF9UzfBDCHRBG8M6iPF5olpZdMfBe8SaduVXE743K8lbHJCAxyMtJqsFxdN_QhwQgaDWIt9G-MrsVA3DBY9UDOGhiWKf9Cv100VN8MhZ_NqfnCIRjUWxOdvqY0dnBFd9F2VwkMTLNs9uBquaDa_z1HSy2c_HjHguAga9qr24k7hVbJpEhrwh0XitaY9EZmblVFuC5xai2eT4S4PmGkZDrkRUo3YTCbtC4oS_mSWvf530h6iJAQg9_zdV2p2kiIABdJ34CbvXUAzrpgMVtcdTA4gMSmEFMF2-899OBZJPPKs7iLpgaMRZ7qDTkq6WYP8bqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23773" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djT-BDUveaq5MtsNQ9LSYR9e-XYa7CyozfPYFPXALmsGWL4BL-a54j_3VuhJUo1VkedYqzG5Pc2UyFfJZ0bTANBplxWrUOn_nNr_j50DLHo1W3_TpOqVmlJtz_YjQB8IZhApijTYBFsoXwsHfzEycIo4UFF0bvcnMqSuV7VaCkTMSLvuedwhusUwOPZcxbhu-YbU5KYx90h4ygXiREwp74M8bxs6ZwIuQhPuJUaeDRqFrByzplGRdoHsLmrZBPJX8Y54GN_YJR7xWwgTU5o5QjXg8UM6ZKtIuq0rRDrwyDOJjh17rCsjVJN875qEkuLXYEYaBb3Jsu0r7uLqNdy7Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇧🇷
👤
برخلاف‌ صحبت‌های کادرپزشکی تیم ملی برزیل؛بااعلام‌‌کارلو آنجلوتی؛ نیمار جونیور فوق ستاره سلسائو دیدار حساس برابر مراکش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23772" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OksPRyG6AdF8EZD4IP2jo94-Z2Mx1SU3mzvbdcMDeCFmWmk5EjtswtQ72oZlQJc76JXQaflmoq6kJ3W-yP5H1A2TMsfm1jp98AO3LaX_6wayRVUCcEUc1Trh4q7TmeWSM-r8y2UFj0xOHJ3H9Gmhsn3KNiQ_sU5VU1THYZoSvC2-FkqlU4bV9a556crcPCD5B9YzQBDw8zzB1SBugkDqT-AEKdreomWxwNA7xWFdy6SqWfD2XpvWezpXviZtRWRX4pF3qRuXezqXxQGzBvimGMn6Uftp3PQKYNRLbbz1ceAIfyd4Wn74HSfYBpJbDReeOoMBpm-yNXAdhP10fEUOZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: ماتئوس فرناندز ستاره پرتغالی وستهم؛ منچستریونایتد رو به رئال ترجیج داده و به ژوزه مورینیو اعلام کرده که نمیتونه بیاد اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23771" target="_blank">📅 18:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkMHsCUqZ4SOoJenXtaYO5oUTECElB2yWF5ZdJwRrfbLPPHCKCZu2cYSEC_B7ot-XfKqH-jS_qMCa0VpE2NSp7mGN2uzsBJ1lR401iAK-RuXUeD11xU2e5CKsqAUcM6wwy-9HfOW42fv3gPZs2OlVE0X_Qc2cbIdSkkoK0hLBEluZ1xC1o0LlqE4msXjWaQEHgCSFWkYLZKynX0Xu4-qIwGFwzNxCudzNenSqo-LQLaaHH40F3ijCwGdU9D55p6zCGSqsjpQ6TBkJ3-fivrQnrwqHqE8uQ5ilteGzXcRy06zF1s3r2I1i4GaT5BmAD6Xp8p60lGQtHdTbSuNiQl--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23770" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2hU8hxz-OTy_loC2_80XINozm-xlbfoflKeP373BGq1BbuMbEytPCNdDfuF1GpkTrBLSyNDo-sy_25RZJp1xHaDn0WuiZaOmo8uevFvg8r9M2aw9ltn9wXRrC9wuJwjysqD954hELlzcKNbpdSsQtBa_CYIrfwoqabt0SHEjP4zWUfOcSZbQZft8B6nbDfH8xIDMW71cHs-3cvZUjRAa1o_jXIHjObNaixlF8zPXtoA0Q83jg4Jxpqxz31yDJvkGMPA7LzwpIbCHnEtm3v_FGg_y4r-Dt2ynshrj0tK_CJ-IHp2ReEWhxRjITAiegfCYDhHD7tcC-mqsnx5DqLvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#اصلاحیه؛ برنامه هفته‌دوم‌جام‌جهانی 2026؛ بازی ایران
🆚
بلژیک ساعت 22:30 برگزار میشود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23769" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=jXo1quXKYYaFTucHNTQ45-veiRAUEvMDwVYzvkYp0ffnj9f56y0Jg0QH4eyKoGni-ippR8WXSlKJQDvmux1edvOo-D7QPdFnrxElZ48tZtvQIjvXakGQSLsszV76QzdszxeGY6dQoxBpinsTNDtcSMVb0Bssancbg0-ZzVnwOT8SfNjAsrJaoXLb3Kd0oa9PeTRCjqLrBtDq0xGPL0KoqUqIY_QTDM3dR9M8uXT635yOyIhMrVZkls3KxHJogJWIobMzzstBPMgya0q2EFraHZV3Gf71E2iFrBWHIdHwhhWJkxsIu7AE_qW9gftn9pBz528FwPn5XvD6CM_Wdy-aZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=jXo1quXKYYaFTucHNTQ45-veiRAUEvMDwVYzvkYp0ffnj9f56y0Jg0QH4eyKoGni-ippR8WXSlKJQDvmux1edvOo-D7QPdFnrxElZ48tZtvQIjvXakGQSLsszV76QzdszxeGY6dQoxBpinsTNDtcSMVb0Bssancbg0-ZzVnwOT8SfNjAsrJaoXLb3Kd0oa9PeTRCjqLrBtDq0xGPL0KoqUqIY_QTDM3dR9M8uXT635yOyIhMrVZkls3KxHJogJWIobMzzstBPMgya0q2EFraHZV3Gf71E2iFrBWHIdHwhhWJkxsIu7AE_qW9gftn9pBz528FwPn5XvD6CM_Wdy-aZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌فتح‌الله‌زاده‌مدیرعامل‌سابق آبی‌ها به میثاقی در گفتگو باپیمان‌یوسفی: مواظب باش بعضیا صندلی نداشتن اومدن صندلی رییس رو صاحب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY6NUaZpESXHn9QiYnVNoZ6V-1LoDacxkZJhQUXm5QEZf8PENNH4Vj65GeM2VlQ_qx-Pr2FnP6JUJxFp51TUNhNnAR5TrKohFiCmMMYVCUX2yIMJ5KWzu3buA5ksGnZreKA9PEmgQOWXNgUkFfUx-PurYFiUj62ycbCoVIcMRCqOJoseYILCCbwTUIldrYYgBE1UVhWyMDVzM2YxoWXGQwC2pJWWUkCjUtbxpayWpy4-ME86zdWN4voun3rjfy2Ti15_BYs1zWh1FVfsCO5hNqRI2gz3eFTxKOzG1DYSnBWrq0EbtFB4l4sl4ntUgNfhsnB8c0tW0HmVNNIGoEcG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvNgW2NSl0sL4t9-3EQAF_vdIGEATCCH1W8d_YDd8h3MmPRCqo04v58u3OWQe3SL6Xa7ca8ilfGopPl1B-TNxakjLsVc1oqUzxRD_20F3nLftc1x8HbYwHEMw-EoOgPxcXAOU3g63I0RInKhgSfXXuxyVliVWS6qCI4Q9vhFw34xuXT6M6bPPIHTzIh6XQsEIAAbwdKAgRmm1zvP3Ii1lJQ_8EY5QQvTZIMl14MqFJKSWiyxnRl79IOB8RIj2BvdXh3LUTwjVVUex3z210av4_aDT911Bad91v28ZjyhXVvOY_AdnvVSy-kvnhrLtXINNpgsZjp94uKRUlO7Lfl0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEpTcfXReAPy5TmwehXqSBJFE927vjDEWkn9ZkqdsOzIYLH2RXjDltOjTS9xZUMPKkWKzmn2Ys8uOwYD2v7aod8qiLMpTeKgc1uhLjVF1JGfxo4qUiLN0JCac_eBqpBSeCJilTjRa7wL5Mt93sJPxEJVdC1dhGeJdwdmksHgZxD2H_J5ogP5u7yZ14Wdjz6QUEbTIC4FZDxRvcejMz4IhnbDs8haVHRu--HAM-h1MS1kHBYW5OoTicVBtW7WHENUTIyGVm-3yab7o2UPHI_AobijT6MhS86O9bQEdTlBIwwRUlrZXal_FPPeyFPa4txPy8vUacglTgfg8KH-5y7I5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cux0B7VzbPF7o7_NrQGkQKFSbfHMqgPP6Xds8u6xPtfa0XAJHVelTxSskPN2cO0VWzJ6yeaLmjOAlb6ZOVO4ZcfGsGnmcYoWyeX0xgPrSmzuwkuf8hT2gI_-3Dlnb22kRIjOINJbUkQ184WWOJnvBIjDqr6_I-efgkruJZTNzKTQvIUX2BJ_6Kl3-uSIaOaaODo0PxOphXd-Mphm2HudQOYPIhVZckm8jfq05dmmaKvncrgHFnT-h4QM0miWhYfPRaspAAXNNU_ksGk4go_8ZCAJ-Vp2nRaIUkmv2x8gkDCEPy9UPuqry99mxSQbxmx1h-4A0JdoIGtnwx5MByazNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-VqVJYf9msm3jyw3H8UxtZSEs60P7G5fUeL9WXao3dGTD-XQaCh7nX70VleK6pvkYXClxNG5pZ73qzEQ9f-fL_-B7Ax2F4h1wE8GUnjuKLBV9wngtpzc0fnh0u2iyIKKbMNAD7Q9WRWbzUQf50lfOpSUrX-jejU3Frv8S7AFToaFYHN6qxV0IQXcE85GmngpLqqlzmVRVVpCkOYjyGTpqosQu-HwrVOG_ys8yaQJFdlc-wBQhtvJDEsawIZoFI2k8GZNyIYCMPkt2HxJJz6y3ygKTTFXVakaEoYURuClZ6WO8PHjDDJ9jAGmBkgZHy-I1vZoicc-KzwxYqVNacppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23763" target="_blank">📅 16:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jR-RE_no82P3PUfmttlkLsk0YqCvqAUv__ZVV-BUtcg-XbK9p_4_Rwno53T1uiJeJsUAiCArZzdkNW3tuSncsSLg3CGxc7EIepKjul3eT46ALVOqDHpf9R50FhQC4fGzK2cThJreHoS5GxKInJwQvFH2FDxkOKIl_t_zfINm2KHqNRV3Vc8CLY0lx0WUGYdjWkQ3Cc1kC3GPJgyxDiiRqcx6dJVODF0yeWgS_cvlXQTFD5F2JWGHjE0qMkpEtWEEaZv5IvH-O01yKDDfcEANPti6-UgCDVNuR-RddiE6qZVlf2EAPJi6dUXsr1nSA04w9SgCf1rWaojaVa55LkTahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اطلاعات به دست آمده پرشیانا؛ باشگاه روبین‌کازان‌روسیه به ایجنت ایرانی که ارتباط خوبی با او دارند اعلام‌کرده برای‌صدور رضایت نامه نظمی گریپشی ستاره آلبانیایی 2 میلیون یورو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23762" target="_blank">📅 16:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIUzWbxvZvWSZUA0LyF2bi4UPIGlRBKM7YVxqb8LMW-21a4AfOO3zPNVwsGyZCiduel7Bas7J-Gz6nDVEWf95UVIXxRlfGsKmLrHi4yk-kFTVlWWiGe38Fb2hEWH6NQsRlyZu2G4VxI711rItH1WbMnBmEAHQTyWHTQakGClPZbcmI70IVoUQ-PEeo_i-oTN3FMBRWLeUyD137xyRaEk_Iii1nzq3qBeVQHMRWVko_lA4WeupiN5xJ3Qy0tPgixZKHkGRXjdXjjYk46C2KU3Z95_OcHILNMCqh5IW7YdSXSe5zeSqFp_dNoPNFrt63jOzn3muyv6_8AxCWxsePG2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل دیدارهای هفته دوم رقابت‌های جام جهانی؛ این پست رو فعلا یه جایی سیو کن و بفرس برای رفقات که تایم دقیق مسابقات رو بدونند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23761" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEjlCh_JhY1ucgM_mhsB9zkzZLTmluSsoUPfE5rPlNv878ohluX5Y_6IcNeZrl-F4hEfn97wWLbMhy6NRSanUx8b8xsu4oOHXxzYJ0y2TftzardGEXLJJm7v4za2A3R4UUjkQy1FJZD36VbvJfHCcVy5E8E5U-nuJQAVOXTxn3mVBZQCm3sHKQM_K1jVajgq-9T-T4HXU8nZUUTxHv3OFnmQ9VWGZ7Pf0GtlsmH6t75gxuok_DMQkCvTtDDoMvlQSSmwOjp2Y78aFiJE3-uILeCArWU58QZ7eGR--pB_6_HWS1ZP89Nyqm5tr3pxpammCwcH64Xc0BONYXqbWTMZsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نشریه ESPN به نقل از مارک کوکوریا مدافع جدید رئال‌مادرید: انزو فرناندز به شدت علاقمند به پیوستن به رئال مادریده و فکر کنم در این تابستون این‌انتقال رسمی میشه و انزو به رئال خواهد آمد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23760" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAj8QDO5ogGYTIvkcvI3daLuKgKKfgui289A3j1FpeBfsinRaQZQy48lazHr-bb3shJHi6rBsVEwBax2qRCNzvxKu4TgS7mzF5KaIay-hF-WTNEhf9VcR2TMlq-D40I5AihNiXh61OUc2cuhbiaPgZpUxVD2b--7cqGakXkpkzv_HP8k2n392iJ2SSBUcHcV_Ls4BTwS573vnLqn3trsBNJ5LoDcLRyrGMdBmZb9h7sMK96yIih2dWo9dUJ_8Rdf7zuXrTPm6WBjI3-7qUgh91ZVRlLT8aQ1q97ILP-BFUXAuDXhpsimr-HEYEXaFYXsd9qwk7ZKqV1bEWcRLVHasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
🇦🇷
#فوری؛ باشگاه‌رئال‌مادرید برای عقد قرار دادی شش ساله با انزو فرناندز ستاره 25 ساله چلسی به توافق کامل رسید و حالا تنها توافق بین دو باشگاه باقی مانده است که این انتقال رسما انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23759" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=XT1rmCSQoIBdRBpcjAA99Rpt7plX1TT2FX1G1JoRc5aEjCFAM4d6a7FHg5inXUcHZZt2ibekMxtJnLqDWeN8CHhJKJ_EJ60qg54f0BYRhYVsCzkF7lcAfojMjyei_nAdZlihy9AsteyOtkZLiCAyU-95ubO_puLrxOmbbKQWndVpSepyxZ82g_rlPK4mfE84ftObSWBsDt2cQIYFKxrQwn1PqZuBbqZAF2uO6eif8MRruem01od12ww8IM04ICHYJcKlR1nviuxkKf_oWYXpPTyUspSvpp4LffUU-fGkFnstzODE1-w82m8Baq1GbesS7YWJj1NSMgWx19G_LrgmMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=XT1rmCSQoIBdRBpcjAA99Rpt7plX1TT2FX1G1JoRc5aEjCFAM4d6a7FHg5inXUcHZZt2ibekMxtJnLqDWeN8CHhJKJ_EJ60qg54f0BYRhYVsCzkF7lcAfojMjyei_nAdZlihy9AsteyOtkZLiCAyU-95ubO_puLrxOmbbKQWndVpSepyxZ82g_rlPK4mfE84ftObSWBsDt2cQIYFKxrQwn1PqZuBbqZAF2uO6eif8MRruem01od12ww8IM04ICHYJcKlR1nviuxkKf_oWYXpPTyUspSvpp4LffUU-fGkFnstzODE1-w82m8Baq1GbesS7YWJj1NSMgWx19G_LrgmMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
آندره آ استراماچونی سرمربی سابق اینتر میلان و استقلال درگفتگوبا DAZN ایتالیا از محمد محبی حمایت کرد و اعلام کرد شادی بعد گل او رو پیش‌تر از بسیاری از بازیکنان حرفه‌ای فوتبال دیده‌ و معنی خاصی نداشته و فقط یک شادی بعد گل ساده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23758" target="_blank">📅 14:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY4ofU_eRkI_6ONAex4-Uf3kdG-PTCCumHaaxwJ__pTZG663t4_YUuD0uEBYg_vkfIegzQx7QhztKD_NCH7wupqlj6uSJM89k6jbWwU5OTsxDg3qTSvqqXVLyO4rzDD391qU1kTyDSIIjceXom4VrL0kMr5269jK6eExBKP2iwl5atoX3-W4e7U-X96Sv10WEEUbu_rL3M4333kDOegmeqDt9fqrhGNuLigIBo7pksEVrAVSx65GPNVFfuM2qwyiCA-fYUuUG_Ux8VOr_cCOf7sAKCw8fnwu656f04l6wi75etsmf5JXpDl5s-aijQa-lPENziQHpSOmeP9he_r7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvNpl75f8wlsfMZwAkrDqmlcQiHOplb-mD1zAR2IXls1Bf3mlSZUCBR51hPQzUI-c2xQJxKeaKrjpFF90jtIA-FdRV75PBNUMdUwIRiIoCwyUmzNZ-hdkNJkq7MrHuzNxEqGvco3xIjPxcpAEIt5Jg50b3hzwPWqsWVf2s5IWNcEhDz9Ho_VjK5pPV3I9_B5S4736TwYwDsPu097sFUix7rxwzm3WYxUlXjVW7_usQwbKf6vAzc97fXMrml74HnmotXyo8MKXoYYG9JVL39ZuJk3ick95QK4_a78q8VIaiuD0YNcKxeSRS5SK5-F4iEYrVaUy6qhb3MLcTNYc1NuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSd5xHMfdwO4amc3kbcQD1p99J-wXrnQtJdl1pNvCOuImJ3ZttJ-uSsl7-IQYBTV2pB6ntCk55bDOqwtCeYBXW4k6_XZOeTM-TJv3cgBY90NK1CpBisfVZlS1LPbCnsFPkX5BLcU1SX5UfgdLkZ0h54O87V4L5DHNVK2L6U38MA-Ikg-1gPraqoCNClEiRx0t3JI8HnZQfzmNDkX8arJAlRzjpQf7dyJdYZT-JVHwgGfgnP2ey-2cxXgWlBxUjNE_WK4-j8CUIVlQ-FkdAr1O88Z3KdoSIujkneArgCWAGKpMGfgnwlFhOsoVutrHzDBNuJ-EfUMUkSAu9SFtbmE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE6Jk-DfeKTf81hEdLz_hLlVFFuE_BzbSOlVgi7GAAGyvw331RBYVYavzZYLrD9_MFAp0CahvwN2Ez2HckHFsgtKw_KHrKSByAcpOXZDXfuT4KdHNb24VVwroZcx7dWHwiv0KpWcow7ThTKmZABPOOMdBGMHiWysU8i6SJY7XEQxRDvxJkkL9h2_QVZJWDgB7rbSWtSO_b1Te6UkFC1XiEUdW_LIa6lvawqLZMFh00PmDu2_5lZbZLeZUwPk2cfCFBmjA7iSaSaVY8wJMfXwNd90C5MqLIMpY3ZU1qWUezoPlFPvu9Wri6MKvLjPLqXjJzMmb3J-dTxP7FCIw0J7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KimHzIpuj7qtU527vVXSxZo9UBSJ5GVvU-nNQIJcNDqipyxzsGJNWC3ubg9yLgyjka8wS3unqCLcHiZlSHSEcMP3J9DT1aUqEeRFDyY1Mq3m94uf7sExAO5Fw0qFXJXpXeH93sCAWIo99x5fbp4yrYiGNfHr354io7Ue0dDEwBC4rbmA7lWiATpdGdCuc-zBDT2zyxI7pKGoks9qvl67eJ6rmsRTD1KS71WV_z8LMmEu8ElCa7pkvGojxsBfROz2eytUY4N8VthlUUkDG6j4-Xkeg-AfCNw_dJMeTIfVRl1kK8j0umd51BhwnGjGiAO2LJ8KSJaNC9RgrETJpkRTZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5J5zGrJa1R8ezqMniBPnTNCsw-ES6CenGzothSCAnw-8RI3HWgmZ1mwidjBGIAtHWS26usEOGhXLE8R4ozu6EaJkgoYoJzjcC7gooNEFBMAHKjBLbdBjaGfd_dPkIuzupEe0nGzxr1NCNCvOBEvvzN2hi4_Z9MQpniey6zumLBHfE10xFj1Gs-cRXioO1wqHbQnUfd_54YebIU6qi8Xjodq0ikkzBz5gTTuiQyagYcG2zg92tm2lYWSnWVQsggUf_x-TqkFpxUF9ZGG8tjlbZ07z9dMIqISxdkdRLlPxXJXEjv1v-fZRLe3LfscPjeO863rojGOE-ltPaOp3UEj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=LPUCtpY1xtw-ePDqjYGZW11oo1LZ0gFoPDi0CD4MrI_TnmQoLsCJEY2oXxetbKhsl74T5Eq6Cm5SayMkEeqXx1eXN6yBZHm0cZK4Zexn3VAQNzZjrZ10yP6BdhDyxGjxGohVQq8ADOW2vC9Wtp84dFeiox-Je7GDvphUxgMfqiuoswBY99N6Xy9hfXEfzkuKgIq2jTSsouInczUXew2foM0LHcvIwt2OSpaBlOSkzt06J8alp9imYuRtDMRd0JYdO1sgX1lqxOCW7etLKHnQLBzOvEEtBcpHxUghdsQ8XQlyd_rewbl-Z1jv9T0VK10ToU9HVTRE6ItWHCs0pQ1zyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=LPUCtpY1xtw-ePDqjYGZW11oo1LZ0gFoPDi0CD4MrI_TnmQoLsCJEY2oXxetbKhsl74T5Eq6Cm5SayMkEeqXx1eXN6yBZHm0cZK4Zexn3VAQNzZjrZ10yP6BdhDyxGjxGohVQq8ADOW2vC9Wtp84dFeiox-Je7GDvphUxgMfqiuoswBY99N6Xy9hfXEfzkuKgIq2jTSsouInczUXew2foM0LHcvIwt2OSpaBlOSkzt06J8alp9imYuRtDMRd0JYdO1sgX1lqxOCW7etLKHnQLBzOvEEtBcpHxUghdsQ8XQlyd_rewbl-Z1jv9T0VK10ToU9HVTRE6ItWHCs0pQ1zyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جذاب‌ترین‌بخش‌های‌گفتگواخیرامیرحسین قیاسی با مرتضی‌پورعلی‌گنجی‌وپیروزقربانی دو مدافع میانی فعلی و سابق پرسپولیس و استقلال؛ عالیه ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkjgD0V25jXHoNr3_GCvlKkkl1F1qsGK3lXY_z6oHf8Lgd255BPefjIjP3x6x5NmDgEamsXLsO1Jly7OQHtqF1SGeCTBEPN8bb_hVpmRw35LLR9GOjJ_27rqMB8i0QbJuaqYIsM3m2GJuUNDPdWJQkisyqlOf6pKuLBxWY2Zo8-wO3i_F54mkv-Rb3M4Ern-dzToPMySyE5WblBykaEqs_VoFeAeiCvCCDB1G9IcodzOVNUjSeKCTL9vRSeQGqxHGb9hAjrU-UK99USsHO8jObclgObqEiXOx5BUKaiE4wB2vd6EnTIBHdA8Bhm8W5OxrNzYAxhqZFVRPCcZdVU7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KguScq1CrpLFvIxuZzjM6FLrghKR-68j8OaikwNMUdIH5vcBmkf1n6Eda2VeER5CLOFY46kreFzCUbL91e06stMz06ypl7TcTVTgZkLDqLcFkFUi31cYATgYOMt3Rf5sgvJFcLrlBK9Vd1tvNhhUUd0avsWQe0f9mUxC00rQSlQTih4fXoCDfMcsa9Mp1-Aej9-28pUE0j1rF3NIe46NsqqxVgvpMpbwm2WasuWHRxV9ZjM6Au10JCOCI8lT8u8JYIuyOqR3iOkCTSpZs8gbfCTX1wy_-wTVrhOKXs_nORyZCJowzp7YqLAulB3Fc0aySDtqGeMx_CllSDE4UYuSRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
📊
مقایسه عملکرد آنتونیو گوردون
🆚
مارکوس رشفورد درفصل‌گذشته رقابت‌ها؛ باشگاه بارسا بالایی رو جذب کرد اما پایینی رو پس داد به منچستر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHh3DFZew6X71sT7Dl2g1L_O2cHbB40InTF23NrME2x2LArrFZ0PFl02OEj0BldLi-cY-xzc61YV33QjhCYzuulsdAqRgQCxG3Hw819pOl8Lpdkfios6oTK1wN2uYa9j3OmTEDj8qAxYfFyXgNF6YYJF9MHjCD-ViLGHzD-vV3nmJVfLw29S2VqllM6QeB8g7tbFoSRcvi1pZ6nNBixaSvEa6ZDf5ztvOnk20HzBHrMEpd5neZVyybpOW7yfPzX3q3mAkP8lx_B4_MywpIuAoJD7wODmZBaR-LBP7wH7RmZN4ZmAK4y8HH8058578eyC49v6Du6gt70xlBW6nM4-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=ipmWg--HVMz3Q9qahBTim_T9d-7_TPVICv5a2-jYGWAqZIPGpEa7bz_8U0auODCc_p5QipFsVEZlwLDPCsFUwq8ZR6HLbWB5lOmeVe-KBZ97s2cIuYTh0ULbzYxUplM5kVoan7Fy4mVtGn0nV-sWK4Yvgmxr-Me0koZSz46wxjBkmpdsGQ6-9wiQvrSHL4V3nQpV5S3Gd2NCoCkwVhLEQ9t94_fgMppYILNAgVxwWGocxw56qitwVnwfr54t5uxbUDQ_cyC_IwAPWTkqSADJTr8ckZbgKGJPu-SOd9PH6BBwOMP2PHLoekUqiL-szJg_b8-XVacLjAfqlECKzYHYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=ipmWg--HVMz3Q9qahBTim_T9d-7_TPVICv5a2-jYGWAqZIPGpEa7bz_8U0auODCc_p5QipFsVEZlwLDPCsFUwq8ZR6HLbWB5lOmeVe-KBZ97s2cIuYTh0ULbzYxUplM5kVoan7Fy4mVtGn0nV-sWK4Yvgmxr-Me0koZSz46wxjBkmpdsGQ6-9wiQvrSHL4V3nQpV5S3Gd2NCoCkwVhLEQ9t94_fgMppYILNAgVxwWGocxw56qitwVnwfr54t5uxbUDQ_cyC_IwAPWTkqSADJTr8ckZbgKGJPu-SOd9PH6BBwOMP2PHLoekUqiL-szJg_b8-XVacLjAfqlECKzYHYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL4gRpYB8WS5RqIq-DWLa8dxFsIg-glPPyrxe1XRt-OHwFZqlacZjmP4BTDXGWHvUTB4Jl59w4MW0OCBACoLD2JM7H9rweqCaeHG0FwJwD6RtRL_kRtO87MewlZprVVKlwkFjucIlS9_sh9t8zqTq7BFFxWpxjOIVyEpq2A4bKiLkGEta5Kjld3XN_GCthZwcBC3GczuN8wlvJo1opKUGh1e32HmdnfSYnNy1nr3bcFTJvtfvNgGHnEaK48YKBIIN3p08xhkyx53Fvpkm61Vuhm1pbaULRWfYhLayt6WpDG9W1_bsoJFbJMCUKoymsUbthUcmu06EBLgN_JL6BbTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrmCEka8UovM_c2l1PHV-Q6sUjQatlQT00Zxf9dPf1VJ-LnmTv7833jHHI3g3Eic_ETBftRWpNxuzrmccNfM5ugwoXxHKYEzeKhb5NFe5AKRdtg5xV7uw5iN4wjiadA5Po1GfK_SI-F-Nn_JvZXpEp0yaAI6QWsjKeVk8-78yjVFp_OOyLS2KnAxHZDnAuzep9bNxch2VBjZXpEOgugEiPZNdAWWnobN9-IxvDoeXyLJgmW8nksPjj6P4koXO5Fj_Lr4sJI5iYBf8PXhdLZFPgX0EcikfTvJ_afb2BGu0obrH2-jbkEhW2ww6h-3pe1e23nU92yEQCiyoBL5P5CnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23745" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPsX4uoY7ISr5rX50c32p5-Y53UsRo2cpxp49qpxXYWyJ3yqirEooBaVcQZ6aCB5XfyFPsHxKoTWvo0LrjjrIMa5VjtAjFpzWO9kddVkf6hly6W8X4PCXfhXPVEssKoVu3avdMgLlF8UsFJUAaM39Z9x2ifm4BNwlB0uCNhn5Pxo5qLLMdS419GKATQRop6A04MWkTwwA6bWY5hRGVjI6N4cPJhcN-R1AZfIXh3HVqqesQrc3pMygy8gTGD0yk4nE_HT6ve4LHDq3UPBg-d0YfudYSJtuGRnszU5XTa3FhL3RAzrjs9NgAU0rHYd7rUZjaqHnzv5WlOgIDHG4ys7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23744" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">▶️
قسمت‌‌‌هفتم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23743" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=iXiBhq7sMTpyzkzHZ-D8kIUNOZX-gJBzjHUO450OV6QYy70eNa9-0GJ4QYNZYs0LKr_a7-55PVdEm7Tcz5wyn-yZay-0KxqAD_u3Isawm4EtIKy8VQ00bTnX7kfyUBUgVcK-h4B4ZyxMVEsdCYf7JlroX1N27VfG_Z-HctjdwE3gq6D_q51PXQNr0JSJsvey30BanDxyWPYmVwRHGiEyG7FQIr8Q_o5Gefzr7_ZIFbaqZlsZs98D8RHijtpjmaIOpXA8TgIgFSkYfWxOHBZi7bBoHMG_1ctamCCL828swGu7TSadVd8U9XM_KScLJr_znbrAYeaIveM-n1L6jYsaqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=iXiBhq7sMTpyzkzHZ-D8kIUNOZX-gJBzjHUO450OV6QYy70eNa9-0GJ4QYNZYs0LKr_a7-55PVdEm7Tcz5wyn-yZay-0KxqAD_u3Isawm4EtIKy8VQ00bTnX7kfyUBUgVcK-h4B4ZyxMVEsdCYf7JlroX1N27VfG_Z-HctjdwE3gq6D_q51PXQNr0JSJsvey30BanDxyWPYmVwRHGiEyG7FQIr8Q_o5Gefzr7_ZIFbaqZlsZs98D8RHijtpjmaIOpXA8TgIgFSkYfWxOHBZi7bBoHMG_1ctamCCL828swGu7TSadVd8U9XM_KScLJr_znbrAYeaIveM-n1L6jYsaqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
واکنش‌لیونل‌اسکالونی سرمربی تیم‌ملی آرژانتین به‌سوپرگل لیونل مسی در بازی مقابل الجزایری‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23742" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzdU_JoFv0TcvMGT5V0mKCXmUg3NSB7yx7m6-okL1SZ7nJZ7xoVNfStI9eIcl16owPIZCshj0npzHOPAsvNupRXdfF_G4DiBrKmriK1Dp6tgk2E79en6riRD4YMcpIszT4j6mSdg5A9Izdt7iXVmmhddGNYja6u2fwlElCP9jo201GPQHibd01n0kTFIqQ1kfQDzQVZYIwjimwCjQ_4lQQTHH109mLFm0j7egUvdc9dtVmz7sc4xx-4vwHG4B1nAp51jUb1HZoKN2o8CkkUenR3BpoI9Eqf4qTB1x0nmMtkvwBS2A-P_rY5Mu3zm_J8Ort3rMYoGR_TGak-AIMzq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23741" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRPuWK6PN9hlBku8mUTHzC1NomrOhsyZH-JdOj0fVUJP0GZ_6PAPWIT5SJu8K-iP2-AjU_7iEe9Os90hW60rvf6bCR5s6AByOdx2MPqs6fEwKg6cC9YsCID90qFiuc5WzZeuKKq6YFc_R7bHA3n5rL_ujZXczG2Bts_jyMvFDWF2-J_PIhm4YCMEBFsRTEMqDHessgt4fkAUvfkLX7tqP1jAoWVq6xKW3ee0cDBXetzVQOMjVFHXBRnJqwc3Wqrl8Pl0ZiXkM7lntYfc0_qCJOvrwkz83nSVOiAFXUshuR2l6L_Ti3UOAXd-mIXD7mYDlICnIsgK3P_Zc4bh8cxW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23740" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlMezIJCLnOxebN9U0WuhFWAzqadmGNkMypb8dTdWnY4DZYSv3LWjYuXzvG_loaaoWFSkUQMKcQk8Ocv4XQ3tbCFX_HMnFvGzi_uzkKyKGdZoS-W8L5Q1IpASA3nEVpYZ2SnZv1Kn621Akq3k6QWqHTdoJm2cq4UZAM9BP5pIUxv9qLon_3mpr2psNaIgQNnq8vuDBOKG3Xxvs5FKBbBG18iFNRo1TxaBuNtWecmVNp1VkULLgrYq9L1l_oi-uEsdBcnk7FwKEiZEkSSBkFeVSdPcO9QYgzkEf8pL9M8yhGYg2pcJnK8CPYmchg5US9LsqPCITyBulBLg9e6RhZrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مدیران‌بانک‌شهربرای‌عقدقرارداد دو ساله باایجنت‌اسکوچیچ‌به‌توافق‌اولیه‌رسیده‌اند و درصورتی که هرچه زودتر با اوسمار ویرا فسخ کنند اسکوچیچ برای انجام مذاکرات نهایی به ایران خواهد امد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23738" target="_blank">📅 09:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=V1YVg-YGmfFMD4idNqHT71eJZ-fBGWY06d6by9ISm3UmFHAFVNJI0RbLojz8GetL71zKewybKtnfpf-XeZgBxDOD2uJB6tJpVnJh5svNu2aZsJmBiUaGZdsU5tP3qHXHavawKvkrFtAzmP1Tgc8wDJ56fVRi1ABnmo06GASpa6reEHUuG_dwXAHjjsLPP3uE08m3Ja3FzcFE99UmgJ5hdZDsPtbn-L1eBwqY3XQXTf9EBDXWiUz3XgbDMbCUZxpiDtcFjJU5FvfGhjqcHb6QSvWLDjBe_kipK8rQTB7NY-omkiG_sI-jkpEbWnhwoVnE6CLRbTiexdFIfu8Isl5cqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=V1YVg-YGmfFMD4idNqHT71eJZ-fBGWY06d6by9ISm3UmFHAFVNJI0RbLojz8GetL71zKewybKtnfpf-XeZgBxDOD2uJB6tJpVnJh5svNu2aZsJmBiUaGZdsU5tP3qHXHavawKvkrFtAzmP1Tgc8wDJ56fVRi1ABnmo06GASpa6reEHUuG_dwXAHjjsLPP3uE08m3Ja3FzcFE99UmgJ5hdZDsPtbn-L1eBwqY3XQXTf9EBDXWiUz3XgbDMbCUZxpiDtcFjJU5FvfGhjqcHb6QSvWLDjBe_kipK8rQTB7NY-omkiG_sI-jkpEbWnhwoVnE6CLRbTiexdFIfu8Isl5cqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌داغ‌وسنگین پیروز قربانی سرمربی فجر سپاسی خطاب به حسین میثاقی مجری صداسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23737" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=F4Mm1xD3ioDySpvsuO3NqMF9YKBVnd-4sMizv981-ji3LyzCG2Gnk_bTiLwrjMaLas9Mrl7LjK4wSdlN4KZwkNA24Vs0RA3ewPmf0JGyiczbtuvTrqWkmTV-4Hg_41xpS2kCNRjaLTs5kllZafcQEKgj98uXdYSMVl4ScGeH1sgFIDfOLKLSqWpkz4YJuiyJyCe7akYEYnXGNYxQFbOvpX4EKFqkM6SnhOSteaZaddKQb59o9h7Hrx1GhK2vPv2sPHPUu26k0s7hJbAqtaoAShsFHoAHCW7-UR5i6LO3V9bMCLwuISewFtBPWG85UOGAYaIs6WRtH0yDqab77fmtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=F4Mm1xD3ioDySpvsuO3NqMF9YKBVnd-4sMizv981-ji3LyzCG2Gnk_bTiLwrjMaLas9Mrl7LjK4wSdlN4KZwkNA24Vs0RA3ewPmf0JGyiczbtuvTrqWkmTV-4Hg_41xpS2kCNRjaLTs5kllZafcQEKgj98uXdYSMVl4ScGeH1sgFIDfOLKLSqWpkz4YJuiyJyCe7akYEYnXGNYxQFbOvpX4EKFqkM6SnhOSteaZaddKQb59o9h7Hrx1GhK2vPv2sPHPUu26k0s7hJbAqtaoAShsFHoAHCW7-UR5i6LO3V9bMCLwuISewFtBPWG85UOGAYaIs6WRtH0yDqab77fmtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر انوشه باتریلی‌از روی ابوطالب رد شد؛
تو عمرش اینقدرسنگین‌دیس‌نشده‌بود. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23736" target="_blank">📅 09:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7467784054.mp4?token=cf2nmcbC8wLEDN_b9PvM8XMsr-4GugVhmY5vC08LGrTtP7h806w7UCK3C8vJvWHxj50WlQo2FygxcuD4MHw4-iJaghzo-Zn_S7ei1L-5PSnLX25nSeprws5mK21PaBK2MNVMcHkncvFTZFjejwYDKzzoWHFn__TJJ75ZWI0eI2Xu9oRSEmY73zBUIqvjc1t2CX0v1HrRG0Inu7vsUaWYeViScuaXjIIYr36gOP6BILVbhgTnVUzbegMx4u4nSWUTnEfpq_09emywCq2s9hkiiObuZndkaOj4PvquRQpN87Hp7IvLahzcp0pPI1GCR7ZXnCD_aCjtLSCxfbhy7NtXnxk852rKqCwkzSQ_8R3fBmNxx2VNrB9H2k4KhMpow6GFC3pBfOZ1gCHpGapje0yjT7r0BiFK5SgJfcXB8RALSmETNqGCX5sGOEmykyYCIRoivw5gQuKs_RKJCwQSFzq-vI59c5qS3MDNVHA5Fx8v_0NaYfnjooje3NJOro03jt2jSFwyQbD0m_aNZL9DfQ8QMqvZDlkupnFJExryuFhBJ_RffCVxQDqk5eu7jMflSO7WJX9H8Ea2s7uzJpZlWw3PuPvZQx6X1MWbn7JhQ4UDITpjYocKy8g6VZmoaAQzx0T16KoplXDHQTXkbcZ9Svh84krMBFnVQqeXtLuaLW7Txoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7467784054.mp4?token=cf2nmcbC8wLEDN_b9PvM8XMsr-4GugVhmY5vC08LGrTtP7h806w7UCK3C8vJvWHxj50WlQo2FygxcuD4MHw4-iJaghzo-Zn_S7ei1L-5PSnLX25nSeprws5mK21PaBK2MNVMcHkncvFTZFjejwYDKzzoWHFn__TJJ75ZWI0eI2Xu9oRSEmY73zBUIqvjc1t2CX0v1HrRG0Inu7vsUaWYeViScuaXjIIYr36gOP6BILVbhgTnVUzbegMx4u4nSWUTnEfpq_09emywCq2s9hkiiObuZndkaOj4PvquRQpN87Hp7IvLahzcp0pPI1GCR7ZXnCD_aCjtLSCxfbhy7NtXnxk852rKqCwkzSQ_8R3fBmNxx2VNrB9H2k4KhMpow6GFC3pBfOZ1gCHpGapje0yjT7r0BiFK5SgJfcXB8RALSmETNqGCX5sGOEmykyYCIRoivw5gQuKs_RKJCwQSFzq-vI59c5qS3MDNVHA5Fx8v_0NaYfnjooje3NJOro03jt2jSFwyQbD0m_aNZL9DfQ8QMqvZDlkupnFJExryuFhBJ_RffCVxQDqk5eu7jMflSO7WJX9H8Ea2s7uzJpZlWw3PuPvZQx6X1MWbn7JhQ4UDITpjYocKy8g6VZmoaAQzx0T16KoplXDHQTXkbcZ9Svh84krMBFnVQqeXtLuaLW7Txoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
10 گل‌برتر هفته‌اول‌رقابت‌های‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23735" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23734" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5_z215n4-rYSawPqBf50IrcFC2anfxRedF3lXe0MOQLZYHJ6fzyGZu6uH4VnVuT1HyMLXXD8GcTS7S2t8a6pDyeMahMI3yC4JUxJRJkta2JY4Nk3cnWTdi1S-JsXn0OxMCa7wWzO70MNtVVhHCdVnL191znAAxv_MUrr08ZnC33sf_6stVqBI3PmqJK-8Z9CeD-qi5zPvJk63NATLJPchW-ncxWIwx9lK1OgjHoLJPxhitt5M8JgWKzUEp6wQZQP0VnDZdLC-C5Rxn4oYnScq9sSAwtmNquPTX0VCdlsiJi9eOGf6lobVSyAsFFFtGgXwN7YN8PNyLPqqsG3s1W5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23733" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZavR8RD6q3dHAYaCqhAeHapUX4H3pXjmP-yzvFj9SJxfVwng-KUgwpNd_KSyEwatwQRoFku3bNSvhRsQJdxfjPMzd-E5vdsXH5UxrZvJKNYmj1uQbLunxix9JL3ENF0udJjO5TYJDQF5rUlq8-prOz_wo9e-TSvjl4nF8HSA76Xfba5kgcorfQIvIpiNEQaTsydXCwVDvc75diIVJ27GdhJklt3bYt-9I4hu0G4P7ipPK3Tq6LUpFb5HUm09HrMoVn8fL8g_9Of-4lR0FmL44VSjzTIiPCJ8-LncCs_bAY67DXO75JChj0mXTgK-_Ns8cIGKuo7F2joM9xokcuoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23732" target="_blank">📅 08:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4jklau7yluQq3mlOFO_zlVlTxKw0hkBxijHfvU6iSDcVL0K0KGeIKmAazdzxTZgBGCqFki8lGFO0phwyLhW9TT0HxtHQ-sbmrfYnxGIoELSKbtXoPwAHLmycv5KJ8Fa8iGqVs-2VYDWhsylt0ne5sfy2riWUbSVpU69g07kANwCpw9Vw9GKb7MK69TOAJmWRriykbCZnkD_RQ8QA-aRQbwkicFkud21dHNRxQmOGjVPpqOv6wADTuAKKh1o60vodRXSQB0c2wtLVMD4gSTG-rFV13fTNsn5WTpIZIyudetiPuernuFeNfRWZ9K0SsKox5SjhSbOdQQZYayqYafm5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibao9lcdUbez6U_1YSdvkz2qBTuLN1Dk5yNsQBbDa1PKwDCqalTK5KsNEdkDnfPgSEHvH68jduCA5IGP5OF8kZ6-8uon3YXYhXtIn_tZdqMeX7s8RMbF5edyWmSq1uYLZt8h406v7T5t5BCjnu6Ciu0dp-GHeUFJuoQrsHmjWZhye0iffbjIXGggLQEQDYjU8qQXZjF2nH_OmjctU69skofiaXYID_WULQW9orHpuBOLc0KwMmVsE8svoGy5ZZsOJWgA2GAWMnS0G7QUZv2eb7pOY9s09ia3pX-pRv0CoK5tVGQ75hNuqMp8hRZEVrhgsS607srAyXzgIq1OW4QK6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23730" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcP020Mt_Hfw2A-PH2MUwwXcvIgl3PEFPzM0F4KTg40Xi_I7kmNf6Qdo7PqKnQ702JpxTcmyx7DmUp12T8L79HQgiU2ywprn19nUv74q5bMEeVKxoNYAvrFf5x4mhMZKoOGDeaEYQMqtzZXB0B8MAJl2rcXigGS2qgC3wtCeO4mDnJiDcMawx15bwB8jSGXmsybbZT3OFGJCNKR_W9Kzf0mvngbTGE-TpJZ7dsShBa0Gag5Fr80bl5ThKZaBHJNk26vjAaTCcI31mzKAPcgSI5biTwviDYQg_i-WvsqvcSYi7IsigmurjpNDta8RA5bXM_Ux476MfQAIbeKAovvPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23727" target="_blank">📅 02:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUV-MEubBM25px-6YNxZFmb5ftjrvNGejT0RxY6oUOU9uc7mBlokQuANUQfuwZEH9iY47iwjE7T2z68UsoiZq35ZO9osHAylvNobteeaWU_aRTn5zr1odQhABMiHqxrySOBCiXetnpbkoWvW9FFek3UsANKG-YRRT7yZE74cnouax2a0EXwhbYwOP0wPi1vEy1SizYNoU5sXOf6mGlZs705siyR4lghD85kHPtf5oulkMUDp9JJkZziHUHoWgsHRbmTf3YJMX4tKUFJ29StDchCWWvqkOrPBJX_cOIA-MQ1SwNJqfYu3BG3q2irk5zxGhTUIIbrjfpnPIWcELcvOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyo1jScc7IIzbnO3hjvEs3HGtc3H047F1QS3IiNa0UtoYRfeFql3_sd0AyJufi6qid_x7ph3894UWdiP1LnDOLsPKligzGVlnC_nuthoPgJ0Ud38FBLIcSPJDaLjADiZUt0wcRn7pG_whQqkB2chDqPtZQ6k_zHpLH2H6oiXO-xtKZ5UVml8hrMKhADJIJR5rzuIbfibYDVkHzQtkWTM0oVJPV-4U01Fz_9e7QT7X1iqVuMEiHOMZMoHiP3zSQ75bLxB2BmQk0xPeZEOkH7pvK3qfyixF8vZ-AANXL4FVet0t5syaq67KJK5Sl416djV6YnCTpyy8asRTm6X8fSQIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
