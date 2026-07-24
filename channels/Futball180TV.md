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
<img src="https://cdn5.telesco.pe/file/oCRfMHctDv52afti7MeH-h-_cA5m1j7NwspSUXMNMLQHQNSGkUCnqtozIL96feFaNMHLkUjV3vtRkwoiG_8aVaO3nWjHSxeGYPQEfjXaNu6wyK5FgncfrifKt_lWrIAeKyJufjuGv13meGpcxED2491AgyrReStQjt9OZuP1CwJN7XKEUSHe9HTaKnv-zMzkf07atj89DgXUoOn627D7vDAle6Jme-wGCe2XOxi2Iq2rXY8EInYSyOan2lZ54Ex9XfC7Wy8EQMBv9zfNdO28hpNz4wxk9azZa_59zuiCFud_zkzEWDt0oxQgGe9Npxj6PSt73zQ7WYzDMH_2wBGAzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 533K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 01:03:45</div>
<hr>

<div class="tg-post" id="msg-101839">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8hS5nyq9ZDtekpSKWSLar57xy8jXakgHmZVnxvPscClK-T_aAEP1qQuCn9gMM1NHn-s3T9q0IYgy9Mx5i4meZBuAyggVbBD0gpzJ0vAs62eTSpxUnyF7wSytTAicgQ7hXIByx44okJRDiqk6ZiqTm-gGIEIw4iwa1sslgKla2uv2tvBaxYgKr8sn1S5xHTj3rtMJrmo4C2FS6Z6O42mLGBmmPGPlxJfxI2NPiTSiT1S1825OJ_YvR76BFy4UqaQNYsOagBshacayxw77MR4z9OorZkrMVngQBpF3FN5ID2-3Ar6pp9o5cRAp6EqKHaekr9DEuPODbsy8XR8Dl5uhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/101839" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101838">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxzpsXHbwHHrLVWtztRRB6Abzj5eJ7VrWEq2tkvGTJAvpe2q7awCsudnWNv1ceSkcntfsOcDCdZs-Oez5F8w_-248UwRWkTiV-TWGgg2X8yZIbNqIM8S_bL9O-r7JAo3xGg6WrvjW-RWAJCebuiftIEnwHZ7zknOFpvgr5ONG0bZfpohpOB1TSFb-qrku2TZDcSLgwmBzXaPC1mHCvLxNA4zcry86xpNfHiGZW366lD2zHSjoRZfVLW_MwSIqZxDRXSqBuMy5yTHFAvCNNfToSrBsl8YkBtjnpfipdWP7jegLsEl_ORYwekJIn7oJSun9WDQ8KFkuN4cnjHP472mgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
بهترین بازیکن جام جهانی ۲۰۲۶ از نگاه فیفا و برخی رسانه های فوتبالی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/101838" target="_blank">📅 00:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCa8kN7cB-y_X-JVn6Y0j5VLR5Oqp5JYMRhwAM9-x_54nhgvaBRFfxpt_bcLGifmsMffBaLBDbiRp2PtMXkaicgaBkuH1gYlcv1-6xw7ZWDc1ZBeLM4fpERnIO2WVWJWQO--__BbXWtSVxxkUYuXV6G3-qB4Svm6CwwrMRsDI8D1KJohjuE3G0c63NRr3GlP5ohLNiaHrO95MHHzt9Cl120gGLdEe7kyUwvJhxxC4RhuR60CHY-iPyaXwxvVO5r0TqbwOQFfCBWWXtFEdF7uK6OkZ0Od7X5xVAe6fhJaCn1BddHygnqPRJWOXohhIez4r46iCLXY4myzGFrLglSrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تیم ملی آرژانتین اعلام کرد که لیونل اسکالونی به عنوان سرمربی این تیم به کار خود ادامه خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101836" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQssKl4K0sbjOY-93pUKzjemIUDfr7dn-UnhSh1sl8PWoy-2OiS_yQBf3DNpiE-7IJ6q-Aut227cidbgGswHI2s_hw3YPrpk9eH8aEeVkIzaV4eznWE9wdOsCGz6DYlqH69oBY-bG61CmYBA5swII8Zs27mQm4jOlFKgm-yWf2AtMGglfyu1aAOm8yU0RWsTolta3mZ8O_MrVzXbQAXHXvYkQi2mmwHodmx-rr8fvUFYl62Mdkm8JsXRyzG7hoNiSVkRvJKUU_I861VswUOb6-g7QApIk1qFDdYmzDBH9Vrxow_UKjnDRFAvkb7FTjg5lg6gcC-YPzpcbMc-Ju4bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فهرست بازیکنان سانتوس برای بازی بعدیشون مشخص شد و نیمار به لیست برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101835" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-CEXRC4nNi_EY7zJWzkogVfcK6QZHqZZCxpE0fkwU805e26DOxvZajlGWoMBkOenZQcPJk4-Jom-7E0Tu84RY13yPzKbA8KYlVXlCfN6CNZKFF94uVS3QCA5LylEu8rZFwnKHBJRhmCW67y2c2DtSzKixRgMRRKZHg_3ugwqzBmL-QQKo5WBlxz6a7CzIpOoNFV33YpVhHJH-hA8XvNV-MtoBvhRlydZVZ80MBPJmWlPaa4W-vzt73BkotjSUZ3iJQQQ43kOAAbDQixT47d7gB0ypWOU4DYiosn073lLg86ujESHPeen1IWmhTGHz0LC81LTZ5UMBndc3NvO_HyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لبرون جیمز ۴۱ ساله با فیلادلفیا سونی‌سیکسرز، یکی از مدعیان قهرمانی NBA در فصل آینده، قرارداد امضا کرده. این انتقال مثل این میمونه که لیونل مسی ۳۹ ساله برای فصل آینده با آرسنال قرارداد امضا کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/101834" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/101833" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101831">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFxco8IjE66VR-rE4X6E0ZSGhrxZmFXWUvSqtrKdBkPf_wukH8hQQy2JsBZ9Av6OzhmSEMa-_aczT6M0oqAa4f52fG1Aeac-c7aMObLxTchl3PG0_BRBhii1iCnaqDy3iYaFUhF5y1elG4Z90Epd_aUICkGGsvWvJl3sThoP1SopLXylt6h45NsPtcIqJPvyYFRAFxIsgMJqpaydFeJEwaSfSthlRFiY7iwHctYhjnOMc2wRFngWFuC34cF6mQdRcNHZfCLdd4fAmihe-_tJsNh6Pxwy8ZlBteiPopK1Vp-7hsGEQz008swN_g_vcUW3VKM8L3mSdkkeKBlPQrmdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3oSbscJ_ZCHVjkr8oXJZR-fsZG54ZMpEQ59P_uFw98XjA7-jYU5T_N5zW18mgcEJUaKbItVe_yX5wjBzVgOkxOLOgnVM5lLsRc2Hec56Dxx5r-7Ye7FXxdMxBJ2hq1fgiXntPosv57rQliYucMjQ6PSqEIAG0wzZUCKkqL065V5XxeOlUKxRlKwcnbHxjVZhwn17JbXor6F9K_zCvFtTiuPEWXHS67pWH3giNctz4l3uDqN505woaz9RHZLJQtxmnZKxtT6nZcGERDI5jx8NK5cxNGEHvubB0tyHuLZw8ejd1Wz2uf96j0aef92Srt0m-y41DDsyRWoxPZVF0wkDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
نیکی نیکول گفته دلیل جداییش از لامین یامال، دخالت‌های زیاد مادر یامال بوده؛ از تماس‌های روزانه گرفته تا کنجکاوی درباره جزئیات رابطه و کلا مادر یامال علاقه خاصی داشته بدونه یامال تو رابطه با دوست دخترش چیکار میکنه! او مدعی شده این دخالت‌ها باعث خراب شدن رابطه شده و همین رفتارو در رابطه فعلی یامال با اینس گارسیا هم میبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101831" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101829">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAt5iPLj__t7lMIrQ6cs4d0XSal9EUzZ0hnGzxpWBseSUwKIiDfDk0j3Rsg1KbtzGJxGWjUuTruvkQzjYs0q5XQVoUgzaAkez3N1z0P_zxnnLsMlJqQrKov1aFuyvtoHXfcnJOgF_7XprNMfHZwKJTgMyLZ2nHqy6gHv2H2KC1SRCjvANsktpXdD-5MyB3vN2R4aYlJzoPZt16IkmduFmwDhd8Cm420ue9jWpfHTrxkoSYmq95U6GAOyNx307tPenF_OTGXiFz7ePxSjS1faK5CBBp6roM4u3gUCb3oidcIQlsrV4NL_3OzI--XXC1EEnqsapjZzka4wcGnY_cLH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dg9ko3xT0_2JsoswkBJovv0oDTGFU5sVU6aOqsY7PyNlm1bqlJs4YSfzjq9hMAJuWGHPrMKIgzD6TJYGYvpuGus1XIsfB3FS0JJfKqe_Uo7kKUPzbpspdtr-ONQntNB4XbSQQYZVHhCOj43BGRIToUXW0ZGZ_FynQbo2QK9n0NBSScRwljIAPRkmfvDQVt-EnVnfR0OGVITNswD6HKJ404KD-iqhQoo_zewAwp8oij00xtuOAz6jstun_ZP2VJ1fKx0z7tEI0-K0YPqt3j3y_Yo2p2rYMB0StRH36J-GdxaF5Q-1NonmuGyhKFuZjLz9_ubGumaS3B3ZWulDsjI1EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
زمانی که رافائل لیائو تو میلان بود دوست‌دختر سابقش با استفاده از مدارک جعلی تلاش کرد ۲ میلیون دلار از حساب‌هاش منتقل کنه، اما ایجنت لیائو این اقدام رو کشف کرد. تحقیقات پلیس میلان جعل اسناد رو تأیید کرد و در نهایت دادگاه این دختره تیغ زن رو به پرداخت ۵ میلیون دلار غرامت محکوم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101829" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101828">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBELRp1JN_dytesghmoDqUaUmUXf-itP2FefrljwWo9ooqAfKaZ36Xo33M8q0QeKrAbfhC0q66RcYmrdL1fdLbiAiHcvkc-XGg_Ni5kzAGFP2KsHcLhU8it_VHLz9RdZd27Hm7fHK60acL3Rtbwxe4X6IDNiSbCItc21D2Ad0HYfTeBy3Sr5jGMx7Vel7vh4eYFOEyc-lSaVVPe-s8I2p-bXN-QOVJlHZsWC04_tQi1SgacyQpF64Okhoc4OGtiFc04iphOdBP4B5FWuGeJYgUl3TC6CpIL_ZrOqnHqFIoRu72Sy38h0gNlxDXS2TdodrURzbaI4w7lHf9aX07n2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101828" target="_blank">📅 22:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101827">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpNkFkSeBqTrI0wpaRgGOMgIPQB1_VqmgWmf9TtgTcIfCgCu-OUtv473buM0XzzHa43N96xNr0Wm40qHvminLO8OtCgrZHREvR7gnA5F7xQkDR-fx9vbo8Qv1XrbGo2-pVhFw1Wa3g3YF0MD316A0-bziH_47N2tSa78TbIMMbyLDgjOQG5u0Sax4yHRJKKVILXsVw-pinV9eYlvZpRLr1WgObl26FWiAi9AqdDF61BSLAQ1Jfzu0F0ooFB1Trrk1p-n5O1aRdCIYdkp3qV9tYKEbUh9yBCkprBs_6pbFvtFiFoCgfLpH2ymGn7bXhsDkeJQUQmU2G7VP5Dc5YwvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇦
•
الهلال رسماً سامرویل رو با مبلغ 70 میلیون یورو از وستهام جذب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101827" target="_blank">📅 22:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101826">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDtiSQ3T5kayivVpv2UbUwAsQGriPWhUh6QCJIKDLYQcBPWRdWLKVFlUtQxTQVwyoksuRk4Q_0E5GBcDdWBM1MjLcGwmw4uF-j52YiSzPuoQN1AVhWEhD3HbU6OqSJdV1mcwIs8yPGiAyIU8M7Y_aF5qEqXpr-uptHRTgVLuyihg3uxU2LoUh-OZz-uLql0ii1D6Xg6U5tnAzbJQX95SZcCQuCJjzaqL4kF3syAEwvGj4kPxDyQFwuJ3qI-jHEpKwBDi2oMlXUyw9REYgLakS5vl5XHKXrfiZNf_JrmhTv-RyPUW0B-DDA3cvVEg0A6u2h023xuJYfaZEzZH8L5ZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین: رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/101826" target="_blank">📅 22:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k50o01M4o1plzV76Y0Ixp5_QzbF4BP9nI49McDk4l3jgJe8GprtqBhy8YuTx34omZKhVjmssYJfWdrPjn80g-gCjFLEA33ivEjWO9w1xnxsqf3Su5YJqBEgAYthkyXlY8OXH1Z0JZMcxLESH0HIgnSOeim_L6OI3P1ODUKY_kz51Bo6LZINXtgpV0QGh4j7U6pkUAMLsyY_kqpH_e18i9ZIDuQ2rFYTEtYbGsu3XB12G0ZkNnSpit6Lpsawf2WGr0Cz70eAibiGfhb_cmUViNTPqIqaPqWUKDElTzQURvYwOtOWULRQS6twV_nJPkq55s-aIHcuSRBQnN2Mi9NGhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🎙
ووزينيا درباره شایعات پیوستن به اینتر میامی و بازی کنار لیونل مسی:
من عاشق فوتبال هستم. اینکه در ۴۰ سالگی هنوز اینجا هستم، به خاطر علاقه واقعی‌ام به این ورزش است. میخواهم حداقل یک یا دو سال دیگر بازی کنم. امیدوارم باشگاهی را پیدا کنم که واقعا من را به‌عنوان یک فوتبالیست بخواهد، نه فقط برای اهداف تبلیغاتی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101823" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB9HU5ZK1y_pES4u6u2TlDRba_hyod27-NgTMHFx0oP92ZfocS-qG5dAHlXUgIPM69ryZlPIOqiSyv78xWbpokeNHP-7cb9bQYxlYR_HzfzGiM1cnqO9Z-EGEWR7q00njUyZ-Z_onyqOF9aopNSbSdMd8P8PnWkYFQ2Qv_Xyofll_FsrISJwJCvgdpjPAN2B8vZ7IW1lJFMcCw77ggL-q3jbXXW5lG3GiQRutVGs2Ngp2D1R7FnDbdiSXZLUlyoj7ogZ5clDiBCEb_YZsclE9Yk_HLhdQJnpojYw3uf0X1nemvqlSRklaxOPEY4qrDYjZDGAa0eUW9i19LtlAv0g_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین:
رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101822" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLOjewV3Gr_9ahfS_suOPBg73gCyBlbRqhpgwy22yZlTAnAxkEVzYzwIyOzLBkueCqqrEbHSIXy1394fSim0lDSXmZ3uuuN5uVubSAkCoud2hnoAjIcCV1RszoYxkAq-i2AgO6vllxDSk0KA4QzYnRq8fztI51RUphqkOtEX_YRaLFnUHOxQm8wOO6Ok5Gwh6z00RnptiMsqkCEmstx5oBZlAdt4ID3vg7IaGtfzNvnRQHnIC686JY999cxVORwF9lDqBdXHzoWlACm4Rc_hzviGvdIoMAMk4AFrxDp3i0_mx0HtrQ6kwTCabKj8q6pOhIsJpjWK7Or3BuMa7RycoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده بندی ۱۰ بازیکن برتر جام جهانی از نگاه اسکای اسپورت:
🥇
🇦🇷
لیونل مسی
🥈
🇫🇷
کیلیان امباپه
🥉
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام
4️⃣
🇫🇷
عثمان دمبله
5️⃣
🇪🇸
اونای سیمون
6️⃣
🇳🇴
ارلینگ هالند
7️⃣
🇪🇸
پدرو پورو
8️⃣
🇪🇸
میکل اویارزابال
9️⃣
🇪🇸
آیمریک لاپورته
🔟
🇪🇸
پائو کوبارسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101821" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101816">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7xcj1BPSTC4zKjjtvBWx3p2iZVUdapcmZ_QCKhh2nEmdvFYbAGPsRuZE3RDecyFs08SCBotb0_TxWeSfj4zc4dk7YgYwViQZvaPu8GgYax7Jz-fFIzIhnUwOJbLH45S5tHbJO1IQ_g7ZcSJ4u0oMW7wzh2t4f3gpkretcU93n4DCYrbq_gpKb-uosH65kphijOZ0Jbhjyhw8egUPstGJT9nz2JjeL7MiiUTleFW3n8ed3Q6xuNOxPR76k-lU1OZpcec-ZNRq7euSIWQKMDEdmnszL6G9_hxBEgj5ZMm6P4nUuzzUCAwgBG1adFr8qYhKd4157ivekb-ElDtZbb_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxCLummXBRR0V8rQFq203bbTBfwxvOHnxGvh6IncwbAn2T3RF6RFaT5hNi8_Nlu1Q7yFA4wCQ3Ql-t6yX1cJOGHFrF6tQsSKz1amWbo0KAf6N3feXmVzwUCJVsMKXiE_zZODB-6dfL0L5_StTMd7VP0I0p5N1aHZEzhkOZ4EkvsGK5dlsK8JQHKiHsSn6QEmA56TKrDFp65ya1wdD2Jz9JxvZTgRFkcLzD8iiIhD38HG4pvRemf6JpZKOaQtbJQjELiFzccaoKuMQ3ReulN6GDjzWC-g-_o5iMVqLYbqRffT3OD1W4lok8lBscrvNOSPdGvMlQKui0f9r3fPpRWMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goKFsU_9TRN-ta3XCsY2vO_nFKzN-I6ZYRMLXxBB1CBMq5u_HTrwqK-cf_guu5WJ2EqVSUqktWAaz6sYxJm5EKqay97V3fQ3OH2mLTxwLZK5YMh1j9LyVKrs0S9RbMiTtcH070chnmr5Mxk8rjcOu7CJeldOMZqeRnwuUx0maJinlKGoaDDWZvrrebQh0cgn1oxMiDao9rqs4Kd84JxmIwJPvwTUKQ3Gh6bS1xFF-wL2LFG9MolQ2QhRhP0i4HSxZtKuJNEJOV_e3PVIVAGxvkzHe9JyjsfrjBMup3btJbxqW8UxFQYz8J8Nz0fJUCItJGg9lIMbCNdhhqyMn-4poQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKXB16wxGTL80Qr6VJzPhHpJ7A67Vhrkfsq7M7fwegkz6EXxQgbWMWkWxF-0ESVBCsjXk7oixamS3qI0iiZpzYdv01G08aurwuzQ_FbfQKBeVT1qqh6jg57zUdlk1e9Jw-KtPJRpRNoxCCg5Q-9dfrXShYw7Z_jnlFgOc0Q2SPy9kfXHC61Rw9DILrNnjgtma4U6b5RplIBaHIfwQ8DxsVJO1nQQBvtnRo3It0w4Zt5FWqeY6GQ19liYxXyUaRcdSh1IYO5AsSSS2Pfv8WIjceHapWQvpdfnu1T3CmHV3HMFrwWXN8GR6KYKmrmU3wA39-O8FwQXMoJzLpv304IEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJsqek0flmiukt4Z9w86SwvdsQoPf0wHxDBrmZSuiBGGk2uKbia1uH0R2WlgdyaBgOlsW2UQz8b68KyKDpnIczQ_Q0xMW18-2-sbAPM92FSdPXR1UZiqKgWnFb1Q2dQ9S9uanwwozZBoIwUk3TASLxKyYHP3V-6L10HE2PzuRDW8COAcX5IhQXPNMmhTShEvCJ8Lau1NGAjvi-XTYi5bkaxR2uO-Wc9SPQ9hzuxgL-cSKZaQPmWWdq4-osRT69uk2e1vCruZHoGajKh_FSFR_YKAe28JZvaE6d6Izzf8hxqvHlx6l2ZBj8TatxWQEwr-HBWZLY4E7QdTQP0CsHBDzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌈
🏳️‍🌈
فران تورس با مارکوس یورنته رفته تعطیلات
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101816" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101815">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEux3hSr_EyLFEDL3A8Z_Cekj9EORJmiIH7nUkmpeh84ChE7GYx8Vt0UbIrnkP7UETzBg36TKT49RxW9Dj2aGwi0CDgvphIL-1diMlwNWMkvn2WLdB6jDRCqgdLErTFFBF5Ya6ph_DMNA37m5olyy9BdLu71LiW8Tl_OSZLLO4GONKPgcGMtCUc8JILJv6JtzJTljV1_7qYe_1Zi8RIXewbc53DyNIv1Fq7qMm8qEGZRq9QKIwJirpchaWIIi2TTOX8GieaE6JxFeqOC11yWxiPoGC4x3cv8jU9H0FCeTp9JejoDklzlbO9ajOTMjNYT1sqoukY96cHQAbDYAgJrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال ۲۰۲۶ معرفی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101815" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101814">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbhFBmq260arm3fEGDVcE0ASX5xKIVgqwTh9b4zcI2WjZAr8YKYqlD0ce_cF9Q9SpmLO8Nka7tPhWBlrN0Myn49mK-OS9cMRjXqHxxtqboll8ttCSX9BdhXfUY33H1QDvFdpD1uaYa41PsJiuBU8ES_AvKviigh9h0wVs-RLX8Pc_w1CsYnNrNNotLC0YiCtgFJpIUuvp08iKUXm0TFRlJuqVGmaKffoN2wgJdTmfgQQn0GGb5t5zl511JpxYsayWX3mlaCiHm35p-VSl5VyQgvGP-fc_F21XpM9yT8dWxZlIb1DMneABWmDKPx0rOU_PZsJN6GrZG_KHJW9THxa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101814" target="_blank">📅 21:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101813">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3wsmScmC8GSoOd1umJuMyXs_IAoFkgVN2a8KvxZbPpjtwbaHM-_9Xa4ImnKUqRSEfFQoUfgRHBbTcImQG-7FZMqMJKZ7hXMPXG4dzEzpSVrUWwgSfth7ZPeqPmr0G9EHWxlWR8zNSkY_Vvrh7sQ1-DIwnNa3RiTEQsWtD3DEoLEBJS2xDgO9W-7NfIskcXe8wiYND7RyvO2b2pk7JLJGOoVUXh_yuvuoGL_MlNlAL4wiNO8CPNgmkDwPK1rexZnCsN7eCLM7d087a2M79Lc4KzWyngJu1VKJPNi-4x8Epi5JW2KiLUqW1q3xLTGwDnZY4QFXAJrN9lbxHYP3dZtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
کریستین فالک:
‼️
بایرن مونیخ تابستون امسال مایکل اولیسه رو نمی‌فروشه و بررسی احتمال جدایی او به تابستون سال آینده موکول شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101813" target="_blank">📅 21:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101811">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWN96zd9e-f4EDj-eq2KcxFj3S8VRosoActk10afebmAJHJi4dboBDktd7Yd89dFZPcHX3w0daS9q7KwmjyewzULnDug4HSm-0ueJG1bl2meA1aPZ-GT-BKZhEpAQjdvGIPEpf1UdLrGHoROmiP_wFmZQ7CteZ71cenomBp18pJQmF4rhpPmXhVWfL5xe03q-ScPK_iVrWPg46_bGox-T6idbauZYJcp3fpY7z4diUnWGIJO77JKC_u2dsLBuO-AOAMhSw5ylSX15tln1gJ26dytJ2H05j-2sm0o2ZjOKvpQq5C_dB9W8oXctajtz8_Z5bUxsOD3qQrBJG5IvyyDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4jUlj0SQCda3FQNcScC1W-xtJxYpNv3Rss0Lz3Wyw_Y2DXX7qMEVkUjCMYHYRo3q_SY0f0zaiZY4Oy19ognjlwVzYkam2QSODUR2dp4gaPjFZ_RKB-q4RneVnGnk7wFBhNQkbhkH44Oa3WXU-lzRumc9KpvMkhro2kHahmxycwPAXdWXjqYiRLynB-K1X1bjoZW3OHdIbGeyU8QxiZro6SC9YzhdVXEgB1n73EsSvAXa2hW_WSjRQtbXaLdBGuPKYFXhcJpXL2H4u6-2N-65L3ahsWR5KXzN7NmEZ1kfN6r7mqo5itubLLVAKLBxzC6J1ZchncTI6te-fO6aldR2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
💎
۹۱۵ روز پیش، پائو کوبارسی اولین بازی خود را برای بارسلونا انجام داد؛ در حالی که تنها ۱۶ سال داشت. حالا او قهرمان جهان است و ۵ جام با بارسلونا کسب کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101811" target="_blank">📅 21:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101810">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=H3CthBqaGswDpp9FkooNarwxMHd1P_iOVzwo7odUKn0I5TMQenNtkq52IVlw3zrHnKok6spXh6zavF0mW-L__TVWegJgtDfBbqgSGqFIM42eK5Z46nyq9N7V13ALyGyMusE--F_WfckgTddFjewj65Y_BNFS2vAvk5L9j59360Hv35nGlwpfhoXaqLG60wN2etOBqog18pWrDLBKTuV8NE6USO8PuW28X3H-bx3EZQxsHDO6SQ7ZheeCaawfGSYq41uNwqBPCrX57zoexxYUSbXs9H5u5wexbzmGF3yFx38Y6r0C_QcHLHJgBaF8Jta-AnHAFK9NDjhxM_qDwim1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=H3CthBqaGswDpp9FkooNarwxMHd1P_iOVzwo7odUKn0I5TMQenNtkq52IVlw3zrHnKok6spXh6zavF0mW-L__TVWegJgtDfBbqgSGqFIM42eK5Z46nyq9N7V13ALyGyMusE--F_WfckgTddFjewj65Y_BNFS2vAvk5L9j59360Hv35nGlwpfhoXaqLG60wN2etOBqog18pWrDLBKTuV8NE6USO8PuW28X3H-bx3EZQxsHDO6SQ7ZheeCaawfGSYq41uNwqBPCrX57zoexxYUSbXs9H5u5wexbzmGF3yFx38Y6r0C_QcHLHJgBaF8Jta-AnHAFK9NDjhxM_qDwim1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیرس مورگان:
چرا نمیخوای ازدواج کنی؟
❌
🔻
زلاتان ابراهیموویچ:
چون دوست ندارم 50 درصد از ثروتم رو از دست بدم.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101810" target="_blank">📅 21:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101809">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euCNY-lNNS7xn0eljc7imZXE-w2NH26cWJbGEi-QnDjRvuhImtBp-AVtPVTJVhdE4kfntyYmXxkUmc-1CkaVc5eEoB9inw02dD6ZhPi2pj-2B4QbesUaZP8Z1K0t1CW-NPseaYEq3cepU1elpjXcV-T7k0Kix5aEvbrkwJJNTpF6J3fyXZPHalV_cfDpJwRMs-oXiZSea8stsUN1xGt9YW_hcNNthLVxMQ_sfZZ8er5XVO_FthTjZVfSNXvmfTA4sSs2utOC2zro0kRCi-7h2rhjytXyrviF218afFX8osAQyB5jjcgGi7OescU3oYGjxg6dkbJkvs--1X2d_jgmjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
فوووووری اکبر عبدی بازیگر سال‌های متمادی ایران به دلیل بیماری قلبی در سال ۶۶ سالگی درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101809" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101808">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwxgWjgkgr9xuw87OzQxUMfadcga7UksRFgaXu60ZW-_-YWDngYr2ze3g_dBhR4aDUR1RhXyAlrz38m7wM4QjvF7cH49Jb25g-gOtjhFTUaCLXBqwSWjUDB3EvYYAVaehi9cqD77wAM1gc3RW-bBd5tplfQL8pDNpnRyt_-ZsOw1gjJegf5L6yvNhwAh04WaQuf0lmzN2dhb3ynj40Lgy4w6cgGSsv5nn6-YI2GuYYPToQllAgqhF67TBFfGlq_GAsgzKvQSmnKnXwf4d3YCOA0lRBIOucmo0Kgw2jbX68DkEQzNhErwpCYRBrWGpnQatTycZcxGIR4UkuMyAbGvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
کریستیانو رونالدو تنها بازیکن تاریخ فوتبال است که در ۴ سال تقویمی مختلف، میانگین بیش از ۱ گل در هر بازی را ثبت کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101808" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101806">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZXiJ7ZJiS2KhB3shdLUZ3FxeTbHfU61clTwrxOgzXYggTCCdSuwiVnuF05cuNfp9M1Tb89FJ6qfbyZhLg4VIbchUgZyx4Hfs51E71p6vddVD5RMKzH18szM5vSxhkE52FeHzUDnwr5qTWUd4BLTYmWzsS8aWDmG2PPdCn4ouiX5bgEZlTyE_wQp7ednZHNv4ZcA1rnhcyxxODeTvYqfaDID2j_0WbjSkrMYC2KkK0ROYbCoZdMPlzyFOe1MPPFdbOu7_oiLBawCJin2bXCCsy84I1Xm189JzaYHwx1CdZ9T2H0EkOnTkCChadBY_wTF8fYhFoREY5sHkjkcCnbuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=Bkoi2REqCarFi0ztyHccuCTC4ENq3dmW-1hA0VGUY11JQF50muD3koDnDeOZRy2O1TNbl-BVFJk2mF5tqeFK6eMK6lRtYLux8a1JJlYzlraKlpuDJb2Z1WDc8faD-LEdG6D91kfUjOOA8_JyjYxKecFAkKe5EWoY7FjW-sATH3sc3eUljN-dDMtvRgRQxK2BeZHvXP0NQCVJDoGxO2OffeQ4QsghWybZ_LzhEBIR6_UQ98MfxzqX3PhIuLNMFkYSaR3BiaHrCILr7bYt-0amlL-C8Dc2xOXDklS39CQSndYDgqpsKAC4wy2S-5XzxZe5kvLGUasBb_dr4-iQVCXqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=Bkoi2REqCarFi0ztyHccuCTC4ENq3dmW-1hA0VGUY11JQF50muD3koDnDeOZRy2O1TNbl-BVFJk2mF5tqeFK6eMK6lRtYLux8a1JJlYzlraKlpuDJb2Z1WDc8faD-LEdG6D91kfUjOOA8_JyjYxKecFAkKe5EWoY7FjW-sATH3sc3eUljN-dDMtvRgRQxK2BeZHvXP0NQCVJDoGxO2OffeQ4QsghWybZ_LzhEBIR6_UQ98MfxzqX3PhIuLNMFkYSaR3BiaHrCILr7bYt-0amlL-C8Dc2xOXDklS39CQSndYDgqpsKAC4wy2S-5XzxZe5kvLGUasBb_dr4-iQVCXqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تونی کروس، هافبک سابق رئال مادرید، بالاخره درباره توییت «فوتبال برنده شد» که پس از قهرمانی اسپانیا مقابل آرژانتین در فینال جام جهانی منتشر کرده بود، توضیح داد
.
🔺
دیدم که خیلی‌ها از آن توییت خوششان نیامد، اما همچنان پای حرفم هستم. به نظر من، یک تیم واقعی فوتبال روز یکشنبه برنده شد. همچنین معتقدم هر کسی جام جهانی را تماشا کرده باشد، دیده که اسپانیا بهترین تیم تورنمنت بود و آرژانتین نه‌تنها شایسته قهرمانی، بلکه حتی شایسته رسیدن به فینال هم نبود.
🔺
به‌خصوص مقابل انگلیس، بازی خوبی ارائه ندادند. آن‌ها بیشتر مسابقاتشان را به‌خاطر قضاوت‌های جانبدارانه داوران و فوتبالی که مدام با خطا روی حریف همراه بود، بردند. به همین دلیل از قهرمانی اسپانیا در فینال خوشحال شدم و همان باعث شد آن توییت را منتشر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101806" target="_blank">📅 20:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101805">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdetRpkX-IaULYBaMFuhqaCQrzGyOgx71P8vAF564fuB2P9kHWikff9Sg9L0TKiSQHHnrsFgAqjoPFRT8oGo2qoubM8qIFXhQnSOUFrkJs-iKvrfwSmbvYOWz6OSequ19uwYdzkWUBG6dYRuZZIwa3Qs_tSLbKzKOMXap3NDFEDrRApzapZ5r7H1rM8ZZt-M1lSc08axc_gC7pDJ_1Xd-DYw8jILdR_kwYNp7cdD4UpPZ4KLUgrvQknfjE8-4c0RU7rKFI-gbbWSInSmO3iac4e7jEwkr20AUI3b6lKd6dwYn-gNn0CVyl29zT2--K7K0whweV-fpjaKgz-IG9Z0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیساندرو مارتینز درباره کسایی که از شکست آرژانتین خوشحال شدن:
سقوط بزرگان همیشه باعث خوشحالی افراد معمولی بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101805" target="_blank">📅 20:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101804">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpImD531ym9jpkB9QMNCA9CfFX3SUQS1ZvvvzQPPNragmer-tZbz4OstlRfP__thLUc6qr7OpcKTLMEvWkHzQ_fJJ47VzbW-LuoM2Ih6GELHn9gGOe6dJxcZCv2voW7eRvjOA_A39vry8ZrEvPCtz9lRrDttFO5RkB_ptQskb_4lEziyPjZMTf-HUIlcvvle7C1S9PtuI_5SrzVaLpICb6SfgHvG0_AVPFT9d1zt6BUbFVx1eAcv6fYrf8BiHI1wsXh_KQnrIQjwcUjnpTbudAt4Y_XZXXpCsOxlT4viu_onxYb6OGsNonUTKSVUUxcWW9nuFJ97dt-q8ncYKK2A8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
فِران تورس از شرایطش در بارسلونا ناراضی است و تردیدها درباره آینده‌اش، احتمال جدایی او را بیشتر کرده. او احساس میکند هیچ‌وقت گزینه اول تیم نبوده و باشگاه ارزش واقعی‌اش را ندانسته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101804" target="_blank">📅 20:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101802">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkcUSJPywdAajBVBt0LBGKpnOslQw3d2gWhJm3y92NN-9-PTTkeknTkfoVfWgLKU1SquYO6OsiL8LxzU5T4xxBx3I5CMVixtAr8it2UDFP5KWoXEJ7XIbv4kpIYp72JgIMr3MzhJF63SyeCeOJlVdpyibrzXN_upGHIAgSDrDvXyneHnd97owWuVIaZ5epd01EBWUP3cMpzhqUIcF59fj2DRg1CaTnnRewWk2lfJkl21-ZqZ07r_4uLCr3u8TdzgZTTJ79NB5ZcvaAKN5O5AjxiT0YCOItkk5YFdCxLvoZf1qRgdGeL0v3IKKN4T6cwl9OyDrRGdN34Ymsm-_tmFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9SLn0myP8JiKbG_qF6fA2GYEhc8tbKS6tsQUyjwYIR5cyc-haf34YY2vJ4UqetMP--abVcZenk9WKMKVVLPsuREAGoR59WCpWpsGFsf23ZJpkBxcZgX1c-5qL6_gzqiC-s6WL5AM4-wfD09mJSjnjNZUOsbZ_bsYfrFIJe3brTe7r-tCcfND0Fp6qeNPitR9zEXQkUjE1lejdRMNvWJ3NTagb0qXNLwBxH508Ilt9dDqAJbTD0hWwoIqygFXb2giPWc5e2W9OD1Jrm6KD7NCWuhgNRcTAAYwoMhER7VfUxZUDaCz9MVQNa1n-lsURc8E_D3WbNav39ROEm_MrJnfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدن سکسی‌ای که فرناندو تورس ساخته.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101802" target="_blank">📅 20:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101801">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FajfY-5QDaz6m6yY6s06MIWWPtxh5fFdI_FC0dnRIDusHz8tvIx-N3DEdi4bU6kqhqkGd8i07j9bLFjVkvrHa0QvUJgfE-sS6dzqOSIA0-GbE48EvZwPWWErd-dj8XseV5Y7dy1hnGFEq45m0R5cEaat1_9AjPFZWJLoIXSvpfoDbVijCXt9dB0rXajzQ901hapfpwfRCXlB5cb4hK-w91Zss0sMjUkvvq9698ZyLMSJjF-Sgouu41l2JStXBY7dGK7UcCTeLc2j8jrhemTDRXseJY6c0us99sHeSteQqHQJUUEipBPFXo7vnRTfMvMbpOHVE_HonfjD-zjMS8M06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لیونل مسی در چندین بخش آماری بهترین بازیکن جام جهانی بود:
⚔️
بیشترین دوئل موفق: 60
🎯
بیشترین دریبل موفق: 28
🅰️
بیشترین موقعیت‌سازی: 25
🎯
بیشترین سانتر دقیق: 20
🥵
بیشترین خطای گرفته‌شده: 20
🚀
بیشترین شوت از خارج محوطه: 18
همه این آمارها در ۳۹ سالگی!
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101801" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101800">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYoeN-9h9KLX8z72DC9XwKCPZUd5dgRgLvpO-nyXSUvpUd8ynbutZiEBIukOPdb_F1bsGG7KZEw0aJaTbgf8V1gba6HehzbawAa36zCMDqjLEjOOOHwZJ0F_RlLUayYAQnloAQk9VoRG_iqI-PRegvmCj2fg_aCIIBaLUH1eXog_h39DmcvJ9P5cwbiDv_LHX5v9DA0XWPIg0DL-_mvBWdiKwZudLrxiTXt766zuQBs6ANykRQU7l1yM6aZJ5WSPlCjsHHKcp9eV6NBmdx8vw9rLeo_RvksEYOf_rmvvmEm8jtFv3DMxzaT_o4iP9NcOsJlNiSKArhJkdneBT20ftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
الاهلی مصر اعلام کرد که روز ۱۹ آگوست در جام خوان‌گمپر به مصاف بارسلونا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101800" target="_blank">📅 19:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101799">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyqw_xrrU-0-tM6kZorXwWoxh5JHTR4Aez_BfTjbT1iw6lkyNEhIsuxS0aX42s5UtgV8SYBfT9nM-0uUgrufYvTd8EppHYXNjr1BvApYWnVvnFpLyxfiwHe5IcMkNoHkRFVWEZDXJtzsRe_V-zQjVbpBSVfIFo5S89RCi4Le6FsM9CxqgboAWQ5dZ81kNI_YAbqoJIjqVBqzRoBuu8nqyiyWmdR7LSSyniYk2BH8dp3qewpPv1Z8oNaD8fRNG_VHI2C31VQXDikLxwSIsJd49qtIrROGnlCZxSLF2r-A1qBN1JB2Nc-rLO30FL3YeNvTeTbbhoy5VIvauKEelMt4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لئاندرو پاردس فقط ۵ روز بعد از بازی در فینال جام جهانی، با بازوبند کاپیتانی بوکا جونیورز در کوپا سودآمریکانا به میدان رفت! هافبک آرژانتینی از ابتدا بازی کرد، ۹۰ دقیقه کامل در زمین بود و حتی پاس گل پیروزی‌بخش تیمش را هم ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101799" target="_blank">📅 19:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101798">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC_J6gGFX9scfc6dFd0AW5e1Q7gg4tL34dY8Kcn58gPrVZAmmuwnd1hftbMADkPRy5Vd7NzAKxIpRBi6YB-O8ikEdiEOkdZ-W_GRjyUF47W4BLnjQpW6KGzG6plg-eLFAhBxX2JF0KzI-cZHAhOSGW03tIPbs9FYOmbGoarxa9uu_T5AeVBK2ahAhI8Ztu058yirLfptMVgtpYs1iTYrT1KcYL7sxvvZXEiJ90D2WZ5RBYegkhievykP7ygTTibn2LT5g9Eku97wp9vZBq-IypU_jJq4nEqJtBVqeMLF9JDLBwZhdJRZmen2Lu8txclLmmF_B5fyxcnEP2s5xueQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
فابريزيو رومانو: پیرلو به تیم ملی ایتالیا 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101798" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101797">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGotLQSyOfkqnNoUMEvUoM_raBjMJapylDhu-CLfLFV4aq54TzIK7DzoyFA_frkveJ8ny0_7Ni4ux7UcoNpLHJ9zEU2P-udpDM8W-xGcbH0-4AUR8C-saIsP5JII8MRBsH6ATA88CHWJstLZHZ9SMIbZIcMABRtgdYiYhhE2_kTFr6Efl5M8WoF129jXjcdkCMd7QPdxMQrabjoVkRM3J2mSGNeKnqYqO9jJTOmVaWWrNt-TZrp_GzZpd4j6vwT3sfIqVSOzrVe9XNvO-frarI0NPmMMmDpW3jLRQn7VvKbrl4MJkNzYCivMHyFmKolB_9ft0l-AmOq_Cj5fu5GcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین امتیاز ثبت‌شده توسط بازیکنان لالیگا در هر فصل از ۲۰۰۹/۱۰ تا امروز (با حداقل ۳۰ بازی):
2025/26
🇪🇸
لامین یامال — 8.23
2024/25
🇪🇸
لامین یامال — 8.01
2023/24
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام — 7.81
2022/23
🇫🇷
آنتوان گریزمان — 7.69
2021/22
🇫🇷
کریم بنزما — 7.69
2020/21
🇦🇷
لیونل مسی — 8.52
2019/20
🇦🇷
لیونل مسی — 8.71
2018/19
🇦🇷
لیونل مسی — 8.48
2017/18
🇦🇷
لیونل مسی — 8.68
2016/17
🇧🇷
نیمار — 8.52
2015/16
🇦🇷
لیونل مسی — 8.46
2014/15
🇦🇷
لیونل مسی — 8.84
2013/14
🇦🇷
لیونل مسی — 8.34
2012/13
🇦🇷
لیونل مسی — 8.83
2011/12
🇦🇷
لیونل مسی — 8.88
2010/11
🇦🇷
لیونل مسی — 8.76
2009/10
🇦🇷
لیونل مسی — 8.65
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101797" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101796">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVQHCcx78PpN6lotQPJM11Hp_aPNe9kJGsi1yxqwGUsEYiSgqUWCwyQkrH7XOLLmasmgRYI2aOi1igpygeBG8LQX5S7x8cMoSuGeAGBHh0Ac_3jiWfom7Ffx_JOk1LT5d2YER9kJl8wrjPnczIUz6o8lu3l1UwoNd9N3zNmQrmrSRDzH0bxPSpsGJyII4qZ0RWGDgvX9ix_mF--TLalgotRmPhBqGl0PNnO6GoIrnBquxAqTXZGc5PnFs4O6pm3SWjc-7qVbDOGJ-5FiiL7vNzmuyKUlLM1NkaqbkYasf69UMINz0xaEc-_rQ0RB6d1QZzsD7BKyBEDCZwNx_be5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💀
مثلث‌خط حمله فصل بعد بارسلونا: GAY
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101796" target="_blank">📅 19:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101795">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrDyMCxWa_MXZ32hykJ3kGDrLWXHGOUeIZlhXbQki0rrBXTixQbgq9IEtlr_lfUN9iYg3KAJaXnmnMh-fpvjISR2QUSULRv6f0dSbcHF33gUgZgIbz-iDhcFLR6DH7i1aMm5P_jWEXNNIIOBa454Z2Tq7fHqPaJl11ULO-V6vGRaakt7KeTSMTHuo6kTC1jHc3Oihibw58WHcKtOHEYlejBnFewcTwpCSo77tEL9wMRJG0YsKTu1Sdhystl1r1vtCnv6ZzBFnoCUxFnz91A5SIXh-Xo50itJY9Rql88SmtC9xu6lncI4-Uf8tfhSkFuUc5v9imiiOF_gLdnIzqT0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
⚽️
بیشترین دستمزد هفتگی در سیتیزن‌ها.
💰
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101795" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101794">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
اشرف‌حکیمی و امباپه در کنسرت بد‌بانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101794" target="_blank">📅 18:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101793">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی همه چیش بهترینه، حتی میم‌ شدنش.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101793" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101792">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
عباس‌عراقچی وزیر خارجه پزشکیان: توافق با آمریکا بهترین توافق ممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101792" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101791">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYT-e6E-u-MQjy5jlesN6aYjZUy7UV7dLQpMyZfNtlAiikbDHp1BDBrnt4WT8pD2SjnCK3Ezxtg3T0iB2S48B6gZ8PjuSV2Z9yRz7curEit_doV1m_FWcUZoAorl_B6A86fjyO6VzcuYshyVj1tuy2-XST8_xPwDjU1qFG3U6KEdakusTuD24iFwRJ5sCR0gth06buRh3WOkxjA1aiboyWbDebDijPWp5dcbru8lHjtqlas87rOldCwYxBPwhcAAIvr5k3AytPy8U_L4h8uXE7-9u2nHMupPXJS-EhsOtwppPJK69OmalaQHp3d6u4l1O8dQCeBrIVQ2fEGhbZkKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
💣
💣
💣
💣
💣
🇪🇸
خبر فوری: فلوریان پلتنبرگ: رودری اکنون به طور رسمی یکی از مهم‌ترین اهداف فلورنتینو پِرز در بازار نقل و انتقالات است. مذاکرات با نمایندگان این بازیکن آغاز شده و پِرز با این انتقال موافقت کرده است.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101791" target="_blank">📅 17:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101790">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👀
یک استعداد دیگه در کارخانه لاماسیا درحال ساخته شدنه؛ سال‌ها بعد اسمشو قراره زیاد بشنوید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101790" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeTRckbG8rf501Apoe_jADIbMkPG5k6Jua-PY-EnkCDOs6HHk6CY3qoCpZ6zYHWE7IJldiBkxwDrOBqKEBPVE9ir_22wb7uAsYlivdRCyv7Ihfz5Sx3gkHavJFG9K7yvH10AzPG3IBO-cerMq2qk6XjtFiEd6U0A7Il1TM5au_ehYPJzeWyYrYuCcbA_wyt5CuLYkyskDcrhieguou3z9mWveARJwh7NtqjHNMKAyye2zDYYa02617uDVw9Chqp7vPovzDkvp30PgPoNKoE41i6ToDuvIW3TMfVIGGw_6_RriLu9y1BmOY5Yacux49jszUU-BDREAPFQ3JYA90PDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رئال‌مادرید به رودری اعلام کرده که مشکلی با عمل جراحی مربوط به مصدومیت غضروفی این بازیکن و غیبت برای چند هفته ندارد و تصمیم نهایی برای عقد قرارداد به این بازیکن واگذار شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101789" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101787">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFu2W1LxLl_tyNaYbEjhCnmc_PvM5h1NNvzARypqy6mlPA8uBJ-8Ea1eZ6Sa5WJUVqxL8ofGUVAXgjE7CR2mZFlHo2UUweNy0gIB0UOYWR2B2QZTkN-8pd94OS5sRqcwrzlmclHfAFRQa7MmBbL9_10KVcn0_xCjgeDQRrFf7R0A70KpDd8i6-Pn9A41GWMWHsTFXf707klsOGlXD9i1c5BMKJFIfyNvkCZiTWRbpzxvz_9oH5mdiUgOf_zE6G3SPJ2Uzj_iCxI7VbmXzu3HWGSkr-ZU6HtiM2BjBMM1DzRkicZkDlEN2DVDJ4kUF4QRK-CbJVjQ6yRW3mQ1AluPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkoJAMfWh5xPhnb598VPbSoK83FjceEZ24DUhknybM2SbCKIy-I2QTzl-NiKiWXoyMrZ-031Iq7CxhI5Ob4Ca8hLtBUozG3AWQUzz53wNTfrMGXzKdTa1W68mfuMnEAz-KKlZKmODGkDNpSJKPNAlijw6QFKs1LFYsQA4KO3wmm8FRSzEpv1rn35BtvjukG7lu6zYchX3-u0bexxeyRP6fCH5dun7bLfPVApRw_35q7py0R4_1JT1u_x0HO_aJk3VWtiM1L2m61uded5wcxr57ykzObnZWLGnxoHgIGzQW4_l7H14inGwjw_84qn9gxT5iLCVvEHtUe5nctUZtw4zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مشکوک به نظر میرسی هالندعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101787" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzLDowtEaEwmYu3s6WFGqSZfioBM-EK6Cx7NMSri2YxyoBPqrWV6E9bXkM3oWdc7Ik2cGsWSUb1_bwFz3gLHLEqEXYPSjQtIF444adA_CgBBEtakfQWXiDSIvK6N8RprY2v6gSwKUb-pIS3hIyXqXv3OoJi2nxOOcitCz4DDnTsZNRQQMcacAEfKlCGV0vtZgEiL9cZX2y-q2Dcn6NhSBlyimeAzOBVJxb4mEgFxTNsG0--VHSj0hqjqh1QYNFPVC82c8NYJziPfd2ilLDlpzt-i6y35f8A0l1IqS7JBwXLDCXC4GZvI_8ItS9OIL3yhTRs24QfxSeZugBdJSzviag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnoKGlEEvvZ5NJFspNoAQjhWZrDLmQ0UtXD8-pauxgeiwt3bOBCyD-ju3orc08yW7d3AL5Z4ZUG7mCry7MK_7etdT9Z5raYcVxQGVM8ovKWp-VN2CaSVKbwwTQ-grSdo_OX2YImWoKwx3LquG2v_yyG-lQiqPhOljFqpuQPF1-lrOs9cZk-zvXGIVsYOXSnVL2e5Ov4uq7W5XYlUWO9AFzsCsjZsVmo9eHBOGM5zxqHEfm2-bCI0EK22v6rMX-H6tGxj7hQBoRzBeIsTGoy3JsaQ22wGIkBZlY-tzp2DGDYZpV91kJPX9YOM1RqYwFlL6N9tRMRSUKBHnLJTxvfx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇹
✔️
به نقل از گاتزتا دلواسپورت، آندره‌آ پیرلو سرمربی جدید تیم ملی ایتالیا خواهد بود و این قرارداد به زودی نهایی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌قایدی ستاره تیم‌ملی ایران: اگر میخواید عاقبت بخیر بشید، بچه‌دار بشید
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTBsOkQ3od8OpQnPP1ReSA57N_P4zA3cvX6E4_47rWgDICUfeLa7aJrbZNsGNP7IhEFkjc2m8YI0jyblU7GZ5ZEPEYJNP67esFSiLH80IQQoxE8xh_Lu62c7a758Bchakh0hSIhSjnsHWm9nlPtfhXKhn07a7U5gPF8p-dkmHqbMgzJP1MxvIhzXl3H6-XpB6D_qyLdKjwvKBhG9MjOILTj9d76UC9INFTLOLEXx_G9Z-xp7uXZQOVx039tgOrkVF1wx7ykvg1fu0v-T672sw-ebn9nPQZ9toxoRE87TdmSDX3YXe8s93BW-SSExcOmEJetoy7j2XXHRt4I-6C37WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avuIHVUerGqT3mSBMqqFQ2qNcGXUK0jQ9y8RZ-cE2Ml-6M3feHXBNZoN6SRInCGz8gouE5OFDMdbXrG9w-wWwx39akZszjcEWwcmkW5wC7AcwNEwsR8tDIj2G71UDUnFbPWO2wsSWnU1H-9SXlENDSFZHtHwOiJnVxAYtz7JjljRF_wpuJ1LNu4wN2S4OHP7ZKGB_Nl9-K0ifnC5fPgxg7TMiqheqrFqgEKX7TAEmeK9QcfMtbpq6RO3mujyzDWIg-BTgCm-6Jy_Ygyxohmt0hSV5wWQEovHjw-gAhrGSnY1a_tpJrCWB04ESEQ2ssMrFZtIddTqQbsWPiSImF9zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101780">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_znP4s3fCsr8s_6r2faaC_mmBR0FXME12_t241SZqZt_pu_sJsbjSnj9YDPpF5IkiyH2zcB9KKFQSNBJuml_3F1iS4TtA2zm8N9av1qIE2atdhMYdydyrSe4W8lZV3cYfTB7Yh6Vck8ymMX1rPutlc7r9ujZ_MSc9762d0mSV1FW4WoUlNXrGQaXeInAZ4yhYenVsfovWu_LH-D8OI8938Lw6GvDpzbr-T9WH622JCHFtWihCPwEXB6OgLTTbyQMASqHdHydJQlVzj_L5TIu48CX9YRGMFv7arAZcIUFRtmTBRZUlpDlLQj_S3RpXDmqkYaxXDcbhfqwb3FPMHkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینتر دید کسی حواسش نیست رفت به یه تیم از دسته 5 آلمان 16 تا گل زد. دوستانه نیست این دشمنانه‌ست بیشتر.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101780" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101779">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f574b376.mp4?token=o-rlC9m92Eu-lGZojSuhfvq8j_HF4Xz_G54RTn47zoj7Y3Bu441j5oURZJcSsVKWqtSxqeU1f_EwxaTnRNVVhtNia_AluLA0Q8VcoaVHpy2-ywdxUSoWEZupF8G_kmk6eDAAqjEQNE1tu8m26o8_ZeUFJylkOAhqjnfEaHBehJglwt-wpX80T2aeXHTjcihBB2jxPKTRM0OrxyPS6R1P_G9FhRXuUF31ENiUR4VxclRGduv2VG9zpkohuPLaRSEVvxa0PvrVd2VBhmf0Lhgpk1me1Szr_5NSlylPGWurGgPlbSG4hEQeGIiQAlKUNVXGbcZr6XwlCphxvXokaL_sYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f574b376.mp4?token=o-rlC9m92Eu-lGZojSuhfvq8j_HF4Xz_G54RTn47zoj7Y3Bu441j5oURZJcSsVKWqtSxqeU1f_EwxaTnRNVVhtNia_AluLA0Q8VcoaVHpy2-ywdxUSoWEZupF8G_kmk6eDAAqjEQNE1tu8m26o8_ZeUFJylkOAhqjnfEaHBehJglwt-wpX80T2aeXHTjcihBB2jxPKTRM0OrxyPS6R1P_G9FhRXuUF31ENiUR4VxclRGduv2VG9zpkohuPLaRSEVvxa0PvrVd2VBhmf0Lhgpk1me1Szr_5NSlylPGWurGgPlbSG4hEQeGIiQAlKUNVXGbcZr6XwlCphxvXokaL_sYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
برخی از سوپرگل‌های لوئیز سوارز در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101779" target="_blank">📅 16:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101778">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چطور در لاماسیا، مسی و اینیستا می‌سازند؟  اینیستا و تشریح سازوکار خاص‌ترین آکادمی فوتبال جهان؛ استعدادیابی در سرتاسر دنیا، مطابق با استانداردهای بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101778" target="_blank">📅 15:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101777">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">▶️
👤
به بهانه تولد 49 سالگی مهدی مهدوی‌کیا ستاره سابق پرسپولیس؛ تمام گلهایی که در در تیم ملی به ثمر رسانده را در این ویدیو می‌توانید ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101777" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101776">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfurPxkr3b3GGrFzNcrw5UewEl_jYP9757ujNvUnLRV2hbQD6PnvKtS11LXsRaRyrI82sZYc-tLWOG6CrFXTdM3eSD9qfRmMD5p8Ka7OXDwbRa4vPlpYvtdRKHUTQg9TcH4krxXTEG2Nhdro54r2YL-jx3or2-hI_GzOXDArFsUXHm_ZDGP8bLZtNAxOyjBSCpgZ2uWZ8TS0hN2-i8IxpOoqKJVNuyUxrhSf3fwDGQ4I6MeMBqUDsoPyloh37i4YvknNagheTB9T1ndAk2fkEmEuJvbIpwPJxr5KLCsf0orN0Iu2VFR1ERMkCeVZ7IWqKUF2PFDVg2MFzszi2cqY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇩🇪
یورگن کلوپ:
با چیزی که خیلی مخالفم فحش به خانوادست! اگر به خانواده‌ام توهین کنید، من می‌روم. اگر روزی فکر کردید من مربی بدی هستم، مستقیم به خودم بگویید؛ همان لحظه بدون اینکه حتی غرامتی بخواهم، کنار می‌روم. من این کار را برای خودم انجام نمی‌دهم، برای شما انجام می‌دهم. با وجود اینکه دیدم با ناگلزمان و توخل چه رفتاری شد، این مسئولیت را پذیرفتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101776" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz2sQB_9XbpS2IFCYHNB4glIn5QlaxpZCTvZd1hID2IVMohFsprEopYm8RhotiOvIYQeTe-9kDWqwtzpXRgx7cb2UwCif4imS8vSdLiKwXj3XX7I2PqYl5nnd2VNjoEzdDVh_yLD2o_LA0O0MddM45z-E9KsifxJFVvL732Z2ADvh0OEIH_AXk9UVDx_XGVP_zaT4na2FS4T4t32P3pHw-qULSlqlE9Hi5ePz7-JLwdz0Tw_XGutHeKAERDs1rjVLacWoIMRH1_uvzd7kzkqcvivj0mcI5BpIEJrBmPrUa15qqsoB6-OLx7xIHwl4oZ27AC-QjdMJc5lTUfcbmp5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjSmTxAPBxbCDj5MDDwlI2QLXeP7wLW6pTjB0CCuC0x0JJQnECZZaxDRbKJYz_cX28DSME5DBYS9yHL45YQ9r4hQl610gnYDI4fHef_1p_nSdCRktIAFgP5gu2HqoH-7rInerF-U5xfd_Jut4DdsrL9Ctzs8Hld0EHEGPgYZ_jZW_66NP1-5jSEb3VU3gotWE0_0VDn7wQZVXNoe-TjYD3XhTyIcXMR7_gm8AWHXp1rezY0GqOWBOm4zNkomR9XK-uiNY5zOUycljKSOyGr-UcEgXbr2zCRuOjvl7JUU-zXtOJ2uA9730JiSTLI8BsN5f3-3ZIlOJ4DTViav5LMsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4CTm3hLbjFEnGh0rcnfL3rcOdUbsE1Oc2WzETcydOz_IsMHjVdX9F3Apq1vFjluUp9gr6qGBWVwRepFq0vFdXCdbgxIBRQZtpDLEQwkFRwn03F881olokkWwaiHJIn7vkYWxgqissPDvU5Z8rZOrrHFCM5tugw-q0XZ92yB3SS7t1Htnuyka5V_IeZ04fyyka0nx2VVpr_OnKTBlYxnuBFNPxum82RVIHinCrcBdjYWNZFcuxVWKpVAa9SMtFlGNC-uxqlAFaalY2B9WJMpnYE7NCFaBj8cfmjoyK3t09u8CVKt4fwgaZACCAI-GmBrW1S7j87fu1t43OvxBIEBSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOM2hYRxEjAXmksjuOQyrutq_2i-oNB1hwBwwikcxk3o_X12Bj58qZemD7EKt-dcXZw1SB18EQvZbtDcGekehcLG70YPK-FKTReE7kM-CiqVktS5fswHzQbrzMUF4FfqBzC_UXSXTxdpke1jjmIt6iq_pXo85MCPTUkdZ9JSGANcxnwX_1LPx-D4zd1jUiFiTv_xJ6G0ij4-94xnSkF9KEASm1uwyEYt8XYT6cptz_8t1yUZAkJnrP-O_O_h3tNvPkUr6gPIVSe2tnwZEy_mZhAOPSwr_Jh5MUW_2PXmlG1o_8qOYetsnobCZaDEReuVYyqDq9g6vI9SZh7O_hT69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRR2SY2iTpczGtmgyqOkUoqxIdVbJF3lwDnKzaRK0KhoTHvWUjv7NsmM7ZEWJ23TAT_vpvWabiJPdYhtwUvkLxf-_j4tWGv308kM92vUcFcpNmpZm8ImQ7nCNLpIfnHa2dOL0WhfRCCEWkvnWlIPK31ZETZBeSvxIYUmwjyBWhk2jtOO2BVBlUEzhuS8lJmQIm_O1EhRnc8sF-FafOHlgA7hteVMuYMq-Cjvj_dcAuwTODVjlQRmghLxMkM2Jthlip4hs-24VLm7TBjRemX374xsVMmJENwckt0qLWNEgTgvQxeBBCT-sMNGHy93b4wlY7Nib9yvGRJZ_Tph2oogWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2YSFpK6PmnyiQhEfOBJg4VEa9PKr3cms92yXo2RBWD4zU94xpVO1b2Ym6IymYUmIV7mcAti-q7C8v122h3iS4L4gdo3nUjZM4jthS_t2j3esSIEStSIx9QOvKd2EvUjm_V57cZm6P_R8OMiuibogH_mftrDML_Ppps9rmADrBx1nDzqoGsLOpDN1btfe54lUqy8l2AXyltOm6khRtyVO2JYiH7WVe4SEXxRdb5DtpI2NURGVX_pP5ZpRsRevVr5Dj9ZikGgNSavPGb3GMtIM3aT-KUg1n-BMR_PDvui_qNyL4HTOY8GBfKYkqiuidaqOZjfb2QcCSwaoM8W4G1Oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
در چنین روزی، ۱۶ سال پیش، ماریو بالوتلی در جریان یکی از بازی‌های دوستانه پیش‌فصل منچسترسیتی این حرکت عجیب را انجام داد. روبرتو مانچینی آن‌قدر از این اتفاق عصبانی شد که بلافاصله بالوتلی را تعویض کرد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=YpZF0tOm-yt0KZMG1-1Knb1P-gF9T-LRz5p4UAGz8HpzHJP2ohNJ0_BRxO5ZI02Bj6QUiGySZxdnz6VgDw3XNebsxj8mSUAlvX1aFuz0aqFWEaxftcLJN1tuunyz3C0ZGYL6rX5do2Vgq-067yGr0o_SJDGLJYl_tbRx7pPko_MKno1neVLOKBBwM9he3ae5iVElja_O1UIILNudkZhqsAeIkSPspi4UdpjPdt8pQ-HKX_iubS6DcxI819vrI0_oOUArXCXXHm_95jdFERpsDRqgyfjO1u1O_i3tdGTpYZHtmsWBav3qejAmdvA8tGf3GnlNm__a6rPeAHapE8R7bzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=YpZF0tOm-yt0KZMG1-1Knb1P-gF9T-LRz5p4UAGz8HpzHJP2ohNJ0_BRxO5ZI02Bj6QUiGySZxdnz6VgDw3XNebsxj8mSUAlvX1aFuz0aqFWEaxftcLJN1tuunyz3C0ZGYL6rX5do2Vgq-067yGr0o_SJDGLJYl_tbRx7pPko_MKno1neVLOKBBwM9he3ae5iVElja_O1UIILNudkZhqsAeIkSPspi4UdpjPdt8pQ-HKX_iubS6DcxI819vrI0_oOUArXCXXHm_95jdFERpsDRqgyfjO1u1O_i3tdGTpYZHtmsWBav3qejAmdvA8tGf3GnlNm__a6rPeAHapE8R7bzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOkzyQY9Aq8LYOgRicG8CiOT99_bn59VuJyWgol9xFG2OeQoshafkuyH-Unyn9x62DMKKz3gO-_CacoSlh5_eZFeU7XRA-A5hQkHYr50-XawdrsBOFL62N3f8uYJ58CyURtwM8Bjy6TAGza1KPYDWAtN9mlyWh1BYx_vhOuREJISfREcbcbD_kvi-oFLF8HyT5MrdgHHZ3A0juw6GlOVxLcj0Bn3Q7y3ehKRUGdk96qa1sYhTM7pXTCzKB3BWLBU8Zy7ut2brbKfWBkD_RfMxOwMMfiIQEH9GzrM0Vpl8mruVy_h_Bc5tP2o_YFP4s83rTMvjORBUMWzczS7ndRIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101766">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=V56_DhlwhgjZFdkybRJzjCD76SL8Hby5bBkEnp0OBw6er7XE9h59lb3UTegAQsV-C1ilI3YOLmELUESEP7jDIGkZS3IXeWtPiUtUbjCh-Wt2AHkWm_hhmnOdkev_GiCODWAi3N6m1fDkhfnsx7j-BZQILDITXdTmDCUqR5M80bLODoMlB20Ir3RWA9cx-1x10rZWKcrJALAzQDcBKTHDLOKUTH-hsug_V7cm5QobekyA3mnbOVPUGE6e99aNJ7MEfIIED0rJuKSmdlYzPUZa8BTTwIMpcZkpaDMeTI3COwq8CXDvQMt65JB8dmJ2Q4-C7t7B5c9Rsl7lcyCgzYjPZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=V56_DhlwhgjZFdkybRJzjCD76SL8Hby5bBkEnp0OBw6er7XE9h59lb3UTegAQsV-C1ilI3YOLmELUESEP7jDIGkZS3IXeWtPiUtUbjCh-Wt2AHkWm_hhmnOdkev_GiCODWAi3N6m1fDkhfnsx7j-BZQILDITXdTmDCUqR5M80bLODoMlB20Ir3RWA9cx-1x10rZWKcrJALAzQDcBKTHDLOKUTH-hsug_V7cm5QobekyA3mnbOVPUGE6e99aNJ7MEfIIED0rJuKSmdlYzPUZa8BTTwIMpcZkpaDMeTI3COwq8CXDvQMt65JB8dmJ2Q4-C7t7B5c9Rsl7lcyCgzYjPZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
مصدومیت شدید یک ورزشکار در جریان مسابقات مردان‌آهنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101766" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101765">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=AOPxc_PQAj17MQ0nKvSqaik-xZ_q6MsVWb1ELwNWo48r_0k4UQO1BG6QRrNQgrGKf1nnjUDpHOEKA5Ume3rJlHkS1cSswrIx6FgsL4ZBry5LuZy7f4v_iJgnbXjcoiRqWCe5S66MglaqFEbpYqZe67rHg2ZEFnAs4fbypu0p-DoHnj1ACP4PnKFSUm3mOLK4e698in0-my6cOH5OnEvM6yb3YmR-sliohfbwveqPFbrCli989RYVyj9ARI_CsNdiuRkEqjHRO0UaMmRWcPECSOFsWDuhHzJvMxNtRhjakLjuogb1Mgs5iO8J58aeGEhlzaAf_lL-JKUUPcXRLapqFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=AOPxc_PQAj17MQ0nKvSqaik-xZ_q6MsVWb1ELwNWo48r_0k4UQO1BG6QRrNQgrGKf1nnjUDpHOEKA5Ume3rJlHkS1cSswrIx6FgsL4ZBry5LuZy7f4v_iJgnbXjcoiRqWCe5S66MglaqFEbpYqZe67rHg2ZEFnAs4fbypu0p-DoHnj1ACP4PnKFSUm3mOLK4e698in0-my6cOH5OnEvM6yb3YmR-sliohfbwveqPFbrCli989RYVyj9ARI_CsNdiuRkEqjHRO0UaMmRWcPECSOFsWDuhHzJvMxNtRhjakLjuogb1Mgs5iO8J58aeGEhlzaAf_lL-JKUUPcXRLapqFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
افشاگری پشم‌ریزون اوجی وزیرنفت‌ دولت ابراهیم رئیسی: موساد به من زنگ زد گفت ۳+۵ چند می شود و سپس خط لوله هشتم انتقال گاز به شمال کشور را منفجر کرد!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101765" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101764">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=L5gcUHI2c6gWKiQqNvFOIwVsxOTul_4ebyoPW66tgwEWq0Mthtqc71IhWTUkRjd1x-iVmAHA6ZKTGBVYXT_GdyRlTJjX2PxlWxm4ZUgc8KRT6TkOz_v-pnIXIgG5jtZEn2kRD7hwHx2H2i5GR-W_zYw3YAQQk-hNe53uSV-nWQH44PX7dvXHBYqvS7B_mD9ke99FNcnUhWGxIC-CfaT_1hf_Xus61Tv7TvMjfZJjN0Chp2pV_Tpp-uzCkX1f86kBay7Qp9yMwCX313mMdxgXsdvfi3xL3giIg1e6tVwkAxLVSYvL2TLbphFbMtKUwPn8HX9xlk8nngZXEkIbKlROfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=L5gcUHI2c6gWKiQqNvFOIwVsxOTul_4ebyoPW66tgwEWq0Mthtqc71IhWTUkRjd1x-iVmAHA6ZKTGBVYXT_GdyRlTJjX2PxlWxm4ZUgc8KRT6TkOz_v-pnIXIgG5jtZEn2kRD7hwHx2H2i5GR-W_zYw3YAQQk-hNe53uSV-nWQH44PX7dvXHBYqvS7B_mD9ke99FNcnUhWGxIC-CfaT_1hf_Xus61Tv7TvMjfZJjN0Chp2pV_Tpp-uzCkX1f86kBay7Qp9yMwCX313mMdxgXsdvfi3xL3giIg1e6tVwkAxLVSYvL2TLbphFbMtKUwPn8HX9xlk8nngZXEkIbKlROfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
پیرس مورگان، مجری معروف تلویزیونی انگلیس، بعد از باخت آرژانتین به اسپانیا تو فینال جام جهانی ۲۰۲۶، دوباره رفت سراغ انتقاد از لیونل مسی.
گفت: مسی فوراً دوید سمت داور، مثل یه بچه مدرسه‌ای که می‌خواد یکی رو لو بده، تا باعث اخراجش بشه. به نظرم این واقعاً چندش‌آور بود.
این‌همه از «سن‌لئو» حرف می‌زنن؛ همون کسی که می‌گن قراره بهترین بازیکن تاریخ فوتبال باشه. ولی توی فینال کاملاً محو شده بود؛ انقدر که اصلاً حس نکردم توی زمین حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101764" target="_blank">📅 13:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRPPS5U-TMAwt1O21HUMLDYvTLNa8o6aBy8yf1aYIcywzX2OGXkwHKXvJ1Mvh2wJohsZ1ITYvxVRFAs0vjz9XtpFMPQXEMwDvGNSK1wVxg5eTS7rGUlYOueRUIAMaOL6CnOnV52CzQkuq4mwQyovEw-qBNcbmbK5g5pPhYHHPCc4MzQEh3d5UrdSETJ76i8MPcXAXwe05R19uSPTvJIR6lFbZXQEUaA8ZKzGLVGGF52HyH3IVvd5uMwIBdk2i-aD9zjsmXDef_0JVYbXeLf0ujHabaYnobdIO0mIThKFM-DD9VyXcZZw6GdW3lD-3FV6CvkJoM1W83C1HUUc1zYJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=u9JlttiOJ_n84n3sPc1xuKKAAunR1bgecw5TD-ckhip4JKBM_X2n1PZG6UURESRC-AzDxhtkF7FcGnjiYaAz7PYWZQ2ejjFCD3FUIOsdEJqJ12afzaJlgawJRwVk___5S77tVY5TWBBYiFi4Pkh7YK3kplQt_dtYp_uPIvgqespA97MWikYYty2NA70iCQukm8QskpNVZsDXXu-zdeV_foKKO2iB9LhMeUBVib1ocTZlu-bG7udiBR6TAgZzxLup40i_IXB76GM8SG_OwZy1Clr4_PpMxoPhvSKe6rqSxrzVv7NRWntlQW-416e4v6lYzh0K4uk7SVemBXb7Y8kh1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=u9JlttiOJ_n84n3sPc1xuKKAAunR1bgecw5TD-ckhip4JKBM_X2n1PZG6UURESRC-AzDxhtkF7FcGnjiYaAz7PYWZQ2ejjFCD3FUIOsdEJqJ12afzaJlgawJRwVk___5S77tVY5TWBBYiFi4Pkh7YK3kplQt_dtYp_uPIvgqespA97MWikYYty2NA70iCQukm8QskpNVZsDXXu-zdeV_foKKO2iB9LhMeUBVib1ocTZlu-bG7udiBR6TAgZzxLup40i_IXB76GM8SG_OwZy1Clr4_PpMxoPhvSKe6rqSxrzVv7NRWntlQW-416e4v6lYzh0K4uk7SVemBXb7Y8kh1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=l8tGYoQCbmqHuz8OA0pS39VrgQH98LQrt-PXjEBfYqHhLeygZfJjdCkt4WMM3evG3wGWC6TcVhXpWDWFynFTW0bK49_PD_N5rL6aoNPfLt_qXpjmtqZxm2jbhVy3cj5yNM7vdNpq7ZRmY74BXmKR8GE8Hi5TvISYcX52_GkrG7dwHSUnjNja_Sj_x8YrBnUrPQ7Wrc6gkTICgFIaaTjQ6LcqiM0E5-kzO-K5tBzWX3YJUx_TiTgxeZ9FvRGFRx0mqfWJ1JCEctp84vzzy0w6FVOx-bh-c4BaKlKnrq6cBXNB_oo3Jk0K3h_nrC6GErzmkDIvcLq-6YH-ey5WmI0ZtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=l8tGYoQCbmqHuz8OA0pS39VrgQH98LQrt-PXjEBfYqHhLeygZfJjdCkt4WMM3evG3wGWC6TcVhXpWDWFynFTW0bK49_PD_N5rL6aoNPfLt_qXpjmtqZxm2jbhVy3cj5yNM7vdNpq7ZRmY74BXmKR8GE8Hi5TvISYcX52_GkrG7dwHSUnjNja_Sj_x8YrBnUrPQ7Wrc6gkTICgFIaaTjQ6LcqiM0E5-kzO-K5tBzWX3YJUx_TiTgxeZ9FvRGFRx0mqfWJ1JCEctp84vzzy0w6FVOx-bh-c4BaKlKnrq6cBXNB_oo3Jk0K3h_nrC6GErzmkDIvcLq-6YH-ey5WmI0ZtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=fzPoz7vO_8UY-ElINJCktSne8YdqAy_hjxAsr7TxS5-qbIVUY1DzmD-Yu1lxzCRkukOpzJTzztuLOZnZ9ztoK1Uj4pS5nz2gUBcajndY0ewb9AHhyqr051rFVEqS7-7aJjfkFHBAo0UIyFhqyNk12H4-6jornpGUgcakDlnm_JkUn60-4RFJUbMRQ7QY2LQ_6shSMJlhepB6o0vgUGR-A2tuLz9hVfMemb0yL6TPJXy2Eu6LpYGN-BUlyO8ngXD7LvMlHVJHEznCGSQpRej71M3NGIi7ut3VbkpKm5LHvZjmfitz1PlxaOJVxzr_OmQB2XRMBPqYyS4KhleGWgEeRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=fzPoz7vO_8UY-ElINJCktSne8YdqAy_hjxAsr7TxS5-qbIVUY1DzmD-Yu1lxzCRkukOpzJTzztuLOZnZ9ztoK1Uj4pS5nz2gUBcajndY0ewb9AHhyqr051rFVEqS7-7aJjfkFHBAo0UIyFhqyNk12H4-6jornpGUgcakDlnm_JkUn60-4RFJUbMRQ7QY2LQ_6shSMJlhepB6o0vgUGR-A2tuLz9hVfMemb0yL6TPJXy2Eu6LpYGN-BUlyO8ngXD7LvMlHVJHEznCGSQpRej71M3NGIi7ut3VbkpKm5LHvZjmfitz1PlxaOJVxzr_OmQB2XRMBPqYyS4KhleGWgEeRoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jztr0NZ4lo1TEJdgobuTuLJU1Ym1gyZn0wsgZpXXz0IKUXHTacl2v9PrOOWylbFJYjPKbbum53qaqx0aNlNoM1N8MzMc0Qc8ScC0xWZfCnWHaoVlK07X7YG9BH8cLkjCRPPLmLD4ehgq_W4G7H9IJ_HEaTojTF43A6NbG3F4qNEPdI23rASkvDnZDJenr5Uf9Bo1HOrSdugGev5kUBhzoje71DmpcSG9-bKe2K2DLn52XoeyV1RND3yB8cOM8zkH66iyMR_BwgPWqT06R_t0UmfcJzYY1adCWm6Iin5dSXow111wOepwaP7p5WodXx56lyHXoGXIFgzoT71ugtbCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6CCljY2cLsQyA7yXqOUgQXZEKJYPG1wbPsA870f6_41K9dPqL4qJ-gPJzKvzBL12aH3SCz66rHTcuROkZ38aR2x9vichTDg5VWK2JXmTRqDyi_ind181q6aEfOovr_FLwcgcDCr45RMKKegeOZoHKd6l_gG37r1WfmtMHIOY_1JMJz4pq5yB2Sdlv0yq0GB4cHS2LucuUf4GdrVN0-QINXi9Kd7jun01_GoQAfd1-0u_aBR-G6__0B81N2SDzol6Yq3M29TbLppvtwDDuTHb2a6Dowec1LdAgl3HmjkPIZx7p8jysB4v4ABA4o1l1R0UBfKlPT29h121lLFeefzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=PcM37ZCj0jC0H9rRYSltcewU6iAZ5jBjkYc4tBvyF-CHbjUgWR8aKgPfXBgjLJAI9pQGVgerfJB4nXhPemDhGFYrqsOpP3ni1dR2q_ZQ-GRzK5HE3eY9aPFriBTLjiPgBndst6NAN0XSDT3SMgvKtSisiCbMAA7STJoo4-6_bVnvm-XiY6Tg5-fkBlFinXtx-CWJYgzVuitg-AZCQuzSTlh6w7kxKDKvbblgxlljtqKOFzF4f7CEdI45BtmrVBkdUCBfF4AN3F3g7um6jA9YWIVdtHjhy0zYzTyZIUxU9BDxossAHPEhhyBByqn5qt8PzSkWJn4AAQrDwAcFe1n8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=PcM37ZCj0jC0H9rRYSltcewU6iAZ5jBjkYc4tBvyF-CHbjUgWR8aKgPfXBgjLJAI9pQGVgerfJB4nXhPemDhGFYrqsOpP3ni1dR2q_ZQ-GRzK5HE3eY9aPFriBTLjiPgBndst6NAN0XSDT3SMgvKtSisiCbMAA7STJoo4-6_bVnvm-XiY6Tg5-fkBlFinXtx-CWJYgzVuitg-AZCQuzSTlh6w7kxKDKvbblgxlljtqKOFzF4f7CEdI45BtmrVBkdUCBfF4AN3F3g7um6jA9YWIVdtHjhy0zYzTyZIUxU9BDxossAHPEhhyBByqn5qt8PzSkWJn4AAQrDwAcFe1n8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=VUnbCWKlQh6ykGKZSP2ADrTc4E6FBBWriIWsD2lKh6U3YvuG-Qlj8GBzir2bzSEUlvg1s2bg2f1V8jGdk8RoJUMbbdYLctZxdfCRJlO9zuSHd86OSAN3yJtqdxqGrybLegfXRafIAqF1CAJ1VdVrmkBflj_7xoxhNnJSsP-biJJDVgorZhjp7MYawWAdqR4qg4jOmTSNwzRuQdGNpfQUVT3TEpajLJx3wAJeAn1XLmRBSy8ZXLhA-RvjGxwlRV18UeB6WgajOx9gAWQFCyfyeyuQlzLicAyUBRuXiv3wyhyk6BwBWt26PCEso6TaSK_SUgrjDsJRpqxjDhgKdPCd4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=VUnbCWKlQh6ykGKZSP2ADrTc4E6FBBWriIWsD2lKh6U3YvuG-Qlj8GBzir2bzSEUlvg1s2bg2f1V8jGdk8RoJUMbbdYLctZxdfCRJlO9zuSHd86OSAN3yJtqdxqGrybLegfXRafIAqF1CAJ1VdVrmkBflj_7xoxhNnJSsP-biJJDVgorZhjp7MYawWAdqR4qg4jOmTSNwzRuQdGNpfQUVT3TEpajLJx3wAJeAn1XLmRBSy8ZXLhA-RvjGxwlRV18UeB6WgajOx9gAWQFCyfyeyuQlzLicAyUBRuXiv3wyhyk6BwBWt26PCEso6TaSK_SUgrjDsJRpqxjDhgKdPCd4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlQ5YM_8rQ-qoDhsMeZ-8m-_b01Od-dWDy3OANoFAfyHaewg43u3KOPzKeLbrIwYNuxkkvjzWFVvGmV4BDQ-qlmDg7hYXQDsiYvZIeS9YUZSAP5vjYZ69M-Mw3RWPNDla6hsS_-yH3s-RfK23hS4iD6a_F8Z3WIOL_HYJfSSJW1bj2tVeiDUndb1taOOldVh91o94lt-MPw15_3Aeg7V9fwNWoBrsGyMbUTYaAY56KaDIdYfZs5aMc6aIe9OxX-t9nqOFMZmvyTzZoM_dpsy4cbXStW2TGKfM9oAjFh49097hA8f1m0qsyJaac9TDtdiEto535wuBIkbQqwrLZlKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=Q9WzPbIppBT-GiI6SYJL4k8dRqrpDMfPUGw0sNOGIPUQ75gVLP7qjuFi3pJHS8GUc7V_o2037LhDSXE3owRbp5aVD4wh6OFMaE8YKEWfPiE12U-uNpxEvbn5iLNacp6f9V8wBQefEbNYyLNPr7gQZdUwu5EbaE7bKXxPdcfF2neZgElSHIgSA-bNR_6yh5r3IltDLkdtgH_pjy2cFr6WjU3vwuBs-QQKjbGIsfydIA55_QOxDqyaoThuUBCe_I5seAYL3E1SSLwAGnLW5DhLJKBqRMK8UDpfZ2p03lOXlxaFEvZsZmiwEQUQi1h1g--UvOvQzbZdnvcD7LmOPXhaVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=Q9WzPbIppBT-GiI6SYJL4k8dRqrpDMfPUGw0sNOGIPUQ75gVLP7qjuFi3pJHS8GUc7V_o2037LhDSXE3owRbp5aVD4wh6OFMaE8YKEWfPiE12U-uNpxEvbn5iLNacp6f9V8wBQefEbNYyLNPr7gQZdUwu5EbaE7bKXxPdcfF2neZgElSHIgSA-bNR_6yh5r3IltDLkdtgH_pjy2cFr6WjU3vwuBs-QQKjbGIsfydIA55_QOxDqyaoThuUBCe_I5seAYL3E1SSLwAGnLW5DhLJKBqRMK8UDpfZ2p03lOXlxaFEvZsZmiwEQUQi1h1g--UvOvQzbZdnvcD7LmOPXhaVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsY1pjdRvb-pEmcrK1Eh_5QN1I-b4zvnU8AF92v7i1q48gEBLcQVTgcKWCqlhxMGVF-HCBKlXbzyNrlWrTHAV_L1MI6xWTe93Pf76YnJOnSlS8RA1oFdWN_FDX2E34jaWx6mBJG30DELW2LoaV8yZDSYclwjHvQlbXkWKgjNKl_3XBlmO7hvd8TOq1kTcTevhrYbyoQETQQq83xP5i80zghwmKdYjB32jf1hn1pq3jb63LxlkwUJ9TPeGYEoT7chN8fga2tbu5pYnx1L2HRcbJoayWHDNg-RXwdItcoEbTN0RUmR9B3_XgCdY5CSkf-VCUHbFRQhtaVwlUOiEwh9VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mz1HMKYu0W9uwCUiPfYiPZz-3vRqVXnQ93waAmcbtBOHZS-qjGlwZopzaW5L0iCcZSqYsTFTilWbmuawuYXrRffdh6bcd20RA6rjwzaFTTxW3LgzmQ7-ojXfGUus2J0mX9EBqAaqy64OiVMYQxGgP6oaxcOtmf66UFOYI_nTXOwXl4FwrGs-AsPeDba3mMVO42BWggVq0Wx6PmrbRtrRjRz9dqIGDT21j-zUFJqqSvQLx2embES733KKnypZkWIbbdFagt95SvI4CjJM0BBjh6dNWDgeezKIU45SK8Wv1aO01xFMNRScw3PavgqTSqUW08WnRjnpw21LMsoCEmAqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBs9yyw_DDKgqnIaBKuOOphwcY1q5HiDIKjhqCGzuE9KRw-CkXbIlfTbp9hxNI5SZGHuS53gbv1YiZFma-KucLDh6fCLLDH4dy3tj1bcdGHROjjt_zW4YnHoA58SdWBHwELiJ0TD8J-CzVU6JstavzxKVCrmkzBL0aisYfJJA8dm6oVH00-vDBJb33MEmTIaSdC60NmI78s1kcd96wCsQEj1wO11JOuAChQR90SOWRMyzGzvwMbdoOpbsmOKEAEo8pNZgQH7Dil0LERRudndfuwcXgO37bvcJSTOr8GbT-en1B8lsOkyzR29mDE0qmEYCZtiKfdQgG5vtlao3L-cHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVUuGSKFZrw4KHgyI1RN7gmb873eXLfcSsm7nNh-KwJxdJRQLWO5FBm9pE_moudPquAhNDP8yZvGLg5KAXwa0UoEQMz3bRfhTpPEA22Q6cemuvP93lVR73kDw_tDG1nJ_hdFa_2hca_Xt1F-fsEXymuieKThkCpcheCcIhRp9MCBD77O_eq58exxj4mSvS7kD8Tn6_s85xtUq9uoIbLkVaFkKEiZIahpfgaGM6SibUZIqvdfl-KLZ5__xiH_lTvwjza9HL3YUmx-EWG6QdQ1g1Wj3isc64-1CiUUwJbi5AAfx876pFn1Ij1mB5uTyvy1Qyng7roABwQxJRkH2wxIIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtC7J_tBvXTUcYX-qeDXFVJWoSyL0C8ly-MRta1Z1S3IrYwNy2wO1i-w9_l2ND_VbMwoxchOnwFsA69xcqOuYU-XCubC-E5VZmgrnt5yJwM0e_Xhb7c2TLCBf_nxw-7HFAAEbkSy1h8yZun4F4s21WAbaCcF2S5h-FO1q5t7HTjZDE8dg9nyZiTEwqGLSH0dzgwf87KA_1liHwfpFmCs0kR74yXYs4PMQU9eRnztleS4skelApv4Zge8KdJjCnaHb7ov2Z6sE8JXGZI4h3iOJvM0mHXOkPL2d53y-jGJp_Aa3rifGCtTmFWph7pXjLHgWZ7mFdCDh6tfgkTEjEXfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raA08f5y-eO9QnPApeBwy6X9U4eH1-b7dN6Wle8DtdIuBnbJjZwgYqJGxjbTjJV5n1wRRoUzdQUV6OacKYItgwO3lIQXlCoRgFnSBf8ahCyMTea5hsekJtbkJpPfmQ_mZgHISIllQC2SK2r7ZTN0COMLIZgfvzrKf40P6arJYsm7Akhf7anzUlmF1p8vZMwwpt99LPlDeKiJJr7HFbVlEeDRAPjOUxb4WUOS3F1TN8NcuK6e587OfmVZQr1Eu-61kD4_5d1u6LBADIewVyczV3jbyW40N52VCpOviyUWUFYbZpwW9HyIdwmpQVm2Ahar-Eu4MwP5dGiQNtBAHv3JIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBdK1T85LFnnN2ZtcwB8nWEYGbjxd2eUS0m8YlmkwhQcABJZQG3ImIOojIt6Ha2SJ2lu2DfjN2GgpY1NXKKIDGyFLcvPemHpL9xuKztmZARToqguRKsgE4QritpHIhiorZ2uNtPlbSsPbwVdhBhkdt_1yv7TSZlb6j2vzZgL_dys5mFd9Q7N1VYHT5Ed8ZMpgQSffxeQN3J6VhuHOClAjB-2X_90pcjFAyoU6lU9vQT2wEElR3jQGaMzZSg5nd2HvOgyC63Ly6hhwv_-URBAXBEdkOuCwZP9mV2bUThiU6wJnaIdAPs8lZ4HN2AnEaw1hsLdnXYKun7iQq_q5-H2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrUXg5DIqOD-cosGqHFfEyaxppfYm9TPmR4HYoHTTFHMZZMAoSb4L_agovbgZiyon1B1nWO4LCUkrwuKMm8RnMcFDkk6c_85rzIEwpUnm_cNQUzIGGNCSEsn0QMjFHKn86Pfxu1SKRpu3DilPUxT1zsZ7Qvo1mToXU1SzGCpkn80aBD_udGK6XNQ-a-24WmQi2xYC0Z4x5-jsf-7QuP25HAwI89jo1f3E1fDub9eDx2nYZqFUt-u99dZVTX0y9rPEh4D2TevQaDMw1w7oJouBFtcEyNP0iIlidHLEoBkz-yae7YIQjkAQtYzikZY9sY-2IklfgwGpu9C90pQygIVpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=tobcaE2jAG0t2q86mZb3zwgOfdjonDIJN8pK-NyID3GNUNhobnARetQRllqzgVkoXOPUrFboCXUZWyCShJJhk0X4MFFTDHuXQMczGcQ6Gg40qk4BLgl8ZHkXYB9BPQc5TJmxljlADgrs5ePz8mCR4dBOddVIebQipH3YgikQgRJftcz6MghxQemg-PJ_lhmx5j-tdpgFRPpQW4fh843E6TE6C54JpQluvtuO8BoDq-E5hnhUL3LK9lLiZ15Wl9RprtYWsqDAZeOH9hjs4XyLJHaCSW8QqyCFsNfcySlu-Nwz1YRPw55qT1LLMlpxR0493OFG9saT_GiyX-W3rCzcjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=tobcaE2jAG0t2q86mZb3zwgOfdjonDIJN8pK-NyID3GNUNhobnARetQRllqzgVkoXOPUrFboCXUZWyCShJJhk0X4MFFTDHuXQMczGcQ6Gg40qk4BLgl8ZHkXYB9BPQc5TJmxljlADgrs5ePz8mCR4dBOddVIebQipH3YgikQgRJftcz6MghxQemg-PJ_lhmx5j-tdpgFRPpQW4fh843E6TE6C54JpQluvtuO8BoDq-E5hnhUL3LK9lLiZ15Wl9RprtYWsqDAZeOH9hjs4XyLJHaCSW8QqyCFsNfcySlu-Nwz1YRPw55qT1LLMlpxR0493OFG9saT_GiyX-W3rCzcjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=f2JMJYIl22eVxdedYHwY1ajSvVA2OpApd57YMWa8C6Vw-o4jk6OeyNn1CSWmi7A7FmctyY-G7w_JUXJH3qghLiyyIvRAv-MEhvE8u000vOwln13NLqil7lvdsc6tYft9BJDuewKT6iW0rhmHxE98QfL9dnugFfILYIEpA9Ju9Nk5_be4-YVsF1fwYaO0BK9C3nJRtecxXeme4PK703FNGOjYUEbKuOdeLqEnR6zc-zC7sXxo5zzewdU1Q4zjQH_Ws4--FJ-QAJzSKCS7B7EKX1ujwj_m02PGDJYmtkh18pjyw00s4HEarDD3ksaI5YjCFa6RW-HEFv_Bg5nZ2ZUpaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=f2JMJYIl22eVxdedYHwY1ajSvVA2OpApd57YMWa8C6Vw-o4jk6OeyNn1CSWmi7A7FmctyY-G7w_JUXJH3qghLiyyIvRAv-MEhvE8u000vOwln13NLqil7lvdsc6tYft9BJDuewKT6iW0rhmHxE98QfL9dnugFfILYIEpA9Ju9Nk5_be4-YVsF1fwYaO0BK9C3nJRtecxXeme4PK703FNGOjYUEbKuOdeLqEnR6zc-zC7sXxo5zzewdU1Q4zjQH_Ws4--FJ-QAJzSKCS7B7EKX1ujwj_m02PGDJYmtkh18pjyw00s4HEarDD3ksaI5YjCFa6RW-HEFv_Bg5nZ2ZUpaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5pGdmOyxcZkYKOz1RbG2EoW-ouCKOumYS1PRNSb9TlU8SWk_9Zf5St9d8izT7_Bf1sUeokDRrSOHir8-hb8Z6b7Z_3ZRdc0A_1UAppwhL5oxg9J5ENHO2ABz2v_KkmWd5DCzBS36EtbiRHMl-RKih-hRasZ8YHDbfxNvM6p7ADn6YQtmzEtPSQLTHj0xuPbs33HN4nBHXIf2Lp8CFt3tnCRD5hWVljCI-HHtEXaeGVWl7e8guCDH1ncWvGYGCR7vZsMFsJVBm8veatj5jYy0FUB6XHlsdQ525kY1QZRXRaoOwoyHFJh7QM6sRpvWoAqYQCJnm89cbVXmoa1Tj4Kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZURZJaQDThvYzNxHtvMDtyinhkrwUzyp0nBROgi8QHuOCXKk4Xc2uAkwPtfm_Ebx4hfQZMEy4kc7Y1cZIXqQRJfwbwEnXJ85hYreVFk1UailhuT3my5P-c7rMOh7cdn16qNIpF0GNILiGC2HlT97HCices-LUp8qG8GjHJzxFgz_VJA6C72o0RfdQMIv8RdlFWKe8Uvo9kS2mykDAWSHpXSBqLziFXFVECcE2LHZSFHd9gRLF7ibXlXCuRVOHLAIH-jFVf63dmU2FphwoB87uWZJPSA3jeikFipuch3ZBpN-6eproyqUCayLSvH3yiy3wGR8oR2PMzOPVYZcAhSpFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIiWofS8oyBfiqnklxK7T_mdXOIAObAcyklDUIFLRb9J2Um8cn3Nr8V70gh7ynxaT4kGTQsRiOiHidHhVynUAT3qySZUsSTjXpg4mF2Md9va4qW794qzniIwa9-VbsR2GHAsA-En0G99wQL0B-ZClw1JySK5bbP04wC9SfUAbp6kBU72KTBT9Mn0_aZsD0z_Hu6-_P-g9Gz82cOPY7J20txrfo2uI1r-kXTleRS0Oq0wD4bQVXNs2kprvmoj0ATAGeObWgv4bGdFlo76TLrSA1UFeJBZlMgb7uIHfo7yvWREgq70zGw7IwI2jcWyUWbYt7nc0a-SeVPT05p9Oq87zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YljoZHnPIu_wudD_GKmN6Pi9LWB6Lsb1mjJ05YEAIyzS0G2CqZ8zK9p0eVZLrhRIgjVvGoAuO2HGfDN20Ze1Tlddla0O88ZqSgw5SioeEYVFmn088SkPRxtcnxSyog0htIlHmhjXw5kFYp-AG-GYjmQ0ioAsWYJcKibu6Vwqpg-iYzRu39EsXJjboGJqHX6_uvoJ-1Rfz0y12hueJ-ZFmC1Mk1H0hKyqEArhE3_Jp2lKo_1XmFmM0iwt21nszYeI3tOPD4QDQ2lIZrAkuKaINUck6LNkTi7sz0-cuWg-aANjSwBcu67VVPLLWjbYkwavpbZzq45EaCguLDfxx8m-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLN1lDaUpUEbafxm6q30zwUJyjPSTIe-n8P9BquikipvTcse6K1eWoVBt1wLadmtrLB88THXjZ25CuBI0O2_hgw3WzXpaWy98wcZsGuxN9d6q0dW_uoQWkiCHhjRkVk9AVrps6f6_0WqxrG9JVubGntXE8GsFEDn_fosV1ZeVXXqR8C9nB7DF4mWor58X4BmCUFwlZIkH6y9B0w4OLANXJONCfD8_Lt6am7dkHoBQiLU7K7RddjN7_2ijRsdHCD32biICBX6vwu2CMRte3g9H8kcZ-4h2T6IDrXfq17ZMS4TvQqnvMiYqgjF98MFkYxd2PfbFvsRX0Q3Yskd_pHnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivl5FQ7E0kdYFMEqRet4KDdpearZ33oleqxIxRfuM_aTd0ybVfxCsdbkBn_bu8M_NZf7GqlXz7E1dbn1v0edKxmBh2WpbGMI4AnxFnCLYzIpyuHGxQOMVSzqPWEBX-BVi5eaSTpPuw-wNn0yRxZN_sLN18UQwHiYAO3YNLFJcwf7fZQHg9zRoIcyK2R68_Ep1CN552SADRcxDZg1YLba9FKrcabKoMR_OYvURg-bAghIXf8vOVZw4yTWov8Z5rDv0uCJDC1DynUoZrBb8_0cbyTMWuFUvG9Nutq6XS61I-bbbtbZTrnyKDS-9015aPt8Dk5-luaYKmxgANP8y7Mleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9DmjNqcfABpS2jxLulzuyITAHcv82YcE9N9QLT7ONBskTA3MLQ5Qt9TiFfW81oDU5S_htJ-PYzE-B7ZfeZFwcFk3-feDcmew_N8PfE6uhQlOncJrjMDtOJ6yzsvA7ruO6_mzt2-tvUyfY3GCGVqol9WokZb_uGOrTYWse3_AO6RTFS8J7Jg2AqTAAnSE0iBBffPb4kCHDx52cHuNNMAtLFRWcE90DxpCpxc08NdnM2q1lULoadxJdyf5rgzNoUhFetOy6nz3iP1JLORiE5-8N7txO5OEej_rKrZfvjVSmnl8z8YdfwLMxQBUUo5Aw2YZOtNgdaEq6BXRgh3VTSaQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yr8VU-FViujigdR1C9a2VjL7S32oLZy4iK6VmiawCJ67fPdtHeZDZdsEnzZWYdLt9znsdTGEWtue4ixKTFZtgJUG7d2oI4My6TxuyX9rH8SMkn9NpJkU_k06qQCdku-JxdwmkySKX91cGx0hTohjtiSSZSPxyj7KSZfoS0uY3uGsNibLb22OXzOX7-C4NEKQjguWjy1jei9f_y_NJcZ2viLPgLCAfGVkZO590eu4XaIncFAE5lN2MZhWQmq4PXDLLaxAXCv2DqDhrBC4Ft7h1jRb5MfUIqKl2P7pHXow39TKIrPEMkpt776uiv9kj2Dxd3sVjOobf_iMZcCD61tz1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=qqh3LTd7UDpeKR6hgYsGtMcNy84IqArCLt4J4vx5_sqKcEGqBh1zqBCJl_DgE3T5nzqBVTEKbhTj0TJVjNQnChC8S-kaxcjS3M9I5EbTnkPZc7-ZzQzjB8LCZpEK1SBnpgxIbZjmbkIRaA4eJbO55PoYEZP5F8qALxGsLJ4v_-cV-m8yZZkmTqC-p3BKTYgBbvywK5G6ZWlQZNMoiwEyBS1L-eSiMsLzkIqV9o2SL8gvUW1OxRH4-JHDj9WN-cysnZx2vXwLzGXzq-9psAOb-GKTZy-nDVoaEj9dy-zvG8ViVl_v3fiozR_2Ql1RX5xaohbrFqr2S8ymFydaSYWK6pGktCyN4poJxoi01Se6jCFmFZJmjc9g1OU74EJXjbBQF7iuhCNblUS4Immo_JVAI33Pzfbqa89vo4HsrvNq7YS9_GrNDb8uFcbitnNHEOCLJW92e5U2h2w-F-gICUYoxr4tNLY2hA5YmiLu1PyUuMOYSl0I3NR4q-9n8_DO7xlCFTSd5vUTMoLX1BurUu_E9oiwkyBL9oDB9pBCxfFsidv4MHEysrjqapDGDtzvJyIUb4Ss09LWPNW2Z5Gb3KO5Aa_aH9RoI43zr_-lPyXDj1PGyOIb43AldEUx-MmDHOyKcS4xUvvxrQqEwutGJnhCfVDXU0FxUheOe8OzuYTe3PY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=qqh3LTd7UDpeKR6hgYsGtMcNy84IqArCLt4J4vx5_sqKcEGqBh1zqBCJl_DgE3T5nzqBVTEKbhTj0TJVjNQnChC8S-kaxcjS3M9I5EbTnkPZc7-ZzQzjB8LCZpEK1SBnpgxIbZjmbkIRaA4eJbO55PoYEZP5F8qALxGsLJ4v_-cV-m8yZZkmTqC-p3BKTYgBbvywK5G6ZWlQZNMoiwEyBS1L-eSiMsLzkIqV9o2SL8gvUW1OxRH4-JHDj9WN-cysnZx2vXwLzGXzq-9psAOb-GKTZy-nDVoaEj9dy-zvG8ViVl_v3fiozR_2Ql1RX5xaohbrFqr2S8ymFydaSYWK6pGktCyN4poJxoi01Se6jCFmFZJmjc9g1OU74EJXjbBQF7iuhCNblUS4Immo_JVAI33Pzfbqa89vo4HsrvNq7YS9_GrNDb8uFcbitnNHEOCLJW92e5U2h2w-F-gICUYoxr4tNLY2hA5YmiLu1PyUuMOYSl0I3NR4q-9n8_DO7xlCFTSd5vUTMoLX1BurUu_E9oiwkyBL9oDB9pBCxfFsidv4MHEysrjqapDGDtzvJyIUb4Ss09LWPNW2Z5Gb3KO5Aa_aH9RoI43zr_-lPyXDj1PGyOIb43AldEUx-MmDHOyKcS4xUvvxrQqEwutGJnhCfVDXU0FxUheOe8OzuYTe3PY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=EzGZuKQJwj_H0t1PUOaSA_wxFUcm6N4qfrp69MeIRXiGq4oXSOoX7Vq_QzLMOF1DrNKj3YzaH28B-sMTB-QMBcFs-81hXbzQYeR4triuEfAh4XS7dGsbTob4a9xqP003AQZ4fUCfnSpDRDskffm2qjxeiKlJ48kB8KW4uXG1ITNCGdYKuIwO4I71tF2Q2H13Q6Jp3sWQA0ZfVul9j1yN63d20m1qtK9bcrTIfYCl-Zlra60dcoc3MHPInQl9MoJGgywghuDDOuQtSqa8IChyjKQhRQcwO9P1l-f98piLqWkJtquByiiRGukOTILmUhK-tju7MJHZSzgqnAyOqVTzlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=EzGZuKQJwj_H0t1PUOaSA_wxFUcm6N4qfrp69MeIRXiGq4oXSOoX7Vq_QzLMOF1DrNKj3YzaH28B-sMTB-QMBcFs-81hXbzQYeR4triuEfAh4XS7dGsbTob4a9xqP003AQZ4fUCfnSpDRDskffm2qjxeiKlJ48kB8KW4uXG1ITNCGdYKuIwO4I71tF2Q2H13Q6Jp3sWQA0ZfVul9j1yN63d20m1qtK9bcrTIfYCl-Zlra60dcoc3MHPInQl9MoJGgywghuDDOuQtSqa8IChyjKQhRQcwO9P1l-f98piLqWkJtquByiiRGukOTILmUhK-tju7MJHZSzgqnAyOqVTzlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=sV3AHhuOmLLbkejuffI6-aax_bcAqfqoTkRyyzRk9w11aceEEo_d4wuMGvj2g5dPTcdx4KTR2Y1SXWJpLBfWbc3PdPJJ3tZiDpiQ0tU8Q3HwG8EDsoGitV_wuCcyus9iqd2uo6_d6JOuKSSYVrQEV7NwJXOxORFHOU4LjFTPJ-yGs3JkFAl1gQOAFCWWVmslMvnr7NkN3yoaedqUeKB_ghJlYq6xT0X0TRzvermiT17dsuZL_97x0jPLcg0tZeGwwSXr-utkfcvlvjVeSeTY_aIw68Sq6-CiXjaQmfK67UyQXjbtRPp2FOkJQDNVSOdqBGJ6790ebmTGSfcB7-s_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=sV3AHhuOmLLbkejuffI6-aax_bcAqfqoTkRyyzRk9w11aceEEo_d4wuMGvj2g5dPTcdx4KTR2Y1SXWJpLBfWbc3PdPJJ3tZiDpiQ0tU8Q3HwG8EDsoGitV_wuCcyus9iqd2uo6_d6JOuKSSYVrQEV7NwJXOxORFHOU4LjFTPJ-yGs3JkFAl1gQOAFCWWVmslMvnr7NkN3yoaedqUeKB_ghJlYq6xT0X0TRzvermiT17dsuZL_97x0jPLcg0tZeGwwSXr-utkfcvlvjVeSeTY_aIw68Sq6-CiXjaQmfK67UyQXjbtRPp2FOkJQDNVSOdqBGJ6790ebmTGSfcB7-s_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4ds0qAN-okT1AVIzbmG80TxVZM_ugki6w9b8TEomtHmfozKsOETxvhDfe5V1FzusxpONUEqR2m-bKVv7DZMPAZ4xX0eAVWUH2ziXImYSy8AP_amr_y0CblghpZNMwH6C8ELRj0SeiqGdMBiCqqGe-2RQdKePB4whWhCY-PIFzeGvkKYPKG2FFBUBnrEAk76QYjdn9bEbhm3xds1ztA2VlOz25bESjiAu80kuvKTtlblpFMQEF4k88xVs26LNRmhvZcE_EU6qcyPJLT4m65QWOn16amjjuH6UwlVhf8eF5khPFprdV2s3GKlNkkqo2fcWBTgSaP0uzOCiTvQci42CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsdeR5eCz6hJGl36UJs87r4ZoI6WyRnDsGqg9EsZ1RBecLi6cKHy0NyNxn1IPLTEO2Nsb6JOjMHcIxzrT4hfDx51C1zJ3-ia2K9pL9ZtjviPiW6HgrjufIR-i_zFZhx3b83x0IkDrn-i4BEx0SoQTK5zrOc2qvG2X2nfiwGA34xicSOIh5n-ayeUqyn6W5BtlTA1cEra3q9GH2laZvQGQx4klI_LXxgjPObXavaVM5WxZhHnOGKNM5a3K-lXhmk0ikRFd-ZEsUJoA076NJ_aR06twLaUZfXkpYIAGts6LvUVrKgI-PIAcF20NhNHVykyK5T5tvvSF-9FOuPGfkdixw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT40zhSt3uSDzlu909Ho-fAsMNQxPsLeGhFu436yIqeiJlCjXL0O481a0zwsQ9FoPoSffTt70zJuCczp2EKQxlzclXZQaUBgowcO_Qu42lSI3EUQ3aJtVzWLCVmU1CRn6fwo9eUZwEPiwb9K7iifQl-E6fsHL4Ua_CH_2a25q9yLkUeGyGOXLwPRJZvOyqaQ-TcyXwlASmYisUefN-PIAUMA2A8RcCVHYSNCIqveYreHCDmgb2ZmrDfJE1TbcVKh_Iyeg6Elj6kEPpw1V1FTMYY2a2Mo5e1JaQ2YgzTIMgRiwhRVPsg483Rm5njVRYLx3kXQHexxnSfhHQKg1Sj9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGhkNJS72mHaxGN0uOYBmRBX4ad4tDBJydsdBje9-8pU6LyNrn2cc-MOEFbdlTvqE0WqQfs5pZ6qn2G6Ip-ckz1Pw9DW5j-czDD7JWNNBL4lFr1NBUdUzDUQ07LyVrYiNVds88sq8K7vOnolY7oyxdgiBGGydXgthwXRJO3lzwBUJLCOD3Z056d4TT6eE70oLfx_G2yrQ4BwVxb9mW5GkenaMCTCmypYc8KolZXW2ru996ER2GBGx6-U4r3avx2C3iLVQImqCCcSoPO7VmnAPi6z5xHfirWQqSgvqay3QsACaGaemAGxKvpSy8Nw3IKUUwBoyxTHOHnm6HUsjZTz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔻
الکس فرگوسن: "آیا منچسترسیتی از منچستریونایتد پیشی خواهد گرفت؟ در طول عمر من، این اتفاق هرگز نخواهد افتاد."
🔵
🔺
منچسترسیتی از زمان بازنشستگی او در سال 2013، در هر فصل، جایگاه بهتری نسبت به منچستریونایتد کسب کرده است
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed8Iv-qHXfwbu6BL4Yo5CnxK2q-9JlGBvol-aOiyqiDpmt6ZZDm_c96jco0ounyreeStr2_UR3YVf93Y0KNJzVLVenAbNbJTH2zdUcujwMwRvmgEKjmb258dAUT3bstnzYgJCceQ2ZQjqsz1jxo6abIAYj9Wh4WoHSLoBM0ArkIF1ZTDIRIFE_hhR6zULb7PT_naDw8iOXS_qGSXxBSkG1KcFaa9gsmX8ik7JxLLaDUhLigwgAanep83sGJz8KB0tGQJ0fTXWvoPF7HX_zOi0jSjNq6F1DLO-Gtr0LZdqPYfPjNHGODLtKJ0zJi1UwgKacXaeR1bdYnS0VoejCVSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3Nd3fY_Vy6oHM0d9ZaQdcta3fgr3JC3u0hks2DKUKArAtL4_JrstkhIxqdHd-b1Q3WmVqtZiK8Z63txeGamx2bM4y5Nx2D3UlK033S0ibdP-uuTppv3YsEJpBU9j_PufiuUuj0Pbl2J5jBD9I_kxJQ5oFtik-4DSnLDNDKuaO_nHuJYKeN1KpRHc5WQQCRnxhBuoF96rsSGw4fT4oLrF9gd2OUeNr2o3Fd7seExxh45gUjzrwtRK1hS8AHc6NOxhmXxnQXvc0sd8AymQOfMu2PMfIFhlGMGGYoRMnUnl2v3OTlmTBNZNyYxh6Om4K78cwrNPnXvWT3pFI6gwN-XBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbY__dlV_ale_8v9Nu4Oy_awcUjfyDgEOsTdUqKWyBpjv4clyM7i5AC2W0j7wIcs954lqOlghk9ObU01Xp08jezLyAotRO91V5Yv8z_iBkDXBMV5ez3IgPa8JNqSuzLSU5wx-YSc2FHNJd7dxz-ZY104GsGWSu41lUhyCPGOs4nF_3znxf59lDZWZ7hyXLBLevo9KrIKO_2IQZQSTRB01C4q-P34wfhIvz8hk8mfDnC5SIhEure2eUUV0AwVLEdOfc2jgufyjxfyII9N80wKT7RmOpWR7xwTjuH9UYqYC9iyuv7IFn5y7ARRJgYNouy-Ns4Yn5DoVe5ku2Oh6Vj27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6U6-mohnLiXF4OaVFx50BxM5xpivHvvgzCEF1UHStERbfU1elWPVJ17CHCdqughhi5rM7qmprwwdPqtEHj9YUtA5kswtCYR-L03Eafj1QqJYpIfF8QnuosqTDYhqcHZ6Wchx9HPsAmVaVkF8JS9j1nmpTCd4pJhFZ67znMI35bKfzQHC9_4KYmpIo1yl8HV2lfvhiWSQzmUIq1WUkE1iRl-WRU5Wugcgi6aAaSzJ7LqxGXnZ_WAssM1sLfGQ1pVp7p4nHYt_mlehgteWyCFmFPLWxm8_2VAowyWGfTyZByugHvX_1v8e4O2_V75wVJoJ97TG2OLVAmdQp1B8bUlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101722">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=NEB3P59hjhHLZEcnOuT-w0THNehb3NcMVRzheaoM5wPLJRKSmHmb4HBXQVtniksocN5jYJh6OoluLaBqk2VGryq3JQAd5h3889jFJjtBu2J1D2o_pkYbwZQNG-028-qB_X2-egmzAmVe7iMvR1mct4LmF1pX2MkyRhAw45xoM6FUggn2NpXSo4u20PdBeKNnN6GLIN5_cvhyR9Y1jaResgTkCBlh-1-lAx5BZ-zoLJvPnzBf11jbyYLGjnPxJjKlDCAQhlaR2mkjUdV0R8b50xvnYGGgeZt3EkWgausN6csKwR-JWvrDBS4n42gxnuMmGNlX6cKlcxhOFz_vqsbGwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=NEB3P59hjhHLZEcnOuT-w0THNehb3NcMVRzheaoM5wPLJRKSmHmb4HBXQVtniksocN5jYJh6OoluLaBqk2VGryq3JQAd5h3889jFJjtBu2J1D2o_pkYbwZQNG-028-qB_X2-egmzAmVe7iMvR1mct4LmF1pX2MkyRhAw45xoM6FUggn2NpXSo4u20PdBeKNnN6GLIN5_cvhyR9Y1jaResgTkCBlh-1-lAx5BZ-zoLJvPnzBf11jbyYLGjnPxJjKlDCAQhlaR2mkjUdV0R8b50xvnYGGgeZt3EkWgausN6csKwR-JWvrDBS4n42gxnuMmGNlX6cKlcxhOFz_vqsbGwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اهواز از این زاویه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101722" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101721">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=QZ40p7dSFNycbXuGeq5-4-AV-Pm7KjAP1SKSv08azyR5lU_SDLfoOsV11Kr31kBeFEFEd4UB2SntBd3c8QI5VUVyxDjLXVIlNoS6SWQPmcCJrXV-xf0eQoBPOMLTvoNPC00CDil1BIELpNBFGfvDD95VJXzHDc3gPmhVgufwypW1N5h9CGPSkXMv9_U1mLNNTRV20SO2ZN0Uzf1JzsYntap5eDhV_PzNj_2FtDl4H4yNuxSPi559g3aT-AjWFUAapfqre88t5ivH_WtzfbhMm37iamzi7NS0TIs_0Ogy9G7q6OG6-xWDc8eDu30X41iqhMIXU6aLewkehTY90XafS2RfounHCPyOunyoqiJyFhk01VIOgj52UWWpG9TKDfwn_TMILXWovWxmg-5zUJXhUPrm71qa1XduZDaKUcaWI3mwMXPAtwkshsyOHQnYPJUinVjPBKdM2BbL6WQ-W4jKTXd4Rv1o1b46XY65GMPVAzAiDZdXz_vz1hKZvcitWg30MCJsTVcgsyR6lFywmOyKnJ8390iDExdHp5fG9SU25iCdOGfkDMqcKlZeFcVCX8_DOhe_rTiHA2OCZpDUpweOiL7kOjwtEs0gujhLDAYeTfS2EvVV2rN7hPsfNyZla-489bPf2q-cxDVM6xpu5RFLk4h1xICf4OUuwmOh1BZAxRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=QZ40p7dSFNycbXuGeq5-4-AV-Pm7KjAP1SKSv08azyR5lU_SDLfoOsV11Kr31kBeFEFEd4UB2SntBd3c8QI5VUVyxDjLXVIlNoS6SWQPmcCJrXV-xf0eQoBPOMLTvoNPC00CDil1BIELpNBFGfvDD95VJXzHDc3gPmhVgufwypW1N5h9CGPSkXMv9_U1mLNNTRV20SO2ZN0Uzf1JzsYntap5eDhV_PzNj_2FtDl4H4yNuxSPi559g3aT-AjWFUAapfqre88t5ivH_WtzfbhMm37iamzi7NS0TIs_0Ogy9G7q6OG6-xWDc8eDu30X41iqhMIXU6aLewkehTY90XafS2RfounHCPyOunyoqiJyFhk01VIOgj52UWWpG9TKDfwn_TMILXWovWxmg-5zUJXhUPrm71qa1XduZDaKUcaWI3mwMXPAtwkshsyOHQnYPJUinVjPBKdM2BbL6WQ-W4jKTXd4Rv1o1b46XY65GMPVAzAiDZdXz_vz1hKZvcitWg30MCJsTVcgsyR6lFywmOyKnJ8390iDExdHp5fG9SU25iCdOGfkDMqcKlZeFcVCX8_DOhe_rTiHA2OCZpDUpweOiL7kOjwtEs0gujhLDAYeTfS2EvVV2rN7hPsfNyZla-489bPf2q-cxDVM6xpu5RFLk4h1xICf4OUuwmOh1BZAxRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو جدید از حملات سنگین به اهواز
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101721" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101720">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=h4pm4DGMdC-oLJlQhPMo332XCsQQsePw5n6cH1r1v56TLTCC-mnPi4t7Sg-NkL1YdwWhG51Gy4RFIqSGBnvhjEmyB2jlM4tE0-jjKvPnRVjn0rD9Y36OZsZJ-4L6GzmnBlQmpjrEKWHkvEZ-_Y3_WIdyFCBXfy-O8vA3ptbIP1ANI3TM8ZNV06CLoxHWLk3BczApXZ8zmgm28J6nmc5C33cd0ZdnFmg0xY47HW-t8tevQKsIKLpzg3sn3PNKG3EsBEmwgaEVLS588hXQz_998wNRHkqQdJQuCp6eOiy8zf2fm-9aKdGiO9RtdRniNjxlvVgNRwErNFrxT9E_sjfDRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=h4pm4DGMdC-oLJlQhPMo332XCsQQsePw5n6cH1r1v56TLTCC-mnPi4t7Sg-NkL1YdwWhG51Gy4RFIqSGBnvhjEmyB2jlM4tE0-jjKvPnRVjn0rD9Y36OZsZJ-4L6GzmnBlQmpjrEKWHkvEZ-_Y3_WIdyFCBXfy-O8vA3ptbIP1ANI3TM8ZNV06CLoxHWLk3BczApXZ8zmgm28J6nmc5C33cd0ZdnFmg0xY47HW-t8tevQKsIKLpzg3sn3PNKG3EsBEmwgaEVLS588hXQz_998wNRHkqQdJQuCp6eOiy8zf2fm-9aKdGiO9RtdRniNjxlvVgNRwErNFrxT9E_sjfDRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پشماممممم صدای انفجار اهواز بشنویدددد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101720" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101719">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101719" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101718">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=aeNDp1lhzgXPXTYHfsomqo24bI41WzqO58qdHny4_IXr3eIeIFFAGCZFdy2atxpWvXc1g63TV7y4AyihMZUPynah3ZXMo-NL6m4BjdXfjWHe6PinexZ5bYKsUI4unYYUbEkcM3ntatVWmrwWhLkppJQ3xJjpzk0P7bg3TgqZfQY7VFYT0U6oM6BTu_lpdpz6KIh7nV2HdVQxHVJVSyd2-yYtrYeEJEJpM0zqtykx7AReqJ97htOvCPe_whRFRg-Qz5g2UM7zbRCHZGwcr2UHb0iXx6Bns-EjMaXW01VZ7M6rYirtWBCU9vSAmSdrcYoypRM_NOngFhnbZJUSN1wizg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=aeNDp1lhzgXPXTYHfsomqo24bI41WzqO58qdHny4_IXr3eIeIFFAGCZFdy2atxpWvXc1g63TV7y4AyihMZUPynah3ZXMo-NL6m4BjdXfjWHe6PinexZ5bYKsUI4unYYUbEkcM3ntatVWmrwWhLkppJQ3xJjpzk0P7bg3TgqZfQY7VFYT0U6oM6BTu_lpdpz6KIh7nV2HdVQxHVJVSyd2-yYtrYeEJEJpM0zqtykx7AReqJ97htOvCPe_whRFRg-Qz5g2UM7zbRCHZGwcr2UHb0iXx6Bns-EjMaXW01VZ7M6rYirtWBCU9vSAmSdrcYoypRM_NOngFhnbZJUSN1wizg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101718" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101717">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onMwvsn7fzQ8BuddHgOIkFa7MFPDmc-kuGawoN2F5FzyxKjPSAb61kKk-Q9f8TlbdQ-LGL2jcPzEQGtEYvTwCAjL55kUY5mEZ6_tQNHada2KjF4nnWF_U3oQES8flawc8kpS57dfKq59qoZPswAzIAuvbz4XzvmxDZkUANXY5ORgI7qpcFfl7KXRjSozAmWYjH53GQGiJ1LJrrZfN7FQUn86Y0lVOP8bxFGkr11ebPMyITnZnohoT9BjpsDyDioD88OrxvesTeOpBNzGlx7mv8o9lpNNvtjn9tH4_fghObpGqqot1ELRj249pm1NL0mmavXBcZ6deW0TYcmujB1gXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✅
کریم‌آدیمی ستاره بارسلونا و خانواده‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101717" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101716">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=Iwer86sZpxTbG5GF2Sg5XDa-_UpEhYixRkoqje37c_zTGanhySwcuVxAAEqQBtHiLN6oOk8DDcSM2Xfrs-0caNLnU7UEdqWEOBTdDIONKF-jZwkEFhE4Nc6HzoYamyCj4wIjpCXx6hbHovXnRnKJnJ_wW2fWjGCvWPopvnsuHrI0guttgg7oYcns9fQxoC5FWTW2F7Vkacw1MTOnW1hjpe-Dz3oG9PA31quzysB_OlBLVr6Lz5XQmQKau-uVMnR7Cwdwh1Pz_Ix0hpmiPhkJU0pxcCIlcRL4DnP9us8BwYYOflA6jOZRU9HQ2GeE9x0WWSujjPnbabeN25IYp5ETQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=Iwer86sZpxTbG5GF2Sg5XDa-_UpEhYixRkoqje37c_zTGanhySwcuVxAAEqQBtHiLN6oOk8DDcSM2Xfrs-0caNLnU7UEdqWEOBTdDIONKF-jZwkEFhE4Nc6HzoYamyCj4wIjpCXx6hbHovXnRnKJnJ_wW2fWjGCvWPopvnsuHrI0guttgg7oYcns9fQxoC5FWTW2F7Vkacw1MTOnW1hjpe-Dz3oG9PA31quzysB_OlBLVr6Lz5XQmQKau-uVMnR7Cwdwh1Pz_Ix0hpmiPhkJU0pxcCIlcRL4DnP9us8BwYYOflA6jOZRU9HQ2GeE9x0WWSujjPnbabeN25IYp5ETQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت تلخ کودکان در‌ جنوب کشور‌ بدلیل قطعی مکرر و گسترده برق...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101716" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101715">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9HKKvMWxactJYqFRHTFJChIP3BdGj32GJx_1qyetsq4aandBm7IBi4GKn45n5azIYQFvTtCgjDMix91yKZJH_0ZTE_vIHADeWzwa5FDu5iGKg8qGxKo0eEAdbXJIrv0wBtDp3ggSaV2GzFVvmJUrbuWR5hoo6GNdqhsTfbXZyYZY5LdSZtLSMyMkDaopKXxWpPzLNpwuKIL6p7LgVORdbS9IIoRILPSXM1FfoPleWBpsXg1Qfnt95KIWMGiLALw-1RlaZaqxfArj_9dp8yYDski2GbJkRwtHb_hXBNS0BdZ-tbLL_RZd2SUrD-gK1mfgwe1nrrVbmVhGhG8v02CTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
اوتامندی رسما از مسابقات ملی برای آرژانتین خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101715" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101714">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jms10k81fktGh5LIfEHjEPFPO4wSOmI012UeF_UO4FIja12P-p52_Jztn7mnRjmJJ8BTeYciohaeSqx_2dWq-zvnJD7wVsCIFEPAr0jPlq0xBzdOKLJh-ShyaI_MvwR7q3t5bfCaXb9hLbkRutIrwuDk1grKTs023izdeXkfF0l9PDrDA_US0EhmAteb9Kv2KUBYb2pA3W5VwCHVz2aaHLw9OQ7ivrVLOGIMGPaot_WC2QxZ3ntREPA0M_WUhNx1Ht4WdcpfrdHGiI8rl5I0WHkHS6UfNgvm4LZq_J9qioBuUAbj94QartKawtKo7GK1FTNR6nkiFEGD0IwHTzQ_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101714" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=S3sl3mGa-J-s3ZOSZfn-BA7sjSui75XbRAj-Sl0BOm1_n3Y3BMjV1NZxqeHis_fA2aWUdukPtp85KCMf4XvX2LNe55EfxJ7RY1C5hIy8Ssf1A4GbbrUc-gGSUpLPdO7moGvnJLyxTsFby_QvmX3e78DdEdDT4zLAFAGrnaLrcd8X95diygyXIDwZ9X28aBMmvVaq5undelSVGfSiJtle91Aw52GqLxY-RXp9m0KycnF82A7Jp1YxS2iqzi2ZRuysTo3l4dG7JQSXxl-82iSczVp6wuiSGvQQlH-U9cn2DCOmEWMu3DFFA3ou2X6TQEWEgn7pgp6__K-HONoTl8hZqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=S3sl3mGa-J-s3ZOSZfn-BA7sjSui75XbRAj-Sl0BOm1_n3Y3BMjV1NZxqeHis_fA2aWUdukPtp85KCMf4XvX2LNe55EfxJ7RY1C5hIy8Ssf1A4GbbrUc-gGSUpLPdO7moGvnJLyxTsFby_QvmX3e78DdEdDT4zLAFAGrnaLrcd8X95diygyXIDwZ9X28aBMmvVaq5undelSVGfSiJtle91Aw52GqLxY-RXp9m0KycnF82A7Jp1YxS2iqzi2ZRuysTo3l4dG7JQSXxl-82iSczVp6wuiSGvQQlH-U9cn2DCOmEWMu3DFFA3ou2X6TQEWEgn7pgp6__K-HONoTl8hZqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=ujiOZ2YEQqxyubvwcin7QMg14C_nfzl7ZPTMstXb7IreEMzPjBfyN4CNyUSM44GCor9i-2J9UHP2T2Fdmo-afchQP-oawFkBualjpi-CXwAegKpr0rqmyZ00vB1-cq-h3UdigPJUvyaU0VCCWwBHXE5HAbfVm4BWyLMgxsLvFkBAtdacPvj0qZGcCI_L-lrdiSGgy9YAP1m6pOcOS0I7mh7tL1ObymKs6XCusDSiF57sfp_BaeJWtImXlZXMT3Vv69ETNmCX0VXs-GozFxqhIsIIn5pB9yEkUFjdu2OnfA7oJNz4kcigV2K9-V3upggqGJq2P9mEbnOHc73dEQt7rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=ujiOZ2YEQqxyubvwcin7QMg14C_nfzl7ZPTMstXb7IreEMzPjBfyN4CNyUSM44GCor9i-2J9UHP2T2Fdmo-afchQP-oawFkBualjpi-CXwAegKpr0rqmyZ00vB1-cq-h3UdigPJUvyaU0VCCWwBHXE5HAbfVm4BWyLMgxsLvFkBAtdacPvj0qZGcCI_L-lrdiSGgy9YAP1m6pOcOS0I7mh7tL1ObymKs6XCusDSiF57sfp_BaeJWtImXlZXMT3Vv69ETNmCX0VXs-GozFxqhIsIIn5pB9yEkUFjdu2OnfA7oJNz4kcigV2K9-V3upggqGJq2P9mEbnOHc73dEQt7rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
