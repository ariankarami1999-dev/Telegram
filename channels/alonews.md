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
<img src="https://cdn4.telesco.pe/file/cWt925GrnxF4zF43HIMG6F-JqYuH6Z0sAzTmmTaqoXb4CrSNVDqz5amntQOmdLjz8xuCtyorfO32Zl5AeadZ-YmkYx1u3hvpTzKepk0xB33qSgIOc3irTnE9qRIkWZu-obe-qOG0HFTxtncJaoL7xbbg0UxPZg8GXqOYjmtGIVjLr-XUMi-Z5LKqhR319AyEnDJogkFJJfV-BEmEoaF7thlVpR2AYrmGaJVf8hU9MJ7SSBjXQlxEkNs_6Gm0FbiERGkdnQAyapB7PdtdH3kqfV773y9Hh2snooNJVSDAuJ1Atjjak2Rz61WYxxmz_diX-EKUNPCbd5cghMbUib9iLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 962K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 17:23:16</div>
<hr>

<div class="tg-post" id="msg-129153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7667710266.mp4?token=WSpaSUNXL3tvvzUYjnUC-mpegE0cKqXOdmTXfrdj_R7JdMQZIE_yYx2tArLZUr-pMu7EATW3mx9LpOPX9Q3IkwCYwQkp4EUVEGHWRcJee1pYSy22YykAPoqcU1-81kl1wtGwAm3HERDnM__HdE3fujhgvbcPuVGw7r2891Jnmw2OiT5eYW1vST6Hgyikj6lr8vwvgQ0KZPIwle-wZLC7V-T_TLI3Ib7kS_oExhj5xXtYz3jX-R77oCrnM1BCAFMkqJe3IUSKrBBQHiCSICBm1GLpCqQHi_F8p_gL4StHgWdUR0zfVVrmzjAZmH_TWR9o_7fvP6jSwM3zfa_o7UZV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7667710266.mp4?token=WSpaSUNXL3tvvzUYjnUC-mpegE0cKqXOdmTXfrdj_R7JdMQZIE_yYx2tArLZUr-pMu7EATW3mx9LpOPX9Q3IkwCYwQkp4EUVEGHWRcJee1pYSy22YykAPoqcU1-81kl1wtGwAm3HERDnM__HdE3fujhgvbcPuVGw7r2891Jnmw2OiT5eYW1vST6Hgyikj6lr8vwvgQ0KZPIwle-wZLC7V-T_TLI3Ib7kS_oExhj5xXtYz3jX-R77oCrnM1BCAFMkqJe3IUSKrBBQHiCSICBm1GLpCqQHi_F8p_gL4StHgWdUR0zfVVrmzjAZmH_TWR9o_7fvP6jSwM3zfa_o7UZV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با وجود اعلام اتش بس دوباره، اسرائیل همچنان درحال حملات سنگین به جنوب لبنانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/129153" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129152">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unSaUbGEOhdvG9GMzMH7gkVup5gUukwpsD1F_ULPVd4bSb8aNkkOaAYccCDFlcPqm7yKIWjtXaVM8-tfz9cl4nUMT1P-6V7JF4WS5tg52Ns0c_5_HLFBKa8o1pclg9_BklIkeG8C47PPCdXMDktPh223qaOtSEEJbUJmrweLHRXX2KiJUx_RAAL0QvxR2bevdQRrN_GwAanzsQx7zPtdSgXzIWrAajGux6dRHAFa2jpPUt2r9LNG-t-sqWpFZOrTSnGl6NQxG-A1gvRgeh1XGHy_Wgyvrdw3VLWb8WL_pxL0eHNGUTdbnuME7e89b85QXyug30EHtgW82HqmSVEWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس به نقل از مقام ارشد کاخ سفید : بی‌بی (نتانیاهو) صددرصد با آتش‌بس دوباره تو لُبنان اوکیه ولی خود نتانیاهو و تیمش فعلاً نه تأییدش کردن نه تکذیب؛ کلاً سکوت گرفتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/129152" target="_blank">📅 17:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129151">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7aa6588e.mp4?token=nMY0LhSef7t32UtdYcpxMWSRyjDXskbnNibb0IdbYC9xnOJk_InIhGk3O1QmmAlryKI-LXc0zIBRDXGO5990hPxgu9yaYzafoVbG_CUHoi3h9rBWUWkVZ7XbWQUQ8PXeuccD6IMvVl9_Qn_-0KSgtq8Ii3zlmg-0esjz_O-PNEsoF42HEG1DtjCUBvW0RcOdvb0aNrJdZREAKUOllOY8a9lQbJJGmkdshBEm1IoCsaSWTJq4gS1wIjr2KeeO25NlOBrWY1Yty_nXO9TB9fuefK6g-tEi36-6fx3mxc1zGLeVPRDi1nIwkyYE1L78AxcNMewFOmhRGqAZrxpaff9ltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7aa6588e.mp4?token=nMY0LhSef7t32UtdYcpxMWSRyjDXskbnNibb0IdbYC9xnOJk_InIhGk3O1QmmAlryKI-LXc0zIBRDXGO5990hPxgu9yaYzafoVbG_CUHoi3h9rBWUWkVZ7XbWQUQ8PXeuccD6IMvVl9_Qn_-0KSgtq8Ii3zlmg-0esjz_O-PNEsoF42HEG1DtjCUBvW0RcOdvb0aNrJdZREAKUOllOY8a9lQbJJGmkdshBEm1IoCsaSWTJq4gS1wIjr2KeeO25NlOBrWY1Yty_nXO9TB9fuefK6g-tEi36-6fx3mxc1zGLeVPRDi1nIwkyYE1L78AxcNMewFOmhRGqAZrxpaff9ltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: از نیمه‌شب گذشته بیش از ۱۵۰ حملهِ هوایی به لُبنان دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/129151" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129150">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f118f174c3.mp4?token=aFUGcyoT0nXRu0L8J5aTrTLqA3GRx4kOrNoh0p-37es8n366vgq2LlqCjgn1QrLDXuHaSTm5nCWdqQyiWzoYRNjxWC6aRFIbryxAaQLdS2CTkm3G1M8LFJtaaR_kXVLxvFHsHahz2YhjzN2sW5zxOLmRnZPgyyKFcBBZsYR2W1FBqrHisc1rmZyT9-gY7rfnPBipfPDi7hylq1cfg-8s0cf0q1HhN8qLwguZF04NGHSQu1nD_owQrPN-8N2J6osJq6wYT54dnnVkNfvh5cs9RFVJmqFLtETcm4x_J7ED8t8qIJcrzoZNYRvYX-Mvg1DfOmgolQLq1J5rExpbsb4qsFArOgJkM-lL6_Bv6Wf_lR1o4f0d2eaLVncvSSDQ9zAePTg3RgPqXctTpOIg9Gfzq0znkRiBJmunVzr7R4ieMPL3Vt3dxjbOVWfFs08znpd-3BJ6w0DrWeUdneIqJkP7CAdhQF2ypyAo4zJTgCNTEvof-UE8awW07uUHJAfUTGnLOZ-lTOmwum2O5SX5m0U8fJhwQBS_8zbrI0rbzZU9PVrDgWe13rzYodYmENOcKT_4oMH2c5pD4D0_aD5bHC1GYgRf5hGxKfdgq6ujVAloR-B2Kgg6MELVQLkTi6QaqjHKY8cy2N_i-gda6UI-gITsUBifs311glvZXGiwnGvVb0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f118f174c3.mp4?token=aFUGcyoT0nXRu0L8J5aTrTLqA3GRx4kOrNoh0p-37es8n366vgq2LlqCjgn1QrLDXuHaSTm5nCWdqQyiWzoYRNjxWC6aRFIbryxAaQLdS2CTkm3G1M8LFJtaaR_kXVLxvFHsHahz2YhjzN2sW5zxOLmRnZPgyyKFcBBZsYR2W1FBqrHisc1rmZyT9-gY7rfnPBipfPDi7hylq1cfg-8s0cf0q1HhN8qLwguZF04NGHSQu1nD_owQrPN-8N2J6osJq6wYT54dnnVkNfvh5cs9RFVJmqFLtETcm4x_J7ED8t8qIJcrzoZNYRvYX-Mvg1DfOmgolQLq1J5rExpbsb4qsFArOgJkM-lL6_Bv6Wf_lR1o4f0d2eaLVncvSSDQ9zAePTg3RgPqXctTpOIg9Gfzq0znkRiBJmunVzr7R4ieMPL3Vt3dxjbOVWfFs08znpd-3BJ6w0DrWeUdneIqJkP7CAdhQF2ypyAo4zJTgCNTEvof-UE8awW07uUHJAfUTGnLOZ-lTOmwum2O5SX5m0U8fJhwQBS_8zbrI0rbzZU9PVrDgWe13rzYodYmENOcKT_4oMH2c5pD4D0_aD5bHC1GYgRf5hGxKfdgq6ujVAloR-B2Kgg6MELVQLkTi6QaqjHKY8cy2N_i-gda6UI-gITsUBifs311glvZXGiwnGvVb0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ارتش اسرائیل آماده و مهیای بازگشت فوری به عملیات‌های شدید رزمی در هر میدان نبرد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/129150" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129149">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">محرم عجیبیه
حکومت هیئت‌ها رو کرده میتینگ سیاسی، خیابون‌ها رو کرده فستیوال
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/129149" target="_blank">📅 16:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129148">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213cbd739f.mp4?token=v5MRrTRD8H_R9UsqTrU5sLtZNikCGzN4j1zP-q7tKItXcMicLC_d_7QFIHjHl_-h7fwS028jROgTq0G2NZ-8Vfc-JQltl2xh-28q94ooCl9ZIsBF-2z7qv_Mfmi3gOb8SkjYeVTu5OeuEYvq_4dtWTWBaDsocY2ZmJa0Y0yU8lMntGe4qBdasS4xmbXSZk-TbP1OYSGxqxZHPWIqGprF_wV5gieip8yOmq8MSAlMAjwLbLZohnKR0nwwdXHGiBj3CK2f7lxc4FrzPe5jDIrS9ag-nK1kddqyd1Yo0mxFfhP5hX90uT7Fv2bRz2T1CEUQDY39inZeaAMNXXYjIn4QxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213cbd739f.mp4?token=v5MRrTRD8H_R9UsqTrU5sLtZNikCGzN4j1zP-q7tKItXcMicLC_d_7QFIHjHl_-h7fwS028jROgTq0G2NZ-8Vfc-JQltl2xh-28q94ooCl9ZIsBF-2z7qv_Mfmi3gOb8SkjYeVTu5OeuEYvq_4dtWTWBaDsocY2ZmJa0Y0yU8lMntGe4qBdasS4xmbXSZk-TbP1OYSGxqxZHPWIqGprF_wV5gieip8yOmq8MSAlMAjwLbLZohnKR0nwwdXHGiBj3CK2f7lxc4FrzPe5jDIrS9ag-nK1kddqyd1Yo0mxFfhP5hX90uT7Fv2bRz2T1CEUQDY39inZeaAMNXXYjIn4QxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به نبطیه، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/129148" target="_blank">📅 16:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129147">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی گزارش داد: اسرائیل و حزب‌الله پس از مذاکرات با اسرائیل و ایران، با میانجیگری آمریکا و قطر بر سر آتش‌بس به توافق رسیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/129147" target="_blank">📅 16:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129146">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
حزب‌الله: هنوز هیچ اطلاعیه‌ای درباره زمان آتش‌بس دریافت نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/129146" target="_blank">📅 16:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129145">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNiGPsqOI9HlSrbUSmrGlrPcRERq_tLkBs8FaHVJGmXCtGi7Af7tuEAKKPWbrHNXLDJLEIdXZjkaHbya1Xi0N13PhVZEWbC7wQ2T0mKDi_cdjy3xu5vsm3oFQrk1jDYe4w2u3zegXmbZSKTwiyflWTueA0zVoHNGSf95aim5QoJ5oeKJMpi5aQ7GbF4X3PLDrG-6obn6f_4IzXUhAy2qQmITg_sI_DQxgdCpqCp-NjmppFZSKIKmE4JSZnK3JTUnSvV5CcFZ4O1gIhlE1bp1l201C6iZ38q1E8TdJOenT5UyR28pMUwSW_yPHOA0mAtphEPri6K1CDPU-xs5Ql_lHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش تتر به اعلام آتش‌بس بین اسراییل و حزب الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/129145" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129144">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کانال ۱۳ به نقل از یک مقام اسرائیلی:
ما در حال حاضر در آتش‌بس هستیم و اگر حزب‌الله به ما حمله نکند، زمان جنگ از جانب ما نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/129144" target="_blank">📅 16:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129143">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: آتش‌بس شروع شده اما ما توی منطقه میمونیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/129143" target="_blank">📅 16:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129142">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / خبرنگار المیادین در جنوب لبنان: همزمان با اجرایی شدن آتش‌بس ، حملهٔ هوایی اسرائیل به النبطیه صورت گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/129142" target="_blank">📅 16:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129141">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری / رویترز به نقل از مقام آمریکایی :   اسرائیل و حزب‌الله توافق کردن که از ساعت ۴ عصر جمعه به وقت محلی، آتش‌بس برقرار بشه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/129141" target="_blank">📅 16:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129140">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / رویترز به نقل از مقام آمریکایی :
اسرائیل و حزب‌الله توافق کردن که از ساعت ۴ عصر جمعه به وقت محلی، آتش‌بس برقرار بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/129140" target="_blank">📅 16:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129139">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4030a7e818.mp4?token=ibQT4DVp9xHDlUMHciA0Ge6moc2_aSJT8jyPuSIThq8_mGXa8qHy3DOtzpaOqYyOMZVupvUJdQCRKW2xhFhKdilrccRIzPAbXZNEimq60gzkBPG7XE9m3X1bfDiyL4otQFrIN2Aoe9CHkttj4c2gJ4D01DvBL6aQDer0StHEZWpKmDFeSwHNBkkfbv6njNrn5wHHxz2dY1aM_Br4jxrsT8omYDGkXlMJOEWda7zv4OLj523EhtnBPlo5bS7-SEzKoV-a1O62sktqPK04Z_Ua_4_LL4DDXdFGGZIHodFpZMS30gZFHcrcr2yXn6df2_1dqt25F7JZWhNt7jthjvGRYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4030a7e818.mp4?token=ibQT4DVp9xHDlUMHciA0Ge6moc2_aSJT8jyPuSIThq8_mGXa8qHy3DOtzpaOqYyOMZVupvUJdQCRKW2xhFhKdilrccRIzPAbXZNEimq60gzkBPG7XE9m3X1bfDiyL4otQFrIN2Aoe9CHkttj4c2gJ4D01DvBL6aQDer0StHEZWpKmDFeSwHNBkkfbv6njNrn5wHHxz2dY1aM_Br4jxrsT8omYDGkXlMJOEWda7zv4OLj523EhtnBPlo5bS7-SEzKoV-a1O62sktqPK04Z_Ua_4_LL4DDXdFGGZIHodFpZMS30gZFHcrcr2yXn6df2_1dqt25F7JZWhNt7jthjvGRYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ در طریق Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/129139" target="_blank">📅 16:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129138">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6PYMwsL6kCM9n4acSr0IyEDAlm2Dlz2CsKovTrDpZqEk5br0eUvecLJpIg_Mcjkw4FZU5Wv-BgDqTVqLQ-XKm6CPmVWV55hsty526XjbtNuWe_LqY8XPggQv91FxF7ebmXFwP7nVR_1nNGSCcDcHVbqGDQVd5K7slUPFcEtWn_kyfx2ZNcl9vaGpKi_PrEkmz5JhIfY8GVYhUFqRIUEJD9p6_uFi2D6Ud94OZ_42KglyGTXmS0D95rz22_DSxIlt-sv8gSPO0zd22a_DqBfXtcU9FiIsw7OLOGY-mGk0OmSbcOg6eJjOQ6IKGhNK-dSybVzxPJt6CNiH9raZYjrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ما از روی استیصال نرفتیم سراغ مذاکره
🔴
این ایران بود که بهش نیاز داشت، کارشون تمومه!
🔴
همون ۶۰ روزی که گفته بودیم رو جلو می‌بریم، هیچ پولی هم گیرشون نمیاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/129138" target="_blank">📅 16:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129137">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgNEXk5tsZ2k2bn4qipDrVYNaXk1UgmFSmcPEOw30n3mAA5g1vWYlkR0PqC7JjfEaj1fGmyom_Qo8aYngi8OAsMTpWaAr1geIE0BCH60M7uKeN-15hgb5cTGAqcqhLtO4rYYpot-LUQNwMyEGTzueyODPisgM4G2qLPZNuwpzZzTu916nUxkg760PRO7aoij5cNduR-N95mqI1fAXPd9lGgGYqSvR6lv8hrFsL9sZYAqKpFa55eUmndTv5uu4zTfM78kmGsIEnErw6YBSMoF8x65OJVtaocEWWTnWCeYsxESr3RZlSY5ZqzKnZQOk2bvmMxaflbNfhLJ2iELBZLvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : این جنگ ایران را به‌شدت ضعیف کرده!
🔴
دیگه نه نیروی هوایی درست‌وحسابی داره، نه نیروی دریایی، نه تجهیزات پدافندی، نه رادار، و تقریباً هیچ‌چیز دیگه‌ای
🔴
با این حال، دموکرات‌ها میگن ایران الآن از چهار ماه پیش وضعیت بهتری داره
🔴
باور می‌کنید همچین حرفی بزنن و ازش هم جون سالم به در ببرن؟ بعضی‌ها چقدر می‌تونن احمق باشن؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/129137" target="_blank">📅 16:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129136">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_Mgfi3FHR6jj8PJdBQX_k2PmEbkEM7uitevIsBClHvOWHI50hPX4lYOhdi8_b5kWoGhqtlosLpr5tib_eq9XTDgicbZ3vbFtskhmr2N3wYfi6Udhu2ZX_1S-UIxNaBTfBhXUV_jqToCfv8PxLDse3L79B7DMvY1aSmXxurrz38IZ-kr7YdbKZImPeJt6e7UE98yY8H-J3UrJfj49xDKhGvCYQ8bKjY7B7VKu6ETWxv4F6dschy5EKZ_S_iedeOZkWpPXFCfieCuZFegLyI-V7-Toh0HqPYket8STINzk2OQOrLgiFx5te_qVF4V3L9fN37Gnpz83v91vmCxmRs4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش عراقچی به اظهارات وزیر امنیت داخلی اسرائیل:این‌ها رجزخوانی یا اظهارنظر یک دیوانه و نسل‌کشِ بی نام و نشان نیست؛ بلکه گفته‌های علنی وزیر امنیت داخلی رژیم اسرائیل است.
🔴
فرقه مرگِ نسل‌کش که مقر آن در تل‌آویو قرار دارد، تهدیدی برای تمام بشریت است. این جریان همه انسان‌ها را تهدید می‌کند و تنها هدفی که دارد، جنگ دائمی و بی‌پایان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/129136" target="_blank">📅 16:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129134">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lb1pxXe8Ex5cFRLfPgq7SzImLeF6NfKDerBXuHjUlH3-rJq9phiIee-t0CyKpxft2HiQ-jUS-TmHhxtXhpGb2HWhBIRnUMU4FpVNXqRw71uSlv5MGUDY3dNadldymN8GSvt98v3cl_Dxh2Rv4_p04cm3Km9D2wQX9lFJ1eQvDB68m4m-jqZcfnXYt4TAUeywSCCJRiGlJJj8E1yWxnvinjXnX9XvtgN09xj_o8ZsIZI4bjMBaVbdB_4nc2DG0wRPk8FbFpSETsmE-ggQn5vnx0JHC1PwMpY6unUKNtHz7ZE7FYXcnlvShD7bqTC-3ipY1kcayIjNdfUdTH3wz2bkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PAZ-Lq-8w4lvZh-nsWoP-XYwdZvmPDAPaDvQ2TuVzBdoFNBbNXPdqUrbgahqzGSAlUr3nypnIAjOmSMaugSlJn-Kh868fUsdpv3PxTHW8uKCevDp6AXhLWcohgGWSt4lccyKxihHEsv3Q46Xjq245GQ4Hcxijb0OegBMjmZhiS-jgYer4TEF_oyDRuhXGMeTV8CPFxWPd2afsN_44vpNA5Cr4BlQJ_897Hsyr-WGW4w4tzvPAdfNDaW3HVdNKI-jbrAQWLGkUfT4NXNbMCJ2H0yUSXmyzwSajOok7a1chvQXoDazPlMxa1pnHvSOZyCdviqulIWuIQw0TSItNU9UEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصادف شدید کامیون با پراید و فیدلیتی در مشهد
🔴
۵ نفر دردم جان باختند!
🔴
از پراید چیزی باقی نمانده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129134" target="_blank">📅 15:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129133">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گزارش سی ان ان، ایالات متحده به ایران «به اطلاع» رسانده است که اسرائیل حملات خود را در لبنان بیشتر نخواهد کرد.
🔴
یک منبع گفت: "حزب‌الله آتش‌بس را نقض کرد. اسرائیل موافقت کرده است که این آتش‌بس را به ایرانی‌ها رسانده است و این وظیفه حزب‌الله است که متوقف شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129133" target="_blank">📅 15:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129132">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خبرنگار الجزیره از حملات هوایی مجدد اسرائیل به شهر النبطیه و اطراف آن در جنوب لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129132" target="_blank">📅 15:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129131">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb5ICu34TgFV0QC2GUhdgLM3LiY2dnUE9AHPuRkHAGwSPFmFbGI1aYaAmvBRZYG2yA36B3F_ly-EmHMFx63hRfNn6lZjXuyOyvFHKDBpbm52g2_HzZlE_IDh7d5AjV7aCCbV4SNjgK4br5kXqfE3pFvyIHwpJpb2ePULXYjFmPc90Osj8oCKVkXp2iWNqhi-Ba8wlxWG1lI443Y7uSxLP50nsPzvsRX8zcnVxMzhIPSLXxqO6mL1bnjisWhEjT-0Q7b142SNUzvojcCKxr9TVGOGkxI2-z4qOsXeCuNQ_uo49XkjoNXA9gfHiNNVuY1M1BMagc6zUKKVk0qkIbA-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر آمریکا در اسرائیل از حملات این کشور به لبنان حمایت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129131" target="_blank">📅 15:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129130">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ در پاسخ به منتقدان توافق با ایران: برخی تندروها دیگر محترم نیستند
🔴
من یک آرزوی اصلی به‌عنوان رئیس‌جمهور دارم؛ هرگز نمی‌خواهم به هربرت هوورِ مرحوم و فقید تبدیل شوم
🔴
بعضی از افرادی که قبلاً به آن‌ها احترام می‌گذاشتم، دیگر برایم محترم نیستند؛ آن‌ها تندرو هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129130" target="_blank">📅 15:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129129">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
خبرگزاری تسنیم :  تنگه هرمز رو تا عقب‌نشینی کامل اسرائیل از لُبنان مسدود کنید - تموم مذاکرات رو لغو کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129129" target="_blank">📅 15:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129128">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
معاون وزیر نیرو: متخصصان اتمی روس به زودی به کشور بازمی‌گردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/129128" target="_blank">📅 15:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129127">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_sOUqjVFjUUepv5dqgXaxnk4Go1abYPxIPtBqGZl9xoOB3Wj6O1pFtaB4X6xgGjhRyJxqCOdCvURLVK3sW1LWcy4oaITOO4tb7eu_PQqJFgrkhAx4LVsKFRydQmbSXdHglB1zYa8WKip86LWCv_ubwVdRqtv5NklCcjqTRFGL4ISNaUS8ZYP9cLKHTMXRlB50de8yega6MxdRmR6cU8yuHAcWSBMOngB8hB9q0dwLMyIWtskmHoO1safqBWx1W_d4-pdvqlx5AsM703v7Q3TNTfKFs_q_rDredfcOpRZtpHXMdFQbDbkBlqsGyzbUXQ8RaWA3rjElqxJTj8VofKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی شورای امنیت ملی: دولت باید همین حالا و از لبنان شروع کند و نباید اجازه دهیم مردم مقاوم جنوب لبنان مورد قتل عام قرار گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/129127" target="_blank">📅 15:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129126">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129126" target="_blank">📅 15:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129125">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خبرنگار العربیه در سوئیس: مذاکرات بین آمریکا و ایران ظرف چند روز آینده آغاز می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/129125" target="_blank">📅 14:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129124">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc08f96bc.mp4?token=p-1pbZwSsN0Dz_81KFYR3Om9LFnIUG0P8_ZSJJwz6DP_vGACFyEaf5A0090JecyOZaoQzLRQGQxijVPtW2t_-w9vMcChP0KIelZibqIh6ScWopdeijSvslE53OVW0GeG0zMWOhtUDhvCtskXa5TcYjGiTsvUMV6liBOwx5a8KBoPsVmL4WgINu371VayzfOVf4spQOZzpCE85xGELMrUGn6dhVLlfr0Z7dNP3kpw6GNBiHyK3FBtUkxHiNXw2LA3TqazQtf_5AKdMtQZVqaSNbaXQrgPo7LwWZ4PZiRR-dZdIPobzpVD1OmDb3AHkYtQ2gNN8jC97QFNdFyi5x2CKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc08f96bc.mp4?token=p-1pbZwSsN0Dz_81KFYR3Om9LFnIUG0P8_ZSJJwz6DP_vGACFyEaf5A0090JecyOZaoQzLRQGQxijVPtW2t_-w9vMcChP0KIelZibqIh6ScWopdeijSvslE53OVW0GeG0zMWOhtUDhvCtskXa5TcYjGiTsvUMV6liBOwx5a8KBoPsVmL4WgINu371VayzfOVf4spQOZzpCE85xGELMrUGn6dhVLlfr0Z7dNP3kpw6GNBiHyK3FBtUkxHiNXw2LA3TqazQtf_5AKdMtQZVqaSNbaXQrgPo7LwWZ4PZiRR-dZdIPobzpVD1OmDb3AHkYtQ2gNN8jC97QFNdFyi5x2CKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش صداوسیما از آخرین وضعیت تنگه هرمز
🔴
تردد کشتی های تجاری در بنادر ایران از سر گرفته شده
🔴
در روزهای آینده نفت‌کش های ایران به سمت بازارهای جهانی حرکت خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129124" target="_blank">📅 14:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129123">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d85acc4b.mp4?token=QjAMwi4JI4JkL-nUWG-iJPBtnbDLJourhvLf574aY1RAKdC__clAEwX0B19iFTgSGDeE8rTgZFU_Zz3NPKFipxekAWtPc1J8mIDm5M_9lL84XXUxl_6fd3Gxjr0JDNbwu6MIzQXqRAmGVdgiBf4d_4DSw64ClJLKI1R3bIgI6WADm60ouMAMcF6xz-uQxUwA8-G_ipvUgCau1v7eq6FxV6gNCvXhhdv3jN4SkIWmYaSlopZTyBf3NLhdXm3LJocGORh9pRgWEkwj41xd2tr0kenQG-riM-OcVx_zbdW7LCvezgCBBlfbWyaBJ5Tq1fqiMVX5Oz4eqzzsFgqQv5Ju4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d85acc4b.mp4?token=QjAMwi4JI4JkL-nUWG-iJPBtnbDLJourhvLf574aY1RAKdC__clAEwX0B19iFTgSGDeE8rTgZFU_Zz3NPKFipxekAWtPc1J8mIDm5M_9lL84XXUxl_6fd3Gxjr0JDNbwu6MIzQXqRAmGVdgiBf4d_4DSw64ClJLKI1R3bIgI6WADm60ouMAMcF6xz-uQxUwA8-G_ipvUgCau1v7eq6FxV6gNCvXhhdv3jN4SkIWmYaSlopZTyBf3NLhdXm3LJocGORh9pRgWEkwj41xd2tr0kenQG-riM-OcVx_zbdW7LCvezgCBBlfbWyaBJ5Tq1fqiMVX5Oz4eqzzsFgqQv5Ju4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهر نبطیه در جنوب لبنان در حال تخلیه شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/129123" target="_blank">📅 14:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129122">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
حزب‌الله: دشمن اسرائیلی به نقض آتش بس ادامه داده و با ارتکاب کشتار و تخریب زیرساخت‌های غیرنظامی، آن را تشدید کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129122" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129121">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / نخست‌وزیر پاکستان امروز در توضیح درباره تماس تلفنی‌اش با همتای ایرانی گفت «رئیس‌جمهور ایران دعوت من برای سفر به پاکستان را پذیرفت».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129121" target="_blank">📅 14:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129120">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOYIM5GDERvrCLDNrtb6wzK87kFG0uzAG4iTFRCW51MzzUWgmVcvOEjV8ajpfidaQNrVVQdKseipk4TxLj3bWY1KgST_VCh9GJ7ruZBA45e-V0QGkbVPtFNwjK1i3AteI6d61J5l5WkJ_uYu_qBXJOJQRQH0eTTfsnjNq-XOonv_Beu_Lqx-7RuFhPu4X6UjLGhPjIWElLpfoLkWZPu9jb82vJQqmRbyLx1zhj6px-NxCm6eLsNxJ3ZchA5ywMPJ2brq0MEcg8Sk1MpppJe7WnbYkVzV9JMS_JW6xufi_8l7Zb1pwP02OAy26DfHYSojDj7LOCUJb6SqN0ZAW2h6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو تیم مذاکره‌کننده: ترامپ به تعهداتش عمل نمی‌کند
🔴
اسرائیل به شدت مجازات خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129120" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129119">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orMRMUsk6HSoUJEcfsQVRlFqUXmJvHcMmDhk9YQMFXCX98SE18dhOeCeqTOWoIh7EWeVbV9Jb3Fj97KzDeUFp1WEquaDKeQDSO_tfmVrJMLHOEOCU4t77jh6oBXZdK6jFQyYsWv3E9Em5KH83SnLeuX5K5uqS2mmxKsMApZLNgUYF6jr_NIPZXM6VgYDdMxDC1_RF-xlV5PU8-gBTcfXdT3kSsnBE3mERVpLipruRU5j3r7l87Rs5jX9VqstwjJFD9XpMbTVnf19vkKUjN-b67X45yxa2yhpCaEc85Mog2rAwQJRLptssWhFbowRuL3UNcMJMVhmXRHXWZn7me6Lgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت آبراه خلیج فارس: با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129119" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129118">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری / گزارش‌های اولیه حاکی از بسته شدن تنگه هرمز و شلیک گلوله‌های هشدار به سمت کشتی‌ها پس از حملات اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129118" target="_blank">📅 14:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129117">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30950fe2bc.mp4?token=YZSsSIaqm1rv-BJ10XjXSQ3VgTKwF2zOSg5kwtqG81lfhlB4mvrk6EaH-zyACeSkMXXMpSjUh3uscNmJxqUTZecgQxHGO28aO0EYWKjYAxdMWRye7fMRvKH5epJSwR21KfLUd1wcKn4t_AQYZsIirRQMUUVCP_PhfptkMsz8tlirnb3VqWHWCUw9jnKCGZo8Fd7hIxSIH0n4qWLEdmtcXq7e2Vw_7aVTQwytM9nKVKI6eJ8F43v1Br37bZS-hhgBSKspyy2q6yhzswzTPg1Cjnrgg5arYggoRVL8eIUK63jDFtKngvH6w1SClkVel_XURQMHzTDQeqjWGYJXs0yX3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30950fe2bc.mp4?token=YZSsSIaqm1rv-BJ10XjXSQ3VgTKwF2zOSg5kwtqG81lfhlB4mvrk6EaH-zyACeSkMXXMpSjUh3uscNmJxqUTZecgQxHGO28aO0EYWKjYAxdMWRye7fMRvKH5epJSwR21KfLUd1wcKn4t_AQYZsIirRQMUUVCP_PhfptkMsz8tlirnb3VqWHWCUw9jnKCGZo8Fd7hIxSIH0n4qWLEdmtcXq7e2Vw_7aVTQwytM9nKVKI6eJ8F43v1Br37bZS-hhgBSKspyy2q6yhzswzTPg1Cjnrgg5arYggoRVL8eIUK63jDFtKngvH6w1SClkVel_XURQMHzTDQeqjWGYJXs0yX3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اکسیوس: آیا می‌توانید اسرائیل را از حمله به لبنان کنترل کنید؟
🔴
ترامپ: بله. آنها احترام زیادی برای من قائل هستند و همان کاری را انجام می‌دهند که من می‌گویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129117" target="_blank">📅 14:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129116">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نتانیاهو : اسرائیل تا وقتی لازم باشه؛
برای حفاظت از شهرهای شمالی‌اش، تو نوار امنیتی جنوب لُبنان باقی می‌مونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129116" target="_blank">📅 14:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129115">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نتانیاهو: ما حمله به سربازانمان را تحمل نخواهیم کرد و کاری خواهیم کرد که حزب‌الله بهای بسیار سنگینی بپردازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129115" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129114">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaJ9bPCHq7Z5fot8jG6hJ0NUrFslbdD_EiXTxclQi3wn0NVHVFhG13jJAXrIrsfj7ECLzNz_1jEIUbn282I2Plz9I11NcLJV6CtpXE3-eGXnt1nCBwxbxVIRgPnfCIAZlgZkwqkWi4yMcfhAFsI_ut-jSvMQ4JouWpRhooWBOUqmZ8zw7A-Bhi3ezF2aR4XE4P-AICts9ZyHh_aVl1Z5EQ1kV3lel4IfCrCrika6N7QgBwjWMIP2HWY0OafpiT2kTtAZCCPGK06MPrICwy7xbwzTR0oErJqvxdcnJorshysKwneyeYPdOXQyb9zF_BiCvstrvqhCrLnFVLbls3zRSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل هیوم خطاب به ترامپ: می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی.
🔴
آقای رئیس‌جمهور، شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد.
🔴
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/129114" target="_blank">📅 14:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سایت ردیابی کشتی ها، کپلر: ترافیک کشتیرانی در تنگه هرمز رو به بهبود است و دیروز ۲۵ کشتی از این تنگه عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129113" target="_blank">📅 14:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPodxm4pldB09av9hd1h9jqI_WFjl2GdCSyq_qTQeIQwHV0WD1Fp3GEoK-yoyjlJXYcErYbgAXcLDW4sPob_r2TLHy4s4Ygt08_eSq_p4g63FQd5zme2Y0_d2T6wHjseHpjg2oHOaz3JQ9SPTbShb2EFa23NQGBmqMWFvbmdgFLJh7VQKGdo2wwDZ_vu7Mq01AWvPYANOy01QvFK8so2UVkK-w4uM14vIB8Ade4N_p1wHFxihVuecenVeg1ZyXKg8V755X_XMcx5cxU8c4VbI324AlnLKMtb88cLLX5MNtPzKLjmF3_xHXvsrInrEE-HRMu-3pRI4nQsq3GsUeeNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش ثابتی به حملات اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129112" target="_blank">📅 13:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ به اکسیوس:  اگر مداخله من نبود، اسرائیل له شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/129111" target="_blank">📅 13:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5rkpKFl5sh7RbK95n0kjoLtb0ig53y5J5i_VTgiQpoPTQTgR60xR528R6Z1A3t5ayI7l7YcI3L07x319NldancQz_gTwphEwDtoV91L_BKBQAuKaFfRo98Fv0i7IOgC2tB2R4J7VyD-XMP583h2goxnAqq8L7KeIpmUwUKhxHXF76-qP-KuDbIbb2NQ9Mzxt0YpwTQtkQNY-F67s0FowHKTw-i_CwoMwRSdG8P_g-ldWm98RV4PyAZyWN9U4LgcKk_1ybWQ6yVBffUtv7Yf4AsBdrxR92Hzp_1os-pl3reGXJedK_GoJe2TLDovD_2jxGdtSZ0jk4Ot6n5JX6zAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز نوشت: در طول پنج روز گذشته، جمهوری اسلامی ایران حدود ۱۸ میلیون بشکه نفت خام صادر کرده است که ارزش کل آن بالغ بر ۱٫۴۴ میلیارد دلار برآورد می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129110" target="_blank">📅 13:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ به اکسیوس: رابطه من با نتانیاهو خوب است، اما باید او را کمی منطقی‌تر نگه داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129109" target="_blank">📅 13:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر امورخارجه پاکستان: هیچ مانعی برای آغاز مذاکرات سوئیس وجود ندارد و مذاکرات باید ظرف مدت ۶۰ روز به پایان برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129108" target="_blank">📅 13:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129107">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
قالیباف، رئیس تیم مذاکره‌کننده جمهوری اسلامی: مذاکرات با ایالات متحده همچنان در چارچوب «خطوط قرمز» تهران باقی خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129107" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129106">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: هیچ مانعی برای شروع مذاکرات سوئیس وجود ندارد/دلیل تأخیر در مذاکرات سوئیس مربوط به مشغول بودن مقامات ایرانی با آیین‌های ماه محرم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129106" target="_blank">📅 13:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129105">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: دقایقی پیش زیرساخت‌هایی متعلق به حزب‌الله را در منطقه بقاع را هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129105" target="_blank">📅 13:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ارتش اسرائیل: بیش از ۸۰ نقطه تو لُبنان هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/129104" target="_blank">📅 13:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شبکه سی‌ان‌ان به نقل از منابع آگاه اعلام کرد که پیش شرط ایران برای شروع مذاکرات در سوئیس توقف درگیری‌ها در لبنان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129103" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bd4028ca.mp4?token=N31xzFyfrOncev6SN4B7pXnnwjD2-bRyW2vfAEAC2PJbXyK0VQIVpM-dzjv47owkaTcJTUv_Hff7PSe0iug-OXjzarhg4L7Bb6SqPPUq0WQysh91pykxuZj4PyD2OIFfuKMfTrENllo8oD0RW1Z3wg9pcKl0yGiqBHoezjZl164igx-spBgZquWzd5sFNw5dPr3ntpNQIuskmy7-tR43cmmE0z3StTlCA5ovADb544VwwsoDz1m-AnkZ5zYwGFGIL_p72ZcYAULLeXcoi69ro8pedYGErrNovnIqYWoEBcOVaacPRkKXX7vWUiSIoMy4wNQUcAcEt7fNHhSKDISr6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bd4028ca.mp4?token=N31xzFyfrOncev6SN4B7pXnnwjD2-bRyW2vfAEAC2PJbXyK0VQIVpM-dzjv47owkaTcJTUv_Hff7PSe0iug-OXjzarhg4L7Bb6SqPPUq0WQysh91pykxuZj4PyD2OIFfuKMfTrENllo8oD0RW1Z3wg9pcKl0yGiqBHoezjZl164igx-spBgZquWzd5sFNw5dPr3ntpNQIuskmy7-tR43cmmE0z3StTlCA5ovADb544VwwsoDz1m-AnkZ5zYwGFGIL_p72ZcYAULLeXcoi69ro8pedYGErrNovnIqYWoEBcOVaacPRkKXX7vWUiSIoMy4wNQUcAcEt7fNHhSKDISr6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
چرا ما در سوریه در طرف مقابل هستیم؟
🔴
چون باید آنجا باشیم تا از خودمان در برابر آنچه در سوریه می‌بینیم محافظت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129102" target="_blank">📅 13:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c80f50a64.mp4?token=JoXQP90qShE7SWlTaJjt9m3TtJtFnrzDxPy9hHfN4dbdu7UrjjW_Rn1eDujmeYKyYRd4K8Q8fCP404pOKg14okotkViuF3sDjUjXoqHkd3OTP3Qa7NhbMVwJIERcGOAXruHQ2zFcbMeaRyILinRfjOeLKBDiQtH8o7o3SW61YGVAcqYLRJmoYQMsL30ipNgK-AkRnYGLYInmUs1UeFKKuJUWqDRYo8wj7Xq_TqgB8yDFyei73ReHMk5UaeTIZdhhoXhsSRZNamP4GGCMKFAgSz8hTU0jBZjYIuv3P2dYIiVyOQzSfAriXWXFJMHzWhpQrdJ-ig0GkqXVVI5ltAxq0L1yUaB6XM4-IMbeM2OeL3hBwMIERyMvcwZ--SFfajPCPz1IRziiH-3Ge5mexEj4tt7XxeDIXaSwxQebAqaS63H5ZwW7axTbRKRrVU6aqP_Gs6lugayuOcd9td67J3s0eGaJk2gMBcVbINpapO_2afoICDByxmPKMVDH_vMKiC-DANtEYRgq7qwexQ1RDqc_KzzJV4rKuPfun1doYn8vpXy-kee6FxfPw9YVj7oKuF5UaYAY0aLKWEVVSSShzuFsBbtSzkwpAH4IH6JelI-YgTm87ULI41SAlvJnZfYlUomav8nu7fa3RVziDxKjhOxb6TNwGqdBrnbbdgfPiNLzrMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c80f50a64.mp4?token=JoXQP90qShE7SWlTaJjt9m3TtJtFnrzDxPy9hHfN4dbdu7UrjjW_Rn1eDujmeYKyYRd4K8Q8fCP404pOKg14okotkViuF3sDjUjXoqHkd3OTP3Qa7NhbMVwJIERcGOAXruHQ2zFcbMeaRyILinRfjOeLKBDiQtH8o7o3SW61YGVAcqYLRJmoYQMsL30ipNgK-AkRnYGLYInmUs1UeFKKuJUWqDRYo8wj7Xq_TqgB8yDFyei73ReHMk5UaeTIZdhhoXhsSRZNamP4GGCMKFAgSz8hTU0jBZjYIuv3P2dYIiVyOQzSfAriXWXFJMHzWhpQrdJ-ig0GkqXVVI5ltAxq0L1yUaB6XM4-IMbeM2OeL3hBwMIERyMvcwZ--SFfajPCPz1IRziiH-3Ge5mexEj4tt7XxeDIXaSwxQebAqaS63H5ZwW7axTbRKRrVU6aqP_Gs6lugayuOcd9td67J3s0eGaJk2gMBcVbINpapO_2afoICDByxmPKMVDH_vMKiC-DANtEYRgq7qwexQ1RDqc_KzzJV4rKuPfun1doYn8vpXy-kee6FxfPw9YVj7oKuF5UaYAY0aLKWEVVSSShzuFsBbtSzkwpAH4IH6JelI-YgTm87ULI41SAlvJnZfYlUomav8nu7fa3RVziDxKjhOxb6TNwGqdBrnbbdgfPiNLzrMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
یادتان می‌آید حملات را؟ آنها وارد می‌شدند و بیرون می‌آمدند.
🔴
ما وارد می‌شویم، نابود می‌کنیم و ترک نمی‌کنیم. این کاری است که اکنون در لبنان انجام می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129101" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129097">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLyRYeDm4PG4US-NI9g8NEml9EQegaWs-d8dWvVVF2Tur9Hsnnq4eV_2c0X39j-yufkvVy7vrmMxFHKfjVqvkYS3dwU1BJ5_PHl9jm1zA4d1k2VdARtKSeX2Pitmu8bUaV9Vc-2SNj4HKbZ2FWj67yLgV2-lWJgwvVTJWR0czVnAj1l82oSnjTos9ZgO5JXl4l-S5NZln2rjD-z5v5NiFhrCbQX41BRAISMstzPOUQoer-o2fCKut4AEtoDXbQf_OWbw5QrUOd-tiNyBa2qFtxoh2ItbmTPPwuiMDHMlHQG6Y01xGQLwrigQOV5e4oWNaRDS5vfJTWmSGN_5bKxyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giqU8MHTkGWmUJ3g7AZZ8MVSMf6ye5n_JcL07iHGojwQZ_K5QJzEhklg0ZaxFEFF8IMdzn6P7wiwKVL-Bpv_AfUoxI0qf2FEtgwdze2aa4Ap8JELpAIrvgtwL2wv_YVSFPADuMEgKoA9oVFJhMkzl6KCgP5Qckm1LbTVwhvwb5JjF5yZAe7JRSJ1YtgCEC9HS6useB_37CDWF2gyvEixPbFZhi780qgdCaFDhSpL6NMskpPAI0E2OLD7dsLuyfMVzB3sqbMixaiDArT7hZijxjK5qmwnYi-wpIjcApptD7z0TsYVhFtGh6wVnTxUGSwqP9Xfw4tGBunFjoKhuATsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N77VtiXDOJUC9fV2FQtN49S_LAlslixlmpF_wrZ2FJ-ZyggRqqwtF_YT1AEijETQL1E8Zpy_p6DMuZEjCWofYZz7NaJPjCnV0RZHRWngtIBoDoAkIY9AKYape1OjbkBUk9JHgwVrsT__a4q5xNCO7fnWPXsXl5-cqXiy5dJ-1w3cIWVTEFpdKO_jMUwq09l7xmdvGEjGSLsji8XFm4DVm87hJT9zM6hwZZQk4U1rhRj-ja-q4bjjJPLCw42Qj-UV4n8RmHVVgOqgLLlGMSzRsW2_4dxuJaO9ZwcCizwjvwEssf3oo5Zjqbfp3oTOV1vc9Ndbv4Vb6GAJ5DxkiOzALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuCsy8jd9G8Z3FitXEVWYuk4sTTd1BnRGOFSPfQj0L5-PbdoJB8JeZrbf19DpTa8wGQgkfBCK2Gp1DLldzGg7AbjVKwPLJDWY8Y_MryiVMgc44SQAKxNfQ0cK1N2tdRrf9bC2TNa0HH-zGBrnHqQy2C8dPH_exI1G5tuKs_1OV8qY4mb1pTo4haCBIOM4NWRsNTZZHT5ekYJlV4rwJWS-1jmLe9F5-gs9GCLIulL7yTdK8lVEqfo4vdsZf_CwU7OjjWcr7qHAlrbO_htxICNFMYu-gKvpXRn8E2Bz_UDsR34hPzMShahNkofpTxonjlA14vFCAUDgEUqsCbLOp7IdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات شدید به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/129097" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129096">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بعد از پیام دیشب مجتبی خامنه ای دلار ۱۰هزار تومان و طلا ۱میلیون تومان گران‌تر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/129096" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129095">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba0R5Bzrx5I9gRN5nGsFsichSxn8PObGJARTGUCOZnKqeUsRSHcT8Vj4-WpDji6WepuItR58B_8u554107jvEJbHWyljo1tJ2-fe02kEVR20NSHksyWefJaJ3aAwHJ8b-EKdwNenjyOcnii7pk2Wc1YKvyRRxfZxmhqMoWkd0mNThxVlZFxpDGrvr0BXvbBgR6CMw9J2x9a61ATSE7duku-zyICo0-Yt1E96qNEXvT1_Hu7lntuZiQpVnM0oLnzqx6xlLQLzIua31FpfMGYckDwq0UfJ8Sct-E0OJG3B4Ab9a5mFiZ4ljaUIgmQ3M17V4exxo8wawxsCwOgSNF4otA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسموتریچ، وزیر دارایی اسرائیل: «وقت آن است که با آتش سخن بگوییم. دروازه‌های جهنم را بگشاییم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/129095" target="_blank">📅 13:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129094">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
در لبنان، ۲۰۰٬۰۰۰ نفری که در «منطقه امنیتی» زندگی می‌کردند، بازنمی‌گردند.
🔴
هیچ‌کدام از آن‌ها بازنمی‌گردند.
🔴
نیروهای دفاعی اسرائیل آنجا هستند، زیرساخت‌ها را نابود می‌کنند و روستاها را ویران می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/129094" target="_blank">📅 12:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129092">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19bde11aa.mp4?token=lU9oLrZ1hga-xXTPbOBH5MVpv9BJneTXMnuMLuvKKTg7brr0N40J4OGiHQPQMpUu9zXiOla9j5eiMqJZWCrlTrzXFSC07ES30iezTpG27tPTIKbDzRIYst7ixhwgOvNVTuXbbMWoCOhCAt-vDxNQ_3YhPVVj3cUWN1Up6OqSv__Yr0uuW0Jmd2Dai-ysuKbeaZsXaQHdFbYLt0VhRDFiQSnxJjGHgeLSc-q3TT1ogt-6hQOGnEFelWG8QHbPqDzl0FE9OM1GVBTdwqnifmOk4cgXqm2aDy-UCnNsfSKEekNQsH9NmepGiYXh4klU_Nfe3uog1qc2UV9SZ8xj6-BtPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19bde11aa.mp4?token=lU9oLrZ1hga-xXTPbOBH5MVpv9BJneTXMnuMLuvKKTg7brr0N40J4OGiHQPQMpUu9zXiOla9j5eiMqJZWCrlTrzXFSC07ES30iezTpG27tPTIKbDzRIYst7ixhwgOvNVTuXbbMWoCOhCAt-vDxNQ_3YhPVVj3cUWN1Up6OqSv__Yr0uuW0Jmd2Dai-ysuKbeaZsXaQHdFbYLt0VhRDFiQSnxJjGHgeLSc-q3TT1ogt-6hQOGnEFelWG8QHbPqDzl0FE9OM1GVBTdwqnifmOk4cgXqm2aDy-UCnNsfSKEekNQsH9NmepGiYXh4klU_Nfe3uog1qc2UV9SZ8xj6-BtPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل علیرغم اظهارات دیروز ترامپ و ونس، همچنان به بمباران لبنان ادامه می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/129092" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129090">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278b037b53.mp4?token=sCoeC_lQ6CHhuyhqTn_2nY9WYqJ95gI7IdjYH2tt6-253nPwj75tCxX_pzqlc5cHPC7GlU6m2LSWo0jMImTnLTF7PDAKwbBfnjvsGr2Ky2y7UsW4St12k507vMTEHG4scLMHL-adzO6legQ-M3mcLKsvcxmjXXrm4Zjqv1gX1GMp5k_Xgw3D7rSlwm1XI1LYHxEaaSvuvgvyJMtsQBQEN6HOl106Phf1r7wdEeNTyMyk1TlULIj2UxNzlQM-jV_Qdf2lQnL7-ZZw0GbWSgYVJ36wyp118xTEPgiYBzuvDPaiwhNFwORuuFkFSPkCjPfffPSEsErVM5163wKOa3p4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278b037b53.mp4?token=sCoeC_lQ6CHhuyhqTn_2nY9WYqJ95gI7IdjYH2tt6-253nPwj75tCxX_pzqlc5cHPC7GlU6m2LSWo0jMImTnLTF7PDAKwbBfnjvsGr2Ky2y7UsW4St12k507vMTEHG4scLMHL-adzO6legQ-M3mcLKsvcxmjXXrm4Zjqv1gX1GMp5k_Xgw3D7rSlwm1XI1LYHxEaaSvuvgvyJMtsQBQEN6HOl106Phf1r7wdEeNTyMyk1TlULIj2UxNzlQM-jV_Qdf2lQnL7-ZZw0GbWSgYVJ36wyp118xTEPgiYBzuvDPaiwhNFwORuuFkFSPkCjPfffPSEsErVM5163wKOa3p4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهر نبطیه در جنوب لبنان به ویرانه‌ای تبدیل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129090" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129089">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd73e104fd.mp4?token=S0RULzFeZHuVdEb3p5Jc8h0WwhGW21pTDhiDqKc2ixoyCQoxB09Ktig5bpEAIL17uer4nCwdCDTDGGBI9FXs3VAqoNffDBgtmIslMBhVdIHMP_LyyPE97UO6bgkx1yeS_tpM5tSK1fAx1vJZYYsTpYZwe-1ZLAXh-5wCQDpF6rLopLc-JXAin8prNr1lNb1lNXEycyCuNqAKUcM1dySoyHdPZdVEmzKHcF-Nuj3eXZD1OO9Au2FsLmLrPbbJOLQVYr0-AENeKz1LVMWhZeYsafYvgCLgi6CdQ1uweM6xJU2dT2eEqccwPm-6YsGRw7q-yymkUvb3iFGIHryW45ME-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd73e104fd.mp4?token=S0RULzFeZHuVdEb3p5Jc8h0WwhGW21pTDhiDqKc2ixoyCQoxB09Ktig5bpEAIL17uer4nCwdCDTDGGBI9FXs3VAqoNffDBgtmIslMBhVdIHMP_LyyPE97UO6bgkx1yeS_tpM5tSK1fAx1vJZYYsTpYZwe-1ZLAXh-5wCQDpF6rLopLc-JXAin8prNr1lNb1lNXEycyCuNqAKUcM1dySoyHdPZdVEmzKHcF-Nuj3eXZD1OO9Au2FsLmLrPbbJOLQVYr0-AENeKz1LVMWhZeYsafYvgCLgi6CdQ1uweM6xJU2dT2eEqccwPm-6YsGRw7q-yymkUvb3iFGIHryW45ME-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.ما از «مناطق امنیتی» - نه در سوریه، نه در غزه و نه در لبنان - خارج نخواهیم شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/129089" target="_blank">📅 12:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فارس به نقل از یک دیپلمات آگاه: ایران پیش از بازگشت به مذاکرات با آمریکا در سوئیس، خواستار دریافت تضمین‌هایی درباره پایان یافتن درگیری‌ها در لبنان شده است.
🔴
تهران تأکید کرده است که توقف خصومت‌ها در لبنان باید مطابق مفاد توافق امضاشده اجرایی شود.
🔴
میانجی‌ها در حال حاضر برای حل این موضوع و رفع اختلافات موجود تلاش می‌کنند.
🔴
مذاکراتی که قرار بود میان ایران و آمریکا برگزار شود، در پی حملات اخیر اسرائیل به لبنان «به طور موقت به تعویق افتاده است»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/129088" target="_blank">📅 12:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129087">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">چجوری یه مشکل رو از سر خودمون باز کنیم؟
اون کار رو استارت کنیم و اگه دیدیم داره خراب میشه بگیم علی الاصول نظر دیگری داشتم
اینجوری همه چی رو میتونیم بریزیم رو یکی دیگه و عزیز بمونیم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/129087" target="_blank">📅 12:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129086">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfddaba168.mp4?token=tWgxDFswQs1rETnxwqx09jl9Rmit5RnCN-z6XEmcUQ5fnARm6wkWc826HpExgJDDndhtwEHNCedL94EoGGR41rQO5KvCYcV_OHzpDvecSMy60nMMKObuN2wUGRD_ohFtoZutD4v9JVTud48NLb4WSZ2wvgBsHB1W8ed5_UsO3ibAU8K0kavSzNTt4YToZY0w5UKOx-0Ola-z1GSwrb1GnEPt_FB0HYtGXrlSQYbi7FqMblFMIwGyZxH2ZhpUl0blVI_Ydrq49lgFXp0Y4oRhDf_bdK6hT92kJiA8sooT-gMoop47NPuBZZp8rfsHVeMDuHfRv6cot0-nZlOf4R4YXBX-KiGvJwvlpSfLoYZg7Cx92YTe9RH1mx4tqmHX8kMu1HaOBItA2BNqqKOBXvQBANgmFDQgPhdS_wo43wtZ3EgvegpIO0op8-oNhNLjcopkhJTwwDQUsvvWjRGfNp6r00jv7oZslAro2eIcLlQKTnw8nqhPUpz0u5izBnYKKrN9eRFrpfG_VxLSatJX054BWikVa9WbKIQpbk2fP3XF7qyknlKDn8VgIGRf0yo2UYp79EbcKw7Skp_2HXrSxc663ASiHulnyHpwNeZlMCu9KqR1aavmhpZLSrmQ_hWcvkNI-CGVRO3bd-iLwKRr4Hejq-9Y80V8HNzauhZ7hq3BHsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfddaba168.mp4?token=tWgxDFswQs1rETnxwqx09jl9Rmit5RnCN-z6XEmcUQ5fnARm6wkWc826HpExgJDDndhtwEHNCedL94EoGGR41rQO5KvCYcV_OHzpDvecSMy60nMMKObuN2wUGRD_ohFtoZutD4v9JVTud48NLb4WSZ2wvgBsHB1W8ed5_UsO3ibAU8K0kavSzNTt4YToZY0w5UKOx-0Ola-z1GSwrb1GnEPt_FB0HYtGXrlSQYbi7FqMblFMIwGyZxH2ZhpUl0blVI_Ydrq49lgFXp0Y4oRhDf_bdK6hT92kJiA8sooT-gMoop47NPuBZZp8rfsHVeMDuHfRv6cot0-nZlOf4R4YXBX-KiGvJwvlpSfLoYZg7Cx92YTe9RH1mx4tqmHX8kMu1HaOBItA2BNqqKOBXvQBANgmFDQgPhdS_wo43wtZ3EgvegpIO0op8-oNhNLjcopkhJTwwDQUsvvWjRGfNp6r00jv7oZslAro2eIcLlQKTnw8nqhPUpz0u5izBnYKKrN9eRFrpfG_VxLSatJX054BWikVa9WbKIQpbk2fP3XF7qyknlKDn8VgIGRf0yo2UYp79EbcKw7Skp_2HXrSxc663ASiHulnyHpwNeZlMCu9KqR1aavmhpZLSrmQ_hWcvkNI-CGVRO3bd-iLwKRr4Hejq-9Y80V8HNzauhZ7hq3BHsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز، درباره لبنان:تمام خط اول روستاهای لبنان ویران شده است.ما در حال ویران کردن تمام خانه‌ها هستیم. ساکنان دیگر هرگز آنها را در مقابل چشمان خود نخواهند دید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/129086" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129083">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCntsqAe46dH64mTe7AnX4YdeDXkY3ShSZRH0wX91gkS1lPXYNWzLIkdVnrMRXIBhE43uPW4Zc76o4cnfRfUzZemykzouUH9MoUnZF0ryRckuJBDvkFwhXIQmyJ-w53lYEjMUinJG_Sb5qUPy0ITkm9LpN0wNHh3GDe6qW5_TdMlL8HSPE7r694Yn3cQsQqSQPqUUtH3DuE3lP74Ldb2QdVy_kQFODvXRZEmVPZMyTActO0AI2SuWPg7BupIvRcPaQyv9ySp8Zb-4Tv25EQW1MkrNV1ktmUmDLN2JOgefGn1OIPpRUjrIWA8khuT-oO8aQPBoB0iNx8kzZvJbvMWTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رهبر اپوزیسیون اسرائیل یائیر لاپید:
اگر سریعاً این دولت را تغییر ندهیم، روابط خارجی اسرائیل نابود خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/129083" target="_blank">📅 12:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129082">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=IzNegGwC4HAYeynOIfF9o1iUnbLp7FKTSfv3jzdcyw3z_zgqAd246JvYzhKYcxAsdDiRzMPruCxQSrNnwvddXL0nuF3SJGnddJD42VlLKbpABxNp-jCpXFZo_MuWIkPUz2Fz31to_46uQEJs07krba7gwkVWwXzI2pgQ-VGs1_X_ZdPqitgqqhGeMMJJe6_fHBTN436nJbBJtZQM2VCg__jba1CoIB2z1Lw8fazubydP8-LwT7ZWYQN7WTZcCrOOlGxPDSOPxzQZB6iKyC5Jg5NcL8420aVTSXQg9s1EeFc56kMUUIkpsatQVJvZl61f425E7oTDWST-ejwEodvKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=IzNegGwC4HAYeynOIfF9o1iUnbLp7FKTSfv3jzdcyw3z_zgqAd246JvYzhKYcxAsdDiRzMPruCxQSrNnwvddXL0nuF3SJGnddJD42VlLKbpABxNp-jCpXFZo_MuWIkPUz2Fz31to_46uQEJs07krba7gwkVWwXzI2pgQ-VGs1_X_ZdPqitgqqhGeMMJJe6_fHBTN436nJbBJtZQM2VCg__jba1CoIB2z1Lw8fazubydP8-LwT7ZWYQN7WTZcCrOOlGxPDSOPxzQZB6iKyC5Jg5NcL8420aVTSXQg9s1EeFc56kMUUIkpsatQVJvZl61f425E7oTDWST-ejwEodvKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران شدید نبطیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129082" target="_blank">📅 12:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129081">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSZHZFgFVFgj2ReTZs3Kbgm-uNQWKtmkNoyMNoeuQNAXEIK71f-MnFjZuOo9-GSCMTvSFyYn3dhBO8csaXAgnaKy9MYmU_BDTTOKaPsrW7FrXa0O0BZ-KKnYiH0C0hadyW3CXtRodVU0Z0UGnjwpaJHqDvJm5UfC_Y7AmqSi15YWgCFXLmhEzFApcUrAF66G9JfBYc2TJJPZvwAObd97YSogKFdgj9WxeZeHAYXrL0p91VI89uzrp10DbfYtDZyv7rJ9mflnTP_J-NzFhr-AhosHoYN89P-r77KJYIKZSEQRMjFdxN4vZ08xW0xYG75hrvvPxYM1VyIG1d31J4nMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لاوروف: خطر رویارویی مستقیم ناتو و روسیه به‌سرعت می‌تواند هسته‌ای شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129081" target="_blank">📅 12:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129080">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل اعلام کرد که فرمانده یک گردان زرهی و سه سرباز دیگر در جنوب لبنان در اثر اصابت پهپاد حزب‌الله یا موشک ضدتانک به تانکشان در روستای کفر تبنیت کشته شدند.
🔴
انفجاری که منجر به کشته شدن هر چهار عضو خدمه شد، کمی پس از نیمه‌شب رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129080" target="_blank">📅 12:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129079">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کاتس درباره درگیری‌ها تو سوریه و حزب‌الله : ما اونجا داریم می‌جنگیم
🔴
ما به جولانی نیازی نداریم
🔴
جولانی، همون تروریست کت‌وشلواری، لازم نیست بیاد و به ما کمک کنه
🔴
ما سوریه رو خوب می‌شناسیم اون قرار نیست تو لبنان به ما کمک کنه
🔴
بهتره تو سوریه بمونه، تو…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/129079" target="_blank">📅 12:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129078">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری / هم اکنون منابع لبنانی می‌گویند:
ستون‌های زرهی اسرائیلی در حال پیشروی به سمت نبطیه، پایتخت حزب‌الله در جنوب لبنان هستند و درگیری‌ها سنگینی گزارش می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129078" target="_blank">📅 12:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129077">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
شهباز شریف: از طرف ملت پاکستان در مراسم تشییع رهبر سابق ایران شرکت خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129077" target="_blank">📅 12:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129076">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129076" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129075">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
حرکت گسترده مهاجرت از شهرستان‌های صور و بنت جبیل به سمت صیدا و بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129075" target="_blank">📅 12:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129074">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=DfDrSudnNgbGGpQfSKB6q7ASOvgMUhGom7A2t0Fgc9epmANDAqUOcmLYXT_xMNyMnoj63w_wsa0_bQtkX4CdDoXzWOpmxS5mRceYB9GvimcN2KfNH7o-uzOamfJr9HnDHp-I72PAjvRNYKoI-vBdLN0DjuwzZajgpODNLbZczerQJsIZh1SRvDgFEmQQZxDnzUT3W_5qptJ68TQRKrJsMEB0uPs1TgWTRchp2uxzyo2AChz-y7Ua78Eu9C0_nSCf6FMNiIBE8ZtZoamvrevlkQySIvBsBgSLWfqZ9cRrJtTTvOipGeTAC9hEjoqPNb2s22cgMC0qTVn0aGYLoeVANg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=DfDrSudnNgbGGpQfSKB6q7ASOvgMUhGom7A2t0Fgc9epmANDAqUOcmLYXT_xMNyMnoj63w_wsa0_bQtkX4CdDoXzWOpmxS5mRceYB9GvimcN2KfNH7o-uzOamfJr9HnDHp-I72PAjvRNYKoI-vBdLN0DjuwzZajgpODNLbZczerQJsIZh1SRvDgFEmQQZxDnzUT3W_5qptJ68TQRKrJsMEB0uPs1TgWTRchp2uxzyo2AChz-y7Ua78Eu9C0_nSCf6FMNiIBE8ZtZoamvrevlkQySIvBsBgSLWfqZ9cRrJtTTvOipGeTAC9hEjoqPNb2s22cgMC0qTVn0aGYLoeVANg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاتز وزیر دفاع اسرائیل: هیچ کس نمی تواند به ما بگوید چه کار کنیم و ما آن را ثابت کرده ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129074" target="_blank">📅 11:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129073">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری / معاریو: مقامات اسرائیلی نگرانند که اختلاف ترامپ و نتانیاهو از سطح حرف فراتر رفته و به اقدامات ملموسی مانند تأخیر در ارسال سلاح، محدودیت در کمک‌های نظامی و حتی گام‌هایی شبیه به تحریم تسلیحاتی تبدیل شود.
🔴
اسرائیل معتقد است که فشار ایالات متحده برای خروج از جنوب لبنان و حرمون سوریه تشدید خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129073" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129072">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌گو با اکسیوس دربارهٔ ایران:
🔴
«تنها راهی که می‌توانم سخت‌گیرانه‌تر عمل کنم این است که دو یا سه هفتهٔ دیگر آنجا بمانم و همچنان به شدت هرچه تمام‌تر آنها را بمباران کنم، درست است؟
🔴
اما آن کار چه نتیجه‌ای برای ما دارد؟ تنگهٔ هرمز باز نخواهد بود. ماه‌ها نفت نخواهیم داشت. تا وقتی که بمب می‌ریزی، آن تنگه به طور خودکار بسته می‌شود.
🔴
این از آن دست مسائلی است که می‌تواند باعث یک رکود جهانی شود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129072" target="_blank">📅 11:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129071">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
بعد از اینکه سوئیس اعلام کرد مذاکرات امروز آمریکا و ایران لغو شده؛ قیمت دلار مجددا از ۱۵۳ هزار تومن به ۱۶۲ هزار تومن رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129071" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129070">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل اعلام کرد که از زمان توافق آتش‌بس آوریل گذشته، ۲۳ سرباز اسرائیلی در لبنان کشته شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129070" target="_blank">📅 11:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129069">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
طالبان مدعی شد که شب گذشته حملات هوایی را در داخل استان‌های بلوچستان و خیبر پختونخوا پاکستان انجام داده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129069" target="_blank">📅 11:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129068">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huMYq87wZNf14_soFTr-srvo1jqy2z0IDSsdop03dFGdheLs3ojHisyvF4VcFyXj8pB9pu75wPkhGffaLawYfpNbuWPIxNhTrNf_g4dSYRO3JpYj-ruuOUFHrVPSK5_KB-YzBRVF4_v98wwwcfc59JGGeq2e1vFmKDdyGyTU77C6quj_qH5A4IgNN71em3FR428cJmjmuHTUl3rSB9DMIK7IrQRZO21kA4RNBdnXvsKh8VuRtuhGyq5QGbuAPqEwibepqrt5RzOpj6IA-8cKcyBjEMqbMfZfpdgz2Z_QBwzGDe97s7SNoWpFsJDrX9Wh6a7yADLkUOeVfqd8WBZzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت به ۸۰ دلار در هر بشکه افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129068" target="_blank">📅 11:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129067">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رویترز: سپاه پاسداران انقلاب اسلامی سلول‌های مخفی در عراق ایجاد کرده است تا حملات پهپادی علیه کویت، عربستان سعودی و امارات متحده عربی انجام دهد.این سلول‌ها که از جنگجویان شیعه نخبه عراقی تشکیل شده‌اند و مستقیماً به سپاه پاسداران گزارش می‌دهند، بین آوریل و مه حداقل هفت حمله پهپادی از جنوب عراق انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129067" target="_blank">📅 11:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129066">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2pCrAZ8fEstpdrwlrUIW4qiaYEVGRTP-F0d2QNdA355RulXGC9Fb0dKahVh59V1GZK8mVDBdtcw__XOkWz3eAFcGcZvqLYBDiLqDz-Oia-6AUv-JmEnePLN_-NcNDkOBYkVg8cQQfmUR4pWFR5wDvaFcdviKF8p0rqvsKLEF16OcZLNDwblISAXQ4-hxJxQdFboJGWeWpWY2BnWPN5u0f7no7iGm4uNmGNh6hZpSuIxMMFa_U5Jyndc3-d2chMJZJiZqX1mNvA_-7AS0v0JsmB3zLF0w2PjNW06wEKA2Tq2uNb_ztIEwFzd7XPQ_AMlxrQtagBZbP9FV6hLiyCT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل بن-گویر: برای هر اشک مادر اسرائیلی، هزار مادر لبنانی باید گریه کنند. تمام لبنان باید بسوزد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129066" target="_blank">📅 11:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129065">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTMwI9gbJh-5KnQBGiu2XPFR4H8tTg6c2vVJyf7GCBGcjaUIdZ0UI-BukyAsigCTMbx-ec27gSRPYu5L05lhRj-3oilvlAZkQAYfN5FEBX5CkbT1rErJlSj8wGYp9b5rBS6r_EOdMEZdow3qCQuIKq2dwXacUj4duTxXRYlfqwO5ocBZzNR1Y4FApe89Vqeob-d09p4VOnTdvE0-Iq9CBXSwo78DIDOHz1OaAxM8Nc7Ufbn871W7RLd9JCDF-9rnyvzXVGK11r35NqadM_qMzG0Y9GXJBdcIRKXGx7CZTWOczwJ2GpShykw9zegX_J7Sll09bHLAR9yIcIeDplCeIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسسه HFI: ارزیابی اولیه نشان می‌دهد؛ سپاه پاسداران انقلاب اسلامی تردد کشتی‌ها را به ۳۰ تا ۴۰ فروند در روز محدود خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129065" target="_blank">📅 11:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129064">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3affd3cf08.mp4?token=PjKbglpjw3shjghbM1je1AOa1Qdm3XTqRVdxapv5dp_3v8mTdQHnyVxtjjndLDUjzpr-Q29AmUi2hNZnk7OlGSNNwhVRm37Uhh6RYa_CW51O_-dwnYN8hankqX1dTQ-KzKHA5fG7InU6vUfh-inGEJiaNlPC9PfUdP0-5RloV6v-P_daD1ODZ3CDc_gP1ZA9vUs9eGkf2MvonQOX6hYeViviCATy43rNacRUETW87OOtDRGyczCM_cQLy8Am6K5w5UTtj9YqF6WR4V1z4WWX0N487Jszx9c44-sdvicev2XpR9FqijxPAb6SlVQlpPzWxj8NuVp_A_QreQL6_QFBdJP4KdMVtnUwUC0gmys1sC501wgmN_3XEl1dDZrqn_OfsFt5GrwEGEYFoMtxFCc44KNEEKT3Q1u2ZqD1awHiauliXdKdyUzu563OzJ_wOWyqL8n3gZiD8ySMW0tyGm8oQ37NZApNDjmoT9s-EBac4k2xJ2EwB6Sh1W7k2o1D34sddV2pn0Q0jROco5x17dD9b39369FqQCY6lDv8p3v3s6fZ6xS6xVTQRcmD2utEJWhj7U2BovkOTLsn6p5Fddt9Msv4ueDoBn0esCKmbli3EGOU8TSWZdsAMlXwmbjszFIuFMLaX69l6ngJrBuHJDXt_ODl-OOnuTjdf2dKlyFNurM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3affd3cf08.mp4?token=PjKbglpjw3shjghbM1je1AOa1Qdm3XTqRVdxapv5dp_3v8mTdQHnyVxtjjndLDUjzpr-Q29AmUi2hNZnk7OlGSNNwhVRm37Uhh6RYa_CW51O_-dwnYN8hankqX1dTQ-KzKHA5fG7InU6vUfh-inGEJiaNlPC9PfUdP0-5RloV6v-P_daD1ODZ3CDc_gP1ZA9vUs9eGkf2MvonQOX6hYeViviCATy43rNacRUETW87OOtDRGyczCM_cQLy8Am6K5w5UTtj9YqF6WR4V1z4WWX0N487Jszx9c44-sdvicev2XpR9FqijxPAb6SlVQlpPzWxj8NuVp_A_QreQL6_QFBdJP4KdMVtnUwUC0gmys1sC501wgmN_3XEl1dDZrqn_OfsFt5GrwEGEYFoMtxFCc44KNEEKT3Q1u2ZqD1awHiauliXdKdyUzu563OzJ_wOWyqL8n3gZiD8ySMW0tyGm8oQ37NZApNDjmoT9s-EBac4k2xJ2EwB6Sh1W7k2o1D34sddV2pn0Q0jROco5x17dD9b39369FqQCY6lDv8p3v3s6fZ6xS6xVTQRcmD2utEJWhj7U2BovkOTLsn6p5Fddt9Msv4ueDoBn0esCKmbli3EGOU8TSWZdsAMlXwmbjszFIuFMLaX69l6ngJrBuHJDXt_ODl-OOnuTjdf2dKlyFNurM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد دانشگاه تهران: یک لیوان آب ۱۵ هزار تومان است یک لیتر بنزین ۳ هزار تومان!
🔴
نیاز به مدیرانی داریم که جسارت تصمیم‌گیری داشته باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129064" target="_blank">📅 11:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129063">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
العربیه: حملات اسرائیل به جنوب لبنان شب گذشته به طرز چشمگیری تشدید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129063" target="_blank">📅 11:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129062">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سوئیس رسما اعلام کرد: مذاکرات ایران و آمریکا برگزار نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129062" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129061">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ونس، معاون ترامپ: ایرانی‌ها مثل یک کشور عادی مذاکره می‌کنند؛ آنها با ما به گونه‌ای صحبت می‌کنند که فکر نمی‌کنم از نظر دیپلماتیک با ایران در مدت بسیار طولانی، شاید هرگز، چنین اتفاقی افتاده باشد
🔴
احتمالا افرادی در اسرائیل هستند که دوست دارند ایران را به لیبی تبدیل کنند، یعنی اساساً یک «دولت فرومانده» با ۹۰ میلیون نفر جمعیت؛ اما تبدیل ایران به لیبی برای ایالات متحدهٔ آمریکا قطعا خوب نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129061" target="_blank">📅 10:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129060">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ارتش اسرائیل مواضعی را در مناطق «حبوش»، «تول» و ارتفاعات «الجبور» در جنوب لبنان بمباران کرد. آمار رسمی دولت لبنان نشان می‌دهد شمار کشته‌شدگان حملات شب گذشته اسرائیل به فرمانداری النبطیه به 16 نفر رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129060" target="_blank">📅 10:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129052">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cd9xwl72yb6W7c02TwfC-y2PxCRqISeyIZ_fskQhj6R4ixQESDopJmOmTU2hd2vwZCnQUik15Clmx95Ts0w3ymg0ntSlOgqiPkAGNoyQ30wrbLiQIMMJ0XNKWfv99oaI2vuS-Z5PWzl4X2n1aGFmaRr9Ivbmf-IKwTavmaDzUydGQ1AbHdWlLo0SUpeehiitJAaxQDDEsE5Uc8ohgQ2jT43rVuGQd3qkkuCT19k0tkP-LEndVuY3XFCyoiJUGY0NnAqaEmV-MRyWo4hTn89KQ2c6JFbqlBWRLDp4lUP8veoDjpvVUAeMSQrWkBU4iOf_m3CPG1o-0mamQ_RmrfXz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZERtOxFQVgYGO0WNJdyCsVmcaUfi_vcCU4CJ2LRFGMdZeOM3V4CbD0RrqQmuFoQu_QL6AIe2Sn7dCZ4jgFS5Cm4eTYHq5cfDDB07m44roWpVZPscRPbLC115jUazMZPefCTJFXgcuWgUwrFv4vVqt8g28EzTKqLZ5Su9IYQWk5hq8__aoCT8X6UydKlUMsX3N21OxYFuLxbWOkSigHQuaYV7C0-cuj1g8MRVBe7x8y4PyMY4vBJtG3IIJiv2Dyr6IkU4qVfuErRjlOiBkKNAmL7Z_Sb63B0KKAnMmpYj2L0c9p7Pv9hIHn6nnBlGWIuUSN_uYT3xpjAQBDtiWzwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYBYMcvz3R-FHdt6gCKmp_9_uSfhElhN_BxB_uq30FOaLTlp-ykkLugRjDoBoMwicQSsIaVp1Gt8MSlYwaroH7ksdQeB1ImTHoOGmYK9Rm-4k3fyrQof1pt13z8Z4Hs4Bik_kUGODuAomAgq3RXsrGEkvAdvlTTcbetXj81kMwvVbnq9fpBMTvPm-j0fOHD3IBHzjOj3jTgusBVZZnTkoNH9eBbZFSsYevneNId-yd8sFGtJNqO1TPcvYgbNgt1yiQtx97dR3mWRxP140n7YEd39B0QDdBTw-nF6D7TKa6RaJUjR_BGsdnFTn8lYNiq55ewGOefBswi4beL7F6dgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vs9nMUTQbZbbBBM7H3LQt77OqloDx879rHCpsxNQQIVXq0j-VJN4FyCwkEf80xKlUzqf3slzqKm9pmTPhiMMBD4lDKe67CwtRd0Ix33qBVfQmybM_UJ6PK5hi-NmVTomdiIFGDOr5rwjILPPYkSc87wr__bZNYQZsFiygcRpxdcpIvRuZKyLnNqjFh0siL81e1lWDEYPag5UXTH_p8lE76ytxLKDRvH8aqOq2kmdTGZHZZ5bXw8VZU_6ce8ZfIEYjL3hLiYS4A1Zk3nBvkhmZ5rGzJyZFchAOFQti1JiVzkTU6vMytEtBGY8N4YIcg1cmNlimzGwfhI7BcT3r9ZbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/piHzzR2xF6Qw-XUcb4ES8czFs4lZoIkpORQ9pZJDrQ8suR23xxB_sjpFwLac2IXP-dgu5wuvmhqGmB-VqgXe3ajj3e2rYUVS4-f6rIItCR03K783Iu2uxw-myqHslG1PTQWLcIfjWf2YEUNwuiw7Xo26HP0UteV8L_1e-kyFpbrk9c_gxknN51NxoXQIu1OKSMFOuhstw0cIk-0Bf2jPaco0czsmpdg1tcHipctfpzTWI43BuNceVNGbmonniQCzSwrWLBjqAJvn8dso8UFn8QNJ0-695WJ8ISD1VxzsI-1S3CuLV4v013nS4W65B399ctWDTfKeCBOxzcJcddb2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8qRYvdKOPUe4tZ5-RAp--o9NgElEIpcRQZ93xQpr_Q7wrthOCOuGQtE4Mnq06-xNTuWQFEov9S9iBfm3scsPgSyVtHKw_XBZS-_kIafO0d9EHGwiO1aRFXXnoPYJ2mQHy7Z396ldbWiKwkaZjDyxPWR9bmBhDosNmub3Tkn5BWA7Qlg4gACr3Kgt8YmGYR-Ct7i1eoJBbFkiau2lqDQz4HibgB2H9gF59st8_NOmOuOkoN_OPxBx9sFqc8l1nA5JpTWEUXfZow4lTq1i5VPgi1aAWoa7x6t7k8lS-nLtAbftAsdlVn-W0R8gThrelhXsxm2dhAGI1Nv-uBkSXiczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vE_UWanA8v0Jn-5cbdDn1DdqyXHqVheBe7KRY5XH7bvDq5LN4hQhdEv6U3C8TewDMxn8_k3dX98ZH0ahi6g1QAtmb9TIjhQQWa3ffxLAUoaoaX2zcYcgLvTgEazLLhvx4ep-dHDk_RZF3yXjyTwJWdWa-KYX8bf6xGFS-Vt90wzUlN-U0uKbsi5VaHuQG4SzSQk2XW_VmTEkMEDQUVfhaaNaYPSn6_g2OHJHKVHvObUNoFqG4E9mBX-ot3tsaAfnZ9n2I8uMFBJ3ZKEf6aS0dGK9TGa1Lb_BSNXUzXZTfqUk1f0LS2bM921Hd8CmBKZlBhlrbItECVvyrbvx1XabMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2WBSw6QLx0DulLK6Z6J1VW051O4MRo8C0QhTyy1N_fXv_cNTPFqNC879UVt2WRKsjkiggGGmmDqUPwu_T_-bWp7gqqa8HuZlUmY6_4wf6Qb3sfuSiW0JvRaEE10yyyAENKLiFod5U2v07yDQpC9MLdFMiaR2DLWDWqPWaCQn-rnCpHOFLe1fptrSbTjR4m6ofB6nZqG-ljymM71uROf1q7J0byRe0rn4KLomNUjcZL0NCVng88Wm66M-3bxg3X7H0V1jhB7FA1N7vmeXNbUi4h0hSBNqk8AG8zDEMYDrjhb1HgfmnQtowfSVTqkanT13FU9fKrjKrNEuJezuhTrgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی متعدد اسرائیل به نقاط مختلف در جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129052" target="_blank">📅 10:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
یک رسانه آمریکایی: ونس سفر به سوئیس را به دلیل حوادث لبنان لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129051" target="_blank">📅 10:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwa3h_HkwblxGzATxKzQs47rFosX8tWffkFMX8HrM3RvZ5J1IAhw6sc5yxfwEzzZZuvQPeDtHz3B27f6OO8HujlRpBPBFHsg6m2CDh73Q7J3rK0z_HFWIqAv3pr6X1VzyWngiyZiIpvUzNyA16GMWzztHdF6dAWgbrR0PE_36ots-_9pfBNDCtxY5G2zfApk4edFDpChXEiKKxYiwPN_OyBmVdCEQBCGKDBzynxwXaE9iblChrzBLlUVEH2S5Z9QAeX6R9vWD9zfRQCy7t74ZCdpD8kTV5yUjA_Vg8kaux4GrAd2PgZO00-qQU3wi1HuLNn90fVQjJ4WR0fvO6UHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش ۵ هزار تومانی تتر با خبر لغو مذاکرات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129050" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63aa3bf462.mp4?token=kJXkqXCgdySgii9c-HrZ2mZslLrj17fntJrEMPXkTBYrZYCKvjuCDIhu6UMFTt7fDJqxlBIYxynKsBeyt_W8kTCiUUTXccmv0sY9rC56Z8ck8mNVlCmcX8Zaj1TOoC_9T3zRrBpXDtEL3q_HpteIKIf9GLx6PzsvyPdmiZ0XpSOYmkJ98zw2ciECIIm0_7j6n4Afmyq4PkNkvMQGwwvCY-6k4zOzwu_JE0vz8zPAE2uJ-IzAV5Tq752FrS5UmC3s7d7cFl5SjcIMWCoX4z_4FFIOz_frOJj11jGSwuMDlvmFg8DAoicWdmRuZGXfmTCvZcWUt523FfJjTgmHI3tKCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63aa3bf462.mp4?token=kJXkqXCgdySgii9c-HrZ2mZslLrj17fntJrEMPXkTBYrZYCKvjuCDIhu6UMFTt7fDJqxlBIYxynKsBeyt_W8kTCiUUTXccmv0sY9rC56Z8ck8mNVlCmcX8Zaj1TOoC_9T3zRrBpXDtEL3q_HpteIKIf9GLx6PzsvyPdmiZ0XpSOYmkJ98zw2ciECIIm0_7j6n4Afmyq4PkNkvMQGwwvCY-6k4zOzwu_JE0vz8zPAE2uJ-IzAV5Tq752FrS5UmC3s7d7cFl5SjcIMWCoX4z_4FFIOz_frOJj11jGSwuMDlvmFg8DAoicWdmRuZGXfmTCvZcWUt523FfJjTgmHI3tKCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت خوب سد کرج ۲۸ خرداد ۱۴۰۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129049" target="_blank">📅 10:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3578fa102b.mp4?token=cKtt1VWas50SKR1ELTCmmbBunaTfZDoVgHZaYhlashdTvKQjCesyJvqtAGL6lT-5Y0eQ3P7iI-9GtuWeMtcDaHVjWyJCu8iCPUQFUrQdqdjCGBpLM36PQdO8gQXbmGrB4otIlohDlnbMgZhpVfd3Cpjl5GdbFsyi0Ckm9vyH66EtbC0zGVmSeJ5SCLFmdYBKumM6tIKOJQMK_u-K0i9BOFi6HUCXcrS2sWFCEVEYm7CR7-DYYtPm4CyPqsYlbDUmXUNwOvS1ojuJSAvcR3hV_tk1ycwcNlJwEWYKOXdx9mBZQOA29e1Zxe8uER0MqB4h7_CqtrPAysgcRKzJb2L9IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3578fa102b.mp4?token=cKtt1VWas50SKR1ELTCmmbBunaTfZDoVgHZaYhlashdTvKQjCesyJvqtAGL6lT-5Y0eQ3P7iI-9GtuWeMtcDaHVjWyJCu8iCPUQFUrQdqdjCGBpLM36PQdO8gQXbmGrB4otIlohDlnbMgZhpVfd3Cpjl5GdbFsyi0Ckm9vyH66EtbC0zGVmSeJ5SCLFmdYBKumM6tIKOJQMK_u-K0i9BOFi6HUCXcrS2sWFCEVEYm7CR7-DYYtPm4CyPqsYlbDUmXUNwOvS1ojuJSAvcR3hV_tk1ycwcNlJwEWYKOXdx9mBZQOA29e1Zxe8uER0MqB4h7_CqtrPAysgcRKzJb2L9IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لغو تحریم نفت ایران به نفع آمریکاست چون چین پول بیشتری می‌پردازد / برنی مورنو، سناتور آمریکایی:"ما اکنون به آنها اجازه می‌دهیم که نفت خود را بفروشند. این چه فایده‌ای دارد؟ این به نفع آمریکایی‌ها خواهد بود. این باعث کاهش قیمت نفت می‌شود.
🔴
و چین را مجبور به پرداخت هزینه بیشتر برای نفت می‌کند! و همچنین متوجه می‌شود چه کسانی نفت چین را می‌خرند. بنابراین ما را در موقعیت عالی، یک مذاکره عالی قرار می‌دهد و در نهایت، من به رئیس جمهور ترامپ اعتماد دارم که تصمیمات درست را می‌گیرد."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129048" target="_blank">📅 10:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر خارجه فرانسه: آمریکا باید بر اسرائیل فشار بیاورد تا حملات خود به لبنان را متوقف کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129047" target="_blank">📅 10:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ارتش اسرائیل: شب گذشته شاهد درگیری‌های دشوار و پیچیده‌ای با حزب‌الله در جنوب لبنان بودیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129046" target="_blank">📅 10:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ارتش اسرائیل تائید کرد: چهار سربازش دیشب در درگیری‌های جنوب لبنان کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129045" target="_blank">📅 10:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXwilRD4XNHug8wmccw_htbM_zDXReng1lf-54XBKwloR0QRo74KWwCs6HJ_4E0E8FFKnJfFP17g6Dyl1C1PjujYgMomV4zjWmHd4zX3_vLU8kBXqoUUPQ3ET_mo-BZGjUGZbDjwIYSsOjspGk29HUTGagElcsAarZt7LK_0Qwo7J-PtvnpdCyLdaKHzLV2wos_H6HmLIopfAs18NymHd_mmOkGIXVjuEdnI0kHKXKTpleJsk6gHGfTmSjOtgeR6DHrdh5nK0C1wOz6xNpX3P9FSXDgqC3yq-lUzTXXBu8_I9kXzSPZWZ2gooKBxZntM_FJp5zRP-g90PmJ_eBGVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در پی حملات هوایی شب گذشته اسرائیل به منطقه النبطیه در جنوب لبنان، 16 نفر کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129044" target="_blank">📅 10:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۴ ریشتر در عمق ۸ کیلومتری زمین، صبح امروز اشتریان لرستان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129043" target="_blank">📅 10:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbnzFq8vXptpqBt5dUohxO6KGZ07FjdmKZ7yI9Mvs9rv6V1-g_lN3FP0RngA0mMX3qH5_Aehw6-fxBicGrzztLBimDlx4pNfwcu3ndi7oCrcuVFK1Wby2rJsazxOx6ZJPoPHuxhpAhH_w6TteFmtaYxFT5FOClTGi8AISurNEPPEDrwXAwVGGLB8AegqLJCvAcuA6Z0d8hD9FM_bXx2a_gnoLd6Y-SlO0mQTXPAIbfD4nIbz6rrDfi4FIfDof8EIIP6FsyswjGsh82oXS15Uy8oz5wdY2EuiN-bSSf1oDSABNfwS0_TPYwwOi6eay3bAORL98nwVSm_8UDpz06TShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دموکرات‌ها در یک چیز از جمهوری‌خواهان بهترند - تقلب. آمریکا را دوباره بزرگ کنید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129042" target="_blank">📅 10:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: حزب‌الله باید خلع سلاح شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129041" target="_blank">📅 10:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پاکستان تردد تجار از مرز زمینی‌ به ایران را از سر گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129040" target="_blank">📅 09:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رهبر اکثریت سنا: توافق با ایران گامی در مسیر درست است
🔴
مشوق‌های مالی برای ایران به اقداماتی وابسته هستند که تهران باید در آینده انجام دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129039" target="_blank">📅 09:39 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
