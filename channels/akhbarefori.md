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
<img src="https://cdn4.telesco.pe/file/tdTmhAtoY087R3ehIomqW-t5lWjSSd-RkzI0yefhIMRQAuroPMVLWNEWEU6br1prKDX84l9-_ALdKRnn-EjmcYCAO-S9-rSFsgXSkG2wEOs6-VzFxiZLb5chsSeQ0e8okwU-W5xm1Q1YhK9ITe-nfOuhOee5meOXqFCDDt3HveNNrgZwquOGibjSEBmlxz3WFYcoTuMjEg94YCQFllHR52a6QR-ruXThF-7P0n8ZpDFPOr8YMBxBE6VK1khOmCrsMEMf9ZVqwid26WkI6xCtzMcqLqWbT-U8OxdwyIpeoqO0Z8ZKlk32OesTeciseJuLo86aVxi2bUTlakWXYDJSdg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-693624">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7e623aac.mp4?token=Ta7tcw9xtxCeI8y4ud0wWTM1NGVvF1OcJJg8I7YliMO_rv1UwWWOGuATjhoJ3PX7ArUcdlbOCUbCu979-wjW5y8NSvITxszYFhIwj4F5GoankaNV2WGFBxl8m8fdKXYox6y8o9xbH0xbBMHzrWPOPH9fgBugdcsmKPMunvzocbgsYVtZzQxMFeeHdPJjJb6I41A2Fg505NQG3nNVAmkVxSdyXHbWb7aQo05Ve2o3vWW5xuHIln7moNIbOdlO6ltCKqGOO7giRkFfBANBdiWQUOcSBQXhPpOVmbZ9OsBnbGZrpmy7qPw8cpu7yDsxHvxO_0_SCHrq_e3IIuyK6m2V9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7e623aac.mp4?token=Ta7tcw9xtxCeI8y4ud0wWTM1NGVvF1OcJJg8I7YliMO_rv1UwWWOGuATjhoJ3PX7ArUcdlbOCUbCu979-wjW5y8NSvITxszYFhIwj4F5GoankaNV2WGFBxl8m8fdKXYox6y8o9xbH0xbBMHzrWPOPH9fgBugdcsmKPMunvzocbgsYVtZzQxMFeeHdPJjJb6I41A2Fg505NQG3nNVAmkVxSdyXHbWb7aQo05Ve2o3vWW5xuHIln7moNIbOdlO6ltCKqGOO7giRkFfBANBdiWQUOcSBQXhPpOVmbZ9OsBnbGZrpmy7qPw8cpu7yDsxHvxO_0_SCHrq_e3IIuyK6m2V9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند نکته ساده اما مهم درباره نحوه اندازه‌گیری فشار خون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/693624" target="_blank">📅 12:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693623">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED-Qvzuwu44i4taqxFjBfaYlu1PjX0Vs4fCAo6YqEF04b99026-KH79xqrd4eslLR6_vQc81rDEaCjl8-xsCCiWbhFaWOfXxQpwOf6fv4zjO8U1cJJMofdXBT9v2OB7h-Km-BpxAk-1mUF6d2lVbhPmJy4RdWbGaZs-a-5RLPrN4Mcdf3pU_YKSBrId9805jkO5mwc6Ww1VOPtB3erICBUsWSotsc_1ei6piS-3CDeIEMJrEM9cS2v5ncDLZ2U-VpJMO9L0M2oSEom0OLgox3XUq8R2a6iEIN7GSNM90KwSfMcawLEGUDMnIYYpOUsRdark0G2tULjqUnNCSGwgcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/693623" target="_blank">📅 12:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
با این ترفندهای ساده، مواد غذایی دور ریختنی‌ رو قابل استفاده کنین
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/693622" target="_blank">📅 12:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693621">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
نفت برنت در ساعات میانی دوشنبه ۲۸ سپتامبر از ۱۰۷ دلار عبور کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/693621" target="_blank">📅 12:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693620">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52e4ac10b7.mp4?token=PU6l0G5gBpnvhjDKKwAWrBd0qCEivFFT2niLLvR8NfOlM72TnSKqtDakp0oo_DcHflMkb8yP8p-Ch7W-ES4VzU5KxRtHoaKu_JrumLGwxU-H3RyisA91UhODVjExVVqKpJz8ZAPUPpVG_OqWOcypqpo-qBSc8NaEbh0e6daVlxzrb8iAs5ILDy2m4B1Xg33Ku0bR-E47WltCnVUKGkSI2f9tIWU6LcHiTPrB1YMhO8DFRVEccH4agZEUDOuGl2lH0Fz0QFG76cSr49h4JJxvSVxyOwWXwRr0RpoDFJxhfII0v6dd59owQyj8YPZuQAPhmJdQ7GnOZWUraFvwMwZ3AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52e4ac10b7.mp4?token=PU6l0G5gBpnvhjDKKwAWrBd0qCEivFFT2niLLvR8NfOlM72TnSKqtDakp0oo_DcHflMkb8yP8p-Ch7W-ES4VzU5KxRtHoaKu_JrumLGwxU-H3RyisA91UhODVjExVVqKpJz8ZAPUPpVG_OqWOcypqpo-qBSc8NaEbh0e6daVlxzrb8iAs5ILDy2m4B1Xg33Ku0bR-E47WltCnVUKGkSI2f9tIWU6LcHiTPrB1YMhO8DFRVEccH4agZEUDOuGl2lH0Fz0QFG76cSr49h4JJxvSVxyOwWXwRr0RpoDFJxhfII0v6dd59owQyj8YPZuQAPhmJdQ7GnOZWUraFvwMwZ3AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن فرشتگان
🔹
اول مهر امسال، دانش‌آموزان به یاد کودکان شهید میناب، مدرسه را با نام و یاد آن‌ها آغاز کردند.
«کودکان شهید میناب؛ ما راهتان را ادامه می‌دهیم.»
روایتی از مهر، یاد و همدلی دانش‌آموزان ایران با فرشتگان کوچک میناب
🔸
الوفوری را دنبال کنید
👇
#جشن_فرشتگان
@Alo_fori</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/693620" target="_blank">📅 12:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693619">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9180e8fe29.mp4?token=VIYt1CgnCPPX1QIkNE5lb0UrzpugMWwD4wSytvodVKIoz2klCsiVWSjsgAIsFbW53irwlZX0tAghezt1GLr6nycrWNDtDHzB5SZT-Wjqm_vLsN11Ndp0V4MtC9qO2sPKhQ1Y6iLuUwgkilBIOU8mcbrEeipzXYbX81ghvvrLBjDAkEwZ80QqZTR8_l_ko2Gpxds4JFC8e3IkPFh9wynVvN5bdLGTuPxL46TITn7v_VCdyfW4m3nOKf3X8U0xYMW2Xh65RCVMMAZqy1TEJTjQL5pr1VOP5cvVLljaH9_XxnEWTzUflPUrmQ6tFOhwoneHlAAs1ybSuFfelK3wGX62yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9180e8fe29.mp4?token=VIYt1CgnCPPX1QIkNE5lb0UrzpugMWwD4wSytvodVKIoz2klCsiVWSjsgAIsFbW53irwlZX0tAghezt1GLr6nycrWNDtDHzB5SZT-Wjqm_vLsN11Ndp0V4MtC9qO2sPKhQ1Y6iLuUwgkilBIOU8mcbrEeipzXYbX81ghvvrLBjDAkEwZ80QqZTR8_l_ko2Gpxds4JFC8e3IkPFh9wynVvN5bdLGTuPxL46TITn7v_VCdyfW4m3nOKf3X8U0xYMW2Xh65RCVMMAZqy1TEJTjQL5pr1VOP5cvVLljaH9_XxnEWTzUflPUrmQ6tFOhwoneHlAAs1ybSuFfelK3wGX62yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرلندی‌ها رژیم صهیونیستی را تحقیر کردند؛ احترام به شهدای غزه در فوتبال اروپا
🔹
بازیکنان تیم ملی ایرلند یکشنبه‌شب در دیدار برابر اسرائیل در لیگ ملت‌های اروپا هنگام پخش سرود ملی اسرائیل سرهای خود را پایین انداختند و از دست‌دادن با بازیکنان این تیم خودداری کردند. بازیکنان ایرلند همچنین به یاد شهدای غزه با بازوبندهای مشکی وارد زمین شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/693619" target="_blank">📅 12:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693618">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224f94a7df.mp4?token=Nc9REXjR9bmHdt1cccg1xIsXwHGM6QQZajXiYh50w9qOB3qgXmaNEB1GJv89i2Nk50O_8aW1xWVrMCSjG7s5kqUKC9qAPbgNpnL9GM2IXDZj9CgJfcxZ70yCJ2rW-X4GOv6VgrA805c_q72_5Mb0_zRU1fNVkW0zJaxOxt59qvTiaN4tpaTZYxJtpPFKdvMk6E92-Rw0uO1auZ1_tN5oojcO05jgsa2NUadYQzqDamjCqak9dMxdroiim6JFBKoYcRoyq56C__aKPK48zSCFB9e2m3YPfu_HGuYxV2pAXpDNVaJTpbKso1WCTyLnM6HQDJ125v3AxyEbhCKW_5QT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224f94a7df.mp4?token=Nc9REXjR9bmHdt1cccg1xIsXwHGM6QQZajXiYh50w9qOB3qgXmaNEB1GJv89i2Nk50O_8aW1xWVrMCSjG7s5kqUKC9qAPbgNpnL9GM2IXDZj9CgJfcxZ70yCJ2rW-X4GOv6VgrA805c_q72_5Mb0_zRU1fNVkW0zJaxOxt59qvTiaN4tpaTZYxJtpPFKdvMk6E92-Rw0uO1auZ1_tN5oojcO05jgsa2NUadYQzqDamjCqak9dMxdroiim6JFBKoYcRoyq56C__aKPK48zSCFB9e2m3YPfu_HGuYxV2pAXpDNVaJTpbKso1WCTyLnM6HQDJ125v3AxyEbhCKW_5QT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کف دریا خیابان‌های ساحلی ماساچوست را پوشاند
🔹
در پی وقوع طوفان شدید «نورایستر» در آمریکا، حجم زیادی از کف دریا وارد مناطق ساحلی ماساچوست شد و بخش‌هایی از خیابان‌ها را پوشاند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/693618" target="_blank">📅 12:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693617">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60f6e63ba.mp4?token=NSmH1qQ0-dMn5EoFNJ8QPSmk01aGV8gBqepY9GRl1Heptcgdkn49zAWFsodv2n28PHXZTXx_caHBB7ve1dqE47FcopNOuNS-UvPWMFWgRVUJwrK3lbVqCnx5BN6-yKC-vLliTjR_z1aEcnHCRL4RPD2UH2SBbhj4uhrrUp2QqY1tZ4jBsMwQ059V1A3YW1Vdi72DwLoXyIKZmdQHsbjR68S13rCsgmAIJ9rtzicVak2wArieWdZaKSel2dvOqOEa_D-QaYIFpTJnPYB8jKho97m1xOR9hbGgEXSoITmemUCzezOzjcYeqr5UPNXZJ4gGemN7UrTV-4lAQcqFJ-a1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60f6e63ba.mp4?token=NSmH1qQ0-dMn5EoFNJ8QPSmk01aGV8gBqepY9GRl1Heptcgdkn49zAWFsodv2n28PHXZTXx_caHBB7ve1dqE47FcopNOuNS-UvPWMFWgRVUJwrK3lbVqCnx5BN6-yKC-vLliTjR_z1aEcnHCRL4RPD2UH2SBbhj4uhrrUp2QqY1tZ4jBsMwQ059V1A3YW1Vdi72DwLoXyIKZmdQHsbjR68S13rCsgmAIJ9rtzicVak2wArieWdZaKSel2dvOqOEa_D-QaYIFpTJnPYB8jKho97m1xOR9hbGgEXSoITmemUCzezOzjcYeqr5UPNXZJ4gGemN7UrTV-4lAQcqFJ-a1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مگس‌گیر سلطنتی آمازون با تاج شگفت‌انگیز؛ زبانی متفاوت برای ارتباط با پرندگان
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/693617" target="_blank">📅 11:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693616">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d9f7619b.mp4?token=C5ZIm-g44fvF3CY7DSX8DYzwU6l1RBPh1V-84y1UJvIWDpM59zk7wHDccHUUV5A_cVIpfHuheCUPoZx71M0bRlQWhRb6373F5tU9ECPun-vrejoqPRx3ejtFnYrhd6u-5HC8RSH6QNiW4bY3uznNk57oI4DkGe4o5rAThkpDF7i1Ses92aDdtYhcWqLDGW9SfW2dzlEN5XadFYHfndcSJDIW92Oz6wdLA94STIrMysp3YhdfrYqZDUpNTYdh9jI676BdGSwbZHdUpPsJU7zXIFqcfz1wFdOFmjF31t1LvnQaczQVkbrsqKEBil8g3jLCog9fAHQN1x3SlIfz20x6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d9f7619b.mp4?token=C5ZIm-g44fvF3CY7DSX8DYzwU6l1RBPh1V-84y1UJvIWDpM59zk7wHDccHUUV5A_cVIpfHuheCUPoZx71M0bRlQWhRb6373F5tU9ECPun-vrejoqPRx3ejtFnYrhd6u-5HC8RSH6QNiW4bY3uznNk57oI4DkGe4o5rAThkpDF7i1Ses92aDdtYhcWqLDGW9SfW2dzlEN5XadFYHfndcSJDIW92Oz6wdLA94STIrMysp3YhdfrYqZDUpNTYdh9jI676BdGSwbZHdUpPsJU7zXIFqcfz1wFdOFmjF31t1LvnQaczQVkbrsqKEBil8g3jLCog9fAHQN1x3SlIfz20x6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناو هواپیمابر روزولت به غرب آسیا اعزام شد
🔹
آمریکا که به اذعان فرماندهان کهنه‌کار ایالات متحده پس از جنگ ایران با کاهش شدید مهمات و کمبود کشتی‌های جنگی روبه‌رو شده، این بار در بحبوحه تنش‌های واشنگتن‌ ـ‌ تهران، ناو هواپیمابر «یواس‌اس تئودور روزولت» را راهی غرب آسیا کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/693616" target="_blank">📅 11:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693615">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/711f4125a6.mp4?token=V3u46zHTBw-dhUGXWVKHHeQecyC0SbQrie_I41EJLt63owPHBTgtNX_Gnf5hKYMhFU-wVaqMSFevSb1z8xeLTbMbyv8wpsmIPJ4zq03GZJr2tLJnrGyD_tKpKvufLdDKKUF0nNlGnK78p389FT60vnlYYP8sA-W1iHbt78Dg-E-lPZb0gQEc2kwaoPrLuJsKJkxjdRxQdp7vQIIATsz2-PczessoB3pGrMVSglzgGWatiUsiGeF4iqGcjb9LcJJy2BOjRwyq1NYH5T7HUnB0i0-HufGs5sSzmhy6OQ0Gh4_WQbnfY3bSkCU45kjrTpZUfJ0BW-sqMCk7E441eITYOlF5q3-5TdbePVrDtmRnDiDsWDUwTwW1x3VTCYS97AEZxe2xOz8pN4JPUzBU4Iu5KtNC7xXF3Uy-AGyL-FMK1Xu_UKkAFRuWZ8J6HgQFuxlPDEkj0M0gDJjspMnlymG2xl7jeeeKJ3pmwezlcIaXy5c0iYM7xbIFm70OKk0Qyd0EdX2zXSO2MKSBxPIhcIEEWhRQzJ3zz0bjd-6gb6JNyrpKEcyBAshk7bZdUcpL8YF80XjUI43d5ge0njIKkGATqSMoZHo4KGlozxgcUnlSHajAJBlUmSt_4-fv5S9B2SbrhTvxnMv2RkChVE3PuQAqN9u8z8ZZU8AUWCfcVSlzQ4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/711f4125a6.mp4?token=V3u46zHTBw-dhUGXWVKHHeQecyC0SbQrie_I41EJLt63owPHBTgtNX_Gnf5hKYMhFU-wVaqMSFevSb1z8xeLTbMbyv8wpsmIPJ4zq03GZJr2tLJnrGyD_tKpKvufLdDKKUF0nNlGnK78p389FT60vnlYYP8sA-W1iHbt78Dg-E-lPZb0gQEc2kwaoPrLuJsKJkxjdRxQdp7vQIIATsz2-PczessoB3pGrMVSglzgGWatiUsiGeF4iqGcjb9LcJJy2BOjRwyq1NYH5T7HUnB0i0-HufGs5sSzmhy6OQ0Gh4_WQbnfY3bSkCU45kjrTpZUfJ0BW-sqMCk7E441eITYOlF5q3-5TdbePVrDtmRnDiDsWDUwTwW1x3VTCYS97AEZxe2xOz8pN4JPUzBU4Iu5KtNC7xXF3Uy-AGyL-FMK1Xu_UKkAFRuWZ8J6HgQFuxlPDEkj0M0gDJjspMnlymG2xl7jeeeKJ3pmwezlcIaXy5c0iYM7xbIFm70OKk0Qyd0EdX2zXSO2MKSBxPIhcIEEWhRQzJ3zz0bjd-6gb6JNyrpKEcyBAshk7bZdUcpL8YF80XjUI43d5ge0njIKkGATqSMoZHo4KGlozxgcUnlSHajAJBlUmSt_4-fv5S9B2SbrhTvxnMv2RkChVE3PuQAqN9u8z8ZZU8AUWCfcVSlzQ4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی فرید، جاسوس رژیم صهیونیستی که اطلاعات حساس کشور را در اختیار موساد قرار می‌داد اعدام شد
🔹
مهدی فرید فرزند امان‌الله به جرم همکاری گسترده با سرویس تروریستی جاسوسی موساد پس از رسیدگی به پرونده و تایید حکم نهایی در دیوان عالی کشور به دار مجازات آویخته…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/693615" target="_blank">📅 11:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693614">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
بیژن مرتضوی، نوازنده و خواننده سرشناس ایرانی، جدیدترین آهنگ خود را برای کودکان شهید میناب خواند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/693614" target="_blank">📅 11:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693613">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
راز قتل زن ۴۰ ساله پس از ماه‌ها فاش شد
🔹
پس از کشف جسد زنی ناشناس در یک واحد مسکونی در جنوب تهران در ۱۹ آذر سال گذشته، کارآگاهان اداره دهم پلیس آگاهی با آزمایش DNA هویت او را شناسایی کردند و در ادامه دریافتند مردی که مدتی با مقتول زندگی می‌کرد، پس از حادثه متواری شده است. این متهم سوم مرداد امسال در محدوده حسن‌آباد فشافویه و شهرک صنعتی شمس‌آباد دستگیر شد و پس از انتقال به پلیس آگاهی به قتل اعتراف کرد؛ او انگیزه خود را عصبانیت و مشاجره لفظی عنوان کرد.
🔹
متهم با دستور بازپرس و قرار بازداشت موقت به اتهام قتل عمدی در اختیار مرجع قضایی قرار گرفته و تحقیقات تکمیلی ادامه دارد./ اخبار تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/693613" target="_blank">📅 11:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693612">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f1aaa369.mp4?token=Kzb8duw9q779blmYrHu0BYB99t1LBjWnV4JCRTi1opdAekU0kwyNPZuv_ezXbhD2kvcLtzzLZwmhhkAgJjM5dhSlM620o8YQIRcYuLGlKopnyU3tibeWz7su8lAIM84Rtk3XPdAUDIZmIeUC6FxDjjhlVUi8Ks2RQv5dDEalC72uXwtsB3r2GuZjJXozNc20QqCi3aulq502J3u6RZs6Lq5bOj9KVc9p_n6cgrzG9b5a6uP8O7B7nydbaCZtkLV0ExFnRc2ToqY7vV12sOlA0uypBrQDLKJJoug7LGoPurTIdF8cP9dZIa9tOBt5hm7MJwpxjoVAkhbxo8NwDF0SgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f1aaa369.mp4?token=Kzb8duw9q779blmYrHu0BYB99t1LBjWnV4JCRTi1opdAekU0kwyNPZuv_ezXbhD2kvcLtzzLZwmhhkAgJjM5dhSlM620o8YQIRcYuLGlKopnyU3tibeWz7su8lAIM84Rtk3XPdAUDIZmIeUC6FxDjjhlVUi8Ks2RQv5dDEalC72uXwtsB3r2GuZjJXozNc20QqCi3aulq502J3u6RZs6Lq5bOj9KVc9p_n6cgrzG9b5a6uP8O7B7nydbaCZtkLV0ExFnRc2ToqY7vV12sOlA0uypBrQDLKJJoug7LGoPurTIdF8cP9dZIa9tOBt5hm7MJwpxjoVAkhbxo8NwDF0SgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ترفند جالب برای ذخیره کردن شماره کارت در کیبورد گوشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/693612" target="_blank">📅 11:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693611">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای واشنگتن: به‌زودی ساخت سفارتخانه دائمی امریکا در قدس آغاز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/693611" target="_blank">📅 11:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693610">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
منابع یمنی از حمله هوایی عربستان به مناطق مسکونی در استان تعز یمن خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/693610" target="_blank">📅 11:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693609">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40322abc03.mp4?token=WMRCpxc6kwgmzAOGuTZCl5xfpgBmqeJsTwIDy9ghZV72-PfRUkF6bWB0ubS1h9RXSHM6Xocrb2tetM5ZYtViVPGAjpOvfP-fSefrfPhaBhpcQBcE3jy5Vpcr26uuudKX2Od5m1RSqwhGZbTatwLJD9E6VF7Yz-_VEdXygcwEPP5EM31-SuxnXoyRFVJVIJesJIbIWy0lEXTaaRefydOOazlPNd4fGGtD3VEXi_hX-j-4OG9HqWagozPtr21lPDiPmaSaH01d_02HVHyECXeFUlUFzcaA2LKYdxKK1F4UEGy6qPZzwG5G6uh5dWv7HNZcPV3g1BP0RWnKX1CpgGEIuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40322abc03.mp4?token=WMRCpxc6kwgmzAOGuTZCl5xfpgBmqeJsTwIDy9ghZV72-PfRUkF6bWB0ubS1h9RXSHM6Xocrb2tetM5ZYtViVPGAjpOvfP-fSefrfPhaBhpcQBcE3jy5Vpcr26uuudKX2Od5m1RSqwhGZbTatwLJD9E6VF7Yz-_VEdXygcwEPP5EM31-SuxnXoyRFVJVIJesJIbIWy0lEXTaaRefydOOazlPNd4fGGtD3VEXi_hX-j-4OG9HqWagozPtr21lPDiPmaSaH01d_02HVHyECXeFUlUFzcaA2LKYdxKK1F4UEGy6qPZzwG5G6uh5dWv7HNZcPV3g1BP0RWnKX1CpgGEIuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های انگلیسی: پلیس انگلیس در حال بررسی ارتباط ایران با یک طرح مشکوک به بمب‌گذاری در پایگاه فیرفورد (محل استقرار بمب‌افکن‌‌های آمریکایی) است
🔹
ظهر امروز پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/693609" target="_blank">📅 11:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693608">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
دریادار سیاری، رئیس ستاد و معاون هماهنگ‌کننده ارتش: تنگه هرمز کاملاً تحت تسلط نیروهای مسلح است/ اجازه عبور به کسی نمی‌دهیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/693608" target="_blank">📅 11:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693607">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال به نقل از مقامات آمریکایی: دولت ترامپ برنامه‌ای برای فروش سلاح به چین ندارد؛ این موضوع از نظر قانونی ممنوع است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/693607" target="_blank">📅 11:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693606">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227c38c38c.mp4?token=ofRmPH6_ryO7GmORlpGZ3pUg4kjocnS7Gb2aMXXF6R33Y-5eIhKbkfKTCnfGKI0wwiAyB1Kab-LMqnRKLpMFXhNvS7Ubz3LbZvBVEblZlj1yFxUb9w1sTFSMeOV5HgakRE_HCGyZpzrPiFkOQKBrL8NQpJ3yM3NSiWs5gzNOTNP-SN3VGKU-PKxleRRzXLmBHRJtbi2C8emxlXY9cu-USQ8PlJTGLxUlXypyCse2sTzqnz6rIhEnHcETslreM4wRynMVTXQWejSIwlMNNsLZuL6_vAbyd6k39H4hNPfx5bIYJ5nvrRpsQe9TRPQlsUhilxoxDSym_iUIPZsaDgXzPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227c38c38c.mp4?token=ofRmPH6_ryO7GmORlpGZ3pUg4kjocnS7Gb2aMXXF6R33Y-5eIhKbkfKTCnfGKI0wwiAyB1Kab-LMqnRKLpMFXhNvS7Ubz3LbZvBVEblZlj1yFxUb9w1sTFSMeOV5HgakRE_HCGyZpzrPiFkOQKBrL8NQpJ3yM3NSiWs5gzNOTNP-SN3VGKU-PKxleRRzXLmBHRJtbi2C8emxlXY9cu-USQ8PlJTGLxUlXypyCse2sTzqnz6rIhEnHcETslreM4wRynMVTXQWejSIwlMNNsLZuL6_vAbyd6k39H4hNPfx5bIYJ5nvrRpsQe9TRPQlsUhilxoxDSym_iUIPZsaDgXzPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرودگاه جبل الطارق، يكي از خطرناكترين فرودگاه‌های جهان
🔹
بزرگراهي از ميان باند اين فرودگاه ميگذرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/693606" target="_blank">📅 10:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693605">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
رسانه‌های عراقی: طی ۲۴ ساعت آینده ممنوعیت ورود پروازهای ایرانی به فرودگاه نجف اشرف لغو می‌شود./ایسنا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/693605" target="_blank">📅 10:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693604">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebca546f10.mp4?token=ScYvtCl9R7NYWYehEp41j2H1k2f95d3Nf-YBULwQFOs4IyNBDMt4eXaKHptPyWhDvpC_6yLfzZJ_hNScAn1xh1N0SBvAhEdO6P78yV4JNkCeQnglMrrfwfo5wujTIQxgd8beytm3RK8YqXqGCR4ZjXI2J7Ob_7Mvh5VSJWvkJ9_sPoZYKRGnsECNTeKjFIBb0rdfIyPCoXygIY9SivzGlk7mwWlgTIxeRd0gleK_G1VmmCmraOEw4nNdkNDQTaaJw3WdUpYAE6CqPUD4xvyytPVGEUnC0AjQoJMvS9ZZJCiFQ9XN7WugJbsoRE3_WTQS0sEAe7FBx3ehBGbjUWII0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebca546f10.mp4?token=ScYvtCl9R7NYWYehEp41j2H1k2f95d3Nf-YBULwQFOs4IyNBDMt4eXaKHptPyWhDvpC_6yLfzZJ_hNScAn1xh1N0SBvAhEdO6P78yV4JNkCeQnglMrrfwfo5wujTIQxgd8beytm3RK8YqXqGCR4ZjXI2J7Ob_7Mvh5VSJWvkJ9_sPoZYKRGnsECNTeKjFIBb0rdfIyPCoXygIY9SivzGlk7mwWlgTIxeRd0gleK_G1VmmCmraOEw4nNdkNDQTaaJw3WdUpYAE6CqPUD4xvyytPVGEUnC0AjQoJMvS9ZZJCiFQ9XN7WugJbsoRE3_WTQS0sEAe7FBx3ehBGbjUWII0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیبا مثل گلستان
#اخبارفوری_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/693604" target="_blank">📅 10:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693603">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
خداحافظی بانک‌ها با چک رمزدار
🔹
بانک مرکزی: صدور چک رمزدار از فردا ممنوع می‌شود؛ جایگزین آن، چک تضمین‌شده است
🔹
چک‌های رمزدار موجود تا ابتدای دی قابل تبادل‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/693603" target="_blank">📅 10:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693602">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5K9PrRGTq9sPi-WpgZFp-md-ijj2VsAMM7yWamRM0Yp9x5Gi_oM4IDhMXo6mV7TH4CSyWzIE_HyifbQeI3hvrV6IpAKIBFDw7HuVqocn3U4k7tuAxIg3M_sQU96bLY0uBEpAscycsL2Jx9wURC2p-2jUWufqiy6ZFufz3oVwP92ZKBtaZI3OzUPAZ9CD2N6LSLE7gHXz8_VzHHo2aQqjvQ9fD2VmNLNk_FYKbV8ged54IQmLyWXW19Fnam4BZJ4pkEGKd4BZvwyh8garRgpvEAa9QYtpisBmqK7GLFlWg3hXl6UjsammVo2B05xxjaV_zxGiydTdpvjAXDH80fSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر نام تنگه هرمز را به "تنگه ترامپ" تغییر می‌دهد و قطر و بحرین را از روی نقشه حذف می‌کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/693602" target="_blank">📅 10:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693601">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0df7b426.mp4?token=uH_hyHeretWnX-ktUF9G2pfHddeYBmGgxrL9WRtCBd82AIquYHsmD9qaTw53Hgu7dc5WOL3ZFiVkFXE1OgYHOpK8Z1eSbMMA1rdCQ0QgD507B1diI0E-sfRqkA-A2jw7jfLI2CyMtZOdQpPf2upLBUfKSkjCo5gMdzsajV1nZ2y4x6_y1R9332p8ls-jyUJBMlsQRfIdwQZsNWlWreicl15K3pTlk98Zw0tZxlHG7QWgIxjbWp_MaDGHGONbvIRbPebcOMtLhNuNFLzNx5QKfrbKtAz3fZoSXHoFwTKwz8-DBtrwymUZ3bsMPfw5kLg735Y8kWF7cX0DCF1m2NWIog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0df7b426.mp4?token=uH_hyHeretWnX-ktUF9G2pfHddeYBmGgxrL9WRtCBd82AIquYHsmD9qaTw53Hgu7dc5WOL3ZFiVkFXE1OgYHOpK8Z1eSbMMA1rdCQ0QgD507B1diI0E-sfRqkA-A2jw7jfLI2CyMtZOdQpPf2upLBUfKSkjCo5gMdzsajV1nZ2y4x6_y1R9332p8ls-jyUJBMlsQRfIdwQZsNWlWreicl15K3pTlk98Zw0tZxlHG7QWgIxjbWp_MaDGHGONbvIRbPebcOMtLhNuNFLzNx5QKfrbKtAz3fZoSXHoFwTKwz8-DBtrwymUZ3bsMPfw5kLg735Y8kWF7cX0DCF1m2NWIog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات نفس‌گیر مسافر پس از کشیده شدن کنار قطار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/693601" target="_blank">📅 10:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693600">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نصرتی معاون عمران وزیر کشور خبر داد: علی رغم شرایط خاص و جنگی کشور در  دو مناسبت دهه فجر و هفته دولت ۲۴۵ همت پروژه شهری و روستایی در کشور افتتاح شد. پهپاد آتش نشان ساخت داخل در شهرداری شیراز به عنوان دومین کلانشهر کشور نیز عملیاتی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/693600" target="_blank">📅 10:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693599">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
دیوان عدالت اداری بخشنامه سازمان امور مالیاتی: بخشنامه معافیت مالیاتی املاک گران‌قیمت باطل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/693599" target="_blank">📅 10:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693598">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72e39fce47.mp4?token=o1UN_51eitd_g4TP6E_rwGPT_83nUvdb_kkN0SPfPM0rU1lFtJLdXi9MZ8rffnOw34Ct4f_6wXkBJyi0QtkF_ueUQL5LvTBc1LQzyTLzO8idV1Jvuzw1fbWoPj6LwhtxHXDo72d4DzPp4YWVSMx6c8xg68zx1f0bhPcy5g6yz8C2uLrnMaGM2bOsSjCwdrbYHmGzDtrjAaRQwrVJ918nlQSY9DWmESGTjPMzxjKLPdSapLpVg-MGUeaPBFRivhTia-YF6dnMTwxfFyMMFDgtbF_KtrZUfXW9Ocs-4FOQWCdbX-wqiFdWurOoLuuCqVsUIgOricOGEWkWR8X-UX2U7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72e39fce47.mp4?token=o1UN_51eitd_g4TP6E_rwGPT_83nUvdb_kkN0SPfPM0rU1lFtJLdXi9MZ8rffnOw34Ct4f_6wXkBJyi0QtkF_ueUQL5LvTBc1LQzyTLzO8idV1Jvuzw1fbWoPj6LwhtxHXDo72d4DzPp4YWVSMx6c8xg68zx1f0bhPcy5g6yz8C2uLrnMaGM2bOsSjCwdrbYHmGzDtrjAaRQwrVJ918nlQSY9DWmESGTjPMzxjKLPdSapLpVg-MGUeaPBFRivhTia-YF6dnMTwxfFyMMFDgtbF_KtrZUfXW9Ocs-4FOQWCdbX-wqiFdWurOoLuuCqVsUIgOricOGEWkWR8X-UX2U7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این کباب ترش خونگی خوشمزه ۱۰ برابر از کباب‌های بیرونی خوشمزه‌تره!  مواد لازم:
🔹
گوشت چرخ کرده
🔹
پیاز رنده شده
🔹
نمک فلفل پاپریکا پودر سیر
🔹
کره
🔹
گردو خرد شده
🔹
رب انار
🔹
آب نارنج
🔹
آب جوش #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693598" target="_blank">📅 10:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693597">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سوال خبرنگار: آیا حملات به ایران قبل از انتخابات میان‌دوره‌ای هنوز روی میز شما هست؟
🔹
ترامپ: نمی‌خواهم این را بگویم. منظورم این است که ممکن است، اما فقط نمی‌خواهم این را بگویم.
🔹
ترامپ مدعی شد: دیگر نیازی نیست نگران سلاح‌های هسته‌ای ایران باشیم، چون آن‌ها نابود شده‌اند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/693597" target="_blank">📅 10:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693595">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXYwZqmXe3UjeAebcfHuYOrvM_gNMDhtuonA81Nax9Qu9GqxKtDbwn1HpQBv8eB5ReVGTcg3OcJLs7XITxvyWZ91kG0rBqJPWXKc20SGj1EvRxtjoqeHDnnnmjcgtSr9_7KXCbbIrUw9xm8hGPT6MQPe8NH9WQfWrd8zIEVwPFO1sBxjkOS7igg2VCWtXBI0r2k62ROd20vUQCrlCoddfJYCBX_65u3u2hX1ot5FJ4FE57U6XyqyE8G9osDI2nVR_69cA4WXVUkW7ikpqW-gDBxngpfHyhLR1WB16gcQKAlF38Iwaqo0UtnZKwOI_uJGJbakzPJD1EJ1t_F_5rBeHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KX080WlOfLF3Nia8uynd3ZfE-jqt7KsuPSPEZqLL81QUiWHpkMi9mVZWSw1JR53JR2riqKCvFfJzO-2uIWn-zU2nsjmKTMIfxFtG-wrIR0k8sphWLv6cEvzaakI3bh5nj7o7a98r1CL99itRIdRfy_avkKLSb25CPLZfgkci01j1kpFzfXIGFwBtpIwG2JbAzM55YpenHaB46VD7WYDkBcgP7xpcXOrDIGzPGuyJp7bLcmS3Bb8zyfOfj9B5MIHlPUoI9eqh2SYF19AH6NN0qs9FP_-nJUDsX1B36r50lmDzZvcAm3afH1PfGTsCqzut6Ao9R1857nPe5D35KW46PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
یک جزیره کامل در سوئد، فقط با قیمت ۲۴ میلیارد تومان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/693595" target="_blank">📅 10:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693594">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
رسانه‌های عبری: نتانیاهو امروز برای دیدار با محمد بن زاید به امارات سفر می‌کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693594" target="_blank">📅 09:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693593">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
دریادار سیاری، رئیس ستاد و معاون هماهنگ‌کننده ارتش: تنگه هرمز کاملاً تحت تسلط نیروهای مسلح است/ اجازه عبور به کسی نمی‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693593" target="_blank">📅 09:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693591">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWK8lBY4FD_v5O7xkPWwp5zsH6yKP_qd7V_gTaIxk5g_KFIT17SIL44c7wOc6Bk9yJ8HhKbVwsFZf0EOrDw8ChmmJwPvbYXTRyHzBmjAyeNJb72MoCB1MqXMrZGgLnrJhjPZIig_PJok4gTOq2nfwxcGTjsLz4VKOd7U3CqvcB6iMKiOu4WE24wBmFEROSg8kzzyhTQld3SKwH07nh7f-CAYeapU7_HbWHVH1gmUQAvsztELjhV1zm2qf3NjBKsU0lmXpT8XNj4gnOOo1Mgneb5cMNwl-hzg0uy82QT54MK2oNnMzlQrUUl_lUYTH4e95y2nvDW3msTnBb7OnKQuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b543007041.mp4?token=KNyWPI8qbEkf3VMPH3j4B8L3rO9fK5IiGZqJWdCx31GqS4kfP44Jya8B64v277bsayB21GIh5Ye_Fk4JHh8VCF7L9ogz1n0Q3nfamL8uOk6EWqZHWKKbp9B3tD3uzG6tf6Ml6uu1anXg6_2mqNgzu8IF7X_AlE2qWqpIT6dsxSWY-4dkwlBh0Cs0cWIVIM_4wtqM01GoK3JujD1-J2RNKV1_UMCydfUtsISOcRBeOVfDQEEA0Jyj48Wp2zFNRKy9V6-b5YwG6-qHruYUL-fp2Zlzc_y2hrqvNSYCEQxVeQq7Ys1JHEvM3kJrbm4eN7D8Z3FoMLz0aiKCKkQVnWo48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b543007041.mp4?token=KNyWPI8qbEkf3VMPH3j4B8L3rO9fK5IiGZqJWdCx31GqS4kfP44Jya8B64v277bsayB21GIh5Ye_Fk4JHh8VCF7L9ogz1n0Q3nfamL8uOk6EWqZHWKKbp9B3tD3uzG6tf6Ml6uu1anXg6_2mqNgzu8IF7X_AlE2qWqpIT6dsxSWY-4dkwlBh0Cs0cWIVIM_4wtqM01GoK3JujD1-J2RNKV1_UMCydfUtsISOcRBeOVfDQEEA0Jyj48Wp2zFNRKy9V6-b5YwG6-qHruYUL-fp2Zlzc_y2hrqvNSYCEQxVeQq7Ys1JHEvM3kJrbm4eN7D8Z3FoMLz0aiKCKkQVnWo48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم وایرال شده از تفاوت سرویس‌بهداشتی بانوان و آقایان در یک مکان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693591" target="_blank">📅 09:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693590">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
صف مردم پشت اختلال سامانه‌های مخابراتی
🔹
پیگیری خبرنگار خبرفوری از اختلال برخی سامانه‌های مخابراتی در سراسر کشور و تشکیل صف مقابل مراکز مخابراتی در تهران و برخی شهرها حکایت دارد.
🔹
مراجعه‌کنندگان از ارائه‌نشدن خدمات و اعلام قطعی سامانه‌ها گلایه کردند.
🔹
داوود زارعیان، معاون ارتباطات شرکت مخابرات ایران، در گفت‌وگو با خبرفوری: از حدود ۳۰ ساعت پیش، برنامه نوسازی و تغییر سامانه‌ها آغاز شده و به‌دنبال آن برخی سامانه‌ها از جمله خرید اینترنت، پاسخگویی به شکایات و مرکز تماس از دسترس خارج شده‌اند.
🔹
به گفته او، سامانه‌ها از صبح امروز به‌تدریج در دسترس قرار می‌گیرند؛ سامانه فیبر نوری فعال شده و سایر سامانه‌ها نیز طی چند ساعت آینده برقرار خواهند شد.
🔹
زارعیان تأکید کرد این سامانه‌ها کشوری هستند و اختلال در سراسر کشور وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/693590" target="_blank">📅 09:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693589">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9587dfbc99.mp4?token=WRpwjBQ8gB4qrjpx6_uFQcf1NpaydGoIH62_EskHbUbwrLgCmAOoEp_mNwwALpYy0Je3WV2wv9Ws7vP6JYT3p3YA9Hi6KYgawXiNBy0E_7tqOtaM4-Y9NK0wYsnpLymSnpeph3Vxr2RjEy-me_pGPtzJ6n8FxBRAHOGXpVESHqZYYcZw8yBMe4F9a5UbSBnl4W1tOjSuoDFm_rQrKyzkqvNDl-NiCksmdypgu4r9zwWAm86HmGEfoeapQJxreZBE-eyW3ACcoJSPnaPflT0H26si-l38vXhD9j-O3q3mkoWNlKFgtnOI79lgi1dXEmXBhCLJO3RPqwmrqlsSFwLxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9587dfbc99.mp4?token=WRpwjBQ8gB4qrjpx6_uFQcf1NpaydGoIH62_EskHbUbwrLgCmAOoEp_mNwwALpYy0Je3WV2wv9Ws7vP6JYT3p3YA9Hi6KYgawXiNBy0E_7tqOtaM4-Y9NK0wYsnpLymSnpeph3Vxr2RjEy-me_pGPtzJ6n8FxBRAHOGXpVESHqZYYcZw8yBMe4F9a5UbSBnl4W1tOjSuoDFm_rQrKyzkqvNDl-NiCksmdypgu4r9zwWAm86HmGEfoeapQJxreZBE-eyW3ACcoJSPnaPflT0H26si-l38vXhD9j-O3q3mkoWNlKFgtnOI79lgi1dXEmXBhCLJO3RPqwmrqlsSFwLxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر حدادعادل: پوتین به یکی از مسئولان ما گفته بود شما قدر رهبری را نمی‌دانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/693589" target="_blank">📅 09:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693588">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPckvfYa2qDClo11itwGHtFf8nGIw857NDAcItZUekrJD-84mhkRW61vRG3lgRhJcMWdpGBPjxwgrTyxFusyM_GMzA1WHujURowjLK8QAHQDzcPynj0Q5eokVeSW1z9tkXljo5xnjypA3KOmVJ5ml_Y49V2UK4yz90yBrZHoawd9gBRzJaax343aD3m2i24sfURh5TpjLc481fVNi0-o04_8bPKhinbLtqnD2aIFs7owBtQhi5FjUtHYlyWAhMLI39H9vr_Gxi3og5Jd9hPX7rOhHfBpnps8Uzdx13qBRe4y8_5fT2IbfHqeF1aMCT4fVTaYru7CHIONQIktnBSkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر وارد کانال ۲۴۰ هزار تومان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/693588" target="_blank">📅 09:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693587">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9Y4zvPE0XM9QMb_TTIvDK0yJXjnxEN60iBvxcD7-Z9CKpLJyy08_sNnhnDx7I-ihWokrS0Xz0Yi8dnmniU5dtDhE_yS6AacKmAI4jr5BdgFbq1SnFxM8hPPxOFAp0jw1v2a7ER3I0xgIU3Zo6OpAJCOQhbdi2dfCNRRJed44zEtVdX4t4AQ8GU01qFCHxC3ZhfRDQEfTgqkNxddYOaKqVUx9f5g8SUYkLQiU-7jTA6v_TSeP_liZUtQpQAPngt4PUbUTRNlgIzI_kfsJORRneWyj3z4ZFv3Sq0Hqnsck6ajeHVlRJz-9Q9RASin05FFzUERQv_1lGTPkOlBEf5qzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین موج بارشی پاییز از هفته بعد وارد کشور می‌شود؛ نقشه پیش‌بینی بارش ۱۵ روز آینده به تفکیک شهرها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/693587" target="_blank">📅 09:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693585">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5380de7b7.mp4?token=bidxRqdRM8MBkzXEDEVcCXHC6xIBzY_4W_3tPFl4s3j0XwCNAkwurkwyCeQAqfVmEA39Ycfs2zPiwuayijYLT7dXosKXnSi4fPi0ZO6avMbqTUNzw7g8mYRT9Q-WhV4Bx3tawUjajaFlDBUMoiBiZKd22mf93UPzqogNiPf9hdoeifUB9iAo5dwa1sMK_VTI01xhRGQy6bsJuNZqtMFFQeCZXyaBb1Mm4gEzI5FAxhRu9f3xkX0RKho4u7fX1YUfD3ZdIhZL7L7MzRhnXczKWAHPV8OpzhEhI_Z_d2JbnlK1ddRaoHTAG2yGqpgAhL9ejWBKQ9AL7tZOULAZCfYBIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5380de7b7.mp4?token=bidxRqdRM8MBkzXEDEVcCXHC6xIBzY_4W_3tPFl4s3j0XwCNAkwurkwyCeQAqfVmEA39Ycfs2zPiwuayijYLT7dXosKXnSi4fPi0ZO6avMbqTUNzw7g8mYRT9Q-WhV4Bx3tawUjajaFlDBUMoiBiZKd22mf93UPzqogNiPf9hdoeifUB9iAo5dwa1sMK_VTI01xhRGQy6bsJuNZqtMFFQeCZXyaBb1Mm4gEzI5FAxhRu9f3xkX0RKho4u7fX1YUfD3ZdIhZL7L7MzRhnXczKWAHPV8OpzhEhI_Z_d2JbnlK1ddRaoHTAG2yGqpgAhL9ejWBKQ9AL7tZOULAZCfYBIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سیل گسترده در شرق گلستان؛ مراوه‌تپه زیر آب رفت
#اخبارفوری_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/693585" target="_blank">📅 09:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693584">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
هشدار؛ مصرف زیاد استامینوفن کبد را نابود می‌کند
🔹
استامینوفن دارویی رایج و نسبتاً ایمن است، اما مصرف زیاد و یک‌باره موجب مسمومیت شدید و مصرف طولانی‌مدت به کبد، کلیه و سایر اعضا آسیب جدی می‌زند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/693584" target="_blank">📅 09:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693583">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751c241167.mp4?token=bWpfrRAjcV2OsEjPkZRk8a460ZLOauio_3NIXka882hBRp7rmBw4d4T1spHqV-WxARShQa_JwR9aGHw0X-yb8Yf8j5Vxb0zwzA71JO6nsIZvbXrh_08jM5_XGLRZUMsr4Ng3JHwzhlN3coSqwYcQqIfQYV2R6uXpEdzXSx4LGHNP_8bxVjQQ7uOKTfdYBX8Hfo-pUIGL15xQOfPqZrzt5HFKRr_rt2pyMdmBQ4-4D4HH5CC14BNu1g1Db3JR8zCHCJvOmoBP3qUEsYZfMUgLPXe0kAWfV2Z5uclIBiRiI_CPkzlXLUncrj941ScGkXR60asBu9_LIgJCcJ4K059gq6DhhEPZn9SrQl2FgXcqWr8Jc1Xn4EQabt1TuQdaSj8F7IuQq5bbLIJI8lqSjSHbkQKywNvq8LfRKCDihcrN2IqsYAuu_QUHY9GttPVPzG5aMrITm4gjueCTZ0NhFET9m1Twalx1v3g2Nmd7MGsg3azhSVjtwWSpxRMAWjpotTTm43Fq5FHm7wvG80lyj10wS6kX6DtEQwq0G0ATqbI6t0R-k0IR3N7IQmuTTdz8i3cGU5NGGBLO8pk6Pz-NcCMaZ0ay_ZUXsrzeoHEWE0ojss-bHPPZsgzCG6edzje_zMjJY67kJ4LL_UYD4kRPP29Gk1nMPkZHi5zQVjUXaHaKDFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751c241167.mp4?token=bWpfrRAjcV2OsEjPkZRk8a460ZLOauio_3NIXka882hBRp7rmBw4d4T1spHqV-WxARShQa_JwR9aGHw0X-yb8Yf8j5Vxb0zwzA71JO6nsIZvbXrh_08jM5_XGLRZUMsr4Ng3JHwzhlN3coSqwYcQqIfQYV2R6uXpEdzXSx4LGHNP_8bxVjQQ7uOKTfdYBX8Hfo-pUIGL15xQOfPqZrzt5HFKRr_rt2pyMdmBQ4-4D4HH5CC14BNu1g1Db3JR8zCHCJvOmoBP3qUEsYZfMUgLPXe0kAWfV2Z5uclIBiRiI_CPkzlXLUncrj941ScGkXR60asBu9_LIgJCcJ4K059gq6DhhEPZn9SrQl2FgXcqWr8Jc1Xn4EQabt1TuQdaSj8F7IuQq5bbLIJI8lqSjSHbkQKywNvq8LfRKCDihcrN2IqsYAuu_QUHY9GttPVPzG5aMrITm4gjueCTZ0NhFET9m1Twalx1v3g2Nmd7MGsg3azhSVjtwWSpxRMAWjpotTTm43Fq5FHm7wvG80lyj10wS6kX6DtEQwq0G0ATqbI6t0R-k0IR3N7IQmuTTdz8i3cGU5NGGBLO8pk6Pz-NcCMaZ0ay_ZUXsrzeoHEWE0ojss-bHPPZsgzCG6edzje_zMjJY67kJ4LL_UYD4kRPP29Gk1nMPkZHi5zQVjUXaHaKDFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاشته زیبای مسی در شب شکست ٢ بر یک اینترمیامی برابر کلمبوس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/693583" target="_blank">📅 09:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693582">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه هشتم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693582" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه هشتم؛ توفیق ستایش
🔹
محبت حق و اولیای الهی، استعدادهای معنوی انسان را شکوفا کرده و شریعت را با لطافت و برکت همراه می‌سازد.
🔹
راه درمان عارضه خودشیفتگی و اشتیاق به دیده شدن، معطوف کردن میل انسان به سپاس و قدردانی از پروردگار است.
🔹
ریشه‌ بسیاری از بیماری‌های روانی، اضطراب‌ها و حتی تمایل به خودکشی، ناتوانی در دیدن نیکی‌ها است.
🔹
شکرگزاری نه تنها امری معنوی، بلکه یک روش درمانی برای اصلاح روان و بهبود روابط اجتماعی به شمار می‌رود.
🔹
استغفار و حمد؛ دو بال پرواز برای رسیدن به برکت و فیض الهی هستند.
🔹
زمانی که انسان در تردید و وسواس فکری است، نور نام مبارک
«الْحَميد»،
، مسیر استوار و صحیح را به او نشان می‌دهد.
🔹
نام
«الْحَميد»،
با جاری ساختن نور سپاس در تمام سلول‌های بدن و محیط پیرامون انسان، نگاه او را از «ناسپاسیِ جاهلانه» به «ستایش آگاهانه» تغییر می‌دهد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/693582" target="_blank">📅 09:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693581">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXqO-cXmy6PfzRtQejYtaiRs6fc-0UI6M6-lpy0Cz8CeoRH_KXRnZsbKeiZi14YVNoutW0b5jcmSwkJnmkyCZn9k7ZnUG-iYe_aVX5Z9vhXKicUdi1cmK52_xgwT8Lv26feGxPjPTCCKYvJSWbcdls8rfpvElRqIKaqmRISlc-Sl64_47WKzuhzBNI2vfzkX_0Al5BLdaRGmfkn9q5LCHAOruce3SmK5phP0hGpNHvX9Xc_3NCiBKRrgCHay9HMXUr_kuryiVvyGfdnkwNVT4LNgyMRJlh1-dPJGaOjyfANuP8-8yFWp0A2xeaxWV9L1NANyDglEORMWZpwboNCquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
مجوز رسمی خزانه‌داری طلای آنلاین برای بانک رفاه صادر شد.
طبق خبر ۱۸ شهریور ۱۴۰۵، بانک مرکزی مجوز خزانه‌داری سکوهای آنلاین طلا و نقره رو به بانک رفاه داد. یعنی طلای دیجیتالی که در اپلیکیشن «PayVal» خریداری می‌کنید، معادل فیزیکی‌اش در خزانه‌ای امن و تحت نظارت نگهداری میشه.
🎁
برای شروع: با نصب و ورود، ۵۰ هزار تومان جایزه بگیرید. هر معرفی هم ۲۵ هزار تومان + درصدی از کارمزد معاملات دوستانتون رو براتون به همراه داره.
👇
لینک نصب:
https://payval.me/app/Login?ref=8RP9NPH8
شاد و پرروزی باشید
🌱</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/693581" target="_blank">📅 09:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693580">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cbed6f4a0.mp4?token=TdJ3bL4mERCxuYT9TJa2Ur2FNhbO_pqHbbnGmDxl8Z3uTBNh9QDcdYVuZkOkqs2z36x6S2qW-7banpn6CZTwoL6i70_Eh0V-9tYWsewElfm725HGgvlQcbxi4yh02yA-LiYUVMLDMJ2hjdhIUo88J2_HutbcG-7R_BvcxKp0Pp4p_ozb4eMfwVWH9USXTzJtqGewMeuBZPiGLuBSUnJ6rGSdeABHAYq8d-cAlaJ2m00cNt4v3EhadsPUBizPA6VBUGsHNcxMD6FUrQqdidUrgdJPLV2m7JkmPUh0CO7Ztb3AGO6fcEk3N7zRmROT7Ok2jup6ALOS-Gow1NcnGDtAZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cbed6f4a0.mp4?token=TdJ3bL4mERCxuYT9TJa2Ur2FNhbO_pqHbbnGmDxl8Z3uTBNh9QDcdYVuZkOkqs2z36x6S2qW-7banpn6CZTwoL6i70_Eh0V-9tYWsewElfm725HGgvlQcbxi4yh02yA-LiYUVMLDMJ2hjdhIUo88J2_HutbcG-7R_BvcxKp0Pp4p_ozb4eMfwVWH9USXTzJtqGewMeuBZPiGLuBSUnJ6rGSdeABHAYq8d-cAlaJ2m00cNt4v3EhadsPUBizPA6VBUGsHNcxMD6FUrQqdidUrgdJPLV2m7JkmPUh0CO7Ztb3AGO6fcEk3N7zRmROT7Ok2jup6ALOS-Gow1NcnGDtAZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیوسالار: بزرگ‌ترین رویداد فرهنگی بین‌المللی ایران در سال‌های اخیر در روسیه برگزار می‌شود
معاون سازمان فرهنگ و ارتباطات اسلامی در جمع خبرنگاران:
🔹
این رویداد، نخستین و بزرگ‌ترین برنامه فرهنگی بین‌المللی کشور در سال‌های اخیر و در دوره جدید ایران اسلامی است که در خارج از کشور برگزار می‌شود.
🔹
این برنامه از نظر تنوع فعالیت‌ها گسترده است و بیش از ۱۳ عرصه فرهنگی و هنری را همزمان پوشش می‌دهد؛ از هفته دوستی کودک و نوجوان و صادرات فرهنگی تا جشنواره فیلم، کمیسیون مشترک، امضای تفاهم‌نامه‌ها، نمایشگاه فرهنگی و هنری و اجراهای موسیقی.
🔹
تفاوت این دوره با برنامه‌های گذشته، گستردگی جغرافیایی آن است. در حالی که هفته‌های فرهنگی معمولاً در پایتخت‌ها برگزار می‌شد، این رویداد در چهار شهر سن‌پترزبورگ، مسکو، قازان و آستاراخان برگزار خواهد شد.
🔹
معرفی ایران امروز و دستاوردهای فرهنگی کشور، همچنین تبیین موضوعات مرتبط با دفاع مقدس، از محورهای این رویداد فرهنگی است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/693580" target="_blank">📅 08:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693579">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ccdd49e8.mp4?token=qKhL0aJ5tst-9yVu5-I-BH49ZJQ2a7GyTOAQRHKm8wW4ZRQY3nm9dG8VBqvnhzvsWBw0GREPZ_LWw25Ud4e4ZZhfumaDN-Ia7cq5Hoe3yw_uLZBCpUggOKmJlb6rtM4ddcgiEVHLehPObWp-h_X0wICvY43scD5SWzgwWNixAUjCY9yJWdTL-5ykp6JsidX1O0buT8_CwjQOfZvYZe7MZi12G_abGjrgZBfoJJC7d5eTDAqi8BCPrMSuLCQIcwnyPCm8KGAQbJ7bK18NCjxmeDHT4oznkD7lOapaeU2LLuPnjK1kbaPNQLDdV0esHygczJASXjI9XxXiFvnisj-5kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ccdd49e8.mp4?token=qKhL0aJ5tst-9yVu5-I-BH49ZJQ2a7GyTOAQRHKm8wW4ZRQY3nm9dG8VBqvnhzvsWBw0GREPZ_LWw25Ud4e4ZZhfumaDN-Ia7cq5Hoe3yw_uLZBCpUggOKmJlb6rtM4ddcgiEVHLehPObWp-h_X0wICvY43scD5SWzgwWNixAUjCY9yJWdTL-5ykp6JsidX1O0buT8_CwjQOfZvYZe7MZi12G_abGjrgZBfoJJC7d5eTDAqi8BCPrMSuLCQIcwnyPCm8KGAQbJ7bK18NCjxmeDHT4oznkD7lOapaeU2LLuPnjK1kbaPNQLDdV0esHygczJASXjI9XxXiFvnisj-5kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط ۷ سال گذشته! وقتی همه می‌خندیدند که این ربات‌ها چقدر دست‌وپاچلفتی بودند
🔹
با نگاهی به اینکه مدل‌های هوش مصنوعی در همین مدت چقدر پیشرفت کرده‌اند، واقعا کنجکاویم تا ببینیم ربات‌ها تا کجا پیش خواهند رفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/693579" target="_blank">📅 08:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693578">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وال استریت ژورنال: میانجی‌ها می‌گویند ایران از زمان رد طرح آتش‌بس خود از سوی ترامپ، هیچ‌گونه امتیازی نداده و اطمینان دارد که می‌تواند در برابر هر اقدام ترامپ مقاومت کند
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/693578" target="_blank">📅 08:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693577">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6923b6de1.mp4?token=R0Tb9yRAnj7kdmKgLY3hmj6ekhac-EjA6sqNBV4uHTvIGu4YJwxfyZoxXytjP09A8X_uxQ1KntvfPkSOQ4FyK5g2XWjCg9rzmolxosgJPNVTEYp5wcphT-DMG9mWD_W0LiEgX4Nnm9Z0sEMfgQCmzI3IBFNVrrMkejp1yr1VHndrBXQzsg9Lvw_NdzWnt9OBsZUzdMdpoEbSuXY5KHYXSrP5RFwgSvhuZn9YF8WjYTbVjR7lzDZ_RpASlrp6O1nvTzZ2RY3bqWyOn4uEBK2VhKlSyNa79ImHot0Qqus7wVLJT66RMjTsCdwr7a64liOM06E2oEpVHt9tF9AfJIKcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6923b6de1.mp4?token=R0Tb9yRAnj7kdmKgLY3hmj6ekhac-EjA6sqNBV4uHTvIGu4YJwxfyZoxXytjP09A8X_uxQ1KntvfPkSOQ4FyK5g2XWjCg9rzmolxosgJPNVTEYp5wcphT-DMG9mWD_W0LiEgX4Nnm9Z0sEMfgQCmzI3IBFNVrrMkejp1yr1VHndrBXQzsg9Lvw_NdzWnt9OBsZUzdMdpoEbSuXY5KHYXSrP5RFwgSvhuZn9YF8WjYTbVjR7lzDZ_RpASlrp6O1nvTzZ2RY3bqWyOn4uEBK2VhKlSyNa79ImHot0Qqus7wVLJT66RMjTsCdwr7a64liOM06E2oEpVHt9tF9AfJIKcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت جدید صهیونیست‌ها؛ حمله موشکی به مسجد در جنوب لبنان هنگام اذان که بلندگوهایش را به سمت اسرائیل گرفته بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/693577" target="_blank">📅 08:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693576">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نماینده جامعه کارگری: هفته آینده بازنگری دستمزد ۱۴۰۵ نهایی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/693576" target="_blank">📅 08:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693575">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تفاوت علائم کرونا و آنفلوآنزا چیست؟
🔹
هر دو بیماری علائم مشابهی مانند تب، سرفه، گلودرد و بدن‌درد دارند و تشخیص قطعی فقط با علائم ممکن نیست؛ دوره نهفتگی کرونا معمولاً طولانی‌تر است، درحالی‌که آنفلوآنزا اغلب با شروع ناگهانی تب و لرز بروز می‌کند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/693575" target="_blank">📅 08:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693574">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50a08f0ff.mp4?token=KKSPt5Dtbb7y8G7cbd9-EsPMe2tsukyizCcj2vJHCx8qjFQJdrpAYarzKPX8eHoKBK3LcLhw8V_f9xorkd3qaPvE4SbjlqKJvPwwvZUtAeSiPCZDyIQjJ1CTQDxi9r1qK43-ya6CB13KiWWtf1n8CjFidFagDf6znzICKjTHuxyH1TGuHgWhJGF5684aHDqRjnFcIb8DJBiQLGXI7aTXSsiz9-WPJ2Sj4IbD3hHBCe0lQdNj4PMaDQqlwHAWycWq6NYkjxLXM6veh_XFZ6wxGqYvAnEPAAIyyLvmvpp2m5ydcdKAXMiZD1YI2ARHY1w3rI-BS3a9lxpuyCPHddn8wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50a08f0ff.mp4?token=KKSPt5Dtbb7y8G7cbd9-EsPMe2tsukyizCcj2vJHCx8qjFQJdrpAYarzKPX8eHoKBK3LcLhw8V_f9xorkd3qaPvE4SbjlqKJvPwwvZUtAeSiPCZDyIQjJ1CTQDxi9r1qK43-ya6CB13KiWWtf1n8CjFidFagDf6znzICKjTHuxyH1TGuHgWhJGF5684aHDqRjnFcIb8DJBiQLGXI7aTXSsiz9-WPJ2Sj4IbD3hHBCe0lQdNj4PMaDQqlwHAWycWq6NYkjxLXM6veh_XFZ6wxGqYvAnEPAAIyyLvmvpp2m5ydcdKAXMiZD1YI2ARHY1w3rI-BS3a9lxpuyCPHddn8wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی ۱۰ دقیقه طناب‌زدن؛ تمرینی ساده و پُرانرژی
🔥
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/693574" target="_blank">📅 08:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693573">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
هشدار پلیس راهور: همراه نداشتن گواهی نامه مرتبط با وسیله نقلیه‌ای که سوار می‌شوید، باعث توقیف آن وسیله می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/693573" target="_blank">📅 08:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693572">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552f5c34f0.mp4?token=Wjfrx1m-C9atBS2Ezcy_h_QSNjZhAkNWHHvM0CtnmFadvRjNgcCAsjYYAVTZ7SxkgAjimKEdqsysceW3LKf3IoMDwDIvJR3BTMOHVawQNLRF_mF_B5ksPG5fhICg6HsUGUOaYjHl_YQxc0zwAQe6irG8io4Z4iU1ECeomToD9Z-2z5rHppZJ_vclRcgFDbjB1iH5979oW1Xc4-gVNboQ7D3K05cwlkeco6AS_PlFTGCqTfxRKWzx2UtwfekV1q8cGaBkA4SaMMnrGmaTwiQ-TEwILVVT4G4nZXlF0fkjJ7oISnzFrIkkgxk3j0lAvKFcmo0ZKH0hiCW-4vI4MR3acQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552f5c34f0.mp4?token=Wjfrx1m-C9atBS2Ezcy_h_QSNjZhAkNWHHvM0CtnmFadvRjNgcCAsjYYAVTZ7SxkgAjimKEdqsysceW3LKf3IoMDwDIvJR3BTMOHVawQNLRF_mF_B5ksPG5fhICg6HsUGUOaYjHl_YQxc0zwAQe6irG8io4Z4iU1ECeomToD9Z-2z5rHppZJ_vclRcgFDbjB1iH5979oW1Xc4-gVNboQ7D3K05cwlkeco6AS_PlFTGCqTfxRKWzx2UtwfekV1q8cGaBkA4SaMMnrGmaTwiQ-TEwILVVT4G4nZXlF0fkjJ7oISnzFrIkkgxk3j0lAvKFcmo0ZKH0hiCW-4vI4MR3acQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطارهای معلق ووهان چین؛ واگن‌هایی که از زیر ریل آویزان‌اند و کف شیشه‌ای‌شان منظره شهر را زیر پای مسافران نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/693572" target="_blank">📅 08:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693571">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c3454a43.mp4?token=b96DUUoX5h0bT8le9YxmiaDLZDcc0hf3rErureLWoYUUSDTsdKuwzGCOvrD91YcCgK8lfesisrxUP9fCKfa-DAqCA6zpXnyeeOiUM8qYBPQA5zNILf2GEcsALQMShZicT6yDXo6HHKmVip1TAG4LpzEgs8PPBTU9CYiQiMyi_GXHFtBz1pTOa6NechBjHGoBEIhVzIyzJMtmmywtYeGiCGlbjRUwfh87JUiTB0xP1f2VOhUIFy3f0B8_REzYkBirrGvJ-rsn00FieAXzNY1o3vyuI3LV9j4Gc0_B15yJDYERAlr8I3NHEP2fdKXyv6Inpr5hXhqCgVE8uSpQkEHW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c3454a43.mp4?token=b96DUUoX5h0bT8le9YxmiaDLZDcc0hf3rErureLWoYUUSDTsdKuwzGCOvrD91YcCgK8lfesisrxUP9fCKfa-DAqCA6zpXnyeeOiUM8qYBPQA5zNILf2GEcsALQMShZicT6yDXo6HHKmVip1TAG4LpzEgs8PPBTU9CYiQiMyi_GXHFtBz1pTOa6NechBjHGoBEIhVzIyzJMtmmywtYeGiCGlbjRUwfh87JUiTB0xP1f2VOhUIFy3f0B8_REzYkBirrGvJ-rsn00FieAXzNY1o3vyuI3LV9j4Gc0_B15yJDYERAlr8I3NHEP2fdKXyv6Inpr5hXhqCgVE8uSpQkEHW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بارش باران در مسجدالحرام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/693571" target="_blank">📅 08:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693570">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
نیویورک تایمز خبر داد: اخیرا برخی جمهوری‌خواهان خطاب به ترامپ درباره جنگ با ایران گفتند «همین حالا تمامش کنید»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/693570" target="_blank">📅 08:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693569">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObJ-D_EvFAWqR4tkO7dUqnXWpSpAov-XgGFZ7QCQBhlRuFV4JmwpFExx6opKTxM4kjBtwQFCmhdEbcU6iChniJwYLWUUnUC__nYbNTk4_z6_Oq8jN6rzHuvXgHjOSkH5fVJeAZTb51dN6B8CWNQnW9EPLGeB-vTPvi27NpSi_TPRQsuVSQdTtUE8slZ9mIx3LsEhsifE3rBomUlwCFZNQAiY5qHFay1E5nY0znOpiKdc4QNC_KUBehVimdKPF4S9dFjy5jQ9xjMQWD9eI-paaBL_UbUB10xgrCF_2yAp7TOAxFUHXquo-2ZtLHRXkq4iVVwZjhjLXpXEbZAYbMxeMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جدید نفت بی‌توجه به تلاش ترامپ و آکسیوس بالا رفت
🔹
این افزایش بی‌توجه به خبر مذاکره آمریکا با ایران در آکسیوس و اظهارات ترامپ درباره کاهش قیمت نفت رخ داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/693569" target="_blank">📅 08:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693568">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
آکسیوس ادعای ترامپ درباره رد پیشنهاد ایران را زیر سؤال برد
🔹
آکسیوس به نقل از یک مقام آمریکایی، تبادل پیام‌ها میان ایران و آمریکا از طریق میانجی‌ها را مثبت ارزیابی کرد؛ موضوعی که با ادعای ترامپ درباره رد پیشنهادهای ایران تفاوت دارد./ صداوسیما
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/693568" target="_blank">📅 08:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693567">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
جزئیات شکار دومین زهپاد آمریکایی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/693567" target="_blank">📅 08:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693566">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8rPz2Grkop9U5fZd_K4Z4IfLplKp7qzd3ZHlKcqsJ4qKLZ0vu-FJJEeyl1wFGwCct_2Iv0AOUecvLsBrFy6oyEoxg2VhAv9mzydc9CZ90lvg5Q0--Wuzadscr67zeXvZ101aDn8AtX0lesl8zRowMB7wbwQWYIvRMv5CeIFU5j1CEXiTqP0o4HglPtKuLVAqhqNDASq5aSX0npjY3zsRlX249AU-oIGQchdQs8m9JQ4sCC7bhk_4Yk_58EveXpQA1f-iv2zUoh1G4FjEUxmjypendq6ntd_gIzD0xxEbRd9YizRBbsuti-uzMbKvcwDtuhCke9sH6-fNgvZ9JX2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۶ مهر ماه
۱۶ ربیع‌الثانی ‌‌۱۴۴۸
۲۸ سپتامبر ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/693566" target="_blank">📅 08:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693565">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnWqptSo1Vno7hMR7oVhUyOXFA4Wzqs3xitpQ7kSQ01IXivt1iY0srCLoI1WWSg7JJwI-EyK6GvyrYY2ApqQ_FLLOw5MloRKaucq_BPZiUD2K6Dx_84pJkws0JSI66zmCVCvv35HTr8RpsSaXE_qIIVm8zi8vaZoZ82MDye-AVQvjyvDiBvd6jmLtgxBzXePJXrFI6txFHBK378pBTzSps97BCbkya-f5ihqB3Syw76QX8mkDaKmGrtUjU_S7y1iwcb5RTdLuJ22ILryH9VmH9XxKFJAoQDhQop2yYgo-5hnzrgz08jWTW1vr-6D-ze3ObFG0RRcxn1yOjEeSCHeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
یکی بخر، دوتا ببر! پکیج ویژه خودرو
🔥
مینی جارو شارژی
AS-228
+
🎁
هولدر موبایل
YB20-3
✨
مکش قدرتمند ۴۰۰۰–۴۵۰۰ پاسکال
✨
باتری لیتیومی ۲۰۰۰ میلی‌آمپر قابل تعویض
✨
مناسب تمیزکردن خشک و مرطوب خودرو، منزل و محل کار
✨
هولدر با چرخش ۳۶۰ درجه و نصب بدون چسب
🚗
یه جارو جمع‌وجور + یه هولدر کاربردی، مخصوص داخل خودرو!
✅
امکان  پرداخت درب منزل و پرداخت قسطی
🔴
قیمت 1,298,000 تومان
خرید
👇
https://memarket24.ir/product/fast/63781/180124/</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/693565" target="_blank">📅 00:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693564">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16889c96f.mp4?token=rOBZKC9ae_iTqKayR-3MhfobnUIkUR1CAaH3Uu-vp71IOWGyGebumXKBGPLtQI6B_7hal6ameBd9LC9A1zFniAXNQTWk3NMwVtt-NoZpJzM0kX2JXhoocsDBudt3eoldQhV6aoTE40N3cMjeJT7H7o4MgbZGtzu9KImeBYNB8AoPT3JHbpYvf3iGoaESDCo2IcQYqw5uoRjr_C6SMhxC9BozLtcbkkSKfcWnBlhb5NL8UImIfUXekNWYWqZWgX_Mggg1GcfTQPvF6n4uTwe2wcFjgZj8ajm0vjNoZ7JqWt64SAfMZGk24JHCSCT70tzPkcXAcT6y7n2jBrEyft1xGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16889c96f.mp4?token=rOBZKC9ae_iTqKayR-3MhfobnUIkUR1CAaH3Uu-vp71IOWGyGebumXKBGPLtQI6B_7hal6ameBd9LC9A1zFniAXNQTWk3NMwVtt-NoZpJzM0kX2JXhoocsDBudt3eoldQhV6aoTE40N3cMjeJT7H7o4MgbZGtzu9KImeBYNB8AoPT3JHbpYvf3iGoaESDCo2IcQYqw5uoRjr_C6SMhxC9BozLtcbkkSKfcWnBlhb5NL8UImIfUXekNWYWqZWgX_Mggg1GcfTQPvF6n4uTwe2wcFjgZj8ajm0vjNoZ7JqWt64SAfMZGk24JHCSCT70tzPkcXAcT6y7n2jBrEyft1xGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینطوری از هر درختی می‌تونید نهال بگیرید
🌱
🌳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/693564" target="_blank">📅 00:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693563">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5eed1c3cc.mp4?token=NlMl46Wcj9atmnIkbYi90T4UdmH7gi9ZFwNg66wirnjf0Xygf9kSE7vbHQN1IXfhC7zoEKaY0ctLo1gL5sRTMO8xGRKmB_W9a-AynTdp-I0ZaZ41zYD9Ly2AdNUHCUsiJUSyOmlbZ2XcO73gmdSCpw_nF_nhdOl8DXOnjhvti-S82GGOQQsxA7zlF3kjXXos2L07zxHA-mkZ86z6CYas6s8_UBDZcgp3KHTqCsG29sN6d2L8r8ybO9QbKfbPQM9The7xOqW0Y2ZaFgC25yBYvWc9tlA6J2Q7YaoSRhJaEJHToxp_2TjJb_DNBC1f0MpUDKH-yckMGclcQrje2tLoskvJIGwO-x99rkDqZLgWjI4y7SJNaBo6dmGS5Q5WOJhWR23g5QyARmV_fUBy5u8tDdCDqVfb7i-az7DNJ2OyPFkE5CNrw8KqlQr-Ovg4whxtb9J4KeZWcom0LyGt3u6FdaRCwSr_cUcUt9zT9f_L9u4jiCtTS83LgdRHEu_CRT8Jhxx8k5LghkbZHRW6BsBAU7DBxd1_UitFkcNUf7eKJSb1meP1LxQnn8YqKa9Tqmi-jSmTWH5-Qpsn0_ehmaeRtGi5w8WVhR_0aqxcMUfaF4h95kjGt7oKREoL635EQOojCisFCWaidzaTuoOTHObdEO-NIwbjuVZcY2XUTsJDap8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5eed1c3cc.mp4?token=NlMl46Wcj9atmnIkbYi90T4UdmH7gi9ZFwNg66wirnjf0Xygf9kSE7vbHQN1IXfhC7zoEKaY0ctLo1gL5sRTMO8xGRKmB_W9a-AynTdp-I0ZaZ41zYD9Ly2AdNUHCUsiJUSyOmlbZ2XcO73gmdSCpw_nF_nhdOl8DXOnjhvti-S82GGOQQsxA7zlF3kjXXos2L07zxHA-mkZ86z6CYas6s8_UBDZcgp3KHTqCsG29sN6d2L8r8ybO9QbKfbPQM9The7xOqW0Y2ZaFgC25yBYvWc9tlA6J2Q7YaoSRhJaEJHToxp_2TjJb_DNBC1f0MpUDKH-yckMGclcQrje2tLoskvJIGwO-x99rkDqZLgWjI4y7SJNaBo6dmGS5Q5WOJhWR23g5QyARmV_fUBy5u8tDdCDqVfb7i-az7DNJ2OyPFkE5CNrw8KqlQr-Ovg4whxtb9J4KeZWcom0LyGt3u6FdaRCwSr_cUcUt9zT9f_L9u4jiCtTS83LgdRHEu_CRT8Jhxx8k5LghkbZHRW6BsBAU7DBxd1_UitFkcNUf7eKJSb1meP1LxQnn8YqKa9Tqmi-jSmTWH5-Qpsn0_ehmaeRtGi5w8WVhR_0aqxcMUfaF4h95kjGt7oKREoL635EQOojCisFCWaidzaTuoOTHObdEO-NIwbjuVZcY2XUTsJDap8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن خباز، تهیه کننده تور ایرانم علیرضا قربانی در ایران: امیدواریم اجرای علیرضا قربانی در خراسان بزرگ هم برگزار شود / این اجرا نیازمند همراهی دستگاه‌های مختلف استان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/693563" target="_blank">📅 00:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693561">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5hFLK2D-2OJk-aAd4WHiE_jMJn17RgyKBMWd_3dv7dXYkfvDtlGrKgVaLBSEwN92Gk99iZ-UvqRed_wIj_3u-d2Hs8aFNS1Er3RBAwKkf4LmH-wjACJRv_Hx9O7l0M5uHC2Hc8UHFeXHGLKqmqarLp2Xa6WNOX_KdfXKRnuaFtxOz-GPtju03C_OJjDXcntm9MX_SWmU4TY4NYB0vNQgCsUkA1xYu_2vLDZR21wBpQIWSMnSXnu8XMoP0WgKpbeCBg4fVOu28ZE3aWOoCsxAgbDtru6pGnUI7WSiqAXqKlRiAjV8RwtSc2lvie8M8uEOen-ml51pyqGVVBlypaHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaNoSZcAzanchgU8XdPb8sL-3AchXrFZieYePRuIIpq60OJSevDQ4OcYaJV1_SB1uM-jc2J0A0QbBppOEDx8oTxbYUD4Pb8wwG6l5A1RVpvqZa0RUFIc6SyzNK2Gi_67LAyKfroiLufALjJW-oanks0oV6RLxvUUwpfWUlE9wroILijxAubhUvsSjgEHbxHME7evy_rqdJNZbjafhk4NOFohK1HQ-Ifid-Ucq0VfEeqs5Mf2aluvENpwitvN_mz7Y2nmOvGoOnQUia0ZonCztfwMheUy7Qyiqe8B1zeDORudBwKogJvqHs1euLeOs2UP4tiiItbv5qgSZrVXjXPFKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
می‌دونستید در چت جی پی تی میتونید حیون خونگی داشته باشید
🔹
از این راه فعالش کنید
ChatGPT → Settings → Personalization → Pet → Select pet
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/693561" target="_blank">📅 00:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693560">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7659ca5aac.mp4?token=KMYQLBVEq1ESbzFzQtClv6SDUjtjFbBXic0HqS1H_p2FLqyUQff_3OgxTG4BNhUcBa1YuQFerx5g6mIDhDe_gXOHwmHaR1gWTPgGMyLstWFVAQZG8BMrTtZL3c5PYvm9f0HKSRTD3xLz3w4hX69pOonSr0PWIuJIpPPgj27vvec4EMKfke9A0GBpg6B3G4ac2rMt_08W5xjTvynXpM8HbMChvvpgTbdIV0gPQQ4DditnQ9E2JSuVil9B1hm0969wDig4gUw5OzM-Kgu51a--PSmeO9i0gsgxx6VCZXdTReGH1eCxJl6ePnsXDvntruIWhW2ratMyN8qs5kogMlqQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7659ca5aac.mp4?token=KMYQLBVEq1ESbzFzQtClv6SDUjtjFbBXic0HqS1H_p2FLqyUQff_3OgxTG4BNhUcBa1YuQFerx5g6mIDhDe_gXOHwmHaR1gWTPgGMyLstWFVAQZG8BMrTtZL3c5PYvm9f0HKSRTD3xLz3w4hX69pOonSr0PWIuJIpPPgj27vvec4EMKfke9A0GBpg6B3G4ac2rMt_08W5xjTvynXpM8HbMChvvpgTbdIV0gPQQ4DditnQ9E2JSuVil9B1hm0969wDig4gUw5OzM-Kgu51a--PSmeO9i0gsgxx6VCZXdTReGH1eCxJl6ePnsXDvntruIWhW2ratMyN8qs5kogMlqQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس: احمدی‌نژاد در دوره دوم ۱۸۰ درجه عوض شد / به نظر من برای رضای خدا کار نکرد و عاقبت‌بخیر نشد
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
احمدی نژاد در دوره اول خوب عمل کرد و ایشان را با شهید رجایی مقایسه میکردند، اما در دوره بعدی ۱۸۰ درجه تغییر کرد.
به نظرم احمدی نژاد برای رضای خدا کار نکرد و عاقبت به خیر هم نشد.
🔹
من خواهرزاده پرویز داودی نیستم، اما ایشان را از دایی ام بیشتر دوست دارم و مرتب برای ایشان فاتحه می‌خوانم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/693560" target="_blank">📅 00:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز جانمانید
🔹
🔹
بعد از انتخابات آمریکا "جنگ بزرگ" رخ می‌دهد؟
👇
khabarfoori.com/fa/tiny/news-3248205
🔹
معمای رد پیشنهاد ۷ روزه؛ آمریکا چه می‌خواهد؟ | مسیر بعدی ترامپ چیست؟
👇
khabarfoori.com/fa/tiny/news-3248252
🔹
همه‌چیز درباره محکومیت یک نماینده مجلس به زندان | شاکی کیست؟
👇
khabarfoori.com/fa/tiny/news-3248230
🔹
هوش مصنوعی چطور جایگزین نیروی کار می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3248284
🔹
خبر مهم برای کارگران؛ توافق اولیه برای افزایش دوباره حقوق | رقم جدید مزد چه زمانی اعلام می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3248171
🔹
خبرهای داغ امروز را هر لحظه اینجا دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/693557" target="_blank">📅 00:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e62f34627.mp4?token=iVPrfBEWSpAs4gN77LV8YJNROQR8juR-VAqLC7MXKp5I5FKO7FvTh9VGoPQFIk6tg9HBlVAHVX5ODPLXdUugruvSfcTzsxBfQ3WrF7Qfc9QnF-8wrYRbo7If_KGGdHWwzt2kt4GUgUnexPa9r-GvyogQdLDF6oC_rEy2ypncUhbZkaG2Ne-y8UOsUnU_ycTY-5bgQMGHQzzS2hE1tMJxevUo540c3hBFQinouW_6Dg3DJjnjT_CGFhpuqwX7j408xhcJxscCHjEDcdwN1iY9ynpdbQCudy5yx3-fbdKFNCT2mxjrktdiBhEvqGO00nJWv7IOjsahDZ4RYC9l6J7R_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e62f34627.mp4?token=iVPrfBEWSpAs4gN77LV8YJNROQR8juR-VAqLC7MXKp5I5FKO7FvTh9VGoPQFIk6tg9HBlVAHVX5ODPLXdUugruvSfcTzsxBfQ3WrF7Qfc9QnF-8wrYRbo7If_KGGdHWwzt2kt4GUgUnexPa9r-GvyogQdLDF6oC_rEy2ypncUhbZkaG2Ne-y8UOsUnU_ycTY-5bgQMGHQzzS2hE1tMJxevUo540c3hBFQinouW_6Dg3DJjnjT_CGFhpuqwX7j408xhcJxscCHjEDcdwN1iY9ynpdbQCudy5yx3-fbdKFNCT2mxjrktdiBhEvqGO00nJWv7IOjsahDZ4RYC9l6J7R_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جیرجیرک غول‌پیکر مالزیایی یکی از بزرگ‌ترین حشرات شناخته‌شده در جهان است؛ اما برخلاف بسیاری از جیرجیرک‌ها، شکارچی و گوشت‌خوار است
🦗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/693556" target="_blank">📅 00:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693555">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvqWaAFAB4UlzMvoPCafEj8GDOPrdMoG9PXjrzQP0hRbgWo4l5GBal1QEr6tfksigj1atWdfIql4Jmv1FwM-4yfnoQZs7gkF6Q9jSjwEojPo88j1K8Q-6pVABe3CdcFIxhwrXMROiWXnHxVk0ntAuKWYG9-UMEIVle6TXTivp_eWyjRGNGdg7l5RKB-Ql0qErm2ffjH7Hly15-rB8KRKkeeSurK1uj0Sd6bb-zQ9GVNQlKGBGxhdIGwv5b3W1LKhAZFPygB0Ijih25DHNcNZWrE0KIlLkwPdB7rf_JQRSArg8EIgrgLKxMcn0QpQlbcUheBRynr6zSaBOSEMJVd6iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👟
کفش اسپرت نایک V2K Run | سبک و راحت
🔥
مناسب پیاده‌روی، استفاده روزمره و استایل اسپرت
✨
رویه مشبک + زیره نرم و راحت
📏
سایز ۴۱ تا ۴۴ | ۴ رنگ
🔴
قیمت: ۲,۱۹۸,۰۰۰ تومان
💳
امکان پرداخت درب منزل و پرداخت قسطی
✅
ضمانت تعویض ۳ روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63638/180124/</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/693555" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693554">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUCtfVzUGZh78Rf7t6cGAiXJrs2iukg-Ic0rClibZpWcY8F55iELPSVejtVxcxbd_0bbt71IB90gODCQsc-od6nLAZ6Onv04f9nNgynbyyRhRkHMj-uOhhv3FsDYfvQVg56UzQdnnDH71hujq2Qllm-klf14cYlhVEhn5z18es5wDV8YdvXufvAw-Z9fFaDolh80KltsW1VKU4mZhcuuQU4BE57u_paUfLkIxAvPjkMBXXJwTetFQmXLq_EOeqFs3MJs5CKwe4N2XoC7s535grSoE8k45HsRvVLiGNmkM0TVfyp-EkcVXsJj_Dox1tpBgks08zSWni0FH2JvhukQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/693554" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6611008e.mp4?token=pGsYyEXGJt9gFNpsYzLnxReEy_VENcnyt6GcdryZJCGOlPNnZxuRRXK32lk0BMwxRIzbclosPu7Ucz4TvH8BKN6dT6OJNthdX7H2K1FWQ9hv27LS10u5f55H2xDWqqFpCTbdQy8hwNckzSmWYSu0ItdWoy3U_JFTWxGKGslkXFAJqhR94Umwv6iHqAg5VwBINcv8TnCF3F5TddaBwBojPA4pFMv_n7uYNbFp7GBVrr-YR7evgafWUTPMBcRQTl1SD48XGfw6eUMivlJQET6iMx4z8BrFd5F7FaRrWttbOzVH0W7TM8eeeid6G4CV9tDCwQ2grccoUhsft7x_RGfuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6611008e.mp4?token=pGsYyEXGJt9gFNpsYzLnxReEy_VENcnyt6GcdryZJCGOlPNnZxuRRXK32lk0BMwxRIzbclosPu7Ucz4TvH8BKN6dT6OJNthdX7H2K1FWQ9hv27LS10u5f55H2xDWqqFpCTbdQy8hwNckzSmWYSu0ItdWoy3U_JFTWxGKGslkXFAJqhR94Umwv6iHqAg5VwBINcv8TnCF3F5TddaBwBojPA4pFMv_n7uYNbFp7GBVrr-YR7evgafWUTPMBcRQTl1SD48XGfw6eUMivlJQET6iMx4z8BrFd5F7FaRrWttbOzVH0W7TM8eeeid6G4CV9tDCwQ2grccoUhsft7x_RGfuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوباوه بابت ادعای «دستکاری» تبرئه نشده است
🔹
بررسی حکم دادگاه نشان می‌دهد نوباوه تبرئه نشده، بلکه بابت استفاده از واژه «جعل» به توهین محکوم شده است.
🔹
در ادامه، بازنشر این ادعا در هفته‌نامه «۹ دی» به محکومیت ۱۰ ماهه حمید رسایی منجر شده است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/693553" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMaEeXlACQKFGInwZjRrVBTtorGtWoOhUKAP_VrHstPNIaTnRYkWf9e3SmP_-6ku9TMGp_jFq077YaV9StverUJ0tBPliIKFZ5VhZ92-6CKttXRwdNCSQWfDXQwGeD3ih9GeCvLNId4qB_DnszqCgq2Q-L124uNMd_kxR7nh536H0Q5VEngZp6IHLcw_16F35iIiBpuaG0tBPPpeHcpdtiF3R8FtTAPxORiUzH86oXIDNCFy9nEGuNsv3eeLbY0UhS1nxiESR7qFRzVRbSZXoYetISxs3HiREABInyvQ_KODZT6Y2HSaGQB8zhszCJJlB3MMvVt7bcVhQJY7dRqaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بار دیگر نام تنگه هرمز را به "تنگه ترامپ" تغییر می‌دهد و قطر و بحرین را از روی نقشه حذف می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/693552" target="_blank">📅 23:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-Nrk-CLhtbsniDhISfeGzEg6bYAeRPIwfu8EMk9Zkry_iEdn5X9UPx03UvRUd8BaYTiIg2FPZBpxOS82JcQDa9i02MtaMRKjzXkM_XTFHvI3ZnjCL8hVUf8hMUhFzkW7okRlw9e2sMGUB300fk2KragMssJZwjbBPp3cIGzebT3S52xSlrWLUgNXfhb3FfaYb7zBMQkDzkqcBqaGPj8-uOVks1ixREhkNDUJACj5xFzhTNsVKL8de313ge2t_NsekwOypPg2DJQfWnL8lKywqQTDry4VauxA9-B4_JiOQm6mZwz9W3iwC-UCoC_SYMI3QCNz-JA9m-MmBIwmzSrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای بسنت: تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی‌مانده است؛ ایران دیگر چیزی نخواهد داشت که در ازای آن بتواند چیزی مبادله کند
🔹
ایرانی‌ها می‌گویند اگر توافقی حاصل شود، تنگه‌ها را باز خواهند کرد. تنگه‌ها باز هستند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/693551" target="_blank">📅 23:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وزیر خارجه عراق: خروج نیروهای آمریکایی از عراق به‌طور کامل پایان یافت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/693550" target="_blank">📅 23:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693548">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
قایق‌سواری در خیابان‌های سیل زده در لانگ بیچ تاون‌شیپ در نیوجرسی آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/693548" target="_blank">📅 23:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای بسنت: تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی‌مانده است؛ ایران دیگر چیزی نخواهد داشت که در ازای آن بتواند چیزی مبادله کند
🔹
ایرانی‌ها می‌گویند اگر توافقی حاصل شود، تنگه‌ها را باز خواهند کرد. تنگه‌ها باز هستند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/693547" target="_blank">📅 23:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693546">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3215fd10.mp4?token=Ge6l4ta2f4d44Bsey_TYZrHN0wzt3vZPC-HVw_m8Ekz7pTIy8MifvFbYWRH4Aqq4bwaeym85VR2HoXlkxIbi1okyaDfpiP1y-xsrClEeTqUCtp6q_r1qHsWmxyGQyI2inHFQwrwGRWWdLatjgsLQE-jMgEQv-WB8-7AUoEktyEAJvlGNwi9cMQUV_WRT5glVYEW95jNVJ38m1P8OpRdb6voWcLt-M-Ox7ORIyNpKqglu8rIPkGdHrJQZ7N5uX8F0gj22B_3nqV7WYMEkbtKtklCWEq7tUN6USGUsMfntWW3UKC2u4aTuN-EPSq8BX5D16FHUIq_aC4JuLddRufjKwkBQ0VDULU2X-PKr03regzo2GeIIZ-qXIEhR7shAQuEoV0zRAKbCrz57GA0mFJq1Gx_wiVlV6-7lMQDirh0rsAewQdnUHZv5jMs0HVT8zAOVpM97AR2w-LZHBvnZi1uNBzrZph8QSvyLfNEL2r2eu4BhK6wnCu7mgdRaVTkgqNs4CDvQUUM-AAQ-QTRnaBiQqR-yMvHoJkieQOC--XRDcOZfDO0po4LsRPRqvtsyVH1ZMd3y13Tbuq52NtZfmias2pyMwY3apEbe6CGJDOK_P14zE8HyPKFIozp0uP2R2btI8kRUoSsp72AoEakTL3Kj9oLvh88n_4lJAukqbiKN058" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3215fd10.mp4?token=Ge6l4ta2f4d44Bsey_TYZrHN0wzt3vZPC-HVw_m8Ekz7pTIy8MifvFbYWRH4Aqq4bwaeym85VR2HoXlkxIbi1okyaDfpiP1y-xsrClEeTqUCtp6q_r1qHsWmxyGQyI2inHFQwrwGRWWdLatjgsLQE-jMgEQv-WB8-7AUoEktyEAJvlGNwi9cMQUV_WRT5glVYEW95jNVJ38m1P8OpRdb6voWcLt-M-Ox7ORIyNpKqglu8rIPkGdHrJQZ7N5uX8F0gj22B_3nqV7WYMEkbtKtklCWEq7tUN6USGUsMfntWW3UKC2u4aTuN-EPSq8BX5D16FHUIq_aC4JuLddRufjKwkBQ0VDULU2X-PKr03regzo2GeIIZ-qXIEhR7shAQuEoV0zRAKbCrz57GA0mFJq1Gx_wiVlV6-7lMQDirh0rsAewQdnUHZv5jMs0HVT8zAOVpM97AR2w-LZHBvnZi1uNBzrZph8QSvyLfNEL2r2eu4BhK6wnCu7mgdRaVTkgqNs4CDvQUUM-AAQ-QTRnaBiQqR-yMvHoJkieQOC--XRDcOZfDO0po4LsRPRqvtsyVH1ZMd3y13Tbuq52NtZfmias2pyMwY3apEbe6CGJDOK_P14zE8HyPKFIozp0uP2R2btI8kRUoSsp72AoEakTL3Kj9oLvh88n_4lJAukqbiKN058" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس: فشار سیاست‌های غلط اقتصادی بر مردم، بیشتر از تحریم‌های آمریکاست/ امروز در شرایط بن‌بست قرار نداریم
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
اعتقادم این است سیاست‌های دی ماه، سیاست اشتباهی بود که اگر آن را اجرا نمی‌کردید بعد از جنگ، مردم این‌ همه دچار مضیقه نمی‌شدند.
🔹
نمیخواهم بگویم جنگ تاثیر تورمی ندارد، اما نکته این جاست سیاست‌های غلط شما آسیب بیشتری دارد. با اصلاح سیاست‌های اقتصادی میتوانیم جلوی تورم های فزاینده را بگیریم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/693546" target="_blank">📅 23:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693545">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c7483d4e.mp4?token=HEfKjrSzVo0FCU9aQKFiRNOPW4TYenVswzvQqDc2N81XwYRvXJiBKIEzLEIV7T_TWBELgpkPbNlPugl4kVmClgycwecniC4r04ThRIS6C2t6WUGYN1cFWlRY-MWlwlPGCSNogLVuVqnBq1J7fkipHuXXrrUFzzEOP0WF3dO9TovR-S9KB6OYW5hn5FTk1lMDMu46imxROmE4Nxom2YYE_y2-zzXMuf_xk_NiisxoYwNbboHEIgFRemIeFpMrUonsxTkD6e_4G1RsE0eb8xFpLDj-V_jvNeWPUMGmdEgJuCz4Cg0E3REkQgk1mf1I7ybVFAfRjKPu89OkGlL9ZtbIhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c7483d4e.mp4?token=HEfKjrSzVo0FCU9aQKFiRNOPW4TYenVswzvQqDc2N81XwYRvXJiBKIEzLEIV7T_TWBELgpkPbNlPugl4kVmClgycwecniC4r04ThRIS6C2t6WUGYN1cFWlRY-MWlwlPGCSNogLVuVqnBq1J7fkipHuXXrrUFzzEOP0WF3dO9TovR-S9KB6OYW5hn5FTk1lMDMu46imxROmE4Nxom2YYE_y2-zzXMuf_xk_NiisxoYwNbboHEIgFRemIeFpMrUonsxTkD6e_4G1RsE0eb8xFpLDj-V_jvNeWPUMGmdEgJuCz4Cg0E3REkQgk1mf1I7ybVFAfRjKPu89OkGlL9ZtbIhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از لحظه تصادف سنگین در جاده چالوس
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/693545" target="_blank">📅 23:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693544">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
منابع محلی از شلیک کروز دریایی به یک کشتی متخلف در مسیر غیرمجاز تنگۀ هرمز خبر می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/693544" target="_blank">📅 23:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693543">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
خبرنگار cbs: یک مقام ایرانی به من گفته که مذاکرات روز دوشنبه میان ایران و آمریکا لغو شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/693543" target="_blank">📅 23:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693542">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1BdLAqauaGOBVAGFp6fvDGSVVBMXjtri8IzVNoLtsIDtSBk3tzbsU6KPSZ8W-e9jNgGJMv_hQAw_Eg9V617SWfDBvVAeWeTOdHwkE_nnQm08WTCJWrrlkQFCUflDmsPyln33P9b6A_WfQUXDX8ak-aprqSOo9XMKlTI9pNxlFVAZt6yqVTEPBNteCVLQ6-W9TzjcNV7OixiByP4gC_x_CswyuWc8w5RHU4uDZdeasNe6Ze5hEF57GH2DA1o8RSXYWz1tndYQALcU7Bj8DULrZwTpBNhn76fNfstza1EZb_ATbQk4Hp4XjzouXxDtJ393Q3WtzOjuXeQ9GR8BIEfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال‌رسانه‌ای آمریکایی: ایران هر کاری دلش بخواهد می‌کند؛ اصلاً ذره‌ای برایش مهم نیست ترامپ چه می‌گوید یا چه کار می‌کند
🔹
ترامپ بهتر است یک‌بار برای همیشه بزرگ شود، این غرور نحیف و شکننده‌اش را کنار بگذارد و آخرین پیشنهاد ایران را قبول کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/693542" target="_blank">📅 23:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693541">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2PHYNWZc36-ISlQ3H_o2V3_O5aohCYB4dUudP6BYX6mVtLXQBC9sZNc7HRFFEuXuXm7cYJmYjQa9ioLrQ8fyt8cYH3rVBH75ve7ZfjUuvZovLZHPvgS_tZsTGzZdze24EZe8uOT2hTgZ2BkAU4vQOogqTd6sW8I27bBAsbqFjIG93_zlCsucNeHhUhDgVHk6cyCWnMntXjUS4TGlDhQrM_vgiv-hTXuTgup8Xot4gmtOdErmRdii5XFq-GxJZv_k3Mxd0gLvjclEtmtPsxkDHxa-zfrk7rw0BxJ1ANJ3fG0V1lwb9aJJ7gkPeDWTqm-rG1CuQueK8xb3Ay4JFAVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: غنی‌سازی ۶۰ درصدی قانونی است
🔹
غنی‌سازی ۶۰ درصدی در چارچوب NPT و برنامه هسته‌ای صلح‌آمیز ایران قرار دارد.
🔹
ایران برای ادامه مذاکرات، آزادی دارایی‌های مسدودشده و پایان محاصره اقتصادی را خواستار است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/693541" target="_blank">📅 23:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
بررسی برنامه پروازی شهر فرودگاهی امام خمینی (ره) حاکی از آن است که امروز ۵ مهرماه ۴۰۵ شرکت‌های هواپیمایی داخلی حداقل ۲۴ پرواز خروجی و ورودی به ۱۱ مقصد خارجی انجام داد‌ه‌اند./ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/693540" target="_blank">📅 22:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693539">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921f1bf341.mp4?token=r7FAV341diCH8rbnKvOCT0ymmLTaXdOxbOM0D4VAPZ2cxwNOsIiCWw1GsHqG9EuAW_0WEASKQ_4h014WhDAZHHG8P0ZLrIoeEB415f8ywylZSMtuSgNkBsTszZ7Zl4kbFFGQ-FWzi9IQ_hZKy6zX1UlMnOk76Wngn91NHkRIg3jl6Vf32Eej1Hrt8ESWwNSFMRijprG5ujswYxlAlz37VlDkaXvNO5SnOSQ7B7b9dvnUaTUxfxfSam_APV3y9u2PYXr_L0KPBTMnRcPKGY3pEtcGZ_KjLrpHanbKeB-QbrQgyDi83_CPx8UmJQSi13ROtRfZPsE9tT7f_C_7eh_mOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921f1bf341.mp4?token=r7FAV341diCH8rbnKvOCT0ymmLTaXdOxbOM0D4VAPZ2cxwNOsIiCWw1GsHqG9EuAW_0WEASKQ_4h014WhDAZHHG8P0ZLrIoeEB415f8ywylZSMtuSgNkBsTszZ7Zl4kbFFGQ-FWzi9IQ_hZKy6zX1UlMnOk76Wngn91NHkRIg3jl6Vf32Eej1Hrt8ESWwNSFMRijprG5ujswYxlAlz37VlDkaXvNO5SnOSQ7B7b9dvnUaTUxfxfSam_APV3y9u2PYXr_L0KPBTMnRcPKGY3pEtcGZ_KjLrpHanbKeB-QbrQgyDi83_CPx8UmJQSi13ROtRfZPsE9tT7f_C_7eh_mOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا می‌توان از ابتلا به آب مروارید چشم پیشگیری کرد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/693539" target="_blank">📅 22:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
آخرین وضعیت زائران عتبات پس از توقف پروازهای بغداد و نجف
🔹
پس از توقف پروازهای بغداد و نجف، معاون عتبات سازمان حج و زیارت از انتقال زمینی زائران و عودت مابه‌التفاوت هزینه خبر داد. به گفته او مرزهای زمینی باز هستند و پیگیر بازگشایی فرودگاه نجف هستیم./ ایسنا…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/693538" target="_blank">📅 22:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
رسانه‌های عبری: نتانیاهو امروز برای دیدار با محمد بن زاید به امارات سفر می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/693537" target="_blank">📅 22:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693536">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6a91c17b.mp4?token=CpRU6vGe6h5KIsUDJntI9asqw-MvyjjTHTqYkVLTcGzCkJ26uhLDdTjsk7k5X1ZSDSVzhmR6J5l3kLwEuTbLZw7pmw_s__G7PfK-C2IKHpoxSzzFdSOh9zdMcII4d6ZptVb0fSGXkpPAr5uskfZFBWqfR6tna-0ShUftSmH8JZ6-nsSo9f7qeyHn0JEQyL2nsQCf1hW20EG3AZyOD5mcnNL-jW19rj6e-Vg0TYIwnF_b69_Y8nhpZh6SpEJ1dIzbr927GbQkGcbrh-6hznTu9v6x6U-bAIZ1-t6dgIJ1GDIfoSPJ_0ZV8E_J_t3x9YlHQz5Y3XEH4KS2KKKr6Bpe3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6a91c17b.mp4?token=CpRU6vGe6h5KIsUDJntI9asqw-MvyjjTHTqYkVLTcGzCkJ26uhLDdTjsk7k5X1ZSDSVzhmR6J5l3kLwEuTbLZw7pmw_s__G7PfK-C2IKHpoxSzzFdSOh9zdMcII4d6ZptVb0fSGXkpPAr5uskfZFBWqfR6tna-0ShUftSmH8JZ6-nsSo9f7qeyHn0JEQyL2nsQCf1hW20EG3AZyOD5mcnNL-jW19rj6e-Vg0TYIwnF_b69_Y8nhpZh6SpEJ1dIzbr927GbQkGcbrh-6hznTu9v6x6U-bAIZ1-t6dgIJ1GDIfoSPJ_0ZV8E_J_t3x9YlHQz5Y3XEH4KS2KKKr6Bpe3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای خرید ۴.۵ میلیارد دلاری بانک مرکزی چیست؟
🔹
دارابی، دستیار ارزی رئیس کل بانک مرکزی: بعد از
اصلاحات ارزی دی ماه ۱۴۰۴،
کاملاً طبیعی بود که کشور با مازاد عرضه ارز روبه‌رو شود.
🔹
بانک مرکزی با پیش‌بینی احتمال وقوع جنگ و محاصره اقتصادی، از این فرصت بهره برد و
حجم ذخایر ارزی خود را تقویت نمود.
🔹
این اقدام به‌موقع سبب شد تا در شرایط حساس جنگی،
مسیر تأمین کالا بی‌وقفه و مستمر در جریان باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/693536" target="_blank">📅 22:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693535">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349fc46bcb.mp4?token=AO0xLuiSHQiMY0ilbt9_tC2IyQosqlbH-EOevJH7UvHKgH8eMfVzFPm45YCCl0MS_-kA2wDsk11RjrZI4Q8yxCVWkwmiKAGQufxkEMB3gSXoLl6UKtYMfK7hfzo_u_PsfBRFbYyizc6hnZGE4LGcJpuO9o9oEBplSHtR4f4O3_DuBxPIh5pOoUeu1WvofWltDVfJ9zCd8s-6L5gDS8U33eM3bsx2X36-eLt743oB0oQnetfZq1FK9TvXr3pCAeewD4ApSWNgilmTw09B3p49XnjDRWvcWRJhb7U2I7GAsT1THYCDV8NnIFk0i-nvrJ8Osgb7nGnFYjpuC07tumRsqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349fc46bcb.mp4?token=AO0xLuiSHQiMY0ilbt9_tC2IyQosqlbH-EOevJH7UvHKgH8eMfVzFPm45YCCl0MS_-kA2wDsk11RjrZI4Q8yxCVWkwmiKAGQufxkEMB3gSXoLl6UKtYMfK7hfzo_u_PsfBRFbYyizc6hnZGE4LGcJpuO9o9oEBplSHtR4f4O3_DuBxPIh5pOoUeu1WvofWltDVfJ9zCd8s-6L5gDS8U33eM3bsx2X36-eLt743oB0oQnetfZq1FK9TvXr3pCAeewD4ApSWNgilmTw09B3p49XnjDRWvcWRJhb7U2I7GAsT1THYCDV8NnIFk0i-nvrJ8Osgb7nGnFYjpuC07tumRsqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات شکار دومین زهپاد آمریکایی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/693535" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693534">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8af71c1f.mp4?token=oIs6Jn8rxstR-jwIx6xexzX_Wi3cQ657F89_lJnRVOvMs2pCBBRSzoYxdh01SucrOS5is393AGE6hro-YmLsIwlRqTRIDicwLziwYwp67FRRYCTQOKRD_Iye1tOUHYY4JkxDngUHGv1t2Cu7krd3p2CdlRJWmu2skJkJ19TUWwPWpzkleaqVo1grI88SR1Qfp0iltZ1uDl4HEUv5rHms1TAIpXVwiA3AWj3HCzv2YXgPSmkKbfarDPWp6zuDphvNwgV6VBt9xqVWltaNUJ9mnT5zYcXSijhgJfASBRXb9J2NruIoBSUO24xh0a5G1zWJ9kvVo8xg1hLSa_5eBoA2TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8af71c1f.mp4?token=oIs6Jn8rxstR-jwIx6xexzX_Wi3cQ657F89_lJnRVOvMs2pCBBRSzoYxdh01SucrOS5is393AGE6hro-YmLsIwlRqTRIDicwLziwYwp67FRRYCTQOKRD_Iye1tOUHYY4JkxDngUHGv1t2Cu7krd3p2CdlRJWmu2skJkJ19TUWwPWpzkleaqVo1grI88SR1Qfp0iltZ1uDl4HEUv5rHms1TAIpXVwiA3AWj3HCzv2YXgPSmkKbfarDPWp6zuDphvNwgV6VBt9xqVWltaNUJ9mnT5zYcXSijhgJfASBRXb9J2NruIoBSUO24xh0a5G1zWJ9kvVo8xg1hLSa_5eBoA2TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی وایرال شده از حلزون‌تراپی برای شفافیت پوست
🐌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/693534" target="_blank">📅 22:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693533">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2187d0c12c.mp4?token=ed-lL7Qb9FN7q54ynr-TgUjG4ioabdDsd2uuEYgEGQ2KOIYFzU4C6i8TXFALkOfcTJq6ze0-zQnSdGSHoasz0kjK-gMOEmgAiTvH4N0jJeRhV--98VueS6aiqYnJKyM6XXbGYssCOZlfRD_RTWZZNgv5Vft8dy_YZs7YfgyxLnuFHvH9tbJlDY7v4bWOtIxDrKrLrsYR3wNjI5EXH4yfUyYA75SnEiIJkXLB_LzVxS0GgiG0yL2-1txe0wxHidmGi42bAMgV2PLOk7HWTHvkeFJ9PkVBfnWwQNe5uEj9R8nmL__ICV2fzv2hFmkPU9fPhP7m3GTRURu_K2A92fpkjhcLnEB7GIoNB25GVWDz8WDE1CBaASloeN5pMyII2fegHgGYWgNwSCr22TzvlcNSQGnwmMR10Z3NT5rxpQYPvOM9pHHTsT7j_DgNPxNH9Vvhn7ddd1UY26Ocz35UAXLIRTbOIzOc6_iNRBwXnYIwCIVE78FmuYlO4fcbG90qzNcMCYEEOsYnSggQeiOohsyOsXurpWy2D1xV1Icp6fKpHte-rPCPblDbl9zmtDTI6n8Ybl2X3ha6L1n5OHfEGV77U9ms2xjRXfdQ1jyu1pr_KSPwhuR_D4u-8HtEZ4ogslmg7Q9_ATL2apAtLCWFpMI8h_m2C9EFqvscXnEt7XCTVPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2187d0c12c.mp4?token=ed-lL7Qb9FN7q54ynr-TgUjG4ioabdDsd2uuEYgEGQ2KOIYFzU4C6i8TXFALkOfcTJq6ze0-zQnSdGSHoasz0kjK-gMOEmgAiTvH4N0jJeRhV--98VueS6aiqYnJKyM6XXbGYssCOZlfRD_RTWZZNgv5Vft8dy_YZs7YfgyxLnuFHvH9tbJlDY7v4bWOtIxDrKrLrsYR3wNjI5EXH4yfUyYA75SnEiIJkXLB_LzVxS0GgiG0yL2-1txe0wxHidmGi42bAMgV2PLOk7HWTHvkeFJ9PkVBfnWwQNe5uEj9R8nmL__ICV2fzv2hFmkPU9fPhP7m3GTRURu_K2A92fpkjhcLnEB7GIoNB25GVWDz8WDE1CBaASloeN5pMyII2fegHgGYWgNwSCr22TzvlcNSQGnwmMR10Z3NT5rxpQYPvOM9pHHTsT7j_DgNPxNH9Vvhn7ddd1UY26Ocz35UAXLIRTbOIzOc6_iNRBwXnYIwCIVE78FmuYlO4fcbG90qzNcMCYEEOsYnSggQeiOohsyOsXurpWy2D1xV1Icp6fKpHte-rPCPblDbl9zmtDTI6n8Ybl2X3ha6L1n5OHfEGV77U9ms2xjRXfdQ1jyu1pr_KSPwhuR_D4u-8HtEZ4ogslmg7Q9_ATL2apAtLCWFpMI8h_m2C9EFqvscXnEt7XCTVPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نماینده مجلس درباره خرید ارز و طلا توسط شرکت‌های دولتی
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از دلایل از بین رفتن ارزش پولی به خاطر رفتارهای مردم است که رفتارهای مردم نیز تحت تأثیر سیاست‌های اقتصادی دولت است.
🔹
در حال حاضر میدانید چه میزان ارز و طلا توسط خود شرکت‌های دولتی خریداری می‌شود؟ وقتی مردم می‌بینند که دولت هر روز ارز را تضعیف و تورم را تحمیل می‌کند، چنین رفتاری بروز می‌دهند. اصلاح سیاست‌های اقتصادی باید توسط دولت انجام شود نه مردم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/693533" target="_blank">📅 22:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693531">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
آخرین وضعیت زائران عتبات پس از توقف پروازهای بغداد و نجف
🔹
پس از توقف پروازهای بغداد و نجف، معاون عتبات سازمان حج و زیارت از انتقال زمینی زائران و عودت مابه‌التفاوت هزینه خبر داد. به گفته او مرزهای زمینی باز هستند و پیگیر بازگشایی فرودگاه نجف هستیم./ ایسنا…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/693531" target="_blank">📅 22:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693530">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تصاویر منتشرنشده از لحظه شهادت سید حسن نصرالله در ضاحیه لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/693530" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693529">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635f76368c.mp4?token=HM5kTFDTlFg-uuKQfmXn2b1vfZTq-LIdTN-ZaecYIwVlmTZdYC0h7ZDfyvfwVfXrfz4gUXCMKEPpRHOgav4hCpP_o3Iio2VtIyhbxxMiVn3y6z0GTo1cfmA9gVhWAunY6IKO5-OWgKds2GZjDJ76UYdA8BNaKj7X9xvmGT98Hoix1igZpzyHsx5I4AeieEIlbXuDP7d0hFPpskR3BSNtYGGQDnVzy59iY1NNt7yPaOXqrPaQ0F-XjLIj7jhXhPWgPCPIT2k4ftvmTHlJbYMjcNFlxZ1Op-VpLe-RmdY2s8hEL5kRiis2jEPo5ck3V2UqHIlwHcD8C1HCI0Mu3DGkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635f76368c.mp4?token=HM5kTFDTlFg-uuKQfmXn2b1vfZTq-LIdTN-ZaecYIwVlmTZdYC0h7ZDfyvfwVfXrfz4gUXCMKEPpRHOgav4hCpP_o3Iio2VtIyhbxxMiVn3y6z0GTo1cfmA9gVhWAunY6IKO5-OWgKds2GZjDJ76UYdA8BNaKj7X9xvmGT98Hoix1igZpzyHsx5I4AeieEIlbXuDP7d0hFPpskR3BSNtYGGQDnVzy59iY1NNt7yPaOXqrPaQ0F-XjLIj7jhXhPWgPCPIT2k4ftvmTHlJbYMjcNFlxZ1Op-VpLe-RmdY2s8hEL5kRiis2jEPo5ck3V2UqHIlwHcD8C1HCI0Mu3DGkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان جنبش نجباء برای تحصن در مقابل فرودگاه نجف
🔹
در ادامه واکنش‌های منفی به تصمیم دولت عراق در توقف پروازها با ایران، رئیس شورای اجرایی جنبش نجباء خواهان برگزاری تحصن گسترده در مقابل فرودگاه بین‌المللی نجف اشرف شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/693529" target="_blank">📅 22:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693528">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzdC4vJs0wYg1IrFW4x02j3XAok3nYufkJ8TEnznxDbo-KnhEgrY8KMZwQVrBvXqGFlr79HwEC3YSvjueBna3Js4kdpftrWCJFj0rR3F4n70DsDQg3VtjatPwrPp4njZIPTfhzoO9L5YE2HpfBd1hQ-4yPJnsKQgElIyfv1Sws-rpvCDCZosy99WFO2WdZ8Lxrz4vupc9vQKE7-zPmcKJij2pmblnwb5Od7Dk1txRy55ckuaTN2CpJhN7xa3tOrFzG2tK-GuIPhlNShBQpVE5CJOV7fJRHc1NvsLreEEUWbrpJatAVxzbYOk0zvO32juypi9XKTziwV2Bv-XXtI8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا می‌دانستید نوعی موز به نام «موز آبی» وجود دارد که پوست آن به رنگ آبی روشن است و طعمی شبیه وانیل دارد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/693528" target="_blank">📅 22:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693527">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 مهم‌ترین مانع شما برای داشتن یک کسب‌وکار خانگی چیست؟</h4>
<ul>
<li>✓ نداشتن ایده</li>
<li>✓ کمبود سرمایه</li>
<li>✓ کمبود مهارت</li>
<li>✓ جذب مشتری و فروش</li>
<li>✓ مشکلات اداری</li>
<li>✓ کمبود وقت</li>
<li>✓ نیازی به این کار نمی‌بینم</li>
<li>✓ کسب‌وکار خانگی دارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/693527" target="_blank">📅 22:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693526">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
معاون اقتصادی وزارت تعاون: کالابرگ مرداد و شهریور کسانی که نیازمند احراز محل سکونت بودند فردا واریز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/693526" target="_blank">📅 22:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693525">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216d7d76b.mp4?token=RlMCKm-N8haXGImezNszpkrjOem8LsajOBEgjyvRRqBTaU5p7E32uFU6DYwqZA17xZYhoWLqT8lNiheVpK2GDKHp2Opso9I-q1P-78NO6nhxSeHQhQEWvMRSh74uEWNRzhqM8Mq9Mz3TLCvAF5li8KEwyaeBxaE7UCv2eBQhtOiDpBlKqiyYsQxdBYkKIrQh789bdyLCwuViN-SNe-aQaE_SEiWk-89I6UxnZJQ3j21OIFFO1jKJUM0cjYJvRnCG4uymtD9LSJUEGBSoP5R_2cbP5QIs7z2qE5YdUTZp44XxihTGxd4adpKuuhqoIfHfcxBiiAXX2fDSM6RX7LGvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216d7d76b.mp4?token=RlMCKm-N8haXGImezNszpkrjOem8LsajOBEgjyvRRqBTaU5p7E32uFU6DYwqZA17xZYhoWLqT8lNiheVpK2GDKHp2Opso9I-q1P-78NO6nhxSeHQhQEWvMRSh74uEWNRzhqM8Mq9Mz3TLCvAF5li8KEwyaeBxaE7UCv2eBQhtOiDpBlKqiyYsQxdBYkKIrQh789bdyLCwuViN-SNe-aQaE_SEiWk-89I6UxnZJQ3j21OIFFO1jKJUM0cjYJvRnCG4uymtD9LSJUEGBSoP5R_2cbP5QIs7z2qE5YdUTZp44XxihTGxd4adpKuuhqoIfHfcxBiiAXX2fDSM6RX7LGvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیل گیتس: هوش مصنوعی به طرز دیوانه‌واری از انسان باهوش‌تر خواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/693525" target="_blank">📅 21:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5686e768.mp4?token=sw0007YW4_SQQBd04TIyL0GVdxASruevYdgRU-90mE_hzQNQSJSe7URNtL9URxO1pR6k07aBaMP4-guMKgNMNHiMtB143c5XfbHtr0D267tKR2b1BKvyGNvJEMNh7QDl2dtExh3oBQbcUcpMvx5E1qW1qa0wZDBGK0wekQUcLZTvKh5DM7PB5OekdLQq3P2Lq11eGu0IQlDPh0PodNeVspBTVMJM4FzrhgLitiTe66Cz6guMVueUIizoFopq-5nJk8Y_CQCc471Xdt6_825M6MO2Md5ous-E0LiLWTT-0huGYkfrKSb8BNbdNNuCUJYb896TUF7WlRXXSW3VAzrWog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5686e768.mp4?token=sw0007YW4_SQQBd04TIyL0GVdxASruevYdgRU-90mE_hzQNQSJSe7URNtL9URxO1pR6k07aBaMP4-guMKgNMNHiMtB143c5XfbHtr0D267tKR2b1BKvyGNvJEMNh7QDl2dtExh3oBQbcUcpMvx5E1qW1qa0wZDBGK0wekQUcLZTvKh5DM7PB5OekdLQq3P2Lq11eGu0IQlDPh0PodNeVspBTVMJM4FzrhgLitiTe66Cz6guMVueUIizoFopq-5nJk8Y_CQCc471Xdt6_825M6MO2Md5ous-E0LiLWTT-0huGYkfrKSb8BNbdNNuCUJYb896TUF7WlRXXSW3VAzrWog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوهای وایرال شده از پارک پردیسان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/693523" target="_blank">📅 21:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693522">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
انتشار تصاویر دیده‌ نشده‌ای از شهید نصرالله در جبهه‌های نبرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/693522" target="_blank">📅 21:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693521">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ede84d092.mp4?token=BPID5mv4mgti896924b9JyETkqQzlayBoygPYQxJgn9czRHPZ6qwf5rwfYkGzmAe0rplEJFLpctse7FO9NgJZR9CC2ILRphqTcpm_7rPWGNM4nh9RDVeT33s0rkimZ5Fpn7j4_trdGoTbeltLNcDskAzp7zxni-KJqzNoMuQ3AB9ggtwBVOUMMIafs5vsXS8GzhqPuO4Jx8-nEKjH_LmgHdv3TLX3Lwol8iYGmoB8W6VE_HY2iyYoMreHcVNY_dwx37LoGLIUx_GzoaKrS12DoYjcWMykirN_89d5rBaEThn9rk-3lYtaUMjeffM96Uen8KQd1Dtm1Q3GqgsOu3fvj-n-LsLC6O04y7yDj8aVHymnCwI7zs5Fnxzzs_Z_cQLUSuMAHo58VVNFQXEYSMqhOeta05oT-JcpMemwleovRElZr_0EWSB_cpEOVEpu-3R5EFZeOE9RYgOhgIebjflT7BnrZ8WFJ_gBVxhUMfmdQanhnmy3MY-pfOGCTqdqQ6tGD1gsJ6Ng-TdOzTiYfRBOGQO-4AFD_-7gKROhPJFfW394DttyZAJXE3mj4LV5eNIr91YiMCE9mmU0gLdjySO_dVDI8H5Ujn_wZ_oyCrJhNIXj2C9jwyqra_WYOOh1OGsz3Q84nzUQaK3-iB1IpCSd5i4uMgiR5LCMY5E4d6r-l8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ede84d092.mp4?token=BPID5mv4mgti896924b9JyETkqQzlayBoygPYQxJgn9czRHPZ6qwf5rwfYkGzmAe0rplEJFLpctse7FO9NgJZR9CC2ILRphqTcpm_7rPWGNM4nh9RDVeT33s0rkimZ5Fpn7j4_trdGoTbeltLNcDskAzp7zxni-KJqzNoMuQ3AB9ggtwBVOUMMIafs5vsXS8GzhqPuO4Jx8-nEKjH_LmgHdv3TLX3Lwol8iYGmoB8W6VE_HY2iyYoMreHcVNY_dwx37LoGLIUx_GzoaKrS12DoYjcWMykirN_89d5rBaEThn9rk-3lYtaUMjeffM96Uen8KQd1Dtm1Q3GqgsOu3fvj-n-LsLC6O04y7yDj8aVHymnCwI7zs5Fnxzzs_Z_cQLUSuMAHo58VVNFQXEYSMqhOeta05oT-JcpMemwleovRElZr_0EWSB_cpEOVEpu-3R5EFZeOE9RYgOhgIebjflT7BnrZ8WFJ_gBVxhUMfmdQanhnmy3MY-pfOGCTqdqQ6tGD1gsJ6Ng-TdOzTiYfRBOGQO-4AFD_-7gKROhPJFfW394DttyZAJXE3mj4LV5eNIr91YiMCE9mmU0gLdjySO_dVDI8H5Ujn_wZ_oyCrJhNIXj2C9jwyqra_WYOOh1OGsz3Q84nzUQaK3-iB1IpCSd5i4uMgiR5LCMY5E4d6r-l8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس: حتی کالابرگ ۱۰ میلیونی هم گرانی‌ها را جبران نمی‌کند/ سیاست پرداخت پول نقد از اساس اشتباه است
حسین صمصامی، نماینده مجلس در گفتگو با
#خبر_فوری
:
🔹
این موضوع منابعی را می‌طلبد که وقتی بخواهیم آن را تامین کنیم، آثار تورمی آن بیشتر از پولی است که بخواهیم به مردم بدهیم؛ این را در سال‌های ۱۳۸۸،۱۳۸۹،۱۴۰۱ و ۱۴۰۴ امتحان کردیم.
🔹
آدم عاقل از یک سوراخ دوبار گزیده نمیشود، اما ده بار گزیده شدیم و باز هم انگشتمان را در همان سوراخ میکنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/693521" target="_blank">📅 21:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693520">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcf3a3452.mp4?token=Ye2aJmvSAHxaVrZhKK-Boqvh_PBEL4MV7ZD3GAKdlPVAGc3MN1QsUHK_U1e_22ShjsCZOCOjBH9hisI1iYidm85miUNRaRjbdX3n2hErGKXAGU6r72_EE6HVkqcrkHYoJ_D7_XYqrMYvzdeDGP62YqiuQtmz4rvjQNzEPicA0g9XT2MeoARponuy1ZZsNan3ri33vn6cscmBk3o4Vufzr2eqXZiifWeF49Th3Tzel9qDd3gI0oPs15Z3bYGKVetwPZGZKxcDYjh6qYB_afYYSP1t-LGaq9JjHtVaFWNiVRG33KCSnDRhnKVWlRAN1FtbPWPR4Fn1w1fju-di98pn1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcf3a3452.mp4?token=Ye2aJmvSAHxaVrZhKK-Boqvh_PBEL4MV7ZD3GAKdlPVAGc3MN1QsUHK_U1e_22ShjsCZOCOjBH9hisI1iYidm85miUNRaRjbdX3n2hErGKXAGU6r72_EE6HVkqcrkHYoJ_D7_XYqrMYvzdeDGP62YqiuQtmz4rvjQNzEPicA0g9XT2MeoARponuy1ZZsNan3ri33vn6cscmBk3o4Vufzr2eqXZiifWeF49Th3Tzel9qDd3gI0oPs15Z3bYGKVetwPZGZKxcDYjh6qYB_afYYSP1t-LGaq9JjHtVaFWNiVRG33KCSnDRhnKVWlRAN1FtbPWPR4Fn1w1fju-di98pn1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری زیبا از ماه کامل امشب  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/693520" target="_blank">📅 21:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693519">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
آناتولی: توافق ۵ رهبر مخالف نتانیاهو برای هماهنگی کارزار انتخاباتی با هدف کنار زدن دولت او
🔹
رهبران این «بلوک تغییر» در خانه یائیر لاپید، رهبر مخالفان، در تل‌آویو دیدار کردند
🔹
این پنج رهبر متعهد شدند بلافاصله پس از انتخابات و پیروزی برای تشکیل دولت آینده با یکدیگر همکاری کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/693519" target="_blank">📅 21:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
روایت تلخ همسر شهید باصر بهرام نژاد (محافظ رهبر شهید انقلاب) از زیارت پیکر مطهر شهید آیت‌الله خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/693518" target="_blank">📅 21:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
پزشکیان: استخاره روز بازگشایی مدارس خیلی خوب آمد   واکنش رئیس‌جمهور به حواشی پیرامون استخاره روز بازگشایی مدارس:
🔹
هنگامی که قرآن را باز کردم آیه «وَأَطِيعُوا اللَّهَ وَرَسُولَهُ وَلَا تَنَازَعُوا فَتَفْشَلُوا وَتَذْهَبَ رِيحُكُمْ  وَاصْبِرُوا  إِنَّ اللَّهَ…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/693517" target="_blank">📅 21:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تنگۀ هرمز نفتکش‌های کهنه را گران‌تر از نو کرد
فایننشال‌تایمز:
🔹
اختلال در تردد نفتکش‌ها از تنگۀ هرمز، کرایۀ حمل نفت را به روزانه ۱.۲ میلیون دلار رسانده و قیمت نفتکش‌های دست‌دوم را از نو بیشتر کرده است.
🔹
نفتکش‌های قدیمی هفته گذشته بیش از ۱۵۰ میلیون دلار معامله شدند؛ درحالی‌که قیمت نفتکش نو حدود ۱۳۵ میلیون دلار است.
🔹
دلیل: زمان‌بر بودن ساخت کشتی جدید و تمایل مالکان به نگه‌داشتن نفتکش‌ها برای کسب کرایۀ بیشتر.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/693516" target="_blank">📅 21:14 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
