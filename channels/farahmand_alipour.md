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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 19:50:12</div>
<hr>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5E1UvQisOUYNvRIBdOWx-bY3uG05FRSG-1gr3f2qY3oNGAiiIv2GUsfaCeCUVPwrhKFukgNo_CqWHm42-opva1tFSKkfTeRpdqHECndLHEEMJt-oHbJJpBy4HryLEee007nSj-xlxGShSLG0qTGx2VmvD2AHuB1RmL-015pVBw66W_pGkLz-eEBBhqWrEMoGU9SOGrKhWRzl_AFtOvQjI5DuRRQOMMgKAzSSSPO4PWulAJR6DuKHFfwtvJZz-sioJ17H7-CeiTyznVfOEOn-eDON1cY1BbsZ2XtNzV5iu9yFSunEu6Itqj_4Z5UUIOnBzCruoQFdUnNuFCxtN-s1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov-5teW3tHTvsvSbgMdLICYXYlU_sDGIu9OuiTSl0594zrfs9gRoJQR8S28V2CiP_XCjD7Zzp5uItinMqAUIbUIRvVFn3zxxaqYh9Km-0nk74uSUdeQvuMYluMHfHS7WfmU5Mq1R_o1vTjHKfD6MlZEq2Yf9KVRt4d2gzoWcCctXxlvrZ83-13fvHD4NvwcgSfJHIpLOCqzOAdqDTCE-6frq1o_rpZ_dr6FZtGyKaUvR4uN5aL7iKlIR-aOJwWaAcP_ZJcq4l0tyEkcUu7cd1nNA3Bm7_vFPEyFbPsYQr_SdVeOSm92Zw0-QEekuDDdOwCr60iw-tbsukbzrBFNmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHVVCza4-k7lMKxM3gRJStW0mSmbHx1HOC_kqRItxfPQPZo3RqgLfbxvjky93wErqiutSbOoRDVDgJO6-5Gt5GeEQYp3ZpC8LbmHHVvogV5fTJ8tjv9WUtzfZpz5NJscTMxYul7zKui-uhcGtGwcbJz9kr1kP6yA61rGmmeIOf2BDf3B7TQdUT7ccFphzbXnhtP5luogZEm_0Gi7-eRD7KumLBDmDBfFnXn0yVHUWnWFFsbkQWbKqce98C8p4SF3LVslyiNzTK7TUUb1kdRXw9U_E3m1dmBOkEfxlEWe_yZkhLuLgJrZdcC01kX5yYjphMbJYFfm6UDxnofukWHSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtqbusLboLN9-Lrqe9rkYIJx_IvHR84ZEHryWdkZeDoRtrOqikXN7EiCJPyxhY0K5n1MEgMzgzs5MR0SrgnYs_3F8GgLoDYdKQ1LYTW7Xido4AUaYEQj0QO1zbE_UI2rRR3Xjp2NfzvzJlA17Y8-RYrjCC40HPKznslTM8wL2b2keXdTihMVSAzhrWsKM2zE1ziTnSVNA2CcNqGAk4EUva6MDz1HAScSWM2X0YSeo7K-8tO5E-3qzHKOu7syOVXFFTPwzsaVcApsYq8y_51MikBazPUNTFYfJVOy4371oGxyqsfjv9LPjVEwVrFbGqSg_gT-daVP7dZWwSQ_f8DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3cy1W2TbhAEaNqko-LkofOvGARhOPamsqF0vCHGyMTA7VOKKvkblmGFd3Z1Cmu624_ja_tAa8n_bbjHmnVTuhNxKTyUxVAacVcYG-q-bRFg662UE5Tria8Te2IEuiazcF5nA2jXoZYHbcMMvjn7bJRAgoWnuSmKAPfMRR3VWB-izE8iOD59w2umFAgheoI3F9cBvPYJO12pwPuaKptJ7YQSh8wu3vjjT20WB8oaFhMleR-Rvz9k8qJK0iV9UMgIccuu8fRJNoDpaVxYVJ8kU5i-VJKdGxh_NlssZVWq_v_rSGXU4LXxVobrRtTg0YWElxLIttczbSrrKRw_7LA-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlt5ohzv1OdqdVm8v4Vv_IX-0JFxqy-G8oYJBsuVCZ0WE2qfU_wROvY65ynPOmrX64NDu1vsIakWGR8vtT5mKHiFbPmRag3vXe7UCO-ac6X3kFZtMEYOSBj3paRx9ihuXJUwNkrzDcQC7bhdWgz1hGE4R1GRCfhLDJMbgLqIUpf7f2sXPUilv_xg2uxob9rxE3JcTndqTsg4-0U2ygixisi3tvIICsmZs1VA5ZV7iD-CYYvf8wrUuw7GQd9_Uy-5W5UAehUBa8MWmeYo45X6O2MYhXRRi1pa2cADIgXL4oopEXqLay4Dun6X1ZHV4RSNCEXLfJZxw1XFgqS1ctKtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa0hWGzhzY9itzmhkoK29oKRx2OQIwsQHrLXuf86OWi6kztKyeqDaXz032MzwDwDwrmBufAyqJw3Kp7zAFDM7XJAeemjd57hloVruYXzBTfzC-4Rcm9kkmefsQhxynFJJiUjJmY6aFWTt3Z6In_EGM4tnk5kWuUv9PfMk34ZUGMfIPCIxRQCLbzvJYpaEimF2i50wZDVzAhvoo8a1kPLk4WGiLEWMMeMssqLLQ9drHduov9jWFZlctgRD_xsUPmew0DpJ361ieOc2kv0httSBkOgUoo7eiuSb-RE_vQESZQ_BaYb6ujBpk3DsI44uTFnRpcrKoXlmVZQLEQjMtUaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOrtCyIAQvdmrktSEWZxv6cri300fmvHZkAIRvbU-HLNXdGt6Po7PDGwVyYd7QTIObxZYUSZeds-TYQXOiBDWFlQ8qjkRtb8AhZq5J2FxdcpTyeFfcwgmUUCj_CfHMd3gW40JNrnJ5SkF8jd3QMDfX3zy-P-0Ongf_t6nzjCIeOjUcQlfgP6V7HnlOvrJjIXKwCorCsJvn7kiTtocmo3Zk9dJfaRHCBbW0YPwbHCpQCJk_xDxoheGJUlqGQFKKjoliiTtL_NbDQcZZkcB7E_tzxypircE7PSQwkpLSy4ApJIxrtp6-PW7OggspvWssaLkrJwE_xjOMGiRkjqN_P9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E01XqjRWTGs0y99EGIylrGq3Lq-VWNg13SUY9yl1x6lYh4n1TaNdIN_sbZT44XEYwC83hPA6_cMzr76071gl0XuMyzmQlD0LPGC0bI9xRipJ0GZk552VBMHGmz27ZCdxjNfzVSL9lRi3COyYkYnSU5U-l2QPw23-GQDdgKxeWJDiU1_TvA9TExZKDIFDuAWGdyEpmJU7r3ERAXfEhT_1c4vbRUoCuyOgD1RC_4ibETfkyWMKdFgT39G4e2Dof17ngQk1G1JgZaW8_8Yrx1_Xbgx3T6cSsMV4fDPIzBnzv-mnb-gsqNVcMPVkyBLexVEK6o8aYDxwFv6D_OyJ4YmLRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxcQbuRG0Ni-0N4DT70NJQFxa20Ekeg2Jug8kX6YSlT_-BGMIK1MkeD5Nsmk55K4vSIaQndulD6fxRURO0t2B7klF-ZxLB_KO7YrPoYose1hm1iuQg6h3Vtw_BHtBjQgzmLrLUWz-_vf4sndmeLWQnZPnKLDjA9rSoMCJH1EhnaQvF0IIzYueMRLAl6V742kHcaT2IQH1dYH0OFLMAcdB06bGXjUCNhuvG6-73AF-ddY81Eug-h2p80VHoyFY1u1wwUih8edrGQwUfzpTRN2FSX5a2uFCUdccpSGDk6N7xUYKXi-6dVVxz2KgNSCMqs7OCSMhQhgbPUWT4zB5FZA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=e5YoOE05gJEAfOaRiJueQPsifQQXsQdJVr3zZ75TkMvRbR9Jpcvyv3pcgAIYfIloEg0_UFHYJeL10RBqWIH7YS84Hj5u18Pvgc3WSyODqoCp0PGhSHNnwCySyyqfsMeYt33OjDuVnjsAwwFqdgIyXdz3PescBfZQ8_1h2Kk_w3Zq7oqjizQK8LEVdZhVxKatsXR5FPUeXVh1_2Jy7aipTqeBZHHKWJIyS5VJvySuu6lyZQWRzq2hRH0PL3IN5PgQ1zEbtWzxQdeSHXp-Fe3QKV6i4Mvj2fmrctMqKBF35UNT7UBV0C--npMnL8mfq56yzOaHq38Pz5AtDvu_pFQoDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=e5YoOE05gJEAfOaRiJueQPsifQQXsQdJVr3zZ75TkMvRbR9Jpcvyv3pcgAIYfIloEg0_UFHYJeL10RBqWIH7YS84Hj5u18Pvgc3WSyODqoCp0PGhSHNnwCySyyqfsMeYt33OjDuVnjsAwwFqdgIyXdz3PescBfZQ8_1h2Kk_w3Zq7oqjizQK8LEVdZhVxKatsXR5FPUeXVh1_2Jy7aipTqeBZHHKWJIyS5VJvySuu6lyZQWRzq2hRH0PL3IN5PgQ1zEbtWzxQdeSHXp-Fe3QKV6i4Mvj2fmrctMqKBF35UNT7UBV0C--npMnL8mfq56yzOaHq38Pz5AtDvu_pFQoDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=UjNH8rk1Y6A7Hy4Eyny_jn73sMaM1SRwu3B9LzuLd5WSm91KF0VdlEON34bd4QXB7R5FtZ8OBpptSP-PuWGk-FOPgNLxlL7QLT7D1sn7Ti6c9A5xGfTodDN8MVK3BLoU8aXUMLEb2q8DGGTs_l5GV_Zz_fPSUeGaqAHusQRlzhVxzcFyuFdgam-GpQDUxpOujddzOocxPtP_RwgNjSA-qa_wc0ctkpNROAlikOBLKdntKtSxU_Y01P-j0iyX2KjGb1LWKo9EaYooIr8eZt7UMb9Wb0aJlhnY2Ib7Iu4yYZZ-LHFnm_hHvKHLsFTvMU8iRfxlqMJ7yHovcttjD53Ixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=UjNH8rk1Y6A7Hy4Eyny_jn73sMaM1SRwu3B9LzuLd5WSm91KF0VdlEON34bd4QXB7R5FtZ8OBpptSP-PuWGk-FOPgNLxlL7QLT7D1sn7Ti6c9A5xGfTodDN8MVK3BLoU8aXUMLEb2q8DGGTs_l5GV_Zz_fPSUeGaqAHusQRlzhVxzcFyuFdgam-GpQDUxpOujddzOocxPtP_RwgNjSA-qa_wc0ctkpNROAlikOBLKdntKtSxU_Y01P-j0iyX2KjGb1LWKo9EaYooIr8eZt7UMb9Wb0aJlhnY2Ib7Iu4yYZZ-LHFnm_hHvKHLsFTvMU8iRfxlqMJ7yHovcttjD53Ixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=AYd9fikqzzYVIxYesJjBLrXd-BR4PwwOmXIVtHKykfAA3l6EwvmGiwTjKv6yFvEPexzHZmVVf7Yf4CzWFaLu4DrGtsurprhgjUFCwV6tAci5KgVp1C9hcpJ9Ul-MaNmZ3HKkdQ_qI9mIJt6S9k6U8MYHnXaTjrJtaafwtnSemHCX0mKxl5jcDzMo0kk5DYqT-A6QaCzaAFjniW4Aj-UrETBDWhlotmUwKfEDb1P3g-Pp8sO9Qa9nro37Gl8LyaH12Ky6hCdiaA0F3qw3VJ2-AcohecRQltFOQCyfPZqoY-rSULUELcidAr0NKs2yDtgIThBbGBBFCQc_R8-gntApTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=AYd9fikqzzYVIxYesJjBLrXd-BR4PwwOmXIVtHKykfAA3l6EwvmGiwTjKv6yFvEPexzHZmVVf7Yf4CzWFaLu4DrGtsurprhgjUFCwV6tAci5KgVp1C9hcpJ9Ul-MaNmZ3HKkdQ_qI9mIJt6S9k6U8MYHnXaTjrJtaafwtnSemHCX0mKxl5jcDzMo0kk5DYqT-A6QaCzaAFjniW4Aj-UrETBDWhlotmUwKfEDb1P3g-Pp8sO9Qa9nro37Gl8LyaH12Ky6hCdiaA0F3qw3VJ2-AcohecRQltFOQCyfPZqoY-rSULUELcidAr0NKs2yDtgIThBbGBBFCQc_R8-gntApTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puyzJVXs9mri7q7tthPGFdMQv1fOCACHtkuN1aTK8w2xax7t62hfWSjjuiJsabcbhIfj5fY7Q5Ir0BWZZwSVEnCpLvyZd9qTy9RXEQObVkDaYYP54sVdGmLUH0bgN8XlaF6eGpXiKDb3vXjHclcM16iAjGrA-A-yTWWpg07XbZXFRkCU0J4HrOGOq4QU9Guv410wi-Fbh7JyVLE8NIdswIP8g-8rDSl0hYIjLkKv1rtSi26rB8o-c0nfNVKXQGAXkVCHYOINoHisp3Fh2F0A9dhpKyd8772UfczbMdr50fh28h32y067u0q2Ej5Ns6-p_jG1YCX8JUdCfZE3fxQuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=ZW5-8zdZEPEMpQuJYvoifcHtsESkPugaSGZJQ0Ochm-5CmND1oLWKuoGrt2bqiYPmC9a5beaZF3x0HfFDKoK1U4w1Yt3iFRMNPWDzUxZVIdP1I5yRKuD2BiV1vKyuLr1vLbJsdHQzECddD64WtjV7Spg_bt5zYpzE9LR92I7PBafDZfqaAjILAS0_3SGLkYNzTnq-Zc_HdQPwKQgEdpEL5C_8NUvYP__clc2MOokt4b8jkQWhtWdjJE44jrGlZfLRHy6JDIsrf_6XT9tLs-oNpTGvmKJ8pdUzQZTrHAcb-3dUCKoBmzgqW_Q86XGaLzfpkpef6PmWL0x0HnEB0C0uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=ZW5-8zdZEPEMpQuJYvoifcHtsESkPugaSGZJQ0Ochm-5CmND1oLWKuoGrt2bqiYPmC9a5beaZF3x0HfFDKoK1U4w1Yt3iFRMNPWDzUxZVIdP1I5yRKuD2BiV1vKyuLr1vLbJsdHQzECddD64WtjV7Spg_bt5zYpzE9LR92I7PBafDZfqaAjILAS0_3SGLkYNzTnq-Zc_HdQPwKQgEdpEL5C_8NUvYP__clc2MOokt4b8jkQWhtWdjJE44jrGlZfLRHy6JDIsrf_6XT9tLs-oNpTGvmKJ8pdUzQZTrHAcb-3dUCKoBmzgqW_Q86XGaLzfpkpef6PmWL0x0HnEB0C0uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Pwxpo3dkWk-I5WtmOMJwCTct6iMY3uRXhPpWl8Yq74jkCxrxGEUAWm5OMw6CW6Ym3Hsq6L3ygbrIg0L_Bz5f1hXuoz9xnEqyZgA867C8h0rZO4dkaM4t4AzPHS-0q5EZ5OjQncBXb1oU4ZrMIpzQEEzxxE73-fyCNVoJjFo4um2JlsEYxWTafhNDggagpZkKB4KdWsWz-_8XRPNEMaB9FzJP4Wm3R7hrX8iRIFCfFObKXRg5FWfby_mci8j0aO2XwZXkhEK6ZsHHz3Kb2FcxgGXdGIyCUWyo8hj3nXR_YEfPCZR7J0N0FV5aFsKym8wA5kyHt-zBxO7v-ZUP8kcFpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Pwxpo3dkWk-I5WtmOMJwCTct6iMY3uRXhPpWl8Yq74jkCxrxGEUAWm5OMw6CW6Ym3Hsq6L3ygbrIg0L_Bz5f1hXuoz9xnEqyZgA867C8h0rZO4dkaM4t4AzPHS-0q5EZ5OjQncBXb1oU4ZrMIpzQEEzxxE73-fyCNVoJjFo4um2JlsEYxWTafhNDggagpZkKB4KdWsWz-_8XRPNEMaB9FzJP4Wm3R7hrX8iRIFCfFObKXRg5FWfby_mci8j0aO2XwZXkhEK6ZsHHz3Kb2FcxgGXdGIyCUWyo8hj3nXR_YEfPCZR7J0N0FV5aFsKym8wA5kyHt-zBxO7v-ZUP8kcFpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=llcBWsiGLaWsyvT4XVcOCP_pKF816vUzNPEgWHKrWO51u7DkpMtziy-0X81jaB__77_aSc2JbdwoNDTuo-81qqkKCa2G7k2Qpc9dISqYAxQB4oh9mTIS_OtNU5ETahBdImO2PlU6xUnU4CznAbJC7wsungi9hrqNSAo_7RubJyXACJJ4alxMoKoglgUbtx4tYNpROWN_6VOTSUm9ZehRvAXtcVj0KAYOYX5FMx-869Gac_tHp9qGkLcpTV4HDSABsDiVkFKUtA82Cy2jfgVTJwhh5Yas7X_64wBf6d8Goy9xab-vqnkCMbMpLtR89Jwh81pOudl9stZlwpYSfCrcGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=llcBWsiGLaWsyvT4XVcOCP_pKF816vUzNPEgWHKrWO51u7DkpMtziy-0X81jaB__77_aSc2JbdwoNDTuo-81qqkKCa2G7k2Qpc9dISqYAxQB4oh9mTIS_OtNU5ETahBdImO2PlU6xUnU4CznAbJC7wsungi9hrqNSAo_7RubJyXACJJ4alxMoKoglgUbtx4tYNpROWN_6VOTSUm9ZehRvAXtcVj0KAYOYX5FMx-869Gac_tHp9qGkLcpTV4HDSABsDiVkFKUtA82Cy2jfgVTJwhh5Yas7X_64wBf6d8Goy9xab-vqnkCMbMpLtR89Jwh81pOudl9stZlwpYSfCrcGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=KK9Ml1WRj8eJ6lAq-WICbj8F4CMUNsOSPmraHNsKk8FjqrWehxfU-hAddfdJQoh1IS_P3D5jOdI8kkj9tQcQm_2g3ktC9SfMlKixWlJrpsMUkSEuMXSjcltLRgyeOZUeebxTugN0HujzHh_W79wjMgX6dP7_HLgSj7KjgEkx5Mj0qm9AkF7tevdjb0MEiD32jyNDJHYhL1qUJVZXyGs_04zy6R7rphYsySe6dBCNKB04jgJZ_5QHv7aUQaSpGOr1U0lmqup1IE2A_OLBGxQpTue-8kaSdxkYuhAXiWTSwbODxrMbax8iyQ2BYzA5n2ynUQcukfWCsrlVhbVvSuEQkX6-JcCAGaWyDIFE_hiwNGgfk8YeKHj4lPhPqW9tOetHwwoy1EMzwPoC8i75k86VFMMTZ8bC7AkiVVJOelwMxvdTEha5kDy8TIlkjoGNhx6BqFM1Jt3BOUYFoJxYP35HPRt16rYhD7iBqNQzPYfjnQK1Dyyi1jqzcMpOk8qfCM8laEj1GUdPml1ctUdKmqKvjJQdImy-_DbBWuGN2lEHnW-m7xCKBs7bAIAxWPMGZKMSsLDR0faocwJq28rbejPOeNdpLVLlmKAtvkMFlhB7-1Mepn7_qaOy10peJ8qD1lJbs1jD7p-8qI02SEftjI7EW0UBf9e-h5iHWOH_PKK7Zx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=KK9Ml1WRj8eJ6lAq-WICbj8F4CMUNsOSPmraHNsKk8FjqrWehxfU-hAddfdJQoh1IS_P3D5jOdI8kkj9tQcQm_2g3ktC9SfMlKixWlJrpsMUkSEuMXSjcltLRgyeOZUeebxTugN0HujzHh_W79wjMgX6dP7_HLgSj7KjgEkx5Mj0qm9AkF7tevdjb0MEiD32jyNDJHYhL1qUJVZXyGs_04zy6R7rphYsySe6dBCNKB04jgJZ_5QHv7aUQaSpGOr1U0lmqup1IE2A_OLBGxQpTue-8kaSdxkYuhAXiWTSwbODxrMbax8iyQ2BYzA5n2ynUQcukfWCsrlVhbVvSuEQkX6-JcCAGaWyDIFE_hiwNGgfk8YeKHj4lPhPqW9tOetHwwoy1EMzwPoC8i75k86VFMMTZ8bC7AkiVVJOelwMxvdTEha5kDy8TIlkjoGNhx6BqFM1Jt3BOUYFoJxYP35HPRt16rYhD7iBqNQzPYfjnQK1Dyyi1jqzcMpOk8qfCM8laEj1GUdPml1ctUdKmqKvjJQdImy-_DbBWuGN2lEHnW-m7xCKBs7bAIAxWPMGZKMSsLDR0faocwJq28rbejPOeNdpLVLlmKAtvkMFlhB7-1Mepn7_qaOy10peJ8qD1lJbs1jD7p-8qI02SEftjI7EW0UBf9e-h5iHWOH_PKK7Zx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=sdDGew2C9ZHKSqP4BIjNSHkDwqCdCYYxxaexJxQSa3NliNIVupnu6oCje4JoZW3YwYzE3ufxCZMoc_shueXwg4xSndFZmY12qY0T82PcYPoj_IL7Gme9iTkX6A9GuV_9WpVuNHNC2Nkh3dNIqLw99IH9rTFz-Zb0bCERews6sKD9wYZ7b5CPMm2WtrwtkikY71sfDyNhJuTbZTiQ3TYfpv_DWHD3yoUJafLGmLfGEzi7GBl3c477fFvHSuwPOT-5cV6KufffJlp5neywqShPJTqq58sIw3hiJH64ljBiVAnWPj7ajlNwoEDJkuAV_MSit6vdIs7ZK5lXXAtKMyPE-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=sdDGew2C9ZHKSqP4BIjNSHkDwqCdCYYxxaexJxQSa3NliNIVupnu6oCje4JoZW3YwYzE3ufxCZMoc_shueXwg4xSndFZmY12qY0T82PcYPoj_IL7Gme9iTkX6A9GuV_9WpVuNHNC2Nkh3dNIqLw99IH9rTFz-Zb0bCERews6sKD9wYZ7b5CPMm2WtrwtkikY71sfDyNhJuTbZTiQ3TYfpv_DWHD3yoUJafLGmLfGEzi7GBl3c477fFvHSuwPOT-5cV6KufffJlp5neywqShPJTqq58sIw3hiJH64ljBiVAnWPj7ajlNwoEDJkuAV_MSit6vdIs7ZK5lXXAtKMyPE-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Wp1eOPW5xAL6Ve-uOpI8n1roToR5BzPzKAaaqANChtuGyEDASyHJtALES4nqcQJAnidCOVzn5JPm3vSyikyO5yFsD0IFOmX-ONmThPbJEKTCR6N4KLQhjKncrpt_37OphaxL3uVD75kEsYRLYB4bflnnZRKNbv3UFDaqM30i8AAfGywXmIYySO5m0zVI0o1e8pIKyPC0qWLEPvQhQHqiWqEp_flfBXBGc9o9rFn75Zi5CSeGBe-8jdvAnj6styCplVJ97pvOvLzLtdQdUJ9_fKa1sQpjKhX-GxNaXNHsIKsTC2Vzb0dNCADLmn2sQx9AiiZD4CgiFUgkeZdFUJqEbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=Wp1eOPW5xAL6Ve-uOpI8n1roToR5BzPzKAaaqANChtuGyEDASyHJtALES4nqcQJAnidCOVzn5JPm3vSyikyO5yFsD0IFOmX-ONmThPbJEKTCR6N4KLQhjKncrpt_37OphaxL3uVD75kEsYRLYB4bflnnZRKNbv3UFDaqM30i8AAfGywXmIYySO5m0zVI0o1e8pIKyPC0qWLEPvQhQHqiWqEp_flfBXBGc9o9rFn75Zi5CSeGBe-8jdvAnj6styCplVJ97pvOvLzLtdQdUJ9_fKa1sQpjKhX-GxNaXNHsIKsTC2Vzb0dNCADLmn2sQx9AiiZD4CgiFUgkeZdFUJqEbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8bRoN9YE3_694VXvN8ZhbaFEVgi9OTx2MTDCv-UjMCQlTeCry-xManOJzMLqSmSHZaOR626slZADRdIDTFk4BVvMmAdRKrsDaGTDA-NraMrj42rvpYVE1DYow4GL1M7sx3vyURcNURLFiFCU4Fh6csGj7xlC5QdTlw9BEqnVQ9aMv0IuhPgJiJPH4azy0SKb2ArSbI0AhGn20ovg4OS6FymeG-C92l2__tj0w-tGviis3MQ_NUT_-LJurizSj-HKrllOXUMWHWl-L0I2aII6ZCxAO5Pc8LiIECV_qDcAvpYo0sFB0WMlPb233R4I-nG4v_5ohfODnDsqz46a112TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpFe71b3g_pDFY1kBzfLkvbCpWJsCUO4j_Mbu7L23HaomQ5ViOArKQFzDBKVa6NnS8wZl9jecQBemSQ18iW0jIO_5gTIAc_9Qb8h_8gNR4UVvjhNzo4kmC7_7lVhFvGz_MUIGODT1OkTkc4K01IBildi9eIEW9JmtJJVavTGAOOxfwcCLxQNF20sYrRAz6ct7JSkAC6bi9DSzkCq08gfNMPoddHDfbqXfD-Qv5PsUYH0-pZkKS7ZKW3I7mgHNB3S6AZ1C2PjzpDEuSATuvbgxbuB43-CpPFBCVinAHNUUcF8uNnqcFcusA4cSVJcSQPeFxrhW1-n0wCtcCCVZBva5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=kMUBZokxxUoNg5IUX74MwicSBbu7DvEcJnmmV1j6mhXdIO48165MWuVgPGOlF-RTdo_NptXUBVsnMV15I2nyzoEoYX0ORm2W6HDxpNPeDSI8IH240jsstYAMp4kz-Mx-3Qez_jiRLtXCXfFCzcdpHKKlnJtLVrSa8odW8qVaPg6O0SoluLevF9d7zy3hHw8Tid1lMqn8x6byl-eQMnGFonXgtiqxAfO1smlJ8rYhQnlhLDwFs0eopc1qEbloKuV6N32qeM57g5SLpPpQwjj7ZFAfEjcNhRSkXxP56_3YTameVWLtmAKERqfLmY3S_h-n2vVVfVsucGZfVE0wTi8zb14VX03lS3r__06dhOIuUrWDd_NIUuWmjFyYPQqeGyG9Xt9t_lJOW2N5_LtFH8y61vZO6GnCKjNeQBe5plPMyPMoLI_x3HDbFtTH7bTTz9cGnUVBPv2mtctFGSBJs96zg5f2FEoKSrDorOcu0y_TEgAblabRCBjK_WvoxCWZuusfZ5uIMFwH_lJvn5rnJwCOBnoLbjkB17cbnmnbBWg4dRDgP-c8IZ0TuBCV9P_cFlodYafXkSDkV0M2noj7Pc7UlnPo_5sSNIsxnO1DY7PlC3yP6sQCJxOUgyeSNdsmMtYLd7T_ugareTdPt91VypMIjWP1vlIaUFmfO40s3_4Ml_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=kMUBZokxxUoNg5IUX74MwicSBbu7DvEcJnmmV1j6mhXdIO48165MWuVgPGOlF-RTdo_NptXUBVsnMV15I2nyzoEoYX0ORm2W6HDxpNPeDSI8IH240jsstYAMp4kz-Mx-3Qez_jiRLtXCXfFCzcdpHKKlnJtLVrSa8odW8qVaPg6O0SoluLevF9d7zy3hHw8Tid1lMqn8x6byl-eQMnGFonXgtiqxAfO1smlJ8rYhQnlhLDwFs0eopc1qEbloKuV6N32qeM57g5SLpPpQwjj7ZFAfEjcNhRSkXxP56_3YTameVWLtmAKERqfLmY3S_h-n2vVVfVsucGZfVE0wTi8zb14VX03lS3r__06dhOIuUrWDd_NIUuWmjFyYPQqeGyG9Xt9t_lJOW2N5_LtFH8y61vZO6GnCKjNeQBe5plPMyPMoLI_x3HDbFtTH7bTTz9cGnUVBPv2mtctFGSBJs96zg5f2FEoKSrDorOcu0y_TEgAblabRCBjK_WvoxCWZuusfZ5uIMFwH_lJvn5rnJwCOBnoLbjkB17cbnmnbBWg4dRDgP-c8IZ0TuBCV9P_cFlodYafXkSDkV0M2noj7Pc7UlnPo_5sSNIsxnO1DY7PlC3yP6sQCJxOUgyeSNdsmMtYLd7T_ugareTdPt91VypMIjWP1vlIaUFmfO40s3_4Ml_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKjLJkqlyv8GUiX4aHcxtPYHAePNmmaYwUxRE9N4BvqumFo45-Acx9txmyHJ05HmaHbN9FdMA4DLSvO8XK9fi0jtyJjTYU-8MuVSH0Yx_l7XbhA_JNWah4CsfDTZtj1_q297lArdl2B0MC6HcdiT7QbfrJsEQpFPWPw3wySXuTkMrkh5scgpX7cM15kiFCHCJg6SER0XtG1cyG0gVnrp3Ldb31JKji3dvYkvoZMXZNafPH28iALDhh-gm0uEbUtlYVlwsX1GXAKR3nDEm-xxKk0vTW1yHi_MBpkHK3d_4wvTLIWtcU0dryyyLXNox3901Rzf5Wne_rOycw18XXFzfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffkc56DorK8slpbTWNUum1b0AjAOHt6tj8l8rrTCemQKEHHQy6YlxKRPHqiLyTVjth20m4r541WFS0xdYg0naR17lva9kkZSYVhJpdxQtTvytl8Zg02Na5JuTr6u1ebBjkyp1i5jMPZJSCpe_GlS6BaHj_EyQ-JL-3z7CJwCyA0QmrgpoJAPYcs5TkIoPc-Nf7RWxDQpc7opdinZ49If_f5e2LGJMKa8x1kIUsw_sS4h98f57barhSh5XJE5YGRh5SLq2vMR63FCzg98nTPrjtK2VQdto4UEr6D4_dhGcJ4lDWJxmQ6761Mx8u2ROca8zyLPlyz9D6mfth1EdsrzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puVqS9gOfIpWl-uv2ddqK1oVzeiS6jT2qgktKrlJ0iHNlpAw_yaeYcTtkiX1roXVLmNzoYOOD3nBBN4BTH4vR6hmXeZj810D2qM0YsWiV84ysld_HBeWeHXky8deLkf9OtgRgYbLbR6-kgUrgXxpol3yQg73YF6jStRKf7DjWy7HFyWszRwkhlWmnZyBMaXenvUrrgaLv5Cev45-VytObkM2vMGA4ytv8nPEp1PF2p1endfLSP6kbH7_CyX7M3eHHx_LeD1lLSa8XKhfXM3D92wKSH2ZvsZeSm0y624Zvz2S_3xWEXwpOJxvRoGZxUP56qCVu4qv8p24U9KcVDbwow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpkAjR7Zudyt47dogZhm66od2AiO5DD6uafsM-LcvBaTLJOzw4Nu6Ac47jDoc9bL2tO06qh1s0Z4shXTaC-MkNFgvcAqLY794_LyE18FOzD5_XUV7nusdU5EbhEhRMz_tgHjPnEuLWBLTo4ME7l_TqCjAbGs8TYbB6VkDoFSMvGB1wEc1UBButdR4bxdycFP1NSP0P2QW1hxSvfcFaopyd04-ivHk6wpNuTEI5ASwbW00RaDabG_DV_noDBNSwuKocw10c_19NDAd_c9RrzejAGPyR9FgUw6QUuzl4B9D_v06Hf767bAKfua86PS2s7l-TK51yDRLUpTwGqeIezA2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=QZZVpxc_lAA5EVns0LlLEKQXy1t-XLF6YtdXflU6P9axjyKmRyHv6l0PvIXDKMD_PGLKNfPwGHRH8rGM2OYt45tJT758Hma4ZoLqC_8thWwi41AVoigXYvNCrga7kcad2rseAJYcRiu31B4S_l-QL9-hLGmmE0FdNubp8aY0XOnm1TMyvvzwjJE4ZI1BZ5hg7XqBgCZg0ZOozx0SPhAqL0L-S2agmkcytNcE79JjVY62ayqr0443iuqthHnONAtCUoIjDtGPM7ZzwrtU_1OV1xJZHnEAOLkRwqYKRprOhZ2r1p198egDErrH99oiytz-xczxz32kMjuodevdux3Aag3oN-9UhAfPoh6PDsv3dcVVx1mbaT0ebPwnblRTRHiEXCO9mnyblAGVkCcglZwJUzNuZnPOv16_1ghPcXMyQgwZGPT3Qf1Pahk8QPK1KXiJrsgF6Zg5IP_JLMy29RKVICFxzWY-PG1_8pLWwQXaw42qBWiGPRvoQQBhnnrBh9TxbzGoPbOPtyvafK9JH0fx8GHGjWmnILJUexm5tFx91poOXAd-tjeCSqQXcITJ6b_WXd3Kysw74Ta7eIPQW2eRWmfy4lRSfIPnkPYGq4TwRu21qRQO6xrMIyUawRiYUCuEE_9YPArIuASxxP7LBsO6UC4FTUWUFZk8Apa7tJYwoeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=QZZVpxc_lAA5EVns0LlLEKQXy1t-XLF6YtdXflU6P9axjyKmRyHv6l0PvIXDKMD_PGLKNfPwGHRH8rGM2OYt45tJT758Hma4ZoLqC_8thWwi41AVoigXYvNCrga7kcad2rseAJYcRiu31B4S_l-QL9-hLGmmE0FdNubp8aY0XOnm1TMyvvzwjJE4ZI1BZ5hg7XqBgCZg0ZOozx0SPhAqL0L-S2agmkcytNcE79JjVY62ayqr0443iuqthHnONAtCUoIjDtGPM7ZzwrtU_1OV1xJZHnEAOLkRwqYKRprOhZ2r1p198egDErrH99oiytz-xczxz32kMjuodevdux3Aag3oN-9UhAfPoh6PDsv3dcVVx1mbaT0ebPwnblRTRHiEXCO9mnyblAGVkCcglZwJUzNuZnPOv16_1ghPcXMyQgwZGPT3Qf1Pahk8QPK1KXiJrsgF6Zg5IP_JLMy29RKVICFxzWY-PG1_8pLWwQXaw42qBWiGPRvoQQBhnnrBh9TxbzGoPbOPtyvafK9JH0fx8GHGjWmnILJUexm5tFx91poOXAd-tjeCSqQXcITJ6b_WXd3Kysw74Ta7eIPQW2eRWmfy4lRSfIPnkPYGq4TwRu21qRQO6xrMIyUawRiYUCuEE_9YPArIuASxxP7LBsO6UC4FTUWUFZk8Apa7tJYwoeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=twf02ABE9H9PHHVXkfOLchmK5uCiaCHkdmh7dJgmsWHA7HXmQtrTwt0DQXrBrYNdwijP1I8wvzf7Ua3bWvpfTACBQUiywFBToWLuzCRnjfuHqZ0MksjdIN8UgB9y6RI_2hTQSuRtPg50gRM5enfVeHnaUUgOodHkebjy7pO2Dq0D9WKDUrVptIcN25gjOBeZql62S7vIlLh7EGVV54Am0bTbhjN2Mt6YjljB0o1OF3jn76guydzmbvrYQbttwJOox_P3iU1JjfgVd52RtMlhEMzl0vMqtxj_QEsXtLJbN4GFR6kVjdmMxrH7GdJ8E6XUjhT-MfbGhVZ2Dr9LH6P0vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=twf02ABE9H9PHHVXkfOLchmK5uCiaCHkdmh7dJgmsWHA7HXmQtrTwt0DQXrBrYNdwijP1I8wvzf7Ua3bWvpfTACBQUiywFBToWLuzCRnjfuHqZ0MksjdIN8UgB9y6RI_2hTQSuRtPg50gRM5enfVeHnaUUgOodHkebjy7pO2Dq0D9WKDUrVptIcN25gjOBeZql62S7vIlLh7EGVV54Am0bTbhjN2Mt6YjljB0o1OF3jn76guydzmbvrYQbttwJOox_P3iU1JjfgVd52RtMlhEMzl0vMqtxj_QEsXtLJbN4GFR6kVjdmMxrH7GdJ8E6XUjhT-MfbGhVZ2Dr9LH6P0vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POE_Y3vzscfFbF9QTsINNyKsGsYxj-_vQL971GcLZgpk8OSuX10gFVaCJdPaoN_q6ChaoEHGK2vzxhrLMwjpqiFYYc-uhLydG3ppgSuVETrvsaRRVKdiEsZjZ2aHwKIF2XXNb3NCLu1ivgvqdeScxVXivXGM8aH7JwYqA3uJC3BzIn0YbQgxUiLSqNqQ_Q0IA0zbQsOWjubNODblOoGnioCJ_M-uMXjPPbStpq0bcoagf80lLoR92j-iIt7sZwpyEepBW_BIXvMW4s5DwyClDqFoQaYVr3HBHXpiVhdNWlpogiXdbiFd5GaLyfs8rlOjkfQ5I6IRnj48XhF5-AY-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmy-W557pcsXJMAgtVtfAmR6sNMBuWKqjLRHBmlF4cR7Eh5-oOOpOsi2e7893nFZ_Z8U5Ewt0blM6SlZqd_XMvSjUeMOQVJHTlBeqPDFJa8kdpjB3yN_jJUveplZghHzoSVGexWC2AVAF6E6nybPBT8KeBwdSpA0rAjC2DrbMOC51K7kZyUjHNL5Yx5E1P4dmugSWJS0J9ZFE2Cvn7NqnsAbgBz0SrFeRMw85MUyOxf_es0YJXcOUJOUrorjoM9Dqu4ry5zv-SbRbe6zqLEyHkIhTNmrDyki9q0n5lJEFnvPyMUSDe6MMwTdGNtzq2za0wkkuhgte1Bp6cUvRsCO-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkKgnSKS-ODhHDzRr3EZ-WoDjoZdalMzkhgnfLJ4jnE5sW9zVJPElhCivK0XrJ51C1PZdy5OPqtLm_41THBkisod9lUnFYcoOF-1gBofYwZtbTbflcLLjWdmi-zlu0ixgdqP5k6J-KJkpTgzM3idexurPcFo1MRVmSHakpb-67poyS0SXzQkg7_3_G35r3xW0dMKw4KFUMlZz3GnUjMV_IVpZUebz4hcVVMlOv0aKxTCq_a3w1QXDHwu1ftdVf3k_9Rf6iE-pC1nZi1lxkH4BlEZJFZV4JtJ-o0m0m8FnW2iSsBMuNeMj15eI-2Uepv7DtxD6EjyC_878O5hXMmXdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRebdzLvcx2Ws_y6msUWTR2-qNNoeEmSMoF0TsOCgCx6kQhtjvGVOUdP9wJaAURIFY0GV3JNezo2LxJuM8H63ooth9olUPqLh5gC9jzIHG0UUJQ8youPIT3219St_QaBNBOzIGTVzJX8HQaJcOQ0cxwP6XkTvEFX5aMan0DhUt4HQ2Ba2DxfPcT5bNfof0cvN-bddMcOw0lPJaCYGXLYAUNXEH-LvQFPC1tZvbo3bu9drb4gL1UTLDY2OmLT02Ok7BDzUvbA_TYwMqbwuTQ60WBlOd3EpvLJ-w7ZTiL-z0WS5hngBHNVZ0CktK8sYmvouhrrMHOYqdEhrH_BSO3Kqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNWZ4SSI4kgRs9XUBP5m_U6pxiU-oWoNnY1NZJsJ_mdHA_VCPEG5H_bJ_3PxrLU2KhtjdILe1zG-dQwrCGI--nCcmb-i6aefRD3JP_kaQ247UBONYLOghtkL6ii2EoS2iNPF793nD2oHoLIAASUqykUU39kaPll9gh5ceRb3C9koj9E1STVO8lxdqpqB6rACHQqm9D3X5Mmx0g2cmVzb0BqZXGKbeNhq3J5F_90eIWaj03Qm0s7Gbf8S440LgjBFp7d_r91AFi1QZHejvcygcxTH-TPuPlpZnb-9oTjjA4PMPcpJkVjes5vvFDULpgo6z41m9arIOYZjk-DyXlXW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoSz0FZBj99Mj7efVNL9kJnO0dd2ioNMP5OJZU8DwEr7Hs2mvuSH-bag2o2Nk9jSIXE0su_B2JjTH7-Aof7xYYJZ8-nNG4oDGYaM9x96NksH6-kPH5LhkTavd0zYLwxnF_-fyMTgBDo17hz96TQwpmu4rtw2QQthvTglxoo3Y7LTgkaitTmA6csrrnPEz-hJwgxfjSGQ8rr5Jn-ru1ajzJludYrlMz2WEQcY2vOlFEHKf0NiV3M3ESsXQqd2PqFTaia0p9UoYnf5tsmn6U6P8gaawc6GStyNzAIBpLTUar2y6mmxXQNWqkV4nYqCkHmTzmTCIzcFXx6UllMQTAjyfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVTcPSAyDaSDPiCdXHAAn1vWHbxgb7TtzTGjIRqWkCRw33AN4IuHLa8P2Ux2g4SKgVBR18vVCKkdHNI-5ajWnDTuLQWuVrBkS_VejajBVOXDjBZrrNfUBcsVXt0wqBe7J9tI2uZMj5Nh4hOxDylgvdkxmQCemQZqUmngwIQvr8WyZsGi7zEBYWCabYmOcrzzj7PUuYhDwe7GoGJf8ExQedoQ7O68NsQP1MjN6fkZFN376RpY1qyy6gLw5da6x0lUDRINgGGtHq2OkNyr7wfpHuHIFDY6xCDAeGyckhh1lnWQEEHQqRBgiQI1FY6Usr8-AY7eEt840uhI9pyY5AVvDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=uljISeYZli7cShmi9B_13xkqiC-g6zCwFp9I71SHiDMplJD5aERNCGI99fxjeWXS2KE4QC6eTLj8biNM46I6tF8Y9wY9dBAwln-geaUuMpsh5oCQc9IbzFGQV-fW2fkKR2aZb--nB01hqVso_Tnm-zGe295bNmBkxx-3VNbfgBnGNv5UBwTemUn0zuSXvlxdrU7KfjutyF9PoYVQSR8Qf4VjJMnBOm2T_KTzldhcoHYiRXSZCqS2ZlsH288_-VY3J3NF44IgSB9vZbDTwiDijXaJWYK1Xr0WXZqI1vMFbmuN3Xa8vdPr32g0A8KaZlyfsN15G-bvoGI2_ZVKlzod4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=uljISeYZli7cShmi9B_13xkqiC-g6zCwFp9I71SHiDMplJD5aERNCGI99fxjeWXS2KE4QC6eTLj8biNM46I6tF8Y9wY9dBAwln-geaUuMpsh5oCQc9IbzFGQV-fW2fkKR2aZb--nB01hqVso_Tnm-zGe295bNmBkxx-3VNbfgBnGNv5UBwTemUn0zuSXvlxdrU7KfjutyF9PoYVQSR8Qf4VjJMnBOm2T_KTzldhcoHYiRXSZCqS2ZlsH288_-VY3J3NF44IgSB9vZbDTwiDijXaJWYK1Xr0WXZqI1vMFbmuN3Xa8vdPr32g0A8KaZlyfsN15G-bvoGI2_ZVKlzod4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No0F8SIPl9qN5rTmCQ6zaXOrndMIfrRn13LNYxsGPpwsBw8azOUmH7UP5FzV09DCVaSlyniZmW1X6X6RW8rhu-AgyVPfHJ8XxsXyTPqZPlaWDtEvY_GqEX4QLFvNpL_R2YoerPZHbh_2553P6hP3DE2lvFKbZqcYk7dB3um4F-RKtM342MnPyJS8D9cSDHGk3I1C5cy4GQnMQS546tX1SYGUQ9sL5U7lGVgXv-y7Mk33X_C-7wjz8piv8OcM8VSatfymlj41L-0o_nM45SXNTl2OJNGs0MGKG5trxWma4nd5XbRLVrud_CSGOuZaozU1qjznEqMiXFVbssrbjiCsBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=bcbeGmJBnnp5gUQ8ujkT418fvh8OgRY9pRUr4pIYAO9ckYH6dUnT-KDjoe-t3_BPsqMbJ21cQVRX_QDfw-oOlzQb1OEAEClYC_eSCauPkbk0P_G8YnsnPhJXp3uHeTDNmr0hhVzslEOXuLJpWeWBToG6iOjdWPZRbLKw89IOGea06RTK6VuWZ4SkjXuvinppNZKb4fcW-gTypCzl0y6rp28dY4E65pzHUHx6otB1nHpGzuwmk44DrW-DEXqK08Mk7tcpmyOgtxmhljiKgfm8CE8EWnVFieCAoOOdeC9e9ro2wqFZIZ2lfq9C3qPYzuq161_Hz45pQwULGAv7keoFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=bcbeGmJBnnp5gUQ8ujkT418fvh8OgRY9pRUr4pIYAO9ckYH6dUnT-KDjoe-t3_BPsqMbJ21cQVRX_QDfw-oOlzQb1OEAEClYC_eSCauPkbk0P_G8YnsnPhJXp3uHeTDNmr0hhVzslEOXuLJpWeWBToG6iOjdWPZRbLKw89IOGea06RTK6VuWZ4SkjXuvinppNZKb4fcW-gTypCzl0y6rp28dY4E65pzHUHx6otB1nHpGzuwmk44DrW-DEXqK08Mk7tcpmyOgtxmhljiKgfm8CE8EWnVFieCAoOOdeC9e9ro2wqFZIZ2lfq9C3qPYzuq161_Hz45pQwULGAv7keoFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAow8yeHw7IiUyiVrEGEJq5AsJmYo1qkjQjLUfOqAa6vjX6Nhr7pcEaVAN4mRDDUNY9VGEG9BfGtJARyBwslTUxxYvzW8ri13Mb4XbPnmHVRLaju_JN9KAfR9qrLf9mg8MQ025vorIfsHVx9VBL6WNRb0NLgy_RQfgV8yyBJcXsXH8pOyss7OTehQzlYOtbn86bUJAsPNI9imiRIMDxJKM8WiQ-H7IXnPZyYgl5vi-cOEhLFwpUP-DOnM4ZUVzDiFyiLpkQwqP8gkGbI6byk2OIGujZd5Pn6wTMX_OUEWhSk_wLiF4PZCrXJOvU91PuutPYROymeV3s4rpydo7SqdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGIy8abmC9kUIZ1_hGe5SjDkOrcxgPD4VJY0rbbuHzb6KzxUVLa8niG1osHLaR6VDyA4rjcPOXjMJmfSY12hwN6yq-wlI2DdTS9AkpQaLE4hP3ZO0L1z5Ewr_tKf_C4CBfubSu8ubwT9jKOxBdcVA-FWMDEWgj1Z5BKbGIv9D8X9W0XhOpxpas5c5XNpy1NwqoGO-U38D1qcMB8ZddbTZHw4xpFUloJ4ABPQ-yA5oFGfhE0IClX2jgZfwt1u3a7v_OPD5kq-hDGQ6hdnQhC5WrVm3hg4cn5Hz2arAHzM-btOdT-dO2BXYT5_VxExWfBUeAoyjHgwNAgV70Kskdtu2q-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGIy8abmC9kUIZ1_hGe5SjDkOrcxgPD4VJY0rbbuHzb6KzxUVLa8niG1osHLaR6VDyA4rjcPOXjMJmfSY12hwN6yq-wlI2DdTS9AkpQaLE4hP3ZO0L1z5Ewr_tKf_C4CBfubSu8ubwT9jKOxBdcVA-FWMDEWgj1Z5BKbGIv9D8X9W0XhOpxpas5c5XNpy1NwqoGO-U38D1qcMB8ZddbTZHw4xpFUloJ4ABPQ-yA5oFGfhE0IClX2jgZfwt1u3a7v_OPD5kq-hDGQ6hdnQhC5WrVm3hg4cn5Hz2arAHzM-btOdT-dO2BXYT5_VxExWfBUeAoyjHgwNAgV70Kskdtu2q-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=kDbv4pL62Q7AFF2B3eUTBc-L0MeLL6WZEDAXcaIHUJHW1qTLniRzPD6NDbsnYBu0zr5859oWuQLqpq1TJj-GyZVeQ-UHjpeZfzhgJjU7Weru84XXzxinoIfMwLH_dfGoR5xt9IG1M33oQ0Q9Stce-7I6IYejhllgMxDe-jFy0y1I-ogKm7vCPdWzM6yfJ_EOYpjgEnI_tbA9Vb89VqsgWUMzWUiq9S0OuyDwca4rrrHeZej39StXbv-aMvepVWqRx2miGr6l7h0EE4OIL0zJErr57ldDT2JSwSXkYn_7FgEiX-At-vup293PGz_mcCpxQ1NSo0AnWHIjgFOkKb6yCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=kDbv4pL62Q7AFF2B3eUTBc-L0MeLL6WZEDAXcaIHUJHW1qTLniRzPD6NDbsnYBu0zr5859oWuQLqpq1TJj-GyZVeQ-UHjpeZfzhgJjU7Weru84XXzxinoIfMwLH_dfGoR5xt9IG1M33oQ0Q9Stce-7I6IYejhllgMxDe-jFy0y1I-ogKm7vCPdWzM6yfJ_EOYpjgEnI_tbA9Vb89VqsgWUMzWUiq9S0OuyDwca4rrrHeZej39StXbv-aMvepVWqRx2miGr6l7h0EE4OIL0zJErr57ldDT2JSwSXkYn_7FgEiX-At-vup293PGz_mcCpxQ1NSo0AnWHIjgFOkKb6yCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BZVffxpbwQkTG5KszgBNJCrJCAJLtD_WezkX8vgb7JY8og01oxmn1a2FnS6yIHXmjEQuJQR6bGwS0kQVlcyOAjJHzPitBLSSVW6vGGbHnMdvT1VMhuJGrc9voAHPf2Za-W90LRW8OzwDojvjtK_on-_Mh2I0atY0yDe1jmoahDGAlWVk2iBluJ5-j70gf1zCMBZ94YLm3jttmjRBNXsnMCQ-RdQ-SDxdTx3bzh95Gfc3G-wOqJYynTQy54tadaj8_Sr2hOVij6aNKtyNwpBV4F3wV5xWzPJGXCKE0wNtMsV6qrWu0dw2CIUM-9XDQfsrOXFhxFJnko-EQPOfPeWr7TE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BZVffxpbwQkTG5KszgBNJCrJCAJLtD_WezkX8vgb7JY8og01oxmn1a2FnS6yIHXmjEQuJQR6bGwS0kQVlcyOAjJHzPitBLSSVW6vGGbHnMdvT1VMhuJGrc9voAHPf2Za-W90LRW8OzwDojvjtK_on-_Mh2I0atY0yDe1jmoahDGAlWVk2iBluJ5-j70gf1zCMBZ94YLm3jttmjRBNXsnMCQ-RdQ-SDxdTx3bzh95Gfc3G-wOqJYynTQy54tadaj8_Sr2hOVij6aNKtyNwpBV4F3wV5xWzPJGXCKE0wNtMsV6qrWu0dw2CIUM-9XDQfsrOXFhxFJnko-EQPOfPeWr7TE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2Iy--69NMEsT5I1Cak2n8GbOUCpvNh4lnxqotmUXa_sJ0tZCcrXH-XgEbpRBntLUjpVKsRjl0mGp3b7JTR68tvV7O_6ikGya5WagyLT2xXfuIKX1vNIemKwcuIebzQLTohkTCbUR2xfiExaaj-HLIV7YL57x-S6Ccd5xp5nAtZyTerDejv7ZFLn1OGh_NxYSWlQ1p28g1AsV4jP1eWvHA8UEUfWsCQ6RLdPzW2iKm4ukuRYEsSr1aJXgUI97fC8xeqNZDJ0C8tYDs8Xp1-83uRd8yagfKT9B_AvzoHOZvSIWNaWALxm065LeDqCUFLHD2YwkXJEmeJ6ECpd9abErA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDOVK6ccBWOV4VTEVOxRnHFHVkVMrIZvTdYQ_awon5z6xOMCaOpJbrXq4TcEl0jR0FUpEVYlldY48RHMoltp-N5tcr2ah0Qe1Bi4YgL3OuXFcGcz2Uc9Rdx37JgZhV3BwPYB0J2cw1CZRoI3RmibXhB7iw5zQWzrSnQX5Cvt26X48tO4lexvIeG3ECHP0WJQCNXcJERLMd2SMPY_f9ZKxtmG6cd2Pzd5_ALjbBbtKi76KxRlxkhxQLAgurisDMFqJP0_fd3tla6pH2rdcA14w2SgcAj0vLyiessX4TcrQJyspqwTVx_PPQXZ9nNgHHpAQU-8mXQSErqVI_jZ6kEWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdtqPDz-vzh8EAOHtWtDHR01LGwalCNXhcF8aeKonSDyfyHjzDD7KpZ1iRB_Aaf1DdwXrOlRBfk-TNc-5Xi1Nd2EN_HfTbXoJ-yszQAw7M-8IH9a_bnAVlDits4HQboI-L0W_dmD5ZLunDsxp88YnqJGCZnKcx16ygmTTnKAVHM6c1JNzpOQhGSj1p6ngYVbC4EkS6EFFQsSOWT6K2r25-qYjNlgO_V9V1tNggyZhR5aUorGq-2lSXHn8aaBVn-ODzgCM1SmcUiEU2V9yIjBGGsoLgyyl9zgJat5KqlZl20edeQSWBoCaDsM5yIQoOw-7yNzV9-fhnFdE9D-UdNt1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMbHpld-P451MNfDtob5j085a1O0XuiMpGb5rwMncbHSzHvOHKuCwvVZGZ50HvLRGhyYJ_zdMVLcm1ktbmHksNiaIYZ6_5fdCP_lU_it6mfAKRHS4meOK21YeY-yO_rrBnEo972GX2yz7TvIaWXvBd1t_C4pr0azCpBektcj0UfJAllGa-iAKM1TjR_D1EBE7dtoFoZK7385VZJo5dM-gKYPJjZgZflh-smpJ5qBo_o4CfJugdgrjz4Rh2v4Mq6uSsG_vzCKrgBdZlFdmiTDoHpFfwqfdxKT11NgGdhkjGOcjOWkdXrb1BcqKw9tTlLBNGq_WSifvIJaug2f0znz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGPh8BdKaU3R9vJywAfhzqcqwwc_RVJwdec83FAhTdOOKaDa9ZrBMAZTlPUII51GhGejZUNpnbJhEWFAFGBfcJOMo6eYQ-hF01mmrRBeUFE36z54t69_FDWOn2HgFQBaHiaBHz4S1SyuJ_vEhB8mbhOKZFnaiz_atN87iLdGl_lVPyCi6DQaWZxwDoY_16uSI2P3PMk1xxbU5id7x4c4wvtBgniSOS9RFUFtHZa1BRoNVjz3kGHr5eUQK7WXg3Jdt6ID-I1ekJ0X5d7-9aa3GwHOlkPbjV2_PuWQ2yJ8SwasKSMxEcNEWBiOpW0SQDF3J8Nc5QCzVHn-4xhYB4ME2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-II67o9Xl7uKaVqdrMxF8gost5ZL-oszBpUU33RkmBZ0eisreDQPipnnDkAJCB6Zt2ivPqZxD26GH8OZl5V5PSfySdcD2FvibWwQ_bH_bqfIojTmmf5L4taUPoGOznrQ2xWYDc1zjYYJ0aQP8oAESDoFrlcaIabLOgjZ3J1BIm0TdYgcZZU1wuv-klztmeLvyKjiCdZkgVO6GSLEeqeKPSAcbj8l_SUe2uRBn6PTeJJQxLVpTAV3uKNX2zN3qS-68X3bMTUfpfMMcplXrYtFZtDjHxgLlQ7upDY_p_ad5s6ng3an3hoMuPCXQV7VapaZmRqXtC9683lbJGHkMDCyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhjSUzh7Njz33l6glAeDMFA8NOBnO1UcwfdY1IE4NVBYLL1ev14fkdlyqORqSDD1hzySh-kmWElIpIr21epNBAsqZ17NW7vMnRi72AFz217DEi_6FfIsxucvDdd5vB8ewuDqSxOaMtlWYFwtE8yBtTa0bQv3ES4ruy_Tp_kRtap0YcJTvLaQ7pzhS-zMiGD9Oh0QU9GmLEnXhmPizn-of1QBL6BatnL83b3OLCfVJr20eC4jwmcT6QtCNLDZEu5RTW4ZsA-zH-QdlCCun9t4FxUpk9OVmOleTBdLYT7fMct-s88vIAQbava9vjPKhvMttyD0w9B_5P4Q4-3w5L7ykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPqvnDpPM38rkYGiMOhQNM3ySnfqRxVChWtnea2kmBS9m6cVaE-BmyMSkLghIX7FvDb539D0ukNikdxFON55dwnlAF3JgOwNaZHQHt-Pq4vqzzJI9ZV5D2MXOgYPc6Cva874t1BAz6Qp8kVAKRV9ekUsd0PTI9hbVRlLpU4QaRsTW1LJJsieHQaqZj6txtXrPY3z737Y7DiI0nzsrveto4sbNBkO0E2sOHxvEmBGChrAikA6o4eJIipW6QPFNlzkF95QGqLjAXp-fVvK3I3hSDllSokms-nF4T-Iw7tgrSVm9zVd2IcP4Og6I29b13e_vTIl-Hbut2TrAa9TDEbkJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
