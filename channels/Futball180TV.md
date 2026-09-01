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
<img src="https://cdn5.telesco.pe/file/fIG_5VExzUQQAmoxnmEfo8a0FUp6HI_KBf7L3h6-IpMBO_EynZip0hItmUlUcSmUsLtPicqcxg1ZYcgfpu42bs-Sh50OGPnrA8gY46AoCpdetsw2dtULYun7D8BQzh1CtQ022xcn3FyzP66BuaJDtkE2IyXNgo0_ahKOxh8NHJvKdTs1nT21xDnoV1hx-CxprK9T-tA_sce86jwN46MKO-uvhqoqGz87DXYGWXe5jBEP3Yxg5ZHlgr3HgjbVJG9WFnbc0B3ezCwPuiawcCkPI79c4oMRT9G8rS6PmXMrHL6Wiaw9iTgUZBJPZ_md-QKUKC7s4ASB2msdi33YhQYYfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 432K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-105264">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=Zt8xZbLC6TrlgdYgBKIIwYG5ZERQl3BbU0OMlYuNeLmzua-H26z1Jz17eb3x2431vxuruIjLMD4DbN1GSvWJ-KfcCVRqD0a_UTbOHJ6TK20YVzO17HU9nwbNFLLauqamhKGJ71GMWEWwvdq7V58o-y3WfgT73tY5C6BnOIhY7rLefYGWds8nP4ilKKMZlYOcs1MRQNV0cDPWkE-9K4VtN1dQ7ebx5LDAvnTyvG9FTTmWMVhbjGeFI4pT-PSQc6YSy3-ZEZsEDdEwYgqOTnL5yhSPX_s7UMxHbf7M-rsfLipoJMFS86aUMs1cOeIOzQCjB7T0WRgVIfjdF90mUunfRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=Zt8xZbLC6TrlgdYgBKIIwYG5ZERQl3BbU0OMlYuNeLmzua-H26z1Jz17eb3x2431vxuruIjLMD4DbN1GSvWJ-KfcCVRqD0a_UTbOHJ6TK20YVzO17HU9nwbNFLLauqamhKGJ71GMWEWwvdq7V58o-y3WfgT73tY5C6BnOIhY7rLefYGWds8nP4ilKKMZlYOcs1MRQNV0cDPWkE-9K4VtN1dQ7ebx5LDAvnTyvG9FTTmWMVhbjGeFI4pT-PSQc6YSy3-ZEZsEDdEwYgqOTnL5yhSPX_s7UMxHbf7M-rsfLipoJMFS86aUMs1cOeIOzQCjB7T0WRgVIfjdF90mUunfRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
⚠️
واکنش عادل‌فردوسی‌پور به حرکات منشوری شجاع خلیل‌زاده و عارف حاجی‌عیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/Futball180TV/105264" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105263">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=cFo54OXtBSx4xZuVo_XzfJEBdcWQiYTmGc4UycDhwPVxoX2F_gAZV1DkuQNmxoTSmzXF2j6KXN_tNin4XJ1yCMuo9pzDjmk2X55ux_tZjTqzg6SxfXA_2S78jktF7YrT91WW-e4pDRv-EyFodx21TeJlO4YbdRF40iZm0ly4Ndf7dc6TW9univBgLRP5lQsxj4UDM_K_7YLg1T-cMkKNd-SfZ0x7SBWeoRBkUjj69OTeFbXadx7YswhvFPk_yHhGz_IbLLUYc0aHbN0VT0IGCpT4hqfr8lXJJz3ZN7YPjlpOkiBkRGpqJWxvEfJ__RrxGrWrCHC-zNT10QPBbEdrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=cFo54OXtBSx4xZuVo_XzfJEBdcWQiYTmGc4UycDhwPVxoX2F_gAZV1DkuQNmxoTSmzXF2j6KXN_tNin4XJ1yCMuo9pzDjmk2X55ux_tZjTqzg6SxfXA_2S78jktF7YrT91WW-e4pDRv-EyFodx21TeJlO4YbdRF40iZm0ly4Ndf7dc6TW9univBgLRP5lQsxj4UDM_K_7YLg1T-cMkKNd-SfZ0x7SBWeoRBkUjj69OTeFbXadx7YswhvFPk_yHhGz_IbLLUYc0aHbN0VT0IGCpT4hqfr8lXJJz3ZN7YPjlpOkiBkRGpqJWxvEfJ__RrxGrWrCHC-zNT10QPBbEdrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دخترای جنوبِ ایران
🫶🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/Futball180TV/105263" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105262">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7EF8RGYBG539V4ZDMhcofGPxUeRoKK0A3cEXqctF989f-xxt2XXNqusb69o_HYLUjkXQIIt7t2cd5_GNvjbFYXYNjG5vbfUTuOy1rjf-B_4vZSOswH9GnZejMfnrDGdVJigOv-MbzRsHP4B7nEXTnvgmOMFOExkha9Obb2dzvMkA8b901py-cwIOlW2qtXykEbw6YinTcFmzGpqW0Brf-NhjPmpAN2WtEWPZ4TfAyy55meCizxgDv4xyC5jyPrngV9RPWjEAQQ2J7WK7ubrRmypbEvIjU8EH-TnPYGOGbmSiQGO-cTSuZUO-74NdcCtvzASayJbdf2bKEAGL8MfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
هوادار بانوی تیم‌فوتبال تراکتور تبریز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/105262" target="_blank">📅 14:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105261">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93b254714.mp4?token=qlRrRulvqfLTwHw6xorT4XFvQDlYrco4SO_jCjBL7fsyrZAYzT2YRfvhSDKrYLZyCEXc9J5h8pnESAYcQvWToOtDjtxkxalruV7-8_qOjJ7-W7g9LvF30VYHITNLLcm-ESqc6qWaEhgU1vZB9jjz8ZEAXGwYPDhQmrKNhh7Mm3OOqQzdvTX9rHp0-cCtsxAjWh17C-chJSfrU_OX7uR3PfSizDhjzQt59GItqjmNYwiUfE7UrVhws1FmQsSOfIictZzBR276reMeSlqPpOP1IfUnscdgNoNXj1Tbe_fQDB5S8nJBiriTRcAWL7l8RxSszGNifGqI1qydHuvGCGuTNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93b254714.mp4?token=qlRrRulvqfLTwHw6xorT4XFvQDlYrco4SO_jCjBL7fsyrZAYzT2YRfvhSDKrYLZyCEXc9J5h8pnESAYcQvWToOtDjtxkxalruV7-8_qOjJ7-W7g9LvF30VYHITNLLcm-ESqc6qWaEhgU1vZB9jjz8ZEAXGwYPDhQmrKNhh7Mm3OOqQzdvTX9rHp0-cCtsxAjWh17C-chJSfrU_OX7uR3PfSizDhjzQt59GItqjmNYwiUfE7UrVhws1FmQsSOfIictZzBR276reMeSlqPpOP1IfUnscdgNoNXj1Tbe_fQDB5S8nJBiriTRcAWL7l8RxSszGNifGqI1qydHuvGCGuTNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
بدون‌شرح‌ترین‌ویدیو امروز...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/Futball180TV/105261" target="_blank">📅 14:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105260">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=NQFFdVXcQqZDeeYUYKS0Pel4fZUuL2pUpynQ9ERhY0GgHciQNMxAz0clePKCOKFdYXnJ7Cg_vuSRJFFJQLNHw_ru3sC7JWPqkPxv1cxx1ZVIVIXQoD1Tkp0tZp1oYQ3XNpqddztMl57-KmpA12bXXGNKmoJ6GOiu_mEqy45W8LS5BZ6JE3wcRkzMxitHSe6SKcYDYm_G4o6DphNWuJQD-IYF-YHCZnyBNyQMhTC8uTbPW8nVxlCr9Piiq-EllexwERqyYJ1mEz-4gMEILDmZV-V5Jj38H5z4Jq10z0CHyEn16C2Y8zj8f41SjOlB8Do7LXhp4gyOh68Rr0yY95_cvbgJt0VSH9ZQTjhE41ZDkM7YkDYTefjOYB0C33EuJCPcPHqyeGsSV7l4hgodVIbUKJWO442RaCJO7cSiFWp-tBOJ5eg0_CzqBjzK1wAek1recfMuiJz2uvcSmtIXXX5EFQwRx972wbq5LELNL0_I69Yt4ZJ45vRoN7Xi7ru-pG0yMjFYSzBIWoyRe414C-dWodqgSzd71S3REboZfyrkh2XK6FBcLkReykQ3MEj-53c9Z_kg3AZs9gEtIJ7mY_w0rlgTptlvwPynccbx5bOH7wvJb49WhRvcFB1lSrt43AXx8q29-ZJNVJhka4kfW6zlK6QiWI10qW44CEHncYUj_v8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=NQFFdVXcQqZDeeYUYKS0Pel4fZUuL2pUpynQ9ERhY0GgHciQNMxAz0clePKCOKFdYXnJ7Cg_vuSRJFFJQLNHw_ru3sC7JWPqkPxv1cxx1ZVIVIXQoD1Tkp0tZp1oYQ3XNpqddztMl57-KmpA12bXXGNKmoJ6GOiu_mEqy45W8LS5BZ6JE3wcRkzMxitHSe6SKcYDYm_G4o6DphNWuJQD-IYF-YHCZnyBNyQMhTC8uTbPW8nVxlCr9Piiq-EllexwERqyYJ1mEz-4gMEILDmZV-V5Jj38H5z4Jq10z0CHyEn16C2Y8zj8f41SjOlB8Do7LXhp4gyOh68Rr0yY95_cvbgJt0VSH9ZQTjhE41ZDkM7YkDYTefjOYB0C33EuJCPcPHqyeGsSV7l4hgodVIbUKJWO442RaCJO7cSiFWp-tBOJ5eg0_CzqBjzK1wAek1recfMuiJz2uvcSmtIXXX5EFQwRx972wbq5LELNL0_I69Yt4ZJ45vRoN7Xi7ru-pG0yMjFYSzBIWoyRe414C-dWodqgSzd71S3REboZfyrkh2XK6FBcLkReykQ3MEj-53c9Z_kg3AZs9gEtIJ7mY_w0rlgTptlvwPynccbx5bOH7wvJb49WhRvcFB1lSrt43AXx8q29-ZJNVJhka4kfW6zlK6QiWI10qW44CEHncYUj_v8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
دیشب‌کریم‌آدیمی بنده‌خدا فکر کرد چون ۱۰ دقیقه تو زمین بازی کرده دیگه بعد بازی نباید تمرین کنه که دستیار فلیک این‌شکلی کاسه‌کوزشو میشکنه و دور تا دور نیوکمپ کنار نفرات ذخیره تمرینش میده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/105260" target="_blank">📅 14:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105259">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=lTzcNW0RLaL7KGyy31c0cQ-YskdQ14X4Nu-GG7lMtvYJdHvN-6OV0aTpf6CyD0FlruH0S7atxdfQ9pto1gzzGKNI-DHPokvhVvcWT8QvMxuCFyK8oNjg7j-hfTNR89WNlf2-vQ1QzlsYVfnIp7x33z-YaEZ9V3cIWD62kgOXP-96-W3YnV0-WDMBBO9xbArwNz155yG5lVlfIVFeodgFF1Yaqeo_xI8THNesjqNVLlH0es-kjgy8P0YOhRaDMIq_InmmXxDgHzp-60cnwNyMPHV_y6dTZgDulGHcKoWRuT55MIRQZDCsTVImJx0-7ENW6T_Npji8YQK0UPlH5O31SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=lTzcNW0RLaL7KGyy31c0cQ-YskdQ14X4Nu-GG7lMtvYJdHvN-6OV0aTpf6CyD0FlruH0S7atxdfQ9pto1gzzGKNI-DHPokvhVvcWT8QvMxuCFyK8oNjg7j-hfTNR89WNlf2-vQ1QzlsYVfnIp7x33z-YaEZ9V3cIWD62kgOXP-96-W3YnV0-WDMBBO9xbArwNz155yG5lVlfIVFeodgFF1Yaqeo_xI8THNesjqNVLlH0es-kjgy8P0YOhRaDMIq_InmmXxDgHzp-60cnwNyMPHV_y6dTZgDulGHcKoWRuT55MIRQZDCsTVImJx0-7ENW6T_Npji8YQK0UPlH5O31SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
عملکرد پشم‌ریزون دیشب لامین‌یامال برای بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/105259" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105258">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=BcyMTYFotNJc5B8KInKakHPahpEZv7azpNKip1JCI4m5c92mF4NC0yJ_SxJ3-KYNYU_XcWPWLkBoXTKrKEyNgbkl7D14IblYTG7zVEr-gLNxj5euBVEXEisZOnOJt67jnSIFVpy7NkSQTqYum_dWjVdjs0f5U0l0kfiquttE8A0L_oLpLbktWUlB3Y6vzBz7NrmCiByfP8cmslD_M0MCx0vjEIioLiumDDVoLXR1FvpQO1iP5MT2NDgBuW8Yd5Zxk4ut5ygz92fV8rn0atbCooOEjV0Aq4ieVMKsUcfVLK67cF8_ZZaS5TvgMAX5pPPbCunhC-lxcnCRMlAflVczIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=BcyMTYFotNJc5B8KInKakHPahpEZv7azpNKip1JCI4m5c92mF4NC0yJ_SxJ3-KYNYU_XcWPWLkBoXTKrKEyNgbkl7D14IblYTG7zVEr-gLNxj5euBVEXEisZOnOJt67jnSIFVpy7NkSQTqYum_dWjVdjs0f5U0l0kfiquttE8A0L_oLpLbktWUlB3Y6vzBz7NrmCiByfP8cmslD_M0MCx0vjEIioLiumDDVoLXR1FvpQO1iP5MT2NDgBuW8Yd5Zxk4ut5ygz92fV8rn0atbCooOEjV0Aq4ieVMKsUcfVLK67cF8_ZZaS5TvgMAX5pPPbCunhC-lxcnCRMlAflVczIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
محسن نامجو مرتیکه دلقک در کنسرت نیویورک، شانزده شهریور سال ۱۳۹۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105258" target="_blank">📅 12:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105257">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105257" target="_blank">📅 12:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105256">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مجتبی‌پوربخش: تا جایی که اطلاع دارم، وضعیت جسمی علی‌کریمی خوب است، فشاری بر او وجود ندارد و صفحه شخصی‌اش نیز در اختیار خودش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105256" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105255">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLZD5ahOk3unTZpmLTTZs9D9PxZ6YBygnrVfwzUIL2C6jwFgeY0-nlWjyB52GPqLIKIn7UCic9-ljFRDHhLjE53bQEcuJkjKrJTQqNhxga3Tq28cwDsRMXfoafrmpXgd7f863NUMmXee2xWI0Igz7R-s4Z-SALwl_sPGFuXM5XSF2pOYbKWlqm-kwj_bGh0R1749Q2rIdlwa01hIfjA_CMY2VdA_FOOR1mdPbWdmaMhcVWN8TosiuVYF6Vcue-vIMfv9Ub5nrPw1U3ePGrg9J8g-Yfwc3n-RWnm4LgoIYtJGXHDpmH5HN2Fud8_G0XH6dD5V-UO-Mjj-pmjZsyaC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
نتایج سه‌بازی ابتدایی بارسا و رئال در لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105255" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105254">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=RIKYLxa4Bctf2cSssATKfdxEXlS6-34suTZUJ2zI0c8U_fZ1BS-ZUSK-2uBEI6xYzg0UuasnaVh8letyJkkcKmBY14ED9DIPVr-llg_un8yumZ34T3EM-2FkJfQfmS4t1ecTArNAMPaTP4rwS1Sg3WfWyCfNov4DVLyClY9DqoHyJvtDMovdOUqU6n-LmiJS8k3WeD5ybcfZjgZS7Gm6v9tm6bzbc1lxxf8qV3b2BBtipLdCjbzaYz6mtL5zijV62SfG5nAPz7EqTr3xhESTbxGE3kr_ul5UHco9TlJDYT42pWdn_xg704VxC_rWoGtbs0qAYHyh307aZ6VFQBC6ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=RIKYLxa4Bctf2cSssATKfdxEXlS6-34suTZUJ2zI0c8U_fZ1BS-ZUSK-2uBEI6xYzg0UuasnaVh8letyJkkcKmBY14ED9DIPVr-llg_un8yumZ34T3EM-2FkJfQfmS4t1ecTArNAMPaTP4rwS1Sg3WfWyCfNov4DVLyClY9DqoHyJvtDMovdOUqU6n-LmiJS8k3WeD5ybcfZjgZS7Gm6v9tm6bzbc1lxxf8qV3b2BBtipLdCjbzaYz6mtL5zijV62SfG5nAPz7EqTr3xhESTbxGE3kr_ul5UHco9TlJDYT42pWdn_xg704VxC_rWoGtbs0qAYHyh307aZ6VFQBC6ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
ویدیو زیبای و دیدنی حمید سحری پس از اعلام خبر خداحافظی اسطوره لیونل‌مسی از تیم‌ آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105254" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105253">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105253" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105253" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105252">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqXmoxUThp-PPfv8cbCxBVx3_l5AbJoQW1iPgi4KXWYKzj1QX_MVKHd795hqf2-71G6qK7oDoHfnGxgp1OdZh2Sd8OLUfQ7up30FIwfqw362-UesNHQQSMuUicCcHfzUQ4-qMCN9KOTdTq5SUOVaQQLWjV0DYyuxfp9k9VYf8GXq7xiLvSYTIdJXsUbwdcQZCr3oiBCx0jzugTqXhVCFd0H8cccCe76jm8HrgiW2Kh__fUgv2dIoUYuDymtAZrcBLukWWPSahb3Yjl1yHKi0Q0VbtH2pA4RIJXzmnmqWvfZcvNEzE6BZnSpLg6jnmFsTti1I2gxiFbsDLvYZgOwkUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105252" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105251">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=oOJss42oCF0BUY2O3BRWFNrNg9eZKSEoPSJvSeMdP2KrvfA-uqLqe3Eg6uMqYSV3AjRTI90T_pKB-PRVOQsq6mBXbh_s9cNh6AOOsRCpiFinEK_BCZNBpNGolNTWwkkYtQ0Tx8Rik2UsvMK9osYrw6Kc0_Q3BR43kCp5tQ0EIqcZoxOcWxRlgSH2O_a9etcl5Gns_ByuJ_9qScuifxBSm0D9FATXyE8YgI7J2JUIlM7J8J-G4pC08iIgsKl3ETF4OYnCt3zXrSp6qB5WGuOUwwsphbnCA-aFMHOjsDPM7C_4K-p7kn4GByez4EVmWnmP_qTTp1fuSQzBcqLl-2UDog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=oOJss42oCF0BUY2O3BRWFNrNg9eZKSEoPSJvSeMdP2KrvfA-uqLqe3Eg6uMqYSV3AjRTI90T_pKB-PRVOQsq6mBXbh_s9cNh6AOOsRCpiFinEK_BCZNBpNGolNTWwkkYtQ0Tx8Rik2UsvMK9osYrw6Kc0_Q3BR43kCp5tQ0EIqcZoxOcWxRlgSH2O_a9etcl5Gns_ByuJ_9qScuifxBSm0D9FATXyE8YgI7J2JUIlM7J8J-G4pC08iIgsKl3ETF4OYnCt3zXrSp6qB5WGuOUwwsphbnCA-aFMHOjsDPM7C_4K-p7kn4GByez4EVmWnmP_qTTp1fuSQzBcqLl-2UDog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
🇮🇷
فرشید باقری: خداروشکر به پرسپولیس نرفتم؛ آبم با آنها تو یک جوی نمی‌رود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105251" target="_blank">📅 11:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105250">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=JF8-dCqwacFNX6G6vgHbt9zMsOdCfEIevDb4O9FMc1wsCzTPsPAhjzGDkrpM3j3F1KWvMyMY3X_zwHATb-4nlIIjsbqvS4n56y6_QB7YsvsNETNhOODVyj-cq4jSfHFFMVi_P-cdabWwxw81zlGlljYSzuydbbKRHsMjTDmzLktaAiJv25zuHdVT-MLvmLb6GDxCCPQvgW0AJePrZkqPHr8Rg2zKvfqQy_y9tlr6WURjkTBrXC9Ii9VwlDeKSHMYGbLWTQaxnphJ9qlaXrLnO9A_T4VAImZZH81wZcUEmPrXB3E9ZYRRThV7OLMM4N445Lahd6OfO6GYWw5K6WkoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=JF8-dCqwacFNX6G6vgHbt9zMsOdCfEIevDb4O9FMc1wsCzTPsPAhjzGDkrpM3j3F1KWvMyMY3X_zwHATb-4nlIIjsbqvS4n56y6_QB7YsvsNETNhOODVyj-cq4jSfHFFMVi_P-cdabWwxw81zlGlljYSzuydbbKRHsMjTDmzLktaAiJv25zuHdVT-MLvmLb6GDxCCPQvgW0AJePrZkqPHr8Rg2zKvfqQy_y9tlr6WURjkTBrXC9Ii9VwlDeKSHMYGbLWTQaxnphJ9qlaXrLnO9A_T4VAImZZH81wZcUEmPrXB3E9ZYRRThV7OLMM4N445Lahd6OfO6GYWw5K6WkoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وضعیت سخت‌افزاری ورزشگاه اولدترافورد که وسط بازی از سقف ورزشگاه آب میچکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105250" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105249">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtfeWEUrJJnzvNR5q3S9ET88mwzSt-YzULrf5W5P7cmIKmhlQ45kKsz8skxzzVMI9d_MgQeIevgGnpXxnBzHrJB5U64lxsEf_545MyENjrRQipSYUL-_B8YNlCDvDemK1BN17PIZUg4DJNInnRwSFlvbKRNVDtP3YTxSQ5mYFIRvq1mnXkVPIEZrKA3EoN9Q5pwx-jlcEMfkEJ14H46um9-hYhoBb2dcLL9s_LpxCV1DCko_xcnQeyNwzIAz11HeFwyoF--tjWSLyfX9qOCSLYOA6kkyA7kZD8jKsPsyWqjcoK7vvudCxFYvSp_qjPyieGm_ol1ZiJgmzuOmK-_pGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105249" target="_blank">📅 10:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105248">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=LeI822OoYijQjLm2bQDT2zrydv5-F5zYnRkc37Yq1pnQynH7qhE7VzSrdBGjkFdMy3u7M4OvoEvnDsvZ8PP5WVU7__EvgQNkqgopItkynVW9WJ0_gRJy85KIpbmx6BL6H2adkl3m06_jAoEb37MF6UYD7m2l14EGxlMw0V2ISXoYoqGxtEKCa9iyIiJzgy2gEtKQP0gI4e6zouxH1wUYZqO75ymIYfR8verRUl-RLnJEwxx2I159R4slgmwLVm5FU0rfqGRpPlL6l6rnYBOVl4j52DEttOG2dPmj1RLbnm4LgvISPrDyHJ2WlCUXqasOGZTNkxia8QF6gzxgh11Prg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=LeI822OoYijQjLm2bQDT2zrydv5-F5zYnRkc37Yq1pnQynH7qhE7VzSrdBGjkFdMy3u7M4OvoEvnDsvZ8PP5WVU7__EvgQNkqgopItkynVW9WJ0_gRJy85KIpbmx6BL6H2adkl3m06_jAoEb37MF6UYD7m2l14EGxlMw0V2ISXoYoqGxtEKCa9iyIiJzgy2gEtKQP0gI4e6zouxH1wUYZqO75ymIYfR8verRUl-RLnJEwxx2I159R4slgmwLVm5FU0rfqGRpPlL6l6rnYBOVl4j52DEttOG2dPmj1RLbnm4LgvISPrDyHJ2WlCUXqasOGZTNkxia8QF6gzxgh11Prg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری شب‌گذشته داشعلی‌منصوریان از فساد شدید در ساختار فوتبال عراق
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105248" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105247">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKIeLhA8u0quiLXa2A4cZNBgp3DmpZu4kNv-wL6bpne1Ddr3_U4A5bYxHRp1B60ZuJt-OOX7D-pwOnHhxg6k0Luznr-IiQz1E7TutgsTPhA7PzvQlOYA9iTViTpl4KhH7R0Y3UXaElvgxi-9o6_s849QqB6880ONyjyHqOI-oX9RQgG5ptjkkGpsRXwnB0LiHvCG-MBZ_9NXwvumaKhgjW3rqOKsCihTZwoJO9oZA0Q__JcYv3cfm_wkcXyl6I1LA4ps13TamEFSZfNgXZsNHhUBBBZPQln1MZI1Dwrewcdl7v97gILG-_rMrO5RHvBX88wDMKwbrfZdbAy9h9ToJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
با حکم کمیته انضباطی، شکایت دو تیم سپاهان و مس‌شهربابک از استقلال بابت بازی غیرقانونی یاسر‌آسانی مردود شد و این بازیکن مشکلی برای همراهی استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105247" target="_blank">📅 10:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105246">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=PgnHrcIpdfSOUTRtZWgmf9iGgy1zDMehO69CbAtv6BsCAYCFLtQXybBGwL8Q4PfOn60KajfuRnrMfPxpMnj4UdLGkEMAxVvP0wCKWemDu1Ck1f7kKkPdoWaCH1pLgxOVMX29b4KSeQowAkLe_UFPuKVLkZn_MkHj2RijY--wKbQLgkK2wVIZ6qwLPslB7Rl1J5sWJAtnRFOtmOnyGD36-rWhakCfLqX7I6vdB_tcSLzR4P4qCpnM3p3nynJpskoICmaTPG04YHT_1C2fesjoof8BINUXaIczaENdniPUrWsvjCHjOh87AWsFKYIjDIwRbepRzqx879ti0-F2eRVi4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=PgnHrcIpdfSOUTRtZWgmf9iGgy1zDMehO69CbAtv6BsCAYCFLtQXybBGwL8Q4PfOn60KajfuRnrMfPxpMnj4UdLGkEMAxVvP0wCKWemDu1Ck1f7kKkPdoWaCH1pLgxOVMX29b4KSeQowAkLe_UFPuKVLkZn_MkHj2RijY--wKbQLgkK2wVIZ6qwLPslB7Rl1J5sWJAtnRFOtmOnyGD36-rWhakCfLqX7I6vdB_tcSLzR4P4qCpnM3p3nynJpskoICmaTPG04YHT_1C2fesjoof8BINUXaIczaENdniPUrWsvjCHjOh87AWsFKYIjDIwRbepRzqx879ti0-F2eRVi4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
‼️
عمو رشید دهن سرویس درکی از دیدن برنامه با خانواده نداره
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105246" target="_blank">📅 09:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105245">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=oS6Go0P5i0hoIUEfRKkKHpHjQzpSDNGK7d0PJ87A3L4GAkFNHGitf_j1P9X50JWUyXxNn79sE8YTN72bpfu-Pu0TGKBmzozlpPQ3TbSQ2NBTddrBYQNrh5zaRwJxhPBN2gU7wWlTVMJwU8NzkgyjOJdrczrpjoINFRj0aAVHcWM_feXHZFMkp_XTG1TOoNRUVn2QRgxAPQiu6KdRXLhOhg6EU6pMCujqrLjto9TqhfULEAMC7NsmXeFB_7PBNzC2ElT9R3CxntZx5QIiKyuYj1mtP06qijebsdeL-VlCuLLk05v1TUPk4imfc3cs0UTQvS2CPY0NyLolQrNmTz1AHELEoSOBPkAd_V39a76UupUicNBuOryAlO9NDBDwsqhLhFvUJa7dr1FTvHRRC7Q8nLI8adSnDEHdrhEUOOK95Hdx9MEdqPwvgJcG-wKS-guck6E01f0C9xKYGo0S6T14jpEpPuuHyzJGA5SDi9u7EvZuEt8zh8hIW0zxggDAFSRYJQVDcIpTglXEyScslJx_5uhkuo1hrJ_Es0lMZf2TFS-ZgCL4b91U9iCR5Mz7rBNXy4gKdqZImo_qPqVLuEzdDDghmbf3_6v2-GV4f-EC5acqEBzaUKeratZ_VqNsX9Tcp1kG_NBai0NF6i89XrIiaw84RJ7Cm7in5EXfgz2jiAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=oS6Go0P5i0hoIUEfRKkKHpHjQzpSDNGK7d0PJ87A3L4GAkFNHGitf_j1P9X50JWUyXxNn79sE8YTN72bpfu-Pu0TGKBmzozlpPQ3TbSQ2NBTddrBYQNrh5zaRwJxhPBN2gU7wWlTVMJwU8NzkgyjOJdrczrpjoINFRj0aAVHcWM_feXHZFMkp_XTG1TOoNRUVn2QRgxAPQiu6KdRXLhOhg6EU6pMCujqrLjto9TqhfULEAMC7NsmXeFB_7PBNzC2ElT9R3CxntZx5QIiKyuYj1mtP06qijebsdeL-VlCuLLk05v1TUPk4imfc3cs0UTQvS2CPY0NyLolQrNmTz1AHELEoSOBPkAd_V39a76UupUicNBuOryAlO9NDBDwsqhLhFvUJa7dr1FTvHRRC7Q8nLI8adSnDEHdrhEUOOK95Hdx9MEdqPwvgJcG-wKS-guck6E01f0C9xKYGo0S6T14jpEpPuuHyzJGA5SDi9u7EvZuEt8zh8hIW0zxggDAFSRYJQVDcIpTglXEyScslJx_5uhkuo1hrJ_Es0lMZf2TFS-ZgCL4b91U9iCR5Mz7rBNXy4gKdqZImo_qPqVLuEzdDDghmbf3_6v2-GV4f-EC5acqEBzaUKeratZ_VqNsX9Tcp1kG_NBai0NF6i89XrIiaw84RJ7Cm7in5EXfgz2jiAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
افشاگری پشم‌ریزون عادل فردوسی‌پور از ریخت و پاش چند صد هزار یورویی مسئولان تیم‌ملی جوانان و امید در اردوی ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105245" target="_blank">📅 09:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105244">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=q6DI3gU3sOv2Y8EWPgZbCWPmEjb4wx3PBV2gf0_hbXX3NWmTk9QPT3738nB2-_5_biXZMMpF6wCQPngaE9nmJCYU8pRBjxM8OhiyOrgNttTDYMTVUGiRAI5R-Lb2j7xgCrIdVxWs4BAxAXoAOUCjxyZIHXUz5_iQZtB5a4qAReoMPbjrEjxuS8a7QR2eEPS4fOFcSFNBlxa5L0G2pOPqvFGXiQMHgHTrSSCAuE8-E55OuxDN0WGjzFzPHXWDJ_ezWVL4Rn5zyz5U-DAHvI6Y7KyvSkAktC6iDvemtpxFPSV2UCZ4gMdY0O_cvrwyv6e561z_z64MI74TWFAvSmwsKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=q6DI3gU3sOv2Y8EWPgZbCWPmEjb4wx3PBV2gf0_hbXX3NWmTk9QPT3738nB2-_5_biXZMMpF6wCQPngaE9nmJCYU8pRBjxM8OhiyOrgNttTDYMTVUGiRAI5R-Lb2j7xgCrIdVxWs4BAxAXoAOUCjxyZIHXUz5_iQZtB5a4qAReoMPbjrEjxuS8a7QR2eEPS4fOFcSFNBlxa5L0G2pOPqvFGXiQMHgHTrSSCAuE8-E55OuxDN0WGjzFzPHXWDJ_ezWVL4Rn5zyz5U-DAHvI6Y7KyvSkAktC6iDvemtpxFPSV2UCZ4gMdY0O_cvrwyv6e561z_z64MI74TWFAvSmwsKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو خواهر پژمان‌جمشیدی از برادرش در بدو ورود به کشور کانادا پس از رفع مشکل ممنوع‌الخروج بودنش بابت پرونده اتهام به تجاوز !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105244" target="_blank">📅 09:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=lxrTYq_f0ZHcBQ_jrHsFvN4an4GbpfOpmc4o2qRzqCsVmd0daY6F6J-k6gmvLtDpN8TPSj7G-d6E9EPaCdi6G6Xkta_jajy1l8fZRuwfdzi-QKNJb5-A7d5EUcO4PNfamS2wL3M2KraOa5qQKSBShvvk-9YxnrDWKSvQIEvWjV058n0is6zSTt14nNhaeCVt8DVwfNRkbyUNAKJnxojisLDM6mVFjCaW4zTtVH7d6RlGlMl_li9vlD8mhhjYnDeh1k5HQ6y4_RcNpw-3Zs2isF5p5dJu2xC4K7c4KChS46b_lw5KGgThS1eEu7AX4T_zOtcle05c1HB4kKCAFJVoag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=lxrTYq_f0ZHcBQ_jrHsFvN4an4GbpfOpmc4o2qRzqCsVmd0daY6F6J-k6gmvLtDpN8TPSj7G-d6E9EPaCdi6G6Xkta_jajy1l8fZRuwfdzi-QKNJb5-A7d5EUcO4PNfamS2wL3M2KraOa5qQKSBShvvk-9YxnrDWKSvQIEvWjV058n0is6zSTt14nNhaeCVt8DVwfNRkbyUNAKJnxojisLDM6mVFjCaW4zTtVH7d6RlGlMl_li9vlD8mhhjYnDeh1k5HQ6y4_RcNpw-3Zs2isF5p5dJu2xC4K7c4KChS46b_lw5KGgThS1eEu7AX4T_zOtcle05c1HB4kKCAFJVoag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های عادل فردوسی‌پور در اولین برنامه فصل‌جدیدش پس از حواشی فیلتر شدن سایتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105242" target="_blank">📅 08:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105241" target="_blank">📅 01:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdFVJlUBRpo_vp_I-kGaf5ySDEBdkqRGpa8QrOPbIJ1qJjX53kvxOLbuk_rm1F5UXk_jrSHPsDgJzZjoqhXJWte2A3OT0aUyRu5L163DSmP-rx43OJzb3BtKNIi3rXEiRFFfcP4jDfq9lzrWyER29LyWJDC_v6I-Si1Q0J2UPzokV5GMHf9nxdVsYbsi8C0BHE_NSm-Y5BAGuZvLDvEb_XMgjUfegoIPGwgHei2JmCqcJq9atLTczl0yrok5taw-p6EsOkKyDmAQJUEKT_8T8NBO9S--GzQJ7_ad9R4O5fO452y6zcM1RYJh9mfC3RqHjqnrncs_VYGwB_H32tjgnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105240" target="_blank">📅 01:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105239" target="_blank">📅 01:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105238">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frpGRetLOPGoH9_UuwH0_sJ_qeSOZBuz82B0x9AX20oxBGBrMlPw_PMA9ROO1LFItajN8muMeclQot6-epGOWc6jqRu-F4FVenT0m6q6vrbtZyR1g0VwXNFY6Ysb3SKubKePxj_XwmhMgsJE8vg1ihZgL3GJPcdox18kEDxeaiQfhBTgr-5s9hSm4CRt54P-9fvZgl_buLQ7xcbrxuAQgO8MbXeOGb5Zzf5RGLRIGV5vEJ-rAPYV4aE2Sc5epLahLuLPE4B0K8_9gcM9HwIbrPIFx_9mOAxjmzzwPX9B6toy9HhwXEV2izzQCdligiB8a5TeV521Vs6Lji5aNCSOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیك: 91 پیروزی در 120 مسابقه با بارسا.
🥶
ژاوی: 91 پیروزی در 143 مسابقه
با بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105238" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105237">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWl37jXyBrR6U_sNjZHdtv0w2Dc5X9H9k_5s__mZlOX3AOTmWfjH8denzAZ7QA8DDhiZDA9H5i3RO8rkg60W3cTi05J_7wAEePvn4gODUCoQDkimEFunLdjCRzUCA0bS9PUm3C8ZkDggxzhL25fswWlXxhU1Lm86pX1ga8bageC7YPc0doY5YPjDndog8GeLgju86U745wnzjPR_Cc_dsdpmE_gMRmBMp-eywtGzbN2hysr38bmyRUqwCvCCGjhVE50-thnV1g1YKKwhpcWh3P6MKVha-oJ9jbKSwVjribtg94WTEIk60vqBAjZneB3J8xU7nWB3LOoaWJysX5pDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: مودریک از چلسی به تاتنهام با قراردادی قرضی HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105237" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105236">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNSiY_amiQf1Do2lM92AVxL-mz4aupIrg84VICMI4Kg87mZr5C4rZUnfu97hzzzgypCHfs3dAag4AgneeGcvP5qDpzd5JzzwRcxppQrhN10MTTgTbirQbtEILrBp0T-y_3GVwhn40n3JSDkNeBzaVFZUVpXaxENgmaHH77TWDhfTMHDqtlNeMNVvSyg-W6-6v8tEtnb3pbnTGnyZCMjM0d4HvVRYq_2MqLrrq3UU2sPRzTd5He8JD1SwL-I1C8kJ4-HQAB5jOVrSyOs33fujEWoSNUpS7U0nwLR7cv2U4I2gWLC0OGWO4eJUNIinjsgnhWqq36GFJsGCEVA2Gg9k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌سوم لالیگا؛ بلوگرانا روی نوار برد؛ پیروزی پرگل در شب بریس رافینیا و‌ یامال
🇪🇸
بارسلونا
😄
-
😀
رایووایکانو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105236" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105235">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">لامین‌یامال دبل کرددددد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105235" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105234">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بارسا پنجمییییی</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105234" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105233">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گگگگگگگگگل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105233" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105232">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105232" target="_blank">📅 00:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105231">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی استون ویلا 0-1 آرسنال با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105231" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105230">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/939ced1d89.mp4?token=r1h-ezJ_82WxAIr1cOKfxZtllfB2TjfPI5z5Q8NsGoiFj9FT5JRUmV6VEWc-z1pg0f76nGtgjxmdfvHbP4A9NrqedyK8tLXMkeShpDavERR_tcXhQnjBdvskocx5npeG-Wx6oAbYHSi3njIB__WX_W-jBAIcHRbX-uecVny5rlGxVNhVkKd4Cww-lZW94TeRumZJEn-ztKtWmVgfofR6MVcq4stUBLfcWNEYKHIRCwhMx8J3XuIMhNP3_IR9_hu1teGgjQGzE5z2NuSJvDVc6uP069DMpJIvLaA7o85kpJAPPbjfqvW7FKd8zzVMcpKLzwMjkbkT6KBnbU1rR29gc7W8IkFcF7_Vq_fkeeNz0HTqFdN0WQg2-q4lRZtYkew60snOx9wr41p2FvFwSDQBRAg9T4qALCiCEzZrxZkM7FYnDHhd9vG49b2JcfIKC-cb4Z0pBrYxy9EWFrp4LYoOy9K6Khc3-AlV1KP4mEO4Bkn3UZqrHqr0Pcz_S0YuROi5eF0N11VNHq3BZz33zIUHXCZ-3e71NG4J-07kT6caDmzMIr85VpJpZcmLJvSbLzTNxJWlJBLjQJZSawjsj3CeDpolVEk8Ys_uiESGN4VgtdmTzXPU-qGhrSqHVX0-Ygzq1UyAHg7H5ZoMDXz2H8Djbz6RYjOxmYEgew2rkR707P4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/939ced1d89.mp4?token=r1h-ezJ_82WxAIr1cOKfxZtllfB2TjfPI5z5Q8NsGoiFj9FT5JRUmV6VEWc-z1pg0f76nGtgjxmdfvHbP4A9NrqedyK8tLXMkeShpDavERR_tcXhQnjBdvskocx5npeG-Wx6oAbYHSi3njIB__WX_W-jBAIcHRbX-uecVny5rlGxVNhVkKd4Cww-lZW94TeRumZJEn-ztKtWmVgfofR6MVcq4stUBLfcWNEYKHIRCwhMx8J3XuIMhNP3_IR9_hu1teGgjQGzE5z2NuSJvDVc6uP069DMpJIvLaA7o85kpJAPPbjfqvW7FKd8zzVMcpKLzwMjkbkT6KBnbU1rR29gc7W8IkFcF7_Vq_fkeeNz0HTqFdN0WQg2-q4lRZtYkew60snOx9wr41p2FvFwSDQBRAg9T4qALCiCEzZrxZkM7FYnDHhd9vG49b2JcfIKC-cb4Z0pBrYxy9EWFrp4LYoOy9K6Khc3-AlV1KP4mEO4Bkn3UZqrHqr0Pcz_S0YuROi5eF0N11VNHq3BZz33zIUHXCZ-3e71NG4J-07kT6caDmzMIr85VpJpZcmLJvSbLzTNxJWlJBLjQJZSawjsj3CeDpolVEk8Ys_uiESGN4VgtdmTzXPU-qGhrSqHVX0-Ygzq1UyAHg7H5ZoMDXz2H8Djbz6RYjOxmYEgew2rkR707P4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌چهارم بارسلونا با گل دیدنی رافینیا و پاس فوق‌العاده تر آنتونی گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105230" target="_blank">📅 00:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105229">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلگگلگلگل چهارم بارسلونا با دبل رافینیا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105229" target="_blank">📅 00:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105228">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🎙
توضیحات پیام صادقیان درباره جنجال سایت شرطبندی؛ من اصلا نمی دانستم این سایت چیست و فقط تبلیغ می کردم، تا الان یک بار هم وارد این سایت‌ها نشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105228" target="_blank">📅 00:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105227">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/40a24dc89a.mp4?token=i39FpXv6COuR8JebwhJODK4_x_XO6xN7sXLJFd5_ls5J8Q3mek80IFkxALKSo2b8Nlbo2kp_3nXVMJfuzsO7tw6uTnIQSwkMpRu5iKlBFLZOLiFHl9PjZeFolbCiZhD8h3_DWvwmEAzddrpEyb3kUUQDNCXDHMZ-41uq22F4ywL23rIifdWgIK8N63TEmrokJGmAJ9aU3vl7GtLJLeKk9wIXdW-2CZJ9wNfgAoVDer7iThhfhzW3MB9K7KJnovqo_DEZlOJIxisBlIrpsXUoLxymVt3ugbOYoVCw85q19xFSlzYvSiuBT-E-Y-2U0tHnhs9Dd42fEzmyh4ZZBZhS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/40a24dc89a.mp4?token=i39FpXv6COuR8JebwhJODK4_x_XO6xN7sXLJFd5_ls5J8Q3mek80IFkxALKSo2b8Nlbo2kp_3nXVMJfuzsO7tw6uTnIQSwkMpRu5iKlBFLZOLiFHl9PjZeFolbCiZhD8h3_DWvwmEAzddrpEyb3kUUQDNCXDHMZ-41uq22F4ywL23rIifdWgIK8N63TEmrokJGmAJ9aU3vl7GtLJLeKk9wIXdW-2CZJ9wNfgAoVDer7iThhfhzW3MB9K7KJnovqo_DEZlOJIxisBlIrpsXUoLxymVt3ugbOYoVCw85q19xFSlzYvSiuBT-E-Y-2U0tHnhs9Dd42fEzmyh4ZZBZhS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل‌دوم رایووایکانو به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105227" target="_blank">📅 00:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105226">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e2518b5e4.mp4?token=U6xmr_ixScLNf_khD6G-n3P_04HbxuesFN0CVQHBcQlrdMzlYRpnyWYMAdR1Lsq96-6sNM16mnEuMZqmaVIVXwBuGSOVxC3ESRkIJOmvmzY62lUgD84yHco2E7e2fdUKjPCEsptH_Tp6uaTaVPjd1YAXS-lOfy2Rb-NGdYzoSEGmY8k9Y-VGhzUxfq2FVPVYV9FZIf-TQsrc1wT7tKLWarRHv38tlQe8jN5oUT6mdImo75jLOSbov9QEaLIrQq-dEbX5MV3sRx5kaEcOGnCE9xp2s7RBbI7Ne6TPkevHsMbvAWPVZmqU5mtpVmGMdho5RDlqIUGvR13RZf9UAR2abw5j5rzWftDjniHSqEFMPiPKA_EHTRdxu_76sA7b768drgCvLSzIkMmsXBzqYuw2F-_OwxxHeJWPDMzGAvgUqQYnvthB4SFHkTmCEf1_7_3Ly558LkBl5mTKiKKAvzd8EovazpDB4X06EjhOSwj0q1MlPVbnul8gx2USCUNIkSsaDTGpIg914zUXl5Mhe85pAFoRVhxczgZw4t_TmNWgiO1-TufDLHGhqRT0kjHCBI1SsL27yq5gZzDB8uj0EzmO2HqLxg0gjomkl0r-LtrCTiAzlbBFD3T1weEwGdOARl8_ZREYXelTfZXs--rxc3si1XRwikR66tJFt9lFxU6Zl6k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e2518b5e4.mp4?token=U6xmr_ixScLNf_khD6G-n3P_04HbxuesFN0CVQHBcQlrdMzlYRpnyWYMAdR1Lsq96-6sNM16mnEuMZqmaVIVXwBuGSOVxC3ESRkIJOmvmzY62lUgD84yHco2E7e2fdUKjPCEsptH_Tp6uaTaVPjd1YAXS-lOfy2Rb-NGdYzoSEGmY8k9Y-VGhzUxfq2FVPVYV9FZIf-TQsrc1wT7tKLWarRHv38tlQe8jN5oUT6mdImo75jLOSbov9QEaLIrQq-dEbX5MV3sRx5kaEcOGnCE9xp2s7RBbI7Ne6TPkevHsMbvAWPVZmqU5mtpVmGMdho5RDlqIUGvR13RZf9UAR2abw5j5rzWftDjniHSqEFMPiPKA_EHTRdxu_76sA7b768drgCvLSzIkMmsXBzqYuw2F-_OwxxHeJWPDMzGAvgUqQYnvthB4SFHkTmCEf1_7_3Ly558LkBl5mTKiKKAvzd8EovazpDB4X06EjhOSwj0q1MlPVbnul8gx2USCUNIkSsaDTGpIg914zUXl5Mhe85pAFoRVhxczgZw4t_TmNWgiO1-TufDLHGhqRT0kjHCBI1SsL27yq5gZzDB8uj0EzmO2HqLxg0gjomkl0r-LtrCTiAzlbBFD3T1weEwGdOARl8_ZREYXelTfZXs--rxc3si1XRwikR66tJFt9lFxU6Zl6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بارسلونا به رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105226" target="_blank">📅 00:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105225">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگلگلگلگلگل دوم رایووایکانو</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105225" target="_blank">📅 00:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105224">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105224" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105223">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105223" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105222">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=A3EueqBlnKpPbC2oFKpqn6n7sE9x7lxnE8QGtKQZkVBmBmz6aZ4sIgdcisJEFYGtf7CJDfS3ppAK7-FawQrNQjToWlFwvaEe-k3HQLaSqmt8zXdRjJm9grdYZMJesXVpP28PdN1fR3XuoLiwdr8PgALvAr3LUr-wKI4Lx6o_5__np_uwAoNuD95xQ6ljvzuGfiOYY45jMjVbp7E_G3Y25Ytx7QCLNrehA6jxQAtDQDherl0nDZvbNsbtqjcMFHsTDaOXHzm1i_xlClbO4tgKo_6O_0iUyd7_ZeZ7RiBBOXuSu5WpKH0zvUGi7zLzrqfSyZ53J5rhk46GJlPLobKKs5UeLn6MsPpC9lwWJEoP7m3T3xUGbSCQp8I9gc34A-57AL3rL_s-GaIQB7jjpDDg0oHfdPW0WwCkMNdqBtXcIgAAf8I6iWFUJfTqIu6R8Sc6hK74zs_u85fvYy5bFaEcsRMJSYrUCyXveCLMwxdF4KRmPbEmYvfz_BfmwPsG7xtfChPU9V9fEyB45K-wJOgHi3GJbvJ5dbwLWPGrRsmTZfEoY6PWpwudMZIsD42hYq_DZ1SJZjdqzWFC9dOK5qT3jw_-VAPOx4OltAHjmDB0dxsa5V9Ou581RZwhPhbTBqGtGIsnsuUFZO3xVVD4o6m-UtNcTT_jWpQds84s9HP0GEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=A3EueqBlnKpPbC2oFKpqn6n7sE9x7lxnE8QGtKQZkVBmBmz6aZ4sIgdcisJEFYGtf7CJDfS3ppAK7-FawQrNQjToWlFwvaEe-k3HQLaSqmt8zXdRjJm9grdYZMJesXVpP28PdN1fR3XuoLiwdr8PgALvAr3LUr-wKI4Lx6o_5__np_uwAoNuD95xQ6ljvzuGfiOYY45jMjVbp7E_G3Y25Ytx7QCLNrehA6jxQAtDQDherl0nDZvbNsbtqjcMFHsTDaOXHzm1i_xlClbO4tgKo_6O_0iUyd7_ZeZ7RiBBOXuSu5WpKH0zvUGi7zLzrqfSyZ53J5rhk46GJlPLobKKs5UeLn6MsPpC9lwWJEoP7m3T3xUGbSCQp8I9gc34A-57AL3rL_s-GaIQB7jjpDDg0oHfdPW0WwCkMNdqBtXcIgAAf8I6iWFUJfTqIu6R8Sc6hK74zs_u85fvYy5bFaEcsRMJSYrUCyXveCLMwxdF4KRmPbEmYvfz_BfmwPsG7xtfChPU9V9fEyB45K-wJOgHi3GJbvJ5dbwLWPGrRsmTZfEoY6PWpwudMZIsD42hYq_DZ1SJZjdqzWFC9dOK5qT3jw_-VAPOx4OltAHjmDB0dxsa5V9Ou581RZwhPhbTBqGtGIsnsuUFZO3xVVD4o6m-UtNcTT_jWpQds84s9HP0GEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ادعای بابایی مدیرعامل چادرملو: سه‌جانبه را برگزار کردند تا پرسپولیس آسیایی شود
❌
صحبت‌های علیرضا بابایی، مدیرعامل چادرملو، درباره پرونده جنجالی معرفی نماینده به آسیا/ رانت اطلاعاتی، دلیل گله از گل‌گهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105222" target="_blank">📅 00:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105221">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dD24cZYWex7GEiR_5sh743vjz8SwiXzC216KUikWKQtWr9Y5jITncPDTXJVlhPrTiW0Jjmc0cHFMRtavILGuuxbRK7W94neN9zMM5o2LQvTG92k4z_1zP-7pRUkdZkMgrGzaYmsy7YzpkV4n8AvNHDDOt92nyEgvcsQkhAGgpfi5NjHa5tkBC0BRtDaHXcJPDOHmU0Zl076muGFjcPghYWgx4PapaUtU3PQCq3kqxaf3LxQAccsCLiUHv17hTtqICE5D1Q6WJlgtqL3FDeae9-x3p3ebthPVW9rz_avwM91o1A2HHSnwlr05wnM1KBSVHq23ZKlEeAGfJcRfq3Ou9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105221" target="_blank">📅 23:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105220">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2a3572ef54.mp4?token=KfbP8Pg0TtMFZ8mhyQWSZRw1RxMz2pqaHLgYDAlFhmCciMJEio9bVVWpZeXwNaVUZdV-1zzeRhwCjfx0UcSfA12Ue95OGLdUf3HMXTXlM2PWaL6FrdtQM0N_sZ2dd8-WSsrI8W4K8bgjD9lJ9tbF4cBwuI5mAlVHXLF_bIvhqhr9no58SVGmW4rCL-fgMiwSR3RqfmHPy42qhm8w4hSbqxqLt8z1-Gpogh8TWjJvkXmY2n-WlUo6LJ8tcbopBRBh8cNkWl6LG6DSKsJpFEt3OEaoeFiYO7ZvxzVZaYD6dlzBT0vxqPUJb-E_u-kSYoXNqDA3dME8AwlEIAEVhjVXkIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2a3572ef54.mp4?token=KfbP8Pg0TtMFZ8mhyQWSZRw1RxMz2pqaHLgYDAlFhmCciMJEio9bVVWpZeXwNaVUZdV-1zzeRhwCjfx0UcSfA12Ue95OGLdUf3HMXTXlM2PWaL6FrdtQM0N_sZ2dd8-WSsrI8W4K8bgjD9lJ9tbF4cBwuI5mAlVHXLF_bIvhqhr9no58SVGmW4rCL-fgMiwSR3RqfmHPy42qhm8w4hSbqxqLt8z1-Gpogh8TWjJvkXmY2n-WlUo6LJ8tcbopBRBh8cNkWl6LG6DSKsJpFEt3OEaoeFiYO7ZvxzVZaYD6dlzBT0vxqPUJb-E_u-kSYoXNqDA3dME8AwlEIAEVhjVXkIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌دوم بارسلونا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105220" target="_blank">📅 23:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105219">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88eb8f24c5.mp4?token=XpARHk-M0s07VKR2BUEVkOVm7VvUTbtMY9A8FNrh6BAArx18ubab352rZdZaxClh4-wdJCqYc6bly7ozIHjvCYlgIwVoaq_OU24r-SI6Wii_t49E8w2MhnnMdO2KUnnL9yMYRQp7Iyknm4NUROgeFWdlu4ntE0nTCQPWH75xn4B94gEKeWTSCI8h91Cbrmcoao0TGikAYBjiJ_-AQUl6wshtRr4zBQFhYhB5IvnLFtvTiUV_mZdZ3q8ezfmm092gANt5tpFq1LBzxuzNPmr-xM1yYJcNhPwiKpWViLiq7SwcjXksNBscIu4dJGrqc-P-7EFZ93XNQJoFmaBDBEicL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88eb8f24c5.mp4?token=XpARHk-M0s07VKR2BUEVkOVm7VvUTbtMY9A8FNrh6BAArx18ubab352rZdZaxClh4-wdJCqYc6bly7ozIHjvCYlgIwVoaq_OU24r-SI6Wii_t49E8w2MhnnMdO2KUnnL9yMYRQp7Iyknm4NUROgeFWdlu4ntE0nTCQPWH75xn4B94gEKeWTSCI8h91Cbrmcoao0TGikAYBjiJ_-AQUl6wshtRr4zBQFhYhB5IvnLFtvTiUV_mZdZ3q8ezfmm092gANt5tpFq1LBzxuzNPmr-xM1yYJcNhPwiKpWViLiq7SwcjXksNBscIu4dJGrqc-P-7EFZ93XNQJoFmaBDBEicL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105219" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105218">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگگلگلگل دوم بارسلونا لامین‌یامال</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105218" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105217">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگلگگلگلگلگلگ تساوی بارسلونا</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105217" target="_blank">📅 23:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105216">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/355ff97540.mp4?token=Gd3vSWeVwXQP57ZSsDSNhGGQ5_jnHZYypZlZIF0QB9fhGQk3yU_0aOwvyBVGOxo4hIVKQO23bDnymQazEa_Ve5HyfSz0TRHsOAyBNKkWyM-VG6EFS61MNoj1CAvv8GVnS26ERg3yxtMG-LiI4p6XbOCN-YOC5VxlfysMPS-CcovZK_-OkKkeujLj9wkwEjeKc67pMNJyXwNuU7fU8GPH3gJG_IltDU_cngws253HN2vITpe0ExP0cdFWuwVyDKf_ElqI0kOQjur_zyyJrXZ3rI5e5tE389jwXMkP-IasOMZagdp8opxAheQZmLLlp2Wy7AC-D6A6s-G7yYbLP8xtCl_HeqFi1QyMyuUTNG0ybvce794uHt_H-flA2cFRaHiXXONwrSnZyKps3ZoEHrDWH1muNAbeCiP61eooS1LyPThbXBsGhwvNX9_qGHIM7h2Oh8QQy3YqZJjssVzBPs9wsnoKt6hxTsMx4VKuXF8mE9FP4tRvT131JzNTtd_Om2BoutueuR1NovkuWLv4HTZNmoWM5TF9adeKL2xtCXZPTo3HMtZMMVgLxuQrf6Jj0OxpdMEj96_vWmu5U5ilNVWQqZsv3515E3ce4BfeRumwOOvtt7-0OZEYLF5ATzUyd21iO-jk4Zru4xo3hyAgGtCEI3Wv9tunS3apQUTqZOrWZ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/355ff97540.mp4?token=Gd3vSWeVwXQP57ZSsDSNhGGQ5_jnHZYypZlZIF0QB9fhGQk3yU_0aOwvyBVGOxo4hIVKQO23bDnymQazEa_Ve5HyfSz0TRHsOAyBNKkWyM-VG6EFS61MNoj1CAvv8GVnS26ERg3yxtMG-LiI4p6XbOCN-YOC5VxlfysMPS-CcovZK_-OkKkeujLj9wkwEjeKc67pMNJyXwNuU7fU8GPH3gJG_IltDU_cngws253HN2vITpe0ExP0cdFWuwVyDKf_ElqI0kOQjur_zyyJrXZ3rI5e5tE389jwXMkP-IasOMZagdp8opxAheQZmLLlp2Wy7AC-D6A6s-G7yYbLP8xtCl_HeqFi1QyMyuUTNG0ybvce794uHt_H-flA2cFRaHiXXONwrSnZyKps3ZoEHrDWH1muNAbeCiP61eooS1LyPThbXBsGhwvNX9_qGHIM7h2Oh8QQy3YqZJjssVzBPs9wsnoKt6hxTsMx4VKuXF8mE9FP4tRvT131JzNTtd_Om2BoutueuR1NovkuWLv4HTZNmoWM5TF9adeKL2xtCXZPTo3HMtZMMVgLxuQrf6Jj0OxpdMEj96_vWmu5U5ilNVWQqZsv3515E3ce4BfeRumwOOvtt7-0OZEYLF5ATzUyd21iO-jk4Zru4xo3hyAgGtCEI3Wv9tunS3apQUTqZOrWZ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌اول رایووایکانو به بارسلونا توسط کاملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105216" target="_blank">📅 23:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105215">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل اول رایووایکانو
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105215" target="_blank">📅 23:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105214">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=bi_cE5RgKvAQx8gdV8S1cG7-9KtIwCDxaytHD5vhSmVJ8rbiWyNnmeJUiP2ybykxMHi4qVpXpNaZsJOJH55y5TNhvbALnJLDgNKdjzV3kv0TNVg-9R4xFJwiPsHGIquvo-uNmohsfA0U46vseYUcrPedikXrmtqMsoFp0AqCuzfY56JB3CerfVRvJpPi-h1bZWa9trpp0ZuhgW0lLFR043yPj71MaU-B4mx5rE14Qe7-_vxvsTnkUFD2-NwP-8G_Pi3s3ZOOmn6GP9KkYx6Ofg4E4wqBk66PWYJiomh6IvOj8Ny9xSlCvXBf5-Ofapa6WfnQ725unSdS1BY4Rvqb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=bi_cE5RgKvAQx8gdV8S1cG7-9KtIwCDxaytHD5vhSmVJ8rbiWyNnmeJUiP2ybykxMHi4qVpXpNaZsJOJH55y5TNhvbALnJLDgNKdjzV3kv0TNVg-9R4xFJwiPsHGIquvo-uNmohsfA0U46vseYUcrPedikXrmtqMsoFp0AqCuzfY56JB3CerfVRvJpPi-h1bZWa9trpp0ZuhgW0lLFR043yPj71MaU-B4mx5rE14Qe7-_vxvsTnkUFD2-NwP-8G_Pi3s3ZOOmn6GP9KkYx6Ofg4E4wqBk66PWYJiomh6IvOj8Ny9xSlCvXBf5-Ofapa6WfnQ725unSdS1BY4Rvqb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
در اولین معاینات پزشکی از مهدی ترابی مشخص شده که این بازیکن دچار پارگی رباط صلیبی شده است! معاینات تکمیلی قرار است امروز انجام شود و نتایج آن اعلام‌خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105214" target="_blank">📅 22:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105213">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
مصاحبه‌های منتخب هفته چهارم لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105213" target="_blank">📅 22:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105212">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=ZH6SCzyRnU09PwA68HVGZTKEgY_wlfuplZheEuKMdgti-PF6ym9-_2Oq6Pq3eykuP_0Ar0XVbIz4YGdNGN94BPUMOAChcTXVaZCCnNwd4kQnjCDFCJgpPoI_T7ldRnuLWA36sTQUs39ETd0SFzo0OSdVyufd4TSdfV9Q2XvIEdxKLvgGu6lU3JI-9uQw4qaAnInZYmItpOLS7hgXWt5vcwCnA7Z565gnwBhFqVtCXlK2XmUodQwTsI_9vqOFTBhsBS3jlXaS4RcR58X5o3t1xgrN1R9akp0ZHYGZ8baloOw-qSPLl0_kls35a1iSpGzhPGnpVFPS7iX3R_V-7hCNsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=ZH6SCzyRnU09PwA68HVGZTKEgY_wlfuplZheEuKMdgti-PF6ym9-_2Oq6Pq3eykuP_0Ar0XVbIz4YGdNGN94BPUMOAChcTXVaZCCnNwd4kQnjCDFCJgpPoI_T7ldRnuLWA36sTQUs39ETd0SFzo0OSdVyufd4TSdfV9Q2XvIEdxKLvgGu6lU3JI-9uQw4qaAnInZYmItpOLS7hgXWt5vcwCnA7Z565gnwBhFqVtCXlK2XmUodQwTsI_9vqOFTBhsBS3jlXaS4RcR58X5o3t1xgrN1R9akp0ZHYGZ8baloOw-qSPLl0_kls35a1iSpGzhPGnpVFPS7iX3R_V-7hCNsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی با گابریل‌ژسوس خرید جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105212" target="_blank">📅 22:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105211">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VK1ksTe7B0TBFqW481pmbEp4y90W1fbVe8XZIwy5y3ev7Lt3ZlnqX3R6XAuJJuNGQFJFQTZpkHHZoiniNO322EhzEYQ_onq8s57CUIuwVopVj_GGPYTBaRY_UhLra9oOyXMstYsPS5uAIhNwJreB_k3hRhdu8dtlMx5G0LIVB1TjcA0QOikQz9Sv6fNEBce5_qES8tt9tmy303-R-uwHVMRZQiBrH1FZSH_2SRKfsd_DZmFFcxh-XUWRsSeCFaX1fUKx9DEdYZEZw0acjWwcnkAxzTdKmftfvDxqW6bUH0WMJytum5h-Fo-1V6LyuxoZvD4tnqPLWIMuIDuWYtNMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ایلمان اندیایه از اورتون به منچسترسیتی؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105211" target="_blank">📅 21:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105210">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxiNwv3EVR9UeUIWZesmCDeedGFUTZ5KYIvMrvlCfaD53-zCZOpoqm4mrFeUj73FEYCp7CcPjAGdWNvKkWFUsqEtNOMUkGutBhG0yTlmE8NAL-1HKNYVf6GWQO3bUQ-hRhrEZee8kOH56aYj7KQ3J9PUfTQUqtwq24l_7cHMzbgLr9-wag0KyJdNnydx9FnkK1gSaeuegIaCYHjZHD7jbBkkPRe8D4-RfeYzwTbzi0mCRUGz3Q3nMG7vTFc06JUIz3vCXPLrceuMzIRjHRRRR8a1odr5Tts0sj1KfihbE6htmfroat7ckJYUQStZGjL8MV7XHSSk1QdgX0MjCCk3cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌سوم لالیگا؛ شماتیک ترکیب بارسلونا مقابل رایووایکانو؛ ساعت 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105210" target="_blank">📅 21:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105209">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iqlc4EpJxaZgKLfiZ_8peelBbX4NuiqwppZJSKXeKnOT-qTgCUh-7YQV5EtFJvNutzZnD3y8E-t4QnozhanTogOc64XUZ73Myj_DDF8pkY8sjLyT4J_0MRTBBH3zrY-F9gUv6xcrdC-jAcWEwLnogHaxiFebK-XNmRs8BLz5sOqGAyfmbGc62f34jjw82yGgCxmAjBn0mh_mSEMkRI-EktezEnZH08XQn1QdzkdP67tzdg91nPbFX2W0eCEH0C7C0_y3ymbRbRaKT01Vc1C0bkFAdZKRF1K52KRbo9kpcqqqKFy_EttC-h6yw7gmZeDzJ5F22kf1EbseidE4bgUyYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105209" target="_blank">📅 21:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105208">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrVhaqmECzTdOZ_8P_jRB3v-9NWn5Gj1MWAC6AYTL7gFgdeAJM2xR2FgTsrGP8GCmbbjrOPyc9UKvQODP5N5FPKT7zY-w7yD6RXAYbFyaobRz88mfW1dVEhiCaTObf5eDR1FCHUmIu26O5SIlmTR3mFrjja1bJJl4RSPFbwlAC0piR7M0-JEA-A5qYJ-TovSvpI8qNaqUfz5Zay6SnlTTKcw0o7-tKd9FoyXL3ZJGXINPpALKqYMRCU_8xajDPzfzvPsu07EHzALlHGT3gQK1ayiWFtlKZO-0_MJFA1VxrI7h7ljuixBRP_Hxr-KNNDypZY7BhX9NZ_debg5mYs9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: اولین پیشنهاد تیم منچسترسیتی برای جذب انزو فرناندز به دست‌ چلسی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105208" target="_blank">📅 21:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105207">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y__Sa1Rx2bXVFJ2uQ_VSLQbM9ozgU8uq9aymLUqFGJSUKwX6U_IBXGuonSBRWmSnfP0KFQO8b2yE_DM3nMLjgu4tgPgrR3I7AzCxZpcZaZlZy7r6xefV1dRqJZ4UIE_WIKuSctO5BPusx7j-GGL4KA2rQcp4NaXoa3bWPH8CkcLx3tMZAojtA2S5520QjlVoBGEuM3AXp9luzDS6JPCU5pAXVt5_iWny5DgVAMSB1TZ7D6pqDXYfbzDDJ2GrXtTroosd6P_oVMlVeeV6PmCj4or0UQ0Vun3F6mUJRXq1h28nUza7tPw7xnIArTSuxkyiTwURCdVkeWIwCcknXb1HJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب آرسنال برای بازی امشب مقابل استون‌ویلا؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105207" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105206">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_OqYbr5iOtfGiqJnuldKBLfvKhGdJBoQaAqvydKCtjF_Gr4Q0P7U2cQBNlfRQomvAf5zC8J7_Ns733CnowtycZRaUMF3lE6qUSjb1_T3AGEcAKhp5ib9CsJe8aNjBJayCkfqekecFm2bKg2dCwkTbGykdJlCGGmZj-Bk-SbUhbvQttJSfjXVpZYtWeDbtwU1iB-h9axVTBujByOvGc-Xd0hvxfZRsuuQZ8Xfw0rRqBTcznLMEe0PJ3CSLbgzRaiEz6VbyBmbon1qWREDEEvKnJXvp7HoojxpzwNkFqKCGoh3K6Y0ec_vW_ofgcwMyHFBWCwNPyjG35o8aFOT75--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: آینتراخت فرانکفورت درحال بررسی جذب خوسلو در ساعات آینده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105206" target="_blank">📅 21:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105205">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay46UnEtwORnUsh3AmsYTTSoYFUGVUKQKgsvQsUBsl6Q6MvX9f2yat8cm-OkonNYIBYZbHQDp-f9ZJzuyARFpuqhuzJQVj2xNLMgvMn7NLBesHLASF94b0EoBEv0J2pm_QLGVoZp2qAT0yucaSeaG0cMzOVYsaYq37PQ6eBsYFE-w4R0k4Rjq7T2FbclmUNM_xAvaW7FTwYIWYtaA27QOf2_-9iIFHfGePzz4m9WCAdzN5UfEWMZ39ImutjDi1kAQ01OQKqJcRYTGl2OmL-EgOlzq0NmWN8CL565g7SO8fjOQStXoTyUvboD2POScLJ17k9UwBwFJ0IrKiMFqx6xcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105205" target="_blank">📅 20:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0618RA62V0AXmTn0uPUiARb-9AKErUnzuWBFkHeEE-gvm0huddKUJY_Xys0RhanXKe3cYTpEmwn3TrimUYFEhfoWItEAetLKR62D9JEjQRZa-H5EWn6ML72UCloIGLjwiolMOIeky6zn5L3_xySmCuK2NMr_9u8nXTrzTsGATWsiTXwNX2D-cBTuPIV4rk77Gy_tKlHiQaqJ25DuWliLauqhHveen6VzVvZKN7Vrw809ReXmVBTRobA2Xvc-p-_17794CPKuhGQtDFjJ_GfQCfGnvm-3UryUTxlFhqRfKoJ70LAPTVhdQQRRXXS78ML5UGzO1axuljVMdkNxpUShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت بلیت‌فروشی دربی طبق معمول ریده به خودش  زیر ساخت در ایران 0 گنده‌گوزی 1000</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105204" target="_blank">📅 20:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
⭕️
#فوووووری؛ بلیت‌فروشی دربی آغاز شد. برای خرید بلیت از لینک زیر اقدام کنید  https://ticket.sepahansc.com
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105203" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105202">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
اعلام جزئیات بلیت‌فروشی دربی ۱۰۷
🇮🇷
🇮🇷
بلیت‌فروشی دربی از امشب آغاز می‌شود و سهمیه هواداران استقلال و پرسپولیس ۵۰-۵۰ خواهد بود.
🎟️
ظرفیت در نظر گرفته‌شده برای هواداران: ۳۵ هزار نفر. سامانه بلیت‌فروشی که فروش از شب شروع میشه:   https://ticket.sepahansc.com…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105202" target="_blank">📅 20:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105201">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoPcI-43I-Eh-YYThjWrV1u7urrI4qvEnKe91QFVjJxzTyko1mApL2-dOPD02DrzYW7etfaoVA_MJ11kRQhHKIRiyLla9qO_ma9fS9dxqNG9Uhrvty8ORoH5ZhPSRpYMld1Khti7ZEKmhNh3jh5ZNydnhuYBlOmhWZ8mQCKGhyXISkrhpyZxFxixY8lsZeLFR4ay0naOEr71p_V1_Y2xvQSVQWC4drc2PqQS-fuWVfLGxK2frM77VhdhdbcFYXjj9P7xlOajyFFNJvpZyjDgaRKk0RUY9iYqvKkkxCJm8PY7OwWVe0L_CzNidSbxGIzCBGDoWwj1ltpA3dHbNfEzQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105201" target="_blank">📅 20:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpJuS6s-iQfg7QCDXtwVUz2JOMd7uuCCirbyX_bfXnqdq2flNzK8jJonr1tz8E-QdYgXuM-nWn3MibLhM2-bqwgI0GizrDpFRqM6wcflJu8j7JoeEQotTvtK6f_Jd6OM32-AsiMI8HJ3CdR7NcvoRTAYkL3-Mot5wXhWMMXbG4AWE7V8cz1HHzGUS8UxUG_9xOunThhDtpEMSfEe6yi6_XLypGQ15t44IYzjiWH-x1K11qG41Ds6pDPxEODDwu4wV039D8XUPu1IbztULhKEATo-8jARDNIqhJOJPUqN-EXE6p_yFswewyE54u6gMz2YLKClzihHEXY-pmxAZt5REA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
قدرت دوس‌دختر در بازی دیشب رئال‌مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105200" target="_blank">📅 20:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=AKaV9phQLBLHaiL-z98o2C2OA9IIf2SdoN7eJAtUvv4lwg6Qut4DzNPj0_6Xy4qxLq9jL9qlIgutlGpBL2qZTgsaSBoiWJxdQ577uBxo2PWEKziKVrHcuKD_kVq_jOnzzStTU2i4zMrvnK7T8JEPyaMHIk22PPhVs7hRfKm1bxcGxWI3cS0YIH5M9WcOZFPAoIGA7ITA7ML8Gklq9MMPU4UR-z0GPSRF-EiQ27iliJyR9qj_QlhhZQ82g8nhRU5wOLNYM93xAJYcyMX9mhXicBcDL35aqLdSz9pMAe7RG4s5fKc0sb1IyuMM6BfpALrz48r93sl4YQLeAANP49Vjk6ihvbstlF86Dy_gMmgXxozq0iQ2Sxa_NN4QV2gwIP_vl6xLeHCtlJDa5dUKfcOZFGXrgYfxR9GE8z0MQ8CWnijmJOl6Qx1KL26uSvPHdX40m5VuAbVe8XJP0RfLTqNYKWar9RnX3dYEigncCcZbNgL8WfhmwW73_cvLySmAQdbyg9XKvxmsbhGCkqNZX9uFfnAAzeimCcok4-4-6xvgWMYC7bneQrWiL8zbTMkcDxv3XWGUrP7Ml2exgvAN27337Enlg3f83u7GyyJdEiXjiuEewff-8Lxt2q8PncdDXkK51MYhGvkCDs4cy0y_VBlzofwn4lYhxNad7_mIuMPHYvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=AKaV9phQLBLHaiL-z98o2C2OA9IIf2SdoN7eJAtUvv4lwg6Qut4DzNPj0_6Xy4qxLq9jL9qlIgutlGpBL2qZTgsaSBoiWJxdQ577uBxo2PWEKziKVrHcuKD_kVq_jOnzzStTU2i4zMrvnK7T8JEPyaMHIk22PPhVs7hRfKm1bxcGxWI3cS0YIH5M9WcOZFPAoIGA7ITA7ML8Gklq9MMPU4UR-z0GPSRF-EiQ27iliJyR9qj_QlhhZQ82g8nhRU5wOLNYM93xAJYcyMX9mhXicBcDL35aqLdSz9pMAe7RG4s5fKc0sb1IyuMM6BfpALrz48r93sl4YQLeAANP49Vjk6ihvbstlF86Dy_gMmgXxozq0iQ2Sxa_NN4QV2gwIP_vl6xLeHCtlJDa5dUKfcOZFGXrgYfxR9GE8z0MQ8CWnijmJOl6Qx1KL26uSvPHdX40m5VuAbVe8XJP0RfLTqNYKWar9RnX3dYEigncCcZbNgL8WfhmwW73_cvLySmAQdbyg9XKvxmsbhGCkqNZX9uFfnAAzeimCcok4-4-6xvgWMYC7bneQrWiL8zbTMkcDxv3XWGUrP7Ml2exgvAN27337Enlg3f83u7GyyJdEiXjiuEewff-8Lxt2q8PncdDXkK51MYhGvkCDs4cy0y_VBlzofwn4lYhxNad7_mIuMPHYvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخرین وضعیت زنده‌یاد ورزشگاه آزادی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105199" target="_blank">📅 20:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwT8gsJN28heQDxpx3C9TgdHHxIhiENcrL8ETkk-DEwEXvQDum2KR05iM6To-uuuGhSSEJ_UdMu3D77rLMBDLFGKcrQPmDUZ-SgMSXz6yjLiR2fwCMZm6hGPCMy4h6JJJsOgnuB8hAmg57010KnIW5oo-Yg8cJCBmcortqwLyb1rI9SGkkKE9yOHywoFutmVSkc9FWXL6GXy35GQDnpwBM9ZdypkypsgUJqkiQti9VtK-BshUMrRLYZntbpvdfd_9FSg0XWSTRfTHdNRy_YNN9U5oDvo6edrYAzEgyfYbPPzo1855jAwY7j6DaHoF4CSFurkSG7imaoZ6LpwnTrheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
آنتونیو آدان: به باشگاه استقلال گفتم که نه پول فصل قبلمو میخوام و نه دیگه حاضرم به کشور جنگی ایران برگردم. قرار نیست به استقلال برگردم بخاطر همین طلبمو بخشیدم چون وضعیت ایران خوب نبود و مشکلات این کشور رو درک کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105198" target="_blank">📅 19:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdQ_HVpxF2MGWVOFc-wwPoxie74r-eEAz41PipzKOn0AQrhY8AqBkq2mu4WfnOlQbV0Ftjz2A9qJlPuPbO58arhOi2OZoyLlluSi6mm5bCpq5Atl871aWLYvMlPqCDaNnebRSljvpc0tjobZJWc4IeV3KEbi55aa8DtcWexHmjibA0Z0jzownpjnuCcLwJhmbviyqPzMDexTRZY0XE6vffAotNttOrUfhlbt7Epyt_Qu6Z-w-uRtFk13g-IQE8mfYeV0B3zXxnzpJSx8H1TdX1hn_K0mXhM4WyjMAZ0fAr1GlaxdCHUA3L5hIgwS0VUfapjUVYBbSoUJagoagLow7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نامزدهای نهایی جایزه توپ‌طلا روز ۸ سپتامبر رسما معرفی خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105197" target="_blank">📅 19:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u98hZ643G5XKzwYo5T98WhN-hA54xM7d23uKCKlB9m8_Nsv6Hu7TOi1idVBT-NUuP7C9AiQM9f1ei-YOzqGiVc0IWLnGBAgUnuVy9n9Y_fHlpVO5xnBfVKFprfmhHn3me219imPI3vn4najQeaUbMMM6svMcfm7LWaOIdxj9nepaCjNYW4Pzw0GVipuHQh1L04ShcCKrMOfKttOqwTmgsGsrKPAsq1I94HiWIyZjm3Y7XxJnBX4T50HjQ0SOqNv8Bzr6cwxDZ3WnabDYdeMnpTg9ugtLNRQ4792_llMwNufLVKKs4f0BgvhS0-vllHXFpeQqXC2Stq0MEuLcwhw28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
🇮🇷
🇮🇷
دربی با نصف ظرفیت نقش جهان؛ این اسمش مدیریت کردن فوتبال و مردم نیست
❌
ظرفیت ورزشگاه نقش‌جهان برای دربی از ۷۰ هزار نفر به ۳۵ هزار نفر کاهش پیدا کرده؛ یعنی عملاً نیمی از سکوها خالی می‌ماند.
✔️
در دنیا برای حضور بیشتر هواداران راهکار می‌سازند؛ اینجا اما یا تماشاگر حذف می‌شود یا بخشی از ورزشگاه را خالی نگه می‌دارند و اسمش را «مدیریت» می‌گذارند.
❗️
مدیریت واقعی یعنی فراهم‌کردن حضور بیشتر و ایمن‌تر هواداران، نه ساده‌ترین راه یعنی بستن سکوها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105196" target="_blank">📅 19:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVv6OMzWY8X8O_uojTpHxYf7nGlRavAhRiCe2KCVyecM9L4zTQHwDBtnebYppQ0Y6Lt4AlQNWOtmXRuQmst4I9w1BkOwiHyHTGgiw479yVfr39jn7HtVLM8ZcNSFFRJXeFCDZRXNNXZcsekbHzZRPwufi6C4Pp_fu-T6zPwsJid3NLdGnVbQ5xsYsNrny8BFwpcHUyICMnrVeR4AU2e41t5UmoSt6rlWrvPdm1L1lfaw-Bu1OrAbSWKJd18BjymdfGnOcDpp56o4sBM1dCABl0fihnTAeizhOFypOb9Wf1csQV41hN4EAqh74oUTAKTNJyC6yEyiwpweVXXX2uWy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اورنشتین و رومانو: لیورپول پیشنهاد ۷۵ میلیون پوندی سیتی برای جذب گاکپو رو رد کرد و این بازیکن در آنفیلد موندگار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105195" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105193">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=AOYy3yEtk3sGDXI_OU-x9eBojbvVU9oREUnXAkTZNwVciqoI6Xbq8By-l1R4J_F8zBqjSA_exeZUHO39e4XtkS391PNRlqYh89HwMOp_3QPALrxgV0hvV3R8smG3Mssj2XAkxlWLmCJmnmEm-a0Th5xSVtJDLT9rUKgTqdQMCKviCVZis3rsnRn-oqmya3p1jwTc1YiHCHBA3fubJrWUIDVvYBGdkP0eJ3mmnjkP8hHJ-3N11i1Ubd1ohNwfb6w1iW7v1ojVToz1i6YHuN_qcxypYMI2NzbYbHNGnuINvq8qptHP5lzwgGYB9hyqw1c4fdXLulKKmtFeaKpvqyvgvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=AOYy3yEtk3sGDXI_OU-x9eBojbvVU9oREUnXAkTZNwVciqoI6Xbq8By-l1R4J_F8zBqjSA_exeZUHO39e4XtkS391PNRlqYh89HwMOp_3QPALrxgV0hvV3R8smG3Mssj2XAkxlWLmCJmnmEm-a0Th5xSVtJDLT9rUKgTqdQMCKviCVZis3rsnRn-oqmya3p1jwTc1YiHCHBA3fubJrWUIDVvYBGdkP0eJ3mmnjkP8hHJ-3N11i1Ubd1ohNwfb6w1iW7v1ojVToz1i6YHuN_qcxypYMI2NzbYbHNGnuINvq8qptHP5lzwgGYB9hyqw1c4fdXLulKKmtFeaKpvqyvgvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105193" target="_blank">📅 19:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105192">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
▶️
🇦🇷
ویدیو جدید اسطوره لیونل‌مسی از دوران حضور درخشانش در تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105192" target="_blank">📅 18:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105191">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgPCdDAW1-s3Yugy5FPXj1lc3nCt_0_uUUeK5VqVPuSUBTBeKB4EvnaGgkXFxi167_z6iZoMsCvZZ3QQrxcEMQb_jcUOyNdX_z3iFawNaZZq5Uz-SV_2U7cRGDbSLrI-Gu-McdGvZWEysI29RGfPSVUV2jGTchg6WIJu0aIctETKj3LRDf67B7rq6-gypZJu0_X-gz8SXtMFBD48O1KQy5bHIjPNg_8bIc28WRXHgr_a7pIvNvC3R8TTEZxsu_Ycz8Cj3B9VFvcy06-14tn_CQDyAK-Rht2V0eNjK6T1K9yivuOmVmnfqGNrYglkVDsUzbUs4xpPZgItKMxlcMDyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
عملکرد اسطوره لیونل‌مسی بهترین بازیکن تاریخ در تیم‌ملی آرژانتین:
🏆
1 قهرمانی جام جهانی
🏆
2 قهرمانی کوپا آمریکا
🏆
1 قهرمانی فینالیسیما
🏆
1 مدال طلا المپیک
🏆
1 قهرمانی جام جهانی زیر 20 سال
❤️‍🩹
207 مسابقه؛ 125 گل؛ 68 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105191" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105190">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwtDvArBepRWr5jNNQ7yzyDdQcQM19C-G3IWj5YFvs4YN4pAtDoibQAYKdTGDPwcKD0fl8jFP42AO2VamJn6wTQunfLnHyW7raB-NGnNw61wtQ-JnSXdc1IZXIVN24drrKW1Qwq13u7j-QE2pE3_GmN_HuBB3s9I3QIhaWHz_GhumFC0cxdBAA3gfU9-O31Mq7DzEUapLss6_Hm0kGD-XeMRVyVtiPKvjmJSvSdNLQiEgNaWfmg01E9Wyet3tF9RpKVrA5CRxte9ea92X6af9lka6yYcbMQWyEEuUxOAIAQbyHiRCn5OybYGnblIW1UXiAvHug47mINN6R9yyrFVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐐
📱
پست اینستاگرامی اسطوره لیونل‌مسی و اعلام خداحافظی از مسابقات‌ملی:
🔻
دوست دارم، و دوست خواهم داشت، و همیشه عاشق این هستم که بخشی از تیم ملی باشم. تمام تلاشم را کردم و دیگر چیزی برای ارائه ندارم.
🔻
همچنین، بازیکنان جوان فوق‌العاده‌ای هستند که در حال ظهور…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105190" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105189">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQbOZ8fo-qyxAP1LF1v98AZYGfsi09diacCclx-HONCICjbeVyOFqPjYRmcwAJYW-FqxiJThCxmzX6cwbRtpnBGUK8IEl7OrosqQgqamEXjw_SqCqVbx7NTQm3_m5v1GiUbiTlIXKQ-BtmYuqGL4FrEoyQGYjvucSLN37VxinpcFyYy6m1RUOOOxjJPlYTbdoL5Jp_A__Xeobk6TNI_SfKlSuM2cNaUmYC_yzGku5dq6GExZTU9pxmWG60qNtn9Hzs7IbtD9Tb56RHs8zjK-6XDFgZpVPNIwCfwAfEat5fpzzsC765jA57bQEtU_JUnbOf-UIObnTBGLA83ba9Kkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری #رسمیییییی؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105189" target="_blank">📅 18:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105188">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4CEjxjUmIH9S4mqlptBNlu_IXujSrq5d8raZUZmhTAX5QBjzCI8tLZflgBNoRnW3F379qOIlG-OF7161LfFRODiiC08PwhKqkElg3G1gPLIj2rvLGUgkc4r-uL8qUa3RNEwIoMLFzoOAp7CugxoucPt4VlCUbhHXKMM41mpluXX_NwO9q5KaHddOpS10ijRp13Yxedd57lKokCLe4kpTrfwAsmwNd5UvLvQiLceBOWe8mZQm-ZPZ-BKU8n1ZKo7EyXg_n7J8rVatNTtDfWoT1wJQ3RKT3zNbzPOSeWvEGvI-9ZY2FDijX97gueF9koQIPeKRmG3qfk2ZJ_ppfrZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری
#رسمیییییی
؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105188" target="_blank">📅 18:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105187">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkozzaGQNHM0O6mDrXRdUb8BgbJ_KBKbIEJ7xvG6l8VDR6k9cQghz7d1JaiFMBkqQ7zipUh-t0im4eWYNlvpjs_XFvkZ_xzt42RHqY7GQTGEkDhh1LGUQ_oQtBd2JuuU4AqYGhmWQKKnK3dwTLc2P5mNjgSX693v6E4woeVWQsA3hHKZ1e7zOeo3Uy32KtZpINpVIRRDk1IFR0RD_f0N8sFA2LaRBsboUzuL-3TqiIoWWceYTT8K3C1bEJA-ALSA0IquL8RlC_yugbUJo4p_ONWPKun7Hj6zewbVC5DEipybyyrK-afB0JugLkFWdQ9hw7UgOZCMD8hcFdMDMUJMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
مقایسه عملکرد مسی و رونالدو در میامی و النصر؛ کدومشون بهتر بودن با ریکشن بگید
لیونل‌مسی
🔥
کریس‌رونالدو
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105187" target="_blank">📅 18:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105186">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D02sVGDw2PiEm3eWDN5aXO2UV3L7KWn5FBro5KKcgUI5HQZTWf-b8hlcwkWYUCkooBZZU0eNx0to3XpM0hj1fO4BDBYqfgVGw9H4bBIZzjmQXacllxbnLKrr_9GJmfCS70Rn6JPUbgjsPDQxbrgofsXqONPWUwJfrC1IEZIlJyy-HAZXorSLU19RpY70hyx1sr7-Tq8dGa5-izvH3x21EShds8nF0OKcVcfCMF5xS1SoBWiOXiTQUH2IhIadhLFMfAcq-KiAT7xs-WYUgmasPv7vCOoQ2wmoxKRbJM0O7c2m4EJnVlwA8NH8PgH3lPiFEG8cezHEt_y2s9WH_-IF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105186" target="_blank">📅 18:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105185">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=AVStLsQRPoSIOON0J9nxBRIA25235VztUWAvS2IUqbWihTE-MTsgMJGy5zT67AtJqrXpJGUrop5_TsogxV5lQzOMzt1bbyHz1Jehj9NlnshN8OTBtnHGjUYEIiUstUkw8yhHibXmynHs5Tusubfqg9n4fyVVBiKeD_HlaEWqL28YOmB1lIC9Fi9Ch88Wsc-P1xhQ0devkGtS0cjbM7nPMkOymZbqYnmlN-zwCLSq-NpNHoDCxP1yPH-lkkvumGcoQXjMESW9VpYcOkvkfNlvGmMsFdO6i47-aD1dxFJaMWXY-nQR2-_0T8dO97S3UN5Hgq3SGz8o0JiB9JtUDk7T_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=AVStLsQRPoSIOON0J9nxBRIA25235VztUWAvS2IUqbWihTE-MTsgMJGy5zT67AtJqrXpJGUrop5_TsogxV5lQzOMzt1bbyHz1Jehj9NlnshN8OTBtnHGjUYEIiUstUkw8yhHibXmynHs5Tusubfqg9n4fyVVBiKeD_HlaEWqL28YOmB1lIC9Fi9Ch88Wsc-P1xhQ0devkGtS0cjbM7nPMkOymZbqYnmlN-zwCLSq-NpNHoDCxP1yPH-lkkvumGcoQXjMESW9VpYcOkvkfNlvGmMsFdO6i47-aD1dxFJaMWXY-nQR2-_0T8dO97S3UN5Hgq3SGz8o0JiB9JtUDk7T_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
استادیومی که تاجیکستان در کمتر از دو سال ساخته؛ امام‌علی رحمان چه رئیس جمهور شاهکاری براش این کشور آریایی و متمدن هست واقعا
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105185" target="_blank">📅 18:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105184">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_2ib_tKK3vq65guw6WlW0b81BrW7P_IEf2y28eR5jxpuLuC18WisdQcEX6Z9lqc6ZZf7sqs_8oUR_XTajQmO7k7vdSfvyECgf1cxZr68p6VA5ztMyao-bMkan8342Fk23S4rJAspygljN_YDWVr6Oa1GTBgqN4Vnq2wkVlEntUJ_-uDsfY3vY9XiyT-WSdDqU7Vuz6mIxMWqMUJBWHAiWcrG1N2IUpGU2Frj6iP0AF5Qqik4Hh_uztMqIeqsfp55bcu5FTRgxieCtudmGU4NGiIHyrlx-HDabLqnt_kEvwnG6ejCuL2YG3DuQiDgIxYBpkMMgCwGr4hyn6Fyukp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
رومانو: بارسلونا هرگز از تلاش برای جذب آلوارز دست برنمیداره. اگر در ژانویه موفق به جذبش نشن، در تابستان ۲۰۲۷ تمام تلاششون رو انجام میدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105184" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105183">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105183" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105182">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2SNioiG0a-NOLRSE1FZNiraVsh_uk9mBEgF_C3ReXg3ftokvp_c_5OaLASacY0Wk2uZLz5XQmR1Zb7tbfnGxYW-m6bYTteuZERSinXo-x2fQ_0fUpUaBEuQJFdWO6Ovs-StmfdGGt418XlzJWFN02zojkiFvHO5diDqInmcxYj_xKvjfgCKRybX9O6Rev2fWkvS1y9WbC0JEcO1EogH6dvpmczjHQ5bx2gflmZcoUokI1BicokKks2RSdl60yNNTVvGa0OpysiZzBZjlcQc4ogB2yzKlwKWYZJz_E4PsWDofYDipuu_BsE-8jZh5mTEF0MWh9WWVwJJHJb4UU5kvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105182" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105181">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t89HJo5skvDYuSuCNWHPLiJyz4g5edpZzedj4D9oFm5tE7ggmFtLSAQXQsOEePFxBbA-I6OjD2Vg_Ty-gjxb7GaY_9NrJGpxyLMTFsMPtvde1_aQisIeXcOgd45SorCGVryR9Nksn6uZqDJ3IWjiTndMw5wbhpEd-Gm4Vk-VjUhafNnpMMl0saTWxndOGlYCZgwtULCM1BenVHoPAiuATY6GBAoMj-XPcSAkTdVqXMqN237RYTnXskvx6UaoXBofyOszTG-VUNf81M648mTUAb_6fzKQcU4rS2HFu7TSLvAJx_70R-AKuNG2ZPvIzzWo24yCT5D8d8mujBZ3I9YivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇸🇦
وضعیت خوب نیوکاسل پس از جذب یایسله سرمربی الاهلی عربستان؛ در مقابل الاهلی حسابی فصل رو به ریدمان شروع کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105181" target="_blank">📅 17:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105180">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×
تخفیف ویژه
× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم
برای هماهنگی و‌ کسب اطلاعات بیشتر به آیدی زیر پیام دهید. سپاسگزاریم
❤️
@Tiivaadss</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105180" target="_blank">📅 17:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105179">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOJMOEg5ZQSj8Civ6yIXjg67oDeHEPRETzJUmELkOcLE7ILzDYVa-TGOoiP5KcltsQnR8L0rNfLpycboBM0LhWwTyu3ggyxT58Ova54AJGUrxy__9G-5Z53u3Ogu5awQaG1TvWnwsd1PPBoY5lltTM6xfhuBSzNltTqPlFqMn2YohXbu9STuVytOysW7HZhiDcqddX58WAPl7tyE77dDChfy7GLRqavpVN4CeYSm5f909YmBfZ57Vd_qMBDGLFdEi4B5nYh-n1FeG1N5XmtjWUWdcy0w6bnkxfAo7o0AhZ8EgnM5X7uzrPJ29l6cJUVUFPrbcwD_oz7vs8qSZQUFyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
🗞
#فوووووری رومانو: کریم‌بنزما از الهلال عربستان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105179" target="_blank">📅 17:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105177">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOpm2ycGGxlwMw_K78_KBmzLvNv0ePPxam79pRlkJm9yzzG9svr3-7IDw2Og2DfuNYL2uValWiTMoMrwYmAYXU6wFEof8eqSwWaZVYnHNigJew0nAKjE8LEOVVU7pSB-JnbMNkqjXZZB-SrIGIigQU5hX_VeHOTrOrpLCWP021bn4GpTGzh9TVJJerp0BmvZefw3AwP5kNHae14bFX_bBwvbZ_SCGlO8S5IzGy5G5N9e-3FdqXu4bAgpMlakJZS7hRmi4_k5wWkL6c66sgSrjxOgmo6aP1MZ4zdYYUQ5ad8N9QwGwZW3Hc53Hh-IYI7UZH7vnhRapqfCadtBLJgvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qo2bJ50f87-OSYbahBQX94GhuUVXJaLH_5qZKgar5_HvEL8bXeKi9IDig-bRjXuIxDMBvP0D25XMulu_p4Vl4tiyZDf0jdohWabjCl8xlzj35m933_jKUKjgeTpDfdwkxUUOcSE21u2xBq575_oxDniIaWW2aqhpmEF8FLFsRBXjOo8ZONdt7ijt_OX2MoR0I_ZBdaiHJW_VV9nyaJNGgKaTWi07Dcc7ghEJLhkCXqfBor36CWN4U4Aq42OvqUpCADA0A4-M9HyOcbtvJwaEHK3rxXHafkLbQ_BA0dAaryqsPN-i6-6S6NrcGjPJHQMOv_wHgQ3-I9QTuR3Tnmui1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇺
اوا موراتی، مجری ایتالیایی چمپیونزلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105177" target="_blank">📅 17:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105176">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚑
🇮🇷
#فوووووری؛ ابوالفضل جلالی بدلیل مصدومیت از ناحیه کشاله‌ران دو دیدار آینده پرسپولیس مقابل تراکتور و ملوان رو از دست داده و وضعیت نامشخصی برای دربی داره. پزشکان حداقل ۱۴ روز استراحت رو برای این بازیکن در نظر گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105176" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105175">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بلیت‌فروشی دربی پایتخت تا ساعاتی دیگر از طریق سایت فعال خواهد شد. ظرفیت این مسابقه به شکل برابر تقسیم شده است. ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به فروش خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105175" target="_blank">📅 16:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105174">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15501a2dd1.mp4?token=kgqVBzZ3pBE-Ber2avTEL92GQUZPu3u28_lcqqqs9AkRnL59Neyg9tjk1KwvgKP6bMUqaUbQCv_VcSdyeRBamH-MgcItiIGgbfb4wencWkOaRApWT2W1mrkeRfrvNNnQaWeOqOdHr2e5Yt6kHZ0l-CRaLl1gnDdYV-v04sqODGwtOKVNc_RCDVOO-EAd9S2tuEHSb5onlskfmGMWNYO1cwX0cKV-nzVHB1DFhYnf5odQ9My5k63CMiVLgsB-WkAogvcd54wauoApeHAz-gC8wlyvU-30LTndU-Ok4br8-rFL7VEqCuXSRcvKMfPPI2uI8PcNadSX60c6uO16KrjQxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15501a2dd1.mp4?token=kgqVBzZ3pBE-Ber2avTEL92GQUZPu3u28_lcqqqs9AkRnL59Neyg9tjk1KwvgKP6bMUqaUbQCv_VcSdyeRBamH-MgcItiIGgbfb4wencWkOaRApWT2W1mrkeRfrvNNnQaWeOqOdHr2e5Yt6kHZ0l-CRaLl1gnDdYV-v04sqODGwtOKVNc_RCDVOO-EAd9S2tuEHSb5onlskfmGMWNYO1cwX0cKV-nzVHB1DFhYnf5odQ9My5k63CMiVLgsB-WkAogvcd54wauoApeHAz-gC8wlyvU-30LTndU-Ok4br8-rFL7VEqCuXSRcvKMfPPI2uI8PcNadSX60c6uO16KrjQxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
وقتی صحبت‌از دربی میشه؛ خاطره ورزشگاه آزادی با جمعیت ۱۰۰ هزار نفری و صدای عادل فردوسی‌پور زنده میشه؛ چه دورانی بود واقعا!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105174" target="_blank">📅 16:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105173">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">▶️
🤯
برخی از سوپرگل‌های چیپ از راه‌دور ببینیم؛ حقیقتا گل توتی به اینتر یه چیز دیگه‌بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105173" target="_blank">📅 16:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105172">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHs2x3ZC88EMkWx68JUpR6d1kxc6ngE3HP3XHaFyQzS8LQPgKo-2xaMkgzcR54M8Y1-Wwt5a80OvF3j-I78O7ZEoNbGy_zXcy3l4cYG-zW_-rnRr9Bo5cSsFO3JTqthRacrz-ox1cc5JRGGw5Svzqx0QLwK71Lwf9aT7TpdD651YTS8JnlSf01AzBZ7GxcObHVIiq1Tcex2Bk2PuA5Ntn5PgnGLL4BKUJJD2EatnwxhC7q_j-355OW7RdvRKOQ-UVdEEgYqy5NnFElY-HA0mumerQq15yc-QqXQcZG3Oy4b-y_VsSbGjQaNo3nCKbgxikCNKMV8t0le6xqO3QULW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
عملکرد اسطوره رونالدو‌ در ۲۵ سال حضورش در لیگ‌های مختلف فوتبال اروپا و آسیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105172" target="_blank">📅 15:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105171">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCymZVPsCP18UQYKdjWLG1VZ3My5sVPK-2WVDlWUPIn1194jumiX1cmHlEbdLzZi-mWKFq7iF1QeSVE1mB1BPVZaumtbOvEt_8DgwnJjjpoYYt23dpP_jfso6h0TzRAwwVWnI-foHNsfakClOGdJo9rc4bttySnpzGATdbc7AeEviPhJUe0kTQSptaO0Ns_46VNfXjPnF9_UMZaJ5sZv3AYhNNW-v4mySnShDlLbbbnVhJeNnIcKND2i6pLJ9oJhu9rprVxbGzwrX4Ep49KL0-okQ8AdQfRya7VonVumULBmvGYBPj-DwI2y7K9T7sV03Y69xtpVbiAfDo8QvPxU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
⚠️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده حسابی ریده به سرتاپای اسطوره اخلاق و مردم‌دار نسل فوتبال فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105171" target="_blank">📅 15:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105170">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCnWbHDDuh3dy3JOxz5eTqCwUjCq517jfuKGByALvwL2d_O6omC5o6fQhLDh8CwhzknXAAD8FbmtdIF0X00bmoqaM2h8avJxjfXUt96RCpLlPjC7Kj08xcDJWnXqlP8BFRbvsI4-wkXCAFdOSMknKQ9PhjZVoGNvwqjFTnNw31yfeVtnwya1wuJb3YYxk0cTYzuj-otm3XmrP6uJGbpwHkCOdm4ZxQ5Aq0l-ymKdnP85IzQJMbPlXo_z7NJYmmMUz1mjuBPMNeU9Kx5JopmVGBb4b9nZ8HkHgL9z8oI8ZgAToiNVkEz770wlDnB2l9un5MWCyY7624KN6CZ1E6yGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😱
❤️
💵
با رسیدن قیمت دلار به 210 هزار تومن ارزش حقوق یک نیروی ساده در ایران به
75 دلار
رسید. حقوقی که
یک ماه
باید با اون زندگی کنه! معادل یک
دیسک بازی کنسول
که در کشور های دیگر کودکان با پول تو جیبی می‌خرند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105170" target="_blank">📅 15:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105169">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpCZzxdYomysIFXvdatjXo7bqnn2iY3HLfNyoDJVLnQ75ecf9_mgMqvfSVlLhNhxEW807QdnSQiXvBjIeF7Nsdd-n1XUdp0NSmYObx7BdjbW9BLdeSRAzVR9XwqQjUJuR8bpC6TEyemgObVXXjMjN_91VrcObG9iP1fO2Wf1HprIVvBIynSayekIf5cT2RxWzpOS0W-c3Kf1BQ2ko49txiQkroIWetgwVj7JNTLHPsInTg8AUpJChzsV4WitoAX7xsmYGitcs5_-Xo2W1csEgvbGWVkoojIn96Hir3CWm5Uovoyj_d9ITmelZ46PWzr4dl910nCOZ2igmRFbvUL1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست بارسا برای بازی امشب مقابل رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105169" target="_blank">📅 15:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a916d757.mp4?token=C6xaRfM3AlpkJHBctbsIrZ4qg8ioN9ko46H9NCMVzsU2SWqfHJCbkmf0-IIexPBLZDnQULATf5wbFtP9Ep9eNEIdpwvZUDFZKqmD5wFrfqE9AOhLj_npRxxONwHQuW6YmA6XwOg2M4Z5b2mDN1VmKkHa-Ft-TS4-ATBG1XcIgqOUhW_P9AVaW3ktwNpCDzJtoxx9Y3lXJERlNl2m0PvtXslbFEaMIG3NAc22KIqnDqfziDIqGpNWWx834rHBj7vA3I07bEfVaL7k8yH3WeCon9s_oLOwnPkQz1_s1olyPoHvnriK4qzmBatEj6z3s2YKTsZFH_5reQoCP8rE7DrdOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a916d757.mp4?token=C6xaRfM3AlpkJHBctbsIrZ4qg8ioN9ko46H9NCMVzsU2SWqfHJCbkmf0-IIexPBLZDnQULATf5wbFtP9Ep9eNEIdpwvZUDFZKqmD5wFrfqE9AOhLj_npRxxONwHQuW6YmA6XwOg2M4Z5b2mDN1VmKkHa-Ft-TS4-ATBG1XcIgqOUhW_P9AVaW3ktwNpCDzJtoxx9Y3lXJERlNl2m0PvtXslbFEaMIG3NAc22KIqnDqfziDIqGpNWWx834rHBj7vA3I07bEfVaL7k8yH3WeCon9s_oLOwnPkQz1_s1olyPoHvnriK4qzmBatEj6z3s2YKTsZFH_5reQoCP8rE7DrdOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو سال پیش این ویدیو از نامجو رو دیدم که میخواد کوکو رو تو ماهیتابه برگردونه، شما اگه این ویدیو رو میدیدی از هیچ کار این ادم تعجب نمیکردی دیگه حالا فکر کنید همین آدم بعد کلی فوش دادن به جمهوری اسلامی دوباره برگشته مملکت تازه ازش استقبال کردن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105168" target="_blank">📅 14:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fea9db172.mp4?token=HrSyG9Upu7ebKkXu9tQZGAmIpGClso_yxJkOcQUeGXW8PRi2DuVexDBiWsL4aE3Wz0oLtjpr-Yia8P3jLWVRV04w8KyynYuNHvF_rH5ZEpI2Zz5M3CU_CkLKFNY8huzSrHrm5Wzz4HTOxIiTSBIBx6IpLbe2IGgyrs6yrxY5se7lsru1ZNzivJLwPT5j1U8m6dHpXjSraRvChdZ4l_G3hZh6r6IPtBowq84brWtxVBYSzsgncz7MElM40RTN147Il0nmqfQmhFlXlOIQB805H9F9dmX1-HUnvqR4NVrpQrKoGU3S3dIY1OwQQ9_onBA2yYfI2Ah08gQc8Zfy7A41QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fea9db172.mp4?token=HrSyG9Upu7ebKkXu9tQZGAmIpGClso_yxJkOcQUeGXW8PRi2DuVexDBiWsL4aE3Wz0oLtjpr-Yia8P3jLWVRV04w8KyynYuNHvF_rH5ZEpI2Zz5M3CU_CkLKFNY8huzSrHrm5Wzz4HTOxIiTSBIBx6IpLbe2IGgyrs6yrxY5se7lsru1ZNzivJLwPT5j1U8m6dHpXjSraRvChdZ4l_G3hZh6r6IPtBowq84brWtxVBYSzsgncz7MElM40RTN147Il0nmqfQmhFlXlOIQB805H9F9dmX1-HUnvqR4NVrpQrKoGU3S3dIY1OwQQ9_onBA2yYfI2Ah08gQc8Zfy7A41QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
🇮🇷
هواداران خانم خوزستانی در بازی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105167" target="_blank">📅 14:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c2e01cdc.mp4?token=Plf8qQjp48PozxCm-dHb9MdgsDozK0S5VIo1UoxrmYXwIwlsnW05iwLmlorwrM_FKCjmJnqANoYLbRKIqqC8QYxzOfB8R6JGCjP7YhX65ezP--yBUUeERb5T9O2i0nZYS_HwRm56p0fqOo6-nVjXNC198nMsew4xnO46CZ64K_5ferUzE0zV6sXFvx1KEMA0M-x8OzY-jTSNe74b4dJY2Q2Ka7ok7d6jqJvUtCYWLWk1T0iViW6IJP-_nU4Sk-ij0tQf6_owRO5yES-ham3JSeXKNpb4UOvAr2_BeS-PcfVdoTK5_IPrzrwN4W9IoX6_Z1Co_TYo51ubI0DQmYi4KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c2e01cdc.mp4?token=Plf8qQjp48PozxCm-dHb9MdgsDozK0S5VIo1UoxrmYXwIwlsnW05iwLmlorwrM_FKCjmJnqANoYLbRKIqqC8QYxzOfB8R6JGCjP7YhX65ezP--yBUUeERb5T9O2i0nZYS_HwRm56p0fqOo6-nVjXNC198nMsew4xnO46CZ64K_5ferUzE0zV6sXFvx1KEMA0M-x8OzY-jTSNe74b4dJY2Q2Ka7ok7d6jqJvUtCYWLWk1T0iViW6IJP-_nU4Sk-ij0tQf6_owRO5yES-ham3JSeXKNpb4UOvAr2_BeS-PcfVdoTK5_IPrzrwN4W9IoX6_Z1Co_TYo51ubI0DQmYi4KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها‌ ایرانی که میتونیم بگیم خوشبخت شده همین همسر جان‌سینا بزرگوار هست. چه عشق و حالی میکنه ناموسا
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105166" target="_blank">📅 14:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105165">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b552c4303b.mp4?token=GEzvQMRoZigWmoHXfwBM4YY-aaucr3Iu_qZR9sGrD6idCDiNndn5EgilYDVrAcp9aeXnXqMbaAEsdu85nKb1GPMeesPautWZhtQVyNlwFIZevxBJrZuXWvElBzkCw28Eg1QzsW7R_y5P4zxFwRis2NNI2tatu6nPIsYRyhJ86N2K01Te_ir5CnXIny36tmN-N-rNKjimh0VR8rkHK7ztXJfGyl4Ht1eHUPcNXqehTFIAxuWidI8MuH4keZ8aEjauuohrFnPQidw7xQZEyudyYVRrVr4mx0Qzq7q-oMNTgQN8gfNvMTEHTKOdgtMtLh_H0HXtuP2-T-H9eMx51ELKay3wxopepXfya2yxjTOsm7SPmGf3uEEZVm_n3Y28wFemrm5VNt7MH13KwC3m2RNqmYJPd5WsdeLtS0Xi53rcjDDPws7g7Bm2vy65uJLbvh80sIA9rwMCBcMhNsZAsHWjUDCejKBRP7WRb07vB8LmQHSS_ISx5lNg-UfhDZ5wpwaY01F8b9lbqJsyqOS3uq2HY-n9tz8b33Su2IG2wEXtpSgTt54JoHSjwAgnvAihO9hRQEFf1bEkMf9g-QewZHawfnk5zlLZo9DqurwNBG0-1Jt4vRBfYTmbEFvvtZolsTjnBVPJ3FghWkTxnNolQEABvsuWsWYrT1GUip8vdFL0Ld8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b552c4303b.mp4?token=GEzvQMRoZigWmoHXfwBM4YY-aaucr3Iu_qZR9sGrD6idCDiNndn5EgilYDVrAcp9aeXnXqMbaAEsdu85nKb1GPMeesPautWZhtQVyNlwFIZevxBJrZuXWvElBzkCw28Eg1QzsW7R_y5P4zxFwRis2NNI2tatu6nPIsYRyhJ86N2K01Te_ir5CnXIny36tmN-N-rNKjimh0VR8rkHK7ztXJfGyl4Ht1eHUPcNXqehTFIAxuWidI8MuH4keZ8aEjauuohrFnPQidw7xQZEyudyYVRrVr4mx0Qzq7q-oMNTgQN8gfNvMTEHTKOdgtMtLh_H0HXtuP2-T-H9eMx51ELKay3wxopepXfya2yxjTOsm7SPmGf3uEEZVm_n3Y28wFemrm5VNt7MH13KwC3m2RNqmYJPd5WsdeLtS0Xi53rcjDDPws7g7Bm2vy65uJLbvh80sIA9rwMCBcMhNsZAsHWjUDCejKBRP7WRb07vB8LmQHSS_ISx5lNg-UfhDZ5wpwaY01F8b9lbqJsyqOS3uq2HY-n9tz8b33Su2IG2wEXtpSgTt54JoHSjwAgnvAihO9hRQEFf1bEkMf9g-QewZHawfnk5zlLZo9DqurwNBG0-1Jt4vRBfYTmbEFvvtZolsTjnBVPJ3FghWkTxnNolQEABvsuWsWYrT1GUip8vdFL0Ld8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره فوتبالی هلیا امامی از شبِ‌معجز‌ه‌بارسلونا در نیوکمپ: پاریسن ژرمن که گل ششم رو خورد، دور و بریام در ورزشگاه غش کردند! جو فوق العاده‌ای بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105165" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105164">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
موعود بنیادی‌فر شانس دوم قضاوت در دربی روز چهارشنبه معرفی شده و‌ قرار است ظرف ۲۴ ساعت آینده تیم‌داوری بازی حساس استقلال و پرسپولیس مشخص شود. همچنان کوپال‌ناظمی بیشترین شانس را دارد و کمیته داوران تقریبا روی این گزینه به جمع‌بندی رسیده مگراینکه امروز…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105164" target="_blank">📅 13:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105163">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c6e037e9.mp4?token=WzODg-9H0YiB3yz0YCAhlnZKQ7Ywv6mulxKepP_4pOHrZv_wAdVFK__wmj16yV2Ixuw_nMrZTwo29M1irG_OiA6IPiMMf_ofuz9Ct-PgxrzPzuJX86GejLwLEoemb0SbTcMS-_YEzS73gmmfrSjnKIOwyidkYndXCdoSLPyf718LplMMTiyL0QMg8Mg0tPmJGHW5Lj9wfM6unoUzIzxGXCz862a581SXlFFPWzAva442w_O9YqCYHkvnqjTZFma0vlsrQlTqRLK0CYtsNia-OK8JEK8WPUe_marBxh_iMTOHNQoRw74tvAM1HGcTod5vvTIYvivTqz6ympamZmO16JnRv0VaRtqo9374vJ5M0iwqWrsWj9lXruQQxVer7EXc8tHjzTHqqdW7mfR2WODKRe2xQjQDN3mnCWKpUlXAbwQ-wmDh95nMGzJVhRjzV-L5oliBl7tzAKTePAfFdlSYiw7zgd7UzjfVDf8jfpL0B4iNff5obBAqAFEJkfj5iiCGmHQtWdvMrJ1KMe9OCjXPgEjMikTGO9Xl4M5rdAQYK6XBFv2IQgNRS7eDE3dSiFBUtD3p1lywYSbc3K5CRrWok1VD4pG_oms28kveQsPlUWO3pwu73klOoRstUgKgj3X_FxxgUWUsFI5fG5d9XQve4U-c2wNDkOaTOgluNZFbxhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c6e037e9.mp4?token=WzODg-9H0YiB3yz0YCAhlnZKQ7Ywv6mulxKepP_4pOHrZv_wAdVFK__wmj16yV2Ixuw_nMrZTwo29M1irG_OiA6IPiMMf_ofuz9Ct-PgxrzPzuJX86GejLwLEoemb0SbTcMS-_YEzS73gmmfrSjnKIOwyidkYndXCdoSLPyf718LplMMTiyL0QMg8Mg0tPmJGHW5Lj9wfM6unoUzIzxGXCz862a581SXlFFPWzAva442w_O9YqCYHkvnqjTZFma0vlsrQlTqRLK0CYtsNia-OK8JEK8WPUe_marBxh_iMTOHNQoRw74tvAM1HGcTod5vvTIYvivTqz6ympamZmO16JnRv0VaRtqo9374vJ5M0iwqWrsWj9lXruQQxVer7EXc8tHjzTHqqdW7mfR2WODKRe2xQjQDN3mnCWKpUlXAbwQ-wmDh95nMGzJVhRjzV-L5oliBl7tzAKTePAfFdlSYiw7zgd7UzjfVDf8jfpL0B4iNff5obBAqAFEJkfj5iiCGmHQtWdvMrJ1KMe9OCjXPgEjMikTGO9Xl4M5rdAQYK6XBFv2IQgNRS7eDE3dSiFBUtD3p1lywYSbc3K5CRrWok1VD4pG_oms28kveQsPlUWO3pwu73klOoRstUgKgj3X_FxxgUWUsFI5fG5d9XQve4U-c2wNDkOaTOgluNZFbxhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
‼️
⚠️
محسن نامجو، مرداد نود و هشت:
کوروش ایرانی نبود. حافظ ایرانی نبود. ایران یه مفهوم جدیده مال صد سال قبله. گذشته‌گراها شاملو رو نمی‌شناسن عاشق فردوسی‌ان، می‌گن به فردوسی دست نزن. می‌گن گذشته‌مون بزرگه. گذشته ما کجاش بزرگه؟ یه شهر مثل پراگ داریم؟ ریشه‌ای وجود نداره. ما چیزی از خودمون نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105163" target="_blank">📅 13:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105162">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabb21609a.mp4?token=AQi8BTeJr4j8VjAsWsCSCFXowiPmCwZapvXq0xvJHXdNmKpwMUa6WbvTmwOXFE6PdM6NzD8onysvEZxOj_7bkVMIQWtY_o5SwMfQYsUyOTZh7xGqatLTEG6k6DoqPugLdzA96-ftceINIr-ICkIEBwrDf9KAhFm-NXugK6RGUpccHoY2yplOdLdz7woVHx-yf5jsFMEOVZhxHMST5F_3Nm1jNdviWYmf55R7YxsG11tvjfNDDT7kl0wkhFAo8nebA7i6tuY_WLVxq8Z8a15CSA5_9GLfbXPg30J5KW_hic-UDd0faES_BUQ-Gsg1Prs20ZdD6JYgEQAuiPK3L-X4iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabb21609a.mp4?token=AQi8BTeJr4j8VjAsWsCSCFXowiPmCwZapvXq0xvJHXdNmKpwMUa6WbvTmwOXFE6PdM6NzD8onysvEZxOj_7bkVMIQWtY_o5SwMfQYsUyOTZh7xGqatLTEG6k6DoqPugLdzA96-ftceINIr-ICkIEBwrDf9KAhFm-NXugK6RGUpccHoY2yplOdLdz7woVHx-yf5jsFMEOVZhxHMST5F_3Nm1jNdviWYmf55R7YxsG11tvjfNDDT7kl0wkhFAo8nebA7i6tuY_WLVxq8Z8a15CSA5_9GLfbXPg30J5KW_hic-UDd0faES_BUQ-Gsg1Prs20ZdD6JYgEQAuiPK3L-X4iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
رحمان و رحیم سریال پایتخت: یه بار کار از دستمون در رفت جفتمون عاشق یه دختر شدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105162" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
