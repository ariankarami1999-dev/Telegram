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
<img src="https://cdn4.telesco.pe/file/V2VEBOYmAQ_uahw2NGUfcn2pZG1_y4Axe8PquWEChYFVJCI160dbLBZNujF4GGUGWj1UrwElqOubUygrg0O0KtMcRQk_bmCthTAuZR6pdY4ivLVJk8uX0LiIf0j0jrR9zcB909O3y35zLN548jcKsaqDJmiFuZlb_MtgkoFuU32BhTVw3s_XoRVFrb0nor81IQwKXu1msiqFJBnd1l1t9D_a1uhE_yFz72KYdPpUBZ7Gd6G98qQOkIN__0AjbxC2yQI4UqjkDAdI8W6gbf-zdskWEqUft7SUTuTmXCH0Ih0PSbJ9lFi9OAUyPzP_ro2VJfNdJUf2ydTBe7sJS77Fug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 491K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 23:40:59</div>
<hr>

<div class="tg-post" id="msg-31286">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcV6RQONWAXjhr-adHgYyuQ7xKBPOtzXOOJZOaBOgGKPqpoRLCJHfzwqI3zbw2q3VI0l3pbg45vBSTFhIi6C_6oXIlaK4GWCcd7CWB5RUqzKHHcv-apOpAbAEECbsVqLVKNblM3qzGw2a2rI0z5ZKxZ9pikN5i875RiA6aJJLz5gmdjeDKIrGOxzzsJthTSIlVnmz_2RhzEIT_q_4ChdRUPeCBlHe6QBNdZ0gJBKSdkW-4T6dEnUJOktnxtzR_0PUeP8UQLQ2_CSHUX07-oMauZZ6iZFU-aVNmRsLd3Vq9Q4f8kK5Vs0JYsx25ryNxt9K3phORS4tRXUrGu6qA5nDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ علی رضا بیرانوند از هتل و اردوی باشگاه تراکتور تبریز اخراج شد و با صلاح دید جواد نکونام برای همیشه از این تیم کنار گذاشته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/persiana_Soccer/31286" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31285">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUIk85HOso4TwVVDlkBKfbVf_VcU-3ZodZvIBNAEGG0ndPuk9xEaCLNK8iuiu6sMRJ6UCBsrccrCy1JHv-yLkhtVooX4zi44YinUwUnAYlb62Zrk_kPdw3UqiYyjeuXiFa2T_x8G-LdekAeV2eHY8cC_nK6KzsOhpxtPyFzT-o7i_skfvOirk20eZqpaxoPp6tJuLWqX7itjclEWVNKLwFmC1EWNu6-e7nOFduAstURO7Dbc8TTpj4hFHd8I3uPnf53oeXDuSDLxNyyCfk2MDCURgK9q2jdcBOJ1K88X6MG-YtvLzVdtWEsTqI4ASyB6NIWrioC_sePr_kKsNFanOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جوانگرایی‌بسبک‌تارتار؛ حضور پویا اسمی بازیکن 16 ساله به جای ابرقویی نژاد در ترکیب پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/31285" target="_blank">📅 23:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31284">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVp-SB2-5nMhaXxVshYnKWVTjp-RrqjTJBaX0e_T2DoK41dO3sb701SFKPLE1U7L69gmBet3ovwGOK5tH7dsrQhvZ2j0ZsRog6yy4LKc0IdJlw2GZFEPEX58xF806iDJCofXtxfSl5cjeBBq8xWf__Ubq--TGA6Fhn0L0cqO6D0bU1-j4vVtFKmZakx6Q3LqT9JKZZ0qjBrCQKvEhiY8h6kf3lCzYJAoEG76PU5g7opj0visjL4IHanCqnGIALuDTHTa-js9G1ZK9xkepGfBFWHZcFVyuUwbuyEeS_Jk_ZCWtLYGXNPruuQo-abZJE93BCL-gd2-z50DM_aXV6JiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/31284" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iC9NPx70psNW5at3fXFr2f3zYFZydAxdXXSmoqMfA4fJ4dF2waDiNLI5TsiRDozA3EDPFyCKwzDk2Z1mA6L3kvx7Nksd8u57w1-ZR7yRpp-0T55AnUTaH2m7Z5jpH5iVrswfUpX77g5xtlKTv9PG_v2NimCQxSpByiGVx8Bf7X9tT5ANGTlSlWlLGlJNlTMeB4GehTbKYJ6-0ustdPbs7ktjpvPgr2O6-s0aPc48Y10pqcK7r-EiPBNn6iApFicd7IjyOkJKchoBAmrk2Rc7CuSJ_wfupTl4hIFHfD8-vnGmzKqR0f1aDoxqS1VXaHgXfCuZB37XyENoYMSVMU5DXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h78pdM4vmhxYIHKTIkNMI6wLGXL8BZtGZ4GQ3IeB74SsJkmTLgo7VPx1sSbiXe7WkiXfSZo_QSGj7DsDbPirTpGxCymvPQPW-c71kDJjBLSS-3OFjkVlNtJyIM8BzrKnoOrm8J22GgteFQ4BuKYjaCL3M9TuLzvC6NEcxzqkghf_CS5_lv7URp643wY112mJUxg7GPkWKmFc3Sj_DkUK89V6b90pHs8WcQUfwR76HCr6ZamR24USx8KKt0bYzDXih8woIG_yVCL-XBgcAzm62m8lPXlVVKDcyyXvBQvEOe88TcqFS7e5e0ol8ZZKEqrI9VM0obBx4SRqEP9AWjSOxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/31282" target="_blank">📅 22:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXBtMME98o-k-ACQWdCkjYy9OaznBDOokVEic2HEudi1p1-dDnG85WwswB-gU1pCD1OAlA4erSY2c3YGP6z8LMmK0_54t8uMaARgeezidEa5Y4bZ8sDVqhJe1OLAtkehgfd65Yh4UgOzqCmTM2iy6gG_xhtxOqjCLUgkvZWolcjKVrgYfPG7lX7m9dv_S2hGFXb183WBmiMrLqmQo-jhnukQ9L5dafSQY-e6Dkx02kt6OxiCUM5_lcE3FXV29fJ9gKXhqOkRCXhrw0mBYeVjr7dUDjJdY1G6OaK4ROA3B7CPvU1BptKRZ5pDNGysAf1TH09tLyR4MvOtP2T98uNnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/31281" target="_blank">📅 22:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tslluv4lP8aIuLtPYgeHmKbt7lQ_qlg0fd9eUcWxEJ1-libdbWMNBSjqln5zvGNP_nTnpg1LmlAoO5Mi5-w1R_FdliQKZdrKNVgkwI0HcsJKnrxj8kKAXwhdBIagz5dlxz8MP_FjroPGYPAtZ5Fzpef3Ye_88677RrEUWK0TooqroDnV7moi4LGyp9pNuPYFAZ8CLzAXfzYRt9r6jFvjqjhUU8hBNHPVPJcUYiQhwRqb7IT0k1uerVF7qN1ie00bTXiKB_GzPn5GmILQU4gKvvOLj7qvihmzR392Kh8a5HFAMRaZOEDeh0lKuQNJq0ARss40JHSlq34lUz0mvLz_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/31280" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/31279" target="_blank">📅 22:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/31278" target="_blank">📅 21:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTkSXKE7foBojBjcDCgp1A7NgWz3HbefRw_ea_Y71RgqvhS4cEgEgfgZTvO7HAWfectKQUjfdZ7DKW4XKeNsXhPiMZ2EoJvoYApqXYNb-2VJet4TdzbCnbYbPCgRYvEfuCX0osOwC386AUJA4OF0LD8rEqqA3326uQepbPnvBm-4di6Xjkkl2u7AOoPXsbWlbMqB0UAkKNiVVtbOHQ0xUpiC2WNuKiqnGWZPc4bHPfEB9xImvuoTlMO2CMC9NJ7WDT2Y08LeHeX80Jg9F5d_Mblg23VGVdaKaXrGgA5r0a0v6oBwbPbGEQUzgxphOL4xo_l50P1qDuGg2DuZ-CmsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/31277" target="_blank">📅 21:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3uPK9HFC8HXNP2zAEFvfMaPmsd-1BsfdCXbNxB_GwFmBVgSyoSun47ezCEo5v-XlkimQq-wlMEGWUrK2uB8BkdCHcGet9L9cdxqzjNmIwCIE4wmLS38eSRcbuRmgwHwwNoirVAVvc6QASms2sBxHSKOsvbjhwQm0_jaXjlCOaIHFKtV6izGhmO2TOse62lLzhGls0apc38_5caP99vMzRsGarErelDJycatRqfnnowAm8UgrxJ_KSTAi4vvuAI8i6_I22e667Z8Kwpw94lQw0W2z9Oj-90XsA8RNzhawjE1Y_4qdSXXkGrEYRckVCPQRRA3qU1pmHGqU-WWcJwmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وزیر آموزش و پروش؛ به احتمال زیاد مدارس بزودی و در روزهای آتی تعطیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/31276" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMuK_XeMrlH2COh_yxo2GFtFcwGWmB89UyhWur6JLgL7C4HRkB7i8OMmpEFpuyhfR8aOyXAxHbcvqtjFvN_rcuP14yjgytuJYxUK_e-1VDpMXkT2_XY3nK0no_murBIPc4hOo02_ep4EL8kvk9RWBZhVzAcsE_AfYKPRuN6o1RUV9cWlPWynrP5IOG4U1P4pFFAXQkq2CRi7UZwd1pMHPU9wqOSfzF5fHNMp1xA-LzmcXrRk5QxZWBjUOZOS0UiJVeQQU8Gm4-6DCIqcADmR5v-QlCQwYvV2uYLGxzX1D52OjcsOmui-Oe1sdGGF0pNmk_wPuckgQPBh2m867uEGAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/31275" target="_blank">📅 20:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31273">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3u9gwcumV3VbopCFtMUEMVUAdODlluvrPM6F0Pcx_VCwHf-BRX0RQqkvtQHTnefYmT_QAmzEUz0o2Ci2DI9SgliuWtOVIAQRMnCYq4UMwv8NLE0W_av4S1zcXnvnfVyeDZUUBp8VzR-FkgvOUiA1K4cdQWQPGxKQEP2LjfgOUcK1hyhPc1k--HPHuvoDCrw9p6P1637WpIGGeR8irlwESmvAxa4nfT6l8avXNxqAE4jmRho4vBZsAXNV-uxD3tYUkqg3Jf7dXV0QKdSeCQ3edIeyGT1JPNDHOgZQXNJPcO_Faxr_50USQGwSRAnXvRS9nQjL8XrBE31cIHFQjtsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_MO2Sm6--7qTurHn_znScqzXC1TUZZAQ0KHA09cYWHX2UqmkZxUPdyQsgqE00aGOH0zBEy1U8V85qygaLe5_mMWEDGaP6U8QsIjLYQsy5T4Q3Qfk5zNeltTKVZZw8tciLx5eHYlOOOwrR5MZORh9E2d9L0lSBlAsrzTCSVP6gro4aEuXQA8LEsaQJV2W6OmO54N64Xady9UABO5sowigCOSoI2bcJr02JsTsKUWwl2vfYqhxL6ew28j3lExCJDROmT6dvBwKu9Wp9xSLdVw-Dyj074hg5W0zwTHucseE2zVjmOxdne7xlUSdugynsW4-ZZuyy6msbprjex8j1aabg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/31273" target="_blank">📅 20:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31272">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=TkxdlQjNI5E1qDxxN54aO2H3naND0ZNeTuY3vVEgQqRGpG3LkArrPzFdXy77sy4oqjN_7wp6S3JLfoegB4IDpL8gC1Xg2AfwVSfmwlIoBxJA9OTI-oKiuIlDGQBU-QpMyEqniJRnxRVkE6tI2o7GrISAWw01i7KEITh9iMLSZJFo6VHvtuLFyzXaMNxdG9RpCSzglYpDaqAqx7WdD7UXqffekMNiSSV4TAlRRsz-HxX0UPaWypzZnxxydUCWBWMf-UM_3e8bjDMoOjTf7RCIXfvJkLtj8PMk4NqRfMY11ytBjIq4_uaPA15kFbG53vkNCZhp9bBI35JXaCInf_ILbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=TkxdlQjNI5E1qDxxN54aO2H3naND0ZNeTuY3vVEgQqRGpG3LkArrPzFdXy77sy4oqjN_7wp6S3JLfoegB4IDpL8gC1Xg2AfwVSfmwlIoBxJA9OTI-oKiuIlDGQBU-QpMyEqniJRnxRVkE6tI2o7GrISAWw01i7KEITh9iMLSZJFo6VHvtuLFyzXaMNxdG9RpCSzglYpDaqAqx7WdD7UXqffekMNiSSV4TAlRRsz-HxX0UPaWypzZnxxydUCWBWMf-UM_3e8bjDMoOjTf7RCIXfvJkLtj8PMk4NqRfMY11ytBjIq4_uaPA15kFbG53vkNCZhp9bBI35JXaCInf_ILbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌های عجیب و غریب دروازه‌بانان باشگاه‌ها درهفته هشتم رقابت‌ها بعد از اتمام فیفادی مهر ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/31272" target="_blank">📅 20:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31271">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK8MZcpgD1Y8unX60G1xbcXjyv3L7nucl5E1AklspfUWgECejqMZEEfO4PtaFCiI1WEu7IGrTsHIB0UbhGkjVWO3BrMr0x8SL8Ax_vFRFbF3_7nyNHJzFmK1w88XzvQj9OdS1IFYHfD6zVtKeh2zZyRWzGBIl2xzP_7BYU9nCaeIvfnSl-eZ-GJnEGEwvm70vjNmZfdnXVi4JRaLJXxzji93-cFL9-flblJLu8MRgTMOs6r3vIeDKOTK0gTnC9wjvA83sVXuuET7zwu0AvAWRYWaCQMGoRE1BZqcP_-bK3UlBSyBZCci1rrHUl9sPrJb4TPy-g-OHaolyP4gjrPDGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ کادر پزشکی باشگاه‌استقلال به‌سهراب‌بختیاری‌زاده سرمربی آبی‌ها توصیه‌کرده دربازی‌روزدوشنبه استقلال مقابل الغرافه ازآسانی استفاده‌‌نکنه‌ تا مصدومیت امروز او از ناحیه ساق پا کامل برطرف شود. بدین‌ترتیب‌به‌احتمال زیاد آسانی در…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31271" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31270">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/31270" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31269">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX0_pTTTxyaZKGQtd59i7CHkPXG64Z-6SM3v5eT9PFBK9x66q5dIBhYo3Y-neZ59LIquL80E9A4kSwa-YkQ1PT3SjLD0pt6UFP_LIXD98xMb_FWp0PqTiiM4fAI6Oz5ChBUS5IhgwzN-WPueVg9Dv_ndblN_zcAXKBR8cBSkL-fz8W-EMpY_mE1nsFMuL23-nBkmUkqup26pvEhKoouZ31aYdD71O7DydN-4smD98eGSSLSBLeSkceLhWs6XkdrN1X3fgOaTx4SXZQmXS-ZLHgDKhbWh0jeMLEraRMIk_uDSSulJ2oEwUOW3Y3zTfL60mwR1rOu9COiyaZLlEUHKSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/31269" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31268">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0BAkWQYPKMYrU3HgzDlZBo0d5jH0b6auX4j-tyDbR6-Tz_GsxAgGi9QmYOlE3M59mhVLSFB6q00FWg3du1YxlzhXS9OT1pYRHYLDyZOqh5mXCv83NKD-SSkJz8CyGmxPMIx_xtW792GRgCu4cj6iCNYqxB9ttZ5jzwRYxV-h936bXCyAFOqwlf6j0CQGQjc_zP75EynY7Xjs4Y-0hrR82CKM0p_Q9tqcAS4MITUnai0Ql2YpVbEv7j7HyoPnulx6IhF33Yn-PbbLi8AMj1g48z_ZU8ebqIou4eA7_jet7C155QmgAWHAw97mzZ7qIPqt3IT5CM1MNJbig9ZfSTpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ وزیر آموزش و پرورش رسما از تعطیلی احتمالی مدارس به دلیل تهدیدات جنگی خبر داد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/31268" target="_blank">📅 19:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31266">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-R9WPBrPaTlcUuZSUcxmT1QFlk-8lzmUMzMj_R_ej8YiaY41ByosvrWreaOeLTl86FBAVTyfZQSB1k8m9tEvP5obbS1-RqdHc4GyxFAbHUSWHlXBySkK5xRhzpU5V6zfVj0Zq3CFXbTUBbHbTIV74fktj4HEKAaB9PqgrFFZjL8RTEOgo9wYaNNo8h0otSl7Y6nj3yWfqdzrhU0FsGu_tFzoPmKWBfDmfcmrk6PkT2aC7FtJ_nlSqEkvJiQeGMnIA-bY4llaDUX_gEXOV8ys2WAirOZL9bvNWvUJBz5UPjv-X37tWG2NxLKtaBN8GIWT-ZKn24iiQMAE2RIH1z19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MesuaPHL0ixhdOKfQG0-h8tKXljVdu53-KNUvKWwpEVZCtV6MFZrwAnSs6laINpEmVMI2tDl0a_SxYw5MyVRpyQfpavtC3tNM9iWzeGTaz0zusytjFaDg0NX-suvL4okVg2M2m1_JSvcVB5AkXvpMUXw4PQP-hoHmvo6ijbY32xCl7AU7HsvcCEYXXSnT5KLTFkX_0DfwEZiZwV5cuQIwpQCJuhCApB3l22R04X-hjBxESF2yrKvQvy5HF5P5pJ88gyB_W08762Yts43KUVJWPEsLln52O9epUTXEeGTMeeIU4mO10AX5APU21_ewdXs_dxu-vB6rPlGFKlE2Ma1Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بانوان هوادار پرسپولیس درقلعه‌حسن خان.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/31266" target="_blank">📅 19:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31265">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW5OoHhxBiLVXL3Gz0PKuQBM7fwO7Yqm5Lnd5ThUhf2w43Z7llQHkYfT_GN1vdZeLW7MzCWEO3CzP5Eoo-4uXp-pOgMhFotqGLsn9PWYScFPz1ZyJz9_gHLqLJUEgbYMiXqTNxy8oIXA_5AxfOdTEIEQyXhBcyJ897l6-MOZFWNDD5A1y241eKZmly5AFoj9KkAYtnxg0E5qPdowOqgVpLPcAwOeUROvnv1BPnZRX7ibdYOlEgXDv5feGO0lGof2oZtmL7T0iSpaZG7j8meHouewgOQpKsUnXxFsgwm_NUjMI0bb7T5LQ_a1DKcI7-D9zeSxa7-148qNqkM5VFyqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/31265" target="_blank">📅 19:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31264">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Ba3939bWsjBCNBMFcRRxdP8AoOC3AIR1wcV129BIYZGcgIwV26cnXToD09YzZ-bSpdbrVygRFIgcXCG2nDsyd_cYkoslzZScBtCS5A68pFcpTQPid6tOwvRGU3tWBpxYqsLImrZBlwvKCp-HdTeRNjsf7G4i8laHk5lRq1nAUHWVqdHrE827CHz23p852CtNrbJVdkH1Cdm4WX2pOMcbnMlUmPoLILd0q2zfMzndaLToUbxtYepWMc_gojwtljsilVl-WhMHPS2wPqYRJgTzRdd9zZYpBZc2bp1ZB3xWnDb9AuFPifmX7KaBCEjS1zXUCWXjLqsuDM3JNWCM6uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/31264" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31263">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiEeCwg0hrhow9zWkUMcO36zX26hoFN4OPUHYpT3QVICbNK2EVPfLa14ITw07-QxN4lmBWocVl5ZGG9YPJT_koGV4tI3assMaFFfl279p7KG4mtF2W9VBe1XHXveGzn1Wtd4MITMgl0BeS0BVMgGGNVUkXRNxA8hBtI0Z-gnxSdlcVeCUNGVoc0AK7iRUOS2730qMNIuDlW-Y6vMbfbMrIHtMODokEZ8-OiOT63QZTb9qQiQlzx2byHQ0gnrOjpskPCpG-33_kqBdLMh2aa9ZTPJ6P7mQgO0PmbxNUN-ySPEE8fTkGN7N5aPLX3zRpegeO9dV0KM_sW7XE-CH1R8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/31263" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31262">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866119f609.mp4?token=mLyVJfYMHEavEIcO4F55G4kM8D5xl1IwMOS-VFIsM-uNkE1AOy4OymPng0UQ-3NkDJIDjLIsla4oAAII4utVH_11sKeDG2rs_5GukmyjWbZgocVUnaN6RAzXwqh6m-6U3LSkL0ld-qP45q8iD03Bvp2-31-LUl2-KKc1nLLHHhfGKgkDDouK3zlGw4y360goUxB4Kjx4OcQpjNqalXFa--S2fvI5cg5Y05-haYo3wEtKj4Ol_Z_EnxnY2uHhBF8_S7nuxMhSj2HfMEHZtRrX880ykrNk8-uUx_vDfbKnwAJSiRrPknzx9PdPvtrHrhM-b9GLJpuJJnUm_xMg8W_9_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866119f609.mp4?token=mLyVJfYMHEavEIcO4F55G4kM8D5xl1IwMOS-VFIsM-uNkE1AOy4OymPng0UQ-3NkDJIDjLIsla4oAAII4utVH_11sKeDG2rs_5GukmyjWbZgocVUnaN6RAzXwqh6m-6U3LSkL0ld-qP45q8iD03Bvp2-31-LUl2-KKc1nLLHHhfGKgkDDouK3zlGw4y360goUxB4Kjx4OcQpjNqalXFa--S2fvI5cg5Y05-haYo3wEtKj4Ol_Z_EnxnY2uHhBF8_S7nuxMhSj2HfMEHZtRrX880ykrNk8-uUx_vDfbKnwAJSiRrPknzx9PdPvtrHrhM-b9GLJpuJJnUm_xMg8W_9_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/31262" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31261">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=YuB5JUQz6x-qG82yPZHDTLSrAAr-fyY_h0EtDvHcRFlXlgvBR0BKqMankLtCRwfX6OiCtv3DCnyCVajqUnWkDjFA-9WzEug1H1C08ifggcOpHK1z7XFp9plW99SOLrRpcM_H0St7DVBVXBvpq_VHkUbjyMbxaFc4LimeE3Vp1ugEXh2nY6Lih3sMdb-ngkp5FF0p8jGmAjeUPoQe89-YOCMvc0nUiWWxViilIHEZjG0iAmSMfhGLScPNx3ZDFLi8l9dPw6PU-y3_Dac2gJGa0sc2qsGaBWATqHDnDM3dFm2B5AG-OnZZMJbkey4t_BRzMecTbZMfAQ5Ke-muA0Hb4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=YuB5JUQz6x-qG82yPZHDTLSrAAr-fyY_h0EtDvHcRFlXlgvBR0BKqMankLtCRwfX6OiCtv3DCnyCVajqUnWkDjFA-9WzEug1H1C08ifggcOpHK1z7XFp9plW99SOLrRpcM_H0St7DVBVXBvpq_VHkUbjyMbxaFc4LimeE3Vp1ugEXh2nY6Lih3sMdb-ngkp5FF0p8jGmAjeUPoQe89-YOCMvc0nUiWWxViilIHEZjG0iAmSMfhGLScPNx3ZDFLi8l9dPw6PU-y3_Dac2gJGa0sc2qsGaBWATqHDnDM3dFm2B5AG-OnZZMJbkey4t_BRzMecTbZMfAQ5Ke-muA0Hb4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/31261" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31260">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=tOafOF6dbB5tK8txlbG3f5nH5HfSb6cVtM4oGKG5p67A3W5-Rk37-busiVMJBRxBkghm8G4f3tdoHPGzCLwust6DX3ikyRVIEUpCj9WkytxXe5VNywDCQvstEzcS785BUM5yaDb-745ZEteChxZlGPmXAEDPghODEuoxuI3peHcOCsXs4k6uipKgSXJKxuduPmWPOVAbDqd6VZtXxHhk0S-Xd9v0EkMCcR0TgWsSao8Owl6ofXPhe3OAqAfD3GWE93qBCdh1QPrEBBXV8tZiZPm-kdd3GBX0yPbyCKI5UNGNCO_pmzjc3Sx7oNbyVWLz04sVqFLpgW08sGPKuw0gCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=tOafOF6dbB5tK8txlbG3f5nH5HfSb6cVtM4oGKG5p67A3W5-Rk37-busiVMJBRxBkghm8G4f3tdoHPGzCLwust6DX3ikyRVIEUpCj9WkytxXe5VNywDCQvstEzcS785BUM5yaDb-745ZEteChxZlGPmXAEDPghODEuoxuI3peHcOCsXs4k6uipKgSXJKxuduPmWPOVAbDqd6VZtXxHhk0S-Xd9v0EkMCcR0TgWsSao8Owl6ofXPhe3OAqAfD3GWE93qBCdh1QPrEBBXV8tZiZPm-kdd3GBX0yPbyCKI5UNGNCO_pmzjc3Sx7oNbyVWLz04sVqFLpgW08sGPKuw0gCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تثبیت‌پیروزی‌خانگی سرخ‌ها؛ گل دوم پرسپولیس به صنعت نفت توسط علی علیپور در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/31260" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31259">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=m48dDSEpiFWaJ0xgzOrEXZ5QKiFaOhRs2CxLwOOQ1NPEeRzxeY9Amx8e4HkaZz_pxtMfABI82QwelS5wYVIFSM8r1_aiV1hdwg5zzNAuOiilsFTeiYA4T0Jb3h4nLqgPM2OgIxBTF4dqftyi5DDqJmAJnf_B5chPSoXiuIeub898sPlHqPH9YMZVbiDM-nh3RrUISJEnwbbdomuIvHFkGhW9xlU34ZJkVS5BjFzF35syOpeHtb6fBamqHHP1yFDt3vibn7qtjd2mWj-CrysX8Y2u9RP3gdsLIt1gyy27nADHACffbhVYTUK2ZsCVdU5Y3K0gSlb663EL5p91Uj6LGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=m48dDSEpiFWaJ0xgzOrEXZ5QKiFaOhRs2CxLwOOQ1NPEeRzxeY9Amx8e4HkaZz_pxtMfABI82QwelS5wYVIFSM8r1_aiV1hdwg5zzNAuOiilsFTeiYA4T0Jb3h4nLqgPM2OgIxBTF4dqftyi5DDqJmAJnf_B5chPSoXiuIeub898sPlHqPH9YMZVbiDM-nh3RrUISJEnwbbdomuIvHFkGhW9xlU34ZJkVS5BjFzF35syOpeHtb6fBamqHHP1yFDt3vibn7qtjd2mWj-CrysX8Y2u9RP3gdsLIt1gyy27nADHACffbhVYTUK2ZsCVdU5Y3K0gSlb663EL5p91Uj6LGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شروع‌طوفانی‌شاگردان‌تارتار؛گل اول پرسپولیس به صنعت نفت آبادان توسط تیوی بیفوما در دقیقه 5
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/31259" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31258">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9dDE1B2rVO1bZa6IrS3kievp_5oFltY98jBhZyGR2fqgyzpUkRMUNeszQt2uvDXGcG6UckLg0sNfO1RbM3Tvpfzh_xbln3ecSAa5Z0F7ODYFDA53Tke9RN4ZdIc-EBhZkNzholOaphYLFn_ZBa_ESXuW-xE2sOtfcTU0BShc5P4b1KdANQyLMiN2zJTe_DIucsY2PYFG5UKrofxfxAJ9JYE8OCp--ws4x-9I6fCFAKyzCwu6OXs53sF7XJeay4iADtPjYxv98hhofOiDLT3Xjf27VcnSMimQUhOVN_2FcOXRakLb6rzRUErOqGujUOkTeVOlu4h5FS89R_bUiZ21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تصاویر جدیدی از بازی GTA VI؛ این تصاویر در بخش موسیقی وب‌سایت بازی قرار گرفته‌اند و نگاه تازه‌ای به فضای جهان GTA VI ارائه می‌دهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/31258" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31257">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=Qgad1eh7zqkc1fBXVcLVK0957wPt0YnA2UeKWXHT2pJrnS8eq1Yr21YUKcfUItlcToOTY4nHOjHhmzWzerySVh47wtPkYv8k1R06XWoKX5aYIJ4jUM6sKRtjlu1UIurqe-hqEUsVAcaUdugams-NVZ1g-XDKtdtrQ_lEvo_vR1uW9nG6sKwF7-zQMUmHh-sY9UF8YREZtK2gnPPUBtTa4604rAFTR4JDG28URyXL2cVNEa9qIwzzr4_KllsBEvmNNvYrEvWetgX5ssN2e3cDwouXc79hB_Ho7Dzd_RiWcqBLrLH0RtSFkVNyI5d4rET_Fp7nN2jhFXo5eBWOhpB7Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=Qgad1eh7zqkc1fBXVcLVK0957wPt0YnA2UeKWXHT2pJrnS8eq1Yr21YUKcfUItlcToOTY4nHOjHhmzWzerySVh47wtPkYv8k1R06XWoKX5aYIJ4jUM6sKRtjlu1UIurqe-hqEUsVAcaUdugams-NVZ1g-XDKtdtrQ_lEvo_vR1uW9nG6sKwF7-zQMUmHh-sY9UF8YREZtK2gnPPUBtTa4604rAFTR4JDG28URyXL2cVNEa9qIwzzr4_KllsBEvmNNvYrEvWetgX5ssN2e3cDwouXc79hB_Ho7Dzd_RiWcqBLrLH0RtSFkVNyI5d4rET_Fp7nN2jhFXo5eBWOhpB7Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از وقتی که مسعود محبی مدافع تیم خیبر توسط رسانه‌ها بولدشد و باشگاه استقلال نیز به دنبال جذب او افتاد هر هفتههه داره سوتی میده لامصب. این چه اشتباهی بود که تو بازی امروز کردی پسر خوب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/31257" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31256">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=p_E8xjUzQ54gOkY8phu7OKaICEA2vj4fw-LeHUBf8slTLWOOrY6Dg3UU42FVyl7khrJ9Y6_8PRbNR7cwc8QyXxt7sdGQ3PO7Zy_27lP7PshIAPx_YpdqLCFqcD6uM6pRZSwkoUw18QRviewynP1mVvDiLhB4wvEaRYt3BnEsW-5DBoZDYlWMuEJP4wfssoWSznezyMoMJER2u0eBcPhQ6xPw2dVdk17Cg2Gf9uGiK35UhwTGzgLauu_eEHuz4Gp5-qTuZKeOz4I1qfI1-UassoW_W4r-cVSBCeQZYrRga0f-CQtcQFH9mkxm7QNs43MdNFXecgGrsQQo-HkTNVg8Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=p_E8xjUzQ54gOkY8phu7OKaICEA2vj4fw-LeHUBf8slTLWOOrY6Dg3UU42FVyl7khrJ9Y6_8PRbNR7cwc8QyXxt7sdGQ3PO7Zy_27lP7PshIAPx_YpdqLCFqcD6uM6pRZSwkoUw18QRviewynP1mVvDiLhB4wvEaRYt3BnEsW-5DBoZDYlWMuEJP4wfssoWSznezyMoMJER2u0eBcPhQ6xPw2dVdk17Cg2Gf9uGiK35UhwTGzgLauu_eEHuz4Gp5-qTuZKeOz4I1qfI1-UassoW_W4r-cVSBCeQZYrRga0f-CQtcQFH9mkxm7QNs43MdNFXecgGrsQQo-HkTNVg8Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ علی علیپور، کنعانی زادگان و ایری بدلیل‌مصدومیت این بازی رو از دست دادند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/31256" target="_blank">📅 17:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31255">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=mqo9Etn2SXc4WCbm1KKU7zPvg-II0kiXY0l27D8E8vzAfrCTKlue6qBS4Hapcye9o34s2OSMmbNfE-PWULOBL9iHhdnrppuF1WIY9rEUx3XA0ZlE02RlZyAxbcITzFh4_8xrnkXIMaYkNEGGWyNm8stH7qxYLDpC54xHTvvae4Yq9-lUdTHzEf4GvXmjKdKdcS7zigi8oIJXFmSUyAFBdbn3cNlUwA7ajGEDtwKJsXz3Uu-BCFEODlPB5yYDd8wH6CL5LDjXie57lq7oeK1qC1pPgFDNbtkATo49SsDcSFcVxBBrvrEvVNRNoH7egYnPSKBrowXVpR8xDDId2Djamg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=mqo9Etn2SXc4WCbm1KKU7zPvg-II0kiXY0l27D8E8vzAfrCTKlue6qBS4Hapcye9o34s2OSMmbNfE-PWULOBL9iHhdnrppuF1WIY9rEUx3XA0ZlE02RlZyAxbcITzFh4_8xrnkXIMaYkNEGGWyNm8stH7qxYLDpC54xHTvvae4Yq9-lUdTHzEf4GvXmjKdKdcS7zigi8oIJXFmSUyAFBdbn3cNlUwA7ajGEDtwKJsXz3Uu-BCFEODlPB5yYDd8wH6CL5LDjXie57lq7oeK1qC1pPgFDNbtkATo49SsDcSFcVxBBrvrEvVNRNoH7egYnPSKBrowXVpR8xDDId2Djamg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بخش رسانه‌ای باشگاه خیبر خرم آباد در اقدامی جالب شماتیک ترکیب این تیم مقابل چادر ملو رو به این شکل "یه نوع شیرینی محلی" منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/31255" target="_blank">📅 17:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZqESWV_Hi0wuiBUHgnzRhoyRvEE-c1AtjVP1uohrFFWZomT1mPhxADCQ0hOPqahkGa_GCmf54vNzuG9yeYysoUYdd27rW-imvPtsl76duE8Y6wW6utIXLmgGediRYTNL8yHd3bj23Tw6eUPboVI9ckOHRkSmnHx94FIm7k2wrZx76MLvc40ENQwCN4ct2GuNFfCYy49vdnJdpNDL1FbDlrJc3xqzmtr1G7fRZk3kX6OksIs7sN7bgji19XzCm6QHuycgkcmxYlGo7C0rdxcS1CR12c32_lHMbgfF2fnFhMrbQ0EomLRHgOwWAqHBxxdVnIwhdTidN8Bu6v_kvGltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان دو تیم پرسپولیس و صنعت نفت درهفته‌هشتم لیگ برتر؛ مارکو باکیچ و دنیل گرا از لیست سرخپوشان برای این بازی خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/31254" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31253">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/31253" target="_blank">📅 16:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31252">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwiMchr5iqOGJC6rXabIGekTYS1Y-PmOPdwd4CT1qAS0jS7Ap4_pJDpgaiBJ5_UwzegAmFI6TM9euxVVJStvHDU-CVo4AwurqfJJI1StYis7XqmqNT8Zv5qNoP76ovk9kfJRd_GHSQGALZxdjTmHEi0GObWMDhua4rAT07OC0OCE6P3_CUvQsA26rN1HT0R_Lf8g5fNaC8SYUo_1XdHNEeY7jMetChPIjBDUtvbDBJPYdTIg9TVVWAKZ0svLk_vuH2kv9cgt1fE_9XIha7pavA6dImcPcToE10EtW-4l7HRR-Wib8doZK7fEQb0KBYLAW0mSi05M8u9VU6jMvCy-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ ترکیب تیم پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ ساعت 17:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/31252" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCD2z-YRTN07x0EtV70aZZSLim9nu4HpzuqlN-ocKxgpgKUcspIC6WKFUujMTvJW52l1VECDCMpRR_ph8QhcmFHdq4jFytqXjRWbgx_zwiXeCJ3B4ehQQ759DPJgS49-JSWQOK1bBJxBZgU8HbJhjmoriv4_9Em9OcFDY74pY5aQ6XOHLA_Sk8O2RDjQtyXU6zykVXPxm_q5QETv2BFqRSf-pdM6Gufzk4T2joLT9nkSK9AHnFDU3V9h561b0NdZLi7oL-POINn6_6zdOtpsA1h8pFtNfdsMQyFARh1UiJp623k0uEAmoJTK4M-4PRLfdAsKMxxBD4MwSB_k8Zw6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/31251" target="_blank">📅 16:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdmUNmi3SOVvyJCQAFrjWnkL3bBzlndMBP2aasCbVouxCIAdvUNUhSqaPejx0ipFHrYNsZqs-8kT0QieitmmE_8vJnhIyvJP2cI8a-cY665qLz0TmXONNAxxY70_EvO_UxSmFL7xXC3IDqlM4pFFOGE2I-O-FQ_04tDi8Qca18BtzKnspG-RzG8xhciLww4K5Mziz_e4DwIRQT7p_c_Eaa5celye-d4-ITb7lF7wsVM0Z7Qkk3fsI1AJj4Q9Vo2zB8erpKI0THiXZ03WhJbxmMOdlCxT7dOuK_OsVPh_G1kkywg1Mz_8vB2JkAKP6bRDVTxl5QeOTkbZiY6q2Y8XDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/31250" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31248">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz2XJADiZamrBXZXygFRFZW3Sneje89fMwsXzHRWO6CSrp_yo18HuKGoGfP7lnuBlv_p1twrTHFIihpuAhUkzAqf-ZdkYZKXPFljf6LTrppHpdnma6XvNFpdY3AabT2hmOSnSciQP8-mwHOklCSrR74ceu_cLHSVKz60lc3zuCX48gqbeUH8dZi8e_1LU8yK3OZdFQcGFv06kUp-t4MZe26mO9HZ1bQrRpSi7sfT3385KGHT4jmYf22K3STuwD59Y5QI66JIFKo-KQ7NHvwphyN2IWLNFHuQggwsU1BPUPLgVG9KbrF_HhWxDrwWSjv3Js6dd7HpfvcwnGZ88bn9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxtBX9qdVHgUHdM5Gs2CTX8j1S3q1M2DvhVGbFTjP91OFP8ICTNhw7-bdZch70ayu4IXcSWgIOKXNaETNjR2jB3Dq3MuokW1-jNptESDFH8Et7Wvfz2CfcNxGdve_19-oBue4I9u5n9DTk5kTWGbdgEcOrqthoEBw-TFk2BjtnmfkpXxS5UbVLqsrYbEOUxts1wPSS6ArJ75wM8J5EtGqQKNPXijFYcT3LFhwGOrmQN3ExpVOr9kyJT0rACdPrEu7Vi0FGqD83OdfHxxU-DetZqErWq8UWj40NNI5cCBPfCpN_jI_hOeKGB4ntihGKrot1VCSpi9gcj7SvnPwoxTJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تشویق‌ده‌ثانیه‌ای‌لیونل‌مسی شماره 10 آرژانتین و ایستادن به افتخار او در برنامه ورزش و مردم بخاطر خداحافظی او از تیم ملی فوتبال آرژانتین در اوج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/31248" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31247">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبر داری فقط همین امروز می‌تونی از اسنپ، طلا و نقره رو بدون کارمزد بخری؟!
🤩
کافیه وارد سوپراپلیکیشن اسنپ بشی و از بخش سرمایه‌گذاری، اسنپ‌سرمایه رو انتخاب کنی. حالا می‌تونی به‌صورت آنلاین طلا و نقره بخری و دارایی‌ ت رو مدیریت کنی.
پشتوانه خریدت هم اعتبار اسنپه و هر وقت که بخوای، می‌تونی به‌سادگی طلا و نقره‌ت رو بفروشی.
همین حالا با اسنپ‌سرمایه، بدون کارمزد خرید کن!
خرید از اسنپ‌سرمایه
خرید از اسنپ‌سرمایه
خرید از اسنپ‌سرمایه</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/31247" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31246">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua81F3pAUaTxx0fUspuPbpMTgJqg9jaVZhggh8HW5xVOfM0rZBLIwa0SPNxMCFkwTvkIb_ntBdBMekm7-IpEs-oTjbmvlBiZbMv0UGgfNe-6qptl7uIDGCFz5pns3OF-OlWgSoDiS96oLnBDzNr-P0dg4zUGUvtKPqWqD52m_bzqfP0hXO7e8Papc290QDmridy7KigsfCRtxMWF-w8S3tm35SFmVEnlXKG_z8xC1Vmj1eKUkEZXpTKgJcZNcyz4EpuGmC7F0H7M5EJVwfWJO2WrPB8x7KkAAzdIYD6LIkiQ4plI7vSQ5xCUGwL53yzc3vzt3fnkFF2fY9uh60B1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور، گرت بیل، محمد صلاح و ادن هازارد درکل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/31246" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2089087958.mp4?token=Sbok8w-UPc6tBibjpEcP16mLETFG93rBW0GlO-OpmM_U7cgRIEtFUVzx4Gz6-m8eDmezsAkoi3b_Uj2Y8OFyx_X2rBJ4Qx-8zXwCkU9w0fJvZ1LgY3B-qHEqTMmR8tN4a3RH5ryD2UT-Sp1gU6HQHhvliFyD9onDOtJQddKuI1J2Tr7qDcPfBwfc-bUGhaQOLw0iP8I1LdsqmJ6giJBzlDsyRM2fYvLwkM1ix4K1O6aLwCfaxTkR5zHD1q4ToaZHgo-OWqgH8jX8c2tsePtp_2NDYz_wKW5a3UYZ2cStRs94GM5M8_yQgpJ--Yxgx2ZxCPs80gNoXbY6SpJ1BVSOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2089087958.mp4?token=Sbok8w-UPc6tBibjpEcP16mLETFG93rBW0GlO-OpmM_U7cgRIEtFUVzx4Gz6-m8eDmezsAkoi3b_Uj2Y8OFyx_X2rBJ4Qx-8zXwCkU9w0fJvZ1LgY3B-qHEqTMmR8tN4a3RH5ryD2UT-Sp1gU6HQHhvliFyD9onDOtJQddKuI1J2Tr7qDcPfBwfc-bUGhaQOLw0iP8I1LdsqmJ6giJBzlDsyRM2fYvLwkM1ix4K1O6aLwCfaxTkR5zHD1q4ToaZHgo-OWqgH8jX8c2tsePtp_2NDYz_wKW5a3UYZ2cStRs94GM5M8_yQgpJ--Yxgx2ZxCPs80gNoXbY6SpJ1BVSOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/31244" target="_blank">📅 15:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmL3ZTriGrG2BxUws5mavVEhqJvEIilybxi9jkXpHmXbywZAgiEHTQlMxlJiadaOxvfOxIY46RVXtt5jeykR2SiSN3C6JSxZyx0F4Dh038mp9PaN0tbQVMvjYO2JJIhQ5swtGO_9_4fJxa2s6xhDSlyaTgG1znMUgAsSlelGLtEcTrHkNpgiS6Y4XTlEbFmZUMj0BKnnHUeTaMTcLSx5yNQFUVkPpeyPuPPP_f_PbvE7vX08R6DFmLPLG3uotdraL-Q_3fZO7T5YTyeUBLemq9w_z8URScEh_T9W24gP10PdTEfbyX0bUh1xvopSQ498JtRNDw4ZI_Roi1rxIrjJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/31243" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=OmZ2O1Ir3oJCXswCKUUQ_7zhgzFSLjlVH--0xs__cfj6yWrg9qPE9CChab1mcwznuyaQ29CMCiK2Qq0GKhD1BxkptagC8YzyVxNmzKJBHZlTqymVt9-p-EIbp0AJOyQYMJtRLqRssLgu36f_IGT1gdd_Jcdxqi37fdSLNQEcKH2LvX6JltFcqLVAP3-LYoDSx3mlb7z2oJSx6wIUH_vcEyCpx03X-Axia4wdSmhKUfGCx37VxeR5UORpKdT-bTDX7qQZJLs2IBeGYx1xF2H_PONkS7z6vfy73GJUZX_o3TEFkXKbSrDy-H_QgEaC1_94rdVNJhNVfGQtEnQ0kBc06A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=OmZ2O1Ir3oJCXswCKUUQ_7zhgzFSLjlVH--0xs__cfj6yWrg9qPE9CChab1mcwznuyaQ29CMCiK2Qq0GKhD1BxkptagC8YzyVxNmzKJBHZlTqymVt9-p-EIbp0AJOyQYMJtRLqRssLgu36f_IGT1gdd_Jcdxqi37fdSLNQEcKH2LvX6JltFcqLVAP3-LYoDSx3mlb7z2oJSx6wIUH_vcEyCpx03X-Axia4wdSmhKUfGCx37VxeR5UORpKdT-bTDX7qQZJLs2IBeGYx1xF2H_PONkS7z6vfy73GJUZX_o3TEFkXKbSrDy-H_QgEaC1_94rdVNJhNVfGQtEnQ0kBc06A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌نمایشی‌که‌یه‌مهاجم مقابل ایران از خودش نشون داد. استپ سینه‌ هاش آدم رو یاد پرایم زلاتان مینداخت. همون استپ سینه‌اش رفت تو گل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/31242" target="_blank">📅 14:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31240">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvpKGGSygx-9gnWozYN5ofvJ9Zzyp6ZAyGnjUl4skOJKfgyLQpNpTH98dLcNZ6QmITy1pT-RdT9AemhFVOI-Nav3iHJkPvZG04xMliTspya1cmr-qgJhMN_s9sDPs6ApNK_ZSJypum_gbtT_t-fC-nzMldNZfoStrf4a7WyjN0psbRsxkXVcwI-VmX4dK10wMydbyNuzjZrU7MzIrMGx75Mh3MBqrKVIB6ZSE4mE2NvDR5tz6e0hoSAEDrt2T0vBAJt9jQMkInqZ3vBmlh2lbRGeOy8-CRZsGG_NbJZ1iEcQZDidl2bnAtf1mrAmill64DBbCkKkyk88kVfOCDDC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6dwuByrKuakR7zTMFGVPTX37qYL2V2BXx18UM17VyC-vcJpLkWyhdMz4xBvHP2m3gpN4J731guM4rWs_aAkgaeeSU7X8qqV48fynsPI8Jd5qfYVfIH_PArCXh6fREW4O0eT8A2kxDpoa5i1--zy-W-cWPLlDTJIQ0Nx2pYVHbey88z7UVdsLaW54hkolto6S8hgkAnvlsN2PyC32Q1Y-89sjsEQh542HdoLmxugvwd_It7xs3s5snkKfz4e0QvrOE8I8wmi0t7mVgTluX3KPjdTm7u2L0wMGVLoqC70vC0HAlik954lN_FafM14I731yFxbDANyqL6sn71slXGm4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حضور بانوان هوادار تراکتور در ورزشگاه یادگار در جریان مسابقه روز گذشته پرشورها با استقلال.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/31240" target="_blank">📅 14:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31239">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy6KwTXSvHj2t36buV04p1ZugdSZmrEdnnD3fVypUiaFtFbVAttfJB--FbI66M-MCS6CBfujIqI9-z1PUwqUoJmMQ_kOG4Aq59SRnxmcT54_bKx9vIVwsGlTTHzpY2fbzxSIGnJF28vRB0V6D0gG47lxwRchuk9DWUrpym5XjeTFRzIWf7CQRKItBc9bKIo089qp7rXNtHHb_YYM4b8uZ3a7FkKTsoSCqEnDTPIvv6k3BUXg3dLIDYDy0xFkUHSW9RwbZEiOtwlcinXZ-jdatHJn3_wBVqgbGnXPKhcHfL7UIggfXfNw4UNnvrXE5aKiKGmm155AOLfAQR0WSkX5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم پرسپولیس
🆚
صنعت نفت آبادان درتمام مسابقات: 48 مسابقه، 31 پیروزی پرسپولیس، 6 برد صنعت نفت و 11 بازی مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31239" target="_blank">📅 14:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31238">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-Vwcx2ATMc_828-bhr1Th1CLDTpV6O-JrU2YZReFu8QXta-KsVS_UVW8075IFNDEL0h5RfUFsLliytgIi48WnJ8bqKi6FA0srG2eDiz1UXOO7UUFjrYD-HpX4duv0Fuf6YioySaEw-e-bZsjFjFKnt6gTj_e9oYAI-hk3nnl__vEA0R-R_0UiZL7GW0bZvvITxqbZx6QvwN7YQctRF3OkVdcAdk6wuS0KnK2rVdixNyxZmNmmtMwD0rS7KbHaCfOutMjroLFYg70H2Q9u1ttTDRJlrYxHZOChrOFb01rCZ0DttNQ77knQnKWAlrzpm2tlfP05M1W_H_B0vv2nm0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31238" target="_blank">📅 13:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31236">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmF54gO1B6YpPV3OYyGyJfk2h_lMmOj6EOLZU1yZC_t0GJow6oIXRPy4sNQ9vDybpACoWR_CuhxD7Qds91m0bIh_s08OEcB5_QhGAhMm9Ok1wCNqRwxyJKKkZa6oW8u3K4OZGtrMC-8hwIF8XRBDXWwN37LV3XTnLg_glgQxq19iUy3wNbLf3telYq52n7YTw221oFqmmSfKLxLbxE5u8ilvylDkVMD7medxL_BxrCWeYQVSePTlfjLEsUubmzhvtWyMkxkw5BcXYxItV05SR70IXV9E1LxG6t0__-Fo9BypB-x7jP7xVC7Q57OC7V5Vb1W7hQcBCqiefZoqspGiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsbmz186mqZaBQK4gzXUX6oyzPKCBbMUmKJNYnM5UTvkomMUTH9icFnqQ4gnR8dvf7SpcPNduiFdCruyfFM9VRs1XXt60C37US0Hef1l9ZqZbVUeM1T5A_mPjypGPhBHuWvIiCVWCNbEDLG4m-tIdPCNGCzxECqy7zBmWeEH_mns7t_QNQrS5O8iCOfptLx4h2BgHP6KnlIW_GbZeqQRYvgG73ooQFAiY0t_O95i-lOwTWq3fopRTuv9w86k-o8VqMpzo9X0WnOTJhTMPJPb3yp1b33mH3cAvILz_t1M9MVzivZIsuib_ungyPuRZtzLo2GNuXP3A6pkW_Vqd_f72Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31236" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31235">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1sNDwAD3zQve35udSJQydO8f17W0CZDCQnavwD-XJlgwTpIQxxCkQlnMIioXafNM-m3_WrslCbtvC3ljMMT8k0ip_bwh8oQEkuxv_eXJj9kKJ_r2eMcxvgSG8G-7TY9ECwZQoHbJ_kCCbvG40ejX6f4_39Hky49RsO_QnBpekzI9aSUyEhq0ZPPfg1bzDA94YoWidKVmAbSYarRlyBSxNqOxQ93VxZXhnOKsTs-GgkWt2bRz0_0w8WuLKrsqNnWUS4fEvEbx7d0TlfSsFj7BTUHe746oYu-cN-3dRdChBHFodnBBS7zLmJZLn-AdXpONlksbOuKx8_HlbzIGx5fPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادجام‌های‌معتبر کریس‌رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31235" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31234">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuVhOHozvo4vlrV7FvM4_sqVD70LUTEdYS2cjoCk8-BTxcN3qBkRej9Z_FMKLS6m_MBlObpGyS8NjctfUKIb7vDY6pYPfiPJPsC38jhcKqCIkXHgNfPyRDKbsAt1owkILawkPu7CYEKCTbC2Y2aTTOi2GgI1Bc-zaNdWVK45FpRXmyJOnGdmH_ExNBA0KHOPdxkKC-3cqoelyKo5A9Ie0SJn-iOigX7K2H5gjUVaXFDfpsYOYS89V_9XQNLxlucMNgzhZPARVSxLA7Euqnhar51paOS_aKrO9gf9E4Z7M54ue-VUXspvMn2O2iVkoP6z7XMiefU7Gn830AzjRieuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
باگذشت‌دو روز ازبیانیه کریس رونالدو هنوز هیییچ بازیکنی از پرتغال این پست رو لایک نکرده!
‼️
این‌ویویو روببینید تامتوجه بشید که چرا کریس رونالدو اردوی تیم‌ملی پرتغال رو اون شب ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31234" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31233" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZeFKTI9KLu5mi99KnOof30mJA0WH2Ssu3c8GllqnpDP65p46N7UdEJX7xXkJl3sz0BUllKUi3fq76G-0W6A0kJZzjl5f_yjEinYc9i8Wae5iIcdqQ_O01cbz6kPkF3vpJAbcn8F44UCSaxQ3AQx0A6Eep-3CHQlksQGj5cVrbzJm1uJIXsZYCL4GFKn8cQ4iDzEFJ8tzWpqZTwtPH27i48xcKlsP9ftEyBBekwdRnRpI7OAhQk6t678zViOJS7JqOD53Iq4Ed-8TGyRfqjbvbZJ2e7214XthGz0p-xUHdla1NPRtahioDb6oD4XGavvEu4G1CmvA5G1VtGGwjvKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جاییکه پیش‌بینی فقط حدس نیست، شروعِ برد های واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌ن
ام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری مثل قهرمان‌ها
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع و بی‌دردسر
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته، همیشه پشتتیم.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!
🅰
r17
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31232" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG9bZn1saMpVmshqEtSDou6cU41eF51-vM9mDfVa1CfRIpoq5E1EDTwPa8_FEmzWrveMPY7ejNs46hZp_or3yWjJjIlztVJC5zODot3V9-b6wPLvHQtcVEKAODIUNws58pCewn_oYtK0X11niAKYRNACUKxWlZqx24UhNWwrhME6uHOR26McRDe1kNQlLfP9O3Y0KrTY1ZCZlgtkUtExKMv-rFPL0Co4cvO47mzDQxpnmVHJ9kG7qPwqaN8lHdMi5zxNY6RJIiu2Zg0V94WfCCqvA-dWwY4dofzT-m75xyVyGWkuYxTCe0Pbw1yejWUaOSALTwbZRjOalgHmlZ06CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31231" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPfcN95V7ywktdTHs7jAKChuuzSLGXn87C_EB0af_IlbcdxODr-cuNHMQ5mjm7uUqbM8K1F3eA7vu3TV5srSeE13gFZZKCsZ5GJm9XSTxVeNZdhC2-1uUfZc28rIPXnvJ68798MzjQdTLeCzPdOX6AqLIZaM4QOrypbzsVcJxQj21xHosmlc11o2lIgfdifxvBEtVICORm5jiltvn_udm-q2-zWDAXBv7zFZSZOnWn8_9piI5ZMCxHAFhAsqhy13OJHDvcPMnpWlUOD9juqpngf0zv1oK6oRJwTyLbwNBeRGBqaH4n8IyoS7ZEapF_fxTV1Np2TNJXrn0v_k-5lK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31230" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=cO0WK_X-TEKfI7sekjGFQbzKKWuhf09ez9zWOHsd2GHVChDE2KvT2w57CK1Ct-UPLelZtO3h-gzH8kp6K6MZWLy4R0iatB3Q8OXy5R2YXuCWwyaLYIWR_WbAMAwkrNaEQFpU5LO_AaCYsJGgS5Cq9Y3IUj_NW2WPVXn4b6Rbcq-MvB_nXFtNXUqDCHPUfTgkxOhBPMwON5XSTlyA814_3wrd2cLzrcivlfx_zouflFTv1sUOpD8cpwDA9eeM55rDqxAPaoAQ7MGPCsfHobz4ym7iUSCPIgtBd1uH7WefYLscgghWENhxFMFL-skTXW3vT8bmaUCo1EoVyhKgBwg80A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=cO0WK_X-TEKfI7sekjGFQbzKKWuhf09ez9zWOHsd2GHVChDE2KvT2w57CK1Ct-UPLelZtO3h-gzH8kp6K6MZWLy4R0iatB3Q8OXy5R2YXuCWwyaLYIWR_WbAMAwkrNaEQFpU5LO_AaCYsJGgS5Cq9Y3IUj_NW2WPVXn4b6Rbcq-MvB_nXFtNXUqDCHPUfTgkxOhBPMwON5XSTlyA814_3wrd2cLzrcivlfx_zouflFTv1sUOpD8cpwDA9eeM55rDqxAPaoAQ7MGPCsfHobz4ym7iUSCPIgtBd1uH7WefYLscgghWENhxFMFL-skTXW3vT8bmaUCo1EoVyhKgBwg80A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو: نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31229" target="_blank">📅 10:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31227">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBJG8VoGWtRArqggSkZ45sWqDP0LO4eKoLHVy7DqfUk1_hsnxOm7-qjY3zRg5-HFMxc0ONhFhA-1edP9oFnhmDNUAkpKU2O-DY0sux8e8z6yJjYSH0T7tW_V-Vl70_B8z3EeqRFKg994c_flr5j6XO_KiZWvisO-zZUxL3Q17U_lbdL0KzxSZXnjOLgto_pDdI2zi2KC3Z7VAqGxp9yjAgDJxukE0-9CnE-bbVs-cT1Tr0bZrs7GmsOCirnfRvLQ3y8JzVAyNr8rZGHssWKCaIsMkrJ0WZYMnnGlV9JT1hcKQsXocEQZicR4PRjtjHpmDthRgUnYRMFihltZPSA04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31227" target="_blank">📅 10:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31226">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgk7WrcmWjIinNKvNskTMy9Xmob4VleIPjgglD2fWxeq1s6KC4zCuDqIBhzk1PmxJ5WAz4SecVP__lWKeslxzk0kyOmMkJPlqBCwobfoKxK25zwMMPR86DLdeLftGdA1QoZD-Zrg9tt7lJBeAa-KcQVJLHaNvoS2CkNKn5NeU_mBUXSsueQSH3GY8YuTaqJj1gyPIT-2Gawwd1GaY5aJYVYB4JpbAy8MT1WWRSYdFh2lw21S5THN_oRIcATZRFh3DTEk4QbyEEJ3mubUCGF0vKNPa9psjxrfeLWipqh2m30SZhDDNSNb1oa4mdeVckdURhtOKVPUHANa-NgQg1uvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31226" target="_blank">📅 08:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31225">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcjesIShIhK8sdUCqphQuahEAbbPeNOikPurddx8cLM4cBiqWs919PVPmoUP9ntjMF7asA04xXxE_V2SGf0HKMcEgZU5Yjpvpj1Hsz9W8aUwTxTvGr8DWtQ6OvWkrSQ4g4gYhJGlQNZfD7pJNJ-zzkFY8TF0FelFFm6P9rjFFifrs9nAkUiy7lYig1-x1kupLLWJ3J79QPwcWL5B07chjODu--esxgMWGDQD4gFqc_SJci-aKJg4CWG9u2awATtvnhn5jtdnCW4MJwYFlsEQ_jzkS4SmfSV1weD8wDte3SgGkcDR_nfCOBoesP_Cx9OuHR5VO3P-B3Eqhk6ipmrRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از تساوی‌در نبرد استقلال و تراکتور تا آتش‌بازی سپاهان با درخشش حاج‌صفی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31225" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31224">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛تساوی‌شاگردان بختیاری زاده و نکونام در یادگار تبریز به کام پرسپولیس و سپاهان.
🔴
تراکتور تبریز
1️⃣
-
1️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31224" target="_blank">📅 01:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31223">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om6yiWgUfibJjwO_CEdCpLhq-_FNWEyN9679eby9waMcFmuLPtLsgTsGLdIpRJBeSgb0JofNLgiMR5X_Y6qjmf-izX-sMemkcITpvig-jLEcbCHDN_xqKU3c0WOjs5ZCp_W2wE-W8OnzeD7Va2Mf5a6c0sp0OGxDPE7GgEccOYgbVXswx4RYODDlXN7if3ZOh4oO8-U6Aw5pFWt3j-kG9ApjLb2exQH52NkL4-6wJ3YDNXjCvfB-bmexDt4NI6JoEp6OxJrpidKC2UzjLlYfMhuKIT5hRA9-qnvkX8XSFWaj2taA5yDoepSBn9edMMcMK8bYVYLl5P_Li8wZ4wvNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/31223" target="_blank">📅 00:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31222">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
علیرضا بیرانوند به‌دوستان‌نزدیک‌خودگفته تا تیر ماه سربازی‌اش به پایان میرسه و در نقل و انتقالات نیم فصل با قراردادی سه ساله استقلالی میشه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/31222" target="_blank">📅 00:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31221">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=Llk1z-LtjnV2iPxfDRARB8HyhQMswCSlr74_AyNPs_IXoPGMOT7ZTB9bgEKD_ee6HU5m9cEDy3iePS2Bb6c7pHKpVB4XbsMzDUuEtCTMkpMUqsgJPb21-gQGMy8vhHBqyDPSyxpZ8cTmE8-xxFPDpBL6YjEWWraOS6iWRLYKmq8iYDqVWlvfn_Jg47w9nFlxXbMpgfyXmer-snNeyTCJMoiGYfK3XlJMi6CPBhGRnYeZcfjN56Epizx6SYyaSPi3ugNqqEdfebamQiowN2vEbxJ2mSdA6tgeDc_4YI7g2jQyN8UNNtMFUXF3heFDAOdXMWRccTPv57X1IE4aCnHGCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=Llk1z-LtjnV2iPxfDRARB8HyhQMswCSlr74_AyNPs_IXoPGMOT7ZTB9bgEKD_ee6HU5m9cEDy3iePS2Bb6c7pHKpVB4XbsMzDUuEtCTMkpMUqsgJPb21-gQGMy8vhHBqyDPSyxpZ8cTmE8-xxFPDpBL6YjEWWraOS6iWRLYKmq8iYDqVWlvfn_Jg47w9nFlxXbMpgfyXmer-snNeyTCJMoiGYfK3XlJMi6CPBhGRnYeZcfjN56Epizx6SYyaSPi3ugNqqEdfebamQiowN2vEbxJ2mSdA6tgeDc_4YI7g2jQyN8UNNtMFUXF3heFDAOdXMWRccTPv57X1IE4aCnHGCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/31221" target="_blank">📅 00:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31220">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqY-a411e4Qu25VENqPZAXbwoJhlzeuoxyfJZBUpbxzi00oqHUMtVQbIO17q9l8sdTCDq7oRlWB6o6SiDs2nxpnvCYZwflMTVU83aZxOIhsZVZDvUPg-65WwhXvJKN-ujf3iquQqS7r4p1cAmBKoWbiroX5hib58j9-ca3Cuu3UIOruglgeSzPi8EXcNMGOGWforbapZrzf7gP_qhyvVIrpgzDZFwORNhGc0LYPRLcDtJ9HZBjqeapy2GpwQZQHCDqeBnStMvBm69o066MHQLm1u3BRb2BWxc5t_-uty_0bnUvQGrsmcTuf-LTqQgcP0NjjF38PLLg_H0cyX5djWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/31220" target="_blank">📅 23:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31219">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU0X1cZbB9qExMp0Rdjv9MeGqGSUgUeb63TRFZynxTRis__D5gyexoXZNbP-GMhCM-xf99JrRcw68Z4CPqSGJJaEg740E54jCDL6MDHoeyOunWhki6fmFuBA62HSQSHwcgAgrFzI5A_u7TCuY3JYB6tV3AVEGpT4m2UE6FCRN07w_9FVhas_Gcbd4Q2nVidMzF4zqUhSeWYNcvdTPfswDNGM91wr9Je-f-Q3NbqBI6_aWr7eo1JS6aZ8DHR1nmSMbEMzYxn4vtMAADyYZ_Ovf3gkd-dwGNdNjcNaZ5Fk9Aq9nEh2XI0HQyD6RILV8YLZkak9DFTp4ALMaFZ5uEbcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شجاع خلیل‌زاده بیرانوند رو آنفالو کرده و از همه بازیکنان خواسته‌که‌این‌بازیکن رو آنفالو کنند. بیرو بعد بازی بااستقلال گفته تصمیم نهایی‌ام رو برای پیوستن به این تیم در پایان خدمت سربازی ام گرفته ام.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/31219" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31218">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qkjse-tIrp2LpTJKiyDs-BxWYidk51EOAmPS9cr5BqQtzKjX9cuI2W9E947cYmP0_v7RcqS7A7X_CuH7wyXzN6zrsDkm7y_IDxZ_bXBnbjpHxGEirnMW5R_PYUJiMnDwdYlcGNkewbdde_wCJZKMmfoLXddXAsjBqf5TuL-Hun9Yhm7NGxggKf7H91X749mzmlTFLpFTVAO2zJ96Q3dcvKjk9zhIG_W25fajhbfhjUiUZf5mj99YyF3ZM7IQLAHRi67z6Ux9_wcDtBGsEJlOATf18eTkyF-qA4xX-rmPH15HT4ONQO6qUVeq9tVuPzAmnkH9OxX7aDs8k41nH5li4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت
؛
کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/31218" target="_blank">📅 23:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31217">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=uAvNJ65g_98rkx4ElJrslWS1gVnGolX4CTu7hBvk8q7n0TVdB5DPyStsaytG1l9sKfDhfa39xUeZX6r_hEADus_HSshOY7jUi9u84KaDjDIRGrgSBb3qcH8muFVBo5TmC9DCCj_z8WlnF0PyRHq-IYNx7sG1I76LGFl6GpTglOV348IDoZKbYwchDIL3Td-6l4qsJwGf0o1SvVVr3KijLAFGTwv08AlIAg359rP2NWAzGf2UNe333Btb0FGQCOp7jptUkiz_mYV24NigKewaEWwhaqzGCBiwS2s9gvUUg2GNCeDr8_tJOA_YprWkUgYD_mfWSG6ko_Wb7OVfyjody0hVt0OUOv-uNmV_c9SXG0pWJFYNkr-0LDuONtxtyhaFI9hCHPv6AzUVR56CqzCRS6ZgD7JnZM324JiTY6vDigC-NmJ6qM62RwXMrPfSuz9vbLc4rW6_WyWFYr2z_BWKdXWLJXIrMknvIei-NglHdv-LdV27IEc8QXHWJu7Hra0_xiaqmndJmcQFwdfcoDnGgaRQb2XBUBcR1mWjvSq2XtTluNK0m1-_c2Puf3vbdGAHfqATT9808VOB2KuH40NdBboxG0qieoErml0NkqmKBgv_OU1YUXP_J7aFLtNHRAAv7DAtJPkSkL6XnUsbD-NOoIXqQ36IpcdNL1xpJGJzMvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=uAvNJ65g_98rkx4ElJrslWS1gVnGolX4CTu7hBvk8q7n0TVdB5DPyStsaytG1l9sKfDhfa39xUeZX6r_hEADus_HSshOY7jUi9u84KaDjDIRGrgSBb3qcH8muFVBo5TmC9DCCj_z8WlnF0PyRHq-IYNx7sG1I76LGFl6GpTglOV348IDoZKbYwchDIL3Td-6l4qsJwGf0o1SvVVr3KijLAFGTwv08AlIAg359rP2NWAzGf2UNe333Btb0FGQCOp7jptUkiz_mYV24NigKewaEWwhaqzGCBiwS2s9gvUUg2GNCeDr8_tJOA_YprWkUgYD_mfWSG6ko_Wb7OVfyjody0hVt0OUOv-uNmV_c9SXG0pWJFYNkr-0LDuONtxtyhaFI9hCHPv6AzUVR56CqzCRS6ZgD7JnZM324JiTY6vDigC-NmJ6qM62RwXMrPfSuz9vbLc4rW6_WyWFYr2z_BWKdXWLJXIrMknvIei-NglHdv-LdV27IEc8QXHWJu7Hra0_xiaqmndJmcQFwdfcoDnGgaRQb2XBUBcR1mWjvSq2XtTluNK0m1-_c2Puf3vbdGAHfqATT9808VOB2KuH40NdBboxG0qieoErml0NkqmKBgv_OU1YUXP_J7aFLtNHRAAv7DAtJPkSkL6XnUsbD-NOoIXqQ36IpcdNL1xpJGJzMvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول رده‌بندی لیگ برتر در پایان مسابقات امروز؛ تقابل حساس فردا پرسپولیس مقابل صنعت نفت آبادان در هفته هشتم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/31217" target="_blank">📅 22:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31216">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe2dSzLOn-RIOyMfhtjFTB8BH3o7hT76plWQV_nBMni7IPFpOUh9lJwk2zt4DdWAQ-H7xVcBnzv4CiaahczRjjcRVpElZ3hXVJKHhB31mOjr4acIjFLqAIoEJnM9N5puttEk0kmhBtXZPG6N5UEsID1BJRwO24NPOItvSnk49qbLrx4XgLhN3AwoKYICPFfWKkaRd37Js6cKaohzqff4yBtVevo5_qAsjmBr7Pl6QPYjOEB9VL5Nn0k_ue6_qJo0OMAt3fFV_7E_W36a-BPoDmLGmifLPnU3vnzeGEYDkVtIwqJjYajbsUyCmOPwBedTkLxf1lbiMbACXOFjqTdV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31216" target="_blank">📅 22:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31215">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctNdIKfpu4XXM4ktvV0dBTkBftc27eTgNCnBlv9J7kJOPEEHxLMldCYYgzTRMLVKHlScruvY9Qaz-dexSwvvKFmTEkwyXBEX7E4hrZdXYFE16ZJF2T6ODg9KmtEk3O4A-Tbc9XiTqcuQDhg5bMMe1D4i_Q8Slizs4xGvy9dc4pcbjRkr2n_l9gd0B9O7y65ScUumK5bV-NIwpoM7TcfW6jOlXaIrH2L7r64BMwXf5GsvNmltrbpqECO-bOpmwSZc2FMmNH2vkoRsoEglVuVISWyWHmhw2xp5DzZShuLOQWzYv5X9zPodA2uZsq-4l4Xug_PzDx-SHonzC4cSrLjGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت ستاره 19 ساله تیم بارسلونا قرار دادش رو تا سال 2030 با آبی اناری‌ ها تمدید کرد. اسپارت قابلیت بازی درچهارپست مختلف رو داره و در واقع آچر فرانسه جوان تیم هانسی فلیک است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31215" target="_blank">📅 22:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31214">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEJEY9kbNeEp95aFoFY8FBaKvtq2SjQXa098bVqCIL76lRcfrECB80mh5hZ0YGcFXM8-l9JdKxXYa5SlmB4L_FmurqpyRljWz62cOY0EOotz3Vreyu03sPamNGiz7F50grpn6_d8AKWRZUblC6b2_-3ykS353O_AKAPScr_mrWC9gwTkokTMP9AygPTUH_99ZoXxXSvEPaOhOSclw9a_CVi5gR0uz9wO4mJV4AH5nDyy-NSJKebxOD3KkO3keaw9rYKG6Tdnsvm840ivJ2tv8z9Dler6nJUbN298C0Knr00dTRx2FwqEa5rG24YUhLiYIHx_Aq-PjvBjjIHBlMA_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31214" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31213">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=cKpd3-uVZ38T0UhJSAoKAI6Qjtxb1rri-ZYuxShhXHpIvm16YJdWAXAPZBeqam2_b-CLYz1U7UEUlFgcYK_6P8EcmPlp_p2xDr_LOwQYut_dH93-qEdi4E7FsbM5H-wdbo0I0xutGJRp0f85AvoaItvklTVfJnLBSqe9PER1PLi96-ZhVTMHWx5eiKWY9M6GYhu4hwLB-mr693zpbAuH2FcL_6jXR1R0C8m2tncE338lT5xJVfGvKJc_dre9qBPzMQxsg3US3ly_iZtoHEH4_X1F9D0Tso6TOATqikdRd3kDiuS2gjmr39lgfuyTjU7Q_5bTYEGjBWaVQHCuJcNqMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=cKpd3-uVZ38T0UhJSAoKAI6Qjtxb1rri-ZYuxShhXHpIvm16YJdWAXAPZBeqam2_b-CLYz1U7UEUlFgcYK_6P8EcmPlp_p2xDr_LOwQYut_dH93-qEdi4E7FsbM5H-wdbo0I0xutGJRp0f85AvoaItvklTVfJnLBSqe9PER1PLi96-ZhVTMHWx5eiKWY9M6GYhu4hwLB-mr693zpbAuH2FcL_6jXR1R0C8m2tncE338lT5xJVfGvKJc_dre9qBPzMQxsg3US3ly_iZtoHEH4_X1F9D0Tso6TOATqikdRd3kDiuS2gjmr39lgfuyTjU7Q_5bTYEGjBWaVQHCuJcNqMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/31213" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31212">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDdL6M6C4zwqbnRDPD56TV0CpLyZmQGn-oY8PKM0aBWm_WCNgqMca6cj2FxTVCiJHi4PMYZ7iuG4LkCSCkZXS3QVfUuhpPp0DstpQ60v7At-DwHXlp3nGA2pWVZqaJjgo4C3dOYQT46MwhNPaIacy53JwgDQQU5nSpJjB8wq9qpO9LqafYmVMmHgAil77xbXIyDPVve66JrH6QZRCucjCGeGcrUnhoZCccwp9S4Xglyemoz3Z1ZHcinJekX3u6hLPadxQBp9xmZePQZ45RzrmonQXZvwC5N7dcqM1MbXdUfEz751pZEQH_MRgZdXqZTFoPFcfnCodX1HuOek7-SrHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
واکنش‌ علیرضا بیرانوند به احتمال حضورش در استقلال: استقلال تیم بزرگیه. من یک تصمیمی گرفته ام و 100 درصد روی تصمیم هم هستم. من نیم فصل سرباز هستم و بعد از نیم فصل بازیکن آزاد هستم و تصمیمی خواهم گرفت که به آینده ام کمک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/31212" target="_blank">📅 21:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31211">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/31211" target="_blank">📅 21:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31209">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CitCbsDX2M4-wad8k6TAW3786XgONLPN70obJ9Y8fsvS1uEfD_3R6B_VDJkA1P1A5XKG_h0SesPr7yeIKkFzGVmgB-5duLSjw4ReTEbCOyann8twHDd53Ly3nsVGuCW3cfm8_PMXaNEBNIbeVZDv9Zl0VLmLZExU6Y1tb69PdSe7n3hwMJb9hJVko6uTSfXmu0SwFWrtzNWndNiBxeHnxGsI9a8O_YTrZiuDIoX3N9WOhnxrB1g5Rx2S7Bip3-gfoaET6y_2b1kk0Q2waxm160i2R88_TbhcDN_akFTPiZVLCXbAkC5UumL49FjljNNg0RFHFoSVp29B8LL3tOoc-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdpMtLXpd5gadqHLBHyRISeRgZIKbycx7CPph5rVoCu58rMHm3qCIughBhmJ4SBuJIYAn_mhzIUM63I1Tcjb7LzUL_wmb4NBu31GwgpWQSh59E70V1kZ8Se2955B9-KTu3BHkeut1zuw9OErbIv07-1zf-HBud25EeBAnSaERMpicUXN0hO2gnkSMzA47VkypdfE_beRJdOXoB7cK-5zwMQIi8oqemXVjscyj4wbSSYtrTvf61o511zRJ8WxxqFLeIDeJON27EuskP3udUOdpaAL71yFXrXcfpxLDWG46Q0ZNIMJvFy22qaZZTmer1U3Jq8niWF3W-LuVwbVxLBKMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
گل پنجم و ششم سپاهان اصفهان به فجرسپاسی توسط مهدی لیموچی و آریا شفیع دوست؛ هر دو گل خوشکل و تماشایی زده شد جفتشون رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31209" target="_blank">📅 21:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31208">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=iR04aSmRkwB-llwhi9bsuOlKsMElGablkhvULNXS2lI5TXur2wHgU10zNw34d2Qwgb_o0q_aTVsGhcll8bh7zkMVVlePZdkUkmMATHkz4BMfQMhh7kXssAwx5TJ2bec6Kte3Z3kNtcDFlEKn5k8fVgxUX82H-m2AIt2pko19dHaWzQ9tIhIscfExJqXIJFpmpCqpwP-o2EysE77IbZND5B4SQg0D6bisMy5JbCHeUe5SLBbl7-CufAA6255caB-rnytzXlDp5EPlBRFrHBQAa_ElyTQJfhxyCZ4dQ7MC-xXDIYaL9j3RJlrtIJh87tEwfVB84oVLO_o2QdqA_e0-naEBs4M6dUY9Qq_xsnp2P2D0tCJ-TATe16FQUqlLYuLxWU_pAsk6oy5KHrohlSFbxjnsMqy_nLrbaX2ynGeaN4G2ZP-HTH6e_fdnw1iCjQvP1BfcY1MTahabqRF92BTyJYfSBfkKJ6mz54AEBMiBxdWj53i6U3T02dv64XImgxfaEvbEK-0rECEmNHJUElKebh491NGt4EGmMkbyD78l7wq4bUsC3pwd68YwWsFraiUIO59G9cvvrqCA9kqE56F2GI3W_xQmdD1r1sCtr1PTqteVU4_wNqG9emu8U_dTW40fKLE5Ob6jndFacSOtIuUpnFaBrUuoG7pKI4SGPH2Bvuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=iR04aSmRkwB-llwhi9bsuOlKsMElGablkhvULNXS2lI5TXur2wHgU10zNw34d2Qwgb_o0q_aTVsGhcll8bh7zkMVVlePZdkUkmMATHkz4BMfQMhh7kXssAwx5TJ2bec6Kte3Z3kNtcDFlEKn5k8fVgxUX82H-m2AIt2pko19dHaWzQ9tIhIscfExJqXIJFpmpCqpwP-o2EysE77IbZND5B4SQg0D6bisMy5JbCHeUe5SLBbl7-CufAA6255caB-rnytzXlDp5EPlBRFrHBQAa_ElyTQJfhxyCZ4dQ7MC-xXDIYaL9j3RJlrtIJh87tEwfVB84oVLO_o2QdqA_e0-naEBs4M6dUY9Qq_xsnp2P2D0tCJ-TATe16FQUqlLYuLxWU_pAsk6oy5KHrohlSFbxjnsMqy_nLrbaX2ynGeaN4G2ZP-HTH6e_fdnw1iCjQvP1BfcY1MTahabqRF92BTyJYfSBfkKJ6mz54AEBMiBxdWj53i6U3T02dv64XImgxfaEvbEK-0rECEmNHJUElKebh491NGt4EGmMkbyD78l7wq4bUsC3pwd68YwWsFraiUIO59G9cvvrqCA9kqE56F2GI3W_xQmdD1r1sCtr1PTqteVU4_wNqG9emu8U_dTW40fKLE5Ob6jndFacSOtIuUpnFaBrUuoG7pKI4SGPH2Bvuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31208" target="_blank">📅 20:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31207">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=PagvIzZ7cB4UIkIpkodqvOXIZIqcEtzAXXJKTP1sGVKbRr4e7v8d_-ACIM-v3p6BCG89BoU7rzbhF-fUpBs3D7RhSjNfxe0HCYiSFhOoXbbsZWTqvBWIghDZbnp2uQ7H10buPczXP-fTnVpOEt5x8t7_S3QjolJaS9V2BVpro6dAlKnTFHGk7d3GoyLmf3OARi0mrAsWu_jNi_PRJYEQe0U4voF9PznYT39-Nd55da0-4VdnCxWBDHo9znr1SKGZc1-q69WR8egoTLsxIB7otVoIJCAg8NuEOFDyVzQaO3K9-RqAPdzT9zb6XX8czLmndwJgbk2_VGkVvdCxtgj0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=PagvIzZ7cB4UIkIpkodqvOXIZIqcEtzAXXJKTP1sGVKbRr4e7v8d_-ACIM-v3p6BCG89BoU7rzbhF-fUpBs3D7RhSjNfxe0HCYiSFhOoXbbsZWTqvBWIghDZbnp2uQ7H10buPczXP-fTnVpOEt5x8t7_S3QjolJaS9V2BVpro6dAlKnTFHGk7d3GoyLmf3OARi0mrAsWu_jNi_PRJYEQe0U4voF9PznYT39-Nd55da0-4VdnCxWBDHo9znr1SKGZc1-q69WR8egoTLsxIB7otVoIJCAg8NuEOFDyVzQaO3K9-RqAPdzT9zb6XX8czLmndwJgbk2_VGkVvdCxtgj0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31207" target="_blank">📅 20:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31206">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP_7yZZ7iurYdRVKUft_IJZdGt5uBMDsiirS7RsNXiGM-6GBwHRU0b2Qb3x69uMRhlfyjXTXIeZViMc57nNYx3s8tWi2R5gVmMJSIXyg9reWjeULGW8fM3m6NFfRYNpsejv7a3vrcOsXY4y7PQrrifRReHRo3khhxtJ4zwep-3_j3WPpS6bTt2unN2qkwotc3wN8vHhSckbKKoTJOhvv8Gmda8PNtpLnmi7TfVuK_izOH9czDv1D_u_xRzmMbLcplKp_7mrm9QCZJRySlm12dJuCFo3OPyC9ezSJmT7J4WBfE1TgUOhnbqdQQqQsEnSPfgA1yWUdn6koGKZIIUIp2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دونالدترامپ رسمااعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31206" target="_blank">📅 20:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31205">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=MOWi3CBXOq0jro2RSRa01eIExHV8Athm6e7LBqOYR4HAycZtA0PLjE6TjzGBKVlfBrXHarJE60pgLgq-ZPHVn6XNh7EfAUqYpXq7yhPK4kmHgr75oHbKIxnzUply2IhbHyI6NstRWcZBrwuI_N9AlO7rT_D2iUy8ggg71ePmst2QZV-xZGVKMoegQWuoM8UqrrIO01eP7tF8TnyrUXbx9kr7jbT35ZoZjT1qOy3xwc1FyUkH5b5TgCYUBBi8j0zKlLolRZ2FYuA6XGx2HJy6qS1iPLc5BXPDSFAlBBxn_p1TeQPoJ2YHRuRx60ZBUb1pcjl_pqXfTImXdMLoSu-v7JnGPupHeKEuN2ECkYlG8QRT1p61eEMKnep15AaOlMqAVaA1fDwfDAhVS5nYEpTZplZYPa_mNeBmZVQ_QsK17rxPB5mPHF5cxBbg0XNBq2d7vK6mDM4X37-luqqga7I4TKJn6QOF0uqp8Z7nJR-uiO-lWhb64DtAatIQ8c2sIN1btjXcTflzyxTslDXGRc2Z4rxu5zltm_6ybUYcfEvCT-IDofSRwwwUGNSHaLIfZRhtxbch0u5xhfdRBFNlvzKOVb0827WZuANC8sME6WNQVVol0bPtX2aIAGpCL7p_uQoPMmFBzrk8LjxcnGg4-QIBpiW5QYZm5c23NO0w_ZvEKCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=MOWi3CBXOq0jro2RSRa01eIExHV8Athm6e7LBqOYR4HAycZtA0PLjE6TjzGBKVlfBrXHarJE60pgLgq-ZPHVn6XNh7EfAUqYpXq7yhPK4kmHgr75oHbKIxnzUply2IhbHyI6NstRWcZBrwuI_N9AlO7rT_D2iUy8ggg71ePmst2QZV-xZGVKMoegQWuoM8UqrrIO01eP7tF8TnyrUXbx9kr7jbT35ZoZjT1qOy3xwc1FyUkH5b5TgCYUBBi8j0zKlLolRZ2FYuA6XGx2HJy6qS1iPLc5BXPDSFAlBBxn_p1TeQPoJ2YHRuRx60ZBUb1pcjl_pqXfTImXdMLoSu-v7JnGPupHeKEuN2ECkYlG8QRT1p61eEMKnep15AaOlMqAVaA1fDwfDAhVS5nYEpTZplZYPa_mNeBmZVQ_QsK17rxPB5mPHF5cxBbg0XNBq2d7vK6mDM4X37-luqqga7I4TKJn6QOF0uqp8Z7nJR-uiO-lWhb64DtAatIQ8c2sIN1btjXcTflzyxTslDXGRc2Z4rxu5zltm_6ybUYcfEvCT-IDofSRwwwUGNSHaLIfZRhtxbch0u5xhfdRBFNlvzKOVb0827WZuANC8sME6WNQVVol0bPtX2aIAGpCL7p_uQoPMmFBzrk8LjxcnGg4-QIBpiW5QYZm5c23NO0w_ZvEKCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
یادگار رستمی ستاره 21 ساله فجرسپاسی به این شکل از پشت محوطه جریمه روی یک شوت تماشایی دروازه سید حسین حسینی و سپاهان رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31205" target="_blank">📅 20:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31204">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=pnQOcXxpcFeuPjBVcfOgnFhPy0z1uYbKJfvUsYQ1y8ar4xr64d_ZvCd2R0BzObHeghlgAPjRc5ko16pzTB9LV3-jpPUwsvCGoJOBC__vPbj-hQ2S9hEbCCoPAFCWDtlZRwX_iEYrVwvlrk_QXMb12WKacnHQkcYPm6yWqvgK765ZHxNZupxBNhFf-oPKhVvI596oPueTw3lWtx1bH53RtZgtrxJHPdix8VET4kqoOwzzzN5MZB1EbrQnxezGLRgvuq2WcvF6Hcau_mxorG03oTyUlhDTl_FcGecIIrdVLAKZgs8cxGxZGAHrUUPLbwhh-lzt1NS9ZAZZBsh-UHKNjh3YhSkNS8kEiemLRoF8q3PBuEDBUWSHb4LCyHSk8PXZBT-LbttYooCjeYzXEupD4lvQj1Y344bIQ1AwspY4ILCTbGD3LiSYixf-4-k5-S5wZ0IGxW4cxUq4k2n3WP0xB1tcMeJbkvqoaMEEH2lX-KJumX6SHHm7V3v3d-Y6uOUh3PDJ55QNYT2KHV2ex2VNZ14MiSEDPXTBidTVLS7JMFKzTSk24kYIBhnNg_l-0C-_fqj3JD9jonBfUyqSI7oEXFB-5qHwoRNCaLEuPpU9TJqNNvaDEywTICcQClb21WuH4zUyq4W_ANMtY3gEsfVFYEnjCche5HD0ulmwzZltj04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=pnQOcXxpcFeuPjBVcfOgnFhPy0z1uYbKJfvUsYQ1y8ar4xr64d_ZvCd2R0BzObHeghlgAPjRc5ko16pzTB9LV3-jpPUwsvCGoJOBC__vPbj-hQ2S9hEbCCoPAFCWDtlZRwX_iEYrVwvlrk_QXMb12WKacnHQkcYPm6yWqvgK765ZHxNZupxBNhFf-oPKhVvI596oPueTw3lWtx1bH53RtZgtrxJHPdix8VET4kqoOwzzzN5MZB1EbrQnxezGLRgvuq2WcvF6Hcau_mxorG03oTyUlhDTl_FcGecIIrdVLAKZgs8cxGxZGAHrUUPLbwhh-lzt1NS9ZAZZBsh-UHKNjh3YhSkNS8kEiemLRoF8q3PBuEDBUWSHb4LCyHSk8PXZBT-LbttYooCjeYzXEupD4lvQj1Y344bIQ1AwspY4ILCTbGD3LiSYixf-4-k5-S5wZ0IGxW4cxUq4k2n3WP0xB1tcMeJbkvqoaMEEH2lX-KJumX6SHHm7V3v3d-Y6uOUh3PDJ55QNYT2KHV2ex2VNZ14MiSEDPXTBidTVLS7JMFKzTSk24kYIBhnNg_l-0C-_fqj3JD9jonBfUyqSI7oEXFB-5qHwoRNCaLEuPpU9TJqNNvaDEywTICcQClb21WuH4zUyq4W_ANMtY3gEsfVFYEnjCche5HD0ulmwzZltj04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ویدیویی زیبا و دقیق از آنالیز بارسلونا مدل هانسی فلیک در فصل جدید رقابتای لالیگا و UCL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31204" target="_blank">📅 20:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31203">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=TMCdoBQse4VWoQ99zwL7H9vE3_PcDJrBK-xgD2cynv-dLQoAYVORQsZPKhDvC_YDH8nvdDKkuEUR5bgDnIhWdOknRTSTJ29HiBCwPAPFcIQmIw_Ek-J2XIlO-Wu_RWKIKR9n3f-tlME3WMU7hG1nx2uIJwY6XIsveDW8OwnCBGxFEZn6K9e_t-bWNoNqqH8tUtf2uamG-d0dEq_K9Kl7GWh5iT1AxYyHAnnpj8fxiVeYKVff4lYWtF1qXMaXUlOr7KC_tWTJiB_ortyoN_SBPQ1QYCJdaLVWErqomt1n3JUuwbzVvz-S2P1-9GVxaOfbVWcOFXnWd8vbiONjgiy3bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=TMCdoBQse4VWoQ99zwL7H9vE3_PcDJrBK-xgD2cynv-dLQoAYVORQsZPKhDvC_YDH8nvdDKkuEUR5bgDnIhWdOknRTSTJ29HiBCwPAPFcIQmIw_Ek-J2XIlO-Wu_RWKIKR9n3f-tlME3WMU7hG1nx2uIJwY6XIsveDW8OwnCBGxFEZn6K9e_t-bWNoNqqH8tUtf2uamG-d0dEq_K9Kl7GWh5iT1AxYyHAnnpj8fxiVeYKVff4lYWtF1qXMaXUlOr7KC_tWTJiB_ortyoN_SBPQ1QYCJdaLVWErqomt1n3JUuwbzVvz-S2P1-9GVxaOfbVWcOFXnWd8vbiONjgiy3bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دوم‌سپاهان‌به‌فجرسپاسی‌روی‌شوت دیدنی احسان حاج صفی کاپیتان طلایی پوشان دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31203" target="_blank">📅 19:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31202">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVzM7WZPO__FU6CZ91mUpupDx9rOyQNm0aq8aa_bkBH8jBIbp-yiR-UlqfQJaohKFf-0kp2WtB5kv9YLmXhjWylbXcxgwNjKkM6_MLNCfZ-ibmPn99Ued1dMY_VIPbmkU4wCbJPHpCOy3KtlfvFQdanIoq1i3zPtnjyLuhgaADusQ8lVbhN9sGstJhnZIUZnRJXeQqpcZRHwtI9cqNRyOkhkctB3iyLzy0sHBHTnx4hwcifDxuzhUNNrYEr3qwVKfbuNnEDkBhKNLKf43ltJHexJRkWjO3xTE5O5kkm6zgN5t0aSWX9Z-J_EAuFUim57RrWmOGM0ZPzE3qYMcT9MNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خرافات جواب داد؟! یاسر آسانی ستاره آلبانیایی تیم استقلال به دلیل مصدومیت در نیمه اول دیدار با تیم‌تراکتور دربین دونیمه تعویض شد. آسانی چند روز پیش با حضور در برنامه عادل با او گفتگویی داشت.
‼️
پیش‌تر نیز عباس‌کهریزی، پوریاپورعلی دو بازیکن  آلومینیوم و پرسپولیس‌نیزدچار…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31202" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31201">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194218a84f.mp4?token=IYl31-NuyFx90bS3E27KdSSbtOh5BIHxVxjwHyHp25ixAnY0EiRAg0tsnY-a4XMJHkQd_3v-Zms73_WiJ-0gjwUxMp3RPvqRO1Notv0f9LjDpgcVnOedwCLab3BsVZImkZ9DiVo7AU1G5JUH0xhB3rDSZG0OYJfGkaTU6eRnmUx0GTCZgBMHfOSkVbhKSHJuKqv1XOfXEXGZPoeOQ0Y16_bvh0YaE6UpDyGaHCHkDVVhQYnWgFIuCCcxIAdsZk2HdiFWQdS4cr_gHX9ugTyeyvhGUvJlKuHnS-66-G0AcpQX-ZidvetZ_JoNfvz10iRtdQlQEUaACkorQV9d8hrgvbRJzH6ephL25wLlOrLMv6frNNNqPQvWhUCzB7muvium79ak-wEWxohKCSMHUHKpfeYJUEc-48AFF8e5HN_TmMqWFWQR4l4DyyLKd9F3rJbFFsjt3SFI-vMGijrRdstrr1w_vpVmqFvKsGPI2ONpR2wuB8mkcPk9sD8BGLNFvSixNvvW-xS88mXUbU0aQ8wlZYip37mUpQ-RPQoS4inDSDcJFWDCAZWMCB7q3cuJxrH5vTHWPl4uE_vjl7WN5dRbo47HkAe7d4V8aMKrNKgAHBnpHPF6VK3OIrlztUhVuGPvlodNQ_Og1SZ_rz_tabTUnKxvxlL4fds8yK3njZg3NaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194218a84f.mp4?token=IYl31-NuyFx90bS3E27KdSSbtOh5BIHxVxjwHyHp25ixAnY0EiRAg0tsnY-a4XMJHkQd_3v-Zms73_WiJ-0gjwUxMp3RPvqRO1Notv0f9LjDpgcVnOedwCLab3BsVZImkZ9DiVo7AU1G5JUH0xhB3rDSZG0OYJfGkaTU6eRnmUx0GTCZgBMHfOSkVbhKSHJuKqv1XOfXEXGZPoeOQ0Y16_bvh0YaE6UpDyGaHCHkDVVhQYnWgFIuCCcxIAdsZk2HdiFWQdS4cr_gHX9ugTyeyvhGUvJlKuHnS-66-G0AcpQX-ZidvetZ_JoNfvz10iRtdQlQEUaACkorQV9d8hrgvbRJzH6ephL25wLlOrLMv6frNNNqPQvWhUCzB7muvium79ak-wEWxohKCSMHUHKpfeYJUEc-48AFF8e5HN_TmMqWFWQR4l4DyyLKd9F3rJbFFsjt3SFI-vMGijrRdstrr1w_vpVmqFvKsGPI2ONpR2wuB8mkcPk9sD8BGLNFvSixNvvW-xS88mXUbU0aQ8wlZYip37mUpQ-RPQoS4inDSDcJFWDCAZWMCB7q3cuJxrH5vTHWPl4uE_vjl7WN5dRbo47HkAe7d4V8aMKrNKgAHBnpHPF6VK3OIrlztUhVuGPvlodNQ_Og1SZ_rz_tabTUnKxvxlL4fds8yK3njZg3NaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آریایوسفی ستاره‌سپاهان به این شکل گل اول طلایی‌پوشان‌زاینده‌رود وارد دروازه فجر سپاسی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31201" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31200">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=Ic-ET1NOxql5LZ0Oq-I1VlaVRKlb2h7Pnbhgf5mqSycxVLBfxoxvtanGtobZS31KER1Aa--_cfS4JQH2fpwZjYvJGd_vMR0_c1Ov4DFMdpUvqeLIlo_axfvm8yM5NF2xzCLrxcbhp7YyLBFnLe0FiSqDCajfSu-BH207fzkSjaeL6iXsJd9iBwRW8hMl7Kp_eaStxQB4qrjixTAmt-UAUWOti766FRL9jGQeBGtUMxfqhqLwCmen0OI7-doBV9TM8RM7JnhwT3hA6ahMk5miJ_rL4Ay0_K8cRDSyRRxdU4fFTC035PwZfyx5eBU9aYrg3xysEy7OMz7HO3G6OLzTLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=Ic-ET1NOxql5LZ0Oq-I1VlaVRKlb2h7Pnbhgf5mqSycxVLBfxoxvtanGtobZS31KER1Aa--_cfS4JQH2fpwZjYvJGd_vMR0_c1Ov4DFMdpUvqeLIlo_axfvm8yM5NF2xzCLrxcbhp7YyLBFnLe0FiSqDCajfSu-BH207fzkSjaeL6iXsJd9iBwRW8hMl7Kp_eaStxQB4qrjixTAmt-UAUWOti766FRL9jGQeBGtUMxfqhqLwCmen0OI7-doBV9TM8RM7JnhwT3hA6ahMk5miJ_rL4Ay0_K8cRDSyRRxdU4fFTC035PwZfyx5eBU9aYrg3xysEy7OMz7HO3G6OLzTLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31200" target="_blank">📅 19:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31199">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJn0NENF7msvfkvehp5j4JiFoSbTNU97-jYuP8IKu0YGyu-sYZW8wtal6AowFr_S_K803JU-piU-S0T3E0Pht711wAH54AHkRObwJtPEQYIE8Y1dYqLPm5NCFrPJkRr45H90QMdmkGbdkinBZSvbmTEwRJxNEjDjgS2tc_e4LFSbUJ_7ENy-jLog_KK8MFJ521NKcIcGxG77eHZHAv0Sru3uL4mGkoUq_kL7m7RoMeFL-HnyCJdWis4e1KAkAdAiS788Q6-iS8TrjRwaW9piDhXzlkMS1SAlLqlRCrWL9Yt21fpUp_u3lcYIQRz9uw_uzr6SIHNR9RuL1yZkSi1o9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بالاخره آبی‌ها گل رو خوردند؛ گل اول تراکتور به استقلال توسط سید مهدی حسینی در دقیقه 74.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31199" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=bO8XocFJUa2hlrXbnA1kxwGjtmT_wNXJlPLCzmOId5gQUtPyHgqtG36669T1H1jksXNxkSAhKDXkvhTOjpQBT-aP5aLkrXu954dsOCPzda3He1I-gFnVJQA_jIOETg4xAmA2i7KHuPViRm-1IzYmhmCSmepTyCE2hcMrW0tfVIu9ZpxkzNhYAlb3viEh7hmpwYfyMqFzyIVA2-Vnh_AXq1ZAxFbRbeF1DUJn3HArW42rT1OAuKZj4o7A86DzJAXsG8qsr-HP3lZ0NunmDGXM3TOw7jvKBT2P1AXMyP9pAsEBqLF4c697-zomWA2L4Ml7bHmA6dm-O2bTcEesRoNUPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=bO8XocFJUa2hlrXbnA1kxwGjtmT_wNXJlPLCzmOId5gQUtPyHgqtG36669T1H1jksXNxkSAhKDXkvhTOjpQBT-aP5aLkrXu954dsOCPzda3He1I-gFnVJQA_jIOETg4xAmA2i7KHuPViRm-1IzYmhmCSmepTyCE2hcMrW0tfVIu9ZpxkzNhYAlb3viEh7hmpwYfyMqFzyIVA2-Vnh_AXq1ZAxFbRbeF1DUJn3HArW42rT1OAuKZj4o7A86DzJAXsG8qsr-HP3lZ0NunmDGXM3TOw7jvKBT2P1AXMyP9pAsEBqLF4c697-zomWA2L4Ml7bHmA6dm-O2bTcEesRoNUPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول تراکتور به استقلال توسط هلیلیوویچ در دقیقه 68 که VAR هند بازیکنان تراکتور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31198" target="_blank">📅 18:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31197">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=Pm9BTPJ-oylHZqNqN-4W_93MK13CPm6yJ3tRXUopbJqHvsRevCZnCZtwdke6Ul70dTdvnrwcl-kxXtovGjau6Nr0ceCZP1v2WRTeO8fWNCn-IxzBrrZVQW-jlnm0IYzS41kO48Q2Hu-70A_fqw91Ouhoc-glmqZFe6UcGkFdGLJ4e4zL2lsV9iayoZnS4OSKnTssatEWaN9lr6nnQauVGa50BU4RVY-g1vtgJc06PEvQOdfNoU8iAYtqvPIUaMwuprQozcF4CptnKksPCr7LYzM7Ol5Z1Htu8pnYSmyGJ9jLRmJgYINgd3hCm_LAej7wmn-OJk-uSD2REkonJ56Fyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=Pm9BTPJ-oylHZqNqN-4W_93MK13CPm6yJ3tRXUopbJqHvsRevCZnCZtwdke6Ul70dTdvnrwcl-kxXtovGjau6Nr0ceCZP1v2WRTeO8fWNCn-IxzBrrZVQW-jlnm0IYzS41kO48Q2Hu-70A_fqw91Ouhoc-glmqZFe6UcGkFdGLJ4e4zL2lsV9iayoZnS4OSKnTssatEWaN9lr6nnQauVGa50BU4RVY-g1vtgJc06PEvQOdfNoU8iAYtqvPIUaMwuprQozcF4CptnKksPCr7LYzM7Ol5Z1Htu8pnYSmyGJ9jLRmJgYINgd3hCm_LAej7wmn-OJk-uSD2REkonJ56Fyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31197" target="_blank">📅 18:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31196">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCzlyR0RoO2faG0ROKpgkeOR3P5c-BJLPfWmnXwxRuZOkyVlWBbq2hZZB_w-hzrDUx3vfCHYp6g14p3Ok8f_HHqh4cy8unPZ5B2sINfPtiwMEnXQGb0n4TLKcjg3qsYsp0Pdf76kEVF2x9pmRdnt2-QXrPz3ePQV_lkIRXnBeeItxu3duY5521y6LH8eaKjGea8xNoz5fEXCBJv4oysg-oWYs8M7xQ0vBvBME1RfjHdQQz-Eiln_1mp2shS_bpUdLS1PwbhSeH9I_Xl2D_dIuKIInGfmPYzcitRlB3RfzlWJy7GlLRHkKxYJFwlXrOBZXLneltTF828vQifex3_3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31196" target="_blank">📅 18:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31195">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KffnbnbS_efkjKrh1Nzp9eDVPZ5653hzKF4axRLFmiosRwFOXf-7WdI9Sfw1E4P2gbJUiojRX3WzvfNVCc_8rN81IgFhayik1qfDLb2nPFgbagoah2Ik5wOYstiQM4aLaXMOONSPu5aXvVcFHqS1SuUAXLgc9bV2-EkSnbs-cq2KsCptAkKhisizUeyY2PzHvKrwbS5ihXLd14AZM_Knj8x3OoXYGdtFZjimavJJ6ele24qdCyZCISw7gPIqVp47CHfDrTCU7O82G8rS0vSExVvd8Rd_TLAWdGnw2VBkZbG9U5ayxCx-gNxD6y-MNqgsqDlqqiy9VNVCDmnbvL3eFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31195" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31193">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2wB0ga7qzgrCwRrfDkAyVFbNbkdGwpdeHZ5DavpT3QgnTlbvjq0KjMSTeBLd3iPBKKJq_NKfcAHTxEWqaOu92_SNxCBZNlMeqiS0NFt01JGoaO60YPTQKP99Fsz_NsS4QsC3Pcv8KEEpFUhftliyqQQJeHMb7K_jG6PQFhMjcSUr4kRYCQwOX4qYRz3GAZAVzy4N08OcnAGcJC_ACP-dZy5UWz-oWZdY2534LUTo04ThKVCoiex9_TjCdhrWjHlOgOqWyxuxBouwqPqkwHmgHrt9yrpAf2PCNutxPnfEo84OanEBwXV5_J6X8GEZBCF2-eLmsi_RkjBjq4Wh726FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEcSoocpZhCQpNXt1n_ENwBwL9fWJ0zpaoKnG3Tig8BB8jd6fV9jeg6bE6z9aygKY3QjgRNaXgmHetrPvp3koRR9PF-zEC3aVrTim5ZQcpbAOoaJvGARpcnUjlqH2lsQjyEzzHtJRjY1b1SBhwAyCvvLM9AtEIi47MsHcmY5HCVeVdknBqUF0B8SNPejK5k7Zx02O5BgBYNQfJ9EwUnuJc1tQjpyvoJe9l7pAo1TR3s1860Ilg9nihjNu5Rs0hn10XtShomctRDMq05yWKwYTlMmol7CHtfDaV1r3RM2TOVnXFgfel-PCrm4it1Nj2hEdXwaF1ednroyD-B4BR5E6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سوفی رین اینفلونسر مجازی مدعی شده که لامین یامال ستاره جوان و پدیده بارسا اشتراک 12 ماهه اونلی فنز اون رو خریداری کرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31193" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31192">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b022014318.mp4?token=RTQe09cWsMNLEhxQvAWR2DVd6svM0YUCAYONqLB9yhDAhpeVIn3auN7pXuR5ih-VgEI7GkflztCyY9EaSVCZtwojeEKrymW2QzVslax3j-6cSfIYIxjXeNZ7BB6hyr3b6tHCCUXiGFQ3fPb7ZAlM9iZS0-CCaL7YU8DwsIsFHhV5as1oPOxJa-mPPmnAoTJ7TMyCIBSokG11rcxdWX9suxrxSvAVhP49UGwdaHG95xu6Nk6zD1QTYYiPP_up9Qh7DTWO_jSteW2C-9za0qT2I360-5ob-Yu6luXJpLHHkwA28mpQQ-Bogx3Tt6eLgxBL1Z_I5ELj1S53hM6wc0HuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b022014318.mp4?token=RTQe09cWsMNLEhxQvAWR2DVd6svM0YUCAYONqLB9yhDAhpeVIn3auN7pXuR5ih-VgEI7GkflztCyY9EaSVCZtwojeEKrymW2QzVslax3j-6cSfIYIxjXeNZ7BB6hyr3b6tHCCUXiGFQ3fPb7ZAlM9iZS0-CCaL7YU8DwsIsFHhV5as1oPOxJa-mPPmnAoTJ7TMyCIBSokG11rcxdWX9suxrxSvAVhP49UGwdaHG95xu6Nk6zD1QTYYiPP_up9Qh7DTWO_jSteW2C-9za0qT2I360-5ob-Yu6luXJpLHHkwA28mpQQ-Bogx3Tt6eLgxBL1Z_I5ELj1S53hM6wc0HuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31192" target="_blank">📅 17:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31191">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPRZ7AQToURhv8tzkEdGvNKxMl8IeIuiwEmXjh0uSajgxDSKT9giRPGsspmz1ZSACdX6-etnNLGK0W0QJkfFbWYmsFme0VK6260qd0OkRUDBYiWMGkN2gztL3MIbmdNhYmyXYpxPbbecdoe-U4YIgbueKDphYHOk5d7-l9Bg10vDuLaKDJhfhvN3vFgEbx-rly31LABQss_WKPSK_MP3PnAmC7RRNlmxUrz49plgMDMudYnjAdlND4Mh2R3pncs48J7NKIpqvzKG0YVbCe3zjHPR0HeTWfWuIhnv5WPCnj4WdpC8FUdMZjk5XVkLxW6RSVakQligyOrO_j9XfT5zNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
باخداحافظی پدرو از دنیای‌فوتبال؛ از ترکیب استثنایی بارسلونا در فصل 2011 تنها لیونل مسی باقی مونده و همه خداحافظی کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31191" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31190">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=sCC34ismEEtFv_GNG1w192EC8zZMVX5elFdQEkpCwNQQ5NyzCk2_KC4HjfN9GKGaTLVuFFYGuYWtJiBnEECO7XK_lFfVzClkedl3jNEHhAytCQIe2qvTbygaM9chu3MbHRlNPsVgaQmU1A2r7Yw-2ZW37NHmRaTyZvzxyjcqYBBeIJXI0LolRFBSPq-4FowEf9sJY9HLUBHTqbBi8QkxLxgHUpqjtt2YtJC0lmdXPANjMhYTgXZAsQy25EQJCcf3k_M685CNdEjaxAyaxsml6kUXh7isdPDaD1KfBANC-XPwgg8C_-GJ8_nN1iRl4CrzDYc8iXp-ecav4wSGTmaQMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=sCC34ismEEtFv_GNG1w192EC8zZMVX5elFdQEkpCwNQQ5NyzCk2_KC4HjfN9GKGaTLVuFFYGuYWtJiBnEECO7XK_lFfVzClkedl3jNEHhAytCQIe2qvTbygaM9chu3MbHRlNPsVgaQmU1A2r7Yw-2ZW37NHmRaTyZvzxyjcqYBBeIJXI0LolRFBSPq-4FowEf9sJY9HLUBHTqbBi8QkxLxgHUpqjtt2YtJC0lmdXPANjMhYTgXZAsQy25EQJCcf3k_M685CNdEjaxAyaxsml6kUXh7isdPDaD1KfBANC-XPwgg8C_-GJ8_nN1iRl4CrzDYc8iXp-ecav4wSGTmaQMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امروز مقابل تراکتور در هفته هشتم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31190" target="_blank">📅 17:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31189">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04026264da.mp4?token=HlIi1SwhlKW6blB2oS4b1ynu-qSUFskqZIfdSjmfBbiD6bgg61emvX0-7P1diVWu0tB05P0tBZppkt6guNhUUTZjv9cfLUl7JnbsBn2aRrtVK8l9zqGAGQqUJKktAGgr8o90Lnx0YlgHoCyN0WRzS82WlocLJtzRAG9xmrb0Vd8BMl09bsFpEVomeKGqFsvex3b6cCGshU3yBS2u2GuZf33h0DWGzwBP6g_sCrnxxDD0locRfyqzPtlO5kc7CmYPK9Z0BjjYdtCLYUjxD71ghiprzwlqhvJYjInChsO-ORmsLHwAOcURNgETqxvt2NUA1SrYLFFoD6_wGlvUiLYt5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04026264da.mp4?token=HlIi1SwhlKW6blB2oS4b1ynu-qSUFskqZIfdSjmfBbiD6bgg61emvX0-7P1diVWu0tB05P0tBZppkt6guNhUUTZjv9cfLUl7JnbsBn2aRrtVK8l9zqGAGQqUJKktAGgr8o90Lnx0YlgHoCyN0WRzS82WlocLJtzRAG9xmrb0Vd8BMl09bsFpEVomeKGqFsvex3b6cCGshU3yBS2u2GuZf33h0DWGzwBP6g_sCrnxxDD0locRfyqzPtlO5kc7CmYPK9Z0BjjYdtCLYUjxD71ghiprzwlqhvJYjInChsO-ORmsLHwAOcURNgETqxvt2NUA1SrYLFFoD6_wGlvUiLYt5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31189" target="_blank">📅 16:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31188">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmKLUcMTjSXUzLAa0UBtPKt5lzTb8bbt-4eqSSvl6EsQ5LWwo2Sa5g0ke3Vva5JvpZKy0u-4-1ywdxMLmvIx1-QAHOT948twcXGOqCYOCgCNhoG7TJBEblBrlDpgx6Fzu6YjPVzEwsW7baNqoIZix5b_8JChg3D8eZq4jzQtDWJjdIyHcvPj0aYCTxWjlgZNirj8hJ2nS_rbRhD9cPBOktMn5oUJ4u6nlvJNBpPf64qgFgd-E_VF3pOc-crujXtb9TU-_GqKIETS9iXbErpfZmSL9tFlX8e2AAYbkaDZc1Avi46foadg21UXz3xqseIcmkZrCHphYkhY5Lt02jE6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌پشم‌ریزون‌وجنجالی‌فوتبال در دیواندره؛
دو مربی به اسم‌میثم و ادیب 5 سال توی تیم فوتبال ستارگان دیواندره‌بودن‌که توی این پنج سال به بیشتر از 50 کودک تجاوز کردند! به کودک ها وعده میدادن که اگه باهامون رابطه جنسی برقرار کنی توی ترکیب اصلی میزاریمت و میفرستیمت تیم های خفن تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31188" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31187">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8tUHbI687eW2BTdvvQ7qE9uCBYvu9sCpY-POy2hcwuz2TrxI6Cq_O_fyvXiRuHcJfeCzulOTzeJhQDnKrxp4Japj7VY-4AH5o8qwgPqcDT6j4bQmq4iMlPrievvXrll5s4fZJX7tWpOompElKFPv0CQRGhD_VyGhbm0TEz68zrBSguDiTpj_S-_HocXefXPGelZ206USUz-lW6oF510zNitLRgoRt2_8C2zHHUx0olBoMs2NxrrMbl7IHYm4NoOmZAF1SzDlSIFzqlLKJYALTnCCID4J3VKlrJobCm4oKvqG5wl_3YgoIn2htku0EipzsGMmTthad864Ns8TBf-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب‌استقلال برای دیدار حساس امروز مقابل تراکتور؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31187" target="_blank">📅 16:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31186">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSPtRmeZDVFPB8rGkHqeTkp3T7nFaiWxf1WksLkM3VmfKnEUjA5fuUsPNJGnQjQtiLS2DFLJe3SMSK_qFwORIgaNTNGjbllk7cTc3rVD0psetdbuWqLMFQskfSlAMwB5zmiF7OfZUk1cv14Wr03FoPN2dFSEF707kWBnUaQV8V-z3yAXM8yZ-gYu_nJoeoLtXtj-Qa7prGv9iKzRWIEA3Tv6c48611WOE_8b8yOkEzDCoEQ1WLSOIMZKy75S2aOU_xuCmiAJTim69gV-hrCgBQZfCK8e5y2P5J6yLvjxYUKDRKrvhFhcL3R8D8c2BajJOR5NtYz_FxXHFQbZdrEazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب تراکتور برای دیدار حساس امروز مقابل استقلال؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31186" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31185">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8CSifbSsVPIMwzin9QW8X0vL0DGfr1ennjkw-rZL07bTjTGvBg4IheE7EI3ZNEBXO2SCNX4C1vBaata8hTcuDeyShhES3fJijDV2ALMGJKbg2056_w0cowY0wTEpn5gfk-qhNBDyjm2yVnUnGbh4FbihiMwM9iV_DvNtJTsSaVfdomMaq-R-UnvQkKjtZzy6D7zx37l_S7HPvU3jcd68lirditPeGY-Wg2hCvo8IrjlbY1RBvIWZ_Agux3wWV88PfvzgYh_8RJNB2dfsXMdEYV-0qw7mvZLjeF917jDfUp2tYcylUeWMFKj4C395_x5q5Hoz6B9qm0prVAa70om_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31185" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31184">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9307641030.mp4?token=Vest8un-mPwYs4dNykVPoRlY98rE1gUxepxftXQ8SFBvIjyON8m0b_9_ecyF6h_GJXkNFmfXyXD6IrP-b9Zj8e6KAYBNKQhOMehUTxeKuBkaijiWUT8Pn75zE10k4f2VlOZIeFdy3k9oro5YdFRcFjtYy-xSa1UR_NsjnrVCuYVzVpV4V8oxnPotHseGfS8njdRC4hViAij1GzzlZs1w9CJUx136DwU8Zz7NdrmNBzJAM1meOR4DZjOrp9nKNMZH3GV3HRxS8zbp_kG27NIAXrHINWnm62PL_KGwMh_jGaLpsWJlrj5JqbanB5RZMZmzVei4kjEOEGyW7DTFN5_rp0VsaaWyRw77rZku2Wd2Qw0jew6HGSRagYg9tHI4FiW4_rByuiAvgFP9LRaPv12SGz0CR8d56e7a_x6Jm5DOH0rUwfCOVb7JofC7w4g3j6Q0NhGuYmrZlryJfucr2-nRvtH4MDWCxUy1e0y_jAGPt8ESxs6welzCvRAe4xPJcdoc54SdDNBwsKenb75QenozONexFRrRQZYFWjWjgkk3uZxiiSfz1mLxAHcUXuTVFSajWtSegJqCucKSccSq5fRcvoEw7bxFtyM5sHSuOdVZNdVL_pE3ymU6q6VobSLIpDNTTmL-AuFdt8Z_Lpp7V2ljwrIRnzDvWo3YhQa1_tLrS0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9307641030.mp4?token=Vest8un-mPwYs4dNykVPoRlY98rE1gUxepxftXQ8SFBvIjyON8m0b_9_ecyF6h_GJXkNFmfXyXD6IrP-b9Zj8e6KAYBNKQhOMehUTxeKuBkaijiWUT8Pn75zE10k4f2VlOZIeFdy3k9oro5YdFRcFjtYy-xSa1UR_NsjnrVCuYVzVpV4V8oxnPotHseGfS8njdRC4hViAij1GzzlZs1w9CJUx136DwU8Zz7NdrmNBzJAM1meOR4DZjOrp9nKNMZH3GV3HRxS8zbp_kG27NIAXrHINWnm62PL_KGwMh_jGaLpsWJlrj5JqbanB5RZMZmzVei4kjEOEGyW7DTFN5_rp0VsaaWyRw77rZku2Wd2Qw0jew6HGSRagYg9tHI4FiW4_rByuiAvgFP9LRaPv12SGz0CR8d56e7a_x6Jm5DOH0rUwfCOVb7JofC7w4g3j6Q0NhGuYmrZlryJfucr2-nRvtH4MDWCxUy1e0y_jAGPt8ESxs6welzCvRAe4xPJcdoc54SdDNBwsKenb75QenozONexFRrRQZYFWjWjgkk3uZxiiSfz1mLxAHcUXuTVFSajWtSegJqCucKSccSq5fRcvoEw7bxFtyM5sHSuOdVZNdVL_pE3ymU6q6VobSLIpDNTTmL-AuFdt8Z_Lpp7V2ljwrIRnzDvWo3YhQa1_tLrS0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افسانه‌یاواقعیت؟ بعداز ۳۰ روز در قبر چه اتفاقی می‌افتد؟ روندجسد انسان‌ها بعداز مرگ به این شکله.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31184" target="_blank">📅 15:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31183">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxVqIWXSa2eaW7MkQ8QCQCuvOHHzEQJc70uycfFupk5sxz0GDMavlLFYHZ-oFF4eQcpDt6oQ6VQHu4jVfpB_KfqmwTk905488wvYOA_ZlJreMymcHBvcPJUqFjoqqCJTULpmVob80vXCrTyHDD6LPNIkoE2vWNThegiud60NFi1oNZXZqHCVQVNSkpQzkRZyPSxyttzgBsJxPpyDI9CcrEjPtydV1eoD5Lp_kQa97QB9ZP5IsI5oGnL_RP0Pu-eJ-uD85m2M3dEOky93nULonRJn-_1NmAN8lhXEjYNPQ_pEJFpIhlTJobc37ucUmLQbzeNBAPgEpFJHFdR69LSAew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌امتیازکسب‌شده در تاریخ 5 لیگ معتبر اروپایی در یک فصل؛ یوونتوس در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31183" target="_blank">📅 15:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31182">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=uYlrGVlgRL0h8UszYl7elCoHLQQFY7z2DSAqwFDUuk_lmO_kstoibf9dCaNmHebqYY2OF7-UhKPNiIMfjf51Zc20vEmGO2Gtq1scScZaQbB9WNj9pEGcxTuf5DDvjPVtgi2MEARJQ4HXeVqGIbGM_Mq46y8gmBRnRn6qZJ6pRBy6cthbEoq5cfEBZbvhCKweikrY-82SSiEZVlUeBwNmOXujNO9joDvf-a95JXccRWw50bhknCW-GlmHxxza-51yf1hvfkXShntFhbv1UklSgZ1Wj5gOYav724X7U0GPAwp9MkC_g93346JzKJdDmdZyMCXWVGVkTZlSV7Klcf21JJRumcZBqehuPzlgSpyaQVbYfZXwhRuGE1GiLanvJ0jN6QTG0cHjIn72cD4vK70rb4Nn4Pjgdso8LXRA82FlEE0PYZOJi3qAcXpIJoz44fVYIXXth9tqBk1OfYKka6UiilLAOCyqxP0O8U7e7F2YQWKpYVAYXs42QVIdEJGjR9OTw4itVpcbaTpNsrIWBFG8e9wSa5WMK1INkoc9e51s3k1BlsLNTPZKV9tPtplZ1YIjpa-ickLxX-3N5p1UanQCqFd68k-7xBbhwgohDFjpB8qZLfu9RtEw0rg8iUeYFdYRESwxMgQQFHC_jjWIYKFkvYnqnTjyHzFzbKJi1CPAbBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=uYlrGVlgRL0h8UszYl7elCoHLQQFY7z2DSAqwFDUuk_lmO_kstoibf9dCaNmHebqYY2OF7-UhKPNiIMfjf51Zc20vEmGO2Gtq1scScZaQbB9WNj9pEGcxTuf5DDvjPVtgi2MEARJQ4HXeVqGIbGM_Mq46y8gmBRnRn6qZJ6pRBy6cthbEoq5cfEBZbvhCKweikrY-82SSiEZVlUeBwNmOXujNO9joDvf-a95JXccRWw50bhknCW-GlmHxxza-51yf1hvfkXShntFhbv1UklSgZ1Wj5gOYav724X7U0GPAwp9MkC_g93346JzKJdDmdZyMCXWVGVkTZlSV7Klcf21JJRumcZBqehuPzlgSpyaQVbYfZXwhRuGE1GiLanvJ0jN6QTG0cHjIn72cD4vK70rb4Nn4Pjgdso8LXRA82FlEE0PYZOJi3qAcXpIJoz44fVYIXXth9tqBk1OfYKka6UiilLAOCyqxP0O8U7e7F2YQWKpYVAYXs42QVIdEJGjR9OTw4itVpcbaTpNsrIWBFG8e9wSa5WMK1INkoc9e51s3k1BlsLNTPZKV9tPtplZ1YIjpa-ickLxX-3N5p1UanQCqFd68k-7xBbhwgohDFjpB8qZLfu9RtEw0rg8iUeYFdYRESwxMgQQFHC_jjWIYKFkvYnqnTjyHzFzbKJi1CPAbBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زرگری حرف زدن جالب و عجیب و غریب ساینا کریمی ملی پوش تکواندوی ایران که در مسابقات آسیایی ناگویا مدال ارزشمند برنز کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31182" target="_blank">📅 15:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31181">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwxiVq4gKOmCiA4xAW7Ol8hxlarRcfv6gCTSLzxL9ZohIy29c6DO2vGBGzbGTLP2V1_YVXz2comcxTr-PDQQn5HpPJcjhsUxlEof470cNhMdxTaRfnfHaaB0qu6fLxkLEYwILujuE75Q1Ow8g338M2iQgKw8LRZzOOpbl9aWq6-SEDrxNU0DUNBKg5_1lTUb9gxT1fTJt8U4bu225VOea6dMsPVaFy5lxcftl9YPNpp54uSaoIS0KMsPfo_uG3cU1hZ695Em-gZ4zSijqwg9s3pKrX101RwUZwZ65lm4y8DfmoscuPa_FZ12F1YRbzhLa8SmBCy2-n39fUuUyJYydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31181" target="_blank">📅 14:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31180">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvuMZa2RwH5e_dGhgZcZCpakefb2yXoTodL9oGPOnI79bfF5QODTtAQMdpt4dOEvMU6yWBd_XfJDRobBNTdowoi1zNDDmMbMIqd1_-PUfIkFMR94aOEdx3x4OVAut86gVNtikEkwR3Ub5kyGW-tvOHN0mMwAxEauukzZWN3iimtHQnzfD2xbBVQWNoUB4GM4UhdtJM1aFDASXgamKlHLcpDFliNdCQM440H4EUTrt7zR-6Jw2FWHfKRTEJaSkoBD6YoCZLjBCbl-cWzxIm6LN0AvmV_Sv1lXEWht-EOw8PNTuH8cvQWs3blHQIcapBFP-_JHe1Uv8IoQPIzp4tvk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31180" target="_blank">📅 14:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31179">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDkCMoKV1zaBl5d4V-aCKGRGpCYbZiXizwwyRI96mZ2vG_HFXav3_OeE92p8C3UlQ4lcoJKA35oq3_KRiP6OwcrgVIWv3WaC_FuP5sgRRTqhnbjdbL3wzhpa2B_F_PwwPS25T71vdYALeFfZ6P9rjDN2Sg4ZC_GL6AFob9grG875tgQa7n_56d4r7WTqfWe1AP1BEgAZClmF1D8emgcfSnfYbW9HD51Eg9vSdRTRzDAuAPAmNqHhsTRPZZT5kLpJqM16NLAkgUhHITsfsb69NKkbxWnXQgd37qvaaRqIOck-_sUa82tV27RG8ly7Ik6WOzrMfsdgxLOdjJtabUXBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ترکیب تیم منتخب دو قاره اروپا و آمریکای جنوبی درقرن‌بیست‌یکم از نگاه هوش مصنوعی بنظرتون اگه باهم بازی کنه کدومشون میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31179" target="_blank">📅 13:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31177">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bNbL0EnzQBkFxKXnEt-bmIL7xegM3rh7cx5nb0WPqfnIIm90OdhNEw_54svcVT1AmG5eG0739FJDaZfY4aAob2uUcH70hy06mL2BqcN5R2TbXXuyVgZnUXTg7c8DE180FpNmtnyLF7Fh2Ax4-Qheoy2RU3QmcVeiGhxUTT2EgSOIn3vf74LQg5MATQgXB44fuLKO9heyBuU3XWf6gKBF7WUZqugGsulCbe6sniM_D2CuCPrxuWS3AKXwWZZwKCXmIKFuWwp8Iy6JLaYFtNjqSv67KYWXCf2wA2i4TXqSMwJqTdv-4XvPHMzQfrEXCs3B0hieX3ImPGjmMwK09cFTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGx-EpBTrqaoLaX9mk7mwXUmjPR0VzojX8atRC0tt9jqI8SbpyEcVmhKj0eZzS9RjmpnMk9O3b0emqdL9lPIPX6S91suEg6w01JO7AcDSN5lgXWElampqI9AeuEir5o6v2h1nzpu0v79v2zYl1EBab6PXOrodEk2inQitdvafIDWFsF9y30lJGpaBakahsgZe8Q26x9sv_z51oVUoqDFf5OlbTgUXVj9HtobTnAc_azaLkmXbqOojyhftVOF-eqF8IEWxyDfXFEXiTNJ8sKiPcr8mlnFL6don6rwpfjd5EmiKxCFZL1ATkGbCnJeVw1W575D6jVAE8JZ9tawvL47bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج‌بازیکن‌برتر قرن‌بیست‌ویکم از نگاه هوش مصنوعی در دو قاره آمریکای جنوبی و آفریقا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31177" target="_blank">📅 13:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31176">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxpN9NsxZ4EQvSgFxYTwIx3fHXa7wYK_HhPmdEErwpFHcFFh6xuPDEEzQJtHZz2wrr7oRMPsC5osC_ItBxAuBvi8JcMZlqhk2jFGHKaYkG6OYA9iC6AGlCrAqeSxcxqbGh8TVxVYan0-IPuWjyueUqyoGJ4wG0OF_3_KsZ5szERdY2RQ1C1NDlpWkmHZpYpMQ0jzQK8jEq5tGp5KKehaZ_8PLYy-10UgrLSsoWDTmuOz_N53j6vMNYnHXtgMpYuLmytSbiCjBjKrVVYEbYPJpTPKXpzvRll9Tbqfa7ANYQ1tu8T7R7_MIrAFZLgwE31iHaB3pIRKorlIZcS0t7YA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31176" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
