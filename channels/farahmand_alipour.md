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
<img src="https://cdn4.telesco.pe/file/lcAJsVvK0ve1DjFRXkHjd9_8632bfWUPzUoVH4ttCYMyIg_a-A9i3ZbxDspY_c2funG1JSKLDwoVkk9SYrPF8Q9-uC208rENsU_RPHNZ3ji0d5bILwFWL4tEV9iOJk5Af520b-zfqihprlo8U5i5_u--KpY0AOIa4ydj4Q2rrIQtH9XHxFSsOhy_zLNKkGt0E8iKhTSAzicUat6e2kpAIYvKbLnFHQVAtCP789yHr9_apANp_Q9Zd5rp9F9lSZxwXv4pw30ZeqsWO_wDNy1JjH20Yq3coz-I2zVZk6qQFygGjtjv_sIa4xezTfIhDlAblCRJMKq-Tz92RV52sXXMJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 05:04:34</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkU7GP-7UdRPPrkQxpLzz2Ubr7NZLzhYLK5ylbjiGMH68dQssEh2c8-XBy9VO-OOiWIUOLdMrJxJk_MJWSGsNvdHgM1mmySixaOQGJoo_Ky_EPA8j4R-DrtTEljhYectwB-l_NsJkYdHZBJ--SXN-6EhO4hKyYAI6zvJckOK1jAC-Jum7LE6O_3rUug1ckOh5BLCGYjDLEfXrNvz38T_DsPsHt0C4lON6Puj6u88NBrh8jZyS1PdO5pZ5lWG6zXyVr5FdubYOlDEq7YlKt0KIsUlx11dxVDIWfcjJ37KqGyCYU2CjUeR1DxSPsXWq7dX69Pw81lCp9LZD-1r14kOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvG_MmqYw18OWuvXMyX_-x2nIY5NjEMYWomy-V2iZcD82mDSzopcBzVAbgCELFy5ho3rYbP6wrPha-EASXRMA3i55snhpwTJ6Ym4xD3HkFTr7EcmnbB9uAnotYlPaqjaDI1Rulor5ZdVMZddbr-kPixR-5wFmoFgSsx59vCJMRTIPmRViqmUtNjEzz_hCGvjqRiScfNWQ7x6S_MhLaydzojTC48aDId7kXApdN7m8ME43Vgxdrb-q7ob4JD_PBVz0oeIIVqEofbvgh-Q3sCVM20IYxc2DlTf5slJljB9ZL-A_m_csuzTE3QSGBq7gXDQcP2qgVFY5PxTugyGAUJKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO0R0JyAdCAoQQ3eo1-Lm7AIfJCcP3PG_4Xoj--bf2aJrENx_37lSsu-joPz2qnjGROAc2FuKeX_8IFyeJd1of5cVUUNMa6PJWWDWpPI9Ze6_RUW0P3o1n2GRe_rwAqAxqmmAeWJ1V8Nrj06mQ4vIhwvlcpRFVY5Ru2f2Ifn-NJcWWzxwcA09-r3KJTOgGhvOCFnEm4dYMRQ-9ihOJXmWW8-QRHyFXoMhvwmZfB0ib1T8aZ5gUDfhvhm-MgwraoDWKO8PpztQcHP94eRF0dkXyWpmnuIHGgJFbT634TnUkr2ZQpxjmXA9O0PYlo_b7CYcFIXl2Mb1r07hMr5-iIQNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct-C0ImeEVTluvheWAPpnR39Sy6ex6sUYOqb4Giojut6X20fOmiMF2OmpKf9WhRv_3_PMiyUW1Rw0zC7IIjtJzvBfCL6KHmp_rq-wnnsZEjzFohaKZRzDLBpgvuwUqSOVF9VGQeb9gITRSsYOlSF6wmFfZ9XmIAommHBVl2lBCTtbIaaszrnLLZkqxdje-O2e57PgRgA_JlhGdOXyIgfnOvPI6lBtv4zywX8LnByEwCo284xfW7x1fEQH2ZzDsdnVLHne51kvjQ_LBpybXXWQSr6g_3NnlTSMWge7m5m4nSHlDu5Ls8YUCLxBh835e4rDKt8dYsbLDc_ZjHBs00ucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InTBu4sUA50Tu5FiMkNOP1bN19tjF89Hc2TQQTkWRaPfa-EhmBIHw4bRWPvK4uj3QcI7G2YGPFn8iTcrzgPAx7fBYtmOM90B9D0myKwMgFdh8VxTKEELJq-Ajg0A0S5KWx6m0ug7OZj3ZJ_YeJHlMas_4Gvj3zIADemvwZoe1q8ZvD-0mzfc4HhDDf60bI2TV_Wp7k2TsQ-Hq9zA7SaGY1Dre9u0R5rac5SKLw1Ic5ZTvUM1KTqJI6JWjEUiVIInyIylSzTa0NY2nH8WetQ3ianR0We8qoJTh262cHKVf-fItR1Ix1IvQHL5ADaNsGKckL7QyqhU73Tjo0ZiiQG4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=e5I2UhE1g4RkFWvuWio9eXPc66Qjc2IAfMGF3k2UR62d3HuzhQEDGA1gCu14On2DNUgSWAY5gdX8LtxajE45Nc9VKbLx0HF_fvLLOHxt3wEFvFAmUMBK1t7CkD7XEaoz5uMLxM8y1MAhwuNfUiL_Csd_k7VaTgYTB73q_VsNsNbeSM92HrxnNGm9vfGVGVZicnxk7WcaaBBRLAOVAl42B5pQXbB8BKiPoGriW4nrTIJvP6YAnEbZkcS-OkrAFng0dQrQZHR7PQ7jvB7BxKbw17vI4sHXWjdt-bHKzHJDJ3ugJbeQuJR2FwXg0x7xMgaPC2zRo6_hcHxi3ptFV0Z79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=e5I2UhE1g4RkFWvuWio9eXPc66Qjc2IAfMGF3k2UR62d3HuzhQEDGA1gCu14On2DNUgSWAY5gdX8LtxajE45Nc9VKbLx0HF_fvLLOHxt3wEFvFAmUMBK1t7CkD7XEaoz5uMLxM8y1MAhwuNfUiL_Csd_k7VaTgYTB73q_VsNsNbeSM92HrxnNGm9vfGVGVZicnxk7WcaaBBRLAOVAl42B5pQXbB8BKiPoGriW4nrTIJvP6YAnEbZkcS-OkrAFng0dQrQZHR7PQ7jvB7BxKbw17vI4sHXWjdt-bHKzHJDJ3ugJbeQuJR2FwXg0x7xMgaPC2zRo6_hcHxi3ptFV0Z79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=eiaNBoZ_MnYSDzyhZp8OGQwVQzxInklTIjWuDgkG_b5whUxQVOGQ_-SigyKSz6QhvZZ_p65dZ-f5RDk4OlCrcmGe3DpiTFpFOtnyWL5JYQ5GK0Ex6S0asp6k3zHnWoYSoQRDqTAj0wqtuDZYb2XCbQka2Jlvmc3cyY4KcpzEtwc7704j6RfD3VYE7zv8reDkz-b6-jGsarOge6m-hXtC22j8d9DWPhKWb8AYbKYli9fsZcUcq6PUQ-DJGZUimNyyxrUWFCU_pPBUtIPSPH7YpSoMnVeJOhsWbIiU9OS7E6hSnrN1QVZMNl69z_AmaGK85VjOfWsjEoaa8nwt2X-UAAcYqsIT72fL_3UT_P6ub71DPc4fngPbM8tTwgskwyGO2iis73hLk8i9sxDci2YMwOUIh_PWWJle7Mzq4rrO9AS8JItktYgNnSQT8PGu7YwbdAIokLMq4cLCXoeHhMS3sVU1r1nRMHSFircYknZ2aZ5ERHo26nVjViSngydM9rIDEhoLNB4aQ1XlYm9qiGH6_OOAUpc4458zrQTrbhioztPh2rDCU8Gpyv1eYjvMkY0dyLp7VtaL1C_bcZkDSgpbDcJYrdA7ugZoqFZTveymzXHgnSIe-dhV1mhQekfvItjIaL5ndEYcPTW8SehEHW3kwK4-VVh4XVDHTLXbojysJRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=eiaNBoZ_MnYSDzyhZp8OGQwVQzxInklTIjWuDgkG_b5whUxQVOGQ_-SigyKSz6QhvZZ_p65dZ-f5RDk4OlCrcmGe3DpiTFpFOtnyWL5JYQ5GK0Ex6S0asp6k3zHnWoYSoQRDqTAj0wqtuDZYb2XCbQka2Jlvmc3cyY4KcpzEtwc7704j6RfD3VYE7zv8reDkz-b6-jGsarOge6m-hXtC22j8d9DWPhKWb8AYbKYli9fsZcUcq6PUQ-DJGZUimNyyxrUWFCU_pPBUtIPSPH7YpSoMnVeJOhsWbIiU9OS7E6hSnrN1QVZMNl69z_AmaGK85VjOfWsjEoaa8nwt2X-UAAcYqsIT72fL_3UT_P6ub71DPc4fngPbM8tTwgskwyGO2iis73hLk8i9sxDci2YMwOUIh_PWWJle7Mzq4rrO9AS8JItktYgNnSQT8PGu7YwbdAIokLMq4cLCXoeHhMS3sVU1r1nRMHSFircYknZ2aZ5ERHo26nVjViSngydM9rIDEhoLNB4aQ1XlYm9qiGH6_OOAUpc4458zrQTrbhioztPh2rDCU8Gpyv1eYjvMkY0dyLp7VtaL1C_bcZkDSgpbDcJYrdA7ugZoqFZTveymzXHgnSIe-dhV1mhQekfvItjIaL5ndEYcPTW8SehEHW3kwK4-VVh4XVDHTLXbojysJRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0lYtwD5-Bx5vrguTVpuewmf2UUbIz24RJJxleH6pkQWRGPB-lVuhfoituLqaoX8UEObgoiZL9ULdiv-YbpUBLh6871OkHLk8MK15ypPmHpSbpSPeqz2wOyaMfYRMyZ_kwgv2pQMKpagxoHv0oVgQgjCaF7EVrEHEoOUpS-w39629zktib7tjUhR0e2fq3nAZgp2L0EVytqlV1DcukHf9OsoGGhMkvNejRMxFrtEEcMbVTlSKh8NZxNZRT7JqQuImJOfcABIJXyg692FHmablmBJm5t905t3rfTENg4_vaeWwaYNxJASg6lyY7eMDDedNwi-3W6ZYpKrZkZQjId_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7EG44N7QGSWJugR3B9JgJCmE8pAr4ZHmxPnzXP9xkJUClK6I-hS3il0ZfeyEEn1MrnDtYY9AQmbx5NvV0YILku1GXKwQFXIB6tw3pdn6hLGmhpQfnFqreFV32MnyqOIoFNk8RcFVEsKcoNdjLG6LSPeeIG3sFC_g3v3_X-cXS8TEVzS_D_Zv3LAE9pcqIDZgGtJVsRDmfNd524Dk1qruQuHOLwLC7aUxBDWz-Y4Sxxk72z8NBcEGL7aGbfmmuFi00XJu29G_WRFsHPJ5g5tJztbmfBJQC15i4iC13HHWcMw8Lu69UaNCDORLMbp6A0cXFdTYkglIDwBKr9SONKq8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_EvW3_JSgrZJs5e0oVbWkALhR5Wnixd36XBvIvOXz_dKXW1jhDEO4aZ_SXx0_ULRwq5Wjt6MQHdae14XpQY3i5NdCMgYx1vOXUo-qSi03NC_Q-E8K6837jIp5Ve6qclnFBkwWaWKKGWPwZDGSBhgDqJNcS-0yKiwxUuU57AUAmDt6fyC6ebCpc3t-_d9Ts6HSTsC1gIAR_-EwkEqJGJpn-MpJdH5yXi83Macot-iY1Ve19g0WsE_BiZFeIe3DMujAdxc3ytJLf7P-6LPjq03KYB7j5FrsCJE4icbYkBw9cPw-zgyWdZgEDkKBHrythwt8l8CkSLLppH9oJ8nekbPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=SEjT_x_BAkf4Nv1cJdm9V8ftWH5F1gzBmO1tAA_TEFCdmDVYgAHJd8eAOaAXlIZcm72RJA7kz4B6aPUsHy16Jz1EABt0kVzA0yjMzfBkFRPhKQ_2CvrHrXgpJHpjlgFQ9WQ6o2-LhZBZWuJsu9fMpXkN3KWTXCtxTNHc1Fj1vFLty1KEmbsTlCvhMyMYTa_bZVDdjl-WWMQ4UYFqP1G4Un3P6TwH8HFpCC-WaPylgpXe0AIHtvSwX6nuLkU1fM0RArJ9fW0Fp0S--iYR85Wdev3ie_1DQYsu23I9ljbZp0FPDkthqiVfFfylTHoys-2YOz692WKzFK-BQ3YcUI6kwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=SEjT_x_BAkf4Nv1cJdm9V8ftWH5F1gzBmO1tAA_TEFCdmDVYgAHJd8eAOaAXlIZcm72RJA7kz4B6aPUsHy16Jz1EABt0kVzA0yjMzfBkFRPhKQ_2CvrHrXgpJHpjlgFQ9WQ6o2-LhZBZWuJsu9fMpXkN3KWTXCtxTNHc1Fj1vFLty1KEmbsTlCvhMyMYTa_bZVDdjl-WWMQ4UYFqP1G4Un3P6TwH8HFpCC-WaPylgpXe0AIHtvSwX6nuLkU1fM0RArJ9fW0Fp0S--iYR85Wdev3ie_1DQYsu23I9ljbZp0FPDkthqiVfFfylTHoys-2YOz692WKzFK-BQ3YcUI6kwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=VeuiYPnsGXKNGK_eRb9BJNiRtJ0wE6OWJtUGfvXszU6_7Amiu4Ta8usJqkYvS8f912N9unyq_g7pwmHMZwRPnX_glBHOwu1bcHeqsazUl5g47GXVak9j8LkLOGqoOVtDmab2QgOwEOLYL0qK7VeA54huumcOubDT4vTumxDMPVXB4qdWE7K_0UkX4-MGn6hHMQFGbgi4HzwXSNvY00d2IvUy5zCt5pt8pSHgPIpdCwr0pbKQoPWzGCuC9CsIDwR58vPldBcDUYGm65m2TM01af2X2FRFvbuhyrtO-L5eEueubWxacZDxlrUNKQQImgFa5oAgFNeKnpCdjPcTnDf03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=VeuiYPnsGXKNGK_eRb9BJNiRtJ0wE6OWJtUGfvXszU6_7Amiu4Ta8usJqkYvS8f912N9unyq_g7pwmHMZwRPnX_glBHOwu1bcHeqsazUl5g47GXVak9j8LkLOGqoOVtDmab2QgOwEOLYL0qK7VeA54huumcOubDT4vTumxDMPVXB4qdWE7K_0UkX4-MGn6hHMQFGbgi4HzwXSNvY00d2IvUy5zCt5pt8pSHgPIpdCwr0pbKQoPWzGCuC9CsIDwR58vPldBcDUYGm65m2TM01af2X2FRFvbuhyrtO-L5eEueubWxacZDxlrUNKQQImgFa5oAgFNeKnpCdjPcTnDf03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZx9tSfVKBKh45juF36CKsq2IKcV4cynVfwA_IDayfLkkuPj10SdUA8qgwvLqVgBBiPIEAJVnqtUULPAFga6ze-cqkNRlxNGpDr3vPTkATWmr6G7qWZEUXrBLwB1Bi35s1yV95uwMRLoM3xLGAbrV-cMnt32xtoMmDGGJoZC2lzS0FiV7XpNmdggT5ZKvkfnzC_QapQcwE5qe-MOMzP4sVdm9nlEHVt8xX1yAb8T4gl7ZZEk7Z3poR4ld93tg3JmTyXdPXChC4FfbvUKHDKJ_rDP4fIbkemgk4lxxhJhYPNNoEzd8BgeXeboAIF71Rsppba_NzpYazIShLGLBzxjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=C_Oz-3b6LDk3INVxG4XY-hep4StAEnmqO9uhSnmQM-q3CaeH5aawUJeZy5ijcQWLatl70TwyFmR_qv93xhLI4GRJcqosFjmBBufqa_OyQsmJ02h5pA4tgNdBIGkh0Ds8MBY2alf-6T4Zg9V9gUrRJWskIBDxNu6HNB2jFiZ1un6f5zb9OEzJsDUGT4PqOimxIR_5oWTKrIF27Ug-9Y6LkMybF41y5XZd0-IeniGIzHbtya2QTJL7Gsvf_sEumrX8KKiCWeQuUg0xkp9tB_OWhqDOOzn5xWRib3Dxi2mTRk5f83omeHa4xSBAFuzSAMHUElJemroQJ-BE_tD7N810UrDZQgYMhgAttnWpnZT0UbWYF0xBXIzgtavt_lY17RDTtZnSuD_NX0Yu-x8QRbJZsfEout446I5B9R7WXa1KikEavtPJtim1w5uHBO7rfTolG2IG9oecQrUUM4VIrossbeUAdshg5IqG7IX9px2tzoMTNGx4niVf1D-QfmNpChXmPEXIXyUkWwTMHmznfDGEtiYqegl5CeYMKMkAF5LgVsAgmkiAVS63hraHC0X4CLLf9eKcbHOFT5RZJhFsgC9WzBTIijRfxACmNpow3gsyDX4Cpd9S7StezNp456SaqFeQJB6fSNNd0eahrLm5Gh4ewsvmqlTi4EeC1IPopM187Z4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=C_Oz-3b6LDk3INVxG4XY-hep4StAEnmqO9uhSnmQM-q3CaeH5aawUJeZy5ijcQWLatl70TwyFmR_qv93xhLI4GRJcqosFjmBBufqa_OyQsmJ02h5pA4tgNdBIGkh0Ds8MBY2alf-6T4Zg9V9gUrRJWskIBDxNu6HNB2jFiZ1un6f5zb9OEzJsDUGT4PqOimxIR_5oWTKrIF27Ug-9Y6LkMybF41y5XZd0-IeniGIzHbtya2QTJL7Gsvf_sEumrX8KKiCWeQuUg0xkp9tB_OWhqDOOzn5xWRib3Dxi2mTRk5f83omeHa4xSBAFuzSAMHUElJemroQJ-BE_tD7N810UrDZQgYMhgAttnWpnZT0UbWYF0xBXIzgtavt_lY17RDTtZnSuD_NX0Yu-x8QRbJZsfEout446I5B9R7WXa1KikEavtPJtim1w5uHBO7rfTolG2IG9oecQrUUM4VIrossbeUAdshg5IqG7IX9px2tzoMTNGx4niVf1D-QfmNpChXmPEXIXyUkWwTMHmznfDGEtiYqegl5CeYMKMkAF5LgVsAgmkiAVS63hraHC0X4CLLf9eKcbHOFT5RZJhFsgC9WzBTIijRfxACmNpow3gsyDX4Cpd9S7StezNp456SaqFeQJB6fSNNd0eahrLm5Gh4ewsvmqlTi4EeC1IPopM187Z4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=dA3wDLkPYnmYtFojsYP4wIDxowfUhEY5_M0OaO3dTBiKPRhSVQf4obsOSPdIJgo7VC0dUp8gQ2NOXPxnMeikA2gC5E-6TWhBVOG3WmXEMLUhNwEvdYosOBTFfOBvzDHBdz3wdsQ2Sr2BIOcgZVxMMScNdya-_2UQ6ViEvnTdSf8A-eNrh5tl8BJBd7dzTqqqPoj2ii5JKxVwIy3r4N1erGnflY_JVRB0fTlVFjom0DtTPgF8U9ucUVp1ENFJWgIgZRFeex6VaW6Kflq6ALKwYhxou0-Xb5_ST2tDGRJfhXex0a6H3VSy5u9sf2BKnfGwLvslQsKbxKtG5UwxtxfOHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=dA3wDLkPYnmYtFojsYP4wIDxowfUhEY5_M0OaO3dTBiKPRhSVQf4obsOSPdIJgo7VC0dUp8gQ2NOXPxnMeikA2gC5E-6TWhBVOG3WmXEMLUhNwEvdYosOBTFfOBvzDHBdz3wdsQ2Sr2BIOcgZVxMMScNdya-_2UQ6ViEvnTdSf8A-eNrh5tl8BJBd7dzTqqqPoj2ii5JKxVwIy3r4N1erGnflY_JVRB0fTlVFjom0DtTPgF8U9ucUVp1ENFJWgIgZRFeex6VaW6Kflq6ALKwYhxou0-Xb5_ST2tDGRJfhXex0a6H3VSy5u9sf2BKnfGwLvslQsKbxKtG5UwxtxfOHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEDi7b2uo0jDqXHwrm-bdsviNYunGLlyFNx6hsLaceZSkQFC4u20BHEMI2m8tKZBzbdnD9-kDZJE2-Q7B0CETpntRsK2NoOY3AJ_3DdPXiRmKU7_iPOICbkAEiDqJi3RL-uLi2a_VLNa5a7WMPgo2w1ypvx_m_ajUqlF10Z-pfJswTmW97UaqKYcWePMnGanG_J3LkXp9MUN3sNWYzN8hpg9Z2i5HlDP2YOAg_3_yWImo8D0UorPb6eNMTGuyPIWFlt3LrXxWhT2zfAFFs-xEk3x7_nrpQraiX1R14RqpYLjiD3A5KgKN1ZTShe2YMGnJTdvYx95HFuD3-cAAo-w3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=siq7fnxJpOOkir8w_7EeBXeTPMI2GHOdj2hErsN6ARLt__f4S_HEoQFsX07ngdR4IEBzMxX-nEhIgZdt0dRqF1Kfi4PRWFwvwczTp2DDEXilQVxAUq73k-8dMdmtFJkIyYHj3Ed-RCEo0DjRsNqvMukan-rw8yLUDhDhULRDjJr0eRu81gueh89FcL2l9vOy6WzHP5ez7m_RBXZFV_quGh9AA-sSdyc6EgjfbJhdZthVyZSBQD0qKg79cJr9aZ9lNPCKZC2Z7U-Vjh3O8FIvb48V0ZEKD97RDITvsk3md0E16GFtp3gZKpev0dhIuxcg8DPd-gaXrTF-oEozpn73KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=siq7fnxJpOOkir8w_7EeBXeTPMI2GHOdj2hErsN6ARLt__f4S_HEoQFsX07ngdR4IEBzMxX-nEhIgZdt0dRqF1Kfi4PRWFwvwczTp2DDEXilQVxAUq73k-8dMdmtFJkIyYHj3Ed-RCEo0DjRsNqvMukan-rw8yLUDhDhULRDjJr0eRu81gueh89FcL2l9vOy6WzHP5ez7m_RBXZFV_quGh9AA-sSdyc6EgjfbJhdZthVyZSBQD0qKg79cJr9aZ9lNPCKZC2Z7U-Vjh3O8FIvb48V0ZEKD97RDITvsk3md0E16GFtp3gZKpev0dhIuxcg8DPd-gaXrTF-oEozpn73KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJOCDh3Q9JBl7FUTFJKt18HyP1Bl0KPs9oJfjNImBvJLCVyXzGtFm8ilsd7_i3AYPKrTAYDJ3pudutOMRt-SSiJoIy6yJesP2m5HrPRDMokBojgMn3gQPYM5XysMcYz7xHqqCoOQdGpgtzOvFog7gpx-rqEhQFo5WYqWvqWE_APImwGM9cAIsVhMIH9URQtZw2b-p-qK4A8gkL8kgJupLyVHkROEsfuEvSpx4BT93pFbvGI_bAnLrrU7420xqHeayksCt0-koAzVixn1P9wU31KiVYKbCWpaomR0i63noPpN0YFMLSlmvp-oH3QnUKRrL4dTlvGI3ibArZ2qRYrkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmYBW61HJCUqcp0_e27Cz6w9azL8xMqqf7gI-DqXpDNu_wsUAefU_HfJCe-FgIKKYeXXxCi2qOlr8FAFvAkCvAPnGanIIVU8C73IxjYDVqSZU_PwYN6AIs3W8-W3JUaB4RnIcN8UC8KhXkdetMgA4_XNI1Mo0ri0MljMYUGKcN_MrtPVCHgbOSBk0-PSnXyxl0W_e2CBEUYwG1WW0bS9bzZRRnPYsMZkgxPyZ9v7SAXBbGPsfoLcqvPIIFGtB-BwNWUAj04Ined_aCpvMxVBiaXZB73UaX39Mi9-wtIhU2h1Bu1I1LtO2CHv40PmPkHK2fff2g7POT8BpFWSmZLXPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=tUqxzN5t7889gujkXqQUsF7Yo8trdUHPiKI2kWIrV8ZCLJYJTXaV7uscFj36TqTUjuV5cgJDUWVy5QIZb5DG_jxoeEr1yFcqwzlfSCHqoPAuxMZuzclwhBxUaCQb_y6_ac54vIwO3_ibr2-UWuxnAadHlQP-wg2u5PGOrPauGwj6beATyEQj3B9SGTh14V9i7usqVcDv4-h5brKBKsYYgGaOXYQDVh4_XGqUPUxvAM72XUwkSANgKsGrkpeCI3hrTIw8WDER6jQhw-9dfrf9kgI0CeFVMUbCGUW5SawqnMKVexFmek5ZFNBmVzh0hvlYqZdr5am5UHXkCzEgjNyt1WzeocTf9_loVW2uzvmJA6JTvZWW_MMT6xK56n1KrsybhdZMBl_uvkcW9OR3vbxpq1xn5erMZiv4TntwZgH18Hp_VO8zyvskZRfHZAe-Q4EWbPFBQ467frHA3uZ9JNYZw-ZmVP3fwIoaXs4F0_pRCxi2icr_82Gm9IY_1BxgCZfzpEfIu4XpHUi4Sf77UTPcMpG7OG3CTEZoTm9I-kH2TL7BQkEBDHYFec7VbtE9bhy0HkocACA5Tr-FWxF-xOAuS1iKGZWykp0zvbK48tup7QLasWufI-JQE1sH7WHlZ6zo9oN1SNOmKB4mKChXd2sO3a5KeFoVfzzgiUaftmFuFA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=tUqxzN5t7889gujkXqQUsF7Yo8trdUHPiKI2kWIrV8ZCLJYJTXaV7uscFj36TqTUjuV5cgJDUWVy5QIZb5DG_jxoeEr1yFcqwzlfSCHqoPAuxMZuzclwhBxUaCQb_y6_ac54vIwO3_ibr2-UWuxnAadHlQP-wg2u5PGOrPauGwj6beATyEQj3B9SGTh14V9i7usqVcDv4-h5brKBKsYYgGaOXYQDVh4_XGqUPUxvAM72XUwkSANgKsGrkpeCI3hrTIw8WDER6jQhw-9dfrf9kgI0CeFVMUbCGUW5SawqnMKVexFmek5ZFNBmVzh0hvlYqZdr5am5UHXkCzEgjNyt1WzeocTf9_loVW2uzvmJA6JTvZWW_MMT6xK56n1KrsybhdZMBl_uvkcW9OR3vbxpq1xn5erMZiv4TntwZgH18Hp_VO8zyvskZRfHZAe-Q4EWbPFBQ467frHA3uZ9JNYZw-ZmVP3fwIoaXs4F0_pRCxi2icr_82Gm9IY_1BxgCZfzpEfIu4XpHUi4Sf77UTPcMpG7OG3CTEZoTm9I-kH2TL7BQkEBDHYFec7VbtE9bhy0HkocACA5Tr-FWxF-xOAuS1iKGZWykp0zvbK48tup7QLasWufI-JQE1sH7WHlZ6zo9oN1SNOmKB4mKChXd2sO3a5KeFoVfzzgiUaftmFuFA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRAf2Z2-aumo8v3Gr0phFadNmwDN2F7qCF8Jqel_faseNTn--meIZTbyPxiB1NhVjzeo30Dfbr-hCQORICxxQJOhUdZFhUpOFdxp9mes1WDlTp1X3cOiN28N4vipgAQuOmvK8xlxe-7D12MrBds4D7VOdE1BmCPjRotiPK8piMLL6It3nGs5dJv1OHKQU30mWdobPORADbLsZIhhb9RnOW5U3865gdbd5sYmwlWylt7pHroUXbJFoyn6KdwxRBn8RXkhUrv65teb0kojnWLVEqulaaGnBAT5q51yvocJs3LQnMjgpOez2OlNTa8Avz4jhFLi1scnuuCkt2gm1w33-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffCRpyFJjxsnu-F2pUQxlJDVVVjs3HZgQOApc1h7kJjQm-gAI0DoIaHBMmNIceoWciIE0pIr4_hk2TJUYhapio7ZGAj4A8AHRWUJsHZSGcO2TyjInzZWv22BeRtGSerobLNj79Iw0kNUHratxSfPOxgPY72oo6YlDKMgjlcdKuQJJYrtWYlK5sC9_q9I5_jfnRmm7hsU79F_DkpcbvFEe-3X52X9e-NA28vFISF4nx3A9xR8KNw-WH6mt3AM-K0MCPtPY_DyxQWm9YUPZ9ySRXQEliadDowkb5X17nYidutxoIRfwkS-ucr8ut_FgwfTrnVCjdDg7KOI4wOoZJ0Pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=ITZDSSLOtQBpmaci1qAwKy1Js0n_Yg2tT1eZTbvxJwQTE0BiLBCwdJz2ATCVfFhxtmQIVv37MRRauAsCDSmypvRV8r3xWDJSLD-Bzq5Yln1XYOFrX-cEg2ei6gEWRoALA6qCeIozY384hJ0VRZuVjkxW2od1kE0NyI4GcRpUh-JxevqVS2CW6kmmLZ3PAPhTxpL8zvdjrkCybpZK4hsd0PF3HipvzuM0oRNSskAymurO0gNUcMJTExU_HHis6rCFAYaz-osUw9oWfz2YNsBu-v1Vyn_WICRGXGMTIXI6x3UYUaDUzJWryr6Q7MTEYRqZ4j_hA982fbcttL3RdGyJeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=ITZDSSLOtQBpmaci1qAwKy1Js0n_Yg2tT1eZTbvxJwQTE0BiLBCwdJz2ATCVfFhxtmQIVv37MRRauAsCDSmypvRV8r3xWDJSLD-Bzq5Yln1XYOFrX-cEg2ei6gEWRoALA6qCeIozY384hJ0VRZuVjkxW2od1kE0NyI4GcRpUh-JxevqVS2CW6kmmLZ3PAPhTxpL8zvdjrkCybpZK4hsd0PF3HipvzuM0oRNSskAymurO0gNUcMJTExU_HHis6rCFAYaz-osUw9oWfz2YNsBu-v1Vyn_WICRGXGMTIXI6x3UYUaDUzJWryr6Q7MTEYRqZ4j_hA982fbcttL3RdGyJeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=B7nydp_PbHLCD65RX_QPiaDqgct0fjM7USM0votHq7qpSverjRxAfPI97XHPxD2Z_luHtp-Ro_f1bg5Om0nlKu7wsn0BouOxtzmDrVzkIsJNoRHTf1O82cWTm7DmrLKvkRuBf9-1VbI9u7p8wGGTByIxpo_Qy8E1COUYVBxZzsCD5K9BTvMuzmt1-JwKpuxDx3A9t1uH_aj3b6kaQNkZhLAL2Qcy49oJya4wH6Gt4thaUDg-No2CZTZa7OTOdDYvNpUUVeSNARI4cobYlXADE5vLpIWwiHUsIqmf0WIkmggyc_aXof2sbyprHmfugc_HIPMZcQ1C8SAev2LUXDTHdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=B7nydp_PbHLCD65RX_QPiaDqgct0fjM7USM0votHq7qpSverjRxAfPI97XHPxD2Z_luHtp-Ro_f1bg5Om0nlKu7wsn0BouOxtzmDrVzkIsJNoRHTf1O82cWTm7DmrLKvkRuBf9-1VbI9u7p8wGGTByIxpo_Qy8E1COUYVBxZzsCD5K9BTvMuzmt1-JwKpuxDx3A9t1uH_aj3b6kaQNkZhLAL2Qcy49oJya4wH6Gt4thaUDg-No2CZTZa7OTOdDYvNpUUVeSNARI4cobYlXADE5vLpIWwiHUsIqmf0WIkmggyc_aXof2sbyprHmfugc_HIPMZcQ1C8SAev2LUXDTHdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=a1lVcfbHJOyDld5TM0CsBmwoyukcPdckKZHd7VKp9bBBbefgfozvAEwZUFOpH7fzajEYZtlqiS9jNG5VQgTYAupNTVfRTpIootv3gAs_cr2T9-_zt2BfsYoYXAvKNbpFmlxRSjchmi78ksf_TmR7VqGrsUvHYhMxVhEsnUxaNyxhSLSsOzF3gAiwGZF4qDN9VdfGBESWqgrINtfvmPAj_CQBdhS4oVHfPLn9Eb_pumgb4x_WJG3d55YjeXwvPmK6IKTJWWLY3LEBVlABSCv1JbGVdeZGiXmHwOPjUtJmOdXRQFZUTBxEQW2QClx6qFq8KumP1YdwgjorR0ZXR0BZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=a1lVcfbHJOyDld5TM0CsBmwoyukcPdckKZHd7VKp9bBBbefgfozvAEwZUFOpH7fzajEYZtlqiS9jNG5VQgTYAupNTVfRTpIootv3gAs_cr2T9-_zt2BfsYoYXAvKNbpFmlxRSjchmi78ksf_TmR7VqGrsUvHYhMxVhEsnUxaNyxhSLSsOzF3gAiwGZF4qDN9VdfGBESWqgrINtfvmPAj_CQBdhS4oVHfPLn9Eb_pumgb4x_WJG3d55YjeXwvPmK6IKTJWWLY3LEBVlABSCv1JbGVdeZGiXmHwOPjUtJmOdXRQFZUTBxEQW2QClx6qFq8KumP1YdwgjorR0ZXR0BZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdeXDakb8zYkbcOVP095eZJChk9rEQe3WdRMaQBGNkgjubDqTDgDP0k17DQNXXevwy4QWm2YoydmYkIfxjeFoIYvDEqH-jeYmhpSYk1glDejs4z7WbB4T-0DQF42BWbWOau2Qee9CeL1i0oedLh7tmmpX9LSWc3O7LbYF80GOEnH6lQ5xnFDC6V81lg2Lee66KC3dd0rr3zoU4SmAQJAGY70OA1_-knnVrLYclGXgciDKBZjpJtTxU7BfxkKpQYTNgtFDObP7H9_pwjjaoxk0FhBOjc9jJrcOJnECr46lwM2m-bBRdL_LLb22s2atjfG_0ZsUbi4eq02eDZu1KZYNg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8A3TnHuTojRp7kbflcePQ7-WeQGK4O28RVShSI7SLWibZt0f_vX9L0PV0_duA6-AjsbL3ucfZ3RyBPHUmlgm563UErBakb-InBRAGH17NvhJkKMnlkZR9WbcGYn-YojlP4x4LooXrMnR-c5H_W711HzNbRyH8OlpJE-_za_ZHmA1w3ACwIm-HtkcO6EzrQdcxJSq5DuctG9Lj1sDeeIJDbKaNdrZ-w8FnpZNuxzDcVbuFCP7tmnyDtTKpMbsohzBWTP1PkC6zwpAvum42otF3mo8gAg4e6AvDwFausE5McQxDNy3eqQV2Cr93Em7yGkTnYGADHIQV-S8yRoXTaXmKWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8A3TnHuTojRp7kbflcePQ7-WeQGK4O28RVShSI7SLWibZt0f_vX9L0PV0_duA6-AjsbL3ucfZ3RyBPHUmlgm563UErBakb-InBRAGH17NvhJkKMnlkZR9WbcGYn-YojlP4x4LooXrMnR-c5H_W711HzNbRyH8OlpJE-_za_ZHmA1w3ACwIm-HtkcO6EzrQdcxJSq5DuctG9Lj1sDeeIJDbKaNdrZ-w8FnpZNuxzDcVbuFCP7tmnyDtTKpMbsohzBWTP1PkC6zwpAvum42otF3mo8gAg4e6AvDwFausE5McQxDNy3eqQV2Cr93Em7yGkTnYGADHIQV-S8yRoXTaXmKWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=C10WZl6mC7GCR7O7dZsaQBODgdRaJM66VdoB3WDcX9NCamCk05h18XWpEmznmZOAHb-gB4ju6PvNlsFlET_2b5NoJ-7YN10gr4LKyoPF6WxUo7ZviRqF6QUcbhyIaa8Hl47NwUdwyEM5oC6R20iXN2k7cT1TZvnrmbBYUuQFw1igEM76WAzaOvPwnYyCfH-WBWgj0z4jAXJFc9EZwPQp0YBDdQeQrm9E7I-UjExklxQSKGfKAdS9KUKeamzMJ5s3rlcrhzci4GVr0ia85su2nCpAMpo7Q2MpcwV3-Fk7CdUrgKSQJ_niRbB6O896e-jxiSpxQLUAcipwCN5Ps7504g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=C10WZl6mC7GCR7O7dZsaQBODgdRaJM66VdoB3WDcX9NCamCk05h18XWpEmznmZOAHb-gB4ju6PvNlsFlET_2b5NoJ-7YN10gr4LKyoPF6WxUo7ZviRqF6QUcbhyIaa8Hl47NwUdwyEM5oC6R20iXN2k7cT1TZvnrmbBYUuQFw1igEM76WAzaOvPwnYyCfH-WBWgj0z4jAXJFc9EZwPQp0YBDdQeQrm9E7I-UjExklxQSKGfKAdS9KUKeamzMJ5s3rlcrhzci4GVr0ia85su2nCpAMpo7Q2MpcwV3-Fk7CdUrgKSQJ_niRbB6O896e-jxiSpxQLUAcipwCN5Ps7504g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCnv3S6IrsjYbV6o8MG_et7WIRILuZu2niVaY9gbkBPYrEiNSJvWzGWcrD442uLd1UwwLD1TPFnA84iXn4jsBA3MJV2LSJkpSfKrlACqpBLFoTXFza-tDdid65jUoGz2VdTCKvpZLOrhbQzR47eZHPJF3mcDWETQCmHJYP8J0dojk3Fcgl39m1yrJer-9JtXnw-hRbdfCNxqjzX-84GpQhl9-8NE2qvtahuWi6u8q2moloqxbxexH4ED917DTjW9UGGDUgQ0hjOo_wNMLjtPWdLQqCHbBthfXiRtNygoPgqyLvuQ5iiLCbWbj5et5UHLhdV5kTkNq1DEv6u-VtexYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=dnkCvRtMcxR3HJeVWA0IFmDxD3Em--CXmVA-0aCAHC5GPN58ClFeo2PGE1yT1xxA3n3_VmtpZiq2UYFztGU1RB18pMlrujOj7PC4vQWmUcOu0AZVpeFV9_n89FTw1P-facDgwfaX2xgbe7Qvpd27fO9EI-FAAxh-ADuNJA7jEo_06eJVfHyZ6cdIZjNnVIt1bhI74wk6-TgM145UAZxZk_BEoDeh6QPkCdoFyIfGWyL_I6FusFcSNIxq5jW2daMVHumm_8UN-ELKQRHpOJgWb1--n748RGn4VrWGM12iS_mMfDHQN-kt_T1TPRfQFRzqJbmIcsaqR-G1Cjr_B7mgOKyXrQ8ci8nwnVzP06THkcfYo8FH2tJGzrP5umiRx7ZrpcLNppLJvVEpoQStMdvj05kc0voTpVUGSasRMlIT-VxRtQ0ZFJZ7dwO4ycLJWQjZZcpNKBySV2LyoKOc80clBOmPEX5Xz7OXXI1X6NUil3mOWLW5cpPHGED2Eae4kvdie0A-k0rdRbQwIsXH6gAT-rRAMIaBOjEbPVZTPyteC9I08XwE79kJvcvg6C0HS2vuXwjGLiFvL562qvPGeJ9O1f3EtFWcH1_rPg8iPaflLIHeWvfYIN4sC2zNFRbMzyKfQk8UbVzASmTDmuxRNFlRRTm5GAnI8G6Nm9QAnQxAMyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=dnkCvRtMcxR3HJeVWA0IFmDxD3Em--CXmVA-0aCAHC5GPN58ClFeo2PGE1yT1xxA3n3_VmtpZiq2UYFztGU1RB18pMlrujOj7PC4vQWmUcOu0AZVpeFV9_n89FTw1P-facDgwfaX2xgbe7Qvpd27fO9EI-FAAxh-ADuNJA7jEo_06eJVfHyZ6cdIZjNnVIt1bhI74wk6-TgM145UAZxZk_BEoDeh6QPkCdoFyIfGWyL_I6FusFcSNIxq5jW2daMVHumm_8UN-ELKQRHpOJgWb1--n748RGn4VrWGM12iS_mMfDHQN-kt_T1TPRfQFRzqJbmIcsaqR-G1Cjr_B7mgOKyXrQ8ci8nwnVzP06THkcfYo8FH2tJGzrP5umiRx7ZrpcLNppLJvVEpoQStMdvj05kc0voTpVUGSasRMlIT-VxRtQ0ZFJZ7dwO4ycLJWQjZZcpNKBySV2LyoKOc80clBOmPEX5Xz7OXXI1X6NUil3mOWLW5cpPHGED2Eae4kvdie0A-k0rdRbQwIsXH6gAT-rRAMIaBOjEbPVZTPyteC9I08XwE79kJvcvg6C0HS2vuXwjGLiFvL562qvPGeJ9O1f3EtFWcH1_rPg8iPaflLIHeWvfYIN4sC2zNFRbMzyKfQk8UbVzASmTDmuxRNFlRRTm5GAnI8G6Nm9QAnQxAMyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITBlfOB51FvNNFYOJfQuGl87G5EVuzjwddXZqCjF4BbpEvDX2IS3r9qK3uOJM63lGk4LRtfINpZPAW8rzFkYkTXCnMcuh0NWolR2gHZocVmyPNbo5bkpEFY4KSO0gfrPDjAYNWSVjAUG3efQ6M73iDe1xuuqE6cuzXtXNt_EkCOMhNIWimqIwuNlfcnhR-tVcmoUUhqLkL3udbCF3sESQHFFBWxYGfji_1wSV3gnf1jegWS8Gf5s86189Ea_FK2KUImfHXYdVCQXhbxUHPEE_kGtMyPKmhUFqpZQ7rBUpA0ymGlKNVkJA6Oheoiaj9-ra5jL0r15RaInfX6AG7cX_g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=e2X485LhsYnNMykHSwAKT8nS9CPlSADWfdnw1b4ztBcGCih2Y023GtAsq-46O2D_J1_rVT02653LFPeSpbVgzDJmfPuyHzBYmbWj5cY7xNl2heyjfyt4jw1TNi1LZs93lIYc4VLpOvOc7IEKthlRbPcDnrdFoRiJKrqxDoRqNp8V-nX71DHhQ-SBA4YJNyQABV8DIa6ADt90ilnOxf1-pItK3L3D0zipMO7wDSz7fpX3wF9IRKuzDF8d1MunPos77fuCj2ECvvqWeb2woJwcTXjYR-KUJgz4et8Su97bwKWkh1g52g9gV0IXZFy2pXcxm_h8BPCY22x8a2OT_9J1ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=e2X485LhsYnNMykHSwAKT8nS9CPlSADWfdnw1b4ztBcGCih2Y023GtAsq-46O2D_J1_rVT02653LFPeSpbVgzDJmfPuyHzBYmbWj5cY7xNl2heyjfyt4jw1TNi1LZs93lIYc4VLpOvOc7IEKthlRbPcDnrdFoRiJKrqxDoRqNp8V-nX71DHhQ-SBA4YJNyQABV8DIa6ADt90ilnOxf1-pItK3L3D0zipMO7wDSz7fpX3wF9IRKuzDF8d1MunPos77fuCj2ECvvqWeb2woJwcTXjYR-KUJgz4et8Su97bwKWkh1g52g9gV0IXZFy2pXcxm_h8BPCY22x8a2OT_9J1ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtIxEOauOkOlVih6oc7-K2yj6kkySU8j1dl91Kon5AWfPWMGk4fgneOJtFG9uI8lLr_c-M8Gp0CYONIVfRWOrwgv2iqruNZMl7G3936Hq_qTtKRxq0mA2X1QBkTO-NzlOJRdkm2pdoqWDTcM9b6cE1fM9So-b0kTknYRoBYU7vj4hq3CDkPSFCecvEGIJQMaaMmtQP4-xi1A8tPEoh8EHUnKvJV383LozbzOkdC8nPP75WX2fvkQXAkmp1zo1SVTxNJck8MrZZ1tU80DyPOGxjASwsbgDymKoCHaRgxiUjV9QOq_UbsxJxV9PuXMgAfSG-srn932V54VacTHtYu8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnB_fEIUAw-Q65AOIWlaCjdmN1-HN4yxTfB-aVRM3G4rxro3oDmTlMHfDxlqZHWytl4ZlSzG7IdYjJHEO0pMp75Lb74Iocy2jcn89WEZL34Bad_MSBLTAS1OZWNgPovgatN5EvJHxEeqS8PSeeWtlp3e47voTxUqJaHBqIEyXIWQ4KfLf-VQA9AvACriGBIpO8BIMkfjypca1yRIw7_-Ot0D0cjvobirF3LiRFZrm-3vsW_MhzhcJdoZw74fnPaYjFR_RtBQ4lIpUFHnfsjlJoXI0yQ11dfp5Bv2-tVaiqq6bGN7bGxwPNEsxBWL7vHOzHMKZxs_57s8YiNDBYBfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQFA8R-u6zzOgzzq9GfooR2Ap_AzNrxxyB762XfDxwhvd9-GJhOxlfh6T4UNSKUVSY6Th9UCLNhhjYlA2jgIoPS2HGTVcfahTnjL64DuvgB17eEwQ_gZh6QTtr8uCFjq0VjyWhrQQWWG3VduEkUbtUb8aJrB4CAWfblhBt16_I8DlH3CEHlzZMDdPJdbWXYIGIoEjg0FpgBiCtbtF0q493Ekp81mGKqzYx3P2I44HjDSdVehP61iWGLnT2MGmxTOm8KEENHfGKfmaqQL9wNWUcEiCG-miq1BS5Fco03cbp2vaYl24LEix0XA8n1Iyw2gSWqJBH5Jrd0n-w93fp-AFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=AjtqoWuQNhOWcGlV5A9HMtXRuhcS5ALB8G0oG3kfiTqhnEYNDARPgMM_fq232QmJrBjZAQkS0Q2N60-ITtwf9awyJy5FxCCmUzErlKsybO8ZiELN7wAPW7kZSbOgfTK8fI5TEV2DeQaqL9SDut3yh45cKSwqmkeeuwooVB3X7rrm8GREtIISIuqFFP5t0bxw8Bh4FVPsmcj8KfJ1xjmVLVQ64ormIgbJBwh_3SGs18EVQrwRU_BKWxpkxf7iRWYYYw-AMzMBv3kbdjggyYcxzVuo_Dul9RjSbA__Qe-CN3lTiazaSzn17AKgBq4t6DaZjNj8NBIjWWpb50QMf80cUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=AjtqoWuQNhOWcGlV5A9HMtXRuhcS5ALB8G0oG3kfiTqhnEYNDARPgMM_fq232QmJrBjZAQkS0Q2N60-ITtwf9awyJy5FxCCmUzErlKsybO8ZiELN7wAPW7kZSbOgfTK8fI5TEV2DeQaqL9SDut3yh45cKSwqmkeeuwooVB3X7rrm8GREtIISIuqFFP5t0bxw8Bh4FVPsmcj8KfJ1xjmVLVQ64ormIgbJBwh_3SGs18EVQrwRU_BKWxpkxf7iRWYYYw-AMzMBv3kbdjggyYcxzVuo_Dul9RjSbA__Qe-CN3lTiazaSzn17AKgBq4t6DaZjNj8NBIjWWpb50QMf80cUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVDBFH4UXxgmOA65din-fwnSLOYRl8QXlBjMNIJnRftbeKJjNhAnltLh_6jJ4DGM2PA0ClmvFKSg2wgEeDgOEsK6xvyPyM3bl8ikNMZ5HIG2AzpK2XwGCiwZptkXAHsr5zjMFtNxTdn2zCTaTilFuvKjTM8LQsp2zf1TWI6DrFQxtOMqSUyuq-fh93emx1i96xQe3O5jE4Ql288QjM3O6LWSX9LhuuKQOp76g4t1SObw8yKWow_9n1z2b1Y6scnXgbf-Cf3dFymbcSKYvLiG0h4QmhByMcBW92oILstPK_A1wan7xYU565VbItaFwXC5Bgu2GeYOrVC_FQ2bkYcYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu03RhccS51oGBHvLATvow0aRLdTkIpz10fIEEsJ7ethCQkkntYXots8ud70-zUoPkO-VNb94guFMC4m1mRj9gazq4cIcmtXaPuQ_WC59CjXUUa89VNqkpReSilJg0Lr_SKdVpTdp_2RO4fQXzttYEx2WXhB1cMCkv-JnIHjmj2ZxxRJ8ptlVthdMFL_FHccYHU8nYIWFAxKpbeIn3n1oM3HGW4kylv_Wv_WrhX8eDLdbO15oAHLcziDntvhfr6wTkbQAKyBEK4EF_Z__Z3HXL3rAKh4frc1oaGJPWf3SUYx96qIVMNPqzURQUW1fALm4xokky6YkIyADnwDiLRi-Dgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu03RhccS51oGBHvLATvow0aRLdTkIpz10fIEEsJ7ethCQkkntYXots8ud70-zUoPkO-VNb94guFMC4m1mRj9gazq4cIcmtXaPuQ_WC59CjXUUa89VNqkpReSilJg0Lr_SKdVpTdp_2RO4fQXzttYEx2WXhB1cMCkv-JnIHjmj2ZxxRJ8ptlVthdMFL_FHccYHU8nYIWFAxKpbeIn3n1oM3HGW4kylv_Wv_WrhX8eDLdbO15oAHLcziDntvhfr6wTkbQAKyBEK4EF_Z__Z3HXL3rAKh4frc1oaGJPWf3SUYx96qIVMNPqzURQUW1fALm4xokky6YkIyADnwDiLRi-Dgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=rMb871uQvCJl-S_HeyeTMDifPpVjszkLnfTM9Pyn3jkU1aio2ielRZplUZ4GMEzbBYX2-LNJ4f_ykQCr51Vl6JA75XQkcbv1zy9TUrUlhdVrkdJcisYuki0z1_GOqYwVjt2KcPQkCoCw6nGN9_wCKcIqemkXGtPpdXYOYv1-t6lz-J9LkrtiTgfwX2aasrTn3DpQl9mCk6Xms_yTodfA-lLPWZAdvn3fqKHQ00U6u_PGL_yyevOS-u3cjcS9I276bZ9WaIEkqvXnfDvwitLxtKQAfg54edytK9mZdD-z9Uw1vJnJ6873uUU3bZ969JPUFi3CxWEw53X4lqAQ_LhyWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=rMb871uQvCJl-S_HeyeTMDifPpVjszkLnfTM9Pyn3jkU1aio2ielRZplUZ4GMEzbBYX2-LNJ4f_ykQCr51Vl6JA75XQkcbv1zy9TUrUlhdVrkdJcisYuki0z1_GOqYwVjt2KcPQkCoCw6nGN9_wCKcIqemkXGtPpdXYOYv1-t6lz-J9LkrtiTgfwX2aasrTn3DpQl9mCk6Xms_yTodfA-lLPWZAdvn3fqKHQ00U6u_PGL_yyevOS-u3cjcS9I276bZ9WaIEkqvXnfDvwitLxtKQAfg54edytK9mZdD-z9Uw1vJnJ6873uUU3bZ969JPUFi3CxWEw53X4lqAQ_LhyWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=JrBdg-RgZD-VmNbE2lzdaV8Hon8E3arocg2ZmDsfXxqJOk80SfV5rl9XFjUBQeIJW1LZWYTvnr7aL47xzBfgd-C4YzSrwrLPoU6oalWCKsEgjhWE99mY2WkAM5IrTmx5W1dDhxP-vKAnlXkGIdkwr0jtDOB1umo4iq9RQh1Zol59nMgaz3UQ7O0IeWJ6nNucS_MWlgI95_Bn7t8OhyZ06K9k75CVa8EEAq0s2qzPsD3G_snzvvZ-AFaV5kx4tthf0xzpXC1tjLqey9jKhN11_7CAHWsFrXojYKLq6-G5b_Gkyc3BG8EbIX8PWmMukxasdgtdSt2rVgKzGXQY_58PMGqU7BezNNrDoeD9o3JFHqHOXFDrtvEzFy60IrkolCGNA6hgONNfDmz86yegh4B-PxitxvNtMid7qIdQVl_PKdT9xVXVRRgjown6QY-6Iz6URlI2NVEzFEWkF_An_tbG_LpHRjxZp1V2L84YSlwslOru0D4yKKKfZ7B6DdRnFgSiI-9SBWvQjYzELHnmSsDEDVgmPjn55EefBNP82IFimRBOStw6ccm0NAclRDTP9XUjxsn2JOXGgGTQUhKKBayUVFtHpGyvHgMNrpKOtCUAL4Qn5mmB_MdDCs_1xKLCg1SfdNxTvhfxW6mS9EGCCUAZgV2L5LtGuKebll6qPbPxTRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=JrBdg-RgZD-VmNbE2lzdaV8Hon8E3arocg2ZmDsfXxqJOk80SfV5rl9XFjUBQeIJW1LZWYTvnr7aL47xzBfgd-C4YzSrwrLPoU6oalWCKsEgjhWE99mY2WkAM5IrTmx5W1dDhxP-vKAnlXkGIdkwr0jtDOB1umo4iq9RQh1Zol59nMgaz3UQ7O0IeWJ6nNucS_MWlgI95_Bn7t8OhyZ06K9k75CVa8EEAq0s2qzPsD3G_snzvvZ-AFaV5kx4tthf0xzpXC1tjLqey9jKhN11_7CAHWsFrXojYKLq6-G5b_Gkyc3BG8EbIX8PWmMukxasdgtdSt2rVgKzGXQY_58PMGqU7BezNNrDoeD9o3JFHqHOXFDrtvEzFy60IrkolCGNA6hgONNfDmz86yegh4B-PxitxvNtMid7qIdQVl_PKdT9xVXVRRgjown6QY-6Iz6URlI2NVEzFEWkF_An_tbG_LpHRjxZp1V2L84YSlwslOru0D4yKKKfZ7B6DdRnFgSiI-9SBWvQjYzELHnmSsDEDVgmPjn55EefBNP82IFimRBOStw6ccm0NAclRDTP9XUjxsn2JOXGgGTQUhKKBayUVFtHpGyvHgMNrpKOtCUAL4Qn5mmB_MdDCs_1xKLCg1SfdNxTvhfxW6mS9EGCCUAZgV2L5LtGuKebll6qPbPxTRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Em33tI26ZZdLNkXnNnyeexmHybYiF_oz8nJ8JKeSelhUg89TZRVe4shT5YpVVD-IRDEfExYhqmXtunkZ3auqU6STDx59OLh9zm0SyI7M_UuIdETO_D2YDe_E35Hw_Pea5aO0qz6DahJJWULaQcgsVSYePaHZrzkSLNUt2tV2G-j4LhrWfGoIWI2FGFmVflIomsXeD6dFEbtwEavi5Msjf0DpeTq7ShJuqjhANuPv6oo6sD80R9pe6x5s8WiiwYvLMg8Ue_tRCT48Rsjsn1nZDUH-TvQUOi4Tbw2v0gJNbDIfyM-ZOQBmzcj-l6i0AxgsJKpkafLk-fLSS78LG7XWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Em33tI26ZZdLNkXnNnyeexmHybYiF_oz8nJ8JKeSelhUg89TZRVe4shT5YpVVD-IRDEfExYhqmXtunkZ3auqU6STDx59OLh9zm0SyI7M_UuIdETO_D2YDe_E35Hw_Pea5aO0qz6DahJJWULaQcgsVSYePaHZrzkSLNUt2tV2G-j4LhrWfGoIWI2FGFmVflIomsXeD6dFEbtwEavi5Msjf0DpeTq7ShJuqjhANuPv6oo6sD80R9pe6x5s8WiiwYvLMg8Ue_tRCT48Rsjsn1nZDUH-TvQUOi4Tbw2v0gJNbDIfyM-ZOQBmzcj-l6i0AxgsJKpkafLk-fLSS78LG7XWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m89Jve8-CZpUUeWD73AL2BsFmZ0soxjQbuQD3XB9nH67tDKVSayKDtvMVZiQFIkeNkHfkQsjiLpIVGNSoURN6hcrKJLllnyoUgSM0CiavLYdhDHSYpcYGOxbfGIDYNvnEYCYvp_38Qq0tn9RvM6eqW6UFTvo0-yo6JXAlsISgLOeVZWBSkhXT847crESR0R0zRV4DmSVyLuZN8yLdwcywCj6s7vTu61x10-U1nW6x08tQ9DL3ff_nGGYhPaayJV1j5PyQQ75KI2nWUuLjCU_RPSu1EoE6rfwt7cVTutmOcgmQjEpkqAX-gAqz9rdbMeT3FNGaEpQsuc5S4AAeCgoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=QkvIIimWL416JBafZ0tUsQ4eq7CneHbo8gd_tyaFckvI6Yr05f0aTlEHQWjaFSPSLi1t-vxol8m3po-jkOv5dPo5XUJJ2pX6HtHSkL3RUL30mD8Ke5ekr6SBZ-Dlm0We8G8eNm7gFBKzXKBuidwq8GfcDYKrNzhHsRmZwfCqf_a8aZ-ROAw4KOth3jaYiso5kzYZlcV3yXjPg6cvunXGL42V0oUjrKoHpep6MlbONAXztmSOgXibCISV4NObrScfrb6jtPDE9_H_ZAwKjkmc7atwYEFvp0f4xd1X1EaGxDAAJNo-HIRg92HPlH37ZpQ8o0tcv3uxM1ggXBqhNEkP1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=QkvIIimWL416JBafZ0tUsQ4eq7CneHbo8gd_tyaFckvI6Yr05f0aTlEHQWjaFSPSLi1t-vxol8m3po-jkOv5dPo5XUJJ2pX6HtHSkL3RUL30mD8Ke5ekr6SBZ-Dlm0We8G8eNm7gFBKzXKBuidwq8GfcDYKrNzhHsRmZwfCqf_a8aZ-ROAw4KOth3jaYiso5kzYZlcV3yXjPg6cvunXGL42V0oUjrKoHpep6MlbONAXztmSOgXibCISV4NObrScfrb6jtPDE9_H_ZAwKjkmc7atwYEFvp0f4xd1X1EaGxDAAJNo-HIRg92HPlH37ZpQ8o0tcv3uxM1ggXBqhNEkP1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=tD6TzQdqHr3PU-PVM4-_3DE25Iaa8kWQZVxaonFLQD3gWV0Zstpb6VmVYntDEPBfq-9IV5MeosHstn7PiENXKOwmt9JAA1w42wYVog5-QxRKG77t7YUjcnK1VAaTA5OwHa1MRgIOY80brJRGhzNq2lhIzkmMIeEE9MWCFvJyOWr7ZKzhVs2mHQ4iJNkxmMA4mgjI-_uThkAvMk_fv-QOT6r_lee57MtfT237Qm4rKBM1MzlwhO3QvrpyISFVzYqJOQcwOfiU-p3cEqemrMi6aeBWtzK2RF6_3kzfVSLxbdGJae1exzsSlZ9M2SiGCvlOr3Evjx7ta95E_kAv4naD22aeDT459hhfZAP5OgUVdDCyl6aNNMLp8V6Sa_sSF-kE0-_VolBovcjmiQQhVOHsJkIeg_UtzbpbOdsixJQlVXEOU6cann_9P9cyyqqitp797AZFqlpAUPktgxNI738s1Fjsc9ud1KkfTxCztq8BkUfvSm4cAZ_HfpjKKbL0u9oM2sdak8o9XgZI12nY7niIt_8048AqE9vkfsmgInRKHgbbISZSiWq0zx6zKxqGe0ugSuweYrgVBPWUu10HIY9VToESmTIK280JaMMK3MuTpjlYyosfbAcV2NP97Wo3adMwJMr0Us9RZKvwWqOa5jN0y8fkhIEDQBSb60WTqBaCS2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=tD6TzQdqHr3PU-PVM4-_3DE25Iaa8kWQZVxaonFLQD3gWV0Zstpb6VmVYntDEPBfq-9IV5MeosHstn7PiENXKOwmt9JAA1w42wYVog5-QxRKG77t7YUjcnK1VAaTA5OwHa1MRgIOY80brJRGhzNq2lhIzkmMIeEE9MWCFvJyOWr7ZKzhVs2mHQ4iJNkxmMA4mgjI-_uThkAvMk_fv-QOT6r_lee57MtfT237Qm4rKBM1MzlwhO3QvrpyISFVzYqJOQcwOfiU-p3cEqemrMi6aeBWtzK2RF6_3kzfVSLxbdGJae1exzsSlZ9M2SiGCvlOr3Evjx7ta95E_kAv4naD22aeDT459hhfZAP5OgUVdDCyl6aNNMLp8V6Sa_sSF-kE0-_VolBovcjmiQQhVOHsJkIeg_UtzbpbOdsixJQlVXEOU6cann_9P9cyyqqitp797AZFqlpAUPktgxNI738s1Fjsc9ud1KkfTxCztq8BkUfvSm4cAZ_HfpjKKbL0u9oM2sdak8o9XgZI12nY7niIt_8048AqE9vkfsmgInRKHgbbISZSiWq0zx6zKxqGe0ugSuweYrgVBPWUu10HIY9VToESmTIK280JaMMK3MuTpjlYyosfbAcV2NP97Wo3adMwJMr0Us9RZKvwWqOa5jN0y8fkhIEDQBSb60WTqBaCS2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TprX3OnrLGZtEye7rXGUDu7PJwb5jrZEb810GHSwW-vwxgEsVPz_Ehnm2LjOjJjpllgSqTMR-xTe1VENFy1AIbkM3rBEb5pAENWtEYy8wJUGNLl35gGsfgbZGkmFE6JiMDgBYdnGWozjr5ochD6_UhMHg044EF6_Ibf3htTTQgnZ3OhG8aoS3m5uPpxXJTJVQodJWiAaH9R3qyR6xOUW8ovY_9edBS0JFBJolNfVnfd-J4lISrwl0VjEUSqp9ldHdhpre6x8NcZncvoJrf6iGFNhBZ2yzx31RV0__qq2qeSzpOw6oxRWZrZkL-uXRWo14kJ6cu4NXnTU469sUAW5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=MYn-pr_sP-6kX88q20db0ubcfsCpu873gTKqTYoAkBFbsdjCDFtmgp_Gqepu5uiqVKExPp-R3UVSm2zqYbf-NiNRopTh48z7l6cktc9ws8hOaNW3ygb-1MKnQFQM7hMLMUMsVoji6DXDd50oMr-PbzV5pSi2Nz2RefiHEfkycDPJfxM-sLgXXebGVx0m4G_larVhu3HTE15_-xPmDj4N5q2R8ts1HNOf5g5ECiKfDezoOT_XzoNWp1o9cYNbZ87w1GOmcPrDbb0ZjSf1pkapUS0AgTgN4znBJAeQG_rXzsPxctN9_s-mG3IsxDwuc7ETwvEFzaqgFElYpA1hg0MB6n9smA3jKAVK2V23n2SYGBYE4qtFQoRVF_6WTicz5hnkhkYHyLIuJ8YhrPONE-dyGGYcQZu3dQtKQw8icz_xxv2zNifloU0Lv6y5USXt2yG15cAJJBvQ-UFqbhyxYPZtshUcc1qBNmpNty6Jcwscx22P0Fv0tbCJK3DWVGi5dF2DgOR4SZudZ59UCKmVC9JZuzw5vCI2Wf4lBlyL30QqaJtOK3AqiFiNmd04UZFb2VOsvWInAf-C8EE4bAb17V-QgLGB01mU1wayBaAhwBXarzSoNF1YwFmy3Vg3Lh64fJfcmIU-U0v4Aym5MVbFRYAiEwcmt5da4Yioe5KVZ6bt5no" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=MYn-pr_sP-6kX88q20db0ubcfsCpu873gTKqTYoAkBFbsdjCDFtmgp_Gqepu5uiqVKExPp-R3UVSm2zqYbf-NiNRopTh48z7l6cktc9ws8hOaNW3ygb-1MKnQFQM7hMLMUMsVoji6DXDd50oMr-PbzV5pSi2Nz2RefiHEfkycDPJfxM-sLgXXebGVx0m4G_larVhu3HTE15_-xPmDj4N5q2R8ts1HNOf5g5ECiKfDezoOT_XzoNWp1o9cYNbZ87w1GOmcPrDbb0ZjSf1pkapUS0AgTgN4znBJAeQG_rXzsPxctN9_s-mG3IsxDwuc7ETwvEFzaqgFElYpA1hg0MB6n9smA3jKAVK2V23n2SYGBYE4qtFQoRVF_6WTicz5hnkhkYHyLIuJ8YhrPONE-dyGGYcQZu3dQtKQw8icz_xxv2zNifloU0Lv6y5USXt2yG15cAJJBvQ-UFqbhyxYPZtshUcc1qBNmpNty6Jcwscx22P0Fv0tbCJK3DWVGi5dF2DgOR4SZudZ59UCKmVC9JZuzw5vCI2Wf4lBlyL30QqaJtOK3AqiFiNmd04UZFb2VOsvWInAf-C8EE4bAb17V-QgLGB01mU1wayBaAhwBXarzSoNF1YwFmy3Vg3Lh64fJfcmIU-U0v4Aym5MVbFRYAiEwcmt5da4Yioe5KVZ6bt5no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=PrEvLZTKzBhPb1QNNMnZG5-jbpXYPQJklksXiT_aCqZrAtyLwJtPtBhecRJEnR-4ZaxWXrINeu4hcK2wvjk1MLSMkkqfKWgvg4xSpxw9Dc67Lkr7EFobAhOuos3pjQS1H-4rVQhxGVXCsI9DEi_GkaMQ4aF86u1W7jBlFK7YN_YPFcajX2EyIHtzsq-JVmrL42R8VoxzjyyFWF4YiYn3Hm8GXMY9UmjHOqaeQ-K10kDcqliiyIHzrsC_tGhZ9ay_LzWe2pfgCqbCP-JM6VCBwKM6pJ6-7DwOiRA82wOAppL3IJgjUo1dNyCXtFxZvbW-hpbDt_T4OFcyJzsB2LcC518f9_EXihcLzDnVMZW0GLMiBSSTRPFKEXXoBGG8_fiIwU6gbhYtcEv7PFd9dzN6e_XipDJkL4f38NlmmW11869eSAxDHFOSCe0t5P63DoQ1G2gHIE2iv81ex4w_p5fc6swOLl1lZHlhFALIlNCplyJKR9k8lyqriC7ivs9cY8uXY3gp_u_jokCBLyuZh9pMzhF03kcaFxGXbfDcJ4eRZ6bLQdaSqBRXevMrhNahDNevnBtjO_OTKtEQejeiVOUKFbFYIptNJrNdsOTSP5lqJiaNJFdS0p02Icq7QrKCPqrIj7B0Qs-dCS-AYr_WVNdrUrBn_KEVOS8XwmEXus3SO3o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=PrEvLZTKzBhPb1QNNMnZG5-jbpXYPQJklksXiT_aCqZrAtyLwJtPtBhecRJEnR-4ZaxWXrINeu4hcK2wvjk1MLSMkkqfKWgvg4xSpxw9Dc67Lkr7EFobAhOuos3pjQS1H-4rVQhxGVXCsI9DEi_GkaMQ4aF86u1W7jBlFK7YN_YPFcajX2EyIHtzsq-JVmrL42R8VoxzjyyFWF4YiYn3Hm8GXMY9UmjHOqaeQ-K10kDcqliiyIHzrsC_tGhZ9ay_LzWe2pfgCqbCP-JM6VCBwKM6pJ6-7DwOiRA82wOAppL3IJgjUo1dNyCXtFxZvbW-hpbDt_T4OFcyJzsB2LcC518f9_EXihcLzDnVMZW0GLMiBSSTRPFKEXXoBGG8_fiIwU6gbhYtcEv7PFd9dzN6e_XipDJkL4f38NlmmW11869eSAxDHFOSCe0t5P63DoQ1G2gHIE2iv81ex4w_p5fc6swOLl1lZHlhFALIlNCplyJKR9k8lyqriC7ivs9cY8uXY3gp_u_jokCBLyuZh9pMzhF03kcaFxGXbfDcJ4eRZ6bLQdaSqBRXevMrhNahDNevnBtjO_OTKtEQejeiVOUKFbFYIptNJrNdsOTSP5lqJiaNJFdS0p02Icq7QrKCPqrIj7B0Qs-dCS-AYr_WVNdrUrBn_KEVOS8XwmEXus3SO3o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=J_dUviofnDFVtCkC5ZKpZWvAVC7112Aut_o9vf1R51L2dkecX_A77nvcSuawpieBr0ZlvUxCxVs8fZkk392iyaWHqQbUNZKO8vndCwMB4jSpZ_fMUKC2MVGO9dzftRqotvGpVdJnoBmuII64DCC2EbPeEeBiIkNCkZhde953YUtFX9TUyXSZvmOwcqlMOnPsmtkHrXpnrUfhmwawkthjIwEBD83vSpd9VviJMGhHjjgGwHpqgtov3sWodLKyWm2Jh5fKPN3FWq8d3EonCNSTKaB9a7CmbVe2gcWDdc_Gp-EahVpOdP1vPsWVCATduj8RBNSSR1scWyzscOItVYukXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=J_dUviofnDFVtCkC5ZKpZWvAVC7112Aut_o9vf1R51L2dkecX_A77nvcSuawpieBr0ZlvUxCxVs8fZkk392iyaWHqQbUNZKO8vndCwMB4jSpZ_fMUKC2MVGO9dzftRqotvGpVdJnoBmuII64DCC2EbPeEeBiIkNCkZhde953YUtFX9TUyXSZvmOwcqlMOnPsmtkHrXpnrUfhmwawkthjIwEBD83vSpd9VviJMGhHjjgGwHpqgtov3sWodLKyWm2Jh5fKPN3FWq8d3EonCNSTKaB9a7CmbVe2gcWDdc_Gp-EahVpOdP1vPsWVCATduj8RBNSSR1scWyzscOItVYukXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=dUC2tB4Ue5rRDX19CPHhEjfVJeX9SAqtJny-2aQ7SfCBNSrXwUDQNzuV7R71wA_sI3pPle7VvvgJwg3zGN0Hmt6jObhp8cxkNJe3QfyYOVYnLX7gHH21vms2jKXX_UtKFq-3dnMi4JdMgtjQGeZST6Uetos3k-9uG8_jn1Rz7GW6JY0X-PsKSQafLABUoz-_aEk7Oj4eRKOv2H-8DXCKjmUvJnMgvQZsHb-5_6oMwtL0x1YAYHiz0-DN3bsrdFexAhUfhWhndgAo_WZpWlBwo_fSLdIm049t56-NTOpK1hqO8hj1vFLTTSY1Y4rnubdcFmv_EwOQVEIZOh6zXSLU_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=dUC2tB4Ue5rRDX19CPHhEjfVJeX9SAqtJny-2aQ7SfCBNSrXwUDQNzuV7R71wA_sI3pPle7VvvgJwg3zGN0Hmt6jObhp8cxkNJe3QfyYOVYnLX7gHH21vms2jKXX_UtKFq-3dnMi4JdMgtjQGeZST6Uetos3k-9uG8_jn1Rz7GW6JY0X-PsKSQafLABUoz-_aEk7Oj4eRKOv2H-8DXCKjmUvJnMgvQZsHb-5_6oMwtL0x1YAYHiz0-DN3bsrdFexAhUfhWhndgAo_WZpWlBwo_fSLdIm049t56-NTOpK1hqO8hj1vFLTTSY1Y4rnubdcFmv_EwOQVEIZOh6zXSLU_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TQZlChILxaKVqbqWeRAQ6OwgOiAQeGhHO-RY3-XEYeEmTy5FycjpZZwKw7w7xVWnIQcv5CyIOpDfzMGXP_OyRlOOh_3NHklagG4WoJ0nNz6asjSY_3ydFD2wAUjVtMZjnsCXsJdq6A7taK_6Uu5da738bikIbROl9bQrn5MWIfwVxbZS-ZbDBkXmcGM1CTh8vWGnlFP5LFH06m9kSOJw0w_A1JTtM6UhnmUda8cOFhUAq7_EJBybZMRQYJBqOAA3-FXgDNeMHpsUymYyjzTBv8mG6MqYoX6wwShrFjMVpQZKKBsegx8yli_TdODNGpyvvD4LPqJxoPqSiODEigWNrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=TQZlChILxaKVqbqWeRAQ6OwgOiAQeGhHO-RY3-XEYeEmTy5FycjpZZwKw7w7xVWnIQcv5CyIOpDfzMGXP_OyRlOOh_3NHklagG4WoJ0nNz6asjSY_3ydFD2wAUjVtMZjnsCXsJdq6A7taK_6Uu5da738bikIbROl9bQrn5MWIfwVxbZS-ZbDBkXmcGM1CTh8vWGnlFP5LFH06m9kSOJw0w_A1JTtM6UhnmUda8cOFhUAq7_EJBybZMRQYJBqOAA3-FXgDNeMHpsUymYyjzTBv8mG6MqYoX6wwShrFjMVpQZKKBsegx8yli_TdODNGpyvvD4LPqJxoPqSiODEigWNrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Z4DC3k0KnbYUMOc9G-zprBD5tEFKpNpi7kB-rpSuROV_0VC6YfYvj-qH5GWuETrSG-wvBSaFlbJJAsinNhev74CdjUsz8Yk3XIoGrbxBSgyo3ZD8G0vuMQnQ9iVuf0rUFGiUZoj9P2Es9SC6o7wYpSXAhHQQLQURRo6rUIt461b_YZv02lGKToc4R3ssrntH6w6xKeo1i8G0zIb7yqbrq1eoFWdsxt5huggAdnvd0M9k-7-CrnLraRJ1xHM9esu5F5utfr9PLCXBPd76Q5Xmg61OhLfjyoQZBsXc_iawazrCFGzUtykoUKvujC_YnHkTpfO2_qUDatLZgLQDCbRz3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Z4DC3k0KnbYUMOc9G-zprBD5tEFKpNpi7kB-rpSuROV_0VC6YfYvj-qH5GWuETrSG-wvBSaFlbJJAsinNhev74CdjUsz8Yk3XIoGrbxBSgyo3ZD8G0vuMQnQ9iVuf0rUFGiUZoj9P2Es9SC6o7wYpSXAhHQQLQURRo6rUIt461b_YZv02lGKToc4R3ssrntH6w6xKeo1i8G0zIb7yqbrq1eoFWdsxt5huggAdnvd0M9k-7-CrnLraRJ1xHM9esu5F5utfr9PLCXBPd76Q5Xmg61OhLfjyoQZBsXc_iawazrCFGzUtykoUKvujC_YnHkTpfO2_qUDatLZgLQDCbRz3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=fRaX58QQ4KaQNri0VBwzfRArC1AgqQyU9w85r_9ugFyKJS44sQQYxXirxscwpuIh4kV_9jsquUEycB5r42cAUEYWdaf5XKxAi5MFT8yjapEoQ4a9McGx_hwzJ9eDbNft9bII7_07g9L5Drs7X07mdOaGvSnV7CgH4yedwa7sWiMkAGOU-FIIowP1HDHZaqkkYBfSssy-bFbTcmNfoHF-dQi2C4Q-5cP9Cq3bdL7QU_mvX-KLLJuh6pJeIg9nvaNHyiRr8zF4mHEFbV5zb-VxeRqpm3Q2oKiLNhQpvNMW6zcINw_fSpiXg10rJVFODzbg0EGkjEqw_SsVWLRhzIE2cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=fRaX58QQ4KaQNri0VBwzfRArC1AgqQyU9w85r_9ugFyKJS44sQQYxXirxscwpuIh4kV_9jsquUEycB5r42cAUEYWdaf5XKxAi5MFT8yjapEoQ4a9McGx_hwzJ9eDbNft9bII7_07g9L5Drs7X07mdOaGvSnV7CgH4yedwa7sWiMkAGOU-FIIowP1HDHZaqkkYBfSssy-bFbTcmNfoHF-dQi2C4Q-5cP9Cq3bdL7QU_mvX-KLLJuh6pJeIg9nvaNHyiRr8zF4mHEFbV5zb-VxeRqpm3Q2oKiLNhQpvNMW6zcINw_fSpiXg10rJVFODzbg0EGkjEqw_SsVWLRhzIE2cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=raaR4XchTUg4ZfqPUsgXX10KKKbzGaiI41AlxO3ytQx5umzt2covvQIxg6Ec2IMob7bg1cEFYxxlatpey40OG1TvRKI5rsgN914lev3qka2F75lLbkaMhYaGg5pAPDHZXwBzqjFnS6nqU3oo_HZ-dvWllgFnyXshehUSR7m3vFFGbEHsqlcxQRnUtGqO2olXAkymqvknGrUAwE9_FIzDt_XZywsmeEntihzG7H7vk6OTHOtqwq10--w2F8IKkiiw06Roi7_1Qdu1Exzlw0niTRYFcNYEaWOMoxtFcDU8jonakMegJ50llnQOOpxsIlnRH61OAdhAt4799QUttcadJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=raaR4XchTUg4ZfqPUsgXX10KKKbzGaiI41AlxO3ytQx5umzt2covvQIxg6Ec2IMob7bg1cEFYxxlatpey40OG1TvRKI5rsgN914lev3qka2F75lLbkaMhYaGg5pAPDHZXwBzqjFnS6nqU3oo_HZ-dvWllgFnyXshehUSR7m3vFFGbEHsqlcxQRnUtGqO2olXAkymqvknGrUAwE9_FIzDt_XZywsmeEntihzG7H7vk6OTHOtqwq10--w2F8IKkiiw06Roi7_1Qdu1Exzlw0niTRYFcNYEaWOMoxtFcDU8jonakMegJ50llnQOOpxsIlnRH61OAdhAt4799QUttcadJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=q4ZRSdZ2Si8u7-dmCqDdepXrkr2baJBfT2uKTDRwa8clIIfC6ZGsEKe17qb_zLfe13JISmJBGlcmlSoLApLs7k9CmKjQPPUhi4rFBUDe_j6aUJtVlAecjjid2BTwdXxlHPtD7EwISUZd1vcB6fH-MiOWEpBlfL6q_Lq5e5GRaZokCqkGO-FZuYDCDEhmSi6_HRHb-SJx77kZJp1u5uI1exnbdOLkK4ARCc4YtV3jT8-L8yyPdXmORPA6RhKgHHH67TC95cdJpD_5TcXRhZTuHPgaeCuUSmZHmSCSLQdlroJeiqOOG_RGq16-c6hgjC-eka6nEoM9ruUyavJsqRhvjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=q4ZRSdZ2Si8u7-dmCqDdepXrkr2baJBfT2uKTDRwa8clIIfC6ZGsEKe17qb_zLfe13JISmJBGlcmlSoLApLs7k9CmKjQPPUhi4rFBUDe_j6aUJtVlAecjjid2BTwdXxlHPtD7EwISUZd1vcB6fH-MiOWEpBlfL6q_Lq5e5GRaZokCqkGO-FZuYDCDEhmSi6_HRHb-SJx77kZJp1u5uI1exnbdOLkK4ARCc4YtV3jT8-L8yyPdXmORPA6RhKgHHH67TC95cdJpD_5TcXRhZTuHPgaeCuUSmZHmSCSLQdlroJeiqOOG_RGq16-c6hgjC-eka6nEoM9ruUyavJsqRhvjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgHuFoosUEmuD3SMYgA49M3tXLxWLcftoigCHX3onuO6wqhy8a0dfX2odgQxur-Iju5Gvu1JHkCNPVh2NuQ2KCEjOI2WyoKm-JtEA7v1V_3B5bNt5HtLVRilZV3nn4306-3CA1M8adjnHgr5RryMHzEnR1liL53lScK1dJOEgnLYA2gaBIRs_fejjpXa51cz_ezl7A2jcCWa6GbKs-v21RH5oo9wPIkkjZAHL6TWJlT-HI5uAZqECcVxyO8O5KNYwkonQLc8sgcPw5rN9FV9vEqcuGxi4GeD5Xtsz6MFDPy3oevrz53WRm9Kql5eGl-e2CXpogL78hIm1zq14vKNoQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=l1Qv4bLc6C0-_eZ0vBf8SxKD1lfAstJ8tg3sWw2ycIzBGBYXTU6yQFzbinH9fHvpy2hqvomnzddQThCHbxs2BOSaqO21v1DKpUGHcvg2azNDIAeHKrNrLtor6B_H4_iKkt6AUx78WDBW8jxFjRwaJG7zeIhKrY5mIXYndhf-ou6MzFSPKE5uuHHJFF_a4Kst94p30Xw9gPxNQNdU1wgGB2YM4Ve1vmguHeBiw5r5lL9fXYYuzNn1_E9n3axrTSqkexibwNUza5nWPC40thd1BJEsny1RyipNtknopaoFvOjv0dVLAzahhX6bt1AfKBoM0QSrKGQJbTZOKnO7dxj0eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=l1Qv4bLc6C0-_eZ0vBf8SxKD1lfAstJ8tg3sWw2ycIzBGBYXTU6yQFzbinH9fHvpy2hqvomnzddQThCHbxs2BOSaqO21v1DKpUGHcvg2azNDIAeHKrNrLtor6B_H4_iKkt6AUx78WDBW8jxFjRwaJG7zeIhKrY5mIXYndhf-ou6MzFSPKE5uuHHJFF_a4Kst94p30Xw9gPxNQNdU1wgGB2YM4Ve1vmguHeBiw5r5lL9fXYYuzNn1_E9n3axrTSqkexibwNUza5nWPC40thd1BJEsny1RyipNtknopaoFvOjv0dVLAzahhX6bt1AfKBoM0QSrKGQJbTZOKnO7dxj0eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=mrBA2xopecl1VPkxu0kdWAK7Z_GYATcxoFj2a4TMFu-3sBR7eX6YxbmfDmgtobZy9FiYBacPejGUwDU5qIvhBeuLALuyNTkIDBF42nKHXXwJ7bYL8nFdmKJ2RVcIevHMDnpSYlVLVqGgyB4PzHz73EkRQ71vjMhXNApqeV61fXYCu88RX95XB4SE3SI4FoS-VNbUn0mcbCI3QcMbBln7w3nR1ZVZ_DiOD7xj0ykM3GjBC2JUuyTyMh908WUo9ecSHR0dXo8Yqj4jpOiheKBbojF8uqBbE7duljYCvjrQBhMUMoR-u0nXLbfvLnbYWd95HcnAOMb_fSFZUnefujUAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=mrBA2xopecl1VPkxu0kdWAK7Z_GYATcxoFj2a4TMFu-3sBR7eX6YxbmfDmgtobZy9FiYBacPejGUwDU5qIvhBeuLALuyNTkIDBF42nKHXXwJ7bYL8nFdmKJ2RVcIevHMDnpSYlVLVqGgyB4PzHz73EkRQ71vjMhXNApqeV61fXYCu88RX95XB4SE3SI4FoS-VNbUn0mcbCI3QcMbBln7w3nR1ZVZ_DiOD7xj0ykM3GjBC2JUuyTyMh908WUo9ecSHR0dXo8Yqj4jpOiheKBbojF8uqBbE7duljYCvjrQBhMUMoR-u0nXLbfvLnbYWd95HcnAOMb_fSFZUnefujUAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=ou18cUyBZ3qODKWXDXTa0U88zjS6U8NqHSGv7Q4xs96wQYC-NpNY6K0p3bjM_l5ABfd03dSWJPhugcvweqbVS_HCarNVJ-JUgJRUbrYEl6IDYgJ8WAOe4UtIRmaZQ5cpq7WCY0cSg1u-6emyfSpOHSZfkRbKtwDRIEfyqjiW3oHW83uKiOWCMsGXkPz3Pz7kCc6pOrLT0inlVvXyF5Wdp0kSU-qZKc4zyHZxtSHT4T2iNJLJNakoJwDDJPttPf5SEOz9sljtv4Www_J860pzdTA5HzsXYUKOpiEyPcECNWxF0fWkvbGogqBeyiSmb5XNW0B1D2unqXjG_bBaXEMBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=ou18cUyBZ3qODKWXDXTa0U88zjS6U8NqHSGv7Q4xs96wQYC-NpNY6K0p3bjM_l5ABfd03dSWJPhugcvweqbVS_HCarNVJ-JUgJRUbrYEl6IDYgJ8WAOe4UtIRmaZQ5cpq7WCY0cSg1u-6emyfSpOHSZfkRbKtwDRIEfyqjiW3oHW83uKiOWCMsGXkPz3Pz7kCc6pOrLT0inlVvXyF5Wdp0kSU-qZKc4zyHZxtSHT4T2iNJLJNakoJwDDJPttPf5SEOz9sljtv4Www_J860pzdTA5HzsXYUKOpiEyPcECNWxF0fWkvbGogqBeyiSmb5XNW0B1D2unqXjG_bBaXEMBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=aE46HTlKH1QqHVfJQ9DK5NhC9a2nWN1Miysxp6rc_6gqGLbCxERkf3LibcZycs6v14rR_HeYTe114-ea0kC1yPPuPZ1vNvhQ_s6YjTw9NJUJu4v-2yjDr-w1fQ-hJ3dTMI5nxpdXrI_SzyYjJx68xOcDG_hbwVBNzoKGiElzbwDjYV6cHvVHJSE7tc-byRjlJmk2JiLJNk8tcnyLdZaK1CnLfj_HBrv7EzFTCbYd6B53iuFT6SIVhG90ZzXpaWCU5qUhsXZwz--sKA_2d7fVRSe99Ahy4OSW0tYrFwe7BZlKEC8RMWc6r1698uWJmmLdzaFh0S1TIX9Q1c9A-JnDoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=aE46HTlKH1QqHVfJQ9DK5NhC9a2nWN1Miysxp6rc_6gqGLbCxERkf3LibcZycs6v14rR_HeYTe114-ea0kC1yPPuPZ1vNvhQ_s6YjTw9NJUJu4v-2yjDr-w1fQ-hJ3dTMI5nxpdXrI_SzyYjJx68xOcDG_hbwVBNzoKGiElzbwDjYV6cHvVHJSE7tc-byRjlJmk2JiLJNk8tcnyLdZaK1CnLfj_HBrv7EzFTCbYd6B53iuFT6SIVhG90ZzXpaWCU5qUhsXZwz--sKA_2d7fVRSe99Ahy4OSW0tYrFwe7BZlKEC8RMWc6r1698uWJmmLdzaFh0S1TIX9Q1c9A-JnDoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnNERslr7mQV-xTuYFFf6octLnpUtdp7ka_vh3WYQhhgYb9_6E9GmSdQ2o2o2RWUDpwFNx5u39iZGDPxfC9ZlUGxp5QuaxMqC95liK_3EPXaLockbnhG8pR-XhSQAmAQDhjC8d-WE9GgqGpT6lcAIEprLTnQ6fQDy9nNBA8ACYH4Tmr0EQcp5bDO0DNRsSItSpLunHZxTW9GaEJzyD8855xYf5MdSo3YzF29L7_B63Kh22iLbWfDv0Ev_UFLpfloknH0f4RJFspXB6-KN5Q6ZGhjrlxVqmoKkjTTY6LTmmcsaRu6-rUPwKXxjJ7-uwYj6nSPu_E8FM0P4w9k8FrcYw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=vCW33Kan6EpWenBHP3WuGiRjr1PHuQDrC4r0550V9EpDjP8EqoUPwsPPh0wIsk_lwOE2vz6T-ZIKZ-n6yLs4v4wPFNObqXF8SyKUpc523mZORi52K1aViJayREOCjNTzgjoDCbll5E845YG44Vpkv7UOYc0MswOybs02mRId95GamnPjLiCwJDj1lhl6CY7o_XzIWD7H_3IdBLVU0KyzfBIpeXVFNXyZPU7oryCiFMalNoEDROOzEmPVhnnZ84gHN9pD_4yL7UAJlQR-xezxN-zlTwNIsVLp_Wc6Odz_2MKuCVE0GuOuDLsXBiKLdD4COHUxroCE3OPrFbN-C3GC1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=vCW33Kan6EpWenBHP3WuGiRjr1PHuQDrC4r0550V9EpDjP8EqoUPwsPPh0wIsk_lwOE2vz6T-ZIKZ-n6yLs4v4wPFNObqXF8SyKUpc523mZORi52K1aViJayREOCjNTzgjoDCbll5E845YG44Vpkv7UOYc0MswOybs02mRId95GamnPjLiCwJDj1lhl6CY7o_XzIWD7H_3IdBLVU0KyzfBIpeXVFNXyZPU7oryCiFMalNoEDROOzEmPVhnnZ84gHN9pD_4yL7UAJlQR-xezxN-zlTwNIsVLp_Wc6Odz_2MKuCVE0GuOuDLsXBiKLdD4COHUxroCE3OPrFbN-C3GC1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SAUYf5ZzKVVYMY3MAMrOvYc6JVyb6eSEEnqrDUIefXU0ulCPcwWBCvR9BSnGmDajm9CRuYwoWP_tRB973-ZmOWBGxm3vqeFh1aBlavk3rmnu1Gn0dB5B17G_4oS9JicK8YaGo_KXejNg7vGMrx3jGSGQp-vI-lDzSHARyiDaeOoJMUQx7rrd6viuqUQBuiOgADmvb8Rhh0pQDVFwqAu1-_61mdXKZDaag_6M_ih6FNOiaVZiePlYkFU5OTO3ps2l3tHUTMuS0lZsdlh6LQzeB2RYKZfnYMYUqo6oZ0WTXe8ju0ubmZhH9ZM0aUKF7ozZTNl4cYWiZ6A2RXXK9535yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SAUYf5ZzKVVYMY3MAMrOvYc6JVyb6eSEEnqrDUIefXU0ulCPcwWBCvR9BSnGmDajm9CRuYwoWP_tRB973-ZmOWBGxm3vqeFh1aBlavk3rmnu1Gn0dB5B17G_4oS9JicK8YaGo_KXejNg7vGMrx3jGSGQp-vI-lDzSHARyiDaeOoJMUQx7rrd6viuqUQBuiOgADmvb8Rhh0pQDVFwqAu1-_61mdXKZDaag_6M_ih6FNOiaVZiePlYkFU5OTO3ps2l3tHUTMuS0lZsdlh6LQzeB2RYKZfnYMYUqo6oZ0WTXe8ju0ubmZhH9ZM0aUKF7ozZTNl4cYWiZ6A2RXXK9535yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqyyQD9TNDvY2qPgr0PfAbopBM5xLb0xprACJlmwvCgOqji-sIc2cAIBgKFkGD8iy2kyJTCvEQhbn1aQPCGZ1CrZHSjTiI-kT9l9SQf-Vdmm19eNesxvgWBNLXA8O5FaxN9jZm3-rDGeRJlqfcXR6L1OM3T4vCmSCfiuhzOTkG5CAP6aag5S1Jwm_zdufTXkBqPudIlMDpI4CoFZ48QAMa1aS7lrfi8YiV_coMJRRs9-kIitQANIo2PJUueflSNdr_DkD-Tt87oixL8neNIjnvMcVAytBIOazJBu-k2riMgFLlwc9FKDpkbrx5CBZCKnhhKRBXqzfsDb21G2nJu7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCDmfB1T6XA9atvVnURfhfN7DeQpdpUrAuTOCoAe-GdaNlIIA3ptHge2keyE4tz2ixZnNvcPj0vSd15D9cLfPJg-dOeK_VrTnR4PFDHoRrHMX0jxLnMEXfsI0Ad7lJ8ndpswgX4l8gHizOZSDLPuGMXazOAIgexCOkeYewPJSF2hjbsvszpXbCnuHzQXLwuqjT3TQMCmQmZUXvG0yefEWwSYTxhdMvvMhWapFxBANyjbird93Ow2W29vj8rFq4umgOFMLkeSuUyVMk0cY6y0KTjAmlYoGzh7aQa8GfobU-9EmAjzwysuCISV8RJoj8UX3HFvuI7zx9uTH5JrQcnTYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=KlVqr4frTI86saR1as1Zq0QeBVwKo17EeIfD9PimRhm2_hrux9rxhrO1MvKIfh5vBPTucZIAzcnvLZF2AZygmkkNRqWva2Zvwn3weIP5E9gGjqSocBE2bRkooPibuRCP5I2xSpFmr1vqst42KYUSkOnpNdDYarz_OM_jAQjahQmKetFncuSBp6jIecbMdC7hGfIMrFw9nzj2peKIBYVmMxZTy644RBNJVJGMljf6ZI2kKy81_NWSbAxpvuPmtKmwRFHyH4KObT1FJL3gsZ5IcQ00v3AbKhhXOGjoK-Y70nFXtQh5WPMGczQJY8oD4TQ4aCYzIulf4t0JHRNHsOSt3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=KlVqr4frTI86saR1as1Zq0QeBVwKo17EeIfD9PimRhm2_hrux9rxhrO1MvKIfh5vBPTucZIAzcnvLZF2AZygmkkNRqWva2Zvwn3weIP5E9gGjqSocBE2bRkooPibuRCP5I2xSpFmr1vqst42KYUSkOnpNdDYarz_OM_jAQjahQmKetFncuSBp6jIecbMdC7hGfIMrFw9nzj2peKIBYVmMxZTy644RBNJVJGMljf6ZI2kKy81_NWSbAxpvuPmtKmwRFHyH4KObT1FJL3gsZ5IcQ00v3AbKhhXOGjoK-Y70nFXtQh5WPMGczQJY8oD4TQ4aCYzIulf4t0JHRNHsOSt3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg12QKJ5S5gupKEVfqjYnOpnO1ShzNzR_SPJizoqvEqrERpRZtRWFY0u-3HXkzxDeaoDCa_Qp8cZcs0dgSbUK8luntChGYjb0y4ck6d3mkLt3UmQQU7vtCKyJmLgeWvHPU5xD0A4vs-mDtd6IibOb0QDlFLUnsh6tEU3-srbL7KkBv69sewPaXoyukkXhzV_4T5Rs9auyoFyPi9hRmST7WUc5oZeBDtmG6lL-SEZQSKPGurLekiQcMI0guf_lCOCNbaB4Irp7spG4IrBJ1y2N9iKbcdIq_BqPMVg8K5SyO2bW7Utw-F6aXjof_0aDI1sRzlj3S5RRLcNJbLxNQ4EFA.jpg" alt="photo" loading="lazy"/></div>
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
