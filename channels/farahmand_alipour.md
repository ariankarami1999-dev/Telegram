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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 00:04:08</div>
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
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGDYdVfLT2yjxfrmqpU3DMHcE56lmQ4Mld9YSZbGVAIVUtXMrU8ZVIFHU9d4hVRalJIzgI9QwyDmxKzNbc3uksUYLSZUC3ZFuQB7CNKWcpA-__ZT4CidkjrGi88IY2s-qodYOScUyejpnkGisClSI7MwwXW1tHeAi6hDyoHQM2azpN0uHPKMMlZRbYwePfI35esvvmvEFIpC_jKSy2rb8ezcHOaXSwgRHqzUlF7ZRX44do5uAQ-XGaOU81xnSQscg7rHtmw3qv_VicMLhhiS3Ye5N6lxDd72wv7RgxAUfvFtaJRbmKy1J4FAZxX8p3WAmJMZoCb-SiaBio44sTsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InUHe-PMLaDx2K9scrvuaCEE5PMmtEv8j37YKAZSFPQeYLWt5YaapkpmI37vouvGii24xDzgum4OdblYGtxXTrlyaLSj43f92Gty6MJln0MGdUxbl5IuZHZ-55D4-C4ZWxwsOu5gjXAoi9bgOp2ekfoGhslblobMxPPOplyoD3PDUfcwUbiELl6XSFaXyWUylQF32ZfInLOY8kc8cBPOQetViZ1avsB6gkpL4WwI_WFBGYsINNYt8gkxhMLZdHSyixDvYj-fmHwes7mJ-0aKPfCDkcc5OxKC5-6PxfGhzj1CVxuSCV4r_dGWSBANrPwcUrmvwCMoEdLRm2fNoSBBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aymC11W0__uqFaytzSgWkPXJ3NGVjEm6fImTas3C8T3WZLKCW7MO5OodyXdx9ouBqIAakXzZsUnsNl4K1A7f9x0z3zecSTCA5HY8BUJfO6UAJhv1OOQZ7rcihNiV8oDynYxyMTA9ZBEfZvYYpXt8B_JfnI7lCwp3PnIJB_XS7Jcw8KZLCfwjKP5O4unj_gNfDIoDqFu4vuITDQBsWab3RsFhKZhABCupEIFRiErLfCmkjKD9c2vqN8tFrjXeGirj7k4YYtY7dxI9FeHgsvhd6pSNx9LbGJnSnpdT9hhQCHPxo_YERl0Yap4qBlwuiq0pzPGzxpwxYATiPz2r7ixXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriPk-JmyG4OVm4p574OCN3_Spm1GBWWe3EnlthafTncF2ykA7pTo28rVV_IizawVZMpAeO6WlhUVwPe317e9m3pip9k7-FJTB_sf9a0thNxQoGAUQfeRgaUfBgzYA-fP3sKzM6-FzpXKtUq-SSgu3iIXCvrCuHsL_3Yxr3J2WiNdbmqJx_x5mxjtOs3tkoc0CuNhxsjbNPO_7v_3JaKMoIJdk15bg9RN-wa1M4gwuBVf5LSgQ6faa2tL3Erez7f3u7bNr2LSjKXX3qtwvOU9j8_jWbzgRZplC1x2L6Jf7z85Iwd0uP6rots7EgZ4W51YueymtTvSuRUAjZPn_QSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov-5teW3tHTvsvSbgMdLICYXYlU_sDGIu9OuiTSl0594zrfs9gRoJQR8S28V2CiP_XCjD7Zzp5uItinMqAUIbUIRvVFn3zxxaqYh9Km-0nk74uSUdeQvuMYluMHfHS7WfmU5Mq1R_o1vTjHKfD6MlZEq2Yf9KVRt4d2gzoWcCctXxlvrZ83-13fvHD4NvwcgSfJHIpLOCqzOAdqDTCE-6frq1o_rpZ_dr6FZtGyKaUvR4uN5aL7iKlIR-aOJwWaAcP_ZJcq4l0tyEkcUu7cd1nNA3Bm7_vFPEyFbPsYQr_SdVeOSm92Zw0-QEekuDDdOwCr60iw-tbsukbzrBFNmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHVVCza4-k7lMKxM3gRJStW0mSmbHx1HOC_kqRItxfPQPZo3RqgLfbxvjky93wErqiutSbOoRDVDgJO6-5Gt5GeEQYp3ZpC8LbmHHVvogV5fTJ8tjv9WUtzfZpz5NJscTMxYul7zKui-uhcGtGwcbJz9kr1kP6yA61rGmmeIOf2BDf3B7TQdUT7ccFphzbXnhtP5luogZEm_0Gi7-eRD7KumLBDmDBfFnXn0yVHUWnWFFsbkQWbKqce98C8p4SF3LVslyiNzTK7TUUb1kdRXw9U_E3m1dmBOkEfxlEWe_yZkhLuLgJrZdcC01kX5yYjphMbJYFfm6UDxnofukWHSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4e6B8cLTHOFZLC_QYWCJylwSJy9W0ogC1kkRdY6btQuH9H8CxCgaa_B10O5ewXYUxmKpJiOTN0Ok1jOwJzi0kgotaQ_2jf9b_Y5lklIwH1mMX9jIZqCs-epIINGw6Yx4PIe39KvGuERRpop0rMJzGtI_xUPz0gFzFQcBAm60EllibNy4qfoms-3jmaAXpr3mODgfU-TkPoqkbeC_wKoaxzAUUJpquRW9VB3eEMGor6OxrZmO2GWGGsilZJVFP8KpTQ60nU37QY7iTkzNHw0mzJ925GZBZ8_gLXhUxvi0Rb0kUsZY6BSvIAEyxdJzyaFGbTkYYq8rukWUxmT8i05hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3cy1W2TbhAEaNqko-LkofOvGARhOPamsqF0vCHGyMTA7VOKKvkblmGFd3Z1Cmu624_ja_tAa8n_bbjHmnVTuhNxKTyUxVAacVcYG-q-bRFg662UE5Tria8Te2IEuiazcF5nA2jXoZYHbcMMvjn7bJRAgoWnuSmKAPfMRR3VWB-izE8iOD59w2umFAgheoI3F9cBvPYJO12pwPuaKptJ7YQSh8wu3vjjT20WB8oaFhMleR-Rvz9k8qJK0iV9UMgIccuu8fRJNoDpaVxYVJ8kU5i-VJKdGxh_NlssZVWq_v_rSGXU4LXxVobrRtTg0YWElxLIttczbSrrKRw_7LA-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBx6AymvCRxlsRVjIFwhgd7sIFxY1LGATWVlsrHq5kuXp6iD_JJNFsTQ4SDIvWwwCT0_8OSfP8y38ozvGXugWD6h5pjQRSSmEJFKeOGIp19kXPO_l-dvp4VUA2LYi9wnx_Xgp9Pn-4jCPGrvtTJHy0UOPZkbaKLqPfiWPOcp525oOJseB0UB_lt061BUjOYHcGJkSIsdfcjuJ8UkzZPrd9VShi8sp0Q6pfPJkvxET0ss-mG6F9H3jhFo54nsbWvQg0xz8zaG5PKqqIhI6hFababkC0DQAGyuabq82BgmVYREwAALWpgd1yqzCXfz0615FadGpERgcE_n62ePwQPRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=JT8KZdtP90FPsM_jGT_iKSAa6aeRP5uTuGI5pLfOqNZhRCLD8dfiYvpTK-2E5_G8LxDJQO4MJNPWEI1zDyWDfq4woB4aBRgCwtil_nfrJOYr65YXgkt4FdTyhROXGbF-_3wPCDMpkPmWzhK1rA9RclmymSVNmt7cUtTQ8Tc7gw4L1-8z_Zd4vQHE8587rzVGE8DOSKEzxgD_zt2WxsRUvT_z8XGXIaQkJvMcA7-894dfc_fv7GRO3NxSsdx9y6VSUuHWWV0Z563STJViGykwxYLcVMohDjRrw7Ortz6zgi8jrN6ovMXCnjk9ZXeZ47_HF4LHey2agWSEELv5TZY4hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=JT8KZdtP90FPsM_jGT_iKSAa6aeRP5uTuGI5pLfOqNZhRCLD8dfiYvpTK-2E5_G8LxDJQO4MJNPWEI1zDyWDfq4woB4aBRgCwtil_nfrJOYr65YXgkt4FdTyhROXGbF-_3wPCDMpkPmWzhK1rA9RclmymSVNmt7cUtTQ8Tc7gw4L1-8z_Zd4vQHE8587rzVGE8DOSKEzxgD_zt2WxsRUvT_z8XGXIaQkJvMcA7-894dfc_fv7GRO3NxSsdx9y6VSUuHWWV0Z563STJViGykwxYLcVMohDjRrw7Ortz6zgi8jrN6ovMXCnjk9ZXeZ47_HF4LHey2agWSEELv5TZY4hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9enivYmrlMKzWVz0sfiexlg_8ALguX963rlFk-vdGutrMM9_zf326fYXBeBKkl2N4RZcQgg53AY8ACGVZ8TjZc4lFBw0d9qHCtQSAHWNw-r8xMhX9swzR6yFyN8vwZ2Z-YAH4RzKSTLq_7cfuM3Y399OloyBYav9vvbQSCoO_lE-zxS11btK76JUGChduvzO1SVj-qit6m-aGcNb9C-BANy8hGmwRp9cWnHMhcoiafb5zNSKYamYamgT0j4Vi7zBbKS8miB3q3TGrJfWnyiE9ZjTsacme3ufYS2NRCFy3xEYUoilj5E0yJ3y2fOOtq0tvnNQrja6b1MM7to_q2dfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgUK_NMpzrS8xQp9xZLB4NaEe-268kbUk9gj-nN7fMZqRiSJmxHSMyn3tJAC5i-dibl67Bubi83XTRczsN5cjtAE-YdksrMctU0W0uYiXqOqsx_-B5G_RiyNDQz0Qhms7wegr3bKEUm_VEsoBzmUYQECcRQNpA0q31GvoCu5eemWcLeEylO24TXlQCEUye_r-1uhxzVa52ISmqXcegC0ylN4LCJNLhDBqBPooH2a1XE42LRqi5HwCjHeV5Td1lR_p_2gToLPSdKo8nB3kcIof8PJ21HuQk1spa3ON8Wg5bZlgydO907Qo923q_FHAwurJOqDZacCt7mX83OfdkCUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5Mc9plheVxUuvONbPNGFCuPxmnT4gV_qvifNxDjtQz5YIHqgbKKHD2skC6WV64aWkq_PJFrmLXMJYzs7l8kOoBVkkTXKLaE23XWXRRQht8jWYeyMSe9NI6sGFlhIOME-SZ96VgERvwdb-vJvd6VXmtspUT82T5n5rJhjbcB7a1bzHP7iPMGAp32s_PbZ2iRvEfAUO8InGM64GgZeP6bvQ3vpuYuS39iDxnHeG2aO6mV3rmAhfRKhT9VkgQa-PJu6REtL0J8FOtLeBhaDbmaFOhO9noNJ7ujRKtOG1B2oSQ4LsMSiFLi-L2bQ8sMpOda1TagWIaSYWeV-tPpcAJgvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAJtiEzLyuDN7_Za8rR2G7jequ0xAMNIB44K4yefrZc1bnbs-ZhYN5ntygdh4ucFvfATgkLun7om0qV8Sln3n4bdvO2fJG1aKhL9Cjwq-6fu_CBYcp8O1cP6-BhfIpfjKaYAWVrpFLYArEM6SEOBTw26lKRLUeqyU50cwtpq1NfKQO76QabGf5qALjHaHaFGZqBw9PITJtViLu1qFbxPuRwCsF3iySdRgl1sNi7gNgXxkRRpttcbsmTvm836z1tMIY8sy-wtuwHnGxfL3FgfW7L4QC6JK4v8lMtcZzVUSqYR1QvOsRdmP4uafNyte-t6Z3qmJg3qm3aSrcM5vclHew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=svTWvY58ScZIVZV_HcMJWUm4rsEn5vkut1IKf5Pe1Fpx5N4nuEPg5JTCKnEdtxRhQVp7aSiM9_UFD8QResGur6Vogmarg2YdcF9ioRQy0eANc7r9zAYdrQGwcKLpTNDfwQxB3mct7ImQEzdwYpXgjXne741PDVYPNgfVLXKrc811oQqQQ9-skSV30dt6FtOl2OS2ukwrpUX-uq04QY7eHwsC1AvzZEsmsmpy6y-uKorAOpSuVSVKxzYnTRSZMgV6D0XZh83jlN1OB7SLUbHYnpyfHwmQSmdIa-l1uWj17K1L7UHSPj6G1I8woBLPIbxMC2d8GA76m_k9A4sHYAdggYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=svTWvY58ScZIVZV_HcMJWUm4rsEn5vkut1IKf5Pe1Fpx5N4nuEPg5JTCKnEdtxRhQVp7aSiM9_UFD8QResGur6Vogmarg2YdcF9ioRQy0eANc7r9zAYdrQGwcKLpTNDfwQxB3mct7ImQEzdwYpXgjXne741PDVYPNgfVLXKrc811oQqQQ9-skSV30dt6FtOl2OS2ukwrpUX-uq04QY7eHwsC1AvzZEsmsmpy6y-uKorAOpSuVSVKxzYnTRSZMgV6D0XZh83jlN1OB7SLUbHYnpyfHwmQSmdIa-l1uWj17K1L7UHSPj6G1I8woBLPIbxMC2d8GA76m_k9A4sHYAdggYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=eENzkUfIX7rBMxLn-3qSKAzhfJVI8hLofwi9KwfO_SSfmHnZ1IFYbSLm_kiMaqN4rEm9bPPYA83tofgGqGskLSjTW9gb-QMfphU4OytaF7kYYiwnF1lhXbcnl855zKfK0Uc5DD3JsoOZ8NZNrds5GuPkCr08TyEODM7deXulZbWBIm1bAGq6SdFQliNrrcU7IKEq4dz3SxxvCqXHhwagHwHExKVSsyIT6-zgMOFU0HJ3TVBAGncQttGSKEPylgipvJpk1ol6ppSWz95wC9aS7y56_Ro8JHQC4_EXydZCmKN71tuS4PSfm_bwu6uGAjzJxFPqCPw_SWoXGPX3_88l8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=eENzkUfIX7rBMxLn-3qSKAzhfJVI8hLofwi9KwfO_SSfmHnZ1IFYbSLm_kiMaqN4rEm9bPPYA83tofgGqGskLSjTW9gb-QMfphU4OytaF7kYYiwnF1lhXbcnl855zKfK0Uc5DD3JsoOZ8NZNrds5GuPkCr08TyEODM7deXulZbWBIm1bAGq6SdFQliNrrcU7IKEq4dz3SxxvCqXHhwagHwHExKVSsyIT6-zgMOFU0HJ3TVBAGncQttGSKEPylgipvJpk1ol6ppSWz95wC9aS7y56_Ro8JHQC4_EXydZCmKN71tuS4PSfm_bwu6uGAjzJxFPqCPw_SWoXGPX3_88l8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=AUpfvlt3dTnOmo8Ncq_vetka1-umrFY-B8nGtsWUZ797a6hpNinbkMMzGODMJ_nnIhIiedpEXdi1DsiLwSExqVMsN4lC8WWGoTuCPgodHOz778nJToAf-naqUFgfs00I1ZAh1WQG0xRZTt5LBjFa_OnOlj-b1BVqhFCF2Bx93YW2-eUyKraNFxzzQuUO5Tx_BC6GY1ribYwknP0o0lVt8olDZwPbmZHlekfK0ry__-JSggylvXTqbXKPsHMS11uoO0-uaotGRoq7lOa4zhn82YxcXNot7V1Jo_McQhzZrxeW-YTvh1qqLi2JyrNEo2D0T3Dnb3sIeZEL7P98swn1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=AUpfvlt3dTnOmo8Ncq_vetka1-umrFY-B8nGtsWUZ797a6hpNinbkMMzGODMJ_nnIhIiedpEXdi1DsiLwSExqVMsN4lC8WWGoTuCPgodHOz778nJToAf-naqUFgfs00I1ZAh1WQG0xRZTt5LBjFa_OnOlj-b1BVqhFCF2Bx93YW2-eUyKraNFxzzQuUO5Tx_BC6GY1ribYwknP0o0lVt8olDZwPbmZHlekfK0ry__-JSggylvXTqbXKPsHMS11uoO0-uaotGRoq7lOa4zhn82YxcXNot7V1Jo_McQhzZrxeW-YTvh1qqLi2JyrNEo2D0T3Dnb3sIeZEL7P98swn1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA7AV3sM0YW7jzXrUMtqEwKlCjb--U-TgG-PYlzN81hmef7CS0XjB5vlbJLQcrtm8BX04bW9rzJzpuuoxrYZbNENs3yKrOqMZyrnyzSTQxa_U8_B3QhP8-7xvPphBXLCcB_M45KAvoW6kOOuhHsENgHlk2PunktmrF6JN5VGemdMa3ThjLl2_931fA8nUj4pgeY-lyh_kfRKAmPEgWOoI1RqYoa_xEFBNFvIlOhs-eiV3yp5gJWapptfJAyi5DE6HYZe_C9sYRpOPygbSEYC_cIwUAOT_hudddvXoTrronkeXaRLcCtZBzLlDescjuUpN7GoljrIotz6sWIGLTNyzQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=n8u9ghEMik0gvZRZY4pAaM_u9e24gAEwrxWYJm2E1VW_qTzLsiUp5D4nXAu4-1t8FTxcAgG6ilamKKofkDZf33wFtS2eLEmM4xLgz97H-DlnWyN1szWiMpL-P75FaI_yCJpARYtVsBI2ztcE8chyLf022yb7YKNpkkPGz6GCA3KS0dE7OmoSeqb-E2s3aXO-XBtLE5a7eRZirDxNf_NIQNHBvIvAoyYnblCs08lJdS9liOkwhtWvKUNJEUEIBklR8JJtEGQDeQMHdjdgD9glH197HdGu4-xbcFxn87CD4IFaGw8P_KjEaUK0klrU3aMrkKSqJ845jbDP9U093r2D3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=n8u9ghEMik0gvZRZY4pAaM_u9e24gAEwrxWYJm2E1VW_qTzLsiUp5D4nXAu4-1t8FTxcAgG6ilamKKofkDZf33wFtS2eLEmM4xLgz97H-DlnWyN1szWiMpL-P75FaI_yCJpARYtVsBI2ztcE8chyLf022yb7YKNpkkPGz6GCA3KS0dE7OmoSeqb-E2s3aXO-XBtLE5a7eRZirDxNf_NIQNHBvIvAoyYnblCs08lJdS9liOkwhtWvKUNJEUEIBklR8JJtEGQDeQMHdjdgD9glH197HdGu4-xbcFxn87CD4IFaGw8P_KjEaUK0klrU3aMrkKSqJ845jbDP9U093r2D3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=gHkACCcQzImX9rPfH_W65G6JwB_6sESfN1zcuXzcPCrd4Di8qNV4N8HRYr9MBJ4pI76AfUIjXRgyWahh3kpykJHKvfywXxTciPsVT2BrMgG2CsL-lGKLVnZcXKWc_gjINxYaQEWzv5Hxl0mMiMk0ve6XwybIZEPlAaqPDsfcUev8GXOJcFO39zPAnZUioKGZ2NicbzqTJhf5JZpfxzxOMEsBRy8OP-VcGjJ8oK_0uLwAYj6gOK-I8BXAfSy6l2Z0kGphbuqqfXgrnamfU23V6mqEH022aO5bmTCgsiWHbRMcTg3FfcyASgn8fGlNFHzsDhmDn9yDniBJ_QN0ywQ1Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=gHkACCcQzImX9rPfH_W65G6JwB_6sESfN1zcuXzcPCrd4Di8qNV4N8HRYr9MBJ4pI76AfUIjXRgyWahh3kpykJHKvfywXxTciPsVT2BrMgG2CsL-lGKLVnZcXKWc_gjINxYaQEWzv5Hxl0mMiMk0ve6XwybIZEPlAaqPDsfcUev8GXOJcFO39zPAnZUioKGZ2NicbzqTJhf5JZpfxzxOMEsBRy8OP-VcGjJ8oK_0uLwAYj6gOK-I8BXAfSy6l2Z0kGphbuqqfXgrnamfU23V6mqEH022aO5bmTCgsiWHbRMcTg3FfcyASgn8fGlNFHzsDhmDn9yDniBJ_QN0ywQ1Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=bBGSCbegMkyLefPVG-JHfJuy5xecAz6L0PFlkZTVrbUL_Z2GnPj_5_0RN72M5AfllY1RylWFuLrRQJT1Gq0-1aDx7k2zWuImv9SCEyDRAb-MZVtpeZZh_F_HDxH8Km0a1DrBgYzMKw1EjTb5poWtmWWrL43zqhuHiocYQAP8-DyUR2QItIIHjQBIq8fVbhz58TJnB4CdAHXYZQaPbn4nd--o72ADNQSv_FD3pdP7iMcAbmPoIC48y-xc6kS0_7qic1_1d-HB3n53YkZPY00CHiD_20c_g72vk0i41Gk-2z2sEmZL08osA9-iSBqpWqOasbJryFVtyNMaIs9qXdp-WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=bBGSCbegMkyLefPVG-JHfJuy5xecAz6L0PFlkZTVrbUL_Z2GnPj_5_0RN72M5AfllY1RylWFuLrRQJT1Gq0-1aDx7k2zWuImv9SCEyDRAb-MZVtpeZZh_F_HDxH8Km0a1DrBgYzMKw1EjTb5poWtmWWrL43zqhuHiocYQAP8-DyUR2QItIIHjQBIq8fVbhz58TJnB4CdAHXYZQaPbn4nd--o72ADNQSv_FD3pdP7iMcAbmPoIC48y-xc6kS0_7qic1_1d-HB3n53YkZPY00CHiD_20c_g72vk0i41Gk-2z2sEmZL08osA9-iSBqpWqOasbJryFVtyNMaIs9qXdp-WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gR6Fzlj6Bwcwi5SvfCnaTwCnMGtN8lcp9CltmGfnTspnXBtxy9RbBTSS6FMzxyKzB5IedfC6ZC6Hwb84eVYnI4eT2wCS4jEYi1SqqrftQ-GnuWO1G4ljAsDeE1mOP1_cNopj8dwNXe0vXU3P2-wmtU5HWnZuNbwzi9a6qVIuK7ih5j2avvACAAmF2oCPmxj_housWlA2eTYEbea2rL2Mfs5lVr-pV35vWVtUo8TKX5cJxJQ2Csptnh_kH6ZmTyOTEnJXE1Ezd8fUtrkqWUVdV4irJuRVXNFjZTpisrrdRmpIhGjSzaMjsGnfRA-naHgHv5ryDk39_HwKeuta1X1Dl7YvFBkLBFh0wpaJ4qOXFfZwAkc_69iZpAMosN_uD8aQjI2f1WCfpONlIJZAXVS0hNZXJ6i5fY3zhaFXJ2SDATiEmjoZaIKWVkukUBqwS6g-gpapaQojxjmqmv6nPMnCiWTcU1hFgWob-B6GPBVjzD0Zxuw9ESKKhLTslGf2I_0uYRacOJCbGhjSxD-DJh26c0-p6HGtM24GZj3bBQSxir02EEroZ98XZWOyyv9L6g9bRjT32HZ2IjCDQulkAvfs47Fh_fnF2WDRPELbIJVQqdZQEZ3OM6gEvaLOwUpzLAGX1m2AS-bi78caWwTC6517U10rOypMLufWgSaRi35rOso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=gR6Fzlj6Bwcwi5SvfCnaTwCnMGtN8lcp9CltmGfnTspnXBtxy9RbBTSS6FMzxyKzB5IedfC6ZC6Hwb84eVYnI4eT2wCS4jEYi1SqqrftQ-GnuWO1G4ljAsDeE1mOP1_cNopj8dwNXe0vXU3P2-wmtU5HWnZuNbwzi9a6qVIuK7ih5j2avvACAAmF2oCPmxj_housWlA2eTYEbea2rL2Mfs5lVr-pV35vWVtUo8TKX5cJxJQ2Csptnh_kH6ZmTyOTEnJXE1Ezd8fUtrkqWUVdV4irJuRVXNFjZTpisrrdRmpIhGjSzaMjsGnfRA-naHgHv5ryDk39_HwKeuta1X1Dl7YvFBkLBFh0wpaJ4qOXFfZwAkc_69iZpAMosN_uD8aQjI2f1WCfpONlIJZAXVS0hNZXJ6i5fY3zhaFXJ2SDATiEmjoZaIKWVkukUBqwS6g-gpapaQojxjmqmv6nPMnCiWTcU1hFgWob-B6GPBVjzD0Zxuw9ESKKhLTslGf2I_0uYRacOJCbGhjSxD-DJh26c0-p6HGtM24GZj3bBQSxir02EEroZ98XZWOyyv9L6g9bRjT32HZ2IjCDQulkAvfs47Fh_fnF2WDRPELbIJVQqdZQEZ3OM6gEvaLOwUpzLAGX1m2AS-bi78caWwTC6517U10rOypMLufWgSaRi35rOso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=ESWzEmQCFbNGTYCzOguuOo8SEbuPLjHwr2AmjIBkPHrjYAg3nhz7lIaverOquEgTOc2cw4cLH_0vSU_eB0wrCMUkeqKQgU_Ohs6VAzPzb0iFngZYN9pkjN4xMc4Zcx51YhDWoivos5BmIT2ROyn81es7nUeF8XCVuk5gZT3z0mqRw-hn3pGN9MJHRxM91Od8NqzfsRw7i2wIk5uDsw6olEV4z_nJ7ctR6s8BHn6ljrg2wd277Y0_k2geu_g7la4udyXMfLj1ul6XJndCoPtwrPPyue5_O5PwbmTsOOFb1b7iYP83jK8g-vOBGhtWcYkvMM6AH7rA7nQqFtVfTrxkdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=ESWzEmQCFbNGTYCzOguuOo8SEbuPLjHwr2AmjIBkPHrjYAg3nhz7lIaverOquEgTOc2cw4cLH_0vSU_eB0wrCMUkeqKQgU_Ohs6VAzPzb0iFngZYN9pkjN4xMc4Zcx51YhDWoivos5BmIT2ROyn81es7nUeF8XCVuk5gZT3z0mqRw-hn3pGN9MJHRxM91Od8NqzfsRw7i2wIk5uDsw6olEV4z_nJ7ctR6s8BHn6ljrg2wd277Y0_k2geu_g7la4udyXMfLj1ul6XJndCoPtwrPPyue5_O5PwbmTsOOFb1b7iYP83jK8g-vOBGhtWcYkvMM6AH7rA7nQqFtVfTrxkdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=fPUjXF0iEpz1ySee82uuj9avfZx958FDBqAGloaQKp12lhaqnXMxtl9MQGyfELE2G_Cjh3L8RZJiwTb7WPNJIVvoxq1j5nZueHDL5BS1qiWodjDXJZOI6f8wfp57uYlgOhZ0vPllHlxSAhpfH0NZ_F_ahMhZL0VBNh6L3x_G2wgsae0faBS32UhlwkQJJID1v6RK5xzOEwGjO8jss5NDNiMsYISIZFJ8VP8L3GLPJPx4Y0tWhwjerDCluNYVpKAmPd6TueQq8UfTRBtQ8yhUlzFD42_-sUiNe1v8kipk8cOVJkSmU2EPBqbBFQ_z6NAbVwt_ttQk6HFt8x4n0fJBqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=fPUjXF0iEpz1ySee82uuj9avfZx958FDBqAGloaQKp12lhaqnXMxtl9MQGyfELE2G_Cjh3L8RZJiwTb7WPNJIVvoxq1j5nZueHDL5BS1qiWodjDXJZOI6f8wfp57uYlgOhZ0vPllHlxSAhpfH0NZ_F_ahMhZL0VBNh6L3x_G2wgsae0faBS32UhlwkQJJID1v6RK5xzOEwGjO8jss5NDNiMsYISIZFJ8VP8L3GLPJPx4Y0tWhwjerDCluNYVpKAmPd6TueQq8UfTRBtQ8yhUlzFD42_-sUiNe1v8kipk8cOVJkSmU2EPBqbBFQ_z6NAbVwt_ttQk6HFt8x4n0fJBqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDYzlad99D0J8TzlGnF-SFl6SeQc9hqRhPPUHmUcdbD_u79lxalm5EdOhT5XPVGec2yX1LqOrY71iAlh_RttgbjtCBL2Dtp9rje-ufumBvIbnWxblnVyL6SIQRdxfQrSWeJrSALbkuOOjYt9c6lC3mM6c7WEj4Fllj2FLg7JBayWt9KJPHT0xL0_F11-UzWW0qA6hYtlNXuz74UDTD8R-oQYTrP5_lXxz0JvYHX27yKu0VD1BVrrBRJ6HGId6HBNhWuV8v6LkkkJnHH7-NIX89wC18lI7Ykb2E9B6QdcTfP2yzpLcLIwWJq6G-JofNeQ8YQRxsUg1TiTHFUCg1hoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgwBvCVyoQImA5GvQ9dmBW_ZBfZPwojNPwRqWh2Cdyu58x0jp2rtcvhSpxvC9QOSk8WvX-rWprgGySEhMB3bRfF-Pwt5mK4292YSJ4dyTSw1_xtom__BV78quVFNhCZVRmSsRIPtFGlF60tEEtzQ3bukD4zT6i7riKtomvb_KFb3qdGTgOY9PxIH9CSB4txAPARHgljrkc0sJZ_33HkfGHqr7cBs8Ip7V5Zp0ke6URoIXkblZ46b1KkEkF2zk48B76N2e2W3ckPv8Rpdt5NmlIFJ2DCVhTbMrT397d1GFbdnjvFHUSmSdkt0uu5VrlZAMPEPDBK4USuYNfGmelAaxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Xf6kpm3iJ4ZLXqnHbztlhTEnaqH4oKr2QMQkjyi6hcdz9DeYpL4AWjjJbTbNRwNk_2kq3MbXrem44447FlN0PuGdqc510eefTnCb2e4Z5utQJzilKBLopvlHHYwLvYgW9CP2NYMv1oJInrThH1N-uuRXwo-m8oUb6CWJIotqqVmluEMmnmxTCOokjADZWdsdy3GwkPGLvwDh4FVmdeL1G2h98bIn6fg015q_g5-6pHeQQUrkgKQsCJZDTsbQezAQkZGzra0v7Z1Pk1BwYjaayq9wk4bDnWFqQKDjt6RP76m184O6874ppmkqHQ_AVsa8qyH0QWd7IwbbkaRHFJdpr2MFOY5d8PDXsjGc1v0Z2pS9SuKblyKAZ0L4oAQwGQnE1YB6B9huCJngYumrUrdFk9CZcR01QUX4xOyy0tyryOfPhVC7rZQIYgu0TeNy-HQlAYTJhlb2u71G4S5DZtKy98GPsGFLSq-ueet5e7j5oo6zq6ctLRDrsmgSP5eW0MpwHdK6L-7tAxgfvpC8PaabXT8aQ0lLX5jP4D5RuC5cB8C1LE4EeYBj-K-Z4DV3jZdd68NK9d-to-xFQTtgwMt3L1EvppKoVatO-AlZdAJYzEAM0AGh_oPT2NsdkTvIvk4JDLxsV5_fAJjdkQZ2zbARJImgvPTeHoXR3G6yZPm8s58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Xf6kpm3iJ4ZLXqnHbztlhTEnaqH4oKr2QMQkjyi6hcdz9DeYpL4AWjjJbTbNRwNk_2kq3MbXrem44447FlN0PuGdqc510eefTnCb2e4Z5utQJzilKBLopvlHHYwLvYgW9CP2NYMv1oJInrThH1N-uuRXwo-m8oUb6CWJIotqqVmluEMmnmxTCOokjADZWdsdy3GwkPGLvwDh4FVmdeL1G2h98bIn6fg015q_g5-6pHeQQUrkgKQsCJZDTsbQezAQkZGzra0v7Z1Pk1BwYjaayq9wk4bDnWFqQKDjt6RP76m184O6874ppmkqHQ_AVsa8qyH0QWd7IwbbkaRHFJdpr2MFOY5d8PDXsjGc1v0Z2pS9SuKblyKAZ0L4oAQwGQnE1YB6B9huCJngYumrUrdFk9CZcR01QUX4xOyy0tyryOfPhVC7rZQIYgu0TeNy-HQlAYTJhlb2u71G4S5DZtKy98GPsGFLSq-ueet5e7j5oo6zq6ctLRDrsmgSP5eW0MpwHdK6L-7tAxgfvpC8PaabXT8aQ0lLX5jP4D5RuC5cB8C1LE4EeYBj-K-Z4DV3jZdd68NK9d-to-xFQTtgwMt3L1EvppKoVatO-AlZdAJYzEAM0AGh_oPT2NsdkTvIvk4JDLxsV5_fAJjdkQZ2zbARJImgvPTeHoXR3G6yZPm8s58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjUd5GILW1uWqbHXICG_iU4uRZ1Uq61R6yML0IZTGHHKey3pPfK_h8AyiX3qZO0YfyLpBbSGghVpBGsH6u-AUXj4QRBNMWpSAh7Eu5KkWnGH08UcKo9IaZWAjfwrb9jBeUgAJutqrCmpTL3hMxGFZiBX8D5hhnPxVeLBryOpKzEhR_DzaGnwSZIPaQZBo5zPQGjY__-UWPLEwEODvP0j34hgH9cRX2apMEOtSwt_2uA5bNw0_RwRwjTS4YcyflPwVzpN8UV-PRdSeQ0_4oW5CwQXIHSph4p6T4qIu6Pl8Yy_yDTiUXz2qT8Qv3FyvpHeUPT5gRIO6E-_TWtIq0LWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLMjWXDmDbAm9fT6OnzVub6PDi4SQQQRD4tp1I8QLTQQlBuj8fEMVto2Jvpz_nbqfaHyUy3Fqyj1RrGzJQsAVcRXV8svHiBEFlGKWI0ckbHp1tZDvVs0g3YX_sTlVVXy-qxChA_umx5tJyAt8sfsy8jffBFFYRjlFIit8tzT3xZO0Q9VKgteadPhBT10US6MSnwqbLZnR9Ae1UQvi0IjEZRi4b-FZxoHFz_8oOXcSJalPzwOWyZQvMnbf1ER4sJR2hCSu-iBpJj8b3nRRSRAf9XXDbEGbvVSNyVO8L-X9XM8TkzKPC0RpWA64XR6HN_NoCUtqF7Corx7A0SnebEpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-ruhjP0J0Qjwbas12Ufb3e7pxlReYx4R5SMCo6biSo3iMOD5VriP87YKaeJ8Kaly5qNumxPfQLS8N4iz9wMh450TWLv6a1IFj3A4lfAEQWe634jYkki_9j-ljAnGS90F_8eHJti8M1GC-ZHJxocvItCCreeGkfH3wY1LJC_HKI8UmLffVuqTLq0UZLPwzD35Cj8EaKvmKj9hiUjJHj5ZVvnd782nuxJJNj-UGsl1GzFrEOIzVkbZOmtbtfaZshD3iD2SBpafmKBg-TGQull1Hck1xoN0nbruOL6p0KmxVoIhaVc_NwIq5KY-uuEFuv6HmGAZ2GJIjbTI8CXIYFpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIDWjarHS6baY32p2i-2vy_arg97knIWN9eK9RYJmRPTG5ofbaaVqkwQ2hpIhXTRMfvFWLB17SmZS2GTVJzvIJOe_XPUy4lPAz7w1Ngq8vUWU5zTQ0qSgclc4OR4mAknlnCG6HHHcmhUjo5s5W8IjdOIyTss7eChyCtUfpusV5HqAWtdS34v-gZK6dp9PsgVfJuEi8n3l11IihTZqh9iwQnjgVhQt65awZG4nOhd6ZbOYXuuQKxx-iuIdio1IgqViSaEJVt-YpiuYaX4C88z0ZqX8JYXh6euZOcjjWriaiSudGeVRZuwnYqyC63pNEOGdMafb7xLzz9DUJlmcD2b4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=WHsmc_Ml8zN4doFMs1UylWbhhfJNTv1bL8-9kQdZ-eWvMDz2zrVTZRitQAcJA1VK7pKXlc2ji6ikeg3780PQMBalGcnYva_KcaQInIU2MTdzIKa4OkmvLDxfa20t4p1LsW0tTmQ1-OXQ3SSIS87gDgyMZzxQTwfAiKFCSnhvaIJrvFrTZCLfcrabnZguXnbhEGB4LrTLOcCfRyf4LNxWWopIi0s6C4r7GXz6rXGH5JwgczIJfKji8oAWLXj1msa6ljaixL10rr7qjvtYNNM1AHkHDbucoso0cJSX9v13_Rb-13quZFSNaD0E6smUsG2jjIrIYbyIf1MQpUoifdqKRw2j-gqKQge8KZM1PdlmFU6POcUMj7fjCqOPLPCvIzxAu3ImTJTlyi-WwxwMFIFCPfpiF9SQJzx-3ruLWF6B0kIOE4b_Tit0FWxdp19nAKwGBrgTzddeYpg-fLtV9GndrghYwZa0DN-nn63_YfF2kYQqsMcVi_yoDljNJ5oMib9sM3p2045FrkbX2fR-qlR0GX7M6ukyZIL3HaldQqN4IsT_Q6sv2s0xA5BFC7GlUhMmiGwLx9mRTWCjYm8jC62B_0Qrqk1spuS1yu9KrQKrbXhfZe8yuCdtrwxWJY5HwD9mTPxn9B5oEIkslSkRvn2Q97yBp7EuVzfAHqMoiSMeeAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=WHsmc_Ml8zN4doFMs1UylWbhhfJNTv1bL8-9kQdZ-eWvMDz2zrVTZRitQAcJA1VK7pKXlc2ji6ikeg3780PQMBalGcnYva_KcaQInIU2MTdzIKa4OkmvLDxfa20t4p1LsW0tTmQ1-OXQ3SSIS87gDgyMZzxQTwfAiKFCSnhvaIJrvFrTZCLfcrabnZguXnbhEGB4LrTLOcCfRyf4LNxWWopIi0s6C4r7GXz6rXGH5JwgczIJfKji8oAWLXj1msa6ljaixL10rr7qjvtYNNM1AHkHDbucoso0cJSX9v13_Rb-13quZFSNaD0E6smUsG2jjIrIYbyIf1MQpUoifdqKRw2j-gqKQge8KZM1PdlmFU6POcUMj7fjCqOPLPCvIzxAu3ImTJTlyi-WwxwMFIFCPfpiF9SQJzx-3ruLWF6B0kIOE4b_Tit0FWxdp19nAKwGBrgTzddeYpg-fLtV9GndrghYwZa0DN-nn63_YfF2kYQqsMcVi_yoDljNJ5oMib9sM3p2045FrkbX2fR-qlR0GX7M6ukyZIL3HaldQqN4IsT_Q6sv2s0xA5BFC7GlUhMmiGwLx9mRTWCjYm8jC62B_0Qrqk1spuS1yu9KrQKrbXhfZe8yuCdtrwxWJY5HwD9mTPxn9B5oEIkslSkRvn2Q97yBp7EuVzfAHqMoiSMeeAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Z_uer48gy9DbrPe1PeMNvCFrVwwXSq6WSZWzYNrwaVmPXXZyUrqFRH9jKSD_xBwGkA3YfAvYgTb3Uy_god65JvEHlamRVbizD14QhOpKZJ1J3t7mZI6h8i0ITTQ915P9ji18PBQ9C796f5b7MFpayiOOIBdnfsm_LcRlpJECQ3sctjZ5pqKPOaN1h-y-10eXP1rZUXOjw15xwYoi89tHb6RRuo-7ZZ4-wiCn4y9bv2ME7snJ4udJAzOeU1FujSf7-r9l5ydh9MUw16thB7-8Qy-QbvhrQt8MuhYq1XzZsmo4G7XEKyU6gCGfYtbR6YeyoasA2yNbnl9O1DDJqiBvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Z_uer48gy9DbrPe1PeMNvCFrVwwXSq6WSZWzYNrwaVmPXXZyUrqFRH9jKSD_xBwGkA3YfAvYgTb3Uy_god65JvEHlamRVbizD14QhOpKZJ1J3t7mZI6h8i0ITTQ915P9ji18PBQ9C796f5b7MFpayiOOIBdnfsm_LcRlpJECQ3sctjZ5pqKPOaN1h-y-10eXP1rZUXOjw15xwYoi89tHb6RRuo-7ZZ4-wiCn4y9bv2ME7snJ4udJAzOeU1FujSf7-r9l5ydh9MUw16thB7-8Qy-QbvhrQt8MuhYq1XzZsmo4G7XEKyU6gCGfYtbR6YeyoasA2yNbnl9O1DDJqiBvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyr54eBMbRpX8IiGY535FbgscGklTIPgPv-QZ-s4i-cxxuF1PltLbv6038bnr6Mjq0F45I42ZZ4LZr0AV74N4cCeVBxGSQHHTwGuIIoN89CuWbvPRSVHy4r8D2DX8O6vx6KKSOuUW6vEOCVNNUKaOlK6-SxRLfGegWDssU6qi7_n0k6usrHNLBI3eyxepyH-s8q5Oli4P7P4znqTBM_w_LlmaZ8WkXoN1CZqFt2_FRktjurxKnnmVyouzzpxlxkjYVi0ARPhNoqIrcYMAFJAvhQTbhl84KUZVsdcduFTpLXqQ8o3fMBl6wLZMwGymb0k6L-UUAKkuLy8tEbGg62cIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIxC8vgggt__vMEdLQv82uYZU-cGb7YyIZJkPLiYBKmxQRm5Apd5dt1J88s6i60jpRO97e5OrKmwBSaIhvz_6UKb0b7C5p5-3TFLXp4aYHwvSYdVSp9gbiZOJCpa5wLef9j6W1VfC_qy1ajFkv76nqHddP_7t6wwOdo_0jUeplhUpXOqOi9EkkVpYgqRznZESsmBtkQCcZIUvhSI0bdFolF_TtB5_f7E6dJuQizbUA0sPJQeSCKy48uIP0vBQc2uGZX-mn3KVo_MaLrSijTrMxsjHFyxw0YTQML8AYfBMlmXTmdKUGinOC7FZqJWKFpOgvv3IahZXKpeVdxPj2at_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnzMHkMUnYOXpBT42gkbQUaLb4HsNghqff_7loKa8vEDBljgdfCUa6S7nQH2RSlGWiSgZji3kM_xjCTzzWAKy3NcoSKpTOVvuDkKYSV1BKeAHBGSJonJqf8PKr9MS1v3GetWkOWDtDugGhfcHXd3r3S6ZWKEVx-HCyeIM8CF9dvH9-0joJtuxc8m-3xhV2xEFW2RDNLn6JuNbLTH7-JVTsOU_2Zd6pO4ok5ogLsnZXd2Dt5dUwJaNHeBZqDaY2TH8Y57dPW9RNmmhDC2Y-DV-XLfVDAv_piW6drBZKReYZUXN0UW2R_N6T91n0u7eqXqQkNFny8XoFNMVv3YMYN0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5-DyAd_uvM_bvJxu-caCVGitNMqcw-_q9U5Bt5RsoDogfaT8kPnlp9rJQu5fsvIAKcr5JMtG1VhstzWzvdmQK2RCyz7o-zx5ARjK9jQ_-RAEuhUBbORcRNK3WUKynawERHhcvxpcIEf1iIc5yEfuF3VqdJexwDlLkAXHaY0h_knzCp-5NYWhspmpBwHVnIH47moqn-j73WK9ftqefew4dmNLNnzLHMLE-Jz9Et-VikN4XOyHbGZojzf_VUllKy6MJ6LNi58Cx0d8WrdzZFYdHPhE2IBzYtOY4yRt3wMzjZIg0w7slvzolaP61aKNsX0UdnUxtjc1Ou7Fdajdyo-mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilLUArMDHtZIXMGUzNNMcpGMPurodEixg3DZJqny4GAXC5OAIfzkQCY-rMFcm3WU_7tH91oWUedNbs8QaY9XLDtwyPXM3oZe2x_zrTW9r9IglMzqQuG2VXcwcZtE25lmKheHaHVgaMyuCXUM2Ett8jj1X3bYJ3NE5hUqO1H5oU9xX1JuIZLm929AiLAYg5eUKvzScQpsPdBHC5AY35j4kzgBzQ8Dv5tGPrYFGrVjF0sCfs3A3_hNR2n947vbIpnJb_qrgU6COkPjtQrUhDCmDrVbhkc1APkX-VMfS1pVyLB7SnaTpX8-7v7sDcT2_eGLX1McfDi3sUXEs97vavcgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUirqMTVufzN29g1GPm0Ul72D3R3R1cqiU6fJF-DT9v15pWEaPOIYMPniixMarrWNg3moJPK7rVWeSRhin99tn7z52ymUOZEMBPOfvtXKjS3ziThdRgS961z9bmo5aGh99CN_vbPgiCcN-dgVxiXT88edy3UFfgh2K-5a0_CQjEd3-pyRMVLTFzsjANqa453X2oFuhq5yMwtzGTWJngk2YHIvhXMI8khgOyGqDoSliyvROfBn1fdHCBaclsnpQDi4bOpEqF3EvVz3VQglPWutH-6W-QjFv6B6PlObGSKbOu4z0VfvHVk9kbKxiHoLijDPnKykIpmEOhKXs6A4gg15A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSOA4PxA5kXwiK1aLAReShexGWvFf0-NflKWC9CWnN7j4KPbqqAmO4vx9YYvs1khYCoSP8n5s9EpvaKpvQP8FcNpsGXiGha4EUuXidCQxLcssOvx05c-cYA93B8F1FMZOYlbRHPDkz6LZUxWwbFyN6reGfgp2xzDmr6w688ReTIOECLHOerEtLPGqsuadWYHB0TiQrENs5HZRgWQnmIUCKjSDN2LDRYsbBbudvjTr8bv1NL5pSqj7qwUnn-XB25aC9h9deOTqL_IRpb1RrGLDArIL2xa2nYywTj29YGbXhZEflpONJfcH0EQe5I5tLfIXzNUAMVdfTIbPcQUMsdlJg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=tvGWEUEoQx-pLsSUVr3rpTAeMQsGrPQSHe4OvvqG7Fq-q-WgroQmCTbW8h8ABX1NU2n0TZgo8mi9KlfYNGhP2BVEdktPRRh-asyL7KZm6yT5hB1NAbENzErPGzhyLOq3OdcMFXARxfyQseRFE6a5Dt2qLEia7w-Cv8ocuwo7O-J3eZpBh57x4LaT_grqPDSeu6VJx9jmRPVtrZ76RUHd2CtpuEJ9gs2wo-SpgMGdh_hGtdipkrDEyt8CXfGQ6CHaPGcotA4-33fRhEAsH3pyf_J11IBlrnRu0Vynjn7bklUq7jMFrGmSxKfzUZSyBvDHI9d1rQ7VlPzlCwNP_V9cMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=tvGWEUEoQx-pLsSUVr3rpTAeMQsGrPQSHe4OvvqG7Fq-q-WgroQmCTbW8h8ABX1NU2n0TZgo8mi9KlfYNGhP2BVEdktPRRh-asyL7KZm6yT5hB1NAbENzErPGzhyLOq3OdcMFXARxfyQseRFE6a5Dt2qLEia7w-Cv8ocuwo7O-J3eZpBh57x4LaT_grqPDSeu6VJx9jmRPVtrZ76RUHd2CtpuEJ9gs2wo-SpgMGdh_hGtdipkrDEyt8CXfGQ6CHaPGcotA4-33fRhEAsH3pyf_J11IBlrnRu0Vynjn7bklUq7jMFrGmSxKfzUZSyBvDHI9d1rQ7VlPzlCwNP_V9cMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbn6Ti3anti7uzyhkK4J2dIZ3UGANFE62GWYb0m7prZaW59JiRzsoPSfL-wHeLWEhw55mIoq-IgtcctqVIMuOiSdxERYHXpjTRcjh6Wv5vspUJ1Okuy3U5DqClX8E5-Epw7tObNIxevOb77uqTRuQqAlT4kRQxZxZarwxQYqEaoEoj3CrtCXeYD3cnjWgF_X5OaBgf9wbrM33O82rI7fLziGBY0wnG-kksK8istc9YjZmTcUz9hOYZfaDfMvnyoBqrkQEQivid0LX3qEkkLa8LiBSrOvO_ca_JOhti2psJRYfAOkm_2sMkMoVftQdEDM15-ZK7BU3WH6vXeUrJGOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=GxoPD3o8_Bci01jKdf51j_f4u2fo47qi88NGsWpV_FnOMPqdL8NzAdBoV2bh2sFNI42fJ3DzgdFL1AWMn2q1eA2-aimD8B0D2a4qLhw57DgK-dyzuqcvSlDV-ttjvsm-x7AzFQucOGYs2pH00Bcmse7bxoNl_P4dllsof_MavAlHvolV81iYgR415YBii-owYEPbR77IVR2zy3QGb-O4cidy3PPOl21NplCwYW2l9g7fHprLA_sfk10o8Yiw6K_6O5M0WiexHkLeaPp2YNOp1gDsSCq7m7K63bFdOfe-Zbi5WEYnOOA0PfaWqT_k_yrWFqMWhvDHgoVxTxLg57TZOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=GxoPD3o8_Bci01jKdf51j_f4u2fo47qi88NGsWpV_FnOMPqdL8NzAdBoV2bh2sFNI42fJ3DzgdFL1AWMn2q1eA2-aimD8B0D2a4qLhw57DgK-dyzuqcvSlDV-ttjvsm-x7AzFQucOGYs2pH00Bcmse7bxoNl_P4dllsof_MavAlHvolV81iYgR415YBii-owYEPbR77IVR2zy3QGb-O4cidy3PPOl21NplCwYW2l9g7fHprLA_sfk10o8Yiw6K_6O5M0WiexHkLeaPp2YNOp1gDsSCq7m7K63bFdOfe-Zbi5WEYnOOA0PfaWqT_k_yrWFqMWhvDHgoVxTxLg57TZOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVkwy2MvBhxdt1HVaPHpectpvClMn3PZDXI38mpCmPAvWTPCh_w_fKZJRx3jFV4HnUUOaxEmsU9xa2MRuhgUMs2uPFDoD_mKrsxwLiTFkbKm0ZeHCt0l4sFw0RsVPsmHp6LBf-laqHOA4J_Iy7coXIlm8FqAa_N4W0-j_Ir3WtaE7ON92if_6qD8YQeot-N-akEg2s_wB6sG_KZthDjCUbKuWfViRGRU2Axx-Akpfwlo310bxuG7ozd23_y2sMCKVcdR9GAp1donKg_WsgKaZZpBsea2SDljMuc4RkJjSgxA5DKegdGjzrL_L_Vu9sUN4wl_0msZIj1UpwoC_c5zDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGDUS1KbnVv8TXGVH2r6mNot3Dvn4wyyjGNwf1z_iUiYA4JYl7kop2Zwa1YmBGOAQMZQsz0bGcoyO9OgsIJxEtGn79Gl5InopapIstflAaXsa7vPMwcAl-O165cAu64MsncLxkN30bQPltZ0HzQvx-6aek3lN2wzFSZklkIIzkV2uYC857FWuPqgeWp_jIBjukEUfvavpg88sj5MgP7PKnyAuJPPbWPqyvF5tHXL1tkrePLdfPBJ83FVwZDL277Fl84Ukzjz6c6VmC1UDhnHh-T3MW_jBTraH6Us5IDv-mcFeaxkP67ZEBGIy4tbpcvywFpp0rRfECfc8nz-Bze9tCrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGDUS1KbnVv8TXGVH2r6mNot3Dvn4wyyjGNwf1z_iUiYA4JYl7kop2Zwa1YmBGOAQMZQsz0bGcoyO9OgsIJxEtGn79Gl5InopapIstflAaXsa7vPMwcAl-O165cAu64MsncLxkN30bQPltZ0HzQvx-6aek3lN2wzFSZklkIIzkV2uYC857FWuPqgeWp_jIBjukEUfvavpg88sj5MgP7PKnyAuJPPbWPqyvF5tHXL1tkrePLdfPBJ83FVwZDL277Fl84Ukzjz6c6VmC1UDhnHh-T3MW_jBTraH6Us5IDv-mcFeaxkP67ZEBGIy4tbpcvywFpp0rRfECfc8nz-Bze9tCrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=qXl1psfD2vB9K5ZrRr4QlyDZ10XV8b6qgzqlUkjF-jKX6F5rm5XoWACLso5_W9ci2NdgXd3LB7l2m7_pXw1zlH5h4k5y1K6IwdJIyRhr0WsiBIeD21bfwJGeA8EQhUpJgcwEKNAR6sI48s2p_PK1EkFtLer-jbmBDVKLjrQJu7ZvhJcjzvDgWobScZS0CnSsdwot3-acHV4pwhUdervWQvOMVrKGPDnQMEX6DT1hAL0I375HmC_b1TBsLmDIKBFtSwAP0xrM4XsY_EIYAMmnbekAhMIcEmON3Br_z_GeMChc_xsxKEfXvkwJdqnvh0fYHXfAXQWg3O9kSJTTKdG4fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=qXl1psfD2vB9K5ZrRr4QlyDZ10XV8b6qgzqlUkjF-jKX6F5rm5XoWACLso5_W9ci2NdgXd3LB7l2m7_pXw1zlH5h4k5y1K6IwdJIyRhr0WsiBIeD21bfwJGeA8EQhUpJgcwEKNAR6sI48s2p_PK1EkFtLer-jbmBDVKLjrQJu7ZvhJcjzvDgWobScZS0CnSsdwot3-acHV4pwhUdervWQvOMVrKGPDnQMEX6DT1hAL0I375HmC_b1TBsLmDIKBFtSwAP0xrM4XsY_EIYAMmnbekAhMIcEmON3Br_z_GeMChc_xsxKEfXvkwJdqnvh0fYHXfAXQWg3O9kSJTTKdG4fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbfJxMaPmLJ1U3ld8_FlBrvB0oBjblUnKOweGZtOx0-COkbSj5I6-SxvH2Lt5ZEdV2EtZeq5sYGl8b8kHSFFC-ddJZOYl6gwC9Vmp4m0CzcNK2wsae4Kzhqan1fZ7d2aZgdGnw0wd4NEunfOviBOKtOGOcqpQNsqe3EjAPSvVs1zMD5cWrG5pvn1VrRyDeEpuyPtYiY9LiW0doMgpK9msRHRjxyAT2FdZ17_s5N7101on581MoWh9jxuxX6F7TUUiACDNZhA-M2sSsxyUOIF0QsNDwQj5PMSOf98WP6HgybkB0F-Qjg-pxSpZopm4StjTJaW-KUxOunwm0r_PKBg2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbfJxMaPmLJ1U3ld8_FlBrvB0oBjblUnKOweGZtOx0-COkbSj5I6-SxvH2Lt5ZEdV2EtZeq5sYGl8b8kHSFFC-ddJZOYl6gwC9Vmp4m0CzcNK2wsae4Kzhqan1fZ7d2aZgdGnw0wd4NEunfOviBOKtOGOcqpQNsqe3EjAPSvVs1zMD5cWrG5pvn1VrRyDeEpuyPtYiY9LiW0doMgpK9msRHRjxyAT2FdZ17_s5N7101on581MoWh9jxuxX6F7TUUiACDNZhA-M2sSsxyUOIF0QsNDwQj5PMSOf98WP6HgybkB0F-Qjg-pxSpZopm4StjTJaW-KUxOunwm0r_PKBg2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUir7tM2vQlGP1JUsxz5NWqbzVRua5TQEsWJxaqGurjuYYx9mpN2sU4UAjMriOKyt_3i96KhdAxxJd6c8QTcQn24f3_TQbHjBm3_Y-P4rDZ5a2CN-gNOryB2xWYAHlg-55HD1BebSTJ0t75oZVmdY9guiebgsmaQZPndkFklq0_nvVhiZHMvX4zP051kiXVZ3tkYJ4BRGWjNuTFXA91MuTo4GpDBJm5jCnwOrjyMKptvRHIgyrQXEH59JLU9koW03L3vJlElER6IqStRcjWQVvbvDq-Ayu1ijVJhuoqdTmMyy0VnNiUH2OvwwdQRSVA29kyMz0PgXfGnyXYgsPF7jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj-svlGBlTcw_Z7vRVTRW-arzF6oh13X8fgrDL87nBzL9bBfYJEOZghJ7C-fCnsvPys9RordLtXajhUrtUxavlHuI4IWQbH45GMaxRqXRSso7KCeD9-QN10Aa3UCwnOQwI4UY29FSxixvkcxVJPj6H1uxppKqV6b8N0m1fPDm9XbjT3c85_47f0cR7KXvK-pP3NHEOhJZ4nUQOJ9xK-zPM0MsOETIKmdPgH2zWKBDsADdCLLKAF6U9BqFgnndbBk-reFccNq0y4VX6xN1s6_XJItdmwpDEi1PSFKovyfkkRCLDvZvY3MXrxpXgnw-BYOsvIFP-ci9IzzCCsETWZL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnAaZOTQwgoaHmwrIY02winIvrmqF5iywV2uiWdpFs3q0iiDYb30xLbPBmyH1gBCDu2JkMClJaHGGjQ4y2P_27fwcvC8NuXG6LwDFGyFgVEZHQjstrLu22UxrUxTgJ7sPIERJv47ULHQ-SZUgnNofELORSgssSMz-EArQZJIRDm1GO7r9maO1wUj5QzmA2VqIcxCzlk7eH7hp2w9qOnhiVWMVwNQJ68xU_Z8UIOeBUlTptimSMjvoZHOgXeZmEOnRF5ogpiogtICQs0mh90W-bxmivx0IojFP2OTgR1oCGiptYgQPeeKlLBJwLDfkLEAzbtQekWWJ-ALvLGHCE8kxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRz-rox_tYTBQV4LncxEXnOqNUCqinuH-H-7ikKJJypmaWBbxnvY8jvsayfPlznCC-wRHRxcCTOA4BpBRl9gAWmNDEepnv6hP2Yo4OZ3okJkz_OTqMl0Gt6WNGEbI8DyKPLQA0USxDeOl5wvB90dVzVqBrj7L4dwPfrTZ2MLuVJbXogsG97_U42hAk9p6AjgDXrQF7oUmHIWSPT5871SG0ezYyNlDCeQ0zCtU_kTr5OpZJjvtvwRpsssuvHuP1NRSR19WjQvwTx-Z5Zlxz-w0OB_zCJmiy1UQTrg-ziR795R35Tn-0ji8kDTjPHZA7V1GtIKyEETT_sLyTL-cVsWgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_hRhDWArfcd6VWOiaBz3KkCOicilkYG3LtXVlnV5avYybBH1WeqDMU9PHFXqc4ADlX-Zo0TYVtC4_ffAQnZbDOxl5MwXDYzIe5g6hWXnwEgvuomWNKVgQI6tdqLl7RwJwo-24rhnWnOEQ3zjsY4C2ZE6cuqgu9z4_QnSYwHgA8PUFi2W0HMIb8vWoqqgwWDrv8QiLxRqsKB63gwEoCtd9_YqXElNoNQOF-w0mp2h9NMhhsxAMZ1dqpCDXW0DpWpXJVThvicvGkxOj9t7ptSUkG25Q7Ih99t2WK0pQwWsCqsdUSXe5HtOvxJG-yh43p0ObgKCVTmddDfodLZ55Xmkg.jpg" alt="photo" loading="lazy"/></div>
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
