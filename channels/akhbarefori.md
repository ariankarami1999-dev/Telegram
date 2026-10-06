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
<img src="https://cdn4.telesco.pe/file/vITvtJNjeu5ybJ6rs3XbSiJr_G3Hon71mB-ORM5q3qRNzWsh_tOBw8B9k0SoZf4n-uq9hFVu4csO6JV2-3eiabOVwNxx5EH426FdDvx4FgCsSf8W_IvQfoK9VG6ds1tA7tEmQL6KnlHnwXGcpVMHC0AYDrupRoCzgVujkDRqiDrT7Jru17v7rpJAbmWLwZjJ0kofDv2ynUO1Xx3P21n9I7Urw-93nEbP8E_sb1GsgVSpAQrbkysjQNxiJT4x1gF4X8c_dGc7L7bxHRpk_Wp0WT6gFZNHuBgW3tB-J4HnyMATbHIo-Im6a7HCwcKZ9ZVItcS17xrc6onUS57fm3Mqmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
<hr>

<div class="tg-post" id="msg-696220">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
عبدالناصر همتی: به بسنت پیام دادم من به راحتی می توانم ۲ میلیارد دلار اسکانس در بازار می دهم. فکر نکنید با توییت می توانید اقتصاد ما را بهم بریزید
🔹
بسنت اعلام کرد تا دو هفته دیگر ایران فروپاشی اقتصادی می شود. ده روز از این دو هفته گذشت و اتفاقی نیافتاد.…</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/akhbarefori/696220" target="_blank">📅 22:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696219">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
رئیس بانک مرکز: من گفتم میلیارد ها دلار خریدیم و دپو کردیم حالا فکر کرده اند ما رفتیم از فردوسی دلار خریدیم؛ منظور من چیز دیگری بود
🔹
به مقام معظم رهبری هم پیام دادم خیالش از بابت تامین ارز کالاهای اساسی راحت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/696219" target="_blank">📅 22:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696218">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
رئیس بانک مرکز: من گفتم میلیارد ها دلار خریدیم و دپو کردیم حالا فکر کرده اند ما رفتیم از فردوسی دلار خریدیم؛ منظور من چیز دیگری بود
🔹
به مقام معظم رهبری هم پیام دادم خیالش از بابت تامین ارز کالاهای اساسی راحت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/696218" target="_blank">📅 22:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696216">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb-vSzpD6uhnG2Mq1-ntpe6XRTLvKEgGz59Hw7WtIzSddNyBmAvTfD9qFVVKW8TpSc63YgBqz3jpB8IhHzcTG43l1b2K0wp7ZNmjokD1giXDnPJ-f6XifMwxT1EjyhyTmwQsbfsM-bnl-b7hHV8vpUNSJvDpRk-abhZUNhzG3gbhMr8aLDL5W771Q3GQxC4rM0raGsjV-BVU3bTYWgJQeEqQyqUs-BWy5myy6EmhZHswYOxzj0Ld3SkDvimC6sVynOUSA_m9Z7DZprUaWZlgkm9c6Ae0xG2tdgFEjZ6iQlvE6pwiDPZXYlh1lvaAEQ6uMTalssKJEY-8rMlQvNbl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست وزرای مستعفی در ادوار مختلف دولت‌ها
🔹
از دولت بنی‌صدر تا دولت پزشکیان؛ کدام وزرا استعفا دادند؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/696216" target="_blank">📅 22:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696214">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jh1KdOJWxI259ZNL7V4kGPQXdEzawSNWcP-NIWTEGihHHLbbQAfZCrvfNmwuKDVTBmj89FhJ9lnoJMcK-1lScLRERdfPJ7B4Ok9ObXMcze315Jln6wp8aIDjW5UAG1adojpFrklf8Ea_YNe36FHzWwT27xe0MYcik3LIzwApfNFGU8Aua63qN3Kyo1TKdnUrOi-yW2zuaDMHucu9ZdJvRxZq_aXzU_19ezDOY6Zxf9tynXFm_0lHDieiQRuwD3Sh5sw8NKSPon5-rcbcPzvuWAPPyA4oTPUUrxs5HO5YEr-YxEopsHIvqk-UiEnkoD6mKu3Opx249t8DieGISBekCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/os2iErzezQnTYFtl4QQU_QrC0zibrn-IkdhdsdekBg-kuMQhXIhcwQ-exCNNtIanz1op4yyKMr07t5kwXmPcmLIk506v1m89Y8ImcUP2DDlIAcvFMC8tARWPdAJkOByG-NBXQNMst3Mo4eRTxeIqEI3yHteHGw94EAcf6ct5rkf4wevnPtNiZwg0IXnX-mrWAd3Tgw6hCTsU0wo55EzCIVlrTeTsITSJaAkfhI8b_PiY4sKDd6f-nFz9yEuz0V-NnBVUcT66Lbvexpt89TKxUY9qIcStQHorgo9V_LC5p0iik6vs3OKxRUqisEEVA9lf0sccIykfXTlCZ3c1OTEewg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدل‌های iPhone 18 Pro پس از یک هفته از خرید، شروع به رنگ‌پریدگی می‌کنند!
🔹
برخی کاربران از تغییر رنگ مدل‌های قرمز و مشکی آیفون ۱۸ پرو، به‌ویژه اطراف دوربین‌ها، خبر داده‌اند؛ مشکلی که یادآور تغییر رنگ مدل نارنجی آیفون ۱۷ پرو است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/696214" target="_blank">📅 22:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696213">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
فاکس نیوز: ناو هواپیمابر «بوش» خاورمیانه را ترک می‌کند و تنها ناو هواپیمابر «جورج واشینگتن» در منطقه خواهد ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/696213" target="_blank">📅 22:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696212">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW_9d9OLlayUM2sSpnuquQs2VFywMZpleVAmMgsFmY1tXUZ7v1BA43_bC5RgSj_f_XpKXh5xLgoCdHvx_D3NPxNdF8yWZzykXs6CuOEckMuLbSmrYJ-LkaL60NN5ArLPv0YcVMxkBucGU3Hm4BgRhCIjuNwUzFb-89qGhsANkd68bX7psZHNfBFcXd_jtLwOCcjv-6DXG75pp1jAh5xvNaqCU-iG_OMncWR09LsYmGbmEBl33MLy5acDBiaE7unK3ggK94Dz0n0wQ0t3XhCzPZl4jznV9KOeZBlgHs3R1Hnpm0Kj1AQeelld6qqamnsSV-_oimqFWkMkXXMjIrX8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام رئیس بانک مرکزی، نرخ رشد نقدینگی نسبت به ماه های قبل، کاهشی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/696212" target="_blank">📅 22:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696211">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
فارس: جنگنده‌های آمریکایی در چند روز گذشته چند بار تا نزدیک مرزهای ایران آمدند مانور انجام دادند و برگشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/696211" target="_blank">📅 22:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696210">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzoMCToS6fxHK30g91lTOGGuBYrMSS1Ujh5s2rBPEhgqKes104RSiXb7UnP-dMT2UzC3OKGUPF2aSDE9Lw-THKr_Wa3O2uPJDxHv0EZGoor3d7HiGK5ns-Zoxgo57IOuvgXvHXAY8LXOAytgBNEKlh3HZEjrNG9sS9of5y0enTO_0Lx2RTQAhrFvK9aekigx4C4lFhTUFHJSOINMucV6NQoE595kZ5cTpWKf343KmyKLsfZEjAtiV4wgarvoNWfoSYR8dqOrvqeq-NrPbHMMCqFHUfoXGBt9ue7z97NlViTH1coSmbuhOXQ1p7mjRyrlEbjb9pG6d88CHs4Al0sVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در واکنش به اظهارات وزیر خزانه‌داری آمریکا، با انتشار یک میم اقتصادی: آماده‌ای تا روح تو را تسخیر کند؟
🔹
در تصویر دیوید زرووس، مشاور ویژه جدید بسنت و حامی کاهش نرخ بهره، دیده می‌شود؛ همان کسی که گفته بود تا فدرال‌رزرو نرخ بهره را پایین نیاورد، موهایش را کوتاه نمی‌کند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/696210" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696209">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26145c3b5.mp4?token=Rwr2NaW9y-nrqwfOsHbmizYqD2jCS5pbNTxuK1Ily_a8cTeSyq7DiRZjjDMlraKEm3D9WsJI0CIyQa219qGe5b2X-Clg3S4pi3CaRbEL87FMyj4o2oaL_G-_eMXSH_Mhm1q-oyq7Och4newk0mbg7OsV-cawHhzHWCkI8w2zodVoQ1u4TqpG-xbelsUTrro8eK_YRIE8oSWJOICc7GET5Pqsa7eHfO5nkGphq_XWrKb4DG6urdXuGOOFJfAFC8bcLpuUqTxrMbQ84PA5d7NjDpN8iDExeuqar0jjUhliUYqfKZXeCnyk73haSVbG5U0wTZ6MRaLjuTKEnrJBlphRwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26145c3b5.mp4?token=Rwr2NaW9y-nrqwfOsHbmizYqD2jCS5pbNTxuK1Ily_a8cTeSyq7DiRZjjDMlraKEm3D9WsJI0CIyQa219qGe5b2X-Clg3S4pi3CaRbEL87FMyj4o2oaL_G-_eMXSH_Mhm1q-oyq7Och4newk0mbg7OsV-cawHhzHWCkI8w2zodVoQ1u4TqpG-xbelsUTrro8eK_YRIE8oSWJOICc7GET5Pqsa7eHfO5nkGphq_XWrKb4DG6urdXuGOOFJfAFC8bcLpuUqTxrMbQ84PA5d7NjDpN8iDExeuqar0jjUhliUYqfKZXeCnyk73haSVbG5U0wTZ6MRaLjuTKEnrJBlphRwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقف مسابقات فوتبال در آرژانتین در دقیقه ۱٠ به احترام مسی  سایت «ESPN»:
🔹
با تصمیم فدراسیون فوتبال این کشور، قرار است تمام بازی‌های فوتبال در این کشور در هفته پیش روی لیگ‌های مختلف مردان و بانوان در دقیقه ۱۰ متوقف شده و به پاس قدردانی از دوران حرفه‌ای مسی…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/696209" target="_blank">📅 22:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696208">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def57d600a.mp4?token=AzcADsbZz-eTEKFrNSxACHH_YTUhf3ktUEN4JcHpqM6SjFmVbbWjkRwUI1CV2KnyZWOaGviSaS4Lf_KlM25z7YhaxCEA3RA_0q_LX2PQKO11Mywq5Sd1Gdyi78YCeZEKfw_06vclo-RzFXksTxRoosHHjvnZhnhHPsdpAd7RNbGwmRGM6mB7fs_NecvAUurE9jFL4wCjwnGEQFln8ZATDxQPl5B8tilYgkN_jp12qpcNqVjDpvv26rdKv4rtBkQ-Yykiw7RjfRX8gvg31ZDCYWnHgZv92BmcJnXVUVaINWjv6m-miHUyh78aignEYhTIJrU8i_2sJP4SXHVp1bse4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def57d600a.mp4?token=AzcADsbZz-eTEKFrNSxACHH_YTUhf3ktUEN4JcHpqM6SjFmVbbWjkRwUI1CV2KnyZWOaGviSaS4Lf_KlM25z7YhaxCEA3RA_0q_LX2PQKO11Mywq5Sd1Gdyi78YCeZEKfw_06vclo-RzFXksTxRoosHHjvnZhnhHPsdpAd7RNbGwmRGM6mB7fs_NecvAUurE9jFL4wCjwnGEQFln8ZATDxQPl5B8tilYgkN_jp12qpcNqVjDpvv26rdKv4rtBkQ-Yykiw7RjfRX8gvg31ZDCYWnHgZv92BmcJnXVUVaINWjv6m-miHUyh78aignEYhTIJrU8i_2sJP4SXHVp1bse4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ اعتراضات در فرانسه را به اسلام نسبت داد  ترامپ در تروث‌سوشال:
🔹
مهاجرت انبوه و از کنترل خارج. این موضوع درباره مدارس نیست، این درباره اسلام است که می‌خواهد کشوری را که زمانی بزرگ بود تصاحب کند!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/696208" target="_blank">📅 22:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696207">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as6g3wWPVG_MJIGmLYxkB6-pU_ABBpm56hHGz0kxgIN3_jKoqoq4qLtP5TW4ZeRWnmmNUhjhqVXlugdQ313FAwABAwh4RYFudo6jIzuQ6nzXjHjRcbL-K4pmg6lg4sq5XvCXgKBvxt7Z3dZLVHxf_E1K-SxEPbyquYnh_GNPBfEWtqAjxQ-_mKhjRRQVACBjHjCEj7NyAPulrFUneM1PG-OsL5EONY5AXPRASN0vO_ss94AmNvFfoABnMK9RRBM3RB6sJZ31um2-V9Qe3REvbkIkhFv0hrzFZzEoevrU1jllxPinsr3xKNCaV8HLHrpqho03XlHcCXWz3CNhOmtZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت دلار فردا افزایشی است یا کاهشی؟
🔹
دلار، طلا، بورس، مسکن و اقتصاد هر روز با یک خبر تکان می‌خورند؛ مهم این است که بفهمی کدام خبر واقعاً مهم است و بعد از آن چه اتفاقی ممکن است برای بازار بیافتد.
🔹
این کانال رو به تیم مدیریت می‌کنه که از اتفاقات بازار زودتر خبر داره و همه چیز میگه
👇
👇
@EconWar
@EconWar
@EconWar</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/696207" target="_blank">📅 21:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696206">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
علیرضا مطلبی: سلیقه گرون داشته باشید سلیقه گرون باعث میشه پول بیشتری در بیارید/کسی که سلیقه گرون داره در خودش یه چیزی میبینه که دنبال بهترین میره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/696206" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696205">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
رئیس اطلاعات نظامی اسرائیل: از ۶۰۰۰ نفوذگر که در ۷ اکتبر از غزه به مرز نفوذ کردند، ارتش دفاعی اسرائیل ۴۰۰۰ نفر را از بین برده است؛ ۲۰۰۰ نفر باقی مانده‌اند و ما به تک‌تک آن‌ها خواهیم رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/696205" target="_blank">📅 21:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696204">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وقتی یک بحث ساده به خونریزی ختم می‌شود!
🔹
هر روز توی شهر شاهد نزاع و درگیری خیابونی هستیم و شاید اگه برای یک لحظه خشم‌مون رو کنترل کنیم، این درگیری‌ها پیش نیاد.
🔹
امروز بین شما مردم اومدیم تا ببینیم چرا انقدر درگیری خیابانی رقم می‌خوره؟
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/696204" target="_blank">📅 21:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696203">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
سپاه در سومین سالگرد عملیات طوفان الاقصی: هرگونه خطای محاسباتی و تجاوز مجدد علیه ایران پاسخی دردناک خواهد داشت، این عملیات هیمنه ارتش تروریستی اسرائیل را فرو ریخت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/696203" target="_blank">📅 21:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696202">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3K2yCv15JvgbAPC3jm25IUttDU4POIeBLhzACnqAjAcklLNmlevyTCb99PfrUyMnjKhVG2B5qUZcfSY_Lk2ps2YhxlBg9kYV4sH0QXEk0rpDuGPKx2pBDW7nyhpvxW4osl20eQx_QVPe7gJf-BRhHC-PjU3bvQWbH7jUPbMjmNKZRvzyp2Bg2aRTtLMpsdNq4O0CzUq6ewFHcFgB-FZXk10idavTdol5RE6-d0byYwqNQPMi7btbjlqRzbOTLCUOnN4mVhlToJnAR3RKJbFoU51brGdvm_BcT5v6J-X3ohyn3GWUadMSQT6aqoi_X0Xkiynw3TZhIMOzP3aui_Beg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور اتوی بخار رو تمیز کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/696202" target="_blank">📅 21:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696201">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU45Pn7646AXqjIvgcnAtatBxPGwpMiFxtmBSsMEIH1v4J9onEAVueXoUTjL5yXbI2PwpJbXfSHzigg-fSyIUmHkLkct8_nQBAK1FXHeePyzXJ0N7q4pbAZKp_vlHAWQ8DKfa-OLAwZMuYk4a2Hfg7YRTMRkMIeHR_EHKG19cTz543o5MYUjmNqNxdxHqG9W39wzTYkgtcyFuZGJaqdfH4RNp8BR5lhCACQC-tkg7P2XNJ27Vl5jAgKjdUx1qkpHqnbIGcvB27jjuXUIIdAtAEspJGI70ptvAlrFKQkaa0eAmhWm4pP9Ct-YXn__xoVKKWUn5tqtKC7VqZIqUgjkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باشگاه نخبگان همراه اول میزبان ستاره‌های علم و ورزش
🔹
همراه اول در قالب برنامه‌های باشگاه نخبگان از جمعی از افتخارآفرینان علمی و ورزشی کشور تقدیر می‌کند.
🔹
اعضای تیم ملی المپیاد نجوم و اخترفیزیک ایران با ۵ مدال طلا و سومین قهرمانی پیاپی جهان، ۳۰ نفر از رتبه‌های برتر و تک‌رقمی کنکور سراسری و مدال‌آوران ایران در بازی‌های آسیایی آیچی–ناگویا ۲۰۲۶ مشمول این طرح هستند.
🔹
هر یک از این نخبگان یک سیم‌کارت دائمی ۰۹۱۲ ، مودم پرسرعت 5G و یک سال اینترنت رایگان دریافت می‌کنند.
🔹
باشگاه نخبگان همراه اول با هدف حمایت از سرمایه‌های انسانی و همراهی با مسیر رشد و موفقیت استعدادهای برتر کشور فعالیت می‌کند.
http://mci.ir/-NYKQCE
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/696201" target="_blank">📅 21:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696200">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadeaf1478.mp4?token=FXxtHc8KKYc9VOxtmEaUJ2BcKKkUDd42X0x_oq44FOk8o9SFgspjJc3jfZTLr_aja96A4Gzhs62wKGaiPDwAjcYQ8_r0K5A6ShVeM9rp0VZ8F2vP0A2gGSAuIOEsyFfcANDL88YjHeiV07caOx3HF2mFIIYkHmJp5WJJrt2UI3DNIgkiSlliZl89_NO0yWdG36tbfdwvGTaLYNk5wmjyUG22JnDwJiQjlynnOGA6C56a8xfg_-H2ngYrD6Tz4g2LPdfawnUNZXKhnj6FHPHpcTud-AviQrMDNWISUG5Ty60G1K984ax4Z9BYphAhdpOz3bAMxDGVFZPDmudzLWeQqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadeaf1478.mp4?token=FXxtHc8KKYc9VOxtmEaUJ2BcKKkUDd42X0x_oq44FOk8o9SFgspjJc3jfZTLr_aja96A4Gzhs62wKGaiPDwAjcYQ8_r0K5A6ShVeM9rp0VZ8F2vP0A2gGSAuIOEsyFfcANDL88YjHeiV07caOx3HF2mFIIYkHmJp5WJJrt2UI3DNIgkiSlliZl89_NO0yWdG36tbfdwvGTaLYNk5wmjyUG22JnDwJiQjlynnOGA6C56a8xfg_-H2ngYrD6Tz4g2LPdfawnUNZXKhnj6FHPHpcTud-AviQrMDNWISUG5Ty60G1K984ax4Z9BYphAhdpOz3bAMxDGVFZPDmudzLWeQqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین زنجیره انسانی «جان‌فدای ایران» در مشهد شکل گرفت/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/696200" target="_blank">📅 21:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696199">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
عمان: یک کشتی در مسندم هدف حمله قرار گرفت/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/696199" target="_blank">📅 21:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696198">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3420338f76.mp4?token=Mv1foUbVoJEoaHba6p1jN8fMtzax82QNv1NIoHHmkwTd-JH7mew07nKfSaL0zCvcuXfLjtsZ1IOxe2q0QgApyUOs6bnUC2PPN8c6TgoAcWhHXOTXcsegVscSPj1btRcjIkR5QfWkEFw_SoDSRkMb7B1c312FLSntTbENkiFfj2dI8Sk2oWgsQrQUk9Ztg1GeuLuxCptHlMI8K9KSewsBgOEFnhdwU4-vsYOn-IWJakJFkqSTHSJDqbELxafMj3ehbYHNwHz5ZNUvcf7ajcVJVgDFZhUq2thZM7d_-tptJ4xhzd5JXzIzjFb_g8LlXHVUGBgAD1VU22EaDuN3RooU6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3420338f76.mp4?token=Mv1foUbVoJEoaHba6p1jN8fMtzax82QNv1NIoHHmkwTd-JH7mew07nKfSaL0zCvcuXfLjtsZ1IOxe2q0QgApyUOs6bnUC2PPN8c6TgoAcWhHXOTXcsegVscSPj1btRcjIkR5QfWkEFw_SoDSRkMb7B1c312FLSntTbENkiFfj2dI8Sk2oWgsQrQUk9Ztg1GeuLuxCptHlMI8K9KSewsBgOEFnhdwU4-vsYOn-IWJakJFkqSTHSJDqbELxafMj3ehbYHNwHz5ZNUvcf7ajcVJVgDFZhUq2thZM7d_-tptJ4xhzd5JXzIzjFb_g8LlXHVUGBgAD1VU22EaDuN3RooU6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا نباید ناخن‌ها را جوید؟
🦠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/696198" target="_blank">📅 21:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696197">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ofw03zqV4yLbNfxi5MIp9rpEZNYazYKRQw_Xe1SftCjBFiAXSwE6N1qdge9Y2luytyaRUrqJX56DL_Sp5FMFRjwgpQKFYkLrfgGJ9hJTEOHGeKy4ehb0X1wN0_HXb9Flq0IveS1Tcq3HYdZtjcywarRFtbbQ293LcRGTe_2jH-emMHxA4e6sje0BzIIkDaWHtv6GJ02O51XdW2b1Jy42T4VmxsrI0tnkatiEJabW20eN1XxLHKJnlJp8NkxtaYUJG9hbhJ_WJwcHGfw8loxd8VKWRJm4BmauMvX6ZLXqZoTpvq2UZft_nwyliDPlQ9aheKkSAvTo-rkfw_8OG_l1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رایتل اعلام ورشکستگی کرد
🔹
این اپراتور با قیمت ۱۳۰ همت به مزایده گذاشته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/696197" target="_blank">📅 21:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696196">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY88vXPIlBYef_FM1Mn-vNqd1axRP-mXULcLPWcBzOnP9_4Ey-hTPZ5AWGFmYi_CeF2bHus_KfqzXHE9w7-DxB8M4RYUWgiZECel33nAycsGZZYmb9zEl61pnW_CfKH6RuF5r9WhaeymlgOoVmp1iRZxOfJyyAfNcdbG8gKQIPvamZY6PgZJRNMhv6U6eqIYhjuLSj9D-CCA1BRZ8wITBBkz9CMupz5ku2ZZBZJNwLmdfvHVUAJ7NUJlyZSpLUx3S97S5os8MSfNVYPcz_y9f1FKTmI2Ec5CWWKythgNZ8fQSMwpgnl5EevRXVa6FY4voXRKfU4zmSymYE0H__mrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شریفی‌الحسینی: تعرفه‌های قدیمی، توسعه شبکه را محدود می‌کنند
🔹
سید محمدعلی شریفی‌الحسینی، رئیس کمیسیون اینترنت نصر کشور، معتقد است ادامه وضعیت فعلی تعرفه‌ها، فاصله میان هزینه‌های شبکه و درآمد اپراتورها را بیشتر کرده و سرمایه‌گذاری در زیرساخت‌های ارتباطی را تحت فشار قرار داده است.
🔹
توسعه 5G، فیبر نوری، دیتاسنترها و شبکه‌های انتقال به سرمایه‌گذاری مداوم نیاز دارد و هزینه این بخش‌ها هم با تورم و نرخ ارز بالا می‌رود. در چنین شرایطی، ثابت ماندن تعرفه‌ها می‌تواند به فرسایش تدریجی شبکه و عقب‌ماندن از فناوری‌های روز منجر شود.
🔹
بحث فقط افزایش قیمت اینترنت نیست. مسئله، ایجاد یک مدل تعرفه‌ای شفاف و قابل پیش‌بینی است که هم قدرت خرید کاربران را در نظر بگیرد و هم امکان ادامه سرمایه‌گذاری اپراتورها را فراهم کند./ عصرایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/696196" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696195">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4857b6b6d1.mp4?token=b_7ShUeeTo3wslVNnR_JvRfS8V103IazayHXt0GZ0IC9fjWKF0NIi9v8t5L1N_ZL86Ihb4k9UAy_LVIJoR4cd-jWxiUNvAz93JeEdq3bch8jDeqoHlPhh0hVoH0JRvyO7CBa43sZCFbJUl7lSr83clIh03TPSMYtm4I9BtcGD6q6A1Qur8HY6BSJOWD6qT6vu5gMYngnp6jnDuzI0azqTH2mSGAb4YxdU_1Uo5PzQuAsiL83Pn0Dz3itguVi14jCGWHvFKKNI4YNFzzi_0YXTTo6Lhugwjn4BZZx_TLllDw0siOYmu6NLGBbCKQZ9NG4FNJs3dRzpUEXNUbTr-G6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4857b6b6d1.mp4?token=b_7ShUeeTo3wslVNnR_JvRfS8V103IazayHXt0GZ0IC9fjWKF0NIi9v8t5L1N_ZL86Ihb4k9UAy_LVIJoR4cd-jWxiUNvAz93JeEdq3bch8jDeqoHlPhh0hVoH0JRvyO7CBa43sZCFbJUl7lSr83clIh03TPSMYtm4I9BtcGD6q6A1Qur8HY6BSJOWD6qT6vu5gMYngnp6jnDuzI0azqTH2mSGAb4YxdU_1Uo5PzQuAsiL83Pn0Dz3itguVi14jCGWHvFKKNI4YNFzzi_0YXTTo6Lhugwjn4BZZx_TLllDw0siOYmu6NLGBbCKQZ9NG4FNJs3dRzpUEXNUbTr-G6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر گوشی‌ات مدل بالا نیست ولی دوست داری عکس‌های باکیفیت بگیری، این ویدئو رو تماشا کن #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/696195" target="_blank">📅 21:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696194">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
عراق از ممنوعیت استفاده از اپلیکیشن مسیریابی ویز Waze از ابتدای سال ۲۰۲۷ خبر داد
🔹
بغداد دلیل آن را ارتباط این اپلیکیشن با رژیم صهیونیستی عنوان کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/696194" target="_blank">📅 21:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696193">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6c09a17c.mp4?token=Wwldph0sCV9yYrjo7LiqtcLPHSvPl0qE-HmBelrukpRPxbSttaLEWRjYNJhyMC_2miZ-pnrBrR2vZd_sS07lJVlLoPTNnrcud5apgjvzufPh1r0rQPYldwPeEX3DjVqgOgDthZAcOzw4OvqPXa5PBONseuCtpefXPvkUu8aRNGqWPXSmSNXprRkfJ-1yOownQ0pP8LWKOa8JMNgHS94vGH9LcdoW2LwlBw6nMuaCn7tsGHtO2l4CwQ-q5HcN6bwGzhjQohplYnMfjRpdmOegKaRxOnwRdhL8mMBM5i-oORScJYwOgpkpsbuJpgQ8tbrpZnUdQAtKYJjomzxQ3NYD9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6c09a17c.mp4?token=Wwldph0sCV9yYrjo7LiqtcLPHSvPl0qE-HmBelrukpRPxbSttaLEWRjYNJhyMC_2miZ-pnrBrR2vZd_sS07lJVlLoPTNnrcud5apgjvzufPh1r0rQPYldwPeEX3DjVqgOgDthZAcOzw4OvqPXa5PBONseuCtpefXPvkUu8aRNGqWPXSmSNXprRkfJ-1yOownQ0pP8LWKOa8JMNgHS94vGH9LcdoW2LwlBw6nMuaCn7tsGHtO2l4CwQ-q5HcN6bwGzhjQohplYnMfjRpdmOegKaRxOnwRdhL8mMBM5i-oORScJYwOgpkpsbuJpgQ8tbrpZnUdQAtKYJjomzxQ3NYD9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای عجیب بازیکن سابق استقلال علیه برانکو: دعوت به تیم‌ملی در زمان برانکو پولی بود!
سعید بیگی، بازیکن سابق استقلال در تلویزیون مدار:
🔹
در دوران هدایت برانکو ایوانکوویچ به تیم ملی دعوت شدم اما برای حضور در تیم از من ۵ میلیون تومان خواسته شد که آن را پرداخت نکردم، بازیکن دیگری آن پول را پرداخت کرد و راهی تیم ملی شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/696193" target="_blank">📅 20:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696192">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار در جزیره قشم از سمت دریا به گوش رسید؛ اصابتی در سطح جزیره گزارش نشده است
🔹
منابع محلی تاکنون جزئیاتی به رسانه‌ها اعلام نکرده‌اند./ ایرنا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/696192" target="_blank">📅 20:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696191">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a00d2411.mp4?token=W892aZwvsVutZTptRXfCoHkgU78LrpX4zQMZVbUns-7EaBryIEOR8Zvq-wgktXJ6fDQ4IeHZmyw0bOI--nTsJ-CVFeEylwflTPVZvkBUu8CIyxSx9fCy3tmE2CV48bbl92HQxsrMAo06oHixVYQlFvqmBxrTflYDcHoQ1V8PdrSW0NIDt_13KBlEgQNPsCJYyxeywh-uV4N5ZCc3xqaelcbqJW-zvZ_4vBlJxaRgY9iUQLvGDOhERQf8HzhFKY6Fg93y26t-n_IG8OfMpvQce1v-x5oBugFgLXRpV_2NSLBWosiJ23DaDQSuO8k_KbgnIYeyjHXZL1J3FkLCqNP39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a00d2411.mp4?token=W892aZwvsVutZTptRXfCoHkgU78LrpX4zQMZVbUns-7EaBryIEOR8Zvq-wgktXJ6fDQ4IeHZmyw0bOI--nTsJ-CVFeEylwflTPVZvkBUu8CIyxSx9fCy3tmE2CV48bbl92HQxsrMAo06oHixVYQlFvqmBxrTflYDcHoQ1V8PdrSW0NIDt_13KBlEgQNPsCJYyxeywh-uV4N5ZCc3xqaelcbqJW-zvZ_4vBlJxaRgY9iUQLvGDOhERQf8HzhFKY6Fg93y26t-n_IG8OfMpvQce1v-x5oBugFgLXRpV_2NSLBWosiJ23DaDQSuO8k_KbgnIYeyjHXZL1J3FkLCqNP39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با سه قلم مواد ساده، عفونت گلو و سرماخوردگی را بطور کامل درمان کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/696191" target="_blank">📅 20:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696190">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5OwKFimjrRQ2EY6erSB_S45LbpHx7tjMMh-3pgy0NqfnuXeY_OeGqRLNlSBTgJLFFNr4Kk4h9W6rGeo3P_mnVxFkUctLlkEJc9xNw60NpnB3EN7VmdJhq9UdmCACt7UwRCJAQJqnPm4mBqCUlI6BMz4uiGva1wlZpuEFzUpPq-FCQ9VxvTaS8QxFPu_MBS2TXuN7CY17Ph-ZuWlCtJFssx41tjC64SZCwB9v5Wo9os69lY9LYb4ujxUOyRrtS2933q9t42uXpf5GK3OnzKIQLNZPN8qQBGcg2_MZiHEK5YYrHJamJEyaKVQZeyJS56hgJG8cnkeK-pw9z3XKapKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
🔻
مشاوره رایگان پزشکی برای متقاضیان کاهش وزن با آمپول‌های لاغری
🔹
با توجه به سیر صعودی مصرف خودسرانه آمپول های لاغری و با همکاری شرکت های دانش بنیان دوراپزشکی ، این امکان فراهم شده تا افرادی که قصد استفاده از آمپول های لاغری را دارند به صورت کاملا رایگان و آنلاین توسط پزشک ویزیت شوند.
🔸
کاربران در این سامانه با تکمیل فرم کوتاه ارزیابی، شرایط خود را از نظر BMI، سوابق بیماری و داروهای مصرفی بررسی کرده و سپس با مشاوره رایگان توسط پزشک از شرایط مصرف آمپول های لاغری با خبر می شوند.
👈
شروع ارزیابی</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/696190" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696189">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuJqgbjAcYdwpyTtlinZE_JqTbd0JD3ZG4qxw1Kntj8UQ-OLqiDgpgTUiFA4uWbQ9kV165lF22YjZyrFbsSUDN9OrRyCERhMd1m_9YCOdwjEHjYIKD9ReA-gltIV0NvHXbF4EhQrRa2JCIyCNKXloHfsjNczUGJYn28GYl-ZHUMjVpk41UmXJ3C5iAOeRqbBN3hpedO0ARlYQ6t8Z8AX0sNHl_zrWXEfILNYymUHJsCeSujInS0du9VcPcqurEUOA_nl-sHcnSbxmbdXt8W1oh4v6x4nC-6O9xF_5WkM_OD4ZTaqPaHdk2OSMOs5ULlwQVkCU1QzY3oHeSBGV0xQGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط تلفن سازمانی ۴ و ۵ رقمی نکسفون
راهکاری برای حرفه‌ای‌تر شدن ارتباط تلفنی کسب‌وکارها هستند:
🔢
شماره‌ای کوتاه و آسان برای به خاطر سپردن
📞
نمایش شماره ۴ یا ۵ رقمی سازمان در تماس‌های ورودی و خروجی
⭐
امکان انتخاب شماره دلخواه از میان شماره‌های قابل ارائه
🏷️
فرصت ویژه مهرماه برای خرید خطوط ۴ و ۵ رقمی نکسفون با تخفیف‌های ویژه
🔎
دریافت مشاوره و درخواست شماره‌ی دلخواه:
https://isp.nexfon.ir/khabarfori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/696189" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696188">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
محکوم به مقاومت هستیم/ هدف نهایی دشمن تجزیه ایران است
عباس گودرزی، سخنگوی هیئت رییسه مجلس:
🔹
جمهوری اسلامی آمادگی برای مواجهه با هر وضعیتی را دارد که در هر سطحی تهدید شویم، در همان سطح پاسخ کوبنده، ویرانگر و فراگیر به دشمن بدهد.
🔹
امروز مقاومت برای ما انتخاب نیست بلکه ضرورتی استراتژیک و راهبردی است؛ محکوم به مقاومت هستیم و دشمن به دنبال تجزیه ایران است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/696188" target="_blank">📅 20:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696187">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2f31cb5.mp4?token=d0Cg3zsXXeeYHRf8FG00iMNCpQEhNtd5-DZykEp5vkk1mXvxvQCAJPHPX6_dHDVYmdKXnCIr6etHtP681Zkye5fue3MEPEO40XE7hFSemNSJmERs9IALGUJOqkKsY7d0esbLxjDLdlE3fIkC9fddWTAisKExNdRZ0l7rYQyd-ZGkNnZNhCoCWFQPfpFi3U589W0pReYgTLuUCDv78WmCNUIHW4vQkB3-to1adMf9xgYQroh-AhgidwIEWZi1NT390cTIvftNHkPKK1-CyyeuNxf_hT6g7qHUF9Nzg5PScbFA2xeoN_7k1kamjJ1Mv2Leuf65z_9INmlwTtfbDc4fXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2f31cb5.mp4?token=d0Cg3zsXXeeYHRf8FG00iMNCpQEhNtd5-DZykEp5vkk1mXvxvQCAJPHPX6_dHDVYmdKXnCIr6etHtP681Zkye5fue3MEPEO40XE7hFSemNSJmERs9IALGUJOqkKsY7d0esbLxjDLdlE3fIkC9fddWTAisKExNdRZ0l7rYQyd-ZGkNnZNhCoCWFQPfpFi3U589W0pReYgTLuUCDv78WmCNUIHW4vQkB3-to1adMf9xgYQroh-AhgidwIEWZi1NT390cTIvftNHkPKK1-CyyeuNxf_hT6g7qHUF9Nzg5PScbFA2xeoN_7k1kamjJ1Mv2Leuf65z_9INmlwTtfbDc4fXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغز هنگام خواب استراحت نمی‌کند؛ بلکه به پاکسازی و تقویت تمرکز و حافظه می‌پردازد/ کم‌خوابی می‌تواند تمرکز، حافظه و اشتها را تحت تأثیر قرار دهد
😴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/696187" target="_blank">📅 20:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696186">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=CNrTl3eUMZ6tR0_29LX4oj4JZ6kKYZmal6yKBCxRYgPOQLaQxzsfhWTVmpjtAr0iEtW7auBiEYmH_C_SF_sqr09wp8ZyXRkD7NwonolWNXh16FGYv8fU9fzugAHij_IlrlG3P49s9l6gNySg8gpNyCF4O7T6mqh_NuHBoSbnUqZSJC1YbEN-68gxHP195vJLEiShy5xRx5tOQkJlxRDnyeM1v3-VEDs-9vW2h7jmprgGChylp_C5cW9hl66f0sFu4hsQUTM9v4y2zdrtdJPSJQADq7mzjjeR24i7YJydm8IWDFQhuYIppdpee2TkTXjVE4AlukkH5LOcVAZxigFSsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8c96111.mp4?token=CNrTl3eUMZ6tR0_29LX4oj4JZ6kKYZmal6yKBCxRYgPOQLaQxzsfhWTVmpjtAr0iEtW7auBiEYmH_C_SF_sqr09wp8ZyXRkD7NwonolWNXh16FGYv8fU9fzugAHij_IlrlG3P49s9l6gNySg8gpNyCF4O7T6mqh_NuHBoSbnUqZSJC1YbEN-68gxHP195vJLEiShy5xRx5tOQkJlxRDnyeM1v3-VEDs-9vW2h7jmprgGChylp_C5cW9hl66f0sFu4hsQUTM9v4y2zdrtdJPSJQADq7mzjjeR24i7YJydm8IWDFQhuYIppdpee2TkTXjVE4AlukkH5LOcVAZxigFSsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی وایرال شده از تلاش عجیب یک جوان برای پرش از پنجره یک خودرو به خودروی دیگر در تهران؛ حرکتی به سبک فیلم سریع و خشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/696186" target="_blank">📅 20:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696185">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
از ابتدای آبان ماه قطعی گاز در صنایع را خواهیم‌داشت
احسان قاضی‌زاده هاشمی، عضو کمیسیون صنایع مجلس:
🔹
برق صنعت که قرار بود از نیمه شهریور ماه قطع نشود، متاسفانه ادامه یافت و کمتر شد و قطعی گاز در صنایع را از ابتدای آبان ماه خواهیم‌داشت.
🔹
صنعت ما بر سر دوراهی قرار دارد؛ یا باید خود را تعطیل کند یا با شرایط گران‌سازی چاره‌ای جز افزایش قیمت‌ها نخواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/696185" target="_blank">📅 20:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696184">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a7b92fa8.mp4?token=UkVk5mDcfKDJL-TkkSF8PgzTCqz8Hafk4A9JKQuu7aGsV1HRW8XRlcKiqL_fJD1XtEfWoEkpjqW07mPkuIksOuJY1AKomZGh_MeOjGleZHeq4b_njCnHsIVp1Ap_J0AqPvAaGbK68d3rTq3hhBN91qwF-2SKz5Gr4yq0eyYoXU284ywtQatwT6m34iUfb5KRu6NsIMBrCZwSt-6IT9Lfv2JXLqhehllYvLu8LvErJ-rJE3yi4snooja87EV4fxWMkNBfBBFSX2khPbBqqVaDuF8UvVr-ompZwU76kyKD_GMcZ10Iju4h_Tx6TrqU6g7SfIPb4A9J_47svEqTpXCRrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a7b92fa8.mp4?token=UkVk5mDcfKDJL-TkkSF8PgzTCqz8Hafk4A9JKQuu7aGsV1HRW8XRlcKiqL_fJD1XtEfWoEkpjqW07mPkuIksOuJY1AKomZGh_MeOjGleZHeq4b_njCnHsIVp1Ap_J0AqPvAaGbK68d3rTq3hhBN91qwF-2SKz5Gr4yq0eyYoXU284ywtQatwT6m34iUfb5KRu6NsIMBrCZwSt-6IT9Lfv2JXLqhehllYvLu8LvErJ-rJE3yi4snooja87EV4fxWMkNBfBBFSX2khPbBqqVaDuF8UvVr-ompZwU76kyKD_GMcZ10Iju4h_Tx6TrqU6g7SfIPb4A9J_47svEqTpXCRrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
​
مقایسه BBC فارسی با BBC سایر کشورها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/696184" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696183">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f3d37bff.mp4?token=EPaA7D9sDBKzTQ79Jc6Q-b7Bsgcn-x3UNFOhpFzewF83gq0_BdthfVI8XAm1gJG0njCVbSwcrPORm7VqVaLejdqFZ7_v4Nw2Xl6VuFB6EV7AyowemI87zhEDNgz3KvSD9LJ2zO2p-KLjDrDBkjoR5edt_N-LCw6_ZUntH9Gn-aZa3SAD-4y1n_TqDE1KkXOyE0t-Ox6CRhfYRXwDU_DLTK-ZheBZKPVqwNu1YNqh0QfyIybG0w6f10M9lAdU8RPOyHqx87p_-1uY-Upo9CPuIuZ4-ZgabLkjEQjGVbx_QQBoyrjGjunfwLa8mMeSKirnASoCMlsycpCWlt9j9D2PYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f3d37bff.mp4?token=EPaA7D9sDBKzTQ79Jc6Q-b7Bsgcn-x3UNFOhpFzewF83gq0_BdthfVI8XAm1gJG0njCVbSwcrPORm7VqVaLejdqFZ7_v4Nw2Xl6VuFB6EV7AyowemI87zhEDNgz3KvSD9LJ2zO2p-KLjDrDBkjoR5edt_N-LCw6_ZUntH9Gn-aZa3SAD-4y1n_TqDE1KkXOyE0t-Ox6CRhfYRXwDU_DLTK-ZheBZKPVqwNu1YNqh0QfyIybG0w6f10M9lAdU8RPOyHqx87p_-1uY-Upo9CPuIuZ4-ZgabLkjEQjGVbx_QQBoyrjGjunfwLa8mMeSKirnASoCMlsycpCWlt9j9D2PYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین درخت ایران با دو قلب/ درخت لور یا انجیر معابد
🫀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/696183" target="_blank">📅 19:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696182">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
بهزادیان: اگر ناوگان MD لغو شود، تعداد پروازها و بلیت‌ها کاهش و قیمت‌ها به‌شدت افزایش پیدا می‌کند!
سیروس بهزادیان، رئیس کمیته فنی انجمن شرکت‌های هواپیمایی در
#گفتگو
با خبرفوری:
🔹
حدود ۳۰ فروند MD عملیاتی داریم که معمولاً روزانه ۶ تا ۸ پرواز انجام می‌دهند و در دو سال اخیر حدود ۱۲۰ هزار پرواز با این هواپیماها داشته‌ایم.
🔹
حدود ۴۵ تا ۵۰ درصد پروازهای ایران را MDها انجام می‌دهند و این هواپیماها قابلیت پرواز بالایی دارند و در چند سال گذشته هیچ‌گونه سانحه‌ای نداشته‌اند.
🔹
ما درخواست کرده‌ایم تا ۲۸ دسامبر ۲۰۲۷ فرصت داشته باشیم تا مشکل تیغه‌های موتور را برطرف کنیم و همه شرکت‌های دارنده MD نیز برای رفع این مشکل تعهد داده‌اند.
🔹
اگر این ناوگان لغو شود، تعداد پروازها کاهش، بلیت‌ها کمیاب و قیمت‌ها به‌شدت افزایش پیدا می‌کند.
🔹
با عدم پرواز هواپیماهای MD، حدود ۲۰ تا ۲۵ هزار نفر از متخصصان این حوزه نیز در معرض تعدیل قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/696182" target="_blank">📅 19:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696181">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff3c118eb.mp4?token=H70yglhJMxQXPLP6aZ7I9-rlm3nV1RpuZXOPLVenlPglwbMxHAl3psMEJMBHYaExmUMMYRUfR_lRuOk6Z23ZKDvNajHPCHsNVqRik9mly3HWbgAnDQsE-pOSRwm-mui5Zi1jpRAuBkHilZIIr1OmokT5xm0Cz9Lvf0Zhd5yMe2mRy4Rkz_dclWkvEbVf_emyE4v-Ek8qfHZJy-OoxHGGX-nGvcE3JwORdc7gYXfAxe4efreXkFFaMVyxd-viYD-y_KDNQXtJBl1biGB8XMcNilef0fCoD-vVYxmEdP_KNJOSaUk18jwXiQc_MFEHY0XZMmd8T0Tc7mFbPHEQMTM1YKYlj-q-q5iUKzBOf1MOzIkE8bImQkqG1tXLwdLdDl0xt8y8UF1tSGvW4KBCssdhlv8OdLamtsaYi3ZGbEDTgur8l_GeDcoAQVDt4Ij5sDAYcz5B9G3t3jHPe8LuDpWJJQCZHw5QBkADpYiriaD9PabkUbmjuYoSaEFJ67aQdoO08NiUGInw0FQvKLqOrmxfkQ1fr83ZYAZk_u0-NrxmADcVn8UCrpGNMbO10yMQwizPMjlNYGe5K7h8FN_Oa92iuzXcv3tI9H22qwmkXWC3vEyE9zj2UrDDLxDycdM1aesF-as9ez7jWSUPiG3gOeYkRqN3aYCKncszxHjABkxJNgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff3c118eb.mp4?token=H70yglhJMxQXPLP6aZ7I9-rlm3nV1RpuZXOPLVenlPglwbMxHAl3psMEJMBHYaExmUMMYRUfR_lRuOk6Z23ZKDvNajHPCHsNVqRik9mly3HWbgAnDQsE-pOSRwm-mui5Zi1jpRAuBkHilZIIr1OmokT5xm0Cz9Lvf0Zhd5yMe2mRy4Rkz_dclWkvEbVf_emyE4v-Ek8qfHZJy-OoxHGGX-nGvcE3JwORdc7gYXfAxe4efreXkFFaMVyxd-viYD-y_KDNQXtJBl1biGB8XMcNilef0fCoD-vVYxmEdP_KNJOSaUk18jwXiQc_MFEHY0XZMmd8T0Tc7mFbPHEQMTM1YKYlj-q-q5iUKzBOf1MOzIkE8bImQkqG1tXLwdLdDl0xt8y8UF1tSGvW4KBCssdhlv8OdLamtsaYi3ZGbEDTgur8l_GeDcoAQVDt4Ij5sDAYcz5B9G3t3jHPe8LuDpWJJQCZHw5QBkADpYiriaD9PabkUbmjuYoSaEFJ67aQdoO08NiUGInw0FQvKLqOrmxfkQ1fr83ZYAZk_u0-NrxmADcVn8UCrpGNMbO10yMQwizPMjlNYGe5K7h8FN_Oa92iuzXcv3tI9H22qwmkXWC3vEyE9zj2UrDDLxDycdM1aesF-as9ez7jWSUPiG3gOeYkRqN3aYCKncszxHjABkxJNgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از آبگرفتگی شدید معابر شاهین‌دژ
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/696181" target="_blank">📅 19:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696180">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
پوتین و پزشکیان روز جمعه با یکدیگر دیدار می‌کنند
/ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/696180" target="_blank">📅 19:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696179">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884904d006.mp4?token=ood7i1tmXtvpbHXqMJtigj_JYiXKoIvVQ3aROq9wQR53CMHSCg79EiN5EiHmnESR-uc_bRpuzjKOXnrktf5I7N6xHO40RKmCQAyVhExLadqdlGAmwF-zCVEwf8yWMgOed5kJT4zrzTLvsn6azZe-UAZQjagx22qIn6jYLWJYgrnuauCddRGZuF6aZJALGBenPThTXYSmSTJEG_FbUp2sx1_udCrGHSCLp3f4Zl9bE_FxeugOzsgf55akd4Aa_ShyUw_S4GFMpdbe5QWFvWElI21MpRr5ve-FkbWGN3BhEx-QL_IQkB740coE4I7Ex3NKhsnR4UobA9yaIuo3gCKq1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884904d006.mp4?token=ood7i1tmXtvpbHXqMJtigj_JYiXKoIvVQ3aROq9wQR53CMHSCg79EiN5EiHmnESR-uc_bRpuzjKOXnrktf5I7N6xHO40RKmCQAyVhExLadqdlGAmwF-zCVEwf8yWMgOed5kJT4zrzTLvsn6azZe-UAZQjagx22qIn6jYLWJYgrnuauCddRGZuF6aZJALGBenPThTXYSmSTJEG_FbUp2sx1_udCrGHSCLp3f4Zl9bE_FxeugOzsgf55akd4Aa_ShyUw_S4GFMpdbe5QWFvWElI21MpRr5ve-FkbWGN3BhEx-QL_IQkB740coE4I7Ex3NKhsnR4UobA9yaIuo3gCKq1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار؛ روش جدید کلاهبرداری با اسم پستچی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/696179" target="_blank">📅 19:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
دبیرکل حزب‌الله لبنان: آزادی جنوب لبنان را با چشمان خود خواهیم‌دید و اسرائیل هرگز نمی‌تواند حتی برای مدتی کوتاه در جنوب باقی‌بماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/696176" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696175">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEhgJBnRwpG1bgx476NdpEtVT619RsDtGKPs_MZ3t1w09QstG8V4uwvSv9u3Mce5bsF4qCptMa_ONmuiU4-uzTRXXRqNXYBrP6G3-e2TtbtxSWYPbP0lePA5aH7hJvhy7ZvS5pE_K5Ku2uSqkMYcLISo2lGgZQBcmjI_1cvNeLSxLKTJvXNPu5MblDvxnQBAN9Xs-FSiVDLKlkaMt1tDqXK5VJ_Ph3EMj1wfvACuI2FjcBX_XtGV_TKrAJZgV70FVfWalMRV13dUnd8Iep2j72MYDlCzCKhJ-OmuideY8OIRyBHI1RZe2wN1JmwmrM8hgm9BZ3K2an2UpS0Fci6dWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان جهانی بهداشت: نشانه‌ای از طاعون در روسیه مشاهده نشده است و خطر شیوع برای عموم پایین است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/696175" target="_blank">📅 19:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696174">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
آخرین وضعیت اعتراضات دانش‌آموزی در فرانسه
🔹
اعتراضات دانش‌آموزی فرانسه وارد نهمین روز شد؛ تاکنون ۶۰۵۹ نفر بازداشت و ۱۰۱۵ نفر زخمی شده‌اند. یک نوجوان ۱۵ ساله نیز بر اثر انفجار نارنجک پلیس دستش را از مچ از دست داده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696174" target="_blank">📅 19:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696173">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d7e3c4ebb.mp4?token=iLSH3zB6GUBJRRSKGp_ZUlyx-9CchDSasKf9uwVOm_Xt_YtcdTO8CYpVo11RtWVZVzC1VdV473Qdxh8UvRWJlPK1Lo4NuJqi1f1vyO8qzzR9O6G7AjPO_l88wvsGf-SalSYHeP6dj4Q8h1JpG7lShTW5_P3740M7mVk78tc2KtrItVOcnmX9XBJu8BbZW5415j4Ed5iEMFQFuF_wB43M71XwAgk32v2K8r6gfbdjzlpT8F1JAQ5n6eFHfAwNEEWV5pDhFkU0kda3NfWZWK654pkly63gkYUHF_y-Xxe0nzlCBO9JHRkiaJ_Yk6jsmxQDWgHnrR5viGSyVQiiptq6Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d7e3c4ebb.mp4?token=iLSH3zB6GUBJRRSKGp_ZUlyx-9CchDSasKf9uwVOm_Xt_YtcdTO8CYpVo11RtWVZVzC1VdV473Qdxh8UvRWJlPK1Lo4NuJqi1f1vyO8qzzR9O6G7AjPO_l88wvsGf-SalSYHeP6dj4Q8h1JpG7lShTW5_P3740M7mVk78tc2KtrItVOcnmX9XBJu8BbZW5415j4Ed5iEMFQFuF_wB43M71XwAgk32v2K8r6gfbdjzlpT8F1JAQ5n6eFHfAwNEEWV5pDhFkU0kda3NfWZWK654pkly63gkYUHF_y-Xxe0nzlCBO9JHRkiaJ_Yk6jsmxQDWgHnrR5viGSyVQiiptq6Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوست دارید عکس‌های بهتری بگیرید؟ ترکیب‌بندی (کامپوزیشن) واقعا این‌قدر ساده و البته بی‌نهایت در خروجی عکس‌تون موثره
📹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696173" target="_blank">📅 19:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696172">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHtAcdptojnBQZ4nH3EMY0HehiuiQiW9Kqsol3st8jU570ah_wW1Ge9-VXDD3nHYt04b48lmCyrIS5Y_v9yWxSiuhX85xRHzOODoTwVET86P1Mzn1tUbhjzisdwT3H4NknGEw4rrVgAWRU5cqUwYAj2hMeoPdm8X31EeVyCFEVdURz1swkD-5Me7phwtPkaBv8Zk3G5_Xjyi0LtbLsdUAygYuHWir9QKJytHB21mVh4DkEunwD-6nzXwmBuKdwmuZ782MlPV8J7SDaLzS-bArEyij7ExNeOc5__gjLk1H1EbZ7-nTLgK0qTFHwjflDuNmj6gWfXaSW3rG4BkAxw7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
«نگاهی به زندگی در روزگار جنگ»، جشنواره عکس در پاریس
همزمان با
بزرگداشت دویستمین سال اختراع عکاسی در پاریس
، جشنواره عکس
«نگاهی به زندگی در روزگار جنگ»
به همت
مرکز ایران و فرانسه و مؤسسه موج نو
، پاییز ۲۰۲۶ در پاریس برگزار می‌شود.
این جشنواره با نگاهی انسانی، روایت زندگی در شرایط جنگ را از دل
زندگی روزمره، خانواده، روابط انسانی، میراث فرهنگی، شهر، آثار جنگ، همبستگی و امید به آینده
دنبال می‌کند.
📅
مهلت ارسال آثار:
۱۸ مهرماه ۱۴۰۵
🖼
نمایشگاه‌های پاریس:
نوامبر و دسامبر ۲۰۲۶
🏆
نمایش ۵۰ اثر منتخب و اهدای جوایز و لوح تقدیر به سه اثر برتر
🔗
اطلاعات بیشتر و فراخوان کامل:
www.france-iran.org/iranphotos2026</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/696172" target="_blank">📅 18:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696171">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a75b37358.mp4?token=uel91dtZi8ppJkbph_87FhwF0K3egiGeuCp_FGExDTtiM6ZJranh9VlzhNQRQdLCtYxB32zoAEx0VS6h4TmxFUqOstEErt5hP1qN2Kh-McwZEs-BxNxkYCftenecJXKriSTYlDbb8TyASblH5lZ3b8MrPBL04Xuyrj9YpK-GRq1RCkC-MlN3DifFSMDHy4SOPNMJz7X4nP2KUJIgmJnf3kurTI0HLN4oe7Pq6kOryvLPDLcFfjuqLdnlRi0l6q1fmaC6hR74mDG7ev_CdvRt2IjR5snb1ax8wymkylWzm6h9H_vzZGTZ1OJ9QMg5rUdcXJAyuy8qEquD0EFQlEoAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a75b37358.mp4?token=uel91dtZi8ppJkbph_87FhwF0K3egiGeuCp_FGExDTtiM6ZJranh9VlzhNQRQdLCtYxB32zoAEx0VS6h4TmxFUqOstEErt5hP1qN2Kh-McwZEs-BxNxkYCftenecJXKriSTYlDbb8TyASblH5lZ3b8MrPBL04Xuyrj9YpK-GRq1RCkC-MlN3DifFSMDHy4SOPNMJz7X4nP2KUJIgmJnf3kurTI0HLN4oe7Pq6kOryvLPDLcFfjuqLdnlRi0l6q1fmaC6hR74mDG7ev_CdvRt2IjR5snb1ax8wymkylWzm6h9H_vzZGTZ1OJ9QMg5rUdcXJAyuy8qEquD0EFQlEoAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارگری در یک کارخانه تولید شیرخشک، پس از درگیری با کارفرما، برای انتقام حدود ۲۰ لیتر اسید را مخفیانه داخل مخزن شیر ریخت؛ اما آزمایشگاه کارخانه در آخرین لحظات این اقدام را شناسایی کرد. این حادثه می‌توانست سلامت صدها نوزاد را به خطر بیندازد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/696171" target="_blank">📅 18:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696170">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
هشدار مهم پیش از خرید ملک؛ سند و مشخصات مالک را حتماً بررسی کنید
🔹
سخنگوی سازمان ثبت اسناد و املاک کشور از خریداران خواست پیش از انجام معامله، سوابق ثبتی ملک و اصالت سند را به‌دقت بررسی کنند.
🔹
از خرید املاک قولنامه‌ای که فاقد سند مالکیت هستند، خودداری کنید.
🔹
مشخصات هویتی فروشنده را با نام مالک درج‌شده در سند تطبیق دهید.
🔹
برای بررسی اصالت سند تک‌برگ، بارکد امنیتی روی سند را با تلفن همراه یا نرم‌افزار بارکدخوان اسکن کنید.
🔹
اگر ملک سند دفترچه‌ای دارد، بهتر است فروشنده پیش از معامله آن را به سند حدنگار یا تک‌برگ تبدیل کند.
🔹
هنگام خرید آپارتمان، شماره و محل پارکینگ و انباری را با نقشه تفکیکی ساختمان تطبیق دهید./ روزنامه ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/696170" target="_blank">📅 18:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696169">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9506fe34.mp4?token=O24MxGFkjBGGsqrdursNbebeZRrgS35RHOOtx_4nQl14ei6ZrcAEOWxASTI5_hcRwU_xG0G5hQyQYKbtjuDuu4CuUT4gjUOn1qDdb3Az-chYeUlQNWb_ivocr2M_Y03dMfXLAn6pR9DuX644VH-v4qDbSHqYOAcQ_aBkXiz1ZvZc4xann1p24d02PSTJL0ojJNvP8bvoZwz6PIAYG8YKXhQp2mEbFe0D6u_zY9AJLS3NSwCoENnOSMaBAMOiGofCcbcd5NyBfKPm3PGBgDzg3mdACde_5v7zW6tH2M5jhup27MdMVgkiVlLIUj3aCqu7q121lIXAJDZh0vj72JZI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9506fe34.mp4?token=O24MxGFkjBGGsqrdursNbebeZRrgS35RHOOtx_4nQl14ei6ZrcAEOWxASTI5_hcRwU_xG0G5hQyQYKbtjuDuu4CuUT4gjUOn1qDdb3Az-chYeUlQNWb_ivocr2M_Y03dMfXLAn6pR9DuX644VH-v4qDbSHqYOAcQ_aBkXiz1ZvZc4xann1p24d02PSTJL0ojJNvP8bvoZwz6PIAYG8YKXhQp2mEbFe0D6u_zY9AJLS3NSwCoENnOSMaBAMOiGofCcbcd5NyBfKPm3PGBgDzg3mdACde_5v7zW6tH2M5jhup27MdMVgkiVlLIUj3aCqu7q121lIXAJDZh0vj72JZI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون| بارش شدید باران در اردبیل
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/696169" target="_blank">📅 18:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696168">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9148079cca.mp4?token=ZbJvF6R3OgDHIMS1DB1Y0HKI__C8YsU627NcjfdlxrlNzc2d8TEDNhdVkoO90lP_lp1YXoUpO5rMMlEKL8UGGflCCRKbN80gpndHXQoJOgTY1Zp7DVaSmxOStHC41grajIYlX8oWoEboD2J6n9t8LxByX_ZF6GjzBtPK37locXJLBlq6WtoNxQrL1oZJ-ZYqYDCw_Oi9OC_4bJL2fOXIzPh7h7Zbq3OpPjzXQhbyOWKiv8utEoTBATk5U5yQs_NzZDxibbnVbwx27oNckLTQj41_YerNwBhu_jbfK7gL3J591jjCKtaaPaJkqG06w3JkbPiVOdbeKEA7PtVeZxHRBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9148079cca.mp4?token=ZbJvF6R3OgDHIMS1DB1Y0HKI__C8YsU627NcjfdlxrlNzc2d8TEDNhdVkoO90lP_lp1YXoUpO5rMMlEKL8UGGflCCRKbN80gpndHXQoJOgTY1Zp7DVaSmxOStHC41grajIYlX8oWoEboD2J6n9t8LxByX_ZF6GjzBtPK37locXJLBlq6WtoNxQrL1oZJ-ZYqYDCw_Oi9OC_4bJL2fOXIzPh7h7Zbq3OpPjzXQhbyOWKiv8utEoTBATk5U5yQs_NzZDxibbnVbwx27oNckLTQj41_YerNwBhu_jbfK7gL3J591jjCKtaaPaJkqG06w3JkbPiVOdbeKEA7PtVeZxHRBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی غذا وارد مجرای اشتباه می‌شود چه اتفاقی می‌افتد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/696168" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696167">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN7EDa810aTD4Hs6FomKbHppRFaNxLrqiKa6tWX_2HXq3HZnRxm5fERKrzyCQLuPPZ6UxEKrZCeNe4X3CDxXndpkBh8dDoPyAVOixv1e68Iq7iFm_5MRZ8aLRsDfN5m24uk2d7vsb1uJc2j1olccOY0mStz5c2lwnXw0LFpiWUrhqnALBmsPHu7sghGotXIngwNFZ7HehYluIhFcqT3M0CmI55ylJyIYg5UT5FvWyEGtQOROAB_nqCMCjnf7NvBbfrVAGDKfWjEHmWePRzjajbii_lyP-WKuTb6R8L5XXARm9-wRoyxUb5ZYZKLa5gKROAiDXJDwhoO8qB38WO3nag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🤝
مشارکت بانک تجارت در بازسازی زیرساخت‌های علمی کشور
💠
در رویدادی مهم برای تقویت زیست‌بوم دانش‌بنیان ایران، تفاهم‌نامه بازسازی زیرساخت‌های فناورانه چهار دانشگاه صنعتی (شریف، اصفهان، شهید بهشتی و علم و صنعت) با مشارکت وزارت اقتصاد و معاونت علمی ریاست جمهوری امضا شد.
🤦
بانک تجارت با مشارکت در تأمین مالی این طرح از طریق سازوکار اعتبارات مالیاتی، در مسیر بازسازی و تجهیز مجدد دانشگاه‌های آسیب‌دیده گام برمی‌دارد.
🔻
دکتر اخلاقی، مدیرعامل بانک تجارت، در این راستا تاکید کرد: «حمایت از زیرساخت‌های فناورانه دانشگاه‌ها، وظیفه ما در جهت تقویت ستون‌های دانش‌بنیان کشور است و بانک تجارت با بهره‌گیری از مدل‌های نوین تأمین مالی، از این مسیر حمایت می‌کند.»
🌐
مشروح خبر
👉
📱
tejaratbankofficial</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/696167" target="_blank">📅 18:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696166">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سازمان جهانی بهداشت: نشانه‌ای از طاعون در روسیه مشاهده نشده است و خطر شیوع برای عموم پایین است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/696166" target="_blank">📅 18:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696163">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrNZijNWVKRFGiQo6pG_f4MqsaABX9tNAln2AhLOcMSclApmFshBqI7LUAMHzzgN5Y_fV8iArTCgOOmvL33u43L42cwGKVqQFNv_zw_VVRxjgEuct8VrkPrnvHo-b22xsQnmZFVHEfSbOoRDzOjBIXK9cD0fZNnh4rtLTgSc9hhWUCz0f3DQgyDi0Y2MWd7Rhfn2R7eH9eoyrxqE3vS0gsmU9KnmMEZSDaYlcJ9IwwJdHUPQSq1kjRL6wXUXVXoUxuP9XQKtbsokPw4tyDXajYR6oQczS0Oh8jBzv8tJkKb2F6OJL_a1z5C7k-XPfxOSX9F0t1k_tRISXQ7XGNNTkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/696163" target="_blank">📅 18:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696159">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37c23244b.mp4?token=Zun9FY0WPCKDED4RuYsgsM6JWLGudgNglK_TqG0gziDsCNukJTa-n9-UcC-4llQANr4_fi0TeiWilCkSeWHXBfFGmdTD2WZz21MMeL6jZth9z3-0XFJGf-lxRi6XFQcn_i02aqBGAsDcxF1AR10JzsRrkz0ik_0JdIMATQGUanE0H8xinOe_tH-lAFIhYxUs8I1PUsPMhUXl8ECQG_ri-Djmx_B3BSd-oPM2Al7z3hJgzYXnpS8D75c7WDPsk0xwPmIQtwYbOZkbaDkb3Sn9_ULBI58pzEbNSEctqT0MXlaZlAJceKKozi0JK5QGTIWzF51JioIL_I415sBo8Amf3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37c23244b.mp4?token=Zun9FY0WPCKDED4RuYsgsM6JWLGudgNglK_TqG0gziDsCNukJTa-n9-UcC-4llQANr4_fi0TeiWilCkSeWHXBfFGmdTD2WZz21MMeL6jZth9z3-0XFJGf-lxRi6XFQcn_i02aqBGAsDcxF1AR10JzsRrkz0ik_0JdIMATQGUanE0H8xinOe_tH-lAFIhYxUs8I1PUsPMhUXl8ECQG_ri-Djmx_B3BSd-oPM2Al7z3hJgzYXnpS8D75c7WDPsk0xwPmIQtwYbOZkbaDkb3Sn9_ULBI58pzEbNSEctqT0MXlaZlAJceKKozi0JK5QGTIWzF51JioIL_I415sBo8Amf3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت اعتراضات دانش‌آموزی در فرانسه
🔹
اعتراضات دانش‌آموزی فرانسه وارد نهمین روز شد؛ تاکنون ۶۰۵۹ نفر بازداشت و ۱۰۱۵ نفر زخمی شده‌اند. یک نوجوان ۱۵ ساله نیز بر اثر انفجار نارنجک پلیس دستش را از مچ از دست داده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/696159" target="_blank">📅 18:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696158">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رویترز: پالایشگاه‌های مستقل چین با کاهش شدید عرضه نفت ایران، خرید نفت از عراق و قطر را افزایش داده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/696158" target="_blank">📅 18:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696157">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2882a026dc.mp4?token=ctUGl2B2N49IhP-YT2pP6ryBMCjA2nfHCA_-XnpckTvC_avatwZEOdBEwr87hHWbjRqE5JR3JVobCgQdLUwnEaM55JOWy5Mfk_MK3NUioDeHOLZHPJQtC34wJKXVt9VRoXovnVFA0Md3w_wqHedmWk9aUwvCSTHtvLRYiIr8Q4PekvRgPSp-QpR__eG3erhZ5KIBfx1BawbH75CeTX-2zO3r_dpmHvybYyXi1Bb60fkt2RhSCQtWasb_BKCDV4D0AZmoh0AKNT-dROxM6nrZ5xLqYEz1ZF8lVnpKNhGPM5cKfZxap55DM4WiGRsmsIPd4FLTA0ByMw8ehYM68AkBJDGieUnpQvZkvEte90xg6FGrpfvJlKQk9uZf4vJFFDUg55DFahgjZL2mnzcK7x9LSsFgDhOsexqXW8spIp5yhq32Fw45bh_YBNIKRWNq8_XmsoeN62aJVUKpZ8yQlxEU83z4mLM5YsN_PehFh12SHS95Kiz9hBCDNgISWcQzFNHPXwQlLa0pQw4vU7VhYcDyTxiCKzBokwGTJCPlde6j-iK_ufv4zovrHJpbm8w_nhuGW3mp8Z4iQXJNFb5OqqUFxyMJruKKo7WfF4JX9K_yfnfY0oI61Qok_US4ZvwdI-2f3sg9Ilz7CFky9absA21ZljMz1ECOEj56NF8vbWYvJbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2882a026dc.mp4?token=ctUGl2B2N49IhP-YT2pP6ryBMCjA2nfHCA_-XnpckTvC_avatwZEOdBEwr87hHWbjRqE5JR3JVobCgQdLUwnEaM55JOWy5Mfk_MK3NUioDeHOLZHPJQtC34wJKXVt9VRoXovnVFA0Md3w_wqHedmWk9aUwvCSTHtvLRYiIr8Q4PekvRgPSp-QpR__eG3erhZ5KIBfx1BawbH75CeTX-2zO3r_dpmHvybYyXi1Bb60fkt2RhSCQtWasb_BKCDV4D0AZmoh0AKNT-dROxM6nrZ5xLqYEz1ZF8lVnpKNhGPM5cKfZxap55DM4WiGRsmsIPd4FLTA0ByMw8ehYM68AkBJDGieUnpQvZkvEte90xg6FGrpfvJlKQk9uZf4vJFFDUg55DFahgjZL2mnzcK7x9LSsFgDhOsexqXW8spIp5yhq32Fw45bh_YBNIKRWNq8_XmsoeN62aJVUKpZ8yQlxEU83z4mLM5YsN_PehFh12SHS95Kiz9hBCDNgISWcQzFNHPXwQlLa0pQw4vU7VhYcDyTxiCKzBokwGTJCPlde6j-iK_ufv4zovrHJpbm8w_nhuGW3mp8Z4iQXJNFb5OqqUFxyMJruKKo7WfF4JX9K_yfnfY0oI61Qok_US4ZvwdI-2f3sg9Ilz7CFky9absA21ZljMz1ECOEj56NF8vbWYvJbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش ساده برای از بین بردن لکه‌های بدنه خودرو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/696157" target="_blank">📅 18:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696156">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c97c9700.mp4?token=OHJa-PYpc57gNwS0_P_5hZEKKj7bw3FPAILGhZ0o3tuF2xcv_2IBYLEJXJ02ZdDQ-eoS91hT0pWmAwQRf7Jmis40Nc1TNExCrbWh9hIpXE80ybaKPajtW35FUQdZYl7SOmerr4Rf-YhIV0qj7FC57q8Qkf46IzF29KX7YJE5GqYNRFvAPDoEDtxcdZl4dtfCB3-nTc9_vXV_SwhZ2JOalASsJ-0H_VzdazjCi719r2II0-Jmu9UbLJ-CjeacRgzDYF7HXZfu_cYD37yybbaJghdPAEYsPPeyCxbXOeI2fAwJFxuo99g4JsK6rSxulH3QBG0REM2ipnogs-0KXwyZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c97c9700.mp4?token=OHJa-PYpc57gNwS0_P_5hZEKKj7bw3FPAILGhZ0o3tuF2xcv_2IBYLEJXJ02ZdDQ-eoS91hT0pWmAwQRf7Jmis40Nc1TNExCrbWh9hIpXE80ybaKPajtW35FUQdZYl7SOmerr4Rf-YhIV0qj7FC57q8Qkf46IzF29KX7YJE5GqYNRFvAPDoEDtxcdZl4dtfCB3-nTc9_vXV_SwhZ2JOalASsJ-0H_VzdazjCi719r2II0-Jmu9UbLJ-CjeacRgzDYF7HXZfu_cYD37yybbaJghdPAEYsPPeyCxbXOeI2fAwJFxuo99g4JsK6rSxulH3QBG0REM2ipnogs-0KXwyZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکای‌نیوز: بیش از ۵ هزار نفر در پی اعتراض‌ها در فرانسه بازداشت شدند که بیش از ۴ هزار و ۴۰۰ نفر آن‌ها کودک هستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/696156" target="_blank">📅 18:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696155">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مدیرعامل آرامکو: حتی اگر بحران جنگ علیه ایران همین الان پایان یابد، امکان‌دارد جهان برای پر کردن دوباره ذخایر نفتی که در طول جنگ مصرف شده‌اند، تا ۲ سال به حدود ۲ میلیون بشکه نفت بیشتر در روز نیاز داشته باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/696155" target="_blank">📅 18:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696154">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0d78119c.mp4?token=NaxY1afWtnwD0G6S3b8wJcDjtcqudGjYdxTb9duC7npERubZekuG9CQBPAvReAHIEFPqlx86ZCxqUer9JlmMXP3oDdP9ij67g_FWJTxIMdPLbsxvBha8uBfDdmS_mmIXnHtLJTH--8vjiDSDd7j6cjb7YAKymxjqUS2NlTKx1hnxcTYMY6AycYQx_pPb6_VSuR8HcC39PHy8ccomDx3UAOGpGjJaMwaEbdEv8aYvdNjnYTqVS5MQOVtMASbieM91Vg3w7qlws3BnqOiBz4kvtu-KCugTytc1NYaM5ZAqSl0P_sJSjrVKn1f47o3VHpMXyEQSpc_TKOo7mfaVfQSDlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0d78119c.mp4?token=NaxY1afWtnwD0G6S3b8wJcDjtcqudGjYdxTb9duC7npERubZekuG9CQBPAvReAHIEFPqlx86ZCxqUer9JlmMXP3oDdP9ij67g_FWJTxIMdPLbsxvBha8uBfDdmS_mmIXnHtLJTH--8vjiDSDd7j6cjb7YAKymxjqUS2NlTKx1hnxcTYMY6AycYQx_pPb6_VSuR8HcC39PHy8ccomDx3UAOGpGjJaMwaEbdEv8aYvdNjnYTqVS5MQOVtMASbieM91Vg3w7qlws3BnqOiBz4kvtu-KCugTytc1NYaM5ZAqSl0P_sJSjrVKn1f47o3VHpMXyEQSpc_TKOo7mfaVfQSDlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس سازمان انرژی اتمی ایران در جمع خادمان حضرت رضا(ع)
🔹
محمد اسلامی، معاون رئیس‌جمهور و رئیس سازمان انرژی اتمی ایران، با حضور در چایخانه حضرت حرم مطهر امام رضا(ع)، در کنار خادمان این آستان مقدس به خدمت و پذیرایی از زائران و ارادتمندان حضرت ثامن‌الحجج(ع) پرداخت.
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/696154" target="_blank">📅 18:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696153">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیوپنا(پایگاه خبری دانشگاه پیام نور)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9bXZAVmaHA9F3fm7Djje3_J_7XdllGspDtO4Gfp-az8dKktwj_WHVwRpCa6afbziByrueJaRc91f4jnTj9MVrTq1CjHDwyT2zMpJn7YfBqb7-npUzB1BbYPREdOAPA0qM3fBVImfD48ohsIXqzl3R2nG1TzOO-4rnFNLkxHbRxnwdVZMbnn-MWbLRtmbYUr0AZ9RTzc7HBKhgwR25a9aAas15iXSu_8dt_9j6dYVS1Royrjf0bgZxiTM8WBRiZJLpuiOISODXiFQJEQaqv1vmDQ8qyicWBYpA-HRYEXOJsLqEYKRwT87CgIq7hj5PCNanbrFAMVNyOEg4-BrPBUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
از انتخابِ خوب جانمونی؛
📌
هرکجاے ایرانی؛
✔️
فقط کافیه انتخاب کنی
؛
▫️
انتخاب دلخواه محل آزمون
▫️
کلاس‌هاے حضورے و مجازے
▫️
وام شهریه
🔻
مهلت ثبت نام؛ تا ۱۶ مهرماه
🔻
سایت سنجش؛
Sanjesh.org
┄┅┅┅┅┄❅
🇮🇷
❅┄┅┅┅┅┄
اداره کل روابط‌عمومی دانشگاه پیام‌نور
@Upnanews</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/696153" target="_blank">📅 18:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696152">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZPhi6U3Wb_z1mfrT1r-XR3HUuoGns5V-TTlwpKHCSbUKw6hz1UNX_dFI08rVzcAba84mWo5lvc2-yMjyvqMtreIl0XAE9cwlrFLF3P_KAbq-plkPqZkBU-Wki2DEpzIQ68tfTtbDp1IISOdN0gQpcaLxDoOVMMYSHmCbYnLrURlTPtcU6azye4q2QsJMFDHqXlZ7v6sdoB8Muok9qonerIv10SiVWeRWW9f4a0p1MmriUTrlfNK73rSK-vq67hFXgNo95b1ejhO2EC1NM9dK8GJDfJP5ocn5UWed-luWGPzlY6rOhBgdFhWLjq98IBqH3YFU9UP4QE-jAGw2KszmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دیوانه: راهپیمایی‌های من دوباره حزب جمهوری‌خواه را نجات می‌دهد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/696152" target="_blank">📅 17:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696151">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f0c1a81.mp4?token=vVWKnYOpkIM6i6cSrmB0FFcl29XQlPFd3MclwdONEv_WIFnVHlGwFGGwwRxGQLDegfoNprQVfVHUL73XEfxAztOvnIyH5UL-ssia4x-20icY5H53y_MopIqY3lzJ0DRSOiMfhY-1jCcXz8BA0jhyjlE539pv6bWlEfY3cFGsKe7BJcgC4CckQDh49Fv_qyaZYLfmsML3RmhtCfyuDgHj-OalGaW7pMCahVpcl2T4BckvR-d843r303ovHjY8HY98ZjTpODVpxM4todZuJfVeC9JcfNKZc34WB__VifOTYnK7y1PYkadDW45Hhmy6dCBK5eMkLA1oJ_0RKhx2Z1DSBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f0c1a81.mp4?token=vVWKnYOpkIM6i6cSrmB0FFcl29XQlPFd3MclwdONEv_WIFnVHlGwFGGwwRxGQLDegfoNprQVfVHUL73XEfxAztOvnIyH5UL-ssia4x-20icY5H53y_MopIqY3lzJ0DRSOiMfhY-1jCcXz8BA0jhyjlE539pv6bWlEfY3cFGsKe7BJcgC4CckQDh49Fv_qyaZYLfmsML3RmhtCfyuDgHj-OalGaW7pMCahVpcl2T4BckvR-d843r303ovHjY8HY98ZjTpODVpxM4todZuJfVeC9JcfNKZc34WB__VifOTYnK7y1PYkadDW45Hhmy6dCBK5eMkLA1oJ_0RKhx2Z1DSBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکای‌نیوز: بیش از ۵ هزار نفر در پی اعتراض‌ها در فرانسه بازداشت شدند که بیش از ۴ هزار و ۴۰۰ نفر آن‌ها کودک هستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/696151" target="_blank">📅 17:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696148">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
به‌دنبال برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گسترده حقوق بشر، امروز عصر پیر کوشار سفیر فرانسه در تهران، از سوی اداره کل حقوق بشر ایران به وزارت امور خارجه احضار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/696148" target="_blank">📅 17:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696147">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91d320c89.mp4?token=PLDnTiRQfxobudB9uEQF3X6ik3CVh98xA9VmJtcIgys_X_bOOnYdeRVvPK5twQC6_HEXVxxMyO6LRyy85YnY_10_sok6WKWGoIYG184UDMdUZcx_1dkDJYGu5qK4RBIQRq96S9UBoDWiNso2QEwBlbF4oce4sAHpwaWSbaZz__Z16zIBNIWWeS4AlH-ucFagPZG_57H8cfRMpqcUzfIvfFbcGlL8gSXielhA0cpQ2F0bcMLg7h1gGONCgNm9BwDQY4RGGt7Y0w0sAgTlNVWlTeis3xz1bInR5r99T442bIXqUiyS5riBpePQzWJJKV3EB8yRXK6JcxzgTYcYhHsnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91d320c89.mp4?token=PLDnTiRQfxobudB9uEQF3X6ik3CVh98xA9VmJtcIgys_X_bOOnYdeRVvPK5twQC6_HEXVxxMyO6LRyy85YnY_10_sok6WKWGoIYG184UDMdUZcx_1dkDJYGu5qK4RBIQRq96S9UBoDWiNso2QEwBlbF4oce4sAHpwaWSbaZz__Z16zIBNIWWeS4AlH-ucFagPZG_57H8cfRMpqcUzfIvfFbcGlL8gSXielhA0cpQ2F0bcMLg7h1gGONCgNm9BwDQY4RGGt7Y0w0sAgTlNVWlTeis3xz1bInR5r99T442bIXqUiyS5riBpePQzWJJKV3EB8yRXK6JcxzgTYcYhHsnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکه‌ای از بهشت در لرستان؛ آبشار آفرینه
🌿
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/696147" target="_blank">📅 17:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696145">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e3d0f1fd8.mp4?token=BM7j8bLlUdkj53QO8FYvwtDQt5jP_ho7q8kJlLX5K4Xl19ksNrpn4kd27dfML_wlP-FIoUQ4WSHltxkqZm65hzc_r8XRRBUn3qtMBzDeWVYLz5nbxrfLP7npkRKhHg1fRcQObe3RbzznXdXOmaTtGTaBm6Y9JJv3wDbLfMxTtFJ2Lxk2Tgi2jtPx5oV-rqPNcYaXI2izMJo6vevfxc8Wr_qRyWLcmkflZ6bMQZKPhXoQlFtrUNEBa7_RWAGzY61m4uXrqE3_lFeCXMjg447UQkd4eRsbeRZNa3u9_1fi58Q29Xw2mfpewHsJoENTcjlTiq-2L4zP6yXk4yO_kxJhjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e3d0f1fd8.mp4?token=BM7j8bLlUdkj53QO8FYvwtDQt5jP_ho7q8kJlLX5K4Xl19ksNrpn4kd27dfML_wlP-FIoUQ4WSHltxkqZm65hzc_r8XRRBUn3qtMBzDeWVYLz5nbxrfLP7npkRKhHg1fRcQObe3RbzznXdXOmaTtGTaBm6Y9JJv3wDbLfMxTtFJ2Lxk2Tgi2jtPx5oV-rqPNcYaXI2izMJo6vevfxc8Wr_qRyWLcmkflZ6bMQZKPhXoQlFtrUNEBa7_RWAGzY61m4uXrqE3_lFeCXMjg447UQkd4eRsbeRZNa3u9_1fi58Q29Xw2mfpewHsJoENTcjlTiq-2L4zP6yXk4yO_kxJhjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با مفهوم علائم درج‌شده روی برچسب لباس‌ها آشنا شوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/696145" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696144">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎂
برج‌میلاد‌تهران‌تولدش‌را‌
باشـهروندان‌جـشن‌می‌گیرد
🤩
تا۵۰٪تخفیف‌ویژه‌بازدید
وشـهربـازی‌بـرج‌مـیلادتهران
🚗
نمایشگاه‌خودروهای‌کلاسیک
🛵
نمایشگاه‌مـوتورهای‌کلاسیک‌
با‌عنوان‌‌نمایشگاه‌"پـلاک‌طهـران"
👶🏻
بـرنامه‌های‌ویژه‌هفته‌‌ملی‌کودک
همراه‌بازدید‌رایگان‌کودکان‌زیر۱۲‌سال
اجرای‌ویژه‌برنامه‌‌بچه‌های‌ایران‌قوی
🎸
همراه‌گـروه‌مـوسیقی
👬
اجرای‌جُنگ‌خانوادگی
🎭
باحــضور‌هنــرمندان
🗓️
روز‌هــای ۱۶ و ۱۷ م
ـ
هر
🕐
ساعت ۰۹:۰۰‌ الی‌ ۲۳:۰۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/696144" target="_blank">📅 17:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696143">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
عارف: از شرمندگی مردم بیرون می‌آییم؛ افزایش کالابرگ نزدیک است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/696143" target="_blank">📅 16:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696142">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO9t0ih8CHuQDG0_uMwN7e0kw5U9w7Vbtah8YT0OnZWTA47A5cg9BFP4gW5Z1DPGx0NIcKUIDf1sNXHlh6C87LfC2asXsErqPD9ePdV-RP8rMbrHjYWIWArAriTJkFjdrwnnnqmwemVT5tBBah7GmdhuhB3CaJSFkr1kdAHUGvZ-IXH9_sROZmXKGbQQp-Q6eaS3Lzt0kQL_5ZZTCF0sZgV_3FJ_G4_LhWOZNwhaGvXiff_dfkBWCw1TNaKPQvY9LuqykYAYuXDQFpazzarqJsx3a1vMmSw_-iaSOUlBw-lyMSL6dFYXi0H2z6ORNxwm9Uime2c9UnlNEhz1HcSqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت آزمایشی اینستاگرام لو رفت/ بی سروصدا و بدون تعامل به پروفایل‌ها سرک بکشید
🔹
اینستاگرام ظاهراً درحال بررسی قابلیتی به نام Read-Only Mode برای مشترکان Instagram Plus است که به آن‌ها امکان می‌دهد پروفایل‌ها را بدون امکان لایک، کامنت، ارسال پیام، فالوکردن یا مشاهده استوری‌ها ببینند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/696142" target="_blank">📅 16:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696139">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c99b29251.mp4?token=IQdr7cnYsAlvuJHDodYYuebwai37fFB3UpwxjjTPy87rzAGaU2cgVgFOk1nwiYfmhqmL28vc3flFE9abB-H0L4kUAlPKyF_pWZTCz5RvKyZ1_bxq3_GkLCFs6K7964Hx9U09TLSzu53x-pHEmxB9_ruJIFSWqQlQ9rDixU0PRW4OzqEKyyuZ0Rwsg2DHmMyErCrN9PcycjPeGhB2i65xvxekB0AkwOFxBmMuKUIcSheeKsPd1-NS10Ka-hdQGnUKvzq42K_a3JKF9g18AHtlKO-AsHBiPhL8JVuPjdR68pVfQFmItKnArwdwV6bxwNC-CQLwDTgxls_96PdCjiEZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c99b29251.mp4?token=IQdr7cnYsAlvuJHDodYYuebwai37fFB3UpwxjjTPy87rzAGaU2cgVgFOk1nwiYfmhqmL28vc3flFE9abB-H0L4kUAlPKyF_pWZTCz5RvKyZ1_bxq3_GkLCFs6K7964Hx9U09TLSzu53x-pHEmxB9_ruJIFSWqQlQ9rDixU0PRW4OzqEKyyuZ0Rwsg2DHmMyErCrN9PcycjPeGhB2i65xvxekB0AkwOFxBmMuKUIcSheeKsPd1-NS10Ka-hdQGnUKvzq42K_a3JKF9g18AHtlKO-AsHBiPhL8JVuPjdR68pVfQFmItKnArwdwV6bxwNC-CQLwDTgxls_96PdCjiEZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه برخورد یک سیارک با ماه؛ انفجاری که سطح ماه را به آسمان پرتاب کرد!
🌕
☄️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/696139" target="_blank">📅 16:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رئیس جمهور با صدور حکمی پاک‌نژاد وزیر سابق نفت را به عنوان مشاور خود منصوب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/696138" target="_blank">📅 16:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696137">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/696137" target="_blank">📅 16:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696135">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSDQoPIzuCRuVMJOhRlLt22nnT49fbn6bBo0Kww8_C5vOLKgDs2r7ca4kT3hvRgupt_oZ1w2gmXBebdPX68iw1pwArGMntFo2vrdYBNyJMOulfgFEfGkhW-dCfkCp-7CFvey3fH3T9VCXS2PLabqlFF9PnzcjDD5Nb4HU9QX3FzX3oZph6khfHQzpFs-Dx0-SdmBn9dGQrwGoc7ed8Ofw92ozPfipaI87baAx7cRF_eWZTdhy_dNEYS3Uk-tJYqeZD_WE2-AUR9_A1mzrScbR1fBz_id4O_Oa-9h7le1OK83q0W8m9hsgvroYHUI2mkBU2r_dB_6dJNaE1rpiCkNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس پیشین سرویس جاسوسی آلمان به اتهام جاسوسی بازداشت‌شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/696135" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696134">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سرلشکر رضایی خطاب به دشمن آمریکایی: شما در جنگ نظامی شکست خوردید و در جنگ اقتصادی نیز شکست خواهید خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/696134" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696133">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
حادثه امنیتی در نزدیکی پایگاه هوایی آمریکا در انگلیس
🔹
پلیس انگلیس از وقوع یک «حادثه بزرگ» در نزدیکی پایگاه هوایی آمریکا در فیرفورد و بازداشت چند نفر به ظن نقض قوانین مواد منفجره خبر داد.
🔹
ساکنان مناطق اطراف نیز به‌دلیل این حادثه تخلیه و به یک مرکز تفریحی…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/696133" target="_blank">📅 16:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696132">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMu0bw_xBP15Lf2Us8Gp-_hIEpe61lG_wAcZAaUjQLrdeOLpNY9_LDMZldxtlsR9s8vOnivfr-8tmJo_wCx9s_pTP5L5WO1wKE0vo79gaRlC4BbSagMH1NysEUQy93zryoR0R5vGYVfKZIoFpk8y-eRZ4WA4B5DU21dn28fO0hZ1dCCQRWMJyEdF588agaxoz1T8egIJe7T6qAwNflwzxrrAvEXuUoSvUjypyTITW-na6a9fh1EFhVLr3kc15iVjK6pdql56Yc_GzaDGU6U3TR90-gPOaheruvklpTx4uaKyE9mkBkcNyBSNgySztJXYwQ0VU5bX8ckBPTPEsk1E_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت واقعی نفت از ۱۴۰ دلار عبور کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/696132" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696131">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqPh-x2O97tXEft2KnBMvxgWqtdObPkplHxdZP8cU-Kn0_LogZHbx3F8Pjn9YiDEI1dTf-bnvkDAVp4CZ82Xjfy3IbKOe4Nuv30zcwcTh5UrOwNOzGbc1CHj5OtasfBz4ewAOWFHvuGaQFtH0GCX18mJ0EMCssgMlZZ0w6RXJF_NgZQ47WcSIb5QbsNPj4gieQBB-aggZJd6Z96dTc8EF9Ncmn1sfQd8j3mUmzWs8w8E837AlvFSWq2sT-AAKbLSXkHBj9qgcFNvXEpb-AUlbdBO_7f8B_f6cy8jhR8p8VqZFWV_lRVDUnA3OVDSD04YwieHZ054wWSPNnP_0TPVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع بد ترامپ در نظرسنجی‌های آمریکا
🔹
نتایج نظرسنجی مشترک آسوشیتدپرس و مرکز تحقیقات افکار عمومی آمریکا (NORC) از افزایش نارضایتی عمومی از عملکرد ترامپ حکایت دارد.
🔹
۸۳ درصد آمریکایی‌ها از عملکرد ترامپ در هزینه‌های زندگی ناراضی‌اند؛ ۷۴ درصد نیز درباره عملکرد او در اقتصاد و ۷۲ درصد درباره نحوه مواجهه با ایران ابراز نارضایتی کرده‌اند.
🔹
همچنین ۶۹ درصد معتقدند جنگ ایران ارزش جنگیدن نداشته است و نیمی از آمریکایی‌ها نیز نسبت به افزایش شدید هزینه بنزین ابراز نگرانی کرده‌اند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/696131" target="_blank">📅 16:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696130">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iiigu1I5nLlmzolKVzUrZHU0trth2wo2XUcOT68LRaIOH5GfG5wPzMklrMTK4qP_oNR6kE7NtfcIhjyHIt8ihEae_d8RB8urQqkmsBzwpvbTrds6awYMvhbyt7amhyjOKaGcIsO_FHnhlgJXwvRQnymHSUA9IrlHjOI0j0LeKW5XFiM4dCTcF-yarySLvPBV8PCWygb6J1mbauCV573GVxWJM-nPTPeBVu7LgXJJm2av8ps4cUcACKSzTSEDKVSe8O5_NEYsRWOHZ2Pb9gzCTHLLrMU-3MIHPUGzZk42fH61ayly9WtGqR41XxGJXNLZseLQHL8X0q_BjEkjHPyRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رتبه دوم کنکور هنر: جنگ و قطعی اینترنت باعث شد تمرکزم روی درس خوندن بیشتر بشه. در واقع، دوران جنگ برای من تبدیل شد به نقطه اوج مسیر کنکور و تونستم پیشرفت زیادی داشته باشم!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/696130" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696129">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ed6ebddd.mp4?token=hgzsbqYYdUXPj07gVxcXstfgKj7we7c8v3ddt3XFTXSYdY9Pe_P2kLLzYNxtYsNZDul5Nht-tcQKeFKAD3RBr7yadDlyx-oW1135wYThjn268XL-egaw7J05BHgkE_qZxI7CL83Z5qPNFT_ddRcWEXiNAoRFuAyNlvtiAXeSFSqA-ay5uPOP8IF6DzpAsQmYUqTf187KqGFecmD7Fk3YUIK3-eodG7M4aPutDe6WHmO1B9CGBBEEk-fdawn2U2pPF5lRpBmcrBOIXoivaI_FJI1d3PV8dn5KTWWQsH87DbkrXXQ8ijzLxI8RNt-1j4CZQQStUUAdzJQ6hOzTX0rn0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ed6ebddd.mp4?token=hgzsbqYYdUXPj07gVxcXstfgKj7we7c8v3ddt3XFTXSYdY9Pe_P2kLLzYNxtYsNZDul5Nht-tcQKeFKAD3RBr7yadDlyx-oW1135wYThjn268XL-egaw7J05BHgkE_qZxI7CL83Z5qPNFT_ddRcWEXiNAoRFuAyNlvtiAXeSFSqA-ay5uPOP8IF6DzpAsQmYUqTf187KqGFecmD7Fk3YUIK3-eodG7M4aPutDe6WHmO1B9CGBBEEk-fdawn2U2pPF5lRpBmcrBOIXoivaI_FJI1d3PV8dn5KTWWQsH87DbkrXXQ8ijzLxI8RNt-1j4CZQQStUUAdzJQ6hOzTX0rn0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوخاری؛ یکی از خوراکی‌هایی که می‌تواند روغن زیادی وارد بدن کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/696129" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696128">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgrUiYFNM_8tQuMWlkhD2BiFBveaBqehcJQc-TDRsz54vMQcivGD21tBNOmTBB-tGMgJRjfU3KgaXSFQABV9I-jlHuPBwLXdNFn0dpAU7QOK4c74N8S2g3tTpMr69kTbNUgyT3PycvNZfenwodPjwU25TOfA9WPDOO1C8CL1_TueJBANJEacw7ZUpO7D8NM5hsYBYlgFJO2EYV5DFme-qdwXpkKCP9ZSPlWVD7TLTdwua2wShEms-ZJXjrymED_2HfjY9KftXkr-kskZWs1357Lnuow-0oeF-VTDdC6uUSPkKTOSXLbi9dhZa7GX91zo5WS_u0CfAXLJoReyDsFLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید اعضای کمیسیون اقتصادی مجلس بر نقش‌آفرینی موثر
#بيمه_البرز
در چرخه اقتصادی کشور
در نشستی به میزبانی بیمه البرز و با حضور جمعی از اعضای کمیسیون اقتصادی مجلس شورای اسلامی، نقش کلیدی این شرکت ۶۸ ساله در تقویت اقتصاد ملی، حمایت از بنگاه‌های تولیدی و مدیریت ریسک‌های کشور مورد بررسی و تقدیر قرار گرفت.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5108</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/696128" target="_blank">📅 16:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696127">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a233b1dc22.mp4?token=v0V03yTn6XUOoV2DlQ6lhid5zLH7bdLR2lVb9dh92Ghk3DUu82f3Ah6IZh4nm_TmH057EJcJvILOf5HnWYtxWBX_jbp4GoNBGvH0KUx60rI5VAJONjbXPWoWXpPhsB9Ch89Wu07EI3Epy0dLMlLTVpjZ_zK4RoNIHSntCb5dFesD2L_AD-Ah0Hjh4EL3_rU04EB8gGpl__lzOEnQLp0hVFMaGK_6fKLaFl7Gzy9Z6Ysl15ynJT-tzn1rWpGJK00GBrky_KaDYEHYlJdJeGl-vVYT0qpisXkL5m9Tc1IgSmuzGIxmaysCAsWie2I02teaGlZ48bXnKCb61FZEWtNI_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a233b1dc22.mp4?token=v0V03yTn6XUOoV2DlQ6lhid5zLH7bdLR2lVb9dh92Ghk3DUu82f3Ah6IZh4nm_TmH057EJcJvILOf5HnWYtxWBX_jbp4GoNBGvH0KUx60rI5VAJONjbXPWoWXpPhsB9Ch89Wu07EI3Epy0dLMlLTVpjZ_zK4RoNIHSntCb5dFesD2L_AD-Ah0Hjh4EL3_rU04EB8gGpl__lzOEnQLp0hVFMaGK_6fKLaFl7Gzy9Z6Ysl15ynJT-tzn1rWpGJK00GBrky_KaDYEHYlJdJeGl-vVYT0qpisXkL5m9Tc1IgSmuzGIxmaysCAsWie2I02teaGlZ48bXnKCb61FZEWtNI_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش موشک هسته‌ای فرانسه / ماکرون: بازدارندگی هسته‌ای ما، حافظ امنیت ماست
🔹
این کشور در سال های گذشته از جمله مخالفین استفاده ایران از انرژی صلح آمیز هسته ای بوده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/696127" target="_blank">📅 15:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696126">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV6Hz1gmVJIicz0Gl8vQvN7Q0hj1CqJEEb4r9mRx7ZraFgUURtNURSQtSLOZZ78xAtFEUMFgnX2hYOXPRjtToGuROe0CCgAzSBqbm9jVgbe8zqQqQwCrZDHl4jBFHQB5otyOUBr_pkZZ3wvaTT4ECJDS4W1mX3K4JOIQtcGSXoqZ_2bkm4rjV95gS8WN7JAFnN_GC8zl9xS6M5uXKjUU-3wOO2M06ru6PdovN7EwGjLzD5Tcf04udvfhWbIBZwynspu3O9f8qHZP-X53qDCOM9eF7xFxNsMh25BE9EyBVSSBf3p0YfQt_Q_Y0fMSeTcsgFNsoePxFbm0iB2dXgouGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تجارت دریایی انگلیس: یک نفتکش در تنگهٔ هرمز هدف حملهٔ یک پرتابهٔ ناشناس قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/696126" target="_blank">📅 15:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696125">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMUaQuem2reKDbTRf6h6oKTPyoAC9U2EFQosDuMxPy4b3xs7PjE88nK69rXQXDjOF5B3j7fGdRQh5BNTSoMf95k2l4gUmkPmfXqAJzeMDhWdysxkcYP1jgj5jfCw47oq7uBQPQJ1fgYg5_OJSdTJNYLx2venZ1n1DzSB98yxJafsCEaP8K_ZbkC1i21-Oxm8cvWcl-_uFFRMpSzwHUQNrx46HoMdDjEQw56wtyoZ4pONi7OV-RVVeQtboSm-wm5tP4x80RWul-Vu4jOFxk7OoCpkhqBmkkxggzEym4Kx4N56FoePPi09SLSEK_QmC1xbgBYGTy7oKx7i_HzefgXP-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/696125" target="_blank">📅 15:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696124">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
آخرین وضعیت شهر تعز، دومین شهر مهم کشور یمن
🔹
نیروهای انصار الله به رنگ سبز، نیروهای وابسته به عربستان به رنگ قرمز می باشند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/696124" target="_blank">📅 15:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696123">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2a0596e7b.mp4?token=d3klCwRXKcnA5cNMNMN7_ybpHrD8WInx72bVvLNALbatkyqRv1yyrMWn9WApJo8dqtVcyhVsEAL2Fbk0gupSjta6wj8ly8Fr-pIo668AS3KfJU_RpoT9R1JEvfgmYbjqlHpzsdIb07H5aRyJKVFFW0G5fQ0zbgF8IFD-ej3Z08hX0xHgSdnZcAEYgSpZCZPjV50JVDUVEnLsPGlVzhK9q5_cpxcp4r2uA8UCYDfoO7msysJcJkDSQohmOJNn28SSo_bi2BB4XgVbusXMXKAwrVodb24DJ-f7Y61OujjxPuLhMunmPn9DdzYCdxOj2ZUL0jd3czwnhXoIt5nGnziq-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2a0596e7b.mp4?token=d3klCwRXKcnA5cNMNMN7_ybpHrD8WInx72bVvLNALbatkyqRv1yyrMWn9WApJo8dqtVcyhVsEAL2Fbk0gupSjta6wj8ly8Fr-pIo668AS3KfJU_RpoT9R1JEvfgmYbjqlHpzsdIb07H5aRyJKVFFW0G5fQ0zbgF8IFD-ej3Z08hX0xHgSdnZcAEYgSpZCZPjV50JVDUVEnLsPGlVzhK9q5_cpxcp4r2uA8UCYDfoO7msysJcJkDSQohmOJNn28SSo_bi2BB4XgVbusXMXKAwrVodb24DJ-f7Y61OujjxPuLhMunmPn9DdzYCdxOj2ZUL0jd3czwnhXoIt5nGnziq-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند نکته آشپزی که به کارت میاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/696123" target="_blank">📅 15:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696113">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trQpuvh5H2Y2pokERyAbW6Rgvo8XmM6JW_-ffQrwXARfjp6XtGCzV6WFtkLJyatwVDIKwwEdTJUqzzn6mKRDZDXEt9kovHg0FC4tWZaihn4FkGI82pZ79cnkpMHeGx9PFnpESYrZJf9VvcsiPrcjzEHjrHv0cioqTUuZq3Wtc1oMNKB6EUoEslBPDdkvKs1DRKh1E7XieK-UwLr3u9Z3rmo5pnG7trmiRYoJtlmB636FQ7h6FgCeJd2XAZ-DIoMJnx9ZAiXlFHuIJ3Aye9DlrynbhWJmaVNL4bPYm1sZtqzNdfN57Pd-9kTK6xRrzgxr7J_Ad5zoRn2vkXatV_Sk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyUSjBB5OnVj6_MLAqR0gHDu1d73JkytNerUqifFg_V-o32mApgJPvR5nGIUYFidnSswGU-u8iAJz0GZgUM7cGbVmihhqrd90bsB0_9rrFj0HtyPfGoPd_YFNsIckzR-h_BTrFTwlP2xkymoE-EQH3m_nf8ZuLEqteScHvVzedGcI7NWbf6yd4VA9NGGEmAgB4nbe7Ki9Wlpxvo0V5h3Cpow2JdlnfiFTX7kdfQGPFOT3y6JjTKTJQU6fD1PzkTrkKUyg-YMQTZByQ-ars19BRPvVrmKNDbPTZnZ4qNbdlRYqpnm44MY-AQuvx3NtZ6jSvqgX3yXCCpuxSCEs9ohGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/US0rfheh-4J86C7W-Z40hIiZpV51QhbVV8lliJtZTO7X9nZMBgjXftfBP_AYIxibOW-qa9eKgDSE8QKV2etmPEy4F_r5coEbXn5dSm6Smg_Uz7tLfs_uMUtFhPVzy9pBa33LQIZxA2XRkgQwLsp946PsjPdfgLE8IjATYaDcwgmdaA6AsJeLs-JIMUKmW8r0-Z36dEl6FOhkQhl6c0wQnrVjHrEdDDbkIxNc1Ach3HpiqbDhWHHgbdlUHJwMdCaTLy6N0-wxz5QWDa5gfk93eiVg3PQ3PWtzGak6aqtgdAmi9cDz62B5zT3j15oEkZGcKdhFPynOiAXA2wg0R_MQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raUPzLL5PkdUEO6JkQkQqGAX8nq0UD_pPAdUrP2bFiPbEO1un3xM0rH9OnTDnfJym6SUYxXRTnaJlzB3ZLC7enQRRqV3vvfyc9Hr0GnejrOeLzB07hIPuEaWyQTG_FmRXddZet1-PHltDe3gGAFB0sbl62G6u6MQ7FMqKr7coAO3gk7YGOHYh3KiKR8TkcCpFB_GD2htK-ch3LEqI3oD77KlcRNiUyB_xxnUCvMd3ClSpbHv36KXqctxoF3KSKJnemTr9LvGZqO8hwDUbtB_ccIdGvLp5ZCoNTlTCqycYHIrS5QVD10p-JrFzn2CWK4S3nJ8fvXemoc34xHmtSJOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjPYbTsvZP7Ij1EvgZrGXvRNKgcQwleqJj1TjBzA0DpPiKmiiJp-NVEM0HPt1-a78JIlXveqobEKVvbmBlZxpD8p1guLFtWzgE3P4OzCGXr9lBHXpBEoIQMTUcVWcm3lAfiN7mYRdU04rnTgbMvWsOcZ_3QAgqmVnB-YaXDnWTjgUewIFoBz2MzuEwm3RALPxSJNENAwt57estnjFjNN7lIup_-3blEvJ1hybnViJq7uLuLUcAdjHJp-brmo6V9tzZh-rL83wVmPvfm80r3T0rvtQ9NIk0TKvhSFsv2ElvkUFQzzS2xljhpKbHS0yRuF9u2fRg3wRRcqs43cG6yT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bi_LOIOIu0dmxD2Lhz3MKv3zip0B_gdDyjWlLZXTpWgD6GIcLjMi995R8oTqB7rC9IYmqLySFS2awHVUCKb0IvWQMZdICSwqG_yHPzc5m5COdckgARn7K5g0GeDdCmxSCdvTsc6i0ISk7C5T9k0_IfX3HzzbUHm2zsK1Kmgvq2A0RQcEeCRywyu1jMutkZUDLvnNTYcoDpAwFyIblcJjSBNKIdI_Xe0O5b7ND9Q9Ts-M3BUNohThDc3Dn4Y3BUtTbgYIf4pDCob1QmKiAvgLh9tW2lT6gIk0XIIhQrGKU9FdywX97uBUpXFYNd3PlHrR01CEZ_ruW4TdZPPojH1fYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgWEmOsp1y1We-kdk4tR_dabK90HxIU2DjbHxLNlKm4jReM3ZxBPz-lws6G0mPQ-PbnKyBnIR2ICWabUCw0qD5q8RcHxfkSbyUiSMBTLhl6PJuyEel24zymsBywpphYKcGBXFrdE89sUBbf6oS3RD9F87JaEFlLawjzEzDrj9wkTkC-hWbZd_q2HfFPU7WpoB10PWL1HVmyJwN4DnTqWTCOgK61x9y8MTrFMw1dLfUPbWCEtyNzzPtj38ZYCFT0-A_xGCsudV57PeQLipAl_bD8agc2pCAMJRFZNBwBuimXkby9nnMJf6dVivbKt9IGOLoTE9l_JnjTwhlWXk-A-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sip0nLsxfRY-8o1_Ry5iTPMtXRtr48TLThn6nHWOd1aPTiCPfI0HYzXy5RMI5VvLqsTo3_cjFAHug0qDdBWqeakYVJztVvmPQ7qxJZv-EhEmdDkZxM119lcDJ6e6o-PKPd2A-bG7chtuBI-nF_X3YMSW_Mons0ONtNmlS1y2I8RjVUE0D4qbpUxDknd31cav1NNP6UZHdoATyLcaFzas5qUmTi7GSiJHB8EIS05XCrTyjzr9t97TnX_R0kIuGhPw_3m8es8P6E7EyNQGSjPxnG1ifj4wTEA4G-aH7FQNcqLNC6MWsNNVzPNQ5qTJQ_HCIpaVkCOqz5A7JYszcB7GBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSD2Hl44vI1CxcnIJ2aeXTJrsWaJ9c0rcAKPwV3kwOXjTGlSveMUFnoU0bSTwD0PhAHUcDAd6JYXPYFExjTVE4BV2vCub-R_3G8DDWkhz9mm9vQXlbCS9iM4gUxiHrQye5a3Vq_hItlBXog_bQLAyqjC2WQaDzFUItYJAbTtsnXt1fRkMDjy0RYaWD-xZcsNZuWd5HxUqR5ePBGIARMHxJu6-m4IWJMsXzxpeRqFf1eWnPyQitFbZrph5MI-bB1QOcTDfaRplZOwPi9tDeOrDzHI2_B_oubpsfv7z0cdBwDjeGlFw-5rIA-J4BFV46nOHwM2fERiee4f2qC-E0aduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpnEyK1e4NoDlOUm3IwR6CKTZxYGpd12xGm_Q5RAVn1jRwh5tfLhCTi7QvijDI1aCucrVd_SPngGwBJqKG9CNlDXw9daGESNU36jk9ZzJ67FOQ1AiOIepcAgtVykPh-jS2myn9q89WGHFUj73wyvyp7rovZOOGsvHW8WsXReqTFbwVIZ6_IKwE80uFILvnQm7xboJVIAR7lcMYZ_dfK4Wkhko8d5-p1BXDCDajwl-T3M6d3Fxq-Xl8MUKuF4iH56-s8_VjEbakx7BQ0PxZEg-hepsnyaJbJzcacXDsRVs8V5x2CDcVVtA3XsEh09qZ9PFoOS4E3I5LQCS4Y33lXMRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از بزرگترین زنجیره انسانی جان فدایان مشهدی
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/696113" target="_blank">📅 15:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696112">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
عارف: ما به هیچ‌وجه نگران تحریم‌ها نیستیم، زیرا کشور در برابر تحریم‌ها آب‌دیده شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/696112" target="_blank">📅 15:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696110">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGxhBoW8Y76o0k-Ma7U-Y3TlvtMgAXWRmKEuLCvaOBOiy7Otum6JXfeej9qEVak3Wbx_6xs1YR3ojdEPQi1i_q5uVN36oozU5U78DoEfSPXSlvv7oxMbx4FG0odhdToGXBdtLf6UShhdYccuwkLXhNo9W_BszaBrqG0AGSTGBJmnoz9Or32RQlyq_kfEksOqlR3gYWiaBNgGvhFDTyX47HDyRHXhVmdB3YWArmHuTpwsyWLoB0lHRRZ_JxNJ8iSk6DmHjTPE82UsM7RnvS6qNKbSb3JYZp3Xs_2FJcoVhKmAZHqURcvSKU-5ldykQLu_a8MsSext0xHnnxEk6qfdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برند اکتیدنت در کنار دانش‌آموزان رباط‌کریم
اکتیدنت در قالب برنامه مسئولیت اجتماعی خود و با همراهی خیریه نوید طلوع احسان، مهمان یک مدرسه درمنطقه رباط‌کریم شد.
در این برنامه، دانش‌آموزان با حضوردندان‌پزشک، با نکات مهم بهداشت دهان و دندان آشنا شدند و در کنار آموزش، ساعاتی را به بازی و فعالیت‌های شاد سپری کردند. در پایان نیز هدایایی به دانش‌آموزان اهدا شد.
📷
اما این فقط بخشی از این روز بود...
روایت کامل این برنامه را در اینستاگرام اکتیدنت ببینید:
🔗
لینک اینستاگرام</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/696110" target="_blank">📅 15:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696109">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d30c47a03b.mp4?token=HcTgLdnIfgDdpnebpxar2cZmN94lstcQtP5mn3xFy_D0uKIcn0Z4b-dU3ZI2SGhuFqnJ2xSlv6rim7dlYWfm27zZhTlvOMZJs9GcxQBSsdSXZ_jHOYJiUEbCYEPYFbz-3SBc6BkwY4zKJjZ79zeBsUGnPEFDlb8qoqhVlE_NwEJ7dkbY3nFExXTV88j_HHmId2CxIKHEgLvy_wqnXZMgz1G-wiiTJwvhlmmrXBIvs9Sfu8B7A7PgK3MzwCNiuJhuNnwYDhA8JlbjfHwGtS1U6cHy_VjJsQ9zrRIesNGKgD0zuMTCy0yZe4Usx_W6JmOL69TfYcv_irDdZZWTGpAGBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d30c47a03b.mp4?token=HcTgLdnIfgDdpnebpxar2cZmN94lstcQtP5mn3xFy_D0uKIcn0Z4b-dU3ZI2SGhuFqnJ2xSlv6rim7dlYWfm27zZhTlvOMZJs9GcxQBSsdSXZ_jHOYJiUEbCYEPYFbz-3SBc6BkwY4zKJjZ79zeBsUGnPEFDlb8qoqhVlE_NwEJ7dkbY3nFExXTV88j_HHmId2CxIKHEgLvy_wqnXZMgz1G-wiiTJwvhlmmrXBIvs9Sfu8B7A7PgK3MzwCNiuJhuNnwYDhA8JlbjfHwGtS1U6cHy_VjJsQ9zrRIesNGKgD0zuMTCy0yZe4Usx_W6JmOL69TfYcv_irDdZZWTGpAGBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی شیشه می‌ره زیر پوست، واقعا وارد جریان خون می‌شه و رگ‌ها رو پاره میکنه؟ #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/696109" target="_blank">📅 15:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696108">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6b2a493d8c.mp4?token=qS8brR-KQeeqE9rvQheF3b2rfJ_32q-IJpAjGYGkAl31ulnlpUsi0W0jonVTC6WvjI-YJGR04SCp8_iC4Cgbd13sncR3BszJKHMIWsJ7A_AXeq90nWAvaQeT2cfuOUeK3ycqPKcoyOZts2NfqxkfEkkkJ_28bSpjiUXXsa4MDdc1mysBoZEgd8PC-bZv5dCF6ToFF6TCvXo5OygM0mNZynuDaePI2zhz1uvohu1g3g_eIM8FH8thYz6JdL-GWRm-CIQ3JLdYLMwc6aqMLnKUXJU-ngQ7HvpQZqqx4hrctYi73TOwAu95njcaD6uR7YHRo5bzdCN0qvDTMcbaPeC9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6b2a493d8c.mp4?token=qS8brR-KQeeqE9rvQheF3b2rfJ_32q-IJpAjGYGkAl31ulnlpUsi0W0jonVTC6WvjI-YJGR04SCp8_iC4Cgbd13sncR3BszJKHMIWsJ7A_AXeq90nWAvaQeT2cfuOUeK3ycqPKcoyOZts2NfqxkfEkkkJ_28bSpjiUXXsa4MDdc1mysBoZEgd8PC-bZv5dCF6ToFF6TCvXo5OygM0mNZynuDaePI2zhz1uvohu1g3g_eIM8FH8thYz6JdL-GWRm-CIQ3JLdYLMwc6aqMLnKUXJU-ngQ7HvpQZqqx4hrctYi73TOwAu95njcaD6uR7YHRo5bzdCN0qvDTMcbaPeC9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس رشوه ۲ میلیاردی را رد کرد
🔹
یزدان بشیری پلیس قهرمانی که با کشف ۱۵ کیلو طلا، قاچاقچیان را دستگیر و تحویل قانون داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/696108" target="_blank">📅 14:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696107">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f593bc51c3.mp4?token=mTciq2sE67SawmfW80GO-757xtGFovxN6rW6UBIEkoA6t4Qn-HOUvrqAJnhZm82l448ytv0BJ8HCA5YBTgtBn9IL7mYPCjrEmT6_C1P--CszXzHEUrVGBk4TtMkSIoBDGNfoQhrUqTy3CH3pmqdcphlwJq-ONm6Th4iibhqg96ruKRNtc8ItxzoM0Mc6OxEQGhTe69YtLXBe7hYyebG3Nq9IBaQ-5cmqUDewdjWhmb7agV8yVEaPtVb44Xo4SUHA-cI3hij6Jv9zWlQr72zc6Pq4OnMlDkEXJXcUvPhZBsIB3Jajm70y0FA2HDggXsvbybQKWuvWFAMOV4JurTj7bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f593bc51c3.mp4?token=mTciq2sE67SawmfW80GO-757xtGFovxN6rW6UBIEkoA6t4Qn-HOUvrqAJnhZm82l448ytv0BJ8HCA5YBTgtBn9IL7mYPCjrEmT6_C1P--CszXzHEUrVGBk4TtMkSIoBDGNfoQhrUqTy3CH3pmqdcphlwJq-ONm6Th4iibhqg96ruKRNtc8ItxzoM0Mc6OxEQGhTe69YtLXBe7hYyebG3Nq9IBaQ-5cmqUDewdjWhmb7agV8yVEaPtVb44Xo4SUHA-cI3hij6Jv9zWlQr72zc6Pq4OnMlDkEXJXcUvPhZBsIB3Jajm70y0FA2HDggXsvbybQKWuvWFAMOV4JurTj7bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاسر سلیمانی، نماینده مجلس: در تاریخ ثبت خواهد شد که ۸ ماه، مجلس یک کشوری تعطیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/696107" target="_blank">📅 14:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696105">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23c356164.mp4?token=E9IM0gn09W1qUeoZXlHyyPNw7JzhCmNpyKAAeZuLesCxpxU3r5pHI_TTWkrVdGPDe05bjWlZzFvoxhysctMrtw1T3TprZGq_FK6rdpxojK7V7QwdL0eRfNOrBxvPjMKW9Pxxzh5co8Lm-TTg78msF8bNU9FoTrE-ghYWaLHo9N2lX24Sm9G1exsdDhMLCRKHD9Z1TVqE7d24e7h6XvtRV1gH7nTkF2CKfQFC-FVnNYF1V1YZ99EjtJXtFT_lZz-UUhQKrMNPNm0roAr_eig0K0DQ4DVVheqmNgEQ11kM5BrqO9Hkjg0bxCNMCFckhqsAJACWwJSU7G2I13kKi2GY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23c356164.mp4?token=E9IM0gn09W1qUeoZXlHyyPNw7JzhCmNpyKAAeZuLesCxpxU3r5pHI_TTWkrVdGPDe05bjWlZzFvoxhysctMrtw1T3TprZGq_FK6rdpxojK7V7QwdL0eRfNOrBxvPjMKW9Pxxzh5co8Lm-TTg78msF8bNU9FoTrE-ghYWaLHo9N2lX24Sm9G1exsdDhMLCRKHD9Z1TVqE7d24e7h6XvtRV1gH7nTkF2CKfQFC-FVnNYF1V1YZ99EjtJXtFT_lZz-UUhQKrMNPNm0roAr_eig0K0DQ4DVVheqmNgEQ11kM5BrqO9Hkjg0bxCNMCFckhqsAJACWwJSU7G2I13kKi2GY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تومار دانشجویان و استادان مشهدی در اعلام آمادگی برای دفاع از ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/696105" target="_blank">📅 14:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696104">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای روزنامه عبری «معاریو»: برآوردهای قطعی نظامی حاکی از آن است که رژیم صهیونیستی در آستانه انجام یک عملیات نظامی در یکی از جبهه‌های منطقه قرار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/696104" target="_blank">📅 14:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696103">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
در فرانسه به خاطر اعتراضات دانش‌آموزی اینترنت را قطع کردند، نت ملی هم ندارند، حالا سیستم بانکی هم قطع شده و مردم نمی‌توانند با کارت خرید کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/696103" target="_blank">📅 14:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696102">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: ظرفیت تولید تسلیحات کشور نسبت به پیش از جنگ تحمیلی اخیر ۲.۵ برابر شده و در برخی تسلیحات، تولید بیش از ۳ برابر افزایش داشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/696102" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696101">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311d9d7cf3.mp4?token=cCQzDmK-PeyHhQPJBLoP35JMZbJ4hipuc9oi5Qp8nwfnC2h0ZTQrWapr9CsLdUr1WzP63oSCtv0YnpmlRTXY3q9tniYVRjLtj7lAJCKaJNrnD5JdQD3kXUO3cz04rLkU4GpG-MvoDzxnAj4E-Tmx2vO-qbO9ac5AooIsUVgHm3fXQRK-_ixIkg60eg7prxrWk8Q9249-B5cCgf8ovP27Bq6nFHzW_LISMuwxj7lARgqzUNeuHfLbg7bDsgoS_E_iI7Vf0xWcFuJXj_7uzGXviYaKngbzbaZoE4vkJwARqMjt9X2WaDNjThrZHxShFXKpmE5KIFxOejGnnLepEpzWfDeATNiZGyZkawEBVoOyTigXUkl073eHBa37eanKVoXKOlVkqYhyySu_An5E5Dc2OqCkRyOaXNUotnAkSXP4xMLP3A7RDELP1o3z3Nox6R2zg08_0So8Dg-P_XGyOKsPDi3QYRFSkERcyAgzcTKN5VfgjxL1x5c6_j67E6blB2OubiyF09lflPNjC3h9mzWRMGU221u5ODq8Hw3kq953huBPAwbloyx173gSewUPTqJt9W93Ryy7rTPCJOpxV0WkbjllylKWqAh4MRh33KcYegEjdnwqBMrR768522nKeCaBvcUFT5NZyoNcPG5KBHwhEjXSr9kwsa-MNpvytgtYLCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311d9d7cf3.mp4?token=cCQzDmK-PeyHhQPJBLoP35JMZbJ4hipuc9oi5Qp8nwfnC2h0ZTQrWapr9CsLdUr1WzP63oSCtv0YnpmlRTXY3q9tniYVRjLtj7lAJCKaJNrnD5JdQD3kXUO3cz04rLkU4GpG-MvoDzxnAj4E-Tmx2vO-qbO9ac5AooIsUVgHm3fXQRK-_ixIkg60eg7prxrWk8Q9249-B5cCgf8ovP27Bq6nFHzW_LISMuwxj7lARgqzUNeuHfLbg7bDsgoS_E_iI7Vf0xWcFuJXj_7uzGXviYaKngbzbaZoE4vkJwARqMjt9X2WaDNjThrZHxShFXKpmE5KIFxOejGnnLepEpzWfDeATNiZGyZkawEBVoOyTigXUkl073eHBa37eanKVoXKOlVkqYhyySu_An5E5Dc2OqCkRyOaXNUotnAkSXP4xMLP3A7RDELP1o3z3Nox6R2zg08_0So8Dg-P_XGyOKsPDi3QYRFSkERcyAgzcTKN5VfgjxL1x5c6_j67E6blB2OubiyF09lflPNjC3h9mzWRMGU221u5ODq8Hw3kq953huBPAwbloyx173gSewUPTqJt9W93Ryy7rTPCJOpxV0WkbjllylKWqAh4MRh33KcYegEjdnwqBMrR768522nKeCaBvcUFT5NZyoNcPG5KBHwhEjXSr9kwsa-MNpvytgtYLCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدرت‌نمایی نسل جدید هوش مصنوعی
🔹
هوش مصنوعی هر روز یه قدم جلوتر می‌ره، از مدل‌هایی که  از مرزهای امنیتی عبور می‌کنن تا دستیارهایی که می‌تونن خیلی از کارها رو مستقل انجام بدن.
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/696101" target="_blank">📅 14:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696100">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667dc38fa6.mp4?token=hT5_wlTrEsuCSbhZjctSkZRWB61YFrn223snWIs1d64-YH8gmqIrRZBZbdv26KC73obf4sn3T88VE8uo2zIXpSxeCiJWNRb8hu5Au1-aEjQXuD6BSt34iYnHQWw1Y7pOxl_Zclwp1ZpUL47EcZoRUv-0MV9hsvexBhKyrbEy5jol5NopUa9NHJw685TbTsJaSwxWswnpmna1NvD2uazo2ajq_Z8nZfKGLplnHIWKLdUcGKwBd4oM7BraYikVTIz3Et6hojtzl2dE5eq-etGCwsy8GR4bT0gqjfF5bTMsvxCRDz8BP7YnNLYbAnq-X39UAuVeoEt947QpN8vVt4UEiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667dc38fa6.mp4?token=hT5_wlTrEsuCSbhZjctSkZRWB61YFrn223snWIs1d64-YH8gmqIrRZBZbdv26KC73obf4sn3T88VE8uo2zIXpSxeCiJWNRb8hu5Au1-aEjQXuD6BSt34iYnHQWw1Y7pOxl_Zclwp1ZpUL47EcZoRUv-0MV9hsvexBhKyrbEy5jol5NopUa9NHJw685TbTsJaSwxWswnpmna1NvD2uazo2ajq_Z8nZfKGLplnHIWKLdUcGKwBd4oM7BraYikVTIz3Et6hojtzl2dE5eq-etGCwsy8GR4bT0gqjfF5bTMsvxCRDz8BP7YnNLYbAnq-X39UAuVeoEt947QpN8vVt4UEiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا
عطر با ادکلن تفاوت دارد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/696100" target="_blank">📅 14:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696099">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2dbjUpNzFfE2n1PIeW7RsUnO_3Y0H9X4OyhIqaUmD9Qog_bkFRbJ7REe9ipn6RKfYNHLMn2z3ptPSalNvC22f1DPl-r11cPOKEvlJN2nADZBA0IXf1wL9Xt4nG5tIlTgGdXXFWcZokzqDL_494OUnUg-KMftlMPQt3ZVQXknLkJwB_oNDGGPkyuFEBVif10L7l_NZpFIIEJyzt9tovSe64S1uk5H4ZGQymgmg3ypzaEsDAjeBtm17Cfs5ZzS8aEHQnze0eeOS8dcDJ-C4YNXhc-p0199s45IotCS5T7-7D2p52YfeZR0eA8BER1en7DJqjYuNCBmbczxhkM0CRL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شعارنویسی‌ها به خانه ایمان صفا رسید!
🔹
بعد از رضا کیانیان و تهمینه میلانی، حالا جریان شعارنویسی به دیوار خانه‌ی ایمان صفا رسید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/696099" target="_blank">📅 14:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696097">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sv2n0CmptaWjjBDFSOXCjSW8Jk4nKuTMSUN7Bx1e7iEMasRcE9_sV-AeTiLlnk4jEKpJ2UBgena4uH2TVwGKuTGSX6nf1Jd3yEzcAq_yHKf2Q42oJnGe45C9kWh4Yfz6rXw_GwlNq46m3gYoAbtjXz8RxqLVYuuJcupZkEZZeMkDF9yAk8D9LiSxoXvkY8BqEooc2qLeR9fk5_uzXvGaA9mCiLtTxi5Wacz-jSQhPErirOrXLX-HbP32HnnQ440mXEJXG3t2gAaqJJklr9yGWXOEUeV8glP7PpT-AakbEDVzFbZ3qiIY4ZqmVik11FqosBDjAdZL4unxF4kzmML7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910e633a10.mp4?token=BSrojcbbf_LwralB52Dzs75UQOJkRSleGQtljMfIFg7DRKy-eXzZ4vWJ1xmEJnGgCIpUBn7fwLajzrEQ5a4HYIvRyW7fazqTcBt7ooAPudf3aSkOMvnEHkdDU7ui-HQzjvo9ByrLxVL91IA7Az4bOZ68VVSSxYIFsDZNvePaWUcAlNl_bie4m1jUGXj1g8ZBYeC4azqPC4kEwxQHrpbZMtOtp7W9YHK3nnvxlwpLfBKuvg7RMaMCxpfqbE5-WSfUAv49jh6rY8_ZY_ntt1RuweoNY2Zjz5BfJDRxyptsaZ0tkHs3RRI6b-q7ID6ehS4LMO9sdfbkoCtpwEQZlf1okA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910e633a10.mp4?token=BSrojcbbf_LwralB52Dzs75UQOJkRSleGQtljMfIFg7DRKy-eXzZ4vWJ1xmEJnGgCIpUBn7fwLajzrEQ5a4HYIvRyW7fazqTcBt7ooAPudf3aSkOMvnEHkdDU7ui-HQzjvo9ByrLxVL91IA7Az4bOZ68VVSSxYIFsDZNvePaWUcAlNl_bie4m1jUGXj1g8ZBYeC4azqPC4kEwxQHrpbZMtOtp7W9YHK3nnvxlwpLfBKuvg7RMaMCxpfqbE5-WSfUAv49jh6rY8_ZY_ntt1RuweoNY2Zjz5BfJDRxyptsaZ0tkHs3RRI6b-q7ID6ehS4LMO9sdfbkoCtpwEQZlf1okA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طعنه سفارت ایران به ترامپ در روز جهانی «فلج مغزی»
سفارت ایران در زیمبابوه در پیامی در صفحه خود در ایکس:
🔹
۶ اکتبر؛ روز جهانی فلج مغزی. برای همه بیماران مبتلا به فلج مغزی، از جمله ترامپ، آرزوی سلامتی داریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/696097" target="_blank">📅 14:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f46eebc4.mp4?token=aJpohdAMRhCN7b7o55XGo4Ma3hsbwjWDMlWCfdfoCE5_BhUZQJkbdZ-HwPne0HXt7fMk6xXC8rXdWbiiL611oDc6U-3H6biQkc_CDLCSY02Ym48trQ4i8-uUrmdrmzBTq3SbmXk89VXEV7NDfnZkq_r_vxt_7aBkvoZK8opotf7SB5kmCunZvy8hAaWFXCBqCh5tQERwhBS-EEduKVGxoBHOTzsAazopUVqZkPcIXx0ScU33TzsmFXYGmIsk-03zxH90XQG1L8p1MRCQAmrhZ6cE-XlPleI6nZKZkfGru7Avb2r50hwBiaytst6SC8V7xUdwDRsPLgz9jDHu0QxoWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f46eebc4.mp4?token=aJpohdAMRhCN7b7o55XGo4Ma3hsbwjWDMlWCfdfoCE5_BhUZQJkbdZ-HwPne0HXt7fMk6xXC8rXdWbiiL611oDc6U-3H6biQkc_CDLCSY02Ym48trQ4i8-uUrmdrmzBTq3SbmXk89VXEV7NDfnZkq_r_vxt_7aBkvoZK8opotf7SB5kmCunZvy8hAaWFXCBqCh5tQERwhBS-EEduKVGxoBHOTzsAazopUVqZkPcIXx0ScU33TzsmFXYGmIsk-03zxH90XQG1L8p1MRCQAmrhZ6cE-XlPleI6nZKZkfGru7Avb2r50hwBiaytst6SC8V7xUdwDRsPLgz9jDHu0QxoWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو پارلمان اسپانیا  به فرماندار مادرید: آیا فکر می‌کنید مادران ۱۶۰ کودک، از ترامپ برای کشتن دخترانشان تشکر می‌کنند؟
🔹
علینژاد: من خبر دارم خانواده‌های داغدار به من گفتند از این که بچه‌هاشون در بمباران کشته بشوند خوشحال‌ترند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/696095" target="_blank">📅 14:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c7bafe0d.mp4?token=AL5bKqIwpZGfJXIPr1gWk8vT3q8FSH_aI3mcaD3OudrI0ODT7UAsXNr7NgCRo-JjG-hK0WedlH9wdX7zQPCafKZ-Hpk5auVsCLMqrmVJoC6gpouaD6IyXbi45mgxW6THhO0EgQ6G-P_a6MqZWjKDFkECVOGM0atrBU5nUe-8f_pgCXATwhP6qxhJZAfUy-4Mdecw-zDgN0LHgTK77MjZeNlUSvfKtLh0cElVhkZORderbOHEARwT_XIIWBlEEZbqKQBSP4cGV69KFPIJWNrlTg67ZHojPaohTqvRh63gTWe63oijNXYL7FEtC-KAnLbcYvpbK6_-orYVQHZ4Jou1mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c7bafe0d.mp4?token=AL5bKqIwpZGfJXIPr1gWk8vT3q8FSH_aI3mcaD3OudrI0ODT7UAsXNr7NgCRo-JjG-hK0WedlH9wdX7zQPCafKZ-Hpk5auVsCLMqrmVJoC6gpouaD6IyXbi45mgxW6THhO0EgQ6G-P_a6MqZWjKDFkECVOGM0atrBU5nUe-8f_pgCXATwhP6qxhJZAfUy-4Mdecw-zDgN0LHgTK77MjZeNlUSvfKtLh0cElVhkZORderbOHEARwT_XIIWBlEEZbqKQBSP4cGV69KFPIJWNrlTg67ZHojPaohTqvRh63gTWe63oijNXYL7FEtC-KAnLbcYvpbK6_-orYVQHZ4Jou1mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بعد از نشستن طولانی، زانوها درد می‌گیرند؟ علت و حرکات اصلاحی را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/696094" target="_blank">📅 14:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2nD_eCDrb4DthQy_be83zVkeRlHsLa1rx1bYQI5UzQ48umugHvab4-_wmySaUhhm0pIJQDALKtszu4Pj05d72aW7QfYorVxya-6ai5-3ney0D_enbbHnBElx0SbDqDnQ3VpZesccqx-peXN54r1nJM0zTNMAYPPPCm0D_SSH1PGDxgPm8IcjGJtSkqA-G_S-3VnVylUtnFOZuxtRLqyFnQgmTY2Oj1rb5oB2TPjAvZpQMvQ-FUKRc9n0LDrqhx4FaivjafBCLDxxtyrs7Ay-O_XmYSCj2MXglSjuXl2C4DxuKAgZ7tUiRQgml6QIdhPW76SCLtHq7kXeo4kdUQr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrObYy5-XZuALnOzNhxRkttXQamMCEMD7X4j9wy69q37eiVeCh6ySx2eEtprS3pxq5lrtCsWf2e-Bc7pycuVQm7R9-rUgutvkJBGM98rx-22sfmjspy1XDBoI8pN9V5jpKhQqq5a1CYwlWzz3QAHPxdSrElfB_Fl9Fx8Au6brUDJd-_0ZXr7ObZNRxwr4Azv0JJp4S7eXRxBHSq6Z7sg8c6KiKm_vEll7mzRFjI4-TpRl7T-6vKoem-gt_Qp9a3aD2TpkKnZVbVml-pa2xBVWG8eXqFFSG-YbNYeqDU5Sqk0-hZi21bPKkhP647BDT6GoAas_h62syP0jdhlw1f05Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juE4yOp4qF-x95QIPanfvRgqnsyh4XIdrvvXRorwHmR0sQXZGpBxUDHKtDA9OqgKZeD7EeoF3_PZnvpufWknfAB7LeP9Mk7XkIufZdwvfd07tROENqR6qLEBXxLc-5oWZtckjxE7CFCU1ZAG_t5NKEGaYlU-NqdlWECQzC066Dj00P5ET_2hTgn3EiPQQle8i-feMHmjAxO1cPCmYgKqljNbyVYgir7I8DmbIqRe97WSiAtauzFlPzYOWXL4fsiSf46zldcvgXjFtd7_YUmuUAhzvlNctJV1IrWttzv7md5nQDpPpAkWmf6ASt_MXH7PnsNZ4VlQPMDxd8aHVzizKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gR08BQ32Efr8nSOp_4WXsCXdlco3Ec0AOJG8dfdI-VXicbqyQt9u8sTCNXUqx08oOOOKZfF7Te-_zrXzD_R5aJJ0Nel6JT90VHLTwTPWDq1ZoIcbKC-bHdoty3mD5BAEs5AzcIAZZN2ngf5U3BM-EdA9TZxcG5-1dkfc3Gra6T5eb8ivWNpaYxThO7RK6ABRuam7ZLQPUtMamJn6xKPWW4PLfu14aujT7H7dthCoMAhMm2fA-4PwJL3vUnqiEmk45S7WK1_U0mK5juhEhMH5GswRt32NwlzOWsoShf2iu_3H1AlJ7DdzuWtEEXNhggYCyLpGeehKII9sLC2GBn2VTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fK71oz9MZe_Ilon0SK5LSLWLDkwg2bOELP5oxsJjS9wBvxERNXx7gT1cskDspOVLSLs5_KDDpD7m7mKCgZ97CY5Narp0ooSjdQPtr3F_eelGI9JKRMVq3ZRfCos_2TRg528yfCPehL3F8v5lpH1SJByBMQw_CEVf-J81kl0YA0EtJc4h9eRF3z1TlgdeRrphM3O-5_nEGMfKFDZGrqk4_p7mVDVw6YsBhSQpc2mXOIV2cbfeY-WQgmlXF_TXwYGRfoLpwoD0I7Vyi-VrMo-NP7-RQ36EtUF3d-7SRwSZqTaTekmZWQuvXleL4EL4ffLh7TWlVQmfQu4nmNsyFnkjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyP87VeFKFw75v6PGxII7BYWwCX-OTXRS0-CB9wL5tzNwTqPtq9CJs-phIDKIJZDoM49qOrbh4HyLnK9e9rCweWnHfO1Fhr1z7fnhyqB1XBWDWyViqvLgofafm9tlYbGOT5F_PDWkKKnchcrJcMMy2D-kn2bK8fLJuRtE9859BaWGW-sqFtus3NG3eNuWMnokGtsSKjA1JswSTqHQ-aLCF71yf8U9M_7l-NepkDL89dxOsSneBYqJkt-CydBzH9re5WsML4wpsCpPHJYgnlYPvTZg2mcRTfvDA8SFzAqn_JKDr8IMPat5FuG6tB2Cfnc-D5jSpOPZRNm6rKKLa1nzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از زنجیره انسانی دانشجویان و بانوان در رزمایش جانفدا در مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/696088" target="_blank">📅 14:20 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
