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
<img src="https://cdn4.telesco.pe/file/oG5WN3DumIyYO2OzQsTg9uzPIveG2NN82nUPehypSDe7gISpQSNe3TuJ76BFTHNb7fKwnhcGlw1QJw48of9NQwERO1rGMMp98FuSPE_81nYlcC2FNfdVeS9CsILDNgyQ-vSw0wfvyWKbqcLWdM3CwxUlrwoRwlj11rj2vGVmSY3CC2As58x5rNo8w-M5MdtvKu4yfXPA69bllcSne9ds6eZ4qh0dj0lK2_F_DgKDiROuYvwmw1Igg3FAQDXKUj6a6-W_tH2DiKsHaLL0sitllotWzymx4U2Ga4hnON2gw12qYUoJPMkyLiwqvfI56RJqDccqVQlgOOiqLyELySSt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 05:23:21</div>
<hr>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=tNU5uEPzoKYo-rrTKMF01kX7H1CATupCxPqAqeJjAWYQiko8IlcNMalrEX0yuOcyeNsf1RRMzUJu0ecZnTa4mmD_ZYwzONb-VAN-IirexBaCu1yzSQBSiPhScGYvyzGE_rjEmmnoMgewxQNiyDTecxkj_PL-3P26UNhbeqbcpAYhG2DHuc8CJS10lrbfEIpMIYnctv5DnE2VTXUSLKqxdqqyvsgSeilk8lLCW2FZ7MC_lkXJOljtGCwvvBYD8NEuo5M47uDsuTM9AQn1i6NSQjw_ep3r-UN53Lw1SKRRqA1YRFKgcaEGZ5mb7WyCfZRAqEp19v_C2IrHEhIU8WiXcYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5E1UvQisOUYNvRIBdOWx-bY3uG05FRSG-1gr3f2qY3oNGAiiIv2GUsfaCeCUVPwrhKFukgNo_CqWHm42-opva1tFSKkfTeRpdqHECndLHEEMJt-oHbJJpBy4HryLEee007nSj-xlxGShSLG0qTGx2VmvD2AHuB1RmL-015pVBw66W_pGkLz-eEBBhqWrEMoGU9SOGrKhWRzl_AFtOvQjI5DuRRQOMMgKAzSSSPO4PWulAJR6DuKHFfwtvJZz-sioJ17H7-CeiTyznVfOEOn-eDON1cY1BbsZ2XtNzV5iu9yFSunEu6Itqj_4Z5UUIOnBzCruoQFdUnNuFCxtN-s1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov-5teW3tHTvsvSbgMdLICYXYlU_sDGIu9OuiTSl0594zrfs9gRoJQR8S28V2CiP_XCjD7Zzp5uItinMqAUIbUIRvVFn3zxxaqYh9Km-0nk74uSUdeQvuMYluMHfHS7WfmU5Mq1R_o1vTjHKfD6MlZEq2Yf9KVRt4d2gzoWcCctXxlvrZ83-13fvHD4NvwcgSfJHIpLOCqzOAdqDTCE-6frq1o_rpZ_dr6FZtGyKaUvR4uN5aL7iKlIR-aOJwWaAcP_ZJcq4l0tyEkcUu7cd1nNA3Bm7_vFPEyFbPsYQr_SdVeOSm92Zw0-QEekuDDdOwCr60iw-tbsukbzrBFNmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHVVCza4-k7lMKxM3gRJStW0mSmbHx1HOC_kqRItxfPQPZo3RqgLfbxvjky93wErqiutSbOoRDVDgJO6-5Gt5GeEQYp3ZpC8LbmHHVvogV5fTJ8tjv9WUtzfZpz5NJscTMxYul7zKui-uhcGtGwcbJz9kr1kP6yA61rGmmeIOf2BDf3B7TQdUT7ccFphzbXnhtP5luogZEm_0Gi7-eRD7KumLBDmDBfFnXn0yVHUWnWFFsbkQWbKqce98C8p4SF3LVslyiNzTK7TUUb1kdRXw9U_E3m1dmBOkEfxlEWe_yZkhLuLgJrZdcC01kX5yYjphMbJYFfm6UDxnofukWHSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Lm01xlwTxcsXljg0TTm2rEFYf0LH6TVSDeILzck1jlF9aj82LMZDtLfz7GoTxmcOcw702PvHqPUozpDWcx3p1SHL13sxbOzbWwoaAomeHt3gomfW6mP2jLryAqOyCkfIrDvguSLsHK9QSLzn4FINHxB_vdAyUSs4fRcbuWUZtYKAwaHNcdsvNVyhu6jMDeYfr1pbKa03kJHJjrKTRvFKDLiozK94stHQMWspQVGOEQPmxl0SwhrvpEiCAGc2CigFjuDI_gmkPzI1JmqOxCJfauYShPwPojtC1RLmjZS2tUeBSkHDzG2FBjseMKYkE3E6Z0aco6mxHBjgM7yPbMULAUUkUiUVQlqi14IrXZz4umo-H3b0eKCL4xyaRmAgZlyOkPxhE0c2di-cEAkPrba2tWn-Q8h2wWLgQuwF8edsHiM0_5gMyQ03WwhhFZmSX8L_dOxWsPcvb7jvv2uaj8UdkyHSdGwN-OqXBSkHTw6mJDLfKXLTfvHQf_AK7PUc9Ohqoy2YlI2uz6pv_I43lmNFvSkXYTqz2DCb9i4jeh8wkrJcAiSRJ0kX5J00WtPslHblj2fStVsZVpViwvgM1D_n3APoi8sjTQBFjwQgHgWKb-Tm8Lio8tvH3SJcM1mq2buyLyWnNV-32yqyuwx5bO1Vqe6QxJTybQ9yL5acDRy6rwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=KFr_RvQ_lfSvRrwCsy33D5v5L8qLWh8fD1b6jCXXmJZyi1ojn_fbuXYG2sYrqN-hvhdYD72J19SR4_a_b6mKjxHZwi8JsyuajbvX3Ks-wO871VJlslmJYxVlGHVtoSjvjy01JCeDoHpdj9ErwLwDgMQcxAsGaNUMHtU5SffYtkoKLlgBx-p7UFJ9JducQHoR6ddOWW8dQtyIPKkhpdFoy3feYafDFZkGnZP2e_qlyMCJeKXN2YDzzYedcMUFYOHmq4oOvtfTDbrTJwOXrVZT3xcspT49zf1-ZSDFCEqXs7k1LteqsfUHa1jODNb2qBOStjnXKTQvjyzoJmvRFSni_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=KFr_RvQ_lfSvRrwCsy33D5v5L8qLWh8fD1b6jCXXmJZyi1ojn_fbuXYG2sYrqN-hvhdYD72J19SR4_a_b6mKjxHZwi8JsyuajbvX3Ks-wO871VJlslmJYxVlGHVtoSjvjy01JCeDoHpdj9ErwLwDgMQcxAsGaNUMHtU5SffYtkoKLlgBx-p7UFJ9JducQHoR6ddOWW8dQtyIPKkhpdFoy3feYafDFZkGnZP2e_qlyMCJeKXN2YDzzYedcMUFYOHmq4oOvtfTDbrTJwOXrVZT3xcspT49zf1-ZSDFCEqXs7k1LteqsfUHa1jODNb2qBOStjnXKTQvjyzoJmvRFSni_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4e6B8cLTHOFZLC_QYWCJylwSJy9W0ogC1kkRdY6btQuH9H8CxCgaa_B10O5ewXYUxmKpJiOTN0Ok1jOwJzi0kgotaQ_2jf9b_Y5lklIwH1mMX9jIZqCs-epIINGw6Yx4PIe39KvGuERRpop0rMJzGtI_xUPz0gFzFQcBAm60EllibNy4qfoms-3jmaAXpr3mODgfU-TkPoqkbeC_wKoaxzAUUJpquRW9VB3eEMGor6OxrZmO2GWGGsilZJVFP8KpTQ60nU37QY7iTkzNHw0mzJ925GZBZ8_gLXhUxvi0Rb0kUsZY6BSvIAEyxdJzyaFGbTkYYq8rukWUxmT8i05hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRDY2c5pEjncJIab9msG0dKLdL7HdwCDTeOfX2BFy2ceNF7j_vB-rfpd6RuDlMgnyl6nyJJfxNr20VwAHxJ2JeEufvCIXlgUfk-AMIEIda4Hnoa6GpSPwpDpQfzsCWv7otgihi_rjYpw4LRpwxU6kE5So8lSsYPQpvE1lonPSAHBhFQ6bY8Y4rcsWhkr0RaPF8BMAGppXW4O3WzgSuk9OGSxUNNI6VWoQ_QvuHSHUO5_uiJyzQ2w5wAI--Uf9IG_eZNo5wIgcl114Dqn6NPXMXd1LteITA_Ycsxfi16cLfkFZj8_WSy5KWKZhHpu2d4xWQHYC4Qrr3XrRqmqbF_-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnzDo56TepHx8jHxXmakVXvXeC4cIzbUflmVGO68ymFjqfF-nwtXM0dg6MFJB9U0qm84g84uMISInnXMazJACF7rKV602ke4vFJBu_CJodfYYiTlVfzY_rTn3dc9vH91P9IHUqm2BVOdcNHZLOMV2X7Sbs8ruT56UVrAc6ymOBU0lXne-ky5oERHTbCunq40TLgpy3Qr1f68ro4elYMTjMhQ5OhQQrLHBi_sd6dfIHiMYbhwLoastWE-pYU07AcBbHnaEVBtnlSJDCj4fI7TfbYzfYR1Y3K9CLveTIylu3W9WUOaNlcBcRzow2vJ5YegvYFKYBZb1vj2ZqgZQfiRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ZpuKgWUbNkBhrlPAyUNiuTdoKSxzGGFA-AMbipgF-QHo0Qhuc-_jUfW8BXES336aNy976NndGc_NnB1uQzefdyZGfL8oWX54-9I82Q4bS8iUM85LwxjiFGLWbbqkON718BshncV0T8SmLj6oZ3w9kveUgQrxgcmhbwa7uah89s5Mh9CbLYA6TGVnMiw2iEV3rr8FKos43tpRIpY0HgxfZEodMcb4G1erfSFT2h9VCc15nQyF-66NFNKBediTHN84Dbt2mU6gROmeO-2ihBmjUSGm-ENVnYUF3DcZgjX8Z-sdLlVwEMJQbQ7PrbHkeiZsqRg0jxXr7YP00q0R_zfKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ZpuKgWUbNkBhrlPAyUNiuTdoKSxzGGFA-AMbipgF-QHo0Qhuc-_jUfW8BXES336aNy976NndGc_NnB1uQzefdyZGfL8oWX54-9I82Q4bS8iUM85LwxjiFGLWbbqkON718BshncV0T8SmLj6oZ3w9kveUgQrxgcmhbwa7uah89s5Mh9CbLYA6TGVnMiw2iEV3rr8FKos43tpRIpY0HgxfZEodMcb4G1erfSFT2h9VCc15nQyF-66NFNKBediTHN84Dbt2mU6gROmeO-2ihBmjUSGm-ENVnYUF3DcZgjX8Z-sdLlVwEMJQbQ7PrbHkeiZsqRg0jxXr7YP00q0R_zfKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxi1-Fa3KbOUc8bDriX2OWx-7yFl827tGW6nk0jbcbbhWdGhTUiJw2AwMmKPo59NUt5dQVDEa3san9atQC20y1VYkjQfUAXWzdlZDkzPlazHF0kNY_G6m1jpGGycGSogoFBLsktaK0wi8-Qa4N5XPLEDcUU_AC2TqnBHYAQy42FycnWAGPUXystBBNpeFxZ6SZzHlaJUq_ivQ2ibkBdBkQXvNoxvlOeFfcPKhE1J85AqGTLQ4LhrGTscm2Rj-JyP7wZMV5Z67x15Rlp2w4UjkWtq7_2gKRDPlOjYSOim2unnHzz7_xkoJi_YQ6tRBQeK-rFGABMF8qPu93LGf-jLGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_y9oIVn2QzqzNL5p5BNCZByQDMfOe9t-tCYVtRuh9kj5yuOnmJedWavzWiB9fxEi6uJbmxYe-3BkRpBzDX39411Jos2rsqb2OkrkhCr5rmM8KsmbpPoCkgUsUNPtRjXl-sBWKPwLqOaKarVFZkJu29H4Tzb_ufi--2jGlQp1J_wDAsH-3j_PccQo5LfT-TdafzijQQK93nbgHtabDgNi41l3h_Pd56FFBX6VvZe0k9SYVH50uE7vxsselebsaPpmkwt5201iKohJqfyWjySr9uhWrzuCZhvWER2lXcGVfAGnUk6QYRhtbMZS5VXjA-vakKQ6EY4c103vLTZD1WvLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_M2ph19HNgixqU3x3ZD7-SQH5CI7vWtrJJjHG64itE8QdMWx0nYAla5jIilhp3uGabJvKe-JuqxnKj06fz7-XPEIKKX2fDrap7eI9YtHl50rfca9ZyC4qiCZmacl6N-ehGE-8OQX9Fm2ZrJkd8ZEljdGl8LAPHGPu4fp8MCSz64nDac5h0VzHdANwtOy3Lc9TVcb6-MnQKoQdcWTDnM0Pbsd-SB-TvwDx21hKthMfUYtw-tgRm86eikjTSjdgrFpv1R9WbBJnGR0tzbFoJ-aE4WFCv5RuPRNKwLWDe6RBPdOKf8At9vHOZR6ogMwcCy-Pl9T8t1w3aNR7-ZZx81pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TatBBNuSswGWPq-PGBb97i-4PZ96gm2rEAeX4y3YDQhY-sxylWI9Q9oMmIr5LkTdar9D_hP1yTKreAmOEYi_pZ_yvI6Q8cD9841eSqDhhx8_r3O9v13TdEJo8B-tKSd5k9vkWGqVyeD9KGpnnkyw4GSMuDywwrIu76oR91BcuWI-oS_6mqrs5xwjXiHQHW7T-NctOMm2rn8aPGFJSvXYq8De_eC6Ryzjy_8r22v_pg5ZGj3vm3kC9XVcDv1tXqFjnctJESCTi6UhhPXoHc9vvH7siosPgYhvagMf1LnHcao_597qiqX6VfvAJuLvIO847X1ggiGbqHMs6iY4KsWE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=QRlcM0uc_RS7i1fz0Fizk1AKMrilwFQZwdnZxp3CYnEc_-ic_lEvmLhM8Bn_AUm1_n_f0uJpMvNRTBL-xqfiFH6XrGmd88nMjlmMbHibQ9tq5Bv9HxqLpUvV_AZJW7yN800xy7xLxRPJz-azmgj4FrGLpiIHfzXLOOgE5bx17RVotxF4XvWKeIfVTfK947SqX0ei-7GBpbzJp_DwGMmVj8PMIS-kLBsjgXqA4mJsBLPpxfR2P8RW3WUC6P-MYhmMaJ3loI7-OaajIN89bB9-FuM9Mv31Yiv3ePOeyVzYilaeF7e5pdLo8V5UXQ6UTHfNB845kXOoweAKaE1279wygIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=QRlcM0uc_RS7i1fz0Fizk1AKMrilwFQZwdnZxp3CYnEc_-ic_lEvmLhM8Bn_AUm1_n_f0uJpMvNRTBL-xqfiFH6XrGmd88nMjlmMbHibQ9tq5Bv9HxqLpUvV_AZJW7yN800xy7xLxRPJz-azmgj4FrGLpiIHfzXLOOgE5bx17RVotxF4XvWKeIfVTfK947SqX0ei-7GBpbzJp_DwGMmVj8PMIS-kLBsjgXqA4mJsBLPpxfR2P8RW3WUC6P-MYhmMaJ3loI7-OaajIN89bB9-FuM9Mv31Yiv3ePOeyVzYilaeF7e5pdLo8V5UXQ6UTHfNB845kXOoweAKaE1279wygIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Cx0bTWlgka5V4xubP7ypwy85KvFis_MHWvxsz2bxOYcdKKBIvTdvIFkrkW-_sme5U7UEc8Na0OChLrESzYl2voSt1EofJBBuFv8BMxa_2iF9OvBPyFwW6Hc9F2BWKIya6AcLvTcz6hjkuCgo5QGtz35MnF4ykIjT6ty8oFyVLIZ2y7uS49bsSbAeSa2gykID-i6S4LD7f5HnG8zvUgBuazUKe8YY-6OTFiazu7sXhqMLajJXH8LVZ5TSmL-gSgzF35OJZOWO3OXVXKtmP7TibwmwpgdpthP5qa7RSjCBWjsPctad378SNpHHJpOl5MOeVouenmyzGIzR_5G3Vd5Llg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Cx0bTWlgka5V4xubP7ypwy85KvFis_MHWvxsz2bxOYcdKKBIvTdvIFkrkW-_sme5U7UEc8Na0OChLrESzYl2voSt1EofJBBuFv8BMxa_2iF9OvBPyFwW6Hc9F2BWKIya6AcLvTcz6hjkuCgo5QGtz35MnF4ykIjT6ty8oFyVLIZ2y7uS49bsSbAeSa2gykID-i6S4LD7f5HnG8zvUgBuazUKe8YY-6OTFiazu7sXhqMLajJXH8LVZ5TSmL-gSgzF35OJZOWO3OXVXKtmP7TibwmwpgdpthP5qa7RSjCBWjsPctad378SNpHHJpOl5MOeVouenmyzGIzR_5G3Vd5Llg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=somt3nSIKyemvI9NZ5ck7GZUDhzKjrUPkVTS5E1r7i0CTx2HBuoeDrqQCcAPQRGRLOfLIglu-UW2vmoPm_S2lzml-Nd9GV8Wei9HwLk3d6L0jJTes5MrQEWL8wI7RRBc5cebc92tipt43XHBFjKbhCPAFX2EnvNR5wrjpge9w5njSbYuagspahwWG7VqXux-spWu2aLV0I7odDQ7KUJGlwOT2dCwEOI7IWtlx1ZhfYzn4wcG6t64QbLbgQowdmGzloVzmCnh-l7AsfjQPHmUR2EhHWkeyl9_RdQt2vFdqW8cnUJgqgYts-4cP9SaUqEJGAzrisYl3sEqUvLQvOibIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=somt3nSIKyemvI9NZ5ck7GZUDhzKjrUPkVTS5E1r7i0CTx2HBuoeDrqQCcAPQRGRLOfLIglu-UW2vmoPm_S2lzml-Nd9GV8Wei9HwLk3d6L0jJTes5MrQEWL8wI7RRBc5cebc92tipt43XHBFjKbhCPAFX2EnvNR5wrjpge9w5njSbYuagspahwWG7VqXux-spWu2aLV0I7odDQ7KUJGlwOT2dCwEOI7IWtlx1ZhfYzn4wcG6t64QbLbgQowdmGzloVzmCnh-l7AsfjQPHmUR2EhHWkeyl9_RdQt2vFdqW8cnUJgqgYts-4cP9SaUqEJGAzrisYl3sEqUvLQvOibIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvE6Kl9FEM14OnGJDoyxL_8EE3_Qhl6PKOFbtYnZ-yQb0ZYMge-Deva2LFOmyUzkXnqM-qcEGcWHA47Jvn3bkUSXlnL0Lt2gj5cRB1Jby3i_k34PZefWGbQJ_YDFeFaTnoRIkRBfdN8w8vBV5zY-295tFICxztPmkUIBDQqqOvBrJqQbZFu3-PZoLC_WxMudcYjXwZquUfeI1a2c9II11wSrfaRl5Z9YmSUys3Tq03QzPHLGH8Sg4hNktLMj2ZWTyaZV2_shajF7C0NA_hd5eeLJsiwBgDSpSA6Fcac0bYTMCrdJnA8kuvCHqlwqZQ0AiBIp-aX46t7d9ChX-_hCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=tCVr9O8i1KN5O88tyBhLeLnjk-RI_VlF22pzX6w6yNSKb7Pc8pUcC2qSn13AlzLLjwUa9qTdzhCnZZDyX1d5LLFXICZzJwOGPJkYpF3_w2GiI61LijqdzH5oioW80MpY0iqfVkKLInvX6k_56mKRpQj47DiZAWQUK8QMDUSE2rqRov5BRc069q1_co_fvFVSWy99Xe3GOYCJVxMeqjgjhw1erYKDEtE5nzHL4_yxVEvg_ufmZkYuxry7X7ilsBkWHDz3A0RQOGGHEuGSD7LFfguJyBPV5sQfaKG5LcNGxRyrCnJ_pWIHrFHMnVVYoPPI_78JiLuBxBbPXE5RVMPIbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=tCVr9O8i1KN5O88tyBhLeLnjk-RI_VlF22pzX6w6yNSKb7Pc8pUcC2qSn13AlzLLjwUa9qTdzhCnZZDyX1d5LLFXICZzJwOGPJkYpF3_w2GiI61LijqdzH5oioW80MpY0iqfVkKLInvX6k_56mKRpQj47DiZAWQUK8QMDUSE2rqRov5BRc069q1_co_fvFVSWy99Xe3GOYCJVxMeqjgjhw1erYKDEtE5nzHL4_yxVEvg_ufmZkYuxry7X7ilsBkWHDz3A0RQOGGHEuGSD7LFfguJyBPV5sQfaKG5LcNGxRyrCnJ_pWIHrFHMnVVYoPPI_78JiLuBxBbPXE5RVMPIbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=JmwY0QSip_pyUZnKB46H8Tkv-AmI4O9c4IAPM216ZLhcQyaenGkAJhRMSRwRHkoZaURtPN1RNIxMqCLuw9C0BQwaMlmBkgNn7lrVXslG8n2XhFrjLsF-H2U-lCWOTLIqxFf-WAQCC9S8cbe14sPXPJzqJrHoTN6VB8_bDObHOxxn0pfSOYxt9qwYbzKjMHOkIC5DlxjIoZVJ5Mip1r3HxjCphLH1UVdGRzr-ZNBM2AbyUiLcZs2vZ7TDUMWNSi-CO-Kcj_Aq6gq3v_WURl4Pax1j-rTnNbhGSDkM0lHvRfEqfOfvtdJwRwo5fikxi7VxVe6l0ZzbHvm7DoXazP98xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=JmwY0QSip_pyUZnKB46H8Tkv-AmI4O9c4IAPM216ZLhcQyaenGkAJhRMSRwRHkoZaURtPN1RNIxMqCLuw9C0BQwaMlmBkgNn7lrVXslG8n2XhFrjLsF-H2U-lCWOTLIqxFf-WAQCC9S8cbe14sPXPJzqJrHoTN6VB8_bDObHOxxn0pfSOYxt9qwYbzKjMHOkIC5DlxjIoZVJ5Mip1r3HxjCphLH1UVdGRzr-ZNBM2AbyUiLcZs2vZ7TDUMWNSi-CO-Kcj_Aq6gq3v_WURl4Pax1j-rTnNbhGSDkM0lHvRfEqfOfvtdJwRwo5fikxi7VxVe6l0ZzbHvm7DoXazP98xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ZSoKhvTJPGYq0ZDgOhsZsK3sz7a79Jjzre1l0P1jwbQZVhO3f2tslOMGXcRGUDH-zTCcOnf7lgtU_1H11aFxepFq2_BB5zt6oqii7vO-KlK0MEZhFb2Z8PxbbGOdczhUIcQG9XfC-QQXGCWGTUmbmMsalrDTDffWCj6aW_aXOn3Iz9c1sPsyPYoxXJ2wfLGU2ucmHwMMLoR8SklvNxNE4cez4sBVpxMYlyxN4cLrGz6SAqqhSpN9rz1AA7CFJtYDXG8U7KmfwH1ojG-vhohJ34YvCKehdzjnbYEcVcLk5DTILWSdvRMUGKY3N_Upem0GdAXEM3at9j3etgWqce9ZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ZSoKhvTJPGYq0ZDgOhsZsK3sz7a79Jjzre1l0P1jwbQZVhO3f2tslOMGXcRGUDH-zTCcOnf7lgtU_1H11aFxepFq2_BB5zt6oqii7vO-KlK0MEZhFb2Z8PxbbGOdczhUIcQG9XfC-QQXGCWGTUmbmMsalrDTDffWCj6aW_aXOn3Iz9c1sPsyPYoxXJ2wfLGU2ucmHwMMLoR8SklvNxNE4cez4sBVpxMYlyxN4cLrGz6SAqqhSpN9rz1AA7CFJtYDXG8U7KmfwH1ojG-vhohJ34YvCKehdzjnbYEcVcLk5DTILWSdvRMUGKY3N_Upem0GdAXEM3at9j3etgWqce9ZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=DMK_Pfj-0_ZUwhcC10EdO7TwMQ886aRiDwa7TCEiIb60EXOF66K6tketkykmBqxnUyuAfP88BolPUvPCRrKHTMKEtZA_rokdwGrv_PF1LGueJWEP_QQv-XKpLulftLE4E9UY-Zn0zlCZkyd0LetuevkZPhZRyv94pY9mznPzOC7RgrHm8nBTEu8oEARO4_OJXIDySq4wdrZn6cuROPokDte_j78ZxiRm8328zqOxNWwGglCPNSiPNgzAie31uNTcDR4Fdtqub2HIKEq5sD85Guib5_S31C2caaLmENVl7cs9LjLdXnUccL9WwL8ta5JSANI_Ni-QWeYQ_SxKlE0x-iH_4g2ipntd62Kb8j6qqW1GslQHOY-C2wSXjAH-wtzXg3ahWCb0qgd9tmaMh3j2mPbs94St1EPS3cq-1aDk6-sx_IvQ7SUqDkQfsABSut8mhb4OIgVlLRRjhJQ4eCrsHw-8LpaQ_TaTrojwlfgJ0oNxkLRM8r8v7fJ8WGy7cwhv4BsmOlrybmhVkxFGncjpP6ONx2YcERDVlEoezc2Ypbaldayf7hqW2dNytvtOrF0RSyBKyFOP_fycctylGJZGhP1EWS3weP_nuuZ37_tKl29ZDAbuI8x8RNyqhFX4y1BA8nGX-uRyjsdhyOF7tyaWNxyVldh_Z-02DTSfGu5227M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=DMK_Pfj-0_ZUwhcC10EdO7TwMQ886aRiDwa7TCEiIb60EXOF66K6tketkykmBqxnUyuAfP88BolPUvPCRrKHTMKEtZA_rokdwGrv_PF1LGueJWEP_QQv-XKpLulftLE4E9UY-Zn0zlCZkyd0LetuevkZPhZRyv94pY9mznPzOC7RgrHm8nBTEu8oEARO4_OJXIDySq4wdrZn6cuROPokDte_j78ZxiRm8328zqOxNWwGglCPNSiPNgzAie31uNTcDR4Fdtqub2HIKEq5sD85Guib5_S31C2caaLmENVl7cs9LjLdXnUccL9WwL8ta5JSANI_Ni-QWeYQ_SxKlE0x-iH_4g2ipntd62Kb8j6qqW1GslQHOY-C2wSXjAH-wtzXg3ahWCb0qgd9tmaMh3j2mPbs94St1EPS3cq-1aDk6-sx_IvQ7SUqDkQfsABSut8mhb4OIgVlLRRjhJQ4eCrsHw-8LpaQ_TaTrojwlfgJ0oNxkLRM8r8v7fJ8WGy7cwhv4BsmOlrybmhVkxFGncjpP6ONx2YcERDVlEoezc2Ypbaldayf7hqW2dNytvtOrF0RSyBKyFOP_fycctylGJZGhP1EWS3weP_nuuZ37_tKl29ZDAbuI8x8RNyqhFX4y1BA8nGX-uRyjsdhyOF7tyaWNxyVldh_Z-02DTSfGu5227M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=jSKRQL_WvyPntT-eyXdd7kJEeyva9Mab4esS9lWjPrQeFtG2HRb_oj7X1zT8lmj6cDoO7I1e0sOcb5ybUPCEM9C6pPkrsbYEu9A4GbhtRMFSfboetRcsxeRcQWlw17-WtZdGBblF8IFPY5qEha1AYYW3TcQeKwmZB5R8MhuG_uXE7lFF7oBHvmPzkDt5y1qzoJkFm2YYpeQ-9OkuO4jd75yqRtOw6foltY1Hzyw8XgPlc0_rlap8xhVtUbwAgVTVUHQnmkbnLVzbZg-MeH8lfnfaDN2CbCrNznQ-RbYIPtcRe0RKeVTnFjteAuvM6Nxg2m1Xna_epwmhf0rK32dGuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=jSKRQL_WvyPntT-eyXdd7kJEeyva9Mab4esS9lWjPrQeFtG2HRb_oj7X1zT8lmj6cDoO7I1e0sOcb5ybUPCEM9C6pPkrsbYEu9A4GbhtRMFSfboetRcsxeRcQWlw17-WtZdGBblF8IFPY5qEha1AYYW3TcQeKwmZB5R8MhuG_uXE7lFF7oBHvmPzkDt5y1qzoJkFm2YYpeQ-9OkuO4jd75yqRtOw6foltY1Hzyw8XgPlc0_rlap8xhVtUbwAgVTVUHQnmkbnLVzbZg-MeH8lfnfaDN2CbCrNznQ-RbYIPtcRe0RKeVTnFjteAuvM6Nxg2m1Xna_epwmhf0rK32dGuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=cDBL1so9HWAfThDs35lbxq09dh6M_MnAl3teSfz7GqdcjCn5g_ZNWM-UqDiqOL76zJjn8TvuxNBoKgQEargDFeBpXY6c4yj1Fgo6oGh_ejnvgXLWj13gyyLzY6oiWl84FKpVAEtPYHOnnWni4AN_AkKoDggQ_6hQ_yt3zZf2JfyH9jii7V1fWtlHHTUiyuDeIr5ydkO30yFItveqUYMqRiAvCwkun11AcCFFzuJnDRIf4DsWDFBnEpvuzDoXQ5JF1GixR2C0kKyEuKlXP2He378xBPW1ZBVC60jLfAo4In21vUze_ELhbUmhHegjkIaisP2quB9m5Ujcm2KTMyWHNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=cDBL1so9HWAfThDs35lbxq09dh6M_MnAl3teSfz7GqdcjCn5g_ZNWM-UqDiqOL76zJjn8TvuxNBoKgQEargDFeBpXY6c4yj1Fgo6oGh_ejnvgXLWj13gyyLzY6oiWl84FKpVAEtPYHOnnWni4AN_AkKoDggQ_6hQ_yt3zZf2JfyH9jii7V1fWtlHHTUiyuDeIr5ydkO30yFItveqUYMqRiAvCwkun11AcCFFzuJnDRIf4DsWDFBnEpvuzDoXQ5JF1GixR2C0kKyEuKlXP2He378xBPW1ZBVC60jLfAo4In21vUze_ELhbUmhHegjkIaisP2quB9m5Ujcm2KTMyWHNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsPR4trgBqFV-SKJFmZkWA1T9yQx-xT-K_b-H5bwEYthWhaA7vNxgtakNr1-e7sd8ucAYpQQKz9QNa1pgz4gQW7KhcXDVLImB_BKQ1pPOKx4VbrBx1l-F_vX5YiHzXBahpFP2PxXMDm1NJ7-vwWTUOffemC-0NYPgnOBmeF50m59D4uBfeIhw1YUFuP_rvpB7sffxLmP664d-HgyfwnePOpMx1ShCiNjx2rALNAepTpdbPscTKT5NKbCR7K3pDPLnbYRQ29sIQ0B0ZyAb2Rw94Mw_5uXICQ5cIswhVDyxTGmphNZ5XTi5tgMXnE4QFVGFtzmNa1CmhcGVTBz8eUvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yrx0TazNmdVZKIY5fH53_Erg6J7NfSwB36dFkib08wkHCCRoK9rFwzTCEFGiWteqCZCJS-Uhf5_UMT75L-jh9_yt9EHEPCrcnVlMXm3RLgkrUTsSGait9gGr3XtENuEtICs4XNoUmZeGe73dmRKuITihl2YygdG_rkgActXZogNXsVooU2xj-cEnw92sDZa7Dd4rjuFR7H5R1UKn8wi-a_I9m9HeQLW39mneUVEg61KVR9knWnF37E1JLHldanLHONuNqG8jeBx-WR06arXFgl5iZwZ14t-TG_8Nlx_zhWT8CrFtGLEfrcnv1x2gLCwJqsBRwH70TfVG2UEKVST5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=AUWi93Ww4CcdEpm0Vv7IRbSyqILolE1MP69C3IJTjoJTY4PkQiMLfOGHd70rbXNN3nC-vFdXPuhMTIwi6ATOXs5bMfJirOWOLwTO6p_Y0E332gC06TYg3Woz2dLn65wHkCED1agNFhCN6gdtvACzcgemRml4ReBBAUV26SOkvoq2dbGd4NIV-K71fRJy9-lt3L7TJckBxgrH4WLQ-KrgPUFBgV47y2j48luvB3oFqOy3xjUkuJdtMjDCkcTe76C65ryB_zPyuzWaWBhQGnfO3LofYx77MQ473njToRwF1ZxCr5cwjcpBRwDB3a69T_Ic19T1xeMXAt3AzDsicd8NJEElAjdbzNyluq2rL4Z0OpbBVO8arMb4kkY7y4JASMiIFp6C1zEB7nU6deSWhfKXDRWvh00Zrhc5e3gZix2byMizeZto6GZiIrqHD3Kef9D3zIKGWpIjr3lRTqJ_NZ5vwM7uBIKDoFxeXXuakWi1lnTVr1Mgkq_-35Tr7SmkePCTEAOP1H6y9hXhaoUgptvnVyBTcmw_pAC51AKXltxdUl3LoBfS62_w0oyWYjjawdf0vpGTc1CJt3t6S9QeQG1iRVllopa2KBxIwwfUWidKEWEtEs91yQlSRorNWHeOhheAdIZm8yKpMJqlObaLPkHC5HSPcUHp3qOPSzFQzT27tEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=AUWi93Ww4CcdEpm0Vv7IRbSyqILolE1MP69C3IJTjoJTY4PkQiMLfOGHd70rbXNN3nC-vFdXPuhMTIwi6ATOXs5bMfJirOWOLwTO6p_Y0E332gC06TYg3Woz2dLn65wHkCED1agNFhCN6gdtvACzcgemRml4ReBBAUV26SOkvoq2dbGd4NIV-K71fRJy9-lt3L7TJckBxgrH4WLQ-KrgPUFBgV47y2j48luvB3oFqOy3xjUkuJdtMjDCkcTe76C65ryB_zPyuzWaWBhQGnfO3LofYx77MQ473njToRwF1ZxCr5cwjcpBRwDB3a69T_Ic19T1xeMXAt3AzDsicd8NJEElAjdbzNyluq2rL4Z0OpbBVO8arMb4kkY7y4JASMiIFp6C1zEB7nU6deSWhfKXDRWvh00Zrhc5e3gZix2byMizeZto6GZiIrqHD3Kef9D3zIKGWpIjr3lRTqJ_NZ5vwM7uBIKDoFxeXXuakWi1lnTVr1Mgkq_-35Tr7SmkePCTEAOP1H6y9hXhaoUgptvnVyBTcmw_pAC51AKXltxdUl3LoBfS62_w0oyWYjjawdf0vpGTc1CJt3t6S9QeQG1iRVllopa2KBxIwwfUWidKEWEtEs91yQlSRorNWHeOhheAdIZm8yKpMJqlObaLPkHC5HSPcUHp3qOPSzFQzT27tEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzjHS2_Wrpi2cVP9SN8Kiml1aswAY0AVaQ93uSqcE7vpm7I_NMuI2SwvqSFVWAp56O4vjahj_YjMylrwfD1l8iShNt_Ci30agA3PDdzFvZkbwfSnu1NQ44pSQEGjH0pk3o50Hn1fcaY-VfVlOccGDq9J5WdjQROxQKpMtu5oSZRMMUOuzw_SlbMbyhkfaUTOmLFLI65JzLDy6fcdA0kA1jT_WDj5PhYXA733TwsIHn5oxpR0fqDfCxViIAn-e9BxGwDVSjHptn8CQSWIzJNadomjJvUR-qt1QXFyHVPkfZ8CtWL_Y8S-OPVf0bNrz0BomkJLrJWvcfFABL_56Q9KDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKo15vJ-hRsYdgkpworVhL_pPOfTL3DhitKiYFGFG8YLkVczVwSMK3zHhIz-NxZqXs_PXk1THyQfNCX7S90MifYTLjXJjBc8xv4YEXFYNx6JqMUcmdM3fxhqhvfFCB-5WXTbjKQRIsUX5neu4POQyUoo1Qz9CVjLH9pEDIlt5-elsUy37xya7fXjMTEHFoux5v-59xoKHgJOKrBfOCfg2O5klhWuD23l0_h4vrnwUq-7k-gvZK7DM6spJLSQ0ZokJYRnTBUboJk5F5Am7Mqs_I4JBpEMAGMv-QLENkTVZU5Cl95EzHKFpic6AnqwsDzctpN-AfMNyOeArOXO8UOczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnkFYOGj9VCHQmX-1yVmKXWYwjxeP8kpHFEtEFqvd2cZU9E7hK01Z5_W45AGbGGWFg62f2xeHS-zR1UaHyUn24FQtOSWqy6d6VrKNYXaP3JEGluH63OKxPGkpwklCa-SudMh9Cxpvx0N8e4R1jCVSfegpgtq3gDUckU0IEWXnqYzYbYKu8qgAJvjxiC7JFFL8Ar7h7OOgClg0J6imDgGwctyKYBrGaP6lR3LLpJaIhUyKHnacCojznBSIBblc854hiqj6IqzOCqmxZU-unsI81xGOyzpWCUzOl6bad7S3uzCWnJM08LpdnOyXIn8qnm9YtMHP3qjnPNVWiWsWsm7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldq01NfYkT7q_4ns3pYmVVUS6j--Cg5tFAR0CpmBl5grMJxcA1piGeoeoJC2xtvkedrcUITXJ1N82JBeQcH8aFNqc8AltG2D7yhf7QiPKEyUA5JGPGt0xhnPxTtMJEN-14ZwkDiKpAgbVmev0OOq_maY3XJaxbMZTG7Ci-d3ovXXSpVNRyy3DrUejj3qdWUsLSBkjnAj0kaT7pwnO5UGjipnFuQqp_xol-d3K9MluuiOaF6CmLl_XdxcfECAHmpBza1OtCSyzm7K1qaKPNfAa43yRU2akahL4YPMt8sA4Y7KcNMQYr_KhfXj_WdaTbPay2VrEEoY1BY9i5Jyo2ImpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=ANIvFCwiaV7CJkIARjWKBm80-v37VBv9n6RIRGNciYuaXLnP7SL3JqtCX9bHy0AfhQWf4PIzsBbffGTv_9q1FVeIseuddz2HUP_rUc0_xVHdw4p8cDSbfjUfg-rtOsq5cOQweFZWQ6QZq8JB3aQLVJ-_fqTiuzqVhN0CB49FuxPLl-XDCZknXblHm9xjKFvUmYvVYBaoPTZLiMzEdVQbigE6Zg4ZEuczLo7Y2ra-DqzPT9UavzFGcGSYBebHua-Gx7UXfO2qbQGEaLbKrnO8fZ2iw-LtlpVTNsR9Jj0mnfjH9MKINoBd_HwjzDckvT6tbRCmmeKyD78sM4YMh2juTD9KRPi_rM7czW4KfP6_K0SGl1-Q19hA_ZYUwNrkY7vOwIFFkmCyquVqMGHbH5xrX2xX__aCv7oYkkRqT_HurXUIcneCkCIo-M9tnr8n1pZYSuys0Z3IkWpWNOPrbD_LT-mdCRYZ9oYc-9LpiVoPIxNMOvwxhHaRmr9zeRfcitWE4xbKq_vBNNRRQcKxleu2O1I7vVmN39cCdh-Vg6NyN4ZwCXMfugnlfg7EntFywwAK818A1PXXlbgi6lTQ896PVr_HcNEW0lUplwRHQjtckRylnNFjKyQd1-jL-DUwUeVVZUXpkAamvc8xoCU09eaU6ApR2Xq_SP1Ygjx4vc7Pgdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=ANIvFCwiaV7CJkIARjWKBm80-v37VBv9n6RIRGNciYuaXLnP7SL3JqtCX9bHy0AfhQWf4PIzsBbffGTv_9q1FVeIseuddz2HUP_rUc0_xVHdw4p8cDSbfjUfg-rtOsq5cOQweFZWQ6QZq8JB3aQLVJ-_fqTiuzqVhN0CB49FuxPLl-XDCZknXblHm9xjKFvUmYvVYBaoPTZLiMzEdVQbigE6Zg4ZEuczLo7Y2ra-DqzPT9UavzFGcGSYBebHua-Gx7UXfO2qbQGEaLbKrnO8fZ2iw-LtlpVTNsR9Jj0mnfjH9MKINoBd_HwjzDckvT6tbRCmmeKyD78sM4YMh2juTD9KRPi_rM7czW4KfP6_K0SGl1-Q19hA_ZYUwNrkY7vOwIFFkmCyquVqMGHbH5xrX2xX__aCv7oYkkRqT_HurXUIcneCkCIo-M9tnr8n1pZYSuys0Z3IkWpWNOPrbD_LT-mdCRYZ9oYc-9LpiVoPIxNMOvwxhHaRmr9zeRfcitWE4xbKq_vBNNRRQcKxleu2O1I7vVmN39cCdh-Vg6NyN4ZwCXMfugnlfg7EntFywwAK818A1PXXlbgi6lTQ896PVr_HcNEW0lUplwRHQjtckRylnNFjKyQd1-jL-DUwUeVVZUXpkAamvc8xoCU09eaU6ApR2Xq_SP1Ygjx4vc7Pgdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=aiWytBdEakIgKa0Y9tqa69e3EHGBqdwfc5_5MmaCkDoTAAN6OJl4UlSrcLs4247DjTqtT6Z6LtQUlL8CmZmQTgs7qjLXuiAQW7cvINbB2GFCTdAT4D0VkwZUw6oFht-jvDyVfgaIGuzcLa0nO7f_SjM6r8olRZymnpM42jlxNmfnyxEF3kEcTfn9Mb7y0E9q4lslNuEJYaY5l8oGCWprEFaE8OWhXUv2ln072Dk1ASjsHwOaU2ECRmbpuH-dAdnSIbfGsJZPHFILc4jIOaN1ezZoN1rV2zBiQjhHKbNVtymnAxXbVZWyZ2MtpSTVGp4NmgMOnB-1Xsyq26bWlew9rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=aiWytBdEakIgKa0Y9tqa69e3EHGBqdwfc5_5MmaCkDoTAAN6OJl4UlSrcLs4247DjTqtT6Z6LtQUlL8CmZmQTgs7qjLXuiAQW7cvINbB2GFCTdAT4D0VkwZUw6oFht-jvDyVfgaIGuzcLa0nO7f_SjM6r8olRZymnpM42jlxNmfnyxEF3kEcTfn9Mb7y0E9q4lslNuEJYaY5l8oGCWprEFaE8OWhXUv2ln072Dk1ASjsHwOaU2ECRmbpuH-dAdnSIbfGsJZPHFILc4jIOaN1ezZoN1rV2zBiQjhHKbNVtymnAxXbVZWyZ2MtpSTVGp4NmgMOnB-1Xsyq26bWlew9rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nidrs50NcixFPwSvHrkryu_qnPZcJqibsipd_mt-XQ_WklXOldL8jkHEI__5Ctr5HdyHujXgsv_yHa8gcduobUY9G0HfwpoFx2WE9U1-mnO585RCi6zxAHfoTAQspLlpnlAAuhjxB7A1hYeHVGLyd5bjH1BauEhuiXEIYxncTR99HR01ojZ021cI1iD0_qeUhh6gg_HJu8U-Um21J8CE5nHlNVBBC2TVALXcobwY3XdM-1LwqdErCMgrnsAJ56qLqnENhMNHnyRYc3e0gy_WDG3k5DYO3tXLNoDKMdellAJndKIUrBhf0Gwi4MSy-n7F3BJg-cNMLb1h3y7-SJzCpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okzwD-cDFc63pSBpQ_-dAItGuDdM8jitoHxvC1wgOztlSYkY_J0Qx79pZ8JO4jUnAhiFkKoqnd42EzPh1AW3CsmMrMfy0tKDu4euXOrncz_38I3SUXZiqxVgsxlzTZqHV6djU4SfjOlSRUpT6ncKtS11D-NZGXMJjIZDPIrxfa5zUQvOSJ2vm_OLrVbNUz1Hjm6gXsbKxxUrV2R3Zpck97h-yjX_LEzsiVRp1ddpKmvZjLeBSdPRc-DNUcUNYwsMWPA15EqXXHOMq5oZwnkq8UGBHxcUg2TwP126MO-7EcVZUUp4S8ExfQyAHniLkq0r8lRwD3sLsLf8noVH6Cb_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZF5jpVv9uqAOkIOcwE0Iq-vdkxvg9MYrFrIBs98YgRzGgrVseUhnv_A_fPx4FEYxHe3AyMybSf7azuK3kxCmXBwrrosA66slcl6IlVs71ob-sIZKZFpMtlqZCn_Fm_sEMwxkufJukEOsQ7hY_oEOU97aT8XoQJnTOvYjnIKs78OJ1ro1fdtR4EKo0mhC4ON_K5Erk3kIvmYGhXxcV-9Dp09-ZUH_cAF40hDDIVIK9k0MtOObmReys8wCXgPJKK5EeasAnYdkbQmYlcMxDOUABhb_YIo98pagTm1HwMd68DXIDpMODyeSw0BlOQkDZVnig45pv1UYYVWUlEotJtx2HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuFLQq6WNxQutA3zfwSTGc373U8Mkr5lZlRqkNLwVoAfCUs3QUTn5gdgkbpWj2tWgyJfjRnQjR7Ve3cK4M_So4YTGPMjefatZ116-iRbd9P5CIVUqb_CJ-6eIDmKJA5NYwSUqLsQ9dFByaMvM6Xc1X4Oc_mCw7zygUhZnzzA4A_Dxd8Q8Xg6aEyZmtvsj-WJDi6hLSMGsSLzTb7_0zW5Euojc2f3Su9v_9oU2ofd6nW_QB7IjlA7J2P9NvLvpIWFxspFau6N1xA0ouzI5Oigr1MYoINpGuY6TBhb6xngyQZ40jDtQ2JCWi5Xra2cqmB12MxRpD0qVJcNAtoNfSAMCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noGxVdHc95nQpy2VDdDFb8BB3-O8kKitBqPoaLbDdSzEc8uWGagVDuRnpdQwCz3I39q4p6H-_UgBuLJMZxKtdXZa9qHoEFfF8WqKz2Hfl1lxEZXTYIStV2s2qVNumkVdzSADW7tNJR2uxXck1L2c0VEu_AfAFzqaJTndSoyg-NnOwt74UbRRqdMYxBuPi-z3I5nTXgoBBojVR0VTBlt97GrE8qwhCBtI28Wd0zzhBZeFyppopODy_K-PgxavRJ4mco2ZeJYwJZjymVSY0r-DEztLqntt-ydEgOacKaFFdxRp8ZoNvDfeiBNo42TlKALbai_1rP-uCnoq5Kk7eakeTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMq5mUy2Hjz5F6jq5V6zZrqy7TMoAPlCeetvBRSmRcDzWCfvnFpRmCvcOfwof2nItfM2B3MiEVwp9Y09B6S-0f_6rbQr03eOkDOMQXT_fzuK0-I19EhdF5boTNQgKxuSUiumN8MIZSYJWA5xCkK6fi8VlE814tOPetgwMw6B4VrfAZ8iPbKHvBn4ZCpRUc_uOr8kRqalVEVefFdLVI7IesRLCz-LAjmux0y1SK8u02D4IhAmwokstGIUTibczyh34bwnN0tvJ9kBg-Nd9iDhEFg-LPswM62F_E8Sx2p5IBRefU8_6JX03zMCTBm_MmIu0UHscXIPaSL3oHXP39KZUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5OOVDqZ1rwQgcqncVEQFZXrzfkEs-8OyOtRGBPSk5Gx8sijJ7ribXNtTX4mszj1j-s5qP33GxaMXcxqj7HPIQQy-LAJf6Hhaq60rBaoM09o1fSRUrSBtlW_AL81xtzG4pBwOqKkkH9GDSewpQIJx74WOlVFpDXrIiqa0tY3cGUqF7H1mmuwDiRZvTt8G1cbgsd7VKO6l3uKdQfT5PEaWnG9onRhWxtX9q90zSdg6IlM-IlzXqmoUxdjRlnh5nr0gv5L2d7KwSkJbx6bI08R6_reGoWhjjVFjOyexO67hHJifX7vXLreRdMWN-U6ya84QOw-zw6WBd8DqtGAivEpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Ob1FNr4mbf9asySjKWGOeVJWXUoBS8qnJihvcqVvRujPCSd0_9vPNe2FYSSZtARhvEBnU0RTvQSn9bbIXmyjm03-knPxYwf-gNN4sVgIMzrX3JjRSe5JSBHSmaYgO_aGnDfGZB1CfQzKDc37QNOUiFa5-V_DhrSqL1vnt1dUbslC9Sr6z8neSExmVhbhX0tLlmwlaXIoaub1CQJKZMjYWlDkBo95RstK13XMQgbAiPsR-YPMGg21n7LZg-VHiULS8IhuT7Xab3OJA9n96CQrm0ogbzQtvGfkZ2VQsC45TlRc2_qFg8ETKWJmwMD73AzA4dixiY5l6N3_B7OlKjQomA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Ob1FNr4mbf9asySjKWGOeVJWXUoBS8qnJihvcqVvRujPCSd0_9vPNe2FYSSZtARhvEBnU0RTvQSn9bbIXmyjm03-knPxYwf-gNN4sVgIMzrX3JjRSe5JSBHSmaYgO_aGnDfGZB1CfQzKDc37QNOUiFa5-V_DhrSqL1vnt1dUbslC9Sr6z8neSExmVhbhX0tLlmwlaXIoaub1CQJKZMjYWlDkBo95RstK13XMQgbAiPsR-YPMGg21n7LZg-VHiULS8IhuT7Xab3OJA9n96CQrm0ogbzQtvGfkZ2VQsC45TlRc2_qFg8ETKWJmwMD73AzA4dixiY5l6N3_B7OlKjQomA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhuEEKkYx34kl8KzgE5viRnigssHebLFUJr6j95kuP5rBuFnZzVazcDyEwlxQ3YnmUkEdcROny87cld81ttstPQrsqTXV72WmOwV7Q3fkeQDR2uVWCVTaGjb9yQ-90q2JbEsMi0mQUiJIi8Ieoq2QpKyTY_O0tXry_UUiQlqQEtYVZkdJ8kOprKmHiZpfiXh056wNOLvWMWSSC5nFtJ2DJ8mqHXXxFj6tDWPXEVsMy9dlHrfmxFmI69oLiVIIrYNOZK9w4Wwx0IjkTUt-T8r-PE5qdDkBB20h7IM7E5QTcqA2HnFTGN6RXGmPWV5i-eWVX1NUMQpuSD0lmkIL-wulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=TSMflLa11EXbrBfBBEWPA-WW_dNx1yQ0aVAIDKu0kZljtrGMq_DA7xy5pi42GlHBgsC1YQFPDfax-D2pASM5m3jpW8Q5a7HEcUBEOt5uaitbAiNSoi47nrL0SGrNWSOq-mwY2pjBZJs_KDt-RidRYyGj-ADjtHmL2TvjJIdwfEs5Mk1oNvP6Ag-HQ5YM3-5kK9RKUCjEXyU5paMcrEs6Sy7kswEoQXsaKc2NuW1QxcNgo67bWOIXxewqkwTItUh7VlWF_0U2B94YZqYIRADotrCIcGcdTP_dusr4qSerw1zwMbvDNH7Z6qih8m-FC2XXL2ZFIlFYjVX2K96m-XVGUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=TSMflLa11EXbrBfBBEWPA-WW_dNx1yQ0aVAIDKu0kZljtrGMq_DA7xy5pi42GlHBgsC1YQFPDfax-D2pASM5m3jpW8Q5a7HEcUBEOt5uaitbAiNSoi47nrL0SGrNWSOq-mwY2pjBZJs_KDt-RidRYyGj-ADjtHmL2TvjJIdwfEs5Mk1oNvP6Ag-HQ5YM3-5kK9RKUCjEXyU5paMcrEs6Sy7kswEoQXsaKc2NuW1QxcNgo67bWOIXxewqkwTItUh7VlWF_0U2B94YZqYIRADotrCIcGcdTP_dusr4qSerw1zwMbvDNH7Z6qih8m-FC2XXL2ZFIlFYjVX2K96m-XVGUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HScFB1ue7LIUepvxatwN9GxUksqiPYrq_0Z5L3LvRdvFRGFfBqKnek_PmUqWojpifhaAErzyZo3n17Vs1Cxg45dIXzzGe00RKa5NC10Q0fERE3vrl-qEP9rgAkIZZ7hFqxMWh92sCkMmo60YGn0wRW1C77qBZK6gEsfR3mEoJbu5b-W-U2tikYc5rH69E1b6dInC-GKQRwiOQy9XgI_aDRDKbb0EP1TBMmrsCFonU6Bg4W_k5slf7rFx6TOq24dZvae4rdfF11dYbrSWBskDFaxdNAffmTXb7q6tN3OZ0pVn8zd4oGknDJpFR8vSJXeAUg2caSJ7zcYCr9ChCq3Wag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGGZDWAL-Pi3ENBrN2kjgoibgFuQqYb1bmFCNKpQlhGC_7eILrb28s5oObBp5h9vi-Qt9zeykm48KalDLOllBvv98ZQ9jCMeH35dfbmhdzAzE9DzxIE-IsTit9Is5y9ENedtEltmEOj0Nq9lwXRU1zvKWUbX19cOBpoFlmOeU7-R8Ql3WTGiUoKPmj33eb6_OCt_oo4e8Vu1WTD2btvECJ8NQSdZt7tCZi8WBmLAmsQrjdjlI5oPAH6lp6M6FXvO8f1hvFro5mmLgDC8fzIAnOAA7VtDSINglGZwW4E5WgN1A8MX6UaLZSfvQVgfV-BgeLXpQMEqT1h5hTcPnbe7HcjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGGZDWAL-Pi3ENBrN2kjgoibgFuQqYb1bmFCNKpQlhGC_7eILrb28s5oObBp5h9vi-Qt9zeykm48KalDLOllBvv98ZQ9jCMeH35dfbmhdzAzE9DzxIE-IsTit9Is5y9ENedtEltmEOj0Nq9lwXRU1zvKWUbX19cOBpoFlmOeU7-R8Ql3WTGiUoKPmj33eb6_OCt_oo4e8Vu1WTD2btvECJ8NQSdZt7tCZi8WBmLAmsQrjdjlI5oPAH6lp6M6FXvO8f1hvFro5mmLgDC8fzIAnOAA7VtDSINglGZwW4E5WgN1A8MX6UaLZSfvQVgfV-BgeLXpQMEqT1h5hTcPnbe7HcjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=uLAOF_Pq4QZgXSKvdbWrf82gAt08yiEKDsZutNBboRWnzLsPrHJSRNuAoizeGzXT6UgvkyokN2XwXwcJHZdCR9oB-vWfejToKjU95fqRxB_lJ033Cuxz6i1ytYIuwOjKVQjCq40smjs-WmewPnpKxXaZFyJMZfaMwAeQFtQzBNLky7dkZqSc82n66OE-PhbkPFvHxKKyH-XBMK2K54O7RAJpMZ5wSOLfFW36fKZ5ju4vHELrGmeqoUHUpaHF4nxDgJ6HIBwoRWmWsAfk-NnxTgFzA9Uhjq_l8cRr4cXfjyiqcps9NhizayxeCNt149foZsqcYyKWpLZd9snRC-uBdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=uLAOF_Pq4QZgXSKvdbWrf82gAt08yiEKDsZutNBboRWnzLsPrHJSRNuAoizeGzXT6UgvkyokN2XwXwcJHZdCR9oB-vWfejToKjU95fqRxB_lJ033Cuxz6i1ytYIuwOjKVQjCq40smjs-WmewPnpKxXaZFyJMZfaMwAeQFtQzBNLky7dkZqSc82n66OE-PhbkPFvHxKKyH-XBMK2K54O7RAJpMZ5wSOLfFW36fKZ5ju4vHELrGmeqoUHUpaHF4nxDgJ6HIBwoRWmWsAfk-NnxTgFzA9Uhjq_l8cRr4cXfjyiqcps9NhizayxeCNt149foZsqcYyKWpLZd9snRC-uBdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4Bb9yYRCisipXLoprGu1TFbeJFpjWbrbtjkBZUWjn7ki9nnqkFoGAnpk1-o2egscPrUgavlYZ-mhtskfCsNNAqTZvRJ9gwaNybQOeAkoYGHGLTV1JgBwGJCL_dwXTTILXex31DIWcfqkLhHNj0xot5c7p7jzMG7FpwNK2BhA3KoAxPCOfNtQEyKVEvfUDVmlY7xbncBXs86SXSWUHYlcEcKgXFlbQEKnVfgCFJ5EzKCsXeSuXfTQWVf3HJyjMtY5UXJc3tjqr7ee-JTo7KpGrb8fs4dRa01xBELCefrVuQUD40gzZ5TsejNy4CfpDJuXrb6CMOSZNlBF5_gnlTmqzjFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4Bb9yYRCisipXLoprGu1TFbeJFpjWbrbtjkBZUWjn7ki9nnqkFoGAnpk1-o2egscPrUgavlYZ-mhtskfCsNNAqTZvRJ9gwaNybQOeAkoYGHGLTV1JgBwGJCL_dwXTTILXex31DIWcfqkLhHNj0xot5c7p7jzMG7FpwNK2BhA3KoAxPCOfNtQEyKVEvfUDVmlY7xbncBXs86SXSWUHYlcEcKgXFlbQEKnVfgCFJ5EzKCsXeSuXfTQWVf3HJyjMtY5UXJc3tjqr7ee-JTo7KpGrb8fs4dRa01xBELCefrVuQUD40gzZ5TsejNy4CfpDJuXrb6CMOSZNlBF5_gnlTmqzjFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1yfqymlRpqCg_9uJ3NfG4Y_Sdup_UPus5PM7Mec7tQXODERKrvKCEFej5o72fNxxEXTKUCxYowR_AOVNKnDDECRUDXBHGWLzcgckEFn0UBBqqQX206vYELr8kxTbg7mGmkHjnP-7JBYLAKMOgGOh7KZ9IdME0JUCErXtz0IZWGWmwpd4kZ9gH_HCnsYapxdgddWavMHUhzJe0GnGiF4FrB9k-0SdyhH2LvsN067FJPU9lDCG9vnJky4_ih2Uui7wh6WJbNALcRxTyPpR-sn-ViykHrSGag6WJFG7ZyBdChfcrahVa5i3ZTiER9-RuWonkbhfdxzy8L9lY5ANK_iaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPKwUXCNBDJ_acIrro0oXtqEMSxMvAPs3TnarPfY4pHOuyMHyhFwACgfecixAGDRyF3YuKnGrzQQxLTVO3IZUYpIQMJ20XACG9RbNkQ8NzM5FfdNL1aQrmVe4WR-lV92jC72-M3-9wxvU-uZEgjhmXhp7LCGkYj62CJ_lYtrcq81J_u7kC3XNRWzAkGXtRxTA2qN6-3KRGRevQ1RgckIREgG9idVH5aslSK4ywTAfF9FcF_UV7mooNVBfjZ9ntLfsVaVI66XWk_oQlpbzdSpwoeJU6O9PzdA6wg548-mOBdN_kCFkRcPr6w3SDbe8WhSd0qfsGhrjgS5rSj5BotN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dITKUpEWXZnsCofurJnpDj7p4B8a79ATNef3KleGD9xESrVQ3qarz3UpVn25UsfSn8XFigWGcSNnidnO8Whukhf5HCxIIph7ot5tUSb75UjeTMCD7IRVpq06RZCgI8Gu9ny0nXTYTAz9RYtPEba5k01r7vNx3UQaSqZrmEYtYHA_v76fi7mwjWZWa19IAHJ9BqRsZUTJ5_4WaHoNNyyU3f24RA6ihxaKHrArldvfCH5uOmfQAVy-cd5IjiJqsLbhIGve2NgJM0qDo_0kr476pue3FrobRYXs-QS7H94IfW71-RGF7PKNt2g_hUTcYt8X7wWPrRIlU5FpIx4LQUr8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1qWhAljAW2hcSEXHJA-PGqMfTIOK7Z4YI48v7nPt-CIyupuKvx_gnD-N6pp-WHjTh18saYQJy1HguJQdhz_2SQGS2QnCcf-cjXnPg37s3L5yh1cAEqbJll-fjcrkRittGIzwJwXq5IML4aipxhg1ct02TODVjmIc2jgARGLM8ULNo1tm_KbS8LwtfWLsdRsughV9t8ZajTOqLuxYtZEmOznD3BbKty9Vucuat7Fp-OZl4Z1AMbFATxfI4VjaNcY235jvfaLDLfyackKvFjOd95w4Oh4gTX6jdlck3kyhSHRr8kTl_Ow3qVG4rW1WvrszvQE4F7oLZs5BgpvdHFx4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qO8fVrPoTWWwQQfnGLxUrnpstD4749l5BVFtSdjN_LLEb38beDXSUmk0yMmtCTYo0YW5_RNhsxCx3oRNa697yTjazJLhqShmVAw5kEeWpVvDFPbWx3SYrU_7sBefEX1Jr_-xsb_Wa1K_HVZ-5b7fCPJLZeUmY_Ihb-GF3RqbXAj2f22JLt1evGBjKAkQIBMBmGXUwUxsf_KE7DY0tj8Ev0PDG02sKDFY1VuawjIzy5Rb_kdcFfclOg3H2H69RqJApNmL32vNgcH-IZRdEPOJ22oJ-GLB8KuxYnUcaJVo1kT8t1RAnAKFXVzlqd4ZJip8bFsGHB0FPs1xV3JoBeJdHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
