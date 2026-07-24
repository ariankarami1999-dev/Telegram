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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 23:41:34</div>
<hr>

<div class="tg-post" id="msg-101835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQssKl4K0sbjOY-93pUKzjemIUDfr7dn-UnhSh1sl8PWoy-2OiS_yQBf3DNpiE-7IJ6q-Aut227cidbgGswHI2s_hw3YPrpk9eH8aEeVkIzaV4eznWE9wdOsCGz6DYlqH69oBY-bG61CmYBA5swII8Zs27mQm4jOlFKgm-yWf2AtMGglfyu1aAOm8yU0RWsTolta3mZ8O_MrVzXbQAXHXvYkQi2mmwHodmx-rr8fvUFYl62Mdkm8JsXRyzG7hoNiSVkRvJKUU_I861VswUOb6-g7QApIk1qFDdYmzDBH9Vrxow_UKjnDRFAvkb7FTjg5lg6gcC-YPzpcbMc-Ju4bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فهرست بازیکنان سانتوس برای بازی بعدیشون مشخص شد و نیمار به لیست برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/101835" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101834">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-CEXRC4nNi_EY7zJWzkogVfcK6QZHqZZCxpE0fkwU805e26DOxvZajlGWoMBkOenZQcPJk4-Jom-7E0Tu84RY13yPzKbA8KYlVXlCfN6CNZKFF94uVS3QCA5LylEu8rZFwnKHBJRhmCW67y2c2DtSzKixRgMRRKZHg_3ugwqzBmL-QQKo5WBlxz6a7CzIpOoNFV33YpVhHJH-hA8XvNV-MtoBvhRlydZVZ80MBPJmWlPaa4W-vzt73BkotjSUZ3iJQQQ43kOAAbDQixT47d7gB0ypWOU4DYiosn073lLg86ujESHPeen1IWmhTGHz0LC81LTZ5UMBndc3NvO_HyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لبرون جیمز ۴۱ ساله با فیلادلفیا سونی‌سیکسرز، یکی از مدعیان قهرمانی NBA در فصل آینده، قرارداد امضا کرده. این انتقال مثل این میمونه که لیونل مسی ۳۹ ساله برای فصل آینده با آرسنال قرارداد امضا کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/101834" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/Futball180TV/101833" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFxco8IjE66VR-rE4X6E0ZSGhrxZmFXWUvSqtrKdBkPf_wukH8hQQy2JsBZ9Av6OzhmSEMa-_aczT6M0oqAa4f52fG1Aeac-c7aMObLxTchl3PG0_BRBhii1iCnaqDy3iYaFUhF5y1elG4Z90Epd_aUICkGGsvWvJl3sThoP1SopLXylt6h45NsPtcIqJPvyYFRAFxIsgMJqpaydFeJEwaSfSthlRFiY7iwHctYhjnOMc2wRFngWFuC34cF6mQdRcNHZfCLdd4fAmihe-_tJsNh6Pxwy8ZlBteiPopK1Vp-7hsGEQz008swN_g_vcUW3VKM8L3mSdkkeKBlPQrmdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3oSbscJ_ZCHVjkr8oXJZR-fsZG54ZMpEQ59P_uFw98XjA7-jYU5T_N5zW18mgcEJUaKbItVe_yX5wjBzVgOkxOLOgnVM5lLsRc2Hec56Dxx5r-7Ye7FXxdMxBJ2hq1fgiXntPosv57rQliYucMjQ6PSqEIAG0wzZUCKkqL065V5XxeOlUKxRlKwcnbHxjVZhwn17JbXor6F9K_zCvFtTiuPEWXHS67pWH3giNctz4l3uDqN505woaz9RHZLJQtxmnZKxtT6nZcGERDI5jx8NK5cxNGEHvubB0tyHuLZw8ejd1Wz2uf96j0aef92Srt0m-y41DDsyRWoxPZVF0wkDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
نیکی نیکول گفته دلیل جداییش از لامین یامال، دخالت‌های زیاد مادر یامال بوده؛ از تماس‌های روزانه گرفته تا کنجکاوی درباره جزئیات رابطه و کلا مادر یامال علاقه خاصی داشته بدونه یامال تو رابطه با دوست دخترش چیکار میکنه! او مدعی شده این دخالت‌ها باعث خراب شدن رابطه شده و همین رفتارو در رابطه فعلی یامال با اینس گارسیا هم میبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/101831" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101829">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAt5iPLj__t7lMIrQ6cs4d0XSal9EUzZ0hnGzxpWBseSUwKIiDfDk0j3Rsg1KbtzGJxGWjUuTruvkQzjYs0q5XQVoUgzaAkez3N1z0P_zxnnLsMlJqQrKov1aFuyvtoHXfcnJOgF_7XprNMfHZwKJTgMyLZ2nHqy6gHv2H2KC1SRCjvANsktpXdD-5MyB3vN2R4aYlJzoPZt16IkmduFmwDhd8Cm420ue9jWpfHTrxkoSYmq95U6GAOyNx307tPenF_OTGXiFz7ePxSjS1faK5CBBp6roM4u3gUCb3oidcIQlsrV4NL_3OzI--XXC1EEnqsapjZzka4wcGnY_cLH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dg9ko3xT0_2JsoswkBJovv0oDTGFU5sVU6aOqsY7PyNlm1bqlJs4YSfzjq9hMAJuWGHPrMKIgzD6TJYGYvpuGus1XIsfB3FS0JJfKqe_Uo7kKUPzbpspdtr-ONQntNB4XbSQQYZVHhCOj43BGRIToUXW0ZGZ_FynQbo2QK9n0NBSScRwljIAPRkmfvDQVt-EnVnfR0OGVITNswD6HKJ404KD-iqhQoo_zewAwp8oij00xtuOAz6jstun_ZP2VJ1fKx0z7tEI0-K0YPqt3j3y_Yo2p2rYMB0StRH36J-GdxaF5Q-1NonmuGyhKFuZjLz9_ubGumaS3B3ZWulDsjI1EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
زمانی که رافائل لیائو تو میلان بود دوست‌دختر سابقش با استفاده از مدارک جعلی تلاش کرد ۲ میلیون دلار از حساب‌هاش منتقل کنه، اما ایجنت لیائو این اقدام رو کشف کرد. تحقیقات پلیس میلان جعل اسناد رو تأیید کرد و در نهایت دادگاه این دختره تیغ زن رو به پرداخت ۵ میلیون دلار غرامت محکوم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/101829" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101828">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBELRp1JN_dytesghmoDqUaUmUXf-itP2FefrljwWo9ooqAfKaZ36Xo33M8q0QeKrAbfhC0q66RcYmrdL1fdLbiAiHcvkc-XGg_Ni5kzAGFP2KsHcLhU8it_VHLz9RdZd27Hm7fHK60acL3Rtbwxe4X6IDNiSbCItc21D2Ad0HYfTeBy3Sr5jGMx7Vel7vh4eYFOEyc-lSaVVPe-s8I2p-bXN-QOVJlHZsWC04_tQi1SgacyQpF64Okhoc4OGtiFc04iphOdBP4B5FWuGeJYgUl3TC6CpIL_ZrOqnHqFIoRu72Sy38h0gNlxDXS2TdodrURzbaI4w7lHf9aX07n2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101828" target="_blank">📅 22:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101827">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpNkFkSeBqTrI0wpaRgGOMgIPQB1_VqmgWmf9TtgTcIfCgCu-OUtv473buM0XzzHa43N96xNr0Wm40qHvminLO8OtCgrZHREvR7gnA5F7xQkDR-fx9vbo8Qv1XrbGo2-pVhFw1Wa3g3YF0MD316A0-bziH_47N2tSa78TbIMMbyLDgjOQG5u0Sax4yHRJKKVILXsVw-pinV9eYlvZpRLr1WgObl26FWiAi9AqdDF61BSLAQ1Jfzu0F0ooFB1Trrk1p-n5O1aRdCIYdkp3qV9tYKEbUh9yBCkprBs_6pbFvtFiFoCgfLpH2ymGn7bXhsDkeJQUQmU2G7VP5Dc5YwvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇦
•
الهلال رسماً سامرویل رو با مبلغ 70 میلیون یورو از وستهام جذب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/101827" target="_blank">📅 22:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101826">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDtiSQ3T5kayivVpv2UbUwAsQGriPWhUh6QCJIKDLYQcBPWRdWLKVFlUtQxTQVwyoksuRk4Q_0E5GBcDdWBM1MjLcGwmw4uF-j52YiSzPuoQN1AVhWEhD3HbU6OqSJdV1mcwIs8yPGiAyIU8M7Y_aF5qEqXpr-uptHRTgVLuyihg3uxU2LoUh-OZz-uLql0ii1D6Xg6U5tnAzbJQX95SZcCQuCJjzaqL4kF3syAEwvGj4kPxDyQFwuJ3qI-jHEpKwBDi2oMlXUyw9REYgLakS5vl5XHKXrfiZNf_JrmhTv-RyPUW0B-DDA3cvVEg0A6u2h023xuJYfaZEzZH8L5ZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین: رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/Futball180TV/101826" target="_blank">📅 22:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101823">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k50o01M4o1plzV76Y0Ixp5_QzbF4BP9nI49McDk4l3jgJe8GprtqBhy8YuTx34omZKhVjmssYJfWdrPjn80g-gCjFLEA33ivEjWO9w1xnxsqf3Su5YJqBEgAYthkyXlY8OXH1Z0JZMcxLESH0HIgnSOeim_L6OI3P1ODUKY_kz51Bo6LZINXtgpV0QGh4j7U6pkUAMLsyY_kqpH_e18i9ZIDuQ2rFYTEtYbGsu3XB12G0ZkNnSpit6Lpsawf2WGr0Cz70eAibiGfhb_cmUViNTPqIqaPqWUKDElTzQURvYwOtOWULRQS6twV_nJPkq55s-aIHcuSRBQnN2Mi9NGhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🎙
ووزينيا درباره شایعات پیوستن به اینتر میامی و بازی کنار لیونل مسی:
من عاشق فوتبال هستم. اینکه در ۴۰ سالگی هنوز اینجا هستم، به خاطر علاقه واقعی‌ام به این ورزش است. میخواهم حداقل یک یا دو سال دیگر بازی کنم. امیدوارم باشگاهی را پیدا کنم که واقعا من را به‌عنوان یک فوتبالیست بخواهد، نه فقط برای اهداف تبلیغاتی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/101823" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101822">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB9HU5ZK1y_pES4u6u2TlDRba_hyod27-NgTMHFx0oP92ZfocS-qG5dAHlXUgIPM69ryZlPIOqiSyv78xWbpokeNHP-7cb9bQYxlYR_HzfzGiM1cnqO9Z-EGEWR7q00njUyZ-Z_onyqOF9aopNSbSdMd8P8PnWkYFQ2Qv_Xyofll_FsrISJwJCvgdpjPAN2B8vZ7IW1lJFMcCw77ggL-q3jbXXW5lG3GiQRutVGs2Ngp2D1R7FnDbdiSXZLUlyoj7ogZ5clDiBCEb_YZsclE9Yk_HLhdQJnpojYw3uf0X1nemvqlSRklaxOPEY4qrDYjZDGAa0eUW9i19LtlAv0g_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین:
رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101822" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101821">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101821" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101816">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/101816" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101815">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEux3hSr_EyLFEDL3A8Z_Cekj9EORJmiIH7nUkmpeh84ChE7GYx8Vt0UbIrnkP7UETzBg36TKT49RxW9Dj2aGwi0CDgvphIL-1diMlwNWMkvn2WLdB6jDRCqgdLErTFFBF5Ya6ph_DMNA37m5olyy9BdLu71LiW8Tl_OSZLLO4GONKPgcGMtCUc8JILJv6JtzJTljV1_7qYe_1Zi8RIXewbc53DyNIv1Fq7qMm8qEGZRq9QKIwJirpchaWIIi2TTOX8GieaE6JxFeqOC11yWxiPoGC4x3cv8jU9H0FCeTp9JejoDklzlbO9ajOTMjNYT1sqoukY96cHQAbDYAgJrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال ۲۰۲۶ معرفی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101815" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101814">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbhFBmq260arm3fEGDVcE0ASX5xKIVgqwTh9b4zcI2WjZAr8YKYqlD0ce_cF9Q9SpmLO8Nka7tPhWBlrN0Myn49mK-OS9cMRjXqHxxtqboll8ttCSX9BdhXfUY33H1QDvFdpD1uaYa41PsJiuBU8ES_AvKviigh9h0wVs-RLX8Pc_w1CsYnNrNNotLC0YiCtgFJpIUuvp08iKUXm0TFRlJuqVGmaKffoN2wgJdTmfgQQn0GGb5t5zl511JpxYsayWX3mlaCiHm35p-VSl5VyQgvGP-fc_F21XpM9yT8dWxZlIb1DMneABWmDKPx0rOU_PZsJN6GrZG_KHJW9THxa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101814" target="_blank">📅 21:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101813">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3wsmScmC8GSoOd1umJuMyXs_IAoFkgVN2a8KvxZbPpjtwbaHM-_9Xa4ImnKUqRSEfFQoUfgRHBbTcImQG-7FZMqMJKZ7hXMPXG4dzEzpSVrUWwgSfth7ZPeqPmr0G9EHWxlWR8zNSkY_Vvrh7sQ1-DIwnNa3RiTEQsWtD3DEoLEBJS2xDgO9W-7NfIskcXe8wiYND7RyvO2b2pk7JLJGOoVUXh_yuvuoGL_MlNlAL4wiNO8CPNgmkDwPK1rexZnCsN7eCLM7d087a2M79Lc4KzWyngJu1VKJPNi-4x8Epi5JW2KiLUqW1q3xLTGwDnZY4QFXAJrN9lbxHYP3dZtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
کریستین فالک:
‼️
بایرن مونیخ تابستون امسال مایکل اولیسه رو نمی‌فروشه و بررسی احتمال جدایی او به تابستون سال آینده موکول شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101813" target="_blank">📅 21:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101811">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWN96zd9e-f4EDj-eq2KcxFj3S8VRosoActk10afebmAJHJi4dboBDktd7Yd89dFZPcHX3w0daS9q7KwmjyewzULnDug4HSm-0ueJG1bl2meA1aPZ-GT-BKZhEpAQjdvGIPEpf1UdLrGHoROmiP_wFmZQ7CteZ71cenomBp18pJQmF4rhpPmXhVWfL5xe03q-ScPK_iVrWPg46_bGox-T6idbauZYJcp3fpY7z4diUnWGIJO77JKC_u2dsLBuO-AOAMhSw5ylSX15tln1gJ26dytJ2H05j-2sm0o2ZjOKvpQq5C_dB9W8oXctajtz8_Z5bUxsOD3qQrBJG5IvyyDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4jUlj0SQCda3FQNcScC1W-xtJxYpNv3Rss0Lz3Wyw_Y2DXX7qMEVkUjCMYHYRo3q_SY0f0zaiZY4Oy19ognjlwVzYkam2QSODUR2dp4gaPjFZ_RKB-q4RneVnGnk7wFBhNQkbhkH44Oa3WXU-lzRumc9KpvMkhro2kHahmxycwPAXdWXjqYiRLynB-K1X1bjoZW3OHdIbGeyU8QxiZro6SC9YzhdVXEgB1n73EsSvAXa2hW_WSjRQtbXaLdBGuPKYFXhcJpXL2H4u6-2N-65L3ahsWR5KXzN7NmEZ1kfN6r7mqo5itubLLVAKLBxzC6J1ZchncTI6te-fO6aldR2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
💎
۹۱۵ روز پیش، پائو کوبارسی اولین بازی خود را برای بارسلونا انجام داد؛ در حالی که تنها ۱۶ سال داشت. حالا او قهرمان جهان است و ۵ جام با بارسلونا کسب کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101811" target="_blank">📅 21:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101810">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101810" target="_blank">📅 21:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101809">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euCNY-lNNS7xn0eljc7imZXE-w2NH26cWJbGEi-QnDjRvuhImtBp-AVtPVTJVhdE4kfntyYmXxkUmc-1CkaVc5eEoB9inw02dD6ZhPi2pj-2B4QbesUaZP8Z1K0t1CW-NPseaYEq3cepU1elpjXcV-T7k0Kix5aEvbrkwJJNTpF6J3fyXZPHalV_cfDpJwRMs-oXiZSea8stsUN1xGt9YW_hcNNthLVxMQ_sfZZ8er5XVO_FthTjZVfSNXvmfTA4sSs2utOC2zro0kRCi-7h2rhjytXyrviF218afFX8osAQyB5jjcgGi7OescU3oYGjxg6dkbJkvs--1X2d_jgmjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
فوووووری اکبر عبدی بازیگر سال‌های متمادی ایران به دلیل بیماری قلبی در سال ۶۶ سالگی درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101809" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101808">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwxgWjgkgr9xuw87OzQxUMfadcga7UksRFgaXu60ZW-_-YWDngYr2ze3g_dBhR4aDUR1RhXyAlrz38m7wM4QjvF7cH49Jb25g-gOtjhFTUaCLXBqwSWjUDB3EvYYAVaehi9cqD77wAM1gc3RW-bBd5tplfQL8pDNpnRyt_-ZsOw1gjJegf5L6yvNhwAh04WaQuf0lmzN2dhb3ynj40Lgy4w6cgGSsv5nn6-YI2GuYYPToQllAgqhF67TBFfGlq_GAsgzKvQSmnKnXwf4d3YCOA0lRBIOucmo0Kgw2jbX68DkEQzNhErwpCYRBrWGpnQatTycZcxGIR4UkuMyAbGvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
کریستیانو رونالدو تنها بازیکن تاریخ فوتبال است که در ۴ سال تقویمی مختلف، میانگین بیش از ۱ گل در هر بازی را ثبت کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101808" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101806">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/101806" target="_blank">📅 20:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101805">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdetRpkX-IaULYBaMFuhqaCQrzGyOgx71P8vAF564fuB2P9kHWikff9Sg9L0TKiSQHHnrsFgAqjoPFRT8oGo2qoubM8qIFXhQnSOUFrkJs-iKvrfwSmbvYOWz6OSequ19uwYdzkWUBG6dYRuZZIwa3Qs_tSLbKzKOMXap3NDFEDrRApzapZ5r7H1rM8ZZt-M1lSc08axc_gC7pDJ_1Xd-DYw8jILdR_kwYNp7cdD4UpPZ4KLUgrvQknfjE8-4c0RU7rKFI-gbbWSInSmO3iac4e7jEwkr20AUI3b6lKd6dwYn-gNn0CVyl29zT2--K7K0whweV-fpjaKgz-IG9Z0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیساندرو مارتینز درباره کسایی که از شکست آرژانتین خوشحال شدن:
سقوط بزرگان همیشه باعث خوشحالی افراد معمولی بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101805" target="_blank">📅 20:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101804">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpImD531ym9jpkB9QMNCA9CfFX3SUQS1ZvvvzQPPNragmer-tZbz4OstlRfP__thLUc6qr7OpcKTLMEvWkHzQ_fJJ47VzbW-LuoM2Ih6GELHn9gGOe6dJxcZCv2voW7eRvjOA_A39vry8ZrEvPCtz9lRrDttFO5RkB_ptQskb_4lEziyPjZMTf-HUIlcvvle7C1S9PtuI_5SrzVaLpICb6SfgHvG0_AVPFT9d1zt6BUbFVx1eAcv6fYrf8BiHI1wsXh_KQnrIQjwcUjnpTbudAt4Y_XZXXpCsOxlT4viu_onxYb6OGsNonUTKSVUUxcWW9nuFJ97dt-q8ncYKK2A8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
فِران تورس از شرایطش در بارسلونا ناراضی است و تردیدها درباره آینده‌اش، احتمال جدایی او را بیشتر کرده. او احساس میکند هیچ‌وقت گزینه اول تیم نبوده و باشگاه ارزش واقعی‌اش را ندانسته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101804" target="_blank">📅 20:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101802">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkcUSJPywdAajBVBt0LBGKpnOslQw3d2gWhJm3y92NN-9-PTTkeknTkfoVfWgLKU1SquYO6OsiL8LxzU5T4xxBx3I5CMVixtAr8it2UDFP5KWoXEJ7XIbv4kpIYp72JgIMr3MzhJF63SyeCeOJlVdpyibrzXN_upGHIAgSDrDvXyneHnd97owWuVIaZ5epd01EBWUP3cMpzhqUIcF59fj2DRg1CaTnnRewWk2lfJkl21-ZqZ07r_4uLCr3u8TdzgZTTJ79NB5ZcvaAKN5O5AjxiT0YCOItkk5YFdCxLvoZf1qRgdGeL0v3IKKN4T6cwl9OyDrRGdN34Ymsm-_tmFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9SLn0myP8JiKbG_qF6fA2GYEhc8tbKS6tsQUyjwYIR5cyc-haf34YY2vJ4UqetMP--abVcZenk9WKMKVVLPsuREAGoR59WCpWpsGFsf23ZJpkBxcZgX1c-5qL6_gzqiC-s6WL5AM4-wfD09mJSjnjNZUOsbZ_bsYfrFIJe3brTe7r-tCcfND0Fp6qeNPitR9zEXQkUjE1lejdRMNvWJ3NTagb0qXNLwBxH508Ilt9dDqAJbTD0hWwoIqygFXb2giPWc5e2W9OD1Jrm6KD7NCWuhgNRcTAAYwoMhER7VfUxZUDaCz9MVQNa1n-lsURc8E_D3WbNav39ROEm_MrJnfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدن سکسی‌ای که فرناندو تورس ساخته.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101802" target="_blank">📅 20:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101801">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101801" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101800">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYoeN-9h9KLX8z72DC9XwKCPZUd5dgRgLvpO-nyXSUvpUd8ynbutZiEBIukOPdb_F1bsGG7KZEw0aJaTbgf8V1gba6HehzbawAa36zCMDqjLEjOOOHwZJ0F_RlLUayYAQnloAQk9VoRG_iqI-PRegvmCj2fg_aCIIBaLUH1eXog_h39DmcvJ9P5cwbiDv_LHX5v9DA0XWPIg0DL-_mvBWdiKwZudLrxiTXt766zuQBs6ANykRQU7l1yM6aZJ5WSPlCjsHHKcp9eV6NBmdx8vw9rLeo_RvksEYOf_rmvvmEm8jtFv3DMxzaT_o4iP9NcOsJlNiSKArhJkdneBT20ftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
الاهلی مصر اعلام کرد که روز ۱۹ آگوست در جام خوان‌گمپر به مصاف بارسلونا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101800" target="_blank">📅 19:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101799">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyqw_xrrU-0-tM6kZorXwWoxh5JHTR4Aez_BfTjbT1iw6lkyNEhIsuxS0aX42s5UtgV8SYBfT9nM-0uUgrufYvTd8EppHYXNjr1BvApYWnVvnFpLyxfiwHe5IcMkNoHkRFVWEZDXJtzsRe_V-zQjVbpBSVfIFo5S89RCi4Le6FsM9CxqgboAWQ5dZ81kNI_YAbqoJIjqVBqzRoBuu8nqyiyWmdR7LSSyniYk2BH8dp3qewpPv1Z8oNaD8fRNG_VHI2C31VQXDikLxwSIsJd49qtIrROGnlCZxSLF2r-A1qBN1JB2Nc-rLO30FL3YeNvTeTbbhoy5VIvauKEelMt4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لئاندرو پاردس فقط ۵ روز بعد از بازی در فینال جام جهانی، با بازوبند کاپیتانی بوکا جونیورز در کوپا سودآمریکانا به میدان رفت! هافبک آرژانتینی از ابتدا بازی کرد، ۹۰ دقیقه کامل در زمین بود و حتی پاس گل پیروزی‌بخش تیمش را هم ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101799" target="_blank">📅 19:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101798">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC_J6gGFX9scfc6dFd0AW5e1Q7gg4tL34dY8Kcn58gPrVZAmmuwnd1hftbMADkPRy5Vd7NzAKxIpRBi6YB-O8ikEdiEOkdZ-W_GRjyUF47W4BLnjQpW6KGzG6plg-eLFAhBxX2JF0KzI-cZHAhOSGW03tIPbs9FYOmbGoarxa9uu_T5AeVBK2ahAhI8Ztu058yirLfptMVgtpYs1iTYrT1KcYL7sxvvZXEiJ90D2WZ5RBYegkhievykP7ygTTibn2LT5g9Eku97wp9vZBq-IypU_jJq4nEqJtBVqeMLF9JDLBwZhdJRZmen2Lu8txclLmmF_B5fyxcnEP2s5xueQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
فابريزيو رومانو: پیرلو به تیم ملی ایتالیا 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101798" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101797">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101797" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101796">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVQHCcx78PpN6lotQPJM11Hp_aPNe9kJGsi1yxqwGUsEYiSgqUWCwyQkrH7XOLLmasmgRYI2aOi1igpygeBG8LQX5S7x8cMoSuGeAGBHh0Ac_3jiWfom7Ffx_JOk1LT5d2YER9kJl8wrjPnczIUz6o8lu3l1UwoNd9N3zNmQrmrSRDzH0bxPSpsGJyII4qZ0RWGDgvX9ix_mF--TLalgotRmPhBqGl0PNnO6GoIrnBquxAqTXZGc5PnFs4O6pm3SWjc-7qVbDOGJ-5FiiL7vNzmuyKUlLM1NkaqbkYasf69UMINz0xaEc-_rQ0RB6d1QZzsD7BKyBEDCZwNx_be5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💀
مثلث‌خط حمله فصل بعد بارسلونا: GAY
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101796" target="_blank">📅 19:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101795">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrDyMCxWa_MXZ32hykJ3kGDrLWXHGOUeIZlhXbQki0rrBXTixQbgq9IEtlr_lfUN9iYg3KAJaXnmnMh-fpvjISR2QUSULRv6f0dSbcHF33gUgZgIbz-iDhcFLR6DH7i1aMm5P_jWEXNNIIOBa454Z2Tq7fHqPaJl11ULO-V6vGRaakt7KeTSMTHuo6kTC1jHc3Oihibw58WHcKtOHEYlejBnFewcTwpCSo77tEL9wMRJG0YsKTu1Sdhystl1r1vtCnv6ZzBFnoCUxFnz91A5SIXh-Xo50itJY9Rql88SmtC9xu6lncI4-Uf8tfhSkFuUc5v9imiiOF_gLdnIzqT0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
⚽️
بیشترین دستمزد هفتگی در سیتیزن‌ها.
💰
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/101795" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101794">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101794" target="_blank">📅 18:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101793">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101793" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101792">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101792" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101791">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101791" target="_blank">📅 17:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101790">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👀
یک استعداد دیگه در کارخانه لاماسیا درحال ساخته شدنه؛ سال‌ها بعد اسمشو قراره زیاد بشنوید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101790" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101789">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeTRckbG8rf501Apoe_jADIbMkPG5k6Jua-PY-EnkCDOs6HHk6CY3qoCpZ6zYHWE7IJldiBkxwDrOBqKEBPVE9ir_22wb7uAsYlivdRCyv7Ihfz5Sx3gkHavJFG9K7yvH10AzPG3IBO-cerMq2qk6XjtFiEd6U0A7Il1TM5au_ehYPJzeWyYrYuCcbA_wyt5CuLYkyskDcrhieguou3z9mWveARJwh7NtqjHNMKAyye2zDYYa02617uDVw9Chqp7vPovzDkvp30PgPoNKoE41i6ToDuvIW3TMfVIGGw_6_RriLu9y1BmOY5Yacux49jszUU-BDREAPFQ3JYA90PDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رئال‌مادرید به رودری اعلام کرده که مشکلی با عمل جراحی مربوط به مصدومیت غضروفی این بازیکن و غیبت برای چند هفته ندارد و تصمیم نهایی برای عقد قرارداد به این بازیکن واگذار شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101789" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101787">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFu2W1LxLl_tyNaYbEjhCnmc_PvM5h1NNvzARypqy6mlPA8uBJ-8Ea1eZ6Sa5WJUVqxL8ofGUVAXgjE7CR2mZFlHo2UUweNy0gIB0UOYWR2B2QZTkN-8pd94OS5sRqcwrzlmclHfAFRQa7MmBbL9_10KVcn0_xCjgeDQRrFf7R0A70KpDd8i6-Pn9A41GWMWHsTFXf707klsOGlXD9i1c5BMKJFIfyNvkCZiTWRbpzxvz_9oH5mdiUgOf_zE6G3SPJ2Uzj_iCxI7VbmXzu3HWGSkr-ZU6HtiM2BjBMM1DzRkicZkDlEN2DVDJ4kUF4QRK-CbJVjQ6yRW3mQ1AluPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCnNI-AV8aSsMeWS7Gml5b0CDsoGsromc6LrJlYoMuP__8f8ewSf_AYza3wQcFNPmveVUaJAjFZ-jFN5hiLx9zNfgvoJwkZuGGXXXIpct3tiw9NLPVrfjR_Tt4fZ1mE-8zFsHm-3GDCrAj7IEuiSp9u8G_2Q573ul92jlMhaQ7XlQxzMnGCHsmEWg1PE0mO-zV4_upagjIKXz4rPo3fc2kj00AJbaZfpYtd-llJdIr4iEsDWabcewgMFGcZfWP2XdpdyHzUTm9TMgP2WwrT1NlCv1q6lAaZbSbe3bw5Enm3gUK0zawCK-qgkJ1z9FMuJOBI_7-RHvDAUnIrQhc0ikg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مشکوک به نظر میرسی هالندعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101787" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzLDowtEaEwmYu3s6WFGqSZfioBM-EK6Cx7NMSri2YxyoBPqrWV6E9bXkM3oWdc7Ik2cGsWSUb1_bwFz3gLHLEqEXYPSjQtIF444adA_CgBBEtakfQWXiDSIvK6N8RprY2v6gSwKUb-pIS3hIyXqXv3OoJi2nxOOcitCz4DDnTsZNRQQMcacAEfKlCGV0vtZgEiL9cZX2y-q2Dcn6NhSBlyimeAzOBVJxb4mEgFxTNsG0--VHSj0hqjqh1QYNFPVC82c8NYJziPfd2ilLDlpzt-i6y35f8A0l1IqS7JBwXLDCXC4GZvI_8ItS9OIL3yhTRs24QfxSeZugBdJSzviag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTBsOkQ3od8OpQnPP1ReSA57N_P4zA3cvX6E4_47rWgDICUfeLa7aJrbZNsGNP7IhEFkjc2m8YI0jyblU7GZ5ZEPEYJNP67esFSiLH80IQQoxE8xh_Lu62c7a758Bchakh0hSIhSjnsHWm9nlPtfhXKhn07a7U5gPF8p-dkmHqbMgzJP1MxvIhzXl3H6-XpB6D_qyLdKjwvKBhG9MjOILTj9d76UC9INFTLOLEXx_G9Z-xp7uXZQOVx039tgOrkVF1wx7ykvg1fu0v-T672sw-ebn9nPQZ9toxoRE87TdmSDX3YXe8s93BW-SSExcOmEJetoy7j2XXHRt4I-6C37WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avuIHVUerGqT3mSBMqqFQ2qNcGXUK0jQ9y8RZ-cE2Ml-6M3feHXBNZoN6SRInCGz8gouE5OFDMdbXrG9w-wWwx39akZszjcEWwcmkW5wC7AcwNEwsR8tDIj2G71UDUnFbPWO2wsSWnU1H-9SXlENDSFZHtHwOiJnVxAYtz7JjljRF_wpuJ1LNu4wN2S4OHP7ZKGB_Nl9-K0ifnC5fPgxg7TMiqheqrFqgEKX7TAEmeK9QcfMtbpq6RO3mujyzDWIg-BTgCm-6Jy_Ygyxohmt0hSV5wWQEovHjw-gAhrGSnY1a_tpJrCWB04ESEQ2ssMrFZtIddTqQbsWPiSImF9zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101780">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_znP4s3fCsr8s_6r2faaC_mmBR0FXME12_t241SZqZt_pu_sJsbjSnj9YDPpF5IkiyH2zcB9KKFQSNBJuml_3F1iS4TtA2zm8N9av1qIE2atdhMYdydyrSe4W8lZV3cYfTB7Yh6Vck8ymMX1rPutlc7r9ujZ_MSc9762d0mSV1FW4WoUlNXrGQaXeInAZ4yhYenVsfovWu_LH-D8OI8938Lw6GvDpzbr-T9WH622JCHFtWihCPwEXB6OgLTTbyQMASqHdHydJQlVzj_L5TIu48CX9YRGMFv7arAZcIUFRtmTBRZUlpDlLQj_S3RpXDmqkYaxXDcbhfqwb3FPMHkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینتر دید کسی حواسش نیست رفت به یه تیم از دسته 5 آلمان 16 تا گل زد. دوستانه نیست این دشمنانه‌ست بیشتر.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101780" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101779">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f574b376.mp4?token=PaTC_YWaZWV_e2QRJTBmA-gjW6qNbQygPv6Crrwv5cgCRBiaajRyDheQYau52NDR2FNXRXequHtrQxOwbk_hxZ65XhxHZTr7n2OZDrdg653V3A9MTcL2nRUOAmBs-pfOSryVP3_IlhJxCZogOHxsncC659R8UaeqtORrNwrBn33NgW2NzOhBHP-X6bb7dt8YMRLEQOQ22xEx9srZga8n3rVvGeevVPudFPGWuPnFvqsDgO2rqtGsNYQqQQ8sZtcdXMirnP4hdQnmG_lEts5PwTwVH2MXMVVAp-XoURUaecfKFcOUNc1G3k9cGQ2lCAWo-IA-FUMncIutdN9uxiR-mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f574b376.mp4?token=PaTC_YWaZWV_e2QRJTBmA-gjW6qNbQygPv6Crrwv5cgCRBiaajRyDheQYau52NDR2FNXRXequHtrQxOwbk_hxZ65XhxHZTr7n2OZDrdg653V3A9MTcL2nRUOAmBs-pfOSryVP3_IlhJxCZogOHxsncC659R8UaeqtORrNwrBn33NgW2NzOhBHP-X6bb7dt8YMRLEQOQ22xEx9srZga8n3rVvGeevVPudFPGWuPnFvqsDgO2rqtGsNYQqQQ8sZtcdXMirnP4hdQnmG_lEts5PwTwVH2MXMVVAp-XoURUaecfKFcOUNc1G3k9cGQ2lCAWo-IA-FUMncIutdN9uxiR-mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
برخی از سوپرگل‌های لوئیز سوارز در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101779" target="_blank">📅 16:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101778">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101778" target="_blank">📅 15:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101777">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">▶️
👤
به بهانه تولد 49 سالگی مهدی مهدوی‌کیا ستاره سابق پرسپولیس؛ تمام گلهایی که در در تیم ملی به ثمر رسانده را در این ویدیو می‌توانید ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101777" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101776">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfurPxkr3b3GGrFzNcrw5UewEl_jYP9757ujNvUnLRV2hbQD6PnvKtS11LXsRaRyrI82sZYc-tLWOG6CrFXTdM3eSD9qfRmMD5p8Ka7OXDwbRa4vPlpYvtdRKHUTQg9TcH4krxXTEG2Nhdro54r2YL-jx3or2-hI_GzOXDArFsUXHm_ZDGP8bLZtNAxOyjBSCpgZ2uWZ8TS0hN2-i8IxpOoqKJVNuyUxrhSf3fwDGQ4I6MeMBqUDsoPyloh37i4YvknNagheTB9T1ndAk2fkEmEuJvbIpwPJxr5KLCsf0orN0Iu2VFR1ERMkCeVZ7IWqKUF2PFDVg2MFzszi2cqY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇩🇪
یورگن کلوپ:
با چیزی که خیلی مخالفم فحش به خانوادست! اگر به خانواده‌ام توهین کنید، من می‌روم. اگر روزی فکر کردید من مربی بدی هستم، مستقیم به خودم بگویید؛ همان لحظه بدون اینکه حتی غرامتی بخواهم، کنار می‌روم. من این کار را برای خودم انجام نمی‌دهم، برای شما انجام می‌دهم. با وجود اینکه دیدم با ناگلزمان و توخل چه رفتاری شد، این مسئولیت را پذیرفتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101776" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz2sQB_9XbpS2IFCYHNB4glIn5QlaxpZCTvZd1hID2IVMohFsprEopYm8RhotiOvIYQeTe-9kDWqwtzpXRgx7cb2UwCif4imS8vSdLiKwXj3XX7I2PqYl5nnd2VNjoEzdDVh_yLD2o_LA0O0MddM45z-E9KsifxJFVvL732Z2ADvh0OEIH_AXk9UVDx_XGVP_zaT4na2FS4T4t32P3pHw-qULSlqlE9Hi5ePz7-JLwdz0Tw_XGutHeKAERDs1rjVLacWoIMRH1_uvzd7kzkqcvivj0mcI5BpIEJrBmPrUa15qqsoB6-OLx7xIHwl4oZ27AC-QjdMJc5lTUfcbmp5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9B2DCE4Th6xLxSPv1vubzwMtklXKOHPgZihEH879abouLfkrwUYd-woPnbdyG7MQM4Nl_T0bb0cB31MQuD8MeBmqcldPu4R24HTfr2hjkZCQt5bvtiHhN79xJpsW7HusymDzQ-dbyijD8IIL7x-To5r4XbbulefixvQtBUiHpkzNMrgMNUXstgAPNWHaVZwQNN_4HIhH6DiaMHClN4ODGNaUJrnjvONa93XrMtumQGplfOYuVMC_OehTrYCsdwbRW17whG4mqUBztIO7f6Jdul_iw0XwTSWcaO1ma6PA_QT17cdISTOoYwiBenIYTSQDk5pIcJPnsi4Yr7TMvLV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewPwmcDrX0Y69VoMzSy6OB3Ur2f0iWgjnIIlXlPteAruMkV6k10mNwgbNKt7EjZ-AvMhajvnGqedy6G-sLxKB1dmNjcGmWJWea9Kxr1542UfCV51mG96iI1w8Vk4Na1GTZ-N1RtR6bmzEIusaPpdVFfG_ROhUi6-2u44fEPX6HXNiZ5BVizEk2ve8VutMsR7EYyYSqrR91tKhJojGkujhVh2RjsbUdyqQ8XbsSg3a0--oQQisex0MDNsabK5GviYuGBCfflPLRv2mi8VzHL6cA3rDBwJOWSSsJrI-rkv4UHNDJsZ2nBDXoKeO1xyEgB1fsou5Uh_Em-9sY9QM2l8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blFjT0z1byrrXQMlu2KVMUU6Wvw_c0Emi29sYV8L9LlOR0m001nuuELzG50bcIYSapWh6PgbBXlAUj5vqkl9r6rWUzuPcTX1CrxY2sOxc6xQ3ySNQhkLuilcMwp1Gcce75GomcmuD4Ojis4grdQt8jwIdnweh4kOg8ubl7bGsO06j4ZMRxDP8qKUbsf4w5ay5qLONNLXKyirfxcd5ar5NxN0MnJ0mObmpyjzyKHEZ1LN3btMXwDqL7Vx-3M52oMlwTIDDCgNf3JK_F4GJvRnVOyQr65R5-Wgh8wDyheMfxh0ol8S8Xe5bLMvSzUHy4DH02kjOWtsi1_1dnwQJpWB7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV0Hu5Uyco2kePNvckgobnhYwi-3LpQO8DV3mppixXOZ99E2v0DaqRvprG6zGBExzoFSeOYLAuaVksXgb9q7J0fJkQ16hCWYJ1463fPYiH4RcepKcafHceDRkySHl5rC9qdXPdhwX_2zIOswf4hs7zl6yiNLJa-sVGGmQfpt0o-vi_GX1nN56a2PS-UrjzXt9qfZbBs1fxr5GWLYx-P7_GIHl4do_gnJW3MhERItOrJUzkMKrC8KMqvmioCK20usfuWyvO7vqpGJCVmFWT1X74S3x_fATacqq4cvXDB_fwqzuFkJLYH53z2DyLwejd3_v-HcLR6WWESMejCFylUiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJq9W1_DMC7VMgMqfCCf2TVx7sVaocImycXL68JQglO3P5u0sA7ce7ogL6rVT13awK9S-MPj5hpW1BQgc5ogPXnQidzx3tNOlJ4Txk9dvuR1DPVPnPlem13T5QXK7n-V6AnXzpc4i7OVpWYc5iO4G5-EM1W54OVh48Qw7uO5TmGby1X8HUzY8H4B0H0Fsyi84Pw3dvzcqmlxmRmhy3CIobs-NGBMEqivSfxlA8qJAfYP3EVmMQgQjsqqkijPSKIN3xOCt-GcN_Rx1U-wVqlvABVDyjs94ArM-aVnCSqis22RiJwhTxIdmuzsmQ2gPDRRXkTBtOzkwI9BDr_Cgemw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhpcgCfdosoUdpGnn2bEYJNnZk6ySyBKPZu11x_Gb19UC6KEAix9Ms8EaTfm7tiwEBjgxBpBewze_khKr_ZSZF481uhpx77ULGpghpipRn2Dac8EeokLmxbZYoMrnjbpjp0ug-_lVDuu-nJp0DILoWhfGUZkaA2v84ib7bdzNP9VRr0wzsD91rE9vYk0PR3c4KZ38EU-DZquMSX5jQ7LGZ_UGLdcXrPg8UXUvDGXVm79QWc2YNtSLDyIsoM1Qr7QJQwMIrTS6gcjfllzSWs_WGRHyon85apCPxd-RJ9JcsebrSz_agZFwu_Uv7gUwrIVvrOEGDj6wpJ5fHepB7qRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101766">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=i2DEiBFKdr72JNFBAKOiqFuxcuMYyIv141NbxkufzQFtmujbN1-1DX6NrOkJiipBlU-PYc3zXi8Iu0r6iqM17fPEDPRyMElo8J-gEwOEa6WVVJVgbYxFaUvNw82ir_FZNMApO9kIa_wo7EOALJ9_7jgH8-6FQBrrib_f0XqUnrUOTdKI7X0vUyJh9AQ5h6amJtnYj0bIK1ThQ_-soDNkhSDnOJMn6tGCUKXsRAtO3hEwa7ihaG0rA3fVbssVFV0j7sMrgxFgNCH8HbXvASgzfuvfyXvbv7ro18mc_zYtxEhw7F6pql7Z2Ltojate88OomvM2hJ-mvAxj9c5jvrfLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=i2DEiBFKdr72JNFBAKOiqFuxcuMYyIv141NbxkufzQFtmujbN1-1DX6NrOkJiipBlU-PYc3zXi8Iu0r6iqM17fPEDPRyMElo8J-gEwOEa6WVVJVgbYxFaUvNw82ir_FZNMApO9kIa_wo7EOALJ9_7jgH8-6FQBrrib_f0XqUnrUOTdKI7X0vUyJh9AQ5h6amJtnYj0bIK1ThQ_-soDNkhSDnOJMn6tGCUKXsRAtO3hEwa7ihaG0rA3fVbssVFV0j7sMrgxFgNCH8HbXvASgzfuvfyXvbv7ro18mc_zYtxEhw7F6pql7Z2Ltojate88OomvM2hJ-mvAxj9c5jvrfLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
مصدومیت شدید یک ورزشکار در جریان مسابقات مردان‌آهنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101766" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101765">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sD-pRhXIu-mUG2SWZAquErJcyU5fTZwqA2xMAqMryX6bdm6Rar1AmLW5FsTiWr3LNZnTyIU0kwyRQhkdfszCYp9sCITkwR0eUE7UN31Qp9D277MlSRfCASzWyaksD16wj_x9XLEc-7VMfxpSf0jxEGPRFxX-H1vTtgMewGaNUiCG0WOi78FYi8etKq8uX1E7xb9OuTMUMpaQ0-ReuwDQvHWCVhB7qtJl9m0ZOYK5UixCrOho8hMqg-rYYhMFxFY4jzWs1-bKRzsajso6uwhA8-Md_C8gPG6_wFbXxkRRY-KhjsTtz1N2g2D_6KciWsDYS2Cl-CPTo1QO1JFqixSgyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sD-pRhXIu-mUG2SWZAquErJcyU5fTZwqA2xMAqMryX6bdm6Rar1AmLW5FsTiWr3LNZnTyIU0kwyRQhkdfszCYp9sCITkwR0eUE7UN31Qp9D277MlSRfCASzWyaksD16wj_x9XLEc-7VMfxpSf0jxEGPRFxX-H1vTtgMewGaNUiCG0WOi78FYi8etKq8uX1E7xb9OuTMUMpaQ0-ReuwDQvHWCVhB7qtJl9m0ZOYK5UixCrOho8hMqg-rYYhMFxFY4jzWs1-bKRzsajso6uwhA8-Md_C8gPG6_wFbXxkRRY-KhjsTtz1N2g2D_6KciWsDYS2Cl-CPTo1QO1JFqixSgyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
افشاگری پشم‌ریزون اوجی وزیرنفت‌ دولت ابراهیم رئیسی: موساد به من زنگ زد گفت ۳+۵ چند می شود و سپس خط لوله هشتم انتقال گاز به شمال کشور را منفجر کرد!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101765" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101764">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=EEF2ZKkN5tftrgF0Qcz2CM0xXtiQwWYi4w8-ZmP_--Yn3rtsb-FPEp7S9hJqysxonDhDpTlxXn59dz11ODrGliJ0imdiGOYuNVEtnUfAAYOoIEzMTkhroR57DvwuQ2Ho6VLI8bT-u0yhiHtztkzlFlu6ILAUbsHxAlPdPaOBXKsTKLV-ntdKQWXfYmYHJnJ7N_q8Qv7jwcpvbLzw9z4LSEnt58XhtDqLaBnneXYf3xkgn6uFM-v7o-o_ZIRkB4wveD6e1WIT4hLbiFTV-wqpTay8MiJg4w0fdCYHRJYOE35lly0VpIlipbb7gd1ldg3yLq5DMCX5ABoJtVg6SAK37Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=EEF2ZKkN5tftrgF0Qcz2CM0xXtiQwWYi4w8-ZmP_--Yn3rtsb-FPEp7S9hJqysxonDhDpTlxXn59dz11ODrGliJ0imdiGOYuNVEtnUfAAYOoIEzMTkhroR57DvwuQ2Ho6VLI8bT-u0yhiHtztkzlFlu6ILAUbsHxAlPdPaOBXKsTKLV-ntdKQWXfYmYHJnJ7N_q8Qv7jwcpvbLzw9z4LSEnt58XhtDqLaBnneXYf3xkgn6uFM-v7o-o_ZIRkB4wveD6e1WIT4hLbiFTV-wqpTay8MiJg4w0fdCYHRJYOE35lly0VpIlipbb7gd1ldg3yLq5DMCX5ABoJtVg6SAK37Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
پیرس مورگان، مجری معروف تلویزیونی انگلیس، بعد از باخت آرژانتین به اسپانیا تو فینال جام جهانی ۲۰۲۶، دوباره رفت سراغ انتقاد از لیونل مسی.
گفت: مسی فوراً دوید سمت داور، مثل یه بچه مدرسه‌ای که می‌خواد یکی رو لو بده، تا باعث اخراجش بشه. به نظرم این واقعاً چندش‌آور بود.
این‌همه از «سن‌لئو» حرف می‌زنن؛ همون کسی که می‌گن قراره بهترین بازیکن تاریخ فوتبال باشه. ولی توی فینال کاملاً محو شده بود؛ انقدر که اصلاً حس نکردم توی زمین حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101764" target="_blank">📅 13:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cud950givDUaHcpKxoWrbilEuhPwYm7f0mY8cq4QnBWxgco9a4Zz5qrbbfLkXaiKuXRud-wNHfQl5O72KJgcd21jPD2v3-VAn6O3U5_KhLY3ZuDGL3_Q6cfbfFjA4dLUzn8BOfiXK4tJy2ajTtNpoyjLRFzVLjkuwdjsLj13P-Jdy1UpIfMvASvNKJUIjpz3x02A0s-YZ2nJkllFrbgdrVOT5lmflaFwyL5GK6TyIPl7daGmg8Ul8Tg42AYjC0oPWZ1TAHLda6a_Rp7QOnrWflkhRZzrjRGICSrOTsG1iUhVs0RJf8IbYFeUFzHAaLSsSvXdulq5p2IGxVaVA4niXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=fDYfXQDw_c5-A0ztqsN96lZUkRT9pCfPWgNdvzyew7b6V_ATeeK8eJ6tmeFZuLigqxgCXQJDPDLE1HxMD3manmr4xiNWg_RCvesl8EdcZYFbCbylp3-L_XiWj57jhyiYxdSTTZmumHdt_pm5Kj7BuhexjExVhjWSkaAKjki1ZX9kF3yYnAZN6htg6dIfZEN73uQXUwl6PdCiCnQi_MP8PJbZFQbcvAJ7QZI5jQMEanUJHPzoK2t6itxEgAoom-YylCM-j_EZUdyQYWUirrd5LKZWi7hE133YAX_a-ku7u_K0tBdSEwyZ2pMPsmbSSSqnTWTdBROgI18jksUux_hb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=fDYfXQDw_c5-A0ztqsN96lZUkRT9pCfPWgNdvzyew7b6V_ATeeK8eJ6tmeFZuLigqxgCXQJDPDLE1HxMD3manmr4xiNWg_RCvesl8EdcZYFbCbylp3-L_XiWj57jhyiYxdSTTZmumHdt_pm5Kj7BuhexjExVhjWSkaAKjki1ZX9kF3yYnAZN6htg6dIfZEN73uQXUwl6PdCiCnQi_MP8PJbZFQbcvAJ7QZI5jQMEanUJHPzoK2t6itxEgAoom-YylCM-j_EZUdyQYWUirrd5LKZWi7hE133YAX_a-ku7u_K0tBdSEwyZ2pMPsmbSSSqnTWTdBROgI18jksUux_hb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=BXbFy_KaL64jihlc_eD7y7glVKTpjBixHdRi-0lhg7T5yYTtRrwfSjyDqWw1JErJWwIomI89guRUVVR94XaEXNoUTJ7_N3IlQxFyyS7mg0bdrVvVKq9InoYhpLKbh-WGkKvYYCcICKLzFlnffOzUcKKdicCde7qJsj-VFz4LqvEuBpOLANv6t_dX6JwcUCduzdxvSHaALup3DDAvBelqj7bbPkg7GmoLIl9ca8eYLptYviDwNbvEtLlukylwuj9XjkieMegBBbEo6XZbimOYDLXYq3ZSx2fWUw2pV77ROYl6_HC2dhs5j2Wz6iASZAGHiU4gzW03eS7-aCMjcxjC6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=BXbFy_KaL64jihlc_eD7y7glVKTpjBixHdRi-0lhg7T5yYTtRrwfSjyDqWw1JErJWwIomI89guRUVVR94XaEXNoUTJ7_N3IlQxFyyS7mg0bdrVvVKq9InoYhpLKbh-WGkKvYYCcICKLzFlnffOzUcKKdicCde7qJsj-VFz4LqvEuBpOLANv6t_dX6JwcUCduzdxvSHaALup3DDAvBelqj7bbPkg7GmoLIl9ca8eYLptYviDwNbvEtLlukylwuj9XjkieMegBBbEo6XZbimOYDLXYq3ZSx2fWUw2pV77ROYl6_HC2dhs5j2Wz6iASZAGHiU4gzW03eS7-aCMjcxjC6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=o3oaRttgRbdosiSUNFOsONvr-65y9jpLaP-xS5VZ36EHnXNgc9aCymj-Efq5wBvQImQb0HlStHU9YqWahlyAMYYbkbY0mWsKKqwPUPs64qQXFHkzfUdon-Q_I3B86QnuMpulrhUVfbuW6l8jjhmSdXY2P84qidOtIb0ZBnnyPGvtMx4xUjACxDETRYwp7I5diKsaJNSgkmcAvi4lN56ZSxqPOykweyXzMRJOt8dpMcCHUehqzvoS_rd93MMeEnriQIcEASU83xCxHxwTEVP_0cbdvpRZc1PypCGZGr53gbV4A7v7w03p8aJ6wSqoaJFJw7cmvpfSUQ-LCrwbFcV234i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=o3oaRttgRbdosiSUNFOsONvr-65y9jpLaP-xS5VZ36EHnXNgc9aCymj-Efq5wBvQImQb0HlStHU9YqWahlyAMYYbkbY0mWsKKqwPUPs64qQXFHkzfUdon-Q_I3B86QnuMpulrhUVfbuW6l8jjhmSdXY2P84qidOtIb0ZBnnyPGvtMx4xUjACxDETRYwp7I5diKsaJNSgkmcAvi4lN56ZSxqPOykweyXzMRJOt8dpMcCHUehqzvoS_rd93MMeEnriQIcEASU83xCxHxwTEVP_0cbdvpRZc1PypCGZGr53gbV4A7v7w03p8aJ6wSqoaJFJw7cmvpfSUQ-LCrwbFcV234i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-gTVmg6iUeYnV5NhGXlg5cUQGHyIGOxJkgGrbLy61pNMgo0pWJC7chqQI2WaofkUWum1qj04M7CKAnmd2Ra5GaBmNUaQw234DHYk7RxrwhoEm0nQXaZpHNA3WALjkVTl3iU2MtjFmblkxiOKdLrLQegf73GKrqUUX3LBqk1_jEdIilfsVShuCdZGGtLVPuH3pT_kkhe3ByVSsJTPusnrdwTDIyVReFMua9d_PqMnRAWhLOneUZdbJqwCPxxYVOY7ld5VHLEEjQk1iFVq4kvH_9Z3dE0MyYXN5GODCy_F83fQSXdwtlEJzMVszkqY7vj9GgRTrPIm-QCpKMXp18pAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjY7MgoX5qKhONGoHjI1701jEOjGE6MqqA48ZZyVnKcuMhmUI8sL2SSCUP8mcaM_8l_08CM9ClFI4E8pSCp4_BO2AQOSHdojWbUwOPN1oMRuqEyHYwRFiW9-xFzoNejyxIkCQ0oei0TieWPNoGokEmPKRrTiYngwry6DhvEZDqfdkC7l-Q_sTN5ZKraMRS022bqEj-TmiH-E7f5uMDqyfiYWfDTpP_aobItoDe-628EIp0_HbMTCjLgkCHyAk5SmKvh9UWP2mDf7cJEMf4hsi0WcjGBCN8dxmxdxOGoj9_JJvb6RpDJ9N1Y8rgy8kh889ToB9-8Q_C1fyXXrQXBohQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Adp-svl2jQvJDNDb3E9-C7Ws4JquA7p_u1uQeBjy8rqgCV_94G6rIvQL6ByV8X4ys5ecasGE95wx1ptSzJGT248N9ES-1VGuUZniVFQCdXeMXOc0nZgayokvUYkJ4MZflTvLCb_TVsZvAHh4COkuDl5q-YaqA5IG3i75dlNxuWJt4er73edIxvD8eY_wEOafvvnMLjcihzYfyT2o8ncmA7G2y7pfFZVhH280n78bMD6bV0cS6gG7MlD8fGWzam94YYQ2n5Z0wajqFFCSwc8IRwj2pkuWqHfzxfrvxPNDylHAZHPaeargdRQml4_NzcJQ_pEyxnoQq4Yg8EMA4oZ5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=Adp-svl2jQvJDNDb3E9-C7Ws4JquA7p_u1uQeBjy8rqgCV_94G6rIvQL6ByV8X4ys5ecasGE95wx1ptSzJGT248N9ES-1VGuUZniVFQCdXeMXOc0nZgayokvUYkJ4MZflTvLCb_TVsZvAHh4COkuDl5q-YaqA5IG3i75dlNxuWJt4er73edIxvD8eY_wEOafvvnMLjcihzYfyT2o8ncmA7G2y7pfFZVhH280n78bMD6bV0cS6gG7MlD8fGWzam94YYQ2n5Z0wajqFFCSwc8IRwj2pkuWqHfzxfrvxPNDylHAZHPaeargdRQml4_NzcJQ_pEyxnoQq4Yg8EMA4oZ5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=iwg-MUpaRyqU7Bd1-eIFsF7PeMN_Q-T1Eb9GlJ8BME4fxS96zVbJnyFWhrTi55JiIcAW7EGAmK1IZmtZvTEC4XBV-fs9jxGY1VbWGdT6bHoazSThZuVTo1Qm05h9UdJF9AxfJoHIuliaW-vr1COyeFxKHGpo9nbAQgWcoAjXY2QOnyP2TlzUH-Pkv3vBTmKa0kGAY7XkGUEICv6gCxYPLn0CuCSko5F9SOfxT9U_JovV2bFcJGaG5qKYVZzlsuRMiOBN9D1YWUyWhGmd_ggzH5E5STMKs_msH-3qvuoA3RGQg4vIcb0bzrGzQ8o1QYJoKstZJGIjpdGvQnE8g6JfRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=iwg-MUpaRyqU7Bd1-eIFsF7PeMN_Q-T1Eb9GlJ8BME4fxS96zVbJnyFWhrTi55JiIcAW7EGAmK1IZmtZvTEC4XBV-fs9jxGY1VbWGdT6bHoazSThZuVTo1Qm05h9UdJF9AxfJoHIuliaW-vr1COyeFxKHGpo9nbAQgWcoAjXY2QOnyP2TlzUH-Pkv3vBTmKa0kGAY7XkGUEICv6gCxYPLn0CuCSko5F9SOfxT9U_JovV2bFcJGaG5qKYVZzlsuRMiOBN9D1YWUyWhGmd_ggzH5E5STMKs_msH-3qvuoA3RGQg4vIcb0bzrGzQ8o1QYJoKstZJGIjpdGvQnE8g6JfRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPWuJRV4sqn0xrK4f4aUZfEyIkfTtOrwBTDojsxtlsaIOlymFo4EChP7dSRVPCyj-1UHDb-46LSPlb3qiwBwya8mAnmfz0Jhor1omin8azCYODBjBYzBSniVxur1HdBE2os4-AFN456FNFdGzutlBWxul6KuT71gsdraoKs9HdnPSulQKhl3b32EKaKm5860DiE8OPMidc0lUE2AbNL4AVGYBtpfgvIK9Rnm_5-_ET1HpGtMBEqkY-49mZetW15n9Q9K17LR9NmUN1Z5n5-XneqZndQe0vHPL8ePR7RV25OAG41VLVunk5RbnvLPnczzTe8-iAcGjTygsaVz3qYuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=mJYi4Z8WNX7iyS0thoU5lyBcvRo7HMdO0lA77MnY0nH70wFFe4z6UxbzKaEOlIGRQxrcAZMej1k7Q3AJS3jz9NpJuKlm61s0iu7NrqS2etC9Dat256ElFFQnxn6YfxsjrzemLzXbCHm311F0GCf-I0vQMSJV4BFvPr84lIzIhXGNkiuEX-W2mmpWTot3ae4uqQKP5NOFk-q4QDbLh_wl_IcHmQjvzcdyuC8wu6dgZcO9ZymfyowhJIpF-M2bhgx9u9lKl74cp3Gum_oeMHP_bZ8YUrWBRrpG4AfQewdqGMxjk4cWjYz1jjDmzCsvTXN-_wmhtVgkghr4Nte51jpYDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=mJYi4Z8WNX7iyS0thoU5lyBcvRo7HMdO0lA77MnY0nH70wFFe4z6UxbzKaEOlIGRQxrcAZMej1k7Q3AJS3jz9NpJuKlm61s0iu7NrqS2etC9Dat256ElFFQnxn6YfxsjrzemLzXbCHm311F0GCf-I0vQMSJV4BFvPr84lIzIhXGNkiuEX-W2mmpWTot3ae4uqQKP5NOFk-q4QDbLh_wl_IcHmQjvzcdyuC8wu6dgZcO9ZymfyowhJIpF-M2bhgx9u9lKl74cp3Gum_oeMHP_bZ8YUrWBRrpG4AfQewdqGMxjk4cWjYz1jjDmzCsvTXN-_wmhtVgkghr4Nte51jpYDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APVUWB7-a8f0K7Hl9CuGLjU_ISvJ-YIytNiAjNv10MzVyNJylvcAGnAo9d_3fq4zcaAyYZicbNkwPyrcG1JjuGzoF8VebOR-UW63InkYovlqpQPHvy4C_l7Wjh57EIUPbOYhPIlytRFOd9QkXzY1NE6n5X0dOs3p_HKoHD3qHjIFSAmTtp16HrkFT20VK6BGDPpEFGVRQROc-SIjxVCQ5B2DxWtUp3x1IsBBpP3527xScz7ZKbcBTaytyun2AU65W3bmpqW8iwMidIPzipQE7OZgkTsAi0IbNgjilNN95j1DTqjQHplgkzqOtSIEm4dQ-mJpLa_rxVZmOehLrLRvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgoLdFpU7KBEDMksPe2lZ4uzy9e3h3XJfc8h244hrB792Bmv3bu3Hz9Evx0enXmYepURelI-ks9wfBKS2SUsCYPiMajjMdDPapaBQQ7m435Fmi7aAs3EgP-DBsP6XyODgmPdtteA74tzSntWTqChpsY9mtmCUdRXJ9gxa5iQ77Albm85ymS8XcHvmNvNp5cDn37LDnf4dKU1wegVV0epvZ4bJMhqYmqg5PvMz05gD9qFYXqYOMqfcsOLDzCf-tqXvAytRAfBfWA94avpwOKZmEP-lW3m685Q34w7eglGwz3vxOq5_oVhYP9BdWNKb4txOFwR_eZs3z6a7qimM4slPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UA9gYGaOStPbbnubxkUVvdZYz55dllTz4mPDCGYXJCCsvL5IUNSZNYQ0KJHNlTvb_4t9rF4O2xbMHcKKKczmP1JOLRavct92oM48Io5F0kaedYI6LIHKDijSmBvSeGjtAMGwR8txMslgZ8Xyx2dgtCnFFjQHnhxyPhkY8nL_onjwlbyAHjE61y431u0XAjV2mHxOA7Xpy9jM14h8Z81TQ7_4OSjLb9JByM7HVJHf53dfy7MhDktTWHUBBryfnIaQmRvFdZVbMIlRxYUD9bZgmmqyRO63urNcAxTW9RGcFz6I2mxTQfP43wPJRNXZUMpqFAw2Ox6kJOS9ytWc0lJeLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVUuGSKFZrw4KHgyI1RN7gmb873eXLfcSsm7nNh-KwJxdJRQLWO5FBm9pE_moudPquAhNDP8yZvGLg5KAXwa0UoEQMz3bRfhTpPEA22Q6cemuvP93lVR73kDw_tDG1nJ_hdFa_2hca_Xt1F-fsEXymuieKThkCpcheCcIhRp9MCBD77O_eq58exxj4mSvS7kD8Tn6_s85xtUq9uoIbLkVaFkKEiZIahpfgaGM6SibUZIqvdfl-KLZ5__xiH_lTvwjza9HL3YUmx-EWG6QdQ1g1Wj3isc64-1CiUUwJbi5AAfx876pFn1Ij1mB5uTyvy1Qyng7roABwQxJRkH2wxIIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqOp-JBsr-iGPggIXMloV2m64I6R_69PC5Bk4oDJr-5FIMrNnQ46OzEJ72z54rxCVVDAezJQ4ddHaiESvMfmOnoKlWyVe9xdFJQLaoNyDN_WPcBnyRsXNmyXmORDmMVbeGSEAtlOD7M7zmLVx0Z9ZXJzic1yYh7rSaF9eDSg_ELRHj--VWDiPmQzQPkCH9nFzRcDh1_Xd2krYZHffNRdDBSB525xRvNLHvwf8IT0CuZgq2mO-OG-WDYAwe_y2_15ndP2kpdY418RPF_RzdUM5ZxVDWuKf88xRjWvQA5tXbPX4rcxnnFoARaD4Z6jB39ai_C-jiKar48twi6vNRUSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZvKdoC-QjR54N0bPQgjaRv3QltvI2U6c5nll2bhT8ci6hnqrMxWVOdCSWy0NkSYAexKyQFGY8Y-N8v3S-89tuRP00oFrZqFcXMIcBU4RLnFUg2wCbx9q9PYuP2fDD5chzPkVXlBTcl-mhXctEtGzU-GrFO4GoG1oibl95hzHyBjc29suUskb5rpIpTbzt6Z9txN8f7QGUfMUWNPDB9PijHq7WbTA2k4KScGOQv65N3jU6yeFFXIN2W22wlbIv42EJLAbLCylS2ikjA7VUw1-VbVJTef3FAhzVbjD5QhIQLbNSJSqzflIHY07otyIiXVMQ7uBFVN1w1Gg7vvfkx49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ElwI3IC--6HsQoeBharFB9cxa4eTFqTRasOQrygldomk4_zpULQyeBbKzGxWvEVyIWR2mspyfK-uekfKv5BXZ0SIL9RW-jJMhLnpxfstvOdNqaXRZtkWd_Bk3PEBIWbh2fbsGneqKyBfGq6cPybcKnVXAiBAbAt0yk2CRHIoE9sZKt0WfJEj0HMdk8es-lyZ08MWLa_2TnbRhF0rYlau58SmFHZIPAvFUiShgl_Q8iAR_y_5CFcNP3I8sEQXVnFDZdIqMd5AnTgs3zOZngxRxR7Q8Z_wfiH6XTtuFop1fZFpBBpar0-MKIcAV7pXAVEFJvWU2peLp1s_6ZanbQtEiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_1jEHiRg35kPH0dkydg31yoQkyUv28xAIGU4xEvMZSGslQLsXlXME9RfGzfogeUpje-MSWgqLzyUr5732qMPvOhTwyjwoFlWz-Pp45FKP_d5SmjHggmIxvczlcj5LKli0sweU86jrZ3Ix5GyyZgbcsml5wE5idGPMQnlrXOBPeRCOfoCojw0Gy7cxpX25GWSM7j2g7kFbqh_dLocZpcTIGlrQy_oosPOWi6CACSs5vjWjI8KeQ2-aam2OwOXv9dEgt6yrhYzZtd96fj9sms4wsePyVRhjKW7p4LWgaBYm0ZZ6pRCP-gLgNEHBn1RKA1tjxKFuTASU5YQ81mlEsbcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=jzcf68CG2noAaCuO_G3AYKar69ATzU3w7qrztPw2y0uWPHM3BG1718v3_HVx53zjgz724BGIGw_siVlbTRmsMU361Dc1GMsMwv_OciGTRO5fD7kORgmJMGqmF2gxG9y3xOu_qXCSjO8tH15Z9VURJLUed1XQsiprlzTzEbWojjFyeffCSYj25kdHNiXl5TazERMY_KolsbqhUiH2qrai2YZ7gQ6dOEEja023rMRIFIVNC5BDnYe2YxmdP_W5SncJ86yCQDYr3khEzkpPNQCbmzx-fs53RFKVYua9v_0U4LU8YoD4wTi1qusFXHYGLKDOlS31scMagq2HS0Vn5enDpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=jzcf68CG2noAaCuO_G3AYKar69ATzU3w7qrztPw2y0uWPHM3BG1718v3_HVx53zjgz724BGIGw_siVlbTRmsMU361Dc1GMsMwv_OciGTRO5fD7kORgmJMGqmF2gxG9y3xOu_qXCSjO8tH15Z9VURJLUed1XQsiprlzTzEbWojjFyeffCSYj25kdHNiXl5TazERMY_KolsbqhUiH2qrai2YZ7gQ6dOEEja023rMRIFIVNC5BDnYe2YxmdP_W5SncJ86yCQDYr3khEzkpPNQCbmzx-fs53RFKVYua9v_0U4LU8YoD4wTi1qusFXHYGLKDOlS31scMagq2HS0Vn5enDpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=DCCTAnvH9ZQdJPGOK2uYDXbsJ2FR5HgjyBZJyd7PEtdZ_eqpT3kqC3syH1taGSjouHFQkdDhR1DqrU95AJsbVr1HMfkaqzZGYMbWsaMqmmG0RUGoIf9WXwL0aRVRwWgQnlIh5WFGfHbnBrY5RAlMBJg-c-iJ1Jy2ZpEA_zXpoHyIR9RLszvCKaRAhu0CcTCxkB-n1gdL04BcA-HXFDvh1l-bv0rpwRSyy-U6QleQDN4yX1YshF-1PCsGCco2PASwnYgkqoEYAMkCW5_kd2yce4NJSHLk5VWbG5SSm7u4othr2KPXnJGuDNl5xdBBb6egVnRuvY-FnJRj3FIhIXAluA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=DCCTAnvH9ZQdJPGOK2uYDXbsJ2FR5HgjyBZJyd7PEtdZ_eqpT3kqC3syH1taGSjouHFQkdDhR1DqrU95AJsbVr1HMfkaqzZGYMbWsaMqmmG0RUGoIf9WXwL0aRVRwWgQnlIh5WFGfHbnBrY5RAlMBJg-c-iJ1Jy2ZpEA_zXpoHyIR9RLszvCKaRAhu0CcTCxkB-n1gdL04BcA-HXFDvh1l-bv0rpwRSyy-U6QleQDN4yX1YshF-1PCsGCco2PASwnYgkqoEYAMkCW5_kd2yce4NJSHLk5VWbG5SSm7u4othr2KPXnJGuDNl5xdBBb6egVnRuvY-FnJRj3FIhIXAluA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlD1aPqtkmSVJQS8ASiuxNjLWB83aDK6Dwyt1aZWjYRSAwuIuApnJFAaG8qz1T5FrNEHb5uppStEsVIEW-1mywHp0tF9EEIOjN3SOcz72iPGmxgJ1D86J5DXfiteJCbWYMkqvUTYXdeo9lxFzScCh0lPrJdHzAhYeyfBP10ECwgBlikYZ5EzavXF5rW3D-4olPZnT7lakSfwPoyZd7fqsrqyGMefW0JIOSsiJK1_IwHrXbQnoTNc3E1IWlsj0QtudGThQiJlQJGVYgL3wenLht1G7He9bf3J9zR2nRHqiTd9Y4huip9-j1PVX5ebp9Baxqg_FxjR_uULaU_Zh_9Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJUnoLmcap9mtSjPI_GrtiWXcYxIisnWrFW8pjVNW9DTFXKnWuVBnZXFTy0SUn0h61lIIsmA_hUdo2aYZLCQ12zpA0kMcm2r7dQOpHfSa2abP2vuCGthM_9rpupHDZbhiCONJsm2879uuuNLkjtXFfOCr_TaFkdpxm5UHjwnsPk4J0Wk4fRg4825ScLKMJDpftE7pFNstxjcK9Ji6mEGN2fRxglqwhvv1aEkRpRwjW9gWVgDQhYTzBtWLaWLZNpj-CDoq1iknZAFcZS1tYjUjYbBfQODKNqryl0kao1ZmhPRt2ij42MCNFHxmD2ATv46G1Zn8Ve5UG3uuhJ-Vb7CWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8B2y1ZamQMOIDexeNFZ3xXh4RnfKxw2fYvEw0w3ODHoAVV5oMgDTR9VT6AB6OA_SL_04CnvIeUC04uPMdC_f8PcANUS7uj1J8E7ArY2zBTToYObjdLoMAgWogn6SNQxOHQJ4m_gbY72PVgZOjUC9mYRePlqAdPjGdwaGw1dJ5eU1uOYvvUEHDbsbNxIt2e7VPkHae3zsLkmnwKFcT9JCDRe-Eh3gdPYB2jUaeUklq9D3DyjBppCPepI6oCbIWGYKCWSgHtTgGGy25wFY0kYJiD18y_iYEw1hrN3xZS1LRxrAZNCW63R4mhIwhBGUzs4H7RbRf5c-6pLOL-BXb8W8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8cEXc_46AuRHqFKlQhYukBy8PG7m9mm7fziq_GvJEZDqD_zbT0d8CJ1IOWtph_5TukCYJxohLLA0CCfXCeDrSyAI7XCoB9idvMsnVREOUOq_BfBq50XAfaQGoyrIoy6y1f9BWStySsqXE-8ZUmqJjcXzeTXTzj_oSzaekDt49LNxjr7ebZjYSwUTZ50sJaQVV7lQRUkGwSodN6OYy1aXC1CT3JE80b8Dg-MmE_VDU7LsrgSlNc-5McPIWbBbgP2T5dC_45ymVIhYf5Gd5oLkVqIkW9Qod_pYixUO3hmiWQHlJj7kMI7w6OP4yD9kZJbkmYFX28XyUcW1yj-QD3USg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhS1sfl9DGQ_RbmTkA6ain8fmUNtF-kxWew4qujyYrM15oTZJhQ3zhN28Wviz8cMhOGCRR0LSv9MTKAx8SfZnY6B8XEsaqaIBWnaV9C9Y1mVE4m4JJxgzoWJlqT0K2QTmzHSsmoA8UsXW_paBf67X3F0WE9roOSm8M4qLkpbWl01760JsgxmyOI-W9u_rLS5lpn8UIi0akNExYiDhAkjradVPAoWHNwgX1QfSjo5791GUgXLXWCHYU3MKxvNjgjzs3d5Kq4L1rqzl_qKOJj2_hFKchFFawGiaARZQupJNB8BboKVBKdNjyOTgC1PGR0aXNFYOR_LshzidYBlYo87-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivl5FQ7E0kdYFMEqRet4KDdpearZ33oleqxIxRfuM_aTd0ybVfxCsdbkBn_bu8M_NZf7GqlXz7E1dbn1v0edKxmBh2WpbGMI4AnxFnCLYzIpyuHGxQOMVSzqPWEBX-BVi5eaSTpPuw-wNn0yRxZN_sLN18UQwHiYAO3YNLFJcwf7fZQHg9zRoIcyK2R68_Ep1CN552SADRcxDZg1YLba9FKrcabKoMR_OYvURg-bAghIXf8vOVZw4yTWov8Z5rDv0uCJDC1DynUoZrBb8_0cbyTMWuFUvG9Nutq6XS61I-bbbtbZTrnyKDS-9015aPt8Dk5-luaYKmxgANP8y7Mleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9DmjNqcfABpS2jxLulzuyITAHcv82YcE9N9QLT7ONBskTA3MLQ5Qt9TiFfW81oDU5S_htJ-PYzE-B7ZfeZFwcFk3-feDcmew_N8PfE6uhQlOncJrjMDtOJ6yzsvA7ruO6_mzt2-tvUyfY3GCGVqol9WokZb_uGOrTYWse3_AO6RTFS8J7Jg2AqTAAnSE0iBBffPb4kCHDx52cHuNNMAtLFRWcE90DxpCpxc08NdnM2q1lULoadxJdyf5rgzNoUhFetOy6nz3iP1JLORiE5-8N7txO5OEej_rKrZfvjVSmnl8z8YdfwLMxQBUUo5Aw2YZOtNgdaEq6BXRgh3VTSaQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvUFXnLvcTl13yF2NBOFyXndpnASCye88-iXNI4ZIV2hczS9erpkWexsuolcdVEWyzvraBr9L4roT7GqDMrG6vERrnQBleqyMwGNOD42S9MjT_zbh-G_iAKCScLaXITBoZ0TGc1xVK92wRar01nvdUXKUOT0FPFzXAZCje0K5s-Ha9GmS73XyzVUwl1JRVNQEjjVwI6aRvGJLcC3rfZvKRYvR-_pNpH8vkiZFJFpGlEgPZDkIishxuvbQwB5boeQOvVEAzVl_XdZWJxuekdgTDTgXbDAn-52htoPRzbeOv-ltddMYWGGPKP39tRJUthwPa9rLR07EbPs88VqZOUlzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=G4zfOhxcEzecBFTVk_H6zFwNlg6B8cXkOjnvFJc9aP0FBA2g5osxJQraDbOdNFpBGiEVvYj9EM4-JRn8l2-6ly2sIeVNhxmwBZuk04x4OONh_4xphl97f616oI3rmS8DuG48ovXJSlJLnC25sC0QcVIrShns4r0u3sRJ4f5rfjV306161AxQOPzSNg8e5rqCahXaFkxQWz8nmFD3n8axMXn4iaLd1xMho-jDISxEiPbwP27kD4yfa1I4kpdDND_KFy1lfzz20fdZ3x92wA_Xbocqc35c-VG6m16xrMd5MlarU14ckoMrYChdVd0wEoRMfUOf148w1Qy7vozaJUlbS2p1f6Zv6eEpqAOD7j_919CW3JN1v5e_2OYmGL7wWtGFgESRbxaP_zxQV6yxCzA524mqO4kWHidwWz4U69mMwYD8maKQeDJ1n76plAVX6Tn07hb-xt9HKYRj_3ekPURx2gKp8tSEL1Zfv_vPItLnya5ILDLezx9qV-FYuleyam1gX0s4bkB6n4gOO5ZX9PXhQcTD-d9SmcLuIw70BgkSdwihrpNfXWa1MstDNjD2RamdLBuJjyRl3vOi8-t9CTy3sbjNCwTggnyjITlc57L7kfIOap0AMY8SWgkMT41Qtyl71V968SxxC76jlQaaZp2NA-I3JA8yQCsUQ6ejE4RrO3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=G4zfOhxcEzecBFTVk_H6zFwNlg6B8cXkOjnvFJc9aP0FBA2g5osxJQraDbOdNFpBGiEVvYj9EM4-JRn8l2-6ly2sIeVNhxmwBZuk04x4OONh_4xphl97f616oI3rmS8DuG48ovXJSlJLnC25sC0QcVIrShns4r0u3sRJ4f5rfjV306161AxQOPzSNg8e5rqCahXaFkxQWz8nmFD3n8axMXn4iaLd1xMho-jDISxEiPbwP27kD4yfa1I4kpdDND_KFy1lfzz20fdZ3x92wA_Xbocqc35c-VG6m16xrMd5MlarU14ckoMrYChdVd0wEoRMfUOf148w1Qy7vozaJUlbS2p1f6Zv6eEpqAOD7j_919CW3JN1v5e_2OYmGL7wWtGFgESRbxaP_zxQV6yxCzA524mqO4kWHidwWz4U69mMwYD8maKQeDJ1n76plAVX6Tn07hb-xt9HKYRj_3ekPURx2gKp8tSEL1Zfv_vPItLnya5ILDLezx9qV-FYuleyam1gX0s4bkB6n4gOO5ZX9PXhQcTD-d9SmcLuIw70BgkSdwihrpNfXWa1MstDNjD2RamdLBuJjyRl3vOi8-t9CTy3sbjNCwTggnyjITlc57L7kfIOap0AMY8SWgkMT41Qtyl71V968SxxC76jlQaaZp2NA-I3JA8yQCsUQ6ejE4RrO3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=E7E13ZQtiSBywV076C105u7IgnBTPIt2vNwR8p0Ya4QkrwWTlrHXdUG9iYLliuSO99Skwc69rA_Z9Eqfrcs8bHibA1pFTKkpaMacAdEjS9dI2ysLAmsHNJrN4LgXzcUHrFzN-dn69ZTWXUl03EG8yw5qOEJZUa3HWSrQRPevr2cFptk_5eUDGvYQPveB0z4fueCgML3_BleYUD8n-RXMUxl-vIy6cbGUtB9pz-UYrbOBxSKHwtAgZrG8ZH6n6uAEBnoyWFIlFy3Ke7-CVh8SN3tQ0aVzNaFibqRNznl8-rwKOscJSELYjurNbfD8A5p7LHFLlcqJOaPZGRXcP5WVVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=E7E13ZQtiSBywV076C105u7IgnBTPIt2vNwR8p0Ya4QkrwWTlrHXdUG9iYLliuSO99Skwc69rA_Z9Eqfrcs8bHibA1pFTKkpaMacAdEjS9dI2ysLAmsHNJrN4LgXzcUHrFzN-dn69ZTWXUl03EG8yw5qOEJZUa3HWSrQRPevr2cFptk_5eUDGvYQPveB0z4fueCgML3_BleYUD8n-RXMUxl-vIy6cbGUtB9pz-UYrbOBxSKHwtAgZrG8ZH6n6uAEBnoyWFIlFy3Ke7-CVh8SN3tQ0aVzNaFibqRNznl8-rwKOscJSELYjurNbfD8A5p7LHFLlcqJOaPZGRXcP5WVVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=tiivGrIP3Md2NUQNPU7Yy3nI-9WWsp1hrjMSCLQrUpoJlJU6WNlPpaLFP-RB2onrINkOvTsMgg5wWJ5zajgAaBKteNESp9BtTew03GII_hiol6ZZhqcerWTthpWx5a-9noi2sqEmMUVKx1HiroCiwdcqKMAXLlIgJXSnCzAYMmSVAETVNqmGmBf3fLzKixucHDqSDqveu-VunYpvPfWyLKMzFb5GKs3Bf7ipzmgpK_SDXbUehsHh2uANIMkMLL5ZRtITDmxy3mvcTyHbtHr1H1iuLM2tfXR0eTGCrjkH2WN0wXflIkj1jQQYiJvzEV7cYMLQakF2rNYh7vChKssFiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=tiivGrIP3Md2NUQNPU7Yy3nI-9WWsp1hrjMSCLQrUpoJlJU6WNlPpaLFP-RB2onrINkOvTsMgg5wWJ5zajgAaBKteNESp9BtTew03GII_hiol6ZZhqcerWTthpWx5a-9noi2sqEmMUVKx1HiroCiwdcqKMAXLlIgJXSnCzAYMmSVAETVNqmGmBf3fLzKixucHDqSDqveu-VunYpvPfWyLKMzFb5GKs3Bf7ipzmgpK_SDXbUehsHh2uANIMkMLL5ZRtITDmxy3mvcTyHbtHr1H1iuLM2tfXR0eTGCrjkH2WN0wXflIkj1jQQYiJvzEV7cYMLQakF2rNYh7vChKssFiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5id0wswk6jiLk0nKxUftkYw6bR79g2-NGlzpqsShIRY3AoHej49GMeDga8WvtvdWUgpiqS_AWWGZnoavbhjFoMFq86EjI_8QegPS01HArgKgN7OdYQI6C34AJkm4RX04-46PzYUC9XwYKQm_db9ucgm-bJo9wX1VmhZJk1Mm3n_Yu1Wg3_siucjqqLU6Mfid80f1WuhGPUhXbDhsnWvK9H6j13kDA4cIHZ231BiUNNmzd7iqo3NjdEntsyXHB-6Vn_lRPcUSO4EhlDFbvNN-NNmsB49XI9PZLn73TIdXcFJw7qiY-S-7yPonLc4yVhO9SDbXa2YtYAnTsEZy4FW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUEB3m7MZZtnnvIqQarluWZJNclCYN05mtPIYpnhZpTR9hUoBXbnRSU1etSozUf5QKtqYg9q2a-7xLqdKqNNxWlINpB8Xec8f2vQfIX202oBA3at0tDohbYrO0UtgE33QZ2VNRz75s9pYYJuhSGANY65bQsAe_GMbOQ1rtaGdEC6Q_QLmaOZZvB8UHrZ69MxGjb_NQsoFr8XCyWZxHAIeoLJh2J4N4dewxgOnc10vn7rZwkmc_F03h3h3eEaTWirU7d0ba4xw7nYDbTG6BDcq1K2r4q1u7EmgcokHx5IAPFS9k_z6-U8KPp2LGoJzq5BTwK3UQ0HveosuyKTy3mi8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv4QugNNqE89stlFOYG8pyRi3F7dyFz0libJ2DYpfxqzTJ2D_Gwp_yLnQVHIOunt-5Ey6y2OVjnOz5JYXDF5dpJSIrKDxxOuF1o4bhswayPVw48q9ND373JWye-HGgTsWdV-82BW_K3ZJk1F3sltSmAp12AowFxB28MPorw3ym-XWnzZpXn4X97nZK800GiGNADWXJuf7o92bwAZgh5htAF-opvNJo6dmq5RWFXmJJS2dJ53_lFxqRMi8jD9sU5kpL5EtuQ-XtFTPaAi31VXx8-97WHz8ar-FQi1jU9U7UEq0IsBuLbd3wFlOzjNVBEMXGDdEb7LEvckPvJ7R1OYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6VxNYA5YwKXQ1-FQKLyGf_ZG8PYmOEdn_KxJjSHreHO5U0XtRb2b7AEufhqwXJu2nV0HfjdawKmCpHmf8TXPgqimO4jDbeafEQZpfpd4LCG7Cj2ltzVW1PfaVhSLPr12uGMSbYMA6rZmA1iZHOsn4yFUS66LtrCHWCHK-Dfism90gK-0vb2I2IWM_OiJmKaoM6NprazfEqFjlHCQp8t3QFRbkDomJkVThKqn9xas6QgvmuBwEzBFLqvA_q15WrYz-zKjmHxR7E_-zMnBAwzJ6sulOVHV5i0RnkVP9yP5DG2wKFJz_6W_fIyKxQa6_P2UIbcwt7TmPEQGAqvvmoNeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7o43_sMYmwLUZeN2lKAzU2LtfLHfX0s81Xq5GLOfZh7f6rySaMPHpv4CeuTShHy7-vdFfsfBAsTh8gBFrU8vx63rLMV0vBdK8p4gkyfLEfUGYom0sPKUlDTdUi6SiGuD86Z1Arp7sKdcfxQ7zWhgzAvfxplX-mNlWs5-5vnH-Vg-6ps-PxwcH12G36x-nb6W17GWIHKolLzjGVm5HIN_hKE_NKGg5HrjPvFOC30CcHTk3hISlLpeusTZPrwnXHH217aOPsj8KbULLVW1nUPtZwN92Iuiu2hL5ZmyRBmpYCqEPTXPnNT2F-RpscUJc3jopwwHu0glYrlKjpj051sfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCd7BV8SseZCJM__So5O3Kxbcdwc0I4zO42vTa6FxQyqXyWz3eibMMh1UYm1vBglNDFa_HAsFNnyIgvevoFnmrxDhac_JlDU8bhfrDjOOIMkKuqw7I_k3M31KoyQhfKsGXkdDVD2392c5vAax9Rdo7zb4D2qFG7WVrNTuQGl5e03HyocfDkecNSKJU98y0lUlR4ukbwLe4nOf_zcC2z9LfgEzKVuHRqDmDgpYWCDSbZCvEpw-AQTFo-E42h3GAKh5hfcFADHZMNrnXJ_HE93ZT4FXyY_I63l3AQx5PJ-07lHvwgyLAadhjnr9Mm846jzv3ke9EUMzXInR5e90HwqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKjGyfvz6-874Tm5UtKNFN9XUlPSpS1J9ZdN4on-b0VIUSzCvfEd-UtLEPUuKIn-3xSp6FtrSKbFF9i1np8ytmrmdnG7C8NfAzrkPKfmAGj2yRFItygRItg-ecy8aTbNpAF7y5kzYoob1aqjOZ1IrN2Cv7wv31jEDWppWINDp8rW9CrAjlBafDVD01uurzLzxCxwLDnt4c0AiFh0aMaEOyJdKyfbzR3bDTPY942pRR3wr5o9vtrOimxV71vONwcQneJVs95hOvyCQ8FfaCVFuSQBNvlzekYSK6FggtaPzpEp0woxRajHYJou9Pl6_XRLwpSO4eUbT7AuF6sZahHNHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsSb45ZwGOO0mLppa0pmZBx1zKmCuJMfyQrnKUJl4xUPnX80AmCfLhs9hO1Ft__GYxhA8EEhdwtYVcnIr1IM6s9ap9Nm1tz-hAxt1mPrefchtF43E9xwgLV_QQz3mQcHDlt_vRFc9uZLLcr_ujq-Rf1Q0etGuGSxpz8wCXJTNH2eY3ZTN41a28xofKomzDrkEYDsIcO6t3ywx-TIFMTgkaZ-kZxqCJb7RaiN70059cDE0VtlapcelGCVQ_L3yMtaHVTczL8NgQ1USRrBkjJ1sIbfl1a19_s5GI5K05KsiRDjM2NtUkXdyHTVdBU8VMoMD-7TsiPbziXfvGcY653cxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101722">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=BsKWBGZWPwzMjnFyR6N5Qbuphi1k60Jq9aUG1VYugTWW1RWpxtbM3ZNFZmAV4IUKF1QhXxcq9h92Czaj_H5YfF-Iqk06en18DU31daIgfgE_J3OMkw-KiQxeiH-XcQXb8IQ1WVvlS4KJrVEw4o4UtGWAKeuJD5GCWhjYEZczwwAy2z-Z4TL_5DuGyJ9PIztNB97LBudGcnaKMjRLnBuUhbCPC2j3OizuROx2Q2AwpxKa9l1gsK7LMZ9ew5EUD8CRSyo93Q7vZ2xHCgNUcn89bq8ZQvmvDyBoOytdHd-Wff3hpRTYMwzxVdORSvMNa5zF9zrCoaxETvadjCLzfV1IxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=BsKWBGZWPwzMjnFyR6N5Qbuphi1k60Jq9aUG1VYugTWW1RWpxtbM3ZNFZmAV4IUKF1QhXxcq9h92Czaj_H5YfF-Iqk06en18DU31daIgfgE_J3OMkw-KiQxeiH-XcQXb8IQ1WVvlS4KJrVEw4o4UtGWAKeuJD5GCWhjYEZczwwAy2z-Z4TL_5DuGyJ9PIztNB97LBudGcnaKMjRLnBuUhbCPC2j3OizuROx2Q2AwpxKa9l1gsK7LMZ9ew5EUD8CRSyo93Q7vZ2xHCgNUcn89bq8ZQvmvDyBoOytdHd-Wff3hpRTYMwzxVdORSvMNa5zF9zrCoaxETvadjCLzfV1IxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101722" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101721">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=q01lE98ANjWhjkc42dwxJYgGIxCFyFuwc0u5WNbDAgBNdF1vkCTX2Z1cemITpvb76TwZI0oRwSZhDmP8ygPBt1KWGc7LyA_Z6NP4pXvrQtrBToAFKiWHWayeX6ZPPRzEONiwO0JtwEsQDkcJUVHC3KQDfW2_5qxUSwamfYkLBZvZEUzSOAhvYsAoTa2ap_X2roDqUXdhUSVCSgiIXgqqKJbFMwGZTRzkuqEETcTu5FVzQ3V-QtxGQjDnlAuPzswYelUiQdJQVBf__yTs4F3h5fAzoEihDJaP5wQ6-AmQzWyxKazc4wPMrKasT6nefQ11Nx3nNGikFfTcjIp00vA5M5D7BGH75SNO3u27_gjrwmpO9GTXUyO4IhSXgRz8Y8v7CXd3BRsXeCL_f5BtO2kZGHhRkLBj8bPlTwr491FtmPMVJs0w_-Sp95siVcoizKUd9wRiX8b0nIL0ANJJN7IF81LscItmvy7iB99-bY4kpLvoXXJ4lvA8EWTtNyH0zLtNW78TrYxiQrpsm6obsLSFIWLMCvfNpiulfzZWKOQDZqT82MuLLq8ovfY8pdsEAC4r1YjdsmPGgKKi764flMOizbim1eII49MK59XYGrHDvDDM1EAvCNDCW0UwltO9-OAJrI8MfrD5tNVjAw1KXvwmGD4stCQyrT4B2Bdl9VhgBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=q01lE98ANjWhjkc42dwxJYgGIxCFyFuwc0u5WNbDAgBNdF1vkCTX2Z1cemITpvb76TwZI0oRwSZhDmP8ygPBt1KWGc7LyA_Z6NP4pXvrQtrBToAFKiWHWayeX6ZPPRzEONiwO0JtwEsQDkcJUVHC3KQDfW2_5qxUSwamfYkLBZvZEUzSOAhvYsAoTa2ap_X2roDqUXdhUSVCSgiIXgqqKJbFMwGZTRzkuqEETcTu5FVzQ3V-QtxGQjDnlAuPzswYelUiQdJQVBf__yTs4F3h5fAzoEihDJaP5wQ6-AmQzWyxKazc4wPMrKasT6nefQ11Nx3nNGikFfTcjIp00vA5M5D7BGH75SNO3u27_gjrwmpO9GTXUyO4IhSXgRz8Y8v7CXd3BRsXeCL_f5BtO2kZGHhRkLBj8bPlTwr491FtmPMVJs0w_-Sp95siVcoizKUd9wRiX8b0nIL0ANJJN7IF81LscItmvy7iB99-bY4kpLvoXXJ4lvA8EWTtNyH0zLtNW78TrYxiQrpsm6obsLSFIWLMCvfNpiulfzZWKOQDZqT82MuLLq8ovfY8pdsEAC4r1YjdsmPGgKKi764flMOizbim1eII49MK59XYGrHDvDDM1EAvCNDCW0UwltO9-OAJrI8MfrD5tNVjAw1KXvwmGD4stCQyrT4B2Bdl9VhgBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو جدید از حملات سنگین به اهواز
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101721" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101720">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=o-vo0xL1Dx1eHe3aascFhzJVTVgLV9A8wzm83GiazkKAXPrTvu3RvdwA5mhEmmC1PpUrjYJ9-yh6svw6Tw0XfpbrISKyfzzL-KGeCXas7eEfEeyBr-42zzUgU_Sn4OKDedhN0yP18IGKSsPQscy2vCSpIhn31c8SZ3eYrmV5i4pH8NojCZRcJha_4Pvs50zL7sGNyoy8clJXJZ4HB4EpbuHX-S0SQ55jpB3pfGZ-R-B4FkBsxKGomXcOSojGvjbXtoW28L9DW1nYXLFEKop7qMrhtFE2oykm9ZLtYShKsOTSwMa-rfiv7E83BFopoNtMRyGt1Y7GPikFyVNwsfEwrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=o-vo0xL1Dx1eHe3aascFhzJVTVgLV9A8wzm83GiazkKAXPrTvu3RvdwA5mhEmmC1PpUrjYJ9-yh6svw6Tw0XfpbrISKyfzzL-KGeCXas7eEfEeyBr-42zzUgU_Sn4OKDedhN0yP18IGKSsPQscy2vCSpIhn31c8SZ3eYrmV5i4pH8NojCZRcJha_4Pvs50zL7sGNyoy8clJXJZ4HB4EpbuHX-S0SQ55jpB3pfGZ-R-B4FkBsxKGomXcOSojGvjbXtoW28L9DW1nYXLFEKop7qMrhtFE2oykm9ZLtYShKsOTSwMa-rfiv7E83BFopoNtMRyGt1Y7GPikFyVNwsfEwrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پشماممممم صدای انفجار اهواز بشنویدددد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101720" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101719" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101718">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=SLufMYG-peFZvns8oRKLF_reYPpf2sfa3ZVv2H1qVn6FSUWI_dRwVU4XSyyWKwG8jIP-g5_qE1pQjgf38fyVosGUUXs4Csv2VNXRL7rcr7uKn_kOMwQv3Mh2oNOM-fuRwoBEKdwn7flwPRyGdDYGcJo5Ta_lSbp9Vsd-GdsSLhmN-As7oHb8DfcEOZl8apu4Quvct26u_JXCgbiMhdYcyYmGo0MSUbssyPFqRxbBmPe79dHZb4OyEfndJYuOf7MGIDzmDlyxr2uAqNkdOcDMGBFUaEyHbf8yXJ6Zok_SidA8yI2FShoEjNs_c94FmpiTh9rG80PHxCRuOFySNcRaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=SLufMYG-peFZvns8oRKLF_reYPpf2sfa3ZVv2H1qVn6FSUWI_dRwVU4XSyyWKwG8jIP-g5_qE1pQjgf38fyVosGUUXs4Csv2VNXRL7rcr7uKn_kOMwQv3Mh2oNOM-fuRwoBEKdwn7flwPRyGdDYGcJo5Ta_lSbp9Vsd-GdsSLhmN-As7oHb8DfcEOZl8apu4Quvct26u_JXCgbiMhdYcyYmGo0MSUbssyPFqRxbBmPe79dHZb4OyEfndJYuOf7MGIDzmDlyxr2uAqNkdOcDMGBFUaEyHbf8yXJ6Zok_SidA8yI2FShoEjNs_c94FmpiTh9rG80PHxCRuOFySNcRaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101718" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101717">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds100D_58uCuMrMvwD-feA-bYBRELAoP-Y3waEsXKl_5iG4qwqShRvvihzaw6-O9nwT-jHwidXY8iFPCRAbfeOpQ539JKauIinKsvE5s-GPVj-wXLuQp1dloGrJLIQfhHHZtZjz6rp1ttYR5-HqCJ9JH34ipisJFh9ux-CvFol_Xj3U_r-HIWTFe8-yAgf82IYN0RGdh2bzYn2rxc0TP0li9R8eb07a8Xa7YztSzVSHnJKBn1MiumL8xIDBAoZ5LH8NPB1-UUshx5HzIjCzH1REeQlaQfTMYgUOk2Sw7dMD-C0-1MeGzZB3OD5H71d7-fd7aYs3mT2VLtXClfD6UBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✅
کریم‌آدیمی ستاره بارسلونا و خانواده‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101717" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101716">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=kBEfEyRENw6f_CE_ZIjmAvAMq65FHAiIfpxZSr5MeZQ2ye09HFxPnbS9-jEz0hmAEWFftqzMbsrQuEwoIhjypFu4KGJPg5qXzSy9ET7TZgwRFyyoN0bB-TiXiG9WY_AJuYy6P-wOQrE4teUOtPtZfozveiXkyz_-2ehR3__b3nn_FTqeHMD7d23S29EDq0Quhy50dH4QZ8aXP8foImN0b9QqAVmi5CilUfSczJ3koCLF7cK_C8TRfr7ibbMRNv6ceT8Qd8rFHsxMJieYoEwr3B7Dfty2vTEc2-iNeSfpIOLpEbmZYVxlN3E-vGujDDvIEd3Yl5Nqee5KMX0xq5Zeug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=kBEfEyRENw6f_CE_ZIjmAvAMq65FHAiIfpxZSr5MeZQ2ye09HFxPnbS9-jEz0hmAEWFftqzMbsrQuEwoIhjypFu4KGJPg5qXzSy9ET7TZgwRFyyoN0bB-TiXiG9WY_AJuYy6P-wOQrE4teUOtPtZfozveiXkyz_-2ehR3__b3nn_FTqeHMD7d23S29EDq0Quhy50dH4QZ8aXP8foImN0b9QqAVmi5CilUfSczJ3koCLF7cK_C8TRfr7ibbMRNv6ceT8Qd8rFHsxMJieYoEwr3B7Dfty2vTEc2-iNeSfpIOLpEbmZYVxlN3E-vGujDDvIEd3Yl5Nqee5KMX0xq5Zeug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت تلخ کودکان در‌ جنوب کشور‌ بدلیل قطعی مکرر و گسترده برق...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101716" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101715">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etqcU97ykAHNM9Oy1xBjXbaSknv2xAQvgpWFepBqr9csA3BU0gAaaAN41Bf5mRV5nHc8pfawe7c42j48xd_0Gh6sI7Mq_ptwk1u7viFNiexCX0iD5g0L3wvUIVjLtZWKukGRWql4nmmBo6OGO-nIyyAn_nvGMIUFGFvMGnsmI37-NlyVwnnF3O0EpD08FhF2f-CzrAdZrlaMV9AJ-VmptXYYnk3twKSro0_AlZCqQNQI5ZDLPb8g8F_rkOOJeZ9BUyAzR9xV_MwYjhz8bj6_o4es2pWnQxOIx2X8kgKOuvgOfQ2DOxdoapUkQ5RO3Aahom1wk2hA7l41WmdglqMXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
اوتامندی رسما از مسابقات ملی برای آرژانتین خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101715" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101714">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oawLSRQgrfpE2WDKaWNeClefPI_tLwHhBfy02bJ_oEDWRuu0oWv97D1r-yGNXFaNe9wY2FUiQqTa4UlLKpm6iInBuvzb1lRA47fgZ86Z2OLDfUo9jWIOcIxCI7uOcKkVbxvGyrqCE7Nq5agQ0-6dJYFFR7Ym8p-JCJ_8wPp6k-iVnTtbjI4Q9rY5WSsnLSb68MTe-kTfHJkErXhMrC2SgMcydd8mUib1ClM3_VD3beSy7if3l9pAKpHVzjVQXzk3g4jiTYP3d2XYDsc2OYeJ5_2SNY5-I8BCThfHlGr-t9XU6uuAtxUVftyvR4NX-qVDnymg78ioVz9Peohlk2w_dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101714" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=DltuCLgKwAw5tuFVxsq45wLo0rbQ18cqVK3S8Y5W8Mo3eicBVDt7iDg9bFLJQLJWPsp6VG-GTj9F6pBUarU4pJxQQ-ZGs3Km1cF1BdAzjkNop-_wHmfuXe7NsVYi5uDgMDeon7OaZ6q8KtIspYp8ETc_0BkIwq56OEMHeeqmnI8dKP3_Qdp4gVvshuvsvI9cHF4HUKQqfG4Mcx8we2Wch_RyBqEFFXPtjy9MIqZKLRlRduc6CkpP1Web1GmBKGQFL8d4XOxQSFHQH8K3PYSDmlYCInEvNThel6kgkmGRVBHWkTKF0s2MyVNCyHTe7IbKY9nH9Q3vWu-1vdMYqi3A3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=DltuCLgKwAw5tuFVxsq45wLo0rbQ18cqVK3S8Y5W8Mo3eicBVDt7iDg9bFLJQLJWPsp6VG-GTj9F6pBUarU4pJxQQ-ZGs3Km1cF1BdAzjkNop-_wHmfuXe7NsVYi5uDgMDeon7OaZ6q8KtIspYp8ETc_0BkIwq56OEMHeeqmnI8dKP3_Qdp4gVvshuvsvI9cHF4HUKQqfG4Mcx8we2Wch_RyBqEFFXPtjy9MIqZKLRlRduc6CkpP1Web1GmBKGQFL8d4XOxQSFHQH8K3PYSDmlYCInEvNThel6kgkmGRVBHWkTKF0s2MyVNCyHTe7IbKY9nH9Q3vWu-1vdMYqi3A3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=CAPXqw3hvWbmjqlXoKcUmEKNhFndYYKcK3h3uh_NrEFkWKcwbmSjXrBfiTBRfZDF1WARV-gRoE68aqlDxSjxlUpTRASafBZVZS3Vt7PkPD4ac2C2Tv3WMWY2P2fkB6FQU9eoB3NVhaMWJYa9ehGkOFqFv8T6ZlCXnl5TiO33C_E7eTkLhO3G_MDM38lmbXH6pKlrk6uaYFbsI8PbXskZVVmKddIZGbSHEn2szoa6PHo3zbc3ZgQZFLtMd1Vo89Pv6XAJyqZ6A0QIQsj7i9ShvllAkqrBuGOYTglq6zsw-H_qAw4eA2MvXf6DgqqnAdLRVZgI9IzvNNZkuJuzaHO-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=CAPXqw3hvWbmjqlXoKcUmEKNhFndYYKcK3h3uh_NrEFkWKcwbmSjXrBfiTBRfZDF1WARV-gRoE68aqlDxSjxlUpTRASafBZVZS3Vt7PkPD4ac2C2Tv3WMWY2P2fkB6FQU9eoB3NVhaMWJYa9ehGkOFqFv8T6ZlCXnl5TiO33C_E7eTkLhO3G_MDM38lmbXH6pKlrk6uaYFbsI8PbXskZVVmKddIZGbSHEn2szoa6PHo3zbc3ZgQZFLtMd1Vo89Pv6XAJyqZ6A0QIQsj7i9ShvllAkqrBuGOYTglq6zsw-H_qAw4eA2MvXf6DgqqnAdLRVZgI9IzvNNZkuJuzaHO-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLaWJvTbjNSfotyGmZDARNI_ZxXX93xvL4mL-qg_mrft0TgOtNc0t_JgrGw63-8Ala_JaeTnZDDb6XjesY1ThhflznVdY2Xx1MKZYLb_X0XHWsL_nt4uUj0brxWH1QtbCfYpGwsvHkeKu07P0KV-__KSQ-0UOWo7FCZyoBiH1D2Ks-SwFS_MHkJpW8h9oPpOIt485zUZI8Qd-imInVXeu1dgV4_zvmHyGQudmjz05bUYjPFRPL6oP4HwO2TGobAlYon0oTQQmWvXja5ud-0g1MkjTVLu8Brsr_pIDBUpBazBEi5el8mjEP5dWhSmlXCuAoCprhvudXvDnkxFdE51Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSfdIQAyCiFC2G_5_kUYqRppaRK2XIpdwtJKX9BhfLsCGUPxkkjb6ZgfGG4Qi0QL7xDAcQzvgIm2ghi-tKJYkVk2So0_UnZeQaiWDQ8sMwqQNYAjZLCVex5ZOrqRxg7gKHbA_vP34I5iQuaKFuXBvFxjOETuPxu3QmPbqBsfJsBLWevOZLBpH4pYYGWac8W2lcUJXNmfZHGOVwGwBAyXyC7fGSxgG9aMukv9YT8_Uml-qE-KCA_Xw8_8DkS7uZEKmQI4XmQvgIVLXyjwh-ZHbPdnawyDsjlMmIU69zDAKaZtzgvkHvHmjfAsF2wOzSzNBJ_5sO8D1EM0tW_fxke4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=U4zt0pJL-1V2H83sbjhF-axGDvbxrIUnaLFgzllLGL9PCNUXCbPQy9Xp-LbkzEVOuAANNr0mBHBg1cKqqz3gz-NYldVIfkUvBNSZmiiLfbYq6UWxiZbI5H4yZ-y6NF64FPuQnhc8Qgdp4VPujQMIApWR5uQu1LqvEcQR5_w5t2lusCOL3_-VHplOdynvMEwei7lMpY3uAkuPntAjHIHUUmh9yViuP1v-o7FSidYlTjSCsp7cE2D5MFIdM4fipB1VQs4LiF5-c005amlR3Xz1F3l3pJJRvukJLjg6YSyv1pOx_k9h3-PmHzXFPcegOlchbEi8EeW7ndDfVZSc7bCQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=U4zt0pJL-1V2H83sbjhF-axGDvbxrIUnaLFgzllLGL9PCNUXCbPQy9Xp-LbkzEVOuAANNr0mBHBg1cKqqz3gz-NYldVIfkUvBNSZmiiLfbYq6UWxiZbI5H4yZ-y6NF64FPuQnhc8Qgdp4VPujQMIApWR5uQu1LqvEcQR5_w5t2lusCOL3_-VHplOdynvMEwei7lMpY3uAkuPntAjHIHUUmh9yViuP1v-o7FSidYlTjSCsp7cE2D5MFIdM4fipB1VQs4LiF5-c005amlR3Xz1F3l3pJJRvukJLjg6YSyv1pOx_k9h3-PmHzXFPcegOlchbEi8EeW7ndDfVZSc7bCQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
▶️
در سال ۲۰۱۶، مرتضی احمدی، پسربچه افغان که توان خرید پیراهن مسی را نداشت، با یک کیسه پلاستیکی پیراهنی شبیه لباس ستاره آرژانتینی ساخت. تصویر او در شبکه‌های اجتماعی جهانی شد و به گوش لیونل مسی رسید. مسی تحت تأثیر داستانش، مرتضی را به قطر دعوت کرد و در آنجا با او دیدار کرد؛ لحظه‌ای که رؤیای یک کودک عاشق فوتبال را به واقعیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
