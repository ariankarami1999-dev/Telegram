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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 15:38:44</div>
<hr>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov-5teW3tHTvsvSbgMdLICYXYlU_sDGIu9OuiTSl0594zrfs9gRoJQR8S28V2CiP_XCjD7Zzp5uItinMqAUIbUIRvVFn3zxxaqYh9Km-0nk74uSUdeQvuMYluMHfHS7WfmU5Mq1R_o1vTjHKfD6MlZEq2Yf9KVRt4d2gzoWcCctXxlvrZ83-13fvHD4NvwcgSfJHIpLOCqzOAdqDTCE-6frq1o_rpZ_dr6FZtGyKaUvR4uN5aL7iKlIR-aOJwWaAcP_ZJcq4l0tyEkcUu7cd1nNA3Bm7_vFPEyFbPsYQr_SdVeOSm92Zw0-QEekuDDdOwCr60iw-tbsukbzrBFNmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHVVCza4-k7lMKxM3gRJStW0mSmbHx1HOC_kqRItxfPQPZo3RqgLfbxvjky93wErqiutSbOoRDVDgJO6-5Gt5GeEQYp3ZpC8LbmHHVvogV5fTJ8tjv9WUtzfZpz5NJscTMxYul7zKui-uhcGtGwcbJz9kr1kP6yA61rGmmeIOf2BDf3B7TQdUT7ccFphzbXnhtP5luogZEm_0Gi7-eRD7KumLBDmDBfFnXn0yVHUWnWFFsbkQWbKqce98C8p4SF3LVslyiNzTK7TUUb1kdRXw9U_E3m1dmBOkEfxlEWe_yZkhLuLgJrZdcC01kX5yYjphMbJYFfm6UDxnofukWHSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtqbusLboLN9-Lrqe9rkYIJx_IvHR84ZEHryWdkZeDoRtrOqikXN7EiCJPyxhY0K5n1MEgMzgzs5MR0SrgnYs_3F8GgLoDYdKQ1LYTW7Xido4AUaYEQj0QO1zbE_UI2rRR3Xjp2NfzvzJlA17Y8-RYrjCC40HPKznslTM8wL2b2keXdTihMVSAzhrWsKM2zE1ziTnSVNA2CcNqGAk4EUva6MDz1HAScSWM2X0YSeo7K-8tO5E-3qzHKOu7syOVXFFTPwzsaVcApsYq8y_51MikBazPUNTFYfJVOy4371oGxyqsfjv9LPjVEwVrFbGqSg_gT-daVP7dZWwSQ_f8DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRYorMv_LE_7-u6f5repCeg_po1RsblXfhsw40pFXv_a19PNIksiD6k4_mG2C04SxN4cxINr8twFLhPzip6-95c0c4ifpKDsvK_z86O-1jTS1Z0Uf-WdsmiMPeynab0RfSXWpHV162_pPpC9Wvno9zW7pPMd2DYD7ddx_AqsazarvaPpN_oR0rhFYKmbJPynGT9OChXVfulP-eNk82T0WoMxy8U3TaDCHx10eJgR4HGLdNzy1dZbrabPk6YKS74N7NrgiqCwFaXcUW-lZlnruJcqwJFWHOv2nTsIsN18ww1lxZ8SHzYLGrzQOdTnCBybI6lS1yU-Nt9TJ0Lb9pQV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpbSRpAJNOWT7GKMBce7eh1uuHCHClHAWp9foEppchDzoi0EE6futb3R08DdwB2Enf5oct2gZT_lYZFXIxhKQOz1qQ4KAskg0Wz2xxz8vkoJrqcjldNRariu01LmlA_L06jCrU3lRXDssg6EunnRBRzSF96Wf2wLqPHpHPO4nY_CSZCAVZKdD50lRwlrA2RWoTmBEmHj54mGi1KL8qFqkvFwPyeO9jW_D1h7U2nzWua1cvIpggabt4lNPLU2QEi1SOeLeKrovu548Z0u16YHcGHxSVYIbse1YC6p00yL90yQM_o0lod5FcQA1eDWm83O3khKUb_Nc7ibczl2MOqx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsuMVwbycOVcKxuIsl8NhNoah4C8Lf-fvDjm9Qx_apRKyHEmvAOY39Pg_XtQb1s0Satath6r65ylCGxZ0Epe7_A3YyqakeYvcaNRozmd-hDudHiUXQRKs1VL0pCMueM9rAIHksMWSYN7-rYaqPGiaRYgXmVuLk8iRkye2Zv-ySE90tEjfd82Nc_I_suh4lAZd8Y0O4CvgtAWQsRiYXGALnytfvYIkHBZObGkDGHWta2AkziBjcfS4twnE6A-rCgYSZiCWLNL5r70ggzVB2fJ8frEXWYv9IBkZL1kJsacTZCGSp4ReGAROkc3slwLZO96LRaYHpJpCi7kGWhGmtir6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk6fphPF7k3GAXKniH27qXUdVZijx136CtDbuOAq0OBZEl9OeXV1Pszr9daS0G2CH7aZMkw5Cn2ftqgqBFI4q-_pniyjcykRvEc8RCyseJZt_rivU95z_joaDJA0kSXzjWWE9MuOV2ynElWJp4Nw8b_BGD5hicnT5klD_szuGWAqr7L56R5zdYGVTgfaADOXjoigXBmPO5uG6VRKYmg7RH6f8epGoGniHMmvlhFXEywxgpwsyrqOk05qGkmW_rwSb1hgG3VWuh5Eai26eQP9fdm5OHFXZDucPZf6pPOeVTO9aTzm4LdEq0YgJGlz7G47N41UbH4QlR1inWtAc3eCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6brwnxT1KHRZ1oIIDlge8EKLDpyqE-k5ojbhuIWve_P1e2hOaIzxcKxiYFp5t_FKUWpDK93JPKxmsD2f9k6VpK0Q7ylFw4QKPoUsrx-RBwlbZBCg6iQgc3XcKEm8V3dgdsKMgySEi-Vgl8_Gz5C3LGc4A6HOSH8Uir-6h76-9Ds_MNPGVJfsmqXiQUQ5oU1dH6VVKyHmgEuX0F475bYz31iR3JP6LKP2_6sp5s1CgrKDRB9XR2UOxtOPswelfiiWpcM5ZEy8OSMjEXVagRH0O2IvzOrA63mfo2StM3Rg5GiLMqgPOXybErSYq0CYEWR5g6WEXZRhoC95X2JTmjGOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFAQexToODT0YsJuANiC3d59w9i1ksL4YvoT19LWtYK9W12QYju2e3q8Ea9LLp8P6mB6FYXbRA6y0STeEOBHBad8R7CRqtkn2DsIOtHgXahJxdwT2vBcvOHkmo2oESkhRgllbu1GVC_Yue3G-Qn-HPZHd9meW0Lx4-zKkTV4p15yW89vjvHw-wPQLX81AEy_KrODuQyZJNYpqGTG5h9PUWFF3CU_5ShpopGIjgDpkUkbJt4F82hXjSb_Gkm51s1EG2PGNp_CwCinAeSRngUvRA1GNGv7csguknPPQs3FQV2z0bemwQ8xA1aS2C-dl6I-ynG9rhI2_y3O3zW6Apfk9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BraOqL1PzsQJUh9QcK8tsT0BEzybzRt9LzCOHPYdDyFexgnvNZ0k-Rt3GJM4XoJ_zETF91bPA3zWfTRO6t6gBltitZkYo60iDbHC3KSRyJOAv_a4i4P1rHEQscNwK-KbkGFlnO3UGLvEB7H-YJgj-xTVImDY3hdQQEQ47qomFvUAPj8rUqNI69E1HmylfaBgjBtdtb_dNqfn6-RTAAEQs9AYf4CzocabJFZfXjEvGJRZiGuqUR1glYcVT83hDcJBFj6-aYYypNlwnIrY1ywvWZUv01WZkvo9aofIOpBlcXdpeN88QInkr2hg1Nsjj95ZgMEaQgoEq0B9L0a8flncfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=u66MiQTknMJIur4e4u_Fr2SjD2OuQctbCQP3_CXZgMfPSvgg6OTLOpcaitNhduhczATQWpjQEzuty5TNwbIVN__KQ2LL7rUjA6fnET34qfIcJCLoFS4llLcJCA_xFQ8Dp8BhIcsy_bNY0MWySowG7bjpmLbhcMROEcNg81ZUMYipCY_EjUB5iqJOT4jfiEuA_8qUXlW5pIokZlLf58WOYvMJmnoHQu1oRvBVPNUCDfCDqpA5xQ6g-ZCCvM-b2kkGt-XpYtZMAuwurrXm-Pyc0tQu--IzI8IcT_itsVRWzP0fZ232Ra_LiggKEImSCPKLwT9gq3p_N1IMF_2DKft2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=u66MiQTknMJIur4e4u_Fr2SjD2OuQctbCQP3_CXZgMfPSvgg6OTLOpcaitNhduhczATQWpjQEzuty5TNwbIVN__KQ2LL7rUjA6fnET34qfIcJCLoFS4llLcJCA_xFQ8Dp8BhIcsy_bNY0MWySowG7bjpmLbhcMROEcNg81ZUMYipCY_EjUB5iqJOT4jfiEuA_8qUXlW5pIokZlLf58WOYvMJmnoHQu1oRvBVPNUCDfCDqpA5xQ6g-ZCCvM-b2kkGt-XpYtZMAuwurrXm-Pyc0tQu--IzI8IcT_itsVRWzP0fZ232Ra_LiggKEImSCPKLwT9gq3p_N1IMF_2DKft2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=gTxQXrpp9CzJeNlZKcA72orj_o4o_gOSM9wQNyZOG3tdP67eOS0KrjoxA1fqPwRuruof0v-LDwF3t1ryY_9l0CQTwrqnfUNlSZAMbixfiAgIyNOX_H4gjm7ra1oAT0lMyt4hIbJ5LykhqiuL4tkAMg0NuD-h39rNlXRDmbqyc9dbMvRrdzCfv3PgFkRrNfAksS5UjKD_XyAZT0KYxE6zDPCGtqN6Th8kzHjE5Gs4MFZJPGbMToWyUKnQCN7CwqGk08kL8GSw_5mi5KUxQYPZr1CvUnXPdgJyabvBvVhaLu6je2FRhFa-Q9qFtt_po1EG3JtQVvhbz1zRRl99BGi1Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=gTxQXrpp9CzJeNlZKcA72orj_o4o_gOSM9wQNyZOG3tdP67eOS0KrjoxA1fqPwRuruof0v-LDwF3t1ryY_9l0CQTwrqnfUNlSZAMbixfiAgIyNOX_H4gjm7ra1oAT0lMyt4hIbJ5LykhqiuL4tkAMg0NuD-h39rNlXRDmbqyc9dbMvRrdzCfv3PgFkRrNfAksS5UjKD_XyAZT0KYxE6zDPCGtqN6Th8kzHjE5Gs4MFZJPGbMToWyUKnQCN7CwqGk08kL8GSw_5mi5KUxQYPZr1CvUnXPdgJyabvBvVhaLu6je2FRhFa-Q9qFtt_po1EG3JtQVvhbz1zRRl99BGi1Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKNUd0eFAQ-khREvIYfGqifTpMvd__l7hFHEdJu9tI-8RRptcc976Y-gnuYBesoL_ZksYdE55KIx_5exr1Rx1mbSrTMVIoCr9ttmufRhN2nKOEJSWtnGv6_-5mMWXNha4GJbYRY5McqQ5CjnaeBcRIylgsonO10T6jj9jFNKFGMljsqNMeGNMpokRQjUbPnGja8px-YvZOoK4s-QNGkghBqcAsqyjuytd7-koyqzOLgyj0nxS2ZtNSUu4Aw9TO1NyoVY9DOSwTAgpjtxe7KcVDEu9B-lm1dmGTzjlpwSifO4CsEVfM6dMzYfmp7OZ1ztsVe7JL6fqS07NgikBVleyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df4nlA4zTffUNQtbFzyQXzTek2ugUaD0dXTDr798h7yciG2NAstHPVcXviC8QcFmeBufJJ3vj_gM0Ko4PtFTnDsTqMaJzlKdjz4PXKwC1OmvP9SupBNHECGtpaf-Q4Il2h9AgTtzq-eEKGNTkD8pOn0H-DnSDYDnCF306dpEAEPbRh9f6-5va8Imo8SCgRzxF5mvtNvfebE6f9jqD8wh61wvuV4dWjHvTaHKVSOsRf3cIkMfnDL24DWfcMvCZ6o3mfr2y082bOAPWOm6HunuPUe-4F4jNQ9LPZpN5CamqVJ7hqRY9zt5_fuXxPBlCc7hk9StEJi1YCd9tusS9Qwk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abnk58ZVti-SiWdDIxfvdQYd3LPIq84ZSwLYM0V5adMLT21eAfzp_bvqjKwQWF95ycwhCt8zcwepsjT143GD1rgwZQZvQuhlpOZkuoDNwCJTYQzacbi3cKt4VackVuUM74jxa1iVtgOtLnqK2Yb6KdMafAe9QrelBeyxFB8bd4NpaEYtL8W3oZeWLm-yKfizw0J2PxWR1hGxuBrlEXIryeN4oH0AIk_84Mt6YrFzvNFNJLRAImCTPrjzyPzxo4rV_iH3cnqkQvDY-_VvVHwyEUm_JrmvNB7hj6R4OBr3OGeo1W5ixkvCagMcmApCQFl9rxJ0mblmYBzQ0c_L2olY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUeFcCi872ZiTYGYJoq654nsJ8-qVUSTsfo9M_yz0WGCsokwHVDHSDuMWPF8M4S0diKwLmEtdbAjd-ii6kDuyD0CXTM5OLZPu5-O8urLV_Et9GOz0MkXUSVfhZ_ktCiTR7dRT7PSp_tNqypgYfQOMqmHJ-x9bxuvLDxpANKmYgEe6JOxjTgyuzCs9eKH2dHhDadra8DQMo3oH7PxRaXXDD8zUdw8_b9k3_lXlPcboFu1a7FxHR-I1p53qPExRlrvKjJiuLQZ5Jf3_lz4u0YpQi1a2mMwlZZkDe-jZrsCqW4Az0D6mNF2MrrMhq6u_HAtXN5rTOZmddU7b5ufDFeGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw-c947nAWEwGYFTpM_fN2_K3Irib2XFYJ40OO2qj_bo2dRlzhLay2AV2cFJr5spRAOAFdl135U1Wsn7s3PApHoWUBlC-8mgIm4RFidf1LVBOF4bu9J6h6lOeF1nhGl4dLYu62H2_DAW6UBjFHNxrUrnqQg1eQRcSp_c5Blgy1esApVTFpT_VMRITX8MQmsxh0KpZnK_xHl2f3NADaKzK3l9t5VyM9jdGb58udlvWbQeG0ypqSyEQHoN2Rm3XfgR_1fQ_hdtgwwUd_PzJGhjBLxv_z9sLbWt8clwogjYorq_2bzVaEjhCPtQAGgJwLGWJfwm5jWMDbVJokHvj65nNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f80_P0Xg9Qew75uqG1P5OIbpGgZ2B8GDWH0mtfJDF8nKEWajqyk-yFGIfUtyQ6ZN7FA3itmcn586B8JYcmz74v_5-cDfuJBp2n2JvkaUKzVQdlM_3gqfAn1KgnZJ-iG9Uq5PULnvp3XRBRJH3uqtyF4h_58cK1oLPYpVSDOmQ4dvW2xkArBYFpJ7Smgdjg6osKmmkx-1834pTZBOPRFLTgMq8zkzMbhkTY23aryrloMl8U_uW4NskWrbCxdFQIElV1j9ho58cWyfu5Yf0ouGSNmEh63usMpWypb6wjQwL4g-T5-V5b8Mae_sUDWRow9IpOZ2Pb_tqasMpjr-Q0puXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=dPDYAG0xj_H4-LViw-xVY0cXEMd8IDUS__Fr9lK_WcJsTXnuLc30ZpJxs9drKV0ODJiWVpbVooge4agcQuqg_zklR-MyY8OhrRMDwtaScLOcPJ-N-oQKMVlUrxlLhdsyQml6irESlVR8XwUouOkCxgua7YkhNyDX74n6OlX4QlCwy_hCcDiKKgL1ZurNxfuAyIWK-1cEuIQxI15LhjudviI62pqJ7liw-nOzNv3PFVPt86VpzABZLsG1suG2QCxF3Xf6lmtkavOq-Eycopsj-ihsX5dJYKvVQjcnp7_yubh4inaWID8ebiCTpyxtrbvvVIreNVa2LRqZHmE24D4ctmSlAucdl1S1n-WOhgEthSiKKUPJrqD7EAwWIM0WQyF81EMLKAEVdMM4_CDC7MeLn7nN8FEqMBtusayx7MMDg6eS0MRF2y_FY5xZ7-uu6P9zvRBSHk0CFYL6iQrUGvr4mkSz0dqCV9yzC4jUTM3DZTUdgGmerrRrnngyWXu01bfa_Z5moKJYIhLzOhH1a4EiXC71R03bEt8K-YOKTkJHCOd8KGu13Tm7WqU7MPbocnBHyDRxVcPALGALNa8YNmwNIUBXN-P7T2vi74Py7PGDhRI5HVsWgs9NYw8rHRiS4A27ftejj8L8KlTv6D3FFqTZY7uDwSMNcGCs7U8y99w-rYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=dPDYAG0xj_H4-LViw-xVY0cXEMd8IDUS__Fr9lK_WcJsTXnuLc30ZpJxs9drKV0ODJiWVpbVooge4agcQuqg_zklR-MyY8OhrRMDwtaScLOcPJ-N-oQKMVlUrxlLhdsyQml6irESlVR8XwUouOkCxgua7YkhNyDX74n6OlX4QlCwy_hCcDiKKgL1ZurNxfuAyIWK-1cEuIQxI15LhjudviI62pqJ7liw-nOzNv3PFVPt86VpzABZLsG1suG2QCxF3Xf6lmtkavOq-Eycopsj-ihsX5dJYKvVQjcnp7_yubh4inaWID8ebiCTpyxtrbvvVIreNVa2LRqZHmE24D4ctmSlAucdl1S1n-WOhgEthSiKKUPJrqD7EAwWIM0WQyF81EMLKAEVdMM4_CDC7MeLn7nN8FEqMBtusayx7MMDg6eS0MRF2y_FY5xZ7-uu6P9zvRBSHk0CFYL6iQrUGvr4mkSz0dqCV9yzC4jUTM3DZTUdgGmerrRrnngyWXu01bfa_Z5moKJYIhLzOhH1a4EiXC71R03bEt8K-YOKTkJHCOd8KGu13Tm7WqU7MPbocnBHyDRxVcPALGALNa8YNmwNIUBXN-P7T2vi74Py7PGDhRI5HVsWgs9NYw8rHRiS4A27ftejj8L8KlTv6D3FFqTZY7uDwSMNcGCs7U8y99w-rYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=UraFgc8kkbDCQhSCYec9-9t8NJnlNWvRVaIckTnXCb06JiealdPixgNgspWE9z-tJ3BNTU8yru7WwjhA3CdHXb6Yy9A8D6CIV1x2GqmhvTl7rLz6koIenPi5DXUaqKwEL2pp7WcZ5F8ZjqTjljRi1GDBeIweFMaSqH0RYr2WZ0b3RTI4epkYE8QRlD0GLuMB_4_OV9LIlZ-7aGt_EZ6dxpd92FmHZA7ZYJRk_5y0z4J3owMbhrO2jS4rWYt_TlfErhTaJEQeRuudyJQDJki1PbsEPf6RorQZ15AgBvV3oo5Ehksf7Ttis1u2SyDMGLxh7zijE3-tDyhAjZKNlrvGuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=UraFgc8kkbDCQhSCYec9-9t8NJnlNWvRVaIckTnXCb06JiealdPixgNgspWE9z-tJ3BNTU8yru7WwjhA3CdHXb6Yy9A8D6CIV1x2GqmhvTl7rLz6koIenPi5DXUaqKwEL2pp7WcZ5F8ZjqTjljRi1GDBeIweFMaSqH0RYr2WZ0b3RTI4epkYE8QRlD0GLuMB_4_OV9LIlZ-7aGt_EZ6dxpd92FmHZA7ZYJRk_5y0z4J3owMbhrO2jS4rWYt_TlfErhTaJEQeRuudyJQDJki1PbsEPf6RorQZ15AgBvV3oo5Ehksf7Ttis1u2SyDMGLxh7zijE3-tDyhAjZKNlrvGuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/um0AzoUOnj5s1XPbbCKtuhDMlx79G9gZsA4W05J4exdRrbToaJkzILiDgNKeiCq0UIrgsAUWi5B5PkBd68KDI8hA9VYMENNTVrchafguzAbSAiF0NYzjauwcSv9n8wluIEmzdRvkLB_fLbw70Y2G8V6AOukQccY9ad-aC4bTxG0m5aIOZHdu25AyrWIDptg_4D_Fpj5WL_jZ0IVlxw3_h3w4Q91J9Vqj3ak9v_MKayIDtZceJ81u_8N3Wpmcaqkb2Z2G6edqOv7I6-ny1iFIda8rbcHwursFAvtskWkXk43DaJABGTIvTJdg454s6pHhrUTBWqTgwwdMaKpViRvnew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFN-syHXGcSK6Ka1aIH7jAOrcm4Ep6BPe9lCUYCw6Fc8iMQqEoe9v6Lz4ECbkCcmWwUa19Q5xNozZVmH3yM4mwbNDAmelfYTcaNfsqoIKe6Lwf9kCWNy-gCUb2PoBMYNp53J4wzb_p-zT75419uXdHtj1ILDYyCqEe-W-ZwIbXuGONDnYRnM24KY-stqmushg-QejtKr-muvZ3RytlauYWC6_P7Y-LZ9Z2Gx8xQFKrhshZbaGDg-qUKydKCXu_8FKrD_MzHlCxXCYE11_ZnHd-VvJP94BgrfKPaylY35Vwx6wd8FUB3KumtUOxV2KG801JUueujgx7UNW7mhK5Y60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIT7MISoxY06QQqFuJ9yKybgYp9Pu3emK3JMxVgHFsKSdJFD_CEEi7x94-dsauu3Ed9biC_w1ylZtjTXtgFlI0-knc_lTuTjxbZrRFiPOIK1At-PMlMmvQ4iyvOcLn4j1Y6fFlts3ueck06MsJb9KCj3mzzv9O-MinKRI9Q3yaqbslA5CLFh8mdHSyWjPtNnPi5G1GkH7m3JhD3vm5IGHh34Yn8POQ68ypcUP2oDiUMhVwhvphZ-XavpO3Cm126iyQHhp63H3-hcIEKAroSHRHzaUgUBxLxAS3HYQdzTm7yx8Cl88HmhN5PybhaOsGK4BQO50-biIwr2msyvLVSEiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pArXYaBpIfdpLxqzYzVIyfC1g23DfbUpwQqWkrlCY6Kgk3_whdTSrdMuuHuVavDVFsdOhR7rGoeuF6JDKi3kmsWTWPF6Ne5m60hl5mi-8dHINCLHqcz_gMn3HzLFzOTmP4QhXC33s34--M2aU2dgExnSs1QaXJ03TrRRszcz4baOhlcPac54_qTM9XnyfZAoU1NroXJC2vIHDtgGcuIhhF2HoW40StnM3cUtdPds9grCa5xD_thD5J2SVLD_qTLHFuqq98AGwK-OTiFKv1jFhT2BRewzoPR0uCVLCJ8yP7t4dcYFgtfxQmSvHOhizJAkKP13tnShgVoRdFNAZzJMEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTckSklrGequ4tQtSyNp6hdMKk7ecndKS5vlWKZIKtNacSNNY1Lft95uhcD3FirOLd3OtFa-Jn3s-jieGRiqBOaAe78tBOrELJA52bDDLwEvdTKlxspSWzC4g3gp_aUM9zmsYYufNPh0E_Ak1yfDBJ7fU9ddjkompKk44ssNe-pwXiKVyxtZp_y6pUfliopVwB0B5EfwFB4X6I0rfgvORVevNZlt4OhHK5SaoTNJihKwsaiVMrsDX320QQzFHP_Hf9NSqgztlybrO9pOuii_v20ZdDHtfij6R4oZVM3MU-BlYK8Bzo6Kx48asYcDwUdEDG6aUzwupECT_Hy4-Qb_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGCWHQ_bWPmbQv7DvgeSrKJgseqy_wNmUFmkFInE0oCRdd34kBIjVzv5qF84qWm_EMM6VnTegCGsOxv8IPbshIKO8X6mP57282jQv1UZIgWJxeRSmyWzceoZzejrmWLu13N9eaPb4LwQgz_vQuUJDFB8X-9ooC93Ilok43MO7Eqp8cgY85f5Fa2j7TVhslFdzOD7lF__OL8mcpfHziHXL6JHOeI21zoIrHPqNSz7oEiKGqob2F74ZwdjT_5X73JbefCUtEoWQBUQ9Vw315q4Sl5wHbvfJ_S4ltojxVQ-8coJ2y_eTg6RkYr1x312VVhh_dArngUt0N-qsj3MPrzndw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6lJXsZclGbg87UAZcfrbCM1vaYDVpp_7qRJMgRuWj5hccFea9V91OpSRsBoBN_vZURyY4CAL3ChwWe_iNxLP3djbXIRUrlLRSB9-w8xxMPfzjhCpSrKeoO7AnWJkPbF1qrF4_oDNxWlwccZQAldTzT3ik29JBi9xaxNh2MxFjbcDCY82Pa-pSTrSAO1sw9hLGZxOv4NP8de0GD6MTlnJCupgjKRmo8vIJxVqNdpDSQfx5Z22ux7MyjVxpdjCQtwxWJcQhck7UcrIcs0EpBgL886kr3FZ5dpl_pAdZ5IJR3PxWVOxcHHIkLg9MDfkx2FLL8CCghBlq3b2jkaLMymdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Wnv-fKN-VSnqXGt1LH2cR_1nIisneROBZlahbZELdltRYHaSndu6d32lKEvjBSP6WUDp2RNkBaBgr146dngWeEw-8GvA3q-XLksEOC0ptqAL-SedaRth4VuC00xSM5kbg9iivLaVhrm9dJmaIQZqHb7TOI2NVNMH7ibDyr-jdT9asCi2lw35yRiRPZYaU2mZJs1bToTAcMh_wZT041CRYDYq1JqEyEuUCGO2gf_-IEflD28v9k-DQtTzxH8HII7HovGVJ_xkHX3c1N_gHpwAR-Yexeh8g5OgMISgQkKna8GYRiXKKdQiOCakZEAWcbEDonABlrU_cKwJD08MfSQJoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Wnv-fKN-VSnqXGt1LH2cR_1nIisneROBZlahbZELdltRYHaSndu6d32lKEvjBSP6WUDp2RNkBaBgr146dngWeEw-8GvA3q-XLksEOC0ptqAL-SedaRth4VuC00xSM5kbg9iivLaVhrm9dJmaIQZqHb7TOI2NVNMH7ibDyr-jdT9asCi2lw35yRiRPZYaU2mZJs1bToTAcMh_wZT041CRYDYq1JqEyEuUCGO2gf_-IEflD28v9k-DQtTzxH8HII7HovGVJ_xkHX3c1N_gHpwAR-Yexeh8g5OgMISgQkKna8GYRiXKKdQiOCakZEAWcbEDonABlrU_cKwJD08MfSQJoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLFTBa9oOChRfatk16nX6mZp57FoaxDbOxkn9tvUjPo1zvtipaHWKntLBNRn4TZEB8CxGjvneynA4DoPALf8oJIpt7GFwywQrsfAauk74Mo5tn-x58AnhcUI5-GeS-8DiBf079vYWlN5GT-BPqrJOS9nBRLITiaMggZUt9XpH8Zy3hZVEymbVCXPPJ0gABxMnkxTpCSeuRQni1y0OZ0U0CdP9LLQTintHPEm3RA98gtuqdBS4V7uN6AWcrJZfjsnY7pL2NjXLVAEbha1i2pPQ0Q1gbzkpV3u2f1w0fB2jEsVKnbNmKsNYf2iqcSCpsFxuddkmoClNbU3GsEBjMwovg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ZSixq9DO5fDXU0o8GzEfvK8SS22pWSk7LoI5kXQYprQvL1zzqhJeJ4bBERJde00ge7l3J-VCOQmIUYo1PjO1Kydih-PFBGV2_lUnH3Le8jXirO6tkTpTrd8wCUkjRLxPEOMb5B4lz4D1HuoJ_v2EQb2JIrKnxssSlhE4LljZURXiZVtSO8iSjYjXvPkI1Q9qIJgt-_STVTXJZGPPBPHyzsQthoJI6nNykiSK3fOXMg7ZnAyokhk18njbWgEU-ow0qJ_I7VwioYA7JB8k3IHNBiIcxHuFXBOKhlOhrenHXgixGk0329lOmoQyN8VYweNaOt-PQ-meo9BALCK72XQH0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ZSixq9DO5fDXU0o8GzEfvK8SS22pWSk7LoI5kXQYprQvL1zzqhJeJ4bBERJde00ge7l3J-VCOQmIUYo1PjO1Kydih-PFBGV2_lUnH3Le8jXirO6tkTpTrd8wCUkjRLxPEOMb5B4lz4D1HuoJ_v2EQb2JIrKnxssSlhE4LljZURXiZVtSO8iSjYjXvPkI1Q9qIJgt-_STVTXJZGPPBPHyzsQthoJI6nNykiSK3fOXMg7ZnAyokhk18njbWgEU-ow0qJ_I7VwioYA7JB8k3IHNBiIcxHuFXBOKhlOhrenHXgixGk0329lOmoQyN8VYweNaOt-PQ-meo9BALCK72XQH0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQVRnE5UfbJ_dBvyQYT1XC_khdx83u_mZ52pyzZ9xnYnLGGgfprmscuHPFNxVJL7EjjutbOAImRXNIRz1_BLGU90ec71F121EBlTA7jtfyAaPL2oV8D3fqawTEtkuymYY_v3BL_8SNJLsXBJqQMSKSA7BNPobz8qoVrtIYa436SAObx0XIa8Bxm4P1SsgfITvF9nQMoDMztXJMM4Kczbb6FoSpY80ks16GJpgzxb6S2mXOxnWCncdcIMmjfdMIWVRWD2DoP7xZH8Njsd2vU9ZSXNYTfFYRDvSMTX-x7Np3_i0f8IA5U-ExxhR3l_5gAH8UrDxBws9YmyQoiuMigqFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJ-p1OhcJrv9SmxE4qxrD0QE2ajAwa15zJvrC_VL8JKXtcVvn6I1NFQOPhOloP2lx3-IIJdO9FmpcOdwi8KMk7ot8-hU9kleWHKyJhE_CqkVEFopSdJLGVV95VpFTEpML8lyCXUz2EUBmSHwnhyrnuis-SQKJ_GT801HWqk1LkvGakOTlnpKuPctNsd4uaULGA9Pc3emcCcrMLZgV4-qorvr10gvJgI795uvLnPMIn7DnSRfk9zzo0OAg5fyQlK2l037WGYO5QXzDS3lnXcUd5iqFX23nzMnL3r_2cRX40fSRvs_XnqX-Obt5Bk_Nk4oI0nP-v_cBAjSVaoL1b27JGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGJ-p1OhcJrv9SmxE4qxrD0QE2ajAwa15zJvrC_VL8JKXtcVvn6I1NFQOPhOloP2lx3-IIJdO9FmpcOdwi8KMk7ot8-hU9kleWHKyJhE_CqkVEFopSdJLGVV95VpFTEpML8lyCXUz2EUBmSHwnhyrnuis-SQKJ_GT801HWqk1LkvGakOTlnpKuPctNsd4uaULGA9Pc3emcCcrMLZgV4-qorvr10gvJgI795uvLnPMIn7DnSRfk9zzo0OAg5fyQlK2l037WGYO5QXzDS3lnXcUd5iqFX23nzMnL3r_2cRX40fSRvs_XnqX-Obt5Bk_Nk4oI0nP-v_cBAjSVaoL1b27JGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=PAO3WW47a1s1EQrdSSIyjPJ3qjSLqdMtyPEQ83Bhgq4XZzAlnB7vdvR_jH6t3HhlVlrAig58Uf7r1_SPUe46oDSXM7_OA3Ub5gG2M6isIw5mCubw35099Fwpo3aMigE5POpHMfMgcufOMuYqaOou2f6WIeoicikdEgg1th3qqb_oJ-r3yt-3F5BsIcQckVGyQhoVoM8rNhAc9AlqfvtgjXU-Mh2pME9NctOF-S6q8XZuOIpNM6sj6WPKomwreOWhhhfxZcf40C90FVDLX2pWIae_eGt48u4smhZWZ7s99TY9K8smK9MC74C2qAy2mi3RfaVMObcd6PFbAqVTGuUihQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=PAO3WW47a1s1EQrdSSIyjPJ3qjSLqdMtyPEQ83Bhgq4XZzAlnB7vdvR_jH6t3HhlVlrAig58Uf7r1_SPUe46oDSXM7_OA3Ub5gG2M6isIw5mCubw35099Fwpo3aMigE5POpHMfMgcufOMuYqaOou2f6WIeoicikdEgg1th3qqb_oJ-r3yt-3F5BsIcQckVGyQhoVoM8rNhAc9AlqfvtgjXU-Mh2pME9NctOF-S6q8XZuOIpNM6sj6WPKomwreOWhhhfxZcf40C90FVDLX2pWIae_eGt48u4smhZWZ7s99TY9K8smK9MC74C2qAy2mi3RfaVMObcd6PFbAqVTGuUihQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXjuOF-ddWNUE0oRlHgS8FoJhxuGJQy4hoGe4urKWOd1QueAV33fvGZwvj-DznZpI3HEFNu0RR8lr6xnpP5uS534_4stYZ0qMmGbj0Ie-23RqJiDcl0TkkmjFEJXpO2hzoM6RsckCooGiPKH9vp29SVvPwAdskODPr56rb9NB9hy1CrKd5jxQ-bk99WaXe06QB71z_RSE038hYQFXARpGF1j4up24eQVi2sNhl9kkL8ocyNYaaCWaiUyLJEHeWu8OhS53aAgcKX8qQZFi4lFMMKV8NYQnq5wSVbnIeF00bUUxRb_S12kjFeh4bXuw_wvYZ4h_qH6THC0IoyTNaA6Stk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXjuOF-ddWNUE0oRlHgS8FoJhxuGJQy4hoGe4urKWOd1QueAV33fvGZwvj-DznZpI3HEFNu0RR8lr6xnpP5uS534_4stYZ0qMmGbj0Ie-23RqJiDcl0TkkmjFEJXpO2hzoM6RsckCooGiPKH9vp29SVvPwAdskODPr56rb9NB9hy1CrKd5jxQ-bk99WaXe06QB71z_RSE038hYQFXARpGF1j4up24eQVi2sNhl9kkL8ocyNYaaCWaiUyLJEHeWu8OhS53aAgcKX8qQZFi4lFMMKV8NYQnq5wSVbnIeF00bUUxRb_S12kjFeh4bXuw_wvYZ4h_qH6THC0IoyTNaA6Stk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRMDC6iLP4RUgarMF5Dhq097ZTeXixMTa_jI-tZT5cjAXUfOCaRAs5gleS29RvZdDQ6W6TNIkFrVlxfkrm23HSxaaBX6zpbD6DVXo3_pE2dQb_oPbHhVxYpyy0G0rA7ALKRzpJ4UF1qtoCcyThTZy1X-oZXuh8YLHLbFOZ-WfHA74E-uG3aZPCeviNYFmx1SVutdGRo6_OdbtRygdKh89RGooXMK2ESNb11qGPSQtRVY6ajwPucRVAdC66iCTcPN0YNG7oV6SD1DqO_SYwTFDPot9jk9b_6gx2n1nE2-Vo1RYUomEAqt0XW2rCtbVmJ3FnxCCFDmDGeSpbrhuhGenA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t45ztkHOM8E7-kg_j10KS5GUwVk-qTMKk1qbrCBiKI9nvHDQLR3J3Vj0q7yAkFLQMCiEFr1xQ7TYXYLUYyDZwB-a6a8X48N3qEvrR2XvolXhV6M3FwrRszrMJN9TzstzkaS6twg37_ZAkLZN8ZQkrAqspI8LXJ80-HM8HdZnx0AKbQ0JW2bejFuRZ8yAbMAbkjE5MnxRnyGflaZZZTt5zqXx0snr4ADIN6ud7TcaOSlol_59TnUXWQDEtSNRrVF98vE6pTbomQ2fpITBGbJVxf84V0f0fvjEihmR0KFvKtmGwybYnkZol316CiGbCAQuu3l3-TA7J2EihbBCjlX_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6IkKOYLZ_rowCZfBOdo4XUn93EMV5iMnBwJ6M3aTXCa7jf3CAFmGaJAC77ke5fY-r2UgCXnSplWo_R3oANXWTdlj-BUVXIYsryyMSrOeJOjNRo1Se00-gkMlGadYLdigj16OFKxLdZyXjY69rwgQNofXElA2G9_EYF-8qHfV6cPVx5YyTfVMOV_GMPbjmqBB9CMMyCMeRt_KyP30MBAAQhJNNlkgbzKQYZ1C_MPfoM-OtVzu7IQyzGSDHNQLXG_zoCia3u4zZvzMV1eQYVv_FK8yR33l63z7kMW1M_3DGgBTaS6J2sHgk934YJKwJWCfwEPXRpqXMYMlF12StZ6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv4GquokpmGr5qQuFlhkw41WX9kPiR_bmyUkBT5TxNPGEllGR202mISWkYFJRNOIdCOg4H5m0kpBrEXGjAR5BCRoeTUJwNuhv0c1ZzcfUYpwsyY2fPmakmV8xMdVXjRA1npcasFZWSA0MdPeQSMRD6KG8CABXB-7QyfBSm7ozz0fS23e5a-vRV2XeFO46_g3GIxQ_OcIJXvsDCg4QWvSduwxPF5gI8taq7RZp6y2eiI98wB1cN0eDD9Irsqz9HTb3KukUoWf1hAw81PjCeJH7HQU_lKqQvD8PolvouFzQTmxRKVyvzzvuZMKaKdq4PZdbL98FtkI8avL_7rSXOe7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HA4yDIIClmwR3KS8PnS-AP-dMfB44NUudf2-30TeWt7pi-DEfTzFvnGUG-aSxK9nAqFqPRi3zGawC9hZAWeZ7jCIQDo1nJjNbbYE2pvXyi-ZQBve33RUYPSOfuHIGMOa1pdyuZZoCugw_ITE1tvenrNe3q9HKtwe5CEEpOR9gcr-XiqdOSlhrHL-MR9Le8sLUgaFIqS65R1MEqzfreJqLOJ4tv9NGKMfjHZAqrI5z9ENxsLVMDzvlnGDHdpiWBlz1CENl8ETwPC_zQDXiolE36IAag-ErIafo5gKFZsyw9tJFLIY-gOdFK4cubAcPqFDeLt6YTuH3E8L4wP17ZGElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwbS3XOVxoDF2mE73KVhW5eVjAeNZMwkcR8uF2VUh0v8mkIZaXmol0uXAKuzgGEIWsLrMEGepnDPIn0s8TCLMVUk-T90LCEsq-vI_AEyRNJdSfS74FbttN_ueHUhGRp1xXYigIDis6RMVenM3L84Y-q7qx04jNczFwHCTXaycgKMR4DvSDJb-ca1kRPhLUE-G9_ILvrtrWDV6FnSXvRKYCAyWXCMvKhNXEya4XsCwUUAaxa0zeWtcQ6BG7KdWDcHRCKrngxwodecu18t7C2Gbp9tXlp8TXd24kmNlZG-LxujRzn9Z28soAlQzq7WWksUXaKxqCVoHQC5SSkQl5iseg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-8h_TI7VTL55Aa6bq9YsrRpDOtmRSkH0nmRLL4v_knxLwxYisrFVcML8YFdKVWWI11RHLbt6PNSwbXqqu_sIVhHW-qxat5XLzA5he1jSTteLgiDBRQW2SJr56QevzyNDGCrlVMuVN00v1FVu8Z_pxyYCSYfy34w4B3bB5CuyBtlBRXvTdQSUGLCTnuBXZv2Pq48eudJS2rYdzthEwbZjSrcwbGtsz95F5hIKCLHJTzrG4JTshs1ukUOjGc7J_ZbSserV3LN84MdEb0IuM3FgYgaypAXHp6pxZ84Gk5EcLnF0ngoPy5aNh6Kq10Snqu6JoE2gCDvYdu8Ct5VUblGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdD6yIssuBkciFmd_Lw9tnJCZE6kiRhRJ2t5JXhia35O_gXBUPuE08fuYbaoQXxpuNROvh3zmwX-wmbkZHCozJI1tEvO0Ps1wAnNv5OrYtFhNEGeJzS-X2U0ZqEpNmwSUdDTd5C8Eu3fYWvJidiVHXKJ8Fa4u3FLT_y1-fdiigxjT-Wq_brOcUaMAoEyG2skC0yD5IO_gRS1XUCgvsgP2I-2eEH_MtgqoKGFLLBkjl4SME-0Ht7yhQE7tK3xP1RQkPmUxnuZsT3c-L388LqxdBiurHgs__1ekUA3BOK7lbieHPZt0i4CjJs93UQVzE10eVUTO4sMODm-qSt-v-sZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtJk6x0v7r42NXH1jT78MWAK88qjwaHMos_YtA3QEREZj71XQVXdWexbosC9UHBgJqKTqjy6hTdVWaRDNhC0f54BXc3kXRwrhKFhp4KOTJ4NGgr6ybfDsrrmuLG4P38Pnzn_OnBLAFPIs3-S1NAk4tmioFIhqGlNJyn3yqdYd_TefDov857krpM2RsLUfjokhG2ql0k54Eqn2Rdi1fXO7OaNlbPzfsn-xWJu9VZqUwgg2YIetowqTVB5wbAaPGTnPx4odkcB215GzAESBZw9--M1pdgc7pPwuTeYgnVklMWcCNqY9wiUG3dDgTXfXtdpR2wyBOZ_39IIqASfHtolFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
