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
<img src="https://cdn4.telesco.pe/file/a2l-I55Ldkag-wHHYKEQHBH0oWbmialpkOhQxDpMyvgobnGOQihjm7ziFRgChQWESm6OCrvljtDrzTgtnWWWsrj4NG54Dz4Jkcc64JIUpAyhuqxo3_Uem_qfgjzlb6_zRHC4L4EqaHq7xLa8lMjBKHA07RtJYYa5hARBpv475b9nNXqF7kJfCUi5-Vcl7HD92saZIAZUtXZ1zhkg-_xShS1UwKarI-iGAjuhOmTAoimML2FAYLaMtbZnMJ1CldfIQsC_8CXypo3PrA8RAFTsaz2_DJEOBX77-xg7Yw1Vr9JUOxsWP7odACHJzRn4yyfDll9nIA_Te85u_bJGNnB3AQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 00:22:11</div>
<hr>

<div class="tg-post" id="msg-664419">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
نشست آمریکا و ایران در دوحه    باراک راوید، خبرنگار اکسیوس:
🔹
مقامات آمریکایی به من گفتند که ایالات متحده و ایران توافق کرده‌اند که حملات را متوقف کرده و این هفته ملاقات کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/664419" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664418">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5993005a.mp4?token=YrDFK63ik3RIFdUTKncXUjWhPLLOKKm82wAdZOvGRa2RJ5g_QrJ5ysqfNtHM9KMraUK4_iyEivx98df9-krVhgMx2vX8z8Yz7frmP3FWinqLP8OisjGFiThBY_dB0xSgDmyCDdpUobTNW50wFOa_8p0iiM1OxsmtUlJ5feVDYb2n-3lc2WLWb35_7qO9yfOh0fC5mCecn5Us3ibZaTssvB1YUdmtWHm1KbpFBrn8A_FzY2vB8QKOdjDE7C-APZRCBwZgABwZYcJe4ACRQpj25088i4Q4qw8IzIE47RuYqiQD5NzSAZ-cDcw5eZ39JX79ZKFgyZ1CCHnBR6b34YvtUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5993005a.mp4?token=YrDFK63ik3RIFdUTKncXUjWhPLLOKKm82wAdZOvGRa2RJ5g_QrJ5ysqfNtHM9KMraUK4_iyEivx98df9-krVhgMx2vX8z8Yz7frmP3FWinqLP8OisjGFiThBY_dB0xSgDmyCDdpUobTNW50wFOa_8p0iiM1OxsmtUlJ5feVDYb2n-3lc2WLWb35_7qO9yfOh0fC5mCecn5Us3ibZaTssvB1YUdmtWHm1KbpFBrn8A_FzY2vB8QKOdjDE7C-APZRCBwZgABwZYcJe4ACRQpj25088i4Q4qw8IzIE47RuYqiQD5NzSAZ-cDcw5eZ39JX79ZKFgyZ1CCHnBR6b34YvtUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«
هالک ایرانی» برگشت؛
سجاد غریبی پس از ۳ سال دوباره مارتین فورد را به مبارزه دعوت کرد: «تازه شروع شدم!»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/664418" target="_blank">📅 00:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664417">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b479ed2ef7.mp4?token=C4AXRn0P1AZHK_E1RA_CLICaBvM7SDsSf0bQ6ic9O8y_iykEM38YDk79fVNI17YOiLRXBczWFaI4NvsY3xHcHjrKHGzku95E8qcjkf_omc_p1H9cp2e8HPA0kqVZ_D1W-0IBydFgh2wrff6oQyPugJTZAzuNJNlcT8u8R0ImfDUf47WvUjxRRcxqw5ZFT2v939DqxsjeKCn-U7CehcfOKNoL-tkgTOa4JQB3WNQviIr7NN7-JrcL3Mjvg1CmQ8H_GGrXtjKmqBoKeMsvwn2vzPYlWSj5NOqPcBqxwFhiRZQI9cI3aqf_1P9TJdh6879pOxeqkfXYHVRbSkP9Pzoq7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b479ed2ef7.mp4?token=C4AXRn0P1AZHK_E1RA_CLICaBvM7SDsSf0bQ6ic9O8y_iykEM38YDk79fVNI17YOiLRXBczWFaI4NvsY3xHcHjrKHGzku95E8qcjkf_omc_p1H9cp2e8HPA0kqVZ_D1W-0IBydFgh2wrff6oQyPugJTZAzuNJNlcT8u8R0ImfDUf47WvUjxRRcxqw5ZFT2v939DqxsjeKCn-U7CehcfOKNoL-tkgTOa4JQB3WNQviIr7NN7-JrcL3Mjvg1CmQ8H_GGrXtjKmqBoKeMsvwn2vzPYlWSj5NOqPcBqxwFhiRZQI9cI3aqf_1P9TJdh6879pOxeqkfXYHVRbSkP9Pzoq7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایالت کنتاکی آمریکا زیر آب؛ سیل شدید جان ۴ نفر را گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/664417" target="_blank">📅 00:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664416">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA5-a0mZUqaUDSGjKXL2jU3W7GUbNqf4c6ZJ9Y9TIhyZbWQ7OzXe5zK7WBML091_aosYZ2xaHeBamJbilrCdIyV8PGPbLXjcYzNGKa1pRuwGMCNr0rErWYH95KHFAnrS-YeQh-nUqX3siz2Y2ajKzoNYdFTFl6l58wk5EEcUH2g-_QXAvcPOdA4ahADLjzV66OmgFm5ZOaJk9ax2wX7fqEXP87abzCHEbCSlsC7KJFEhYHS3X9nXbvcpvsXz_ZMzwvUakzdPIUdQriAW7I37tCloqq5YsSdLPeTojP7OHhaQe0BfS9rqCwLrZZUC8W9eVSjNfH5C2m6uGcX6tScdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاج بر خاک، تخت در باد؛ آغازِ شمارش معکوس
🔹
تاجی که با خونِ بیگناهان تزیین شده باشد، جایگاهی جز زیر پا و در میان خاکستر ندارد.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/664416" target="_blank">📅 00:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664415">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04ed2bc321.mp4?token=fjocHiHWnhY9kWY2vp2si1TS2YSyr9VzVE7IPpd8KydwyiZ0-N-osCpuSW0hE0YZeSTmCdMC4TtNgIrvc0u2cBDifoaQtlvJEpM7qJ6ROC8hSyQML31rbhGIj4dWZmsNDi2TSbNWUWYeslKJH7G5AuUNWJ1ZcSiJzTO4A9ao4Hs9zDLlVvTGvK4HDnfgtApUtgj7JOFLATOPyLPLKhq52FLieMmB4OjA2cfagn6LqyyMW-dWnQ2600onZ2sagPxRsg13MpZy56uCeR90FXpZsjPTKe1_0Ga0zxKAm-Z4lrEPVf0gy3dNMeIhe7pTGr5tGnkTSI9DpWuAhxtg_W2iVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04ed2bc321.mp4?token=fjocHiHWnhY9kWY2vp2si1TS2YSyr9VzVE7IPpd8KydwyiZ0-N-osCpuSW0hE0YZeSTmCdMC4TtNgIrvc0u2cBDifoaQtlvJEpM7qJ6ROC8hSyQML31rbhGIj4dWZmsNDi2TSbNWUWYeslKJH7G5AuUNWJ1ZcSiJzTO4A9ao4Hs9zDLlVvTGvK4HDnfgtApUtgj7JOFLATOPyLPLKhq52FLieMmB4OjA2cfagn6LqyyMW-dWnQ2600onZ2sagPxRsg13MpZy56uCeR90FXpZsjPTKe1_0Ga0zxKAm-Z4lrEPVf0gy3dNMeIhe7pTGr5tGnkTSI9DpWuAhxtg_W2iVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب در جنوب لبنان؛ ارتش رژیم صهیونیستی شهرک «مجدل زون» را هدف قرار داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/664415" target="_blank">📅 00:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664414">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
نشست آمریکا و ایران در دوحه    باراک راوید، خبرنگار اکسیوس:
🔹
مقامات آمریکایی به من گفتند که ایالات متحده و ایران توافق کرده‌اند که حملات را متوقف کرده و این هفته ملاقات کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/664414" target="_blank">📅 00:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664413">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ff4662cc.mp4?token=WHVzzad4SQBVQmWBu9e-pi66gfnOUhWR_c30XoA2kr7NVYduNfULVKEQDBxU32-bRuuu3h6gCWKrfKaDvAYy8zAQr_GLJUO4p_F8hXCjd75DM53ZwYN5Tzq3pcOrzIbJKh4Agoac75fbIlSHpck6Uov3pGM6YWM21jYmRXnXs3zCLdebVWSS38wfqom6g4fXdXQlW26Fmpe1WKurpcu2QJ81GGx_7ttzf9tCddjO00-Ir5n18VXtwGas_NWLBfrDPqcPJ5dZ5-1EwMl7ZSkYfmTVfHdUEtcqktc8HXjaAIOAGmAc9zx1g-dkgGJyyMvnHBgv_6z9xs0wEm4vPzDQRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ff4662cc.mp4?token=WHVzzad4SQBVQmWBu9e-pi66gfnOUhWR_c30XoA2kr7NVYduNfULVKEQDBxU32-bRuuu3h6gCWKrfKaDvAYy8zAQr_GLJUO4p_F8hXCjd75DM53ZwYN5Tzq3pcOrzIbJKh4Agoac75fbIlSHpck6Uov3pGM6YWM21jYmRXnXs3zCLdebVWSS38wfqom6g4fXdXQlW26Fmpe1WKurpcu2QJ81GGx_7ttzf9tCddjO00-Ir5n18VXtwGas_NWLBfrDPqcPJ5dZ5-1EwMl7ZSkYfmTVfHdUEtcqktc8HXjaAIOAGmAc9zx1g-dkgGJyyMvnHBgv_6z9xs0wEm4vPzDQRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در هر کشور چند روز باید کار کنی تا بتونی بازی GTA 6 رو بخری؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/664413" target="_blank">📅 00:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664412">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB8u5wmHJL9FSLHZe95OMlIqwLKVUG2bDXjDJaZm1JBtyb10vKEkZ0DT_gnK9pIYXx0Gj4ZYVnYB6I0Pr6Nv4MYh4MUSmlqJenNU7Nn7Ih3kkne8CaWLOSArPOuJoiomJ8q2Y2QFzr8JM-DPWwAmPp_IKVRaLr1bCOApk9boz-4MdRKU1i2XoDGCqT8OX-TvFu_e7YqRwXUQQ9NIKkfyaYavJzf__gF_YCqiTdmnbTriDsuxnUPllQwgREMcy2GX8toxpl45EFF1dPTr2dpgK8rR3kyAAkE509dIkCQeQ9lpzR-w7LcyEQVkcqT9XirWu7JMC5wg5h5gWrKOq504_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: مذاکرات فنی ایران و آمریکا با وجود تنش‌های اخیر ادامه دارد  نیویورک‌تایمز به نقل از یک مقام آمریکایی:
🔹
علی‌رغم حملات اخیر، مذاکرات فنی با ایران طبق برنامه پیش می‌رود و تبادل پیام‌ها از طریق کانال‌های ویژه برای جلوگیری از تشدید تنش همچنان…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/664412" target="_blank">📅 00:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664411">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-toZcGt0nDKjG20dhponc_71caWgA83ctT17gxH87tEJVhceSkxCgPYwwTlQyndUJPEuv2AhTP4ewhLuEEaKamcUz4TZWAvHS2b_4xaMp5hLnt2ltG9mvk5ySmwqgUI4n5kdsbpp8UlRR8W96YYF6L5lC-5LUuLR1u6fqNTaNI_JtjmJhwI7aQMPy7GVZCvotFZmYbHY-Dnu6jQg2LLyzzJZ5PSR8EW86W--lRFs9XTbQbzjEROgjoYvOzpzhLPySjebB_LtznyGcLcCDOMJL7kb5x6hKAM3MgauxhWUbacfUKbmayfYt-wZYr_7EcVtMugEWdV9sy7_qCFGeCnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/664411" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664410">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بر اساس اعلام مقامات ونزوئلا بیش از ۶۸ هزار نفر پس از زلزله‌های اخیر ناپدید شده‌اند
🔹
قرارداد اوسمار ویرا با باشگاه پرسپولیس فسخ شد.
🔹
رایزنی بن‌سلمان و ماکرون درباره آخرین تحولات تفاهم‌نامه ایران-آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/664410" target="_blank">📅 23:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664409">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn-LoyljgLVQSqq1W4l9_tX6fAOi38Lz7jFLklDcirObhFxba8UIfiDS5ycHsiUw1xmNJtt11U7bUOl8iBNMZsQ1nqjl66xOq2pzAhX4MKHxaeU-FPhv08ZmlAVMVjbHEjXet0Ib5X_5ZFTZIIbLfkNrvOR1xoIomYPYCrOr5jCDTpOiRfejPwQ_5n2GqGJxJUNinpWz0YVoUVtOACG1wgtkqIJ7lFujvPoQb0ijR0_nb2nAIyGvQ1SkGJpT6zHrVNEkAFh0Z2dFXUcB2kWkwCROYCpQJl0WJdKhBFqP5A7so7Atjfp55sp7_7gDZLK7bcVl_Sqmjfj-lBG65tmdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گریبان جنایتکاران را باید گرفت
رهبر انقلاب در پیامی به مناسبت هفته قوه قضاییه فرمودند:
🔹
یکی از مهمترین مسائل حقوقی و قضائی مربوط به همه‌‌ی ملّت ایران در این برهه‌ی زمانی، پیگیری و احقاق حقوق تضییع شده‌ی آنان در اثر جنایات مجرمان بین‌المللی و مستکبران و تجاوزکاران جهانی بخصوص در سالهای ۱۴۰۴ و ۱۴۰۵ می‌باشد. از خون شهدای مظلوم جنگ تحمیلی دوم و سوم تا صدمات و لطمات جسمی و روحی و مادّی و معنوی وارد شده به کشور عزیزمان و هر یک از آحاد ملّت مظلوم ایران در داخل و حتّی خارج از کشور؛ از کودک‌کشی‌ها و جنایات جنگی بی‌سابقه در میناب و لامِرد تا حمله به مراکز درمانی و خدماتی؛ از کشتار نوزادان چند روزه تا کهنسالان عزیز؛ و در رأس همه‌ی‌ آنها شهادت شخصیت بی‌بدیل، گوهر بی‌همتا و یگانه دوران، پیشوای مجاهد عظیم‌الشّأن اعلی‌الله‌مقامه‌الشریف، هر کدام پرونده‌ای از صدها و بلکه هزاران پرونده حقوقی مهم را تشکیل میدهد که در محاکم قضائی داخلی و بین‌المللی باید با جدّیت دنبال شود. آنچه مسلّم است گریبان جنایتکاران را بایستی گرفت و آنان را به سزای اَعمال مجرمانه‌شان رساند.
🔹
هفتصدوهشتادوپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/664409" target="_blank">📅 23:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664408">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ddcb5c72.mp4?token=m7zKV5cI9z6YWN6QX7iURVRNJaLXSQa6svKpyWNwGer2pGJitSfiHF2n5iNUafl9eZkCto4F2YuyJb4cJ9eyEjhPg5-24xnfIRP-7QdAlhFRSJRxyb06FP0_GhirzAw_GDai1YpkAsSjcq4vLuzWZ_zTlJbmmfOjALSqy5JuOhXgTQYZFz1UXP8KJf3KYSYxlm8GwwXOkH6vMdv3u0eVSl2Nc6RM-p5WrOYY06W-cPgMcDYGSC2UIWb550yyKlFQ1eMBPVMrqRcgKvkwGUp2uLHOO19G5uRr-zGe4ZDHkXARuLV7x9Z2ovlIdPQ9DJeAGMbBDUa9K5zMVlLffSuwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ddcb5c72.mp4?token=m7zKV5cI9z6YWN6QX7iURVRNJaLXSQa6svKpyWNwGer2pGJitSfiHF2n5iNUafl9eZkCto4F2YuyJb4cJ9eyEjhPg5-24xnfIRP-7QdAlhFRSJRxyb06FP0_GhirzAw_GDai1YpkAsSjcq4vLuzWZ_zTlJbmmfOjALSqy5JuOhXgTQYZFz1UXP8KJf3KYSYxlm8GwwXOkH6vMdv3u0eVSl2Nc6RM-p5WrOYY06W-cPgMcDYGSC2UIWb550yyKlFQ1eMBPVMrqRcgKvkwGUp2uLHOO19G5uRr-zGe4ZDHkXARuLV7x9Z2ovlIdPQ9DJeAGMbBDUa9K5zMVlLffSuwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست اینستاگرام اکانت رسمی تیم ملی مصر با کنایه به شجاع خلیل‌زاده
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/664408" target="_blank">📅 23:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664407">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e402fd7ec.mp4?token=WAxiA7DMKRl3P7GtwYdWXtGQfyi5Br4sjfR3xqWRp19FkWF9XYqz20XLByCF_cJLSCJnYF_cr8P0VK1LI0OrxdHWbfLQyvfedimBqW2U3VCpJXHLxnYhtwPEToPRy_e9um3PFdnLtKwzpby-L8gZ1hMRO4M-jc12ajsBL9-NEsQnbhAN-YgbB6UeOYVntrCh7GtDYtgTQEFeA8V7CgU1RGPgUhQxB8fRckSbHeNgIq2n7dq59Kzh89Ux8BKAyaohy9nIx4OSQJzWN5m132ar5ynLmxcDmfg9i0ekdIFzUby0pfkqXXv8FbqC13BIa_ByPtGy5BiAenPGUrbBcfXqxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e402fd7ec.mp4?token=WAxiA7DMKRl3P7GtwYdWXtGQfyi5Br4sjfR3xqWRp19FkWF9XYqz20XLByCF_cJLSCJnYF_cr8P0VK1LI0OrxdHWbfLQyvfedimBqW2U3VCpJXHLxnYhtwPEToPRy_e9um3PFdnLtKwzpby-L8gZ1hMRO4M-jc12ajsBL9-NEsQnbhAN-YgbB6UeOYVntrCh7GtDYtgTQEFeA8V7CgU1RGPgUhQxB8fRckSbHeNgIq2n7dq59Kzh89Ux8BKAyaohy9nIx4OSQJzWN5m132ar5ynLmxcDmfg9i0ekdIFzUby0pfkqXXv8FbqC13BIa_ByPtGy5BiAenPGUrbBcfXqxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جف کری، اقتصاددان آمریکایی: همچنان حجم خروجی نفت از تنگه هرمز پایین است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/664407" target="_blank">📅 23:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664406">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7adc36fdf8.mp4?token=qI6SeVZ2XPc7kd4hqVaa2Yd7Nmd-MkZlEENHqeboYqffS0Dy7lSfBtf6d-Sh_E1ow-pLJENDqS0m3ZyiZMiFpq9fqF_tnTgt1eaTQko1kfcCK3PqwIXF5wv6ZH1X4iWEParVR0yyY39Dh3TdtLYJ_OhWCAWmoLzsx2E0OOJg1BaXuBV6vD0LAHitTkaTMvQT14EWw_4khDH5P6jOE40R026WRWzwggExaRPtjpQMY6wFzpaQ3kmEIkhApbaVgmq2GqcWp9vZcEpE0cyMCHr11cZFS8cvh3eoaw4r4lH_TP8Oitx87IB2iSd-w_xa9CZ_1QmCbamCe9TuOCGAFkgxjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7adc36fdf8.mp4?token=qI6SeVZ2XPc7kd4hqVaa2Yd7Nmd-MkZlEENHqeboYqffS0Dy7lSfBtf6d-Sh_E1ow-pLJENDqS0m3ZyiZMiFpq9fqF_tnTgt1eaTQko1kfcCK3PqwIXF5wv6ZH1X4iWEParVR0yyY39Dh3TdtLYJ_OhWCAWmoLzsx2E0OOJg1BaXuBV6vD0LAHitTkaTMvQT14EWw_4khDH5P6jOE40R026WRWzwggExaRPtjpQMY6wFzpaQ3kmEIkhApbaVgmq2GqcWp9vZcEpE0cyMCHr11cZFS8cvh3eoaw4r4lH_TP8Oitx87IB2iSd-w_xa9CZ_1QmCbamCe9TuOCGAFkgxjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابانی
: رو دستت تتو کردی "باباعلی" ، یعنی چی؟
🔹
نورافکن
:
اسم بابام رو زدم.
🔹
خیابانی
:
اسم بابات "بابا علیه"؟
🔹
نورافکن
:
نه آقا جواد، علیه.
🔹
خیابانی
:
آها ، پس اسم مامانت چیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/664406" target="_blank">📅 23:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664405">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
هشدار بلومبرگ درباره دور زدن ایران در تنگه هرمز
🔹
«منچ‌اوسینت» اعلام کرد بر اساس تفاهم‌نامه ایران و آمریکا، مدیریت تنگه هرمز برعهده ایران است.
🔹
هم‌زمان، خاویر بلاس هشدار داد هرگونه تلاش برای دور زدن مدیریت ایران، بحران را پیچیده‌تر و بازگشایی تنگه را با تأخیر مواجه می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/664405" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664404">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
خبرهای داغ را هر لحظه در وبسایت خبرفوری کلیک کنید
🔹
🔹
حمله دوباره آمریکا به ایران | ۱۰ نقطه در جنوب هدف قرار گرفت
👇
khabarfoori.com/fa/tiny/news-3226210
🔹
پشت‌پرده تهدید ترامپ | بلوف یا هشدار؛ آیا حمله بزرگی در راه است؟
👇
khabarfoori.com/fa/tiny/news-3226385
🔹
قالیباف به سیم آخر زد: بعضی‌ها هیچ غلطی برای انقلاب نکردند و اسم خود را گذاشته‌اند «سوپرانقلابی»!
👇
khabarfoori.com/fa/tiny/news-3226201
🔹
ماجرای رابطه جنسی آقای مدیر و منشی اش | دوربین مداربسته همه چیز را لو داد + عکس
👇
khabarfoori.com/fa/tiny/news-3226323
🔹
توقف مذاکرات واشنگتن و تهران در سوئیس| آکسیوس: آتش‌بس بین ایران و آمریکا می‌تواند به فنا برود
👇
khabarfoori.com/fa/tiny/news-3226441
🔹
صفحه ویژه اخبار پُربازدید ما را اینجا کلیک کنید
🔹
http://khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/664404" target="_blank">📅 23:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664403">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teNTufCG82mLraXif_Dq6uOOIEauRa3SXugMjCWyzjLZp9YRH74EfkDZzqptGgmEvD0aTNv130Ix7ANCTLDQ7TqP4eL0h24bLJePmLnhR_aAZtzN8ZeqPPExqCUUoGAqHv3m6vzgiE6FDhf07v19Pvd8OfRsrA1OnvleCJdKeZaykUb7WryLmtToJgObRyiPtAy8TmFJjYHwQR2OiHH8qULxBBggsL2oz_-P05FOTiPPeXDbstT50KjCIb2AfXZZd2cRitvBNMezZSPv8HXMDYq8EmRKPXvgbh7L7CRrvNsXwtCyfxarbHsA1a7LPymPDh1hpxy4yMwUw3CaVNXekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدام کشور شمار مرگ‌و‌میر از تولد پیشی گرفته است؟
🔹
در کشورهایی مانند ژاپن، وضعیت رشد جمعیت منفی است و شمار مرگ‌و‌ميرها دقیقاً
۲ برابر
تعداد تولدها ثبت شده است.
🔹
در چین، روسیه و اکثر کشورهای اروپایی، تعداد مرگ‌ومیر بیش از تولد است.
🔹
در نقطه مقابل، قاره آفریقا و کشورهایی نظیر اتیوپی رشد جمعیت شتابانی دارند، به طوری که آمار تولدها در اتیوپی بیش از
۵ برابر
مرگ‌و‌ميرها است.
@amarfact</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/664403" target="_blank">📅 23:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664402">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/664402" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/664402" target="_blank">📅 23:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664401">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/664401" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/664401" target="_blank">📅 23:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664400">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfqoRTCuzWk6l5PVwTN_dLWqsDUQvkwyd3y8gwEuZ07-LZoNYE-nm_Uo9rEsht1qzzjc6aQSYu3UTFVzVgGzDxNyhhQ4iKjxpTOgHFhCQwJQlMkdfnhpfYvbtvtKOiKSZpJgErWcJdkZA5nLTH7khhy9T_YtjF4kQk32_qYuhSghjOK_ucgTvuwk9-TEQQ8dAtqFaXAD500fKDYYvChlX_TaQbFUUHRCTS5UdEBsh6HQdBZkiugeiLOPrIJXrp7_HmjS7DidkWH2pOPG7t28vfeEbCC8sKWBTD-WnONu2lbUhYVVJMdtUtk9HKn7PBpvQy94pgY3OwIwBMZwWwh1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فشار ترامپ بر سوریه برای مقابله با حزب‌الله | پیام محرمانه دمشق به لبنان | دلیل پنهان فشار آمریکا چیست؟
🔹
در حالی که دونالد ترامپ، رئیس‌جمهور آمریکا، خواستار ایفای نقش مستقیم سوریه برای مقابله با حزب‌الله لبنان شده است، مقام‌های دمشق تلاش می‌کنند به دولت لبنان اطمینان دهند که هیچ برنامه‌ای برای دخالت نظامی در خاک این کشور ندارند.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3226369</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/664400" target="_blank">📅 23:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664399">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsGYJpcJ8egmirqI3V7U-gjkaVjNMuyfnEbPbkkGBLgSarCnCt5GPQr7UQ1UzDHvB7qfUZ6Ls2i03avw4iVveg1FzxsUsWDWv883P2s3rk_swbXiJeQokOc3W2inmKURsFrBhrysMjXd_2IPmkK2B6vuWPY3NcCG5RExdbN7nPO1cM5E3VsIQlpRvU-ZtsfuBTjGLN5lFTxzLpem6jgDgiTqJtygYkv9c50DXZP_Jsxv5mSE8LMTzuJQAb5_1kJqTMh2eBaAdlJpuYBS9N8BlXR8JOLMBDfkUWV446wpmpomIKpnxjKWEY1vrVviJWvI4mdTBFHLRofmZr_7Dlx10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاع رسانی به‌موقع؛ جلوگیری از تبعات قطعی برق  #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/664399" target="_blank">📅 23:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664398">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N89lXjQ1_4BucVki6YiBaTy8czeLPFrvfsuhmBU1-p9RAeyjPOdj7Jt2Ll-83aSVsHqYEW12T3CSuny-_GAPIwmutFlIhRLj06XSc3341HVcMhfLlJuCMaHqDeTr8g-jchVKVL03z_50XtpSi4XfUj6SCMUuyOTmgsmuwX0OYNxON0Up-Immhf588pei6A2ZkmaoSwRlNPGyi6bOpUUqNFcnYHF6Mr8SZRx630k6c4iyaEReJ1CKmy57YAC_FqA0_6E_W7D_aVOn3GLkXLfkT-vTocr68VW8IGNfORRQxMbGDNjVvLdmxQeKiOQEP8yLuFCTYvusbnexMhmEyBIdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پستی ۵۸۹ کلمه‌ای درباره مجسمه‌ها، بناها، زمین گلف و فواره‌ها منتشر کرد :)
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/664398" target="_blank">📅 23:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664397">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای
الحدث: موشک‌هایی بر فراز شمال اردن رهگیری شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/664397" target="_blank">📅 23:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664396">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: بازسازی پایگاه دریایی آمریکا در بحرین ۴۰۰ میلیون دلار هزینه می‌خواهد
🔹
ستاد فرماندهی، چند ساختمان و ۲ پایانه ارتباطات ماهواره‌ای این پایگاه آسیب دیده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/664396" target="_blank">📅 23:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664395">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9FUWZZg9VohqIj5nePmzObAZf0z5aYziM9YsMHbjYV-faXl72EswqfiTRg3epjxYnbpqBQimk13K9ZosOfHVE35oD2Xls6U4SI0rx8jJzqXLrJsi7VrNdsS57WdLFszqr2TX7lsWxTDH6_tCpT6pbypkpR4x5QBqHitmjZ3dTT9J6GZPrrxVrH23LpXY5MPRsRzA_FLrz4GgaqmnDDlysl0Ax9g7_Lf9AWXsT28mENCB18f-nNvxOBUUIv94dDZ8jT94DFnVxUUxvQkoF8c_jUTTsqO7BMLQT7qhGRTfd13CXDK6z2zZ9WdwkCuQiedeC1avcFhglL96sz2wRVMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_چهارم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید بزرگوار
حاج قاسم سلیمانی
، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/664395" target="_blank">📅 23:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664394">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به جنوب لبنان
🔹
جنگنده‌های اسرائیلی شهرک «میفدون» را بمباران کردند؛ جزئیاتی از تلفات احتمالی این نقض آتش‌بس گزارش نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/664394" target="_blank">📅 23:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664393">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skPSYJth7l2eaHrrz8XHEaQLnGJ-ggAEU1J1mDvTQBPzsCLwZu0eNVnGAuz2-agrKEX9_E9XZInGddvOQ4NLx07xnXpNMFY8wb7ab6OwCmHtRoZpuiIYM-DcB9Dhra0tgBpDo2F8bgDWKmWyzBvy0yk1DoPY4IRd5lcCsarWAl0_l8puescO8iej7wufDGqW_Q9kyAf8X3AUbuj67R4bM5HC3HR--qRV-RQDzNp3pTS9FddbKMHwsG-89AaRvnRZLEIiHqZndH__nZef2ZHmfk55C-Syqr4D3iZza28X5is2Fx1x8flt7Tae3aQcGuYda6oeBNRRt28fUENzHK3VAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرمربی کره جنوبی، به این شکل بدلیل حذف زود هنگام از جام‌جهانی، رو به مردم خم شد و استعفا داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/664393" target="_blank">📅 23:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664392">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf46726b2.mp4?token=pFYdeXPowztKUMDkd09TPK8nE5LipJeeJwfO1-qxTvbKqGREFryHVsVdtnz7nQ09-o4EkM5eKH33OJkS8kvUydwAilRn1o1jGkxNofFEI2Jaa_D0FWawyBWsEVh1BcxyYXt2OmSsSfHePhHIONxvwFVFI1P_zTZkkh1vbZX9L1UUzagXkiCoAZwS-AQ8Du-nVBfGM-32D-oxUE0_qMXLRYKAWx29WQZj-yqXEiL8t7lTS0nxbKVQMjG1U4LgLh3S5NIsfVoxAQLxdTaFfE2o77eUzuRpEX1sxz_VYumnCnJ1ck5PVwvIMtGcr100gHqrAx6ujMjgXmKyRgf9B0qw4lZQAZZaRUFy5tBQTo_c2TR87iy4oXAcrjPoRi7EQgM4PnnX5YZrNnH2lp789aVjXJ45u7JWhlqyWt9OenV_tTtL_Vp0_lUmpeg6Z9SJMLRR8nyrh3Q1gDM4bC3D_9URXSBcYhQvh4eRC9Ojz1broJBdLyKbUKTP4kUHWw-NlxxVC8363NQAe3rxl4CoACAD9Q56hmNlx1Aaq_Ae8k-dutcxjJ9fcP1zlMXEjSnHMSIaIYXQtsydPALeZZSVYXSncLwu7SvSmigNJGqj5Ajw-aeNApKfXh912GMoNYXWghY-_-UvR_y-a-Ifqwv4vEDA-QBUdK8RxJ2jUC7KmXamNMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf46726b2.mp4?token=pFYdeXPowztKUMDkd09TPK8nE5LipJeeJwfO1-qxTvbKqGREFryHVsVdtnz7nQ09-o4EkM5eKH33OJkS8kvUydwAilRn1o1jGkxNofFEI2Jaa_D0FWawyBWsEVh1BcxyYXt2OmSsSfHePhHIONxvwFVFI1P_zTZkkh1vbZX9L1UUzagXkiCoAZwS-AQ8Du-nVBfGM-32D-oxUE0_qMXLRYKAWx29WQZj-yqXEiL8t7lTS0nxbKVQMjG1U4LgLh3S5NIsfVoxAQLxdTaFfE2o77eUzuRpEX1sxz_VYumnCnJ1ck5PVwvIMtGcr100gHqrAx6ujMjgXmKyRgf9B0qw4lZQAZZaRUFy5tBQTo_c2TR87iy4oXAcrjPoRi7EQgM4PnnX5YZrNnH2lp789aVjXJ45u7JWhlqyWt9OenV_tTtL_Vp0_lUmpeg6Z9SJMLRR8nyrh3Q1gDM4bC3D_9URXSBcYhQvh4eRC9Ojz1broJBdLyKbUKTP4kUHWw-NlxxVC8363NQAe3rxl4CoACAD9Q56hmNlx1Aaq_Ae8k-dutcxjJ9fcP1zlMXEjSnHMSIaIYXQtsydPALeZZSVYXSncLwu7SvSmigNJGqj5Ajw-aeNApKfXh912GMoNYXWghY-_-UvR_y-a-Ifqwv4vEDA-QBUdK8RxJ2jUC7KmXamNMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فضائلی: حرام دانستن مذاکره خلاف مشی رهبری و خلاف عقل است
عضو دفتر حفظ و نشر آثار رهبر انقلاب اسلامی:
🔹
به هر دلیلی ولی جامعه تصمیم گرفتند که این کار الان انجام شود و اگر شخصی می‌خواهد ولایی عمل کند، امروز وظیفه‌اش این است که  این موضوع تحقق پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/664392" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664391">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5b502fb8.mp4?token=O5J2L72a141iQObafslBaN-hepWoY9gVI_yckIJCsW7Oi5VDoOF3o3bAAGsD37s36R_BK8bDB5Oo1VJ1ndkPtgA-Gr5M6cf0561WF-v9Ov_Wpz4hmu1ITejQqbFVXWdl_ha3Z9rVdcCnIGnH8NqmM0W0gzANhYKMnvD1Bqpne9OwVkeQ9wM4ISb5fQ3N89ScDAUTdL3zJVYAWjDBT0Nj9LdhZDYY8EHUsVG6ZSkn6Bt7kSrlqQJuiJ-BVnZPzeECMt5xZJCdZfKE_HrWsaORA7Z_-vkyOipJ4ISDnEpAJ5cd-D73WMJ4AEopmDMWY_qmSVyz_R4hwOD5l9vTpsULyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5b502fb8.mp4?token=O5J2L72a141iQObafslBaN-hepWoY9gVI_yckIJCsW7Oi5VDoOF3o3bAAGsD37s36R_BK8bDB5Oo1VJ1ndkPtgA-Gr5M6cf0561WF-v9Ov_Wpz4hmu1ITejQqbFVXWdl_ha3Z9rVdcCnIGnH8NqmM0W0gzANhYKMnvD1Bqpne9OwVkeQ9wM4ISb5fQ3N89ScDAUTdL3zJVYAWjDBT0Nj9LdhZDYY8EHUsVG6ZSkn6Bt7kSrlqQJuiJ-BVnZPzeECMt5xZJCdZfKE_HrWsaORA7Z_-vkyOipJ4ISDnEpAJ5cd-D73WMJ4AEopmDMWY_qmSVyz_R4hwOD5l9vTpsULyIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مذاکرات با آمریکا تعلیق شد
فضائلی، عضو دفتر حفظ و نشر آثار رهبر انقلاب اسلامی:
🔹
امروز قرار بود مذاکرات فنی برگزار شود که ایران آن را لغو کرد و شرکت نکرد که دلیل این امر درگیری‌های این چند شب گذشته بود و دلیل دیگر این است که منتظر اجرای برخی شروط هستند که مثلا امکان برداشت پول‌های بلوکه شده است یا خیر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/664391" target="_blank">📅 23:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664390">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k25YA0Qj5IyEmS3TMPgzB2P8jkSfjHvfb8SXaT2PKp630SJlawcH50SYBbTFJoV18HQpnFF5QoU1KVv0gl_dgEp6IjrapH8GPq-uf69ltIULEw2QKNtj9Zclwqg9NfZHqseOQjyTLyOXi9kdtHvZuq3OiIpNdbk7r9TFAEDVRdMXkqd1FtXOjQlmMBz5IH_Jv1VTot91gkqK8MGPw8nPkMRpDP4aLZpW2zp8iNOneqsyJ1RCPFVT4wFsjIVermGwZ7qe-aAKO5g_mSkzJxtEa5MZIpiYcf-LJ_wbS7VGIC8IRc5NgB0UlLtYH1GQuISzRxoEYdlTL8HPNJvfP5IyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توجیه خاموشی‌ها با اسم‌های عجیب‌وغریب!
🔹
در حالی‌که خاموشی‌ها در برخی استان‌ها ادامه دارد، این‌بار قطعی برق با عنوان‌هایی مانند «مانور سراسری طرح ملی سامان» و «هفته مدیریت مصرف برق» توجیه می‌شود.
🔹
توجیه قطعی برق با عناوینی چون «هفته مدیریت مصرف برق» با…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/664390" target="_blank">📅 23:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664389">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXXae-SCFEXoSy2B-KoFQAY7PYYVIcJhL0fZOxnSmQBX7c6zTOzgyJILqOn0SdmTUdrA7gFYcKt_KB0Jm2iADU7HVWL51LnSEKxEcDLJoNNv62mDtyFBNeP6ud5VssdWM22iOJBmw4j6gwJuh6-eym1akHMF34SJoXkYY2YxpJ6r86ZMOyaCvi88prT4Styki2QvCqgIQdN1XSuFW0JDohEZQ_L2eVX0yCeFopS7pHe9kPaHu6NkDg0LOLXLv-SM9pri_h82U1j_-xS813p2x93plHPJkfhWNNQyyLKCVG5URPGzZPJPQY7O10wPUwZkTJbC8D5wgFqSyDVOEB91RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرما اروپا را فلج کرد
🔹
لایپزیگ آلمان به دلیل گرمای شدید، تمام خدمات تراموا را به حالت تعلیق درآورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/664389" target="_blank">📅 22:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664388">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fedc264c5d.mp4?token=BUfQKeuxFNo7jZK9Z6dZmdXsX-Cv4tCFQORC8g7UQeVL9QCQ_K7Xhz8p0clL3fZFaRrxGs4cK2h1cclGU0TWTwrX1ASmL8xazjzDfMUVpbXk11b5QWx5izrmhq1OvQGMG6xNGJ5HMYaV62_XmH4zMPNDx0MsS1NLoQlZG1SP8wDrkl0eB-yYsiKTveoIDamNZm4hS8uVoumLowKTTF2c7wpxw6wfuxxD7s_Hvn2rWLdcz3Cymqnc_JHJPclG2NTZjeCmOe2vUYSXgx127E0lO-sdspcJ9ikcEoZ1x_ybDotlL1zTQ3O1v0VTJtTpM6TlkHULiKC_iokJMo28D1HJgDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fedc264c5d.mp4?token=BUfQKeuxFNo7jZK9Z6dZmdXsX-Cv4tCFQORC8g7UQeVL9QCQ_K7Xhz8p0clL3fZFaRrxGs4cK2h1cclGU0TWTwrX1ASmL8xazjzDfMUVpbXk11b5QWx5izrmhq1OvQGMG6xNGJ5HMYaV62_XmH4zMPNDx0MsS1NLoQlZG1SP8wDrkl0eB-yYsiKTveoIDamNZm4hS8uVoumLowKTTF2c7wpxw6wfuxxD7s_Hvn2rWLdcz3Cymqnc_JHJPclG2NTZjeCmOe2vUYSXgx127E0lO-sdspcJ9ikcEoZ1x_ybDotlL1zTQ3O1v0VTJtTpM6TlkHULiKC_iokJMo28D1HJgDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزادسازی دلارهای بلوکه‌شده ایران پس از توافق تاثیری روی ارزانی یا معیشت مردم ندارد!!!
/ مدار
پاسخ های صریح یک کارشناس به سوالات کلیدی این روزها
👇
https://www.aparat.com/v/jmrz2dg
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/664388" target="_blank">📅 22:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664387">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
توقف مذاکرات واشنگتن و تهران در سوئیس  ادعای وال‌استریت‌ژورنال به نقل از منابع آگاه:
🔹
مذاکرات برنامه‌ریزی‌شده میان واشنگتن و تهران که قرار بود این هفته در سوئیس برگزار شود، به دلیل ازسرگیری درگیری‌ها لغو شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/664387" target="_blank">📅 22:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb933369f.mp4?token=hkZGJdtaLwU0CF4y4kM-nAdrgnPSb1iYHTHCugZz0SZBWGWaOySrvpB3B23haVEl3Oma_24S5lzwZLRlWbD2chlpU7PMoRWF4CJkgwu8yejMxCkkDmgb0aksQEkPyT02iun72YJ3q_3S0Yrl3jGCZ0AJ5anJ99AK_lrt72doXil1KU3yF5ki1tFxpxlZWn4FbWjL_Vh45S7CKmbmDmun5oYxyLnfP2ouqoWQfLjBNbdGthROpJmLAktWPjnc0biDK5dIvoeCXNNUdVVNHLcP6fKQSywrp3LucB-zGp7Xd17IeYjzfSDxjNAsKuB4PcSeiSfADTFhHm1e8-cvax2I1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb933369f.mp4?token=hkZGJdtaLwU0CF4y4kM-nAdrgnPSb1iYHTHCugZz0SZBWGWaOySrvpB3B23haVEl3Oma_24S5lzwZLRlWbD2chlpU7PMoRWF4CJkgwu8yejMxCkkDmgb0aksQEkPyT02iun72YJ3q_3S0Yrl3jGCZ0AJ5anJ99AK_lrt72doXil1KU3yF5ki1tFxpxlZWn4FbWjL_Vh45S7CKmbmDmun5oYxyLnfP2ouqoWQfLjBNbdGthROpJmLAktWPjnc0biDK5dIvoeCXNNUdVVNHLcP6fKQSywrp3LucB-zGp7Xd17IeYjzfSDxjNAsKuB4PcSeiSfADTFhHm1e8-cvax2I1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهردار نیویورک: از دولتی که یک دین را بر دیگران ترجیح دهد از جمله اسرائیل حمایت نمی‌کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/664385" target="_blank">📅 22:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664383">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDqR6X1YrJnKpVyu_-o7-01FWKc4w_gI_XuV3Axa0xnEmJakoWc-bMnFgwdQVYpmeCrM4vs6NpukoXb2cyEn44hBM7AUTQagCKeReIqdg1Sptsf6hcoCEmjCOkFP4Y2fW4lnrUgChw_a1299_S_lfK_czmnZRlrbS3Bq-ngs93EluH5eY9pDNj4uP-zWzCdFMfI1VdgYg4BI3q9-zYrGCjkhGMX8vc7Yb22TKeR3QckoAPBaAIbNWetg13j8fFo7xzj-w2rztKjrLHtdrdIFrtv4lzc6jKDk4871ZXisHSFAwtxOkHX_0r6hRj8Gkk20AsPmFsgIq5byAymp1ygTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوسان‌های عجیب قیمت تتر پس از درگیری‌های دیشب در خلیج‌فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/664383" target="_blank">📅 22:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664382">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EL6gIzjmf0l-9ElluwEfkdCVr5AAYoQAquY6bhRYMNnFxsLUVPCE3CgzQ2ls9lFPzSg8EzairBgKDY4BzJEo6zEyVQ1tKyiVEpyLR57vMVy4Kl9Pn-DrCsNz_Vih7Ptrarxlj57xWh1uNFaOI6eCpuUoUB7FK_gCJcPyOQ_5fSr-g-u0cxetsmpRa_Ny_AgdVIUqTbbna3QPEDlMZyUGhpWjzormVj6TNlzvz-_VPV-DjKUtlAn3Rtd0cQtVopDM_nwTkGMze6Z1YpdvB7ZTomDsd9gDwo88_WzO0ZwH8eVbIoAC-v4R-5fRLhBSWTd9V-tD5oAb_fWZhU2RIfYm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
جهش سودآوری بانک رفاه کارگران؛ ثبت ۳۰ همت سود در سال ۱۴۰۴
🔹️
گروه بانک رفاه کارگران در سال مالی ۱۴۰۴ عملکردی قابل توجه در شاخص سودآوری از خود به‌جا گذاشت و موفق شد سودی بالغ بر ۳۰ هزار میلیارد تومان محقق کند.
🔹️
رشد سودآوری بانک رفاه حاصل مجموعه‌ای از اقدامات در حوزه بهبود مدیریت منابع و مصارف، توسعه خدمات بانکی، طراحی و استفاده از ابزارهای نوین بانکی، افزایش درآمدهای کارمزدی، تقویت فعالیت‌های اعتباری و... بوده است. همچنین بخشی از این سودآوری از سرمایه‌گذاری‌هایی بانک در سال‌های گذشته نشات گرفته که با مجوز مراجع ذی‌صلاح از جمله بانک مرکزی ج.ا.ا انجام شده است.
🔹️
حدود ۲۷ همت از این سود به منظور طرح‌های توسعه نفت، گاز و پتروشیمی در شرکت‌های تابعه بانک نگهداری و حدود ۳ همت در صورت‌های مالی لحاظ شده است.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/664382" target="_blank">📅 22:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664381">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw0e-jCFjMFrEil8Y3vu-4M93PWuB8ZDFNVeGLNKvoXB-94EdXLJ_Q0BA_Els9d066a1B5mny3dL298oylwuF1WI9ZlbVkHR35eI9F9BA81Nh0Lou1VPF-t4dMndupNTj-xLlaMP4tCwVsbdnAfWqi-ZVo0dhsW2e_kt9SxEgpWCal-ROPW0kcXFTBrOxDwIqgP6b-hm_cHnU64DodGqdpqm0_clFOobMY6sGK1tbN5KQXVTcYqECLvRjJfTIje3UpJeaEaAb-E5ycWU7pl6lVJ3Z6_PXgs7UMyRgqPlQdZL8vnHHlynurwiUraqdHO2REojDXH1ZaT78877zEAcug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالعمل امام در آشوب‌ها و شورش‌های اجتماعی
🔹
امام(ع) می‌فرماید هنگام فتنه مانند «ابن‌لبون» باش؛ شتری کم‌سن که نه توان سواری دارد و نه شیری برای دوشیدن؛ یعنی در آشوب‌های اجتماعی و نزاع اهل باطل، ابزار دست دیگران نشو و بی‌طرف و بی‌طمع بمان. از درگیری‌ها…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/664381" target="_blank">📅 22:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664380">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkkR4P5412Ro_cThoZ4ub4iyDqouD1DHMoUuo7ZSOorAzMLkNE9_sUA7uo6AkUs-wzocCv6MI8mlHoyqcfIS3DKB0NphupJm1RIPhMtc3qhfDuiiW86CzmIetQucBC95Bl3BFnLJjgCerRpqIWzaXReeuJSH8d5zEhrPYx9qN44rRtpjIZ6hUBUO2w4VANaA6yQcpF33W8MvmcZPEnIoys0wZ9GXmIaONZUMdRRcpEgo7ubmuh1sB8dR7R5oifgNokTV2KNjQn-v7pOGtDgln6U4-Voz1DPC1r4KKpxVPNT9X63U_YQSFozHVRqPJalYYwbZVAWlSASt73Mqs8pJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده تهدید ترامپ/ بلوف یا هشدار؛ آیا حمله بزرگی در راه است؟
🔹
به نظر می رسد تهدید ترامپ صرفا واکنشی احساسی به ماجری تنگه هرمز بوده و این واکنش معلول خشم او باشد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3226385</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/664380" target="_blank">📅 22:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664379">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlRssGXuzucxx3k-3sGqUlZ5mM1EZI47GETjwKNnRAEL6LrmUhDT-ssDJQoRhmu2S9BODq84MFO6tjo89mYfsB_6tinaPYgHgiNvzxb97FiRjRVsERH9SxEOoXjamfgKhikJRf05pPxLxDx0lgt6Su6-kdK_xybpQY-GebDWzoWBcHStqRsiOB-K_yVDaJ19I1-di91Ii2BdIXErE84mD5opS5NZ9geHlDWWGfcFeJFcRTTz5emsrzURXhpy7mG44_m8eZYszq_Y1Y7-b-z68J_EiKAAsOqv_T8xYJdGOWXgkbf6vBxU_dH7sAn5uaRMkm1JDowZvB_NUvPdoAjr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخفف‌های چتی انگلیسی که باید بلد باشی چون حتما یک روزی به کارت میاد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664379" target="_blank">📅 22:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664378">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
هشدار تهران به واشنگتن: تعلیق گفت‌وگوهای فنی در صورت تداوم تنش‌ها
روزنامه العربی جدید:
🔹
تهران در پیام‌های ارسالی به آمریکا هشدار داد که تلاش برای ایجاد مسیر جایگزین در تنگه هرمز و حملات اخیر، تفاهم‌نامه را تهدید می‌کند و در صورت عدم توقف این اقدامات، گفت‌وگوهای فنی تعلیق خواهد شد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/664378" target="_blank">📅 21:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664377">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عارف: مهمانان خارجی از جمعه برای حضور در مراسم تشییع رهبر شهید انقلاب وارد ایران می‌شوند
🔹
رئیس دفتر نخست‌وزیر عراق: میزبانی مراسم تشییع رهبر شهید ایران افتخاری تاریخی برای عراق است
🔹
رئیس مجلس لبنان: توافق دولت لبنان با اسرائیل قابلیت اجرایی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/664377" target="_blank">📅 21:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664376">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2947d3d6c9.mp4?token=hMoa8ovRPtmwG1ucRwCiVMl5psp1bIjl8jTGC-9tCXqscEg9rehvKjSmEBZCqyi1HPTC4i6qJ_ISUjVtCHH0rsv9DS3ACs_DV0rtUrXXC8f5_bUvyPZt1OCbIsqR-YfPafeL0EwB-eXfP35iUkQRMx2HydqLUPrPUlOqugoQEA4dMJEti9XNcor_q_NIv3QcrxnlX3jIgq97ZzpGgL65lnTS0SEhIAMusbyAk9GdyxyM6C4f0thzYPnYyDU-yYOdkiTQ_T2wma25en8cptbF9GhXUuGWaARu2tI-vY6YGLQuCGRaUAiDJqdkchOTiPzxDlfgJ4V79gTQQ7r0rOJ_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2947d3d6c9.mp4?token=hMoa8ovRPtmwG1ucRwCiVMl5psp1bIjl8jTGC-9tCXqscEg9rehvKjSmEBZCqyi1HPTC4i6qJ_ISUjVtCHH0rsv9DS3ACs_DV0rtUrXXC8f5_bUvyPZt1OCbIsqR-YfPafeL0EwB-eXfP35iUkQRMx2HydqLUPrPUlOqugoQEA4dMJEti9XNcor_q_NIv3QcrxnlX3jIgq97ZzpGgL65lnTS0SEhIAMusbyAk9GdyxyM6C4f0thzYPnYyDU-yYOdkiTQ_T2wma25en8cptbF9GhXUuGWaARu2tI-vY6YGLQuCGRaUAiDJqdkchOTiPzxDlfgJ4V79gTQQ7r0rOJ_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض وسط سخنرانی؛ نماینده آمل با تیم حفاظتی جلسه را ترک کرد
🔹
در جریان سخنرانی رضا حاجی‌پور، نماینده آمل، درباره نقش خود در جلوگیری از واردات برنج، یک زن از میان جمعیت با انتقاد از «باز نبودن مجلس» سخنان او را قطع کرد.
🔹
این اعتراض با واکنش شدید حاضران همراه شد و فضای جلسه به‌قدری متشنج شد که نماینده آمل با همراهی تیم حفاظتی محل را ترک کرد.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/664376" target="_blank">📅 21:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664375">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMY5Xva3N8E0pdL75pvGEdFUpN9Wu_4amsGeL82i8OwUzjljD9aJadZ8Tm86Wg8PbTnZfraGdpgdTIoAvy8phCwv6dyOeuApGapeaEzaimW1HHktQTi7EWFjBeP2CK3yEU3GZ_Gl7OCGsK0BVjRVpSOBE44Pe6rd2DfEYoyNNm7awgcVS8zlz7y8hBX2dKEhiGkfPbg0xvvbhgHlyU_rEn1CPU9GjBYQf3CwcqPw5mPvis7LlYpuNQY7XtS2HNf-Jj3ZvXMcMnWfqooICqCovSw2iAY2JaTxbKPtTZAZDuRrhDbGI7f79Vj4HcVN75hynuw56l4OETHdbsfVi5z3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی سریال: سوپرانز ۱۹۹۹ـ۲۰۰۷| ( The  Sopranos)
🔹
ژانر: کمدی سیاه، درام مافیایی
🔹
امتیاز (IMDb): ۹.۲
🔹
خلاصه: رئیس قدرتمند مافیا، کسی که همه از او حساب می‌برند، ناگهان خودش را روی مبل یک روان‌درمانگر می‌بیند. سوپرانوز از همین نقطه شروع می‌شود؛ جایی که…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/664375" target="_blank">📅 21:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664374">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
جدایی روح از بدن در میان شعله‌ها؛ روایت متفاوت یک تجربه نزدیک به مرگ
🔹
00:06:00 ماجرای سوختگی کامل بدن در حیاط منزل
🔹
00:12:40 تفکیک بوی سوختگی هر قسمت  توسط روح
🔹
00:19:00 انتظار ملک‌الموت برای همراهی روح بی‌نتیجه ماند
🔹
00:35:00 هدایت شدن به مسیر گمراه توسط موجود ناشناخته و حیله‌گر
🔹
00:42:00 رؤیت هیبت عظیم اسب سوار در بیابان دلهره‌ام را به پایان رساند
🔹
00:54:00 تعیین حریم برای من، توسط اسب حضرت ابالفضل (ع)
🔹
01:09:40  بازگشت به دنیا با دعای خاله در حرم مطهر امام رضا(ع)
🔹
قسمت بیست‌وچهارم (آتش)، فصل چهارم
🔹
#تجربه‌گر
: محسن اسکندری
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/664374" target="_blank">📅 21:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664373">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/664373" target="_blank">📅 21:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664372">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
گزارش شهرداران کلانشهرهای کشور در حوزه بازسازی جنگ/ طراحی مسابقه ای بین المللی برای طراحی یادمان ویژه شهدای میناب
نصرتی معاون عمران وزیر کشور و رییس سازمان شهرداری ها و دهیاری:
🔹
با همفکری شهرداران کلانشهرها راهکارهایی برای تامین منابع مالی برای بازسازی خسارات جنگ دنبال می شود.
🔹
یادمانی برای جنایت مدرسه میناب و شهدای مظلوم دانش آموز، طی مسابقه ای بین المللی تهیه و اجرا خواهد شد.
🔹
جشنواره شهید باکری برای تقدیر از شهرداری ها و دهیاری های برتر برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/664372" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664371">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da10dc61f3.mp4?token=cN1OuqnMPedurZG0b6kNeB0BEKSnsRhjrdqO1uCZNOYzJfok0m980hvpxDVDb0xXCDFYZZmIWlbiHZRv0u-nwfIam-_eHnydwVtZ8Ernwzsw4Nwzo2bPvCB6THuOxpE59zA4_ACFoC-3qbPrjKZ43Uzw_lfujcKbT3Juxz8nY8L6LwnHCJTnPnQvtewv1iGsDHAjRKgbhZS050jJp1JAEWMlbBfuZccrDExRq9MEREhzkxkyEGFic57yLd0FgkKiE1neZKNI0DHuJUXCJqytxc6P48TNYV84oPisJ883pcuTFCHPg4eyps2MjBDvwLXprbgyPvNB8q2Xtb-D8jm0tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da10dc61f3.mp4?token=cN1OuqnMPedurZG0b6kNeB0BEKSnsRhjrdqO1uCZNOYzJfok0m980hvpxDVDb0xXCDFYZZmIWlbiHZRv0u-nwfIam-_eHnydwVtZ8Ernwzsw4Nwzo2bPvCB6THuOxpE59zA4_ACFoC-3qbPrjKZ43Uzw_lfujcKbT3Juxz8nY8L6LwnHCJTnPnQvtewv1iGsDHAjRKgbhZS050jJp1JAEWMlbBfuZccrDExRq9MEREhzkxkyEGFic57yLd0FgkKiE1neZKNI0DHuJUXCJqytxc6P48TNYV84oPisJ883pcuTFCHPg4eyps2MjBDvwLXprbgyPvNB8q2Xtb-D8jm0tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پلیس راهور: جاده‌های تهران در روز تشییع رهبر شهید مسدود نمی‌شود
🔹
فقط به شکل مقطعی پیرامون محل برگزاری مراسم محدودیت‌هایی وجود دارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/664371" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664370">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای جنجالی نماینده مجلس: ارتباطات ناصحیح عباس علی‌آبادی مانع از استیضاح او شده!
حبیب قاسمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
باتوجه به شرایطی جنگی که در کشور به‌ وجود آمد، وزارت نیرو اقدامات لازم را برای مدیریت قطعی برق انجام نداد و اگر مجلس باز شود این مطلب بیان می‌شود که چرا در بحث توسعه و زیرساخت‌ها، انحصارطلبی وزارت نیرو باعث شده که مشارکت بخش خصوصی به حداقل برسد.
🔹
بارها موضوع استیضاح وزیر نیرو در مجلس مطرح شده ولی ارتباطات ناصحیح وزیر، مانع از استیضاح او شده است.
🔹
هزینه حق انشعاب‌ها به‌صورت غیرقانونی و سرسام آور توسط وزارت نیرو در سه مرحله افزایش داده شد و از مبلغ ۷-۸ میلیون تومان به ۱۵-۱۰ میلیون و در نهایت به ۵۰ میلیون تومان افزایش یافت.
@TV_Fori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/664370" target="_blank">📅 21:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664369">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8586c87e09.mp4?token=Hqo7WHCS0JFMkcYQHxPJACcgJGrGzAY1B04qXcNxwpFZycUAPHewOMY4QrVIxD3-xwSrkvIGtavSi2CWiR4bvD7HZoC32B-xU8NoBin7kJpolVrZ-XqXvcYT5QnJJ0cFA-WUKTzoSQUC-a4t7BgpaOy_YUIZIWZsvWAFkHdq8JegSwtyGu7LZHSINtobzgeL6AVOCKP7FjcC4VSv68vfdRVzA8wX8cgs4WD3srjY4voK4O8C7VASTrPxSOGX8beai-EVKWcgZqTc7EEYr_Hvq19RXSSwXW1dceqWkYXPu8udHVdzgV9Qy34YqRdLhdnkrM6c9WGt4755ClZetBKIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8586c87e09.mp4?token=Hqo7WHCS0JFMkcYQHxPJACcgJGrGzAY1B04qXcNxwpFZycUAPHewOMY4QrVIxD3-xwSrkvIGtavSi2CWiR4bvD7HZoC32B-xU8NoBin7kJpolVrZ-XqXvcYT5QnJJ0cFA-WUKTzoSQUC-a4t7BgpaOy_YUIZIWZsvWAFkHdq8JegSwtyGu7LZHSINtobzgeL6AVOCKP7FjcC4VSv68vfdRVzA8wX8cgs4WD3srjY4voK4O8C7VASTrPxSOGX8beai-EVKWcgZqTc7EEYr_Hvq19RXSSwXW1dceqWkYXPu8udHVdzgV9Qy34YqRdLhdnkrM6c9WGt4755ClZetBKIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو چه حکمی میدی؟!
قصاص یا بخشش؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/664369" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664368">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سید عباس عراقچی وزیر خارجه ایران در بغداد با علی فالح الزیدی نخست وزیر عراق دیدار و رایزنی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/664368" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664367">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGqc3-1xPM-u2gYDNAyAzMV06ehy6dRneM0Jyrf5l_ECYgATPk4emZaUfBW0eJIArPvXjiXpEZmDdTZdqfu4jqpptfEeeV2LRFiaLH2_OvMv9JXqSdPJTSFi-sFJA-ftNJSRu81IiWsnA1erT3-zv18SwHpokWHMpPjdoDkzRCAqIiu9QTj05tJPGyQ4fDNbRDr8r08KIfPILe-OydbD32yHqkR-PfLN6xQ2ZbZTmFj5R_4PJufSmzsCbybx0Hga2BAs0BoAcd11Kxj-3RQH8uao6nn_yIF7IKGQ1vmltNpBS-N1hVv99GH0gRCkHUDUplhgipeNq3UJBDcfVsXj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین شانس قهرمانی در جام جهانی ۲۰۲۶ از نظر Opta
🔹
فرانسه در صدر جدول؛ آمریکا در جایگاه یازدهم.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/664367" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664366">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEJZe3FJ26GfNbQMLXd5a6ileLDzKXwqQd151qWpkThVElTHeoiUmFMQhOAxfKEc-ouN90jSpqLKGCwGJP9hIosF0fIXinVzAbuFnyixFqXgMIgY6TS1QbXiwxONj4TYzspkAzF0KGXxOHW9Gon6WQprbFHJoVJk72uZVSoWD1BDe1Kk60R6eE1OHKpy8jKP484nFvn_wUh6zgODe7jB5IFv_7H_GZtwCQOefSwm1RcSjsJ7pjt4vxxZ-NKBLxNc0ip90vLiSbrSuKinQUz8l3lecFpOQViRPd3y9i2kv1TDCuOkF0XhNNeBYhy7ec_LQpZMnzWkXcIccqca8D6wBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکاتی که باید قبل از امضای اجاره‌نامه بهش توجه کنی وگرنه ضرر میکنی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/664366" target="_blank">📅 21:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664363">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بانک‌ها در خط مقدم تاب‌آوری
🔹
جنگ امروز فقط نظامی نیست؛ از حملات سایبری تا عملیات روانی، هدف اصلی اختلال در زندگی روزمره و فرسایش اعتماد عمومی است.
🔹
در این میان، شبکه بانکی یکی از مهم‌ترین زیرساخت‌های حیاتی کشور است که حفظ پایداری آن فقط یک مسئله فنی نیست و به آرامش اقتصادی و اجتماعی جامعه گره خورده.
🔹
تجربه اختلال‌های اخیر نشان داد با وجود فشارها، استمرار خدمات پایه بانکی و همراهی مردم می‌تواند نقش مهمی در عبور سریع‌تر از بحران و خنثی‌سازی اثر تهدیدها داشته باشد.
🔹
در چنین شرایطی، سرعت اطلاع‌رسانی، شفافیت بانک‌ها و استفاده مردم از مسیرهای رسمی، به یک مؤلفه کلیدی در مدیریت بحران و حفظ ثبات شبکه مالی کشور تبدیل شده است.
مشروح خبر در لینک زیر
👇🏼
khabarfoori.com/fa/tiny/news-3226382</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/664363" target="_blank">📅 21:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664361">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwafO5yCiLLqAkwv4vCOShH8TqqG8Nsv-0j03UoHo1O7rFB9t2kkoDGh8pjiVrFluoN1YPk9DKEgBYnBugnie0bPkpwQXk5n-4Htu7kIhjk7ZM4RDWuXzmdR7HPjyoGG2Y4F8djkHbrULlkX4d079SemRygJJq7H1YkQApUMbVN6huGthZhggNFLR2-pbKV4duZoJKZcMJmahUdwnEAxqkWTz_UV6Fd1nKTQUCogyeBI7eicDDezk-s0sdjn4duUPcQ0M0NttjxPNTk6nycRpWZJsTOzQIPwlQcl1gYjNmCC1y-ubcVcg0WB9lAGlS-5_FrsUdwj9v-zQqgJ9804mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی: «حمایت فنی» غربی‌ها پوششی برای تجاوز علیه ایران است
🔹
سخنگوی وزارت امور خارجه در سالگرد بمباران شیمیایی سردشت، کشورهای غربی (آلمان، آمریکا، انگلیس و فرانسه) را عامل اصلی تجهیز صدام به سلاح‌های ممنوعه بودند.
🔹
بقایی تأکید کرد همان ادبیات فریبنده «کمک‌های فنی و لجستیکی» که در آن زمان برای توجیه جنایات صدام به کار می‌رفت، امروز نیز ابزاری برای توجیه اقدامات خصمانه علیه ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/664361" target="_blank">📅 20:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664360">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تکنیک جدید وزارت نیرو برای کاهش اعتراض‌ها به قطعی برق؟
🔹
گزارش‌های متعددی از قطعی پراکنده و بدون اطلاع قبلی برق در شهرهای مختلف منتشر شده است.
🔹
بسیاری از مغازه‌داران می‌گویند این خاموشی‌های ناگهانی باعث از کار افتادن یخچال‌ها و اختلال در زنجیره سرد فروشگاه‌ها…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/664360" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664359">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sypLng0BUfRSxa85pwhaZrewt_KCAH34AQe2WjlrIHPdRHbcTOoKrXWiw_OV2PAMZqsyPX2aKaCpBQjKEHa116q26OZgOtFd0ye9I5rXhhqyt-7-klVJfRcYyD8msI2VP2X1F96glnyzIh7kh1cEQHuooJtyY7YrM_Hw5hx5l6satfgxHuvMy1xr8ItsVIYPfz83dlWql965iWu1JtjNcYFxgz5xs7RLM4sx2nenxS1rQ2FTnKn7Q_egyCFNSiUuhAqkhrQNdqBjQkQaQqL9-mn_-SuZXYWikM-FuD9b8dLqy2Jggk5_Vnjib-DBtiehHR8JV9iO2lo1HoxycKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری جالب از عثمان دمبله بازیکن تیم ملی فرانسه و همسر محجبه‌اش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/664359" target="_blank">📅 20:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664358">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN1uvFLJYIocImwK27dLX_0nCrvHcrumtjt5jsAOaYEL2DcbUhL4EfZsz58ljeb7gnP6RHe7PtD27EetEFEtA7FauoPJhdbnBmEdHeyHQRRqNVVFVIoXQWvU83GSpinAk2jBzUzyV36cZNlRfVmaOn3hpb96saEv4QM_L2YOYzQD6vs0tDPxoyEi5kENUmH49Z4UiF6DAHiX0rYLjm2jRm05-TdhiPdcJ7DTRaREJupR8IBEIHkvltuJI_ddx-SmZRqbnkqRKmUogbCjmsODYwut3wSLndfPvjewA5DQQRBhfp02scZtJ03QF6OuDYgdopoN9yKVEQPp9Yq5NNAzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان عبور کشتی‌ها از تنگه هرمز همچنان اختلاف بسیاری با میزان تردد سال گذشته دارد
🔹
بر اساس داده‌های «PortWatch»، میزان تردد در تنگه هرمز در ژوئن ۲۰۲۶ با کاهش چشمگیری نسبت به دسامبر ۲۰۲۵ مواجه شده است؛ به‌طوری‌که تعداد تانکرهای نفت از ۱۱۵۰ به ۵۰ فروند و کانتینرها از ۴۰۰ به ۴۰ مورد رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/664358" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664357">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت بهداشت: مصوبهٔ رایگان بودن بستری کودکان زیر ۷ سال همچنان به قوت خود باقی است
🔹
وزارت کشور قطر: یک شهروند قطری بر اثر اصابت ترکش عملیات نظامی در منطقه کشته شد
🔹
انگلیس اجرای تفاهمنامه ایران و آمریکا را خواستار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/664357" target="_blank">📅 20:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664356">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff799e747e.mp4?token=FPzM_BbFXUyWFRpdGyvSzauULNRy81t-bAJmhasQwiikn3Lo0gzXO1GyTwzUNdkzy3wL8sn0utJpUBicFP5bQxvbjIEMJbTyr0noxM5m2g1OmjLmiLIOPT4XGbqpPe70ZrmgSSp_EAQIIhGbYvtdRU6DM4UxRQtipsBDv-MoJH2-QwE30astgc-_5ItiPET-yFE1Ks418tEKrkU9E13liA1yXlZQtOV-jlWZQ22QUA79hO1YyHywYFFp84ytRMinOafv1oQLdVchSSis8_LZBqDQE04MwrMa8klGtMrsPHO-gCvocdFzCZ2T1uVWqL0heWRzy8Cu8ooJ_LiE67jMCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff799e747e.mp4?token=FPzM_BbFXUyWFRpdGyvSzauULNRy81t-bAJmhasQwiikn3Lo0gzXO1GyTwzUNdkzy3wL8sn0utJpUBicFP5bQxvbjIEMJbTyr0noxM5m2g1OmjLmiLIOPT4XGbqpPe70ZrmgSSp_EAQIIhGbYvtdRU6DM4UxRQtipsBDv-MoJH2-QwE30astgc-_5ItiPET-yFE1Ks418tEKrkU9E13liA1yXlZQtOV-jlWZQ22QUA79hO1YyHywYFFp84ytRMinOafv1oQLdVchSSis8_LZBqDQE04MwrMa8klGtMrsPHO-gCvocdFzCZ2T1uVWqL0heWRzy8Cu8ooJ_LiE67jMCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس مورفی، سناتور دموکرات: ترامپ بزرگترین تهدید برای آمریکاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664356" target="_blank">📅 20:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664355">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmIRfY4p5a4--1VVpq46wPG1Fw8hbhMNlAKcGJqoYBPcJ7HV4qx16ZNuNox8sbzXk6wHBB4f00cArQLFHMd8PGykY_wBgKH9GKUN4x5KLEQIVFbWod3DeOWSIH6b82-QiodZ_3BJH5W9cZgqqAmL_O06dlzMY0nbKcekFmcP7tuvImzNlk9qe9AJQ-BfmCsefIqxklL4a_K5ffYRkKx4yswuwQp3fRX4kQAtQz5EBGxGFgvZ6bmQcG_9Mbll58BVRohJQLMGRF1qMq3ouz3542YFt_lA6V7Cz-cYxNxv-FnNUmjz-9ejslhw6zSuyrJKUmw10xlKtCYlQB4do9Q-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم‌های صعود کرده و حذف شده از هر قاره
🔹
از قاره آسیا فقط ژاپن به مرحله بعدی راه‌یافته.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/664355" target="_blank">📅 20:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664354">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تمدید آخرین مهلت ثبت‌نام آزمون‌های نهایی
وزار
ت آموزش و پرورش:
🔹
مهلت ثبت‌نام برای ایجاد و ترمیم سابقه تحصیلی را تا پایان سه‌شنبه نهم تیرماه تمدید کرد؛ این آخرین فرصت داوطلبان برای ثبت‌نام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/664354" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664352">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/liN-hnyI4H8u2puo6JIjxQgW2UGdTAJM27AeE0eMRwQEiVSWK2UqMjnf3i8rFSnaZ0Uck_5FjZqFDUIUmORKZ-BIGrZCKm4L7nP7gn76_8V0Cfg61tw1DNpFrXSbWuxa1OQ9JEU5XrPCTXbN7zExlZHwT4fjxE2pTGKdCWIVwuq69F-7hep1PNlVNKz9ojQX6Vnd1ePrpOZFzl-0TVyrJkbY6mqYUPuvb44xatobRsLAf9LDC8a0VRv7sPFmoJgf3rbC2gyJvTHc2EtQn4jdaXBbOIvCHh0aGDeHZ9GBExDMT42zb8wLajpmYtKK7CPzo5TM0GVxdZkCLrrOl2I5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC2xLNnBDCQ4Bxb_FaekbAUlEhMA6PmW8PbzQymozx-4Mdo2hEt42abyHBWW-KIrltNRlcx6jAzoKgAVJNkx_UJSrcYisSXc5vqBL6kUxOCSd9enPm_ZOVM1-EZ7tb5HMo3YaNYzAg0mCLEXNc8EM7a67MM8eNR2NOnCGesVnFrpUGWCwFkSHKalnjKkJNfEMRy3T8wz4zzTO0EAp1X20E2AvWH5mnIGT1_CfhUpGzXt55pBXIKHaA7vD4QyenW1zTNPRi3a_HDWUQGx_acJoYFiVE3OIvULV1KNw70Zt9i75d_BMXWkUsN4bDJF59dBQbDvgx7ukkcO-XF2F3ZFXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا وقتی تاثیر نماز را در زندگی‌مان حس نمی‌کنیم باید نماز بخوانیم؟ برای پاسخ این کتاب را بخوانید
!
🔹
اگه تا حالا نماز برات فقط یک «وظیفه» بوده، این کتاب نگاهت رو عوض می‌کنه. «چگونه یک نماز خوب بخوانیم؟» از علیرضا پناهیان نشون می‌ده نماز می‌تونه منبع واقعی انرژی، آرامش و معنا در زندگی باشه. کتابی کوتاه و ساده اما تکان‌دهنده برای تجربه یک ارتباط زنده‌تر با خدا.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/664352" target="_blank">📅 20:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664351">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4Gb1e63sXIPyoCucLaFNf1pm4AiXIXZ4Kqbo-hmDv0-BaJeTRvkvv3B-V_X8q-5WMmQEAyWLPQKA__HxQ9U_Kqi_zbYjSUEzUFq5iSrsaamvIjCIxnhiIDxVplXQCFfNTd4vipzsUCmDOyxXF5fsfgHz287fNjGT9giCxDjkrv2oMdhVwi3E8ArULtLyTYTRB-RfMmsmdR9ebAR4h8KAAIqwXX5wwgFG8pNTVefdjn1iZm51QKi07C2ozs0H1CMumT-LwAvYZft6RcimxoSsL-AeJYnvF8jrBxjqipyuyMscwdbbx7O7YY0zXQ0p5A7MMfxjPr_6IvnQW_R8Fw-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨
☀️
این تابستون
یخ خریدت آب می‌شه!
🔥
✅
تا ۸۰٪ تخفیف خرید آنلاین و حضوری
✅
خرید تو ۴ قسط
✅
امکان خرید نقدی با امکان بازگشت وجه تا ۱۵٪
✅
امکان خرید از بیش از ۳۰ هزار فروشگاه
✅
خرید از بیش از ۲ میلیون کالا
✅
خرید راحت حضوری فقط با اسکن یه بارکد
☀️
برای شروع تابستون آماده‌ای؟
😎
⁩⁩
⬅️
از لینک زیر خرید تابستونت رو انجام بده:
👇🏻
https://l.snpy.ir/auukx
https://l.snpy.ir/auukx</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/664351" target="_blank">📅 20:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664350">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a2aed935.mp4?token=P0qTz7J6onDvm-nhxFTeaQ2-WF6yHIQqB0iC2hrneoFuxp0vAojftuTSYYLzw47Wd87TWDQHtGH6BmhRO4n0OU1jGmkTYxanemcX8vGKSuRjZmyZZ6OvCiHcDD5AB_c6ZRtpKKFRFjkIerRkdyh5RDSW-ADMEB7QSIjtUYDBacS3J4tLUtjQOJSpFxNwLiKtPWnribx6MXPeO_dERaxC6WcyqGAyDoTQVgVbwgecB1zKNtFvmyvKJRAj_8hN2uHes8lN1uqb4nuYYNTvvRR975Aa1KuXH-uU0uiabMlgn6jnzypKAJX8KSoPtGgs5gJK5nBBhb8ZI_tILwyCGJre_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a2aed935.mp4?token=P0qTz7J6onDvm-nhxFTeaQ2-WF6yHIQqB0iC2hrneoFuxp0vAojftuTSYYLzw47Wd87TWDQHtGH6BmhRO4n0OU1jGmkTYxanemcX8vGKSuRjZmyZZ6OvCiHcDD5AB_c6ZRtpKKFRFjkIerRkdyh5RDSW-ADMEB7QSIjtUYDBacS3J4tLUtjQOJSpFxNwLiKtPWnribx6MXPeO_dERaxC6WcyqGAyDoTQVgVbwgecB1zKNtFvmyvKJRAj_8hN2uHes8lN1uqb4nuYYNTvvRR975Aa1KuXH-uU0uiabMlgn6jnzypKAJX8KSoPtGgs5gJK5nBBhb8ZI_tILwyCGJre_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در یک دقیقه سبک‌های مختلف نقاشی‌ را
یاد بگیر
🎨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/664350" target="_blank">📅 19:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664349">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
توقف مذاکرات واشنگتن و تهران در سوئیس
ادعای وال‌استریت‌ژورنال به نقل از منابع آگاه:
🔹
مذاکرات برنامه‌ریزی‌شده میان واشنگتن و تهران که قرار بود این هفته در سوئیس برگزار شود، به دلیل ازسرگیری درگیری‌ها لغو شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/664349" target="_blank">📅 19:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664348">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ستون نویس بلومبرگ: تردد کشتی‌های حامل انرژی در تنگه هرمز تحت نظارت آمریکا
ادعای خاویر بلاس:
🔹
چهار کشتی (دو نفتکش و دو حمل‌کننده گاز مایع) با سامانه شناسایی روشن، در حال ورود به خلیج‌فارس از مسیر عمانی هستند.
🔹
این ترددها تحت نظارت سنگین نیروهای دریایی و هوایی آمریکا انجام می‌شود؛ واشنگتن در تلاش است تا این مسیر دریایی را باز و فعال نگه دارد./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/664348" target="_blank">📅 19:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f218dcc87.mp4?token=mf9FNJQlUED4oHSKvtIFL_peIfP8J8zqkXYFaqrwfw-3DK_6qf4ClW3YzU5AhChpuUQZeDYAlqMrbq9QiJMpbBonHK71i2V2QiNK0Xt0IGzMFVdsJSfnCwSkcsdRPsWeUaVHfjrz1PJiQJx44TiuEk1-7DJSovOt7ByP32hAXrltrw7a2kVOfD066aqogDEmcincXyzoUksdSkkRdR0Ezi4trhTNdJhF9Iee6hTFOnx2hB7tp2L7Fa8SoUs-Hgk5c5uDiI0cWJ4pUhZJnkZA87zZMlDELsCzVidk65cF7VHGaPXjA6VpG6xNvKAtLQCUYXuTXOQvgxdufJp2kCA2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f218dcc87.mp4?token=mf9FNJQlUED4oHSKvtIFL_peIfP8J8zqkXYFaqrwfw-3DK_6qf4ClW3YzU5AhChpuUQZeDYAlqMrbq9QiJMpbBonHK71i2V2QiNK0Xt0IGzMFVdsJSfnCwSkcsdRPsWeUaVHfjrz1PJiQJx44TiuEk1-7DJSovOt7ByP32hAXrltrw7a2kVOfD066aqogDEmcincXyzoUksdSkkRdR0Ezi4trhTNdJhF9Iee6hTFOnx2hB7tp2L7Fa8SoUs-Hgk5c5uDiI0cWJ4pUhZJnkZA87zZMlDELsCzVidk65cF7VHGaPXjA6VpG6xNvKAtLQCUYXuTXOQvgxdufJp2kCA2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای جالب از برخورد صاعقه به برج ایفل در فرانسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/664346" target="_blank">📅 19:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqIaZTtysxUjJ80pD7OcW5RbhNWwGZ_k_AVqCPGYoc4vBuQeEZLOdKM9-QA_Ptof00_NXxGUMR4ymAFO9AsfAcdIPfzC8_U7ZXvaMjnPSsK7YXeEhvZJs4I8tU0r_i4ackhnYyuV-MibdPVt4_eAFM3Vp5tpKYPCRxGAYTyQlnMHd8qUg6ZMiggmU2zmw_7URBYCIuSeMfekXCnudQFLRAnc9zGHgI6d4q65GDV6GHRLaSU2KkKnHzgi-_FPQFJ_3qku57h0cT3DNigNbQcxpDorAL4ecCjcBl9i3nbCQnpP6aEjgIfMSznXS4Up0beIl_bI3Sd6pMjKH-7_HVs99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش جهانی دسترسی به برق در مقابل بحران دسترسی در آفریقا
🔸
شمار کل افراد محروم از دسترسی به برق در سراسر جهان از ۱.۳۵ میلیارد نفر در سال ۲۰۰۰ به ۶۷۵ میلیون نفر در سال ۲۰۲۳ کاهش یافته است.
🔸
برخلاف روند کاهشی جهان، در منطقه زیرصحرای آفریقا آمار افراد بدون برق از مرز ۵۰۰ میلیون نفر فراتر رفته است.
🔸
بیشترین موفقیت در این بازه ۲۳ ساله متعلق به منطقه جنوب آسیا بوده که توانسته سهم بزرگی از جمعیت محروم خود را به شبکه برق متصل کند.
@amarfact</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/664345" target="_blank">📅 19:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubEDVGqDbOqxwKB9wBpbbrwPt5Rstb_QhjxR21MCPLz4ZZfPEV3h0W14dd-SLBRVcXgHt2J9ziVe8BcgjdpaFxgZ2SWSvOZ_gMVV-AJZPs24-hW9gD8dnkaasekjAn4AzQf652dDl5E9Ko98BuP_MKvV4CMZ2sHJQ33lb-DgNbu1ZYaLEBF8sxn60LYESdE_VVhbtw9qRBcYCZ9Dyg1XzNJxXx4nvioKRV9zLPj78yeSbwLoed4pnaf1IKVxcowzkg7ISRBtLC-lWpcLq7LPl-h5HgHa3zlIGYXYTJCgsOA9kOzDtVzGH_u1aM75PLu3YIP1SBcM6-LRQgScnFoLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صف پمپ‌بنزین‌‌ روسیه‌ که در پی حمله موشکی اوکراین به پالایشگاهشون اینقدر طولانیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/664342" target="_blank">📅 19:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664341">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c8332b4.mp4?token=PWABwZxQVAIyyes3ZncggkDftgbaCh5CU-gCSs45stfy23-bSF8EIzrJ7LqoEIfgFgA1e1sV1nl9koW6vBOW9CFcsRhTWNYx3fevTrm3w9gVbBemBjZmYwiPkhIna2xioShpTugMTMkj9jvf4-XPPubaZ4Ib5K6h-4n5S2LAnFJF4_tFCP_oal8fnx11xtvSLFmn9AiK7izm4PZ3QBKJO5Rpwy-OKZVP2hBQ7f94es0zEOKDdBoWhwdIDuAQjdDKk9qn_rdVfryW3xaLVS7V5mIGHDd9TNkO68rd7uSkLJdFKSwHE5nag-T477-2DdtHurqFYRdEseBb7j-C6sSlxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c8332b4.mp4?token=PWABwZxQVAIyyes3ZncggkDftgbaCh5CU-gCSs45stfy23-bSF8EIzrJ7LqoEIfgFgA1e1sV1nl9koW6vBOW9CFcsRhTWNYx3fevTrm3w9gVbBemBjZmYwiPkhIna2xioShpTugMTMkj9jvf4-XPPubaZ4Ib5K6h-4n5S2LAnFJF4_tFCP_oal8fnx11xtvSLFmn9AiK7izm4PZ3QBKJO5Rpwy-OKZVP2hBQ7f94es0zEOKDdBoWhwdIDuAQjdDKk9qn_rdVfryW3xaLVS7V5mIGHDd9TNkO68rd7uSkLJdFKSwHE5nag-T477-2DdtHurqFYRdEseBb7j-C6sSlxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری مورد پسند امام زمان چه ویژگی‌هایی دارد؟
/ مدار
برای تماشای این برنامه کلیک کنید
👇
https://www.aparat.com/v/dod34p6
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664341" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9pLr-UD8-Oesq_U7p133DF59PFwdkSGkgrHL4YahIfTdlr2p0nKn-m3vanFyTEc5-uLmxbGOMcn9S9RYfJmjCMuxahwbs48Zf7pSHKFV5wLWDTOh2CuDJD9PgtlajHy-CfxXLUCWU5qBQz9YBif3FUoT2xdkg3quT_wreWWY1WLMCz3Jy3EK3nnE-Cjzd8M8r8DSuzObbWvfl_5ueXXwvnAev0cL2Z_MIVzEzaMlER94KWddbHVTMNOThef1KR7NRRO_SCtc__QYxUIUtnExeqL_cjVMnL8T3OgSSQFDdfmI5TWBO0z5T3U-5mykh0ErWH0bCIZRsDZznmtj3vLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQK8PXGSUOQQSRrDRg9HduoTWj0UImBVX-aGM3cEpj1v8WDoRjRlPOK0ULgJlYQ3lH4XcNNrKmzz722iriD0GMpi9KcXqvcq1zWnUTw3nLIvj8SnlmplLmE_tUGwi9Vk_YbkXWtoM1ehJfjchwyXv041_3XWTCD9crgouDxDzfaCBajktIghdFXgnzW9rGBfma7JLbNCX8QcCvyh-IR_3jKMWZc3q_Q2AyrLBa2mBDhfD1GuQUu71jCSIJADgPtZB66r_UooNPsupbfNhG6U3lDRKilB8mGAo02-NlVPc2uU8jammo5Wqs4DTN3htqd5T4Ta2yCd4Wn7lcTQTK16Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRxHtUaXDlPLxAfmpP2q5Fim0t1MmvsUg2Z7QIK6rOIwQ4n3Fgif0D0kqtJuULApAnD2Fz6euBvnMWzD2_Fxim5it9lrd_lNp7Z7BMCtmmcwbMb5ZovQQmv2Spq9QGyZMuVDw-ryOEfHNsVFnawzf3scxwyrlqOlZFJYkptJTtLbBufyuR1ZH8_dIy5A57tj9J0cS9PjOmSs35iRkoIPoLuFpZOeDJRuyNw-wgLSVK4Qf7g4tni4P4YpwzZgZ9wjnFOQBuxO9qWVzc3V87zFzTnihVkv8LtG31ucjy-yO0_qs2SJx4pvdomm2ZrMzLI_bNCg-WSdyn6LeGa1CBKqQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش فعالان رسانه‌ای بعد از انتشار پیام رهبر انقلاب
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/664337" target="_blank">📅 19:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664336">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZQJzjcmcU1ipyIAfUCZzXempLMINftutH5hRJicpWZJ03aMBcTOagtH_k3SRkE2B5U8E_l_JXf50rf9_ONEq-he_U1qbV6eM3ZwrvAjAT_xx5TKXW5EuaEzOrz2ZSJEmgaJE05BJzSgsg2DiFXeX9F33mvZktG3JILxD74giFtZ0zT1ZkEijc8v2XME3Lcxg-ai6_haAMbf9NIF7RlHdC9acKSyNKpRxgqlbCOB4Pn4eufgt0MJ5rYvLo9voWZT3IoFVi34PcqMoh66iOebEbd59ZppOMawkboZdYSSgsGsprV3-4TYMuKdA8AusM_GE0DQhJ3BNaF-V0fuV6CHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز سلامتی در یک حبه سیرترشی
🧄
😉
🔹
سیرترشی، فقط یک چاشنی خوشمزه نیست؛ اگر چند سال رسیده باشد، در طب سنتی به‌عنوان یک ماده غذایی ارزشمند شناخته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/664336" target="_blank">📅 19:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664335">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz5a1pSlZ7J3fLttkEJie81Qo6-6pyjFQkXTfY4TvSVRZI0gSx_zW6KiFK9Bazu6yIEib5lg4WRRK2H2frLh9rLlvCgGQUcM-L6nX-ftw6qM_2F10bMhelFiTrtZDpIOmH4nRbD39QvowAD-CF61yHwLWUybao8Z2ncw9WwLiEaaOKqLMh_Nv5JffZO7X7YwNL9F2X89E48wSjN3cSeuinw_r-Q1UbHgFM-nFI_mk4mc2KazbTYZFSAgHewdu--MufZ0g5ngCgfAUpqJe6emVtg079jN6suACNLlmC7wqRe46bOXoXThhYbD6-Dg1PpzHfdEDpA3MwN66LVBUpQMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/664335" target="_blank">📅 19:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664332">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
قیمت غذای دانشجویی آزاد می‌شود
🔹
از ترم آینده، یارانه غذا مستقیم به کیف پول دانشجویان واریز می‌شود؛ دانشجویان نسبت به تورم، ناکافی بودن اعتبار و محدودیت مراکز طرف قرارداد نگرانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/664332" target="_blank">📅 18:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664331">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
افزایش ۴۰۰ درصدی تعرفه برق کشاورزی!/ ۹۰ درصد مطالبات گندم‌کاران پرداخت نشده‌ است
سلحشور رئیس کمیسیون کشاورزی اتاق بازرگانی مشهد:
🔹
تعرفه برق کشاورزان در برخی موارد نسبت به سال گذشته تا ۴۰۰ درصد افزایش یافته است. تاکنون حدود ۱۰ درصد مطالبات گندم‌کاران در خرید تضمینی پرداخت شده است.
🔹
قیمت نهاده‌های تولید اعم از کود و سم و لوازم آبیاری تحت فشار، بیش از ۱۰۰ درصد افزایش پیدا کرده است.
🔹
عدم پرداخت به موقع مطالبات، می تواند باعث کاهش انگیزه کشاورزان برای تحویل محصول به شبکه رسمی شود و ️این موضوع می تواند پای دلالان را در موضوع خرید گندم باز کند./ اخبارمشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/664331" target="_blank">📅 18:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664330">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4209601e02.mp4?token=rVCk0oRfed4SNpKVXM9JOWHNw14Z_2qby-uhVGaK_C87YEb46uqKGVyEuKCoH8S0-47ckZaZ3t1XT-N-GRnW3C8CMBm7nu-xpBsdiSxslmF7gIczMIGoOfVaTM530Nk8ICSkO0S0l93E6OXol6bXzkIK5nRZqGtGNSXX-Lb2UIomi7eYM4gmL-7qNZeor_P4rgGiue4kawsKkj7Bn0aCUCD5tskKIg0SHoLiUE1kVOGhqqftNwf9x9lIVawi9OPsWB24FjHnMMlFcgCfl-mUYBFds2oBDIHaMm8M9BenJVjpH4tKAHrWHxSAZjNQazCHojb9ZD2GcruMcUScJ31WOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4209601e02.mp4?token=rVCk0oRfed4SNpKVXM9JOWHNw14Z_2qby-uhVGaK_C87YEb46uqKGVyEuKCoH8S0-47ckZaZ3t1XT-N-GRnW3C8CMBm7nu-xpBsdiSxslmF7gIczMIGoOfVaTM530Nk8ICSkO0S0l93E6OXol6bXzkIK5nRZqGtGNSXX-Lb2UIomi7eYM4gmL-7qNZeor_P4rgGiue4kawsKkj7Bn0aCUCD5tskKIg0SHoLiUE1kVOGhqqftNwf9x9lIVawi9OPsWB24FjHnMMlFcgCfl-mUYBFds2oBDIHaMm8M9BenJVjpH4tKAHrWHxSAZjNQazCHojb9ZD2GcruMcUScJ31WOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رضا پهلوی: حمله آمریکا و اسرائیل به ایران حاصل اقدامات من بود
رضا پهلوی:
🔹
یکی از دلایل عمده برخورد جهانی با ایران به ویژه حمله آمریکا و اسرائیل حاصل سفر ۲ سال پیش من به اسرائیل بود و به آن‌ها گفتم مردم ایران دشمن شما نیستند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/664330" target="_blank">📅 18:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664329">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKDrE2JrL4kvfe9xBUqPDNw3-uaQd0lZnrgHnQLCIt8SrGpCYMSsM8gfFzt5PHfKEwB9ytccwSyVpRz8_8rOKHSF8BBgNjQqFG5dDssLW6IrBrIarwh2JixS9lQBwlZGiTXrB4McTLa2WHTb0KzP2RExhF_U72c7eV7U8tbbO8uCbcMlAqwiaBw5xTwWw2ky7vfcQjYbC6XFAW3-nAvKG_Fol3DBWoVlooRwQzzaNT75VnBMxgZdIKjICGPSCdfZv7U2yHFBFjbOtHsBwK-is7X0gyK9C7C8mh4tkcklVQ1Qzx-Kjx-dyRp8VvIcugf7he1et5MflZZfx22F5kpu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تایید صلاحیت برای خرید تلویزیون در دهه شصت
🔹
دهه شصت خريد تلویزيون سياه و سفيد مستلزم تحقيقات بود و اسامی واجدين شرايط از طريق روزنامه های كثيرالانتشار اعلام می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/664329" target="_blank">📅 18:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664328">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32592ca1dd.mp4?token=LXKmYZmXOWIhEBKa88QDHpaJu27b_LllnZy3KRADuh67tu7etvjaneXIm8HKnH-PsSUAhB9IQ07mBX2R6fNDg_5KjkHSarQFKX82yiPMRMzq8vdYM1VrkJM2ASSTJsy9pZXUuXcq1QAABd-HZwydhT0KITlAK1-861oTxbwFOe3ErY7pZZ57kL3byAEmzBKWXWVuJKQhKRdDjidM_rTD9LuoLVF5tpCCTAtUV8aOzmM5EXj3Mb9tZ-xkB_x0aiYheifaFyXWZRk_9W4Ks5m7QSKkYdpjxegVWwFiSFURP0Og6_O2JCbyCluwD4Ec6wLAzqOFHCynqsOPZ9dfqzmfyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32592ca1dd.mp4?token=LXKmYZmXOWIhEBKa88QDHpaJu27b_LllnZy3KRADuh67tu7etvjaneXIm8HKnH-PsSUAhB9IQ07mBX2R6fNDg_5KjkHSarQFKX82yiPMRMzq8vdYM1VrkJM2ASSTJsy9pZXUuXcq1QAABd-HZwydhT0KITlAK1-861oTxbwFOe3ErY7pZZ57kL3byAEmzBKWXWVuJKQhKRdDjidM_rTD9LuoLVF5tpCCTAtUV8aOzmM5EXj3Mb9tZ-xkB_x0aiYheifaFyXWZRk_9W4Ks5m7QSKkYdpjxegVWwFiSFURP0Og6_O2JCbyCluwD4Ec6wLAzqOFHCynqsOPZ9dfqzmfyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
سپاه چه مراکز و تجهیزات آمریکایی را هدف قرار داد؟  سیمیاری، کارشناس مسائل امنیتی و نظامی:
🔹
در عملیات امروز، ۸ نقطه مرتبط با نیروهای آمریکایی شامل شیلترهای راهبردی، مرکز کنترل و داده‌پردازی دریایی، برج‌های دیدبانی، سامانه‌های راداری و ارتباطی در پایگاه…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/664328" target="_blank">📅 18:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664327">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4gvComh7LxssjwkEqz37i94cql-nMlrTh92nziclDdW-uhs4E2ivZS81QCUOePhQpt2CGs9A8O6TXBladtBDsz57HI3xspsnRfXZ3j399kceV_GVbWOqdX3Jtg-AYiIxiGMLH_4QV-KSXfC4_C3UfvLtH_AItUlikejqLcYkkaBO7xqlFDN7xgWlZitU9BKcC4qQe4Bn2aoZqRIoPsYzsyhG1HSmZxumRkiReULe8DEJ2hMVQf9hlUeSn7V51Hpav-htA2BG6tIqR4uyBnX2j4zmUQbgEz6_XOMXmHM256p1ge-k6WQWK6mSl-rZRy4QE4s5P4Bna3dl3lhqbY-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حسین صدقیانی؛ پدر فوتبال ایران که احتمالا او را نمی‌شناسید!
🔹
او اولین کاپیتان و مربی تیم ملی ایران و از پیشگامان فوتبال کشور بود. فوتبال را پس از آشنایی با این ورزش در اروپا به ایران آورد و نقش مهمی در گسترش آن داشت. صدقیانی پایه‌گذار نسل نخست فوتبالیست‌های…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/664327" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664326">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07250fe20c.mp4?token=li6CjlA5XE88srbJGzODPoqyzJWV-4D1nZoLjQdaReh1CJOc2lrkKJsiDGhHW7lh7DMYOdD62twskWRE_g3v-7_bP7cTBc7u1QI3FrNO86GAwKALpX0Soo1V3CkThxMGIVIhJ_B1koh7kW5L5Zz-y4mECgyhE1NUpkyXm3Q_s0LIdUOAg3e3IduIXxG4CRpccIz_7KT7Xxj29GAPf5d9vQawJ-jPc5fQWYTotX0errIb31rXQE5KehWF0abYhWydTQJMTuwlLYqI_XiEtnFN_ozTRQIzMFZWJ3B1Tcrytntz_kF4xsfSfNsZtnxZYEVyo9rBwUtVmISvaKJbVPfvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07250fe20c.mp4?token=li6CjlA5XE88srbJGzODPoqyzJWV-4D1nZoLjQdaReh1CJOc2lrkKJsiDGhHW7lh7DMYOdD62twskWRE_g3v-7_bP7cTBc7u1QI3FrNO86GAwKALpX0Soo1V3CkThxMGIVIhJ_B1koh7kW5L5Zz-y4mECgyhE1NUpkyXm3Q_s0LIdUOAg3e3IduIXxG4CRpccIz_7KT7Xxj29GAPf5d9vQawJ-jPc5fQWYTotX0errIb31rXQE5KehWF0abYhWydTQJMTuwlLYqI_XiEtnFN_ozTRQIzMFZWJ3B1Tcrytntz_kF4xsfSfNsZtnxZYEVyo9rBwUtVmISvaKJbVPfvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگفتی مهندسی در ژاپن، تخریب ساختمان بدون کوچک‌ترین صدا و آلودگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/664326" target="_blank">📅 18:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664325">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUm8PVgyQWqek8p1ZGqtIyxeSUQa5GrbFYdm4lZx-lP81BvRfvX-B7ss5WM_waLFIruXZysYstsB0-apfmgWzBjy0ihurvzbTV8aAfcZz8LxLcc-IvApCUZbKrODZoOhroPc8FoI2QD1FCP-B6R7vBpvU7ILStvoSVvqzpN7fOdoYj11Cj3SbqUnKaxlppNNvy1FRF3flaeMnKLxyDdj2mWdnm8uJ4bofYvsf5lZB6lZQax_6xG0URn32vTeg5JC-1Tmhpp-veGohiwNZOjxUsnSrtYHteHOaieFrTYc0m2hWGum17eVX5__w-oj_JojUuDwAN1H4KU38tmFxDbBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
@Badragheyar</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664325" target="_blank">📅 18:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664323">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 اگر برای انجام کاری به یک اداره دولتی مراجعه کنید و احساس کنید حق شما رعایت نشده، معمولاً چه می‌کنید؟</h4>
<ul>
<li>✓ پیگیری می‌کنم، چون از حقوقم اطلاع دارم</li>
<li>✓ فقط کمی پیگیری می‌کنم چون روند آن را سخت می‌دانم</li>
<li>✓ اطلاع زیادی از حقوقم ندارم؛ همان روال را می‌پذیرم</li>
<li>✓ ترجیح می‌دهم پیگیری نکنم تا کارم به مشکل نخورد</li>
</ul>
</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/664323" target="_blank">📅 18:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664322">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a900854f.mp4?token=kJSPPoWLmCpDZRZIAvzSNBfMHgSm0J3gYaFnjZQUNkrbH2Na42TNMOZiK_FloNlxpGxxto8i4FS4py3b27G4MEMoce5SYe-MVRAbdwt0PnrX0TFXgtBjNHDkwz3Mcn-LanMIZHTWkSQKzITH8825lFUhI4ExfcWJKwyfk-6f5d-im86mdOlyuucGGaMU6oB4BPhgzm4MJdVtt0MBPRRmdAw5lDzDp9G9BBrT2xNUZ-YWdrDYjgRGYXGpWquEHcKK4XP6yV1lg1JFdf3cEkFfq629VjNtasNKWH7ZyRW6gcJ3lgIOt_zH5pKdqBQuifo_pPRdt5pGXQyLPL6EP4RFpwXjwdLu5wgVy4mfo1Z42j8WWpjpbXr6H5e-2vOP50GFo4n7B58AJcxRtl314l8OkbLLj_NLfwXT4sQq7esrGz7ORW7PNtBbjzzU9Ay4_PQdnjxiG9yRBUmGkaZYmVBp8UIfN3WdYDAaF6xvUr-UNs-_HEgYyCzzludJTFkT3jo48GPUtKqvqEdg7YVYLsAqVXIewq-z6N9l2gbSyXOfpV1OGOEdSP3Fjbt-w7A52E_DfkSlp3QYU_i-rUKHjdxljuboDsi18i-u1AZtI3Rj50yLGoYrCokGw1dic6HfIXwzZkPNW_EU3d34ULukHZO3kQPCfSkQNBM4rS7A2e_GoPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a900854f.mp4?token=kJSPPoWLmCpDZRZIAvzSNBfMHgSm0J3gYaFnjZQUNkrbH2Na42TNMOZiK_FloNlxpGxxto8i4FS4py3b27G4MEMoce5SYe-MVRAbdwt0PnrX0TFXgtBjNHDkwz3Mcn-LanMIZHTWkSQKzITH8825lFUhI4ExfcWJKwyfk-6f5d-im86mdOlyuucGGaMU6oB4BPhgzm4MJdVtt0MBPRRmdAw5lDzDp9G9BBrT2xNUZ-YWdrDYjgRGYXGpWquEHcKK4XP6yV1lg1JFdf3cEkFfq629VjNtasNKWH7ZyRW6gcJ3lgIOt_zH5pKdqBQuifo_pPRdt5pGXQyLPL6EP4RFpwXjwdLu5wgVy4mfo1Z42j8WWpjpbXr6H5e-2vOP50GFo4n7B58AJcxRtl314l8OkbLLj_NLfwXT4sQq7esrGz7ORW7PNtBbjzzU9Ay4_PQdnjxiG9yRBUmGkaZYmVBp8UIfN3WdYDAaF6xvUr-UNs-_HEgYyCzzludJTFkT3jo48GPUtKqvqEdg7YVYLsAqVXIewq-z6N9l2gbSyXOfpV1OGOEdSP3Fjbt-w7A52E_DfkSlp3QYU_i-rUKHjdxljuboDsi18i-u1AZtI3Rj50yLGoYrCokGw1dic6HfIXwzZkPNW_EU3d34ULukHZO3kQPCfSkQNBM4rS7A2e_GoPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع کوچ اجباری مستأجران به حاشیه شهر با شروع تابستان!/ دستگاه‌های نظارتی برای کنترل اجاره‌بها توانایی لازم را ندارند
/ مدار
این گفت‌وگو را در آپارات ببینید
👇
https://www.aparat.com/v/gqj0f3m
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/664322" target="_blank">📅 18:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664321">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">گاهی قشنگ‌ترین روایتِ نذر، کنار هم بودن و از دل بخشیدن است..
تهیه و توزیع شله نذری در روز تاسوعا توسط جمعی از همکاران خبرفوری
اجرتون با صاحب این روزها
🌿
#هیئت_قرار
#گزارش_تصويری
| تیرماه ۱۴۰۵
@Heyate_gharar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/664321" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664320">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
♦️
سپاه چه مراکز و تجهیزات آمریکایی را هدف قرار داد؟
سیمیاری، کارشناس مسائل امنیتی و نظامی:
🔹
در عملیات امروز، ۸ نقطه مرتبط با نیروهای آمریکایی شامل شیلترهای راهبردی، مرکز کنترل و داده‌پردازی دریایی، برج‌های دیدبانی، سامانه‌های راداری و ارتباطی در پایگاه علی‌السالم و ناوگان پنجم آمریکا هدف قرار گرفته و منهدم شده‌اند.
🔹
سختی بازسازی این مراکز باعث شده که پنتاگون دنبال اسقاط بسیاری از مراکز تروریستی در منطقه و نیز تغییر محل آن‌ها باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/664320" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664319">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77125ab336.mp4?token=WQs8LrTsWvwbgzuXDbNuV4jaxkY6AtmqY5oHwQ1faaUav1ju41UBntPr6qFwtspUX4b4p6vxP_1dd830oVtfjJppuUDhVGmXN0EEEXD_bAGae44k-0b5izGC1aao4uoJlZjV3cfRsg0lPPLTBHbc6ro48ppOiWxrCE2TmeUAcgsZvISVGF_XEN-Qeezy_5nF8LectNiLbqawUaE3ahrDCHWpYa-Yt06WCrIPBSEw59WdPRzk7lml1YIxoYXjo3_rRv0FqRUhJQZGqZLFDCimxLgtOZichoc6Lh3HIX3jR_lKUAZx3AHMz7hvdd_muKwDABuOz1fddIUknojSQraE4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77125ab336.mp4?token=WQs8LrTsWvwbgzuXDbNuV4jaxkY6AtmqY5oHwQ1faaUav1ju41UBntPr6qFwtspUX4b4p6vxP_1dd830oVtfjJppuUDhVGmXN0EEEXD_bAGae44k-0b5izGC1aao4uoJlZjV3cfRsg0lPPLTBHbc6ro48ppOiWxrCE2TmeUAcgsZvISVGF_XEN-Qeezy_5nF8LectNiLbqawUaE3ahrDCHWpYa-Yt06WCrIPBSEw59WdPRzk7lml1YIxoYXjo3_rRv0FqRUhJQZGqZLFDCimxLgtOZichoc6Lh3HIX3jR_lKUAZx3AHMz7hvdd_muKwDABuOz1fddIUknojSQraE4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی سازمان ثبت اسناد و املاک: کسی اگر در سامانه ثبت اسناد ادعای دروغ کند به ۲۰ درصد رقم ملک مورد ادعا جریمه خواهد شد
🔹
قولنامه‌های مستاجری زیر ۲ سال نیازی به ثبت در سامانه ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/664319" target="_blank">📅 18:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664318">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0688eec0e.mp4?token=J_zF86ya1XD22Bfj1YR82MygTb7hZtPvKNXQSfWA3sqe9Y89C0ffP2UGv3W7q_7_FQNeo82s66pUbQvNC6feQpccouyQiwpXghw281-iLK9Gjn5MEANzTpAxd_D2vIaBAPdPdTZzdmaC8AZ7q8f4kY3Sw5ZQqo5Ns5esmztWMOrGaPMzzWYrqpCmSBnEBSx75uQ--6Xlbg6zYv6jiR6IDRYQZEm8PTU-9iXRTMiXIQVxsU6cwLCW33gE16hitdL841q9MysP9Md9syCp5gvG1Q5ZsbXyD2TSPdLYZE2DjGefMbqdtR-jS8swyIV85-DKZSwF5-Skdi9DmjU-BN8u7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0688eec0e.mp4?token=J_zF86ya1XD22Bfj1YR82MygTb7hZtPvKNXQSfWA3sqe9Y89C0ffP2UGv3W7q_7_FQNeo82s66pUbQvNC6feQpccouyQiwpXghw281-iLK9Gjn5MEANzTpAxd_D2vIaBAPdPdTZzdmaC8AZ7q8f4kY3Sw5ZQqo5Ns5esmztWMOrGaPMzzWYrqpCmSBnEBSx75uQ--6Xlbg6zYv6jiR6IDRYQZEm8PTU-9iXRTMiXIQVxsU6cwLCW33gE16hitdL841q9MysP9Md9syCp5gvG1Q5ZsbXyD2TSPdLYZE2DjGefMbqdtR-jS8swyIV85-DKZSwF5-Skdi9DmjU-BN8u7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود و غبار دوباره بر فراز کارخانه سیمان تهران
🔹
فیلمی که امروز از محدوده میدان غنی‌آباد ضبط شده، انتشار حجم قابل توجهی از دود و غبار از محدوده کارخانه سیمان تهران را نشان می‌دهد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/664318" target="_blank">📅 18:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664316">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
بیانیه جمعی از اعضای مجلس خبرگان رهبری پیرو پیام راهگشای رهبر انقلاب   بسم الله الرحمن الرحیم مردم بصیر و انقلابی ایران اسلامی با عرض تسلیت ایام عزای سالار شهیدان و اصحاب باوفای آن حضرت و آرزوی سلامت و طول عمر با عزت رهبر معظم انقلاب اسلامی(مدظله‌العالی)…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/664316" target="_blank">📅 17:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664315">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
گرما در فرانسه نزدیک به یک سوم جنگ ایران و آمریکا کشته گرفت
🔹
مقامات بهداشتی فرانسه اعلام کردند که حدود ۱۰۰۰ نفر در پی گرما در هفته گذشته جان خود را از دست داده‌اند. این درحالی است که بیشینه دما در فرانسه هنوز به دمای خوزستان و سیستان و بلوچستان نرسیده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/664315" target="_blank">📅 17:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664313">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2EGZqYSchc7sSGPXjS27Xu7IYVWmheHx_X4BEzW5x3nXNGApP4ZEegMt660AvBh-P9lTZwXpEZ8ALIUMcjtU3f1wGC3FI92iqQSmN-iqK9vkHKaBU1ddW1iv4b27zZizsLWEWAKZuk69Vj0x355UARzjiBJaxl9VWXCq8C5uUJzqQAwhFdjcWQQBi0nZhWPTlicRIgAOFVI3oSYeoACdYEJrBx2I_8oHkOaANx_11P6P-zpSuZ3JjDRAPXMXLPW6IfbRW1XGdDQm-515U5mIgoRek3aiVsBmmD4wckvmhSDUeO6woNcVKFx1P2W6L79ygh4VSeltPlNDOmgOk_s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uac6isuWphyOWlqc89FMnksSTCx2PRyqyPNftkWjLmalNEHXmojvgwx9s1MMEMipbbl7SauU_mFdtaiaWRpsr69R0l4VIlN4Y_QTPhe63qz658w-O0XPHcYY4dRRvz8nekSBtOG9HwUJLn51BcwrADahUTAgtmNtxiI7qfr6Sqsz-kVXF3XD9q_tL5meXo-Y_vTD1op2zDyr34z6UUYLd9VDFCj8YSJkOBKDTcqq3LDcJIOKRilCXhf2ZhTw5TD0QeqbHqJM7wpcpQ6ADhdzUhO-Qcdn5x9l5o3zhMqK8okI7GDJ4M7mDi_ZMOP6unRv8SjsYV5o6V52zaBtEOHzdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قایم‌باشک زیر شقایق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/664313" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664312">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iooNyZVB-3YV3SGFI_EH1cGurDVxioVj07j1IOOc8uzDbo4KBgbYK4Nv3Dq9ruMqvwwViyA4XgYNClsLTsz_NyLCTCOFgo7ZKhHouQKs-hte1VdlT-a5rXwMW75e5NJR6b_DGCbEfDExYVaCVaVe9nhXLkfuGMDPkmy2avzbXcOPNmghwWRv8L7lYAuyw2NaOJwvgEyz66n5DQIAhCniIKkg7yw0Ha_t-8bSjBLLNpHND0wDcNzHkS2Drdwgtql_3ukup8S7ECT-tVVsPfFneMDBkI7rv9ewWqp67n2Qgy93fw3_OlNyOZ1sTwkkPZysv_tScp0D7OGmwowOBBx7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت بالکن، ایوان و تراس در آپارتمان
در یک نگاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/664312" target="_blank">📅 17:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664311">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پایان ست چهارم | برتری والیبال ایران مقابل کوبا
🔹
ایران ۳ -  کوبا ۱
🇮🇷
۲۵ | ۲۵ | ۲۰ | ۳۰
🇨🇺
۲۲ | ۲۱ | ۲۵ | ۲۸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/664311" target="_blank">📅 17:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664309">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تکنیک جدید وزارت نیرو برای کاهش اعتراض‌ها به قطعی برق؟
🔹
گزارش‌های متعددی از قطعی پراکنده و بدون اطلاع قبلی برق در شهرهای مختلف منتشر شده است.
🔹
بسیاری از مغازه‌داران می‌گویند این خاموشی‌های ناگهانی باعث از کار افتادن یخچال‌ها و اختلال در زنجیره سرد فروشگاه‌ها شده و خسارت‌هایی به کسب‌وکارشان وارد کرده است.
🔹
پیش‌تر معاون وزیر نیرو گفته بود که نگرانی جدی درباره خاموشی‌های گسترده وجود ندارد
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/664309" target="_blank">📅 17:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e2f8e78d.mp4?token=UMkO7USLefmrET5teKQUWb9D4udVTwZo7F2VOvwmD05jNLnwcvDeozJrottn9jmbB8jQOFfFuVQSvps68isss9bk5s7j78_0MFItP1D5c6lwYKlZXfSElWr7XiFdZKOCYufMqlO00tjU4mMKyObT9_EKqzq6PWi3D-Hq8u9n6tuqoiuSInviSMosTyjG_EUzhy5pLQ9ch3gJLGjOBDZtF2Lvp6h0Eax3aH5UDOBJen0Glw1Xpuq0uSUC9lu1CEXMX0m-mGfvGnCruFJsjFdl44UPjnPxjRgwlJUItJG4u8bn6SqI0RuujYq5OYXhiVDSHgKfzBo9_0bZCKhJwRYmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e2f8e78d.mp4?token=UMkO7USLefmrET5teKQUWb9D4udVTwZo7F2VOvwmD05jNLnwcvDeozJrottn9jmbB8jQOFfFuVQSvps68isss9bk5s7j78_0MFItP1D5c6lwYKlZXfSElWr7XiFdZKOCYufMqlO00tjU4mMKyObT9_EKqzq6PWi3D-Hq8u9n6tuqoiuSInviSMosTyjG_EUzhy5pLQ9ch3gJLGjOBDZtF2Lvp6h0Eax3aH5UDOBJen0Glw1Xpuq0uSUC9lu1CEXMX0m-mGfvGnCruFJsjFdl44UPjnPxjRgwlJUItJG4u8bn6SqI0RuujYq5OYXhiVDSHgKfzBo9_0bZCKhJwRYmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعتِ صفر؛ تقاصی که گریزی از آن نیست
🔹
ما نه فراموش می‌کنیم و نه می‌بخشیم؛ تنها منتظر لحظه‌ای هستیم که عدالت حکم کند. هر ثانیه‌ای که می‌گذرد، یک قدم به حساب نهایی نزدیک‌تر می‌شویم.  #WillPayThePrice  #تقاص_خواهید_داد #خونخواهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/664306" target="_blank">📅 17:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7Lf6wYF3hWWRaowJpyhnofAHkjombsUmpdXLtl6r0ZvhLMovc-k3DnKtQLv1xP7b-RKo9cnIuc8W47vqHXVwd51eAhzwjwQR1jsX__kC9rODcfYGn5UUHWDVok6HeJi9OGi3qBZfg0eNFmKaqpI0inxil_nunBLxo5nhvSiKSBqRw7urRfmzGrPDVfhHUNMLjTU9goN9G9tlinJJ4Ugz7hOQYGrB2cjzBfjZHhJkEqOl19Mlu1-kvwPQs9_v5W6_wcKXRGIsmd6aLREuHPToU3uAteUUQHS3KAq_lwmJ-8pTund-qU41tMszHJh-Eq6lKY8LPNZaTpnSUnR9wbnVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکاوی مبانی فقهی، قرآنی و کلامی
#خون‌خواهی
در اسلام
با ارائه؛
▫️
آیت‌الله محمدباقر تحریری
▫️
آیت‌الله علی‌اکبر رشاد
▫️
حجت‌الاسلام والمسلمین دکتر عبدالحسین‌خسروپناه
دوشنبه ٨ تیرماه ١۴۰۵
ساعت ٨:٣٠ الی ١٢:٣٠
تهران، میدان فلسطین؛
سالن اجتماعات سازمان تبلیغات اسلامی
جهت ثبت‌نام، مشخصات و میزان تحصیلات خود را تا ساعت ٢٢ روز یکشنبه ٧ تیرماه ١۴۰۵ به شماره ۰٩٢٢۶٢۰١٨١۵ پیامک کنید.
#ظرفیت_محدود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/664305" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664303">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
سفیر آمریکا هم ایران را تهدید کرد
ادعای والتز، سفیر آمریکا در سازمان ملل:
🔹
اقدامات ما در صورت نیاز برای نابودی زیرساخت‌های مورد استفاده ایران برای کنترل هرمز ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/664303" target="_blank">📅 16:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664301">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b9209944.mp4?token=aKFJ6DWtcDl5JDdrMNaNPM9Elbx4aMK7IPxeninnecATZ3_1Qn8YH2N4y3qViOqqVsN33fA1g6lNNthPtjGLdpYy6xRojLZyFgBhjOp7pGAok_Y7xeL6_zuqmAU8poXMMBohdKhKkgMq7J7pBNkqnJAXuq0Eg6zn7ylL-yvW_2vkPH0x4PIyH_jdh9dNWNoQn5fQp0UnSBKbMp4nOTEwfPmYPuq2WysyLyZ8IrySY_WSZjWWm5PQs4kAmYSaerCysOHXLA-6ysblhc_0i8L6YB_NdDeydQif7wG4z5tBv2frsnoS_ezsjuuKtQYNGdObsjB4OUS6tjWOJdmjIqGRjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b9209944.mp4?token=aKFJ6DWtcDl5JDdrMNaNPM9Elbx4aMK7IPxeninnecATZ3_1Qn8YH2N4y3qViOqqVsN33fA1g6lNNthPtjGLdpYy6xRojLZyFgBhjOp7pGAok_Y7xeL6_zuqmAU8poXMMBohdKhKkgMq7J7pBNkqnJAXuq0Eg6zn7ylL-yvW_2vkPH0x4PIyH_jdh9dNWNoQn5fQp0UnSBKbMp4nOTEwfPmYPuq2WysyLyZ8IrySY_WSZjWWm5PQs4kAmYSaerCysOHXLA-6ysblhc_0i8L6YB_NdDeydQif7wG4z5tBv2frsnoS_ezsjuuKtQYNGdObsjB4OUS6tjWOJdmjIqGRjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رواق کشوردوست تعطیل
شد
🔹
رواق کشوردوست به دلیل حضور ساختارشکنانه‌ جمعی از کفن‌پوشان تعطیل شد. این گروه که روز عاشورا از مشهد به تهران رسیدند، تحت عنوان «خون خواهی از رهبر شهید»، ضمن جلوگیری از برگزاری مراسم روزانه رواق و حضور عموم مردم عزادار رهبر شهید و با سردادن شعارهای تند علیه مسئولان، باعث بر هم خوردن فضای حضور عموم مردم شدند.
🔹
به همین دلیل، برگزارکنندگان این مراسم تصمیم به تعطیلی رواق گرفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/664301" target="_blank">📅 16:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664300">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-9GoGFrCpf-i7Wz--GhcGKc3HI59ecRiWhu6JRaLlEy83GN0MwQSS7kM3fpMf7m9FIqvLBQewSG_nraeOOegSnBvIcR8UhvRN9Fo5IszWssfxwncmm0GOrpirrzKSWp2Xo9Wt0X4E3RePnz3jx9VXK9zykMECEpES7mWK6QMN75D8kp2D6o2AyxmJxl2R0p3M2a94GYyOAWXi-3-T-SWzdaa4PsKAwurINj1Cqs8hjZEffN5UE-QVaqvBTFos1vgDkyLTubsfRwY-KDFTDRrOLesbYRHOQd2np-04IEdAGRqSAvDWMi6iI2TtEk5ONvv6NpBSQ3_YYwGDA4vf65Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌زدن تابلوهای تبلیغاتی توافق با رژیم صهیونیستی در لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/664300" target="_blank">📅 16:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664298">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/929b4f703a.mp4?token=PTxZL6sR2osG5Ob-M-ApCZVd_T2YnjI6EJStVBhbgXPCdEegBZ6d-DzJsoDMkXgDg4crxwFLz5tt_utrv8duAWhcYubF6M-VvTXAvJrXTBVC81P6m0aVugx815JLWXJcAhdbjsAVFpYQf_XrHPLIkw0gvd2p4DqnCbE1jLBC5GcTdKoozEQV2E92w43etJw1aSDuiMMFN2p_pv_LBHlRKH0__aVo861hKuzBJuyckGU6rljpbXWyLi9ccSwopyB6ZBcbAE_SEiqNxAnGOf40tF3wV7LH8cg97FqEK7hc58Ho8vAcCbUfp_Xr5x3ovJQoEoSDI0GWi6ngAuR0dA6nPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/929b4f703a.mp4?token=PTxZL6sR2osG5Ob-M-ApCZVd_T2YnjI6EJStVBhbgXPCdEegBZ6d-DzJsoDMkXgDg4crxwFLz5tt_utrv8duAWhcYubF6M-VvTXAvJrXTBVC81P6m0aVugx815JLWXJcAhdbjsAVFpYQf_XrHPLIkw0gvd2p4DqnCbE1jLBC5GcTdKoozEQV2E92w43etJw1aSDuiMMFN2p_pv_LBHlRKH0__aVo861hKuzBJuyckGU6rljpbXWyLi9ccSwopyB6ZBcbAE_SEiqNxAnGOf40tF3wV7LH8cg97FqEK7hc58Ho8vAcCbUfp_Xr5x3ovJQoEoSDI0GWi6ngAuR0dA6nPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۲ راز پول جمع‌کردن چیه؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/664298" target="_blank">📅 16:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664297">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه بین المللی نجم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebee81128.mp4?token=Sr5C2hJvO0OerHWUiOzCIHqMkCfXNLFoovOmufEoHN09X1rFsuMVMAknMKagL7iNHhKIGx5XiFZilTmiAZKdnZXUU5d7LLIaLOxZU0bSng7tcmwjIb1qWk3BZcSqV8ccF6pC-FG6yQIh_M63TicDrEufUKPBxB6Mpu9a1Uh9mO3HK-QfkIUuWikyEb4d21AKG1mgOM51fSFjRTztdzhMRCcP2uYhnFzie-ifQyVPECqE-Bmyz-cvlDLYV1a0qZq5l-w9N_WmDa2vJo9gbjUUUjWZF9UithszahAesuhjvL8bYIt4_jhHt2TgC3qNe6pHPDzoQfkj1ciGPdbSbpyKrLCZvSz6FvngUPyAa3Jz39EapoNHNLfxrMK3iElnhrDSFWJ5JLhRSAoJ_lxwxLBcTEAK-JpEA3eutT2Pt5xZ30XTCRytyqMCBuen0WHNqsmNfvI45WvAMxXPufHvr2EffP7Z8QDlAph4UMXNSaYFeqWMeytj6NpvKPxoxwbEmURC6dtHIzN_jGcC4x3dJE7eAkRuABOQoIFOLsKavGkkawqdjTVDo7z7suo7kwVkr1SaC08zUJevLiM2NOmQkFkhozqqh1iz_GdZwFbj3yEFFH9jMEPQlSZrFmdNCOKHvz1kvclrPKbAYdTxz9a-dauF0pIP0VnKmhZeqLzm0tyIKQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebee81128.mp4?token=Sr5C2hJvO0OerHWUiOzCIHqMkCfXNLFoovOmufEoHN09X1rFsuMVMAknMKagL7iNHhKIGx5XiFZilTmiAZKdnZXUU5d7LLIaLOxZU0bSng7tcmwjIb1qWk3BZcSqV8ccF6pC-FG6yQIh_M63TicDrEufUKPBxB6Mpu9a1Uh9mO3HK-QfkIUuWikyEb4d21AKG1mgOM51fSFjRTztdzhMRCcP2uYhnFzie-ifQyVPECqE-Bmyz-cvlDLYV1a0qZq5l-w9N_WmDa2vJo9gbjUUUjWZF9UithszahAesuhjvL8bYIt4_jhHt2TgC3qNe6pHPDzoQfkj1ciGPdbSbpyKrLCZvSz6FvngUPyAa3Jz39EapoNHNLfxrMK3iElnhrDSFWJ5JLhRSAoJ_lxwxLBcTEAK-JpEA3eutT2Pt5xZ30XTCRytyqMCBuen0WHNqsmNfvI45WvAMxXPufHvr2EffP7Z8QDlAph4UMXNSaYFeqWMeytj6NpvKPxoxwbEmURC6dtHIzN_jGcC4x3dJE7eAkRuABOQoIFOLsKavGkkawqdjTVDo7z7suo7kwVkr1SaC08zUJevLiM2NOmQkFkhozqqh1iz_GdZwFbj3yEFFH9jMEPQlSZrFmdNCOKHvz1kvclrPKbAYdTxz9a-dauF0pIP0VnKmhZeqLzm0tyIKQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اختصاصی| نظر مردم کابل پیرامون امنیت افغانستان در زمان طالبان
🔸
گزارش اختصاصی خبرنگار نجم از خیابان‌های شهر کابل
🔸
مردم افغانستان: قبلا در افغانستان انتحاری بود، راهزن بود، شبها نمی توانستیم بیرون بیاییم، جاده‌های بین شهرهای مختلف ناامن بود اما امروز امنیت کاملا برقرار است و به همراه خانواده‌مان می‌توانیم در ساعات و نقاط مختلف تردد کنیم و بازار بهتر شده است.
محرمانه‌های حوزه بین‌الملل را در نجم بخوانید
👇
👇
@naajm_ir</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/664297" target="_blank">📅 16:29 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
