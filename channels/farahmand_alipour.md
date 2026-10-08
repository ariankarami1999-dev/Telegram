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
<img src="https://cdn4.telesco.pe/file/ZBKwSSKyFaDo5gZTGFIejcAyq4jjwfFXZfiCoq1rsSGeBNL093Ym7vKRxV8Rwi4GzvKN0CoMI4HC1aCWV25aqfgNVuwLtGx5QVnZS7usU2sM8zbMhN3FimQN3i_9_iOUWaBpS4ORuM4WNtwJMiX19ULc2yeEZMQUZ8oJh3Lz6pb_V62paqzWni1GFMnmMwGeMBnA12-FHChP2GHaau80xMpBo4-Gqs7qdf7Gh52BEbCqZgheL5DgmlIvbpeHeDC7dAGCjmGl00qIZGoWEoPuVRiG0PWU6K2R2y2HbyJ0dP-9PMLJ3CIh9uxsR1u3qUl4EnhO2JV2Ww_ibUyUUhdabQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjieEiAjGYQWiSrW_5QermMUVTcElQhZbpBSd8abhSA9Lw4rP5DxvFy1tEyZJKR15NNHv6pVAd7HDgx6AyiU3-NelEIEFtTeOCl_8M0EgY5CfASWWNhN6HmxoBPq2nelavRL3xP6DTQ5mjMulTTNfNV0E8YOc9rloiflcJcMN61Q7USnm4Qqy9yVIZEflyWcHKLTvyJx-LchBABCXfZSNE18vEgJ3d9RT8Q-CBOofQ0ZwoZZFM6N4j7zJvcKrh6cOtj_J_AKBoDbXG5Ad8cjqtAy8YbfG5Zwd5bZ_5eu4sO7EpvClwt4ffMPDl3SakIj7zs9LvKNWHNbxXTtb_LUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saHKT9WHfAweYBYPZBkG2Srr6_j2XWItyGYb2ENaKaK5pOFr519WDyEUSN3JXK1ZNr1tNuRY7WAEupy5ZYbnXnMSJe7S-9uu_NQzXpc-tJhv5Zi4ZQzmIUgdhEaTdAQid5FK7HYi59qzAW5EAae2uYlvfJjau02IZWEiL4Az3p70U3xO01uDsXaCIMbX-rqN1MyR8nU6QZCaWW83cnsgNwrqe79i-DNVMnPF3AISQ0vbZ3czN5Leh6G_tpNoUJncfhpwhpasQyzgqGfp2PPV1VytUC15WuIDNyQuLuIP1aIou6pColSjEngsDXlQzJGa0zD5_vf-trnjv89fcMovzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=XPEexr7JweO4PzlMvUsAvS74MBIXlukUwvzZLD28ryUiA1HEKxQJiH312uCXmBfs08zxLtFJYqKdOR9gkXkaDLETHs55IAcrh-iGzOoP4qCbAxzsKTCrEpyuTZ4rj1r1F8WqUBuJ23NUMXLzhcWHce6o5Fn6cVqeIRRhV_DnmdYGRQAyUzWLu_Bqpcu4o1aWCzvjosrA-PpWaN9lUFyYkOPUwWSBky8YWQiCa9vgzd6nzVfrChln6y3HMKINlSsaqUAk5zVEZBZVUYmPb7wE3bTnbtrutLnNDY3lo0-DIRiGvS7L-RDv4gRyoZTGMECpHAMPqkREWdVRwm2iqv4K6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=XPEexr7JweO4PzlMvUsAvS74MBIXlukUwvzZLD28ryUiA1HEKxQJiH312uCXmBfs08zxLtFJYqKdOR9gkXkaDLETHs55IAcrh-iGzOoP4qCbAxzsKTCrEpyuTZ4rj1r1F8WqUBuJ23NUMXLzhcWHce6o5Fn6cVqeIRRhV_DnmdYGRQAyUzWLu_Bqpcu4o1aWCzvjosrA-PpWaN9lUFyYkOPUwWSBky8YWQiCa9vgzd6nzVfrChln6y3HMKINlSsaqUAk5zVEZBZVUYmPb7wE3bTnbtrutLnNDY3lo0-DIRiGvS7L-RDv4gRyoZTGMECpHAMPqkREWdVRwm2iqv4K6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=gr4RQrVTUaT5QD3rE3L3qccM97CCfGfI955KRmGp8JrATQnLx3w9q7vzL1A2hBQVpHwLbLMyXsfdtzyO3OsH1rTMIcta9yqZJnNojRt4fI15ZArP_TIQjmN8MBY-s3MnC4MxoHWBOr1p8M5ZWNrHvSfIGWGiyNi3y0h9ubgPX7GFDGCQnp5c7yBqH7-eTd0jq4aY4Ci620vhOiSso38v8XhFoW4hJhYcFs3Yef32UgmuJoHb2GED861Ho9QIMZQEFQdwuGS1NwXmIaOdJ7loDOpjBKF0XWQUpt7rkHNIGLmHhBDPp09Su3ZhDhPZu0TKFksReZY58qoA2KpOjujIGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=gr4RQrVTUaT5QD3rE3L3qccM97CCfGfI955KRmGp8JrATQnLx3w9q7vzL1A2hBQVpHwLbLMyXsfdtzyO3OsH1rTMIcta9yqZJnNojRt4fI15ZArP_TIQjmN8MBY-s3MnC4MxoHWBOr1p8M5ZWNrHvSfIGWGiyNi3y0h9ubgPX7GFDGCQnp5c7yBqH7-eTd0jq4aY4Ci620vhOiSso38v8XhFoW4hJhYcFs3Yef32UgmuJoHb2GED861Ho9QIMZQEFQdwuGS1NwXmIaOdJ7loDOpjBKF0XWQUpt7rkHNIGLmHhBDPp09Su3ZhDhPZu0TKFksReZY58qoA2KpOjujIGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkU7GP-7UdRPPrkQxpLzz2Ubr7NZLzhYLK5ylbjiGMH68dQssEh2c8-XBy9VO-OOiWIUOLdMrJxJk_MJWSGsNvdHgM1mmySixaOQGJoo_Ky_EPA8j4R-DrtTEljhYectwB-l_NsJkYdHZBJ--SXN-6EhO4hKyYAI6zvJckOK1jAC-Jum7LE6O_3rUug1ckOh5BLCGYjDLEfXrNvz38T_DsPsHt0C4lON6Puj6u88NBrh8jZyS1PdO5pZ5lWG6zXyVr5FdubYOlDEq7YlKt0KIsUlx11dxVDIWfcjJ37KqGyCYU2CjUeR1DxSPsXWq7dX69Pw81lCp9LZD-1r14kOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz2_RKwSWjDv1K7AXcWKMF0Z4zMOk0YprDBQZ84zBENhdzrobykC9gIg_bEKMgSPtUkDpLBOnNDm2QDxcWxnhp7l2vA_7sQGHOjS8oLeE58JR2nay2I18RU6jB5na9Bu27gFXUD_-z-jLopbxc4OgVvA_-U2sZLMWRdupFjz57lwFm_2QPRW7fip60X9FFKdpAfyLu1gSisaVSZvcA3ys13QyRJI5UHjqap15Z5Wp-xIfMgEesP2xSd2I4E6wBNZNRvlyhV3TVQYM60VJn3vJe5L3yHZXl-8xu37fh6ke99OBU-qcpftvWZwPJJ3p0ONu4yki9d3-XuEfRfzlPLPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=mxgo_UurUnLh_ovBYkNn3e_ISd_qYUsoi1ppQab0c7DpTX1kTqrEOCu1IOZdz4hwv4-zIpim7Jcz4i_Nwy6MQ3r_J73yj6GRAoKZzGjM1QkcrndKrnTRgs2IHIS11FLBor7OIOwTORr0TZ1Rt7WJbnt_zNZhmd0uyCH62jr3JHepDxFEOq9_663fjtkeOUlFn7YPWiXqR0DCUh6SQHwqAo1LE-v4Vdqtkqrlbiw66SZDV1cRdfiCzUNhR_JQvK0c6i5v9JkZ4ZXsAVt_fd-r9pyECtLepOcXYkeSbb6E31pVxDPQtl_i_0_LhJDYwxbhZPOY6bJNgw5AkGUjA8Mzd4xsK0gxloix0fkloXxBu7vYcEawd94FOnAzXX-3XXVWkZKB46iwxRdrhJ6b7RwsxlCF3KBQSzIbNomH29F2Q3tx0_EsWXg1f-_W0YXeS-8k-Na-Y2VHVS60kHLwykbs80vLRZiLZkYdZRFwEkwNtGMk5rVKNmREsqN8laG0n0f90AxgCvH6SUMcllGLYk-0aH8LeHgU3tXU7bLe_BFuH3CMWUfzkEoW9o6ZfYJFzgMFL-DXoa9Vq-Bsz9ac6QyAAUCF2ngl6a2RemZqgp0CCGQJ6r7BYZPClcvkf_v2QHXYq6zJ95zWf6lnrW-CI9PrMOpvT7EbalYRw_6NUgYHpMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=mxgo_UurUnLh_ovBYkNn3e_ISd_qYUsoi1ppQab0c7DpTX1kTqrEOCu1IOZdz4hwv4-zIpim7Jcz4i_Nwy6MQ3r_J73yj6GRAoKZzGjM1QkcrndKrnTRgs2IHIS11FLBor7OIOwTORr0TZ1Rt7WJbnt_zNZhmd0uyCH62jr3JHepDxFEOq9_663fjtkeOUlFn7YPWiXqR0DCUh6SQHwqAo1LE-v4Vdqtkqrlbiw66SZDV1cRdfiCzUNhR_JQvK0c6i5v9JkZ4ZXsAVt_fd-r9pyECtLepOcXYkeSbb6E31pVxDPQtl_i_0_LhJDYwxbhZPOY6bJNgw5AkGUjA8Mzd4xsK0gxloix0fkloXxBu7vYcEawd94FOnAzXX-3XXVWkZKB46iwxRdrhJ6b7RwsxlCF3KBQSzIbNomH29F2Q3tx0_EsWXg1f-_W0YXeS-8k-Na-Y2VHVS60kHLwykbs80vLRZiLZkYdZRFwEkwNtGMk5rVKNmREsqN8laG0n0f90AxgCvH6SUMcllGLYk-0aH8LeHgU3tXU7bLe_BFuH3CMWUfzkEoW9o6ZfYJFzgMFL-DXoa9Vq-Bsz9ac6QyAAUCF2ngl6a2RemZqgp0CCGQJ6r7BYZPClcvkf_v2QHXYq6zJ95zWf6lnrW-CI9PrMOpvT7EbalYRw_6NUgYHpMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvG_MmqYw18OWuvXMyX_-x2nIY5NjEMYWomy-V2iZcD82mDSzopcBzVAbgCELFy5ho3rYbP6wrPha-EASXRMA3i55snhpwTJ6Ym4xD3HkFTr7EcmnbB9uAnotYlPaqjaDI1Rulor5ZdVMZddbr-kPixR-5wFmoFgSsx59vCJMRTIPmRViqmUtNjEzz_hCGvjqRiScfNWQ7x6S_MhLaydzojTC48aDId7kXApdN7m8ME43Vgxdrb-q7ob4JD_PBVz0oeIIVqEofbvgh-Q3sCVM20IYxc2DlTf5slJljB9ZL-A_m_csuzTE3QSGBq7gXDQcP2qgVFY5PxTugyGAUJKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYJdRgFd8d3DmYRnLZS78hdAnxtdbKskJQ0n7MsffybgVJOVmZKcyfYaaIRddo7eG6VSE9fRdlhR27zzIuFRxHnmJlT7LJ7E6BI2rlJ5SGpRABaJc1dtlc97Lhd3XIyDhtqSEtjGE8rEALd6rJPj5of16cVYrr7NZ3HvVtozwJEYY5VUlQWojf-0HOpCMnap2Nzm_cX3u7PZs3Oeb6kLcSaLTx47MCPn5DPsMgFFhkl1LhEEcBWG2OmfaCIyvUZVLnQOeZOHNgnFD23dn_MC7DVuGB1YDKrmU1_kZy5Jnkyyxc-pRqifAfXAY0EJQs-4asNnFnoNtbv9L_wX7tWHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpi8Ii19b2z4GHOqwMJNsowIBmCl88CLlO2yK9NhciP7xETvZHtiFrNjw6IuLRNT-85HCNtPsGSw3onGrECWmq8Hgv_qujAnaObhs5gleTrTWtKEiP5R9CVu0wy-2ft3P-zvUnd8Nt23OOUcfQ6kWbUT9UXjEjX3-I20rD_vy3iBAMw1-q4SwcYMFwrzEIW7DngLVDWCRmsV-PgWXAhlaMIsm9Q-qL2_7e0heF4T6qQ_MRQJ1cCziFfyY_JY98IOv4EQjXkBC0sLwIi--E69xu63XxhnxW1CyT4WzzkjVFfMqsTIgcZwWiiGuAwegNQQaA2fyYtmoA1shOVaGl-qmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlRvt1TxSVWp1iohvXnkGKi2SBh1GOfJmUCZBBbWdPa4Cu7wKpPG0WClmreeZ9_htHV_W7nM_0L06bmyGxVOrR_cULTGjMpmVhbZH4mZeiHSDg1o-couPw7ao_FLWHVZQN8W9CM2Pb01kjaEG29GbWr11DoyF9GwoztbYE0-irlstad9ekTgp7b_4qPUH-zNHiBA8WGVSGIGCnsNOmkNgUvMgl5U1n1_su7D3QCTNo0xoyNrUvEw2xZQMvWchLIVmHYwTcfLXLLSyDWJeaneFhD6ZoracCHmwdoTFiv8k1VvIrVoUwSKeu2WfcNaI63f2N27TJy-UqWcraIjVqxnoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiGk6ynIBWfx97j_8VKc2x-k708UaHBdtS02gaXxuv6u7c7uO53QWRGBtbWLqpf4teUadAByk6KO4NzVWu5X0Xmgw0K-oFEmvpSmDLiphimYW8mK1xdvqRawKkzqPvUJaH87YW9HOjNpz79sJdAalIDZpfCgt-PA9zrcmp17vaUiqCGyqapvhN4fOE-77pSyp9wsaO2y7-r8o0mzUfaITvuzlJr3j-Efi5QZxr6h7P5QMfWqT0c4SAO4wGJtNC5HB3XVYr-yF4D9DmBZWKY5glsqknGExzWr06oewy5H2S741H7zWlYcvgW6Fo8WHqN3S-znn2PF3DnOTOB8GLwkHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwLhJt8xCye6H0WlWoYnRJRphuO8xvAG9F1M-Uhd43KScvpXeiMoNLoJePHSxMC8MEPNmD36d5XCNe00MXX9Exeg8g0_M0nayxbip5ty9iauwiDN5az_uqseR45juJpuJiKGDqKegcJp1A3PXqBla6Vl6AqwnpbyH0FVH9OqfLHIJjFma2q490BKhMcC8RRSJC3B6fK1SAfe1BW-_PmOJi_TQL-l43JJzb8T7HHORnfZFQuOSRp0sz-imxS7OrTLESCUm59vU2pnm6tqmEqiGmQMPIFaOthUsgPcMJUsYDU3LJuLvzx6nd1VEb6OgOMA7Jag0FYM07gWHnPwEY_g1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=bW_LrKmGINRUekHwcQK4CEoARssZVp2mDgu2atIdxO1LDSefdbp9T0GuU6XblaQhFBLtKrgtfM97yGcExDlze1PpaR7RNamgwxXqx_DO2hVEnxoAd5MPxMwBW1gCENhhUaWe1RTLJXnuxC7i_s8acWg0K0tt9lf3gU5ue4gNlGHmBYZQLi6ILzfUR10ze56P17Qtnj1gxh5CCzK489JKukddt7CHiWUP6l_1Vutx8XXSUU9MY33f-3aUgN7RVAA0yRJ9BdZn99yXA68GWpviprsdBkzdZgHL3OHfvgneYPREFamEKK5sUn5_qmKfyQPE7zE9K6MWDJrNXx36VsDCnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=bW_LrKmGINRUekHwcQK4CEoARssZVp2mDgu2atIdxO1LDSefdbp9T0GuU6XblaQhFBLtKrgtfM97yGcExDlze1PpaR7RNamgwxXqx_DO2hVEnxoAd5MPxMwBW1gCENhhUaWe1RTLJXnuxC7i_s8acWg0K0tt9lf3gU5ue4gNlGHmBYZQLi6ILzfUR10ze56P17Qtnj1gxh5CCzK489JKukddt7CHiWUP6l_1Vutx8XXSUU9MY33f-3aUgN7RVAA0yRJ9BdZn99yXA68GWpviprsdBkzdZgHL3OHfvgneYPREFamEKK5sUn5_qmKfyQPE7zE9K6MWDJrNXx36VsDCnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=JW8kC6X9SqRWp1-K-lYC5EmLNiqFRzc28yrPPVldcG7TaDBNofhYBwKHkU-JZgtzpPKjP9GhardvTFP5VRPpsdGw3kfCuqrRM9ZxoN3hXxnc8uSEOxhuKDzrVCg_-MNG1zWEKkDU4EODN9eaQ0QIBWckbwsBTcDo5QphUq15sV3IVLmNttzf4xMDPGo4AjP8g3oMxl94sDJvqKNtEJ6TgWIWd3aw9y5r5eORwWIvUj3RNxowQZu_kh50DthpmEad5hlUuw8XchydcNIpDOx03GLKC9jNevNWsSv3JPkR6p4fF7rHrAG_rumobeHupbAU1MvkiEgpmqv7LUdMnF-IW5PEfZiCQ0A8WuWpx_NRZoXNH8bIXZl20VwoMmVbqY79P3IQXzV2k9y01Yds1Y2BFGbfzy8_uXJJrd9vmZH-g0JfPZ-17_tdEC5ZRqcaqE_VC3vcjncoX5iUS6zLAY5OfU_HwsRRGJYC1lKuUpwhgeSQtuK1HvcPiJ0_doqIJWOcxR5LnuI2aO-0sUB2Axb2hFzGWyI3iKvCZ3ALs6v9qGphEblw5ZUMX-ugle8Xsms5A0P7k9maDldis3CCY_CZeJc3NdPF5NwS3vDL-jbItcwl1fnwKjPK5g-47u-FD8_TiQMbpIFjsUIPE3sp0iR_Yhc7OfuIn3ftDo2Q_uwBPqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=JW8kC6X9SqRWp1-K-lYC5EmLNiqFRzc28yrPPVldcG7TaDBNofhYBwKHkU-JZgtzpPKjP9GhardvTFP5VRPpsdGw3kfCuqrRM9ZxoN3hXxnc8uSEOxhuKDzrVCg_-MNG1zWEKkDU4EODN9eaQ0QIBWckbwsBTcDo5QphUq15sV3IVLmNttzf4xMDPGo4AjP8g3oMxl94sDJvqKNtEJ6TgWIWd3aw9y5r5eORwWIvUj3RNxowQZu_kh50DthpmEad5hlUuw8XchydcNIpDOx03GLKC9jNevNWsSv3JPkR6p4fF7rHrAG_rumobeHupbAU1MvkiEgpmqv7LUdMnF-IW5PEfZiCQ0A8WuWpx_NRZoXNH8bIXZl20VwoMmVbqY79P3IQXzV2k9y01Yds1Y2BFGbfzy8_uXJJrd9vmZH-g0JfPZ-17_tdEC5ZRqcaqE_VC3vcjncoX5iUS6zLAY5OfU_HwsRRGJYC1lKuUpwhgeSQtuK1HvcPiJ0_doqIJWOcxR5LnuI2aO-0sUB2Axb2hFzGWyI3iKvCZ3ALs6v9qGphEblw5ZUMX-ugle8Xsms5A0P7k9maDldis3CCY_CZeJc3NdPF5NwS3vDL-jbItcwl1fnwKjPK5g-47u-FD8_TiQMbpIFjsUIPE3sp0iR_Yhc7OfuIn3ftDo2Q_uwBPqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arIxxu-gETUTbNtKWZB3h09XpfZZIJeUd1mJ69JZXCtpNh6r7QiXsOX6obcA77cEKz4vfWVh8CDNAFZH9qHs0Blrqiv2_vJQDOANW7Eakvm9PTD9qugEm8rQehYCSPcTQFiw3NpTHqf5EVuIpUE0wyE_feVTI4qez1yTH1BLxuyyZV3cZiOHTpcAO5nJ0u-8VesXqhpa9ZsAwSn6YFmBv05XzU22GURjZeCBVYxc-0KP65hnxtk03nHesfPWLuxlRNdfJZM8VzMdXXLmBCfRzkfhVfH22ATdpNhNxAY0PQvCVk4BfkYPZa-wNzwtcf5y_HESoEwK5XsIgZCLFRJXRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LurMyqRvDUCvbYB8tdO_3_YqMD-4oAlzc2zrKH6tqPIJAMgu1R3UKlDPiHGRJ3muvm3n75P9_3e9aJVSPs6MCywUTdK1dO8h4EvjdyhHiEdu425pyCD4dRAWotqRtkgydcTAMp7IyzJwBp6alFBIPm06O0al3EdlBJo-vV2EZr9HAtX_MFd4EVqp2BCX1wFsVDSVp5bCqBD62LpCQ9vg8b4el8My-wyqO0KRE7GtcakkYUoEF4H5vwmNxQ_IH7KLF3LfHbhHojK3WMt_4M6F1OvP_Kr8leXT07tKaosuoEtYO6Dx-vIDlqy5nMgMM58RJcqQwEjEAlalG-DMtI19aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBxKbeZQU9ddRAt4khhp8jIIAERyBjxCLA6fUBS3n4-sjyii10cPnT-SadsHJvNdzKyo9tc2NLhhBigAWPWZE7MtGrQB0a1jEZ-mxqMyHdyz-gClBWgbK7mfIxtBrpL5v5MzGfcoDt7Tuljh4BIiDhhl2Gak80jpfBqihxeGrYmxx1DcPAYYrhNjo9J0kUe6GDOrki285mdkQDhZTlddoUJyxnwB-Fbtwg_l-j2NQpMKJzAqrysFvPLR9E-uK2VqxgKe0u6eAlFd0xVxms-AiML6rmlmaQBWfQibSpHLyOXb4oZ5kea2EPj2NA0cryJLSBZCxBJ5LBN7sCJml1BOUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=XywrxNi_5Erncp9d1kMgP_u6BW9bco42eZ0sONxw9aQYV17gt4OKolD7K-E4tIMNffsigmocRHqYX5HOY88x6K1igmxanmBpam_YebjMLOEHv-ssuGNx3g6lTw6hK3Wi0tQwvtvoDEzDXy3cJJADtwUL85sEJx14N09bpeRF_j_sn-33hQM0bjCvVOrz2JIgjk5PZpVbLZ8ffUaALWrqsu2qMQddTkArAzMJqq8BHu8DH895aOtxNVYAKJ35VZQPvElqmBC4Vc9NOJw23INo0L1RS_1NGGrOJ4bisEws0HZ4QyRhBAmnoEYIsFH1D668Uc6sUcOplFu5Z9xRChC0-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=XywrxNi_5Erncp9d1kMgP_u6BW9bco42eZ0sONxw9aQYV17gt4OKolD7K-E4tIMNffsigmocRHqYX5HOY88x6K1igmxanmBpam_YebjMLOEHv-ssuGNx3g6lTw6hK3Wi0tQwvtvoDEzDXy3cJJADtwUL85sEJx14N09bpeRF_j_sn-33hQM0bjCvVOrz2JIgjk5PZpVbLZ8ffUaALWrqsu2qMQddTkArAzMJqq8BHu8DH895aOtxNVYAKJ35VZQPvElqmBC4Vc9NOJw23INo0L1RS_1NGGrOJ4bisEws0HZ4QyRhBAmnoEYIsFH1D668Uc6sUcOplFu5Z9xRChC0-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=vPXZGI5n6rf1TQ3fDIZSAsi0aZAOrItND-MHFIg-MoFSPzoSsH1_wAX2Fkgp8W6A4LJjY3Sx_shKa1hKAd1ohHE-Ab4T8FX3QsARYAWf28jecHVm3MhH-gnP7PxMs7z4QZ09xHp4vkf4oZCJDAMKcE6BDGf-HdYK8e76xqWGcqjp-yNsIBpipZuMc8pMHyx-l6Pj4wUaFcsxS6GZIelb6mNqOakCBAzn8WpZQZr_bnKvIJS8S0lxaUCY1mVIpXo-pmBJINDwu4CIztyCjdHpddBNreVN78vhi8BfI5B8mh_KJEzkuX8t-G_3K8ytjkzkzgUnwWdtqX182ac4lGBaIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=vPXZGI5n6rf1TQ3fDIZSAsi0aZAOrItND-MHFIg-MoFSPzoSsH1_wAX2Fkgp8W6A4LJjY3Sx_shKa1hKAd1ohHE-Ab4T8FX3QsARYAWf28jecHVm3MhH-gnP7PxMs7z4QZ09xHp4vkf4oZCJDAMKcE6BDGf-HdYK8e76xqWGcqjp-yNsIBpipZuMc8pMHyx-l6Pj4wUaFcsxS6GZIelb6mNqOakCBAzn8WpZQZr_bnKvIJS8S0lxaUCY1mVIpXo-pmBJINDwu4CIztyCjdHpddBNreVN78vhi8BfI5B8mh_KJEzkuX8t-G_3K8ytjkzkzgUnwWdtqX182ac4lGBaIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV5Un0Va8JjsAn030nS4X_htO3epRSZEy1nxEbAhnZPF178MrmOFPFyDasr5cdMzWI6NZ2Mn9ILnqS9EFguw1RXJ05vp-b6pUdm8gtzsCGJuXx0kDpukIRNZSSLnpNiq_ZBvkyfZWtI4sh5qHXw-TZlIDM8EFawQNPWvlCxAcMbae48pXaAG0DPjhHji5XSg-tIUYMUfD7JqocSAiJmqQH_oBtyffI9jkVOEibtYhAz3hLPPsdrnxCKz7rTJ71gteCmGlwBS4Ls-8kg9UAesPMhG9_l6YtxN6bTf6G6TOJI001uwEnJhUK9yO-DyEodpo2ljWTlHOpF1Fo7TI6sFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=SxrFUQc94gzrTrz3IHrfGaMGcs7MY_ghjtZC_NZ9iAsOgy98WtA8iqbMDqZOHC9YYkCmYpeeDrNJ-E_CTWsxhj2oZk2kaK2HK4hOnmWZUJvAZ2T6cO-vc-5pZsQIdx0c0Ob_D69s8ggdIZ7j2ygnUR_qYZda9iSws7NqPqL3Y2tBwzpFUqM5_bPcGzRIrTmye5whSmmv5dENipPAkDZrWTIzS-KTsdfTHJ-do8-7lV04hNQ6DL0qp1BzJMO8cUz55xtWDTDkbhsdg9E01-On0Z7xOboioHZuuenz7XtrsL3pQDOayyK77VSFEzK1EEVmbcDOvy7aHyQBc3UZQ5V141p-M-ttbgYLOZswXzQX0mv1nVwOjgHhcB9O55yIcTmzUjOggBLcor1AGYMO4zq5rgxfJidT7Fv_3-n_lycckFbJuJrgjltRfKapcS8LCIYDJp12ZiwEfRTibsct1nuknRDxWxgExPjOIbxSCdKN2HeLtxKUQvL_Sl57m-95-SPGoPfUM1s46t0A8HF8WOAL6_85Lt4QDO9mevNcLla-vBwYgHLtYJrKKeZJtVV3Ns9UHW3tmbB800JExaTWRSxdMTNdx6mINKESdJgcKON545ognv-xw7ENLbss1nA8BfFGQmmnvoEaB8dH5FBUx9zD6NYFo153LEjt6JBFIuF--yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=SxrFUQc94gzrTrz3IHrfGaMGcs7MY_ghjtZC_NZ9iAsOgy98WtA8iqbMDqZOHC9YYkCmYpeeDrNJ-E_CTWsxhj2oZk2kaK2HK4hOnmWZUJvAZ2T6cO-vc-5pZsQIdx0c0Ob_D69s8ggdIZ7j2ygnUR_qYZda9iSws7NqPqL3Y2tBwzpFUqM5_bPcGzRIrTmye5whSmmv5dENipPAkDZrWTIzS-KTsdfTHJ-do8-7lV04hNQ6DL0qp1BzJMO8cUz55xtWDTDkbhsdg9E01-On0Z7xOboioHZuuenz7XtrsL3pQDOayyK77VSFEzK1EEVmbcDOvy7aHyQBc3UZQ5V141p-M-ttbgYLOZswXzQX0mv1nVwOjgHhcB9O55yIcTmzUjOggBLcor1AGYMO4zq5rgxfJidT7Fv_3-n_lycckFbJuJrgjltRfKapcS8LCIYDJp12ZiwEfRTibsct1nuknRDxWxgExPjOIbxSCdKN2HeLtxKUQvL_Sl57m-95-SPGoPfUM1s46t0A8HF8WOAL6_85Lt4QDO9mevNcLla-vBwYgHLtYJrKKeZJtVV3Ns9UHW3tmbB800JExaTWRSxdMTNdx6mINKESdJgcKON545ognv-xw7ENLbss1nA8BfFGQmmnvoEaB8dH5FBUx9zD6NYFo153LEjt6JBFIuF--yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=dSrUr6dumsQfUsFEivYfgJyQ7rwil1IE6HE1P9IyiBBiswbjBHvcM964p-kKGfE_txprmM1Y0ky1JuB3wXeiL99VqOffHK-M6LTXVydxvSpguRmVrzwopifuB2LfyGjsDVM5s0HhcTeUoKwZKBeLAHRvuMpgdh7gsmY_FaJ1u-ElqSn5gbgqSyIxTM7gwgVrl5kqGFKOEzLmjBUtaxdeD5p_zD-rP21pu01A6tTk2Ln_pNcPKXabFdalsydXcC6IspmREuTAbTXrcBYBoFuV63C8DTPaGQ99HpLTo2uaJuXTor28wV4oncbkqCfnWMyWBcebp49qS5-iNDsKByltow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=dSrUr6dumsQfUsFEivYfgJyQ7rwil1IE6HE1P9IyiBBiswbjBHvcM964p-kKGfE_txprmM1Y0ky1JuB3wXeiL99VqOffHK-M6LTXVydxvSpguRmVrzwopifuB2LfyGjsDVM5s0HhcTeUoKwZKBeLAHRvuMpgdh7gsmY_FaJ1u-ElqSn5gbgqSyIxTM7gwgVrl5kqGFKOEzLmjBUtaxdeD5p_zD-rP21pu01A6tTk2Ln_pNcPKXabFdalsydXcC6IspmREuTAbTXrcBYBoFuV63C8DTPaGQ99HpLTo2uaJuXTor28wV4oncbkqCfnWMyWBcebp49qS5-iNDsKByltow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpP2bCP_MfAbcY0GOPB_wle3hBE4WRJGj9I0vhgRZn9rJUdkogwKXX44zO4T6y_bdInUvx2o-FY_FxG5WcvvUyR6cvJcmAEVF6X5VxMjARS_pmkhR1WxURoADvjZ4mjjXm4O-exlADbIItWBbqKvj9LKVZj5NK-uaG9EWQYjRMANJf1IHi4keeSXxYnebx9eCdJTE4NsIaS3FMQ39pRrAosueA2SdoIoyWACCzJKyoMWxE9Mx3dDjb-pJvxJhIDmCBvQAKAPGo7gQOBYALmt0z3zX_wKiRfzrY5zyR2zH0hO7JsO9P1qGUGIectSiPF51tMZiKdbW0EsTQ91aQlvgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=GlCHMrb5fQZz5hCPiD6Cc9VnE57cXMgPkx6xeYVjvxrpcSxjnjMcIEEjAMxZLIdNyDGCi3DfBMRM5SXxKKfYlsSCEm4L_q7FAdMtGes0FwANjXaWi5qCwGe_7bOAZFofH_sbw3nfhaSlly8XfYzWxLPk9ivxPAMCjmq1WgTmCqpy9onQ2PuP-Jpo6E3LusG4y3xIVwYkr5OIqEIylcdtGbnh8LpIAYJNFXWUq8xkSQXS7d8_ITiGZZti66KkNr11GQ4oCaOP9PSeDQ6qLw61an9P6kbHyRffsyrrKT0224HwZ4PKkcJU9CfdST7Fefy2kk4Qu8by03mhMfL0CpsSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=GlCHMrb5fQZz5hCPiD6Cc9VnE57cXMgPkx6xeYVjvxrpcSxjnjMcIEEjAMxZLIdNyDGCi3DfBMRM5SXxKKfYlsSCEm4L_q7FAdMtGes0FwANjXaWi5qCwGe_7bOAZFofH_sbw3nfhaSlly8XfYzWxLPk9ivxPAMCjmq1WgTmCqpy9onQ2PuP-Jpo6E3LusG4y3xIVwYkr5OIqEIylcdtGbnh8LpIAYJNFXWUq8xkSQXS7d8_ITiGZZti66KkNr11GQ4oCaOP9PSeDQ6qLw61an9P6kbHyRffsyrrKT0224HwZ4PKkcJU9CfdST7Fefy2kk4Qu8by03mhMfL0CpsSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmUhMhbjoc4o6BDOSdfOhrKm9ZD7q_BCmj7entrSfy14WRutAksG2Dy6ATX6R0Gcc3Kf-imxkiCfFgcQ2FDB0vXgf57Bp2KbHIbCpvGOAZdiqGV0NSuT_WmBsrTmc0NFQPFMl2bQkLO-RSM0rF-TorM-D2URDi3AUb5A6w-AJDnAHvyPnNEtkOdg0BQ8liRqMEO6jtgD3j2xzPTK1SK5AiQZfVwM8qgK0v83i-GQUBL4W8-6-9Zo5Dbgd-fZbCh5eA3OUTUe73RXpboIFlnGZLo5qMdhHr5wSQTf48_oBf-4zQpUby6Vdm2vKJn8oKtgTRyjausl5dl1_nCHvBQlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsiVjuZqrRBRz0NX5Wy2a4UONBviFuKV72s3vwH6L-0N_MVXSAoSuwhoIxfZtHjwGwyZ9NU7EP_1-5NLadMonjmI7djG4ey0fJXccvaav3L_AHDTw4OiyPc-0VCXxucC6OmiCvs2Kxon2Ixq4vAXLm5K_BWT5kBNHD5BBSqsPN5kZhdCp3otgPCHWZJEAyYiX9B01nusPaGIuycHulJxLlrTeaEIHy8wUevdmMNyyE1VGOivCTCEqXx6s8Q0yN__NEbueT6VlKqwNJrvUNGbdnGzIl2Ag5l1JceccoOqLzIP7aWM665le39IyP10TicyzTeytacTm062DfXmLvbdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=axS7Zb2BPFQzblhPlnxjbOLgxVxgqHG2RLtOX64w-Mc6HDDXEICSE0arUjn_3L8fgQBjaDNvJh_qqGJbu3hRxd6D4DE9e5Y_oPgWAsBTSwhoTPPPm0keYL-VLrwkZ0gkl23r1dJZLwab6fK6XonJH6iwOVSWcPXel3_9qP5XL9AbO9qAd1cwoI-b4yvXPLLG1GDQHgu8R8LUGmzykeCstVDdVobU1WJIC2Qn9WBZJf3oZwAe69Y0XlBsheVVWC2ujO04VVHUygwL6jbQKeEZSt4X-GXoHpCHy1avNzMFE0oYX5uay8F2nOiAvzsWu4XjT8m_bxKwx3dG3Qm6XDI3fbFyoLUDj0QgG7nZzSvRlTjW9sPkmLOuqabKPXSiZEujtldpI6KoFKf0CCQcgj3dTlQxBMGeOPjN8_wZtuvLipKXLJfP38HIRULZkz-9i39c793TwpZBjMx5Cx8vTGbx598-7FPM09iI0CjuqLz4cXibldmzfpKz7FPHjuubIofPYYQHpXEZh2PFQ4ObaC8Em-KFbGbUP8HsV7mP1J8F1lADMeCO7wxibEJThJ865VXNYlI6AHj6aQoukJJJKdnjo_HbMz_6rVCfkkMaEl58vRTZyHKQJVL10bxl0htaYD3h9Lqb2FFYjOf72-Ui9eBHHN3arRnyZMCSR6AU7fljWCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=axS7Zb2BPFQzblhPlnxjbOLgxVxgqHG2RLtOX64w-Mc6HDDXEICSE0arUjn_3L8fgQBjaDNvJh_qqGJbu3hRxd6D4DE9e5Y_oPgWAsBTSwhoTPPPm0keYL-VLrwkZ0gkl23r1dJZLwab6fK6XonJH6iwOVSWcPXel3_9qP5XL9AbO9qAd1cwoI-b4yvXPLLG1GDQHgu8R8LUGmzykeCstVDdVobU1WJIC2Qn9WBZJf3oZwAe69Y0XlBsheVVWC2ujO04VVHUygwL6jbQKeEZSt4X-GXoHpCHy1avNzMFE0oYX5uay8F2nOiAvzsWu4XjT8m_bxKwx3dG3Qm6XDI3fbFyoLUDj0QgG7nZzSvRlTjW9sPkmLOuqabKPXSiZEujtldpI6KoFKf0CCQcgj3dTlQxBMGeOPjN8_wZtuvLipKXLJfP38HIRULZkz-9i39c793TwpZBjMx5Cx8vTGbx598-7FPM09iI0CjuqLz4cXibldmzfpKz7FPHjuubIofPYYQHpXEZh2PFQ4ObaC8Em-KFbGbUP8HsV7mP1J8F1lADMeCO7wxibEJThJ865VXNYlI6AHj6aQoukJJJKdnjo_HbMz_6rVCfkkMaEl58vRTZyHKQJVL10bxl0htaYD3h9Lqb2FFYjOf72-Ui9eBHHN3arRnyZMCSR6AU7fljWCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCKIAgJJ0uEw_QXkVDFJ38OOvaSGTaF29_2vjEhFZn3RCI4oUPsi2M_L6fgHDr2zfyru8N8aBM3-5uVp4WaydhlS_m80hLCKyO9STGErd-MKTGe-SEMtSCJFuBne28eNiVr3zhPOECH5gtpbU3NNDTGkG7haljlnw6z5QpjFMDJWgxN5IK57BOhvV75K_dMPRw6o30IJ-C5j91HWC9wR_0wINeeQOBKdey1HUqJP4l15EHYD5zVJ8m5IHC5V23GiKTK9iWmXsZpVzwavxg6W-y1v7RySpE4GX8DPUETUjUhsg2u1c2B4TQN6F2c4dKTu1mnZPR3lb2_UuCCxvvEmgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzp-aDR6Je5N0JEnNxC1WPbHScfM9mblQyX0ZTVJJ6eEMza8YosBEUg-Xez4mnoLp5JXat4Jz3vOVdr0iupqHXIUX6_iqymeCRbuYLR9X_PkLvSWzFBfmH8bMabRWhNuYQfo4ovRYn6wWyvWliciYGqtTcbpl2byzKciHII5Qx4OFDz-BjD7DURx-xvQBFCPthz--ZeIX57nbLaqALuT4k4jfpRUEwSiwLFUbSKcKRZRvow0k8XDGt9j3xhrc5rM8HoepLUL3AiWA0s51EQ5b0H_P-128VwvTkTcIiVe64FT-6Z2Zor65ByH8rBK1gJ5lk2VnzVaPl6IwhJfC4_NDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=hAJ2PYmtgWbe0ef2Tm39GAxcY8hLg0S-UxLUNS38ZpkfwMvnd5jGlErzO1ZV2kvDgVDWrccyU7GiELWv41hO4LE0isJl3u9EIuf6DpYfUesgJ0_MDD-ul4P8Ip2c1FSUETiBDSDdWgUvJnXFN4fM4gYbg7hMMFL-UEPh39eIWmNqPcfMBus2o-aNDOwXSO9x1BMRdXQKDGF5QHP08O7FyyJFIk9cfcWsatfcK_BoMzQkktHVG0IOXkwKeXpYacT349uOc-Gog0OnmmnAp8kU5xSLgrzrolmbwKiKSWc7k7M0tHMiW7kcVBn0uSKURxa0u3GQG_B2pFSpFl3Y2_r4Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=hAJ2PYmtgWbe0ef2Tm39GAxcY8hLg0S-UxLUNS38ZpkfwMvnd5jGlErzO1ZV2kvDgVDWrccyU7GiELWv41hO4LE0isJl3u9EIuf6DpYfUesgJ0_MDD-ul4P8Ip2c1FSUETiBDSDdWgUvJnXFN4fM4gYbg7hMMFL-UEPh39eIWmNqPcfMBus2o-aNDOwXSO9x1BMRdXQKDGF5QHP08O7FyyJFIk9cfcWsatfcK_BoMzQkktHVG0IOXkwKeXpYacT349uOc-Gog0OnmmnAp8kU5xSLgrzrolmbwKiKSWc7k7M0tHMiW7kcVBn0uSKURxa0u3GQG_B2pFSpFl3Y2_r4Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=lqDcOshet85ng8WLuIOsia1PVitswimbk7JJ13WmKk3cR7o_vHSuzeHK_YP-B0VbCyyhV1xVIZmKeOQuca6wVWrWaUDEOFyOInqV_AE90O7_9hMW0B4FCIYf7wXq808Nvmc6sk2Amlgk3IHgMAuWhSn53XYLY0tjwQgH-cXmq32FHsjLrhXk-EOuNzEscZSNE7Pf8XOI0DajHeO1NEK0ZQbpxKr70KkFtMw-rMF2J9Jjjx4OaZGrDzn5CO_GJ8VW4R3_DaZyfIdwxWnqIHyL6MNFnjJvAu80ee6V4L0xSUeHafB1PzgQxK6-5iD2Y7boEja842ufj63-x5cxBkM_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=lqDcOshet85ng8WLuIOsia1PVitswimbk7JJ13WmKk3cR7o_vHSuzeHK_YP-B0VbCyyhV1xVIZmKeOQuca6wVWrWaUDEOFyOInqV_AE90O7_9hMW0B4FCIYf7wXq808Nvmc6sk2Amlgk3IHgMAuWhSn53XYLY0tjwQgH-cXmq32FHsjLrhXk-EOuNzEscZSNE7Pf8XOI0DajHeO1NEK0ZQbpxKr70KkFtMw-rMF2J9Jjjx4OaZGrDzn5CO_GJ8VW4R3_DaZyfIdwxWnqIHyL6MNFnjJvAu80ee6V4L0xSUeHafB1PzgQxK6-5iD2Y7boEja842ufj63-x5cxBkM_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=kx07GhHWAh6Kcjw4s2oxv9aaQP9ca8fN54eFtJIlNyRLsNh5pBuEV0HKF0wq9hk8nc47yKL05QjZHtwKt4WkqFUiXLmGcD1Ec84qS_8PteIJu3j0ywzheB4JSTLKD6kjFHaT02WFgDFjRu1Es6fTC4KQyZ4t_K5cahR6Enp71762e_0NeJ_Bbvj_py-7da6qW3gwgFHBMAB6netD9l2bt5uAcBJ90n1fJTQk7GVEZnNqejeannKW8u1XDBl5SP4hCEzncn2gjFOV6xITCxIgEPjq9RGpjvz3VXWmkY2u1ZVuEw5ku_maX_Ea3EREBFWaQHyR7BsY6cJLdmYrq7CQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=kx07GhHWAh6Kcjw4s2oxv9aaQP9ca8fN54eFtJIlNyRLsNh5pBuEV0HKF0wq9hk8nc47yKL05QjZHtwKt4WkqFUiXLmGcD1Ec84qS_8PteIJu3j0ywzheB4JSTLKD6kjFHaT02WFgDFjRu1Es6fTC4KQyZ4t_K5cahR6Enp71762e_0NeJ_Bbvj_py-7da6qW3gwgFHBMAB6netD9l2bt5uAcBJ90n1fJTQk7GVEZnNqejeannKW8u1XDBl5SP4hCEzncn2gjFOV6xITCxIgEPjq9RGpjvz3VXWmkY2u1ZVuEw5ku_maX_Ea3EREBFWaQHyR7BsY6cJLdmYrq7CQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMYuv9MoCxyVJouHkjN_pRjqIfpHun1Inf18q4Ky4HjqIrXSEXQgNKYitZDupbJexeF1PZcjsyrRgNRtGW3ebkIgjHB3dP9PXze5wQwd5tmr_LPoX7vYWvkMjBvvSeh2AuR9OhIUh4-uMsJojiQRe28oNr8tmb-yMhKrSs9_t1DQo7FL8PKhTIOAZ7hjuP_fy5ZYTFhEbk9tMu1RsyHQYnCQx4Zk0Kg8Jw-7dWhVkyJIfhQ8eoKe6hGvidMIR6-gOqDegt5vIevS3Gw94_F4z4eORb8nlNfGEU-bxwQw_VRYSjwoz96yOEmAE6NeUvbN5k4DbPe0Lq2yzbak1Tfx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8FiVazrXg1p2unu6YXQbZLnGOEhOMMmpY_1WQqgPRfthch5QXic45PrdvZNT2j_grRs9LMdS4TtegCNotj5fRfn3AQPSqZKLu--S20TMuzfuUqttbSkneOwEGbo5UZWAofwidIJHLhel8iOjzs2Ehw1O4ZjC9wpdsiVFzL4qTWL_kklMJ6_pMBVq5sePbLfqewK18q74dOwSke8qzUXsiqSh3Q5pWStMPvG1jMhM0FgWr_x_SvfpmDootGr5sXmgdkExGRaChm455nF1dtc-ewYuJKCT4DWHXixE65oiLdXx560uzyDvasdX23-vtQnEfrXa32Fo8oZN4S7GWJd_cmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8FiVazrXg1p2unu6YXQbZLnGOEhOMMmpY_1WQqgPRfthch5QXic45PrdvZNT2j_grRs9LMdS4TtegCNotj5fRfn3AQPSqZKLu--S20TMuzfuUqttbSkneOwEGbo5UZWAofwidIJHLhel8iOjzs2Ehw1O4ZjC9wpdsiVFzL4qTWL_kklMJ6_pMBVq5sePbLfqewK18q74dOwSke8qzUXsiqSh3Q5pWStMPvG1jMhM0FgWr_x_SvfpmDootGr5sXmgdkExGRaChm455nF1dtc-ewYuJKCT4DWHXixE65oiLdXx560uzyDvasdX23-vtQnEfrXa32Fo8oZN4S7GWJd_cmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=p2j3GQwIccH9QzRkDJ26GUr482q3o2Arwo6dlG0ux87Xn4dVUtBQp7-UXmgOYN2nmaA2gt63XzAHz-Gn_zk5afajIWDRHEDidGQo3eKiGs3lFqyXdhTHecEu--kgKJStocobC97oFsOPv6gzHLE6CeyIpTGnzhsuqrNs2ARQG_fGWtpIJC03RpdRQqmuFBkY0XUDlRMJVmB6sakgLmw9RLuEXAbl08dpEfCFz0jX6Jqj2zAY4c_JZDc6e7xl_6cIpyaCtAvgTR7rqzjG9B1DH6JdPIR_IDDmjq5key3IhdCk3cHNq37qRgmSpbMbHwMD-c-rU_k0O6G9_0_qLqpuNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=p2j3GQwIccH9QzRkDJ26GUr482q3o2Arwo6dlG0ux87Xn4dVUtBQp7-UXmgOYN2nmaA2gt63XzAHz-Gn_zk5afajIWDRHEDidGQo3eKiGs3lFqyXdhTHecEu--kgKJStocobC97oFsOPv6gzHLE6CeyIpTGnzhsuqrNs2ARQG_fGWtpIJC03RpdRQqmuFBkY0XUDlRMJVmB6sakgLmw9RLuEXAbl08dpEfCFz0jX6Jqj2zAY4c_JZDc6e7xl_6cIpyaCtAvgTR7rqzjG9B1DH6JdPIR_IDDmjq5key3IhdCk3cHNq37qRgmSpbMbHwMD-c-rU_k0O6G9_0_qLqpuNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAW6_4u77qoydBsyxPTr12LG5Eqy6qOceV4Nu4m-u-BV5hWdR-vMLlpJA9s-kmM1EVc7pSik-kC6252Ade2whtA1gNZgAubIIxqUI5oikLF7Rp-ERPihSfNHtCEdvalXXGJhGQ1Le-I1BkXY8jbwCmUAwwQqP1VnXVUVibZ8KMqQrE6U-HrzTBCiE9aEpJiAlT9mmZBL3QhZR_yDnC0yz7Q6dg0TUJeO0AviTQsK-x-5LV08pPDLFX9S8arEeUJrK0iVjoRAlZNMmCZ8zH66_54KGoiLXA4Xspl0-y-_PBuOYAcKc_-oFlktZuwIOzgjLj7S_dm-mrolCpPrReJkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=DVISWMDIRg9WY1E18b6n2gqfW7u2cu5XwDg00b3lsEuZfpRyuE-tTTe8AqhhF-WB0JaHFwU2QE71MOFSeDxOYEuAtw5EKHScZCG4INdQMjiXiPKKAzLeHbURd_VwA35iHb12m3TUZ5jtLoxCnSWJD1NWkEK-g4ngr6DcCWlsZQlUQ-nbikgKoWO2ikw8yKxhA70XUZy3Cfb08-imPFBmQRXItHO8NXukOU4SxwSVnD7yRjFfRxIaFKcZB7T1VzsIcA3SdwxUPhK5jow-8Br8FWczM4NkHol9dUifgdsS2jNpxenPdLMCtVLtG1zFZyYYosWnVvnmKOMdQRPfXiuFA38ktWDZOr_ic2uZ57DoZsue2RVRGxV_-piBV6bcWxg4-U8utjRzlOpKmCrYJti91-nvzyJvWzd49geQ6oCrWWt47CdNhrkNo-0jn7FaFQ79MccfW3L-LCQh_FOeW2OYYNlLtAlgVglciquiokvSs2BZjjpWGoT14xSzExYsex9BPi-qZ6FfxJ4IiS6lGFzMN_3OziFme_i2Ht2xtwywvN7QpLYwgetbqK23RNXwhK5dvhNFaV1FGmQOS-djyjXhcPtVSUMJrO7vd-kgI-c7JxkJ6CmUISRQaxRAE6Tl1LoWQ05nckA-FLBpZF-EngzOKoYOtk6cHP0pQDY69JfHJwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=DVISWMDIRg9WY1E18b6n2gqfW7u2cu5XwDg00b3lsEuZfpRyuE-tTTe8AqhhF-WB0JaHFwU2QE71MOFSeDxOYEuAtw5EKHScZCG4INdQMjiXiPKKAzLeHbURd_VwA35iHb12m3TUZ5jtLoxCnSWJD1NWkEK-g4ngr6DcCWlsZQlUQ-nbikgKoWO2ikw8yKxhA70XUZy3Cfb08-imPFBmQRXItHO8NXukOU4SxwSVnD7yRjFfRxIaFKcZB7T1VzsIcA3SdwxUPhK5jow-8Br8FWczM4NkHol9dUifgdsS2jNpxenPdLMCtVLtG1zFZyYYosWnVvnmKOMdQRPfXiuFA38ktWDZOr_ic2uZ57DoZsue2RVRGxV_-piBV6bcWxg4-U8utjRzlOpKmCrYJti91-nvzyJvWzd49geQ6oCrWWt47CdNhrkNo-0jn7FaFQ79MccfW3L-LCQh_FOeW2OYYNlLtAlgVglciquiokvSs2BZjjpWGoT14xSzExYsex9BPi-qZ6FfxJ4IiS6lGFzMN_3OziFme_i2Ht2xtwywvN7QpLYwgetbqK23RNXwhK5dvhNFaV1FGmQOS-djyjXhcPtVSUMJrO7vd-kgI-c7JxkJ6CmUISRQaxRAE6Tl1LoWQ05nckA-FLBpZF-EngzOKoYOtk6cHP0pQDY69JfHJwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urPmxIgl_loy5skFBKa8_WCHQw8GMF2ZeObep4amYnKdMVnXsjxSWix7SYCH5FW8O5Kgayh8BooUKqXKgZxq1qyDJaRaRCJzBKMmIIXyxdsT-FZzw2uE0vJw_dXIsvD490plKDmYJ-hAc2ySeiSe-0wJUyAlowgZFNP4t6ToDLlvy4nxd2vGJJ0uJtORYA-lGgUzji2SfJQsBicE6iTT8YDrvNvQOEA_d1e4TO4XIkj1VUwgVP5QzDjnaX0XBIPA0P-_tQlVil6any-F7nSSqWOomPZaWatnJ_Bm2j-l5bNaI9GxAT2zjyiS7vLCu1XxJZXkRNeC_OrZvhuSVETn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=V9spcQU2MuXCtK18ElC4PSXjgaBgot9IZYHZQSRQP2x5A0FiKqpwJUtUulH5fi5T4lvSrzA9PmanSKVPALLlSIODciCZvMqAXJMLgB-9B2N5PF4DLgMNlrWIAYgOE8Yl0ZUj130OY0jFo8ADiFeO5m2ZOhoL_BRbAs_nFqyUsng0_yCezd_SSxUoIV7Qs8y-uAiD1N2gP_JyPC4izXHEuJ9-ucNnKya7Znc55KjSy6e3ei6SqTGl6AGONiLRpxFd57nGcoEqPMr2ur0xhU2nq5Tj6LMfdyWxyv2grZGZSDSc5wywuFx4ai08M50DO35JL_w1vozRDLSbYK9QUAF5nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=V9spcQU2MuXCtK18ElC4PSXjgaBgot9IZYHZQSRQP2x5A0FiKqpwJUtUulH5fi5T4lvSrzA9PmanSKVPALLlSIODciCZvMqAXJMLgB-9B2N5PF4DLgMNlrWIAYgOE8Yl0ZUj130OY0jFo8ADiFeO5m2ZOhoL_BRbAs_nFqyUsng0_yCezd_SSxUoIV7Qs8y-uAiD1N2gP_JyPC4izXHEuJ9-ucNnKya7Znc55KjSy6e3ei6SqTGl6AGONiLRpxFd57nGcoEqPMr2ur0xhU2nq5Tj6LMfdyWxyv2grZGZSDSc5wywuFx4ai08M50DO35JL_w1vozRDLSbYK9QUAF5nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZaYe6VgxDlKbaoX1fnkOaPEF_FgB_I7X08_dX2KzLj65hznssiBOuu0oVxbdCCRM4IOQ8_ADD_65kZ5nwpOwBi9ONVtOuk8n72yTlrm3jLQ3_zuyIzbI__hQREapTjGMYlLYAEFiRobRGbWfYMBk6Jt9muMLfK30AnJKzHn9hv5XMh3oMQD88__LL3iXTGNW2-W775GAZK0mx0kh8KqB6fQLPRNf4LylR1T8LjVM4TpFkl5dJr3fqY1rO3snkPmUJYbcSw3LNrQRpP6WzaZRoMpRsUBVyq2feNqLrIt3t3B4V5zHPUVOWXxogKGdP5ym95TyuEqMWVOA0tQb-ZCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml69aru5f_1HK8ZIL7qps00eDIVrwJJAcqmbQaxzEsegtU80BAGnnFQkgJq7Sy-hDAm6VTi_9apvDYDoeIkaP293oSxfh7ST1Qnr7MvtSxaGN8OxDOn7pMbCvB_cZvIlTDpyJE3boz8vIjTuVYoFSu64qEP7abtFNWr_AZ5b0Aav2xeci1OziVr9TYwDU-Uc_0XwKpxzQ4hGg1687OAu2LqFoltoN6ESMt0VOZSkLneFJ14ZYTY7EC0K703m0LedqfwODsEtx2ed0c1CIxXCOwCNihhhK_-aeLS-r71k1ci3gkBP0bhUL3d7IV20vF0zRQ9fDvRJXiUR0gs7hFLfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLxv0oR4cdsYtLZSe2dyJti_DQzDKz394BKGSbQhfTkjaPa8Acu0JdYJrqqv4x0uJguceHzi-PFpULDYhbg0zXtdmvtTNNSVj13gNYM9UsSnlADspyMWl6w6zc2spKX61ijejXYvxpZc29gkJViId4OFGrAcIo50S72Dd1MEojWMWDjUJ5HLXgsfHKkyvrgVu7_5OgtU0xGw3pGUoSg0tmOPMgJUqUE7D1UzQCLOu6zqOOem05t6599qAyDyAFoiybVVDY3DTvlBg05hpkzxdPsuiCQ8ecvUgCVFXggLGL1v4Tvc9boEg-am9bMI9Xp6WLPIrwdvNqnkZRQuhcIMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=o_6faQNb5V9g0NbRcM1okKHZnZHKUapw9O4AdHraMmY_xSWwZCLe1Vqt4Y7qA-EA2Krd0O6bY9AzDumACDQK2ZPEkGl4Krv3xaLR4FlfTQzW6ZHt7ZCFiYGahrViKYqaYIKiYu_JFYzhNCQDJg4Tkuod-hWLo_sXqJv5hWGnSa6jThYghH_Dxyb2nt0k9WzmzKmmPze68_w1LidbaGZqAJ0ll77b3416ZYM-mR79Y2Q1CepRpfNU4b85aNpMEV9jptm5lFwggBtjALs0bF7yyB7cVmIAWXEfzD5hkKY-zC2bzDE7JfLdF2_A6hSurkMqhKshai7vJxDiyH4r_Q0q1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=o_6faQNb5V9g0NbRcM1okKHZnZHKUapw9O4AdHraMmY_xSWwZCLe1Vqt4Y7qA-EA2Krd0O6bY9AzDumACDQK2ZPEkGl4Krv3xaLR4FlfTQzW6ZHt7ZCFiYGahrViKYqaYIKiYu_JFYzhNCQDJg4Tkuod-hWLo_sXqJv5hWGnSa6jThYghH_Dxyb2nt0k9WzmzKmmPze68_w1LidbaGZqAJ0ll77b3416ZYM-mR79Y2Q1CepRpfNU4b85aNpMEV9jptm5lFwggBtjALs0bF7yyB7cVmIAWXEfzD5hkKY-zC2bzDE7JfLdF2_A6hSurkMqhKshai7vJxDiyH4r_Q0q1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMgBM0NhT34NteZAutqb96o-jVe01Oc0wZzGqGx8SnrmPgV8tGAkzc-ofo4Qg9puFyUSRMjr2kieQNEMJKXDJ_Dzs-LuquGjwqOrQgKE-HM_nqfap0lrN6gtpcKzSDJi-eLPJGXmSiK3K7HtFD_mmm6NB9nOP8vSWICtufxn-_I6wN0TDGfRtPPcKslwFKmLwRPnC6O7tTZB6jzkyraOBbcBtXgCcw_cUSExGyXBJ3c6SSKcsH0z0TyEagX9QGSc8Af6MzKCqL3ATilxxFpXTrl7XRMlz24WL-OulQrGZw5qKC2bKIYkR-48j4gOwme0GvZOgtnrhDvnJBbZptL_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6SAimG2oMOZ0-BqkLjSsGQYR9utSxFVLiBylac_HBWAstYhKXofqgXCb4uW_vzya4dOCAfES9Fb_20evj5z0P261ZidQexUH_vabKSVlyoMNnqk3DkkR3JMW_BfbvId5JLMGpjEOjybfjRnlMT_9Dp9Xf_KzMkooosbsHgv_wynAh5aZuFHhbAnsLSaO761lhwzosswiZ4QHtWORV-YE43xfwX6FBQ33jTdXkbv7PE0XzxQmuiqA8dBkWmq74p_lV7cQrMHSCSTqUB5sDOFH0C1MouKLcO5PXxopvunlAHceFhH07TdKWonYGOiJR8qR1tPzuNEw-SsVCd2s-x6VCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6SAimG2oMOZ0-BqkLjSsGQYR9utSxFVLiBylac_HBWAstYhKXofqgXCb4uW_vzya4dOCAfES9Fb_20evj5z0P261ZidQexUH_vabKSVlyoMNnqk3DkkR3JMW_BfbvId5JLMGpjEOjybfjRnlMT_9Dp9Xf_KzMkooosbsHgv_wynAh5aZuFHhbAnsLSaO761lhwzosswiZ4QHtWORV-YE43xfwX6FBQ33jTdXkbv7PE0XzxQmuiqA8dBkWmq74p_lV7cQrMHSCSTqUB5sDOFH0C1MouKLcO5PXxopvunlAHceFhH07TdKWonYGOiJR8qR1tPzuNEw-SsVCd2s-x6VCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=jons2KYGqV3ZtX_FHGv3p9vYit9FcD9_9np3Nki97Sewskfk4MLgv37SgPE7hD61SObYBvl0iqTI5tOFzLItIWhT46W4FvW8VmnQYUypQdulzjdCiBzgY6eQvUWY9v9H27xxdS9gQLHGWp8i9DJ2fXJrYOPJdhrrTdsJIWT3t7prj8ZjOtJoACoU56a6mHGAxLpLcWfkQea8TUp91Qky3PYI92LQIU0GadBQZ_4RPZKB274lbljFWmpnkmSlWzXNr_MFP96o7LSQCBJGzzcZTluFunUL33AoyhaMikHp7wXckQR7x9nX2WFmxlGDTE1lGwDbuvbZQgmY7eN0k223mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=jons2KYGqV3ZtX_FHGv3p9vYit9FcD9_9np3Nki97Sewskfk4MLgv37SgPE7hD61SObYBvl0iqTI5tOFzLItIWhT46W4FvW8VmnQYUypQdulzjdCiBzgY6eQvUWY9v9H27xxdS9gQLHGWp8i9DJ2fXJrYOPJdhrrTdsJIWT3t7prj8ZjOtJoACoU56a6mHGAxLpLcWfkQea8TUp91Qky3PYI92LQIU0GadBQZ_4RPZKB274lbljFWmpnkmSlWzXNr_MFP96o7LSQCBJGzzcZTluFunUL33AoyhaMikHp7wXckQR7x9nX2WFmxlGDTE1lGwDbuvbZQgmY7eN0k223mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=F45FmmnNiMklv2R_59xy5Y1BHkBLFfYJRCOzX2_pdhlu6oPO6e_EFMIitrIcJbzI8CSHJvq74RS3Qpr0W15xF6zNwNEb6wAhXp3yc7Zb6Q_LwV4NQSCThvHIfE_MgYhHaZ94l8yTzJK1qZX36eQBjKM00EW1H_NigEjbMhiiR5TgM-79ZT3rRQMkIePutpL0qFIEkFA4K-tfiHhshoFVIsYc584HmC3KyVzJWxd3OR3SkikSmKUX5BqEHGS0t6gMkbbkoC7HfsGfayioCns5x6wZGAj8s9AAbFzj9PSa2FEKonH5fSSTrUDRs-xKjIXl9nAeem7_ScrAApRfY39bpglCWgipQ5At_c10nvS80sjNRDKii3GBYijYP9prfp57DOGWmVzwBJ3XzV7HQEKFMMD-CSEEsXeJDYv7jBHTc346_ybA_YlhdOM0giMDskr8nMhXas_Kg4GJyaYgxeN0dj570Vw7Th0Bb7p6GJsDCKvv_Ww9Hp4IRVos1Ggk01p5cZFF-7Rzh-IlfbF_R_zZohQHfIM-het-jwQJuFnl-N3bXcwKSifTvsCbvQN6iupIAHVdGUUX7oREgZOB8i-6M5kMy233aFjLGP0H5w0s-VJiABaEeKxZ_W04OaLF1U3-1G7_Abcvv_IOiDF2jlEPTCaks-XEzT5XWKYA758iNn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=F45FmmnNiMklv2R_59xy5Y1BHkBLFfYJRCOzX2_pdhlu6oPO6e_EFMIitrIcJbzI8CSHJvq74RS3Qpr0W15xF6zNwNEb6wAhXp3yc7Zb6Q_LwV4NQSCThvHIfE_MgYhHaZ94l8yTzJK1qZX36eQBjKM00EW1H_NigEjbMhiiR5TgM-79ZT3rRQMkIePutpL0qFIEkFA4K-tfiHhshoFVIsYc584HmC3KyVzJWxd3OR3SkikSmKUX5BqEHGS0t6gMkbbkoC7HfsGfayioCns5x6wZGAj8s9AAbFzj9PSa2FEKonH5fSSTrUDRs-xKjIXl9nAeem7_ScrAApRfY39bpglCWgipQ5At_c10nvS80sjNRDKii3GBYijYP9prfp57DOGWmVzwBJ3XzV7HQEKFMMD-CSEEsXeJDYv7jBHTc346_ybA_YlhdOM0giMDskr8nMhXas_Kg4GJyaYgxeN0dj570Vw7Th0Bb7p6GJsDCKvv_Ww9Hp4IRVos1Ggk01p5cZFF-7Rzh-IlfbF_R_zZohQHfIM-het-jwQJuFnl-N3bXcwKSifTvsCbvQN6iupIAHVdGUUX7oREgZOB8i-6M5kMy233aFjLGP0H5w0s-VJiABaEeKxZ_W04OaLF1U3-1G7_Abcvv_IOiDF2jlEPTCaks-XEzT5XWKYA758iNn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=RxndHR7NsL01xJ3HTehqfuTGRPnA7EFbJPmOsh9VQHvncsl7UqlFwjnB_J6yXkC_NbDBzPKGwUeezl_hmaF6e96SGKcMtrIzsJ61LDv0ayBsToiRtS0S_doYCwXBWvBBzg7ZQzBuhM1l4k36I1qVcFxH9HFsSGIybVhixjxEBkjz7k91cJC2mBHokpmRSe6cupVvgWL_igtapZ8pD7zvePhKmJI2a2-yQezy_zB8pmTR1I-Ocs-lKLI2x7mP-eXlU8p0oAD-AYYb-WXWJJ2HL8pRVomi2RT2gSqcYOSed4RfKnvb-9-QclBOhQsBR7gR59HYpzCSQDuz1XZ-TMvCpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=RxndHR7NsL01xJ3HTehqfuTGRPnA7EFbJPmOsh9VQHvncsl7UqlFwjnB_J6yXkC_NbDBzPKGwUeezl_hmaF6e96SGKcMtrIzsJ61LDv0ayBsToiRtS0S_doYCwXBWvBBzg7ZQzBuhM1l4k36I1qVcFxH9HFsSGIybVhixjxEBkjz7k91cJC2mBHokpmRSe6cupVvgWL_igtapZ8pD7zvePhKmJI2a2-yQezy_zB8pmTR1I-Ocs-lKLI2x7mP-eXlU8p0oAD-AYYb-WXWJJ2HL8pRVomi2RT2gSqcYOSed4RfKnvb-9-QclBOhQsBR7gR59HYpzCSQDuz1XZ-TMvCpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtiE0TxrylHFfJTrkQ0h52VersVhhX6bA4AJzCkXECfhBLRjssjuQaddVilFr2vEwNV-cQRVjvmPUcQ96Ebtn39DaUygvYptZRY8W0ulV7GJXY1Z127S0uuD66FXfYeymhuDUaD-XF6sAklSC_YAonHJTj13BSx7OtUUqstAxqgX6BUqadNHEXhvKFThnYABtYgsfD3FqadwgFN1whCgEGGInhQ0ORnq1O3MhbEi7bT8BOms_x33EF61y0ONlId2reNXrQ8v0GUlpZn91gW9Kk6snJbMoazNvEA7CoeAm1DssdMgKt65u1f8kDMO9g61siUgSQAsN5RJZM3yNJCHvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=s67TFjuA2OSP-41GorBrvoW-EgzaV6juEwQ1APnujKmt0jUeGn5qop9Sm7APbRk35skmwIlksQNUirLLMEzadNfqYDUGD69mOuTfN6EMXY8nYI2JP86RqvVpsBxctaFEH3efLY-Ro-sug2WoD1z5LZcHLBv0a4RGlDAttOXkjHXdLiK79MNaCrmtWjT9nDscCxd9jwGFvpSdjUmCIac6vZJxXaGEEbi1Hr1H-HBhCEqjBU0okhIYEi84NiMGndpOSnGCNd6SjjOWJy_yXvLXqQ2pmIhjanO8Lpj47pSJTntSXvG1NhbXcx9K0qGqjkBQZUsmvTHBykv0JWOqfNVzkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=s67TFjuA2OSP-41GorBrvoW-EgzaV6juEwQ1APnujKmt0jUeGn5qop9Sm7APbRk35skmwIlksQNUirLLMEzadNfqYDUGD69mOuTfN6EMXY8nYI2JP86RqvVpsBxctaFEH3efLY-Ro-sug2WoD1z5LZcHLBv0a4RGlDAttOXkjHXdLiK79MNaCrmtWjT9nDscCxd9jwGFvpSdjUmCIac6vZJxXaGEEbi1Hr1H-HBhCEqjBU0okhIYEi84NiMGndpOSnGCNd6SjjOWJy_yXvLXqQ2pmIhjanO8Lpj47pSJTntSXvG1NhbXcx9K0qGqjkBQZUsmvTHBykv0JWOqfNVzkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=sW5HVK7ZsJSAu9ixa6CrX3vbt44y-PEf_Bv33RNSECHvZUx7AEdQUc5nQje1y_vDixckZrq90Hw5-MNLL6q9UdCfdRzQbtnKTlL52AbuquZWCyH70DfEWBumg4I94M5CBEI7yCRpl75DXoVN6OqTlLf4d7BboG8czpuArBEIq3abSMMVNGQYtjeQumQ30-SUwrLtaAzb3jFbsw-P2oT_xxkXDjXfPI0Tnlg8ajuLPY9s4fk6ikIaFJpD6a5s9aA1H3OcF91Yuj_o3NY22hQ3yF8U1DD_APdZCq1SpQA7TT7yEemHs9fEF6A0SF6uLRoPZKDjIgZgnvuWaq3yzgSgF61fBIyxvjdrQzmOhYfXnCSN6Em2YE-jorD4g3w7FpMeRSJYv5qefp2t7cWNqP9L7e11VjoMIpP2JEa6Wy0d_3uJIqB3rNQ_cRCpC39BuScET8nRhuR4EujvO3to_BpusXfrG6uxaFGvpp_nsbL04VrfOr9-eXlqK1BNO3-rKRqM1iB-SfUmc7HXuai6P5MiSOUX0AtCAQbKz2D2EfvpTQ7YOm_u_QMP0mab2gpYJfIZzSvcSzV43fbvur8qn11hWpfHhrfXgWuuvzyD6QihGvLA1LzkqkTRM--a36v2oDeO1HEi2UqJJodNnEVkVbi-wsHIoRjiQZqzZTrDJA0qzF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=sW5HVK7ZsJSAu9ixa6CrX3vbt44y-PEf_Bv33RNSECHvZUx7AEdQUc5nQje1y_vDixckZrq90Hw5-MNLL6q9UdCfdRzQbtnKTlL52AbuquZWCyH70DfEWBumg4I94M5CBEI7yCRpl75DXoVN6OqTlLf4d7BboG8czpuArBEIq3abSMMVNGQYtjeQumQ30-SUwrLtaAzb3jFbsw-P2oT_xxkXDjXfPI0Tnlg8ajuLPY9s4fk6ikIaFJpD6a5s9aA1H3OcF91Yuj_o3NY22hQ3yF8U1DD_APdZCq1SpQA7TT7yEemHs9fEF6A0SF6uLRoPZKDjIgZgnvuWaq3yzgSgF61fBIyxvjdrQzmOhYfXnCSN6Em2YE-jorD4g3w7FpMeRSJYv5qefp2t7cWNqP9L7e11VjoMIpP2JEa6Wy0d_3uJIqB3rNQ_cRCpC39BuScET8nRhuR4EujvO3to_BpusXfrG6uxaFGvpp_nsbL04VrfOr9-eXlqK1BNO3-rKRqM1iB-SfUmc7HXuai6P5MiSOUX0AtCAQbKz2D2EfvpTQ7YOm_u_QMP0mab2gpYJfIZzSvcSzV43fbvur8qn11hWpfHhrfXgWuuvzyD6QihGvLA1LzkqkTRM--a36v2oDeO1HEi2UqJJodNnEVkVbi-wsHIoRjiQZqzZTrDJA0qzF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDtyK4mabzOYc2goVkxPoJjW4PDJ05kMKMJ_18DE5Fgkpx1r6NlYxL5nUvHZffs7Di5PuTrWx4ldYRKhKqjT__0gYLrvMfh2AX5Cubi4oK8Kgb_Foddg1lQ5YpQNEM7IYZtQKH5m7vyAh5QUTJN5guPLm-Z2IqRDW1Xz2fkSE2iOFv4badcH9JVQ9-eRwXcSgedmpcu0nQ4ptGVNzVqdMR4UDqHxP2GQDHoXDC_nwwN7_PYo0Y76-HoYEE79moaqEUoXQ_Gvpq0eezPI6l5GVMUdvwVPs9MRJJydS6is8uAeD4tUTsKQ6dZEiUWOTNfbRfyBoVtkMXUr-Ig3ZBn6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=uUydiXhnGUYfVPlNvPz8ZaJt4gFO3YwA2OJNtdZSC03Op1XyBdhSEe6yyw8QULmY1XbcPzYRXXB5pFYzjniDkJVaJ3UeKwTMRkedv3NjUh0v6XD1ImbGKBfGcvaN9tYnwDyrU8lvN2Gu5wjtIt6ZAH9-7GyqRp3FFhAtJhaHvq5o-GmlO63mb_32HrJiGuyAKLJTRnzzwq02qxoWkhUDj-9yi_rxMTmGiyJiNVC-mUfhjKWXm03hB_Bq2rzhpisnM7bqJyuJ1LneV_CebgC-Kj8dfM7_FuF8rB3mLozs-H1xCHhiApAlcDyzoeKZ2j3SGTGNTFsJIIvCymY2VvT0arI-sBctRpffZPCZJz_zDhPXDRJ6y-22v6-qXsU7kVUQKaYOSKfvJZYZgrs3fQvApSTkNjQM8fPmqqTZtNvtQY6MgpKEOmRCursq9BkBt3r4BVU8lDsUSs56NIyCHXZQThYMljI5YD74-jjePNMl-wOs-G4iuA7ATO9X-spw58rlRXzT4Tj9WEyEmv4kSxwHoThEqspxOxNZFRai0DDNf5Mb9nSytXcJgbVEvESR4lSdGcAc3SC0UuSG3qc2E35_GoHoiTOMnpKcmaGdRxuZGo_TGK2fjLwsRZgAYfC1MEvfEay_PLE2swEe2iJtNbxrPNgUFPsqdsewCAE64ly8vNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=uUydiXhnGUYfVPlNvPz8ZaJt4gFO3YwA2OJNtdZSC03Op1XyBdhSEe6yyw8QULmY1XbcPzYRXXB5pFYzjniDkJVaJ3UeKwTMRkedv3NjUh0v6XD1ImbGKBfGcvaN9tYnwDyrU8lvN2Gu5wjtIt6ZAH9-7GyqRp3FFhAtJhaHvq5o-GmlO63mb_32HrJiGuyAKLJTRnzzwq02qxoWkhUDj-9yi_rxMTmGiyJiNVC-mUfhjKWXm03hB_Bq2rzhpisnM7bqJyuJ1LneV_CebgC-Kj8dfM7_FuF8rB3mLozs-H1xCHhiApAlcDyzoeKZ2j3SGTGNTFsJIIvCymY2VvT0arI-sBctRpffZPCZJz_zDhPXDRJ6y-22v6-qXsU7kVUQKaYOSKfvJZYZgrs3fQvApSTkNjQM8fPmqqTZtNvtQY6MgpKEOmRCursq9BkBt3r4BVU8lDsUSs56NIyCHXZQThYMljI5YD74-jjePNMl-wOs-G4iuA7ATO9X-spw58rlRXzT4Tj9WEyEmv4kSxwHoThEqspxOxNZFRai0DDNf5Mb9nSytXcJgbVEvESR4lSdGcAc3SC0UuSG3qc2E35_GoHoiTOMnpKcmaGdRxuZGo_TGK2fjLwsRZgAYfC1MEvfEay_PLE2swEe2iJtNbxrPNgUFPsqdsewCAE64ly8vNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jA4yaKXRb10I8jg1NjIMPUwLacbVNOhEwBKg-U5md4TzJp2InKkbXE7QT38KaNW95qwctcDuYwXTqFEh3ubJR4JZ3VLS8OXMdIFm2Vu_6bL2Rk51EkFTwexNLRii7SktqrCDt6SyeyaTs_3Hzwnc7nD1lpUUYET8mrefbrBsC59f2yW3njnmbKRZXlRnXj6EqzYoplVokE7Do6WMduGZVYyv3TWBsaG-wcXvPuewR7nwumEG2QtiqMBXd-vrZMUQ_Hl8XtCUFLdSTPJ3tMz0WoWitqIaIL1TnmNHLS6qBZbzdqV9jVG_ESWdhvMRG4I-HKRySaPNvE1iv1XXinSIQyxcwITArK9BqAuLSTUmM3CTJkwTVS1gjkNmCIKTbyiMkssAoqwEjo1vZ16oF1Pu8rxb5o4jXZfpT7UOsjkUFUDfJ6aZ6VxPW_pMZXy77F31ySOE1uLRcIwoLJ0Bb8lgiu5OGZ_sdXwNDNgTABDPc7IMIe8JXkJ_6d-DA6Xv6bCRG-rHlfqR0RqaGNTUAyUx7C7e3RSNYf4_4Az-hRPHjwZHebjw-617GSYx3lE0ozH5knDbR9oGN8RXK3ZP21xnTVMFJdKm75UQj-TF1g74ToGg3SKhXIUiRD-TUnMN7QwjqQI9IUognZnqw9HDHpgkm-KjcfoB46eGZyFeuKnL4Ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=jA4yaKXRb10I8jg1NjIMPUwLacbVNOhEwBKg-U5md4TzJp2InKkbXE7QT38KaNW95qwctcDuYwXTqFEh3ubJR4JZ3VLS8OXMdIFm2Vu_6bL2Rk51EkFTwexNLRii7SktqrCDt6SyeyaTs_3Hzwnc7nD1lpUUYET8mrefbrBsC59f2yW3njnmbKRZXlRnXj6EqzYoplVokE7Do6WMduGZVYyv3TWBsaG-wcXvPuewR7nwumEG2QtiqMBXd-vrZMUQ_Hl8XtCUFLdSTPJ3tMz0WoWitqIaIL1TnmNHLS6qBZbzdqV9jVG_ESWdhvMRG4I-HKRySaPNvE1iv1XXinSIQyxcwITArK9BqAuLSTUmM3CTJkwTVS1gjkNmCIKTbyiMkssAoqwEjo1vZ16oF1Pu8rxb5o4jXZfpT7UOsjkUFUDfJ6aZ6VxPW_pMZXy77F31ySOE1uLRcIwoLJ0Bb8lgiu5OGZ_sdXwNDNgTABDPc7IMIe8JXkJ_6d-DA6Xv6bCRG-rHlfqR0RqaGNTUAyUx7C7e3RSNYf4_4Az-hRPHjwZHebjw-617GSYx3lE0ozH5knDbR9oGN8RXK3ZP21xnTVMFJdKm75UQj-TF1g74ToGg3SKhXIUiRD-TUnMN7QwjqQI9IUognZnqw9HDHpgkm-KjcfoB46eGZyFeuKnL4Ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=sFHSW-GrG2t7F9eDZeeAFDmet_zeRS5GNbg2r1Ym_iLQtpJNg8BvqgDmYwSSubkivdKpdiLQm_5UEdBbXAXPmFmC_QMnRER11dZC31n89uXMU6XPOnpG-2arKlSbzN3CoifTz-56Sq2znHH04DdwK24nAVDAGbGhkxbyfoy7Lh0U5NtwZGAGkDtYcQXdD-bHhCs3KG30qgFokxINeplVdi8YKozCmS2Yh4FT-rP1PMTYJdFrgGrcI4gWF8u0_45PJwRzn5TyTHqfm4vIkNPOmchh9QT7MRHLAZ1JmppBUnoOrS5v9yc-BR3iKF5oR25ECJ91lj83dOh-g9XhEdVfdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=sFHSW-GrG2t7F9eDZeeAFDmet_zeRS5GNbg2r1Ym_iLQtpJNg8BvqgDmYwSSubkivdKpdiLQm_5UEdBbXAXPmFmC_QMnRER11dZC31n89uXMU6XPOnpG-2arKlSbzN3CoifTz-56Sq2znHH04DdwK24nAVDAGbGhkxbyfoy7Lh0U5NtwZGAGkDtYcQXdD-bHhCs3KG30qgFokxINeplVdi8YKozCmS2Yh4FT-rP1PMTYJdFrgGrcI4gWF8u0_45PJwRzn5TyTHqfm4vIkNPOmchh9QT7MRHLAZ1JmppBUnoOrS5v9yc-BR3iKF5oR25ECJ91lj83dOh-g9XhEdVfdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=AMFHpnKTaCXgBDjKkCptD9oOcvzdo1HjLeqJRHeBviuk7Dq9elakkbQED6zQcSj10sj0AiEs5nO3Ivhxi8ZsrbTXizk5AYMoTYoU5D8wcr27CQS9d3yypzlI5yZMG97exOv7raNYPItzkUFe6Jr2UxI7or1_vlcALlBdvskvGjb2xaM_IZCK4pQZwT3IpuwToJp6BUzGb1SKEKF3gwcHlGyj0DMGBHmIULqPDzNZPb_0WF4kk3tdCixzsuhxESyYykt5R-RSVrEyub388PCmLAgA4pBmwhdQPI77IbGROZHfGXyv01xzA3z701mYB1H82_rMGrAsMlEvKndwjTybLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=AMFHpnKTaCXgBDjKkCptD9oOcvzdo1HjLeqJRHeBviuk7Dq9elakkbQED6zQcSj10sj0AiEs5nO3Ivhxi8ZsrbTXizk5AYMoTYoU5D8wcr27CQS9d3yypzlI5yZMG97exOv7raNYPItzkUFe6Jr2UxI7or1_vlcALlBdvskvGjb2xaM_IZCK4pQZwT3IpuwToJp6BUzGb1SKEKF3gwcHlGyj0DMGBHmIULqPDzNZPb_0WF4kk3tdCixzsuhxESyYykt5R-RSVrEyub388PCmLAgA4pBmwhdQPI77IbGROZHfGXyv01xzA3z701mYB1H82_rMGrAsMlEvKndwjTybLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=IQ8TUREuOrFQmpW6wjD5lMexFxCueZf4VhSL2F-pTHpBNBtdE72mxjFXHmf6VM3mscBnh1Opa7lccAniLZo4Nrs3wIL7RZMY4SPzB4Pltpj2TU6YIjCyRPjCq4DUcBOCvLlluGiAZOfTaA7YJr1OSiYhwgzIXKSEMk267r8QWnyxwv3tSqan5mVDHEPgjS5iIui-AxcYMI7Tfmbqq9-ZCnXZCG7AXH1YROzgZoe8JmAYAA4Jr2W0C_AhQnqhKg3A6xeiMjFU-PmRhk-1pcZxAbgGRTWoIUzAW3WgtCOlsT9PnmnByfzJstsrZFn5XGAksK4gf51ukHcQa2ggTc-4pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=IQ8TUREuOrFQmpW6wjD5lMexFxCueZf4VhSL2F-pTHpBNBtdE72mxjFXHmf6VM3mscBnh1Opa7lccAniLZo4Nrs3wIL7RZMY4SPzB4Pltpj2TU6YIjCyRPjCq4DUcBOCvLlluGiAZOfTaA7YJr1OSiYhwgzIXKSEMk267r8QWnyxwv3tSqan5mVDHEPgjS5iIui-AxcYMI7Tfmbqq9-ZCnXZCG7AXH1YROzgZoe8JmAYAA4Jr2W0C_AhQnqhKg3A6xeiMjFU-PmRhk-1pcZxAbgGRTWoIUzAW3WgtCOlsT9PnmnByfzJstsrZFn5XGAksK4gf51ukHcQa2ggTc-4pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WtoVR1FpvKgJnUqiNcbkRQuho01vO-687DKaopgC908VQIOnKKmmzO0KRzkzdbS4DD-k_rDjrkGEJl9LVOcCOUGL8llhoXstjpO8uOeaDuP1CetC_UBs0Va12bLfUv4PRbW7UCzAi_Uy1wiv528-pGpVLprips6DjjRXZAbqM4OZLESNGs3ZClgJ1IH-Pr6dVrEMJbWZIDtquYe1izj7_4O0poB8m8XOiKIhOXSsYV5OpkisuTGZeeIsHxdxAOSfSRejgwhJMEjrolnhxWugqzBkngZe5PizdcDtA3EVk17jgBqAAgYXpSInibCQQls96IpdSH41ItuB6Nb9M9hFaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WtoVR1FpvKgJnUqiNcbkRQuho01vO-687DKaopgC908VQIOnKKmmzO0KRzkzdbS4DD-k_rDjrkGEJl9LVOcCOUGL8llhoXstjpO8uOeaDuP1CetC_UBs0Va12bLfUv4PRbW7UCzAi_Uy1wiv528-pGpVLprips6DjjRXZAbqM4OZLESNGs3ZClgJ1IH-Pr6dVrEMJbWZIDtquYe1izj7_4O0poB8m8XOiKIhOXSsYV5OpkisuTGZeeIsHxdxAOSfSRejgwhJMEjrolnhxWugqzBkngZe5PizdcDtA3EVk17jgBqAAgYXpSInibCQQls96IpdSH41ItuB6Nb9M9hFaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Z_hMJD8D0WyGOMzGgAeYJgHuhkjSyuXn3xKcokCOzrvwmxXDaZ_WZnOt2CJGV4sKYUx3iRWaUCdSfpd0jWbGHfosHxJogfG7BmHFBLvfXYUVCixErx1PL15ViRMEvKi-_6as-sL5OhKRVkv3gXJXnjtyZMxtrv-xD8uDK6hWR83dzHwLjrGyoSGVaM9wTP_i4_Z5a8n0LRiI39wlvXh5YoOFf-wCvEZr4ZViQKb9OjqhxukBTlCUex3QnDPgE11jsSR9hqHVab0JZ7p7uw7T7fE7BRNq41wNP5DcJFrO5WynHtLwBozNv9LisEuYN47mTrg7NOtOIG6Vj2B3LeKvDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Z_hMJD8D0WyGOMzGgAeYJgHuhkjSyuXn3xKcokCOzrvwmxXDaZ_WZnOt2CJGV4sKYUx3iRWaUCdSfpd0jWbGHfosHxJogfG7BmHFBLvfXYUVCixErx1PL15ViRMEvKi-_6as-sL5OhKRVkv3gXJXnjtyZMxtrv-xD8uDK6hWR83dzHwLjrGyoSGVaM9wTP_i4_Z5a8n0LRiI39wlvXh5YoOFf-wCvEZr4ZViQKb9OjqhxukBTlCUex3QnDPgE11jsSR9hqHVab0JZ7p7uw7T7fE7BRNq41wNP5DcJFrO5WynHtLwBozNv9LisEuYN47mTrg7NOtOIG6Vj2B3LeKvDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=mPqcezX7TXkI86dmSNTVDUVOkMfeyTLNn5LnqpvUy3kCP2DZVRR0VkKGSwjVyozEeGYFlILX1othLyytXHMAnOXn1llQuc9P64ATjxThuOLiDwfWyKECspPqlrTsQLUUzJOwyAGOaYA58F68nUlk77ZnB-4Q5g3tZRAPb3fW75soXNn4YUQ8Pjc01ks4ogadZAtz-iIGAQ7Fb0NdkxxCwmpSkyhaOG36a5sDJRno1IiIWlZPr3ETpVEzpNlJelkqn68U-CPLo6RT_vtZ1XXNFTHvwo7bVKsluqzKTWDlho92E__fVBPEnPpnEuBsxfDlzxqN0TMZGuInV08o-mgxoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=mPqcezX7TXkI86dmSNTVDUVOkMfeyTLNn5LnqpvUy3kCP2DZVRR0VkKGSwjVyozEeGYFlILX1othLyytXHMAnOXn1llQuc9P64ATjxThuOLiDwfWyKECspPqlrTsQLUUzJOwyAGOaYA58F68nUlk77ZnB-4Q5g3tZRAPb3fW75soXNn4YUQ8Pjc01ks4ogadZAtz-iIGAQ7Fb0NdkxxCwmpSkyhaOG36a5sDJRno1IiIWlZPr3ETpVEzpNlJelkqn68U-CPLo6RT_vtZ1XXNFTHvwo7bVKsluqzKTWDlho92E__fVBPEnPpnEuBsxfDlzxqN0TMZGuInV08o-mgxoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=qw4Sd0f-me9fY65C9OG8Y3CX8KOmrGUTV3QlJP0uE6DrOWTyigujti4Iykosl0SaHQJato3iwHNSP3p5uFPuO10KyZrLCz46GhZRpEtdNrCgbNFn92rkhxP6XSnXl-JzjxFCGqLRtt8l7EL9uDIDT7jHICNiNDT2CoV_pi6bNlLaF-g1zS7dKVVTmTza8Q6cMyAgcyFzKj6mcfqA0nN-V5DVFRXeuN6gITlQnHeHel8IyORKdR3GWKEVhT5E-IZnVv-ZJw7KwPiSb9z2uSFDPnxiRU9GKvipqhgJWi1eSWhebar1CqgyXnSoCICSXC70fsa3EzLl0cixXGconfB1Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=qw4Sd0f-me9fY65C9OG8Y3CX8KOmrGUTV3QlJP0uE6DrOWTyigujti4Iykosl0SaHQJato3iwHNSP3p5uFPuO10KyZrLCz46GhZRpEtdNrCgbNFn92rkhxP6XSnXl-JzjxFCGqLRtt8l7EL9uDIDT7jHICNiNDT2CoV_pi6bNlLaF-g1zS7dKVVTmTza8Q6cMyAgcyFzKj6mcfqA0nN-V5DVFRXeuN6gITlQnHeHel8IyORKdR3GWKEVhT5E-IZnVv-ZJw7KwPiSb9z2uSFDPnxiRU9GKvipqhgJWi1eSWhebar1CqgyXnSoCICSXC70fsa3EzLl0cixXGconfB1Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT9QEEcVdWCI8tdzPgA16BFG_SiANJ-sf9WMQwwq0BpusYc39RlWFTt-qJV29hn_yQqh2Tun1CiFBYFFxMn0iaJtsOT9k4sVbxQAByp0U4LRmidZZ4zffvxvjHBnWW2lzyWw8UJcyTdQrzd5sqdDdAJ1fteuoTapDnPWYICl5Tz5e0z2fwjR2Jhv4bmSx2soiw5hlEkmh-sw6isuqyewVhH1bV3PYNJxWbIkZOSWzhdSPisOjEIZ5vk7UEAyAjRWjLqGaJJxJXdprTswjmJ94qlKOg7t-yJxv-RR1XwDmfe-2UCf3QkVl92RIb9aeHe2-5t4oGrV1HIh8kz_lBbNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dqt1HURthoWAQCOXo893e-yK0InAxSP-WkS4grtH9zSiBEKDlBqkizWNuvGv8VNH9QqGFqTBJ0LMiaxBaz4q77VhWuSD6cwjvepVK68-Gdpa87ZUhlHxoNiEtZeO9ik40SuaUBxo0PuQozLyGXtZ19X3vYmNUDmfZ4YslisSEjD7-SCCCBCy9y9SN7eJ-ybG2K6Xg1qd_OPSAvsgcJF7d-TK8w0DVedJZrPnTafKlqbcqUOij4lJsjRxHy1rL-WicRXdm_NfpoS8rqUW-tHe0ILJGR471G1zUZP92Te1kcaoZxbVYy3pzJOk65uJAUAlpFnKc4coh4Ql4mV3qmAXiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dqt1HURthoWAQCOXo893e-yK0InAxSP-WkS4grtH9zSiBEKDlBqkizWNuvGv8VNH9QqGFqTBJ0LMiaxBaz4q77VhWuSD6cwjvepVK68-Gdpa87ZUhlHxoNiEtZeO9ik40SuaUBxo0PuQozLyGXtZ19X3vYmNUDmfZ4YslisSEjD7-SCCCBCy9y9SN7eJ-ybG2K6Xg1qd_OPSAvsgcJF7d-TK8w0DVedJZrPnTafKlqbcqUOij4lJsjRxHy1rL-WicRXdm_NfpoS8rqUW-tHe0ILJGR471G1zUZP92Te1kcaoZxbVYy3pzJOk65uJAUAlpFnKc4coh4Ql4mV3qmAXiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=dNW5X-cw3vjrUOQH-ntlqGrYiqGTNn3Z6AHiraXbH8ZTXJcud7GMORh74fKhoIO9_q4eUaWAHlyH8i0HcuzqA1zT97JE_UFGS5NIMyW0EVCpWjf2e4SCsMK8q5r8m1z_KemhDW0oOWfFgV0lvfwZ39JcCfX0F9HhTD-fL-0VIC3AcQPXqPd-Lb2RhbIDAeRkibM0Ct_T6eccTRMqU56k_uS5-BstfKMkiilakYOw7CWQ50kqIr6qpZ17PgCMCCNF5eDPSSPL0DjZ5Pz90xwoc_0fBxZFcTiF7U0JeAHlkHBF-pMdPEsoBC_YqMPacE5HcZ6CEYd_kGWlYnUoaf8SZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=dNW5X-cw3vjrUOQH-ntlqGrYiqGTNn3Z6AHiraXbH8ZTXJcud7GMORh74fKhoIO9_q4eUaWAHlyH8i0HcuzqA1zT97JE_UFGS5NIMyW0EVCpWjf2e4SCsMK8q5r8m1z_KemhDW0oOWfFgV0lvfwZ39JcCfX0F9HhTD-fL-0VIC3AcQPXqPd-Lb2RhbIDAeRkibM0Ct_T6eccTRMqU56k_uS5-BstfKMkiilakYOw7CWQ50kqIr6qpZ17PgCMCCNF5eDPSSPL0DjZ5Pz90xwoc_0fBxZFcTiF7U0JeAHlkHBF-pMdPEsoBC_YqMPacE5HcZ6CEYd_kGWlYnUoaf8SZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oX2ogxMdxXjJKYams3lm1ito4AL0DgUbAn7MqHp_lBHa0EjkDkqmf5mIliUn52_fyu-Ty0B42bgAFzGgfuSfBW2uK8lF79EyjxWRYw7t2mDoFNrY8vEg8xQB7tW08vsLPETCJltImwnCqIVAzDf-J47SCOi4vIXwBO_OGrFR9L68YbuRMJ9HoDM-duAH9zwFe4QNkPKZn7SChBqxPHeu46pzsq2BQmMtnkK1t1NTEA9tV0Pq79sWbnJNkSj9dS8Hleh9FIFL5D-YFhKrBX8i9THHjCpbcMf6LZdE_PEjPKjQGpr5_h7BkD_adTFKBnpgWu_O_FbE7ZkHYnBVZd7lZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=oX2ogxMdxXjJKYams3lm1ito4AL0DgUbAn7MqHp_lBHa0EjkDkqmf5mIliUn52_fyu-Ty0B42bgAFzGgfuSfBW2uK8lF79EyjxWRYw7t2mDoFNrY8vEg8xQB7tW08vsLPETCJltImwnCqIVAzDf-J47SCOi4vIXwBO_OGrFR9L68YbuRMJ9HoDM-duAH9zwFe4QNkPKZn7SChBqxPHeu46pzsq2BQmMtnkK1t1NTEA9tV0Pq79sWbnJNkSj9dS8Hleh9FIFL5D-YFhKrBX8i9THHjCpbcMf6LZdE_PEjPKjQGpr5_h7BkD_adTFKBnpgWu_O_FbE7ZkHYnBVZd7lZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=I_VDL3lekGt1JGNbFhWKU07SZNIS_dFzbytfgFrxy_Lg9CGNevsY35n7Sz-jIajdV9Rt86C50mKXcfcu_4BJ7DVF0FNTsVdUxSouYIZG7w2y_2ax_YC58cyYRWB1p1i62_QfkZZVnGJxpD6PGLuq_p0Pr5X6rZLezghD2OB4AcUcNLc18oLB-Tg729iC1L5SzhhwQYBxzsZDvKM3IOtWaL87mhlQoQ3x7WF-uo-50LMi1xuHVJrAcR1d73sHErWUpVRYIAs9RgCVKYZQiVWD_3h00L3m64f0C5I7HpFlnQPH6UoX-jRK-yEHqKlffiPLUzuw0CRikwbRAWXTKsu5GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=I_VDL3lekGt1JGNbFhWKU07SZNIS_dFzbytfgFrxy_Lg9CGNevsY35n7Sz-jIajdV9Rt86C50mKXcfcu_4BJ7DVF0FNTsVdUxSouYIZG7w2y_2ax_YC58cyYRWB1p1i62_QfkZZVnGJxpD6PGLuq_p0Pr5X6rZLezghD2OB4AcUcNLc18oLB-Tg729iC1L5SzhhwQYBxzsZDvKM3IOtWaL87mhlQoQ3x7WF-uo-50LMi1xuHVJrAcR1d73sHErWUpVRYIAs9RgCVKYZQiVWD_3h00L3m64f0C5I7HpFlnQPH6UoX-jRK-yEHqKlffiPLUzuw0CRikwbRAWXTKsu5GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOsO7W0Kpat7a6dP4UIHF2gkimbcEvmsFbYlIZvtL2lVAWTYqfulyiV7hcCrxrZCSXfCi-J-FpndSFznS8559jX5uxWbBuUUnQPImV5kSc0k1rabv6ngNxtTqfZVEtCDazsF1QAQ-o-WZWnVBs0nUKzTtvDIVzCSL-eysf2o81kpxNSc_AuyYUgHU5FYTPEbNrzpepnN-Clrvmxpdv2EGLL-r9x6ugAkwETCe6ACmLqpNxdLE-b1z1V2nH7KKTNyRjT4hWgnFmQhJ5Mj14VYnGVikyBUf6o5nZBhAipIBDepyU02KclQGfDcbsZQS4-CKDmJqy1-YV8ZofWtSCVEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=u21e7rBiTf3Q8_fFYePxY6DYZJ-FlnIlSGC1vFQkN8qUP23HAKFsCNUMKmh45-p2D75UZer7d9jOLLdTWHmaFJCRvLQhIJMgeEdAHL5OORY0qNE6kK5eg-LHk0aDKkIO8peZuhJhExdOP8QN_w2sk_Z1kU03nzgzDxT5WYhdM0MqVOYSmAssADWT9Ciz75PaF18EvnBS7qiPHTcKnTtkfLla2Y4uOVi1goZ7zKtnE0tOGhDQZcA07Gb0bFasQhOTlEhxKJ88dcQ4b8SgfoTedMWD-iRkoyx_VPGGAjzTL2cUtILuUHBWbEo3Bl0J-gB_N4gx8_jrGE-Kn6JAet-KyDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=u21e7rBiTf3Q8_fFYePxY6DYZJ-FlnIlSGC1vFQkN8qUP23HAKFsCNUMKmh45-p2D75UZer7d9jOLLdTWHmaFJCRvLQhIJMgeEdAHL5OORY0qNE6kK5eg-LHk0aDKkIO8peZuhJhExdOP8QN_w2sk_Z1kU03nzgzDxT5WYhdM0MqVOYSmAssADWT9Ciz75PaF18EvnBS7qiPHTcKnTtkfLla2Y4uOVi1goZ7zKtnE0tOGhDQZcA07Gb0bFasQhOTlEhxKJ88dcQ4b8SgfoTedMWD-iRkoyx_VPGGAjzTL2cUtILuUHBWbEo3Bl0J-gB_N4gx8_jrGE-Kn6JAet-KyDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=AjcHrnvEdN7SG3-qJ4KZOjMj4zD8mdX_OceTN-mQtzyizeSilmz-CN6peTSfauCjC0NDUZAuiKol7avxz5g_Mpjk5HqJj3LWpM09Hxn73IKB3llClFaYugviba9Sff8V_nGnStVbTMRgVhwqVjKvvAQC1fL46JnerI9Mi8U82p1VZoWg22QhF0PFkCOwgyqOF8pzxIRyefLz-LP5CersI-AwWDyW2P99WxkR6wL_lAqaN7c0ictPJG-6NCk0UgpFD1ItzVq_DRX32hIR8WFFGGjIBsSUmKgflRR40wMQauC6QCt0wZOiRuxcIKhIOGRN-IoKoxVswrpdZlOkSAPgNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=AjcHrnvEdN7SG3-qJ4KZOjMj4zD8mdX_OceTN-mQtzyizeSilmz-CN6peTSfauCjC0NDUZAuiKol7avxz5g_Mpjk5HqJj3LWpM09Hxn73IKB3llClFaYugviba9Sff8V_nGnStVbTMRgVhwqVjKvvAQC1fL46JnerI9Mi8U82p1VZoWg22QhF0PFkCOwgyqOF8pzxIRyefLz-LP5CersI-AwWDyW2P99WxkR6wL_lAqaN7c0ictPJG-6NCk0UgpFD1ItzVq_DRX32hIR8WFFGGjIBsSUmKgflRR40wMQauC6QCt0wZOiRuxcIKhIOGRN-IoKoxVswrpdZlOkSAPgNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGzQP9TI0_hcvvTSsj_YYYiVjAu78UbEpGXnPwxjN2kJsC-M3w4fcQiCWC6iaDhOGwmcxDiYMqhXRsrSo0aKkfiAchffWCRXAUYq9F_cs6_DtETlB_XXK10dItK18bIknoq1HTE3iHChV6y3ZiKRWOSYPIpnZZROtrRxikYrSFh5iy8pPNMfDNMhmbxgu5eTTZuuq4rSTADLynGzxMi15WF7SAdrViHZd-6YLC_gcHen9lqTr-fDNlpuK1kWX0kEqxVuC641DXdwm5-7rhucKQiIvvgSQBHgnPZG24v7Cc645oVTiph71dpmyIsOjGjDXIOzvAxpl1JhXryJRy27zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-qM9Pv-Pz2qkd56R7AjRBmQmUv-4TQBPx05W38yUVIwrQMvn3TRGXbbkPt9oGxbgbtgJjIEdjGl8ZRARzNxNryZmWyu_YxDiUDbvKq5s5DXr38jdmv9oMKmWgD8PbYHkfMN0bW2ZahtbiFxP6IZ-Ek3AqVa8idI1sfEkcSBFGjvRwCq482RvEbcvv7qxCWYaLHbmZZAz_x360sfVxTyO65gIxCGwORzxa2yGWPvlUyjNrtFCBrGv284IhqNJKfGD3wBZVB6xzYP3u5CFniEwRiXZgnonKSHZQT1vzHxTj_87ubu7rz_qe73LJmHzjAkbi86u_QW-DP6X1qvMrPOpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ug0sllgtAIbY4haWpUdONJCstQx_vGkr_l7vpvf9XbzkkkSwUNnTqzoBZikBc-xW6RHmp4DxadIDSzruzLph19wdEothzWKoWBKjaQGv30gVn39aWpXbM4dngLu3wOdRx0OdoiG6nD5-0ED3MUCuQ1x7q4xd0SguTi6zJJ1PSzdKr34teHjdeEE1MrJhdnDQ35JaVmEE-mIjVARVqjfEY7KQ4R6U8tbpbR_mCsZEyGezgGcj5mFjcieV0CH7H-SaF7_jTUve5kIwXq3KJRhXbBbtnaGdwfGC4F-uNc9ohQG4a3YQHayWqJrpw1Oham-lJ_YRNdeaHG0HeSvsebNikw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ug0sllgtAIbY4haWpUdONJCstQx_vGkr_l7vpvf9XbzkkkSwUNnTqzoBZikBc-xW6RHmp4DxadIDSzruzLph19wdEothzWKoWBKjaQGv30gVn39aWpXbM4dngLu3wOdRx0OdoiG6nD5-0ED3MUCuQ1x7q4xd0SguTi6zJJ1PSzdKr34teHjdeEE1MrJhdnDQ35JaVmEE-mIjVARVqjfEY7KQ4R6U8tbpbR_mCsZEyGezgGcj5mFjcieV0CH7H-SaF7_jTUve5kIwXq3KJRhXbBbtnaGdwfGC4F-uNc9ohQG4a3YQHayWqJrpw1Oham-lJ_YRNdeaHG0HeSvsebNikw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFwlbPR4OHy9NCSmQvhpya56y8n4BdNlfaDYvBL6XXPSh3afDtI2BLkkns2FXKWBsg-eH86TX5aFC2Kv8IwxNCFG6gIjmb4nUg3gQGcgnBYGyiDa_bvaGVz9Yt5PsvgzJ1uZScOFffsP8-HAS4SAH5tHgpVlrv3h5-y9i75ga1aELDGK0jmXlKkX6712_QxOLid2euq-8hrzmpCjyp8QCkNZ2oRUQOzbIWZfKb60_lSO1azcN9fFYauSB5W7Hmu2MpkjUF0WrTLwIaTkXcqjQWo5ozfWoDz-w4XZff-dFAOVOKj2-b2Y29QyoOvdCgLqRV_TKdpGzdR9vh6BEc9FdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
