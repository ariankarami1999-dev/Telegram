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
<img src="https://cdn5.telesco.pe/file/q8zVPVUVXShLXCAWqdG99yp4UpuOlDawOqsNDgFgaSMNrxNiceHGMjqkj-icXmX1Hv7kiKWd5pCHrMaSC5omiKEBSAjVXD0R8Q0XOCHUAQob5zY-gxUQJw2EndY2nZDDzUJgpxChmwPn8iuvpgxJTesgwzJuFk5wDGES30dCWYjV6_UHxLZ0H3YBGEEi3rLr-PlDGKCMUeQpGuLaIOHqAFvu3mMhdv1lI6GpjwdTZbxZe2sL85I_5YeWDKv4Ptfet6iVMz0bmT9u0ygJVd8erPsKtcdWs-nRFXVAkawezxUu23YR6aZOLkKhRgQ8Rt397QTPiz65CoX6RWao0GMYYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 463K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 01:11:09</div>
<hr>

<div class="tg-post" id="msg-103931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7dPQ844SrvyH7onyJSFtWWF_sa6wNB9EuXTFcsSV0SZIfN-j26_BXt3eCZw5OU3mWDFMXoYANw2kPh7zmO0NQoZOTcwj9OC2WscRRfcw5yBjiHXJFP8_P8_hgi-oFJo9BGAUMOMTJvS9vrnRwvMGm24gazJYd_qqqXBFvev1kJRGdyoHaiS7m30BJW4swh-Ma7bUq12TlPDAQZsFwOKY5-K-9K6KOYdWIGO0jdJoZ6nvui_dcqMG6RHC-y0ggnUzLjftCK5ADqi5f6C6CjqtkQI1zPhp8T4VBkavj5QxNIKxhW2moS9w5G0N9og8mBv0uYAwMcvB_Y9oAbGWKZb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3d3UWPj7099CJY5XjAwEQdqXYSp6pmcmkhfqYLEAweus0ndXDo9zcCf0XKWydZkBviOUVLAFFTfHxg8yO5-9xzfJXEAUY71sSyLVNzxeAgt75MxyO5m7i0ZgFpdzbTzKxQc8i9qXZHxvOB7LzcboMtvWFojy0QS-MihhmjfxeN1Z9fEQiYMMi9kdzBAnZgk5uNtke8tIUlkSMPwCiTBUIOaiZR-UQxmsdejj4DMyk_sw0dWJ2uwVwNnFy3UU5a7cY3kSRg88VXUJWOkBD72rmVFZMmIGL1uqRJLTPIm49HiTKkJNbOlvQvG-38FtZQfZL-7paeIO3hghNOKcjj0HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاپ قهرمانی در دستان بازیکنان لانس.
❤️
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/103931" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/103930" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=qKqLhhPm6JHx2787XpsodsCZ9fDZwmF2nsLnO3sF8Zb3WkAMRO_mqcVjqwLkIDw18iQCZ4ZYUevOqeHu75WtfO5Qdt7cfnDtS3gBEDQd7Eh--VL_8wXxFupsqRvH7AY_oLsF_oo3zQ0ZrxPi06OXYZhoIMy_BrlSdCl5Eb9nBoSRbDR8j_Y0O-0CvEVVN73x3zBMRP53cCt3AsR5J4FODM6iuoP-O56ieTKsubcKJexsb3UXku5tPU0N-lt_C9PZxHp1WJwFWN3h-4pNfKdiq3F2_3eDcvEIYZJBnO6eNJWxURSUvTTxO-8eFnP41zf6gY80q8wRplLdYP7Np5b7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=qKqLhhPm6JHx2787XpsodsCZ9fDZwmF2nsLnO3sF8Zb3WkAMRO_mqcVjqwLkIDw18iQCZ4ZYUevOqeHu75WtfO5Qdt7cfnDtS3gBEDQd7Eh--VL_8wXxFupsqRvH7AY_oLsF_oo3zQ0ZrxPi06OXYZhoIMy_BrlSdCl5Eb9nBoSRbDR8j_Y0O-0CvEVVN73x3zBMRP53cCt3AsR5J4FODM6iuoP-O56ieTKsubcKJexsb3UXku5tPU0N-lt_C9PZxHp1WJwFWN3h-4pNfKdiq3F2_3eDcvEIYZJBnO6eNJWxURSUvTTxO-8eFnP41zf6gY80q8wRplLdYP7Np5b7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a25
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/103929" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQp52RYctncY2IFw50RsIXk6d8trHcEGukn11XgQ_bDp7gqbPDfiCK7X9ptP-zdA_Pks-K4w8mQsirjpJs3t48Xj1UQ7Bz5ReYSiwxhH63FuvsxMe6xprOkA-I3yXbCWkZ_ZJ_fFkob-WBAIS1mhSz-VVOIqd8Kk8q9Am5yZ3knTVgmC_13368KPV_1QNEhko0M9fMUfX3XvoGAJBxMuhoYVxjtxvPnAllZF28gxYLCOyDvlZdFOLVH9bVhokBWpCd5-4bx3FbG8oDQF2xk83Ev-HOHDtEAJafDfdHuBH3Zx8bd1Qgye77_lb534gJKstNeSayTB47KywTRswiYgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
سوپرکاپ فوتبال فرانسه؛ ۹۰ دقیقه تلاش فوق‌العاده لانس برای قهرمانی؛ تیم وحشی انریکه مقابل حریفش آچمز شد و جام را از دست داد
⚽️
پاریس‌سن‌ژرمن 0 - 1 لانس
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/Futball180TV/103928" target="_blank">📅 00:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0ba339f4.mp4?token=iOF7xAIwMERPIvm05ebjyl1vZw2XrTXG4NSP5IxkHNwY4vmNlOhNtlkT-39IFfqSWg_wFcfPbulGaAyxti5BITHu08IszTfSVoxYdGD-rxVVhYi7pEx6CzY9wDpG2T2Gnif3zdiqXVT-D4ZVV87c45awyP56BBVGSRTty45OkPfQRA7qMwjWUuIe9uCYrRLjtzqW5DvCFUASAc2dDZ8I_y_6Y8Xtei2xuW9098BqOcavzZ8ca2YQhNkDvf3oTqXgvAa1NYiyLx3gF1lUlpLhGCZNlAhwmsDZiuMOl1r3wo9WizvwdRI5CGcgnlalPixsAaDui7TMClWezP6iykrzpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0ba339f4.mp4?token=iOF7xAIwMERPIvm05ebjyl1vZw2XrTXG4NSP5IxkHNwY4vmNlOhNtlkT-39IFfqSWg_wFcfPbulGaAyxti5BITHu08IszTfSVoxYdGD-rxVVhYi7pEx6CzY9wDpG2T2Gnif3zdiqXVT-D4ZVV87c45awyP56BBVGSRTty45OkPfQRA7qMwjWUuIe9uCYrRLjtzqW5DvCFUASAc2dDZ8I_y_6Y8Xtei2xuW9098BqOcavzZ8ca2YQhNkDvf3oTqXgvAa1NYiyLx3gF1lUlpLhGCZNlAhwmsDZiuMOl1r3wo9WizvwdRI5CGcgnlalPixsAaDui7TMClWezP6iykrzpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
خلاصه که گنده‌گوزی آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/103927" target="_blank">📅 23:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fefaf274f.mp4?token=FtS69b5wN51eME47YeAVupcgnwt5MfUemJSOdNmrzihBWbBbhB00nXPsEStgW1mEfISBKC_1pKTCc6LhfbVs9QzOt7W2zgdm_XZbkH6tz64CfkZFNH80Em9v_8FmcIz31KOEUxo2PxV7UoKN3u818M93fHeWaWhEdIFaAx2egaLSrfYE7Dmm2pO8cnUy69gQGAh-zL9PxZ-jjxVEQkEnQ9SVG3RxGa9rfnCd-S1lNT1drclKXjZjfLijlLzkqEu6FTQ7d6QQPQdEpPcaYnukNfVTGrVSScR6BVrjbJWyd62EbgXQ7-90DRo2fvPqtO5W2D6hrf_jfQ3m37hjsF9Eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fefaf274f.mp4?token=FtS69b5wN51eME47YeAVupcgnwt5MfUemJSOdNmrzihBWbBbhB00nXPsEStgW1mEfISBKC_1pKTCc6LhfbVs9QzOt7W2zgdm_XZbkH6tz64CfkZFNH80Em9v_8FmcIz31KOEUxo2PxV7UoKN3u818M93fHeWaWhEdIFaAx2egaLSrfYE7Dmm2pO8cnUy69gQGAh-zL9PxZ-jjxVEQkEnQ9SVG3RxGa9rfnCd-S1lNT1drclKXjZjfLijlLzkqEu6FTQ7d6QQPQdEpPcaYnukNfVTGrVSScR6BVrjbJWyd62EbgXQ7-90DRo2fvPqtO5W2D6hrf_jfQ3m37hjsF9Eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسوت اوزیل طی سه سال شفا گرفت
🔥
🤯
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/103926" target="_blank">📅 23:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8863db9835.mp4?token=K0JKNPDxa67RdetKOAg5MN4dMFMsLBCl4McaIacRCSXMmfEhtwR5geZUrM2Pq-XldSdIlPoi6aeukSJYUJere2iszxwdV4jlDZkIDy4K0rXNua4cNBUjU2nkMmg1cfJbW0CV7tq2EJOivuTAVvIDr3bx287gPGW8iRqESLdBzkJZHwBCwQd1VFj2j5t_jZL9mlvjblNCm2hG1TMQdDbI2gAOPd-DkiDJQrEprexLSUEHk6FUfE74ksernFTcuKwBR76aoI4zKW508is4rVwvuRJq1Yt4BRpxtIRrUlJCECjfvQp0J-iRKu0e_wJVcHGDXmRKzaTlO0FU5xD4FkQ6SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8863db9835.mp4?token=K0JKNPDxa67RdetKOAg5MN4dMFMsLBCl4McaIacRCSXMmfEhtwR5geZUrM2Pq-XldSdIlPoi6aeukSJYUJere2iszxwdV4jlDZkIDy4K0rXNua4cNBUjU2nkMmg1cfJbW0CV7tq2EJOivuTAVvIDr3bx287gPGW8iRqESLdBzkJZHwBCwQd1VFj2j5t_jZL9mlvjblNCm2hG1TMQdDbI2gAOPd-DkiDJQrEprexLSUEHk6FUfE74ksernFTcuKwBR76aoI4zKW508is4rVwvuRJq1Yt4BRpxtIRrUlJCECjfvQp0J-iRKu0e_wJVcHGDXmRKzaTlO0FU5xD4FkQ6SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیو وایرال شده از تفاوت رفتار جلالی پیش و پس از پیوستن به تیم‌فوتبال پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103925" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103924">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLsQI0-QHI61tIYrMgh-LSs8dFP6Ny6S5E3VfCM8kzxCPI_7a77HWQkglvEPflpazS8ndU-tBOr0o96BV6iCHX2-cQvqVbGNxm29K4q6w9DIWa0q8zJYCSmErDmZ_4_PJjo2zFSbAq0EsWVwa49jXtQMtOxj2b9ZLITltRQ_ClCjHZHw05oaWuSYsO48IPk5SQDy30KeiW7KzWzz9q8k7PJsEACrfAj7TE3sfe02Gu6MKiyNM8wLLdXHDlo5YVgVoKePX-PUw7eCYhgiHaZy2tF2kRBclmUuEwz_KKfED9MCkNRKFuj-WA96ZTD2r08FH3SPL2wmf_YJflOYGov4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🗞
🇪🇸
پوستر دیدنی رسانه 433 برای رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103924" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2mi8xrXqN-rXuxDb9i9gLzLA6dG9y3iNHSIEBLoB8ydSKu3f4A53qX9KM1YavPuTtTm6Z-DQq5QwL54oph01d1v6VE-9peVSDhU7dOKfOEdE27tMpeBXVxsGXb4RUVYnOQhRz9lRilbP_JHflF7nF2yNetIa8shF2tj5zMg2n8BkXlVi93z7Mj4zuBRYsdTPxTKB-edKKMNt81nZx_U0nUGWKS9WRZtEwguw08goQM4j9Nzhr6vl0Ngcj6puW2nzbGuGP3Qc6b07zJK_6_-BBUvGEDdWVVzEgE8449rg30O_fstfmblgXfNtpidII2fqUjVcpmoD3hkL5NFLTyYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇪🇸
#فوووووری
از جرارد رومرو: رودری فردا دوشنبه وارد بارسلونا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103923" target="_blank">📅 22:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzwcXPs80da-Suu6VKnp5_yktuh2profXUKKR0jlj9TFW7DL7TVaiI1g5l88xsummpT996o2lk1BbGL_8hcf2OOvMwW_ZDd1te6DI5cNDfngWutIsADn4aIRovFd3oBdv9e_G-45F2s0hlSIRrTg8_inZU0RWgTKFOAN2mUapbxHSz7x0k7Z7xCLiJlZVkv0VmCbrQVpFzM8hr-YH1PPvFYaxIS06pwbg_kvyD9z9A6WW7Oxh9HPZL0zuB10DLJrpKm-rHCTEwOcMX1hzC-hjBgEWlp7pKYN8pW2epi3LJ0Fo1wjWejHAc-o11fipgXl-85RSSMZ1DALJEEOnN5B6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2/3 DONE
✅
👀
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103922" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjE26P_w6tL7__uasSkSdyoTz0EWWm4iSzSQwsj74937a5mAzNDalR2Q12SSeNEz-SGVRbE2ydzi8jVOwSee2nKDKp7OorfxrhgWU42k56nCjqKkeXZlQ8673NJ43dacy2YBV7lwYpcS9KVCWWKzSzBG4fjJGfFSl_EFielVWdtyICGpMtZsGK6BD1J_9Wh888PGEakIZLPJn5mBRiYGYRV13NMLRyrly9S1IvImYNLFP87AnGygAkWTm2_OwvBa147dIBlDFn7H7l4Fno-4oIrNbi1tqdenoDKTGQN4XLPNkyAmxwsKOVPo9eg6FsfAdHCw2MNOjLarSkEeUIBa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
مورینیو درباره بادمجون زیر چشمش: نگران نباشید از شوامنی مشت نخوردم. فقط یه شوت به صورتم خورد که اینجوری شد
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103921" target="_blank">📅 22:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3Dni2VFg5cdyR1OB9saaDieSvAMWuEQBZjVFkXAU9yEwLPEclzWHjzNF27bUbvqJFIj3X5FO7YPOCY8BLQDK9vyTliIrapukncpdKrXVSEGnU2iDwljWm2eQEgzrJdy7du31c7WqWyFbFiMmrA0iKuVwdfIvuKUxHWkpFi5wpqBqiEIJNIuRRYBikhNLMdUAJXQ-96muzd_RPVDkOif_wRRrPdTyLg5hK73zWFuray5SRoRFOsWPywgeY71fV1cCcXRpkVui9HGIiK01C4iJmLy7Xq742BcobgZr2AhfVmQVqm6LRKcXZfQmQN92khtYRYQtXW1PxA_QBn8tVconA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از COPE:
✔️
🔴
💸
منچسترسیتی برای فروش رودری ۶۵ میلیون یورو ثابت + ۱۰ میلیون آپشن دریافت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103920" target="_blank">📅 22:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h15nwjPObASir1NokU4vpQdlcB3M05S-fAmALE_YqXYkDcn96DlKuJUOb3j0QC0mG9_VRSfRVEv6r9T9VibR8I2uh8rpOTQb5JWst0OJRLISxemNA1CcRMnltbZfYl02uiBW-P2zDhJgy_v1n0m4PaPxaF7WhRUv21Ml_mp37sURro0Ntrlj9KVFSDeFc7GLIsEnjpzEZ0vRqU1wZEhK2XEKXdX3b9xkH8RfQZD599AflxgndZkVZOCNMzRPjllP3rKllR_Viq3elpYzWOSKT6MJBSfmJ8BT4T28WpU0vDnINfEoxeOWqAlf-KTjinP0v1gUJyJmZoa_JMhvLGLy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
بهترین خط هافبک جهان در بارسلونا
😐
🔥
🔥
✅
🇪🇸
۶ بازیکن اسپانیایی و یک‌بازیکن هلندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103919" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg6lHtjBCFLFCMFm1wU1Rye9SMJsCUmJarNgDtZIVI-X_H68mDSStmwWRCYanOcuMsh3Dp00jkL1TsMls_KuIVmes8guVvXWqCBEZUAPPljioOvWbPnTkgwtGT85EjjpZ2xhzTiKC320C2dsav5Yl-QDFgYdZux-sKnAc130qmu3h8YziF1z4VgbujwvqZln5i3Fb2ZFoN-sELqf-ZWgYTKAuqde9NG_WlZA9_ODuZ0cT9SWgRlzH_2fNFbo5wOk09VnSv1VPPPygFIzEni96L1yJFPUYPyv2Xnqm0dm6qBTnWtpW8ClEiR5Fu9boHTDVFuSGxzVvLm1e1S-Mby4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوووووری
از رومانو: رودری ستاره سیتیزن‌ها به بارسلونا
HERE WE GO
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103918" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103917">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqjqLlrse_nJ4DiAewu7rWba2n5AZkdXUkjRgI4HD5zpwFMhKimVngc7xWyyB2GWSrPjh-7SO3HNx-q0T2kC992bpW05Z4N4oIquqrnAnq1B99cGhDDlyLY26dfi9igetWulPJYB4em5VQSFOkodWhPVIcrw6fFOGNJtF58ms4YoGCW7SGdW8hRJ9eNlQTND-lE2rIgLuxG0ps8h1yO79HrFFLOTnUg8C_n3LMQzVt6ihMOtRDo4pgMdO2TXREFQTLCQUwwsBqiN5v5_qBH3UMUetqwZzmrJeZpd3s6kdfzZWcYfpQY6DGVxHqDDsgfb84NSXIMbRql-XvqWo687xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرکاپ فرانسه؛ ترکیب پاریس مقابل لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103917" target="_blank">📅 21:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6285ff8281.mp4?token=sYs_yx0KHbDXlIumr7Aa5JTWfZf8PCgAjfV5cBZIEISfJv9yrpfHZ5d8dJZ4zZ46TzOUaXn67bJBqTAre4kX3A8T4lIZH-YXDsGK7gtWk31wLgPFFoIVJ7vov9t2C6F7OCBJSElpiuVqS93jmAWZG7iTuFJ9y3an131M8-lIfOFi8Mv7pfrmSRAcy0BXckLXNhqz2sY-a3TMHzSsR7K0Q3FRN778uf2J2ilPh6rrvDRzvFyitrrfe9-7g7VKGrSb4IN5kfC8vHA_wFKdXdVOlpmaZDfDBzB4ImuzcGZzSuaUxBlxR_xwc7MKchxcnfD9MXTyHcaCWpLAcxcpRSyMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6285ff8281.mp4?token=sYs_yx0KHbDXlIumr7Aa5JTWfZf8PCgAjfV5cBZIEISfJv9yrpfHZ5d8dJZ4zZ46TzOUaXn67bJBqTAre4kX3A8T4lIZH-YXDsGK7gtWk31wLgPFFoIVJ7vov9t2C6F7OCBJSElpiuVqS93jmAWZG7iTuFJ9y3an131M8-lIfOFi8Mv7pfrmSRAcy0BXckLXNhqz2sY-a3TMHzSsR7K0Q3FRN778uf2J2ilPh6rrvDRzvFyitrrfe9-7g7VKGrSb4IN5kfC8vHA_wFKdXdVOlpmaZDfDBzB4ImuzcGZzSuaUxBlxR_xwc7MKchxcnfD9MXTyHcaCWpLAcxcpRSyMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
اگه موقع اجرای انواع پرس سینه، بیشتر سرشانه و پشت بازوت درگیره و سینتو حس نمیکنی و به ناتوانی نمیرسه، زاویه دستت با تنت اشتباهه.
✅
هرچقدر به 90 درجه نزدیک ترباشه ، سرشانت درگیر تره. هرچقدر به صفر درجه نزدیک تر باشه ، پشت بازوت درگیر تره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103916" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT0nYnHPSt3dULYrPeDFP-PnnIWM9HhGkYPxcTlnlwUC8W6B6bGcbzzMO-NPuFoEkTK1QZFQrUmTyTBQsF27KISLQGu4LsMq2Re_rKGbO0jF30-k2zgRbhDUzEGak8FcdlRjyKR3arM-KJ-6MlzEm4PgtszNC5JZUL-FrwSuMQ5HzotgKmtSJac4IcMWPYrSNEa62ITm5rPQHRhNuB5HSumAaGGApJMTwmLXRZv-5BFLPEcdwDkuFxfQOWyO5wE_t6fjGJvm-gfc7tUR8ZaVhCb-05BKMnfAgjmhQAbGjl2cRhWfXQnVRGfcFEXKKGv0HQkNJsB1jsFSwX7OcTHffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇫🇷
اگر اتفاق خاصی رخ نده، پاریس فصل نقل و انتقالات رو با یک تراز مثبت 129 میلیون یورویی به پایان خواهد رساند.
🤯
🤯
🤯
🤯
🤯
🤯
بازیکنان جدید:
✅
فران تورس — 50 میلیون یورو
✅
ماگنِس آکلیوش — 50 میلیون یورو
✅
لوکاس دینیه — 7 میلیون یورو
بازیکنان خروجی:
❌
گونزالو راموس — 75 میلیون یورو
❌
کولو موآنی — 41 میلیون یورو
❌
کانگ لی — 40 میلیون یورو
⏳
بردلی بارکولا — بیش از 100 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/103915" target="_blank">📅 21:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAYQzRHtnmU8cRW4UfKJ5X0ffpOL9n8vYXLS11fnEFpCzC0byORmBLLHHPed1ogtxL8ZIjdwITqllXXR2r1m2gKbY-fY-khPH0iNR1I6nAT4BaEw906duaPNhnfX5WP82GpLkms_yVz2eNNjCD4xIh9sbIJucDHKj4y132rwn48v8zdY3VcbZlzavte5K7ZjjBDYYt6tpqPu0GkoRzyO89iw8trAmVg2Fe-mLCwazONws1Mryt9pbktO9x-nLi70DJhD69SAigk2Zi4hZIPhik--g2xi4zPRXqVlSxAwnBpJQpg6KX3CGoOG60VG41WsAxTQtGp7O-nGQSWxo2vjCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوووووری
از فابریزیو رومانو: ژائو کانسلو به بارسلونا
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103914" target="_blank">📅 20:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f160aff0.mp4?token=AnrKUWFmgwb5sa8inafllvYSt9lDYTqR8KjVVsSEEKkttSw7Rq3tEYiHkh-HcN3AD5p5nPoITiiKTvU9nzgTFROtrc09eL3-MDv9K7Mez1EBUsGpWCgOvtn6QhgdfaS52LsAjtcMQQS6-ivKKrg0UFG87EFbJZUlpJDnnoI5Vr9gJAgMU4a7L1F5oUpg4427py607MuyTjLXVijBLkQSHlyVngDHK4GDtUH_vzvtf1x6iHc1fekglIW2Dbd-NFW0gECZSoIE4alslgkFUi-gERUMqKmhqYRaXi2ZRt_K_W44Phd_-7wNzK_mNgE6ubge8PLE_16DeZ4Wr-92pIXOig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f160aff0.mp4?token=AnrKUWFmgwb5sa8inafllvYSt9lDYTqR8KjVVsSEEKkttSw7Rq3tEYiHkh-HcN3AD5p5nPoITiiKTvU9nzgTFROtrc09eL3-MDv9K7Mez1EBUsGpWCgOvtn6QhgdfaS52LsAjtcMQQS6-ivKKrg0UFG87EFbJZUlpJDnnoI5Vr9gJAgMU4a7L1F5oUpg4427py607MuyTjLXVijBLkQSHlyVngDHK4GDtUH_vzvtf1x6iHc1fekglIW2Dbd-NFW0gECZSoIE4alslgkFUi-gERUMqKmhqYRaXi2ZRt_K_W44Phd_-7wNzK_mNgE6ubge8PLE_16DeZ4Wr-92pIXOig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
دیومانده در تمرینات دیروز رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103913" target="_blank">📅 20:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPSFjZYI7NbNpWiXigfO2y-VRT6iq2Lo6lB1SBqw2IABa-nXK8kvYPj5MdpO-Wg27_-uGSy6IhcVPemErOle2yje9M7tVwy4BqH7Yw3EoPOB2KGZ14bxXG0-r1wcqqpmluJoWF06A02MreQ_E6pxthLdeSaB7MCJ6wHRzKgyVuGcsVOA2KojZBpAG-5ZX_AAWqWFZXNfg4eyDYOlFFmIQE3HA-nl5d5mTGzBVeH_YF7K-g4tzVKUGwzK4igCnJuMg2LO_AvMD7NgHKKrKpG8GODgIle0NP6ydTzQgaZCGK08exck4sEiC-EeWUQbnL4QC0z3S0IHl50C4Ic54raeKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با نتیجه سه بر صفر مقابل شالکه به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103912" target="_blank">📅 20:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
⚽️
بارسلونا در یک بازی دوستانه، تیم بازل سوئیس را با نتیجه 5 بر 2 شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103911" target="_blank">📅 20:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA4OsB4_9a6XCnVCMtcRjcMSiDbvEMFiKG0ZqN9yVhMAn9E6q9d_plnmeVCRkl8NzmgisRgeAGR71xN2WDP-lYOUiwt353ouRHjOpy5D-SGhhoeebqeuJ_5kq9PVRzhzwTjjijZXpi6fC-8KN0CzOfUR1NS9Ei-IrSPd-hnCigb6JMirLwcqnbPEoWA_aGEWwe0XsQJg2-kzhf_0fFck6T12R9IHUuuq1zSeQJMTAPwEOlQaPA7s8ZagZhyNv88zXnhJL3Ls9l50zoa1rfUeF7JinCMAMP8fal-FmoaFT0syHSshYUYjVIMTsbdQtX0Flc6sUrkkpZoJbs045udruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
بارسلونا در یک بازی دوستانه، تیم بازل سوئیس را با نتیجه 5 بر 2 شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103910" target="_blank">📅 19:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP5lpbJ3YfJPMnc_gLTzSysJMyxiflN8CtMmRzMNDtdA9RxhIu-PuunKYHfB2jlMoRqCFjvZWBuwN1Q1UygBnQZTDMHUEi0H0ICCrOxGedsAlRS3DAdvf2tLnlVEru80tUvI-TB7T1Iw4FgjwV2IIfnZt8mhXfBRyc8Toe3GeNFpZuU9WZ34eHrkv-7eTsLUQmQeFi4NYLH6kEguntPvS10fXeGHiOTv_VhqGLwXlBF7JN1jS8rfPJqZvPfAKGt7QO_tRXnM9BRl1CHqRT0siupnp07wV5B7NEeGxkUgkn0IuyFdWC5bHbjdeB_2jO5w21xGhvPCOBnGG91y0J3csg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
تاریخچه قهرمانی‌های جام خیریه:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
21 بار — منچستر یونایتد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
18 بار — آرسنال.
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
16 بار — لیورپول.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
9 بار — اورتون.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
7 بار — منچستر سیتی.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
7 بار — تاتنهام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103909" target="_blank">📅 19:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHhAp7HQjNmMNhNcB8gF2oCt2jUk6EHwukUWj21nT65Vkr8kH458iDYr8Jv5WqcUAtpoPgPHoFohG5SDtq7APu1RdaoMZGhbd-Ce_cUpVuwKRZrWkragfOWb2o7pDOhvUiXbZ0Q3ESwKn8jRUcm1di8XFoNo5gmkq9uWW-tnTwQ2B_dBTqDRpIAyhUjNDQZGZT0BmX3QwDftmUEaPv5XKKFXkol_seJL8WnToeQ1fFrSdJoGk_A1JqJp253T0poVeuQzVI3NcPxM2Agg5Evuj6OLhFrbN0x3DFZhkCxsWh6eU2m38uRK2JEGe370EtBnku036cPwZwGZCx5Br5MPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز دوشنبه ۲۶ مرداد
💥
بیشتر از ۴۰۰ آپشن پیش بینی برای هر بازی در سایت بتگرام
✔️
شارژ حساب از طریق کارت بانکی،ووچر و ارزدیجیتال
✔️
۱۰۰٪ بونوس رایگان اولین واریز
✔️
امکان فروش شرط های خود
✔️
تسویه حساب بسیار سریع و بدون معطلی
⚡️
همین حالا ثبت‌ نام کنید و و از بونوس‌های ویژهٔ بتگرام بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103908" target="_blank">📅 19:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7EnbJqNrH-fam-uyUPEM_yU-Js5P-Z1ToKy4Nt33AcSRfe6p1JIYze-o1fBp9djtx8N65SrLuukyRDL5gR5DJOcWigRpOok6PJ6O0cH8i_VSXek-HS15XdTzdj7ZzE3Ck0wxXl2YDsKJvXEKAlRbg--j53dxOzkLRM0ObwWped59A-CQhpBL2AeEDCrPX9IkBBvDkdcES8MAXWjmi0VQwtzCxEP1zMAWyGiCzhqqFY83aCJDmjzHflsjh_NGPrP5exlhND7yKpq2Ol3ko0AUeWeXGbPH-u8yrU5dnZwUpBCyX9qIh2nbOmKBq-n7KmwbjYfe671ZDE1dEkujLO-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#رسمیییییی
؛ کسری طاهری بازیکن نساجی با عقد قراردادی به سپاهان اصفهان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103907" target="_blank">📅 19:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElXGddR1zbUbvjtRtffUMetnINDPKToZDBY3rGWHxFY6a2OUXoFpW03nN-0AlkYgZLOqEpykxl0ai9vcLXlxKnftYHWZ8U9NtG4hscD2vxxXS63lCmUl7Wo_LAGNh551wVXFPcPi4UnurpI-4yUogieAV0IFDRQLA3AR3xOBY5l79GizDS4n1_LSSDxMTRV5yULusmxJoEy1mb24HjNQbGAFCATR2pe6KVxvHFdAqfTol2FOMgB9SJFXiI-ZcvkDYs7dM9k65HswpBXkCt6itMWXkYwV_L_NFjIyExfRLywGIBzw6-2d-MI624BTosfhQ-GwGJkNpSxrVPutfDvoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
پایان‌بازی جام‌خیریه فوتبال انگلیس؛ نبرد دو غول فوتبال انگلیس قاطعانه به سود آرسنال شد؛ روزگار سیتی بعد از پپ رو به افول خواهد رفت؟
⚽️
آرسنال
😆
-
😏
منچسترسیتی
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103906" target="_blank">📅 19:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103905">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYM5EDY86py558nAM6bG05n9HATearA8RlJ411Id1TSN4JpPEBxLpx-Ufs3aRsxI8wU067aGq-7yeUm3RBypkziXL5Qf1SBhHX7jmNMK5x08DgswFZ9z4FmK0aWunws07Q6fru0obrngELLXG9p_4mLyaUwNleWoLXCkjR1K_W6otzPVFtaQs6ObBEKjYLM7Qii3AIvL04M2nQIz-i1esaNJ8EkWWOA91qpeZVSOTlqJ-TRmqkZrqtgk0SX2ABUKF0LN_C_kRhOu5y_MJ6s-f8NjWyiMKYuElxJSJ4oQOlm6r7x22-tyWe52wvjsGpu0SA9-B4oN4CZBcR9GBe6NCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
پایان‌بازی جام‌خیریه فوتبال انگلیس؛ نبرد دو غول فوتبال انگلیس قاطعانه به سود آرسنال شد؛ روزگار سیتی بعد از پپ رو به افول خواهد رفت؟
⚽️
آرسنال
😆
-
😏
منچسترسیتی
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103905" target="_blank">📅 19:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103904">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlzAGaBWMH85CxIPkFgE5oCOj0_kJ_LoMvLWYHOTWXyLy8HfHB7_qk9KzlDJL3Pbzv4v-hwCjvJJw4LKR-YkvN_vL-9xhXhrPhOuAy7clqbZP2ceQPhg3WA27yf0mePZcMocImrD7Qm-Gwd3k_hj4avRlxW8FLU08Xde_QL_Y7k8QABYnMKaru9Xh5uMRVQyudjcTrq5l2IDWfLLCr-DV04xqDEZ2xcje0kNdWQP6A-VAZ9g9qdeUK9oCS0QqfTB0LtFNGeo2UFXseFMK9LcWKqxeq-OGJrIfo9ZRq1uhjYzFT752ZiATH4NMbNvUco_-C5LxHiJpj54SCRViszBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇵🇹
#فوووووری
از کریستیانو رونالدو: به احتمال بسیار زیاد پایان فصل‌جدید از فوتبال خداحافظی می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103904" target="_blank">📅 19:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244baec6e5.mp4?token=Qbpar26QeiqpyyJWH-KCvmQqO02L7FbkK1VlthUCAbW7o-8Pj5x1pyyARUP57uVJ1sKIpfnju_68LvL8sDzSpeey_Ml5q1Z-ywK-_DcCDiK7WrywyeuYsIWcizPDA67LcW0ZDam0VZ6gqBSvQCyIhKj9GMdgWMJ0xdKdDGvUSr6edVLKcVDT37-1h1Dc22gkuqKyQh_Y7C_EXesi_vWbAJdzrTepKC5fCBURMYpUP3ZnEGoK1p04ssE5szyNcsije8jZbDRF1YFXo0lCTbOPd3qn4VTatoNUdAQCZUuOE14AUc92e16TR4gXKBzhjymVQCMPaxv9d9FRhCKlGGXQwleKlu-vCZ_YVdMsC2xhmAQ3e2FDGSXSRKHNKNnsZIl3whEVZYqPSEiUX0YMe9_h7YE4HR3EzkZYF0XefJFWHoCBbv8XwqfYpxd9PDAkr7imvIJPoDJZsgVZ5-J1pK5U_L9YnT23o7tDEqj8zk6MROTKgNG09GK8GCbUkREB8y_DQexaZn4STjHQKy_lhCoKNnVmhirpIeXJmU2FsAOtzQEytBQPMGTH9lCNzoLMMfnnnwSq2yvZieLPLr23d32oWy0TISFDIhqQH7ZWtQzKKYbS5yFGu7AWuClkLq7TyoaPXKSB6By-LJQbiSW7aJ3d5YeBccOX3Hw-VlFoI4tf4GI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244baec6e5.mp4?token=Qbpar26QeiqpyyJWH-KCvmQqO02L7FbkK1VlthUCAbW7o-8Pj5x1pyyARUP57uVJ1sKIpfnju_68LvL8sDzSpeey_Ml5q1Z-ywK-_DcCDiK7WrywyeuYsIWcizPDA67LcW0ZDam0VZ6gqBSvQCyIhKj9GMdgWMJ0xdKdDGvUSr6edVLKcVDT37-1h1Dc22gkuqKyQh_Y7C_EXesi_vWbAJdzrTepKC5fCBURMYpUP3ZnEGoK1p04ssE5szyNcsije8jZbDRF1YFXo0lCTbOPd3qn4VTatoNUdAQCZUuOE14AUc92e16TR4gXKBzhjymVQCMPaxv9d9FRhCKlGGXQwleKlu-vCZ_YVdMsC2xhmAQ3e2FDGSXSRKHNKNnsZIl3whEVZYqPSEiUX0YMe9_h7YE4HR3EzkZYF0XefJFWHoCBbv8XwqfYpxd9PDAkr7imvIJPoDJZsgVZ5-J1pK5U_L9YnT23o7tDEqj8zk6MROTKgNG09GK8GCbUkREB8y_DQexaZn4STjHQKy_lhCoKNnVmhirpIeXJmU2FsAOtzQEytBQPMGTH9lCNzoLMMfnnnwSq2yvZieLPLr23d32oWy0TISFDIhqQH7ZWtQzKKYbS5yFGu7AWuClkLq7TyoaPXKSB6By-LJQbiSW7aJ3d5YeBccOX3Hw-VlFoI4tf4GI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
خداداد عزیزی: نمازم رو سروقت می‌خونم اما رفیق عرق خور و سگ‌مست هم دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103903" target="_blank">📅 19:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d00dcf8bc.mp4?token=CPMxbHlrUWXGadfz7N1IFNkUhrhVE135s1sK5tcoeSNeqkXX0mrKk6ZSaJYDSfxN6FBQduhW6VkV03DrHVkbeiQw23zHM5e7hZ_p5E6OLxXxJFFkB1SH-NaGcpItSrD1m8gSzy8fOcjf38c8yr-Nt8ThYpMPGdwolGfLr_qAPbaHoxlpMC0rlPlvIKn0Pq5R4jtYxwl0Nobaw1wu-PpEpOLqpO56Fse_TdufyCIeMShSgAgBVliFF_KnZ1GR0RPB5R5j3Q0FRAyqkNzh6FOeLfUSuzRmOzszqKRmDvpYhLSPUpc902uxPMYvoK1XYMUVNy2qjea8sKPaCa6m-eMXTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d00dcf8bc.mp4?token=CPMxbHlrUWXGadfz7N1IFNkUhrhVE135s1sK5tcoeSNeqkXX0mrKk6ZSaJYDSfxN6FBQduhW6VkV03DrHVkbeiQw23zHM5e7hZ_p5E6OLxXxJFFkB1SH-NaGcpItSrD1m8gSzy8fOcjf38c8yr-Nt8ThYpMPGdwolGfLr_qAPbaHoxlpMC0rlPlvIKn0Pq5R4jtYxwl0Nobaw1wu-PpEpOLqpO56Fse_TdufyCIeMShSgAgBVliFF_KnZ1GR0RPB5R5j3Q0FRAyqkNzh6FOeLfUSuzRmOzszqKRmDvpYhLSPUpc902uxPMYvoK1XYMUVNy2qjea8sKPaCa6m-eMXTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گلزنی کیلیان امباپه در بازی امروز رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103902" target="_blank">📅 18:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754c7f88a2.mp4?token=OykZYmEyAN2_1lf05NJUKD3YGqRvbPz1_Jnd7fB_nATUL456WTW_cPpD__8zDkF6FIlH0-Ke6aIxF1HC8aA9Dl4JN5I47aAWdhlLMlQDac6Ykolsedhexe98a9OzFVQ_KClyifhS-IXZgdKje8Tjx2TrPFPTEvFQnT2fQCAftJALzAUjdm2Goefum3JEr87TvWZ_AG6MhUoS52ZoHAoRSbbTwdizH46nGeUK6UJIK3khNkCJadAPfiobzzJ_WDQPtr7FDXoyCXgztOexAQG2KKXiwUDYPSlJLbYVjEYjhdvWopSCHLue6xHxuHDYso41IdWEDyayX8-_JzKTtiuz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754c7f88a2.mp4?token=OykZYmEyAN2_1lf05NJUKD3YGqRvbPz1_Jnd7fB_nATUL456WTW_cPpD__8zDkF6FIlH0-Ke6aIxF1HC8aA9Dl4JN5I47aAWdhlLMlQDac6Ykolsedhexe98a9OzFVQ_KClyifhS-IXZgdKje8Tjx2TrPFPTEvFQnT2fQCAftJALzAUjdm2Goefum3JEr87TvWZ_AG6MhUoS52ZoHAoRSbbTwdizH46nGeUK6UJIK3khNkCJadAPfiobzzJ_WDQPtr7FDXoyCXgztOexAQG2KKXiwUDYPSlJLbYVjEYjhdvWopSCHLue6xHxuHDYso41IdWEDyayX8-_JzKTtiuz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل کریم‌آدیمی در بازی امروز بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103901" target="_blank">📅 18:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گگگگگگگلللل سوم آرسناااال</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103900" target="_blank">📅 18:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56381f5fdc.mp4?token=n2DUabW_b70MJ188SJ-dnPcVR8cdS_heLcRVLxgUeCD2_yw_azh-BkXyYIIigiXbVt3Msd4wPEw4cx8nGEmfyjoqSgoyi5MZ6BLcFK9vfezizCBn11E4Vj6GAAAsVwrXz8MzzKZPxObdyY-nO-HVnCp8S7HTfFUeqd-3N5x0s5H3aZcM54BsytDso1N1iJEIzouby8Cn20IXE7yUCESog-VTA6EfMYokDqh-yM28USqLmFgct-SSVu7tzeKRClT8_Kk6RyRfsDggqS-y9w6JiiiQcijImMGe7D_ew2gEDDc-_YLLu9qoEdEd6Prj1cy9WmznSU8ZQKpNzmyzT-_MuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56381f5fdc.mp4?token=n2DUabW_b70MJ188SJ-dnPcVR8cdS_heLcRVLxgUeCD2_yw_azh-BkXyYIIigiXbVt3Msd4wPEw4cx8nGEmfyjoqSgoyi5MZ6BLcFK9vfezizCBn11E4Vj6GAAAsVwrXz8MzzKZPxObdyY-nO-HVnCp8S7HTfFUeqd-3N5x0s5H3aZcM54BsytDso1N1iJEIzouby8Cn20IXE7yUCESog-VTA6EfMYokDqh-yM28USqLmFgct-SSVu7tzeKRClT8_Kk6RyRfsDggqS-y9w6JiiiQcijImMGe7D_ew2gEDDc-_YLLu9qoEdEd6Prj1cy9WmznSU8ZQKpNzmyzT-_MuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
امیرعلی‌اکبری میگه روزم نبود بخاطر همین ناک اوت شدم. ما که نفهمیدیم روزش کی هست
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103899" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6oj6cKZ8K2RVchCMJiyn2ackZGbwA-W227vLvvXh2hZQ8Jz-wbcAse5vHHyRrL_OLXKqbdGQ3lC8PJVccaxlzThHhkPx0TAZYt9HyeUqKpDRRd0Dnf0_RXFGerf5lq2Xe4RH4xrXfMwUIPFQiBzxNoUc-5T7XyygaExK9Spvhj9j9hJ4EmfMZbYFjYGNfcWEw9DIosoKmtA4OWWwmPXCRLZ8_q9vuxw99wem8YTHdPQQz-e3BBnnEpLgffi_a3ICWE3MPBpDZ4NAfW1Z_w7r1XSENTdxpOCnWEUtiOH5IEFv14V5sU3ly8v7RrKSRZn3rBundQwjasc5NvbLi_BzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام اسامی داوران هفته دوم لیگ برتر
🇮🇷
🇮🇷
استقلال - نساجی/بیژن حیدری
🇮🇷
🇮🇷
پرسپولیس - اس‌خوزستان/حسن اکرمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103898" target="_blank">📅 18:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3ab768679e.mp4?token=SphXLZhiSQvnhmHIzDhZorozf_1IOqvr3oxUxYbNkWSgKkn3udornisvCIUXaLUgzgBFNumtCXVg2Nb7rYQ3mrqLE8zKR8rqvi6po4f98y1NGebQR2G4AeaP37mkxWDgtODepXfq0YllyATNN3YakdBW25u0-1GD6C7mRxNfIzwH5nayYFitmk-I1BMylnpWSUBBjzWGSt1RQ3l7jda57KZvJnM9s8A-foRgu7lyXQ0G67v7BcVpuU9isAX9U9WI1NLrGAC2Fw-3pqO-bZOS5NXhx0aEQCn76QygsapXCh5Qp2uVNxGS-Dvd75RzRjMNBApTQYC-sBwL1kVyDnaC7S5ionPV1OFLcYn_4Af2sT2LeO7Tm40Ztt4Zf3H_yHWku8yDuK4UwP7Ewu0rPuAMpQ2SpeLYLq36QsoqHfSnk2_eUYnnD_htkfkrIqBzLQtbvOQUvGep9prwttZC4W_4-2ssJVt1qcwMX2v65XlMJC9gW-YT9dlPK2pjZwz85a-1QFNclSBTlAQbXcN2cub-5HQN5i0YRFRR4W6D-GZsrUg3BcR2lzEs7Jz1AmpOU8gz5EW9VAiYr7_vD9EttxxjB6baxn3gOxD44dwVn2v1Ue_xPd0ZpgUFmgypsxDIur16Q8dnrjLF235-MsD3ief8NCUBe74wkRiJL5gDe2s4x8k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3ab768679e.mp4?token=SphXLZhiSQvnhmHIzDhZorozf_1IOqvr3oxUxYbNkWSgKkn3udornisvCIUXaLUgzgBFNumtCXVg2Nb7rYQ3mrqLE8zKR8rqvi6po4f98y1NGebQR2G4AeaP37mkxWDgtODepXfq0YllyATNN3YakdBW25u0-1GD6C7mRxNfIzwH5nayYFitmk-I1BMylnpWSUBBjzWGSt1RQ3l7jda57KZvJnM9s8A-foRgu7lyXQ0G67v7BcVpuU9isAX9U9WI1NLrGAC2Fw-3pqO-bZOS5NXhx0aEQCn76QygsapXCh5Qp2uVNxGS-Dvd75RzRjMNBApTQYC-sBwL1kVyDnaC7S5ionPV1OFLcYn_4Af2sT2LeO7Tm40Ztt4Zf3H_yHWku8yDuK4UwP7Ewu0rPuAMpQ2SpeLYLq36QsoqHfSnk2_eUYnnD_htkfkrIqBzLQtbvOQUvGep9prwttZC4W_4-2ssJVt1qcwMX2v65XlMJC9gW-YT9dlPK2pjZwz85a-1QFNclSBTlAQbXcN2cub-5HQN5i0YRFRR4W6D-GZsrUg3BcR2lzEs7Jz1AmpOU8gz5EW9VAiYr7_vD9EttxxjB6baxn3gOxD44dwVn2v1Ue_xPd0ZpgUFmgypsxDIur16Q8dnrjLF235-MsD3ief8NCUBe74wkRiJL5gDe2s4x8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال توسط کای‌هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103897" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103896" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEkNGtnaM_SMUnLQYuAy93M0niQgphj1f2wa706yqqciusAbhBoDFU7qy1D5aWZUoF-TedQxPvPSzCzsM43QYZyessrfs_ARGOm8WuyZq71yHtc9vUV32iSmOEH1M492LWtab5CluLPp4Tci2LlT5x0jtFLg8hmR3KuH0netyAfzUDvcFPzQJ9vob7SzLnEfSzmjz25w1mDDcc6VtxduJxKD1BMUG_T_SCfjpuDHutOkNkBCLO2Y9LV2p0zM0WfavG6XfzEOQJ5ZdjNV36jiIcxZQ9TQ3D-awDJKAYOK2zpq7H_xnREuiIkKaqtHpAQUT2AIenavDoUiWMNgPeD1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g25
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103895" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگگلگلگلگ دوم آرسنال هاورتززززز</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103894" target="_blank">📅 18:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103893">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0fc033ef.mp4?token=CgK-wchzeemHv1dd_U5nQT1E9rHpwFKz3StlsvV8NNbAsZNYejidu1SJNHsFEhT3IJoxlM0wa0kSB3flIKVV586VQ-6yxvzt62oo8dxEwC30PzzElCrRbm3hmEL-Jw9Jh-GjsQoXqM9Ru3luin7T8xjhfeM7UCks3KlLARPdNPWfTA7pmS2WO3rLGNIveo-jLG9YKG8TiSD79qHlyiyeOyAciKT8hA0KaRJDuyPO0_uGWWC52foGyeL2hLrSGeFleA1eNgCpUP4jMBkXqi2ohpYGqIktG0EpSem178scxf_cFzlSRR4mvrP48xkt-YdB74AhQkOhFeAJIJkeQ153Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0fc033ef.mp4?token=CgK-wchzeemHv1dd_U5nQT1E9rHpwFKz3StlsvV8NNbAsZNYejidu1SJNHsFEhT3IJoxlM0wa0kSB3flIKVV586VQ-6yxvzt62oo8dxEwC30PzzElCrRbm3hmEL-Jw9Jh-GjsQoXqM9Ru3luin7T8xjhfeM7UCks3KlLARPdNPWfTA7pmS2WO3rLGNIveo-jLG9YKG8TiSD79qHlyiyeOyAciKT8hA0KaRJDuyPO0_uGWWC52foGyeL2hLrSGeFleA1eNgCpUP4jMBkXqi2ohpYGqIktG0EpSem178scxf_cFzlSRR4mvrP48xkt-YdB74AhQkOhFeAJIJkeQ153Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
سوپرگل دیشب ژائو فلیکس برای النصر که رونالدو از روی سکو پشماش فر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103893" target="_blank">📅 18:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103892">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648b67b731.mp4?token=hfjwdVTez1M3KGhqRYi9WZq_EpYnk1o8TTXzcEEWghe6v1TKL9fhn-8Idh40NJ07an4gocEdxbzlBMMs2SxDjaMTSWk4utWP_ezTeyNtB0vthubii55rpPO1A0UsxmpAgaP6_BltpH8gnt1SwYNNgTz6LD2nLkSE4JCvGJBV7Kcfdaz_vuGxkV8igGUdkPg79-wsn4pModXF9BpZY3_qXZnePwLq2Jc6YykbgB6bfUS8l1F7iewV_sL_eDlRIdjaRbU1G-h8-WIEzZVKLQKz8GI9x2KvBBfZ_C303K2JN511CmD9-3edePVqiouC2mvmwW2A8hFeHY4UspENQWtmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648b67b731.mp4?token=hfjwdVTez1M3KGhqRYi9WZq_EpYnk1o8TTXzcEEWghe6v1TKL9fhn-8Idh40NJ07an4gocEdxbzlBMMs2SxDjaMTSWk4utWP_ezTeyNtB0vthubii55rpPO1A0UsxmpAgaP6_BltpH8gnt1SwYNNgTz6LD2nLkSE4JCvGJBV7Kcfdaz_vuGxkV8igGUdkPg79-wsn4pModXF9BpZY3_qXZnePwLq2Jc6YykbgB6bfUS8l1F7iewV_sL_eDlRIdjaRbU1G-h8-WIEzZVKLQKz8GI9x2KvBBfZ_C303K2JN511CmD9-3edePVqiouC2mvmwW2A8hFeHY4UspENQWtmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول آرسنال به منچستر سیتی توسط کالافیوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103892" target="_blank">📅 17:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103891">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آرسنال یکی به سیتی فرو کردددددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103891" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103890">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103890" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcoa6bEzT5WDhopbW9TU2WxkzXLdkB2HdOgfcYdsMWVNAW8VX-6u4OZxOyCK-mnugcML7EpO57nrBEp2hYXd9TDGBNZsvxH5OKhNGTIgNFcT6RuKxs-p3DCl9GMSmHxVFqXg-mhTAQXo4_sd_0w-NYkw_QMWeB94O5XDUkbnC-HPLMNbY9J7KzuTULGc7PHvseSOJTtVumiJriFq4F_HeDynmL32Kte2OJ_-2H_3GMO06HMDuFxf1xDm4DL0tDPHcpvpPt6zsUTQ8r6HzekSxWwGCdqoqICYlP-z2Zsw6AnjufpiFnNCUrzMEROwdnQkxTiLYAodysjmEeBIBPnFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZnzkiYKhhSExkT0A5EuwOtnCRq0_nvNxsCgQ2kPiw-32e3BKrJMQV5oF6ai0URjGj8TW6sMAKrm9TtavBewOj5U5GhzrjdHPB5DqxigMFDt2dXJZtx-GnafO22yGFVO8iiRTduMIPOGbdM5wVn4fsPoO7Lxkokk8qGDU5A-TWciHqfsv56ZCQjJALDmtkSLrJ--sx_HSia7gmBgVcOalvsDDekx4hXpIDIYw4GLHirc0QmDMTgFiUiDYS5w7NnRTrz7XlIR5K7JzVeuYnzMfjxD407V0qou1RWgj_8r_ULtdaK34PueAF1ybGGCnOtXd1rlgHLBPjld7ODmmYXKMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب رئال‌مادرید و بارسلونا در بازی‌های امروز تدارکاتی مقابل بازل و شالکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103888" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2aced863.mp4?token=ZGTYw1N6l89H7zfW2RYJSxszfq2E_ZNwkE7xrl2N0Q--GX3tzFCPFqazNiJixmbuY1XiOQ4nfA_dfP1yjiLNNjmLReWcTmDKQR8SjJka26A04rqkd0rcmk1m0oibE2G1u1jtej8O1Hpe5JN55PbhgyVPJhWT9Z22G-b9KtokA6tujH1gOZ04ANOizOua2s-0zwz6CZO76x8-0S8QjtNBZ6AEL4rDunm_FeaYdC_-uXpu-cpokeMwXVNOU71PIzSmPJp9VkJ_Da7twEXsX1RnKHhrYwu9XQ3bwLYrUacZRJ5DNSTFlq1FSGcT-Y0MLlYaKkE1wVgaCl20ERd2oTsICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2aced863.mp4?token=ZGTYw1N6l89H7zfW2RYJSxszfq2E_ZNwkE7xrl2N0Q--GX3tzFCPFqazNiJixmbuY1XiOQ4nfA_dfP1yjiLNNjmLReWcTmDKQR8SjJka26A04rqkd0rcmk1m0oibE2G1u1jtej8O1Hpe5JN55PbhgyVPJhWT9Z22G-b9KtokA6tujH1gOZ04ANOizOua2s-0zwz6CZO76x8-0S8QjtNBZ6AEL4rDunm_FeaYdC_-uXpu-cpokeMwXVNOU71PIzSmPJp9VkJ_Da7twEXsX1RnKHhrYwu9XQ3bwLYrUacZRJ5DNSTFlq1FSGcT-Y0MLlYaKkE1wVgaCl20ERd2oTsICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
عملکرد ابوالفضل جلالی در اولین حضور فیکس در ترکیب تیم‌فوتبال پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103887" target="_blank">📅 17:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6927287d81.mp4?token=hlveF5DQHl2Ddxfm2-BNanRqqBFvkm55WTAtkjONP-c1wXha_v2sSdK1ybaud8yb0Zxd52R9uhgMfbrRPqroKAJab7tITknOGAhT_vu2T3CCeZqMjPewgSg_87BVOpsMcp2SVzF6JGDNL1PeH__VnmiWMkIDrlc9nQoQ1uNfxiX1ENrIVosoZfT3k-R0vUJLhIV_gKfjS5epS8_7TsAzChdptvQguDJgp5WHF8g97zq72jzumS35uH9eXMB99wdbN18B9gbayigCh7hp5EoQNVXDJMfMit0hdOGJU9EUTF47t1uATqh26kBBl0aYt9gTckDa1V-8avzyPeUbIzhI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6927287d81.mp4?token=hlveF5DQHl2Ddxfm2-BNanRqqBFvkm55WTAtkjONP-c1wXha_v2sSdK1ybaud8yb0Zxd52R9uhgMfbrRPqroKAJab7tITknOGAhT_vu2T3CCeZqMjPewgSg_87BVOpsMcp2SVzF6JGDNL1PeH__VnmiWMkIDrlc9nQoQ1uNfxiX1ENrIVosoZfT3k-R0vUJLhIV_gKfjS5epS8_7TsAzChdptvQguDJgp5WHF8g97zq72jzumS35uH9eXMB99wdbN18B9gbayigCh7hp5EoQNVXDJMfMit0hdOGJU9EUTF47t1uATqh26kBBl0aYt9gTckDa1V-8avzyPeUbIzhI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
تمسخر ۵ سانت و ۱۰ سانت امیر قلعه‌نویی در گفتگوی خداداد عزیزی و مجید واشقانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103886" target="_blank">📅 16:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5zXh8-qGWsxccOao3MZK6jeL6POYF70YibiQQGCu4fU_b0gkhfexP7GTsDnjs7nL1RLfI6-uRem6pJJc3J3M_RJwGtaYfK5Wt_TMgSRMlsjSkv1ruaJETnaT5t4pRTHKH_p0dzQ-qmyppP_Xp3mLBH9zQW9_q6ZBzreor7o0xnpj3jPkfBKg-yIPkZvRpgxwAkyLRNUs99Q-ECrMPoN-YxZEK7X3RqrRXyqFEsDpHEgLSI1sGf_YK5q1oBjlbJn2rvrklhhrLDBxR_4yJonvYGxxfcyYjEvsyRtpa5CaJVG8eWPV8NVyUT1akPDlCPhA8YjBAjXncBpf8vWS6fJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
5 مسابقات اخیر بین سیتی و آرسنال:
آرسنال 2-2 سیتی (2024)
آرسنال 5-1 سیتی (2025)
سیتی 1-1 آرسنال (2026)
سیتی 2-0 آرسنال (2026)
آرسنال 1-2 سیتی (2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103885" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248d4f7bea.mp4?token=QxpbyYIhHLe7iuX0_6sxXMZjAcWRWnTcbqPfvfiY6BzIW1NVn-HHTfXhVl90tAJK595FQqU6tLfAI9XZjvE4d2gwz28N9zkpTZti7kavMB631ogyaDcZRzedYbRV3M_396AfeWVstbHXivpouFnJYca8maTJnNPmyG7Qhi0KYFaXxXAT0RtHJRxPhjbr9S5xhqcJjgQAEIlZmxDhjbWdeNx_osOckQA4vfQFokbiNoQnHO17UBpK7YoZ4HpDGEO3AI8ljclijC87n6-S-tTPa49TOHMmoZs3tjLNr1lgOmiFhsDu2ZfBNPJh9N35AZrihLXVY_2jjLr7X6CZLKUq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248d4f7bea.mp4?token=QxpbyYIhHLe7iuX0_6sxXMZjAcWRWnTcbqPfvfiY6BzIW1NVn-HHTfXhVl90tAJK595FQqU6tLfAI9XZjvE4d2gwz28N9zkpTZti7kavMB631ogyaDcZRzedYbRV3M_396AfeWVstbHXivpouFnJYca8maTJnNPmyG7Qhi0KYFaXxXAT0RtHJRxPhjbr9S5xhqcJjgQAEIlZmxDhjbWdeNx_osOckQA4vfQFokbiNoQnHO17UBpK7YoZ4HpDGEO3AI8ljclijC87n6-S-tTPa49TOHMmoZs3tjLNr1lgOmiFhsDu2ZfBNPJh9N35AZrihLXVY_2jjLr7X6CZLKUq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رامین‌رضاییان خوش‌اشتها
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103884" target="_blank">📅 15:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b623d393f.mp4?token=KK_5J03YoZiD5ESlouce6hd7vH7ADwSrvzjEdh0xyF9vA1jAdGUJWExYEKTvFIeNhFvue67F88jOGlmSk2Ulh2ob0P0Ll442JFw400gXRxRx-_tCS_I8Lsu58__I_sr73B6o8HiUDOXDiFA9ZvRtD5hWVNY2yEJHUcIfiavChT0uqZcvscEuXiv6BlYdtEpkMMtJaCcKELo4qMXrTPC_KV5AtQWMD5TLsIBIH59m_3711KDZssCRUEaoHdlqLgGfmXYZg_pYv6LvIvya8AfZtTR4rBEFReIU_jwd6uMjubpGVOifCGk7sREgxbxcRyskNvaTga90tzIgjt-Jy1QS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b623d393f.mp4?token=KK_5J03YoZiD5ESlouce6hd7vH7ADwSrvzjEdh0xyF9vA1jAdGUJWExYEKTvFIeNhFvue67F88jOGlmSk2Ulh2ob0P0Ll442JFw400gXRxRx-_tCS_I8Lsu58__I_sr73B6o8HiUDOXDiFA9ZvRtD5hWVNY2yEJHUcIfiavChT0uqZcvscEuXiv6BlYdtEpkMMtJaCcKELo4qMXrTPC_KV5AtQWMD5TLsIBIH59m_3711KDZssCRUEaoHdlqLgGfmXYZg_pYv6LvIvya8AfZtTR4rBEFReIU_jwd6uMjubpGVOifCGk7sREgxbxcRyskNvaTga90tzIgjt-Jy1QS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشی داره تشویق یاد میده یا تقه‌زدنو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103883" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103881">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kXwNWZBLKZvmqIfdCcT1wCqvJsYUbz3MbXa82NoNvRJ_uPxdN9PY93tEGv_gjY7JcbW4YTavPCuB1vjz5VXPLusvnHc_L302qn2w3kC-Rs2vaE-mJeFUlodgS5adM7XKgivMOZLyPaJpAZFDdR6J_wndl5kYdWoY-33TqIhTi0dHJOkuXQMxgW_f5yZJZ9g2T68zn4GmM7zT6oDpbF1ux-OI5qQ48uM00Jjs7qdJE5AgRHVsw13QEdODlq35rnmCizWpm3TBX0ZYS_C_GQMp8L3LVbsiodXsHnNPPip3DNQyYLki2fwxJZkGZYMn_BKxHJMEs_uCpxUXFEyOU81ayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q64RpEwc-qX9Tx83C_0RV7yMxzjC0fk5lXBlEodDer2A2kq7ClaZbSuIy3aqTp_59FgkBwPlnIbYrKvSyxBscg20QrfqlveF7dhfeuKssRIfZWJL49_b-QbtxyCLbDs9OI3xPnfRcYmfpzQtGJuUTdc7iE-AWMZ0EZn8AkF5IwDmHtwGxQky4JW_20-HHmcCTNLQ47LtSIrDFAFS2CqfqzV2BHUUwkl99pK5YxigT1YXc7Swc7U7LsGAFfgAta2HX_F-gqFDcUlQtu2XWb22Gtf-ety_I8U2VFcvGHbB31qZJCi2KbrPnrHw1x4rdORAz_oOpO1Efr_9c34UY-S7Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😐
🇮🇷
عباس اسماعیل‌بیگی لیدر پرسپولیس درحال یاد دادن‌تشویق وایکینگ‌ها به طرفداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103881" target="_blank">📅 15:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103880">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP311GYroWRpguZ4PY65duGFF8Fyo98ngzU7BVTwQd3LZa7la8CzOwWHBqs_bawPgBkjcnA9feOk9m-IUnymT-j0hbtupp9axIUv3qox-H0HdcQEvO5tPALRbjn50ehcwdPFkCKCGnIw0cR4s8-pJ-OuS3K5ASZUIy1fqUTn0ybN1IZRVLcD-FCQpFbRpmi4HeyoUs_iuQPNQ4CgfyHpZ1DxSLLcFi2ZNSL6r9kZ8izXtXCloE3Av9M1r6XuE_PxNrhy34D3KXNOZL3CH8p3Tpbx-Il1sE4Qr2bgR9ncM9Rtfjcw-lQ7y5wFM3Hlu0gUjewsywcQRpFAcQ-HQv4z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فرهاد مجیدی پس از گذشت ۴ سال حضور در کشور امارات ساعاتی پیش به ایران بازگشت. مجیدی اخیرا پیشنهاد سرمربیگری تراکتور تبریز رو رد کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103880" target="_blank">📅 15:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103879">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLCwaHbFxaBrkSbJA3MEbadhyC3BnjW2g4x5EKYQTexNKqqNRL9H2iAgKwO2M6P0XKah-4yb_7vSvliFJqono8cHzYey3uf805I8CoYM5Q7dkPsM5S01smlrL7nMC6k1qLfcf9V894FqCwamiigt0kaZ9jT3Dv34gj4uerg7vSdOp3l4Zdq9yl_HtZrntMS9YTl0cJfNui1bOPDjNTkc6QJSPSlokCI-2JEJVGW2mOqwhLBQHu-LBBdxxph6e0wtmY4MrSdRvEipFCHJZm8_-urVf_KyCWbeaa6yxgYKDnRrOf1j1a_SxXvrqbFoZ_nT0kZxML7G5T4QNUBIL3SQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇪🇸
#فوووووری
از متئو مورتو: ژائو کانسلو با عقد قراردادی به بارسلونا بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103879" target="_blank">📅 15:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lu-n3GUMsf4RsZr2ptxlP4lMfvRoEbkItIUp9xRQYQq8VLw3T9C2dwVVrHdihWYaog9fNCjs2tCgbvlrUJoY7Qva2CW-DrAOSn9SqUi7NO4dG4RA6ylfQomeWk268473uKRYJx11td2aFp0soFFmE7xZ3zNiNkyk9Mz6nWwRB5m0vZ7sOLvNpuOSTws1kCYm3fCAQH8RZJ5z52Faqe2tR-iJIslen8FZPZvIbdVqx4z4a792JbSH60RieQdFXlaYihW8cMrARIVJ8si1E8oIc0GWGdGT9t-Krywoh0CxiUDF9HNUAvvW1HkVkR5QR6CvghkaeRsHmtfP0f3Fou-e7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCrt7mDL34hsBaOkCUX3_JtMsyt5KYsGu2Ac-zY1q_zectVOSyhQkRL0njDIzFUT8G940fClGihBuFUQR3ukviiIqAMewlA9kiHa87xguTEyRORKrgUlNvQQ73CJ16H1TaFn-k2BUqISbT13OH2FOL-2EYaibdOI8-ggJq2iIWnfn4NnG6jfLoSKOzZy64lgjYLmRszRfZDwZHCP5GJXs4CQJ0GiwMbPBpUapJvuAJYif1cFqspvpKC7JxUcBdRoUacD7WreQY4C4IzawMrfoaLcrT0N2weZlm8IfdI5MiYj4YsheCLbg-aGW-NmR13ntBKcl0_lDDjYzS2ovZUmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezsXJ-qBUsXr6N72jx76GpdYpfTytCbsckW1wbJL75NkvcR0VsLceSBWnIdEQcyj5qgTFB5nvawv55oLcyqNuqCHYi4mb5id8MSCIZrWakNdjnWB_cowEfN7r6LrmX2RaYTozQL3In4ILRpe_xm56UOZmNTqJTLByxJvaSE7QA2ITTnzlGPHmfPfr6aWcWQjFLsnx-k15m5EQCK_r3OYBLjVJlkUwCB40DVYAo3DSYyv4vV7ZN_QfVb5LJ9vfmOg6mP4Pp-KgV-vaNEJCPAnYpAVY0dxDA-VzEKMWAJt4m0gUYUkPKo9Pvp8KL1goPiXxgkaAo9ZHKWyzC4tfDleGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😢
⚠️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده حسابی ریده به سرتاپای اسطوره اخلاق و مردم‌دار نسل فوتبال فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103876" target="_blank">📅 15:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103875">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5Wf29OCPSbsoilELIl4lNKQfrFV51lijmnUywExksZmqRMopBfQLE-b9xZ5ASK42v9qrpZMQ6sYcO_pDFYgF8Mae0JsPrdL792CdOfTt_gavNNwT7iShFzxw9KgV3ZNS_a0vH-p_DQHGfiQ0Ej6W5bhJwExeGuoBiP3bdFyNj-VjINGaQ3_YRzb3JZw3L29qgqjTIvps_WBR8Ad2UqzlXN73eStBGkudwRDmVMkIZzOmhqVvC56UNRJyAe-Zx8vX0mvVktxjzHt7L21HPweJjq7JECp4yh-nouyUYwaExLQqjyIPOrko4ULYOHrhSWAm6gBYnQPUVQBp_Aq6spZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
غیررسمی؛ زایان سوزوکی دروازه‌بان 23 ساله ژاپنی به استون‌ویلا پیوست
💸
مبلغ انتقال: 30 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103875" target="_blank">📅 15:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccfdc09cad.mp4?token=UHmBY5R2wF1h5ll3YfkeF-q1ezm0Psrjt-v435LnyCzl4wr3WVeeNk5G2TYYUo2FV2oyNsIR6jUy5OP2r9QPC1NKwHZYT6eleO2uNwOvvnfE9vvZNH8wDDMpeR2IDQs6D5x70Oj5g3D29TJjID5yOXfu6T2iUHOU7QcKEUB8-JRqW7baKVhJyb8arHicSyiaJUnG64StDbc4CwGEzzu852qLAj2APVMXzxdsn-XAN2WMjuYvhHGKfSKhaguR4YFQswpOSzHDpkjAu0GZc3lki0qtlHLWwLN6bic-QWxnCA7nXEs2QHPCLtTpdNF1YEsR3HYmslbc44RhQaPWBl_22qqzsF0JZswuLTh6U8Sj6gn5z9PxCktQVcwXmGd8WQxDW0OP5SoKHpjbyODAkD1_i0yz1axqeA1aXc887lgW-YGm_IX1MuRKfyGTxFTZeaiMi3hSwTHBAK4hUJL0AC0lOo89sCNcTQtutRQ0BZa6tEZQoDKwvplsZy7UnQW3V6ZyFM27FFdAazjhVR-FOirI2Hwq0R6j7sFA2J8qIouGYkY5ZE1nZfzPqLuxiIETirUsxWNAJwxLkG-jDGh3PU8iJ32alRm8RNlJCWJ8KGcZRGR0b-cyktwYlxAUAs0LB6bojK49Sb5nCQs-YvFKOR0vj6b1Abvt3TV_yPDknGzea1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccfdc09cad.mp4?token=UHmBY5R2wF1h5ll3YfkeF-q1ezm0Psrjt-v435LnyCzl4wr3WVeeNk5G2TYYUo2FV2oyNsIR6jUy5OP2r9QPC1NKwHZYT6eleO2uNwOvvnfE9vvZNH8wDDMpeR2IDQs6D5x70Oj5g3D29TJjID5yOXfu6T2iUHOU7QcKEUB8-JRqW7baKVhJyb8arHicSyiaJUnG64StDbc4CwGEzzu852qLAj2APVMXzxdsn-XAN2WMjuYvhHGKfSKhaguR4YFQswpOSzHDpkjAu0GZc3lki0qtlHLWwLN6bic-QWxnCA7nXEs2QHPCLtTpdNF1YEsR3HYmslbc44RhQaPWBl_22qqzsF0JZswuLTh6U8Sj6gn5z9PxCktQVcwXmGd8WQxDW0OP5SoKHpjbyODAkD1_i0yz1axqeA1aXc887lgW-YGm_IX1MuRKfyGTxFTZeaiMi3hSwTHBAK4hUJL0AC0lOo89sCNcTQtutRQ0BZa6tEZQoDKwvplsZy7UnQW3V6ZyFM27FFdAazjhVR-FOirI2Hwq0R6j7sFA2J8qIouGYkY5ZE1nZfzPqLuxiIETirUsxWNAJwxLkG-jDGh3PU8iJ32alRm8RNlJCWJ8KGcZRGR0b-cyktwYlxAUAs0LB6bojK49Sb5nCQs-YvFKOR0vj6b1Abvt3TV_yPDknGzea1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
به‌بهانه خداحافظی چیرو ایموبیله از فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103874" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9IINhDIiUVNuh7T7ULcpO0k4VySOax1KNbEyh0TEsi4Qvge_EcZzR9Wif1xbmOXq6GRISOh0bLeE0-22huT65lUtrIw6Oi6VUXv0w8Pl8UsJtokN_PgpL5vwRIdq3wK1BCaRlFeVxfdAN41wOKqpMbro408674uogL0vFpey6voulmtpMzUP--OOrMj9A-n1JXU_nhEdFbOBcIu0uyCCX_vaWImOilDBktIdZaxmYAmCG3yv2entTis1xuhfZBYTfb3CuvROXQdsiiTuj16A0a3GdnuuTYLqQ5pr0nh65wj8eAvxc30-5rL6jZTbuoivSSTN3wKi9lPjiFtNZqHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار فصل‌گذشته دیومانده و آنتونی گوردون دو ستاره جدید بارسا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103873" target="_blank">📅 14:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794f2f910.mp4?token=qfk-xsT3tA89ZqL_MC9VZFGO1WxBFyzys_BJwYTkSw10-FhzlMMj8SfQcWSnOBaBGc0S5ONwR8BhkPOUZwk-0GhjX_YmB8KpLzG6GlPTWeSE8tf7lENgRvxn2L9f55TOmHqlW6Pu3lCmThZ9t9ct2ayIX0DWIYodjCcjQCW8nOrAP0WnOLqcJPJPoe2iksjVRuyi1e5r-s331Un-5_hGYdEYVRnU-wUzwJcvNr_vrgQVY1X89-e_7vQL08gWxQHMJPBfwJzQG2tk_jDUO0HN1xozxew_75ytSS7mV5NZ8rwg7MhPPcC-JM6GNuwJZbDA3JHSqwGiu0anuESz1oxocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794f2f910.mp4?token=qfk-xsT3tA89ZqL_MC9VZFGO1WxBFyzys_BJwYTkSw10-FhzlMMj8SfQcWSnOBaBGc0S5ONwR8BhkPOUZwk-0GhjX_YmB8KpLzG6GlPTWeSE8tf7lENgRvxn2L9f55TOmHqlW6Pu3lCmThZ9t9ct2ayIX0DWIYodjCcjQCW8nOrAP0WnOLqcJPJPoe2iksjVRuyi1e5r-s331Un-5_hGYdEYVRnU-wUzwJcvNr_vrgQVY1X89-e_7vQL08gWxQHMJPBfwJzQG2tk_jDUO0HN1xozxew_75ytSS7mV5NZ8rwg7MhPPcC-JM6GNuwJZbDA3JHSqwGiu0anuESz1oxocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
روملو لوکاکو: تلاش میکنم یک‌ماهه ترکی یاد بگیرم، سخته اما من زود یاد میگیرم!⁣
⁣
🥶
در صورت یادگیری زبان ترکی، این هشتمین زبانی خواهد بود که لوکاکو به آن تسلط خواهد داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103872" target="_blank">📅 14:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32096c018b.mp4?token=tUQ-o1mC3cptjxmUZ7u2czr-Bzm06GEHxfRmx5ZS0wDX6mDLOpL5Gw5Ahx3IF_jTKqfnyWTJgnWA8US1yHGV-FZhJZ6kbXCDeB12IPUSHGCoOnGhSxcUbBxwoVtxgEWOGNXe1fexXSc3-StSd7Y0kz2dIkrVrtILcg6JL74JhH61lIfgc021F7zLlW9jg48ZXwShrqgGts_nVqqxlvtYznWEIck617y_By9aaiOGPaNfU_NLqEGLyi7XMC0ulivudLvi0_Cx3l9kE6iflpzVEB8KLjFaYDf0prU_b0tjwCFXyAF0PVArXcnd6Gm32851vY12skRFhyZgP55tiH4ajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32096c018b.mp4?token=tUQ-o1mC3cptjxmUZ7u2czr-Bzm06GEHxfRmx5ZS0wDX6mDLOpL5Gw5Ahx3IF_jTKqfnyWTJgnWA8US1yHGV-FZhJZ6kbXCDeB12IPUSHGCoOnGhSxcUbBxwoVtxgEWOGNXe1fexXSc3-StSd7Y0kz2dIkrVrtILcg6JL74JhH61lIfgc021F7zLlW9jg48ZXwShrqgGts_nVqqxlvtYznWEIck617y_By9aaiOGPaNfU_NLqEGLyi7XMC0ulivudLvi0_Cx3l9kE6iflpzVEB8KLjFaYDf0prU_b0tjwCFXyAF0PVArXcnd6Gm32851vY12skRFhyZgP55tiH4ajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نونو مندز یا کوکوریا؟ بهترین دفاع چپ فعلی دنیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103871" target="_blank">📅 13:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2353879d41.mp4?token=BhyBJZAc2VZi_9w4KsqshEEyu2xSU8kdvZI0i16DTrpVJRZea8kIJ6UWseBplxOZ4-0U7D-1o06eYdCKw-jzD_-Xg0MGWAL4XM55-0OzdAjQv3WuISw29kDBh0MN0VQh5bsqarcES0k0LRnCdf_5hR--8YT9K1gQr6hXgH5jT-8t21YkMCS1uEHPS_XbKs2ycY0czi9r0zXMI-ZPJGfn82A2zLrstmU3uj8qvuib0QazGqXVuJ4qNak_x5MgsQf6WOT8Fhqa7wJRBWIXNqx9OHPJAY507BiDPFV-soYDydQceeOzddxrQYuYa1vvXzdAOcExwm-nCt7oGKzjunwkjGKz5zKifiMIZ0nZ16WyLLSn499dF7KXr7KtnlWitIoqyRYHP6nHy62cnpwkxhfTIk3RnVd4awEjs-FUKQw8pwpC18dcA4aizY0QjBS-3NH8GL4WpVax5K1BrDfZGLhCCNLukt11SMLuDFh-jm2iT4BStp5TQuAtvkOFB4K34okzIZ0Jq6b21DOk2sDLWBRCUCBm8IFkQb4D1oIhuRQY5G5c61ZbIHNmyV2B6Ql6bBd8vC64YeY5yGmiw3kFdd0K5QQ8XXYmohgDbFqJJDJOSFmqUJrRreihsZ_sp6kFCb1coEGzFqqO2GVv3IyVvFweIKrfW00f-hzyo9Bzlk7ic5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2353879d41.mp4?token=BhyBJZAc2VZi_9w4KsqshEEyu2xSU8kdvZI0i16DTrpVJRZea8kIJ6UWseBplxOZ4-0U7D-1o06eYdCKw-jzD_-Xg0MGWAL4XM55-0OzdAjQv3WuISw29kDBh0MN0VQh5bsqarcES0k0LRnCdf_5hR--8YT9K1gQr6hXgH5jT-8t21YkMCS1uEHPS_XbKs2ycY0czi9r0zXMI-ZPJGfn82A2zLrstmU3uj8qvuib0QazGqXVuJ4qNak_x5MgsQf6WOT8Fhqa7wJRBWIXNqx9OHPJAY507BiDPFV-soYDydQceeOzddxrQYuYa1vvXzdAOcExwm-nCt7oGKzjunwkjGKz5zKifiMIZ0nZ16WyLLSn499dF7KXr7KtnlWitIoqyRYHP6nHy62cnpwkxhfTIk3RnVd4awEjs-FUKQw8pwpC18dcA4aizY0QjBS-3NH8GL4WpVax5K1BrDfZGLhCCNLukt11SMLuDFh-jm2iT4BStp5TQuAtvkOFB4K34okzIZ0Jq6b21DOk2sDLWBRCUCBm8IFkQb4D1oIhuRQY5G5c61ZbIHNmyV2B6Ql6bBd8vC64YeY5yGmiw3kFdd0K5QQ8XXYmohgDbFqJJDJOSFmqUJrRreihsZ_sp6kFCb1coEGzFqqO2GVv3IyVvFweIKrfW00f-hzyo9Bzlk7ic5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
ادگار داویدز: زیدان مثل یه جونور بود و با وجود اینکه ستاره بزرگی بود از زیر تمرین در نمیرفت و پا به پای همه و بلکه بیشتر از بقیه تمرین میکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103870" target="_blank">📅 13:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1863d1e5.mp4?token=AmKloMRaVNaK1ZpJfinyC49RGvyLmIrMaI-prIu-RCHafrDBPBdyHHXrOGITZSiFowWoS4aP6ggPmm1qUviEdbQtERe_YpbZ7LJGsp95W7BbNJXYbjxuQVIAkJi0kieCErc_pjJ2vWYcMQ_PnOSplRJwqLFAItKxTZXYearCWv_iSsZP34x3YReKzt9ycxUIIi5vIVA2v_bMFxH-MAY_kFgPRiXvmO6lzqZgBDJz-qdStQSme3M8dvnIutZlNVtLcrNrgnz0UBeHU0E5z7kAwQnydS-QJFWi_nkB9dAFcF6II2_1bxhAeuX0vlwNi8f8vOJXsrSy3uymG1Aqpki3ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1863d1e5.mp4?token=AmKloMRaVNaK1ZpJfinyC49RGvyLmIrMaI-prIu-RCHafrDBPBdyHHXrOGITZSiFowWoS4aP6ggPmm1qUviEdbQtERe_YpbZ7LJGsp95W7BbNJXYbjxuQVIAkJi0kieCErc_pjJ2vWYcMQ_PnOSplRJwqLFAItKxTZXYearCWv_iSsZP34x3YReKzt9ycxUIIi5vIVA2v_bMFxH-MAY_kFgPRiXvmO6lzqZgBDJz-qdStQSme3M8dvnIutZlNVtLcrNrgnz0UBeHU0E5z7kAwQnydS-QJFWi_nkB9dAFcF6II2_1bxhAeuX0vlwNi8f8vOJXsrSy3uymG1Aqpki3ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
بیست‌سال حضور احسان‌حاج‌صفی در سطح اول فوتبال ایران با پیراهن سپاهان اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103869" target="_blank">📅 13:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103867">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3orUlFNxr4c_t8ZZecSDJuDDQHTP-U4Oe1NjSsKnwNKVthzJ8xhFowWJnGs8xFu6aUPUuWvp9n_zHggdh6zqydzpGP9xXRkwmhQipELx_J7CvDhvZoV4xNQnkSg_Z5Jx9Zt2c5c1BJUz0soSztjiCeOzh0Q396X5SmthEwU4usDiybnOBoqR83sWiFmdWLFY6Ar217ygRTQViRFsYlABVDCktduBArzBDFcOoOczWvgwoxer1PhRlOdGph8GSTq4uDC-PcvlMgUsLf1ghJ8J16Ql-IRE59-ir0btsh6nSxQB8YJkPTGrUDIHvBCfmXEGuIzgkK1rGx5ClEHoSD7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBJBxmQwcthv1-kofbrd3dGQUFE9taYpUmGP4eHs8PY4lkXPUc8l-WxRt2HIP0UV24vIX0Pu9iV36OYgrjFE_pVc0kRCD7y3oCP7AdIB-gaHBc0eZgRMdqk93bA9WdWCL5NiQ-mpRDDLAM4qm5WJTtC7iab6AUrxUAtidZlhRSqgjGyUe52PcyjVTUpkrMUILsuZ31lFlxQneGSCYpHy6XmERzYHQtMduzSb8i-FV-5CEqa5l-33FsdUpi0W2JV2Q9JrsURVAs9M9muj7Ra1GQV1JIeOZgx168YR7cmd3aL4ziutyYf5mXL13gFi4cu-kOliX6rUEh2koS95ID0tHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
اکس رونالدو خانم ایرینا شایک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103867" target="_blank">📅 12:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103866">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTwQvjb3D002nh1UzdW121jdSgAXOfqoCtrNVv2O_Mrbr47Cye-UmG-aKuhVIVwSLYXAkPTTaupaf2_v9ygQbVfqQ5oMFKkqbicS9CTsAzE-Iqv3_b2_uJbFbE5IGZ7K54k8RrZQ93TrLJ5YPe7DtdlCBempPJuLd-PUDD2vI9nVH48u--xEid9kPISf3rMMty78UeMckWsOyHw_p0K_vMKYtcoHeJ4_bwQGLaHkC_A61nHGrcHx_8o7_uR2LcyBI-wP2e8nlfu_gKuBB_oLt8X6OJ3PR-RtcrpBNeRiUyhicuDCCmMBL-zZmasH9NlffPGDjISGXkgDYWds5zmqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از نیکو شیرا: قرارداد برنال با بارسلونا تا 2031 بزودی تمدید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103866" target="_blank">📅 12:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103865">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86eaeca4c6.mp4?token=C6tb9ZWcQfNKBHRcM32CVpffe_WBDe5PpKLq3I3PnQZa5egu7WxLmvVnk1noaEDSt8-w8vT4oZ0QVCZITZeSLzC-QvcFhksYuJkp4yEgpoP8bTenACngwYi53WgoQ-FJ85bfBvFIaHHBv2FYqh0ZHReg9URbhNCSmgUvjHJkYQCM0BPYFBF1bLd8Z7C52WTlt_WOTiAcTNvosG01bbH91vYcbKwXCzZ6rkIy8iBljTa4b2Y1OclQnoZ7MLypvc1ghpj94C9QjsymT3Hnlke0BbR7TvLmtudVPKCmAuIjqRnlnCFNWLotgmGZI_xr19W9h3u3Ai1PsPJG-uypxrbs1C7EIOolRA1GEsN1mQl79liESXN5PLJG8P3mQzBg4QvkoMigPOJNXprXAyiaG2aQ7LkexymKREBhUlnwuJbWLtR2qOzu3TPEpK-QGb-cnG1vv9sD4LNAHptpvt_6sTRyIK9KYZtc7HcyPBinURRrRH0EzGhLib0mGK9nA8bGjx0GAhHnhtPqtu0_Io33hU2RWbjIrI9qv4TZ6sffqRdrWj8Amhlc5qAe0Mpt146pV-tNYM-TKNv8UQ3StUi4gspJbOsVfeYDvPcVqPP1GSsQlHAuV8Jo8alRHsTrQHI9q_vyBYg9MfDaVfL30J78cCiPvm4hHb-btJe-Xyv2Qu-qOXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86eaeca4c6.mp4?token=C6tb9ZWcQfNKBHRcM32CVpffe_WBDe5PpKLq3I3PnQZa5egu7WxLmvVnk1noaEDSt8-w8vT4oZ0QVCZITZeSLzC-QvcFhksYuJkp4yEgpoP8bTenACngwYi53WgoQ-FJ85bfBvFIaHHBv2FYqh0ZHReg9URbhNCSmgUvjHJkYQCM0BPYFBF1bLd8Z7C52WTlt_WOTiAcTNvosG01bbH91vYcbKwXCzZ6rkIy8iBljTa4b2Y1OclQnoZ7MLypvc1ghpj94C9QjsymT3Hnlke0BbR7TvLmtudVPKCmAuIjqRnlnCFNWLotgmGZI_xr19W9h3u3Ai1PsPJG-uypxrbs1C7EIOolRA1GEsN1mQl79liESXN5PLJG8P3mQzBg4QvkoMigPOJNXprXAyiaG2aQ7LkexymKREBhUlnwuJbWLtR2qOzu3TPEpK-QGb-cnG1vv9sD4LNAHptpvt_6sTRyIK9KYZtc7HcyPBinURRrRH0EzGhLib0mGK9nA8bGjx0GAhHnhtPqtu0_Io33hU2RWbjIrI9qv4TZ6sffqRdrWj8Amhlc5qAe0Mpt146pV-tNYM-TKNv8UQ3StUi4gspJbOsVfeYDvPcVqPP1GSsQlHAuV8Jo8alRHsTrQHI9q_vyBYg9MfDaVfL30J78cCiPvm4hHb-btJe-Xyv2Qu-qOXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
صحبت های زیبای آرتتا در تحسین پپ گواردیولا پیش از بازی امروز با سیتیزن‌ها
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103865" target="_blank">📅 12:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGgp7u27LEjo8viTaY19GsaPdoEed1VuHiRrIx7-WN4jhX5zCVCyjPc7YrA8SxoWQJPgPqMjtOdJoe3nKqf1FxWHFoVaLXnjIk1D_nMHubYKNpM47j2Cheb7bx3GjFS5cKg08QOhnWdVi4W7-1-sLFz2RetPAL6sj8vjekVyraGyRUUlke3W8kkNJKmeYeD4uA1PJGGnD91TdcmiY152DdPyqnvN6PcYXzkcdL4s3vqGTwNYYlXzl1V-jjLVNFvcvpKVVEPKtfVEivIv_4EopvbaJMraA4QccLp-3SKnbArMBHqXzvRkI2s7gu8Z6fp5jDsfPX0vKzpa9T3U015xaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
❌
ورزشگاه نقش‌جهان اصفهان به عنوان میزبان دربی رفت لیگ‌برتر انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103864" target="_blank">📅 11:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14206cca0.mp4?token=ePREXlvoAmpakuW5LZnH0Rw3zv_h8ds7-uHOzxFD02muMEhjm_9aOdLVmDkH6MhQ5Zbtte8MHOUbtkAHSCmtnM7CYFTVxDyUh8ybR9_3X-YNPjZVtVwuy6-jUcxRwWxxIEN442vwB-nKLYPlyROwKUXJuHkq_9LmFZUQAQnUeyWR6ieZRqTUX67BVuPsUd0xAbRmoft-Ig3SAzbR8HgsC-oxDMwh6rriKvpQQEn07LWAp2_d-i4XSWIJz2awNkns_ui8tPTedd9qLHSR5vwbOhO2gJYkqo5jA-ZYjIu7cWB3u0l0RNdSDygY54SZm8I9MLwrLmFzU2batN6R3GmXbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14206cca0.mp4?token=ePREXlvoAmpakuW5LZnH0Rw3zv_h8ds7-uHOzxFD02muMEhjm_9aOdLVmDkH6MhQ5Zbtte8MHOUbtkAHSCmtnM7CYFTVxDyUh8ybR9_3X-YNPjZVtVwuy6-jUcxRwWxxIEN442vwB-nKLYPlyROwKUXJuHkq_9LmFZUQAQnUeyWR6ieZRqTUX67BVuPsUd0xAbRmoft-Ig3SAzbR8HgsC-oxDMwh6rriKvpQQEn07LWAp2_d-i4XSWIJz2awNkns_ui8tPTedd9qLHSR5vwbOhO2gJYkqo5jA-ZYjIu7cWB3u0l0RNdSDygY54SZm8I9MLwrLmFzU2batN6R3GmXbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظاتی با درخشش‌های یکی از بهترین لژیونر های تاریخ فوتبال ایران اشکان‌دژاگه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103863" target="_blank">📅 11:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f9fca4e0.mp4?token=pWtkZBeHmDtzC1C5i0tptm3yTbcE6A79iG3SSbmvUSXRzgmIGUUBSgn32YuzmqENviDuewtOxCkKsO3woFZXjtGo4RF3_Ia2n50g_6EsgrZKUI0tBra0Z5LhwghcFYfFCiVy0fQXml2tz545OAcmrjIjwsJqKZCG8fVyIZwz2SjALS9MmNjiAfULMGQSI6O8dSc8EEC1ZLnNzig0jSLJMM3XzGsA88tOn8xI5-x8545kWJxdokfQA-vcwiC4JuO9n5RfgIKuUdrGGoVWkE6seTttK5p_Wzh4CQ3aS6P1vm1kqrTWn4bH4ijSho2A_fPPcrMPtMOo7BXtr3LR0taRdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f9fca4e0.mp4?token=pWtkZBeHmDtzC1C5i0tptm3yTbcE6A79iG3SSbmvUSXRzgmIGUUBSgn32YuzmqENviDuewtOxCkKsO3woFZXjtGo4RF3_Ia2n50g_6EsgrZKUI0tBra0Z5LhwghcFYfFCiVy0fQXml2tz545OAcmrjIjwsJqKZCG8fVyIZwz2SjALS9MmNjiAfULMGQSI6O8dSc8EEC1ZLnNzig0jSLJMM3XzGsA88tOn8xI5-x8545kWJxdokfQA-vcwiC4JuO9n5RfgIKuUdrGGoVWkE6seTttK5p_Wzh4CQ3aS6P1vm1kqrTWn4bH4ijSho2A_fPPcrMPtMOo7BXtr3LR0taRdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
💥
اجرای جالب و دیدنی هومن حاجی عبداللهی و آرش برهانی، با ساز و دف و تنبک و تار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103862" target="_blank">📅 11:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🇮🇷
فدراسیون فوتبال برای مشخص‌شدن پرونده فسخ قرارداد یاسر‌آسانی از فیفا استعلام گرفته و بزودی نتیجه این پرونده جنجالی مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103861" target="_blank">📅 11:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df609bdcd.mp4?token=Rhe-9VuqRRT8H6DfTro9QTdAnn2p9Yc3O2SGRiZ5sqqka-QrxxlTX8oinyR6e8X_IS_yMC_fmjyQDtQ1LFVrZElDaL0yyFyaGuC2tReaCdxcpO6vACZmSc24otyedh58fMlsZcMgIYzZUcXyujajj17bFjnbVl0nyKbBAggvviILCYwO6sHgYl350fif10n0uJV9y4RDYndO576p1Y4tlSfiO2p2uzzLDxF2t7qtkl2qPQIK2cDxrfHz-dvUKNbQL-9nL93l2tkTB31s1SlR-y3tacrX_gKCiUNF-L5ecdM0myua0H93Ey7MTERTHMciSKvzXtpIWraNgq82kqlfD0Z7Om4bI-A88FM1vUXu2bG845VX589P3PGoDV-lQIf2U5iagk0Dy2aAHCnagxGXokzfIVQo8ld8xVRhV_wolO29JQsQw75fepPG-2m7Qg6S8QZNMuBalt67hp9zQrppKI8vmIS9eP7b-HNP4fTqvdTZ4laYgoXdboBMYZ2e19ezaeIU22uKtk2ZplznAY8qHjNIHbMRG8hR2QXXLQXCw8lindUdKZVXWXNCcKo-Byrh2FtT8MHfSHrPDGNgxuKGLGtfv9C1eugb2x6YGqqjWAAYdgd--fYBvh0c1ydtxNxKAEya9jiMhWd6mawjWpdhO7m8YvPbBIiFmRDkkJm0dvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df609bdcd.mp4?token=Rhe-9VuqRRT8H6DfTro9QTdAnn2p9Yc3O2SGRiZ5sqqka-QrxxlTX8oinyR6e8X_IS_yMC_fmjyQDtQ1LFVrZElDaL0yyFyaGuC2tReaCdxcpO6vACZmSc24otyedh58fMlsZcMgIYzZUcXyujajj17bFjnbVl0nyKbBAggvviILCYwO6sHgYl350fif10n0uJV9y4RDYndO576p1Y4tlSfiO2p2uzzLDxF2t7qtkl2qPQIK2cDxrfHz-dvUKNbQL-9nL93l2tkTB31s1SlR-y3tacrX_gKCiUNF-L5ecdM0myua0H93Ey7MTERTHMciSKvzXtpIWraNgq82kqlfD0Z7Om4bI-A88FM1vUXu2bG845VX589P3PGoDV-lQIf2U5iagk0Dy2aAHCnagxGXokzfIVQo8ld8xVRhV_wolO29JQsQw75fepPG-2m7Qg6S8QZNMuBalt67hp9zQrppKI8vmIS9eP7b-HNP4fTqvdTZ4laYgoXdboBMYZ2e19ezaeIU22uKtk2ZplznAY8qHjNIHbMRG8hR2QXXLQXCw8lindUdKZVXWXNCcKo-Byrh2FtT8MHfSHrPDGNgxuKGLGtfv9C1eugb2x6YGqqjWAAYdgd--fYBvh0c1ydtxNxKAEya9jiMhWd6mawjWpdhO7m8YvPbBIiFmRDkkJm0dvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نبرد تاریخی دو اسطوره یونایتد و آرسنال در تقابل‌های مستقیم و خشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103860" target="_blank">📅 11:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcsr9ONg3ZG-ijS9bfejpTMFogKlrsv4nVUf-HVLN2uPNl9KDV1tyvXmiwCxgI0alR-9HmWVLfhxV2i6nyWb2VEFc1n1qbhD1riylkObOH1oYtTmL7EuEXJ_fqHtmP1_Vp9m-X-pt-ON5naLsPM6Bw3mLUBdWGphrgsLzEPY-VF5cBpQVLiJ2Y2_DRHNr6ZE3z6h5AscnuHMadHrx66IZFhKsYA6rOk6_WuZRmFKm_7L8ukmIWQi5vJ8cZo_GcUauttwL4CCZ28VgXfPvQTe8B0oND-Aq5OoIot1sIfmOGHtRHMZ6SCzKYYwfMpmkTuwTNs6AZE5tbwiyWu6MTwlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
فدراسیون فوتبال برای مشخص‌شدن پرونده فسخ قرارداد یاسر‌آسانی از فیفا استعلام گرفته و بزودی نتیجه این پرونده جنجالی مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103859" target="_blank">📅 11:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103858">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103858" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103858" target="_blank">📅 11:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac_l0fsnDbR4zDd_EzJLH7oSQGR6QCZ-_HhCA1rxtzrFzHrdmylbLRg-p8i7He6-GDOFKO1zILlMIqbPYSHxppB3KIeGbHeWnkvPB9L1tHtczAOXmwSFgW3vJVue7FDbUcK-IsaKXV8oUy2rYZY68xJu8gGD5PQ0ZLqXHDmxf3gdbShW53tltizYHCwY18f862yM-Yo58qnsIcnrJr6sZl3NBcPQHCbVwkH8dA6nTTUaGM9lQV5zwyk1ufMkYyUKUrd1YWDGJPpjDBHYIDJBtvZBAp5K6mPuPcHnjS9WK0UmN1ceYB__qOarQeblanPr07AvhLFNU0th1x_hO7iJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r25
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103857" target="_blank">📅 11:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103856">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9fcc1320.mp4?token=eWv_xtojLY2Eirc25Kqg1BiGptGIiRrxWpoOSMaRP4qsZpVDtTza5OdLAHK0FrLLcaaFzvPkumSSzed4-znFQYEBJ8S-D-m9T4y2RX8TOHsjUBa8CaAryuz0pgJhg6RSNOdBaLY2SrXoIhSj17gQvikRbusZwA6VtfutOtiAxP4cBodwjk2NCIV0B_gBe029uQp3raKh_CRFuyEW4rD3Rn3fWBfniv_j0u5ppUlG72u57h2BEKq33PoXvOR-J_m87L0ZCu2J2NszFYjiQQ4nK8d_KETKUsVTw2p2tBsd15A7Ky4YrWHwyyJ-zryTb4cEMgvaY2IIkEAUxEnVdo4-VWXIn13iTBaJ3wsd1qsnR2Je4_441UdqZbwzGiVPgvzIYSU8gAHTRIUUZbLDdFBPxjwxD6-1LKUaLd9XBAT6kJr5U00nNCwKpBdsIFABRI4LBoa55OOext2ichsjRCg_Gkq_FVJJgOQs256zW8W3myfZkzJlGqRV3Y2dUMtlT40Smwd6_J1YFuM_LyE-3_uKm9DOlaebIoEaksYDniKXZyhatqvLl9AbrXPVS31BSm01JAMCngswSN8Bq6HoGK3j7GcLxM5ti4y5vjhq7v9TOUub7jP0V5SV5-m_BnrugvJvrmNgLuNqBbytmbNyEBRfO3Mity8h0XfsufRXRkczu_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9fcc1320.mp4?token=eWv_xtojLY2Eirc25Kqg1BiGptGIiRrxWpoOSMaRP4qsZpVDtTza5OdLAHK0FrLLcaaFzvPkumSSzed4-znFQYEBJ8S-D-m9T4y2RX8TOHsjUBa8CaAryuz0pgJhg6RSNOdBaLY2SrXoIhSj17gQvikRbusZwA6VtfutOtiAxP4cBodwjk2NCIV0B_gBe029uQp3raKh_CRFuyEW4rD3Rn3fWBfniv_j0u5ppUlG72u57h2BEKq33PoXvOR-J_m87L0ZCu2J2NszFYjiQQ4nK8d_KETKUsVTw2p2tBsd15A7Ky4YrWHwyyJ-zryTb4cEMgvaY2IIkEAUxEnVdo4-VWXIn13iTBaJ3wsd1qsnR2Je4_441UdqZbwzGiVPgvzIYSU8gAHTRIUUZbLDdFBPxjwxD6-1LKUaLd9XBAT6kJr5U00nNCwKpBdsIFABRI4LBoa55OOext2ichsjRCg_Gkq_FVJJgOQs256zW8W3myfZkzJlGqRV3Y2dUMtlT40Smwd6_J1YFuM_LyE-3_uKm9DOlaebIoEaksYDniKXZyhatqvLl9AbrXPVS31BSm01JAMCngswSN8Bq6HoGK3j7GcLxM5ti4y5vjhq7v9TOUub7jP0V5SV5-m_BnrugvJvrmNgLuNqBbytmbNyEBRfO3Mity8h0XfsufRXRkczu_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
این‌هم تصویر اون خانومی که پشت تلفن موقع زنگ زدن میگه "مشترک مورد نظر در دسترس نمیباشد"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103856" target="_blank">📅 10:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103855">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7e9ad548.mp4?token=fcAX0tm9uR8FqVXQufzpbTlGB6qRl75ysRIPOn_zdwpEkPBoEChip8sSmFJwS6OwHJjNlzrQsBEXVZZ-yaa8DQ2_CAM2te2hamw_tUQ1RbXFwl2oiRAmgKjgevniqa6yvcBeFMVkCejf1o6vKzb65392_yLlKqtUAxfnHMnoXcf5NKqwHCVCg_gamSG2f3xmvJYeYgh6SPCDX5O3jM1N8qpD1IQzTiPzutk0-2t9HlySESeZCr6M-C52QaW7k7CdwLmXH5M4w9xGodMfHM5dz5sflELu3HwtkRSzlxthNxSdaajbBwbh1Ub8CgQoNIecKuu3DlOlWZtG-4pngIX1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7e9ad548.mp4?token=fcAX0tm9uR8FqVXQufzpbTlGB6qRl75ysRIPOn_zdwpEkPBoEChip8sSmFJwS6OwHJjNlzrQsBEXVZZ-yaa8DQ2_CAM2te2hamw_tUQ1RbXFwl2oiRAmgKjgevniqa6yvcBeFMVkCejf1o6vKzb65392_yLlKqtUAxfnHMnoXcf5NKqwHCVCg_gamSG2f3xmvJYeYgh6SPCDX5O3jM1N8qpD1IQzTiPzutk0-2t9HlySESeZCr6M-C52QaW7k7CdwLmXH5M4w9xGodMfHM5dz5sflELu3HwtkRSzlxthNxSdaajbBwbh1Ub8CgQoNIecKuu3DlOlWZtG-4pngIX1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
🇮🇷
بالاخره مشخص نشد هیچوقت که عشق بچگی کنعانی‌زادگان استقلال بوده یا پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103855" target="_blank">📅 10:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103854">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b721594231.mp4?token=AvBwn7PXx_JICot7chWoU2UD3SP2y2aFbk2VpfNp3rjzaCb4Ep3r34an-EOjHqLNOIIp9RUsmuYcGOZ_mUAT9cxWMVDTXJyvuI5QXASV2AYkfNx4aoVlQgxWTVVWLqvoNBddzGpU9U1uAyWLxyFP1bhbInDXP6e7mGPGN3MrxqoXCSw8yHlNwQwl75psQ2---gd-amYOVbkvRsPexH9ghH0lQX3DDJYVPJVp0E1wgaBYyDtaGkL11cBmXzqtWtNI78nW--SRIQ7I4g8ARMIG1Cypwqkr_b4xUPQthHR_ykBFRHFKP1514M8sMsdCndQwwKXoJRk7EkDVvNo7McX-3WqICYWJdIpY1GMF8lP7nhhUVpwQD4xt4CnkNGozblLzl1GRQLMXkK92Bp9Cl6aSV6vbAtBD__JQ4KwqimaZX5wuyRAuRdIuJC5vw3cdjNjOL824jbc6kMtoHHe2CSx-xltt2vFKzo_G3fSsJr8LvcSPSl0bLtuIQWm4bpDdIyXLD6QLlrCW-SKLlrrpPCBOKZx7VNUa7V0k7m5QrsusRW8djZCR6aN1FOT6xCcU9Bwh0KX9UW9xMfcRRwZxl3k7rs8o0_gI3UVRG5n5jZn94XQnOMXiyDjYF0pgQU4gsL3dY4WHUPmEC7pqT0YM7yKLfxOu_rFOMD-CGcDM3EJ6qEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b721594231.mp4?token=AvBwn7PXx_JICot7chWoU2UD3SP2y2aFbk2VpfNp3rjzaCb4Ep3r34an-EOjHqLNOIIp9RUsmuYcGOZ_mUAT9cxWMVDTXJyvuI5QXASV2AYkfNx4aoVlQgxWTVVWLqvoNBddzGpU9U1uAyWLxyFP1bhbInDXP6e7mGPGN3MrxqoXCSw8yHlNwQwl75psQ2---gd-amYOVbkvRsPexH9ghH0lQX3DDJYVPJVp0E1wgaBYyDtaGkL11cBmXzqtWtNI78nW--SRIQ7I4g8ARMIG1Cypwqkr_b4xUPQthHR_ykBFRHFKP1514M8sMsdCndQwwKXoJRk7EkDVvNo7McX-3WqICYWJdIpY1GMF8lP7nhhUVpwQD4xt4CnkNGozblLzl1GRQLMXkK92Bp9Cl6aSV6vbAtBD__JQ4KwqimaZX5wuyRAuRdIuJC5vw3cdjNjOL824jbc6kMtoHHe2CSx-xltt2vFKzo_G3fSsJr8LvcSPSl0bLtuIQWm4bpDdIyXLD6QLlrCW-SKLlrrpPCBOKZx7VNUa7V0k7m5QrsusRW8djZCR6aN1FOT6xCcU9Bwh0KX9UW9xMfcRRwZxl3k7rs8o0_gI3UVRG5n5jZn94XQnOMXiyDjYF0pgQU4gsL3dY4WHUPmEC7pqT0YM7yKLfxOu_rFOMD-CGcDM3EJ6qEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
انتقاد شدید یاسر همرنگ داور بازنشسته فوتبال ایران از رفتار دیشب بیژن‌حیدری:
🔴
داور پناه تیمهای ضعیف‌تر است. با رفتارتان آنها را بی پناه‌تر نکنید. می‌دانید چرا؟ چون سالها با عملکردتان این کار را کرده‌اید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/103854" target="_blank">📅 09:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103853">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641c149f79.mp4?token=ZC_SuAby36rpaqk2-6ldRq0Qt7GA84tSUhgEhJAgmDwDBwTPY68KN6WWbH2xAxg7HjKNoBqWDfEgOraF2CHG9Aju3bFpO0R-C-s_JHud6TAPH3rkiJljXo5Zgksj-G7djIopKR0NDof4-op_kMJbyJjNy7NkRNqUbrteKYrI8bALvnakwTsTieo2qp9Z90e03PPKQzbb8QW5q4eDaSWi99T0GDQ3qeLuV4m-DH9kE1gj_N7dxNlTTazel0UkWCfcWswnpLjr8rJtvsQvjX0_I7M-doBGJN5ccvmjFIq_mm8cjGutxjE12ZKnY5w9G-u3bMsPIG8H_10zCB71-WPiqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641c149f79.mp4?token=ZC_SuAby36rpaqk2-6ldRq0Qt7GA84tSUhgEhJAgmDwDBwTPY68KN6WWbH2xAxg7HjKNoBqWDfEgOraF2CHG9Aju3bFpO0R-C-s_JHud6TAPH3rkiJljXo5Zgksj-G7djIopKR0NDof4-op_kMJbyJjNy7NkRNqUbrteKYrI8bALvnakwTsTieo2qp9Z90e03PPKQzbb8QW5q4eDaSWi99T0GDQ3qeLuV4m-DH9kE1gj_N7dxNlTTazel0UkWCfcWswnpLjr8rJtvsQvjX0_I7M-doBGJN5ccvmjFIq_mm8cjGutxjE12ZKnY5w9G-u3bMsPIG8H_10zCB71-WPiqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😳
مصاحبه منتخب‌این هفته لیگ‌برتر:
شجاع خلیل‌زاده: گلم تو جام جهانی درست بود و ترامپ با دستکاری وار اون رو مردود اعلام کرد.
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/103853" target="_blank">📅 09:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103852">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3905dabff1.mp4?token=dUYwrhb0BD55T5jrCrm1W6KfXCPWMulhLguTS2_FL0j4SCW-qSwAASpXMDHHcNwbQcjothkOEYKdMLSJ01kXpQafLG8Dfz1iGTHWd4q6tMooIe4LhIaj1TOlqWT5jdolPfj0g-7O2DPQnIaYru22appNGN-5Z8GWjFH5n86j0dYF21FWve0GmJ0dvRjvz5oZzKwb0Knd8I5tBuH5gVU5jLhCByuSK0Rq-vljcqIGKGydiFH9xHD2TKQzYVde5uSsEf5Ey9mrChyzK0KJ-DymqEW_xuFv29jsG0l_BYgpqahFWu_2ytpQriPdWSkt412HbnmUvt9peI8xWnRooRTN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3905dabff1.mp4?token=dUYwrhb0BD55T5jrCrm1W6KfXCPWMulhLguTS2_FL0j4SCW-qSwAASpXMDHHcNwbQcjothkOEYKdMLSJ01kXpQafLG8Dfz1iGTHWd4q6tMooIe4LhIaj1TOlqWT5jdolPfj0g-7O2DPQnIaYru22appNGN-5Z8GWjFH5n86j0dYF21FWve0GmJ0dvRjvz5oZzKwb0Knd8I5tBuH5gVU5jLhCByuSK0Rq-vljcqIGKGydiFH9xHD2TKQzYVde5uSsEf5Ey9mrChyzK0KJ-DymqEW_xuFv29jsG0l_BYgpqahFWu_2ytpQriPdWSkt412HbnmUvt9peI8xWnRooRTN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
خداداد عز‌یزی سرپرست تراکتور: اولین نفر با پسرم رفتیم و جانفدا ثبت نام کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/103852" target="_blank">📅 09:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103851">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba79548dd.mp4?token=IeZhvMuJ30ZRXSAWPVi9P-RHb2_dovXJcaUuWUjhs-1co9SJuUssGikI7W3DYhOkY35m4l6oZYtB9Zu3dqbmApk4txckYlBPk9CImUOwP_uqPQa76gvobsUQsNe8RKOBvkgYHLmQq0sdbI1KqeQNhJjPBzCsJjdRzSm-VMRMPrWlbgQwAZam5VZFds9JavIT478kEAPAV2vYCvKqsmJ6mzwUzKhzLp20sn50SCuQA2a-QW1JvkYHiSKmHOumDwjhy8ying_8UWwIYsL49tU3JT9FgTg6bpSeUEFsKNFOc3P3y7RxeD7PpPEYM5AfSemA76Lo-pudoCUn4sBX8nsTag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba79548dd.mp4?token=IeZhvMuJ30ZRXSAWPVi9P-RHb2_dovXJcaUuWUjhs-1co9SJuUssGikI7W3DYhOkY35m4l6oZYtB9Zu3dqbmApk4txckYlBPk9CImUOwP_uqPQa76gvobsUQsNe8RKOBvkgYHLmQq0sdbI1KqeQNhJjPBzCsJjdRzSm-VMRMPrWlbgQwAZam5VZFds9JavIT478kEAPAV2vYCvKqsmJ6mzwUzKhzLp20sn50SCuQA2a-QW1JvkYHiSKmHOumDwjhy8ying_8UWwIYsL49tU3JT9FgTg6bpSeUEFsKNFOc3P3y7RxeD7PpPEYM5AfSemA76Lo-pudoCUn4sBX8nsTag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🟣
لیونل‌مسی چند ساعت پیش بازم پنالتی خراب کرد و اینترمیامی با ۴ گل مقابل حریفش باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/103851" target="_blank">📅 08:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103850">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f77aec0f40.mp4?token=bGsyLc-9UL-fudf9c1GA4JmQtXu26BAb04Uo7WUOyHYDYP-Hb1U-bLM9gu6HoACIWL4KyVH-hKtw75wUPu_ZpfPNJNNp_OOy7V7tbvUarv5B7Pq-0vvPg7mIYPO0hYzq-uHJy0aJs-gbEcphtGr0JrwIvCyEq2wwZExIx3jAlHGdOZM6Sf2DogorarFYrhMX1Ro8F98sy2eV6mo_DzxaMD-hf_HbX4JtB2G8JCRrQqGviUtXVWfTnNQL3zaeilaQZ3qnSYE2ukGn9e4sr0PC4-Q0LBbATmBrPe8jcGLV6ivGTfzmuqvPJ47AdJeXpomgr0uQxmD59QJvcsTmuZ-XaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f77aec0f40.mp4?token=bGsyLc-9UL-fudf9c1GA4JmQtXu26BAb04Uo7WUOyHYDYP-Hb1U-bLM9gu6HoACIWL4KyVH-hKtw75wUPu_ZpfPNJNNp_OOy7V7tbvUarv5B7Pq-0vvPg7mIYPO0hYzq-uHJy0aJs-gbEcphtGr0JrwIvCyEq2wwZExIx3jAlHGdOZM6Sf2DogorarFYrhMX1Ro8F98sy2eV6mo_DzxaMD-hf_HbX4JtB2G8JCRrQqGviUtXVWfTnNQL3zaeilaQZ3qnSYE2ukGn9e4sr0PC4-Q0LBbATmBrPe8jcGLV6ivGTfzmuqvPJ47AdJeXpomgr0uQxmD59QJvcsTmuZ-XaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇮🇷
رسول باختر: آسانی دقیقا اراده فسخ داشته و همین موضوع کافی است تا قرارداد با استقلال فسخ شده باشد؛ فسخ آسانی نیازی به ثبت در فیفا و فدراسیون فوتبال و سازمان لیگ ایران ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/103850" target="_blank">📅 08:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103849">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOLZ-u02wmKNJ-mkxHUtVxRbeGj5B9P3dZGIIvsufcNth6T5pjViYZe_H1FdLBd_ykXArRx-vNd6X8j7gcuCyQF4jAsIcU0nXE7Itn2-V76WbQA4OlVSo4fxFkvUDoahHsH8FBvhCvxYhX88M6nQ-M84bJ3cff94-dnleBLBt6D9n2anDmm8BEqQoyQ6EQVk8IMnNnm_kjyu905tYerKPpqjhVTZCMt5eTHQ_VHlkHGkZpwdlDi2SDWIGTtVY5CYCrDhVxUK8C_riMu9vsgnEA5YNBrxZZESoW6brNYtIK1XNwqmu8LoOEOyWdNqxIcapEq_pceIIaINSyLM809sPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری
از رومانو:
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی موافقت اولیه خودش رو با انتقال رودری به بارسلونا اعلام کرد. سیتی نمیخواد بازیکنی مثل رودری رو به اجبار نگه داره و پیشنهاد بارسلونا تقریبا مورد موافقت قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/103849" target="_blank">📅 02:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103848">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=DulpzRUXaNydUtB4xcdwCapkVdG3gsxMeWDxyodfB1QKqhAokrJt685_Ukoig4CYbNFagghyomEn45HCP2ef8kvvAGXww_Kqbbf4m7NC1m_Id3piGxXjumiGZV2ORpB3zDg9FrxxtFEz4fvPXilciBDSv6_35qcZs63V8XOPnAHUlm-6MNdNAz99BEx_TYl5ArUUAvN_d4awN7bYhiW2HKCD58x65v51MqN9XvefZrMLrRtY13bEJOk285K_IFqD4LhI2xFMdKQ0WsHdoVbKEwdbdnNg8OdaOlPG6qa5j7Aog5yvw14TdX_fcDVED9UzSPB9WkuYQjuL6WSCsaFrz2vRuCmSEUu3FjUyv57WdNTslJOnQoeij2AOJuCV_A3ztOfTm3W0NzSoBaeEBSIjer1F_81wEYqoHfmpb_ekPAro9LBDxAX-etC-itOSgsMy0tY-pKmXaJyFdCyIfSBeiNoHqBOtAuCtpAeOdTwXw0QUL4tSfre9nEmvsigA5xjtNX9WwcyN8fGuotz-F2kEZGrtuiPcF6_VfhlnTxnjdVS-IsqSRr7Ic73MhrPvm3m8UdiapKldHqhhGDyx_a1kobrzfrSe90SLqveZCndIlxqP9QrtSR1yyCbfHsYR2nZizZi86yII52oBUFnchSBA0l2Ub91mIHRSJIPcipg-pwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4e1ff391.mp4?token=DulpzRUXaNydUtB4xcdwCapkVdG3gsxMeWDxyodfB1QKqhAokrJt685_Ukoig4CYbNFagghyomEn45HCP2ef8kvvAGXww_Kqbbf4m7NC1m_Id3piGxXjumiGZV2ORpB3zDg9FrxxtFEz4fvPXilciBDSv6_35qcZs63V8XOPnAHUlm-6MNdNAz99BEx_TYl5ArUUAvN_d4awN7bYhiW2HKCD58x65v51MqN9XvefZrMLrRtY13bEJOk285K_IFqD4LhI2xFMdKQ0WsHdoVbKEwdbdnNg8OdaOlPG6qa5j7Aog5yvw14TdX_fcDVED9UzSPB9WkuYQjuL6WSCsaFrz2vRuCmSEUu3FjUyv57WdNTslJOnQoeij2AOJuCV_A3ztOfTm3W0NzSoBaeEBSIjer1F_81wEYqoHfmpb_ekPAro9LBDxAX-etC-itOSgsMy0tY-pKmXaJyFdCyIfSBeiNoHqBOtAuCtpAeOdTwXw0QUL4tSfre9nEmvsigA5xjtNX9WwcyN8fGuotz-F2kEZGrtuiPcF6_VfhlnTxnjdVS-IsqSRr7Ic73MhrPvm3m8UdiapKldHqhhGDyx_a1kobrzfrSe90SLqveZCndIlxqP9QrtSR1yyCbfHsYR2nZizZi86yII52oBUFnchSBA0l2Ub91mIHRSJIPcipg-pwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رامین‌رضاییان یه استوری گذاشته از صحبت قدیمی مهران مدیری که گفته هرکی دست به افشاگری بزنه خائن و بیشرفه   گویا جریان درخواست نود رامین جون درسته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/103848" target="_blank">📅 01:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103847">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZKhBH4-F9tfRPIy_c9hlIS30A-BvETTas5pD9jHmG5gU6YClqt0VeTFVlAg838PhfESEMieH678NXP8d7Ko2VPIWKv0d7gUFGJBk2i5vOzd0HjQrwLvEsKN5T2sj1trIvxU6sFKwL4yvzDC8-WFQbIuI6XOWwwD4Hq6yc0YDseD9sVhJeQ5NfTp37eGllgJWDPsc-CX8AmlB7Y3lnstQbPJ0E3me6DNmzFUNoxrizDDKFSbSJexTXoblBKYob-LOfXaIhZvubvutOwLOEmUikc7iosdgT2mRXuBAgkozt8WLuERK5p9lvhy1mgGB_pPzHUNqQTCqxOshyJu-Ta6Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری
از رسانه‌های نزدیک به الهلال: اوسیمن هدف جدی شاگردان اینزاگی قرار گرفته و الهلال تمام تلاششو برای جذب این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/103847" target="_blank">📅 01:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103846">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11fbd749fe.mp4?token=bi1ya8vXqyMEsAYVYe2bAG3WzNLM5OpmufO0c2syEL7tnB3Ix9JfcjK16yaTBjNUU-6I_eLLdu40JbHeXlX_i4TJDZ1MZXPSWLmV3igZ7iMAXyLTg37QwkK5o2IndKwyY_iqG2WoVmxh6L8_zPogJRQLIzvWQEDiyYhYJq-5GVuc0kylnexH6EMiJV1x4xjo4w6ecohQZAAat9w-myAFhSb4_0Mo6lOdPPOJMj8UGIK36JkUchiYH46Sx1uP4w_Yo6ChdGTgX-3qOoICTeFqwkGv89Tuhu1bEYIKkJPEa8sdheSoiiSlJLGfkEguTcqvLBn6JeHFRja8wt17QXJxrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11fbd749fe.mp4?token=bi1ya8vXqyMEsAYVYe2bAG3WzNLM5OpmufO0c2syEL7tnB3Ix9JfcjK16yaTBjNUU-6I_eLLdu40JbHeXlX_i4TJDZ1MZXPSWLmV3igZ7iMAXyLTg37QwkK5o2IndKwyY_iqG2WoVmxh6L8_zPogJRQLIzvWQEDiyYhYJq-5GVuc0kylnexH6EMiJV1x4xjo4w6ecohQZAAat9w-myAFhSb4_0Mo6lOdPPOJMj8UGIK36JkUchiYH46Sx1uP4w_Yo6ChdGTgX-3qOoICTeFqwkGv89Tuhu1bEYIKkJPEa8sdheSoiiSlJLGfkEguTcqvLBn6JeHFRja8wt17QXJxrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚔️
درگیری حامد لک با داور در جریان مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/103846" target="_blank">📅 01:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103845">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrjDax2tL4PX4M1bOkvO-y3k8MJz98yaO40Sf94lju3eqHK4k9toHYj-291nG6Zh789uwNkKrv0tzIt0vznsNqOWfBKnaJaXuevBrYZ999WqL8OLVbv7nbNg6onU2rTITSL7_hZcmWdj1k57p1U8ooPwiCyroy7cLg8T632T-zE4FFDQYBJ0NQlhdq7Iz_2_LxzW9nR7hAofOv1Kd8GDO3a1Vh6P8z2qHOmN5TQAXqOydXNAGXk5ppBV12FYxFdabrTxgSzgWQWSERQAUGSOHus21KKb0I730-bpkggVgdRxrQGFNNaVy7Zi78kwLv22nKL7MzAGv2P5yF8WCxs2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
توئیت ترامپ در لحظات پایانی مدت‌زمان ۶۰ روزه آتش‌بس: پیروز خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/103845" target="_blank">📅 00:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103844">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxBfOZqUQkqFMKCeW1DChOXvzg16rELvyC9GS0Y8OFfHmhraRjZXbpB8X5nkkmo2pHQi3iSjiMixkcgESlHBKhHcQnnbP9p-9RQifD4-pvv62ZWqUMj9zvozRszgSKsSUaYCoYGJf1Sa_SMeecLYppZ4p9WgkBlGgdJBEZO_AJDurYy5fPAFR3qIMj6YO2JXKxDXqtrvZbjVdvb75G-d6Ve-TxQsCgh4cVJqYTMIbpsM_YPV0zdPnVoB98CEWaOZ9-dhPj8eqqQSrA3uvXg80CQbPHFIoY7nTiG4W5ABIpn4fPj31WEgxAP3-UWXllwti05vr7AAtMn6427ueinQzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جرارد رومرو:
✅
مبلغ انتقال رودری حدود ۷۰ تا ۷۵ میلیون یورو خواهد بود. در حال حاضر قرار است مراسم معارفه او روز چهارشنبه برگزار شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/103844" target="_blank">📅 00:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103843">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buLuohuPQwvD12EQIwRT18qNRv6WyHlfmM9yU-OR1u7yaQGFpgq_Uo0ujN5LRLOGGHFGRuGH2Xg_pCQmDjlwCYE0VvD_K6pH9LcnMBjWra3ew5og7D-WPygZ9FpgHZxdV4fjro66apo0nkdDwVwjLgrNAFDMQEWxJc6GI1DbykRg1I1WeRu15PZz4Smn753KUl1bdrSu5Pl6E5RNUfVuRBOA86mwriw6US13uHhQULoIWhLatSr8aLEQcsga4BEyXgXLtSUPVM2cf2PvOfEUaHaYgNZvRj6eNO05Tr5fr6RiFJR8nvjKPUpoLYml-CGUrASgGkAWQnodq4ck4wYC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🎙
پیمان حدادی: اعلام قهرمان برای فصل گذشته منطقی نیست/ می‌توانند تورنمنت 5 جانبه بگذارند که ما هم شرکت کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/103843" target="_blank">📅 00:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103842">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifdePbyHZDk_WmqzWez-miPvhCZB7HckaaP9czSMdqivBpVYzg_M7nuBE11nPciMqRW54I79MGK-1xAD4k_c5N31RO6HTBqwzAR-czrNnJLwyvW8jlznR0vpja8ElBfAxwPfHfDWQSHcfdvFDzXMk-624Kvdv7PZ8IW3x8DpZYD1X4hD4JmAi68RaRzvrmzRIutFNBa7vh09kXLAaZjYVQUThQaKaFohO3o9shUT9zed1J-ygpIIRD5nBhPrdvdHOhOKWgdIzoqeIJEYXgclB-SP2BrYFLn3M-PyRG4nAenNfYXX6cKvj_PEkZOTHRthjFOeW7qwktjWDRyuhYKAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوووووری
از لونگاری؛ مالکوم برزیلی از الهلال عربستان به الدرعیه این کشور پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/103842" target="_blank">📅 00:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103841">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMmA6h2KCXiGZtuuacepSMuhqu4sM7QE1Y1vm04L4sA9t01HWIgTxSR5GUCJP4Oo1oIjKIpvEZfbIIc6BXZVszssFZktccG8kGFLkQ3iGqE3cxVRsPZOLOgk1Sh6hIbZRF1NoMchmXD7XoKMoJSLE6R4TQmoug_wv2zcL4DPL9GbuS6i7K3qbDivJWD2Ipx3q2igzs30qIP50pz6MUVw1WvkKPRzrXIPYykt3XhmcFyehVBSP3m13TKPTbFiBUgiwlquBIK4Rvm86Zl5jO9zqlN8aWGlv4Bhlyz_mYCZFPPDkRqKthHl-atgzPRsuokKEZ9MPYqYhWIPUpKhD6Uo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🔵
#فوووووری
؛ باشگاه الهلال به صورت توافقی با ژائو کانسلو فسخ قرارداد میکنه تا این بازیکن رایگان راهی بارسلونا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/103841" target="_blank">📅 00:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103838">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
⚠️
امیر علی‌اکبری در مقابل علیخان واخایف از روسیه ناک اوت شد. واخایف با این پیروزی، کمربند قهرمانی سنگین وزن در سازمان روسی ACA را حفظ کرد.
❌
هنگام ورود علی‌اکبری به قفس، ریمیکس «ای لشکر صاحب زمان» از صادق آهنگران پخش می‌شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/103838" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103837">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3713adcda0.mp4?token=WwokIjXOoB4hpCtXqHbqYJZAuaVvGz8AcgMWkKk72LIYrfRQlPF7YxWL1LhNEx0YlxdU_SM0IRB0pe82LxaKH-d-vy1aYEbBjuP09Iepra7xRN0TcC6_B-6CmyAv7PkOoemfz3k7j65hRnEY_1C3Y16je6Xu8OKClQh5TLIxZz-qaCqLd-vH-LY_9_UH62cAZhkwx2PNGKmgvdpb0W8D6YGOP8eDT_rESVVEhtWPVcFb5nRbpEZppfBCcMnlFwNvxaJwZWwtwcHU7U0JKFQQq8zcjA_o80GGYpRUip0DGPYXEmX50AibRE2oPRayKXJru_tkmxCyX0wEyGzZ2WoJikvC5QWUgz6uvlIT8_DWmca23nLvPZtZmmK6ESLmBH6kcw1HDT9z8FivQI8dcpRf4v64FE2pgl5dCbI0iT2wyawBPsRodUBxN84g7yxaB7C_gHuvA8xbxZiMHLh0bQ6aiwTebVplQIhJVU-vB0matgcjS8AKNktOkh2muOA25vzpF-vdEqWyNByR6gdh1UrBP26KA8x59aCPQBigT6VU9MVekYMnWuR_1RTrdIQl6MFHWycctTOCeZCWwomN9wr9wQdXnbe0nKxW3Ym_0S9bxSgQkEYW_4_Wb6Hnug4BoLIWZBxvbIM9uT26PSy0iYV7E23Uc3UMdScIUhP9CX_nZRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3713adcda0.mp4?token=WwokIjXOoB4hpCtXqHbqYJZAuaVvGz8AcgMWkKk72LIYrfRQlPF7YxWL1LhNEx0YlxdU_SM0IRB0pe82LxaKH-d-vy1aYEbBjuP09Iepra7xRN0TcC6_B-6CmyAv7PkOoemfz3k7j65hRnEY_1C3Y16je6Xu8OKClQh5TLIxZz-qaCqLd-vH-LY_9_UH62cAZhkwx2PNGKmgvdpb0W8D6YGOP8eDT_rESVVEhtWPVcFb5nRbpEZppfBCcMnlFwNvxaJwZWwtwcHU7U0JKFQQq8zcjA_o80GGYpRUip0DGPYXEmX50AibRE2oPRayKXJru_tkmxCyX0wEyGzZ2WoJikvC5QWUgz6uvlIT8_DWmca23nLvPZtZmmK6ESLmBH6kcw1HDT9z8FivQI8dcpRf4v64FE2pgl5dCbI0iT2wyawBPsRodUBxN84g7yxaB7C_gHuvA8xbxZiMHLh0bQ6aiwTebVplQIhJVU-vB0matgcjS8AKNktOkh2muOA25vzpF-vdEqWyNByR6gdh1UrBP26KA8x59aCPQBigT6VU9MVekYMnWuR_1RTrdIQl6MFHWycctTOCeZCWwomN9wr9wQdXnbe0nKxW3Ym_0S9bxSgQkEYW_4_Wb6Hnug4BoLIWZBxvbIM9uT26PSy0iYV7E23Uc3UMdScIUhP9CX_nZRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
کنعانی‌زادگان: در بازی مقابل تیم‌ملی مصر، عینک فیلمبردار را به شجاع دادم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/103837" target="_blank">📅 23:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103836">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bb9b634.mp4?token=KJSN44bvyQ82nsa7HGF-3_t_QVr56B7djNfNGVVXARbI7CFAii_zNQG_y3WYxjkQlp7ssjaIfHPwh0FAYCgXo7I3MrJu5wAA925t8eSMlmJTnzwFoUX2F6CshfXXginMKsgUuvdnsBjb5_paFOylMKFwNwY9pgEiRIt3jKHg9tzumHWXg_X4WdAEnAXEojr-oWtSx7lXs_3Olu42CEFr3ySJmO7zw6WnmsjzI1RKv9UfaysK1yCFuiX5FIxoGRTC2fse5hLaNXHB0LfSjhwYukZ5jb_9BXSEpR0AY3wbKT9a3w_rwwKlmys9ZTUw7o6LsA8i4GaCe7e1p5pHye8bPFk6YR5R9HlDDJ_iYxa5NEXRJgMZKMQ_EZIXKn1BAjPh-TpJf5pOus5vpkJAPcvcXZVq4vFS2MH4_uSLmA_MRaqBIJb0yQEvz7PQpwJMm0Ft8PKEhIrhDMrFBOl_-c7YktmPuWBQGVePVnq-MhaZiMbenhIFgeQlYTH6i0k6Nc8dKrtzdUfRZR95PbWNhg9eZCGs7xw00_RcclFi2soEvp2OpgnAvNPqTXYfgM7vi3zYkG7YrucGcd54HK0SxbN3wnUWIaFZTCIPEGTPUeihWMz4hsBSWOHSN4JSD0-LKJOkyfa86nlGIsus_KM8JeDHEMVnyy2IaIYy3W3LlYSdKO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bb9b634.mp4?token=KJSN44bvyQ82nsa7HGF-3_t_QVr56B7djNfNGVVXARbI7CFAii_zNQG_y3WYxjkQlp7ssjaIfHPwh0FAYCgXo7I3MrJu5wAA925t8eSMlmJTnzwFoUX2F6CshfXXginMKsgUuvdnsBjb5_paFOylMKFwNwY9pgEiRIt3jKHg9tzumHWXg_X4WdAEnAXEojr-oWtSx7lXs_3Olu42CEFr3ySJmO7zw6WnmsjzI1RKv9UfaysK1yCFuiX5FIxoGRTC2fse5hLaNXHB0LfSjhwYukZ5jb_9BXSEpR0AY3wbKT9a3w_rwwKlmys9ZTUw7o6LsA8i4GaCe7e1p5pHye8bPFk6YR5R9HlDDJ_iYxa5NEXRJgMZKMQ_EZIXKn1BAjPh-TpJf5pOus5vpkJAPcvcXZVq4vFS2MH4_uSLmA_MRaqBIJb0yQEvz7PQpwJMm0Ft8PKEhIrhDMrFBOl_-c7YktmPuWBQGVePVnq-MhaZiMbenhIFgeQlYTH6i0k6Nc8dKrtzdUfRZR95PbWNhg9eZCGs7xw00_RcclFi2soEvp2OpgnAvNPqTXYfgM7vi3zYkG7YrucGcd54HK0SxbN3wnUWIaFZTCIPEGTPUeihWMz4hsBSWOHSN4JSD0-LKJOkyfa86nlGIsus_KM8JeDHEMVnyy2IaIYy3W3LlYSdKO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
😆
حامد لک: مشکل داوری؟ فوتباله دیگه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/103836" target="_blank">📅 22:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103835">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3867654e00.mp4?token=uXS1PL3LfkZBG85OZfplFhidrzoRmo2VF5pSQpocqqKOTFOFgwyh9WdJf4wimeZAoIvGvzydrVbncqRHoJ5QLg6mQjVfnesiZQzTv4hZFZ9nDGidf51Y4yKG2tWFobHF5-xYePov13TL1N6xqr8KMUH7Ss9f4LHXx8iIt3f17FKKG402p7lAYZQpnROss7pnL0bFB-aOjD6NuTSvbYBUhLQLxdZQB3X-7A_Pah_iNClsp0Y4MKI0IENcr4b5nzVsjedgSyV-eL-C_Zoo2GKo7zComP6TRqglzJg7T87cUpsBduudXoYhC1pNFU4tq0sPrbhPaajqQt3d2aXxAm5Q6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3867654e00.mp4?token=uXS1PL3LfkZBG85OZfplFhidrzoRmo2VF5pSQpocqqKOTFOFgwyh9WdJf4wimeZAoIvGvzydrVbncqRHoJ5QLg6mQjVfnesiZQzTv4hZFZ9nDGidf51Y4yKG2tWFobHF5-xYePov13TL1N6xqr8KMUH7Ss9f4LHXx8iIt3f17FKKG402p7lAYZQpnROss7pnL0bFB-aOjD6NuTSvbYBUhLQLxdZQB3X-7A_Pah_iNClsp0Y4MKI0IENcr4b5nzVsjedgSyV-eL-C_Zoo2GKo7zComP6TRqglzJg7T87cUpsBduudXoYhC1pNFU4tq0sPrbhPaajqQt3d2aXxAm5Q6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
واکنش تارتار به ناراحتی اورونوف: برای من دیسیپلین بازی و تیم بودن مهم هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/103835" target="_blank">📅 22:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103834">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd00ae5ce.mp4?token=hCyn2hXJGCIzcsLv5cky1XnUABGaIfZen3HnvxCQEktVKXd-p05iH5q2yqsO5VG3wqofINfz-4o1tGaRuDl-SUJ-uPl9NNaMFZimrMSGccjhS8jNGg9nYmIuft2-uLJiQcccdnpNt8v2flSiHeg4xjTTQ2D86WZgODA0ZSF-gfDjwoK8KvxmJLXC5XFTMYkZKM_RRlwR7Qt105z_FdYGNlUJS5Yl5uOBdzTF4I6Zgd2saYQPqk-AfZ-YO0_bI3r1EVwboX1dLD5BgD7wixv8glOkJUzCdDCJa-Tnbg31egpKQngGysdaiF2IT3m6WK9Xodjyo-dGr0T5ODiZK8w7PLIEGQ5dK7bVZH7Mm9SzfaBpzv0J5GlPuqhwGgkdBb0JGDysh4VhwnnN72EBuHlIDDmexmIadk_YS19m7bC6Hb00rnYLN0yoMpuZVExSwGnK4_nKvVw4iVSfIR6r4TtruJHLaWZdiuYTBxaXUGVLmkW2k5W3b5WGWiTJzdTx69D5WFvlcr1qgDkbrn-eOpQ96saXYVk_11vxyWY7uJsZ28Lpsh8O6DHi5DoZe9pUNeHhgn_-Cxzt78VG_BOuoRd_gJhNseY7dPBHv06B1DvnH6hQNkiXtme3FHihIo_cfKR3o2Au-LCmmuHeLewDLaI9iaAz7CKiCHebCecBS634cfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd00ae5ce.mp4?token=hCyn2hXJGCIzcsLv5cky1XnUABGaIfZen3HnvxCQEktVKXd-p05iH5q2yqsO5VG3wqofINfz-4o1tGaRuDl-SUJ-uPl9NNaMFZimrMSGccjhS8jNGg9nYmIuft2-uLJiQcccdnpNt8v2flSiHeg4xjTTQ2D86WZgODA0ZSF-gfDjwoK8KvxmJLXC5XFTMYkZKM_RRlwR7Qt105z_FdYGNlUJS5Yl5uOBdzTF4I6Zgd2saYQPqk-AfZ-YO0_bI3r1EVwboX1dLD5BgD7wixv8glOkJUzCdDCJa-Tnbg31egpKQngGysdaiF2IT3m6WK9Xodjyo-dGr0T5ODiZK8w7PLIEGQ5dK7bVZH7Mm9SzfaBpzv0J5GlPuqhwGgkdBb0JGDysh4VhwnnN72EBuHlIDDmexmIadk_YS19m7bC6Hb00rnYLN0yoMpuZVExSwGnK4_nKvVw4iVSfIR6r4TtruJHLaWZdiuYTBxaXUGVLmkW2k5W3b5WGWiTJzdTx69D5WFvlcr1qgDkbrn-eOpQ96saXYVk_11vxyWY7uJsZ28Lpsh8O6DHi5DoZe9pUNeHhgn_-Cxzt78VG_BOuoRd_gJhNseY7dPBHv06B1DvnH6hQNkiXtme3FHihIo_cfKR3o2Au-LCmmuHeLewDLaI9iaAz7CKiCHebCecBS634cfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🚨
🚨
🚨
🇮🇷
نصیرزاده: اینکه فسخ برای قانونی شدن باید در فیفا یا فدراسیون فوتبال ثبت شود اشتباه و ناشی از بیسوادی است!
📝
من قبلا در باشگاه استقلال نبودم که بخواهم از این تیم حمایت کنم یا در جایگاه مخالفش اما ولی باید حرف حق را بزنم/ دوستان باید سواد حقوقی داشته باشند که در این مورد نظر بدهند/ موسسه سیلا، کارهای وکالت آسانی را انجام می‌دهد/ این موسسه به باشگاه استقلال نامه زد و گفت به علت اینکه مطالبات آسانی را پرداخت نکرده‌اید، این بازیکن جدا می‌شود/ هیچ کپی از این نامه در اختیار فیفا یا جای دیگر قرار نگرفته است و موسسه سیلا این نامه را مستقیما به باشگاه استقلال فرستاده است/ اینکه برای قانونی شدن فسخ باید فسخ در فیفا یا فدراسیون فوتبال ثبت شود نشاندهنده بیسوادی است/ فسخ یک اراده است و آسانی می توانسته فسخ کند چون مطالبات داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/103834" target="_blank">📅 22:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103833">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce26cb22e5.mp4?token=RWOX9zbRZdXkR6eu9_bqXk2jqwT7qRBOaLso23UE0tRjePuOLTJSU2ubi1yVPQHCyCvXRoM9Qt7pdsrRzQOQvbrOK0CBZiWHoiaMaPqlbYryusv9ky7MzWg9GdC-vpyC5FFvOsRm-QlZZkloljtPBFRKl-fzCLQ40AQNKNPv1BIMNz0iH-OAiYjn24JDGx-cvpIalIOAcwrT5I5oAVAJrwSoh2BLF4abNa_N96U0MXfuhKtOWUtK9UBP2UqvgmjrGCi_-MiO6eCP2FdwVzgmDPS8oUwWYCP_3gZRQG1qJaM057SKXwDjUd-2P7H2-THtk03Vkyq8pMDwGg-KLJgiZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce26cb22e5.mp4?token=RWOX9zbRZdXkR6eu9_bqXk2jqwT7qRBOaLso23UE0tRjePuOLTJSU2ubi1yVPQHCyCvXRoM9Qt7pdsrRzQOQvbrOK0CBZiWHoiaMaPqlbYryusv9ky7MzWg9GdC-vpyC5FFvOsRm-QlZZkloljtPBFRKl-fzCLQ40AQNKNPv1BIMNz0iH-OAiYjn24JDGx-cvpIalIOAcwrT5I5oAVAJrwSoh2BLF4abNa_N96U0MXfuhKtOWUtK9UBP2UqvgmjrGCi_-MiO6eCP2FdwVzgmDPS8oUwWYCP_3gZRQG1qJaM057SKXwDjUd-2P7H2-THtk03Vkyq8pMDwGg-KLJgiZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوووووری
از خبرگزاری ایسنا؛ ارونوف بدلیل ناراحتی بازی نکردن در شادی بازیکنان پرسپولیس شرکت نکرد و مستقیم راهی رختکن شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/103833" target="_blank">📅 21:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103832">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTixAY9OnfuU_oCK1Da_9yMgCIuC7_jKm2Qz9phZGn7ZUITIZWTS7InO99EPF4Aonh7xvVkBBDbdQYgMhIlfsYu_kc_xrma16EhZXkUhc7S_qNKdG8GYevLONYByAC7W-7Df9PEMyQW73ax00OMdPqRAlz42PR2Gb1Ahum6edOEBGvj-2ec24Mj10jrFU7xVcQnYJPEQPxpVKIcsHSDMHKsvO1aM8tN0EdthQRWaRgKOnYdPRMnI5NWO4HKaK1DxEuBOvv9q8XkPSMu3Yi-abWN-SIJFOmLb0R4b2TPNBRCIwui3Ehjgew5AgSOhbSiMsc2KW57CiekAXKN1EiftYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇮🇷
برنامه بازی‌های هفته‌دوم پریمیرلیگ ایران؛ روز سه‌شنبه و چهارشنبه بازی‌ها برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/103832" target="_blank">📅 21:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103831">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrWDzcI_WsKI1SFvHSfR3YQyIiAzefWgeL1fPHMTT6IjU6rk1TOuYAz-ziffWGmpve8IGsB1iZDa8bAdjDzug8i8AcRrLgUQOu__oB7qiV9a2nG7Z7uC7BtZyNOpmrK8VMtxifNLaxVNVm0zGY4JWs0EMVXrSuUcBpA7mHaA9JEMUVnHCM6t7kte3t3X8cMfQZQMMYFAFhr_PqfBV4r_63Pf8CsU1vZIePnxaBxWVu9YJvmC3pPtv6c03HGIO5ixENu9MDQUHWZZisaIOY7pOq0VbqRfAvqFoDsJBXoBLowKaRvdO-8UgeSvMjgFklpL0Nlyi5UgmH11co1cIMiOvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
#فوووووری
از لپاریسین: لیورپول میخواد پیشنهاد فوق‌العاده نجومی ۱۴۰ میلیون یورویی به پاریس برای جذب بارکولا بفرسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/103831" target="_blank">📅 21:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103830">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTzBkFXWD6aQq5W138hHBd5KlijgvABplS3KduSKyXQQ8-EhRweacEO4SQg5B9JbzBgnYnONMxTo9jfo3stWIvZEVSvW13higYK_ZwpgPOpVvSDHFgloeAF7pbssqEu7I9prcmQGoGo8MJZQg6dg5GuVgkhdMnqc-Zlg7jI-BJXvRp2JemyCvL9YWQYgwb9-czHAjAoL2aAzm6b2f05MjOYuPjNrIbEb13Vc5R8BK627Jt8dkj2wotuyYdFEYNCOL9O9ZLC0L4wj_ofpvJTVJ5ZeJNjHM5EEwMD1CBE6c8f8B46wY_qEF-ly4Zk7V4hQNkGrKZuMzBtY7PYsmSzJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید نوید محمدزاده با لباس فلسطین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/103830" target="_blank">📅 21:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103829">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsTmhAxdurBvdl7b_ldyhnfjKDVm8lErqab624owJ9Eu0qApkivab6mt56oV7BuaqzogkL8ubPGPgcAXeUlXp_gAXI-BkW_R1djTin_adY1eiN2RaRp3eYJxH41N1zthyWNWuJq5lrv1R8Iy5U-Xi0J1Z0uw-hIDvwLLgVJHeyROdLBQqwPhfyJe_IKzdeDBIF0OslES7IqJGq67hgn1qJBbPo11xqTtf_2E6vCLI46pgooxPcYk1riWtEXgjM7t32rcZq0Ce6YKD0KUD-uWUVtgHskvKKMwd1oNPahvCuCNusEfTsl64kP96mnTZ8FsxOPl6qbxYSXhK7BC8xZJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇮🇷
هفته‌اول لیگ‌برتر فوتبال ایران؛ نمایش اقتدار در قزوین؛ شاگردان تارتار با صلابت و یک نمایش درخشان سه امتیاز را کسب کردند
🇮🇷
پرسپولیس
😀
-
😏
شمس‌آذر قزوین
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/103829" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103828">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP-UDM2yFaT6ghLvQri42d76PEdN4C6dMydJaMAWXc9rBV5P53mPKlqMP5ZKEA8foeascm3ACmp4zpgsvFRfygUgo5Eui_DtBm70W8tsDbSKM-QY0-a10iS8zeIA1_HCC3ifMUrp-BuoSmM_bvytRyRRIvHuprMI1Ck6_kaGUzNGRdwL2wDDkTZn9SOIFdcZqU1WlYBPSQ3NKvgSSPSmZWmu_zAeNxnSx0MusgRChfnYPJGvv4TSyf_lYGUgN0w8q_z__RYnOYAY7Mn9rTBtpbsJwVo4T-VqHDz0WDDjne9Yrxjdn1SK-Rb_GTCw0n6w4A2xtHXE8xvbu8WRpJya6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رامین‌رضاییان یه استوری گذاشته از صحبت قدیمی مهران مدیری که گفته هرکی دست به افشاگری بزنه خائن و بیشرفه
گویا جریان درخواست نود رامین جون درسته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/103828" target="_blank">📅 21:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103827">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCMRd8-u8U1cYnHCgXItDXEiKsc5ONK-VyJyMzMJTdUHisM47zdgk5uWdTHKLgVEYyJFmh91OhR4C_pEA8FeChUtFqwZGQ--tDfH39JyCa9PB7_fZ5roollliIQVxLCl4g3T_JmW-k2mT7A-x1W-pgLbH5GUnPYibiyg-jpTOZSGwK4KmeouYsz1sdOAFOE62ku6RAJqANFhp6VT4KMCrbfuYHSDUBgougIWo3eSE32jv5f96v85w-zzqNTPO3dyRLY9DeBw8hxcwhCRmy0Qfl1S1dt51LfQ33rXNdhKOgNLVrATcou93c08b_QCxRkAAuvgwOG_QUxdwzfAM-D4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
الطلبه تحت هدایت علیرضا منصوریان در هفته اول لیگ عراق با نتیجه 2-1 مقابل تیم دیالا شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/103827" target="_blank">📅 21:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103826">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rye6VDbKby98wUsYaYfPfrAEYuWplIlOBXaBYCojuk1NUcL0xgH9XSvHPNx6iRwn-Zrqp5eKbnO-8xYvfCLcNs_FN-rWC0Xvm-0ZwCUmdJ-zsi1NcdXeB3zFiYAneCU8pANRtfyfa4Luqa5OSkSiUSsIZ_0IyTOa7YxgkDxoUEpRJHBROHKHzJBMv4qyZF3jKXApDjpBlXXbDc6z8KEGP9TAiWwbhJxF3pSrit0ipCr9W7pKGKVgyq2g0fYRWiaMNswiVNN9Wxcntzc5eBvbulXWk3qWKSOxJJxwFcpV678jTxwtNbH72g87tXGmmlTisZ2DgEy-emMlYbxZ6FQvtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از RMC:
❌
منچسترسیتی سومین پیشنهاد بارسلونا رو رد کرد. سیتی گفته فقط با ۸۰ میلیون یورو راضی به فروش رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/103826" target="_blank">📅 21:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103825">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e246017a9.mp4?token=X93r-IDGf_ogWyIuaYrkdkMpdgYYxZgJO-MYqFX62W79b0JkDYJECKkqVV4GqZ-oSnPp_roHbhLFarYG2AFInH8Keb4EiED4mgcvWCrfDLeSkpsB2f04buYgVWUdIlq4GFIQH3iBnUM5zz_d4qEemlwXstO9u6-HTWW8O2dq_J3vSN9QNQCV1yVGTgnS5pydRqrlVQri4jA5gO7t2xliDbqBqEIPU2A7-AFA_CABw-t--_vVzp7fdFYPvY0dD-Dk1oStgjDpx6O9LACaZ0LUiY_G_2gWDRz_PlGLRXaKiJxAnvdvXXEJ6K_vq5GPVUmMgBn4edoVrnTEXMvv67niSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e246017a9.mp4?token=X93r-IDGf_ogWyIuaYrkdkMpdgYYxZgJO-MYqFX62W79b0JkDYJECKkqVV4GqZ-oSnPp_roHbhLFarYG2AFInH8Keb4EiED4mgcvWCrfDLeSkpsB2f04buYgVWUdIlq4GFIQH3iBnUM5zz_d4qEemlwXstO9u6-HTWW8O2dq_J3vSN9QNQCV1yVGTgnS5pydRqrlVQri4jA5gO7t2xliDbqBqEIPU2A7-AFA_CABw-t--_vVzp7fdFYPvY0dD-Dk1oStgjDpx6O9LACaZ0LUiY_G_2gWDRz_PlGLRXaKiJxAnvdvXXEJ6K_vq5GPVUmMgBn4edoVrnTEXMvv67niSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیوی‌بیفوما بدلیل مصدومیت از زمین خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/103825" target="_blank">📅 21:10 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
