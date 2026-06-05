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
<img src="https://cdn5.telesco.pe/file/DXS4la6HD-4NjPxFR3uS_9x919RdS_T4AckDu0wBxXbpWodE89S1KxVBemTkNMEkXcea2iYxycwHiMQte_BKdUCzbae-qZnWvpF8aU_i2GMubgOudoorEX525is7kGc86tPJJC8jfO2VgY-hDA5Le2x5GYP8itWgQ24WNcjMFaQ_7fEe2U-sDNQZGEzP3po1m0cZQVDU1vRXFnv4fCdkvYhKyC_-VZ08eOZXbV7KLBBcYscDSctEgo-0UNpMkEN5slVt-v4YIM9Up7L6YtXkbCIWHaOU1xZkXIiItTZTXkKN6ZvIPp9bqY_hd9YEfu42-kRr7n3ttar3w5Yr1gqWNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 193K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 20:29:14</div>
<hr>

<div class="tg-post" id="msg-91070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aphckmaqQcnm5otirqOPAlWPQKVLubxU4Pw9uf8HjIP3E5Bj1Zxfu9xA7-8dAb2K4jZeQK_n6IVphyiXcZFECVHAZeorrMMarWfos-Ly-j40Hp6U7mm-tT5PX-iiGd633BajviQeZuEZ4_OK_KH3RhDR0kAP1hdxj8G0T-Pm2gwVR90WQtUIMsLQVtQBH0i9dUdnRnH639AZsfrD1Z_Jj_W9dvCiHAPG8rOkPSr7VafaLmNcPnzzCi0XpwKfq0NzZ6I_XffOOftbCrtYDf5hA91c8QN5ZjGO9G304IOTf4GO0OM1gzi2qbMqWCyrj9ZftVSTzcJ8FpbCgrpOE_alMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یا وینی؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 921 · <a href="https://t.me/Futball180TV/91070" target="_blank">📅 20:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91068">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6A3P8CPbe3-oKuDO8fw4HSNtKW73Y8h3ndNjBLB6I5xaY5xGS9AC-UNwtxFJbcm5L3A5uo1_oehh7khC_WBQuyrptvie1wHKfgthH1wXZpd6R7U_AoMY_VLi0zAKMoOzRkuPxM2RKGmxBb8UohUuNHBIQj1tAAVYN9zxdGhufwMi0B9z-dnf4OHmqGNcde_7PFLtgYVrOgLLUKmkV5yIafQTsGDybE5bRPAjY3oycUQH0quhl6Cjaht4jmAfdONZyEvayysoSzbdt8fhMxGhxkquq_rwPKNn49mfMrP2qSKgZpGVhvwYAkosLWxDp4Ns6IZBx06108yAG3XWGrX0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMEkrP6a75pYAysLaGAaq-rguqZrCXOSI6UXQaE_q93HVJWdOq_RMXv_dysnlbXbX1rahrUN5Z4Kwhg_PKZHy5TFRwZBgzWx8rE2NbOFlHhsjyj-v0bdIllZntEnF6YFba4UzDgTD4jrihS8am694_wlXCnvQby_L3EfwIMz2pqWRnkF5a1pKea_nuO7__K7dHGr7YqfxztMjeSETHu1JPUx3gPADFnp_NTsVffh_8hSjCINbP6BtYuLGXWK9XGDVRrc_Dlex67bWU6igmGMhFTmjXbrJa-33Bt4QWk6dF0ujzGZEp9b3yqJ6cl-mzLLE2JT5n3nBi2BwxQgFRpdSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز همسر فرانسوی انگولو کانته اعلام کرد که توی دادگاه درخواست طلاق داده چون فک میکرده طبق قانون فرانسه دارایی‌های اونا به طور مساوی باید تقسیم بشه. ولی مشخص شد که کانته هیچ دارایی‌ای در فرانسه نداره و املاک و ثروتش در کشور محل تولدش به نام فرزندان دو قلویش ثبت شده.
حالا کانته کسیه که حق دریافت سهمی از دارایی‌های همسرش رو داره. وقتی همسرش اینو فهمید سریع سعی کرد تا درخواست طلاقش رو کنسل کنه ولی دیگه دیر شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/91068" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91067">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap3Ol1pMRuatjxgNk2u5xTY4OHtKDabYo3JlOZdkFVNlnZ6iCwel-a-jJoB4a3hIf4DjPg1QngurG-JtR7FvZ0jghbXobFvBpfIRJTPwySWRZg2JxygI7Hy_J-JqEva38fHf7R1Bp851Zvn8tn0cKGQ3RJoW0tIiif-M3km9MoytkSyiXqDrNximDKlIr5cSAuBuo3HbgC_RcV-GY3fU1Xj2Tkps_DhediqkgwW5eJOmKV9XL79VyIEsP7HF4GGVuGW6130ed2FICmifO3devkvldbKx8b17k9pYwLeD2nDR6Vd76Sf0Zdgfb7WzG98UOL_eFu5Acc1oVCurDaHX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خیلی هاتون پرسید بودید به چ فیلتر شکنی وصل میشیم !!
🛜
دوستان تمام ادمین های چنل ما از اینجا  فیلتر شکن. تهیه میکنن
🤩
🔋
حتی تو زمانی که اینترنت ها قطع. میشه  فیلتر شکن های شما کار میکنه
🚀
تنها جایی که مورد تایید ما هست و  پایدار هست اینجاست
👇
💎
سرعت و پایداری. عالی
💎
بدون  قطعی وکندی سرعت
💎
قیمت عالی و بصرفه
💎
پشتیبانی ۲۴ ساعت
💎
حتی میتونید. تست رایگان قبل خرید بگیرید
حتما یکبار خرید کنید. پشیمون نمیشد
😇
🔋
برای خرید از ربات زیر استفاده  کنید
👇
🤩
@irans_vpn_bot</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/91067" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91066">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F384hMYZLKCC_-DcridnrbhhaYTZkZABmGqm6p6Rbbf2JqI1t3nnVrPZfxHThmo0Rx1eKOxgs0ACp5LF0F0X6xd0O_ziD1lTu7pKhwJ7Il3BkNBYoF84gYXTwzx9_LZbzHus9-jluA9ftQssxOVaxWAp002mXmkLLClztXXK4imq99UIFFifV8iljj4EVe69ouLMFaBpFNj2DZ7OkRuxWy99JGG1DPTT4r5UgvFshOJ7JwhIjyiw43sJ6jVwVsG4ccChJ1eQDkYZBenIJ_EuMJI-ThBeMAD775CFHtxSOU6Rx65eMG1eg_LUlfMQvXD_pZ97VkmYx-0NXE7NZAWOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها. طبق این مدل، هر چهار تیم مرحله نیمه‌نهایی از اروپا خواهند بود؛ پرتغال انگلیس رو می‌بره و هلند هم اسپانیا رو شکست می‌ده، تا فینال بین هلند و پرتغال برگزار بشه
🤯
🤯
این پیش‌بینی چند شگفتی بزرگ هم داره؛ از جمله اینکه ژاپن تو مرحله یک‌هشتم نهایی برزیل رو حذف می‌کنه و پرتغال هم در مسیر رسیدن به فینال، آرژانتین رو کنار می‌زنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/Futball180TV/91066" target="_blank">📅 20:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91061">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7uoM7b8AQU-RQvYFA89JoBXM_ky2z7HRAwnqVDeJ3_gK_2LCNdt0R-Y7Z-4OGwAD-g3mczkTKsYL_1h2789ntbHyrNWzuBSZeIsLjKJipBkOQxDRCQ7Wyd7Y-_uKk-QzJkwUo57dCl5958-WzAcE69V4RnuIAB6W25tNvHeuAc24wbAqT98OHZSM0nchQPvSy3LjCzTSJK8WDEJJ6ZiqlVABXNbBxstKjTkvWfbWF512LQIholBcsNnZ5hdSc-qmGxMmcfIROXSFsX4_K-s8mntdWzxooqjrYapnJVC7cClLYV7NPn2ft2D0uHqUo1m-Rf9cpbSPQjno1MEuvva-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-JlucDLONmNQ9VhS5KOWCOxHCWoRkqMheosxtaU6RMYmejwbe4AaiUFUoQal8HzKlGnIPyiqdGnALVIjW9W2mQ-hjNDbXnr5D49dhR2Yxp-EfIHLsbeMZRyxAiNL9UosYEXWOYG1oxec_8bFPpJrNe2f05o6LUomi5Vkxd8zbPlX71Fv2uuxCaVuslAazMqojIqW5puqb0safU5dGU4-FCXiL4NZBW6Lk23SezglFEp8dZQ_mcNO-IS8zA3KQjTZzrShrQ04LlikXcKJ8fs20GuviBbB377V26UYlXUgMUDYX9h_UHYvorXR4CUp_8vFD-pEmrpTTHyQ0fXE079GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miZltfdfdHugk0inuA3dGJ4rH9QH9KrYcq_C_S-g_tHMc97e31xpWQ4ESrYbVTv2n9DyJuSk9sY0Dhssnx0y8ZyImnaRjLt9UJoYaXEbUBV4XcVkOnIKeajWJRDHTWM8-DK95VGKDrNUDFLVaOG3TIunRGjLv2iO10Wv-Qw2RKLB_bSD5QzqKTRaSl326A5zZmoPtEH3zAEZdp7GRFYCyEl3c-XDkO2VoKWl2MCM514s20vSdA8joG3adIKjdITd-8kQ-ezu1AvknI12sz5NaIoiZEG9n7BNz-foAD0D5iysaNFkwB5WRUs8OP6zypyo4M6ZS7Iu7LNVVwWPywFLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5Vpd_FTwhxARr5QGPi-J7jb0qJUFpQ2xQbCGmtzOkpBSdE78jwEMCpFBSmg1kni0T9Ty2pwrNUDYlq7XsRCLDmMoZ2EQ-PzxBKpxEi3H6-QgAnihkmHQWRElhK4pvSHAjgn0n3f-RzogLXUWrSeosrTs8tgPYjexWEqU2fHwEqNmQ2jG7n4rCiSKXzt4lK4nOZGlvjn83HttBJZyMCgmAq_AWWtsIP84DxWWUB-TIskzX3zTEDE25CiZAPOtYI7n5gLQYWFEDKMOejWRqBe9KglmYCbWLUAXAnEG2wYahTk3Amg5jdu0QRv5FU-Or7QiMRjC3cQHdBSG365hKSJSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
#دانستی‌های_جام‌جهانی
💥
با کلوویس آکوستا فرناندس، «گائوشو دا کوپا» آشنا شوید، کسی که در سال ۱۹۹۰ شغلش را رها کرد تا برزیل را در ۷ جام جهانی و سایر رقابت‌ها در بیش از ۶۰ کشور دنبال کند.
🇧🇷
🏆
وقتی برزیل در خانه با نتیجه تحقیرآمیز ۷ بر ۱ به آلمان باخت، یک عکس نمادین غم عمیق او را ثبت کرد. اما به جای تلخی، کلوویس کاری غیرمنتظره انجام داد: نسخه محبوب جام را به یک هوادار آلمانی داد و گفت که آنها شایسته آن هستند و باید آن را به فینال ببرند.
🕊️
🥲
کلوویس در سال ۲۰۱۵ درگذشت، اما میراث او زنده مانده است. امروز، پسرش هنوز در سراسر جهان سفر می‌کند و کلاه و جام او را که نشان تجاری‌اش هستند، به همراه دارد. عشق واقعی به سرزمین هرگز نمی‌میرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/91061" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91060">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👀
#فکت
؛ چوآنگ تنها بازیکن تو لیست 26 نفره تیم کوراسائو هست که در کوراسائو متولد شده و بقیه بازیکنای این تیم توی هلند متولد شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/91060" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91059">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdHNBeHy90jzZtq_Tz1jDDsgiyN1Aft-tfw7SP-v5caKRyTxKOwe0rK_zA-72A0rlzMK8AR9imJrh6V9E4dZWuFx75blWTNb0mxCL0C1iCLaidDDuGEmNQtIp5krNr9iUfKci7kJnIC3uCgE2AhfZ1HoP_Qsy6qM1QeND-YtvFtPcnbAne6XaIDL-Rf_sfDLypfO29omoCLAaR4I937qFqXgeRjwkRU3KFs6iOe7bYHB1hsGtvJHZI8LbJ9nJfPcZvqowrynK81LiALYBshQ8bm-B7vqT7xMY24AoUNGpWZNmLMOthoer1JwtStGfhB8CfBR54CdJ53R0O7IOTSqwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارتین بریتویت (مریخی) 35 ساله شد
🟠
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/Futball180TV/91059" target="_blank">📅 19:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91058">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0-AG7McBPMdLRv9WvUSaF00mxY8vYyAP4lDdfXKI_VaZjN03aEDyC_oYQ_unY6SdfwGisAqXTMwTiKCTir6w3mHNOpUnDratlBoUx4SibBi2IN2HCMcF-pNKWbGujVv-_jsTmlVDOAw77yQEyE0AFGeJnkiS9wxvZGL8JzJa-fzFbcv8_zlAmF3oSgI2lzMcsnirk4QBJYyipmHGnOQtrVNCeHORA60BYPK-E1P1Dya6mLxazvjZ6ifPqq-vUbghka7NlAaIWqMCn09rni-5S9BMk0vVcEsDa3QR6nQkcEt9HNcz_Adv5kK2xMl9djF5PIfRfYzN23w1a6DTgCU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏆
تمام فینال‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/91058" target="_blank">📅 18:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91057">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fZTntVvx8S-Kd6RuktWM9LzF9gsOuIgcE4Zz2b_tMFI7MBLIyXrtdcclj8kTXb94TeSge-LWAqFPpykik7EKGYSlqtjYx-qBESsNLGAXtVdPMlWnCyIPzrWzkMrxLUjzUagRGBbKHlDpbrxzl0OOfsuzoycX0kvIE0Y1rbnlsZQPtxDQCdchTQhvgwWrpnc7GoBOJ7yICrFvmYmiRWs3hG-jHVIxjV0bi7hRHPjvd-ygV2J97oceqIZtLyj7FS-huzaeF1mvvQi1UlXKjvrc62G4BeWb8hwfC8nbmsZdfe7bHzPDHS_TrSNXxF1js2oYyXPhMS3aDANf4-rpQcLQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب پرز
گفت بازیکنیه که تو یکی از باشگاه های لیگ قهرمانان بازی میکنه
#بتیس
گفت بازیکنیه که هافبک هجومی بازی میکنه
گفت خریدی مثل رونالدوعه
#گاته
دادم هوش مصنوعی اینو بهم تحویل داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/91057" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVB3qOm2gmblbapcme6IAniEPl9nY-ywYYqRE3ArH8rwpsMXk9HrWLo7D5i2U9_GIUHHGG-jaiiNLES9NaSeTTAW_TPRfVMD-_84clrMLuJtDIP2F-5knP66IpRGvXxtVr0vayM8n75igDtxLFfjSgOU1GdaLMT8vPEb1MsFb5bo0au0ClaHJN9zqPy16PslUUo_rAcgcTJczDdXGxHv98nUXPypUPiqrxv-GVONJzk8W_yUWWo6p3b0Wk0rPt4sPtykegVEoqk7l22xyYeJajynd0jzehrYrYL2AbX0KyoqonML2g5yeYVwGxjy1vEDTLkGjHcGfi3SJlX7pBW9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNt3scJKMfOMzOA3BvurucTfsb1Aa1hqs13WI2qpX9kiKYlIr-eqntjPjL85TDnqbf6BSjOcobeDl2VyIgjCPBwHlxx5QczkyCxQqVCipI9iWUf8_rDY9KMEPToH6P9dkTpkCQZVIuNeisNeFG4qNUTjT5K-pcWo4iuyd5VOUazjqLGrbAr_mxGu-oGRNCxJqzWIxwooZN8jIZwbE5XIUpBlcqNGTM6wg13QSQvzsyz1uMzv-Z9aND1nsvfddQpsQtGKGiXT-PZMLYfZBAjgkape8jjfGuGlACs_iakr3iRWT0x22lhjzTelw3_TMavP74JbmZmwZA7HQ6lJ5U8qyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوسی که هم لیگ قهرمانان رو برد و هم زندگیو..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/Futball180TV/91055" target="_blank">📅 18:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=mKLnBm1HGIsuyKMCM0CF7ANrJKKXI5Gq1MnYFMmFj9n9AFE56V_glBfUA8KylcxrHipendiRiFicZUJ6yswKEWtZpOZBJMw_fMpDEmH4Y57ffdi6sk1T-tz6ndxwg78Tz5oa68NDxb_9lT-trEmvaM9IRT5gAR0BaZSBKHx-cau0lNEnNj2lvimrUJVRbl0V2PCdA3C8_8-eoCJ-t6bynzBwKZCkO7keYbFm91LdNSgcaIUgnsaAKsQ4w_wpLyl9TxxnA6-fCENvjYA9LqIEjZiurMxighdU55Lt5W9vbuOyLFqlisNJD89TJkAfXwHzV26Z-knGz5SCBA1wZo7s1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=mKLnBm1HGIsuyKMCM0CF7ANrJKKXI5Gq1MnYFMmFj9n9AFE56V_glBfUA8KylcxrHipendiRiFicZUJ6yswKEWtZpOZBJMw_fMpDEmH4Y57ffdi6sk1T-tz6ndxwg78Tz5oa68NDxb_9lT-trEmvaM9IRT5gAR0BaZSBKHx-cau0lNEnNj2lvimrUJVRbl0V2PCdA3C8_8-eoCJ-t6bynzBwKZCkO7keYbFm91LdNSgcaIUgnsaAKsQ4w_wpLyl9TxxnA6-fCENvjYA9LqIEjZiurMxighdU55Lt5W9vbuOyLFqlisNJD89TJkAfXwHzV26Z-knGz5SCBA1wZo7s1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
على فتح الله زاده درباره حركت جنجالى با محمد حسين ميثاقى: چاره‌ای جز این نداشتم که بگویم آبش را بدهید آقای میثاقی بخورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/91054" target="_blank">📅 18:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt4RW7olhqfVD_mVNUe01ya8Y6d7SW6VtsVSyswS1KRDKpJYqU0nz5D2f7B5XMr_yQedomd1zhVcRnS7ir3S1y_7kUXMTBwktkgLCYpvHAd8X7gNXCu9yFXPpSHuH3lopEJcQ-L611JCUqAQgLkQOJsmT0m4649BzeqkdjO9meoB4M5o_aEDGOigogUq9g9K18K78PgtO96MDceKUNCVy-Z8j2lh8NGrYXbXNamvZqlj1p9x9I4cbQ5y5ZxhIyRCzSw3Ga17qAL317niQYVP3-0x_Fm5obkVMeAtJTJI5ck8XaY7J5C_zA0i7xuHywc33Hcz5Gazko-kRFiaPZcKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/91053" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91052">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEaye0KnzEWVHmfc1S5055vVlw6iHTultptwEZbxyenmMnfXSyjybKugfql6_KGNR5hvcVXEOcpntlx9XT2XE2stTl5fwU4mJWegsNymhmJEpFMFVA60z8hjyvZg1270jnN0cwvzEv4n8LDB_2hxgmI9xsudVcvaQCyJl3wj0y8zzSFofs6uAZgTOSwHOZHfrFsjdKC34rTFQZhVEhKmJZvBnJ8SkG8Uj7EaFwvJ32MC_Kt3_f4jZSYfVfqsYJ5ITFtY8DpITfX_jWtd5uVSRqiv2OO68S5C-zGoiY6JkktvBBJdXptx12g1OeF5uXf0ugEGY0P2pjehrfzFfSjyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی قراره با این استوکا تو جام‌جهانی دلبری کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/91052" target="_blank">📅 17:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91051">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
رومانو هم تایید کرد بازیکن مدنظر پرز اولیسه است.‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/91051" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91050">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=CX76g_PaqvQPYhXosK3mvU_5aZHKpgqn6cilYre3EPzoHzRfr57XaUgeW8l3u7wlsyBBJKFpLrAmk8j6tJeOTHVHq0-H7TAJmimzIxGdy_iD0dFbPbrqrFRHa8uZyiu6X7TdpTx4h9-YqfDvjVm9NSR-AfnrtdfdYBqrFVThzMt-Z5h0ct57HMN172vNEVOHXWBmYkbzxM0bM0jYetAyL5oH1ldnAJ5vW7iYtzuTMDSdXUdHS8PyUg5C8dI6j0uEysWuyU5Uj82OzJiGvpooQIonTukIr0PMlqYD8PrzjA4oVTBLhBXoPpY2B7vqt9cJn2MGE1Kkc_0EnzxmQbSUzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=CX76g_PaqvQPYhXosK3mvU_5aZHKpgqn6cilYre3EPzoHzRfr57XaUgeW8l3u7wlsyBBJKFpLrAmk8j6tJeOTHVHq0-H7TAJmimzIxGdy_iD0dFbPbrqrFRHa8uZyiu6X7TdpTx4h9-YqfDvjVm9NSR-AfnrtdfdYBqrFVThzMt-Z5h0ct57HMN172vNEVOHXWBmYkbzxM0bM0jYetAyL5oH1ldnAJ5vW7iYtzuTMDSdXUdHS8PyUg5C8dI6j0uEysWuyU5Uj82OzJiGvpooQIonTukIr0PMlqYD8PrzjA4oVTBLhBXoPpY2B7vqt9cJn2MGE1Kkc_0EnzxmQbSUzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
🇦🇷
فینال افسانه‌ای جام جهانی ۱۹۸۶؛ جایی که جادوی دیگو مارادونا و هیجان بازی در ورزشگاه آزتکا یکی از دراماتیک‌ترین فینال‌های تاریخ فوتبال را رقم زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/91050" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUm9h5Ds6ruhpzNTEhL3F9le8bgA1Qy6kOZm6kSB83jKDRSC-xR0QzLRw809IzlV5l1XGKEVk6SqHwDkntUcCoTwld2eNKWgfrWoGrraZDqYkxI112D_otR9ku4NxKnIFPy-46Tp6Vzs_o8HZGrq8adGENrFfVcl0J4wmYYolLbf2ElmDMJnMgFy1qSrRqOWeEO8zfocUtIdQmESukzYSM_zorTP98nOGwZLJDoITTrGdtmB8ZgGDno-X1D84tTMrhAkhkVxoYihp40_zFLG7g-YNd9PXjJxrAWgXPhRGbR7DDGggJzDNWPuiV4fYJwYEgS98mYfe5QkbfnUCfcOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/91049" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91048">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=JW9tYPPytyHz3OnQcCWfKTYgQhsEWeDQlyrB-E_XSRJWkWJJ0QUqIi97B-U7RuvB8I5V8hPQvsSpIMs0JFQvWeEuwgRuXjNmN3rD94sZk6eshCWsLObQ61441gCw2eM2L4q62KarrTc7cpgAWYUOLJwCwiMVKo56Sv-z03LxHFDiQ3KfLstRntsfe7Hi6p_JuC6ocGVfer9RG2tOE1RyEyruho-aos5-o7eD0RnOfG7V27LlY6pUoZdt98aqqwE_VdoKqsGfpf-3JqDSJ4B8Lpx_R7V1lpTaT-BQnYF9qjDhw5hZ-9Ehaou97JY-4sCgjvBF8u_11vaYZ-73ESw0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=JW9tYPPytyHz3OnQcCWfKTYgQhsEWeDQlyrB-E_XSRJWkWJJ0QUqIi97B-U7RuvB8I5V8hPQvsSpIMs0JFQvWeEuwgRuXjNmN3rD94sZk6eshCWsLObQ61441gCw2eM2L4q62KarrTc7cpgAWYUOLJwCwiMVKo56Sv-z03LxHFDiQ3KfLstRntsfe7Hi6p_JuC6ocGVfer9RG2tOE1RyEyruho-aos5-o7eD0RnOfG7V27LlY6pUoZdt98aqqwE_VdoKqsGfpf-3JqDSJ4B8Lpx_R7V1lpTaT-BQnYF9qjDhw5hZ-9Ehaou97JY-4sCgjvBF8u_11vaYZ-73ESw0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/91048" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91047">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/Futball180TV/91047" target="_blank">📅 16:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91043">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_faNCsC2ivHnZla_mukdk5hPg5ZygSbfS-M1NslFGUTig7WhsKiuqKX0-sHxx2Mi9zTpG6sNCJYNssEONMuJIGT21TRLZXC0i4w0z__uqjE9gPHFq2Mg67vZLrrF8Kz1TuhLQhyo5u_mIfaiy2TkZlql0SD46LGyLy-UK4JJyRgdKVO9hJlnT4Z6kk7MqYtAiIEd4OTipw96Ff0BsDwEY5Q66QcmJ-tGoesaEtaHua5rbe5FuRKLKd6QOCmfYvJcUaoUXegJokEVbe83TQlOOz0DJ4XDuPlSVcduodzEjwLITu_OV7Ny1mcWRD59CK6Mz7eB09qa3XPZIzf-o47Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDVo76YQX28_xVZSsSGVEezzgssvJ5Y4GNYxjMTri6NMM88tG4QlOI99TrMhB1epakKz5q6YS2nxj5PS-yj7k00hST9_SwlfikBW58PX-uP3KG9Xtaspe6JVHtzKd6G1pRY8dcU0s0i-HpVD1wVW2GycyRDr-HBz1Dr1p1zXQZ-tugWpe6kVXz6X3mB17kOFlkCg7mE0IRSm_mvkwLAlYEJw6D7Ls3BWm-3NEby_7th_jrBAsYIMGEQS9ODiS9zGDRaGhbQm6e-vZ8-1lKy4QbKiX362TaOuB6sqoA74bbrMGmnIKNyL3_r3ekQg9R7KRvWiQKdFTy1rjd6vxDXQSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joTnyOdphdsnuEyQ_6Q_o09csT6vF3qxvx8ooVKT8wI7XrDGIS17hJTOOWh9xc6YEBf0UC2sxjcUaiBDJiD7xINyis0s8XiSzr4dTe3acD7wslgotg-MxvQjnKsqjCk55OYE9yspb1xcpko475yg124awObyojXb2sNle0ECtcZM5XFdr63_5AmXNLjC7kccu4lDO-YYMyeaYXEs6DjuFh9s4kIat_teoB1ue0IqFGdvXYBdZK9gwpoRnccKVvSOqOwnuyln0Xq2954kW2mfNmlzpzLLKjUDB0MWwxbF6RTFSskjIP3axAY0748RBUwjDzihGVGNouSL7ktl9Sq_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8frmYVv8FV-xuQHuyjGiIcWEFLAH4dT2ohBBpR6Hj_PQTBsPnbTCUBOKAQ8iw0wttOt5E17PN-6kdn3DhYYI2bWeYqqkIUbyfNp13NLYzWpEbZuOS7TQuKBCcxIrMeMUoHSND9kwU5eWR78jIdJ37U0HnkIYze0mHNftbyEND76qxiNfLJffkJsIg_VIyBV4V4DvRxxH_TV7dzLGiyl943i_MPlfIwtPOSXf6buXmjd0hRUlAtZXGwDmu5eM7ZpPZdLzxN-H8LQgXpcFKEei9_jYSvM25JyOW77B0pVNLd3Gwfr47YTbtJqvO2a1jNIRTg3NdOlOeBME_q1cmpGdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت بازیکنای تیم ملی نروژ در آفتابِ آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/91043" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91042">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmgEZReKv7SpUSwBuGIRPbAMlS_7OuqZe3t9O_C2JQFEu9x0pbWCCJwG852cl5V254I2TJYL7k1Ib8Cx0T25EKNhVp3ikuvgF6FsAyAx-pEl-GbJAZCqA1I9MANjlW0TJ0KmA6TpvgpjAFccI0HBBQRyGZDOBc1ZHAMp21_Tu0ZK6yRTkh4WXpGxMM3Lq7NRhEO2XCpD2QNHHmz80AMLEwPfcLQU5IRmWoJRprMF2rvmHY7-Js6WS2H8dY4XE3KWwmP1OGVGbKCUHcBazpm94jx0OY-6EKl2gdibt2CIK2rmkkg5gVKTlVmN9QmJ6MLOZ8YTnT5wT0FxfOgbKPN6YEDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmgEZReKv7SpUSwBuGIRPbAMlS_7OuqZe3t9O_C2JQFEu9x0pbWCCJwG852cl5V254I2TJYL7k1Ib8Cx0T25EKNhVp3ikuvgF6FsAyAx-pEl-GbJAZCqA1I9MANjlW0TJ0KmA6TpvgpjAFccI0HBBQRyGZDOBc1ZHAMp21_Tu0ZK6yRTkh4WXpGxMM3Lq7NRhEO2XCpD2QNHHmz80AMLEwPfcLQU5IRmWoJRprMF2rvmHY7-Js6WS2H8dY4XE3KWwmP1OGVGbKCUHcBazpm94jx0OY-6EKl2gdibt2CIK2rmkkg5gVKTlVmN9QmJ6MLOZ8YTnT5wT0FxfOgbKPN6YEDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هازارد، استعداد سوخته
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/91042" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ujkvYav_p1cCxKVUkAokXo2O5lQZHv8BqlL80IBr-en3Rn2hCP02Ol6nrQiOx3RIU69ih8n21cmga_H0vdQ312x94-ywBwcEbNTmlqgvo5U4PYj7nmekKIvniuav5ahrV5C_Hnh0-yJiXbEknfDwPNbS_2F4bcbNVYfGHWgD5wimLZzUHI2iRvUFo5ibWaqX-KZNAANexwhW9JPEseOtqLe3OAXaPyR4SHjcHWDL9d0P5oR2xquBUOar0rp043ZmjSW643k8PjNJ041aCol5x_QquxXBu3ZwBVlixXUJ9y6Z1dTHStcXgfpVPj8n4zZYDkXwGT3odX7G-p1roWI3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
یامال به عنوان بهترین بازیکن فصل لالیگا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/91040" target="_blank">📅 16:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91038">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxBmARQhEIlqkNfpEnwA7iWWOwhTzsk7FlXGdax7ayXd5QZPna3wioaxzawLh7HSOiowKCs99Fszj-pXv-cCCWzjpcPmJxZAVQTK8RZI4NGlllxpDrTUOMsZBXMvScTLvcZkQcXqDzTOwNvOhYy1lcC4MXmg36gUdULw-IsIX4li7uXhmkHEjiGxqVI-vkrIYxs1pUGy8hbzqP_8js5-6FDsa5w00OQIHfqF40EpReoRPrrRC2f3M7nF5TaJOpj2a9c62qHvd-4DXrJOWezz6a_NKVzHYdnnZS-A2yrPn4FjulD7zTBz5j060piWhgFZ5H_mb5b7EB6I5olRXBoICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فووری
از اسپورت:
اوسیمن به بارسلونا پیشنهاد شده است با این حال فعلا جایی در برنامه‌های بارسلونا ندارد و اولویت آلوارز است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91038" target="_blank">📅 16:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91037">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMM7LU8izk4BPVmFJrXSw2pBMlZl2uKSNCmnJHMOTqO92Pj-8D50q3XJNWQl_7vit9wb7Jm7dVpv3iStKPrQzIpEvIPYIiB8MHijDSvxHn6aJQhQX37_IJnFLAGTcNptwuk6NWQGK1XzYj7FYbcADb1kjUeavJjYFg3utxOHSl2dYNwjCWIONr0hVrP53kH_tWndadP1ibI_IH9-waC5PLA7qh0PEZpCqfi-dQIq1bXwDxTuELe0I7Q-KdGIY8TVb1DsHYcbg5UyvYjxF9VA9OaAyiavi5tn6klaz79bI3S0rFQwXwdJonbMiQz3nTXubJDkMWLkPAKast52EQt1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه یه زمانی حس ناکافی بودن داشتی به این فکر کن که برای سقف برنابئو 600 میلیون یورو هزینه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91037" target="_blank">📅 16:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUToaF1yXLA9SWyStd9TPd9JuwK0Wp_OwLZVQyvLOwFACdMlX2Wf3ZUPrIKootdR7ppfK6BKcxfBYe8TWbLsVgcg7n0-5UBP9XRmXgPpo3wdeUdqyR8A-mwqmQOUKk3gjk_OI8iRt14IroMywhIuFBmR2nSwiddoqUfqTy6m3-rvFOQ-kBbrw6SqWpBjj2PIljRzjukATmJ-U-MBmlCy0nqMAXA92gVLBNDUl7xhJSaPq4qxHCfSJ28t_61WsKUgenl4jJtiwQz2Xe7_X5GnXZLhRN2Iq33RJ-mVtDVkO7zQUR_armDGDHO8jQIUbN0Jjk9JZmLCmAl2G7rBkxeBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل لیائو: من یک چالش جدید خارج از سری‌آ می‌خواهم. لیگ جزیره را با دقت زیادی دنبال می‌کنم. اگر فرصت بازی در آنجا یا لالیگا را داشته باشم، واقعاً خوشحال می‌شوم چون استعداد من در آنجا شکوفا خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91035" target="_blank">📅 16:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e01837206.mp4?token=qyfnA7kStMsnpC1MPzRDS5Cg0EYSnxiomHA5sqUaRMsLsE98sCg5PiNbSKIdjwk07o8mBWVaU61EQZi3oCIvmis7r2V5da7dU_9qmNj7CXZZsETh2KD7PxhC2LY5Mk7aiJCnmaTb9toiA_kedVyN_6biSoi0J2wDXgTfbm7z98TRbIkcAsUd3XXc2pfMbrf9K9IA5AVo3KVGd2wHHX9HuBhw9Y_rWuPGFT9C1v2zvg-rSLp8dj-dcMJnaov-Q7J1IyMufmnrHZZYA1jmCxZr1aVJTRMI5QQUp4eb4pgdWkgDq2v7xAi9VO43L30f5I-EC6eFOKqWSazhoGeHHZobJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e01837206.mp4?token=qyfnA7kStMsnpC1MPzRDS5Cg0EYSnxiomHA5sqUaRMsLsE98sCg5PiNbSKIdjwk07o8mBWVaU61EQZi3oCIvmis7r2V5da7dU_9qmNj7CXZZsETh2KD7PxhC2LY5Mk7aiJCnmaTb9toiA_kedVyN_6biSoi0J2wDXgTfbm7z98TRbIkcAsUd3XXc2pfMbrf9K9IA5AVo3KVGd2wHHX9HuBhw9Y_rWuPGFT9C1v2zvg-rSLp8dj-dcMJnaov-Q7J1IyMufmnrHZZYA1jmCxZr1aVJTRMI5QQUp4eb4pgdWkgDq2v7xAi9VO43L30f5I-EC6eFOKqWSazhoGeHHZobJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
🇮🇷
یه هوادار مصری اومده به سمی‌ترین شکل ممکن ترکیب تیم‌ قلعه‌نویی رو برای جام‌جهانی گفته
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91034" target="_blank">📅 16:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91033">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaVuLc7EDU6jRuWcyjpcgYKrSQtrfupO4CTRJItVeER2Wmqpukf3lOME4BICbZV5zG-vVNF4GrsYOttmGjZwsJWC9BSMt8P8t2qx6r4FeAluBO_Nptj8ioM-suZTdJUSo5EFiXKvP7xJz73gZDKU_9DWa7In60340j0dSj3k7xgvVXyd7b5F3OyZhrW3UYGDF_APhTLK0ch22F9HJJTebbrQG_7zJVyxtW0r912Gq-idCTaI47eWmkX3tPIk5XXs4gkhQ1NiqD9Cl-swTLmAEE8xurRIniSkx5I_iAcrP1GSBFAKwSTh0Ik8dVP_9MJ8PvPcpVty2I0bbr3kXBViXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اگه لیونل مسی در جام جهانی 2026 پاس گل بده، به اولین و تنها بازیکنی تبدیل میشه که در 6 تورنمنت جام جهانی پاس گل داده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91033" target="_blank">📅 15:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91032">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk_E7A8NXmyXR7J66JN50okU6UICElODMsNeswIPb4qFmY7nFgY6aZFiTohrbpu8Z2v5ZFqyu8DAFQD_agkfVHAmGAZj_YJufDZHPUyvb2Ak0msFcIcvxc-1GZgFPESSDRwBdkGwYWLqQPuyJPTFV-fG2mGu_J3qlr22aDb00j5kDTnbKCDLpt9Np7j4qMHqPgHs5ZbY8Duwkz7nmrCgnKSW7dZcsdXyjlrbnUl2Zdb3YVrTBqDS6aOfuR5tJqEDHlREXd13kDsdWgQBvOsLDnKM01lBZENwpdbplOc2p2SvXkEaTN6DPOVBLWRaOFnrvhMhrOW2kmqzJbLbCn7MXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری و رسمی: اندی رابرتسون رسما از لیورپول به تاتنهام پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91032" target="_blank">📅 15:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltCqq2vdc9f0l-Pnl-EeKfLraYGclKMcGfPpwsZtOtglTkHyOWLpiFWdhbLQy8M-EUxfbqg5nmlST-FA7GWuf3HbRA-xo96cDsIQoAtVoaPQ9qkxAPTxlMQTSA1BodZ4PIEtkZe1vw9kjBLZ_nPFv_m5O4EHs4E-UND3VUFmU6xzdjOrH63zg4v8cq7Y8Tr7P-ClHhpp4n2Zo4xGsHn4fZJ-cY64pQ4e-BpuNjFiVXriZq-OZt47BVgwJKvGtZMA5bCycpPWOY5177r8qd4dI8wKrTuXZwdot_JtUOvhC7GYDrzObVoojPfOM9sylX28BmJLiF6KqgZ1slCgBve0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
🇫🇷
#فکت
؛ در جام‌جهانی فعلی، ۹۸ بازیکن متولد کشور فرانسه حضور دارند که فقط ۲۳ نفر ملیت این کشور رو دارن و برای خروس‌ها بازی می‌کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91031" target="_blank">📅 15:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=IqMOkFjcRIVy55i34nbXsvdjNPa6PJCHYs-MnvFUCjgMoSDajqBAzb5O0DRJ8eC0GPtIdH7uCBpTYOdZUr1s-zDVpoVUgTCayh0PKI33FnxfjxAuHZGVF5qQZh9JosP1rCVmVchcZUqU6P4RBPnd4CAX9kNFBFjxPDefhUiAzSd6ZCQJKnb8xTTibz3PQaomoAQRbbl_7IoayvqEnK-6OL6X9ZBE-v8RRiv2hC_PnZf9xNzjuYwWQdK4zpbeKOyDuSA3-wWE_fartUt9MqXk1GqUs4f67ba_PA4kKWv-1-7rfmgIG-x7pDV03hfFW70_ImXN2biHoMe3v62RDBfyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=IqMOkFjcRIVy55i34nbXsvdjNPa6PJCHYs-MnvFUCjgMoSDajqBAzb5O0DRJ8eC0GPtIdH7uCBpTYOdZUr1s-zDVpoVUgTCayh0PKI33FnxfjxAuHZGVF5qQZh9JosP1rCVmVchcZUqU6P4RBPnd4CAX9kNFBFjxPDefhUiAzSd6ZCQJKnb8xTTibz3PQaomoAQRbbl_7IoayvqEnK-6OL6X9ZBE-v8RRiv2hC_PnZf9xNzjuYwWQdK4zpbeKOyDuSA3-wWE_fartUt9MqXk1GqUs4f67ba_PA4kKWv-1-7rfmgIG-x7pDV03hfFW70_ImXN2biHoMe3v62RDBfyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ از یه عروسی توی کرمان وایرال شده، مثکه رسمه فامیلای عروس اینجوری فامیلای داماد رو میارن وسط و با چوب میوفتن به جونشون
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91030" target="_blank">📅 15:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MM6eKXM_mT4N1JwDhws7HWaw3cKcxaT5Rbo2WYSzPy-i3KhWUUqmj0idDzJG1IyGzElqRmnYTVrTALgRQ_I1klnxNqZrIrpWeci3HHEvxVHVYuYTLohL0HFk4CfafeVEU6PoSaYq_s-2d3nfRFa7IgL1ftBELbO_avOma1t0T5F24gorXI9O-4jXqtDtBwBTwblNjSfvgKZHZSjUwjRlV6PKsD_iQ2sxjuL2UXIBfOMLgTz1gHuImXMJz8jXkwsoFFGufFC50bwQRCRtaqBaLFpG73tA_mo70m7MX2ypX4L4dqL_7-5OCm4HDjDqJ6uKb7Cnu43jhEnNCw4hhdpUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9IOryRMBNo7HvRs75SjICZNHYN9vaqLZ5Q37OXnEMpSyXmKoIru4D4OXXYLmsugN_9mmgmaaOG68_n6-xNtpox6uAB2S3Td-7mNWvq5i9z5glugI5k71JEHBIMxUdllkdDqFx1jXsJ6DJwJaDOo_D1YgCSLuX58EYUREuUnvX0Pn3FwEzBRUv0HD6Hwivd-VeNRkLlT2cS4q4VLQosPCJDbdZhE8hDjp77ja8WZ0eq4rBIp9BQyEtF8xAirZDnmEukBRC1D_BVyDe1DFem3wUjhthoLDGtw4Ej3MP7VtAmu2LwBKsLQQW_44nxc0wnEf6uDrh65Q5RNxFIbw6zTyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🎙
🇧🇷
جسیکا توگا، دوست‌دختر سابق وینیسیوس جونیور: «بازیکنان سیاه‌پوست همیشه از نژادپرستی شکایت می‌کنند؛ اما همیشه زنان سفیدپوست و بلوند را ترجیح می‌دهند. هرگز با زنان سیاه‌پوست رابطه ندارند. چرا اینطور است؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91028" target="_blank">📅 14:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=PFd8VIvGMYfKSj0uK6AzFORK13wL8P4KBI-4RK-O3JoQUQIWRDWsMCjSLb0FEjOqkS0tMuQtOl7YE9HUnyanxPk5aicGFtlGpR1hHSRdSDimIYtkMbp0Z_RxFhIOD-f6Uq7DyJdQLB8nYre3wDtOlqHCon6ul7fy4JEaCZaJKHZsslprYmnqBM9Fx0v8c_53ry5MvBbzC7qyzRC6uWeY1STOnhWygrLy8vt-D4QExUCdV_oWaxL5NI_tFOem0Ib3b0zvUUkkPQ8FJM6T4lH_2fRh1ESSMePV1If93oLRt6zPKCtcqhl9ErZ38hUu9h7pbU_Cy7NAjb_rf-6UnkbX-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=PFd8VIvGMYfKSj0uK6AzFORK13wL8P4KBI-4RK-O3JoQUQIWRDWsMCjSLb0FEjOqkS0tMuQtOl7YE9HUnyanxPk5aicGFtlGpR1hHSRdSDimIYtkMbp0Z_RxFhIOD-f6Uq7DyJdQLB8nYre3wDtOlqHCon6ul7fy4JEaCZaJKHZsslprYmnqBM9Fx0v8c_53ry5MvBbzC7qyzRC6uWeY1STOnhWygrLy8vt-D4QExUCdV_oWaxL5NI_tFOem0Ib3b0zvUUkkPQ8FJM6T4lH_2fRh1ESSMePV1If93oLRt6zPKCtcqhl9ErZ38hUu9h7pbU_Cy7NAjb_rf-6UnkbX-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
امیرحسین ثابتی نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد و ایران را تبدیل به غزه دوم می‌کنند.
❗️
اگر دوباره سایه جنگ بصورت جدی روی کشور آمد باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91027" target="_blank">📅 14:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91026">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=nFFREtfQEfbtrX7-K1JolHESDnwngz5ocobTbtw611Dnbc_qJMRZnP-05BRNxjVs8wnZ_NP_yy5EFa-qYwU2JDv2vjuUTCLPkCGMVGwi5ZuqigA5V-KhAZ1vfnzXVAoi9UWZgbwEQBoQexyrr8-EhKkc3-9R9TPHPuPxM2_5L_Bk6ArmcIzxizB5Z2mlgffk6pLRH2Hv1t01phqyuW6DMsAoF0lN77jiBFCZXOIrgvx5UvOza5sI5ipqVrSUr-5fsgMXYl-g99XM509CMSHZWuEAiG1Q-DHkjnw-d7ycOVmnIKohUhTquIaPJ2JRInwJON30WycEtzY4EDOGWUJ0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=nFFREtfQEfbtrX7-K1JolHESDnwngz5ocobTbtw611Dnbc_qJMRZnP-05BRNxjVs8wnZ_NP_yy5EFa-qYwU2JDv2vjuUTCLPkCGMVGwi5ZuqigA5V-KhAZ1vfnzXVAoi9UWZgbwEQBoQexyrr8-EhKkc3-9R9TPHPuPxM2_5L_Bk6ArmcIzxizB5Z2mlgffk6pLRH2Hv1t01phqyuW6DMsAoF0lN77jiBFCZXOIrgvx5UvOza5sI5ipqVrSUr-5fsgMXYl-g99XM509CMSHZWuEAiG1Q-DHkjnw-d7ycOVmnIKohUhTquIaPJ2JRInwJON30WycEtzY4EDOGWUJ0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امباپه در ترکیب فصل‌بعدی رئال
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91026" target="_blank">📅 14:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91025">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKEafMEN09GeMpLdPEZ3Z9r1SZOnUqsbvzdb9Do0JU42z4ZSWSqXMwXcwpjn4ep3sD9aPf-2UGMkS7pK8U4_DQP5r8Kd1HHyWAfYWATxrn159FW52DnNM-fU6A_ZpnTfJwC6vQdLXp6RKWu6PvEIF7IL_I6VqXKO4IpnLtKONawMhscc6B_A2gCUasgYzUCyHYc8gyc9yTI4Y-YwdRbImlcVyNPzR9CB_TNX7tY8FvLJ4JJ_V3NAqHcOLBkJxpRgmk5SC71tPZGsSQprIiuQZf9XECV2xIatEvH2NAASsaOo6P9-684kkp_f7sb7QuvqarCer1Vkji8FzNggvwEv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تلگراف: با وجود تکذیب‌ها، فلورنتینو پرز برای جذب ستاره بایرن‌مونیخ رقمی بیش از ۱۵۰ میلیون یورو پرداخت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91025" target="_blank">📅 14:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91024">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91024" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91023">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFonJw0zwgzaCxfZ1EEsK8EiLxuViwWEQxZq0VfI_wdtC2mM6_6p4cfeeqc37q26_ajJcuXok1Hdk829VsSdeYaeUCV6OICJx0SN1qO3PH4xrB2eOE6MisETbmbZMso9tYAi6UVOvBrsOGxoljqBCi2vwqLaVtrV8pxzKoM76W7DMeSKzwqzKrry0FTBSRS4_WqgZJ3SwlIyLxm5cIQelXh5GEu2eRAl063sVCstrKr8mXLThtsLPNBARIb4d0okrw_rAZpt2Un1VhQAflNcaFx-1KxH3ddTAxeA9xEVb9cYvPLtPT7rgcMWIm36AfLE-qjaAp0RwQfw_uU5Y7lmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91023" target="_blank">📅 14:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91022">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJHp7oNEVB_bKcOZ0KdPZcrCF4_ZLC_KSM4TbF47G1fNA9UnB4dwmtvg6QTZchtV_EgXx2BNv1nBkytDjsYdKizyA-QvPoCKve_89MEy-pEyirIrHkPH6RQ_xZqZFxBRAr3gcUdyvYG_lPqbjabgpPoai0_tphsyRwnPoUg7G6ys5HOz6psk2qtK1ssPRO1Bvb0-KvTCSyA4l9vF87AjbZPwHHpF-Gn8u4T1kO8tJDfXgY4JkbbKT0sCM--YkChz68Pxvc0FW5NTmDwWwZzEmy-28ggbxiLx9qXGzHaxgxSLzC-WvdhE6lk5zUTWZbiji-Mzk4qXXx157_d8JQqqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان هر چند وقت یه بار هوس فحش میکنه یه استوری میزاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91022" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91021">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e1282030.mp4?token=N42aJ1nT5-cba5sk91TxOKYXujixYDLkLyc5VNQVL8LibCSTDx1WEWbagPto4bsv-mZ3EbWML2gbTdI5purcX2-oonT5BsLk-MROEDodwq0JyVnlj8cuSl-eit0sozi-iPJcXTWKY3oNExZXUagKq0Wd-W-H0W8S_snbR4ICCwEIWbkWk_cC9OfIepioT1aWtXDA3f_8EWuNvfW5L03NftMJGKefRBqYcaRaXOb_qor9-XyWzhyJwr5RUgIYmbIhVl_G7gRImqXaJBO7k3PVDlP6rcuumCcbybKxRQE2leqLZBGrexavJUToK6hVuPjBUU95IoUuJR8Xbc8kob6zlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e1282030.mp4?token=N42aJ1nT5-cba5sk91TxOKYXujixYDLkLyc5VNQVL8LibCSTDx1WEWbagPto4bsv-mZ3EbWML2gbTdI5purcX2-oonT5BsLk-MROEDodwq0JyVnlj8cuSl-eit0sozi-iPJcXTWKY3oNExZXUagKq0Wd-W-H0W8S_snbR4ICCwEIWbkWk_cC9OfIepioT1aWtXDA3f_8EWuNvfW5L03NftMJGKefRBqYcaRaXOb_qor9-XyWzhyJwr5RUgIYmbIhVl_G7gRImqXaJBO7k3PVDlP6rcuumCcbybKxRQE2leqLZBGrexavJUToK6hVuPjBUU95IoUuJR8Xbc8kob6zlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شهریار مغانلو:
میخوایم با ۳ برد به عنوان صدرنشین صعود کنیم!🫪🫪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91021" target="_blank">📅 14:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91020">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=Y5-T3U_koupFs_2cEcgyfV8Ii_pItugMU31PccRXGi9I7ORcjKBzSpDbuIXYzUA84UMB7Lr3PtdtgYnejijoaX2mJt6A8aAzJuOxVEuS-22_4rbtQW0ncXtQMIxnb9dEhRT7RTH55VcijfQL4m7wXJDO0LzRaXfamiEn0HB9xhafeoWWWsY7N-etjCgU_W5uFGXnogM6yFhIS67wKXWIdWhPHA0y6opxa9MCUhYZqQWV8lse3ZY5cme2YDV8waMXxXsq7_p2jT5ufjLppYl9DSMrFicD5N4ZnyZqqJ2LB2S5pKZgGc5JR90o7odVabiEszxN-lHasjfGhzs423jsEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=Y5-T3U_koupFs_2cEcgyfV8Ii_pItugMU31PccRXGi9I7ORcjKBzSpDbuIXYzUA84UMB7Lr3PtdtgYnejijoaX2mJt6A8aAzJuOxVEuS-22_4rbtQW0ncXtQMIxnb9dEhRT7RTH55VcijfQL4m7wXJDO0LzRaXfamiEn0HB9xhafeoWWWsY7N-etjCgU_W5uFGXnogM6yFhIS67wKXWIdWhPHA0y6opxa9MCUhYZqQWV8lse3ZY5cme2YDV8waMXxXsq7_p2jT5ufjLppYl9DSMrFicD5N4ZnyZqqJ2LB2S5pKZgGc5JR90o7odVabiEszxN-lHasjfGhzs423jsEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇯🇵
ویدیو منتشر شده از زمین تمرین کمپ تیم‌ ژاپن در مکزیک که کیفیت خوبی نداره و باعث‌اعتراض شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/91020" target="_blank">📅 14:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91015">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb_zhLThUCgLUcLSt66kU8WnJ3pBcR9l8eliSR4_DDxX4wz0L412zlG4LiX5gLPVjmD6NOopu-cgAJrjjCoFcsTWLf6l-5H809p095pBfwGnlNp3hyhvO6OZOWKKozG1NeoyCLA0qR4MAqMWwnD9x0-eQM8PMy2xT5KjuVzmcfcw2Z0OaR3HnyUUTtYXwf4ROZSb4gJiHn3CbpJPRbtOh9kCTI2ewYXFyw7V5g_NMSxigiiCEJESjS2-MZl0JIBos8-efEeDu0kEkfvpizmnMQ_WfEUpC5s7PnUB3CyolwICSXjcKYqqeLci1-wrjW1KRnyfogysPrtct2yob3FLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMSatLVANNzK2GSOQpXe4EVirt7yL6ZUAKSZtY7LLGVQOEXeM0sWvMK-ZX_VNRCcH3QqqOzfch31Esgwgm8WyoJOKK3N2l5Qr0yLWeVq6b7TqKJ-gzt3ZPqPFUtxVKTQutA2g__6Ah2tx3sgXCDGPcegd9pcgu_iqyp1djbsa8XIKJibJIgGyZ82iUlhw94t6lVaEeVgD6Ly5vHrkX83XWMcM82yAw6i6gew7hdLjk6cSMTlmRZm9NhfBnWwJQ1oNRXlI0RDi5FnXmsxwBrJgkoCbybRu9VJinYZvnqiwQuyHbu3itVnv3sbT3Sxjn2BO04CaLXn4QXs1207Gms5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSBJlfh3AqvVA3DhNKEbk4WuxCFJnjM1IBt-tubP9uBhxqOLttqCkzPZi1jFDZWKH6heJVuZcblnp5AvvxpM1Uu3McQsoAK3nUj_gZKmVMvX-C46h7Lc7-LpmtPIZOaDxnE4YDR-56GEWpoQySnvutZ52lyKqHYu4DL7szwbtrCS8V22Vs-iNtm1MTZP30rmW0QRDNrfjLH9IvFB4YRM2a9b9FYOvvUiu_btkmH_V0r9QZm3vBdK9gefojGyMgsqUoH2c7NcMGoARDlbR9KNkfRag-WqxVMndXNiuCjmmprWdtU3IDNQf0xyyRmo77Vn_WzK5mzmRncVgGjOhn_CjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEHuTFB9WKJpapjbj99me5W6PKj3CE6eetE1RSBtk8q0wtOESsh6HWQRegRwCO0SX5j7-CLZF_G9o3pTw4kR1fUX8NrhjG8xR52A4gOY1B7SLkqQj0ru8loAz_n1_4UbUrGmqkI5mFJ6vzqYvfGj2KO-pZEUzGFOx0llTbwNeDqc9-n7dFiZ10eyP0PlwvrnpPpZCUzfNn6jEsjNboqu-LBzQibx-ddEy78zb3v4hmQ0NhC4D3hULvVujzMQhaLPswcOVDSrvHF1k9LqnMAt41J9YVlyx5t_OpbWksas3wBEqui9sHZviy1u9cSmrXrq5D8-1lBqhUFVXL4YPvCL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4sSgxOGmyC5aJCMt0twiQoL-en6-IrjGOuupRaFLJd5cQzefX_ZM9T8fNz7HyhbRqA8Ra6JF_E-yaRlWhb3ko4HhzNQdpercAqSoo_1RaVFwUJ15U0bms6DsWYdRdGxWVP6z2fNxKXl6gIYltPNV_goMkJ0tRw5o5HfIB_jrgOG5ukKwMXnDNlnMHkloBU-U36BBbjGc6C7PhDvL_TChVLVURDM_Gfo9qWHxmmPvMHu0yscOY0vTrfMGtPm6KK3UI0t70tfceeJRJVsYrqPSGNs1lZjSFbuH_o8hVk0SAP7dtmyxspVMoJ1rtb97MgHxajnhGGICUrk8jRfW99O5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
هوادار روسیه‌ای در انتظار آغاز جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91015" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91014">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=FMzTmqqZM1NQBk45sdK19VSLE-Ejrxb2NrZAEHKhu41eTwHi4VgSd8Yfc6XZ5Z4XyRyCwMWrVJ46xm9xJyITBBqZG48HeTE5pAdthEnM2cWP8rQkJMsCZWMSBTnHkCk2aEs1IC0tOMo0YIM4OivVAyuI5tyHHBu0sWn2s5tnW9TKEMB64Kc0SnQaP0UNYs6cXT96bXMv4gF_YgUUXTu-43EfazbWiyADECwddLGbmNw51rzeddazt0QTPNX2rgQNVo7ozr9oBpQIAdbJgHR_NbF6F4ZrcnyiJl5NA0jAJkgTmPSnBDUAxw8XhQET0ZVult2tvGD9p-j2tblOdwraVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=FMzTmqqZM1NQBk45sdK19VSLE-Ejrxb2NrZAEHKhu41eTwHi4VgSd8Yfc6XZ5Z4XyRyCwMWrVJ46xm9xJyITBBqZG48HeTE5pAdthEnM2cWP8rQkJMsCZWMSBTnHkCk2aEs1IC0tOMo0YIM4OivVAyuI5tyHHBu0sWn2s5tnW9TKEMB64Kc0SnQaP0UNYs6cXT96bXMv4gF_YgUUXTu-43EfazbWiyADECwddLGbmNw51rzeddazt0QTPNX2rgQNVo7ozr9oBpQIAdbJgHR_NbF6F4ZrcnyiJl5NA0jAJkgTmPSnBDUAxw8XhQET0ZVult2tvGD9p-j2tblOdwraVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
بانوان جذاب اونور آبی موقع استادیوم رفتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91014" target="_blank">📅 13:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91013">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=XdXXM-evgJgYivKKbV7X_gqdeV5knS_SXj-VMZa67ys_rL7WaTBd42vHAKRlURssAQ9nY_8mPrTZ5i9zgn4SqWTtoFrB-8cCbmwvZxTkM9oviEC0-mpJsbz18DAmBf5o9lkYntgqSdFnY7rJ25Om5BOin9djMcYKgHvmiQFjnVZQ3owVF3mt_n18SGKmi4a29qS3BmVvjFUdz-W_9nfnD6tubWfXvUiUXl3t7zp90uTPdCvbCYa4MKlRq4UG9Dsq8vtKRUR42vMu5FC4RwZcN56mS8-Edi7fRBqOGbbodtuq9dphfoxJPkLyJDM0H6bwT6yLukVmh8aBmjGBdghk6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=XdXXM-evgJgYivKKbV7X_gqdeV5knS_SXj-VMZa67ys_rL7WaTBd42vHAKRlURssAQ9nY_8mPrTZ5i9zgn4SqWTtoFrB-8cCbmwvZxTkM9oviEC0-mpJsbz18DAmBf5o9lkYntgqSdFnY7rJ25Om5BOin9djMcYKgHvmiQFjnVZQ3owVF3mt_n18SGKmi4a29qS3BmVvjFUdz-W_9nfnD6tubWfXvUiUXl3t7zp90uTPdCvbCYa4MKlRq4UG9Dsq8vtKRUR42vMu5FC4RwZcN56mS8-Edi7fRBqOGbbodtuq9dphfoxJPkLyJDM0H6bwT6yLukVmh8aBmjGBdghk6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای‌کاش اینترنت وصل نمیشد اینارو نمیدیدیم
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91013" target="_blank">📅 13:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91012">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnvWugjr5jr9q9vCzvET6uy48AaL9UzaC5mehuuPKSxAsN_85iewLqVaxgoYFUUlWR0YNhaVDKz69npjWbZ6k_B55STzdgdx6q9Cp0nMDyLX7iVoNyxF7hNnlEpn28SATrvAaBW5PMIfw5ZPw6SkdDO7MNrQp432ZnHj69-20-ej1Ivq0epRtl1FbI_vycPl8uVX6Z8fqKH-ZtsA77p3vQVX_6ynLXpHp2_MwnY1YGNxPIwebTwJSh9kPiBEujTlo2cDA2Ycu213eHI3RXkKqkfrX-UMRYCYLFZRWMfPUrZYlE3wyOpWxVu6uVSbf47FEL9evhYnDRPqc0CnHSYWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇪🇸
#نقل‌وانتقالات
|یوونتوس درحال مذاکره پیشرفته با اتلتیکومادرید برای جذب سورلوث است. در صورت خروج این بازیکن، احتمالا ولاهوویچ که قراردادش با بانوی پیر به پایان رسیده، راهی مادرید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91012" target="_blank">📅 12:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91011">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
‼️
🎙
افشاگری نیکبخت‌واحدی از پشت پرده بازداشت مجاهد خذیراوی در پارتی شبانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91011" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91010">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137c5fb470.mp4?token=SINbqSkkX6pR1g_mrh9OSecE9CFcSmaEZKUGB-IjSRQWdTiWlZ9WaYLmsMnuUc58fLu20EvWHalFlEjlJ4zvQ57SduZD1JYriIAIb3WXvYlK8b8xuoUkYQjUTk7L5HUmC0VJVB8cJQgQstvL6jRcf5kQ4TU0cwMDC16SG8jL3YclSnw8ey7_YMRWkp9KSat0PDwlWZ3dAO6JYJXwUUsxlvmHFkAueqSP_pZMIeMlW-RfSWyyHqHU16kWvlXs_aja-1q5Km9UWi1Zy8c2v_E2BiLlmW75PiNtF9-Dy7V1hmSx-XenyjGfZtTTrjhX4bcI1nATthEjlEQomDXZIp3eGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137c5fb470.mp4?token=SINbqSkkX6pR1g_mrh9OSecE9CFcSmaEZKUGB-IjSRQWdTiWlZ9WaYLmsMnuUc58fLu20EvWHalFlEjlJ4zvQ57SduZD1JYriIAIb3WXvYlK8b8xuoUkYQjUTk7L5HUmC0VJVB8cJQgQstvL6jRcf5kQ4TU0cwMDC16SG8jL3YclSnw8ey7_YMRWkp9KSat0PDwlWZ3dAO6JYJXwUUsxlvmHFkAueqSP_pZMIeMlW-RfSWyyHqHU16kWvlXs_aja-1q5Km9UWi1Zy8c2v_E2BiLlmW75PiNtF9-Dy7V1hmSx-XenyjGfZtTTrjhX4bcI1nATthEjlEQomDXZIp3eGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیدا مقصودلو شیطون شده و میخواد با پولای ددی مورایس موزیک ویدیو جام‌جهانی منتشر کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91010" target="_blank">📅 12:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91009">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul1Gl1NyNMXJcq8TmyO4o95r3yHlu1cK8mgFJMP0XFXfK_ov3gZNgXcE1D403hPy8UQB6GGlaFsju6TfF2yPpQiIKb1BMJOmkoVYZKrTmKhMz-_i3gsK4fxRbZHU5VMsD6H802mMMiQPN3kLWURm-B35NvdrgX4ug5B1pG3hrF-jtbZFFhiIxG-LwmCM5NaZBr3x7225Fji6j2tr7jN89jhcVFVRv60449Rukif4Z86wuDsydU5uONINbihrqzXpUIp3nPHeHZ5VBu-_2QqrPsDIcl-ecsGbdk2-PRgj9rHn3Xsid2p7Mh_peJeFxLLdT3gw_lTUdzEur9KoXB47lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇫🇷
#فوووووووری
؛ روزنامه الکاس‌قطر به نقل از ناصر خلاف: ویتینیا و نوس به هیچ‌وجه فروشی نیستند و رئال‌مادرید باید قید این بازیکنان رو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/91009" target="_blank">📅 12:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91008">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4d39e7f.mp4?token=a2Thuoj1JgIsSyXvhQ1lbrjd-MHvF17iaEVpjzr183Zt3FLwnOwhH8bgsgs2t9n-Tv78pijk3aWaFKXCfvREUGDJ4F3zm-u1A74B2Q8VzcbRnGmTZWUZBmmPo3bTPFocov2b2TYw1CV6utwrDM4Epmi0YNgmb0JvjPmNgpWyP3jK-1-PZfHmEMjTkbtbmz32CCBEIvvbszYyeYfrJNjiIGiBXGP4B-yQFsWwrrc5z5lS0pqdYicccIGYRKqu-N9Lu69FuaFyqA551GZZ4k1aZGgCHP7X85bgkoZKBmOtGXwGn20UHY09ERHzKTnoEEZgqtvYKgbgqIOf6nufefr6Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4d39e7f.mp4?token=a2Thuoj1JgIsSyXvhQ1lbrjd-MHvF17iaEVpjzr183Zt3FLwnOwhH8bgsgs2t9n-Tv78pijk3aWaFKXCfvREUGDJ4F3zm-u1A74B2Q8VzcbRnGmTZWUZBmmPo3bTPFocov2b2TYw1CV6utwrDM4Epmi0YNgmb0JvjPmNgpWyP3jK-1-PZfHmEMjTkbtbmz32CCBEIvvbszYyeYfrJNjiIGiBXGP4B-yQFsWwrrc5z5lS0pqdYicccIGYRKqu-N9Lu69FuaFyqA551GZZ4k1aZGgCHP7X85bgkoZKBmOtGXwGn20UHY09ERHzKTnoEEZgqtvYKgbgqIOf6nufefr6Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صف کشیدن بازیکنای عراق بعد بازی دیشب برای گرفتن عکس با لامینه یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91008" target="_blank">📅 12:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91007">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FM_gRtP3ZvJ3JV_ATEkTfQaAsGBs_4slx5kAA_HIce6XGRD_BgV-2LDkOLNPuxI-An4yc71vr-yjuhJ0lRbAfNEQcCe1FE4bypujos7brlexipEjs7oLzegfwJF-M0ekbO4QNX-eQQ6jeNu8DbaQ5kCV926-Zu8RENQkvewTBpoAxEjaHo6vA3v4lQdW6CD-ig72aXPWuGDK27K1-ygZ36rMcdLtzwRzzLBQd8696pJg0tLrsyGIzDuNFv6Hb5xPNHnx8t7lXlULGwtGsyaKFP2dnxG9p50iux-jbX24oQgGD39o5aoqMZXsE92AgXUixCpE3yvjyFG7M1KcSR4S3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظر آموزش های آشپزی هستیم دوست عزیز
☺️
🙏
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91007" target="_blank">📅 12:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91006">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=cXykOVT9YZW_b_66jUh_KAEfsJ5h6LqzquOd9Rd5sBjN00X_mPf1hAi1Zx1JS0nahGXXKOCUf9WzANMpoV7rBeP7tlw-gotXOp7fjnueehcKSTjukUJHTEs9E2yNssF4hvUEh5jHX3JgaIRILiAuPBSOtED0C2KaRJT-78ZNBoUedVctfeJaJclKuxOiKtNUTftlrSPN1kyzvtUVgFwWeU5WHw5bPUOZeSOUZShpz1BTzC6iwddAR3BCyJMz_ISTrklmETa-mds9rcYW-a1Vjw-jt60PIdPyFvZZ_Za6VJowoGYoT51yHLfJ2It5fzwFxeFEyi5TZYMvqwzvaMiSIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=cXykOVT9YZW_b_66jUh_KAEfsJ5h6LqzquOd9Rd5sBjN00X_mPf1hAi1Zx1JS0nahGXXKOCUf9WzANMpoV7rBeP7tlw-gotXOp7fjnueehcKSTjukUJHTEs9E2yNssF4hvUEh5jHX3JgaIRILiAuPBSOtED0C2KaRJT-78ZNBoUedVctfeJaJclKuxOiKtNUTftlrSPN1kyzvtUVgFwWeU5WHw5bPUOZeSOUZShpz1BTzC6iwddAR3BCyJMz_ISTrklmETa-mds9rcYW-a1Vjw-jt60PIdPyFvZZ_Za6VJowoGYoT51yHLfJ2It5fzwFxeFEyi5TZYMvqwzvaMiSIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور مکزیک در کنفرانس مطبوعاتی یه توپیو انداخت وسط خبرنگارا و یه خانومی انقدر ذوق توپ داشت که با کله رفت تو کف سالن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91006" target="_blank">📅 11:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91005">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=Ory-P0v2EAmS2-VRoZp97CJRLCD6kNJMcVdFiJkYIsgB_ir6QctMqyIYFvtLnglN_mP2i2WTqvwrgcAorQEMOn6osO3flXDu9PbMjmHH0YZlg22on-2e2owwOSgXaQH_7jPiDAFzmcbnD0F03rRfFwxB6Zi88dD49AvfIY2BSb0c_jJaYTHgb4ruUg3TyngLLHFqCpLVBRhT7JIP-3MeTgo1GtpMBMvIJYRDvoifaCuFHYIKLDOmUsZsH6YgUDEIzfjhzfd53apdE3LDyJGAdtrT-s1DKdjYSbDz9zPdCceHsps8UJqk3gn1PlNc3OYAMthBUthEXqTLpLZDCxUE7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=Ory-P0v2EAmS2-VRoZp97CJRLCD6kNJMcVdFiJkYIsgB_ir6QctMqyIYFvtLnglN_mP2i2WTqvwrgcAorQEMOn6osO3flXDu9PbMjmHH0YZlg22on-2e2owwOSgXaQH_7jPiDAFzmcbnD0F03rRfFwxB6Zi88dD49AvfIY2BSb0c_jJaYTHgb4ruUg3TyngLLHFqCpLVBRhT7JIP-3MeTgo1GtpMBMvIJYRDvoifaCuFHYIKLDOmUsZsH6YgUDEIzfjhzfd53apdE3LDyJGAdtrT-s1DKdjYSbDz9zPdCceHsps8UJqk3gn1PlNc3OYAMthBUthEXqTLpLZDCxUE7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور با انتشار این ویدیو نوشت: و شما ادامه خواهید داشت...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91005" target="_blank">📅 11:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91004">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icBJTP3P6RFD__fmZt_17EJ9TBkXY_-KkWXwUwYQK91UPvIjv_KhhzrwG4C2p3-fGWXWb6Tc1v2xx-xt2BPpTFrTIKkLPpkwVK-EFNvb1wldYxDRnNqf4Ej4Q3rpFwNYBKnH11Ec-NhBOg2jVUXQcSiNp1REhLycKW-OeUTB_iLED4QeT3ZTfgWjI0jsy5tIb84TMv1PclMyn-se4Obo0deU0t_gcjGVh72OFw0ArH4jlT1a-rAUxW-VXM2SAbLFsDkIU7k6KXZOSMrXDFUD8APZBjwN-LzFVmDpNE1eH_EfvFS7kitVFd07gHeB5eypsxg75wyIvOGOrKQyxdfcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/91004" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91003">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae875521b.mp4?token=AaR4qWrXCFOZp6MczcgRrknjzqpgwUZVdprO-D7UEiFUdiz6E3hbHMY90PI-727xBN8SOE0uHsKzt1nNZVP0bJVCja0zeODVP7T_MhCGw885ADFss25Et6QN614prM9hEls-T381OzMEHAAPCW9LrQQ7wfEDRKaOBq97Y8hrHVcsZPcapbdooTnfZAu2-vge02rWY4OC3iM3iNXZ3CwQNQGNd75dLnffpyz1xe_MxGHVLBJvz31X2X9j4EPP7AjeSTy7K5xnoOHZsRaui0TdkGizAc5W2ZjqvPlrQoH7E9PUXC9sIDbLBT0dErvTPgmvunfsGwwgrHkYhMbSG6sBSQ17e19KbgV8FywUWQ4j8MaTbs87CD9uSMqcJ0UTzx0bJAse_cfLDAhv7VkTjBhNjNdiZHtt7CxcwI4cMbMqDdqKLRJKjy2pT_UJ7TroWzNfo26_sJhcElrt9FhSsA8nFWDimJ75c5z2ov3OooaKoXtqosHCHT1XYlCxln-5gYNt6VYRJ7YorzoSFiGclrNKdFst5tYvVhhAIKKuLEvO5mid-sgorFVNb8JIW50Mec-Wii0AgL41Gd3OwA3-2elSnmho6rURGvb4ZjvJQI42CWRyftqVxX6vgurV9Jz1tAI_3MrtFBrBdBVDBxheWH9ulGRQcPIc0QmXkmNXz6bE6Ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae875521b.mp4?token=AaR4qWrXCFOZp6MczcgRrknjzqpgwUZVdprO-D7UEiFUdiz6E3hbHMY90PI-727xBN8SOE0uHsKzt1nNZVP0bJVCja0zeODVP7T_MhCGw885ADFss25Et6QN614prM9hEls-T381OzMEHAAPCW9LrQQ7wfEDRKaOBq97Y8hrHVcsZPcapbdooTnfZAu2-vge02rWY4OC3iM3iNXZ3CwQNQGNd75dLnffpyz1xe_MxGHVLBJvz31X2X9j4EPP7AjeSTy7K5xnoOHZsRaui0TdkGizAc5W2ZjqvPlrQoH7E9PUXC9sIDbLBT0dErvTPgmvunfsGwwgrHkYhMbSG6sBSQ17e19KbgV8FywUWQ4j8MaTbs87CD9uSMqcJ0UTzx0bJAse_cfLDAhv7VkTjBhNjNdiZHtt7CxcwI4cMbMqDdqKLRJKjy2pT_UJ7TroWzNfo26_sJhcElrt9FhSsA8nFWDimJ75c5z2ov3OooaKoXtqosHCHT1XYlCxln-5gYNt6VYRJ7YorzoSFiGclrNKdFst5tYvVhhAIKKuLEvO5mid-sgorFVNb8JIW50Mec-Wii0AgL41Gd3OwA3-2elSnmho6rURGvb4ZjvJQI42CWRyftqVxX6vgurV9Jz1tAI_3MrtFBrBdBVDBxheWH9ulGRQcPIc0QmXkmNXz6bE6Ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شکیرا از ارتباط عمیقش با جام‌جهانی میگه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/91003" target="_blank">📅 11:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91002">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwdzxk20RPi296LZwGHw55A17Jxse7cBJf5z5ALL8yaetht-f0oAMeaaOOB3X27qECn4vCnoXqlaJNjAevquABwQ0ch47HrzyzzS8IsCEbS0p1VCI0ABTvl4jvCEoWxfQXWPHi4KWjvUKsdq0KqURazA3y95J0f5zGPtvWMCW0-OMkAFyRmFGTwZDxn47NU2V6sV8cPr_TYyNFm15nJsBsatD2dCcwWCUJXl8cXvaYhiz7Kwujhe6LDI8C7ODZNTwZixyctUMEoZ2nLnqgUXZeGKGjS7WxEfN6gCjdymR2aZghOz9Kkq0OI-aHpMrK5ywA1ElaPNam1BuliL0Vpvfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇲🇦
پشماممممممم؛ رسانه‌های مراکشی میگن که یاسین بونو گلرشون در آستانه جام‌جهانی با نورا فاتحی بازیگر هندی ریخته رو هم و به زنش خیانت کرده که شدیدا در کشورش جنجال آفرین شدههههع
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/91002" target="_blank">📅 11:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91001">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=EeXZwTnLQbBA8VBrYN3EvpJqa3NnGy8Yx6qxv9u0t6GV7LJCsDb-2A4u2TGE0CdmbrLuSTJZFwr9XpQdc5qiZry_DGdyXLABbuL4UpGgjm4FkSJdvUb75EN5BK7AKnk1btsTa7zTA-__9r1X0mqdZkfnb5vC-dQkL5zXp7IJDlaQW2TP4cxZIGBo1L-Ayk2V7hSOPuDV5diNp20qlDqlFpSiKKdt-U6eItTEdv4uqHNiKyhAgpAcBqkJaV-KFgx3lpMOLFaK9oFZoZ7f04aaMBfX_gHu8tZ1VBY2--cts-ye5seJvqPT0HFBUqiX2IU3DjGlm4rvrA1uHz8Z_jffBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=EeXZwTnLQbBA8VBrYN3EvpJqa3NnGy8Yx6qxv9u0t6GV7LJCsDb-2A4u2TGE0CdmbrLuSTJZFwr9XpQdc5qiZry_DGdyXLABbuL4UpGgjm4FkSJdvUb75EN5BK7AKnk1btsTa7zTA-__9r1X0mqdZkfnb5vC-dQkL5zXp7IJDlaQW2TP4cxZIGBo1L-Ayk2V7hSOPuDV5diNp20qlDqlFpSiKKdt-U6eItTEdv4uqHNiKyhAgpAcBqkJaV-KFgx3lpMOLFaK9oFZoZ7f04aaMBfX_gHu8tZ1VBY2--cts-ye5seJvqPT0HFBUqiX2IU3DjGlm4rvrA1uHz8Z_jffBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تو مراسم اجرای حرکات نمایشی ربات کنگ‌فو کار در شانگهای، ربات کسخل مسخلش در میره و با لگد محکم به شکم یه بچه میزنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91001" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91000">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QepJXtR7nApaS5w_IogjnCO5BZKLJbU_b1JVUj9vBNN3wy1aHWw_7S2kBwq53hIRN0TSVCOg-TXIXhFozmhqQjWTMyNwaEr_2ojefdmBM9TBjwZi13wm72gE5muSZWEP3RDAJGBs2kQAcnFH4ow6eYF-4nUg33-MY3uu4VaR5e4EMioRXFtTjvPLZ-N12CNSgE0m7-BKi-_LxGaLsYrkKT426Gs09LRUXFY7ejX1wEqSsRK8jttq0CwzgRCfroIKYwsKsb9cQpdZqlGQdSRzDIhscLqtswuCAh7XxsKlWOa5j7NGsMALjRN6xBNoUBOlNz4DF439NBpW7yxEWYxfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو دنیای امروز به بالایی میگن آفریقایی به پایینی میگن اروپایی
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/91000" target="_blank">📅 10:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90999">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=VBXReGxvGJcbc8SXvYon1a2NHzxeR5wrC9YYu-3Tdi4bx60P3whGiGXEa4VzzKtcsTmjU82mY3fURrEJyOzt9Ny4Ui4GAsw9njXLR925w75F7yZAxVct-V06DnZJo49p0Y7bx5JztgQSXNukDhjsNFJRBZLVxFVAyk8qL3-mkvbTXqK9uv87pWzye__vSH-HZfB19xUTjOvR-8j49WpVnrwWW6wg24CwShVr7VJaTwjB21QiWSlKrlUpXZiOfl_a00xlWaMEVdT0sP9tBOTw5EL3B8o6S6zMQE1wgchvQ1D9KCpLegVnS8G6W7MbUqp0qEuNGGZrDCo3Wo5LaOo8TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=VBXReGxvGJcbc8SXvYon1a2NHzxeR5wrC9YYu-3Tdi4bx60P3whGiGXEa4VzzKtcsTmjU82mY3fURrEJyOzt9Ny4Ui4GAsw9njXLR925w75F7yZAxVct-V06DnZJo49p0Y7bx5JztgQSXNukDhjsNFJRBZLVxFVAyk8qL3-mkvbTXqK9uv87pWzye__vSH-HZfB19xUTjOvR-8j49WpVnrwWW6wg24CwShVr7VJaTwjB21QiWSlKrlUpXZiOfl_a00xlWaMEVdT0sP9tBOTw5EL3B8o6S6zMQE1wgchvQ1D9KCpLegVnS8G6W7MbUqp0qEuNGGZrDCo3Wo5LaOo8TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇿
عملکرد دیدنی پسر زیدان در چارچوب خط دروازه الجزایر در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/90999" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90998">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg3sjMLLbe-9DLAcWM91zXnIZ6hKQiPWsGN1RYGVNHODqc_BjmWjCaXCnJkcqH5WPWocUt1Yr-pcWUEevvZ7MSj0Uid3ljKuDwCIFCA7oVdCVdka-OpIx45UXuMV1bH9H-uvQjS72oqOv5IpDjnOFtWiS3vb1An3wnUNghO8C55eZ-BkhWlXUzGLsODD9-7hvIvSrHD0IOd1w3F-H3SNlTtE_rZLUS-bTiD9AHRA4CGyqDi5cPGTKZxy_BlCOb_7peiLt3d5EXfI3uYDqdF-9sb4PTShphPKS9CUFWK2ki4q4wqz-e0PkjjW9EgzAh6X57A8Mu0Jwal81Qs34mQHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنا د آرماس با کیت رئال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/90998" target="_blank">📅 09:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90997">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k215ttvBBs6EFheK-LXzWbHhBv0hALcICwOzaGPAaNpbVd1SEky3b5JzAQBdaI0xhqF2ifdUozN2fAOIegOci5Hm_h9-UHjJ1H9nAbwJGYGKnef0_Ev0RIJBRxTf5xpFJC052G_tXl9eo4k5PQwrFZ1u8hXuqlkA636dOvs1_X3mzCLRz5XpaBLcM-m2dCjb58mwVoRY-o-PmCiw-bhV9La1dfxP0-u70sPrwykmVVCqrI4MDerC6J7uUwdUOgkiy2NUDiFCuquPyKLIPIZhYZapglgCnvDyGgbohjiHKWwuq0CiBuQhhudf2sGjwJWSyZfqDtTXc-WGHkkj5al3Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/90997" target="_blank">📅 09:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90996">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcd2dc7981.mp4?token=c-EYnLNUzw47FnKiEgdBMcze9Qott1Rkryj36a-nmEiQgUo7U0ioJz6UPRjH_IwjOrzZt02APoi5Wv_j6E8Q5J49j-fI1ODNbGHZ_wkJWNnLXlX-CMJD33n4r2llKat3iU28UUetgL4stkkeJ5KfyHM7BRTZulppI9RTMdOToLEULxwa-Wi_3B49siyXkuMC51B21ncNiBc-UtsFfUmffIpFna9xQxIZK_mSR8oEcRQKKaMZSqJu86eeu7HHi8pTgj-TFFjylqZg57ZTLZSc0Kz3Dq3zCAVoos4xU9x8e8cdKYigAZtyn5eCZ0_39zXc5PUFZfJGRtPAxbZYsN_MTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcd2dc7981.mp4?token=c-EYnLNUzw47FnKiEgdBMcze9Qott1Rkryj36a-nmEiQgUo7U0ioJz6UPRjH_IwjOrzZt02APoi5Wv_j6E8Q5J49j-fI1ODNbGHZ_wkJWNnLXlX-CMJD33n4r2llKat3iU28UUetgL4stkkeJ5KfyHM7BRTZulppI9RTMdOToLEULxwa-Wi_3B49siyXkuMC51B21ncNiBc-UtsFfUmffIpFna9xQxIZK_mSR8oEcRQKKaMZSqJu86eeu7HHi8pTgj-TFFjylqZg57ZTLZSc0Kz3Dq3zCAVoos4xU9x8e8cdKYigAZtyn5eCZ0_39zXc5PUFZfJGRtPAxbZYsN_MTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وضعیت مردم ایران در شب‌های جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/90996" target="_blank">📅 09:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90995">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">▶️
🏆
گل‌های برتر جام‌جهانی 1998 فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/90995" target="_blank">📅 09:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90994">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65885deac.mp4?token=VAqGoBVws67KfMSqGgOgg1iF15PL3zL4f3wMvCTSpUcGNiNNxWCOiz2uqEtHHSrgROH6zXLLz_weIbmmIu0MfysBpyh85-tIZNQ2KnrVTzOx6i3zm5swvCLCm53iK3Fq6emfuTiiIHv-b1Mkg1CQb6cW-3JsLvwZ_9khFc2pGWaPU_NKxaWeek1A-QfeBoCxcPvSYoafVZpFiMFGl_QxeJCVBUhL4D_WfHaUDurZnaqpinAzyE2o4MIzEYocZFDqUunBAWwjEiiZiRRnuK7RTS37EUe1l00OXaqKoUn89ZBIme7qt2mE5RtOMPdsCNITrSbLrtHM3nADv8EQ6AHxGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65885deac.mp4?token=VAqGoBVws67KfMSqGgOgg1iF15PL3zL4f3wMvCTSpUcGNiNNxWCOiz2uqEtHHSrgROH6zXLLz_weIbmmIu0MfysBpyh85-tIZNQ2KnrVTzOx6i3zm5swvCLCm53iK3Fq6emfuTiiIHv-b1Mkg1CQb6cW-3JsLvwZ_9khFc2pGWaPU_NKxaWeek1A-QfeBoCxcPvSYoafVZpFiMFGl_QxeJCVBUhL4D_WfHaUDurZnaqpinAzyE2o4MIzEYocZFDqUunBAWwjEiiZiRRnuK7RTS37EUe1l00OXaqKoUn89ZBIme7qt2mE5RtOMPdsCNITrSbLrtHM3nADv8EQ6AHxGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چون از پست قبلی ورزش تو خونه استفاده کردید، این ورژن‌هم ببینید خیلی خوبه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/90994" target="_blank">📅 09:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90993">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlUrV9O-dkth0nXRhAeRF77YCcxetByzXY4L-D6fqZHq7k84g2j55k0WYcIcQPEL7kc5yR5k1138Rx_gRx6_-U1--qYaUDN4b5P6krq2QyYOMEJYCGfA1hX25fCy3dgvDTIjOXPukp7oHGNDIs1GuyJAF1glwYXfsyS4uCTbVKUJnMFlQirO92S_E0dBmCrhNChvmHv_th1sTjiZmL5lZVoceWiATKAjzVUBEsWn4zoyMz070gkSvWg6sh-IUq0eQh0LvPi7ve83MxDKus1UfyEX4xY7bBNwrKiml4jfrKX_bXL_xRclhUTYc2h-7r8Drb6NZkIVsjeWmCLCZfI-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بهتون با قلب رنگی‌رنگی شب‌بخیر میگه
😎
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/90993" target="_blank">📅 02:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90992">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خوب بسه بریم بخوابیم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/90992" target="_blank">📅 02:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90991">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
خلاصه اخبار امشب اینکه الکی گولتون نزنن. خرید احتمالی پرز یکی از بین نوس و ویتینیا هست. گزینه‌های دیگه بنظر بازی رسانه‌ای جهت وایرال شدنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/90991" target="_blank">📅 02:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90990">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ox97ndaOxQYznyoFVv7iQeZ3Q468ua8EUeILeUFNZdmFOYe2btdM432pDiEAbwgr-dnSGOhG_0z-GzQH-tTgG3zGRBjMBA5yQaRP4J8jEu_b_U78Dal2J3rrwU6X4OY6SNGEO8RUk5PTZ7kPd5b-0qO6q3xWU9-8KS4WsaCOeVAaMOz1xbYXZBw4TvLq2qlkYZmhzLysVp7kk0gc28ldyy_LOESJ8vZjARfm7ctXpiWKWqqosjhY_W0jp-MNzOb7YfK2SzlexH7gl0QJDqx-gW6Qrvrkj1tBJ3Ooi9Pe5WKvhI1YotzqfFhtdK0TO4HxNvraAHJPrJHyoWdsjBJHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سالگرد ازدواج آنتونیو آدان و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/90990" target="_blank">📅 02:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90989">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/90989" target="_blank">📅 02:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90988">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
مارکا در سال 2021 :
🔵
⚪️
دو باشگاه بارسلونا و رئال مادرید پیمان بستند که از یکدیگر بازیکن جذب نکنند، پیمانی نانوشته ولی محکم بین پرز و لاپورتا که بر این اساس هیچ‌یک از این دو باشگاه برای جذب بازیکنان تحت قرارداد، اقدامی نخواهند کرد، البته این توافق شامل حال بازیکنانی که قراردادشان در پایان فصل به اتمام می‌رسد، نمی‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/90988" target="_blank">📅 02:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90987">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQo6opxmHmw-JAzjw9HqsLZhfuO-P43E4zZDH1Z0y-qOtqwBfj73YtqxbY-h3nUO2XY0aJ6Rvk_arellIL_ErOfXa8Y44xb5To0WFzxiyhaZR6RD26gUmSae0gNF4IBDYVTKcEQUk_JRlRhpD9eA3G4YUDfs13LBexd_L1u0xUs0xMiELVTpz1lwqMy6IJ12rFnLf0KA6QAZm4rr-P6oRXfbvvPlpvlQFAj-8lNlcLliCU8bUWobpA703XpHFlEXULx5LYUKiQP9Pna-gSuclLErxSVNq3fIzpJEcG9nHzSP14FI2wWjjenjkXA-ImStvZY9io-_ZwyhUawYVt0yeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
#رسمیییی
؛ فیفا رسماً اقدام جدیدی را قبل از بازی در جام جهانی اعلام کرد. بازیکنان اصلی و ذخیره در هنگام سرود ملی در دایره مرکزی خواهند ماند، هر تیم در نیمه زمین خود [مانند تصویر]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/90987" target="_blank">📅 02:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90986">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3ZrxWeh--OMl8e7yEZon9YHQzXKaX2eyX08_k4oq9suaFQKi_JgwVSMEuKKDgxOdJqTOzh4O_vTL4RsDrfofQJ6SfYzn1sDVjifmu3I19PmjgFDTDyI57J3FIwyl7Bk_5hSq0wiSRBtARWatmoucnV9UGr67Qyr32RBLQNv4AC7AURmadCQIVE13oM5Hro_eSqi2vFHfjlAE3nrkqec8XKl8jNDo6ab_M8en_-ZlMD4jTX5E7NvqJn7GqTbc0ECmtR7xaf4tbkCxpFN9vxqtg1rj27YV5Dgha5fnfrncRwlR3hRyHfax59r6mDrGMmU3Yx3-G03dVHQAhbCElXwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😴
😴
محتوای خواب امشب رئالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/90986" target="_blank">📅 02:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90985">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXvTksR1ywfNqTR-qMbukuDJ2YgFpAqZhfjPAZt7pvAKjU8d8j4i18Np2ON81pK9Ymh0MINrbb2ZuoghZyvJOjGjzRUHkeK38Z9ELrtiK4x8f1ydO8Vm64E6rEUve8U7ITDoPeDPGL9mRr_0KQ0_OuE0EFDbHFGMvskbRDR9HrH6WAGaaEH6dJw4oEGBiQs1MIaV3DQzVPut2XQnqcvjfucuSoEq8FAIlRPCZ1ddYEjl4USgclmO-6ESlKJhI9_UuHShtYkOaOYmPkpbDwQmX4chEb83r6HMoLc0_OEr6UBjTw6Bl6k8lRMtO24cNd3zPPRLbCsx17PofYO5To0Ymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/90985" target="_blank">📅 02:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90984">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90984" target="_blank">📅 02:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90983">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فووووووری
؛ رومانو: پس از جذب کوناته، رئال‌مادرید شدیدا بدنبال جذب یک مدافع دیگه رفته و حاضره رقمی نجومی پرداخت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90983" target="_blank">📅 02:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90982">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/90982" target="_blank">📅 02:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90981">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt4K8XzT1RT73k-E1U663xfv9XHsFaSO-BEIeyj6UJZHcbf16CsFcnAYFOZNJvdgoxMd0CaLr-k-DmDrZM0sXmLi0sEvCeHEMIK1N7iJU3GVzpkOIn7NcQKnB0PUXLSkHRQ-hVDlOq5KqDdatNxPGoSCXyuzlytX12Q25I54s-BBA5vB7q40zU_-vZ7dNlkTQ6G-KaKnz-EJh6y6T45Cm30oh6vy5_5ZNH37uRQjEvgb48KlbTKtAnHgePeNBOflcyR3ovn_lcYif83OVQ0i9Y3T7Y7T3LrhB2jUu9jn3EL_sFuKQbDj_WqX3JuMwIA-EzbZSLZ9yuYbhFavl8hC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
از رومانو؛ سوژه اصلی پرز تیم پاری‌سن‌ژرمن هست. ایجنت دوتا ستاره اصلی هافبک این تیم شخص خورخه مندزه و شدیدا رابطه خوبی با رئال داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90981" target="_blank">📅 02:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90980">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
فوری: خوزه فلیکس دیاز گفته گزینه‌های مدنظر پرز، اولیسه و نوس و ویتینیا ان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/90980" target="_blank">📅 02:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90979">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
وعده های انریکه ریکلمه قسمت n ام  : اگه رئیس بشم دلبوسکه یه پست مهم تو رئال‌مادرید خواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90979" target="_blank">📅 01:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90978">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/90978" target="_blank">📅 01:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90977">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تمام رئالی ها منتظرن رومانو زودتر از سه‌شنبه بازیکن مدنظر پرز رو معرفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/90977" target="_blank">📅 01:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90976">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pLvvwdKTMqwF_C8P23i8OqDYdSnMQ_4I2SuZfV7tMha9JR8m0DLbBOjwXJ0xVWV6B7d-OtUvTJgKm7WRSe-VwDuRvrd-hiLp2cVLV7bMy6B-pkAm4YmxIm6UVsoX9ad1Z-w10bVyuvR_obX7qxb_gPWYgdBNr9TYmNF4i2xLyighSL_4ASroN4ekkryXhT4_ahacxJoeMOXd7e3HvAstZZ81UJ287dHrTBEnmfstKaEmgpH8ub28HZ_w_dF1tiBA_3qNvfB_LevB42Ww7XScN1AyHtjCFDYRDkMmqzyrZ4XJxk_PF6Hfzf5jbtQyfCQ65345mnXLtz2G3P2jf5-WTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی بهترین بازیکنای تموم اروپارو هم بیارن هنوز خیلی کار دارن به این ترکیب یک دست برسن
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/90976" target="_blank">📅 01:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90975">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
⚪️
کوپه : این 150 میلیون یورویی که پرز اعلام کرده پیشنهاد اولیه اس و در صورت رد شدن قیمت بالاتری اعلام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90975" target="_blank">📅 01:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90974">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC6DuZtE9DHMztV0Q9b5QSWeM7spYNoS7VvVSAibu9p1Y7DPQKZBc2B5twEV_0xog5c248sKw66dYvRXhbiyDHd7-a2I8qjqJ6dVFoL8Dar_Md4qB41bn2RDj9XMpPqCNLpMldrpKQvd0rQLH3wKyjMYX-9YVjiOrYTNxD5qJnBWRAzl1fEVEcTqxEAqkNCxcrI3lio5HCXdjE3XnUKlWZNNfD3Ur8WxM74lNzvtoT2pQ5tdTzG-jXVrOtWobOk_jDNtAUqStNYVvQXKWiqI8toj9o2Y7BNGil5WU2Yt_YM7tWEL51kTn64sOkbuANYmmfZdc2wuYHnyBsaQ4M0-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/90974" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90973">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fe1rBU8f4hBRNZCXImW23oHW3oaC05daTmyo-c74H2QD4KnDyeF1Su2GMMNiiuHhFiyFO8ijtq7Lt-KB1h1Ysvwj33stopQ0HWkb3zBMEkiaRpAHQnHXgMeS-YN4MRUiMSmQc_rWerph8EEknZ90yn-m9RCsCKgANP35_jlqckoN_ii22TRzo1LRYO-y97qb3h_qhOrv0dvYS7a5QMMa1HjWHA8DQtknOflhp8vHm-NYubMeznJ0WkMnD204FptKLDfbWecdGHfpip9V5E45Y9Nrhgnyd_5Ypwti2pzA5kXcXCjYlb0ImH6jERJPAL2pz1NJXWadiihw13TGwYYyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توییت جدید اتاق جنگ اسرائیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90973" target="_blank">📅 01:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90972">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qaUkdFTqqfPlHq_0HxR4H9YBuV8mXdpQUaz-2285ypo4muwby-PsTAG2H3cSQcn4rEXWA0jdgQ6I17JuWHAhup8_zpRboeES8bDk0GF8pABiQHNQRrUVN5CttkBNTiyo0SxACt8iokVb-mUcWm2A4VQ59aG3ikXAim1j21bpWHtKuo6pSfe4LZTMNobDMd944En5IXRURM_5w2PE4U_3CWRoL80f4gDtAXVAfcTLnmHf39pr5jxub18lL5Yd4v6evzCfBVMDyWA6EZG7MbffdeGkk7oyRW3-zELaI-A7A4uh-EjQvPI1t8Q4xMh3BwbQtlpLTXjzKD1HVIwE0ty_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از فابریتزیو رومانو | نیکولاس جکسون به رئال مادرید
✅
Here We Goooooo!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90972" target="_blank">📅 01:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90971">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGU90PGtDBpmJJHl57pyK6dSdXyFZnK2NoxJIp8xBrm_8lUn1m0xTifixNqOolyxzkUobJihum3GEJCzJNnX9-ctGBMnAHkhDyC-dHjlkuR9bz9-hNkHnIxidsHpd1j89hfnzLXERNV60anKXNLhH3OF-mK0sdUKkd7QEBjX-9gwHp73_MxScvMQTQkU4Mbi4S6BjkbGkt3cmPegivX5pFmChNvf9TJrBLHGnxZZPsnTj45fcgb8sJzuNC9kSPt3rLKdVshQ0x_XZishyJXyIAmoaMK9vP91amOUvOPxE5ajEbg92sK4IpvA1PyBGLFWsGA_c-UgTYVjxGNJLT5JGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
پرز نسل جدید کهکشانی‌هارو استارت زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90971" target="_blank">📅 01:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90970">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ولی خودمونیم ها   پزشکیان هم موقع انتخابات ازین حرفا زیاد زده بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90970" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90969">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90969" target="_blank">📅 01:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu2hIfdSjHWsJ6PR39NHrWLuPXSGWTwLDiabJWBw4qGON_EKhVb6_FvF0-TDMX57lb2Ou0eDroNOBml4uug8uRwzbx-KauQQoJdBkADxVZVmVZAZWNvHnN1Fn08fpZBZxr_50gaNWBuruLdi07lW88qPsFTHJUfezYJe7x-JGz31tBrGeJADClVgPrUFI7yI_2Od2wnnXhXvQ7Z4RRFMrWOOyZgqeY4olGsKDPhW9Z8oEGy_dne-c_FSPVuRECw3X0hqfpSHDVQTijSQvPl4p6W_mIiuq00dNt8dH-AcV6W469VrEKRpFm3FDUc09ernB49QyBSHlMq-GkznZspnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90968" target="_blank">📅 01:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90967">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">لاشی دنبال پدری نباشه یوقت
😐
😐
😐</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90967" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90966">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/90966" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90965">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووووری
پرز؛ هیچکس باور نمی‌کرد بتونم با فیگو و زیدان قرارداد ببندم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90965" target="_blank">📅 00:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90964">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Tb1CZeNNCRVMlKdPFaaY9ARyjEvY13xY95wY2S-3nk2tWvfxOm-5yW7JOUYW7lBmm4fEFiCiEa0UNDeeevwAiQwmmQkpdD4BhI4t22dQgSYt4NY2wLY_rzAIqa7uYidF5mL0l8gqGXVBOfb5rbhv1tbhlYMDBfkqTXZqRVLrpRMyY5eFbHIT8q0yYEbnMhzfVtiJCdLTAtO0KDYtErNRgsOEVbqWQijfdSHe9S0AWbxqDCDxzoyHaiuNlL2ruXFejVAxgusHHkPnyOeXvhQeuuMbMlN-wJWb99UwgTvxqusYRG7jsv4Rhm13XXUw4emnLWDJ_faA0m_oW0gf4m11yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فووووورییییییی
بمب پرز لو رفت !!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90964" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90963">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipsMm6CF-n4_u7s-enHvjTM-laQJfMwelUYow_vLtoTwHuo_FfV4lr2lu07RA_q9_pVmWS962w6FxltSl-Yq7H1RXHJY0Pys6M4z98s58JTWZtXNqwegzSj20B3-1CdsThIP876M_w6jYz-N_Vn7thi6CIQM_FcKSRX8ZKJ6QaQWCc11uQcrL9sHHMrMB5M9He5ZTnySSNoLCHLVvOZC4HQbhtyx93mgY-rx8Te58m4OiIfzjzAY1lEl9c3gFWbdMuBKduXIfPERTnAwvKlci3O1WsJbMBgZViJWEPhhyoTy5HNvFihb7l5h6Utan72-PBe3StSbF-609Hs2TaBINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
ویتینیا یا نوس؛ با ریکشن نشون بدید
🔥
ویتینیا                  نوس
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/90963" target="_blank">📅 00:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90962">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90962" target="_blank">📅 00:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90961">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
پرز تایید کرد که بازیکن مدنظرش هافبکه   نوس، ویتینیا یا رودری!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/90961" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90960">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
پرز تایید کرد که بازیکن مدنظرش هافبکه   نوس، ویتینیا یا رودری!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90960" target="_blank">📅 00:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90959">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام پرز،‌ پیشنهاد ۱۵۰ میلیون یورویی برای جذب نوس تا هفته آینده تقدیم پاری‌سن‌ژرمن می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90959" target="_blank">📅 00:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90958">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/90958" target="_blank">📅 00:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90957">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇪🇸
فلورنتینو پرز: اسم آوردن از هالند یه حقه انتخاباتی هست. مورینیو حتی اگه ستاره‌هارو روی نیمکت بذاره کاملا تحت حمایته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90957" target="_blank">📅 00:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90956">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
‼️
پرز: این فصل هیچ درگیری بین بازیکنان شکل نگرفته و هرکی هرچی گفته زر زده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90956" target="_blank">📅 00:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90955">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZmSw2rkVAccNendJGa3trvu_BoWEUDMnZRaZ-SW217xM7HFs-4MnLfIqTw-5KKec_637x41tyePxdbY9XkcpIgphix48UKEUeGsLC9UIVxsKkLppFeZ9gWZt_JjeUUvO9HDFnSCBfvpQataxS1eleRzaa33Tgxp3h_DB-5xO2Wr3kQcKzMdAKL5XlyMQxo7GZvGggS4eQAH2BHV7WFLcsO7kRt3hnCObxfjrJ7drxOZzVKc94UfJNnKnlP3wc3pDnkBfxNV-O8ewocOBdKU87mp9HC97fhRPMz-BG9DZ8tG53R1LGe3NY6dfTG3WFPbwAGa-r9wtZbD_xtmMIJ3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه به ساحل‌عاج 2-1 باخت.
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90955" target="_blank">📅 00:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90954">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">▶️
🇪🇸
🇮🇶
خلاصه بازی امشب اسپانیا و‌ عراق با گزارش فارسی خدمت شما عزیزان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90954" target="_blank">📅 00:41 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
