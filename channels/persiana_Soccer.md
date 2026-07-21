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
<img src="https://cdn4.telesco.pe/file/toKjM-XBPhDFdEauepOrDFZtFiRmSSKY1Ia73S-DVUMkT8h6XVwtNbqIREdD9ppRQZ3SPvv30rj0u5TK7xx13gX5Ew3ksiYYYoxUIS8FiPZK56nOLcSzDIxBQq1eYmZYPpGk0PrERePBGh2US24sunf28O4B_QfVoNmDLgEOnjFm9WDCwl8YACgjInKkX3GIOJGBs6vdHzl8gTtgZCjKuS-Y0lKPOrqT2BbGvNbT_0IZbe8fzmOsoSw08enfUGpE6GdNhr6Ju1DJibp286LdYws3igD4LfQq8B1pdm0flYe4C4lkp20SsT3fdRlFZLKFvU7jjUBjCS7NbV1mG37SZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 19:46:29</div>
<hr>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRAmecfDKlXPuYVlDIoU8MbdFLenMJyOr5AK1FQtCDHFtD9JxhSFOCUV71rsCbmQhQv25xv0z_X3odP7qmrG6LAa-bUEQe4-SBNlmI3ZxCbl7F29trIhyPNb5QHzYx-Cg0rKFseBJGh5W_pd13EQ0Olyboarj2tU5GB2Qkd_I4TCrb64ydmK8pJiStfgB8bbt-aLeOcJ3fKoXmSZZqME77lBx8b1urqv-SJwFCFxjwckIYj0Bf0rkeAzr4gmIvcqr3ebRYS1TUqfcNXDTD9wd0R51TGAH4oUgBDz3fzaEkx6K6evGnBi5J9bT8MXBPETibLCsMQA0XRbyp16i5zuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfa8C4ekVwGpgRLbqoE2z9XuNwn9hai3QNwSlzugT5E7lLb6BTWBHdlvDLq2iU7t-xoWmUg7trV2sNs5P239Q4b5l98aEPi1wq9hTGK2ADOpGa1KaKhcu5zF2ahvQgy7-uPu8Mfzva_see99eBQ48OvnoHYdaqIEber9gJRezP93Ag-lH9z8wJd04UqAA9bZXdBOJdCl6Dam_WS4rl0bNrkLjBAQQUCA2EtVrj5GMrlCKWjH1_-R13Y0E9fIhCtTC0EnfyoFXM-ZsUeQLvZAKs_xNnC0DU8YlNv2LHaSeSK7Yoo5UVv148XZF1ClzFb0uMmLna1cOjRsUE4ANuMaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=l5PumpUKU0DylDMWNFIiisj6iWCZfl1Nj3skaBkAncLVMj4RzYp2F71Gg2Dhn40XGK5JICir7nIb6NRzH94bQSwE1ZfYYdEbwgrcy17MHCvyrmJ4RGtQzNYQ8GB5QGSNdBZ1xiIpYrpNorbEoxR3oxmbksE-sNCY9J5Elo1NainGLCqdqGcYYHNyl3FBy2UwIZl9gcSZdeupiSiLUQN9TaUwrUgy_3W2lb2R-kv1LRbIwvcc3i8yUnqUBdQr_uWC0q1QpBfTmW2NnOorAKl5G59O1kjEIsyNFal5qGyCYIHNMCCky_PIoy_Ymqg_UHk_a3ownrXWccF2CpNNPPAM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=l5PumpUKU0DylDMWNFIiisj6iWCZfl1Nj3skaBkAncLVMj4RzYp2F71Gg2Dhn40XGK5JICir7nIb6NRzH94bQSwE1ZfYYdEbwgrcy17MHCvyrmJ4RGtQzNYQ8GB5QGSNdBZ1xiIpYrpNorbEoxR3oxmbksE-sNCY9J5Elo1NainGLCqdqGcYYHNyl3FBy2UwIZl9gcSZdeupiSiLUQN9TaUwrUgy_3W2lb2R-kv1LRbIwvcc3i8yUnqUBdQr_uWC0q1QpBfTmW2NnOorAKl5G59O1kjEIsyNFal5qGyCYIHNMCCky_PIoy_Ymqg_UHk_a3ownrXWccF2CpNNPPAM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip6eQHWHApF68Roh7AkoHgplyBJYIWaqGSonTjik--AjJD9wigrs_cvRqZsiRbUc7VS4jlx_iDaPikkZ_GSfxEWia9V5OXmK6S1qRGOBV03-K-jYVRCUfDNh_JlujjZ0m2Tg5NVHDTOu3KpG-_ZACwyFFb2DCrOaN1qIk9CZmaYD67_UoXk2ewfA1TCzYZI_6jd15BIyBpDc6q-wlGLnUSPSmkhk6-oEWGH5Tw67tU2xlYrOrpL5qgVaJCpQ1p5p2w1pZ0QgunzPADjBOnxdC8tqRAESN2dwuEOASzYxAg3C_Gwvo069pqwTFbUeklNkDJH7j1dN_6JOO9_nS-_J-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfPLzcoTbVk2O5Lvep4sRpeLRKmFh2mf_ie-CiPq25W-CmwLtv_aBw0WiXQXIpYMTHglTXalUGg4v-U4lxNXXWRtETo6_lOEa8WSkfJIKZExm43p96MfVMrKY4t-G_yrvy3gmcxbbDWEtLyRVKN72QlADLyAxn8L8RoW1JVWuQdOJF88cyvo2-HEiR5BW0A-o2Z1-qYjsEMGDDScr-ivIXbwqUWf8A7L227-o_4KgHQxVLiVl5AhxljWhMTblxI_Baj99V58gQf_Nu5lWYYdpn50cnuytE1wPl7K8aklvBBUBUvWjcZdkY20uzQ-0j0GoZwESJkW_gjwBwkmR8BBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIJnh1lGly2nQMFfaOoZkqCOG5OSLVmK5pgp8hvUr72ji4jO8RVS7wnnnHaAt5LQZ_FgcPja1FIlj24a8TW3u38hD6j6DarR9TFXOGypoGKFI1rWFuc4sDrG9HZKwmRhmAN_S2P5CsnnPVjA1mfyy1mo55084LY1uv4G3gDuswXTdzJTOs4kdhyz1kMakGSLi4RpayGHxcuBnSQdEJ0KTV7hra3ASZxcVK1jl378GNfgK_fJejOjFm16z_Jc5mAcARv9Bj8E67eTrK80bMNNLWMKAAiXp-Pu_1T4F6wlLUIACiJyXX6Xu4CTBuY8TNtwNT7izz0KHrsqidnRj6xYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=kijEBuHNudk34zpjHafUFJ21aJI9n5M2DSEBvfgyrmOF1pMd2BZYrAxXbNFNuLAJ2XqOhgyXdF9p1WDqWoe26yi91Jb7T1UsFtpIAZSjSzLUvm_i9fDXwzbp8xYNxHrN9CIdGyDe-8Y0JL4e-71NZYIbcMP8DBtnO_kr8EffUsKhNwKv5KUcI7_R3gfZFnmJRYjAjHgRE2af2GCUiG7Us-70dDkYm3XNiabIDNpLnv5DOhHI0YlM3RVuxZ_TQK9kiyGPnsY_4aEezwh_UgjnNogpuvy8pMRHoD8gu77C7dDNjh1fHu5vntYb9iNhjhDuCh-laDs17eokWD5tqFPEcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=kijEBuHNudk34zpjHafUFJ21aJI9n5M2DSEBvfgyrmOF1pMd2BZYrAxXbNFNuLAJ2XqOhgyXdF9p1WDqWoe26yi91Jb7T1UsFtpIAZSjSzLUvm_i9fDXwzbp8xYNxHrN9CIdGyDe-8Y0JL4e-71NZYIbcMP8DBtnO_kr8EffUsKhNwKv5KUcI7_R3gfZFnmJRYjAjHgRE2af2GCUiG7Us-70dDkYm3XNiabIDNpLnv5DOhHI0YlM3RVuxZ_TQK9kiyGPnsY_4aEezwh_UgjnNogpuvy8pMRHoD8gu77C7dDNjh1fHu5vntYb9iNhjhDuCh-laDs17eokWD5tqFPEcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haYJuQGzFUGCjn-7v8tSzDv4ah6EOn_xGs7iCaot8Kgm8oXyn27s3vYKmCC_WICDgJko_dt0KY9Rb8wl1J3gLCUpbHR-X_UJUYS7GcR3TTKQwMhMbSIeGDxiumm0Qp-kEFB5_bJSg8hhJsH_frQ3zwwC_HnEDWAinqYt0kYZVc9RMiptrR8RHHMfLxCahhDU8UcYRz-DGHZCgKW-5DR2D4cG2fddLDa-9Io_45L1V6K3Mv8yedS60Qlqi7AV20cWfTCe2C-J0W0jAdg4GJ0MzxNpTL2KW1LT9AFvlGsU96Bgukvs_QH_KumynI13SisHTBYaU4b_nVcXyTxpBj3QJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mcx-SrEfdcONkub2sZRI0vhuH57_oiHI4wV6JXi8qxKU66HjYjU2wKx2JLZCEh-9CWbyASUxWlPFcX7uj5RZucObs6BAQfd1Vd0BUicj0bZmAzt_HM_ETdiBzKCcdD7LM1jlJjc2lI1NSgW1bw3g1bmIPg7zOILf0IeubxQL6k_eKq1syf8w18a_RbesD-927aZrIY8glQs7N4ONki3kcDh-1M6QrLv7Vl1GLruh7NzXYxolZjSKQ6XFK0Pzmcaostr5qu1gU9HrPIsfejmrIwc7mTfiMIFoAH7PHXV5Miuhu1XvPMw2erBokH68zihwE3OAp5QbeAvFbAS-xfcsxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxFdImJ6BHSvbMqfEMuhtepnbHYRR9aYsA-sx1sWYOTOwuP0o8jWk9RMfk8zMaPnRm3KgCVy97oXZ2QJXcl30NVcSYClHCoLg_nAmTS7R-iPPMbhsmZtFqA-jpPzprmI94-Z2dbI9LTB1kDTTBCBzOaR8KAo8ZsqUTvXFNUbnV08t3qzL5ZZSYJ8O2aV5REkIYMD4-urnnKeDFJ7D8pVm3BEFHrts6Y_6CcERTa7_nwkHkLPkXM4X6NY0VGdXgaPchBWFywzYamQlX9ma9m68BvSurh2n19dgL89jnJFAqWuePyO0YV90agpm5fmsA582qsB86fD-4dkYEsBeiKK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keaqzuBCRk3rm51hC_ZkvZpYbrZvbQtSrCiI5K7phSvpKOKzgiBOPNdr2vnkP1BVeVo2ZhlLEg5jq877HRMVM6DVQO5IPzZMx9N9AoclI6pj5OlQlkMNTN8a3-x5cxkRF9iAn8yGUEWv0kIJFBDj7vTFjsZc6w4do_2u9Xj8S1Xk1_ArQd-vxe2FA0pay6FUIzB5OWkFagAPc8d8MmuABgfcHvmK-XKZjWwx_3E2gFf_qixenuRhqN7UgsAP3xyGDh8p5O16mt-9cVtQyKsjSt5-0gASqKWGvy1WLIGKT11Q5fW1UEhsFJ4niCOvJS0RNQcQ6aOYDnR-3StaoBPo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV8tnVDWoHBR9qW8VAENrC08hNM1RVcRripU6rpb7mVZ9GBNjADX1fR8un11hKi9-nC-4z3To3CYhEQjLbl_1a6TbC8cot8ah-B1O1F5YjJvlosJ-MTU0CtwKNPDSBuZUlcDn6HWvEtLj6HJCLcXJntcVkUzwZrr03qzJf0PeaI-7LfKEbR53Gc0PahKwPNWF74rA73mQKVErUfucUlkZubp36gHgAeOzMM7tbpUKal1I5B4nfnTv5f-CeP1tUzxYbp_6_kFSZFD1P3NXlBxtb1QrSiYjM17L8JVDECO6rFsDH3T0XqC4X6pt0EIb6ulX-qPz0WW_XxAlqBWTMeslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26226">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqA5-_1a2UUXEAqsbUKLdSDLOkvyiseDzqk_dXW6XA4eTfauHKVIY5Hqp5wEVqnvi9fT_9n3eu_Ail_d_rNKkLDGXCoPUPFawODGLWKaJZ1b9mIwul34Si3jDmGqPTJjLtHm7i6JZRhT86wQFCOeIY_WIS694v0nGf7CGpoBQXJnR4uZkNAoyJEYtGnT1RtCTS3VEE6HEQz2IMTC8PBF-fHcYOlA7BnzSXjt5Nr4nkrZDvgeBvL8w19dBz_zFQCcgl7lYUbX5nZ5hhEsgeSw3zmJHwx7616Fi_oKhjKYu7KgnJyGF-UslDCJXMH8yHh2Ar7rk7hhHLnpq7V6svh3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/26226" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgGRecqPvkEfSA2uARHdVgQCy3Zu6tTVom70i6jrON1DoOtChpxS4tJCC0V5v9KsoiexePBFsXAaK7_yhy0QuLjPpOUdGr2llPUWu3ic-OsvEW9e3mNUMJliYqC9Ac0pM4_mqdsPOC7xXpGqms3oWbENquwz9syStdoom1k7sl9cGJgre105TRG5UcQ1-pprMZrasfnOhN5FW8o9oJ9B-4Er4UvNji2y6_FCEtjFF8FwO2se3M0Iyf5Y0pmQRSWuGI8FYAVaNqbevAfQj8p0r1fe8KkjYxy940wiVrkq9z27NWH-zzHEpfrVfFz2D7iclqpblkUtsHwRSKXo-Csceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6Eerm4-BOZlhrUvDhEMXBp5De-FHtxjzsASfgxFb9t2Q42vZyES46yB71M2mnk6a6KEsdbiNs_yONekXTBFensFY3K-mPsRtUIqtkN236Pwh-uS5XEaNguGwhfD6IW-_lMaT_owUjbvhLFeWndZ5S97yAOM7j_1Fy7l34ltpPoZXl62ajfOI1EY9X2UZYmqM_3EJu8j4AEUsZLL2KIWo4yPWBajF1N_PRsxiNERM7T_oZNGTXxY8bQWQR27zPX-AVaKad8XLmuQTUQ5Bh8gWbofDbjw8jOGd7WGL9qZEB44Dg_44UJ8FuqzJl-_CTsR51JnnXPHIX1Up7fUakLEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afv1KEPeobz2-6_LwYbXHnUuB6kdjz4rGKzqOOUICG6VaTy6B0xXHA8stYDzqOfbFUyp9g5s5rZ3FKURJVTpKWZL6sWyDgveZvP9wL8nyoYbUG4FjCHrCunkC_Yvep-1jJj8Owpqo7SbfkWSZqonnHBf80SEq39aZlQWveNJWCSmAGE121y80irkWcMYkaFh3_qLEVnh1D4zjyNPLPPoNOuFXRMdmE9oWZAiqDf7euRSBH9MzLwUX01WgwcIbLDcf6mSK_OCdvbN-Zrhv-esKpu0ZR7mOSD4DoQjAAzF0wBZL51znoRfcebITH50g0Hj0jM0aknJYgkj_DliO5AboQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEH1oAVtARzS5gez9pVVM5qkk7NB670GOryxtG_Nii5bFfkpk4S4_HEcXEg9VsKN0T6DNXZuJgrcc6ErZR2Pw8BiGcqU40M5tyBMmV_mYEvJ_6PeZ0OwKDNBBonytDCUgRHKy8y2U-d9ByocAKlOlC_cdapH79mg5OhS1ybMVGLY-UspGTgyppzkTiq82iuuE7F8fvcgLuNhva85atypNJ7COVDZ4zchf2YmJM_IQCHg_-tBZX-rzv4_LO7zE8Te-ujG2ifrSl55mcyQWXaKaRSujZkCRC-N4NDL4LIdXCJKZym43wZ2I1NYbyoudfKtfE9cTNWvzXOBv7-f8DE1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HndLgVCLy5P_TjJAHm4xxjZaGF1D_Cn1RpjQWQ0gAOzs-lAJu0LYIukvWbRJwnJy4lx3LQM6Rn5Igx0KL3wzkh0D9qBuiAVDcgFnVRjuWBjdleT4rQWl06F5LAL0ZLfNvXr5svfPkBdMmv9jPEC4sQV6jX1WM_u0od2rFNetATE6BzzuX05xqI3z9zSUFzfRIf9t7kxandAiduL_vwHz6OrTasmRgQ4KQXkJu3IAMOdqAZJHJfhtoyGETG2F_36XxoDhac_uE4hDyGzO-u_glPcwqiW71WC4aJgbjU0mq2kIeMOpYZKCEA3ZqsJQEOWtUC7sU97IqU1geL3iEJvKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0BmT6gWhBnRVDVnAMLO0DAYSJR7jLThJW67978r-PCDl_FQASxYYwpe6-rSKrtE6MDUxsGBwUdAIF3HFa2MpzjowEe1YSW4Te3QqIyvyL0D88pi3rtJRNXp6W-VIQwzoRTMvU4bezZixBAQzOTZOcHMKPo23b0SfWpwxe3qvviZvI1_HSVxhU1kIkOpdKZcNJaTxmfhdbpFJiRkL-U1Tj_Y1gnrxgqjQtkHNsdfzJjc0H8xafcDXfn58H636TeoPajVsXNZgnLVyFWrIRm5wdzQNftMRTzHnaHkTnzOro6JqNJEhqKn74Ul0ddhlgnZi8xhJZiqRZpbHaQnyNwkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFmpKLhRCH-49FlAgbyfcMTAE15LgubTPEX7qQZUOIBuLTO6yInG687WWeZlteiKiSXy3JruLHnx42HyJQUmuXNRIbzorH3_3Tx_TI1k8gd6ZWY6RnvA-MS5AIVyUFiN4e2l9-Z8VFppN6aPvi37U5LWRzwGdLnp7QC-k2OuAGWjvrBpS4GJyCiFiXeO_KkOuxKs8bTcWpHiucDHWAEIOSeqgJRTZd0OUcYTM0kd1VVcFLj1mW3e1iQxj6_VH4Gke7B3o7glihr43UEWv-t1SlD_A0UZ6ev2SY6WE0TYxLEaSjxd6aEnJAHlNrTdkrFfMOVLYv3A1TjH27uMaU6wGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klYgDuWf4OusW5KzWZ0QBFSwiIU9Rx6BL9x3gYiBReF9Xzb3s0Xy8ybQVOqPrCWXpO7ccvlKPwOlpSd5X4JTNis9vWYjQ_h9cPQdAL4Gg5ltkOI3yZEZXTcvwIS9kbPgT9aDKXpX_JQEatxSTLDs6jcF0jaLg-BkDxO_pvQVKMEGVxi3QvH-yY5FPRUlrWxQ5M1xjOsjmHTKsl_SUDCq8h36SLtQ2RwWQ9q7R-ou-qGJhXFPwqm8aXtXZy2_EmF3og-o6P5TIdQ4oK3UxJ_QLNcevLuUhNMe3DuL6o3IYf-JgU6MR7rdAAYLVWNdbOGOpZQqd6Z24r-muNxp1v0uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scgutJYuS7zOAPOeEnaQDKJWxac0iD_fEcsiLyODiIdMMzLAPy0mPzTiFk3cQb9MhsiXNEZOygk8Og8dys8U1masWNNnCuNulJZOwhsdlr17nnXJh2NJIHK6Aaz-KDlAcA7K1o7IghXsIPvZZiUvYQV_onQ72pd1FJcklBMvWpHYP8MQSx2xzxeKtiFMdI8_iecCcoA3ajQ4GIkSVC4gmS7KDajy51gkXsh8NQySwQy5EFV6VyNyCGfjko-KvV3O5aXnxsiL3_qr2cZzRV36GmNtxZ9Ny88sk6M8iuPCOrGppu_8YvKWVTn1N-uDgsMPa03IqTvFlCVXGnXxQkqD_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbrkH1VgTZrO_Xa-cWJKXzkuMklCGp1LadUg0L90R7MeWZLx4B8OpkKTmU6jO7aJEVCTpdgp5o2BXwE5_XkHdiIwEkCa5_e2aNhV79KagmVwXXi-Mgqm0r2XzAFowjOLgqT0cvtYi68Mhr113jGU8S3THwmlSS7Tf2VzLKUdHZinuaAS2369Fx0MBWuEXDcqBOCX3KPLAb2F_KNdltt7umozBJURC76xxZVX7Q1xVJuR7V0EiYyn5RgC4-Sfswfrm8pingL2mVFMt80nrX44IlBVrPYWG33PLTBdjd4ZBlljEJ0hZiX3Wa72F0yo1UWAuTi-4AbtiVgnhw83mgoGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxvKLDD9aAe2lB9Z7NwHpEO8jgHzd_OvJ03hPN1oSSlYF0buYCnxTwq7DffZjmb5iCEtibYKppnbGDEkqaWqDqhT_m5yKwh_UexqcjzmC5Wql7mxEOoeCKC0pS0tIXnOtQ74MfaEB02IWFUaQtaQ25DCH4W6MPj3Q148O6EHm5sCBU3c9Q_ApsUeAQlWOluRHGgk5kx-posu1R7fJr9QW-XA4vi4WX1bHUaSrewlIK_m_LdG1k1vCtnfrNAY64Va5KaEMAn6YUgzcY22M1_CYaC58ShEbkrQ3vYk7V7LBOGd9SwuHvnWZDWtANmP3Z-G9_6PFxD6Bi8Zt-j4YlD6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKTHBmXZ1hPrFEOtzBQ-Qml9zRX_BMX_lic1uyvTfeLer8I7HsMlosXERJV1TMxlROypWVtKeEyN52y9UR0hEEtbVp7u2LeSoYxWjVkgZsqZQeI282Mr7L6UGOmQapMbtod6dnfsSE6sXQjek-hF-m_wzmqIBZS85c5U1Y-qeUF74sPPvodIKvvYHUtkX0EMkWgnWjxyEy7rKyq7HCR0Hvdz3uBwLJQJZIjH11wleqdF6qSg5S7ILs81dsqRsKDsjX2w-8ro-D5tOU4RvJwcAX4ijUFEZ6pt8EbYrJkzfipUJ208xbdau0VuexFxW4EWoNnLJnwfULolDEhPe-zrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jmr8SUKSZzD4C7jz96gTJH_SoQYp_umuCphZqfuaclyDfte6DAv9lnFE1pYJECsf7fU-Fh74jIS4EHegBEUgNaLO5m3bYHFY17jkxUjXwVCpMpFpr24Pzu8lQ6O7jK5Y9sBLxuBoz4y2AOx-PJUGvLTO2lv1RF1Eb8ygjIzEhHMFvInKHo4bmzaHJuBEvF-un9f9oe4HYCl4-og6Wp27tUVgofpZ1T11HUQINcP0H9u7CtZBPvuMSU1rg_QnOrtsubbJQgwjuxXBe4rRW4iD-nxODMlDgb43la_QQKM3iQJXBHmt-8wKx68uLwU5j8caN4QSQePDE5-LiQfS2Qt2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJCdgnAvmv71M89troUfZK8qfO9qcbrc-IutRU_lKDDF2iQ3T7yBfH_lk5KUzjRTonFnIU9zLDrGF-exX3s6nEcfQV_fsisZy_SFBym-6f2FNgLrT8D6IHzfIDASQdF987tTZHb7j9a0X9P55U1dGvTf-6e161OPSyYNQXxJWfc6hbi-oxD0rXIk4V7W-E_aK_sNAqNgXLK4-5QBgAAFQkefGD9WlKBbsTgZiWeYOWWYV3Z--jfGGpQJmQRJU8W5B19FZQH_bF0RLqeBm0UVu7gfKjaaxb1x_fGc5B-_fH2GqHZCPwD77S2EzXDkI56vTnlA--8dRW7pwd44OhEQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVfb-83ruLyvuJ-SVkGNsq5VIwkfaP9OwXkSmPeiDUm2xZNAbMQN819kP051juS8yUNwtIW7Ayy95tOf-YX4pQOg6ComrtPhtAaoIQrIYfih2W1lZPw79KFQnRPnY7RItY5k38n8qM-aZfR3GSzXWCUhE7SWHKcvdDg6nJr0UyQhvb3HEV_Jrp00PU8X74R938UVeaxvfOWVwwzAvw9eP8KeSy6iEJT_1mLG8gi4tp2N-fMdbUn1EXWKAuXAHTebO4Ouwjn_UXvZ3ffdYmSdqhpwyOOC-8BEyo2t8HZW67olxbCrVuUJrc9kUlrwuPt45ZORaCmlj9BKhWxifBLL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZzlTbMTZA2M10pK8f3BthNO1QnP07TaCK3qsgp0sVbKTbRqxL1odWvgPbWoL6t7qCj99grzgRvUWj4c45ipqsnpa29GVpTKq_rBHWmP0fmZjdwzBmFiHk1xZOT_JXGO_zBZV2Fypk1eMeHJcK3Aq_SIzvbZXdPCNGbOfaNiRcEgQxYGjSRWEtxul-MzYk2-gcObPmvRN1UWpTL7PxTjnrvk2SPT8Vx5fXq08B9Hrf8HsybAsOa7dITYzA8zHU3_zK3AlyQCB9AeaInWwtYlpxPYz2ghkSqjCutNiKcmv8LaHTqYjb8np-_ehMhFao7ZqdE-tRo1B43qkCO4ZO-itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSl5fW67J3sgzFsIcZz7SqqNbBP2M7OvfQ-0iaODasNstv_wgc3Ia-DvxO98Sdm4ZbMizoZi2nzjV9fc41jFeNo1991OLa6LgOpSyK7miJLf0wQUJkYPmfAoIf-OM2y57kev4lleEc2lcjAXxCTwo8Bkm5CjwE67PCZlmsMjFQbOBquMyPCL3bhvf1qHpPi_26qJODvMuZC7LkUmM51I-NYRrpkQEcTwkd7iPGTZTC1WGAI14oi5tLn_kJzyAX9ux-9-E6F8PyRrIG9SjaqkSWV0eiesoEMwBSe1qkx4jcwkz3h-3CPF5-YqNRGY7QI1MKpBIzQ1OHfIGbqo8lWDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq5NwEP_f4tg5TxCJFqBj_ddue0iQiEBKXigLaAzY5Sev9JKhfluUCYiYCbC905UCNBQn3IieSBFMx9emDePPqrg9IR1tWJv72b1tpHzm7C1kBERHiu6FYQZ2r5sBuaw98f0L-pB5dLxV6SxyqbMUCQjU7mOGHUQ1a_odZ46Dpa6u1dOAAsS5Sqy81CVI5LoCpuOHw7flFhjrXQfQvqf2yoA23QcCxdAaWfEDv9zgTPtyRT_AVfABhxcfo0251LAP8UGlhQS455_hMQWCJAjPt75CaBNVnZYhwwTfkdaj4QpL1TGZHzsw20QvRftr2fgGjSYVNolYKVPZLjU5G2T5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=jvsvA9tDCFX3MFZ5aRvQyr925uSYuK0zaxnKL96ZS92fhxIE7FCiY4UMI94hvpTrg8dPOBk0vF94obUARYEDMgxuKWPQv8J4wsjz19HmpndVlU_sfC-TLqV_Ioc5mOKbLX_LN8ZWhKkK_ARNsUNMY5ehNoo7gOwPg9j2-t-S8FiKeRRk6RvfD5PNryzRL9YgHe6dfzZ9FdHNYhFda7TfBZdwX7TxJjEgU0uPXKUiBd_ytMa4zp4tlEqC11QGhdn43jfxFd53KJbOJHUTlcePJLVSRQBOpsnLwfTdX6L_tO0bE3D9AK-m-8mtB1Hjwi_cQ_dBsEkWaepasZz89-95gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=jvsvA9tDCFX3MFZ5aRvQyr925uSYuK0zaxnKL96ZS92fhxIE7FCiY4UMI94hvpTrg8dPOBk0vF94obUARYEDMgxuKWPQv8J4wsjz19HmpndVlU_sfC-TLqV_Ioc5mOKbLX_LN8ZWhKkK_ARNsUNMY5ehNoo7gOwPg9j2-t-S8FiKeRRk6RvfD5PNryzRL9YgHe6dfzZ9FdHNYhFda7TfBZdwX7TxJjEgU0uPXKUiBd_ytMa4zp4tlEqC11QGhdn43jfxFd53KJbOJHUTlcePJLVSRQBOpsnLwfTdX6L_tO0bE3D9AK-m-8mtB1Hjwi_cQ_dBsEkWaepasZz89-95gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mar34L5ZORXaufR1tn8lIIPL0Mk5IfRHQdVPAXSggyGeFd-mVTuG68K2hkkS8iOfZeFlnkAJaHFtAQRDj9nnMCzENNifgwIu3saveGGjVZD1ZyLfD_dQ5L2sneOh52rbzzJhC--NDRtDH5HTVyUDshWTm-rrhXTUQtpis_kShVRDWuPwTE_a_-ODC_kwv0MzAxB2FCEFf_1UMsNsQpq1K-VNnD5j1YyfH-eLREKLGb7IooAHIAVSwnqe-M4_y2kL_-aDzOuNLPqbT1aPR3lEQmcilMBhQcxaviJrn575m2zKxbCKPOTEKKpaL5izPEBtloquw9JxwY0qVCLwx0Wf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRF7eSVAYubGR5w1U-oWhaMma-QMK5AiHFe2upmIdCnJuKfgbjJ34PsXY6MQKQyCLcndP2A3dEHTatOOPJy0zzDfRSEst_HwHeItK7hB8ds1SOlCFzQDteIu_sYMQadcI6FNnxdamsHSdHmq0nAJ4za3Wi7Ib2hu7LQ8CShtinL3hobFHUtVs3R8OVCFKG1zFKFdCdyi0enhEflWVAtk0GrRDSk3jaP9dp0uauIZ8ROQ_xCgMkbnHxUcfhYyWcaY0pxulntJY_L9kgwcXjxT_J1-7hLJr8yn-NleA3ATgVxjWVe4mRF-TUJ3aXcMyeDJJRD0UL69uokLDpkv-uZ72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jht8nLq_RcXzCut9ZBoTnEPrK7l3K4HIcbHeNEbGgHqx59IVyiqK1YwqvM_3x0G6KeavW2rjPpCv-Ayk7S2UOL_bmuBoWUhFjTo5_1Ay0zTz0AO2C0u-j4KPaCUHX1q7Meb9kotsPtNALr9RIXlabIJjzppNazcOSTSWy4ThfQdlpN4Jc1xhgyXfhe1Gs_F_rKEGr2tCAFCHRYzjTJjJ_ueYuk2in7__aI62gYQNbsJRQKLmTs9NPzu9AKW-VQ71Bf7NqG5ft747eZysHfolBJf4pwtF4u_v0ViLvZkp5Fs5IxkWA-L30xNA6gU3OrhalLoFNaaZytzU1MWAzSnX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=DEDJCwAPXMhAl_I9awy4orxoP0XwXMs-oABOVhi1cYap8nMjwWUZKAz-jLcSw5vUZWqMiVsBgbUq-NmT3Bd6OSeuMVQhwWoYlHUVAYxnq8CVOyjP_feDdS4GgxAWUQ5m8wPXNo0fGESvy3gZPt0bBClBHI0Y3lDy094vWp3HofPjq1WI1PI7zY3-s6xFUKheRqdvORnmO8ZF8xApYNHYHLzc3vEHha28H-8H6X7jx_zrFBsg0KRsmHmA_kfx2lA3Tu4KT9Ykm4j8dRp85qgcRuPSEuI9xHZyoz-KF03SdXtMjyTitj83w6NoqFvBi3tYoUqHgsJOKY8mLTam0QkYyUStuwE5CKfT0rUsAFn0azqTFmQ1aASVwambQFxQTuvdsQM37g9ClWQnATFEBkjegmqX3uwmHtZmDvf3Wgz_LJGG0sVUbh56bkQdoYwBpwkiJihGZkptjdp4X0O3X_gi_46swYytleR22D4ofkDypFdwcaCKLjmDGRRi98_UYPluX3FPlU93UXthfELt7dE9YBI_Fsf8pc4Xgjuh89-FqkmD2rVXz_8qdDgXyqPz2QEQLtywY802ewJTzR09olf2N2W2BkxtmrcTBbNn_1DJvc-ATDVjKIZPyuwiVcKz2LF4U4Xa3ILKBn3w4I0JTQM8RAbiyU2_XGNURPTG_H6n9s8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=DEDJCwAPXMhAl_I9awy4orxoP0XwXMs-oABOVhi1cYap8nMjwWUZKAz-jLcSw5vUZWqMiVsBgbUq-NmT3Bd6OSeuMVQhwWoYlHUVAYxnq8CVOyjP_feDdS4GgxAWUQ5m8wPXNo0fGESvy3gZPt0bBClBHI0Y3lDy094vWp3HofPjq1WI1PI7zY3-s6xFUKheRqdvORnmO8ZF8xApYNHYHLzc3vEHha28H-8H6X7jx_zrFBsg0KRsmHmA_kfx2lA3Tu4KT9Ykm4j8dRp85qgcRuPSEuI9xHZyoz-KF03SdXtMjyTitj83w6NoqFvBi3tYoUqHgsJOKY8mLTam0QkYyUStuwE5CKfT0rUsAFn0azqTFmQ1aASVwambQFxQTuvdsQM37g9ClWQnATFEBkjegmqX3uwmHtZmDvf3Wgz_LJGG0sVUbh56bkQdoYwBpwkiJihGZkptjdp4X0O3X_gi_46swYytleR22D4ofkDypFdwcaCKLjmDGRRi98_UYPluX3FPlU93UXthfELt7dE9YBI_Fsf8pc4Xgjuh89-FqkmD2rVXz_8qdDgXyqPz2QEQLtywY802ewJTzR09olf2N2W2BkxtmrcTBbNn_1DJvc-ATDVjKIZPyuwiVcKz2LF4U4Xa3ILKBn3w4I0JTQM8RAbiyU2_XGNURPTG_H6n9s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26197">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKU2tLFziWPQPDbyzWYfC1x_TVYCZ-SEq9LvGwjpyYficBpt8Zton6ns0UskOQc6uxHZIkEBj4w9oFRJfozJ5pOrkRnTaHRvwC1Irn0xIDCGPDJ1BmwatUixy8D94sV_9KnCGoIG7mHXYyHms2Kq4tQHAuW-_exoVfGHGJtVPBv88aiAlYyioIu1l7Xc5IMfZf_JJNWp23eGQsj-yVJwXgQ4XloX2IRdkddMlosrkEnYCtmqS89MSiNTovIZM77YTrPzIjfHQoR-MKnf5Q23fHT-lHv7O95AYz32qApPM59kDpzOKUcFwNB6WGU5evcG-9PqNzqRLDiMWSF4TYqcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r30
📩
@winro_io</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26197" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESLGO6g75P09C3Wl1XsX4fNGyMNqM0RfNEY3UPjWvVAs27bUpKB3AYZrHL-J1YeDZjLMQ8hdZ-oKT76u-ViHA7qKO3XH8ilyJn63pytOvsTi7PmHiaoyo7mg9HCzoQfc0AZgBPBgzOW9q9o4HNAZv1d0pru9hefMt3988BGn4r6ZAAFI_tm3pz6WMWSAR084i3-6k7hhLxHYLBbxYlgjtP5a2TvSjiPGthdAxNeDYm6JOJZCU5CNGYlIWAfK1Y5qvHOioogIVAHgchbWAMIdoUd6aZ0Fw7xDFIwqi7kwxyevthopeETQhmlB28hMOiUg2gJ7t6st2-xnIdj9Sy1Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnl9ymVkSXNfGTYR5mOVOLFT3oK4Iw7Pm8Pz_pa23Sh05bq7wNkne3VEcltpp4JakYGm-dsJDGeW5x-8CBHrLANEPpnvH7yL0FfEkoJsW8_tGe0MRBlpK7GOoL3nmXeRUrewWEhuY30bHk1hhVCN9vssc0oqJsxxTfi1koP601ccQYHeZWFLx6YSTneRW1YA_GumKT8kyZAXFPddePoo05BJeUtBgcASdyLVUUIHvhyDwZAOD0CQCMjrRnxSNRKGGMNaPwGjnCklAh0HVKoJazoK5fzvXcz54pG4EL6KFaUCBS6vEr_6smB64353qQN8kapjSvWyG9WLw7mQGGkuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=XZu2XudPaWg4jrxGnfPaqqzNzdiQFuzRXZPdlbzPO6RsSkUCEfmu_AG7ZIq89bXhE_xCqO2FdkOGwREUNc5RMTJAPdbMhDCiqL4SACUFjjy47c0iMiiT1fRl8AYRd5QXOzLnnMaDGm9jsiyMCXjrMXKag2PeSvAyz_3eaSpQILVwAaBij3Z9-MNVyxqIE2iJeIAaYszH8JxQtP-zUNrghh64PeTvACvlRYFUsboIharl8muNoXsHVV5dSOShWzlsJe30LzVhRGXQ5WEa0KxDXNDPvGGMHyezjK2Fz-020TgBc_qWoxCJqBaC12xVRWrqS_CdtPBZWqN43-mkkQ7ogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=XZu2XudPaWg4jrxGnfPaqqzNzdiQFuzRXZPdlbzPO6RsSkUCEfmu_AG7ZIq89bXhE_xCqO2FdkOGwREUNc5RMTJAPdbMhDCiqL4SACUFjjy47c0iMiiT1fRl8AYRd5QXOzLnnMaDGm9jsiyMCXjrMXKag2PeSvAyz_3eaSpQILVwAaBij3Z9-MNVyxqIE2iJeIAaYszH8JxQtP-zUNrghh64PeTvACvlRYFUsboIharl8muNoXsHVV5dSOShWzlsJe30LzVhRGXQ5WEa0KxDXNDPvGGMHyezjK2Fz-020TgBc_qWoxCJqBaC12xVRWrqS_CdtPBZWqN43-mkkQ7ogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=vR-9P2LRErQTgns3ktxtiAPfp-Jg-WgOfGcpwshwzXqd3IdCgIs0DQxGTRO5QiUYKrSlQ8nKIp3OB0w08LNO3TBsZSPcQumDZOtZj4e0HiF9eSLZWHVo1C3XNVSBBWdlYBb6elZimB2b6zDPcLXOVnbaxoMH9KiVU2szPO-66ED6r1AOHHvfFTOqmyQVTrSEyN1vFsz7Aqcck09B3gzNLozT0am1_8XHJumhKsliZoMCATmSEKJTbrbekGdq0B9nvmEx9MGuskXKZ-0Km8XkrdZBmpBsvu4qiYqHppGU9000h7GlCrJpMcC4zStAr4EABGgS187JrkluHg4AAI8Ewg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=vR-9P2LRErQTgns3ktxtiAPfp-Jg-WgOfGcpwshwzXqd3IdCgIs0DQxGTRO5QiUYKrSlQ8nKIp3OB0w08LNO3TBsZSPcQumDZOtZj4e0HiF9eSLZWHVo1C3XNVSBBWdlYBb6elZimB2b6zDPcLXOVnbaxoMH9KiVU2szPO-66ED6r1AOHHvfFTOqmyQVTrSEyN1vFsz7Aqcck09B3gzNLozT0am1_8XHJumhKsliZoMCATmSEKJTbrbekGdq0B9nvmEx9MGuskXKZ-0Km8XkrdZBmpBsvu4qiYqHppGU9000h7GlCrJpMcC4zStAr4EABGgS187JrkluHg4AAI8Ewg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVsgep2ywfT4v9S9sj6luoLyo13mo6KFi0K_Z-TCUnzg8oH1vJDbK2FJ3U41G5Xg2J0gRaDAnw7I6WJ9YOwVJOJYMTfkx2Jt9rLfB80QuH_R1QmrlvgsmhQ2mVVlcWtsyFrywmIGi3GKPUwHr1UYxI2NmtG5rnxyebPNgEF5cheWWqSCZxY0ljuK_532yqZ5kwah_T8d4h_7LQrsKQqMSD4q9fSC1LuhAKIAPvRQr7lqHCTIz-Vf-a1pIm1nB943EBRX4mpx7RzVKukKWpc261ylSrg0E6AwkHJ-yKLSYhZu1eHAUPhIEXdYYRUyJhPlu0iTWtqXH3D4uFFqTgsIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5ymtbkah9Lo2l5T6O-1DWOXZELtkIOF8XRsS02m-BpPTR0qDvCocEa18NadY34gMEJDz_OgEtxpvkKJwYfdOhQ_kZGhlR6X0OQaWHjM0mlog3fFvxsh_c2uK6I80nDa-5aHOmQ4jr7ZpNA97Wk4uTgwmM3KKgjFYEju43P2SyxF2xKrRwY4MIKlSQ655flxYRe8AK2AtP3o-GI5P6QkYXGTjKo5miYI0Y7qyDOyY4Ou4tj9wOHkuR2ZV1oKeuZo1g_D5XLdduma4D5nKVE-CsvhgLqpGssnVUuS9xqNt-t19Ahp_1wgN9sb3Z8znP-ki7EpwzqQAAcPL4uvx93O_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=bZD0DUyYAMEmkC4H8_aZ70RRYv7QYt9YmyZ3OrzK5aV_-UmvrwHHnnjv-_LrY-0bEomBGcId0XhYlNB31joiLXAcKGe7u4tBi_T2M7xalgGwLgtpy0XCvvkgS0tJBe3CDniA8t6V5Dv3YcPT5nqUYlHMgsSc5HMNxfZkyM0JaGwryXQz4klCiXRvbOPDcE07cXhy9ke8f6kE3qgYLzVV_MQ0aizTCxvOikZbpppDaxcwCO8tqogPnsV69PX3tsRWknowO2--oaw9OW1gBlmpBHEVcUD0rACm6kknKBgUhrxcLNump916cHw2CwZQa5dXYy2lEsvdE96zzW7u-kiWHUdqNUhxFyIa_BuDOe_JF-Wi6yaKrAFzFifabwuwvvAqlqoNgqfZS2X3MCPWGLn6p6XfA8F9Y0VAu-CoQ0lkz7W4XWhZwLEXIuEOjCu_Cz39lvOepGNQtJOIJx2DR57ZEWT1CYUxzq2bBZkjGpwnkHhrswQ_wvgkm9q7-s2XEL7tSD6kGzwChKuOFTpT0RwAXkWVXuYCHLSCVp-UA48_s19_k_qvVnxzFB_AGtl2S2V9fe_cOGZy-cqjQrS1h6mKEvO4lLGmUbyUl2f6mMHmDyjCfzfTqKRRJgO767WynaQWaMHFuKyVHAt4IeCoiwJ5ofFR8WCmnJBw2hiVDApJ0q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=bZD0DUyYAMEmkC4H8_aZ70RRYv7QYt9YmyZ3OrzK5aV_-UmvrwHHnnjv-_LrY-0bEomBGcId0XhYlNB31joiLXAcKGe7u4tBi_T2M7xalgGwLgtpy0XCvvkgS0tJBe3CDniA8t6V5Dv3YcPT5nqUYlHMgsSc5HMNxfZkyM0JaGwryXQz4klCiXRvbOPDcE07cXhy9ke8f6kE3qgYLzVV_MQ0aizTCxvOikZbpppDaxcwCO8tqogPnsV69PX3tsRWknowO2--oaw9OW1gBlmpBHEVcUD0rACm6kknKBgUhrxcLNump916cHw2CwZQa5dXYy2lEsvdE96zzW7u-kiWHUdqNUhxFyIa_BuDOe_JF-Wi6yaKrAFzFifabwuwvvAqlqoNgqfZS2X3MCPWGLn6p6XfA8F9Y0VAu-CoQ0lkz7W4XWhZwLEXIuEOjCu_Cz39lvOepGNQtJOIJx2DR57ZEWT1CYUxzq2bBZkjGpwnkHhrswQ_wvgkm9q7-s2XEL7tSD6kGzwChKuOFTpT0RwAXkWVXuYCHLSCVp-UA48_s19_k_qvVnxzFB_AGtl2S2V9fe_cOGZy-cqjQrS1h6mKEvO4lLGmUbyUl2f6mMHmDyjCfzfTqKRRJgO767WynaQWaMHFuKyVHAt4IeCoiwJ5ofFR8WCmnJBw2hiVDApJ0q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZGntM6fYV1ysDu2reQoLKUcVeOLCmTpyWDR6gA5RqrYBjjdARILJ-P34n25iFDytCzXmG_bIxbT9FLnZOxjaySdn-iVEans6nkb-D06gWo0OQu3BywH8ZeKwQzTXK7Mf7KCUsBBKuRHgy95TqFIyuKV_eRxQk3O4Icp0rjf2ikt55VP47MD2hmt4RqVP1-ezpqZzLNCLN26qy50zxLEFj3Z9CuOCewY4w3FZg_QRywIkeavrszxfWaaFCJYIZ_QuyfNQQ-aSvcBFeNkJQ-v48udW7htwP7r9y7C4DZ1J57ymnsCNyv-JiZw-uumCsXWZ5EeCT-pMSvR7Q0_D1d30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=jmz_-e5kMjgGJeQdH7mzP6OUsghv3Z-fr9U4TX04RwmB5yM1uPd383LeOOBCvuhN4knx99l2xvSZOv2wWsS3sFrrxwn-NCd_gvyuhyQXIGKfqk4B43oLCf_SqiNnh_UsA-NHjlP3R2JR6PYpk4611iI3mKOkA49Ezfzj4Jb-maLRPueWgOhlF8NjgpksD_A-CG8OrgaOYIvi2wprufxGa4SYv82hNw4EAsBjfctX1oLmZ5C4jS74-1c-utBbXmwguY_hTIgALaUrTcSyczhRybGwqh2JcCaPqp-4I2SjjG7hE01g76DrizXyR0AslyRlbZVi9PdpqdrDSOnH2DUAZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=jmz_-e5kMjgGJeQdH7mzP6OUsghv3Z-fr9U4TX04RwmB5yM1uPd383LeOOBCvuhN4knx99l2xvSZOv2wWsS3sFrrxwn-NCd_gvyuhyQXIGKfqk4B43oLCf_SqiNnh_UsA-NHjlP3R2JR6PYpk4611iI3mKOkA49Ezfzj4Jb-maLRPueWgOhlF8NjgpksD_A-CG8OrgaOYIvi2wprufxGa4SYv82hNw4EAsBjfctX1oLmZ5C4jS74-1c-utBbXmwguY_hTIgALaUrTcSyczhRybGwqh2JcCaPqp-4I2SjjG7hE01g76DrizXyR0AslyRlbZVi9PdpqdrDSOnH2DUAZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=IdcCQRGARim-O5celWWpiYWI5OuAHYQ696KGoBv1g0gW-3MAvGDNOjQstgHIP8Vj3S91wK5QQwDbkbSBtX1QdDSfA2KVGJYrN3N5am3X4fdNe27Z4Uwe0kYM5Q9OwxBZ0xzMvGPnhp0K8Q3vQD7HYUg8UqDSVidapU7MDKSjBbuW8JJKwZlVKmOI8hyc3tT7gDyF8Wz80O9UGTQaYfqNNSk1AhSe464qIATot3QcZpKl_V9oYRphFOlnt85A_2NkZGa8z1aGQNeol43DcEUapHS08voCbWONxPQosUnA9HPuo0xFM2JwF9bv-qd-rsHS16rta9gZMvgtl1kfDkDg5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=IdcCQRGARim-O5celWWpiYWI5OuAHYQ696KGoBv1g0gW-3MAvGDNOjQstgHIP8Vj3S91wK5QQwDbkbSBtX1QdDSfA2KVGJYrN3N5am3X4fdNe27Z4Uwe0kYM5Q9OwxBZ0xzMvGPnhp0K8Q3vQD7HYUg8UqDSVidapU7MDKSjBbuW8JJKwZlVKmOI8hyc3tT7gDyF8Wz80O9UGTQaYfqNNSk1AhSe464qIATot3QcZpKl_V9oYRphFOlnt85A_2NkZGa8z1aGQNeol43DcEUapHS08voCbWONxPQosUnA9HPuo0xFM2JwF9bv-qd-rsHS16rta9gZMvgtl1kfDkDg5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9Np_qFNE-3dgSV2SLLBx3vawQpz_zCK-tPAatNo0LyTGzDGfL3TTw0OxCRY4iA_pQdd6kN4tU4nBUBhXdiWvB9jy_9zgKU-54B80r6DpGAERiBylZxcWn3yUOPPknEhGVSC5zD_Kk6uBI525odwA-AeC-XtDsxc3sDx_qhbYJ5dDlatpBrz8YEx71Vd1bu4Ko5H9lOw2cO395h-1INeSQW1hP4B9l8kjsO27x4pywl0csgMCD1zzXoTDji6mbiGbj5X1NuclXXcAyN_8J3dQSI5lDf23OJoM3bOK0rsT6NW1tc-CEZ6WOAZR7RhpZhb9tOK7AyFJs8FXjlAzxguBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9eoEPc9yaxJG-ZzHm1Ww7cq0FGhKH2qpqsdoHLglAB3P-AuZXE9b7MxH5j0QZ6m5kB3X9MvzBz3YWA1SrZxCMH1fU68Ih7F-EakiMMVJHCA-eqCTt5dKxToCg9BGeJKBmCRnZ1uPmpX3Ei63QcpwL7N50s-fdnp5oHQuKO-8ZfuAe1pdi2WLUHp11EFhmR91JVoy6AwzZMA0Q7pos08-QTo9Esv0vBu8_PiCNciQGIahE_hhCp8_nkbk-VRUeZH46n1ehsW5oDpvz_KYWRsXpA6cw95-UFJLYMg8Wvx2VKJvjN_6CHLecyRNv5M65eVsfrucONShaTtsGI7RuchYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=p3ynj43YxNfHLAoS2J3XDpbEdFdbKsiJSEUfYBKLn_0Q75wZ9tt8nafLWO7reZykH_dV2zBobGnBusg6Jz5HA7oQ5caNpU3TwmPEsfTS-c0eyytSnIPY2WhIX0QFJFXkOMypS5JMgnFLs-DlfF1tbTtAp2Ouwwuq8X8ONIN2ObZFWw9ExEHWxMyDt10z1cJwUu81qjk7NdhohYUERRYHbgPDTb1GVgGMv0fWBtOc65Lhj31plUqka3Uwl6Zfui8qwp_HHHdRMcxiIhbkENkGspQpPawRkLz9iQNj-_LTlo_qrW_8axpcRON0q4ssHh3m_iT_I_DR0rzXBP9XN5muKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=p3ynj43YxNfHLAoS2J3XDpbEdFdbKsiJSEUfYBKLn_0Q75wZ9tt8nafLWO7reZykH_dV2zBobGnBusg6Jz5HA7oQ5caNpU3TwmPEsfTS-c0eyytSnIPY2WhIX0QFJFXkOMypS5JMgnFLs-DlfF1tbTtAp2Ouwwuq8X8ONIN2ObZFWw9ExEHWxMyDt10z1cJwUu81qjk7NdhohYUERRYHbgPDTb1GVgGMv0fWBtOc65Lhj31plUqka3Uwl6Zfui8qwp_HHHdRMcxiIhbkENkGspQpPawRkLz9iQNj-_LTlo_qrW_8axpcRON0q4ssHh3m_iT_I_DR0rzXBP9XN5muKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=uHRr7RZd1jicfprxUyDQQVPe731QKYdlDsNHzyuyb80p4fnQSrVeoSUCB5i5p0vMHzUzZZFaZ7ELH77KIW9lMxIaQ5lf-4YQGHX00A0Ml3GfXDCS41EaZAday3wiIBUHDvI1bt6TzrZwKChRuclTGmVd9lwAsIorM6NziqlX1uIYXwv6SQXbv5qGZ97n5teMzibuMAMOBxUQdiifpMxN6oo4hamuOqYa5cNcp8HS5nSZyG4-RaxQQnfnzcRX8YaxyJff0F-d0j8_CuqniuxOi0ixEKQHLvv2MqQ3DUBgbmTTSZfXXoPSLG-EfKXrCOnMitQgKCM8ub7CcMS21xt82Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=uHRr7RZd1jicfprxUyDQQVPe731QKYdlDsNHzyuyb80p4fnQSrVeoSUCB5i5p0vMHzUzZZFaZ7ELH77KIW9lMxIaQ5lf-4YQGHX00A0Ml3GfXDCS41EaZAday3wiIBUHDvI1bt6TzrZwKChRuclTGmVd9lwAsIorM6NziqlX1uIYXwv6SQXbv5qGZ97n5teMzibuMAMOBxUQdiifpMxN6oo4hamuOqYa5cNcp8HS5nSZyG4-RaxQQnfnzcRX8YaxyJff0F-d0j8_CuqniuxOi0ixEKQHLvv2MqQ3DUBgbmTTSZfXXoPSLG-EfKXrCOnMitQgKCM8ub7CcMS21xt82Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNIKhmnR9Kg9FDXvRfm9MvrWTaZisbtCvU19DsF4pKAmtY2T4e4JOZF_vDslx_OMJwJJPdyQW1a0jzVs4AQEO494bYZ_eGy_PcWYqKFvEQWfhp95zf6Rw1Bshz3mOZgxg82TF1wIHbej0Qho0g2T_zCQ8pavmD-d36fWgTs5L5Jju_wRr44-zWa26VDJMBOpFa1dkxDENbfGH392GHUNAh6Mai7QPV_PrjnNfX_niD55B0KaegMR0kRRKbSwGVykW8IE2upQpkVOJ1hoPqpstBOQqhZNNZ-HQXpo7c90DuWf1cLN-0T09vKlMPcy1sxxVbRcbA2ZEEn-8GDCmG74Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfSuIqtgtlv-sZ2onfulatxDez4V8yMbLD7plegFoTqLeSfQvwOF-j3gVEPAuDDiFNwsiSN0bRGNGximv_4gQi5XhqOFY7e3abosL6mAhF7OKZYNFTuoYdQkmzIhDQx3xn7KyBgKot9wYThTX7y_Wcl6gwhXsEkmuiNKOYsJbW-_TGwQgiXeTXjDE_jqkYJJMclKixfLmF1dCxQK2FOGp2rPzh2iVUo8-Cw-JjqrDGm9Db9zZg495udYuII6-DNzRv1L3fSiLI9kwrtHJvzsXJUZvFYAUfCDhr-N1XpFCB_f_ohxjjgRGjO1zmy_3d7tuLBu0iRJ256LCrD4v27bnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIKKf1oBerHw0U80ATWw1yd-su5K2C7CMn789A5xLCrNbRnnO-iQbWP14Oo-DerBtxe1SUljOeAjVcVzNwj0reJhsRf4wOUGJcQeo10vH_ymP0RD7MT4Zo_19JO2FW-hzCghWxdQIQ9ZbacXNXTp0K20jIvvwVUKmbFh46-wOHCNLkjJpEdUxAhww0K-RfJ-qN_pNdQGE28Nxskihwkd77vcwtMFk8d5Mv4fROrJmXdKr60_VP0HBTh3fZ25N0q9Syl7zT9Ei73teXu-tjeG1R8WC1WSAi8RzvhfweZzIu1CmCIdHY0X2OTWgHBvTJecf3H50HkRIp8WIjM_xW5O9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfak0iTDcvSsZcxdAi6UyPLZrayUOMH5znaFkW9AyezB39M_FuAVBRfW6DZaYq3aMJ5_4CNSzsbwAnS2VQcu3FolV61xruI9qqOE_j_MQQ3L3b5XxcNrtNZJdP4im-gUVBgdBs8CbfFesPb-OQ61zMoMyQ7uO60BdlcNLVaaxRGhdGe3xAhLsEU3dCY8BizbOs69VlzFPZvBanSj3zEnYNBWE-DNLwzeTWQpR-5qT4RXwnBR90nzvgcOCu3Zl1wKJQlx8sXoYoRAaQ8IhSfBdl5JBuPd2UIZaqwVHzngCfRx07YSJyS8eeVetXc7Ika7cQsEAu8LpydyvTasHFwEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=UYJk8A_z-TJvJeWM-0BV5toD5aQIFP3K62cfF3LNkBGQpYulG-F8FUfHKDj4_PM2-Hrj9XWu0X3kHt-rd34K-aH1xFuhEPo3aazjEEZPI6LMfM0XIpYITtOimDwt69JfCS6mCn4o3-8JLRkktt2v6VXHBnNGOODlDJ-9oTerb6Nq7k3hUQyTph3q0QZLyNfeQyra99WqbRnrFYWFOcWYgnJzznponXbWDikR3ekPjZO5rBGPlO1GIqA7qLN3X5gblZko4SZ8EMN9nrhRMg_cc5ZzsQUl7zHgFAITeQvtPXrb56ej0eLSoMt6vsp50Y6w0bkTzxz1131TuTBvWtb5Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=UYJk8A_z-TJvJeWM-0BV5toD5aQIFP3K62cfF3LNkBGQpYulG-F8FUfHKDj4_PM2-Hrj9XWu0X3kHt-rd34K-aH1xFuhEPo3aazjEEZPI6LMfM0XIpYITtOimDwt69JfCS6mCn4o3-8JLRkktt2v6VXHBnNGOODlDJ-9oTerb6Nq7k3hUQyTph3q0QZLyNfeQyra99WqbRnrFYWFOcWYgnJzznponXbWDikR3ekPjZO5rBGPlO1GIqA7qLN3X5gblZko4SZ8EMN9nrhRMg_cc5ZzsQUl7zHgFAITeQvtPXrb56ej0eLSoMt6vsp50Y6w0bkTzxz1131TuTBvWtb5Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=j-pPDKRTqLahYVROjbTdOifIWzbwbJw1iBP38SblGhwYgz5xcdfK7cPLlvgTaAoHn6xPoVoSzil0XGwJFbh8dU1Ufm94gL3AmQhKhC2zFyvw8jlJvm85rPJ78dkYLWDnQQs2FJeNbT6oqWxvhCtp5eoE6vVEN4L7DssHoQXlAZHcFBvbSF3948K4EfwKs4VmRnBXiNG75vyeHdFebsCiPc21tQkQ99cBsh339594mSfAcuC2BE_D6oKlvDh460B53ERUTi4mhgHOc6oAqFekzOvNhi3r0PKOkxnhxPQlTe8xsYN9pUnkR0zN3SG9_tJi0w4MuZn5AlHIL3qTKArSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=j-pPDKRTqLahYVROjbTdOifIWzbwbJw1iBP38SblGhwYgz5xcdfK7cPLlvgTaAoHn6xPoVoSzil0XGwJFbh8dU1Ufm94gL3AmQhKhC2zFyvw8jlJvm85rPJ78dkYLWDnQQs2FJeNbT6oqWxvhCtp5eoE6vVEN4L7DssHoQXlAZHcFBvbSF3948K4EfwKs4VmRnBXiNG75vyeHdFebsCiPc21tQkQ99cBsh339594mSfAcuC2BE_D6oKlvDh460B53ERUTi4mhgHOc6oAqFekzOvNhi3r0PKOkxnhxPQlTe8xsYN9pUnkR0zN3SG9_tJi0w4MuZn5AlHIL3qTKArSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=LRX15F8XG-YEx0aBLGRzKJf94LLa1wET2-8skcSaqQj9xvQzLDwKTEIk3jJ98zSHem9EtbdocGFEji9c1LS7ixtXaTPnfjqmE1HYBwEaNFsCEWytIeiYbomE33T7DQ9_pMz4iejCADkVvKUX1KH0Y3sWD4FLOtnbd8C0Y8AjTt1WHBPBfWNa6cnvCd4wsXb1JGlMYmtjeg5zDcyIG7imzBaOq3bo12VJ8jdKkWWQI_jMp_AERSASjUbHDNvsbkHGvyXlNck9EjWkUhxKVOwEWGSiUd-dxTs-dtFrQJQSBP8DRbyPlEug5LQ0mengVKG5ynrmY9seup3gH0qqpEJUKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=LRX15F8XG-YEx0aBLGRzKJf94LLa1wET2-8skcSaqQj9xvQzLDwKTEIk3jJ98zSHem9EtbdocGFEji9c1LS7ixtXaTPnfjqmE1HYBwEaNFsCEWytIeiYbomE33T7DQ9_pMz4iejCADkVvKUX1KH0Y3sWD4FLOtnbd8C0Y8AjTt1WHBPBfWNa6cnvCd4wsXb1JGlMYmtjeg5zDcyIG7imzBaOq3bo12VJ8jdKkWWQI_jMp_AERSASjUbHDNvsbkHGvyXlNck9EjWkUhxKVOwEWGSiUd-dxTs-dtFrQJQSBP8DRbyPlEug5LQ0mengVKG5ynrmY9seup3gH0qqpEJUKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=Ggr2qCoQjMGOH4a04x1qX37JZ7agT_6gUyUMXH0tIn2abfWPUNG5dHzPX6tO0HxcNDyu4bv8KO6hnVtWDJG1a6N2mSqMBBxvt5MpUUslzNhvRQ9bTvz_pZafujL3JTO-XkqNjB84pz1nn6moRWgUfjVNMO0Uwr28Ae0gQKYRg17ueGBgrbIECTtTe-saXpMLnXjud0tdGq6Vfl6FYRvCreY_CD8Mq5LkGqZVDDIlT3xvvHnGtgVrtsoSix2fXV1VGOHO0Ei2Zb0DZEIEQ3QllcRQJF3MfrlOnHL6kRqaFYyPUSKXKgVD8B_aWvFVlSmyc6Ik_cFHWzhs6n4YHapGCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=Ggr2qCoQjMGOH4a04x1qX37JZ7agT_6gUyUMXH0tIn2abfWPUNG5dHzPX6tO0HxcNDyu4bv8KO6hnVtWDJG1a6N2mSqMBBxvt5MpUUslzNhvRQ9bTvz_pZafujL3JTO-XkqNjB84pz1nn6moRWgUfjVNMO0Uwr28Ae0gQKYRg17ueGBgrbIECTtTe-saXpMLnXjud0tdGq6Vfl6FYRvCreY_CD8Mq5LkGqZVDDIlT3xvvHnGtgVrtsoSix2fXV1VGOHO0Ei2Zb0DZEIEQ3QllcRQJF3MfrlOnHL6kRqaFYyPUSKXKgVD8B_aWvFVlSmyc6Ik_cFHWzhs6n4YHapGCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5RVxfRpcn95sSbrYQqmsElK74rJ7SRLJ1vSsy5Zi8T5Qk_1iwghQKxDt6A8mOj-Dp0xw4mwkkh2Pb2QWVrdQ0PoDfY7v60m01u3Tra7d5mwI7Wvk33-AWgdBEuOdgDfdjdu0fN-Ao8qO_gi5qpXFbrerWA5ZvNwzMX_Wp0AtwPh-R0MxM6I53h9UNqnZxg0MEin2VyrcJdXKGPJ3Mf5wFCLSwCNxEJ2juXsz9MqeQnCHadZ1l3K79Y9GDploLFq0iee3w3bUpwfw6TqzhgosqPQK6Vr-paVYulVcDSQkyytLmKAG9vzb8OBR8XIqTythsZWIgOReFEOlah5QUFMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=UtlBkCXdo_hl53oIpsrCrHsAqiDjN7SBuZ9YVOKCGwl3qfdrkyFnLIlRlSHZb24bbdrc_SUdCU7DxLAkMVH4YVzfyOn9347akfo-Jboby1KnC39A2dpTxLacLN__9pr9q0gQdISIS02mCSiDfXF3_gqVzBBhZz24-XTIjtZIgSBCu3crNFbNhWg7WLpTTf3ExBH2YhQ-hs5KIHv8PiMFX4JJD5IieX7emXBIkREkw8GqHJXtxKkWHzBaX-l_1FhRyadr_3By2DpJSWjEj1phdrPsJ5ZyUa_-yIZpyXBKzHugaPgmoRRjEJmFFeKeQ8DTA7HwJ5JpY7vRD10iJe7LzbZ9MqcOs7Ei9Oaqnm7SKF9cVPqn7-MTQzZaxmtSjq54ZAug8BGd9lHaslHVu6cgjKRRrgRrDMpEyB27F2CXmjOD_JpSGPg0paGaNs22no_pWJ7fubR5iKxPSKeBbNOjCmaobnfFS12LZ4HAIkbammi2L0oWYFh785hGrNKqb3awRWcrcTHueqv9fTEz1XLjHXpfT66_SRkyscFaPGL7xJYdZILS6k1Av6_a7Js2iAfG5IgHZYGeQ7FddXDb2medK-dj1IPEGTSbttFu-mbvTzpxKuQIjoQJUXEVFy-N5NvKNh1LHPURmPEuQiHLHBL_W7H7vYmBBhsXFlKBWl4k30s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=UtlBkCXdo_hl53oIpsrCrHsAqiDjN7SBuZ9YVOKCGwl3qfdrkyFnLIlRlSHZb24bbdrc_SUdCU7DxLAkMVH4YVzfyOn9347akfo-Jboby1KnC39A2dpTxLacLN__9pr9q0gQdISIS02mCSiDfXF3_gqVzBBhZz24-XTIjtZIgSBCu3crNFbNhWg7WLpTTf3ExBH2YhQ-hs5KIHv8PiMFX4JJD5IieX7emXBIkREkw8GqHJXtxKkWHzBaX-l_1FhRyadr_3By2DpJSWjEj1phdrPsJ5ZyUa_-yIZpyXBKzHugaPgmoRRjEJmFFeKeQ8DTA7HwJ5JpY7vRD10iJe7LzbZ9MqcOs7Ei9Oaqnm7SKF9cVPqn7-MTQzZaxmtSjq54ZAug8BGd9lHaslHVu6cgjKRRrgRrDMpEyB27F2CXmjOD_JpSGPg0paGaNs22no_pWJ7fubR5iKxPSKeBbNOjCmaobnfFS12LZ4HAIkbammi2L0oWYFh785hGrNKqb3awRWcrcTHueqv9fTEz1XLjHXpfT66_SRkyscFaPGL7xJYdZILS6k1Av6_a7Js2iAfG5IgHZYGeQ7FddXDb2medK-dj1IPEGTSbttFu-mbvTzpxKuQIjoQJUXEVFy-N5NvKNh1LHPURmPEuQiHLHBL_W7H7vYmBBhsXFlKBWl4k30s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B43ZaMOANYKGLhF_8eNeDel81sw5Yx51JuCXGZtVr_OHDrhOGKIZk1Xs80lAuVjMy61N4ulTDR_bFif0OeUtUyGDdWG_n7smegY0l9ExdrqRH1LA_zfHIVixuMAKiV-RTDIaQZkXi5qY_4Z24-ZMXsNPYQjZOqjhCxRIJxIUc2czXVg9sM0WGORW21EEQ0zyNdUnWuxbd9r91TBOPw0CN_jW5kiBAiET7_dfvFxCLNqe7ie1mU7KRoyOiEmYXJkxwMF9gggiINeIisdK_HPlnIOYyObbNRVKuNiR6h7BIJbQblvdg3hyQwTWGyMADxPOwO4gJgWRhI2mJJ7P0x1GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogBUUP9aXj20HTqqEFR-SNXTPAjqWfyYMAOpIyVYprzAnPj2n-kJrkKcNlOrxHKiowasGS8li6ZFa8cA3klTpTzut6Dz9wN9JY9nolF5ZJ5pS4H8-rOChu4lA8WGwzUtF-YoX65tEy_EnV-1c8eZ6fdo7CYsSw89C3oBxS467gF35i_UJ2M-gwBbEbU1DP-A8DOVPzIPfTHwCbgSufRaaOHFuKWVRyRW9Mm1ZZtq_ZWuscJCLxaEjTLc9w6P2CrGKwF2P2fWyTd_p_I2WHMaSHZHcSl5UvGdA2gwtku7f1LG4RwO8X67zbJd9AkqJbnADSEUJqFImPNZUlvqeUjDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEOuotHLtrLJEqhI2wjO-lRkd5wL4sMpgbEsSSs9L7WVCxZa9Dw_FYK6OebLIIyjXIuB_YkrLcCkUAxqP1cLTHOy2ObPHjOt5jv41-FHOVGJ81Lw8eLuX6URBUmFeNvOzgIMOwd08dm80UmItrWfURUowHMR71kKj1jRC9i88eFF1aHYHnwNQ-qPKyqW7e-zBnVmvLXcE1D3_XEYwC_jk9in6-_ttMBpIs4rwz9-yziurCn3GgiHyK4JTqmDfnqVr93cud3teXeoL5aWTbXAdiBBcxqlQVRZqTNZ7Ry8KnpEHuHSuZq02NBOkXvObl3ZJ4q1WvUfK0fZPzXi_CTcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSwKaqIsQCnsoNcljkDpUkuhMdP1HWZ2PnZV9gy0f68kXpDQVDpfupKBIvlj0bgP4oXSu0ESPWpA9GS3RbA51kv6Tuqmska4bVD2awUvb8fD-AzRk78nIxNKqPpLnOSjdXH6eEUfGM4tL5hhaYGygOJa65ccfJQO5b715KJ-XBuHH8uWkR4j8NzHBCsr5eFoEt6kf3xylPfvG0X6mY_0ISUMU4sN826jEvgNr-5gs35OmmGc7TmmiGf5qlcyYv9oGbN_jqL0_Y7gfosraANUlCglWe3xfj6szjE4S4y7xR3hexTICdPS2JAflJbVT7ckpr56ulAeSpHzVXa3tUFaTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=fQ4yYtsh9P6jyc07lrC5DUYp-vIvE96AIZM33gSRyUV1FfDqmxFr6_DRdc9sGQ_aiKRhihCl9tngAW9ypKlYFXRLUksRgySgJ_t1bkU2909NKolC7xCeiGJejKcw0k5f03Ju4_8PhUJV_dnK8Hsgth_p05Hm28lmD7Nok6OfhlF9p3jia-9uD8cvqXddPNBqwAfd69cVINSbbh9onAJeoZt1iURKfmvYl7y3P-TKXBX_nQbIJzkYmm8WqQcSiwFYC4jiZjLMDqWK93rFzQ7S9f1cIQQK5gDim75ggXOSwrPI0jqbO1cMggGs4mgcKDxBLFnuFHlnJDr_-OaLQ72qtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=fQ4yYtsh9P6jyc07lrC5DUYp-vIvE96AIZM33gSRyUV1FfDqmxFr6_DRdc9sGQ_aiKRhihCl9tngAW9ypKlYFXRLUksRgySgJ_t1bkU2909NKolC7xCeiGJejKcw0k5f03Ju4_8PhUJV_dnK8Hsgth_p05Hm28lmD7Nok6OfhlF9p3jia-9uD8cvqXddPNBqwAfd69cVINSbbh9onAJeoZt1iURKfmvYl7y3P-TKXBX_nQbIJzkYmm8WqQcSiwFYC4jiZjLMDqWK93rFzQ7S9f1cIQQK5gDim75ggXOSwrPI0jqbO1cMggGs4mgcKDxBLFnuFHlnJDr_-OaLQ72qtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYtBMraCVx3vnpxhAH5ragQGdruVjBJkTQauLBvoPCl5T6OiF_ShhOudwYV4Y5a_MG8_lwtIePJLDrBQCSQZ7nTyzb3aTu7JckH-SztbP5Isnlx10dpFRz6z1Ou1ly8b9eDljnIwojdLwuJ9KaJEZ8NFPkfLsZSln5UoO2aic5SLj1EkM6rupaTPQig2kB6zdJeMZPTmJUO0wDekme6Z3BjpgzVsxPxr3mEMnTYWAT_mFNzihGo0S6vHzF02xCIMMzhOQP0ZcNSa1iAswxois3wudB1ulac6ukzRNASZtxX763-2wvzrAvJQQgQ9tgT-q50EtVzKTeJkxBBDaB8aeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=T09JRsyFmnBF6u14ZzGH6UU0Sr7uOnk7V7z45MGVnzdmC1-OY6dw_0-lh2DjEpZhAaH68M0uvfeNJHO8x5-EMVx-NPRx4Y6u8IMwGKeSYCvZ8IktzKkyJwqj1TDXDtHIyz63KUodGuehSFQJKcy7BKu6KKfP80ABJzUHfnDmFJ0tlvzbZ91frmetvMlFfbbLZhASuz-fW0I5sbYIf8vGWFjvy4wYTMoBCVsA_ynl8Sqob5m3-tgPPkC5fQUmmMxskPmCCIn80n28e3HNVaq8yqHtGsXch1hhN_9LkarIwjFgR2MPz92dKYU77_08FHSeARZMwStheNga6Lhr2g4VJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=T09JRsyFmnBF6u14ZzGH6UU0Sr7uOnk7V7z45MGVnzdmC1-OY6dw_0-lh2DjEpZhAaH68M0uvfeNJHO8x5-EMVx-NPRx4Y6u8IMwGKeSYCvZ8IktzKkyJwqj1TDXDtHIyz63KUodGuehSFQJKcy7BKu6KKfP80ABJzUHfnDmFJ0tlvzbZ91frmetvMlFfbbLZhASuz-fW0I5sbYIf8vGWFjvy4wYTMoBCVsA_ynl8Sqob5m3-tgPPkC5fQUmmMxskPmCCIn80n28e3HNVaq8yqHtGsXch1hhN_9LkarIwjFgR2MPz92dKYU77_08FHSeARZMwStheNga6Lhr2g4VJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=M4hI8cxAiLQ-GLr-2sjvxjhPUb8W-Np9HCGNcJ-Jd74oFrC5QjKyrhrqFOx6UsE_t0WIb7UcQQQ47QP6OddpT1udKkylCgB-QBQWKubittj2bNMbcIzz-1SM2TK-YXhdHT9Q0uFmIx7Yrq8kdsE0LAqqpABUYGJveJeaXw1WRHuJpVQ4nUIjxmsWJUja2VAuwXii4dSeUGGfD3ifrXh-zN7BVdhLGO9S0r8sjd1UedYTf6YwJOGEq4WB260rSajikBMPze7Rkts6aO9aZ5K5guJQ_8_6XhvzEeqNFjlmosolg_XGBLf5bJ46aHiKR2W7B72dqr-ABkOjMv6Qq3ua6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=M4hI8cxAiLQ-GLr-2sjvxjhPUb8W-Np9HCGNcJ-Jd74oFrC5QjKyrhrqFOx6UsE_t0WIb7UcQQQ47QP6OddpT1udKkylCgB-QBQWKubittj2bNMbcIzz-1SM2TK-YXhdHT9Q0uFmIx7Yrq8kdsE0LAqqpABUYGJveJeaXw1WRHuJpVQ4nUIjxmsWJUja2VAuwXii4dSeUGGfD3ifrXh-zN7BVdhLGO9S0r8sjd1UedYTf6YwJOGEq4WB260rSajikBMPze7Rkts6aO9aZ5K5guJQ_8_6XhvzEeqNFjlmosolg_XGBLf5bJ46aHiKR2W7B72dqr-ABkOjMv6Qq3ua6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=eXII67Ggh3dud5GQPS-edHGI8tWTe7gi3j3XRtaEw4liI0a9Mg0HuXpq0d0REtvsdfND1ZlhPByvn0TU034k-tbifrN1ac_m0j06qPuWz0HWgHFC8tCbokPCxYpvoZG4y29CrYfaJC4FqO0vbHTzOB9vSuaU2fQRuOMXmSm1EIondMSoF54E6DZioo7wSEA24BTZBosFkV-r8Poqi-QDORr6CP1uOWvbTqmvt-1o499yauJ-penynOEUee-o3Dif_Tt8kKGCR90IZx0UEvGsDyUv1XzHw9SKcLJGl57yBhPFulrPRij6JPqWy6NfOK_ZbofjCBfjRYT9xL5W8pWAPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=eXII67Ggh3dud5GQPS-edHGI8tWTe7gi3j3XRtaEw4liI0a9Mg0HuXpq0d0REtvsdfND1ZlhPByvn0TU034k-tbifrN1ac_m0j06qPuWz0HWgHFC8tCbokPCxYpvoZG4y29CrYfaJC4FqO0vbHTzOB9vSuaU2fQRuOMXmSm1EIondMSoF54E6DZioo7wSEA24BTZBosFkV-r8Poqi-QDORr6CP1uOWvbTqmvt-1o499yauJ-penynOEUee-o3Dif_Tt8kKGCR90IZx0UEvGsDyUv1XzHw9SKcLJGl57yBhPFulrPRij6JPqWy6NfOK_ZbofjCBfjRYT9xL5W8pWAPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvirIqlDJv206Fm57GDFyYvAvlihHMwP-2uKz23Kd72IvX_Lod3_b8ggVs5sbqU92qmAMuO2xgjfBxI5dYQ4Dc-UUzKeKX4rnDGFGziOWCAbY2DbqWSHmokAyrRCK3nXqG2iQzBYQ7aEOufauyCmRnexg6dpg7w4ovRRBTrPQPs9PEpjk7gc3Z7DEgbJdUmu5x-ZSsjMBqujHqWIoBktNnu3nKrdy5q0zTtt2nEKxig2XzH1AAzzCQYadsS-mw68TYQBkKkHXzZyQc94zbHgGtr4S8yKk7eOYQVKu6b6KGV79_CdPENhY50w4Ysjb3Jimi0JN8eKZNFeVyid_iMLLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSJEcKa0BlHAFiF0k0oD2pdabIvtYhnb-PEK9i5EhTgmWJypS6OJbvRLMMAZLJG5QfXmInek5-S2MQzKdhg3DutuQfK5BWWyVShj9XaA4XBI6EYjWce0STQ7a9XSDzeIyT-RVRQd1LAdHtXxyB9IX854C97BttzU3dfCwa4pXut_WUUG12PZwwZJlJ9FJqEl4bHDT_Brwo108eiVZvKy2Kl5rGi92hZnF04Xo6T6uJAT_o_T0wJYAI0t3EM1xmQgt-bFvzPj-ni7BAaOQkwU6ej1KQ14a5u24m9yLV_cPtMLrI3UpDDkFcSmO1N-GIhU3NfwKvQYN2D7NkIoJ05JkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=QkIJFDI14K69_M46TD0Cv-Ci5Jy21nBfNs3ENsktOFON-RW9Z3Aw42KV0wH964ibjfHoPnwCNlrxV37up8mE5R7BMpIRE8QpoV5THpQ3CGVwt5Zwz54fsD3LTdUwfri2pHpYPEYClbAgGuYqT_XPPoh1by9wT43bJ1YdJFxKYQ-4BT9R6KWAwEDnACsYD-UTL3dY5luITybiWWA-96YScq4wOQVM6nP4NHEHuRVxXeY9U7AOJ1B3kYE-eAPtJ1CLsdnHCZYd27t9Sx2gFq_IOY_nYeTELxMCVbkr2VxmMzcbXD_0CQ3216ksp7arz1bpKTizctnZpmpOudOcgcEYDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=QkIJFDI14K69_M46TD0Cv-Ci5Jy21nBfNs3ENsktOFON-RW9Z3Aw42KV0wH964ibjfHoPnwCNlrxV37up8mE5R7BMpIRE8QpoV5THpQ3CGVwt5Zwz54fsD3LTdUwfri2pHpYPEYClbAgGuYqT_XPPoh1by9wT43bJ1YdJFxKYQ-4BT9R6KWAwEDnACsYD-UTL3dY5luITybiWWA-96YScq4wOQVM6nP4NHEHuRVxXeY9U7AOJ1B3kYE-eAPtJ1CLsdnHCZYd27t9Sx2gFq_IOY_nYeTELxMCVbkr2VxmMzcbXD_0CQ3216ksp7arz1bpKTizctnZpmpOudOcgcEYDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=Ck7P7AEu0KwMsSrXKHBF__0CJSKilthTldDGjQVku3enkwDDNAVtxuERuOXymQMhHlM_gSo1PCTrUyrbrVQRfPeWGTPd62V0O0p0mmwqZnjEvCR8qModY7md6V6kFyhJTdlkOZngOUeXxDdjXztiY5NEE_qmWLJFx5-AYi5Fo8MKRYjWZ64oAB8xYJ1Ez-8rQYBxPmEoMkh0cAvgHyqXWzZOj1MwZL8-TWk4WvdVd7FEQVhQWTtaRksHt-lIo-XgfdijOiAzgzzuN4N_PAdMEdlZe_I7n1MhhA_OP2FqmjbAv9SdTvmPJjtdncubhfMnioORO0p_mKKJbVj32zHa-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=Ck7P7AEu0KwMsSrXKHBF__0CJSKilthTldDGjQVku3enkwDDNAVtxuERuOXymQMhHlM_gSo1PCTrUyrbrVQRfPeWGTPd62V0O0p0mmwqZnjEvCR8qModY7md6V6kFyhJTdlkOZngOUeXxDdjXztiY5NEE_qmWLJFx5-AYi5Fo8MKRYjWZ64oAB8xYJ1Ez-8rQYBxPmEoMkh0cAvgHyqXWzZOj1MwZL8-TWk4WvdVd7FEQVhQWTtaRksHt-lIo-XgfdijOiAzgzzuN4N_PAdMEdlZe_I7n1MhhA_OP2FqmjbAv9SdTvmPJjtdncubhfMnioORO0p_mKKJbVj32zHa-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJsvhmOSm2EZEV_4fvFHElVVSINrZ7RSbLGpnk8ktI5FaAGXsRXQd7URLTIEGp4phz0gCboAMKBP4JhGkU_tNHeCeNC_Nd6UpkGheDoOleFeuhxhK-KfaABY73bXU04yvd9fvXRaPkztSoyfbFQDTw7YCFugGmCeLgklBV770kJF1VULFX4rsZT1If6Ppcotmpxa7jczo5BCBGpX_YO4FHkEKD5IIY2AGvizq6A7NuFCkgM4dYJOnnG0PjT9mtnMqF5Huf_uNfGF9-3Sm_4-FtDREwnvIQ7bfKWV-mkwF4CtSlI9bw7xhLU5fVI6g1gPVbb4yLx9LSWD_zTeCW9ALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJyIpUU4RNuRotWZaGD2jQoOWf5PT1Cv4K8a2_AUq1iFd-8ZFif8eMjxIIQJ4ikIcNN-jgpGjZhOkgr940iZ996PLJtPtVynEfrfowg8tiudKxoT4MfGoMID3M3mpKjY1WKr-EUnJoontzoQ2Hrz_zHuNTm4CrqmvAFXD8CYuUzouSRqDHHQvFdkwItka98ZCzNjjFjAEQ-YF9iBueq0ntRG30Ta0iMsp-D6gdOEbY4vFRM_6mm_Ukw_HcmZPrsi5bGGwtBNTLBv0IhUG1LaTpKtRICzL_TY7u90IEHQAvXMDzu6SbWWIrSIQp-M1cWeJapptggxsXfnwZbwPF7b2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=biT3Y9wBu0sLo6PCtR74ksSKoeBjr8JBo5-8t2zuTqDn9oRXxES8xdPbeCbEq_utxOx9Y47uNFmqGew_ZpWG79jZUo7QX2FDP5_CbYIHAi01z-SQ3xWDBrXjBTXlYDohucxXM9g4c5rDWy8jP9k3qJ-ZZupvuGzr-rjvRSo6ifcBbJ6aYc46u62jQHmrj_OPtY21OvKE5LXYNxlONyNCZQzKHyqelCw6EPzOdOBitgFE2MkK5IopaQFayCrycgR0xcyENA9EaR77orMZphz5SoM6vGPmGX3qO3kZnbcQQd72wHCAJZbc1-ATf-g1aU-ihev2xFm2nrUJ6ex7sgtDEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=biT3Y9wBu0sLo6PCtR74ksSKoeBjr8JBo5-8t2zuTqDn9oRXxES8xdPbeCbEq_utxOx9Y47uNFmqGew_ZpWG79jZUo7QX2FDP5_CbYIHAi01z-SQ3xWDBrXjBTXlYDohucxXM9g4c5rDWy8jP9k3qJ-ZZupvuGzr-rjvRSo6ifcBbJ6aYc46u62jQHmrj_OPtY21OvKE5LXYNxlONyNCZQzKHyqelCw6EPzOdOBitgFE2MkK5IopaQFayCrycgR0xcyENA9EaR77orMZphz5SoM6vGPmGX3qO3kZnbcQQd72wHCAJZbc1-ATf-g1aU-ihev2xFm2nrUJ6ex7sgtDEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXcYDnnqjoZOMVwTrivTFbYfcV2B2tNBH5U5RRnAytD8kkOpp3wRkkIEvG5hn02EKi2PlYv_AnD92cMsbRHuuV4Sw_NkYPT3B57i1AGN0lBbYV8ZGuft--7z-T-9kh5tMrL2ZTexY4FHkSLva-9a23c0Id0Ybh8j1ZRghhpnrnBF-RRt41BeygS8O-No70pCLc8RlpDWthPPGDhBzsCZlSipgibRDhiYQtJI6tVxmK2_L3JEnGTAGHNcFkpMJrgaHxiCSIFs6sfZwmW8b2DXZ1fhojU0jukEiDFi3yq0AKZtpfjXzDkbnpRQlCPty24OCZt7OcCQdHdDpKeutiy-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlv5uWZM-edYNL3MJnZDd5Rj6qvHVOfELoCEWx11xd75wH90rVEmOG6Da72hmj2N8h6MIJAZR6SkvplSMbneZKnCKjWSW120mdS1fkYU7jqQ-5qNkd1zXnqEB3K-_0tpHOQiKwa0kQkv0GnZ3TlAy1jg2raew_a_k-NPevwh2uZqiFEmzbRhlN8h3mLdDRQci5Qkwd5F3opi-fUMSWuIvacNmpnzed-LJ5LelG8s-KPha1vPqyZn1ysFbyuNrcHCSNQ_j9EdnS4oDX8AsAAvX_8j-TOp_oxw6-gRO4LmlkNMaUA5gjDQDPBDmPKTq4zyxcPTTlVCpIlxFotH9afEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBMpCvjSE7sDw5h2T8P9luNWKd89i19OONPW8AvC43MvBq9g8nAOp8fz9xcuUJlgzR-6qY_-f824-yByLyx3ljEWNEwGtlEIz0i7RhGDnITRI_Eg1w2XcRhLk6tZxwyowC81ClqcPNB7vhlCnJbmDIUdV2su3RFiWBahZzYs90O_1rU7iV4XHzMVzANEoOp_FK_wO0JZyPi1XKxmTqqQ76xGidv2wWrvEPhV3Jw9KjDfL0jQRtE97LXIWpG8-7rhP3jMG-8wyD-CZR29I6meu2BtQHR8riosBi003nR95VIw5CRy21g3I5R-L_WMhhKDifJYL4_ZvULp5-sTW79ojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MM7ltHcvUlP_GmDBRmMChvLCOMirs6p8j5TVvSl3r4WPhvcDcdWihi6pUqiCf8IsIsDJvGra-1xLLv7Gy50fDA9wFzDpSZiFvUwRtPjULAa6J6r2XC3bU-aUb65B2v90hsKQkZ8t7xBJ0gQedfP9nlAopJHUDG72hx5rzMhfdKsM20xHDQTLmsuOShDJAafGbB4Oq6W5HaCsNrdPJcewF363Kjz_csxRTD-W4pQPzMHGuFAyNoReLOiEWKLyfJn9xEVQULfVFs35YJOH99Rp3RF2CEZq82k8bLXDNfU01eFlmmFdJasZ6PCpaXFJ0fda4oxrHkSXUvDRZP8ct5U5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zp1GuqdmLfW0ZUfwrKyLr5UGglrV2sBkWc_tIJFYf2ZXOE5WTgwXf14vrW2AvajiJJWTazidnSdFOda3Y0i8hq3yTS9mz2rksf53ciFqIhpFSTQ6xO0cYfDElfwZ3yR7hdmkihre4L_-C-ExE90Dv1tCeBU0wO9zUl5q7S8427oOrBQ0ISaa8OCDrtqgFywGwcLZ3EKNHqEGM4EnMemc0c4excD-HBG4jTWt0xUqs6aOyBHgIXVetFuT1ElsegTQ57MiaBDP4Apu1bOYD7OHIcAN1i_M7J2ssu8RzyvpLnAGjKs4FeIY-_j3mA63GVnSFr8HUDc3zoaWIKtg837DlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyIPAU9sYSFeKbOuU50c_aRmb1pXXVJOXm1Tf6tul5BnHN8_ZCmF7mLHLrASnUuTyxajcZV27b75hjwjsV_EN3XKeSqHxHRZS8IgWGaSTfebaoQ0EwyUBhi_pGZ45hQs1MAbeyNmvyP1wpyLXVLnKzx4avGIvYKj-n2JAVJSpCNjPu7RfzAvRDgh7oaSSsXsTlWcqPBfNd6nAUcBMeOb9dXz7viCK8yglxJIgVMTjUFtBlPpW0kt5jvEsAmaAo3t4Tz7zzuDCvcC29hjA1ORVvz-pHlk6wdpl4SpVjuB0g_Ns5XSoRf4EmeIWjJnP1O6NhOIb4eYZwjrbJVZL78yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTGfyLT8x_jPS5aQmnFxPzg6Mou4ysmfkCyRQjqa7JKOGPxxrg37-TCxe-dfszBGAB1_3iX9vsXqVuSHiW9gMiiBZBdBMoyuYUdxse7WZvRmfQJOfUFHBjZHUcbSqd0jLAYIf4F0qd4OhpWK9v-xJr5sy4uvlTz5kuRsWZuzUgszCXhpWWvgBzhDrKqQBKKdpttDvhlKTgnS217DiMOsWmvQAwXT9kcojQxxPKYWGPX6SNbM8Pzvwo80New264E9t7lhWDiCA2ZsLYFNqpFCr2CNQCs9e1CrdwoCjVvDK6RMpocWHjNvvaTbXHmb5V4PGJYZvLP1voUx1snbvXDN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnxtOoh-K6TUpT0to1yrTBBVku8K1QY0oLE-m7sU6jnVTvk5yIixXkZpPnlZ5XPnawm2_UbYC8WhlhGVK39c0meuGRWP06QY0jxsnSz7rbs0YXPN3D6YuJsLQVh1M80KP_Ny6ZLSK4WMZ-QPJq3QYJ0SgWKKMbf5z3qhmvNFbo7wjUk8GioBs26zvSSCP0uQvavvHasgntdTDA7Sl_GkqAbR-iJqc8PI_ME2xWfqcI09Msn5VjDmFdEBXasElTr4m3K_fcwwcRS7yVx4thhFsKWQ1F_9eRZyNYXs4VJMpGnRy2BY7DdmdFPcwIhKJEz-kk83hDtVZ0tKOMi3jdtA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=Gc0O4jgU2QgJxzS6ILUUceMp7qA8axQOn8sta1eFkD_NAKZvxdQbl9szF4Aw8ZhUwluwkX6urK8qWLwLqdS02m8kbXaBQnoMo7UmTniWyZa_yWnzEdgBhahIVcq4FztyDVqgquHDhZ_gwr_5qtT0JexFtOo6J-NhGvQb3OzbT9TewV69vhlfRq-1nOoj52HkMsEugcO6igsRAuu8FyE19Ku_Qja8EHSvnUsV0mnBKCfJ-RCbUnGtmfzblNqOm5b37qubzPIiQyb70nsIpn4FyJ8AVqG45hQGsA2d2APy8DgqlsFdOT_uHBo7TjvR9uXH5t5HMj6_gONg6R8k0muE5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=Gc0O4jgU2QgJxzS6ILUUceMp7qA8axQOn8sta1eFkD_NAKZvxdQbl9szF4Aw8ZhUwluwkX6urK8qWLwLqdS02m8kbXaBQnoMo7UmTniWyZa_yWnzEdgBhahIVcq4FztyDVqgquHDhZ_gwr_5qtT0JexFtOo6J-NhGvQb3OzbT9TewV69vhlfRq-1nOoj52HkMsEugcO6igsRAuu8FyE19Ku_Qja8EHSvnUsV0mnBKCfJ-RCbUnGtmfzblNqOm5b37qubzPIiQyb70nsIpn4FyJ8AVqG45hQGsA2d2APy8DgqlsFdOT_uHBo7TjvR9uXH5t5HMj6_gONg6R8k0muE5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvGWhLL7Y6q77zXYRdopxa7mU0SOe0TuCLvi8DQNZaB66sy4TdrwB5sTYponUzEwD_Kt9TSGh4GFoc1s6RMV1F5UnGES-KXFJER8pYneThQZr8L6F59uzn-QKrWX7Gb97_aDyQ_qMMKKEWJeE95hGtX313AIvbSyjyCApgyTZ7a4I9HtdLma0kWWPBtqfNP1JvAaN_iPytZCZBiifTGU2ysFvHLwATc-5ANgdX3NiduN0yzrmEflWLVhG_yKZOWgkTgPYQzGV0IZIqXJ0CmPndyVlEj01NrTL7er2tzuAg-Vl0viKYm9_F9IG3BBdWj_KnlhjC-XCosTmjAjT3foSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_lA8VynBcYPCWS9dF9do3mB3RzjsJlvzRUMV-VNVu80GLzPs2qFyRQZLJ_rSCdml5HGUrUXkKgVdR7o1D1YQbA6YD6BTcYdpVw81iw4rUzMN-BHzJdiV2sKQwtJvxqEkQZCA4QT8VQrWT11cbefzVagIf_xdOGTFMauRC5bhJhYDg2qyuA_mlYpiLnL_9FnvuzzQkoPjlLyPRTptZWdjjIjkEc0hH-5Lly-ECu3IndKl6UwjteY-nz_8lD5AMfGaIOq35mdrKwtGNLCYtsfy7TaxJVyJIUr2ihnFMu9q2IlIbR6OzeYo8eBBi72f9_WowdWp0CwsWUDluCXO_L3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULKlHgKWq2pDFnecTTiYhNNpgF44x5cAW6lfIdbQHpe4CuNtc4fggO24HUWVa5lHJahzhlodNnb6sZpqiJRGgR4c-yDgMxIOHg1Ue3I11nI4VIMdefXCi2FHSU2XeUjLYtzksS4jQ8GQNtKwwS5Xhpv9eQPVmA0jjhOPa8zPDvF0DVAm4ClcQcjllz2YyVyafKelwyBys3MV4ab44zAsIeQr-GZ4Qut7T1zOZwMkk82A5bK6iKX2crh9sbvSAOcF30gEDnSm254GEyuuvgl85pEXOf5u1pUOe4wriVzR_ZccFZ9_PUi5B2lTnXNtfj7aff1btAfLBHyefjcV7JqnuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcv0wV9UaOddoZPA8oBR3KRg1eVFB5xM9tYtwkvgarRxzbkTvdlbDetNx0lpUTYuCNicSO2TlR51eKKHxrmxuEDrHaUvCkeKUAUXUFSBW2i5SY8TDd8uPSleXU7_OfFi9qKdcynK5o2E0P7siQT05L_CpMnI1z2ES5ub9DAtm_yAqRPd3pzoAMNGX07Ua9EhndCzjy4DE9DVQ3YS9NFz8zn2Qf1YgxWt1KGErsND41RYImNXyv7Ktg3Ypm7qy0USkqAcv9sWcfsm46bgxXZEZ_VGmLJOG0U_kV0vXpGCYxIB1xuHQvdwzl_ZZ-G6YgxrdMrMCGa5OCVDcprQqG0Jqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWIhs7YnY2Br6sEqTD93_0ZnevHmBmDogPTH0V0rrEMbGtqdy_GdzLKGT5UwiBRm597iPmpKqM7Qgc_2ar68JHMyPAWeU-lsjHf2NIcyvCUDSqKAeR0SkeIYTae6GrLxMNJu1xktt6z98NwG4FJoG-ZSs2B6yLNv8v1WAZHGb8jWzsaUbYjWYvXPFUnnwoCDcAcgS1PhI-YjxPn4Py9do6G4Zo4w-l4tZDdquGk7FAHvy9hokexDTzZ6mEsbhLb02iaFOcoNii2oaqm8WLZWfa1oAT02aqT3k5Z6odWqy04jUYPkWzjcLkI0rZth9HvDo87_xjOtobW8xeXV0fCWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwhzog9XjCZBNuVQPO6PxHzdd5SkmeYvnfEIWBsHd6T0U6W_3rZIsiikUp3T9H3L5eXuYPFVZseUggrfBqf-tRiDgNXL9bccudfP2nk7wd978cW1iEobEAox1yzDe2H69aE6vzuv-dPFTMDmpUxTtja4kXCQ6XtW7el_EJ7OLAWKzzg2ckDfFrsZE6x4mADHENst9UiIzH0ozbM9Qw03JfNQxk2Bxod3L1PRKqJKSnraeX3vakxzpN93glSuNdrre9ElTr-jAmMeCUl5GwWO8wSxaPaRA2KwavhaVJmd4RMJPpf-3asYpCqWbAtBzC35PS85II_TaR9v6Dple8uKlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVZTNFaV9PKOHMMstKmBD5O24ja5ojGQGu7mq4Fqg6WcXYrdV_Od2qX-V1KB64-gJFKCyscYQla_QUPKpgZK6CION6qsjEVc9lq0u4d4Zp86W4XGj-b-MvIuh6f5CFlwJnjHncuUDB4KIX_fmwTJO8rG1SWEqda3tc10TSVLqBJzl1T2pKoGg2KNS6iRX1sEI4ifpuW9Eo4zzmBzKX0-YeozukacYd_PSMISKx1R0MELwsM5qORaH_Y_tO549cKPquZim9scl3HKCNTGL8IrbuByD9oCuHlV1VIfeMlyl3FoqG1wkVJpr-tA8VuihkjvewkmXtAk2EME6jCN8M1MFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzyKtyyb3p3cMxGm-XYppfysPUZt2V082_lyeOPfSCTtALXnok5Z-XuedOkpZ3IkKQEFsCVV_gMvIn4Z6v1XeSX-GcPlK3XV9TMJYYFe8h2MZk2XF6zcch9dma9R9KtvIzz5LKkxBIN4SQPG-IL4lK9C8k4JOIvscX6b3Pr5zln2kPuiwW3T8A_xBy3NmWmi1OYf6FS-m6PAhSwUssoxr5tVg-z3yysZMcIwGHWSgC90b0LuCCnJdFzWnxgVfHzPXrpsz5tYRMTmunepUhIPOANuv1vjvRlZyS9U8LwPNhqlvqjMDu7bQVAEd7Xy4yBqteKExekK1SOPjQGmJz7oNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE2AmCBQ82kRlpeNXkEiimU4ZbIgq7qF9b61TrKdPmLaa-xAi9_ijrUdHxK5wLVUZgCJ8JLlHdUpsOCadLWGxOeJJXI14-zaEaQWLuxVR53Gk0dvs59KmvYIomVqmYV43vvQHkwIRPtCECOmuAA3yCGx1w_yHOCeqyRTboeE0kD3n0l6bOZU3Uf6k3Q0HuX_dFrQzaNB8lukFq3amzH_wZI5K49v9caQR_yYXvGS1jFSmunuVix2I74TDT2PY2zTaMSyQJq3RelFWVkTz0U0u76RDxEJ7XEijTXiHejRJmmikhgvwnSq1x40qyXfaM9J464W7yL52h0mVB0gEbC4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2gpOXH0-9mA-uH6jTE3P9n7iH-MTG42NaPHndIn6xW20dYlfeU0U_ekPcrX4MB1JY_wb71RsPge_5l_QQjKMABmv-n3JqmHsQI724Uij0fgNLZqJTd15G-lwou1X3UE963YzhCPkGkP54T8aT6zxULehCzTjNtDYqr04G8WDudT3FCMzk5VH6Zdgu91Etr-YNEtah4grH-br4GMYcj5pg8xxYEJufWpfqWJK2078ohDEPdmL7oC-CdIEueuENtAckS7lpFKm4tSHE1chPIzEXGKIKFFhFgYyx637palT8tSwq4gaqRheSVG4tSZ1M4b8h2mLqouY-x_TqeRYegmJUoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2gpOXH0-9mA-uH6jTE3P9n7iH-MTG42NaPHndIn6xW20dYlfeU0U_ekPcrX4MB1JY_wb71RsPge_5l_QQjKMABmv-n3JqmHsQI724Uij0fgNLZqJTd15G-lwou1X3UE963YzhCPkGkP54T8aT6zxULehCzTjNtDYqr04G8WDudT3FCMzk5VH6Zdgu91Etr-YNEtah4grH-br4GMYcj5pg8xxYEJufWpfqWJK2078ohDEPdmL7oC-CdIEueuENtAckS7lpFKm4tSHE1chPIzEXGKIKFFhFgYyx637palT8tSwq4gaqRheSVG4tSZ1M4b8h2mLqouY-x_TqeRYegmJUoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
