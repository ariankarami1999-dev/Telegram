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
<img src="https://cdn5.telesco.pe/file/P7d3I4BfVc4-z4L2DbTxHzOvCbUhT6qNkFKwqeDNubdIa5dhdKQO08tJQ1of4jDANZ1Cw69muWnxa0rLcrhaR2dHgegKlEls6qNrnl7H17nvPDtdm_AUOnIysT9Ic_EV2WFlUiFHzkmULJXfCPJ26pflSnEcBNFOKAnGsg-kY0waXla298CkIvmheai2D3M1K9qsyip7Yz5_lJfo9uM4XDrsP97xlwbZAu3H0wLjO_lSeI1dh45DmprN-nIw_wdJDbLeRS4soLzPdIiI11GxR77AbIXRPCQOJ9BdSnYao07NffWbavaYJA0uv9FWsQZ6PPSOdgtjGL8AlYHDdPekQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 461K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 20:48:24</div>
<hr>

<div class="tg-post" id="msg-103988">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myhXpAFGmN4xVg1evta2HNiDEyZh7tk0FzB7WiIeRpw8nCWm7-H7NwzYWVDGpg3NjtjF-AmVN470XbF1_a9qq_2QKMfGdtW7dutBQYlgpnBknWdvJDqqnhpHZJAnEorL8KNPkiyK6D-MNiLzv3ke43LqcFWPHVYOFVl1E4PfluZkoBz6A71gn9v4cWDaZ18vaB8eFc28_VMvHeClO3k2UbCbKYZn3HeJ4Nr155TfmHlZApTQGpnCz_qgN3ouvExwVMliPR5RdaOqQ-S9zb3_EW1lcUXbFKQoLvW0xMDgmqa7CQvH6ryZlP4pi-FNV2fGcobdIUrl5jVCd2yLsu_oxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نخستین حضور دانیال‌ایری در تمرین پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/103988" target="_blank">📅 20:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103987">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2WWHugav6wlEcTLrHurTZgq6wXvaZbvzFUv0napJBhUooE2z6fm5JJ2XlnOKGcQUdfOHSy0iV1e7Sb-NaIho93CAZrP4WADR6vH3l9H7KJQlKedj0_-fibHmvvvjqjyZecuxwYu_G3Xs9k3Hvw00CALK0OhsEbWk_60PzWgou-VZBC6ZUvBQf1qVPeB3DPLRglI-7N_DVtL9POxLgNJ5YHjJP2GrQqiTvoxXF1WKWUE0jg-X_ookscp4v18tnEL5F_pT6p28Jd6Ds366JM2ltShjbvONhfR4VerETnQ4mBxsNWaa98wMPoEVBOtz-jwcLJCRpvPGyLilM5niD-Jog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔥
تیم فوتبال خاتون بم در نخستین دیدار خود در گروه E مرحله انتخابی لیگ قهرمانان زنان آسیا، زسکا دوشنبه را در شهر دوشنبه تاجیکستان با نتیجه سه بر صفر شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/103987" target="_blank">📅 20:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103986">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c623e2cb.mp4?token=lAlujt8PuuDHmp7lWxElIWE0DvCViVo7J_IJ6LWzWSKN2z7f4rpwyUy0dbq61WLoYcSU06Y-tQeEglRKGSWCfh5gXicV6b2GL1wJP-IUzJC6LK7G35Wypfg9bYwyDZ4AWzhUr7llNGyd5mBuv8S7YVzTwkuIJyTaWNPHo_uhgTvy7jJn1OHI3YshJo6-TGZwaDCzxH2Ahutormwvp1NOo0xdfJZta5-aLfnst-gwew9d727s7yQdUIA26Vq4c3fRMugeDsadsF23KwS3X9wUP0E686xZL0hl15RrpxSUEZjxUBK8N8o0g7KAthHPm9mHjpcB7KLdmuCSObi53w6QWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c623e2cb.mp4?token=lAlujt8PuuDHmp7lWxElIWE0DvCViVo7J_IJ6LWzWSKN2z7f4rpwyUy0dbq61WLoYcSU06Y-tQeEglRKGSWCfh5gXicV6b2GL1wJP-IUzJC6LK7G35Wypfg9bYwyDZ4AWzhUr7llNGyd5mBuv8S7YVzTwkuIJyTaWNPHo_uhgTvy7jJn1OHI3YshJo6-TGZwaDCzxH2Ahutormwvp1NOo0xdfJZta5-aLfnst-gwew9d727s7yQdUIA26Vq4c3fRMugeDsadsF23KwS3X9wUP0E686xZL0hl15RrpxSUEZjxUBK8N8o0g7KAthHPm9mHjpcB7KLdmuCSObi53w6QWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تمسخر مسی در استادیوم‌های کشور آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/103986" target="_blank">📅 20:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103985">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7HXbST4KOypRwdmgf04C6H2z3R2-FjtjhKkdX2z6VZJpNpLe5_eWVLtG32pfUh6_qsmPRVm1acQ9CcQhUfoGffhIZSEba5Oh4-s4noSCvb_x0bnF2DbJtVJyhDzjrYcu8xW2mxE5oRxP2V-53YyGw3tz3fOKDAHxL093bf-pP34a10jJ5cTgsREll84ygRS8zb27BkhH-FvktshwGOrxdgijtYRuL8x4f9Nc-at5fm_Ce9mr7PVtYDuMmETL-e03L3V7AdPHBIf_5u9Zrp7gvdwac9-Y7DZ54aFu4qSG5dMvbYyR_aD7tfn_Vt9nUBJn6ap_MW7wkKqrDO0OuHehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
متئو مورتو(معتبر): احتمال موندن خولیان آلوارز در این فصل برای اتلتیکومادرید بسیار زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/103985" target="_blank">📅 20:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103984">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4dihpDNGFFbGF2hwjHw3YO4RQgU754HksI3sYbCORW6jGs3wj2iuvTbPMZX4nV78-XlbVXV2VDqS37aMxdYrzVGQaKSLwHwRAk8QKCSAmKglY-IBrj5WvoRC9ibCQ8QnRO7IMxY8chG7tj5L8uXFCr-1si7PTsFt5bWW7kbBygOWyeokXeiYvEzmX3z4cB4ElYZLAc8fRQhHlq_XI0x8JYXrafo1uOlRuGVdmN14dEVVC8qNCbe5yYFnJUg8bLlrS2YzTxzkhzuH1TG6DkmpSpwbSRudqyDQTcGrKazpj7SXtUS4LlHFRNOCXrpgDhbcABjvQsu5_OktWIypf-UHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
😐
😐
🔶
پشمااااتون بررریزه؛ دختر تهرانی با دندان هایش گوش دوست پسرش را از جا کند
🔴
حوادث رکنا: یک درگیری عجیب میان یک پسر جوان و دوست دخترش با آسیب شدید به گوش این پسر پایان یافت. به گزارش رکنا، این زوج پس از بروز اختلاف و مشاجره با یکدیگر درگیر شدند و در جریان این درگیری، دختر جوان گوش پسر را گاز گرفت و بخشی از گوش او را جدا کرد. شدت جراحت به حدی بود که پسر جوان برای دریافت خدمات درمانی به بیمارستان منتقل شد و تحت مداوا قرار گرفت.
🔴
نکته عجیب ماجرا این بود که دختر جوان پس از وقوع این اتفاق، خود نیز برای کمک به پسر جوان او را به بیمارستان رساند تا جراحت گوشش درمان و بخیه شود. جزئیات بیشتری درباره علت درگیری، محل وقوع حادثه و وضعیت فعلی پسر جوان منتشر نشده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/103984" target="_blank">📅 19:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103983">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szE9xj1HBNJmCLyjeP3NKiD3bCxU8bQeIOYi-N2EtytY-QEN2KV1xgPwTXxZlWRLzBDyelaDN3pQONZXotJg2JEYPV3vjzniVOLdAjoUfRJLC_NkJYrG1F-9UmC3pPsq-GWgALT4PGpxIOqXBmD2VrOXpppHENqe96Rv8RTAxxW-5BejDRzuYXQD6_MyKtIyLy9mR_gwL7XMgeTM0QIc9fok5W7pHT8yzmEww9xEUNULnVanBlgZ-bgthUOTglXZyj3s8AwQPUccAw2sp7AtT3P97h7q5VTbgRfQFq-aMceGj3w_UBkkL06CfjsVn25QV3RGxdsJih7_tnc_Ao5uZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
رامین‌رضاییان تا ساعاتی دیگر با عقد قراردادی به فولاد خوزستان خواهد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/103983" target="_blank">📅 19:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103982">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xedmc63Sm67kMZKxLBwYnY7JUC1_dIg2ydmDCEqRfxQJHmXGQxN4427YQRpJQi_S4N7fCcgeoQ1tr_lrYkZAuL4wieX-OCf_tQ6YAYnWeGttsuMSY_jVU2t6cfApKipN0lIj6pR36-_Cuq-LdIWO-ISsjV-T28IvKjRMMVNrKVrtZ-wG9X5Us8BDumI9cRZEuZaJXTOFCOTtxWLzdREX8Dtg2by-ZZNsjT4dmXv3uMpmxkA51jn7qihemZ2WI2I2KgUIVNGTWJByL2B5ccDAB0UtFB9dAj6cusGOBf5ANeH9tbehl5x6EnsrWI2Am5lPxPxL60AZ9BxAkfL4fJxRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رامین رضاییان داخل هواپیما: انتخابمو کردم بقیشو میسپارم به خدا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/103982" target="_blank">📅 19:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103981">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rF29MaWH2CCryKMSwVrduofoFNR84ugrYzVd30Egd6FhcaoA95QxvZWMpl4xGwa-g2idrh5Ae-Q4wZHJi7gAPkwBfHqsdRdG2GC186omfH6H9hD426Qrx2XfjSffhCIcNyWq8lALow1fTOGUQDm1lRwe7a_5IpH1f5fkD7w1JvhCrd-87FXu3Jsu9wukJ4HQUO79eciBJDBGxB2N4jF1rg21t2LFEA94FVKY9qCGC74INtYviVaeF2RKR2TEtCRSEi41x8u0BMIkKe5QEOyrg-_RaUInIjLl0hHrwW1FHrOBgPtj3oqGW5jx3erccAyeZa5EgKqmOSYoIiTvSKHKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
قرعه‌کشی فصل‌آینده لیگ‌نخبگان آسیا فردا ساعت ۱۱ صبح برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/103981" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103980">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLnCPhQ0TMmB0AnARLhkKbtQ8O7euUFsMxy7j11Ts6fh8TMnNTnddeWGoCsYYpgSNiBlKS7RfpwvyczuKDp780tk6RPhB8Ea4lEycULVpqtpS0zODhtFdDpE6fsgGc3NUe1t8wL94UxbiBB81G5KRqkqVHihjpCbQgf2qX7bK4s9MOPiOyNpugQLMSz4j_WX0ReFelS7BZPRmobh-Zdt2lS-nWEx1vk6SJHYoGiEid_jMVkm6WjWj3ttIvG2mRhG8TwdyP4rZ-botvQD3Ez68jn2at1N7m0Jl6vgPx7H-oKCy-3-jiXT6sfFh5lahtUfUJ263o_r8Kr6qop8KyEEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز سه شنبه ۲۷ مرداد
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
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/103980" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103979">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdOcHP1vEzBocvOuDFJNWHlNamgka1zbkxCfNm6x13L4gWE5zYLI9U6NEiIiayWm5cNE3SqJidGSkXAemzXBaWxSVdYbNODytihq0eC43uNl6oP15V75lzXk1AGD6eW-nu3QDuH_RvznKSNzjtjkIVQS-84qecH6DBE8ITdsrw96w4sGWAKfZX2-3kx6wRZf9Zx4Orub8i_J7U_Srfufk0GZJX3H-WRWQVOgu5KBZuy0ziNQXqf2OjVjR98mPFbEUXt7QvLte9nisJa30HHQ26z0jh902csIWquzhp4xIEPDrbCxH4IN39iA-W0Y-pUJ2zB1ZyVCoVjJ40FFpYxShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رامین رضاییان داخل هواپیما: انتخابمو کردم بقیشو میسپارم به خدا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/103979" target="_blank">📅 19:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103978">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868e8de9ba.mp4?token=Dhjomvw5xoMbT8VdZOHyqrS5NvssuZSypTklGLoqwLHLu7-_js1fnUwX2bzbYswJfOUwn11dbVYpaCfbATRnX53fQERSd2oq71oqzpeOKzLpSehOFzPlzur2GUIiQeZ4CGAfBeczezULpSXVYomkUVZjNDCV_YaejuyZJ4NqIz9l8Ue9nDupvyCkVefHPSwWfGKj_CzcK2nS0puqCqs4gOd8pqNCOZDNKTuuirF9gUcI_XEiJ3WNOLf9vzp1SuZftRGxHgRo0bj58fqYhwNr6k68_KhhoSpgZXCJJH4Nat39-Erl_zalVjrTG5ZsSS64er3qHQz3oYxahTvTdzdbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868e8de9ba.mp4?token=Dhjomvw5xoMbT8VdZOHyqrS5NvssuZSypTklGLoqwLHLu7-_js1fnUwX2bzbYswJfOUwn11dbVYpaCfbATRnX53fQERSd2oq71oqzpeOKzLpSehOFzPlzur2GUIiQeZ4CGAfBeczezULpSXVYomkUVZjNDCV_YaejuyZJ4NqIz9l8Ue9nDupvyCkVefHPSwWfGKj_CzcK2nS0puqCqs4gOd8pqNCOZDNKTuuirF9gUcI_XEiJ3WNOLf9vzp1SuZftRGxHgRo0bj58fqYhwNr6k68_KhhoSpgZXCJJH4Nat39-Erl_zalVjrTG5ZsSS64er3qHQz3oYxahTvTdzdbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نمایش درخشان آرائوخو در اولین بازی لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/103978" target="_blank">📅 19:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103975">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TREh80RVrRXUy31jaaJXumVCgmiPFrrd1bFxnq-lA1V8q7cs0kwuaQCK2GovTFgp57m_N8MmV3IYzZrFikBkTGghle0Q-dKo3UOx5jBu5w1-o8FoMdrZT5NSJDHGBaQE0XU_K8bMCQWgsgBmD4FTp4sDJmUUvJ4utusGiw8vdn_9RjCgViu25Exg7ueocfdnwNnw_aKXe591qtvr9D68_bTZB9jh0DulNza0gvX5LnaL9bZh_qMpvqT20JYNsN6PgEZnQDOKoifBGU1nWxAeVnCX8SXrOhZXkbEwQuEHXU1WKPOYbxNAtjLPi2B3CJZ4MxPrimTbvqAhV3lZLTO-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmBoFaqyvAnRk54fAFLeVJbVOOkZ4PbfAoZezOBRgoa8cjLiIDxR8paOsi75AMllanJkkECjFmVw4cvCFu9c3gjTUgTfULc1x8fHhINA-O6zKDvwyV6OAUdsKNRKegqqJ6DYW3Lxw_N3t4ikJRdcdCRaqgx6kgy8sB0Xmj6lgV2BBAeZCN-0ZYeRZpm7WPFWvhSvHdMXpBAyCiOtrroFb8yXzlEd5JCyqc-DIomF0Qj9UOdG1T0fIxYzuUy5CuOTVINRfCLYeBy8uHj1DJ2r6bRKub-q1lXMcL6DvKZjPEhGTppQTPCkQxxIkpdafM1imOFg6ZX6nIVABwmm6FxJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3gbe5Zx2wzwEXEFr6TByKnQu2pdF1evfm1CjlvlyeXnWQy5VUtvH2bwy_GBE8CVcx6CA79d_NyVNj3N_BCqMQveKV8WlCDOry2FKi6nYDEVr-Q-cT_Fy72ZCYh6tUJAEkdwVOCZblm6LpLPTbXZrygzdmWsqnFymvbfgJ_8ItrGhxN1PLZ4VEVRHYyy99xiGOZYYwFcdssSUuY6-sL0DoZS4LUVqSv2jiUwRsZmKrhr8gfRbvFo014xb_-nPHqhd_1KdPOXuiwmFDaHe5iBTDoQaFPzo-uUbEHL822E1hJniKmxb3cK21pNilPSce4gz_efIPBdTiTSNKjQxp2Erw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
به‌طور رسمی: کیلیان امباپه و ارلینگ هالند، بالاترین رتبه‌بندی را در بازی FC 27 دارند!
⭐️
🎮
دمبله، ویتینیا، رودری، کین، اولیسه، پدری، یامال، بلینگهام و کورتوآ با امتیاز 90.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103975" target="_blank">📅 18:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103974">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20aeb6e887.mp4?token=slY82Elp-uHJMvgIP0pbA82rlKYnDO0eVCm8X-APu1RDBL6XmKJ7_SHoMNcf8VSJunTjSUKtIMRYmIo7Z471tq4N5hmImICKlIAxF25KbWS2xSnlXOvlTpM362K0snnCT5JKwX7UulGgep6igydUyz6l1JR6qGKzGVeGaCsgflvLNnCQ8sc2HUmSHHaFTUqhSXSz6IF5KrSgNCHdkxg387_tb60MS5IYxZF3YDHs4xsWZoZUGaS6pJNyVas4v4V7LHQ4gv8LTbM8yMxFfGefPsAAb2a7rj4QMqAFZ4_4eYOkQNb7Jwmwq6HDtWIT9k-OuN8nfGg1nOspd6ckqc5B7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20aeb6e887.mp4?token=slY82Elp-uHJMvgIP0pbA82rlKYnDO0eVCm8X-APu1RDBL6XmKJ7_SHoMNcf8VSJunTjSUKtIMRYmIo7Z471tq4N5hmImICKlIAxF25KbWS2xSnlXOvlTpM362K0snnCT5JKwX7UulGgep6igydUyz6l1JR6qGKzGVeGaCsgflvLNnCQ8sc2HUmSHHaFTUqhSXSz6IF5KrSgNCHdkxg387_tb60MS5IYxZF3YDHs4xsWZoZUGaS6pJNyVas4v4V7LHQ4gv8LTbM8yMxFfGefPsAAb2a7rj4QMqAFZ4_4eYOkQNb7Jwmwq6HDtWIT9k-OuN8nfGg1nOspd6ckqc5B7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال فصل رو با قهرمانی آغاز کرد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/103974" target="_blank">📅 18:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103973">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bede2499.mp4?token=ZEEtJ29PhmUA59Mun87LMsW3zRi11aCX1V6Ziq2i6SUJe_xPZhUjMYcWoSRjpWtAzFF9ogNEst1jsnkGRtKN_GJ_4r8otRieq86eUTR5lARpy0iKw8KPabAot01yVKLJyWWws9tMNjnepHQ5pn7bJ6ahXDGd9ahd3fRhMykt72ozseMKRA_mzqXZpUTPEIrrhxXevki86zgHyA0t_n9QDnomzn7mYWdQA-yrkgGswYDiL7PcHKmUPniTVTEAU3oAkQZMl69aMI5IuYL_E04kKQuRZQvWL27brcZAE0CUV-kTjZ8DtXe5XDCBwXYQ5kBXhj9sSZRBKsDOi-ecwrELvzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bede2499.mp4?token=ZEEtJ29PhmUA59Mun87LMsW3zRi11aCX1V6Ziq2i6SUJe_xPZhUjMYcWoSRjpWtAzFF9ogNEst1jsnkGRtKN_GJ_4r8otRieq86eUTR5lARpy0iKw8KPabAot01yVKLJyWWws9tMNjnepHQ5pn7bJ6ahXDGd9ahd3fRhMykt72ozseMKRA_mzqXZpUTPEIrrhxXevki86zgHyA0t_n9QDnomzn7mYWdQA-yrkgGswYDiL7PcHKmUPniTVTEAU3oAkQZMl69aMI5IuYL_E04kKQuRZQvWL27brcZAE0CUV-kTjZ8DtXe5XDCBwXYQ5kBXhj9sSZRBKsDOi-ecwrELvzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🇪🇸
کیلیان‌دیکتاتور به بازی‌های رئال‌ هم نفوذ کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/103973" target="_blank">📅 18:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103972">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/103972" target="_blank">📅 18:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103971">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djeMi0Wyyh82jzAaVbLjjXzh4lXx7mpJPUohuUPT-Kah-ligh-EeAErTle2wG9Jn_b7Gv0ipLBO-DRW6kUt1i5DJPEeLgsZlO_IPKPPEMnogbM2fcniXFPKRu2EmJFvZsLl7yXc-GC9vLHnaFbb6dFVDY4NJ5RBK6_69fyodWTdy74D77YR2w0IeDQCWjcCKwcuHhcXmQAEYjGqvVo2HwSNj-lB5zWS0lvj1-awB3NhPjwmWPE2t16_IOBYXvYy9cB1A2n9tjRSIDGsrAkqTVUVQuwXmIk_MfTeecc283bQf0xcR9cxsA0LBE5PyNUiEoygrKP539rCTDcEJXNEnyw.jpg" alt="photo" loading="lazy"/></div>
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
g26
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/103971" target="_blank">📅 18:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103970">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">۱۰ امتیازگیری زیبا در دوران حرفه‌ای استفن‌کری
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/103970" target="_blank">📅 18:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103969">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aed8d80e6a.mp4?token=s0wKtNc_x1Q30NTTIyYkDtx-xzHslJZZ8U6BvngFeP3AupDwB_UFV_tT8U_sALSaZLMVSWB7Ip2Q9KxcxVLwTNKKzaNmNTjgMghcqmwFJlYsqKmZ-8qxVrEELcCzxXAz05TVrNYXLQ0HdElGF7534OLCL8J8jmDnVKIOwd5vCs7JS3_AFTC7sno4apwLZwtAP0ktIc87llLAa0c3ZX5celVmMxhFOQVJXrYnP495me5x1JREDDDc-_ENAiiaUSPmCJlEzhf1sBRk0XuavfeAo0Hyey71WHmOpGK-U5Y6QsK1JLQ8GwZKeqqCwnoBFTyaLp4xFUY5ssUxGE2FjlXTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aed8d80e6a.mp4?token=s0wKtNc_x1Q30NTTIyYkDtx-xzHslJZZ8U6BvngFeP3AupDwB_UFV_tT8U_sALSaZLMVSWB7Ip2Q9KxcxVLwTNKKzaNmNTjgMghcqmwFJlYsqKmZ-8qxVrEELcCzxXAz05TVrNYXLQ0HdElGF7534OLCL8J8jmDnVKIOwd5vCs7JS3_AFTC7sno4apwLZwtAP0ktIc87llLAa0c3ZX5celVmMxhFOQVJXrYnP495me5x1JREDDDc-_ENAiiaUSPmCJlEzhf1sBRk0XuavfeAo0Hyey71WHmOpGK-U5Y6QsK1JLQ8GwZKeqqCwnoBFTyaLp4xFUY5ssUxGE2FjlXTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
وینیسیوس نادان در بازی دیروز رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103969" target="_blank">📅 17:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103968">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPZa4aC7NL97bkMyAkJsRzy1OewUZHbkwgeaRty_j4N8yyHIjdzI--teWR4ri6gDHG2uQT31B46HF2b6u9CAGJC0zvPkyi74YSFNKDOXQLZzaaA2DR57VwNaIQtw-RhuZDslxfMle6PmNGJqHw00k0wvFWcRzbwla0ZvOOel22qeYHWQR8VltFo7BNibouc3wkq-4qb_Eink_rnWAVgDQXuYwfr02H86aXQ5uzLjRrE5T7hWbWOqZtsSPrgGCsQkIXqF8IIEYmtZCof9BaNB8RJIN8uuKQim-Bsail1v3hsDUkEHLt9xOXwoRjRWWepGBMWIin2lr2KFp_okSZv1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رومانو: رودری در پیامی خصوصی از فرمین‌ لوپز درخواست پوشیدن شماره ۱۶ رو داشته که با موافقت این بازیکن قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103968" target="_blank">📅 17:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103967">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJDZlrKRMCwRqazxEKoRs51WWkb-zvVfywn2ShFQvPCetCEyC0-lu_QjyoIFIkQWe2rvKpmJOWCYftiV5PmYU_F7IsxjkCcmw6o8H85O_T6HX56k9pZmV1-A9dFMIRmNPUIAlYSH7ROKC8OoerLfvNTkdzmX6lkUmNp3kLEimeyaZuurKItAkYKuEc2jvmC8X0AQWgL8mRPEuJ5ilS5oBcYxChigQ5hT0-E4cPLwtqP4DmdXiZ8j0jXFqmSEgzNTFj8EA2HurwyoUm27wJOC4ngegZLSp4D1iHCJd-9vLc1tlVY0vvq-k1qT0NZTg-WZRnrsSDHn5S_N7z5x3-9AKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از موندو: مورینیو خواستار عقد قرارداد با زوبیمندی ستاره آرسنال شده. بعد پروژه شکست در جذب رودری، رئال‌مادرید هر طور شده این ستاره رو از آرسنال قراره بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103967" target="_blank">📅 17:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103966">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebf8f1007.mp4?token=JIm56kRyMwr7kT7P4-h3tkz3SyhDa-8nG1bwHJ8I000SF1xrYhC8ldjA3OdpEgZJZtRL2oMIXQHF_a38c0mezr2rghobB1c8y0PSZE5SNTB90FGxTxNJYJSKozRooCgPGSnNLeVceiwTsuOuNrA5nDTQLOeI_EBKk7G4u6jMp9fxfCgfpb_IhKAvxbrFtyf1zSQLvs23nH0XT3Tl9Kxn_X36e8xMWTeb2kERhYxbwH8xrh1JjG4Qj-GQcQZwPBenBa6OPqJOO-pLK3tLmZAPHIVvgA0BemjEvNPse6sivBhWBfmSjhoVQsNdJ_iGqnlYgcz_rFCh6P0ZZd_AaK-n7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebf8f1007.mp4?token=JIm56kRyMwr7kT7P4-h3tkz3SyhDa-8nG1bwHJ8I000SF1xrYhC8ldjA3OdpEgZJZtRL2oMIXQHF_a38c0mezr2rghobB1c8y0PSZE5SNTB90FGxTxNJYJSKozRooCgPGSnNLeVceiwTsuOuNrA5nDTQLOeI_EBKk7G4u6jMp9fxfCgfpb_IhKAvxbrFtyf1zSQLvs23nH0XT3Tl9Kxn_X36e8xMWTeb2kERhYxbwH8xrh1JjG4Qj-GQcQZwPBenBa6OPqJOO-pLK3tLmZAPHIVvgA0BemjEvNPse6sivBhWBfmSjhoVQsNdJ_iGqnlYgcz_rFCh6P0ZZd_AaK-n7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇪🇸
🇪🇸
هایجک تاریخی لاپورتا از رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103966" target="_blank">📅 16:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103965">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b51eb3cd2.mp4?token=gLMFINSLCIViYhfVUAScVlSgQ8e_GPd0_4cDma7cSO8tZNOqQwueZn02ZlPBxe4k9osqUh0DBwE0q8WWGx06wVIvNBEtEXLX-PinZFJBIh-GSxIamTsAzxufyRCA73m_0dfsSs9YE28JlhVZ5lPW_u_rsQ1IIx__F0GScGx4UO_q4BeJd3IUznYqfNxSYNfip8kqZqyNDUAfdEDYXKYsItqAdDXcKrc6xiUI2knirz61Q101-E2u2VBt6JHDM5LZvhzQnEslcA-_UBMImYggLvnKmRkrrwu2XJ_JvO7aM2EMZRx0XlwmBH2RffaU8aESParPCa4-_yZCYD73L0jonQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b51eb3cd2.mp4?token=gLMFINSLCIViYhfVUAScVlSgQ8e_GPd0_4cDma7cSO8tZNOqQwueZn02ZlPBxe4k9osqUh0DBwE0q8WWGx06wVIvNBEtEXLX-PinZFJBIh-GSxIamTsAzxufyRCA73m_0dfsSs9YE28JlhVZ5lPW_u_rsQ1IIx__F0GScGx4UO_q4BeJd3IUznYqfNxSYNfip8kqZqyNDUAfdEDYXKYsItqAdDXcKrc6xiUI2knirz61Q101-E2u2VBt6JHDM5LZvhzQnEslcA-_UBMImYggLvnKmRkrrwu2XJ_JvO7aM2EMZRx0XlwmBH2RffaU8aESParPCa4-_yZCYD73L0jonQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
بازیکن ۱۸ ساله و استعداد جدید بارسلونا رو مشاهده می‌کنید جناب جسی‌بسیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103965" target="_blank">📅 16:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103964">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca61d3191.mp4?token=oADdiz2g8UwAROzTeqy7JP8pTwuEg8zJEuphz5_peqs4QXmWBUGQCQeGzDzZG6nFQ8AY8XF2FxCauG3702t7rF_uzJD5NjRfMwcwBZxBDLrWE6YicW0dFUU37AepMPaaPHt_H7nbFpHp-LohlsqDywDxiiJH1aweGfWL0QnNirkbR4GX4zBhrB-wr6cWr6aYAL3I7OmwMia9XvWTAe292lFYS2ZOeETG5acQ-wT-rcvMLNcgdB5l7lPbcwISJDEMCwpWIJol-M8YQZxy_STaCzyKGyMXCY48ryjtvPNwaaZLaMA2tEzqt2FOlnAY01Bvp4vBNb2HmIvYB1SSoKDk6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca61d3191.mp4?token=oADdiz2g8UwAROzTeqy7JP8pTwuEg8zJEuphz5_peqs4QXmWBUGQCQeGzDzZG6nFQ8AY8XF2FxCauG3702t7rF_uzJD5NjRfMwcwBZxBDLrWE6YicW0dFUU37AepMPaaPHt_H7nbFpHp-LohlsqDywDxiiJH1aweGfWL0QnNirkbR4GX4zBhrB-wr6cWr6aYAL3I7OmwMia9XvWTAe292lFYS2ZOeETG5acQ-wT-rcvMLNcgdB5l7lPbcwISJDEMCwpWIJol-M8YQZxy_STaCzyKGyMXCY48ryjtvPNwaaZLaMA2tEzqt2FOlnAY01Bvp4vBNb2HmIvYB1SSoKDk6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار چادرملو: بخاطر ضربات پنالتی تورنمنت سه‌جانبه جلو گل‌گهر تلویزیون خودمو شکستم اما حالا سهمیه رو از ما گرفتن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103964" target="_blank">📅 15:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103963">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e6573bac.mp4?token=BO5szwKrKCidoqXKQ1YeuxofpbVOGE426wFgnyV1syBcFbRl26gldOc2_qKx1Ys4StxG66dLD5MUJRccn5_Dqbk2VE4UGe37VEqzGzoa6_EUAUPpocxK2zPTjXM3HuzqXGTMbXOdZd3fO_zR9Qih190CtYhvTDZJwbDlIMuJYqwjjGuDB7eQu6UWkxzlJOruSMmQfiWTSoreTRn63-Bsn0CurdrKLlmJ7GWZIKyyfymrhbT6Tch58iOXuM3fdNezffzwdn9M3C2D-y9gCBaZkL_BtzbM2EUMjf-x81b-scaSX9w5_jsCyEVIkxsajlAC12meVOtC7yWWzIAjMyphyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e6573bac.mp4?token=BO5szwKrKCidoqXKQ1YeuxofpbVOGE426wFgnyV1syBcFbRl26gldOc2_qKx1Ys4StxG66dLD5MUJRccn5_Dqbk2VE4UGe37VEqzGzoa6_EUAUPpocxK2zPTjXM3HuzqXGTMbXOdZd3fO_zR9Qih190CtYhvTDZJwbDlIMuJYqwjjGuDB7eQu6UWkxzlJOruSMmQfiWTSoreTRn63-Bsn0CurdrKLlmJ7GWZIKyyfymrhbT6Tch58iOXuM3fdNezffzwdn9M3C2D-y9gCBaZkL_BtzbM2EUMjf-x81b-scaSX9w5_jsCyEVIkxsajlAC12meVOtC7yWWzIAjMyphyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
کنعانی‌زادگان بعد بستن بازوبند کاپیتانی تیم پرسپولیس فاز دیکتاتوری امباپه گرفته
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103963" target="_blank">📅 15:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103962">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=ao23IXo-yqk5SJ9JnMZl4oFvM6i4mnYvwdL3mBSH3XRxFzYTgD-ieC9CcP_MskYWNQbBIOJJpC-SmKO5TYH6yoOI5IFv9jrqTxlybyVp7yX0PpaFknXTG6WbAj3IyNB0v6nk52cNG7MttbNfrcQCVHjpRCn9t-TOxO2R2pfd42KhMeZr8rkfh6GhHigWxpYodV01vhv6ofD2pmzxQghhRwhSl8Ftc8NQiYTjvmmrkOcLDCl_Em-JUvwyiLoBnSBXMH67dkZt74D1vacSjAmd9PRaEWCVwGTDLiQFi5VSuOgdiiELWGyTBPrjx_EtynZToFh7s2IGvO1iPUtPbfy9dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=ao23IXo-yqk5SJ9JnMZl4oFvM6i4mnYvwdL3mBSH3XRxFzYTgD-ieC9CcP_MskYWNQbBIOJJpC-SmKO5TYH6yoOI5IFv9jrqTxlybyVp7yX0PpaFknXTG6WbAj3IyNB0v6nk52cNG7MttbNfrcQCVHjpRCn9t-TOxO2R2pfd42KhMeZr8rkfh6GhHigWxpYodV01vhv6ofD2pmzxQghhRwhSl8Ftc8NQiYTjvmmrkOcLDCl_Em-JUvwyiLoBnSBXMH67dkZt74D1vacSjAmd9PRaEWCVwGTDLiQFi5VSuOgdiiELWGyTBPrjx_EtynZToFh7s2IGvO1iPUtPbfy9dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
خداداد عزیزی: دخترهامو زور نکردم روسری سرشون کنن. برام مهم نیست چی دربارم میگن، حکومتی بودم که بیکار نبودم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103962" target="_blank">📅 14:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103961">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQsv5_CqAPUAZ7H_n77jaw8C_R_gz-EWkNWh-JYMYoBHuCbTZ6Zy242vZHoxt34gzbWBKU7S6q9eCKYQw4wbnBCM8GruqY2l8Po-UnchLi-PWAc6gHzPggJOjuMEC4isl-GuFuzOLe0ShbfQu6kEc2G1Blg4pxT7c6rltHht_xHS8RhHSDRVUKzqvwCWHtwyHQYmsRg5DNmXkwKGLAWMEy-9UjHNGHgnWFNRyHbvl77qv1MZDnitDohtO5hZ7DwqEUqKhI8oThUlqtl-KVyryVy70U3DOzM9-vhW0dYZY1lE1ymEYmdI1lkbvqxEgT2gGYKm6Eps7Dfmer55RGAZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
👍
آغوش صمیمی کوین‌دیبروینه و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103961" target="_blank">📅 14:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103960">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLh_uO5SKRwV5O9CP_j_vtwnfPpnpoiSgOY49leKldo21K8v0c2X88Uvhi-PEFVdlAX_4uw20lEsm7v2uneyU2eFqVxEEpcp_oDHvtCz2et3_aLB7EcuL3DIk_PwlI8hNNO8Dag0ocd34EQLPIThkTl-EAGsbuSizWoMghN8I7quNWHjamoVElEgLiEiclLTe_lxsccqdZGeGyncLWw18JJjyRa_1UJ9vTvEV-340uN1KhhI_dPsp_xkxyn0SvUCg3QchHBG6Nml3o_Q9z0GH29JfuOwJBlO7cWUyIeOJ5MbW26rlwBYyFIImwuZadySfzxLS87ZsQhCz4KXS7vgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
افسانه، کریستیانو رونالدو، در مصاحبه‌ای با مجله ووگ درباره آینده‌اش صحبت کرد:
🔻
"کارها و فعالیت‌های زیادی در پیش دارم که به قدری زیاد هستند که نمی‌توانم فقط یک مورد را به شما بگویم. من برای همه چیز برنامه‌ریزی کرده‌ام."
🔻
"وقتی بازیکنان فوتبال از میادین خداحافظی می‌کنند، ممکن است یک خلأ بزرگ ایجاد شود، و شما باید وقت خود را با فعالیت‌های مختلف و برنامه‌ریزی‌شده پر کنید... نه فقط یک فعالیت."
🔻
"من آماده‌ام که بیشتر لذت ببرم، بیشتر سفر کنم و ورزش پدل را که خیلی دوست دارم، تماشا و بازی کنم. بنابراین، می‌خواهم به لذت بردن از دستاوردهایم ادامه دهم... و از دستاوردهایی که با هم به دست آوردیم. زیرا این ۲۵ سال، پر از فداکاری‌های روزمره بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103960" target="_blank">📅 14:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103959">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34552c022.mp4?token=vX0N99tdY2U1eabZSfbv3ldcenrgKtINJWBwbDWtjHTjlbdlhOu0obDL-m0S2gwtq26Iav6M6sAV2_3TB7cAaDRHLgjipfN_ug_1htUJBpn0u6cn-cl8QMPYWqcY1SG_EvV6Yc4Qm1mh8KsWOVcm3Mfe_6wGBwV9e7RMrthB_qtjiSmSEtvzSyMmfsl3zD-I9YiIk4xT321yZMYDnHHhMX7FoImF4XZu3VfVC7QV5Plslf6Af8HSy_yaoQqfU01yvIGMG6BKAaC-zMlUkGBaYh2M_sZ9-pfFLIxqOqD6cP2FXAYHtHK8Hpq4qieLfyVEFbaFE1lrvwpvCe8fpyPQdQx1u-0EUwgAwR60bv8QQSmL1eyXZjCYnqJ0eapUU1vPyaP0J3YOBw5nPCPcDZx1PZRRCQ2t79cGSwokECERzP03AFbHhFrBT6u9tF9RKZuGoH9aFX65ZMKwdBKmfSVXCKT_fVZPO0cxFXXTwGTyXrV4xQiq9LnSHiNp2RxqsOaAWH-PSg45dssIWKxiNmb1Om9jgNuWI1SqjcZoW-UWHLghkQeeojjb2irA2kFHyha0MWuA58r2JLSWKf590aFXFnfF-MgoSllnXscnODZ5FBsJq4sLsfGbs1VrEKscDndND5dEESQlK37MzW2KM5Mz1GdJ9lduwhZhGixcI7vRW4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34552c022.mp4?token=vX0N99tdY2U1eabZSfbv3ldcenrgKtINJWBwbDWtjHTjlbdlhOu0obDL-m0S2gwtq26Iav6M6sAV2_3TB7cAaDRHLgjipfN_ug_1htUJBpn0u6cn-cl8QMPYWqcY1SG_EvV6Yc4Qm1mh8KsWOVcm3Mfe_6wGBwV9e7RMrthB_qtjiSmSEtvzSyMmfsl3zD-I9YiIk4xT321yZMYDnHHhMX7FoImF4XZu3VfVC7QV5Plslf6Af8HSy_yaoQqfU01yvIGMG6BKAaC-zMlUkGBaYh2M_sZ9-pfFLIxqOqD6cP2FXAYHtHK8Hpq4qieLfyVEFbaFE1lrvwpvCe8fpyPQdQx1u-0EUwgAwR60bv8QQSmL1eyXZjCYnqJ0eapUU1vPyaP0J3YOBw5nPCPcDZx1PZRRCQ2t79cGSwokECERzP03AFbHhFrBT6u9tF9RKZuGoH9aFX65ZMKwdBKmfSVXCKT_fVZPO0cxFXXTwGTyXrV4xQiq9LnSHiNp2RxqsOaAWH-PSg45dssIWKxiNmb1Om9jgNuWI1SqjcZoW-UWHLghkQeeojjb2irA2kFHyha0MWuA58r2JLSWKf590aFXFnfF-MgoSllnXscnODZ5FBsJq4sLsfGbs1VrEKscDndND5dEESQlK37MzW2KM5Mz1GdJ9lduwhZhGixcI7vRW4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
۵ گل‌بخودی عجیب تاریخ لیگ‌برتر ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103959" target="_blank">📅 13:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103958">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d709f3b074.mp4?token=Qu4lXxMFUe4vFNXUSx5MNB-YlSMIFkWktFIFwr6B0KAvffKP20Fr5-wZQGAdsLX2q9PiaVMgVpKbvyykd4o3Rugo3WfLmZ2H88i52CEZrbwjSgbrbh2TKE2TdK4uNhzgJkbXbJOulqTbbmkCOOjzFl71x891YAITBA1HQGr43QZguj2Eu16kMHhP7Ewx-vjiOn9v8hHKE4Xe6_fniWmWMndN4WO8eK05HIQ1nBWGe75DQIO1qdApzw-l1zXQ96FhEXTetdZh4XmMZKMQUO9Tc30TS3RmNnhYcEuMlOO4iojinCzmZ0H6QMV9xxeMt6LFBMknF4INFIU6pGa3nwdNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d709f3b074.mp4?token=Qu4lXxMFUe4vFNXUSx5MNB-YlSMIFkWktFIFwr6B0KAvffKP20Fr5-wZQGAdsLX2q9PiaVMgVpKbvyykd4o3Rugo3WfLmZ2H88i52CEZrbwjSgbrbh2TKE2TdK4uNhzgJkbXbJOulqTbbmkCOOjzFl71x891YAITBA1HQGr43QZguj2Eu16kMHhP7Ewx-vjiOn9v8hHKE4Xe6_fniWmWMndN4WO8eK05HIQ1nBWGe75DQIO1qdApzw-l1zXQ96FhEXTetdZh4XmMZKMQUO9Tc30TS3RmNnhYcEuMlOO4iojinCzmZ0H6QMV9xxeMt6LFBMknF4INFIU6pGa3nwdNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بررسی واكنش‌های جنجالی به خوش و بش بازيكنان پرسپوليس با داور بازى پرسپوليس و شمس آذر دكتر بيژن حيدرى⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103958" target="_blank">📅 13:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103957">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAQQlfkluXsE8tl8Uqd9wE83va4Lpf-N1w12pTlTGY0R8kCzZsyyiMv04wDLF9MWZ2PFrwMw6djCFqm2lRmxXygeN3w3KX5-_VBAPtSyU-EzklAoMHcchPRUXXoo6w-HUFxdeNEXA_ki68LrFlf-lYX0tgRETHbxIt29LSyYVMgank6cPKTZDsMF_LBZ4nT44fl_g2Q9boJte_BsmLpIMDSkaM-jueOC_PlkTdzLJlSKGXPe_xwZbgoM84qE2joeq6HGG2_eaOt-QYkC9sOGwx61yE32B-B9i1VeVCIq_4h7fQaacbMtCRFb4Nq3xeq9zcbKyPF73ngKO9LyTrNLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین بازیکنان یک‌دهه اخیر لالیگا در هرفصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103957" target="_blank">📅 12:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103956">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHm6fElWLKZSrPy4LnObSdo7J8omoco6UPUav3T3QYeL575YWEgJ7UvUD5SoD_RxVRXbeBG3F_0Kf2shZsIhUfceiftg1lnWgtL_Pl4LRErRyFtRwjIywZrky6irJpyW44o8Gf_Jfcm9fLqFlhfdV88zoDUjrMk05JfB1pj-YdAqB3jH51Kx41kYvvcjWllEgdpqSomk7jOtWigcljbzjzIt0ogHtWbOvC1uhf_MnV9QQu0CVuXYDfNrGEVLg9YTA4yE8yyKMgSxLRlvBZIa3g-Ip6-YaU7aoWreW0Mb7G75nLEIuqPLe3cc6keQ73wcv0Mt1VMhqtTt8yVf6RuACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامه فسخ دوم یاسر آسانی با استقلال رونمایی شد
نامه رسمی فسخ قرارداد یاسر آسانی با استقلال منتشر شد. بر اساس این نامه، این بازیکن پس از پایان مهلت تعیین‌شده برای پرداخت مطالباتش، قرارداد خود با باشگاه استقلال را به‌صورت یک‌طرفه و با ادعای «دلیل موجه» فسخ کرده است.
همچنین پرونده آسانی در پنل فیفا ثبت شده و شکایت او علیه استقلال در جریان است. آسانی در این پرونده مبلغ ۱.۶۵ میلیون دلار به‌عنوان مطالبات و غرامت درخواست کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103956" target="_blank">📅 12:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103955">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇪🇸
🤯
پشماتون فر بخوره که رئال‌مادرید حدود ۲۰۰ میلیون یورو از فروش بازیکنان ذخیره خودش در فصل‌گذشته تونسته درآمد کسب کنه!!
💸
60 میلیون یورو از انتقال نیکو باز
💸
40 میلیون یورو از انتقال گارسیا به فولام
💸
20 میلیون یورو از انتقال ویکتور مونوز به لیورپول
💸
15 میلیون یورو از انتقال ماریو به میلان
💸
15 میلیون یورو از انتقال رودریگز به بورنموث
💸
12.5 میلیون یورو از انتقال خیمنز به بورنموث
💸
10 میلیون یورو برای انتقال پالاسیوس به فولام
💸
10 میلیون یورو برای انتقال اورتگا به استراسبورگ
💸
8 میلیون یورو از انتقال ویکتور به فیورنتینا
💸
4 میلیون یورو از انتقال گارسیا به بتیس
💸
3.5 میلیون یورو از انتقال مارتین به ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103955" target="_blank">📅 12:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103954">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVibQqUuILAefmgYyN9-adXGGjMsAZTCfSdIC-bUuF6Dg8jEOe8OgoNTiTQCNswa3DNDxLxEskThXRwuRduGboQPWFQavibHPE16TLR8RhIdfYksPcLHoZC5ozBgkCOwHJgzmDWJhHwanOiARS5iHPTk81iolC1W-FhQt0ZhzNkC9yexqVgF4R1IKeFus0JCSGZBw00H9RTIFotIbaGqfzUAy-GBDu2mQYJNRRXujXL2RqzveNDVF2Ux99wMS8jMOZFoBrTcRg22bq-nCkLJrA7DolOwiFnpcHS03-bo5si9ucyKpfRV2N6MOmNRdOX4YmPYQMcFijK-7NLshT3p4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر تماشایی باشگاه استقلال برای تقابل فرداشب با نساجی مازندران در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103954" target="_blank">📅 12:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103953">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908dffe6e9.mp4?token=XJLS1iqTHOGwQk83g9ewh75adNNHEFTk1_q7yDgFXRnsEBIuKmY2nvwr-0fYA4cL7ZWYJe0YXrHDyuOe3BfzO_8550R639LbNbDAHU5100WS0PHoVmmCqHI9EHhZBdSFLzuCKQGSWagmTEJt3KK3ne3m2PXjxWNe-IeUr6EyvKWd3Qm4v_6kdromrZq6YOsEsUw0uKaHtxiyhn3I6xPBuR3qdR-Jx0d7wSVkyJYBXXJ-6TW95F_-IyY2zvAxL_HjMLYZHcojtUSWEin7C0Rmsz0uncEus4vXIF3D-vEVw27I1ZG3qGFow4r7GGwle0ujqY6PYi_6Tw0VT1Xuk7NRDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908dffe6e9.mp4?token=XJLS1iqTHOGwQk83g9ewh75adNNHEFTk1_q7yDgFXRnsEBIuKmY2nvwr-0fYA4cL7ZWYJe0YXrHDyuOe3BfzO_8550R639LbNbDAHU5100WS0PHoVmmCqHI9EHhZBdSFLzuCKQGSWagmTEJt3KK3ne3m2PXjxWNe-IeUr6EyvKWd3Qm4v_6kdromrZq6YOsEsUw0uKaHtxiyhn3I6xPBuR3qdR-Jx0d7wSVkyJYBXXJ-6TW95F_-IyY2zvAxL_HjMLYZHcojtUSWEin7C0Rmsz0uncEus4vXIF3D-vEVw27I1ZG3qGFow4r7GGwle0ujqY6PYi_6Tw0VT1Xuk7NRDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇮🇷
سهراب بختیاری‌زاده برای اینکه ریز برا استقلالیا بماله از مصاحبه‌های فرهاد مجیدی مایه میذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103953" target="_blank">📅 12:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103952">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9760c12668.mp4?token=s-voo9uuV60_iaOclKGICapu7GQGxEvjDYgvHuM1FcUc73aaoXFpwEBN7QhwqfCM_HRNzP2mw6StnaEPN6zyi9hV-Or_RUN2JKW3D4rT6y6HkbxZfB-CU296_uiOs1B3SnDmum3dadGOzidoHKsgBFlJQ8pLm1OkhM8h_LaJkt2J3u5Am7_sv_a4S24q7OjgvcUprHmOFxbtxz24YdCtdEFOqKbE4y51LUFFY90bQh9TU7Eix5fsjY59IF60L2rOcv23r9Pa6gJoZowYgBP-sgCwlD-tpKG8BXC0KwY4imTAcOsYTEtxkWLS0M04r9PKLgiyqYMse0QowGdpl9fHEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9760c12668.mp4?token=s-voo9uuV60_iaOclKGICapu7GQGxEvjDYgvHuM1FcUc73aaoXFpwEBN7QhwqfCM_HRNzP2mw6StnaEPN6zyi9hV-Or_RUN2JKW3D4rT6y6HkbxZfB-CU296_uiOs1B3SnDmum3dadGOzidoHKsgBFlJQ8pLm1OkhM8h_LaJkt2J3u5Am7_sv_a4S24q7OjgvcUprHmOFxbtxz24YdCtdEFOqKbE4y51LUFFY90bQh9TU7Eix5fsjY59IF60L2rOcv23r9Pa6gJoZowYgBP-sgCwlD-tpKG8BXC0KwY4imTAcOsYTEtxkWLS0M04r9PKLgiyqYMse0QowGdpl9fHEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
تاجرنیا: اینکه من نتوانستم پنجره را باز کنم ربطی به کم‌توجهی من به تیم فوتبال استقلال ندارد
انتقادات نباید طوری باشد که من از کارهای خوبم در استقلال پشیمان شوم.
وکیل به من امید داد و من هم به هواداران. حالا اینکه پنجره باز نشده مقصر من نیستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103952" target="_blank">📅 12:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103951">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eecbdca57.mp4?token=cDU3rfnZirjSxvv7vU4oLJnrj6z1twl6DeVgmZaMjxeeeXwHpTVIKKhA3j-dykHydZ8JK2l_TJPRgb6-q1VjaNri2UYOtXIxQidDp5RFbeqk6j1i53uf6TOM1v4jU6LT9Vx5hUCHZRX2AmaqofKwIB0G5Ys7T2WWdWfJBlWXSn3YS9D5dkra_nXj12VKn8v19GLVQpd-z-wuP0tl0bk8JBMaeHXiMOQoN4lrbjW1qikdpdAUVKFtXNBYlcwH6BO6z4JTEshJf9D5dDptmFqE4Wg9vh3ED03bWfRccmU49sDetIrJ7wuw2cnu_phpwYBTwxVEK-8rirOGGdOTbrVdkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eecbdca57.mp4?token=cDU3rfnZirjSxvv7vU4oLJnrj6z1twl6DeVgmZaMjxeeeXwHpTVIKKhA3j-dykHydZ8JK2l_TJPRgb6-q1VjaNri2UYOtXIxQidDp5RFbeqk6j1i53uf6TOM1v4jU6LT9Vx5hUCHZRX2AmaqofKwIB0G5Ys7T2WWdWfJBlWXSn3YS9D5dkra_nXj12VKn8v19GLVQpd-z-wuP0tl0bk8JBMaeHXiMOQoN4lrbjW1qikdpdAUVKFtXNBYlcwH6BO6z4JTEshJf9D5dDptmFqE4Wg9vh3ED03bWfRccmU49sDetIrJ7wuw2cnu_phpwYBTwxVEK-8rirOGGdOTbrVdkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مارسکا بعد از شکست مقابل آرسنال: "من در کل همیشه نگرانم، حتی وقتی بازی‌ها رو می‌بریم؛ حالا تصور کن الان که بازی رو نبردیم چطوری‌ام."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103951" target="_blank">📅 11:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103950">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ba20e0a3.mp4?token=BiTRHlBpWZv1X9FpZOtn_PnR9qgbvOVQgzDwmk4MKVuS0Z7Qb_eoQeTVGJj-pU6Im-_dUWQM2g2AoX7nzn0sBArsB7UO_5q7tQullLAa1FrYg7E9FJ0hOdLFrweTHUdpGKIOI039aWq2qoN2OCgnHn6sbv5jKGyTqbIV3gg6b9CuLQ_gX6q4v8z1-Dvm5no1_05RMRAutqiHCR_wyZDAJCln8kTwkyFkUTcoFbBWgA8RSBz8-EIU1Nun7buzEx-MhAG9IXH5xsjVqYP7gfRoYL40EA8h93ZU-NlgRKEraApHNbgwUp1fQmW6t7hbygJkfqBTqmYoi-PMLIIqvdbnb79iD6zT9pRo1Q_aTriUd-n5hWKIzWaYBAKVMmvBGkwjonB58jmrwvWKI4tN_uxBwaFc64Qas7_IuAFiydfnQDk76_RJJUV4DHid0OYfjb3ZeozdYtCcJ3msnxPg8yVqFCfDEoTLbHyzojOC8uc6iuOcLQRKNVj_LbuNYPk25Zer0U1lACw_T9HUWQTPAJayZSEY6L81nICm3Lj8L8yt7b4yPWNJVfU8wR-sPgxnHnEDS1p8BHnVwLo3gBTN7qfCRx_3DymiqC4gkNIF-PNOUuBLbwmXf5nDLFba0nVUmaBfQoW3ji-PqDceLIQ2VJTf4TuvtFqUn_S2m-SQsbAxVDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ba20e0a3.mp4?token=BiTRHlBpWZv1X9FpZOtn_PnR9qgbvOVQgzDwmk4MKVuS0Z7Qb_eoQeTVGJj-pU6Im-_dUWQM2g2AoX7nzn0sBArsB7UO_5q7tQullLAa1FrYg7E9FJ0hOdLFrweTHUdpGKIOI039aWq2qoN2OCgnHn6sbv5jKGyTqbIV3gg6b9CuLQ_gX6q4v8z1-Dvm5no1_05RMRAutqiHCR_wyZDAJCln8kTwkyFkUTcoFbBWgA8RSBz8-EIU1Nun7buzEx-MhAG9IXH5xsjVqYP7gfRoYL40EA8h93ZU-NlgRKEraApHNbgwUp1fQmW6t7hbygJkfqBTqmYoi-PMLIIqvdbnb79iD6zT9pRo1Q_aTriUd-n5hWKIzWaYBAKVMmvBGkwjonB58jmrwvWKI4tN_uxBwaFc64Qas7_IuAFiydfnQDk76_RJJUV4DHid0OYfjb3ZeozdYtCcJ3msnxPg8yVqFCfDEoTLbHyzojOC8uc6iuOcLQRKNVj_LbuNYPk25Zer0U1lACw_T9HUWQTPAJayZSEY6L81nICm3Lj8L8yt7b4yPWNJVfU8wR-sPgxnHnEDS1p8BHnVwLo3gBTN7qfCRx_3DymiqC4gkNIF-PNOUuBLbwmXf5nDLFba0nVUmaBfQoW3ji-PqDceLIQ2VJTf4TuvtFqUn_S2m-SQsbAxVDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خداداد عزیزی: زندگی خیلی سختی رو گذروندم. با پدرم گچکاری میرفتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103950" target="_blank">📅 11:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103949">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9244a473.mp4?token=InVKfH_av7CQfuGa2QBnuMXQBcJMoTVFTpvMQ9PlPGRN3tWtRVriGDblIc62rtA0mtgTB04kOW3bg--5yBU7L3aVdJpDwVUeOwbuUnZlnx1R3inN7wgfKUfsQbm0ExeAxMg0e2ACgDXUAtMACvmRvlGu2ciyzil-BO240uwg_Sg_lPuPU3nNe5HLc9JfC1BM9kOYS_V9EMLr1l6oScXofSgazUCNZDtrG4db4DK-2GRE1mGpkI0Pm3T64rr-8bUEAe08szULRndhZe4ihkOxQ2CJdvxTalVkxnNRn25nEzg8OAWKlpDpfdKppLEZPqmeTDbmR6mugImMcVmW2Cw00A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9244a473.mp4?token=InVKfH_av7CQfuGa2QBnuMXQBcJMoTVFTpvMQ9PlPGRN3tWtRVriGDblIc62rtA0mtgTB04kOW3bg--5yBU7L3aVdJpDwVUeOwbuUnZlnx1R3inN7wgfKUfsQbm0ExeAxMg0e2ACgDXUAtMACvmRvlGu2ciyzil-BO240uwg_Sg_lPuPU3nNe5HLc9JfC1BM9kOYS_V9EMLr1l6oScXofSgazUCNZDtrG4db4DK-2GRE1mGpkI0Pm3T64rr-8bUEAe08szULRndhZe4ihkOxQ2CJdvxTalVkxnNRn25nEzg8OAWKlpDpfdKppLEZPqmeTDbmR6mugImMcVmW2Cw00A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✅
🇫🇷
هوادارای دیژون تو لیگ 2 فرانسه از این به بعد جای بلیت کاغذی باید شال با خودشون به ورزشگاه ببرن، تو هر شال یه تراشه الکتریکی وجود داره که حکم بلیت رو داره
تو پریمیرلیگ ایران هم تماشاگران از در و دیوار باید وارد ورزشگاه بشن تا هرکسی بتونه صندلی بهتری بشینه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103949" target="_blank">📅 11:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103948">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c1acd77e.mp4?token=kMGHo2hFbpFE3l43efAU6plg5k2cCYp9xzjR7GWwDA-SWuMLPxRsNToegdJ91WzaWV5AxyS52F3DLMJZpAUTNKd_mWtsMUCA6ST-c0P9LJReUC5-l6CtvPwgUt-UneYaRTMIeARamy8ATiwk1-qA8x8zYZ08xiry2lHDSKErrC9ewHaugWTgLt9ugEOZfVotPZoqvO_cs0rAJbysVoOy4Y1bCwehj-ZSxF90UXn3io7s6iz3sY91sz3ltbT8quK9n41NbpG5Pa4RPoQ-cWqAiN53KyNjKbaj4ExJlRzuKZjcJlm3A0X6RYJStF-ImSYIsTbkGIEEKIQSFq4ct6CLCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c1acd77e.mp4?token=kMGHo2hFbpFE3l43efAU6plg5k2cCYp9xzjR7GWwDA-SWuMLPxRsNToegdJ91WzaWV5AxyS52F3DLMJZpAUTNKd_mWtsMUCA6ST-c0P9LJReUC5-l6CtvPwgUt-UneYaRTMIeARamy8ATiwk1-qA8x8zYZ08xiry2lHDSKErrC9ewHaugWTgLt9ugEOZfVotPZoqvO_cs0rAJbysVoOy4Y1bCwehj-ZSxF90UXn3io7s6iz3sY91sz3ltbT8quK9n41NbpG5Pa4RPoQ-cWqAiN53KyNjKbaj4ExJlRzuKZjcJlm3A0X6RYJStF-ImSYIsTbkGIEEKIQSFq4ct6CLCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تاکتیک جالب دیروز آرسنال مقابل سیتیزن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103948" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103947">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103947" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103947" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103946">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJYjiML1DAeLFbhJ7tTosCVo84DbwE5BA8Nn09MbHyQqHnYNFRA_1WSF7GEcCRSGv26LudbKKmF1-1wJnn77zZd0Ht-p_c8ATcG0_vL1A2EOg_Q6KBCHmz3Gs9ygjtGPQkMGuKw21yYyKDdqGpWfYD_gffiJN28oaTFX2PglksTB-IwxD789g_FC3p-JiGJLQQ5NhEc7wz6JbkJj7AfMUh9cVNlkys0K6IB6TW2_kb4nkjun_32_tdIYc71ezj_7WBIwnjRDNrIKg3aF24BrAx6BEnFR0-71yjnt3dexIxEJiCRrgKibMinrjpw51prLKU_vrj7iSzgpjMZuTsJwqg.jpg" alt="photo" loading="lazy"/></div>
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
r26
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103946" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103945">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1OsF0Kr4ODpd-NR-BMhwyqhPArqROjMrdTwFEox45I3G_UrN6KiURez-LdpRg3_H9FXpx4NIIqlbZnM6YNE1ZEAvCu4IH2mRVY8ik85_VQ36uGa6lIrwvDtM-R51YK9If9422fTFmtKU0mkxpbWordyi22vEdbqXXleqRCdvQwJMrcWX6hW7ElNqpVbwKZW5LQZONZQrMnSylKW9TMYwdHkv-PU_nqw2glP93gxFkIwYcxrZJpyp6lqiM1Y3BZYcDa5h4bkzjudws6mTERNUcpggLSlXHpxr8yFEu76bLqhAIKr7ICplFf8vmySMSo1F9uWTOd9PP6x8ul_LK4Qyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
رومانو: ویکاریو سنگربان تاتنهام به یوونتوس با قرارداد قرضی بدون بند خرید اجباری
HERE WE GO
✅
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/103945" target="_blank">📅 11:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103944">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f807afbf18.mp4?token=po6OjW6DWLple3ccMvGlty6lNk2xdX9riJhnqzwtUOB8oeXBC6sQc2I8fpmc6WeuDxucxxOrBypLXdxDzs651JU3p44xHPeVy2LoCeSXPRaoK7gkX5n8seMhayLEHQ0dC8NXPTeoMisoOGLGwuZgFY3ah7Alkt92ay3SwvZbFd-L6bb45FyCh5f-gTQUlSZ5hQt259lX5QPQ35oolNHT-LVY1c6BIDI6EKh05yL9H9obFn8fRjAKOm3qx4X6gqWt4pYZEFT5nlBEA1RCQ_eH-hddBwiLoPLb7LIRtWKPBHZg7wTGL0SOrwA-m3aUmQUrU2jaSFeiy3dKTOwYdSJC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f807afbf18.mp4?token=po6OjW6DWLple3ccMvGlty6lNk2xdX9riJhnqzwtUOB8oeXBC6sQc2I8fpmc6WeuDxucxxOrBypLXdxDzs651JU3p44xHPeVy2LoCeSXPRaoK7gkX5n8seMhayLEHQ0dC8NXPTeoMisoOGLGwuZgFY3ah7Alkt92ay3SwvZbFd-L6bb45FyCh5f-gTQUlSZ5hQt259lX5QPQ35oolNHT-LVY1c6BIDI6EKh05yL9H9obFn8fRjAKOm3qx4X6gqWt4pYZEFT5nlBEA1RCQ_eH-hddBwiLoPLb7LIRtWKPBHZg7wTGL0SOrwA-m3aUmQUrU2jaSFeiy3dKTOwYdSJC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚠️
‼️
دختره همچنان دست بردار رامین‌ رضاییان نیست: رامین‌رضاییان ازم خواست که عکسای لختی بدم بهش. دقیقا میخواست مشابه کارایی که جفری اپستین انجام می‌داد!! درخواست سکس با دوستام رو هم داشت! دعوتم کرد که باهاش برم پارتی و این چیزا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103944" target="_blank">📅 11:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103943">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCI9shVgECh4hpPl8ntESndC79MMXoPnh5uUYOLYuaHTYi1taMNJhrNMtnmJEK0ElKROZXEw9-JWVUJ-_z6S8nLxK6gMu0CEiLQsweL4_dfj0sDLqE-t9PHu0_GvreG-FRJ_CZF4KKvzHpTIixrvpsKpriXrr5CysEsArTJjtsBu16L-XVfSMfTd0-RukjNfLyLOV-oVlyS_8Jo3UzeXGBOhXLAc_RGi4moxXligqJAkV-44l78MJ1T7LSZZVGXCaHClLx2qqRsB_HPiSxJ0rY4rtDTae1hwJeeGdu7V7wOyI9yLNcyqJ1Z6bVRUg0gQh9LOi6GtEn6aVswpzsDyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از شبکه الچرینگیتو: بارسلونا میخواد برای جذب گیوکرش از آرسنال اقدام کنه! گیوکرش گزینه جانشین فران‌تورس هست و هدف اصلی بارسلونا همچنان جذب خولیان آلوارزه
👀
❌
برخی منابع از معاوضه این بازیکن با ژول‌کونده خبر میدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103943" target="_blank">📅 10:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103942">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2151ad88d8.mp4?token=ticsQ72IV-A4CD3fAlwRzflj0pPMzFt5b6_be7wBwB3AvX9sRRJ13SguDb5M3yl7q43w4GN2AXCdbjIFu9WO19D5k5GoAP8m-6-n27wLinQq6xj9qd8ELv5HzWA8OZAVo7XbTB0l_3zjGpBN5SvLqJuMYX1RVg6KttcZ3Ui9DM7fMkpEahtf3V8L-_h5pQggK_Do1aXKr7Rim4UX0GHjF3tf4_91GHGG-oncaefAW_CdR3fFUxEZcYly1FRY29TGn8olF8XwWG9C8bP7kuX-fw0rXt7wrMnRSr_fI5tLjkWLTwJAwsL40LUH7nh2ITW7R5Lm_sfTUleylsXmKs1bEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2151ad88d8.mp4?token=ticsQ72IV-A4CD3fAlwRzflj0pPMzFt5b6_be7wBwB3AvX9sRRJ13SguDb5M3yl7q43w4GN2AXCdbjIFu9WO19D5k5GoAP8m-6-n27wLinQq6xj9qd8ELv5HzWA8OZAVo7XbTB0l_3zjGpBN5SvLqJuMYX1RVg6KttcZ3Ui9DM7fMkpEahtf3V8L-_h5pQggK_Do1aXKr7Rim4UX0GHjF3tf4_91GHGG-oncaefAW_CdR3fFUxEZcYly1FRY29TGn8olF8XwWG9C8bP7kuX-fw0rXt7wrMnRSr_fI5tLjkWLTwJAwsL40LUH7nh2ITW7R5Lm_sfTUleylsXmKs1bEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
خط‌حمله وحشی و حشری فصل‌آینده psg
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103942" target="_blank">📅 10:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103941">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPjntqq-YX0Uy-TbqPiPkPV8FTuVd7cRR_pcTCGOs7RvIrOwJweI24tZFhN3QEIzfy2a9SbV2gsL9k6OI0a8gwCBz4PmQhETsdlNszAcfElRuv6oDey6Beoj7ddC3BA6jZGFORzW4XK5U6mW3IVPW3uqZrEpLV4UDiHcs7U0q5eb-CAXkhXDVZfJj0ITQ72GcwMG6VvY43LBMaSPiq_q7arZfC1qgH2IMbb4zO0OqFEB-QNtN1DlfBDPw_vJ84ibxtbZLlWDL8JdietR-yBXMrQpkZz0cJ8EQzmmJ40NZjTVDvUUoA8O9PZF_awOLzu5DtbaIFow55g9ec1SyCSQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
🇮🇷
مهدی هاشم‌نژاد ستاره تراکتور بدلیل مصدومیت دیدار با پرسپولیس و سپاهان را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103941" target="_blank">📅 10:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103940">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdbe4bacfb.mp4?token=ImNQvLQJickUkZpdvpk1ZVyEAM8Oak7Wmo8OH_ezw5_Fy_wfNPw8r9D37K1gCM4gt-iNuheicdONmZ0OaTb_ZCaN9rJ6ah2V7StTmnCddITGBzkVA5sGS1lXZML_5PCA8CCjpl8VtZKooemgyVCgOvzyRXOfxMLorl4PUoQea9lkE6AtW79hYvB7U4ljcZOO1MzpCIB1PjJRl5aD3-XpYPXY-ODxoeEHw8hBo4lZK0DOdtA3qsJDn9kKgMThuTYuVz-yhEUJrsPN25wSNMsv1aWbHew1hGHzf47Tzq50QanQXreBx6XU3SyrU8e-oROVNMip-MXa54p7AZkhUQPWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdbe4bacfb.mp4?token=ImNQvLQJickUkZpdvpk1ZVyEAM8Oak7Wmo8OH_ezw5_Fy_wfNPw8r9D37K1gCM4gt-iNuheicdONmZ0OaTb_ZCaN9rJ6ah2V7StTmnCddITGBzkVA5sGS1lXZML_5PCA8CCjpl8VtZKooemgyVCgOvzyRXOfxMLorl4PUoQea9lkE6AtW79hYvB7U4ljcZOO1MzpCIB1PjJRl5aD3-XpYPXY-ODxoeEHw8hBo4lZK0DOdtA3qsJDn9kKgMThuTYuVz-yhEUJrsPN25wSNMsv1aWbHew1hGHzf47Tzq50QanQXreBx6XU3SyrU8e-oROVNMip-MXa54p7AZkhUQPWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇩🇪
گرمازدگی جمال موسیالا در بازی اخیر بایرن که با خوش‌شانسی خطر رفع شد
درحالی‌که دمای هوا آلمان حین بازی ۳۰ درجه بوده! واکنش مردم جنوب با دمای ۶۰ درجه:
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103940" target="_blank">📅 10:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103939">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=QLXF6id72LBIFN15CmduQxhC7Xof4tw5XEisBgNFp9i28oFLWAVDbQvl-x4y14hDsOqPDeVhlH74L9iu7Sg7EnSDXPkHhb41btZ4pwei7-sJTqoK3Kc6ijMgCqH-sAsWxnpdW014zSnE6GY5TO15pdQr9hxQ0nZx4k4qoDc7JJF-N-6R_DcLHFSYFliapYh0hHdRZiojRMmLLga_1RITB5Hl7YDcS_L1xEcpxQv1lR-_lI_qEXGuKLeeSmhhSSeYCgCK_2Gt6bdezw5QALTIUJ3AWYMBymQGvtDFeYr3J5qP1YNrWMiEwPH0w5z_PuqDasUXwWVICRawZLyPBJJDhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=QLXF6id72LBIFN15CmduQxhC7Xof4tw5XEisBgNFp9i28oFLWAVDbQvl-x4y14hDsOqPDeVhlH74L9iu7Sg7EnSDXPkHhb41btZ4pwei7-sJTqoK3Kc6ijMgCqH-sAsWxnpdW014zSnE6GY5TO15pdQr9hxQ0nZx4k4qoDc7JJF-N-6R_DcLHFSYFliapYh0hHdRZiojRMmLLga_1RITB5Hl7YDcS_L1xEcpxQv1lR-_lI_qEXGuKLeeSmhhSSeYCgCK_2Gt6bdezw5QALTIUJ3AWYMBymQGvtDFeYr3J5qP1YNrWMiEwPH0w5z_PuqDasUXwWVICRawZLyPBJJDhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
آنالیز فنی بازی هفته‌اول لیگ‌برتر میان شمس‌آذر - پرسپولیس توسط محمد تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103939" target="_blank">📅 09:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103938">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0698ccdb66.mp4?token=s8Z0u6WaexaMkNceSwKshfTe9bZHkld5yxyIEFXJ-a2Q3VD6r7SrbuxzNMpJEOIKYe0Q1QK9ZfPW4zVC2KB0K6zpr5Iv0Q6yocE3-qmuyRi0SmLDtE5zQ7yHOrHAKuGdp4OpQBqsnemOOqVLK_-xhYbmgp-6MKck4Q1F1CGp4311-6oCvmL5KLr1wmyjcZgf9ld9HU4XCfQYxI1WZQyiSV8QXUHT9Tbr5IN5QdcbCBpX5SZVReKzrvnt_P-IST5MVzyE8a3okkhzp20kiPiDqiKgFoByRJbSKkDBe8K3sWDqII_S1Uf6f9TsHedGHiujNx5Gj1wTnJZlMycNrOMKSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0698ccdb66.mp4?token=s8Z0u6WaexaMkNceSwKshfTe9bZHkld5yxyIEFXJ-a2Q3VD6r7SrbuxzNMpJEOIKYe0Q1QK9ZfPW4zVC2KB0K6zpr5Iv0Q6yocE3-qmuyRi0SmLDtE5zQ7yHOrHAKuGdp4OpQBqsnemOOqVLK_-xhYbmgp-6MKck4Q1F1CGp4311-6oCvmL5KLr1wmyjcZgf9ld9HU4XCfQYxI1WZQyiSV8QXUHT9Tbr5IN5QdcbCBpX5SZVReKzrvnt_P-IST5MVzyE8a3okkhzp20kiPiDqiKgFoByRJbSKkDBe8K3sWDqII_S1Uf6f9TsHedGHiujNx5Gj1wTnJZlMycNrOMKSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
دیشب تیاگو مندز تو بازی مقابل سانتوس این شکلی نیمار رو دایورت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103938" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103937">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyrc83iLCT-kvf8RlAXdODNZK-HThTkH8VMkP2vPD4KG5azaBkq0vDjgcE2nkuOYch1GbaQyw7LfmjFyp2NFZGAwrHQT_I0w4oz1nAPpyc3NKyyiS4BVjkCoHlPRb6WoeSJRBfC-IejfeYZRPD_WR7hhnr9mRWLXgTsBj1SYhomZNY2QBvb9VLilydWonjS2rdzxvHg-v_RAPPkjJdhHkmYEg72Yp_PjuYU8BYVOzyUtS1sT0ERzmF_CyuJSlINBXHIwH8oXtLegTT9eiWkLwZ4fKVcCuwF6Wxi6dm7WrLUBKzwKd1xpp9RD34ZpxHg9mxMx5aJW1uiExPNUx7V3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
سرمربیان بزرگی که در رده ملی فعالیت میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103937" target="_blank">📅 09:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103936">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZRgIvVviU2AyrPp2E-O_9J7RfXJ3apjpS8MhpT4q0KBGPGrad50g8Tg1MkVAC6DJkfP8CtRGcpK4WHGyQV0wbOFaBfM5GuWSixRUo-_jJznqtJRE9DSbSSb_n4HxjXlamSSWYRAkc_XpqdjjpLBSw4xJnEnSwyjH5I96TD8MoNo90_pHW9yrNpxuWHOmUlsGDVZP2VSOKHNc3no_D_1ou_eTTYtgUC5_7b-xg2W1gODaKHO_dgFNICwJb6JVZTHNRvFXses15R027vOM0uOughmBZsuyV9VjbOTUMf7MybStayNj3UsO8bWWDBN-UT_qXEzYPECPodFMhnO3-BCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از شبکه الچرینگیتو: بارسلونا میخواد برای جذب گیوکرش از آرسنال اقدام کنه! گیوکرش گزینه جانشین فران‌تورس هست و هدف اصلی بارسلونا همچنان جذب خولیان آلوارزه
👀
❌
برخی منابع از معاوضه این بازیکن با ژول‌کونده خبر میدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/103936" target="_blank">📅 02:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103935">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccba4b58f.mp4?token=MTnClMy7t5fpJbRaNGgSLeoR5x21mafc-AaWra8NLFNb6G-RqfCZE25WV4CqLJFwzvUA2fR_vReOC-Mpe4KeNsvbQr7jGNLfFV1AKiVzP8H_cSEDiSI8YG3bKo7t_k96z_A5BRSnZzPoj01keyXnFDjAcG0auink0x_c8JrmvHbWT62GEWOB72Dv_92EAkeNTezAyeAPAy1JlrS9C3Uuc1DTB-vwFjz8oMY6e-1jxnOm-r4xjgXwBB5okyiaDswr2L6D_W444yzPaMr71farHC_nWIV_77hK9nI09nUqN4n3_r_pIKKkKhUdGUUgaSaEFnU6niYEFF4fxfTBlLq37IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccba4b58f.mp4?token=MTnClMy7t5fpJbRaNGgSLeoR5x21mafc-AaWra8NLFNb6G-RqfCZE25WV4CqLJFwzvUA2fR_vReOC-Mpe4KeNsvbQr7jGNLfFV1AKiVzP8H_cSEDiSI8YG3bKo7t_k96z_A5BRSnZzPoj01keyXnFDjAcG0auink0x_c8JrmvHbWT62GEWOB72Dv_92EAkeNTezAyeAPAy1JlrS9C3Uuc1DTB-vwFjz8oMY6e-1jxnOm-r4xjgXwBB5okyiaDswr2L6D_W444yzPaMr71farHC_nWIV_77hK9nI09nUqN4n3_r_pIKKkKhUdGUUgaSaEFnU6niYEFF4fxfTBlLq37IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
💥
ویدیو جذاب از مراسم ازدواج رونالدو و جورجینا؛ حتما ببینید از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/103935" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103934">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgFAO2RMmMe7O7k1TugBBTvQuCg8psVPhb8pgwNsnJovgsdgNkeQRejA1iReb7mczvsBi5-puFhn9VRKpD1p23MEcrNIPsblsNJNaGvN1QU8AWEI8vDMVXzipwjZs-37EuH8dUqJCXv9u8GfRKwQ9fLPvAidbPHJqHBmU7UQz1lziNvYNFbzIo34Mjk4zCjPopFauVjIMbEb-j6wrD3crfCSoJ9m0sf9-yUD6vHoaDiH1ncXuBbZiYJqHuxn4m42k1Eu-LMMXpVokEWeP8K8BY8yKUeYdXnOP0qVwV1Tqsqdr0uEA_hg_HVYE0QNXZbQjvODnsprIYkT94_WRVPhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
🇮🇷
باشگاه پرسپولیس: اورونوف هیچ درخواست خروجی نداده و شایعات منتشر شده در ساعات اخیر اساسا کذبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/103934" target="_blank">📅 01:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103933">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
🚨
🚨
🚨
نوید محمدزاده: قبلا هم از فلسطین حمایت کردم الان هم میکنم چون با اسرائیل حال نمیکنم. مارادونا و رونالدو اسطوره‌های زندگیمن و اوناهم طرف فلسطین بودن. من نه طرفدار حکومتم نه طرفدار شمام فقط طرفدار ایرانم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/103933" target="_blank">📅 01:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103931">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7dPQ844SrvyH7onyJSFtWWF_sa6wNB9EuXTFcsSV0SZIfN-j26_BXt3eCZw5OU3mWDFMXoYANw2kPh7zmO0NQoZOTcwj9OC2WscRRfcw5yBjiHXJFP8_P8_hgi-oFJo9BGAUMOMTJvS9vrnRwvMGm24gazJYd_qqqXBFvev1kJRGdyoHaiS7m30BJW4swh-Ma7bUq12TlPDAQZsFwOKY5-K-9K6KOYdWIGO0jdJoZ6nvui_dcqMG6RHC-y0ggnUzLjftCK5ADqi5f6C6CjqtkQI1zPhp8T4VBkavj5QxNIKxhW2moS9w5G0N9og8mBv0uYAwMcvB_Y9oAbGWKZb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3d3UWPj7099CJY5XjAwEQdqXYSp6pmcmkhfqYLEAweus0ndXDo9zcCf0XKWydZkBviOUVLAFFTfHxg8yO5-9xzfJXEAUY71sSyLVNzxeAgt75MxyO5m7i0ZgFpdzbTzKxQc8i9qXZHxvOB7LzcboMtvWFojy0QS-MihhmjfxeN1Z9fEQiYMMi9kdzBAnZgk5uNtke8tIUlkSMPwCiTBUIOaiZR-UQxmsdejj4DMyk_sw0dWJ2uwVwNnFy3UU5a7cY3kSRg88VXUJWOkBD72rmVFZMmIGL1uqRJLTPIm49HiTKkJNbOlvQvG-38FtZQfZL-7paeIO3hghNOKcjj0HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاپ قهرمانی در دستان بازیکنان لانس.
❤️
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103931" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103928">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQp52RYctncY2IFw50RsIXk6d8trHcEGukn11XgQ_bDp7gqbPDfiCK7X9ptP-zdA_Pks-K4w8mQsirjpJs3t48Xj1UQ7Bz5ReYSiwxhH63FuvsxMe6xprOkA-I3yXbCWkZ_ZJ_fFkob-WBAIS1mhSz-VVOIqd8Kk8q9Am5yZ3knTVgmC_13368KPV_1QNEhko0M9fMUfX3XvoGAJBxMuhoYVxjtxvPnAllZF28gxYLCOyDvlZdFOLVH9bVhokBWpCd5-4bx3FbG8oDQF2xk83Ev-HOHDtEAJafDfdHuBH3Zx8bd1Qgye77_lb534gJKstNeSayTB47KywTRswiYgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
سوپرکاپ فوتبال فرانسه؛ ۹۰ دقیقه تلاش فوق‌العاده لانس برای قهرمانی؛ تیم وحشی انریکه مقابل حریفش آچمز شد و جام را از دست داد
⚽️
پاریس‌سن‌ژرمن 0 - 1 لانس
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103928" target="_blank">📅 00:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103927">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103927" target="_blank">📅 23:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103926">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/103926" target="_blank">📅 23:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103925">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103925" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103924">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLsQI0-QHI61tIYrMgh-LSs8dFP6Ny6S5E3VfCM8kzxCPI_7a77HWQkglvEPflpazS8ndU-tBOr0o96BV6iCHX2-cQvqVbGNxm29K4q6w9DIWa0q8zJYCSmErDmZ_4_PJjo2zFSbAq0EsWVwa49jXtQMtOxj2b9ZLITltRQ_ClCjHZHw05oaWuSYsO48IPk5SQDy30KeiW7KzWzz9q8k7PJsEACrfAj7TE3sfe02Gu6MKiyNM8wLLdXHDlo5YVgVoKePX-PUw7eCYhgiHaZy2tF2kRBclmUuEwz_KKfED9MCkNRKFuj-WA96ZTD2r08FH3SPL2wmf_YJflOYGov4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🗞
🇪🇸
پوستر دیدنی رسانه 433 برای رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/103924" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103923">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2mi8xrXqN-rXuxDb9i9gLzLA6dG9y3iNHSIEBLoB8ydSKu3f4A53qX9KM1YavPuTtTm6Z-DQq5QwL54oph01d1v6VE-9peVSDhU7dOKfOEdE27tMpeBXVxsGXb4RUVYnOQhRz9lRilbP_JHflF7nF2yNetIa8shF2tj5zMg2n8BkXlVi93z7Mj4zuBRYsdTPxTKB-edKKMNt81nZx_U0nUGWKS9WRZtEwguw08goQM4j9Nzhr6vl0Ngcj6puW2nzbGuGP3Qc6b07zJK_6_-BBUvGEDdWVVzEgE8449rg30O_fstfmblgXfNtpidII2fqUjVcpmoD3hkL5NFLTyYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇪🇸
#فوووووری
از جرارد رومرو: رودری فردا دوشنبه وارد بارسلونا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103923" target="_blank">📅 22:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103922">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103922" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103921">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjE26P_w6tL7__uasSkSdyoTz0EWWm4iSzSQwsj74937a5mAzNDalR2Q12SSeNEz-SGVRbE2ydzi8jVOwSee2nKDKp7OorfxrhgWU42k56nCjqKkeXZlQ8673NJ43dacy2YBV7lwYpcS9KVCWWKzSzBG4fjJGfFSl_EFielVWdtyICGpMtZsGK6BD1J_9Wh888PGEakIZLPJn5mBRiYGYRV13NMLRyrly9S1IvImYNLFP87AnGygAkWTm2_OwvBa147dIBlDFn7H7l4Fno-4oIrNbi1tqdenoDKTGQN4XLPNkyAmxwsKOVPo9eg6FsfAdHCw2MNOjLarSkEeUIBa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
مورینیو درباره بادمجون زیر چشمش: نگران نباشید از شوامنی مشت نخوردم. فقط یه شوت به صورتم خورد که اینجوری شد
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103921" target="_blank">📅 22:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103920">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/103920" target="_blank">📅 22:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103919">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103919" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103918">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103918" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103917">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqjqLlrse_nJ4DiAewu7rWba2n5AZkdXUkjRgI4HD5zpwFMhKimVngc7xWyyB2GWSrPjh-7SO3HNx-q0T2kC992bpW05Z4N4oIquqrnAnq1B99cGhDDlyLY26dfi9igetWulPJYB4em5VQSFOkodWhPVIcrw6fFOGNJtF58ms4YoGCW7SGdW8hRJ9eNlQTND-lE2rIgLuxG0ps8h1yO79HrFFLOTnUg8C_n3LMQzVt6ihMOtRDo4pgMdO2TXREFQTLCQUwwsBqiN5v5_qBH3UMUetqwZzmrJeZpd3s6kdfzZWcYfpQY6DGVxHqDDsgfb84NSXIMbRql-XvqWo687xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرکاپ فرانسه؛ ترکیب پاریس مقابل لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103917" target="_blank">📅 21:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103916">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103916" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103915">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103915" target="_blank">📅 21:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103914">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxmnMVg90EDuGfM9WmMG86K49DF031066PHuqhvnOQ3iJbyUyvipeeiDYnAxKEfhu_O2490-RgYLKy9o9pQSdGbY-hj1ebH14lrPb3X4zxxD3eMoP9HMGQIIySzI11RyEhQmOFRji0qV3faIEMwhKvz4Iprm454EyTLHUDgiHI8SOqE8rxuHfFsuJm76M5zIpdh-NnpLaUzLv8TEifiTtNUCgZ0NNJ0KWt9bnCT44g55U1EPkXUxL1uyuVJjKSlogBa8eUk3dqt5r6VPvYG7Nh46fR6MS9fWEylMqXKdvnpZB1L55juOSDOptsyvTwBbVr-TK6LCrvPbEFGno4qcVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103914" target="_blank">📅 20:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103913">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f160aff0.mp4?token=Izq4lnuoHH8Fav_o7R58mTc_0wVSGpoSgu746LrChv0x50qlpykLf9UukcTyHH1SKTQa99SG6fGGXOHbBvwaN394RzEFxftZj9tQ68vjl2BnMwy1A-BbRaEB0-5LlcRsvSeRtJrNjTFYHPwBcUxVTn1HMaBySV4kIwAmzDtfEH8AspEr6OhNqBicS-Ko3QwLBT_yu259EZuXdbgcEm-WVe-uiwTRUV2qz67ebzcCZN2cHiu0Y0u6Pe3LSNN6pDl1qmnU95g347k1xh5EQu39dF69ET5uk06hUhhyAwquq93DP3xhCitM1_egn-xH2zXPtl4vXkZYssn72010hpEZNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f160aff0.mp4?token=Izq4lnuoHH8Fav_o7R58mTc_0wVSGpoSgu746LrChv0x50qlpykLf9UukcTyHH1SKTQa99SG6fGGXOHbBvwaN394RzEFxftZj9tQ68vjl2BnMwy1A-BbRaEB0-5LlcRsvSeRtJrNjTFYHPwBcUxVTn1HMaBySV4kIwAmzDtfEH8AspEr6OhNqBicS-Ko3QwLBT_yu259EZuXdbgcEm-WVe-uiwTRUV2qz67ebzcCZN2cHiu0Y0u6Pe3LSNN6pDl1qmnU95g347k1xh5EQu39dF69ET5uk06hUhhyAwquq93DP3xhCitM1_egn-xH2zXPtl4vXkZYssn72010hpEZNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
دیومانده در تمرینات دیروز رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103913" target="_blank">📅 20:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103912">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn0wb4O0O2vKvKyhc-KuqMPq3H9cTE7WN9dtJTODNdO4X6AFxVrZL-JlZbaMsxWw0ZscTnKGwf4tyRmUPNScq-fMIgCumJTBZkoGIwZMnpAkgK-4nwf6VcQ3CGDB-148MVKzoXl6jq1QMh87bepZaTfvt3HDIxZD6TBZ-zobgD9dzUxk4o2TMCLJ7Nrrrb6jpFs4B1A7r6Pma1tSeW4IFN5_QTtBew2xdvboho9_yNw1eu-qfy8E041RgyU7Wd9ZLBxQQDJwBAac6tP107M4TGQGYzhKG6f-GIUgFsmWl5EesNpXst_22b4LS1sA8FqXh9NqOIDIs6oyCWBLJKJzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با نتیجه سه بر صفر مقابل شالکه به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103912" target="_blank">📅 20:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103911">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
⚽️
بارسلونا در یک بازی دوستانه، تیم بازل سوئیس را با نتیجه 5 بر 2 شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103911" target="_blank">📅 20:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103910">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeT6S_1Q4PMTszjsn_yDCDNa1YwU57oKECkuIB4PgHBmx60c9tfonjgAmrTw2Mv_-xKS4TMWN8jYT9QRg3cqUtsFMMyQBy4ok3ZLUYYTXNrzaTEHu4d5C6YurO09WOl41eD44BONk8v_NYuuhkqYg_dMf4Vbb2mbtuqc4FLGgqGKmAM4_eUW3h-mUdMemXksb5ZNpeKhNi2zFMUHQvbZHEoZ3loau7nLEnStaTmJV81U7aGYkd_XL0YtYCKg-IlOSgk_AjqkIS5o1TgjCsvjgHTluGbc6eOHhk5ve15e5yYljqZcwKh45EmoXn3L_AaoVJtj0P2XtUvvizL-2EK0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
بارسلونا در یک بازی دوستانه، تیم بازل سوئیس را با نتیجه 5 بر 2 شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103910" target="_blank">📅 19:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103909">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU85zLFwurKjDakvr3nGZf6UW5oNhuFeG_Ty97xaWBO6UTtEliZIaF2cyEUm_s2kZt4OHzsLKwRIcx115WpRZW6dpZJFZyxtyneUzuALBX-LrHmz6_3ks0LBpyBpPvLOO8WTHaNxD8ZY_lTfaRSMy_ju21KUoXOQp9IW4Q2oUvdv7IuslAO087YrycPae5IQpWTim-24pXOIM02j7XaafIvFnDuGukEzUY8wJRzMGv3UiaWoA7N5w3dsOkYCRPN_Lfd8bYcO71JhDS2auGJXop3BKhiCgaSTl8pu6ICZzV8kYKQVCzCSf8cnTlVd5ioN3Lzcwgas6G3cVbtf-konBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103909" target="_blank">📅 19:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103907">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr57o1f-h83M_Itfl5x6wo_AtjW3-5Q79s-XxFhJ9lwzCIE5YECA62O2i1the_iDdEexNe7TXSlQWvJ2m01tv_VVIGTIZpGeCFXcRde6OHr67En8nqzP0ffJz3ZY4vy0h7emkNT9jgmDwUjJ7QqudRJ27yQFNrYvvlXuNbGE2MUOH1SfaDmLJJ_rHtSlctUJNklHyfFhoB5keNKxsbdakcPtul9jhUSSCM-VHOL5jLMVngl8TUH829PJQMtcRmd7SD0V8of7h_02yuUB0OqFW8wXDUpNKvP1IzyKyEFxYLj_LTzdFIbA958wAjqtWjEpfA2M-3af8Iwpf9Et1vxQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#رسمیییییی
؛ کسری طاهری بازیکن نساجی با عقد قراردادی به سپاهان اصفهان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103907" target="_blank">📅 19:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103906">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoIn4tlX0WgAHUnskbpoo2rvbwhUUSWhwIPRM_jVLI3S9VBYF0vXaE46ZjHNf19Rq3ONwCwhELxoBgBRRBwAhaQ0MyN_GY74KU0BeCzFDmNiz8AZJmgHaxo59vJveIT0PtQ6lGC20T5jLAiNG2GkMx8T_aZ0nMD1GIzhzupMrWUJ1YGF2yhZVNSpUveFqbMl7kKRRdsBLpnXSIBgkrlqqFkCWO8W2Wh-EO71I_TDic9ZbAG1ogaN2UONS0UMcmQlx8kZ4aSBeiL9OFk51p7VsfbyPNb5NAGcPfwTZ0qD6WgaqwUz9Ae73_owIKKppqle3LJLR9eIJ7cs2FWo838nYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103906" target="_blank">📅 19:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103905">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCpWS-9xMGZ7YLrwyVMrz7_d51DPkGDdV0L0NzfPteNXqvguhsw5PyrVG9QMlT2AfG_a1BCnyZAIWlGWmweY-p1cXe962-EyRlIMyVfuKlvgvXgwNRv7MX_IVJYmis_JHzYm2dva6gUyQbqV9lVjqMLYorJoFaH9dH2eDpyg2GDItvR5TW-X2FpF40hm7FOiTTOC5I25ACRfahFjz3k-rvcGFX0TPF6WICIqj_VPluoKZsL8kbZiQ_Rc46DBPhGAPSQUPJV76ow_RGmA86GveNgv-yqCK2WoYOD6_QDYrc_3Rd4LoreDaLXpATVzddUS-1aEs1y0C3x5Ej4TejHBeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103905" target="_blank">📅 19:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103904">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2eQS-AldJazlDn24w3agNUXb5vqDdWwxx5OENqwGEt_6SP4HuY9Z1wA_EffXOFVMy1rod4epOiq8eWBZQBJ_YPtEoLWNcv9dAZ9UaO4DkjvcX0lX8khpPWO2p4YCf6X0gcoAZXIiA8LI510IetbvnctppGRElvc0gTj9u0uenbb9YBd2aEhKFXfkf3c5Yo2h_8kuUn8KurNCu-y6za-8eS3LK29hbFYnQ_FbpnxdZnd34nPJo78JbmrcdLXxcQl1KyatpJwaJz2Hv85NhS-2cNmOqcLPIZZPjETlkkijqxOS22NnkizN3CRyIKZ8Hq4qKS6zl5tTrgsxoqbyTSAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇵🇹
#فوووووری
از کریستیانو رونالدو: به احتمال بسیار زیاد پایان فصل‌جدید از فوتبال خداحافظی می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103904" target="_blank">📅 19:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103903">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244baec6e5.mp4?token=E5gBkXxZF6Mfzkg3-nEERKpPbSCArwzY9gIAAicGk64p0CACdwnnGfjxUPRox5H_mOYS7hWZR-Fcv5yqbm-3BcnniCcCN1OeSYFdkZK8wwkA3F3zPRv9cyF9vLUc1A5o7gif5B8lm-aaThqtUKFBzIhqvmJ0-WZt-0ifME3B7ERXwIczug2vn_2KYBWavzKUUfr_JzWTtQ8JHxo31uf70_F904aSrksb3qgA3PVJJz31Nv5yMyNJEiqD6YJKUeiJR5oSfzxp7ldfZmMpd1ieUb6pJMQlPDcnoCAAJ5U4ceKIfFT3VP64d7vV702OjZTlDPO6ouZ3jFpZIUIpc1g0dVG1lrPW3OSGV14bQzR6MsgZDn2W6a2u9D0Dw1Dz5TF89wH2ZxWYzs2myHrpco610KNsJvPBbzwt_GzRdwTflkyO9VpiRFJycQASM7SZzGkas_QpvLiq739uZyTylhqNPAs38Y2iHtxNVM2Klaytk5OfUJ1I09_Vq_rVcF-dpxKNOHHdqxqGwtayXRMrBTXLRickaPQWdXewjxNuKbEYStHvaeh1fPc2HSIKF0nZe3aaOVBeZwqPdEqnrue5NptA9fgx7X3h1e1oPL2k8TPgHzkkmpdC0fU-Bb3UH1HGfiEYOqYKNpQM4A0N75uVlV7QGxQzhMY6OQeuq6iQ-ZHtGnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244baec6e5.mp4?token=E5gBkXxZF6Mfzkg3-nEERKpPbSCArwzY9gIAAicGk64p0CACdwnnGfjxUPRox5H_mOYS7hWZR-Fcv5yqbm-3BcnniCcCN1OeSYFdkZK8wwkA3F3zPRv9cyF9vLUc1A5o7gif5B8lm-aaThqtUKFBzIhqvmJ0-WZt-0ifME3B7ERXwIczug2vn_2KYBWavzKUUfr_JzWTtQ8JHxo31uf70_F904aSrksb3qgA3PVJJz31Nv5yMyNJEiqD6YJKUeiJR5oSfzxp7ldfZmMpd1ieUb6pJMQlPDcnoCAAJ5U4ceKIfFT3VP64d7vV702OjZTlDPO6ouZ3jFpZIUIpc1g0dVG1lrPW3OSGV14bQzR6MsgZDn2W6a2u9D0Dw1Dz5TF89wH2ZxWYzs2myHrpco610KNsJvPBbzwt_GzRdwTflkyO9VpiRFJycQASM7SZzGkas_QpvLiq739uZyTylhqNPAs38Y2iHtxNVM2Klaytk5OfUJ1I09_Vq_rVcF-dpxKNOHHdqxqGwtayXRMrBTXLRickaPQWdXewjxNuKbEYStHvaeh1fPc2HSIKF0nZe3aaOVBeZwqPdEqnrue5NptA9fgx7X3h1e1oPL2k8TPgHzkkmpdC0fU-Bb3UH1HGfiEYOqYKNpQM4A0N75uVlV7QGxQzhMY6OQeuq6iQ-ZHtGnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
خداداد عزیزی: نمازم رو سروقت می‌خونم اما رفیق عرق خور و سگ‌مست هم دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103903" target="_blank">📅 19:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103902">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d00dcf8bc.mp4?token=vYcpkp3GYXS5_gnFq3tn_VmXkRjEvr9wuzCXbSoTt3VEn_Znwq_sdB_eWs-nFHhny_0idSL7wcOXDuqARqWuKroN7SCFR9rRuDdfrRRu0ok3Ir_vq9g91tlGtLudRaLCNrHtidP_RksPciKf7ERaAZXIp64DI1whH3dmZBxDN6KnG3vQTjg9-imsM82eqeg2Xit58rnl6KYxT86yJT03bff3lQi2B73konLlakXBGb0dkTeGExEMujnUBodIfBjLYTSt4XvavBIQ6Wcmt6Xwpdww5RIi4uYFWCg_AKe9Eq2_L6amjLCdrgljpd42lzH6Y_7jTRWeEnaBLQpmX-eg3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d00dcf8bc.mp4?token=vYcpkp3GYXS5_gnFq3tn_VmXkRjEvr9wuzCXbSoTt3VEn_Znwq_sdB_eWs-nFHhny_0idSL7wcOXDuqARqWuKroN7SCFR9rRuDdfrRRu0ok3Ir_vq9g91tlGtLudRaLCNrHtidP_RksPciKf7ERaAZXIp64DI1whH3dmZBxDN6KnG3vQTjg9-imsM82eqeg2Xit58rnl6KYxT86yJT03bff3lQi2B73konLlakXBGb0dkTeGExEMujnUBodIfBjLYTSt4XvavBIQ6Wcmt6Xwpdww5RIi4uYFWCg_AKe9Eq2_L6amjLCdrgljpd42lzH6Y_7jTRWeEnaBLQpmX-eg3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گلزنی کیلیان امباپه در بازی امروز رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103902" target="_blank">📅 18:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103901">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754c7f88a2.mp4?token=CEjRFZw8HGbtll1nM055veiBnvvieygPC1iMzHY_aIVOqjja3OvcDPz7NTYNhXXkOAlzXZowNTuDFZ4tqzUc25a2Of3eZbjepReQB1R-zJZBC3ZEBN57JJEhtce5HntLZfuGyhTVoKUKBni_Cwh13TJzk1op2MTMF4XhFP-GTJHCru3DTW3jOh5bdVwkKkz8wUjrt2oB7ZcDtRLNHuMALOWlsSVefF9uRSIkdVLBB6cxH_YoPbNHwhNUgMBnL_kgPRl4-IhMsNGr_JzEMBUXaVLkCYQi-UbMrxgIoXkI7R2h-6FWwUEx2sBAccrFFyYNcbo2pi6CdCSpyv6ODH7AVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754c7f88a2.mp4?token=CEjRFZw8HGbtll1nM055veiBnvvieygPC1iMzHY_aIVOqjja3OvcDPz7NTYNhXXkOAlzXZowNTuDFZ4tqzUc25a2Of3eZbjepReQB1R-zJZBC3ZEBN57JJEhtce5HntLZfuGyhTVoKUKBni_Cwh13TJzk1op2MTMF4XhFP-GTJHCru3DTW3jOh5bdVwkKkz8wUjrt2oB7ZcDtRLNHuMALOWlsSVefF9uRSIkdVLBB6cxH_YoPbNHwhNUgMBnL_kgPRl4-IhMsNGr_JzEMBUXaVLkCYQi-UbMrxgIoXkI7R2h-6FWwUEx2sBAccrFFyYNcbo2pi6CdCSpyv6ODH7AVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل کریم‌آدیمی در بازی امروز بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103901" target="_blank">📅 18:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103900">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گگگگگگگلللل سوم آرسناااال</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103900" target="_blank">📅 18:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103899">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56381f5fdc.mp4?token=aBfGlGxWnT03CToTRCBo0tEGReqfGSCBhzxF9ly6_PEe5zZ2mtRAZU3Dz8oyp1z2l0Ps0pFIcPBONv6k5ukrr3lYtWWR49Ne0IXIwMZumJZN_zGqsTO6yM8PSZo63eaoJxJLJnpQlDza2NICLlm_0yn79Q0dozNeEUoSpqx3RnOikwTjyMJC3qJxSqV3NWEV5vjY-Bv8gtfee64lkgK2KBhv60nFy3bOcJSh7kQy5npwP7Q19PTg-p50nzcyrAQvrm3QzIobmpWdUBqw1OGMM3aKwO5KU-Ib2ILXFAEOE0QaGznVFqF_f8ReeBx2eF6qUtqG8AVplF9QNWvSKVf8LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56381f5fdc.mp4?token=aBfGlGxWnT03CToTRCBo0tEGReqfGSCBhzxF9ly6_PEe5zZ2mtRAZU3Dz8oyp1z2l0Ps0pFIcPBONv6k5ukrr3lYtWWR49Ne0IXIwMZumJZN_zGqsTO6yM8PSZo63eaoJxJLJnpQlDza2NICLlm_0yn79Q0dozNeEUoSpqx3RnOikwTjyMJC3qJxSqV3NWEV5vjY-Bv8gtfee64lkgK2KBhv60nFy3bOcJSh7kQy5npwP7Q19PTg-p50nzcyrAQvrm3QzIobmpWdUBqw1OGMM3aKwO5KU-Ib2ILXFAEOE0QaGznVFqF_f8ReeBx2eF6qUtqG8AVplF9QNWvSKVf8LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
امیرعلی‌اکبری میگه روزم نبود بخاطر همین ناک اوت شدم. ما که نفهمیدیم روزش کی هست
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103899" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103898">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah--8aC1m3vDfw29F7ZZwLSBR2u_X2mKVPAP9NGlLXc_4iIPqOfLK_I5w4q5uUAvA0R368gAFZjqoYvyhabR-9laxzH6po1cvXyetF25i7URlNLEit5Zpql0lUxXeBDOZTE5pAP9cZZuBiHvAtLVBbfYbs3wXGkZo-yROYh6xWNDc8gMxKUsYHr1rSp4v2dQzthGANHVCJ031gWt0sJ2sNdyWIDY6xKDN5HrheDuy9_yg2SrFfUoeO3qpwUZRQmhnd52QSFTn0KtF4stL-RR0DZWYV5FmYzc1uXXHb2zX0lh-a_mddMyrV5uq_eENEv37Bt7ysQBcR7kO5wL_hxSKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103898" target="_blank">📅 18:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103897">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3ab768679e.mp4?token=tVnNL5EdGydLmjsIfh-ZQGVx9cbsxTOJcc157Oik43Fc3_Sm1kfSiw-I2VH3tg4TePAfJni0yJ9tBqfVm1PA2hzE1_R5ofpIPbClXcgSSSUpwPEq0uHEK5sDbe8_YwxLl4_t_Brc1L5RyNRQoiJEV7a8t3iAMn9ItpQUlUm6GNWFTXpeeuz8ycTCZkcjVS-p5k7ULsh27_1-Kxuojy5ZBzEW59KVn650JKXCCEGqrLQPJzLs9lDo8MXHmfCxrA2CiIivsHQucT-tzIS1r8iqCwcc9d2es9_YyQElu7Y6GByyeThWrjrwpiedQPlovoJ-yxZ6Gaonfl4BglY0GOTOTSQCxpikecFMJifKzY5gBfLqZBkYEL1V4JOiIoMR62ITXhX2SKLsW3ELQAEaP2E1CJydVskMZHUU17QqVfa2-VSaDq7UT8yfp0uTnOrjh3AjdzB6864eDzhnULcX3_VfVdwTzwoqJ0VStR-bQjO6aNy_iMgITTDdp9TPMObQ3dl6XAfrXaDHeMu7SqsO1lr_VrFf2AX8WfQqjL6NXg4wSeUTAaHGHFiHgdvNjoi3nh77tKoQW2kltn_nmgK94Sj02uLKIkkiDCOrT59bG6ujqNVOhIAvORLUXfFNvYB1qazMGWlLrkC8wcF_Lp6zr2zGPKwf1mY6foNqWwBLq5eF9cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3ab768679e.mp4?token=tVnNL5EdGydLmjsIfh-ZQGVx9cbsxTOJcc157Oik43Fc3_Sm1kfSiw-I2VH3tg4TePAfJni0yJ9tBqfVm1PA2hzE1_R5ofpIPbClXcgSSSUpwPEq0uHEK5sDbe8_YwxLl4_t_Brc1L5RyNRQoiJEV7a8t3iAMn9ItpQUlUm6GNWFTXpeeuz8ycTCZkcjVS-p5k7ULsh27_1-Kxuojy5ZBzEW59KVn650JKXCCEGqrLQPJzLs9lDo8MXHmfCxrA2CiIivsHQucT-tzIS1r8iqCwcc9d2es9_YyQElu7Y6GByyeThWrjrwpiedQPlovoJ-yxZ6Gaonfl4BglY0GOTOTSQCxpikecFMJifKzY5gBfLqZBkYEL1V4JOiIoMR62ITXhX2SKLsW3ELQAEaP2E1CJydVskMZHUU17QqVfa2-VSaDq7UT8yfp0uTnOrjh3AjdzB6864eDzhnULcX3_VfVdwTzwoqJ0VStR-bQjO6aNy_iMgITTDdp9TPMObQ3dl6XAfrXaDHeMu7SqsO1lr_VrFf2AX8WfQqjL6NXg4wSeUTAaHGHFiHgdvNjoi3nh77tKoQW2kltn_nmgK94Sj02uLKIkkiDCOrT59bG6ujqNVOhIAvORLUXfFNvYB1qazMGWlLrkC8wcF_Lp6zr2zGPKwf1mY6foNqWwBLq5eF9cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال توسط کای‌هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103897" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103894">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گلگلگگلگلگلگ دوم آرسنال هاورتززززز</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103894" target="_blank">📅 18:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103893">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0fc033ef.mp4?token=JdNhoSLkBDa11xWJG_FjgP9k_DLcA-2WzkOjn_W6kiAR8ndtQe_IGRysV-k3RC7vFYfgFoabkyEvBge5m0i2bnBr7lbmMqWE0xg505EBBHjfhMj72vTl0033Yb6zTAiIFz2k6OeTFFSnjiETTJVb3bj-PwmJ0rKmuboHFCZke5oTBjLc9VsHyHCQCKEraVJ-M-hjcc3fEWxzcsXGpE2nvcRE4p1uFFa1OPSdzlVoWyobDAsDxkf_VRAeDM4GgT73_xa7yW7vtxsJBd3f57quC439TqItSaIPAZTea-gr4_O1sswu69Vs3KkQ38vi6oiPhW1owSxFMMfcaMN6KtG_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0fc033ef.mp4?token=JdNhoSLkBDa11xWJG_FjgP9k_DLcA-2WzkOjn_W6kiAR8ndtQe_IGRysV-k3RC7vFYfgFoabkyEvBge5m0i2bnBr7lbmMqWE0xg505EBBHjfhMj72vTl0033Yb6zTAiIFz2k6OeTFFSnjiETTJVb3bj-PwmJ0rKmuboHFCZke5oTBjLc9VsHyHCQCKEraVJ-M-hjcc3fEWxzcsXGpE2nvcRE4p1uFFa1OPSdzlVoWyobDAsDxkf_VRAeDM4GgT73_xa7yW7vtxsJBd3f57quC439TqItSaIPAZTea-gr4_O1sswu69Vs3KkQ38vi6oiPhW1owSxFMMfcaMN6KtG_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
سوپرگل دیشب ژائو فلیکس برای النصر که رونالدو از روی سکو پشماش فر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103893" target="_blank">📅 18:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103892">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648b67b731.mp4?token=mTclYFQThgRXEVnPWdIE9aPzouUbtEbYcfShMCrNWSIFvSfn7lzrRfLXxu5aI82cxzcLoyLen9gmR6m34LxJCgKUlEDJzS5ZNs-YLtbeycyLwfKpp3Aj9YanfSdBYbSfMsw6xt1_0cg5Jv_GIIa0VnBHY5HLjph2vixZ9QNwj9VTos-TjITFyquR3-egHzzoYosy5MY4F0wGzA2YaOZJ90yF7awhzynVBG5MkyHWpFNFFDVipHx21HgPsvXIpobaoduVvuzHiQa4fxZDr9nCeUyv3zkkx_yIyH2g3Q_Gq9ulSbL8xlSOWnOY2WZDYRjXSIS3yIC2Y6Ogvx8khvGibA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648b67b731.mp4?token=mTclYFQThgRXEVnPWdIE9aPzouUbtEbYcfShMCrNWSIFvSfn7lzrRfLXxu5aI82cxzcLoyLen9gmR6m34LxJCgKUlEDJzS5ZNs-YLtbeycyLwfKpp3Aj9YanfSdBYbSfMsw6xt1_0cg5Jv_GIIa0VnBHY5HLjph2vixZ9QNwj9VTos-TjITFyquR3-egHzzoYosy5MY4F0wGzA2YaOZJ90yF7awhzynVBG5MkyHWpFNFFDVipHx21HgPsvXIpobaoduVvuzHiQa4fxZDr9nCeUyv3zkkx_yIyH2g3Q_Gq9ulSbL8xlSOWnOY2WZDYRjXSIS3yIC2Y6Ogvx8khvGibA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول آرسنال به منچستر سیتی توسط کالافیوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103892" target="_blank">📅 17:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103891">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آرسنال یکی به سیتی فرو کردددددد</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103891" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103890">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103890" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103888">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxHs3XsTJgTE-SKdj_qh7E0jJYoEBYShjP1CAw296R_0eDMOA2rVRGIYvlH2wVJag-n0KZAcgczbB16glEEmqOCDRrpOg815Rz247mLW3eix6MFVYnNCJfcgv3_Qzg8Br6aIv5XehBXIq9zwG6elyvrk0Eo3qZv4nP3aOZBdKWGZkdrM5_O8lNZ7TF2BaxopbAoqE_NI7gfTPisXHK24DIYvelaEkMjziNXM3zS8iPMwrhuc4-Rb8-l5bWpH3W0iexIpf1wgw1ReKMdCaUXiRWE_V4OpBk8I0golTtZYsATHqmsOTeJX8411HIXHFUfQEwY021mrWRVZP0KAfD0i_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgAZuFGgP0m_rc-ALH-bGjvzKjO2k6jtBpD7EqKTV4UyGsVG3fq04uHiEArZeIjN6j3CazyX6QddhtMyStep6IEZkpG4bu3YTVcxAxVsxTv82_Q0BEjNbGnDBKhxvr3Z8fyEfTOlUVC-zNt3j0V77zvh-6Ry42TSA8TweSQzfBxLKViVQfjjK98_roRBYDlG33mKGpbQYMaRVV9VrirH7cpDrY48eIKgPtwu_I3L6QFDle-INXdBJu_GJfrpteYMwgLgDxq9nXIbUbIqdq8TCd8W4fuktQCOBN3bKp_6BX9qI1TTuI8XQVvKwb9AXzUpZUdSsUJS-r9PVigQXmzpdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب رئال‌مادرید و بارسلونا در بازی‌های امروز تدارکاتی مقابل بازل و شالکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103888" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103887">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2aced863.mp4?token=ByykXff33AXu4yJ-M0u-ttBEeVm0hYmaoiQuaJftyeZBdHo6FJtUZ0ItzTIrfcfO_s5CNe16_WLbYzlK0cYQZFsW5GUExGLFQTDwbQbkpBUmsgMLHiHB0WKQbvZiT3aSY6iZo_e9tqMs2vE1I-Ik6h7LakR8gN_sTtBAqvdCdnhZYVjFnRfzFYUOWqpUXhQ5Hd17JIYV6pHVrpe6PPu8c2BL_m3DWNi1APE9ChA4NKY1nGkcN9-JPlvoL8RKbybszipv2uQ06RsT4v6IxmXPDKldPJZYhublWjTtooH6SRFW1SjLnJA9FUrJB6lPA2A8La0Fzb5Zc-4uiNy1BJGIUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2aced863.mp4?token=ByykXff33AXu4yJ-M0u-ttBEeVm0hYmaoiQuaJftyeZBdHo6FJtUZ0ItzTIrfcfO_s5CNe16_WLbYzlK0cYQZFsW5GUExGLFQTDwbQbkpBUmsgMLHiHB0WKQbvZiT3aSY6iZo_e9tqMs2vE1I-Ik6h7LakR8gN_sTtBAqvdCdnhZYVjFnRfzFYUOWqpUXhQ5Hd17JIYV6pHVrpe6PPu8c2BL_m3DWNi1APE9ChA4NKY1nGkcN9-JPlvoL8RKbybszipv2uQ06RsT4v6IxmXPDKldPJZYhublWjTtooH6SRFW1SjLnJA9FUrJB6lPA2A8La0Fzb5Zc-4uiNy1BJGIUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
عملکرد ابوالفضل جلالی در اولین حضور فیکس در ترکیب تیم‌فوتبال پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103887" target="_blank">📅 17:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103886">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6927287d81.mp4?token=NxJz7ctEtSfiwT4sKI7-CT0YPh90ZX30F0vEH4fv2Rax56Xt06sAgjAuzhPtx-wueq8VeO6ntWn7e6vWO5qjWAlZjyh7suU9yPjuH6adSbzxC0bTWtgktZExmqLRUwpdCLIMgChNIbMCGuimqCICVnKky4s21zrQnXnt_wzIOWzLjXD3G9IQg7cQ2ET6xz0wy9gsLCCjweUh8O6bTA8mjSkl1OAPDFgMNgp6kX_rCVlhpvU2p87iK3yp9mitk4uPSt_lp2Bvq1qpWqAO7AMkqwfDQoVP7i-GFpA8wvYEirUrcAx71apqW22bg0KVFI9RSdabFOEVRGMhl48GwHEbMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6927287d81.mp4?token=NxJz7ctEtSfiwT4sKI7-CT0YPh90ZX30F0vEH4fv2Rax56Xt06sAgjAuzhPtx-wueq8VeO6ntWn7e6vWO5qjWAlZjyh7suU9yPjuH6adSbzxC0bTWtgktZExmqLRUwpdCLIMgChNIbMCGuimqCICVnKky4s21zrQnXnt_wzIOWzLjXD3G9IQg7cQ2ET6xz0wy9gsLCCjweUh8O6bTA8mjSkl1OAPDFgMNgp6kX_rCVlhpvU2p87iK3yp9mitk4uPSt_lp2Bvq1qpWqAO7AMkqwfDQoVP7i-GFpA8wvYEirUrcAx71apqW22bg0KVFI9RSdabFOEVRGMhl48GwHEbMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
تمسخر ۵ سانت و ۱۰ سانت امیر قلعه‌نویی در گفتگوی خداداد عزیزی و مجید واشقانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103886" target="_blank">📅 16:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103885">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO7AcdvtD_yp1BRmHw4ZcsDseAw4Yba8BiPM10hXM4ekxJlZBE04BaIf7Tqb36s3MtBkxwdVLQLsVjzvYD6tFt00bHGopQNJANO6siSsm34Rz6S9Vdr5gMQuhY8_eLcMPu-YST2f2wZiGUjD-fOU7GNIsS-jGSD-vOHpUsOsVIa_3nSDFECWlaVKBohXtuhhZVBZ9njsC3DA34nj5Hi1KJiV9xGo84-vGPKe1CADiUYmY7K1Zy7ooCp1rSmkEaP20yDUYGtuUETyetOVALD_9fkmhwfFB1dwg9nb1Paqxil0RMH4EqFuddnz_qHSYcciFn8PinLnsqk9_svDz3pIgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103885" target="_blank">📅 16:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103884">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248d4f7bea.mp4?token=alAzRM5MW2aQeTjBFsLTy21pNVGPGrUS4nvrRP0MZ7TcIBg2lOmEVQbSnpLdXpXISzDuG-cwiokukXl1oBv1DcEyjWWItpyamkZN9LoerylcYCaKeJKaEF9YJK4PJ1IjrQgzKdpmYxQznoTB-bn7Nyqkz1QRB_pBXUP8wEJJ4oVtLCBRG1_ijcMJjdYWZWf2PBPV0IPqotTFb0IlIxtRQhtTrRUj2zogUIq7qSG7ut7fJF6_1OzpxGjyrOuuFJdG9VSBwgila5tWBY6-OpD7G8O9b12m-txPr1CUqxUlXzNVRrWz0WgcPUC7jFTPDHVhMmAL5Jz_1gNRMfG3csEP0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248d4f7bea.mp4?token=alAzRM5MW2aQeTjBFsLTy21pNVGPGrUS4nvrRP0MZ7TcIBg2lOmEVQbSnpLdXpXISzDuG-cwiokukXl1oBv1DcEyjWWItpyamkZN9LoerylcYCaKeJKaEF9YJK4PJ1IjrQgzKdpmYxQznoTB-bn7Nyqkz1QRB_pBXUP8wEJJ4oVtLCBRG1_ijcMJjdYWZWf2PBPV0IPqotTFb0IlIxtRQhtTrRUj2zogUIq7qSG7ut7fJF6_1OzpxGjyrOuuFJdG9VSBwgila5tWBY6-OpD7G8O9b12m-txPr1CUqxUlXzNVRrWz0WgcPUC7jFTPDHVhMmAL5Jz_1gNRMfG3csEP0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رامین‌رضاییان خوش‌اشتها
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103884" target="_blank">📅 15:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103883">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b623d393f.mp4?token=Gyghn_y17pd9jqH7cHhgdTorTlJy_f3or3cDuRlBPX4FJ7dnz2QAumBt2fDhjvdpS-Y4Ec6nH-4-TIeFfItlg3uiWvLjVJedp2CjNx3VL0ET4xIhYzi79atWIErluYD2ZKs3kD1TUEEVEr7SjHd-HcHE5KpnbVUpQUS9qdXJ5DsrlFp7NXoreZBvtyGfZo3oP2STBEqvvPepfDifbviK-ck4MRnTNdM-ueSXj5ToM-XNZQwteg3oZc45n2l0WcFfm3Xk93_t1FUpv6ktFVQQrxNlwFtpNYSg-OvpQtO9k2yJhyrg31SbeFTWJ87-YFa-xRmw3ysOqzaCRW7ERwmCyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b623d393f.mp4?token=Gyghn_y17pd9jqH7cHhgdTorTlJy_f3or3cDuRlBPX4FJ7dnz2QAumBt2fDhjvdpS-Y4Ec6nH-4-TIeFfItlg3uiWvLjVJedp2CjNx3VL0ET4xIhYzi79atWIErluYD2ZKs3kD1TUEEVEr7SjHd-HcHE5KpnbVUpQUS9qdXJ5DsrlFp7NXoreZBvtyGfZo3oP2STBEqvvPepfDifbviK-ck4MRnTNdM-ueSXj5ToM-XNZQwteg3oZc45n2l0WcFfm3Xk93_t1FUpv6ktFVQQrxNlwFtpNYSg-OvpQtO9k2yJhyrg31SbeFTWJ87-YFa-xRmw3ysOqzaCRW7ERwmCyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشی داره تشویق یاد میده یا تقه‌زدنو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103883" target="_blank">📅 15:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103881">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKP1rfPvtgjSyroH7-pTmW1Rjo3-CvQ5QkX0Fbwl3s8JdpL1mttsUgx6VCSd13A4IO5qXn68NphiNWlNfeOxrcLkyWdf_0MI-3u60QisilTVfU8BGj2_rx7S3bfs9-L7ApVvY8CZsTOrrk9CXJzO7hyXSETShK70s6YWZE1VG-bZxTj8SlXcCxp6VJ8oG7CWRkUnqDmbwPU5n91icLxuWvnQFGvANSnM90xXYtkFhHxx3hcenHEnMnzPqJzeQC6w0rdg_NSoTV4P5cNNrm7KJp48q-uime2N8-1VQGL74vsyCxkRFIZ2dGUvGE9ZAH05hbyF62JvT5jiyvtXYnlsXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCiGEiYb_cq9wh7alI9uxu3FzulWlOE3ozF12wWv55molxJXcGZ55PYxWHW4vO7p_NGwYhuX0Nac-FIBmJ5CocAeebFMxFyhZqKlOap-ygQL9SAeisaYVHwPCD7rlZxnWQa-hVMnY3nPhJUxZb4em3z971zJJXclNnJPcqLaz_bkgkwWAFKZASs-yJNFxbBdDMFbJ1WdAFa5e5hWEZ1FKN_KMbIX8WQVusFzprGKhhNi2p9EJF6qUOf7_PZMr1fntXM4YWMqiQfV6mlAOS6vo-VDrkasnTUJGYKE7dtfPkffQ26eaUerPbpv8hBVwBv9ji4M8VB8ZTQApXr_0MWu4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😐
🇮🇷
عباس اسماعیل‌بیگی لیدر پرسپولیس درحال یاد دادن‌تشویق وایکینگ‌ها به طرفداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103881" target="_blank">📅 15:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103880">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFNzFlEPDIl7twn-hhpaCyfxQXsCa8de-abNNP5Gwwci1PtmlgEZZv9uCWu24z2cD_mBQ2WlE6RxjgTV466nAVodK19Gg4FrIhr3C5jryPL1MEuJ4_L0CFXE6mq2F-DSxDJY0E0VU3doFojRbTGL-mlBph0witqFrjOaigum5Tq7hBZPAQHw88kcj3Q9sMLdlQeS3VPph2ky_QQZ13jps7mfs8AuYouiVOoHEWWUoNFCDKp2rjlada4bgN3qySv45gOGxxdaAJKgExZ66tHoc-2vQrFQgm5QM5o9de2wOjbP8VpzD3__F1RP6pHDWHZuJLm9KjfnbkJL2oYuZMXYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فرهاد مجیدی پس از گذشت ۴ سال حضور در کشور امارات ساعاتی پیش به ایران بازگشت. مجیدی اخیرا پیشنهاد سرمربیگری تراکتور تبریز رو رد کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103880" target="_blank">📅 15:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103879">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHA60veO61X-fha70-nOTSMeUDlMU4UqgU06f9tk2_yxigPsUnfSTq8biFeXAVsmVTfBUpwy_1DWRKfbIhoHuC_1zTqpFXf6rj8c5HdcMfKRh30BElJaNueytzZIP1sIdb1wuTmLh2IcVB465imq7yPGKnNrk_dRxzFG1fYNgYKqqjL2y5nw6RCCoI7b_vqzfxMLu4qFFItpU0PQ2D8_LBdRnwsdDs-7HmyWZzKmnZ8B6GxWwQB-BBjEZsjVabKaehjfgzrKKkYZiW9LAnZBQ2Why3B7bK865Qzi1DGGJhQfjCPJ3r6oTc6yWQnLYcpedCOu4zAv2L0lvXDPrfFvHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇪🇸
#فوووووری
از متئو مورتو: ژائو کانسلو با عقد قراردادی به بارسلونا بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103879" target="_blank">📅 15:19 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
