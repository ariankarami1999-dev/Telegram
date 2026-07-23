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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 21:23:04</div>
<hr>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 727 · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5E1UvQisOUYNvRIBdOWx-bY3uG05FRSG-1gr3f2qY3oNGAiiIv2GUsfaCeCUVPwrhKFukgNo_CqWHm42-opva1tFSKkfTeRpdqHECndLHEEMJt-oHbJJpBy4HryLEee007nSj-xlxGShSLG0qTGx2VmvD2AHuB1RmL-015pVBw66W_pGkLz-eEBBhqWrEMoGU9SOGrKhWRzl_AFtOvQjI5DuRRQOMMgKAzSSSPO4PWulAJR6DuKHFfwtvJZz-sioJ17H7-CeiTyznVfOEOn-eDON1cY1BbsZ2XtNzV5iu9yFSunEu6Itqj_4Z5UUIOnBzCruoQFdUnNuFCxtN-s1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov-5teW3tHTvsvSbgMdLICYXYlU_sDGIu9OuiTSl0594zrfs9gRoJQR8S28V2CiP_XCjD7Zzp5uItinMqAUIbUIRvVFn3zxxaqYh9Km-0nk74uSUdeQvuMYluMHfHS7WfmU5Mq1R_o1vTjHKfD6MlZEq2Yf9KVRt4d2gzoWcCctXxlvrZ83-13fvHD4NvwcgSfJHIpLOCqzOAdqDTCE-6frq1o_rpZ_dr6FZtGyKaUvR4uN5aL7iKlIR-aOJwWaAcP_ZJcq4l0tyEkcUu7cd1nNA3Bm7_vFPEyFbPsYQr_SdVeOSm92Zw0-QEekuDDdOwCr60iw-tbsukbzrBFNmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHVVCza4-k7lMKxM3gRJStW0mSmbHx1HOC_kqRItxfPQPZo3RqgLfbxvjky93wErqiutSbOoRDVDgJO6-5Gt5GeEQYp3ZpC8LbmHHVvogV5fTJ8tjv9WUtzfZpz5NJscTMxYul7zKui-uhcGtGwcbJz9kr1kP6yA61rGmmeIOf2BDf3B7TQdUT7ccFphzbXnhtP5luogZEm_0Gi7-eRD7KumLBDmDBfFnXn0yVHUWnWFFsbkQWbKqce98C8p4SF3LVslyiNzTK7TUUb1kdRXw9U_E3m1dmBOkEfxlEWe_yZkhLuLgJrZdcC01kX5yYjphMbJYFfm6UDxnofukWHSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=odHMJ-cnZqCmU5M3PkKe1giDk61NuULnnlWHW7-IDjpj1CA59hdM_SCHObNT7lXoYB1aiPD7t3cLtdvgzhH6BVkHDluFt6XLM8NQKtajNrZj5RLMiJhld2Aw82wz2VlzUqzTJrHzJcGL05Oo86mJeVJs8QB1pWspJa0C0VLjS9R_lKplwOkAuQuEdT3hw9QP3azjPl6PTfUR6xJ9NEe2LfcoD0Y2na8Hx6J7Q0V5utWPNbS3BJDc4Sp9vaHSMjWQ7mFj4_zJuLGxOPnP1EpcHauNIm6iyIHWLa5kYWJ4lWrjxJ4C7Dnl3jxnst63XLluGf5kDOMYX6NPrWivABaK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtqbusLboLN9-Lrqe9rkYIJx_IvHR84ZEHryWdkZeDoRtrOqikXN7EiCJPyxhY0K5n1MEgMzgzs5MR0SrgnYs_3F8GgLoDYdKQ1LYTW7Xido4AUaYEQj0QO1zbE_UI2rRR3Xjp2NfzvzJlA17Y8-RYrjCC40HPKznslTM8wL2b2keXdTihMVSAzhrWsKM2zE1ziTnSVNA2CcNqGAk4EUva6MDz1HAScSWM2X0YSeo7K-8tO5E-3qzHKOu7syOVXFFTPwzsaVcApsYq8y_51MikBazPUNTFYfJVOy4371oGxyqsfjv9LPjVEwVrFbGqSg_gT-daVP7dZWwSQ_f8DMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3cy1W2TbhAEaNqko-LkofOvGARhOPamsqF0vCHGyMTA7VOKKvkblmGFd3Z1Cmu624_ja_tAa8n_bbjHmnVTuhNxKTyUxVAacVcYG-q-bRFg662UE5Tria8Te2IEuiazcF5nA2jXoZYHbcMMvjn7bJRAgoWnuSmKAPfMRR3VWB-izE8iOD59w2umFAgheoI3F9cBvPYJO12pwPuaKptJ7YQSh8wu3vjjT20WB8oaFhMleR-Rvz9k8qJK0iV9UMgIccuu8fRJNoDpaVxYVJ8kU5i-VJKdGxh_NlssZVWq_v_rSGXU4LXxVobrRtTg0YWElxLIttczbSrrKRw_7LA-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlt5ohzv1OdqdVm8v4Vv_IX-0JFxqy-G8oYJBsuVCZ0WE2qfU_wROvY65ynPOmrX64NDu1vsIakWGR8vtT5mKHiFbPmRag3vXe7UCO-ac6X3kFZtMEYOSBj3paRx9ihuXJUwNkrzDcQC7bhdWgz1hGE4R1GRCfhLDJMbgLqIUpf7f2sXPUilv_xg2uxob9rxE3JcTndqTsg4-0U2ygixisi3tvIICsmZs1VA5ZV7iD-CYYvf8wrUuw7GQd9_Uy-5W5UAehUBa8MWmeYo45X6O2MYhXRRi1pa2cADIgXL4oopEXqLay4Dun6X1ZHV4RSNCEXLfJZxw1XFgqS1ctKtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUZWzvmoqZKbg2Hg3j632oqFLk1s6y0Ph4BmI1FfCDNkfzW9LmbP-klbRXbThuQIo-0rrfbCQy-UtthBviCQugRULJwGi-14BfB_lV1Es2l9xlVnZUhzX1kqERC8CvSC3odfgRdTuQmtblhV5Ynys_R6qFiv91_duQwwT9VlTb3DVKw_D7A5CEKaBwJ0GLJFWcrrIj419Y79wqvBQet-7L0Lp04luMiYkKZWqMaDdZbK8SRo_SI5fMdekoeQaaK3J1igScpRTcNCS-l-f1HRQ51Kokeco_esn1XkEjFeJoBqc40o3tGeTn61SzBC30Aiw5fodue7avEwIOk5AG6uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2yGdlVEuqBNZcYJmXvZjV0QZNscIJQtqQ7hiqoI5mGWPfJBPdMUr8QAL57h5lM5uzDvDlEUf6ztGCzuoTfPvyneW5Iy88xrqkr8gAyUVASZd905jkuFjIMjrrdEos1x2khwrSr6OWgJGDhjiCN581SBhPRApOv66YWCtDA94WREQsUODGNdgGcwJmf5_Z-l67-zQRq6wDu6EPq1GG69j5NlNUROLYUrbHKjp7gh4G9NytkhS5pKL4y70vYfSlsjOYZZXwy75ApELhEVOuyFnwnGJeLsfEUE-B5SLOXvBS_bki08TIVijZ4XSsA2OiIFxG4RYjThOV8J4KKZMSpZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSR9kCmiMdQGwgwdw52BdE9p58AMB2XEi1L8eYER5ZggYMpOP7hX0W7cvvqQK_bbVLBEQ7DvStIrUJDFtfjRelqsd6SGuG4OlCJ_tHXh6AFKQu-vrqzsAKcPSGwHiawnvI3v-HDftq9OlqabqzoBq09H2hkjAs_P7oGCmErdtAzS63Iz2CzYTQoU0UzRNcnN6ugTPlgSw3L4Kmcv8t1HEdywICmChpjOz181Uq_iOA3JxiHnvGyAFcneL36Aj_EcSTsr6rzADKRHHBpA8Z9apYbAKcRd995P1jsDYRrwRtfLDFWKgUpxcPTZPO9s_mMS01JbTCNCox7GH8LJCDgZOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyWrv8bPvmcaqLKbKPQUqioUc5ri7dInVGG8dm93xlEkNwz7KQIg7s1189fkHmdQqapyv9YWy8GQDZFg_whpVPAUzt2ystn_q7H9saAv13rsS56ifHcibKCAZ5s-K_KhwdgitJSCrRpxbhnqHa53TR8B0ciEdAYYX5Q3Z_FCOF_FbYa0Ae1L5ABt5VQn4Ad6dD8WoqZYYAoUB4mwhqvYByeLllHEnHj3C_Q0eku7a4nrwroc2h9MzASLOJ6O-X-iGmNvUXd799aCa6WwBPEvxEA3Lj2MJ55UiRuVg8QhZmDLIVGyxIGRtrxomzzbQ6DmZ25eFw3Bag9EI-voJYHzeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=JDnF67FA3imWMh9Ea_D83YlplOSC_DMew7HdI8EzW7DDl-bgw1WN7gyt9tzWAfjjBbYL2pKfzoQoYtYvtCuwsNhgW5EU7L0psFEMVFlRoa2f8QyQN0EiIy8h6fAlrI7elaYByZlHeffyo5WzSwWvEhQJQB0sOhqOjvD0ApZX5URpVDE3OBp9WKUQZ0Oj_EzIjSNwbhTWCjT7h62oUPmLjCeIaajIA7NZdWXNM9ofOX90h_AiKaYSUBAC1Ct6tOU3qBvzCERWQKnRwgBvGa11Z-S8-MQLVSMo91_9quTijIMsHm5g_AwPf82I0ynu01r5-MNel_LgCmVy0aY0jmUwqDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=JDnF67FA3imWMh9Ea_D83YlplOSC_DMew7HdI8EzW7DDl-bgw1WN7gyt9tzWAfjjBbYL2pKfzoQoYtYvtCuwsNhgW5EU7L0psFEMVFlRoa2f8QyQN0EiIy8h6fAlrI7elaYByZlHeffyo5WzSwWvEhQJQB0sOhqOjvD0ApZX5URpVDE3OBp9WKUQZ0Oj_EzIjSNwbhTWCjT7h62oUPmLjCeIaajIA7NZdWXNM9ofOX90h_AiKaYSUBAC1Ct6tOU3qBvzCERWQKnRwgBvGa11Z-S8-MQLVSMo91_9quTijIMsHm5g_AwPf82I0ynu01r5-MNel_LgCmVy0aY0jmUwqDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=OcVanp8tYRA50upX-rxKK9kF7Ic1SVCVwadtvLm050zf13WRJTC4mvKD7UU9w2p855cRtfqjU0QuQjdIOr549SHZOb0P3Gx0IHiQMbOGS_cApVx2FzUyQw3Wjhbn4ZjUdbToYKHZ9qjF62gy7taHFQAHr2Tt4-VQjzVj5nRbRiq_sGdxKwm8elMf_J4TXL9yGoitSJ6iMvGfo2qAwUNTcEtekxZZhust8Jgnl5_O5LGLc6VfSWHEmHW35AC5T8mkdpmjGOiJYnSAZepNOinUrbito16w1zRugPqDt4Brn3fHW-V6FwWh1DvPLkamzySGmHV2pbq71P6H3plyzow_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=OcVanp8tYRA50upX-rxKK9kF7Ic1SVCVwadtvLm050zf13WRJTC4mvKD7UU9w2p855cRtfqjU0QuQjdIOr549SHZOb0P3Gx0IHiQMbOGS_cApVx2FzUyQw3Wjhbn4ZjUdbToYKHZ9qjF62gy7taHFQAHr2Tt4-VQjzVj5nRbRiq_sGdxKwm8elMf_J4TXL9yGoitSJ6iMvGfo2qAwUNTcEtekxZZhust8Jgnl5_O5LGLc6VfSWHEmHW35AC5T8mkdpmjGOiJYnSAZepNOinUrbito16w1zRugPqDt4Brn3fHW-V6FwWh1DvPLkamzySGmHV2pbq71P6H3plyzow_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=hdmE1f3PLafZWUMs1SdeZC1Lihz-fmgHhzkHIGxxoliofhjrya-SS00BBPZg6EVESLFWyQcb2ejYk7100kSW3f4iraP0HGXkk972pxhTeIF1h3Ug2qvGUr7T5f-izKXVuMtEc35Q61uDJbLWmaJuiQGbgBWeE4u2ecKueVGaEAlPZUlQPKYeB0-wyA5HARcdTPDsNZS1CQlLq-RFs4e2QURbdRLrINvxfQDcmcCRUP9XL9IpM9W826vhYqrKrAYrmiyXd8AlHBXoCSvvbJpwDZEdUnz-JCYIGGPGO1fSLYWkrE3OU0tctTfwupzFFyzOATKtceO8zx-A5eYZk6XRAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=hdmE1f3PLafZWUMs1SdeZC1Lihz-fmgHhzkHIGxxoliofhjrya-SS00BBPZg6EVESLFWyQcb2ejYk7100kSW3f4iraP0HGXkk972pxhTeIF1h3Ug2qvGUr7T5f-izKXVuMtEc35Q61uDJbLWmaJuiQGbgBWeE4u2ecKueVGaEAlPZUlQPKYeB0-wyA5HARcdTPDsNZS1CQlLq-RFs4e2QURbdRLrINvxfQDcmcCRUP9XL9IpM9W826vhYqrKrAYrmiyXd8AlHBXoCSvvbJpwDZEdUnz-JCYIGGPGO1fSLYWkrE3OU0tctTfwupzFFyzOATKtceO8zx-A5eYZk6XRAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFv_8PVh4cYgShowLeiHtLzbM2wkPQ7zaxuKKbIYGcx9iNQrzpUQiUyAHCSiEoE2EwYwxsVCrvMaPle-5AYzbdOxfH_ZSz9q47HyF2rouJOAUkV76Yt8RGeWbwjRcaaHL4bVWbFqaAFS-ajo5sK_Dc8jKum-TCsmgyAXq7vmIoEGRHbu3qgtKjCYdsW5Zt8hAazdTU9wQcEjaIOT_L4EnvBMV0NDtSTza0rBMTk-oRN2pJ9PvJEhUYM9Lf0fIKGKYWARTUXzXSvGfYiVsEkkXSGtq0w8ke77DeOlZeygYamdZR8X9LGJYchXk0Q2FrRW1EEd9ywLuzqe_aEIrLChEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=AGgmnF2yv-F1wwTu9DDMqhH5jzG1zYHq8m2iQ14huhnvSQUU2v1bMMFgX30b8qRbLsF8JXOvy4uaE9whtEa0DY1wFJj5yucOe7MX2n4aRe8CPWhVlBLTo3VYG-S0qDtcwqgSZC9tZY6ak6bgKnpfhX-fGZsqlsmg0JmWZH4tn1_S4RFlH3hwrer43ySqV1UcHSVVU2l2Y4aGE50Eag-ud8Oe56cvsdwV8QFVwnR7zLuRfuWuZbUiIUtkq0jUWcORrEch-k7Rau-Y_vdjVtGk8gbb-93gp-8b3LCKe0PltNaQHR30rweKRRdh0GNBVk2nFM9GVcLSrkbHhUlAUzCSCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=AGgmnF2yv-F1wwTu9DDMqhH5jzG1zYHq8m2iQ14huhnvSQUU2v1bMMFgX30b8qRbLsF8JXOvy4uaE9whtEa0DY1wFJj5yucOe7MX2n4aRe8CPWhVlBLTo3VYG-S0qDtcwqgSZC9tZY6ak6bgKnpfhX-fGZsqlsmg0JmWZH4tn1_S4RFlH3hwrer43ySqV1UcHSVVU2l2Y4aGE50Eag-ud8Oe56cvsdwV8QFVwnR7zLuRfuWuZbUiIUtkq0jUWcORrEch-k7Rau-Y_vdjVtGk8gbb-93gp-8b3LCKe0PltNaQHR30rweKRRdh0GNBVk2nFM9GVcLSrkbHhUlAUzCSCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=h286zq3ZPDmPmBM2ufv5Fw09WCnLoRWiKhoNg80eVN3smu6TyTa78rbAsapwUe9OiaoQkWN_K9o7IZxPMpRSEVEf_2jse9XYNr_B91WaXt2HffYMK1BtOB6e_U5DrfNAxz84tleF1R2-7c_mPWofbpsKUwYac8XDN22v0JU3F2tjw9ZqQ8rF6ip1oNxK2dCRJdhRzARcQFP4Mdwu2SycJO3A8VbEnN_Jps3X8sjkt7fZsLAo_Da0nMal5E7woTjxdAMTQlEPICJ5VdI2RlpXhje1J0C3yz4PWAdigrBkkAqpHQ0zAvVDAb0XiASRlclXVxnSTyFBwlTjee5k0akc3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=h286zq3ZPDmPmBM2ufv5Fw09WCnLoRWiKhoNg80eVN3smu6TyTa78rbAsapwUe9OiaoQkWN_K9o7IZxPMpRSEVEf_2jse9XYNr_B91WaXt2HffYMK1BtOB6e_U5DrfNAxz84tleF1R2-7c_mPWofbpsKUwYac8XDN22v0JU3F2tjw9ZqQ8rF6ip1oNxK2dCRJdhRzARcQFP4Mdwu2SycJO3A8VbEnN_Jps3X8sjkt7fZsLAo_Da0nMal5E7woTjxdAMTQlEPICJ5VdI2RlpXhje1J0C3yz4PWAdigrBkkAqpHQ0zAvVDAb0XiASRlclXVxnSTyFBwlTjee5k0akc3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=CYay5n1USjWvS5xcs_EwROHCM45W27FKE2NhYla0mN-LBrxuf9dCeJxMhj_xLq-BV8w4_1YfAbONyYCyFFbE5FHtbfddtzFk97IVvE2qrDE44cVlHFCvGvM8wSRSEQVPpO2_nXjOGsJ5NSsGvEAPzcQOT649fb4yz19WbIrcoPV3FhAD1rA0r15qVdn3t1Ez9Fi_FPsWDYax4Mg7nMgZECSJyZ1Mef40XifenWSGyC4KsHUu6gSQXkoJaTLm3UZiv4VNObGV6qtkwDC0AwrXeBanqau1m7IoRrAvsXYInIWMGykgmloi5i7G9po9666QfPJC8rEkGG17DoeM0sZnlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=CYay5n1USjWvS5xcs_EwROHCM45W27FKE2NhYla0mN-LBrxuf9dCeJxMhj_xLq-BV8w4_1YfAbONyYCyFFbE5FHtbfddtzFk97IVvE2qrDE44cVlHFCvGvM8wSRSEQVPpO2_nXjOGsJ5NSsGvEAPzcQOT649fb4yz19WbIrcoPV3FhAD1rA0r15qVdn3t1Ez9Fi_FPsWDYax4Mg7nMgZECSJyZ1Mef40XifenWSGyC4KsHUu6gSQXkoJaTLm3UZiv4VNObGV6qtkwDC0AwrXeBanqau1m7IoRrAvsXYInIWMGykgmloi5i7G9po9666QfPJC8rEkGG17DoeM0sZnlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=UMMFhN0mh7_fNKbWX9PgvlDubjBL-GMGk137aOFCipTGcFh-8DyINoZR0FOk-pTVN4smLHHmMyHwTowgnyS9w3su2j87HBh-2xxqB4MqBDFF6ILk2e6BJDG0KHBDf-VhYr9wbLKyus2IgNqo9rTQwiBl4RWx8X2GJc3miRErSKvEUzM2T5_z7lCcsq52gyPHNCLmDrRnHUu95KA_sj9rDCrxAi2I5J1_aF4MkGGB_br3VKqHyHZQEaSCxEXEpqkKHq7ODOXw2H8-MOEZKp0faoHAGfruv7FjPhSdr-_iW3s5726MYhKc1x3vtJzjBilIyZC1RNWZRhqmRKsgx30IVI7O-J0orABKcnBitJzrxJfobXwsgY2m6GBJJ34iQzrQl4w6Y8vO3X7BQtQzDtvbqghJjdHyb_NKNOLN2iHVSJ_dsPLlPZjbC3CVJZ0nL8bwTtNva962vRydf1NBGTLF3KXRTMjWjc4rbmc7Q0nGhEWO_gpdsgoxWsJM3RQiLqET0g2ukYo-79QCGdEOf_YMy_F9i1RqAYKV4Dt27b85rFBddPg9ZzB0rAGYGLM8s_StkkXmGdRZrt0aLt6QMjc85LjqMA9s5ddctqcqJKFSss-_Q0DO3QxSlSrgvIsjwnma_ggs0c0kWgEabc6KSKexZndmTjvz0xxvFobsne-IeNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=UMMFhN0mh7_fNKbWX9PgvlDubjBL-GMGk137aOFCipTGcFh-8DyINoZR0FOk-pTVN4smLHHmMyHwTowgnyS9w3su2j87HBh-2xxqB4MqBDFF6ILk2e6BJDG0KHBDf-VhYr9wbLKyus2IgNqo9rTQwiBl4RWx8X2GJc3miRErSKvEUzM2T5_z7lCcsq52gyPHNCLmDrRnHUu95KA_sj9rDCrxAi2I5J1_aF4MkGGB_br3VKqHyHZQEaSCxEXEpqkKHq7ODOXw2H8-MOEZKp0faoHAGfruv7FjPhSdr-_iW3s5726MYhKc1x3vtJzjBilIyZC1RNWZRhqmRKsgx30IVI7O-J0orABKcnBitJzrxJfobXwsgY2m6GBJJ34iQzrQl4w6Y8vO3X7BQtQzDtvbqghJjdHyb_NKNOLN2iHVSJ_dsPLlPZjbC3CVJZ0nL8bwTtNva962vRydf1NBGTLF3KXRTMjWjc4rbmc7Q0nGhEWO_gpdsgoxWsJM3RQiLqET0g2ukYo-79QCGdEOf_YMy_F9i1RqAYKV4Dt27b85rFBddPg9ZzB0rAGYGLM8s_StkkXmGdRZrt0aLt6QMjc85LjqMA9s5ddctqcqJKFSss-_Q0DO3QxSlSrgvIsjwnma_ggs0c0kWgEabc6KSKexZndmTjvz0xxvFobsne-IeNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=nTEHZEY43SrL9HRzP2Q69D9KudhOK1YDT5nPUKOmDfd3EFxdYtZff75QAkrAm6e9xH_EZXFduv0y-02MN1mr3p9x2n7OvraKQjS_1FR4LIYFbInSCw_EbmHHmftSVQSh0pPd2UJ4mcV3B7KzHoQ8vSjAwIEIYqzmjuuHwL5WI3_n6_Q49LYQl8hsnZET3pKJYKKQUdh1wRATxQQRceQRNel7es9Jg2A2BxREpJR5hdg_HPWxtS8oHaOhnaX-pvdnGplupPzKSbUwT2uxwR6JitDQbQNhFroiRU4lD0qqpGQ5OIGVF4K2p64Nd02fEnGE5tKBjI2A68POAwWu8CdF_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=nTEHZEY43SrL9HRzP2Q69D9KudhOK1YDT5nPUKOmDfd3EFxdYtZff75QAkrAm6e9xH_EZXFduv0y-02MN1mr3p9x2n7OvraKQjS_1FR4LIYFbInSCw_EbmHHmftSVQSh0pPd2UJ4mcV3B7KzHoQ8vSjAwIEIYqzmjuuHwL5WI3_n6_Q49LYQl8hsnZET3pKJYKKQUdh1wRATxQQRceQRNel7es9Jg2A2BxREpJR5hdg_HPWxtS8oHaOhnaX-pvdnGplupPzKSbUwT2uxwR6JitDQbQNhFroiRU4lD0qqpGQ5OIGVF4K2p64Nd02fEnGE5tKBjI2A68POAwWu8CdF_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=fb3LTgIYZC8oMltlwnGIypP3kmff5loTh1ZxuCK4uyWSdVAz-JISTRUldqMnX0H45qzgUPiKZfQhzZKxdd32JPpvNS3WpDJuBNKm8niC8ak-0377bjL104rp-OzHIvP110meW2b_ywvZQgWmXLHx85BbivdDu8GaZAGIqarSlp9n7QBhDgu8xHWa7ho7eZ6mJ-UViK732iQQeDBPBtzNGxVNvzp-ZvepDvD591zrjMBBGwJFZTIQsjNvDuu5GqpJwnVbCYi5abJ383ItXsdB89O0d9vt-NaQ5t3WpQvSFx_8rWepXGIVOt5d5JbUygGX1OM6JjbxIJuZC1bSQiWlHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=fb3LTgIYZC8oMltlwnGIypP3kmff5loTh1ZxuCK4uyWSdVAz-JISTRUldqMnX0H45qzgUPiKZfQhzZKxdd32JPpvNS3WpDJuBNKm8niC8ak-0377bjL104rp-OzHIvP110meW2b_ywvZQgWmXLHx85BbivdDu8GaZAGIqarSlp9n7QBhDgu8xHWa7ho7eZ6mJ-UViK732iQQeDBPBtzNGxVNvzp-ZvepDvD591zrjMBBGwJFZTIQsjNvDuu5GqpJwnVbCYi5abJ383ItXsdB89O0d9vt-NaQ5t3WpQvSFx_8rWepXGIVOt5d5JbUygGX1OM6JjbxIJuZC1bSQiWlHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXUbzPK0mUhna_qMmi034eZ4xIh8ls1CIoNfVY1KSPj_EKl03fIfl9_hcYzXL8x8jIm19uLNM4Zfic5Uv2fHGA2ab9oN8zNvkMkylV56xnlF6hGRbYLL0XlOytqdFgDt095KsuSUSFXZUbH50oHqfc6dA__GCPFltkoNIhWBik46828k_QVpzQiqiWiGOwGfqIrJzqhK3w2O28aWwRyWuH55EHE-h2YnrtQFewo4nqEIu8lhOOQfnZ0tyCewPYq9YJlVoN09DXdbAUqRwloJ3pUual_mS_OBl-5-6edXk5JDDr73dhS0TvAbHHNee4e1Vw3kzB4fQQ4MIvi9izGWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJl8YlN82yIR6wq_k_TnWsWmCY8zE_Dw7SoAM2-70uKuamNQUfrE7ZMbFWjo4kOTPhRqcJRj0Gk8IPSyRJXdLlxI_znmXMYTH-tGorvuG2pOz5c1_mRHFz7jSmbCoPPsp_sxEEEWea1G-QfVM71yZ0LDQX1EMH1de11hjsaxNaFDj-74RKZ_4d5KZ0IyVEVImSVUCNfPxoqp3GF2hUColb1N-hMwEFEE_OOQUCcMfGpL8Qw2qcjfaXesxIx2FWRVnq5VRbfO2NMf1-3giaNGFvdI0JsDRw2zUm3eyaNVcnroSHyw7chKoay4hFc3an4OuHmpM7KV1XnC_4exNQyUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=TpX3OGLVh-k7xR89I0CtXSWvXwWVZ2Y4MfE-WPdYF8nVDZ4WGqzEHzle3TwlJz11-LpG20Ydb7Um6RKjVvaIVQQh4eqUg3ZF3Lsugumqf8xZjOmjLiA53KpPa0o9W74n2ynPnuhPBXGJSIpcZeZv06ln02lAs3xAtnmqzoB0bA8faHhuJRCPaoPIs19ydihdvFkKRU6LUqhPZfcTsUeTXUhNkFKUb2YNmWmQVTPrKa_-eIX9XNqngpX2JUlU4TOiPKvKtBf9i48H1lid6YjZYAXmf4qYOyXY5OKFTdMPRWpo5vtSN4KcG2dwDGisoUyiw-RR98zxgJniiZ3AyXvwuk6sasoac2kjMCxLiOD_i8QIgtOJVNCgV3LO5tUuay6J5SFtmeTV8Q70wWAGEVvg7z85tOGIdjTvYEDA8fJLEtANCohwIWsR5FvQ13fc_3JDzOQXsHjtxrwPHSyfWxRchrwVMwwyrj5Q4Sd1f5gdSW4SgwmaCTLEPI5Bh17vamAzWyy5EXlm6f7EOazvO0HYfU8Og8R0LGXa0LL32nitTbqFJieItNVuDskQHmTLS_B7e3AcSukC7ZrE_-k0W3Lf9Sl3Bha1CgwsSOXSLytWolPze3HK-ybjVnU_RYswTwCmZJRmusuFOULwLHtUVeOujlS0jyZX20qII9UHbSL4njg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=TpX3OGLVh-k7xR89I0CtXSWvXwWVZ2Y4MfE-WPdYF8nVDZ4WGqzEHzle3TwlJz11-LpG20Ydb7Um6RKjVvaIVQQh4eqUg3ZF3Lsugumqf8xZjOmjLiA53KpPa0o9W74n2ynPnuhPBXGJSIpcZeZv06ln02lAs3xAtnmqzoB0bA8faHhuJRCPaoPIs19ydihdvFkKRU6LUqhPZfcTsUeTXUhNkFKUb2YNmWmQVTPrKa_-eIX9XNqngpX2JUlU4TOiPKvKtBf9i48H1lid6YjZYAXmf4qYOyXY5OKFTdMPRWpo5vtSN4KcG2dwDGisoUyiw-RR98zxgJniiZ3AyXvwuk6sasoac2kjMCxLiOD_i8QIgtOJVNCgV3LO5tUuay6J5SFtmeTV8Q70wWAGEVvg7z85tOGIdjTvYEDA8fJLEtANCohwIWsR5FvQ13fc_3JDzOQXsHjtxrwPHSyfWxRchrwVMwwyrj5Q4Sd1f5gdSW4SgwmaCTLEPI5Bh17vamAzWyy5EXlm6f7EOazvO0HYfU8Og8R0LGXa0LL32nitTbqFJieItNVuDskQHmTLS_B7e3AcSukC7ZrE_-k0W3Lf9Sl3Bha1CgwsSOXSLytWolPze3HK-ybjVnU_RYswTwCmZJRmusuFOULwLHtUVeOujlS0jyZX20qII9UHbSL4njg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggUhqgQRiicjI3Zk2QaygVB_W-3WsZxxE7HTqP20lNFV2QWMkrO1BFc8y3DOMGGNscz5krIzntuT6QBUeECuzt3WgZE0KWcgrT296izig-DgbX4226ginLf-5eovsXhKJ5IG29af-bvfylvdfN7nHcgAxjKgKsM-FQi8u8E3Cjma4y5BwVQgQqOauRy-mYOGFYV0EBHRfI4oK0aLKJLxOlloaCiC_3CX1J47S07ZShji11jCkIpzJSzcLbwlq0LzVOa_A6NCyj-ej93MQVrMnq-N-a6KiSYCfIldNSiij5zIUMGibon7Uu_TnLSSNC8BrNYXEk_apMm878KSp3pV4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eV5NPpEScdR-c4cfqKSfYlXI5yAUzqJu3hftLX9S-B9vM5GSjQah_RldHK7SM37OwzKiGdCbRXwnleVCXEjHHCugGrRVGBb_GxiWs7oWdImnrYG3Wj0DYH30ez9_N6uTRPLwexQntEf-SwJbD9jOaUQQP7RSOWripYXVp6UZMas8tOi0jn3f8BNf_ZdyrYWbSpx21UDhA-B8ET5yuDETppxnDfl4kERxXrC0-DQRTIcong7NziyoKMpbAYED_SCkTAnT-xpiGH6hw54d2Wpk8MAy8lq47q_LboMZh8uQ0jjqFSIYf6kQVDXQE9PgIi_TgzFL4Lhz2FLiE9Y79WxRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUky4J4ji1PpCErQlIaKxpsTQb23K5Jxi90j0NizGmZt0MQKPFa6DlPi3IOlbfPx9c3wY9tiL_mtvP-rkxzF12Wv1_rtp5eGtvb68Tam_MquK1QaTk1qdOsbJNJ_l7LzvMl7slCe7pvHCpSsId9OzZIah-rYwE7ztmW338TfUg-bNGV88JAh_pH3p3rBHDwKRoE0tRJYHWNuqga1CYXN4yHZaFvt6naIcmLbCPDiAmthDVVa-cHBfujq9Zxry4V6OgIrX4NNeXEqDKisPisyEaTdmFgD9ePCJy7s1quvTDuCpLv5VMS5wcIYoV6wJpW6xQGe9Jg0zX7_Lw_5B7o6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlQzozIAkCsmVO-eDde9L4EB5-_k2uD-WSlScuVCAPSDG_w8v36oZi_E_7-q-zIW4eC8CybZ5dlzAVw6ERkM51tV7KjMEBMhrweKv-3xF01dfh5UiA8s-GPjKhV7QQ8qse1IIila7Zkmj7U0MAfcAqGmpdYY3HTNZEUPbOyqyKI3g9Xv_ipi0ptKlbe0Eim_mkTzuADntmFYl6fdig29fXRlU8jKbazpu95yop1pesWFuBCDqyhiCw0gOpGdZfggfyJvnlp1ClY5nmM0fnxv-JcS077Ee0UXvxyh9RJUPM028PDBl9xhNjr-ZKEuvJHTZW5QgpW5U--hdg9xGMMcQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=eZnhts7COyab1q-dgQQw92eiHxhKNGRFEFcKhulP1Rm8-fKqtay2yKUXyLvDfkaJTSA3_WsEFqnbCiRPyPKQddI25wMh1DxCrjjIZf8VpXWSIEj9Xxsd8PffFQxB9PL21GGoLJOr7FBjlhvRku7zkP7uPbS_rb_yXYsdtGGGCDblJskkvuzyKaNlAMGuHul19dOUuFe3S6YHmSxpWLN8DjkIBZZK2fsd9NgfnTpmg22j3zSEzXzW_rbRV-HlVuro7Q6pIp0q4B25qk6rePZEpN8B5UVZk2Brx5Hm22Eg2Le8yfXS4PR15mJMRcketrAX12Sweopc6XF74QvY9aCwMDRJBlDuLReUv7CWOVI6Qzpb0jJqu6foijQNQkPvh9S-qR9_V0zSeRo6WxeoYBys2c1VYcdyK4PMGtQUpVU3fEn7BKfV0kM-evggrSkBoPkRDVHAROdpLhkhxo4tYMDN9UkE6Cb_YGJyBCt5gm3NkA05hz9UrBP9itT3WdpHNp0pgwvWFQJ9HyTo6yWR0n1i1DQ0Kn_SYyCiBxlzxlaqfhVptu-488y0LjHn8GGpV_zcwLpb5l9nz2wGEqHB-nrPqSI9HRfeAKEC7lMoQ1L9uDZKgHTk4b6-l_v3K4DGRyRHrSAjq4kQIhnhSSvcxOWUjx_rNvriRVYNJ1Nt4orVLYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=eZnhts7COyab1q-dgQQw92eiHxhKNGRFEFcKhulP1Rm8-fKqtay2yKUXyLvDfkaJTSA3_WsEFqnbCiRPyPKQddI25wMh1DxCrjjIZf8VpXWSIEj9Xxsd8PffFQxB9PL21GGoLJOr7FBjlhvRku7zkP7uPbS_rb_yXYsdtGGGCDblJskkvuzyKaNlAMGuHul19dOUuFe3S6YHmSxpWLN8DjkIBZZK2fsd9NgfnTpmg22j3zSEzXzW_rbRV-HlVuro7Q6pIp0q4B25qk6rePZEpN8B5UVZk2Brx5Hm22Eg2Le8yfXS4PR15mJMRcketrAX12Sweopc6XF74QvY9aCwMDRJBlDuLReUv7CWOVI6Qzpb0jJqu6foijQNQkPvh9S-qR9_V0zSeRo6WxeoYBys2c1VYcdyK4PMGtQUpVU3fEn7BKfV0kM-evggrSkBoPkRDVHAROdpLhkhxo4tYMDN9UkE6Cb_YGJyBCt5gm3NkA05hz9UrBP9itT3WdpHNp0pgwvWFQJ9HyTo6yWR0n1i1DQ0Kn_SYyCiBxlzxlaqfhVptu-488y0LjHn8GGpV_zcwLpb5l9nz2wGEqHB-nrPqSI9HRfeAKEC7lMoQ1L9uDZKgHTk4b6-l_v3K4DGRyRHrSAjq4kQIhnhSSvcxOWUjx_rNvriRVYNJ1Nt4orVLYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=SN69glNgMiyovgPHoSNJdpcjPmP10cIFwDFjo7t3tDUamYLHgDoftzmCkKOgEnwOwztD9fLMUjlWRCGh417bt8z1GRBZ3s7hnKf4BUqflP29dJaL8OwuHBz28K7QeDLfNF-N6aRWRYq0T67Ycm20sXC_luyyLmgYWwuYEQiMSwAd5ninNOdQ6S7PJGhGjsW4taLDUMv9nHRozBTnbeDU5YRIGElXRT_oP6ctbN2W49SfWC63wMH1RzZgC2lU-ORZXGE0EmjovLZNjDen4K_EJ55NpK7UOM73V7o1-_04gm918tN6O3_duZInmaYvaUyNoBdlT9BTIKT3fgr0Wciirw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=SN69glNgMiyovgPHoSNJdpcjPmP10cIFwDFjo7t3tDUamYLHgDoftzmCkKOgEnwOwztD9fLMUjlWRCGh417bt8z1GRBZ3s7hnKf4BUqflP29dJaL8OwuHBz28K7QeDLfNF-N6aRWRYq0T67Ycm20sXC_luyyLmgYWwuYEQiMSwAd5ninNOdQ6S7PJGhGjsW4taLDUMv9nHRozBTnbeDU5YRIGElXRT_oP6ctbN2W49SfWC63wMH1RzZgC2lU-ORZXGE0EmjovLZNjDen4K_EJ55NpK7UOM73V7o1-_04gm918tN6O3_duZInmaYvaUyNoBdlT9BTIKT3fgr0Wciirw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzERZr1TUm3k98GGyjPBc23zdgd4CkLjnsMJ0p4ZMR-84KAYShGF6Y2ppmhaZNEQIOOVdCHlxSu1Cnl5jrC-yX2wDgfKvbN7vxeMyI1OdRzEj0DYxgIFmd8P0aFQSrvwnJ1_tO5m0gmyTYZA0Jn-D14OrBcHjDjeGSmBk9zmAfHeqeeNj1dDhmdu9fOTpys5tmSE_xpbiamYiFb66Zvg6uSGHyXFMZcVY8VUSIt_Zsx9A3UQpqx758-LcdoBXM9tsqh7RJriHVUbXUdyVMM8oeR6TlanAknwST_ISMcr7PW8wd_v5_n59nUoTrZX9OrbOejNg9MVB1cQAgDppz52yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGNwS_QdQH9xoryMD3abLQYU_HhvFYodq6_PdYAfD4TjpCljMWrSjYlssZ4T2XF6Y_CIs6IGu78cyw6ZwYGiG5vAN9T18OyCzj0OHMPDpFUtlyowlOIIUd-wdBqKFRNdzvL_r8mX_s-afOUw-IS2nrhZ_k96tVdX_OxCblmnA_VuGcHGEtMfEbpxcubNmH7ma4FmKiUxoaYYotywEfI3RiOrhE3ihuqOzB7y47g4vlBmxYeT0Ya9C0t81yewCLGclu3uHVulRdWIgFKsgMF3KLjgJMMpry7_rmge9Lbp72LQhpvs5YizbQtvbrzFuSmjwqHeUEcMDxCUv_Yx_S3C3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1OqLxU8HU_WwKAs_Ota28RD2jEGkxzip5mCD58MJ8r32Vgv78wgs-BBKsnw4GudE5_oz3oSNyzNZlJErWfstwkhb_j4t0AkF5HNHPjFTxTo_eTlfM2wTbiKfpQEIJH9y2IwudB-Q1Nep7pdo8JM17dfh7jZ-cGC0RDm9JlaTQXjxd5_QFcYYmVkm0kiDTB2gnw2v_Vj6XFzTctmKLHNM6WknQgoduGSEjZn1D0hNuw2yQ4py5mDZgi4BRYRo7OYy14COdZRwGO5PBacNcsPJsSSqyy_9ylzWZnbySPvzR136CDyL8IFH1zUnaXPdBv-AZpGaMnCfE_HMlRrCSDonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q30m35lO9swQbIJ0FZoKPvzkRh1p9fenIonP9unX9nbEbSc21VYv_RaaC3H9eCTYsBEgBhUWU_irPsFv6GYV_G_0c7SPPSLfsn7VZ1waTht7kuEOyvDeLs7HNKL3OPbUmHqcWGEcmKQw05gR5ft0UmQSFReX8RYYFgo0HujkUy2huepFVhibEWgBoQx6GFctcI5WT3y0tUmIWD3OskQi7ERtS0CzPi9zItlwB3djgxf2Vae4Mj2_OhhmI0MwFCIwRtRRMquc-ozhW-RC8ve1_0DxveEIV0qTP1TWA6AijE0rUrKAkfwwijptQUG-RRx-4cGOaRXphAyhDGzvC-kteA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg4ljcN205Qz307P34xjfay-AoMFSW-KZXi-olTWx692LGWmxxiOExjN0bsmZVSItIea_r2Y8OWhu1J7JslIOYK4gJjmncKZ9ggypiIMuUCMWaM1-1Vp18NrTrTCVhxbUO2GAamGsdLOffQnCR14_umdd64mFPJN8KExRrUMluCaWZqJ4vja4C5y12INOnKYSk-AUqgH18Nu_kCkgFJt2-riDFiV8-WIcHzJ3XCTSiWHN03f9EqfVVVsf31oFFyMPOM6G4c8P1rbgkt7ppTYkXxYvH5ZMG3RRSd0PmI9iWmC92hHg7_Wd5h-xW_mFraQyRWQT71DR2-la8T_QcrP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEe0nREo7OR8NgSZ8E3pbRbMF978v8Bt3Bs9IAvQRDq4ZJ7xOA3277_xqyBGhCxN5q5M3nMPoBcMG38P0APya-U7B-kKGcYMYTwOSrVjfDE_mMYIWxnevtQR4dRQpE7dHdggmPMtkvFICvMvHXS-NUlT9kTID91fGsvu6YrI_YItDJppGcZRDr4_VpfVa9hS8oZhvedNmyAZt0mfHek2Lio6WVdp4UBeqIKQRpFxI5LAwlN14myOjvnI5U2ED-5I07oU0O-vF3vmTVWnUHwqpJv11xjDDulQCSEAS4Cb-PDVKjekmRczS0uReIUL3thb-8x9eN7l5XaRxDSGSG9cxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5wIdQKLGZ7Zy37ih-X_r10hQRyyx-JSFMQ_-WsCzSm9vPDpJVP7HbFN9nnwj8BTFtRCBn0LIWuMSfuWzHYAysteEbowANqnyTK3c0M3bJ4efucUzrLk8WHf6vA62ha3wdrY6RaQlxIdVDJZLc40PXG0-PaRQa_7mZ5HaX1c1QJH_qQdjXdjwfIKMS_SEONjS0BeNRobaZNg1hLpvP2LAhXVSxhQDv0NJ1dt-HcNPkunO2dBHMMrHQ01qp6Zv5Fq68vIHlRrk1MUWo0n-PoE_t62P8zEv4qw3Dn6yTYbbsK5b1m6rjgh-bKfQ8sTPxuvVIUIRnz_Be8vZCJtrAKnzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=NIvrhH9_ws7icNQ4FYDLqGYvW2ZFq8HH-AMLA1eV_MYDGHXMOE6SnYNNVQPf_7zJpIrkEqEizfZ7gYWnxcotqGWWHVix3usjEcTAmNQw6sFjH567wFevVMvg3KCbkP_egMRFRiezYzCrLhuR67mSyxvCUzLMpTCmWPOr-DXOcbnFhBfiz5VSJdqAbxXX0rooYw6-xALJix4jP9nWZUydAxeH5TjH6bUupMd5Esm4X2vY-X0B4rmSvE6MXKgKL0eMP9jhiQCu0DkT3kY2H1Y0tyamblbO9JzQA8qPU1eiWjA8c_bTQCv-oAzxkSPsWvnYJxEQyCQ3dCxkGZc-NOYCbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=NIvrhH9_ws7icNQ4FYDLqGYvW2ZFq8HH-AMLA1eV_MYDGHXMOE6SnYNNVQPf_7zJpIrkEqEizfZ7gYWnxcotqGWWHVix3usjEcTAmNQw6sFjH567wFevVMvg3KCbkP_egMRFRiezYzCrLhuR67mSyxvCUzLMpTCmWPOr-DXOcbnFhBfiz5VSJdqAbxXX0rooYw6-xALJix4jP9nWZUydAxeH5TjH6bUupMd5Esm4X2vY-X0B4rmSvE6MXKgKL0eMP9jhiQCu0DkT3kY2H1Y0tyamblbO9JzQA8qPU1eiWjA8c_bTQCv-oAzxkSPsWvnYJxEQyCQ3dCxkGZc-NOYCbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwNSKfLf4HuGxLgO0mJ584gJxFUJ9enRsQEihHFErEZ35rPqbngi57QS5YpbPNQOpG7wbsjfBeizzqqXkcJItTMnW9LpIYDRxnWrq3ahZ5yqAXuDzpthSMMxwJZOG14WPG3Gm7scBBSzbiwtSrho3E9KveKR6moZY68hZ-ZvictQY77d-hVwXN_fLtYqmsqHrZ3eKN1Vo3dXofMHt9oTXOQMnYbCcF3JrE42TDnNa-Vf65amUALXJk9dbht54WSZvQcxyOGyvFRg6JvFfKa05vBxiLSwyGNEBNNauT5oZiyN_l0vir_OLKQpQjJXBqvXVnclNcFvYe3QOGaFC_TGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Cq13tyt08eK30r4aTMTrLD-3wCgwLKJnepT3Sonv8-fIntIeGtRr1cn8r_b9rxDh-v830FD05_roCvlDGCTxHgR6ChDzgDfJEVVbryI3GplF36b1AVH6dd94Lxy5IH0fFlApDXAl4UUlbs0IYgjw0oiOMjpwji22FHnOCIlmJq6K8lojhpMuoHKVyLwYGvgwcoI7sJVaD8DGjF-VIiHqamKXSOeXamxp-ZWYLIyQKLop9nM4kaSKVhwbU42dpgci_f-vexWSj22ozPX0oAXjRIGXx5dJnv5x93kgdn1I0qsF6u4nPFRRh6NPBoVpm-avwPKIebOhYdgiFWu_ZNPPEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Cq13tyt08eK30r4aTMTrLD-3wCgwLKJnepT3Sonv8-fIntIeGtRr1cn8r_b9rxDh-v830FD05_roCvlDGCTxHgR6ChDzgDfJEVVbryI3GplF36b1AVH6dd94Lxy5IH0fFlApDXAl4UUlbs0IYgjw0oiOMjpwji22FHnOCIlmJq6K8lojhpMuoHKVyLwYGvgwcoI7sJVaD8DGjF-VIiHqamKXSOeXamxp-ZWYLIyQKLop9nM4kaSKVhwbU42dpgci_f-vexWSj22ozPX0oAXjRIGXx5dJnv5x93kgdn1I0qsF6u4nPFRRh6NPBoVpm-avwPKIebOhYdgiFWu_ZNPPEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wixz4AEYnGNpolYQ6-7I0MMFh9wrc_PshHMuEMLoUbt_Arb9zZofHDZ6dsy1GEgFN7CR1FEdMTko-JYb5HR5YwYiOKKZmPWYw74q7lZlAaR313ULzKG6vZSxbFLqhmIDilZSHDzYMP-EOMjxkv2Vo4XdchSFlfiRYUlkRhpTzCloHurwJGGFbo0hssd0x17rzPL0ojUxgI0-1fAQwQsI2I-tZW4sfAPKNEAkAI8rgBw8FrrMvvMKCq183U3joHwy3uX1t85K9mZOo9-q_7sdwd8vM2JYnMG3EdUEYkxjs3SigUs5HvnTZ1AKBwL3NjXqxJ375mtP1P9D3ErBUliqcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGH6x7ywzoGgQZ-4s6vQ9AjM99LvNkcwLuwZtikNVqiFf-EzUEaiAtPX9QCvQTz_I7opHAuslpI7f0cb8BAaDkb_j36VK2Tbt9AOfx6FDtrBb3Xn4dgBCJ2HD2ZtKIPyt231iszL5dl2PvZ9wXUuUUMNNgggo87d_hLFbiRiDpBE0OqEZLhy-xNLJDOxLa3ShsT0no9xmUF8EOitZdmMffSrjrdFvTlmC63v8KTJyRA4fAY23SX01StEVU1-nKsZy3Usob7qyUlt-FWWvnsfScav9GjBrzZH2JdVl79wT_XKcbJdwJUp6iDifCgH3j5yGpppFZIN8e3zq_j2MMoP3izM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGH6x7ywzoGgQZ-4s6vQ9AjM99LvNkcwLuwZtikNVqiFf-EzUEaiAtPX9QCvQTz_I7opHAuslpI7f0cb8BAaDkb_j36VK2Tbt9AOfx6FDtrBb3Xn4dgBCJ2HD2ZtKIPyt231iszL5dl2PvZ9wXUuUUMNNgggo87d_hLFbiRiDpBE0OqEZLhy-xNLJDOxLa3ShsT0no9xmUF8EOitZdmMffSrjrdFvTlmC63v8KTJyRA4fAY23SX01StEVU1-nKsZy3Usob7qyUlt-FWWvnsfScav9GjBrzZH2JdVl79wT_XKcbJdwJUp6iDifCgH3j5yGpppFZIN8e3zq_j2MMoP3izM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=gy-kSZSBROtqjrM96G8Eiq0p2nBdlOPKZUn2kXInDQofEnDobTN70x4fePmNhv_rhT3eKSVYhdn9ZWZNfKRK0XIUO7KvpNgnNifWalgxxuDCWTVSancv473qOGu6tUULWj7uUMBtP9cYqRv-QDrvQIbvAhOV-JuLNq6PNlQZyf0VzuPdaJEzllxHK3h5SnBRIo9N9mdd6NQatlmjUK43qM7tzPR2it75sf8tdck6LuWhYwr2KL1SuyC1Dn3yH2s15MmE5scie7glf8Arld3R8eXOIDxlQLfg7VT4VoIM5D-QNGxjkLQoUHZc9izAGEDPC7RSLtSzQgumb1CFXVm0pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=gy-kSZSBROtqjrM96G8Eiq0p2nBdlOPKZUn2kXInDQofEnDobTN70x4fePmNhv_rhT3eKSVYhdn9ZWZNfKRK0XIUO7KvpNgnNifWalgxxuDCWTVSancv473qOGu6tUULWj7uUMBtP9cYqRv-QDrvQIbvAhOV-JuLNq6PNlQZyf0VzuPdaJEzllxHK3h5SnBRIo9N9mdd6NQatlmjUK43qM7tzPR2it75sf8tdck6LuWhYwr2KL1SuyC1Dn3yH2s15MmE5scie7glf8Arld3R8eXOIDxlQLfg7VT4VoIM5D-QNGxjkLQoUHZc9izAGEDPC7RSLtSzQgumb1CFXVm0pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BX2lywfABDeBJBK6W4pBbPevP42tvL-xQQt9SPklBJz2m_XI4bRhF_3BBntfnITj57bSHsGQB-kUhjyweOgN4aOWSMl-MiKIu7OEaiphsCbhUHefhEJ5YL0TdhBiZ71xu7vXlskXolsJb4nZWPai6JqYPBig00vyx6XlIdcbgr15eqgh21MOXe_R9-03AN3P3Y0rqSYUstMXWUjcsPNbmA-jrnhsuTDthN-nvoAvTVey0KQ2IO4OdfStDeFULzsEASpaObBaX1Fxh44QvhfaJKSMcBckMG9FZfMSz_DRTPLtC1hpCaHLwpp5TBuRxOYbPkpRtU87nFy5naD9C3E3DPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BX2lywfABDeBJBK6W4pBbPevP42tvL-xQQt9SPklBJz2m_XI4bRhF_3BBntfnITj57bSHsGQB-kUhjyweOgN4aOWSMl-MiKIu7OEaiphsCbhUHefhEJ5YL0TdhBiZ71xu7vXlskXolsJb4nZWPai6JqYPBig00vyx6XlIdcbgr15eqgh21MOXe_R9-03AN3P3Y0rqSYUstMXWUjcsPNbmA-jrnhsuTDthN-nvoAvTVey0KQ2IO4OdfStDeFULzsEASpaObBaX1Fxh44QvhfaJKSMcBckMG9FZfMSz_DRTPLtC1hpCaHLwpp5TBuRxOYbPkpRtU87nFy5naD9C3E3DPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HERB-965MFCH7VYfLLEVbLC_qTJbG7YTO9NlCsB354JYmjhlYwrK_KAh83OHyBQfGU-3v8KmDTlR3JAKcgaTULUBRN_ZS3BE3XoZ_s_7iLEooTUl225Y8PaiClopP0AJMV1bnXQXPgFWhrWXQ2F0eBI3C6EEr3Z78LyWeT8x_ELEGp_1g8uLeTfwyveFpS_NrWcANR9px2fhwUl_-4JHYgT2-6qfYyBgXSRrOe2LHcqmgnWLT-t0DbkETj-hWRrPI9Sk-VOfksU9OnTytTlvM92q2bkafA_SKcAr0906oYCGmMWhZz08u9IUmplshFXHSRmoPZpjfh7ILPezWDkDKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBMX6JA5NhWk0vwCSRKhVZ0uyoR5vq-4-J1W6mKh41nFMWBdDJYDgPKXqQGHnol_tu3JQeK0Key1XA-Jz7_A6DjobT2pPI2CSoQWqsElDbhiuLf07zVoallC4BJzwQ8-GocoW7A1sugSjSxhB2F_WZ9wpEJT2l9DgLTtQ1kPsRaXZWc6liXdtEwbuQy9qt_fwn03N6OkA_b_ApWl0POrSlW_uL7DRXDOxBKBd_hgPr1uX6u7PnqaKM-IhhqtPqYuhzWSz2fIBCFHh82R2p8zGYXdILBuQgYoq1CTyTC8sUtIkrNgmxwY6lfJzXhPWgBRtWWv9ZIIQiB9nNHGQo14YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICVOlYbl2G9tO0ARXETJKHq0PYRbJ2Z_wpOXej--hJUVNjSJttWq8GBGy3the-knXtHqmJtyR0ICguMpjalmYyALzqobqh_8YmHkZX7TlgrNN6aT9BS7uog_Snrlaw8XOqE-SSZAkwOIqBQe3oA3J6_ZStgp4xRKgDpczEWdtNOY4t9m7Fmmp8BTObkRyJmLCUUI9wrkjYbl4BaSXyl6_PrlFQ8Vso2Oy-TzDN-NdK6JJnXGUzSVH89hW0xOZsQ4wXvEetyIu5JUutB2ocyujigUJjXey8mbV69vvQ7E78b6uG7EhLPStt_cjWb4D_-3kzm7QQX4wbqJyvFSTN_lWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALOTnR0YsrlyBkMdwA5hXSeTMpu8LR8LjpxnX2RnNiSKTbhnApbzvlKih2gSMYKvR02USVsEbGQ7Gl_H74Vyrn4QO6hCI7dvlp8n3VcEUMyHFNM3d1iX6iWquwhp-7760yGi0aCQS8qqrcbiap6m3-w59LgSdC89f7GJDbu3tHozvXTzN3K3xiX3ZVBZ1xoa7RdKI3j6JQ62CloZfMe7EI20AYRMTiTCrikqYMwlGlFVdxj1uCnlUXIk7OVfVR5ZyM9-vbjsrz0BydMIXqjqzhVQKhbilaZEPH1JpDOMssl3K4fGwHbTLvoPd9dy4Z-nvfhqG5GfbAC0c8M4S468mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHGSJ9sXAgaDb1MTqRj2Z6fi-yQXBz05qn7NnkZhM0VugPiNAn2KB-4INjn7JL1SUQ5einpKQTG5l8q5RQDJXLKnNPPxT-kTIPAom2hj8voM8VuYT2PKEI6lJF0NHjdBqxu0YXjvM62vUhCAyJWd3ywWeGx4zGIVZlBI6KCL_H1YcgBKdumY1J7QxCTQ33VDcdVY3pOwEkWmFanYKqop7F7YIKMkcLFpoVU7KPObzlokxsmLVPgrt6RR71iV62pT5zK6VEWJhhYFPYMDCAmCs7TDzHPR-NpVB2N4mp_NbxZXXTzFe8f50OagBnp7w4p5zSWdrYuv_pWVF4fpZB6mQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNnEHF81rHlDKqz45EnKpFitosGQyloiwGqWSP5XfiFDZCSb0aRg6kYFsyj8pDrp3j8n7qvROTqZZiNb2p5Q5M0BD7B-ZKedzUqPwWrpJkCeJU6en1ROmMUHLyIQkukxUsrB8F-OU2lOJSDpt1cGvjsBEEIUMPiSEpxMm83ckZQNia4d8CzVzSaTHZjmN7uOdhkFk7m3W85grn6gUUUshUpmOXTEzN2Ih7DvoPVMTY1r0WsdqLrkOvXEJxPLN4FKjrVW4P3rxuAlTnnPnFPj4SHiY7PMAeTy8elH9MhXagMSlTE3zk7dloV28pbVZQESXbHLkulz62yA9LNoRG6whQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
