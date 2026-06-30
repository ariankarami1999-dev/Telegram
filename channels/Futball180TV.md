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
<img src="https://cdn5.telesco.pe/file/Nc-cII8i0XDz84v1XFyEo6I0MXz71hzZ91No93OOe6vtbiucK4t4Cnmjvc7yPVp6ph0b-u1hoKU2vDMGSzw-2Z9nbyNZp08M4Cyqpn2-WV3jB73Pl64FhbSqNn_AUvLi0wqAQFOdl9KhCeNXJD-F0SgPRdaWtpK32KDbWzSr2gw6_l6-sy0iVmcNmlTkpIoWw9SpE_Bo4L8P5Y8PGcGwV4qNmxiNG-sC12QvjqU498LZYEUjXI26vkU9JE8UpbvyxdCRng5dCh-X4G3Gihott-bMgqQWMdIxFut2UeYlEknT0LMPZLsioFs8AT0SoCW42nCcZkod2-I-NEd13LcPXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 676K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 18:41:02</div>
<hr>

<div class="tg-post" id="msg-97162">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMUYFOw4KPTT8Yf8RVt9hDTy9sIYPuzaqBDiaRlay392g6_FCpeDWyP9-iK0PKY8MbSknOKLK-rPt-CBzs9sZRVZKtIz9zUk95Ay8gc7e6Rqp-1wpz2bKCYO_dMkBNx2tFy7QW_t9TTVDX26d6J-EPD57A-7eLv71JqzzG2lzJwXX6OpGAaM3pbgyK1Sqevr2ogWk5zXwye7azbFNqo8hVzpHStyyleDIO0Za88156IqtowE_h6YEK7mJLqLgN77TzSLwH_ONuezKBYdiNIt1gvUyXnJT96lst20-OWi9aLj3NNB2vQuF8pse2Kim1uEyOhJHpDIBHA76OlCMN1XBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فووووری
و
#رسمیییییی
؛ با اعلام باشگاه بارسلونا، آنسو فاتی با عقد قراردادی دائمی به مبلغ ۱۱ میلیون یورو راهی موناکو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/97162" target="_blank">📅 18:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97161">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erF3-LiHJ36KyBnMHlt-ECso37k5UpN4E2mJRUSFgYqsSDgYlDGIBrMrQrVPPkLmpAb5XnTXW9g3Ungu1pySn1cj0ufuUzRN8qKb3g_bxZR0Uuv0mgPj54Qf93Ajmv9TjSxEIF4DUW1Tfv5Se5RonKqJ14COTL2RuCdkPmYxqIG0VeeijSgqNqsrgT9iLzYfZ7VRQ5O-wfWh-OJ-iW_AKRFB4TLxnkIOi-M7JIlMj2K2djePapLcW-nC0AOCyQbwkmVpWXbvevc7KbWN1VxCQLtkJ-r5_6daEPTVzn-74KXAicRQqBzJOSZLuCaTvS91bTMrLYqDZmwYFwZF5oV_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
؛ با اعلام منابع خبری اسپانیا، باستونی ستاره اینتر در آستانه عقد قرارداد با رئال‌مادرید به مبلغ ۶۰ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/97161" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97160">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO0kFbOL052jYPnrwIcMFmNcMk8s3C8Rw6WhlzDrqe15gJ1xY42Ug98Cee6bklDM7Yhn3WaeaDuU-YEQGQibrIp03n5EPn7a31X7Gb3rSVB62DGv5vHcC8yXxC4SSGfrZcafhi4u1UPSe6NcQIpkxW2wVQ3sPL8Q2H1qVO-aJQ5Xa417Ij5DvESAn3qXcvZMAK3SVZwav87DqYmACNbH2dX7nIaF2xaOT57-V_D7Aqad1UUbrYwGFJeB4iSCye-p8kFZbFwkVaYJu8j61TXErhCXY3OGfXKZ_7tX3uYyhE-ztAyvxKnUAmWx7EyosuIjCM16pq5KySiL_o0MO9Pckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جای خالی ژائو پدرو شدیداً توی ترکیب برزیل حس میشه؛ آنچلوتی به خاطر دعوت نیمار مجبور شد ستاره‌ی این روزهای چلسی رو از لیست خط بزنه و حالا توی تورنومنت مهمی مثل جام جهانی یه مهاجم شش دنگ نداشته باشه.
درست بود وقتی مهاجم نداری نیماری که تو سه سال گذشته ۹۰ درصد بازی‌هارو به خاطر مصدومیت از دست داده رو دعوت کنی ولی ژائو پدرو با اون آمار فوق العاده رو نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/97160" target="_blank">📅 18:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97159">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=kDOOTl8_jHUXesZsmrhnLFfjos67x-CSWjalA3o8wgH8QLKz_vU8xokcMU3JgFUW1vIg4fx6r0Gpv0jeY2qlwZYdKtdn8TCa4DkhkegvPKY_7jpSMJavecKDx0OwRcNpe0qVkFe1U8GPwlmglYHZKAZpa75-gBso8K5bXJU2wW67avKZfjFfsydsH_urc7g7nZ900lzrwmQm94ACATDaPRFFphG4FqTKEvx7LR62hWKj_gTV_o4TJJB5sdHH4p-U3iHyZQgtJPNAHZyWTVOY-wIwOTuf7DoiIppW1ryf0Br7EwsbLr2wzQ7xqjTAX7lK2r-P1nCZbvQrtEGsb6TYEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=kDOOTl8_jHUXesZsmrhnLFfjos67x-CSWjalA3o8wgH8QLKz_vU8xokcMU3JgFUW1vIg4fx6r0Gpv0jeY2qlwZYdKtdn8TCa4DkhkegvPKY_7jpSMJavecKDx0OwRcNpe0qVkFe1U8GPwlmglYHZKAZpa75-gBso8K5bXJU2wW67avKZfjFfsydsH_urc7g7nZ900lzrwmQm94ACATDaPRFFphG4FqTKEvx7LR62hWKj_gTV_o4TJJB5sdHH4p-U3iHyZQgtJPNAHZyWTVOY-wIwOTuf7DoiIppW1ryf0Br7EwsbLr2wzQ7xqjTAX7lK2r-P1nCZbvQrtEGsb6TYEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
پشماتون بریزه؛ سر صحنه آخر پنالتی دیشب پاراگوئه یهو تلویزیون قطع شد نزدیک بود نصف جمعیت سکته بزنن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/97159" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97158">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=Z--8mK1N8zk_TP7E8LJuV9kz2sEqNlEGk0TETx1bgetyZAa2w3zZsRjfZ_GfUboeWDN00vrFuDpAiL2qentDHwJD9Wic0s3hWEeG1dQ3UetjvdE61hLDST7gQ5gjIphFdbxNfDF9H5gwx54MiPDgcQr5RvraUIG0sVf3Yccl-Q4y0ktTESJ9edMBHFd9Wa6FXLX9YlaQ4T9hEdmrssrF7nJGPTQbBgd4Cf4zZeV5xUuSDx39d0jeDE2gR-SN7KIzEr74TCH3eCT5v09U1kjVdFcndB0liCzGcN8jF1x7ByTWOZ85fOAbaEOvTI7Snc-AxDTj1RUHOigM5HdbsFADww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=Z--8mK1N8zk_TP7E8LJuV9kz2sEqNlEGk0TETx1bgetyZAa2w3zZsRjfZ_GfUboeWDN00vrFuDpAiL2qentDHwJD9Wic0s3hWEeG1dQ3UetjvdE61hLDST7gQ5gjIphFdbxNfDF9H5gwx54MiPDgcQr5RvraUIG0sVf3Yccl-Q4y0ktTESJ9edMBHFd9Wa6FXLX9YlaQ4T9hEdmrssrF7nJGPTQbBgd4Cf4zZeV5xUuSDx39d0jeDE2gR-SN7KIzEr74TCH3eCT5v09U1kjVdFcndB0liCzGcN8jF1x7ByTWOZ85fOAbaEOvTI7Snc-AxDTj1RUHOigM5HdbsFADww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد باخت ژاپن جلوی برزیل، اسپید رفت که یه هوادار ژاپنیو دلداری بده که طرف هی داد میزد "مسی، مسی" اسپیدم کلش کیری شد و گفت خفه شو مادرجنده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/97158" target="_blank">📅 18:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97152">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_jpV-Oj2rIfwDy81uPHJCwzzaIdYSiaF2V78BaZvAK4lQPS2m-IcpFgSrgsLuLg7WVVtIMQ8OChsNeZn0LAOqY-oyad6c_JICNY9YyMYOjosYWjVnLwi2cjxCEOEd1Atkke8WjVuxRfBLuqI8cxCPrL3Mm4Y5RW4mKzlf_Vsp1HmYKi-Xq-KLJf6vGu2fovQk5JtiKCaAmKyUaWoycXZoHO-ORJdZyQiAhu3kh7Zg1lktoIXTZjZ888ZiZBRI9l-V9LUYF02SUlmwY31Tjf3YoxkQKQhxWO0S8y-NVdqvz849ed1aJzknrAH5DnEa948Pk575qenvpFvIfboHT1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xr7mDNhh5tU9MrH9aptILSx45JoyfoEuRIfSiWUkMBNKnv6sVwLMv4rYw3k0tgRA27yZWA3U4aOorvG-eLVZ-w5gXxTyyjf0DZJIc1q4GoRYj43kJbOc-41ANb8HYFHHqyDbFPPzLpdTfwq3X9EhWLvocYgQ8kQ0c7UcFMV9oLKGE7mS0dXN8Y4FCz-Z-QUlhMHK2kmih5RZBhi14DIRNIGXyWhRqF4wYjJrzj8Fty9yAu13d99JYENF3tsCz65Rc3npcujyIdWy6AhVPX2iqfHBSbw1exgjqzc1mGdswPKrKcDqiFO4hH378IhHzk3G-NmroGxjwYSiXOqbM8b_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et4vyubH4Scfsze-GX_R_OVEeDy0vaw1fEU4APsnFXezwXfr957FkNpG_K-WGAJEcWrIj8hUzs4G5vdqcGnOFqpDVUmlqNO3P5RQiBLqWVHeZEurUpjmBjFCVXDg8M8TmUKD3Xj-NRc5rnqt_ndwhC8oqCH6kc6wDG_oqU9_d46pR8e_n7eoPv9CLs5iweKGmgn5hNRQ5zniGlmsXO8BqFdCRDaOd02Aub3YJzOfbW2ELaPL1pMfJakZTxTC6tkoea9mMeFeX8SnEPxjhYmrehAK8e9ERUYsHwCt8PVDg67D4TatNEoQb72_6rOIpPDVZR1pvu48JEB8uNUMsd5SYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ffk-j_2WMb54LPvzQ5MVK21bRhntXjK83J8kv3tk4WL_HlZQGLdJoOnuq2GVgTgzP6xYOjt5bWVAE2vDGZLVsmpQd0qEVtR7ii2XySB18ikx3tn--jJtePyldZ275VxqcCJ8AwadmOzNBB8nVsgpuDA3H9Egm_i5-Fn1P3Tfb_JmJtIASZUeM6QUYmZrfd7xQm2Mi5OmnR-Inz2-hgRp3VwhID3bE5WisKPbLtWcihoT4ukDk0M1PuL8E6VGc7etVEyW7U8T5pZ5Vhbm85hTQpm5czLwVr5G3SaZ6LxSG5Cwo9PlVGrfeuX1K2OJDLZip-NnLrqQ8Ggm3POlWoZFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrCbZ_nUnuzgc492HhxgBrcH4JIqSMkPxLJ8DiJWsp7MZPo4JnHgMqQeS_R30BapSiCEM0YZgBSZd0vnkEurmdtPSDPWvkxywkesCGD67cpjDF0PBRw-2rv7jNHvle4NuxJ94TJASEPqUH7zaW4-8_9C8GHClzkHcxC6mNs8v8RJ761Qaw29gQ0nvkuwmNV6730yDhnJIm0zjNN89IrbXwd-7bAg9HOdq_uQ9KpMEAt6sMCNt-B8Edwc_3eV0uLmCgse3fb04Mg6pQhtlqgcUlSPcRSjn3Eth7lDY7r1ZOr5Z9DTVMLsyWxz0dBpakjHx343_WpV2QYgBa8bhxXi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJOeSzlHYJwiZHjtHIfmWLyS6fuBwG5BezaaU2NmMboqwR_Exstds4stCpsSOF5sbmrV2L6VVG3PRaSKPt70kHTgR3EShIthkTelzOwKHD61Ala9w_0wi2XviA0HfoFUgc6F6F8GOB_aREGx0cYnd9qmglQinYOQZSjYzkPtm6FNpyGH_N4DRx7tObwaxXBYbIIvXYxpz7DsOnvqKgsjghws34SeHGwnKLFd77T3gowXOQMDIEszO4MLcRbZOL7N_uprApi2ZIZFO7X6Yl7IA1v2Yp9yrh_vOdbcRgp9xoPf8rtGtzlkKhRXA45KVbF3BYXJtgLnmIIY77MQ5b0vhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فضای‌امنیتی فوق‌العاده در استادیوم‌های مسابقات این دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/97152" target="_blank">📅 18:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97145">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hd1P5st4TeRDZxSFwZqjFistvV2rw1joUqyoN4JYtzg4vSM_KmiKe-EfvjMvcmQpxVp-jSVPFzJu_A5oFfB1DszK1DOkw9BRwDRTC4UVt6H-o-ceJdzI55iqLbqMqjUngG6IX0TmsTqx--fjl5cqD71dVaL7niqqDx3FVz6qdCpHCCBJhRxwn-XYUczJv_fO3GlwZ-xFTvPtw5I6DNYypoWjZp6yNKuPd7rUkn507R0jntz_HWVnh8GUrYVh1az51xYFi9kwx1fdVtarBBx73gx_QhiigTyBggx4FLr09kqDYc5se1e6evmdfZ3d56_723AR9k34-KY2qpJDaXTZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAikrWcrtrM_z29MaXtb7iKxNMQyJeHwY8wWvEtK5c3W3fKBRehxQs9HkUg6o-CPVNajWsIipeqTHUBEBUYxEiYwrwm94YpeslGvV5Lj478WPO8-M1g6uu65BCiezmSqyKE_AGYNOuTw8iIlBLmdfz8v4pDAdP8OnOT9qYbj-99hHMJLmFCD92-lBhJiIOWP1nXko_CjsBJSaK3qXPLQcR1Q5iOP9O2GIGUQPcmIiqUyNaJbSxSU3wGWbcOIKdajVz0cm3mLvQtcpNWI6zaY5OXGqt-Zy37Mt6b54bHR1RCHDUN1MoucmQssty3GI3cgTxG8xx50rsryhAMwb5TKvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjcUdfBvg4hwo6xz47bdMaEqZLz146mbhbvreg4cCgVUNfz2sS8SwnffohVFjCTpwaQhXtQGUyIHlss4Z3QQE2ROQoIhwIxJwhmn5uNLWm9ymYImylsVC4y0cf8rrW5SC0qskM7mD18q-REhQWf0tahaaibUQ3CCjCeph2vkQSilOTwfFP8HxeZ0u3D2hj7poQiwfXf3CWSv3OPBd6gAV4aBMIrY6OGQLqxTw_YBNrJ4j0QojhmInLlYhbCx-9698ip76UCrkefVYSNkCKVWljQdYt1YeAVj-c5e8AXcD5L9uyqJ-SxuBcRlLLWzmsi0vg56jxEsPLZPTQpDLG8WRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsCG14gT-cr2-1qXtbel5I8RUmwRqHUloRZcXlcLeSEiLiRazGQoGRWaB2jCTI2XgEKlD2qESzYE0S8Sz6dRyxfXZC0DxDQ7vIXlE5v-HdYOHAzRWKSc-xqLLu_nNRF8Woj0GuORGUR5zCmdOlhV2EJvRqOTC1lLmdljCA1bsiuBBmWJbf6nBCph6FBPFgo2iVyeIoikR79zFHfpthqWG-HUggN8IyU-HjaO8mGhwLGpJDpAIF92hQHfo5HF6PyjbJLoUiQgbNJa7niQBCJbFGa2HDIK3HxjOyF13gV-KmNRogRDLYwlTufSCJR8bkH8nBPWyE23VgqZVM24NBwcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9-WVK_Cqh2vfGtRoNeutZx-26UVn78gn7m6oKywvWYYwX_HeXCxq1qQQlQb6p8R722FPa61ejsy14OxAJogIp-CA9IgyDz6Ev3NOiAN_ue4c8xwenL7b1QFv3DF7zs2HQw6cARuUyjGJ6jVtT1SBkRy4gfgRAxI4O2RSkHk_EWcN7WVkQF6be8E8JKLWV3oDoN7EnBorXTZF_hzIL5RPew0esg9_pn0ZKjpmRmPXhNMNrXHMplGleFxFuc8zDKLXKsUxPGaCgIv-cjBqfZoZC4AIIg8f0nkIyhKDJkKzzm5ywpjdd_C-zb7KbzHH0g5cV1K_PaV4S9zdfHjZF9bRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/api1yG50cffQvSM8KvIRh8cPPywIlgTcpYvoI1Yz6cLlRl0j3ShpWI8Qyp9TCQNnZeMi9SrkOpOkpxZC5nSLRPkkPKbuKYmxfLvT3o2lhcfgoQTNq4GRrDNSay17kky6FFMgCxTBs11tr0CwcGg1tzLyS6mUC5cdIuczq99T4iVXFwIPDbPTVmJAez2hm1g4qdLxpxI_yiNfpRWA_uSKPxsFR0bR8lIwE0Wem_PzhC33uMs_v71axgUcmdQz-xGgTLPo01S_p4b2yFWuzD4o_vUzBxUjX9sCs1bU7XmkL9c5tqoKNJnvStYYjrDDoy7stWuH2xF56AFVgjk0E9Usdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WO3GA46_JNqh6kO0sh5zeXoWIa5l-I0VdR2GXLIoDpRkkHE-6zWscCfS94ocoT_E505ME_oSotIYbkyBUMG3DUZVf6DUfoAOg4AiU0oPw_8_5qB1phYMz_EO_8FFJpXk9LmwFiGEw7MFraE9f8XLXolG74i6bRT-j3OF6tmCEpNHZXhb_RgnOlv257Y2g1-IFMybk1ABTVEbbnevfSGjpRaikMAV8lpqFy6FmMkw8CXR3FlwMFIzToCbaS_FwqNqdAndeSxvwHoo_2w-nk-77pJx60yOaYbYmJUypT0x1niTLURGtKZkRi3ax0_Ch3rQDn7ujMrJiYTaFaoomxhMlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
همسر ریاض‌محرز در ورزشگاه‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97145" target="_blank">📅 17:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97144">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRgfTSxYVMPQGOkBXVm2b6SIK1_vcoMLIHMRJYqrmmtMunsr0Cfx3CTNe6_ic7VuMUD0oOpmFYGrVjkNkiVaRHAC5cj56BmFfH88ncR5mSVJAQZIDQA79Us0kNkoE2NZf0BZp4lwgXcDM4mvSbJzX48J0SQQTg7A90FFM6-b2PD8fAp1FaUfa0ow1p6pA0DWB7VHj-MPpCEEqZMDQuEfsWlGm6HARMqE-nG9Rjt-Xi4UMEPV7b2e64UzRhpnwEVRPt45lwMuMpRk4J3d4NnJQxPCpJFOASKB9wnmoxGC58NNxTVecGtOsFrt1jVMAgMIH0-tO4Ii1O2X4nU5UxOqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
فوری و رسمی؛
گونزالو راموس به میلان پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97144" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97143">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEEOATv53qeVl9LsocCFne0yfUaeucyr3r7lttOMwwxfhw6k41-IS3ZdiCEj5lYG6iuQbu2PL4fE8w8v-E-4n-i2I0TJFmhKd400NpTY7RbR65eYdl6CcR8QLd7iU0ALcmi4mTo3iAermeL51A4Hxs60VHYQ5TtPvWRxVopmjqtUl9QS8XKOyyRZ-Te6EwTbAZe2CEvR7QM4AOwARZlhmTikIBTZt6-6Bb-pR02mmWBbCYa5r4zBj1I1xhuGdvlFXyBLN0ZdiJmXRig8U2XKsSaNI2qp37_iPobJ66dVLvXhhgNywOLXKnC9gn3LEQ-oHI_HCu8LhVhGz99PbEfvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🏆
رتبه‌بندی نامزدهای برنده توپ طلا تا ژوئن ۲۰۲۶ از نگاه‌ وبسایت Goal :
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین.
👑
🏴
🇫🇷
دمبله
🇫🇷
اولیسه
🇫🇷
امباپه
🇪🇸
یامال
🇦🇷
لیونل‌مسی
🇬🇪
کوراتسخیلیا
🇳🇴
هالند
🇵🇹
ویتینیا
🇨🇴
لوئیس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97143" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97142">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rincd8t88bdniycA-fXI1fRf0fWfGox5vqV6FYZx_QQKWyHCTXYdUBeT15YlD_WNQFozddDBGQW-M8SaT7rNlYUemFuoClXlNJ24t7zjTfO2hw_0Kn6O4dFoe-Tov221NcgUvkFv2t0XnzjRQ6kWByolXDlIFqV_Vp9M2erG6yuhgtoOPMfswMJLP-6uKp0QcIZVbslKCJadQqIDS2N1fMmMLzGNpDVgnnLM2YHH19-tTVWrS7panpTNwDlRCdXhJhDmBhB53cxgejnoyt8_60oXKUjw2BztvAEybaDS_TT-7DdwxRZzLzdX6UhTYhj0rTCVc4w-C98odIul-EPafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
❌
فوری؛ فابریزیو رومانو:
فعلا هیچ پیشرفت یا مذاکره جدیدی بین رئال مادرید و چلسی بر سر جذب انزو فرناندز وجود ندارد. انزو مورد توجه رئال است، اما در حال حاضر جزو اولویت‌های باشگاه نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97142" target="_blank">📅 17:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97141">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1401efae7.mp4?token=RSJ7UnpvMhINm--NzE9e8M69VJNT7WrpBBM1ock6jL5XOg8FWVnAEbBDuoR2XqHdK6Zb2jLXA58y-2syLNmMRX1FYUM4Mf2vCoam_ND3LLjTDw4cIopT0ocovQC2gGLqVywKJywu4IloY1M1rzpjlDSw2Noo6DQg0sPcE79uhx-2sbkuP9wLqk8YIGBc1qK4XmltJvdvRmP485BCfGS1vnHgASfAX0mq9DnUcC12oD2TpZFjJHUARpDlnbF7ySssaseRA7NFkQXaPU5TJlRD9o-35cBRoaqUV_HX3p-GDVjCNUuurXvCZ3eWG2U_b92fuA2iBa62jf2O6S3U-tOGvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1401efae7.mp4?token=RSJ7UnpvMhINm--NzE9e8M69VJNT7WrpBBM1ock6jL5XOg8FWVnAEbBDuoR2XqHdK6Zb2jLXA58y-2syLNmMRX1FYUM4Mf2vCoam_ND3LLjTDw4cIopT0ocovQC2gGLqVywKJywu4IloY1M1rzpjlDSw2Noo6DQg0sPcE79uhx-2sbkuP9wLqk8YIGBc1qK4XmltJvdvRmP485BCfGS1vnHgASfAX0mq9DnUcC12oD2TpZFjJHUARpDlnbF7ySssaseRA7NFkQXaPU5TJlRD9o-35cBRoaqUV_HX3p-GDVjCNUuurXvCZ3eWG2U_b92fuA2iBa62jf2O6S3U-tOGvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
اسطوره‌های‌بیشمار در حین‌بازی برزیل و‌ ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97141" target="_blank">📅 17:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97137">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPeOHIeHAoY1tvWyutHxduO7QS4MAZDfhnzq61TqLtGyvU9iSVWgJ2uprgYoHXCZd0OxRMN1XDOmFoh_-VozUASP7JeEGHFwAUbD199FfSebvhrPZberHy1cJbjYuxDEk2Rj_xYQNLYADw339q6ZHOLW8EXhkpr-GvHOvXjsoqAN-lXGnp2KdWXlYfvPsYCHiCPw1nzD2rHL9t12Gd45RgY_zTSKNhU5LjCv5NeZB4Of-7Jz0H_03MM_990WKsqFvY0BJdKagwWudFeUarD0by-TkYlW8AAkQOmXewK0N46Vk355oYNsrnelkQyG7UyeVy45KwlVzXWQXtHz7wPZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOp7k142i_tZP0ayLa-mkuYsI60PNrA6dDJB_Jygganfs1nahKKBeMS_t2i2jROHSsCZjGOFO59aeR6jKpdjnhqC5SLISVF3ZJi-kfvCTynKZV4Hbhw1iyb2cryOqBDDcvxwxF-V8MGWp3QkeuMqq7QAn0CqWnMx-YGoAvPaL1X-gqLFycXxpM6syM7wvgd91w1I81LaZpckL3Oy_ohfCmJoKSfqsfIlo83YUggVbaUIdfzYq6Y7g4MkNgo22IQEa6CT8vnKNRVdvPUlyJtvhH6WqhIwrnJceQMF0NFinNog7DuQ5FzxmpFX1svjlA3Tl8t6ofEd5kew_9yKjWuC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMIdtgkgvQzBfll-CcMPTb5wNOoe_HNh2uXM4OE6zahAtnP4G4DTNpSgOzMnyFx7fJ3eufPy_xtgQw_vUpKqruIL128BgDunG6pBYUUS_ttcMoFh8DDoQkU0nYQw13G7oOscTXgmxOzw1bCt0QEewLVN_hOU57ZIGnzRLE2ozESHDyFWOmNH_ftn8aWysudMbgOeNj-04MrBV8jxHlaiAFNMSfVzie9bZCKc-RaxMxlUwUxt7_ut4dYSxceZo1GI9UPF3Cogv6O9bC62zWtEl2JoFCsymIYbt28kdOzUUBJW7GwllAnhcld6H_Vn5QtJFHnTvaWfxejSjSKQGlb3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMWP4gzYsztZ_0TBF45OV7Qn-WWlt435ddBVjwABPd8IWz9JcVFoLBPiSXG6pE4jA2DZHAH3tGeDizbxZcQ2snFaGO1mcUvM5lsa6qPYvQx-8f-dvOazFHDvB0uKY7H-433CKv0i6cbuAoy8rEa4J6lFWre5gNQYwXg1sqQ4t6K7nCyXgbm8D9jfa-jsYLctuexb5xibbp6fLLppcp7Hztzu6tzzbf5ny1jvrS81qTGjEGTev04w_n6AoCmdOGOJOStcpo0BprO-yUcobsKu1Iwo1zfOfux1sXuU04RAJKadV2k3Q9r6i30EGiXpX2MxNZRZH7pt65APqGT94U0KvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/97137" target="_blank">📅 17:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97136">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">😛
یکی دوتا منبع خبری آمریکایی صبحی گزارش داده بودن که جان‌سینا و زن ایرانیش قراره دو هفته دیگه بیان شیراز برا یه پروژه تبليغاتی. ایشالا که خیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/97136" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97134">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdHuTSvhtsckY9Cu0mhXQvHyGUtG3XTYzWBCZnaSBzk0ozncT_-vcryeh5Lbb1a3BswrSpoioQRJcNE7n49wexxJla2tt1dywG8iDLRx3k6JFZaTLlPJ3MZLFK3kQPIg-pA3cjvTbOPKgHk0aOAUiacee2k2hDzIOU95MaDJ7G4cnKTtWFJVw-mMOwtzJEtM5df8hx1k70XvNKRESGBjjWpRosKCy2sqo9FHf3LJL70kyMh3TmcxVa-kQ31rzisaiDVx1r421H3WRH2STnuH_G22NwYAA-6Qahwq_w1Ugoqw6GwoAzh7Q6N1F7hjrGrlWme0F1kiONVMLmNiSZgyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pklekeEi4EXM2-XhVb_TLRR4-z9Cn0u1w44dE8TWI5JDmfTjzxj-N-8VFQYZdawUyUJPl1xsiPTs8m8cU6NtjBJ74c0L25zE0MPh8VzYQPNWtPF-ctdpEJ3fh8pT0dSCO1DTM2FPfmzCeZOnL_O07z-vogVKjxSIBjtMUWWsyEhvt6iqE8QoZBtnFD82ABtPATTd44SraCEg56_mHm3FvczAkBRaoJ8maPHJagMlNQJEJ4YEoAd7wxnyyAVO5N0VIGdqE2Qnh_9igLYlF9xGG99RWMqw565pbQg4xEf2SwgABklfVt20bT0Tb8aZpDzvczQUEOfGiaFRlbfgUKTQhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهر جدید جان سینا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/97134" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97133">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c88f5b44.mp4?token=EzSdB-YJXWCmKf_fCF3gfOoSGMX0sr4Q4QIxypz7Gik1_FjBrQ0o8C1ABaCjnFsZaYg-kLjKcJT0ZJuXzB7MVmHy-PRsXIB9pvHAR7AGDT_xIY-0j-kgIWYr45LiZsf-AQjAn0NrChB3Bat1q28gsEab2XsBRQPJTPhggWoxRq4PJWfW9DVCK5_KNc7YjE8b7PpCesHXsmk9nrIwRVO21VaNV07kfhseK085XM40P_aIpxXZaNlVlPMC_FQ_a3AuBlhDlHpLwGj5dWAqByZ7wIQ8TUc67myI9mutA8Txifav3Lr6LDWzUHm5lRI_bgGOF1l9rgxhSqofI5qGWTWFpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c88f5b44.mp4?token=EzSdB-YJXWCmKf_fCF3gfOoSGMX0sr4Q4QIxypz7Gik1_FjBrQ0o8C1ABaCjnFsZaYg-kLjKcJT0ZJuXzB7MVmHy-PRsXIB9pvHAR7AGDT_xIY-0j-kgIWYr45LiZsf-AQjAn0NrChB3Bat1q28gsEab2XsBRQPJTPhggWoxRq4PJWfW9DVCK5_KNc7YjE8b7PpCesHXsmk9nrIwRVO21VaNV07kfhseK085XM40P_aIpxXZaNlVlPMC_FQ_a3AuBlhDlHpLwGj5dWAqByZ7wIQ8TUc67myI9mutA8Txifav3Lr6LDWzUHm5lRI_bgGOF1l9rgxhSqofI5qGWTWFpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
واکنش آنجلوتی به گل‌ لحظات‌آخر مارتینلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/97133" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97132">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXBOGMYzEmfU4-O8t9ZJ0qFTgCWp17xvTmveRGfxhKS3hVyUSSrmvVS7ZoR392gFXdaDK39zeHNJ4ezJnDP6MDmE9rs9TT4Lu5QV2QGAAfQ1xwRV-Qhnf19oLITL-jFpn64bpdfnhyAUelOGGlMBUSTuden7ZG186oFWWw_kc_9T9fpTe_pJB4hmHjwqGRw97PMo9JjNaSX7If4tW1TeONuaQnpy-6TzTfyOkQJrWXm1RsiS-G3A0OBE-Dz6qJ3m5tAuY-uAOSQBcyFGjvCjiy-OBLkGKV4_h4wVJF7ZpWGLTXW_tgzLeUaxZLo4vpKSjiRU5I-epM6T0tlwRpZYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇾
طبق رده‌بندی فیفا، پیروزی پاراگوئه مقابل آلمان چهارمین شگفتی بزرگ تاریخ جام جهانی محسوب می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/97132" target="_blank">📅 16:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97131">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180
؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97131" target="_blank">📅 16:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97130">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa3275ad1.mp4?token=hyjxDZqtyvgLTvHQ35PqZprWj3qK4mY42BA6MdR6p-__HEg1IqVCpI72yMQl_kTPYi8UGpnHu2JgAqE1NXY1eXyV8EVijCiLQJgUFMV3-oIMfjF21Fxgb2CI8itPbI4uHr6N5xejSEkpFsDUhikpsS3z0Rz2Dddit3mNyEIx29Y1oXxQl6pK62spFKCbRDN5deF5HaHwzANf-jLZ8QkSUxeAk5m7_iOH3YdYkQVYLu_Xsf67HRV19ZAr43gntzfTJbCzTsHZDLrBoqfXl7ZJSaIyBweqMVj707j9WM2774Kouy5MUYVZ2TcVUz9D_0lq0yXPiYL5UalELQC1oZi5uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa3275ad1.mp4?token=hyjxDZqtyvgLTvHQ35PqZprWj3qK4mY42BA6MdR6p-__HEg1IqVCpI72yMQl_kTPYi8UGpnHu2JgAqE1NXY1eXyV8EVijCiLQJgUFMV3-oIMfjF21Fxgb2CI8itPbI4uHr6N5xejSEkpFsDUhikpsS3z0Rz2Dddit3mNyEIx29Y1oXxQl6pK62spFKCbRDN5deF5HaHwzANf-jLZ8QkSUxeAk5m7_iOH3YdYkQVYLu_Xsf67HRV19ZAr43gntzfTJbCzTsHZDLrBoqfXl7ZJSaIyBweqMVj707j9WM2774Kouy5MUYVZ2TcVUz9D_0lq0yXPiYL5UalELQC1oZi5uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
شادی دو‌خانم برزیلی روی سکوهای استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97130" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97129">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0faDPpaIB-WenUn28L-QmewBMzxm1lg6BuFhB1cjzv_C0On8cW45eNvqAHNs4gocJ61IwJXBuDeAS2T8jctfC2wKa268o_lvonKpGKeMuo7Ast0-SrELpoZoO5E3UnDSC_893HlbxwGHtmJF6ots4BkOVy_odwLgt4aaT-scIStasA_KBIzi_3kIJX6b9HlbcJsjkg9liEa2d1t_Vcuq9Usof6ht4ADnCq7e9-WaG7dXS_vHDXkkoIT8jFWzOlp2Ri_g0V-r7V7z4y9aImzTkpvZO3V33TQas6033OyJVBPCU-Ox3WdBvhSEGlmDM_IxRS4LIQ3B2vQHaV4-iMpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8 سال پیش تو چنین روزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/97129" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97128">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97128" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97128" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97127">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=F3uWugtR1kWkDj_xAtpNMRyuWBo5ywRZtwldwFoKnDlbR6wmOzAST5LJuBj7zn_VJ9bqkQbI-GT4fGD0mJy9GnPgQJd7B3YS4FyyFMBvRktyJqe_RqU6YGOtm1Av5H95_qWwIhHCLaMZghByBTWBzCBqChazZ9Lau1QuzAK9R5SZBFGZS1lcCz419durQGN_h1vZ2JzY2qftaiWv8dVJHAw5j-TGQYNvjKj57mqAH1upeiFwWC_0nwQRwB955YRTl7b7_hGfTwA2uMlZTpQivYj6Qa-NKpKQKmsp5nKr6n6MkExoafNMiBIArxXCTg3yWSYHlBEUolT68uO5ZkoaOg3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=F3uWugtR1kWkDj_xAtpNMRyuWBo5ywRZtwldwFoKnDlbR6wmOzAST5LJuBj7zn_VJ9bqkQbI-GT4fGD0mJy9GnPgQJd7B3YS4FyyFMBvRktyJqe_RqU6YGOtm1Av5H95_qWwIhHCLaMZghByBTWBzCBqChazZ9Lau1QuzAK9R5SZBFGZS1lcCz419durQGN_h1vZ2JzY2qftaiWv8dVJHAw5j-TGQYNvjKj57mqAH1upeiFwWC_0nwQRwB955YRTl7b7_hGfTwA2uMlZTpQivYj6Qa-NKpKQKmsp5nKr6n6MkExoafNMiBIArxXCTg3yWSYHlBEUolT68uO5ZkoaOg3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97127" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97126">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZhkz3FVi4QDfl-WXeosYuTy2EbpWjBJI7fnJsbf8YEWHyKncoqKq0g-yZg36LlTwZTqoPKypuEkVfdvHVxOxrkrUXL4D5E74BpGqBgGV24qKJS9Qe8aeGegIE_gI36hnN90QRx0O2GNbHKilJlFHS0tsyL4bxo_UqbVim9_Wp-YrOubPprzPaZQ15vwRt_jWdUF2AlItMoA3EUlOL2sYGhAGUproLPJFGwtY3yQTDMydSWzwfBV9dwElXd_FkQANRUXUGCuTjOARvPKihkffn3Hxuk4Y9SHqlkaWSSpkk7V24O1k1dfW7zlEsdqTWT7ihvTY6ocu-R2rmWSTuMd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسیر احتمالی فرانسه در مرحله حذفی جام جهانی
:
🇸🇪
مرحله یک‌شانزدهم نهایی: سوئد (قطعی)
🇵🇾
مرحله یک‌هشتم نهایی: پاراگوئه (قطعی)
🇲🇦
یک‌چهارم نهایی: مراکش
🇵🇹
🇪🇸
نیمه نهایی: پرتغال یا اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97126" target="_blank">📅 16:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97125">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f012c953.mp4?token=unqhgqQvlII2BEJNhHZk3uPpvdWodrV9w2BoCGZsbekv0Kl7xMitPHk7lEN0ZbDCLAlpO4RGwKDBPL2Nxcwf7YA5MVc2bDsclE1MlSnOg79TgD3pj5vENbWDLsRmbv5i9k371cgeR0w3hYVnQH0j-a_nBSqpjg4g8th7Jkc5Xbf85WkAP6vj893-7n6ozjUcITPvNf4m7aOY6-KN4MsfdcakzgXR6m7Ggsqg_IRcpFzk0fol6c7ogn0xzKkc5azZKPw5lA7OkAXOJtktB9sBPF98jyiUm6Vr91NxlVUCOBpR1YnoNOyNnMnC_VIenGfKyMjvxesR3NNtDLKjaRjj5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f012c953.mp4?token=unqhgqQvlII2BEJNhHZk3uPpvdWodrV9w2BoCGZsbekv0Kl7xMitPHk7lEN0ZbDCLAlpO4RGwKDBPL2Nxcwf7YA5MVc2bDsclE1MlSnOg79TgD3pj5vENbWDLsRmbv5i9k371cgeR0w3hYVnQH0j-a_nBSqpjg4g8th7Jkc5Xbf85WkAP6vj893-7n6ozjUcITPvNf4m7aOY6-KN4MsfdcakzgXR6m7Ggsqg_IRcpFzk0fol6c7ogn0xzKkc5azZKPw5lA7OkAXOJtktB9sBPF98jyiUm6Vr91NxlVUCOBpR1YnoNOyNnMnC_VIenGfKyMjvxesR3NNtDLKjaRjj5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇧🇷
مراحل آماده‌شدن همسر‌نیمار برای بازی ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97125" target="_blank">📅 16:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97124">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVacDt5WMNMzxwcvsUWx3f5Z6s_Ivh55aAGwVnHoQxnXQAtcAPAsnUiQMbNOpiW4A1yly8N3AF0xCugdrIm0xL1k7xuowMqMnoOOy7-moiUOD1T-TCwdkfYE-IYp6_Kox1GVH3LBBj1BPDkDfhy2jHkzBE6ibFF2wNhdi97RLlm1uy5bSb3On6pSYUrj5JNhDMiZhMoim1tHQGDXKiy79XpM6ZCsTBCjzzLM_sLLMWNbIWKsEP9aXviOPjqhj67cMsC3zsQsI-0R6toxdwR0G6ESZ_L8GikSWS7rLDJXqh36Y8ldpBZtaXUT7g0n6mk5hCb4jX9OPi-csS_9IQP-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالد کومان از سرمربیگری هلند استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97124" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97123">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9b21708c.mp4?token=Ik2QOLavaFdEL6Y7UgyAt0vHIU1AbiejeZmlKRk3NbSHWmi5RCJ8UVyqiaPXqzKh32VxHhFPts-bNcC69dlm4juBWcAf-kUWXrxrhu4FXIfMToTLD1PzagbtGMXe8p9J-RhYPEUNM_7FNM_hiFQ5Cjw8UNEA520BdWXlgd8gnUlUq7RRot-o_qKhezSDZcJAd7FVvZJcitl_GpYEz4fNMQ9JD975Moc8xo_8dXJCOxf7mm4gAXVWnBGK52rbKKWKsqADQTeyYP1zOzSnCB1tCpPdmFBTqvlWLf8oaPfnJJBX4zCGgpjiDnkycT4Vq6swZNooWRTqTj4ukGmqTwdULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9b21708c.mp4?token=Ik2QOLavaFdEL6Y7UgyAt0vHIU1AbiejeZmlKRk3NbSHWmi5RCJ8UVyqiaPXqzKh32VxHhFPts-bNcC69dlm4juBWcAf-kUWXrxrhu4FXIfMToTLD1PzagbtGMXe8p9J-RhYPEUNM_7FNM_hiFQ5Cjw8UNEA520BdWXlgd8gnUlUq7RRot-o_qKhezSDZcJAd7FVvZJcitl_GpYEz4fNMQ9JD975Moc8xo_8dXJCOxf7mm4gAXVWnBGK52rbKKWKsqADQTeyYP1zOzSnCB1tCpPdmFBTqvlWLf8oaPfnJJBX4zCGgpjiDnkycT4Vq6swZNooWRTqTj4ukGmqTwdULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم مشکل دارن: نه مردم فلان کشور وضعشون بدتره
❗️
جامعه توش جُرم زیاد شده: نه فلان کشور بیشتر مجرم داره
‼️
مردم شاد نیستن: نه توی این کشور مردم غمگین ترن.
❗️
اینم از فوتبال ما مینویسیم اینجور فوتبال بازی کردن قشنگ نیست بدون بی ادبی ...جوابی که میدن: فلان کشور بدتر بود. یه عده ام که متعصب الکی بدو بیراهاشو به ما میگن..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97123" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97122">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">💥
🇧🇷
شادی‌طرفداران بنگلادشی پس از صعود دراماتیک برزیل به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97122" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97121">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=XojwCf6exu6Vs3PR7Ft31R98DDCv1zBpyXmyuEEcBxK2FGFwwAnYA7pk58mBmIU-U3Efrc_j7sDJz3mmamb0X31D0fuZyEmx_ZIebi-UrVX6AcyOrBtuB7wImyzKF-z9ZNCAtr0N5lOxzYRT79MhHMm6yR0JifnDG64mPQb-2tcZbkVApDVga9nuhD9Y0TCvGvmuWK1BBN68IaAGaWKj3Z5F0W2NopEthiR9WXWWI3dyik8fOVdwF0_dA4Q-e0hFwP8TW3k2ZZ1lmXsszHm0l9nCP7s-T3w0DCiWZPQy6W2n-69sEytARN6yOw3-Nd1AvB1SRWIZIzBYnHEp39u9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=XojwCf6exu6Vs3PR7Ft31R98DDCv1zBpyXmyuEEcBxK2FGFwwAnYA7pk58mBmIU-U3Efrc_j7sDJz3mmamb0X31D0fuZyEmx_ZIebi-UrVX6AcyOrBtuB7wImyzKF-z9ZNCAtr0N5lOxzYRT79MhHMm6yR0JifnDG64mPQb-2tcZbkVApDVga9nuhD9Y0TCvGvmuWK1BBN68IaAGaWKj3Z5F0W2NopEthiR9WXWWI3dyik8fOVdwF0_dA4Q-e0hFwP8TW3k2ZZ1lmXsszHm0l9nCP7s-T3w0DCiWZPQy6W2n-69sEytARN6yOw3-Nd1AvB1SRWIZIzBYnHEp39u9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
❗️
اقدام جالب نیمار در بازی دیشب بعد از ورود یک خانم جیمی‌جامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97121" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97120">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4sGGoTLFEzdvltjZ8zWj8c_S6R5aWbUpwS9-vB_l9RXCKuuWcN0RGNA5wWTm79aTilkM0BRB5mejuLHOBr8tzUY2BVIGh3vo5LzM_JcdD5a-txhEdgXp6upJDNZqUN7KwfPnDfaS8_sGQq8VqBCzwsJMj-c46Mwn8WlECc-Y3HW8XzcYqgOap6l2XuYDK9Ue-vEuCP9ob9tcm505MVEhXXbKWnyt7PLfgGrNvY0xOSgyqMmVtHSB882pm-vuok5RpIMMklJ3DHQJoGVTDwL77HDuS1ZzkS73_5OPHRm90etW8lE-wTW6g2XL-bLE0YoxdVr38410oN_1VuAHO4ZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
- کوپه:
😂
فرلان مندی پس از اینکه یکی از سگ‌هایش یک پسر ۱۷ ساله را گاز گرفت و به دو سگ دیگر حمله کرد، به دادگاه احضار شده است
❗️
دادستانی خواستار محکومیت مندی به شش ماه زندان، جریمه و غرامتی تا ۲۲۵۰۰ یورو بابت آسیب‌های جسمی و روانی و دوره درمان است!
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97120" target="_blank">📅 15:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97119">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnbpVjb3HRZBDKDYJ2oZdTjQxYxfAAVfoS_xDzbvRRNQef9ZaSiMWLtHJc2KBM9BiP3kHaxEjjRKBYcSq_Sh4dlAHaXHEARIrWFgORgVkMqN-1blm8IvX-pv-rX69xAR0rw37XxIUmGhJ5qqlYTqgIZ7JmnIlLS9fETVD04MYCcbOx8L3HACCf2esIfvDdPogwDkMSLD-QFsQzEpUWIPJN8zIBdcZgMxqdqyjrjZRTrSev5ASkclIQRsfChIj5AWc7giQXEvWgjIWAFoKCqXA6_hHMiJmbhOcJoNi1qN4VRtxKfSw8oaH-rf_Hdy3S_tb_zCALZSV6Y66F1VTu65Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حواشی‌جذاب مسابقات انگلیس در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97119" target="_blank">📅 15:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97118">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=p2QcimXWHxMjwFe_kGSVGmH3vh3hjK68QHV20mhZugyoiiprjOlO7D7e5Ph1nZu-g_AmSCcYTawYTtFt3Fd5xcC_uKvO3lJRsKSZQ7c9rILNtgDC4GNC1Hb63CB-68wUTMPPPaAlgBP3SEcRUfxEzvKzLgx0BhFATls7oMfBNAz-10Y3hE_U--idDk5Rxg6gSbobY0o00gZdT6zk8XRJ4bso6-vs5ZOTElWt7l-Wcgj5hMGoMV52W3yqia2mOMX2C_HvL6sHykK3IgKsUoRIpb8yp0SDUOyGX1z2qd_fsiV4e44qKJkNk6xRFoYIcJrYtqj4Rt_QLyh7pXkw1LCbaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=p2QcimXWHxMjwFe_kGSVGmH3vh3hjK68QHV20mhZugyoiiprjOlO7D7e5Ph1nZu-g_AmSCcYTawYTtFt3Fd5xcC_uKvO3lJRsKSZQ7c9rILNtgDC4GNC1Hb63CB-68wUTMPPPaAlgBP3SEcRUfxEzvKzLgx0BhFATls7oMfBNAz-10Y3hE_U--idDk5Rxg6gSbobY0o00gZdT6zk8XRJ4bso6-vs5ZOTElWt7l-Wcgj5hMGoMV52W3yqia2mOMX2C_HvL6sHykK3IgKsUoRIpb8yp0SDUOyGX1z2qd_fsiV4e44qKJkNk6xRFoYIcJrYtqj4Rt_QLyh7pXkw1LCbaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
طرز برخورد صحیح ماموران امنیتی استادیوم های آمریکا با هواداران بی‌انضباط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97118" target="_blank">📅 14:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=Pokq_4cIdnWfEmfIGlSfGbLG1utTSHdNzOz58pPF43rSZCzR0-j0vEju_j64iREEdNcyADK5pikEES-DOBH9KoyhzpYLQKUxOCh9phWxE2qCXud1abCR-T0PH_-f9C_iPKpuHbz_HyfO1c2uzPUyo6dlI7ElczkkOmxLdbjC23xqqlpxySebTZnDxQ5TUlRkLnCDbxmwBxaqA75pUIRrpPnTKrMuMOBk4p7D4uY-5_nRG7jUnv2Ft-8AqxciMgI8Nd1GjF1VAKaGQsy2VjOUAbIKny3fq9gdqhw1VCP61Qs5nX3ktshh3tR6dQR8Lx8zHr8FNr2v1r2brno5B4TtyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=Pokq_4cIdnWfEmfIGlSfGbLG1utTSHdNzOz58pPF43rSZCzR0-j0vEju_j64iREEdNcyADK5pikEES-DOBH9KoyhzpYLQKUxOCh9phWxE2qCXud1abCR-T0PH_-f9C_iPKpuHbz_HyfO1c2uzPUyo6dlI7ElczkkOmxLdbjC23xqqlpxySebTZnDxQ5TUlRkLnCDbxmwBxaqA75pUIRrpPnTKrMuMOBk4p7D4uY-5_nRG7jUnv2Ft-8AqxciMgI8Nd1GjF1VAKaGQsy2VjOUAbIKny3fq9gdqhw1VCP61Qs5nX3ktshh3tR6dQR8Lx8zHr8FNr2v1r2brno5B4TtyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇯🇵
انیمیشن حمید‌سحری از بازی ژاپن و برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97117" target="_blank">📅 14:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97116">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJKOVZUY-pUgsJRmqGQev-pYY0itSQIB0ag0E_WNKThK7A50Zqe0xRZCHzyasj0-QNXyIxLB9x6O87v-v5KqWEQjIgJblwqJN4015K0OwKb2sww2aROG6UZCGJ1BTlvBn9KJS_6LcqIWkoCkqF_3i1Ae4hTHzB7P4Ag_aYWbMtW6LDOaSKvEArHHCg0Ru5j6dMMZkUhbgWplFF5Q7awNA83hRXH8Kb15m_6QoL2CwEP9y9vG1I_FhR6ebgLgZ_tBl7v0Zd8Bu8Ge6pUoOL_wXI1ydp1tiiNSd-yPtUFV8mzbyVVy1Kdtx3cl7SaCD_IKPOGJMHRzSu3AuUq34H69mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کوکوریا :
ترجیح میدم کچل بشم تا یه تتو از لوگوی بارسلونا داشته باشم، من حاضرم برای وینی و امباپه فداکاری کنم تا همه چی رو برنده شیم، تمام کارهای کثیف داخل زمین رو انجام میدم و فقط هدفم اینه به پیروزی برسیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97116" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97115">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=nWoj62XGprtp0z5wzuT-VJxNa8z0746453ALtDZQei0AlfRpUuYh8k4zcdy2gWKh9mjqpHL6WqPDhDl-0CmKIHlYdmKFDfy9rU2GBiXbvyoeYel6NP7KGjIRU0mvDoDg175Y_MPrn2G8Tc2AILarYgMQi_WFWvFgJQ-gHZfx3DSkJocFVGE-t69ppV-XFk2WsTebiH3T1hmzC9jFs9WBMnqNBtjsycnKO82KmwXsF56vN6ZXeNgBr-EnhFGpVQKifeucG6F8dhewGnSUfOGir1s3nQl44v77V2opNcAISJDF-KY7F0ogD4iwOkqDDDugL_eC18PYq4ISxD73ILolQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=nWoj62XGprtp0z5wzuT-VJxNa8z0746453ALtDZQei0AlfRpUuYh8k4zcdy2gWKh9mjqpHL6WqPDhDl-0CmKIHlYdmKFDfy9rU2GBiXbvyoeYel6NP7KGjIRU0mvDoDg175Y_MPrn2G8Tc2AILarYgMQi_WFWvFgJQ-gHZfx3DSkJocFVGE-t69ppV-XFk2WsTebiH3T1hmzC9jFs9WBMnqNBtjsycnKO82KmwXsF56vN6ZXeNgBr-EnhFGpVQKifeucG6F8dhewGnSUfOGir1s3nQl44v77V2opNcAISJDF-KY7F0ogD4iwOkqDDDugL_eC18PYq4ISxD73ILolQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوشحالی شدید میثاقی از حذف تیم‌ملی ژاپن از جام‌جهانی؛ چشم دیدن پیشرفت فوتبال کشورهای دیگه رو ندارن تا به مردم اینجوری نشون بدن که تیم قلعه‌نویی عالی بوده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97115" target="_blank">📅 14:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97114">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=G9yXknsW1vR-e5WaI0ncl5HZHJ8jS1fx4uvVQV21tYieJIDVIIpT2VlGGs4aOjXXnOHCmcfQuobYaX98so4X-PSv1eLWgnY7fkLHfNiXbZ7mS19HyhzzgQjn4duynkTpVbzE_2ILB-h8DCh7qK-Gypq6z_lfcxwp92L6DEbRwFlXYJCWXroWyaxCQJeX0FQsvEANasnpO1rAn4hFfFJpp4h-x-lP4ULju2vGXmmgRG4ZR8bLEyTdCpA2Q7we1hY9imegMVFWABAcD3PjNe-rrF6rfDXuOUr87jOkvc-zK7tj-9uhmKBZBRBgKI3t65ElCByRXbVYUWxJSiWKg-xqZYGAj4Wbq5H7LyLFpjQvfLQPrdtjyPh8TeAcvDKfhg4l6_kqRpWW2PtBs0JeQFxVJ0elWq2_lCLRK7XThN6-z3rTg9-KLjtbEiu5Q1cNEzTInAfRopl-NR-MpWge-69J3kgVTpFGipofiRp9K-qVVbO1135PRgxgMutoA1rgA5U-R7mHywQ4Z3PTAF8vvND2QAsZDJ5ntwMslEoOtWtuAcek3FVf1NDKTUp6mGAJiQk6d8gJ1a2uCRMde09kqbVK5eivP0iH6Ril8hkncfxceQ7RH2WtOAKlwW4jAps0QZs_7tpBK8cNH-72akQ5O5NisVTovb0Xe5Ckc8hyj0YTjPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=G9yXknsW1vR-e5WaI0ncl5HZHJ8jS1fx4uvVQV21tYieJIDVIIpT2VlGGs4aOjXXnOHCmcfQuobYaX98so4X-PSv1eLWgnY7fkLHfNiXbZ7mS19HyhzzgQjn4duynkTpVbzE_2ILB-h8DCh7qK-Gypq6z_lfcxwp92L6DEbRwFlXYJCWXroWyaxCQJeX0FQsvEANasnpO1rAn4hFfFJpp4h-x-lP4ULju2vGXmmgRG4ZR8bLEyTdCpA2Q7we1hY9imegMVFWABAcD3PjNe-rrF6rfDXuOUr87jOkvc-zK7tj-9uhmKBZBRBgKI3t65ElCByRXbVYUWxJSiWKg-xqZYGAj4Wbq5H7LyLFpjQvfLQPrdtjyPh8TeAcvDKfhg4l6_kqRpWW2PtBs0JeQFxVJ0elWq2_lCLRK7XThN6-z3rTg9-KLjtbEiu5Q1cNEzTInAfRopl-NR-MpWge-69J3kgVTpFGipofiRp9K-qVVbO1135PRgxgMutoA1rgA5U-R7mHywQ4Z3PTAF8vvND2QAsZDJ5ntwMslEoOtWtuAcek3FVf1NDKTUp6mGAJiQk6d8gJ1a2uCRMde09kqbVK5eivP0iH6Ril8hkncfxceQ7RH2WtOAKlwW4jAps0QZs_7tpBK8cNH-72akQ5O5NisVTovb0Xe5Ckc8hyj0YTjPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇩🇪
آقای‌ناگلزمن خدا ازت نگذره که دختران سرزمین ایران رو اینجوری ناراحت کردی
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97114" target="_blank">📅 13:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97113">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=bI_jrMv4c-7MiV5X1Hv8sRqIv4Kn-bBcJ29h2iGw25QguvFrHQqSNhdxyO8GM_a1zILEjHWLRhdkhIR6X7sDToAxklm0KJgyuGICS_nz_uuTR9j5Ht975sdF8mocuyJaFBA6gEEEOsFLg7W9hlzgAAsfQFhDyRV_9lbt7ki17_f6EXIm3fkri0Dr3rZjXu0TZqcEsjrpssat9J82ObJ04d3PyswjIuwR5Rt-DqJJcMwSPR8p2cbGPFk9ICZUMyOhQIXKOJN4D39D1WDz71W1tUgdBimMyEA9lpdJswTicSscYjt9SiASorOiuTR2Pr8_JetUCXphR_XA44lQGmI5eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=bI_jrMv4c-7MiV5X1Hv8sRqIv4Kn-bBcJ29h2iGw25QguvFrHQqSNhdxyO8GM_a1zILEjHWLRhdkhIR6X7sDToAxklm0KJgyuGICS_nz_uuTR9j5Ht975sdF8mocuyJaFBA6gEEEOsFLg7W9hlzgAAsfQFhDyRV_9lbt7ki17_f6EXIm3fkri0Dr3rZjXu0TZqcEsjrpssat9J82ObJ04d3PyswjIuwR5Rt-DqJJcMwSPR8p2cbGPFk9ICZUMyOhQIXKOJN4D39D1WDz71W1tUgdBimMyEA9lpdJswTicSscYjt9SiASorOiuTR2Pr8_JetUCXphR_XA44lQGmI5eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🌏
پست‌سمی پیج‌چادرملو بعد کسب سهمیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97113" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97112">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_2MgLXZOh5kfxPkHGWi4GhtWw-f30Sp-RLBQDzM2rTC_DBTB8UAjGShm5M5KT5zsRoYDm2VPKErVRkC7-I37_wpv4Z0KdnvKbw5RJDchoI04oGW90V6SAruQMKDGkGIGf0fj8Fj_TAiu94XHeyOQ-_zcgT6yU4IZYlcA1PRjdI0AOi8DREliyfH-tYxKJsowcNS5mYnVfmLO4teiDdQxj5XGkL5LU83Un0-hAQPbdU7MaaFNghpyawzT4eHX4DXUyXbQ1nFCv4YnaQJHHtAsqd9Cv7wg4ZdmW41xviVcT8_psHwrESMjv5lJXSP5w9jmriQtSPUJl5ze-xyaNN0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
#فوووووری
از رومانو: قرارداد کاسمیرو با اینتر میامی سه‌ساله هست و بزودی رسمی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97112" target="_blank">📅 13:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97111">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oowxpQFzkdN0UVdHSdTYwT_T7CgelnwDk93BvdVMWElrbiGYrDLvFdxw2Xn6XN62UTILokqfdYn5MxuB75ZZlWEVWJIU0Cq_5syMvM-hbbhO66KNA1bkf9d_2c1iAOl5wWwl2G0Q8V9OMyOZmq5Nli6_kYzK_MSa7VppZLETBfX91qCkjYWsZQWVppmRsKJkI1qD6in3DU9aHhrNCRO9IMp_iXbGoGSk7i8R7yv_hLJA0PlhSm7vNUrKDEdQy7X_av-tIcP43lYmT9pi2dPKsduEGlm6Dg-MOeVbfyMfmQZ3ebu8PfQv28CrV7MySsU2fqkbabxq9YMMGRWCA7uYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متئو دارمیان هم از اینتر جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97111" target="_blank">📅 13:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97107">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDt7PILPWDS71ZbcQ2RXmIeOuEU7UgazyJEuWZvEvFBUfkpfQ0ITgDzGL4PI_98UNkoB1kn5spPwVhJn94_xUn_AbGbn5KUeeDMKxrd3CkRmOZf7E0tX3VW4C1vashFMeMsLccU1GA56-QhmtmbCKNiz_JpXzsT8Snnq9psblSuAWjBOXCIYHpXasGB-aihu-rrNc5FvcxwAvu2MS3XmBilM1_HUvKN5qsBfmKAvcIrguppyzjni8Z-PzngNIOCP_gNlb2osPUMBsrbOWVi8qJcXHLRS9qAdcBhLizmh9bpC8Sb6CE6uC7qKThfMYnkeBq_fyejvWtS6MmS4xrRn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXtDyA9_fWJJipoK9l0pU3-x9xScrRvOh6DjphGAwJjcNhlcleXR5m6VQ9lZKOx7qLkhT2wZF5C5pposyluqT1covy3ePLJvTI7sXCrkD9EbK2ShD28i7tNjwAXzkhTovzEPahawnm9_iy9926v60FET72zjHf2lW1KtwYBWgV7nZ7b6eQQ62MN3LdC4K9_YyNz3OEnN_Lmhz22UPZXFFYD01SLztmHxh_fMHCpOli2s1iYs_1GdgpAHNQ3hC3AtqwsFAnZonNww7BKotfcsg_dmkgjU3tQHu53jKJCxdx0yhP_ibeQzLzdeo7Fg40chj6dW5WQHarEExBMifimTvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7tzDjr46ptABTY4s6WFkFKSXQGatA4Llh9U42Z9RJ_6xvyyOICIylPGy1Co-YTHIhU6qqvBercTKuNOXc0hfO7DOaBXeooK9gE9ClaniG661EgBjeNvjfsNU_iM0rgS_sa2-EXkF9kFQl6BJreuwYMeMSghmDal0btpfCpmExXmdmyhqNplyl6Or1WxOtg6snjaZ3kqUmDX09ODM2PqE5cQ2BXb7BvrION8ZCprrAoKfbcvZmdmD4hWTXAkjMDfvC_FJip79yQnX7L6uATIE_7dVY4i1F7eDx6exkP6VDEzQ4mGM46xQwIaHJRkG_6fCpb1EWmp00coJjFWi2Qbww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwGsXzD6YC8eR2RWjZxIY_k9yD80Gx8rD4mWiND9YW49Hu-qV2owimqL-Q1KpzutHYefdLGOQ2u0aMSo70wi4G2APLRYNk4H43uIag1o_iGfC4djMroaHyO5KmGdc2i0Ao-WPJ8cmq3jDU8RdqSW_RfhbZn1npwtL_hNRUNEic68veu2Eo0C8TD_b2O80P8FTB21Bqu8HngdEajLPKgv9zGqbrPzWWJJCkDGdsk1aSVsBwWBDNrKOIfJWuu5LLbBR0vTILjRDueNS7_SNdz5u8_ASEciLpTe9Kl80BmwCoiinbVj5ZRkSfLvHWynTR-U-hn9C0X7f5cKEwJxKNdGhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
تصاویر جدید اللهیار صیادمنش و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97107" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97103">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcOdKCMD3rjjcYbKXHXEbbkj29WQKZaiaoMNSRMcUQQUdEUYILFsnc_PsFMbjaY9rG9c0xc2ijiwPnczmk32AmE0XHoq-2nSwC8x6z0JuRO8Esc8MvxBhWR9CuP0xpJPXCEU-s2Ckj0yhsqXUFQlQNIvfiVAbb_m82pePFbePBJtw2iTvw6gJhJmmBgpP4OJ6Ce_kQvZwYLnKYohg4As4iu4pmd0KSL8JQhpLM34Op03SdP2l5Qq0NsdrNVuEl1-rkaw2bFEd1ZerrvMtcLzpdOMz38QI2ZeZDZblLdzuqZgqNdOS5IAOTMEVe-4gLgIZdyvWdKsP5akXKFpFxzU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcC7SaNCeUEijoNnsK3LfyGIMkMDLixpfixCZXdtoQ7NC2Pt51QrIK125sDdczb5xm9syTvGVcI0LN-ktazaNCUMABaIp_zpnu7BUbZruMGszqE8Wl0ZJHmddf7n_1rgxwiyB4Qkd7ubjmRT3vUqI3mhKv30BGGlIlaM9Sy_R8y6DOnAhUSUAdApFyvcENIbyb_uESKi5C_16S_syeryij1FgUy3DUpw6RGYj4B2LKGClE7s9JW4NBh4FnKpQY1XAGGMrs59H9srWLkeVqj01mQu-Rl5jfu4IvDJ9KnIXgn8Aeyrh7Jsj55PbT23iagcrjFJ2i4wZhnl8ysAA7gtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCZcHAoy-9wC3EQQi9zMb-4SIpD5befDbT0qxvpowF9LjRdUt1Gob5r1owQOm_VKH47e6TgwNZe-wTRkaiNjsRfalszAcAwCmoATBHZUX5gUBrxnGjQ9jOXUh7Xo-zBHjbxgmFWfxxnKqfEy8AFuQ95NfEltKB8aPNBc7LaCZfhS5iEdovWU_jd155fcRG4QqzWX5h-LpxJti4f5iJg3WYEEnFK8bpkN02vxMeqIWX57nk4LYRcvwiBT-VinHUm-DpEGbnJVuWnN_Iksu8ewzq7FGF1cSMoq5ROK8K0T3Vn5MBPjczJE03D8dNzwmtmHmz2tICxdST9yMaGxrGsbgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qze_jRWZ6NUWE-HLFAQyQPlS9zG13X0XCZaoMjBHzNlRkia4McGG49ZjfpKGjnViTQJblkF7kLy3dxG9NEWM5q-B-mJfk7TGpCRx5UBaIok8G_WzlL1j0RQkds7S_WBPqSLejODImgVP3kM2yjQyFS15AX-ELJJLUJllULo816OmbDvQRWc87qEnWv1tYaAAafX3sa9B9z9oxwKuuMqKzcHU5o730QbCACw7lPhThAuqRO7Mb4NbHkGTOyelQr4nhoqTaKMuRNAyvWW_nGUnidKudNdRYqPV4lbvZKfBp-HKtBl6Z3nqg9_2q-_50rMV_RmzsxRH6xTobCrl2b2Kig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
هوادار پرتغالی در بازی اخیر با کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97103" target="_blank">📅 13:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97102">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThlxQKcw-xhQiw11YvOC1ZKOP-jkbhZ5wGSwS4LZMRKg5zpL9Hd_3ic-LAcJ-InpLuQHgyBuK9xh_nPElvB3OAlztu0_jcVw7CY1CqK8lQSvkRjVWshxes79-iUoGnJ_XIgNgRHi3Ovqpxf4-yzhIaBwu7qlmsd89pgUra-3c8dYlFz39CBU9wa0eL4G-ar3f-DCi4-c5U_KtnKnpzla1hZF3JPb31taHrCpQ0LuZaSqCEAvPCWhtI-cLSYEfbi0W2SDI_dExDQj9PcuEQf4b4elGW44bw_WsQd4joC2NV4Vd2lGIXsta6P2DjYloPk1TyWRLxkn4L8c78uPNp7CKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
باشگاه اینتر اعلام کرد که آچربی مدافع این تیم و کابوس بارسایی‌ها از تیمشان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97102" target="_blank">📅 12:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97101">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=XLrYEkHfPKiHx6Isu2l0AvBnsnX5OXv7IR-keF1f7iVMvTrIOw90HDfpda4z3DXHTFC7RveL_JKyUjI_0lO62ozruAUge4lLqhp1oM0mqKFiwgxXoiSJhQp0AXdpD0AdfVAqb5ryldI69nnNJLxlA8i1hQfX8c56idOLBwvuRaNolPdhgnNZB6XfbPRta32apfnLgf_jy3USWQQUIHg3-vI5jBlOUbggsqaGWq_qVjVuCLYRPEoyZ_zQTeKX0OGfQ43nx523O2f-mp1Lgy42cfDTlHZs4dzfTN7XdhxMLNqsAaSUL-j9uDco8p6aLiXH0cXNW6PTEfrSneA2Fwo8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=XLrYEkHfPKiHx6Isu2l0AvBnsnX5OXv7IR-keF1f7iVMvTrIOw90HDfpda4z3DXHTFC7RveL_JKyUjI_0lO62ozruAUge4lLqhp1oM0mqKFiwgxXoiSJhQp0AXdpD0AdfVAqb5ryldI69nnNJLxlA8i1hQfX8c56idOLBwvuRaNolPdhgnNZB6XfbPRta32apfnLgf_jy3USWQQUIHg3-vI5jBlOUbggsqaGWq_qVjVuCLYRPEoyZ_zQTeKX0OGfQ43nx523O2f-mp1Lgy42cfDTlHZs4dzfTN7XdhxMLNqsAaSUL-j9uDco8p6aLiXH0cXNW6PTEfrSneA2Fwo8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
وقتی شجاع خلیل‌زاده سوژه ابوطالب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97101" target="_blank">📅 12:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97100">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAzKXdhgggNMhW9_gtnaXXQ-pXE9pes0sCexohoyGbqW4f2AnRo9WbAvwliq_rHjoP0a7h9Z0MSKoqSWWNuc89b7X_lgWtvhfDxgtJApLXRiGrssLXbZ862yLHDiwWcWuDItUv5Y5AQt4_J1I7xhcBDU29prYT-hwWiK0bNnG9v5G4nnNjRJvYHq8EGBdK071zilp_xjQ03NWrHVfi-K-LR2r9-MpUB6GthXWe2tW7uDYTC9h93saRT_Bk4mWqwb8Z8Bs2pPaShPcpgEAW_wDmoRH-bbYPgAkECcGyLsYYJhNd-Frst0FDWtgYthgPhf01SFQ840FUPsrUnT72VMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🗓
🏆
در چنین روزی ۲۴ سال پیش، برزیل برای پنجمین بار تاج پادشاهی جهان را بر سر گذاشت و فصل جدیدی از افتخارات سامبا رقم خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97100" target="_blank">📅 12:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97099">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197441ec59.mp4?token=eITAWPeWDOGfl5sc1zsCWTZDJ_eOM-Sj8dgtg9LXsQuGzIp9A5K64aWYNqCEmMDRV0JWVBIZXN1vYZg97teWidTAv-xEwUEu04MqIWDq5s1QQv0po4AfY8z1h4iECH-wy0rb_AmoJZr6WaIxUubq7Znl0-pt-0YxKR7c8TkXgp8DtK5pqrBaWpwXvXv96MQRNzoin6YN9qD2V9tTNNocBoHvxpE5LVesfxJLROIY9JtDzBAaBhs4kwm9OfuQ4VwcStIe_fDjmY3AnQXYhDt9AcbSgqHU8j8DF_SqlOGeZFu4uR2nNUdnJBKm430nWOvMlP5X1JLC39xl496Kb00Lhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197441ec59.mp4?token=eITAWPeWDOGfl5sc1zsCWTZDJ_eOM-Sj8dgtg9LXsQuGzIp9A5K64aWYNqCEmMDRV0JWVBIZXN1vYZg97teWidTAv-xEwUEu04MqIWDq5s1QQv0po4AfY8z1h4iECH-wy0rb_AmoJZr6WaIxUubq7Znl0-pt-0YxKR7c8TkXgp8DtK5pqrBaWpwXvXv96MQRNzoin6YN9qD2V9tTNNocBoHvxpE5LVesfxJLROIY9JtDzBAaBhs4kwm9OfuQ4VwcStIe_fDjmY3AnQXYhDt9AcbSgqHU8j8DF_SqlOGeZFu4uR2nNUdnJBKm430nWOvMlP5X1JLC39xl496Kb00Lhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
💥
شادی هواداران ایرانی طرفدار برزیل از صعود به مرحله یک‌هشتم نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97099" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97098">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c36135326.mp4?token=tYEC8mDCJHBzaurDZRcJ54Fwj3amgTf-2X-9IPE7BoG719qfga4OHMymj0o6jImhbbjnuZtntEVWkOx_A5_4Z6Yx7iRK18ftFN_mOxKmtLs3fwsMyu1gq3ckAxrXRrdGeexAMaq2xGJ8aG83exy67_aaXfbWjfp7iruc4hVasqZQnxc_nQwXVXp_FousHowW_R-zH6SvXlSvljFEt-Luc10cyF7QbTcmc8N0ebB2Lkm0ad4D4MmqkoLNHHRTYN9AXdpD6XYFNLnUzKLgViOttDilnOtSrlxjFuVQByRKxgoyWgk0vrSbS0_UyyQ91z6DRGmZcd3PIaFXp5ankP4lXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c36135326.mp4?token=tYEC8mDCJHBzaurDZRcJ54Fwj3amgTf-2X-9IPE7BoG719qfga4OHMymj0o6jImhbbjnuZtntEVWkOx_A5_4Z6Yx7iRK18ftFN_mOxKmtLs3fwsMyu1gq3ckAxrXRrdGeexAMaq2xGJ8aG83exy67_aaXfbWjfp7iruc4hVasqZQnxc_nQwXVXp_FousHowW_R-zH6SvXlSvljFEt-Luc10cyF7QbTcmc8N0ebB2Lkm0ad4D4MmqkoLNHHRTYN9AXdpD6XYFNLnUzKLgViOttDilnOtSrlxjFuVQByRKxgoyWgk0vrSbS0_UyyQ91z6DRGmZcd3PIaFXp5ankP4lXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
کسخل ‌بازی هوادار ژاپنی تو بازی دیشب
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97098" target="_blank">📅 12:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97097">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnZRbm0oipLQabHXJ52KK01ySWVuqZaJWXd5ZHNwqetfV4FbVfi51JuXuGhhFPLnQwK_VGHlBm4AWtzmmJ_yClbjNfETyDFHTwCSlMWX7YMIjqWRm2I-1OxpyQAFeAusuGXoAzgaYhZWD9nrTYB3FJS5BKTPr7HpzVrECdMT72U1yDivLO8_JYM0q7KJpU7Tc7B9-mw_Aw-ZiAgPwLYbEQccfJ4GsVegkcCJOlPitA1wjFc4Lyg4hozFg9lZnAktHD_0xQRK17UVAkuxk8tTMUN6goxNP3L1z-b7Rc87mq34cOa4EYQsoMxsuoXZ1WdYbqzNDO8ZBj2JZaLVYfESJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97097" target="_blank">📅 12:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97096">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnSz0VWb2qXm4b0s5F3JZEBlgPzHZrMg_gA2uoNH9CV31uK-_l26We9cPIXa18XT1pO-IT810RLWZ_CLqrRTqu0MIEeISBLLZy0Ap2e3NVb4T832T9dGqcNciuDF1kBH_7JMeY0Kb_GW1bb_el7_cSM1GtidRRrsZRhiwoaZ97KYL68BOy-_9duHUDnz5I3-h8_78bOqcFwlD3iDgS4LHFBGKimF_R5rUBUVzgGSPHSLY5DRvGOrOmC9LOzmeTR4lUQ-lBr1TGf--BVAc0I4lTtEcpKAwaWlBZSkEM9N4O251Wj-CpYDSwmAPawjDnM1BowpIm6JNuxfuDHQZ-FYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇱
رونالد کومان سرمربی هلند درباره ضربات پنالتی دیدار با مراکش
:
"
من سعی می‌کردم تیم را بر اساس تفکر درباره اینکه چه کسی می‌تواند پنالتی بزند تغییر دهم. دی یونگ را از دست دادم، خاکپو را از دست دادم و سپس سعی کردم بازیکنان واجد شرایط را قرار دهم. موفق نشدند، به من چه ربطی دارد و چه کار میتوانم انجام دهم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97096" target="_blank">📅 12:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97093">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWZJRqeT6-zprKinpTR2QWrsJJqy8lySCGy61pfVfNPOZniK3a-U8JYo4wdRl9x0h_d2sCPeCkuvcKAsk5kN9z8cGaM5l6GLRDVDb1KUJWmSkzEqUaBiYdi510jeXj3ULj31hVSfMUZIo0t2GfD-Fwuy-tIfQHhiLGViU46uYmiF0PikZAVCP4BPcUlzSqWhTpXmRlsTQatKQl7LU8uUXf_ggf-sojge2Ycegnbs3kITVyEy3YaDqtuZTI-iicHywsAWqyJQ2dae5qaCPE4eM_aFkzmRwbrtyFL2djkGOVtoYSKMm8iTbTFTvRzvIZp8Mnof7mBe6AXZB5rYqTRoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3pWsciNY8FutrMQ0Vehu3q8K5jf3Bfwpj8cauMi1Og1bredAoqXhlZC6OH_fGM0emxA58eYsmVIelVQz-JbbmxcqMI4OGMEyDgcdLa4ZjWxuTO_HHgJswGNE-3sBpiNpQsxv_2wAzKBj20fCNL5EOopdDWfRH7vfhdkCaHPZDzVYThvwBqzWcZu7ooDA1hYEHPy4f9O6Vrs9ulpLIrWSn5KE5Ub2b0gqulzX3L0uW3X-ukTXUsg67klH3omr9CnIYVp84Zrxm7cRBApZoX6Pl_-anlL2Wd50LljaWSxAgE_0VyHh0KEjRrUajS1rKTHqxfPkPt79u03RaopqO24Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKUUgoUkr1TrjIkJrUinjdv9GnaG7Zspa9xdtB4P3NYPu0a1mfa_UQMA0MqHRWd3nBdrHFTGatIbZw-Yu7NaT48h-3zt7wZ_36Wspiv0r842t43OVZB6mQyFsUEJr61Fzg33NJZY01aCiDK0ca5mnSQh-0KrbysIMJj7-MKB_hGcAXu3q3sUu_aF1w492h6gnm9QEiqZy0MTgMJwhyqdd4H9b8sIoATafdS_VHkx0bKszd-VeDafubgPiSXM9x1MD5xMqcAZPf05-Nz9beClKy471IqnqHjLCXLhuQJWJOTjdCHAEfEVm21te9-NOgylwHMtzJPV51a7-dBz0S7RMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇧🇷
همسر اندریک در بازی دیشب با ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97093" target="_blank">📅 11:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97092">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">▶️
🤩
حس‌‌وحال دیدنی رختکن تیم‌فوتبال چادرملو اردکان بعد از صعود به آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97092" target="_blank">📅 11:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97091">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1ExoO3Drzj9dI6Ne4Dfl8r4n4AXBdavWPf6rRMxQVTLak15djVY-gOHaPLxDfKqDTJFZSk56T78g27s_iIppEUTzFt4q9HN5qVXqQpGGpBKJV6INjpAuvtf5Vnu6aDO6IwWVJXyBDWsghw2yClL4zQ6YL0fA_2EcsusBfOYRq_i99L3L9Rs9wQVEC-uOH-XrIDatP8XTQXOKstLcsLgbQQ3865g-_y1gTrfGE7VkEgM2VG6fidLkUcimOEI4S2HgdDQRLwDv6wuXA0VggIn0bE4sA56gtZm4tOrYrPKzMGHIMvV2H1Tc9_EGg2RByowSgjQ8V5_06BBioZq7KLYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97091" target="_blank">📅 11:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97086">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUOd4zmQRs4QWcOz80sXlSYNDE_NZtwj1HIcaLLMAxNSzN8F7wne3PGWXWGiVHJmFXgwIh0jQN_lceGdeL8KLNrNazv84yV851s_MSVwNrWx9vEDimGXY3gKPuxjpaLfNNaHOnwuEZqICkisRbm-oS-Pj-2g6GNr8ojioVpdXEtVwWlHixrU7CkHqG55dE8N__VSwP0fUJD3Pkujx00uypIyOQyFYC21geEMq9pyDIR0GMffgIdRydrX8AK5ZlZHJ_1S0x4DusNp2UnD0aly16QjYy8hPMAFXk2z2gRNjHl_prxTEO0X6FUTNIWY1Mo4hvtzlKM-7u-TUKOZCBSSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2BhoJfeLQXzn3jo0mUqKMJVS0pk7nsmJ6EFKVxXbKCh42r1WhAKjsIfIan8AAaVcwgP9EVZLSQVvtz5t9Rd4ohd9SoNnbU5FncjMWzlr26oCsG6F4UabRgoDnWcVvK-cYyXJEajyOKBwVst04oWJlWZ_TrF8K1ot_FSiSseGLRuPqSACllZSwtb0SYfyV9ak-XgQMG5KJS-6-d5AuweGfwn6qkrtI1Uu_wn7lt0ir3qJlU4ypLtMt5CC-ExwfKL99-2WoKXxrKa4-vLJN7E5z6IQgcsdUxL1se4lCnR-LGkCOJwJD2OtrVXeh5HOMnNdnDhIaAtQ5XGmWNFl8dq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTM4dWYwO-Us6rix2NbRH3kKMSb1vkm7Yd9S2gmkF1vv-9m3wbAC_-HLw-5f_zpWNNA5UqJ3yaBLI_7SCVGMGUw_1rajw5yoy2bc-LbZkMLp-Vp4NaxqtnoP79HkOWsOLg_H9ubKdJnwEErv8Hnwnm1zasmOJNU2M80C_8Kwr3ckdFncuUn2b6uuxV71e28RoA3KP9Fu-8jg3nCTJeO6MmxUbePeGaxIu8xwEolCL70AI3d1ysfGaG42FNPVtM7XrjZ6krm5dPI_2Z2n0j7-icoyJm9QU964OycewmUXAQ2zzIU8EPWPFDpXKRYEvVCwoJHOr56KRYv0uYJ0UTkD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5HYaR1VyGMva8I_tBdapQCSlAEqES7OjC-KREIxaAKLdPBgNtV74mJVhE02isWDBWlmZxXuKYYkzHOL1CGIlZq46WQa-GGN_xbTMDnbjQ6ent-gaTTa8BUU92XINr6O7Wfll3LwmDkJ9qzM2JvOHfhfNZWM_5A2GjDl-6hrgqcJ4q9FwWWIQJlAHHmWnpXe91F3ck6A4IrvZUctloGbBDHAXZcLWTHSfMPjgyN31U50LIXqd-bKgkSm6PnbM4VrWB02nzDdpgZzKlL1NNpFQCen1AMgco54W4OPsV9sZ9PF3qVVX9mAbWqt9o1cS5GFPQA1WQDwKdpibdq0IZe3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8vv2sGW8RdboY7kolLxkcCUgfhui2O7SZSIWppuU7KSjDpq-w4t49zB-yRSs8knp27qrWNxiBZe0gf20SE8_ugoLI2PazoiN9ZrxSWF80Dp_HoTtXM9BsUrj2wsaBeUEDkAiVUOq_xJDHCbfr33YwJzIdfeZuhOHCXVQxneN1QbuZlDcaNebjncIMfxMX_-nIO5WNJ9Jnc2WxokAlIeVK--zbIVwyRnXqBk2gQFLEUMJvg9v3lN85HJsMtDs3ypxGP-1GBo3Ij5neUJfv5MLFJxBvXVtzM5Zaqz0YVY4DyIztuVVC93T-r1TceAGiCOdEWfvyMLuKKh6H9YU1f-WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر رونالدو نازاریو در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97086" target="_blank">📅 11:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=O3DrIDvZ_RLlxfVczXKKbM9edYdacqGEuDIqSmEejYhguQuG8BBEEKZKkfXQuwXPVp9dPtN9dABe8y6fxcxmPzoKbK5ugBC9vpLl9leiqWQbdP-07FbWu70alIbYia2GNCXJ6RPV5mrDBa1AZSCsfzq_YEMJ84rvauzzkvBkodB2A7a_qi_DAseIZBc8XJU9WRUBYyYRnBzvcdtnRFS46bLyPPDy3rWV8QaRxCk4YTPifEBjtrC6P_ba59G_6vk2pGSaWkPnA3ko3uBwBpYgPLLh2DaD47Cl7cIXVWX1yR0Of7fJ-trJ7o-O2DB2LXTsNVg0RYP6iVhUwMVESUI86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=O3DrIDvZ_RLlxfVczXKKbM9edYdacqGEuDIqSmEejYhguQuG8BBEEKZKkfXQuwXPVp9dPtN9dABe8y6fxcxmPzoKbK5ugBC9vpLl9leiqWQbdP-07FbWu70alIbYia2GNCXJ6RPV5mrDBa1AZSCsfzq_YEMJ84rvauzzkvBkodB2A7a_qi_DAseIZBc8XJU9WRUBYyYRnBzvcdtnRFS46bLyPPDy3rWV8QaRxCk4YTPifEBjtrC6P_ba59G_6vk2pGSaWkPnA3ko3uBwBpYgPLLh2DaD47Cl7cIXVWX1yR0Of7fJ-trJ7o-O2DB2LXTsNVg0RYP6iVhUwMVESUI86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
هالند تو اردوی نروژ داشت غذا می‌خورد یهو‌ تو آینه خودشو دید رید به خودش
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97085" target="_blank">📅 11:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97084">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=ROc2pc_ZxmbuOlpHvh4ldXoIxLwTSUDzjV6oFoL2CdXGl7BBXAB-S5ddtKr3nJqBzwjtt4hKMwGRosJVRJXQOjss7VpqfO3k5oToh6CiYnGgLHiy9A1BBBppaQnrLrF_LFKKUOsinnWVhJDOJ0dxbQVfksoxbCLizLK_HlulzX4NLVrJbodm2LKfxwdbHeibLiPmTnxXhtFc9sftNU-B7C37z45e5rl-qgfYpJXpURabQegGYmRuaiYKDKiC2UaHsjqU_lhKDuIuC0idcSvuvnB9cu0g6MuYHXaYg5DUMjtgyOCmabTN53g-hN2KWEoe1YiGM1uzWRwiPtBTStHAPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=ROc2pc_ZxmbuOlpHvh4ldXoIxLwTSUDzjV6oFoL2CdXGl7BBXAB-S5ddtKr3nJqBzwjtt4hKMwGRosJVRJXQOjss7VpqfO3k5oToh6CiYnGgLHiy9A1BBBppaQnrLrF_LFKKUOsinnWVhJDOJ0dxbQVfksoxbCLizLK_HlulzX4NLVrJbodm2LKfxwdbHeibLiPmTnxXhtFc9sftNU-B7C37z45e5rl-qgfYpJXpURabQegGYmRuaiYKDKiC2UaHsjqU_lhKDuIuC0idcSvuvnB9cu0g6MuYHXaYg5DUMjtgyOCmabTN53g-hN2KWEoe1YiGM1uzWRwiPtBTStHAPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
🇲🇦
خوشحالی سرمربی مراکش و خانواده‌ش بعد بازی و شکست دادن هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97084" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=m9ZW73s8M0l3rGGSGEamgcOU4WagPWLrMN8GXtZt-c2Tzgl6wfm5TrPS2HpQ4IQA3-HNgQcPDvUpoNPFW92bKuLArmG2ySt1rGdNR7GpcgPDmMTZXe9ytpGmmozAzjS1hhqbMzCufdQfPqItzJPHCYsPHXjbLkWaRkNigcXOZuC33cGxJia9lFoDVfP4AO48QKFbBco0ZSiRSLWdF9kX2Rf0xSEPr-MQn8i6dF8sowuvW6TPn2idveIDjO1vcxTi95Qo9PakBH6GYXOE_ROlfbA0id-waiHs2f8yuJ8nWGlVrp7DJvs7vt4K80544sQmRr9pXjefkfzSHKZeYe2_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=m9ZW73s8M0l3rGGSGEamgcOU4WagPWLrMN8GXtZt-c2Tzgl6wfm5TrPS2HpQ4IQA3-HNgQcPDvUpoNPFW92bKuLArmG2ySt1rGdNR7GpcgPDmMTZXe9ytpGmmozAzjS1hhqbMzCufdQfPqItzJPHCYsPHXjbLkWaRkNigcXOZuC33cGxJia9lFoDVfP4AO48QKFbBco0ZSiRSLWdF9kX2Rf0xSEPr-MQn8i6dF8sowuvW6TPn2idveIDjO1vcxTi95Qo9PakBH6GYXOE_ROlfbA0id-waiHs2f8yuJ8nWGlVrp7DJvs7vt4K80544sQmRr9pXjefkfzSHKZeYe2_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇩🇪
🇵🇾
خلاصه‌بازی دیشب پاراگوئه و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97083" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97082">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFf0OkswszzQqlg7uyPdVMRd4Qs21D23M5iZndEHsOdGWWZxMiPEed75hPUgBc76wnVYRfJA1hFdIV7P0R4PfNj1e_5C8jqNsemaVWSEx7mM6cIbRMQ0Qh-xGxYC99z8q779_eTF8V0C8wCuWR1Jf8oAV_Fg_Wp0pvl5hMCyIcLRy-oHxD4_4lV2zpCoavvqhfNIjwE_1NbOpbXByllxsdn3HP_uyP007NK2Wbx74lQaAMx4WOzcegWkaMz1K_DFlxFwsQqYNeggO4Ke_y1w5B9T0mBKJpZ-5rV4kgZAepMkBI-R3UTJdfRrri_eBQJdyMKrcaB3yw0WFHM_Pal9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
عملکرد تیم‌های آمریکای جنوبی در مقابل اروپا تا این لحظه در جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97082" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97081">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-text">ریا و دورویی برخی مرزها را درنوردیده و حد و مرزی نمیشناسد.
واقعا با چه رویی میخواهند در مراسم تشییع پیکر رهبر معظم انقلاب شرکت کنند و در چشم ملت بنگرند؟!
https://t.me/hashiyeh_news24</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97081" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97080">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92c81a09.mp4?token=NWMquooF-fDhb8YQnxeU_HQVXYCgyQc7gl-vAC9707VEQfStx22SVUlhQvR3xzrTYG0rFoPwDGlhHUj9zMtdYWgNGffLklxAlxvrWI3luhhS_OeVNrXYZHi9TBuyVbhdhdbd5hSNHrcQn6V-HGH79RE9YwtLSxVSthF9LQtRCEjQg8LgiR3bCqWsHAs8XCdmz_C99P55Zl9VW8e3uFKLxS7HyLbKxJzzeCEgkuPozGnyoApP8YvYY_Gvpx1-vLnZzPa0Vlk-CVXLwOMiG7FazKDvZF4EYPK9ap5sj78zeB3tuRGVfU4Sa9OZjuEbvDN4tvDVLmK9LVpqXLOLXJPsgmbF3VvZmAsl78tbiHJL3JNJYREftUQMBh39Q0P98zkUqeIyqb2fGqQ27u6ZQGyf5SFagnMJX0wgqns9mAAgOzOuHg-Ha1f0gWbI6ZW2fLNUPNML2ftCdP3BDJPK8A86h2xK9HGz8ynrfO4260PkYI29Wqwms1DWXW3zrwWPdDuzGTyTREp-wCdvup_ssvxtBh6c6KmPLojkfm4eyCHq34qC49bHLXvRMh0Lr8-IqoIanuZ5zcjK-19ZgS9IoMdz0XXnMzVgOCzsiYssOFbT6iy31xYbkC23gD4OFh3848gfHyvtCE4QhvzzkGLTvIG1UKZ-uaaT45XF2h4QKmBoNYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92c81a09.mp4?token=NWMquooF-fDhb8YQnxeU_HQVXYCgyQc7gl-vAC9707VEQfStx22SVUlhQvR3xzrTYG0rFoPwDGlhHUj9zMtdYWgNGffLklxAlxvrWI3luhhS_OeVNrXYZHi9TBuyVbhdhdbd5hSNHrcQn6V-HGH79RE9YwtLSxVSthF9LQtRCEjQg8LgiR3bCqWsHAs8XCdmz_C99P55Zl9VW8e3uFKLxS7HyLbKxJzzeCEgkuPozGnyoApP8YvYY_Gvpx1-vLnZzPa0Vlk-CVXLwOMiG7FazKDvZF4EYPK9ap5sj78zeB3tuRGVfU4Sa9OZjuEbvDN4tvDVLmK9LVpqXLOLXJPsgmbF3VvZmAsl78tbiHJL3JNJYREftUQMBh39Q0P98zkUqeIyqb2fGqQ27u6ZQGyf5SFagnMJX0wgqns9mAAgOzOuHg-Ha1f0gWbI6ZW2fLNUPNML2ftCdP3BDJPK8A86h2xK9HGz8ynrfO4260PkYI29Wqwms1DWXW3zrwWPdDuzGTyTREp-wCdvup_ssvxtBh6c6KmPLojkfm4eyCHq34qC49bHLXvRMh0Lr8-IqoIanuZ5zcjK-19ZgS9IoMdz0XXnMzVgOCzsiYssOFbT6iy31xYbkC23gD4OFh3848gfHyvtCE4QhvzzkGLTvIG1UKZ-uaaT45XF2h4QKmBoNYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وقتی سجاد غریبی کسخل با ابوطالب‌حسینی فیس تو فیس میشه؛ سطح برنامه رو فقط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97080" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97079">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_Yu9JeIb0SIXW_ix7l6FLQsRejlgBpnoqNkF6l9ms6nD-ZazMvci91l-GEOcliY4dxJ_rr3dE0weonDC1PZwIkjuns9r0wpyK1ksO1jSM-vz2UDtsr3JPX_7gtTaaQXhFyoYBRu6nGcW8hCg2g8ufJbX0uRdlB-KeROZFyF6KyFtboJ5kGwu64XsBgePptEkiks0bkYqXfXVDFW2Wv6q0CbYsB3cGUUZpXSap9Rgi-PNh_r94kBmj_PfFYzYfvprBLxltmmpMhUQMa0CmBdRnw28yzNBzpJUieFsASb1T5ap-0qBXQwYW2cNwdnh4MU71PFnCeZ28-4TMjqQ8x6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#فوووووری
#اختصاصی_فوتبال‌180
🔴
با تصمیم نهادهای امنیتی و توصیه به ارکان فدراسیون فوتبال، امیر قلعه‌نویی با توجه به فعالیت‌های اخیر در دو سه ماه گذشته، روی نیمکت تیم‌ملی برای جام ملت‌های آسیا خواهد بود و خبری از تغییر سرمربی نیست. این موضوع پس از حذف ایران از جام‌جهانی از طریق مهدی‌تاج به قلعه‌نویی اعلام شده تا خیال این سرمربی از محکم بودن جایگاهش راحت شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97079" target="_blank">📅 10:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97078">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b45db9c9.mp4?token=ZC_QD99_oOzgEwXR0PFx7occOKX2Lm-0zyu_-DE0b3oSPVhlagdxPx3agSure799Ahrzz_6yhmCZ6rSfgeXsBkp2hFv70gaVkf9fwquNP8jLcM3sExsXiKh9LmeNFymS6fdKTnl9tPG-kUm6rVoAhfbpPGxqViee5UU1MoiNeR9TlcXeN83Ag6i8u_hMyWUBWILUCpV5GGRqjN9gONT79HMZNtNJZLzLtSg3YdZxl96zbgEPfTNvBju3A2AIhRQalDtAjStjXSG3VpueuxmPxQP4-dj2IJrCKs3KkrsGd1BrkREkEPWTqvL5V3rDwXA3h4M-AN0AWznhNIC_ziB9gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b45db9c9.mp4?token=ZC_QD99_oOzgEwXR0PFx7occOKX2Lm-0zyu_-DE0b3oSPVhlagdxPx3agSure799Ahrzz_6yhmCZ6rSfgeXsBkp2hFv70gaVkf9fwquNP8jLcM3sExsXiKh9LmeNFymS6fdKTnl9tPG-kUm6rVoAhfbpPGxqViee5UU1MoiNeR9TlcXeN83Ag6i8u_hMyWUBWILUCpV5GGRqjN9gONT79HMZNtNJZLzLtSg3YdZxl96zbgEPfTNvBju3A2AIhRQalDtAjStjXSG3VpueuxmPxQP4-dj2IJrCKs3KkrsGd1BrkREkEPWTqvL5V3rDwXA3h4M-AN0AWznhNIC_ziB9gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🇧🇷
گزارش فوق‌العاده گزارشگر برزیلی روی صحنه گل مارتینلی مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97078" target="_blank">📅 10:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97077">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKZ4PTn3GDM5-Jg9VBokuaANXztFGgCuKqZAwoB7KesFKNImA05I73iGei2oPtL0VQ9wZYJmubvuhgWCL5qdHS5-DPBw1D_J2qX3cm8CgvQBGXwwv7NL45qwTqJAzIlOIiO4G8_uHsIEImP_qItfgXYPlmvvKlwvIUsZsPuKHNDd6ywQ66zvwMiOFvZPNawJFWnHCSONZBK6835HG8acbts_P8oYt_DJd6NeuV0EX-DsTnt7_prGac6LAcq3ELr7Q-Du4QKf9I3wEqz8tutq5tVVKIxHQZsRpOJsl3ORUe9XAHOCQqTSnScveOdzhZEK0afwuPrRBmz24qLF3iEpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
📊
🇦🇷
جزئیات عملکرد لیونل‌مسی در ده بازی اخیر مسابقات جام‌جهانی قطر و ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97077" target="_blank">📅 10:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97076">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCM9aSB0tb7qKrsYnyS8jZpYs73y3W2kSDkVaCxTUJGXGt399WJ-2GcIbtZobYJ_t2aOizOPdDkTCYzPtK5GslL18Uo-xyUvxxOV1QWr6skmedem2MmF3A4V58HMiWgkhxVhLSjEoUKnfpj0E_VGbgZZibx32J-nyGZQzG8dldjAx7amE9yZx4TBkAfF458OaYZmX-DTHbfkN4YR5jnweShZZiPWQGxpOTkt0llCFup5E1r8TRrFiiVrwLM0FGqS4sgEnuJkOutp9D-AAIQu9Bc_JrJ1CIhVVAmSdOOkxYfHiRHfyI5O_WnYEP_0t-0aaeKPTpZULTbYEnAHDQxDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتاین:
پاریسن ژرمن معتقد است بردلی بارکولا را باید با قیمتی بالاتر از 116 میلیون پوند بفروشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97076" target="_blank">📅 10:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97075">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead284c858.mp4?token=V_pAKNIDNgN31u_m7IFfbCFs0ABQmYulX1M9FMWrDVjIfPQoI739BT84wf7AY1C8pynNnooHgg_Li8QC9YvGK0V0CtDNkCIXVRGoOd1gFoA8OteDeaP09JgU2x8Ay3MGYGbaDtou8Qp9_H6M8wlzlXq6z9uXXYi8AGjFdu5zU8FCWEd62fALGyhnlEAlvfopi0Micf1uENH-NVonJym5QuWi37VnReym9Cwio0UnG5IrQMTTmiZoOROUcWyD-6Vhqv7S2Izi1NrTS2rZXpVSpCB4Qsf9ve1jEWR1wO-vNWMCYmlCWNYc-Wj8uy4v3aqrEp5BCx9Okf0dKx7F6uUlqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead284c858.mp4?token=V_pAKNIDNgN31u_m7IFfbCFs0ABQmYulX1M9FMWrDVjIfPQoI739BT84wf7AY1C8pynNnooHgg_Li8QC9YvGK0V0CtDNkCIXVRGoOd1gFoA8OteDeaP09JgU2x8Ay3MGYGbaDtou8Qp9_H6M8wlzlXq6z9uXXYi8AGjFdu5zU8FCWEd62fALGyhnlEAlvfopi0Micf1uENH-NVonJym5QuWi37VnReym9Cwio0UnG5IrQMTTmiZoOROUcWyD-6Vhqv7S2Izi1NrTS2rZXpVSpCB4Qsf9ve1jEWR1wO-vNWMCYmlCWNYc-Wj8uy4v3aqrEp5BCx9Okf0dKx7F6uUlqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
وقتی میری میوه بخری فروشنده قلعه‌نویی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97075" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97074">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
▶️
🇺🇾
روایتی از مارچلو بیلسا سرمربی عجیب و خاص تیم‌ملی فوتبال اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97074" target="_blank">📅 10:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97073">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=ENsd7KP08Jtxchxfiu6wV_gjzpuVpw7UB5jcVi4_c8OM8hYQotwad2J22zspLZRrNPPat-Zpt7N_N2se0ccGq2TnXgWmv_Nr5jnJS6-dmD1qliTQM652PEBb4EsqhfrDSnPf9n20JK5lSiAPROSwfrBZCQPSlObaFZ0kdnhKjbRLf4rHdNJo3zhSdzcAYCwrK6r3Zh5mPyXRtyuTIlK0sqsGiphlUZSSr01GE0V2mlt4BWQL0_saRq-UI3Fcuvqhe3iKYSyJij_HtGL_KZw8epiqFe5b1dwKp60WcZuj5SuLyenUA40pau72PhScxiMLHQv9_1IVW41Zzl8cVjyIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=ENsd7KP08Jtxchxfiu6wV_gjzpuVpw7UB5jcVi4_c8OM8hYQotwad2J22zspLZRrNPPat-Zpt7N_N2se0ccGq2TnXgWmv_Nr5jnJS6-dmD1qliTQM652PEBb4EsqhfrDSnPf9n20JK5lSiAPROSwfrBZCQPSlObaFZ0kdnhKjbRLf4rHdNJo3zhSdzcAYCwrK6r3Zh5mPyXRtyuTIlK0sqsGiphlUZSSr01GE0V2mlt4BWQL0_saRq-UI3Fcuvqhe3iKYSyJij_HtGL_KZw8epiqFe5b1dwKp60WcZuj5SuLyenUA40pau72PhScxiMLHQv9_1IVW41Zzl8cVjyIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عصبانیت عجیب وحید قلیچ از خداداد عزیزی؛ حسابی کلش کیریه سر صبحی
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97073" target="_blank">📅 09:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97072">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=JuQP9fmK2j9qeD60wY0SuFJmnXOSNzd_2v26u-DIZHj-oPsfeSQtrRA0smTSV7ecYb9ag_cnFdM7usuztvCdqA0WeJbtAWO1GXV2qRBUwhHYfKSRufLlX1g2jMMaDuyAhqvdIBoBXsCOCrllUTmNMkScTeTQWNY1qDDH_IWw4IPndM50MyOyLhPfpeCz1-qDocfWoz1JNBfSOrhpaQouVTSQFsTHb6xkC3HmNdmGuULGBdZ-TFtXb1NNA7E-Jd35RpIcRTuBhTiwmtJ9cN_zoQuiz8ToHlhAcHGe_4-U0i1hU59gO4J9tER9VFCGnSi461D-PJulfVadycVNcQClEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=JuQP9fmK2j9qeD60wY0SuFJmnXOSNzd_2v26u-DIZHj-oPsfeSQtrRA0smTSV7ecYb9ag_cnFdM7usuztvCdqA0WeJbtAWO1GXV2qRBUwhHYfKSRufLlX1g2jMMaDuyAhqvdIBoBXsCOCrllUTmNMkScTeTQWNY1qDDH_IWw4IPndM50MyOyLhPfpeCz1-qDocfWoz1JNBfSOrhpaQouVTSQFsTHb6xkC3HmNdmGuULGBdZ-TFtXb1NNA7E-Jd35RpIcRTuBhTiwmtJ9cN_zoQuiz8ToHlhAcHGe_4-U0i1hU59gO4J9tER9VFCGnSi461D-PJulfVadycVNcQClEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سید حمید حسینی سخنگوی اتحادیه صادرکنندگان نفت، گاز و پتروشیمی:
با توجه به شرایط فعلی، احتمال دارد مدارس و دانشگاه‌ها امسال نیز بخشی از هفته را به‌صورت مجازی برگزار شوند و فقط یک یا دو روز برای رفع اشکال و حضور دانش‌آموزان و دانشجویان به‌صورت حضوری باشد. هدف از این سیاست، کاهش ترافیک، مدیریت مصرف و کنترل شرایط موجود است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97072" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97071">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=B-oRNqWGzLyQDbyBB0G42O962SGrD7711QTWPc5fpaHPjGTBGgS-FZrF0LV1dE1zA5NIE975JH2PmQWha62lPCfJrTdROC-ECF-hjJFL5ica25Kf1GvnWsVrXpwGZNrvdAdwLy8sLrRK3rbnYNbbfrdI9IxyaPVTEtKqcrMwCV9DqXCmk7VzhjWuDpoAA2LDWcCRxGYBsi7m95pgUA_5tUS7Lhw8oLKaAPDgh3wefCQM_vEdpUxc2sJWC0wTFOhamLpXn2PYhW5lx-AxdRYPWu_5FJ-Bm8imrF3CN9ORcIIiiW9C4ozO0W2i48dFw40_vzlrJE-Uh0LlLobw4OZrHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=B-oRNqWGzLyQDbyBB0G42O962SGrD7711QTWPc5fpaHPjGTBGgS-FZrF0LV1dE1zA5NIE975JH2PmQWha62lPCfJrTdROC-ECF-hjJFL5ica25Kf1GvnWsVrXpwGZNrvdAdwLy8sLrRK3rbnYNbbfrdI9IxyaPVTEtKqcrMwCV9DqXCmk7VzhjWuDpoAA2LDWcCRxGYBsi7m95pgUA_5tUS7Lhw8oLKaAPDgh3wefCQM_vEdpUxc2sJWC0wTFOhamLpXn2PYhW5lx-AxdRYPWu_5FJ-Bm8imrF3CN9ORcIIiiW9C4ozO0W2i48dFw40_vzlrJE-Uh0LlLobw4OZrHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🤣
وقتی زودتر از تلویزیون نوتفیکیشن گل دریافت میکنی ولی کونت میخاره نمیتونی سکوت کنی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97071" target="_blank">📅 09:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97070">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKTdc3TomD6ReTZqJ0PqfptKaCHdkwklzOJUg0rSTk2P8HEPfuZWIUbPw0XbIdnGF34ehvgBGHEFLioQQQifcnogufuMM4EoiQzLqh6IBt9NftZJ7FKTTBAn04I6nQiwRsEjb1ELlM1WBz5k2MZoKlvOlC0SOBvw-vlzw1P8pVj5lcE2f7VN6FucJqNTMyoeADnm6V70IWkDfnREVrRtHnVmGtI7Brbag_94rxyJ-aIuEp0a9EAKLt5WAuDC3WyO3JPK3xhgWIvoAaUNWtNNK2tNoYDliaKkzJXcDp-zvxQY_BfVKijxP7qml0uU-PmgBhV6Wxi4n8wB7o7A72Crpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بوسه‌نیمار و همسرش در بازی دیشب
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/97070" target="_blank">📅 09:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97069">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=bfsgNJZB7RBJCku8XwoGFg1J97h8NKD6h7ZC_ohyjOIXQqWKeFU7AxE59-8tX4vFQHjHwsjjbmBdmllCgWiBMUb4fBEELtDas8cse3H7b4jJ5cp1bDC7LR8jAdzpMSDyZCEagC3Rn6G88kX9ogG3dZwQE6hzCGwCMb68z2Ip0MjQBeWHS6op7nVpskNlMKZfbN7aZmUwfFyL4dj8a_nZNroWFDtUWwZbSvI0l_5H8aVCmp8i46HUTyNr-KOs-gPlAvyp2Rr5nsphEnhT_QAkelOux2Jzn_iSw_s3htJG2cocNUGkk5rZJX9dDqzCj4gTMJctltfCnX6Vyv2Eo9KODQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=bfsgNJZB7RBJCku8XwoGFg1J97h8NKD6h7ZC_ohyjOIXQqWKeFU7AxE59-8tX4vFQHjHwsjjbmBdmllCgWiBMUb4fBEELtDas8cse3H7b4jJ5cp1bDC7LR8jAdzpMSDyZCEagC3Rn6G88kX9ogG3dZwQE6hzCGwCMb68z2Ip0MjQBeWHS6op7nVpskNlMKZfbN7aZmUwfFyL4dj8a_nZNroWFDtUWwZbSvI0l_5H8aVCmp8i46HUTyNr-KOs-gPlAvyp2Rr5nsphEnhT_QAkelOux2Jzn_iSw_s3htJG2cocNUGkk5rZJX9dDqzCj4gTMJctltfCnX6Vyv2Eo9KODQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇴
ماموران امنیتی فرودگاه دالاس این‌شکلی به  استقبال تیم‌ملی نروژ رفتند
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/97069" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97068">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTjpYqxLM6OfLGw1upHPVKeMe6KFE936LvrZeYqDbKcliZ6CysbiRmDEnPvnx-O7fESay6E4LwWBxRrf0ePU_Pp4FqWQ8b64nhjZ6dgY1EmCvTvop7rZTh3wI6Xski4SQcK8MFaaxitmlKeYB2bme7EndVWWv-lOESfB68QCJaSDmYvjeHVLlhHv7QUUWkupCT4dyBLEcvlMB-G8srz1ddes5OHVpM15-pkyPTYz7xeafP0VMHb_VWCQT8cJVXRJ064YsOx_OByi7kLxGa2ICeYN8fQQQ40E8JFbXdiDSKcCTx2mDCou3FqwBMLM_HTbAwpG_8XhYrNmQppQCMZeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها.…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/97068" target="_blank">📅 08:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97067">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VffQ4zuFrYUGgxCeFJKf_BMWhvaAZ0txCd3Nz4p9_2gV1orLeB8raCMf-L05sdxKGkbec6anBkSxmlL6V7AOIoyXHlKt25G4tld5b2Epd1bNvoiij-1e-xxqGYGN7zxj0en0p48COQLtGwjIFwLFqd-xIvfa8EYvUmO9fIFFKCK4KfrCTp5eBALMmofzAWE_hKi3eherFicBqk42KfkvDx7d1bh-bFV6kE2W-MoDJ8KHnTNxRJCAWBBllInawsrEzOFidPS8KqpvxKlY0D5HaDJONRypp6WEraER4atcb4qt4XJ-x8vmmEdCdlPmOruWlqSN7GuPaqoC0yuQZoV66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇲🇦
اشرف حکیمی [
🇲🇦
] :" بسیاری فکر می‌کردند که این فقط خوش‌شانس در سال ۲۰۲۲ بود ولی ما نشان دادیم که قدرت جدید  فوتبال جهان هستیم"
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/97067" target="_blank">📅 08:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97066">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpApqg6TyPsSgV6rRKHfZE6TvTHPHoKs_looEadkRxTAK9ulUIx3DxCfl4ef8vMNXGIU_PgcptTMgtCcwY-9oW5746wg7l1cHQGWyqIzMOnVNoer53AmF4D7VJMb-OnPL9-BbHblSniKF019pU6wj7II7BG48L2gbKl4c_VnJ4w3Uh_Ao_lDtdd3emkoJPdlkZpWoNa09lXaUPg5ZllGfHsu1_1WeuPN2OHFsu3LZQ5ej6xixf0f0j-5ho1b6k_QYhORZEYOWxfx46OR1rkW_82C04VKqZPY2inq4NbHTGsZOXugqwc0kNvhHddyY_E9EZ37-0_NixQFFduQ-82Bog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇳🇱
🇲🇦
آمار بازی حذفی هلند و مراکش
🤯
🤯
از 878 تا پاس مراکش 800 تا صحیح بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/97066" target="_blank">📅 07:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97065">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_d2ZOSNbUDtFvYVXKwX7ZEd-tadHRuQwD7FpjKQHIb6_tFeJX6nd1CBsDZisCZpge2jFm4OSNKD_hhvdJqIrMMyfQfTHWHCFzwBsh14Otz_KcgR87lOt1jOUi_LII88YquX9GvKLiH7kmZKAKIZlzCpHZqFEKuHYV9M5XWPvl3lKv2McVIPEyCEqBcoarWrmqZLa81Qnm2329OwJKPfinyCNH9JAqAw_pKhRTmploNVEKT0bguo_kim1M-FYVYn73MOTeAsXXb42KpDHLuFQ9TZ8Ey4qQxgOgBdym4BEFDip9Q3AnULL_RncbURF_JRauW5KeGBfEtClWohzSiLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
🇪🇸
🏆
بازیکنان حذف‌شده رئال‌مادرید از جام بعد نفرین‌کردن توسط ژوزه‌مورینیو
❌
🇹🇷
گولر
❌
🇺🇾
والورده
❌
🇩🇪
رودیگر
❌
🇳🇱
دومفريس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/97065" target="_blank">📅 07:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97064">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VN_F5xNajdWizbI2AE4itBavgFxzoLRryBRjzzfRV-jtk0geNjYEbLErLQvMwze6fH554XNYVI61BLn-NE8oMFL6iyIH_apcgFzOl180EMNpYAh2OCubKCQE3jFhIEqnEBBOBny36gBTB_7-T8DlsyA9jyDct1GWQx_P93SOvPQZ4NJc6sZ-csh3wf4UnLYyFkRJ8i_CtQFPurOIzpAJaYxEO8TdgSYBInE0IymZ1JwjDxKxfdKrGn2CNsU4yglYPFGtbnqdTq5PG9OSLulfO0x0nYTp5x4OvA7ntRGGFNsaBqxxvpRbTQG6L_FZndIqJO3BbUkb0KyJ8dqV57DkHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
تیم ملی هلند از جام جهانی ۲۰۰۶ تاکنون هیچ مسابقه‌ای را در زمان قانونی (۹۰ دقیقه) نبرده است!
• از آن زمان تاکنون ۲۳ بازی انجام داده و در زمان قانونی هیچ باختی نداشته است و یک رشته ۲۳ بازی بدون شکست را ثبت کرده است.
🇳🇱
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97064" target="_blank">📅 07:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97063">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki3mHO-pZJJaRF9-e6HlgwMkFthZ60-A9YnV7W3QLXDWj5wKxVAgbZM7Z9j8ggXf13AicCgwcyfvOnW-spMsHPWPCwtkUHHbPJLNMLXjRaw4xgSPtL6RejVDCpcoPehfxSU9j34ZLMboxrAj6DGq-qaXvQNggktU-c7R4S1hC4Tc3HiQ_SeKVpu9HmqqcPY-_qdke55LGg0ldR5dA-uWLFDPNVIz-SqTAoxE7cPMcf64kn8seTuoEzc2IUhUBfanKK9hl3IfxfjvgjalLAjrBtbC9s4D50L9wLOyXR9g_w_bfk94DGY1xEwCypOiQ50jmaKmxq-Rk-e3ZzE7CowyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97063" target="_blank">📅 07:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97062">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACEJyTq8D2fpI0dTV8BH2FNzZhjDZplNCugr1ZvawoCgiVIwLG2JPZlQnIw5cbR6o5wdidpKKl9_A6DMFt5FRzjeom6hTWB8JFHgivE0ZWWjN7lkBveCkqoKJvKv7OVt-059uldOoRf8dKvPzwu6XsIVgYMOxpW87SxXPFA_r8B5M1fsjPM9P36xLWyKrYrNi0NiEvzSTI4T3pKnykeHQHqGwR3lWa2hMtl2kaqhBlvvZJRDu6UTkW1Xhb-WEfg5akuV9hvTlsWefjim0834QyX3V-OinOHd-R6nf3MhtrpuWcKNfx8sTtgQNJi0NOZRGxdykBH8qvhMrzkND4cxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
یاسین بونو، دروازه‌بان تاریخی مراکش، اولین دروازه‌بان عرب است که در تاریخ جام جهانی به سه ضربه پنالتی پاسخ داده است
🧤
🇪🇸
در سال ۲۰۲۲ دو ضربه پنالتی مقابل اسپانیا را مهار کرد
✅
.
🧤
🇳🇱
در سال ۲۰۲۶ یک ضربه پنالتی مقابل هلند را مهار کرد
✅
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97062" target="_blank">📅 07:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97061">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjqqnBkgqBOwT6UBs0tx3zBVMJ1KyFQfJDBnXmHHtYfLs3HK0lzBrgEcKfifv3Li11eJvEzjzrf33n_1HM5Pd1obLw2EHWpEebguGyK-8l0db66nslol7dkTQuOEUBww52yH-Wb9vuhIEvetgwId-Qk9XI7l9NjUgpEVJ1eMfyyExMMcyc0D92vZnoBs0A8vPaGB2mh5opIDEN9HzcrLrcT7Pr2E1hW2tqVpvOZ6JxrFbicOtiFUkWGI8rptUldtryDt-9KQGh3CUSMToIy6ThJ1f0XMrgrfMSQNOKGDoN7dPeoWFoirnqJiEGGBKdXIPogxra6oFDSlto-I7oheMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇲🇦
تیم ملی مراکش به شکست‌ناپذیری‌های متوالی خود تا ۳۳ بازی ادامه می‌دهد
✅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97061" target="_blank">📅 07:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDh7H1Ry1o2rr72cswb3jAC3eMnBqwtdp4pA7Pv4489Z2i3ROi8-i6PZrjQ0a2aANVIhK6EzV63_mF_FKdTwSsdxmGcNOePd_QQ_t7sQajkLa7Aa4XJwmUpdCiR-97IJPCH1Nt3hXEZJ-prcF_NpiVF-ZOUyaakGkB3cpZLN6omr1Uy6HxXorblWOdn6Qqxb7AOMbnf60cAJUTwPco3VQnW8z12yijclkTquQCuvQi8rnIJd7rZM-sGopvRvFWmznsC5qTRGqkNohOvhU8YjTIIFXmwRT9_YqjZV1TZiCRkHPZiwr76Y8NVQYgK3CUv5qljgPYv0ETbN5CAeRJI2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مراکشی که تو جام جهانی 2018 از ایران شکست خورده بود تو جام‌جهانی 2022 و 2026 تونسته اسپانیا، هلند و پرتغال رو حذف کنه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97060" target="_blank">📅 07:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA6X17d_tgKZ9px4ikPAeH780tv_c5lYya97smqxNzUjYyYrP0unFjpagOSIbedxeRYGMK-mWr91Qo75wAKDWTn2tHmEUWV3Y1w-fQVnvdZdpUMEGUYRpmutmLU0LcBxABsWjcau4LJERT4HdfUDVDgx5ZvTxv2fNVkMYBr_ZcLeigzKCfK4egrkv4I-FT687f8MCnyuDPBn4p5fjiYchsJ_RujSYlLOs7gql4Q21IR0zFjez_8Wp5uuLe5JwpH9DCvrN5WDE_yM3kz3nKIrIqzwuxPLep0BcUNeTMpSkeWOhmPvNBiRQQCNMmqOLfLxNsqeE4FKm43lG_HB42ejJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97059" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i98bLhDkh-QP0-MtkS8395i_1FHXM2syUZX8KJLj4-wti4QmKkoIye55eCdjq7qMahukST3g5Ap-6WrqtNTZDN1rMUs5fqdZSD1LOoZSvvIdh8nV6KV6BpCMxotnK5uQ13J-fv5vN9Po_s4IT1UsZFgA9B9AZe8ab0L0CbKwG5RMYIKZsAfmwbKpTfNWDgg-ygplWQ-ZgSxkiixd9O8Lbk6Yoflggocld9eYDiaYcFaqaDAm6UEkWSSxbMGdySqJdBeh-wiMkC6pdnKvqqxqY9QWrcVPqEgAKl1nPWJXGRrrrHiyQ981c6InN8C3r9VRh6zKqJPUu432lg3CsTPtMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ مراکش با حذف هلند راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97058" target="_blank">📅 07:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گللللللللللل و تمام</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97057" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مراکش بزنه تمومه</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97056" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بونو اینم گرفتتتتتتت</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97055" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پنالتی پنجم هلند</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97054" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چه خبره امروز</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97053" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اشرف حکیمیم خراب کرد
😐</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97052" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97051">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آقای کومان ریدی با تعویضات</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97051" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تیمبر پنالتی هلندو ریددددد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97050" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">همه چیز مساویه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97049" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97048">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مراکش هم گل کرد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97048" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97047">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شمس الدین پنالتی بعدیو میزنه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97047" target="_blank">📅 07:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97046">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هلند گللللللل</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97046" target="_blank">📅 07:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97045">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عجب گل کصشری
😂
😂
😂</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97045" target="_blank">📅 07:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97044">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مراکش دومیو رفت که بزنه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97044" target="_blank">📅 07:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97043">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کلایورتم تیرک زد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97043" target="_blank">📅 07:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97042">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پشمامممم هلندم رید بعدیو</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97042" target="_blank">📅 07:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97041">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کجا زد
😂</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97041" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97040">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خرابببببببب کرد</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97040" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97039">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">العیناوی برای مراکش پشت توپ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97039" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97038">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
🇳🇱
هلند
✔️
❌
✔️
❌
❌
◀️
🇲🇦
مراکش
❌
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97038" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97037">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97037" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97036">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پنالتی اولو هلند میزنه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97036" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
