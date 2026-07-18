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
<img src="https://cdn4.telesco.pe/file/XsC6sW3Ug4EOkokJQpk_lMnxVg9_YQ0I4pzD-VZsv1pRr7dvE1TahgD4Brr_EZbxf47ZbsGbKd6K3AgHnImN6wUt4VZ8nGqlOmHEzKTUptt3oEB0AKU-HeL5Y3YLeB2LZFRCGsSul7ZKgIuELS1FMsDvFADoh8vOcBlxewx5omDIpF3zoCBX5L24X2lIlHRzrauF6-Oy_y-TaId4HRaV0aZ_BhaWIQFaZfbWE-ppm8oatz-G-iUXwNWAN2EOByoXic-e4iwxL3e4J-yaM24SeLM9YrsMiMBJ1oDPCdQG5FNx56XGii6V83gZKJ4CIEfKrnDOWIzqkTakku2YyHnuVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.29M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 23:29:14</div>
<hr>

<div class="tg-post" id="msg-672742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71053f856c.mp4?token=Y3800GHNLVb0_QXEmXxOpFakztZkeK7djuf8hjj9kXEjSP_169SoTlFXbIwAoBV1gM3a3QGyA42uXwPCaf_KCrs_r0enBf7LGBGWSdX9pJswswb0gtPQJ7rarT0OtpE56oOLO0RCzm-tE3wYTJF33tJuEBgUrfJyOvv3HIeeZKum3gKZ4SDzzaCjkrz7tTyFfSUob5RX79jRq2HVOkXCTJCBJAPQUuvXuB8dnw3GdDQIgeil6PNI9JuMSc2eHZniln2VVnL4RmT5GfDHi7fg2UXEIiEAMB7XBZuC0IIyHPEstmo2kjBgds0AshFyR83zPlQV0QLii1Y_9mAhFXMDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71053f856c.mp4?token=Y3800GHNLVb0_QXEmXxOpFakztZkeK7djuf8hjj9kXEjSP_169SoTlFXbIwAoBV1gM3a3QGyA42uXwPCaf_KCrs_r0enBf7LGBGWSdX9pJswswb0gtPQJ7rarT0OtpE56oOLO0RCzm-tE3wYTJF33tJuEBgUrfJyOvv3HIeeZKum3gKZ4SDzzaCjkrz7tTyFfSUob5RX79jRq2HVOkXCTJCBJAPQUuvXuB8dnw3GdDQIgeil6PNI9JuMSc2eHZniln2VVnL4RmT5GfDHi7fg2UXEIiEAMB7XBZuC0IIyHPEstmo2kjBgds0AshFyR83zPlQV0QLii1Y_9mAhFXMDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش فاکس نیوز از خسارات قابل توجه به تاسیسات نفت کویت
🔹
پس از آنکه مقامات اعلام کردند تأسیسات نفتی کویت در حملات مکرر ایران مورد اصابت قرار گرفته است، دود غلیظی از تاسیسات به هوا برخاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/672742" target="_blank">📅 23:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672741">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TanHNbYmGjybgXQlCJyqJabxA2b3cqK_1sQxwGLun4i2-DUgCWo9_tzdSthJfdW7ab1HcD-xp0dfJwwJK2Sa2viGgbGQubOa8B2lqZlTb5qww7Dtz4pq58f1X83k1UqvTAbE2ajaQIrMEuq_1n0P_KdGaFiRS245PyOW13zBTJHtrCdXPcZP5afKv3Sf5jehJlV9a6pdtcAYrioqTmIZ9pACHQGML00atWt3vKCcwpStsqmPfJ1ArVQPep0AsEeqUgW3GkDqavhC-jbC2bfZVLEnBUmsicodKk1n3AwDnhmvtcTIQge_btoU45DUP0ycEipCM-EFMyAixeFIzsYMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملات هوایی مجدد رژیم صهیونیستی به جنوب لبنان
🔹
رژیم صهیونیستی روستای «کفر تبنیت» در منطقه النبطیه، واقع در جنوب لبنان را هدف حمله هوایی خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/akhbarefori/672741" target="_blank">📅 23:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای خارجه ایران و عراق
عراقچی:
🔹
روابط ایران و عراق نباید تحت تأثیر برخی اظهارات شخصی و غیر رسمی قرار گیرد.
🔹
ایران بر احترام متقابل، حسن همجواری و توسعه هرچه بیشتر مناسبات با دولت و ملت عراق تأکید دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/672740" target="_blank">📅 23:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672739">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
آماده‌سازی همه‌جانبه آمریکا و اسرائیل برای حملات گسترده به ایران
👇
khabarfoori.com/fa/tiny/news-3231341
🔹
بنزین ۱۰ هزار تومانی در راه است
👇
khabarfoori.com/fa/tiny/news-3231318
🔹
پیشنهاد جنجالی مشاور سابق احمدی‌نژاد درباره پروژه انتقام
👇
khabarfoori.com/fa/tiny/news-3231310
🔹
علت نرفتن تندروها به جنوب برای جنگ و همراهی با نیروهای مسلح چیست؟
👇
khabarfoori.com/fa/tiny/news-3231169
🔹
این سلاح کوچک تعیین کننده نتیجه جنگ ایران و آمریکا خواهد بود
👇
khabarfoori.com/fa/tiny/news-3231295
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/672739" target="_blank">📅 23:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhzn5MlViXA-KIcySuOhuINLAKSGW34EQqZhLVSx29LydvNxxhTmvyza2ns9usqe2XyfeVHDuLSsB569vfUOazlZRx0KX3jL1eD7AgCUrzV_WIAwFCI24IrNWlMOfgulSAQnDPw0T8hK6ap8uxVviKThL-2XyJy8XfaIbSXUr6wyfWN125F1mdX2KH9WeFuJlZ-T9qqAFG7wkemkv1Utq39Vg8eRjczKGlvSVhQLFptC4fmLkUh5up3Effk_ZTRWMQH-CRXyirmqscQJh8sX6sdbZv5qZGs_ehY8kRm4CuWIfXXcUpbzCFoTXQRfkRUMgxwm2N30HaFNghJ1DEmUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم مؤمن عراق در استقبال از قائد عظیم‌الشّأن شهید حماسه‌ای عظیم و پرمعنا آفریدند
🔹
به محضر شریف مراجع عظام، علمای معزّز و اساتید و فضلای حوزات علمیّه و دانشگاه‌ها، اندیشمندان و نخبگان گرانقدر، اُمرا و سران قبائل و شیوخ عشایر و سران طوائف و مردم بزرگوار…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/672738" target="_blank">📅 23:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLCw0AB0ZGhus79-fZOP96KlLVH6EafautKe53qaeFlqKfnABKzjCejd9O7t2TV-83GJgn4_VqyFvriGqpdlhWir63mwEBEaBswvfhoTRXopuOB1QjtRpSC3RQo7wKT1ymU2L6Ms15Q_2BTjRsrL80IqIfpWbssjBJ29E3L-kSUYmQBDcV7foJfdZxl2Fl_avBk9iDYuSQ9FGwUapALqe0CtB6yZuBUw856bLlBHgwZFHn1Bce31KAgEPgg66nGOQaLAotsPUqQPOn22WthTeDUA4W1nVLWs4X2aOfach9MF2cPuNfGRfdanvj7ZJ8hkj95eQUr1pev59jerEck__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع میلیونی و بی‌نظیر علمدار مقاومت، فصل جدید تغییر معادلات مستکبران
🔹
این تشییع میلیونی و بی‌نظیر از علمدار مقاومت، جلوه‌ای تمام عیار از همدلی و اخوّت و هم‌مرامی بین دو ملّت عراق و ایران را نشان داد.
🔹
بی‌تردید سران استکبار با دلهایی هراسان، تصاویر صحنه‌های…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/672737" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZOlbIcrTqsb-vkk5Mc2dTu3dol8nAMVM0fOEjLY0elqAEOnRsO3vgo4gmL67lq3L6A621erzNy4pMBvnz8cBF813aILlbwUkMaEi-rL0rm5QZBoDGAuLjacs5AgjIR_sGX6arcUz7ZKgkvK5GbDil3Y6bZQ2uOZwOSbkK7PHkaGji_ao0ifLw08Hg2BgYhTzx57fNvQ5BwTHSOZQ1l-BGNr48BzrUIBGR0BkYFce0k7GPYwbku2TvyjoQqtttHKsucrYz0Tkf0tuGlqLrU3BF-MERUxpCfQ8nveC3rrI-SC0nZwDrYi9H9ht65ipGbnpgi0sNmPbvhv-6jNZYo3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع میلیونی و بی‌نظیر علمدار مقاومت، فصل جدید تغییر معادلات مستکبران
🔹
این تشییع میلیونی و بی‌نظیر از علمدار مقاومت، جلوه‌ای تمام عیار از همدلی و اخوّت و هم‌مرامی بین دو ملّت عراق و ایران را نشان داد.
🔹
بی‌تردید سران استکبار با دلهایی هراسان، تصاویر صحنه‌های باشکوه این اجتماع عظیم در عراق را مشاهده کردند و دیدند که چگونه سرمایه‌گذاریهای کلانی که برای تخریب رابطه‌ی دو ملّت به عمل آورده بودند پوچ و بی‌اثر از آب در آمد.
🔹
این حضور چند ده میلیونی هم در ایران و هم در عراق آن هم به مناسبت تشییع و بدرقه‌ی امام مجاهد شهید اعلی‌الله‌مقامه‌الشّریف، فصل جدیدی از بیداری و نقش‌آفرینی برای تغییر معادلات از پیش‌ساخته‌‌ی مستکبران را رقم زد. اینک شیطان بزرگ، امریکای جنایتکار فهمیده است که استمرار حضور بی‌دردسر و سلطه‌گرانه‌اش بر منطقه، خیالی خام بیش نیست.
🔹
بخشی از پیام قدردانی رهبر معظّم انقلاب از ملت عراق به‌پاس حماسه تشییع امام مجاهد شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/672736" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672735">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
متکی: با توجه به اینکه دشمن، هموطنان ما را به شهادت رسانده است، رزمندگان ما محدودیتی در زدن ۷ هزار تروریست آمریکایی موجود در پایگاه‌های بحرین نباید داشته باشند، ملاحظات را بگذارند کنار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/672735" target="_blank">📅 23:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672733">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rdojbL4GwW-08dNvd2cZhWZGHVRk1h0T5M6eDzecBdDeenWOn-u3UehoAmhJrI_yPIsxoH_Q1LzSybBD3lz4hWkK35B0T_akgg_DrnSaDJEWyHhlfZJxPLhHxipeq7MnXE58NkAvb3Rs1IPiztvmXtXAel_SejFCIrCvzBX2lFVkocUmly0vZ2G3Q0ofwxuEsk1gL_Q3MDjtIdsgRHgsy5AOX2ETuq0aZnGE5BJ-AITRqSFMZKraLTiH72JCaNa4sLQ0LNGukgw6dZ4KdLe7Hlbtomi1Pz_V6iiaZZOSBQwI0RJX0SnnuhKNjhSAdY8Rlky04t4S-FX_IzVh4iuagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBuGZskcW4k3_3JqJoI2ES1k-F-De0w9J6jiQxu72kYEOA8qbzsIOt0ZWlyKZTa5T2GcWrq6MIifG_tVktqebqh32xF_-HJNnj-fhUz57o68ZlY5zAbAlwScc0sYp_Rolye5M8MrpC9i7S9lJqpJ4c-OjpW23q01J27k879KhtYQOhtBMOUw791vc8Ni-2nUSThArjNGXReTsRd-6dhR0S1feGc0K4hWLLvMybIbhby0nVnxAmxjNdWw47IVlKUvZmgU_zTE4gRP6KuXFQDRO5YBAu6oCnSPy_ClS2r6Jc-QMGTijUT2noG4acskDhMIW-ZjsKjxSP5vRxLrGOe6cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر بخواهی فقط یک کتاب عاشقانه بخوانی، جین ایر بهترین انتخاب است!
🔹
اگر فکر می‌کنید عشق باید بهای از دست دادن عزت‌نفس باشد، «جین ایر» نظرتان را عوض می‌کند. شاهکار شارلوت برونته، داستان دختری یتیم و سرسخت است که میان عشق، فقر، رازهای تاریک و انتخاب‌های دشوار، هرگز کرامت و استقلالش را قربانی نمی‌کند. رمانی کلاسیک، عمیق و فراموش‌نشدنی که هنوز هم نفس‌گیر و الهام‌بخش است.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/672733" target="_blank">📅 23:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672732">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مسیر رفت بندرخمیر به بندرعباس بازگشایی شد
🔹
بلژیک واردات کالاهای ساخت رژیم صهیونیستی را متوقف کرد
🔹
فرماندار بوشهر: مردم بومی جزیره خارگ در کنار کارکنان صنعت نفت به زندگی روزمره خود مشغول هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/672732" target="_blank">📅 22:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672731">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
متکی: قطر برای تفاهم حتی ۱ سنت به ایران پرداخت نکرد
🔹
اولین محموله پهپادی اوکراین در امارات را نیروهای مسلح طی جنگ منهدم کردند؛ اوکراین در عملیات پهپادی علیه ما شرکت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/672731" target="_blank">📅 22:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672730">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
متکی: آمریکایی‌ها شعار اقدامات زمینی را داده‌اند اما ما امکان اقدامات زمینی را داریم، ما امکان این را داریم که یکی از پایگاه‌های آمریکا در عراق، بحرین و در کویت را تصرف کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/672730" target="_blank">📅 22:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672729">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae6fbe629.mp4?token=lw8i3mR5tDfFHOK7pf8hzsWxzgndE3xIvve4ZDLsYCRyK7cq8RT2UYKDMVDTO8ZCQ_Ds10F4vrxpPqQ2UlODa5wgnai8BEq3paisoppNu1dRhF5ww1Gm9EhqGIWzgkmqXlxLFFGuwKataRvgyi2XDuxgDFWZcAa86BFcds2o4m9ngAVlt6N6V-O_YBagTdwkZtSTaeb9BOaaYrSOekFRMAwcsmnyqJavg10eCf-zyb3-mG1Q59ZAkxrs1Y8vodtChBvhsEY4nKoDb3oLaa3AcXRLKZb6sCIxIeqX9CVY6t8fr665joZsa2bgB0EOHMTI6ERQbtjKy1MuM_4_S11SRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae6fbe629.mp4?token=lw8i3mR5tDfFHOK7pf8hzsWxzgndE3xIvve4ZDLsYCRyK7cq8RT2UYKDMVDTO8ZCQ_Ds10F4vrxpPqQ2UlODa5wgnai8BEq3paisoppNu1dRhF5ww1Gm9EhqGIWzgkmqXlxLFFGuwKataRvgyi2XDuxgDFWZcAa86BFcds2o4m9ngAVlt6N6V-O_YBagTdwkZtSTaeb9BOaaYrSOekFRMAwcsmnyqJavg10eCf-zyb3-mG1Q59ZAkxrs1Y8vodtChBvhsEY4nKoDb3oLaa3AcXRLKZb6sCIxIeqX9CVY6t8fr665joZsa2bgB0EOHMTI6ERQbtjKy1MuM_4_S11SRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی:  همانطور که مذاکره اول و دوم فریب بود، مذاکره اسلام آباد هم از سوی آمریکایی‌ها یک رکب بود
🔹
برای ما روشن بود که عمانی‌ها تسلیم می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/672729" target="_blank">📅 22:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672728">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E16X5VhaWLIcdwu8Ly6HcKoTQR0BeGwQwzY0pnMEfjMGQw5uaiAfTCU3z3bwfEEuf_9vstlzzEl4kTdktRYcDS7i7dArBBCG8EVI59xlc3Wp__IWXsX7MFSKQ-q-U5HLuqYyH9LJ0DARc2_S_aFpYtmf9SfA1BS3D6q8chbD5GM-arRduG9rJidgm76hZWlU8_t2oAR490GFZWVNWB2EawBU1qAb3cL--k2vtPcMDfs0sKvIQUQOknPDNNh11n3r1pP5eU7SPecCzumaEbUy6FlW3zpCBQkiq9ckoP8Egx-hks1XPvn5xorgb_gTxgwcGfmeNb7Ldt-ZcXjm_9vtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر ارتباطات: خبر قطع اینترنت پس از جام جهانی با دستور قضایی هیچ سندیتی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/672728" target="_blank">📅 22:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672727">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQWXC0MPYIzdndRVXUufYdz59mm39sGnfde5ArdZ6xmpsCrRQ2XeJa-NvWiLfgg4BAHRaEWJIGQtyxIQgmHjKRhOxgMVdyHDnjnQpd9IKC8SDotoqUrAQ-VtQknDKZRExad4RRXsof9ovUtPx_eay3LOdyz6guBr6Z8XSOnOz01vgmy19yicgL6hJAr06Is7fx63-7l2ZZqsesJ9LILs7c5cNJuKs3OBzwJNJxVSXrgQl3duqkBBl7FaAqMlpKlmrc0Yj3b5isoOtaYRDNsv28f-pBMlugfifnivwfiUCFR0a6Rw5ZRMa_1J-ZsRatvO0e6sSTgaUJMo-XficEqwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جین شاهین، سناتور مطرح آمریکایی در واکنش به کشته‌شدن سربازان آمریکایی در اردن: ترامپ باید برای پایان جنگ مذاکره کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/672727" target="_blank">📅 22:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672726">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfc7da749b.mp4?token=e2-fM7CWelPtCraA3EQbxdfCEon150Tmr-xcK1szG4QgT68vrPOmsB8Gv3GBoIUKZsFf6Icj6kao5y4WW2NzjYX9YfgjlfYYcyFraEeyGXIj_NS5qZ37paZoKxC5TAqzlXhYT-SSW9zr2rsyrZCE7aeAnRIFndWqQsZY301SklivNDoiba8G-0sY1gc4gFteYMFFdQO1nz6oPqXExHm_wc4ChCvLfmfJuub97Z_Afy0-xHeWkZz7cc9OsWGykZw2hQYxoL0DB_PYjdJno4B2vW8ehg3UfK-_Ml26WYeNBUxgcRpQ2hqvbzIgOtPRKQB9tMkKb516FgLCWMHBJiJYj0eAiLo1x87I5_Eg4rVGlP2TNxhEtitnFpAzsJvKaXPpi7r9_0hzUkn4x0TbyK57fNw4muywOZqq3CQMmK7EGzXBHe66ybpJa88-6wzM_i4V9MVKt7AtfQf-WuaYQsTXwBz_7Q9GJK4s5u8jg9nE6Ng_gHazXoBLriEp2HJz5jJeRQoK4iFi9H13jp7f1by80RnMTOVviIRtwoRi1X6Uk_n4ePJuO2iuhc9t4f-qI8FLzSHGyy-rvULNL24fOIAsWyN4HzPFHYaIKgwJ6bW7E6WGsr46PQBza_fuKDDA9HedQpcOf0qZLS7-PRLUK2dEiauXjtvmMfZ8GWXBuOOF_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfc7da749b.mp4?token=e2-fM7CWelPtCraA3EQbxdfCEon150Tmr-xcK1szG4QgT68vrPOmsB8Gv3GBoIUKZsFf6Icj6kao5y4WW2NzjYX9YfgjlfYYcyFraEeyGXIj_NS5qZ37paZoKxC5TAqzlXhYT-SSW9zr2rsyrZCE7aeAnRIFndWqQsZY301SklivNDoiba8G-0sY1gc4gFteYMFFdQO1nz6oPqXExHm_wc4ChCvLfmfJuub97Z_Afy0-xHeWkZz7cc9OsWGykZw2hQYxoL0DB_PYjdJno4B2vW8ehg3UfK-_Ml26WYeNBUxgcRpQ2hqvbzIgOtPRKQB9tMkKb516FgLCWMHBJiJYj0eAiLo1x87I5_Eg4rVGlP2TNxhEtitnFpAzsJvKaXPpi7r9_0hzUkn4x0TbyK57fNw4muywOZqq3CQMmK7EGzXBHe66ybpJa88-6wzM_i4V9MVKt7AtfQf-WuaYQsTXwBz_7Q9GJK4s5u8jg9nE6Ng_gHazXoBLriEp2HJz5jJeRQoK4iFi9H13jp7f1by80RnMTOVviIRtwoRi1X6Uk_n4ePJuO2iuhc9t4f-qI8FLzSHGyy-rvULNL24fOIAsWyN4HzPFHYaIKgwJ6bW7E6WGsr46PQBza_fuKDDA9HedQpcOf0qZLS7-PRLUK2dEiauXjtvmMfZ8GWXBuOOF_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی:  همانطور که مذاکره اول و دوم فریب بود، مذاکره اسلام آباد هم از سوی آمریکایی‌ها یک رکب بود
🔹
برای ما روشن بود که عمانی‌ها تسلیم می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/672726" target="_blank">📅 22:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672725">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای پوچ هگزث از خدا خواست محافظ نظامیان آمریکایی شود
پیت هگزث، وزیر جنگ آمریکا در واکنش به کشته شدن نظامیان تروریست آمریکایی:
🔹
خدا نگهدار قهرمانان؛ فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/672725" target="_blank">📅 22:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672724">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
روزنامه آمریکایی خبر داد: تمایل ترامپ به گسترش جنگ در ایران؛ از تصرف جزایر تا حمله به سایت هسته‌ای زیرزمینی
وال‌استریت ژورنال:
🔹
ترامپ پس از چند روز دریافت گزارش‌های توجیهی از سوی مشاوران ارشد، به سمت گسترش عملیات نظامی در ایران متمایل شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/672724" target="_blank">📅 22:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672723">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رویترز: به دلیل کشته شدن تعدادی نیرو آمریکایی،ترامپ دستور داده که در ساعات آینده، یک حمله قوی انجام شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/672723" target="_blank">📅 22:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672722">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
به گفته برخی منابع خبری صدای چند انفجار در بندرعباس شنیده شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/672722" target="_blank">📅 22:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672721">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlstTpfnXRxJ7sb6EVraa_tHhyYYCTwCbLYMfpRZfcLCvHPY3s1JLEnXxo85Dc4GnomPP0Gv99BCIp51Y85emjOR0XItG2bLwieM_rpcrYlk5_lyu2ktaJVdQ9Uo_93EfEN6DV08Rrf42w58Zvv8lb0b_q4SGVYyeQoj_VaSgccmfbT6aZAdC-x0CPzDo4vchGLs8lbUrkOdBk4Ugw8Y6ykRWAhf96ieElhr58A9Gb_9lEWsv_FnOE8rI9wQ0WPx4v_K6CWvba4COcPh_EbJbI97ioJGhyLMsqtGApZuN-x9jWvDdPkyOYvVNuRsMkgQR7XvCYBHP4xNc9HqEVpf2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ما بازی به نفع شماست
🟢
همه در حال حدس قهرمان جام جهانی هستند، اما شما با چیدن ترکیب مد نظر خودتان از صندوق‌های ترنج، شاید برنده‌ی ۲۰۰ میلیون تومان صندوق طلای رز ترنج شوید.
🟢
کافی است وارد لینک زیر شوید و ترکیب مد نظر خود را بچینید.
🔗
cup2026.toranj.ir
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/672721" target="_blank">📅 22:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672720">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
هشدار سراسری آمریکا به اتباع خود برای انجام سفر خارجی
🔹
دولت تروریستی ایالات متحده آمریکا در پی تحولات اخیر در منطقه خاورمیانه و افزایش ناامنی‌ها، هشداری سراسری برای شهروندان خود جهت انجام سفرهای خارجی صادر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/672720" target="_blank">📅 22:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672719">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام قدردانی رهبر انقلاب اسلامی از ملت عراق به‌پاس حماسه تشییع امام مجاهد شهید منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/672719" target="_blank">📅 22:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672718">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
هشدار جدی بغداد به دمشق/ دخالت در پرونده لبنان برایتان گران تمام می‌شود
🔹
روزنامه «الاخبار» لبنان در گزارشی از هشدار صریح دولت عراق به احمد الشرع (جولانی)، رئیس‌ خودخوانده حکومت سوریه، درباره تبعات هرگونه ورود به تحولات لبنان خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/672718" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672716">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4495c0bcbe.mp4?token=OqsEEx15jwJrxcTmz35g5MlYjj8gSazqTMlXPi4FQRRkWrw2Y5Yk-9GIz_qUFZaEMewdToRj3AroZuMdD05jz-DJpfCbfkVuYQsE0YjXl1sJyAYhz-ZFiu5xfqJ8hfhWPBGIYzju0TSwa4mHLFVRaNm9M-NpsX2leJOhCDRNd3eHdD20rerz6lpN2cVGBltGqgpMRUdES3b340uwP5kuPbZf1WJxLLCZX0wVQhuOXBZv0yDduBRigvfO4KkA6fWYSPR5qFSa9mw5XcR_9UJ9r_sS49MOyJwH54WVJ_k7von-Eled-BTZ1nsO4cZcHfSqq0tNmTkbYoN7dx6-7-pTfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4495c0bcbe.mp4?token=OqsEEx15jwJrxcTmz35g5MlYjj8gSazqTMlXPi4FQRRkWrw2Y5Yk-9GIz_qUFZaEMewdToRj3AroZuMdD05jz-DJpfCbfkVuYQsE0YjXl1sJyAYhz-ZFiu5xfqJ8hfhWPBGIYzju0TSwa4mHLFVRaNm9M-NpsX2leJOhCDRNd3eHdD20rerz6lpN2cVGBltGqgpMRUdES3b340uwP5kuPbZf1WJxLLCZX0wVQhuOXBZv0yDduBRigvfO4KkA6fWYSPR5qFSa9mw5XcR_9UJ9r_sS49MOyJwH54WVJ_k7von-Eled-BTZ1nsO4cZcHfSqq0tNmTkbYoN7dx6-7-pTfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت آب‌گرفته خیابان‌های نیویورک در فاصله ۲۴ ساعت تا فینال جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/672716" target="_blank">📅 22:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672715">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
علی الزیدی، نخست‌وزیر عراق در ۲۳ ژوئیه به ایران سفر خواهد کرد
🔹
بغداد حامل پیام آمریکا به ایران نیست؛ اما می‌تواند علاوه بر ارائه موضع عراق، آنچه را که از نظرات واشنگتن شنیده است، منتقل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/672715" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672713">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4zOmNatgpPXcyleTb2zTekW_UgjEwPu-DZYLZAZWnz-D9fPqg7IkFLpDEM9_Uo-GgaDrKPmA2qc5H7hlU8vptOgMsicXNMA0v1cYU6MNX_QlpBPAflpBlqIZB6OAFuYLQHR2O0jLbD2rl9YD31QpY9qRb4Meu11dCpG1DPSMoNNl6avhYGCpF2j4-QoFzvS_-VuJpTLGVAaIapxqLWaPjIijbp79nFvG50QlBCgU9QFvTVCCzwtyDUPiFO1HipQSQLmAEpwx9JdK4S9bioaqJUQoPpHOZM1ewYVUySjufx8qXOEujaD7PXm1AhbdSWCHsP27LChdnV_BCydAJ22kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«همه باهم برای ایران»/کمپین ملی صرفه‌جویی در وضعیت این روزهای کشور آغاز به کار کرد
🔹
در روزهایی که دشمن شیطان صفت با حمله مستقیم به برخی زیرساخت‌های حیاتی کشور در تلاش است که اراده ملی ما را تهدید کند، نقش مردم در حفظ پایداری کشور بیش از همیشه اهمیت دارد.
🔹
امروز باید «همه باهم برای ایران» پای کار وطن بیاییم، یعنی همه ما با یک تصمیم ساده اما اثرگذار، از سرمایه‌های مشترک کشور محافظت کنیم.
🔹
آب، برق، گاز، سوخت، نان، مواد غذایی و همه منابعی که با تلاش فراوان تأمین می‌شوند، سرمایه ملی هستند و مصرف مسئولانه آن‌ها نشانه همدلی و مسئولیت‌پذیری ماست.
🔹
این روزها، هر قطره آبی که هدر نمی‌رود، هر چراغی که بی‌دلیل روشن نمی‌ماند، هر لیتر سوختی که بیهوده مصرف نمی‌شود و هر قرص نانی که دور ریخته نمی‌شود، سهمی در حفظ توان و پایداری کشور دارد.
🔹
«همه باهم برای ایران» یک دعوت عمومی است؛ دعوت به اینکه هر کدام از ما با پرهیز از اسراف و رعایت الگوی مصرف در کنار یکدیگر کمک کنیم که از شرایط فعلی عبور کنیم...
#همه_باهم_برای_ایران
#صرفه_جویی
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/672713" target="_blank">📅 22:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672712">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fddfe1fcd.mp4?token=Vqnd8JjkfCq7Vf3ga4gXTrhFMSliLvM5kF_1OxJxCaD-c-SWW2s4fEz9wq2MswBp3XbSV4cGdcxAgsPIqFO2NRmT4fVwEk8G4LPVEAOismrUsNO-e75KKKaeobQNXdlLxyrTXuCAZxhCkFuv8zhQYgWQdHcxXG12-4NDOiSDHZ3yyWrHwFFNlxm83Evq7VNdmTQTngQjKDvKtlO3Ak8lSS6lQV7WngXw6GbVahJj7fjeOm0m8GmzczZcfXMm0yYTQKU4QFxetsfr3scfzl5Aw3b7GMM95qsy_ExwkF5N0QvphAY6GPJaBQKQt6Mfn_RoJ3j6APF2VymRgfF8AUx4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fddfe1fcd.mp4?token=Vqnd8JjkfCq7Vf3ga4gXTrhFMSliLvM5kF_1OxJxCaD-c-SWW2s4fEz9wq2MswBp3XbSV4cGdcxAgsPIqFO2NRmT4fVwEk8G4LPVEAOismrUsNO-e75KKKaeobQNXdlLxyrTXuCAZxhCkFuv8zhQYgWQdHcxXG12-4NDOiSDHZ3yyWrHwFFNlxm83Evq7VNdmTQTngQjKDvKtlO3Ak8lSS6lQV7WngXw6GbVahJj7fjeOm0m8GmzczZcfXMm0yYTQKU4QFxetsfr3scfzl5Aw3b7GMM95qsy_ExwkF5N0QvphAY6GPJaBQKQt6Mfn_RoJ3j6APF2VymRgfF8AUx4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شلیک موشک های آمریکایی به سمت ایران، از خاک کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/672712" target="_blank">📅 22:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672711">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7XS20UbdUePoASlxXnulJ0vzqtaimseXA3jzDFRJ9Rf4aTcP8lSyIf23fzXUgcbgdkrqb4T1TlykZxPI5Q1ucnTMB23AMoF2n8CwX-2rQyd40jfKVaJsi0oDFstFyFcE0TkUByi2GuwLuS5tt6YJnBFq8BBgSeIvMwyd3dRbaZGH9ySuiNxCec1ml3AfoIyLrbONzi5uYZrjJNChfgENz82i65PmjyqLggBO7xZxiDnWT8YNzT1df-VJuthAudOR-RmNAWs9bJiGPeeTmYfjS02ONoXx1y3JPOLClHvJFWuNW4tinu0N8leWsoY4X86tYKZ4L7MSoZnVT1ENjgKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
ویژه‌برنامه عزاداری شب شهادت حضرت رقیه (سلام‌الله‌علیها)
🎙
سخنران
خطیب توانا، حجت‌الاسلام‌والمسلمین استاد حاج شیخ مرتضی ادیب یزدی
🎤
مداحان
کربلایی جواد مقدم
حاج سیدرضا تحویلدار
📅
زمان
یکشنبه ۲۸ تیرماه، ساعت ۲۱:۳۰
📍
مکان
امیرکلا، میدان انقلاب، حسینیه اعظم امام حسن مجتبی (علیه‌السلام)
🌐
کانال رسمی
@gharib_madineh</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/672711" target="_blank">📅 22:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672710">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
انفجار مجدد در سیریک و جاسک تکذیب شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/672710" target="_blank">📅 22:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672709">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f4d4b9b2a.mp4?token=nwezV_3g-R0KRiGWRWuMuDu37UQVRivtvwfaVoU_PM7izRk7jx_YH5mmNW_qxKdPAhL8JV7SnU7Cbfw_od_8NySDTeBnHMCaUOygX2TrVNIAzKXbyECoNxhFORGZT_TV25pu6FjAQ3DEaNgJrp2mJOAtzxBOZeiYd8VGyHMkvEKoLBbzga3GFKQ-OheVv65Dw0zZKQ4bm40oZilQKJNShs3c4GGHVBt_coPXi_7zV-FAQ7zDIrOea2PCyvfZx8N5dmFzpcuucpf3vn2VzJvS8PJEltuhMz4Hic0EWllyPc0b47krFPfULaWswWVKideduVXL3UUes5wQJAxb2AlT3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f4d4b9b2a.mp4?token=nwezV_3g-R0KRiGWRWuMuDu37UQVRivtvwfaVoU_PM7izRk7jx_YH5mmNW_qxKdPAhL8JV7SnU7Cbfw_od_8NySDTeBnHMCaUOygX2TrVNIAzKXbyECoNxhFORGZT_TV25pu6FjAQ3DEaNgJrp2mJOAtzxBOZeiYd8VGyHMkvEKoLBbzga3GFKQ-OheVv65Dw0zZKQ4bm40oZilQKJNShs3c4GGHVBt_coPXi_7zV-FAQ7zDIrOea2PCyvfZx8N5dmFzpcuucpf3vn2VzJvS8PJEltuhMz4Hic0EWllyPc0b47krFPfULaWswWVKideduVXL3UUes5wQJAxb2AlT3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر خارجه: پیگیری حقوقی خسارات ناشی از جنگ‌ها در سه سطح درحال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/672709" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672708">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
فرماندار بوشهر دستور تخلیه به ساکنان بومی خارک را تکذیب کرد
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/672708" target="_blank">📅 21:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672707">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اعتراف وزیر جنگ پیشین رژیم صهیونیستی به عدم تحقق اهداف اعلامی علیه ایران
وزیر جنگ پیشین رژیم صهیونیستی:
🔹
تلآویو به هیچ یک از اهداف اعلامی خود علیه ایران دست پیدا نکرد و عملیات ها علیه ایران شکست خورد و هیچ‌ یک از این اهداف محقق نشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/672707" target="_blank">📅 21:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672706">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAqc3nc1VvkLoyC4G3wGao0NJToKhZOoKdmQeb4fq7rA9tExUBvLnLPRp-tVOlq83OZwR2jE8MWA4zY9AkG7jTDWXd7ttdqpZwnYU0EB_lrIrvE-Osfxx-AJjLo_sGf96y0foA2Pbn2DXPySXIGLC9KOiuHZxPoO2oLf0jpBO4M9dAUR2ARmXyX78rdx0wcth9URM_3tZ4sogDuYdZylLBdUVDSAnLhxddhKC3eGne83tBbzPB9XpiRIYAbzG5IhBQpKo8iOuaSKqLALMtcJfly0p-mBFwQ3GD6npEFT0jLkJOrQYhJD1zCX1fPJDvKqjyLBDIvIjwwlfuuABzcSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز فقط قیمت‌ها عوض نشدن...
ارزش تصمیم گرفتن هم عوض شد
💎
اجرت از ۳٪
🏦
بانک طلا؛ شروع از ۵ میلیون تومان
🔄
طرح تعویض با عیار ۷۵۰
👰
مرجع سرویس عروس
📲
داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/672706" target="_blank">📅 21:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672705">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5-IIOWSDqQmB0uptCm0Y2JmWyEP7OaUQzJI8wswOXYD0mge91UUXO9HdCTyTeBwwSF7jLqfgqaxSwjN5mHSmj_oYosTH02aoEU-VDpUbG_vit-oQHI4Ydm1vbqYyKcaKg071JlCZnp2GpoOM5uiEbJIARqvhfkcJETLZCVGi6VhCSHPMbHsKP-sQuq032YSAd7H8OxlUhrmoFfhTz-hDi-ycIMn2w0Op7W6Yupo1Ofy88IA1F5O4Du2s0WTzUcuoY5C8WkDR1uUiAkfIHNzNQR5vTm5BTABZ_ZX858XWNvjcWsRKmsXJ36bTCl3ic1eHkHaS2RCxXa3bfkwYnwMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تظاهرات علیه نتانیاهوی کودک کش در تل آویو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/672705" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672704">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0W1Djs2RVKdraWOMsaHuA70ok_8CUfQNDff1Dt8Rt8etzrBtC2Psiazgok0r5JanNysmjgsc-c_vFOW0bybfSw_KHoRdba1AuA3xwsLYxyetju38xFh9m17a0icBqcRPK5gdM29ZpdRjwnZOsDgUHJm1azyawQgmcVsd4PIFzzLuJNjHz0rK4Ab-Yb2hJFBytlxr5hcMAHq-6EMbCyIGwqrqOpuKIPcRr45NOIEsNyvGZaEqm53EutglIW_i21PWPrkbstd6aDC8RZirLZRTIirJHzX7e0WMgbOatvN90NrgcATQCnoF8mE0OGuYytkTDL7n8gMUmoxrtEebfJ1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: پیام حکیمانه و وحدت آفرین رهبر عالی‌قدر انقلاب اسلامی و حمایت ایشان از سران سه قوه و مسئولان کشور مهم‌ترین پشتوانه و سرمایه در جهت صیانت از منافع ملی و سربلندی ایران اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/672704" target="_blank">📅 21:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672703">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnWQqFyj7DLxmaFcx9Bz_uZCtCPEsDoWZxkM6IlBm2f4bcgRjzdXYjwJ5y_BLnzGK3hBT1OEkqDQhpM_xcgvsPhsoXsGv5F_TZt2h7YCEUQKnLEyGvQAqJY_ErWLBrBj_Q79UsrnLofk2dW9W35ksyH3PXrebIEehf48JmgosyfjcjzixsdrSK9HSWa4h4XpkYUu_8KazYbkIdSwOu90Zs92UvRqHhGvYP2Xsa6gyhL1XoGEHm_PUcZiDr8kNz4sCJo5vWV6Sz05--bvEk6N7AYgahRQFsUZksCLDj_5POilTMF4F6_Yv3vYIVDIckg1BDjfaj3ThnDCXWZH9moQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان تداخل با سیستم موقعیت یاب جهانی (GPS) در کشورهای حوزه خلیج فارس به سطوح بی سابقه ای رسیده است و این میزان تداخل حتی در مرحله اول جنگ ایران نیز ثبت نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672703" target="_blank">📅 21:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672702">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009c2f2675.mp4?token=FvU7KpawUW-2QzwxwFRbkfZo18cPwBuShLF2jAIbbMcCh41t9QDzUNixBMoPj2y1VjQGV_zay_cJhWqtBK4k5-KC4BCcHNuRxkrKEWj4KqR8Ai2NFElpq7uWarb5CJFooWCYtNCafTdERI2fyGjKJ4ZzqbWuNqUBmWJ3pIkrX0F-YtjfPBekfOprMLOTtsOt3lCtRTXrGhwyk_5Az9HW4-J7N1PElcxWWHl6g6wp525cGlVWAui4fcPBeHOPG8KEuuqSdZC2RdUwH5D1Eeum700wPj7dNFfQRHxGICupQQNkTaUIwcngt5mhI9nfEyRS1G5i_3AFiY4OUtjMYwJbgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009c2f2675.mp4?token=FvU7KpawUW-2QzwxwFRbkfZo18cPwBuShLF2jAIbbMcCh41t9QDzUNixBMoPj2y1VjQGV_zay_cJhWqtBK4k5-KC4BCcHNuRxkrKEWj4KqR8Ai2NFElpq7uWarb5CJFooWCYtNCafTdERI2fyGjKJ4ZzqbWuNqUBmWJ3pIkrX0F-YtjfPBekfOprMLOTtsOt3lCtRTXrGhwyk_5Az9HW4-J7N1PElcxWWHl6g6wp525cGlVWAui4fcPBeHOPG8KEuuqSdZC2RdUwH5D1Eeum700wPj7dNFfQRHxGICupQQNkTaUIwcngt5mhI9nfEyRS1G5i_3AFiY4OUtjMYwJbgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای نزدیک از لحظه اصابت موشک ایران به پایگاه موفق السطلی اردن که منجر به هلاکت دو نظامی و مفقود شدن یک نظامی دیگر آمریکایی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672702" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672701">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b8938fde.mp4?token=P_YMhxY-TZC-trIihuWttfeid93gOwFIM-4a0Pj9WjvDVL1q-320ayFmA-nx2PGVJBaVuNiX5cUgqb9oBGI4_TzYszXMYiooadFGrI01M7g1dQj4sr9yBjYIVI0klJyMckPZTRyc_ZrezRwgHvHZZY8e_faXIpdjhvmxUZwa7AWpyd95mWYnMZEnu3lWbNYSnKKrfRP-8c39qg08H9lOjylT2imLEMkjEfzAw10Qh4znx6bcZbEhuA2ohIIUHmLuDx_c0UcEjvWVgIMZkVvVR4NJK54LI_Tzt7GKMAxQ33Ov22hduYbN-d0_qTiuTIeZe9hMhDoolGrGlSCHqqwKGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b8938fde.mp4?token=P_YMhxY-TZC-trIihuWttfeid93gOwFIM-4a0Pj9WjvDVL1q-320ayFmA-nx2PGVJBaVuNiX5cUgqb9oBGI4_TzYszXMYiooadFGrI01M7g1dQj4sr9yBjYIVI0klJyMckPZTRyc_ZrezRwgHvHZZY8e_faXIpdjhvmxUZwa7AWpyd95mWYnMZEnu3lWbNYSnKKrfRP-8c39qg08H9lOjylT2imLEMkjEfzAw10Qh4znx6bcZbEhuA2ohIIUHmLuDx_c0UcEjvWVgIMZkVvVR4NJK54LI_Tzt7GKMAxQ33Ov22hduYbN-d0_qTiuTIeZe9hMhDoolGrGlSCHqqwKGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کانال ۱۵ عبری: تشکیلات دفاعی اسرائیل در حال آماده شدن برای احتمال تشدید تنش بزرگ در منطقه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672701" target="_blank">📅 21:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672700">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCFx_VyaZdyqZGmiOKv-SFBkGJ5ZzirWhKtcaJ_AEpruYzt5kI_p270kG3jVMtBD5S8ZdaHaHxL6uh5BeSxH3ZrSeMQ1G6KKaMdYFSLOS3WkB8qXLz8gHIWb7ydZ0d1LmZ2swjEz8GsugpcMC2WoeSoH32dylZZCquPtVY38s5ldSwou13-Y_GpIGJIytiEz4g53H4Lia4NrRxcFDHAjIRQGDboaetQZ6LECkUwBob-TXoRmGzYiMCql6-zZaYf6aMvjuVp-uW8vr5BrrCl78itug4d-ck0XXIa6a4rRwIc9HqGV8VWGKjdbk0LT1cI_Z-IufBRWRA5vwI-PpPK3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۹هواپیمای سوخت‌رسان آمریکایی اکنون بر فراز خاورمیانه در حال پرواز هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672700" target="_blank">📅 21:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672699">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn2hgdhYL-OXx_JF8KzXS6wUF2qi9S1XHHWefYo0TgEnpAKJ3__qQwhRu1ZwvnDGDHBG4hIaIkLmOY2BUfyOkF2P6d0qLxj_N3-MGcu1WkdKQPLjgdFBgemYLw_dWywMuyS0z3phAD7dX4q7DhhjLsdEEuZPBjbu8Ugejd1nLvYIrvzcZGdWdkFAk_85pT-rX7T-Nt-YL9iz9Ohg1wodI3Fl-Uz7g1n0aUkrHLm64XzAmya3iWEAFHp5xv7EvvNypmfhi_V0_u-8zG0KsA5bOYXywQOyDP1tJ4-GgYOgsSM8DKH9n8GdC7yTkWHz7J52P_GjFTABa82d8ZkbBz41Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سید مجید موسوی: حاکمان کشورهای عربی اخرین هشدار ایران را جدی بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/672699" target="_blank">📅 21:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672698">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
هرمزگان از برنامه خاموشی‌های برنامه‌ریزی‌شده برق خارج شد
نماینده مردم هرمزگان در مجلس:
🔹
وزیر نیرو با تایید شرایط خاص هرمزگان و برخی استان‌های جنوبی، دستور لازم برای خروج این استان از برنامه خاموشی‌های برنامه‌ریزی‌شده را صادر کرده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672698" target="_blank">📅 21:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672697">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
کاخ سفید: سفر رئیس‌جمهور چین به آمریکا همچنان پابرجاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/672697" target="_blank">📅 21:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672696">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/narQK6jwGLzB5Xz7RSmQoYJUE0J7Pwbnw9RuvD8C4ecXRlAS9AjwAxGkTRqe2eicZCgnr4Lwyw1g0eO0pQTTYELnqZFSNURUYCXqk3mdA5S93HPAKH9O5JnZCgejcXpAgjkCnCZKFDPf-iWzW4_hEKb7iRI-FWtW0aMlBI8lA6ZkXoLU813pvvYaphcZtLRNgQGLJtJZ_tZUw73mKq59tkMJRfTn20XzneKHDVE4-BsAjoIA32szrqf0CJ3Aw2AEZigyqWVtD00DCqTJvf9wR27lu79L0jVX1PvldY_8JOVMPO5U-CsD_hx9XEHaqKkjigD-UnW1LocG7tyRTfEOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در جریان حملات آمریکا به پل شهرستان خمیر در استان هرمزگان، ۷ شهروند از جمله ۲ دانش‌آموز جان خود را از دست دادند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/672696" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672695">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3LWQvLp7NLbLcQLRvoSENvLXpOGfG6MPgTbAeJj19DcuC1DUFvgcCIa-BGZE-_fF3QJ_86ywIET3YzeI0d6JyoDZbtD4M6M2MDF3qrCNObghZD55MXf0U7iAnHhNDzcEUBzrmsVxli5ucFPPMmCebYizW1qnDA6TqZU6d5m3lhGLmpMcJBv2koRQ4gVfN1A_cWoNPEsR5fU9VSRoR74oXasogrjlqQkmasAfZQrvgCsFLS2WUbR4gJ18Qvdg_lPqgjLK3SwuD6CihisIZGOI3M6lxBl2uEApEFmsOkIUxxVoeuUEmDbUDDnXLZPnK68NH5XpUxH7O4JD3nfAKklyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام امت اسلامی
آقا سید مجتبی حسینی خامنه ای
رهبر آزادیخواهان جهان</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/672695" target="_blank">📅 21:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672694">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc93bd0cb.mp4?token=OJwUL7nT3952_vtXThZEOaAwYzaEggFAr23y6_c-W7kuE33360c7u0pxH-kTstj39a0VBdcn813gHnGXurGMk2Fwfoy8NFcukeyXlkgvbc20LjspUiGkdHfVhJhL6_M6zRfnRD4oMdVnO-6L4M5vsHjO413_9tMRCOrSoxjgOjlFgzyqknPyOrPMgvssKI8eDbVWy8MrPAqoB0RG1aptbyGQ2OuxBxdpMO7rJ8PO8mmWLA7pzQDJSGYg_IwigJfNrkl_ULiVDFbauH_gSONKcaH7xPNaWh7Wlkvriw-MnAIhHVEaE83rMuIrd-HMHH6iZcYGzBCupF_xEG7RQgCPRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc93bd0cb.mp4?token=OJwUL7nT3952_vtXThZEOaAwYzaEggFAr23y6_c-W7kuE33360c7u0pxH-kTstj39a0VBdcn813gHnGXurGMk2Fwfoy8NFcukeyXlkgvbc20LjspUiGkdHfVhJhL6_M6zRfnRD4oMdVnO-6L4M5vsHjO413_9tMRCOrSoxjgOjlFgzyqknPyOrPMgvssKI8eDbVWy8MrPAqoB0RG1aptbyGQ2OuxBxdpMO7rJ8PO8mmWLA7pzQDJSGYg_IwigJfNrkl_ULiVDFbauH_gSONKcaH7xPNaWh7Wlkvriw-MnAIhHVEaE83rMuIrd-HMHH6iZcYGzBCupF_xEG7RQgCPRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: خوک (۱۳۹۶)
🔹
ژانر: کمدی سیاه، درام، معمایی
🔹
خلاصه: ترکیب عجیب و شگفت‌انگیز حسن معجونی و لیلا حاتمی را از دست ندهید. خوک، ساخته مانی حقیقی، داستان کارگردانی ممنوع‌الکار را روایت می‌کند که در اوج یک رشته قتل‌های زنجیره‌ایِ کارگردانان مشهور، تنها…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672694" target="_blank">📅 21:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672693">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHGS2k8rbLfA8tYsExmYMcceoEOKcKTRUCMzUHcaYlCoI0pfBlUKOJakPJTbcv3erDGgyBNfRcEVbWDIzs2u08U8e3MuYIPN7bEtAEQgDbKXpq5zAMeB6zGS-OwlrXn3WTD7KbrvALTXQSY9xzQ4DiJn-PdC8Z8n2_2-S1ZmIQv7rJjsKu_Ze8_n2a-G8IE5nnklJOw3DgWqK1YdjSX1aqlEYHnJVaIu0VYEuW7utJ9WkA5OQVfbU5s4-VCJ6e9PAbN9neqoY9vTNdXXrkfuzuf8qWYcCAYLZxHQHPpIoDMxlJaz5nR4JePRMpyzVh19_UeaalpEtpmb2Mht1MlgHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک در یک روز ۴۰.۵ میلیارد دلار از ثروتش را از دست داد
🔹
بر اساس تازه‌ترین رتبه‌بندی فوربس، ایلان ماسک، ثروتمندترین فرد جهان، بیشترین کاهش روزانه ثروت را در میان میلیاردرهای رصدشده ثبت کرد. ارزش دارایی او در یک روز ۴۰.۵ میلیارد دلار کاهش یافت و به ۷۹۷.۶ میلیارد دلار رسید؛ با این حال، ماسک همچنان جایگاه نخست فهرست ثروتمندان جهان را حفظ کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/672693" target="_blank">📅 21:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672692">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bbb86703b.mp4?token=XlEy2IVFLbDe9W4sxnzz6TS9EXJlrIt9-x-oOhTrZEOGx2cHNWfxMWzhq6KxIuthMecDlQyJH16TkR5D2_mglqOKznnsodnyz8l5q8FuAYKhEh6nTOA-YbRQvWPAfZgfrh5UYtRUvx9MEh8KPDBHdhHhqo70BuY8ltrmlY2pTfuKv7Qpakg5ogvY_-gMQ7jiijAoUgoUrvM6sR2zXeoZ9bVs4lshmKIitYiL4U0g7HnwzeOLxs21bPfHNrFCJpd7zfNUhdsKZSL59EkeN9G-9LojtOzcl-QvYo6q_dAhHSQZjNXBXVihDB9gKlrWgMGiFy29-0vhARbsrQKTt45YAoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bbb86703b.mp4?token=XlEy2IVFLbDe9W4sxnzz6TS9EXJlrIt9-x-oOhTrZEOGx2cHNWfxMWzhq6KxIuthMecDlQyJH16TkR5D2_mglqOKznnsodnyz8l5q8FuAYKhEh6nTOA-YbRQvWPAfZgfrh5UYtRUvx9MEh8KPDBHdhHhqo70BuY8ltrmlY2pTfuKv7Qpakg5ogvY_-gMQ7jiijAoUgoUrvM6sR2zXeoZ9bVs4lshmKIitYiL4U0g7HnwzeOLxs21bPfHNrFCJpd7zfNUhdsKZSL59EkeN9G-9LojtOzcl-QvYo6q_dAhHSQZjNXBXVihDB9gKlrWgMGiFy29-0vhARbsrQKTt45YAoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران وطنم
🔹
پیام‌های صوتی مخاطبان خبرفوری در پویش «ایران وطنم»، روایتگر همدلی، غیرت ملی و همراهی مردمی است که با لهجه شهر خود، پیام امید و حمایتشان را به مردم شریف و مقاوم جنوب ایران رسانده‌اند.
🔹
این صداها، نشان می‌دهد که ایران، با همه تنوع اقوام و گویش‌ها، در روزهای سخت یک‌صدا و همدل در کنار یکدیگر می‌ایستد.
🔸
شما هم با ارسال یک پیام صوتی، صدای همدلی شهر خود را به گوش مردم جنوب ایران برسانید.
👇
#ایران_وطنم
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/672692" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672691">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
استاندار هرمزگان: تردد در تمامی محورهای مواصلاتی استان برقرار است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/672691" target="_blank">📅 21:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672690">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
حمله مجدد و نقض هزارباره آتش بس جنگنده‌های رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری لبنانی از حمله هوایی جنگنده‌های رژیم صهیونیستی به اطراف شهرک «کفرتبنیت» در جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/672690" target="_blank">📅 21:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672689">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4f473dbb.mp4?token=XOBqhN8qtFqgGZdSELZSO7zDcoms8gTlW8iQB2PCXaolXKgeUVipSSLwqugYKaBSgIIbdS43jaATE4q26sF4woRX_3T1lU39KI-HzotKTm6mvH-fzpH9cza0JixyqBoqynaok3zT4PTQK1_tBrSW7ZKib6DhnytQ40WlcnxBF4EsRVkk_RzDTlO1WHQWH_WoM7NjFYsCaz7XsWOytzREjEoqHYkYM7yfs0O-XKIyXYHqSSw6urwMrsg6aaSumDhoYPMcD-I-F8XsyW6xes4g_FbGJAauSRbnpTBoFBlVwhaarlqQdGlXz6z7-JfCspeNlhUNsyuzCeMi2oUCZceTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4f473dbb.mp4?token=XOBqhN8qtFqgGZdSELZSO7zDcoms8gTlW8iQB2PCXaolXKgeUVipSSLwqugYKaBSgIIbdS43jaATE4q26sF4woRX_3T1lU39KI-HzotKTm6mvH-fzpH9cza0JixyqBoqynaok3zT4PTQK1_tBrSW7ZKib6DhnytQ40WlcnxBF4EsRVkk_RzDTlO1WHQWH_WoM7NjFYsCaz7XsWOytzREjEoqHYkYM7yfs0O-XKIyXYHqSSw6urwMrsg6aaSumDhoYPMcD-I-F8XsyW6xes4g_FbGJAauSRbnpTBoFBlVwhaarlqQdGlXz6z7-JfCspeNlhUNsyuzCeMi2oUCZceTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهار آتش‌سوزی تانکر گاز در غرب زاهدان / تکذیب اصابت موشک دشمن
🔹
بنا بر اخبار منتشر شده در فضای مجازی مبنی بر اصابت موشک و انفجار در زاهدان این خبر توسط منابع اگاه تکذیب شد و علت آتش سوزی، آتش گرفتن منبع ذخیره سوخت شخصی بوده است./ایرنا  #اخبار_سیستان_و_بلوچستان…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/672689" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672688">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGyBiRCrp8mxndV_g1aE-uMZXQaGVQQnjXgU6ILQxN8SVgPTIfx8W6MF-Xp5IUMxbz8TPyPFebLXEOGXOamkA8VxdTfokRixzRr1-O36GsGi1wwTvAPXNT7OTAP0CZ97wCX4hClze4AgHGec0t2nE0keyQFZaNC1pmSkVZbIZJlO8K9xoNpAuCCvc0J2ngxZE6MF913Pzr742R0Cj_lOg-9B59kvwRoItiyey5LhfBKQF3viQAZrKrAM_5kWRAL0NhJM_YXjwm8wtdoOqpIhmtxQ4UhXQTcroRjBgL5ide4kyU5q9vEdVXPEhGP7X-V1fXxbwSxvVC-5LBkLNg0QQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پویش جدید در توییتر: برق ما رو ۲ ساعت بیشتر قطع کنید اما برق عزیزان جنوب کشور قطع نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/672688" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672687">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THc4Q72oRQk-YU_EpgVsYHNWZTQPqk-ZJOboHc1Hz7E-prBZyGETyaZXcEyrON0GIkVbrdS2EgLhkzkRlLo2P-n4Ldo5JkECdlPLWStA7iVw0WHbdUxJFLUkIrqonMTSjNkmumiGBnSXS56dGdqPewVb0PH4N_m1jOUDh-RskhUeoIxznkBZ8w0T2lxnceamuP0BWwpY7Doeep7pGBNo4y_pgHFQOnv_Is0bbtMj4DVgIwIeTAPGQvxfqKlRkZZZxdJRyazWqjUPxiKlX30TFNA2MAKsVC_39WkrOLBONhTh3BVZSx1ZdemJke4xRZrUBf09oUPq8hn-c_PmmakPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
از شیائومی تا اپل، موبایل بخر با وامِ اسنپ‌پی!
🤩
📱
برای خرید موبایل جدید، تا ۲۰۰ میلیون تومن وام رو با ۲۰% تخفیف اشتراک و بدون ضامن بگیر.
💣
تا ۲۴ماه هم مهلت بازپرداخت اقساط داری که دستت رو برای پرداخت بازتر می‌ذاره!
😎
پس تا تخفیف اشتراک هست، این وام رو از دست نده.
👇🏻
https://l.snpy.ir/84aj3
https://l.snpy.ir/84aj3</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672687" target="_blank">📅 21:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672686">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fg8WRfkQOjslS1WiRhXGMwUBRbY4gLw_nD9zrKnLnJybw6rXykt72qZxiYJrJs00bFxN7j4rPjWoulc7O__b0bxhjd8HITeQ8GrGfH7vPfufanaR4sFdbnMKq4PS5EF_mlTtuo6ciOBnwcqHeMqUEHciINdBLL1mCcQpE5IhYtHGD9lJhtKQuisJs-Xw_DpHWhMJjZrT8_uJcXX_J8ql_yVdeAXCiItT0T7J4VZAKfmhc7SH1jw2vEcHxYBZqcF5ufRkZ4kavJr0JZe8Yok-JIDn8keH7QUC5kPa2FQLKCSz7fWJNv-jyzrbpyp60qHnkWCWBw7TD-eKEmP3zHGzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر قصد ورود به دنیای هوش مصنوعی را دارید، این منابع می‌توانند نقطه شروع فوق‌العاده‌ای باشند
🔹
Anthropic
آموزش اصول هوش مصنوعی مسئولانه، ایمنی مدل‌ها و کاربردهای Claude.
🔹
Google
دوره‌های جامع از مبانی هوش مصنوعی تا ابزارهای کاربردی گوگل برای همه.
🔹
Meta
منابع آموزشی رایگان در زمینه هوش مصنوعی، مدل‌های متن‌باز و پژوهش‌های روز.
🔹
NVIDIA
آموزش تخصصی هوش مصنوعی، یادگیری عمیق و پردازش با GPU برای توسعه‌دهندگان.
🔹
Microsoft
مسیرهای آموزشی هوش مصنوعی، Azure AI و ابزارهای مایکروسافت از مقدماتی تا پیشرفته.
🔹
OpenAI
آموزش کار با مدل‌های GPT، مهندسی پرامپت و ساخت اپلیکیشن‌های هوش مصنوعی.
🔹
IBM
دوره‌های مهارت‌محور در زمینه هوش مصنوعی، علم داده و یادگیری ماشین.
🔹
AWS
آشنایی با سرویس‌های هوش مصنوعی آمازون و ساخت پروژه‌های مبتنی بر فضای ابری.
🔹
DeepLearning.AI
یکی از معتبرترین منابع آموزش یادگیری عمیق، یادگیری ماشین و هوش مصنوعی.
🔹
Hugging Face
آموزش عملی مدل‌های متن‌باز، پردازش زبان طبیعی و ساخت مدل‌های هوش مصنوعی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/672686" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672685">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/562a7ff08f.mp4?token=gSUVVdi-RHI2rXhFsymPnA_q0cgfrBvFhIMb4n3HtgT7qeJhHoJlB_-0YndZQQTFxEs1OR2swYK0qTQK4LB07kOXUvdArCRN2T9Oz6hmoAcHncqL7QAEUmIIprJJdZhSxS21F3SKYIM40ZN-aSTuEGkI4Ljh6fuJu-28EMy1IkQtQJTYK1bwwmqw0yimDNL_hGqGzE1rX4uUJhjgNnqfrQ2hvZaveGx4OMFtxt6pszTVhjqdxb1WxcTrHelrnjJMNYBK-hpIF2rL3X1_fbUGsa0VtRBQVmOo19kSttXyTNFr8nFxRBRQVJU1rLsiYkZW7z-w5DoXTqXC5MbpQxoM0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/562a7ff08f.mp4?token=gSUVVdi-RHI2rXhFsymPnA_q0cgfrBvFhIMb4n3HtgT7qeJhHoJlB_-0YndZQQTFxEs1OR2swYK0qTQK4LB07kOXUvdArCRN2T9Oz6hmoAcHncqL7QAEUmIIprJJdZhSxS21F3SKYIM40ZN-aSTuEGkI4Ljh6fuJu-28EMy1IkQtQJTYK1bwwmqw0yimDNL_hGqGzE1rX4uUJhjgNnqfrQ2hvZaveGx4OMFtxt6pszTVhjqdxb1WxcTrHelrnjJMNYBK-hpIF2rL3X1_fbUGsa0VtRBQVmOo19kSttXyTNFr8nFxRBRQVJU1rLsiYkZW7z-w5DoXTqXC5MbpQxoM0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672685" target="_blank">📅 21:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672681">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
اعتراف سازمان تروریستی سنتکام به هلاکت دو نظامی آمریکایی در اردن بر اثر حملات ایران
🔹
تلفات حملات موشکی ایران به ارتش تروریستی آمریکا در اردن: ۲ کشته،‌ ۱ مفقودی و ۴ مجروح
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/672681" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672680">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای کانال ۱۳ رژیم اسرائیل: در اسرائیل می‌گویند آمریکا برای گسترش عملیات نظامی در ایران آماده می‌شود؛ هفته‌ای سرنوشت‌ساز در پیش است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/672680" target="_blank">📅 20:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672679">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buDjDu4L0cZM162MjKk4kNxPBEFB_VHeFhQA_vE-lMO7X2iVxuPLe3DZJ_8nWv8j00rPw4SaHkV8-CP9d9nz2aA46FvAtguxjM--5KBVFgfMEMye49xRzYO47SN0KI2lUxHj7yUCMtiwX2__JqgALS7RA12Pn2SD_oQvemgcJbXxdk-UX4HXfxg3hp0Wyw5d3Pphg1yDzfDD5QQjuXp6cr8c0cVqtXrbdWCBYXI7KPo9vlD_p_PaXpvcqtTlW_jDkAJ5NkWtpATsGUplanjK9OrP9RdoaoIOQ9j3Zgxlesx4NHnAraSx1SjnWC0-wZqa6Zpz9VSefdBCDVfXMyPaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از کفش‌های مسی برای فینال جام جهانی ۲۰۲۶ رونمایی شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/672679" target="_blank">📅 20:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672678">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtbHJ38hD51HJ-vdAcGSuAfoh5xV-VAJCxSOQdgiZ5nkZ1YdWsX32HOkkXHwAyIO2Porf0wR4yncg6yZOT_FF-AM6I2azTVvEsgj55tfe3qV6hLu2I21uBlxohaOYJ2rKbTTOtPoXJH-Biq5JmAr-bZY8gy0XbYnz-KRu0vP66Y54rmMiN0U1CLA_li42H5KwGZobYA0nBeJ50nqFM5x4AKXvFp239jYClzcZvRErO2FBsstZRrJmDV_qOv1lcerhAlK5PQqrtnmKUrCBSDYCWwyECQRc2cn7Z4gh0L_3FlSAuFn6Hb23SZwJOUSGRT-S5jrKgXt0UM1nVpK_32JBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام تشکر رهبر انقلاب از حماسه‌آفرینی ملت ایران و تلاش‌های مراجع و نخبگان در بدرقه آقای شهید ایران
🔹
از یکایک مردم عزیز که خود، صاحب‌عزای پدر شهید امّت هستند و با وجود دشواری‌ها و برخی محدودیتها و ناملایمات در رویداد عظیم بدرقه‌ی ‌آقای شهید ایران، حماسه‌ای…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/672678" target="_blank">📅 20:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672677">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ee473e85.mp4?token=ZOxETTiSP1W2xpM2mwLeRMLrWIf6pc6-YfYXC5Oy7fLcVVExinS0ae3kggntssGMv8CwuZsoN21p1z8lm6l5xfpHzTIsZL6ikt777RqdkqsuHSYZFxGEQfG5pS6TaRuwbXWEQQbiyQvRKLqGwttW_sxg0oI2N-oPqvDfam4LkY8_o7zx-efaSVkY7p69vTFisbMBLdFe04WsDVm69jZ2qPnXTLHNijwQ-7QtzHeMssqiOMHWqxaPrnjK1ZEWP6v9xx7LNeVUs4l98u20_DBFC0FHnunPen9cOAeVNM2VrptxgxGsQyTuIURAe4jT5TZwICQlL1GrMKbrhUlxP-mrMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ee473e85.mp4?token=ZOxETTiSP1W2xpM2mwLeRMLrWIf6pc6-YfYXC5Oy7fLcVVExinS0ae3kggntssGMv8CwuZsoN21p1z8lm6l5xfpHzTIsZL6ikt777RqdkqsuHSYZFxGEQfG5pS6TaRuwbXWEQQbiyQvRKLqGwttW_sxg0oI2N-oPqvDfam4LkY8_o7zx-efaSVkY7p69vTFisbMBLdFe04WsDVm69jZ2qPnXTLHNijwQ-7QtzHeMssqiOMHWqxaPrnjK1ZEWP6v9xx7LNeVUs4l98u20_DBFC0FHnunPen9cOAeVNM2VrptxgxGsQyTuIURAe4jT5TZwICQlL1GrMKbrhUlxP-mrMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: پایگاه تنف ایستگاه پاسبانی اول از سرزمین ‌های اشغالی است
🔹
هدف از ساخت این پایگاه پشتیبانی در جنگ زمینی علیه ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672677" target="_blank">📅 20:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672676">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ترامپ از اختیارات خود برای افشای اسرار آمریکا سوءاستفاده کرده است
روزنامه نیویورک تایمز:
🔹
دونالد ترامپ ادعاهای اغراق‌آمیز و گاه نادرستی درباره دخالت چین و هک شدن دستگاه‌های رأی‌گیری مطرح کرد، در حالی که کارشناسان انتخاباتی و خود جامعهٔ اطلاعاتی تأکید دارند که هیچ مدرکی مبنی بر دستکاری فیزیکی آرا وجود ندارد و سیستم‌های رأی‌گیری امن هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672676" target="_blank">📅 20:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672675">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
روایتی تکان‌دهنده از سفر به آسمان‌ها؛ «یا حسین» چگونه جانش را نجات داد؟
🔹
00:07:10 جسم را مایه عذاب می‌دیدم و از قفس تن بیزار بودم
🔹
00:11:00 یقین به حضور و همراهی دونفر به سمت آسمان که قابل رؤیت نبودند
🔹
00:18:00 علت رسیدن یا نرسیدن فاتحه به اموات
🔹
00:34:00 نمونه‌ای از کمک‌رسانی اموات برای جلوگیری از چشم زخم و هجوم شیاطین به بازماندگان
🔹
00:44:10 سقوط جهنمیان به گودال آتش از ترس چهره وحشتناک فردی از نزدیکان من
🔹
00:49:20 نجات یافتن با گفتن نام «یاحسین»
🔹
00:53:50 حال خوبی که با دیدن بچه سقط شده عمدی، از بین رفت
🔹
01:04:30 بزرگ شدن و حجم چند برابری روح نسبت به جسم
🔹
قسمت پنجم (آن مرد که نیامد)، فصل پنجم
🔹
#تجربه‌گر
: طیب پیشداد
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/672675" target="_blank">📅 20:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672674">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fev38zXk2baY3dx8wgoZKIYvTJZ8Ju3P1dy6miCPFmwoWbeU6aqLUAiPuXX3bWn-K7ppBBsQUOJC6uZdUN5t-WmAh1z_aV3Z7rH9ZEpD-AOmgSgBWU_Q95MM8brohEKcJgQ0O41JNlPsdsnPgc9_ZrymPb15HHqBhLfaiRcAgTnVABvNpw_AyQv1KSu-UrP1HenI9WCQy-dng0j88Xq99EY59RaQitriAzktOLMYD_kycj9S0zKtNkIaOsK_70YiGifHhpv3Ktnl5h4d3jpQ17500ZGVYP5UmbRrS847RJ1kq4oT7eMvdnNUoOjNL-cXbM3D_V9hlKHSc-Yb3IcZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/672674" target="_blank">📅 20:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a90f4306e.mp4?token=XysAw4BGGXj80qRuMvd7EAo3EbMr_4nQVyAVostoy2_jaI217pgxrB7r1UoYPpFfFKn2yXlPoslx0oJW7hhCRFNR8rG-4ClqF9xx1Gc5tcFMS5IkAAxFDc3ImvFTHTceFI1hxfJTQp4Jm_fMEagJZasRI9vU-CnK4elVSqJmFEoZSTheoqr1bc4ZDn8Jakb3oaGjjA5zih_ZctdnGZsxdHV-UhWkil3c3k2v1SKJt4y_kp9MEIE5fhhTomhOoOb3X8FRXqAyvJ-dln-06cNLV_nsHpu5xmoVqM9dwROmuCNaYRxdLjaZfhDUDejFod6wv926Ax1RBSWsiTKrL8g77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a90f4306e.mp4?token=XysAw4BGGXj80qRuMvd7EAo3EbMr_4nQVyAVostoy2_jaI217pgxrB7r1UoYPpFfFKn2yXlPoslx0oJW7hhCRFNR8rG-4ClqF9xx1Gc5tcFMS5IkAAxFDc3ImvFTHTceFI1hxfJTQp4Jm_fMEagJZasRI9vU-CnK4elVSqJmFEoZSTheoqr1bc4ZDn8Jakb3oaGjjA5zih_ZctdnGZsxdHV-UhWkil3c3k2v1SKJt4y_kp9MEIE5fhhTomhOoOb3X8FRXqAyvJ-dln-06cNLV_nsHpu5xmoVqM9dwROmuCNaYRxdLjaZfhDUDejFod6wv926Ax1RBSWsiTKrL8g77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود غلیظ در کویت، در پی حملات ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/672673" target="_blank">📅 20:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672672">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekYtbdC1sk9EAVdaWUTCXMaCMZeIx1AcKH__96MnF9vogF_Y2dXffUyGWBr8ddNCYH-Jgp6EZpz7rnWfOEoXTKcyqppaSk6v8h3mkgZuK2Q36woa8TtD0x3_yFBd_9F6bkzMUgKlhTVQzR4AqYDzW75Z1ciAItZZqbpoIrUxQagAgXHS_b9z94pg683c1QaS9JurxpFQvDy3QV8-3-Q_sLPAdmK8D9fP52Wd19ZAKk6jMc1zbEme5WI0vAwmWde9yf0KItdubFMbwSk9VEjqlhXtxy2SfaXdHjgsfKvxGOs65sYRyIhwdrzMwj8DGgmztdAw9wr6p4wBWDf2tp0maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام زیرساخت‌های غیرنظامی و مباهات به آن، یادآور رفتار گروه‌های تروریستی است
اسماعیل بقائی سخنگوی وزارت امور خارجه، در پیامی در شبکه ایکس با اشاره به توییت وزیر جنگ آمریکا در مباهات به انهدام برج مراقبت دریایی چابهار:
🔹
برج مراقبت دریایی چابهار، یکی از زیرساخت‌های مراقبت و ایمنی دریانوردی، روز پنج‌شنبه ۲۵ تیر برای سومین بار طی روزهای اخیر مورد حمله آمریکا قرار گرفت و وزیر جنگ آمریکا، تصویر فروریختن آن را با افتخار منتشر کرد. وزیر جنگ آمریکا اگر می‌توانست، احتمالاً به همین شکل حمله موشکی به مدرسه میناب و ورزشگاه لامرد و کشتار کودکان و مردم بی‌گناه را نیز با قساوت تمام به نمایش می‌گذاشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/672672" target="_blank">📅 20:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672671">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2109385f6f.mp4?token=FyMCAsafjUYxVcqv0tLLOdVUgJgux2hjoIlLRQDBbqOneyhVehIEhVntR4xTw6JORpKuXyCT6V0u1GiWb46SVpCj_TL8ger4Ku15p7nkAPVR3WwHGLUjNJdZ5a_ly_Pxrj-y_BTTZN026UbJyQtAE-Xx7-sgxoZ6t42kea3ApXVAc4BgG0XwG855lvkDLEHqqlk2TLn3IIqYdkQVv1WhiKF3CJhtEVEUIrQITrKxYq7Tms9seObKsjmd82td1_BRyeIA7GavtXvd6Z_JM_mJWUNWlNYPBVRE_USgNwth-JEZntnQ6jVfG9Ivd-M34ScOcFdzBYNL_6_Kboz11R2EqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2109385f6f.mp4?token=FyMCAsafjUYxVcqv0tLLOdVUgJgux2hjoIlLRQDBbqOneyhVehIEhVntR4xTw6JORpKuXyCT6V0u1GiWb46SVpCj_TL8ger4Ku15p7nkAPVR3WwHGLUjNJdZ5a_ly_Pxrj-y_BTTZN026UbJyQtAE-Xx7-sgxoZ6t42kea3ApXVAc4BgG0XwG855lvkDLEHqqlk2TLn3IIqYdkQVv1WhiKF3CJhtEVEUIrQITrKxYq7Tms9seObKsjmd82td1_BRyeIA7GavtXvd6Z_JM_mJWUNWlNYPBVRE_USgNwth-JEZntnQ6jVfG9Ivd-M34ScOcFdzBYNL_6_Kboz11R2EqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: پایگاه‌های آمریکا در اردن پاسبان اصلی رژیم صهیونیستی هستند
🔹
تمرکز ما بر اردن باید به اندازۀ سرزمین‌‌های اشغالی باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/672671" target="_blank">📅 20:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672670">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
گزارش ها از وقوع حادثه دریایی در سواحل عمان
🔹
سازمان عملیات تجارت دریایی بریتانیا با صدور اطلاعیه‌ای از وقوع یک حادثه دریایی میان یک کشتی و نیروهای نظامی در محدوده آب‌های ساحلی عمان خبر داد.
🔹
این حادثه در فاصله حدود ۱۰۰ مایلی شرق شهر «دقم» در سواحل سلطنت عمان رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/672670" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672669">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بدرقه آقای شهید ایران؛ حماسه‌ای تاریخی و رستاخیزی بی‌سابقه بود
🔹
ملّت عظیم‌الشّأن و شگفتی‌ساز ایران!  سلام و درود و سپاس بر شما که با حماسه‌ی بی‌نظیر و تاریخی خود در رستاخیز بی‌سابقهِ‌ی بدرقه‌ی آقای شهید ایران، نِصاب تازه‌ای از جلوه‌ی بعثت و اراده‌ی مستحکم…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/672669" target="_blank">📅 20:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672668">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اعتماد به مسئولان صیانت از منافع ایران را تضمین می‌کند انتقاد به عملکرد مسئولان نباید موجب ظلم به بیگناهان و شکست وحدت و انسجام اجتماعی شود
🔹
ملّت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوّه که تلاش ایشان برای رفاه و سعادت ملّت، مشهود می‌باشد،…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/672668" target="_blank">📅 20:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672667">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgyKz2dgQ05FyMAm11bYzbXuFZRWG54xJswyirovhcAY8WK3yWDPrGesOXvXA9CGB7YHGrT_uRSERzIVkbApY6v7vRWb80ncpIJUOaOviSyy1lmZGTTu6SVPdL7CT6iuJYyytlIEIPJsOGPhzLLZylD6QLxu9IA1AT-cRngi9SDoiuxbhPfa07ZDJfzQblllbxDUEA3NUGABLLPb3HgjEYeOCxxV6m-AlhbL162ONUsY-Kqej3w92jqomXpeZGx-jy9LOIyJYU9-6zekM1TxywJDykNMfyII2v6PkK7MwXc_kh4lQXQC_kSi2dJ5FmqCBIsSOvVK-b0cQzqNCRqz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقرار تعداد بیشتری جنگنده و هواپیماهای نظامی آمریکایی در پایگاه‌های غرب آسیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/672667" target="_blank">📅 20:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672665">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
از اصولی‌ترین امور، اصرار بر اتحاد مقدّس در همه‌ی سطوح است پرهیز از تفرقه و تنازع وظیفه همگانی است
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی سطوح مردم و مسئولان…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/672665" target="_blank">📅 20:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672664">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPp-TwqJ3BPZB6AJ2-gqoxy3ocaLYebKRuxsMREjHBzZjeZ99Oss4TRXKMfpjjrvUcib3uFU0dLDUmKI0cfHKddrcfZEwZoB4i9X5kOffTF9dlDZwnVwrIjvKt4g7BK59iU-npW98FbHQsk6-adJ4Aovn7_J-VtqBkJ732-7kkUAZyyMgh-FjzBFXxyEGt_DmUoQHb0ADshRe9qAUM8crPWIe_dVShHzos6XNVUi7Ra5IWuwpVuMkayzgi5GRJ0OX0U-GkaskPwvxtNWqT9myFvPDDIJhpJ_AhIOztv8d7DaodJmcvQ6SZWcP5HOfe2MqtG9L_J9F_Gm99fQVuLiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/672664" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672663">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد ملت ایران برای دشمن آمریکایی درس‌های فراموش‌نشدنی دارد
🔹
همزمان با این حماسه [بدرقه‌ی آقای شهید ایران]، نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/672663" target="_blank">📅 20:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672661">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvYgThyz873fQwveVkdbhRdJeLPKKExEeEY9_P7Sk0dGMGu8_4zdoIsUKeIGFRq0YVEb9KSuSHrXn3LQrG-2n4HdTfIJnWwvV1qDgDllI28iwIUuBQxvc6VFUCWRiNiP-PtR0G4sIcgNLNW2mpnlSlyXJjAmcARPmh6DweUbvBvQhkSl9l2zp9Eev_lsHBDvyCKYzT4qgadhjHZEm10FZfsYciZvzq31F3ia_75EbJw7nF8EPEtrPtpyoqH2XGqNUt6Xy71Si7DiVIjfap5W4359XnKXj8G7HFEUqBj8xIg3fNg_ove-Ic1_PHvVMNIhvhBcxRSLGxO8YMkqjYapWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد ملت ایران برای دشمن آمریکایی درس‌های فراموش‌نشدنی دارد
🔹
همزمان با این حماسه [بدرقه‌ی آقای شهید ایران]، نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران ایران و امریکا بار دیگر این حقیقت را به همگان ثابت کرد که امضای رئیس‌جمهور امریکا چقدر بی‌ارزش و نامعتبر است و زورگوئی، تمامیّت‌خواهی و وحشی‌گری، اجزاء لاینفک مرام و مسلک امریکایی می‌باشد.
🔹
امروز شیطان بزرگ بار دیگر چهره‌ی واقعی و بدون نقاب خود را آشکار کرده تا این تجربه ی تاریک از جنایت و بدعهدی، سند محکم دیگری بر دروغگویی، غیرمنطقی و غیر قابل اعتماد و پلید بودن امریکا باشد.
🔹
اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمّل هزینه‌های سنگین‌تر و بی‌آبروئی بیشتر است، بداند که ملّت عزیز ایران و جبهه‌ی مقاومت، درسهای فراموش‌نشدنی برای او دارد که رشادت‌های رزمندگان اسلام و غیرت مردمان شجاع خطّه‌ی جنوب در این روزها نمونه‌هایی از آن را نشان داده است.
🔹
بخشی از پیام رهبر معظّم انقلاب درباره‌ی حماسه عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور | ۲۶/تیر/۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/672661" target="_blank">📅 20:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672660">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJFcavZlMEo22j1k_UWsAKCISCO_YNPQ8r_TGXEX5u9bWWtjsX_ZSi7SSG5HLuS_UqNXiE0vaCosSMeetAp88qwn_9dCHNlZW0GoQPVt5sCR9GcMdZuMy4kV44GYd0wfTBRgY52_5tl-KmXLWOm56mAKKPLdm7I4-g6npsKWaYuGXDctH1xzja_Vb5h6AGrx53ze-q43LbeMPFHd1vP19LbiheC96ZC4zdY4XMU0mPEbEgVnfV3uvFjO8wGcwqoxkXYuQeKuU0Eb0xjOsoT-tdP5Sw0Y90z6zo89rAnl_lHsXo2uW6Oc-1dirgGeDDXOSkene2g5KhIIS8Q4ToiTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان ارزیابی و شناسایی پیمانکاران واجد صلاحیت
🔹
شرکت فجر انرژی خلیج فارس در راستای اجرای طرح‌های توسعه‌ای و بازسازی، از شرکت‌های دارای گواهی صلاحیت پیمانکاری معتبر از سازمان برنامه و بودجه کشور در رشته نیرو با رتبه ۱ (رسته‌های تولید، توزیع و انتقال) و دارای سوابق مستند و موفق در اجرای پروژه‌های نیروگاهی به روش EPCC دعوت می‌کند تا در فرآیند ارزیابی و شناسایی صلاحیت شرکت کنند.
🔹
این فراخوان ویژه شرکت‌هایی است که به‌عنوان پیمانکار اصلی، سابقه اجرای پروژه‌های نیروگاهی کلاس F، سیکل ترکیبی هواخنک و حداقل ۳۰۰ مگاوات را در کارنامه خود دارند.
▶️
آگهی فوق در روزنامه‌های ایران و دنیای اقتصاد منتشره در تاریخ های 25 تیر و 1 مرداد 1405 در دسترس عموم قرار دارد:
https://www.fepg.ir/fa/tender/368
📍
اطلاعات تکمیلی و نحوه دریافت اسناد در متن آگهی درج شده است.
🌐
https://fepg.ir
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/672660" target="_blank">📅 20:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672659">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادارات خوزستان دوشنبه دورکار شدند
🔹
ادارات هرمزگان برای فردا هم ۵۰ درصدی شدند
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/672659" target="_blank">📅 19:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672657">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiugI0H6GX5j1_89rM9lU_rel6l92F3jt7DZM8dMHBVhBOhWcvg1389olt91h_oez37BO5JXS8clwfHgMmMs65vSX-J0v-np6Ju9eKGH3xBY4eIQPpIu59ohgyffQYJqzjM8qguFR9Oma0B3aGUK-4qPmHSQqSntwSUmq70RsXIUc8l2cpOjuVZwOLxUdG_kT1scLAwiVCEgoiLWgdYGUpdWiiHM7TLzsgoWT6P4K5XmR7zRVbyBO7P1pLOKqx3LhrEo5jm_kKrfwq8_lOwciJP39HgEIXOTHEgSdvEyrKGSrP9hV0Jpxvj9gDrQiEnsIoo47TTPM5kGAjnCJV9eqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLmY80mrPDgYGfLK6tJvw44B7fhSrmaG1DNSAM6dsgHdskbqDY8Y61stN4Rcg49ktNcYvfjx80vDb2UDfS059NaCYx-xLrSJcMvLSS3S4sEtjNJW4OrgUwV48DXCqVQz7rezG4e-ia0MSuZJHjjmHcjdFwifqZ3C7xXXnUG8OwmckRT_U_jxwYnYDE6OlyLUqXG8685fvsFhJieNY1HbW4l-6vSGQ0crtN8kr060uJ65wq9S88e4N6RcvCORyd6iHB_qXlyaZphd-JxWdnNuHMF13GUOhHUONniIvRgpevx6pr1cwu0Nk5xhSPfaD2BjQ9oJmwVS0eiDCG22xdWf0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امنیت سایبری ایران؛ نقاط قوت و چالش‌ها در یک نگاه
🔹
شاخص جهانی امنیت سایبری کشورها را در ۵ سطح ارزیابی می‌کند: الگو، پیشرفته، درحال تثبیت، درحال توسعه و درحال ایجاد.
🔹
ایران در گزارش ۲۰۲۴ در سطح ۳ (درحال تثبیت) و در کنار ۴۹ کشور دیگر قرار گرفته است.
🔹
در ارزیابی ایران، اقدامات قانونی و سازمانی از مهم‌ترین نقاط قوت به شمار می‌روند؛ در مقابل، همکاری‌های بین‌المللی، توسعه ظرفیت و اقدامات فنی مهم‌ترین حوزه‌های نیازمند بهبود هستند.
🔹
ارتقای همکاری‌های بین‌المللی، سرمایه‌گذاری در توسعه ظرفیت و تقویت زیرساخت‌های فنی می‌تواند جایگاه ایران را در این شاخص جهانی بهبود دهد.
@amarfact</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/672657" target="_blank">📅 19:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672656">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glK8BvLLbBY_ZhFzRai4yxv33X1m3UQ4p06LFDmH0FTBG84QFTrFPdjbJUBkDHeDDRuOFUyZsYn7kR2Jyj4z_uxO1lpW1lrBHekC-ibW8rwUTYWfYzRN342OkWXFdQdBYi8VzzZTopKpR3FGfThrNta2nSealpXYBx0F45C0Tn-GkGIAh2_IWihUSeZov5Hsr_qEFboUYdPDMHM6ltoccrQ6ro3AGILckPl-ql4ozsgg0fNsFaAQznQVi-NgOXlSK57-2ECDuuG0HajSfD2Su-Ge4gpUfoMqpdoQVREHx7neK_Ia050kH5nfAGoaNCB8Lv8e_n_VzJkeY0qImXFCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی جواد ظریف درباره جنایت جنگی آمریکا در جنوب کشور
🔹
خطاب به ترامپ: تاریخ را بخوان و از تجاوزِ شکست خورده صدام به جنوبِ دلاور ما درس بگیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/672656" target="_blank">📅 19:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672655">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVYlVWQjdcyn6c3cihWZMCGtv5U1bogrQgQhhfB4EMgrLryhZLttNLA6lC5u3rrGuG8qleZHxdXziWJ5qxnyXrT1useP22AK7DzixPy8EAHO1kNGP4sS6KxBH0dP_XDrl0kLBjd7gZ0O_NQtBBK53qYlG9OaysJC4a06Nd1a9Zb-dYdO3rQikxsrPYYJH0IZblolIwxiPstW22-VmGEc-KRoB9GBBahIZEj9ZTAmnM7gwl_rbFmcduI0EVlaLtIVlgQUe__QlziXER0R6yJ1THK087tx2keiiSCHYB0UFEoFNXAHJqLPDA9Stvt-dP-bB5Sr6IgjMgdCph5W99_bsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهار آتش‌سوزی تانکر گاز در غرب زاهدان / تکذیب اصابت موشک دشمن
🔹
بنا بر اخبار منتشر شده در فضای مجازی مبنی بر اصابت موشک و انفجار در زاهدان این خبر توسط منابع اگاه تکذیب شد و علت آتش سوزی، آتش گرفتن منبع ذخیره سوخت شخصی بوده است./ایرنا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/672655" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672653">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA_gKA6xV88ZXI3iWa1Xm4ReWFytFJOlWwOrE1ogtNCzqgknZ9Qv9y4TEE5K2uqYFwy_fy-xR5hIc_sD2ob9eiqRk_43TNG9lWfAlIOe6GviPyhkl5EMoUMxfDGyaDRSp5IyqKwItXuFytsv-LhAnQMJ7fiM0c7_dqVaiDC783TXhI8p2JjMwrfPz_wbEaxRavjA-1_yfpK5NaMMkQ_AS8POZfLXDwN9p1n0qcsYM8W0unL_rww5atFoTmUSe8lMT8afSs8oOJxvQ6ZXkBzqtvYf5gxVBjtdyGgD751We8sMDpqvodgBxRTYj9IIrixcMoNKR-l-Qp35RI1Elbfjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای: سیاست ترامپ در قبال ایران را می‌توان در یک عکس خلاصه کرد؛ یک پل تخریب‌شده در بندرعباس، ایران و یک مسیر انحرافی فعال
🔹
این حملات خود-براندازانه موفق نخواهند شد. ایران به کار خود ادامه خواهد داد، در حالی که تنش‌ها افزایش می‌یابد و مردم عادی ایران هزینه آن را متحمل می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/672653" target="_blank">📅 19:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrlkki0w_tnF6m1_eY3whazlXbYry9K40_SClmQhP9R29Mq9aAAoC4kXBEgzIf1jK65PPZw2olFFjHGNfNcKyV-FbBKDmmS51JUbhkuCM6BdeQFTwK7tzR1Yw3w_4vVvDClP-tlOqF8gNLefT0bmPEw9j9A3ERzjIM7-r0x7CcCg0eMt174IF_FiDFtu4h2TS34OF_Y07dij_fVSstByxsnaeHB5zitoy2cklCgUP_sxWvhRKiUwtWrRAvuGmPz555TZ1J86M6sC-2DG3RUBlSnOWfCN4CIvHfoXaehYM3RtUJN5hB-OBC3bvglikRmjVkZ_O4cdR2SoYuxYu4eQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه پلن احتمالی ترامپ برای ادامه جنگ با ایران/ از حمله زمینی به خارک تا جنگ پل ها
🔹
برخی تحلیلگران معتقدند عدم پرداخت زیاد ترامپ به موضوع ایران در سخنرانی بامدادی اش نشان می دهد که او نقشه ای تازه برای جنگ دارد، چرا که هر وقت او در مورد مساله ای ساکت است و زیاد لفاظی نمی کند، نقشه ای جدی و عملی برای آن دارد و می خواهد اقدامی جدی انجام دهد.
نظر شما چیست؟ گزارش خبرفوری را اینجا بخوانید و کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3231099</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/672651" target="_blank">📅 19:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672648">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihcfW3P25QrGJ6Lrz3syhp9f3mT8f2i9O7nod-dINQjA1AUzAG18PR1jsS8941-w0uFQ2h1kGAaQXB_EHpBzMRP5UeYkvaqWI17F-ynrjF1BV-h6UiABu33-w5z1W0OWFR_NU9qwb0GscR48-bc3JUSr8fMFij209b1yjM61-k9lxllRE668heVUo-t-snKNSUPGUq7x-DZSsgWa6iT11yDyi-29yWWG1-q12bK6e2Zt8hZ6u-E8P-IcegC5ob4JTWxQlMYAyuDG9Js-8-G9A5ZjP2-ApA9CZlBBcer1iRdhVZcpt7ckkcNEdAWGtxDkmEL1NTD-ObxjA34E6PTtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تروریسم بد/ تروریسم خوب
Terrorism bad
Terrorism good
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/672648" target="_blank">📅 19:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672647">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تردد غیر‌ضروری در جاده‌های هرمزگان ممنوع
هشدار استانداری هرمزگان ‌به شهروندان:
🔹
با توجه به احتمال حملات مجدد دشمن، مردم تا اطلاع ثانوی از تردد غیر‌ضروری در جاده‌ها و محورهای مواصلاتی استان خودداری کنند. از شهروندان می‌خواهیم تنها در موارد ضروری تردد کرده و از حضور در مسیرهای بین‌شهری و مناطق در معرض خطر پرهیز کنند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/672647" target="_blank">📅 19:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672645">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_p3fI6c0b3lUSa7SoymlAU6Ba-iqxBR6fOadJMfq2h4TOgQ9NqtutI_cjyvil5WwqJUInx5EJnAuN8f6ftmFc4UgnOLKDH7VE1aYRQxf5ZoUb1_HxdOR4wW3wHNDUTpJKpojKodnpxtYW4rMKPmj4scjkCwo3n5RfzFd-RKrN0G1rha7tuUKH5Tj2xCxWTU9IkP7D1nTnR1F9aqJx3aRECka7nehr7-xjIKivphvwnXe26MEAm8ejPrYF9ZBaUt0fkUP3H9oxr_mhUJ2O6XFcR2rodmwfxC81NK_vxq0g7iAsJFlnO-aIEffWfj172Z8haWVbedp-H9lXmLNSIkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت خبرنگار بی‌بی‌سی: گوگل مپ داره تمام نقاطی رو در کشورهای منطقه که هدف حملات ایران قرار گرفتند، کدر می‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/672645" target="_blank">📅 19:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPPVajg6KzFwSTfb22Lx5XG2IVhssoFHpw_eep_9VhX_1X_0bePnhSchWwwq2fct_ognTwNzwWxaSa6hvq-DN2dIifjsqf0BMweIiK5IeJYgB9y07vNwiVCMosRNms6yQytPrFpUHdTbQcNpy6kanNE6tj3ssICGmQYYUkc_BH3EcBawiRlkxBB1wtsTl3OH4Z22iWruKdCNrf5sC0ep90M9S_JUQMr_McoX0cExuaLJhu0xgtEGbJSsvYURAbz1xbNmNRPrV4bw8nRsBKGMiRsx8-6I3tgL24rGa5flo5skz1DB2oPqWlm9vVMM57lzKB0r0fHO6tvgTqvwkKy_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر لکه و خط روی ناخن یک هشدار است؛ معنی آن‌ها را بدانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672644" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2872367cbe.mp4?token=T7X-AuZiNqLLuqZ1bJkw-LkEqwS8oZ3H5AnnKy9evEDjZFLSp0SdBfe8ULBYuaViyAopgT9ePD85AzC8-uks3rJCzVIPNktIuuKPMbgG052hmn4C_cHZesP1AdgGTuC6Jv4oq-UVVuKlMSxbaY3kTATnX92KxE6dVb2HkoayCTLVHtMJJClxdKekOP9GzQdApTlVbO2YO-Z-hJS2KJKkejWIrv_REM10JxSdtXcGTMsFnLg4-dXVNO1z-D9rkaQXggfZCuHA6jMAQviTIAct1_d_TD5ogoL3V0EWR_pmFM1hrbP6LtrgNQq6O5yLb3N5yJXLoqjSri4lhOSMp8oUELiOmH_suUTrA1-C3M1t2H7hTdUuVNwMhAK2PrAb0EWH_8MUD-tLjYHhBy4D7TDx5Z1e5L0u8IAG7qqZURUKKzAZYDfg4gfAWihEf3QlFiVvkpwO6jFTRKhn-EbBsTIWCwq96DGgPN3qWZ6jF1WokqTOEUBJfjKVK8JRL4cEPT2qL4wEZcZWkj5D9TemWSsd1GTdU4PI6-nt5J-d1y3952c0ngDK2frQKmbB6SBLxrzUhVSm-BMLBmgSUkA-egs0G_R1dTyy5oFfoS85wFvB_rLMxjPg5Z9DmibrIsNoiFEr9-IswaizuCq_Yvn1cEJR_Xg7lnC_Mzua1AnY_QlZaN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2872367cbe.mp4?token=T7X-AuZiNqLLuqZ1bJkw-LkEqwS8oZ3H5AnnKy9evEDjZFLSp0SdBfe8ULBYuaViyAopgT9ePD85AzC8-uks3rJCzVIPNktIuuKPMbgG052hmn4C_cHZesP1AdgGTuC6Jv4oq-UVVuKlMSxbaY3kTATnX92KxE6dVb2HkoayCTLVHtMJJClxdKekOP9GzQdApTlVbO2YO-Z-hJS2KJKkejWIrv_REM10JxSdtXcGTMsFnLg4-dXVNO1z-D9rkaQXggfZCuHA6jMAQviTIAct1_d_TD5ogoL3V0EWR_pmFM1hrbP6LtrgNQq6O5yLb3N5yJXLoqjSri4lhOSMp8oUELiOmH_suUTrA1-C3M1t2H7hTdUuVNwMhAK2PrAb0EWH_8MUD-tLjYHhBy4D7TDx5Z1e5L0u8IAG7qqZURUKKzAZYDfg4gfAWihEf3QlFiVvkpwO6jFTRKhn-EbBsTIWCwq96DGgPN3qWZ6jF1WokqTOEUBJfjKVK8JRL4cEPT2qL4wEZcZWkj5D9TemWSsd1GTdU4PI6-nt5J-d1y3952c0ngDK2frQKmbB6SBLxrzUhVSm-BMLBmgSUkA-egs0G_R1dTyy5oFfoS85wFvB_rLMxjPg5Z9DmibrIsNoiFEr9-IswaizuCq_Yvn1cEJR_Xg7lnC_Mzua1AnY_QlZaN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احساساتی شدن داوران برنامه محفل ستاره‌ها با تلاوت فوق‌العاده خلبان کوچولو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672643" target="_blank">📅 19:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672642">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d070710477.mp4?token=H4Evaj6DrdxDdwsT4oQjo9_-RQvghqMTqa41lYbozPPDjMArShpic2XHnqOWiDuwUUz2E3k5GvYeKlOsPVrNTzmEUcy85lHktHMXQqjkNeEQKZpkIG0j1u3pJb-5xd0PoS2XHmTLl-omOrU6SjTM9xerVu13i5Z_ziBS0Ti_PIDxPHtGtqrlUCs0Bn7s-0C2MesXrAZ-79PuAEmVsMSbOWv_wSZNj0PD0w04Yz4pKXljHosHpjM9OS6Sq8vP_cAoc1cc6nEsoCx7NynMVymqhAMZevjJfAvK9E5nY-2f0iMOZYlekFzi7-g0tNmeSICILSiOXc4iK37MnjcN2H9qLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d070710477.mp4?token=H4Evaj6DrdxDdwsT4oQjo9_-RQvghqMTqa41lYbozPPDjMArShpic2XHnqOWiDuwUUz2E3k5GvYeKlOsPVrNTzmEUcy85lHktHMXQqjkNeEQKZpkIG0j1u3pJb-5xd0PoS2XHmTLl-omOrU6SjTM9xerVu13i5Z_ziBS0Ti_PIDxPHtGtqrlUCs0Bn7s-0C2MesXrAZ-79PuAEmVsMSbOWv_wSZNj0PD0w04Yz4pKXljHosHpjM9OS6Sq8vP_cAoc1cc6nEsoCx7NynMVymqhAMZevjJfAvK9E5nY-2f0iMOZYlekFzi7-g0tNmeSICILSiOXc4iK37MnjcN2H9qLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارلسون: هیچ راه حل نظامی برای جنگ با ایران وجود ندارد چون ایران یک کشور بزرگ است
🔹
وقتی ترامپ در تنگنا قرار می‌گیرد واکنشش این است که نقش آدم دیوانه را بازی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/672642" target="_blank">📅 19:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672641">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: براساس یادداشت تفاهم، هیچ نکته‌ای وجود ندارد که به آمریکا اجازه دهد مسیر موازی مستقلی در تنگه هرمز ایجاد کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/672641" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672640">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbMxORYlCHMEorHAIlI0Oow6_UFO1sIZ6nGxLx2P2ll_MY6AyRQaQfIkQFaHG2haiCGwPvQSTe8kD6Zan9elvkvzd-G0X-mzWm8W3pSHrpXZvTdWhT29gvqxW9dSQZgBjtl4cl9Qn-GBWJ9o8xCdGu4tJ8dZxtYgNjQ7spnJKJSb41jzd0RAsBOVLIECxOvWbo18aFxXHF6kGChPLcwqxnwkIgop7SBw0G2YV43uuPXNIX-idRQ0PpMg4v3ttoLSMSwvnMkWc3gmXylQkp74TWYtxy7YTd_RwUkNCEKukl26_kk5mhVx1_1iEmb4aiZ7qESth7VmeduuOO0YtzyQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجیب‌ترین داستان ایران شاید مربوط به یک «گربه درباری» باشد!
🔹
در دوره ناصرالدین‌شاه قاجار، گربه‌ای به نام «ببری‌خان» آن‌قدر محبوب شاه بود که تقریبا مثل یک شخصیت سیاسی با او رفتار می‌شد. ببری‌خان فقط یک حیوان خانگی نبود؛ در دربار برایش جایگاه ویژه داشت، آزادانه رفت‌وآمد می‌کرد و حتی بعضی از درباریان سعی می‌کردند از علاقه شاه به او استفاده کنند.
🔹
می‌گویند بعضی افراد برای جلب توجه شاه، عریضه یا درخواست خود را به ببری‌خان می‌رساندند، چون می‌دانستند هر چیزی که به این گربه محبوب مربوط باشد، سریع‌تر به چشم ناصرالدین‌شاه می‌آید. همین موضوع باعث شده بود ببری‌خان در روایت‌های تاریخی و خاطرات آن دوره، به یکی از عجیب‌ترین نمادهای نفوذ غیررسمی دربار تبدیل شود.
🔹
سرانجام ببری خان به طرز مشکوکی ناپدید شد و گفته می‌شود زنان حرم‌سرا او را در چاه انداختند.
🔹
شهرت این گربه آن‌قدر زیاد شد که اسمش در خاطرات و روایت‌های متعدد دوره قاجار باقی ماند؛ گربه‌ای که شاید از خیلی از آدم‌های دربار، به شاه نزدیک‌تر بود.
🔹
منبع: خاطرات و نوشته‌های مربوط به دربار ناصرالدین‌شاه قاجار، از جمله روایت‌های محمدحسن‌خان اعتمادالسلطنه و پژوهش‌های تاریخی درباره زندگی روزمره دربار قاجار
#روایت_جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/672640" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672639">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhFriBXZnTeIZ3Ha3cg6FbSTXfDJkyz5bvFEMsHlcYqt9iQ-3Q2Fmgx7IPcfRXo8Fr_Vrjwgil-VKrRcxZlMWhpLAhJsJ5FZnk_1KdPQ7heGr7RpVL0uZV70VNa_9LXnoeBvHJttHeTKe7sm1bgJZhPsc9e8zKXyFA4xEOmLjZXuCifJBGoHI1qFTGffCgYGwJ7hTZzSysEuWW8Pj0iQ3Gu6uJWqdhTaRxCFRe7CkhMp8iZfLGe-xMBJMfWxpbEFxmWHO0-aNhL5_pYHLCRgMuhwPWDWR_dcf7FXptpNEevJOP-7gYoJM8JFEX33gMzwWQwa3DGljSiI84M-vKRVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی: اگر ترامپ به هدف قرار دادن غیرنظامیان ادامه دهد، امارات متحده عربی هدف بعدی خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/672639" target="_blank">📅 19:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672638">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS0Zk6fX0SuqYQvXRoXvAnG_PLmJrANna-_LYNOZW7QBrFayIbpQ45v_FWQSXzpLTmyy5hHvcc6Uw35ubSnedNdeYQaH4XW81WYYQ3mVhqCflYveVn_zmct2JuS4LurfdHMbPyx7ndonn0HA5io3wQ08HFUIN_PKG7SMeF646St11BDfeh2lx_OCLdoXG-3RjReFxmmiUWbfKvv9h5yq8ybU8-dPVShcEyF3Lzstm15aZ2s8SBCh2sPJsVm4ox_FAznFmolZqden-AbuAOwDUAN3gtM-J2w7O4_2HilnPR__x3VXaYdhYspr5n2mHjYCNs6MQEUvX0TBkqE8O6lXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
https://khabarfoori.com/</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/672638" target="_blank">📅 19:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672637">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
چت‌جی‌پی‌تی تخلفات نوجوانان را به والدین گزارش می‌دهد
🔹
اپن‌ای‌آی از گسترش قابلیت‌های نظارت والدین در چت‌جی‌پی‌تی خبر داد. بر اساس این تغییر، در صورت غیرفعال شدن حساب یک کاربر نوجوان به‌دلیل نقض سیاست‌های مربوط به تهدیدها یا اقدامات خشونت‌آمیز، والدین متصل به حساب فرزندشان یک اعلان دریافت خواهند کرد.
🔹
اعلان جدید فقط از غیرفعال شدن حساب به‌دلیل نقض قوانین خبر می‌دهد و دسترسی والدین به محتوای گفت‌وگوهای نوجوان را فراهم نمی‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/672637" target="_blank">📅 18:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672636">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11955b90e.mp4?token=LRFdxuXLOUzpOEPB2bNmgHDjoHWdfux0ieQiY7G754JEBHgm4kkwAmZ1EfQiJZ3ryarGCA7bAzq3rPR-KXph99mE5DYdiVB4Lm2fcC3vrRYTWblZqqtDqlZVDCMHxjbZhp6q3WfxFVxcmkNpYJceQ0TJV58_3ZztOPQ57StZYZsEJKDIOMpCmuqRMedkKOwgeaOgl146FWcWS2mUrFbKuHEe748e45hp_63J2XfsNWiAwWT5vQ797DhzhoO_F_tCKinbrqoFGl6xXcmf1Eey81wNJfmARC200A1U_5UoNB780P00DbvPabGEg5MuSbvdXGgTMhDdxGFzisJgZH29AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11955b90e.mp4?token=LRFdxuXLOUzpOEPB2bNmgHDjoHWdfux0ieQiY7G754JEBHgm4kkwAmZ1EfQiJZ3ryarGCA7bAzq3rPR-KXph99mE5DYdiVB4Lm2fcC3vrRYTWblZqqtDqlZVDCMHxjbZhp6q3WfxFVxcmkNpYJceQ0TJV58_3ZztOPQ57StZYZsEJKDIOMpCmuqRMedkKOwgeaOgl146FWcWS2mUrFbKuHEe748e45hp_63J2XfsNWiAwWT5vQ797DhzhoO_F_tCKinbrqoFGl6xXcmf1Eey81wNJfmARC200A1U_5UoNB780P00DbvPabGEg5MuSbvdXGgTMhDdxGFzisJgZH29AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده شمال اسپانیا را فرا گرفت
🔹
منطقه «آراگون» در شمال اسپانیا شاهد وقوع یک حریق مهیب است که نیروهای امدادی را برای مهار آن به حالت آماده‌باش درآورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/672636" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672634">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5df86f50.mp4?token=oIMmISML40scqnRNLac5jsaWXMs-D-orgq-5sXwnaKlzfteX9mb7HHIUsnOKcHh7mnUTBOXYsWsXyKfY5QsPq9CM9VWFAe1FPMPuH7Io1HGUaZjS1FBdqcQI1uirRskbP0834OszBfqosWbIbTBckShh-IAhYH-wZDItIN0ZXm3LwDz79b-Zj_t3dRhiYL7ETw8fvuWqNtNhRSoEzX-HQBUGRI_3oLJW-IroFX6GllUYOofoY1uTTZ58WiBnLDHsKqrFmxAwuhgZfAe1UOMMdM_Adm3FWV0DeiBvWFE6-KCt_PZ6uFap0syfAeoWaM9NFMfThFjn_f34SqEWCg_vYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5df86f50.mp4?token=oIMmISML40scqnRNLac5jsaWXMs-D-orgq-5sXwnaKlzfteX9mb7HHIUsnOKcHh7mnUTBOXYsWsXyKfY5QsPq9CM9VWFAe1FPMPuH7Io1HGUaZjS1FBdqcQI1uirRskbP0834OszBfqosWbIbTBckShh-IAhYH-wZDItIN0ZXm3LwDz79b-Zj_t3dRhiYL7ETw8fvuWqNtNhRSoEzX-HQBUGRI_3oLJW-IroFX6GllUYOofoY1uTTZ58WiBnLDHsKqrFmxAwuhgZfAe1UOMMdM_Adm3FWV0DeiBvWFE6-KCt_PZ6uFap0syfAeoWaM9NFMfThFjn_f34SqEWCg_vYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین بخش از تجهیزات پزشکی هم به بندر ماهشهر رسید
🔹
در فاصله یک روز پس از ورود بخش اول، آخرین پارت از تجهیزات پزشکی مورد نیاز بیمارستان‌های بندر ماهشهر و بندر امام خمینی(ره) اهدایی پتروشیمی امیرکبیر وارد این شهر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672634" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672633">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9lDxqb6iFCDQtveX_I2bcwDXqGzdsxfbC9xgzZazRtYb2l-jahMTlDRLAFR37jwX4TeSIPAtY8BuUyGXEATJvqX2EDUilJ_FFiCKycL6Qk3x2Xg2N8cBjQ38fkwk05A7AbI8xkCEomi0oPaKG-syHqUAXiNoHNyotkVulckwyf23MFPYY4vk9RH8utvSz_GE0hqBB8dvHZp6YLag9h7DnQxAVqNjGPx5nqXtcfK85uUeD1IES2LdTnMZ0Mxv945RcRaiT3vZRkTB0vCrnHnscmqb-bGLen8sZn2snciJrU9A8Lz8gpI2Jqfe0b80sbXeuGB_D27uap7hoUZQJtJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعر تصنیف معروف (مرغ سحر ناله سر کن) رو می‌شناسید؟
🔹
محمدتقی بهار، مشهور به ملک‌الشعرای بهار از درخشان‌ترین چهره‌های ادبیات معاصر ایران است. او فقط شاعر نبود؛ سیاستمدار، روزنامه‌نگار، پژوهشگر و استاد دانشگاه نیز بود. بهار با شعرهای میهن‌دوستانه و آزادی‌خواهانه‌اش…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/672633" target="_blank">📅 18:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672632">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC4GzM69-m00fIUl828LWXs5MMUqceBHQtJ5tbx0KJPLWpB_xjZOm-oLzFGzC3Gvy4LTxmdGdFBar6BtO9kEzS-tGY4RpJ4gYgSbFvGzsWpvqzTywsQH1WbKGJM41CGCdN90C8ZKMZuko_Ywf2NabDDKC-RTmBtSmP3e53KuCSJ5pbTUSwDUlKgw9S5bA--1omfzxJAPkDUGJGdE1EhZ-HAV5iU2yt014_UIJj6GZk0WSJctyKsC_Ukhu6I4QCfH_c7BsfZGR0Vqq_FYJfJGi4vr7D5ukQtNNzolSdNvMd2p5hXXcxvajJ5xMErwFvRwkuKuLvNcRTfvtmZxoYnJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفات نظامیان آمریکا همچنان رو به افزایش
🔹
پنتاگون اعلام کرد در جریان پاسخ ایران به تجاوز نظامی آمریکا، ۱۳ نظامی دیگر این کشور شامل ۱۰ نیروی ارتش و ۳ ملوان نیروی دریایی مجروح شده‌اند.
🔹
بر اساس آمار جدید پنتاگون، شمار نظامیان مجروح آمریکایی در جنگ با ایران از ۴۱۴ به ۴۲۷ نفر افزایش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/672632" target="_blank">📅 18:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672627">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae992943.mp4?token=BgkwWxq_uMdgCpT8HCt4E42f-BKNOKyYHWrowhqCESYQqzOHA4Kohx-ChPKXW2P5FdKJf9FO_t4Db0vuyqjZ3pOVA6gXRyFnk9JXGnDu8qD3Ff-1wiR8vFFVop_Lu-Hp8GIXEv9pnLlC3NwTPFCpAuZnU-89X4ow3XI9Xx2b_xq8x4JyO2bxS2dRNPBU5_7wZqBlaF9GKYk7zGBiNt3gjV0l4qWf70zAFyFaCcKmXVMdWs35bFfegUV6ULLIVaDFpgfAqN_7KACFNQ-7qhxgVUXeA68camSriDx7GAoKjkUzDFd01LLZXwLLf0IpfS6aOVxHKR2wcYXjWjc6HvASag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae992943.mp4?token=BgkwWxq_uMdgCpT8HCt4E42f-BKNOKyYHWrowhqCESYQqzOHA4Kohx-ChPKXW2P5FdKJf9FO_t4Db0vuyqjZ3pOVA6gXRyFnk9JXGnDu8qD3Ff-1wiR8vFFVop_Lu-Hp8GIXEv9pnLlC3NwTPFCpAuZnU-89X4ow3XI9Xx2b_xq8x4JyO2bxS2dRNPBU5_7wZqBlaF9GKYk7zGBiNt3gjV0l4qWf70zAFyFaCcKmXVMdWs35bFfegUV6ULLIVaDFpgfAqN_7KACFNQ-7qhxgVUXeA68camSriDx7GAoKjkUzDFd01LLZXwLLf0IpfS6aOVxHKR2wcYXjWjc6HvASag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از اصابت موشک‌های دشمن به تاسیسات آب‌شیرین‌کن جاسک
🔹
بامداد امروز، اتاق پمپ اسکله تاسیسات آب‌شیرین‌کن شهرستان جاسک هدف اصابت موشک‌های دشمن قرار گرفت و تاسیسات آب‌شیرین‌کن این اسکله، تخریب گردید.
🔹
در حال حاضر، آبرسانی به مناطق تحت پوشش این تأسیسات تنها از طریق تانکرهای سیار انجام می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/672627" target="_blank">📅 18:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672625">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799874b1b5.mp4?token=Z4Pn8_wtaDqBNfnM1zehgFYdLa05AGzscTWM8PHYrmTIeh8rqAwKNS00QSh6PNLihIyGmBEw8LbidX8o1yeoUC8ZjtCGTHW-KX_8o02wGWEBox03QITt2mMd6kq54WsYw2qw8l0qhTHzoNYtC7T3_NO6If-6Y3PZ7FLEY_DKMq-rPozd19U2xX_AxTUWZhtIoIcEyBhIQozm-XgVJj91B0rtxr-UZhrBMCUdQY3CUGEQLV3rQ48nSaJeC9xp319jqx54M0TSZTDxWOBLtvDwT4cW_2zUVlj7aDm5NbD8X6y0tN6h03lyAXLWjGSNaKtz3Qj-YKebU399H51xihVDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799874b1b5.mp4?token=Z4Pn8_wtaDqBNfnM1zehgFYdLa05AGzscTWM8PHYrmTIeh8rqAwKNS00QSh6PNLihIyGmBEw8LbidX8o1yeoUC8ZjtCGTHW-KX_8o02wGWEBox03QITt2mMd6kq54WsYw2qw8l0qhTHzoNYtC7T3_NO6If-6Y3PZ7FLEY_DKMq-rPozd19U2xX_AxTUWZhtIoIcEyBhIQozm-XgVJj91B0rtxr-UZhrBMCUdQY3CUGEQLV3rQ48nSaJeC9xp319jqx54M0TSZTDxWOBLtvDwT4cW_2zUVlj7aDm5NbD8X6y0tN6h03lyAXLWjGSNaKtz3Qj-YKebU399H51xihVDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدئویی از عبور یک هواپیمای مسافربری بر فراز انبار در حال سوختن «وایلدبریز» در حومه مسکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/672625" target="_blank">📅 18:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672624">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRg1daSD3GMrbUdpULREjJA0wO1lZtF4an3QEBUKGpZy06R7LKvvyQfuPbXj1DALnnPPBrrGveUGTK0kTKel5VuC5KGKnpGpH_KSMMTo0AjO3v0A5bqTOGCVA4RYajQt0ardUzEBDTPXTHoUr-YbZxdqMq9EHTMD3oaNsEpRG8PiqFlq9sbZS9bYADKU9vygbX8h9BiiqMqmuIVbcpXM3ND23nVVsXOa1d-uUHvLSLvKS6ZUAAKdAzeh7Xx6OyekgI_H0UiL2MqJsxlfhMfo2eA-kO5PIrENeiTOSSA9ErVUUZhy3EbVS5MmuXqgEKdwm-oPyyTpzTm2L5sKMdOxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این سلاح کوچک تعیین کننده نتیجه جنگ ایران و آمریکا خواهد بود
🔹
مهم‌ ترین کارایی شهپادها در جنگ های جدید، تغییر ماهیت تهدیدات دریایی از سطح به زیر سطح و ایجاد یک بحران "هزینه - اثربخشی" برای طرف مقابل است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3231295</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/672624" target="_blank">📅 18:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672620">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7f6b7989.mp4?token=e2Nik0roMcSJ6awMEJdwDlndsGDUzYqWL60O-LIG7NSYglCqyIFfN29G3sAlroe42urUdfnSP8Y4SjBqR8bamtwO_EdPGYr2xnMdA8d4w2ibcJ-HGDA6hWq_NrhRbe5r8BxFyDyJ_sYFO8_atlqojeCkPMdAiJdfmTpYAkKJBJtKT2uloT0tTcXGkSLUu4kN1TfkYcwnBQZ93vRqiCpsCg1rZ8RevfHBfK75GIA24qT5KLZEDkTm509DslOnWo7rdhpQ9PYo34jcRuvbICeEEqegNy8vmWIDx2nsEF9OBusGqFGQoiZmGmv5IO11Tzxwmu0VtWnUxap6D3MmJ9iCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7f6b7989.mp4?token=e2Nik0roMcSJ6awMEJdwDlndsGDUzYqWL60O-LIG7NSYglCqyIFfN29G3sAlroe42urUdfnSP8Y4SjBqR8bamtwO_EdPGYr2xnMdA8d4w2ibcJ-HGDA6hWq_NrhRbe5r8BxFyDyJ_sYFO8_atlqojeCkPMdAiJdfmTpYAkKJBJtKT2uloT0tTcXGkSLUu4kN1TfkYcwnBQZ93vRqiCpsCg1rZ8RevfHBfK75GIA24qT5KLZEDkTm509DslOnWo7rdhpQ9PYo34jcRuvbICeEEqegNy8vmWIDx2nsEF9OBusGqFGQoiZmGmv5IO11Tzxwmu0VtWnUxap6D3MmJ9iCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادق خرازی: روسیه و چین هم تصور می‌کردند ایران به‌زودی از هم خواهد پاشید!
سید محمدصادق خرازی دیپلمات پیشین کشورمان و فعال سیاسی:
🔹
یکی از مقامات بلندپایه روسیه این موضوع را با ما در میان گذاشت و چینی‌ها هم رسماً گفتند که در ده روز نخست تصور می‌کردند ایران به‌زودی از هم خواهد پاشید، اما وقتی از نزدیک شرایط منطقه را بررسی کردند، به این نتیجه رسیدند که ایران با استحکام ایستاده و در مقابل، طرف مقابل در حال فرسوده شدن است، همان‌جا دریافتند که
این نظام، نظامی خدشه‌ناپذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/672620" target="_blank">📅 17:50 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
