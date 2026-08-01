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
<img src="https://cdn4.telesco.pe/file/SX3EEjUqyRk0XgPufYLRM0eIJ7yH0Jn2SVJiQkGetc7ixWVP1_DdnyoMoxP4Ctk9apbB1F-fbCqefpHDA80371W-9NKi_zLXXQuiaPgBQhBMQtbjA8z_30Bao8ifhoM1Dc7JwjvBlV-20BL_VZbjeY54JvvrEECnqApiql1eKYtGBiLZfvN8UBZr6OT1GqjHqLuN6RsZB56XESAAMx5UPKnJHY_QD0n4mispqbDvJ7yup2Z_ZIze5l2VrgEVgNDrXvNoxXIA7XBOYh73Zc1p-AoxQvNxFQDUbpFY7x7NKmPLGgee9A0OCmFlhzsEhwol4VmJEKUP1qREjzMSN4wFGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 438K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 09:00:12</div>
<hr>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا به فاکس نیوز : فکر نمی‌کنم رژیم ایران تا کنون با رئیس‌جمهوری مانند ترامپ مواجه شده باشد، چون واقعاً اقدامات را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/20223" target="_blank">📅 04:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEObPe0WdDvc_dVBruFjk_K3iU6Doi5HeszEWWnNo6p2Np8x5nWkf-erM2MnSvKKaYtkMx3G2tHzYWIMO06t-2OQGlWC78fkKoub22OClISK2wbYV7mNzvKIJH-uzQsS9TXTHGctTD5IWyuvT__ZVkDUBMAITLPDRx_WGAOXzX_lUIn8WQuLnc4EiM1AU0jSLCHHDCa58traTiPoCRBYubhlrKYub2KOAGRTRoEY85xiyokMuQTWBMgPTfMwYC9Tn3mETFrtj6VPZnKcsqC5C-rkcY8GFT338XKrkohyxQXefwsuzX8jmF5evvqNPPEGfjOXWjirz1rBDqlfuIsWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7dee0280f.mp4?token=D9cpYrbeCWpwUPJK8HLYcWYqzJGPD9n5dag3MIw9fY8tF9pBsZFtmNIZtGrLsFEHWINuA7q3EoSqePUsJuuNM7NJhUTMWqf_SvIDSWvw6lr3VpL5eqJqgoRG3tFCaKfVPgGaGCptnCoxos3qQPeQepI1RiejzMbLZDHvJ1winjx9iH6_OGRk4-t92P66Jj_RxmR8AHxmzTxJy0idDNzcwVI9d5L2aTiCNC3bbY42STYBy8IvMGXoNQNx1HK8QMHDxQbFd_e8sLNKbI__FsGhEkCnwKDeHB1A5kEWEYoV8fsbqNmifoc5SG3V5Bw9k9PBdz0o34R3Vh6KcHPkz0j7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7dee0280f.mp4?token=D9cpYrbeCWpwUPJK8HLYcWYqzJGPD9n5dag3MIw9fY8tF9pBsZFtmNIZtGrLsFEHWINuA7q3EoSqePUsJuuNM7NJhUTMWqf_SvIDSWvw6lr3VpL5eqJqgoRG3tFCaKfVPgGaGCptnCoxos3qQPeQepI1RiejzMbLZDHvJ1winjx9iH6_OGRk4-t92P66Jj_RxmR8AHxmzTxJy0idDNzcwVI9d5L2aTiCNC3bbY42STYBy8IvMGXoNQNx1HK8QMHDxQbFd_e8sLNKbI__FsGhEkCnwKDeHB1A5kEWEYoV8fsbqNmifoc5SG3V5Bw9k9PBdz0o34R3Vh6KcHPkz0j7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری i24news : ارتش اسرائیل با ۷۰۰ تن مواد منفجره ، شبکه تونل‌های حزب‌الله را در زیر کوه بوفور نابود کرد. @WarRoom</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/20221" target="_blank">📅 04:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏وزیر خزانه داری امریکا: ‏"بزرگترین بانک ایران سقوط کرده است."
‏"دارایی های آنها را در همه جا مسدود میکنیم این پول به مردم ایران و آمریکایی‌هایی که توسط رژیم ایران آسیب دیده‌اند، خواهد رسید."
‏"بانک مرکزی مجبور شد پول چاپ کند، هزینه تورم را متحمل شد. اکنون آنها تورم ۱۸۰ درصدی دارند. آنها قادر به پرداخت حقوق سربازان خود نیستند!"
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/20220" target="_blank">📅 03:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اکسیوس : یک مقام آمریکایی از دلایل تصمیم به حمله بزرگ آمریکا گفته است که ایران در روزهای اخیر «بسیار تهاجمی» عمل کرده و برخی مقامات آمریکایی از سطح بالای تشدید تنش از سوی ایران غافلگیر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/20219" target="_blank">📅 03:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVZ2tSnwi-R4uAFKvIQ--0zQqg2e745Vy05T0dCfaztwwRO_VBZHwQxEZWlZInHIr8MjODB9HVb173F_5-0FDjt10_a29iPe20EyOcTw19VUEm99aPzUMnUBqRQMa3a_IIUCKaz8VCHXm6oJ2sfGazDUCLAZgCqUqCVHKjniZOHLRpYYmU8aItr8s4ueCtaE4znqsxzZH2Hrp92F0xUOVXSi9yhYwIW8RW_73Ry2MOKpcyrAWfty3wrtNJmu8oe9B0DlP_VQwXpuYTuJy_BpYtABpPr5mIiqFEp3ssHRhR_TYTzQmY5DQg55AwXuHWmBBM8xGAHP4mHGindncInCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، بعد از جلسه کمپ دیوید، عکس خودش را در این مکان با چهره خندان منتشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/20218" target="_blank">📅 02:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سی ان ان : یکی از اهداف ایالات متحده، هدف قرار دادن سایت هسته‌ای کوه کلنگ عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/20217" target="_blank">📅 02:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شنیده شدن صدای انفجار در کویت
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/20216" target="_blank">📅 02:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/20215" target="_blank">📅 02:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2lIMbwPuViomzJTgvyS5VmJuWmVRCO37w7uzXEBJOE9h31bTnl3bGxlHfoxS1IYMUC2XH6pOikdaFQjva4ZxCdZOOgxyUD6w6ni4sGMIlEDKCRJCWq_mQHQ_Jl5nmoyW07jvlwEEsG9IARug5JeLVTFklrPhu7kQzrommrTI9NW5WcngVlJpY2ZgXyrI5ACkG2IaSackpXuXa7F-G3jm0kfm-Qrlk9QGFrGiZBuNTZfokWZMAkIYVwOgGIxNxB8KCwLSQoS43zp_CB2w4oyoPaHpEvEHa7q25aL-Kjd4RUo2ZDDWUH4HBz7vFzj-xjz_1glMYDwXZxV9_pDIKaq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین : با ترامپ دیدار داشتم، نمی‌تونید تصور کنید چه بر سر رژیم ایران میاد @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/20214" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20213" target="_blank">📅 02:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تسنیم: یه آشی برا آمریکا پختیم که یه عالمه روش روغن داره
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20212" target="_blank">📅 02:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20211">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادعای آکسیوس: اسرائیل نیز برای انجام حملات علیه ایران به ایالات متحده خواهد پیوست
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/20211" target="_blank">📅 02:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فعلا پوتین سنگین کی یف اکراین رو داره میزنه
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/20210" target="_blank">📅 02:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سی بی اس : مقام های ارشد آمریکا امروز درباره قطع کردن برق تو سراسر تهران گفت‌وگو کردن!
هدف از حمله به این زیرساخت‌ها، تضعیفِ توان تو ارائه خدمات و اداره موثر کشور عنوان شده...
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20209" target="_blank">📅 02:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مطمئن شوید که چنل تلگرام و اینستاگرام رو عضو هستید. در صورت قطعی اینترنت، تلگرام تنها پلتفرمی است که با ضعیف‌ترین اینترنت هم میتوانید اخبار را داشته باشید.
حتما چنل رو پین کنید تا بالا باشد.
🌐
@WarRoom
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20208" target="_blank">📅 02:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت جوریه که هر کسی بخوابه ممکنه سکانس پایانی رو از دست بده.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20207" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک مقام ارشد امنیتی ایران اعلام کرد:
ایران یک طرح جامع برای پاسخگویی در صورت حملات جدید آمریکا یا اسرائیل به زیرساخت‌های ایران، آماده کرده است، بر اساس این طرح، اهداف احتمالی شامل زیرساخت‌های حیاتی در اسرائیل و زیرساخت‌های انرژی آمریکا در سراسر منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20206" target="_blank">📅 01:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شبکه CNN: مقامات گفتند که ایالات متحده در حال برنامه‌ریزی برای انجام موج جدیدی از حملات علیه ایران در همین آخر هفته است.
دامنهٔ دقیق حملات و اهداف احتمالی مشخص نشده است. هر دو مقام آمریکایی هشدار دادند که تا زمانی که حملات آغاز نشوند، امکان لغو آنها وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20205" target="_blank">📅 01:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مارک لوین : با ترامپ دیدار داشتم، نمی‌تونید تصور کنید چه بر سر رژیم ایران میاد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20204" target="_blank">📅 01:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس اتحادیه کانفیگ فروشان : ما با تمام قوا آمادهیم و سرورهایمان را تمدید کردیم.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20203" target="_blank">📅 01:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سی بی اس :  آمریکا و اسرائیل در حال آماده‌سازی برای سخت‌ترین حملات بمبارانی علیه زیرساخت‌های انرژی ایران هستند ، حملات ممکن است از همین الان (آخر هفته) شروع شود اهداف شامل نیروگاه‌ها و پالایشگاه‌هاست اما ترامپ هنوز دستور نهایی صادر نکرده ، اسرائیل با آمریکا…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20202" target="_blank">📅 01:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اکسیوس: یک مقام آمریکایی می‌گوید ترامپ به طور جدی در حال بررسی حمله به اهداف انرژی ایران در عرض چند روز آینده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20201" target="_blank">📅 01:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کاخ سفید: تهران تفاهم نامه را نقض کرده است، بنابراین رئیس جمهور ترامپ بیکار نمی ماند و پاسخ حملات و اقدامات ایران را می دهد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20200" target="_blank">📅 01:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us4j7vgOyMUaXpEYvYLBXqpt5cA5b-FU3go2j5YKHpoq0RHqB73iM8TACeb4Y1kpLlJnXIQTUHu-NuZG-XXus_8CTZSrxqJ2mcTE9ktYfAduMiXpjdb76y8fVj2I4kD2e8JeRvGSAS5fjk2rix0CEMqBfou2fO4TTPR9tRPlEQNEZ0uaBM5vxdjnCKw4_9UDW3rRgyWFd-IiqrMKLedhf2ra2hj87vW0IdnaohNEsy7sN95UHWVznKos9Q3NVMdCALf7T2SmUiWDqHMaUYBMGaNwzQdUt_MP-DsFLqj47cezvskKOs4_QFCQkX8Z6ycGun9LO9-mX8-l1N-wRUMlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت جورنال: رئیس جمهور ترامپ دستور اجرای مجموعه‌ای از حملات را در طول تعطیلات آخر هفته صادر کرد تا تهران را مجبور به تسلیم شدن کند. @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20199" target="_blank">📅 01:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اتاق جنگ با یاشار : تیک تاک ، تیک تاک ، تیک تاک  بینگ ، بینگ ، بینگ ، بینگ @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20198" target="_blank">📅 01:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اتابکی : بیاین دیگه ، بیاین ….
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20197" target="_blank">📅 01:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی پنتاگون: وزارت دفاع آماده است تا در هر لحظه دستورات رئیس‌جمهور ترامپ را اجرا کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20196" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jangal bedoneh risheh (iG @yashar)</div>
  <div class="tg-doc-extra">siavash ghomeishi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/20195" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20195" target="_blank">📅 01:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرنگار شبکه i24 news: همزمان با انتشار گزارش‌هایی درباره آماده‌سازی برای حمله به اهداف مرتبط با بخش انرژی در ایران، یک منبع آگاه از این گفت‌وگوها به من گفته است: «رئیس‌جمهور دیگر صبرش را از دست داده است. این حمله می‌تواند رژیم را در آسیب‌پذیرترین نقطه‌اش هدف قرار دهد. تصمیم نهایی در آخرین لحظه گرفته خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20194" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتاق جنگ با یاشار : تیک تاک ، تیک تاک ، تیک تاک
بینگ ، بینگ ، بینگ ، بینگ
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20193" target="_blank">📅 01:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وال استریت ژورنال:ترامپ در جلسه امروز تیم امنیت ملی خود در کمپ دیوید ، دستور حمله نظامی جدید آمریکا به ایران را صادر کرده است @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20192" target="_blank">📅 00:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سی بی اس :  آمریکا و اسرائیل در حال آماده‌سازی برای سخت‌ترین حملات بمبارانی علیه زیرساخت‌های انرژی ایران هستند ، حملات ممکن است از همین الان (آخر هفته) شروع شود اهداف شامل نیروگاه‌ها و پالایشگاه‌هاست اما ترامپ هنوز دستور نهایی صادر نکرده ، اسرائیل با آمریکا…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20190" target="_blank">📅 00:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سی بی اس :  آمریکا و اسرائیل در حال آماده‌سازی برای سخت‌ترین حملات بمبارانی علیه زیرساخت‌های انرژی ایران هستند ، حملات ممکن است از همین الان (آخر هفته) شروع شود اهداف شامل نیروگاه‌ها و پالایشگاه‌هاست اما ترامپ هنوز دستور نهایی صادر نکرده ، اسرائیل با آمریکا هماهنگ است اما مقام اسرائیلی می‌گوید از تصمیم قطعی مطلع نیست همچنین بحث‌هایی درباره پایان قبل از باز شدن بازار دوشنبه وجود دارد،این طرح در جلسه کابینه کمپ دیوید مطرح شد و برخی دستیاران کاخ سفید مخالفند اما پنتاگون اعلام آمادگی کامل کرده همچنین بحث قطع برق تهران هم مطرح شد!
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20189" target="_blank">📅 00:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار اطراف اهواز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20188" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسپانیا: مهاجرین غیرقانونی به مال ها حمله کردن و در حال غارت کردن فروشگا های لوکس هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20187" target="_blank">📅 00:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سنتکام : از زمان ازسرگیری محاصره بنادر ایران، مسیر ۳۰ کشتی را تغییر داده و مانع حرکت دو کشتی شده‌ایم
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20186" target="_blank">📅 00:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مجری : در مورد ایران، آیا ایده‌ای دارید - یک ماه، یک سال؟ چقدر طول می‌کشد تا آنچه اتفاق می‌افتد حل شود؟  ترامپ: همیشه سخت است. ما ونزوئلا را در کمتر از یک روز حل کردیم. @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20185" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsvySuIl4lZlNLZHsW7bWrYNrkAaE1NExjSsbqytNkbszJR6lIqSxjnqEoUpgXFPtPGtYN6BttEcSJf7e28yxJ4soV6_5Z8hDYyf-cRXRRW3njqyUkozjko1FkZPA2XMR8-sNzdTIrRswjT3HoIGloEpzePuaTpz4OA0pbNxWlT7HsuMbLBHiV8ov3nEuT4R2GPX9gCo997Uk06NRGPD3q1BOBXVlOQn9Vq5nKeU2w0jRctGx2CpzD2X4_qWcDssxYBA9c35PPqIBmthJ3_H3-qqxk4CRl78Wyq7xUuUdRtaIvQ8zc695jkgFafx9Rp8SqfinNpUDmj5tpPRrd0TfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان اسکله پل بندرعباس
ارسال مهمات و تجهیزات به قشم
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20184" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش صدای انفجار غرب بندر عباس @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20183" target="_blank">📅 00:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb09e50276.mp4?token=eNmVM6OIItIWPBPbBdpub1eHhUAxVGVxA65qD1oNqoXPv7I1CeIMHZQaRFtssgGm8pzTMskHpktC2SE_XufwuYDIQodfMOZ6IdkyJOflItRc-Y7BIAoKWMewI-5YTpBp1JZvbDeuxbUgfDZ30YexjcRqyEcsghDv-25m1d0QJpmJMAD0PSdgd-wNnoXaHBcG5JfLsgvC9s6Pf_J83PRXgoMXEI2p4WmB1v82xuQm-yXMTWTI2pWuUD4lPPhra1ZDACKJNKscZY9iqrZt0ARfB5v7jZJp-TSzO8StLIxZDrKKiesr_ahcG3YcTw1AQ5yvW7ozkNgyCgIW_OdGnxiErw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb09e50276.mp4?token=eNmVM6OIItIWPBPbBdpub1eHhUAxVGVxA65qD1oNqoXPv7I1CeIMHZQaRFtssgGm8pzTMskHpktC2SE_XufwuYDIQodfMOZ6IdkyJOflItRc-Y7BIAoKWMewI-5YTpBp1JZvbDeuxbUgfDZ30YexjcRqyEcsghDv-25m1d0QJpmJMAD0PSdgd-wNnoXaHBcG5JfLsgvC9s6Pf_J83PRXgoMXEI2p4WmB1v82xuQm-yXMTWTI2pWuUD4lPPhra1ZDACKJNKscZY9iqrZt0ARfB5v7jZJp-TSzO8StLIxZDrKKiesr_ahcG3YcTw1AQ5yvW7ozkNgyCgIW_OdGnxiErw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: در مورد ایران، آیا ایده‌ای دارید - یک ماه، یک سال؟ چقدر طول می‌کشد تا آنچه اتفاق می‌افتد حل شود؟
ترامپ: همیشه سخت است. ما ونزوئلا را در کمتر از یک روز حل کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20182" target="_blank">📅 00:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار از دور در قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20181" target="_blank">📅 00:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار سکنج کرمان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20180" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حوثی های یمن
: ۸ نفتکش سعودی مجبور به تغییر مسیر شدند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20179" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ در مورد ایران:
می‌خواهید همه چیز سریع تمام شود؟
به دیوانه‌ها سلاح هسته‌ای بدهید.
خیلی سریع تمام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20178" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش صدای انفجار غرب بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20177" target="_blank">📅 00:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8900ed7e3.mp4?token=Bw4kRQijJzIH5LhuFnduXYKFwJu3RVdOeeOrHMtHCf387EL7yB_zPAkjjF1KmxO1DsqsLm6jiuqVgkgyUxS7d_JLyHUKf-ZXJMXARwSi5xOvCH4Lq2SACi5Ly7NNcIeTJQlKNHB-Zp6-xgoh4LFcLDJ3uikcVwpM3EcwPNARlnuvgJG055JZraHJg59yoE8NIcSyq6qVgBa3qLDD99tpi8wuFd0uVs1A1_CrOGCWPZI_tqUqkvjqd87P7tmChdFiS4BKmLHCjHWs4PkmoojC00wNIYmMCmIpsRak-ua3N3bkeqcLwQl2yWmxFZ_sX_U5xCUA1skyVj5KzQwuCdn-6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8900ed7e3.mp4?token=Bw4kRQijJzIH5LhuFnduXYKFwJu3RVdOeeOrHMtHCf387EL7yB_zPAkjjF1KmxO1DsqsLm6jiuqVgkgyUxS7d_JLyHUKf-ZXJMXARwSi5xOvCH4Lq2SACi5Ly7NNcIeTJQlKNHB-Zp6-xgoh4LFcLDJ3uikcVwpM3EcwPNARlnuvgJG055JZraHJg59yoE8NIcSyq6qVgBa3qLDD99tpi8wuFd0uVs1A1_CrOGCWPZI_tqUqkvjqd87P7tmChdFiS4BKmLHCjHWs4PkmoojC00wNIYmMCmIpsRak-ua3N3bkeqcLwQl2yWmxFZ_sX_U5xCUA1skyVj5KzQwuCdn-6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران
:
من در حال انجام کاری بسیار بزرگ‌تر از چیزی هستم که گفته بودم انجام خواهم داد.قرار بود وارد شویم، توان نظامی آن‌ها را از بین ببریم و بعد خارج شویم.
اما بعد متوجه شدم اگر این کار را انجام دهیم، باید نوعی حضور و نظارت مستمر وجود داشته باشد؛ وگرنه آن‌ها دوباره همه‌چیز را بازسازی خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20176" target="_blank">📅 00:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdg0cgFhVz1GjYJAgTDisSiir7PhtDd7Oe5SzrmID7H9LKw5vNPvqZS_6bM717Z7eBYAFjA8U7P7TJw1-aDdIvgEDtuvvORvhkNnfgChcxSnj_5H2rVwORrPU5dH2iGiVgIc3MGM2KHUS4JPPcVAU69-LWtj_Koxr9bCqvo2EUpEm2VsjXU9m2Q4RVaf9m9lX_xp-UwvR4DB4z4uC3pBrAUOHSw3VBJkTbCZqYnh1H0ud8upglc7u0TkoTG3EQZbQAC6KQmkGEgi_F2ELxmLzVd-aeLxvUdmI_8YVdKJZjT_z2wmrn2zuFaHIBzOf5sOJ6vosyekepoySYUsjsjbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس تحلیل داده‌های پروازی، دو فروند جنگنده F-35A Lightning II نیروی هوایی ایالات متحده آمریکا با کد دم LN و معرف پروازی TABOR71 و TABOR72 صبح امروز از پایگاه هوایی لیکنهیث (Lakenheath) بریتانیا به سمت خاورمیانه اعزام شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20175" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAW9EEtCpBcjkpiVxRTRB45J_r1iR5WXWgwjPddKYI_SWrDCBFq8FPvbfSZNiVK53PPH-ulGWkKHXqIJ8i9U-qG17zI7S5nkiWePfPHbozp2oikG3WA8UNll46YQwfSzKJssAzCr9v3o81oYVcwCDQKWXwff6iVH7LA83BgxKb6-_IRjHBccG_4pR-GLTqslCqOGfE6hO6px_sGHtKdF35u7tPb4RQ75b-B8AaN2rkrfX-cxHSA_IHGmDQ-Gr9LaJjexmA996YYb5Be_wmYyd9WFgcGcjGUBecyvYojbqpGTJEFXrHcJnjZsJzJJ0uYUXeOpxFdxJNHQax6pxQkYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش فعالیت سوخت‌رسانی هوایی آمریکا در خاورمیانه همچنان ادامه دارد؛ طی ۷۲ ساعت گذشته دست‌کم ۱۲۲ سورتی پرواز توسط KC-135 و KC-46 ثبت شده (میانگین روزانه حدود ۴۱ مأموریت) که حداقل ۲۱ مورد آن در خلیج فارس و دریای عمان انجام شده است. این سطح از فعالیت نشان‌دهنده حفظ ریتم عملیاتی بالا و توانایی و آمادگی کامل آمریکا برای اجرای حملات دوربرد، گشت‌های رزمی و عملیات شناسایی بدون اتکای کامل به پایگاه‌های منطقه‌ای است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20174" target="_blank">📅 23:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b1ce5038.mp4?token=mUghwy943j1Di8FYr_aW31lFMYLAvBNBEsR81gScASShEy5SJqEs6w_Ot8UEX94Ac0YIk33bleBgCtmVElckMUmaSNb6QzUGrJ_Itq5w4LQh19PT5S7FPjKwVpjKh8qtlGpTNiVdul1dW56Iwun0r33uJCKnLEFfEWi9-fcBXrGosYyIovCC4HZz6I0FJ6hCgaEQ3fE7Ch8r2iaGTU8_6b0WYlozaQ_jICyrkr6GyqnGv3fGpWc8ejQxT9HTNvbWPtuHCV0orqjIZPY8ubgMCCmvqyWQCOsoBMqdaR5SDl7ttk-2WKhMNIeJg5eK7Xnu7rxNrMYnIjP2KwuErzsC_J29iWURZgSaqyzeYped7YC-rjdT5TrEU7DIeMzm_BTSDVbyuWe_Kv8Kwj0iGdp8A7CARJgYBzlp7pBzVmV7-mQl_j6xRJpRTKjbZwEmB8qZMyoqYj5OzrI_-gkkoW-ySPUXoy9m0uL4qkYJU8NX8iJdCIP-3gJeuh3JRUOinndST3N0tXE48fdBXFLlDqQyvE7xv4Sw-rFeqSw-O9M9-8_JXuqI1AMwmxoHkHltToQlmGCpZGcyX7yThmVbUik0xkBVeyf6hlQqDMBPz9hcIPry6rpxMc5V3OByAHxXsnUeksiEmN3v3sePZwi7gc6tXZ9VKAeDYByVaLlAfRCtkmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b1ce5038.mp4?token=mUghwy943j1Di8FYr_aW31lFMYLAvBNBEsR81gScASShEy5SJqEs6w_Ot8UEX94Ac0YIk33bleBgCtmVElckMUmaSNb6QzUGrJ_Itq5w4LQh19PT5S7FPjKwVpjKh8qtlGpTNiVdul1dW56Iwun0r33uJCKnLEFfEWi9-fcBXrGosYyIovCC4HZz6I0FJ6hCgaEQ3fE7Ch8r2iaGTU8_6b0WYlozaQ_jICyrkr6GyqnGv3fGpWc8ejQxT9HTNvbWPtuHCV0orqjIZPY8ubgMCCmvqyWQCOsoBMqdaR5SDl7ttk-2WKhMNIeJg5eK7Xnu7rxNrMYnIjP2KwuErzsC_J29iWURZgSaqyzeYped7YC-rjdT5TrEU7DIeMzm_BTSDVbyuWe_Kv8Kwj0iGdp8A7CARJgYBzlp7pBzVmV7-mQl_j6xRJpRTKjbZwEmB8qZMyoqYj5OzrI_-gkkoW-ySPUXoy9m0uL4qkYJU8NX8iJdCIP-3gJeuh3JRUOinndST3N0tXE48fdBXFLlDqQyvE7xv4Sw-rFeqSw-O9M9-8_JXuqI1AMwmxoHkHltToQlmGCpZGcyX7yThmVbUik0xkBVeyf6hlQqDMBPz9hcIPry6rpxMc5V3OByAHxXsnUeksiEmN3v3sePZwi7gc6tXZ9VKAeDYByVaLlAfRCtkmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند جنگنده اف-۳۵ با یک حادثه در پایگاه هوایی میرامار نیروی دریایی در سن دیگو، ساعاتی پیش آتش گرفت. تیم‌های امدادی حوالی ساعت ۱۰ صبح به وقت محلی به دلیل دود غلیظ به محل اعزام شدند. علت حادثه در دست بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20173" target="_blank">📅 23:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">روزنامه نیویورک پست، به نقل از دو منبع، از جزئیات بیشتر طرح دو هفته ای ژنرال براد کوپر فرمانده سنتکام گزارش داد عملیات بمباران گسترده و طولانی‌مدت علیه ایران تدوین شده است.
این عملیات، یک بمباران مداوم خواهد بود، برخلاف حملات محدود و شبانه‌ای که در دور قبلی درگیری مشاهده می‌شد، و از مهم‌ترین عملیات‌های نظامی از زمان آتش‌بس هشتم آوریل خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20172" target="_blank">📅 23:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20171" target="_blank">📅 22:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20170" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20169" target="_blank">📅 22:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نظرسنجی شبکه 13 اسرائیلی:
62 درصد از شهروندان اسرائیل به توانایی ترامپ در جلوگیری از پیشرفت برنامه هسته‌ای ایران اعتماد ندارند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20168" target="_blank">📅 22:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">واشینگتن‌پست: ترامپ نباید به توصیه‌های جی‌دی ونس درباره جمهوری اسلامی عمل کنه.
به نوشته این روزنامه، تهران از مذاکرات برای خرید زمان استفاده میکنه و آمریکا باید فشار نظامی و اقتصادی بر جمهوری اسلامی رو ادامه بده و از ازسرگیری عملیات علیه ایران عقب‌نشینی نکنه.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20167" target="_blank">📅 22:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BprGewxcclvkhdKxeSG0Z0RCK5v6iGB7RL0OZNGVK4EdT8uyU91kk1G8o2Xp4BdBGVZ9FrzzI3E14hUjzqggyT2VWJhrBOnBjgIEaJdZdAQlf0sN0ffNwFYP4jcPRBPlShE_MomjzErwhzViRUS9iedyQ2iTsZXUOI3kABeBOwyKoSOblkixBRKy6GiZOZroFkAU6N8xaFKXxtK7tf_pcTJCwlbvKbDGy1TsYlXBiY39Thsm_9hN3vTxsMw2ohBUTi3UfXM5NxdIymKdlpFYFU8gahwRqut4V_1Xiw_Ip0nj_k7NSlT3i2Fh3FGHDZdPP4S3aamQkc0AJZnsElYhFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش تحقیقی رویترز منتشر کرده، یک صرافی ارز دیجیتال، به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است.
این صرافی یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به صرافی بایننس و فعالیت‌های استخراج بیت‌کوین و بانک مرکزی ایران مرتبط می‌کند.این شبکه قمار فارسی‌زبان که متشکل از بیش از ۲ هزار وب‌سایت است از جمله توسط
ساشا سبحانی و پویان مختاری
، دو اینفلوئنسر ایرانی تبلیغ و اداره می‌شود که ارتباطاتی در سطوح بالای حکومت ایران دارند. تحقیقات رویترز همچنین نشان داده است که سپاه پاسداران سال‌ها پیش کنترل بزرگ‌ترین وب‌سایت‌های قمار قابل دسترس در ایران را به دست گرفته و از آن زمان تاکنون از این وب‌سایت‌ها برای انتقال حدود چهار میلیارد دلار به خارج از کشور استفاده کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20166" target="_blank">📅 21:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d306e1b0.mp4?token=RhflMQe-vo0AZO4PXJOqMrqc_qYa9jwEOvdy6p99NkiFwrs9eyZDJEJnNpi7XkdUNLdXT4OrosjPLKV1d56TvGUbLc9J88JlBvz2wu-7ECgiNnFFIowyJwmUk8-BQYlwVv0HBfPd8-J2bUjgxPMi1yTdcx33quNibif116ROmiH5ejmeDIOac3VTFZueo4M2j7_toKmUYr21aJgBUjIfCHfRTIdCsDv6kdKtuQMQU6JQWdE5brTuWQ-r24Ad00TVd_VHaONm1qXhIznCue4guEDNHBZ9u2IeKOS1Bfvgl7iUHLvPQ2xZkfdU3oOY7Sr5exiK0zNznVKN41Qe9tQxDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d306e1b0.mp4?token=RhflMQe-vo0AZO4PXJOqMrqc_qYa9jwEOvdy6p99NkiFwrs9eyZDJEJnNpi7XkdUNLdXT4OrosjPLKV1d56TvGUbLc9J88JlBvz2wu-7ECgiNnFFIowyJwmUk8-BQYlwVv0HBfPd8-J2bUjgxPMi1yTdcx33quNibif116ROmiH5ejmeDIOac3VTFZueo4M2j7_toKmUYr21aJgBUjIfCHfRTIdCsDv6kdKtuQMQU6JQWdE5brTuWQ-r24Ad00TVd_VHaONm1qXhIznCue4guEDNHBZ9u2IeKOS1Bfvgl7iUHLvPQ2xZkfdU3oOY7Sr5exiK0zNznVKN41Qe9tQxDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: میدونید موشک هایی که ایران به سمتمون میندازه رو چطوری رهگیری میکنیم؟! اینطوری: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20165" target="_blank">📅 21:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngEQ5FhIn-kb2o1A1T-53-a8-vL3z3znac4GMli68NpT0ipRL-3G2lJTMhwVY-th1vVQFaEXajLuwlOAZTNMfkEYY0vAQM-e9K7oECGFOO9F0TrwSAWjVWW-gTdZ1UyrVLiFmtpNuQnP62HmW6pdnzXOAsdgwqoI1Av6u8_u5lJx7jL71Ap2PCNZMgqLTiVpkLSE08IxZWh-IcMkzfSYMOzPDtlauWaKEpM2LjM2qyGO3F8NDpI-cum9JIce4PCXLZhMa8pyKMO01nhdEt0HzYyyCqkAiN9ZCkk2D45VgT1LhloK_9QeOY5OBLILuHLoHywdTMthc30ZGOvqUEJDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای، روز گذشته یک ناو هواپیمابر آمریکایی(بوش یا لینکلن) در ۳۴۰ کیلومتری بندر چابهار ایران مشاهده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20164" target="_blank">📅 20:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c77f1bbbfa.mp4?token=JS44VUbwhKp58TLjcF79imD6fqnyk00hKkbHhT3eVK9UR0RqvzwnPFYUk2-X-31NFq5pHymmNSJu2WMHGRrEcCj-rqe4mvd31-7GL8mF-GMUoC0uqxmLwJVWl-irWHw2KTYboy5_KnQ0vsf0YLTLda4_gtNCpeGpjmhg8vec76pNqFA3LGLp4O_dCV-5D5N3r1-UO7tPSVdfgyBgryNg6ma6m-TtYqM8TcAo2HzaxzCynP97VKuCG9S2by46FMp3zhEyv7xZXr_5fp-axMkd-qMdV3gOTtwiGYxtQ7IM6z5v1RiyvMXn36nSFwZTstgt9Eqe7aMRIxGVdphnnlOg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c77f1bbbfa.mp4?token=JS44VUbwhKp58TLjcF79imD6fqnyk00hKkbHhT3eVK9UR0RqvzwnPFYUk2-X-31NFq5pHymmNSJu2WMHGRrEcCj-rqe4mvd31-7GL8mF-GMUoC0uqxmLwJVWl-irWHw2KTYboy5_KnQ0vsf0YLTLda4_gtNCpeGpjmhg8vec76pNqFA3LGLp4O_dCV-5D5N3r1-UO7tPSVdfgyBgryNg6ma6m-TtYqM8TcAo2HzaxzCynP97VKuCG9S2by46FMp3zhEyv7xZXr_5fp-axMkd-qMdV3gOTtwiGYxtQ7IM6z5v1RiyvMXn36nSFwZTstgt9Eqe7aMRIxGVdphnnlOg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید ایران هنوز برخی از توانایی‌های خود را حفظ کرده است. آیا آمریکایی‌ها باید برای این حملات پی در پی آماده باشند تا زمانی که ایران به سادگی قادر به حمله متقابل نباشد؟
ترامپ: آنها کمی قوی‌تر خواهند شد، شاید الان، اما ضعیف‌تر خواهند شد.بله، مطمئناً. شما همیشه باید هوشیار باشید.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20163" target="_blank">📅 20:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f7a15aa5.mp4?token=CsIZ5RQW5k-Ro_s6MX7Kgz3RpFjTiT3CD-T7opwyE3EFoWydhAxXbTzGncgg9n9wp1Pg0DMG7V9kvbFylBO_fuZmODw2PfKUhkH_0pgFgm9iwwuXIAU1FyhjEYdlCIafR8mkkrxwQR_fHl4DGx_ZEfE-uMgdOo47HGBJOs0xd6upJnXSwPadWG1K6VzosXSFxnDyDU2BBig-KL7fi-hRVRol1XpiEDzCGjO5_8pjo5qu9hnUv76YKBrrkLQO-neHRpMYIR0Pu-R5XCwWc067VWLT7BNyyq2cLtxA_fOemT7pP-p8M8i9tDgd5s7QfxwJW_mjAMCDXhluq8jN00ofdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f7a15aa5.mp4?token=CsIZ5RQW5k-Ro_s6MX7Kgz3RpFjTiT3CD-T7opwyE3EFoWydhAxXbTzGncgg9n9wp1Pg0DMG7V9kvbFylBO_fuZmODw2PfKUhkH_0pgFgm9iwwuXIAU1FyhjEYdlCIafR8mkkrxwQR_fHl4DGx_ZEfE-uMgdOo47HGBJOs0xd6upJnXSwPadWG1K6VzosXSFxnDyDU2BBig-KL7fi-hRVRol1XpiEDzCGjO5_8pjo5qu9hnUv76YKBrrkLQO-neHRpMYIR0Pu-R5XCwWc067VWLT7BNyyq2cLtxA_fOemT7pP-p8M8i9tDgd5s7QfxwJW_mjAMCDXhluq8jN00ofdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران:
رادار؟ «رفته.» رهبرانشون؟ «رفته‌اند.»
و بعد جمع‌بندی نهایی: «همه‌چیز رفته.»
همه‌چیز... رفته. همه‌اش... رفته. رفته که رفته!
آخر هم با یک بالا انداختن شانه گفت: «البته، باز هم به جنگیدن ادامه می‌دهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20162" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f38497106.mp4?token=WMJjgymfIILPmcUiR6EQy0AziL5dW8XMDHI1N3FVWgsZjp64b4HWPocjS6M_tcYX5H6Y_DovH7MCl83W7UraqLbtp9rhMo0eTUsMxB8Ui06QdGyFh_zHZLDNsNfJiItaPhTFQo0cVvZ9_yincC3hEnS1sFE1fnY4Evz8YNUsdeB_KFRAtJ4EvMPb5YpkLq2jd0-GSYAS4PomPVuDMe-8RCzWvul9cr5gyx2gJvZrqzuL2gWy8Gm437CT00NIotRNx0d_QgwSIBk2jEiRtl9kd4V4_QH2jIIW34h-05QXmCO7mMnnAajg2uCIEFakVq8rKqAhxOVbfjqPQbJjmO3bgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f38497106.mp4?token=WMJjgymfIILPmcUiR6EQy0AziL5dW8XMDHI1N3FVWgsZjp64b4HWPocjS6M_tcYX5H6Y_DovH7MCl83W7UraqLbtp9rhMo0eTUsMxB8Ui06QdGyFh_zHZLDNsNfJiItaPhTFQo0cVvZ9_yincC3hEnS1sFE1fnY4Evz8YNUsdeB_KFRAtJ4EvMPb5YpkLq2jd0-GSYAS4PomPVuDMe-8RCzWvul9cr5gyx2gJvZrqzuL2gWy8Gm437CT00NIotRNx0d_QgwSIBk2jEiRtl9kd4V4_QH2jIIW34h-05QXmCO7mMnnAajg2uCIEFakVq8rKqAhxOVbfjqPQbJjmO3bgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
ترامپ: «هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20161" target="_blank">📅 20:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: موشک تاماهاک باورنکردنی‌ترین است - می‌توانید از یک درگاه عبور کنید، آن را از پنجره یک خانه عبور دهید.
هیچ‌کس چیزی شبیه به آن ندیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20160" target="_blank">📅 20:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ
: اگرچه نیروی دریایی، نیروی هوایی و پدافند هوایی ایران تا حد زیادی از کار افتاده و تنها توانمندی‌های ناچیزی برای آن‌ها باقی مانده، اما تلاش‌ها برای تضعیف بیشتر این توان باقی‌مانده همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20159" target="_blank">📅 20:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حقیقت یاب سنتکام : سپاه دروغ میگه !تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران آن را کنترل نمی‌کند. هزاران کشتی طی چهار ماه گذشته از این آبراه بین‌المللی عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20158" target="_blank">📅 20:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8367cad8.mp4?token=lJmsV34zpNp7-OgzAWqUczYEDfAzl6t-B_NvmJbOsuIsQ--pxatcvrJAg2rtG2Vz1Fnvw6tFf_Hz9KG5RYkWpf2N9JBM9UWBbed0PskYZJsx9FIn6hK0LkiuHgkcWJmRS6SlRG0dtAXmfT7hZeWAI8BXZ6F44_XG-BSpgYVdQ3YwXY7rOMI7v-k9kB6YP3hbmR6t2zqvo3s7R8iy9vIxz6NMcFisl3Wvyz79S8eIuvs8HCqllKF4Yl2sYFzGimkLXs6zT1YwZh_BZRlLLyESBwiZ4QoFO1dxEBzwt6cqHFVSVVfHbKvj8jAYr8wOb6nZYU5A-CEot3nQYbS0yZji0gyNquKu9nNP8XUrCNpIhEyRvS6rXCZVFqtftEu-UZIP6NFMV44vvzHfUHoszo4Ref5vtePjIqgGjVbfYUvuGVZTqbwV1qfxGPLDP8B29wR3WIkU6T48xBY5xMvn8ParBKCWT8z8otyd39TtIilZKam4Y69L5pDWulEazCFbjvcAw33P-lCPwIqqK3dzBTCRXffmIyewl1tGLxgG_Pr5hAy_q174d8zBnOsisJBrPiVCNKqeKjKDVM83cQJQm96DC5TvTW3dyGNaLE2oYR1Y6-B9_7l75e0Le_VufestDnMmm4VKdnc309o_iZllke-jtshPVOU2w-PMU2wtKsT4Iv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8367cad8.mp4?token=lJmsV34zpNp7-OgzAWqUczYEDfAzl6t-B_NvmJbOsuIsQ--pxatcvrJAg2rtG2Vz1Fnvw6tFf_Hz9KG5RYkWpf2N9JBM9UWBbed0PskYZJsx9FIn6hK0LkiuHgkcWJmRS6SlRG0dtAXmfT7hZeWAI8BXZ6F44_XG-BSpgYVdQ3YwXY7rOMI7v-k9kB6YP3hbmR6t2zqvo3s7R8iy9vIxz6NMcFisl3Wvyz79S8eIuvs8HCqllKF4Yl2sYFzGimkLXs6zT1YwZh_BZRlLLyESBwiZ4QoFO1dxEBzwt6cqHFVSVVfHbKvj8jAYr8wOb6nZYU5A-CEot3nQYbS0yZji0gyNquKu9nNP8XUrCNpIhEyRvS6rXCZVFqtftEu-UZIP6NFMV44vvzHfUHoszo4Ref5vtePjIqgGjVbfYUvuGVZTqbwV1qfxGPLDP8B29wR3WIkU6T48xBY5xMvn8ParBKCWT8z8otyd39TtIilZKam4Y69L5pDWulEazCFbjvcAw33P-lCPwIqqK3dzBTCRXffmIyewl1tGLxgG_Pr5hAy_q174d8zBnOsisJBrPiVCNKqeKjKDVM83cQJQm96DC5TvTW3dyGNaLE2oYR1Y6-B9_7l75e0Le_VufestDnMmm4VKdnc309o_iZllke-jtshPVOU2w-PMU2wtKsT4Iv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: چه کسی از دولت با ایران صحبت می‌کند؟
ترامپ: آن‌ها همیشه می‌خواهند صحبت کنند... استیو، جرد، جی‌دی و مارکو درگیر هستند.
گزارشگر: ایران می‌گوید مذاکراتی در حال انجام نیست
ترامپ: ممکن است مدت طولانی درباره هسته‌ای صحبت کنیم و سپس آن‌ها بیرون بروند و بگویند: «ما هرگز درباره هسته‌ای صحبت نکردیم...» آن‌ها فقط کاری می‌کنند که عصبانی شوم
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20157" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ درباره ایران : آنها هفت ساعت درباره موضوع هسته‌ای صحبت می‌کنند. من می‌گویم: چرا هفت ساعت؟ این کار را می‌شود در پنج تا ده دقیقه انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20156" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ درباره ایران:ما می‌توانیم به توافقی با ایران برسیم، اما من به تدریج اعتمادم را به آن‌ها از دست می‌دهم، زیرا آن‌ها دروغ می‌گویند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20155" target="_blank">📅 20:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار : طبق روال تمامی جمعه‌ها از هشت ماه پیش تا کنون، امشب بیداریم و نوشیدنیهای الکلی و غیرالکلی را نوش جان خواهیم کرد.
امروز بیشتر خاص است چون ورود ششمین ماه میلادی شروع جنگ هم است
@WarRoom
💥</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20154" target="_blank">📅 17:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزیر خزانۀ آمریکا به فاکس نیوز: محاصره‌ی نظامی و اقتصادی ایران متوقف نخواهد شد و ما در سراسر جهان به دنبال اموال ایران خواهیم رفت.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20153" target="_blank">📅 17:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌  اتفاقی راجع به ایران قرار است بیوفتد @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20152" target="_blank">📅 17:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ به فاکس نیوز: ایران در نهایت چاره ای جز تسلیم نخواهد داشت‌‌
اتفاقی راجع به ایران قرار است بیوفتد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20151" target="_blank">📅 17:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ در مورد اتفاقات اسپانیا:
واقعاً افتضاحه، ببینید وقتی آدم نادرستی به قدرت برسه چجوری یه کشور رو نابود میکنه. این تصاویر رو بخاطر بسپارید، اگر دموکرات‌ها دوباره به قدرت برسن همین بلا سر آمریکا هم میاد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20150" target="_blank">📅 16:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ امروز در بحبوحه تشدید تنش‌ها و ادامه جنگ با ایران، جلسه کابینه خود را در کمپ دیوید برگزار میکند. به گزارش رویترز، در این جلسه علاوه بر مسائل سیاست خارجی و جنگ با ایران، پیامدهای اقتصادی درگیری‌ها، به‌ویژه افزایش قیمت بنزین و نگرانی‌های سیاسی جمهوری‌خواهان…</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20149" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حماس در بیانیه‌ای اعلام کرد با مرحله دوم چارچوب آتش‌بس موافق است، اما تأکید کرد که فقط سلاح‌های سنگین (مانند راکت‌ها و موشک‌های ضدتانک) را تحویل خواهد داد؛ آن هم مشروط به خروج کامل اسرائیل از غزه، تشکیل کشور مستقل فلسطین، بازسازی غزه و پایان همه اشکال تجاوز.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20148" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEW2_raCIng8pm90q8SxpkZgzr4PXxU1b5EXjuVcVh1MRTvDJQFpGxMbIjGKjc4gK1Q0b-79t9beactV61lgFFhYfZBPBC4FTH2v3eWdjgFkMSvAp7SuUU9d6PKMfCRXjgzqaz1fTUvBpp2vGcjnE5II2BGVoBuOgdfbM094pg-fise0vrOVbKPoc4QNw0a2hcWcBuZJc3NjvdLoTID3B4pJLsmdGt9aminmMu-IV-LGbECYu4J0387w1I9CoLZgjuSTTGAankjn_qmq_6wvhKSWn0_l6axTVeHxEA6Vs2bI3FTy46_45qpvApkrsvQfaHwxNT2vAHgMQcJIkMs03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر سند محرمانه افشا شده از تعداد واقعی ثبت نام کنندگان در پویش جانفدا  که 8,311,811 نفر بوده و حدود 2 میلیون نفرشون نظامی و حدود 6 میلیون نفرشون بالای ۵۰ سال و ۸۸۵هزار نفر زیر ۱۲ سال دارند !
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20147" target="_blank">📅 15:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ امروز در بحبوحه تشدید تنش‌ها و ادامه جنگ با ایران، جلسه کابینه خود را در کمپ دیوید برگزار میکند.
به گزارش رویترز، در این جلسه علاوه بر مسائل سیاست خارجی و جنگ با ایران، پیامدهای اقتصادی درگیری‌ها، به‌ویژه افزایش قیمت بنزین و نگرانی‌های سیاسی جمهوری‌خواهان پیش از انتخابات میان‌دوره‌ای آمریکا، مورد توجه قرار گرفته است. این سیزدهمین جلسه کابینه ترامپ در دوره دوم ریاست‌جمهوری اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20146" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر دفاع اسرائیل ، یسرائیل کاتس برای بار هزارم : اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20145" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کويت: از بامداد امروز هدف حملات پهپادی ایران قرار گرفته‌ایم , خسارات فقط مادی بوده
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20144" target="_blank">📅 14:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOWIHzCIOj7BGphfE9U6gI-Zn7dW-ySKuJquBSSQm_tuCTGffisMaioJsRqZOzljnMar15iYtbkNIRgoZCkAq6YbLoKqBTfNFUQFvtj0wWfqkECloTu1iR9JV5Xc-lAT47TTh3ge_cF4WYBp4jF_C4jN7cLQ1WMSZBqkMzFlerPuCUcp5rSnvQ5K3t-MwAe-K2E9HgnVqLExK73FlXUh8N_DjergdOKFT8YwPzWPa08v3pF1k_SgXlJZNDbDtdp-T-Ju5loTNll4Fkl4N4Z0l02L0XlkLS1_WevHOSxSGgHH9_LVGt7UMrtaEzr7-Y0Hj6TR4yVPSsjUuaNDwiwSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون تنگه‌هرمز یکی از کشتی های هدف قرار گرفته توسط سپاه
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20143" target="_blank">📅 14:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd52784122.mp4?token=TJ3OLlRuE4a2yzxkxOxrlKxME8vnn40CDVtXGk6A5rH5KypY439PyOxYDucComTUsn3LTmk-4JYAkWw3jM2Y2BRYvkmG7A2JX2yaFuFPnTAWxructUr_CaPvncXRvicwNJKL47Uq-fCQzAI-l2M8NfjSVeXLOv4fk9vhi2TXYSysWy9FMYVeNKf6vpeWU-quC9XqZnINX9AqYzooXAUj2jgqFCJ7ZiB1epzOL_IVcYRNtiW7sLdKL-DcG3XzmiNP71lmf_VjhrEcSybfV1vdrZ08TsXkDj4aZvRxOse430b-6vtUZGhBacGANxjZQUa7CWWuEfe1ZmeF1xOkADh91w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd52784122.mp4?token=TJ3OLlRuE4a2yzxkxOxrlKxME8vnn40CDVtXGk6A5rH5KypY439PyOxYDucComTUsn3LTmk-4JYAkWw3jM2Y2BRYvkmG7A2JX2yaFuFPnTAWxructUr_CaPvncXRvicwNJKL47Uq-fCQzAI-l2M8NfjSVeXLOv4fk9vhi2TXYSysWy9FMYVeNKf6vpeWU-quC9XqZnINX9AqYzooXAUj2jgqFCJ7ZiB1epzOL_IVcYRNtiW7sLdKL-DcG3XzmiNP71lmf_VjhrEcSybfV1vdrZ08TsXkDj4aZvRxOse430b-6vtUZGhBacGANxjZQUa7CWWuEfe1ZmeF1xOkADh91w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی آتش‌نشانی تهران: دود مشاهده شده در آسمان شرق تهران، مربوط به حریق ضایعات و فضای سبز در محدوده جاجرود است
حریق در دره است و آتش‌نشانان در حال اطفای آن هستند.
@WarRoom
یاشار : چیزی نیست بی بی داره آشغالارو آنیش میزنه تو دره دید نداشته باشه</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20142" target="_blank">📅 13:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20141">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085ee0b373.mp4?token=VQyCncduvlJU7BLHcE-gtyd-1R5NnbcbbZEXhQRs4Gj9Dq8vIrXFv1vwICN9fsLQWSh6q7lM3_Di3U9BHJas_jOk3PTzV8TlCgCChHI62NTk17yF1TT5FAyu9gywOjJyd6Iou2FetTBQJBqHvbfBQ9EnUzSF17hB-MXAsp_2Iv50CC-lwO9zjUcSaxTQtADwyk_U-hHNQg0WUGKUR8k4jNRN3Ltjb1y-BbJyNmUu3Hwac5oU4bXrMh4tKsCAtySNNVskOTOwW5d4KPT65JZSjdAkPRB1k6agQKcSOdticCg557ROAzNweuYF5DyL3hSRsPETZE6_-hKcq4inC7GGQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085ee0b373.mp4?token=VQyCncduvlJU7BLHcE-gtyd-1R5NnbcbbZEXhQRs4Gj9Dq8vIrXFv1vwICN9fsLQWSh6q7lM3_Di3U9BHJas_jOk3PTzV8TlCgCChHI62NTk17yF1TT5FAyu9gywOjJyd6Iou2FetTBQJBqHvbfBQ9EnUzSF17hB-MXAsp_2Iv50CC-lwO9zjUcSaxTQtADwyk_U-hHNQg0WUGKUR8k4jNRN3Ltjb1y-BbJyNmUu3Hwac5oU4bXrMh4tKsCAtySNNVskOTOwW5d4KPT65JZSjdAkPRB1k6agQKcSOdticCg557ROAzNweuYF5DyL3hSRsPETZE6_-hKcq4inC7GGQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران ستون دود بزرگ سیاه و غلیظ در پشت سد لتیان
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20141" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20140">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به گزارش تلگراف،
آمریکا و اسرائیل در حال بررسی گزینه‌ای جدید برای افزایش فشار بر ایران هستند که شامل «محاصره زمینی»
پس از ماه‌ها حملات و محاصره دریایی در تضعیف تهران است؛ این طرح بر اعمال فشار به همسایگان ایران از جمله عراق، پاکستان، ترکیه و افغانستان برای بستن یا محدودسازی گذرگاه‌های مرزی و قطع جریان واردات و صادرات تمرکز دارد، به‌طوری‌که به گفته یک مقام اسرائیلی هدف آن است که ایران عملاً از تبادل کالا محروم شود، با این حال ژنرال بازنشسته آمریکایی شان مک‌فارلند این سناریو را «تقریباً غیرممکن» توصیف کرده هرچند معتقد است در صورت اجرا می‌تواند فشار اقتصادی شدیدی وارد کند، ضمن اینکه احتمال دارد طرح مذکور بیشتر جنبه انحرافی داشته باشد تا توجه ایران را از اقدامات واقعی بعدی منحرف کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20140" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20139">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2xGmmIoG7uNewBRnGddgF5pVq9irevBsdVoYa0wvznNR2CoqMt7WhVbMhR_7lECUe5TyOAocxznQtyFdW8wM6VcUKLLWTTyabVPVjH_GT57oq4AOxrY008UZak6rD3Q0USRBIhBXflAhT0TBXkAJi-K_YhjgwU26arWQhzOIHhwHlWH0Kb4kU3n3E09LoUzV_qLSeJp_34dbtbO2L5s2HO3cTVoRiLOjLZA-tg1TH9xryQoirVCX_fXzKcLM0efCvT2eS4QdnhtJKfxOwx4RKPf2fP0-FuSg3vlpaxvBy0eWeSo9HOW7H1LVb53wOFklZzXWqPQt6kVUtbQFYi0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر سوخت‌رسان KC-135R نیروی هوایی آمریکا با شماره 8017-63 پس از ماه‌ها سکوت، دوباره فعال شد. این هواپیما در پی برخورد مرگبار مارس ۲۰۲۶ بر فراز مرز عراق با تانکر 0347-60 با شناسه «ZEUS70» آسیب دیده بود.8017-63 که با کال‌ساین «RCH169» وارد منطقه شده و پس از فرود اضطراری در تل‌آویو (LLBG) زمین‌گیر شده بود، اکنون با شناسه جدید «RCH564» سیگنال داده و در فرودگاه بن‌گوریون فعال شده
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20139" target="_blank">📅 13:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20138">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB5huxH64z_JspbNMQazfqkzROLJMExN_948OziXG-5-4JR72XbqZ_8tWbsiNGiN2vrZCYV3_2SZVIpM43iiEHT9b-jhbMAYYfh6W-EoVn_8lQtH1aEOYAyCXioGNYe2HY0yVAIAtzOd6TuKGD_IO1ZuhYglUNvgCixti1hLEWJqcsQxE13WWptLJJOr2idL0hO07ccEqzxyxryVit1X_orz0obZPMLxAwYC_HVKdRKp4ejyNQ7UUuEaIDZHrxB0fPm549yV7QSM-3ldnybXZqaPvomUSFGhvtDz1-_IJdobbzt2xyO1om9jPASjViAzbiaNP1Hiebrq19_8b9CGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اعلیحضرت شاهنشاه محمدرضا پهلوی و انور سادات، رئیس جمهور وقت مصر، هنگام تماشای یک  مانور نظامی در تاریخ 28 تیر 1355 در منطقه علی آباد قم.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20138" target="_blank">📅 13:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20137">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش صدای انفجار در تنگه هرمز @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20137" target="_blank">📅 12:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20136">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حماس بیانیه گروه بین‌المللی صلح غزه رو تأیید و اعلام کرد اسلحه‌ش رو تحویل می‌ده.
این یک شکست بزرگ دیگه برای رژیم در آستانه‌ی دور بعدی حملات تمام‌عیار آمریکا و اسرائیل علیه ج.ا در خاک ایران محسوب می‌شه.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20136" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20135">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/054d20c537.mp4?token=W64_3Ia5rkgQ_NY3ObJ86xnwSVtfTFusCtqrJ2ghpuUP-Hb5qKTDKXbtZKaTVO-jjc0CF8UziZ4muBdQhcO3EXoCTnRutuDQFvsFNIc8sDg06MINj2NsZ0ZbsKmDFh_738rkph3oEVxctj8q4HHlCFxEL-3tVdAzF1J46I_bymYZhYc8lACTELLLtwWxLVRzjn9qXLpZHO5VHQY4zyXIDzTuVt3bHiy5IO_JFoqiNqVOOPx05c20zxD4-1wnXSTt7j5YK2dE7lA4qsFtWc6M5feFLPNEG1_JfoPCoZid1D_n9gdM4fIzrWw1BIdQCTEjOih-MZTD2nSDXdlvR40DZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/054d20c537.mp4?token=W64_3Ia5rkgQ_NY3ObJ86xnwSVtfTFusCtqrJ2ghpuUP-Hb5qKTDKXbtZKaTVO-jjc0CF8UziZ4muBdQhcO3EXoCTnRutuDQFvsFNIc8sDg06MINj2NsZ0ZbsKmDFh_738rkph3oEVxctj8q4HHlCFxEL-3tVdAzF1J46I_bymYZhYc8lACTELLLtwWxLVRzjn9qXLpZHO5VHQY4zyXIDzTuVt3bHiy5IO_JFoqiNqVOOPx05c20zxD4-1wnXSTt7j5YK2dE7lA4qsFtWc6M5feFLPNEG1_JfoPCoZid1D_n9gdM4fIzrWw1BIdQCTEjOih-MZTD2nSDXdlvR40DZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال بدل خامنه‌ای از زائران مراسم تشییع جنازه خامنه‌ای (فکر کنم بیکار شده اومده آبدارچی شده)
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20135" target="_blank">📅 12:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20134">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXMo-rXxJ0o1IGYRIKlheY6632I1khoNkLR3Yu3I2bmACcxglZuKEmW9TYQ6A48-jt884oI5rxe0XPblRsRxLsDmiAC6SmpkUt5hMdQL5e4wsAC7N61jMockn0_De_Ni78hbjmox5LwV_pOUCuZsGY_AGzxVAGf8THkB3Xoq4Z73SMKDr8WnyNyvvDch_R_TJEAf5iGeyryTIkb9oPHn5QX9cVydZqG46z7fltu3IVe1Y6mHW5oJj60oTRjwY5dMnzg1hyjCw3R7qix6KTuIVaUp2d0vt8p6N_XjV4xH8VB79a1CKLMBGLbIWfSlyA0eiTBtn3OvC2DIfY0ey1Tc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایزه ۱۵ میلیون دلاری جدید وزارت خارجه آمریکا برای اطلاعات درباره شبکه مالی سپاه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20134" target="_blank">📅 12:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20132">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش صدای انفجار در تنگه هرمز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20132" target="_blank">📅 12:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20131">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانال ۱۴ اسرائیل: رسانه‌های دولتی ایران به‌نقل از یک مقام ارشد گزارش داده‌اند که «با اطمینان صددرصد» حملهٔ قریب‌الوقوع آمریکا به منطقهٔ کوه پیک‌اکس در راه است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20131" target="_blank">📅 12:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20130">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">باراک راوید، آکسیوس: به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم تشییع جنازه علی خامنه‌ای، رهبر سابق ایران، به این کشور سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکند و وقت‌کشی کند
یک مقام ارشد آمریکایی ادعا کرد که ایران سعی کرده حماس را متقاعد کند که توافق‌نامه را امضا نکند، اما این گروه ترجیح داده به حرف آنها گوش ندهد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20130" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20129">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce43f3e25d.mp4?token=tiRFAkSvTXPb1YAWKJZHlSUKuIo0aImpfK8tlKdwfDHVx0_JPxnJWpyauqBNDiBsysT9YpLv9dAWoEsnBmnhLTc2iZvi7VbEldmtP7zksrI6yGfbIvzf-AjMldzWIzJbZ6gkZsHF-T09aaifXiDoUqyKPE5aAf8nx5yHl3w4iIBkmtaUZVP320nCnPVR1nFMVWAF0Av1xTs3wMjvEqmf3kyq8tiw7Nyfecb7f9LXL4ZDeHt-lAAsr5FBxCTiuRA5hKdMYiOnfxFF8Ihzf2QEykyFl28asJm2g4dolbVC_c6VfCoAlXNpPgN_JnwAPXaevk-e08Dxj29g-0OvNccC0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce43f3e25d.mp4?token=tiRFAkSvTXPb1YAWKJZHlSUKuIo0aImpfK8tlKdwfDHVx0_JPxnJWpyauqBNDiBsysT9YpLv9dAWoEsnBmnhLTc2iZvi7VbEldmtP7zksrI6yGfbIvzf-AjMldzWIzJbZ6gkZsHF-T09aaifXiDoUqyKPE5aAf8nx5yHl3w4iIBkmtaUZVP320nCnPVR1nFMVWAF0Av1xTs3wMjvEqmf3kyq8tiw7Nyfecb7f9LXL4ZDeHt-lAAsr5FBxCTiuRA5hKdMYiOnfxFF8Ihzf2QEykyFl28asJm2g4dolbVC_c6VfCoAlXNpPgN_JnwAPXaevk-e08Dxj29g-0OvNccC0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون پرتاب موشک از یزد !
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20129" target="_blank">📅 10:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20128">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d722b8754d.mp4?token=LJJLdiIYgqUHCAdRCptp8lNY3etwAhrRkH_3ueBjVJNyZ1cPNJ9tUfUtwezXzdeyT0vdtKZt_RsNMXFRhOqP32JpMaMtsZooZoFRGODSePxHwsDz-gu6rN6lv9CvhBj0N7Qh9VsLTQPhObWvClVAhGAMsklTWcBdvoydTJjuDPEdxc_Z95bHCgqB7BNqit5yZb0rWN5V_ghsivtoCRFqx736_IzlsupwNJfd8x6XjOQRwLc4Y6uRYIYyHVQCqTU92_B948MP4xtAqStdLPWtOY7nqge-qnVPJ8pm6oIKSuor2WYaDoZMHY7VDBUdDBJAnOUT9xvx9p780-zKvwsiuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d722b8754d.mp4?token=LJJLdiIYgqUHCAdRCptp8lNY3etwAhrRkH_3ueBjVJNyZ1cPNJ9tUfUtwezXzdeyT0vdtKZt_RsNMXFRhOqP32JpMaMtsZooZoFRGODSePxHwsDz-gu6rN6lv9CvhBj0N7Qh9VsLTQPhObWvClVAhGAMsklTWcBdvoydTJjuDPEdxc_Z95bHCgqB7BNqit5yZb0rWN5V_ghsivtoCRFqx736_IzlsupwNJfd8x6XjOQRwLc4Y6uRYIYyHVQCqTU92_B948MP4xtAqStdLPWtOY7nqge-qnVPJ8pm6oIKSuor2WYaDoZMHY7VDBUdDBJAnOUT9xvx9p780-zKvwsiuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس نیور : آیا می‌دانید چند روس در این جنگ کشته شده‌اند؟ آیا تخمینی دارید؟
زلنسکی: کل تلفات روسیه ۱،۶۰۰،۰۰۰ نفر است و حدود ۷۰۰،۰۰۰ نفر کشته شده‌اند. تقریباً.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20128" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20126">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78bd5b2c6.mp4?token=Y701Fgf7qRuZjrd0GZQqRPgyHpgkpOs6RdPLASz0HibM2RGN3SAlb82jHsESzN20SdP0TEdMcoIPrf9XkahTMyBcr1lu_IdL97kumNzrGs4H01G3YMaQe_ZLz76z3u04NHMTwVe6GJXkOyKkqUSa0vZ5dbkqHryaNojm-gxH9SKIc52oqa4Rt1Zy0zzhz1baB8Phu0sx-qMCvqTc6Lw0L3Ai_2YQIQa-spMZPCFERlcVYLpmdo3MXCKN-rcXXi873ySmLwDvP5E4MdnmnHVdfX3q1NRYiQaOV7goqULW6sZ3hLLd6mdx9OfOQ_4urEd6pnfwisyJk73RFUbZ-vM_kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78bd5b2c6.mp4?token=Y701Fgf7qRuZjrd0GZQqRPgyHpgkpOs6RdPLASz0HibM2RGN3SAlb82jHsESzN20SdP0TEdMcoIPrf9XkahTMyBcr1lu_IdL97kumNzrGs4H01G3YMaQe_ZLz76z3u04NHMTwVe6GJXkOyKkqUSa0vZ5dbkqHryaNojm-gxH9SKIc52oqa4Rt1Zy0zzhz1baB8Phu0sx-qMCvqTc6Lw0L3Ai_2YQIQa-spMZPCFERlcVYLpmdo3MXCKN-rcXXi873ySmLwDvP5E4MdnmnHVdfX3q1NRYiQaOV7goqULW6sZ3hLLd6mdx9OfOQ_4urEd6pnfwisyJk73RFUbZ-vM_kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور گرفتار وی آر شد !
عادل : من دست بوسی نمیکنم. آخه چرا باید دست یه مسئولی رو توی‌ جمع ببوسم؟! من اگه دست بوس بودم الان داشتم برنامه 90 رو اجرا میکردم.
ما این فیلم رو آهسته کردیم که ببینیم واقعا دست رو بوسیده یا نه. دیگه قضاوت با خود شما که دستشو بوسیده یا اون لحظه به هر دلیل دیگه ای یه لحظه سرشو آورده پایین که شبیه به دست بوسی شده.
نظر شما چیه؟!
دستشو بوسیده؟! یا اتفاقی سرشو‌ اون لحظه آورده پایین!؟
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20126" target="_blank">📅 10:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20125">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بی‌بی‌سی: یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه IRGC، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20125" target="_blank">📅 10:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20124">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک مقام آمریکایی به رویترز گفت که تهران تلاش کرد حماس را از پذیرش توافق خلع سلاح منصرف کند، اما ایالات متحده ادعا می‌کند که بر فشار ایران غلبه کرده است. این مقام آمریکایی افزود که سمت دیگر اگر اسرائیل هم این توافق را رد کند، رئیس جمهور ترامپ ناامید خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20124" target="_blank">📅 09:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20123">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e9526a12.mp4?token=PcAGxo7F8_mTZgb4-4GzAlxjBQ53iF6uSn2EVBySuAon7LjiwOzNui913WdkmM1JwllRW-TK60cg9_bXzJiHMduTYnkmFcG7pf1YadcI0T8i7uQjfEsBZZez6PWcTGy5yOpFjZhHC1ztrtokJashQrPHCKbew17n9oFm5toioTSbpQWaPWzvonrTaqXAtaIK6esH7LpH4AqcEk6iBUHq_RlloU8w6B44hyWIyipgvhw1KsC9QUVt7ANmTvxp1942aE2dBS5Qt1oXYT7bjh9Zit3sPYNr6gnKm8teVjUxeD7aIyhYLFkBz4CvhadJtvl9ZMEUCrCBAfm2m5-BxJhmiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e9526a12.mp4?token=PcAGxo7F8_mTZgb4-4GzAlxjBQ53iF6uSn2EVBySuAon7LjiwOzNui913WdkmM1JwllRW-TK60cg9_bXzJiHMduTYnkmFcG7pf1YadcI0T8i7uQjfEsBZZez6PWcTGy5yOpFjZhHC1ztrtokJashQrPHCKbew17n9oFm5toioTSbpQWaPWzvonrTaqXAtaIK6esH7LpH4AqcEk6iBUHq_RlloU8w6B44hyWIyipgvhw1KsC9QUVt7ANmTvxp1942aE2dBS5Qt1oXYT7bjh9Zit3sPYNr6gnKm8teVjUxeD7aIyhYLFkBz4CvhadJtvl9ZMEUCrCBAfm2m5-BxJhmiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای اخیر، چند شهر اسپانیا شاهد ناآرامی‌های مرتبط با مهاجرت بوده‌اند.  مهم‌ترین درگیری‌ها در شهر توره پاچکو در منطقه مورسیا، واقع در جنوب‌شرق اسپانیا، رخ داد. این ناآرامی‌ها پس از حمله به یک مرد سالمند و انتشار ادعاهایی درباره مهاجر بودن عاملان آغاز شد…</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20123" target="_blank">📅 09:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20122">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مقامات اسرائیلی و آمریکایی به اکسیوس : ونس و نتانیاهو عصر سه‌شنبه در یک دیدار دوجانبه در واشنگتن، گفت‌وگوی «مستقیمی» درباره اختلافات خود داشتند
تانیاهو با ونس درباره انتقادات اخیر او از دولت اسرائیل گفت‌وگو کرد
با وجود تنش‌ها، طرفین سعی کرده‌اند روی «همکاری در حوزه‌های مشترک» تأکید کنند تا تصویر هماهنگی استراتژیک بین واشنگتن و تل‌آویو حفظ شود
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20122" target="_blank">📅 09:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20121">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در روزهای اخیر، چند شهر اسپانیا شاهد ناآرامی‌های مرتبط با مهاجرت بوده‌اند.  مهم‌ترین درگیری‌ها در شهر توره پاچکو در منطقه مورسیا، واقع در جنوب‌شرق اسپانیا، رخ داد. این ناآرامی‌ها پس از حمله به یک مرد سالمند و انتشار ادعاهایی درباره مهاجر بودن عاملان آغاز شد…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20121" target="_blank">📅 08:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20120">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ: مطمئن نیستم به اوکراین اجازه تولید موشک‌های پاتریوت را بدهم
این یک سلاح فوق‌العاده است و باید کمی درباره اینکه به چه کسانی مجوز تولید می‌دهیم، احتیاط کنیم
تمرکز اصلی من پایان دادن به جنگ روسیه و اوکراین است؛ کوشنر و ویتکاف، برای نخستین بار طی روز‌های آینده به اوکراین سفر خواهند کرد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20120" target="_blank">📅 08:43 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
