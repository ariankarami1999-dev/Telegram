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
<img src="https://cdn4.telesco.pe/file/OFccW3G-snRbKETu5yKM5h5vMcBMJddttnggzN0iDkRZWXkia1e8M9ryjSiKtyiPPL0wpBDuvfNX7aZisTjebp7_Wr8i8UFlU4HOmDF3rIeO2qc9MGnGATebPiaXpEUp7nxKxY1vXmeM3x5O9Tg6cWEg_QhDSvAKxPc56XMCJEh0aE-t8ovrcAfzssHZZa8JiElx5Xcc0jmadslMS7ylePVrKmrk1z1DcAG6H009cAPCaVZHUX11Qyk015Tzw-JDnMfeevsU637mvI0MY-t00L23LGOxuA2IV5Yq1QfHbdqvxA_wl5MG0pdwGaRIMTRyxEkSER7EJb5-XXskRHeFbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 18:13:32</div>
<hr>

<div class="tg-post" id="msg-678691">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
لغو تحریم ۳ شرکت هواپیمایی مرتبط با ایران از سوی وزارت خزانه داری دولت تروریستی آمریکا  سی‌جی‌تی‌ان:
🔹
طبق جزئیاتی که روز چهارشنبه در وبگاه وزارت خزانه‌داری دولت تروریستی آمریکا منتشر شده است، تحریم‌های اعمال شده بر ۲ فروند هواپیما و ۳ شرکت هواپیمایی مرتبط…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/akhbarefori/678691" target="_blank">📅 18:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678690">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/041ad29cb9.mp4?token=ElWN2RPPQjXYGtJ2d1j6pNKxembh-4POQWiffJ61vXz0ZqKH4OXQrk2BRomdsmM0BUxetsir1ChbOHAIJSn8TAXtXb7VTBz7WEu5Kyb6HI-1noikfudtTGp2ZPvfTKxRi8i--B3vSHhOGritOexY1YTNbfkfu0Al_POyx0KYdxLFEpYsUrPgJlTDKvV2oEUvz3IeNOZSI-ePAVQpRv2DmmXkLtbXqHXJUGTtm8oP0PJfjJ9hf8EXcQZScG4PUqrgDXCN5Wug-vgSAaXABIhOq_XYcC9aU4zhwp6AC_BtYGL0Z2TZ2TDv3of5LoASvqMKTZLsGrtBADCDLO0VDSWcLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/041ad29cb9.mp4?token=ElWN2RPPQjXYGtJ2d1j6pNKxembh-4POQWiffJ61vXz0ZqKH4OXQrk2BRomdsmM0BUxetsir1ChbOHAIJSn8TAXtXb7VTBz7WEu5Kyb6HI-1noikfudtTGp2ZPvfTKxRi8i--B3vSHhOGritOexY1YTNbfkfu0Al_POyx0KYdxLFEpYsUrPgJlTDKvV2oEUvz3IeNOZSI-ePAVQpRv2DmmXkLtbXqHXJUGTtm8oP0PJfjJ9hf8EXcQZScG4PUqrgDXCN5Wug-vgSAaXABIhOq_XYcC9aU4zhwp6AC_BtYGL0Z2TZ2TDv3of5LoASvqMKTZLsGrtBADCDLO0VDSWcLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: حرف من را از "خودِ من" بشنوید/ گزیده بیانات رهبر شهید انقلاب ۱۳۹۴/۰۴/۲۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/678690" target="_blank">📅 17:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678689">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای رویترز: وزارت خزانه‌داری آمریکا اعلام کرد برخی تحریم‌های مرتبط با ایران را لغو می‌کند./ تسنیم
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/678689" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678688">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای رویترز: وزارت خزانه‌داری آمریکا اعلام کرد برخی تحریم‌های مرتبط با ایران را لغو می‌کند
./ تسنیم
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/678688" target="_blank">📅 17:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678687">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامـیـن‌الـلّـه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883ac1089e.mp4?token=qz_ssD3Kvd3-4V7fwQ-ImyPpz6hoi-yCprmlT9MVYQb_Xv1Svy7MuAvzSRe1325TwsA9xen17n4UNduRt72HOPlsjEorOcWUjASypJszivOo9NKDpSOv8Src80KoExF8RT3a1O25J26MY2XdEQExM_qt-SWiFHBHT3_Xiri7UdffyvnDPQn_K0ez6uPt_9K0UgTfx4mFA7NQPbdwQ5FZZ_hf0c316wPaBu_9bgc3N8r8ybRPsgOYh2UmO5PhWGzk-0bQZ0H6VlW8hSudaxthSkGXBOw_wUNqoefGBxePAIZajJw2K1za5pzf4xc2GRTPWt2XkXR4SYFPgZ7sXZP2HKJAj6zdjgtZA__m7DoAtRtmel2TJnYR4AyKlzr9JBdhUkyKRg8vsC8kDU5pN2ZpznVJktBNRQpj9n3X_vAXFBWQUBUu3xj3OHw2_eawWvudzCD3q-ic0Fhf-Q35ryt3ljL--dOzbYjEmUCoQfkZpJki22ulT1SHclH_WVvq3GkGHzu6qceF8H1WvMSTElj1_KywsE3HNJ4ln6t9ZK6pGRtfdsdC_6pqk5Uw6_6UhekKWM4rgnGAMgz_PJt5ZKHcfspL-q_zcmC0PH77brDPBBUTr58SS3ym0d78bjgJmAC3kQyjT7lfJyxB5M2LgNRGDFPAelkktu83uPJ-8oWmCHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883ac1089e.mp4?token=qz_ssD3Kvd3-4V7fwQ-ImyPpz6hoi-yCprmlT9MVYQb_Xv1Svy7MuAvzSRe1325TwsA9xen17n4UNduRt72HOPlsjEorOcWUjASypJszivOo9NKDpSOv8Src80KoExF8RT3a1O25J26MY2XdEQExM_qt-SWiFHBHT3_Xiri7UdffyvnDPQn_K0ez6uPt_9K0UgTfx4mFA7NQPbdwQ5FZZ_hf0c316wPaBu_9bgc3N8r8ybRPsgOYh2UmO5PhWGzk-0bQZ0H6VlW8hSudaxthSkGXBOw_wUNqoefGBxePAIZajJw2K1za5pzf4xc2GRTPWt2XkXR4SYFPgZ7sXZP2HKJAj6zdjgtZA__m7DoAtRtmel2TJnYR4AyKlzr9JBdhUkyKRg8vsC8kDU5pN2ZpznVJktBNRQpj9n3X_vAXFBWQUBUu3xj3OHw2_eawWvudzCD3q-ic0Fhf-Q35ryt3ljL--dOzbYjEmUCoQfkZpJki22ulT1SHclH_WVvq3GkGHzu6qceF8H1WvMSTElj1_KywsE3HNJ4ln6t9ZK6pGRtfdsdC_6pqk5Uw6_6UhekKWM4rgnGAMgz_PJt5ZKHcfspL-q_zcmC0PH77brDPBBUTr58SS3ym0d78bjgJmAC3kQyjT7lfJyxB5M2LgNRGDFPAelkktu83uPJ-8oWmCHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛
تمام عالم رو هم بگردید، باز هیچ‌جای دنیا عفت و حیا و ادب زن شیعه‌ی ایرانی رو پیدا نمی‌کنید..
زر و زیور دنیا ارزانی کسانی که هنری جز نمایش تن و خریدن توجه ندارند..</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/678687" target="_blank">📅 17:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678686">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
یک منبع ارشد ایرانی و دو مقام منطقه‌ای به رویترز: توافق پیشنهادی با عمان به ایران اجازه می‌دهد بر کشتی‌های ورودی به خلیج فارس از تنگه هرمز کنترل داشته باشد. این مسئله یکی از بزرگ‌ترین امتیازهای اعطا شده به ایران توصیف شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/678686" target="_blank">📅 17:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678685">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo0N1r8uXVQCl5QzhdMp9oqo_-1kBTp26G8PzmLyV3OW_nOTiBNq4u73v_a3gGN6l5LELeGQjkSBOVZcpNnA_3Ml4IfaDLeuUQDyY3Il6BGmToYZJ-qHjjqHMAfe2mT9yXSn7fPwEmMn5o4GX1V6RPJ0BEJE1u9gyoOZjltLXxo-t19g3bgi5pYeH8Bpsc68C3RiYwD837o7pCla0zQoavjAwNilqYakcZ31bXsXWCt7iNOrqk03SquRETf4LD_usUQWTMqFLxuvjoqN_TJEgKhAZ0snnZSkeK10_If3PDtOSNUZg0kcfSVGhUNwdDHc1EXR8w5wsvI7SD1fobJcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط در بلوف و عقب‌نشینی | چرا تهران دیگر تهدیدهای واشنگتن را جدی نمی‌گیرد؟
🔹
هفته گذشته راهروهای قدرت در واشنگتن بار دیگر صحنه گمانه‌زنی‌های داغ درباره احتمال وقوع یک برخورد نظامی گسترده میان ایالات متحده و جمهوری اسلامی ایران بود. اما حالا همه‌چیز بوی یک توافق تاره را می‌دهد. کاخ سفید دچار یک سرگیجه سیاسی است که صدای همه را درآورده است.
ترجمه گزارش آمریکن کانسرتیو را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235490</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/678685" target="_blank">📅 17:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678684">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7471eda44.mp4?token=DVIUWVlJ4ZnMm8oJ2O_AxA3h-pVx0_w4DOHAHaVI3J2Wb9jrFhvszfqiU1q93HiKKidszoIvGeFoYcb5Fuv2xmSA-1qkoaKF9t_wloIGj0i0usB2wE3TUkL2FvsmjpCNbgmc2iHRI7Wa7NT3W1Xob74ISXkrwOdUAkiOfreYO_D16XhBCajKbXVvm1efdzN2gBOhsH6eliP_tbwoBJs_iUDwVpxUKvcsNtE3Aoi7MjAO5IQGQwN_CoM0aE-bnecOt14xnhEKpiYuEu_veWbd6d5DGabRiuu7uCAHUrPBDuHQtTg9SofHovSkNPy06RTHFPWLZCXqv4fCHnKUiWChIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7471eda44.mp4?token=DVIUWVlJ4ZnMm8oJ2O_AxA3h-pVx0_w4DOHAHaVI3J2Wb9jrFhvszfqiU1q93HiKKidszoIvGeFoYcb5Fuv2xmSA-1qkoaKF9t_wloIGj0i0usB2wE3TUkL2FvsmjpCNbgmc2iHRI7Wa7NT3W1Xob74ISXkrwOdUAkiOfreYO_D16XhBCajKbXVvm1efdzN2gBOhsH6eliP_tbwoBJs_iUDwVpxUKvcsNtE3Aoi7MjAO5IQGQwN_CoM0aE-bnecOt14xnhEKpiYuEu_veWbd6d5DGabRiuu7uCAHUrPBDuHQtTg9SofHovSkNPy06RTHFPWLZCXqv4fCHnKUiWChIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعریف خنده‌دار کاخ سفید از جنگ
سناتور آمریکایی:
🔹
ما جنگ راه می‌اندازیم و اسمش را می‌گذاریم عملیات غیرجنگی!
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/678684" target="_blank">📅 17:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678683">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b19afaf3d.mp4?token=hgGzQsxuMnV-Co1RjEcp0lEfc1WCyYfdijc5MloCcV4DpRb5sk35Rkk_w57xbvmfCr523R536Jck9XGYdcyYUIPP5q4xn0VrSzHlkrlnWwBO38TJYP4BOAlgV5zEGvpmYtx72EqpykRMwQomKYlYRyVUA4M0MyM4Ww4fRbact6P5L13u4dePg_9pI7YVbRNUXPtM3QSeoSign5CWH2eMm_XQDCv8LBVDWeNL0DCoxFwZ3BU6dhGPB4H5aY6WBmMd84h-8xRgItf_7yQ-JXDkLuqxx7IEOWeYfzaIlD44sgia8rQhqotg90e8oclgU9FQGFsLfYOlGRKXAKYT7AUEIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b19afaf3d.mp4?token=hgGzQsxuMnV-Co1RjEcp0lEfc1WCyYfdijc5MloCcV4DpRb5sk35Rkk_w57xbvmfCr523R536Jck9XGYdcyYUIPP5q4xn0VrSzHlkrlnWwBO38TJYP4BOAlgV5zEGvpmYtx72EqpykRMwQomKYlYRyVUA4M0MyM4Ww4fRbact6P5L13u4dePg_9pI7YVbRNUXPtM3QSeoSign5CWH2eMm_XQDCv8LBVDWeNL0DCoxFwZ3BU6dhGPB4H5aY6WBmMd84h-8xRgItf_7yQ-JXDkLuqxx7IEOWeYfzaIlD44sgia8rQhqotg90e8oclgU9FQGFsLfYOlGRKXAKYT7AUEIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاله جای مادره؛ آخه سینا مادر نداره
🔹
سینا ۲ ساله شهید شده، مادرش هم شهید شده؛ پدرش هم شهید شده؛ مادر نداره که در فراقش بی قراری کنه؛ خاله جای مادرش بیتاب فراق سیناست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/678683" target="_blank">📅 17:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678682">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
چاقی بی‌ارادگی نیست؛ مغز وزن بالاتر را «طبیعی» می‌داند
پژوهشگران دانمارکی:
🔹
کاهش وزن فقط به اراده ربط ندارد.
🔹
مغز وزن بالاتر را به‌خاطر می‌سپارد و از آن دفاع می‌کند، به‌همین‌دلیل بسیاری پس از رژیم دوباره چاق می‌شوند.
🔹
خواب، تحرک و تغذیه متعادل مؤثرتر از رژیم‌های سخت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/678682" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678681">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSMer2oqSORRrSAO_f24Lfqcuj7vfeSVVvBA4kkcEomEAbexaCQcUKj1g2rDv-V698j5xcfHgVwwDRixtNlvWQaCdK3dgiB0IshlghUs8ujaluBEfAE_m1hok85PeNnjsHQGyi9ObQWhDV0QgcwY38gfRk3ta49YLYtu4UEcZ73_E-u8kgrjc6nUBDFT4xTmZLiN7zoXn4QKOGsyTLns5E7Le5fQqnuZ9Ae3AbMIbeUnar58J7xKrlTdHKLNF-MS04qG8-xBaFUGsbd17H33q_I_kgNlJkgU-oEeC3ikfKElvNEfiEbgShSw3VijiRqgu_Ajpk9iQn4vTmLxV6_mJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشورهایی که بازار جهانی تجارت الکترونیک را در دست دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/678681" target="_blank">📅 16:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678680">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
یک مقام ارشد کشورهای حاشیه خلیج فارس به سی‌ان‌ان: احتمال دستیابی آمریکا و ایران به توافق تا روز جمعه «۵۰-۵۰» است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/678680" target="_blank">📅 16:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678679">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG56t4drpXwpZmyU7WKIQg4If5J76guYATB3qP7Jn7tVK028LYAX8B1W6xGodkko8pZSuOpThBSJ1eJtDiTjpMEPV5iiklv_1PG_d-HHBraLTR259SRmsZD0-g3xBSps_bZca590uAZl60vtuJmq-ofcs5m9EurosFah7nRqC8hZvouOyLW2NOAv5sV1XPA8luRnGjmL4f0xphw9GHjZ9JHgshLdmk-jq09brxMYkLw_QctvQcoOw6iqswKedoapxniHKV8JsFb-85eaYNM0quXWDvUCcsOXlw_-yBWAkKgrNfsjsgNzlDPI1I5gqFhLbKT5eJt9nPrPKBzwT255rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در غنا در واکنشی طعنه‌آمیز به بن‌بست راهبردی آمریکا:
تنها یک نتیجه رضایت‌بخش برای آمریکا باقی مانده است:
تسلیم کامل!!!
اما ترامپ متکبرتر از آن است که آن را بپذیرد، و درمانده‌تر از آن که راه فراری داشته باشد. «هنر معامله».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/678679" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678678">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHQ0Epig34VVC4rvTp4aMP4JmtekKaOn-UrkF5jWBXEBVPBIP3cZqzC1KWNnDws89ylVjgpSgrotryyGPVqhYM9PlY6i15GXKveSjDBLh4ruM0S0nz3u5HzKsuzmAMigxaLV9We3RJu16-TakELdnIg7v40654FwlZ0ubfI4rZoeA3BxT3kWnYUj-0yKD5KbMG1ySHyp5X1aS_kzpasclgJ0WgYSCNZQ6pYjFSHkb4B7L6KZjTX9KRjlbKvgeqBvmRIxpcLr-2gRriFQcFMjr2boSlBe6NyvCX86SxYh-Gh7x27hXHYvCbpk04f6CtC6od1rORxxbi9DR5ho67hHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای حرکت مرموز چند ده هواپیمای آمریکایی اطراف ایران/ یک خبر اشتباه یا پیش‌قراول جنگ بزرگ؟
🔹
دو اشتباه در تحلیل‌هایی که در رابطه با تعداد سوخت‌رسان‌ها و جنگنده‌ها و هواپیماهای ترابری آمریکا در خاورمیانه ارائه می شود، وجود دارد. یکی از این تحلیل‌های اشتباه مربوط به هواپیماهای ترانزیتی و حمل و نقل یا سوخت‌رسان است و دیگری به هواپیماهای جنگنده آمریکایی ارتباط پیدا می‌کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3235051</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/678678" target="_blank">📅 16:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678677">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
مقام پاکستانی به ریانووستی: عراقچی روز جمعه به پاکستان سفر می‌کند
🔹
وی قرار است با عاصم منیر، فرمانده ارتش پاکستان، شهباز شریف، نخست‌وزیر و اسحاق دار، معاون وزیر امور خارجه دیدار داشته باشد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/678677" target="_blank">📅 16:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678676">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرودگاه ‌شهدای ساری از فردا تعطیل می‌شود
🔹
رژیم صهیونیستی ساکنان شهرک المنصوری در جنوب لبنان را تهدید به تخلیه کرد.
🔹
عرشیا به‌نژاد با ۳۲۴ پاس موفق، پنجمین پاسور برتر لیگ ملت‌های والیبال ۲۰۲۶ شد.
🔹
امید عالیشاه با گل گهر به توافق رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/678676" target="_blank">📅 16:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678675">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
قیمت دام زنده ۳۰درصد کاهش یافت، اما گوشت گران ماند
مدیرعامل اتحادیه دام سبک:
🔹
هر کیلو دام زنده در تهران از ۷۳۰ به ۶۴۰ هزار تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/678675" target="_blank">📅 16:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678674">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGY7IPwwWA2d89sOIWGM6J18IKb3UTImg3pFzJnAwvFxeyWCvmF6AJe9VnAoPpu5p6AJaa1RsF2E1VFb2U-GVNp2So_aU3a9Hy_Asu4GQirAKgKajB48W4GF3Xnu0araJLxtgh_3k3EYm3aEAz7aDzoLlAMZZqr7tqQy7EkCOD6I8X6la4939oGMKmBHbT65qmpDEV98d9PcKEQd4FfjASyUa1_t3fgRPJzIwessxwwcf-re-acJWhAl0pVvIlF4GovzW8-IcpQXa_th5A2PnoaEfwR8yU4mdfEcSDRuuHimrCiJxMqCWy4xeQtofLVGMXUzjnlMzQbcc6s78G35Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آپدیت واتساپ با ویژگی‌های جدید منتشر شد
🔹
واتساپ در آپدیت جدید برای چت‌های گروهی چندین قابلیت کاربردی ایجاد کرده است.
🔹
مهم‌ترین تغییر، قابلیت منشن تمام اعضای گروه با @all است.
🔹
ابزار نظرسنجی بهبود یافته و ایجاد گروه‌های فرعی از روی گروه اصلی آسان‌تر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/678674" target="_blank">📅 16:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GeLajSzhJp4G2hqiJfL_63S7AM_IEjV2abVlDrBwVEI4jNNGoIwvM8e9uKvjPLZ3gsU2ZZUtiTuzQFWxs5vGEZock8mgtjxCwoxvtFRUIJEsVhdqD1GyWXY2uFQ2aizgK6Mh8g4ODxb9YShiEpHODKrvc8k_ykR2Ds0J0ul_eC30D_HqekvlRJQ8zimeBXkxMs1n67KIF5sA_vkNPUbAh44-W29j80dkwoAwaVnDtTgCPsesFjjhEvED9lE5PiVrFzKMnaClWYF-_ZffpX90GzRGIUuGoxQiaj707d0M6NxbaM_1ngzl6roeqzx6TJMmH53eJGA-x_kY_tl0ZHh9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaGlYzrgY0Y510Yp3_g1H33wLMLjx1Ko3-CY7z3p75_lXnM5bTPTRqh1Lblb1hFiwzQdJFX9h7NHBUHpdaqYbHKA0_8cBeE2h6TngTw09GTZ2CRkWsnYizyzhdz70k2aWMRpHDA6TkGfTgPavxpJJ9AJ8FWGLVND14bpodOW1RK5NSdujXeYxAvFB3nIKsGCyQ4jSzrteh2mOOpvm8LYqjfu2oA5GT_VLNMqsMgwx2JVYI6ruEtwVXJZ0RNivNkOB2ea6JryklHzAMxkzXwrre0oTyknp8foU31DzcfPWkzUTbQr0BCUIkKWIDQ-7pJNvys-QkfCLf0VrwAHrKVd4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جواب آزمایش‌تون رو خودتون تفسیر کنید؛ هر عدد چه معنایی داره
؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/678672" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c5cbe00c.mp4?token=Sf_QzvN46Ol4WLvhVh9AqDKj1nfYe6rZdaQAIUbGdeiWBohFSBw0pCbnOTi_Z-IC9emRFrTEGotOkWg4N-oqQqKGmxjG1t5Moz0OtPbkMcuJzU9epDmYHWxxeedS1Ky37SyRi5Q0OlzLNe9r3i2GyqLHMQ8tbCEV_Hqi_fYxsiooIeBGJDyhlZHZ78MCONxyeR1KTWcliClPUAXp2geSF4BRhzbOAEXUGUKtRTwd-nUoPwl2vrcsnrZGUxkewwG3mm3SsQDQuBvregZCQB4jXQeiYyLOLEsSzz4UjxTZamQv-OHp8M54z9XRzut-sPL3yi6t-Ngy3g6tWCC2Ayhn2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c5cbe00c.mp4?token=Sf_QzvN46Ol4WLvhVh9AqDKj1nfYe6rZdaQAIUbGdeiWBohFSBw0pCbnOTi_Z-IC9emRFrTEGotOkWg4N-oqQqKGmxjG1t5Moz0OtPbkMcuJzU9epDmYHWxxeedS1Ky37SyRi5Q0OlzLNe9r3i2GyqLHMQ8tbCEV_Hqi_fYxsiooIeBGJDyhlZHZ78MCONxyeR1KTWcliClPUAXp2geSF4BRhzbOAEXUGUKtRTwd-nUoPwl2vrcsnrZGUxkewwG3mm3SsQDQuBvregZCQB4jXQeiYyLOLEsSzz4UjxTZamQv-OHp8M54z9XRzut-sPL3yi6t-Ngy3g6tWCC2Ayhn2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شش ماه جنگ، ۱۰۰ میلیارد دلار خسارت و نبرد برای باز نگه داشتن تنگه‌ای که باز بود!
🔹
سیاستمدار آمریکایی؛ حمله به ایران به نامحبوب‌ترین عملیات نظامی بزرگ آمریکا تبدیل شده است!.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/678671" target="_blank">📅 16:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcbc4d7bd.mp4?token=F5yOZdtjRWUfy_uEMEFGR0M5xLxGJSzJhEfU5UwSdxWmpm2XTeW3aSogSm_0sadofiF-Xp4hcYQ8QBj2VLX8kF6MpHlNOtX2ASm0RI88PDhg7-MFQxcd-uNg2dqGivsXx5AQe0E0JDTgNesLS7AsYM2CsNPU5kDRvo5xbehbfHsK0XOhLaNfqqw4M2nNqr5EahIrRW8dHwukFoJLB0mtvegtRP7Hckl7w1LvISGhDMuaR8VIOQpg-_SDf9RL-38bcOJhAYz1kGkel3xJdS4ztS2oHjR2b_t-j3ivOYngbsvXsUyeizALqeqrXYwlvkx2K8xRdfi-rVriVOiqvDdnSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcbc4d7bd.mp4?token=F5yOZdtjRWUfy_uEMEFGR0M5xLxGJSzJhEfU5UwSdxWmpm2XTeW3aSogSm_0sadofiF-Xp4hcYQ8QBj2VLX8kF6MpHlNOtX2ASm0RI88PDhg7-MFQxcd-uNg2dqGivsXx5AQe0E0JDTgNesLS7AsYM2CsNPU5kDRvo5xbehbfHsK0XOhLaNfqqw4M2nNqr5EahIrRW8dHwukFoJLB0mtvegtRP7Hckl7w1LvISGhDMuaR8VIOQpg-_SDf9RL-38bcOJhAYz1kGkel3xJdS4ztS2oHjR2b_t-j3ivOYngbsvXsUyeizALqeqrXYwlvkx2K8xRdfi-rVriVOiqvDdnSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیت‌کوین یا طلا؟ کدوم برای سرمایه‌گذاری بهتره؟
🤔
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/678670" target="_blank">📅 16:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآدم</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVUJgF2SKwq1KO3Ft7PMXaNQn2wuuKfTSSplRysRGtiHQxrK165t6KvXkxGwa2vnppTavZpIsLnUHWbFrtFv8lVfHxNgGzyuytzPIRZRT7l2eP0FAnBcQmxpq_z-_7htSH8HLPThZw7_ypJWMnjAWf4UF4XoypEaKAI7tcEPkbT8XdL6FgCOnK1FKXe3402n1j6td0J_MbU0f3UNwmb2nl1gtffECxGbbe5lxXW4IzmGI7dHfYFTGj9B7bdmIfEw9gIkSCF8aeYEy5LKiV85eJ72iQxrBHuc6jEXen0IEbzdXZ5Wk1oEkYOWnyXktd05NzBov5heYspi0HGnX29C5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود:
۳۰ درصد نفت جهان؛
۳۰ درصد کود شیمیایی جهان؛
۲۰ درصد گاز طبیعی جهان؛
۲۰ درصد محصولات پتروشیمی غیرپلیمری جهان؛
۱۵ درصد پلیمرهای بازار جهانی؛
۱۰ درصد سنگ بوکسیت و آلومینا جهانی
۱۰ درصد سیمان و کلینکر جهان
۱۰ درصد آلمینیوم جهان
۶ درصد غلات بازار جهان
۵ درصد سنگ‌آهن و مواد اولیه فولاد
و ۴ درصد محصولات کشاورزی جهان
همگی از تنگه هرمز رد میشن!
نعمتی که خداوند از هزاران سال پیش به ایران داده بود بدست قدرتمند نیروهای نظامی جمهوری اسلامی نقد شده و رهبر جامعه صراحتاً امر به مدیریتش کرده!
از دستش ندید!
@AliEbnehava</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/678669" target="_blank">📅 16:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678666">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0W8YR787SzzoLiclIMt9fyCTTCYKej4HGDertzKi4jSMTthczGEmKC2iOOJ7heU7mfDpXp_mkFvQvkRYfDcquXdMxQmXfrf5bkfI6ceCtFjyvZhSfj_9QQ3jFO3xyXYJARZnhD17XkvMioNrWe6G-mumM5O3cY4mMGimz5imCWnht9TBDLKbiMsHa0BAdnAO5_D4U7InoDXjJdw-sUVt-IeXCQNDM7AfXHWvUBD-KNhJwMohH5SWEjusK6S0qq31Gg2biDI_w-ZqSgE9xdhXpzWjnxy_TKHLIGqvZkoKN-BqypE5oI14q_d3p_66lyHKIpMYdDu-dm53mTwfq8KZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dec1751cc4.mp4?token=dzOYuRgWDExsXZOsEIDkST53BIY1xv5vNry_j6y_zAwFGehRFGf0JB58OEn54r8I6QOmbUoF2gja8gg20M6NOTqZT_I0ILqQBAqxyHRPfKkHsgPfca5hWdCp05oEwVm2-sNlsRAPJysWx_FsbBpex6p3fW2kYq_M5vsr0gaC14CmnqnXjLh-mm8BO1W-EjCG4W9tWBNl0kFvpB9oDjyiUaaL7PtkC2BVrGmecrAvNLKULI8fLxPdsSnr3Xvxt5rc3g7TN3RAQmpFqtZzCgL7pWeyg4vSbreTgjRMAFtSIoC2RVf70jsmgHmGm1w4T6OKzRcPjSPqG2ewkW6GSHTGUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dec1751cc4.mp4?token=dzOYuRgWDExsXZOsEIDkST53BIY1xv5vNry_j6y_zAwFGehRFGf0JB58OEn54r8I6QOmbUoF2gja8gg20M6NOTqZT_I0ILqQBAqxyHRPfKkHsgPfca5hWdCp05oEwVm2-sNlsRAPJysWx_FsbBpex6p3fW2kYq_M5vsr0gaC14CmnqnXjLh-mm8BO1W-EjCG4W9tWBNl0kFvpB9oDjyiUaaL7PtkC2BVrGmecrAvNLKULI8fLxPdsSnr3Xvxt5rc3g7TN3RAQmpFqtZzCgL7pWeyg4vSbreTgjRMAFtSIoC2RVf70jsmgHmGm1w4T6OKzRcPjSPqG2ewkW6GSHTGUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی عجیبی که حمید رسایی با موضوع مذاکرات در کانال خود منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/678666" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678665">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAJjo2j3GRs-xuyOKWp26VapmNXcZ5MZdqhpn_KQVF8XYmYO8clMvjNckpxrV2EIQkgKmFYOkYmzIFFTIvuezYqtDE0ShfaipIHD6NBxLADQOoFNS9ME9k2Z0ucjCThDdKW4p2PSnuflyTlvFWy8BKCL_xuXWgIXrlR4MX9yXZAOYNMQaSe4coetLT7BL3448fUMbiDdafReFQbfU1IvgYNXCxFchgTLyO7sQE4JKU4kWrVHPFYJda6ji8jantVBOlfAI5aZXtb4LYsFs24CeG7-iVo4BzAVds02JcBiBDjWoHjiK-V9SY1LWADfhrh1ilYy18aoGdkdC2CNXFrQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جهانی اونس طلا در ساعات اخیر بیش از ۱۵۰ دلار افزایش یافت و به ۴۲۰۰ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/678665" target="_blank">📅 16:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678664">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II4d2BFUqXZ8Ee6jv1Q4jKjxbry86S7nHe8i5pWgHoRoHGfgab6g_HD0wwD2wtJO3_Vp4EJVYxiUbrcOqpIXHv6MXv5UD27GAdwl2Pxo9qvg6IQ0VV4H4JXMpAKn8fYGpNV7mzR3aQhd2r3x3NTVK8NzoG4NJfY7j7ew4UQtWx3ktTyFfj0wgFECsSRfyQm_9-7_kKtjwhF79WtSk13dWGWU0pEKwrHdB0X3N8TcFPzXfVm2QG-nFwLkCk2tIx95UCudKGRqC2zdHArW-U9u49dSr9lG3SYTjUSbL6L7whsqAXqZCyIRGq7_Cjk4-5edEpREiWm1eHozH-b4dBQ0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶
خوراکی معجزه‌گر برای سلامت قلب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/678664" target="_blank">📅 15:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678663">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
خبرنگار المیادین در تهران: چشم‌انداز نسبتاً مثبت و خوش‌بینانه‌ای در ایران درباره پرونده تنگه هرمز وجود دارد
🔹
اگر مداخلات آمریکایی متوقف شود، عمان و ایران می‌توانند در مورد تنگه هرمز به توافق برسند. / انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/678663" target="_blank">📅 15:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678662">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اطلاعیه وزارت آموزش و پرورش درباره برگزاری امتحانات نهایی معوق در ۴ استان جنوبی کشور  ستاد عالی آزمون‌های وزارت آموزش و پرورش:
🔹
به غایبین موجه امتحانات در دو درس تخصصی پایه دوازدهم هر رشته تحصیلی در مرحله کشوری اجازه داده می شود در امتحاناتی که مطابق برنامه…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/678662" target="_blank">📅 15:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678661">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d45e52ba.mp4?token=Br6RPqoxyvrZbfk99ih4THL0_pZJ-Ztl3zkOPOOrb3kzd6rMtLlsmSmYHPB088ohabEn2h0-spbwYfQJDHJzxOqVNBHjAUegL9JwUwaLWIHwqp1zfgLyl5uriJPFo9TLLoTHU2LX32HMr178cmwM-SvNfDpSluNZOSxEhGAb-vttBQAsjV7wOCX7sgMZVoU353O2MxgD7CLq4SJIbenJUOJjav3XFWXCxJl7KkoaDzRDdWk_IfOUSDI7zGUBWoch5pLbwBCBtHjft1y7GEDJk_9uLXgSqV5Fap2MfVLAVyaqjxe5lBA0R4LBBdyq0JtN_ShEfJg7nHaEKnlw5ZN5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d45e52ba.mp4?token=Br6RPqoxyvrZbfk99ih4THL0_pZJ-Ztl3zkOPOOrb3kzd6rMtLlsmSmYHPB088ohabEn2h0-spbwYfQJDHJzxOqVNBHjAUegL9JwUwaLWIHwqp1zfgLyl5uriJPFo9TLLoTHU2LX32HMr178cmwM-SvNfDpSluNZOSxEhGAb-vttBQAsjV7wOCX7sgMZVoU353O2MxgD7CLq4SJIbenJUOJjav3XFWXCxJl7KkoaDzRDdWk_IfOUSDI7zGUBWoch5pLbwBCBtHjft1y7GEDJk_9uLXgSqV5Fap2MfVLAVyaqjxe5lBA0R4LBBdyq0JtN_ShEfJg7nHaEKnlw5ZN5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ یک فوتبالیست تایلندی پس از برخورد صاعقه در حین مسابقه
پلیس:
🔹
سوفوان آوای ۲۴ ساله روز گذشته (سه‌شنبه) پس از اصابت صاعقه به زمین ورزشگاه «سانتی‌فاپ» واقع در جنوب تایلند، دچار جراحات وخیمی شد.
🔹
۱۲ بازیکن دیگر نیز دچار مصدومیت و به بیمارستان منتقل شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678661" target="_blank">📅 15:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678660">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW5sIMusCv1bd4f7FITFsOzFkIuFntWuDZXWX7LQTst28IwFa49R_v3EkO358VAm-hIIqLDEUOOe9djgxXg4fBOZ8PV62HNw6BO5Xb9V0vLsAQrkDkRK_IRSE5HC-fyR_wl1GNUk9V3kM7mJoYlcg1ENqLK9g8wkbtALsRRPDg2dDlyHjnIbF7sfXrcl9Esn27MnXSC7zlkuPlbo8UZTKiBnUCSecZyPuhRMyzXq5lNkt5BH1PkVtI9un11_qvf2SafOuHPAV4fGmKDSttzQkaTZ8IM9iuLjJjmzSsP3QQZHp15Lo0imZMALIwpEEF8TUgwGcl6xLhyluvKjiocnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشتگ
#پرچم_سرخ
در شبکه‌های اجتماعی ترند شد
🔹
همزمان با راهپیمایی اربعین، هشتگ
#پرچم_سرخ
در شبکه‌های اجتماعی ترند شد و تصاویر گسترده‌ای از پرچم‌های سرخ برافراشته‌شده در مسیر پیاده‌روی اربعین دست‌به‌دست شد؛ پرچم‌هایی که از سوی کاربران نماد خون‌خواهی، انتقام و ایستادگی در برابر ظلم توصیف شدند.
🔹
کاربران با انتشار این تصاویر، بر مفاهیمی همچون خون‌خواهی، انتقام، بیعت با آرمان‌های عاشورا، وحدت جهان اسلام و ادامه مسیر مقاومت تأکید کردند و
#پرچم_سرخ
را به یکی از داغ‌ترین هشتگ‌های کاربران ایرانی در شبکه‌های اجتماعی تبدیل کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/678660" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehNg8YJ7p8qEaH49OQcPGZwMMW2QuGCNmk5aiXGgLnbSR009FxXvebanL-3jZJPjSwk3s--Zv3YcYt4znxDMwqMCplpDstjOLcDmLDkloT4T9AaxT_GlyxjKjLYrxzM0YFcC55DQHiu3z9wiQINriSWPEUlzWlxmrkd_fvoO63_ARQg3ljsP1TtB30zMoypVgu4b59cA90GXi9JvlXYYNBZMwEjOmAsxq9aOscUy263m--OW7Jnz1-byP-zX19HQbs9IJK-D0GnxdPy4UiigqIXM3BN_F9BpqeU6Eh7V67Dz0JA0XV2qVAVZ4QULbeF1utMl1VtDH0JnLghhDdLyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه برای یک کشتی در نزدیکی یمن
سازمان عملیات تجارت دریایی انگلیس:
🔹
یک کشتی در آب‌های نزدیک یمن مورد حمله یک شناور بدون سرنشین قرار گرفت.
🔹
خدمۀ کشتی نجات یافتند اما گزارش شده که کشتی غرق شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/678659" target="_blank">📅 15:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678658">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217a3500a1.mp4?token=Co4MDXXULp8FfUB8897zCxYLqcFRrMaN8oE3LpXYqh78BBs4XGIFe_K0IBqkJazzgJpQfrQ8FxNr62n-YYN7bCuZ5TW95IV4_LK6xexEhXN-EmS55Wlfq-AH5hJf4hjtdnq3fdVZjzlTAy_lwVP01afB6jUbz8y0S09SNXsoxtZnBMzPsT0DSqjljH5n1CITIvnyFlE4VwOvnzRqaUpRoue0cvXRC8k6jOngrapS98h9lG2Qq-bz3pF__lJLSondxD6aqf_NiMIIuahKSAJYIdFAwXyHqB9YQuFY6MTeqSnrof5mme4ZWAT7S0QeoZekccXtvZS_Yv3yhfA1Am10TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217a3500a1.mp4?token=Co4MDXXULp8FfUB8897zCxYLqcFRrMaN8oE3LpXYqh78BBs4XGIFe_K0IBqkJazzgJpQfrQ8FxNr62n-YYN7bCuZ5TW95IV4_LK6xexEhXN-EmS55Wlfq-AH5hJf4hjtdnq3fdVZjzlTAy_lwVP01afB6jUbz8y0S09SNXsoxtZnBMzPsT0DSqjljH5n1CITIvnyFlE4VwOvnzRqaUpRoue0cvXRC8k6jOngrapS98h9lG2Qq-bz3pF__lJLSondxD6aqf_NiMIIuahKSAJYIdFAwXyHqB9YQuFY6MTeqSnrof5mme4ZWAT7S0QeoZekccXtvZS_Yv3yhfA1Am10TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اصابت هواپیمای هندی به زمین؛ سقوط این پرواز چندین مصدوم بر جای گذاشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/678658" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678657">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون برق و انرژی وزارت نیرو: هیچ تغییر قیمتی در قبوض اعمال نشده است.
🔹
پزشکیان: از هر تصمیم رهبران فلسطینی در روند مذاکرات حمایت می‌کنیم
🔹
رئیس ستاد ارتش عربستان و فرمانده نیروی زمینی سنتکام به یکدیگر رایزنی کردند.
🔹
دستیار رئیس جمهور آذربایجان: باکو هرگز اجازه استفاده از خاک خود علیه ایران را نخواهد داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/678657" target="_blank">📅 15:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678656">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
مقام پاکستانی به ریانووستی: عراقچی روز جمعه به پاکستان سفر می‌کند
🔹
وی قرار است با عاصم منیر، فرمانده ارتش پاکستان، شهباز شریف، نخست‌وزیر و اسحاق دار، معاون وزیر امور خارجه دیدار داشته باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/678656" target="_blank">📅 15:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678655">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbvKA-5NPYycyPG-0Zq7etDQv_Y_qdx36aUkTL_BkbhcigxydDWe5_VjeMiugtv81R_wyfL14L6nvb0awaruA2LSa2GU2TYaQmV-kS-qutjpVqzWjH-CLGh_sdIub2OeBKp0IYAuvyNo7Bzf6AbOMAzZAwiTk_uetcxj_wufYuGStKaGut9TjjYNWmmtjY_j-H-pUsRiEiHDCGwMhv_Fslk7--OsPZHoRJL1pWLgMOplKaIqe1vfJxBzcX0CRtoERnb8u8sd8eIj_o0_YjfaoxU72eE3YkcVwfgPZghL4KmTll36m8DDk6r7alZYz92YlEy7_Y2Hr6wT5XSKhvO7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طوفان حاشیه برای همسر بیژن مرتضوی | جنجال یک گفت‌وگو در استانبول | نرگس فرخی کیست؟
🔹
نام نرگس فرخی در روزهای اخیر بیش از هر زمان دیگری در میان کاربران فضای مجازی مطرح شده است؛ نه به دلیل فعالیت‌های هنری یا اجرای تلویزیونی، بلکه به واسطه گفتگویش با مجید واشقانی در استانبول، زنی که پیش از این هم ازدواجش با بیژن مرتضوی خواننده و نوازنده ایرانی نامش را بر سر زبان‌ها انداخته بود.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235690</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/678655" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678654">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0c348b7c.mp4?token=E0T45z0XetPlOJG3XPBlKmMV1aL8XiJtSDRLPj9jXvKuE5FyVC4Qae2yDYqzFP-7EIBjfo8u6mM4v1HvVtHwUtBXwkvxID3v1mWslpI77lCgNkOqp1WRhhXpEs0fyJeBIS54N_PXLLwcVKJYZwjldytod7iq8dA435IvUDjDCuofDdOgS9RHYjQA_ZGlpl9rKL9M0VzOfZGBXDXjIyr2TrS6N6PRxf3uIVFcoatSfG0zNkVXoyxn1-IepTRz6bHWG5prig2YfEUXdBD6Lk5RcIg44rtxcuS79h7eceG4Bf-g9nf5O72MXlsVutY6m2mG-IvozHyy4keluX3oWrGBb33gx04b7rmkAhvYfKM71kEUkcMoVCNiDv7XBXfZF36J3TpV8PAZ_LZjht8JFKcgd9TEVYFeEYLtP07FdFAFdYNMRSkFCB5dHDXKQJBnM-XnuIhZ-iyR5qOcxjliN0ayclJ7fMAHvWvaSKXAsBiOO5I26Ij848kMS6YOBUZ-F9fYcBO-jyvgtV4z-RW0b66fICUCZgDMVxFrCy2pIPM7PPeSGn6r-ACgc5BgEbJG7N2PpZbd8ctsKI6l6jozJDpjiGSJ6MMk-ATtKKsASbqSUsm7HikJKuns42U2JHfDhNEpi_GS1Ydh61QpsLtfNZ6sSDT2eiYBufrrKlndc7maMKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0c348b7c.mp4?token=E0T45z0XetPlOJG3XPBlKmMV1aL8XiJtSDRLPj9jXvKuE5FyVC4Qae2yDYqzFP-7EIBjfo8u6mM4v1HvVtHwUtBXwkvxID3v1mWslpI77lCgNkOqp1WRhhXpEs0fyJeBIS54N_PXLLwcVKJYZwjldytod7iq8dA435IvUDjDCuofDdOgS9RHYjQA_ZGlpl9rKL9M0VzOfZGBXDXjIyr2TrS6N6PRxf3uIVFcoatSfG0zNkVXoyxn1-IepTRz6bHWG5prig2YfEUXdBD6Lk5RcIg44rtxcuS79h7eceG4Bf-g9nf5O72MXlsVutY6m2mG-IvozHyy4keluX3oWrGBb33gx04b7rmkAhvYfKM71kEUkcMoVCNiDv7XBXfZF36J3TpV8PAZ_LZjht8JFKcgd9TEVYFeEYLtP07FdFAFdYNMRSkFCB5dHDXKQJBnM-XnuIhZ-iyR5qOcxjliN0ayclJ7fMAHvWvaSKXAsBiOO5I26Ij848kMS6YOBUZ-F9fYcBO-jyvgtV4z-RW0b66fICUCZgDMVxFrCy2pIPM7PPeSGn6r-ACgc5BgEbJG7N2PpZbd8ctsKI6l6jozJDpjiGSJ6MMk-ATtKKsASbqSUsm7HikJKuns42U2JHfDhNEpi_GS1Ydh61QpsLtfNZ6sSDT2eiYBufrrKlndc7maMKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعدالله زارعی: خون‌خواهی، فلسفه اصلی اربعین است و ایستادگی و خون‌خواهی در برابر جنایت، بخشی از این تفکر است/ رهبر شهید بر مردمی‌تر شدن اربعین و اتصال آن به مهدویت تأکید داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/678654" target="_blank">📅 14:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5973560f48.mp4?token=SrQF5M0-wIQ34syDslfoDkDsPTecZ8Q_V0XgOeGU6P0OSkzhWqkIST_r0RdbJ7-zvKifNMW5RoRr060LTlfxh6oIZqVMBAgKwBpilyZCOsjYEsJEDd0gHxqiigLNOA-frJYsB-_Aj9TgF9ml1UyXPCqZLxGuz4TXSF7n-2k6RfNeMNt2hRomPu-_kNn_beHn6D_UEr_CSfqfc12ii47DNvks_EH98LvLG0_2-rf9ylRJ5tCwNwhSaIiGBiAeR-b-v2zl-OdzuoSRxohuFuMDIKwz1DiQtQHxpDqFtBmbcW49_uquwP8hHZHv6ajeU67nNPIvEQwdJe2UpWzGl7kt4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5973560f48.mp4?token=SrQF5M0-wIQ34syDslfoDkDsPTecZ8Q_V0XgOeGU6P0OSkzhWqkIST_r0RdbJ7-zvKifNMW5RoRr060LTlfxh6oIZqVMBAgKwBpilyZCOsjYEsJEDd0gHxqiigLNOA-frJYsB-_Aj9TgF9ml1UyXPCqZLxGuz4TXSF7n-2k6RfNeMNt2hRomPu-_kNn_beHn6D_UEr_CSfqfc12ii47DNvks_EH98LvLG0_2-rf9ylRJ5tCwNwhSaIiGBiAeR-b-v2zl-OdzuoSRxohuFuMDIKwz1DiQtQHxpDqFtBmbcW49_uquwP8hHZHv6ajeU67nNPIvEQwdJe2UpWzGl7kt4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روت ۶۶، معروف به «جاده مادر» یا The Mother Road، یکی از افسانه‌ای‌ترین بزرگراه‌های آمریکاست
🔹
این مسیر در سال ۱۹۲۶ افتتاح شد و شیکاگو را به لس‌آنجلس وصل می‌کرد؛ بیش از ۴۰۰۰ کیلومتر جاده که از دل بیابان‌ها، شهرهای کوچک، پمپ‌بنزین‌های قدیمی و کافه‌های کلاسیک عبور می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/678652" target="_blank">📅 14:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aafd12b8ab.mp4?token=rhNToea8WcYakLtST9BUXIqR4a6tEhILJBVi5tcNuZZQZzXV8aBLJntxwe3uo_gY410zXpU4DYUuzqYgSjL9PwLdkT8DTHdV-G4thsSwWeoujGOIHLfFMaaLNJPB1hmGDXe1W9dJZzRYB5UdbAIn1zdeS82T0PUMkKvXnFr3GGkV2Ky__176RidWyUAAww2XeOPM217d8RECsxcAXW7WCX9q4CcUKlWqWMX8JI4u8Ecx4MSOAv63NCSCKrij9IFA_nkVhbIPzZcSGbj4vcckfy9KkOzR-nanH6oDKDE6XSrLNVgMNxDZFjod6F5WpqsLK1BObk4nFH9uPRwsA7urEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aafd12b8ab.mp4?token=rhNToea8WcYakLtST9BUXIqR4a6tEhILJBVi5tcNuZZQZzXV8aBLJntxwe3uo_gY410zXpU4DYUuzqYgSjL9PwLdkT8DTHdV-G4thsSwWeoujGOIHLfFMaaLNJPB1hmGDXe1W9dJZzRYB5UdbAIn1zdeS82T0PUMkKvXnFr3GGkV2Ky__176RidWyUAAww2XeOPM217d8RECsxcAXW7WCX9q4CcUKlWqWMX8JI4u8Ecx4MSOAv63NCSCKrij9IFA_nkVhbIPzZcSGbj4vcckfy9KkOzR-nanH6oDKDE6XSrLNVgMNxDZFjod6F5WpqsLK1BObk4nFH9uPRwsA7urEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خبرنگار روس از حال و هوای اربعین امسال: اینجا چیزی بیش از هرچیزی به چشم می‌خورد زنده شدن فرهنگ خونخواهی شیعه و پرچم‌های قرمز انتقام است که مردم می گویند برای فرزند حسین و انتقام مرجع عالیقدرشان به دست گرفته‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/678651" target="_blank">📅 14:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBSgtYRfvV62lqsGLfunebhCDhd0KagFVoTxaYiRYcsQvojO5lZ_RLvVx11gGLKumjTwzanrY4GZw5ISaCz3CItckTShnab9JyxliJFdzZm5CRNZcolg6_BBvlsP1K0W5KLI4M5KHHIdSM7VPKyvnf-yqSlPXlQZx5LQroU3HaDAxb-KqjUFuZwgvFPyMrAxbC8yO0Ls_hmDhOvWqrTAf0_JxI12pyYAzO-_h2xk-_vDL3IHbmUzMaxdZB9s_1oa8DiWkdReHRjCIERpdi-6NZhZOcYHLsyCaar6dVQd_IONbOuFUhmtbldI8YeVFpoUCTlWGfF8Pi1EJujeh5vLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه وزارت آموزش و پرورش درباره برگزاری امتحانات نهایی معوق در ۴ استان جنوبی کشور
ستاد عالی آزمون‌های وزارت آموزش و پرورش:
🔹
به غایبین موجه امتحانات در دو درس تخصصی پایه دوازدهم هر رشته تحصیلی در مرحله کشوری اجازه داده می شود در امتحاناتی که مطابق برنامه ابلاغی به چهار استان جنوبی کشور در روزهای شنبه ۱۷ و سه‌شنبه ۲۰ مردادماه ۱۴۰۵ برگزار می‌شود، شرکت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/678650" target="_blank">📅 14:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78392bfe3.mp4?token=Zal_FE6It0lR4y2tVe3vObqoPsGW_qggl22YE8vOZQ6BW8qL76qe9bw8mvDd2REQctwq1T5C8HWcQQPN-Ep3CtB1hKK4FXgPvRiOFgUUebnSulieGKSetUPRPq74OIBY3gVxpUq4puqEiBcNfJ3PvyGio5U2KjB70gXZbOxhlO3nAPJ1FrKSJ9PpftDCZD70Ktkyr_f9SVLRk_SDzoptzlZxe6b8Mi8UjiaVcn_8NBYUFmM4y-vXmFMhFKWE84hgA7kQ4pqTPHAYiFNt50-rmXinU2MH_r4nVm4f7Z50KEjcVAvgd5D7neObeipXui_sJFiu4M3ngLZHT-AO4sIKLC4SIW1veJSYNL23uhjOvm9c3lTNa1HbMc4KtHZnvQsSxwV0QJTYjHA36k5qqVmui_tT-ypeA9EkNLJy-jUcA3QbhWixTR4jIMd0J6weKS-LXPRUnfV_zMPccYqn7zGWTi0Fir6E3Z0gUXBAD_RIPU31GfF1yLGToNzGzVsbEwMX5ijzOw9YncTcrOm0zJ5dTHKt-IIdhqylb-U9Vtk_KhxdplM0Z-3mFPUmy0Xvc9Nma3_mpBdRrWLq1yXbLn0Dq0Mm58AqJXcGq11h6pNrDpafw5Y4_oF072kim7kwmZyk-mvHSOL1NmR5ns8orKqMVaWd_ZjHTPxqDqtev5BD444" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78392bfe3.mp4?token=Zal_FE6It0lR4y2tVe3vObqoPsGW_qggl22YE8vOZQ6BW8qL76qe9bw8mvDd2REQctwq1T5C8HWcQQPN-Ep3CtB1hKK4FXgPvRiOFgUUebnSulieGKSetUPRPq74OIBY3gVxpUq4puqEiBcNfJ3PvyGio5U2KjB70gXZbOxhlO3nAPJ1FrKSJ9PpftDCZD70Ktkyr_f9SVLRk_SDzoptzlZxe6b8Mi8UjiaVcn_8NBYUFmM4y-vXmFMhFKWE84hgA7kQ4pqTPHAYiFNt50-rmXinU2MH_r4nVm4f7Z50KEjcVAvgd5D7neObeipXui_sJFiu4M3ngLZHT-AO4sIKLC4SIW1veJSYNL23uhjOvm9c3lTNa1HbMc4KtHZnvQsSxwV0QJTYjHA36k5qqVmui_tT-ypeA9EkNLJy-jUcA3QbhWixTR4jIMd0J6weKS-LXPRUnfV_zMPccYqn7zGWTi0Fir6E3Z0gUXBAD_RIPU31GfF1yLGToNzGzVsbEwMX5ijzOw9YncTcrOm0zJ5dTHKt-IIdhqylb-U9Vtk_KhxdplM0Z-3mFPUmy0Xvc9Nma3_mpBdRrWLq1yXbLn0Dq0Mm58AqJXcGq11h6pNrDpafw5Y4_oF072kim7kwmZyk-mvHSOL1NmR5ns8orKqMVaWd_ZjHTPxqDqtev5BD444" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین روایت از «روزی روزگاری میناب» با روایت ماکان نصیری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/678649" target="_blank">📅 14:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0fe9bb76.mp4?token=aywfSUJhyFuhP-me-hTC_jG0FgQUuKby_QO--od9NW2MOI7RmJxRorC0sYPZDtSaLVPNSeGTL_hu8NGXgCEMmvOM0_w67FpQtUY63NM3Jx42AjyvjQZwrOSsIMH0Wa5l2wMrMsE8YLU12mXndmuG1U2zQORZd0GSQYQpXVq0vcjzxK7kT6tnuVhCJu6XxpfKgjB3a57G62hc8lOR_-Kaffdw1huFH31ajQJ8Od6Lsst6XNxpV5nSiMSgqxzlzVLWTV0KFzuWfVJ1UXlgZR6_1k1bKbxkwAZMOYcmADOus5xxpKMdIGsNOzyokElyBeOUPCdllR8z_L2RaBBvApfFbBbAxC1WVhedzNilsq7TvaI5CH_5OutqwoAuQSpo9UbFyP_s6V85LRsHtMNrx_PRbNunTLPV0pTvjAh_RBXwl3y1weJiYYRmX6oUGklimTT_rHg9unuHC7Vque2FBbSEeEUz2bOPqZhY9Loc6uj7KxKAgu7CgvvknKJ9OoWj6naqdXm9oezK9lKrc9Kl-YWWXke1XLyTcz7KaiuCIVr7zE-1aN0KfM_AT74cOF6Mxs27lyVqoJiGZQiW-OYpCq7WgBwxULNmMJ8EA43gtoy_H8f-vxW4EILkSksfgFAXlJTqUsFjys6XjzLawplYkGRNUWiZHyuWe8znD7Llq1hTbVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0fe9bb76.mp4?token=aywfSUJhyFuhP-me-hTC_jG0FgQUuKby_QO--od9NW2MOI7RmJxRorC0sYPZDtSaLVPNSeGTL_hu8NGXgCEMmvOM0_w67FpQtUY63NM3Jx42AjyvjQZwrOSsIMH0Wa5l2wMrMsE8YLU12mXndmuG1U2zQORZd0GSQYQpXVq0vcjzxK7kT6tnuVhCJu6XxpfKgjB3a57G62hc8lOR_-Kaffdw1huFH31ajQJ8Od6Lsst6XNxpV5nSiMSgqxzlzVLWTV0KFzuWfVJ1UXlgZR6_1k1bKbxkwAZMOYcmADOus5xxpKMdIGsNOzyokElyBeOUPCdllR8z_L2RaBBvApfFbBbAxC1WVhedzNilsq7TvaI5CH_5OutqwoAuQSpo9UbFyP_s6V85LRsHtMNrx_PRbNunTLPV0pTvjAh_RBXwl3y1weJiYYRmX6oUGklimTT_rHg9unuHC7Vque2FBbSEeEUz2bOPqZhY9Loc6uj7KxKAgu7CgvvknKJ9OoWj6naqdXm9oezK9lKrc9Kl-YWWXke1XLyTcz7KaiuCIVr7zE-1aN0KfM_AT74cOF6Mxs27lyVqoJiGZQiW-OYpCq7WgBwxULNmMJ8EA43gtoy_H8f-vxW4EILkSksfgFAXlJTqUsFjys6XjzLawplYkGRNUWiZHyuWe8znD7Llq1hTbVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، تحلیلگر جبهه مقاومت: خلع سلاح مقاومت در کار نیست و نخواهد بود/ هیچ سلاحی از غزه خارج یا تحویل رژیم صهیونیستی نخواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/678648" target="_blank">📅 14:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678647">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKDy2YLciWQrIFcsCa-Xe3s0nrovFXleENX47d8qOhyUYyu3r796aVUcT9EmjEIITjfT6_xMiAfXyemDyxwZWjyhSPwLl1_DPO7c6X4f-_-XkwfSa_saLMwVSXvoGqDQTQ9M8IpzmxDMzBKS0_ZDaqjeb1Z0BhoTJ_BX84dEz093983AD4vMyARR-Izg9dO6NZK48cGZV3MhzyLa69373n0JF8CTe4AGEmcOdKWM0jpSvIbl-5IMuXjHtKEmlMEtceIeofZnVEfIf4jNinaTFGU_JTjCnGR7exmY_R-D69EYd1Ab4KyXS_WkufU0j9RuR35_M6PIVv487PLNvgpHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عمو فقط «ابوالفضل العباس» علیه‌السلام
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/678647" target="_blank">📅 14:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678646">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل به نقل از منابع: اسرائیل اطلاعات مستقیمی از آمریکا در مورد مذاکرات با ایران، دریافت نمی‌کند
🔹
اسرائیلی‌ها معتقد هستند که تصمیمات ترامپ با ابهام، تاریکی و تلاطم زیادی همراه است.
🔹
ترامپ و مشاوران او به هر قیمتی خواهان توافق هستند؛ تهران نیز از این موضوع آگاه است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/678646" target="_blank">📅 14:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678645">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b43e18223.mp4?token=D20cEpw51kl3-KHmg3qHkHlPwuaKIpzXEBPu4tzcfgASWUZXIK6AYVc80trhaCXfEW62Y2kZzK0anTFzZaffH3EcCLHEHTxPd8Lp28MuUHFP3RDSkaHzPd6WWSMTCrU6_Pfry0VKo3aFLbT_-qz72LHzo1jPHHQYLHa7e9ZLGmbXP2atb1yFwlSLSyuoWd5NEUG7Qhe-elk677XOP36Qxr7DdmJRY0wOPK5vB0hOB89JcpwlHinMXOc3xNuAWj5d2tPilUc3ShpQDfQgVCuW_nacRwZYbxaEp_mHcPM5ZGfwfIm_kxuIXvVPgJIA3G_95L6uWsFXfJkwWMy83luWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b43e18223.mp4?token=D20cEpw51kl3-KHmg3qHkHlPwuaKIpzXEBPu4tzcfgASWUZXIK6AYVc80trhaCXfEW62Y2kZzK0anTFzZaffH3EcCLHEHTxPd8Lp28MuUHFP3RDSkaHzPd6WWSMTCrU6_Pfry0VKo3aFLbT_-qz72LHzo1jPHHQYLHa7e9ZLGmbXP2atb1yFwlSLSyuoWd5NEUG7Qhe-elk677XOP36Qxr7DdmJRY0wOPK5vB0hOB89JcpwlHinMXOc3xNuAWj5d2tPilUc3ShpQDfQgVCuW_nacRwZYbxaEp_mHcPM5ZGfwfIm_kxuIXvVPgJIA3G_95L6uWsFXfJkwWMy83luWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری عامل تولید کلیپ جعلی اعتراض نوجوانان کشتی‌گیر به اعدام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/678645" target="_blank">📅 14:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678644">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
اعلام شرط تداوم دریافت یارانه نقدی و کالابرگ
سخنگوی دولت:
🔹
افرادی که پیامک اطلاع‌رسانی دریافت کرده‌اند تا پایان شهریور فرصت دارند با مراجعه به دفاتر منتخب پیشخوان دولت، نسبت به احراز هویت و اعلام حضور خود در کشوراقدام کنند و از هرگونه مراجعه به ستاد وزارت تعاون، ادارات استانی و سایر دستگاه‌ها خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/678644" target="_blank">📅 14:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678643">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
دفتر رسانه‌ای دبی گزارش‌داد که آتش‌سوزی که شب گذشته در منطقه صنعتی جبل علی رخ داد، ناشی از حادثه‌ای در یک کارگاه بود که باعث آتش گرفتن چندین کامیون شد که خاموش شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/678643" target="_blank">📅 14:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678642">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
برخی منابع خبری از شنیده شدن صدای انفجار در استان لاذقیه سوریه خبر دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/678642" target="_blank">📅 14:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678639">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umOdMXFSJnNAzHFqSJxGzw68djworUO98Uaa3Vq6EWxvayN_JIaZgLDu9Delka0mqSAuDRYK_VsJPo4p-A96t0RcFRARBIy8qaMjAgGb5ebF28oDWyT69kvCpLUZIjJ0VhM2TT6iCUB1SK9kyEEE62Q0OpskS5G778aRShbu3FHn05UjLqfH_keFzesLQAzx9QB6gcrFyXY4O0j0hRhM2UFmrCfQBIoPdcLcERrqjJ0ryb_p9TuPZpNSRASl84rwxITfieI-f3FUN3W_i26OCB7wIN0aXKxG2xBmgCzb6sBTSjOLMvsF-OfGM8Qyd8x9yv0MIAVVhsCfQyqSuykywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3ySlFHufWUfU8fV9ltUMJ_29MQF8qmtj_uFizkadjniNmr7AOaf6OBZWROyvgq4Bb9HpaKzYSgkDr-KMuuOPes7cGpLEAnJfmeofGckiZwGZY4krAkZfcPyoN1cTddsH8WGn_wGBNcuyymDC1oEy4sx7K11kYyF8WIsosguMhHX6XsieJx15ur2OM6FYspa9i-W7AA3WUmOznKwTA04_z9-xicOQeuGZo-yZY7I-f8ohYj8u5l5XVlTW_tLFde5_QBp67drWu3FSxZPUP2H9tjSOKAGe7kUu_NseQOqSMxvHL0hYj1uI7ItqjYjT0g3UEa371_aDYHQT4h4D3vAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UiVXHAgrfb0WPlYuUmPfqpG7Hv4CavJS-rzjZXKtVDyOBFEhIS4a-pDM5ALO0Pv_TWB8a1ANtyab5jDcrHKrR0LODXAM7bvNg8DfKikJbITRCqsHuoVHadq9DZQZjxgKwlJ6A1LODdt5YRSucfGzdCIVee14JcU3wjM_oVcQbgZPgPN-8tg1o7udXLJKCe2hzn8fTPbl5D9ST-v7Mo907NI2C_XM86z1gBgaSGEAk_0i8feMu9BaBQESbQQC0PstwW6ZO1d1QSwTqstyDydMwir3IzcvJk5DL_T70uA0ljTROTEZ1Lh8-HGVhYtBmZnjQlwASPmrxVGx0uJ1fG54PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عقاب‌کوه، شاهکار طبیعت در دل کویر یزد
🔹
عقاب‌کوه، یکی از شگفت‌انگیزترین پدیده‌های طبیعی یزد، با صخره‌ای که زاویه‌ای خاص شبیه عقابی باشکوه دیده می‌شود، نمادی از عظمت و استواری در قلب کویر است.
🔹
سید محمد عرب فراشاهی
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/678639" target="_blank">📅 14:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678638">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25f690277.mp4?token=MwQCXCkmjJG0NjD2mgedXSVSfu0kTbXYJYLmnjGHIW9UsTvyWtQebahEztZrnQ4l39xK2DVQ_6SjLJz4J0UGqN9lBzlxcloicNi83sl2Kaoq5nZhAMZpAAvkCMlp7KiUAyJCzZOX6xg5Xi1Rg_M8lSs0Mq6xYbOlW-4A59IqwX1z1ePlYDXsbpYRITSBuC7TRijdcc7QI9qjM0OATH_dwEuSuFzhRnSDyljgxEGeO0v3qQLko1J5wsE8yF1kT4-yox_ppb_ZsuCawzI4i11Z87Ve5QVgfMVJaaLU7Crbx8fVR1wn-ld0U-ptPs9I7sc-QukwR5QiIeNFIKcsZRg_Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25f690277.mp4?token=MwQCXCkmjJG0NjD2mgedXSVSfu0kTbXYJYLmnjGHIW9UsTvyWtQebahEztZrnQ4l39xK2DVQ_6SjLJz4J0UGqN9lBzlxcloicNi83sl2Kaoq5nZhAMZpAAvkCMlp7KiUAyJCzZOX6xg5Xi1Rg_M8lSs0Mq6xYbOlW-4A59IqwX1z1ePlYDXsbpYRITSBuC7TRijdcc7QI9qjM0OATH_dwEuSuFzhRnSDyljgxEGeO0v3qQLko1J5wsE8yF1kT4-yox_ppb_ZsuCawzI4i11Z87Ve5QVgfMVJaaLU7Crbx8fVR1wn-ld0U-ptPs9I7sc-QukwR5QiIeNFIKcsZRg_Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌬
پنکه رومیزی مه‌پاش | خنکی بیشتر با مصرف آب بهینه
💦
دارای تایمر
⏱️
+ ۳ درجه تنظیم باد + تنظیم اسپری مه‌پاش
✅
مناسب برای خنک‌کردن محیط و مه‌پاش سبک برای گیاهان حساس
🌿
🔌
شارژی نیست و باتری ندارد؛ مستقیم با USB Type‑C به برق وصل می‌شود (قابل استفاده با آداپتور، پاوربانک و فندکی خودرو)
💧
مخزن: ۵۰۰ سی‌سی
⚡️
توان: ۱۰ وات | ورودی: ۲ آمپر
📏
ابعاد: 23×17×6 سانتی‌متر
🎨
ارسال رنگ رندوم
🔴
قیمت 1,780,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/47572/180124/</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/678638" target="_blank">📅 14:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678637">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حسن روحانی: رهبر شهید هیچ‌وقت دنبال جنگ نبودند
🔹
تمام ادعاهای ترامپ، حرف‌های توخالی است، دولت در این ۱۴ ماه کار بزرگی کرده است.
🔹
آمریکا با حمله به مدرسه میناب خواست بی‌رحمی خود را نشان دهد،  باید دشمن را مهار و گاهی هم دوست را هدایت کرد.
🔹
می‌خواستند برای سخنرانی امام زمان در تهران جایگاه درست کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/678637" target="_blank">📅 14:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678636">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ودوم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حمید جعفری که ساعتی بعد از بحث و ناراحتی با پدر در خیابان تصادف و روح از جسم جدا می‌شود اما مدت زیادی برای اثبات حال خوبش به خانواده تلاش کرده ولی در نهایت از تونل تاریک و مذاب به برزخ منتقل شده و عذاب اعمال خودش از جمله بدرفتاری با شاگردان، خواهر، همسر و پدر را متحمل شده، اما بخاطر جلوگیری از خودکشی مادر ایشان بعد از مرگ پسرش، به دنیا باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حمید جعفری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/678636" target="_blank">📅 14:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678635">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
روسیه از تصرف دو شهرک زارنیتسا و ریژوکا خبر داد
🔹
وزارت دفاع روسیه گزارش داد، شهرک "زارنیتسا" در منطقه زاپروژیا و شهرک "ریژوکا" در منطقه سومی توسط نیروهای مسلح روسیه آزاد شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/678635" target="_blank">📅 14:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678634">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD8j9Y0OBZOrswN2mGArJOdk8vRBBP0U-eU2x-oVFADeV5k0oz-ZnssWFQVm7PBOgWGFmjhpfJMna-FtN1po5in2DiBP5ZZrGJkAgOkHF5E2SMS_1289szUv5S0lYADYM1-zh1uoF55K_efCK7COFUbSjvto4balKKKoG0MiGyzKINmhSUw4D_ZYRfsUprY0DYeQXzmE_um2ieAmJJgbEhvb0R4eG94BoGqV4lsFLE8shwZcITK033YsrJetFcjjfReewGZ7CoUNBcaa57m3_HROkehAnM245uDtNpUA2I2HQ0mmywKFs_SHk46Ndqice1bHDPTxJnsBeTry1kMFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
جهش بیش از ۳۳ برابری سود خالص بانک رفاه کارگران در بهار ۱۴۰۵
🔹️
بانک رفاه کارگران بر پایه جدیدترین اطلاعات و صورت‌های مالی منتشرشده در سامانه کدال، در بهار سال جاری با ثبت رشد خیره‌کننده ۳۳۷۱ درصدی سود خالص، عملکردی درخشان از خود به نمایش گذاشت.
🔹️
بر اساس صورت‌های مالی مذکور، سود خالص این بانک در سه ماهه نخست سال جاری به رقمی بالغ بر ۲۲ هزار میلیارد ریال رسیده است که در مقایسه با دوره مشابه سال گذشته (حدود ۶۵۱ میلیارد ریال)، جهشی ۳۳ برابری را نشان می‌دهد.
🔹️
براساس گزارش کدال، درآمدهای تسهیلات اعطایی بانک نیز در این دوره با رشد ۵۳ درصدی به بیش از ۱۷۵ هزار میلیارد ریال رسیده است که نشان‌دهنده ارتقای توان تخصیص منابع و حمایت از بخش‌های تولیدی و اقتصادی کشور است.
🔹️
این جهش عملیاتی در حوزه اعطای تسهیلات، بیش از هر چیز بیانگر تمرکز راهبردی بانک رفاه کارگران بر ایفای نقش اثربخش در اقتصاد کلان کشور است. هدایت منابع مالی به سمت پروژه‌های پیشران و واحدهای تولیدی، علاوه بر تزریق نقدینگی به رگ‌های صنعت، گامی عملی در جهت تثبیت و ایجاد فرصت‌های شغلی جدید محسوب می‌شود.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/678634" target="_blank">📅 14:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678633">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d566067c28.mp4?token=F-5dwUjNOOBRUFIS3FHfPNaPPex0cByuJekF9CYy5PGSusvvFhveNASIyLr0sVzBKzB8i_QRx3mtImhtKWWo-NE265oJY_a6eBeemQNkR8VicSZNe3ltyiVuJoa-Z5saIb3oPQ19xbh84BEeXtpOKwO1DAM2DWIWVq5bkL6RfBEKQdeKaQvXzBq36shiK7icvjSnze5pvISoLLVaqvVf9JbhjERRRkOTNmyflPaZGtTbPNA-Q53kRhw3dhtZBMtsfASfQzEdxHmKBKpmdQhIXq9VorB6eHJ9v7QEPXPnsFktKpDy-bir9wq6yOv5EzPl36ud0riIwUDdkqMcNY23Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d566067c28.mp4?token=F-5dwUjNOOBRUFIS3FHfPNaPPex0cByuJekF9CYy5PGSusvvFhveNASIyLr0sVzBKzB8i_QRx3mtImhtKWWo-NE265oJY_a6eBeemQNkR8VicSZNe3ltyiVuJoa-Z5saIb3oPQ19xbh84BEeXtpOKwO1DAM2DWIWVq5bkL6RfBEKQdeKaQvXzBq36shiK7icvjSnze5pvISoLLVaqvVf9JbhjERRRkOTNmyflPaZGtTbPNA-Q53kRhw3dhtZBMtsfASfQzEdxHmKBKpmdQhIXq9VorB6eHJ9v7QEPXPnsFktKpDy-bir9wq6yOv5EzPl36ud0riIwUDdkqMcNY23Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به همین راحتی شالت رو خیلی شیک و ساده اما باحجاب سرت کن
✨
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/678633" target="_blank">📅 14:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678632">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8dfce68e9.mp4?token=XihAgK7WPWCSsKeQmw0j5iwzmqezDX15P5LSRD8fcjaDmS4k8KsLJ-ksyYuSndELxOSZQ8cveipTNofl7Klys2WNHQrHrYyKNTsnZ0Dlt9U_Z-iROvTjZK7ecdBv_IduwLN2dqyJEcD0r8cVhXDgVXPm67UdT9r1zf8t-wjWC4w5RVggO4j8tDn5QjvYtmoRWK1X-LmskHU7ri_ESPcEytxZynUXomCXT1dMs6EsyaZydKjCRvc4YN2PkBcAzasuO5DcFUdc5ooq34CQ4-4WMnEbvL3IJYNs-R_ghDDUvOA_UteGmgtEOXeKx6jU4vuF1gaojYv39NLqxyGgxBJi6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8dfce68e9.mp4?token=XihAgK7WPWCSsKeQmw0j5iwzmqezDX15P5LSRD8fcjaDmS4k8KsLJ-ksyYuSndELxOSZQ8cveipTNofl7Klys2WNHQrHrYyKNTsnZ0Dlt9U_Z-iROvTjZK7ecdBv_IduwLN2dqyJEcD0r8cVhXDgVXPm67UdT9r1zf8t-wjWC4w5RVggO4j8tDn5QjvYtmoRWK1X-LmskHU7ri_ESPcEytxZynUXomCXT1dMs6EsyaZydKjCRvc4YN2PkBcAzasuO5DcFUdc5ooq34CQ4-4WMnEbvL3IJYNs-R_ghDDUvOA_UteGmgtEOXeKx6jU4vuF1gaojYv39NLqxyGgxBJi6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تست ساده، قدرت ریه‌هایتون را به چالش می‌کشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/678632" target="_blank">📅 13:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678631">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c47d2a81d.mp4?token=swzrtlY_Dko0AhwD9j8MTU8QT2CvfxxOXB3h9n0hcFpSXWXFI1T6P30Owp12unZGdZhXbwc_gMtlrgv2-jymrKg4wd3pp9IbgNLqmfeGQS47nfZ0nl7EqRHDUw4A3FpOGejdmZWvZzRK0Fg7zh6wvIaDlDPt1k0lNi2behWXq9-7TKiqREVuDX71rnPIQVCQ1ejBYMoGpEGfMn0XXj2wyIu8Bi3vlZumTy_JAiPXt5feUyqc2nV_dDXagmicpnW1XPlNcZbQuBUiC65LUaRDf19lYKdLodlsvAxRcC3429usQ9Dw3SnyUWcKQmLF1NebTmdRie488YYM-ost7-cjyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c47d2a81d.mp4?token=swzrtlY_Dko0AhwD9j8MTU8QT2CvfxxOXB3h9n0hcFpSXWXFI1T6P30Owp12unZGdZhXbwc_gMtlrgv2-jymrKg4wd3pp9IbgNLqmfeGQS47nfZ0nl7EqRHDUw4A3FpOGejdmZWvZzRK0Fg7zh6wvIaDlDPt1k0lNi2behWXq9-7TKiqREVuDX71rnPIQVCQ1ejBYMoGpEGfMn0XXj2wyIu8Bi3vlZumTy_JAiPXt5feUyqc2nV_dDXagmicpnW1XPlNcZbQuBUiC65LUaRDf19lYKdLodlsvAxRcC3429usQ9Dw3SnyUWcKQmLF1NebTmdRie488YYM-ost7-cjyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: با هزینه جنگ علیه ایران، می‌شد میلیون‌ها آمریکایی را از گرسنگی نجات داد!
🔹
هزینه واقعی جنگ با ایران بسیار فراتر از آمار رسمی ۳۷.۵ میلیارد دلاری دولت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/678631" target="_blank">📅 13:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678630">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa54ce8da1.mp4?token=LVlrRIp5cTFDCChkzJxultIVCmEKIrC_t3GqXidSMCVErLSMsX6J_MsiLURIdu7JksMgTDm-T3TzYgB3ZRfsaYBcw_ekpSMM-gHWvjkloQ7soqDnG_6LWAizvvhbB6_U2RrMgQL5BIVxBN_oOC_ff7gKIVtIf_v6NBtGFwnvYQU0lLxIZuuuk1uLPI9oStH5CO3DIZqCD3cjieTcANX-mQn6z7ak2g1j-syW7zg6BppqIbVxA-bBSg6E_zZiR6Ii2k8LCmIZpp8c2XD_Zwf7PC9mk-1NDSzL-cbLLh58h_cUfht12_B34UjM2CFtUQhTRfiIvl05TYrgOIKyQhfyxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa54ce8da1.mp4?token=LVlrRIp5cTFDCChkzJxultIVCmEKIrC_t3GqXidSMCVErLSMsX6J_MsiLURIdu7JksMgTDm-T3TzYgB3ZRfsaYBcw_ekpSMM-gHWvjkloQ7soqDnG_6LWAizvvhbB6_U2RrMgQL5BIVxBN_oOC_ff7gKIVtIf_v6NBtGFwnvYQU0lLxIZuuuk1uLPI9oStH5CO3DIZqCD3cjieTcANX-mQn6z7ak2g1j-syW7zg6BppqIbVxA-bBSg6E_zZiR6Ii2k8LCmIZpp8c2XD_Zwf7PC9mk-1NDSzL-cbLLh58h_cUfht12_B34UjM2CFtUQhTRfiIvl05TYrgOIKyQhfyxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران من دور از تو چشم بد عشق تو تا ابد با من می‌ماند
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/678630" target="_blank">📅 13:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678629">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f827818fc9.mp4?token=L0ZsvQnbBoORE97qLOGan_Chg4pzJOpDc0MzW97K-i0P0QQj8ey5ZTIr_z_z7-U1vOBcNuDBxN5solVTSpQKf5ep7QRUDrytchmdXtKigYuDT74I2L4lrEr45VJiZ5tos4B43bm730QsTlQxEbKHtaaUzGz6v8pTpQLzxlOubPV_UOdzrvnsYQbCzXKU8jn0y6-le030kzPyd3p5jZ4GvzwsO62_iwp3tl_bNdtkwEJNfnosmf9iT78FLPWHrxovy4jkFc8HT24mkl5d1jhp1ObkNxnwRsngUqu8ghsJfJ5iP2ut8fkFbuieVMWrtutCRXOPHn8nLFimVxihim1ub2AJxFuo2Hl_SiXpK67vjry7SjnH32BC901yG6cgv2VL4Zp3NuQ5mfTNpZNqEUuPNZQ3jBtJPF5PJG4ZW2T-q1Wuj9lTtuWOxpFK2NMZ_JCFix2Gqrlx6zJ4SdO4mDfUzae2cSVVXlDPtcB-JxzKacpp_cbx1tNz9re6YZ78Ei3gRz33fDZGfCvwPf6D4LiqOPGHtBKhSpwkD7WpI5EIQLuPW5GvxSLTBL5hDeGzqFYMvHieFbS88LTghQ9zfp0YISmEcE3PsGvLr2DbCnPZswbQ128sPzA44yV10h1oGHDrv6bt2GXsqDrrnQ5sMQ0ywpH_YweHbHYibZhl29aA4rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f827818fc9.mp4?token=L0ZsvQnbBoORE97qLOGan_Chg4pzJOpDc0MzW97K-i0P0QQj8ey5ZTIr_z_z7-U1vOBcNuDBxN5solVTSpQKf5ep7QRUDrytchmdXtKigYuDT74I2L4lrEr45VJiZ5tos4B43bm730QsTlQxEbKHtaaUzGz6v8pTpQLzxlOubPV_UOdzrvnsYQbCzXKU8jn0y6-le030kzPyd3p5jZ4GvzwsO62_iwp3tl_bNdtkwEJNfnosmf9iT78FLPWHrxovy4jkFc8HT24mkl5d1jhp1ObkNxnwRsngUqu8ghsJfJ5iP2ut8fkFbuieVMWrtutCRXOPHn8nLFimVxihim1ub2AJxFuo2Hl_SiXpK67vjry7SjnH32BC901yG6cgv2VL4Zp3NuQ5mfTNpZNqEUuPNZQ3jBtJPF5PJG4ZW2T-q1Wuj9lTtuWOxpFK2NMZ_JCFix2Gqrlx6zJ4SdO4mDfUzae2cSVVXlDPtcB-JxzKacpp_cbx1tNz9re6YZ78Ei3gRz33fDZGfCvwPf6D4LiqOPGHtBKhSpwkD7WpI5EIQLuPW5GvxSLTBL5hDeGzqFYMvHieFbS88LTghQ9zfp0YISmEcE3PsGvLr2DbCnPZswbQ128sPzA44yV10h1oGHDrv6bt2GXsqDrrnQ5sMQ0ywpH_YweHbHYibZhl29aA4rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرشایمر: ایران سخت‌گیرانه‌تر از همیشه مذاکره خواهد کرد
استاد علوم سیاسی دانشگاه شیکاگو:
🔹
ایران اکنون بیش از هر زمان دیگری از برتری موقعیت خود آگاه است.
🔹
ترامپ هیچ گزینه دیگری ندارد. او هیچ راهبرد نظامی در اختیار ندارد که بتواند با استفاده از آن وضعیت بحرانی کنونی را تغییر دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/678629" target="_blank">📅 13:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678628">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H69NYRMCMpTAJKQxFPG8s6DcJJAzTnQNH25K1yZ1RtAW0fKA25LwihjLQa-YKJkNe38ZySvxp-2slT1TA1PtBL7GOU9alSIwQuvdaecoiPfE8Pxa48y5Tw2KIWrLMLdjBSKEQmT1TRCl2ubTK7q9LxDEZPjHETzCRA1iYDGgiXDP0X8SQf-s866kC4xJXo65dE-V0T4gA3jnLvfCLcYt1hoDTWf4LZJNResjshDdJeKofdpcq9ZyhWy312Ptjq1nRqgXaVCUfbpATxRwkNpWIA-jZilyGwoUji0TJu0If4N-wIspVJLYNYLahA9W3gk2duys7KPV8UifgCz9_2HvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به ۷۶ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/678628" target="_blank">📅 13:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678627">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL9JVluWFOpT9DBIBHE3PubBeKdLSeTT9hIIgZuQ6kWs4UAo2wzTrcFEBLBimhRH-uYNOGrQ-qejx2rWu_or6lTO8WzW3y53Q2NhdcLBXXSndgGgDnHwvDFRjMwoZH_i_dlxbTB1nQESvwml7tZDCXoA0LBDMoUElXN-GxswlvBwIQM4yYEA5Nb-9xU4eJSlrG0amhu_xf642mySm0pX9QhrR_0EC4SDfQ0SL-DE9BQlt8O7im-dZqcqvFHD4RIbUWTDnKVVIh7lKEppKG0YpS7GwwFPDhE1In-POIR0uLvNGoNy_pKCQBAzfi3IolseF_IxUdqZqeRtxBuN9LMHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به شهرک «المنصوری» در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/678627" target="_blank">📅 13:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678625">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGTUXc2M7lf6Y4EbBKnjYP2Q6-2U65uDV4uP3b2V6oykgwnpR60IZXq1tEhHMdhtMuuKG183hkxa4j-ZfS6xOksDP0ib5hxo-4SiBNq-hlir17_vhl1ALShkSPrylCtbZBxtT0uj49-sQmjB-sekHfEusVH8XVbw2_3bcSPCfu4wBAKzg3HyGFJL_I1rMID9rq83slFRa48fjP8cSF-xzMSzB7B6cySJhELtBt7Z4T2MPg5AcGN6qkdA7ay-3wYP4-C5WN9L1ZdYlcn7UJ_jjk3WHRFbkdcAuFhKpcAFrjBTnZnl_-e9CIYOc1pc29ZAs3E_vyGLdJ_Z2T57eZpJLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی محیط‌زیست هم از ترامپ در امان نیست!
🔹
ترامپ با انتقاد از فعالان محیط‌زیست، مدعی شد محدودیت‌های زیست‌محیطی تولید نفت، گاز، چوب و ساخت‌وساز را مختل کرده است.
🔹
کسی که حتی به حیوانات هم رحم نمی‌کند، چطور بعضی‌ها معتقدند که قرار است ایران را آباد کند؟
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/678625" target="_blank">📅 13:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678624">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ان‌بی‌سی: آمریکا شیوه استفاده از بمب‌های اتمی تاکتیکی را تسهیل می‌کند
🔹
آمریکا قصد دارد با تغییر راهبردهای دکترین هسته‌ای خود، شیوه استفاده از بمب‌های اتمی تاکتیکی را آسان‌تر و مشروع‌تر کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/678624" target="_blank">📅 13:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678623">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه نیک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIyhmY530a6vYJ1W4B7AacKui4DR4c3Ke5Aj4EAIcx5LnwGdwLkISQUUfRHIJZ0wRdtle_oaXR8qXLEU7aCYL7ASdkCMwVVK7XpU4n47lSbDp_K3PQ9klGHzVkkNM9WEJJpx2hsoEuSnqD_havLF1FIHKAqOEUiQAdZcNw2VLzv3AS1buCnO7Nvve316fAuuWWy0kCMq3LHXmCA9kYlSu727hZ07fLbthnkx5L-YRBQOjmd2vTcpN8aH4JWJWX0Il1amwKPgWMsSh-75C1o_Prxg_Dm0GbVRTAk07A8_6Iz5VfG7fY8s7LGucE05KTKQa-Yobp6M6sijeU7gQvk7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فقط ۲ سال دارد اما روزهای کودکی‌اش میان آزمایش، دارو و درمان می‌گذرد
😭
💔
او پس از پیوند مغز استخوان، برای ادامه مسیر درمان به  داروهای حیاتی نیاز دارد؛ اما خانواده‌اش با درآمد اندک کارگری، توان پرداخت هزینه‌های درمان، اقامت در تهران و معیشت را ندارند
🥺
بیایید دست‌های مهربانمان را از ارغوان دریغ نکنیم؛ شاید کمک امروز ما، سلامتی را به ارغوان بازگرداند
😭
🙏🏼
🌹
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
6037691990491185
6280237094218423
IR
110190000000216777746001
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@Pr_nikcharity
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/678623" target="_blank">📅 13:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690251c8f1.mp4?token=XJd8ChcIRGdZHzYs7TDGpgA-egudjLD4_0lbJ803nIF1F367m-Pws-FMZA6yXqG_Onmw2Wvf_WciNaL0ldw1gf5t1DDeO_kZHRc7fEE9iNPdNT3C6e2r4mEwwPpRGrSwqgNua59umx1Gb4ioWs-QDLZy5eaV1yZz_ALWEaKDAHF4aZKVmzD0JX8B4CO5EO3yqiEjKB9T4im8L4YMotU1zthTeCFk0y_1cld26lc7ZuufZvpW8EA5ZcyMXte5AjQJVocl_giqOvmmZQ13Cmd9RWqGCtWlpdoI8mp2ON1hqDJlRig01LXhehMClhik9lAnU5OYTCdv7tEf3rIZ7oWa1JPclnKs8tgX5YKMSMpWykCbYQk_5imriLvrjSkvSgLPRZ7jbqhZSAqfH2d8xWAWjzxsRlsI0vMGv-iwfA1eBeWpQVV152wGE4pTrCjOnPW868iSn-xEZkBJgXeDLKTJGmZaqbBKTmaSTHeXpgOKjal9i0vj5bkoJPGIYXC-K7OhvrdVY0VBNWx9R3n966OMybMvDZf-fUBxeAenYJtngZSsx-mluDTeJ6-MzNdsBO73UqimBEXVHJ4FT9bufgiEqL7y1ojFrMUjKteKerc6XtoZS87xWbIPCCc1V9qQGXn43v_ezIKzpapHKMTjgaCo3FVj2okg7CsR4F-BrmIV2U4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690251c8f1.mp4?token=XJd8ChcIRGdZHzYs7TDGpgA-egudjLD4_0lbJ803nIF1F367m-Pws-FMZA6yXqG_Onmw2Wvf_WciNaL0ldw1gf5t1DDeO_kZHRc7fEE9iNPdNT3C6e2r4mEwwPpRGrSwqgNua59umx1Gb4ioWs-QDLZy5eaV1yZz_ALWEaKDAHF4aZKVmzD0JX8B4CO5EO3yqiEjKB9T4im8L4YMotU1zthTeCFk0y_1cld26lc7ZuufZvpW8EA5ZcyMXte5AjQJVocl_giqOvmmZQ13Cmd9RWqGCtWlpdoI8mp2ON1hqDJlRig01LXhehMClhik9lAnU5OYTCdv7tEf3rIZ7oWa1JPclnKs8tgX5YKMSMpWykCbYQk_5imriLvrjSkvSgLPRZ7jbqhZSAqfH2d8xWAWjzxsRlsI0vMGv-iwfA1eBeWpQVV152wGE4pTrCjOnPW868iSn-xEZkBJgXeDLKTJGmZaqbBKTmaSTHeXpgOKjal9i0vj5bkoJPGIYXC-K7OhvrdVY0VBNWx9R3n966OMybMvDZf-fUBxeAenYJtngZSsx-mluDTeJ6-MzNdsBO73UqimBEXVHJ4FT9bufgiEqL7y1ojFrMUjKteKerc6XtoZS87xWbIPCCc1V9qQGXn43v_ezIKzpapHKMTjgaCo3FVj2okg7CsR4F-BrmIV2U4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
چگونه مجوز واردات و صادرات بگیریم؟
🔺
کارت بازرگانی برای انجام واردات و صادرات ضروری است. برای طی کردن راحت‌تر مسیر دریافت کارت بازرگانی، ابتدا این ویدیو را ببینید. در صورت نیاز به راهنمایی، با مرکز تماس اتاق تهران به شماره
۱۸۶۶
تماس بگیرید.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
service.tccim.ir/membership</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678622" target="_blank">📅 13:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUrdv-fkvKW-SNdp9FkGh0uEVQCKZtZj5DSeb5-TCOkQ4-SJdcJ7uuYCJkAm9KeevGtvQEzdjUSAZCDxEJPGtsCfQmwj-Ucd_pFlSMNyPX-5hJsPSc6vn7DF3I4p4B8KvQZIoKgw4ANB6wzLCdoPFDtUAeEZEpqezr99LjEp2j3OzbkwFGAR9bk6Cu0HS27W6WkrxWD06hSy5OKKr2brWvssFwoi63wnlcmc9Q7-Z5pd5khw8KP2dbNbXdHN4YoGV28VsLVawrDpZmYA_zG7TSQHHuufdQsjxAbrKB17M4LAIv4-T9_mk10a5aZhmOzcAC7U3_bvWBSDGZnvEFaRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با عبور از ۵ میلیون و ۴۰۰ هزار واحد به قلهٔ تاریخی جدیدی رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۰ هزار واحدی به ۵ میلیون و ۴۰۸ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/678621" target="_blank">📅 12:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvo4hbk_TPuo07e4bwZBL8eKLBpfZYiDueb4IwIi6AgaAcifC1yc4TUJQDgrzMBQlKXsLJw0kSJoGvbolb9jpzbtoTYbvqcmbSmkuiOeqs1R2Du1v_wzctzi2jWcV_y2RYrArYEnuzApDYwA9F8YuGDsudSBu-35u8dw4v9QEP-n1I9lQnB4REqmL_DclhEYKesTPJTgc3qC8boS0-S8RRk7OZHQ5yhsDfOUCJ8carabf1giR9qQ9g3ZE7tRIbbWyOugHbTNm4499MVdt1IddIS6L_KK8HC5YUOePNjIUbxOLJ94Vfgc2SUILY-L-twFPccHGra3SY6kEh86jnQoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقرار موشک‌های کره شمالی در روسیه
رویترز به نقل از اطلاعات نظامی اوکراین:
🔹
کره شمالی در حال استقرار یک واحد موشکی در غرب روسیه است و قصد دارد ۱۲۰ موشک بالستیک و ۶ پرتابگر در اختیار روسیه قرار دهد؛ ادعایی که در صورت تأیید، نشانه گسترش همکاری نظامی دو کشور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/678620" target="_blank">📅 12:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHWkR9jIcS2EhD19DFIYtXhPFVZmvUQH81Kh6T9Uxn7rSG0x7KeOEPjwFi_dOL7RVfslpn8PDxU5UCsITI0QNmxeOdlGPDa_OBcsmR_6Xbd9Gg9MLBonVs6DoeJtAKwoRhKdoaKWTE6ES73DgRAkV3UUqYAscBYSvIofeda_obyGMNQlv3g1o7zYeFvbGDIaYIGQibqnzdlBr6N1s8VPXH6JvGBTK0qfDEJjNFM_0OCsp22D558wcfX_vDjAoQ8wWOfmNGccvC98OIi40c3LzXuljuBIna_10pzWJVVHFGjFxLfAriERX7QD0PIYXv2SiQxTFqrqoS-apEHkkFICXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آدیداس از کالکشن مخصوص حیوانات خانگی رونمایی کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/678619" target="_blank">📅 12:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678618">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کالابرگ سه گروه فردا شارژ می‌شود
🔹
کالابرگ سرپرستان خانوارهایی که رقم انتهایی کد ملی آنها صفر تا دو است، فردا ۱۵ مردادماه شارژ می‌شود.
🔹
کالابرگ سرپرستان خانوارهایی که رقم پایانی کد ملی آنها سه تا شش است در ۲۰ مرداد شارژ می‌شود.
🔹
کدهای ملی هفت تا ۹ نیز در…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/678618" target="_blank">📅 12:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678617">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/832b1431db.mp4?token=ZkVbO6_EA6C4HSbTrOmaaE9m2RkFqWhwPf2wBH9Wn4_FNxesEmyaITf2TWPj2835CXuMJanaMCPorRBp6x3FwsRp2uPJOsfjA4MjSKMk36SquzruVE_Jrvf-qhi_kPWlQkoOFKkWsRn4WXTBUoQhUcsxPS8aw1r6yvYMnScZrk7ubtdOeol8sEmwta_NrfVl6V0uecnLTvDhLNyZKz74ca3-077HbOH3ED5KbbfynY-PXUrp961KIJxflhyWbSK4Fkqio6DgtjRfjuQsl9V-lzTqunDGP1BUgWLvFFYt8x58S56gtQzsuj74S58etCBdd3Kxwwdk6asqMRDDzzQ7Dpl1YzyidlD1tCdk-e8xozJ1AwA7Eg3c4xDBGGRhfFPKR_IFTlI-RgiNdnTy8HNIbxKzDQIDUynVHFts4KnxDGb2IDTPTwu6s8jfcdFhjuv66xq7pP7SjDC6zzDpJb2z2IiRCvQByXnTJ1vUZKeT2hG0nbmqCxH3CTEAgI4IfUFTeUWzoDQT6XOi-aoM2EpbiWaxDByw5OQqyBRcGT9g3eE1KvnQiL1N8Nl44MmJ0qpxIZMlOiC15W-sxaN8C1B9ZYQgEcIOHnd4pbxZdAjd-5suNvxtda1I055vZTdb5FM4Wg9yusVk5sbkIrUWATMTVrlxvwsdOEtepOSfMkQjEUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/832b1431db.mp4?token=ZkVbO6_EA6C4HSbTrOmaaE9m2RkFqWhwPf2wBH9Wn4_FNxesEmyaITf2TWPj2835CXuMJanaMCPorRBp6x3FwsRp2uPJOsfjA4MjSKMk36SquzruVE_Jrvf-qhi_kPWlQkoOFKkWsRn4WXTBUoQhUcsxPS8aw1r6yvYMnScZrk7ubtdOeol8sEmwta_NrfVl6V0uecnLTvDhLNyZKz74ca3-077HbOH3ED5KbbfynY-PXUrp961KIJxflhyWbSK4Fkqio6DgtjRfjuQsl9V-lzTqunDGP1BUgWLvFFYt8x58S56gtQzsuj74S58etCBdd3Kxwwdk6asqMRDDzzQ7Dpl1YzyidlD1tCdk-e8xozJ1AwA7Eg3c4xDBGGRhfFPKR_IFTlI-RgiNdnTy8HNIbxKzDQIDUynVHFts4KnxDGb2IDTPTwu6s8jfcdFhjuv66xq7pP7SjDC6zzDpJb2z2IiRCvQByXnTJ1vUZKeT2hG0nbmqCxH3CTEAgI4IfUFTeUWzoDQT6XOi-aoM2EpbiWaxDByw5OQqyBRcGT9g3eE1KvnQiL1N8Nl44MmJ0qpxIZMlOiC15W-sxaN8C1B9ZYQgEcIOHnd4pbxZdAjd-5suNvxtda1I055vZTdb5FM4Wg9yusVk5sbkIrUWATMTVrlxvwsdOEtepOSfMkQjEUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران را تست نکنید! جاده‌ی خشم ایران!
IRAN: FURY ROAD!!
🔹
اثری جذاب با حضور بازیگرانی مثل جولانی، حکام عرب، مکرون، زلنسکی، نتانیاهو و ترامپ!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/678617" target="_blank">📅 12:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678616">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f90ed60dd.mp4?token=jJqWqj38LF3SXPBk8mWufV5G1jfdQguiBsrocx-6y1MBbGT6u_U8nTBwB11ggiYlIuG0QkkHOZCNLuOuFXN02-mq9AmLXs_0AAc0YJ2WwJk0qO7MIs44jTOnbf8mUZ2j-mH67lpF93WaEHEfZWtiJyYm1yfukytbH7vgrr2dhbVfYYBhASfMAz9FNktvB9JSncuT5HO7FtN2iTHfCYSTVddofY18Wbft_GSllCWWHZrtj0CEyPEzxSIqg4ruIxJJ6wtZ1GLRlCHhacxxbBmxkKmmc_WGwonD7SwlYid4J2uvsI0ALuEzpLACFKWAG131VDCW7ylD6DLZ8FzzP-MpTCek9aKUyRONFgzzR1NpfqBijU5VM5kwL8sxLpEQS0umcfZBAk6t8ehsg6pHIfDp4ifop7FLl0whPNzgZ1us-i_6wkr6v36imY2kiyNf9JohBgDre7J7n74sTl0dpQ-Z65lGNCOMqLhmPVRPnkfV943yNghubUASsK-9K0SYimqwbwGtnqHrKXgRWnghBsOzGPufJ_03tRWzhbvrgqKw5WTfdQB98aL9IfRRo0UzHDbKyaeuhS-qN3Ai9brbG_CymUttj9QZzwGFLDuRKASInL2UfcKXPVOPn9HRhQ177h9s6gyyqwe2VOks-wglzHzu7S_36GiEa4IU2VxUXTsjX3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f90ed60dd.mp4?token=jJqWqj38LF3SXPBk8mWufV5G1jfdQguiBsrocx-6y1MBbGT6u_U8nTBwB11ggiYlIuG0QkkHOZCNLuOuFXN02-mq9AmLXs_0AAc0YJ2WwJk0qO7MIs44jTOnbf8mUZ2j-mH67lpF93WaEHEfZWtiJyYm1yfukytbH7vgrr2dhbVfYYBhASfMAz9FNktvB9JSncuT5HO7FtN2iTHfCYSTVddofY18Wbft_GSllCWWHZrtj0CEyPEzxSIqg4ruIxJJ6wtZ1GLRlCHhacxxbBmxkKmmc_WGwonD7SwlYid4J2uvsI0ALuEzpLACFKWAG131VDCW7ylD6DLZ8FzzP-MpTCek9aKUyRONFgzzR1NpfqBijU5VM5kwL8sxLpEQS0umcfZBAk6t8ehsg6pHIfDp4ifop7FLl0whPNzgZ1us-i_6wkr6v36imY2kiyNf9JohBgDre7J7n74sTl0dpQ-Z65lGNCOMqLhmPVRPnkfV943yNghubUASsK-9K0SYimqwbwGtnqHrKXgRWnghBsOzGPufJ_03tRWzhbvrgqKw5WTfdQB98aL9IfRRo0UzHDbKyaeuhS-qN3Ai9brbG_CymUttj9QZzwGFLDuRKASInL2UfcKXPVOPn9HRhQ177h9s6gyyqwe2VOks-wglzHzu7S_36GiEa4IU2VxUXTsjX3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استخوان‌گیری ماهی واقعاً خودش یه هنر توی آشپزیه
🐟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/678616" target="_blank">📅 12:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678615">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
بگومگوی مجری صداوسیما با ناصر هادیان بر سر مدیریت تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/678615" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705eaa8f9e.mp4?token=E22qm8Vwids8tNgZdu3qoAvulFQEh7CYGVJyKkc4bnSEaLY-AS3TUX0EBWn9Y6d7OccZWgFUocQT3aqIgsfGiR91E9k02enmOTNJA1qT_hhrHxq4gMfA0K1eDxStpw1bX9S7E0pLxOojod4FdIOjEdooPNeWRv3Cdsjw-y9PIcd635lOzjiCWMP1y4Ly9owodNeIXRgERzMewXzS3inm6ratTUV743tsMJpA407HmYa7tGN2JjJquzv3PTXE-eOkuUIV0DIfGMeuEI8CTDA6SiykG-li_kez98Oc9KJEnOIWPBieScH8p1yi3U0aWi9xKJeRw3fDbyQX8j0DhLJLOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705eaa8f9e.mp4?token=E22qm8Vwids8tNgZdu3qoAvulFQEh7CYGVJyKkc4bnSEaLY-AS3TUX0EBWn9Y6d7OccZWgFUocQT3aqIgsfGiR91E9k02enmOTNJA1qT_hhrHxq4gMfA0K1eDxStpw1bX9S7E0pLxOojod4FdIOjEdooPNeWRv3Cdsjw-y9PIcd635lOzjiCWMP1y4Ly9owodNeIXRgERzMewXzS3inm6ratTUV743tsMJpA407HmYa7tGN2JjJquzv3PTXE-eOkuUIV0DIfGMeuEI8CTDA6SiykG-li_kez98Oc9KJEnOIWPBieScH8p1yi3U0aWi9xKJeRw3fDbyQX8j0DhLJLOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۶ سالگی و تیغ جراحی
🔹
دخترهای زیر ۱۶ سال هنوز در سن رشدند؛ چرا باید از همین حالا دنبال عمل زیبایی باشند؟
🔹
فضای مجازی به آنها می‌گوید زیبا نیستند در نتیجه از سن ۱۶ سالگی سر از اتاق عمل در می‌آورند تا بینی گوشتی را تبدیل به بینی خوش فرم کنند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/678614" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4mCr_9QjtJogMpW9iZiuEqORMToAxIwbH56tYyeBkFz7FOsBuflr8lReJoYFJb_0fnCRXU--doQoYsJ8v61CRb9bOPRbyU6FQZdntuiU_KlGsTqBWiGVtZbzBGDC7o9XhRPM6yQoF9T1xSCmA36X1nwckjsx3NMryP02vSKh2VeE-MeIq-j-GuR3AMkOYl2hEPdG2a8viArtXclWOb_pkuXzTwIO5R-10DQ0rYFWiU9rU2chkqKXwBAxeAUbhOM1ZnNy49WWC0chB8FLy7XZhL3c9R9nuQjObYlUG92rrhIdM2FW21KQxlX6IGqbK0A40KzV2f0Zs9U5PTfC5ZD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام باشگاه استقلال، رامین رضاییان از این تیم جدا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/678612" target="_blank">📅 12:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678610">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنمابان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11fc209778.mp4?token=et8ICuzhnR3Vyf2wxATAaYh_UfC9aYBv1_RBk9MDooV5JpzY3bj4aJbol5hItYdZGqYDvdk5xwn7ZYmG43TDMy-35cz_ZdK_db2Rw854Esc0MeIFZvgl7HhjCVpQ1XU2NKDfGF19aItX2-fYW9w1r59y8ly0f4zVXRCEjg3N4PZS0hSK9861uTKUMCL9XX8s9lEVfXUtMh7oJ-ngDC6mTqGIUSUMMWz-ZdNwYjsKz0dKSCINFERqyir5a99raRKh-qyBmYAlvzKW6iTANN9wb5zfQh7a-LS-YYzS7WqxDW8HhO42gsJ8yp59UDCDv-zXzHszkmpHiRuoeGVc0j32eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11fc209778.mp4?token=et8ICuzhnR3Vyf2wxATAaYh_UfC9aYBv1_RBk9MDooV5JpzY3bj4aJbol5hItYdZGqYDvdk5xwn7ZYmG43TDMy-35cz_ZdK_db2Rw854Esc0MeIFZvgl7HhjCVpQ1XU2NKDfGF19aItX2-fYW9w1r59y8ly0f4zVXRCEjg3N4PZS0hSK9861uTKUMCL9XX8s9lEVfXUtMh7oJ-ngDC6mTqGIUSUMMWz-ZdNwYjsKz0dKSCINFERqyir5a99raRKh-qyBmYAlvzKW6iTANN9wb5zfQh7a-LS-YYzS7WqxDW8HhO42gsJ8yp59UDCDv-zXzHszkmpHiRuoeGVc0j32eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
بالاخره اینترنت داخلی و خارجی چطور حساب می‌شه؟
اخیرا درباره کم‌شدن حجم بسته‌های اینترنت کلی سؤال و ابهام مطرح شده اما اصل ماجرا اینه که «حجم مصرف» با «نحوه حساب‌شدن تعرفه» فرق داره.
طبق مصوبات رگولاتوری، اینترنت سایت‌ها و سرویس‌های داخلی با تعرفه ارزون‌تری حساب می‌شه. برای همین، با یه بسته عادی یک‌گیگی همراه اول می‌تونی حدود ۲.۷ گیگ محتوای داخلی مصرف کنی. این عدد برای پیام‌رسان‌های داخلی حتی به حدود ۴ گیگ هم می‌رسه.
پس نه بسته‌ات آب می‌ره و نه حجمش جادویی زیاد می‌شه، فقط اینترنت داخلی و بین‌المللی با تعرفه‌های متفاوت حساب می‌شن. / نمابان
🔹
@namabantv</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/678610" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678609">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwtbs6YWq1FN32MmeiNw2nXvGZFb_RjPyo7EHlJO_gYEmL5PMroujPoemrVhvmiMljVUU68U4mH-OOybdk8v8o2uEwo5FCq--DLN_5mV3DLk13siJY2mJ3tJ6gAAVGCqZlumP3oJ_P5lDcLWyTYQP2nIlliFn4aI9e_nAno4kmj231GShZtiMeCcoVUh6ZQ8FM2JwHQ1NCKatySN0YFZ0ewhAwN3l9_6A4Rb29bE-_cf2Ur3s466o0_FCzWz1zdjn5oTCajV563zy_hPNQCDpH7_DKWwte8PF8tGWmNyZYWIF_NhoUJysVUpuFoP5I6Kv7ynwnsoeR8AdKhlaV-knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
جعبه هدیه صحن نو
ترکیبی از یادگارهای متبرک حرم مطهر امام رضا (ع) که عطر ارادت را به لحظه‌های هدیه‌دادن می‌آورد.
✨
مشخصات محصول:
▫️
نگین؛ از سنگ‌های روضه منوره حرم مطهر امام رضا (ع)
▫️
مُهر؛ ساخته‌شده از سنگ‌ صحن‌های حرم رضوی
▫️
تسبیح سنگ هرکاره؛ یادگاری از سنگ مشهور مشهد
▫️
عطر حرم رضوی؛ با رایحه مورد استفاده در روضه منوره
▫️
جعبه چوبی نفیس؛ مزین به نقش ایوان طلای صحن نو
💰
قیمت اصلی: ۲٬۲۵۰٬۰۰۰ تومان
💰
قیمت ویژه: ۱٬۹۵۰٬۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/678609" target="_blank">📅 12:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8JIQe_6UvCGQuZ3LAgKwjJKvdjaTFTph8UYRktNLKbSKSG651QPp2yj21JnmgA6awVny7L-YKAU8QtMStxNalAsQsi37j1B17g9767Pi0Gpavt0PujZ0emLNRhEAQ8DNDXlrHyxzihrzK-DM02INtoiuWy5-_zUiMkxuffi5Wiq7gu-KATOvn7LJ1GPqzcGQok6GpZcAiVyBX_5YDAm5PTTG8JXVnOjp1GCcWjF9MVpHn25p3B48y_kWjW_HcbR_VFck0sszZO97J1dfWcflxq4XXsHt6hiDa542QXs1GRfjMG_Zz09zh4ujGiz1ZGPDa9qIWGbrdVGmE7zsd_xpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار جمهوری‌خواه آمریکایی: جنگ ایران یک فاجعه راهبردی برای آمریکاست
🔹
اسکات مورفیلد، روزنامه‌نگار آمریکایی، جنگ ایران را یکی از بزرگ‌ترین خطاهای راهبردی تاریخ مدرن آمریکا دانست و تأکید کرد ادامه جنگ تنها شرایط را بدتر می‌کند و هیچ شانسی برای پیروزی وجود ندارد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/678608" target="_blank">📅 12:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD8Uxyy9MijWKOcB7o_py4Fvukcj2A1Yi000ydpHl9VNe3c7MTwFb-7EDpdP8hhqXyeAYFFVvjMsYphfg-SYeSmJzADXgu2KjoKG8jDc5LYrlQHQv38g38KnnagWPjRgEZSlAooT7K4lqtv0fFkfC49pq9dKAGythRM21FnmUq1aw_wbfCDlks2J5cDJTXt5cZhZFyvvT1_rJ4mW1VJUXAYC0zh9PJ3o8cNGoz1PE82qLvXvbFHYBO7Br7glVS04Ce9yqJlPCpcEvnDfgPs1vfnP1sPR8qO7soIhifGowUVzVjYQW4fu5gw2sOKqDUZssCbWJ_y7ZUm0FjpJktHtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینجا ایران؛ مازندران؛ میانکاله
🇮🇷
🔹
ایراندخت غضنفری
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/678607" target="_blank">📅 11:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678606">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: تنگه هرمز ممکن است امروز یا فردا (پنجشنبه) باز شود #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/678606" target="_blank">📅 11:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678605">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WidR0T4UGCA5YnDWP6R2snWGlI02JqnWndPMaxNYHUyRDK75gOMBIoe7ZK4TlCsBZPlnUMEc0dIHk_j7zV8zFeGNahl4PmOeF2k_a-cTMbA0sxCbkuvWRk_W_uU-8OpiLvQZ8MvWY6lBL5ZrvY6el9OeqOghAZ1LshnWyJ3-hwv7pB0KU_MNZEhUxgpvAN4W_3CnA87s-R-SwXaWZfgdbTss-_q470KZ3P8ujuNWJK6Dtxi1DocwYQ3ZPPmBlC9vrzHJEe2RFNMRlDsv2HB1oAU63guqeA7ytXR4dGsr7T9qoolJT1_4OsVu6qVoCXRJjaZg-oxGKfVtq8ArBknb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار رئیس کمیسیون امنیت ملی به آمریکا: به زودی از منطقه اخراج می‌شوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/678605" target="_blank">📅 11:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678603">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
عبور از تنگه هرمز بدون تأیید ایران ممکن نیست
دنی سیترینوویچ، مقام پیشین اطلاعات ارتش اسرائیل:
🔹
ایران کنترل امنیتی تنگه هرمز را در دست دارد و از آن به‌عنوان اهرم سیاسی و اقتصادی استفاده می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/678603" target="_blank">📅 11:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33cacc9554.mp4?token=PvxfRl3q51J8UowRAmg8rm77VOyRtzZeaKk6AWjwN0gsjPylHQvXnmRJS20PpR6pe770cLQn1vhpDwmPn2b5sJHBC-gSJEtAkgrBkaiNPKVipSjasZzBzg5sZijB2KJNIg9Jb_ep63Ouy-xpnH9u6-xxYYF646Kne2aib3fh7MPD8_vp8R6zxabuhxm4ChXwGNTIMNtzwW60zh7o1R2Hp9Go6XX82wueV1el3Xomkk5yfDoxgNIF2roKEZlBq5xqpv7T0QotPzJIUkriCZrWRnTVmICRNCW02-VUIEIHdGb4W4zq6lA85VKoAOAnS39GyR0sX4Am-u7YDgZk2LG2TiCTWPPuZ-7aE9beENgYciOHnmvxMpf6EC1ndIf_T3NQBSudgwzyvXHSUb2SI0vCHsGuNCsxE4fq7q5JaXQSLnqVAf_Y1c4FcpS0uvACWn_lCTCrDh-xMo8trRhcheymJfNDia8QBB6PqWb6Qk4RvbwEcdGJdEv0OwSLIjuff0l1fbrKZaJiPJjycSWS5_B5HGMJZnxBpY6xYm8dQZlKiXdmkdcXXKgQUUZgYIaXSWSCgG5wlH9Yfa4Idx0Lxush2RAc_ycPHNfvW5_yGX3YttD0dceQS1a3uIx-cE6DUnNY9ZWJL2BLWbhAyViPEITu_PYr1FfiQBS56t8LUHDa3nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33cacc9554.mp4?token=PvxfRl3q51J8UowRAmg8rm77VOyRtzZeaKk6AWjwN0gsjPylHQvXnmRJS20PpR6pe770cLQn1vhpDwmPn2b5sJHBC-gSJEtAkgrBkaiNPKVipSjasZzBzg5sZijB2KJNIg9Jb_ep63Ouy-xpnH9u6-xxYYF646Kne2aib3fh7MPD8_vp8R6zxabuhxm4ChXwGNTIMNtzwW60zh7o1R2Hp9Go6XX82wueV1el3Xomkk5yfDoxgNIF2roKEZlBq5xqpv7T0QotPzJIUkriCZrWRnTVmICRNCW02-VUIEIHdGb4W4zq6lA85VKoAOAnS39GyR0sX4Am-u7YDgZk2LG2TiCTWPPuZ-7aE9beENgYciOHnmvxMpf6EC1ndIf_T3NQBSudgwzyvXHSUb2SI0vCHsGuNCsxE4fq7q5JaXQSLnqVAf_Y1c4FcpS0uvACWn_lCTCrDh-xMo8trRhcheymJfNDia8QBB6PqWb6Qk4RvbwEcdGJdEv0OwSLIjuff0l1fbrKZaJiPJjycSWS5_B5HGMJZnxBpY6xYm8dQZlKiXdmkdcXXKgQUUZgYIaXSWSCgG5wlH9Yfa4Idx0Lxush2RAc_ycPHNfvW5_yGX3YttD0dceQS1a3uIx-cE6DUnNY9ZWJL2BLWbhAyViPEITu_PYr1FfiQBS56t8LUHDa3nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات کاشی‌کار؛ آینده ساخت‌وساز
هوشمند
🤖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/678602" target="_blank">📅 11:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
حساب شرکت ملی نفت ایران بسته شد
🔹
بانک صنعت و معدن به‌دلیل بدهی، حساب‌های شرکت ملی نفت را مسدود کرده؛ این در حالی است که مهلت بازپرداخت بدهی‌ها تا پایان سال ۱۴۰۵ تمدید شده است.
🔹
پیش از این وزارت خزانه‌داری آمریکا در قالب تحریم اقدام به محدودیت مالی برای شرکت ملی نفت کرده بود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/678601" target="_blank">📅 11:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678600">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سازمان وظیفه عمومی فراجا: معافیت‌های ۳ فرزندی و ۴ فرزندی تا ۲ سال دیگر تمدید شد
🔹
مشمولان غایب هم می توانند از این طرح استفاده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/678600" target="_blank">📅 11:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPD8VC165T8kC3K0yR7LOlfEHadkjrzGeIch67f5_ffCr08QPzBh8kHnWTPiOpQXC2eO6ogiagI1HDysBz1ftVYBj_lQtOh1dyB3jFDCoiWAnYA4oFMxBrzERSI3S_MPmsepLKdDf2nz8zLAL20RliA6TZbkIlFeqLd0JmtF6dVw5ldUqV6dDoH7dXnhIuXCluL2odckCcl9VwgKyMxNipEo0ggFYEGaxyauXrrvSqnSNjAGXKfnSPBO7ycVL5GQkXkccVH_PefEwn1-8XyFpgBDp5LN6-eOiS29YyQ3mCGX-YvkIRCevA6AC-l3YqfxB9ATXQEzPs5_5OJYwle9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی پاییز پربارش برای ایران
🔹
مدل‌های پیش‌بینی هواشناسی، پاییزی پربارش برای ایران پیش‌بینی کرده‌اند؛ اوج بارش‌ها نیز در اکتبر (۱۰ مهر تا ۱۰ آبان) خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/678599" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678598">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
ترامپ ترور شد!
👇
khabarfoori.com/fa/tiny/news-3235561
🔹
اخبار لحظه‌ای از مذاکرات تنگه هرمز | توافق امروز اعلام می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3235587
🔹
قبض آب و برق ۴ برابر شد!
👇
khabarfoori.com/fa/tiny/news-3235621
🔹
پدیده ازدواج بدون رابطه جنسی چیست؟
👇
khabarfoori.com/fa/tiny/news-3235475
🔹
فرزندان خواننده مشهور برای وداع به بیمارستان رفتند
👇
khabarfoori.com/fa/tiny/news-3235480
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/678598" target="_blank">📅 11:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678597">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guf16yP1Y-QZgJz2Xbjz3BTMMv57EJDjYURuRGXD6lD8nwvmqdUcqucSo-ede4PknXDZgRCs_QsCsrkJ591AyXrudvqcSeCH8-NKac7JEswdLJkWpaNOhKqHMQlB6OrXAoyjWjuqaOgwbgnShEFdPiJO0LSA6Hewl7NGPiimjLpiym-QpqlrZXSdyWT0DZ_aokL6FWQNR_6NhSL0f-59Xu8-re6-mx8xgIaQjI6vrkF_ALYQ7tpaRnuVFCgGM3BMmI7WaBsgSSe3FulNP8jHW4nMZ1ypw8YT-HwyQW4YyV-agm8Hp8ZK67U0IUAbQKGTvl-pMA2uuZ4tt1TSPbqIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت عجیب انگشت دیدا، دروازه‌بان سابق میلان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/678597" target="_blank">📅 11:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678596">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
شهباز شریف برای دیدار با بن‌سلمان به عربستان می‌رود
🔹
به گزارش رسانه‌های پاکستانی، نخست‌وزیر این کشور شهباز شریف برای انجام گفت‌وگوهای سطح‌بالا با مقام‌های ارشد سعودی، این هفته در سفری دو روزه، راهی عربستان می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/678596" target="_blank">📅 11:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6c6b9445.mp4?token=hBT8qRGNX10y0nhqPBKgm2n0uJqeFtCzcnw8AY9QRA9HjY9SdhAeTrEHERVfq3sVDuvWshzR7-Ya4CMhjqCp1wY711PQ-h0hO87h5qfww_g3mXvFS8ETkuYUNoI7NAjerxG0loh3HXPGIfDA_HPKT7r4cq66yhScdwItsutIym3u3KMt3jG8zNv-_Nbksnx8rOCSIdw4uysoQRQA2DmxleVaLV2JlMwaevUuFTc2je_9_Z7DJXVxEn3Xwp0_4fxkZleHQO9aGkbuDunpu-QK1UKjNp4ZF7Y9-yP8UNW0crwdb23Q_umy9m7wxBal6CheIiFVBlBmrJIR2LRQmyYO0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6c6b9445.mp4?token=hBT8qRGNX10y0nhqPBKgm2n0uJqeFtCzcnw8AY9QRA9HjY9SdhAeTrEHERVfq3sVDuvWshzR7-Ya4CMhjqCp1wY711PQ-h0hO87h5qfww_g3mXvFS8ETkuYUNoI7NAjerxG0loh3HXPGIfDA_HPKT7r4cq66yhScdwItsutIym3u3KMt3jG8zNv-_Nbksnx8rOCSIdw4uysoQRQA2DmxleVaLV2JlMwaevUuFTc2je_9_Z7DJXVxEn3Xwp0_4fxkZleHQO9aGkbuDunpu-QK1UKjNp4ZF7Y9-yP8UNW0crwdb23Q_umy9m7wxBal6CheIiFVBlBmrJIR2LRQmyYO0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار اروپایی: آنچه در کربلا می‌بینیم، میلیون‌ها نفرند که خواهان انتقام هستند؛ انتقام برای رهبر عالی‌مقامشان و کودکان میناب با کشتن ترامپ
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/678595" target="_blank">📅 11:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678594">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: تنگه هرمز ممکن است امروز یا فردا (پنجشنبه) باز شود
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/678594" target="_blank">📅 11:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678592">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM71rfUbHDPB9HpgOXX34VPgYIdif2AThU9ZJjWvN7TUfQzCv5W3mPvypopSLCTckGYCGcwEqTd9lPEeN3mRD3Ewq8RfqvJjTQKW0We1gVs9xLRV0UyPTyQG3khPC33ZgzurDjLxy6I41e1QRL_eCC3A8Uo_CmZzouON3NiCIgvH6FKRywYomzDG0Cp836nsKyunTpNT1GEraKZEJxKktVU2NgVOmklh3feo0fXLUh8ntl_BQbjJivZykfb2DLfQfzyN7WrohxksOgzQPrpDA-uoMaNMEf5sO7CdeCFqGJVQLXfoPFhHWn8EtRHLsflfSX9jJnGoEWxbSs2QgeJNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر ارشاد: مسئولین سرچشمه ترویج اکاذیب را خشک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/678592" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678591">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eicbRGwhmZhi9Cu7Gu3dAHQuhrGK16asYyTuOUl2zL6nMP93VuE-kUqs-b4NMJHvrXg3xqGF5wVq_1-I2jTYVvY2uC83FDVlQWUpawqfAhCzPHv73Aribg5FLQ-sAhzoPZ1bxvvWjuUJ7auOyfIvhjRWlXZV4KIWX5QO1QNOvQetER3RJ14HN7pqe6x5PKNtesFOSv00C_ADwIo_6ZqQPst49r64UFVZoPKQ1xj3w8pbHaHFSVJ_ho1O4rzYdksxLNFGMqvDKzcdDMhmcPb_os-Zknsl9ksBdSyOp8zNdVHxRheNOQBvj0zr4FvvZul_Ae3hcxegrYtwseSRHjIP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يك كليک تا خرید اسپورتیج
طرح فروش فوری کیا اسپورتیج 2025 کوشا خودرو
✅
قیمت قطعی
⚡
تحویل حداکثر 20 روزه
ثبت‌نام و پرداخت وجه به‌صورت آنلاین از طریق سامانه فروش کوشا خودرو انجام می‌شود:
🔗
سامانه فروش:
sale.kooshakhodro.com
📄
دانلود بخشنامه فروش
⏳
ظرفیت محدود</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/678591" target="_blank">📅 11:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678590">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpd5QmGyDyvM-lXY1MW9jAZX-SZFklzl_bo_KBaFLF_trmH0OpHWMU3onzphHLyF9l47UTGUO4ubHo5GKhQro3g7lGRPDLZuKuWBdYY8kHKm3uazh0AM4QNFx8-LlyjoIw8-TjjjmIhA-ZnPgf7HnXNxn8V39u3mVLMkPi6o1bE6E4Dy-0HXA-Y2bJeGW6nNX_6qfppzqPbXN8V0d0n6b-IMuCE9aDeQdBuiE1U21cbUhv_zu7EHBQLmBdpvVUoH5ZmifgSdsMNMXQbdmmByVyhJ331IcYnRGuZP7z7s41VFgfQn9pz8XxTGl1CxPEfzz70dQNiubDLdoaJr7Ks6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار رسمی زائران اربعین اعلام شد
🔹
آستان مقدس حضرت عباس(ع) شمار زائران اربعین امسال را بر اساس شمارش الکترونیکی، ۱۹ میلیون و ۹۹۹ هزار و ۸۷۰ نفر اعلام کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/678590" target="_blank">📅 11:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678589">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای
کانال ۱۲ اسرائیل: تل‌آویو اطلاعات مستقیمی از مذاکرات ایران و آمریکا ندارد
🔹
تل‌آویو اطلاعات مذاکرات را بیشتر غیرمستقیم دریافت می‌کند و معتقد است ترامپ و مشاورانش به‌دنبال توافق با ایران هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/678589" target="_blank">📅 11:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678588">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای العربیه: هیچ مذاکره‌ای در هیچ سطحی بین عربستان و انصار الله یمن انجام نشده است.
🔹
آتش‌سوزی پارک ملی بمو استان فارس پس از ساعت‌ها عملیات مهار شد.
🔹
انهدام مهمات عمل‌نکرده در پاکدشت تا ساعت ۱۶ امروز انجام می‌شود و جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/678588" target="_blank">📅 10:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678587">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تکذیب دستگیری تروریست‌ها در مرز مهران
🔹
معاون امنیتی استاندار ایلام خبر دستگیری تروریست‌های بمب‌گذار در مرز مهران را کذب اعلام کرد و گفت امنیت در تمام مرزها و مسیرهای استان برقرار است.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/678587" target="_blank">📅 10:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678586">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82cdb975d.mp4?token=LBjNbzKa0ux8JyIXqRPR_owtTVBYvSkEc3TB9M0b2PRZdYWplLm1vkCbTp_CCKg7Dgk89phHacalVfb_EwCmEK2lrXppaL3YT6Zh94Tle5t5cx0-qEUJHr3RUSXdVOJasiX3cROhM3LuQS7MnIgA8oLRKFTRaRi2dg8XsU4bzRgDLGTXbDeJ7WVj2HZ9076_XKLwc9k8IXgSOcK0bFh8wC7so2ZhLgs4UrcIkoTFttydpsIU8KWx6XGa4RabmtM5ZIaQJwwe5mFcUJQoFm8Htfe20G7FzlWH-8oWt9P1hDbgGs956euKVDkPOIRGRf9b6ofX_Xqm06n5jTgyVMhXe4RGTwAZWQ-9wRdToGrgYjFILckMHaF3x-S-PpMIE5mSE5Apy2O9q_AshNz96eOLoN_l9NlPr2AbfYnxuuGp26Xt2sGndjUYVh2ypqpn1zsg5jZRNlU9nPURSnkzhlVhtiwBfP8OHDu_IKjLrcx85l7m8sUVqcbNBMrFypzL15G6eItzNG06IjThBddF1ZddHqC-2qGvKozommv1PkUT8Y6AjZ-uMU_Gip_PVkVFiEZoXDz1yERx3ogpdjdJ6T5ock9nk6GrRLNcIMI4ZYzVXPiSXnai5OHIpHghYFsCR89zaBEzALpMiFMi83weXx9VZp0b0jp5gwWoO_eeco2qx8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82cdb975d.mp4?token=LBjNbzKa0ux8JyIXqRPR_owtTVBYvSkEc3TB9M0b2PRZdYWplLm1vkCbTp_CCKg7Dgk89phHacalVfb_EwCmEK2lrXppaL3YT6Zh94Tle5t5cx0-qEUJHr3RUSXdVOJasiX3cROhM3LuQS7MnIgA8oLRKFTRaRi2dg8XsU4bzRgDLGTXbDeJ7WVj2HZ9076_XKLwc9k8IXgSOcK0bFh8wC7so2ZhLgs4UrcIkoTFttydpsIU8KWx6XGa4RabmtM5ZIaQJwwe5mFcUJQoFm8Htfe20G7FzlWH-8oWt9P1hDbgGs956euKVDkPOIRGRf9b6ofX_Xqm06n5jTgyVMhXe4RGTwAZWQ-9wRdToGrgYjFILckMHaF3x-S-PpMIE5mSE5Apy2O9q_AshNz96eOLoN_l9NlPr2AbfYnxuuGp26Xt2sGndjUYVh2ypqpn1zsg5jZRNlU9nPURSnkzhlVhtiwBfP8OHDu_IKjLrcx85l7m8sUVqcbNBMrFypzL15G6eItzNG06IjThBddF1ZddHqC-2qGvKozommv1PkUT8Y6AjZ-uMU_Gip_PVkVFiEZoXDz1yERx3ogpdjdJ6T5ock9nk6GrRLNcIMI4ZYzVXPiSXnai5OHIpHghYFsCR89zaBEzALpMiFMi83weXx9VZp0b0jp5gwWoO_eeco2qx8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا اتصال سبزوار به شبکه راه‌آهن سراسری محور سبزوار خوشاب از اهمیت ویژه برخوردار است؟
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/678586" target="_blank">📅 10:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678585">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
یمن: یک نفتکش سعودی در دریای سرخ هدف قرار گرفت
سخنگوی نیروهای مسلح یمن:
🔹
نفتکش سعودی «وفا» در نزدیکی ینبع با موشک‌های بالستیک هدف قرار دادیم؛ تاکنون ۸ نفتکش هدف قرار گرفته و تردد ۲۹ نفتکش سعودی متوقف شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/678585" target="_blank">📅 10:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678584">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e6f734c9.mp4?token=NEaxZty7DrquUQRFsA1sXHfaEORF5Y-SdifXELejnpQQYjyYmediM0LRUoHPEyYv_c5C8Qj0gPqmGLlEVa8sHs03bzGvRRq4Mv2POVZd5U9dVzyjwibc1VhyB1MRl9B5B7WvXijPA7L0saKxpuCEkKcUT2HS_NNPv-8zZsM2Q7sAc0Bj_KpObSfzDY_fjHT4p2Y8Vhqeu-ZheNYSlykMaM-7un494iQVYEAiGadoqPvyHj6f1J4iXz1wlzD3kO11T44U_Hr9Ugk0HB-v-igUZik8nobzwJb7UZEDtP3UyE5EwoU-vnoH70A-V-GxmL-MCuS4dj4bK9Yoqadfe5Z8vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e6f734c9.mp4?token=NEaxZty7DrquUQRFsA1sXHfaEORF5Y-SdifXELejnpQQYjyYmediM0LRUoHPEyYv_c5C8Qj0gPqmGLlEVa8sHs03bzGvRRq4Mv2POVZd5U9dVzyjwibc1VhyB1MRl9B5B7WvXijPA7L0saKxpuCEkKcUT2HS_NNPv-8zZsM2Q7sAc0Bj_KpObSfzDY_fjHT4p2Y8Vhqeu-ZheNYSlykMaM-7un494iQVYEAiGadoqPvyHj6f1J4iXz1wlzD3kO11T44U_Hr9Ugk0HB-v-igUZik8nobzwJb7UZEDtP3UyE5EwoU-vnoH70A-V-GxmL-MCuS4dj4bK9Yoqadfe5Z8vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهارت عجیب و شگفت‌انگیز این آقا در استفاده از چاقو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/678584" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678583">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4511285b47.mp4?token=De4gRkSxJHKM3b_5EenkAZm6h8j5ffTDD7tJtGVRatCzSyhFK0dq45jf-mxrisltZ3DXxGwqaShrfr2E-Hlj53z1r4z2ugCZoKy5roZCW91Av9DTOGXRYhVZJWZo8ctcnWZHHdiDAlcUf5zqVo0jaVMjzrH_0yaYPZxcZB6o_LTtTO0PdVqjiARBy-pcB0ja7jM4bKZ-y0n-pMgppgPaKrc8BWc0xVGXjUH_EFfFdFBD4mtQJkh8-7aC7O_qMYiuvmBknwfDYtncR3UYUQ__WnwOdpsIwIuKDVn81Nh_FEZGys2cIGiUuPVEt55GM-IousBrUK59BpUswxDLqb8mlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4511285b47.mp4?token=De4gRkSxJHKM3b_5EenkAZm6h8j5ffTDD7tJtGVRatCzSyhFK0dq45jf-mxrisltZ3DXxGwqaShrfr2E-Hlj53z1r4z2ugCZoKy5roZCW91Av9DTOGXRYhVZJWZo8ctcnWZHHdiDAlcUf5zqVo0jaVMjzrH_0yaYPZxcZB6o_LTtTO0PdVqjiARBy-pcB0ja7jM4bKZ-y0n-pMgppgPaKrc8BWc0xVGXjUH_EFfFdFBD4mtQJkh8-7aC7O_qMYiuvmBknwfDYtncR3UYUQ__WnwOdpsIwIuKDVn81Nh_FEZGys2cIGiUuPVEt55GM-IousBrUK59BpUswxDLqb8mlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر سابق ایران در ونزوئلا: بعد از ورود آمریکایی‌ها به ونزوئلا، تورم از ۱۰۵ به ۱۳۰ درصد رسید/ از وقتی آمریکایی‌ها به ونزوئلا آمدند، با وجود حدود ۸ میلیارد دلار ارزپاشی، ارزش پول ملی این کشور ۱۰۰ درصد کاهش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/678583" target="_blank">📅 10:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678582">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcSOV3omLOPDibj34azhMktOUgFh2N-u2wPioo6ItZZCCz17ukXT_NxyhfHde3fPNqM2g6XkPfiRJtVmcHKUWRvEbkeCRkISW4htNFkUJJ6SsisSO36p4IEt4J9wHcZzOaW0RBlh8Rj3XJCX2M6JE7D1ramUS8ergbLHPNW3TU2QhbGOzGLRo-nA-Qn1TTZS_QR6g-TTb9j2EqTV3f_1H3wYXlNhO9UMSexLupXl4t5DVdgqakrCWtjgysQbjGNymuEasjXNveCJ9-nsN2YhE0PQ13n51rlJnlejOUau-mwdRpdtHEfyuZRa9VjFXraM_0LWwLBuSotNH6yXGIAyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم ایران مبعوث بودند، مردم جهان اسلام هم مبعوث شدند...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/678582" target="_blank">📅 10:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFz9X9QUlSMDq_1E9eSQxQfeMvsKCCE88cgIF_B5Smesqj4CiSVLTz3elvsreXv2lkMqNXJaM-ssrzrqnFaiRYOcbE2w5OhvQYe0RF1wK5eK1-27ms38O-lPxniLfMTVN0OrpjG7vstB4ur_-r2l1U0FY4qP_yQZYibzu_cHEya4k1JJ2xIIrK8Xv77-wCezD0Q06FwyUR8atY9sFviwD6eoy4dD4-fwhAMPCFBlS1zYCOX6f4rjW_qTTClQXw4-ewMwlwoiSMz3bMpYgXTKWfJeZ05AFuS93cB2734CfCPm-ZHFGgz6iztMgAttmOPKpjjQwgvRXDo5txxtDmThOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این پنینی انگار از خود رستوران‌های ایتالیا اومده
🇮🇹
مواد لازم:
🔹
گوشت گریل‌ شده
🔹
نان سیاباتا یا باگت
🔹
پنیر موتزارلا و چدار
🔹
گوجه و فلفل دلمه
🔹
مایونز یا کچاپ
🔹
قارچ و خردل
🔹
ژامبون  #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/678580" target="_blank">📅 10:03 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
