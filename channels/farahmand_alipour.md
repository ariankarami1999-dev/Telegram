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
<img src="https://cdn4.telesco.pe/file/Ml60COLT4KvrJfA0juPT56ekKDYD0K1jxhtZUhtfJqFK-UCY76e2lOuDm24viKkLcQOnXM4TNYzXqWKwc_Q3nO9I_RiwHBrDvG2iHiWimnW6gOuLorekljARWFI97qk2adis84d5jc3yhHXZnS2lKqcWX_v6cH8EinJ-DDHOZO-NdxPLccz71HhY57IcZOwo7BWF50VrzgMjvVzbDsN3z3PVlHXI4N88BVFaBwfEntu4VOrhyspxVEnxVbGAWaoO_MO2DdkGYs68OSemCifrCIhSc_ZOZcSr4ZwnBlKfBgIEjskr7UMRFkWOnx3JQivtQjvSi6iTIuk3xHlMVNScUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 13:47:57</div>
<hr>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=YyfB1BxdxwYTvWWAQsWmNcfDtjEVd1cdIIvljNlTGaqZy2kuXXRLymzxY-h8PFb4vjUiLx26otYTsaTTQ0DXJmUYGV188zIKh6_iXaQhIHbmAme8ZFt88tT7iUIpSuvzh6IMmjovdZBt79-t3JLiBU-TDPemCCaItQ6wAeKk0xlIXbl60AfFcYulZpIL78of4MiNXxhUike7w5hG_cCmkqvksp6Hm6Ql1X-fjg_7RivbEkpXC2adLwck0eRhl0qW-l9ydALb-xt3srlrkR5zRexqYMWqfS4Gu4GZnZQLsmKGS4VPatYvx3I3EgwqKYjeN4cqjrSWKSOT33YqDf427Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=YyfB1BxdxwYTvWWAQsWmNcfDtjEVd1cdIIvljNlTGaqZy2kuXXRLymzxY-h8PFb4vjUiLx26otYTsaTTQ0DXJmUYGV188zIKh6_iXaQhIHbmAme8ZFt88tT7iUIpSuvzh6IMmjovdZBt79-t3JLiBU-TDPemCCaItQ6wAeKk0xlIXbl60AfFcYulZpIL78of4MiNXxhUike7w5hG_cCmkqvksp6Hm6Ql1X-fjg_7RivbEkpXC2adLwck0eRhl0qW-l9ydALb-xt3srlrkR5zRexqYMWqfS4Gu4GZnZQLsmKGS4VPatYvx3I3EgwqKYjeN4cqjrSWKSOT33YqDf427Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov-5teW3tHTvsvSbgMdLICYXYlU_sDGIu9OuiTSl0594zrfs9gRoJQR8S28V2CiP_XCjD7Zzp5uItinMqAUIbUIRvVFn3zxxaqYh9Km-0nk74uSUdeQvuMYluMHfHS7WfmU5Mq1R_o1vTjHKfD6MlZEq2Yf9KVRt4d2gzoWcCctXxlvrZ83-13fvHD4NvwcgSfJHIpLOCqzOAdqDTCE-6frq1o_rpZ_dr6FZtGyKaUvR4uN5aL7iKlIR-aOJwWaAcP_ZJcq4l0tyEkcUu7cd1nNA3Bm7_vFPEyFbPsYQr_SdVeOSm92Zw0-QEekuDDdOwCr60iw-tbsukbzrBFNmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHVVCza4-k7lMKxM3gRJStW0mSmbHx1HOC_kqRItxfPQPZo3RqgLfbxvjky93wErqiutSbOoRDVDgJO6-5Gt5GeEQYp3ZpC8LbmHHVvogV5fTJ8tjv9WUtzfZpz5NJscTMxYul7zKui-uhcGtGwcbJz9kr1kP6yA61rGmmeIOf2BDf3B7TQdUT7ccFphzbXnhtP5luogZEm_0Gi7-eRD7KumLBDmDBfFnXn0yVHUWnWFFsbkQWbKqce98C8p4SF3LVslyiNzTK7TUUb1kdRXw9U_E3m1dmBOkEfxlEWe_yZkhLuLgJrZdcC01kX5yYjphMbJYFfm6UDxnofukWHSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCjBqZM5jXwzu1sJL8r35MlTnF182x6QbMhDGU9VEkhPOMChzNeaXqCYzhcd6LJGEc8XKVJhDEOCZLY6-Bg0mo3gTyV7KA0W0VgKf1y-eJ7xunXvZC0jkta8Nk7KLol8xZCfK53OOF6-KxT0W-zsm-O6oJt3QluEHjRwZQJAw5WWfouz4Vnl1rFgim-MT9ftv3NW4XmhnqGfImmekKcW5GnAP8lgCRU3mqBn08gEhzpWgPR85EYKfDhTOrHvtUQI8sXGakrwAQfehtQGujG7Jvkcanrp1cXZhxmJ8qYpaj9r1_clqQmhAQ1abKOPsQqWg_4Tt-exEDe-rJ3r-yrtthW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCjBqZM5jXwzu1sJL8r35MlTnF182x6QbMhDGU9VEkhPOMChzNeaXqCYzhcd6LJGEc8XKVJhDEOCZLY6-Bg0mo3gTyV7KA0W0VgKf1y-eJ7xunXvZC0jkta8Nk7KLol8xZCfK53OOF6-KxT0W-zsm-O6oJt3QluEHjRwZQJAw5WWfouz4Vnl1rFgim-MT9ftv3NW4XmhnqGfImmekKcW5GnAP8lgCRU3mqBn08gEhzpWgPR85EYKfDhTOrHvtUQI8sXGakrwAQfehtQGujG7Jvkcanrp1cXZhxmJ8qYpaj9r1_clqQmhAQ1abKOPsQqWg_4Tt-exEDe-rJ3r-yrtthW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtqbusLboLN9-Lrqe9rkYIJx_IvHR84ZEHryWdkZeDoRtrOqikXN7EiCJPyxhY0K5n1MEgMzgzs5MR0SrgnYs_3F8GgLoDYdKQ1LYTW7Xido4AUaYEQj0QO1zbE_UI2rRR3Xjp2NfzvzJlA17Y8-RYrjCC40HPKznslTM8wL2b2keXdTihMVSAzhrWsKM2zE1ziTnSVNA2CcNqGAk4EUva6MDz1HAScSWM2X0YSeo7K-8tO5E-3qzHKOu7syOVXFFTPwzsaVcApsYq8y_51MikBazPUNTFYfJVOy4371oGxyqsfjv9LPjVEwVrFbGqSg_gT-daVP7dZWwSQ_f8DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRYorMv_LE_7-u6f5repCeg_po1RsblXfhsw40pFXv_a19PNIksiD6k4_mG2C04SxN4cxINr8twFLhPzip6-95c0c4ifpKDsvK_z86O-1jTS1Z0Uf-WdsmiMPeynab0RfSXWpHV162_pPpC9Wvno9zW7pPMd2DYD7ddx_AqsazarvaPpN_oR0rhFYKmbJPynGT9OChXVfulP-eNk82T0WoMxy8U3TaDCHx10eJgR4HGLdNzy1dZbrabPk6YKS74N7NrgiqCwFaXcUW-lZlnruJcqwJFWHOv2nTsIsN18ww1lxZ8SHzYLGrzQOdTnCBybI6lS1yU-Nt9TJ0Lb9pQV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpbSRpAJNOWT7GKMBce7eh1uuHCHClHAWp9foEppchDzoi0EE6futb3R08DdwB2Enf5oct2gZT_lYZFXIxhKQOz1qQ4KAskg0Wz2xxz8vkoJrqcjldNRariu01LmlA_L06jCrU3lRXDssg6EunnRBRzSF96Wf2wLqPHpHPO4nY_CSZCAVZKdD50lRwlrA2RWoTmBEmHj54mGi1KL8qFqkvFwPyeO9jW_D1h7U2nzWua1cvIpggabt4lNPLU2QEi1SOeLeKrovu548Z0u16YHcGHxSVYIbse1YC6p00yL90yQM_o0lod5FcQA1eDWm83O3khKUb_Nc7ibczl2MOqx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=jZQPllj9zplsVJ6WXyXPgbxYIpBMfzupXgeycxHR4RSxdb9Kh6p0oCKDwp_9MLv4IQwvAqEYcb2v62am63iM9vQSgvv-xkVoi4Ba3vIsM6dOyNB-Kz5ItLfzGtspQaRB7KA4yNJQT2aifvn7OYdmdBba8pac5Ib6ItbdtOT_yZikQ1adr-x67toVlZf2Fxl4Pzo_VrJm8ilHujvk7u3XSbwAlnhednqtMYmnKZt7K5YqVWVLlbpHzHt2kNXoYIzsXsWFc8BGk3tGnU1SFhTh8ptKR7jufqJn5DWFukepEMnR_YyP3D_rOGYMhy5FwMhG0AZ_SboXOCt_tqmngUTRMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=jZQPllj9zplsVJ6WXyXPgbxYIpBMfzupXgeycxHR4RSxdb9Kh6p0oCKDwp_9MLv4IQwvAqEYcb2v62am63iM9vQSgvv-xkVoi4Ba3vIsM6dOyNB-Kz5ItLfzGtspQaRB7KA4yNJQT2aifvn7OYdmdBba8pac5Ib6ItbdtOT_yZikQ1adr-x67toVlZf2Fxl4Pzo_VrJm8ilHujvk7u3XSbwAlnhednqtMYmnKZt7K5YqVWVLlbpHzHt2kNXoYIzsXsWFc8BGk3tGnU1SFhTh8ptKR7jufqJn5DWFukepEMnR_YyP3D_rOGYMhy5FwMhG0AZ_SboXOCt_tqmngUTRMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsuMVwbycOVcKxuIsl8NhNoah4C8Lf-fvDjm9Qx_apRKyHEmvAOY39Pg_XtQb1s0Satath6r65ylCGxZ0Epe7_A3YyqakeYvcaNRozmd-hDudHiUXQRKs1VL0pCMueM9rAIHksMWSYN7-rYaqPGiaRYgXmVuLk8iRkye2Zv-ySE90tEjfd82Nc_I_suh4lAZd8Y0O4CvgtAWQsRiYXGALnytfvYIkHBZObGkDGHWta2AkziBjcfS4twnE6A-rCgYSZiCWLNL5r70ggzVB2fJ8frEXWYv9IBkZL1kJsacTZCGSp4ReGAROkc3slwLZO96LRaYHpJpCi7kGWhGmtir6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk6fphPF7k3GAXKniH27qXUdVZijx136CtDbuOAq0OBZEl9OeXV1Pszr9daS0G2CH7aZMkw5Cn2ftqgqBFI4q-_pniyjcykRvEc8RCyseJZt_rivU95z_joaDJA0kSXzjWWE9MuOV2ynElWJp4Nw8b_BGD5hicnT5klD_szuGWAqr7L56R5zdYGVTgfaADOXjoigXBmPO5uG6VRKYmg7RH6f8epGoGniHMmvlhFXEywxgpwsyrqOk05qGkmW_rwSb1hgG3VWuh5Eai26eQP9fdm5OHFXZDucPZf6pPOeVTO9aTzm4LdEq0YgJGlz7G47N41UbH4QlR1inWtAc3eCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6brwnxT1KHRZ1oIIDlge8EKLDpyqE-k5ojbhuIWve_P1e2hOaIzxcKxiYFp5t_FKUWpDK93JPKxmsD2f9k6VpK0Q7ylFw4QKPoUsrx-RBwlbZBCg6iQgc3XcKEm8V3dgdsKMgySEi-Vgl8_Gz5C3LGc4A6HOSH8Uir-6h76-9Ds_MNPGVJfsmqXiQUQ5oU1dH6VVKyHmgEuX0F475bYz31iR3JP6LKP2_6sp5s1CgrKDRB9XR2UOxtOPswelfiiWpcM5ZEy8OSMjEXVagRH0O2IvzOrA63mfo2StM3Rg5GiLMqgPOXybErSYq0CYEWR5g6WEXZRhoC95X2JTmjGOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFAQexToODT0YsJuANiC3d59w9i1ksL4YvoT19LWtYK9W12QYju2e3q8Ea9LLp8P6mB6FYXbRA6y0STeEOBHBad8R7CRqtkn2DsIOtHgXahJxdwT2vBcvOHkmo2oESkhRgllbu1GVC_Yue3G-Qn-HPZHd9meW0Lx4-zKkTV4p15yW89vjvHw-wPQLX81AEy_KrODuQyZJNYpqGTG5h9PUWFF3CU_5ShpopGIjgDpkUkbJt4F82hXjSb_Gkm51s1EG2PGNp_CwCinAeSRngUvRA1GNGv7csguknPPQs3FQV2z0bemwQ8xA1aS2C-dl6I-ynG9rhI2_y3O3zW6Apfk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=UnoxBFIzN9DShbYlKyXdmE4mi-KE21L5tYYViKMRgZObZitavP1Uf9iO35LAYG5TDtH3PYVIYj179zw9u_OUbCtSa0-287iDRSzbLiRlf-b7a92uemWB9pnoJUZ4HXi-6TSYL4P_2CWE-T-vsOjZmrGqpgsFnwPMpHQB_NunKpWRjydwrU8ChyuYnIR0tgPnxu36r71oHju86LNurQ2vXGLrFVglHzvH8wh5cYF8Xw3nVt4oL4ONu70PilrkH2wNcjh4K6HsdIg4BQm2smZBAdKfwmSDevaFHecDRW1DYQf-FEGL7pB5yvMoT52sNNzO9tkgpNQqrC7k00vCgwTy1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=UnoxBFIzN9DShbYlKyXdmE4mi-KE21L5tYYViKMRgZObZitavP1Uf9iO35LAYG5TDtH3PYVIYj179zw9u_OUbCtSa0-287iDRSzbLiRlf-b7a92uemWB9pnoJUZ4HXi-6TSYL4P_2CWE-T-vsOjZmrGqpgsFnwPMpHQB_NunKpWRjydwrU8ChyuYnIR0tgPnxu36r71oHju86LNurQ2vXGLrFVglHzvH8wh5cYF8Xw3nVt4oL4ONu70PilrkH2wNcjh4K6HsdIg4BQm2smZBAdKfwmSDevaFHecDRW1DYQf-FEGL7pB5yvMoT52sNNzO9tkgpNQqrC7k00vCgwTy1zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=vv9FkJ6NIewOAnSfH5yeJCun-hvp_sFojV39vG-GM_Ks7QQru1xql7fpult-YEdHi6kFkbh5eBwJoOrFt1aOfNREO1tjxzuMs-JpIuhtI-BBWBcwpDab_NcBKs3dZPiZkfsixnxLnTnEV1KvuN96oV4DI8KLYTHEKgqtidGeaJBqye5mwbtz8C1UuExRIk0j2pTnGZ69_cRwAJht1JvnXKqVwmUGk588RrMZ2cOjF_RndIFVkTC8oCLxgOMF4AQPKv2YI6yer49oEitdbrRzonA2D0vfrM4uVXCU5WsWShbfqAnAODOSRQidHbv6SUNjw9tOhz0RwHCFCmRdM9Qxfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=vv9FkJ6NIewOAnSfH5yeJCun-hvp_sFojV39vG-GM_Ks7QQru1xql7fpult-YEdHi6kFkbh5eBwJoOrFt1aOfNREO1tjxzuMs-JpIuhtI-BBWBcwpDab_NcBKs3dZPiZkfsixnxLnTnEV1KvuN96oV4DI8KLYTHEKgqtidGeaJBqye5mwbtz8C1UuExRIk0j2pTnGZ69_cRwAJht1JvnXKqVwmUGk588RrMZ2cOjF_RndIFVkTC8oCLxgOMF4AQPKv2YI6yer49oEitdbrRzonA2D0vfrM4uVXCU5WsWShbfqAnAODOSRQidHbv6SUNjw9tOhz0RwHCFCmRdM9Qxfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=BsN5vznYf5mpxdqPI1nDiX902JVsLcDPpi2xbRJgiC2GjLzw6ukGARlxqR2CQDtF6Qbu77hu_vsYZ3P-27-FcKrYbLP7nqHODfEgr-T5_tQkn4jjj-tGaZkPHiwRhzVZRM8JfusIRmMXTFqQTRnZM_5cW-Go1Qoa1mi1AIuJvCq1oE5U9SP_Rg0A8HsOcf9GCuk7sDo5Qt9YGDcClE0ETfcgb6Jq3NqjF1XzhMQ2v85plUdFeB50Ewx9RzcfJsnbxdi6oHy2qS3-In4FpHhT_Xh7-1kJiJRLiqklyT2ki-30xiaGlLtnGo0ON-6asvlJ2m7bGrRs7d3IJDz8fNzlwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=BsN5vznYf5mpxdqPI1nDiX902JVsLcDPpi2xbRJgiC2GjLzw6ukGARlxqR2CQDtF6Qbu77hu_vsYZ3P-27-FcKrYbLP7nqHODfEgr-T5_tQkn4jjj-tGaZkPHiwRhzVZRM8JfusIRmMXTFqQTRnZM_5cW-Go1Qoa1mi1AIuJvCq1oE5U9SP_Rg0A8HsOcf9GCuk7sDo5Qt9YGDcClE0ETfcgb6Jq3NqjF1XzhMQ2v85plUdFeB50Ewx9RzcfJsnbxdi6oHy2qS3-In4FpHhT_Xh7-1kJiJRLiqklyT2ki-30xiaGlLtnGo0ON-6asvlJ2m7bGrRs7d3IJDz8fNzlwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BraOqL1PzsQJUh9QcK8tsT0BEzybzRt9LzCOHPYdDyFexgnvNZ0k-Rt3GJM4XoJ_zETF91bPA3zWfTRO6t6gBltitZkYo60iDbHC3KSRyJOAv_a4i4P1rHEQscNwK-KbkGFlnO3UGLvEB7H-YJgj-xTVImDY3hdQQEQ47qomFvUAPj8rUqNI69E1HmylfaBgjBtdtb_dNqfn6-RTAAEQs9AYf4CzocabJFZfXjEvGJRZiGuqUR1glYcVT83hDcJBFj6-aYYypNlwnIrY1ywvWZUv01WZkvo9aofIOpBlcXdpeN88QInkr2hg1Nsjj95ZgMEaQgoEq0B9L0a8flncfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=u66MiQTknMJIur4e4u_Fr2SjD2OuQctbCQP3_CXZgMfPSvgg6OTLOpcaitNhduhczATQWpjQEzuty5TNwbIVN__KQ2LL7rUjA6fnET34qfIcJCLoFS4llLcJCA_xFQ8Dp8BhIcsy_bNY0MWySowG7bjpmLbhcMROEcNg81ZUMYipCY_EjUB5iqJOT4jfiEuA_8qUXlW5pIokZlLf58WOYvMJmnoHQu1oRvBVPNUCDfCDqpA5xQ6g-ZCCvM-b2kkGt-XpYtZMAuwurrXm-Pyc0tQu--IzI8IcT_itsVRWzP0fZ232Ra_LiggKEImSCPKLwT9gq3p_N1IMF_2DKft2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=u66MiQTknMJIur4e4u_Fr2SjD2OuQctbCQP3_CXZgMfPSvgg6OTLOpcaitNhduhczATQWpjQEzuty5TNwbIVN__KQ2LL7rUjA6fnET34qfIcJCLoFS4llLcJCA_xFQ8Dp8BhIcsy_bNY0MWySowG7bjpmLbhcMROEcNg81ZUMYipCY_EjUB5iqJOT4jfiEuA_8qUXlW5pIokZlLf58WOYvMJmnoHQu1oRvBVPNUCDfCDqpA5xQ6g-ZCCvM-b2kkGt-XpYtZMAuwurrXm-Pyc0tQu--IzI8IcT_itsVRWzP0fZ232Ra_LiggKEImSCPKLwT9gq3p_N1IMF_2DKft2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=RZRA2sDR8t46eNbxhGgWWRGjRQAtNmjlkdHGcJz5n4YXdRDA50Z36z94iJoMbXyip75CBmu3-DggIYeepB4iQHOH0YVdzPzDA2bYJJ_cjy9UrTsyIpawt4USE63IzlxyyiXj859DfTpfHPat31LMqYrEKwkSeBAajGiGvxRQeS1k_Zt6ll7e_DW2A4S83UdYgCaYrmQ-rxzq6cfXfG-R-KPqu9W3Ht3Qb2au4G5pkw80-kjZRicABwAqrDgE3WTwcF1lf8O_XTbZiBTj4UB5G3Yk6O8IWyteKXJDqKLdzyuMgAwSpXFWmWb9rPvTJOIN7sVDps-zYoOsNvbTw5KMYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=RZRA2sDR8t46eNbxhGgWWRGjRQAtNmjlkdHGcJz5n4YXdRDA50Z36z94iJoMbXyip75CBmu3-DggIYeepB4iQHOH0YVdzPzDA2bYJJ_cjy9UrTsyIpawt4USE63IzlxyyiXj859DfTpfHPat31LMqYrEKwkSeBAajGiGvxRQeS1k_Zt6ll7e_DW2A4S83UdYgCaYrmQ-rxzq6cfXfG-R-KPqu9W3Ht3Qb2au4G5pkw80-kjZRicABwAqrDgE3WTwcF1lf8O_XTbZiBTj4UB5G3Yk6O8IWyteKXJDqKLdzyuMgAwSpXFWmWb9rPvTJOIN7sVDps-zYoOsNvbTw5KMYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=e7ltopzRNBHPzlwlQLv3my2rQDQ9balyDy1FC2Aq066BTn3fpCEyo0O3WgT04-cZmYd8ZwlaI5KVgXn2BOmLcrEq3mRUNoIELRog1rSz884lCeF04vFJFgnjA-mVxQ7giWuMDZvSneaA38HPmMCvzARlaoWF_gBZMiHP9QC41qRKjQOt2c-Gu6w5SXDJf-670sPN_kZJbYZ7po-qG5fpX0GCQfSbpTAZ_8h95FkgppQBwWmPqam41-85dr8CgvO8Lp8NUV_VYzB3E8mb-vVxXtxI_PG6IhWeX2mHgLpv9d9hVu4hwfTbGESZKNA49ybeHI0u3fK-7A1DTQU5AqZPsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=e7ltopzRNBHPzlwlQLv3my2rQDQ9balyDy1FC2Aq066BTn3fpCEyo0O3WgT04-cZmYd8ZwlaI5KVgXn2BOmLcrEq3mRUNoIELRog1rSz884lCeF04vFJFgnjA-mVxQ7giWuMDZvSneaA38HPmMCvzARlaoWF_gBZMiHP9QC41qRKjQOt2c-Gu6w5SXDJf-670sPN_kZJbYZ7po-qG5fpX0GCQfSbpTAZ_8h95FkgppQBwWmPqam41-85dr8CgvO8Lp8NUV_VYzB3E8mb-vVxXtxI_PG6IhWeX2mHgLpv9d9hVu4hwfTbGESZKNA49ybeHI0u3fK-7A1DTQU5AqZPsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=DONR42PK0RVR0sWnYQm9zWY1XYiNfxkXYpzPPfgBkf59LywinIfb00nRt_AI5fx70J6VCGQoEAgubpqHeCMFiMHn6r55YSKjFMXYBKL6XrajtFPRfY19SRKu-6RieEBdDaMXynasj2AND2k037N45Gm0_kcdyQ6Q7JvzsmntI-GTsc02QRGhK-E-4mfDijgNdB_KAf_Rnn4cyzAciqeZYepUvdwa1oLOALarM0VBBaaHBZebAKco4wbnFnzeFkWIgmgUDtP2Qo_ncgeU5o-BPqCV7R9oadoof8hUhQxWa6NXqXkxbdk6je0KZ3JIXrjgNRMUgIC8lpZflm3oeDQq1QcvaBZeiXhMibXGBxUqplR3We-xcjsA5U6cFVKMxtYvwl_pbUO6V-lf5-ukKse70zhtt1G5a0R87rPH2-s0DObtDvNOIO6Et2DfrafNknkS8tJKxsMLFx3pHZu3dbRD_UHTtNHMUNEn3eGCYQl6IAZnhCX72qrZRGMSpfz0QC2Bt_Y5dfL5XtbO2BPvyWsT8Los9mPtv-F3aFx2PNtFjkFKbsl1Y991e8qmTpD6c00utQOOetYcN4680qa5H3jy-xGqn3n-_os418tRKMdSukst962yYV8MwFdjIelUPL_D5-f5yxlkqibkGxVRAR-I5VvaPBNW3xRzl-tDeWEgXXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=DONR42PK0RVR0sWnYQm9zWY1XYiNfxkXYpzPPfgBkf59LywinIfb00nRt_AI5fx70J6VCGQoEAgubpqHeCMFiMHn6r55YSKjFMXYBKL6XrajtFPRfY19SRKu-6RieEBdDaMXynasj2AND2k037N45Gm0_kcdyQ6Q7JvzsmntI-GTsc02QRGhK-E-4mfDijgNdB_KAf_Rnn4cyzAciqeZYepUvdwa1oLOALarM0VBBaaHBZebAKco4wbnFnzeFkWIgmgUDtP2Qo_ncgeU5o-BPqCV7R9oadoof8hUhQxWa6NXqXkxbdk6je0KZ3JIXrjgNRMUgIC8lpZflm3oeDQq1QcvaBZeiXhMibXGBxUqplR3We-xcjsA5U6cFVKMxtYvwl_pbUO6V-lf5-ukKse70zhtt1G5a0R87rPH2-s0DObtDvNOIO6Et2DfrafNknkS8tJKxsMLFx3pHZu3dbRD_UHTtNHMUNEn3eGCYQl6IAZnhCX72qrZRGMSpfz0QC2Bt_Y5dfL5XtbO2BPvyWsT8Los9mPtv-F3aFx2PNtFjkFKbsl1Y991e8qmTpD6c00utQOOetYcN4680qa5H3jy-xGqn3n-_os418tRKMdSukst962yYV8MwFdjIelUPL_D5-f5yxlkqibkGxVRAR-I5VvaPBNW3xRzl-tDeWEgXXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=JvMnXNoZuRQ-7ItMTV_xhbax9-0chIIOoWz0nnaNAFtKxDRmy50cxHzDv7m33lSwowxpG-w98Q4wiFOscjsJ18DJgtpg19Mx6oK2DHSAi013vVFXy4wJ3S8Fj-4OF__9lrflWBY8AUO8QBirab4zNEyTbM-n_yO5Q59zGkzWFZyzVEQ_VWBHJcaGSsqk5Snt8uoYtqt4XyokSmZds5SGRi9SQKIGdrM5m49NNgZIp4s6B8U6Y8pk2pjS90g-vOLgrqWQi6Y2vzN93bbnn9lYroz4O7nuWgYpa26wKUCC9guV9NjQpFE1tlQMUeP6IWbnPk0-spdjGETbA398pKwa6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=JvMnXNoZuRQ-7ItMTV_xhbax9-0chIIOoWz0nnaNAFtKxDRmy50cxHzDv7m33lSwowxpG-w98Q4wiFOscjsJ18DJgtpg19Mx6oK2DHSAi013vVFXy4wJ3S8Fj-4OF__9lrflWBY8AUO8QBirab4zNEyTbM-n_yO5Q59zGkzWFZyzVEQ_VWBHJcaGSsqk5Snt8uoYtqt4XyokSmZds5SGRi9SQKIGdrM5m49NNgZIp4s6B8U6Y8pk2pjS90g-vOLgrqWQi6Y2vzN93bbnn9lYroz4O7nuWgYpa26wKUCC9guV9NjQpFE1tlQMUeP6IWbnPk0-spdjGETbA398pKwa6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=gTxQXrpp9CzJeNlZKcA72orj_o4o_gOSM9wQNyZOG3tdP67eOS0KrjoxA1fqPwRuruof0v-LDwF3t1ryY_9l0CQTwrqnfUNlSZAMbixfiAgIyNOX_H4gjm7ra1oAT0lMyt4hIbJ5LykhqiuL4tkAMg0NuD-h39rNlXRDmbqyc9dbMvRrdzCfv3PgFkRrNfAksS5UjKD_XyAZT0KYxE6zDPCGtqN6Th8kzHjE5Gs4MFZJPGbMToWyUKnQCN7CwqGk08kL8GSw_5mi5KUxQYPZr1CvUnXPdgJyabvBvVhaLu6je2FRhFa-Q9qFtt_po1EG3JtQVvhbz1zRRl99BGi1Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=gTxQXrpp9CzJeNlZKcA72orj_o4o_gOSM9wQNyZOG3tdP67eOS0KrjoxA1fqPwRuruof0v-LDwF3t1ryY_9l0CQTwrqnfUNlSZAMbixfiAgIyNOX_H4gjm7ra1oAT0lMyt4hIbJ5LykhqiuL4tkAMg0NuD-h39rNlXRDmbqyc9dbMvRrdzCfv3PgFkRrNfAksS5UjKD_XyAZT0KYxE6zDPCGtqN6Th8kzHjE5Gs4MFZJPGbMToWyUKnQCN7CwqGk08kL8GSw_5mi5KUxQYPZr1CvUnXPdgJyabvBvVhaLu6je2FRhFa-Q9qFtt_po1EG3JtQVvhbz1zRRl99BGi1Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKNUd0eFAQ-khREvIYfGqifTpMvd__l7hFHEdJu9tI-8RRptcc976Y-gnuYBesoL_ZksYdE55KIx_5exr1Rx1mbSrTMVIoCr9ttmufRhN2nKOEJSWtnGv6_-5mMWXNha4GJbYRY5McqQ5CjnaeBcRIylgsonO10T6jj9jFNKFGMljsqNMeGNMpokRQjUbPnGja8px-YvZOoK4s-QNGkghBqcAsqyjuytd7-koyqzOLgyj0nxS2ZtNSUu4Aw9TO1NyoVY9DOSwTAgpjtxe7KcVDEu9B-lm1dmGTzjlpwSifO4CsEVfM6dMzYfmp7OZ1ztsVe7JL6fqS07NgikBVleyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df4nlA4zTffUNQtbFzyQXzTek2ugUaD0dXTDr798h7yciG2NAstHPVcXviC8QcFmeBufJJ3vj_gM0Ko4PtFTnDsTqMaJzlKdjz4PXKwC1OmvP9SupBNHECGtpaf-Q4Il2h9AgTtzq-eEKGNTkD8pOn0H-DnSDYDnCF306dpEAEPbRh9f6-5va8Imo8SCgRzxF5mvtNvfebE6f9jqD8wh61wvuV4dWjHvTaHKVSOsRf3cIkMfnDL24DWfcMvCZ6o3mfr2y082bOAPWOm6HunuPUe-4F4jNQ9LPZpN5CamqVJ7hqRY9zt5_fuXxPBlCc7hk9StEJi1YCd9tusS9Qwk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=P8f7i2UssNXOH_bJNr6cE7d96fV-XsohFCspk95r3JGa1B7QS65fnGkw_0fOI7pmio-q8UtqHNZoq1IgmVVtETmA62wePaTpm4i1rJPU3nz9qcoeTdFrIMUAgjEOJJm_1W3NeHbr7ew687DTUbIMV37zRLeJOhF2YDj99S6Ns8XezCqwA3MJIO9f__q_R_ktgHsdvhrpbqmbfOPtikKGVhtin5aktN-NyrrcStaek1N1hZ5CFoyzDYd2NroGzPZ-o3K3FAZc8e9tCGBP3LMzGfG6bGtDWXhzeranJ8RIieS8o9f1sAJgPAluSIPX3i_e-VNYyC3C0hIOanScb1f6YyYJutwHnpaqCjvkv7KIbkYVaf7Et79GWRbz26g1UTkHwP2uypzQUq6L9havcoEfSKUF_jjVv5LYIAPrIddK2jcSPLmsExf-oK3lJOqsvXTCpmM7mnSDNmjiRhPvNbZKzf85q4slBNHR_BwHh5XfyLwbiXYZ0FTuaBa7FT6fQZazpClkWjuSzpqqxM5lH83MUXqfHfMIn-L96Ixuz14tPhzgjTWvjS4BF2mbmY2JY38xIbeeevIhEMf2bMuPvDp8dVf_2DZISnKw5bUzf8SaMAzw5WIlyD56i_6BFVcO0K4v3Bkv6tZT6IgELH8lpDNwLaxuo8Ha0vZ5A7r78H8CIbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=P8f7i2UssNXOH_bJNr6cE7d96fV-XsohFCspk95r3JGa1B7QS65fnGkw_0fOI7pmio-q8UtqHNZoq1IgmVVtETmA62wePaTpm4i1rJPU3nz9qcoeTdFrIMUAgjEOJJm_1W3NeHbr7ew687DTUbIMV37zRLeJOhF2YDj99S6Ns8XezCqwA3MJIO9f__q_R_ktgHsdvhrpbqmbfOPtikKGVhtin5aktN-NyrrcStaek1N1hZ5CFoyzDYd2NroGzPZ-o3K3FAZc8e9tCGBP3LMzGfG6bGtDWXhzeranJ8RIieS8o9f1sAJgPAluSIPX3i_e-VNYyC3C0hIOanScb1f6YyYJutwHnpaqCjvkv7KIbkYVaf7Et79GWRbz26g1UTkHwP2uypzQUq6L9havcoEfSKUF_jjVv5LYIAPrIddK2jcSPLmsExf-oK3lJOqsvXTCpmM7mnSDNmjiRhPvNbZKzf85q4slBNHR_BwHh5XfyLwbiXYZ0FTuaBa7FT6fQZazpClkWjuSzpqqxM5lH83MUXqfHfMIn-L96Ixuz14tPhzgjTWvjS4BF2mbmY2JY38xIbeeevIhEMf2bMuPvDp8dVf_2DZISnKw5bUzf8SaMAzw5WIlyD56i_6BFVcO0K4v3Bkv6tZT6IgELH8lpDNwLaxuo8Ha0vZ5A7r78H8CIbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idpYJhIzSbZknqewcIUl1v8hmFui135i-H3n_fGyZ4Y6bDmVXkFpaVmKlJ3THo7VEY8kznXr-FbmIvIoQasGgD3sVhWGXEkG1fO8Fi_4B92TD2cNaK-2SAycsWrkri2r5ZbhKVHRdTb6UxL8gNYCis1i4wTYGO0_t9AFes5SIaXpaiwx0vwRGd4pZw5sl-JRCtzV2wb-EosBCRC9d8Kifz5m9lJqq9z6vshpMmvc9XcD5tlEzLKoDwxZ9VX16RTgsF0C1f47UW-slyuxjIivdh8bkKaCLZltsnYr9G9mTvr9rTDfU747vg1Cn_nJzbRwa41quCZJ7LpEUhz8CicmNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4yItLAeSNIkUDlGfyc0MSGqrploU410eu-B87netQMKR0CRQ2z_A-baNdPpFx9uJ3hv8JJAVXtDGFd1pBblhngdh1_T87bhqMZlcU1RVZhNe9TjKnhW5YKfq6zXQArYRS1lx3ix5dUHV5Z3HDqDtH3i7Qd5pNsXsahOGcmzGF0W6tmS4jJWSxQ_VawtvubOR6HZsz12bp3MOtV7jIqdrgfEWjRPmTdoVRAReEdUaiW_L3CpKRu8zqHmXkUluupq5rF3LzU6qqSpPWcEAvkkcKmo7wTlAWg3tCDtRhJXrmqDsspraFBHhU5bHu9oBxS3kBsy-8ctMuuWOHNxy6bfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeG9rk7GrhgjU_C84Yu36oOWdDZnP7jIGSFgCS1aUz2feDqIU1Zbfn791WLFL7ZkaypD31RFgLjz7648x2rqqp974oePOgRooF8dGBlGhX2eTYDtLNnN04N_8d2vp-VDg8TytSlcoq0BpDTyuj7EKTBgnFHxleOBBjTiiabvh2y5WftEmolzeMJ9l3vh1293-21usk3P0j8-TPKQ8sC6hlLSOgk6dY-dNwuvC6PyxjJCiYAxVOoAcmPr9X6KVXhZKrPm14rk1xuNSLzFAt8u7tvK9g8bjkJp4Y-sOEfQ8aSgimxgf0Brv2XbPo6AyEE6tB3sPwvBSGkOAxLnR3Sjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2n0KMp6EWX_aqTrvOR0tNTH6RLbF2Wt-y2O6Ih-mVORHz8B-9As7UzFjrbidXbleLNOsVWS13Fl29iA12CZpHHIWAgRDroudpXg5zABCt5H4hzBzSGzINs7nTOPDI_Fwwm1AiA-nI1EoGBJI_aKsR3t33o83Vm07fqhRbm6hUsN76zNQpYdqFe11JQ0wIMuO6iLuxrj6SG0ewCLySmTJzPGJCEXjcmtcnCZ7z5n8YHxOr3fzBR8kJpiIHC47PKdOTzzmlUD-k4dY7Xu5CS5jgktVwgAf6fQlJazg_0akDECl2KKmYI0JvaBbzEYxletTzJf4GkhGQImesiGrfSS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=RSx5WDNMu-O0APXNxakaGDn7Mq0OV86zRwlb5T_g0n1-7nerMk4oxPfVaq7eqHvRgv0qKhgug2gpMLFVmXntnoBtVPy5KKnNP8l7seyZwt5idg3JdmzSDzFJx7NWULJcXd66k6ZYMHK7H_10gQ0KX3eY2EELDRAQ2S28cditqjxltCs3vH_ZN7oFozDwKWkdTFKpIaeHCCeBBBv6qrvBW4QSfUEt0KarJdSO3TeZ64YlJkS-8dwBMBdVtaPXjmLqIv7BFSL6ifAV2jZgsf5pTkgK1U8xKr1iWfMHCwWWgczI6wmIKwVIffpvjzWMTYzn9azg6FktbLdbovn3KarCMy_YXj7dEtXa5MK2_AWYLXZKnMQqIezCbaSE_yaVnf4SyoCehieU6zjya1hftQ9c7IXgsxE74T1buTdxKBdokL-mL4qnHo7j_0rUIX0kmm4bddv4Mr7SntBlbBcGt_gki9LjzWxqWfqBuCDlAAJW_LUEGX3C9XaM8Biro7bdPciTUlNbLLU52wYhu5lcoiIk8Ylz4TFuIPXISFh447-I9nK5pHmuKJVtHxbXJ6Gb0hxb2bSO32Gt49HYRdcLu9bRaOJIQ8aPSp1N0Zr9kbOVrpk-pufyy61CYUocJRwlodZwkvkSsfVtr9kPWhUzWy5yD3Oqd8AcpRpHDVG0zh-cfYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=RSx5WDNMu-O0APXNxakaGDn7Mq0OV86zRwlb5T_g0n1-7nerMk4oxPfVaq7eqHvRgv0qKhgug2gpMLFVmXntnoBtVPy5KKnNP8l7seyZwt5idg3JdmzSDzFJx7NWULJcXd66k6ZYMHK7H_10gQ0KX3eY2EELDRAQ2S28cditqjxltCs3vH_ZN7oFozDwKWkdTFKpIaeHCCeBBBv6qrvBW4QSfUEt0KarJdSO3TeZ64YlJkS-8dwBMBdVtaPXjmLqIv7BFSL6ifAV2jZgsf5pTkgK1U8xKr1iWfMHCwWWgczI6wmIKwVIffpvjzWMTYzn9azg6FktbLdbovn3KarCMy_YXj7dEtXa5MK2_AWYLXZKnMQqIezCbaSE_yaVnf4SyoCehieU6zjya1hftQ9c7IXgsxE74T1buTdxKBdokL-mL4qnHo7j_0rUIX0kmm4bddv4Mr7SntBlbBcGt_gki9LjzWxqWfqBuCDlAAJW_LUEGX3C9XaM8Biro7bdPciTUlNbLLU52wYhu5lcoiIk8Ylz4TFuIPXISFh447-I9nK5pHmuKJVtHxbXJ6Gb0hxb2bSO32Gt49HYRdcLu9bRaOJIQ8aPSp1N0Zr9kbOVrpk-pufyy61CYUocJRwlodZwkvkSsfVtr9kPWhUzWy5yD3Oqd8AcpRpHDVG0zh-cfYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=QstbZ2n40_ERXs3HukoR1927tPFa4A03jjJk0RbLrN1K5Al2FfpsaoEC8I0DGJZG1KkYB0-G4xKycbbFEXE8IicmBG-0Mcx4mlxyHhzQgMM0tzklVFgqaA6f333vC8hkbH9IrUNst9JET_IN-_z7aomvGc1e5MWI_wXTZgmP_OvlwXiMOfOMnTUnsCqELSD8xtp1jp0jPsGqQLMSThThgVBiiPpRICM7X51VGE7ij0ypU10RUnMQ2riO-EvqefBN2Ozvogk96MrIfTLk56RAAKotjnTGw2TT5gaKtq_Ioaei6MYl0MXUasThdhJQtRPeahkRIVntjEgHlLPk1f3y3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=QstbZ2n40_ERXs3HukoR1927tPFa4A03jjJk0RbLrN1K5Al2FfpsaoEC8I0DGJZG1KkYB0-G4xKycbbFEXE8IicmBG-0Mcx4mlxyHhzQgMM0tzklVFgqaA6f333vC8hkbH9IrUNst9JET_IN-_z7aomvGc1e5MWI_wXTZgmP_OvlwXiMOfOMnTUnsCqELSD8xtp1jp0jPsGqQLMSThThgVBiiPpRICM7X51VGE7ij0ypU10RUnMQ2riO-EvqefBN2Ozvogk96MrIfTLk56RAAKotjnTGw2TT5gaKtq_Ioaei6MYl0MXUasThdhJQtRPeahkRIVntjEgHlLPk1f3y3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRzhXNRHY-htPx1urtcqQO0DnPLad9rh9B6XhwB9A0H69BZU1531LJGglugyze0r-RXZgGhYFEEFDzumLcEpEeXYjRtbXvPRGLcWnmHS2tvXZYG4vU3pXXgI18R7a6XVKRik_kIf8E6uzfH800fdKYjZygF8yYhMpgY3tUs8JWgbS8gFy_eH0zoaL4NQd4cijNe2jukvEopN6pqLcZga5Gn_ASZAmeXEaSzJlvhn4BKumNVUQqxlmxvNFdRRCSDT3P5V8ZPdQdScMibc5SG1ZVCloRbvjRlzV2RtyJD05yoiyRaIEZgcbnJu9q3txBRbln-IP7Hw4_tKm-aHKKvF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GirHx14VjvkwD-SA1xbE5AHWkUQcww0E3ucEKGJlYmTAcYkxQT3qr535nfkS7Bf-EjBe9cCwJIEZNtsqX_dAcBungHHq9yVgfbf445wq3RHJjLLKMKet2pcoi0SQxWO-K5vsC_JVFHM-6INMVxL8ww03GEICKMnyynEEQYymqeh_DvQtIUSHMKkUXLftWZxS5yQUy0pH-k96DySAGnBjAZEopy0GO6ajxKsXqpX_vKrTDQQOINIvsp3E-EQ_H6YxZQW_QuWyL0zUyqdtn8W5_oNsDH-gypi0CIZB2jbDDkxJr3ZaTRfC3wFLci1pOxXv1meC1seffr-lrPbDOCTGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1sm7KEQRR0azUF_JWZdYNE9UbtgxHpk2CHWJHmc-O1Nkcjjh7AJP6iXYA4xIV4vSr-aWrdA-i3BYN-FrtkIgS95WySQXHNznNPmQM7377gWzJC2NMZDnxL-p8mFq3VZEhvDSWNiMmHlwTjVrpqawB_ZsqrJ-HQyJi27f90UAJX1DuewKJBs3P4cSme91pR_DEBqCZ-6rcX8-y0VRPbMk_8q8YRy5rgHQxF73Rdh3cUFb8OXjSWX3jxFjcoJnYKh-cy1Qi0VyMPI62NxhFfeTXkGOR4yL79mANlq_08RS1Ci4Vpe5gcKBeiATpzd0bxgqI4EzjVy7ePkp-69mG0CGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwOXtaPD3MbzATfiDoqQId8Iw2wFF12bQ7veLHxk2hDJcozLhqlATrChH_N2YmfWgRO0siMngJcYyDv4fV3M0SOnmMiXwZEQouHxPsPhUnM2qTasX952i0uAyPjeuRPRpba9RK1lZuuZWwNaz2_3SL3xCwAaJOOXlz40rEYLwHKhx3-403tyl6EzS-m-IlESLaniUL8uB9_K9kqKOeuOzM6g4Yc4KCNauqUqg3zkq46fOKetSw4M3D6V6cVqggRO7zxBbyV_C0WpcroA_yxGoaohNAhXOD869MRFR5zEZ9L_8EuQNxJeRCpoQ_HWc28fv8R4XNmhDjzXYVr5anCyHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVFV8PChr4rvkmMICcz-khrjEmLrnHm4bJOJ6tZGhiUQpK5IUxN318G3zerQ699cjPM4Zdvb_EDNBszqwVsOUsX4heA2tC0XEIEuEjf5eSTM0vLU_Jg00siEyIkJNeVDyqn4I_-YUxst5aDnAFc9zgQqxTth1VJNpFcSY1qvRDqS06eYjBf3I0sMJbdiJLYSD9NN1vDOqGHd8ERGE29HViBtV_u5DGNmFLnVNTeDRC2yiQTXFGGPGXt5dLLCPteWBeqn7K8jMQlut7rziFDcCluhEd3PZ6TsTvYkqf6WElwW16NwNXAV2x3PYDcQ0Dob2nh74pxtwe9TnMxjCoTL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlAT2IHsHz5ObwSVR57QBPxIOoBPDEeGI3x1SEXzhOGf9DylwFqA-TbbZHbtwfvnMIAjTl1MXff1M-LTL0vblu0VhJHi6DOSyma1Yjan4ux8xJqEWtWZAPGQpu-4P7K2KSPprFkKUttJyV6dPrB30wZrm2HN2nYs7m2QO8gQtxCPBsOtKfWgzkip7mTpr1zqN23Mci2FYjEY-dE6R_M0km0Fyi6KowVeS7Zwibu-AvR-uE4sUdZ1f_rFpiUbzBj1kpUO6Wj1q5QYkOontJWEc4b01WZm3GvKS8uFV7SV1ScLk_1pktThw04R2EwbOYK3dm34tDklaIIANYFQijc8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU2qBGFyadPSt_-5CIyESPUBc_JDpB7zwx_ya7re2zewqxbRBJU4jgIL0a9tgazSkK4oi7z0R5qGB9OFy2oJwP2mCMhPP8KuVGhEOb4k2zqpbeZJL3KRe7YwPe1HK0QbkUhX2X4lcPAPGF0mttkz7H16f4_yi5kR_rdXHkrZReETxXOYt-3InqIBCjCKTZu5c95xBoCaybfb8Bo1Y0WXvxboLGi3keRFTE0IXR2M-O-ThTsDV59OvuK2JS1lqB4xtNND9DMYXz1l4N63Py89h6_zsEBPias_1Az5AJaqnulQalD236TzUNl92bqf19Oy5TEJFokT4I8yYaTWsKtz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Qv8bneL-JhePkr2KJqK2doi2PzcyJ_Wfa_42-t7MLpfv2Kpth6xVpO3VaO6bP-6IcP2Iv57tQ2VqP67gQQV0_O_zXrY0669yc9P-1MUfy21Fc63AhR5DmnSc72zC0FGFMcfTwA_eOfB0DlTCBNm_6C1nP1vqwkwgPlPnqQbYaWpXB0R0QJ4adsos97WOxhiSJtEAv2uLKKRPZY_F6CUI2chzO2JW1QMwmfzwiUeLZlIANc_BPTexKR9PfI5Rd_khw9b8r_mYsZTl26ru42oE9nf3ICtlKykdo1hd4XSOwmfYiiEPKWWBkfuNzwaKBQ5F0E7SZBfjm-yL7PBdZ35V3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Qv8bneL-JhePkr2KJqK2doi2PzcyJ_Wfa_42-t7MLpfv2Kpth6xVpO3VaO6bP-6IcP2Iv57tQ2VqP67gQQV0_O_zXrY0669yc9P-1MUfy21Fc63AhR5DmnSc72zC0FGFMcfTwA_eOfB0DlTCBNm_6C1nP1vqwkwgPlPnqQbYaWpXB0R0QJ4adsos97WOxhiSJtEAv2uLKKRPZY_F6CUI2chzO2JW1QMwmfzwiUeLZlIANc_BPTexKR9PfI5Rd_khw9b8r_mYsZTl26ru42oE9nf3ICtlKykdo1hd4XSOwmfYiiEPKWWBkfuNzwaKBQ5F0E7SZBfjm-yL7PBdZ35V3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itWznLHbotQAgut4SfUfLAOVwZ4IE0Q3A3OUk1jymBVT8dmGR6khlvgRVFSvRzDTcnam7d-vxKbRISMlO6TLHy2kjsDalj29z2-bg91lbF1IPZmZMeuyftuofuWIlD44v8bPll2CRzNCKi7T0fgSuPlhQtE2DyZCKfm8F8GLgPKVcGYA1kSLqHWAcw6BDBnOyG994-fkygzPE1tTl8lOAFaBVsq9XapJ96JclxAP8Tfq4dshG7uGGjDfN_fmkaA6rrtmc32L0oA7pcZCQbFz3PWvTy3lDZLgG0DLdX7L6dmOyhxQPfL3Wj_UgYlkunl3Al1jOQ9HsfyUjRhNTSFW5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=GRiH7oKXZwGYDli9dLRUsEd6kCNY_AN282ecZMfYd35kLfxdDfYw4NApEcgzqLmzLjgfOIFngYafPf75ZTSbBWFHlyqrRAp43FCN7wDvn-IdKk2fU8sVUABVk3_B8UCoq4L1qpcX4uOk4HpRyRJOsnSrWFXxOJGcX_BGrCVsRoO8b1fTcuxky8i_ydXYXAYWuQITAlOKK-re_VqB_ndodf3qw0VnymSUG1OZ9ffGHs4JrjyC5HpP4HVpFQfL2Vm7KYq6JH3w9IWgp-Hm6siBktyOsVf473ABneZlA-SDhXtxZg6vzBOuggbnZiVeWSKb6OGeUO9EuzvCxe_kWrbfSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=GRiH7oKXZwGYDli9dLRUsEd6kCNY_AN282ecZMfYd35kLfxdDfYw4NApEcgzqLmzLjgfOIFngYafPf75ZTSbBWFHlyqrRAp43FCN7wDvn-IdKk2fU8sVUABVk3_B8UCoq4L1qpcX4uOk4HpRyRJOsnSrWFXxOJGcX_BGrCVsRoO8b1fTcuxky8i_ydXYXAYWuQITAlOKK-re_VqB_ndodf3qw0VnymSUG1OZ9ffGHs4JrjyC5HpP4HVpFQfL2Vm7KYq6JH3w9IWgp-Hm6siBktyOsVf473ABneZlA-SDhXtxZg6vzBOuggbnZiVeWSKb6OGeUO9EuzvCxe_kWrbfSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzI1b-g8Vc5oX65OVo2lGD8xKjvElmkeZ8sR55AAOSlr6NiU7lkiaV6b220GmaZyoqfriT1mQ3fbSc29GNpeVP8X5L5d4jRJzV-4hDDemky5_Nhxb1pR9YzjB3l_EDsjphJoFWF-sLxfKtmvdQ4tnD4gQMj9J1McmlqUzrFhmInvb4ynJzkzgUHLu2wFV-L9QFoxUw5hqGNzqjZH6d69gHv3R58d4VCaxm_yfvt8CFUJEPYHpEinlvisdG_LOTV7ObGwbOpOiCs6nCpUGop50RmF3_bEJealjn5albYFhUlEuYpjWlVUzDxBKulksDDPqvnardiFp_cCyUx6a9afmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGHsRWQOwdP_AxzVWEiYKQjOU5zjmtpR4m96_4gYu6_WSj08K95IR4B4fNFstV6qsreYEqwvxUbbIy9nwkOf-PNqZiRqiYFBhElTNhDKWJSSVOSZQXnia2HJ-VdN0C6QvnUXuAhzLSYkUJSXTZTLBb997lYPKn1jZ6I0kugKoM2tN5vpj72ErBkAyaQ4SxCSBkxKMc5D_WIvDNQ7XA5jAFnpCpzo6rr0pkihN0Tf_5xNTvySgkEzwlDnIg7u5tKEwtgOlVPynKAx_vvd28wlVyX6FOOIGH-DaquoRUjMjW3Hy0lwd0dnqo4SFu-1hAjitUlEBjHcPBHY8x42NnEQbHtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGHsRWQOwdP_AxzVWEiYKQjOU5zjmtpR4m96_4gYu6_WSj08K95IR4B4fNFstV6qsreYEqwvxUbbIy9nwkOf-PNqZiRqiYFBhElTNhDKWJSSVOSZQXnia2HJ-VdN0C6QvnUXuAhzLSYkUJSXTZTLBb997lYPKn1jZ6I0kugKoM2tN5vpj72ErBkAyaQ4SxCSBkxKMc5D_WIvDNQ7XA5jAFnpCpzo6rr0pkihN0Tf_5xNTvySgkEzwlDnIg7u5tKEwtgOlVPynKAx_vvd28wlVyX6FOOIGH-DaquoRUjMjW3Hy0lwd0dnqo4SFu-1hAjitUlEBjHcPBHY8x42NnEQbHtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=LbAc5NTYPM1vjbZLtJMGCDO0gyaSqYZhK4UpNjOe00tf9FIIjqSQ0fxT8kiKyg7umY7Im-59QsibaYsV4hJiTJILTapWcdhFlAE0hZyyajXlJ3lwGG0viXUWnve4t9NC_RCQExuNdRoGrABpAPsz4mcPBhLxuYprPzXBGpVtUN_T1m5iiSjXK7uD0h0rD5O4-m7alYy2b9QLTVpOen3TOeNWfCmQF1W2vGZCoznkArhvQ4G6I2evn7wIWvUwcOysCXI4yO1fmpO7mJ81IXeNMz8o_oCXqYxfIvGT08u8jRftRH0ymK6UihEYqqxlkhadx_IMpA6SnlLmYF4M_vhPQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=LbAc5NTYPM1vjbZLtJMGCDO0gyaSqYZhK4UpNjOe00tf9FIIjqSQ0fxT8kiKyg7umY7Im-59QsibaYsV4hJiTJILTapWcdhFlAE0hZyyajXlJ3lwGG0viXUWnve4t9NC_RCQExuNdRoGrABpAPsz4mcPBhLxuYprPzXBGpVtUN_T1m5iiSjXK7uD0h0rD5O4-m7alYy2b9QLTVpOen3TOeNWfCmQF1W2vGZCoznkArhvQ4G6I2evn7wIWvUwcOysCXI4yO1fmpO7mJ81IXeNMz8o_oCXqYxfIvGT08u8jRftRH0ymK6UihEYqqxlkhadx_IMpA6SnlLmYF4M_vhPQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BboOcNys1c5_UtYkm7kB4APfmKEertSq142tfliTDebpLi8wWxOyxgdzgC0AewyvjujE1AEraRuAE64nrn-RS6e_lxRsi-GiaqgEdzy0CIZ64VrUjdJ4-B3yg2FtFee-kxPZMa9JPZkdS1KiWBB7mhqR-o2bMBWo71xzG9AktBwKDlXZIOezsLzRyiKo2lgqA4OZ7AV1z38JZmRBXu6gmRnJ9tTV1k98rE9z6TjBmQMmMAxD-tWV8vJKOfVTebanz_FLh4MOvcPNKRCXCMUQ2DIStBGhVUt8haHvVRI3WIXcSOxjgRaROYa0Pyh8ubFabVccMv9alinMLy9d7g6Ss3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BboOcNys1c5_UtYkm7kB4APfmKEertSq142tfliTDebpLi8wWxOyxgdzgC0AewyvjujE1AEraRuAE64nrn-RS6e_lxRsi-GiaqgEdzy0CIZ64VrUjdJ4-B3yg2FtFee-kxPZMa9JPZkdS1KiWBB7mhqR-o2bMBWo71xzG9AktBwKDlXZIOezsLzRyiKo2lgqA4OZ7AV1z38JZmRBXu6gmRnJ9tTV1k98rE9z6TjBmQMmMAxD-tWV8vJKOfVTebanz_FLh4MOvcPNKRCXCMUQ2DIStBGhVUt8haHvVRI3WIXcSOxjgRaROYa0Pyh8ubFabVccMv9alinMLy9d7g6Ss3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyC5BVUWXuLZ3HSRRaxiugGi5n8ViAfW27FpkfAVJPQEx-uxrsgWzc4UzJlr7JqYYy5zihlGpxPhnFPv5Euh7tnscHZ_uvOTHjgxchGOukqyICtta_cjnc09K7Nr58fWR1XjIR-7tj4ZXPUIENAvfnBD_QtOr2vv0s0QRAuOAz24yMAdR-iZjriGh0cOtZNaoEvaj72gzaqWn61tHs_fjaxTCtZZYc-r1TOUrV8XPa_YnGMTOlaYh3cyqtdd5tBzkdspaVO8_mjEmZPPB7_Obe6h5-Fgt-rrYkoxWXb2FSW3X0kADJ5fMnhB3R8_dNFjoMA_EEj9Zrzc0BajFRUQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpV1rjuZQluCH7kL_AKgFvvtmBsmZWiVQBVras6i6CRTkI7wHkfHAzkUKwdglxw-qNN-uKTss8cP7U5LlRQbYGOYzONFxaJHjSgCot8LXrCQqAJhlMbXCVUcKegrjLhSu982YsJhbyFmSTwuxm7E-q3hryn3w25gA-8E2usyx0TzsD1IZlifk7qmczhmydCStv2FZPWkc8sjtssmil_8deniYKF1yXfKPGfNv3yOqxcrARs9EUL-SA5WWWuiV5YbSnPxb3uwiXzK3tR_5GhGKzev9e7ENw3HC9Q3qjSRzRbwvuyc0rRvXVlBRgrQF2ADXBNZTBwCtTT0blaNincdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzlnfmnQhxdFrq4vdDH9NB5JtqqHzfaGXKwn3zYjRMPRwcQuq0mlAkYyANVzk-FdoIkjy3bXkolccPqxpdZKxOaYxiYz7SbZCzZQrUcOw7RUceuaNF_21IMaM6H96F4xE34QbSJ0eJYi0pz2KoKHdetpTIY3pIEwKto7CF4t27p3LeqJgpC4DURLPwQ4kzKzy3so8p91LETOo4QkIxL2ERV0XfjQcqRQR72hcfajtUrx2yQOKComfWlhXzXJAf-AF8bYs0yoFiNlvzjKyC6f_kob4ZqPkim7P6hfSs_qYftfJroisItHp39NnA5IyZriG520ZgTE9lrNQV0TwhnN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yylrd27I9HVAjhbNUXbtnxNYAL2EYvTUvwDaR11bcONPeqKmyELy3llfy6-V8CLcFBVeiM-vsbgKXExj0k_dH501Ywnafty_OvhX33Vbu_5POLrC34oKuqAG0OMhd6V46CU81pB-Xc1cKEsTPfD5yhlk27UZsUpKwXpcknw08TdlGDp2aXpV31hju-gYuF-Qjf_1Xb1AB16GwRslKjmNa6lXbkevDLBZCvBOYCEqSYLMmZZZcnLyIl58CZYzCyKvRHbgFcce1l8w1-Bj98N7L-CKuSxG9weaFbPgSuAoYFVJHCx9Fbr70sJfvjXw7ALXB9c-otcspGpqr6ckl_CGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRzn1Xoys9xQbJPASlnB16u8OkpSHvlEPtPXjYcEvA3by_9bhL4UR8-SDci7VbQRmOblnfgUsUlQc-h6pS6VfBEboqjOhNMmyqbEJuoRg3XoITqBAIJW1OlwmjiOUQFqBIICK1-v8-iFc5hl9SSgPG20goi_WdsAmj_M4BmO6lLyGP3bmwKp8lafSID5vb0W1Xq4829qasBLoqG4sJMtrZQxopUqJ_ryNrAEqxlZJDkUHt93CDXvcuJM-X-mwdqaO3CdNh0BLl9WUhxELmqjRAQqcx9RP3aqA1DQCuPta2Tkp4M2-1MPGTA6V4lEji1ydPqM8suAwM8bX-E3gpUcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7ZXSN36eeyYChAeLaBfm-MLIJe4cP8rb3gqrOCH58rx6Z1SdCGPrQQaDVq2xcN5M3ZNUyQaDr0TgnIS7Aj0cli_xk3haemMMzLkzn8pOOujE0DS8C3h74M1fTGglznTuLONnzHFLmJLZCP4QlqZIKRwFT0X2cUqJ_ghF1WI8-VknDLJxwkREskT67JbPPkfio1B46aOVjfg-FCnVBXPlyzZl1KZyf34m9y9CKb5fRVA5rCAFz46R75NqYP0XUAFKNWTNFjmVRstNagzg6CdB1VheogEUBl4OKccfVZh9CB8QBffS_dhoYo-kGQ15ESzMOKsLmHqFECP2UC11R7AKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCPlnw6seN-KbcR7qJ7vRDf9A7gIbkjPiJWLJA9a6g_pnaPT2qXDJyzwTLTgmXQhFGP35goGNZKB2tG1Cp7ql1LPxCLq1sA-VMUe4xKZLn-eOT_UIOYpoiV_gHxoj4I_PKCCWMPof4I8SyVdo-wMzNi9mqjPNi_h3_ucfXqGm_HxJt890p8EciNfPiXWooB3OgntA9HF0ncs8KfMTZpjdgR8fzBQBUzPjyUiVBjlQRe0C3SrZ7h0vGIGxacaNdZRBd_W6GX2F4dX_EnAdkXPEJtRQgW-nwu4vSQCJqJpMUJaCLSKTXFqkKvx3frnZfW2lg5AdC4wq0jBBLxEwBMz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEJ1EjJoVR2E7mAPv7b9qLr9W9gLfVM6XF3UWZROa1YbWZpap13E2C8iWfqTNE6ZLXQ2mZA3OAp-d_4h_BU-CeUAdj7XLSka_lWUiPHRJsQk0XtTGCqxkUMuFl602qR4IKVyrCxSpG5UYzHszkmhqTUhRvUJggQxwc71z6JQTwZ80vi0_o6fhPr7yX3MWfyCZsKT1dxXvgCqLJIb9mCVDRccL-_4SHryWXfuNqalI_xCnhcKPetIjcUu8-4al3STsBC2fWC_ysdv_T5vGyFRHX75jaH-s04okl8SuynPu4vjF2yv2PqsFEagNwlh_Xnp0246ma8Lqy_QtpJk22JV1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgK8y4BWBTd3z8o6TgZNyjl7sWy5lsnji6C72a0ZmrfCXhj05t3jSrjhlqlM0gL_ivLF1rW5PnrmhGrsm3pmbJFVe8wd91lF5fAu_phICK3kLptC6vyVOZJJSsob4XJj2DIQx0h4_jhTDmEKrbYXw9qkZiDB0jp3zMpSv11-MgAn1UymlF9vid94CO-TkOEMbEOVM4-342SxGU48U66D0sffkgSxO_YXZMetEnkf_lLkI7teSEY_UoHI-MAh1X8fKbAkbC9mNq9uxQj1734vSOcSkdIQWQd62h2TiR0dk7xgeDKphQ8V1lK_XTHVqsa8WFlRMPMh-XmMlREobl4Qrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
