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
<img src="https://cdn5.telesco.pe/file/CBhBu_JPh70SSe_q3tj9nA8r4BprJ77OFkfgr3vpDbZcSl6K8HEMx6-hogzVkvcZP08XG1wr0qykUTSd8JqpqcaJf3wi3iM78jyFFpx6_bPp022x7Pi5YfsFCXn8XEmC7t3sU9m6S20FT425TGgGOI0uVuHHxKsEoYh-gxwnr6dLS-sACzyfpBnbIwmKE1M7tooYXnpAOvo5rfmjH5ccYKIvuEqgXJZfsNdQPT6S2UfCKXsPiKnwm6mWbR9UyqFdd6aiIqLuiLGtjjxJF0JOXBxGdNsui-iJDRnLFJU0-SEenTfOSPKryXbrP2dCsNWJBX9Vrc4YJEtHBmH_wk14qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 388K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-108059">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1507fa12f.mp4?token=ogiYx2vIMp4gJRhHnR41Jhz5_3dNlFlWFMQY3LzFzRan_rviAAktUiTycRSJxm7KOGfiP38UonEr6kEzJUiIVNj-vWNuP3HwBN6F9Dl5IkZO0RGE_yS2CID_sFiBh4Kx-eVdEd6_0hzucPyXlVKLdE9bl5kqaPSKtgYaidUXAOk3O16T_QwuzAcq2JRT62pxpjKdQpe6AoK8-4Vr4S2OZAb1FnjdoPb9TeqV7jhO2lKuzgxK-Ho3tcka1H5d7BLtLgP2Vk_bn6qUphKfPG2C8rvJIkRQjh4SBOY2ihh5ud0X_Xj9PqyRRrlcab8YqSKKeBdaH-J4VR5uhU3BTgxAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1507fa12f.mp4?token=ogiYx2vIMp4gJRhHnR41Jhz5_3dNlFlWFMQY3LzFzRan_rviAAktUiTycRSJxm7KOGfiP38UonEr6kEzJUiIVNj-vWNuP3HwBN6F9Dl5IkZO0RGE_yS2CID_sFiBh4Kx-eVdEd6_0hzucPyXlVKLdE9bl5kqaPSKtgYaidUXAOk3O16T_QwuzAcq2JRT62pxpjKdQpe6AoK8-4Vr4S2OZAb1FnjdoPb9TeqV7jhO2lKuzgxK-Ho3tcka1H5d7BLtLgP2Vk_bn6qUphKfPG2C8rvJIkRQjh4SBOY2ihh5ud0X_Xj9PqyRRrlcab8YqSKKeBdaH-J4VR5uhU3BTgxAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
محرم نویدکیا سرمربی سپاهان: هواداران و شرایط اقتصادی را درک می‌کنم و این که من به عنوان سرمربی از آن‌ها بخواهم با این قیمت دلار و گرانی به ورزشگاه‌ها بیایند خیلی جالب نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/Futball180TV/108059" target="_blank">📅 12:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108058">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e684a43eea.mp4?token=k-yyJAg2SexTA1k2XU8J0UIBxYU1mJCGx7qt49mc4QDpVXw5p5otWFpX37_WxmPJFkNoIiu9fvY5pUG76Zt-5CwA8AvXpxP-NcGBJYgEfmfiTg7bYdU5kviX0KiXJBJToPNhHtZeQZA08EZVsv4GbngDIlX-IBZBYUW31Ob-DZ3GPuG27M7QRtbfe5UEJ0P142n3D9QpafX4crpArHYyCv5IR-6k9Awz4v2C4gdOGLGvDCtw7GLKmQBRaEjoKtEO_Bb6umYh1xuEw8hFi6OdtemieqHW5MBdueq88-ABVFlZdkIOef5Ghr1bb0kF5TrigOqTej0FZisFRFX6f5qR43ZzoUXg_ncO7LbYZ_-ZWv_wwWPU7rRlLMA7Gd4ew0ux-at5b20P6THIiJWjMQnm_tFI1k7Ztu5kqBPaxOwgAXve7MnRxCpcRtqsCaLf7ApTN2DmbN8KMg-SsyuLvkNJ-rZK6b5ECiWfafa69egQphJIGo3qOAqn9SuNM0GiSoyEzbfrPQZ50AaIpsH1XOMCXibjezhlcuFba324QQ3RhKTtRjkN4wFap1QhTNKY5QjfjIZ5coeYvqUMyx7q0BQtb93SrWff4Lftp-gmqvROP6Rwf2nH264-ft2m38PkFFPwLvr5Ru6OSIHsq4sonb0oxJqKuFHynrks0bFi7oV7rtY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e684a43eea.mp4?token=k-yyJAg2SexTA1k2XU8J0UIBxYU1mJCGx7qt49mc4QDpVXw5p5otWFpX37_WxmPJFkNoIiu9fvY5pUG76Zt-5CwA8AvXpxP-NcGBJYgEfmfiTg7bYdU5kviX0KiXJBJToPNhHtZeQZA08EZVsv4GbngDIlX-IBZBYUW31Ob-DZ3GPuG27M7QRtbfe5UEJ0P142n3D9QpafX4crpArHYyCv5IR-6k9Awz4v2C4gdOGLGvDCtw7GLKmQBRaEjoKtEO_Bb6umYh1xuEw8hFi6OdtemieqHW5MBdueq88-ABVFlZdkIOef5Ghr1bb0kF5TrigOqTej0FZisFRFX6f5qR43ZzoUXg_ncO7LbYZ_-ZWv_wwWPU7rRlLMA7Gd4ew0ux-at5b20P6THIiJWjMQnm_tFI1k7Ztu5kqBPaxOwgAXve7MnRxCpcRtqsCaLf7ApTN2DmbN8KMg-SsyuLvkNJ-rZK6b5ECiWfafa69egQphJIGo3qOAqn9SuNM0GiSoyEzbfrPQZ50AaIpsH1XOMCXibjezhlcuFba324QQ3RhKTtRjkN4wFap1QhTNKY5QjfjIZ5coeYvqUMyx7q0BQtb93SrWff4Lftp-gmqvROP6Rwf2nH264-ft2m38PkFFPwLvr5Ru6OSIHsq4sonb0oxJqKuFHynrks0bFi7oV7rtY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫣
نورافشانی فوق‌العاده ورزشگاه مونومنتال آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/Futball180TV/108058" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108057">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c30835c72.mp4?token=M1BAo-oMi0F5NGTgawEXqoGAAkqBeEECHYX15qksbSvASaIHj32dSKBx-jpEgP_4XH31YMgDs3z6bptJ5DwNSTa0qStjJdiKaPUM6YLwngdIeNHDrs2OOxAnx1I99Zz_HfQjFRiSc2uslNTJNq34kUcxvMF8GzqLb9ho4AD0ENG3vwRD5p1W7XJo9AQ0HHbjr9Tl9BjzaPEiL7hAzOMKAt5RrZFiZ2sHzH4D9CsrEmu5NYU6tyQGvjgCznIhW22G2KOyP4QOOCiE9MyqVK-TWBqV5vwqlNsVQnzorCCbJNJdow-wtbLvp2So6n4v2SEH_fIEdg_aYdPKosB38KOMIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c30835c72.mp4?token=M1BAo-oMi0F5NGTgawEXqoGAAkqBeEECHYX15qksbSvASaIHj32dSKBx-jpEgP_4XH31YMgDs3z6bptJ5DwNSTa0qStjJdiKaPUM6YLwngdIeNHDrs2OOxAnx1I99Zz_HfQjFRiSc2uslNTJNq34kUcxvMF8GzqLb9ho4AD0ENG3vwRD5p1W7XJo9AQ0HHbjr9Tl9BjzaPEiL7hAzOMKAt5RrZFiZ2sHzH4D9CsrEmu5NYU6tyQGvjgCznIhW22G2KOyP4QOOCiE9MyqVK-TWBqV5vwqlNsVQnzorCCbJNJdow-wtbLvp2So6n4v2SEH_fIEdg_aYdPKosB38KOMIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🔥
🔥
پایان یک افسانه ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/Futball180TV/108057" target="_blank">📅 11:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108056">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6399207329.mp4?token=cGt81soMtqOMmA6_l8ToL6FbfvFRsU77KkXygLrYVgVgGu24RVoiUomrztZdthrXN3y_ehasXs0X2RDNiOsiVylZ_XXcHDRQdzfLdgwTw9zugrtTB_leOJgS0oS4lZ3eDEzd_FdbO5Mqv_99BNWAN_v5x7NcgY3166ZuISPXU1TfYmnufky8EysE6hu_7nGaBFgPYU82k9e4Lwq-BuiyWeppAz2hWzHy1vij-8ZgcohtcU9CtdBNiR-4H7LiCjCIY8BOWMSAUOf5Dm5nXJRUgL8jg3lv5YeMM23togY0ceSXMVvu3sLlJBYG_nV831Fe04LAILB2jxFzbEf-MkOtGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6399207329.mp4?token=cGt81soMtqOMmA6_l8ToL6FbfvFRsU77KkXygLrYVgVgGu24RVoiUomrztZdthrXN3y_ehasXs0X2RDNiOsiVylZ_XXcHDRQdzfLdgwTw9zugrtTB_leOJgS0oS4lZ3eDEzd_FdbO5Mqv_99BNWAN_v5x7NcgY3166ZuISPXU1TfYmnufky8EysE6hu_7nGaBFgPYU82k9e4Lwq-BuiyWeppAz2hWzHy1vij-8ZgcohtcU9CtdBNiR-4H7LiCjCIY8BOWMSAUOf5Dm5nXJRUgL8jg3lv5YeMM23togY0ceSXMVvu3sLlJBYG_nV831Fe04LAILB2jxFzbEf-MkOtGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
زیدان محبوب‌ترین فرد در فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/108056" target="_blank">📅 11:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108055">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37d8d2b4.mp4?token=WNdcej6VGGnaDDR4beQrIwEWx3nF4AN01FK0oDh8CX7db190LphR_1FTXAwkUNdfy2DzIGqF_T9yU_UqVaIFqiES9PPcdZ5BdSTEUzZWHQLFYIT9-FYxxKPhurMd6OvjlZSJ56Gt1i9SGs71Lq2UDLBqHIeQnkG0hHuxO9uys7S0wGUMlO5ZrlwbW7FmLPFlWazB75I9jeWx5GP7cVhM3cah6zJZ1K2XHWv2GnQAc8uVWIr7aZd5hdJHxRfik7GWgl7xbXf-WByT1m-kZg2bAfcLG2hxdPTc_rQZnLBQ7lZBx82tA2h2hfmIxH9YUUIn1EqoMjurutF2m6VaTMgUTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37d8d2b4.mp4?token=WNdcej6VGGnaDDR4beQrIwEWx3nF4AN01FK0oDh8CX7db190LphR_1FTXAwkUNdfy2DzIGqF_T9yU_UqVaIFqiES9PPcdZ5BdSTEUzZWHQLFYIT9-FYxxKPhurMd6OvjlZSJ56Gt1i9SGs71Lq2UDLBqHIeQnkG0hHuxO9uys7S0wGUMlO5ZrlwbW7FmLPFlWazB75I9jeWx5GP7cVhM3cah6zJZ1K2XHWv2GnQAc8uVWIr7aZd5hdJHxRfik7GWgl7xbXf-WByT1m-kZg2bAfcLG2hxdPTc_rQZnLBQ7lZBx82tA2h2hfmIxH9YUUIn1EqoMjurutF2m6VaTMgUTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
آقا جمشید حسابی سوژه هوش‌مصنوعی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/108055" target="_blank">📅 11:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108054">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
🙂
ماجرای لقب حمید بلان از زبان حمید مطهری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/108054" target="_blank">📅 11:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108053">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/880aca12e8.mp4?token=vaSCPqdKqqgEhCtBY5k6sz-FYRSsgyrqmXji8e0qRZAHUyk7jXdkS3ICZ_QIPij5zkrFzU68hy9De-CWQ1wEQT3fsXQundBTC7re3_WigIYN6G18Nkr0HBBqouSt6L6f3ae8aYxT1tciUKm0iw8Rmj1ExKmHyOlbx0mSbffvLelzDOeqrFrpBejS4KQPuvb6CGg3x_WjvFTLH1cL7FmJGZFmRh4xh0pSMSkVOms_AFlV5DcEbnyiJs97Vz8oZYQprBKvwatRyO9wrYmpKp-ige7YZSYokH28XuIvrn6kCwXIIEvpmsoIJW4Gr6NEKI1qKLAphhDp4CoAyMVbAwhurg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/880aca12e8.mp4?token=vaSCPqdKqqgEhCtBY5k6sz-FYRSsgyrqmXji8e0qRZAHUyk7jXdkS3ICZ_QIPij5zkrFzU68hy9De-CWQ1wEQT3fsXQundBTC7re3_WigIYN6G18Nkr0HBBqouSt6L6f3ae8aYxT1tciUKm0iw8Rmj1ExKmHyOlbx0mSbffvLelzDOeqrFrpBejS4KQPuvb6CGg3x_WjvFTLH1cL7FmJGZFmRh4xh0pSMSkVOms_AFlV5DcEbnyiJs97Vz8oZYQprBKvwatRyO9wrYmpKp-ige7YZSYokH28XuIvrn6kCwXIIEvpmsoIJW4Gr6NEKI1qKLAphhDp4CoAyMVbAwhurg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دلیل نتیجه نگرفتن تیم امیرخان مشخص شد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/Futball180TV/108053" target="_blank">📅 10:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108052">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108052" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/108052" target="_blank">📅 10:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108051">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6lEMElmMbg93uyTvwvMauwa_7f5R5NKlJn5alkaUwnShwNsT7fLTx0ZY3XoWeeBx7uUJMgHAmf8NkKTihOZvqRvZiwq8oogzuPOSLUXARJrOfqb-uBi_LJCX4Y_faQ_lw5lszhvuhtsXVvjTSOiwa_DUqAxxv31gwVVkD1Y_0VJP-kdLpOBX-tMwSkjIIqNu3V7VyYJZgQnQ_4eqk63R36s5aksuVskbKypdqtMHwWkEwnyccaUHK1VyHROXsN6Xen2BsKSawmG9GUp-SaFvbuAH0PHv1NOafPBI63YctLzQoT7exWlcbavpgaChMaM9zmZ8YpKWIZKd_x1s92WPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تراکتور
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
⚽️
تراکتور: ۳ برد، ۱ تساوی، ۱ شکست و ۶ گل زده
⚽️
استقلال: ۱ برد، ۳ تساوی، ۱ شکست و ۳ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/108051" target="_blank">📅 10:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108050">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6152c3dc5.mp4?token=S4CCplfwL5qRCfhTdSXlIsJMmQLnBsLlGDVb9lIQARA0FOWGCOLuEBhJw5-oUU18Dgrdhv5n9rjQCFH82ws7tAP-FOLr8Tf6e4bVfp4w7S_Ku25uU6w2Z4OZZBHo55dR6FGSukymwHkAYalhmVrpTl1LWtCJ1XdoLES_wVf4vYslcZqbK9zLxvLOoDq2TwqLo1T22IzlcTtTtwtd87vuHtE9vyLFSZ1HkcSJ94xwYr0QpqzGArrFvL_C4d0BmFjjXRJUPAuC8WvncgQ2NeZK22uSjBgcE_9El3GpyRW3N7S_Gl152z7vKJ9KozLr4vH4k8VW1PPyWAGN1NOxb_lqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6152c3dc5.mp4?token=S4CCplfwL5qRCfhTdSXlIsJMmQLnBsLlGDVb9lIQARA0FOWGCOLuEBhJw5-oUU18Dgrdhv5n9rjQCFH82ws7tAP-FOLr8Tf6e4bVfp4w7S_Ku25uU6w2Z4OZZBHo55dR6FGSukymwHkAYalhmVrpTl1LWtCJ1XdoLES_wVf4vYslcZqbK9zLxvLOoDq2TwqLo1T22IzlcTtTtwtd87vuHtE9vyLFSZ1HkcSJ94xwYr0QpqzGArrFvL_C4d0BmFjjXRJUPAuC8WvncgQ2NeZK22uSjBgcE_9El3GpyRW3N7S_Gl152z7vKJ9KozLr4vH4k8VW1PPyWAGN1NOxb_lqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
استارت بهانه‌های نکونام: بازیکن نداریم…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/Futball180TV/108050" target="_blank">📅 10:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108049">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22eef45598.mp4?token=ULFbPhfMGbiuOLLdUhw9K5okidCxwbx53jOPcgk32NrrgoHTbUjxaAGtk7QT49XkMOD-SSsoOIlzATWsyjBIfdo7u94uUy90lAoGgQi4z5BwNfXJbJ_qh8YzrA-cUmEPTYS8RbwYSYINNcQoTrTQHZGRTxggPX6D-wKyi1k56FRtsUQASZT-f7hA-gJwcb_3q304VtKqmA8NYSM8oV5l8nqcpGgArJI4onxfzE1rGZGj1I9Z7Xy-U4IGqJcpyVOkea2V6s29XGW_PF8WrpqYOUcVL3oPRSADD_2qg364Ssp-l-5MMcYo_n4WWN3ObdviIpkPnhvqpL_C3CVHaIF5KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22eef45598.mp4?token=ULFbPhfMGbiuOLLdUhw9K5okidCxwbx53jOPcgk32NrrgoHTbUjxaAGtk7QT49XkMOD-SSsoOIlzATWsyjBIfdo7u94uUy90lAoGgQi4z5BwNfXJbJ_qh8YzrA-cUmEPTYS8RbwYSYINNcQoTrTQHZGRTxggPX6D-wKyi1k56FRtsUQASZT-f7hA-gJwcb_3q304VtKqmA8NYSM8oV5l8nqcpGgArJI4onxfzE1rGZGj1I9Z7Xy-U4IGqJcpyVOkea2V6s29XGW_PF8WrpqYOUcVL3oPRSADD_2qg364Ssp-l-5MMcYo_n4WWN3ObdviIpkPnhvqpL_C3CVHaIF5KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
❌
پیروز قربانی: آقای دبیر احترامت واجبه اما فوتبال ما دست فوتبالی‌ها نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/108049" target="_blank">📅 10:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108048">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5PSmWt3hnp1Rm_Q1peZ007et5odcAwzkGH42qshswqXEtu84ZXgc_AZg2tZ8sNPOJSglFmgdzRChwEEe1x9_-M9tLXfRFFBPUB7v9lK8jDYi1uSJBmYoX5Pe71bso6k73g2R2hyKyRpvKed8e5niiv8ZmwvFaTO6gQRzu90OOB2X6BeoO8KwzFziumt7aqUKowfaJLIdSAt0kYNqhBr4PjEtJhChUg52nZLlj5hr8rI5w74_xXuiu75dVUrdzC_ND54h-aLMepIf3Ty7BBTF32bevQ2YOHXsjiwiIy97KmtEQsljUmbnQdUnYVqaCAKtQNLpn3tXxBWK-ClKoIrCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🚨
‼️
بیلد المان :
⚽️
بایرن مونیخ آماده است برای جذب دنی اولمو اقدام کند. بارسلونا ارزش این هافبک را حدود ۸۰ تا ۹۰ میلیون یورو تعیین کرده است. با این حال، هنوز هیچ پیشنهاد رسمی‌ای ارائه نشده و اولمو هیچ قصدی برای ترک بارسلونا ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/108048" target="_blank">📅 10:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108047">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
🎙
افشاگری عجیب عادل فردوسی‌پور: همه از بازیکن کمیسیون می‌خواهند، حتی فدراسیون! سهم ۵۰۰ میلیاردی فدراسیون از قراردادها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/Futball180TV/108047" target="_blank">📅 09:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108046">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddf4bbda24.mp4?token=fmC9TcPF4KAffnCK5IJTn2DEL8Xb_O3REg2k5B4e_YXR0Sy0xmpf6yetj8TbQhumJpO3gQHrnofcyqxhRJdB3V1dRZiwLhkNHmqYjoBXeGWeVb5BIgODxZQt0YFZ-fWr_PzmrbzsMbcTDcnqDvoxhjnkuIg0ubw0zGmFvIWvcT-gy4K3eFlpN1Fb8k7i4SX8E6kj4ob-PhGv9ONkuKOA-9Vns0V7hrOOd1zM7SW6BTnmxQNFzLRfBmBJX8xW6CtFqCTg9gS1TpZZOtvVvaji2JLC0tKq7YR7kp3XDT4X5ZKGMkZTeoxut0h6TdKqOWWBscLip-eUxVZjxZYpYLr_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddf4bbda24.mp4?token=fmC9TcPF4KAffnCK5IJTn2DEL8Xb_O3REg2k5B4e_YXR0Sy0xmpf6yetj8TbQhumJpO3gQHrnofcyqxhRJdB3V1dRZiwLhkNHmqYjoBXeGWeVb5BIgODxZQt0YFZ-fWr_PzmrbzsMbcTDcnqDvoxhjnkuIg0ubw0zGmFvIWvcT-gy4K3eFlpN1Fb8k7i4SX8E6kj4ob-PhGv9ONkuKOA-9Vns0V7hrOOd1zM7SW6BTnmxQNFzLRfBmBJX8xW6CtFqCTg9gS1TpZZOtvVvaji2JLC0tKq7YR7kp3XDT4X5ZKGMkZTeoxut0h6TdKqOWWBscLip-eUxVZjxZYpYLr_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‼️
🇮🇷
صحبت‌های قابل تامل پیروز قربانی درباره وضعیت کشور و‌ فیلترینگ؛ از من سرمربی چه توقعی دارید؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/108046" target="_blank">📅 09:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108045">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d9f01002.mp4?token=luaOttXWocTc7rRLJ8oY5ELmGdynzryeVVjpQtni6iGpx3zA64WxJSacvR8zNvg7PTp3k1ufp299jwQm80sKAE_blyN0UQeoRmMyGHF119ZHfZ5GYpw0e3Io3nDGhqAobxbqVw1o1e3WOI21Z3OrrS4NfewDYxbDNn-q77ccS1HVKLZFqVHpv9Asv54yJSfT-FLeikbTmnikr9I2yu9yEoWFTHwoB_4HJSIVBtJbSdUt1Od9EpmfA0Kf3vhkVCEdnYrlDm2KFB1RSpWFk0we8wFtty0CYflUjQM3-rBJJZbZFfuvLtPA-XDdaugw7jacW-JfjMCCOdWflA16xbuiDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d9f01002.mp4?token=luaOttXWocTc7rRLJ8oY5ELmGdynzryeVVjpQtni6iGpx3zA64WxJSacvR8zNvg7PTp3k1ufp299jwQm80sKAE_blyN0UQeoRmMyGHF119ZHfZ5GYpw0e3Io3nDGhqAobxbqVw1o1e3WOI21Z3OrrS4NfewDYxbDNn-q77ccS1HVKLZFqVHpv9Asv54yJSfT-FLeikbTmnikr9I2yu9yEoWFTHwoB_4HJSIVBtJbSdUt1Od9EpmfA0Kf3vhkVCEdnYrlDm2KFB1RSpWFk0we8wFtty0CYflUjQM3-rBJJZbZFfuvLtPA-XDdaugw7jacW-JfjMCCOdWflA16xbuiDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
⚽️
کنایه تند روزگذشته نکونام به قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/108045" target="_blank">📅 09:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108044">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dbe528e3d.mp4?token=ZTf0KXSGFNPlE08pXBavStpAjSkwgNvL3d0rUQ9KUI0VZkyiL-kyzEgeHrg41iuo5Y0rQlfoq8msj-buoSEZ8dgeTR05K4Lve27lAv08CUwwlzTJBBCEgSpKBDpqMcDIYpgm6etsqnsAAWrngTb0K4V-ERp6nIpwPM3V9jBDT90RG0rTpW5Y4t39RJ8LNFBQ6Bze_459LQvpgMR7kzkyK4CzCZqqOn-DESNzOPza4PhxcuX85xtYAShsVxl4uoBVm6utt9-Fa6HK8eLQhHQhzU856rNyvtZ8s_HwvETjVwgpSLDFH7n93PnONfSz_cN9X90y0bTIGNKFUT6EPUFl5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dbe528e3d.mp4?token=ZTf0KXSGFNPlE08pXBavStpAjSkwgNvL3d0rUQ9KUI0VZkyiL-kyzEgeHrg41iuo5Y0rQlfoq8msj-buoSEZ8dgeTR05K4Lve27lAv08CUwwlzTJBBCEgSpKBDpqMcDIYpgm6etsqnsAAWrngTb0K4V-ERp6nIpwPM3V9jBDT90RG0rTpW5Y4t39RJ8LNFBQ6Bze_459LQvpgMR7kzkyK4CzCZqqOn-DESNzOPza4PhxcuX85xtYAShsVxl4uoBVm6utt9-Fa6HK8eLQhHQhzU856rNyvtZ8s_HwvETjVwgpSLDFH7n93PnONfSz_cN9X90y0bTIGNKFUT6EPUFl5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
واکنش تند نادر قاضی‌پور به سوال مجری درباره محمدرضا زنوزی؛ مالک تراکتور: «این همه پول از کجا آورده؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108044" target="_blank">📅 08:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108043">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108043" target="_blank">📅 01:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108042">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108042" target="_blank">📅 01:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108041">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108041" target="_blank">📅 01:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108040">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ceb61fe00.mp4?token=LLGd1hhjPgEVqmKPofqqb4QsZFAm1KZz0FyYA4zu-dd5-KeF_Cdkn1_y7zx0h8TJ-KWaYjQsbevFMQfWJuEX2PoQGQuAS927DPk9NyT3vrM-fy3S6MHwJlxI-0ouVUjWUg-xpSyeqlyNPCK7eB4JJRvWvyW42IdmmIvV4bHacaUSZX-d76Qifrxmc4Mtp0p41FqqbvpY06hLOOV5UQ0_HUvR4arU_9pP3K2eCbsj_Nwwr9J3u01R8-vLp4z85-Y-a63CKWXvyHeDzqp-Na8k2eCYUo2-JRhx-VidU6O6asSIvhg6rQHpitlqRwed0eZI71UvauhPcxpMWMzPnTLd9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ceb61fe00.mp4?token=LLGd1hhjPgEVqmKPofqqb4QsZFAm1KZz0FyYA4zu-dd5-KeF_Cdkn1_y7zx0h8TJ-KWaYjQsbevFMQfWJuEX2PoQGQuAS927DPk9NyT3vrM-fy3S6MHwJlxI-0ouVUjWUg-xpSyeqlyNPCK7eB4JJRvWvyW42IdmmIvV4bHacaUSZX-d76Qifrxmc4Mtp0p41FqqbvpY06hLOOV5UQ0_HUvR4arU_9pP3K2eCbsj_Nwwr9J3u01R8-vLp4z85-Y-a63CKWXvyHeDzqp-Na8k2eCYUo2-JRhx-VidU6O6asSIvhg6rQHpitlqRwed0eZI71UvauhPcxpMWMzPnTLd9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های تلخ امی‌مارتینز حین تماشای مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108040" target="_blank">📅 00:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108039">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">احساسی‌شدن دیشب آنتونلا‌ و فرزندان لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108039" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108038">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11ce2c532.mp4?token=SY7ZxPnzFr-M3O9BVE_MiPQa4R2mC61FEKbfJxq0LcegyxwvcWTEQXrNUlr917S-Hf_hQx0mf31iVCXK4UMqPi964jxWP_Je44orgWwomM3ZcDXgEgGpiVnaabRQrVSYCanA0-COC285uYL8aCE6eK07Y8MKZB2yycy1nhmQqL37j5JNCLzSv-vUMn4gL1ElV33vpqjF8Zm7Do-_Nwo0ws6wcc7xeuJmuPQaya2L6PGSAzHUSd4sVagwn3J88bbmY4wxnzvxEca8lS4t2KDkbpvWZ4raJvS8Y6QUvSlzjxK6iic6IRWbtjaTSDaIfA0BxNJk3V3WzZXKZm8Q4K_ucQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11ce2c532.mp4?token=SY7ZxPnzFr-M3O9BVE_MiPQa4R2mC61FEKbfJxq0LcegyxwvcWTEQXrNUlr917S-Hf_hQx0mf31iVCXK4UMqPi964jxWP_Je44orgWwomM3ZcDXgEgGpiVnaabRQrVSYCanA0-COC285uYL8aCE6eK07Y8MKZB2yycy1nhmQqL37j5JNCLzSv-vUMn4gL1ElV33vpqjF8Zm7Do-_Nwo0ws6wcc7xeuJmuPQaya2L6PGSAzHUSd4sVagwn3J88bbmY4wxnzvxEca8lS4t2KDkbpvWZ4raJvS8Y6QUvSlzjxK6iic6IRWbtjaTSDaIfA0BxNJk3V3WzZXKZm8Q4K_ucQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
میانگین نمرات لیونل‌مسی در ۲۱ سال حضور ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108038" target="_blank">📅 22:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108037">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f285b4a4ed.mp4?token=jmRZNKXr7chjGPJO23Hsl0xiTbuB1U7qmOpqxox58dVwBdDwuVmAeJerKB0DZL0uBsRdR2ireFY--CdGQ04QdNVTVhyFV5vmewQumOpNPvbxeX849BzBgm7zm9eNWQ1sF1eAbcG2penO3JMJCpmutOJL1B21gqa3bK6_g427rrqA-uIJ5I5_3xG4x2-NvNS4yXPpTYkADJAObUyngE0aGUpJR1Fj29ZRnC5WvsFOVnf3qyOFOgjLJ5Gmlhn8PZJRWhBiknOVPjYpCEI7mrxONr6bBiFSn5dTgkHwesOGLcua5TS7IlRLM_XtjEa1yT_BTOTHQJF75wwPjCjiwGXnMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f285b4a4ed.mp4?token=jmRZNKXr7chjGPJO23Hsl0xiTbuB1U7qmOpqxox58dVwBdDwuVmAeJerKB0DZL0uBsRdR2ireFY--CdGQ04QdNVTVhyFV5vmewQumOpNPvbxeX849BzBgm7zm9eNWQ1sF1eAbcG2penO3JMJCpmutOJL1B21gqa3bK6_g427rrqA-uIJ5I5_3xG4x2-NvNS4yXPpTYkADJAObUyngE0aGUpJR1Fj29ZRnC5WvsFOVnf3qyOFOgjLJ5Gmlhn8PZJRWhBiknOVPjYpCEI7mrxONr6bBiFSn5dTgkHwesOGLcua5TS7IlRLM_XtjEa1yT_BTOTHQJF75wwPjCjiwGXnMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
فریاد بازیکنان آرژانتین در اتوبوس برای اسطوره مسی فریاد می‌زنند:
🔺
‏لیونل مسی، ما می‌خواهیم برایت بخوانیم،
‏تو جاودانه هستی، درست مثل شب قطر.
🔺
‏رفتن را متوقف کن، یک بار دیگر به این موضوع فکر کن، ‏این چیزی است که همه در استادیوم مونومنتال از تو می‌خواهند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108037" target="_blank">📅 22:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108036">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa857c27d9.mp4?token=Spr1BO4ELk8kMBb8m3C7Xv2VBvQehhdFxyZtOof8WM78fLYZHfCwSBKKUFY_yfRJhvNz_9tSWWvWqgWC-RKmV3Ltln0Gb6wSPX2d8XxyqSuSG4OSCeirHcQjj7MMAg14GvXVZI3uu9zfjtWIERTfog90aLcw47ApVacCFyXzL1zwOW6VBpxlQLZcTVw0yaU9dOYDQ7ag5TDFLW4ppmN7YZDjEZoU9K4kIfkhF0rxws2tzL-QEwt5IfWmnbKWT7QH3mOzTmlaxi-WmTa0GQleqOhRbfDpWmgHktSjY7OkEj6XkYvymq69MvDViee6d3daSrMz6oI2PbrJ4CuIkeF-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa857c27d9.mp4?token=Spr1BO4ELk8kMBb8m3C7Xv2VBvQehhdFxyZtOof8WM78fLYZHfCwSBKKUFY_yfRJhvNz_9tSWWvWqgWC-RKmV3Ltln0Gb6wSPX2d8XxyqSuSG4OSCeirHcQjj7MMAg14GvXVZI3uu9zfjtWIERTfog90aLcw47ApVacCFyXzL1zwOW6VBpxlQLZcTVw0yaU9dOYDQ7ag5TDFLW4ppmN7YZDjEZoU9K4kIfkhF0rxws2tzL-QEwt5IfWmnbKWT7QH3mOzTmlaxi-WmTa0GQleqOhRbfDpWmgHktSjY7OkEj6XkYvymq69MvDViee6d3daSrMz6oI2PbrJ4CuIkeF-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوبان‌عالم وقتی راجب تیم‌ملی حرف میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108036" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108035">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOWD6_ghEz8OVLo5nwc0uZhZrz-UFGSBmAcUv7tV_NW4DUtg7Z7CuwJitrVGk0L5V3Gc_3XLq4HCfRVTtUX-fUoV6cdeJ_Ddd-rs8jLcC9GbyljCJi59tD7UZD6R5ah0Kn-AWsKx6qVQtC3MT3v-Pb_H41nJghtp8banQ0Q4b9LcWcqVNxSbfP9hVVFg0jE51gNNaNtE4Uoez69eaFih_V29KunehZE7vg8Hl_fqWWNHWRHvwmO7y-4ATLDXa2bk4BNJItDgYw1byQfQVnvuRcD_zAHRdw39kjDoshud6BK80BpRy3a5fvURyR4h4UR_Ij7qSmDXt0WzzmdlPG01oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇪🇸
کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108035" target="_blank">📅 21:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108034">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb4f97376.mp4?token=TWY_LcZcQyjlWWeiW31AhIFVrR_GJ_AMiIcnk_jGN1zAnER6auFk-C95B0KQgiHxI8ykhDZzH3iqNbXgEz5eXUc0bURaOpDZrinrqGDHLyye2GWgR9GnDZPZTCR92DDVfNjKGvqchEoSPxWZVhxwDGpFHxr0ops7yMbBnSMgX_d5OuX3lBT8E7XCpmBXhsWJIPvoVmTUIg6IHtAMNyCIc_PYCjhSR9Fm9R7imA-7NwAOmOrChZ73zzLe0hAINAbxQbItudQjgMgdbOhUlph34S6eVCzPTUqud8hJrlStYhl2PUJdgLh2-sMIZ_5UanbUyMl5gPgmpUJx-pQ3VCSYkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb4f97376.mp4?token=TWY_LcZcQyjlWWeiW31AhIFVrR_GJ_AMiIcnk_jGN1zAnER6auFk-C95B0KQgiHxI8ykhDZzH3iqNbXgEz5eXUc0bURaOpDZrinrqGDHLyye2GWgR9GnDZPZTCR92DDVfNjKGvqchEoSPxWZVhxwDGpFHxr0ops7yMbBnSMgX_d5OuX3lBT8E7XCpmBXhsWJIPvoVmTUIg6IHtAMNyCIc_PYCjhSR9Fm9R7imA-7NwAOmOrChZ73zzLe0hAINAbxQbItudQjgMgdbOhUlph34S6eVCzPTUqud8hJrlStYhl2PUJdgLh2-sMIZ_5UanbUyMl5gPgmpUJx-pQ3VCSYkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره ابدی تاریخ فوتبال
❤️
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108034" target="_blank">📅 21:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108033">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c820a58fa5.mp4?token=rgmegkVPQ2ej-9p04ggkAC84uXu19TlcWxArJ-1ih0EbnpiywUhats52Z5z4zQjKOKtuIEfboXjqmwv_S0BHVUgnnOnxcpR4oizpxts3Xltz1htxPuvIqH66ojIQxSWOZ1ztUmGqxa1HFGaOS0aWPimnKiooMuXJG7M-Kl2HHt7CYahQb7n0qIoMfITzi1JShX6Uz3PNmWvUIbJK65Pc2UEetZsFuOeOT_1eITBaYWhrV2byxQpg4CTSabSaB9cy2aej3pZM_ugMwWRbg7_Cr__lzH4lHQ5saqbXER2XrWEkf1htN9-1SzdpSjBB4pjwnzEW54bv5He2rGjfF8fGzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c820a58fa5.mp4?token=rgmegkVPQ2ej-9p04ggkAC84uXu19TlcWxArJ-1ih0EbnpiywUhats52Z5z4zQjKOKtuIEfboXjqmwv_S0BHVUgnnOnxcpR4oizpxts3Xltz1htxPuvIqH66ojIQxSWOZ1ztUmGqxa1HFGaOS0aWPimnKiooMuXJG7M-Kl2HHt7CYahQb7n0qIoMfITzi1JShX6Uz3PNmWvUIbJK65Pc2UEetZsFuOeOT_1eITBaYWhrV2byxQpg4CTSabSaB9cy2aej3pZM_ugMwWRbg7_Cr__lzH4lHQ5saqbXER2XrWEkf1htN9-1SzdpSjBB4pjwnzEW54bv5He2rGjfF8fGzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیجان آرژانتینی‌ها بعد از آخرین جمله لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108033" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108032">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de5ad43b.mp4?token=VuNHsF2-lmVcMj2aYANtXVJAH4WeP2ziEBgt2DPk8-RTHxD--WpuS-LVJ0w5UWd8AVvRDLyCjaHiEDKWjB9ZAKCcIy8Jt88bhOgzkm1-_VDwUVZD16RNJL0U_EOuP1wcwkl6Eqn9XdPigOv3JlwODZYtc4R5bwCBmBw_dC8mHeWwSJepqcwOxcjgy7vXw0JSwNJcw9-FcSeWbcZ1Szuv6Iqeto9ic53mI13ExmT_Plo572k059qkYs4cK35Reux9xlbQ5EPYjuEtpYRI7niIB-dG7hC3vGlX8kTgZ5B3M22QM2jPKMv7L4UN4C1EJw_Cofr8OlToLVc4aDb9sWn1pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de5ad43b.mp4?token=VuNHsF2-lmVcMj2aYANtXVJAH4WeP2ziEBgt2DPk8-RTHxD--WpuS-LVJ0w5UWd8AVvRDLyCjaHiEDKWjB9ZAKCcIy8Jt88bhOgzkm1-_VDwUVZD16RNJL0U_EOuP1wcwkl6Eqn9XdPigOv3JlwODZYtc4R5bwCBmBw_dC8mHeWwSJepqcwOxcjgy7vXw0JSwNJcw9-FcSeWbcZ1Szuv6Iqeto9ic53mI13ExmT_Plo572k059qkYs4cK35Reux9xlbQ5EPYjuEtpYRI7niIB-dG7hC3vGlX8kTgZ5B3M22QM2jPKMv7L4UN4C1EJw_Cofr8OlToLVc4aDb9sWn1pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🥹
لیونل اسکالونی: "اون «جذبه» یا هاله‌ای که داره. من تو تمام عمرم چنین چیزی رو تو هیچ‌کس ندیدم. اون شور و حسی که مسی ایجاد می‌کنه رو تو هیچ‌کس دیگه‌ای ندیدم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108032" target="_blank">📅 20:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108031">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603077e1bb.mp4?token=DNqgndSH6XyMET3KpCs8htkhqpt0mjN-v_Af3ssgzGYqGhwuoLQTxhydDQNjDzEF4vadOCtSPbhxX8-cl-aCKCX-1YIE7bougNMqzihc9Yitd2Dn3qYOtTvAodhO_Bwc0m1pKjqFzN8vdLLffAtsD0_ugrn4y4tKCPeP_ITAhAOWAUyHzmw1xTQmR3S34iTof8Q_yyg-4zizbKEp6La-rvbBmBifZ-sDTdmMuS8rem_momMfqhvIQmWESrsitVamKQ_nVvokdAivcYDelGWbB_g2EHuikRmxLxs2Iu0APxT30HartBurm5KghDjPc4KP0wIeOwGsN67_nSFW-HYhFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603077e1bb.mp4?token=DNqgndSH6XyMET3KpCs8htkhqpt0mjN-v_Af3ssgzGYqGhwuoLQTxhydDQNjDzEF4vadOCtSPbhxX8-cl-aCKCX-1YIE7bougNMqzihc9Yitd2Dn3qYOtTvAodhO_Bwc0m1pKjqFzN8vdLLffAtsD0_ugrn4y4tKCPeP_ITAhAOWAUyHzmw1xTQmR3S34iTof8Q_yyg-4zizbKEp6La-rvbBmBifZ-sDTdmMuS8rem_momMfqhvIQmWESrsitVamKQ_nVvokdAivcYDelGWbB_g2EHuikRmxLxs2Iu0APxT30HartBurm5KghDjPc4KP0wIeOwGsN67_nSFW-HYhFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌ویژه ابوطالب به قشر دانشجویان عزیز
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108031" target="_blank">📅 20:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108030">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98248b467.mp4?token=Up069H89FIaUN40yMqwrMAcPT44jy6Yz3C6goLuaK7uOajMGkRInIPSNvfik8WWo9wI6vBEw-Fen5IUPaN4WRYQAU-06RcZkqVOD8l-VhsJS4NLHusVpBWyW1PqChFPQPk6mfupG8QUcZVD-T_f0QBOzosu-EBSBhVu5GjnCekf6qmHOz5iqv4tE5yxEeAnu_M63ky7p0wCHQKXFcyu8TVGyjJlZMLVS3of2QXysz717Bgz-ntekfRJVtWRNmcTGts0kZLAJk3K9b7_GUC08Qk3aCE6gBCahq74AJEdrFztbKfGytuaUa9ZKl-ckREaunOcfq8gowNUkubaorLNJ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98248b467.mp4?token=Up069H89FIaUN40yMqwrMAcPT44jy6Yz3C6goLuaK7uOajMGkRInIPSNvfik8WWo9wI6vBEw-Fen5IUPaN4WRYQAU-06RcZkqVOD8l-VhsJS4NLHusVpBWyW1PqChFPQPk6mfupG8QUcZVD-T_f0QBOzosu-EBSBhVu5GjnCekf6qmHOz5iqv4tE5yxEeAnu_M63ky7p0wCHQKXFcyu8TVGyjJlZMLVS3of2QXysz717Bgz-ntekfRJVtWRNmcTGts0kZLAJk3K9b7_GUC08Qk3aCE6gBCahq74AJEdrFztbKfGytuaUa9ZKl-ckREaunOcfq8gowNUkubaorLNJ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«یه روزنامه از ۵۴ سال پیش…
تیترهاش حسابی آدمو به فکر می‌بره!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108030" target="_blank">📅 19:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108029">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmE41YSpFjO26sF25YbSmdAcvo2kMauVi9gnlKS3U8-ZgIWlHZGsLmXvaHgfAjNhkvvfigwic-bMtM2lt_pIOe-KGP4ZaZN_Q0XaxdJhOgpXKkcv4h0D8bl9AjvIawtnSTISrW6qkopmaFZLXxOP37bS86hPmXDRqiXPpGzSoWslPHnvmPimU1wLJgIPGAyae43shP37ysYJsmcYXVD5IAiF2iHTcSr3eueT74KM7bmvhulUHGOt26jxC8WXkfWos-RhGz2ZwR_asU0X7aVzqqEawGAeiyDjO05a4plDKoaaWzzQHsoNXGk5fhGrNOrFm-t7TVZRw15XirpkawtpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
تمام 126 گل ملی لیونل مسی به تفکیک هر کشور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108029" target="_blank">📅 19:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108028">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ad568bac.mp4?token=IliJ3Bx6thOUszqpSFZEL0H-gch9fWxKlYJ088e16CUUr7cbVAz_peMMXuHR2YR_MyMH_a9j2Bn491owOuj7M7x5xgTgxYFURG2A7v4nxJZ8oBmhaaZfhPM04DMZCnZ6SCpt8nWWa6IR3R7oEeDjN4rCgzAxuyrDf_ILZhnpgOX73bZZrLa99f1LTpmv9TDGvyvqFab-PAp73NdwfKP-Oma9TVSJFqRfCsGBKmETPjizjzQ5UPHtsypVA4I8jR9LtIJ6sByRyKRif_OpMW2CeoUk88E85nx734NnuFEPnp1Nbt_8K5bOLbB6ABxuCARFse5cmDvDhtQob_FFYaPrZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ad568bac.mp4?token=IliJ3Bx6thOUszqpSFZEL0H-gch9fWxKlYJ088e16CUUr7cbVAz_peMMXuHR2YR_MyMH_a9j2Bn491owOuj7M7x5xgTgxYFURG2A7v4nxJZ8oBmhaaZfhPM04DMZCnZ6SCpt8nWWa6IR3R7oEeDjN4rCgzAxuyrDf_ILZhnpgOX73bZZrLa99f1LTpmv9TDGvyvqFab-PAp73NdwfKP-Oma9TVSJFqRfCsGBKmETPjizjzQ5UPHtsypVA4I8jR9LtIJ6sByRyKRif_OpMW2CeoUk88E85nx734NnuFEPnp1Nbt_8K5bOLbB6ABxuCARFse5cmDvDhtQob_FFYaPrZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اهدای تابلو فرش به صالح‌حردانی توسط تبریزی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108028" target="_blank">📅 18:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108027">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8ce218ac.mp4?token=YzfgMJgLKevEsaXtz7mRK1a80bTPZRKU1nAtUP2OBbU5AgZesRXkCntSbCXqLLhS0-XnvUFVEG6ya9_3foDUI-nz2o_y-lOkRg0zjlhCqTLPa8lr8DYlBlLYkocw4xZpplQyQSiYjpaAJpo2L73WtKZSGwXMrSGgVqdj5muxQWzHMRauVYxC-do0jMZsWqS2JvkA7Q7DmqZN9Z6S-2471FIhvb08-z36nJ3lNgvLZLnpsA1X7fqwV9XR3m56F6P36pQWEEv6ykMX6lrd8XeuHyib22FV4C3fVZ3kM7hAPZuHpLHfWOquLpL40051cdC4dE4kJvX4lM8KW4MMurW4Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8ce218ac.mp4?token=YzfgMJgLKevEsaXtz7mRK1a80bTPZRKU1nAtUP2OBbU5AgZesRXkCntSbCXqLLhS0-XnvUFVEG6ya9_3foDUI-nz2o_y-lOkRg0zjlhCqTLPa8lr8DYlBlLYkocw4xZpplQyQSiYjpaAJpo2L73WtKZSGwXMrSGgVqdj5muxQWzHMRauVYxC-do0jMZsWqS2JvkA7Q7DmqZN9Z6S-2471FIhvb08-z36nJ3lNgvLZLnpsA1X7fqwV9XR3m56F6P36pQWEEv6ykMX6lrd8XeuHyib22FV4C3fVZ3kM7hAPZuHpLHfWOquLpL40051cdC4dE4kJvX4lM8KW4MMurW4Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
🇮🇷
استقبال گرم وصمیمی مردم تبریز از اعضای باشگاه استقلال در هنگام ورود به این شهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108027" target="_blank">📅 18:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108026">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17e60dcfb.mp4?token=A-n23ljqUVAuHkMDJ65fsADC2ylpVCb5HGiJK9fzxsTzZTqX2SD_JVx-2PJEoHyMwlsCNFSCCbxDoRiY2ZnkVjunWj96pQaQji7WMroGrfo2NFK_q-KXUjiDn55gdD1rptGHmr4VfweeJkbQ6NX-6wBXukAeOSAgfOKgEEWQZ1cfrvubAe864HR26LfSP-Z6mQIGF_bkDhtF4s9tCTbp6uPIomoTs7SJOpjqiLuVfUrVX3FSOQJrx4SpZlRj6v6R4GUXCs_B-J7k8J0XYCUZ7jHRpQj3OCCcuKdbNhL2hR5AsPgJXmCMSnadgDpfRri_HHxaEBtwXevXmZ1YO02b0JmQomKIjHW0gZizxAhA_7w_MKiMQByMTTBKrnpuJwXVM8IP_F8yMNtmVudptnxTGJ5_4AO4r8pRRguAPioHKwXgGwROAzyI4LKuvrHWhjooDpeeA56Bd5G5FjRY2ZVnxn0PFLY_PZx5oSG6w_x8EMXOVcturXw_RfRAeSqK6to2eqcQ_VLzOUvg1hD-C9DYPqDJUuE3j5WzXSwa1hSqGZhuC0GBlD95JQ4TJ952GIYOLo8LxtXfQeOVlw_FWkHieTbtT1RGoJ5zjB3zP6CdtDZDeAM9VxxTRQ_7UKo8yl72vJpBbcG2V6JhoVQIK8WpuAQ2uA0h28TtmTK6X_T3FQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17e60dcfb.mp4?token=A-n23ljqUVAuHkMDJ65fsADC2ylpVCb5HGiJK9fzxsTzZTqX2SD_JVx-2PJEoHyMwlsCNFSCCbxDoRiY2ZnkVjunWj96pQaQji7WMroGrfo2NFK_q-KXUjiDn55gdD1rptGHmr4VfweeJkbQ6NX-6wBXukAeOSAgfOKgEEWQZ1cfrvubAe864HR26LfSP-Z6mQIGF_bkDhtF4s9tCTbp6uPIomoTs7SJOpjqiLuVfUrVX3FSOQJrx4SpZlRj6v6R4GUXCs_B-J7k8J0XYCUZ7jHRpQj3OCCcuKdbNhL2hR5AsPgJXmCMSnadgDpfRri_HHxaEBtwXevXmZ1YO02b0JmQomKIjHW0gZizxAhA_7w_MKiMQByMTTBKrnpuJwXVM8IP_F8yMNtmVudptnxTGJ5_4AO4r8pRRguAPioHKwXgGwROAzyI4LKuvrHWhjooDpeeA56Bd5G5FjRY2ZVnxn0PFLY_PZx5oSG6w_x8EMXOVcturXw_RfRAeSqK6to2eqcQ_VLzOUvg1hD-C9DYPqDJUuE3j5WzXSwa1hSqGZhuC0GBlD95JQ4TJ952GIYOLo8LxtXfQeOVlw_FWkHieTbtT1RGoJ5zjB3zP6CdtDZDeAM9VxxTRQ_7UKo8yl72vJpBbcG2V6JhoVQIK8WpuAQ2uA0h28TtmTK6X_T3FQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
🎙
چرا او آقای خاص است؟⁣ وسلی اسنایدار در مصاحبه اخیر خود با ذکر یک مثال به این سوال جواب داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108026" target="_blank">📅 18:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108025">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853f3c2c34.mov?token=QE9mjS9IYEBvRnWc4_gCWEZ0hZtfiTzsOCSw0pbdFG5KTfv6U0ER2iWq2QRLkqPggnQJFlyDLXKRXAALMx2n3KqmpV5VKbvDvQHSwhK5FmCWtthzdMWP04Wt1C0PfEo5rf8CBa1cmsk6DJuDPIn03iaWrR0d2jDt2xnalOHHH1HuZGwcaR0Vx864lWJR8Fuwdq1IfwhJenjy2AR63h3-xBHHJ75klsx_zKxZunu-myLQQEjD7O3NsyXd9F7lGL3b3MGTDArQygAzwn_GP-ks4nXZkyeA2JflfExTQLmH6JRl6Q-7TN6P9MkeuYWygYFnqlIHL8TS7bb_pZXjknAC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853f3c2c34.mov?token=QE9mjS9IYEBvRnWc4_gCWEZ0hZtfiTzsOCSw0pbdFG5KTfv6U0ER2iWq2QRLkqPggnQJFlyDLXKRXAALMx2n3KqmpV5VKbvDvQHSwhK5FmCWtthzdMWP04Wt1C0PfEo5rf8CBa1cmsk6DJuDPIn03iaWrR0d2jDt2xnalOHHH1HuZGwcaR0Vx864lWJR8Fuwdq1IfwhJenjy2AR63h3-xBHHJ75klsx_zKxZunu-myLQQEjD7O3NsyXd9F7lGL3b3MGTDArQygAzwn_GP-ks4nXZkyeA2JflfExTQLmH6JRl6Q-7TN6P9MkeuYWygYFnqlIHL8TS7bb_pZXjknAC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🔴
دریاچه ارومیه پس از نخستین باران پاییزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108025" target="_blank">📅 18:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108024">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/babe4c4985.mp4?token=KxRtSRakLy1d70RnXKCjCiZKyEw0fDj3e_J92pNszf4iirV_Qvz18ASum5SICswUWSbXfnOmTff9cGV60_UFIkg8bZ30dhq2hj06nTnnryDp5LUWTdhzkNcw3MpTfA027kl_OLYHhI89QSWLIddpCJuIqRIZQuxNadbtNDlo3LRHRJtMs6pabLS4nj_QqAYwaZA9k2Qtrvm4im-XMgoIdu2y9nKqjFxdab8vZCKJhq4vLZ3fLrjKY4TCDfnARlYRX9C2jS4kjI4B8cCgzYBre5SKN0KZ2MCrkfDyFKtac9YGoAHlw5OIKe06sroDSGrQ5vm_Tp8iYHNi6EgocPfp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/babe4c4985.mp4?token=KxRtSRakLy1d70RnXKCjCiZKyEw0fDj3e_J92pNszf4iirV_Qvz18ASum5SICswUWSbXfnOmTff9cGV60_UFIkg8bZ30dhq2hj06nTnnryDp5LUWTdhzkNcw3MpTfA027kl_OLYHhI89QSWLIddpCJuIqRIZQuxNadbtNDlo3LRHRJtMs6pabLS4nj_QqAYwaZA9k2Qtrvm4im-XMgoIdu2y9nKqjFxdab8vZCKJhq4vLZ3fLrjKY4TCDfnARlYRX9C2jS4kjI4B8cCgzYBre5SKN0KZ2MCrkfDyFKtac9YGoAHlw5OIKe06sroDSGrQ5vm_Tp8iYHNi6EgocPfp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
حماسه ای دیگر از آقا جواد؛ آموزش زبان اسپانیایی با لهجه ایتالیایی‌فارسی توسط جواد خیابانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108024" target="_blank">📅 18:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108023">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ewe4a4PkkAtYLJJnNd4j5ywvujW3JRJgnsgD96tiffHndaAYUbdL1rWXT-cZEpwp7XNZVKzqo7F5XDZ0kUZdW_08e9pinafaMblVYSgTPWM4leOaY3YQhluHqL8KYGEqvpaAQCemWUo0twGk_9m7588pOdC-JStpzdp9u9Djatb6wTUSnld1fd5T5Cb1Nd7MxtMN-p80-I0jBg7ZehBIgh40vVxriwjX00-3ka4VtuOQkvbjqix3KnMpCjKdWfyS9UEmZR3U0EkZFn9KNX6-_vGF4jz5gA3IEj3gd7iOEweirYdFkQsA7qpKlFXm7yGOea9hyBcyADSxKRbZvON2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🎙
لوکا مودریچ درباره مسی:
لئو کار فوق‌العاده‌ای با تیم ملی انجام داده؛ او جام جهانی رو که می‌خواست برد و یکی از بهترین بازیکنان جهانه.
تماشای بازی او لذت‌بخش بود هرچند که هم در سطح ملی و هم در رئال مادرید، مقابل او سختی زیادی کشیدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108023" target="_blank">📅 17:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108022">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef62a4022e.mp4?token=Q3hq8vnQLCSHIg9918gtwPAUY1T8Z5As0P4n7MuKXwavskvnxybwV7bG30-JhGKCzBe0TOTT0IzUxG5MhOqK_38AfbUrVwZD8p0Y3z_KHJjSJ9mQE_IQLLpMpruYH3OyVL-3CfC5Gsumx9eYaN69GiCYYNo2FRSu7gBityu2mQ9zywcAfdVKR_nCiFWtUTAMUhyTD1KU8OGmJAoQKHo1i5DP3xUTbSJnGPOlTpdKKiscmxUndWf9RoTUwESiaC8QMk-QsmpYOIIh9AnaOWDTR6t7ZLKEC3ylLwfEsWTGvKQ7xvcdEpif9uo0e8M1diGqkDQmf2YKlWvMfM0126qiGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef62a4022e.mp4?token=Q3hq8vnQLCSHIg9918gtwPAUY1T8Z5As0P4n7MuKXwavskvnxybwV7bG30-JhGKCzBe0TOTT0IzUxG5MhOqK_38AfbUrVwZD8p0Y3z_KHJjSJ9mQE_IQLLpMpruYH3OyVL-3CfC5Gsumx9eYaN69GiCYYNo2FRSu7gBityu2mQ9zywcAfdVKR_nCiFWtUTAMUhyTD1KU8OGmJAoQKHo1i5DP3xUTbSJnGPOlTpdKKiscmxUndWf9RoTUwESiaC8QMk-QsmpYOIIh9AnaOWDTR6t7ZLKEC3ylLwfEsWTGvKQ7xvcdEpif9uo0e8M1diGqkDQmf2YKlWvMfM0126qiGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خواهر تتلو شایعه عفو او را تکذیب کرد
خواهر امیر مقصودلو در ویدیویی اعلام کرد خبر‌ ادعایی مرتبط با عفو تتلو، صحت ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108022" target="_blank">📅 17:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108021">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108021" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108021" target="_blank">📅 17:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108020">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVp2nv51IYLy6HSHqPFmvcn_jZfsAq7yHX4jqUR3B5ioGIyRzIPTgWa-rMYURh9ejDkTTDuLnNvVQXmWx7Woy2ZuWp0c2LFr2cwiZYuN7SLl1m3-YuEmh_N7mh4TNLBOEokeJAfN6Ji8yno38LmM-jIoHAxZuA5k7B9biUV4OocFsQOgvcNSQSEwanUTryxNWjlRY2cY8o0tcI1nKQYoDfc9YNP_kjsUKa_GO2mCjcnUc1who4CVaDl765120nua7hy-L8OPYF486Afbt0WZrRjp-3MFLnvpdhvpcj2tmJlss7GcMZD7OnCKBJtCNfMRBBaLU1XqA6AsSm5IjO_CTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108020" target="_blank">📅 17:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108019">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c636032d.mp4?token=ZN5jAWhUp7GE8JjcxZVUyrwjDWfyfNAjef0moBfAceEULWRspnrTY-yZcBkpGT-xBZ0Ch5gl_Exo4SfwYyO5obNR2mCdaA0BEp5eTixM9w_9LZ5V-9_MdNuCAivB_tH4eiME4Bi9sjCh-zCLVjJ0qaq5oByw0q3pBdHGQEvBa8RYoXZglEBxCa5YF8oOhR10mVW05rCHEVIr4KnPzacXpP0HquQ6GkFiceB0ikhq_Zk2rbkfzwnMZ2nVekWq_PAYcSamIoLaxfyWKLuhK-ZMF7xcQOk5lbypign6zbi9SSSTg31od0_SsU8vA8gWRR40r5Iznr9qN0FDaoCm6DuEmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c636032d.mp4?token=ZN5jAWhUp7GE8JjcxZVUyrwjDWfyfNAjef0moBfAceEULWRspnrTY-yZcBkpGT-xBZ0Ch5gl_Exo4SfwYyO5obNR2mCdaA0BEp5eTixM9w_9LZ5V-9_MdNuCAivB_tH4eiME4Bi9sjCh-zCLVjJ0qaq5oByw0q3pBdHGQEvBa8RYoXZglEBxCa5YF8oOhR10mVW05rCHEVIr4KnPzacXpP0HquQ6GkFiceB0ikhq_Zk2rbkfzwnMZ2nVekWq_PAYcSamIoLaxfyWKLuhK-ZMF7xcQOk5lbypign6zbi9SSSTg31od0_SsU8vA8gWRR40r5Iznr9qN0FDaoCm6DuEmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیگه دیره! خیلی دیر جناب ماله‌کش اعظم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108019" target="_blank">📅 17:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108018">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922b32f940.mp4?token=h-hq27uA48-S6RmC4GqZnoSSGUmsB10wdXK3Paq-mUCnyjcd9ctCo7F2tz_jivU_R4Fo1sEsco_uwRiS4I8iOu7MZkDKCoulyuAx59MXclHMIkTih9pcQGmx79P6pl9jU8G0P8R_4k7rymN9u4HAT-BJuerWkYIdHo2-QA9dsnG0S-INaFs9oXGr5vb88ULRSJDlnFtJXQ66Tk47PuZny7X4TZCs2Vj9RGHmYdgN3zTP4E7ZwFIHCJ-Zis4Ic6H6lh0raaiqaa-gCbSSpXW5-ZYatdMc819WuNI-2qZLn-F0lYhQKDk7g9Vvmd3-CKs7okWFG_xxSJmCNXal_kz2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922b32f940.mp4?token=h-hq27uA48-S6RmC4GqZnoSSGUmsB10wdXK3Paq-mUCnyjcd9ctCo7F2tz_jivU_R4Fo1sEsco_uwRiS4I8iOu7MZkDKCoulyuAx59MXclHMIkTih9pcQGmx79P6pl9jU8G0P8R_4k7rymN9u4HAT-BJuerWkYIdHo2-QA9dsnG0S-INaFs9oXGr5vb88ULRSJDlnFtJXQ66Tk47PuZny7X4TZCs2Vj9RGHmYdgN3zTP4E7ZwFIHCJ-Zis4Ic6H6lh0raaiqaa-gCbSSpXW5-ZYatdMc819WuNI-2qZLn-F0lYhQKDk7g9Vvmd3-CKs7okWFG_xxSJmCNXal_kz2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚪️
کنایه امیر ژوله به لغو بازی با گینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108018" target="_blank">📅 16:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108017">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d567817fc2.mp4?token=TCaUUheFlvr-Iu6RlIatqVw_wOvuOneWEjq2DaR5W8jV3eTUsPK9j11MYAGbId-S1qBoVS8-HxJXP3UMvzBT7Ec4iCt6xLGig2d9byq0AB57hhq1646WEyjKbEcJJJwcjGwQr0Cg8uvzKecE7lHFjogl8aMBVE40MihyHRhmTINfhc8RQRazEAVa-mLlemFjYUq5hQxXzOSZg8EsfwfbwY3GsS362UfS7MOqVRaNGPhDjggtaTFOljBX3njCH6juEe-VSwrhYKFUEQiMdgc38DQ38Blb211JTnc3m_bzVhaJwlg9YEdZGxueFC9HGHwRghkDpzVxgD2atjwmxQ2TmiaI7BsQ4vtl0ePUk52FBE90Aoq-IrOSrqemxhAPjfLERZh2JlghqkPwhcg32_a_ngaZLO5O5hOwVJY-kt2AvmWcH73qWwe7Y6-OMDB6dry1eRRsKHOSire6NoJl0ncO-vYwB6_gBxtOJaAvV0LwTKeqkLuPfMKAXtQdOHUOL5IVzWNQIUb3-JV6Ydrsf_8t9eyMrJD3XgnIqlCngOuyfNDwbx25udJlhn7bqcvdxZhxKeDtc29dkA8bsBH0x6_-cvnxvBt9BdVFyK0r9Uazft_eM3b76ZYML9wVRgL868BTZgw05afQ8o-016mYISxuZ56VALUfVs68bTmPvKs5xxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d567817fc2.mp4?token=TCaUUheFlvr-Iu6RlIatqVw_wOvuOneWEjq2DaR5W8jV3eTUsPK9j11MYAGbId-S1qBoVS8-HxJXP3UMvzBT7Ec4iCt6xLGig2d9byq0AB57hhq1646WEyjKbEcJJJwcjGwQr0Cg8uvzKecE7lHFjogl8aMBVE40MihyHRhmTINfhc8RQRazEAVa-mLlemFjYUq5hQxXzOSZg8EsfwfbwY3GsS362UfS7MOqVRaNGPhDjggtaTFOljBX3njCH6juEe-VSwrhYKFUEQiMdgc38DQ38Blb211JTnc3m_bzVhaJwlg9YEdZGxueFC9HGHwRghkDpzVxgD2atjwmxQ2TmiaI7BsQ4vtl0ePUk52FBE90Aoq-IrOSrqemxhAPjfLERZh2JlghqkPwhcg32_a_ngaZLO5O5hOwVJY-kt2AvmWcH73qWwe7Y6-OMDB6dry1eRRsKHOSire6NoJl0ncO-vYwB6_gBxtOJaAvV0LwTKeqkLuPfMKAXtQdOHUOL5IVzWNQIUb3-JV6Ydrsf_8t9eyMrJD3XgnIqlCngOuyfNDwbx25udJlhn7bqcvdxZhxKeDtc29dkA8bsBH0x6_-cvnxvBt9BdVFyK0r9Uazft_eM3b76ZYML9wVRgL868BTZgw05afQ8o-016mYISxuZ56VALUfVs68bTmPvKs5xxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇹
اینتر تحت هدایت کریستین کیبو با تاکتیک خاص خودش یکی از پرس گریزترین تیم‌های اروپاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108017" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108016">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c192951a7.mp4?token=AtzqAM1RKgD6OpUHvH_y9R3I9CUjeiq2Kqt-jquf0F_yCtjmkbA7epnJ-IXXV4EoH7R1-P7HIDExK5c1cISdelUvG9l-4GzXNtZcUQE75p9P7HWIQqJ0riY084_H5M9JBphELKQrBsC68SXZANAwjhm4WnFTePMqKhoGu8b6gpLisiLR5V71vYbqse927cLZLoGf9dvafA2kLgu7clkMreptj27YQ53b7YfcMst3Ebk9gmbIQhL-c49iq0uDK92jqmNdmuqlV_vB-g2AzHLOU6i8rRFEty6Xlpf7f2szC01z7XBIhmo9ebGXQBw22ohu28rPYBOztcnb8wDEyf_I0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c192951a7.mp4?token=AtzqAM1RKgD6OpUHvH_y9R3I9CUjeiq2Kqt-jquf0F_yCtjmkbA7epnJ-IXXV4EoH7R1-P7HIDExK5c1cISdelUvG9l-4GzXNtZcUQE75p9P7HWIQqJ0riY084_H5M9JBphELKQrBsC68SXZANAwjhm4WnFTePMqKhoGu8b6gpLisiLR5V71vYbqse927cLZLoGf9dvafA2kLgu7clkMreptj27YQ53b7YfcMst3Ebk9gmbIQhL-c49iq0uDK92jqmNdmuqlV_vB-g2AzHLOU6i8rRFEty6Xlpf7f2szC01z7XBIhmo9ebGXQBw22ohu28rPYBOztcnb8wDEyf_I0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سامسونگ از اپل گرونتر شده!
🤦🏻‍♂️
یکی هوش مصنوعی رو از مردم بگیره، رم یجوری گرون شده که شرکت تولید کنندش به خودش هم رحم نمیکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108016" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108015">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8260fe1faf.mp4?token=NSW7RA-C-_SJ5OSbTJ_6sqJfD7y4JwbhghHMlA3XjpHwIzfYj57If88hA2yjyeFCWDeY6XoVmqTJ-ovFP_ZxC8GswnJi2CqOUdH2CQNkZUJMmvVzloUaVS_ZL17corrvnGMItvYNUUOoB9jx_7GymeMSsB4kYG3BTCYUv5jeKNkXU_rOFh-AZ3cwt_ndZ2pp7zbVyYZKSwvNnilgGVau-oF0kcw_fW5AYJiEihF7zGZ11dIamStlzz9aTZaOSG-35tE-GgvWX7h9cK3F-FNBzAKlYrDs95oYQIuUX4FtX_XMPIRO8jPXyt_8gAkVJJPBHoWJOSqHCmNrOu92zPDOeFbOQDO-ZDn4ifuCPsmHm-mnN3sc27doSZePQryW7P1aBKP9KPxNwl--JF3vA1Apc3a5Aba6zu6g_pWUu_8CDKuKle_1rt_RtgzfwO1r8wytNXXYbQ0kPWHgfKYz6t8zd-f2PGwvB8__hh5hDHVExtiz_GE69LP4du7fhYozjirveOoHDoT5EE8CujJvhAdZyyfMGIiHTEoF268AN31WJhyAS3jGI4cl-3qUDWjNK4v9zMHF4lEoKhqYqARnyQ7ayOe6-tx9G0aB5mdzTtGKhx8MQwa-MNsAYL1zDmbG5U3axIb7X0ZXORq-UR07w8Y6NQP3aGwVkb3mCbIix37VWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8260fe1faf.mp4?token=NSW7RA-C-_SJ5OSbTJ_6sqJfD7y4JwbhghHMlA3XjpHwIzfYj57If88hA2yjyeFCWDeY6XoVmqTJ-ovFP_ZxC8GswnJi2CqOUdH2CQNkZUJMmvVzloUaVS_ZL17corrvnGMItvYNUUOoB9jx_7GymeMSsB4kYG3BTCYUv5jeKNkXU_rOFh-AZ3cwt_ndZ2pp7zbVyYZKSwvNnilgGVau-oF0kcw_fW5AYJiEihF7zGZ11dIamStlzz9aTZaOSG-35tE-GgvWX7h9cK3F-FNBzAKlYrDs95oYQIuUX4FtX_XMPIRO8jPXyt_8gAkVJJPBHoWJOSqHCmNrOu92zPDOeFbOQDO-ZDn4ifuCPsmHm-mnN3sc27doSZePQryW7P1aBKP9KPxNwl--JF3vA1Apc3a5Aba6zu6g_pWUu_8CDKuKle_1rt_RtgzfwO1r8wytNXXYbQ0kPWHgfKYz6t8zd-f2PGwvB8__hh5hDHVExtiz_GE69LP4du7fhYozjirveOoHDoT5EE8CujJvhAdZyyfMGIiHTEoF268AN31WJhyAS3jGI4cl-3qUDWjNK4v9zMHF4lEoKhqYqARnyQ7ayOe6-tx9G0aB5mdzTtGKhx8MQwa-MNsAYL1zDmbG5U3axIb7X0ZXORq-UR07w8Y6NQP3aGwVkb3mCbIix37VWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
نکونام: از پرسپولیس محبی و بیفوما و از استقلال آسانی و کوشکی را بگیرید، چطور می‌توانند گل بزنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108015" target="_blank">📅 15:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108014">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b905343406.mp4?token=ImrOAGjITDQP9IMFUWc3JAs8vw1v-B8MXKsrxdU1OLuJbvqbiEyebKpvGido44UPXAjUAIqorrDK_Xsds5WrdIpYlqLzGFMNnOaHMFbR5YrAG66p2zs9RU1v30HomX1UbyTbXB1ti1G_8iSzts0RT7rFB1tubo0TALTl8jwlnBJIyjv9-MT7UmYMkfsftHH3gdAjJAR7llP5F6OcBvP9ukVLQ_MsSo2gklPUG5WhyfjkRBM72VgmcwedJ_Ggm1bvyZvWCWo71RK_I7jtzG7w5SJ0kCN8MHQvhPtf10RcIOwBwhz7i_DtpV7UKIqR_jd6fFm_w3ID42FRNz6tcfA_8Yj6x2DGIlROUmJJLlFcEz6STH0y8zNQB42HFKg8PAJrGLiWwJDW0YgDtqFU-IUyjBqt8XOV0MaA3_lL6ImN78F5alfZvj4D4RcIVWQHrthl59TIUe1GXVrtHV-6RddyuS5BjsHz_q1cUHfWGtFkcodvRbdtKXhVHFjjipeUwY_FWOkkA-bjPqO9XHI1_Yq8k9vDaWdqy9Jp1On9WVR9xwocpBSpXHmcyMKTPOV6WrPuoTYs_L5EEJsMFRrzTAxbyskUc8mee-z4hVKyoJqBEOYCf-BQNV8Xzfo3UBRGEqSDFVr_qtZGKXx0lwmtdyqhijkEG97H-gmbjkoMck86jk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b905343406.mp4?token=ImrOAGjITDQP9IMFUWc3JAs8vw1v-B8MXKsrxdU1OLuJbvqbiEyebKpvGido44UPXAjUAIqorrDK_Xsds5WrdIpYlqLzGFMNnOaHMFbR5YrAG66p2zs9RU1v30HomX1UbyTbXB1ti1G_8iSzts0RT7rFB1tubo0TALTl8jwlnBJIyjv9-MT7UmYMkfsftHH3gdAjJAR7llP5F6OcBvP9ukVLQ_MsSo2gklPUG5WhyfjkRBM72VgmcwedJ_Ggm1bvyZvWCWo71RK_I7jtzG7w5SJ0kCN8MHQvhPtf10RcIOwBwhz7i_DtpV7UKIqR_jd6fFm_w3ID42FRNz6tcfA_8Yj6x2DGIlROUmJJLlFcEz6STH0y8zNQB42HFKg8PAJrGLiWwJDW0YgDtqFU-IUyjBqt8XOV0MaA3_lL6ImN78F5alfZvj4D4RcIVWQHrthl59TIUe1GXVrtHV-6RddyuS5BjsHz_q1cUHfWGtFkcodvRbdtKXhVHFjjipeUwY_FWOkkA-bjPqO9XHI1_Yq8k9vDaWdqy9Jp1On9WVR9xwocpBSpXHmcyMKTPOV6WrPuoTYs_L5EEJsMFRrzTAxbyskUc8mee-z4hVKyoJqBEOYCf-BQNV8Xzfo3UBRGEqSDFVr_qtZGKXx0lwmtdyqhijkEG97H-gmbjkoMck86jk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
و این شب دارک در ۱۴۰ ثانیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108014" target="_blank">📅 15:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108013">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79183c9751.mp4?token=gNDFQRAfsv48PFtK-sV2-3bCq9T5PU1RwM5BwrPA7nEqTpowtkvZvD0CvlNpU1s_qlj0VT40PdwFP0wA9QwO_iP67F1OUsDeF9grGczQkvZ6lJw3e7PA0YbecSuAw-JnapQS9M-0O1uHW9IHePo9LUPguFK3Oe77UZbvHVeBc5d270He6pn-VZq2-x0C2uuUQSKUhAnS76BZBtGbCoIQYD6j82aE3z7CCFJswL5Ei_vWii_8Egu5P_ZXnp02SXghfkjUjC-xBEHfFP5jTptRP7rdtE0WNUvcdS8VwAYMDMMLAMj3WGJzsCAoUMHT4_3TwlG6vwMxNZFNwziBkU6cInPvVhj3TdLr8TDLzWEFijay5XioB5F_iPrqUX6XW_YT4KhCae2yPM_zX1XAXIR_gQxiJhchMZ4aTy0CRvgH_q70WNSqUzNeacjslgPkp4Pz4AIySwuB32PE-UI4hNBkqrAu5738eoaAuyGisKYdRqTCwcGL0WM-BIrgJJAmAEqxipfU9_N5Q4KTgyRvtdfZ9exjucgmRyPhYGuAD5rVu3VxvDoz07QYtAIeOn8iBa9rA2pQ1_81flT8HjBzf6iSxmYgjIutnzQGoqekX6g8U4mY_6vefxpLqVdw_60DByT5Bqz_AMApWn9i-876XBIpnHLrJwUG0viBdcfhBitm2bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79183c9751.mp4?token=gNDFQRAfsv48PFtK-sV2-3bCq9T5PU1RwM5BwrPA7nEqTpowtkvZvD0CvlNpU1s_qlj0VT40PdwFP0wA9QwO_iP67F1OUsDeF9grGczQkvZ6lJw3e7PA0YbecSuAw-JnapQS9M-0O1uHW9IHePo9LUPguFK3Oe77UZbvHVeBc5d270He6pn-VZq2-x0C2uuUQSKUhAnS76BZBtGbCoIQYD6j82aE3z7CCFJswL5Ei_vWii_8Egu5P_ZXnp02SXghfkjUjC-xBEHfFP5jTptRP7rdtE0WNUvcdS8VwAYMDMMLAMj3WGJzsCAoUMHT4_3TwlG6vwMxNZFNwziBkU6cInPvVhj3TdLr8TDLzWEFijay5XioB5F_iPrqUX6XW_YT4KhCae2yPM_zX1XAXIR_gQxiJhchMZ4aTy0CRvgH_q70WNSqUzNeacjslgPkp4Pz4AIySwuB32PE-UI4hNBkqrAu5738eoaAuyGisKYdRqTCwcGL0WM-BIrgJJAmAEqxipfU9_N5Q4KTgyRvtdfZ9exjucgmRyPhYGuAD5rVu3VxvDoz07QYtAIeOn8iBa9rA2pQ1_81flT8HjBzf6iSxmYgjIutnzQGoqekX6g8U4mY_6vefxpLqVdw_60DByT5Bqz_AMApWn9i-876XBIpnHLrJwUG0viBdcfhBitm2bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فقط از خودگذشتگی مهدی مهدوی‌کیا رو ببینید ۵۵ تا بازی برای تیم ملی نکردم تا به جوون‌ترها بازی برسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108013" target="_blank">📅 15:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108012">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d16bdac48.mp4?token=S2gR8dMEQ4yCFg3BVvsoR5K6Nrd2iJ5w408ugB2IUuSATqcrMfjLJvEKoPZo0B4Kt6OCcOtDl8_QkEHLwLM1BKJ6mKHGDVQmCcmLR_lqn5W7bkw3WFu0_tY-94QOMAwBG4a1EJtfZU1HPI7DZjb0Bzl0JULkSOgRTHxRVnxucei3eIarLrHeHHWN3BFZciuc-P0_JCmLWaI3iybYRFzfN50mbR9wkZxX-kiy_DTfVV5HMPYRNGlqdq4KckCfscS6_OXrXZFLYjLFgDJ50pAZZPFp6pd1F0NVjoQkCwizasNhps5yOCMMqiUdK8nk4erDufo9rTstPsyBtIWd_GSWbIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d16bdac48.mp4?token=S2gR8dMEQ4yCFg3BVvsoR5K6Nrd2iJ5w408ugB2IUuSATqcrMfjLJvEKoPZo0B4Kt6OCcOtDl8_QkEHLwLM1BKJ6mKHGDVQmCcmLR_lqn5W7bkw3WFu0_tY-94QOMAwBG4a1EJtfZU1HPI7DZjb0Bzl0JULkSOgRTHxRVnxucei3eIarLrHeHHWN3BFZciuc-P0_JCmLWaI3iybYRFzfN50mbR9wkZxX-kiy_DTfVV5HMPYRNGlqdq4KckCfscS6_OXrXZFLYjLFgDJ50pAZZPFp6pd1F0NVjoQkCwizasNhps5yOCMMqiUdK8nk4erDufo9rTstPsyBtIWd_GSWbIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Goodbye, Leo…
💔
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108012" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108011">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a871b4e8.mp4?token=PI4WysotyxQy9ugjknoOsgYMo48YfJO6BSvTCdOHBE5T59zxPdIPDoYsGA3EZNLRezNtxQNCMJbptjby8SDk0KCZOA2pJPhA0FoIIltn7PkAZZA90iG3R4ZoNk5B-xskNRchzY9YVlAgx3tXzzCORRfY4ttyGVAQ6-SoodILRaZ5v7s57MZze-xbUYZFDHFf4PQXtMPkoTZaBcemMlyaN6ADo_L684bjCiXy176z06VgLabxsR1-Kg__2ytuTuTo_lhaLpWcgpJy0lTvj6C9Veug1c10xSFxUiP25LwZqpbwl59zKDHyfVsnM9hncudcnlgFwalh6GBYmDhLLf_5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a871b4e8.mp4?token=PI4WysotyxQy9ugjknoOsgYMo48YfJO6BSvTCdOHBE5T59zxPdIPDoYsGA3EZNLRezNtxQNCMJbptjby8SDk0KCZOA2pJPhA0FoIIltn7PkAZZA90iG3R4ZoNk5B-xskNRchzY9YVlAgx3tXzzCORRfY4ttyGVAQ6-SoodILRaZ5v7s57MZze-xbUYZFDHFf4PQXtMPkoTZaBcemMlyaN6ADo_L684bjCiXy176z06VgLabxsR1-Kg__2ytuTuTo_lhaLpWcgpJy0lTvj6C9Veug1c10xSFxUiP25LwZqpbwl59zKDHyfVsnM9hncudcnlgFwalh6GBYmDhLLf_5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
💔
یادگاری‌دیشب داور بازی به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108011" target="_blank">📅 14:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108010">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHwNQiMxu8UnmHeOEzhSkLeoIs4SnfRH893HAkroR6HmAAnFUYeAfFyBUw8ms2O6qGpCwjoc90cWJyQ-avD5uh-CWuUNEMyW4UT68C6K4mDCyOjHxH-2MUSNe2MuGtIBoywbrG21BNvaQ13dVNjZGkGIfLVSp5DEJTB9fTm6QLdqUgojsXQuTJoK4sg1dBHSch7GQ0u3OvX2bb8XvyXh4pq1FjGet8xV1KnCkLa5RaL33jWdRFNsKqmfyz3EWm8H0bxGbjbuv7BbKWen4mR5IpvRP3KK3uextBSgSyWHHuMx-lENxKB7Ig5vgKhDx0JOdjYTg8iDlauIwyG7iJ3cKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
هفت‌بازی اخیر پرتغال بدون حضور‌ رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108010" target="_blank">📅 13:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108009">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV9-BD-1--kSQvnhxagVv4pN-GtM4eaqB816ViAJUIvTpzrYv2q35Ywtjt1MR0QTqVzwtJjwc5e1TEmmnVJvnNSRN4dtWmBnlzYlv6pf6l5bGaYjlHD5yDu92a_XWwAd0vqs81jfjxb0vJEEvGkqsqykHOiHuAu8vdBwafr-MOcQZRv6t6T41MWDp6OS9JQZMb9RLmgyIevqEL41-V7hwpAQx6Qh3f6XdfaFa15zs964izrQspxGhWK7ADNGJRie7nbxFi4CoxBdhhU46dDMpg66cw7kZkUloLh2jXnukucm8cvhYiHwblDrJuQa8q5dcOwNf4fUBYVhv2h_0CiTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
خلاصه‌ای از بیانیه کریس رونالدو:
🔻
رونالدو تأکید کرد که مربی قبلاً با او توافق کرده بود که در یک برنامه مشخصی برای بازی‌ها شرکت کند، و بازی با نروژ در این برنامه نبود. سپس، به طور ناگهانی از او خواسته شد که برای بازی 30 دقیقه آماده شود، و در نهایت، با وجود…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108009" target="_blank">📅 13:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108008">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VySbcghllTDn2L288SdkC6AXCd5ZYNTgG1q0Vvxrj6flBmzEXdOnbhW3QR_GBpBkJslg5ngdcX1U0ObBOx4A2UI5VkkXNP_4TyOTbjyg0hIU3b3fHpNQ6LnaKwVAEaEf05EpmaXdfJUsbp9wqAXYMq0mFujuAzEPfrHIARpaSUnKefyae4yg0YxwnTpnQ47rflLRin_QwM-8AM6nPUcoRrofy5vOH4kOaZw1ikFnBOe7_aGVmuoqSaMopuM3tDyadZxq0omE3cOiWuHOV9ecDb6g3UENA4GFZtFgBS-3V4xtVnbNPSct3rFJNrppesZBjTQopux7hj2f0a-AFhzbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
🇮🇷
فرشید سمیعی مدیرعامل سابق استقلال و کارشناس حقوقی: هیچ خطری یاسر‌آسانی و استقلال را تهدید نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108008" target="_blank">📅 13:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108007">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bba5e1d5b.mp4?token=BQ6d_9dEOCmzQjEjOcPgP2rTMYBDlvKy3vwKvrN0lVZzhEr4zv-7iILtbNBoLxMN_wHNDeibb46a_RgeHjqemIZu95wyAN74S8SIXTUA4h0tbx_Ybyy0HH15ZEO1ghIc4z4iZ1ljhvGcWrLdnZvMYAApCjryqXlxc63vh7u6OgyOgIrCSO-sEEEWmncM3RpqyNiAx65h_TIu-KiOrPpQhC6PXytaxCjDyds-tguAeKiIMSD67R7gXsndplNorxUDE1mbcqyYnxu1PsXsa_7DLuvYP5RP6aYNbLe45GS8yyfmqIV81ZNyUSds7R8-5tmrBL45rKTkXF1ePhMpP9S2Zld260cpnWpO_lxQXRMSCI21C-x5yoVnsMIbZYhe7IWNauj-pd5SWGM87zknaWhxwExmmXLZtMVzp6zqXueDB_XYrZaMZ0uZbTI00vETqWGe_apdxPXL-84YVOmJYHoItI7LdLy_yhhW0nLIQJT-QQKPuseipYc1H-f03QeDPHX3_wh1h1v9wnhRgKpe1g4JuG7kR5ANfyEQXtCylKUS_UmwDM2zLA6rDNLvdSEtlosr57BVSvyFoUc0vsndxX7VgcFrE6yoUxGoG_UERGku5e33tY9x82evNLnTjR7MDktH-eY6F7_nUG0tKci3VmSObBJ-arOTbGkSdNP7Qaz9QME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bba5e1d5b.mp4?token=BQ6d_9dEOCmzQjEjOcPgP2rTMYBDlvKy3vwKvrN0lVZzhEr4zv-7iILtbNBoLxMN_wHNDeibb46a_RgeHjqemIZu95wyAN74S8SIXTUA4h0tbx_Ybyy0HH15ZEO1ghIc4z4iZ1ljhvGcWrLdnZvMYAApCjryqXlxc63vh7u6OgyOgIrCSO-sEEEWmncM3RpqyNiAx65h_TIu-KiOrPpQhC6PXytaxCjDyds-tguAeKiIMSD67R7gXsndplNorxUDE1mbcqyYnxu1PsXsa_7DLuvYP5RP6aYNbLe45GS8yyfmqIV81ZNyUSds7R8-5tmrBL45rKTkXF1ePhMpP9S2Zld260cpnWpO_lxQXRMSCI21C-x5yoVnsMIbZYhe7IWNauj-pd5SWGM87zknaWhxwExmmXLZtMVzp6zqXueDB_XYrZaMZ0uZbTI00vETqWGe_apdxPXL-84YVOmJYHoItI7LdLy_yhhW0nLIQJT-QQKPuseipYc1H-f03QeDPHX3_wh1h1v9wnhRgKpe1g4JuG7kR5ANfyEQXtCylKUS_UmwDM2zLA6rDNLvdSEtlosr57BVSvyFoUc0vsndxX7VgcFrE6yoUxGoG_UERGku5e33tY9x82evNLnTjR7MDktH-eY6F7_nUG0tKci3VmSObBJ-arOTbGkSdNP7Qaz9QME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
💥
عملکرد تماشایی دیشب لیونل‌مسی جلو‌ بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108007" target="_blank">📅 13:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108006">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbfbf7f72.mp4?token=a5QPIeYnHLH0I4D8pMc8RbI4fnisMeyfYRHvvvEjNybQRlvYbF3klZC9WpL637FAtrO1YNIB1CqfWlnve7VcuDu8FX0EC6qTevrP5K0eBnGxmjyoLof068n-sCRu3vZubD5shY8kEQsCEVBsuBglgWO1ZOH0n06BDyyKnnga4axTnLboPIyr_Eqx7ODnq0YwGgSz2fj-hz0e9VxmSeY0Vib3TpBlebgeGSzmbAT15Dgwl1oyFf-EyZxqXj2OFxEh3yHHPUBGOPZ3yIEpaJJuYX9QX1WPjwxNneXeX7fZ64OF9DUyWd1xbSgousAoYylB-eDDBYOFLYCX2lAI6YCgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbfbf7f72.mp4?token=a5QPIeYnHLH0I4D8pMc8RbI4fnisMeyfYRHvvvEjNybQRlvYbF3klZC9WpL637FAtrO1YNIB1CqfWlnve7VcuDu8FX0EC6qTevrP5K0eBnGxmjyoLof068n-sCRu3vZubD5shY8kEQsCEVBsuBglgWO1ZOH0n06BDyyKnnga4axTnLboPIyr_Eqx7ODnq0YwGgSz2fj-hz0e9VxmSeY0Vib3TpBlebgeGSzmbAT15Dgwl1oyFf-EyZxqXj2OFxEh3yHHPUBGOPZ3yIEpaJJuYX9QX1WPjwxNneXeX7fZ64OF9DUyWd1xbSgousAoYylB-eDDBYOFLYCX2lAI6YCgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
⚠️
کنایه ابوطالب‌حسینی به مصاحبه اخیر مربی تیم‌ملی: امیر خان ما رو بهمون پس بدین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108006" target="_blank">📅 12:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108005">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeEJWAhT1DecySVQ0KgSkxwmrlTBbloJT7ZiQq186sbBXXg7cQ3VseIKKtRpq4k6FdmvCTnuoprsjsSjFkzp_hi8QplVsvp92O8qXX4FDjOzBH2l9tHpETXOPGkXGJ32gOe7OVSHqydZ9YKqn0jb4XN13BypEILI366jbH-SmFBuUWdKaYB0npg5xFgxqXJ_X32yeU4yo8udrU9p-Fxu48t-pSPQgt8Y9veJKAE6gRNv5LqEu-0WMwmHSmj0HUAQf3CDW8he3Z4dnKDdxZuRYGHWSPBvPyCI38-hDUWcGZ3FDrATHDUEVtVPfA5GfljN1gtBq7uE20mMHdzG7AfITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر باشگاه استقلال برای بازی با تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108005" target="_blank">📅 12:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108004">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7e310d4f8.mp4?token=TF4ctPak10y2rUl0tL97MWl-_0JMcd4ti13IDcXrUZeVORTjcLt_B3QK-NnVpYb6wCxCUvWoZeU7Om3TGzIZOAt3TAWOEVxUdunp9-zLfNGSIU1AHewU--808IdkvFfSe7CpMcoytPDPaiQ8jymPlviOARRAcns-xZ8HVguyNwOj2d40uBzR2UaD1Crx3mhnIygSdWuEnSqnuXwYUEcaNtCHBwgxGeQMoN7nGY3D7nOdWNoFz_WpuUtF__ZHg4NFzU_iYf7H8EimOaU3C8irRHajhwMIc9mDKxdeDQfqe9F34mkggQfiFWMq9o63rhIriwOD0hvvqTKC_vLycV4vYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7e310d4f8.mp4?token=TF4ctPak10y2rUl0tL97MWl-_0JMcd4ti13IDcXrUZeVORTjcLt_B3QK-NnVpYb6wCxCUvWoZeU7Om3TGzIZOAt3TAWOEVxUdunp9-zLfNGSIU1AHewU--808IdkvFfSe7CpMcoytPDPaiQ8jymPlviOARRAcns-xZ8HVguyNwOj2d40uBzR2UaD1Crx3mhnIygSdWuEnSqnuXwYUEcaNtCHBwgxGeQMoN7nGY3D7nOdWNoFz_WpuUtF__ZHg4NFzU_iYf7H8EimOaU3C8irRHajhwMIc9mDKxdeDQfqe9F34mkggQfiFWMq9o63rhIriwOD0hvvqTKC_vLycV4vYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دبیر: اگر اسم قوه قضاییه را می‌آوردم باید می‌ترسیدید؛ خداراشکر فوتبالی‌ها دوم جهان شدن را برای کشتی شکست می‌بینند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108004" target="_blank">📅 12:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108003">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b7671e0e.mp4?token=gzU9mpgAyoZVgdP7MY6khDhYzMlnHYKFrkKHBi0pbjioqyyb2Wu3XN8MfkOnLbot60YUiABDPnf2svEchDcvkDII3-vT8nfYpxdaFPremB8oSjs8FktXbiZiPOn_EsMsh73Xz3vvintVcCm4vr1zp6T77vw2Hyr3jRJDG-RXMtdAvfxY4CRqatUGxEcYfCihzMYmKDNkPnLD5CxlW2OM2lj8kXxrbNt_gZNMye3TEbpLKUw0uaW2EEvpwt1FbaQ9-X-JxYNWppsvDE9UTeb0cxbS6JsIV_82i334aVLQfUmkZO1HHgXUQjTvl0mE2TqPCRei2hrj-81CilM08cOXEzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b7671e0e.mp4?token=gzU9mpgAyoZVgdP7MY6khDhYzMlnHYKFrkKHBi0pbjioqyyb2Wu3XN8MfkOnLbot60YUiABDPnf2svEchDcvkDII3-vT8nfYpxdaFPremB8oSjs8FktXbiZiPOn_EsMsh73Xz3vvintVcCm4vr1zp6T77vw2Hyr3jRJDG-RXMtdAvfxY4CRqatUGxEcYfCihzMYmKDNkPnLD5CxlW2OM2lj8kXxrbNt_gZNMye3TEbpLKUw0uaW2EEvpwt1FbaQ9-X-JxYNWppsvDE9UTeb0cxbS6JsIV_82i334aVLQfUmkZO1HHgXUQjTvl0mE2TqPCRei2hrj-81CilM08cOXEzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
🎙
👍
لئو مسی: از همه کسایی که کمک کردن آرزوی کودکیم برآورده بشه ممنونم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108003" target="_blank">📅 12:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108002">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbb5ac04.mp4?token=PLm4P-PpalW-Hf_CfTGjb0fTDzYCqM4rbFWl181HMqK1-ahcNGR3QuM5rdlOLMTVp_QsmY8ex701JPOknAlNRcRnBMVKDM69UIrQXD0MG1lVKnqwH4pBvaSvuAkSvx4vm2SvDYc4KwcXUyf7byrQBt0oFF0z2ZUAD131nB1m_SLn5O3--KdT6KNbzZBdTKSjRrXWmyCmUuNOhGsV-0205Aw-VFekDiDhhbH013KfiamQect36B_GZMwo3GU4txMeehPgqWXZarqlnf3U2O_xi2HGd1fKkgEfowsjkip38xSUfimi49XJ3LoA8NCT749jqok4uEUy8RDH9QbMSEt-yTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbb5ac04.mp4?token=PLm4P-PpalW-Hf_CfTGjb0fTDzYCqM4rbFWl181HMqK1-ahcNGR3QuM5rdlOLMTVp_QsmY8ex701JPOknAlNRcRnBMVKDM69UIrQXD0MG1lVKnqwH4pBvaSvuAkSvx4vm2SvDYc4KwcXUyf7byrQBt0oFF0z2ZUAD131nB1m_SLn5O3--KdT6KNbzZBdTKSjRrXWmyCmUuNOhGsV-0205Aw-VFekDiDhhbH013KfiamQect36B_GZMwo3GU4txMeehPgqWXZarqlnf3U2O_xi2HGd1fKkgEfowsjkip38xSUfimi49XJ3LoA8NCT749jqok4uEUy8RDH9QbMSEt-yTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
👤
طنز فاخر ابوطالب؛ ۸۰ ثانیه تلخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108002" target="_blank">📅 11:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108001">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇶🇦
🇮🇷
الغرافه قطر اعلام کرد که استقلال بدلیل تحریم خطوط هوایی ایران حق پرواز مستقیم به قطر را ندارد و باید راهی جایگزین برای حضور در قطر انتخاب کند. آبی‌ها احتمالا باید ابتدا به عراق سفر کرده و سپس با پروازی مستقیم عازم دوحه شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108001" target="_blank">📅 11:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108000">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19eaf1307e.mp4?token=dYjcZ9VZFhiQDQDP43Ifp1e0KByrLnAMr14Qk7fM6jGpb8Z2FY3fpgW3EQC23QoZggVjpjX8PiJ74TZCoRpMd-1qG3HlFcM-KUWVIQR7uvIFxuggrvKE3BuL0OAxU00Ei6LY0Ulg7oHBeeSrj_zZtoqhJwVuyJhjZrbQHtaR-QIS0CXirbfj7VZ7Yef6eqQwaPj8SHrcfrXxOdhEPOrVuHlqf5GjLYVwGoNQD_zR05LMnFZIka7O9DyygwjKHIk6Xk4ZNHaJGQZiHWGHPrh4-oNsbx8Hi2ib-XiKtZAA8LUzWRzv5ZxMsX8NPXYtTmlBstM7DGMDu5XHomi_e-0MoTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19eaf1307e.mp4?token=dYjcZ9VZFhiQDQDP43Ifp1e0KByrLnAMr14Qk7fM6jGpb8Z2FY3fpgW3EQC23QoZggVjpjX8PiJ74TZCoRpMd-1qG3HlFcM-KUWVIQR7uvIFxuggrvKE3BuL0OAxU00Ei6LY0Ulg7oHBeeSrj_zZtoqhJwVuyJhjZrbQHtaR-QIS0CXirbfj7VZ7Yef6eqQwaPj8SHrcfrXxOdhEPOrVuHlqf5GjLYVwGoNQD_zR05LMnFZIka7O9DyygwjKHIk6Xk4ZNHaJGQZiHWGHPrh4-oNsbx8Hi2ib-XiKtZAA8LUzWRzv5ZxMsX8NPXYtTmlBstM7DGMDu5XHomi_e-0MoTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
پیام‌ویژه یک مادربزرگ ایرانی به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108000" target="_blank">📅 11:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107999">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpoUFPKDr1TwpTud4aS9u7YQsutVJcGpJYBDf_97kaK-nBg1UCJRMiHbCDOmS5KGqzKNHSPXG5E0FIq6QvKJNXsxO6rzpI0lg5vVzY6Are8SvuxGs2-suUnkdYt3ftjOjoWLMLbuMsZTY34hiSLPgeXMNH8KRIqQxnFRgZ0_WiWpnul3QY7pO1oNVVpFcmFNwxQv6hNTXSI9_WCtbxyeRrRni0buyoXwH681Tqg4gyTfiq0SIDJBDZo3WcVGiVDkQypdOAoFeHapn842Wd48Rn5UWWG__jQxM2wtYnq0gVSfMSGYTpida0vFMfoWV9HLXMlQ0YG65MGCLTzzY8zGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🐐
☄️
لیونل مسی با همراهی استفانو دی کارلو، رئیس باشگاه ریورپلاته، کارت عضویت خود به‌عنوان عضو افتخاری این باشگاه را دریافت کرد. همچنین یک پیراهن ریورپلاته با نام مسی، به اسطوره آرژانتینی اهدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107999" target="_blank">📅 11:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107995">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcYozKx8BFTR297TZysxSUj4q2rkzAKjT6-lb19OruSsdEONM-N9X78dJmQNk66aSKENIBlXrNGHqbqKT9_6c71WCt9YZaa3OUzXNxUl8RiNIravPXp43T-5NU1yif8XIKKZHlo_9lwxACx1zn-yh7ls09f1V2R238HdS6GpQ9UmQMVD8at0KOwYz3UaEQ6WVfcoIKlWGtQKAbN1HniqEgmJXwJA2Krymwaxuhq44_1Fy9cxM9f1Emr_cpOFYp3NW250xxvrRYZKL0e9mgMaSVmPLEh9qifvO5lApNwgU9iKP5Xzg7G6HG2FfPNDwC_GiLnBD2KvTg_KbTCRFeS16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auhiwZm4_2qu4a2mvezz-Q_M-8N1vXN7ZAUVTpVQcbfH_IgX5O6ZD1SYebfz73kbb-_rllj1LK599WkOeLjK71ImTiST8j7qDXkLFx1pbqYoafBGmrhxQECkwmEwzQIV0UDPeD3d2yLHDUJ7rYHpOkN9TGUe9FYC8H4t2QdW4wScGa7sSH3qu9kVJ_TtbadVf76d-H9zmBr0dYSAA9rh-8oRdEySBIJUEz4cWGb3DtaQ5XTZRAKZTiCmhVPpV-D2-2bKtfDF91k8aRw4WhPLjv8_zfytQ_ezpY0wPkn5r1Q591y4fBmbO9TBa_xkekF43i-1kq9TBHmXMkyKlbBnIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tWHW33fUfqFgNVdZfOMQcvawWZt1NmcEJPocuwDpY-2BZZuFZrcC8bfdfoBqMUCF2dFukCmghBq_kMgejDxcrQYamXRv_DWzgoNHgh4Mg1IAnpexJWGj1IfAWtIa7DdvPXTNjEaKNnTxxBQ58L1HSHFHzWas3dMXhB1oWqM1aeRbznuox9Eht224tYPeHzoIjiJH2lzYex2flcJrr6JyspxNi8f09AABxbOgshaxPVm0H5ljULXsx4dPlpP81yRd5xdYvNv6e9OTx2ofX0c2MezxZzjOYnGg5f9jDZ8kAJcWNuxmin2JIlvLC0LkNqaVVb0Wa9xkvV7VkI7QZwyP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tusM9IOcW3pTpOWVGF7g-v5eAoS38wVfBTD9m5024GAeHXK9n5RK6Xhp9RAyUksd2TqeB9wykYeIavsr7KtM8DOs9fW05NrJ1ai6NwXfobJExC21CRimvGXZv7iEVF-d_KzauvjeQNYdXghD6EQbvxkyXEahex9-s4Q4Zq0wHUMz8toONQLmFb7Akt7NE5VO3yoLJnP5M-iflAywUOuOGuCmS-kZHv2rsv2CPfRd5Z6nZogrX7Nc4QPf8MkwBV6ueZ5a9LbJE9RuWUVEVANogNlYPmEJVynCfG-5aBi6wl2hAQFiyOLxXdE25-2dI5YGQTcyIlzecXnVT8J_NJl7dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚪️
کیت دوم و فوق‌العاده ملوان با الهام از تورهای ماهیگیری و امواج دریا رونمایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107995" target="_blank">📅 11:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107994">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎙
✔️
😭
لحظه گزارش آخرین گل مسی در آخرین مسابقه‌اش برای آرژانتین توسط جواد خیابانی، رسول مجیدی و نیما دلاوری⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107994" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107993">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107993" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107993" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107992">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phtBi2Epw7Q38JK2FAMTSm4Xu9hg-sZD7l5Z_Ad2_PD33IXZj3bb5LJy1LsKC0fgJHG9W-I-0MZE14TSeYzFLdkTmQ0_8S1f3FMr1H0GBMzzipW7_A0BgXQtheLjphi2sxOmvO55DAKBfl8W0KFBLQA1kk7olBvcc10YrtyKKqysRolJU6vIoCEAH-SbwXxVPcz1ahoGY9lXFI2MNVwZ14NcMYegh4vxV1g_yx9uqLDJnpoJOEDlj2Zi2U7pM6WVVB1Forv9jqPIfip6sY_3vHNKiQWFrAeRFksd7CRfffQ-aGWKQSnYAQG3SMBLUV8NnrDvMIZj-r5MOw4em5o97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107992" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107991">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4e8b514a.mp4?token=owaHgddhOTZ3zp7QSWW4tNBsjkqddTmD5Bu8NrwF4rrPI_7CSZKRnLcFFWXQG5kCURzFpM76p8xDl7QVhszFOFlJPvsSlHuSXmJsSO0m_eGdZitLy5LmvJC3niSXERUIdj3JDHHCQ5vqiFpns9mH0gRCwQmtwRCIFCmyGu2Bu_EN5a5HpKdyKW48HYgMQtWavcTVEree6pzW3cURqK8nbOMvF3VAwvvCtIyP5uF1RXcv4VNhhDLmMxaKdJCcYAnNZ9ccVT5PjASunTTuX3TSbGFuVvogKurS3-2DB51Q7-Q16EFeqxoljRpQhpFrB3W95YAjm0z03uUDFO_G9VbtQJcM_bRnK3tfKb_A7AWv1KPCNYAK7IIL1jt26OBZaIBUT_O84JUXt9vCG2TUV-s5F73ghkeTPargPWHBqW-nEQtVDGYSFHdgkaC1gT6gSgbi_rQs45gYwtusjwANK2c5_Z1A02K17G9kUzzrQh0aFxrd3L-HCRH7cQmWjjF8RQOoTo8HXy-v8wFKTOQyayR7N9CzTbPzN9sg9mJGwKTltDS0O2GssH92PaXWHdQxaUxLeDoMkiPzzxWKfcwHOuV34uAkX5qGhUC8ASAu6GYHsyybbGDNtldJ8JGvR0Zqe0SJCY72rNRgZRYOapbKIQ9W6ST1DZAxHfAavdy50F4iObE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4e8b514a.mp4?token=owaHgddhOTZ3zp7QSWW4tNBsjkqddTmD5Bu8NrwF4rrPI_7CSZKRnLcFFWXQG5kCURzFpM76p8xDl7QVhszFOFlJPvsSlHuSXmJsSO0m_eGdZitLy5LmvJC3niSXERUIdj3JDHHCQ5vqiFpns9mH0gRCwQmtwRCIFCmyGu2Bu_EN5a5HpKdyKW48HYgMQtWavcTVEree6pzW3cURqK8nbOMvF3VAwvvCtIyP5uF1RXcv4VNhhDLmMxaKdJCcYAnNZ9ccVT5PjASunTTuX3TSbGFuVvogKurS3-2DB51Q7-Q16EFeqxoljRpQhpFrB3W95YAjm0z03uUDFO_G9VbtQJcM_bRnK3tfKb_A7AWv1KPCNYAK7IIL1jt26OBZaIBUT_O84JUXt9vCG2TUV-s5F73ghkeTPargPWHBqW-nEQtVDGYSFHdgkaC1gT6gSgbi_rQs45gYwtusjwANK2c5_Z1A02K17G9kUzzrQh0aFxrd3L-HCRH7cQmWjjF8RQOoTo8HXy-v8wFKTOQyayR7N9CzTbPzN9sg9mJGwKTltDS0O2GssH92PaXWHdQxaUxLeDoMkiPzzxWKfcwHOuV34uAkX5qGhUC8ASAu6GYHsyybbGDNtldJ8JGvR0Zqe0SJCY72rNRgZRYOapbKIQ9W6ST1DZAxHfAavdy50F4iObE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
اشک‌های تلخ انزو فرناندز در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107991" target="_blank">📅 11:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107990">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb06960e3d.mp4?token=IOUlNROA5sT9xFP1rrwzKtDSLgwV2Pq3susU9QpVtTQLWmUH3mD3HERyrfbFFh9IqPVwBrGVvNkmD0oQn9q0k13s07hFXGBmkNBnRhdNB89bDr-5teh3yl59n-xhMRw9fAXei5bvHRIr4nNmd2ffLDAA8O3kmIdg5BTQucYkLuaJgrb0LoJxC2jEHcVJC2gxBVpkyJQwSyhbm3wx6RBteoCG04mszC3u3jZtYvsBN1VzBd4OeTy4jhaGGz-O10f7xYOhVTCh5WmjHI9mCtTyG5f0QYXBZu0huFSQgkATs-XXrwa384blLzweh313OFB0U_exyBcpPFYvfVQJzOLDrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb06960e3d.mp4?token=IOUlNROA5sT9xFP1rrwzKtDSLgwV2Pq3susU9QpVtTQLWmUH3mD3HERyrfbFFh9IqPVwBrGVvNkmD0oQn9q0k13s07hFXGBmkNBnRhdNB89bDr-5teh3yl59n-xhMRw9fAXei5bvHRIr4nNmd2ffLDAA8O3kmIdg5BTQucYkLuaJgrb0LoJxC2jEHcVJC2gxBVpkyJQwSyhbm3wx6RBteoCG04mszC3u3jZtYvsBN1VzBd4OeTy4jhaGGz-O10f7xYOhVTCh5WmjHI9mCtTyG5f0QYXBZu0huFSQgkATs-XXrwa384blLzweh313OFB0U_exyBcpPFYvfVQJzOLDrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
😭
خداحافظی یار و اسطوره بچگی‌هامون
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107990" target="_blank">📅 10:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107989">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO8AMfR46LtPWxx0DHPs1-gGWi3Q5T0uUhS6OImp3mbveD8o0ryEazEOpT2d9QCkw1IAjgFRNduX7aux4osfUKKTbwHop9rv4iBmkSfQPwh1Fd7mVZa2-jupnLPDb5PvAX9LMFXT5eU__TkTZ0uBlAGpSMgqF3GHvwOTTS7rKN6MBpadRXCNGFkgyaCccEACT--hzyVkg83iN7zQOCSW5hgw25sSoTcBZqbkKoz6SG6mVtKCMbYBkUWI9zFbYNpzEHztczj0RBkveqtIlJp-twlzFqubCE1LhUhuXTnkfzrG9J1CEN7cq8pp4JRaD0VTYoVMZsF2QkFXKwGkD8fbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
🇪🇸
🇪🇸
مارکا: هرناندز هرناندز داور ال‌کلاسیکوی پیش‌رو خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107989" target="_blank">📅 10:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107988">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951062ce8d.mp4?token=WWGgho2F62_R_sCzJyvURxEJjiPlHNy0Qr-75k_fwuZPJJOZRlwZPiGZwDhMVRYk-aByTgHDn1CfTIkH4IMPSu_vMJheuMwhytDKGda_lTryKHPgiTA2GBcewTrPa6E41J5LyLWshgJHk0tcE1ZV3bjAnjjDXSWpVVm5Vn3ejygbJ7K3Fj6K0HrM2iPNrfVcFKw6p3AbDxnLBHuRBGTUpH8FD46Tc2vGO6Bcyxnsb31z11fJlozcl23B-f2qoD_QdBEsyIhvHzl9QTzy2M89ww6RS70Umsyv7DQXOjnOrptRyMDJlecm-BfafsLif0ql-PcuqGRzXenHwWNUKdTp7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951062ce8d.mp4?token=WWGgho2F62_R_sCzJyvURxEJjiPlHNy0Qr-75k_fwuZPJJOZRlwZPiGZwDhMVRYk-aByTgHDn1CfTIkH4IMPSu_vMJheuMwhytDKGda_lTryKHPgiTA2GBcewTrPa6E41J5LyLWshgJHk0tcE1ZV3bjAnjjDXSWpVVm5Vn3ejygbJ7K3Fj6K0HrM2iPNrfVcFKw6p3AbDxnLBHuRBGTUpH8FD46Tc2vGO6Bcyxnsb31z11fJlozcl23B-f2qoD_QdBEsyIhvHzl9QTzy2M89ww6RS70Umsyv7DQXOjnOrptRyMDJlecm-BfafsLif0ql-PcuqGRzXenHwWNUKdTp7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
😭
بازی تو دقیقه ۱۰ به افتخار مسی متوقف شد و کل ورزشگاه مسی رو تشویق کردن. همه هم گریه کردن و اسکالونی کنار زمین همش داشت اشک‌هاشو پاک میکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107988" target="_blank">📅 10:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107987">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea54b6fd5a.mp4?token=I8dGS6mrcSGeV66sN0757gIiqtAC4KBNfxuhKocPg3i3Q9kIQY6RPUueXt7zm-StSV3aMZVllzVPpltx1LmNwwT4Jk_ZXaXtKr4YMsQGRNdCeDlHgwHy_f3DHijDFxhib9xIUnsY2hb5AXJGNrSouf4J3-pB8DwARjqwoXeIooDqLZrvLMghPx2D7g_Pajk8sIrjL4c9w7qtcrOWWWx-_nGe6Fd6UcvvJbALrcY2497KqSqKtF8U6nO0IHs1DRXZnQF1NMPA4C2-DpDhr8BP_JnDaO-I5_oVGNkmiUV_s5x2c4__SVREnJUB-v_QX3YBQfbnD9hKquWVFMUcNDhptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea54b6fd5a.mp4?token=I8dGS6mrcSGeV66sN0757gIiqtAC4KBNfxuhKocPg3i3Q9kIQY6RPUueXt7zm-StSV3aMZVllzVPpltx1LmNwwT4Jk_ZXaXtKr4YMsQGRNdCeDlHgwHy_f3DHijDFxhib9xIUnsY2hb5AXJGNrSouf4J3-pB8DwARjqwoXeIooDqLZrvLMghPx2D7g_Pajk8sIrjL4c9w7qtcrOWWWx-_nGe6Fd6UcvvJbALrcY2497KqSqKtF8U6nO0IHs1DRXZnQF1NMPA4C2-DpDhr8BP_JnDaO-I5_oVGNkmiUV_s5x2c4__SVREnJUB-v_QX3YBQfbnD9hKquWVFMUcNDhptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌دیشب اسطوره از نمایی متفاوت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107987" target="_blank">📅 10:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107986">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ce0c64ae.mp4?token=a9Gn2eK0_6vZgodTIlZ0LPllF5QE6ocKQX5DWDYhA4mIWkzFwHgUi4mMNfyRV8KSuh0U1Tzrd4lnnEdlHlrPrfzu9t8NIz5ZynFDCZQhQJ5lRpNcCdNse-oM_EVL6df0ye6mOD9dXheGh1Ptp7RClDsIbA4GICCIc8GiHppaSitMG3tpiyHGXB8-Jt8Xj32tTzS1Mog4lBKdP0bYhnQoUECAZmPYMA1ZDayvd1Tzh8vDXj1ghEbJUjUajUYlgMXqjZc2z5Wg7Jmn2qp0aeZ4htLawsZ8nPWRwKpO84JbMWAb5sh6EB9xG4vZbAf-G1i1hKKHUssecoEGL5FTTFiy5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ce0c64ae.mp4?token=a9Gn2eK0_6vZgodTIlZ0LPllF5QE6ocKQX5DWDYhA4mIWkzFwHgUi4mMNfyRV8KSuh0U1Tzrd4lnnEdlHlrPrfzu9t8NIz5ZynFDCZQhQJ5lRpNcCdNse-oM_EVL6df0ye6mOD9dXheGh1Ptp7RClDsIbA4GICCIc8GiHppaSitMG3tpiyHGXB8-Jt8Xj32tTzS1Mog4lBKdP0bYhnQoUECAZmPYMA1ZDayvd1Tzh8vDXj1ghEbJUjUajUYlgMXqjZc2z5Wg7Jmn2qp0aeZ4htLawsZ8nPWRwKpO84JbMWAb5sh6EB9xG4vZbAf-G1i1hKKHUssecoEGL5FTTFiy5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
فوتبال ما شبیه شوروی است اما در مناقصه باید وعده اسپانیا را بدهی تا برنده شوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107986" target="_blank">📅 09:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107985">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd225b786.mp4?token=CDgbatPeptHdu2mIlZsPrcSj-JhPsrNcS5UkycFzDbJIWE80PQcftABxqSOHdDc90rdtCMxlXlgYlqas99qmw25MHU_1UfW8Y0u8mmxXZ1EmBC-6BMGPHbEkbV4F80S1SynCTikysWxFyOs5tiNBrFSlud20-NgOEvzHqZKapYYQOgOttQXD8TqGK_ra-rdEaanDAwqBf687vn6qybAm-mIfKPzg8WXn4Q4WPtiRbr9LIVWlltx5nZyOkpsF2TAGTDnKvmtZBgf6w3zw3rTdInbvFflosSya2NjIRBqYMEonV4tDya71_-FP96Jzif3cG1MzsJLVvvSeO0fkp_nc9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd225b786.mp4?token=CDgbatPeptHdu2mIlZsPrcSj-JhPsrNcS5UkycFzDbJIWE80PQcftABxqSOHdDc90rdtCMxlXlgYlqas99qmw25MHU_1UfW8Y0u8mmxXZ1EmBC-6BMGPHbEkbV4F80S1SynCTikysWxFyOs5tiNBrFSlud20-NgOEvzHqZKapYYQOgOttQXD8TqGK_ra-rdEaanDAwqBf687vn6qybAm-mIfKPzg8WXn4Q4WPtiRbr9LIVWlltx5nZyOkpsF2TAGTDnKvmtZBgf6w3zw3rTdInbvFflosSya2NjIRBqYMEonV4tDya71_-FP96Jzif3cG1MzsJLVvvSeO0fkp_nc9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
خیابانی: سه ماه دیگه صبر کنید تا بفهمید اسم واقعی من جواد هست یا جمشید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107985" target="_blank">📅 09:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107984">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce8d64d12.mp4?token=E1Lnl40BhFJN5Y5NUNyCk0_vJukC2eZlALloN42RH-vqLHa54BjEyN8vQdP_bVophdXw1X0sYI5_SYYjwn4oc1gWuDw4CM23ax7z7LsaP-dif0PC2R-tTsyT1Mjdo_pPcQh1PRhvno5877qGfKTYtXUIJo3rmLPOfQzPPdNN6PZUDuv2ugG3rJzAlewv-bMXxV1mb1Nve_MjaHCtJrVMpZhQhdlecpwK4FdvEwCWP3xK37F19FF4VzBIcshZO2yPgWv3J9dpBZmBnQ81ndSPi23XXfZgtkn61sPFfIlJ4hlzNl61SALg997OQpahjI0fEZb0md3F88kyw-t_5Hm8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce8d64d12.mp4?token=E1Lnl40BhFJN5Y5NUNyCk0_vJukC2eZlALloN42RH-vqLHa54BjEyN8vQdP_bVophdXw1X0sYI5_SYYjwn4oc1gWuDw4CM23ax7z7LsaP-dif0PC2R-tTsyT1Mjdo_pPcQh1PRhvno5877qGfKTYtXUIJo3rmLPOfQzPPdNN6PZUDuv2ugG3rJzAlewv-bMXxV1mb1Nve_MjaHCtJrVMpZhQhdlecpwK4FdvEwCWP3xK37F19FF4VzBIcshZO2yPgWv3J9dpBZmBnQ81ndSPi23XXfZgtkn61sPFfIlJ4hlzNl61SALg997OQpahjI0fEZb0md3F88kyw-t_5Hm8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پاسخ جالب حمید محمدی مجری تلویزیون و برنامه فوتبال‌120 به دعوت ضیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107984" target="_blank">📅 09:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107983">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نورپردازی و تمجید پهپادی از مسی پس از پایان بازی آرژانتین و بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107983" target="_blank">📅 06:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107981">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYVsPACXMikyfLMHb7cSXDNJYyrZvtmVG8DZDgHYVWn42O5TxB3IQk7mp5Mg83XAv0unSsvhwK0ivB5QQGV9iYIEcFSzvaOrVfmprPpQCOWZTc-N5IhfycNG8F8NBExsW425kXPY6RdNfOdS6eN5nnBrGWqVV34WBLva5YcwQlKi8iktzZAqyRRBf_FOXpe0PbTFzuTXFkjFyzKdVOzihiAPPdVxpg6oejm2vPwB6f5r08jRSKzPuMw-Ih_gObq89IHm9wbs3721KbthwzUvM43PMVPmNT89xOhqhWg_z_jw3sIV0oVM7WarnfBISDoBEgBBMzJFbERZAgdmlcop-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVjWsBvQK6rBlgwOFuPrxcEZ6hvjdos7srAfepd13yY0ljcIzxYqg1ijOrsBdkrqBun2Zpe2_TVea39E4bUGFnnpnD940jutGIUXOQZFJc-IXwCwCL1h0rVjo3RxXlSGS0l-MqFkCI3YJNOBAollGTr2P-pxJdZsZr5JPaAnRSmKT-_thVeDdlOox0EVBWLXXoVUpdKeqzJ-gvpG1YDEPdzMiLodGp8FVNSY_GqBOP3ljn-2hoshA-OxKvOqwldJx4-PBGPnORmP_gNuIbzb_CzFGSTqfSaj66XbRFJl_oGswfalt4xyrNbJeBgUG4XXS6FaRO8TLFjYxxDk-KZ5dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😭
😭
😭
اشک‌های دی‌پائول بادیگارد مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107981" target="_blank">📅 01:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107980">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=nGEM34dkyQJN9Ihj5b62OZqxU1-9Vwhbao3jctXqoKhW2zu_zZ8TnvWYTJvGda4_6TqFonfPzVKdNQu-x3J9vf24qPMqGuV9Lh9SlmLphMqyWyvhLX5-7gdconKDo4yFNzj6ufsCgcb4BWgFvU7o_tvPfmi16uuo4qqJRgFylc73umOgYlePRHbP5faCHxIs3LE8Ho2AlFYqO6IYYASO-IceOetwV0VCoztmW7PcR5jYrxyAMlFBaWC3badsdZs47eCbthfMPukifBim93nqBIZ6H1vMyl3UefP-W5TfkPt9Yi3Ub8TreFFs8Yojj2obK7uowWu-ut-BtLjVTrMUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf74e1898.mp4?token=nGEM34dkyQJN9Ihj5b62OZqxU1-9Vwhbao3jctXqoKhW2zu_zZ8TnvWYTJvGda4_6TqFonfPzVKdNQu-x3J9vf24qPMqGuV9Lh9SlmLphMqyWyvhLX5-7gdconKDo4yFNzj6ufsCgcb4BWgFvU7o_tvPfmi16uuo4qqJRgFylc73umOgYlePRHbP5faCHxIs3LE8Ho2AlFYqO6IYYASO-IceOetwV0VCoztmW7PcR5jYrxyAMlFBaWC3badsdZs47eCbthfMPukifBim93nqBIZ6H1vMyl3UefP-W5TfkPt9Yi3Ub8TreFFs8Yojj2obK7uowWu-ut-BtLjVTrMUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
آرامش‌خاص و لبخند‌های لئو در حین ورود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107980" target="_blank">📅 01:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107979">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKd7w-EdaOEBxpV-83_NCVht53KJcckHjEmoq18v4hnZHTmYmzD191HAks3pOpKFDJ1aTDy2sI206BlkxBRcaPDRFsIerANs55MnzjFhIoTFIbfL7qrD_LyAJV7ZFH6Sn6AadGQBKwqPgL1npFYQYt49k_Pt-UyT4wkTt6ZouOjw__kDfCIUYhV4J_MmWKqUQRi_tnL8964wF-wFCjXnm02eSxl4DZSOxGxgEQLbd_CE93ZhxjhLBlx26uVx07h2_N0-tcW4k_DIBUZKitkdMbDmTErWBkKNN78ytww3zaiTtXnEzAB2A_edifgoI-74TjGNMAEUf-Remu0JHfwxJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لبخند زدن هاشو ببینیم
🐸
🐸
🐸
🐸
🐸
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107979" target="_blank">📅 01:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107978">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agWLhJItlQcvwa-PmjIePCnLjcIoK9xpUGr5_U-lPY_XvL5nzG0EMcTkthgpZzf5L1vvtrDy2-6a6Af8f7vpkjZiGxQkO6_t7Lwqm1A_mBBr30ftSnBlArUrtbQ57yzv-ZyHTxeT7D4Sd660KGcTpuPBglg1rF_hKvKVXtMOpmNAIrzYtl9KfkKA3sRyanDHgnfwM9EqHyU5PDUn3PgSazf17bdl5XGqlfCO4VXjEb4r2VUHBjt_GD7llcTTxhQD0mPeMQYoxm6JTo1O1d7D02zkQ2eVtdkjBfyyUCuvtw0_Y0wfJHLzT3o6O_JaHbfSAk5H9P1Pu8zpxzDfDz7rgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
لحظه رسیدن لیونل‌مسی به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107978" target="_blank">📅 01:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107977">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyK7FqFYLM7RalxFb6dj32GgtZckkt-u5zeJTDXbrcO-j_i51UQYUZzpYq2s7le-6bzMCrSgbvCFMEnaaU3YByLvmvLzuLXlyE2SHHNARwlGGK6Ap0DetzBjRye2PAMFhbCEksgYBeMGZ7lytAH2GTHMJzAX7jcKKtKDXJXPY5hjGLsDAU1OHTVCmkXtY18DZ_PfB1llqxwke-uGUM6waVNIdFN5KE_WkFUqy1BQDsF-BBDktb3MDfhdUMFUl7b6laWPucQwW6r8UgN6bDKGyKLxY24mEJUvruZxt3BXDrGXPIrjr-YbZx-8kCpYKOGMW51iOebeJVpSYnjUCm_w2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
نمایی از استادیوم مونومنتال آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107977" target="_blank">📅 01:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107976">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=q3jjgTlKcLWrKAEG1fmEmDft5BKLVTyNvKq6h8_sdFzSV4ZDUP0tKXyKz0qdFbxCcnLA3IzgPWJfX-VgzVkUmkerLq5UKsrpA9rdfYln-CE2nF3BQK1049XJBF5WNh9iz695qSGWBV8MpEfm079TlczYvxremUG9w0PlRR38mGEwJ2HoJ156MZiDXYLunqe1tlDTAi8S4y2Em7T8Gzwiup4zBAqBDkhw6bgWreW1qBug7LB-YoahlsFVUsF2j5ydg3wRbD6FIpcjdcrvRigBGoZKQnlglhqD_Xr6DWxZSiOdaWpuWtoILXJiugVDj5RYO3wG3ZdGyzUYCcQi_uG86Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dbdaf83b.mp4?token=q3jjgTlKcLWrKAEG1fmEmDft5BKLVTyNvKq6h8_sdFzSV4ZDUP0tKXyKz0qdFbxCcnLA3IzgPWJfX-VgzVkUmkerLq5UKsrpA9rdfYln-CE2nF3BQK1049XJBF5WNh9iz695qSGWBV8MpEfm079TlczYvxremUG9w0PlRR38mGEwJ2HoJ156MZiDXYLunqe1tlDTAi8S4y2Em7T8Gzwiup4zBAqBDkhw6bgWreW1qBug7LB-YoahlsFVUsF2j5ydg3wRbD6FIpcjdcrvRigBGoZKQnlglhqD_Xr6DWxZSiOdaWpuWtoILXJiugVDj5RYO3wG3ZdGyzUYCcQi_uG86Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😭
استوری امی‌مارتینز از سیل‌جمعیت اطراف ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107976" target="_blank">📅 01:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107975">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=PJvXLIx_J2bP_zv2c_oXT1EfpkVUsOJOK8ep9R_1E5tVKJzWzsv6-gNGupVhMFenWh60mdFK-QDa23J1UKVho_jiCyI7oDweyGxL6jnfGpMGpV-UcFpMXzVIwn4wbYMqQSe8g_9Hu7419xKFa8yj2ea-cDJr4E-xpMgpElp6UHxAL9LrQ1lnkAjBqmYdINgAF0YJLTXmi05Zd6oYLl9rTRJ_12bPvdegCHSaG257rXbXurAGFlz0Rdywz4ov4fadJQPq-1Q44ZnOkscbmSzhhwZsD8vVHiQbJX4iioWHcSmoQ9L_kLAKj5VVIL5MdB_dn9F9dVyM0zBWU-OqMY2Qe4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbdff94ee.mp4?token=PJvXLIx_J2bP_zv2c_oXT1EfpkVUsOJOK8ep9R_1E5tVKJzWzsv6-gNGupVhMFenWh60mdFK-QDa23J1UKVho_jiCyI7oDweyGxL6jnfGpMGpV-UcFpMXzVIwn4wbYMqQSe8g_9Hu7419xKFa8yj2ea-cDJr4E-xpMgpElp6UHxAL9LrQ1lnkAjBqmYdINgAF0YJLTXmi05Zd6oYLl9rTRJ_12bPvdegCHSaG257rXbXurAGFlz0Rdywz4ov4fadJQPq-1Q44ZnOkscbmSzhhwZsD8vVHiQbJX4iioWHcSmoQ9L_kLAKj5VVIL5MdB_dn9F9dVyM0zBWU-OqMY2Qe4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جو فوق‌العاده استادیوم یکساعت مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107975" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107973">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSW3H_aGyMXKgnLFt2b4R-IxZW8ib0_4IV8l9HadmshOXFIcabtW9F7sDaUBvRjWd90mgpYWLGYB_DuSounjtkjFQW1d_JPMBqDphzYT0YdhGONBHt2rQfuIQq_unrtpGCsKT6jP3kl5s4R3Zc-bzmfWa88NbIW-WJF-XTe4dNPHNHSTMNtI8Q16RLnQxOPDqcK1gRgeZh0peIf5Hv1j-xfDvm0JGJy2g62SD48yAHfCzojMDk9e3N8rLeblyeMmlwoABJMXhLEd8XpN27eVdIeAedE5kWkOlNjA2LkPLgzoL4gH-GPNOPvc7jfbsmTNKSfJzB-LYVuu0KTEdu79tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoc1axLTS69XGC52gvEIeyA3kGF4JWNs-clxS-76GYNUiCJg2h4aNO4eOCE3isgF5PbB9IrLGS0kWeU9n-WeYHIlryMAoKuRUY_lOafbF4XVS6FmHsf4RnB9KsUQ1saPxyTf_5JSlaH_bMxByvHs9TVHKSPS7a_LaEzXH5DSzz8geNJu7R-6ZLns1c3APFvEa_S_8bjeGnSL9YLzSBz1EI6Zw6qpF6CDC7NHEYgfwAtEcS0IJomkYa8HNOR_bhztnj9tw-FEKFeQAJsLMwZzrMnbR4fBV-1IiQ70s-11Hvw1TQlSjEtqO5MGggum74Z5t94IIdHCA3eH6L_PvsLHOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تغییر عکس پروفایل آدیداس به شماره ۱۰ آرژانتین
همه اکانت‌های آدیداس در کشورهای مختلف، عکس پروفایل خود را به عکسی از تشکر از لیونل مسی تغییر داده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107973" target="_blank">📅 01:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107972">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اینقدر غم امشب زیاده که آدم رمق پست زدن نداره
😭
😭
😭
😭
😭
😭
😭
😭</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107972" target="_blank">📅 01:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107971">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SGsYYiuBYwKGDN2QktuAVBnClkPtIpYD8ENvnY-zlDhDooDXA6x8yTL35tCwLDXDJKprTXGSJru_3eIJdGk9KrikLTGNN7WcgEyLywaBKzSQFCIWb8YtGBBNEBwfv_fpChtAMmxz7txzk_st29zZtpEydGqIbSDT9ZYqOVG4E9N3CziQ54dP_HUsUfhmR7mR9S4Hr804qyb42t4aw5hd30VtR4RvOZsdfOpsmS1BdY3vW3bogqUEIyHqYL_NMGuSrIhJXnAMVTyy1v8-vETNx7BJ6BKEGjVteBJfOLBHJyz21dWIbvhoGPV_xnOLwOJQrg1lDoBmyca7RObWJh7vYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
⚽️
The Last One...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107971" target="_blank">📅 01:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107970">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2Dmr19N2bBwgJIfcTnczbw7U3FFDEqP3enwSWANOjDujOgv8S5QYL7JWr3yNVPBYkdykwtxMvYrMrlXfZmoPPbhwBUhxH8zSjykBhrjxyjZsxnWidayjfRh-38U8UlfBkv3C_GbS2KoNQLo4yN1pRmf5NyuFeoYVfEa8mJUSqwBYUb7HlSH4_ccvRfgE6qgyc9BB7SEqTL1j1QTXvepf2oysT17N-Z-51NknFVmvs4D8b8SgQQ3vAyqtvtoAAl1dR56HAbKDzu2AzOuqGSOfZmvq5kXfIfyly6KvpGuqHX9EoUJaytR_feqvnVpahCem09RSC8YtV_Shle1fb2Rlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107970" target="_blank">📅 01:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107969">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbeWS-F8vAl52L0_R4zklzuzPM2PDRUmczPUOrzXS0khEIWMvuDftuznfc4mt-uTgWsjRW2LFNQvgVhLMaKYmjlPc_wB6os-d_rJkR-umHfArUdRJh_hsLTGI8DvZn31o2BGZF8SQptglNRdLp81zFzq0p5PEGXJ5jqcfYAtEWBh6kN5IZDjiknZ6onJ5l3sRONWmwvUW0v3YeHtIV4izrxBkAQXxp45-E5p8Yc_Ek5aqpuFn-xTYIMs70NRLuS0WWjxHd3RD05DnF_ozX452Pl4g6pnza2IT4YzXEO38DXKsHE8Hqu4bx6phDYxowd8SeOz6rbYhXA4zoILxedmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😭
گریه‌های لیونل‌مسی در بدو ورود به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107969" target="_blank">📅 01:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107968">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jnoe_PIkCFiuBUYPwkvV6jZROFp6mTityO-IuoWA__SoNWvRGjcefECjbiVgnG1Dm-HB_XTuEVGJsqxIrSoFw9hnRiQ1zNvYsJ58VFT-hMj7JffoblYYCfoNkl1A0UGK_ly0kWFNETAhmXAAq2riGiMxAdI3Kf7CxD8TVUO_-dhUAJ2uaDOfRAn2HEjXpZbwE1I0I-bgJKwqByBHK5t5EGN6LEh626vdoSTCOqJ-fldG5_NP4hffnKflecwOmfNGS13ZoLb5rYoPooDG_XKU4ikRHtauOKqayb8aESduzJZagL9Ivp_4w09nYkFAEV_uMQSt2UCAGQSTdjqeVTwCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
آمار فوق‌العاده مسی در ورزشگاه مونومنتال:
29 بازی
⚪️
19 گل
⚽️
11 پاس گل
🅰️
30 مشارکت در گلزنی
⚽️
🅰️
✅
هیچ‌وقت مسی در یک بازی در ورزشگاه مونومنتال شکست نخورده است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107968" target="_blank">📅 01:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107967">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=Hweu0YNrk6y7VJtWefdta6hw9SAhRgFuDGC_2JLBdsiZv245t4UIHmO7KFHHc01LNn5iRu_tCsGb8f1vFcmV0xkBa3RfS1fk9R2FyT4DJVwVvfk68FcbD99oaPmZntaIJI4oSjE_bkiTxHZBmGSBwNxTzko4onkVt8vTmlcZTv1eQjuCnU2ZlvtPKJN_ksfqvb9cxhbZJNbNmG1JteCwou4UIDQdaxAAJ0a_jE89dMbGsV6ThdvmNE24d-BP_0xYzq0QaZNga8ataQFw6EqsxfBmsfGaHbmfjf4wSuWSTn0ur_vuCeAtBeEJp52wAG9WJol7JteK5MK-j9o31ISReA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577bffe68.mp4?token=Hweu0YNrk6y7VJtWefdta6hw9SAhRgFuDGC_2JLBdsiZv245t4UIHmO7KFHHc01LNn5iRu_tCsGb8f1vFcmV0xkBa3RfS1fk9R2FyT4DJVwVvfk68FcbD99oaPmZntaIJI4oSjE_bkiTxHZBmGSBwNxTzko4onkVt8vTmlcZTv1eQjuCnU2ZlvtPKJN_ksfqvb9cxhbZJNbNmG1JteCwou4UIDQdaxAAJ0a_jE89dMbGsV6ThdvmNE24d-BP_0xYzq0QaZNga8ataQFw6EqsxfBmsfGaHbmfjf4wSuWSTn0ur_vuCeAtBeEJp52wAG9WJol7JteK5MK-j9o31ISReA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
زلاتان ابراهیموویچ برای تماشای بازی وداع با لیونل‌مسی در کشور آرژانتین حاضر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107967" target="_blank">📅 00:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107966">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=Jgt-9Xa1uZOUYD2FuVeJNjy0jogYN1zxAI3UtaaQ7XlPIpbJLHY4sOvjMyyWiqye4lHwRtKhaiLXU9f5oDQ-KXoa_vtEpTHoi8Ex4MZpcyuXnD4LX7J5dojZxMtqpgJjLn2_f14XEbmn__Y-_Ii4tFF6gglMi3XtLQ7-IUZwwVANSlfYB4nR2AL0TU-yhqDxZreH6TusMEFePPG4EGsLpMhSzRIgZeNTDWuVP6T_wLKgUk_lEnTOl2wJe0OoQ_4FQAm96SwDLPBx7xFuhhxj4CJJmjKiljxz9A2a3DlLqGhPKRN2CmiPPO9_NXdGIq-cbRmQKnoKYh7JopARXYYeEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b38517c17.mp4?token=Jgt-9Xa1uZOUYD2FuVeJNjy0jogYN1zxAI3UtaaQ7XlPIpbJLHY4sOvjMyyWiqye4lHwRtKhaiLXU9f5oDQ-KXoa_vtEpTHoi8Ex4MZpcyuXnD4LX7J5dojZxMtqpgJjLn2_f14XEbmn__Y-_Ii4tFF6gglMi3XtLQ7-IUZwwVANSlfYB4nR2AL0TU-yhqDxZreH6TusMEFePPG4EGsLpMhSzRIgZeNTDWuVP6T_wLKgUk_lEnTOl2wJe0OoQ_4FQAm96SwDLPBx7xFuhhxj4CJJmjKiljxz9A2a3DlLqGhPKRN2CmiPPO9_NXdGIq-cbRmQKnoKYh7JopARXYYeEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دویدن مردم آرژانتین همراه با اتوبوس لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107966" target="_blank">📅 00:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107965">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm_s5BGj_WiQeU_AFjRHaSq3Jip6hDJtMd2psszSRbCXUW0zGBZFjABFxGKv46Jyu5zVCKyZmCU857EoSmkgXL0UYLeX8575fOCpfUAXSOyEtwK2dw1FPVqzsqe2bHCc8nCS11CtyV9fi5C91wkJM7VNDeZpVAwVPnQ8bDm23zGAzNrMM7XWoGV7asEkXtJoiQ1ZMVI_ZM1ir4ZiokggM2PXW9NeEmL0WreW3yAZCnXkYWFKJNuH1sYUw8dDcR_IewuDHFEFa8fFhK490ai2Qmm2IVG_suMq0HX1Zgfs2OqFGFvKRUREBiottWlwCGQsHYAYHB5-wV4CHBDgpuN-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⚽
رتبه‌بندی گلزنان لیگ ملت‌های اروپا پس از پایان هفته چهارم:
🥇
هری‌کین — 6گل
🇫🇷
مایکل اولیسه— 4 گل
🇪🇸
لامین یامال — 4 گل
🇫🇮
لیو والتا — 4 گل
🇮🇪
تروی باروت — 4 گل
🇸🇪
ویکتور گیوکرش — 4 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107965" target="_blank">📅 00:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107964">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dI3MRNsOJGWmGFT5mtLlCT3dUctXNPqKH6IMMKEc8xDhIwUkOZPWo4IFVzJwNfcEZ4_KHglocJrW2FvOJAQEV5_oDC92Y1aiyEJxvGRvJtn3DINivanMBcyaRIca6Wc4rzf0ZeGPk2wqA3gfa16MzW1kzH-NaTHoLvZU0Ovkfp3IRo5GnDA2e7S2gObrFoq0IU_HTK7owOfC0yVOD7SKnxRglkjPmuZr7xeSfEZ1IGuGG43Ej6xHX0PDNLlubOkQwQrcliE4qo4_rM448P5HE0ftIBQMNrSHIkB-05rrgfLxA-jKwnB6G2plPBfR5B8DVd6XHLwSyJ0QUV5Vx_EtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره در راه ورزشگاه
😍
😍
😍
😍
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107964" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107963">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=pOqRQ9jgYK3rMyMjMZJbKcb7sNtULSeXglZ5hg5Ojcqhygh9ZMPEw7Tcbv-i0s3Gaor80AYuqVLXzwLBSOtAmjyjqqlkyIBdDgsPEB33jIsC-G6c0sAPkM5T0L2iCyhoSTK4hvMw4rqQDDHo6HDZwlg_q6t_r2vjg7ssZKknbxU8L3PStakV_FZb4XRA4E8KsVVRtk3vHQ_cCCD9QLH0Xvx72Dig5H8P9l18MAq2QR4KNCNDKFogV7suUttRTPC7rc3B337YAA_HWBaRiO7VbbsheytCqGhTYrDYQi560yV7soSQPSwuTg0VGGXQYaZCJpctXtViSm9UU9corgVJZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=pOqRQ9jgYK3rMyMjMZJbKcb7sNtULSeXglZ5hg5Ojcqhygh9ZMPEw7Tcbv-i0s3Gaor80AYuqVLXzwLBSOtAmjyjqqlkyIBdDgsPEB33jIsC-G6c0sAPkM5T0L2iCyhoSTK4hvMw4rqQDDHo6HDZwlg_q6t_r2vjg7ssZKknbxU8L3PStakV_FZb4XRA4E8KsVVRtk3vHQ_cCCD9QLH0Xvx72Dig5H8P9l18MAq2QR4KNCNDKFogV7suUttRTPC7rc3B337YAA_HWBaRiO7VbbsheytCqGhTYrDYQi560yV7soSQPSwuTg0VGGXQYaZCJpctXtViSm9UU9corgVJZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه‌ای از دستاوردهای همتی در بانک مرکزی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107963" target="_blank">📅 00:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107962">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPVhDXGiX7RjWMxXlZs-HDzPquIE_OubkpaNUNR_Lm3fzuNGjplRivntu8kYSw4tOLTaw6WmXC3YhrJehEU-NqyYOK-ug8x8-Wleyk8b4XntvmB9gc0OwbKGwTm8_IhOjMVa_E0iCqEiHs8pQMsvltxJHCgU8OMOYGXKI4fFVZS-zU-5uDtkbYi78y3ekhqhp32M0xAduJuoqL2biK3XKFkEeKXWVwD3qLJug05il-E48ad3DR2ozQxtAocqkBSFbo-nQqoousIxf7W1_4z1bOGpHvepzIGnfh_tI6edUrFFFwX3bGnJU9kkpVoaGQR6WI2scVfd-Yiinz_uOUrdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب تیم‌ملی آرژانتین مقابل بنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107962" target="_blank">📅 00:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107961">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5uLRowWVYa72W6iAs6cbne4sMTBMnk_BATsj-S26RDlyltL5pVLfR_8Sk2gn56I6_5zN_47RLUiljrYBIqZbaWjO7iMwGB1XIA2a6jj-rWfPLENdLl-ErxNReNGh7pYOtlP0NCdXooYO0TDyZzJaDbtnt_Y0rlqtnmjfLXhl9xKpYf1TFP77KHqYXSSCVEODh67r5JXDYJJ5-GWmvxs-WCKrNR_tlxRYfKmqbBAUhPPutq5N1HuwtFWkr5A0TeNlL_izD0lPFWUAn6UN0FkU7Ko6AhkLaLV6x0CACxzuDDMQTr4wJU1X8X8lkkEVC4S3xlWPDZsPXvJaElENOJg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی اسپانیا به مرحله یک‌چهارم نهایی لیگ ملت‌های اروپا راه یافت.
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107961" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107960">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shatel-VPN.apk</div>
  <div class="tg-doc-extra">58.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107960" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فیلترشکن شاتل
🔥
✅️
تازه نفس
✅️
تست شده رو همه‌ی نت ها
نصب از گوگل پلی</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107960" target="_blank">📅 00:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107959">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
فیفادی کسشر و طولانی سپتامبر و اکتبر رسما به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107959" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107958">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=dboQmQZ98vkQk29VC_l1GrhLJtbTd9tixljxTcQALU1ugLNyV2VYdssY8mMUPyoI74O2uZQ-jVM5Y1Yy1sy_Yx4K4NxWx2WsP4k3gbNKOVnAYvYBZZpELaz1GJyInq4Og9tlMUR2333q94kxUbxICRP_NC9IZvc6Nz9j_kF1VSOIH2fYIULd3HhYJXXe__rEIWg3NTnOM7t7y0_TOicbeMD_4kQfeyUwZsOduJJpvQHzC6gsfp5W5HIJfgqwxXDxBUXwAS8gKOHYXY_uz3u_vEWV5t3BvdYHC4P8dI5EvEi-02Vce_yOdQymHW8yCOAEhvCTa69SzZQgwSgkOK1d1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580bfb3d91.mp4?token=dboQmQZ98vkQk29VC_l1GrhLJtbTd9tixljxTcQALU1ugLNyV2VYdssY8mMUPyoI74O2uZQ-jVM5Y1Yy1sy_Yx4K4NxWx2WsP4k3gbNKOVnAYvYBZZpELaz1GJyInq4Og9tlMUR2333q94kxUbxICRP_NC9IZvc6Nz9j_kF1VSOIH2fYIULd3HhYJXXe__rEIWg3NTnOM7t7y0_TOicbeMD_4kQfeyUwZsOduJJpvQHzC6gsfp5W5HIJfgqwxXDxBUXwAS8gKOHYXY_uz3u_vEWV5t3BvdYHC4P8dI5EvEi-02Vce_yOdQymHW8yCOAEhvCTa69SzZQgwSgkOK1d1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107958" target="_blank">📅 00:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107957">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=lXHxTrLp2cuA2F4b4ua1GuarMbo8ySu-682vvFUOTdgxV5b6qcDh_cP_f_SUU_ILFaz1mXAj19Lgm4zdhyujRa8jRUoob0tXAggfzRCQA6-qdmhUV2_-snnBULrH-Px4oopzZve1flMHuBx4tmOs3zE8gNjSDcurzmoVOAUNDx5cjo4Lwrgy-4c9c7Pw5u-b8nCwhuB7HghR23glsj19NspFH79MzeIzemSoNy-WFL0w7hK8IDR9gdW7Qeq1OIagqdkCEY1bI8IPD1GyDmWdG0dHSTom058MOfqxdV5Qf4ZQIZt2Jp4PXonsoIQEnoFiiaWKbAl_fYzNMclZsUewig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0272b88.mp4?token=lXHxTrLp2cuA2F4b4ua1GuarMbo8ySu-682vvFUOTdgxV5b6qcDh_cP_f_SUU_ILFaz1mXAj19Lgm4zdhyujRa8jRUoob0tXAggfzRCQA6-qdmhUV2_-snnBULrH-Px4oopzZve1flMHuBx4tmOs3zE8gNjSDcurzmoVOAUNDx5cjo4Lwrgy-4c9c7Pw5u-b8nCwhuB7HghR23glsj19NspFH79MzeIzemSoNy-WFL0w7hK8IDR9gdW7Qeq1OIagqdkCEY1bI8IPD1GyDmWdG0dHSTom058MOfqxdV5Qf4ZQIZt2Jp4PXonsoIQEnoFiiaWKbAl_fYzNMclZsUewig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107957" target="_blank">📅 00:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107956">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=NwUR_q-PcVQSBbMYBRz3nBXQMgEVG48VlzhBAktcevEW9tQkFhjf5TYxf_BvlNlNqc_Pp8Oqx_I55RKLZDgpVZpXxS93UfiUDpJaOISNvuW8WKXtYMC3-Xw4Hxcp8GjbUO0Zg-Gceh_VXPZoSvUCOl3In8pcrfHfTDzGjcUTS64xaWjFSzKVgcsQCfb5gp7ci1w1VGbTD-PkhiS4ZRHNmQUM0ETmvEXrjkDnAX32Z4imauXkGHdj3H4cEtr_OtmQ1_sKtaM9c_FKPLYbwgksAPl0u_4rLwvHSplTLOVRny0svYCLQf8PowV-hGy2rsd5EaKbNS5HOhIO4Uib2-CAMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7164783.mp4?token=NwUR_q-PcVQSBbMYBRz3nBXQMgEVG48VlzhBAktcevEW9tQkFhjf5TYxf_BvlNlNqc_Pp8Oqx_I55RKLZDgpVZpXxS93UfiUDpJaOISNvuW8WKXtYMC3-Xw4Hxcp8GjbUO0Zg-Gceh_VXPZoSvUCOl3In8pcrfHfTDzGjcUTS64xaWjFSzKVgcsQCfb5gp7ci1w1VGbTD-PkhiS4ZRHNmQUM0ETmvEXrjkDnAX32Z4imauXkGHdj3H4cEtr_OtmQ1_sKtaM9c_FKPLYbwgksAPl0u_4rLwvHSplTLOVRny0svYCLQf8PowV-hGy2rsd5EaKbNS5HOhIO4Uib2-CAMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تنها سه‌ساعت تا پایان افسانه لیونل‌مسی در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107956" target="_blank">📅 23:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107955">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=UVTvJfwCQ1GLVGTnuV5V2thD4dz5pkPXk4VmiJI0f41PUsaReM1md7CAO7ZPvnGNSFOAprarcws2vd6iNH1XKSPlpTMzHUsl9WugljDdTJW1cjbSrxE2QCjwF7tdci8Rc3Zc-cWQTOcWYQCAa2oUt20s2OpmedHOnSS2wK5PpGgBCBzzeyuRLxYdBd-Fay2VEI6aMnCnqo3VV6pIA9TpFc_9QGGjVQWhgNAVPXZHn7v6GvbsCdFmvSnRbo6Va-JUfB3lihjr8Yj_4VtX0rSyD5Oxm9BAA2IrlAdaMoz2S3hlTG5Okvlf0rzg8pufMgvCM_Cmlv2gmQevwqKcwqOSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0fbc6d16.mp4?token=UVTvJfwCQ1GLVGTnuV5V2thD4dz5pkPXk4VmiJI0f41PUsaReM1md7CAO7ZPvnGNSFOAprarcws2vd6iNH1XKSPlpTMzHUsl9WugljDdTJW1cjbSrxE2QCjwF7tdci8Rc3Zc-cWQTOcWYQCAa2oUt20s2OpmedHOnSS2wK5PpGgBCBzzeyuRLxYdBd-Fay2VEI6aMnCnqo3VV6pIA9TpFc_9QGGjVQWhgNAVPXZHn7v6GvbsCdFmvSnRbo6Va-JUfB3lihjr8Yj_4VtX0rSyD5Oxm9BAA2IrlAdaMoz2S3hlTG5Okvlf0rzg8pufMgvCM_Cmlv2gmQevwqKcwqOSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
💋
پرواز لباس غول‌پیکر لیونل مسی
به کمک هلیکوپتر بر فراز شهر زادگاه وی ، روساریو ، قبل از شروع بازی خداحافظی لباس غول‌پیکر مسی به پرواز درآمد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107955" target="_blank">📅 23:04 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
