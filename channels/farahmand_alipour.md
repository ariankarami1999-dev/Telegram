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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 22:30:52</div>
<hr>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5E1UvQisOUYNvRIBdOWx-bY3uG05FRSG-1gr3f2qY3oNGAiiIv2GUsfaCeCUVPwrhKFukgNo_CqWHm42-opva1tFSKkfTeRpdqHECndLHEEMJt-oHbJJpBy4HryLEee007nSj-xlxGShSLG0qTGx2VmvD2AHuB1RmL-015pVBw66W_pGkLz-eEBBhqWrEMoGU9SOGrKhWRzl_AFtOvQjI5DuRRQOMMgKAzSSSPO4PWulAJR6DuKHFfwtvJZz-sioJ17H7-CeiTyznVfOEOn-eDON1cY1BbsZ2XtNzV5iu9yFSunEu6Itqj_4Z5UUIOnBzCruoQFdUnNuFCxtN-s1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov-5teW3tHTvsvSbgMdLICYXYlU_sDGIu9OuiTSl0594zrfs9gRoJQR8S28V2CiP_XCjD7Zzp5uItinMqAUIbUIRvVFn3zxxaqYh9Km-0nk74uSUdeQvuMYluMHfHS7WfmU5Mq1R_o1vTjHKfD6MlZEq2Yf9KVRt4d2gzoWcCctXxlvrZ83-13fvHD4NvwcgSfJHIpLOCqzOAdqDTCE-6frq1o_rpZ_dr6FZtGyKaUvR4uN5aL7iKlIR-aOJwWaAcP_ZJcq4l0tyEkcUu7cd1nNA3Bm7_vFPEyFbPsYQr_SdVeOSm92Zw0-QEekuDDdOwCr60iw-tbsukbzrBFNmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHVVCza4-k7lMKxM3gRJStW0mSmbHx1HOC_kqRItxfPQPZo3RqgLfbxvjky93wErqiutSbOoRDVDgJO6-5Gt5GeEQYp3ZpC8LbmHHVvogV5fTJ8tjv9WUtzfZpz5NJscTMxYul7zKui-uhcGtGwcbJz9kr1kP6yA61rGmmeIOf2BDf3B7TQdUT7ccFphzbXnhtP5luogZEm_0Gi7-eRD7KumLBDmDBfFnXn0yVHUWnWFFsbkQWbKqce98C8p4SF3LVslyiNzTK7TUUb1kdRXw9U_E3m1dmBOkEfxlEWe_yZkhLuLgJrZdcC01kX5yYjphMbJYFfm6UDxnofukWHSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=KFr_RvQ_lfSvRrwCsy33D5v5L8qLWh8fD1b6jCXXmJZyi1ojn_fbuXYG2sYrqN-hvhdYD72J19SR4_a_b6mKjxHZwi8JsyuajbvX3Ks-wO871VJlslmJYxVlGHVtoSjvjy01JCeDoHpdj9ErwLwDgMQcxAsGaNUMHtU5SffYtkoKLlgBx-p7UFJ9JducQHoR6ddOWW8dQtyIPKkhpdFoy3feYafDFZkGnZP2e_qlyMCJeKXN2YDzzYedcMUFYOHmq4oOvtfTDbrTJwOXrVZT3xcspT49zf1-ZSDFCEqXs7k1LteqsfUHa1jODNb2qBOStjnXKTQvjyzoJmvRFSni_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=KFr_RvQ_lfSvRrwCsy33D5v5L8qLWh8fD1b6jCXXmJZyi1ojn_fbuXYG2sYrqN-hvhdYD72J19SR4_a_b6mKjxHZwi8JsyuajbvX3Ks-wO871VJlslmJYxVlGHVtoSjvjy01JCeDoHpdj9ErwLwDgMQcxAsGaNUMHtU5SffYtkoKLlgBx-p7UFJ9JducQHoR6ddOWW8dQtyIPKkhpdFoy3feYafDFZkGnZP2e_qlyMCJeKXN2YDzzYedcMUFYOHmq4oOvtfTDbrTJwOXrVZT3xcspT49zf1-ZSDFCEqXs7k1LteqsfUHa1jODNb2qBOStjnXKTQvjyzoJmvRFSni_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCgUt_qdKOzEwfnChLmAwdMcVnVxbr0vnnUZ4_fjEuuc7KieRrF3SrrENxb2bQPx73SJpMgHXz39ZlDwQZg3sctjRmVLd1Npv4Toe4mFXfOfKqYTLvR5TTI7PcqnavafrfILV67NsQw2AfCOLdtZXxsJJAShk6SG7uP8nt8ssxlzvFwTRdvx7BT62P_B8r3gdRUxCwry49T0fCFnwYvbdMjq9jj9URSKQBiQDQ1yhq6r3FUYp458xncQH9LRNDxiAAfGJ_zMBRYRgTnIQIZxdyLTYwsFgkFODuLPwxP4J4LQOPULGDRYvKlGsld8Be7E1tkqgufucBADMjwk-Yj9-bpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCgUt_qdKOzEwfnChLmAwdMcVnVxbr0vnnUZ4_fjEuuc7KieRrF3SrrENxb2bQPx73SJpMgHXz39ZlDwQZg3sctjRmVLd1Npv4Toe4mFXfOfKqYTLvR5TTI7PcqnavafrfILV67NsQw2AfCOLdtZXxsJJAShk6SG7uP8nt8ssxlzvFwTRdvx7BT62P_B8r3gdRUxCwry49T0fCFnwYvbdMjq9jj9URSKQBiQDQ1yhq6r3FUYp458xncQH9LRNDxiAAfGJ_zMBRYRgTnIQIZxdyLTYwsFgkFODuLPwxP4J4LQOPULGDRYvKlGsld8Be7E1tkqgufucBADMjwk-Yj9-bpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4e6B8cLTHOFZLC_QYWCJylwSJy9W0ogC1kkRdY6btQuH9H8CxCgaa_B10O5ewXYUxmKpJiOTN0Ok1jOwJzi0kgotaQ_2jf9b_Y5lklIwH1mMX9jIZqCs-epIINGw6Yx4PIe39KvGuERRpop0rMJzGtI_xUPz0gFzFQcBAm60EllibNy4qfoms-3jmaAXpr3mODgfU-TkPoqkbeC_wKoaxzAUUJpquRW9VB3eEMGor6OxrZmO2GWGGsilZJVFP8KpTQ60nU37QY7iTkzNHw0mzJ925GZBZ8_gLXhUxvi0Rb0kUsZY6BSvIAEyxdJzyaFGbTkYYq8rukWUxmT8i05hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3cy1W2TbhAEaNqko-LkofOvGARhOPamsqF0vCHGyMTA7VOKKvkblmGFd3Z1Cmu624_ja_tAa8n_bbjHmnVTuhNxKTyUxVAacVcYG-q-bRFg662UE5Tria8Te2IEuiazcF5nA2jXoZYHbcMMvjn7bJRAgoWnuSmKAPfMRR3VWB-izE8iOD59w2umFAgheoI3F9cBvPYJO12pwPuaKptJ7YQSh8wu3vjjT20WB8oaFhMleR-Rvz9k8qJK0iV9UMgIccuu8fRJNoDpaVxYVJ8kU5i-VJKdGxh_NlssZVWq_v_rSGXU4LXxVobrRtTg0YWElxLIttczbSrrKRw_7LA-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlt5ohzv1OdqdVm8v4Vv_IX-0JFxqy-G8oYJBsuVCZ0WE2qfU_wROvY65ynPOmrX64NDu1vsIakWGR8vtT5mKHiFbPmRag3vXe7UCO-ac6X3kFZtMEYOSBj3paRx9ihuXJUwNkrzDcQC7bhdWgz1hGE4R1GRCfhLDJMbgLqIUpf7f2sXPUilv_xg2uxob9rxE3JcTndqTsg4-0U2ygixisi3tvIICsmZs1VA5ZV7iD-CYYvf8wrUuw7GQd9_Uy-5W5UAehUBa8MWmeYo45X6O2MYhXRRi1pa2cADIgXL4oopEXqLay4Dun6X1ZHV4RSNCEXLfJZxw1XFgqS1ctKtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUZWzvmoqZKbg2Hg3j632oqFLk1s6y0Ph4BmI1FfCDNkfzW9LmbP-klbRXbThuQIo-0rrfbCQy-UtthBviCQugRULJwGi-14BfB_lV1Es2l9xlVnZUhzX1kqERC8CvSC3odfgRdTuQmtblhV5Ynys_R6qFiv91_duQwwT9VlTb3DVKw_D7A5CEKaBwJ0GLJFWcrrIj419Y79wqvBQet-7L0Lp04luMiYkKZWqMaDdZbK8SRo_SI5fMdekoeQaaK3J1igScpRTcNCS-l-f1HRQ51Kokeco_esn1XkEjFeJoBqc40o3tGeTn61SzBC30Aiw5fodue7avEwIOk5AG6uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2yGdlVEuqBNZcYJmXvZjV0QZNscIJQtqQ7hiqoI5mGWPfJBPdMUr8QAL57h5lM5uzDvDlEUf6ztGCzuoTfPvyneW5Iy88xrqkr8gAyUVASZd905jkuFjIMjrrdEos1x2khwrSr6OWgJGDhjiCN581SBhPRApOv66YWCtDA94WREQsUODGNdgGcwJmf5_Z-l67-zQRq6wDu6EPq1GG69j5NlNUROLYUrbHKjp7gh4G9NytkhS5pKL4y70vYfSlsjOYZZXwy75ApELhEVOuyFnwnGJeLsfEUE-B5SLOXvBS_bki08TIVijZ4XSsA2OiIFxG4RYjThOV8J4KKZMSpZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSR9kCmiMdQGwgwdw52BdE9p58AMB2XEi1L8eYER5ZggYMpOP7hX0W7cvvqQK_bbVLBEQ7DvStIrUJDFtfjRelqsd6SGuG4OlCJ_tHXh6AFKQu-vrqzsAKcPSGwHiawnvI3v-HDftq9OlqabqzoBq09H2hkjAs_P7oGCmErdtAzS63Iz2CzYTQoU0UzRNcnN6ugTPlgSw3L4Kmcv8t1HEdywICmChpjOz181Uq_iOA3JxiHnvGyAFcneL36Aj_EcSTsr6rzADKRHHBpA8Z9apYbAKcRd995P1jsDYRrwRtfLDFWKgUpxcPTZPO9s_mMS01JbTCNCox7GH8LJCDgZOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyWrv8bPvmcaqLKbKPQUqioUc5ri7dInVGG8dm93xlEkNwz7KQIg7s1189fkHmdQqapyv9YWy8GQDZFg_whpVPAUzt2ystn_q7H9saAv13rsS56ifHcibKCAZ5s-K_KhwdgitJSCrRpxbhnqHa53TR8B0ciEdAYYX5Q3Z_FCOF_FbYa0Ae1L5ABt5VQn4Ad6dD8WoqZYYAoUB4mwhqvYByeLllHEnHj3C_Q0eku7a4nrwroc2h9MzASLOJ6O-X-iGmNvUXd799aCa6WwBPEvxEA3Lj2MJ55UiRuVg8QhZmDLIVGyxIGRtrxomzzbQ6DmZ25eFw3Bag9EI-voJYHzeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFv_8PVh4cYgShowLeiHtLzbM2wkPQ7zaxuKKbIYGcx9iNQrzpUQiUyAHCSiEoE2EwYwxsVCrvMaPle-5AYzbdOxfH_ZSz9q47HyF2rouJOAUkV76Yt8RGeWbwjRcaaHL4bVWbFqaAFS-ajo5sK_Dc8jKum-TCsmgyAXq7vmIoEGRHbu3qgtKjCYdsW5Zt8hAazdTU9wQcEjaIOT_L4EnvBMV0NDtSTza0rBMTk-oRN2pJ9PvJEhUYM9Lf0fIKGKYWARTUXzXSvGfYiVsEkkXSGtq0w8ke77DeOlZeygYamdZR8X9LGJYchXk0Q2FrRW1EEd9ywLuzqe_aEIrLChEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=miK-EC_-wXX4RFADNP2-uG73p3mobwi6J8blWaWED15cf8Is6Bkgcu9DK_iB2Ki8G2EpxK0nN4sN3kZVn0agcfJcHSUQSc9Fdw0z8tCkieYmL51cp0krvhaxXTHtEjNgboeibODjzgmLwJYs7fIS3yuSdyRrGzChWT6ubdJd9Ww4VRaWvkh4ihXZc7y425HEP4hb1xhyoxz-mGZuDzM3_2QViO3cSM3u7e2C80GSh13HwzuXo--AETT49DJS4giWqJTTdX3O7PP83KduAfRXg-D6x8F7Sh6-CU5Iy3IQuq6EdO5kPaeNiLv0BpZVHZlkIyws-Zm8q9x1xCmags0B7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=miK-EC_-wXX4RFADNP2-uG73p3mobwi6J8blWaWED15cf8Is6Bkgcu9DK_iB2Ki8G2EpxK0nN4sN3kZVn0agcfJcHSUQSc9Fdw0z8tCkieYmL51cp0krvhaxXTHtEjNgboeibODjzgmLwJYs7fIS3yuSdyRrGzChWT6ubdJd9Ww4VRaWvkh4ihXZc7y425HEP4hb1xhyoxz-mGZuDzM3_2QViO3cSM3u7e2C80GSh13HwzuXo--AETT49DJS4giWqJTTdX3O7PP83KduAfRXg-D6x8F7Sh6-CU5Iy3IQuq6EdO5kPaeNiLv0BpZVHZlkIyws-Zm8q9x1xCmags0B7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=v90f5WYbf-AGP0bnz7EM7Pq3kTCG6rZ79Jw7GGF9dPTJNkjZnB7pokZcBRM9vh_kjcuaqyfbtGM0tb1dWsKy_l8abq7L3g0319haNlSgVS3r7eZkjNVDkD2vrRIu3CIJnx1Z7JPh4JFEdtCi_VseLOWWMfpNSov4E9wUzSbNkIe1NcMQPMccbkcDq8RsjdM-SiM0idMTM7vAcOCe1BqaRCvQDJxi6S_5v7eUMjfg0zGg0FIiuu3uJimpVbIkfglZxTyvHW4UNK_48fyeE6Gw1arg2zAParf4r2wLyWd3G8K_SMUuCv7vScSGBIBs496aYvTFkr2c2nDZLrFIWnmUQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=v90f5WYbf-AGP0bnz7EM7Pq3kTCG6rZ79Jw7GGF9dPTJNkjZnB7pokZcBRM9vh_kjcuaqyfbtGM0tb1dWsKy_l8abq7L3g0319haNlSgVS3r7eZkjNVDkD2vrRIu3CIJnx1Z7JPh4JFEdtCi_VseLOWWMfpNSov4E9wUzSbNkIe1NcMQPMccbkcDq8RsjdM-SiM0idMTM7vAcOCe1BqaRCvQDJxi6S_5v7eUMjfg0zGg0FIiuu3uJimpVbIkfglZxTyvHW4UNK_48fyeE6Gw1arg2zAParf4r2wLyWd3G8K_SMUuCv7vScSGBIBs496aYvTFkr2c2nDZLrFIWnmUQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGADrU6TXa1OOkZik38sv3eJhS3zcYWuptzFEkt5dEFFmrRpRUo2clAagpoFgFDBFND4eDWLuZEhmUQOhnVI0VR5wUaWBoPVzJUV6rsjc5a54IxPtn-ZZE_TMTuIVME5YKmZ-zh2MJO1FFRicgfOuhASbtbO4q_ekX1n3dcV9lBscGzsr78ua6Gsh1veeWYA90ovsY86Zs7tXSubYHX-bxJzPCVJcxBqoMP0tyOALfTsUb2-lTm8vvVIshIP4WFbhL28EYkyq0PuQ6Y0MLxuzYYoQbPlY3PqxUPgu1zhW1FK33nOqhy0D5UkF7KpFE8HKA_nbGhQ5jVhGOc2GJvvPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtx8h1Jwd3FfgHyxR6oJ2vnk2xKeyXMtR0z3VmzXt-rd748s88EXrt3ZSe3XGkZmOPQ8x1dL7ZO5__0XIqyuMpCjYuU6n_HBuvRN7hZGCDZjIB1JcOKLIpAf2778ZYtKD8ZzIXx7uA_R34-N9KJLybx2pgK6KrAkPeyHuBWWIBJJCPrkQMH7xgpMc1LLi1-nq9IomNC7I95TJPYNLhagf7AouVg5L4NMwstfGXUPVKCG8NaSE3YJpNkWMysUl-4le9fZCZyOGva2zfr60xmQFUP18_EudYRURkPSWeHB-vcxLoYhNuq0SlJIBGm-8SYf3zoiEUDrWufy5fQPFKk4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=arriiUzO-82ZyPi8nqKBljXouZJff1NFLiwHtX9oSjUtyiBHfhKXKLeamgpzVG9kCrB3titmeVNlcc9NbHohCSkY78auY-D_7jSLWlE0ipCs49t_9PNxzV3SCyGYtf1n_hLYp0bHuRhZM514EQcBZ1T58AUZyN5nVfk_soPZEy4e5yiZqJU9xqgSoKgXHqvHmTI6L2I_6zwgfwZ_O30lAivltOaixUqunHYIwRtd_Xz1Eqh3eSuYKyAKP6wPQ7-uAKT8N01klW2REZROvayhQoSvvpZr_0ypP0YHc069GWqmK09nMfb2Q8O-KrnwrOJtjSLSmbqG1BIUIS5wYGChX62321ty3CzKCsP96LeTrTDWmkuCK7uiQUlsyQI6U8E9pNRb9jWPGpIJPyl6qCpFO7rC56_BB2zVs31b26mR0KN7Wyn9KHIYSLs-O3gEpTdkTBVDtdSOzMYAIS99u-Ef_gq_klxJASErhYZk37QgVgds6e1xy43OhPM7dm3QfC92ppiTGzxMGfQznWNt_JWwcWQaaAQpk_yv53BM96OAVQRX4Grm1wafJgMNFADsw9ZZN26q4osw673X4dfVJOftOatMnHHIHk3WCleZ8WfGPlDv8iIsN_1tP137fZQEpvcavk0RQZ_WMg6gTgY1i8v1bwYoScd9aYjhzH2uDakz5Es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=arriiUzO-82ZyPi8nqKBljXouZJff1NFLiwHtX9oSjUtyiBHfhKXKLeamgpzVG9kCrB3titmeVNlcc9NbHohCSkY78auY-D_7jSLWlE0ipCs49t_9PNxzV3SCyGYtf1n_hLYp0bHuRhZM514EQcBZ1T58AUZyN5nVfk_soPZEy4e5yiZqJU9xqgSoKgXHqvHmTI6L2I_6zwgfwZ_O30lAivltOaixUqunHYIwRtd_Xz1Eqh3eSuYKyAKP6wPQ7-uAKT8N01klW2REZROvayhQoSvvpZr_0ypP0YHc069GWqmK09nMfb2Q8O-KrnwrOJtjSLSmbqG1BIUIS5wYGChX62321ty3CzKCsP96LeTrTDWmkuCK7uiQUlsyQI6U8E9pNRb9jWPGpIJPyl6qCpFO7rC56_BB2zVs31b26mR0KN7Wyn9KHIYSLs-O3gEpTdkTBVDtdSOzMYAIS99u-Ef_gq_klxJASErhYZk37QgVgds6e1xy43OhPM7dm3QfC92ppiTGzxMGfQznWNt_JWwcWQaaAQpk_yv53BM96OAVQRX4Grm1wafJgMNFADsw9ZZN26q4osw673X4dfVJOftOatMnHHIHk3WCleZ8WfGPlDv8iIsN_1tP137fZQEpvcavk0RQZ_WMg6gTgY1i8v1bwYoScd9aYjhzH2uDakz5Es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ug2yLwbuZrzQD7YCIlqgNRVAc40eqb8IlEDgbkSBZhXGQJfhl_8xPWCg5mu__0Fvf8437vIMH-aZmX1qrcLZ2sxfuO2NUB7xnt3PXsHBclT05FcqYTB7F28gCvJL9SnkskX28rqVSdMKDQTfn4l03zA_WH8ppygEU5ilIt9kDmh4aslEV-ySauwMD_ZC7PHIAMR2PFPfPia3hKYGW7cfGUbT9bDivgx0MCo4GlRSIDei97vXJoa6K9bVw6KCl4g_Wunvd-JkBfbeg4Wb_ycc0HV7FZxgVI46dyC7C--rudTR4rNTAnoMoaFWW98dsC-5Ypo9XvEhhexHlkvoffu_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFOxBhiZchXIki7Tkm-9jDV_KKX4e4_zWdzUZaq7LGqS77gtPodFWwI1oroIUC0Q97eSVKAcVmGZUQesTIaJ_j7tlCur7yIT0YV_WcYPgS5q0AW_eiOwJ8qqBI_tnE9v1P8b3K4iPJbVjMp8ww9fT8N63INIC_AHXen0JftUVu1ZyPTduzl4bGuYz-5g7i0BN-EzBg6QQH6j8BJxL7niQvsi2e_JnjCrtzVFGhez_aFfnLXFQrg6BRKTpSEa_mpSaQ218usQ8Tybaw_4td0rIBtPSTuEz1B77f88PDRI1vKPGtMYDWqCp77V9D0yVIkzMuJnSJ_LmvHfM_vZAmrJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF93svTAmJyBkmPi6xQfEwQObyWjGuB_H6h-N9i9Jnh8tDmc9IvZfHJU4KNkXnjjRtPB_-vsQI0Q6OfYz3ZpnYxsxKons06UFAPuVak4S_WoD9KCoHlfWaj4OMG229s20qLYkGTdN1ViKFMwSMYW6ZP-mvQksE8kMKJrjM7C9dUcqMLdEE55bHlr8DsHwHk7pNJwl4QfqRvNL1J4RyfNZUYYuz7pr1twiA9nAxlMAhMYB_INFVpwn8tngdrQE0r7UfK52z18bzxwZ595iJnz7WcNey_OYXCEuJY4Q3pslcyq4pLi3RzDPuAE5k5Bw269LdZWK8bk3nn_e4uFVfStqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imLUjvdkzodplMG_HWGcAiWYGRXCmpjVjCIcONqd7ZEjc7ICezH0SVCNltjjRigloE9urKrT9OHxPA7TBgwUXO468vbokaWi5YAc_2mHxU4WqL5qV13Hh2I2BYZ_-b9Uzn7FpXNjmk8Be6Mu3FhdMcgWYiRlKiM8ywwWF5Q7QTTBcJS9Pr6jX_NXGD9mdAmRDWhrfdMoc4TprbUYY4ClnIkRUXWQ0vyNk8PUK4lgndbQg4NoPdO8tLWsQVzBhcjVLa6KgDB04wG_Dl92CTKmNDIDef5CfpCQjE7YZ8FBYY-yGDToQEsceOwUI9O2VZ1yr3XIeowAtlwd2ssBAJ8vfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=dJ4eDaqe8jojDChqTrJQMtWGpe_O8Z5Dx-cJ2gBd0_AIOcL2gXQHnjWpVdsW3Z6DCtKCp0qu8AlIDJWM_Z1qAxs-1u-pxJDWKdP_O5XqBluaoEyj_eoicfaPF6f2IGOAP5rv3YDXq5W_cvXQrOpPxQ4EPRmHZkeUrwg-jTjaYLIW9gyImfCn35jWAAippC7owQLklhFWoL3rMq6zRzVYwbUZzYSwQ3yJeXaE16JZs4T-oVLedsLA_OYUKdbPMx7hyXOf9Rl4yE-oMjW1fW5CMs4IHn6_zo9cdFr2YAUJ1O_wItTEhN7LQMqhBbRpSv53xU7Vs2RSu2ay2noSr9QShQmt2AUXofdvsbFN65Co_O_aBYKzlhBG110s1FVutNHu61uBTwnAmAYsuB9g6bXq-Z9XqVlkwKZiEsoNNMgLq68z00Qf4a0e9hDjUDPVOFBiO48UwoptoEHDu4it2rAOF_JuKH71ZCTpKksWfoZyzP8qAPNtP8OH4myzVOJO7OhKJ5i9w_-yaqPNgrSAkoysWF9582WRele6eaANWugFvvMyCDany4nUM3745NQZ6ThhCg22VN-Jn524sZjqIWHg_l0gJ_3LdJrReaCgHXxBHFup_Z_CLyJBJMLdC9ZddXXdkTbOA1klIfKlXi6naOQeLzGY3i-Cq5Cg8dAuqHpknLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=dJ4eDaqe8jojDChqTrJQMtWGpe_O8Z5Dx-cJ2gBd0_AIOcL2gXQHnjWpVdsW3Z6DCtKCp0qu8AlIDJWM_Z1qAxs-1u-pxJDWKdP_O5XqBluaoEyj_eoicfaPF6f2IGOAP5rv3YDXq5W_cvXQrOpPxQ4EPRmHZkeUrwg-jTjaYLIW9gyImfCn35jWAAippC7owQLklhFWoL3rMq6zRzVYwbUZzYSwQ3yJeXaE16JZs4T-oVLedsLA_OYUKdbPMx7hyXOf9Rl4yE-oMjW1fW5CMs4IHn6_zo9cdFr2YAUJ1O_wItTEhN7LQMqhBbRpSv53xU7Vs2RSu2ay2noSr9QShQmt2AUXofdvsbFN65Co_O_aBYKzlhBG110s1FVutNHu61uBTwnAmAYsuB9g6bXq-Z9XqVlkwKZiEsoNNMgLq68z00Qf4a0e9hDjUDPVOFBiO48UwoptoEHDu4it2rAOF_JuKH71ZCTpKksWfoZyzP8qAPNtP8OH4myzVOJO7OhKJ5i9w_-yaqPNgrSAkoysWF9582WRele6eaANWugFvvMyCDany4nUM3745NQZ6ThhCg22VN-Jn524sZjqIWHg_l0gJ_3LdJrReaCgHXxBHFup_Z_CLyJBJMLdC9ZddXXdkTbOA1klIfKlXi6naOQeLzGY3i-Cq5Cg8dAuqHpknLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=mRLt_cRFXnjB519psmE-KiKRhzF-lrVpYIflXW95QfQk-FUPLOvxzH9DukwoPk9VDusUX4KbpvJH832aL7q7Su4KGzp0U_LGe_SKn0roVMTUaYFcgFFonwG13YhGMXVYfpOcr9CYo5xYlF3milKZNpyKce62dRh8V0Qo7OvnQTGcCin_8PKukcNL0mTDBibqsa53jMNfZJDsoHZR7X3CLjYJWg8ghOEEgzj2xXIq4SEcruMRP4oW033gdEPv6dfFypZnMydxtElQfqFmluAAuYTJgV71xqaA8ya6A0cyVB_M1mN3i5wX5gCtsVpqkfJILYESuLwJuMursc8tRQo3eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=mRLt_cRFXnjB519psmE-KiKRhzF-lrVpYIflXW95QfQk-FUPLOvxzH9DukwoPk9VDusUX4KbpvJH832aL7q7Su4KGzp0U_LGe_SKn0roVMTUaYFcgFFonwG13YhGMXVYfpOcr9CYo5xYlF3milKZNpyKce62dRh8V0Qo7OvnQTGcCin_8PKukcNL0mTDBibqsa53jMNfZJDsoHZR7X3CLjYJWg8ghOEEgzj2xXIq4SEcruMRP4oW033gdEPv6dfFypZnMydxtElQfqFmluAAuYTJgV71xqaA8ya6A0cyVB_M1mN3i5wX5gCtsVpqkfJILYESuLwJuMursc8tRQo3eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqbW_Tti-xX12yYb5PyoPKtq8Hp4AosTxr4e_C9R8tFz1Sx9SwSSdP29fV7YbMm8jnaNSvlC5gnM3XgjkOdpJ5liNias3I-xlcaR8hJMvORPkzDObcOqyWLlqbOHIhB-wmUOG1_y4BOnzuneO4mG8BrdleZWNObY3jEUHs_NfaRmghSGdRzxmdqmKVSRo3pFfKMossfUn5NOkS7eguJCvCd85A-Fr10w8SqO5uKw-Tlc-HbakmH_h_ztzEbbyH7Epz_xtn3g9bvWhOu0S0-LL8MnViK__cD2ex0ssgwIjv1tmMlznHMUB_37ZSY_jMUlh_Zr1WHe4wZ4bF8s-Nd18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUhxIAMn94xh1DvwXUJrWHT9Rd5HVWufUq8iTIuq3O9owHwLkFendQoVaQNDc6MkeMIaPwZF1oNhEDv24wBT2wkd6PjYX6dTuJCmF00YU6x37pAA-2rycJle2Qb5l-BSGU91TtU-EHbdFbAY5D7JGEMDlh-d3dMMHtCKvimeLzvxEUOajFKPJgpd4_Afsq477S-rA6cLuJvKqvYaPIxLbyARsQjx6l1rfdi2VnfFQ01UQskp1GLs0ri3llovNOA5qTHfr4iSTXUlBnWgA5NmTJLffmCEdIpAZJUWp-s8xvAFDbkHWVydHp_waPcSEClSiUpCJSeRNn6jNmxF1-eQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZ8QgsPxkinvoVTIhAWpIkFM6pHTVxzL2aHG9HI9A_eqxVeOnHonZDv7ODBAAnkfRs4MtGcKiwzo1Q_c29Qj24Ew2lyPIj5A5uG2gur5X88-qs3qRPevFD8Bl9LApZD7kcCELbHCF2TH4D0CrMafeDNd-svEYAgj1JfAn2wdJ-4NIfpHN9jleNEMeb8N5aJ4246qrH0dLrulTZ6lsqR-BGcPZ5nsRG3ZtvwQ3cxaDThJtMt4sy4hOcTvTkDEjqngpevv4p2BcH3adJErp20E1J_tdi4H__WgNpoUSx70hikrHOx9w8fvIj_NYMx1BXb7X4J8bw6BYnlk79cLqxQ_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jah-xfY79DbqdBs1oumsnt0Fcx6605D_ep1Fy0mYJ8ZVxzqRPFI-6vxR2P3LTlI1pKB8xsGOjH0H5e73-2_Ja6SSBmURLTuQZPghh6TgIe2_sSGv3EAJMfld8ZtYp0AexCVfZx_njQkPHL9sx7Nhvf6jNGCXV0YVJwu9vC-ST2mWt4RRcZ68ESLSL7DOs-K0n1rp-FvXf0Tkp2GkrEcwlFCvIWhJkNZDjlAsEZWuuvSUXf-N7BHnCXIJZn6y6FjyLbr8qDNr0PUdJd0Do4i8mTeFOD6Ke7fGYnwkTxhsLw7zbXRyPHTZKnQyyISBXrEtr6tDPBixrrU8gYU_h6JHgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IovmsxU9Sj-Q0-3g_CFhp6Ow-hKL6TIF6cYjnt2B7K50V5TC2g5GsYcMUaaJ_qOHmm0sjEoiKGuVbnT9UyMt8qrjDK23vP7BdYkPZl_YLpYhGaltyF_RpwjmJJDoLfZJ6-1SkFYXVAYsaPE-4VmNMNO0vrajNdtAT2Q0oxxx9PZNaLEAMcw9ZeqSKnYzVRWhq56OjooqgT3QjsUBM3CzNBVqraenNX7hIOTRU9ehdoLkYh5wYyanf39kuzx3qboCREBHwguWhBvsxQuk4nT92mND7rxm6juZ7FUL61vsNPEh3olfT6xTrIp3_1LoImOvUS1OvpYtah0feWsBq79Xxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9Rlw2qQyoRTiCmdd2hp9dNpszJc5zdJ-40zuJ-4YysRlaqDm4XY39zYc_ngJVXpk0f7QlABsqtPoNeJZhWcyx39CRkz5SKF34EsjSnIEphoQRnAKZH8425Ess4tT0eAAl3M7zou6R9l43bYLEk7sRuNq0EozOjLTqEbiFCmZIKRzVk3d_Ier3dsj0j90H3Td7DB2K2mquBYng6M0oeCTQpMHjAX2WyIxqBQykBiiouCJB3gmFrT7o_zfOzw6WpI97qa4jMn762AmCYATQ5XRe-U5QKr7E2EAwbDfK4WM_y_BcOmOU4OTWWdjo1Kfdg1CzQnTRBBTwT8hQwCFi-uPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K97RhBYtLwzrEFiSw66clYnbFdvnsQjDG_dzdbmtC0IpZyQzhERII92wyl6OHEupdavm1B8VlImsjnshkoZs3eTU9M9ikNRhsrxgMk2tdJJStM0N3oX6IdviAxDXb2-mTmAEBZ7rOlD8sXo-3y8pKx7505IvobGmTWiaqNJ8qsAVmvJlEWLtxXJDMyFrAQka-xrkF4CuskQeIRv6wkgmGIloBvEL6oKQBHANu4daq2RMYDXpyjc3Q3uMrdu-0SV_AG4M8jVQMof6pnZ1y36y2487gIzMqv-toJCEkoEruc07iJv_TEqkMB6284PE75WRdXHUVnQD5p6smrAqoMYV1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=ZePRfMKrYz1nv7HUbibY5oXnTXSXs6Iy_Iq2Q68lAJdfJvirzj5lLYb0EhBojchDh5v_IekwSzbOJBh-5lj6YbsSPpdmxX4RSX59iq3RVoJuk07rBwSlo6stn2TQJzaWRK-BX6V-FKNiU80YD8VGd-ZMm9DHH37F34yVK0TCjoXymLEXSIDps4jbFrvzcOnRdQGXx8lsSn2U7JrzBchurbRoGTRqtwXqst5MGXlftBNDmivdAQSiruOf1iHJ8MlZAFqG1vuV7TgGXynUC4qN2c9tmjpknjeuzDyQh-2NkZcTdsx2VeJbyJ8RFHae-MP9Qx_N3eiJPY90X5oHyeTI9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=ZePRfMKrYz1nv7HUbibY5oXnTXSXs6Iy_Iq2Q68lAJdfJvirzj5lLYb0EhBojchDh5v_IekwSzbOJBh-5lj6YbsSPpdmxX4RSX59iq3RVoJuk07rBwSlo6stn2TQJzaWRK-BX6V-FKNiU80YD8VGd-ZMm9DHH37F34yVK0TCjoXymLEXSIDps4jbFrvzcOnRdQGXx8lsSn2U7JrzBchurbRoGTRqtwXqst5MGXlftBNDmivdAQSiruOf1iHJ8MlZAFqG1vuV7TgGXynUC4qN2c9tmjpknjeuzDyQh-2NkZcTdsx2VeJbyJ8RFHae-MP9Qx_N3eiJPY90X5oHyeTI9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBMVmHOjuPbEqt4J4E3OkbCdrGt2LZ5LzuYkCv2ky8fJtXrSOxR7WROLnkJiW9IzmE5fOGSJZRxJD41GeFIku2LVe9r3H4TjjFX26ijpJLNdZpdD64-b_DZOyddh3RDy3LznAgfgVy3xQFwzVcu_sEkJgLfzsIK35BLdf_TFCBvjo7nYnu63naTBBsU2sY-uG_18SV3qsqdanDqLWbzu6oWLAgiy4PZIrbMQm9zcn2fRC1UqbZALFAznIUh0THir5j4PUQLLe-G60Vf09tHWS2sFQ3sDfrZ1ANXYvZ-u4xVCn-TrrTTW8A-iRvfPAtpDO9P2E6PX6g5IHkm4iGv3LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=rvCw8FsXHfJTmW_bQM9UDb8yFlvY-k4aJc1YO6NpuRA2QNZ-w61KQTfYoAjkfpm8R12imtNKplGuHti-fO0-aYYmeQsusyxaZ9MvCA64mtG3VU-5XOGGDyPxPbzlvvvjPXLCstgAS3DkqPM66rXHrrOKVbdVkSlM8yuTiYHhEuVuM_XyUGqBMFxx_66QLjQADfZvrAEj4Px87HIIOmndYniZVmaIFfQfrNA5b13knSOZ5D9KOCGs-OsQbB-fmNPPvbjHz-USyNuD4brF0gfkUzuNZp4MMykyRv1k8x9KBhJ7woFHaOlxBGW-LnxhjlKDIPoIp3TtiOXVBuI0TC0uAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=rvCw8FsXHfJTmW_bQM9UDb8yFlvY-k4aJc1YO6NpuRA2QNZ-w61KQTfYoAjkfpm8R12imtNKplGuHti-fO0-aYYmeQsusyxaZ9MvCA64mtG3VU-5XOGGDyPxPbzlvvvjPXLCstgAS3DkqPM66rXHrrOKVbdVkSlM8yuTiYHhEuVuM_XyUGqBMFxx_66QLjQADfZvrAEj4Px87HIIOmndYniZVmaIFfQfrNA5b13knSOZ5D9KOCGs-OsQbB-fmNPPvbjHz-USyNuD4brF0gfkUzuNZp4MMykyRv1k8x9KBhJ7woFHaOlxBGW-LnxhjlKDIPoIp3TtiOXVBuI0TC0uAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSvZV_xLJckeuBY77Ge1jH7wd_sDve6uWZAkfBHpV9DYbGm2iMZVDS8OPHli-aV89yjcWr99jo5ht7UCjzeEC6SmtZ5cwM7c1uTQHw0I-EtKFHk6rHlP7JTZwn5wqNNfL7sFGibj2Fb8wffyPhE9CMA8fJLYTWjBYZuRHDfDg3KsBZmTpMlCd5h0ZRsGdr05kuBj3NDvf06wwdeajTf77aISh4a0wjldxguEuXZS9ENOsVSRNemZEL6YuCtonoM78LBQqwORYDCcbLqrNq1sBSt3uF8eEbpVLSy6EEXNa8X98YR9ta8mM1xTvgLFtJTw-AHrxdlnEVYCE0UKenHK6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGCuqdbTxfnt7weSlkvoJ1pqyzWlcj0w3LaaNOoT7oRyplHpiMZMGx1lJFfXEzIZH0lI0-LwNo8eFb92ZaWJ8d6uIlIYHJ5bKkKdI3Hkh6JQ4XKHU5lkQIE6BV-x0Q19-CacKB4VURA7zGvqiaggurxVpeftd-o20jIMNNMPOdIjH8hFc_QZfpLyC4TJuzq3AntZT7rMMJfhDF441uEHoCnGHyWX6EG02o-P09ZmPEg58-ojr15hvQTaq9epIfy_9zBI2t-5VGWRIfkanAhVYwdfm_HY4ygBrq1_2BYg3xC6sJ6Q3Vuhggb9MnSxmfG-NAP2SA6X2V1cjuSDZFPlz2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGCuqdbTxfnt7weSlkvoJ1pqyzWlcj0w3LaaNOoT7oRyplHpiMZMGx1lJFfXEzIZH0lI0-LwNo8eFb92ZaWJ8d6uIlIYHJ5bKkKdI3Hkh6JQ4XKHU5lkQIE6BV-x0Q19-CacKB4VURA7zGvqiaggurxVpeftd-o20jIMNNMPOdIjH8hFc_QZfpLyC4TJuzq3AntZT7rMMJfhDF441uEHoCnGHyWX6EG02o-P09ZmPEg58-ojr15hvQTaq9epIfy_9zBI2t-5VGWRIfkanAhVYwdfm_HY4ygBrq1_2BYg3xC6sJ6Q3Vuhggb9MnSxmfG-NAP2SA6X2V1cjuSDZFPlz2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=De19j7GaKlTwD-XR76t1lEbkAVN7GOs9-enBMK3KjEqZ771kgM-yYiGqgojzYj23dGH1ptmbgUthgLl4Zk4bSHiyGe9cYmXaFtmRvI3G9QsVVWa2JsGmmXS5ndbGvhqb03EF1iJ8vkXfZWSxJSkTAobGU9PpgXh24NOsBHFRcWOClZp1PrF7X24VQZpA4RnxlgLEJV5EnubLzsMdm-HSMm0cRdk4jwkUImEJ5Yr_aZJm_kXChs8rqaq_yoVptMk8Np0DCnna0mV24ecIxuWAOQpksxy4qNjctIvlqmsfUmtJOZeaeBOYsnmkhvMPogLS4C6Rcrn3YtNsBNlYQd_E5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=De19j7GaKlTwD-XR76t1lEbkAVN7GOs9-enBMK3KjEqZ771kgM-yYiGqgojzYj23dGH1ptmbgUthgLl4Zk4bSHiyGe9cYmXaFtmRvI3G9QsVVWa2JsGmmXS5ndbGvhqb03EF1iJ8vkXfZWSxJSkTAobGU9PpgXh24NOsBHFRcWOClZp1PrF7X24VQZpA4RnxlgLEJV5EnubLzsMdm-HSMm0cRdk4jwkUImEJ5Yr_aZJm_kXChs8rqaq_yoVptMk8Np0DCnna0mV24ecIxuWAOQpksxy4qNjctIvlqmsfUmtJOZeaeBOYsnmkhvMPogLS4C6Rcrn3YtNsBNlYQd_E5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BToBQaZ_PcItgwnmMxQpduSFQNZ11fqpx5uMi5zhHsTBMxCtboyl_U4XgeMom_YK8h6b7KIXijw_MFz1Fc3JxfVCi1fQkBifrNDndiK0orM9B4XfmwIQuXDwOkEMXyVaQWm7Hg_EirnrK6A3-sa7ImRTOWtUB3GiM8gHACYUERWPkVuFk7xZCUY7JMbZXjo-UyLHw9FFLWqXs9OTABsAwUw4_ojLcsqxRKbmh3hJFjAaW6_hg8MJ39ScTKxcE10BxPRb3OZqh2uQJ8SCBZf7lxJA4Isg4MxhdotpKH8FBgFF1vk200WpqFytEUXoPWWo6WYOEbYiVArQLwRNfbYiHYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BToBQaZ_PcItgwnmMxQpduSFQNZ11fqpx5uMi5zhHsTBMxCtboyl_U4XgeMom_YK8h6b7KIXijw_MFz1Fc3JxfVCi1fQkBifrNDndiK0orM9B4XfmwIQuXDwOkEMXyVaQWm7Hg_EirnrK6A3-sa7ImRTOWtUB3GiM8gHACYUERWPkVuFk7xZCUY7JMbZXjo-UyLHw9FFLWqXs9OTABsAwUw4_ojLcsqxRKbmh3hJFjAaW6_hg8MJ39ScTKxcE10BxPRb3OZqh2uQJ8SCBZf7lxJA4Isg4MxhdotpKH8FBgFF1vk200WpqFytEUXoPWWo6WYOEbYiVArQLwRNfbYiHYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAYC2WQE4JDWJi65_rA87InRoYmho3TsBPS_qO1FaCor693jDxtw8QZRGfAhIa_Mvxc6aL-fhAvBnNi4nUJcPZ6gdluCVS8tmh4Uux4rBQYdzrV8rE1_z5qPhRT3R5xTknvo3CS6t2U5S7eQgJsZEJE2UMs0F3_5asEikb2cAQBoppkqzMCR1gIVWLQM6ZeWjR1L3VOi7Y7wW67ezepTmVyYEombxssosfov-q5FECHQkvVjLYy7m-B--dtFDGobzv07rnasu2Jq4lqfw-F--UrE3tJJYDkaID_sJHjk6PxvdlrzcsBG7QgruFOa4iZ8BqdOYwXLmhzBncu2SxFmSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC_k1edIx2li7TC9CasLZ5daGSZMYny5U3Q_TaLSonEsHn2zArO-WtffEUKLRcBqmQBM-w6ksvCGVhuwmnVYZCy6y1L_rSPp4nsEiNajBh8n2dmnzGJL02El663EsAMkALR77V3VBVO7hb5eECPj8xwGaV-KI8hoRbEiYYXA-mP7XQvY1p0D47GXYO6NCjoL0guI81zIdpyxG4Ve10g9N2f5OyFBkYvcOMsDvYd84Ht_D5UmbBcH819aubRMSdmlJjEcEBPVGorfNmi9p2-TriFDPLPseEnQBfs5sO07E5f7sDqIZoB8hlU-BQuIuOH-Lf1Vz3QfQeYIQtKiDsCeWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PknTwRAiGP6igtNOHXCsB-VMTQXVqpa_EmsEJ-2-NJf2fGqwsJ-vgS8BkXVm6nhb7qBnnOcOFfyHY4y2OUeb4nYtbpNshNIagE8lKVV-oyZyDDkZpRKZDVyHZCyz3ZBu5RxmTCUKLr4WbDhkVQF_04d4qve-CKhJ_afpXc9NLtfpQcdZk1fsxQeAG1IpULhGzonVIOqdVBZfyCO6trwM8EXpN0EotWIcA14FALf1QNIezwUyN6ySxaJK7FWbcP-6dY8VHMYU2cZeRVum1ufHHXKtgEwmyvdQWc0fJMg3iQgGDYhWBhB35-ok_5WOPd5joQeDHdqAyFFHcrh8sh5Nwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0L_HqRKDdPVtDf95njZynRobUrnVOYz3z_fP4_9CN_92eSkqWZ9YgAz07Nj3t7WM01ZeHfODO8ydszZwR4mZnpBfIMYF5uyLT00XbpnvzLbxL0yRRFtaObWOlFEJt1N6B_je2k9gPQYQHf2uaJXU0S62kV6y6siGlQb_RxI0AjxTx-dhFc2yx_H4x8pym5rr7AKnNT0EvzCfGYT0fgGdc4B232cTxCgC6NdmHD-eaANdvQPYhwml6ADXSmrf9_ezubIyrvET1BwsLFbnkxrwiRPOWcw8B4l1y8aQRFvyWvYrhX-ZKVxNImstNw4OPObUl40SC-6Q0xulYDPEBhGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9l-SnG6uOkshEhMJrQY1ser8lm8Mw0fTTIR1rI_CUt3U-brn4c0gL0VoqNfEsWydOpTRCCZicZ2HK8WLRYrGEs5bEwe3utKhBGK9z-tEUYZDcZXr0nMSVlQIb6vHsur0XllddvHoGk-D21sjLyBZxu5gNCjWU7_ccwAMPLfY9eFjhVy03EKELeoASy98I2AoUPpqh5sNEvunE5s9M3OCmSEqW_9JrCwAmca9ruViRFca8HH4ySqumtc759GG7W4_Fu6x6qfjBum_-IEh39UycSuHJ3xv8j2t1M6MM3D7gOq1WOMKaGFEjX8Uwjop2YtygxA1s-1DQa9b4wQdAd5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyd_OOp1JRNonhtcYtBkhk1gXulHxRFD8auG_av2N5ofDW3EZYRplJoABpCpAGS0uaV95KT2odzGpQ7RHGlghfobo9qGFfxuzGt53MS4DGZAUpAvBAxxqu1z6TYmIAdowb5rU3gBwXH4XgnEik_zPizY-UMovZJVdqGySdbWTfuDagxGQqwfEpuOofeRz60b3K2RDlUk2aqXZs3Yq9FXAAM2L2B6GEBmiXi0P-LH0a4KxPDHjXP_YdUdelwnqUh3XzII61LxbjyicxDs7EcwJtofmzgXEWdUybP-OhBb7zTTyAZfbNWum6xVWS0m6JhANWpsCQ_4sfPUdksBFMdcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
