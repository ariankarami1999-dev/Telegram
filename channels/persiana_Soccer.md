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
<img src="https://cdn4.telesco.pe/file/EU5c2yAGjUBlWox8KcvH719BvL-vjFYZQNAhIakn7AAq5HIIESIQ14X3JtrDHabn5MUrZmFP2Ih4jn_OnIUWroAlIA944hM19StBUUC16xcCq83NS9uz3_WV7XJyu-h6_4-I_OSZe1kr0f1H807Rfvo0kyDYGkK_RGEjYDBX14Jj2BM2P1x2dL67EIvzeTQGkeQ-_8ecNBSsISO0HWR3fWAygNbUzppnlKHMqwgKUqihvNsxLUrTeVJwMSyt-mecCY-BsVXdRO9BILqPmEfiGeTvbJSoq5LI_EACeEbdwrCESit2_AUK8B7k05npJKTkPvigpGnytCF7AWsyBdbpGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 323K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 23:20:31</div>
<hr>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=kaUa6REGT5cr2Ta32179lq4IbuRMTMi_FOXoZcoFdq_qyPfH3yDKM3T6Rd-X9dSbyosJGWHoG9cBegvQuysbxg08a962QIHR8AKeZ8hLWmcHTPqNJPzlKlWbZxQ9NM5pcPt-DxZtSHplMCX3JWomaPPkhRfNDlnk-Z075L9IPnDMH7LC9ZzNBwFMeFNfd6m66Ovc-K6qLBaKjxzrqC9IGfZxDhgiwtuDb1Ob3YdRC7SdQnKLsHFZWlL5ZwkRyr7BXtskNLsLfpugDAojT5jwBngbt9KqFxUQO4tdBKqAyBRTKaO5MceZ_ZwdNDY4WJ0YMCZobk82Fwvhrd-mtrgL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=kaUa6REGT5cr2Ta32179lq4IbuRMTMi_FOXoZcoFdq_qyPfH3yDKM3T6Rd-X9dSbyosJGWHoG9cBegvQuysbxg08a962QIHR8AKeZ8hLWmcHTPqNJPzlKlWbZxQ9NM5pcPt-DxZtSHplMCX3JWomaPPkhRfNDlnk-Z075L9IPnDMH7LC9ZzNBwFMeFNfd6m66Ovc-K6qLBaKjxzrqC9IGfZxDhgiwtuDb1Ob3YdRC7SdQnKLsHFZWlL5ZwkRyr7BXtskNLsLfpugDAojT5jwBngbt9KqFxUQO4tdBKqAyBRTKaO5MceZ_ZwdNDY4WJ0YMCZobk82Fwvhrd-mtrgL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgFPmy2r-_XDZZI4R2M8gJHQhR0EbZX2ltTQhyDh-SvP4LePK6uVz-Cf_AxEUy3I_9WSLp1GBqclt5mwXwt6S78dB1LTbgokmXXv84GEV7rbw46TncKdN38ybLXrcET3sqhGsRHSJxWewaRIoph9sdugBZI9G5zwrHcSfRI1RrThWkn1ifAnC5gnjmobc4aDaagFKSM1pFJIRjeqdeC5czRfmda6VaPZbAWBavK8SOT67jtB5wv-m_M1Y66dXlG59FeqGofq1ah74Eh92R46-4Jez8lc4JMPeXVXGS-mT0k6a1H1lKX4yW8G9uK91WSnVtPJuI1aqPUI59VegWScfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqmPGL_rrOpcw7BQ_NN49wMXROdGDMSDSS_5ZNQ8VGQTR6AE7EXF8cuJ0Z4t1NFbnNxn9z1aWbr6qWB-z-0u_IbtdzwClz6CpZ8zxdo0aRbX50SHhFxudqSMF1w7vT90fDB1KF99QQW3OnLdVadSea-YywwlsQ8_IfwfdYC1L-Q_v-8GbJHr0OEjfP7Vvhf6RjYWfpdZvCSZKmQZboaKnBjUrJ7kq--5gVLzwXQtzjbufAi-W7nSPQgGXkNkCCOBBlLpiqG33bVFsSwEto2VpnF6soTm1WdeQ7zkz8hT9Dwa2A_N6x9HJXNbHC8G3qYXQBpt_OgtM5X_LM5kLntIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRcrWkUpT1_Rg9GSMMm_lfhMYzsNwFW0Uc1eakw5VRjx2mz_fsTk4t3zblqyQYZDGFV1-3DTK9Xa0k_LzMdogt8dp5Oa_vZTgHk4kZ5UhkcZWvjy-dYn8h9tpxLpACfiuGcxb0AR41dChFw64O5p1mB1WyxV_qpVq1nVmcWJJESL83ImY9fzoM3XHmbaVTFDV6iWPKjVknD0nBmlPwOcESh9lz3PcamftEXk-O_2c8JJ1aVVsiOgaaQrMzwdzI4niZlOp7ek9ZJDnZV29UXvMtb5ITKbaxaKfHbINlWGJxbulBiNLYRdw2zRV1l8ooGrvfwd0wV0Eo5RVWJdb7EL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq5bEDYrw468VjfchIFb5wCOXQCBlKaMoKUTvTExF1vS9MLjXHPn1WLGDmYk2oHGPeGU_-7_apqKj35A-5ma2mbJGT9EAZWmR9BTwwFe5EH07Xgm6PLfGmstT-iusii5O6hUq6-iWpXHLPBPcGj95Rl2phBoxhQEQr7osn01ne2Pxuvmh26sk2_hCc-Zn9j3_8q2wZmsfhH4bab5QgLnTkT75sO09fZRkwd5pk4oTIarBugnJ5QwS-D-ntzxyNi6CxqKt-nutbrViVcijJSCe1b4rZisIIAncwnzi9sSpoQpopueQfTco5aJ-jmF_hhoo7vQHgtWef9y3HQYb3tgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbeb7hXk3EwiMKcWbI-1bU1t0SDA_YDZkGno_dVcUFIIKD5MdAHl7yxCK3bGc24RawcCt1Y0D8MxfNfJTyVPgRwJrIvQLKbkRt4Pw4kqlAFZyllOFwMpMmXKnr2xsSHxvgQvS0YIr_4vmUbc3QOCNh53EZg51KzHx3jAKBuo0oxIqHE1U9lMToYIlm7Zh8SKCS44tt-TfjMC2-LLs6lKjZYgxHbpG5faNZeD0u7PXB5wa_DKNO9YKp1WQb6GiPs64hATGAdOLG4P9dffHW7CxcQtfVhoxSdxmmk7fGY92Q9csptDkQJEfnCJWdqiAKtUmzMUt1rIQZLl27EDxI2gHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCMS5wMKmZ0G7DK0ovXrFIyxpV13qG9HZIa1aSpySIFF5lFG9Fa2YVivArsoI9obZTbCinuCrPvcMhEjeExU6V-MsxNB51vTCZdNoTbsNQet7i52g6DHlmXXx3yedYzdUC1IlUiruoa2Q_iB1kfcXKRy2t0gQ7E8obscrvsjDAJnPxBa8S1JVd2IPIWDtcB11Qj6mI6z6tKmqeV55HbQ6iELImIy3MKvci19Zivz6qchmhHOPtV3hFHnMw9XqLcK35b_WiaB4b4au2RvKpxWKEJvMRSdL9GQgb7dRJqNG1BrgySaU91hhsa4Ew_uREeDcCtBvX4-WHeniZiFxPezTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l45UZTHVz3bJIDOieOkFmt4HLUlXFoUwhF_qGI1r-LecV-GRKnv2PYcTWUiYSp_iKSZFczPp8nRdEyRXiCb7gioXJxoeKVnrdfrssIFgSatjpV2Wh9U0PGmRXhxOmuWsr8Y7SbVeXJ5MR6DFI1kz96V1sph17OImEI2PWvmOg99yZAVnR5Dg3yjH8LsjMGym4TxT8J8x5-75kMULvuibYOeNSrSYiXbZgucr-Rus2TCGNKzG-2TRNE_QQ9du8z0-petGuF1DoDfcnP745wcCFtICrt5R-TPky9cXVGHCIQt1Yv-Tn1NO1JLi9mmghq6JB56Mnitf4wEAwkMcs4fBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkBqacVAAXT0TPLkF1a-ymhldOzxHbKgkPrRcL6StbyisgBV43Nw4uKGXECz3SPq-oxzx58l2y06PpmkugiwYF77uJLvfLIg2M4I7jROxs5Uq3otxDMbqeLRbfOQbOei9pqQLr8EnnuRA3G062EefuwuY2beSAhg68W2mXGWo50jCMP2Ziv_GP79rQF9gyBHSBMpLf4dp4aLfjipVQMF0j0BfiqXnqwXZUbZravzJYZvc3uIA4cIVClqVl3bYPBuoy-A2iqOEPFOFfT0nOOSZakqg09hAwDypKvNSaLWcQtTWzhOquE5jsSgPcuOkBu0DGFuo5iDhVHFpgpkgDGsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=sALoWcUCA2IOpkOhZ8P25XrurhU-AkEnON4p-h3MnW-HXAvlAOCSWGW_7aedBhzHFU-jvSNmANkdvAFlvErlh31t-zTBCqAVP2Mp6TNLfBZohfdgRSQRxP7iOdBcUBER78X-3WzPggZLuASc5jo1dY3CKKuPUIm42TCxR1F_Y_dJHAHKGR0v0J5BvlJry_OKbZwC65r02BLLsi2LHgMuyXa6TlvByw0CHvWbxqi4G5L1kaScPeCVnTMEuB7tHmw2xNZJC5Eb0ixrqCv5faYlSvM9fog0r8wpMFwj-ASlAVK_66TJcgOqMnRO4rotAWA0U2lVxq1VeisBfN2EJlN2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=sALoWcUCA2IOpkOhZ8P25XrurhU-AkEnON4p-h3MnW-HXAvlAOCSWGW_7aedBhzHFU-jvSNmANkdvAFlvErlh31t-zTBCqAVP2Mp6TNLfBZohfdgRSQRxP7iOdBcUBER78X-3WzPggZLuASc5jo1dY3CKKuPUIm42TCxR1F_Y_dJHAHKGR0v0J5BvlJry_OKbZwC65r02BLLsi2LHgMuyXa6TlvByw0CHvWbxqi4G5L1kaScPeCVnTMEuB7tHmw2xNZJC5Eb0ixrqCv5faYlSvM9fog0r8wpMFwj-ASlAVK_66TJcgOqMnRO4rotAWA0U2lVxq1VeisBfN2EJlN2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUf_cmzLhvi-LfLU1vm63U24P0wzrkH-B7ybda6nxyK6EZ982RI3NWb5QjPzXz65nILDye0ObiFwnoEcwryXHFbm_2Hh-l-E1v8yuWj7VoOeTiE-H8KdV5qfqVKuUirZ0l80YBDTrHJ8kmx3qu_ySlsDbArsMqDS-E0gNoO1TIIf_cSC2oRvfD6L6CwOXJ_n1ViNvIAr_5OW-N2qtqvpFQbWnlW5FSzGeAal1w05qitCF-fqrs-1G0H2VXfb-R5xJ6Gtb0Jst3g2ngq-pkQVU2kJQplazPdsu8DoCP6f0T8Q2wAf8xD7bto68hrrpUzmnUHZRwe99x6OTOVuDYawSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf1fT1baBfZeBAaqurmo0eM0StgsZmlKGfoTXoK8JPswP8WiUMwlssOvMZp8EFz4WRnpfXiJlTILJPEBOxJIO746b0TVlGGGE7vGwbHLEK9dPrTospJva6MCa_m9rNG0uCAKDhuUjqmoi6TmEn3S7CIsjRVANye03pT67-ubxJSwzt6XWyv0rUBR2gncjI_HWeg4RbrA7EAsexnX-frZAOTshYR8TiuUc76L8YSGQOpvnhYXae5SH8vbDQ721mJ7WWe-swW7n_gK_6ahYgGtv-B0787NW6-f7zVl_5CBEnD7tzWToAh-r5qE4kRr5t7cXWRy76F0TCtBm6uLFZljow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlU--fywcKBQougDMHneCF8p1u9upW9z71z0NpI51l-Q1AKKJbYYj6AmtkfOQARua7IFaUN8xBBOrjKqS9krY_3lNYissD-isN8ne6X9bGOC0qRfxuSzqPZnCLcZE9szX4SjmptZXbX6ODQwOJLcLGN_pOeHfcAQIuQJ7O7arMisNYv4NLlsjedxaeZvSlRIZ0Ff7ei0jFjpaGxBL06JBbB9WQqDFDDzsfUVFEdYFTetG0EQ9QDk8XdMifPITKFAb7gMG6UFPcq-X__dre1yavqFS0QOavptwiRpiDoDjKyG6UD5SocWnd-OAduBVNrFTGyC936e1z-C2At8k4JDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0SGpEhvj3pA0QjvJPwWQtSdljBzk7o0mIgcNackYvZN_ANBNL0EiZZjMStPUmhl1vD5iWaK04KywXSI9KiQgdLJZLndo8mtMg774j4eUWlfq6xR44IPLIDfCtwNmTyx1jga4ewv3I4iCZy0gkkUfOHr0hSWQY0UD5kSn5KbG7ko-B2OwGobMWzNif47JRaIBhDOyCHHx4aNp9b_s17nr4daPnSLDXg8zPRJ1ZqQsYAFUbAhp0cSmQSzgJ_qsVxz02oGOZFISFbJoB84ZSMLnpzNB2aqdWuqb32vg_m3krA1ZSvL14RVCuFjGIr3cmeLYiQhYJuOBc7i1ehDXyed_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24471">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fqwCBfYfCGbQ2CNMUYa-K3lN1xZEozQ5e4T9U3TKYkLPRmoQHmD3sQqJTjhaxxthuDH3xiAUMU27qln_bTfcBPbV0WcWFIALFcsHItqT86ASRdFBptMwmSIBeIJAbbe5YOqjRXbnw0VwmS7POXV8sbmJ99J3K5rGSjQYyj3bUkXjcs6hD2rlT_mfvEb43p85eCHh3-FWtDCLPiAA8dRWFpYb8SSRcmmAs2Cv5W11Cncl3hPDnqRdi-QZt42ZDDHoLygyig2kIfKRL-geTkEJyZESm2m4ajx2tvECxNpVK6NKC7WvUdPHeBV-vUye51EBN7wLvV3w6fz8J_BqPRgvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
با لنزبت، هیجان بازیهای جام جهانی رو چندین برابر کن
🎯
⛏️
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🔝
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
💰
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از اولین واریز
📇
امتیاز وفاداری با انواع بونوس های روزانه مخصوص کاربران فعال لنزبت
🍀
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
G6
📱
@lenzbet_official
📱
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24471" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzddh3S9A0gKM9d_5xrvTtgPkOhFIhW0NqkuqckpUDx5oA3yCSEPa-O4xU-uM_jJDZvFKjX00pQ_PF5cq5JhA-nTaqazCLPuAqieV8RWPdavUYsyi2lL5MwL_tax_OjEJlTerGEQwYbrvgcioCHRpu4IRmL3T9VtDMpGoO01PpIVXxPED7GtD2VgLv3XtS81mt3OiawRZsUdSGbmnGIznNujeQqQAjECF0vI--9qu-K9DkLlPgXdlBM3MLmceT5HZAty5g31G2v6EIDrA_f6VcG9XulXlYg4QxPVe2KPE_neHp9TgoqHKotV28JudU-kvRjzoxHLUBTSEljC0lUtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTJPecoUXtUKZFl5nT0gP0Hr5Yi3GNSfXuOIM_onkA3mrYjGZxghDJTNt2jJNRG45QYlNATnVTQ_4o7OVhW5BAe8zvjWUW_OnWBd8JP2udf1VV73CLF_aL9jJPQSqCgpyo2NtRtUDjIwAkEZ7PohhGEwsfXhPYm0AHuKMVXzFkvcXA7rOtL5fEFCM0J1QFSdRXGE0aROjDe9vo35J7yeaxIHKRjKuZI7La8moL3LkONYXSxvWTRPGcCKZWAndSX17g6R0IMCRavVS_0VL9SgMSZNkpRPkIGUv4-QMlXudaMWkj1OdmY7ApgUIRVMPhpOFWfI7UXvUH6UCzwwYHA-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbnnzt24GrTjoQjNMmcP-AAzOvgGfvU4zUeRcBsKlNdm7BrxToj5kfV7REotrF_W3_Nysd2TtqYDg9fOyTTeOTkPLBe6udTfsxDVtF9vpoI-n8m4p5j-UKJd-ZGTgR9IpD1WTrCUxxBXtxmU4vx3Lsu2VwRgSDJaHREkWkSZfvpj3czoLTm15aIe4xWOrPvEW8aDcIHB7GmFrRjrG2kOHbokg-x53NC6S5xhpz9UNV1dxvtn0aD0xtgocQLCsw8IaX2oI8BBXEwrd13tNLmnAmK5-jQRPIiLV4eWzDwAsqGA4y9Eu5fXYBOyAHkwoJAJKxPuNoyeUreSTtT5RvBjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsGMifHXJV_0ZrtRNJ3rbkAmZr-ngSeE1zOuxU6vfNOkW-cV1L8hzjqf5rPBGwb1I1Kg4B_JjC1qoms47XPbNjhWsN2qYaPIKJvO0ClmpinhSWxlDlZtNz7zzmzWxG8wotI2kwcdNvJkO1zbOhw1nqu_hNkPbUbQrqRS2Cp7z4p8H8Nq6Uai96T_W1yqhmP-T3viTkFWQRQ6xVcEXoOv_Xlv0CSLw6h3UE3ZFDJWOG1nAEjUQo2EQmEvi4q2LgJxrFHEU6F8hujtwSfa7OYXmYpxjN5kS-c_pdH1EHVqGe0Q5jr0rlLZW73GClosOgXoEeyvSphlMbF4e0H4l_Qfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7vx4BE_YWhYp-qqyioLFeqUj8GgJCHUy_YzzeyIdlxCl3ZsQEV7kMmCvlU-K-XEcszK6uiWeAdEVQ50SZFZ8Op7L-NZmOp2pOQvYSFd7RytCABrnmpJjHXskgXj6NTlcxeU6Up9moMsLme2tJDn2qJ23L7-x6dImAl-cTR-H69wGspkiwrS43T9L20EYvogwCTN2j9Rb1ylInsvN22EN4j5YvVAg3imdOZqqbbWHTtCeI0rkQXniQUme5F5P2z-hmpT7NbAnIzwOMIlN8yIxcZAiQCIWCKEeM_uwRQM6lD3baFHYAqer08ZEvFO0C-fgchhbIzUUWh0RJ_AS8HA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKk7FD0gwumuwarwtXGYgoh-OyNcOKDM8CVOzSJDGtIqzSnznYLTVgNrbfAIcapfBSHqiQi35ojy1ZiSEy3IgwF-WMJdBaLtdHlw1IMysazewyfqibwOY0UGK8jsh8kXKmZmkwBVn-6cEUSTlByqtDtNcedPmkO_OmIfWq5d74jH6QQzmkI2cvT2lBl9e2hkfU-3ung5oIWuKbfccGnVQSC-ngi6ASblBZXwT1t76rEi3P92hjPv-uCR4GJvSqDjrwSvo2fRfnPCeNdsdWBVn0GuMgVwhu0FEmhCb6Jp_E7YkcYu2YUhghYtck3G20Nvqai5d8AbULWV3tB-UOfB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZhQR8zLAb06zPZjceI6rn8cGlFMcY-LZLJPltvns64eMiLa6cZOySGqzhnpcVOIazMSexACUAzWV2ZWdoKqMkxxXVWUlFUUNH3v1fy-nlZqZUYPd9wN9rnhlyuz32sKPJtRo13ZUnEeg0NIQ2NSLoY3jhCR4qHuATqxjJo0icH_YoBgpsXv4OZ_Wly7TAtdsy5EPTEdGa3Yl3FKxCBxrR7bA5c8T8khcIH0-lkkYDabrZfvLsOC5AauDWRmA8fzDziE2J9WLx7tTcr36JaV--P-JdYrbGYpdEV5szLCCBz1Iv3iK8caxnb_0o3pJiob2KIkx13_0UQ17YecLuxRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQSnunTtcKL0vdieXEwMC0XsLji7RJxd4FCdGzQ97LNsDpLWsWeQIEpTEPyR5wpOuORvqyGwThwNTjKkq7mh7JCSoMuLziMhKOX3pokyvmWl9HgTyBOABMOaq_n0_CHBrwIzBZKOTjgbqFXVZOvPSEpGAJ3mvag6XJqF0AHXIrqKN8tBaWjpknjD9T9B9oouoTQAv_tgxawQhD0RbLdx91xplnqDTE9l4lVQCXNFidO0462y4a2BBVPsuXyuzGMInhUhldcyWCDHurVu4d9oKivfaA8vRvej1l2Ai152wtYPtHE0MS947xLvIctb6u-Za3oUVzmLn6hPVvlvkF6GAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=DHjYVbywVc2JHi3DQ4EpDIGNi9kAyYOpggzobb3Z5bwLjhCeE1nuTe6eJcukYBKYVaUL45Gmycpdw3xuinw2sJBTIAWA9sTlaYsG9gwUo7Puj_o9QNHbvJf6nZC2cB_asy4uhfmuormfHIdsu_ZoYr5kfjOZkARIuodO4BPy8GL7sZDha29BoQqA8BzEXhIatfHTppGyjY12apJH9Wp1eHnrpGs5PsKJv_EJDNjGpb-1Btn0uIIew0YslUfex48u2n2JRsmyO4xB1XdQqmTrL7GorA2zNFyJex8AQKpDAOi1nZv0apv0iuYzbhiMPEBi3ImRBZP23a8sHyzodwSMrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=DHjYVbywVc2JHi3DQ4EpDIGNi9kAyYOpggzobb3Z5bwLjhCeE1nuTe6eJcukYBKYVaUL45Gmycpdw3xuinw2sJBTIAWA9sTlaYsG9gwUo7Puj_o9QNHbvJf6nZC2cB_asy4uhfmuormfHIdsu_ZoYr5kfjOZkARIuodO4BPy8GL7sZDha29BoQqA8BzEXhIatfHTppGyjY12apJH9Wp1eHnrpGs5PsKJv_EJDNjGpb-1Btn0uIIew0YslUfex48u2n2JRsmyO4xB1XdQqmTrL7GorA2zNFyJex8AQKpDAOi1nZv0apv0iuYzbhiMPEBi3ImRBZP23a8sHyzodwSMrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=sSfd_f2rMqLJSfD9LEmOGdKxdeOOcAYafmtXmPUDG3ABBzl_lvzUa6WW_9rbd_eEcuOOIvNPdCrSOilvVTuqTrHlkyqldq1l7V4db8oB_Qs6neKP21QdiU3a7G1EvLFWVLOSATnSgHM7tRiv1l8udN_UTyHkMX1TOpNAaj7KjgETpgocIUGQ9LC9J8jqpguyWuXlleFYOQL8l2RiN-jrq3BPszn5b4v-ZpjAKHFOA7UaSDkPLpQ6h8hq7tomYSm4ZRlOOGvrIgSycBz69LIFr73miBNwG4H-G-HJCJvqLsZI1aOng-04q3iMHhOm_3lkjmGgx6trPO6Vd3XgHwNqhk0RSg0S5mutlCp4O9GvmYn842VL0Bvr5QBOSbKOIqCVCEcm6zh6EWR03_ahDIFave5nSYMKpdFXMQselFphJQVt0IUKOf_H2yYKMpRnl6Dw0kD86eeHrUukBM3DfAvHHTEu6T52Ms3XsqjBRiimzpN7MT0Dx0LcPoXG12I3d4mpAhc3lDMAQMgM-BuWY4PltZ9PIxsvIACP5St2XTnqndqMm6YX4k1ShcYQCKKEwH6_3vB439nPya_chCTW7mSweSBJ8iLKLbAQCxCr9DmWGm_WOJ85tX4rCGaPX8XmqV-QvvH0h2zqGqq34RiYUAr9SkbWOb-4K8Xc2mrUmUD7AV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=sSfd_f2rMqLJSfD9LEmOGdKxdeOOcAYafmtXmPUDG3ABBzl_lvzUa6WW_9rbd_eEcuOOIvNPdCrSOilvVTuqTrHlkyqldq1l7V4db8oB_Qs6neKP21QdiU3a7G1EvLFWVLOSATnSgHM7tRiv1l8udN_UTyHkMX1TOpNAaj7KjgETpgocIUGQ9LC9J8jqpguyWuXlleFYOQL8l2RiN-jrq3BPszn5b4v-ZpjAKHFOA7UaSDkPLpQ6h8hq7tomYSm4ZRlOOGvrIgSycBz69LIFr73miBNwG4H-G-HJCJvqLsZI1aOng-04q3iMHhOm_3lkjmGgx6trPO6Vd3XgHwNqhk0RSg0S5mutlCp4O9GvmYn842VL0Bvr5QBOSbKOIqCVCEcm6zh6EWR03_ahDIFave5nSYMKpdFXMQselFphJQVt0IUKOf_H2yYKMpRnl6Dw0kD86eeHrUukBM3DfAvHHTEu6T52Ms3XsqjBRiimzpN7MT0Dx0LcPoXG12I3d4mpAhc3lDMAQMgM-BuWY4PltZ9PIxsvIACP5St2XTnqndqMm6YX4k1ShcYQCKKEwH6_3vB439nPya_chCTW7mSweSBJ8iLKLbAQCxCr9DmWGm_WOJ85tX4rCGaPX8XmqV-QvvH0h2zqGqq34RiYUAr9SkbWOb-4K8Xc2mrUmUD7AV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=Lq3qmyiNnsLHExPWJYM2BaADEx20k1K39Mbm4Ka9SJSRnvrE20s44KAKXP0NCSDOYHE8GJ38AN5am7fnVJtvubMf4bqDblDcXV3J1dVrGL5jEuIQn4m555Y2mUnMoY38ZK3CzNrk6gyFxQiGQ73Y3TDDfY6IKj6SkyoWjXnTV8w14FdfSIN2Mp7ZQ4vDK79dI2R_69UtFtj4im4mKkKwMqcem_hnMvLqIa49p_uWcRukfiLGxRr6b0JFcieG6zbZ-dkLp4boV_lQRak714dECgzZdXdVqfuRdLwHOSR1Bg2p6cCJtdbLBdYVfcw-PsyNXX84BPEcSm4xE1eDAsWAHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=Lq3qmyiNnsLHExPWJYM2BaADEx20k1K39Mbm4Ka9SJSRnvrE20s44KAKXP0NCSDOYHE8GJ38AN5am7fnVJtvubMf4bqDblDcXV3J1dVrGL5jEuIQn4m555Y2mUnMoY38ZK3CzNrk6gyFxQiGQ73Y3TDDfY6IKj6SkyoWjXnTV8w14FdfSIN2Mp7ZQ4vDK79dI2R_69UtFtj4im4mKkKwMqcem_hnMvLqIa49p_uWcRukfiLGxRr6b0JFcieG6zbZ-dkLp4boV_lQRak714dECgzZdXdVqfuRdLwHOSR1Bg2p6cCJtdbLBdYVfcw-PsyNXX84BPEcSm4xE1eDAsWAHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgIvApAJAMBrfQrVPliHW411TIitBAaMlRGhZyh4dcGZhhF-kShPxZ-K62Xvzb_2tNZBwKbAUbQ107ItRnbfSylVFjhe5fyTCALoKqWbtGklhIWA4cVmb4V3eYnRolbLnlnRqmqfPYcNI7JDIMMGHdyuggV-Pw4QUkrxlgVnMIBWhN9ezVSc5uE124SvQ9kVTfAAqz7kips-EyF4rDtfz06bWuZ8fUsvBJkHukLZBHeyoKMKi-baRAexsvFTm_SV6XnLOxl9Ai8oqlQ550GfucpHpy34j17g5DPaikJw6LPxEBb5vVgeZKk-zDQaSz2u1Ymj0rMxxdNtnrQiPxZ4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS6eJEqrJZvesYyoBO-tM2rToogYx5PO5QMwtAbCsPb3aqiuVuAGLrpjGCJlQzImlSAlSzPJRjuI_TJNtajerGKqMNg5oz-nSFmPWNqEKLjidgmRCsTMLpKsAE0oI9wfTybwfBZ6TXFMrP4FkNBukr337GvzE4HH5ArFbiOsoX6E324x9zLWHYE9ICW_yH161mzav9fwwNvy4HOIypFDYYp7AMTN4K1NLR_mOAy-dZUFxJDlXvSOi9yTlKjyotk7cfFrSNCQg-oDE9hhusRyEYITvrYmAVaZMSNRRaKaCA-LyzIybGBf1F2qxk2klTxr52tnqgrkcF3MRDvAcji10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=DrTjCWxDub6HmYXEU_xa5zQpXGhdx7HtaOHPOR0Zmf2EPkqNpBRqsoL3VE5vQdFgXOMKsJSdY0jtUz_3AG11ymPdD4ud6bRbF2sJNR8zWPcre8MlrYipgo1-2MPpMr5-ocwj8qfPOoUgeYBmMzQ4iv2G3sWzmoggXmCnSSABu0SiDtoUQXOeJ_2emnz9xhDUiwi7QHZzbsL1z1p-ctZ6KvchFi6ALTjDwKYdbQOqqTUrxbPX35wZPKaBteqHnJTJkxJj4UCkIqZoWvuiEogGva8vB4Whh8S0Q5N1hSBDuLnvj7u22SDV8_sObySOEtVuOilfZOVizQ6Ol2nRM4g07w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=DrTjCWxDub6HmYXEU_xa5zQpXGhdx7HtaOHPOR0Zmf2EPkqNpBRqsoL3VE5vQdFgXOMKsJSdY0jtUz_3AG11ymPdD4ud6bRbF2sJNR8zWPcre8MlrYipgo1-2MPpMr5-ocwj8qfPOoUgeYBmMzQ4iv2G3sWzmoggXmCnSSABu0SiDtoUQXOeJ_2emnz9xhDUiwi7QHZzbsL1z1p-ctZ6KvchFi6ALTjDwKYdbQOqqTUrxbPX35wZPKaBteqHnJTJkxJj4UCkIqZoWvuiEogGva8vB4Whh8S0Q5N1hSBDuLnvj7u22SDV8_sObySOEtVuOilfZOVizQ6Ol2nRM4g07w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvSYX3bX_g8XJw_PCObkc5o04rRhyEPpHBoyIetAAvQynr8cu8ETyjInlgi2B3rsH7-vj5ft1D3OGBYRsV823SwRMfvcoL2mkBH9eWTEzQGQafhhYbHiT4GM7WIivqkeVLdjA-EISpoKI5OVUF33wBbxqmFE1zFGE3B_LMixVDH0-T-PyKN2yF0nBxb-l5VxR3OixKGGK1MAxTL3BM9XFkJsbm4Ye6jnzDfoyX9US9vRx6aYWdPaFPPLOhlmQd_SBpLZaT18Yy7TDPdZ021P2A8Vs5vLpA54ZQyjtq8sNcB7lnMI2G549GefmYK5YtUfIZeTGfa5UcMLKCyTCvzuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC2y0TSCmb2XIXhJdtNNObA1w6s4MLSKGIIk6cVH7VdY7bAZIsf2mV480QT--FrIMPu4fbTbrwCKV1_iVsZ-Mj2KhMW_vK6o5mP3EHUMywPu6alAphjFcsKdtxAL_wYpZDfitlxlGsOfwgrOdpRCRebkqCIKhfo2Fnlrxb8fQvbeHEkdlSHPtvfSKNoCtDNeekk15jqO0UpFLF5Ig8a15aJHZxYB8Pw7mRnDZrg5sSEJE9sXTndAei-463NYfx01uC2agGRQfmihDzR4k_465wJbTAfNJlA3PhFG8Ha4699cPbvr8tkQo8Hn0Skt1490zWvdJWZdDvmwTscGd_dEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEtjUhhRiO3g22dG1yapfKUT3Gv2HUVzDhSAAJblhgB6AG3-2ckz3ypyT9f_HGn2AiR8pxC68b7gYD7rby2qPgSUPQQN92pQls-k7PO3ZnSxWIAeD5sMCB7PPezoNHgjKbAhwvmzltvc24Ms-Wnkbh09s45DBcn34ECjdjhnH0w0sDI4jizCBLTTFgry2xj-Np3hmZFSnGAnCbLN282sqEd8fs3bs8xl0y3M5hM8YZtHsG6sQLMAzKnSImiUBk9cz1u2GqNTx9IY-XqnQtPZxZj3FBC3E7qvxyujX9Q17kEtoCwAi4Yi5pZGmhtJTqs4qYhzza-4G5tvCxkSOTNj4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgMSSoV3RypEvcEO60A9dHPsptYeyj50eQLCWDgaNQs_za6qWghtb-IaYiEhkQWhtP2orBd2IXS7ssKkN4LSpwCbaHkn4q7v-WLb3EW2DHuRCQcC8GK93lGhV47_4pEpVoLMNB1Kqd73dhQcTxXNdfW53P0-o_cAS8UqYZfbWBcXSb3bUW7gIpAUwXMEWnoMI7QuR-O8hf0QHe8QPJH52cczz08LCwp8VTdhCUtyvlbhCOR2frncKo0bc8DB9Y5KxYRfcejvDwRfPKECcCD3yfXb9mC6RtbCQn3gqa2f0tVbtpOmvCC5L78KB_vvV4ndsTwfa0DFJx__2tJpndwJAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkO0YMalOZMi7jZXO_FILQEng3da7PDu6drYPrsacwaKFndnY13-cYOd33-LfRUu1iHRW4Z4-6BUTlLOudqFhjFP1Q061wnt4QkJs2dsQEkvTJmlX0-O1AqgYZRpip4noPBri25HbGLjXGmNgHK6LleRdy96UB2-IT3cLZwR3lmsWsFQ_POuD-6l4yUDTHCMrifXySSBvoiTdDr2v8PQ6IKByGjnYrYf-yKK1ChdYW8-Mq-4lYz6ep1m1iHaVR5K9Ni7QlyOOHFM4jALP0hL7jN1SepD1oSfHu3hM8cNttBcvJgyI5B1rGOHskmY5v2luo_g4HqL9EI74mbQJ-1ebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIGpndCf21xFU5kkHlS4RfcQOfKily703skAjyODUUw79eKy0Hq_NRWd12nQ45MVqA1lWAojlcHIX8Nw-Ilkw2ACP1rTwAdk3cVLY6TmWAMXxqUWIPQOy7Ys12oFGxTWCdDRHqstBaWjH-XE4Bi2id9jRRUbj6Sd1VLRQDLNs1hWwWc2cgAPSuURg4OUimcoY6h-BttbbF3OUb1F2jCgs2rhK3MlXpOpcxam28uFxopnMqnKVUrx8ZESB8YmoILvjaOT6EnHAFlgx0A-hFQs0ZiDUavp7jZNUBrCxHO0IRY1CqBWifFGFvFJu8njvjaEEiCO7SAiJ6GZslqYoAa_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thm8BtiyZ1Ud2gxucbnx8coPNxl9DLJlv_zKnLd7KWu-F8k0UWH1ngBm5uVf3wdWg2_eB1EEs7aAjZz7mJ8QzxDwQLFX4rpw6UrpDptLAAedmeuJdefVenTYEa1XtFze-OIUR12Ax__vM1FmclB0vd8v7DU7KlVWhYcC-T9_AJ86nWg2kXzlQRhUqRukh9HNjr9MVSTbSSye04VRnl9tMyOFGXKgrzca2kUI6fgv_GT6X3C2kRJFzKfXjN76uU2DCKgkurQ20WAdrGHES03rMNbpNWIbu-HhnYmaOevWKmiMMu7aQLyxKlyslr8VhGcenckFefHpwXmYJL351pg4gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMeNt07EqnhvYCQb_pkwdvjo0IhXabu41Mk_oh6zbi0-YB2e-Ocbn3oOKBINfGDPyT0Blpv-2l_jurMSJHXcIT6SbkIbp73-QDHXlDDOawVJgjMMCVrQ9O5u5ierff5JGu_NhVzJkYcC8QoH_nLI4eXHstYOlXVnOpMRSYNAJ2RfFOmjnD95QtN8G74B9aJPN1R18UF7Ou5LBiNv0xIVyt-MlssrhSSdr-uIwXPK4s-rk0y37BHF-VIUHeLpZAT_BIwvBMIPk-RHJodHxW4elcYKa7i06NvKz2xPlB2Z2V6cM1DQLNlaRlH-z6sg9P9TpfDmfcMAbzkiVlLtssjIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSBgCWlxlpCXpjnlACNNYASwYBO0qj5jj9G88wt0Wp8Q-JTd8B5k_du21kQwaaZpYqYf5TUxpwahqSP8DXLyvrZ7aojsuHoGUMQTn53jK38c45YpT1LCVqvESZLflZUdiYDcXfCSgiWg64NXqTpv5DAnZiCJspP7e0P3kBXDuhiwmTU5As2bRu7rmEEPUnY_3DOPeJ3VQI20tklQiQX9O9-ya3fZkKEiug8j8d-WTcwnyPncJ1-JfPaZUP9V25QC4o6LjJ8ODTo3Wd67yPzUm_aTTW-urig7b_jHEQjDMR_Pvc-l505PSXWaRtrqyjzdkzEHDFvJNZdzvwIye-tDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=oGsdN3EYv180zWs1io5jjwjt_j_NwCww2KWLyaAJxacRPUQwdSIuigoq3oXLBKSRpt6HxFGJYXTmvnnMkpb_CmdTjmB4weoaZRq_AN-kcLNrksxLnDDjNZidjT_Yiib40E8kL9H2NcYeK7XwJW1-Y2L_i2B5xWYqsYYay7hhYIpYfw2l4a5fy3ncxN4F4YoKTrdYM-zoy6KVtCyRIYKlJUaJmWyjRZgnIc_qRGO3CvVI7vDoaQutZsAVry9Owc85SLY3_kyMfyaqVrBg_MUntCui_kfNrAIakRL3VW9H_OhTLq1ulumKaRpArlyo3L2oCyKUY15x2RJsHpINeQxvjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=oGsdN3EYv180zWs1io5jjwjt_j_NwCww2KWLyaAJxacRPUQwdSIuigoq3oXLBKSRpt6HxFGJYXTmvnnMkpb_CmdTjmB4weoaZRq_AN-kcLNrksxLnDDjNZidjT_Yiib40E8kL9H2NcYeK7XwJW1-Y2L_i2B5xWYqsYYay7hhYIpYfw2l4a5fy3ncxN4F4YoKTrdYM-zoy6KVtCyRIYKlJUaJmWyjRZgnIc_qRGO3CvVI7vDoaQutZsAVry9Owc85SLY3_kyMfyaqVrBg_MUntCui_kfNrAIakRL3VW9H_OhTLq1ulumKaRpArlyo3L2oCyKUY15x2RJsHpINeQxvjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=cdT9bMagDxxxRlHZoBpCVO98NNsli9vHatGry2kNDLVv5viobfSI1jzJeB2NoxuwtRc8i-GI5EfHpOUHtmgCFf_XHkrB657ScIbxt89SXZgbgPGs_uB8Og9ynSSx7sd6d8CQVP6ndRSal87I10kM6UBPL665cVmU9sk-tUnzeQhMd--clKK7xPdU9IV_c7HBi4yh9kDzPO37foYIS9MZHtRKhmEOGws5tTjFiqm6rJ7jw0IoVrQnLXxNA0m_EUnX2iiygXJVgdFeiaNFhpM6LI_l056PiO8mIcoSMYXeN8czW1MgZVXryPeIYm5LLfPEypk2s7qoXLFxmNGBoV2RAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=cdT9bMagDxxxRlHZoBpCVO98NNsli9vHatGry2kNDLVv5viobfSI1jzJeB2NoxuwtRc8i-GI5EfHpOUHtmgCFf_XHkrB657ScIbxt89SXZgbgPGs_uB8Og9ynSSx7sd6d8CQVP6ndRSal87I10kM6UBPL665cVmU9sk-tUnzeQhMd--clKK7xPdU9IV_c7HBi4yh9kDzPO37foYIS9MZHtRKhmEOGws5tTjFiqm6rJ7jw0IoVrQnLXxNA0m_EUnX2iiygXJVgdFeiaNFhpM6LI_l056PiO8mIcoSMYXeN8czW1MgZVXryPeIYm5LLfPEypk2s7qoXLFxmNGBoV2RAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mn7c8w9_E7pafB151OAOHms30a08JA1DepkeH_5wGNn1dfy2sNXkjCtd7XQlMolM_UdVN-rqq4Zs0YV3hCjOofAE6oyGt4a9LBFFrtbG-hL2S0CZ7YwsgQfZoubqdkFqrnkmD_h4VZWsJKDEKY4ISo6IZRYxSOir5Z0vmw7fNYDm35IfkIgS3eQx7oADixVhmXCpeGBin-Tdh8M-x4g5R-OvVJ2ER1zIuQaumETU2frKvsfFA7JbKQZKEuaq4iFVmpPYuEZILj3EYwWXf0rA-yTdOqjm-SwgioWRTWaXc7K8sLd3klK1hcU_R1CQ4B-wWkfHfxotcF1e4DbG3b4Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود بسایت فیلترشکن خود را خاموش کنید
.
🌐
Link
🔜
MelBet1.net
🌐
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24445" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgc4JjoXi2dBKOR5FNWarPG-ZVqX9I61ssTe2ma_mZh4EVLPFv7dvaAbk2EUj4Hpa_fEQBHbsaL_nsKTXsRUpl7whlRjChk92F32ggTMm0ZERpH9_plZ03awtPTHT3Y8eXgr8gih3zbr-MNIUUmRHan76ChAJMH4Erj7alpnbGtDnFQorhcgWzeno2FxmWET4V93YpOkkxrk3q2BL-z9adC4ej3An_0SLL2AB39VJkwOQjrHWvJfIXlOYvxEcO9GB3qpgrsQLoN07WMHprbdowRZg1oyR6vYc986oQAcjJnFnia373fozOVk6SiFerIbg2atskTFYxLFHl6GwPfp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd049s5gF1oQAQAxMwRKCdhLq-zejrep5rJlfJ4M_PGZNGHELz4627OrzhRVb1t1ib1Euj8q7uuCWJUY26Ua29ET3fBXQhwYcHHTKqQGxBcUfqRBa6Wkg3tGE_7q1Z71wOnqrVJqbvaYRtWEuFnslTkMmpVKN9Lsqm87APo8ZJr5y8RCh-l1wlnWE9jw_ivxtGrX4Y5kdUopvNz09ZWaKNVbM4Ho2LFbMV_lSpeY6Pxr19boTtYq3FELOs02_VUyE3GB5W5A8p529KA0-uF-XWJeTj8FY4yGV8sl--RX-AvuhsVGYwz3SFK92KIrB0qyXfIzs6Xxi3vlY2gx7rHzJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=lFD2q7YY42FK_U-TH83jEQkmqwRfsGlZuNItfbvKtCa2E371cG5LnMPxR8aZZUaCoM4z6ywDx6uHkh4qQsnqrzenblzJZB0Zy2sCS3vD-gSSrRhLKrOUpLNBbyMkYh9vgUil-HMG8syc1D6miyNxiXjT8VB5xuPCTki9c3P_5WG3z4zscQn4u2UrYHwJpnURHvvTr3e7-8wFCl_8XEz17s4tocLCwDofAcAFouydV-cOnon58Kyu6VOENuhHEhhOZw3LNAXzMeOYBBlWbaSxdbKnMA-wM5xOcJXQg0tIOlAL7A4uZF-nhPUhbBnx7szZxrsFvHQyTKgdsN0AEV2A7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=lFD2q7YY42FK_U-TH83jEQkmqwRfsGlZuNItfbvKtCa2E371cG5LnMPxR8aZZUaCoM4z6ywDx6uHkh4qQsnqrzenblzJZB0Zy2sCS3vD-gSSrRhLKrOUpLNBbyMkYh9vgUil-HMG8syc1D6miyNxiXjT8VB5xuPCTki9c3P_5WG3z4zscQn4u2UrYHwJpnURHvvTr3e7-8wFCl_8XEz17s4tocLCwDofAcAFouydV-cOnon58Kyu6VOENuhHEhhOZw3LNAXzMeOYBBlWbaSxdbKnMA-wM5xOcJXQg0tIOlAL7A4uZF-nhPUhbBnx7szZxrsFvHQyTKgdsN0AEV2A7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDpk-RduazLlnPgZr-_5n9K7IF5-xc2KEu5P6bibJ_H0ABy5AxWFhwc9MClgUM-lJSC7drZUcZlJxFyH-UCSnIEHLDH9m4i2cNpGUfU3K2Fv5SJSj2WDQhbrc0Bg_nUvYxYli44OClldhfdkpA8KcgvLZgitDtsrgKyaJX0vHxMkqoVo20WYGwas1GjKQPSPWcGiPX_gnCPdTjz7WxuZOJeFQDkj-lfQC31mZwh8kWuXiIxyd0xV99MjgXUC8QwJ7pJj_13PM-3d2ejKjjPI6SDod4XRiyRLDv2KNLMMCTsj7XYU26FUC8pGehGyVlNLN59KFZYb9T4zrH8NOiaGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwua5BdbN97YHiEGKakaCFKvapatPxyA8_jjCfI5iO0D_CVO7YuCU7BL23jEqWqSFvZ7o4u58-5zlourmVEwX-YLJXtcfAdm1kSCbqHb2Zsa_TepleRsMss8rrkzoacNDWXLaiT43W7ayoBngPF0p8S1Hb2QohEljOrRC3DfoSM1hk-S3UgLZLF3_fHnY4jy5880VFkQctYaummyUuHDD5Nx1-hiyreB0zJgwPBnkeKRwws7S9UWpf7jd1h0ApKzKETX4re8iL4176MyxU8LWyRGo1IJFjQWczU-CdI1kbs7Q21HOMN4OFVUvfdWz8op6tWr9xE7DIDokw7Gqkrn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3SYOGDssPuc6uwmvaxuUKqQsXWutxCBdAI7FnLnasyFk2n3GHCDzj0JGi1Pkh7GU7Gsf7-Fg0dNeZ1QJEhDc6eO4kfA45bhPGKN-KVHNLne2Cc7yE4cHmb5prKgbdebwc2UJEknS_EJJtvroj9qD_SuBc5iest15pmXPnnUcj6nEtM-QwHVdKeLCpcl1q31pPREbnlVqt1c7Nwa1iYZINCiMAXe0bqRGvK2JfK90-xLGpSv6qSq_kR-mQPCWNTvTe8Oj9Ps9tWLhk7lkg1D-FNPYq7EIBZO6l4_FTWoa5-PkcCZOTaHlBp8afFVouND65jLYUXvRdP6K9aappWC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJNqCJG6C5U0KxMB-S9is9MgDPfRmHJ5JSeJRGb1Pc-kazDCcNTneBy4Gqu09oTSSgkK28_cbDHANQE3rByIzADRJ7eoPoTQEDmpKOVvgFfSST2YwgSYYM_hchZjiLzE-kks244xWgX8M7vapqpYPhDXjdTxVrmiyRysHxn_8Z2ooLFBR-8BlwwQVAJhPxABeWKse2dlZ4JYmlKiS6CthO65tEcx-L-sR6rTCGKTn-54I0uqRBS8NmA1S11sTHeW430c02K_ta_9g4Fv4tO18LFvDgrOz3i6hmGS7Q-YenHFoxEF32LuBVVzR8ZRZkwg5BQxg6eNhD7JVHDYEtsykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uU99Skli0jVPOoK7YPrXOtmZBOzPJsp23gVXA5BK6O-RSs7Jkd7z36KZppTfJgfvpf6rHzWZIAZkMOtgvbFxiIGgAUrChdJVNVJrVrctTTu84sF6RqBMTF2nrmBaskYf5sX61xdudh9roqJy4FUty2JAdC8X0O4PrSNhN2r_nrsePAXcrVM2eCpCI0Uv-UIkoD5p99CEmD9jCnNDh1eQKjC5d8aNX4UHVZbugdUhGVEvTcZCSlJQzvQvisJBlXefwhYdcCr9EmQKSY_OqTsO1xoy-BPlD7yqUP9nFzGc_PcHy9HwSBzOfzA5oghl5z540v374Xp3kH_g3F9HK5KUoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp-timlgxGGPhGIP8I_P3Uq3WOmTHvwZz2uYYR47TP9koMh4B3m074Wajr5fvzRWN7zuuPidMEEIxG_wERUCN7NpckyNuuk6pX5fVSME0hpNe1Z1NNipCItQB5pRx9MviDuNO6YGh94eX1Vb2lbQq6Q8piANGf19FmFdlg3Fpr8J3EFic6KeI10awSMqQHQiEJrGSSjhQMgmoE42eppC3QLEMyrnBOgonxqGNS1eZXMdowmrtDx79aANF8xLN4ohTwqsDvd95jefhhU-hNCTLYEJc18Z0UtSbpISL1MawznZOE-rIjscyzF9cGQkcYlIB_3qa-1ooqKgg3sg19Oljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLmhstzzHO-DH5KfPFM9DgIYEmQiILJNLCcShjfHxRHVCTn1UGXVI9dQpKwtCI2BBOlsvfM3Hd3n4-pmmCsO6KLl4Iq56g5ddcahWPeJT4PvPhXWd63GFafP4EgdM2aMD85E4_6pL82SVBzd65b7m8b6f4-RmvPKGIRA1TCA7gbOGSLZ1G8PtO7H1nGgJwy4DlpGuUwLJ50E89W4n9LpxKhiCa-WDutcTI9j6SzerhjMKCwlQqe1GExZQ6BuKHaDfZ7N2Y65Z1Ff5g3YnUkNmzWFSZKocmXkFIw5CedQ6XXmMCVJ5WVDVXFsyfI3I-6dpTTW9Uvc1BdAEv8uHy29Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oF7HHz2ZgxmTwj4onzCmlEY4MaKRybK1K0IUEy1Rn__jIsFFhXV9WlcgmammCHk-mikbe8tVYbC7e7ICgCygIPgvIHzF4g_NVD6AAvhCrgbY9B8QB9lb_tS3C-7Rcvm6YjcKMjqNj-JXcn1SCd6JVQYa6AF2M_q8Ka1MKyoBtusTznHj3wDp0eyMoBgHqa77Pi7D13uDppJmhu00Igg2Z9cOj8QwmboLGDMiyYhIbw5lEy3vCjgvlHyMFInTD2nEa57AtkgxNPAanAntOZvSo62ezfew0RjAeVtAKwvVz39UEOxR5a3yKzoZKfCg_5u5d9r86aRINRosNWtqoCBl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fk-tzrbA5y2XBIoVhKBFECmDlpA9PzJRB9225z5m6r5Yr5pMCs21xHS3YKiKg0K_cI_yIBngkYKNuU6ssOqZc26PhuRKFyr_Fm9jJnSlBy85m3dqxGoafiXN6UOFc3t3g3yAMZs9scQ-Lur83AaHOJzw4GPvGmnIeVSkMzwgQV9eYV0AmKGb4Uacc4Gx0HPDJaXzf-m5Z7lKWOy8dEBbcjgFAIgVyP-njMxyejO25ZwDcyCnDzRSIs4pr1dr_vS1oV3V5LWjTRmB1WxWJjOnBQKQ53-2yQYjj4r-6mXWwiFZTPUSur0Nbe6leqbSbeZnoOaU29vL6KhJqz6HOEJN_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jt0z5r5eEhRnifH8to7DYAhEAU_wu_rI97mQa-uvpICckjrIsL193Vv6nJG43Af0zFhZmB0-Xn4ezK92ai8e8OV34kGy0ssHa-ivQj2piAMJusGaFAhcs_UDDVvC92ahBzbYyRjXh-lTzPNqK7VUDHp3oOqfu3BILwNLVURnzglLbDgy0NouG37etTrsAncs9qo0OkHm4FySRCs7OQtBTqoBNdvF5lhbD3nigeKRF25TgeVI9hiv364j6wzCDyBOHx6zCET3ZpE3Z5rfpb5qsya6F60vR3rHgzqMwzb7p7JYbMWR66oyEKaiLi0M61w30ESxOw0xlFQ_8JN7hNcwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ74ah9slNZ_f-Yf4lo-Qp48qeTylb1YfT66JTkdvpdkYR-QGDfqhiVYK-eFdKFr6h959Np9R8Q20hXXM6MYP8FR5byh5xoApzv0m-EWF2DDq4AzCkSVLG1rZ2WHDdBHVYGNC3tZQ72AqyVxI2DE26InPvIiI4yDAc4460GxX4XLcGfUOv837Wehrvy8668rJeoJ5lh7SQiG2dDMq1WxIbCGaWHubomRBWMCtocFoK4snq4LOFffUBHVgUSq41YoKwVx-Lt-i-mHRk9Ziugv4PokKdHvHshr3F9bcdeV9R8PeexXRAOuJpWJV0dP_jxzoXiZv5IL3zbuaDBwcF0JvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=mTUCH6jmrnyFnXdELZ-06NCRtieOqHr3S_oYR5FvQ5EjkMKHb8Na58f6ewvlLR60bksVE-jeN3_EERJoWJIYDL_NWFd7NUlp8sE2Mpm8jAE1eeWPrUgZL_nOxY-ut-vZTOXhPmaksHMJpXUBsMWQR-8Aj4OQBWgOrUfMXohl3zK2RMQqb60RElNio3nuY-anw6a35zc4QE2MYprokN4QwSr2tWrQvopZUEVUt5G366xTLOJ7gFO5NrfxwvDLF5zWApu_ChUiqWUHxaMoZZU0xIWrp48tUSBWqT-W0yhBLWKjUPtIzO2Sp-JBCLd6Ifh7yCcxgtARM5UGqRGOQnq5_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=mTUCH6jmrnyFnXdELZ-06NCRtieOqHr3S_oYR5FvQ5EjkMKHb8Na58f6ewvlLR60bksVE-jeN3_EERJoWJIYDL_NWFd7NUlp8sE2Mpm8jAE1eeWPrUgZL_nOxY-ut-vZTOXhPmaksHMJpXUBsMWQR-8Aj4OQBWgOrUfMXohl3zK2RMQqb60RElNio3nuY-anw6a35zc4QE2MYprokN4QwSr2tWrQvopZUEVUt5G366xTLOJ7gFO5NrfxwvDLF5zWApu_ChUiqWUHxaMoZZU0xIWrp48tUSBWqT-W0yhBLWKjUPtIzO2Sp-JBCLd6Ifh7yCcxgtARM5UGqRGOQnq5_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmCv7qhMIQ7GWzYz4onPAVstdEZR9tKTPEVsffosDUsnl3osAH-n13ZXLhS5PJZMYRiqKahNgWd1pWZCi6Kh_aAwZSu6CPEJfVmbRF78jM7ICUifq0Q4SarhTFVI44AGIgEp2fjX6EzRv01coOrDX54J7GakBc8ueplvv0NvLy0LbHH_ccPFHA_KDXLkG6eRsubnSsg0w90ZJi9WwidBmfPnxGyvEUTIRo0bMr-YhMC-2aS5vQZJj1MItt-hcwQFeejzrapdI-PzjU433k-rzINzaeI_vgBJE-5bUsGg-A-QwORibcon1320oNwVr7fy8344JXZ2jSu5tLBAXNP4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24422" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwlOFdVQrLhubmVwh3uLysIMHLvlGa2b3-J7V5xGnh9pIWXTQ3F86hL2EG0MHt4Plewfrybfa0-drhLJXdn52MU0wjoP8_1Esea_vmvY-RO9rd8M9L_6W3WbS5y5ZyOcOJyOiJUSGQXOct7gcyH4SvBh23dM3cb0ITjMSWpE3yrbDYwiqhYlCkTmEKaS63qaSihvrEWBOdVVABztjZb2BK0ai0i9cjd0ryY7Rfsid4RoV9smteL1qowSUxsPJZ-kEqJWRsYiWi4-gobj07xMce7KWCqeoUb6VfaWr2h6bY7Ge3c4JCdctwvOFhwUARhIbX-cqG-CyK3KZzW8bw40Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=RcaQ7UDspH2Gi_wsENL3Y3YBrePjQukwXgIo3dyq6DvR2SfUXdDRUPC43KbUkoQoD-HQZh8-D9jNxnamrwjK7RHvybh8kH5keo-u-jyZ-dSJv-6cZSYBk9e8i_LNqpZ_rl6FzXAkKTglrFNLglP62F-6eJSJPKzSfvthik8L4CfB6qg6lo9RvMBRAhLr1O92fHA4tXBNOy8fgt1QNtylb5BYFhtiTscbVnwMHa4lFU2nmUjaMB7X2OJKLSbd2XCB6XH30nQaYj00IIyEDLWp5hWapyQYIIk8DPbVZ4K5sThy_spTEWBLkZhlbIXShz5YNF5oblEs-0SqiFE6w6X6VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=RcaQ7UDspH2Gi_wsENL3Y3YBrePjQukwXgIo3dyq6DvR2SfUXdDRUPC43KbUkoQoD-HQZh8-D9jNxnamrwjK7RHvybh8kH5keo-u-jyZ-dSJv-6cZSYBk9e8i_LNqpZ_rl6FzXAkKTglrFNLglP62F-6eJSJPKzSfvthik8L4CfB6qg6lo9RvMBRAhLr1O92fHA4tXBNOy8fgt1QNtylb5BYFhtiTscbVnwMHa4lFU2nmUjaMB7X2OJKLSbd2XCB6XH30nQaYj00IIyEDLWp5hWapyQYIIk8DPbVZ4K5sThy_spTEWBLkZhlbIXShz5YNF5oblEs-0SqiFE6w6X6VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNqfisdSRRseU8LvbY1o_xhELvGrIge2646WQsEniPcZAkpafDFnOmX6dnXLbChHbq87EToZT7nCcEx9ty9JAwU0xwP5_lwKYmczEJOdx8vxcRfPITWXapTj5uliwaig0s5ZwWYH9he_gQ8H-n9fu_KfFQL6Zs0q3VaFeWYWwhdNYTTgwaHAQPZ-fFyNlcn2lzbnlNM9ncw8SEsj_LLkNqxBRatM_Au-BvbGp0yJ7eEQBkMHSgX957piTP9SKCHBR2S0CvJhVsJG5jvbQAJ22IZV1b70oRlARIw15msEdgtNe8v-yhLPxcEHtI2Xfu7zZ1Irg8BbsfL_ORaM_7aeFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0mA_aUKCzz_lTJ2Vyl3tSSnI6q71ai04sznnj2U2HRvPz4UkXd3sC2BTg8g-ckzJJ3a2oCFlO78pA-VGDE5MYgRwgmmRckwrtylOUAuYQtdHibKKVivog5Gz_q2tyP9pPI6bOtl2WlpYVRr_RoGghQYNMEUO2T9bIIadEZv5s6qHFIHSSpIf2rmjXQmPsJbJa6ux4tBcj5IPI7s_PZLjPmmUUxKbrlyzolxNUtX-VSOWgF3vvKTDe3CsVh9fJ3jY6JGbk0hjTAiXhBMHhnb_R72u2mkvSbiRz9OeX7gdV_BkAhX5hA9xM2ZcvUCiD_yteBX_W0l9y9sLkJPcVskaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yb-0k8-ckrZX0pszWPklWL74jpJPiyYrSuC2b35_Uji0Fv1Bob-ab0fUdAPjDwwtD6jdbmKgLel6Gxv2grDGYvTm7V-lGZ0uPBZUJhJwQYKdeZ7nsTBqTWNWmpPToZo3y3eEtxARgzXgS62_VsgonN4km50Tiw_o6ekAJJem--slb4IZCHMalT0rfJQ9JEFVGsXAizc64RdNkrfWiryIRU48jg4g8betWRUszjA0Bb2tiZDBk9Iq20Gr73QQ2zT7BUPx1nU7YroZvqX-ozc0RGU3HvP9zjyIztE-5XqeVl9PIhLyR4Z3y4TBQYc2ucDsThboyXOQyayrCU8z_4zHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd3s8bgVBqUBMexkrzsfa3OswySyGtkhhuF-hSyxGYkKNsMM6YmB2rBieM7CHhhLmkdRDaEezjJJLuHTebBXkHVnP-kYZk8p6QMdVdMwh_Yo2V0-3daMwrcDldEHwtRXIwaER8fh8OxoaLlklKvtiyMwWwRXF22Jh8eDRD-31uUxkis4FpAAnpjZVHQfGeIDrNgs5I7nM_RpRDF4wmedhBHPrFUSZiw0QFgUR31BVxk54Oa2txh6XmM9sLF9h4tibvOcgw82RnRmF-Ws6eGXlqad1APjiw2HdSgARQXZD-4yd-mkGpxDWWkDjnby4C0NI0wv1hv4BgcsY58DoFVFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJPKLMNOACmrhNLuSCkznZI6aeFB5lAlVeGHYolKDACEcObFhIFYHb9k4KIdtCSxqh2aFcyhLoMKdpZ1aGenpHjVOY4mnQIZjNUXEJrcLFNkOBs1qRefz2Lb5_UuIT7xmVw105wEON2Hw7wKSymS00Z-WxrZrQL4U7Dej4qTrb-i8IXO_EYJyn1uNbSu3nfBkp4icus3rGY5kwEWoVAP47M90zT5vcYdQMqKaZolEnDtw1BGty6doJVZ82Zw-gOcAhQGatknBzAzKu2TuAzAmvEaEFGgC-lH2T0JKVohNBMVFA8hrB5SNO9Wov14hJ0ldetTa2MHR78UmGfFfCUDnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAWsYO_O8z0S1MBRRDZx8WQF0aEeP6aI05AFNGmX4QYcf6ax3ZoaFYBggedmC7JfmC2swuwkhqZriHmiwmSdYPfXIQ4fLx-jHi47TLtlbVjYKFoRJhg_58v7C8el5reBjJPtHBemIrgRaVuceegAoMoflatkf_y5Fl2lEd6x9Po8l_jpiV25XJaxs-On1535jRLJFRHjd2CfNbc8VIyn1OpupEo5_a9_aVtQFpAcwOcbF_X8zG4iAG9NoH8qJdkHiUitmfMZolGFd1pQ5QcJS_BGLYFWIiDkzjZUOjRaCpvYl3UjquZz7jGLzN7k6lnI_YODCIj5_ctRdSYf_28EzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3C7PqPYvuvD_ojKFAf3XZH7JU1gT16Pgbb13IAUOseRXyNskGs_Xb7rtnHENWvzwVcTaJlf-pevqxo89vcmvpu_-4s5RCfsw7-qWZmd2Zg9fpHy0sNrjdxRfO8ZFKppT8qbjELwWOEqIVWcq5F9fn0fMD9YuBaxV1ne4DPNrthgjtpq2Si4sETky-7WYHlMIQH-ZwwvS8mO_5HPaRZc5luSR5NI9u3RkfGHfXwGmHk_DRz86n2kYc21UCCqWKOw6JPkwzifX4mtFS_EjT-C1elSXViLRRSZNyT3RORWHzwy0S4JmrdhnbJuzuqlp8VkRmSvky4qQI18Frs2uSlT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohrkyRHUnlJAFdgZ-vO9zMdKRnf4F1fKFZ0B2TYC0jhx8pM3hVEFusx0wHD6lRHC5L_LvzxnFBFC-8MFL1tu_sIsmUwowpiZLtfeLYPna6Rw7PlJXeZuztsC92uKGsXctGA8k2-rGvgn4G5eGxtGEj6zq3hcMtuhn4uDnkJELJir8U2Kco9_7LZEErIUUdH17sbdgcX6LccC0Cb44Yx738giMTPNidCGBhB0_hJOXB6znHWwtdkWZ6tjXDZLsYz9EvSPTz2co4eeNx4tfTVP18nTdgOhLJ3hyGiOGTsp97ONL3xigCmUngnKVBaQoALJS04t-cdtJBvy-85W1B7mSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGZXhsXyRRlFr42XBjgw-JgTSxonvmG-NoUja7So7ARLDaINj1yTIti9oErJzwtDXqMEUIFWswHN9gy-q52g8lx6kqXVCM8UcovcBgCL4SaPa2IXbX4tkzHP9REQe80jtPA3jMyqKaebyouc1zCluz4QRqFIZdkQrbQHLAFh0CcJkhFOzJpnmLFpQm9Q5BLgMt2lAi-rJXdH31YRCXrqp_wRBXhJb4yu99smNERzVIxGB6ZDYFTYn0WnFywFswLZuyPetEuhc_BU0QgneCKjk3uZONemNZdVRU562UMKBGQraIa0APwDTzx-rut7S5GniGU-1zT3iFisWHncLCJNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSOpSq5T95ieD8CO9AhasyLp2Kne8lR6klTfvI_qr_dYs3P463yfAvw-QMet2jzfmmOmBWiUeftbkBCeOUAateOnZ1Bq3FHDT9bt4IgmhDJCxK6WnWaU8mS62MPB2bhIMtxfGeVmkoofk1rgDU3HYhswbF9Yh0Jhr4LMg3Au50K7dsjsPw34ADKyOQwBN4NxPCLhtgsaiztdwn3U0dJmDtDh2xsm_ff5XeOkFvpqN-PFpqu7MCwhaJed_5NO0_K6qCaO22G3KvZ1FbvidxNfx05z8o0fJBlkvfbWNzcGOR50YswephjS67vf5YguAt2nXnswQkSq8WnsifM_lJ7OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niRjw43LM8_63-kXF9qXRi9m21XBB1HWeY8XvciIRvszZj3Z9R-GdHt84x41os79RIPKMD8EAeXjsUam7KlLrW7PhZOB5oi5omfcW17sxliXvkGbUbdQ-O2O5uMZKU92h-APm6t_32sh1SH0FZw4A2q1n1fKRiwLLvwvVIXZ039mvhl_fMjcKG6KeDP_F4O2EpJpCRdJ8t9b2Cx0TbEj32cSec1QpZKZx2L01Miozqd7_4jpgXmN2GhgkjEtESh8LeJ3oJUZArXqZe4IrqQL0Lk3EMdoZoQPBksy1qePsJ1sQ3-20wmHMfaTe6gc3tXSPL0RIq9IoujfF95yIjjmjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=VHs72gts27P3VnGsa1DZkybbM4vcfwp3DfV3eci4uDExlX0PNM0A6dwkesx9v9Z24_mL34QrPuxr3x8Y27tUjfo53wa2qfnLr9ZyNSYVWZLueNtb6zBzgljZB-Ed2cQxMd9KpTV5j61je181quuRYkqEjd4xG2SHfkIvAyhlZiS9oNIOlfac_v8hja2NF4W54EV4aL2PrQLgMOZezn27r34eLo9jl3Vtjqnd_nO25VniOHZ8PTf2y0Q3OA9mG2vlR8jgCF8VTugmvcz-f383zRCgV93FrHm5QMgnG-Yp_aKug1g_2k2vegToT7itV7ALqCEaotFq0J7Pi7jhbrmw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=VHs72gts27P3VnGsa1DZkybbM4vcfwp3DfV3eci4uDExlX0PNM0A6dwkesx9v9Z24_mL34QrPuxr3x8Y27tUjfo53wa2qfnLr9ZyNSYVWZLueNtb6zBzgljZB-Ed2cQxMd9KpTV5j61je181quuRYkqEjd4xG2SHfkIvAyhlZiS9oNIOlfac_v8hja2NF4W54EV4aL2PrQLgMOZezn27r34eLo9jl3Vtjqnd_nO25VniOHZ8PTf2y0Q3OA9mG2vlR8jgCF8VTugmvcz-f383zRCgV93FrHm5QMgnG-Yp_aKug1g_2k2vegToT7itV7ALqCEaotFq0J7Pi7jhbrmw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNfOtGCRGQK9yuQNFyRSt_aDFav_9K0nkANZYm0Az0nQ4HMahlgBgvxOwQWnEMH20vpyY7hUDppoeURE4WCBfVMi6QfxxXNwrcpuWoERXSHsaPZ-qQ0YEQFtIF1gSArCljYyDWYZ9bo9wrcEZj2XbStSugopUVd7dfduUhCyvbBd0zdpF-lVPldrStiJ0bhjEsBPQZ_cDTsKWD-yfFHS8zpY88YFeVpzSpXSFsI37yzvqQFqr1dUMMV0szPVtxmL9gs2_J4oo8QFSM-eqXSg1zOjhrq7V82MqHS3-dyfjyR0KfqV7YS-9VGpoAes3K2pZNMeFZhiyB2zIvMdgGk-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=LYFAhHI441rketRwNfWRWfOV6zh0XksJIWWCP8soDQazUszAb4QFRT2qv1b9PQDvXMvBl6w8PC4oJ6Xne2WBZFBXvDYFcMqfDCH6Gv56AWnf8LG9UYWKXSSvru6T64hUa4lWNy9EknVpqEPfUO9X93mjLeJl66Sn_EoLR-8reI0ioYdyJ9SSzVSpi2Y28IDtTWU-UGYC4cHmbbcYzElcZjaCcXy5jgkvFJ92ShSmznOJlmiTxUasnbat8E4vMn7fZK-drZ6FBQCD1mynlWxtIA528WA7QUAeV4vpW-YLuuzXEQFeLWpGYHTGuAOEibyrEbNYpml5g_ynbMxcQbZZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=LYFAhHI441rketRwNfWRWfOV6zh0XksJIWWCP8soDQazUszAb4QFRT2qv1b9PQDvXMvBl6w8PC4oJ6Xne2WBZFBXvDYFcMqfDCH6Gv56AWnf8LG9UYWKXSSvru6T64hUa4lWNy9EknVpqEPfUO9X93mjLeJl66Sn_EoLR-8reI0ioYdyJ9SSzVSpi2Y28IDtTWU-UGYC4cHmbbcYzElcZjaCcXy5jgkvFJ92ShSmznOJlmiTxUasnbat8E4vMn7fZK-drZ6FBQCD1mynlWxtIA528WA7QUAeV4vpW-YLuuzXEQFeLWpGYHTGuAOEibyrEbNYpml5g_ynbMxcQbZZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=nx3AOHqmHZyY-t1w-fUTh3no99ba9dtuV31uSC3j1fexgMIZivzMvUb-GY1OWuiQEQmtCVlCdTiRno-1L04YNn7NxyILkpcKlr7RSPXrxhZ22fy4D0JK-ea2RNt-f7rxahv6jjPmcgKIsabs9LzdKLjM6F9KZHT2VyrF6queBzILN6XwGFPpbSjxY86Z6THccdWmqZq5vMqm3UWm95WO-xXKIe7bOb20wD5M5FZJEaacfQE53CHkcsFjH4AeGb21xm-qWv-B4nLjjA3id5oD0JevjKi1FzpA24wlNSo53BpmnLNkAmRL8QYxbD6KpfcRK79LnIXh8vZeDE1BgcwCuTCtJvswNlJGp5DR8_2GOSNr9KDwaocgE4yOcELIBy01Fg8WNkXVuBQR9xnFXFjmEsTl1TtygU4yQWX4SoLNBvkoVOyopaGFYNRd2X7jUl79oysjjobq7ABJfwwdjd15ufgX9S_qhi_QoxKC4i-Up3eGWS8-JJzGLBtHmdgfamqQKa__HPWSo8iCO0xJKPmaKuSNMHPXjk8D23kh4LlZiRoxaVS9wBgSDiYqBq4TuDX2jmfko0nxU4im_CWavwtrhRw8GigdCC_xUco7xekZ7QKVgwlujgXlPsNwTtnvEf_2cFkFZ_jfGLEMPN87n93WffeuhWquy7OQUsxK4Kv16ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=nx3AOHqmHZyY-t1w-fUTh3no99ba9dtuV31uSC3j1fexgMIZivzMvUb-GY1OWuiQEQmtCVlCdTiRno-1L04YNn7NxyILkpcKlr7RSPXrxhZ22fy4D0JK-ea2RNt-f7rxahv6jjPmcgKIsabs9LzdKLjM6F9KZHT2VyrF6queBzILN6XwGFPpbSjxY86Z6THccdWmqZq5vMqm3UWm95WO-xXKIe7bOb20wD5M5FZJEaacfQE53CHkcsFjH4AeGb21xm-qWv-B4nLjjA3id5oD0JevjKi1FzpA24wlNSo53BpmnLNkAmRL8QYxbD6KpfcRK79LnIXh8vZeDE1BgcwCuTCtJvswNlJGp5DR8_2GOSNr9KDwaocgE4yOcELIBy01Fg8WNkXVuBQR9xnFXFjmEsTl1TtygU4yQWX4SoLNBvkoVOyopaGFYNRd2X7jUl79oysjjobq7ABJfwwdjd15ufgX9S_qhi_QoxKC4i-Up3eGWS8-JJzGLBtHmdgfamqQKa__HPWSo8iCO0xJKPmaKuSNMHPXjk8D23kh4LlZiRoxaVS9wBgSDiYqBq4TuDX2jmfko0nxU4im_CWavwtrhRw8GigdCC_xUco7xekZ7QKVgwlujgXlPsNwTtnvEf_2cFkFZ_jfGLEMPN87n93WffeuhWquy7OQUsxK4Kv16ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=nFt-e7NdOT_UgAMb6f61uPK2q0s_2fByqH2b71uG_RKM-9AMcfJ_nA5893paBnn_tbR9i2GdUXYWnZk1q9JMJdFHY6AuV8myS_s7aPjIvErf5F8QLgpxHlif4cZ0pK1mcEb2gh_6Oau2JGq3M0-dpLSOhhdGirEWApMSvrUqYZgkU9AW5TeNcf4FT0JnFFGipEZR-XNoDTzuejiv6v60U2nFNmyaIL6dGVDybqyRVOejEEU7ArLYkMbpmy4xIqTltKOqEUWn9fhQHSeOPxNK4pUDeDEvuvvepgd93iBpNBZbEZBp6R1leddd11nCbZNEv8SZthhqIU6hkr_srhffrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=nFt-e7NdOT_UgAMb6f61uPK2q0s_2fByqH2b71uG_RKM-9AMcfJ_nA5893paBnn_tbR9i2GdUXYWnZk1q9JMJdFHY6AuV8myS_s7aPjIvErf5F8QLgpxHlif4cZ0pK1mcEb2gh_6Oau2JGq3M0-dpLSOhhdGirEWApMSvrUqYZgkU9AW5TeNcf4FT0JnFFGipEZR-XNoDTzuejiv6v60U2nFNmyaIL6dGVDybqyRVOejEEU7ArLYkMbpmy4xIqTltKOqEUWn9fhQHSeOPxNK4pUDeDEvuvvepgd93iBpNBZbEZBp6R1leddd11nCbZNEv8SZthhqIU6hkr_srhffrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=CAc3kTbOLkwJqaTaPZ-7pCZ-9FNCN2Mw6UPxbBJGjkvr7NglVygfMniNZdnuKlsmKBpnps6HOOku7kSbS2x5gQPYpsBU4GT2mSelT2GlnpN9FevnAI5rJ4TrAaYObtCoxmT2YitYmEmv57MJM1daudyG5wPfa1B-0kGAc5SyaXKuXj_UZ-23os88bvPBHRkfq21TGi3AAnlj6F2Gr5S2tt2BP3kPiE-eu1DtgtiYkAzAGXLdEGuqw_20SIX1D485JQeAVDaq2LY_D5dgCXJ6KBlkIF6aWnkmIKiRXg7mgTw2-2xQCj2BRmOsfs8vBNuJ1nYq0tn4q9QfFoHWMx18TXKM85bYcPAHcS6-ao4DZoYGArewEWgtD6QYvEapfXXuw8_FWXS9jJgbPY5vRlTTYrwL1rKYieazTkA0CikDZ0E-J-m7c_NpY0y8MBufqE21GhFIs_-JC3yATmqurNA1uJoMFnhnBtwe_IggvYcDx609YbLuD6dGcfceltYr1-fou2TLlH0lcR99ORrBOwLRogSI5ACmi-7TlgaLj-qzV6YThCTmlRYFhQfJ7VPAXjDAZHnRJFWf9c1wRkdeBJxTxXPnf3Hn5CNNcLl4GYfuvPvAYmozDfH73cuN1cK9dlBSOajlnwzW3m1ktHoJxMRLP8mgYIWVWCFSD8aHE5W-Tqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=CAc3kTbOLkwJqaTaPZ-7pCZ-9FNCN2Mw6UPxbBJGjkvr7NglVygfMniNZdnuKlsmKBpnps6HOOku7kSbS2x5gQPYpsBU4GT2mSelT2GlnpN9FevnAI5rJ4TrAaYObtCoxmT2YitYmEmv57MJM1daudyG5wPfa1B-0kGAc5SyaXKuXj_UZ-23os88bvPBHRkfq21TGi3AAnlj6F2Gr5S2tt2BP3kPiE-eu1DtgtiYkAzAGXLdEGuqw_20SIX1D485JQeAVDaq2LY_D5dgCXJ6KBlkIF6aWnkmIKiRXg7mgTw2-2xQCj2BRmOsfs8vBNuJ1nYq0tn4q9QfFoHWMx18TXKM85bYcPAHcS6-ao4DZoYGArewEWgtD6QYvEapfXXuw8_FWXS9jJgbPY5vRlTTYrwL1rKYieazTkA0CikDZ0E-J-m7c_NpY0y8MBufqE21GhFIs_-JC3yATmqurNA1uJoMFnhnBtwe_IggvYcDx609YbLuD6dGcfceltYr1-fou2TLlH0lcR99ORrBOwLRogSI5ACmi-7TlgaLj-qzV6YThCTmlRYFhQfJ7VPAXjDAZHnRJFWf9c1wRkdeBJxTxXPnf3Hn5CNNcLl4GYfuvPvAYmozDfH73cuN1cK9dlBSOajlnwzW3m1ktHoJxMRLP8mgYIWVWCFSD8aHE5W-Tqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHaa9u5672bmbfEigFouUpXt9_2q0Bn29DbjCyzA9MNdEmkBNvEbRl-3FoXqiS8hMrY08ZzmoalDJPH5s0VLxyaZt_in8oqhpzN9zRAc-wBd9X9VfsZEjCztR6dxqpJE3X3VXE35tArayvNasVNjHx6vcD6p5BitYauNRYwshqp5Unad23K-zfOGNT-1HB0GVGB_IxM0TPNDguAuBJ0qxBOH42aCqA1cwvImMAlCTwBSv4PibbfGZGEd7Pgx1Pa-WddERBgmN-WyfeO5HYhUbXVk9w98l6Y3c2TwyUI0ov4ZCZcF8C6GBgvwXNDvzuJc3i6sJZKwZvzm277Od_crQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=F8jGMvYk2WEzSKhGfCT1JLC00mfQN8xy12GtkAcTY7h2pHlejQT9MIHhruH8oKDwcpSmC38OB9P7KzCWTtzAPPiSf-A87grFKzLBWQCiM7EEV5RlZbCgZRjyt8RP3vHVY8xSMMSSX68263XPyiorRSJjFwbxHBOCOZNbiPbJRzXRHbuwqNQhvRw-ZTwJdp7JHDj80ZPF2-Kw4kjL1gfR9gE97_VCSPqkN8LYZJoekFVFJIkH1_n7LtBNOr5U9YERoSMKWR6rmRQgFRGc3Zd32f5Miaoc4F4w2Mbb0U_vH70c2uQDfWmbeNNomvmgmUPcAP-1EsqIdEJOnkHWvY5_inJUnzrluJ_-I9Cw6JLAcbdNWKe7Zu5XrQUXsra6JfkAG5VnVewi4MpVqSfsVt4P3zjf81T-zI3jMJnsiyvs4R1swQI7EYCj0gR6qAIph0eIW3VDT6v1vz4ibe6BJ7ATF72teOgbzEUwKyRpDiJ4SbqbO7WSYgYnzPK9M25o3ECnLR7qTQZx8sWkHxkYLhxWZwnvucZ2HEScsHHFuR2MgEc2dyU6oBpM_hi5hlojeDIapkQWk_SzPOxV-QnS0TmcGtZJE-j5Hrv3COpbqmllZ-sMaWeEp_qcqDKWBuf9A8KJU2OpBK5y6yKRSFJQ4sGYo3GyEgJOUYZDBu7F49_07Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=F8jGMvYk2WEzSKhGfCT1JLC00mfQN8xy12GtkAcTY7h2pHlejQT9MIHhruH8oKDwcpSmC38OB9P7KzCWTtzAPPiSf-A87grFKzLBWQCiM7EEV5RlZbCgZRjyt8RP3vHVY8xSMMSSX68263XPyiorRSJjFwbxHBOCOZNbiPbJRzXRHbuwqNQhvRw-ZTwJdp7JHDj80ZPF2-Kw4kjL1gfR9gE97_VCSPqkN8LYZJoekFVFJIkH1_n7LtBNOr5U9YERoSMKWR6rmRQgFRGc3Zd32f5Miaoc4F4w2Mbb0U_vH70c2uQDfWmbeNNomvmgmUPcAP-1EsqIdEJOnkHWvY5_inJUnzrluJ_-I9Cw6JLAcbdNWKe7Zu5XrQUXsra6JfkAG5VnVewi4MpVqSfsVt4P3zjf81T-zI3jMJnsiyvs4R1swQI7EYCj0gR6qAIph0eIW3VDT6v1vz4ibe6BJ7ATF72teOgbzEUwKyRpDiJ4SbqbO7WSYgYnzPK9M25o3ECnLR7qTQZx8sWkHxkYLhxWZwnvucZ2HEScsHHFuR2MgEc2dyU6oBpM_hi5hlojeDIapkQWk_SzPOxV-QnS0TmcGtZJE-j5Hrv3COpbqmllZ-sMaWeEp_qcqDKWBuf9A8KJU2OpBK5y6yKRSFJQ4sGYo3GyEgJOUYZDBu7F49_07Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSp2oKY3V9R4bRGdSVJWzcN7GDkbIm6lgJxk8Ag6eINK0uY5F4ezzkP1WC3vEgj_QLkc2E-KAD9qqAdKShKJD2Th8K4kAi3kh1vyO9hq1KuecYWfuI7KAiA24akgCJEWHchALIkdfn7X1cGVfaxUOR-1kwqgDiqDnR4U4H5m1qAZI08HcySDfcmAYfA1wHAinM9eoill2S0DNo3HoWtpm0EaQxGhFbKNiYfB4kHjq5WLqqljpVFGdHH48tBrCJpxf5SUBap1mDsoEmsE_qI_a61AtBF4M52NeVSpKQNhf_yCHtjS6DKtcpjt1KkOsmPbfLl-BC2vsLUoH2gsUi_rSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTsLqnDRocp3ueP_J2G6Ou_QQGOCJEG22dwgarxRTn3ecE3VQuwWsqG-hsiii3IIXbojjgYdurCRkQHlfoFq_lZTeJYVsMbVPXnPL5TGjfE5W4fwF8Uq8zAIuaJbSUZNXdqGFb8dSeE5zshjKXxUvJXa87UFvZbtlacGG0n5qgSnZr-lC8NSaF5qwV1eL3nvwlDBtA02wo2WO-GNACVnB2Rcc_SNFlxUKmLs_VRR_mRJYWeJRaamEHXz3n8eGWI240PdL5q9h7_GKtvxU6RK0RGqbWSCUaOrgj0-TjaTHbCk07dKKmGKwtqAdKBqcbSiSRkOq1E54F1D-AIbd29Qqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/padNXgchBrz_NkCiiEz3OKD2KnYDfn2AC0_jszpRNJWP24_GUi08m2HX99tKR8ADEWUbFWPHAKSrsV_M1IXN74jdY49tihh6Hf0oXkdD3EXM-uFjvV-SZUVDCI_RlvRkw3WqOaibBvQ2u-CwwMI0gwH6ctmBAv_9WQu4Wu0mxsyyPuuxcghaXVqmJAYEdlBmcT90GkAM4jsQPcgtzA1EOLae4S5x7VwymhcP3kruvsq5tquwsb5DsnCr9z-B5Rzr_BlOcd87DMYvjIoBAGAJlOKOdd7LOW3i-_YJGpP_AEOz5IvvTC01iYLo_YakVvci6y7vaJLOZYC9f4-cVBLdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6u6U-6SrqmcFCgjWby_y3IhVeVJTfJ0PFbUn2AytS5aE3JTEVdaFEDOvSN-GzsK8XDoZf0Cy34XaSWqS5JiClcrl3HEnOc-5ppyIFTyDYlCPtJzG4jNfkJhB_1w5ybIy4QCcy6rZ9nrkyRRezQDdnmNwj0ioBuaPlkeY1uFQUXqxWqtYUxWEJysIzciy8BMoUONT5L2RawwbDFdGcHqK5aV7NNntq3MFh2UN5NxPUcqV1WJ0wueuDFIBhhAa649m7Gu82ZN54NJak2GVZk07i8gviWmtABOt9kyL4WOVY7PDjLnNwnZXAtN2y6jjnvpy1MIHvYhfsjHcvOVVIWGzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grJ1Dxz85JUEj9X_FXBhkaWUW40oNG5byOkyTTAP8VkVQWVDo0GHCwWBQ7PJsmGeH4kmMDkwvdcMksjrAEdeUNcIxR0FDOnJ46yiA1YYR7chPmmKCgxEGp4Nr-JZ8kIza3X5fUP5b77HheS3iCC3B_0uvNkh2MKjRLGF1jzgeE0AeMzBy-knIf8LMhzCXRETN17eUvrb-Eulx0RloAUx8KPYSnL4F0_YN4NnF-kdkLvBI6O6Uv_eK8qb7t9yBhOS6PP9bRzCgr2siSdoGIPzwvjoAEqq_DHCTgPq_Q_6UY16ig_w1IOx9W7RecxO7fZGBHD5uaeNLLf-z8r-awWNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkhj1u3x2Fw51yxeeEYF7NOZEnoMpPnUZNyisCrsgLvIiuxx4shJsq75hYSuHkksx2vYbdmW-HyyFnpL0A5JeJdHBEHAjwLtAZBO0Wml97w1lQpKwbPmZe93-BRDcplgLv0ej6nq0bb-wFZghZUmyzndvT9-fGjjbz2uBo8EIs2p1MokwiY5DUqFMPy-HKxflOeajgK-RMqTQia7E1iMJlAwF4PQ_kIoMQ4mu71YASV0a_kHyvz3jYBhI_47GmJxmmUqLCtggAGIhI5wxNx_Vk3h590z3Mp5zmVp5P5hQXq8cCb9wb5D_3URWbt2apV8TcVDiP9_I_MA8rkHmXp8jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGRkRZx2uIAMSSG_bPMAVHnj1um-FC-KEDUtLeRqTuEHzQ9VUEN_ZJAJ9sGjCiXLhQPNn4wIvrMReO-qY0ZoCH1sxhLFzhJMs8-fGCcmgeonEGmbd5x67M35M9EcqE-zTiQj1FcuVaU357yQQs5Mblg6LGALBuFX73P6hCCO0el5tj0k1NPxLx5zZQ90wq7wgOK3GYoRdQSaiMCkD29yyBey2zGI18g8aY6STQkU0WNZs8rn6gFHH0oL_h5suRqYsDlyi3CSbtKBNnf5WFHV_alvpT1Mnf4VLnj1eLqDbSA4_STOzJHUxn72wXJXWOQ9InxOrNY6g5YneQcpKvzEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf8jVH2rrJa5ix_T8UoIQkeRKA0_SW0DnsA3Yk5Z6RWjKB2YBmEl0wyPsPuBBAtgQUYrXiyi-xc4z-NcX69Ly_nEiks3wX1URaHltk_6p3Qkx9gMD6DqJK9LzN6mEcm83HmUX79QC6nrEtUteKajH7VJoS0lLf2NhMNOIiXp_l2EfDtUaeyvC3iXzSs4xsITE2NaoN8g75xuiyT2mfhDKdRiZQ8C0NOSsnNCNyTjiTdL8cCUXcrtR0Wmr0VmxBVB8ceyurPCQF7uO1nuNNiRAHBXW4_7rS9OPvCMLMb21JPR0feHIdE21YikXSqWeUXhFTAVXBIprUaIxXdTK-z6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rln4u9SfO7svXAA8gRq3Q7WxuG4GnkA0fAVTN43J6WhPyj7AGYLG5cbYOvdL3q0X82EgZShPW3Wj9yALvaiqTxUhL314k2Cbz4tLDVHfvUOyRYET5BFOA_8csCGktep9hnB3uwLV8sj-T8MzeFkMr5bIV7zWd0mO6T02sCj7y5zSWSJdSa28Gw5yzE1Saj56-ueC_PKRl7Y3mj56AijjBNI42efONfbVCYHmlSXm5VtzpY7cFLcL5W3U7XRpA9cjDiJOEa3M8qEzFImfAUxLYv8pJey8ogof8_UnoK4HQnJFmr_mYWFBNynGYl2qt2A4pgYtOFvrgEAP-Xqs3yuaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwbD0tE-_yhkZkwtjM32l9wwV81tGKMbl47GPiIIhtGXqV23qxopcY60XJILpJOjoPyJ87hKdd5aY8MzAlZ6lJZLbWHVdmoTfzyWjaSAVgzs5a2ErBUJ4Pv2f925jg7Qz3ccjy5FPmG9WHrwb89uteFel9dwbjnmD-uh1hcz5jHNz3wyltSGggasvFwNk4RNHefXsglPy1VWWxCGbczHiokmTH4Qm5ykDKDgMyRxve-Z_ZYOn0_dBNsKeDf9qfIcTZ6gbxNCrbk67sfnwTA2vBBw4x2h9Nq7y8YO6AU4-rXG78rQ7rCCf_w7NHIRSWHwrlIkCQEKAEoK9Vr8FUtI3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFnzli4K8qxWKdKsoxSs1QbwKtbMUDVpuGp8T9hXuk_Tnlp--fX7il9c8Q3RyPnTIAlI-HHRL1g6IiyaN9W4NHrTvbd2jZR2kog5ykywF3KgH08b-v43SL8u_ulZl4FUKl1cPIaXtfAJAxN7aavlLTnLj4xNF6ukj_EwAjdzuabGeqYmfrTJa9IYZiedBwdFtG7IpGAMnuK6DMjd5rCHb-E1lvrLstbh1031KpRshyuPm-ya10brFNsX52d2RjjwK-IbFFaSE1hMEXdTrc5N2SXorPR-X6i-ww1IfE6znwarEGctDx-sWGPDw6tSACo4icQ8nCRptS4fiehytino7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJfNtmX1U81qaOvog54-nnxt77zV-rm8cijLy9UUnuXfKeF_ui5tZo7am7nMqzDgUaBQj0y8k3wOnprcMefp4ghKqiBAkmgigArczHoXpUf7xSxR-83qg4jpCW0YCmk6JLqN7rjl8ZZqjgpCepEfZT7mTJh-4SFjbOQ7FUCYKqA0sUrzSsjzCq2jEBB6kJsuugahdtfXg6YJGA0W1QBmx3dMGzLEnbbsmR2t1jZFbAx9nH77tQYUSLmMV2Q8PN6lrmEJ3AiJB9-C0h0z_7Yrd2qyIllzlpmO0Mtl3AFzGiKiOz4TS6D9G4w5jMMCJljQJja03Td92YFrgZ4LAqQnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOft1HjPVjC1MkSp8jK4cbv4qVWYp4e2GF2SXUrQp25u5vebq_9rW-G1og1blLGrjzgJHPUx5Sd0UASUqRkftKsdKsthsPrGsXTYNdcgbm4QtQ02r3HtnXo8drWIMeTPYWSQ1sWXgqirJNGm9yVLNzFjDQCvfTM_9WglLEUsNii8XGASxYRluB-tNHlPOwuvLhBuUpnj_pgshUj8d2wEvJkffjpcFZXyEaFyaqpN9pprwbZMVXkgOD21qOhumi3QU-kq8xniEk0WmSanLjVhXk9IgQUSSNo4WbAWOtXR-RsRKY3Ao8wqKGSPMtO9PhV6n0_vtaWL_rAl0fHAH_uNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQotHNuCnWH4qirgl41WEZ0KTOcKzlEI1yMR8r2UbcNv5sXjmGIQMX4mj_0lIPpZlJobaA1pdU9yvGrpP88Hv2Mp8Uw0aTIgJZiiV1TlNfOthGMgFpCxZaoFkZsVO7BLh3tFVuJLo3EagjIdeqjbgEjviKDg_VLBs1IOE65m6MaCPY97RahWRNVSskpkm1WnxDGKpZigoLUuJyA5XszWzQIqTE7wyGvfJ3BczhAYVB4d2-ijL32s_aGiGnaPcp7gu06U9f78s7vdZetsIIvdLWDHmMg0uYgzTjBqsMxGq772gsSO_IOXSu7X2Mj9lN0RU3eVcACs2lG7S__EadCo6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL6KFZnrk4fIkq8eBzP53e38k4ezBshqhtxcqkQ-dQ-cbYF2DsLZxIUqDucWRyW-d9fxQ18D1Y7IV-IIuFcwFFaFM4l3jNeHlkqveVzNIT6OevON-FJYIaW11G3f3dWVyFe67U8MmgaiecyVcfZW6K72gM81zqYSfUQxEMpo0yRmRH6akA2J0naKrv-_Fp-aeIPFBCcAQvl0fvW1AlNfTXr9oaHrgO5u0InfLPdpH9WSleNOoCtJkLOoU4OM7qO3dCVu7jGkO77Mln1jsKL_l-UqCBhXx7LyZezISxPyqLwVnv9xdoDE8AHWRZf2NWEDuYSG00x-CeOg3urvL5brgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-A3DX2j3-YQJnGo-AtQPmf0tCGGuqiEx1tKGeVnOblky82cXBfyuZYckp3jjGPwpx49ZlvKAUJX3FQhz7DVr0w_30iHhkCk__dLkQZoqq6hgMzkmyu8qk6Vn52oTXe06_8i6yL9dctSH456m1zfhWJIbS2SRRUQAqn0UAuQd552BhGFKNWIhTzY5l4iEcOr951C01dswTk2v6yjG66zwez0rlRLhJpFP8ZZXzOFfGBEHXXUPNU6fBEKkjtAsN9jSFxDnWwwo6f_T7lpNkSnL0HIRBsYkTSkJXXLj8P9vIlWMEyHxV92uIU64trS37DrqjBgrzSvuKdrm6Vej78CEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=mzZHuvjCmwpMifedKGLBQoF1nHXu4ttgogPUYBulzxzuY8ILcPkGwsjdIIpKfdmM42ci6VDlqr2fij8Dzu0vdRsyKM9icSW_i-2c2nd0ulqynzfDvakXRoFNDj6F6IZPCAsXgZ0p8PXaoRweNan7xbI9Y5JpqxJIQHKzMqKyrrOE47fFpmOv4Pju7FXD_ekCw7UZzHiI56hffJuwh0V247jBwFIzh3laMiyHcEoPRst4Rd_Lxa0XCMpnUwXNjVIrGkX458gcjmYPlokBDzR8cXExZIGViG9xK1JKmLEf74K5J44VhqhYIH7Dl-k8HRwAQrKslUtL1X-BQIFRJien1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=mzZHuvjCmwpMifedKGLBQoF1nHXu4ttgogPUYBulzxzuY8ILcPkGwsjdIIpKfdmM42ci6VDlqr2fij8Dzu0vdRsyKM9icSW_i-2c2nd0ulqynzfDvakXRoFNDj6F6IZPCAsXgZ0p8PXaoRweNan7xbI9Y5JpqxJIQHKzMqKyrrOE47fFpmOv4Pju7FXD_ekCw7UZzHiI56hffJuwh0V247jBwFIzh3laMiyHcEoPRst4Rd_Lxa0XCMpnUwXNjVIrGkX458gcjmYPlokBDzR8cXExZIGViG9xK1JKmLEf74K5J44VhqhYIH7Dl-k8HRwAQrKslUtL1X-BQIFRJien1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSNqVudpUtR8W9GGcCnD4SGPhOmk6J9vGPUqZHFNQL3MvEvO9937bPLAmmFfL4v2YyfBuwijNCWxzFoTISxNCMTSXx2w-rPBEzVcGkdBz8L2E5xMM8J9aNtjY9Yioask4DVt5ih1E5lhUclDqPr-_ZlfEatdJwJLGuS0vHuvDIi0cYuZIzdJ0PdSImHdV17ZNdZsmM65nT_RwJWIcifIjrWGYy1kcw5RBdtYxdcfHemgb_LaFP-HWqUJhkoWI-VKDNO6Fb8jb9CqOCZ2gwMYgtCXl72xfaBqAbIABAqBeZeyvEAEa93788xVWY2cMU9vsI_p51pxkJmQt5q3TsBsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMOtLqIS5Ee1IFkOms90AuRvVRL6_tgCLR3zghkYr2w88B7kjAunR-Z1bjVg8G-gMEywsyLnipfDP4d5EnQ6SEag5ivvMfKTsGLTs9Qnq1GaHqUHAYp1GscHgtJDFSpJtjxN45Ncf9sglx_7DqXWScCUHPIEDDSzoZRB1plAM6czz8O53_MduWzvbLOPIoIS0KH6RipGJjNZcuqbtrKXK-7nX1HcBwTky16hQZzJror1sbTAbMi0uFiZF_RGpbt4M6qG-Q_Jgdp4zVwpSEsGGipJ7IUc0fiUO62Mi0gDlH4mXi7Jx04gT139q3SzQE59l7nY6pWptJfl33ggd91OqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0G2uqT0gK8f0R-Ldes28euErB_8iJgxCkAYJEHJt84ZM2nHQCY-uvMlJ0H_ZFye36bwOzGS5Wf01erF45miPAeZA50QWTuR7bu1NqfEnXVxaESAVATQjKpNXwqrOpSwcPaPON7Z2L75o0qnnqu6o1J9kY1toB1Rf9-31eX7ZOQnF18tdr3rZAnrvp6gKhnCVCVSqm24Kql0RSBcHd8L8zGW0O465WxgCU-ZADnos_OW5dqbmQswN2aR3R6BIoj11FZhaFp6IhUP997sg5F3WMy4c-pBU0K4RZj4rLOvifc09kojiSPYofhz3EGVQx5a-kE7PI8AHlxg6zk14GTDDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCYeONczn3x5vASaoW7PakibBu6JLRTK7x8V4Wdzby4LXPNsm9R1YeozoDPV4Rvx2DdRAUA2PpTpS33rrvPP2zzfFHMqHB9uQSG2jjqy4cx1LGpjESAQnGEuAp4HdWCYpRrDMdIJv2xjPaZJsA4zHO40DYsqQuAtgPfo23pzrCv_LDf4k2DMqoFPUDjseCl_MI0VlirjIZHxwGkHAGDixLLZ2aTghYqkcrDzWni05g-c35wJtmtNleGe06QL8iiHjPCu_iz-jv__aPnQ6teKG-cmkYckYeV6LOGbnPsq-wqoR05kQpefShDU22ObM7RQVJjG98EvyHJGcBIm3Xyl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=payFO1p-CtTuW0nxKsOZ9bpAhpj_smZn1jWdP4BecrnjYMfFKGIgqLgFP2450uGTngjzfVHIfhC46G_INQjEK3ILUkA9QU-sIKyy5ywAB0HdQ3gfV5sL5pneDJ56l81AKY8v35ox1u2PrwozoVdwny202Z0F4YsH8ZgdtnMJV4Iuz4hhGCHFBklogtqzgdHinxbxfghLIVILUv75Mlg-14maeWKGizyEGkQ9pC1HGJaHTJejVqVmqdxNyu0BiU-9mWbitELA8vr7ZLWcAnoZrbqB34WlfXiG7KcHav0FWbGqPMTUPQtp6cwltfzqGj9k31boaSGoqDQTK3XRmaQlmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=payFO1p-CtTuW0nxKsOZ9bpAhpj_smZn1jWdP4BecrnjYMfFKGIgqLgFP2450uGTngjzfVHIfhC46G_INQjEK3ILUkA9QU-sIKyy5ywAB0HdQ3gfV5sL5pneDJ56l81AKY8v35ox1u2PrwozoVdwny202Z0F4YsH8ZgdtnMJV4Iuz4hhGCHFBklogtqzgdHinxbxfghLIVILUv75Mlg-14maeWKGizyEGkQ9pC1HGJaHTJejVqVmqdxNyu0BiU-9mWbitELA8vr7ZLWcAnoZrbqB34WlfXiG7KcHav0FWbGqPMTUPQtp6cwltfzqGj9k31boaSGoqDQTK3XRmaQlmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
