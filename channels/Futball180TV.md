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
<img src="https://cdn5.telesco.pe/file/nAxnj0MPRgiJyS_Q0rlaa6LWj3MhChcs6lXnGVpAEmHdJOzstvXqLiUiLOvqS7El4fQDMVoM1Dp5UNWHDBty9pgSsr97HdMA8ujPOMKyDLD_oV9Hgeb6U_a5AsaTLW9LLxoBqrRtLS7pJYehS0y5U5pUWGobqUzZ88m7UZfBLB-giJ3MiXB_LwOmnUJmXZ3AB33fCA211U_OPZ1HvJchWqrNUcWolECC2Cla68crBsU9XTGtZ6iWrikvIYZJKki53_kcaY6537kYnbyXtxMY5DYWDdJqz7dG6H2Fx5WFnXk1ZtbxrtGOAeS60mbYKqABlwA4Jq0oue7INwtGaEOVHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 491K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 13:59:38</div>
<hr>

<div class="tg-post" id="msg-102864">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UT35HWXvbRqIapvxUPKtKJAR6o21JWdEUy0ZIYG_dgG9s7PFKfEyXCN7rl28hDvCmTOJstndo235ZF794_2teUqVJWyHPE_-LdCSNB8n0xyQT7zne3xuy3fy37849_vXcRnf56Cnf7sH5273M6IJMrvqRX1NIz8FJf1BqK8mrBPgICvJp2u4F8kCTXDu_gNX9xVt_zh1_uWQcZZuNQ5MspvCjblMR7sjIjI6LevigcWwnM3sKh0d_YtqIa44Bex6b6x8fvqCncsFlTx-1pFjYEiOjOJdE4v-YwkxjjkmTQxY166wfLjQA-UzBdI42aK6EVK69ScYE1z0_zCUsccGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
بهترین گلزنان تاریخ فوتبال اروپا:
🇦🇷
لیونل‌مسی: 496 گل
🥇
🇵🇹
رونالدو : 495 گل
🥈
🇵🇱
لواندوفسکی: 395 گل
🥉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/102864" target="_blank">📅 13:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102863">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3mvSleTPAt_CJW7UHxVNBatePKHF2VrMGEXNpoFH8oO2KDpEMh6q1ZYA-oe3UC8oieCMEhiKnSxNmENUn4L6Cfd1PjChsawRhNjVfLFcp6M4CUgpoVdbmrvaX9Bg0Hcf0OEcFSdjZ8iiHPzkRkOJc92co1DhA68T7tESoboqSNLduogflbrsEEo67QW7cHU_1nqb8Gyozkq7X7WcINxXU6ADxc4W7rjd-DJ54GDtzyGYWX3Y_HxKA1EpOQVOI0wY1YUJUiX3DLdzZ9OkFyd7AaxOX4Wt14ZYiauKxjwGiWyYbD55C2CZyrKcD4-OrsSlJRp3IRT7cR8vguGcRLSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
🔵
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/102863" target="_blank">📅 13:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102862">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSAaLwybEUyXehy1cxYvHyJmN0dHgYtyubnPxTgbjuaOmKdPzGBvv7sPArWjawl1K_-9q3z81CEP8ZLEQ1KVax5ezwB_RdpMnB7BZFKSIfZrXdZpid-D61S-dW9bc97f8TbcANY79pzRuUYL9rP7D07CFlTF2865eSiVepdOIyqk4ll6EK59xgtr54mlGV4nNiHzI78w_I8VEEnX_7r1sSdSWSBDw916si17YDgM36Vd_2V_xicnTo4TQltGaqLj96CRoVxgvsV_GUxFjHtiQlpTE6dZyemO52SDI02bxBviVfmBDUSnOKZ8pwDSzao5TFcv3KSnwnbs8XTnWNiZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
یان دیومانده بعد ازظهر امروز به مادرید سفر میکنه، بیانیه رسمی بزودی منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/102862" target="_blank">📅 13:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🔵
فووووری از فرناندو پولو: خبرهایی منتشر شد مبنی بر اینکه توافقی بین بارسلونا و رودری وجود دارد. ما با باشگاه تماس گرفتیم و آنها این خبر را به طور کامل تکذیب کردند و گفتند که این خبرها نادرست هستند. اگر رودری خودش مصمم به انتخاب بارسلونا نباشد، نمیتوان در…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/102861" target="_blank">📅 13:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb94d33db.mp4?token=iTMa12vdL72C0y6hCeBweJP5PaIbE3iLw6sMBS9_4EeNoBwyTydaDEVHnmgAG0OoGxWjpQy3w5sF2eOzXOKypcz2h7KfjantFwujclUjYeiF7mxqc7QkeHH9tVefdPci-WcGoejQ1iXikPHKQsjLm286GumTYdbyglqaQLc_u248XlgnFBTu3h7Q6AwtHy6MuRaLdJgLXSKOrb6ctekgMvckVaCb6V8R3es1fKruT2q8jv1murpyS6MUtskAvhJZQd5P5GXdLb6XOhy9c6oAXBbKNLht3-RMN2zr6DQ51CADUOdYx3QQrNTT10or659ixIJ0AVJ0nFn7og6umT4cLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb94d33db.mp4?token=iTMa12vdL72C0y6hCeBweJP5PaIbE3iLw6sMBS9_4EeNoBwyTydaDEVHnmgAG0OoGxWjpQy3w5sF2eOzXOKypcz2h7KfjantFwujclUjYeiF7mxqc7QkeHH9tVefdPci-WcGoejQ1iXikPHKQsjLm286GumTYdbyglqaQLc_u248XlgnFBTu3h7Q6AwtHy6MuRaLdJgLXSKOrb6ctekgMvckVaCb6V8R3es1fKruT2q8jv1murpyS6MUtskAvhJZQd5P5GXdLb6XOhy9c6oAXBbKNLht3-RMN2zr6DQ51CADUOdYx3QQrNTT10or659ixIJ0AVJ0nFn7og6umT4cLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤕
⚽️
بنظر استون‌ویلا با خرید گارناچو حسابی پولشو به
کص
خر زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/102860" target="_blank">📅 13:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102859">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری از بن جیکوبز: پیشنهاد رسمی بارسلونا به زودی ارسال میشه. رودری از جو رختکن بارسلونا خیلی خوشش میاد و مشتاقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/102859" target="_blank">📅 13:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102858">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXmh_TuM_nuVhSr947SUFq4T5I0pbOB8BTtKGxQqWRHwMhzK8Cyi2hPqozyYi0Ej-hvIVQhUZNH2xz3qY7QoggGseoZxU781AZpHgAdYGeDWIsjIywnGdFFmAQtDc1xieigwk6fJS1vCqVls9J9F3JE6KMRC_3uwSsYaEbYWt2jWAMD1YNpo3AkCOYdNvgWocUYw99ELdNbEDRqZi5oIILyiPPwquQTSkWw7EDADwgbiTMUaHBX9Wli4ICtUuN5GigD_EFmt4j3WbzANsW1lXVUQK6kVuBUx3G3K5YHFj2F6MqP4IKAVSeKgcYGLsoW9kBVDiGpl2VkN7YJqnTlzpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
فوریه 2024:
⁉️
جایگزین برای بوسکتس؟
🎙
دکو مدیر ورزشی بارسلونا:
🇪🇸
•
💬
تقریباً غیرممکن است. کسی مانند او در بازار وجود ندارد، و اگر وجود داشته باشد، باشگاهش او را نخواهد فروخت. تنها بازیکنی که کمی شبیه او است، رودری است، و باشگاهش او را نه به ما و نه به هیچ تیم دیگری خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/102858" target="_blank">📅 12:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102857">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmdTvpIbhTLWUtkBPDAqO_1XS9g6nSqc2BrdxdhlaNqJQe8zJDYt81lxAfRYfNQOpB80Xm0R2mdvKF5lWqOJ6WO6v_vduCYJ6ooQTzUwilMfK5aPP_NMqNrWo3BxHIBGw-5UEIGY360zQSO4gk1bLzmcHvA6N14cUgBf4xXvdfM3nU3ap5jMQ6hCpCdZ4x9QjYVzOx20nI0Qs__naTycpZYVldqXKQsxtfaOzuaFX156mOZWDd2C9MJSs9f47wAyF37Lc8qZ5s5pBXgr02mX_3RdBRRChUsfgxOOIGro5pSwCTEW7s2APv6ZvXiaZ289RVAr7pltnildJYWxzzKBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
کوپه: بارسلونا پیشنهاد ۶۰ میلیون یورویی برای رودری ارائه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/102857" target="_blank">📅 12:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIvkU8fHnXTrKvPp9XiPR8sw2B7IUrPtj3x0iqe4oADrKgs5veMeA7uJhgitOM02ceQPn9k7C-hSmAmIkDuF6AECHTlrwmFUkmAezBw9M7Fkm2O6crijwbMYjHjxmUtxejtDYh1QMQXpGSy9hhr3JQSr9gSpvn7Yhhe_rW5git3er1gFbAwRnr-jg68nr07kGRn70y2N4V354qm3Ove7ChuAfaEAw_uJFGitvMN0zhlsvzExv7ItVMo9u0THwtxcbmI_0IEHYRth-M1fWOeidGREBS-SJTERZNANTI9WIidiftWfK36b4j4yVemuGx4YRFH6x3xcU5oPr_IeCDmuoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtRKDRabVeSIO1mqchnO6PGFm9XEB1w6jCuIfaSWoOuybADloWMynaplqFuc23PQmYD-NAGgZEkpXqpfiq_OIG0EziKZfd9wGu254t1QSolsocBu3u-KWHvp_WfYYHIRbn_J9OvWwDSdRZU83z359yPTX-BYn4-82W7D3gSQOgMIP629Hxrb5_565T6qVr1yvCzJgTm7YKVGk6QFftkZdxSctDWqNTp-TEXAePDCIE3006F-AkOK0AzOrjEePYIipvBUNNws5oUwZkUR5kYz3RQx6wmMBzzmBNbeK6czu5LSJ9NuvkugcJQagbImG_TWLE8SOsF2Oq1OatSztaeY4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⁉️
می‌دونستید؟
کریستیانو رونالدو اون‌قدر درآمد داره که می‌تونه کل کلکسیون ماشین‌های خودش رو 6 بار دیگه بخره! ارزش مجموعه ماشین‌های رونالدو حدود 50 میلیون دلاره و با داشتن بیش از 40 خودرو، یکی از خاص‌ترین و لوکس‌ترین کلکسیون‌های ماشین دنیا رو داره. گفته میشه درآمد سالانه‌اش حدود 300 میلیون دلاره؛ یعنی به‌راحتی میتونه کل گاراژ ماشین‌هاش رو با درآمد یکسالش 6 بار دیگه بخره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/102855" target="_blank">📅 12:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVkqbHacfhk4hmYT1Obw_KL0pcLk7MhikqqeXYkr15VyCerZ28w27ZwPndZX9GDMvLfsQVXsP_dnVbWUZx-R4iIQXsMQvbukybv5zmtKH8oRuA5Ez4SQLJC9zPW99fgjzP1tIpeUyQOStUBiEBGW0kb3gr4zbrhFKe200nGV99Y8MjtWQJPN9u6OnxPd72Hj82Ue9S_rISIFv5euOTXzzuVVEMjlsm8T8tNGnIpxQFGW1Ph3CKrLehFfj5kyWwIdjdNjw7E3rZsalkhqRF1OxTSvHsqFGPXhB8rBukzXvlDB5-SPRnh2gTE5P4J3TSF3trw2TE8zLgqDv1XnGyPc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از بن جیکوبز: پیشنهاد رسمی بارسلونا به زودی ارسال میشه. رودری از جو رختکن بارسلونا خیلی خوشش میاد و مشتاقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/102854" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMbFvR_1EIhTMBX6WYW5ICr4upoJlu8NVSx-wLfYF6_Wh7WRuXwqK0goda-2ezHrNN0sApGgLbPQy4kIPJfJqDXq1cnVRg6QJo6sJiwz1k_UW5EBtH-tmi4J_KkoMI2RadllGacucmc4BUbU2psVa3r-oi0kq1_vXg674KpuNMf3qeKbFX6ScamUzFCfofBWltasbkm69Xww_K1DWVl5an2d0SWRtHh95HlLCC_2eyf0tNda18GOgAsxi4w-b4zWNaH_DBbNlvvJamRlJ9nxglmO0UboOphv8gh0CP4ariisTkg5OZNF06koAx9lkp8r1Y2zEOmJUSuGz9CZwabRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از رسانه مطرح ESPN: رئال‌مادرید کاملا از جذب رودری ناامید شده و از این معامله کناره‌گیری کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/102853" target="_blank">📅 12:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBmtH9muL7fbv1rk23ZMsNbLdvhlIjmYIucha36vOCrqnzEZW01zCsVAY10TE2_SAup48fFnuSEmk6B6yk4dc5eDkHu_MuxaXpjv-stDXGMkYHPzo2_lKgtjuWDUHfnNpwKnUcXvSieviItRrQwCXinE7GkEdhz93lptP-B_cxhhXq7iHkrziDvdmN-4iekpdDuJrQe80gPaHeQ09k9ns0WSEi_ohsZxny9Ys0TGm97YiAmZaIw79Yeh4lQNhcVCFgU7mlrW0cUBxR8FQ9GxZuoO1JLv4SHroYyvuR0LQ6pJno_55k4pTT4KYas0wvevHn67nbPRmTfQSWy4-uEycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
گزارش روزنامه COPE از پشت پرده نقل‌وانتقالات تابستانی رئال‌مادرید:
🔻
فروش آسنسیو برای جذب یک‌مدافع
🔻
فروش کاماوینگا برای جذب یک‌هافبک
❌
هر دو این بازیکنان از فروش خود خودداری کردند و خواهان ادامه حضور در رئال‌مادرید شدند تا پروژه تقویت تیم فعلا تا این لحظه به بن‌بست برسد و رودری در آستانه منتفی شدن باشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/102852" target="_blank">📅 12:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwRfLZIJkz3oXeMvIz7QO87pROGPIM_rz2RhfKz0mC_APPq-X6OoQo7KHZy9dUn44LSzQrT9dTaa28QMxm_vQRbw78M1E8wF_OeqPeWthQKJKsVNcviYJOKD1VgCIwF2oGdtO8OXaukp6FYTnUd_q-Da5i4AoUpFK1BeI0rm9yxzk2L-lZgJ7PjMJflu4jKsUoal28CpDLUJtO6eTXY39PMfraDf6u1SQDSwZcCATxdNfKEG_jue5I0xBCm6jQJiCNXOpW3NOUHN91yYAziVgkNHvStFoFDtCyJjzP26v79BpXxGd62Zyss3P5J96KaJaHo_k4_gJa7yu58luvVfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ شایعات دقایق‌اخیر مربوط به رودری ستاره منچسترسیتی:
🔺
رامون‌آلوارز خبرنگار نزدیک به رئال: بارسا در جذب رودری پیشتاز شده
🔺
فابریزیو رومانو: بارسلونا با سیتی و رودری تماس گرفته تا شرایط انتقال رو بررسی کنند
🔺
خورخه‌پیکون: بارسلونا حقوق بسیار بهتری از رئال‌مادرید به رودری پرداخت خواهد کرد
🔺
روزنامه‌آاس: نقل‌وانتقالات رئال‌مادرید پس از جذب دیومانده به پایان خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102851" target="_blank">📅 12:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
رومانو:
باشگاه بارسلونا با  ایجنت‌رودری و همچنین منچسترسیتی در مورد انتقال احتمالی رودری تماس گرفته است.
رئال مادرید هفته‌ها با منچسترسیتی مذاکره کرده بود، اما منچسترسیتی با این موضوع موافقت نکرد زیرا احساس می‌کرد که باشگاه‌های بیشتری به رقابت می‌پیوندند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102850" target="_blank">📅 11:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6547082d.mp4?token=KgC0rKn44bGP0EPf2n8IIbvsmzMFudLz5AaMuJO6S2N6DdB6WQNTBAmfhYpbYoGkI3t9xzPJyrrXiTAfRjWg5tJM24kyFDgtZbEQ4TlH7EqFFT5Eosmg6eDKCm4ojlRzrwJdVN409fY8iJHGgPlpzqcRG0UJuHdp9ArAQmkg-_FvYpp5oTaQpksL422Yen5CylHJAKaSGCXUe4qgqpvbV4M4BNDTkG9p73hLUUPLWGRdHIPZ-nh6oZmAVX0jm7gtgpnIuXDICsegU-eQIQQ2ZjMtggVSJ0fWtBjiD1E9KK_zTomHP993Eoj18Zi9KxfUI0-tZNf-spKGeDNXzN9IiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6547082d.mp4?token=KgC0rKn44bGP0EPf2n8IIbvsmzMFudLz5AaMuJO6S2N6DdB6WQNTBAmfhYpbYoGkI3t9xzPJyrrXiTAfRjWg5tJM24kyFDgtZbEQ4TlH7EqFFT5Eosmg6eDKCm4ojlRzrwJdVN409fY8iJHGgPlpzqcRG0UJuHdp9ArAQmkg-_FvYpp5oTaQpksL422Yen5CylHJAKaSGCXUe4qgqpvbV4M4BNDTkG9p73hLUUPLWGRdHIPZ-nh6oZmAVX0jm7gtgpnIuXDICsegU-eQIQQ2ZjMtggVSJ0fWtBjiD1E9KK_zTomHP993Eoj18Zi9KxfUI0-tZNf-spKGeDNXzN9IiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
تمرینات نفس‌گیر ووزینیا برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102849" target="_blank">📅 11:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P94pdzz3CbGzrwfsLbkVMcNioKSM3YpTpOCjdfCK6hyb7ThI03ViwchTG3-ui2JcNrJOB2_Xa24mSOCwekQrrwFR6cV_xL88cnaATZs6cOQvnNyQezDGgPIFxaIKz7N10dIekHEeH5vIPDpeYZBzFpS6R1P2jAyPdkDDlbrjQRmKmwf7C0TaB3Dqnsv7c-8xgFNc1f_rlDRAqcQapSc_ZFqJiz27kqmfpgtUWUAN9-BjPuNmrZ8G538tLeyPDxBhpwx1WkjFOZv4yezP2k3kC_CLhTooSnhuogpKOX0ErwLgQ1heC34N3NbJfY4r1VWigalc5lR_COWr_jFCX3GzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
جام‌های فوتبال دنیا بر اساس رتبه و اعتبار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102848" target="_blank">📅 11:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102847">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇹🇷
⚽️
مذاکرات فشرده بین باشگاه میلان و گالاتاسرای بر سر انتقال رافائل لیائو به سوپرلیگ ترکیه درحال انجام است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102847" target="_blank">📅 11:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102846">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AfST7p-HsAI8Me7wIctfa-q2q1xpb5E8Bu4-9J0QTZqneEy9yBfr0PQfCB_fpwdKzENlZiH5AYUI7C7_e-hYv7i3Jt9vKjPKey9MuslFs6TJPB8V5QXiy1iB9DurAbdHM3wuy8OAiNieKbBaqG1CeoBTeGbRFoDlE4mZ9V9pa1I1fBdgo0Ppto6tUQ4qfqnz8Oi8fzsbZrDbX71DD2-NtuZWnl8yo_wOva2tzZoVT_eU0wNQOQtw8zpfD2uaGnLLq8Xa5R8faNTJNo1uBdoEV3TQ_VKAKJyJk0QI0Vy9TjBRUs2a0Vj6LdIovd8_ve_yTNTagju3zHb930xfDuAqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
روزنامه‌اسپورت: مذاکرات باشگاه رئال‌مادرید با رودری در آستانه شکست قرار داره. اختلافات بر سر دستمزد و مدت قرارداد همچنان پابرجاست و تا این لحظه هیچ توافقی صورت نگرفته و طرفین از خواسته‌های خودشون کوتاه نمیان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102846" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102845">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT7EpETOVcSlkVlrmY65c11-pEld7VN6ijnj-tFfrApCu89NwgTL37u3XzkOfTrbDfXHSj1s6PfL3PiVD1aD2E-7dvPriHbrba8WCHtNAJ9wJNl64yAhwcakQbns0oZhJ0QA2ZHziviQnosSxi_HBM-iipWPi_YRR4CoGogwRVXKF2s12FUw8T-wcwYcsRGKd9jzstn3oKE30XR96upvNrJrXo6GdbT1km7dfZTS5LXOntbKgTX-vaflaPUvuGxK0xOsYEPqdYq1RMauBAEO0TaAYCwlq1D_rt0Og6oWaUBdWCwX58Y3FrW3nJRLeAiG81PQNBAG0PCrGCHRadqgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به مناسبت آغاز لیگ‌های اروپایی؛ مروری بر پرافتخارترین تیم‌های پنج کشور برتر مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102845" target="_blank">📅 11:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102844">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5d8ba0a4.mp4?token=Mrf9SNJ4jhcqZ3ZUi-g3dFhctGrumBXZF2-FhRzmnbutorNbfs9bNewyuuIoU6azT9_TD-hvVjKFjgoMKnRgXtflng0N2SDHiufL_zYhZgqdUxDdaX-SvfO0e3nWHH7r_aSlRHZ-2JjYFH0fMC2sQAOuJpvIJzZxmPd65z_g6hZHKO7YkTxUHcgRBV72mLhs6wnN7oIAidxtpgB0XnhSoox5dmpdVtKueqYZMChQ3J2O4rAU0wJiBOsRd3FjbxsWJgBRt3zXXckJiW09yr9RLlctg5GXLFHoYGINweoh0KSqHc2YnfDQfRfpsLzD9jKM9zL_5ZBlwZ_y_8KGPrvthYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5d8ba0a4.mp4?token=Mrf9SNJ4jhcqZ3ZUi-g3dFhctGrumBXZF2-FhRzmnbutorNbfs9bNewyuuIoU6azT9_TD-hvVjKFjgoMKnRgXtflng0N2SDHiufL_zYhZgqdUxDdaX-SvfO0e3nWHH7r_aSlRHZ-2JjYFH0fMC2sQAOuJpvIJzZxmPd65z_g6hZHKO7YkTxUHcgRBV72mLhs6wnN7oIAidxtpgB0XnhSoox5dmpdVtKueqYZMChQ3J2O4rAU0wJiBOsRd3FjbxsWJgBRt3zXXckJiW09yr9RLlctg5GXLFHoYGINweoh0KSqHc2YnfDQfRfpsLzD9jKM9zL_5ZBlwZ_y_8KGPrvthYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این مصاحبه در تاریخ ایران رو دستش نمیاد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102844" target="_blank">📅 11:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102843">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKXFGXr0vRO_c6vk0WQjCHxm_0hX37wZaKr4AysCuodz1-azRggrQNISUmrik8ZhYhXIYbSzRYrGOQ8thpOG7D15iN5yBcCJo5FQ0ktqih3lPuY4g_aS451HuNk_91xQYMEji3gRV8BvcuiOSnCPgeaKL_dzF4xaocsRfLvqHgd9DV3N6w1saFNq7CG-heY-TaxlkehIt0sKouNBDEILxrOERBZQOdpa7WAawi8uNXk3DAittMCDUA1JRc83UoWac0Fy-4mUXh7h1df6Ryn2Vr7_LXQ8CB5LTlcffZKlMoGD2uQrfJhylfLETpB5StiR-Gz3czNADI2Ly6XTiq_o8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
👤
#غیررسمی
؛ قرارداد وینیسیوس جونیور با رئال‌مادرید تا سال 2031 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102843" target="_blank">📅 10:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102842">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6a1ff7af.mp4?token=DpfKJTaePITjLigulT6AVskr9PXxxbVA0uMfmNuhasYrJEp0iI251S39pjuObPQ6SQYyG-unsCPvsNLpE_1VzHzffvFHiW-blvMix8IZrNg7mOplmlemvjCvDR3lreAit0fPAJZ7w51iioBv12nm0BnSi7kA_hUJjmBcS9Kk8jPHk8DsGqx3yZfOijvmdvIUVlyEZq8z1IOH-sHxhlXeQa-a25EeOKrq8LiqQOCKYB8cxbG8q5MnOxl4KE03nRyjUDEAXK70grvG42mLNLuGi3CRmzf9-5b3ljKV-G7S6TCXA_35GqnJYflVJ1PBhp755zqaKcJ1ySPQd9GBTUZKGiBgBwIXIh4khzNnVG2wsrAF5sM-dY8ohx2FcSbIyhc0UVnlfWaDYE7eyQiGtc_UdrA_rBbP20Vtm3q52TD0KOa4mOjqqV3jxGcfd_sJB2z8nx4qcNL2j1p2gpqV2fjcjydfl89-d2jlCA8b3g166rm-PraCKDKHlAtpiViOsHDsch_4wgDI3oPrsbtmbpHZXnbuCJz6Icr6m6f05cf2hls8p1GCvXfTyjT5bq61e-nCAuFpGt_uhhOpEXy-CbqCofHaQG84W42e6F_LZnWYhN6cU6Z6YqB4FMgMZywjfzJIa4y6vvnrmSkDdvbIiVBANSRMzt4d-vQrjHRmSQe87lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6a1ff7af.mp4?token=DpfKJTaePITjLigulT6AVskr9PXxxbVA0uMfmNuhasYrJEp0iI251S39pjuObPQ6SQYyG-unsCPvsNLpE_1VzHzffvFHiW-blvMix8IZrNg7mOplmlemvjCvDR3lreAit0fPAJZ7w51iioBv12nm0BnSi7kA_hUJjmBcS9Kk8jPHk8DsGqx3yZfOijvmdvIUVlyEZq8z1IOH-sHxhlXeQa-a25EeOKrq8LiqQOCKYB8cxbG8q5MnOxl4KE03nRyjUDEAXK70grvG42mLNLuGi3CRmzf9-5b3ljKV-G7S6TCXA_35GqnJYflVJ1PBhp755zqaKcJ1ySPQd9GBTUZKGiBgBwIXIh4khzNnVG2wsrAF5sM-dY8ohx2FcSbIyhc0UVnlfWaDYE7eyQiGtc_UdrA_rBbP20Vtm3q52TD0KOa4mOjqqV3jxGcfd_sJB2z8nx4qcNL2j1p2gpqV2fjcjydfl89-d2jlCA8b3g166rm-PraCKDKHlAtpiViOsHDsch_4wgDI3oPrsbtmbpHZXnbuCJz6Icr6m6f05cf2hls8p1GCvXfTyjT5bq61e-nCAuFpGt_uhhOpEXy-CbqCofHaQG84W42e6F_LZnWYhN6cU6Z6YqB4FMgMZywjfzJIa4y6vvnrmSkDdvbIiVBANSRMzt4d-vQrjHRmSQe87lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇭🇺
فرانس‌پوشکاش اسطوره تاریخ فوتبال دنیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102842" target="_blank">📅 10:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d755c0e765.mp4?token=KrmHWlyvjao63jIVozIF4mMNofYAPOct_AtY4P6NRCXC99M4gsNth1qTYn6zQtvb9HcLQzwzCdKPy5MvIhn-xmYVvbzqvBLeC0TMGzOGOgKBavSzN3RQTOOydyMjdU6TVJR-yMqgYfpSE10A49ekVESwR-xiAoNck_0xK-XUVcqyrrvkBKjdYXrJE7FdEzk581sNQtF0f1eNUGYSN7HfbreaY8zYOlRP97O-WxxTi47dYEfUFejftX9a40nOunyW7hBYBMzD6z-SBsF4afh4yECVx0I6XQC4D7225JuYK2mc3YrT8_4sgaoO10ILlDJl3cL6QriNsLpJWgeINfYWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d755c0e765.mp4?token=KrmHWlyvjao63jIVozIF4mMNofYAPOct_AtY4P6NRCXC99M4gsNth1qTYn6zQtvb9HcLQzwzCdKPy5MvIhn-xmYVvbzqvBLeC0TMGzOGOgKBavSzN3RQTOOydyMjdU6TVJR-yMqgYfpSE10A49ekVESwR-xiAoNck_0xK-XUVcqyrrvkBKjdYXrJE7FdEzk581sNQtF0f1eNUGYSN7HfbreaY8zYOlRP97O-WxxTi47dYEfUFejftX9a40nOunyW7hBYBMzD6z-SBsF4afh4yECVx0I6XQC4D7225JuYK2mc3YrT8_4sgaoO10ILlDJl3cL6QriNsLpJWgeINfYWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
🔥
⚽️
سوپرگل دیشب بتیس به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102841" target="_blank">📅 10:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102840">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe450fda7.mp4?token=h3xtCqtQ4D_M9LwjRsMyE-AvM6b8nLnfZtUvdL35zAD4McSRLvytJim-QG-e_0t3sZmeiKDJnbLDc8PYZ-cNplgMBztkwSrfbMvmp8beZ6t3vGH94WvCoq7OlOrXHcI-0JtW6ojgwLDD8vA1-QYlC-Ewm0ZwYo02KoRmJsNU6VdR_ckGrcrTAbkxaTH-FQOAa30qjzB5VnTPsv7jAM9XtxNG6jGbwF9xdCwUiMfdmCsGTNE5BtpfiPSEznFBXhVx_Ee8iigkpABLX32HFA3TOWxyGQOa8EcohnFXcgbt95LaXeI-ZdKkGwlv-ZajdBSd7IUMy53HgmMe37Q29ox8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe450fda7.mp4?token=h3xtCqtQ4D_M9LwjRsMyE-AvM6b8nLnfZtUvdL35zAD4McSRLvytJim-QG-e_0t3sZmeiKDJnbLDc8PYZ-cNplgMBztkwSrfbMvmp8beZ6t3vGH94WvCoq7OlOrXHcI-0JtW6ojgwLDD8vA1-QYlC-Ewm0ZwYo02KoRmJsNU6VdR_ckGrcrTAbkxaTH-FQOAa30qjzB5VnTPsv7jAM9XtxNG6jGbwF9xdCwUiMfdmCsGTNE5BtpfiPSEznFBXhVx_Ee8iigkpABLX32HFA3TOWxyGQOa8EcohnFXcgbt95LaXeI-ZdKkGwlv-ZajdBSd7IUMy53HgmMe37Q29ox8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
۶ سال پیش، "انفجار بیروت" که یکی از قدرتمندترین انفجارهای غیرهسته‌ای مصنوعی در تاریخ محسوب می‌شود، اتفاق افتاد. این انفجار معادل حدود ۱.۱ کیلوتن تی‌ان‌تی بود و زلزله‌ای با قدرت ۳.۳ ریشتر ایجاد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102840" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102839">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP9TY2OY81nRZsJdU7QDhq119gc825tRAAGtK3b23vPDW9z8a1fckRslo_6i4D07Be5BGwKhS5-2wKLYupMXtu_fXu2pjDX4F9CGmxJ1BoaBrS2zze3rtwlNJdy3oV9TEAgQuX7GWg9cPYzXXexWA9nnXfqVoEKlStuTFKNP1TPA6FWgJkpzWdRroFAUvibNw5qB1-tOhRzZAqAEUrQGrDEaLe0grqnbtxtId59gamTPPDCGRnKC5v6_u4gtnLmR-rw5A3D2ADcYvaAv-kYCyQp9WHGYKxGVip1Fr9qFG9DjoV-ediEzzAO9ZjLbBoO_dodPPXfoiiUomhiq0FvQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
⚽️
#فوووووری
از اسپورت: فران‌تورس به پیشنهاد پاریس بله گفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102839" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102838">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/102838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پنالتی
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102838" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102837">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=nqNs8y0637-m0W4YYJyr8e7gB0f3bSN5siztWBvwV5PmoHeAxYSdAA0jdaoBeoMl05aBbTcL_1Lz5GVf6eCxUgn7QsxcT3DJprNKVo4KBN04MWyHy7p6wNp5jUKDXJMayvMR00s6DGPv0Ka7goerf43sTGyG9cO0v9v6HffMyMc91CDi6fVpXjfip96p4P0F5rhSPoeoCK2hTN63hu-3vkpQgyrTEGxYVVh5Zd2EEtCI94VQEdmgb97bDaUUrwvJQZH14y-GiRX-SM1-tTTJkKu-Bz6Ss6R3TwXgquEI3S5lEhXoOMiXlY2NuNOJ_8NHvcJ9eO94-LctJOKMcemcDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=nqNs8y0637-m0W4YYJyr8e7gB0f3bSN5siztWBvwV5PmoHeAxYSdAA0jdaoBeoMl05aBbTcL_1Lz5GVf6eCxUgn7QsxcT3DJprNKVo4KBN04MWyHy7p6wNp5jUKDXJMayvMR00s6DGPv0Ka7goerf43sTGyG9cO0v9v6HffMyMc91CDi6fVpXjfip96p4P0F5rhSPoeoCK2hTN63hu-3vkpQgyrTEGxYVVh5Zd2EEtCI94VQEdmgb97bDaUUrwvJQZH14y-GiRX-SM1-tTTJkKu-Bz6Ss6R3TwXgquEI3S5lEhXoOMiXlY2NuNOJ_8NHvcJ9eO94-LctJOKMcemcDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آقاآآ این بازی
#پنالتی
چقدر خفنه
⚽
🟢
بازی خیلی حرفه ای و‌
#پولساز
پنالتی فقط‌ پلتفرم جهانی و معتبر
#بت_اینجا
✊
همین الان ویدیو
#آموزش
پنالتی زدن ‌رو ببین و با شارژ اضافی
🤩
🤩
درصدی که سایت بهت میده.
💖
حتما ویدیو
#آموزش
رو ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r15
@betinjabet</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102837" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102836">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac92224ed.mp4?token=tcAkSDwdwoBdz2APZhPp0EYASthhoBxPm_ayR0oRdVzjm7h02ScHH__2FPsCVxBlML3slf1Hmahnni8fYDFYbJzwzJFAQZfy5fS_49mRdPkGYmYPdcXSN5bBwrKfWvkREVP_Pu39e3vHNv4PinTYutyA-9DxW1-sc2sP38V4UmOjbBWSqE45yv2nJSQN6S6vCRV_J0ycCDB6uiAnTDzE1ixhRffBH6q1WUpNfP0IU9W6ozik0KXpREXQyiQgDoCsjiNMM43W33bvCFcopyjhm0TjPPvKcIWAMc42vSjDSqc1AF3UHJnqnipmqq0QYo8EvqV0x42NEIlY9_pCrDaEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac92224ed.mp4?token=tcAkSDwdwoBdz2APZhPp0EYASthhoBxPm_ayR0oRdVzjm7h02ScHH__2FPsCVxBlML3slf1Hmahnni8fYDFYbJzwzJFAQZfy5fS_49mRdPkGYmYPdcXSN5bBwrKfWvkREVP_Pu39e3vHNv4PinTYutyA-9DxW1-sc2sP38V4UmOjbBWSqE45yv2nJSQN6S6vCRV_J0ycCDB6uiAnTDzE1ixhRffBH6q1WUpNfP0IU9W6ozik0KXpREXQyiQgDoCsjiNMM43W33bvCFcopyjhm0TjPPvKcIWAMc42vSjDSqc1AF3UHJnqnipmqq0QYo8EvqV0x42NEIlY9_pCrDaEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
👀
🔥
مروری بر آسان‌ترین پاس‌گل تاریخ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102836" target="_blank">📅 09:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102835">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz-Sqsu64lErmRGJJEblsckSBnlXqf3uUotE-IP0VpuiFUWC0OJI2F_ch3zxgIuSuIOyDzct5LYT-erbymNEZGUMosertrArPMgNsdghBedW2Uby62FEJGIb-rmRoGhxBaTroyT989wCeXGwbNZCKnhaXmFomklYmkexn9eoI5ad8yMZ_QuG4A3TWJZ0TpFUSnPa1G6o_JMlMTmUzQCjmljVPWJIt0h8CUySR1Di0ffEZwHU-l7EQeR1IuswE7hBja3FXlHOcH4IY3Zv3GCVexvMA2Wecr4w1P4VYAMVlinJ7mGpz1Ilqalm2n2t6JMzHCXXUgETvjY1hAge1AgnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
وینیسیوس و رئال مادرید برای تمدید قرارداد به توافق رسیدند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102835" target="_blank">📅 09:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102833">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f753cf0933.mp4?token=rjXDe1-15FTanlxIGTlzFSoanSPk-C7p3hGrSxbgi6xk2RIvuiyigbttYUlLRS2pQ13tsKJLSC_9U0_ZvNyeGuJ5xRvJCQr7Mv6X4_2ShIUdheFmL7mZAQjekM1yjPN3gsnVRGHGuGI4tRdLYgIgeglRBn_a-wvB7vF6D2bCtC2U4MRSinL74Ftz3M-_PzgUH70oaPtTO-2ZHypH9IoGxabUmoPcgbzO9kqnGGWuNQxLa2p95jSeUDlPPqZ1spZ1EP70Zmg96GS6IzjXPZU61xjMELqcq_e0BEfie3LmsrU70FVZgDd7flWp_BUzSblmL439jeYRJVuvWIxcJqglDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f753cf0933.mp4?token=rjXDe1-15FTanlxIGTlzFSoanSPk-C7p3hGrSxbgi6xk2RIvuiyigbttYUlLRS2pQ13tsKJLSC_9U0_ZvNyeGuJ5xRvJCQr7Mv6X4_2ShIUdheFmL7mZAQjekM1yjPN3gsnVRGHGuGI4tRdLYgIgeglRBn_a-wvB7vF6D2bCtC2U4MRSinL74Ftz3M-_PzgUH70oaPtTO-2ZHypH9IoGxabUmoPcgbzO9kqnGGWuNQxLa2p95jSeUDlPPqZ1spZ1EP70Zmg96GS6IzjXPZU61xjMELqcq_e0BEfie3LmsrU70FVZgDd7flWp_BUzSblmL439jeYRJVuvWIxcJqglDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💝
مراحل‌صورتی‌شدن گاوی بعد از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102833" target="_blank">📅 09:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102832">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqzM3FCI3i6xP5UbAVohlP2XtoXMLj2WcXlTHk67zk2MZAmvqoX8Qh0_agd9lR5vpqzJxrfuVtf6gXxwxSGfArVQKY3yHrmfHWEqkGvAZZfXWHnMvC33LIsX6WC7_USVVEtGnp1E5kin3Wy_O6xCCF_pyqKa8QsPAQnxnaPeW-1Huv43832oMzloJ1jpWuzzBa0LDZFW8tQu_7bMDb-mOWFMe0NAEKG2wdjWNQ98WSbhsiiYQrGQLmobATmCEQSlCHSwv47UpZz2P5YM8dMv97on-qjx0YjrK2LuQUWKoUCb8mfuzd4CUQWdAM5qzpSqBL8wL9k3QtDYxQExtl7ttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سرمربیان تیم‌های پریمیرلیگ در فصل‌جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102832" target="_blank">📅 09:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102830">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e40774ac.mp4?token=uO7PinmAqu-fDEcn7nrSl97hQmwV1sY-Dkt5RbbPXMMwSSiJdUPJGUiago5pzycm94UrhM9kKZe4A4xWiPp64QB_mYSygeJ1m8Buqdbn_7Df_cERHVBK5UjExnq-j0RbgqRoDZoUcqSXJ-3jjuYmkKMCa5ZZEt1VvndvlUaikrkZeuZLZ258WfY-b6JIhjt9OEKHf08vfiwgzFpwN-mt2B882W1GM6oimOd2eAUCQl2Ra3peEthF0dNrF8NN0z4WEJJdYXldXPNEbcnazaYq4wR-No6Wc-wa9IpKnTHWTGj21p7FClU9AyajMTM8hM4rPO1EgQ-U98qRMVA8cn53wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e40774ac.mp4?token=uO7PinmAqu-fDEcn7nrSl97hQmwV1sY-Dkt5RbbPXMMwSSiJdUPJGUiago5pzycm94UrhM9kKZe4A4xWiPp64QB_mYSygeJ1m8Buqdbn_7Df_cERHVBK5UjExnq-j0RbgqRoDZoUcqSXJ-3jjuYmkKMCa5ZZEt1VvndvlUaikrkZeuZLZ258WfY-b6JIhjt9OEKHf08vfiwgzFpwN-mt2B882W1GM6oimOd2eAUCQl2Ra3peEthF0dNrF8NN0z4WEJJdYXldXPNEbcnazaYq4wR-No6Wc-wa9IpKnTHWTGj21p7FClU9AyajMTM8hM4rPO1EgQ-U98qRMVA8cn53wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🚀
🔥
🔥
🔥
دبل اسطوره لیونل‌مسی در بازی بامداد امروز تیمش اینترمیامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102830" target="_blank">📅 08:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102829">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3b409b3d.mp4?token=YbDSsCc-bvar8vw7fk8EJD_XOIi7zS0tg0eyFHb6fVVZCnYgn_oy1d0rrTt8ASDIEP8x8kCku6xUWMv8LOowRvndKcY8c4Uf2i0iFRrctz_KL18bTxVMEb7ZlItUOOTpg6nN8Utm6v66e8mEeTIDzhsBWa5xnyYaikg0InCnxeHE9WkR0iwuAjo7mQaiJGJlRCcseD4tC-7D--mfFRTaj2-5OrA0KsNW_JG4_er22ZZwwJmYEfKFRL9iT3LGHLcaLZVpV84dzCuSXYX5r1qMYKOcPU05Jc0evsSsv9s7ARvc9hsuTyY_BTjzfMEdGiDw8S3F-Nj2qWe1CL_Vmw_2Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3b409b3d.mp4?token=YbDSsCc-bvar8vw7fk8EJD_XOIi7zS0tg0eyFHb6fVVZCnYgn_oy1d0rrTt8ASDIEP8x8kCku6xUWMv8LOowRvndKcY8c4Uf2i0iFRrctz_KL18bTxVMEb7ZlItUOOTpg6nN8Utm6v66e8mEeTIDzhsBWa5xnyYaikg0InCnxeHE9WkR0iwuAjo7mQaiJGJlRCcseD4tC-7D--mfFRTaj2-5OrA0KsNW_JG4_er22ZZwwJmYEfKFRL9iT3LGHLcaLZVpV84dzCuSXYX5r1qMYKOcPU05Jc0evsSsv9s7ARvc9hsuTyY_BTjzfMEdGiDw8S3F-Nj2qWe1CL_Vmw_2Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
رئال‌مادرید و وینیسیوس در آستانه تمدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102829" target="_blank">📅 03:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102828">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a87de8fd.mp4?token=v1pgdLhAxp4IkV2yLWX71bLVONJllgK3kv-RY30B3SFb1FEecLo7v3vvfXGOUYOQOxVaYd3Xww5kaA-x_MLAg123qWhvIrCW-hcO452Zk8qgraHak9ntoDW1x676Cz3JhVCBaTi697zm38ywyU1ZLw7kR4ZGqFzvTKE2KLobAz_TwiDdlETPq5pvM29i9VQbnFrrWCBrJjvlrmochM1oekKgMNvGhNe5kC8c9-yaV3YIbwx8F4VcnZbOlZTjjxvtsnnMX53OoI7QdkyZjjb_mjNp8nCKM-73tPQqcUIfqGf_VKCAPYLAS9OofCaPIZXy6hVH-4eKERQu52WTajTE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a87de8fd.mp4?token=v1pgdLhAxp4IkV2yLWX71bLVONJllgK3kv-RY30B3SFb1FEecLo7v3vvfXGOUYOQOxVaYd3Xww5kaA-x_MLAg123qWhvIrCW-hcO452Zk8qgraHak9ntoDW1x676Cz3JhVCBaTi697zm38ywyU1ZLw7kR4ZGqFzvTKE2KLobAz_TwiDdlETPq5pvM29i9VQbnFrrWCBrJjvlrmochM1oekKgMNvGhNe5kC8c9-yaV3YIbwx8F4VcnZbOlZTjjxvtsnnMX53OoI7QdkyZjjb_mjNp8nCKM-73tPQqcUIfqGf_VKCAPYLAS9OofCaPIZXy6hVH-4eKERQu52WTajTE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
حسن‌روحانی: «یک اقلیتی هستند که می‌گویند اگر این جنگ گسترش بیابد، امام زمان زودتر ظهور می‌کند و برای ظهور امام باید جنگ را تشدید کنیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102828" target="_blank">📅 02:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102827">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJwrgxg3oS5JT4MyXRuCiPmdBqOnjSZnkw5VN6yuMXSyA7KiSnUmkmThVWguOJciCNwL3X0JLWB1b0mROS6DpThTo-TBsLhKGwGnE5gI87NwOm9qCkryk-DFruiQZ_4qVXN5Nh21oEfGTjpi_thKF-Y0AFi2EcrD6K0tzRiV3pyJ871_hOCN6mLHbnuOsw4ABbDUaKDUC6X-f-rQoMO_lFQygmzx2fTBxtRRZ4bTYmxKa09fSn2_JCAYEagWByT3IQTYydt3ndk1N-ygzcpOanhCVgOD4i9OOLrv8MhvedpjqvYnw8LSNw9SSxtCNbm4oJieT7FxTpygE0R8b4x-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
✅
🇦🇷
لیونل‌مسی در ترکیب اصلی بامداد امروز اینترمیامی برای بازی با سن‌لوئیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102827" target="_blank">📅 02:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102825">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9dWfjSZf9SIag-ZXuHWaFGhCD7PT9PGB-tXT5otNh4Tb4cVgEHWC9IFBR7WN3in7g2_CRrrZfe-_m74Cx655MP5TCw2Ugm3InWePyfFX1wza2jHhyziCjrI8CtoDjIj9rZSxSz1wtamW-hlqa5jNshH7VBINzCp9i6pECsFiKrE4aesyHbf9BqzVTGxkcKiOXxNmkNYGNBoq2o3ES5dJ2BLJdbwlJwXW0_qvJu-TYn1HOZIqpc-0J9-UuQ9Jf6NCfNZfX8uTUGEhGWESxQ61HntZ1vSEpihWDXVcWOariCFpoHPEwFdYxCf-e2sX1dqpn_gwaK7AdJcqiwq66D6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
اعلامیه‌رسمی انتقال دیومانده به رئال‌مادرید طی ساعات‌آینده منتشر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102825" target="_blank">📅 01:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec57fa35e5.mp4?token=ukh5rD2zb-hPMw_IsMMhy7HTMOOlo-3Jvm9zdztEeaCyVg0YGt-O_7GlpJtB2bcJsOCjfg3YKanJfmx0I80p3wj24djs_zGZtvrQG6wWrGy6pMkiIA3H8J9fe8mLxvTLRhYwinNphvlh9TnVCtMn0hcBMDr8fXGYDES7CbNVBl5ZpPylFrOycI4idmPLG6NI1cBSwt0WNl_7rQMAGtnv2tkB7f2yDnuyj9vOEOBhiLfDXpqIonJ4WJXbTrwCc6M9Iax4CMKXI9tTscMu8-N-NovN_vpDr-tFiqmiVfNfvLqsizrHoh1EesaujPdStkdsmKtQhNZnwH-Et5Ht5IL7HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec57fa35e5.mp4?token=ukh5rD2zb-hPMw_IsMMhy7HTMOOlo-3Jvm9zdztEeaCyVg0YGt-O_7GlpJtB2bcJsOCjfg3YKanJfmx0I80p3wj24djs_zGZtvrQG6wWrGy6pMkiIA3H8J9fe8mLxvTLRhYwinNphvlh9TnVCtMn0hcBMDr8fXGYDES7CbNVBl5ZpPylFrOycI4idmPLG6NI1cBSwt0WNl_7rQMAGtnv2tkB7f2yDnuyj9vOEOBhiLfDXpqIonJ4WJXbTrwCc6M9Iax4CMKXI9tTscMu8-N-NovN_vpDr-tFiqmiVfNfvLqsizrHoh1EesaujPdStkdsmKtQhNZnwH-Et5Ht5IL7HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
‼️
خرازی دبیرکل حزب‌الله ایران و برادرزن مسعود خامنه‌ای:
ما باید از جمهوری اسلامی گذر کنیم و به حکومت اسلامی برسیم. علت اینکه این الدنگ (پزشکیان) رئیس جمهور شده و بی‌حجابی کشور رو گرفته اینه که هنوز از جمهوری اسلامی گذر نکردیم! خدا لعنت کنه شورای نگهبان رو که این آشغال رو توی پاچه ملت کرد. چهل ساله که با آقا مجتبی رفیقم و خیلی تندتر از پدرشه اما یار نداره. باید به نیت حضرت فاطمه از هر شهر 530 نفر جمع کنیم به تهران بریم و کار دولت پزشکیان رو تمام کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102823" target="_blank">📅 01:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb48689a3.mp4?token=YKfLfFseumFZvFe76DcgGoNBt_o5GpEsvlYK4L49MHBPIM6Sh_TLd4jhno17iXs1wCNKP_YxntKSr0rN1Vk_xiXAJAnUY-tPeOEpHpk07RyRYfMK1RV8NhLr-dK1ZgT2rCnHRbiCuIGXFLb8alCwtVUhlSTYtW1auiB7j6CFR7LQ2hW_HshNB82ddDaMSJzWsTrsX0Lb1O-bQlDP9KsymNfNNfyyaex6meMkpiDQQQjwI0R8sGoVWPWpFuNsH0Tna5zivKzsthiYv5WItJQz2y6iKRtdSniXfAP6g0QiSHC-4fRvI5s3Qxyv-xTTdiOft-1MhGvA2gywoMz_YbfqrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb48689a3.mp4?token=YKfLfFseumFZvFe76DcgGoNBt_o5GpEsvlYK4L49MHBPIM6Sh_TLd4jhno17iXs1wCNKP_YxntKSr0rN1Vk_xiXAJAnUY-tPeOEpHpk07RyRYfMK1RV8NhLr-dK1ZgT2rCnHRbiCuIGXFLb8alCwtVUhlSTYtW1auiB7j6CFR7LQ2hW_HshNB82ddDaMSJzWsTrsX0Lb1O-bQlDP9KsymNfNNfyyaex6meMkpiDQQQjwI0R8sGoVWPWpFuNsH0Tna5zivKzsthiYv5WItJQz2y6iKRtdSniXfAP6g0QiSHC-4fRvI5s3Qxyv-xTTdiOft-1MhGvA2gywoMz_YbfqrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
تفریحات علیرضا فغانی در ایام‌تابستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102822" target="_blank">📅 01:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmIALxeJtyMquKpXEIAs8sFpXHd7D5U48bZv0j2PrWuRSQrLYouuc4RTfBRPk7AzA6f1eiHV70Gh7nuaiIUxG4HTVjD60gUCu-3gHB5YKwnslcPYBPRMR1j6B7KtINN_8tLieSW8hb90WHdeu-uPPyKmBOWML2huRn8mJBcXZ5U6RYvL2vN0skZg4qPft08ZmheZ38nYtLreEsuQJyyygzoMZ6F_RITzQP70US0dcccvHpPdYVXqCKwRrBohIp5CXisvlcLZlfHSo23BoLFbPMgwRv-VlWf3HkfbTLcAfTxyfa1hzzJFf53NYETPhUMOQuqSAzfbZhpi7OY8SDJnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پایان‌بازی‌دوستانه؛
🇪🇸
مایورکا
😆
-
😏
PSG
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102821" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgdmFBCjz_6N-b6qCQM8-UqGW8oE7EYET11ODVSDd0Abtoz3a1e4vnvCFiisW-fww4XjuSTQUMLTecGgkuRQEeT3dfO98_rogNhSsu96vDcaIlPnMjN9oId9PAJl-y99uL9CXYix0M3IMwiKPkwPdM6Rszz1Ib6lovm8w7L61VwqCOvUGK4DmhHr1Ke813lCIPKIgcPGJ9XANkM7i5aDhwpsm4DQ0LB7omvm0mUBLnFmQYEDvdiqYhRVZnZBwH1LinJ6wyaXtDf7VmIHrrlCWXf5muS1eeqwLDlirdwher1OeJwmzpXg7G8YL2H2Kt3qC1ObrCMrlGJZAVbx8wsJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🗞
اصلانی‌با عقد قراردادی راهی لایپزیگ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102820" target="_blank">📅 00:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2pPkWVvNjOPiyIpDyCLRAYcCkDGoY625ABdMUBK_eFNBxYVRHMpHaZ6xhFXyxCxiJOQzJgnBNCUNByw4KuLCOUs-o6MGWyXoiBpgKoV_NYoqT8dOZbkNrP_A7yli0YUlS0YbOw-4vsla64agmniZT9ki2e8jibAhh9CH98KHnBYaptLDdMNQTS3_KSl4f6MSJkTRagQWEKNYFJdPX8G7-Z6MycEqwFHMUle7qhvGMYmwdMauEQrbCzYPiRyDMc4bSil1KwCm6JjFncJhBZXGWdugOEedhiumdE-KsNCGq-VQvzN1W_UVu0c3OxmNww8PyeXqujYea59EW86kUdJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پایان‌بازی دوستانه؛
⚽️
آرسنال
😃
-
😆
بتیس
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102819" target="_blank">📅 00:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/102818" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102818" target="_blank">📅 00:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=s1D6oSOlUpYppRUxOM_KvKIP_yn20-J_O3pOP9QJZcxWl7_LxwoCWiRZU-NS2WqWkpSldUXN5mOt7TinLOqbKDXoW91X4d0mQ8_PGoOL-s3jp5etVmS_J7xujsf5Tp2FweVZ1PPQb_0GI_iyZPN71ln_X410jNqCLOiyNwpY4edpPXSZfBXoMaZRMw4cj5XOUD3e6hfFuhCv_l1txw38QtMhUmkEasWx6ztBilzym0lh78-XOXMQM0uinUrmO2daLWyA2HYmjsyVxaFutD2xPeO-ZX2Cm0jNJEvb_b7moDgKzhFcOnZKtyqmire7Bf4xeP7QnTpQRM0BTR1FPcb9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=s1D6oSOlUpYppRUxOM_KvKIP_yn20-J_O3pOP9QJZcxWl7_LxwoCWiRZU-NS2WqWkpSldUXN5mOt7TinLOqbKDXoW91X4d0mQ8_PGoOL-s3jp5etVmS_J7xujsf5Tp2FweVZ1PPQb_0GI_iyZPN71ln_X410jNqCLOiyNwpY4edpPXSZfBXoMaZRMw4cj5XOUD3e6hfFuhCv_l1txw38QtMhUmkEasWx6ztBilzym0lh78-XOXMQM0uinUrmO2daLWyA2HYmjsyVxaFutD2xPeO-ZX2Cm0jNJEvb_b7moDgKzhFcOnZKtyqmire7Bf4xeP7QnTpQRM0BTR1FPcb9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a14
@betinjabet</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102817" target="_blank">📅 00:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaeDplIUDMqOMnzm_FUdpFUMIswdkX5HPqkDSQyGREM4dB4Cw1C8Mf5Vc43WzeTa5CeH6k8gMqNP_W4l82D00f9bvhcPX-QyK20IxAk534wOxUPAmxk4K03ulU1Fv15rb-vK4bCx2vboWooA0ls60iNfVUmzKTou4fUtsg4EYTYA2m37gHa7rOy3o2RQ99nm1-lqA62OJ36Ichyehl3jnRAZI54g_nJYV4ZPPUtITGaV4JOt3dgSxB5YxMvLD4lBOWYmF9KhyWIrYWTzGNj8CSgemORMwW_LiFHgWCXQoLnO192UJrlkal9Qpgu2egrzhFyDopeth30BUIteV-qe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💭
کامنت یه کاربر زیر پست تلگرام:
من آدرس مخفیگاه پاول دروف رو می‌خوام.
‼️
📱
اکانت رسمی تلگرام:
اونو که نمی‌دونم ولی منو می‌تونی تو خونه مامانت پیدا کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102816" target="_blank">📅 00:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fd322bcb.mp4?token=Bs_CaLGRG-ofz1lX_tBrEV9Tb05Z_ma3z5WilU94F3fywnNg4iO5Km0Er6iHp1WymsRxaBClLrS2Lrr---1xekWitWnzoJFa-VKG4qxp3qAG-PPUS4JKfFwq71GjcjSzaqAPZQgJXaupM4exWFT7XrXjeA3hW59y2-Z-r-w6EPAzYNn7-BNf5SacVQ4i9ctGmGAs9mRQdQQVCQIFBOQ5ezyh_cow925mxvEOnymY3uuW-Cth342asYbEzIpuD634zmU1wHWSvM8RC7tYxSZ2s6dsFOhGQmj8E7YHziejbnV1_G6maThUEI-32_RS2UGt2dQIg8gUoSvlLKcVGPEFYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fd322bcb.mp4?token=Bs_CaLGRG-ofz1lX_tBrEV9Tb05Z_ma3z5WilU94F3fywnNg4iO5Km0Er6iHp1WymsRxaBClLrS2Lrr---1xekWitWnzoJFa-VKG4qxp3qAG-PPUS4JKfFwq71GjcjSzaqAPZQgJXaupM4exWFT7XrXjeA3hW59y2-Z-r-w6EPAzYNn7-BNf5SacVQ4i9ctGmGAs9mRQdQQVCQIFBOQ5ezyh_cow925mxvEOnymY3uuW-Cth342asYbEzIpuD634zmU1wHWSvM8RC7tYxSZ2s6dsFOhGQmj8E7YHziejbnV1_G6maThUEI-32_RS2UGt2dQIg8gUoSvlLKcVGPEFYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا مدیرعامل باشگاه استقلال: از عملکردم در مدت اخیر رضایت ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102815" target="_blank">📅 00:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP40D9F30psN-Tju7rV8FUsCor5ijGGcPAwyXsHpPr8GOvbedQfQlHDNgvCTXmNlFiDdZvY28oNzOaS-Mlw7q5xDyo-c8ArZ38BcOWLl-O4T3W5egn1Np8iUJy3v9pZow8rOApBOnN1ltDBHtBg9sG_f_gPys759f37j3enpyurNLSRjkF5Ya84jUEX6QfA-9M8ov7rVh4oMODbT8mml8o014cMXHMHkQ2Fe5n_MIMLJQ65v2yxSA_csvPp5CcUgbwewwFK_gYGU1OcmYR4qp8Zo6SAy0DnETJ3Y0ZyLvCcDPoKBbRzTlajUFF3UXZIVkdpCKwXv73DU9SllutOl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد صلاح:
من تو زندگیم تاحالا همچین چیزی رو ندیده بودم، 25 هزار نفر فقط برای خوش‌آمدگویی به من اینجا حاضر شده بودن، این باور نکردنیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102814" target="_blank">📅 00:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102813">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102813" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7IA22RfNJOdhtpFD2zNaO8eeS8dUSaWzZxwGB2IsEcrk0WAVocj88pdybalg5RNNqNaygjG-Yg9qEWYrtQ47bUfj4nZumJmJKB9s5f74RUp2l4UoghrnihU82xXYW0lyCIxuUz9fuaik9EzkfQdCfTdUiASA391nGDnpkMYWo9pSVikcFRi59ogOiIUEPCwG850gJRBznwtPtpLRJNlZhI8g6ZSGhPGF1fDLhd_0hOJw-i7q753BCJh3u4TVin0ck9YUz4Ms1PLVdRtFNjHruIYVytpvAwNaA1Qpvc5CBWzbKXzfMHXxg4NpJ7w_gcRECoLTR2fDRTzKrovcQE86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه تلاش و پشتکار:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102812" target="_blank">📅 23:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102811">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv_EMleGhaJ2Zv9h_eVbxIYkd8XjiZaNp2BWzkpbGJvHWWy4RkpF7BKI5rbe31EMNj2m91KHXMKEk6kC8I1GhqWuD1WTrPW6Guoj-VqRWlcQwzQjvPJ6mp7PsAmJ224VmN6A6-2RsW7nwM4SD29TKHMgWaoJHgyPehoLBmEg6S_wb7-66kPmERnhDma15eqL3l7Y25oWk73zDTtsgP4P35X4nYx8yp3306vbwUm0C00Em8VjD0XOIjIT6un_ISS8YAjIcAPQ2AsYXyKWbjnd_pJBBX9fjXfvpObXv7NSs8dQTo_gXAZRPHiOjl9SZ2IeGJMtZqh43-OgJb5L7sAXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد صلاح:
من سخت تلاش میکنم تا در لیگ و در اروپا به موفقیت برسیم، چون من تو هر تیمی که بازی کردم، موفق بودم و همیشه یک بازیکن فوق العاده بودم، و این چیزیه که باید اینجا انجام بدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102811" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102810">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/102810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102810" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102807">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBjFr2_xlhuzRNGSgSgr3Zrw1PDrC_VXjRQTDUUzgdPmeWxvpqIDqhV87ghuWaLGAYzGeGl9lh665cdBZHvf4OVbaVJJui1R56gSY19UPCZNtvwqJVil2Yy_91RjrytO7vPSnicUppHqT6nn-Q6JMaWM8ntLr5_AoJYIgWbG2vcY9I0mNw_HPqu317tKYrCCUaDBROwGPCBfmVhIRZ71lqGL6er3UAfG4wgYHW04o9o9xLwem2Ig9Cap3z4L937ASukOKJbfT0IF9rDkYR8tBDkt4bF2OwGFHhHffbltbrThjt_rjmr_TtnuYjPdnIL0JkL4nHFPBgdJc6byYemE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyqG0Ck4kebPut_1y8BvvxNZHucv93uJZS-Tlm1vO1b5UBmnHHnE6o_pXORQnabEYBKTnDtYtu3Qm4GxNrZskAbcLDeWjqC9nDL3D5xj1xzEELJ9XRqpwMvsxUlnnoZvCCSHR70tgyg5Xn8aKtEmAAXQ2McXThHQWCPd9JdikAbjIEBsCt7Tr6De0QCuxP1fXjOuXGY3flyQ5Wlr247-KlGpsFrgGSq8oja0764uNSeMKV57v0eJyHeCgNv_WDKQR6yLn6TE-Jhygp6gYuMhLLu0vH1JXQie6yoLTMEOi4qoYGqfNV_ebpyc6jkzfOQWIfSN02agTp_JSoRckOXRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1r5df2mFjtcu21w5na4Pail4dL-zjaAMPn7-1KMgMLpJ_-ocju-WGhhB6rznZRA6cErFTrWrHoNKOuAugbQ7jbDcI75QhejzOWmFUM8wpAhWy1CbvKUv711siHjDRM3dv9igbmSYif66sRXTD2mY_3BxYAweP1Bbql3jy92FxEOY-B5CdWKDwNvBevHemIebN1NKR7AhR9i5Mq27NSGsF9ZIV5-MJgZYBcMpZGbBiXAPzjMcDv8sTbjLQNbohjL0l1Il8j-462pfx8AZ_AS5fS2DH5iQqclnr6ZTI50PJKtdZznN0dsHaGIZADKG9OyJ95QrzKTuWdJPkamnudq9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استقبال برگ ریزون هوادارای ترابزون از صلاح رو ببیند و کیف کنید.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102807" target="_blank">📅 22:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oncZ--quFdfw8FdfxXzb688QEqDKCmTp1ol8OWeEFvfQds6JUIajW3l_KHHVsp6R4U54ZiI5P3wfRPRt1CfEixMoRWZMotny5KIPqPLnpyKqcI9e0FLJLqWDSOmCT2pb6sKYPxCl1ePX-F4EM1jIohzb94z--9U8Qg-LX-9IIuSXjKxZoYIbDIqdsrhUlwJzN4WQVwnV9OVWRlHqjkmoeBy4rDlauKo2LFad5g1ku7La0BVgRZ4F2o5zuQie04yEMtPxZ6a0dzr1z_XOIv-41h_ShZVlEE91CnQcZmcOuxJYgg2slgT9RpVTb0YiiWBebNmIevvEAva00dpAY0dsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
‼️
وینیسیوس در اقدامی ایرانی طور تمامی پست‌های صفحه اینستاگرام خودش رو حذف کرد و عکس پروفایلش رو هم برداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102806" target="_blank">📅 22:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ8dYXei0MHfl0aqrgt8zKRhVZtIooi2VgrCW-FP5Idp4MgThxBEy2lfnbSiPA9jysbGNFquFIoLcR2Jwxp-qRoAKY0S07ObXHrtbKUpUiu0rAjbr2WVC0iFpyMkoUoFGUyvfg0ibIHZ3H4XMXsF2Gg6vVvMfY6PnCZmWernVWSy4MQIhX5APQwjkcjz_8vkrpPhynC7dUDHlNrJIOABoN-U7GL0liBopm6myDzEfVHANp3d2F7IwH5eZWNov7aGChdFNhOa5m5L1t25Wv30_YycVCVe1gf2sKqCZ7_yonDf6Dk7_tg4N01ne-k0vMlb2gHI2gc-E75yJWQDc9Z2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
رومانو: ژوزه‌مورینیو شخصا در پرونده تمدید قرارداد وینیسیوس جونیور وارد عمل شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102805" target="_blank">📅 21:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htPYzc2RVBf1ocvDnU1xpdM8k9omqvyZkaXvJ-yDoHtXmZiZ6wpPCJGflRzk6akykjFtzlKZewv7PQUgwjd-83o8F6eoAOr4LitDV3izIS72s2YBAWZLYQSotoa5RYrp2_jJgZPvxoVj1RQP17IiKVmSjwVpxHcJUAgbQpOGm0BaD5_TEP2Vi1_2l_h08XOtEgCL3ZoFNv9Fdkg7mQWOQwSU4mRac9xtTHKwxzDaMPxNEhwoZkpffQmmyumPXdeBvTlYIpiGLzu8VN_OEoBzd7TCPUWrF8wJuQQ1pu7_y8NQ3G3ZXfYcTDDQ5GfIYCdV940yQEHds6fRRsD9O3m7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
کوکوریا و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102804" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102803">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCduLpiQbvJRhW2eTS1-mxX2MzKQ73X6ZBEY2ZGQXJ0CkQsd4f5IRJBZnnzZSBU_Ae2NjDNfvibqR4Z_WT8ngmjw_Ju72PjXwf0dlDDDU23siGsr_q9dp9ChTFmiC8pa77jXt7wJoGQmzXnOD9rDzSo0Rx9mN6xfr6tixhVjnHlOimzXaWksJjy6HrYYZVayMcHarnFo3qM7tA4RQvNXw1tii18I4nSQI6PeXuLXMglI7_oj8AsIjuqbvQSsrDcdjePv37ILkwJh7AmHmNx9_Rcop_cUhKXgVdQZ1-P4k4LeK6w80_7Pk_xtTXPjwU_avA2KOTffG7SGEuWwhM9uwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تاریخ
مرحله گروهی لیگ قهرمانان اروپا:
هفته اول: 8 تا 10 سپتامبر 2026
هفته دوم: 13/14 اکتبر 2026
هفته سوم: 20/21 اکتبر 2026
هفته چهارم: 3/4 نوامبر 2026
هفته پنجم: 24/25 نوامبر 2026
هفته ششم: 8/9 دسامبر 2026
هفته هفتم: 19/20 ژانویه 2027
هفته هشتم: 27 ژانویه 2027
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102803" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102802">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQQiiRAEvKN_rFGGfyOipu4NIEvyVJEdZ6Ia8nXBYD4pZGBq03Ro4VPyIW9eME3mp96ofxPGj0OrF99vdg86YHx6aW9ti7_P5LO1VR4LBQEqgn6Mme2jyzJ4-mfRlNFaWTc46IMYTuh8YrCJJgaHNlChLY7ot06YaQFAk2n1itJYZU33toHQenOMQczXBN-U0sT5kFrCgjekej3x9WIl11D_pFfIuKoAO84kZL7Sx_MjqbP0KuhkEFpmlOmArmGNsATjLi10G9HodeJyLGxJmIVAarLKybf4iKdCJbczzeiK8O_uoXM8dvlJD0XaYJKAL7dkRACQCE1q8guUtwUR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇲🇦
جیانی اینفانتینو به مراکش پیشنهاد داد که در صورت حمایت این کشور برای ابقای او به عنوان رئیس فدراسیون بین‌المللی فوتبال (فیفا)، میزبان فینال جام جهانی 2030 باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102802" target="_blank">📅 20:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102801">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=r4NVFu3vknprsLDal8-pNaKB5_ZOV5T9nciubtQtx3rqcTZAooboFoedaDquSMKQ9zcGxqaAV_ewuvRWM6-RrEfUdl6F65Et_xuf2xl7rUIj8tBHaJ8pvcKq8KHYpfmivw_Lo3nxMK4Gd1AWeySHElBCLyHFMxw4vEtfmGs_9faeTJpup-AR2aEVtpOvAbq_-rBRlHlsHQGpND5TwQJ3mcbDyc1V3rKB5escusHFaA_nr-9ICHVMoTy0u8HQKjZ2ehqIVys85pIBUauvS2lvuct2qV85NQvxa_-CFB3uUS1RlPpNc6MmWijo3zul5Tromo0GhH5naEWGwYUyzrCDrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=r4NVFu3vknprsLDal8-pNaKB5_ZOV5T9nciubtQtx3rqcTZAooboFoedaDquSMKQ9zcGxqaAV_ewuvRWM6-RrEfUdl6F65Et_xuf2xl7rUIj8tBHaJ8pvcKq8KHYpfmivw_Lo3nxMK4Gd1AWeySHElBCLyHFMxw4vEtfmGs_9faeTJpup-AR2aEVtpOvAbq_-rBRlHlsHQGpND5TwQJ3mcbDyc1V3rKB5escusHFaA_nr-9ICHVMoTy0u8HQKjZ2ehqIVys85pIBUauvS2lvuct2qV85NQvxa_-CFB3uUS1RlPpNc6MmWijo3zul5Tromo0GhH5naEWGwYUyzrCDrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8/5/2021
💔
🇪🇸
🗓
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102801" target="_blank">📅 20:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102800">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr181opHXdU4VrgBZThmcFYcrfG6j43yFncLtD_Ry0ibtNGSXSouWF0Q9raSTub0YQycaedWhWF-t8aPOAOuHpthjF3lu9ZtHpCmFAL0mm4NUzdGOosvjxjrSwp-d9C1PXtuHL4sPzIpqdNtuzkJuPhiKUZmeOzmfoKZVylmGyiU0gQutebbLwJPdpo2dg_agNnyjwOx2y6UmFZLPFuZEjBHOWIpRux9DE8iRsW35OwJzBL-iML_WztCDFZEKlHNUk5RHzJJIDtCw7xPjZCRjMN4U_6_jGyNDUWudcaAZgxtFnYltNvgHv-habzRJGkwXt7ykBSlOGs7CNsKfxp_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
استوری جدید رونالدو در حال صفا و آرامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102800" target="_blank">📅 19:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102799">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b7936557.mp4?token=UabXrTbJ0_ubGg9hqjsiTW4oRmNYhUSQtEe0pzNTJDfIq0vJ0OWsoiUBCBbl9nlibjv3fLMSlYk3KDp3npkaog-RyC0eo0OkdPBCGdyx3avEXBErDH0HnmIIpYDptpXryRoC1T1CgDDgiqA-f5V3P8ZYjK600t_6U51ZcBRRUamoQ3xckM2O22hK7gvqJkSLIFiuglFdaClTT6WVjv0UMoM0imaIogb2q5kabdyHzylgXYCEmqcy7b-EGIaTCZkBQgTA531njQuwi8KnshLBA_QkwdtwY1s8-iqo6rDyLVRw9Vt3bQzt2_j8vWozcNkejQ3H4RpRFb_FMUmvrJD1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b7936557.mp4?token=UabXrTbJ0_ubGg9hqjsiTW4oRmNYhUSQtEe0pzNTJDfIq0vJ0OWsoiUBCBbl9nlibjv3fLMSlYk3KDp3npkaog-RyC0eo0OkdPBCGdyx3avEXBErDH0HnmIIpYDptpXryRoC1T1CgDDgiqA-f5V3P8ZYjK600t_6U51ZcBRRUamoQ3xckM2O22hK7gvqJkSLIFiuglFdaClTT6WVjv0UMoM0imaIogb2q5kabdyHzylgXYCEmqcy7b-EGIaTCZkBQgTA531njQuwi8KnshLBA_QkwdtwY1s8-iqo6rDyLVRw9Vt3bQzt2_j8vWozcNkejQ3H4RpRFb_FMUmvrJD1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادمین صفحه رئال‌مادرید بازیکناشو اسکل کرده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102799" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102798">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_zXNWOGbHKDZQe5vOLaH_x8XYVmXHtsrk8J_mNNFNjtiM6UE-0VyLWo9jxlqwTSfNHNaVD40DYUQIoK_aj8IkYPSBp8Oy-esafeMKQyKM4ELn-s-1DBXq9mQZmgGaYZn8137Oxckwi_6oXOOhsjoIyixyPKacSc9frqBP0IgXApPnYZYXFXBc3wyU0vrKSoYbf2-tq1wT_wATGAOQ_UTCIhgUEpzpQK9Mg2PqSZtam9vht1-nhz_NfztwLJMvF5QdQMD5BNHrxWK9afauHBBMqQTArTniJ73HuaCTT3A64Wk-DCN-S-CMIEqB-exgEMjyjhCiIBFmiEZLBpey5QoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🗞
با اعلام رومانو، مولینا مدافع راست اتلتیکومادرید راهی آا‌س‌رم شد
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102798" target="_blank">📅 19:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102797">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=vK62w3kxyLZIs9xqcij_QX_IkK_Fqp5hFwI-mJfy_BfMAvsiHHoyMwYg8AbLo5Nna6hmHmAj1mXJGCANSBWVbuJUrIZ9MP334oNe6SxgnN7umFZfXcFEbSV8CbXpxmUwLQivIX0ZmJjbUqWJF_SRjXxaiki1TsaNWXq4vmGnYmQ50RAM20YagM-51thfvM-hUA6tYMtvDbu5_9vWhjB4aNA-zXHH5S99SRgTIo3kCU4BUIqgQZwvFNtEy2JsC3OLesCF1Z8mzyDzCBY39mvduKoeXGi_FuUpbeO2sR1RNS_0Ap1rUUVaOyVaz8-E2Ni9rIDlB2ccGDS7EUZ3bV-nwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=vK62w3kxyLZIs9xqcij_QX_IkK_Fqp5hFwI-mJfy_BfMAvsiHHoyMwYg8AbLo5Nna6hmHmAj1mXJGCANSBWVbuJUrIZ9MP334oNe6SxgnN7umFZfXcFEbSV8CbXpxmUwLQivIX0ZmJjbUqWJF_SRjXxaiki1TsaNWXq4vmGnYmQ50RAM20YagM-51thfvM-hUA6tYMtvDbu5_9vWhjB4aNA-zXHH5S99SRgTIo3kCU4BUIqgQZwvFNtEy2JsC3OLesCF1Z8mzyDzCBY39mvduKoeXGi_FuUpbeO2sR1RNS_0Ap1rUUVaOyVaz8-E2Ni9rIDlB2ccGDS7EUZ3bV-nwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚠️
هشدار، ویدیو حاوی صحنه دلخراش می باشد: صاعقه یک بازیکن فوتبال را در حین مسابقه در تایلند کشت
❌
تلاش‌ها برای احیای او در زمین بی‌نتیجه ماند. به گزارش رسانه‌های محلی، ۱۲ نفر دیگر نیز مجروح شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102797" target="_blank">📅 19:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102796">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVb4VgzxnVQrFSNNDRb-wSnCBvT5lLvMw5VYrSmWAL7lbXZ9NhRGtR87ULcIuPruIzOgtlJQTeTPnZMEhcrQocdv_1fp16sb3oe0GuyihdKbEmBButqUJ3g_8sGqK6UAlIhrQptdalOXJrZ56jdGg7qK5HfftXp5GdYWR7cDxthPJo3K8beFzMcGONLvtw9-Sq3fpOXVQJrBbj610epmIlfi2e0pKRDQIMbg9Bub993kTwmW7DVx4p25WMr-bQPw_LPEaoaGrnOF6bryZEFVlYAymcf9kyBSxDcf0c8ojyBsajifurCYdQiq6B8k3l0zHsAuUDZqgzmWxKv7KxXRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
💥
جزئیات انتقال دیومانده از لایپزیگ به رئال‌مادرید به نقل از فلوریان پلتنبرگ:
🥶
مبلغ اصلی ۱۲۵ میلیون یورو
🫣
مبلغ اصلی با آپشن حدود ۱۳۵ میلیون یورو
✅
۵ درصد از حق فروش به لگانس‌اسپانیا تعلق داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102796" target="_blank">📅 19:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102795">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZJBnNuGIBWGRepBebqi-1PGaEhxymkThk21ggJidxcBEH76o9YfmS6AZPYzoPFXC-mvWidkVGra2ooP94bPdEkjIMNVL3J9uNcmim-0jG06stR2zhHnyg3-_q71TYWPF-R527iFl1D6EptKhQzQMoNDpkndM2rrAiVjthY-QzP9dcWNfQt7upCiFcdW7t_oP3WQXVhM5xADcRWY8oGKZfMDO_UoPu5vJIgROQXp9BBqSYjVhX6YD2vUayt-89Jwf8hqYddo_9YJbhYR4Jb0Scu7v70vP1QVd-6KmXbsOWFh9bFcc8aZOXNVymVJ6zvAjhqW2decLHc6CQGZ12S2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
از اسکای‌اسپورت: وینیسیوس جونیور پس از مذاکرات امروز با رئال‌مادرید شانس بسیار زیادی برای تمدید قراردادش دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102795" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102794">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=Mz9DIwbGSyha2m4f-Jn5u7MgAXVuCn2YCnAM-Zb7weGhhVJryEFi-AN3QrwL4dDbw7LILf0AFDfDoF1nlAf989YM2yHabl7MV9M_oqnK4xCm2HpdR_LPKI0ttKNnPmE6FfemiwKqE7zbJJbvCbGRGBMGUcihpytQu6qVdGwykhTMACIUMocTaVE3FT_50RE1OLi7FfSaTfTxIeCxCcTeJKcZrUzIremDXEy3FiCIsvX6XI_rPoVIK6BY815-zDVGw5FGp_ozDPUUN8MYvr_11DgNvO4mvEPLtnxURkdSBXSNsMXuCFKximYUV37j6t3_81WMzy7Cgci_-wCi9lSVgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=Mz9DIwbGSyha2m4f-Jn5u7MgAXVuCn2YCnAM-Zb7weGhhVJryEFi-AN3QrwL4dDbw7LILf0AFDfDoF1nlAf989YM2yHabl7MV9M_oqnK4xCm2HpdR_LPKI0ttKNnPmE6FfemiwKqE7zbJJbvCbGRGBMGUcihpytQu6qVdGwykhTMACIUMocTaVE3FT_50RE1OLi7FfSaTfTxIeCxCcTeJKcZrUzIremDXEy3FiCIsvX6XI_rPoVIK6BY815-zDVGw5FGp_ozDPUUN8MYvr_11DgNvO4mvEPLtnxURkdSBXSNsMXuCFKximYUV37j6t3_81WMzy7Cgci_-wCi9lSVgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
وینیسیوس گذشته خودشو فراموش کرده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102794" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102793">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102793" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102792">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhRxfjh3zwAUwitgWAjfbwirLeGI3Y7nZFyH_b2qTDp5hrO_DeG8oFbmNBuqVeYng3U4qzjAFgsikXWEO-dGXdRsy2mr7Goqg67zmAme4LM1LjdGUD37V2G0AbV_K1tSbBOCt_gx95vE7bpbFrC4f5ng7Wwru4B_edijhGay9XA2Tj4QHtRo7r7gn7dY9lrkUV8qpFqJSTSyDCFPtAIzYl2PWeYtc1Ous6vDXtqethBhawOBSD60hMuAG2Vug2RTT1IlBYxhI11mJBkcTw1ZQkT-AxpY30cc1z9LN8hmTVrLX0BOt9txerDKgnGS-P92jVyU7Q8pdABfo5K-2FNN9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102792" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102791">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=OzDG7NPjQy3q8L7k4QI2Cfpl5htn7p_ZrS33TYk7pZ1f3sTMY1XWCdN45SVh2-D94MOQjPDQwnPpvNL2e3ju-kL2Pfp0xyLpF9VE1AXoVQ6JSMqe8G2g6w7bI_H85swsSzu2bvC9ffe3rKQ8Dp7ej76qoPVDaqYmZPbVBAgi6a0yzgLEfYlvKVZfLxslGfk58UfECt9M_dRA8oVttM1w6GzoGcgtoJGUNts1PL5ujPMRq7A5AiISAmBislO0CVbIFw7pXIQccNvMQIa8yCPKY2mrE6z9EF5j2bL1I85QkcNKFa9Ib2a9IdMrO9wsVnVXE1H0svEqLlhvmt7jxcxYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=OzDG7NPjQy3q8L7k4QI2Cfpl5htn7p_ZrS33TYk7pZ1f3sTMY1XWCdN45SVh2-D94MOQjPDQwnPpvNL2e3ju-kL2Pfp0xyLpF9VE1AXoVQ6JSMqe8G2g6w7bI_H85swsSzu2bvC9ffe3rKQ8Dp7ej76qoPVDaqYmZPbVBAgi6a0yzgLEfYlvKVZfLxslGfk58UfECt9M_dRA8oVttM1w6GzoGcgtoJGUNts1PL5ujPMRq7A5AiISAmBislO0CVbIFw7pXIQccNvMQIa8yCPKY2mrE6z9EF5j2bL1I85QkcNKFa9Ib2a9IdMrO9wsVnVXE1H0svEqLlhvmt7jxcxYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚽️
برادر گارناچو که فوتبال‌بازی‌کردن یادش رفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102791" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102790">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZz-Fd9n1SP8X9Yx6e87-jPMCsR-G6LNETV_3NepwPxrWTGCC8nHe9qy1LMCTtuBJKZlnsl_f-3FTYcFm169c2--ND5xERRuahR-eBSb8yOLcFZjE1WjYKnuajmbs8nJs5ywBrHHJtrKLT6DkAw_J3MUVWK8a-CO4xo75I7MKYVAcONBZg2qc8MTMK1LyaIEglZ1OPgGFsdPmGmZc8-cjhLmBRpjDPmBkXlxPErHX-FMkCfdh6C9bMlZBREBOI_7KhRcyQkklJ2y67xgwEbThgsjkMCFyfn1F6Qht8r8u0duQF1ROJThCnKsVeabgSXWMsqlVioKz3maCdifcZLExE-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZz-Fd9n1SP8X9Yx6e87-jPMCsR-G6LNETV_3NepwPxrWTGCC8nHe9qy1LMCTtuBJKZlnsl_f-3FTYcFm169c2--ND5xERRuahR-eBSb8yOLcFZjE1WjYKnuajmbs8nJs5ywBrHHJtrKLT6DkAw_J3MUVWK8a-CO4xo75I7MKYVAcONBZg2qc8MTMK1LyaIEglZ1OPgGFsdPmGmZc8-cjhLmBRpjDPmBkXlxPErHX-FMkCfdh6C9bMlZBREBOI_7KhRcyQkklJ2y67xgwEbThgsjkMCFyfn1F6Qht8r8u0duQF1ROJThCnKsVeabgSXWMsqlVioKz3maCdifcZLExE-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایتی شنیدنی و جذاب از لوکا مودریچ افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102790" target="_blank">📅 18:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102789">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102789" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102788">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6Du85w4_MVtjHfzVRHs_Gt9OkhtEsBDEPUlKOWiDfwMGqrp8rh2CpqfDzsgyyfT0PLNQ2-M9rqmy5QnYhQdIHPeFLkhwTVWjB5zM_VoycGuAOFJzYTMQiRLfuAd4VUfQfiX03f8HfOURWBbsZP5EJhR7Yrg7itFAkCZwnmjxHWkzXPISqIdY4iR9FCW6UxfrjEfSE_gfk0EKMAhmaaaf74rKP9Z8rq_pVdrWlBFyRe5mHjhIxYAARyrjAQkVwJSdbEiqRbjUzcP9GAkB7eUt_bkcbWl7ObhG-Z7Tjm9QVY8VLGjpKjFyldbZU5QAki-dj8-BNvOYNhIEMG5WHw0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102788" target="_blank">📅 18:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102787">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5sRjgoYU1Mp_ELUeEDGApQZMG7UP8NotXJW7oAtvwNibbm7MPVNAY7VjRaf-fr3GZBmqxCzEtU_s-9aqi9PxREpn2Xm4ZJM_vC0v2S1oqjnQ2edabdvUuThBv_Sr0bY-2dCPgRjHVg0RUaeI-T-_Sbi5eWEGFzZ0Nx-KBPeDxSg-WhTKIW90RaKtmLHGmCe4_TwG7g_kJpwKY3lkeQHsJiJusjxX28azjhv2rwdpJLJDCjXyYB8kuD-R3wG7dfY3GplJWFSEK-b_-mCS20y1WcK8g_OkNjKaMtL-xeGUrE3rCpWkM54zUifFwu7fHOyOoh6oURLHEeC4tzU79pkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیس فیگو:
اینفانتینو همین الان باید کنار بره! رفتار او پست‌ترین، فریبکارانه‌ترین و خودخواهانه‌ترین رفتاریه که تا بحال دیدم، او برای خوشحال کردن رفقاش از هیچ کاری دریغ نمیکنه. ما باید شرافتمندانه زندگی کنیم و به یک قانون متعهد باشیم، فیفا هزاران مشکل داره، اما فقط یه راه‌ برای حلش وجود داره اونم رفتن اینفانتینوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102787" target="_blank">📅 18:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102786">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d841566422.mp4?token=mOZLnUzy_DnZQSuHp4Pg9xxorKliDQsjgs80v62AKYYJd_M7jjuG5D2xcRNzkjXS1hab6Os-a9VobcQC3Ecws-JdgGLPqBBws54g2E6ayYgK66gmtHve5Qi9FmIeXqVryJ5Nfl2joIVU3qx0UTgq0Dv2a6GARDd7Oeqq488m6JNTJE9H4Tg9GpSdBbyHQwYbSW_pF6RePxejEZu8YKBi6qnQO8acplg4bXFbtI0MLAG0OobvIKDhZWpyguwuEbaVTJPhxfLyiYvGP73Ne-M4gnO6N7z2PRDunbtBVvHn7RBTIkIMo9MkhDiCGlpDzizQHdwuh2boF867FfNs7CH2Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d841566422.mp4?token=mOZLnUzy_DnZQSuHp4Pg9xxorKliDQsjgs80v62AKYYJd_M7jjuG5D2xcRNzkjXS1hab6Os-a9VobcQC3Ecws-JdgGLPqBBws54g2E6ayYgK66gmtHve5Qi9FmIeXqVryJ5Nfl2joIVU3qx0UTgq0Dv2a6GARDd7Oeqq488m6JNTJE9H4Tg9GpSdBbyHQwYbSW_pF6RePxejEZu8YKBi6qnQO8acplg4bXFbtI0MLAG0OobvIKDhZWpyguwuEbaVTJPhxfLyiYvGP73Ne-M4gnO6N7z2PRDunbtBVvHn7RBTIkIMo9MkhDiCGlpDzizQHdwuh2boF867FfNs7CH2Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سکانس‌های تاریخی ورزش ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102786" target="_blank">📅 18:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102785">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtHRyrZ43xcghqki2k9NdUcXx4BWIHJzAIcX8yJOp06f4sQPaJFC_Gjgt91yHg6kNYrU2A2CHO-7736n02oYKV9M4OiTlW17OTYnrvH2uADKMlqUCQwwpopqPnNtaSy6Vdz-TOTyuSBMdYlGz0kE3m46YYmZCg2jiiMXBjpcGkbkUwGp5tq1k5hGMc_RqRZU23X4ycFaOwohJGkSN2FyTTSdfUOJkTRLNn0byRA1lJFcDNxZqIkjt_q_ikL0G-TINVP-51zguu6rSf0Gyb6LEGy6I--TZk0X9rCJ7J-JXHQvCPV-DtZVPrG99uSs8VJK-hDk3nH5yCks3CFBpldoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنالی اینو داشته باش فعلا تا ببینیم چی پیش میاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102785" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102784">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
وزارت خزانه‌داری آمریکا: تحریم‌های ۳ نهاد مرتبط با ایران لغو شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102784" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102783">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=p78lkj5fbnErfGDcnDncqWS_kJg7995aC9uhJ4UFPsmSAeMihQf9vo9llRf8coGbKtulOqRKIrZ5vjxDApm096D7U-QRDJVnM6pKyGt5D5i88rEWflLVX-ahCKenL3mLaiT89uJHfoSBc0MueiMCbYgnqZ7ofv0R4mqDUVrRMlKRlzt94TODZCWhfihN5XIb-LP8dKvX5MbLZTgJdAY5_-62YzfiTx2Irfw9EUkZ8maTppzMhuSL7_6arlpQBdYqemVmqpnBPC9Sb2L7pyR3DQb2j9DLxhaMHetGuggqRgsBQZilpgf9R_R1CYqQQ4s7xzDNrK6qOSCKcotYVISO75529XSkL0RyOFFTQBgPI3RKYSEdmF6CnIqkvnSKnBqvXkhKpKkJ1ZbWuD5ikUBA0HkyShNaQEBCCrbxK5VQSL39eOs7ZUTRzGF60EoL6BfRbiYm5057qkC3hAtbWwTeel18KHt0-S5azIi8hHxtlbONI30NVx7e4AWCph-EaiHOa8RPouARJ5aUNcQ0kNd_D6TIoyMG5f9d6ie-EZZl12RA889KWoGym_gPVJ074OCwegAsvhui4lMSkzJtUGWu6w3i11j-HSuhXYN9-5AJbaPvK6_b18hp1ssxkfIn9znh4OUtP-go_udUUCp1kztVh0AbWTv4u_oxt76gDLp3qK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=p78lkj5fbnErfGDcnDncqWS_kJg7995aC9uhJ4UFPsmSAeMihQf9vo9llRf8coGbKtulOqRKIrZ5vjxDApm096D7U-QRDJVnM6pKyGt5D5i88rEWflLVX-ahCKenL3mLaiT89uJHfoSBc0MueiMCbYgnqZ7ofv0R4mqDUVrRMlKRlzt94TODZCWhfihN5XIb-LP8dKvX5MbLZTgJdAY5_-62YzfiTx2Irfw9EUkZ8maTppzMhuSL7_6arlpQBdYqemVmqpnBPC9Sb2L7pyR3DQb2j9DLxhaMHetGuggqRgsBQZilpgf9R_R1CYqQQ4s7xzDNrK6qOSCKcotYVISO75529XSkL0RyOFFTQBgPI3RKYSEdmF6CnIqkvnSKnBqvXkhKpKkJ1ZbWuD5ikUBA0HkyShNaQEBCCrbxK5VQSL39eOs7ZUTRzGF60EoL6BfRbiYm5057qkC3hAtbWwTeel18KHt0-S5azIi8hHxtlbONI30NVx7e4AWCph-EaiHOa8RPouARJ5aUNcQ0kNd_D6TIoyMG5f9d6ie-EZZl12RA889KWoGym_gPVJ074OCwegAsvhui4lMSkzJtUGWu6w3i11j-HSuhXYN9-5AJbaPvK6_b18hp1ssxkfIn9znh4OUtP-go_udUUCp1kztVh0AbWTv4u_oxt76gDLp3qK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات فری استایل یه دختر خانوم با توپ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102783" target="_blank">📅 17:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102782">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXbGsVKU29on1DI3aigzSF2YAlPaMu9iTKOwM8n1Wfs7nI2LjMQ5pngSub0ka_7sT2qkw5qllw-_-UUJX8hMJDKQwyj2OJyVuFWYRvuGnfyST1tD1U4znpArTTMKcJqwGc4D8zRTlci5iOGHL7ChMnHzkp0tItCAE9OagVrVhomiMR7XxR_QNKSluwQYRExQNbGzXVYNlsdCStcPXmjFHq_BMKBNs3YxtlRav4YjbHQrr61ueyLSjLN3huRHtcjBZCWTw_Rr_6P92q-Rw3pKEF5wscWFaxDpvgLylp6z4CojthkbKn9EHEqkt5Ia5v-XGVmeyBuuxB8w92vR_efgJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وندا جان دیگه کار از کار گذشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102782" target="_blank">📅 17:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102781">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvno4vQR2fyRdGvrxzTYQENX_Ho86a8gjEsMjlRBC2T-gsNQspwdoL751vCHOu6H6Mdp8uPOzrZnjXvDjv2yFuepblE5j1pFaD1u4eW00JlhFAUHiJpy92d3OjaS3zVHhiUKzPJW7Diq2x6DJgt8NAJ_vNye8wNunTVqbMwYnal8uHSn-ybb3gkFc2pCStvtge1tP97xCHHZhJRyKMb_KiViNF77VHoSDs0iAx0UB2GuxJPM_4p3AQgcFfN2kbOdRsbp3I2-WQ85GMITzwPxs0TJfglFkv_FJ9dYboQuMpPHcUAdhb9xs2o7iozNXncBNTpJDl7YPT1I7D2q0JN_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار در بارسا
🆚
پاری‌سن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102781" target="_blank">📅 17:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102780">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLTdaAJ6MEeVZXWijkawmol1CT-wsMnFmihVpZdVfl1qTv8CenYhNe1BZ0uCTRIItb1MAIK0VUzfNK_vKwzJsVbHWihjW4J4cwUuGHYf6JuBfRwz8kkTVLwhj5IhZunEIRklkO2gGpxqF1R4mMAem_9jmOs34l1dv9g1VqKsoLVbdtnn6Tq6uAyBHB7_21uR6xD3QNq3KZeZQP8TWp9phLOZMWWN1Ytpg21uw8veOwPJWkadr2_PZx95nhrCO1IZY97oBVqGlgPaWFnfhmv4lfS9zasONJmJYFWo2Kp-60GWNWOOEIMDrE84SQMI3kIU8sq--KEzQqV5aOWsDCOZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
بازیکنای مطرح حاضر در این فصل سوپرلیگ ترکیه:
🇹🇷
ترابزون اسپور: صلاح و اونانا
🇹🇷
بشیکتاش: تروسارد و نوبل
🇹🇷
گالاتاسرای: اوسیمن، گوندوغان و سانه
🇹🇷
فنرباغچه: گرینوود، کانته، آسنسیو، تالیسکا، آکه، اشکرینیار، سمدو، ادرسون و لیواکوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102780" target="_blank">📅 17:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102779">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReuffxOcE2g7TXv24VWJvjBY0ZT37OpITRSr5P7cJtPRhhsFbi8IvG4bP6H0sqltJsotLWm8onlmuQOMiJ1cOeiYSMifAv09oPrdqrp5WPfOcUoBbKdp1ubGMOZ79wSsbxlqIcXO7T46onU5ScO6wgrH-kifY8_3DmJi5brcIXdxz07_C0X-_2FbpykYiFCPf84LUuoBOnuDZkHwhNd-LgNFxmK-wlfhIsZr66NySBeEDTtp_SHBYijx1jqonG2qUgg1xBcPBDEEvU86dgo1zpdBopgRrXtJKlIL7rnEFjoMojwsidq2UcHhxGLAiwapOPmti-o_n7WHum8stbO7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
چلسی بازم تو بازی دوستانه باخت؛ این بار مقابل یوونتوس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102779" target="_blank">📅 17:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102778">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4B6g6sfPTVulhlcf3jcab0l8IFd8wsGwJG9FT88NK3yNNwCqzItda0eblq0NhelOVg4HkvArfDR0acnd3ctjGcIFKqtULE82M4BOcJYGRqBPPk77tWRkWzUWoI9dlQ0MDBUdLwMYWgSfpDwmsIJNzk5OI7RFfS1cAs1WTgUJrexL0uiLjA5KsFXe2YeLlaECEzLn42Vyrohjj9aPS-MhK8Da-zYd7MeFQ2XFr6yrJGQn3azqW2jRM5fMg48OjKWjPgqfh9yMO4cQhGp-A6LsN8Umxlg26l-HetmakXRYrrTVX8awBV9VST_0QRqkNAtFsCef2N9_OYNeszSj6aARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
چهار خرید رویایی رئال مادرید در سال 2009
:
🇵🇹
کریستیانو رونالدو (94 میلیون یورو)
🇧🇷
ریکاردو کاکا (67 میلیون یورو)
🇪🇸
ژابی آلونسو (40 میلیون یورو)
🇫🇷
کریم بنزما (35 میلیون یورو)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102778" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYZmeW0GXOsxVVJGSNg9Q6puXaBM1EFtl8-71vGXwhsWoLIhH8IUGLedsfZlTausGYSW4d6NPvVaVqYB9Jxaj6v-Y_xakc-xAVHJVig2NHp8IDg4HgsdbDZ8XTuif_0DAglSapFq4Sv5AY9db3ByNCFKKWJ4OgoilbksACT36tJzn5clcGVbhchHzzJb6sKvrthengETXac8JFF7vxFRGr1__gxoGKZqj5XrOX6RoaR4ivK0eCmk14Zlu6lcphFvOTzVGmxqVDBdI3UVyu2xIcnBFrcH_yT65GAudzzcuOccxzS3Hsj20-lqhdV4w2EQCjOLKXdBhdoejeTfms10LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
بارسلونا قرار است بزودی رقم ۱۳۰ میلیون یورو برای آلوارز به اتلتیکو پیشنهاد دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102777" target="_blank">📅 16:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=Ur2bk9PHGN36tfwK3iTxEmrRWE7gUJ3NxdD4fuswDn8bvl96KMJ0027it1tcFJNxEyOaSR4peeA3qT-ZWLeHd5kCvwz1xWBFoz6YBVflfbbYrd_PoqSVaMQakA7FF9PFV1dMmK6hlHdJwYI9ZGnjgeHK3acZwgkYwW8cAaWnhsUU4EcQZEDRPwDF20sIxgfR8ccdjvQambT2141A_7E4KpAy8-Pwi_07wTijfNyvWQZrU03dpU99Jk8zoj16lb0QUGsNycP3MOdPw6AllOE7AIDrZEZS9HNvwBp2CzyUsIMvnzoWFXnC6TOr9ie7PO45Gi2_81uMdAV2V-Y1SizWew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=Ur2bk9PHGN36tfwK3iTxEmrRWE7gUJ3NxdD4fuswDn8bvl96KMJ0027it1tcFJNxEyOaSR4peeA3qT-ZWLeHd5kCvwz1xWBFoz6YBVflfbbYrd_PoqSVaMQakA7FF9PFV1dMmK6hlHdJwYI9ZGnjgeHK3acZwgkYwW8cAaWnhsUU4EcQZEDRPwDF20sIxgfR8ccdjvQambT2141A_7E4KpAy8-Pwi_07wTijfNyvWQZrU03dpU99Jk8zoj16lb0QUGsNycP3MOdPw6AllOE7AIDrZEZS9HNvwBp2CzyUsIMvnzoWFXnC6TOr9ie7PO45Gi2_81uMdAV2V-Y1SizWew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🔥
🔥
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102776" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102773">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8ina4LZOxkQd5zJV63z3sWrTrhPCkcbstfolgq4JrOrBbW9TM5JsSL8niEHlFtFCf5IA_vWVQJrGMG0F_k4xkQcUl42xFXshDEocma8YFxGd5RE5Sh43wk8FoyBwuypeayCcAvTtnt-87F1jfbJI5FJe65vip8zNWdD2eJBXNaSSgkYtw6TMV67axv_mm6ckzImdPIhpQCR7wOznHJMyXFzv2bnfQZ8Z77GAfRSRekqdBq4vsTGVFERxpx35wEJNawRaqcONUk9CTJGuiEYbXrqRHUtUQr1Tt1WSf0RjTMYymCu0pTy2_V52tSDjW76kxnDQbNjanGuDx_BIcl_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bgfub9mYXwHSIiz8XcP8PNlX1Ls2Dwh_mSikS7H3ZV6ajRrTM4ULrnLOP2wTOKrMroEFKhXXI3DQ_QBw9GZ8fpt_89H6Hgxbic7SwK6xBrWtTIYHb_6-Wj8BomdBfgFsWrOVGPvOIPHA2zhmVUmgfPWT2axrL3Iwqwuw3PxFvhzY2dOlHsxO0DOwG8AbCHceW_RQX1GI7RoCJImnMLz1paLvwcmEuhhLiZ-vVi_Ulh80WUxoow7LJSL_GcKi-prfxzHQHvbCe1Mz2iNeSkN3ek4dWO1-3ZzjwGtUDh_-9IOGmLCXqolO4RtaRlT5M7oAfISNN10yEFwy0V2-0kwpsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLuIzRHYdxbcF5y4tn5tIFh4RFuU6vqBsfw1zwb1qDtEHJm957SK884uUz-fjY5j_SArQQxc9JPEqgiCgsaztvQ80CtF8k-BfW8_VvmXuvZ569IChBgNH7k4bfouJcyeIppe66hV9ONqwu9m5eIzqqvBMOh8V7foRNbCszOJBMgcHyXdxU0wLX-V7uBGELINBLnd_bt2ZHho8K9Tr9iY95M5pM6IBC7moQq-j470U08GbGnKTDoUBooQqDIYYVp-8tWd0nosD74lGLctV5zt1uFNDZ1L4NsfgQp5WdPJBAlrS93TBZ8oHn0EUl8YEL8gjuZU1DEmH_u5CYMdzFtR3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم «کومو» یکی از قشنگ‌ترین تیم‌های دنیاست.
لباسشون، شهرشون، استادیومشون و جوری که مرحله به مرحله و از سطح پایین‌تر ایتالیا رسیدن به سری آ و گرفتن سهمیه اروپا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102773" target="_blank">📅 16:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102772">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=sBJ_SA6jT73Vv03WFpBdUgQygzxNK4RdC-2E4fLoh8f-McgmBFWaUhSOBth9kEXOJ5BsQW04DOfOY8ywSE_5Fo_rJP0GqCNTT2zhdgIgVxsgauvjjQ5vRwoKvEcyQ0SiBhNOcEhOFO0Os-YCh3l0CLJwdeNo0YB9-IdyCuaNEKCvmj0VFG7J9ViruMlrx-He1Ptn1gfMTxn0SmRjLoEepCjNg7UgzMQ5l_pYDt-ves2qRUXDqyK_Diway_rY4ylal7ga6SmO8Mulsj6Q3WfZdO1JlHElxfKOfwUGckQwWXb2kZVBpW3pfkhcjhVbr0D9sP8EJaM3PuXGVtDyp5H-YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=sBJ_SA6jT73Vv03WFpBdUgQygzxNK4RdC-2E4fLoh8f-McgmBFWaUhSOBth9kEXOJ5BsQW04DOfOY8ywSE_5Fo_rJP0GqCNTT2zhdgIgVxsgauvjjQ5vRwoKvEcyQ0SiBhNOcEhOFO0Os-YCh3l0CLJwdeNo0YB9-IdyCuaNEKCvmj0VFG7J9ViruMlrx-He1Ptn1gfMTxn0SmRjLoEepCjNg7UgzMQ5l_pYDt-ves2qRUXDqyK_Diway_rY4ylal7ga6SmO8Mulsj6Q3WfZdO1JlHElxfKOfwUGckQwWXb2kZVBpW3pfkhcjhVbr0D9sP8EJaM3PuXGVtDyp5H-YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
روزی روزگاری رئال مادرید در بازیای پیش فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102772" target="_blank">📅 16:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102771">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OejijyKrrQ9QKKAkNGRdvmU899zUJpS7yKb7nNQ210G-8o1SvHiZuOufSN2eRbKaYcwWPyJLaFsdRMNCs7697tNHwB9m6vMkOhXbBYUxZ26bv_aYaT_uRnSUUY-37k1hDAvElWHUt7mfajz2fI8zBEYZ7GXDipZMwcARavhE6VteIM0nOCXXslNGHcP6-sFqQKIhKTzYyPASlxSU7l2qcw1zWD-wZe8wzlYUqaKXbuaj-kWzwt3vA0Dym6k1EDrNtO060jNUtxBG7QngH90IGAT3rdaul98tea_X3gftgbtAjSzl3hL1nKai2lPYQucZLzH_sor1ZuLwiJgCj32Z9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس در واکنش به هوادارای رئال که فریاد می‌زدن: "وینی، بمون"، با علامت
👍
بهشون پاسخ داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102771" target="_blank">📅 15:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102770">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=OJR0L7HTvbfeC-IKQBilIl4U9IKsI6-aQazQnz8s4ZB1eK_JP4npIX_xbfORAPAs6KLEPk-dh3SQfqJ2i7nWYCXbOq0FukuzXUhiEd3PvZb1IdKNcvGsN3lBAPQ7W7U63t7wSG_18Xx94MrOfa4Scuundq-TLfZ-tEotqXx8TxJFa_I3X7Vf8NNp0gasR2m8Jib8Eq-6-RFvozeKCqCieRJk4eafqFzXUs9e1sfXWiM9t6b6p0CeWa7O1hA-Bh44Ui5-DBnxyTFyCsZqZP8cIV8tBwH5lpv6_LXX-JwPn3crD0rPf__0acNoqB0l5XcU0GtYsLkDrcNoAQcY9V8kzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=OJR0L7HTvbfeC-IKQBilIl4U9IKsI6-aQazQnz8s4ZB1eK_JP4npIX_xbfORAPAs6KLEPk-dh3SQfqJ2i7nWYCXbOq0FukuzXUhiEd3PvZb1IdKNcvGsN3lBAPQ7W7U63t7wSG_18Xx94MrOfa4Scuundq-TLfZ-tEotqXx8TxJFa_I3X7Vf8NNp0gasR2m8Jib8Eq-6-RFvozeKCqCieRJk4eafqFzXUs9e1sfXWiM9t6b6p0CeWa7O1hA-Bh44Ui5-DBnxyTFyCsZqZP8cIV8tBwH5lpv6_LXX-JwPn3crD0rPf__0acNoqB0l5XcU0GtYsLkDrcNoAQcY9V8kzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی نیازی به تست دی‌ان‌ای نیست:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102770" target="_blank">📅 15:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102769">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=u1WZHIMhRm2VPipDwOJkdRbC14uStvXvf4cHtBPqlprQeuLzs7fODvqyyX7Wiqh9dTlh2nXD4M6TjeaesZyEUXwNs7RS9VtA0jja8T0Rz0HSBLNZXlnmGuGnO0mNwbsP9ac7WeS9cPr3gn_BBbmjY_Z5OOYl767Q7XuMufQlUAgJcvYQwju8cGR8RHL0Bs_zhxdolowaxsmSEPEgsfRnwHOL9j9P0jLhCBK53g92Wno8AJHdjuN7jllPQNgPxQPa1PJdn4Z7dxO5YgELygefTn-HI11Aa-x713nBXi5KulD4v2hkZ15BdGI3HRhu4H7e3ZNAv8MRiCqSgkKjzBy9ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=u1WZHIMhRm2VPipDwOJkdRbC14uStvXvf4cHtBPqlprQeuLzs7fODvqyyX7Wiqh9dTlh2nXD4M6TjeaesZyEUXwNs7RS9VtA0jja8T0Rz0HSBLNZXlnmGuGnO0mNwbsP9ac7WeS9cPr3gn_BBbmjY_Z5OOYl767Q7XuMufQlUAgJcvYQwju8cGR8RHL0Bs_zhxdolowaxsmSEPEgsfRnwHOL9j9P0jLhCBK53g92Wno8AJHdjuN7jllPQNgPxQPa1PJdn4Z7dxO5YgELygefTn-HI11Aa-x713nBXi5KulD4v2hkZ15BdGI3HRhu4H7e3ZNAv8MRiCqSgkKjzBy9ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ياسين‌چوکو بادیگارد لیونل‌مسی این‌روزها علاوه بر بدنسازی به تمرینات دروازه‌بانی مشغوله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102769" target="_blank">📅 15:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102768">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=VwLqcfil27oNG2cF2nXtSRFfplVx7vSVYFc4SzQpHFDPlebPcksjJAhizdKC-H5nA8gBloxXf8XL1VK0Nhp8lK124AgQO3W2aIWefhb8SeS7julGB_wMUTnPGiE9xT-f9v1h5_fF6i1nIU85Uboj3thHS8Ui9EB74YxTNErPnp7GJ7NwzjKK6x2-lPWZzIbX3kCHUC8IVHSosmeIFr8Fzk3P6HYrkbo5-WTNf4aPshQiGwagW17JPtdzSqKHJs4vipNfkIDxQqFZbkOZX23KWin_Vq7PRLYqMxE13EZXaTmXaZRb3GKJ3SgKq1NvFTCQN9jWyn1p5c2lVj8AYPF6Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=VwLqcfil27oNG2cF2nXtSRFfplVx7vSVYFc4SzQpHFDPlebPcksjJAhizdKC-H5nA8gBloxXf8XL1VK0Nhp8lK124AgQO3W2aIWefhb8SeS7julGB_wMUTnPGiE9xT-f9v1h5_fF6i1nIU85Uboj3thHS8Ui9EB74YxTNErPnp7GJ7NwzjKK6x2-lPWZzIbX3kCHUC8IVHSosmeIFr8Fzk3P6HYrkbo5-WTNf4aPshQiGwagW17JPtdzSqKHJs4vipNfkIDxQqFZbkOZX23KWin_Vq7PRLYqMxE13EZXaTmXaZRb3GKJ3SgKq1NvFTCQN9jWyn1p5c2lVj8AYPF6Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
▶️
#نوستالژی
؛ مروری بر آخرین تیم قهرمان پریمیرلیگ انگلیس لسترسیتی دوست‌داشتنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102768" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102767">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e70775585.mp4?token=l1e3F7ly_IoePeqfRTdYLbx4YuLkLmTx_ufUueNgrEKePKyLwtedrSrtrMM-Vg1jQRP7mZ2W-fAwidEfg0cOjwmyqxIZu6HZJOFqJ1hypXOQWhn0Rwwiv0VfvmuK5QXI0z6oImj3HZ-bSvJdPp4t0Q9IwZfIWhKGp3EtwlmsLeOia7LlFal8keTqDTHkljK8f8TRMEOljBeWzSX9CE10QZ6J20wFztxoRUvjxcZc543OtRYzm8wRu0rioVy3d-bhMrwb90CwCopPwTbl8HO_DRv1Nr_90xJurpuCpcZugxOBMHptqi4agpMtMj20zENC_ioIQisAfkloNFey8mXDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e70775585.mp4?token=l1e3F7ly_IoePeqfRTdYLbx4YuLkLmTx_ufUueNgrEKePKyLwtedrSrtrMM-Vg1jQRP7mZ2W-fAwidEfg0cOjwmyqxIZu6HZJOFqJ1hypXOQWhn0Rwwiv0VfvmuK5QXI0z6oImj3HZ-bSvJdPp4t0Q9IwZfIWhKGp3EtwlmsLeOia7LlFal8keTqDTHkljK8f8TRMEOljBeWzSX9CE10QZ6J20wFztxoRUvjxcZc543OtRYzm8wRu0rioVy3d-bhMrwb90CwCopPwTbl8HO_DRv1Nr_90xJurpuCpcZugxOBMHptqi4agpMtMj20zENC_ioIQisAfkloNFey8mXDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
خیلی از بازیکنای جوون دنبال اینن که سریع‌تر بدَوَن یا تکنیک بیشتری داشته باشن، ولی فوتبال سطح بالا بیشتر از هر چیزی به فکر کردن و تصمیم درست گرفتن توی زمان درست وابسته‌ست.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102767" target="_blank">📅 14:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102766">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=t2gFLgPJ8sBYX7k5G84rbGiiMUVZX7_Uu_lgf31srX-dS_NyiU-HR7V3TEVEfWXkHterurgmCEGut-gdvcV-ysnDO0WNN1kVjaE6c6URldflz8AkZaBhdhcPDnOVscJGakXXV6xdPx_7cZkMIYh1TTr2mxkRXkPSXsjMbwa6KXtwdWNe99j0jGu0PTIoWrjFOSo64NPbFQ9Wd_p4BK8_qqIfX2kwmyIBD3np6-dKoAofVVSH2Z2CXTLOdPNDmimbrolyycH2ulTVsafPu_AVvjSIc9n_XZP44BdfXsy3Or74JKDkLl0G_e4HPug9mbRURdxD_X2NLQ1oxVc8ywN98g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=t2gFLgPJ8sBYX7k5G84rbGiiMUVZX7_Uu_lgf31srX-dS_NyiU-HR7V3TEVEfWXkHterurgmCEGut-gdvcV-ysnDO0WNN1kVjaE6c6URldflz8AkZaBhdhcPDnOVscJGakXXV6xdPx_7cZkMIYh1TTr2mxkRXkPSXsjMbwa6KXtwdWNe99j0jGu0PTIoWrjFOSo64NPbFQ9Wd_p4BK8_qqIfX2kwmyIBD3np6-dKoAofVVSH2Z2CXTLOdPNDmimbrolyycH2ulTVsafPu_AVvjSIc9n_XZP44BdfXsy3Or74JKDkLl0G_e4HPug9mbRURdxD_X2NLQ1oxVc8ywN98g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وقتی میراث فرگوسن نابود می‌شود :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102766" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102765">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCSZ3vWOmmWXPP1FLnialrARKevMppWGKbwHFY9V2dKeowAHldUcq86a3yV4no_Z9jFujM3cT2MBMIBhs24SSfd3RHxYgQNEDX3eD47m2XAJUPbvDiRJoBTh9_32vuqTKDMDjH7NexXHwKFE5KNlZ9hV5Qpe9J1V4U9HypuL36pjB7P5GLY6GVR-YUuiNrAcZKxR3zTJQwCuf74CE_aG8TmBJdGJ08rgZYnbxHq1w8tfX9fmbr8uy7ziIaG_Qq_CQPk9uVd_js4JscYhjsRR__hprLmKsJaAiUeWE-m_As_ElSi1fm9ebuoHDdBs2mt4qOx_VKFHfYHrT3LHcTxk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔴
7 سال پیش تو چنین روزی کینگ هری مگوایر اسطوره فوتبال انگلیس با 80 میلیون پوند به منچستریونایتد پیوست و تبدیل به گرون قیمت ترین مدافع تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102765" target="_blank">📅 13:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102764">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKc51iBboEx1h-OUg7bm82yi0ne9k-UJPHh2hKQ8h1sDiOGlTalG4O1K7yCsRb0C4z5TT3Q-QSCtRZiZk_7DLLGzwSecqsPqg9A2elZ4sZy3dH6JCTeiFh9fecGY83mU0yT25GaYRkWe9JbPLY_CDFSw1pRxY24F1W5Cp1NdD5omPXH_1NKARQPRx58PCheTkIGzcLKD8tmtTAjWxvg9PjEg8jPikqK4QnazjheVEUgjrjHI6Oeh943YoLSCHeEMMTqThJNOxyLNwJbxp9W6B0VHJvGVQLuLui_b7j_loCT57N7qSU6fujJt6q4GtIhPCb-8Gisi1mStx7hpr_Zn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102764" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wncz41qyXg6B5mSx7H35yo5ueZMSYpOyCX88iwMuS7R4cATu3WOeZqfpwRkOTxipNtzd2wXJKfAPh1DOXibcKBmi-cYe7vZ8bpin5gT12UW4wbUwSO6Eq5bdQTepycQ3sm-HXmk56UKLb0BODt71Uhn5aRxGhnuYShK43gdBOwl57lIb5EeRSOJdGDpU1TxBxpp9b1cIVW_kw8T98LjinACP30fdhb_TQigf5RoJPi1GBhOjtLE9OEKHJ1SAL2Ap7WmUJrsNt9vW3_iByFJdyM2XbEmRpK12K7W9zhc2qgcHnWLk2bz6Uj39_DZN3TYQpLJQLJw6iJauHYcTdIOS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه که بدونید فصل گذشته
فران تورس لورد بزرگ ۱۵ بازی پیاپی رو بدون گلزنی پشت سر گذاشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102762" target="_blank">📅 13:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=IegSF-OwhpNsnS0kyMIEidw0hdD6u5hyZfykpLOuNjQ5WDsbvCN2uqfU6zPYxjrznvoqJsdLIPP_jCtyeAkiTrXfG5YgbqGKUrBKNP9N4RapBHGBb9VfEUGKzPYGEah3_euPilzvs9mVNUTANt2HqVcZpB8C3Xpvv5GZqqE6ms_tNxKmUQ7QcadIP481zUdTa9DPennGfjx9NtEP5av5TpMTblNJv5ianQvsbsTBcO4R2vmEAjeA5buwV9AuOgqd3WdF02OJBZjXnpyuUJ76kCXxo2Ili00V6lgNiTHcmJHo7-Gf2PEHT20JjabV4AHF4h6iNdfOPM4GXPf1PBqQog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=IegSF-OwhpNsnS0kyMIEidw0hdD6u5hyZfykpLOuNjQ5WDsbvCN2uqfU6zPYxjrznvoqJsdLIPP_jCtyeAkiTrXfG5YgbqGKUrBKNP9N4RapBHGBb9VfEUGKzPYGEah3_euPilzvs9mVNUTANt2HqVcZpB8C3Xpvv5GZqqE6ms_tNxKmUQ7QcadIP481zUdTa9DPennGfjx9NtEP5av5TpMTblNJv5ianQvsbsTBcO4R2vmEAjeA5buwV9AuOgqd3WdF02OJBZjXnpyuUJ76kCXxo2Ili00V6lgNiTHcmJHo7-Gf2PEHT20JjabV4AHF4h6iNdfOPM4GXPf1PBqQog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
😐
⚠️
ارتش‌روسیه دیروز با پهپاد یه سبزی‌فروش اوکراینی‌رو تار و مار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102761" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oaov65ySugupcjd-_7QoaaTCzy-uIPxE7lLjvHVQqGEEMb-vFHJtq_tCxtSiLgoS_Z3_pSQugZGapdWiW9--MmUukGuJL4cME8DW0Ht9l3dwWw9MNxg2DUlVt15pby6Hhxb8vuEQngfXN-gFxFhmF2VoXVGEdJF8-yOkApCd01wy5UQWqhxIhEcMsfoZtplaZw9zrTS-GWz4b1LhktAwBKrgJiNbpywBudpOlH5pfDiRc_uJk_Itpjkkjlv4dEtZ0x3m1BYAplmMBJW2e90SkPVv1r65G8ondkNYa-YlivGm80AZkHEGAgmZ4D8Tadzbk46ZF7k1y9rWEVe9mRivOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102760" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edu1bXwF9VChfplgODRA3K_EJmkmIMRfvCVoDii_APr552c4NktBpuduLK7LzT0XE0P_ChWZpMG6TNB8BdX0mUyg2ckryUZo9sRKZ9aDPtbh8jij7Pn89m4V0Rvd2S4N9enO2rYWMHrxWZLUf7KW-8Xs4w8cNgBzQvjrbM6QqdyiSQxN948TpEG4tF83zpHOJhE42IC29ROP6jVZkv4xA3S-8-qwVnQgzeaC7hF3IKxqYP9aCYOjV_wakg1yS8UOqtDz4x4lwAUBJ8C8Bp74BXLEATIQrmZuSPmP4pWx8EkLUk324xl97LqtDfpQRezwuvY_S2o-7HMooDWLsSyQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بازی‌دوستانه؛ ترکیب منچسترسیتی مقابل منتخب ستارگان لیگ‌کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102759" target="_blank">📅 13:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aovIjwTQr2HA4Y2qu4kjH-9Fp1mBA14LKMMcAOy1NX9juAsFBNO4vKNZuu0Vy0_GWdt4wgZe4rzNvGmBfzocQ81cSSTR_-piV2H7rcLUguWja3mtWEkVhH5aNRe5Jh-KGl8zdm-zZhOF-eRwpHhfQM04T0G1LXddFRorqJ4LYY7vBsAiBWG6F2st4KmEZuEEMOXmp03WuBQOtdMvBl4RtBMwsrQNqElcglrGJ86fcIo_swXzHDbu4BpNLooxvj57wnz-QjIKdgq6W7EkIIEn1XyQ1ZiSW9Y2g0vx1hiEVnIs6tM7fzOqzOXQv6rLqvdzOb7y-ya3M4rmisKTDgTHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
متئو مورتو: جاشوآ زیرکزی بازیکن شیاطین‌سرخ در آستانه انتقال به یوونتوس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102758" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=iIyJ9tLXlELCbkiLZTSydeb-lSwkJn12cliLHG3EXKUBHxLPXyDrhH3Y_RFb_9Rmth8dLkgVb5bElfaJgZRj_FO5HOe_zBqeHrJjiX7RoMleRSH6ephNOW8GUSgvRS8iCwVNoedaheX9wbf4Hxwt4DTqj26B9YDrL1jTpP29t4XAl1m1_5-FoongorP4ZbELEeVldQSglnwwcW17_ZBOGoLLw8tDbxGgode3sPA4So9ODmPCIYYi3DpfO88uRzyjl4q4kqZ607CIa5DuCFnxij6c2KIRcKqdC6_3r5bGoOsjmwcIR5xf7TfpIpq2R5ytlBgHe3_159g6C-_9U36foLGGMYJl1AnroIuruBT2PHVZ4xDFUrEUhsLGjJCwLtT-9MlLDjbSLL9Twg2WyHYhUwQGu0CDpgcR1drg_Ue5CDJBy6MmVRf5rqbkVHdLe4xM309a1o2lQNEbUr-7naUxOA0SIFH0GNgopkVpuJVP_B12l6tm98DDaYwJeHygcWjXCUwgkBTbmkFiyuQuWRNZpVNCLoFMvWk8SD9SBQDwJR-pilPKo4qGSekTTEXnuiDtqDZwbtiIGQ83TApX3dFBkrD7utfMKYLnPm_7JQnUxC1Ot_z56Rw1i5NddjoRU4hFZ_0dVnCZ_lDpGrKSuf1cKfVhcemsaVfEIN-lfztDthU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=iIyJ9tLXlELCbkiLZTSydeb-lSwkJn12cliLHG3EXKUBHxLPXyDrhH3Y_RFb_9Rmth8dLkgVb5bElfaJgZRj_FO5HOe_zBqeHrJjiX7RoMleRSH6ephNOW8GUSgvRS8iCwVNoedaheX9wbf4Hxwt4DTqj26B9YDrL1jTpP29t4XAl1m1_5-FoongorP4ZbELEeVldQSglnwwcW17_ZBOGoLLw8tDbxGgode3sPA4So9ODmPCIYYi3DpfO88uRzyjl4q4kqZ607CIa5DuCFnxij6c2KIRcKqdC6_3r5bGoOsjmwcIR5xf7TfpIpq2R5ytlBgHe3_159g6C-_9U36foLGGMYJl1AnroIuruBT2PHVZ4xDFUrEUhsLGjJCwLtT-9MlLDjbSLL9Twg2WyHYhUwQGu0CDpgcR1drg_Ue5CDJBy6MmVRf5rqbkVHdLe4xM309a1o2lQNEbUr-7naUxOA0SIFH0GNgopkVpuJVP_B12l6tm98DDaYwJeHygcWjXCUwgkBTbmkFiyuQuWRNZpVNCLoFMvWk8SD9SBQDwJR-pilPKo4qGSekTTEXnuiDtqDZwbtiIGQ83TApX3dFBkrD7utfMKYLnPm_7JQnUxC1Ot_z56Rw1i5NddjoRU4hFZ_0dVnCZ_lDpGrKSuf1cKfVhcemsaVfEIN-lfztDthU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚽️
روایتی از تحقیرآمیز‌ترین گل‌تاریخ‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102757" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=NGKolOmFdiljJ67EhMBqqcBhZhO5cTFjO1ReY4riyyxzXrne7H3dwalQr7nOPcpFTg4NQetEIbCYbtPlZdSB3Lqzc0YyttLEpQP00XT7WIjWxEGf8J5uh938x-YUMYY0rdwZ7UZ5mZ7cOqNYhhspgD1eTKCybFxPw3xx6mi_kJG1laX3SZM35M-fpLdMPoEMEBH4CAjCtD_mO86Sidt9sSaDyBSiiQ6V9Ki1Xphuby9BNYKKa3jIj-0RDUjh-IsXvW2imBFLEB0GEtJhb0zrvXWTVFP2oIg84SXIc_OSQ5N0uUhBqysmaCBBWrz1U0A0ylmY_Ymg2Xo-FL7BELeKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=NGKolOmFdiljJ67EhMBqqcBhZhO5cTFjO1ReY4riyyxzXrne7H3dwalQr7nOPcpFTg4NQetEIbCYbtPlZdSB3Lqzc0YyttLEpQP00XT7WIjWxEGf8J5uh938x-YUMYY0rdwZ7UZ5mZ7cOqNYhhspgD1eTKCybFxPw3xx6mi_kJG1laX3SZM35M-fpLdMPoEMEBH4CAjCtD_mO86Sidt9sSaDyBSiiQ6V9Ki1Xphuby9BNYKKa3jIj-0RDUjh-IsXvW2imBFLEB0GEtJhb0zrvXWTVFP2oIg84SXIc_OSQ5N0uUhBqysmaCBBWrz1U0A0ylmY_Ymg2Xo-FL7BELeKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
تحول تاکتیکی تماشایی انریکه در پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102756" target="_blank">📅 12:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=dN-Jb6uba5LSkZA9fCxVDNqf0rB_j0IqdLMYEKtBNEHQrdhvkwxMK5-m3N0U13Tydf_4sMrojRWSmlsE10JNtE5TJeEw9LuUlckDYZ33gUISuVmSPj7XAipt1nmQUWqtbIKobvHAQ5TtVzve1LKN7ReEyYPw_nYE2S4UEy8F4uBdZAmlZMYa6ng7kvLr0uFYlBgO1SwfrD_DMWYfr3s2JymW66tcBYr1HD8tJaCZBstCjc0353YpnV17xrgKz7jPzAjHYnLaC9d9WJcYdrzX837TvQvAo26zBCjf7S6s4jrdZHRzhb5uNVTJ8ByWRGTVFxMoi-gw1OGBlwPT_TJpiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=dN-Jb6uba5LSkZA9fCxVDNqf0rB_j0IqdLMYEKtBNEHQrdhvkwxMK5-m3N0U13Tydf_4sMrojRWSmlsE10JNtE5TJeEw9LuUlckDYZ33gUISuVmSPj7XAipt1nmQUWqtbIKobvHAQ5TtVzve1LKN7ReEyYPw_nYE2S4UEy8F4uBdZAmlZMYa6ng7kvLr0uFYlBgO1SwfrD_DMWYfr3s2JymW66tcBYr1HD8tJaCZBstCjc0353YpnV17xrgKz7jPzAjHYnLaC9d9WJcYdrzX837TvQvAo26zBCjf7S6s4jrdZHRzhb5uNVTJ8ByWRGTVFxMoi-gw1OGBlwPT_TJpiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇺🇦
آردا توران در تمرینات شاختار اوکراین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102755" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
