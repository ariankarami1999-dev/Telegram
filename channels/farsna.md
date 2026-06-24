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
<img src="https://cdn4.telesco.pe/file/PHTd81e0rJiS0rXjwkceDNqMOFRh0KxCOibq-MqnJoFX-brIVRgCYyqXhn8Libw4eWjvUyqsmoYV3O2GYZEseY7zxTJmf9voCtFPSKkJ3u1HJBkLGViPY4Lxgzd6520_7wjOB_dA12rW05s63cmjUM73YuE8bxgZZPdm-AFkGKpoGazUDU3XFvvZkK--H7g7A8-z6I83kNG7CmVoIF4U-wmtulQ_kbZhrE0xHJfTECf5KRu41OfZBNQqKr8TBE6HnHUkmLheEi_QodHGETRuhhsU6MxiOAjfIejsPjWimtLPvIN0vdcWYD_p7gow-F_6I_PZUI9rIg2eUBNWUWqj8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 09:59:19</div>
<hr>

<div class="tg-post" id="msg-444440">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISQnIChJ1DHI8W67V_Nx28nSk4O7ZUTjBCj6QSWR_NHfaEKcl2oP8362C_X1u-atCQf5IE_uCj2KI-Omaq3fG_zL2l9vDjjuELz1vQNpFVVZ5CXznJrKtZwSgGEwUGN1mR8-COlDA3dSgXFkfczaq5G8tvubY7-hBboRMYTXZec6RqyX4l6IakjzFasFrJxsL8Lk9YYiFbK-uZwNm9zrjDJbL793w-xWm01s2JLiAFDtvkiU9pEyS5Wjb7ocFnceUfKOHgkMkrRjPbHcBWClw5Qk48Cvy9FPlUb3zgdLXD7_1Ptxqtu26iM6DMmeOSGR6i52X4FgEDZ-PWvCqoen0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باج‌گیری بزرگ حریدی‌ها از نتانیاهو؛ انحلال کنست عقب افتاد
🔹
در حالی که انتظار می‌رفت کنست در هفته جاری روند انحلال خود را نهایی کند، معامله غیرمنتظره نتانیاهو با رهبران احزاب حریدی، به تعویق انتخابات و تصویب قوانین مورد درخواست حریدی‌ها انجامید.
🔹
به اعلام رسانه‌های عبری، «آریه درعی»، رئیس حزب «شاس» و «موشه گافنی» رئیس حزب «دگل هاتوراه»، در بیانیه‌ای مشترک اعلام کردند که به نتانیاهو «مطالبه‌ای قاطع» از جانب مراجع دینی «حریدی» اعطا کرده‌اند؛ مبنی بر اینکه فوراً در مسیر «قانون‌گذاریِ قوانین مورد نیاز» حرکت شود.
🔹
این بیانیه هشدار داد که اگر در روزهای آینده اقدام عملی صورت نگیرد، آنان از انحلال «کنست» در هفته آینده حمایت خواهند کرد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/farsna/444440" target="_blank">📅 09:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3oxB7iNH3LO86_F1HI7S1L1OHxZfX5SyppQ5CmruQFEL1jKg7cU1d3dmaKQhLIeH9IW5ovfPNq85yix54qpbvZwXC6FLdUrptx_qVLHmtk3Ym82FYE0d0tVKWzmH2l1e5QbLEKCgZ0ymXjasDjekToQ53X-oxgow7j_OdICX1wDKdz6dQfYfj0Y_0KSd3EZ_9qUiba1u7HWSJBbix1J2hTFMQ9ITkrtmJ-bF1SPIHA8dcRZthv7d-UPtV23Xnukbi-0pIaeJZARxkHV1swT81gKF_ZpLG7ejBdiZwb9vl-j-RkqkZS2LGfK0bNLlHQJ-5MQzsSzCFiqaewshQKNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تیم‌های صعود کرده به مرحلۀ حذفی جام‌جهانی پس از پایان دور دوم بازی‌های گروهی  @Farsna</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/farsna/444439" target="_blank">📅 09:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444438">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6471f3a8.mp4?token=G7Sx-LVtVIarVmD1bPq_oZvfmstBg12GO-915v8SR1OMNWSnqIFmTzZXRspdBl_6Nq53OdS4_HgxB0LJvraWRs4wG2iwLjnD6O_aeYJccyX2P5GPFN6ldchM6Q1hXxNSXMLojOpqK5sxqK-wN7539swTvIKjbtK6Fc_TBAyTEGX9DQXqAfYfctiCg2gVujyXVz4r7sb9RMcZA9OgH-gKtMasoK81bWzwmNvvHsZqtg707-wxIxYk1rhh5wRgpcj8L09ubDYPg-fu0QQ5UPI6CMFw18Vv-hBUKQnCrnwof5nBBr5VjbwHb-Tk3DnwXEFOV7kE7RS4WphRQFRqGvsu8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6471f3a8.mp4?token=G7Sx-LVtVIarVmD1bPq_oZvfmstBg12GO-915v8SR1OMNWSnqIFmTzZXRspdBl_6Nq53OdS4_HgxB0LJvraWRs4wG2iwLjnD6O_aeYJccyX2P5GPFN6ldchM6Q1hXxNSXMLojOpqK5sxqK-wN7539swTvIKjbtK6Fc_TBAyTEGX9DQXqAfYfctiCg2gVujyXVz4r7sb9RMcZA9OgH-gKtMasoK81bWzwmNvvHsZqtg707-wxIxYk1rhh5wRgpcj8L09ubDYPg-fu0QQ5UPI6CMFw18Vv-hBUKQnCrnwof5nBBr5VjbwHb-Tk3DnwXEFOV7kE7RS4WphRQFRqGvsu8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اختلال خدمات بانکی تا پایان امشب برطرف می‌شود
🔹
رسانۀ بانک مرکزی: اختلال خدمات کارت‌محور همه بانک‌ها به‌جز بانک‌های ملی، صادرات و تجارت برطرف شده و خدمات آن‌ها به حالت عادی بازگشته است.
🔹
تیم‌های فنی و متخصصان امنیت سایبری همچنان درحال رفع اختلال سامانه‌های…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/444438" target="_blank">📅 09:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444437">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRrKbhcexnRpRULupBhQe0nRa5UNSqRm9XYC6zmoO9JcuR9CP8ua-8Z0VtbgjDvt6awiW2FXfGBFIoa7sVHIr0A7F6M9LnjTKeimilJ-l36q-A0_W0st1P_yWcUqOH3BpJjv21PgnG8MdwqKfVLGCtTVvxOT_6M_lrfuI2LNBK1A2_Uj71MNxwniUd8n9s2Rop0yICNQt3MnWf3KpcwbE2BzMwI4ErT5wtnTgxrUM4JzasLDnjL-vd6Iul1tCEDC5Bj4arQHEsmG_wT-28ej_HzxSfJ3p1BZWYcVwaKrz4rilLdElMoHPEunkPYk04udy4mEhTKgMY45c-L7dAGwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف عازم باکو شد
🔹
رئیس مجلس، دقایقی قبل به منظور شرکت و سخنرانی در بیستمین اجلاس کنفرانس اتحادیۀ مجالس کشورهای عضو سازمان همکاری اسلامی، راهی باکو پایتخت جمهوری آذربایجان شد. @Farsna</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/farsna/444437" target="_blank">📅 09:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0KVa7Dq36yotWSaSEdtkz2WuWUq8aG2g84kAjgfat8tdz0rX902lbb_uWDxgNZxTyw_N9LC6gl-AYL49y2OqFywk8AbsUeLjDeQrY70YIpuFQ-gUXaRIBowezbFyqG9hlZEWWlLHQCF2TK9CiIQAUs0pPYXVLUfGWiDQbmM6OQdzYfMIW96kJQWKJnHIYkVPMyt4-R6g3Q9UhJzcNa9aeCBH6OcWU7WV0cmSn582ZMJ5rCitYd1IyPksvz-K2yVJE6vhy82E_zrI3W7gnuExokWoZEJLyE2jQa7pX6BUw4lOw8mrHXq3dx3z76uBBXME51tqsAnN_lwJURaflOD_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnTrhf1lJBpSE2JJayk6rYotwNT5NB5uyHBAsExwGv7m8JLXdp6oGl3b-SmlEHxMc3P7Bl1QZ3X2Lk1PdjHR9CQ9dM_J_Zx5RVF3DIpjG_aDxsHgRNRm8QhSbP8d2M-DhGCFN9u-tyK3kXerTbAguNHEu1SGZTtVQ4wxwuiH4mtak8C4tVwvsnfDNy1xSe4ZnHjxIu_RBtI8aPNpjJNSFsFBQDPJwztiCQ1QdXlxG3rBaBb0GSnQqlpsbhTJMpOf_Hl2d1V1OTfW5B4tjJMRh8kSpPjcLw657lLETTafL5kJUnm1VBfbCzpxF2qabVcn5n99gdMmxirOnEhFshKwrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYMpPyyh42Ojsx8gRa6Z5i0bqJmfPslHQF7u220QgqLUZINEHQ1CinBm4kyUtOm-wEjWmKPVQ6Mc5naumi07gUH707Es6XCJ1wG8n3irEP7qA3ViJLFIfGfsQefUV70P4kOZVEVt5HFKg5F2DCu6WkqarjOEyf70d-9tCNmpqsxlBfRntAGDQKCQaBxUlsF8ZNZyb-VXnWIgD6WDTRJmekgqYRXpDVpKEYeia1hD2Pu9PMq2VJwzwIHoK34M0x6fj7oy9mabMmuhFT9M2N_OxBKrx5WeIFr9uEs9cnD12PDepxhA4T7yH8Y95HCR2MCwZbhNnNWJYg0RIPNpBUheag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRXBy7gwPFd3bp7REb7h3QwiR4smKYtAYAWYE7M5CiSkS9FXt8nmEUSx3_96OAZu34QnG8UhE3gUlnWQRG33rVtfxsA41G_PzkrapN1LbLcvyhGCS73zP1o-Emtr2ALciNjs2Hq1bgDC-qp5bWpbXkbNAd_-acfZllBwA5s4Nk8ojMDfp88w9DujW6l3qnG9IYYNSutUeXpNjcufWs_2GgUZIZBBJskDxsGf1EIC5LOp0ZMZ2kS33PIWquWc820j1vFO_bqldLBCH1SA2FQSgQ74gR8TfcEH7-Rf01LIorIASAOtdNMscN2nXUM5L5o-WC1NrMeV0hp4blXexDeuZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTbbZdq4iq9Y9KRsXVrRmekZ40IqXfjjE0oUfvbt5cXUXx6KQcfEXDKKccn4yAMj4Rhcr0K9W7fQaGW9KkVrdJbATEeg1Hk28A9PO95Fd8FCBj83fp2BuLXUA_P97K5NJMgcCyz-dzmiP-myWLyKre5XNuc_arFH0qOYC0mhEpJjqZIC8mFjX5NGE-XoYhhIasZ4bDGjH6TQnRH7wTlAZuvuKopAn7CQVyZxqcJwzwGNOokamTiV1KiEmq-ApLkzu_LWLVvrX5GttZRI35_eOtAsw9pui50XmHAizMgoIMC9ao-eofCxA4zzs3zI4w51QFtBwTVRtTA3X4VklpFP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnTrhf1lJBpSE2JJayk6rYotwNT5NB5uyHBAsExwGv7m8JLXdp6oGl3b-SmlEHxMc3P7Bl1QZ3X2Lk1PdjHR9CQ9dM_J_Zx5RVF3DIpjG_aDxsHgRNRm8QhSbP8d2M-DhGCFN9u-tyK3kXerTbAguNHEu1SGZTtVQ4wxwuiH4mtak8C4tVwvsnfDNy1xSe4ZnHjxIu_RBtI8aPNpjJNSFsFBQDPJwztiCQ1QdXlxG3rBaBb0GSnQqlpsbhTJMpOf_Hl2d1V1OTfW5B4tjJMRh8kSpPjcLw657lLETTafL5kJUnm1VBfbCzpxF2qabVcn5n99gdMmxirOnEhFshKwrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین تمرین تیم ملی در تیخوانا
پیش از سفر به سیاتل
🔹
در حاشیه آخربن تمرین تیم ملی پیش از بازی مقابل مصر، یکی از مدیران باشگاه تیخوانا تابلویی نقاشی با نمادهایی از ایران و مکزیک را به فدراسیون فوتبال اهدا کرد.
🔹
در مقابل نیز پیراهن تیم ملی ایران به نشانه قدردانی از میزبانی و همکاری باشگاه تیخوانا از سوی تاج به مسئولان این باشگاه اهدا شد.
🔹
همچنین کادر فنی و بازیکنان تیم ملی با برگزاری مراسمی از علیرضا جهانبخش به مناسبت انجام صدمین بازی ملی‌اش تقدیر کردند.
🔹
در بخش دیگری از برنامه امروز، از پرچم‌های کرنر ویژه‌ای که به یاد شهدای مظلوم میناب و با نشان #۱۶۸ طراحی شده بود، رونمایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/444431" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9pA8xivsp6JJxH8n2Z46C1pL8Ao1kcB3iKnjwsOSKOLjhHhnzXSyD3E6MZ_q02jR7X_0inyC1eDZwZk8GAiNBOREaTbsS2iwsZbCDMwcFIaIOGZr-i9av8UiONTMI8qpiuYv2PJVhz9cnZtBUKKVM46IdVkJcwVG1PanvxroLlliyhWoYUhSiLK31I2Zhs7oOjno4v_ISbaxtJG2yyUMw5gNTGmYXGRdniUOmksFISKufD2sP2nf847ANpOF2r4YNCB2cHpF2JocfbM-Asd2p3SBBqJV7wTToS2p2mOrOEXinSZuNdYAzPb43qYudc8OWO1DB_Kwb-Wvmr7faXP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد سخت کلمبیا؛ صعود قطعی شد
⚽️
کلمبیا ۱ - ۰ کنگو @Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/444430" target="_blank">📅 08:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دریای مازندران تا جمعه شدیداً مواج و تعطیل است
🔹
هواشناسی استان مازندران با صدور هشدار سطح نارنجی و پیش‌بینی وزش‌بادهای تند و مواج شدن شدید دریای‌خزر، تمامی فعالیت‌های تفریحی، صیادی و کشتیرانی را تا جمعه پنجم تیرماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/444429" target="_blank">📅 07:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444428">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9cQbtYkuGxKxhJQdo63F52RY5IOkslNlqv-sJkMmrnnqN7aVRUkGincjKuuxZUWQeIOa3ShetMWNEUcQ4EmDTLSCGtI_1v-xgLs6GdXhRpDg15JqSi62TRUBtSnml6T6i5JfA_n5ZscTk58LakFWvGkNkc2GnDJ3IN8sNfpNFjFKVTPJFp3Von9U-fEZ50CBDxql9JIzgcgzivbrsdoyCl3pxKSErsxU95KKJWzFjpxdAzdcXLQ29s_rqgE_LQPVJ_3OR6KLTBH1vbp2yyJXU8t0GSah92yc0J-3hSXgBttLbQV5mYfbsIIQd9TnvRMOdFaslSk7eItb1v31bRUpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون افشا کرد استارلینک در جریان تجاوز آمریکا به خاک ایران، با ارتش این کشور همکاری داشته</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/444428" target="_blank">📅 07:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444427">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nc-ubvwD1h5MnbmigfIpOOj9r_Z7gvk_JD-0Ik2gxbXZ-aC88pe7WXdFWh5tFS_1y6yW_MvxdeRAXBEUGdOIOSw_6asLlP0GoSPjqFLv9O1u_i0HCuYvNCzz9GF7NeVt3rZACzg8AJFGXng1nc8U78eDxikfMPME_pci9aue7GKxS5e9ANQkpBVUlzqmorHsA-IcBLmpUHbL6obqP-zPMfdfj_I7j9-qkXKrecMJ-vLnGCUql1F_jfZKBjwkT5_2okXwTlM4OLeexPGKTfjPJ_P9e19YcwCVoIICsBySvXyLc3nZR0_GXXpzaIBDYyCHmQzLuIRD-ZVqB-PwHbt1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد سخت کلمبیا؛ صعود قطعی شد
⚽️
کلمبیا ۱ - ۰ کنگو
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/444427" target="_blank">📅 07:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444422">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mF_nsX54X3sgBZOiQZI6G6DptDWuwyRNH2DTGglZEERKJYbtUfYC3OXBVT1xV0KzrkCV-jEwl4PRKxPa1TGn-dIMTTYyNVUMaFPPmM4Uv-Rou5woSecgEPbx2DX6NqOh21BnBdYzZgJ7Pz3HpYFJjUWiAumLFeD_vRdD7BFp5220ikyf35KMcAiv94H8Of-2nInJ-xg91R_XKyIjSHudJIHliIF9s3nj7uyn5MkLYgnTPqcn094e6evFE6Fu0Eq8h2aJa2O0hgmmahXlIHubKyit44xYoYCkhj6xiL8yWWbLy-ydNZnck13CfrUerAd71KBryqvS-D3EYq2TsPvt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mf9WSu2QtzD_m1q7Vyi4cMOovHYnu_nLgm2DdgFr50SC-CNVwZuTgNc1g44wrHVZTJEyJcPeb8Thn0u26lBp7xsDHFfMFrCcGiIdQ4UNUDAe3LFgiYx8QlwcvLGaKTQ203r9rvAKQclzrfBi8Np03J5_c7GIdSO3uZyzCjsifzV7Ornudv3odr8fIStCj9DzvpFXj-PPbiLOig4zNLcQDjXpcx7hX9iyKSjxuYKGzz-6HJyYehEx2u2VViMcxhWE3uPPlS7Z-xHw-BFVc6P1knHbEkNOiCdxBToFpQr9GHl5Zxkv6S5E1yN0Ca0-Q12SRRaNRD5-aVDNGckLsbd57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSD8pqHRzfaxBaBMpCKUYihbYn16lbUk61_80TtIANh2_JkQx858zs9Cj-BVvcokrF-kKDAZhcvRDBbRSWdZ7PRznIVr0poyj8qAdAZdLN2wXWHD18VwXURVxbxOePeY6p9YuRZPUoXt8xwxcwmvezE2qvT1iqxluH_UiW0tSSGBCAwdP5M3ktDabBSemjZYcGcWWYvY7vUu9ktGQbGgEXBGsbrQzIcRS4bTzBD_hpAHKZrLM3H54Jis9qz-0wdCoACndVv3-sJ1b2MBHUoNFPIpNtOMSFD5wbAjRhEJrrlXn4Pqzw4ha5aKi7g10u4msNz3GPMQ0qO2ciMua4zvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uK8eL5lAybduYpmhjiWvrI9CZomDbZpd0OJAfITZFCKNC7ty2CN1WY6551kXiUST5rP3TFmOGsU_e9M4tsfYNqwQum_pIXEVnwhvFKAgYe0nfwpcVK4LjxBgJ5d5ZBwY7tK6dRYgxroe9QYbP1npxBA4MyZSfhZpXm5K5O67DvDlTfxm1Fls3UYY24ZOBK0o21ivCrobQMdc0iVHEbzKBxPiyoLQte-mvklIvWINH2WcD3aqiOZCoXVsE-3jnLgEZpqfpJxFUf4AGQnyBuFtu67qPphoHZztY7TGDNOcFAvAAWrXV9cneRdQoR7y4qxF767zmeDKX1c7a0iMglvHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PxNwZsuka6UPskL--QK9eaGO7Wblc2EiK3NER_19HI0huJTL68-eBB341eeNmOIUmbzdwFeZfDRbC-ELxJbEqbxdmn5IPPLl34nZoNdCZXKKjETGBj2BMAJEWx7QEJliVJwOP0YdYXwvt65uRuBWaC7tnj2Fsa3Mx7FaG87fNyPZd27LPX2otASe5mabB8XFUrV63WKICxFXfnlcNly9dyt9uAKBxhhu88ADp8ZnZICD07tWf1PzGv9ArPrBm8fLSOYQYdCgVefFL8ws01JmkqPitDIqZjxH_OC_nJDDUk2FeEQOjIAkcDJqKHcsbY_mgZzX1X60kMTTxReuOFwprw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسینیه‌ای که در آتش اغتشاشات سوخت اما چراغ روضه‌اش خاموش نشد
🔹
اینجا حسینیه‌ای است در بلوار وکیل‌آباد مشهد؛ همان‌جایی که در فتنۀ دی‌ماه، طعمۀ آتش شد.
🔹
روزی شعله‌ها به جان دیوارهایش افتادند و حالا در محرم، مردم دوباره به همان‌جا برگشته‌اند؛ نه به حسینیه‌ای کاملاً بازسازی‌شده و بی‌نقص، بلکه به فضایی که هنوز زخم‌هایش پیداست.
🔹
میان دیوارهای آسیب‌دیده، فرش پهن کرده‌اند و جایی برای نشستن عزاداران فراهم شده؛ پرچم های مشکی بر درودیوار آویخته شده و یک صندلی ساده تبدیل شده به منبر سخنران و ده‌ها نفر که صبح شان را با اشک بر امام شهید آغاز کرده‌اند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/444422" target="_blank">📅 07:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444421">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کربلا به آخرین روزها نزدیک می‌شود
🔹
روز هشتم محرم فرا رسید. اکنون چند روز از استقرار کاروان امام حسین بن علی در کربلا می‌گذشت و شرایط اردوگاه به‌مراتب دشوارتر از روزهای نخست شده بود.
🔹
محاصره فرات که از روز هفتم آغاز شده بود، آثار خود را نشان می‌داد. آب در…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/444421" target="_blank">📅 07:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444420">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSZDv_7WHprpl19BKLmEvj12Nqx6VleJo74axFVthyM3kKydc1JN7grR5PtXAQlNwtFc_0Rh7g1kRHfkIR85WA0TQvJIO_AVqz8LmGU8f1UKvN4es3JAin6JNOdesc_bvKau9mSkpjry6MPmrluwvu7L_iIAt3cgo2lO3qRUPxCldzuWXpNONTFgUOddIQHpUz3niDPt_ZTt5nrwvWgyeavWsWA6-22BHlOLTYAF86tWv6gvntdjJMCpi67jU_tymbAX5r248UNg2-PI9wOLhvv_YiC8w-jGxT9DGHFp0jp2gSoKxoS8hvEdfMHHSM6ibElo-tdy-e4IJ2M2mhhUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف عازم باکو شد
🔹
رئیس مجلس، دقایقی قبل به منظور شرکت و سخنرانی در بیستمین اجلاس کنفرانس اتحادیۀ مجالس کشورهای عضو سازمان همکاری اسلامی، راهی باکو پایتخت جمهوری آذربایجان شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/444420" target="_blank">📅 06:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444419">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-rLDw5wYMXGka7PL0y5xg6XullSbHJqAsHYu0tKCsFPJdM6g2fzkbEiBb-JvOouy4cGI2dXFE3rkOhcZNJa39Fs7ljUc2oXFWK8uQhx7HZbJHIHtZ1xfw3gQ9bxMS6_aJoIat0RVrUN8Li8nuWF4-OnTzsYb48Xhts6mNLpwAgXlSE_kV7QwZqkP2FVBNvBoweQ-uK_-TtpAO2dkvHHOfRJBGOopaF4ngkvN4WGSkg6mbDXraVNgqi2SIeVp9VEDXqTfVApavSHqjRfpipFGXNkTH0zKbbT4tx9O0rhiuvTdodYdDVTfJH2X4UG-_0S6y8Fgsk5ojAxOx6F610YEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجهیز نیروی دریایی کرۀشمالی به سلاح اتمی
🔹
رهبر کرۀ شمالی اعلام کرد که نیروی دریایی این کشور به تسلیحات هسته‌ای مجهز خواهد شد، و برنامۀ تجهیز درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/444419" target="_blank">📅 06:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444418">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XY3VO3CXy56y5yO-Ob0PYRA0lKAXh_BVERvY2RQWwgvoLXxgCjTpwsK_JvIcGFO0eLVqc4-9l1UdEQb6k46JU_ilts-vrS4HEutPVBb7dY4KKqDPrciS4Hg9kh7qM26bbyVO2jxvpCMo8DXX2xNGUjGRgMgSMCTd8pv5GQWgF3kY3_fr67AbfsZL9qSWgWgiAH3eJ1kC2SLMZoxSBGVDXD65DAKsJykJaTRobtzl48qTPSakjb2mWEf-gnW8r1Iy9xTJEbutn7pnxmN3wR0Vb5hjbVdG8wqjN-vBQsX5cOIU4P67xt1846Xq-3YKqOV4TFemFl1DgJYPWDyNAgNNNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای پرکردن انبار خالی موشک‌ها سراغ خودروسازان رفت!
🔹
در حالی که ایالات متحده بخش مهمی از تسلیحات خود را در جنگ علیه ایران مصرف کرده، هم‌اکنون دو غول خودروسازی این کشور به فرمان ترامپ خط تولیدشان را از خودرو به موشک تغییر می‌دهند.
🔹
او گفت که دو غول خودروسازی آمریکا جنرال موتورز و فورد، در حال آماده‌سازی برای تغییر کاربری خطوط تولید بلااستفاده خود هستند و تاکنون توافق‌هایی برای تولید محصولات مرتبط با موشک منعقد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/444418" target="_blank">📅 05:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
تست موتور سوخت جامد ماهوار‌ه‌بر
🔹
برای نخستین‌بار، در مستند «مرد ابدی» تصاویری از تست موتور سوخت جامد منتشر شده که گفته می‌شود مربوط به توسعۀ پیشران مرحلۀ سوم ماهواره‌بر «قائم» در جریان پروژه‌های تحقیقاتی شهید حسن طهرانی‌مقدم است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/444417" target="_blank">📅 05:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO2E2qDNQ_gjWZAIt8uS0bvsq2X2oQlaQE06BwGGmpApXPu-GOkqfAWw9XcmqVeVnCT4h7yJx99lEuMoPqY-9K2AOCM5E2uU01pFDeAd8l4nP-Cq8K-1l8gwSU-i7T17eekUz-MytJS8v86VE4YWJDVd0SLtxpZKDa6S8RCIuXBSVvU5hHLtf7Dh6V631ZVD4HYjsSmMvKeY-3tGiu1tAU3kUh1Eqo0PUBdhTxVzXJvwDtcpCRemgB_9gD6pU_XszM29-QG42Eg58YzzDICer5snBaLA8cEmSC0G_GxQnEqmtl6LpfuZ12gR4-v_iKkE1n3TZWdHTLO1yQqnmUcZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد سخت کرواسی؛ پاناما از دور رقابت‌ها کنار رفت
⚽️
پاناما ۰ - ۱ کر‌واسی
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/444416" target="_blank">📅 04:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiDSIpQBuWaQbF_MwRwWnKofOA0CGHVhPC3Y3-ZSt3wAA9QozR2fyDdXtXEf4lLs6Ezb3TU_BV_v4bMP4bbTJEblU33JwXs442Gt9J5JeQJ73gLu2LsUdKSkOx-hdXTa_DQvMFoVhEG2wGhSJoleZ2-AZMV0U24InTkSr0r1gpKm2Sy0aFTpcnY1iu3Q0_azqBjcB3taulN5DyZhYBqORXa2ZlT2J0NEtf3e2SuPjm7QSnLzQVvuKRcpQSTw8hMdYBwQ9PzY4TUEKNW7tOKzhMhHjUVguCY_4yPho5GiA6azvM9Nqnad2nS-jEJDfnFkw-4mKx2-G4fOY17zmhN3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جریمۀ ۱۲۲ هزار راننده موبایل‌به‌دست پایتخت از ابتدای امسال
🔹
رئیس پلیس راهور تهران از اعمال قانون بیش از ۱۲۲ هزار و ۶۰۰ فقره تخلف حادثه‌ساز استفاده از تلفن همراه حین رانندگی، در سه‌ماه ابتدایی سال خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/444415" target="_blank">📅 04:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444414">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN-jnPnowAcPWiUZnfHp_I0LqyfWUuOQipkbgfyGuzpRtPeYykTvbp2_p_KoizwUtaqm4Dw8nzrV5LS_Qv5QMDNYqLji-loCCyuUhUBB-2fXwL3yrohYDWWKKm2jpvJko9yDu1SNkRWSOJfzScKJlrwhIcW1MrGxB_gH_4bVmg1Ru7T81QPlHB-jV_pcO-MrZbnYhaBgNkKatAF0Hlb7dVsZOEyaNcqJGpbN1cCkymkG73j311SuDIlO1oYNZMp3gsSq3PrXL9ncj684if9a_b52Bu-_aZraHa0bQe2WixYJSs2x2ba-F5X-BjiYZSZVDnghYLfO3G1-wyOA61BzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۰ درصد نوار غزه در اشغال ارتش رژیم صهیونیستی
🔹
شبکۀ آرتی گزارش داد که ارتش رژیم صهیونیستی اشغالگری خود را به حدود ۷۰ درصد از نوار غزه گسترش داده است و پیش‌بینی می‌شود این مساحت در ماه‌های آینده باز هم افزایش یابد.
🔹
همچنین ارتش اشغالگر در حال گسترش مناطق امنیتی در نزدیکی شهرک‌های صهیونیست‌نشین است؛ اقدامی که از طریق ساخت جاده‌ها، توسعۀ پایگاه‌های نظامی و تقویت نیروها انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/444414" target="_blank">📅 03:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSQOL1AMh1c8lQokkw1oYbHGPC_ia32sPSjZRJfeL_5QgZn5SA32yDWMLfD-qk_BIl_zaZqiFqtJjdJkeLkW7_FpaUreoZ772CJ7Y5BANUc58S3iVE9ci4QWbS16F0KU3sMVg730L3tnDS0O4fa5xvDqXcmDVwql4z8MGDQ18YQcdZYSmvRBA817WiekoY82kzlQZW5gOn6bEtL5Wwz3DrhXCL0OL45KUg2YlR3z5D2DspOxqau15EkXjs69ZaTeephASa8YSLbUH45VCl-PRCNOhOGTm3aRpc6yvSfc5MoRnqMlWb0N7AWUNVNlS8Mhr_1f1VnRl7GbTHLYWheTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6I7dYpNxJlQxNwxYRco4zmmaj7fC5XPmZNyPkW-kNO0rf322uFPJzzA_8xaZTWRsNyK3sE6DSl2sXCWEhJQK7OypFZATonitnGdrZBeEFSrD-hLJ5-imPReJn5BQV7YL0gTjOHBk9EwZqND0wfycWz4w6W0YopLNQa9kWVp0wd76gG204MdYVtdSE_vqJuqcpW9IxAVkvV2pt3L0iR2oCxI6MzQVSrhiP7_xliZfgUgwbYXElh9fKg3zN-2Rvhh-i-yFa48KaCYn5Sp0MUpABkL7TZurTm0PiprNRwOjBapqIXZtD1Q8fGmTMRoBX2gmAG6ggUefYayGuFGuWlwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQMd03DzV4ngYVOFCvxUo-A0CEoy4HRJ5c1TEfmBlNg-VBnWhT3rTrROHnqzy6iw2Im8oAi0wDux8PGEddr46MJJ7HQ-dl7x_Lm26VkcZ8zcKBK73g7AQhWanWzBrfRzJ4zfCCWjJOkUrYF5nX7H_BOXVjlbmUy-0M7QekWW3pxADLLLvf_7ZRaMtbI6tENTjTJVb1GOc7lCAbaw4jIz6pTPuGLY4hbSYfIHVg3kwHkO06otGQYyVSfRnLyBTKA4nOy4BAqSXt7q-OxSmq9ARo3XwhgqNQfKxfvOZ9txVrUrU8MjNF8gdlAKPKFYu0q14P-iDXCfYqg-WTPT3rbt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ0O_iCqLIJcPs2ttnd4a13RUcuXODcEPI2LIZnYQLFwtyImR_a7oNvNUkUYWtC6FyVrYraujklRjkevxGgrl3aLu4OUwlUysN0kn_89CSE7qghs3H-grFRdbVobZ2fokzT-tZjhoPJq2sbPmyIlgd6z9v8tJk3eKWEJH9tN6F_KW_V0P9F_bk3_udXPAgtN6OW3VrchfSYiwAN0S_pnTh6NOFbjkdroyQh_66OlFNNhFsru3KrHcbtkhpPYppN9hQofadapdcUOZABty9AxKqi22IuPo53G1ogewZOApXAnMwk74jwa7QXripD_7_t5EYqhKZbXA7gWT9qQkURU-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fbz-bHwSeDxWbZlWkcUK4V7rWOyZGkYxQiczfFjETxvAy_Vl4t1gb18PucmPyWLpD_M4Mjl3nQT7rCh9C5NReRtuUREht_TfUmI-q3Z89DyFf8Dt67_IkP8JjCZ2kPVUm0EKXgasd0xju9PVJu1vNouz_540T3pjj_LXx4TmcLIlYm3OED_1AZ2KKMTzH7qoqFVQmSNlU_RHrXKZX1EUZbSFd5sefhMpR8sUKvXA2VU_AE2DCPPiicgtaQ-SPWdl-rJ36IK01QZH2c1_FqQd9nbRPWNVaFc8oH76Fh0T9fQZincPiFN-Qi3CsYqpLkC9HDlHm_Kor-AoJyycEWq3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owFG3NzZzfWsKGBrmnNECrl8kqTFo2S1VAm1lZKwsvntFoz5zlKfniWeCx9fXLCOOogP5kF0SuBhZOnFGKb8A_M48LvRcmVZ_21VJRc9FBprIvyWhbXYhJwO6nEnJnYHOszYi7RBRfOj75f8h6NWtGOLRtYy_XsBvh1JtrsY0HOBlAeOlbdmskxJhk8lhOH8DxNPH6czjbbMbVDzkYueK8zOW1sw1L3OFbyW8LKrm7Tsaed7LqHwDgiouFBY8feHTwWV2r71aJ1YLy69x4trGbuw3DIAyXp13NAXcqZ2FwMaK7KysBme7YSsMqyrcLbJOxrrfX5n4vZXevH_1yDdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hA4m9lVxuoDEr9-0GZ-zba6YxzscnJuakP-j2E9iezZGbFOYdX60GbYnOdfgfNHgFemSNnxNSiFd30sOv-HlilEqhQ52daybrBUG7PgXwGfJ7UHLbd8OJNp3fy6tX94E3NA1JDMvgV885o6iWm_mTio16QryppbMC4YuPlttKOYMhFCR38NrnWFUbFLpaY8xOKMZgkq2ZnL0-7QWKHmykVNxLqJfGlUMIOTfBtn256vMFNIlxGbTQv98hmDFgiFzyuZQ3_qVYuauu6Bj71QUkc4YAzJNKtw-ip0vekXvFSCpIdTFfHqf-ko6dfqN6dAWepRa_-keeKzNP8yg1phxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqERGz1JAZAlGA8GH1Hq7VTWZ45tLw41J3HgkIvRG-jx4YRyiZAjuKhrD6CigXfFqNOLaZOi-D7SeBYew3rD8mNLd7djC3BbeMejhcfUK45rqaSbMwO0psVYXrlhOaY9KLPd77QLj5bunjzyK6estOPfCMRw4JoOZNo3ckiLs7k-6Z9tKVvS2CFn6PK14kEuOQ--RpRx-uUkwwzZDUp9AfmswxpXrRP5ZomDv2O7FbMuP8r_wA6DcWbOfRQNKZmLrbqSHoKENDFZ3kaj7DNjwjXHK2f2JOC48PgUYUgp1aVs0-PFqbbeX-QePubLmEkd3FL-ZtFcabLNhgGZhtqDvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع عزاداران حسینی در رواق کشوردوست در شب تاسوعا
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/444406" target="_blank">📅 02:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd86c81b16.mp4?token=AKhwfk84-AkP-SDP9U9bWp8ssL61iGnM9FSOMPFe6rTKrVqW_--saeKK7MVhkrDwM2PZ1pQZ3PhXGRIAcwGLsWn4XAupQ5bgXYvlYSgQYWwBKFtdYVuL9wXTtYEgQQJF4o63DD2JFoy8u3Zy_pUPF6pU64U26Nh5x2GL6ztNqbIAbrvVYkvZFvmnApvnjDRVs8HGmaU1Y0Qft-bJHSYv-fmsozz6g73NJH6t64wlaa6ghOdnYFZ3WUfNEeDtdqFC23U4V5KrCmUdufQVV6rtoprgUR0_SDI8a0WPVPEr39qccX6QLuJCF5OAza-3T4xP3sFxWvBdQTWLYdADhYfOEVYji_4-gdCFQHXPvNUE5Xb1h0Ae1a4SiU_bDfK4YcW-jhIWOopwIMKIJ4k1B34cOqiw8vxjLoGbwKe7Tf4zieibDS-zgYbpbK2gNsBpfYeyy805V7-Q5E_SgbF3YyjxtmeYhafElTG4QCcs17bMmEJaRU-Co2VPiFwBc31TzH27OcnL8DgtDeuFXrzKtvPa3KywBuGcfJNbRu4xEnrdC-u0d4uHoKMcprOWfDsoIQ7dZF-Sf6yr7qzhc-0NQXZQZ8HNyix8OoKPnMLlyXMvqKS6fwMGpDetgvropfPLiHaerITFRg7MW6F4ikv7joMy61A-OTDy_1o8u1BkNKUfBlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd86c81b16.mp4?token=AKhwfk84-AkP-SDP9U9bWp8ssL61iGnM9FSOMPFe6rTKrVqW_--saeKK7MVhkrDwM2PZ1pQZ3PhXGRIAcwGLsWn4XAupQ5bgXYvlYSgQYWwBKFtdYVuL9wXTtYEgQQJF4o63DD2JFoy8u3Zy_pUPF6pU64U26Nh5x2GL6ztNqbIAbrvVYkvZFvmnApvnjDRVs8HGmaU1Y0Qft-bJHSYv-fmsozz6g73NJH6t64wlaa6ghOdnYFZ3WUfNEeDtdqFC23U4V5KrCmUdufQVV6rtoprgUR0_SDI8a0WPVPEr39qccX6QLuJCF5OAza-3T4xP3sFxWvBdQTWLYdADhYfOEVYji_4-gdCFQHXPvNUE5Xb1h0Ae1a4SiU_bDfK4YcW-jhIWOopwIMKIJ4k1B34cOqiw8vxjLoGbwKe7Tf4zieibDS-zgYbpbK2gNsBpfYeyy805V7-Q5E_SgbF3YyjxtmeYhafElTG4QCcs17bMmEJaRU-Co2VPiFwBc31TzH27OcnL8DgtDeuFXrzKtvPa3KywBuGcfJNbRu4xEnrdC-u0d4uHoKMcprOWfDsoIQ7dZF-Sf6yr7qzhc-0NQXZQZ8HNyix8OoKPnMLlyXMvqKS6fwMGpDetgvropfPLiHaerITFRg7MW6F4ikv7joMy61A-OTDy_1o8u1BkNKUfBlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله میرباقری: اگر می‌خواهیم با امام زمان(عج) همراه شویم باید از وسط دنیای بنی‌امیه عبور کنیم و با آن متارکه کنیم
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/444405" target="_blank">📅 02:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444400">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axZRLPHey6xtEtFfGq9Ks3WP5D_HIa--CoWVHARg03EAIMDffDuY_-ssoM8Bzy8fFFEtZ-Ixw4LfSRajV6EWnvt3J23iVmEeKvwULH5jfmTGQUMfZuuZJlQBN0dXsinVPEHmAJho5AxxgzanUN2zvJt3-Ike_3JrxiNPEcizW34zjWbfqnsWCs0_W0yvKnmVTF3z-YBkC5scQq_higf9vCrKMereHQl0GqxWdxUVZl475kaj-rAY7Yd8DwJz9qs36UvGh1fkk7MS0GJvlNpM44u4QnZXXZgD3yLucY-8v-0ImQdyYgDJ4W-Cj0ib05huGsMgL5dE-H37-nkZR-RfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkyhPP-YbdVoW8GeHfiy5MRZD9BoR5rJc8kgIGB07p3KYl4UXjKaCgclaCbD_xV4bHRtnSSNED9DfSDZrA2FUu5fs-IrfZrzuNsCbDFJ--1h9v06h6Qa-k6VR5MFz1WV9xeGd8A_ufNYj0w4YiTyK2oahqn26BD1L4A9J5uuQ7SaPJy9MftVArhL8Ivfbqpe9bgW3TSYZhPTlNGYfLcxsuKvpsmYm5Bkr_eKgZyiuGo6buE5U8wpgKzIKpHCbH-nPeDGv0pbDQt3qPVtYMKWYfJkM3wW5by4-yCGuE-Xj4UEMHe6gjg7rFbpxYMbCapmx9tsT9-weGnMH5z_Bkn3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVmYhcJfSggAzfaJyG4Ssx1sjfjXscvbucW4MgUHPNAKu0jsTdPCwoqb46wFiR9ehJ_1vna-Jc3fUir8gPZlKNlgjeuH3NlCaKDWDZyjPuS2tGbOhucHrSt8Qjtc6HJv8ogu2M_slXP1WF8-DNZcQB54O11y6pb3BHZCrZmec8aYWXhTM5HR_kSSlr8zIYIqQXUVpGlCFv3ehCVXnfFfBRTGXULih3G-ADjLxyjiPMv02Hch-lG6Big-nieq6-sqYWgMwaMiC8vN9nxNlP-v7Z5kG01kXtG2QK80dnaXrB1y4qT3DV2kZbSShxiS-jZLYZjyga4SaPwEmXfsoJo3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gw30-IRy1qcMToraxh2LNYblXboaGDWa_7xDegkFoDh_oEr_ktzhx8k8RSv81jCE5huuPoyo-GkE3ppR0AYLO3HaHo8_HaqfpbovR9QRRaT4J8OAPko2Ab3UuJEu1k-jzWlTchBEsX2X-NUifhDIJCb3QZc-2elTUmUQ1VyZYTWAB9NbCosLkKeE_SyeFdSNpVKtN1vcL5Gy4W-FEH2nMQWstevbqLmL14HntF12g1Zc1WyBLtE2xLlz0mxycGXLLzDCjjhNqWKe1hIust_CAxu8AJaqIzLU43-BioFP4x_GixRfCTAVwb6mGdLq_Vvow-RCRijSjhhqJENG0IEQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/td3c3CREYBuMRy7K-12DblCY1KF3xgLfK0oUO6VZyaCouafarQWRyCSQZ7s6OJF1lo_EjSdhxwVovRKgLtYB-d_wKCX44E4TQG5yoAh5Mg_Pw-25FzoV_396KKLFcp452ttOR9bYkz7ow6zvbiLkNFut3kyCl_A4ihGIUyyNCXN56UOivBPw94LfGnef5J1rVLJ3ELKdghDeVa1Cr13X5O-Gj9BLOfVVVBYHRtFqetb3QzAVxpHfuedUqVSzVPTtnbt0zjtVb8AI8BrXq4a7kiGU3_U23t35KSeGGCBXYgmxAUddIiZxZNOp-9F4yxcxBxRFmv-KX0oIc4jNqCkzmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزاداری ملی‌پوشان در مکزیک برای تاسوعای حسینی
◾️
همزمان با فرارسیدن شب تاسوعای حسینی و در آستانه ایام سوگواری حضرت اباعبدالله الحسین (ع) مراسم عزاداری با حضور اعضای کاروان تیم ملی فوتبال ایران در محل اقامت این تیم در تیخوانا مکزیک برگزار شد.
@Sportfars</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/444400" target="_blank">📅 02:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444399">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSeAKU4yqLoP6KTLk2lrOgLX1s1nuUSeRqXp6-dKvPog_OUpLEAzReGXs2gExMoCISwIt0xKPjEriTQJxGAqsUYZNUs3vUvDE3Sg_5jOX0U-UPU_Bqq0f0m-sbXZsTL_lK_3sOl3XFC9axiFea2IBFxvjTJHU3LDFWXzhV4_U6vfr8nqyvradCHkHx9d8pSwn3_xaHWH3VZMBT4GHXmO0_uDjbE6U7z0xJ7aBwk_CFL6Zqjm5uT7KI-HIaacGoppFWurFB2lRMn_0Wi-LhBvKTCn2mvyXpF4kNCyqtA5uyoL4OanD8i7UZ1xS-VFXIy-m3GrH5oSQ5cRqc-DqB87zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان تیم ملی فوتبال: با روحیه و اتحاد بازی قبلی به مصاف مصر می‌رویم
🔹
علیرضا جهانبخش در گفت‌وگو با تلویزیون فیفا: این بخشی از فرهنگ ماست که همیشه در شرایط سخت عملکرد خوبی داشته‌ایم و نشان داده‌ایم چقدر یک‌دل و یکپارچه هستیم؛ این ویژگی وجه مشترک همۀ ایرانی‌ها در سراسر دنیاست.
🔹
ما سعی کردیم در این دو بازی هم همین موضوع را نشان بدهیم. امیدوارم همین ذهنیت را برای بازی آخر حفظ کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/444399" target="_blank">📅 02:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444398">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نگرانی اسرائیل از اسارت نظامیانش در جنوب لبنان
🔹
نشریۀ واللا به‌نقل از یک منبع امنیتی رژیم صهیونیستی گزارش داد که اسرائیل نگران احتمال اسارت نظامیان در کفر تبنیت و مجبور شدن به تبادل آنها با جنگجویان حزب‌الله است که در تونل‌ها گرفتار شده‌اند.
🔹
به همین دلیل، به سربازان اسرائیلی دستور داده شده است که برای محافظت از خود، به صورت دو نفره و سه نفره حرکت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/444398" target="_blank">📅 01:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌ قطعنامه سنای آمریکا علیه جنگ با ایران غیرالزام‌آور است
🔹
قطعنامه‌ای که ساعتی پیش در سنای آمریکا با هدف محدودکردن اختیارات جنگی ترامپ و جلوگیری از ورود به جنگ مجدد با ایران تصویب شد، جنبه غیرالزام‌آور دارد و معادل یک قانون محسوب نمی‌شود.
🔹
پیش‌تر مجلس نمایندگان…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/444397" target="_blank">📅 01:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9oSFotrmupLxBq4W-yTQGdTVGyoCbPzcK7IQyP1RgV9QQsmSsV9NnmYzUQtdKxhAdOR8CQs6W3MY_ICi-7ybQ-aHrtN-XNO22ynH8Hg-lP_9SusqpIksCYdaFW9v6BRilXegl2rAYt_rzJrOp5wB0_r7cWTCLjbFukN0C3j_SQEceGZrgxCyk1gleKQ2a_yg3ZF5bGbR0ejg2Mt-EZY9bxZu8nnIqdUbPQ6zmGFH3JVgBRbtcPilbvoB7XHhXeyR7RnKA8GQrxexqSqAAjuhWEUtyeg837fUxMsLU4nrsTsBm5SuNjtFT3RGQcpnN1Ng9C8ywDgczNW8uqlFJIUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1XxcdeOQRH9qIDPNT6_ku2uPOkCAnvjRznJ1CQJxwgXp5snoC54klexYL6V3vy27914g9OWxF9w40x6-EvajN2hO59wOTHZIEpopHOh5B97Hjm8DRDFCHapwUUSMK7LdhUsQjSrf0-ID0dgPdvCiEnsxCy1MTGgFaWP7SXw1BZWWWn9kNXtRe8DOgHVMTlk1MLRIZim7mtbSv6ZyMmbqORZnk9IqPxGIkTaEDd7SOJTGDCJf0RdYNUXhNjcLR6xjm4VfP_0H5Qt2qV0-vaGEIjRYhagjxCnBPUDQXO8xbp8GqQb7MW-pjiDkSXKOdM8AdsEx_as7-9s2a0NMpSpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYMg6VR9vbWph8hsK9SR5JxjF1TOtdf-c6u3J8nTrMnF40WY0q6JdYI9DvkHNjeNopIAwg00XNllfsVXCaelGkCakPvj-hbvNSe3boXBfj7DMel0YXV-LaZkJ4U_ArgxlcWt1OkC7V335cI_FC3ZZToKpogQYR1THwjHZRAaCh0JyxZpCniMrNNwDI1ig-V6tvXPEGQBxxev9rl6mg3cBAz-OhoZm7QCBfomPQOkjz78QE0gs6Qp7jRFk575HRGkjVna6gXNG7y4gKPmiXwn_CrndMKBX2I-UvR530Vw8Mw0NQjqVoh8cIsuvnlG5bcmBbobj3qgMqDPiJWso2gjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h96BJ_lAceVFipT6ZZHNT9JCViycfdxqg27bEb4nTYemyTQxHYcv9cjSuStNmW2O0D52uVLD2Z32W7e2wYUOund6bdvslehjptbubcoK7U2yhpFQY5ggb9Qn8riApNSFX-pGnnjZZTdPLRv_wM-nbh3rPBrTOk3d_8P8u5Ld0D3229Be0fqnxXZ6npyIiGSMHqKOJGYRIo1fldE3pOLbHe8ytJ_IO9AESCtOs0BqWpBtfsMnCAyic0PANSDAjD3GDFbGFt38YpuOfu-ZZq0BfQ5nLnZlo3FFPoC0ccFkJlrHj3TvNjCy3GGx0HL-EjvRYpF6jTJh0ZeyJnC9DS3mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTLER3esMPxI1zGdVnawc8u__-w4gvu__ocwieDUVHuqDxWicK8QqryG5EdfFSm525I4PxKDG7VteC4iHqOlyVaHh5-ZZLPzlXCEsdg00ollPSnjSdrvsQBwuPB_kTscx3xo87V909fETS1f5flnhRf7ho9Zmim4NqKtq0zNj4A8qceaFjHvDqd43ntRasYYMcYA5cY-eCwRH7r-76pm6E4eByfAujw_pozrW2Tp2ryGCxtpcygBm9zmSnYnOoqmsD1YkoP92Lk8QgLEA6emc90jSDjm2J9TaO2kJwewzo6HJjuRFox0iDuBcEhxX8h5EAS9bksvFFzaAEtvZaiXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZzJK3dHi5gGLq434qSr4bWNpr9ICj0-KVqYGMhApKwkjepQ1DbZ43DfPqybQLayqMyI7s8ADLaoqES_BUV1_OqKjlcPnr7rWOU-Qvj8fLHihgNVg6kBn_9YFdBJG8vfHQVHNKmydSIInUPuy44-rIs91RiSiTnU81qvjdMpctmb3yWoaPII5B5b2PSXmur4Rx5Op4Vmi3qxtcQwnMU1GWP8KTfAv0hDLyCm7z1SFyGCdQ5PJlfPkvyh976R4mowaGpUm17VfZ3z3z2PaeITe8T2B6w9UPHNBmQtRTd431gUVAdlnb-SuNuPYWTjMDwf9KaOzuIR5LdDHOCvIs8lqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/so3Ij_uI1HCnHqrhwqVx3jvJkOBwyLtuwQkgXZNlboc-EI4dJOrgZpiuYfflfXFyMRJcrnVsnXPc4mFmLkIY-oQUam00M-GwbePeyf-MrcMSs0D21qHmHxo0znptlR1xSP6PCBDk8BtBfligzYAxp_LzG9NQxwGIdQ8piVWoJOTaKFq6NqaH70z1bNIYlHMPCeSQKGqoxYBu7GsHOpu00W-q2-quc69d1z9mSI5M8ziuXnbzIuXjIJo_pf8VYgiR-BH4BGwR9DfIIUoYyhhdkWrOe1qU2s3dep4s3ZT4aIN4Q22-lfkOsuLaTXiPyaQH-YRIn_bHXBtKGGUJZscAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUr8tI9o1AAJzPy6kJefYZ9OD9GcA6poXXht7VK4u_unZuucmv6u3jh0Dxrk4CQALKwVZikbPBEzHVZWyIM0AwchHnZLnnKmJTvP_C-NcZw-kOdiFtfouU-EaWdmMf1oeuChb8hv9pEL-W9JP_D7IGVbd7idPuC0CdFkJ3IhjixVYqcsas73szwTBVfQvGeA-h9xn0gl-dGInTnja86rBPZPTi4ZKefe3s73nbI2HeHC5aKTghdY2vy91LjGes2RGGc6APkoEKTV58N3f7H6UldRVxzqvtqOv5CvJvmV-R9m9waNzUTmzkUacDx_pxmKPOG4QcRpCDWp9mr-_Ei9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stzPJy7sz-thA67ylDYZgCEkWhCmd8BpxSrm-MO6Ze9Kuy4AEc21cgoVdzdQUjsGdYLTc4GLbtYX8CYb4Cl3v8HEcm6a0DildxJ-Ia3P_w0gqNAzIWWmqse5HasyUGYhCtkv4jafEfPipWNDAE7ljJQnbdfEBiMiR9KJlDFPW--MW4SUiODwTUn7mP4lbTzV7YfCo9GTHeDHTP00xi4tdoeAKUBClHIBM5_FQZiVWKA_r--G8FdRKMpq68GB_WpWcH55DCSLPFvVZMvFxMzsfFLm8AOpOf8XaPGDFShONU5jKoV-6EhGYXhXxLpzNFL0vlxjbbLMMlw_BPGhL5nQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjvCsJiQlc6RbD1J0iLOPIvS2_fnGx1iw5RWRb4SSLZoFwuIADvUAVDZtiBxZrg9CT48DcbR0D5iQdC6mcsT1P4SobJ6mqMttz2RQzOuBXgCg9JDLGgvw4l6R6PMKRym9u7qciWwQ0eIguzEP0Z5z8fRf666piDa4hUwZQtkAMLfoVe-VUGfQ-50JyFiMB1fkZlkFUM_Iu3vRHMAC7QfD9R-wHxh1ycocePpcW6bxUB1IHpvNK-eIDCB2zZNQsi6AWtJsAvrZ2UijZA14T-2ChH37r9LQHBK2qApDJXmSM6fhA_nAq9vYPWuFj9Ab4Da7XzKro1EWNVJatzyyVk-cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم عزاداری هیئات مذهبی رشت در میدان شهرداری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444387" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooTb1AZ_8zzdB2POyXXh3S54dC85b_UJT4YkxCWnsj2BJMfme6yd5WM54DOOU_F4pp0-cLEFHNmHrr7gfIALDF8f6Wl53Zs24DJ4grMbKpPVpUEPh4Dx5STqVQXS0-BLTozgH-Hx9FyhYXYCMtiipx87O5b5jhaH89hB3uSAaAkUcmGIaoymuU8m6aq9cch7BEDXpoB0OSrPk0gAHWnoi9us7vH0umqoW9uJKbTomYXssHz3AU8ZWD5nex4B7U7wC449_PhfbT8eM7yNq_luxk-SgQFLI6gO24gB5myi4wEKZFpgVBvBS_xqadokcEfu-3ERXyCVK8j2RsV6XkuhmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تیم ملی فوتبال غنا با ثبت یک تساوی مقابل انگلیس به مرحلۀ بعدی جام‌جهانی صعود کرد‌.
انگلیس ۰ - ۰ غنا
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/444386" target="_blank">📅 01:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444385">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
منابع خبری از حملۀ ساعاتی پیش رژیم صهیونیستی به اردوگاه آوارگان در جنوب، و نزدیکی یک مدرسه در شمال‌شرق غزه خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/444385" target="_blank">📅 01:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444384">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4588151e87.mp4?token=ePMc3ZtKkF-fxF1ql9oFVYeNhkgEaxaNVnGeKevhkyMuUH5FYVWrtyf8Fn2b3hPabGzSMpWubK1sitPMK6t8gTaYSZpDvnX_m9vct92gQyjjgz3GrvEU0bf2NT4WwhbSW_Kx-0dQQQdcII8v3QcgNgp6HhOFRwGJfULrZmsdPcdsXjKg3wqY5WroE7rcAQIX2eIiSr07MUIsZ-gqhHWkJqEkjuLw-TfGXaO2xzXp5Vrw7h90z0gExViUHjfdqJ6qXbwoJ-jzeFFumo1H7s50OXeKuaE68OIVtR2-hNNgmuUPVc3hZgbuJgGuN0C5j5I6kLiwq3IfokFtwGrNtAsJQoZud9N4siZFDMUSqv2sPq2q8jEAwuNugVt8xBbbTgk0Hgy5MI3ypuo3q9LXvo68DkYnMHcFK-RMv7gselVUAjwmC9eVO9JiqP9bmASPjLYQ_yksHMRXDwBTEhqmMi1rgvOeznyHSVsBf2HwKQ0pAGA5gp9e8yfQ0toXqz0O2w0XtVq05NKLEeYpD4zC4k_7VzyKtKKuWJ0km2CV8For8vAZYv-srIMmtXWLYrR4Lv8SKTTYYR7kt1Axx57tckk2TJ4SwqSngevPCjvOmD_EdLU95u5nItMmCPA7_kruk1KsAK6ErQ4FKRDBdK4841o0e0HmaFMDxg1n34Z8-OojOX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4588151e87.mp4?token=ePMc3ZtKkF-fxF1ql9oFVYeNhkgEaxaNVnGeKevhkyMuUH5FYVWrtyf8Fn2b3hPabGzSMpWubK1sitPMK6t8gTaYSZpDvnX_m9vct92gQyjjgz3GrvEU0bf2NT4WwhbSW_Kx-0dQQQdcII8v3QcgNgp6HhOFRwGJfULrZmsdPcdsXjKg3wqY5WroE7rcAQIX2eIiSr07MUIsZ-gqhHWkJqEkjuLw-TfGXaO2xzXp5Vrw7h90z0gExViUHjfdqJ6qXbwoJ-jzeFFumo1H7s50OXeKuaE68OIVtR2-hNNgmuUPVc3hZgbuJgGuN0C5j5I6kLiwq3IfokFtwGrNtAsJQoZud9N4siZFDMUSqv2sPq2q8jEAwuNugVt8xBbbTgk0Hgy5MI3ypuo3q9LXvo68DkYnMHcFK-RMv7gselVUAjwmC9eVO9JiqP9bmASPjLYQ_yksHMRXDwBTEhqmMi1rgvOeznyHSVsBf2HwKQ0pAGA5gp9e8yfQ0toXqz0O2w0XtVq05NKLEeYpD4zC4k_7VzyKtKKuWJ0km2CV8For8vAZYv-srIMmtXWLYrR4Lv8SKTTYYR7kt1Axx57tckk2TJ4SwqSngevPCjvOmD_EdLU95u5nItMmCPA7_kruk1KsAK6ErQ4FKRDBdK4841o0e0HmaFMDxg1n34Z8-OojOX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زخمی که التیام نمی‌یابد
◾️
روضه‌خوانی میثم مطیعی در مراسم عزاداری شب تاسوعا در جوار محل شهادت رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/444384" target="_blank">📅 01:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444383">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de08a11e6.mp4?token=QrbbA88c8WfebfP6l96qfSgOo6uFr1IGUGPJVJg9wWolNldvBqKDKYE25__E83JqP3sDIIe9KpjYADdlDy6sSn48TXfqlLO_13sTwEsIL39IBm8CzKTkjppOweEaXNla_xfSX8RuFqVoDbDO0vtgBt-xbTVvS44hp_pNOhsCbi6y2waoCxog-DOPxbdP18xFpe76q14xxsrCQXy4zpI3eVg2i6ytJGLOrnv_j-4KbvKY3JELbBfTi_2EQnt6n7-P_7k0ejhNyMrpaA1rgMJOcVQgk8Aeua_sSwxNT2dk_zA2TAHZc-VZKAW-icI8w6Fn8_PdYEYkNNEMCelKlIoaNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de08a11e6.mp4?token=QrbbA88c8WfebfP6l96qfSgOo6uFr1IGUGPJVJg9wWolNldvBqKDKYE25__E83JqP3sDIIe9KpjYADdlDy6sSn48TXfqlLO_13sTwEsIL39IBm8CzKTkjppOweEaXNla_xfSX8RuFqVoDbDO0vtgBt-xbTVvS44hp_pNOhsCbi6y2waoCxog-DOPxbdP18xFpe76q14xxsrCQXy4zpI3eVg2i6ytJGLOrnv_j-4KbvKY3JELbBfTi_2EQnt6n7-P_7k0ejhNyMrpaA1rgMJOcVQgk8Aeua_sSwxNT2dk_zA2TAHZc-VZKAW-icI8w6Fn8_PdYEYkNNEMCelKlIoaNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شجاع خلیل‌زاده: اگر مقابل مصر نتیجه نگیریم فایده‌ای ندارد و مثل جام‌های جهانی قبلی باید برگردیم.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/444383" target="_blank">📅 00:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444382">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f59f08ba.mp4?token=mx9JbwLH7hSP6WBcxF4nBA9vutfjMonE0_G7aTXklcriIWf1EkbMWBg83336yhYD1G4vKjWyURlR1ENVguCbjalieSh44Re_E550QSeowWW6kkmVgSxdmY14bSAvzi9ZhDR3oGOphphejM6dRChCpr6JJbiq--Ypmf86VDdtp1QvSceEvUMsvCIjEWhkIli6Kn7-3iwV-y4ukJ5EqfFCahXznssYmapW-IpiaHN6FygtA3ULM13zJpg99bQo2hntBRV60y9zMrMRJLwD9YzyN25QR8vhr32eSP7T86Zrdn2Pr_0szsdjYu-u7pvmTctO2rkzh4TYIZmNDLxo_vaYGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f59f08ba.mp4?token=mx9JbwLH7hSP6WBcxF4nBA9vutfjMonE0_G7aTXklcriIWf1EkbMWBg83336yhYD1G4vKjWyURlR1ENVguCbjalieSh44Re_E550QSeowWW6kkmVgSxdmY14bSAvzi9ZhDR3oGOphphejM6dRChCpr6JJbiq--Ypmf86VDdtp1QvSceEvUMsvCIjEWhkIli6Kn7-3iwV-y4ukJ5EqfFCahXznssYmapW-IpiaHN6FygtA3ULM13zJpg99bQo2hntBRV60y9zMrMRJLwD9YzyN25QR8vhr32eSP7T86Zrdn2Pr_0szsdjYu-u7pvmTctO2rkzh4TYIZmNDLxo_vaYGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شجاع خلیل‌زاده: اگر مقابل مصر نتیجه نگیریم فایده‌ای ندارد و مثل جام‌های جهانی قبلی باید برگردیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/444382" target="_blank">📅 00:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444381">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI7tCHliy1aAg5qigi0w3qML34aUBOR2eYzBHPfjk8z8YT1m_ZDUxkOIgrJTZQYZk1h61i4eUFLPH48aSuPt_tUJEE1uf3QVfAozSRtDsnF8TVU9FAtaV0WFenaWrOu94_Sv_SwWA-Xkl9Intpdr7k2USeenbOSGL_6FEsBMXV5PQfVf8Y9ESoPurCPt3qeutZ6-O_GFSs_b3cKFjfQNpS7GujG2VKf54AAUITQGKEvHSeYM_UjWBHEIYNNBSRhZ4yRZTZsLF2DXDx1_DldZmM63Qw_7cf78OG-uSJlZ8SuU3nzhX5IYYHepIk5WZ4aaLdfAbiNcrKv2M4RvR6XT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وارد مشهد شد
🔹
رئیس‌جمهور دقایقی پیش همزمان با شب تاسوعای حسینی و پس از بازگشت از سفر رسمی به کشور پاکستان، وارد مشهد مقدس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/444381" target="_blank">📅 00:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444380">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAlzHYxOEWDXcMkLmpJVV4eBWqGmlFrrxZqXBBTd9cPCJGAkZzNtYmSls5xem-QrUICJp_cXwRso5DkvmmzBez_BPXgQ4AIUGKNS0M4tEFi7Ds9kOLCp5VbnZiiDx7iHaatNgXowMVUARq6K_n1YSwnkjUMqOnqngsrUaM2Zg_FcyuOAm7DHHMic8BNurPxGoc3CcFzsGHFzhQB7JlK6QQrkHa7XL053UnwhcvONmVDW7O8z9AQ9NETesyixqCm7OoI6Pi8SDgEuKs7BAtJbmIinqC6DjwCzdr61-sxQizGq5AsNEiQ2me2mDbCU0xxChjPnsVGMT6LZFxIChgUrBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام مراکز اهدای خون تهران در تاسوعا و عاشورای حسینی فعال هستند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444380" target="_blank">📅 00:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444379">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۹</div>
</div>
<a href="https://t.me/farsna/444379" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۸ – کتاب آه</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444379" target="_blank">📅 00:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444378">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJYd0FmywUxDjy1kKj8zr51SW1hfQRFXQDfaqyJVjY8prdgJE1OUPQiR1g_BcXsDOxMNCduTTKlrYfboOdmriqiyNEyW_ihqKdfVoF5-BX7QVAoVpoCQHuXlg9Sq2psnCuiwCK8569nIc552pfZ6FfKlsuaMPODjwpU3WT5zfw_lhhqauPAWVXqVBI1xI2Y12GM1Di6BTxgePD5zV59or34z7flMjoHcqLKIzLL3bYcZS6wOx8vNXcepX6R7rreMFf5NqXrZ1oipGw3rlqUx8PGtIKErO5pjsilVqN7tsNuuY7XUqDqlADC1yyTdjgblivWk-a9pr65Kg1ZCYnBaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرق کار
🔹
روزی علی بن ابی‌حمزه در روزی بسیار گرم و سوزان، امام موسی کاظم(ع) را در مزرعه و زمین کشاورزی‌شان دید. امام در حال کار و تلاش سخت بودند؛ به‌طوری‌که از شدت گرما و فعالیت، تمام بدنشان خیس عرق شده بود و عرق از سر و رویشان می‌ریخت.
🔹
علی بن ابی‌حمزه با دیدن این صحنه جلو رفت و عرض کرد: «فدایت شوم، چرا خودتان را این‌طور به زحمت انداخته‌اید؟ پس مردان و کارگران شما کجا هستند که خودتان آستین بالا زده‌اید؟»
🔹
امام موسی کاظم(ع) در پاسخ به او فرمودند: «ای علی! کسانی که از من و پدرم بالاتر و بهتر بودند، با دست خودشان روی زمین کار می‌کردند و عرق می‌ریختند.»
🔹
علی بن ابی‌حمزه پرسید: «منظورتان چه کسانی است؟» امام فرمودند: «رسول خدا(ص)، امیرالمؤمنین علی(ع) و همه پدران و اجدادم. کار کردن با دست و کسب روزی حلال، سیره و روش پیامبران، فرستادگان الهی و بندگان صالح خداست.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444378" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9803e13ea.mp4?token=dTfyrqAgosSPC38kB053v38xgJdtboIkpO_PRPj3LQCJVefVE8aNBm77pWUX4cX2Hg2-Pppxo0gx5BOqPFv46GgvD8_VDJLVxUYwPc5brz3N-Mjoi3n6VCJP6MWNFhCztHWpUmFdQdxM7rhH0-AFZ574XK3rV9-hmf1rg_am63uFF-I-8WdZiSV9GtfzygSHby0UYhPvtPmz7TTmC9p-6_rkCzuBdUMvC1LFIWz5ptwOu6JsiHyXkynJN8Nl9AEOC8JA6DNRgubJldMdhYdmhhKObbPEsTGNkr4zeMpNm1s8VoVU9Kl_ymLMKLIvR_b4ZIgnAjC808EHKQ0bT-leeiD1jkEWD7WBqJtlOXh07uGw2bUerOXLB9gNpcnmzqck3AMgOxIKiO9FWRbwCV-bvZPruzR-tDyFpt3a6glmMRSLrEcMEblWaglbhpc3Pd_0LLtGFm56t7TCp3PjDCqQU_j8MUTwyjp5ZUWqiy5ViID8iZwluvscPTGXRDgFnNdx0U2wPHp0R1Y9xXi4YKRAiIl29GdC3Mu0Zo53ks2IOKrnN1KNc6o6Sm7XQxiI8y0BLeJcdFW3KLNkHO_BBZxJ8AKFQzLOI0lJ3Wiquaki4db_Cqh37rwwVN3GQlWU51bhfRtO6L-l0AVxwmCOTSrtOp-q-ZeN0EAdd0CiGvVqG0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9803e13ea.mp4?token=dTfyrqAgosSPC38kB053v38xgJdtboIkpO_PRPj3LQCJVefVE8aNBm77pWUX4cX2Hg2-Pppxo0gx5BOqPFv46GgvD8_VDJLVxUYwPc5brz3N-Mjoi3n6VCJP6MWNFhCztHWpUmFdQdxM7rhH0-AFZ574XK3rV9-hmf1rg_am63uFF-I-8WdZiSV9GtfzygSHby0UYhPvtPmz7TTmC9p-6_rkCzuBdUMvC1LFIWz5ptwOu6JsiHyXkynJN8Nl9AEOC8JA6DNRgubJldMdhYdmhhKObbPEsTGNkr4zeMpNm1s8VoVU9Kl_ymLMKLIvR_b4ZIgnAjC808EHKQ0bT-leeiD1jkEWD7WBqJtlOXh07uGw2bUerOXLB9gNpcnmzqck3AMgOxIKiO9FWRbwCV-bvZPruzR-tDyFpt3a6glmMRSLrEcMEblWaglbhpc3Pd_0LLtGFm56t7TCp3PjDCqQU_j8MUTwyjp5ZUWqiy5ViID8iZwluvscPTGXRDgFnNdx0U2wPHp0R1Y9xXi4YKRAiIl29GdC3Mu0Zo53ks2IOKrnN1KNc6o6Sm7XQxiI8y0BLeJcdFW3KLNkHO_BBZxJ8AKFQzLOI0lJ3Wiquaki4db_Cqh37rwwVN3GQlWU51bhfRtO6L-l0AVxwmCOTSrtOp-q-ZeN0EAdd0CiGvVqG0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام سردار موسوی به خانواده شهیدان جعفری
🔹
این خانواده پیش‌تر با تأکید بر گذشت از حق خود، اعلام کرده بودند تنها خواستار گرفتن انتقام خون «رهبر شهید» هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444377" target="_blank">📅 23:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444376">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌ سنای آمریکا قطعنامه‌ای علیه جنگ با ایران تصویب کرد
🔹
سنای آمریکا قطعنامه‌ای را تصویب کرد که از ترامپ می‌خواهد عملیات علیه ایران را متوقف کند، مگر اینکه مجوز کنگره را دریافت کنند. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444376" target="_blank">📅 23:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444375">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e70b355a8.mp4?token=p-Yggdq3UIxaeprmTiSko43un4oAZMYvV16kMYA4FSQYsyJUUEWu0mgI4NbXpa6hu0YnyZCcwGX-kpinzJO2DfDwY_zeTNUNlutfZrE92zkBA9nrz2oJQazyj5bPUj8vk6AkB3rQib1BVxEKfrJ_hCEJYdJRHO3xwo48hiW8YGugPrVPpO2BayFBrqtDolY9cQnp5OlG2ONQp3DqBR2BnCumxomePqaIK2Bu5iwQtdcrD7rIeiAqEUjAvkIuWjlEzTj1XWdK4fQ4zk9bUf46D6OkO-94Wa5Lh6OVOoTxSPi2AtZtNSeFsINlxxAHgGlCZRKdiaoQzz8jDoo6BRkMfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e70b355a8.mp4?token=p-Yggdq3UIxaeprmTiSko43un4oAZMYvV16kMYA4FSQYsyJUUEWu0mgI4NbXpa6hu0YnyZCcwGX-kpinzJO2DfDwY_zeTNUNlutfZrE92zkBA9nrz2oJQazyj5bPUj8vk6AkB3rQib1BVxEKfrJ_hCEJYdJRHO3xwo48hiW8YGugPrVPpO2BayFBrqtDolY9cQnp5OlG2ONQp3DqBR2BnCumxomePqaIK2Bu5iwQtdcrD7rIeiAqEUjAvkIuWjlEzTj1XWdK4fQ4zk9bUf46D6OkO-94Wa5Lh6OVOoTxSPi2AtZtNSeFsINlxxAHgGlCZRKdiaoQzz8jDoo6BRkMfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان جمهوری یاسوج غرق در سوگ علمدار کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/444375" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444374">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJwaaMSeMmrj0hTayKb5ODREcJEGhsxgBkAHq1Jb7ZaZPCgbVn9CZ98cJkAwgYDeSaqO1O3NGlVvt1Hc_s6Wm2IL7wMLgb3nhitgN4gATskFdndUQvpURJlYw1JlyoZwkx6tmEyc5GyJh07b4HA_iULtkL0BlgMT47tt1Z5_ZRKu-opOAUvN6qvpYfth4uefqeLPVhL7PWsFrbNkbkOXiHemNHqWEC19N2tvjtQs79eT4sCaIavvdbCS7-f2lVOWiMlrHdNo51lGb8gLZPJEMBwusJrPeoHr_-RSvk14lEwGIbQq6RB3uaHLEjnTnfKVDFpGA2o4BPoT6jG9JeNxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری اسکن ۶۰ ثانیه‌ای بدن جای ام‌آرآی را می‌گیرد؟
🔹
شرکت میدجرنی از یک فناوری اسکن تمام‌بدن اولتراسونیک رونمایی کرده که می‌تواند در حدود ۶۰ ثانیه تصویری سه‌بعدی از داخل بدن تولید کند.
🔹
این سیستم با عبور بدن از حلقه‌ای از حسگرها، تصویری سه‌بعدی از اندام‌ها، عضلات و استخوان‌ها تولید و سپس پردازش می‌کند تا نقشه‌ای از وضعیت داخلی بدن ساخته شود.
🔹
با این حال، متخصصان هشدار داده‌اند که این فناوری هنوز جایگزین روش‌هایی مانند ام‌آر‌آی یا سی‌تی‌اسکن نیست و ممکن است در مرحله تشخیص، خطا یا تفسیر اشتباه ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444374" target="_blank">📅 23:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444373">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd0156436.mp4?token=Tg3qsrm--Tx8xjUjBgJL7DSySvM-XSuFhYL65TuyUVFdO1CDVmbgrT7YMcO9PSC3MDJo575i7bdLn5FCC2-f5N5nH-COaCgMW1PtzKlCNFxMUc68sFS4viRzqyTAsWVnqG9Hgs2yLzmdOu-LFpLlnjBJE0yCtqxFO3txtGZ_MBsVIaN4LKB9FlBwYQk1lKRxBCYhoxvOiX724izniVklbJ9Gs3fEH4oKYFd_vNHlvHui9heg1ZmgLVA07SPoDZxMRH3l5SQGdVzxRGtR8JiQ54HodVxgTmxNkTKq_0wvqvQjWSVoRGA84-7N4FBm9Ehv_LNPas7eiCRqdo5phB9-Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd0156436.mp4?token=Tg3qsrm--Tx8xjUjBgJL7DSySvM-XSuFhYL65TuyUVFdO1CDVmbgrT7YMcO9PSC3MDJo575i7bdLn5FCC2-f5N5nH-COaCgMW1PtzKlCNFxMUc68sFS4viRzqyTAsWVnqG9Hgs2yLzmdOu-LFpLlnjBJE0yCtqxFO3txtGZ_MBsVIaN4LKB9FlBwYQk1lKRxBCYhoxvOiX724izniVklbJ9Gs3fEH4oKYFd_vNHlvHui9heg1ZmgLVA07SPoDZxMRH3l5SQGdVzxRGtR8JiQ54HodVxgTmxNkTKq_0wvqvQjWSVoRGA84-7N4FBm9Ehv_LNPas7eiCRqdo5phB9-Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی شب تاسوعا در حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/444373" target="_blank">📅 23:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444372">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRkgIe4pE6L7AeziQdHiX8FhYbh8KTlVz_MOwE3anIQVk9psrf1McK0c5H7kYBnnVqHW7sNvVqSj2c8iEZb8TO2XpqSChQIUPthkNTo-e7i5QMs-W6vEKx2zdkjmhSgODBfvOfmkp-pk4Oz5Cc-zXt4ICR9B_vsPBNt0xsZGhmab-Pu98G8gBcTClTyBJtJs8fnaJjHTJ3Uwj4P-N7AzGRKEpsj7eXLqZC6CUyMuLWtUir-TVZOyLxqtQPrfawEM3aEhlxE9Lu6mlggLWmSs7tdW0PLtl9ka--mJLn0BP-yCgKJm8AbquoECGS3evIGXsAbIfm_CxB6xhsgtbpxjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای ونس! تعجب چرا؟ ما با تروریست‌ها دست نمی‌دهیم
🔹
مو لای درز پازلی که طراحی کرده بودند، نمی‌رفت. تیم مذاکره‌کننده ایران را به بهانه بحث و گفت‌و‌گو درباره تحقق شروط تفاهم‌نامه و ادامه روند مذاکره به سوئیس کشانده بودند و با تدارک برنامه پخش زنده در محل برگزاری جلسه، خبرنگاران را به صف کرده بودند برای ساخت روایت جعلی مدنظرشان.
🔹
می‌خواستند با راه‌انداختن بساط عکس یادگاری مشترک با چاشنی دست‌دادن و لبخندهای رو به دوربین، تیم ایرانی را در مقابل عمل انجام‌شده قرار دهند و با پمپاژ خبری سنگین رسانه‌هایشان، ختم ماجرای خصومت میان ایران و آمریکا را به دنیا اعلام کنند ولی پروژه روایت‌سازی‌شان در نطفه خفه شد.
🖼
اما چه اتفاقی افتاد؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444372" target="_blank">📅 23:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444371">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اختلال خدمات بانکی تا پایان امشب برطرف می‌شود
🔹
رسانۀ بانک مرکزی: اختلال خدمات کارت‌محور همه بانک‌ها به‌جز بانک‌های ملی، صادرات و تجارت برطرف شده و خدمات آن‌ها به حالت عادی بازگشته است.
🔹
تیم‌های فنی و متخصصان امنیت سایبری همچنان درحال رفع اختلال سامانه‌های…</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/444371" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444370">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
تکمیلی | طرح پایان جنگ ایران برای تصویب نهایی به رای گذاشته می‌شود
🔹
این طرح باید بار دیگر در سنا به رأی‌گیری کامل گذاشته شود؛ در صورت تصویب نهایی، به مجلس نمایندگان فرستاده می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/444370" target="_blank">📅 23:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444369">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e95e00f67.mp4?token=MW3McprmsAgjnqKCwAD_7iSsBJzdZrh-PmaYWJmq9JyNywJzGDeLEPHFbt8K8IeNZHjkJmiUQSTF7FKykv8OL-78YpmC-fjmtaBQY6G_EFWsiOAL8gsSqe86a0CoW7rnkyApp9-PefT_NpwlID7MEgO10YDI_hwMZ8a8TgsrWcetCWxzRaabABdh5rzozf8QbqcdHcY3U_g6rHSdrPZ3wcKlSBk7nvY219ZlNREukRJEamapSdFbFnBPZP9wM-cZCQMx7gXCFJhfXncbZQT5SHoArr0ej7CNB0rgreqlW524pEbqzHeGjUDUI8BOQ2fDtuIBlhzbC0Hcb4fJi_RIiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e95e00f67.mp4?token=MW3McprmsAgjnqKCwAD_7iSsBJzdZrh-PmaYWJmq9JyNywJzGDeLEPHFbt8K8IeNZHjkJmiUQSTF7FKykv8OL-78YpmC-fjmtaBQY6G_EFWsiOAL8gsSqe86a0CoW7rnkyApp9-PefT_NpwlID7MEgO10YDI_hwMZ8a8TgsrWcetCWxzRaabABdh5rzozf8QbqcdHcY3U_g6rHSdrPZ3wcKlSBk7nvY219ZlNREukRJEamapSdFbFnBPZP9wM-cZCQMx7gXCFJhfXncbZQT5SHoArr0ej7CNB0rgreqlW524pEbqzHeGjUDUI8BOQ2fDtuIBlhzbC0Hcb4fJi_RIiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع اقتدار عاشورایی مردم ساری در سایهٔ پرچم قمر بنی‌هاشم(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/444369" target="_blank">📅 23:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444368">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6789ddf31e.mp4?token=X2MfKNTGuvGOHWi_3kZHECWQpLEhBdBNHxPEbLKEGF4kA5K53rPlQ7ihieAdyVQoymHseFisfpjtd2g42mWce92YONnuIzFERtaxEHsh19_aOA63oWRk6f3uj2fx1WMPm_kTelCNf9xWThrC1iEvIP7FZoPkeI0QKlat7Oib2Uqy3QqdkxX6lSoHSMQNKYcdkC5cWm1M1gIxporq5ftsosuIFdUqfQgbmOtJSl-KG5a_2xqaxnQuhxJqLfXr7kabrGpQyGrXPz1xOIFcSh0oGmfa46zpcN5GkzERa2jLXjzOwJqdjz8OC6GY3tBDLGPsAb4o6YraMx0gWuMfw6EsvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6789ddf31e.mp4?token=X2MfKNTGuvGOHWi_3kZHECWQpLEhBdBNHxPEbLKEGF4kA5K53rPlQ7ihieAdyVQoymHseFisfpjtd2g42mWce92YONnuIzFERtaxEHsh19_aOA63oWRk6f3uj2fx1WMPm_kTelCNf9xWThrC1iEvIP7FZoPkeI0QKlat7Oib2Uqy3QqdkxX6lSoHSMQNKYcdkC5cWm1M1gIxporq5ftsosuIFdUqfQgbmOtJSl-KG5a_2xqaxnQuhxJqLfXr7kabrGpQyGrXPz1xOIFcSh0oGmfa46zpcN5GkzERa2jLXjzOwJqdjz8OC6GY3tBDLGPsAb4o6YraMx0gWuMfw6EsvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
سیدعلی خامنه‌ای کشته دین است
◾️
خون‌خواهی او نصرت این دین مبین است
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444368" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444363">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/444363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
| شب تاسوعا
🔗
سایر مداحی‌های امشب را
اینجا
گوش کنید
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/444363" target="_blank">📅 23:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444362">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/444362" target="_blank">📅 23:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444360">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb48d4884.mp4?token=PYnfV0Q-7IosrqltcDRFc-rv4XPtKARl9yfL7uK0dd-fOfe70mupkH0vPoX3aWNLwwWgda6LqYFZs32RF0c61JTxpv27CwpQ1MiwKcehJc1rKukyvXFcNu8fBzgIPQUdAHZtpb6s30L2dSSQ-Cmoj5vQn2LrYwlsNtklwdALRFcZ_ONEc3Tr5CO5oBd4EpiHHpzOB4QeXN3WEA4ZtX2KOjhXfMAXc4WFwHmbY5_qxs2Wt1_DL6x92eYhT7ZJU2-2x9VvSJ2CQmfqnlMrnxrAe-fmY09RRgfeu69Nbo6BXSv9L7TEFPPDADaHo93FVsIIYQmvNdQWh99JUMrX5edoCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb48d4884.mp4?token=PYnfV0Q-7IosrqltcDRFc-rv4XPtKARl9yfL7uK0dd-fOfe70mupkH0vPoX3aWNLwwWgda6LqYFZs32RF0c61JTxpv27CwpQ1MiwKcehJc1rKukyvXFcNu8fBzgIPQUdAHZtpb6s30L2dSSQ-Cmoj5vQn2LrYwlsNtklwdALRFcZ_ONEc3Tr5CO5oBd4EpiHHpzOB4QeXN3WEA4ZtX2KOjhXfMAXc4WFwHmbY5_qxs2Wt1_DL6x92eYhT7ZJU2-2x9VvSJ2CQmfqnlMrnxrAe-fmY09RRgfeu69Nbo6BXSv9L7TEFPPDADaHo93FVsIIYQmvNdQWh99JUMrX5edoCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ پرسپولیس و چادرملو در دستگردی
🔹
با اعلام سازمان لیگ، دیدار پرسپولیس و چادرملو در تورنمنت تعیین سهمیه آسیایی، ساعت ۱۸:۴۵ جمعه ۵ تیر و بدون حضور تماشاگر در ورزشگاه پاس برگزار می‌شود.
🔹
برنده این دیدار ۸ تیر به مصاف گل‌گهر سیرجان می‌رود.  @Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/444360" target="_blank">📅 23:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444359">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408f212365.mp4?token=a7GCF6eX1HGNGIrkOqQ5hiUICkOgVESo4pkdJjN9wCJI5MO0C1l6V2rXFDfy2M7g-_DWq01HvhiGsXPlCVPxMMDWJSk01Q93FXAj-Q6JHfWyAXOWGHEsT7TD1Fb5a5fllExp-3hNgWpNDroINnTHMPn4M96Y8dWVXaAZprY-TjgnWXQi1euVxd1wwyDxR3PGH6-s6z02Ytd2kpWvD19oWJiUUVITM8qIKu7YRH1edJWNdti8IK342gx19PK-ntJgxbUvVusc2U2p14k7clCTfYAdewEl-gvLbYrCxKNBxWdVLo-c-4DjSVWKo4OiItpxn8z0VImR58DlYUfBne2wdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408f212365.mp4?token=a7GCF6eX1HGNGIrkOqQ5hiUICkOgVESo4pkdJjN9wCJI5MO0C1l6V2rXFDfy2M7g-_DWq01HvhiGsXPlCVPxMMDWJSk01Q93FXAj-Q6JHfWyAXOWGHEsT7TD1Fb5a5fllExp-3hNgWpNDroINnTHMPn4M96Y8dWVXaAZprY-TjgnWXQi1euVxd1wwyDxR3PGH6-s6z02Ytd2kpWvD19oWJiUUVITM8qIKu7YRH1edJWNdti8IK342gx19PK-ntJgxbUvVusc2U2p14k7clCTfYAdewEl-gvLbYrCxKNBxWdVLo-c-4DjSVWKo4OiItpxn8z0VImR58DlYUfBne2wdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آیا تکذیب‌های «منبع آگاه» در برابر روایت‌سازی ونس، بازدارندگی دارد؟
🔹
مدیر گروه سیاسی خبرگزاری فارس: به‌عنوان یک خبرنگار که سال‌ها تحولات سیاست خارجی را رصد کرده، این سؤال برایم جدی است: آیا تکذیب غیررسمی برای مواجهه با ادعاهای جریان‌ساز معاون رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/444359" target="_blank">📅 22:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444358">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هک بانک‌ها در روزهای آرام، کابوسِ محقق‌نشدۀ جنگ
🔹
اختلالات گسترده در سامانه‌های چند بانک بزرگ کشور طی روزهای اخیر، نه تنها روند خدمات‌رسانی به مشتریان را با چالش جدی مواجه کرد، بلکه به دلیل وابستگی سامانه سوخت به برخی از این بانک‌ها، موجی از شلوغی را در پمپ‌بنزین‌ها نیز رقم زد.
🔹
این حمله سایبری که از سوی کارشناسان تأیید شده، این پرسش را دوباره زنده کرده که اگر چنین رویدادی در دوران جنگ تحمیلی رخ می‌داد، چه پیامدهایی برای کشوری که بخش قابل‌توجهی از مردم آن در شهرستان‌ها و دور از خانه‌های خود به سر می‌بردند، به همراه داشت؟
🔹
بی‌گمان فشار روانی و اختلال در دسترسی به خدمات بانکی و کارتی، مصیبت‌های جنگ را چند برابر می‌کرد.
🔹
براساس اسناد و گزارش‌های منتشرشده در خبرگزاری فارس، در آن مقطع حساس، مسئولان وقت با اتخاذ تدبیری هوشمندانه، دسترسی به اینترنت بین‌الملل را قطع کردند. هدف اصلی این اقدام، بستن یکی از مهم‌ترین گذرگاه‌های حملات سایبری و خرابکارانه دشمن بود تا خدمات حیاتی و زیرساختی کشور، از جمله نظام بانکی و سوخت‌رسانی، با اختلال مواجه نشود.
🔹
در آن روزها، شماری از رسانه‌ها و فعالان فضای مجازی، این تصمیم را به بهانه‌ی جلوگیری از اطلاع‌رسانی، رد کردند و آن را فاقد توجیه فنی دانستند. اما اکنون و با تکرار الگوی مشابهی از حمله سایبری، واقعیت آن تدبیر دفاعی بیش از پیش عیان شده است.
🔸
با این حال، تأکید بر این اقدام به معنای نادیده گرفتن ضرورت تقویت زیرساخت‌های دفاعی نیست. کارشناسان بارها هشدار داده‌اند که باید توان سایبری کشور به سطحی ارتقا یابد که در شرایط بحرانی، نیازی به محدودسازی شبکه نباشد. اما در شرایط جنگیِ تمام‌عیار، هر اقدامی که از فلج‌شدن خدمات عمومی و سوءاستفاده‌ی دشمن از خلأهای امنیتی جلوگیری کند، یک ضرورت غیرقابل‌انکار است.
🔹
اکنون و با فاصله گرفتن از آن روزها، می‌توان قضاوت دقیق‌تری داشت. تصمیم قطع اینترنت در جنگ، نه یک اقدام سیاسی که یک راهبرد دفاعی برای حفظ معیشت و امنیت مردم بود. درس امروز هک بانک‌ها، راستی‌آزمایی همان تدبیر دیروز است؛ تدبیری که اگر اجرا نشده بود، آن روز در اوج یک جنگ فراگیر، شاهد فروپاشی خدمات ضروری کشور بودیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/444358" target="_blank">📅 22:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7becbf5b47.mp4?token=VYowFw1YmidXlJ3rWLeA3inEYbiK5s5HK1qozoMMS6yLjebp3IWTQGJJI_JriYJLKmLzNqBTppgWPKjB6OJ6gWNXogarqhwYLPqjneBtOYDBW0Qu1RG_5XdsAB0DmKPHmsekZmaQqnVtlBEl04LhjrGAqTP9u7KiiOGCqL2vMl2MPqY8mlAKU6nRauL8Rrr6VGtMWMaXnchqrltRxy7-Fcsh034bpwUHEvpfTZLPQuS9mxT9hoJZHCwydebDR-k_VYJFbZtAJt7Zzv1foilsT1n8FDe4H-LKSHBtqb_c0agreY6WG2ns21k4prjYo4Nf26nm8SYM1eFMUa5MIh5ENA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7becbf5b47.mp4?token=VYowFw1YmidXlJ3rWLeA3inEYbiK5s5HK1qozoMMS6yLjebp3IWTQGJJI_JriYJLKmLzNqBTppgWPKjB6OJ6gWNXogarqhwYLPqjneBtOYDBW0Qu1RG_5XdsAB0DmKPHmsekZmaQqnVtlBEl04LhjrGAqTP9u7KiiOGCqL2vMl2MPqY8mlAKU6nRauL8Rrr6VGtMWMaXnchqrltRxy7-Fcsh034bpwUHEvpfTZLPQuS9mxT9hoJZHCwydebDR-k_VYJFbZtAJt7Zzv1foilsT1n8FDe4H-LKSHBtqb_c0agreY6WG2ns21k4prjYo4Nf26nm8SYM1eFMUa5MIh5ENA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما خودمان را بدهکار مردم ایران می‌بینیم!
🔹
صحبت‌های یک جانباز در حسینیه معلی شبکه سه.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/444357" target="_blank">📅 22:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444356">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b7f3a95d.mp4?token=Zd6v5JEgunsjEA51JA-d3eQ96ZXjqQMQTeMpoBcXGk1lazbXMKl8pHyHARRDWdhXWbnqUkyW4VPMjwjQxpCLO2nyQY53Vm6dVBwEKePu_vH1M8I94sb8CpEocYdfIDMHoQmPZJNU0voD7zaIFvH1K5LojRhcGIToF0nZas1uB97U21Ilr5Y1T0Q7999Th-wVjQMJh-P3K_Blfhn3OFXTBJRyn-b32auLav3OuOpEWEDsRBBO1Pit8SsF3fO3fe5h5EzvyyenFmhu4ioedpkm6d3DEPrWBJRmwSpH81KvZnNBV4074uI7qKAeIVKazEZF2O-zqqEgq345NkWgO6pY-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b7f3a95d.mp4?token=Zd6v5JEgunsjEA51JA-d3eQ96ZXjqQMQTeMpoBcXGk1lazbXMKl8pHyHARRDWdhXWbnqUkyW4VPMjwjQxpCLO2nyQY53Vm6dVBwEKePu_vH1M8I94sb8CpEocYdfIDMHoQmPZJNU0voD7zaIFvH1K5LojRhcGIToF0nZas1uB97U21Ilr5Y1T0Q7999Th-wVjQMJh-P3K_Blfhn3OFXTBJRyn-b32auLav3OuOpEWEDsRBBO1Pit8SsF3fO3fe5h5EzvyyenFmhu4ioedpkm6d3DEPrWBJRmwSpH81KvZnNBV4074uI7qKAeIVKazEZF2O-zqqEgq345NkWgO6pY-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری جوانان دزفولی در سوگ اباعبدالله(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/444356" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444355">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mepnykBtGINTT91__xlXV-eV78rcqfOWYvbfPdLfLrJ7PghWMEo-iDER1C2jqKojJXoXfOWBWkT8ncEZNYn70QpxkRjKfJJaWwlgPxsjetV-bLu_PDqDx9aay6WZhNp86E_K2_ibCAtYH8PYKDNEp30FJNxsXKx2h6Z8oieTQxo_SNYehuEPebLPncdgd8efFClMpO9bMnNqOA4mlTtcMQMLBiX6GypWxqI0xnS2OnJVn_nc_nFCPHFCFGSJUkHXsO1y_hw6QBGCJRywYFpKfjin4IWfpjz7ITTbVD0LdHHeTQ2lgmkb5lw2Mx-ohA4X2bYdfigl0cPeGEv1ufFJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل زد و رکوردشکنی کرد
📊
🔥
کریستیانو رونالدو با گلزنی مقابل ازبکستان به اولین بازیکن تاریخ فوتبال تبدیل شد که در شش دوره مختلف جام‌جهانی گلزنی کرده است.  @Sportfars</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/444355" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444354">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
آقا! تو اما نبودی...  لحظاتی از دومین شب مراسم عزاداری حضرت اباعبدالله الحسین(ع) در جوار محل عروج ملکوتی قائد شهید @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/444354" target="_blank">📅 22:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444353">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c94f64cb48.mp4?token=XZao0AaWmid2b7j3N3FaxZTXygauhrLzHwylV13B6fNBedF7x28KJUGgo9DOTAVQ96KTBFg72iSf0lmeFT62ESKgbIg_GmXaGcpG2xW3Fxc9CxRb_ovvm7z9g9HoAN8dZwBTrgKfZ8toZOVRp4ObwhJMUUyIVrtr-4EyPoAjUA9kZh2at_wRPxdMRI9GZhTDJs0V0U6Z1hZsiKfOOlW77S3YIVlNyfmst9a-8LOtY9NbNuk2mNbVGal4nnoYEwrTTcuiuUHIltKL6Q9b8kGReNyRq1BDEO7onPpm33lsK4SnEIqjlkH9L-io_wABjRwd8t3XfA76r_yAtu01jdvxgCXUA0LPjwL7nsLlK-D2qDv-DyVQSYBPrxOsPwYvW6FZzxDI_3iuNkfZUWTU_lUPED4iCjPODxpj59-GVvolCT5tmfJXBc_bJzUgdIkv09tgaFl4-pmWVlq1TxBMZTQD-fpWZ7Mu-t2yaC4eyHXZPfyWzRdkZXJ9KcPoxM5YLdM0KY0NhO73TspGN0z2Jdhtr4qwaIwdYlK_kklutTzfZ47YbtVN0S0kjsKYGcHNb5CeGalSJw9u4GhFZFpon3dsFYPI-Q6Ylrpg95xoP5EKnu3ElBbzceCJk5zdczNN9naeW-GqNHrmgXF__1Usy_x59oVCZh-2_WIir1gfRrf49Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c94f64cb48.mp4?token=XZao0AaWmid2b7j3N3FaxZTXygauhrLzHwylV13B6fNBedF7x28KJUGgo9DOTAVQ96KTBFg72iSf0lmeFT62ESKgbIg_GmXaGcpG2xW3Fxc9CxRb_ovvm7z9g9HoAN8dZwBTrgKfZ8toZOVRp4ObwhJMUUyIVrtr-4EyPoAjUA9kZh2at_wRPxdMRI9GZhTDJs0V0U6Z1hZsiKfOOlW77S3YIVlNyfmst9a-8LOtY9NbNuk2mNbVGal4nnoYEwrTTcuiuUHIltKL6Q9b8kGReNyRq1BDEO7onPpm33lsK4SnEIqjlkH9L-io_wABjRwd8t3XfA76r_yAtu01jdvxgCXUA0LPjwL7nsLlK-D2qDv-DyVQSYBPrxOsPwYvW6FZzxDI_3iuNkfZUWTU_lUPED4iCjPODxpj59-GVvolCT5tmfJXBc_bJzUgdIkv09tgaFl4-pmWVlq1TxBMZTQD-fpWZ7Mu-t2yaC4eyHXZPfyWzRdkZXJ9KcPoxM5YLdM0KY0NhO73TspGN0z2Jdhtr4qwaIwdYlK_kklutTzfZ47YbtVN0S0kjsKYGcHNb5CeGalSJw9u4GhFZFpon3dsFYPI-Q6Ylrpg95xoP5EKnu3ElBbzceCJk5zdczNN9naeW-GqNHrmgXF__1Usy_x59oVCZh-2_WIir1gfRrf49Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علم عباس(ع) بر دوش مردم سرخس؛ ۱۱۵ شب همراهی با انقلاب
@Fatsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/444353" target="_blank">📅 22:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444352">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVG_Orf3XV3hi0vA4cdGUsN3FwP-nra0638RK2Jg93QKeOiBy8gjg4Qzi9wOEcp5rp8SnCzDIdLPBY_PPHseHSpKLpWhoBJaUPHeQQRg2TznnpqCRARuLqC4N-dzJ5OCG8X9bS7cDe0gtGAtd1V-uc_c5dFUgGVuu9lcRThvcvqZ148jVyIiuHwEQesMA5S5vC4jXMtECVg3oObiLJMgsy4O0zlSleZcxB20242zroa8jjIzD9MYSM_gMEORIadnHoSxwB3KyFlT3IH5GJ3O7M3JzLJb3GmVWex_JUjrYDF__6qaEPnz19H0uH99NBO-5TfKL6xmv75zX7Tk--S4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پربیننده‌ترین برنامه‌های تلویزیون بعد از آتش‌بس
🔹
طبق نتایج نظرسنجی مرکز تحلیل اجتماعی متا، ۴۵.۴٪ از مخاطبین وفادار تلویزیون در روزهای پس‌از آتش‌بس، برنامه‌ «من ایرانم» را تماشا کرده‌اند و ۴۵.۲٪ مخاطب برنامه «به وقت ایران» بوده‌اند.
🔹
همچنین طبق این نظرسنجی، برنامه «گزارش ورزشی» با ۱۱.۸٪ مخاطب، پربیننده‌ترین برنامه تلویزیونی در میان افرادی که مخاطب همیشگی تلویزیون نیستند، اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/444352" target="_blank">📅 22:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsrxH0ONkvBn0ZXCrVErKoN6EwTPsKFmPonN_Ww33-DwC1Mrm2smtDr_bL8XGwt96C-gQrFukUurszI3d6oWDuYfqIXd2pwwW2CjuSE0XmuK4AdUzm9bgzqqL-7H1tWaZc-MWNSF2nE9-YbPM7d5cbIAzk2ChfcymfaTnR-RrT9N3_tdxB4ADkKwY4SAqW8KnIbuSz1CR6iy2rLQJkY7Y--4MGHesII8g0aXxh7yztwsVH_DNVSIPgDC_ESl8ESBzzOT3tKngfxOBnk0eiNjrQnI5JbTM40VoZdaBh59BoZitOkqIrB6xpwDzhifdgGfG0xYSox11rb69RegBYSVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXtwwic8ZBWD-Qw8RXJ-hV_E9bdhg_xPRwMPnA9M1sB9xI59ack_GyBZji_fMgWKfijJu0RTrLO4Hr6cWkA6j-YAM9VYIqbVBRUKoYWL3UqBygzzwhLw0YP4uOerjrmERg88jtuM7c1maofzIhSSILv3qyCpHyqT2lkUlhx0R-FSfN_D9HYuC2XWYVAArH1c8vpjMo9wnAvSEKCIKcN8ceOyT5uJN60diWdK-7N9oeHho7nIqoxHe9ym4SiBaQbQCu28HX_Bg8_WgbXLm6c__8XkYz9dypdlhKl4Fw-gvS4G06eX7serWCQDSOxThPsNzcTeWhJmhd1NrraYDfMF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKyTuaLpo6cnftSU3IIuZXAvqXxO9mD-eE9w23iw1OUhrW9uyGHYGqby6HVnLQndeToS0h2NxFc0ARniy2296rEprHR0-K9vlpx4p4GNKfD8zg5L7pPjzBcfGLXTeAfMOANMWHcfdwnKtMbcfCgHLtLl4WoCoJdXQxdBWEMxM-wMd29X-0H3eWtxjdwHbj5Xtt6N0ctD0-NnAbAnU3B0IGrUZRihNfBaJNQppaQQ5nT1Zl6A_rtxqAJh4ssXlUv3LXYsYX71-_Iluof6mtdT1S_MeS2s9Swmlw6x4dpZ89n-c52Bhlw6m89NdGNPcNHeV42AfAVNRCzS9VDArZubdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVLFEVGKTpnlKZtNguMl7MIIlOFu23x0CytyIspSAbJXFE1Tyt4LlLceUvKEPPalONfCQpHEclwUL_a6Dg6SWeBGhXgR0HKYpRtziNFl11NupjTbXAVCb4WFYcOZCDPk3cCDB7oLgAT2On1bh5H-Ir26nrVIoNgRP5dWByHihK-07Shz6S-wx0xsfpAaZRbg22SSDKaLQh_uFaHxNvGV-ifQXUNMUrGDBS9JClshpVudEk3pFGIPR0i2qEyo7CHATPpJmETCQtOQdDyAH3KgHrgHsmFssM3HkCb7XUBlBFmOpUv5ZP4txK68WT_QwXKyqqQJ3grE0zLJac6xpPFwDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpVjNAZXJX6OWvzB-19BYSnJw7fT7KJt3vXTX3MQG0TpOs-Nes24N3K4hQv47auz2fSNH7WaSXFQ90zSRjy7I2mkQzrduJ1Qw5idKQ5aTggyCTDJjV60S0iRCZ-k6HSgwXeIX6KkLWYcj0H8kCygN73z0TeudvvlcP5yt2ewHwvzkFyWfTTIZKFJRHG1z6EmlVx4qm77UmlPwAwzDocnILgJ-LM9Dq2nrbaL9GC-VQlPFjxCjlGjOgCrEceT9ejd3xSQHqNpwjlUUKKmmoSABqLmsw5J1OK_Fknfx_Rmdud9wXnmHEsqXR0S03iiZ5sxnkAExov_gfdeK9UwkitBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePyI2iV5gFB7_84VM3n8vN0I27Qx_1CAkWgL0thHd2LlLg5Pl8YJxu0T0qVFPx43L_4YPxDu4lYciTHPdNA_CMdg_VMrQZtuML9wMkMjBn0TJfCkEjj96jqLD4SgzTiq6MMSrSZRfWUqt_60iAW4PWX71ZtOMWkH5E6LUSEuQILq8wYWit4NlUXvX1soy7FsuLou-oEq50clyRmLIZOIuC2dq5xSeoKX1BZh1IdYtaP1eA9bMbghqnzfmGcQhu-H6RJKMHSlg-dhTR2bhl0z_RloeElGZnleTDHw0nH-dRkgN8X4yl7bXgfpwbj53LtvfloTJsdRyi3AHfTmHTdgaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خانه‌هایی که پرچم‌دار عزا شدند
عکس:
عاطفه گنجی
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/444346" target="_blank">📅 22:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zakhmie Aftab</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/farsna/444345" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
شده آسمون غرق خونت حسین!
🔹
قطعه جدید «محسن چاوشی» به مناسبت ایام عزای سیدالشهدا(ع).
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/444345" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnc91gyVilErG1Gl79VdkU1RyDp6A4Zea-eenZT0V5fAMpmnrysmQ9fn6RQym7n96k83lffyvI7DkK2qsZfCvqvctbizR-d5XhjnsNBkbVOS-5SpOsqQ9H2AmVvDWzi_B8BtR4cXk8inip-mR6HoNXHbP4b77IHKXt8sLmoiV5NGPgfEUibqK8iNCTU-eKdmczDe3Zz2FAHv3qUvTpIz9zRq3SnYvp_bfkiNrBq74Ezol120hi2HyRj2u78IkrPcWwAsaZGHOlCtyAXXaSM8eIGjOPZkfzTC9HtYGkNM44pg1qhiEpAjt-5CncSkTjmnoavaUp0KcyMMKfJkgJBEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو رسانه‌ای تیم مذاکره‌کننده: هیچ بازرسی از تاسیسات هسته‌ای آسیب‌دیده انجام نمی‌شود
🔹
آجرلو:  هیچ‌گونه بازرسی از تأسیسات آسیب‌دیده در جنگ نداریم؛ اگر ماده ۱۳ یادداشت تفاهم اجرا شود، درباره تحریم‌ها و موضوع هسته‌ای تصمیم‌گیری خواهیم کرد.
🔹
دربارۀ تنگه هرمز، طرف عمانی دیدگاه مثبتی ابراز کرده اما این دیدگاه باید به یک پیش‌نویس مکتوب تبدیل شود تا درباره مدیریت تنگه هرمز بر سر آن توافق شود.
🔸
ترامپ در ادامه ادعاهای تکراری خود امروز باز هم گفته بود که ایران با بالاترین سطح بازرسی از تاسیسات هسته‌ای خود موافقت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/444344" target="_blank">📅 21:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444337">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJPt_cflJnYiB56o2Q4p1HhLK0hytvZHIOHZ4VoiAvZmidl4Fwk5xToTLhN4EMA-VYgbAN2-z5LSIvWPswXPBHgHkG3KyTnxM9ozWtgDaFesXlMs9fiKNUUiDN0J__4P3_WuDVZ4ioa_CH_oRz6qMJtSiI2sY3bo6uRYKmuZdtDt3dW5fkeTGJ44sL-Tem9GDqgPbd2_tM0nZO1kFZ2eQ8iDPQrmMsczQqlDaNSl_hcFFEx-VdJoQV5SsfCzfiARaV_ypafj-Ocx9ri6dyC1bA-q6CjC4S3sQ2RPv4wSZji_8aVQT-uP9mqlHqQFUaXXwRRBS46MRPM1ISQqEmIZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9RttxsjZJRjTiukx8SggRpkkcfdnizNB50yTJ2RkQ5wfy1gP6H4aJ9Dg1coCxW6G6Oan2tuCvSf0L5YojVjTS8Ld1-sseFbNO4GF8rgvER5JCQIWcynT9vLZFhjCMPYcS07B6LoVENOMyHyB3nLTi6gKRDPSUvuwsGXjkuF1-tK9eq2u4P7EFchYdZDmgiVE7W16cWZdBVMFPAzbS6kHML47v8oV7szgex__JsM37Ktey2wWMt7fW1VLoDfbYcIArzffDiDE39oOL0bY1Jq0zw-xG-aTFd98W3Wa6R0FKZvMWutCirnNHsZ41G1kqBYhrLSPQXQmhL6YMRBSMm9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6lwH7NMDThErDCFGN2QyBoJ2AH1Lk9V5VIH6zoj8GCrH445gUmQUzNBNiTv6f9011bcSrlv88gCHI-SkEJEMNUZL_JAWnUmejkt5ADkdAnezwe01_rr5rPD4v1XbH6uem425cDS1TYsvsfzqzt-7PVYYfQdxjDXaL78N1hiHRTY4a3OhCUlhLEqglWQ1Uo3VxyE08acstXc6g6uURR2-mAIeemLvNneICDLIrBQ7oQZIzT3e8FjYfeCBZN4vN61yMLU6os1SefczQ0tSVIVAPP7OzbDNgbZxKKJJmOIejnVz4hR1achyksaEBxk7Vf9CHrmFIXCVM6FW6aX-3kH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqrECK_5sa41t6tlKvrlYnHVK_PIMXlQpoBaIfVNEf4OEn5C3z3O4mEiCNKRBS2eJRLDr5ddf6JiiTjUJsJvSU40ZS_j_z5qfCJzLUki6SUHTzoBK3chIa6PTYQFCsgtyAZtAhHlEDTcLS9VPY7oodEYunWbYGxTqWz-IWQb49pjFYDIxGZVozD0_mToN9pIYNHRJfhID1VuzpC1PW3e2U2fQP2hn1QZcAEEuVALr3J9uFcd8IR2OlEx2aaIF64fOJzNsap6c2_7nc4Po-l31OyAcztyn0W1jxugVg01JDAI67idCTv66RHUHBfTbQRAo8iUwiqJDfDFmUQGcebWXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LG_UtYCLgDrs0Sa7F3ASWS5m6wJ9rAeHPxUb5h3Zgxpg_fT0NyI_zh8HgA9J2oTRQuxtyVVtQwmAPoha0SOMtpgwhRvjt0v3N45nKKjuBzYU4jQW2qLDJAXbmlhOR38i1A0dXmHDofDTibOb5HzzUf40xc68BI2_JnjgQymdipqokV8Xzz3SsePt11slZrnOqlBjOe-OJwiyKMrD-m3X7t48QrYEKzM_cu-0iBh6cpDeN5CoRRDNIu739DEik7oCpKyk8jSd0zjzKlCrT8FftDbSPBgqXpiT2H2G-cXNj470qTSMSst65huQlLjLa8vK-7kPWXLrGXaLONNBJVGo9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3wgqQxs4uLW21XtjuWKqOZ1M4sm1Rny7B3xF6PtJQlEdrRGsa32zwWVD45N2q9-pWcSSZwdP-jEWAYpCSthxIvzubUwUyqUG82O8wWMSt6aRZggLy9WjmoNAGbhG1j8J8X9jQxBX8oF4PP9atreNXo8DIqiOKibCCqSD4TxW826wWU7pamelQbmylheDDiNh80C9Yu_PClQyxHq-vu4yTtTuVaiknVH82fDqEQvejzRVAkGR34QGHBIn-Kfh98q5DWRRlX4OXOpzGODzcaxPbFebRtHtBfO0dKW8dfIZvGQjuM0n7kx_EO4NUhlTNb1EizkS8N2J9RwUopoRMdpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXRkLXsN6zSzumUbpNwsggaxzGA_sU5QzEzx6_AhaxtoWQZhOAIsMI4uZN_9HILQXh5riW6VvMpcvBIOwMsk8HP1TiULHw508yX5wmIlMq8yYFe28iyJdkb02RVJ-vm6yWya18SnJ082pxKUJraXJ2JvNMmPcxSVc8-gFSHVQ4lVjqfdxMUchhgxxVQ8hBCYoQ9z_TDDQbxidHCM9I7caxNxVqcP9HC8LOCTtMjEZeTQqx0MKeUS9CNX4oMe-w7VD-hFWoWpfSaGZdAbUN7JXX7P5hKOehHfzqMb1MVhIbInjwyMWI9FuuTY71Xl2QoReYixRwYw7L1sZNQ0vT3GUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مشهد الرضا در سوگ اباعبدالله
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/444337" target="_blank">📅 21:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444330">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvSA88vUR-vF1o1SnkhR2dzFcZlA7LpiwXxrWmF1EbZpc05iW6gFt8VYChTi-hN0AR1FbaTV1LgQ9aaECZV03nUE6300St_-4FBDDekBhhQ2J4ScxY-RMOQjH42IJY6GsbG73pasEYNjAI0UBZzxjz0NmanLTjKkYZEF35PqYKhvUsp_-LZWbFhAd0ki9lMz4sXNKqrNrG9iO7t6LUubeyPGDkawnhSlhKl5XAQLD7dGCfnA8YvIHKmRnismb6SlRQPomPzFppzVPqdbT8f-EqpnX-mA9hGM9jqO_TLLpiMOw3cItfABoHdsJjDbHPMl5GVSOKeKPqyDFFQdLAVG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbnaS8cA2MiFxg6I185dKm0f-zjtcTNJ663uqCkyFPvzefi3dAr7TesREqpcZ8soYaOQcTbevZyHU3OB8MbQffHW0rGe17VGsxUxNGhNa2ZSTvjqgzZnwez_hGYjhhD5Ca5dqie1wFHfg8SRwf3LywuIyV6mN2URBMMeCQdgS87j_9RyNRHY0HYiq8peXD5c7k8PhU8UhU3GlqFewT-9CO4y_1bBth2TkmOO12Aka0FYwjenluAgCtx_SlsmtqidPq38Y4FMhByfDce9VeeKgeNDNJbdEEPp9mIoDFWmfjWnGzG0cBUuRIvPgFg3poqYXXa4SOb4OWNYgPm70XnY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtB9jGAQDSDqGeKzeFYedeWBDoX4VOMylU4FKk0tA8tsDgGSEkBiSrAtjpMaOqC1pPjCHJN0gNSirqbmWyxW1Z65Ik4IJBIsfoUYo7gv4tDv9GvLlYoLTyQYFXAuX8n3GSMVGpRxjK0VLGOUEz3nNdSJGnepS964qZqoE-m8rn_VVequ2vem_lw4ZHKVpRvgpUxzFw7wRwh_QSXpDldz41In-ufoM6wxBUkiE8XMJwscUIRN-qBFaaDb1c94TFuDb9r6WoylV748Sl6nidboSnBU331Gj5xlHacMof7AK2td8k47Qo3u1-8OZOeRCjvFZrGtvwG5kC-9Ub92poQEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aokc3XFgul3LSJnqiCjMqTynsa869cZx5DRCqL5p829i432E_hN70kBDToFSoDyBJxhArMZ34DfFkkN-7ETUStT3MzTbahkUxaaJs-5u1NXXXjgcp93AdROEXlYaa3oP7zTcInlkNX1w6kqbMPUXdhuU2FnqaB7RhXW4rT_v_DgaS9b6uSWVXu4Si5zUt_L162AXeUIrkhPNj4eDYms9sp34sMs4hPENiWfK0wjv7959gaXKb-4EWeleCoMKx6ZpaM49v5Gm02VPXe-9zlPQOujSlOd16qAM7EEvg8a7dC5Z1DUS1O-z42gZzij8ouEJ7C0XbRMJRDL45WDyZXjVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I62l22SuBrDE9CBuqYNnj998pE6dGHbNLRLgU_ngyOLOQ-rCdyfFJGVEhEVCv5_Hk9ap39F-r0FeawrV7voF0FQgd4XWhKpgj_zqU1ruLHNsqlS3gkyrzRCc0NmYlkawq4lHNAvDdv1JpF5ZjzZllNHmHnA5QSbEKDL3wRjd-duT29ZiGK-Jk6PETRpy0JGnCX4EWuo2oOBg2o8XNY7YMeDqry-y04B8phdVB7jZtgoVUupoWnAe1FppoCrK3luKCUgaM3YLR2udth3n2WCZf66WaWYvggT4o0eR0H8_QWYngW6ng-_tvZKH2egIu-ggrwXiZJwhAHhJrWnRuPio0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGQ96gjrdOS5DfyuLjQE7mVPIFvpiFzj0Lvdkx56qUXuglAt_skfsKhzxnfdEtcdeAQ_314P7c0Whco5MMp7XUeVh5GKY6BqM2wTEIksMXLLbKmsr3kLw2lzaR10qmP93q6MsXinwlP9yVJPXX0XmAApZ5jb6V55R4sE-2NGsaN0Zf7bCAXTTjcwiYgpCFExmT2nQsMZvAvL_bdepUMPcnQjwBXi7zNAEYh5UdGn3uwVVEXblsfDl8xclLf4JwMyml1bSkzUf8JtAvdvaSL7xkotoNIbDpUNtpzAHhMwiX3Y4RT4E76CHWsyV5PgUhaw-vj6ukFiQa0yPYSEWYT6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2R2McYiMXYhEzGBl7fw8yIvglgwTOBnbg5_CTg5uP6DDh-wgGzIQgWuSRhsFtullrxzo-sj8twaLb3IyicA3Z6kpx9NRIENEEhN1A_YMWBsqKYKoczaenSGwywP7urd17zn_GeC6yMk8fJBsOy2AN7XdADIP-PXLRobYdEVEzWdpfIeuS9YrPBOLjEZjsvCjdnm0LFR1cakx014LXW6FXEjg3asaka-KyGvf3mGEZn5mn9b0I8ZMVieY3Z1hKanEjtBR4awIq8Loi43IaS2lBIUV4X6uZOo_55k3t1VF4CimO2RHzQsBhivaW_SDgl6gv6oQZ0SXMcc0kV_CNneKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم عزاداری شب تاسوعا در جوار محل شهادت رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/444330" target="_blank">📅 21:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444329">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbMdbaz-OGgWhWFaBYA-6ZxAZVniMYhhrt8ZqwVGs02VMlfZ-Ur3e3HmaQBiklATPdXjRX4h4q62Hqha9EmEdbGO1QIPTIvT1EVVe_ht57lIZuUqYTq8wb2as4BQaZcG6qwdbuAvTUus9KuDCdTzeBQwT36yFxn-lkhgzMr3tUddbsDZW2q_FQBPj9ZCheb1H3FEQG_pbzIU2WyA12eShI7M6mPYXTYRWP92pjt8wgxk3JzGJ9TuLz9ChqAFaYMyMXVb7oq3FQV_AjWZn1Wx2wjV48H8Un-YbkO-t_PWhJx4_ouT8nzuERUpoTtlYPO5L0pgzKVM8GfUqfVtIdpE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار پهپادها در آسمان جام جهانی
🔹
سازمان‌های امنیتی آمریکا از آغاز جام جهانی ۲۰۲۶ تاکنون بیش از ۳۰۰ پهپاد را در نزدیکی ورزشگاه‌ها و محل‌های برگزاری مسابقات توقیف کرده‌اند.
🔹
دفتر اف‌بی‌آی در میامی نیز اعلام کرد که برای ۴۹ اپراتور پهپاد به دلیل پرواز غیرمجاز جریمه صادر شده و ۵۴ پهپاد در ایالت فلوریدا ضبط شده‌اند.
🔹
مقام‌های آمریکایی هشدار داده‌اند که متخلفان ممکن است با جریمه‌ای تا سقف ۱۰۰ هزار دلار، ضبط پهپاد و حتی پیگرد کیفری روبه‌رو شوند.
🔹
این اقدامات در حالی انجام می‌شود که آمریکا در سال‌های اخیر با نگرانی‌های امنیتی فزاینده دربارهٔ تهدید پهپادها روبه‌رو بوده و سامانه‌های جدید مقابله با پهپاد را در نقاط حساس از جمله مرز آمریکا و مکزیک مستقر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/444329" target="_blank">📅 21:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444328">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24559c1356.mp4?token=OLftS1lMe4o4QhkOlvXcSgRs-soDSFVBYmo7WXyP8nV1NpLCPtW3rSsKP8O6gXJhVWct8lvvEFHmL_yITkFLvfFebeXaozaBKjiemMBQE47B-IihYOG--pv_585GQior7lajLTZDEqY-r2jcrr4f68y-wmbyG-ZM23tMc1wTJcBt9ZHRL-_5iaJtMi6FDFjFOjzDJCcce7z0u7v6d2N5NtcYK0Qas980P0vLrYCJlcudOVgKb4WqtQHlWDDXNRRe3m8mNJylmlY1supmA9rUOMpLJYgvCq9HYwxiBlOegaUP11dJ4zmWuvHCGaOIgR5FSACNnh3pbrhDt-aCtzFEmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24559c1356.mp4?token=OLftS1lMe4o4QhkOlvXcSgRs-soDSFVBYmo7WXyP8nV1NpLCPtW3rSsKP8O6gXJhVWct8lvvEFHmL_yITkFLvfFebeXaozaBKjiemMBQE47B-IihYOG--pv_585GQior7lajLTZDEqY-r2jcrr4f68y-wmbyG-ZM23tMc1wTJcBt9ZHRL-_5iaJtMi6FDFjFOjzDJCcce7z0u7v6d2N5NtcYK0Qas980P0vLrYCJlcudOVgKb4WqtQHlWDDXNRRe3m8mNJylmlY1supmA9rUOMpLJYgvCq9HYwxiBlOegaUP11dJ4zmWuvHCGaOIgR5FSACNnh3pbrhDt-aCtzFEmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژاپنی‌ها با فرهنگ‌اند یا نژادپرست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/444328" target="_blank">📅 21:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444327">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e447e3e393.mp4?token=cr3IkVHl0UPuDFsuZnJSzAwubXNtBM8I6ImiHPaJIipyIiBU6RnyFmxh4gDcqDL5Y9jdUGyRVshUpOY6DqPRphwKwDklB0Pk2OKunWTIuRQrb7nt8HMXzmNK29fmNK7nObdJN8hoUYP63lvRStnnZ6yla7f8cQgpzQsBQZtkag5i64WAuNHXD_RxmtoRmVQlXf8hYNdUcYmgc3QMakQ7FzmQ78vC1TVtPhC9-UYOzbU8oSkNT3pnlDVW-9OFJTmWdGvEsLxu7iO8YV4a6dAF1LAp92xFUchGKfCrcYD7Q1xkGdXgk7ULz3x5KDTXSheX_pIRlzCU3rTmIfrCWNbT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e447e3e393.mp4?token=cr3IkVHl0UPuDFsuZnJSzAwubXNtBM8I6ImiHPaJIipyIiBU6RnyFmxh4gDcqDL5Y9jdUGyRVshUpOY6DqPRphwKwDklB0Pk2OKunWTIuRQrb7nt8HMXzmNK29fmNK7nObdJN8hoUYP63lvRStnnZ6yla7f8cQgpzQsBQZtkag5i64WAuNHXD_RxmtoRmVQlXf8hYNdUcYmgc3QMakQ7FzmQ78vC1TVtPhC9-UYOzbU8oSkNT3pnlDVW-9OFJTmWdGvEsLxu7iO8YV4a6dAF1LAp92xFUchGKfCrcYD7Q1xkGdXgk7ULz3x5KDTXSheX_pIRlzCU3rTmIfrCWNbT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا باید کولر را روی ۲۵ درجه تنظیم کنیم؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/444327" target="_blank">📅 21:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444326">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eca1f9f76.mp4?token=GUyaC4iFmaDSVA3QnV1v2qHyU9nYbQVcnwjE7e7BCFAmZg0Vl6Ch1SF8KqG9_oNgLcZl_ZilygYB8aq4AF2iMLXJDI676fJ5tTFbGJfnG66bVsXrDvjAnUZ9mvjFCegoSKUI0nh_BumQzgij22PjV7LH3pOvVtVPrIJAs6nxXZVMKqDlq0YsvO07zD5xJ9DqIHfpVHUmyvYNZtelsUDHVyfPTGP9AFU0QktYg-xoMpGaEm5v8as01b9v4FQwTeIomt3fb3u1wJbGK_BG6ZWHzcbhoS6wVR8ClsoPlb6Rna2yEdt34g4SCFdeI0fX-86Zbm5hjUtlaJsQiZp2yJMhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eca1f9f76.mp4?token=GUyaC4iFmaDSVA3QnV1v2qHyU9nYbQVcnwjE7e7BCFAmZg0Vl6Ch1SF8KqG9_oNgLcZl_ZilygYB8aq4AF2iMLXJDI676fJ5tTFbGJfnG66bVsXrDvjAnUZ9mvjFCegoSKUI0nh_BumQzgij22PjV7LH3pOvVtVPrIJAs6nxXZVMKqDlq0YsvO07zD5xJ9DqIHfpVHUmyvYNZtelsUDHVyfPTGP9AFU0QktYg-xoMpGaEm5v8as01b9v4FQwTeIomt3fb3u1wJbGK_BG6ZWHzcbhoS6wVR8ClsoPlb6Rna2yEdt34g4SCFdeI0fX-86Zbm5hjUtlaJsQiZp2yJMhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: نیروهای اسرائیلی امروز در جنوب لبنان آتش گشودند و ۲ نفر را کشتند. آیا اطمینان دارید که آتش‌بس همچنان برقرار است؟
🔹
ترامپ: خُب ببینید، آن‌ها سال‌های سال، یعنی چندین دهه است که با یکدیگر می‌جنگند باید ببینیم چه می‌شود اما درست خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/444326" target="_blank">📅 21:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444325">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b67f614c0.mp4?token=RjshU6cPYleNS57rAE9GEOwgDSJX5tUF4hT4KzSu6eoRwNuH5_uqYZ5AgxOvkE07lwQLoD2pNSTtuGsLXwvWEzaKGFiqqI3L1DohsSRhaBZKScVmVTnxOCakhKBZJcvp9Egv6wYbQp1LxLJkhfYlhOcVD7_xLpZk0z_xwjQEm1O4eqWiVfJyZXhBQh-VZQq5yv0LSG6YcXkBA2PygLA5g64n9CsZXCRB_qYN9yXI4iyzYEBEvnhVyzSdKjgCx6zWB4tjd7PvHUISfZLVXcl9aN3ilYN_zxRGyHpyMKzHaBo8HXFYLdHrhUdV7YHyG2_TEEq86yfTOq35KuUoOZY37A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b67f614c0.mp4?token=RjshU6cPYleNS57rAE9GEOwgDSJX5tUF4hT4KzSu6eoRwNuH5_uqYZ5AgxOvkE07lwQLoD2pNSTtuGsLXwvWEzaKGFiqqI3L1DohsSRhaBZKScVmVTnxOCakhKBZJcvp9Egv6wYbQp1LxLJkhfYlhOcVD7_xLpZk0z_xwjQEm1O4eqWiVfJyZXhBQh-VZQq5yv0LSG6YcXkBA2PygLA5g64n9CsZXCRB_qYN9yXI4iyzYEBEvnhVyzSdKjgCx6zWB4tjd7PvHUISfZLVXcl9aN3ilYN_zxRGyHpyMKzHaBo8HXFYLdHrhUdV7YHyG2_TEEq86yfTOq35KuUoOZY37A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: هرکس که از توافق با ایران انتقاد کرده، باید آگاه و توجیه شود، حتی اگر از دوستان من باشد.  @Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/444325" target="_blank">📅 21:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444324">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM8MIoq5h1Lznn6Sh6KS3P0FC2kNE-IOc8QuF8ZWPed3_cRObFsZekTyQnVDZieRrmmIdeBDR8EWw1Cz07-KDveuqH5Xyu1MVsU5QmyDNnMg17QlHgS3yyXuh812-0bWO2_mL5-6e54fJ6eZukr1vf_ixhRnVTAte5gWyNN_jhPDexZOF4AukylOBYm_qsrSmoJXqgGNdxNeLXrkiPZvz2elacNmP34oWgr3guM47KLuN9yJKvFkWNxHg3vnC5YmU3XcDNj51WMFw1EBVCUYchoPCBqK8NETaRqNyTnDMVTeVdbpqKCQMRrM-iDLo2LX9SiXiJugfzxpc7eHfr-4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پرداخت حدود 11,000 میلیارد ریال تسهیلات ازدواج در خرداد ماه سال جاری توسط بانک رفاه کارگران
🔹️
باهدف تحکیم بنیان خانواده و کمک به تشکیل آن و در راستای ایفای نقش مؤثر در حوزه مسئولیت اجتماعی، بانک رفاه کارگران در خرداد ماه 3.236 فقره تسهیلات ازدواج و تهیه جهیزیه به مبلغ حدود 11,000 میلیارد ریال پرداخت کرده است.
🔹️
بانک رفاه کارگران از ابتدای سال جاری تا پایان خرداد ماه بالغ بر 8,600 فقره تسهیلات قرض‌الحسنه ازدواج و تهیه جهیزیه به مبلغ حدود 29,000 میلیارد ریال پرداخت کرده است.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/444324" target="_blank">📅 21:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444323">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8pTXVhsTr1H1gG887eOuS0-qb5owf67SHJuGrFvIP2L7RvjGwfSKQNXv_9rY6AzzJg_vEWSJ3NfZp4FU5Y6ccNZ5TEbvrqx2qWxCH9jZiCyfAM4n-sit5WP0Xe0DAN198VSG8-SEbDG-8QAaE-l93GMYfabiU6iE2Ao66QQUztAv9tylJhUhR6Ai6EdCF6MyQtslORfdN623oGGger0E4ffNL_U-Ao9z2A0-LvhoKLuSKTgo1oKVNOknWup75l9pxrheZunzwxLbEBvUqb_dcU-qU3TYL-oddLWrq_AxDMWMk8eosG2rNJkroytVxctZbqVTG-avpIk7IJfVAISxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/444323" target="_blank">📅 21:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444322">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/444322" target="_blank">📅 21:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444321">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db07f3a020.mp4?token=LXhCtJQqmhZO9VlxXvwMmCL1GfJ4F9der8EiPoOtXCNFYj_MKLh7I82cSLLXlXy_ElhVaprFU-8Y9fhYjzv0znpCigIYcgPjqWSoK42gtktFfhQh7pKUd8YAQGs04Uy-jjSsZ4iZdy6LCtH7Iv-NPTLO1ebHounco0nOrnAjEZcpEZUFtBa-SHhVpPZa0PWVdcvbhbSrlrPly-Iljb3FHQxxZwg0Wx7FXps0St7WdnPRd_4Ep_DzK9TrAUnkIwMJa-ojcvmNj4GDUQAT8L5-tuus-S8pew4BJdHAgXei45-iUQY66xIYzQ2f1dpiYewZAoDPdPdnBKBck65P96qBQmb2XkHnjMsDXbbRy9LvpJoqWsHf1S6lvJMBQS1i5hkWu8fApxoouuCdxcAraYiOL26I6a4Cj9eQcOuVAEWal7_65APGEZa7RRVnFAtWEBxPgqgQBh6bbZQi0GSsE9APgrS_A825jWLnVRB2jVeAu9uuv9X59Ctx1EtBpZDl2onBzquVCeLBo3LQjTUaTUoy25HxmoTozZrAyum2-LrzA7guvoFLke3REjle4qotwidCTWmLn3KgpTQIrSE302pZBWWQtYe3MshC4XodG91wCAXVORnmEvhayPKetTcYs--mqRoj1gDPxc7zvckhElvlMxdvKtTDFDJYrXxp1ZcCDBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db07f3a020.mp4?token=LXhCtJQqmhZO9VlxXvwMmCL1GfJ4F9der8EiPoOtXCNFYj_MKLh7I82cSLLXlXy_ElhVaprFU-8Y9fhYjzv0znpCigIYcgPjqWSoK42gtktFfhQh7pKUd8YAQGs04Uy-jjSsZ4iZdy6LCtH7Iv-NPTLO1ebHounco0nOrnAjEZcpEZUFtBa-SHhVpPZa0PWVdcvbhbSrlrPly-Iljb3FHQxxZwg0Wx7FXps0St7WdnPRd_4Ep_DzK9TrAUnkIwMJa-ojcvmNj4GDUQAT8L5-tuus-S8pew4BJdHAgXei45-iUQY66xIYzQ2f1dpiYewZAoDPdPdnBKBck65P96qBQmb2XkHnjMsDXbbRy9LvpJoqWsHf1S6lvJMBQS1i5hkWu8fApxoouuCdxcAraYiOL26I6a4Cj9eQcOuVAEWal7_65APGEZa7RRVnFAtWEBxPgqgQBh6bbZQi0GSsE9APgrS_A825jWLnVRB2jVeAu9uuv9X59Ctx1EtBpZDl2onBzquVCeLBo3LQjTUaTUoy25HxmoTozZrAyum2-LrzA7guvoFLke3REjle4qotwidCTWmLn3KgpTQIrSE302pZBWWQtYe3MshC4XodG91wCAXVORnmEvhayPKetTcYs--mqRoj1gDPxc7zvckhElvlMxdvKtTDFDJYrXxp1ZcCDBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم پای‌کار تحقق شروط رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/444321" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444320">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5b2888b6.mp4?token=UXH2Lahbw79gKJHNT_b1tEA61XjC_svdF6zRZ2ait2nOqZoizjPXeFj7mvEU1o7NnPgYUlpXDiX7thm0EL5-yFxR0OyjKDkykOp4he71UMpm_QzgZ38ZS22_OL-jxIUebFuG4GerO1mTiTWwRgavEyQDZTQTNxC2opOec2B_JiMEeA3sUvN8ZvrMCtrN_rMk8YqqJrSNNe2kelVvg2_HvnKDXo-fBbL-sbdHjTCvWBK0yl50uakKC1Ri0_FgBCTGK9e7qStmbCA6qxv4VYUXUG-vW9x-tiWGgj6nUlTV6ky68YSiCJq9e5I80lGoe4Bz4p8ShwFf2PB5u6iP4YoWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5b2888b6.mp4?token=UXH2Lahbw79gKJHNT_b1tEA61XjC_svdF6zRZ2ait2nOqZoizjPXeFj7mvEU1o7NnPgYUlpXDiX7thm0EL5-yFxR0OyjKDkykOp4he71UMpm_QzgZ38ZS22_OL-jxIUebFuG4GerO1mTiTWwRgavEyQDZTQTNxC2opOec2B_JiMEeA3sUvN8ZvrMCtrN_rMk8YqqJrSNNe2kelVvg2_HvnKDXo-fBbL-sbdHjTCvWBK0yl50uakKC1Ri0_FgBCTGK9e7qStmbCA6qxv4VYUXUG-vW9x-tiWGgj6nUlTV6ky68YSiCJq9e5I80lGoe4Bz4p8ShwFf2PB5u6iP4YoWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: هرکس که از توافق با ایران انتقاد کرده، باید آگاه و توجیه شود، حتی اگر از دوستان من باشد.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/444320" target="_blank">📅 21:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444319">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صداهای انفجار با منشا نامشخص در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/444319" target="_blank">📅 21:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444318">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quDZSjrWem1chC-GEDE8-Qce7b4zrj-F_6w9qxztfEq9VaCofFduIKz8cYUojEG-JEKGr-G87sBePDK90H6KerbYkGxMjODd61gbZR6iAtVzfIKE__MKUcFn8Vs70aLf4QByfhmk9P8cUBYRRXUgsKywHVi82dy4BocCUmL2hSMAidrSqcbi9k85eoY9didwVSS1oUQQCW6B1ZmFWHWquvhDRmiUooOiLI22BWwwVcsv_JUJWGrejVs99opFTEEsOYc9lHj9wABGGipjTnDns5Hqwboq8Ld9fqC9qE44lX5pyr1V58QmftqkXibZiNxwpDFiNRqQfmCRquIDu92F8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل زد و رکوردشکنی کرد
📊
🔥
کریستیانو رونالدو با گلزنی مقابل ازبکستان به اولین بازیکن تاریخ فوتبال تبدیل شد که در شش دوره مختلف جام‌جهانی گلزنی کرده است.
@Sportfars</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/444318" target="_blank">📅 20:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444317">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9a71a909.mp4?token=ky7zdeB_mzBndmKwsWsdv5CsawFmz1lnFsIVmGPTx3g5zOVKMKlmi5ytjk3jnz_KbhBDzDsMyqXLd2cd7Ni4jGGPscUeqe1AOybmzyx6U6jskKNfnwdR1-IURhwqzF1Fuk95qZduDbR3kCvJ684eO35hm1R4d-vwthXq6RDHBzjpL1T1eLaM44ZjMns2_6dosR7y5F_9CEzsaFz6kce3IKoNbd9bHh-mzJtxgSxkQBmv5me4VQUEJvyJYrFKijWwWd2eeEGAfK2sSc8CT5In13Qj8A59cBVpE_kdjg8JX0NIDLrYmoySShH-0P-bobxNFyX_Vo5p9Fn9419uLTAzXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9a71a909.mp4?token=ky7zdeB_mzBndmKwsWsdv5CsawFmz1lnFsIVmGPTx3g5zOVKMKlmi5ytjk3jnz_KbhBDzDsMyqXLd2cd7Ni4jGGPscUeqe1AOybmzyx6U6jskKNfnwdR1-IURhwqzF1Fuk95qZduDbR3kCvJ684eO35hm1R4d-vwthXq6RDHBzjpL1T1eLaM44ZjMns2_6dosR7y5F_9CEzsaFz6kce3IKoNbd9bHh-mzJtxgSxkQBmv5me4VQUEJvyJYrFKijWwWd2eeEGAfK2sSc8CT5In13Qj8A59cBVpE_kdjg8JX0NIDLrYmoySShH-0P-bobxNFyX_Vo5p9Fn9419uLTAzXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل‌زنی رونالدو به ازبکستان
⚽️
نتیجۀ بازی تا این لحظه ۱-۰ به سود پرتغال است.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/444317" target="_blank">📅 20:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444316">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWA1vWvKUGX4eIoYeHQRxjfYHvNKrtcfMqqWnsqfY6bZUcsIRlFOGsFQU9N0BJ-ll1tzr4BxKMqhNEuC5Ik2szvdC1Vh-HbmTpAijhs0whkHCrffuR1hzs9r0dO58ZarWlMzcpEw0rojxMy1W3ux1lfTXkLGK3oMseEt436d6Vvu3AFxvR_IdFk-lOMgfC0TU6Jgyu0TFtaHnM6CbQQUJoWkXMxaqj0MQ2zAT1zxs79mEstU-z03u-MGtYJUROWiyVAQtFRFYeJ3HdTuIhyNViouLgE8UCK9bwg0fcKUpiXsiTehN5GSBXwHKq8Z_t-C2ngxPd_KrCi5HZGd4ry8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرسنگی دادن؛ ابزار صهیونیست‌ها برای گرفتن اعتراف از اسرا
🔹
دفتر اطلاع‌رسانی اسرای فلسطینی اعلام کرد که رژیم صهیونیستی از گرسنگی دادن به عنوان سلاحی برای وادار کردن اسرا به اعترافات طی بازجویی‌های نظامی استفاده می‌کند.
🔹
این نهاد تصریح کرد که بیماری گال و حساسیت‌های پوستی در میان اسرای زندان نفحه شیوع پیدا کرده است؛ این وضعیت در پی بی‌توجهی پزشکی و وخامت شرایط بهداشتی داخل زندان رخ داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/444316" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQYM-YqtrAQvYGIgtMtMUsFCIjX7HObzhBD6m8EexsHlRztho0_nvnXMpJvIBnPyYm9RSG-YMU8i8jOASK0YEmTN2mzbRi4sJW1aAPucdE-2PiuSVPW_h1O8yA3_-nZRYzoBpMHV7T0x1P8KNat44b517ckBy-DNeQran6P6NJV8fk2dtWPbX9xNyrRAFZmXtQvztl8PXBWcbsiN14e9QQRby1g6GUDXgdbM1sJ6mshLX0SQbF4DtZhIiiOKNkiZY3qhCjd-jiiFzh4oYwDRVB9CglkuN4vwU9rAwfKumaZzqLELEB7MvZ7tMghrz5Mf7q_bUZrKYy50wwqBzxol5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف وزیر اسبق آمریکایی به تسلیم آمریکا در برابر ایران
🔹
فرانک کندال: جایگاه کنونیِ آمریکا در برابر ایران، ضعیف‌تر از قبل از جنگ است.من یادداشت تفاهم را خواندم، تقریباً‌ شبیه تسلیم شدن در برابر ایران است. اهدافی که ما داشتیم و هر هفته تغییر می‌کرد محقق نشدند.
🔹
حکومت ایران همچنان در قدرت است. ایران اکنون به طور قطع نشان داده که می‌تواند تنگهٔ هرمز را کنترل کند و تا آنجا که ما می‌دانیم، برنامهٔ هسته‌ای آن‌ها تحت تأثیر این اتفاقات قرار نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/444315" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e3aa64f2.mp4?token=NHwgMzcIe1MsNE9r1HtuA8OprShNrgbCXwDeIn1ZMImtQLPDVLoW54G9BPdbqv9dR5Cd7D5QIQFjpyXciWh1pVr1Gy_Nisj2OIfgsrmxZXHshRECCwdRRQHFG3GlnbVcDMZBuMU_ZpWf_hqVrDy6T5sJWfiYaUTJDCfixU8AQNXX_NPyBWSNjmq47KDqkhS6hQGtvZIoIeaT2CeJgSiZ5ZiP6miqRHgihFvLjCP90YiB9rue77fx2wIu6xR1KAR_1immGJSPOL_QHD5n-Ifv323vP-Vsp6orB7ZSOlpShHKGZN_IJNo_UhNN-LrPWJVHvAU_XqxrEf7FwcN6mYhz2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e3aa64f2.mp4?token=NHwgMzcIe1MsNE9r1HtuA8OprShNrgbCXwDeIn1ZMImtQLPDVLoW54G9BPdbqv9dR5Cd7D5QIQFjpyXciWh1pVr1Gy_Nisj2OIfgsrmxZXHshRECCwdRRQHFG3GlnbVcDMZBuMU_ZpWf_hqVrDy6T5sJWfiYaUTJDCfixU8AQNXX_NPyBWSNjmq47KDqkhS6hQGtvZIoIeaT2CeJgSiZ5ZiP6miqRHgihFvLjCP90YiB9rue77fx2wIu6xR1KAR_1immGJSPOL_QHD5n-Ifv323vP-Vsp6orB7ZSOlpShHKGZN_IJNo_UhNN-LrPWJVHvAU_XqxrEf7FwcN6mYhz2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نخست‌وزیر پاکستان: شفاف می‌گویم که هیچ بحث موشکی در مذاکرات ایران و آمریکا مطرح نشده است
🔹
کشورهای بسیار زیادی موشک بالستیک دارند، چرا من باید اعتراض کنم که چرا ایران موشک بالستیک دارد؟ با قاطعیت می‌گویم بحث موشک بالستیک جایی در مذاکرات نداشته است. @Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/444314" target="_blank">📅 20:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444312">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df08714da6.mp4?token=DlPBQTAUcfoENw0ndpvPMvnz6bjNAtTohqmIl8wh06nw9AmaaNyARCFz8kCJiCcXRvvuAA9sZ4MhhMWtCNNEL9dEAhtgPGXvKYWyBmy2rMjgs-_d_ZbnbNzmftW0C3aBpiUFXG6BfWKNCSHpBg-ur8UuYvBhYebsKfzyjyILLJYSAhfE_8858pjWuIb3nE2nlsuN4SBT7v1WgDJ6F7Gx9zWOINo-AYt3Ro9fUPeNsbH_JNeH5w6tVXbaFqJLJve_cANuaVoGJ08pk7cfEy6mx3bQ_YIcc_yBdOECNyUyupHAAKdLvHjQE4c2sAzpRlnA12J9cxlM5zddCvVODb5m9TQfnOqFq_9y5kHzxJsGLPqjHHwocYTaROq6PQcUCUkNU0S0tWxn5V8QDh-V2utoJ1TdWh0yHt3djn31FCF-VkQP7P9sm5oGopZhs6HPYv2paNUaD3TXhYNvS_9xEL--1MaqHxf_YYXZ1yuxf1v70TQ89jhIQaIoE1kOXjkFJrFRMPNgPAhAyBzWRF_BzfDub52zgY5bpRilw5azOQbsed4pUhCnHNuC5DyRujynlPD2HOAuuSI6xXvyQzGSrnp57vDvmyedC_gJTmBNICGESQifsDmONn4vmiQ7K4VWotkzOA8YXyUH5xN8Th19J982xrO2280G9N5EKst6NShirUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df08714da6.mp4?token=DlPBQTAUcfoENw0ndpvPMvnz6bjNAtTohqmIl8wh06nw9AmaaNyARCFz8kCJiCcXRvvuAA9sZ4MhhMWtCNNEL9dEAhtgPGXvKYWyBmy2rMjgs-_d_ZbnbNzmftW0C3aBpiUFXG6BfWKNCSHpBg-ur8UuYvBhYebsKfzyjyILLJYSAhfE_8858pjWuIb3nE2nlsuN4SBT7v1WgDJ6F7Gx9zWOINo-AYt3Ro9fUPeNsbH_JNeH5w6tVXbaFqJLJve_cANuaVoGJ08pk7cfEy6mx3bQ_YIcc_yBdOECNyUyupHAAKdLvHjQE4c2sAzpRlnA12J9cxlM5zddCvVODb5m9TQfnOqFq_9y5kHzxJsGLPqjHHwocYTaROq6PQcUCUkNU0S0tWxn5V8QDh-V2utoJ1TdWh0yHt3djn31FCF-VkQP7P9sm5oGopZhs6HPYv2paNUaD3TXhYNvS_9xEL--1MaqHxf_YYXZ1yuxf1v70TQ89jhIQaIoE1kOXjkFJrFRMPNgPAhAyBzWRF_BzfDub52zgY5bpRilw5azOQbsed4pUhCnHNuC5DyRujynlPD2HOAuuSI6xXvyQzGSrnp57vDvmyedC_gJTmBNICGESQifsDmONn4vmiQ7K4VWotkzOA8YXyUH5xN8Th19J982xrO2280G9N5EKst6NShirUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
نخست‌وزیر پاکستان: به کشورهایی که می‌خواهند در مسیر توافق سنگ‌اندازی کنند می‌گویم چطور ممکن است خودتان موشک بالستیک داشته باشید اما این حق را برای ایران قائل نباشید؟ @Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/444312" target="_blank">📅 20:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444311">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
نخست‌وزیر پاکستان سخنرانی‌اش را به فارسی تمام کرد: زنده‌باد دوستی ایران و پاکستان
🔹
شهباز شریف: هفتهٔ آینده به تهران می‌آیم تا در مراسم ادای احترام به رهبر شهید ایران شرکت کنم. @Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/444311" target="_blank">📅 19:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444310">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda5c8ae83.mp4?token=b11WrTcglP7G_VJ8Yxe42QZ3rzvB4w33P0qBT8oGdZXM3HpEmMfbQ1Z5AINZok2y6Xh3Vq5DR3NWG4-hhTFuN4OdP6_zKkx0mONkOC4iOXSGJoPwwxT64g0sAk_bJLbCtw__xhOFzEVX8MjFrh5KDpbSTb33tJGmIWH3_e91n951cGWBPQhbg7vgZs4m17U-ynzpHdRLGCclDPhTOY1XSdZhKB08QmVM7gdSWElEsYZVYPqpXzskZGGxqpxPL1fjij29Fij3Mn4jEo-3sk1OfHL8qXXtKbQmDZedOb6GyEp7DVknsq7URMMitsiNgUZuHnSlBM09PFv4ZH7Ko4FMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda5c8ae83.mp4?token=b11WrTcglP7G_VJ8Yxe42QZ3rzvB4w33P0qBT8oGdZXM3HpEmMfbQ1Z5AINZok2y6Xh3Vq5DR3NWG4-hhTFuN4OdP6_zKkx0mONkOC4iOXSGJoPwwxT64g0sAk_bJLbCtw__xhOFzEVX8MjFrh5KDpbSTb33tJGmIWH3_e91n951cGWBPQhbg7vgZs4m17U-ynzpHdRLGCclDPhTOY1XSdZhKB08QmVM7gdSWElEsYZVYPqpXzskZGGxqpxPL1fjij29Fij3Mn4jEo-3sk1OfHL8qXXtKbQmDZedOb6GyEp7DVknsq7URMMitsiNgUZuHnSlBM09PFv4ZH7Ko4FMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جملهٔ فارسی نخست‌وزیر پاکستان خطاب به پزشکیان: غم شما غم ماست
🔹
مردم پاکستان همراه با مردم ایران هستند؛ ما در شادی‌ها، غم‌ها، موفقیت‌ها و شکست‌ها با شما شریکیم. @Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/444310" target="_blank">📅 19:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444309">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37bbe0e8e2.mp4?token=oC0y1iNZo3i7kA6H5moQVpLpbKRgPTjVPVfUKGPCgem-aZFhoAqNRdYjmq82N5acB6SKRrs4H6JdjgnZVFgGBC2TgqS1YCf3ekEECE6dfuJLeZeUCkV7Gwy44yOrQeRH2ms4zMKI6muzCuSP8S8VSjD90Rne3JS21yPLed6HqWrxEITsmYEplZ0roHcGEgPLRe9ugSN0UQJ3dxpJ7IX1QgF6aYEaebCkW6vgqi2EbSoKQ54qAcYS2z9EHA_SfS5y2rOnYAMNvVRWAm3WcnUzehHvnEiTyuuyie4KYW8LX00bg41-OQwHM9EccqAdEuiwgXyChr6qQrbiu3yINTFm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37bbe0e8e2.mp4?token=oC0y1iNZo3i7kA6H5moQVpLpbKRgPTjVPVfUKGPCgem-aZFhoAqNRdYjmq82N5acB6SKRrs4H6JdjgnZVFgGBC2TgqS1YCf3ekEECE6dfuJLeZeUCkV7Gwy44yOrQeRH2ms4zMKI6muzCuSP8S8VSjD90Rne3JS21yPLed6HqWrxEITsmYEplZ0roHcGEgPLRe9ugSN0UQJ3dxpJ7IX1QgF6aYEaebCkW6vgqi2EbSoKQ54qAcYS2z9EHA_SfS5y2rOnYAMNvVRWAm3WcnUzehHvnEiTyuuyie4KYW8LX00bg41-OQwHM9EccqAdEuiwgXyChr6qQrbiu3yINTFm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر انقلاب ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
🔹
مقاومت مردم ایران را ما تحسین می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/444309" target="_blank">📅 19:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2efa8e227.mp4?token=RP-mLXSjvW-iijeDpe3a6347dcJLVMK_VSQEQveXg814bKIZ_y-VKPt5o3yjDIGiEfhnNsAxI_dX1ezO5ehA99LeYJdD3zJuqjZuxI-IVGeX7mKOoBoo2f9WpZ3H319CAUhtshrdKs470qHqa5eajh7c_9V4kqIutfnm5JKn--x8cTHZYDfZPZ3iWfHgwEYqw59rfE_rQJX0SwFL7rbc8lYeXWINWf21BoHD7DzO1DanZ9t5Jdw6TOe30Yk3gdUMNkTNGbTJgMhOO_AO7ZRj39Zwkw3pfOikiLWC_5Bz4UfPeLwgBL2MG7K0Hn0HOurC36O0EvadpaFtK96YFri_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2efa8e227.mp4?token=RP-mLXSjvW-iijeDpe3a6347dcJLVMK_VSQEQveXg814bKIZ_y-VKPt5o3yjDIGiEfhnNsAxI_dX1ezO5ehA99LeYJdD3zJuqjZuxI-IVGeX7mKOoBoo2f9WpZ3H319CAUhtshrdKs470qHqa5eajh7c_9V4kqIutfnm5JKn--x8cTHZYDfZPZ3iWfHgwEYqw59rfE_rQJX0SwFL7rbc8lYeXWINWf21BoHD7DzO1DanZ9t5Jdw6TOe30Yk3gdUMNkTNGbTJgMhOO_AO7ZRj39Zwkw3pfOikiLWC_5Bz4UfPeLwgBL2MG7K0Hn0HOurC36O0EvadpaFtK96YFri_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر پاکستان: شهادت رهبر عالی ایران، آیت‌الله سیدعلی خامنه‌ای، را تسلیت می‌گویم
🔹
ایشان برای ما و تمام مسلمانان جهان قابل احترام بودند. @Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/444308" target="_blank">📅 19:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bdb4f54c6.mp4?token=oI3VyK4gGQexSiZOwT689Uj_hNBJZdajEmu56toqRleaGpZ-5mL_4ZDeDNIABaUgavbYb2QryDF8YEWDc5kYM55_uKv6nS4up7tvuwTz3Yzy23DP0ABNIiOx5552aT3GFBB76gd3dZVmG26ss43JfA_PdNqrnZ9D95RnfRvkGwV0mySjKc7x2zoLGB5iCiRkvqtFpJ19Lw2D52mqyvQTOV2SRN4Ji1AbvRGa-GR8ySxXBEI-RCdh0DhyEBtVDKXs4MQo1_Ej1uZ2I8uLoABoyMyNVaYQ07OvLdIeY8xMO205BzKo2-7QLxf799Bsd4S3aazHE-G5ilPaHQeS1_AADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bdb4f54c6.mp4?token=oI3VyK4gGQexSiZOwT689Uj_hNBJZdajEmu56toqRleaGpZ-5mL_4ZDeDNIABaUgavbYb2QryDF8YEWDc5kYM55_uKv6nS4up7tvuwTz3Yzy23DP0ABNIiOx5552aT3GFBB76gd3dZVmG26ss43JfA_PdNqrnZ9D95RnfRvkGwV0mySjKc7x2zoLGB5iCiRkvqtFpJ19Lw2D52mqyvQTOV2SRN4Ji1AbvRGa-GR8ySxXBEI-RCdh0DhyEBtVDKXs4MQo1_Ej1uZ2I8uLoABoyMyNVaYQ07OvLdIeY8xMO205BzKo2-7QLxf799Bsd4S3aazHE-G5ilPaHQeS1_AADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای پزشکیان با اسکورت ۶ جنگندۀ ارتش پاکستان به اسلام‌آباد رفت  @Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/444307" target="_blank">📅 19:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما با تکیه بر ایران وارد نبرد اخیر با صهیونیست‌ها شدیم و با این کار، قدرتی را به قدرت موجود خودمان اضافه کردیم
🔹
ما می‌خواهیم لبنان را آزاد کنیم و حملات و اشغالگری صهیونیست‌ها متوقف شود‌. @Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/444306" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🎥
دبیرکل حزب‌الله: بعد از آتش‌بس، مرحلۀ بعدی عقب‌نشینی کامل صهیونیست‌ها از خاک لبنان است
🔹
ما از ایران تشکر می‌کنیم و به ایرانی‌ها می‌گوییم شما شرافتمندترین انسان‌های جهان هستید. @Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/444305" target="_blank">📅 19:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb26baee6.mp4?token=j1tW6pP2bHhPn3CMIREwadTgIuLxwjOs613mbLOZ5OFjmo0-t3p6zJixPQWNl81PmRPqJAdQ7DtG_aVCs9VCW6kWEjOa3seDklTjE1emvsgjBt2tATjH6H__Ak_K2caxrd_mo6cQC87QNt9QeWFHxvM2LgG7HYhy8-efMLQ53xEMZM5zos3ISE9S8TY01kHAPkOO716aIm-aj4vRKtoYRB4-uxls7GpQhavD7yrGfZQU5ictWDR3IaXBM4Jd4Ry-CEW9fqMs1iJk6njVH6rscH6vhxLhz0iAvhgXShwruqqqARTpkhOrFyqA8enmQ-iyfpXj1-DisgIe6rR9sZ6sKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb26baee6.mp4?token=j1tW6pP2bHhPn3CMIREwadTgIuLxwjOs613mbLOZ5OFjmo0-t3p6zJixPQWNl81PmRPqJAdQ7DtG_aVCs9VCW6kWEjOa3seDklTjE1emvsgjBt2tATjH6H__Ak_K2caxrd_mo6cQC87QNt9QeWFHxvM2LgG7HYhy8-efMLQ53xEMZM5zos3ISE9S8TY01kHAPkOO716aIm-aj4vRKtoYRB4-uxls7GpQhavD7yrGfZQU5ictWDR3IaXBM4Jd4Ry-CEW9fqMs1iJk6njVH6rscH6vhxLhz0iAvhgXShwruqqqARTpkhOrFyqA8enmQ-iyfpXj1-DisgIe6rR9sZ6sKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: تنها تضمین برای آزادی خاک، استقلال و حاکمیت کشور، مقاومت در برابر اشغالگری است
🔹
اسرائیل در میدان نبرد دوام نخواهد آورد و حتی اگر زمان طولانی هم بگذرد، نمی‌تواند به اهدافش برسد.
🔹
برای ما هیچ تضمینی جز قدرت خودمان وجود ندارد و قدرت ما همان…</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/444304" target="_blank">📅 19:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: تنها تضمین برای آزادی خاک، استقلال و حاکمیت کشور، مقاومت در برابر اشغالگری است
🔹
اسرائیل در میدان نبرد دوام نخواهد آورد و حتی اگر زمان طولانی هم بگذرد، نمی‌تواند به اهدافش برسد.
🔹
برای ما هیچ تضمینی جز قدرت خودمان وجود ندارد و قدرت ما همان مقاومتی است که بر پایهٔ ایمان، اراده و توانمندی بنا شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/444303" target="_blank">📅 19:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e6ca44db.mp4?token=VgNBEVK5e8olxEPuU7SHzaCNKnbhSJh3uSiZrtcY7NnDLf17zw_l8242cKEuI6vqEjYeS0g-iPqGS66yrldoKcX8aPaUWi8BKbWU87S19i6dru5i6653jfN4IhObHYpZgyTnsfJZTCn1XWz8FPafkBE_70Br3m6XGuj_MDKxFhj_Y5UNhzT68Qmdh64Cw7Das-Ka7yCQUjzUjwQxoQKaJoFgnnxypGqfS-T7JIgZ7NPALbJ3apw1pWiYtyRtDVMMCrZWzYGP5kUT1j0rCDVDLhlUe5c8wyQW8m12rhQXfeAF779EFnEhip5RqyrBEcbkjhbZb0Gf4jyOr05Ko2OltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e6ca44db.mp4?token=VgNBEVK5e8olxEPuU7SHzaCNKnbhSJh3uSiZrtcY7NnDLf17zw_l8242cKEuI6vqEjYeS0g-iPqGS66yrldoKcX8aPaUWi8BKbWU87S19i6dru5i6653jfN4IhObHYpZgyTnsfJZTCn1XWz8FPafkBE_70Br3m6XGuj_MDKxFhj_Y5UNhzT68Qmdh64Cw7Das-Ka7yCQUjzUjwQxoQKaJoFgnnxypGqfS-T7JIgZ7NPALbJ3apw1pWiYtyRtDVMMCrZWzYGP5kUT1j0rCDVDLhlUe5c8wyQW8m12rhQXfeAF779EFnEhip5RqyrBEcbkjhbZb0Gf4jyOr05Ko2OltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
سندی دیگر از جنایت آمریکایی‌ها در لامرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/444302" target="_blank">📅 19:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بستۀ خط ۷۵.pdf</div>
  <div class="tg-doc-extra">2.5 MB</div>
</div>
<a href="https://t.me/farsna/444301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۷۴.pdf</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/444301" target="_blank">📅 19:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43390b6bb.mp4?token=I1Q_T_q8wOFwnu1qvFsboCFBtHc_VuQzAxxWL03TBxtnidJsqEJ_LxzXl1-daqwoqzx7LsCnJa--glCUz4aKmkeo7W2t4hNLddJ3lkFht2_Y8TS4ZxKYwHP_Wdmo0iukhxg0XJx1UGx-00WNTU0y6renuVFIIstVom-413aJ-Gpoiz8eJTulDPpITImjiAO7mC27nmxmfB8O7dW7jbK-q1oqL_a2hbbsjaTww3-cszlBAKBNzK874Yxr7z-QjIRRDss0ZV70X7kBJP-Y6xB-i6cbVOap2qdF5_CuwYZbJOrSR2Wo9p9gazQnwHDNqzxwEBd2_3cyxQ9ANrQ0-Q0d0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43390b6bb.mp4?token=I1Q_T_q8wOFwnu1qvFsboCFBtHc_VuQzAxxWL03TBxtnidJsqEJ_LxzXl1-daqwoqzx7LsCnJa--glCUz4aKmkeo7W2t4hNLddJ3lkFht2_Y8TS4ZxKYwHP_Wdmo0iukhxg0XJx1UGx-00WNTU0y6renuVFIIstVom-413aJ-Gpoiz8eJTulDPpITImjiAO7mC27nmxmfB8O7dW7jbK-q1oqL_a2hbbsjaTww3-cszlBAKBNzK874Yxr7z-QjIRRDss0ZV70X7kBJP-Y6xB-i6cbVOap2qdF5_CuwYZbJOrSR2Wo9p9gazQnwHDNqzxwEBd2_3cyxQ9ANrQ0-Q0d0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار یک‌صدای زنجانی‌ها در حسینیهٔ اعظم: آذربایجان شرف‌دی پهلوی بی‌شرف‌دی
🔸
پهلوی شهزاده‌سین خار ایلمک چوخ ساده‌دی
🔸
تک بو دنیاده علی‌اکبر بیزه شهزاده‌ای  (خار کردن شاهزادۀ پهلوی برای ما بسیار ساده است تنها شاهزادۀ این دنیا حضرت علی‌اکبر(ع) است) @Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/444300" target="_blank">📅 19:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444298">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b87e7d200.mp4?token=ti1M5P1eiaQe_naouS3FMz80Omhfq9O_GuXrYzBBKo83EAwwKMV5V9Qq4AOpl-7_YOhOqpNQ89KVnpzh42nkNsdetFVeVfEWBFDcB8xOpFOC28QIkhUDkkToc7glpzGfMg6ueAq_CTTSSmwQ1tumxUu9PUj4qYE62KZhsi64hUH7KRpw9xR0BTu0GhK1ZlgrbxCtorHbPMJryUooUrWA4GXJoZ5hRSsxprIcjuGUxh_sKYSum_nlr0D_Zwj-SkA_J3lqdA3kctuBdrr-zOjerkJOjzeEY9V9c6L4AeZr0CGbgNVhVtT46g7H6H2Px9LV2fAWyebmW630aSUew8TmlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b87e7d200.mp4?token=ti1M5P1eiaQe_naouS3FMz80Omhfq9O_GuXrYzBBKo83EAwwKMV5V9Qq4AOpl-7_YOhOqpNQ89KVnpzh42nkNsdetFVeVfEWBFDcB8xOpFOC28QIkhUDkkToc7glpzGfMg6ueAq_CTTSSmwQ1tumxUu9PUj4qYE62KZhsi64hUH7KRpw9xR0BTu0GhK1ZlgrbxCtorHbPMJryUooUrWA4GXJoZ5hRSsxprIcjuGUxh_sKYSum_nlr0D_Zwj-SkA_J3lqdA3kctuBdrr-zOjerkJOjzeEY9V9c6L4AeZr0CGbgNVhVtT46g7H6H2Px9LV2fAWyebmW630aSUew8TmlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای «مرگ بر آمریکا» و «مرگ بر اسرائیل» در حسینیۀ اعظم زنجان طنین‌انداز شد  @Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/444298" target="_blank">📅 18:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444297">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9442cd8cc2.mp4?token=EmI6GUxBWputIrHbys53pwpjtEFQ5KdFQgeVMK6xjRlu0-1Salld1vaa4tO-rVKdBu-9w6WEHVKV953AmaL_GAkdUjBS6x9y1N5vH_zGf94hvA0mjmqRjjYKCTus0ybvG_URdncoHesSk9Q5C6YvXDy3MQUcn069l5ydwW7W6bhI1vNEVzhZkhUfW9KuueHb04VUB8rMA0AL09H1slFABC89pPwEGCHTYhJA1dv8YHNIs0J4QlxFub97ep_g_IPMPwj5axjty4ZhEdHjiBkDYgxJY7quutNpbmbYtaaTUOsqiZApPYukE6lgnjBe1mCnyId3uNhsV9aEACI95xxDSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9442cd8cc2.mp4?token=EmI6GUxBWputIrHbys53pwpjtEFQ5KdFQgeVMK6xjRlu0-1Salld1vaa4tO-rVKdBu-9w6WEHVKV953AmaL_GAkdUjBS6x9y1N5vH_zGf94hvA0mjmqRjjYKCTus0ybvG_URdncoHesSk9Q5C6YvXDy3MQUcn069l5ydwW7W6bhI1vNEVzhZkhUfW9KuueHb04VUB8rMA0AL09H1slFABC89pPwEGCHTYhJA1dv8YHNIs0J4QlxFub97ep_g_IPMPwj5axjty4ZhEdHjiBkDYgxJY7quutNpbmbYtaaTUOsqiZApPYukE6lgnjBe1mCnyId3uNhsV9aEACI95xxDSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
بو مقدس پرچم، آخر کفنیم‌دی
🔸
کِچمرم ایران‌نان چون جان و تنیم‌دی  (پرچم ایران کفن من است از پرچم ایران نمی‌گذرم چون جان و تن من است)  مداحی زنجانی‌ها در یوم‌العباس @Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/444297" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444296">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
جمعیت عزاداران حسینی در مراسم یوم‌العباس زنجان   @Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/444296" target="_blank">📅 18:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444295">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23cec62f.mp4?token=MPup09aOhks0Mdh52Jt0kwfJgX2ztDJ6bD97NJXLWJHmqUCsNK86mM4ZVqamVNhOVSQQvXjEE04VzTSAnUgm5bODzWQwoVHJFnCMDyCBwQJDt89yGwwtj7VRvpVoVCC9VD9VceqPlOoOh38UuJOYB-_ND5qFB3zlwX0i39oiwkzBymPi-aBQKrzEmPu5P3jUSf6s0hSGRt5lBXg0tS7d3PJOg3TJ4S5_WI0t2ANXK2J05F7ee2nOVyTEHqxtrLdvGYJRPxh60p3IuubYJywwdtTA6wZXqzUrbbcEfrvGFcBf9KDGxS3k4-GrwnPoEUFxMokivT8aAsLxS0VD3nMGtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23cec62f.mp4?token=MPup09aOhks0Mdh52Jt0kwfJgX2ztDJ6bD97NJXLWJHmqUCsNK86mM4ZVqamVNhOVSQQvXjEE04VzTSAnUgm5bODzWQwoVHJFnCMDyCBwQJDt89yGwwtj7VRvpVoVCC9VD9VceqPlOoOh38UuJOYB-_ND5qFB3zlwX0i39oiwkzBymPi-aBQKrzEmPu5P3jUSf6s0hSGRt5lBXg0tS7d3PJOg3TJ4S5_WI0t2ANXK2J05F7ee2nOVyTEHqxtrLdvGYJRPxh60p3IuubYJywwdtTA6wZXqzUrbbcEfrvGFcBf9KDGxS3k4-GrwnPoEUFxMokivT8aAsLxS0VD3nMGtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم باشکوه یوم‌العباس در زنجان
🔸
حسینیۀ اعظم زنجان در جریان جنگ اخیر هدف حملۀ آمریکا و رژیم صهیونیستی قرار گرفته بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/444295" target="_blank">📅 18:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444294">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d9848065b.mp4?token=CTNGnqs7IP5hgvzstq7sNkk7LqglI1ZiALZ4QUrYsON2gU9W0ejnnazNZ-QQuNUplzNY3sKQZvyghyLV3l5lI4kdiR6cGDi92AJQHsyKZgnMpEfu3aIe99znGIjJPlMhlAqL8xG-w9NJcVH8JlP67z3oWHBH3Tz1pFMvXAXx9H5Ygy_Tn3GyodLKT-ZhbemZmCom6LWGh_bzbsko-CBW1PJ1ESiREyTLVPnCNA8zxnTRV_bWREjhD9XwjtVljsGq767af5xwP05LZe9XlvKEd-RjOWUgOMALPCksOYfVPm8O042F4DjTYxMqqY8VIqq9IYR5HgLZTsNaw8fb2t-New" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d9848065b.mp4?token=CTNGnqs7IP5hgvzstq7sNkk7LqglI1ZiALZ4QUrYsON2gU9W0ejnnazNZ-QQuNUplzNY3sKQZvyghyLV3l5lI4kdiR6cGDi92AJQHsyKZgnMpEfu3aIe99znGIjJPlMhlAqL8xG-w9NJcVH8JlP67z3oWHBH3Tz1pFMvXAXx9H5Ygy_Tn3GyodLKT-ZhbemZmCom6LWGh_bzbsko-CBW1PJ1ESiREyTLVPnCNA8zxnTRV_bWREjhD9XwjtVljsGq767af5xwP05LZe9XlvKEd-RjOWUgOMALPCksOYfVPm8O042F4DjTYxMqqY8VIqq9IYR5HgLZTsNaw8fb2t-New" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر انرژی آمریکا: ۱۲۱ سال پیش، آلبرت انیشتین مقاله‌ای درباره پدیده فوتوالکتریک...
🔹
ترامپ: هیچ‌کس به آن اهمیت نمی‌دهد!
🔸
وزیر انرژی آمریکا: نکتهٔ خوبی بود، راست می‌گویید.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444294" target="_blank">📅 18:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444293">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فرماندهی مرکزی آمریکا: ۲ ناو آمریکایی در خاورمیانه فعال هستند
🔹
سنتکام با اعلام تردد ناو هواپیمابر یواس‌اس جورج بوش (CVN ۷۷) در دریای عرب خبر داد که نیروهای آمریکایی با ۲ ناو هواپیمابر در منطقه حضور فعال و هوشیار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444293" target="_blank">📅 18:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444292">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_LM4cSrXQ2qWUJYJ3S4FryuFWTyhnqxloHqHAdYQoA3Cr_LTfF6DUJlbOdtSObOuhBROveBa1NywDZA0khrdcD0JGVr2D8YLmyu1tlvrWOeZZHGu-xRLGqrlzZI3deQ6gnZNXIBGbQJp0g0ZiS6034Dr9TxeNnfI__TTrhywb0bgLGZFuoUjIs75GdlnmSNAJ4UpqGAy9xUy9GPOAVZDMZfMZ-GEdenDlNwAUkS64pQ-hjWP2EvriItl5eyVsXuRfbld7lya5Iscu4-AlyaplV7j5OUpulZqH4SmePlaDe57a--7BLyUQ1tcv3V8dbBtX7GL38u-7I33a7__KqMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جریان سوخت‌گیری در پمپ‌بنزین‌های تهران عادی است
🔹
پس از اختلالات ایجادشده در شبکۀ بانکی و پرداخت موقت هزینۀ سوخت‌گیری به‌صورت نقدی، فرآیند عرضه بنزین در جایگاه‌های تهران به حالت عادی بازگشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444292" target="_blank">📅 18:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444291">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d0b10e2d.mp4?token=HjpQCgt5yYyoyZYWCjWzAmZ-9FixCtZeGmZoQC1-YERbP4ZZ9pjqFU2GMiWaTDkRDzUMI-VK5qo-fxlF8DrsUwT4Ezup-fWITMDoKsN9DcYulc7wTucTa4AKYef1k6YMcZRWyjxL4em4Wz9ihQF03QmxIqSh7tF0HaXh61D84M6VTLM-w_YShiOWxwnyXOHUma6OKJ2xc9RtvSMaDsmxCeJW246i-rS_8knC-ib6KUETm10XgUjgf9XEprYAgfGWNclSkOe026yCm2Q8I-KjHcbd4G9HXu21HwALlustnNqiTH702ngGjUaCvrRWoricKm9rd7UV0azykR-JYf_8vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d0b10e2d.mp4?token=HjpQCgt5yYyoyZYWCjWzAmZ-9FixCtZeGmZoQC1-YERbP4ZZ9pjqFU2GMiWaTDkRDzUMI-VK5qo-fxlF8DrsUwT4Ezup-fWITMDoKsN9DcYulc7wTucTa4AKYef1k6YMcZRWyjxL4em4Wz9ihQF03QmxIqSh7tF0HaXh61D84M6VTLM-w_YShiOWxwnyXOHUma6OKJ2xc9RtvSMaDsmxCeJW246i-rS_8knC-ib6KUETm10XgUjgf9XEprYAgfGWNclSkOe026yCm2Q8I-KjHcbd4G9HXu21HwALlustnNqiTH702ngGjUaCvrRWoricKm9rd7UV0azykR-JYf_8vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدرسهٔ میناب امروز به میعادگاه آزادگان جهان تبدیل شده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/444291" target="_blank">📅 18:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzi6xcjapTh0jYwBEKNkcv1m4yVxWSAqNjwENwQAMbVwxvZrY49fZKK0FPz1uqMIr4xjHK5DBBXXuBE92FyxswsOLWTF42Riv_30GZ2HKE5m5OF1izc36auenLJJlksPEU1nTRCDq1PnwHDiq4u_ItQYKSqTj7VbVDfylkoZ6bW-litVwnbz6s2eA7hPoXdUDzUKgHLGb6t9dYtUrdH0pqwS9SwpOPiI4JuoXKh1aTV844vkF15R4PFj9Z7Do5CSTgswtc7uzwwQCJoaZsRZTGrb-LE__50TUOkLUQtyo1qB_3f4a9k3L-We_IGQUWhphZx5FHjqA5jqokPlp1hyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4f1l5OOzQiGuXZTESCq6Tjpu5CBImPzpi2ytT3gSwh0V7eFgAK8_TCZD80xr490r-iY0j-NaFM3Xb6kkG4OvXOLGIvPw7j1sJFS9kYQt9diebvY_C_bHRdLmfD3cXLjLLSGwZcu6nSdIhUt3wWnnPeFIaH0DCZZymMt__BKi3DeO3UoLCHr0-ajQ7erfqgm99CPdhQO0nHxeqgTRMZKhqdz7I8f6tuyVOSkMp1ZMcrZmOcRcbnu4-84Zosl3-pVUwOihWTwarZNdenjhFs9c-pGbI8ubbdFbULeC20H4n0dFFol64G2pB8QopZCkXRER9S7Ju_c06rmi4uLsfpqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivcri7QMOhlBKJInb0MZU5vg57KVHekE-p4S6uQh8uKzuNhq2ajyX3w8Q1BH3RXTbZr6WNp8MoLC5bCpIouObS40hbPO-KzWNSqhxVL2qKez4Og3cBNFLTMkWR5qeY21ikMWkj4vAGFabZ4kYaVnMahSfeW8TtwnbpiieSYcOIQIKVcuP4hJLgNWMazB2Rs0Qe0s3vo5ZNA1imNe4u4NyFhWC31s-joYKkdVeIGwCAPyRo1weWbeMt8JdCbocz-npTSw5Aw34As3DLl-zo0j7erpDJCnuSa9Xc1eK9WNqh4BdkPtf3ZNbadv3rObHSzUf0gaVIphvWInuhqHJzDJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL2r7BLtNIs0uQSCWGsiGcfBaa8mooXdrDetjRFRbDh5IS_HQQCCAFbZtiNAAgXFMDs-hNQm6J3oyApL7i4ypP21PSHmMi6BMEKs7214RVMRaaZssoQS5cN5fJWRfkmoBq9kob_ziJSFMOMRfcTqiR9-C07yBE2QxIdfs8YvFi0n4qtuMuV8taZZxLpUX-JNeONqDOZZFxdcaloGSp5iyfnyU7t92NjADyDhp9LBZ0Pmkrb4XyOUZeXBZ8t4Ye4WxYzCgy8BgPX28h5YlY2fL8l2Hf6IJn7zamG0qmKXWax7FxzaSBEbnzDPm-Cu-AzucYGcifb5yhw010wvENOkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFzDQ0Dnmg6xGthK3UFgF9YheaU8zvh29RsZ1sFkV1nCHswJN44C5bgCU1_5CknulHscMARHbigXfhIQWKoK4fBje4ZvYsHHfuqBAF5nL3eIFTWW8q5bcdnfgdtud2euTqdptTf__X46p9XTkh1pMBQJzrl64Hub8Ig0pEKSAC2JpJpAsj_v2Bzk4aLAJC3GR_B4FoVz6y3KhArX5DR__FoSMJc5HnAoJEuM8pkAd1NaVb32ntMlqZYw-Sh82_kSIMLmbO7ss4SoM_7c9UzWIG4R9jhk0T3qgqlkYR7Zbgx3J3-mtDlXKkttTYIqW33jj8NOiiy0pUXs9oi72UGsxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دشت آزادگان غرق در عطر عباس(ع) شد
🔹
مراسم یوم‌العباس(ع) با حضور پرشور مردم دشت آزادگان، جلوه‌ای از ارادت دیرین خوزستانی‌ها به علمدار کربلا را به نمایش گذاشت.
عکس: میثم گمراوی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444286" target="_blank">📅 17:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82297da050.mp4?token=tiQy5M5nk1weW0LSJkz-diH9or7ErY0wyQOrEHZYYlb6uMOW6wN2-z10kxR6Nt4JPs3wbczpVBh26SPk9wBArL1evUrOO32Ntza0gQvLefHksdlhFK5GZqz7MidWN4wOKol-2gNTIxO3p2WZDl2LQTjqDXzXH-fZQhEkFDdlsS5FUY8j2cm7x2WvLiQwoi5J7F-EGG-sWd5uh6mxIEXJFAhj9PAT7-JIT3NIre4Pcr3gHkI_a30wedGoBSeNHTguU6vFXdluE8WYnQJRZnrGNGH2_P4NoOCOxBwrtDcdP2WHJJgeE0qihYbCuIQPAk2CujeWEHoeL6wjsfeyr58Qcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82297da050.mp4?token=tiQy5M5nk1weW0LSJkz-diH9or7ErY0wyQOrEHZYYlb6uMOW6wN2-z10kxR6Nt4JPs3wbczpVBh26SPk9wBArL1evUrOO32Ntza0gQvLefHksdlhFK5GZqz7MidWN4wOKol-2gNTIxO3p2WZDl2LQTjqDXzXH-fZQhEkFDdlsS5FUY8j2cm7x2WvLiQwoi5J7F-EGG-sWd5uh6mxIEXJFAhj9PAT7-JIT3NIre4Pcr3gHkI_a30wedGoBSeNHTguU6vFXdluE8WYnQJRZnrGNGH2_P4NoOCOxBwrtDcdP2WHJJgeE0qihYbCuIQPAk2CujeWEHoeL6wjsfeyr58Qcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اختلالات گسترده به بانک‌ها برگشت
🔹
در ادامهٔ اختلالات ایجادشده در شبکهٔ پرداخت کشور، امروز هم گزارش‌هایی از بروز مشکل در خدمات کارتی و موبایلی چند بانک بزرگ از جمله ملی، تجارت، صادرات و ملت از سوی مشتریان این بانک‌ها اعلام شده است.
🔹
پیگیری خبرنگار فارس…</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/444285" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbRNBzkf2qq3gdmIQQ7UaHcvgg9bWf_fENVKteZJhabf7zZTJumw3eD94BlyV4H7403o9ZvFNdc4SxyONID_odEEE61cplnbGQmz5Z1HvWae_eyC-SK034dIZf4VZALpA4Nxdt8w9oGmxcuiLvgy_XaKd5n59hC8hutyvkL74LaXPZo1PEZmpDiTXuQ1qnFGOgrAGGA0pfMETGDOo5Aewaw1cSt7gqCNKO9NAcYLRnEj0nQ5sPXPtjvhutJUfIyfQuXZsOvyAc0NPXURIRl4I1eSG4BDz29g7phLmFt_29J7Cce1RBdvsBv5ljk5jIhx8JMcT1qRDQyeEOpm4CDbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط پیش‌فروش خودروی آریای سایپا اعلام شد
🔸
مبلغ پیش‌پرداخت: ۱ میلیارد و ۷۴ میلیون و ۷۸۷ هزار تومان
🔸
زمان تحویل: از تیر تا پایان مهر ۱۴۰۶
🔸
سود مشارکت: ۲۰.۵ درصد
🔹
ثبت‌نام از ساعت ۱۰ صبح روز یکشنبه ۷ تیرماه در سامانۀ
saipa.iranecar.com
آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/444284" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
