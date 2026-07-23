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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 18:09:18</div>
<hr>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov-5teW3tHTvsvSbgMdLICYXYlU_sDGIu9OuiTSl0594zrfs9gRoJQR8S28V2CiP_XCjD7Zzp5uItinMqAUIbUIRvVFn3zxxaqYh9Km-0nk74uSUdeQvuMYluMHfHS7WfmU5Mq1R_o1vTjHKfD6MlZEq2Yf9KVRt4d2gzoWcCctXxlvrZ83-13fvHD4NvwcgSfJHIpLOCqzOAdqDTCE-6frq1o_rpZ_dr6FZtGyKaUvR4uN5aL7iKlIR-aOJwWaAcP_ZJcq4l0tyEkcUu7cd1nNA3Bm7_vFPEyFbPsYQr_SdVeOSm92Zw0-QEekuDDdOwCr60iw-tbsukbzrBFNmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHVVCza4-k7lMKxM3gRJStW0mSmbHx1HOC_kqRItxfPQPZo3RqgLfbxvjky93wErqiutSbOoRDVDgJO6-5Gt5GeEQYp3ZpC8LbmHHVvogV5fTJ8tjv9WUtzfZpz5NJscTMxYul7zKui-uhcGtGwcbJz9kr1kP6yA61rGmmeIOf2BDf3B7TQdUT7ccFphzbXnhtP5luogZEm_0Gi7-eRD7KumLBDmDBfFnXn0yVHUWnWFFsbkQWbKqce98C8p4SF3LVslyiNzTK7TUUb1kdRXw9U_E3m1dmBOkEfxlEWe_yZkhLuLgJrZdcC01kX5yYjphMbJYFfm6UDxnofukWHSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtqbusLboLN9-Lrqe9rkYIJx_IvHR84ZEHryWdkZeDoRtrOqikXN7EiCJPyxhY0K5n1MEgMzgzs5MR0SrgnYs_3F8GgLoDYdKQ1LYTW7Xido4AUaYEQj0QO1zbE_UI2rRR3Xjp2NfzvzJlA17Y8-RYrjCC40HPKznslTM8wL2b2keXdTihMVSAzhrWsKM2zE1ziTnSVNA2CcNqGAk4EUva6MDz1HAScSWM2X0YSeo7K-8tO5E-3qzHKOu7syOVXFFTPwzsaVcApsYq8y_51MikBazPUNTFYfJVOy4371oGxyqsfjv9LPjVEwVrFbGqSg_gT-daVP7dZWwSQ_f8DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3cy1W2TbhAEaNqko-LkofOvGARhOPamsqF0vCHGyMTA7VOKKvkblmGFd3Z1Cmu624_ja_tAa8n_bbjHmnVTuhNxKTyUxVAacVcYG-q-bRFg662UE5Tria8Te2IEuiazcF5nA2jXoZYHbcMMvjn7bJRAgoWnuSmKAPfMRR3VWB-izE8iOD59w2umFAgheoI3F9cBvPYJO12pwPuaKptJ7YQSh8wu3vjjT20WB8oaFhMleR-Rvz9k8qJK0iV9UMgIccuu8fRJNoDpaVxYVJ8kU5i-VJKdGxh_NlssZVWq_v_rSGXU4LXxVobrRtTg0YWElxLIttczbSrrKRw_7LA-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlt5ohzv1OdqdVm8v4Vv_IX-0JFxqy-G8oYJBsuVCZ0WE2qfU_wROvY65ynPOmrX64NDu1vsIakWGR8vtT5mKHiFbPmRag3vXe7UCO-ac6X3kFZtMEYOSBj3paRx9ihuXJUwNkrzDcQC7bhdWgz1hGE4R1GRCfhLDJMbgLqIUpf7f2sXPUilv_xg2uxob9rxE3JcTndqTsg4-0U2ygixisi3tvIICsmZs1VA5ZV7iD-CYYvf8wrUuw7GQd9_Uy-5W5UAehUBa8MWmeYo45X6O2MYhXRRi1pa2cADIgXL4oopEXqLay4Dun6X1ZHV4RSNCEXLfJZxw1XFgqS1ctKtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsuMVwbycOVcKxuIsl8NhNoah4C8Lf-fvDjm9Qx_apRKyHEmvAOY39Pg_XtQb1s0Satath6r65ylCGxZ0Epe7_A3YyqakeYvcaNRozmd-hDudHiUXQRKs1VL0pCMueM9rAIHksMWSYN7-rYaqPGiaRYgXmVuLk8iRkye2Zv-ySE90tEjfd82Nc_I_suh4lAZd8Y0O4CvgtAWQsRiYXGALnytfvYIkHBZObGkDGHWta2AkziBjcfS4twnE6A-rCgYSZiCWLNL5r70ggzVB2fJ8frEXWYv9IBkZL1kJsacTZCGSp4ReGAROkc3slwLZO96LRaYHpJpCi7kGWhGmtir6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk6fphPF7k3GAXKniH27qXUdVZijx136CtDbuOAq0OBZEl9OeXV1Pszr9daS0G2CH7aZMkw5Cn2ftqgqBFI4q-_pniyjcykRvEc8RCyseJZt_rivU95z_joaDJA0kSXzjWWE9MuOV2ynElWJp4Nw8b_BGD5hicnT5klD_szuGWAqr7L56R5zdYGVTgfaADOXjoigXBmPO5uG6VRKYmg7RH6f8epGoGniHMmvlhFXEywxgpwsyrqOk05qGkmW_rwSb1hgG3VWuh5Eai26eQP9fdm5OHFXZDucPZf6pPOeVTO9aTzm4LdEq0YgJGlz7G47N41UbH4QlR1inWtAc3eCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6brwnxT1KHRZ1oIIDlge8EKLDpyqE-k5ojbhuIWve_P1e2hOaIzxcKxiYFp5t_FKUWpDK93JPKxmsD2f9k6VpK0Q7ylFw4QKPoUsrx-RBwlbZBCg6iQgc3XcKEm8V3dgdsKMgySEi-Vgl8_Gz5C3LGc4A6HOSH8Uir-6h76-9Ds_MNPGVJfsmqXiQUQ5oU1dH6VVKyHmgEuX0F475bYz31iR3JP6LKP2_6sp5s1CgrKDRB9XR2UOxtOPswelfiiWpcM5ZEy8OSMjEXVagRH0O2IvzOrA63mfo2StM3Rg5GiLMqgPOXybErSYq0CYEWR5g6WEXZRhoC95X2JTmjGOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odxN9WnIedtZxQMTtaYWdMLESDN19f0yV_MU7Zh5AxnB5w9I1Ngay-EbdntKC6yHnulqJl0bFJOGV1KrTqD2vcsUb-L67wqluZ_XZzuHMirtEHGsDodmqn3IfFA35qJiMkd1tSSVgko9mUeFfjojvYIjIn3Zx2fo_Bc0XfvuJF6Ce-3_ml2AZ5wurIt-dwLOH6cU1TdTLr4Iv07ahidHV06gal3MREmSYtLmyw63luEI4mK2igk01QBOYDjRvz2dUc7fDfspr3TdVO7NNYL0a_1_qeQVDnB35gdfNSwDdkU7rbL2UN50WC8LiPteKMCLNO7KWI9RMwW1k5Pg5Ai_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=EQW3TJZdyJfTPfSR_ewV_Vqs0RVJLYVXhDGosozgLZbLtTljZS8GiphUUxXfqXlnDG5pK_-C3ExH_ZC82WRJ9jZyJMWvIDFt2A31NLaPNxUlxzoECOx8D3NpU_z4DWPKHz-jgmsXgN7MWabmp1wg_0rHKsC11FL9Y9kcgyTF8dnZlJ2HViAg19_skbOP8qo-0yJA4tG4GgMSf5p2c0zE5hv8dcH01oH_mlBIVERHw4FJYuChHk0Y0AvfWVyrXUFE0pg2DQ_fDD9uYbP5PI3A0wfXrG51i63pgiSTwdXVefeifq1tGggU-XfE0FMzgPX9AGotdpGAo1ckoTdjpu_MUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=EQW3TJZdyJfTPfSR_ewV_Vqs0RVJLYVXhDGosozgLZbLtTljZS8GiphUUxXfqXlnDG5pK_-C3ExH_ZC82WRJ9jZyJMWvIDFt2A31NLaPNxUlxzoECOx8D3NpU_z4DWPKHz-jgmsXgN7MWabmp1wg_0rHKsC11FL9Y9kcgyTF8dnZlJ2HViAg19_skbOP8qo-0yJA4tG4GgMSf5p2c0zE5hv8dcH01oH_mlBIVERHw4FJYuChHk0Y0AvfWVyrXUFE0pg2DQ_fDD9uYbP5PI3A0wfXrG51i63pgiSTwdXVefeifq1tGggU-XfE0FMzgPX9AGotdpGAo1ckoTdjpu_MUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=a7vysE9JNcbgeAJCf9saYYaYd0YWO69hybiPlWLXqKUCk9uw8aEpzYy_Jyfh94_GCbHL62NPEWbloTMNhhCtYwFu9IGXtK6FUKHQZFQ-5P7Yb8O2iNbvDa8m1uxWWftEgM3YupTTC-K9IoTEartS4kEbhpM65gB5AQBIHurhm6_oJqdEuiRZW8MSkPGPrt6J9y65_STB3mpbRhkJw2Jd7duwMbfZLCw-DaPQUCFSPTne0iKQggN-w5JFYvMq0nvYMvYQbYb60lEKVzOr6-SX2ktWbVqzvh_9gnoOSt-Zj6DDWLlefuZHDb1QycH-s6aVcdBvJqt9_vHuQFuyzFhy-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=a7vysE9JNcbgeAJCf9saYYaYd0YWO69hybiPlWLXqKUCk9uw8aEpzYy_Jyfh94_GCbHL62NPEWbloTMNhhCtYwFu9IGXtK6FUKHQZFQ-5P7Yb8O2iNbvDa8m1uxWWftEgM3YupTTC-K9IoTEartS4kEbhpM65gB5AQBIHurhm6_oJqdEuiRZW8MSkPGPrt6J9y65_STB3mpbRhkJw2Jd7duwMbfZLCw-DaPQUCFSPTne0iKQggN-w5JFYvMq0nvYMvYQbYb60lEKVzOr6-SX2ktWbVqzvh_9gnoOSt-Zj6DDWLlefuZHDb1QycH-s6aVcdBvJqt9_vHuQFuyzFhy-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=mxHRKJhVPIJbfloEhRJ0umuAiOx6LXDzjmzMC8sXUcc_wvipcVr0DDt3TDamqaGJNj7cH9M-3afKb12OHzlvEY9cyCRyCRMuKJmll_Mw1MnNXCiwkkRlKHUEV0i_Cxm1cfWgBwIkwBdU0aQambuv3VglNSUM4T_7_Po5N_DTbsEDKmNYfPH8_A3tJAjXEGJZeXpimJM92Z0mMN99kYDuAYlP4PmRDYL6LEWdglu7Ij56xk7CiafQQc1svEcYPJLIN2FBcKuXUzlHb8YjFJb-epsyQJUZpy3R0y0ucuryoAW0a1SAZl0Xf2B_UqOmnB2cNPuHmfX82v0en_gJoROsTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=mxHRKJhVPIJbfloEhRJ0umuAiOx6LXDzjmzMC8sXUcc_wvipcVr0DDt3TDamqaGJNj7cH9M-3afKb12OHzlvEY9cyCRyCRMuKJmll_Mw1MnNXCiwkkRlKHUEV0i_Cxm1cfWgBwIkwBdU0aQambuv3VglNSUM4T_7_Po5N_DTbsEDKmNYfPH8_A3tJAjXEGJZeXpimJM92Z0mMN99kYDuAYlP4PmRDYL6LEWdglu7Ij56xk7CiafQQc1svEcYPJLIN2FBcKuXUzlHb8YjFJb-epsyQJUZpy3R0y0ucuryoAW0a1SAZl0Xf2B_UqOmnB2cNPuHmfX82v0en_gJoROsTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUcUgblp0XCisTeH8HgpfxZKbYofQ-euhwMazZILJ1XHd71oxmEDUcNgbuXsKQjnWRudwiIr36QE0eqNSJI-y3Vc1VET7NOYOMOk34r0rtb2mqRXn81CT2o03Qbc89zZWO5qMfnhMwqT-gp_vP6FloIaxIli7AdmUUTbPJ1iHvfRkQS4lCB6sFO4c_BMtH_jl9N-NKr1A2WCmtp3rqprS72z5NF_s958NFoZRanew7FfHaKQTes3IUY_cghG5rp2Ik3PdIfrw-le5H3ZEZHUP8EzHDqFPTnabMPd2B-XDYai5BbGnlOST7U9jggYUgBBKPY4Z-zrvnbc_XLiDxjXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=OhdSlLa36Yy8pRXL94xdX6lMnVHmvLhukxUdUtnUwGTQXML_xp2Elpry28coUcKomRnPVV12ecXctzb-js9ZNbffqhZfg3NP8tsfHufP55OW9tw_dwKfgC_iAvFCjv5aQRPD3Dl2EK7wXNi_34mTh49FNzrwCWy4UmOL5zrft1K_3z_orPMWlBdnV0ZYVW99mNEt3xyEE17LrsUNn1LjbLBujSawqTqtHrTQSa2-_swJl0NmgE-jczzANR9sOtd8RF65lCw_SEJi0Jmf_IBdQLpNYwh2FFxY03Be9svzgxLV7nwe3b5sO5vDKLY3TEy-PtJvB9zTt92h9sN8p_o75w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=OhdSlLa36Yy8pRXL94xdX6lMnVHmvLhukxUdUtnUwGTQXML_xp2Elpry28coUcKomRnPVV12ecXctzb-js9ZNbffqhZfg3NP8tsfHufP55OW9tw_dwKfgC_iAvFCjv5aQRPD3Dl2EK7wXNi_34mTh49FNzrwCWy4UmOL5zrft1K_3z_orPMWlBdnV0ZYVW99mNEt3xyEE17LrsUNn1LjbLBujSawqTqtHrTQSa2-_swJl0NmgE-jczzANR9sOtd8RF65lCw_SEJi0Jmf_IBdQLpNYwh2FFxY03Be9svzgxLV7nwe3b5sO5vDKLY3TEy-PtJvB9zTt92h9sN8p_o75w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=eUKq-jsXS-BlVPLjGMWJ8Jk0MOhlyLER8DJpisTyZttP3ZpwCnL2lwNswk9GZ9u_oB_C4ZpIDmFUJBGiwIuj2LFrE_KzMM6VE1ve1l-01Ur72HPAKBlDgEVTl2nG1TeKz4EMnqw4eN6e2ORVJnZUwUZqije3LhvPCBumLHgzZBEb_k5PTIiUoRb2pZH5hCT1Ek9PSG6Qxx9c0E_2y-0cJHCLfyrfSvdvM_X1d9JUS3C6TybDMYCvbEuGoETgB4mQTJjlArFpqRqdBY7fRAusGkWBbIrIHre9-iUebmrJlmTwMs4dqDQi87A7mguSML9_VTKS2C8bYtvOHZWn4Ddb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=eUKq-jsXS-BlVPLjGMWJ8Jk0MOhlyLER8DJpisTyZttP3ZpwCnL2lwNswk9GZ9u_oB_C4ZpIDmFUJBGiwIuj2LFrE_KzMM6VE1ve1l-01Ur72HPAKBlDgEVTl2nG1TeKz4EMnqw4eN6e2ORVJnZUwUZqije3LhvPCBumLHgzZBEb_k5PTIiUoRb2pZH5hCT1Ek9PSG6Qxx9c0E_2y-0cJHCLfyrfSvdvM_X1d9JUS3C6TybDMYCvbEuGoETgB4mQTJjlArFpqRqdBY7fRAusGkWBbIrIHre9-iUebmrJlmTwMs4dqDQi87A7mguSML9_VTKS2C8bYtvOHZWn4Ddb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=PUcEqiJ6GxZDlTSraa29GcspEwQVi6DdFUEqLVnXl1pJMBWlFruo9TWofE5Cb9e59rMDchshu0PeDsNRq_rMTBDeCZVcJChUwqqJVb0GIj4aHard_zEZOS7IafWAshO9uQNecA9G9z5AczxdS1hWn4ZGFQ5Hju6BjX4F0wn-MaFWOvh-cz6J7Dn1PISVTS6ui0J3K_AdFcJaVmF0qQnrbB0RfEuHzWMQpRmOUr8zb69TtAZKktXhzG1r1JN_gCEvNk4tDdZ_J0lqrNI9I_pwMkGGekaSs-DxMBcAtm-m3JuZcX_mi9yxzjAjK6URiRpYd4dpUSh3yM5gE7ROCygeSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=PUcEqiJ6GxZDlTSraa29GcspEwQVi6DdFUEqLVnXl1pJMBWlFruo9TWofE5Cb9e59rMDchshu0PeDsNRq_rMTBDeCZVcJChUwqqJVb0GIj4aHard_zEZOS7IafWAshO9uQNecA9G9z5AczxdS1hWn4ZGFQ5Hju6BjX4F0wn-MaFWOvh-cz6J7Dn1PISVTS6ui0J3K_AdFcJaVmF0qQnrbB0RfEuHzWMQpRmOUr8zb69TtAZKktXhzG1r1JN_gCEvNk4tDdZ_J0lqrNI9I_pwMkGGekaSs-DxMBcAtm-m3JuZcX_mi9yxzjAjK6URiRpYd4dpUSh3yM5gE7ROCygeSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=nobojVIOoNNvf7lMftzvMlCSOrR-I8N-SDxWzGZovaPbS_TaqOYTpEnGAocpHNyfytCeGEQjXGZFnm2jGARzC-0Y6fA1Eqt5avQHkpnUMPHfpVbrrb33EQj5nLO1ZzeESyDUdUo2Njb62DDk9v9s-DsdwGfmcAhCIUxnOBsIhOxbv21dXKLLiouo04q6lHt-RRtffR6C4UQAufddNwtSs0cgGbEVux_Izj06tENyF2KOxmLH_BEqnL0JnlXnWXlLsmBrRSN-GH6f_pfXMTkj4xIpzVyYl_rLmBKPYy3B7DGNTJfT8b4CF43EqdPVda0zMYPRAVMEEuuhDiiXpzzKAFxhvIf_wSMTz29KRDcPfmfTGIeYtoj4z1T_6tQGedlHO8Aolb4jmk5Agyr2Wctd3xXgfk7TaUpQVzvW3taaYSDn4_KcNvg8fCN2l4tyaU3iPxegCr7aIUDwWButz0cR1waNWB334ybYT-wmTD1D_PvuKkKmkIvS7tXa45r8IRQFX3VMY9RKjJzZGCK-XaP0PsCXT6j5aF9oeYbRBzrB9bl06mqkaSv13gTnk-5p5vi41woBjCsz3ltvGCkexyQDUTnGEZeNfE5I8Y0VXV_ws9N6DxMFYDXkGSoKPX51vXEPZdopXNpo2FtOBAj9bGKlbyCyPEnRKbZTvT95U3Xy0iE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=nobojVIOoNNvf7lMftzvMlCSOrR-I8N-SDxWzGZovaPbS_TaqOYTpEnGAocpHNyfytCeGEQjXGZFnm2jGARzC-0Y6fA1Eqt5avQHkpnUMPHfpVbrrb33EQj5nLO1ZzeESyDUdUo2Njb62DDk9v9s-DsdwGfmcAhCIUxnOBsIhOxbv21dXKLLiouo04q6lHt-RRtffR6C4UQAufddNwtSs0cgGbEVux_Izj06tENyF2KOxmLH_BEqnL0JnlXnWXlLsmBrRSN-GH6f_pfXMTkj4xIpzVyYl_rLmBKPYy3B7DGNTJfT8b4CF43EqdPVda0zMYPRAVMEEuuhDiiXpzzKAFxhvIf_wSMTz29KRDcPfmfTGIeYtoj4z1T_6tQGedlHO8Aolb4jmk5Agyr2Wctd3xXgfk7TaUpQVzvW3taaYSDn4_KcNvg8fCN2l4tyaU3iPxegCr7aIUDwWButz0cR1waNWB334ybYT-wmTD1D_PvuKkKmkIvS7tXa45r8IRQFX3VMY9RKjJzZGCK-XaP0PsCXT6j5aF9oeYbRBzrB9bl06mqkaSv13gTnk-5p5vi41woBjCsz3ltvGCkexyQDUTnGEZeNfE5I8Y0VXV_ws9N6DxMFYDXkGSoKPX51vXEPZdopXNpo2FtOBAj9bGKlbyCyPEnRKbZTvT95U3Xy0iE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=I69wiWiT1ar0KqNIlw-ASwb5EtAJfRSS_CiHCmbivajrUsnj_CW0-pd8_ty1GKd7GTq_TfDnCNyp8exYIsBJhGFCS1Oc4n3ZJe6Asn5LVJFhk9oFSa51LpmcyxZ2n_6iqwpfyjr3Bggm6vx-HwU4Pq8PZABTs0kp4o7p6-8O4j-OZpxyowMsqdjigofoJlk-yHd62ueHPk7RZIweRreAFFgjIqeF0NBsg8kdvDZ0-2uNVCgSkfenh6JmtOG9ES1vHZBnNyFYUVhxlFoNdXlyl8yIU7TCHOeQS4RSweY1oLFLGBr2XME1Qh52aUlar7_LV8LcB0Ypn3XKg4CdB4PSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=I69wiWiT1ar0KqNIlw-ASwb5EtAJfRSS_CiHCmbivajrUsnj_CW0-pd8_ty1GKd7GTq_TfDnCNyp8exYIsBJhGFCS1Oc4n3ZJe6Asn5LVJFhk9oFSa51LpmcyxZ2n_6iqwpfyjr3Bggm6vx-HwU4Pq8PZABTs0kp4o7p6-8O4j-OZpxyowMsqdjigofoJlk-yHd62ueHPk7RZIweRreAFFgjIqeF0NBsg8kdvDZ0-2uNVCgSkfenh6JmtOG9ES1vHZBnNyFYUVhxlFoNdXlyl8yIU7TCHOeQS4RSweY1oLFLGBr2XME1Qh52aUlar7_LV8LcB0Ypn3XKg4CdB4PSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=kUY0QPPBSVLUjkJdPGLw8V8JXTZ60-qzS92vZY7JrrN7rKC8G6cAnLU8thxeeERBQQ6WCxmRI6f_xxHAytbIQ2XxQTT-iqELXxdZEpp38YmbPm3CeTfDoK2eU6tSbHqVHNbUKjkv9LPNbAY_ABeEEEKZPHLkB0o86L_Bt1FG1sbQdWjJpddDcJRmGqcwoWTiFBIIU0njFDlvbdWpi89YRhVl-6-UtRgKVrdzN0U3yuw7WBvdW4EnrbGRwhm2LnqV0290dpK3ahvug9k13HsJhHOLhfmnARccF09fkCODCVcZpqCeWK2Dme1JiwPodaixR8zZ1rcami_U2XScMGSOAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=kUY0QPPBSVLUjkJdPGLw8V8JXTZ60-qzS92vZY7JrrN7rKC8G6cAnLU8thxeeERBQQ6WCxmRI6f_xxHAytbIQ2XxQTT-iqELXxdZEpp38YmbPm3CeTfDoK2eU6tSbHqVHNbUKjkv9LPNbAY_ABeEEEKZPHLkB0o86L_Bt1FG1sbQdWjJpddDcJRmGqcwoWTiFBIIU0njFDlvbdWpi89YRhVl-6-UtRgKVrdzN0U3yuw7WBvdW4EnrbGRwhm2LnqV0290dpK3ahvug9k13HsJhHOLhfmnARccF09fkCODCVcZpqCeWK2Dme1JiwPodaixR8zZ1rcami_U2XScMGSOAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCEZYW9i5U08VdgB6WWAWohCsblAtlpJL-HTXEWUwDNilBEmVHKHQLJLn3jlAS-1XacL8D8p1Je7oOq8zwjd1nVZPw7z1fmdZAFt8TkcOU9NCQXMOC33hFAIw2GrQx56JCum_7l37f4GIa0RIJ293vh3ehtHM6aj1ixHA3hvjkhGrzyk7P7m-F7-BPvJGm22-3ctuF6t4GTKDpw_xf_k_SDj6QkPfcdIIP8CM44HYqRZvSKKJ3VGLlwoXwMpBuSguzSFml9mC9I8QGm7SawShFZI8U2utOP8Q2yq_jMvzpLO7MizekgQ5KYo0WeT-RyIIPQQLRd0ll0GToV4AEznaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARVCYsG9u6LbE-PWnl-Lt2IFAilqpt859ZrAoJ4_D7p5zYQ2L-dxdsFSoRTRXczIKCN32hV9ctxcS2-P46ak2C2JQGMUeeqU3FCOnZ6BI7-Nf8JsrQT3gE8qEjgkRY-YJeYwQOI69uwqli7G84UyeT91fzGG6PJL5lAvYCr1B_73ke7ZvZ0z9MiA3WPjIAKvyl11xhJHY2RQvrbSnemjbHb02HSCXf6vG7pTGW-LVEzrs5LLu9Y6sJQpdK1yI_WbT5xXeWqweE4AMQwkWIB_Uijr1r4kJISeM0ibGcBnYjdc2K0OqVLIRATt8tTocuMXcFe_IvShEoZbV2aRVUmWqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=r4lbM1oKLCM3j7nfNrfpuikbBhimG7kzcG6jEfJuzVRHSC2X3EDaDVYXKfiRQN578gjvW68SU6kBlhk34S2b7NqVr9ZkepFM2xpn27zDNaclycqWDID7e3DsNZCt75lUvNoV0grf3MINrUkLnbL1gA0AHV5BlkecyqyxC0ZuU2Z7NozcFqTcFgdctxoCSmx70jbn0uSE0T6_is44CNNs8k1Wiz7xthTJ8rpAqGBZiCwJm-gFV_xlgpSbGgihztuCtGB9mREV2OYWrUfVvIiMMCLvab9yBOaVCi4lqJykvqse2r7GByY6kT9AaxQAKiJRdnWAodjMXSD783XQG6-9VDGtNGR4MVkUGo7SRmDOplwtUeE4mufH2Hgei0PpgVjmQuIORlDq68p4YwvDiwRQsstera8YCzSf4Gu57BYiGZRQOOVSoWZDXSPrIx1mvsPkspUADAnUWkBaHlL0ZOCgA2SSiiY_ZiK4Nq1pO3HpiARtcEI7HzuspCQvoOsuWvZYkM25I64iza_E2R6FCPmXMfOHg3egKxuU4oeekyDb8OpelEO1J8KdnYDULUhcTj9pLkhn0j5gP30BldTlRPWFhaILO4J8aSiPGsQopQzzxTrxUtY1xIlpynlI94RStXzjWIR5Ar1Uwibfmi5eFlypbKyC5pis3xYHPTLDzHU7Oo4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=r4lbM1oKLCM3j7nfNrfpuikbBhimG7kzcG6jEfJuzVRHSC2X3EDaDVYXKfiRQN578gjvW68SU6kBlhk34S2b7NqVr9ZkepFM2xpn27zDNaclycqWDID7e3DsNZCt75lUvNoV0grf3MINrUkLnbL1gA0AHV5BlkecyqyxC0ZuU2Z7NozcFqTcFgdctxoCSmx70jbn0uSE0T6_is44CNNs8k1Wiz7xthTJ8rpAqGBZiCwJm-gFV_xlgpSbGgihztuCtGB9mREV2OYWrUfVvIiMMCLvab9yBOaVCi4lqJykvqse2r7GByY6kT9AaxQAKiJRdnWAodjMXSD783XQG6-9VDGtNGR4MVkUGo7SRmDOplwtUeE4mufH2Hgei0PpgVjmQuIORlDq68p4YwvDiwRQsstera8YCzSf4Gu57BYiGZRQOOVSoWZDXSPrIx1mvsPkspUADAnUWkBaHlL0ZOCgA2SSiiY_ZiK4Nq1pO3HpiARtcEI7HzuspCQvoOsuWvZYkM25I64iza_E2R6FCPmXMfOHg3egKxuU4oeekyDb8OpelEO1J8KdnYDULUhcTj9pLkhn0j5gP30BldTlRPWFhaILO4J8aSiPGsQopQzzxTrxUtY1xIlpynlI94RStXzjWIR5Ar1Uwibfmi5eFlypbKyC5pis3xYHPTLDzHU7Oo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSxvF9zYIy2IpHgwsKJ6qfTfepn413wUSNdy5-e1B1dGqMmkZIiQNiNe1cQLYsBgE7oWI__izwuADIeW-TwASJ4bAKLuf2P09__w2hYs34RT1tBS7rb-figkso0Dedy_SwWB0eLYKPJk6rN5NJMowl_GaCX8JIoPVrbuNHsHfyGoQs61aqyrnXHbPWdwBh73UVbITanv_oydBXal8gCWlH32gt2BRe3ZzWrve22SpItJnKu5Lm9hiQFrEtSG4ds6l19hUzBhsG5vCg6EzxmVjV1R536c4vNBn9wh9ZwqpV3Q_S19jmRK2zUy6fRsoj3AKzyN3p0o4JZutjlituV0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6kvTu5XAUC6zOyp-fKFGZGBETMdWEhTgMNGsjrH2JCzeODSjO9cKYx2m_SKFNVqGuxnZimJHkXeUUXJcgPhZeGgRiVJDCS7jU-8DNBkjhEDLFBdkd_HVpJuTm5P1zKLIPc5L9a24VkzXUnwvcIaw455XbrcJDyej4d8cYmIHI1K0Mw4LEp9SucZFvBctlhu1_ZgP9qRHG4pgpDjViGkTBKf9pWtYJofZWtxEoRa7aZ4KEcTufjMPu5FC1jGcL7cu_rVUJibWzJxQ56WIeHusKhBrmhmTAY4_nNI9hpjt5H5oldyz5Vo3TCiRaydY_EgtCaPAME81Ov4dfJXLCBdtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyYdIU_T9Wo85TmHFxpoWT38LALvaJKKjR-9cC6JFzfXVjOWlU7rkPcbaO1Jf4hGUC5GjL8z4MPyZkgQR7tjMrgRZDe1N7U7jrhzNLvu2MmdrNuDTUUt2BohhUAn8HuUXX74HBTJQ2k6HVAc-8TbEVSj4kseO9Uj5NLRsJMXWkq2EFo2s2WyhfGSw_uXaOgPALCCb_3twd-M6BIQgRWAeicob6bSwZtl0TPgu05cm241VE8tYuxf8E_yn5q9q3r8fLY7qn2fIOfaEzP9e87cnRiIp-rmX-jzbsCn0u3rHRVAaEBwXN5Dd9CBNalXG8n_49FU66FHAmDlfyNmQPLDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_drF-orrQ6NqYkA9k0HK_pXyzbzbrWla-vhVQiv_2h7n2q59Bi2PLt3OtV0ArVo0ShrwSspHQpf3gOJwP7Qw_Uu9kDi-vgYNRDHOqRIK4Vr4dl45oTRFME5HS74dUxa6LXIIhgywlqtkYhmKCyUmWFS4_Ijk13_uYxhaPPRRx3ayuCcDg9PSWDFtAp8e742tanmXGutXJW8ynujTDSyTcacbcx6yEuCGTvKacMcZvpsf7XpDitI5dg8nCUrnJs7tXQTT9Bk232PNk70VfbxWwu6PBo3Eh1yWzuXbAHDGjEZkeglGe14RLohpLG4w1ehh3zH2vJ_fYNjv8zHy8osxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=aytBQGO35usmi6sOplIvm_Zz5ggXstx5j1BSMIFx2NUw9_p-a1wmBpcFlNl9MCCyHC6K5anZxxFJrT84XnRzGql72kW3i9UwWkg20vE1wyRS_iCERxL2_nWJsb1YXR1eJDPXy8rOeUW9JCb4T3M16CCZexNjCL8lcIYIVUFWfkFz1eb0azrQSiOX26Z7yNPYvWcfv4WYLmMIca2YcmA4JO7xjauIMbidH2GQZu9clAlFaapywwB-rtkRN2u3N-a5ExXGS-YDSS-UO_5JiYQ2bERxCeIvzWxvjlQn6oHupWN_DFJp58fW6H0MZvg8Ia-Bk-GFPkzUyPSzl8l2pTqamwBeBGm4lZZs9NLOOae-QYrlxSWUKiOos5atpKKIr_PRIsLTgEyxk6dLNy7-IawAxhTa6e_c2OyidBB86IyF2l3QAOjd3Lo6We83eNCp650H1QH_7oDFUEUJJLf4YDZ2mTfLMhUAvQ3-0ZSjG4lNDhMZmOhAvweBbnfkaeOXjLq1H4O0RzjwiuSzOZMf9TDHfW-PHs8ilUhoVnlLHnjPkeY7_Ym1ooSAp69S5Dm69hvb0d54C36riozvl_O12yu0-a2miy_QaPKOy2V_NgHE_-2XhxqoaQqzpU2QXqQapAmTgQQA0toJhbb2hioQpJpfJSZ6VsA3g4uz8JblcgxD5cY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=aytBQGO35usmi6sOplIvm_Zz5ggXstx5j1BSMIFx2NUw9_p-a1wmBpcFlNl9MCCyHC6K5anZxxFJrT84XnRzGql72kW3i9UwWkg20vE1wyRS_iCERxL2_nWJsb1YXR1eJDPXy8rOeUW9JCb4T3M16CCZexNjCL8lcIYIVUFWfkFz1eb0azrQSiOX26Z7yNPYvWcfv4WYLmMIca2YcmA4JO7xjauIMbidH2GQZu9clAlFaapywwB-rtkRN2u3N-a5ExXGS-YDSS-UO_5JiYQ2bERxCeIvzWxvjlQn6oHupWN_DFJp58fW6H0MZvg8Ia-Bk-GFPkzUyPSzl8l2pTqamwBeBGm4lZZs9NLOOae-QYrlxSWUKiOos5atpKKIr_PRIsLTgEyxk6dLNy7-IawAxhTa6e_c2OyidBB86IyF2l3QAOjd3Lo6We83eNCp650H1QH_7oDFUEUJJLf4YDZ2mTfLMhUAvQ3-0ZSjG4lNDhMZmOhAvweBbnfkaeOXjLq1H4O0RzjwiuSzOZMf9TDHfW-PHs8ilUhoVnlLHnjPkeY7_Ym1ooSAp69S5Dm69hvb0d54C36riozvl_O12yu0-a2miy_QaPKOy2V_NgHE_-2XhxqoaQqzpU2QXqQapAmTgQQA0toJhbb2hioQpJpfJSZ6VsA3g4uz8JblcgxD5cY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=jk6c1g-Sta5ZKiePdXyTbBn4_ebP2W_Mp5hNKR73XjSO_-Cv4NhImvjXzMgyIpI2uP8m7YlVa64a6CsFxiWHKendBha_emGf-5lJEI5Ktudp6DIY8OBAqzKKOkFBbLhXrzjvm6D93eCTXcfx75vUqBw_R-v6zUf8ekhSJzyXiuOkYhR-V_pXvoI6laW_0r01XSOBYDcEHBUbSZr40L-xugS8tuBnAo4c8GGxDY-wIdmtn355dm6CViYBTy0Pf6Kb6-X0NM0x1PmI2BXG1Xi5iqZOuIFFFkxb6UEGO3n2WTW1G_T4dajm-CTFp0Z8DxFbeamX-GfgVp45fRsWZhyXCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=jk6c1g-Sta5ZKiePdXyTbBn4_ebP2W_Mp5hNKR73XjSO_-Cv4NhImvjXzMgyIpI2uP8m7YlVa64a6CsFxiWHKendBha_emGf-5lJEI5Ktudp6DIY8OBAqzKKOkFBbLhXrzjvm6D93eCTXcfx75vUqBw_R-v6zUf8ekhSJzyXiuOkYhR-V_pXvoI6laW_0r01XSOBYDcEHBUbSZr40L-xugS8tuBnAo4c8GGxDY-wIdmtn355dm6CViYBTy0Pf6Kb6-X0NM0x1PmI2BXG1Xi5iqZOuIFFFkxb6UEGO3n2WTW1G_T4dajm-CTFp0Z8DxFbeamX-GfgVp45fRsWZhyXCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIbRaZwlQyowyXVlOTo_KO8wav3N01e31hSlfqnOQUFvB0lyvBfCf20hE4KFIYKRS92QeTTARbzMAyrXA6p9563Zp1YbRDF0TXf5QrQugxzhrRchox-ZQSq8YNGCjm9aKvQzWeo72cbYb-s_70mDfXkQXF7HMOeKpiiTRDKfQITLS-oQOPqojpQKENCQQ0F1-b6LvHXuBlozEjSHXnnek5aY5p2jSeaQOPNi_kjQBhVKD8_0VdMHeBJjSE5cqVSq7Ma5iH-HtBIsmqQmxLvl4ZgQFr9ViOmEU-5SO_a0YgSJPp8ABfltIHZjNz2km2ETtTwmThiiKsTKFZKz3wYQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_GeCPFwU8-3ktk5bppm3JPe2b6F0XhtdYsc0z7cWKIRsD0Zc4--9EMEACueoB1TSMZ-1e34GD3H1hY1lo4nNrkw0UIsd8nRF6O7CmW14YYAW9d0x-y2FJTWZev7PKSrF12RnuptNHF0N_T3KtYTQjXxJSbp7P0qDrxi9TrvafwIU1UT9AF0jGqofgFMBZO_m2UkIXtCf_F2K1pkgyJbzJQ7f7PW2untBgVWGk8yqsQS7kOBcIry_zkWj8D_M4MwwLhuryHMc0gg_n-K8nmNLJ-Y1kf-zZ2cU6w8I580w80eMIVbYTleFOu_eY9QwVwzRqiJ2UIJiRSrQ8F49gLvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOeCvD1SrhfD7UoszM5Ad0DQGmQNz0MipSxtNzH_bSQAKdC_eAJO7CG2Y3lGOYC1JU1WyXsKRZdrxRbFHHu0zP8BHg3CDD4N4sh5mT4aBqGFBxZFetA5G0Z_AvxOrb2cQ1AfJ5q3btR0K36qts-HQSNe5gxHhZdXuytGalfzn0i9AI0ot4xcU8l2EHg-ZMf8A5RkJ5ZL6mliBTjTmFnIpEMXfyrrb6aMhmLjBSV_YoK0qS9dlT57oanGDUWbCPRqC2hwCgVD7jCIAf3PkfkLimnWwMwqOkYTU3819yA0WL06DNZYNU5RCWFh0gRm1T_DL3wmt4-xOzvFnHWf1j4eHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ccni-ctR03FNCrtJrCN20kreiaUiF10g_KAdJ6P_AUOyd81Y4cLmWHLhifHq6LJSIrWT2lwsg4BWTsqoyY5vRq7av8TD_UoRpmob5xx0_3k_h267L-GvbHUIJovK3da0gmTxvFAHq-r6oeHGLHp3TserTkdbkApdJk5SJj2B_Ykb0QyvFZKB_7VXUoC8SGi4PVCVU0Ocgng1K91RUwFRVVx_-gkr3uyYECAbY_I5EDcJ7msxQ8Dyjx14VOdL8fQrMOH3LAjOEgXSvyC0hRrhMxgjnF9SM7qzZIke-VxXO7xJGMqo3xnwFWan8CLUH_9DzOGgtIuwhKKcP8NVv73_Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWMRuXvVXcTDcJetdqGjGIWQDMlebrOpzeyFUAYbo0mn-SogpH8ZU0hACclFtWnVPsbg29p-9QRV9Zf_IsI_Gm9f4h2PuZ0kvdTLikbwICOQKIsKLSxp3cA8kawfJFDCiAWlGsxHB3wIM_tlNkfAn4IBSMJpy7RFmlT4gM3SaHncLPSmcfCAxog3X377GI-H8FzRicr-xfsU3MVlhSqvfTGggCnF8x_d3Qv31CPX4PD08pXsMvqXTUD_zH6MtBXnbHGT6m0Omq8ViURkTS6YFeK3eSBwCMIX-eLI6vLqXczoE5F2NYPALckYNpEXFOtzJTamuGn4E9In_eriW9pYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPXZtsyUctmYdmTi3Am0dAE8YQB76IJAvwei7IoAxXXkZmMhiX2fINr7pY6zS7AafDn9SyUgbS5IMRUaJ6Ao6zrm86F8WgA8ObwfL_x4KFOPvmm1LxnMoNAgvulsHyol6YbT9-bsZhfVyAvVZOiGQtUw8r54Tx71Cc3oNWgeHcRcQPob_0b36teESpOIWYRuNdofxKHx87DhHjZ-6XZSn4p9TlAEk0xi2B5QrjwYSt2L_buglNV41_xhvmFBSOKokJ5DPvhRl0CQ5w2QavviZIq9Rb5CHYyc0K27sRB3kkwJFFnNWLhozoJVkCojK-CB34rwn17GRak_f3KmQM18uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJQjKwwL9YuhHUC_8-hAGn7zKRGmAP2xRGwAUakN-XqRlChEd1SnRlUaO_D3jXS-hQL5CaHD9-q8PG_-jP1JbeG-v9-lPMo_pM6lkHduzRimU21wDfRzG9aW4v5apfu-CIwoS29IfwT7CyMKo6GNVp5O7SP4I_m2Htjv6othDrdsj8gQGA4xzGDhQffCSjX5E5MEbnVOsjiUdRnPsfGpVfnPFPgRSVXvoSWIDVfkDEZqDzT0A9icGcVKVZusuBjpXXrxNjuzPEup00w_-45Ei6ll21u2gEYApjbDC3ElMk8QB3LjfZD_f7y2EIPLZPsyljcaRl78vo3UiziIhb24ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=dvHrqLjutMo2Eo7GqHne19nNFub82GVvsNrGh6j3pgzCuDE7aE8lJBUl7SCdgz5RVAxqDoykhME8i05A4iobakvi9mkjhECRY0Dmf74H-0Cgo2bxFfEeqZ3kIauOJKe3o0xkKS-dzt4vDDuVU9svDnpO_GGp6XLCn44MdvfL11WC7WDOA29wS_82SVXkrXoqRAXQomv_o_vI7pPB2ODb28vYxRc7IflXPU-Wjk_cuy7nVGG8M-XucjwqjCTZeMaJYjDtoDOhMnm4OMNi3mcUyRZJO2g1IUidKjd6udvGNM9_J-1bYNGckeYcmGxIrFfS4zABbDnA7yOA3jq3nOtx0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=dvHrqLjutMo2Eo7GqHne19nNFub82GVvsNrGh6j3pgzCuDE7aE8lJBUl7SCdgz5RVAxqDoykhME8i05A4iobakvi9mkjhECRY0Dmf74H-0Cgo2bxFfEeqZ3kIauOJKe3o0xkKS-dzt4vDDuVU9svDnpO_GGp6XLCn44MdvfL11WC7WDOA29wS_82SVXkrXoqRAXQomv_o_vI7pPB2ODb28vYxRc7IflXPU-Wjk_cuy7nVGG8M-XucjwqjCTZeMaJYjDtoDOhMnm4OMNi3mcUyRZJO2g1IUidKjd6udvGNM9_J-1bYNGckeYcmGxIrFfS4zABbDnA7yOA3jq3nOtx0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZHWZYXPtMkP2x9TG6aGn4L29-8dLaN6d2wuRPY_WkXFjlFIEkuSiIwLbU_jhwymH-A3sTF0GvXhT6zhN1ek7OMiB6O0MRJXSib5w7X1xeOikuAT0wj2jPcyc_UHHvnGryFuwn0D163Fg_sU1rnoFlidWg0Ud-HhnuZ4oDmadHk794jBa9DGi-6fLd6_JC9xUlmRF6xrsXjPnwc9QIAAp8M6RJaWb7T9aOdmTYFhsO_AqZhNP9w1o335EVRYXu8MAzAW9PUWGmsrcQzUIBEn7bpqfykWHg7z163b2cfwzr7-4qgrRHWBakh7JIdYoeKHTboA9oFB1smnDOFztL6lDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=BxevGiXnScfGXTAil68t5glHpRNu3T_PA_llYhPzjAZWXQREHkvKpNHPEWiki_Ru3vcpDHozGubiF-xEbsWFNZh0GqL-cQgiZJaOqCqRj797PZcNJRcWlEQVyMRlMiz_YTLDQRpta529rAwqn30uAZLmSuSM9gY-Gzd5NC2DJe2d5IpaPfW5G8uXn16JWY5xDlMO0gfg31u914nmmkV4xS0Aw-1hMB06988rw4SDuivS4f9-K7NaKPfUUcYpdcGXipqy1rHiQg24iG6kan42JHWkCmqL3m2Mk4Isjy94GH_lVK0geRMw0vsukWznZCH2vz_HldZKQZ038YIu3WPK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=BxevGiXnScfGXTAil68t5glHpRNu3T_PA_llYhPzjAZWXQREHkvKpNHPEWiki_Ru3vcpDHozGubiF-xEbsWFNZh0GqL-cQgiZJaOqCqRj797PZcNJRcWlEQVyMRlMiz_YTLDQRpta529rAwqn30uAZLmSuSM9gY-Gzd5NC2DJe2d5IpaPfW5G8uXn16JWY5xDlMO0gfg31u914nmmkV4xS0Aw-1hMB06988rw4SDuivS4f9-K7NaKPfUUcYpdcGXipqy1rHiQg24iG6kan42JHWkCmqL3m2Mk4Isjy94GH_lVK0geRMw0vsukWznZCH2vz_HldZKQZ038YIu3WPK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmdmCBXYW2OLK8m4EWnl0QK9mHmL2qL36ykZLHaFhG3f0IJIYOqCebIBMY7MegfsZ-zMow21bqvf3_dIGrrozIeiNtSEnkZ1hzACTq6cJyz3IobYOYRwp1ChkUkiVYv3v4BtNbLakfUCQHDbUs5RhlDJaVZurNBNngyJm-boLeL2_YBIuaO20CnRGYvJgR8O2GoLvpSk6u5GvIYP3YyfBVfESP1ISkPOUbvbkcGSaOnA1K5x2WfRGT8cAmsGQZQ7zm-7GLt8ZZhyt0rdbKDdxfkj7EfGqmHmwImdY6H6TH9zdr0uXLXUUuS9RoFL5KFBfjKsMIxiIjNNXscpUZcdNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGBU6PCI6NpQqIxa8_INfT0AsMmJgd2Fweh0zawrLB_i_AexoOxlr9drZCoi64i80TZls3Aa_F2ZYDVFSluff-5J7xt5cMBG5teS_yFP9dlXDE0R7EfmPHlCUGpAnJmVd0xQ0DIVbluXgK9yEOrB5AuUB0mXCMhs4D5GMz83bDzJIvmp6gpzI6U8uqddhW9d73boMOB30MLb7qwEuxIJTtjuQz8aRWdRYmpz8hFyv3hNDM5zfv2_BaBz4D-Kdr3SH5BdUpA6uIlZQ-WsdFvrPDJR7SoOoo4-n-oyy2N3JKu7Xs1C4U_-8Wcwf6UZP9nG5Te-NXPnzUG3YnMsED4NBwxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGBU6PCI6NpQqIxa8_INfT0AsMmJgd2Fweh0zawrLB_i_AexoOxlr9drZCoi64i80TZls3Aa_F2ZYDVFSluff-5J7xt5cMBG5teS_yFP9dlXDE0R7EfmPHlCUGpAnJmVd0xQ0DIVbluXgK9yEOrB5AuUB0mXCMhs4D5GMz83bDzJIvmp6gpzI6U8uqddhW9d73boMOB30MLb7qwEuxIJTtjuQz8aRWdRYmpz8hFyv3hNDM5zfv2_BaBz4D-Kdr3SH5BdUpA6uIlZQ-WsdFvrPDJR7SoOoo4-n-oyy2N3JKu7Xs1C4U_-8Wcwf6UZP9nG5Te-NXPnzUG3YnMsED4NBwxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=lSZFam1YvtDEcb2hr777wQqrop2DPGI0CZNdTk52qcJy5b4T99zq8wLsCNbDlN0r3qWirTso32FVvj5FVpB3IdKTj9Y4FNqOszF0iMQfZf50KHHkekI56NKWyz7co7zdv3ioHD8VY1IP0kYqDooe0yRcGVabYM-USFt8rntLC33LVGynmEivcLTPVNg0_yKJBwRt2zf1hVB28oN5rKJ8qAItbbNp18mvn3kvt3_MZgDjVx726LsUS8siOdhF7O4Nn1emM_g911iuiprGVvj4EAC3brZdENVrBZW9m1GhFNUXSO_amyTBAEOYi2yByeWFr-fct0v7BwG0p5nKUSXaag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=lSZFam1YvtDEcb2hr777wQqrop2DPGI0CZNdTk52qcJy5b4T99zq8wLsCNbDlN0r3qWirTso32FVvj5FVpB3IdKTj9Y4FNqOszF0iMQfZf50KHHkekI56NKWyz7co7zdv3ioHD8VY1IP0kYqDooe0yRcGVabYM-USFt8rntLC33LVGynmEivcLTPVNg0_yKJBwRt2zf1hVB28oN5rKJ8qAItbbNp18mvn3kvt3_MZgDjVx726LsUS8siOdhF7O4Nn1emM_g911iuiprGVvj4EAC3brZdENVrBZW9m1GhFNUXSO_amyTBAEOYi2yByeWFr-fct0v7BwG0p5nKUSXaag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BR2pER9F4o4x2rRu6RwyuVmf4aPToYD8dpTUvIu8ZBmaBu96K9Rxyy5QYkBVvXlEbgM7RDzt8JbRpL5eSzTzZ9q5VFLwTlI27NrLe1yJR0RySkLCG4djRezt_icPR7G4UlXZi1MaE5FsX0t5zx1WDUEPtE4GhG2uW4qOeb1WNBDc1YRAFOId3L8p-fHswbVFUYQUp0vG1sPuspCtFFQ2qh5GGp3tP-JJcSoiLMdrT_wtOINMbD5wFzPjpJWlgL048d-N3oWovazC9sPqUPK2d525jibiHp8uDeU7wZ_3Vyyg5hIoFSRw-6M8jlws3CwxJznAZeTuelPqtX5t0HB3Z-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BR2pER9F4o4x2rRu6RwyuVmf4aPToYD8dpTUvIu8ZBmaBu96K9Rxyy5QYkBVvXlEbgM7RDzt8JbRpL5eSzTzZ9q5VFLwTlI27NrLe1yJR0RySkLCG4djRezt_icPR7G4UlXZi1MaE5FsX0t5zx1WDUEPtE4GhG2uW4qOeb1WNBDc1YRAFOId3L8p-fHswbVFUYQUp0vG1sPuspCtFFQ2qh5GGp3tP-JJcSoiLMdrT_wtOINMbD5wFzPjpJWlgL048d-N3oWovazC9sPqUPK2d525jibiHp8uDeU7wZ_3Vyyg5hIoFSRw-6M8jlws3CwxJznAZeTuelPqtX5t0HB3Z-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUkj5VowUtvzT4gyxR0yFfpcI4EbCzMBZvq_-Y_M-qrBDigj8mbrIJQHtjk_27dwr9C3CkkH4DzTzkUa2FugnSzmk3vV8tAiALpZqGtWzdsRDtHwK_khl9BCj-mPKnH5-Lpm5F8J0OB4d1VE4g680htEuek_MOcKkQB0Zml60YhKlqhp9p1BpONmreqiRv9zqZi8iRzA0KiHNhDlqnbasibBIO3YKfpvX7rNDLUt3ObrdBhd04Iu3zB6SQqBguarb9J7We0nHBWDkl-4fxlQAWqlQKKxkhGEeiAfYZ7Ecos0l4EpeQsQshCVuwmM-6a6dUFHILL6BIjdhJn3O9OQOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax4LWixg8AH2q8as3mNkoZlMdaW4XDHCwtLx4t96P1dqvpz3Qv5lNXCEQsm1yyvM2oYZaYsqFZzG_ffBsL4e5I7ayXbNBklBdKShXKMmFHr4wwFUEihxKAKctcfO-vMiQed3mn62xuGNJOrDoGogN1LEjWbcU9MW_g8MML2ilGhMnIQ3UquVzf_DLasbGU9qqZTWJJu2UMLYaIAXdV1NeoCUIBk_qgZkPUvcqrnu3x6icExztedBqNfLofjCVZV3KYNnQyEFxduFYGp8bg0XoJKwWeop9Y3KX7emj929JreHpheLIzPRT93EQDMZSmqLNPCyvt4q6MavRz-2iY19eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7hosXpG-V6gz5bgV2SDvohP09DRXFPw3XW0mPresCsLtxJSg6xr9PrX0bqBK0rMYMd4gve-jSXBQc4hB157HnSe__uA_MP55GS4m-Yi-ZYICs6_BPtuDPflx6IX_ZNYNsCdSxnU5gYVYzSdMFrGhttZZBZtFnb-5RLVoCvbL5W42gMeA30gFBtPsqgh_7olIF8MhrVu01orB97miOAqAPS_wiuj7h1nJSK71VgFbglFT1ryKObRfwjeWfBVZ-A6nuj6uaXC39GuV5OclIiSVweidrrUFRNyhd8UIt2KVRnK68i_VKYMRBdbjoRam3nvQRogNIU5oyoOfn7V3IFWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIKT0NG8yUGC7oZeyAEsaPaX78RTGUqqjDMbfs6wCMsC0vjyyDMD4tBMbiiIHdA_nTtajV5YoQ7VFWtB_tuZQqmSb8ZZXae-XB2S_6GNkpB_c2HCQyTcIhZ6p-oYCXmBahI5rOCRNi7_Ue7soNsOg_kt6pKNrcudxACC9aVkbJG00LOjOmlGBE87_6wgQ3jhsA-QbKpjbL01a_xFfM-s-dV9KRrzxWLnH_cyXpVlQkiyIVp--LE_6oNlU480whIVPyaOF49LaMc38oC1zeDpSIHPMKmKO8sashLjnigvB3lZWog5nmP3qwW82zqdhQU9EZYX2wJulJaGSb7Kr_7aNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMIwxoybBb5mdjZ7iiRvP_DM6GWPJMAxRosqjmslYWz2_kA1nNINsSexD_3AaJKGuQTsJws1HeWadljIX6v19RKqa9JtUvwhCOyVSCIZSgXPYYgdrmdi8sH69srSvvr-C6IedGDzVHBo2xp1MpYBUX9XoncczWJlGnVHa4sgAf2sieCLf5TK9NldMiNqiR4rjc9Ve09iTuawGc1pW0pMnOC4nKt03nXKr9a2UQMRYl2SuT2V0j3xqjBaLF5icni6bTnVidA4bs7LnkAJw7VQ-40-YXypzRJVpfvy1cowCDTWfhZKoTRYpysU8JLMkg_pSCW-fhH4nbpADGxBpcuDCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7u5XIhftIsjDnUHQKERRTMZM91an41FxVtAKYtCBM5TKtgspr3Ur9UI618hcK9fyjPDa9MeQp5X3rOFwZFnXSlX2m5Qyvkt5Fisxq7iWRxE0JxI-9pFSiESyZ8UhDAD11VWheeOabG6oRvEQF8xI715NhCEw8vEgx7iKjmAvy_Ib-PRJiqZ76Iiwxt6lCdDwoQYeIU6FapxUImFr-6Y8kt_SVCebn-mANGBFkAv9NPvB-gKOnAttG6Du6GEoBo-yBjSLV7gLIPZF8jpKpDdoZ70rxrR4YfmoqIrIP9dZ7j1Ts_kiAq-uOoXphsApw0di7vu4NJCbGIx5Qj6jAA_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAyeBpIZXFEuhmiuxpbzvvb5toGBvynyVvcDswJKNMo8nVZg1bkwEV-FAEEQGD1Yc7Siwzw-4ep70_B5fqBDqklZcJScbXwFSWcsfX3pHEeRoggmryGj6ulxnFcYucvGoEnTISeIDoQoIAw8Vj2J0waALAbAqo9whHAUYDqiqHw0D-mGZlFBm_CvgozWhrDoMjPm6H9-_nqaZuFFbdnU_4q34qXozDRRCT7Cle2xnMaX2GgUmZFz7W_60ltbwlXsHIC0if2K-hfWILkmpkBwCZYW4aOKWP0L9gmyEZKwYmj3P8N0LH64Cv7cdtGTD8QIU8li4AQbO8qeHnxIZSl_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVluzkGnGyRwz6lnz5TZWNvblmSGD2qrf1m5m2wJICnLxo3L8W8Zl0gmQPaSc8PLGx-mYieq75z1fExKGH2LdOgBy-qH_lve9tf3_CmBlf5VAT3H5OYst-DYne4711nAlAhyZ1uFZlwy5jYlyu8YMHoYhsZRhpXMAal_aRDbi5BpXZOptv8CgC2jcTt3ZxHXnxXJCgK20fkIAfvPsFF6ByL288EwHXZOjVIzs6YSvpf-fQD1NeZKB31SxNXNg-na_0Psb4xMPfEKqOGDoUOwsXzO9U31Bbbv5jf5l5hy6bUxbKtNjnrADvp8NrHjkQ4HJKvEVjablkTgMciAv1qJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIIjN92h5DPywYZnpHJWbs9DOObGJvV7kF0dkpMszKokUckRQ_XcQj3kRjtW3Nqm0ZPUlmigItR_yA1bxw_dDIahx6snWAH8g5sqOxf5U9k1UzlnTvC816janaxsh-HcwgXFgBbCfC1mhOW5q-NN8TQWTStG6MpiuYdvPaWJX9wiI0Wyhz08zcNKRk1bnaNzgqsxPG7syN6gEMP5-r2_b3zCQwdnc8tD8uNkur9kstJhekmAUYTmBwLb39fYEpcMaV1ecAz-U-wp6oRE6YCBHRFwgxfbDZy0eS14eeILZ_eXAtPfB6nAmuxn-cNIeUjGeQ-nDLLox3WEARWjW2vuBw.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
