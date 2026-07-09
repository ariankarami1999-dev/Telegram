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
<img src="https://cdn5.telesco.pe/file/KX6WaudVpnhPjmhPkiCidedTWThIbMksinPEOu-qhPEugewpb1EwhLwr1sQbob9rBUbqUBzVnCfbwwGseXgIp6JmvBAn4ZFxKLiy_R8JQ9Aw_AW77ZNXA0vwq8F-RCL5pqa5qDKQw4LBgN-0lBWoFoHy-UbUJElEd_hAbOhp5nKt8eKpdS4LfdnS9gZbIAWx5GQUvC7aRYZLRxd1A5L4nOm_C0E9J1POBKKKi_7k-Bktv6YxkeLfbWv-_5FdJK-pVNB3eMfW4akYsCbYofXxkrF1QJBJUM58EObip5i9W6wVD5jp9feq7d0z25VLb1gEpvArO2UthRXk6JWylS4U6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 606K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 20:42:49</div>
<hr>

<div class="tg-post" id="msg-99238">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMP86KSnBVkYWffmgy4bM9h1_82iRNKm8_xcjzzBHjI77mvakJ5bttgi-8FKOFWxFDgzqu4_tUSzH26X-Hazn5zdyk1AhpGkMr1-Nd0WfDC3xdnBp8Y2C567fsza7ZZh2tUteAwG5y4sDorCsONaFC_P-yEBsqahUA8Lzs6YGt9NK0WAosCZhzWy8XBQ2lW7VlIXXG8AoF6FsOyT5gdVNhoJQQBumeJG8YLqaDLqkFeSeGgLA_r8UQQ_hQYpTvYvf2AnLrlizafkzQ8pE1Wqw3OTdXyVzKgSQZ8Er9PvDZhmoRDG5UiAcZJnuAOUUbW2m1YLJNFKHYeRkNq1Ev5e_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
🇦🇷
نتانیاهو: راستش رو بخوای، مسی 39 سالشه و اون قبلاً هر چیزی که می‌خواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی خودش رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/99238" target="_blank">📅 20:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99237">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJOE5q7awPifyKLD5F-NdPS-Wiv-RKwbXkHiE7uYrphktNdDHfLqfJKNvsTxvQZnsZB8TAR-LXhix4rlM20vNzLMPbdVjwRG2z6_FoqoGHbYsWS2VGJhVXIaeeUA86fNsT6czcpMHeftucEEzgI8qGmaRbkjWf5zfVtnPqKzSmkzVjygpyYdHs8N4bl-2_k85xSQlOtcwD12dVpvcZWFEvSI3LkTIirW3n4xIaZ6VeUbSoouA7wSC7iUET1yTBh_FrtObVW11NEaScn0IMwKfpWmGZJl_YDZCroISCSDLHr8Yz3jUiCHELpYFtCp1T36vrJvDfrqzJH99yy5jCG-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
کارل دارلو گلر لیدز یونایتد به منچستریونایتد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/99237" target="_blank">📅 20:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99236">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNydCLkvtR8tqTH9urLeoiYITM-ZpkPfiBieKYpe9wWc3-4qYFbEb0SHuzYdRwvOkkyVoPPw1pUFjfadf8t2qW6pSsEyWIaoUshYBeYw7CdjzUs_FrtUivWNNEWfUBmneIcIRCzP0FOcgMYE0USvJRnaVRVNQUL5RBw2zWGHRBf875MC2TswUK-rZ085DVzzAFfGka_vxrzpIYK4EtfvTlyJdWsu8V6zI0mfV4qA3IQ5flGS5ETnVrv2f38dIr271ZUqeb4qIv52jakb8tu3ujKImaChEaWn7oVutgyH9JPGrS7AU5ZNGC6OjzEjI53pu92snhbWjPBD46ycC1PtbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتامندی نگرانی‌ای بابت بسته شدن تی وی تایم نداره چون همه سریالایی که میبینه رو روی کمرش تتو میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/99236" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99235">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9MIMzoVj7p7qyAc68GNqtg38zOKsgDG-vkR4SwlRQr_birMdGFipyjj946fK7n5Tp8hfyqd0aiufr86KUMkwlvSpyoRt2ua3h1WkPkAbs9EOroojWFC_-FlaVMpueevGRqZ63Ip3tNUP4QaOdkn4VDbjyg9w7H95-4YMb2MssC1ZnKydylliakBHbXX1D_saABtNHUsUYtS8qM6kn7zqH-mb4MCFrnQv47JtcjywbQa1kiK0GqPHix2Bzi7vzyoNhGm9JFQzLhg0B56H1B5ZFjeT3FZN192jyvkw7neL2F4XHR2-4PUQUjrBOjQKes1W1z-OJNBWQqbEhk-AmMOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇨🇭
ژائو پینیرو داور پرتغالی به عنوان داور بازی آرژانتین و سوئیس انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/Futball180TV/99235" target="_blank">📅 20:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99234">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcN17fWIZAqG-aZQu1t9sZe8ARlKwMFWMpXFfwjGxf-Qr7kLXu9JwW_acobhhYjFm9oJvpAdw4bjEs78Bw8pDJfxp82U5nlsoxOkyK8TmPu2AlGQhtEjnyVN1wKsAOm1stOfAwfKtBvpOnN_Tt-y0lPIXKcHvX7eM_4wxgz7eq00y-YC1I61ACZElLmOJPft4PwC7xHYjf_e0eqbLlCmi3PCrjBu0ZOHV4LG3dLfOGPqNB5W2EYZyeVPgroJ4rbKczPSSJcf-WCrDIBTAqzOW00GAbG2vQpqzDlNfZSUsNP0TEQmqtZC2LhvnIVN0tL4U0xGBFb63qcayUcxE6ktXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بی بی سی نیوز:
قانونگذاران یوفا خواستار تحقیقات درباره اینفانتینو، رئیس فیفا هستند و ادعا میکنند که وی به طور کامل کنترل مسابقات را از دست داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/Futball180TV/99234" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99233">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66bc2aaa07.mp4?token=UHDZx6TzXow7moXi9raXXX_cr7vlhwsO5L1NX0yyNITmeHnWkL_C8F_xV3G0JwlkuuOrm9gpgQt8dn2RTc6J4QohduWA1NM6M1uKk6en1NdiEA42zygy0Ar1bMLQVYpcJx-jKISu8HkPoNOlotAwg-PGp9F6LD2bO9XoIlx_BLmguf0zwOHgviXo_RO41bmV5I7jWE45ZYG4EL8U5yW1tmzFbSga45UOmmd_69k4uK18b82ZYhQl0ZQyyvWmzQO_uLR8l1jZ_zs8IkNAltkIWxncrM_GzeSOTy0iklkdrrtX82C47k53vaOBNQfaBZqNhoUq8mNj6DzdOVrFuKkHKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66bc2aaa07.mp4?token=UHDZx6TzXow7moXi9raXXX_cr7vlhwsO5L1NX0yyNITmeHnWkL_C8F_xV3G0JwlkuuOrm9gpgQt8dn2RTc6J4QohduWA1NM6M1uKk6en1NdiEA42zygy0Ar1bMLQVYpcJx-jKISu8HkPoNOlotAwg-PGp9F6LD2bO9XoIlx_BLmguf0zwOHgviXo_RO41bmV5I7jWE45ZYG4EL8U5yW1tmzFbSga45UOmmd_69k4uK18b82ZYhQl0ZQyyvWmzQO_uLR8l1jZ_zs8IkNAltkIWxncrM_GzeSOTy0iklkdrrtX82C47k53vaOBNQfaBZqNhoUq8mNj6DzdOVrFuKkHKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریزمان تو اولین بازی دوستانه برای اورلاندو سیتی گل زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/99233" target="_blank">📅 20:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99232">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-q3YUKQNHCeWjbIxh63sjVNn9y4Hcp5iB51Cm5Wk9NEpixXgnb9CFyMnxSgGdqz_Vvb3-8ydJLMnpGkD4mMQWMnuxkSzHBrJoBdh7PjoM0RaHYDtPBiML5SjNY-ChbMacZ_c7XFdmENE4sfeyqlk7xgNG7NF3Ddk_ae6WVBZjgPADseDR1nqy1uh7LIuQ-D6D0GjAPrqC42C6FFkwpCukcL6u40BUg5H_6-xNDNtt-yZhv9-aBFq0DXBFOVcd5aedH2ulVD1r2otur5X6RRhkyQFlT_auaYRYTLoMZ8uYX5YqCxrLlr_IuApjPSHZy1-Fs8ca1gQDvBQJ3hNWp5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/Futball180TV/99232" target="_blank">📅 20:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99231">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de986e6ef.mp4?token=RcNAVtYuSuHZKta1Go60L5e974nQtW2K0mNsx317dDGXtpUGVPO6YOJ8_MAnqPT-yadCLFSRvnrR_xlMjwLUlvXlKAa3gROWWudpmZJZoOtPH3hHnR3ifBWSIb6xbXtzZBIIYPlJAnjsnNso4E87qFQONm62oKs31WzHlTHBMFwSFkj84AXYkRaju3l3QOflx8ZI1ce8ORw6N1_4oxGM0KkR18oOvqFEBoEiSmjD3JFXBPHZ5Rx5ssxfx5ukx4MitFJGp1Gu-l8YfivaZXDrVagznnIhHA_z14tDVbRIKJW-nsO6hb1HaNxTzTMNMegk9hodgzPbqSzsKC0_VCvPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de986e6ef.mp4?token=RcNAVtYuSuHZKta1Go60L5e974nQtW2K0mNsx317dDGXtpUGVPO6YOJ8_MAnqPT-yadCLFSRvnrR_xlMjwLUlvXlKAa3gROWWudpmZJZoOtPH3hHnR3ifBWSIb6xbXtzZBIIYPlJAnjsnNso4E87qFQONm62oKs31WzHlTHBMFwSFkj84AXYkRaju3l3QOflx8ZI1ce8ORw6N1_4oxGM0KkR18oOvqFEBoEiSmjD3JFXBPHZ5Rx5ssxfx5ukx4MitFJGp1Gu-l8YfivaZXDrVagznnIhHA_z14tDVbRIKJW-nsO6hb1HaNxTzTMNMegk9hodgzPbqSzsKC0_VCvPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال قطعا یکی از بامزه‌ترین و کیوت‌ترین موجوداتیه که تابحال دیدیم
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/99231" target="_blank">📅 20:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99230">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzgwGbGhv9X3KsbjN9L36qOcUZXenqCSQH4kITAAbhKDfQ65sdpgomNAYPv87cw311geIy3Y3rkDcrEwXH2uwUWmrXr-u1Amzar1PArqR73t4Re8XVBHu8x8ZTyjwXJhA2ryWZ4m3fsygqDSj1KhsI9tYYmFZE-gtz8zp6MATUac7oL4YCxthbjFhWZnF794WGh6AsMOzatq77cNjJv4MSgfBKu9HH069e0PfzNVhB6lWeZnYodxcb5DsKxKE2TmXk0_p-tozUoKqMhyiWuitCKsOKh3_SyZIa_oc2gtE0UmsoU4mxbf_MVyVNt1z_BiMPjvSHGtOgX_E2AA9JtB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
لوییس روخو:
باشگاه بوروسیا دورتموند، پیشنهاد اولیه بارسلونا به مبلغ 20 میلیون یورو برای جذب کریم آدیمی را رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/99230" target="_blank">📅 20:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99229">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg9c-qXofQG-SoZYIlT_dJR_iRy25UKnCk-T8_iqQiv8YtHM6qXA85j7CrKYkcqP-OKfqep_0jARvQlUxh88axburxIfp6mpiQX3kmbY_r9C05EOivQyW4Zg_FmclRWehvBEFCqulNhYTP3vexf185Y7UrNj4WXpE0S9nX_ozHLLkBBAsTAh_A2Rv3o7TDcAfhzptw7m-kxLzrc8fSaxhWkyELjKaJt9H8i-XIXZQxWw0RhoKyyC95yB3wSwe_y7S214HBvbCT0iAQ2J_ymLB93Gi82UUBmrE0Ec03DR2Qmrb8ZXu_m2fnd-OTSRYHx1DocUJnGzhk8o0jWBQSNoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
#رسمییییی
؛ کوانسا به دلیل کارت قرمز مستقیمی که گرفت ۲ بازی محرومه و علاوه بر بازی با نروژ، در صورت صعود انگلیس به نیمه‌نهایی، اون بازیم از دست میده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/99229" target="_blank">📅 20:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99228">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzvsWEoWuH8WASo46RI2_mXfpgmfSBkDgADFFrgD52vwJ6TMJisibcyqs1oNCe8hv3PcofRm3kfGvsFG1T3uAgo25GyxVjbu4guIyR7lwtZhDBKJPYzxq_Kqv90X0IQftzyVr-_mIw3jbNJHbln8Zgr9TZQ_-nULf7cNoqkvuEtRpL1A4QD-vlR1lykHLbOlcfwlV4BWWEUMltYYGswex6lT10xMoLlfJfyjHUMXFDFSkhoKNHwJiGgZaXbrIE6bM2yBwIt7nFPQfoomX8fz4L1sT2KmnZHOlfbBgfhbUZGuDzA4-iHCYZ8VXK6AbEAFMS_ewBzF6N-xG_efRhQxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
#فکت
؛
برای اولین بار در تاریخ، مرحله یک چهارم نهایی جام جهانی بدون حضور آلمان یا برزیل برگزار میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/99228" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99227">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU-UE0yM1HwCX1DX9a97wKBk7dUDmMa9yvx3P-LiszneChi0Fg4do-QCGm4kZDhGI0GBOty9syo_uNhcmSMGg5tfHdR1SJdhgxbuJ7vRgpm9WZz1zhpsU_GekYfVfr2Kr__Tei2Rv0WU9Cmdy7eBhAqcRS0PB2zG1qhWsRy-_KLr9AiD3KGmWONJVNxtfPIBr4QSB9DDN6QaueExRkrHd1uf0wZP87AhTLifDJ8VCISPpGrHM6UKKEUYeDfjF_Vv10GUxSYRZnFb7DUJ8QuOEnUXcMJROmnb04XWJ9kat6TB2kGs6znIl9_-cun1IFw5PN7k659Fuv28IRczR4Bumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بانوی پاکدامن میا خلیفه: امروز من مراکشی هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/Futball180TV/99227" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99226">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXClwSzkntCEzuc6knHrskKA--3yqty86gLgHMQ7UX0ykwq5oXkRJcsczejvKUXIZ_4h2IktyHR1lMc9ZnGhKz7qM6gICh4dCREXAcCE6L5M2yT12rXxywyb85jBSZSzrpzF2COEvUernTTCCsc0L9fhEVuNcuRFd8HfhQdhVbLg5_bwkvd4-1alXLCOyW-3-RRp-4WVUtYxoUKYduzYFP-NcJBmC11y4sHXkzNNOFP8TWC_x0B7iQMmx20eas2wKyUr9EiB7nCURnNPGaiOlfF1nt86rbrvkCPcPNoeg5jJ4s4gQ3BEsP5QfEiuaeUkzcb3qHREaSrqks_x1Kbmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔻
یادی کنیم از تیم منتخب جام‌جهانی 2010 که با قهرمانی اسپانیا به پایان رسید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/99226" target="_blank">📅 19:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99225">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvA0RcHD8ZsMfWh34_xrRjCVDM-iftZOnhRle17JzPsjMepGEXb6e15W-Mc4A1_7Exvtdx5qpXPiN6AlEOLUgZ03NkaGICkN0tabwckZy-hP0741ajYt3WBqBJMR9gj87IFI1qbUX53xYn2qxGm_nu_7pivVZPPGiO06_J6JsUQeVEo4j2xDWc1A0BkX2H1GX-cNq9VX9F0m09uGnHwS49M6CzkrJcIpeDUncqLmutRxwhAYlmWG5WxY8j-k5Kw5MnbBJTgBkzmM7Bbg5XrjHcACWITH20gXNyPL5ofDDDyTYfXTezOyPQj4aLcRF5UcwALmjbzFAUN4gidv_8q5hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پائو کوبارسی:
خودم را در حال بالا بردن جام‌جهانی تصور میکنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/99225" target="_blank">📅 19:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99224">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/99224" target="_blank">📅 19:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99223">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP075B2GhwedAweAFGdJcEKtk6ZtJKlRYsYW6fsKbhSUbdFhI6eUQk2EY47XkdRz3rLdKzjCXJm0nBXnk06y4EnEKtl_WtlgXnhzrQRHmTiO_UV_9FWSOheLAZZYtpzm1v3vgOxOzyF7ecMn12dAC15SsEx_xX5fFg_yrQTfp19s5gJGw4NPMqIfXY4xh7w6jcY-dbTFrRWeuP2mepWt7hwcEcq9K_wCvTMZatGPjmKrjaB8NURPvzoOeOnSVN-g1fQNmo44DoCj0Ce64isOkG31E0T8_Sr3lpgT2XKZdNZhTrn3ENZdMfrH8AA_U4p5VoywKqlvRanlqVzHoYLUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/99223" target="_blank">📅 19:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99214">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EK-Ht3pQgOwSZMyAApsHc4kRlc-gDFXSNYVb2vlBKpNxSOXklv0Ts5X4_Iw_4PdDnWeOu2WwX27UmI8dVh80-g9HUvpmZNbEkpAZ6hOaHkyIhFHLVXYCmRi7npF6Ou3utuqjgcNG-_dQgMHJnfhNxni2ANWx1CgdKaIFeALL_p6C056q3z1aCiKDXXkpgUCkTd8f5xOAC5cSkcf-Pz4PjAFwtjEy4hteXJ8C-qrLv6LVDVpMKZ2rC99ieFljEKFwgy5Txz656Gah2BnTaPn9UC7DRgCcbtof0EGz6WDnHYhr895rugbSCOCExa7qYoH50UWqij2bkuHXdUu5wBRLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RfAXpWji_4-qUzahIEjtH2gMI-ldsqgGBrM4pFVn_z6KaUnnd2PFG2I1HuB05cx8ia6Bgr6JQDwiwAvwgKd9XrqOXjtRD87nGgKJFmYgXB0ucOE8pgiq5XsA_t1Z29zOIDWE9Xe7dOeA3bApuHa1eGo7bbuhYgN4OB2CB4fzH0HkGL98g90rD5uKAyPMaCv0Lerc3r5pW0GppjEpPs4GVkslIjlyyubfdfoqvst7ynjZ_LHSxta4SMo_mPithCT91-tv74hupJLtBF85BZVDJIp-GXjSOt7ae6qInvQZDyj1eVufwmnHXSsY85QyicMlP9nS02SaTRlYMR2baypS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0iJMXWUF_6vPlJ5QL8BTc8N3hHfLvuIAGX888HGlKqLz1nVTzVEqqumxDZ0eBonlYIZRfvbGZzbXGJUnqSPVHRsevHXoteFwkXWuS5GoVbkoI-MUDv-D7BOfOaS1ew7GBNh8Zelbrc6ST6F9eoc3EjbNhtkFqsevGEqwbVoirUqXKeTIxL_jt-nV55aujr7Z7PnNf3aQS1SYxVbAhPdlFXlNjYID5dNjF4tdlmMFUfTHJSRy_3xMafarCwpUfock5zr2VP6LXF5rwzjDpSlZUi0PmEIaHAsBs10b_0iEpbMu8VLD90cRdQvDAeQImxkSXaKjvSCtXMAkzARqpVvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9OxsnKpcTG7kc8Nl43WrnJC59faAJtD8vNR3gMJM2_dW9KR6KAFTl5KRq9fqYAvei8TL78BJWEpK-GCI-ZNKuTWUoXUfBPJkUpQr6BoM2w1W8oyYlbjAVK6286ihnpk9qH5fWdf6QTIM17eRABBspsaVdQF1vLU23g6ptjlm16g23OpxRtpDtu398aZgJDhvz47rlz5bL4oB31jr3m1JXAYYT7B5vXM7cvyFmylKBd8b0run2bu1D87OC6nnFgDl1QlpknhsIbNnh8IBs10XuJDNZ3-oFaTdku_m1x82wetzUYbjPw6vU_e_ryYwD-l-OS7rdOAYkPOBaRESVVWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faylKcVJAGahovOVKv7139MutAiaIn_urUE5Slm5G3Xd8dPB9GsRUpCVqILTOuZI7ubsnlU4GixavHNCxlNRnDrOnDeEqWVwqLzGQBk_7mF3vin1mzO-Z_DNSWvb3s-OAKj8Zby1CiDkj4Bk8Ksj-GIcA7mnetb19S1ImCG-LLMiedmVRMWcIRu0ck8IRPZWlub-TC13Nd-iNHBxY0o8wtw1zggmHt-3i2IweeZAW_XJaxLvw8ITItWSbsN6Q8ixLgy0sgkf7PQjHVjIgPS3jlx8ZW4BDlNC-1lf27xZmKn-AdsS_CHW0Gey7kTtuih1CBqt_7R2eLV-LJISnGGg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrR1WAx3qRdTQF79E15wDlupPKWhhjOJzcWtJNHNP-vGTZUBipLZcfANB2j-1jIS-GEkdZerh1AZZSWHKQWBu3MmGv067ALVs8sJpr97cgM5Q-JRj4oIH-R2zBN9hR4op-4cQg8cJC3eVAmLblWAW4cGuYV3GH9ZrFg-8wP8R6Let4_t1PdH6-JwxEUeM70xW4c36JEyWHSmSxe4B3s2g7Rd6TM2GcD3g4mFIGjlwZ8MmZaQGqfDmyy8iVekEDaeyDEPj0_Qh2IXvSD1hZ26QjBsr1D5Q7PmLzMqGIvsuqQY5Bcvj_wziypsNzJLO3MPJj6IsMxn7Vpjslb9mCojzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HANMN7VFg3Ee0oD4ITHKsBGJJjbmHJLpk8AFUKRJnY6DxUdIlLhqmtp8RfnaME6VTr7BOBhWflOEdT297AhoXN4mRbHxUrYEkR7KFpbvWDK48FLEQ08oMU3ulhS-y5mHri7Ez5sOuVdZJCeMUcjTaeMUIRS4gaOi9lRlLgA5BWViMI0cMxmps3dfhromcxScRgo51HOc7MgNiZmM-G4hAkuu1qyRy1kqok5BTBL7mU0IF5eMXgguMeQkr8xsVwBJmhYOJvKrr0pmeenygkonC6JoYhFLgPYzzQgKDKuo2tMnXH1ZEHtMM6OskxAuaztRUfNkgCYVsjQlgDsyoofVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7K7uRx76iOf3WmsK213vZcJ9L8IpiIkw53NalOUR-5A0wCsa5UBVClm66HuyT1vHw28XUFCxc1zPBIT7fMhethVYhHjgfc8THQyPYa6_4egUqbrJ5jFFnXpdqMxHzxyVUamqi0A0QHPMBgh_sYZDObCBUWb18GnmJ2MHuk4rJPCREvHAvY3wcpeTZDa3rlpBV0dyNzhtOQRWyhEOBs76Y4hhP65GR-E9GQAzfvyFnJRZBaDXh2h1To-4DdpqAjwUy8L4i_IoPvncaF1coMImYHzHG1BGSdbjuZEEY255U00-ReZ3-o4Au4mFgkHg2REqRwpyQeiZYivPpbN1vVaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0pTRzjnFShgRv999Q18jSXWfbOj3B5x5k1wN_Mhwgh6TNsUZvrGPto8VUejHDf-35x7We6x_KKQMi6ExbOi1k6Rk5JZ6hHFViqdh5CQHOmAww_FUm610YesXIDG8rwNTWkg7I-zPS8ntEoDHc3DA1h_fM9i2opYlV2Mn8JjyoXDaHF1fKYtJMbyNo1tDSIjA2Artj18bHtwIvH5UUGkY0LwIniL8MFXI2fGPzlqdWl8I4Y-6NZMbkfkzoGtWZ4CfJk3MkwnOVTWH0Scu4w5Z0s48oI4pftXX1xfwSIJFxsNMF64Hiv4shTkTAu3koblUBJfHtWQG54HCJ9lHJ9QWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تتوهای جالب تعدادی از بازیکنان فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/99214" target="_blank">📅 19:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99213">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgNIVDNiSl7Xw2QXG1ASoV2yeNsM-Gje5DtvZGjHcJqAYcTYcnsxXsO3ii6GGOdksUhHxxDqq37VIvmFjTSs-yV3xot3C6IdD1qb2eZ5HZ5SJj_KS35v3itZDMejdF9G_lccTY7fSNg8wgaFF2c4QKTD_cYd2D0EKTsRhpPPey7WEI6NK5RHmyKgqAH9r3ldZ6Mu4J55-ciyHOr7v8ybOBaZrIdMKoxrQzCeDhyDdMX3MX3Y_WUUdx-mqKlcIq6wWm37ye-h_ZT5V_q3Duf9HcREaMM1KB3Uw7HTLSrLuVQfl_vLNV_Zvgqs4ppPGTJkx2auU75vpERLDlmoEpZpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لکیپ:
اتلتیکو مادرید پیشنهاد خود را برای جذب میسون گرین وود ارائه کرد.
قرارداد 5 ساله، دستمزد خالص بین 5 تا 6 میلیون یورو در سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/99213" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99212">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVWeafleUpKzBJnTapIfiuNxJvw6ujpguK23lZ9cjfgEAt599JbWckYnk8wOUxG5FaM7ru5huQel8MPmnbzoPGb_ufPGsphxLAkpTcQC3yYbYhDPz4epbKIt73tDsXl85IgSj7zUA7P4tT-AcNe2OMgvguGKPiHsGFiXyOWqk5xuS-jnJEr8Yy7XOxLGtHe2QOHgUGsHZPRM5wkXZrRHtHVHns5_nHxLN58S2pzhks1dQE3Ysao3vnFLLH3wShj_X6Ti1y3ZwQSjqHvNtz8eT5QYrgDTU6eh_-0IthNBYAR6qcMGenXn39cplAH7I2rDK6p1WTqvQVzJApGX0J6tCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لحظه امضای قرارداد آلونسو با چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99212" target="_blank">📅 19:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvWEsz9tIS6q5PpYeWK-z0qn7jIs7bQAu5u3meG4tbs-ix22xYcSFEdJ8LG9x8r4ok8rs_WtxMn5WWg_kGIFhtj3pfX8_L6Bl7NnjCYS3LCoPWX2DR9PHrVvwEvn2vrDgiTdCvHpDxlkwGOzbN5aqyl-fHsw_SKfpTf58X8hGNGtvNCwopCbvFDT3riuAsclnrh6x27_PyJPRO33O1e6u1E-0lbrXRMSaCAL7sd7bGRXE_asr_mD1yFHtopiiF06UI1Q8wNXfJlbV-QMBn60OLBxdpOe0Ae35913dJIrHmjgwGDnrshGIzPoljOCccjt-tUNE6KVpDrQpmYmu4g_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه لوئیس رسما به عنوان سرمربی موناکو انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99211" target="_blank">📅 18:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e9304b6a.mp4?token=Z8RvVIewz-AO7IRyXArqWkJup6H-9UMefluyBMkpSqTHybZXiIcVUdlYlWKU2xminYTXU4ig1qOMUCklhnpVNMMy5vs9HLjfMUxnwuuq3OeH6ZZ0wwHtPJHNUvyNhXGUVedt8KaAMpLRwebM_nnktZWIOF-LFC0RAneIGuGvtDJR2_NzpLI_fbvf5QrJLvPcnaWiy-zICZS2Hb7XxP8u6m_bmHsHL0RlXtDFWAyJmTZ0ZjftdkmTpcc0iaAm8egMnLorU9aGvXBmM8c_2UM7YB0_agD1sWlHGp-0SuiJPuKqG304hqwGqlKVKEfW1pZx8uVXa4RtFgR4z3BxAwe_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e9304b6a.mp4?token=Z8RvVIewz-AO7IRyXArqWkJup6H-9UMefluyBMkpSqTHybZXiIcVUdlYlWKU2xminYTXU4ig1qOMUCklhnpVNMMy5vs9HLjfMUxnwuuq3OeH6ZZ0wwHtPJHNUvyNhXGUVedt8KaAMpLRwebM_nnktZWIOF-LFC0RAneIGuGvtDJR2_NzpLI_fbvf5QrJLvPcnaWiy-zICZS2Hb7XxP8u6m_bmHsHL0RlXtDFWAyJmTZ0ZjftdkmTpcc0iaAm8egMnLorU9aGvXBmM8c_2UM7YB0_agD1sWlHGp-0SuiJPuKqG304hqwGqlKVKEfW1pZx8uVXa4RtFgR4z3BxAwe_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ می ۲۰۱۷؛ بارسلونا مقابل ایبار
همه‌چیز از دست رفته به نظر می‌رسید؛ موقعیت سوارز از دست رفت و توپ به وسط زمین برگشت… اما وقتی توپ به لئو مسی رسید، غیرممکن‌ها شروع شدند.
یک حرکت انفرادی، عبور از چند مدافع و ضربه‌ای با پای راست؛ لحظه‌ای که دوباره ثابت کرد چرا مسی برای ساختن جادو به فقط چند ثانیه زمان نیاز دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/99210" target="_blank">📅 18:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99209">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHnhgFIUmDbtQXRhG5GOictfrKHZYJngyBxBqyfcU3jZXxfzCNHjiG6KKmTXjlJ8pDgzyE8TsLbdZ1MvKGfAOoo5Ybw0EcoFanIOa2wf97UfGrmbJjdNx_00PHbeQxbR2g7s61ZiePGi3BEeTTdnBHJWqMaqqAEPDsDoetsNA_75KPwqpHKiFoAMu1OfQpRTFPwt8O8HNVVcDaBHdHygl_bisncFfOwNPlY2g0DajMtBNj4RyZYukAg0eSWEmYTtal6q6qVJHQzxD5fiK8FKI4zD4gNHb76SdkzWyrCScu7f-V20gbJI1w4skS76hcpUrqBxYKjirv0MGyv7Ev5mdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار صلاح تو دوران حرفه ای خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/99209" target="_blank">📅 18:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99208">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKiE0ipe6fZ3iLRbWLu3PLL42TetB0Vxlw5QgV70tfEdGkIW6y2Zy3_utYDziCLJhpQS4eobUjJjedGayMQLWXb0Zur1HEL9jwSInhrCGGI40VJz0tXhigPWI7leL1KgVIwRlSkuNAqRiPWxz4cEl5bLfRpXnbNQd_L-NQHQ7TCGaB9FsoTXVkHZLh5ttubYuLA4Z9Hmf_Xxd1xcNzAiAp8HB0pRg2GUWWi59JChzX__JFjg4s1pC9Kjx3381bdiqYiY62LVtHYbDPW4zcXmg_UV-njDyS_0073tPFKFq2tK8v7gMIb9mQbsZh7oi7dACRH41Hb9DiE61fOMY-L-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه و ست کردناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/99208" target="_blank">📅 18:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99207">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=rPN4QpdBaSfbx1zWmPLGj_xqANCLG3C2X7LZji9TSSaxguEBbX1ajZZfog8IoNwr4MojeWN6y2gHO5zCWjzMqQ1YksERuoRUMqE2tQsSnJZBlbafRj0J0T0w948K44mcLOcTKlVXdDqbZCPG5phPfeSVFVBCwXQHXiNa6mlzdlVNEgKIk05Y8KBZdwWAoqX8pAw8jbCW9pLGiwDdFmbkbEsXPsgDHt2Zc668XQUqawv7MIHThoxfOAeZgzl2FkxZT3_7c7fDzAmqdHNgMOYEYpEyY2Y6Eud-KqrfyYKhF8PmDIXRySXfL_Z53kJ3tokWc3j0U-3xm2tvjlNqu6Hhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=rPN4QpdBaSfbx1zWmPLGj_xqANCLG3C2X7LZji9TSSaxguEBbX1ajZZfog8IoNwr4MojeWN6y2gHO5zCWjzMqQ1YksERuoRUMqE2tQsSnJZBlbafRj0J0T0w948K44mcLOcTKlVXdDqbZCPG5phPfeSVFVBCwXQHXiNa6mlzdlVNEgKIk05Y8KBZdwWAoqX8pAw8jbCW9pLGiwDdFmbkbEsXPsgDHt2Zc668XQUqawv7MIHThoxfOAeZgzl2FkxZT3_7c7fDzAmqdHNgMOYEYpEyY2Y6Eud-KqrfyYKhF8PmDIXRySXfL_Z53kJ3tokWc3j0U-3xm2tvjlNqu6Hhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوري در باران بانک کشاورزی، از برندگان
۹۳میلیون‌تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
🎁
اسامی برندگان تا این لحظه
https://www.bki.ir/fifa2026lottery
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/99207" target="_blank">📅 18:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd3eab163.mp4?token=m2_x_l4mdatq49be17G0Ms6RAFmO2rIGW4Ay_15cCpmQUINt7LT7m3tWHsfCMPJS2LDYBbZim2erhAlSVaEMWSuN32g7vdPCZUgux_dOxug6K8F1OtCeav5bISRwDYjh1vgQ3U_lJCqRVKZMECnK7GCh_YIqv9BVj1FDYTnapCefww_V7iFGcTLyPpX8Bz2LymCYK5JmjgU_cj2Y04WdCfhRSIB8L0ZZPr5WKD_YjHnLj8q2EGU-ym6BP4AWYF0Dm4TG0MrEdSEuhlTtikm1iN-J3Mt_uHpug21gHsP80dTLNsrhnBvdT6UlpQnRa7gaPGuuuPD3R_inmlBm7Cgp8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd3eab163.mp4?token=m2_x_l4mdatq49be17G0Ms6RAFmO2rIGW4Ay_15cCpmQUINt7LT7m3tWHsfCMPJS2LDYBbZim2erhAlSVaEMWSuN32g7vdPCZUgux_dOxug6K8F1OtCeav5bISRwDYjh1vgQ3U_lJCqRVKZMECnK7GCh_YIqv9BVj1FDYTnapCefww_V7iFGcTLyPpX8Bz2LymCYK5JmjgU_cj2Y04WdCfhRSIB8L0ZZPr5WKD_YjHnLj8q2EGU-ym6BP4AWYF0Dm4TG0MrEdSEuhlTtikm1iN-J3Mt_uHpug21gHsP80dTLNsrhnBvdT6UlpQnRa7gaPGuuuPD3R_inmlBm7Cgp8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇨🇻
تعطیلات دروازه‌بان کیپ‌ورد در کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/99206" target="_blank">📅 18:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a3f6f2a0.mp4?token=OvDM7nhdiWtXJi5WL5XI8YZv8x1PinmCwE4VLHspo1MPc4dVqMNw6aHiUy-yNmxl9gv73u6846lrmoHpOafjSwMzIx90OXgROOuid3JOY1CM6CaJ4mVd3TL9ow8KWWVPPV3MK5svo5GnQpGfdbwN4vBkbveCa6S4CBwkhsG1vGlpXMcvNsNzAYF_dp9M0cZlyPKvvfCgDmoa41ign_3hE8R_QqXOLPX4_T7F2vO35tVp1ncN92mofco38PhooT4HKcU8y3f2xGNF38X2MLkhlIBEZKFBw2vD7FbFnFxPk2i4S_G5rLRN6z20PSg9WWV3x326A1VVOn_JhHB9mVGmSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a3f6f2a0.mp4?token=OvDM7nhdiWtXJi5WL5XI8YZv8x1PinmCwE4VLHspo1MPc4dVqMNw6aHiUy-yNmxl9gv73u6846lrmoHpOafjSwMzIx90OXgROOuid3JOY1CM6CaJ4mVd3TL9ow8KWWVPPV3MK5svo5GnQpGfdbwN4vBkbveCa6S4CBwkhsG1vGlpXMcvNsNzAYF_dp9M0cZlyPKvvfCgDmoa41ign_3hE8R_QqXOLPX4_T7F2vO35tVp1ncN92mofco38PhooT4HKcU8y3f2xGNF38X2MLkhlIBEZKFBw2vD7FbFnFxPk2i4S_G5rLRN6z20PSg9WWV3x326A1VVOn_JhHB9mVGmSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نظر آرسن ونگر در خصوص حضور کلوپ روی نیمکت مانشافت
: کسی شکی در مورد کیفیت کلوپ ندارد. اما همانطور که بازیکنان خوب مربی بزرگ لازم دارند، مربی بزرگ هم به بازیکنان خوب نیاز دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99205" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/033b9f8094.mp4?token=bEVKDZjEgDAhNXIxv-VDvCjuwgJ7ccAJjGtaqWDD4IxNZofvdkglTYJb7CQqqOwNnVY23BHDgqbARpX82MWucm1RT6Xk-qjZwFY5Cin7_W9XJXeAHNw1X5-oUoRZ1yQBI23K3pvoWfSsinjmQaXEMRSpzqR-vfKVdCSYhFEuauI01HNKvI14a4xnqgdcdFbYaDyFcKJm_K8mqs17oQmxyjEafNk1eXoQ4Cd_HUKIOrcY_5ISodxOLy2w40mvKcV_l1J_owR8K5iL8890m10Wl8itE_ZqgtVCCuxS33GyyNUTXup0gPhUf54WyhbRiOqK0k3FUXt8MJb4kYgeeGp00Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/033b9f8094.mp4?token=bEVKDZjEgDAhNXIxv-VDvCjuwgJ7ccAJjGtaqWDD4IxNZofvdkglTYJb7CQqqOwNnVY23BHDgqbARpX82MWucm1RT6Xk-qjZwFY5Cin7_W9XJXeAHNw1X5-oUoRZ1yQBI23K3pvoWfSsinjmQaXEMRSpzqR-vfKVdCSYhFEuauI01HNKvI14a4xnqgdcdFbYaDyFcKJm_K8mqs17oQmxyjEafNk1eXoQ4Cd_HUKIOrcY_5ISodxOLy2w40mvKcV_l1J_owR8K5iL8890m10Wl8itE_ZqgtVCCuxS33GyyNUTXup0gPhUf54WyhbRiOqK0k3FUXt8MJb4kYgeeGp00Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
نظر جالب مرتضی تبریزی بازیکن سابق استقلال و تیم ملی در مورد اشکان دژاگه و مواد مخدر جدیدی که فوتبالیست های دنیا به راحتی از آن  استفاده می‌کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99204" target="_blank">📅 17:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c8dc00a6.mp4?token=Y56DnCJkYEshQjJdZ5L6hpI0pxBnJsahFKMC5cfPQWslg5r5qbyHB_iocszUC8xlzBtKYddx5_1OF9VFEUjUPLRXJgjFiEKK9i2JVrP-OwjyUwtYQSQpH5A_5WItrgAUYlz3B3PfPUdO_cscNTK0GY9eE6-dCjZHGMYed7SqsK-a5oAx9OWbADiZybp6RTUi3jJIw2qZ5ZMUCE-zvRQ7MiZdoPN0kVu-Ml7cpqIRqUlhcwCvA8D3OYM8xQ_u9O6a3snIiIJ-O42tZTgFMdZbpR_oW_j-GiOmqj0Wld7wylRVpalFe4ArZ049KzS_2c57dC4_yyuRYuV0LW3WJtq56DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c8dc00a6.mp4?token=Y56DnCJkYEshQjJdZ5L6hpI0pxBnJsahFKMC5cfPQWslg5r5qbyHB_iocszUC8xlzBtKYddx5_1OF9VFEUjUPLRXJgjFiEKK9i2JVrP-OwjyUwtYQSQpH5A_5WItrgAUYlz3B3PfPUdO_cscNTK0GY9eE6-dCjZHGMYed7SqsK-a5oAx9OWbADiZybp6RTUi3jJIw2qZ5ZMUCE-zvRQ7MiZdoPN0kVu-Ml7cpqIRqUlhcwCvA8D3OYM8xQ_u9O6a3snIiIJ-O42tZTgFMdZbpR_oW_j-GiOmqj0Wld7wylRVpalFe4ArZ049KzS_2c57dC4_yyuRYuV0LW3WJtq56DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
🇳🇱
به مناسبت بازی مرحله ¼نهایی آرژانتین مروری داشته باشیم بر بازی پرحاشیه دوره قبل این کشور در همین مرحله مقابل هلند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99203" target="_blank">📅 17:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99201">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1F99m_1mSjmR1u4AczX0UvTeS4Ndb5Q5LYhoTE6SV0ydeczH_UwsV0EU_WKMJUEJi7-ymrSYoGnfs-DUNkAwDYOfInnpkFljBIZoyKmkbki96l0Bm8WXSz5nHT1ystalrIlqS_y5-n33y8g-eAiKpf1BbquU2-atXrf9yXUknoB9ecIphaG3CnPksFuygIuNZmnyhxbREYlW-8ExBWtW-_CHZg7_6c_LE6pBrLLQX9BJIuuz_XtdJL8bTf_l3Y_fPd9S87fXxMAAFSzQJHhECFabFIgsAJZxJfPgjKDxMRhJ9Om4COqOs6aIS5LEZDfQytrdTAa3LjrVWi9I4kMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rsi3evXSD2qiN3vtZ5lYwNcTC4zo6QereFC8_GhyR4ovBA6VM6vbVEKs5S4MhdRKzR09QdUIImAblo9aomQuEeNe4AD4I5AuBptxwgr9gNHvfVUvrL72MEEmENeGzWZjWzkdIZQ4HMuLM3jm0JYe0g-KiOHVpZOlzp3nYQpAzxAedJSGgeYys7sP_4V0GvUvRnQzgmq91hpdAlC3X6Pb3zHLloK0GuPAnKT5ZOc8IFdpbLRDmlhpLoBRsmT0xwePnuztI8uZ08lrxqFmUEXMVrL6toRW8gikybrLNMEsxY3lX_vG8DZKhbT09m0zcoQaesgpwpK1sqSo4SduXa50CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
ژابی آلونسو در جلسه عکاسی به عنوان مربی تیم چلسی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99201" target="_blank">📅 17:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039d015f28.mp4?token=NWOLFQsdMP8TbsmDugLBJDreQMibc3qDjaJ5SuOymE6vstnr78M7qL2weVROy7wJsjWUwxiMTIYolnQJrp38RHugod3cASWJlevlHAu_UaliSpMwpjWkYsWI5wlJaQE5pWcpJ_JKzwc_Z65VUmXPn-cKULK9nx9hwOqwZEodZj0hoWsOmm9J7RwJ2E9Da8g03YKe2R4dV8-5NlzRbx6bd5_WcEyDjEPSBn8DAQfjJeebkrejXJP_ypxkldW1fqzQhKSEkBGwjb1MDmhp8T9449-v4KTt9HyHogcoAE6TGCkrSqcig5hAjLAeiRGnpTpJdLhhFHUncMMrcHAFd_8vhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039d015f28.mp4?token=NWOLFQsdMP8TbsmDugLBJDreQMibc3qDjaJ5SuOymE6vstnr78M7qL2weVROy7wJsjWUwxiMTIYolnQJrp38RHugod3cASWJlevlHAu_UaliSpMwpjWkYsWI5wlJaQE5pWcpJ_JKzwc_Z65VUmXPn-cKULK9nx9hwOqwZEodZj0hoWsOmm9J7RwJ2E9Da8g03YKe2R4dV8-5NlzRbx6bd5_WcEyDjEPSBn8DAQfjJeebkrejXJP_ypxkldW1fqzQhKSEkBGwjb1MDmhp8T9449-v4KTt9HyHogcoAE6TGCkrSqcig5hAjLAeiRGnpTpJdLhhFHUncMMrcHAFd_8vhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
رونمایی از ارلینگ‌هالند در آستانه بازی با انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99200" target="_blank">📅 17:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99199">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPnBEjnCZu9yhMaW9yx66hyFuo46rMs6iO4_7QBsmDuu_4DZvpIYsT0x6RgwVY8UdlG_mEzdRUC-X9bopluJ08mUQWv5wfOsZX6jrubaeGlZcLjYmYF-YF5XiWVW5WKNFpW5b3oyE_Qzc8GVwnuwjfZ8HBFSTem30YmLlCuWVp-SpdD-wPPmxKsi9SRc6-fUEClq_e6irbiNwSt82F_I6YLktGv376IDRiB7KeXAZnFOikJHhTA3rmeiE4QVLZzpAYEUGhLMK5rJ2FUP4rcOvkk5Xpod5elNi86mE36KvKThTxqcvJrarTVyJVx8sRlnk9q85m6xHZ7OH1cNTPE20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
باشگاه گالاتاسرای ترکیه درحال آماده سازی پیشنهادی برای جذب ماستانتانو هافبک آرژانتینی و جوان رئال‌مادرید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99199" target="_blank">📅 16:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc2675cc5.mp4?token=P9PMzFyF7iltMANuTgOCgBiXIRSDKoxRD2RmlZucsYbvdMRMPud4n4K_v0JhQUYauXh4j2qco94m08UtFqdCc3fYqX2HGM0T53grSFJnF9mUCdBeltrYBMcka6sTk_IoTmBOQUpFh292yhU_C0dg6o5I5Mxe1JO7IlhfGZJuRLlNhpa54SjVlqoOdc4O5hig1yacfJDtrOOZNJ77U2Q46KnlDY5iLcrugDQulpoiOvdafo7-pf1sOF2qDvsUQD7ZrCOqaVtFrMWTnV5oqyufMndo6jUkDlgx-1yv1gDwIl2QklOPbis1vTVenIuWurektLoCidqumieItLCpPAitMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc2675cc5.mp4?token=P9PMzFyF7iltMANuTgOCgBiXIRSDKoxRD2RmlZucsYbvdMRMPud4n4K_v0JhQUYauXh4j2qco94m08UtFqdCc3fYqX2HGM0T53grSFJnF9mUCdBeltrYBMcka6sTk_IoTmBOQUpFh292yhU_C0dg6o5I5Mxe1JO7IlhfGZJuRLlNhpa54SjVlqoOdc4O5hig1yacfJDtrOOZNJ77U2Q46KnlDY5iLcrugDQulpoiOvdafo7-pf1sOF2qDvsUQD7ZrCOqaVtFrMWTnV5oqyufMndo6jUkDlgx-1yv1gDwIl2QklOPbis1vTVenIuWurektLoCidqumieItLCpPAitMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
👀
دوربین اختصاصی لیونل‌مسی در صحنه گل‌ سوم آرژانتین به تیم‌ملی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99198" target="_blank">📅 16:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0PHqVshh49__6HuPmd3iUIXSVSgzwhOqHrqdxxzLsD69dGv7q-Tv8exjx7SjuMoayZbKiUECIdwD22ZCTWPt77HXjbICLXzczCpQRpOqdskTHh-yd1C0RoqSRw6NaTVyXo6y9PIlSIkJladfhM6BEu_hljJQdZ5SLWjoifyEQyjPoo0Ue2EO52P5KUrPh_Nf7fIo0bGVZnkGlvzOD9J8iB9FlT2v2u0QtutD_OkOOktjL4Tst69E5SjtAS-DmHqPCltSG7sk0KtPeZEVXjRYJuKNXCXHt88ivhjfeVoQGbVgDd604NizCfsL0Jej8wqzit4siI1ED2V-SzgSvW4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کوبارسی رکورد جوان ترین مدافع که به 5 کلین شیت پیاپی تو جام جهانی رسیده رو شکوند، این رکورد دست مالدینی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99197" target="_blank">📅 16:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVwh1aT5zYRv_B4OfIarOGyLn2e7TXs5u3_wjpHmRVwuTvEzlDADhVFB2d3KDoREUVFM3ftfLJVQqqrOXmPRXEhBzwzJxGmby8jv7aoIIxOu7a7xet3HaO5C1KjMb_FOOjUeNqEtQp4w9njiFWQWq-kmIOLMwSV6kO444NmwAI3de1M7ZeIIq8xKTIka6V00sOymSL8OdbswVcy7HET09w8AYiJcuVKh3ST-McYoYzTVRm8kCl53vFL8zrNMzryiZHK2Bl01luHBVbml-R7u2C8fmaLd4LX_D8Wpz3R8kK7xbPb5TbWjgZQ7roImFRoDs1HNJoEc1SPfF4Ecw95oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پوریا پورعلی، پوریا شهر‌آبادی، مجید عیدی و علیرضا علیزاده چهار بازیکن گل‌گهر سیرجان هستند که اگر اتفاق خاصی رخ ندهد بزودی با پرسپولیس قرارداد امضا خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99196" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99195">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef7ff1dcb.mp4?token=RiEi8brA-McOgyT2-9akZK5Lxzym3OVriZtmxkHxynvpsffBiqPsoHJ3_WRGWS9xWepXDqPFhux0meuhkfCycTX7wEbwS4Ld3Hi9iWPetTrDoyB7MAbwFsgl5dmZBXd--Nbsw2gZhkvpLAWtGaNhQJJbBJlLbMSY5-kGzg8WHkCIDkyk-qsW54iIarXerSAHBj2Ou3CHyyOEw_uYtE2VUDoRmAZG4QnIjT-8Q3YdDhQ0btao8VmAqKpAXdgNwRHmbcfauAJXOpg8pRmri6oKaA23otPlSVdsnyfefucU23TKbsHcQIKwwJ1afcgY8sKnK1p5I-zatp9AnNhD9-JbRLuWSklHaHeeHcYZJsttzDcAky2RG2snTv4t5CGQ8OsJ38cewyD8fbUO-a3tO4bMykFBhmGay5P9L8QPCdC2izDJoSBOJLiKGPsBduog40xow1T1gJ93x0-kv06o1unQCaoTrXJUTTiF5yQtRyPYbEOznyi1eajAn3oFJH9cyc2JIg7Ud0FCobsJXOssYk4UlT22BWq-gTXZ6ebSGAe6RoYTjhQZcZ3cAFMs2OZPknrjfzIGRatjtay7o-J6zGZFUMLR3uw-EqoF59OB-zFo25mZy0QM46Jo0RpWjF4-hvHI_IMCoaAjlKGo96qSkAICUWaxTJvZ5mcecuchhlt14kU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef7ff1dcb.mp4?token=RiEi8brA-McOgyT2-9akZK5Lxzym3OVriZtmxkHxynvpsffBiqPsoHJ3_WRGWS9xWepXDqPFhux0meuhkfCycTX7wEbwS4Ld3Hi9iWPetTrDoyB7MAbwFsgl5dmZBXd--Nbsw2gZhkvpLAWtGaNhQJJbBJlLbMSY5-kGzg8WHkCIDkyk-qsW54iIarXerSAHBj2Ou3CHyyOEw_uYtE2VUDoRmAZG4QnIjT-8Q3YdDhQ0btao8VmAqKpAXdgNwRHmbcfauAJXOpg8pRmri6oKaA23otPlSVdsnyfefucU23TKbsHcQIKwwJ1afcgY8sKnK1p5I-zatp9AnNhD9-JbRLuWSklHaHeeHcYZJsttzDcAky2RG2snTv4t5CGQ8OsJ38cewyD8fbUO-a3tO4bMykFBhmGay5P9L8QPCdC2izDJoSBOJLiKGPsBduog40xow1T1gJ93x0-kv06o1unQCaoTrXJUTTiF5yQtRyPYbEOznyi1eajAn3oFJH9cyc2JIg7Ud0FCobsJXOssYk4UlT22BWq-gTXZ6ebSGAe6RoYTjhQZcZ3cAFMs2OZPknrjfzIGRatjtay7o-J6zGZFUMLR3uw-EqoF59OB-zFo25mZy0QM46Jo0RpWjF4-hvHI_IMCoaAjlKGo96qSkAICUWaxTJvZ5mcecuchhlt14kU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇩🇪
فینال جام‌جهانی ۱۹۹۰ میان آرژانتین و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99195" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99194">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99194" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99194" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99193">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99193" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99192">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e630de904.mp4?token=UJBNX6z-nXGB6ntldIbJ1JIVszJS0sMFUcosWLkQjfrsrd0A9IEbFKwi0WcL3y18E6hvKrEc2wCgOgKuLxqA3baARSRBxhBU_EB4t8_Jb9o_LGEBaIr-Luj2FDrODVKtf1he3vqT3u4pTXb6HoCoQkYoGKzXoFQ9VPZG8fOJUWIkBUoBQdbEAGVn0rluOY-zf_DnYLlEba-FJQwzQs25Jj66tZuXdjTzBqjTqCvtNRPCFOrNPxr1GGjC1qG3w4u0j9IYj8BMM5aOQc_htZqtFjp4EY1n4o8-oxUMIWE1nFw8bMb8CUzNqVKk9ulpsAmoy4HbpZavpembp814zgFJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e630de904.mp4?token=UJBNX6z-nXGB6ntldIbJ1JIVszJS0sMFUcosWLkQjfrsrd0A9IEbFKwi0WcL3y18E6hvKrEc2wCgOgKuLxqA3baARSRBxhBU_EB4t8_Jb9o_LGEBaIr-Luj2FDrODVKtf1he3vqT3u4pTXb6HoCoQkYoGKzXoFQ9VPZG8fOJUWIkBUoBQdbEAGVn0rluOY-zf_DnYLlEba-FJQwzQs25Jj66tZuXdjTzBqjTqCvtNRPCFOrNPxr1GGjC1qG3w4u0j9IYj8BMM5aOQc_htZqtFjp4EY1n4o8-oxUMIWE1nFw8bMb8CUzNqVKk9ulpsAmoy4HbpZavpembp814zgFJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام یامال به رونالدو در تاریخ ثبت خواهد شد.
👏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99192" target="_blank">📅 16:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99191">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61fb637797.mp4?token=tQ5tllmziT-w52PoZdGNmlpWE7toYK7zf8jUZDWgdMqs4nHHxcFxguPmbazhYElElZbU92jfD_xWQnehP9axdyHztryrATxqVLP4mrupU7lVur4r1kU9bpc0ikCMriqiA3HISsg7lX33b2wWPmhG2Et2YXoEwbgsT3x2vhOM_tNk2DMXgbtrGnImazmjcF0RvbAk1rcPqZP-2KkpPY85WO_Z2BiI0drBMJxpn0dBIfhgWSwiryMHY8Hfl_90F8hrZClJygoUCVIKrahNqZWZCmlsodY6apa5lkHBzJcOsBvtF6PWGfv_2utLOdWGjUF0bXWRYAFPsZYQKvgqF4nMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61fb637797.mp4?token=tQ5tllmziT-w52PoZdGNmlpWE7toYK7zf8jUZDWgdMqs4nHHxcFxguPmbazhYElElZbU92jfD_xWQnehP9axdyHztryrATxqVLP4mrupU7lVur4r1kU9bpc0ikCMriqiA3HISsg7lX33b2wWPmhG2Et2YXoEwbgsT3x2vhOM_tNk2DMXgbtrGnImazmjcF0RvbAk1rcPqZP-2KkpPY85WO_Z2BiI0drBMJxpn0dBIfhgWSwiryMHY8Hfl_90F8hrZClJygoUCVIKrahNqZWZCmlsodY6apa5lkHBzJcOsBvtF6PWGfv_2utLOdWGjUF0bXWRYAFPsZYQKvgqF4nMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
▶️
🏆
دو قهرمان، دو قاب، با هم و تنها
🇦🇷
🇵🇹
تنهایی کریس رونالدو بعد از حذف پرتغال و مقایسه آن با تیمی پشت مسی، بعد از صعود آرژانتین
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99191" target="_blank">📅 15:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99190">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKmHqRUNl4qoQ-11j_69e_jPLKHDS-pwtrH_eO9FH1P2wkIs5a_mOR1iK9tJ9yy6Dl_lpidq-ehm4cViU4z0lxjWrhFFTrB_VTmLt9v2WFaM_fSvqArLpNcjlzjcPmPMxpQJG1xi72Y5BGNLBp5gpufZNKgStiHKDvnWZp0jUgmhBAmW4GK1ZXbU5UQAV0apvAHgxgdt7C4poBv632y0Cwjgyb6jIxD_Xr5Rx9wqQLdMVXIX4kdBAwQhsUQELJVfKno_5w8p_4w_EL3O562oHlA-aI11rAGIUB3yAE1KcYZb5H5yccF7kfiH7ivFUk9GqimzC-TjqWQY1e2EjEH98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بانوی پاکدامن میا خلیفه: امروز من مراکشی هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99190" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99189">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=LPV8UvtwlR7F9ESpMHSJwoRdp71db12lGd7NJ9pmY8axxE-jik0Qr8JEAusHMP-8Mn9PlwhO29vxPi_or9ALJgkKANCFhetYU9XuRVp-KWDvev1a0Z-oEpT1fykB9sdtMzywbCAcWSfJbTSyAcrl8BXNXUIYaLye293r-74cAwodY8cnjzrh_86-3DwuE39TxoAjU5gRXqrsCJ0NA0zgcnOLtCLEMD977HV0bj2wfYk3kh0Q_0B_E95ydECB-pPleMtarRQuACw0k-Qs3pRq1gCxfDEQzi21nB85mBSk2_7uPQLIXJmqZDQEvtMAJB7l4sb7Hf5MhW7soeA80erw-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=LPV8UvtwlR7F9ESpMHSJwoRdp71db12lGd7NJ9pmY8axxE-jik0Qr8JEAusHMP-8Mn9PlwhO29vxPi_or9ALJgkKANCFhetYU9XuRVp-KWDvev1a0Z-oEpT1fykB9sdtMzywbCAcWSfJbTSyAcrl8BXNXUIYaLye293r-74cAwodY8cnjzrh_86-3DwuE39TxoAjU5gRXqrsCJ0NA0zgcnOLtCLEMD977HV0bj2wfYk3kh0Q_0B_E95ydECB-pPleMtarRQuACw0k-Qs3pRq1gCxfDEQzi21nB85mBSk2_7uPQLIXJmqZDQEvtMAJB7l4sb7Hf5MhW7soeA80erw-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
از کودکی تا تاریخ‌سازی با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99189" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99188">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=nwSAWC3AFhNlpoVYiBz79L46Py6hea1TCmcVwl_DvLfHSFUTjAmrPrngll8cMpX9mcbplkvNyiBYu35w3WcqFcoloao7WmwzfzgF_WYuMZk_xVoeWoPgFYlBDGmSMK6Mtulkg36eemDtizhwQ-zrcSNfnEXIKHFYOOt3H217wUEprnkX-CExwuxq2eIKSkr1P4Hnd2PPjnuzXmSSrD6Bz0jrLy34MN5nzCOXd1ZnIcpH7skPcm2O0XH2Lm6zbhfgh9nOg8jdhh3u_DxtsJ8DYhYgfhRldZJh8GZ7q2KAOgbguY1CEKo84sGxHt-YD-wLvZkxo7xJlZ3uBacpqDQr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=nwSAWC3AFhNlpoVYiBz79L46Py6hea1TCmcVwl_DvLfHSFUTjAmrPrngll8cMpX9mcbplkvNyiBYu35w3WcqFcoloao7WmwzfzgF_WYuMZk_xVoeWoPgFYlBDGmSMK6Mtulkg36eemDtizhwQ-zrcSNfnEXIKHFYOOt3H217wUEprnkX-CExwuxq2eIKSkr1P4Hnd2PPjnuzXmSSrD6Bz0jrLy34MN5nzCOXd1ZnIcpH7skPcm2O0XH2Lm6zbhfgh9nOg8jdhh3u_DxtsJ8DYhYgfhRldZJh8GZ7q2KAOgbguY1CEKo84sGxHt-YD-wLvZkxo7xJlZ3uBacpqDQr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
حرف‌های ژوله راجب فوتبال که محمدبحرانی از یه زاویه دیگه برامون تعریف میکنه. جالبه ببینین حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99188" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99186">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkChTrs5DheEOn_KcE-7YPTW3o50Fwe8tfnlQwT1FedtzA6GwFoTPxtFtrprtFXi_ckqz_b8vEspPN_wO_6SgVa3M8hKxmazalfCFaBhf0335Ei2xzpJ48MecNv18JphKWgJ1TFKcqx6D9LI9E9FDrnJb6TndM0Ys7L-gAJA8lsnB53CKwOpsZp9ScASohB4iyqdLqoAw2k4UoR4y-8wsfqt5cR2k2aTvyHRKKanskh6L94uRqxh6MseVLDLZ8Se3yU8T1ivHw0MhQTVGIRoZlevn4VgDKA_fonyWczitNCmDKnM5GoMCCqncZgkmDN4qDxAlRtA0jEMaXBAJzemkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkBtFk_ceNmQcN-Gr8vRLpWleEpsg7yRb7SDHD1R5mmTOatXBOyeMuC3nQUGDZRmELg1AQL71d1vJGI4TYCt4Cuw_fM05svvvsp9ALDsUtuwgqYZrcWooCTerjbLcNlhFv_D6WEq5EdlHkOGVqR7ttEsfRsI3uJAFDL-dy9LnIpYB82-ekKPPGVtCPJ-veKYU0aV7Ogo4LJ7mb5XatM5LTryapGRzL_KC-m9vMkV5DGVdPjn4wmgMUcBAjw5lpWCEtMk6_wumvNusmq7RAZhZNuDGYU5F-upFYhf5qek3ATf6QuuxsQSFVZJJ5THwzE8dZgDkadAMT9dqGnA33I11w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وضعیت اسکله بنود شهرستان عسلویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99186" target="_blank">📅 14:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99185">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
گزارش ها مبنی بر برخورد موشک و پهباد به سپاه ثارالله کرمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99185" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99184">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
فوری؛ از اکثر شهرهای ایران به سمت پایگاه های آمریکایی موشک شلیک شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99184" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99183">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=mYveYTveksq4u_gE3QhnUBwzBMDxfplq_OJeugPv0Dhh_Ohohz5F1wAdsO9D-ZSYUXfGm1h1AlSZPEFUUvtaAV643cW7GSTmCHX5zv-cieHO4CA0LoSKlqEDCBv2_ux0fz1absW8WZqZWyUcUY8tlO05o5QVhvEg_H4odghyttLIcM3PMpuHLZPAA4FzsGyGSt6F8T32LHKPPMzynQ-j9X5HpMk--2BOEIMa300W5FJRXw27JdMXHNLzAZsgivI9r8lKABZweuEYdsFXbUjLjt1hYXS2TktLi5I1CgMo_vYuhASJluuZ8TSz-co6zxRZyiNq20CPwD-eOrzXHCiZyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=mYveYTveksq4u_gE3QhnUBwzBMDxfplq_OJeugPv0Dhh_Ohohz5F1wAdsO9D-ZSYUXfGm1h1AlSZPEFUUvtaAV643cW7GSTmCHX5zv-cieHO4CA0LoSKlqEDCBv2_ux0fz1absW8WZqZWyUcUY8tlO05o5QVhvEg_H4odghyttLIcM3PMpuHLZPAA4FzsGyGSt6F8T32LHKPPMzynQ-j9X5HpMk--2BOEIMa300W5FJRXw27JdMXHNLzAZsgivI9r8lKABZweuEYdsFXbUjLjt1hYXS2TktLi5I1CgMo_vYuhASJluuZ8TSz-co6zxRZyiNq20CPwD-eOrzXHCiZyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
‼️
نمایی از سرمربی پرحاشیه مصری در هنگام اعلام مردود شدن گل تیمش مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99183" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99182">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeXEPGuSWm1htsKRnV0d4txYhJAMavF_YkLYz8eY4W4CQZ7vHYAv_LZV9BRfJwfCqaRS-FPjwfFr7sxZfdSzg6OiSm2X9yUTDPK4ERRf8ZTSYocBYC8048xi5zjjPhVtHo6D3bLxJa753j7XCC7VAteGa_UVEBWVHgkIFaqncKX7h6J89T19_UXsXKMQQyDY0zyCtRsNgRJVddWXyQMj3zt0RrQnVPVMhs46p1eXVaR7I8RATXR9J2aIwN2xpBtmC1x_qkTDoE1p_tlGCg7RT-GKjDShTY1lE57eU4JUQrK0M45gWLXdmz8L8amC4xo69dzef5z3XTOmLk2WoQpfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لحظه امضای قرارداد ژابی‌آلونسو با چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99182" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99181">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ یک مجموعه صنعتی در کشور اردن مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99181" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99180">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
از منابع خبری عراق: چند قایق و ناو جنگی آمریکا مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99180" target="_blank">📅 14:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99179">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ گزارشات از شلیک موشک‌های کروز به سمت بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99179" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99178">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99178" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99177">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=DF0F9k0AicJU0FmfYhuduU3LiHc1x1bjiyLVx5fqESugkdiOWfJacv8lTLMI94X7tDd_5Wqde8LD1fb5jEfwvP75xJxZ5FjlYiKlQnMGHRHDanWWbM-ObpP2tqsTt_HDUEmaGjW7YfqTmU4vAnGuhqjUWHYK2evr0sno94qz1PbgS0s4cIPVFp9phYMUkcPv1uNLsnc9ZXy45nBQ4Sks3urRqP_PtLVXGkOgcIic8t7v5TB7aBXASmJ6GosdzobkwAO6UxhpovHGnqLmSJkGC_brJtN0GmiFyxTPXjlyKaU-dZwkedFf7hRpf4qU7NAKlMInhP0N1JDoO47Mwd8sWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=DF0F9k0AicJU0FmfYhuduU3LiHc1x1bjiyLVx5fqESugkdiOWfJacv8lTLMI94X7tDd_5Wqde8LD1fb5jEfwvP75xJxZ5FjlYiKlQnMGHRHDanWWbM-ObpP2tqsTt_HDUEmaGjW7YfqTmU4vAnGuhqjUWHYK2evr0sno94qz1PbgS0s4cIPVFp9phYMUkcPv1uNLsnc9ZXy45nBQ4Sks3urRqP_PtLVXGkOgcIic8t7v5TB7aBXASmJ6GosdzobkwAO6UxhpovHGnqLmSJkGC_brJtN0GmiFyxTPXjlyKaU-dZwkedFf7hRpf4qU7NAKlMInhP0N1JDoO47Mwd8sWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری
؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99177" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99176">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
⭕️
❌
🇮🇷
گزارش‌هایی از شلیک موشک سپاه از نواحی مرکزی ایران به سمت کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99176" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99175">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
اخبار غیررسمی از شنیده شدن صدای انفجار در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99175" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99174">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJJt_RKJoStXQm_awcOhXBzdGnXJ2_T9poNi0e0S3hyzqighrwYpZAsNWHROQ1oLXPgefx-hJ51CXxIdbZTg2U15siVfQe9ukbI52hpCCAAIeOnEEpcXUFpBsJAe1dmkR2M3a67A_i_X3DkiQAvqcXQh4D9gxHzz-LRoqynqfPpgQRKTGfO62BylqV02xtr_St3DBBuyiqRFnJx2up_pOSka-W_rPuNGPED0Dx0vyZc0we3IaYOuEb18CeSTHeb_R7j5kErm4Xt4DbaCM1KgF0KgCE5DDrXCEv0e3uscVS8X9W5gg5SuL4P0jL0TIBcsprhyfUKtGeGgPZ_-dxPT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فلوریان پلتنبرگ:
نیوکاسل با فرایبورگ به توافق کامل رسید تا یوهان مانزامبی را با 60 میلیون یورو جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99174" target="_blank">📅 13:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99173">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99173" target="_blank">📅 13:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99172">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0EyenYZhiSDiXUBpdDSl-0Cn6WkrfFuOhtOvYd_2UuNK0wy6AwqvH9FfnrDi0HwGkzcAJ-OvDc5pRzvVQs67Cf1SOTuoWlrPC5no9FdUzkr9nMo0wRoB4PqqT3_yTovu3KuHVozjLipyv6PkdRiFJRnVbyRki7rlyLoSBFXQ3Vyig2xBSzuOvRHFdunc_lwbnnkJ46-jgCUUOOPne51Sv1YLZxohEcxkbtDqRqQuatILwm4x1t9IdsRYmBGue9O0BgupGxMxyJtrtCZ7FkBLllcBZfnfGHsp0KfgS6_KeqnBVyS3VcGMFxjqMXD8UvzarRf0ePPMeza1WrdiphbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بهترین ترکیب فعلی جام‌جهانی فوتبال تا پایان مرحله ⅛نهایی با حضور علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99172" target="_blank">📅 13:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99171">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99171" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99170">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=PXc0-nPltYDvG_Zxd-oXppAsPD73yZNtS3Fvk6C8PP1uP-_qr8ww0Lu9vCGyX6uJanzxEHFfodiAmGXKSp3ykhYkkkRE3YGF8d43VaUTtZE2S9RrCGXPCBUGuabukSWcBWxJf8f-r3aulvXD3FQlwZK070EYRMu5W-VSoxUgkp3xuvmYPx9udc-YNsO44gk-eBxCELoY7hiFM4H_q58EDl5wHXINN6w4ki_p6UJBssiIOs94YFbXHy8a3AVhbsO3FlUMTafraLa90gYPnzyFTTkDi0IQOcM0Ntb0OdFz1KKSDXngR9vZAjz8i2UFxSZO9m-KGZomeOqMauR7eIW2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=PXc0-nPltYDvG_Zxd-oXppAsPD73yZNtS3Fvk6C8PP1uP-_qr8ww0Lu9vCGyX6uJanzxEHFfodiAmGXKSp3ykhYkkkRE3YGF8d43VaUTtZE2S9RrCGXPCBUGuabukSWcBWxJf8f-r3aulvXD3FQlwZK070EYRMu5W-VSoxUgkp3xuvmYPx9udc-YNsO44gk-eBxCELoY7hiFM4H_q58EDl5wHXINN6w4ki_p6UJBssiIOs94YFbXHy8a3AVhbsO3FlUMTafraLa90gYPnzyFTTkDi0IQOcM0Ntb0OdFz1KKSDXngR9vZAjz8i2UFxSZO9m-KGZomeOqMauR7eIW2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👀
هواداران اسپانیا در آستانه بازی فرداشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99170" target="_blank">📅 13:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99169">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d3a36342.mp4?token=D96Shl3xfSErAccieQIQ5BvnMZ0Jd-lKnI67WikaKz6rF1GxZyxkIYQwVcx6fP8NNKVZfJGopXYpRSgZpP7eI0Zpn7DX-gCgHGmDN6ltPYwASNiM25JZMe3dTPQ5N7hEYJeGOBk8ZDPlQBkiF2CEh_6RijtyU6_G0c84iQFeRpmQEDzSlc3jsQKqSHngoH84Ckuz8J-z-EGlSyVRsQfH8FlLd3rhsGE_s5b4buAsVJOuZclyaAEm4WE5qwJpWR-zRlJ6iP7qXNNxF269yoHW-1YjwZKNnrFFsis7OTbD3b5eSXXG5ZfUHP7qjBQRIT3tkcdYffKvZuuMo5UblwFgmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d3a36342.mp4?token=D96Shl3xfSErAccieQIQ5BvnMZ0Jd-lKnI67WikaKz6rF1GxZyxkIYQwVcx6fP8NNKVZfJGopXYpRSgZpP7eI0Zpn7DX-gCgHGmDN6ltPYwASNiM25JZMe3dTPQ5N7hEYJeGOBk8ZDPlQBkiF2CEh_6RijtyU6_G0c84iQFeRpmQEDzSlc3jsQKqSHngoH84Ckuz8J-z-EGlSyVRsQfH8FlLd3rhsGE_s5b4buAsVJOuZclyaAEm4WE5qwJpWR-zRlJ6iP7qXNNxF269yoHW-1YjwZKNnrFFsis7OTbD3b5eSXXG5ZfUHP7qjBQRIT3tkcdYffKvZuuMo5UblwFgmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لحظه‌ورود ژابی‌آلونسو به لندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99169" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99168">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx68o2Z5JjwdWfuloYzSKVWTgPwdnsEuI4N8SzlWWjOAeXLxmY_CmzFK5hQuVTw9NctyXzvIL1R3a5_LFF1dGMasgppaJ7TpX29aYNZ2UF2xOksKCIS_q5qwKOBaKqiCZjddcX6KRHGtpyu4YOVz7j40-LFSDZJut0rQ-pRUDyKrItYi-LOkikzpTp7JY2xy00qK87yuAQgKhmHecpJpAhIk9QEIxNo_o3SoBJlNUoh8d4EBFRKCgyQUYPspE9TZYxokKUCWsDd6Kpb2HjJbMe0dFFJgehvP7UZfBbDkzN7xhe_EQ1vtgNcwK563u_9iY7qF2ZTqBwtg3c31Kmf-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
🏆
کولینا رئیس کمیته داوران فیفا خطاب به اعضای تیم‌ملی مصر: پذیرش شکست از اصول اخلاق در ورزش است و هیچکس نباید داوران را مقصر باخت خود نشان دهد.‌ تیم داوری بازی آرژانتین و مصر کاملا عالی قضاوت کردند و از آنها سپاسگزاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99168" target="_blank">📅 13:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99167">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
آدیمی‌با بارسلونا برای یک قرارداد پنج‌ساله به توافق رسید. مذاکرات میان دو باشگاه درحال انجام است و بزودی اعلامیه رسمی صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99167" target="_blank">📅 13:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99166">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwnlzhrUcfPD3KVeXNUtoeCCcngHJsymp01HqHFkUqRPKE5MwRc9hNbJmaw5huoVqsGjBYePjQpB1J19LxpqSgbLupglSurnHUeAcLEqZeJyLwVypeJEZGMWJDrynB7snm0Dlotj08frP28mK6eUjBdFMxyQyu6_9Lh60GQpeum5gd0Fq2VG8GpDJTumOgC99_m9pav9RZJGBOEJSsvw4xHkQWirdgWU8zpWlGKqcQzsqX2JoqfJUZV4130GIvInoD_tZZ1NjDN0kxI4CPj78sGvC2vW1ph20FElnSqgeu8vMVVIZ7dNEYdCTTy-exLpxkeAFrYpqhRE365dFQHEhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
آدیمی‌با بارسلونا برای یک قرارداد پنج‌ساله به توافق رسید. مذاکرات میان دو باشگاه درحال انجام است و بزودی اعلامیه رسمی صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99166" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99165">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISGo3LCDt_Ao-juWBPrpYePbZ5BE4tv6swjZFl5_IozXslL1GIsKOI9BhwDpoVPQy_P-3c2iDbFI8qRhigGams73pKt7L6ndZicEUInqVQtgQf41b3-OmmQsNBCryL2FjPEPwMR9m3abNufA4QVnBzBXbMJrX1K7vhiOtU6qmukmdwxHcwEeKBamuEvc2rh9M4BzQaV2Ez9MyNORnFi2xDpgoMIzwmvFxlDMnXhN4Ho7DeRpP7MKV3m65aM1aqljViJfjWooLvbIZqof-VWgDoIbgpImZkjO3Y_KRv6fDPGwokdSMaBnaBRIRSDE8fxo2_vLT4wybvANsn4aFIveVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
هشت‌تیم برتر جام‌جهانی از دوره 1986
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99165" target="_blank">📅 13:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99164">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووری
؛ اخبار غیررسمی از شنیده شدن صدای انفجار در بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99164" target="_blank">📅 12:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇵🇹
این ویدیو یه کم حجمش زیاده ولی ارزش دیدن داره؛ تو این ویدیو به وضوح یه تفاوت جالبی رو ما میبینیم؛ کنار مسی، هم‌تیمی‌هایی که همیشه پشت کاپیتانشون هستن و تحت هر شرایطی واسش سنگ تموم میذارن در سمت دیگه، رونالدو که حداقل در این تصاویر، تنهاتر به نظر میرسه و آدم احساس میکنه فاصله زیادی بین او و هم‌تیمی‌هاش وجود داره. دلیلش رو نمیدونم چیه از شرایط تیم گرفته تا تفاوت شخصیت‌ دو بازیکن، اما یه چیز قابل انکار نیست: کریس در پرتغال اغلب تنها دیده میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99163" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b5ea886a.mp4?token=ahj9bT6cbxdU5l6GUfxK6D3nu_0VFRCN2LV1MiNgnnGzKCuaNz-wRIEwUIn7KJS0fL7Vsqrpgagp72FAJsu3l0PdECKIjiMqYP8X4lXhPAiyZiHcXHVtRNebv8qw8Ac61GU_mubhVRhYuLGmqBes8igigVgsqtzQrg3JPd-aVZG3IqjPS3dL1L-X5aXrh_ulLWS9r1DxBNycrw4BQJ8o0dANWJ8wDBKB1BlQLZFTf6T414chNXAYDw_wPoWVm6DDHGDraapFptVaJayS2JS3I06pRlCRZxro2wj1neUoI_BphY9N_Ak3pOgKcD_XJX5nsl0Ehlfm3kUez5Y_rRaevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b5ea886a.mp4?token=ahj9bT6cbxdU5l6GUfxK6D3nu_0VFRCN2LV1MiNgnnGzKCuaNz-wRIEwUIn7KJS0fL7Vsqrpgagp72FAJsu3l0PdECKIjiMqYP8X4lXhPAiyZiHcXHVtRNebv8qw8Ac61GU_mubhVRhYuLGmqBes8igigVgsqtzQrg3JPd-aVZG3IqjPS3dL1L-X5aXrh_ulLWS9r1DxBNycrw4BQJ8o0dANWJ8wDBKB1BlQLZFTf6T414chNXAYDw_wPoWVm6DDHGDraapFptVaJayS2JS3I06pRlCRZxro2wj1neUoI_BphY9N_Ak3pOgKcD_XJX5nsl0Ehlfm3kUez5Y_rRaevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وسط کنفرانس مطبوعاتی براهیم دیاز دو تا از خبرنگارا دعوا کردن و کنفرانس متوقف شد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99162" target="_blank">📅 12:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a986561ad0.mp4?token=hmSZTgYHXhkqOU_FOxeOqZ08Zko_yQ7Ns6WIjYc0a94XxPIOgs2gETaaYecCrkrjJIqIu-hc5jvJcGDVZKEpVsV-a6yUJYR5AZq2mKWyvLrA-WsdCggQ7buoDpvab1VY1Hwqo_1tY6dnQfkj8X1SkXNknPNVHwsiG-q0unhroDK32eijyNyqGdvAP-55l5OtKmzymQ7PrPjIMNXiQoH8O0FFiUlAPRD7ocg4X5ANBp8kaAkUhiKZ1msmV_PUXTIzcC19rQ7fg2KxsH7C5KFP5hhwwESVW6cu9bz5t0Y2eqi7qdlIRLJZ9vo4prNyNCGjNHzAhBsf-YyVCDvVnZJI9GZsdDgHLoiKUzZlEffMOhfHDI-x-l_R5ePIcJXkfvssTZAHGrqYfekxOKP-xgYNNW7NDff0o_wDETb6ZTjONVvLw37RxP9dyFe0ruSTknvwrWGh--O2NMpbXWf5rPUsGYAcOAiIQMqLYpXbpZuVmL5UDVjFVIUb3NDtNNsUf9Y9apNACesgfIzGhudwmgwWUWsTBgB8Az7Z2zhwgFSpwQEZLB9GkzE6rScyWGWejcJGoirpYR6F2uaets9l2svRCeGC9LJfQf4zpqxgYMiUK6jSh_wKl8n8ebrmKCf6lLFBqsRgeC0z6t-I1Us_nH6ANrJkrIdy0QKUBA5L4SeuV2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a986561ad0.mp4?token=hmSZTgYHXhkqOU_FOxeOqZ08Zko_yQ7Ns6WIjYc0a94XxPIOgs2gETaaYecCrkrjJIqIu-hc5jvJcGDVZKEpVsV-a6yUJYR5AZq2mKWyvLrA-WsdCggQ7buoDpvab1VY1Hwqo_1tY6dnQfkj8X1SkXNknPNVHwsiG-q0unhroDK32eijyNyqGdvAP-55l5OtKmzymQ7PrPjIMNXiQoH8O0FFiUlAPRD7ocg4X5ANBp8kaAkUhiKZ1msmV_PUXTIzcC19rQ7fg2KxsH7C5KFP5hhwwESVW6cu9bz5t0Y2eqi7qdlIRLJZ9vo4prNyNCGjNHzAhBsf-YyVCDvVnZJI9GZsdDgHLoiKUzZlEffMOhfHDI-x-l_R5ePIcJXkfvssTZAHGrqYfekxOKP-xgYNNW7NDff0o_wDETb6ZTjONVvLw37RxP9dyFe0ruSTknvwrWGh--O2NMpbXWf5rPUsGYAcOAiIQMqLYpXbpZuVmL5UDVjFVIUb3NDtNNsUf9Y9apNACesgfIzGhudwmgwWUWsTBgB8Az7Z2zhwgFSpwQEZLB9GkzE6rScyWGWejcJGoirpYR6F2uaets9l2svRCeGC9LJfQf4zpqxgYMiUK6jSh_wKl8n8ebrmKCf6lLFBqsRgeC0z6t-I1Us_nH6ANrJkrIdy0QKUBA5L4SeuV2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
Maradona.
🇦🇷
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99161" target="_blank">📅 12:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99160">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=LGutAgSRbOmbgeJ43vs8ynW83W6XVD5ewkIlDcy-YIhVjxxzPkgRN5MhWcxuMTaMENr_5XyzbtXT7WTXhsR-ZyBm83lOMtzexUKNaj8Vm5PNoYxhI8p-3dMvpmRcCFVVh7GJ44ykkTO5gXUCNRMX0AD0vmvEB103_E6UquF1pydanCJffV6jSocY4MomFgbAXq_cMkgQ9MZ7VcQydqALL-Gh5nJIdEoxvcwT4BF1Tw3WkMJSpccOC_r5NFACAQk-G94YF8gVqiODuEQ23I7UQTZsLI11hnMaQpsIzBdeZMcKS2xOQ-cByYqE7Tn0TTwJjlWYyz1iiuriJhgzA-TCbza8xA4t9V8NO5wtrm0Wn_7wt13Dq3M80SwClnU3wQYxBaVb8r2AO7YknUhiGsOnbwQm78kkSeKUWBa1vTwvYHa4QxvA1GpBwoZsX4BvIH_q0qOsNMKHa5UmH05UVjIgD5271KbFaVg07itvnnCG0zvcCIeRtLXCIquU0e4ZSjKhckeaDGqpllr0lBmYcY_Un9zOdbgxRS33KUMHFk3UmKPcofWBWrBGFNqTQnN4PvOFNUyXqQMVdUaefzrT_7ucO7bHjcqS3_KiIaV3apdFjCpviMVdtWYR4rFLmIx8PI1L0X9KxkgkGbyG3yBdDFOXAM7uUYeXgbPJFgsW4TH6IOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=LGutAgSRbOmbgeJ43vs8ynW83W6XVD5ewkIlDcy-YIhVjxxzPkgRN5MhWcxuMTaMENr_5XyzbtXT7WTXhsR-ZyBm83lOMtzexUKNaj8Vm5PNoYxhI8p-3dMvpmRcCFVVh7GJ44ykkTO5gXUCNRMX0AD0vmvEB103_E6UquF1pydanCJffV6jSocY4MomFgbAXq_cMkgQ9MZ7VcQydqALL-Gh5nJIdEoxvcwT4BF1Tw3WkMJSpccOC_r5NFACAQk-G94YF8gVqiODuEQ23I7UQTZsLI11hnMaQpsIzBdeZMcKS2xOQ-cByYqE7Tn0TTwJjlWYyz1iiuriJhgzA-TCbza8xA4t9V8NO5wtrm0Wn_7wt13Dq3M80SwClnU3wQYxBaVb8r2AO7YknUhiGsOnbwQm78kkSeKUWBa1vTwvYHa4QxvA1GpBwoZsX4BvIH_q0qOsNMKHa5UmH05UVjIgD5271KbFaVg07itvnnCG0zvcCIeRtLXCIquU0e4ZSjKhckeaDGqpllr0lBmYcY_Un9zOdbgxRS33KUMHFk3UmKPcofWBWrBGFNqTQnN4PvOFNUyXqQMVdUaefzrT_7ucO7bHjcqS3_KiIaV3apdFjCpviMVdtWYR4rFLmIx8PI1L0X9KxkgkGbyG3yBdDFOXAM7uUYeXgbPJFgsW4TH6IOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
احتمالا بهترین تیم‌ملی تاریخ ایران :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99160" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=eCS9eFiULfhqhVuUph8vVukfVnM24szirTRtNKmKP552fwnAYGQMinjPq_qKyfgsK48l94Q40CK5srcK0ReqA_GFirvDEsvAK3PkbkrdJsnFEFOdQJUvLLBoBkD1p0kPEtjXMWqIL8oHvBnMXKg0c_TIfl8JprjkPhDcVJCfk_5mN0a3RvZASTZveDcWwxXC7Ji2L3OD8_ZggkEknQYJnymDcdQ-NjUR7oDoBUIIUD3fiV36SKH15BvvKv1Nh1FzKQEDmNIHC5nuVOUF3-ok8zVnMCwFrFN3jQslcTEm4a4OJnyR76gJGpPSLI6-Upit-NwtnO9udWbPaKczqN-sag8sPethse-7inQQvzpgAXTJg-5j50C-pMDVZjKeIpwMV502lhML3W_KqSRjR8xGRGdvkJAIEDcybgErT26Hv3DhtxQdXrCcH7d7WjWMSo-OzBtb17WAINBR_a0wAYK3qOJfLm-cikgJW7H9XFNoMwuHA0d8BlJqr9sSXjJ-If5BMau4htWrltZDHV0sysuy-icGpMkLwtdSB0m2gxlWOl-r_e3VtctHRM9XjkjllqX2lu2wjWuLtPze5-STNnNu5xsuJm5yX8Nd85EOV00eZwEbALFtv0SxhJ9zEBUxRWF4CazMZFlqtTHP2MhebilEe524hyQDADMf4DcJea4ogjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=eCS9eFiULfhqhVuUph8vVukfVnM24szirTRtNKmKP552fwnAYGQMinjPq_qKyfgsK48l94Q40CK5srcK0ReqA_GFirvDEsvAK3PkbkrdJsnFEFOdQJUvLLBoBkD1p0kPEtjXMWqIL8oHvBnMXKg0c_TIfl8JprjkPhDcVJCfk_5mN0a3RvZASTZveDcWwxXC7Ji2L3OD8_ZggkEknQYJnymDcdQ-NjUR7oDoBUIIUD3fiV36SKH15BvvKv1Nh1FzKQEDmNIHC5nuVOUF3-ok8zVnMCwFrFN3jQslcTEm4a4OJnyR76gJGpPSLI6-Upit-NwtnO9udWbPaKczqN-sag8sPethse-7inQQvzpgAXTJg-5j50C-pMDVZjKeIpwMV502lhML3W_KqSRjR8xGRGdvkJAIEDcybgErT26Hv3DhtxQdXrCcH7d7WjWMSo-OzBtb17WAINBR_a0wAYK3qOJfLm-cikgJW7H9XFNoMwuHA0d8BlJqr9sSXjJ-If5BMau4htWrltZDHV0sysuy-icGpMkLwtdSB0m2gxlWOl-r_e3VtctHRM9XjkjllqX2lu2wjWuLtPze5-STNnNu5xsuJm5yX8Nd85EOV00eZwEbALFtv0SxhJ9zEBUxRWF4CazMZFlqtTHP2MhebilEe524hyQDADMf4DcJea4ogjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
فینال جام‌جهانی ۱۹۹۴ میان برزیل و ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99159" target="_blank">📅 12:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99158" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99157">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxAZBrbb34ZsCCVDisH0i6GMVRzmO8cJOvUgDZUojCgoxd-C68LSSvAI52Qvzm_OgUZoB_WraQkL_lQ6QZS7CoPWFxHvWXQ-ariebPOzLwDtub3lEjH9v8cgC6ZnvFJRWHSfhutswHXCLb2Vx5rcUhBuTPk4R_Z778YbGJ8qIvmQ1NxM2IcARiNLX-muvlI0a_dB2XqGw87wg8Det1Nt-RQI-w7K-_vnI1OUlJQMBq4SJPqlVWxZu-PsMyhOlL1JeSpxM7fcv6HTf246EnlMkh2PHAvzkDdVDTrKDDaCQRjqD_1M-3XBkFmGptwkUOfyVaJ_RqlA8BP8ezPycmtbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
❌
#فوووووری
؛ اسماعیل سایباری ستاره مراکش بدلیل مصدومیت امشب جلو فرانسه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99157" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99156">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99156" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99154">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=dNGSnKicTHSmKITWvZhWZDqBTELnF76Pb_-KH-9-dj4sw3tF33Z1k9RjE_5LI0t7T9DqYnZlEY9FkIQJdk0eYH47VJh0sGN4K60Br9OtKo-9_kxHUv_vSDy0Ksc-Nv8Zf_Qz47w3qCIi7iFUA521YsxHIQV-A0gjA7metgwar3Pd-cCbpqa-jnnfphGlXRRlb1S4rwOnsa6BFLoIbmPaYTGtPn78oLo57PLeQLNZaw0vgZ46BZG6HyK5MtaUgTAy6EoabQaumxeg-0gQhRCgMHp4P5WecZgvknbsRCZ7wM7ARRsThM06ZZY6ld-RRnJ7yjQzxJapGRRWZSYRbDQyqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=dNGSnKicTHSmKITWvZhWZDqBTELnF76Pb_-KH-9-dj4sw3tF33Z1k9RjE_5LI0t7T9DqYnZlEY9FkIQJdk0eYH47VJh0sGN4K60Br9OtKo-9_kxHUv_vSDy0Ksc-Nv8Zf_Qz47w3qCIi7iFUA521YsxHIQV-A0gjA7metgwar3Pd-cCbpqa-jnnfphGlXRRlb1S4rwOnsa6BFLoIbmPaYTGtPn78oLo57PLeQLNZaw0vgZ46BZG6HyK5MtaUgTAy6EoabQaumxeg-0gQhRCgMHp4P5WecZgvknbsRCZ7wM7ARRsThM06ZZY6ld-RRnJ7yjQzxJapGRRWZSYRbDQyqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇦🇷
🇪🇬
حرکت زشت و تحریک‌آمیز بازیکن آرژانتین در مقابل چشمان محمد صلاح!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99154" target="_blank">📅 11:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99153">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=p-f2DCHU4oNp4mjdMAQJshOG1xiTsuvVqR1seoXSE3rotf7UmADETeizSkatNIlt4RzFEYMOXpLIyKjgf3bIrojnwEo73s_HfP2TtT-KHL6KW9qCa75kDwvi5qWJl7mWmoLpqOG7kcTemA6hVk5BCnUbvIyJb5oY176OutTiRCfLLYb56x4s7iNdh0lXbuDW9Qvauos4rd5_VsdAsoKQS8GNqHBcbbuy0zCqvLoHeNTEvsYHlG-vaBnEZ4OBJ9UfNZjOI5tP9bIGe1orTQEv2t-Ul2npJPW8p5BLOf7kRnC_wPgeWQWYqKJvJXuAPpGP66Kod_Xi0O0XHTNieV3X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=p-f2DCHU4oNp4mjdMAQJshOG1xiTsuvVqR1seoXSE3rotf7UmADETeizSkatNIlt4RzFEYMOXpLIyKjgf3bIrojnwEo73s_HfP2TtT-KHL6KW9qCa75kDwvi5qWJl7mWmoLpqOG7kcTemA6hVk5BCnUbvIyJb5oY176OutTiRCfLLYb56x4s7iNdh0lXbuDW9Qvauos4rd5_VsdAsoKQS8GNqHBcbbuy0zCqvLoHeNTEvsYHlG-vaBnEZ4OBJ9UfNZjOI5tP9bIGe1orTQEv2t-Ul2npJPW8p5BLOf7kRnC_wPgeWQWYqKJvJXuAPpGP66Kod_Xi0O0XHTNieV3X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو فنا در حال امضای قرارداد 10 ساله با تیم ملی فرانسه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99153" target="_blank">📅 11:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99152">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrTMp0AdoCPlUtjWH03MDDoNSsjwNHoMQ-JQwJB3ALFzSi6ZQpzG66CaxaIfIqDBQHtvT9ygTrm0VRjZ4EPStYCdOvZRBhMyfk2bmOJI4ypwt5D5v_GpJn6ph8YPSe46AXcKkL2uiWHEXts7mLXqXpHAw0TpIWwrcxpQieXR_QwDku1cSt0hFFeWy2le_jgjjSvyFRL1k8wL_0qhQgVfbK2OlGVk2ltfwY27WXiQvLxG1RayfivgaQEB5bE9HHhYjKRNH7UxSAEmVVGB9PDL5O5DjpX8-LsRqFZ9ieOqB3znJsLqUeSHjJ3UO4MlAkS6EczlexYEPNUZrG8Lc-r3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
#فووووری
؛ هانس یواکیم واتسکه، رئیس باشگاه بوروسیا دورتموند:
"ارلینگ هالند علاقه زیادی به رئال مادرید دارد و این را پنهان نمی‌کند. به نظر من، او ظرف دو یا سه سال آینده در آنجا بازی خواهد کرد، نه الان، اما به زودی."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99152" target="_blank">📅 10:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DagpWLchpzeYZKRDQjTX2rqR8i4YAFeY8Rka44R2i0xofEoXKls5J5PXe2WBIrWpKDOVgKG8ewR8yiBu6YuJWeqg1tDlbzxMTsPkl8S1URerRrzztLOkyu3Dkfhe7LvViJqhFFKSMvUdKWmfjVbIhRCLHDxcpT5Ia9Oa_i3KCs9yE1RovzX6RI3rWNCOPVyWTLD_6oyBdmip5t5gx41TDTnNEcFWc8ZqDjg0-3joBsjEynJPj5exEH18jcxQ7IRktgKgxq3PC6dUg03kv_NURmL9BFNEX8lQZAMXlTzyHr1z6qdss0Y7Pg1ru1-_M8OsULdR_qV-g7pFlPNhTsqHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— نیکولا شیرا:
- باشگاه آرسنال و برونو گیمارئش به توافق کامل در مورد شرایط شخصی رسیده‌اند. قرارداد پیشنهادی تا تابستان سال 2031 اعتبار خواهد داشت.
🔥
󐁧󐁢󐁥󐁮󐁧󐁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/99151" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99150">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تنها چند ساعت تا بازی مراکش - فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99150" target="_blank">📅 10:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99149">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔥
مرور ده سوپرگل تاریخ مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99149" target="_blank">📅 10:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99148">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=iRb6zcy5aoz3iq63m5QEgp4Ll1kGWQr1vlbaHIa6AgFVdB-7zLdXBT2koh2OkonQpJ8hyoQaxyaIi1Tdx_jXaSQjgtxMOj2Vn5BV-kgUYBP5-pWYlMRZE4Tkqwc7Il4WFUtqWBwJCYjlSIu9AyES3OD4odK3RW-bQpx8MmAeQ8kg_36OBZTFEkgPrBSDpUuJ5YiS7RLS5w1sYrZIU34XEmS-rfMKbK0_VuhgVPLd7qUdT_zzxJ8SLNSc0Ge6r1PBF0o0fL38ApW3c3hh3k0YjYgmCxsIGR0zs7bFzZc19v1ylef_POFvTyTd0ybLlc2kK3FDl8RU8pzH4h8QI64vHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=iRb6zcy5aoz3iq63m5QEgp4Ll1kGWQr1vlbaHIa6AgFVdB-7zLdXBT2koh2OkonQpJ8hyoQaxyaIi1Tdx_jXaSQjgtxMOj2Vn5BV-kgUYBP5-pWYlMRZE4Tkqwc7Il4WFUtqWBwJCYjlSIu9AyES3OD4odK3RW-bQpx8MmAeQ8kg_36OBZTFEkgPrBSDpUuJ5YiS7RLS5w1sYrZIU34XEmS-rfMKbK0_VuhgVPLd7qUdT_zzxJ8SLNSc0Ge6r1PBF0o0fL38ApW3c3hh3k0YjYgmCxsIGR0zs7bFzZc19v1ylef_POFvTyTd0ybLlc2kK3FDl8RU8pzH4h8QI64vHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
آنچه در بازی آرژانتین - مصر رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99148" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99147">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPyqohfYnsmLN_Ozst4rRVSf55blrN_mdtvr7Eo17QLWKoYY1uHjEK3SmXCTBTXOUB6kdp4skBOzGCAwF8Bsrb-2FLIaXufIXcK_aOC3jxxKWgkvHFiS4rO8swdPmVGNFjQMMpoqgGMG_3gAgTWTpYoDOOLXj9d8lq83e0lajnElF-IDs4NAmah1GDpgLML8_6bCmJND1zoCNiRnr4RMuBikT9SvdaxxxMJlxNegkkC61EWpdM0UmnfJQulZKxhUfZAFX1pCK8BfXBF_Lf3rDeIR3KlvezxKsw2bD1QMQrv8xQzcRR1QWThjY8YNXI5vtbxSWRyG3Opq11ZgzBHNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/99147" target="_blank">📅 09:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99146">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=hak7iYtJrSZgn2Ipv6cx14H1I5sCU5RjQixIbfoGZjFRbPVJERI5TUGVq_D7r4Nel2dofid-iwlYZa_LX8B6VHCa_HPPdV3Hk0OYR_eRHTZa4-SExuattHvGiZQnt7HaBwXRlQFTpwTiZx4egs0W3C-KOtTnKQ8q1PHrcLs7scJgME5sO25gqL1VVsQm7zTDc8_-Hw7d9LkGDEZts2k8c4svrDXgD0QbwvxYZjQMjQTHc70pFMFmvoiORpcZKEN2z9tKbdxUh18wWt9z3aroE6mxxYzfw84gLC6rhDgGrWC2vIGfr187o1bnMcx57-dIr5q4tXJMDKAlsBlUCYkh_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=hak7iYtJrSZgn2Ipv6cx14H1I5sCU5RjQixIbfoGZjFRbPVJERI5TUGVq_D7r4Nel2dofid-iwlYZa_LX8B6VHCa_HPPdV3Hk0OYR_eRHTZa4-SExuattHvGiZQnt7HaBwXRlQFTpwTiZx4egs0W3C-KOtTnKQ8q1PHrcLs7scJgME5sO25gqL1VVsQm7zTDc8_-Hw7d9LkGDEZts2k8c4svrDXgD0QbwvxYZjQMjQTHc70pFMFmvoiORpcZKEN2z9tKbdxUh18wWt9z3aroE6mxxYzfw84gLC6rhDgGrWC2vIGfr187o1bnMcx57-dIr5q4tXJMDKAlsBlUCYkh_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
شادی عجیب و غریب خانواده آرژانتینی بعد گل‌ سوم و برتری مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/99146" target="_blank">📅 09:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99145">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=piIEIjC-ZHFnC_HxxytKeGP-ZgJqyIg_Ss32zjJmJ05gv7M5EgO37d9MNZbC3WkwYneqKjwpayp44ixzY8_A8KMRdeqKRDAoCwCu45RDk8dIrXMJzGldtyvetDXjP_zVtUaJTAq7wIqTh6gzNOuwaRNX2Fo_KDaZWzZQ4UHXhsEmgWTEMwWK_o_bC1PsWQl8C2QP6avxPScPNn2GZnlWVCmCHz7K9I3dyiEr8xnfWli1sbgTjlWj6oMApMjGlxWwDefsnB9GZGpzqOX1ANeFjBhsLDh5sAl9YczsIEOgOzHRKz4QXYtEdFXId9krg-zNWjSeqTS7581UOT3BJtZ8rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=piIEIjC-ZHFnC_HxxytKeGP-ZgJqyIg_Ss32zjJmJ05gv7M5EgO37d9MNZbC3WkwYneqKjwpayp44ixzY8_A8KMRdeqKRDAoCwCu45RDk8dIrXMJzGldtyvetDXjP_zVtUaJTAq7wIqTh6gzNOuwaRNX2Fo_KDaZWzZQ4UHXhsEmgWTEMwWK_o_bC1PsWQl8C2QP6avxPScPNn2GZnlWVCmCHz7K9I3dyiEr8xnfWli1sbgTjlWj6oMApMjGlxWwDefsnB9GZGpzqOX1ANeFjBhsLDh5sAl9YczsIEOgOzHRKz4QXYtEdFXId9krg-zNWjSeqTS7581UOT3BJtZ8rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشتباهات مشکوک داور بازی کلمبیا و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/99145" target="_blank">📅 09:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99144">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
به نقل از آکسیوس:
مقامات آمریکایی خود را برای یک جنگ چند روزه یا چند هفته‌ای با ایران در تنگه هرمز آماده می کنند که بزودی آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/99144" target="_blank">📅 09:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99143">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yq2Rm8ATkWDxdujdXaBA5DXfKAF9w6Z8hesFw9ZHjeh2668Z-sWdRimipY1PruaGYZDdgjKKClyIwWsKfGMzUHeEqkzqnxwKQE7croJCXq6xr3dnpJ0ngsBRYK_2tErkIP0zBDilmskUUhOjvtL1W75ppzImEudOjqLu4ScGXQpDr7U_xIfnRmdrtE_R0_Dr9gf0A3iEK7NH5w2RjD4Bl1_EtYsK1Fi8p1Qn4m5r5riiPXjmlIHYq-d2xDZwCRhG46Qv_zPU2p3LXyOMT4Mky67bKbWTpUVb3FusAukFsNx1LtuuOl0-BQc9Of0NFfTGlAHje-LZkVV9ltIy8ZPI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
در اقدامی عجیب و برگ‌ریزون؛ دولت مصر ورود لیونل مسی و خانواده‌اش رو به خاک این کشور ممنوع اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/Futball180TV/99143" target="_blank">📅 08:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99142">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
بیانیه سپاه:
زیرساخت‌ها و تأسیسات مهم پایگاه‌های عریفجان و علی‌السالم در کویت و پایگاه‌های الجفیر و شیخ عیسی در بحرین را هدف قرار دادیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/99142" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxN3sudeambK-hH2drlu2NzQDWNvgzzb44bluYINh6NLcDdt5ZO9VQzLIuxbBcZSNYBNQmTNEg-F5IUYpouH3Ux6aJLCumMbTTR6OZfe3ZYCz0VJqoduEdtfQHZIZPn00baMhEXa__rfyAK_El5fUSFT9ROgtZbG8YcjySlNzKU9qpfIqeAkMK_LoGwk6XPHkJ-a4Y7PB-ImK6EaEE7tnMQFqYxOrCpa2dVrkjgOqdH8k8rEgvYj4-4VjlLB8ELSs018ikzbcQQ3sszApyCs-aosEyeJVzSMUyEkEu48nUYI6zpNWtQqybkCVO8Mhn_tKTg1_dmqcv8PWgjkOSbrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دوست دختر جدید لاپورتا
: «من بخاطر لبخند لاپورتا عاشق او شدم و نمی‌دانستم که او رئیس باشگاه بارسلونا است.»
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/Futball180TV/99141" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=eBZWBWO1QxVQDcBuuSgn83umznI8OYr6YBKHbIMIYjqBUVc7uRWySWIRCwA5i9kpmbMTaq9mbvQpfd9Axv-a5aMm3W09NxbnqgN-6d1PCDiGpCbXLRD0s6s1N6LSy1nrflHgIQhaPuwYXQHwpVQcK9A16EmCAzlM0C2jtlGNIojqnJOc7MuxW_FqkNT8aVLmBdXpI2MvO6x4Nmg_jyvce3NjcAefC8I91uE2Cwjif-H6tpDN7mIt4RhOJtFPr5yAYcrs61b6hpZYAtw2RuBfcfBTG80pUFZuPCrqDt_ldUPIfw-wfCl47-_LwCBLobLZgMZXYLyL8mfVjqp8gxzxqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=eBZWBWO1QxVQDcBuuSgn83umznI8OYr6YBKHbIMIYjqBUVc7uRWySWIRCwA5i9kpmbMTaq9mbvQpfd9Axv-a5aMm3W09NxbnqgN-6d1PCDiGpCbXLRD0s6s1N6LSy1nrflHgIQhaPuwYXQHwpVQcK9A16EmCAzlM0C2jtlGNIojqnJOc7MuxW_FqkNT8aVLmBdXpI2MvO6x4Nmg_jyvce3NjcAefC8I91uE2Cwjif-H6tpDN7mIt4RhOJtFPr5yAYcrs61b6hpZYAtw2RuBfcfBTG80pUFZuPCrqDt_ldUPIfw-wfCl47-_LwCBLobLZgMZXYLyL8mfVjqp8gxzxqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تعجب مهران مدیری از درآمد علیرضا فغانی وقتی در ایران بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/Futball180TV/99140" target="_blank">📅 02:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUJT_IuwCSbUaVMGP8grYdskkgmE569gbjtFkcacp-apGCxeOm3gQyE0q0JCqsIVTC1XVv8dgC6hQQ2JYDPTqT6ks81OkikuUahd1TBCHy39udmnFxcEDNExXiT2tkNGjkH1RwoCSRRWSQQwl6RuYIw9cQtmjx94x3SghskYYPbAWMs_J4R6kthq9bvSeppKyYvFogNl-5FJedgqTpqJ-XuOR56ZZ1KHwuUeMOfySotKuD1bQT0BywoKorxeeco3TY3IG3UK75F5EJz6PwI3sSbxNroawcMTFCEj97Kp3zrFAy3eyfdTxmONX4lBAvyUMRUZOvz2-Odrbq39MY6VAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/Futball180TV/99139" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkONVFgQlObxH2XrmCDNdkvLLa6gZBxZ3b2DmCai_fHhFlHVwVA5BQ3G14-I8VgG6P05WzNfrVBfskKqcdC-AhrEsG80kjS4Xut3nOJocvmOKVp-K_CQtEcsybs-5PsL2OFPPvMktF-KoRKHiFtlma0DdbgsHjo8o8qfu8TPZpjtPFjkwka9yGOgtlDTEmRsQN2ZGapl1Sjd-rkRq88ARoKa_a1j6Q45LvHbI54EvkjJPkBG2JL__FDRHZsqanl7pZHpZRcCkRGGCljoaGre6YzQrxaUEeB07AaMpAEL65EV_qlgodsMusH_kDRLctc1VUBrXgCac7HvBtkpJI2_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تفکیک 3 هزار گل جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/Futball180TV/99138" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/99137" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H6r9X6pFSsb3AzStQv8vblHISK0eUv3WlRy2CJPgVCKMju0cc34UMnL-e7wIlru9H-_WII4fvlkUkqLcR-MqxPJPIhYJGGDwS0HYurXYyODmMM6YJbSasIBj0UN_x29wZkAFYxhTlmvodwOE0pbJk09NwCaJPoh6UT04DmzyE5x06yf9wVHa-63qsq131szLK67YsuxaPnxOSFE8KMnWKLW6WXiSDnEPgN6j484i6MBkRhGrXDlj_3zHoAo1WFV-F8XVbiRjch1fUnt8iZRE9l2cz0d5mte8r10S95u5BBf8l_bjw36q0HJlAnDMe5IMU459Y5lwnWABSY8R6yypPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/99136" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99135">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
رسانه های برزیلی:
ممکن است نیمار در روزهای آینده از فوتبال خداحافظی کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/Futball180TV/99135" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99134">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdFrz5omLd1urXUKIyBBc0zNiRrG56EGuikiejDPJKU4NBdW42mxrw7tiYvSQ6N5OMw_WzfIvfaE_mP1rdMd-V4bEphiwaZBY0Q5yYYan0Bo0VsaCRFYw9voqHNdbyh0PDnoUXy24e0DJW4R_PiFpEwD9WKr_csjpFpdKo3T_QPbf-s93wafSap6ZwsGNrqBTFyawIyo1s-w6pXrgqocWDMF5iPyEcckMgTKh21316ZLY1uEsRtF9H090OUB1HeT5iHaCQjPZKcBBkWC4GANZ4pZvD2vvc7myM5gNDUWdiRNCAYXg7G-KR7wUrTZmF4nGotpPWFqk9ODW5UU3pxEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو:
بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/99134" target="_blank">📅 01:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99133">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjK5oc0aZ-gZCb_ymbIoVAdcu48HZi1rfYszNyCCZdfbiZ-1z8Tt_hutznkolD4F8aaxA50NDav5UeFS5s5fIB_tHcJKeHEe3-qHnxLh6J2gPy6eZK1k-kdpNjgvII6It3UdGDFFskjd0ni-V0BIrB7XzZYgf84WnfKdWoJ3mkj3PPEUF2waLTFsL97j9k0LqLDDMUfiipgpseDKBjietpt7ImHlx1evXYVerIxmkicmIMkJ30jFts53GhuQnHf6hRTspKyqhu2EhXGmdDq2cLyTrvH4pfOhFejSVA0i9jrTUNwc6wCv_r4eVfHuiigPHvfamb0yTz9E_KsKkvmn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب مورد حملات آمریکا قرار گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/99133" target="_blank">📅 01:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99132">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
حملات امشب آمریکا رسما به پایان رسید و تا ساعاتی دیگر حملات سپاه به مواضع آمریکا آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/Futball180TV/99132" target="_blank">📅 01:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99131">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EenNr-aVVSUOXUs_xdJoX77ej0KRByWIFA6kLD-N4M0wuJBkk14PkF3rKB2hetG7P1kuIwwpgqukA7T0w-F0l8MY-QBFr_vQVtutjyRtm4Fn7DsnHsg9qgRTakPvcx_LBiGYda2OgauImeG4kzLc5slCO4vbtX2pPsXWYjmN7O3VeJyUMZiJp440vLoDfuyhL0Q4jELtonTEhJHGP5L62k4FF0oNvnVcWWPqL7Vgd1wwqmNXUITcJOPiiy-wlOPI58iIvWSy16Z1QrbW5ZNkuQHWYe5lAPZ3DIp4KH1VnkWnNcvNisHUTC4pv4ny3KlwaYtwxFkGR471pzlStHY25A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زیدان:
لیونل مسی بار دیگر ثابت کرد که بازیکن سیاره دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/99131" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99129">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQCkVH-D7w03fbT9A7A0D3Fgcl7pW-F2xkWAU9LdbbVIihTaiAmLi9As68BeGgq25etmJjeaIr6b24gOmlZXHJg9aI0in5xF4CjYUITUYqO9OYcXUSSePeZZI0tDQ8UvBJuNx4R9axHlHSk0zA-8aqDhg_erWDfWUW0vN6Phy03VyAm_2lJMeLbQYLguR4nBQ_bhNZjGGcE6tw7hmC_EAEP_fOSC1mJqT92UU9Im_ZesOliGYAsg9VpBdzBeSa2yRN0jWjv_DGuT1lnPPPw9wsp7C8U_BmCQbVth1DmgeBmbyNyE9UZSjIsSX835iBtHgsb06ITbbdO6lNxrgp7--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/Futball180TV/99129" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99128">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از کنگان استان بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/Futball180TV/99128" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99127">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-LE8KGinNImX0tZgwEMs_BziY_h_6IP_lVQ0sFaI2bu73sEqQ2RHZ8opWJC3t7j0U1BbV9sqFpR3K_kVt8pffsHwRmY-_DXWQjEZKL_5eyGJfx-OYvZZElQHIwITCUC4h3Y_IxsVjpUHfDPnTsgzEEcIekXqsLsXH5ZsGRADMOiw1vTzb9B9FKblT9NRVRMiu5uRYieOOLTaoNFxXoPPsjDcdsfmf8KMDcULSl5hbxEZmIn8eO99BIx6_umbdevDW6NlNN5mnPANBuNvmBU2d_rAFyYSqVOgtYrGxvMQmCyB7O_0LfS-mgXGsLC9Jebl2gDHSeM7tQcwso3EiN3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
محسن رضایی: دشمن متجاوز و هم دستانش به شدت تنبیه خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/Futball180TV/99127" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
