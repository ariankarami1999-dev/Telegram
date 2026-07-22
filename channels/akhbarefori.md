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
<img src="https://cdn4.telesco.pe/file/nWmmIbWfzOCvUSXZpld2h2pKB1Y1bN4nXJwkLgXsT2k60RJRIfPEcd70Vtpgx6cDvDnhLq_paLk3jYP-9HXIsnYEM6cm_0qqjj-si2kLhUe1iG10Y0ebltp4RKaQpc_CQjcwZX0ra63uHsp1Sl6lQIFZPkw76i4OZStWY4i78I2DumCql_KLsYTpSI6L56Pf8DwYZU_Ijic_cjEwn477RGs9ZI_pKRc7D3JKcWRAaHVHYMa905J4gEIwpyT5w08mTPzkFWpvOfu8ba8kQTrYznZ5aKMspjQTtrAhxnXciFGz2cv7zEaItqzmRz0WC08GFnFVhXfcoT4hWovI273xkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 13:46:19</div>
<hr>

<div class="tg-post" id="msg-674073">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoBOgKj22UblZYwD9t_f5_XDminOdb1VKAUJRo-qsrlqNQm1mdvuD1lJNuikLS9YBhaaOPdRG4SbQAw8kP-PElPvZIM2yiuOMh5-Pu3MPLsx6ZdCzrUFohxqQShiRggBBr9YWtmVbFtyhK0qwT3PtkIGya9upuWsSMmAhUkzmTBED9S8c0poAkyubPPdPTLJP1Y4fwOTJJemlmpGA4WZVjxWH_o0Kpeh00ShGi75pj5SsGxZu5XIz-jxo9tWtvrL-6EKNRQipw9XfuO775iVJVuzs5yFRsZlESLsfIpxmcmJIUj1Ffi1zQg-SxMr1nxfFysg1bGrel6IlCHFmst9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: نوآوری ایرانی معادلات صحنه نبرد را تغییر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/674073" target="_blank">📅 13:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674072">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای روبیو: ما برای مذاکره با ایران آماده‌ایم
🔹
وزیر امور خارجه آمریکا مدعی شد که خواهان دست‌یابی به یک راهکار و توافق دیپلماتیک با ایران هستیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/674072" target="_blank">📅 13:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674071">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
روایت برای اولین بار/ ماجرای نامه اعتراضی پیروز حناچی، شهردار پیشین تهران به رهبر شهید انقلاب
پیروز حناچی، شهردار پیشین تهران در
#گفتگو
با خبرفوری:
🔹
کسانی که دنبال رانت بودند با تصدی من به عنوان شهردار مشکل داشتند. نامه اعتراضی به رهبری نوشتم، عکس‌العملی را که منجر به تایید حکم من به عنوان شهردار شد، نتیجه پیگیری ایشان (رهبر شهید) تلقی میکنم.
🔹
آقای علوی گفت که آقای روحانی به وزیر کشور و وزیر اطلاعات دستور داد که چرا بیخود چیز می‌کنید (سنگ اندازی می‌کنید).
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/674071" target="_blank">📅 13:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJ_EPmE2qnIs4QbXi-U6lqK3AkqtYKY343rQy82FxOlHCwoVy_8Fi9zk__KNzPiPysCzhgABG3KSCCUikQae3K4AY8Y6nT_3C94JETJmr9dQ9bmGhia7NKqbr7K9RjH65kLhTO0rPptbDa5uO0e8xOiYn9_1L7YXu4-P-zxpw7hoa-dmNFy1EeQzeLsVIgsmJIt8qc4LcNMhrnrLE8RruUYGqp2ayz0L6MWzFDyGn73NvYtCtpoR8WMCX8PQG4L3-9gymO6FhyKauoItKEUGbq6p86F3RBNXvOjlSMkql3oWM4CKWLuN-gwgYjOfYcKtfN6bh4mE7evF5ZaqV-6SRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWq4v9RVevWWkiuQuQkBpjlauTR89FMLfiAuDpjozlrgS2NRvAhJ3Z_bF99gNIo5csaHmC2kJ50fXwmgscMenWE3Va9ZjMJ4Dmotphcb1nIvYky_d0FUbxLAWWCx4ZwhaNF-5jY8TOvZywh-LD0yFp1CXfwBrdvoAB5LXURhgN2AJggYL_V7J4gno6YAKmIIPgHI3zY9kr6nYvIQlyIFeiEh0gERepslTE0KEFaIwKTD2kr9Vl57YIT6wexnCVrSyVqvVNa36kXx-O0JNxiEjiMx2Ac3yTiWDq2wQS72Q2E3CGAVbNJhWEhcOXBq726A2WLkgKNpfAbzVWTogL9C9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDwXRQs_Y4QFtxEbxJPRBd1b87zgcYuNCpeu34cGbZJ_Jve_lsL10jBeHGjP57AgymfvzjHqA42QI5EhnzktV6PTqobnJSC2tvNE9VFFj_Vm9tdzB61H0TjG84GagPOpahqLl0y-pL7PfI6HDLTtYRZVRJ_WhR6nlyX98ZrMXQu6BvIHvGFvvyk0qRUlRWZB4e2XKJ3cMblJQ9ev5aXtgIp0UtZ_zYS4NDl4XTj7ZJMmFFUbeg2QvphiUiMGqDcfqunoriUPhxeFDjUCCNj0SjktHuk1XZI02D9pwe3uX9bOV14SgsYzKVoOf0CdJAPO3ICVvt-rE6MyxFzUxeylYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khqKQmMuIcUoHsph_xWXh1vCA7GDGkcDkTbSzyt8fQ5VLFAN6OMT7m8GNZ-_v1J-N6XknKgVltuHIeg6lK1iSGCb-SWXBxs1lwhpfgNZRKo7yE7d5nR_xEmGh93XUQ47FTNW4y9IYym9Gb4HnfDhs5ZwfvP8NhkWJZ0wZqUO-wz2YKec19TfKyGBErgctLG4RoSwP67J-g8zN99_SLm-Mtl956HpBKvGY8dW4jweVLYAmUS2Pf-NEhTa07BE6pp8O79KfAYn1C4n1VTmM9HVaRS_NDC-MYvr5mn2uxIrnSg5gtGeMK_mOE6pZ38KtnCksDrj96KI-lOuwKWWVCTv4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چگونه در تابستان خوش‌بو باشیم؟
/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/674067" target="_blank">📅 13:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhIDzB-2RxGA7uSC6XzFjQmwHnvaLQEdnMEU9DvZmsDeoZezWbP4a7naX9tWmlyFRrJOAGTob06qS_Icl_x5du_OD0uSdfRjtB96CLjqrPvXhhh7V_hWgKeoVevR5pZ7oNxTkcmdsQN9KONWz0AbnTtWs3mxcP-Bc2NGMg7H08ASGwOONw93hKkyTkK6rFR4HDbSO5iACzf0Xj4Wv9RuUfC4lWB-i98YIqXT7chOWyvvdg4SVh7SbQbT6sIQzD7yZX4npzJ1LbmzkbWc5DP0lNX9JrVFNNR5pRAPjeRcngzWIHI0ms9LEIclDcn4DOSISuO1x47os9ykc9WrLpGHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال: توانمندی موشکی ایران همچنان پابرجاست
🔹
در حالی که مقامات آمریکایی می‌گویند قابلیت‌های موشکی ایران به شدت تضعیف شده است، حملات ۲ هفته اخیر ایران، نشان می‌دهد که تهدید همچنان قابل توجه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/674066" target="_blank">📅 13:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911c88bf87.mp4?token=EHOHhmvtOn1rK05PBTXZ3drsz6zQq0I8RZM_Gb4i60yi8_Dr-F-g4RhcLLj8F7MEQ6zq2-S9YmoKNESPjJBLpYqqvV2UsW58T980ymg1zSA1gbhRq5Itdrv-z7_haSSJ_dmXFcC_BePTOIpbvIxYuxaRz2i-vl927AWOeh03G7F18v_un2171J4VXibKr31LOVJd9QiBukotBhsaCHe4s8Z6ngRAHv5jjYf8JHrrBIgsvuAZInD15HOpmJF9zff-lydBBwJ2miGBPeeVYszqwLUn9YA08mlX2lEJnLBYoY7AsCc27etNbxPOgtrCC4Ga7JNHulwZFMEUL74ZS_y8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911c88bf87.mp4?token=EHOHhmvtOn1rK05PBTXZ3drsz6zQq0I8RZM_Gb4i60yi8_Dr-F-g4RhcLLj8F7MEQ6zq2-S9YmoKNESPjJBLpYqqvV2UsW58T980ymg1zSA1gbhRq5Itdrv-z7_haSSJ_dmXFcC_BePTOIpbvIxYuxaRz2i-vl927AWOeh03G7F18v_un2171J4VXibKr31LOVJd9QiBukotBhsaCHe4s8Z6ngRAHv5jjYf8JHrrBIgsvuAZInD15HOpmJF9zff-lydBBwJ2miGBPeeVYszqwLUn9YA08mlX2lEJnLBYoY7AsCc27etNbxPOgtrCC4Ga7JNHulwZFMEUL74ZS_y8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماساژ آسان و مؤثر برای جوانسازی صورت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/674065" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674064">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
تکذیب فعالیت پدافند و انفجار بامداد امروز در پاکدشت
سپاه استان تهران:
🔹
گزارش‌های منتشرشده در فضای مجازی دربارهٔ فعالیت سامانه‌های پدافندی و وقوع اصابت در پاکدشت، در بامداد امروز صحت ندارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/674064" target="_blank">📅 13:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تردد ریلی ایران به چین ۳ برابر شد
حبیب قاسمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تردد ریلی ایران به چین سه برابر شده و محدودیت‌های مرزی با ترکیه نیز برطرف شده است که هرچند هزینه حمل در مسیرهای جایگزین بالاتر از مسیر جنوب است.
🔹
دستگاه‌های اقتصادی با محوریت وزارت راه برنامه افزایش سهم کریدورهای جایگزین از ۲۰ به ۶۰ درصد را با هدف کاهش وابستگی به مسیر جنوب دنبال کردند.
@TV_Fori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/674063" target="_blank">📅 13:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB4D3dvCcEPmeC2o_wijl9lGY67nQQTr5N3JR-v-1eY1d-VQXc2ICH80cGWmJJDsoAFgGXkJvzuo84P0k8l-pjqulT10DjCU63qtohAHl8BCSGxilnoa4Xyc97xQdz6wPoNbIzjuyjtZbYplmp-XkBTshd8nRXjl7h8GpszaEXaAW2lBgDGwNUES9XXR51WjsgcrNDdiY5iEWkFFXGEzcZBOy8H5x_g1NgSJUBtKIfb3t1d4WUkkeJJM71xlpc7QumNHO6R3RCgzKyCs-ovJ4ITBC9xX-OmIo0To11Xi6Cm61KfNwLdzGQmp6dNlr0wBgZL9HCggIloAvLo7drTNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر تایید سهامداران بر عملكرد سال ۱۴۰۴ بانك ملت
🔹
با برپایی مجمع عمومی عادی سالیانه بانک ملت برای سال مالی منتهی به پایان اسفندماه ۱۴۰۴، عملکرد این بانک بورسی مورد تایید سهامداران قرار گرفت.
🔹
مجمع عمومی عادی سالیانه بانک ملت با حضور بیش از ۶۳.۴۱ درصد از سهامداران و به ریاست مسعود نصر اصفهانی رییس هیأت مدیره و نظارت علیرضا خاتون زاده ابیانه مدیرکل امور بانکی وزارت امور اقتصادی و دارایی و اسماعیل چمنی نماینده شرکت سرمایه گذاری سهام عدالت، منشی گری احمد خیرخواه مدیرکل حقوقی بانک ملت و با حضور نماینده سازمان بورس و اوراق بهادار برپا شد و پس از قرائت گزارش عملکرد هیات مدیره از سوی فرشید فرخ نژاد مدیرعامل بانک ملت و قرائت گزارش حسابرس و بازرس قانونی، سهامداران با رای قاطع صورت های مالی این بانک را تصویب کردند.
🔹
همچنین در این مجمع حسابرس و بازرس قانونی، صورت های مالی بانک ملت را از تمامی جنبه های با اهمیت، منطبق با استانداردهای حسابرسی و مطلوب ارزیابی کرد.
🔹
در این مجمع، تقسیم ۴۶ ریال سود (از محل سود جاری و انباشته) به ازای هر سهم بانک ملت به تصویب سهامداران رسید.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/674062" target="_blank">📅 13:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN6PJRBaX4WcYPr3jWOM2_80GxZVAUFxLJPxI78LZgI6rTa4sW0jRN8SlUICQAqqx4D5If-pajnKSkM9y5gHC4aLtx19VUQhBVHVxXo5QgCJro4TdYAJqUI_BVsFjHNEmhzWMyKEo2o3bokLgF9XkZj7u_3GOJFu5BhCPjchO5tKrF8pbytT6imdArEwVp4Sn_-y5CZFR486EFPOylyWcFE62YVyecj55sVJY6QSpWMQ7M_jnlyE02pz5DdwXXndVrKMSy7rQoqMhpJG-Aj52ZBAV9IegPRGDXXZxunGvaejnCKOVHlOtTmRq_4Jmz-Pn9K5JTyt7vEZlnzmdE3R_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار مدعی انتقام چندبرابری از ایران شد  ترامپ در پیامی جدید در واکنش به کشته شدن سربازان آمریکایی در حملات ایران مدعی شد:
🔹
هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این عمل را چندین برابر پرداخت خواهد کرد! این دستورالعمل به وزیر جنگ، پیت…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/674061" target="_blank">📅 13:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTS4Fr4QVul5fmRlZ0XyLkSfo-8YNo3Qm7dPQSTPJ_eaVQ8N7ZEqKYS3NHuLxSsvR6fKRpFglNSzcmoQ-HkWtAiJSlSlyZRplf2KP4oaV3pbFOzWo-4x2EyDGzG-ZbP1IRzYgXyRokRi-4koejfiJU6H9DxRLoIfS49d2vb-_Z9zNhV9oGQf5MNnYtpQG5xRTAWBhU3yF_81JcHoSblpYwYxnWyl6-_A1FeAWRS-X0dS8aaAbScVLUnyxeOYL9yG9QkDr5gfLIRu3XlHmgV02oRhAn1T2HUf2mGC2TgmOjtLbJlNnsRrY77OyLl8Qw9qInpfsN9aypZTS1UoN8IBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۳۱ تیر ۱۴۰۵؛ ساعت ۱۲:۴۰
🔹
دلار امروز ۳۱ تیر با وجود نوسان محدود، همچنان در کانال ۱۹۰ هزار تومان معامله می‌شود و بهای آن در بازار آزاد ۱۹۱ هزار و ۵۰۰ تومان ثبت شده است.
🔹
در همین حال، رشد طلای ۱۸ عیار، این فلز گرانبها را به آستانه ۱۹ میلیون تومان رساند و قیمت سکه بهار آزادی، حدود ۱۸۵ میلیون تومان ثبت شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/674060" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تشییع شهدای تازه شناسایی شده مدرسه شجره طیبه میناب  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/674059" target="_blank">📅 13:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
فارس: دقایقی پیش صدای ۳ انفجار از حوالی سیریک شنیده شد
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/674058" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تکلیف امتحانات نهایی روشن شد
🔹
یک منبع آگاه به خبرفوری گفت که طبق جلسه‌ای که با وزیر آموزش و پرورش برگزار شد، تصمیم‌ بر این شد امتحان‌های نهایی به جز در استان‌های درگیر جنگ به تعویق نیفتد.
🔹
در خصوص کنکور هم هنوز تصمیمی گرفته نشده و طبق برنامه قبلی، به قوت خود باقیست‌./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/674057" target="_blank">📅 13:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674056">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h97_HtdEiL2DG8SuSB4Aw9Rcxr49j5E3iCQ67ZvVIwpA8EfRzf0KcQUs3zY2VEZ8R5k9HGPD1F9BB2cHSVOG_zibcM_iBuhGFvWvdnik304EqQF2MgY4T-aqoNFdoYaIAVpioh37H1C-27GhxTBuH80kHckU4TJPSAumX1X99xfQoNJMhL3ZldqyC1TWTgquMnXonprbXDa539hKy1lAE8DCdyF6gwKDW6oFdFZXW0TMqPaj9gwjysRP3q8jX0bcpXhyYyy8H72EZl-lZfMa7xP9lYxpw2WpjhIxzGHKN-j0E_JCtIK6vtfKDj5ZyZWASRHfTGSPTWPvyMCjiJu5Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
جادوی دمای رنگ: کلید آرامش در خانه
🔹
رعایت استاندارد کلوین(دمای رنگ) در نورپردازی، تأثیر مستقیمی بر سلامت روان دارد. اگر این اصل را نادیده بگیرید، فضای خانه به جای حس آرامش، شبیه به روشنایی سرد و بی‌روحِ مراکز خرید یا نمایشگاه‌ها می‌شود و خواب راحت را از شما می‌گیرد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/674056" target="_blank">📅 12:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSe-tkMIM9kvS5v10GWVrF36eiidp1qPqRt-FbkNeVx_NbWYe-4UEOSmWGYPLOfc-hnRTDZy3LasfmDogbwc-iZ5eEvmP__9Zjqrca1IIQEOErHTZqLhxhk2lfhL72CxpyJPlju_IvHGuJyeOT4QktyGJSA-NavK_7R0DLc6EbnKAgsFcm6AyYs5vJ3Asjp-k_c_Linzt35zncy1np_ULYvxoWnp51olWk9a35QYz_1b-q3ZUxskLGCIP3nHmn0TmNkMkS5OyBLp7HReo7F01bQI4lU-YkECSTA5hc2mQUhut0filgK1MDymtsa8sdkL84dj8vujUMiUSVMrlkim_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خالق ملودی «پلنگ صورتی» درگذشت
🔹
پلاس جانسون، نوازنده برجسته ساکسوفون جاز آمریکایی که با ملودی ماندگار خود در فیلم کلاسیک «پلنگ صورتی» (۱۹۶۳) جاودانه شد، در ۹۴ سالگی در لس آنجلس درگذشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/674055" target="_blank">📅 12:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674054">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4042d84114.mp4?token=H1DeGYrxhDr6ovaX4uBdKSzdndH86YQBkaocjlVRqoeQF6c3hosvVXJTrCuraZ7M5Zjywcp5lY8wJQEQuKHww8ik17r7GviNuhbGPRtDrtfridK0NZhbFWmPrdIlNxR44Xo1uYuy5qtsnjSN3nk_9Dc2dqUv7Ij4YD9uI4dLXxwYO87BNpMKAnTUxRFXExBYwbVZWVAvdVtob3VIoJId5XCbtxdueU-5xOnEHIdGTMCPxJtzvEVSrG2rL9Kk56hdLv2GQxlanuNXGaVJtft96dbNNunmqg2FqahK6MN16uaVTueDUNENGro36zUyJxvxRkpAKsAarZeQr0oPCqBwsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4042d84114.mp4?token=H1DeGYrxhDr6ovaX4uBdKSzdndH86YQBkaocjlVRqoeQF6c3hosvVXJTrCuraZ7M5Zjywcp5lY8wJQEQuKHww8ik17r7GviNuhbGPRtDrtfridK0NZhbFWmPrdIlNxR44Xo1uYuy5qtsnjSN3nk_9Dc2dqUv7Ij4YD9uI4dLXxwYO87BNpMKAnTUxRFXExBYwbVZWVAvdVtob3VIoJId5XCbtxdueU-5xOnEHIdGTMCPxJtzvEVSrG2rL9Kk56hdLv2GQxlanuNXGaVJtft96dbNNunmqg2FqahK6MN16uaVTueDUNENGro36zUyJxvxRkpAKsAarZeQr0oPCqBwsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی، شهردار پیشین تهران: ای کاش احمدی‌نژاد هیچ کاری نمی‌کرد چون نتیجه‌اش فقط تخریب بود/ احمدی‌نژاد سازمان میراث را به شیراز برد و بسیاری از اسناد این سازمان گم شدند و این سازمان نابود شد/ تخریب باغات در تهران را احمدی‌نژاد آغاز کرد
پیروز حناچی، شهردار پیشین تهران در
#گفتگو
با خبرفوری:
🔹
احمدی‌نژاد خودش را جزو نخبگان امر در حوزه‌های تخصصی می‌دانست، اما به نظرم تخصصی‌ترین موضوعات را به وجه بدی به اجرا درمی‌آورد که دیگر کسی نمی‌توانست به آن دست بزند.
🔹
در نتیجه سیاست عدم تمرکز در زمان احمدی‌نژاد، سازمان میراث را به شیراز بردند و این سازمان منهدم شد طوری که اسناد گم شد؛ اسنادی که برخی از آن نقشه‌هایی با قدمت صدساله بود.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/674054" target="_blank">📅 12:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0137ab5.mp4?token=CP2f3zfIkCw_aUFhgsULsubLCxGgN2qkWJYtiwBN61y7U2Ykd9v6Z6jcm0YqJzgCrNfBAaCrFwk5q2N52nezC4-3WxPso7mWeJgxI_jikVHDWLj7AfCZBk_RLZw1Etyddrc1R2_c3O9o3IsmDIdftlSpiLgWIwY6rJttul4pZn1NXYjZuB77Uk5IaqRXiqXPqSgm630w8D6zWpqWSCnK3Sk48zF-8JXBkplnH2X9tRANMhke1mAjPxFe8Fxl01ObNQAsJNswGKTwfF5OmgyaSYxYHiyAbP3yYFdD27u8yhLWd3zy72tSSdwEciUAPvKRBxNTIvYg_AY8QFYQwhuHGqicyqhv7UoqicGgyqE3wKksqq6F1XVKJrFzspHWSaZOnelvZSaaJQGOkYb76lenw-XvMCZ4YYQw91H3CopLwIl6nvZ-_nJeJTkR2_mu0tevaztw_YdYG0XdIkSvp7zFQpPGApWlNzvkGi3S526DIKaBwYKAheT8Tr8v6iqjaIKHw61PdI_HjxpaqyyNx0z1tnbNCjRCp9hnbub4H3oWUKgaDqTf6gcbKDH_qylWeY7VZ1qWueOkZFjxGXTWXaj9_GEy8shWEZRYapp2j_AhHidIgBEubWdBYM0b7kuAXBs8G2PLddgsb0RXpwAqeFTe2j_sPB4_ru7SnxSuXN8B4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0137ab5.mp4?token=CP2f3zfIkCw_aUFhgsULsubLCxGgN2qkWJYtiwBN61y7U2Ykd9v6Z6jcm0YqJzgCrNfBAaCrFwk5q2N52nezC4-3WxPso7mWeJgxI_jikVHDWLj7AfCZBk_RLZw1Etyddrc1R2_c3O9o3IsmDIdftlSpiLgWIwY6rJttul4pZn1NXYjZuB77Uk5IaqRXiqXPqSgm630w8D6zWpqWSCnK3Sk48zF-8JXBkplnH2X9tRANMhke1mAjPxFe8Fxl01ObNQAsJNswGKTwfF5OmgyaSYxYHiyAbP3yYFdD27u8yhLWd3zy72tSSdwEciUAPvKRBxNTIvYg_AY8QFYQwhuHGqicyqhv7UoqicGgyqE3wKksqq6F1XVKJrFzspHWSaZOnelvZSaaJQGOkYb76lenw-XvMCZ4YYQw91H3CopLwIl6nvZ-_nJeJTkR2_mu0tevaztw_YdYG0XdIkSvp7zFQpPGApWlNzvkGi3S526DIKaBwYKAheT8Tr8v6iqjaIKHw61PdI_HjxpaqyyNx0z1tnbNCjRCp9hnbub4H3oWUKgaDqTf6gcbKDH_qylWeY7VZ1qWueOkZFjxGXTWXaj9_GEy8shWEZRYapp2j_AhHidIgBEubWdBYM0b7kuAXBs8G2PLddgsb0RXpwAqeFTe2j_sPB4_ru7SnxSuXN8B4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی یک نظامی آمریکایی در پایگاه آمریکا در اردن هنگام به صدا درآمدن آژیر هشدار حمله موشکی ایران
🔹
سربازان آمریکایی پنج دقیقه وقت دارند در محفظه‌هایی که برای آنها طراحی شده است پناه بگیرند، این پناهگاه‌ها با فاصله از هم طراحی شده تا تعداد تلفات به حداقل برسد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/674052" target="_blank">📅 12:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674050">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e810dcc5f0.mp4?token=GRC0mL8uEo1PPkL0qS_i-99nlZzLiSPuxihbN4bIADhMYPNwAOwcUMqJ6yLN4m13Rn3kNx2pYc89dtTOoMIVgR_9tvl0ng6yu3bI4cly-2qhvl_80f2Z_PGBF-i5a3Dmo2NOzH6W35zUYWUxl0c1zJZpFUrz-2-hoJPvoJ1ZrsVxxon4_dGjwcbrB_CVpCeQPXGffEps75tlsi7469kvZHmBCo0LyyIqTC6XU2i7l5BezbSMWFukV43nv3JwQUoW8aefgk0MdrNO4hTXbVlXOCQfHJw7KbAOaIh1C2kFO9uDrkjmotNCJuzx8x67Rw2vHI6FvwX3hZ9YYIWnPT7ac39Q-RPZQCf5X2UwkgVh_3xR1nUhFFpEn_Vi5a8PX21Dy7tLlHBelSXKEtq2We3x_S_f7DR99ltOKgnV5QXpttFNpL6_eNqzdoU_1jLR25kvFKqFbEM4xxswI2GWu4EpthUyhzu8VwLMFhnS5ezNM9KYPt4NOyxRsNwbjUdVaHGmewheLYJuuh2GcwXQWtGCTJ-15USFmIHjlRCrejYMqDqrAWC56IFPhEBgLshgqIDCjuWTjM4Z4wRA5Iw9FlMh7p7n6QKbVo2p95XIQhOjmwFbxJQH5eZTtWBs9S2aXfxv5QqFijW9LndnCh-klcpZ9BGJs08yrSeBVmTrK0URBR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e810dcc5f0.mp4?token=GRC0mL8uEo1PPkL0qS_i-99nlZzLiSPuxihbN4bIADhMYPNwAOwcUMqJ6yLN4m13Rn3kNx2pYc89dtTOoMIVgR_9tvl0ng6yu3bI4cly-2qhvl_80f2Z_PGBF-i5a3Dmo2NOzH6W35zUYWUxl0c1zJZpFUrz-2-hoJPvoJ1ZrsVxxon4_dGjwcbrB_CVpCeQPXGffEps75tlsi7469kvZHmBCo0LyyIqTC6XU2i7l5BezbSMWFukV43nv3JwQUoW8aefgk0MdrNO4hTXbVlXOCQfHJw7KbAOaIh1C2kFO9uDrkjmotNCJuzx8x67Rw2vHI6FvwX3hZ9YYIWnPT7ac39Q-RPZQCf5X2UwkgVh_3xR1nUhFFpEn_Vi5a8PX21Dy7tLlHBelSXKEtq2We3x_S_f7DR99ltOKgnV5QXpttFNpL6_eNqzdoU_1jLR25kvFKqFbEM4xxswI2GWu4EpthUyhzu8VwLMFhnS5ezNM9KYPt4NOyxRsNwbjUdVaHGmewheLYJuuh2GcwXQWtGCTJ-15USFmIHjlRCrejYMqDqrAWC56IFPhEBgLshgqIDCjuWTjM4Z4wRA5Iw9FlMh7p7n6QKbVo2p95XIQhOjmwFbxJQH5eZTtWBs9S2aXfxv5QqFijW9LndnCh-klcpZ9BGJs08yrSeBVmTrK0URBR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این داروها رو با این مواد غذایی نخورید
‼️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/674050" target="_blank">📅 12:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674049">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfxz0AfojKdLdZ1b_X1KMnaQpEWyvo3J6Gkd7LWVVBkIHeW3Ce74SCAek1BOVDfTKblLnA_b6lb_0WLb7mmjT97iyo_M1Qf9yuDH8HEChNIjrzR5Y5XGddzJ_n2Jln1bBejBpL6VZg-P0oVA9NVJmJE4KQasoYISmP8I1ORhI3RVioD8gUQptEBOdy6BtBOmPKHizXlg1mKR5XPS3sU97kXk3gE3wXFSuW9EbuRANv3C5ExszAXGXNotMWAtb2C5s75jX_dDmHGRQ1Rice7tMUGuobQfYgp-KunbYvESGfH-jVod8umDSMMsdabtv3sGr0FEA_WRflBkHcq0Q-JAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس: ‏ادعای ترامپ درباره درخواست ایران برای مذاکره درست نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/674049" target="_blank">📅 12:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674048">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سرنگونی یک فروند پهپاد متخاصم در آسمان تهران
🔹
شب گذشته یک فروند پهپاد متخاصم توسط شبکه یکپارچه پدافند هوایی خاتم‌الانبیا در آسمان تهران رهگیری و سرنگون شده است.
🔹
این اقدام در شرایطی صورت گرفت که بامداد امروز، مردم تهران از شنیده‌شدن صدای فعالیت پدافند هوایی در برخی نقاط پایتخت خبر داده بودند./ فارس
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/674048" target="_blank">📅 12:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674047">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
آماده‌باش انصارالله برای حمله به کشتی‌ها در باب‌المندب
🔹
بر اساس گزارش بلومبرگ، نیروهای انصارالله (حوثی‌ها) در حالت آماده‌باش کامل قرار دارند و موشک‌ها و پهپادهای خود را در نزدیکی تنگه استراتژیک باب‌المندب مستقر کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/674047" target="_blank">📅 12:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07db88e44.mp4?token=D_MfZnd0Mpb1Vq0L7b783Y31VSlSvAVHQyo_HRVQKRcFigGrFZpDUA0LRgHjo-u3qce0ezDD2OuLS7Poeu7G0T_8bBSe0AIDRniWf8LDhJZaQCv21rCsRj9queebAQ5qgw7C-B6Snp50rGX4L0UOEs_c2cm1qFNgvNxNeo8qZWP6pw3F3__d-Md9FRqJieY-okW5xtKjLVzwyUbHD5i3Yi6pvHAWgsLjI-xxxnAEde_6scBOhA3BsLqY0Ird5NUVq7SDCKlwCyi2muViupwHu5Upfbka4kd4KmgocZTJgeIjESQDDTHmbDcrJWKaNLQZ5n1uCZl2aWJl1HspOf44lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07db88e44.mp4?token=D_MfZnd0Mpb1Vq0L7b783Y31VSlSvAVHQyo_HRVQKRcFigGrFZpDUA0LRgHjo-u3qce0ezDD2OuLS7Poeu7G0T_8bBSe0AIDRniWf8LDhJZaQCv21rCsRj9queebAQ5qgw7C-B6Snp50rGX4L0UOEs_c2cm1qFNgvNxNeo8qZWP6pw3F3__d-Md9FRqJieY-okW5xtKjLVzwyUbHD5i3Yi6pvHAWgsLjI-xxxnAEde_6scBOhA3BsLqY0Ird5NUVq7SDCKlwCyi2muViupwHu5Upfbka4kd4KmgocZTJgeIjESQDDTHmbDcrJWKaNLQZ5n1uCZl2aWJl1HspOf44lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
چراغ شارژی خورشیدی تاشو با طراحی کاربردی، مناسب برای خانه، سفر، کمپینگ و مواقع اضطراری.
✨
ویژگی‌ها:
✅
شارژ با نور خورشید و USB
✅
طراحی تاشو و کم‌جا
✅
نوردهی قوی
✅
مناسب برای قطعی برق، خودرو، ویلا و طبیعت‌گردی
🔥
قیمت قبلی: 1,598,000 تومان
❌
💰
قیمت ویژه: 1,098,000 تومان
✅
⏳
این تخفیف برای مدت محدود فعال است.
🛒
برای مشاهده مشخصات و ثبت سفارش، روی لینک زیر کلیک کنید:
👇
👇
👇
https://memarket24.ir/product/brief/47540/180124/</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/674046" target="_blank">📅 12:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674045">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv2kTOw8oxRl-pK_g5IIUhBH5Dlfhi_UKJMCNi4b-PdX7z4sCAZ3J7d2MwogRbEiHfVlq9PeR1PcuKLkRqLiR0yqMe0NUr69ZkzRizOmJSDV2ADoE43lWtC6e5NOQZytCSAYnCmWON9NuknScvh2__W7nL5sWm12mtdyQCxAhBY0L9CHN-4keD54atVkAYBif0usECnjXEmo7Tcf-MFM1TIZcKEAPZLkpJkmvWNJeS7npdSb2KL6n36egUoM_RHc_B-R9zp_BJl2cxXxJwyCpoxOq4N4uS0yNYhZjOtwjuRNh4yqR83cJRCIEHaiD57irCr7FJykzWFQqTXehn7BQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جایزه‌ عجیب برای قهرمانان اسپانیا؛ از جام قهرمانی تا کارتن گوجه!
🍅
🔹
گاوی و فابین روییز پس از قهرمانی در جام جهانی، در زادگاهشان سویل طبق سنتی قدیمی، به اندازه وزن بدنشان کارتن گوجه‌فرنگی هدیه گرفتند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/674045" target="_blank">📅 12:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=m5qrpbCcvzjlPJmOejeTZh8hv8XUQkHjrb3wZOvP7B9pF5J6Up6t_YUVJeKCGGCUBwHupEuV_grGaqmjvDXh2wqLC4YUX2D6a9ApK_W3OIiq1rISIoYpO9Hv8TlieFZExEkNHb0il5VyIy1qxjP6BOTgsOLJYArwqT-EYI1AnyKUfEycstX9lF2XYvUGtW8xZ1xh69IMpKnPbzeB_FytknYTODqOTZ238TZT7jwG9jlNr4gqyHHuBCdRXhWAdOTaicFrj1y9CsmUdDWfQgkgg3FsEK3vh0-AjXXyPyF2dmSs_UmZDF7lLxktSG6iFiNbIT2nbWwfMUGfVh5OJO8iwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=m5qrpbCcvzjlPJmOejeTZh8hv8XUQkHjrb3wZOvP7B9pF5J6Up6t_YUVJeKCGGCUBwHupEuV_grGaqmjvDXh2wqLC4YUX2D6a9ApK_W3OIiq1rISIoYpO9Hv8TlieFZExEkNHb0il5VyIy1qxjP6BOTgsOLJYArwqT-EYI1AnyKUfEycstX9lF2XYvUGtW8xZ1xh69IMpKnPbzeB_FytknYTODqOTZ238TZT7jwG9jlNr4gqyHHuBCdRXhWAdOTaicFrj1y9CsmUdDWfQgkgg3FsEK3vh0-AjXXyPyF2dmSs_UmZDF7lLxktSG6iFiNbIT2nbWwfMUGfVh5OJO8iwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: سقوط مشهد در اغتشاشات دی‌ماه پارسال را کاملا تکذیب می‌کنم
🔹
آن شب آقای مومنی، پورجمشیدیان و بنده در وزارت کشور بودیم و مرتب با استاندار خراسان‌رضوی که در استانداری بودند صحبت می‌کردیم.
🔹
بعید می‌دانم آقای عراقچی چنین چیزی را گفته باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/674043" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAMuVT5lM5kvjgPcdSpJyu7qhek4RRbi7eNsiv1YDXzr2tiMMUElJk-yBnyHeaA4Tg9ERbSbcoz6n_CZth-uALA6sfjgkULrq1jByySzS91i2ppFtYr76AC9BBinBvkjR_4fESqUaQGARDWoBRPS6_Tr0QA1y3qB2RQF2JKaGVGnHViWN2DQCL3nnCod5oTWwKeeZYAtHqxS_Xza45W_FyQqvLImDk7RQFa_n-dT28bOinMEtve_a-7tZUx7yw_GNIgS-CAfS6TNm-XA9nzcGzCSbObLOMbpkEd-rKIVGJ8vn6zaffo4xbPjNAZUK1S-gAjwNyfsvM89W-TxpvNICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlg80-_Pwf_5eXIsvnSlZ8G5p9G_0oAf1xZZ98VlWacAua77RwQBKg_I25pTaauj3QTR6aoVT0ybKY27XfFWwGSP7FS2qVqsturyGYowQHJYUA7uaYbY8Jv6POXbyDgx5SeSNjWpsOsF1d30o3Hpd2yvOTzZ2ph8Yg4uHnCHYmlFA07KPVoXNcAwHoQf_jpAifjIT-mw9UuUB0MRnykl1G6HJNhga8H95jZhSHMVebChCg5o9ucTnlV9m_LIuUUx5yilztQC82GGoyRe-HylofA72VAJLfnHQ28FeJYHK2i2bPFj-pYssTeS6RbkabmKyf_NeyPB5_7UsvhSMpZcyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از انهدام رادار هشدار اولیه آمریکا در پایگاه احمدالجابر کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/674041" target="_blank">📅 12:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674040">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd68LO1_6AnNWWidRO1lm39XFNo46GiQF3c_nCy3MUiz5g1XRH-gv5MFbqzBBKdT2VAkLor_4uwDxXqMzYR77VOmKo64hjV-whpoWwnOSFfq0Bc8Z_KrsRnI2JAv6kT4ufU-QIidQgWfB0mEszUB8PHJm_x-ogIyVXFkK5BZQd9PJg-aIprjCCse3sYJ9MMQdSsYdgM-6GulGToRK_BymOa51lTDM0y0oROJ1ROnyApHpVH0anXstDnkBNDVjyktU8-CkBs-MmfCpiao4BU1PCU5T0l_3WLzDxLQ208HvX_Q1ivcFnlVUhHBXiCUXre98t3oxlJUbvR6zQtNCZOO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام قابلیت تعویض یا تغییر آهنگ پست‌های قدیمی را فراهم کرد
🔹
اینستاگرام قابلیت جدیدی به نام Replace Audio معرفی کرده که به کاربران اجازه می‌دهد موزیک پست‌های فید و کاروسل‌های منتشرشده را تغییر دهند. با این ویژگی، برای تعویض آهنگ دیگر نیازی به حذف و بارگذاری مجدد پست نیست و تمامی لایک‌ها، کامنت‌ها و آمار تعامل حفظ می‌شوند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/674040" target="_blank">📅 12:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674039">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a25e7a443.mp4?token=i6dCZXmQLX90bgnN5lPg_7R38XxO0df5qjX4tS9bV2FNyJGZRKqWilqrJHQtHBWmwRUpqX-TeEixUPrC7gBCdupAekIcrW6p0NHyHB0bYugKAXOX1J9ank-NHRbO0l_vOarsJXSS_8Nj8YKZn3YIewg0InZe13YxUjBknffrlocq_5fCxrHV2heybxHhaGGFa44qjgxMdQV1ELThN_pVptdJpXYiTuQuxt6NPrpigBXDQmuVPS5EfF0J73_Wk6rjMuf6jxMdyuRnP1ttBLa31nKu6zhETrvGl2WKn8e8EIUpH1SiOXil64talAoGOzy7Nk3jJjVH61WsFwLn1-0LxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a25e7a443.mp4?token=i6dCZXmQLX90bgnN5lPg_7R38XxO0df5qjX4tS9bV2FNyJGZRKqWilqrJHQtHBWmwRUpqX-TeEixUPrC7gBCdupAekIcrW6p0NHyHB0bYugKAXOX1J9ank-NHRbO0l_vOarsJXSS_8Nj8YKZn3YIewg0InZe13YxUjBknffrlocq_5fCxrHV2heybxHhaGGFa44qjgxMdQV1ELThN_pVptdJpXYiTuQuxt6NPrpigBXDQmuVPS5EfF0J73_Wk6rjMuf6jxMdyuRnP1ttBLa31nKu6zhETrvGl2WKn8e8EIUpH1SiOXil64talAoGOzy7Nk3jJjVH61WsFwLn1-0LxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از کارگاه بمب‌سازی و دستگیری مهدی خانکی
🔹
«مهدی خانکی» عنصر عملیاتی و فعال یکی از گروهک‌های تروریستی؛ صبح امروز به دار مجازات آویخته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/674039" target="_blank">📅 12:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91b263bf7.mp4?token=IWoUSBppBWIoU5auMwyp_MdqDsiw7SsAExrWM7ZvnGIJSx1fLnNdSlPKZMRTyXMWYptU7yGLN2zGVlEmgmeZ7FQ0a3SRmLAQOIgdEycZPVk4TBUg73KoVdkfoMyLgOrphfeR35caS8DdR3HtbyYhmbpQrS6FyLfiX8UoxATZjpOjOGma0DBCDf5yp9TPVyFB4eYJL7rKiLifSFGc-2CMG6HFAPbaZdFMJRDwAhg98OUQxvafwwwDD3aQpNoVEV_APjvDqVWNBdrh_RZahmFXmM2Q7B6PihVMe0NIRKW8wyyob9VQhIQtyKvJHeCNGo0iYWkwQdp-FgfNNxr2RtYZMIJoi0tjHkY-6ltFWJmfGlY65FIdcTsyqkEgYj4tlHs15XcHp9kMVdLi2CqdIqgiaJgTt8QAfCQ5ZosbLeS-V2qL2BvZ-Qs4Ci5lu0BDk0ZUVQ3Z3YMZdq4YMyUAo5SpfIrJXwe0gnbRp2tV9rOnwqtZbV3Us3BMSQLLuvlF5UVLa9R-zpZuGvu7QbFzYXY7Vm1TNCBraQxncWUWpqrusX8jXY4Ep107tqVu6iap-2m12PXGQQ6ng1DAmZVV5BPcNcTDHu5FjmvNmmkKGSUNIf5Q3gKmaQvRbzp8KfmcviU9fsBcIOMDboJtKjM3ElHamXb64jg7MNjMEQES-CvCCyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91b263bf7.mp4?token=IWoUSBppBWIoU5auMwyp_MdqDsiw7SsAExrWM7ZvnGIJSx1fLnNdSlPKZMRTyXMWYptU7yGLN2zGVlEmgmeZ7FQ0a3SRmLAQOIgdEycZPVk4TBUg73KoVdkfoMyLgOrphfeR35caS8DdR3HtbyYhmbpQrS6FyLfiX8UoxATZjpOjOGma0DBCDf5yp9TPVyFB4eYJL7rKiLifSFGc-2CMG6HFAPbaZdFMJRDwAhg98OUQxvafwwwDD3aQpNoVEV_APjvDqVWNBdrh_RZahmFXmM2Q7B6PihVMe0NIRKW8wyyob9VQhIQtyKvJHeCNGo0iYWkwQdp-FgfNNxr2RtYZMIJoi0tjHkY-6ltFWJmfGlY65FIdcTsyqkEgYj4tlHs15XcHp9kMVdLi2CqdIqgiaJgTt8QAfCQ5ZosbLeS-V2qL2BvZ-Qs4Ci5lu0BDk0ZUVQ3Z3YMZdq4YMyUAo5SpfIrJXwe0gnbRp2tV9rOnwqtZbV3Us3BMSQLLuvlF5UVLa9R-zpZuGvu7QbFzYXY7Vm1TNCBraQxncWUWpqrusX8jXY4Ep107tqVu6iap-2m12PXGQQ6ng1DAmZVV5BPcNcTDHu5FjmvNmmkKGSUNIf5Q3gKmaQvRbzp8KfmcviU9fsBcIOMDboJtKjM3ElHamXb64jg7MNjMEQES-CvCCyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیروز حناچی: مردم انتخاب کردند در جنگ کنار نظام بمانند و مقابل دشمن ایستادگی کنند
پیروز حناچی، شهردار پیشین تهران در
#گفتگو
با خبرفوری:
🔹
دنیا ایران را به واسطه تاب‌آوری و مقاومتی که از خود نشان داد، تحسین می‌کند.
🔹
قدیم که جوان‌تر بودیم در خاطرم است آمریکا سر ناو خود را به سمت کشوری کج می‌کرد، حکومت ساقط می‌شد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674038" target="_blank">📅 12:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674036">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ffb7964c.mp4?token=Guv8nuXNDrVWnOC2XgzYPYmN6f5xhzjfGjQkcNC6MqUBkc7qyOAqQWjGxGLgNhw1Hb6SZUWD6mEfHsZHg0CSAX-hRuoDUsTiCztrAX32OktiwSfU7w-50RVJh_ugIr4yT7luAK9EHFHS0k0hMbZE6_xvX4_QD4c2hyMlX3fhg3WJRD25k5MmvG-b14CL7JXK8zI-N9g1IrgNBUljxT0UqX-Y9s1RPHGv1JQHbSxgeK_K4tyD8ey5XFn8aMYtv_sLjy2iuh4KAD-0xpETx5_hipuadR67c1GNATMEHL6oUnvPiiJKulIW5BAhgfKp6VNAGGg6-ts9rVT1J0RyvlF-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ffb7964c.mp4?token=Guv8nuXNDrVWnOC2XgzYPYmN6f5xhzjfGjQkcNC6MqUBkc7qyOAqQWjGxGLgNhw1Hb6SZUWD6mEfHsZHg0CSAX-hRuoDUsTiCztrAX32OktiwSfU7w-50RVJh_ugIr4yT7luAK9EHFHS0k0hMbZE6_xvX4_QD4c2hyMlX3fhg3WJRD25k5MmvG-b14CL7JXK8zI-N9g1IrgNBUljxT0UqX-Y9s1RPHGv1JQHbSxgeK_K4tyD8ey5XFn8aMYtv_sLjy2iuh4KAD-0xpETx5_hipuadR67c1GNATMEHL6oUnvPiiJKulIW5BAhgfKp6VNAGGg6-ts9rVT1J0RyvlF-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور می‌تونیم هورمون‌های شادی رو فعال کنیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674036" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674035">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">مدیرعامل شرکت توزیع نیروی برق تهران بزرگ در برنامه زنده تلویزیونی تهران ۲۰:
همکاری شهروندان تهرانی در مدیریت مصرف برق کمکی ارزنده در راستای کاهش محدودیت های انرژی هموطنان ما در جنوب کشور در شرایط حساس کنونی است
┄┄┅┅❅❁❅┅┅┄┄
💻
وبسایت اینترنتی توزیع برق پایتخت
www.tbtb.ir
┄┄┅┅❅❁❅┅┅┄┄
🆔️
@tehran_roshan</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/674035" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674034">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8d6SjuLqSk1_Viq7RRxvoMDxr3WCUemCIkipVQFzVX4P3Hsj9Uox9lyk29EWyINJz6DW7_G2UhK_mNJrSCbJt4V_sHDCPqodUgMxblwB6UPCGE1K9iurfIT3_UwNvabvJP7N1WVMsI_1uFQ_0vgjgYEQZwdMP3b_WU94vsL8mMPIcUclFeulKJpaIA1e3PByKOVvhPII1Jsh1OyqWuMUUm5jFRta1IeHpHNfGvM0NFnHmWja9BTOXiy3IGPMe-7o9Pt-DfTepNbUOeVQ1th0oNEsJPu3HhRbU6ese2pq4wFSxHOawGsbuzP3V6P1IfvinDsWpGowZhywwIfXYMq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارلینگ هالند روزانه ۶ وعده غذا و حدود ۶۰۰۰ کالری مصرف می‌کند؛ معادل تقریباً ۲۴ چیزبرگر
🔹
رژیم غذایی او شامل مرغ، پاستا، استیک، ماهی، سبزیجات و عسل است و تا حد امکان از خوراکی‌های شکردار دوری می‌کند.
🔹
جاشوا کینگ، هم‌تیمی سابق هالند: «او مثل یک خرس غذا می‌خورد.»…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/674034" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674033">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSXxO_sGwzUGRKAlAxkMxJxE2ClLsd78F3_-qrXoSdfIVGtXybrwOLxGI8reA5d7n4T3XcdIi2a1_pE5jj49Mubfrz-Gl7YbUiZzBhCEDW1lVjWj9SDQ7EHsIcIygykihAFOpSHyXTUV-1IsQVgJKaCgVar25HKqfQHMVgd8aVAtkK07UjDHhlnOt2lzzMSZ-mCDUFj4uIc65d2d7NTpJxjrIlcCMy9i4qwxObDMAOiYNw3Z-i-UxVn_b6RaJqxchyR1pkFeZq4cpY4FdWwpWlt1qo6alFhfdhMd6GQKkN-wGm1nZILiqAQEOZ-0Ityc38NNt64bH-mYc3AzPB6ctg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخی منابع از بلندشدن ستون‌های دود از فرودگاه ملک حسین در اردن خبر می‌دهند./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/674033" target="_blank">📅 11:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: پاکستان میانجی اصلی ما در مذاکرات با آمریکاست
🔹
در سفر وزیر کشور به پاکستان و در لابه‌لای گفت‌وگوها اگر مسئله‌ای در این زمینه باشد هم منتقل می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674032" target="_blank">📅 11:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674030">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
برخی منابع از بلندشدن ستون‌های دود از فرودگاه ملک حسین در اردن خبر می‌دهند./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/674030" target="_blank">📅 11:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674028">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfTjjqlelx2OfaHVOcsuBAZ6hOmRGq9xtpAAXrkWNaxAwbLam5ed1OTkfbFIVetWMyljstWLfJwZHWqJP9dxGcibLTm3zg91VOaLD8qPlF9DqeJ9-Rm9bREzisaU7AAfvR9UBBHhe4YCLJw0aCIl72gJxbPeJc2Xu0AwHdMNFjHdKl4uesHt9_I--56S_uy-eRyYoU4CkIBLTPpJ9Z6rXY1AqyxjY8w7gEZQDEoskpGYNCLRIr_RXmPQMddIq46FHM2GqAtMhin9T3pTKF-1JELlTXnGB4HwqFel6IWitxhp7R_h1xJESAmodrqm4r5ldyklJ_FqboWT62IV-d48bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHGx6YN-bsVvLa4UntCIWL78wseia_YN0LW8EWMAuopZnoRHcdAnb9-NcXGqalC_MNtrmoNUMGtaM6pnR_zM3WwT3WuuUUqHHsO7m3W4JxZrqeXZAD8U50fJ9EZ6ixTNIr0ikKADFukfKG4AHFF9EvkJb4c6jg4py0ocKDtqZiGGrzqKeeHtCjfV6w9R5H3TYoDj1hFQLrHcOqMluhAfJq8dKjG3RXWOxlYIYEpF8RHGva5ojCMUnjzX5HLeuGRL_WdST7S__QLivRe3PoPIlVFN4qDMoZ8RVJ9rZSmeX_fpptUI_E0TCjfWWibBfgRa6CPxEbOzpJlB3qBDl5eLMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اردن
🔹
منابع خبری از شنیده شدن صدای انفجار در اردن خبر می‌دهند.
🔹
برخی منابع گزارش می دهند که عقبه اردن هدف حمله موشکی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/674028" target="_blank">📅 11:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674027">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6N4jLLs4E3Ej28cPs5zvLvXwrhnibw_e50ADpFk-dqhpHhB01EV0zPOdxpB-eEtEFkr7co7kvNuGh_SrFbsvtOojzcMtT3RyqbU_7UZX5xYl6GUwfV9EcwjYRaYGW2u2igTr2-WS71gft3yBQctRAyazM0alhSOpPhddqaJ7dQ-VF7mM9Bb40gR65UC3FyxWyyawPmZHAnLxKbRzKU2_w_tIiKNRxr0GrurYqWiFgNRL8950TtFUBc7eKp9TkUl7xA6fmjGw7oDyo-NVSbj_fb1qwuRGUExcCm67qbKbMXCEb7ZD3r1PzMi7fiwhXelabqoFkLIf0gLTGQOwO967g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین حلقه ازدواج جهان، که مربوط به ۳۲۶٠ سال پیش است، متعلق به ملكه "ناپیرآسو" همسر "اونتاش ناپریشا" پادشاه ایلام می‌باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/674027" target="_blank">📅 11:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674026">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5ipRCQFfQIOj0SfDdQ2ZOYCjtdvnUsyq05YJx2jSeiGCUVjui0a0PtNnEmR9UhoCDxgLbkvXKPiIVX9Imbu3zXMNbchNtIley9Tnu9aQtxYmhRW-f6cvUsFiH_XGnqt2OYfPoqFBraUu8KyGrBzipEBXxi5LgSFkleTshAtmiG0KgFCwpNV199kqotgSIcTvTBYonaQPwJf0PQqIcWkz0B798C9HK07XVDpha6Wqwu-W1idKmoopGpbP-d6QFGhQasE8-8-GMs887jcdGXILSkAnv2MmcsCl8D42jvzL4QVU-Z7z3liyWwRn7J-y4Um2fYaobgNkUr21Oacd3kbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشیدن ۵ فنجان قهوه، دوست یا دشمن قلب؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/674026" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674025">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUoOwgbsrymAKEvZLRvcUpY5H8tAojJV2XMygJYm_M1o8LfJsXOAC0OQbUlsWhcsf2uxeJ83iV7vpKtX3rOBWYX6qSxu3UX2pRO3AG91SIN3t5d828JtbbB5vIMCeJFjZMk7kCnwRoZ_VdYTGfwEhtPC2e55wN2AN46oRrzgl8vCHtZqGds4xhdhnD2AZ1YXJW2JgGiOlc1WTb6NvsFjks_vSJgpx45WKtwc71BvHL6UKjwS7JM0E-B-akSv-NEmebtdywonEovHK6UaBgA9GVJlX7xyGHVAzlkZ0i1pC2T9Lc-SfRwJdeo1uH9Z4oZpWKyJg3OcGZJKTGKwbRboLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بانک کشاورزی جایگاه برتر نظام بانکی در حوزه صیانت از مشتریان را کسب کرد
🔻
بانک کشاورزی بر اساس ارزیابی بانک‌ها و مؤسسات اعتباری غیربانکی که توسط بانک مرکزی جمهوری اسلامی ایران انجام شد، جایگاه برتر نظام بانکی در حوزه صیانت از مشتریان را به خود اختصاص داد.
🔻
این رتبه‌بندی در چارچوب مأموریت‌های نظارتی و بر اساس الزامات قانون جدید بانک مرکزی، با هدف سنجش میزان رعایت حقوق مشتریان، ارتقای شفافیت، بهبود تعامل با ذی‌نفعان و تقویت پاسخگویی شبکه بانکی انجام شده است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/674025" target="_blank">📅 11:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674024">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI0W_3Q9xT8vgfLGWtsCgeaXvh_ig4xqp-M_XX5-FNPTRUPz-jI-dtJeHDNQg2W4xSPo0O4Iym9YxVZ1W9T5z0YsIsCVzY8IiUPOUfoGd3XsDbzCZbMlzHcg2HTOAJOceqgQt-YsD75rPs5U1b_YsZY4h7v2gUoRDEwYwdRehn4cFWLxQc0-7OI4hewyjYr01V7RjrQeyj94T13Gq9CcSgBc9AOy1RX3LqDQXbzxm3w_iM5WTMj23F7gGt3ExT3WUhFspibnyjEpsCbNwLK-Dgut9KuMkPba2YnRAm82mo3vlI807jEUWyn5CghPfEBeJRQaN2g8ON4BqPOz9ojrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۳ دلار رسید
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/674024" target="_blank">📅 11:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674023">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5ff34b00.mp4?token=nFt7sHiFtQL3RY6xzd9NAlCmDTHKBF0OWnCdorgXeobf_DYAhNat30zMCjQg5wijUSM5WR0UQcd5Sdo5jrT-Ini_EZRhjw8K3GNV0LWpccWfscoAjvtcNQGr0njBvL66GgwT7VL5SVAE1ighp43EsmJ9ZkxxN0dnD3CO9rsocBmIZ7EcGFOj0EEyDWtIVlFpCuMX_aZsgwiEUsUDxka5EDtWLL8ioF-EGcba3VR1ECqgsad4MIKRwjDZgADHpscnC12B8SQu7u41hCyGwu5FAI2Xp0LR1gGjyF-_7AnKJ6IP8pJwzijTUq8i_OglUTq_QvRz02W8YNfy9VZyEvkl9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5ff34b00.mp4?token=nFt7sHiFtQL3RY6xzd9NAlCmDTHKBF0OWnCdorgXeobf_DYAhNat30zMCjQg5wijUSM5WR0UQcd5Sdo5jrT-Ini_EZRhjw8K3GNV0LWpccWfscoAjvtcNQGr0njBvL66GgwT7VL5SVAE1ighp43EsmJ9ZkxxN0dnD3CO9rsocBmIZ7EcGFOj0EEyDWtIVlFpCuMX_aZsgwiEUsUDxka5EDtWLL8ioF-EGcba3VR1ECqgsad4MIKRwjDZgADHpscnC12B8SQu7u41hCyGwu5FAI2Xp0LR1gGjyF-_7AnKJ6IP8pJwzijTUq8i_OglUTq_QvRz02W8YNfy9VZyEvkl9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرمای واقعی جنوب، از دلِ مردمش میاد، نه از آفتابش این روزها یک ملت مهمان مرام و معرفت مردم جنوب‌اند اگر جنوبی به خودت افتخار کن؛ تو پرچم برافراشته مرام و معرفتی #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/674023" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674022">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قوه قضاییه: فیلترینگ سایت فوتبال ۳۶۰ ارتباطی به ما ندارد
.
🔹
رویترز: اسپانیا به ممنوعیت استفاده نیروهای هوایی آمریکا از حریم هوایی خود در جنگ علیه ایران ادامه می‌دهد.
🔹
جانشین فرماندهی انتظامی کل کشور: در کودتای دی‌ماه، مشهد جزو اهداف جدی دشمن بود./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/674022" target="_blank">📅 11:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674021">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea9b7e62aa.mp4?token=BosjTKGMAkiN2G60JWNzS4mIPNV5ejqkA_IVwJDwbJ7jivacJdkQ2jtc0jqdPeQz61mhydAqSTsA-ZtTNIZWl1pIWf2vJw6zUJeG3qUHJ8asm0vMts-RD4jx1UUAe1WxwmLnyedBYJI7ltjE6aG5l8fn6gQ6CKn3TH-hv7T8h576xDE_oo3UfJrbBgPZadcp51rFkKb_Ok0OWDVTMxWidokePMYT3v6z-SLyAss0CPId1gvqH4j73y-s6SSdVIw4_YeHKeRXpYqSmiGKXjdpDQfVnrCjWjXDjDE9FMrVCU9EGzied3laQGJc2NOo4LFWW_xUkp8qqWkBpcr0rYE18Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea9b7e62aa.mp4?token=BosjTKGMAkiN2G60JWNzS4mIPNV5ejqkA_IVwJDwbJ7jivacJdkQ2jtc0jqdPeQz61mhydAqSTsA-ZtTNIZWl1pIWf2vJw6zUJeG3qUHJ8asm0vMts-RD4jx1UUAe1WxwmLnyedBYJI7ltjE6aG5l8fn6gQ6CKn3TH-hv7T8h576xDE_oo3UfJrbBgPZadcp51rFkKb_Ok0OWDVTMxWidokePMYT3v6z-SLyAss0CPId1gvqH4j73y-s6SSdVIw4_YeHKeRXpYqSmiGKXjdpDQfVnrCjWjXDjDE9FMrVCU9EGzied3laQGJc2NOo4LFWW_xUkp8qqWkBpcr0rYE18Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بی تابی پدر و مادر فرشتگان مینابی از آخرین لحظه‌ای که فرزندان تکه‌تکه خود را در آغوش گرفتند
🔹
از پیکرهای تازه تفحص شده شهدای میناب، ماکان هنوز مفقودالاثر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/674021" target="_blank">📅 11:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674020">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef08200e3.mp4?token=NPJO7U4ynEgAHy4goMvpGxAO-UFYNZOEEhMo6XkeKWFAeuTg0IPAiHp86GMNmpxjStW_85VL1s7jDPwGNCvEk6FICwkUJDcsb68OKyMr7y1qHyb_d81OnZek7tBORdHY3kh2RHWKkvhi8k55qm-AsqIdbmduPS8BMX-pi-Yg5pisMKmWTVbyi805WKQPbdIAuOIAV3LHmbbi4T7511lfYHSg9pL9HLhEG4R8XH0kGw8ptt26aVhP9payWhMMHyp9naO16BN1sI5-R0MkUvpZtkMmUNH35ZqJXomngGfkCP5b2F6exEuTY62LAF7KhCDEx0VErEJogh1NZG8El9XHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef08200e3.mp4?token=NPJO7U4ynEgAHy4goMvpGxAO-UFYNZOEEhMo6XkeKWFAeuTg0IPAiHp86GMNmpxjStW_85VL1s7jDPwGNCvEk6FICwkUJDcsb68OKyMr7y1qHyb_d81OnZek7tBORdHY3kh2RHWKkvhi8k55qm-AsqIdbmduPS8BMX-pi-Yg5pisMKmWTVbyi805WKQPbdIAuOIAV3LHmbbi4T7511lfYHSg9pL9HLhEG4R8XH0kGw8ptt26aVhP9payWhMMHyp9naO16BN1sI5-R0MkUvpZtkMmUNH35ZqJXomngGfkCP5b2F6exEuTY62LAF7KhCDEx0VErEJogh1NZG8El9XHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر زهرا میردادی و فرزندش علی سالاری از شهدای میناب بعد از چهار ماه تفحص پیدا شد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/674020" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674019">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شبکۀ ۱۲ رژیم صهیونیستی: در پی شلیک موشک از ایران به‌سمت اردن، صدای چند انفجار در ایلات شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/674019" target="_blank">📅 11:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674018">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اردن
🔹
منابع خبری از شنیده شدن صدای انفجار در اردن خبر می‌دهند.
🔹
برخی منابع گزارش می دهند که عقبه اردن هدف حمله موشکی قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/674018" target="_blank">📅 11:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674017">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c0200817.mp4?token=Ut5H4iRzhdV7e8WHhYoq8zKjEO3dEMjDPv54HabvrOvLThDyIX4em1Y0wSLI-GxPqSSlLW9lGxWLFfFDTsyRMDrJn9DU-gpuy6dnoS2DNAW_13NuLxbZpYChOQcrQEXcdkVSiFHDIljgzgHESiMxizTTgzNt8Z5yEoM1IRhNPxuvaqO4Nn5uY5166mO28HcYuSEdVBJn0vTgAtnBhTHTILjeQ_lcGYq8-7csm66ZcUneg8dEFt40yC0ImZ4MX-I-4zBLRb5WqfdO3LXaSJxTWMWt-2NLLmoj8tEcL_ukem4ZwUhm3JHH4850WJpT7pubTHge6bt-nAkmAfZ0ffsN_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c0200817.mp4?token=Ut5H4iRzhdV7e8WHhYoq8zKjEO3dEMjDPv54HabvrOvLThDyIX4em1Y0wSLI-GxPqSSlLW9lGxWLFfFDTsyRMDrJn9DU-gpuy6dnoS2DNAW_13NuLxbZpYChOQcrQEXcdkVSiFHDIljgzgHESiMxizTTgzNt8Z5yEoM1IRhNPxuvaqO4Nn5uY5166mO28HcYuSEdVBJn0vTgAtnBhTHTILjeQ_lcGYq8-7csm66ZcUneg8dEFt40yC0ImZ4MX-I-4zBLRb5WqfdO3LXaSJxTWMWt-2NLLmoj8tEcL_ukem4ZwUhm3JHH4850WJpT7pubTHge6bt-nAkmAfZ0ffsN_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان نام فرزندان «الهام علی‌اف» را می‌داند و تلفنی احوال آنها را می‌پرسد
رئیس تشریفات نهاد ریاست جمهوری:
🔹
صمیمیت پزشکیان در روابط با کشورها خیلی اثرگذار است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/674017" target="_blank">📅 11:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674016">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATjv1HQDSt4Xc7bsPNLc4fVEbtyIjrsNcgvlB29xg-ToyaVWt1VGURIAxIpvgQZSj557GwP1Ip_8IqkIp6c6mB889GP_5ncQ_xbhH_d9_wnz8rGTmTe6I6AUg-FIBhItPLkhRU4SgO1YhK8e0DHqEFawdwhzN28-rT8Ex6y2FiLXSnu-XFFWADeIat2909Je9TWgfGOkgfSm175p-Kwb4p5lc25sy0doIDzlYAm-154sXaRMeBnlIusUOGWGhltYp4D6-0YUO3SS-lRYYaMseGpYRF-AyGLGfTiZjv9tJznH9-QgIcw2QufQ92LhcZymCzSPr7uSuJborqSNZM2tlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده کل ارتش: پای کثیف آمریکا به ایران برسد با هرآنچه داریم با آن‌ها می‌جنگیم
سرلشکر حاتمی:
🔹
دشمن به خاطر بغض و کینه اش از رزمندگان ارتش، هرچه در توان داشت، علیه آنها انجام داد ولی رزمندگان ارتش جمهوری اسلامی ایران راست قامت ایستاده‌اند.
🔹
در قضیه جنوب اصفهان، آمریکایی‌ها تصور می‌کردند اگر پایشان را در ایران بگذارند، از آنان استقبال خواهد شد ولی با تنفر گسترده و ایستادگی وصف‌ناپذیر ملت ایران مواجه شدند.
🔹
با نصرت الهی، قطعا بر مشکلات فائق آمده و دشمن نیز بیش از پیش، در رسیدن به نیات شوم خود، پشیمان خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/674016" target="_blank">📅 11:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674015">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
جنگ تجاری جدید سگ زرد با ۶۰ کشور جهان
🔹
ترامپ در حال نهایی‌کردن تعرفه‌های ۱۰ تا ۱۲.۵ درصدی علیه حدود ۶۰ کشور با بهانه «مقابله با کار اجباری» است؛ اقدامی که حتی اتحادیه اروپا را نیز هدف قرار می‌دهد.
🔹
همزمان، تعرفه‌های ۲۵ درصدی بر محصولات برزیل و ۵۰ درصدی بر کالاهای کانادایی اعمال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/674015" target="_blank">📅 11:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674014">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQhFN2q5Nb_xt9lDDwo5YAw9zHxeBe8fzJIvZCu_FSZYr4s5adLZC3kjtM7mPdc6TKgv3DHESxR1QpgX02I2DNIc2bB-x-a7gXQiRAKReLEj6x_RO-Hh5r4X9RKVkDIsGW9iQ6qBaS0osT4nUUSe2_8mM07SJcLSjFYixlzlOBdbf1UiGxKnf7V3YQn7R0cflBqhzL6FTYdSPu9gck2J7-CMytdI3gXbAlf7opJKPPEdNos1iZI_uw8cBz8F7kbYyN2Ld-fqGZtewbTra7ccOH8wNsPLeiesCS4PDINmGnoBRZmd8VBNtlpIRD6kH73Jehgugk0mX-HBO1hJtViSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۳ دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/674014" target="_blank">📅 10:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674013">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f520b6b90c.mp4?token=vKDWJC0oC4c3pXm7C0QlsdrR_rKj4IlcM_PW9ayX9yx6GK5S6WGrlBemjV9mI7MSbaxu-wUZHPRMMVO-Usp54VzUp6vMYfMtwhK63rVkfpe4Nt78hqilPaPMxcHEzS_wFqfjp6a7DG8qOSSXd_yDKBxqv5dVBuxxWpFvxfexameeDTDsjRhl2CEPPB8Wb2sReyu2CptrYhVODO4x3xd1iwB-X6K1smGopGw3mzGWe4kcxuvI_Vx5FewcpvXBeixTY2ewmpIQPoracCzYGwKF0DXI-uriXNMEvwm2Lo-P4pL-_4rDecz9X5KfR-e4iBMpNpOvA4DdqF3ibvftQcGykg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f520b6b90c.mp4?token=vKDWJC0oC4c3pXm7C0QlsdrR_rKj4IlcM_PW9ayX9yx6GK5S6WGrlBemjV9mI7MSbaxu-wUZHPRMMVO-Usp54VzUp6vMYfMtwhK63rVkfpe4Nt78hqilPaPMxcHEzS_wFqfjp6a7DG8qOSSXd_yDKBxqv5dVBuxxWpFvxfexameeDTDsjRhl2CEPPB8Wb2sReyu2CptrYhVODO4x3xd1iwB-X6K1smGopGw3mzGWe4kcxuvI_Vx5FewcpvXBeixTY2ewmpIQPoracCzYGwKF0DXI-uriXNMEvwm2Lo-P4pL-_4rDecz9X5KfR-e4iBMpNpOvA4DdqF3ibvftQcGykg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع پدیده‌ای نادر در سواحل شیلی
🔹
سواحل شهر «واسکو» در شمال شیلی، بر اثر تلاطم امواج با مواد آلی، پوشیده از کف سفید رنگی شبیه به برف شد. مقامات تأکید کرده‌اند که این پدیده طبیعی هیچ خطری برای سلامت انسان یا محیط‌زیست ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/674013" target="_blank">📅 10:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674011">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سخنگوی وزارت کشور: مسائل قانونی و شرعی گواهینامه بانوان حل شده است؛ مقدمات آن در حال انجام است و به زودی شاهد اجرای این قانون خواهیم بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/674011" target="_blank">📅 10:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674010">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee7eZOpNHOGAmf-ewArdhl3tRlRawkT56uPOXZSLPlepScVypD1wYtW1NlGtyklX54fo7qZ0ZEPA6SMlYpMW-FnEj0A1_s4Q0Es1P804a_Hm3OwiwARc84tJcI7FNZgczWxFmAtk__bePofGdBH3RyEwwRx7OYPNZFtuubWmvh_TsLdaShTDJ1NpGrUI2wIgpyIuMvConS-E7U1WjTe0RZao37H6OCffAVuOEc4hE-HNSqADPTxP2DJrHz52X8R95YZiOXHisDyVJYabTXOJ8dI4rUIYUNQWaz3nIVKNr9Cw_5_fEoa57_wjNKZ9zn0eAibTQaIqPk1D_FnFDfw5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول جام جهانی پس‌از اتمام بازی‌ها
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/674010" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674003">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJx-boLqTNx7N-r4tieVdUIJxzb0u6bolHelPMlzZejbqpfon0PwzLPSrNZunGbMyH5-djl0a5WxzvlR-nrWD6LZwq979LR7vooOcryGsCPjt551DLEOorQdqVPAVlE9ciTUjaE-S4a0YKQUIXQndDIZ1nlRD9eFcFcqG25s3WcBaQ7B3R4H2L5AudwwQJYXQ8SKZ8C0gzqEisdhwGlRkLHQIr5BjeRe9BgzsyPy4BndDYnMz4YCiY7Sr1fGbxnWEZE8Ko92c27HLxsYtJeshdIhK26a_pO2U4SRi6O9BRmuzMe3k1TJNIi1Whlm-bt81kefvVzNdvnU_4reXbrjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoUSfo_yJ1vaONbHQmhw81LHXc8nwtdxZHoNiYl_AqzhP-sMauP1w1eeeKl3MZPzFvNTqLArD_0zkuPi8S5Ng8d5wl4I0d42zYF-QT9b5REhrSGlfIczYwrKbS9poh9ibYYb7EAyf-xyi5Gtc-HQbZL3H4GPqy9KCJoSZ7YC5grzJVmPKmnZhy05GaIKHum3bai9TFfOjCPc5hOGP-p1fa991-B462KRjGdR-bEpP0YW-ky5POfhS0ebebHrkRqU46Rnm73cFt4e1dBqYPVxKDQR-0JhRq4qVLj7h7vK56YfsuzgcdqgntpRIBH7IQzyQIk1NQaICph3rtSmut4n-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9neQ2wDqF1ZqedxmmBS2pAddBhnzaO4ZCZfh7owBsu0MhlsAgGvnafMN5UPF_c9z1ltjxDfag0gEnIpGsWU0R8pVmS5GOtQl7mw0zw3ebgUDNRb_-fuT8QuV6cXUf372Kb-rmx7yJi0gjqYjaU4n8uhu8CxxHP1KzEkzc0GGNSUXB9ZrQonxCpIJTUboGQ-aAyAcz_pg7NNSKm-BjL4QwgPY1fRSHfnlR48qErem_xe4V-eiaPRCI25896aCEpd0H1pRJfjnsg4Zf8Iw70RHcYXPQhQ6ifZr97mRey7eD2TkQUir_xMfyi5qoRNOaH73xqqXUMHFaXCd77X5YNuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbUvLZw37_lQvTvMF0IkJIxcw2VdkIET2piuejik0m1wk6QmrhMNzbflnEmiKg8ranL9r9HLzdUyVjzGKR0hcRz8a_uGJzOWulQa_x6EqM74mJffrhS5n0sx7Co4JnQGDX-xV1YYTLyEV7HeEi-fe2vQtINw2fUpVs5o9w2aT6KMHIS6LA2ExyOTU68Lfe_pWYG0LXCQEvjKdxD2ODkfQivmazFQWdK5CU0HiCE2fr5a9AE6TTnbvTB1VzXBkqrcGyNzpAIL49BbkvJ2hZN_vp2_C97nsK7KGHNE88yQp-54kLKyexeFBuJ-xm4Gf2LsOSOasCnK2PZxsuHK6YGZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u05A1xhA4zWsXDA_dmEGOtfQpnOHmBalzDVNiBpxUong9PhJ7ftUHSYj_C7WhwGUCVlI3jsl0653V7NdYChum6S_PJcebjuPficK9GfJ_I6QIRoLMgrauvDD7WZISzX_WYyjm80Dw7N5tqU0V1n4w5J5CZ6uT7JKvSY0MZlFi6cIsoURNTXtvvAWzNxf_MbVYRlcPFN0779gC9z3qMc7oo-UxwPOw0yb6dCXmY8AVyQAoPLOqliQu5nfygOpkJy5i6TzZOCU4m7NlIZ0PsXffv9cJ-gZOhsDX__dTYcXBc0N-J-ObggjzXjZH8TTQ9RnjYdQMJeTTKrYpc8BCqqIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HncLOpAcdq6mIMKnL3HFz8Cuzu4XubbIFiyDJmga7yKW7nSdKgdaYqQcovw5vo8RxZRclZdDdEYB7DFyRhFcEw2LAxJ7501XS9r1wjEp0AxZMfmrabvydaPuyvZYKAy9lakveBoNkzDOORrQIByn_J6MNtjtA68u5cChzuOtgdi7cZvc-edqfbKwcVnOEGO3BYtIMUTN8W0cd7d1Mx8iV-Txtz9mNrBenCa659vIdATgfeRKCpi4txEahBL3b8YOq0lJp17xNMNBSwIUlqkuwZWLUU-tj_X-FqhV2DBbU7l6PjHkpPZNfC93zk5kRLmXypWunhOcrMkZhxXZ4azKHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هنر بازیافت خلاقانه؛ تبدیل کفش‌های قدیمی به آثار هنری ماندگار
🔹
این خانم با پیشینه فروش کفش از سال ۲۰۱۹ کفش‌های قدیمی را به گل‌های زیبا تبدیل کرده است.
🔹
نکته برجسته این آثار، حفظ جزئیات، لوگو و بافت کفش برای نمایش هویت اولیه آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/674003" target="_blank">📅 10:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673999">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9NZA7GWTTlXIhttnhfXN1gZRp1W_v9qhnXNp4frNBfBERa9X8-iij41Ucu61-obc8NfPN6uRjj8IIZyvdSQijukC3la7pXVmwNN5933dbLeGO1n7wFWDwyZmc4gPIwwS294h33WgUjJwgalBUwCgcd3iylB_uFKTTkvEcvu1fC2je2l8S8cAkhu3gP3aa-omm8vI4LxkktXR0yx9vwWi1U0SW8JT7xS5noiZYPCwwe3dvY5FHhHQLpKglrM-nTYdHYql6QUq_VjOReres0Ez1LWjMcRp7KZZK9TgciV64ls-LwBLkWoPVpkx3jUvgFD2iAnTmw_AN_U4sdB-wXVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فقط تو ده دقیقه و بدون روغن این فیله سوخاری ترد و رژیمی رو‌ درست کن ⁨ مواد لازم:
🔹
نصف‌سینه مرغ
🔹
سیب‌زمینی
🔹
نمک و فلفل
🔹
تخم مرغ ۱عدد
🔹
پودر پانکو  مواد سس:
🔹
جعفری
🔹
پنیر کم‌چرب ۲قاشق غذاخوری
🔹
پرو ماست ۲قاشق غذاخوری
🔹
جعفری
🔹
سس زیرو‌ ۲قاشق غذاخوری #آشپزی
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/673999" target="_blank">📅 10:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673998">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE2j1z4h7s-Lg3jAKNYpfYw3N_w5zZfDTcmFmN4l-oDGNLx_OYad2yMA9OHIR2XdRRNPb7GZS1vl0uIJlJlOBI87uQnwblhwt-yAuPJpmihzx2ou0ykurzQ1QuHFyDVj4ZNQ822mfaDrjfRN4pxhi1xSlfsAgyqMU3IgxYp5iMQLiRc25XIX_c04b_48N6aOOWw2Z0VkGyp1XBm8V7lwH7F5vP5_QiyvYnaWyTQFOL7cx_kB4IL3wx4C2Y2XM4rL8qjVMw4g4dtxpbbyv29d_9YQTmWa3iw0pNABecicXPKWsGgFU__id8uPeG-L1lxCaQZ_VBkXPCRA8wBtQpB0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قابل توجه سهامدارن بورس و صندوق های طلا
🚨
بررسی کامل روند بورس و طلا در کانال زیر
👇
https://t.me/+werraAXV39phMDZk
برای دریافت مشاوره  به ایدی ادمین کانال پیام دهید</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/673998" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673994">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6347d7eaab.mp4?token=cdOSkEDWIHiczLQ7jg_FWmQwvtGTthReGgvVmDQBl1u9DB-aiBPXS_CU8wH4295EfKCFeueFq5H6Zqy_qKhIbKGmiF22H6SNUdllwasM8_VuzBQB_zxKQPUukQJGqMvaWneLCUw7AxdGIQFwU96jrP_TnuD1YbUpI9IwDXJIzTnKbBnmoOa4c1RZePydCo2O2s5mtc0-M9aJF0NzULGVZSJgiG2fCgnGQiiPIZ7PFvF7wlTSVa3L16M-aI-wFg40bLKiHdUZyCkciyiEBOVmgFj0G28YKRtdsaQQBC-2qs8QMnJklHF1Ad7hFiYBPm9LpmCIwh-OSmrOLrQrXgI8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6347d7eaab.mp4?token=cdOSkEDWIHiczLQ7jg_FWmQwvtGTthReGgvVmDQBl1u9DB-aiBPXS_CU8wH4295EfKCFeueFq5H6Zqy_qKhIbKGmiF22H6SNUdllwasM8_VuzBQB_zxKQPUukQJGqMvaWneLCUw7AxdGIQFwU96jrP_TnuD1YbUpI9IwDXJIzTnKbBnmoOa4c1RZePydCo2O2s5mtc0-M9aJF0NzULGVZSJgiG2fCgnGQiiPIZ7PFvF7wlTSVa3L16M-aI-wFg40bLKiHdUZyCkciyiEBOVmgFj0G28YKRtdsaQQBC-2qs8QMnJklHF1Ad7hFiYBPm9LpmCIwh-OSmrOLrQrXgI8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله ارتش رژیم تروریستی آمریکا به چند قایق ماهیگیری به نام قایق‌های تندروی سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/673994" target="_blank">📅 09:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673989">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0127444c42.mp4?token=nnQxDZhGnuo7x6xp4yF29QeZGBtthw7Cap2GoE0AMOlA0kggF11s25zavhrFq7ijikDHFRMo4HPh5jC0iIJZlEViGLzkEuonyReYMZ_r30iHLxkucNEu066cFTazs70MsKLOyccZzkmATVb_e4P7aQmgT8EPnGNXyrWW8UE5n23kVn2uuLvdV_cKp2tt_NBfnjnYOlktSw_UlLNEHYjXuMcExiBEZRhQsnxmyVO8ZMVrjuWJ5x7J4lGt3mzm9Nd0YlPGdpekdWBL9ifl5bAoDZ6c2MADFXkzxCv-OQxBEN1TkBQvQhFodj8uWY4GSdbdkYIhL5d29CWJh84qn-olhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0127444c42.mp4?token=nnQxDZhGnuo7x6xp4yF29QeZGBtthw7Cap2GoE0AMOlA0kggF11s25zavhrFq7ijikDHFRMo4HPh5jC0iIJZlEViGLzkEuonyReYMZ_r30iHLxkucNEu066cFTazs70MsKLOyccZzkmATVb_e4P7aQmgT8EPnGNXyrWW8UE5n23kVn2uuLvdV_cKp2tt_NBfnjnYOlktSw_UlLNEHYjXuMcExiBEZRhQsnxmyVO8ZMVrjuWJ5x7J4lGt3mzm9Nd0YlPGdpekdWBL9ifl5bAoDZ6c2MADFXkzxCv-OQxBEN1TkBQvQhFodj8uWY4GSdbdkYIhL5d29CWJh84qn-olhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر هوایی از تشییع پیکرهای فرشتگان میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/673989" target="_blank">📅 09:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bESu0incjMWeJEbrQX7l4RS9e1omAp6WWFe0p_RHv9x14ryRPdwsulg_b27vpugZjmcCKK69Zztx1ACYd1u7FIed-rLlwnm3_RKsoIPn_uAdvMOmLGElKYzDBtjaGEYeFURJvlsBF3YdhRJ1CrbgvCiJOk8nQ_43Nfg_DAigK4zH-gEYXvvHCgAk3Er0qvorykq_-ug1-o00f0KoKnREuZhkme4-YQkAlgSeap8g2OxIg0xyQa_LX6k7-DoPhhP8iFYF2RuP4JMALGeo5e6COJf-cfwPPlTbViYgH9pdh9LnIuReqPPNIStLLB5YLkoYvXeNTHQyMeRdpepqDhyfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه دردهای بدن؛ هر نقطه درد بدن، نشانه چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/673987" target="_blank">📅 09:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e92d6bf4.mp4?token=QxxSUlgHQ9xqDWXL21sugK7CKfkahVme3M_9Hhxv7K5YYAGNhaAGgbc4yU8JpSnl3PkC1yFi9DHIfSDfLfDqWMe55B2cS9jLeREwgJhIBLSVb756bQhgGc5N3It0NihmOLIU_MNsNCF9WH5RbWiZHUzLi0UnTOf-yQ096CRm5GvLxCPqXEybNMXUf6EtHFJMqb1pX_m4jHzBIn5ueMgs0C0Pjtb9UU6MrR_wcGnp_6ExrETVz0m4KjsgXKTcbE_6-rtexgBWnEmpmod4u5yQSy-Dj3QEB54A6vSZJf0FtcQY4cm1ikbzlH-ipBxbM2dQhRNfGTIEcXQuHRjFcNaQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e92d6bf4.mp4?token=QxxSUlgHQ9xqDWXL21sugK7CKfkahVme3M_9Hhxv7K5YYAGNhaAGgbc4yU8JpSnl3PkC1yFi9DHIfSDfLfDqWMe55B2cS9jLeREwgJhIBLSVb756bQhgGc5N3It0NihmOLIU_MNsNCF9WH5RbWiZHUzLi0UnTOf-yQ096CRm5GvLxCPqXEybNMXUf6EtHFJMqb1pX_m4jHzBIn5ueMgs0C0Pjtb9UU6MrR_wcGnp_6ExrETVz0m4KjsgXKTcbE_6-rtexgBWnEmpmod4u5yQSy-Dj3QEB54A6vSZJf0FtcQY4cm1ikbzlH-ipBxbM2dQhRNfGTIEcXQuHRjFcNaQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
فرزند شما فقط برای امتحان آماده می‌شود یا برای آینده؟
🌟
دبیرستان دخترانه هوشمند مدبّران (بارسا)
🏫
✨
در مدبّران، دانش‌آموزان علاوه بر موفقیت تحصیلی، مهارت‌های زندگی، اعتمادبه‌نفس ، تفکر خلاق و آمادگی برای دنیای آینده را نیز می‌آموزند.
🚨
ثبت‌نام آزمون ورودی آغاز شد
🚀
📩
برای دریافت اطلاعات و ثبت‌نام:
🆔
@modaberanschools_bot
📩
یا عدد
4
را به سامانه پیامکی
3000909030
ارسال کنید.
📲
❗️
آشنایی با روش‌های نوین آموزش و موفقیت تحصیلی
👇
🆔
@barsaschools
📍
تهران</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/673986" target="_blank">📅 09:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df897bf3a.mp4?token=k-SMSPTaRtHnI1GO9LsyewaBKyD44coZCf5bGGlmaTCVIUwL2npPX0ctg2Y-h__SFVnR5I8Xm9-GyUi6elz6eu1tUYDPrUmVDR-ZrgKyK10ngQXV4zrhEC7AOEMW65k5usgVfhgY9i-cnbuB-n0WW06GWxtstv-zfEFqTF8RiekFjVTooUPgZbM4R4JBF0KgY_IkpaMpgDb3T0_JN1SU6ZYAKAXmPdZNXGOiCDvEQcLVOS7zCYY8AvMldRVm2eUP9cQHcHYt7lSee4Ul441TJ01kl9_WNYIdFTHhM-bMCEn7Tz8kdOvHmHlu7b_nLbJMLiX8a-0b5DuCQbQdzl0WsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df897bf3a.mp4?token=k-SMSPTaRtHnI1GO9LsyewaBKyD44coZCf5bGGlmaTCVIUwL2npPX0ctg2Y-h__SFVnR5I8Xm9-GyUi6elz6eu1tUYDPrUmVDR-ZrgKyK10ngQXV4zrhEC7AOEMW65k5usgVfhgY9i-cnbuB-n0WW06GWxtstv-zfEFqTF8RiekFjVTooUPgZbM4R4JBF0KgY_IkpaMpgDb3T0_JN1SU6ZYAKAXmPdZNXGOiCDvEQcLVOS7zCYY8AvMldRVm2eUP9cQHcHYt7lSee4Ul441TJ01kl9_WNYIdFTHhM-bMCEn7Tz8kdOvHmHlu7b_nLbJMLiX8a-0b5DuCQbQdzl0WsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع شهدای تازه شناسایی شده مدرسه شجره طیبه میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/673983" target="_blank">📅 08:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673980">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b36f8da2bd.mp4?token=LzYW0N9xDMLoq8gp_rYnj6XYEFzTQ8Kw8NWD5u4f-wYNkKowZC8BQdL5dMmeoV-KN1tVUKG32w7Gv9zp5wT3AasDMwOvtgmCk0LlBahp7YeM_0mmXFsgQ2WUifupo3DdGAB1jaHht9DRBLpMjf6EugDuhOWxDKHl-RKiaplianIYfoqcnXlPUQdQRjb-e0J_SZC04Xbdz-hOusY1JC58MX22pzMphf0Hs-ZhOdxGnFSdgPHf2fU29h0aslFqz448VRVasCO0_9wVbDsYO_75GZr23ZqJn1uzpmQTy0afkdEsmPzbjjYOuZSh_DaoOH-P9roWzdkykSrqZyxbIkViiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b36f8da2bd.mp4?token=LzYW0N9xDMLoq8gp_rYnj6XYEFzTQ8Kw8NWD5u4f-wYNkKowZC8BQdL5dMmeoV-KN1tVUKG32w7Gv9zp5wT3AasDMwOvtgmCk0LlBahp7YeM_0mmXFsgQ2WUifupo3DdGAB1jaHht9DRBLpMjf6EugDuhOWxDKHl-RKiaplianIYfoqcnXlPUQdQRjb-e0J_SZC04Xbdz-hOusY1JC58MX22pzMphf0Hs-ZhOdxGnFSdgPHf2fU29h0aslFqz448VRVasCO0_9wVbDsYO_75GZr23ZqJn1uzpmQTy0afkdEsmPzbjjYOuZSh_DaoOH-P9roWzdkykSrqZyxbIkViiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من ایران را دوست دارم چون شعر دارد هنر دارد تاریخ دارد وسوسه ماندن دارد وطن در دل آدمی باید باشد
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/673980" target="_blank">📅 08:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673979">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d68b609dc.mp4?token=GVL2QDZ5gNT7A-Y1-13EZYLLqXVrfE8o4jjLPC1mMde4Tgv1cYVv3qpVYW-CtbApcRhLyc1BzFQa2hKSad222k3SIHz7awqlQmapeyP_vOnIPGlGA7_GKGpY3XiG8LJO1csKCL_9skVLIKOwVoW6QlM78bPOt9UqpDTcAizvNzXRs1YxV0CMqrfvssWGi3gHOLgZbJxApinNpeCKGsuy2s_qIUKWiwsA7B5oE_bgNixgLvRqf0CiDccC3Ip627v6WZfZFHezRaNr7Yt8w-4qJn6n1GAnU8IPOkFWbNSm9QrT3t4b7erPzmreSmAhOZL5dbFuciUm0DIeKDlsAsogUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d68b609dc.mp4?token=GVL2QDZ5gNT7A-Y1-13EZYLLqXVrfE8o4jjLPC1mMde4Tgv1cYVv3qpVYW-CtbApcRhLyc1BzFQa2hKSad222k3SIHz7awqlQmapeyP_vOnIPGlGA7_GKGpY3XiG8LJO1csKCL_9skVLIKOwVoW6QlM78bPOt9UqpDTcAizvNzXRs1YxV0CMqrfvssWGi3gHOLgZbJxApinNpeCKGsuy2s_qIUKWiwsA7B5oE_bgNixgLvRqf0CiDccC3Ip627v6WZfZFHezRaNr7Yt8w-4qJn6n1GAnU8IPOkFWbNSm9QrT3t4b7erPzmreSmAhOZL5dbFuciUm0DIeKDlsAsogUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب جان ایران
❤️</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/673979" target="_blank">📅 08:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673978">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/388a278e8e.mp4?token=lgm4CmqUXe1Y-pxPEnGiJ6wvpqoTKjMvriLr0WykHJrLjyzPS3ohDTvhlXjn0g8ZrpBVWQ3plYPAjn45rC_XcJfFW-F8Dxa34Y2N77az5xUUlAGIAtJmy2qVs3-zR9O8ftKBne3vBPVJpSOH7ppzpfqAMvJsBMbpgThwx32JI-DDZTv2PaKGHN8N-0q_2pdM6MuWghtXqVv_UKqn3r-g0Ge-N6lG8WTlq1kgD1v80-kfQfEkIE-MiJlIAEXFQqHhlRpEHDjO1_o0S21QGJVCdxEe53RO0_6ePvlHhnzlJEXaecwf8lqDQHiPSOM5GHOlRPNYZzXvo6ZaHgTVtl5WPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/388a278e8e.mp4?token=lgm4CmqUXe1Y-pxPEnGiJ6wvpqoTKjMvriLr0WykHJrLjyzPS3ohDTvhlXjn0g8ZrpBVWQ3plYPAjn45rC_XcJfFW-F8Dxa34Y2N77az5xUUlAGIAtJmy2qVs3-zR9O8ftKBne3vBPVJpSOH7ppzpfqAMvJsBMbpgThwx32JI-DDZTv2PaKGHN8N-0q_2pdM6MuWghtXqVv_UKqn3r-g0Ge-N6lG8WTlq1kgD1v80-kfQfEkIE-MiJlIAEXFQqHhlRpEHDjO1_o0S21QGJVCdxEe53RO0_6ePvlHhnzlJEXaecwf8lqDQHiPSOM5GHOlRPNYZzXvo6ZaHgTVtl5WPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ حرکت مؤثر برای کاهش درد و خشکی مچ پا #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/673978" target="_blank">📅 08:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673975">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721598e238.mp4?token=hT3iu1DF8u05OCyxljo44CGIHETFtEW1t6kmEkJJ5UDuY7PFHQ0CJeSxoBFGnLiDK_wF-vx7x71nYK9fA0kE2M1RVpKNJJLFCzvBm7eTccPHnz2Vt4LY43JM3wyERIG2HKuOAsD7jPS1taulVlDNJO0yGjnxuQ-RYtsI14KwC3eBWDpxp5zbYGmM2PXS32gIfXSoQJ8irKQKnFHFKUAiyvQckEUnlpct7aVSJLYVXQ__Jl70Ce3qf1jjfAhO8aHEcKwgxPs9tKUj1482OjYc50dP77N77tVVEEQJdzkhVYppZKeo6thAU-_v0pE65zk5iRWZmeY4ZWZcvfKev470yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721598e238.mp4?token=hT3iu1DF8u05OCyxljo44CGIHETFtEW1t6kmEkJJ5UDuY7PFHQ0CJeSxoBFGnLiDK_wF-vx7x71nYK9fA0kE2M1RVpKNJJLFCzvBm7eTccPHnz2Vt4LY43JM3wyERIG2HKuOAsD7jPS1taulVlDNJO0yGjnxuQ-RYtsI14KwC3eBWDpxp5zbYGmM2PXS32gIfXSoQJ8irKQKnFHFKUAiyvQckEUnlpct7aVSJLYVXQ__Jl70Ce3qf1jjfAhO8aHEcKwgxPs9tKUj1482OjYc50dP77N77tVVEEQJdzkhVYppZKeo6thAU-_v0pE65zk5iRWZmeY4ZWZcvfKev470yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی پیکرهای تازه تفحص‌ شدۀ شهدای مدرسۀ میناب برای تشییع
🔹
مراسم تشییع و تدفین اعضای پیکر مطهر این شهدا، ساعت ۷:۳۰ امروز در میناب شروع می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/673975" target="_blank">📅 07:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673974">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اطلاعیه شماره ۳۹/ زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین با چند فروند موشک کروز مورد هجوم قرار گرفت   روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت قهرمان و شجاع ایران اسلامی؛  با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/673974" target="_blank">📅 07:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673973">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kExtpLglSV1zNJGMOJVxe5v44JNKfgIqYzw2LbOhnphZovd-tiIY-U0n61mcCNnrChZxRCj01D4kK9indi04P1XxyB22mz3Ux8aG3BbhwQomomyoh4ktexMWEcOqFkNUuOIbb1FmdKeFeKozLNAa8qCNar27UsCb-9Gn39YTHnVH9wYlyeBuLXhBOvbD2syNysZaUKy4OWlQsqmYzi_R6LMR4HE_F0_3hP1e9QG_zltGqpmrq2lrKZr6pEhunltPp0RKD5Q5esDjJP37Ek7lJrjRvYoTzxAFHZF8cvyG4Bi_lhuQRaQ9BuSm-CL52pRO6f2aKqHT32eyYbOpw_NFSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۳۱ تیر ماه
۷ صفر ۱۴۴۸
۲۲ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/673973" target="_blank">📅 07:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673972">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
هواشناسی برای برخی مناطق هشدار سطح نارنجی صادر کرد
سازمان هواشناسی:
🔹
به علت تشدید فعالیت سامانه بارشی هشدار سطح نارنجی در ارتفاعاتِ استانهای زنجان، قزوین، البرز، تهران، سمنان، مازندران، شرق گیلان و غرب گلستان صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/673972" target="_blank">📅 07:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673968">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
تایید حمله هوایی ساعتی قبل به نقاطی از استان ایلام
فرماندار آبدانان:
🔹
ساعتی پیش منطقه چوار و آبدانان در استان ایلام مورد تهاجم قرار گرفت، این حمله هیچ تلفات جانی نداشته است.
🔹
همچنین حمله هوایی به منطقه انارک در چوار منجر به آتش سوزی در اراضی منابع طبیعی شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/673968" target="_blank">📅 04:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673967">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به بانه در استان کردستان
🔹
بامداد چهارشنبه ۳۱ تیرماه یک نقطه در خارج از محدوده شهری بانه هدف حمله دشمن قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/akhbarefori/673967" target="_blank">📅 04:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673966">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ترامپ با توافق هسته‌ای ۳۰‌ساله با عربستان موافقت کرده است
🔹
این توافق دسترسی ریاض به برنامه تاسیسات هسته‌ای غیر نظامی و احتمال ساخت تاسیسات غنی‌سازی با مشارکت شرکت های آمریکایی را فراهم می‌کند و همزمان نظارت واشنگتن بر این برنامه را افزایش می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/673966" target="_blank">📅 04:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای سنتکام
:
ما یازدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/akhbarefori/673963" target="_blank">📅 04:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673960">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcrY8LbQrulbdiKPOP4hMQNWqFl8bx-3_BisSWr8FkuM6E1b4RUgKrOXGannc5J_1BYHKteYhG5-jAfrDmJIal99EIvG4UnEaGPgXdWG1Zw57GW9Jdlso4bax2Ru6FRmGWHQRGLHq6F327ZfuEwcDdwQ6Y1z7-0dJbvianPG1O407yhf41FJbp3izJXFtWOEUVT6TShkCOO73b9ilT_ODHpmjP3Qa1MN9Y6mkUZE7H_491tWI8Q08n8fJC0twkuNS5Tzu-98yYS1pFejOyIdufNm4NrBPZCsgc6kqmlRYxCv5QO5dSsGe9E3yAjiFOdKLU9-3hoUwMQ4j--n3GKmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از پلاکاردهای معترضان ضد جنگ علیه ایران در جلسه استماع سنا همزمان با سخنرانی وزیر جنگ آمریکا
🔹
نه به جنگ علیه ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/akhbarefori/673960" target="_blank">📅 04:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673958">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
پدافند تهران دقایقی قبل بار دیگر در شرق و غرب تهران بزرگ فعال شده است و به نظر می‌رسد که پدافند مشغول مقابله با ریزپرنده‌های احتمالی است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/akhbarefori/673958" target="_blank">📅 03:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673957">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
منابع خبری دقایقی قبل، از شنیده‌شدن فعالیت پدافند هوایی در غرب، شرق و شمال شرق تهران خبر دادند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/akhbarefori/673957" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673952">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
دقایقی قبل دشمن آمریکایی نقطه‌ای در شهرستان کنگاور استان کرمانشاه را مورد حمله موشکی خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/akhbarefori/673952" target="_blank">📅 03:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673951">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd130fc44.mp4?token=UodKWJ1--qy-1yEnArXa--7TqIbmP2PbWn77AYgLBHn_DxROMfaoIDoU8fcOTY4tlT0XXRH0ZNFN_gy7u6H0hLO_c44suhLvmdekQHhIapc3DusUlFY0ezbOgGwvJG3eRKVONhYwgfHDsYu5zQvCHeOShF4OTsPtIsrJgcNTXGfZtqv2WtAK9rBvPjcA6DiIfkeVTygW9zdKXM5othBNvJRM7JhS_TKQCaYk0KIPxeOnP7ioxP30-tHq5lsafJHewUMAL813ZMH272-ZvDLPH13shwkuKesMXcxyOGTkB2wGIcqb-LR_-yWOhULjpZ_lmal5hJ8dL8pyIagED-qCWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd130fc44.mp4?token=UodKWJ1--qy-1yEnArXa--7TqIbmP2PbWn77AYgLBHn_DxROMfaoIDoU8fcOTY4tlT0XXRH0ZNFN_gy7u6H0hLO_c44suhLvmdekQHhIapc3DusUlFY0ezbOgGwvJG3eRKVONhYwgfHDsYu5zQvCHeOShF4OTsPtIsrJgcNTXGfZtqv2WtAK9rBvPjcA6DiIfkeVTygW9zdKXM5othBNvJRM7JhS_TKQCaYk0KIPxeOnP7ioxP30-tHq5lsafJHewUMAL813ZMH272-ZvDLPH13shwkuKesMXcxyOGTkB2wGIcqb-LR_-yWOhULjpZ_lmal5hJ8dL8pyIagED-qCWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شمال شرق تهران
🔹
دقایقی پیش مردم تهران از شنیده‌شدن فعالیت پدافند هوایی در شرق تهران خبر دادند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/akhbarefori/673951" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673946">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در تبریز
🔹
دقایقی پیش صدای چند انفجار از حوالی تبریز و از سمت جنوب شهر شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/akhbarefori/673946" target="_blank">📅 02:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673943">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
هشدار مقام ایرانی درباره هدف گرفتن منافع انگلیس در غرب آسیا
خبرگزاری تاس:
🔹
اگر لندن به واشنگتن در جنگ تحمیلی علیه ایران کمک کند، منافع آن در منطقه هدف مشروع خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/akhbarefori/673943" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673942">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ترامپ به دنبال دبیرکلی اینفانتینو بر سازمان ملل
نیویورک پست:
🔹
دونالد ترامپ خواهان انتخاب جانی اینفانتینو، رئیس فیفا، به‌عنوان دبیرکل بعدی سازمان ملل است؛ پیشنهادی که برای تحقق آن به حمایت شورای امنیت و تأیید مجمع عمومی نیاز دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/akhbarefori/673942" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673941">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHBH2jOAgBaulvD3aQQTGoXh2yDXlLg7GEqaF3wj5-s_MTxJ5a3-Q9BooilB7ZXhYS4M_LF27d6hn2yuhyw1D9oWVA8gjlG6lbKAaysrQjz30FW2T6X7KTEyLzH-oxBH1kCpnFAqQyyyxmKXbRvGt0oJidD4qdoiBTKm6aTY-QHTqkNGaIvabur-HFYUI9yiNTu8aFlXQmrsVmEkhY1ih0PyFC1zEZqhGDLtYPT3msLgJZ9hF8hoCqzTTCWnuT64D5Y2YqI2SSNiewDkNeFBhoglH-JUSZOiKlj_Hkc4szyUEpPHDGMkrL624a4AcA6H_hNMmeeBy2f8L7zPw7G_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر خارجه چین به ترامپ درباره تنگه هرمز
🔹
خوک نجس: برای بازگشایی تنگه هرمز روزانه به دو میلیارد دلار نیاز داریم.
🔹
وزیر امور خارجه چین: تنگه هرمز قبل از جنگ باز بود. ریشه مشکل در اقدامات غیرقانونی شما علیه ایران نهفته است؛ شما از هیچ، یک بحران جهانی ایجاد کرده‌اید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/akhbarefori/673941" target="_blank">📅 02:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673938">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f18f4b5b.mp4?token=PAFYvJKneqLKiWzg5BnKUFTrlprEIgEnaC7pUp0p1KIH68-AxxOyBntv8QnTMafIZns5RvbAo6b67lWmwORdUoO71lZ_X98j2QroKuEJSBVBilu9OzLJsFD4I-Nd8hR6FKhH36srqG-oHv715Ge_rnFj_jU6GbpGdrnUgVtY5Q4DEj5vFuAqjk_b5iQAdZYiD0XJ9nZbWhv7YqFFKGIRcqRt_Q7Pzii6YRu4uOcLDOcqqP00E3f9HdH5hKjqOUooYmvhNIRFyNbKnfrfXRzIGLl3K6lXy8usA3B6VDgkSO5Mplw1g97zLlT_FaxuAIEaNOBAAOGvHkO8TQ1kRqVg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f18f4b5b.mp4?token=PAFYvJKneqLKiWzg5BnKUFTrlprEIgEnaC7pUp0p1KIH68-AxxOyBntv8QnTMafIZns5RvbAo6b67lWmwORdUoO71lZ_X98j2QroKuEJSBVBilu9OzLJsFD4I-Nd8hR6FKhH36srqG-oHv715Ge_rnFj_jU6GbpGdrnUgVtY5Q4DEj5vFuAqjk_b5iQAdZYiD0XJ9nZbWhv7YqFFKGIRcqRt_Q7Pzii6YRu4uOcLDOcqqP00E3f9HdH5hKjqOUooYmvhNIRFyNbKnfrfXRzIGLl3K6lXy8usA3B6VDgkSO5Mplw1g97zLlT_FaxuAIEaNOBAAOGvHkO8TQ1kRqVg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تناقض در ادعای نابودی موشک‌های ایران؛ چرا موشک‌ها همچنان به اردن می‌رسند؟
🔹
گیلیبرند، سناتور: شما همچنین گفتید که برنامه موشکی را «نابود و از نظر رزمی غیرفعال کرده‌اید.» پس چرا موشک‌هایی باقی مانده‌اند که به اردن اصابت کنند و منجر به کشته شدن مردان و زنان شجاع ما شوند؟
🔹
هگزث، وزیر جنگ آمریکا: آنها ۴۷ سال است که تلاش می‌کنند موشک‌هایشان را در زیر کوه‌ها پنهان کنند، دقیقاً مانند توانمندی‌های هسته‌ای‌شان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/akhbarefori/673938" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673935">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
معترضان ضد جنگ علیه ایران در جریان  جلسه استماع سنا سخنان پیت هگست، وزیر جنگ آمریکا را قطع کردند
🔹
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
🔹
پلیس کنگره هر چهار معترض را از جلسه بیرون برد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/673935" target="_blank">📅 01:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673933">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2256ba648c.mp4?token=CtSD2axueUwf8c4poO3XSk8fSzvu-7G7M7ir-CNkS8514VCLZiPRuwOemRLtfV-V0H1HTc1SRY90WJ6BHs6JZpDvq5dNn0_qujhZ-v34olMKQIEgGHG6yu5C0GyY_1rH8HjuulnWY8vCskk2G-gQ-noHWChd3h5899G_tZy-g7u-XiVokYZ1uEsK5qksB4SVw6ZGSauSHKQT5eR2J7WEvm14Obgim3GdDkRDupka_A1FYvZ0lWVF2AyRizKM8dlmgesw5f8tbiDB1wPYqUpGg7eQhcgviGNKyIAzAX7LxXr96tycyKrUXh8h7hBFR_dK82-QeNBGUaZyb482BTvWSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2256ba648c.mp4?token=CtSD2axueUwf8c4poO3XSk8fSzvu-7G7M7ir-CNkS8514VCLZiPRuwOemRLtfV-V0H1HTc1SRY90WJ6BHs6JZpDvq5dNn0_qujhZ-v34olMKQIEgGHG6yu5C0GyY_1rH8HjuulnWY8vCskk2G-gQ-noHWChd3h5899G_tZy-g7u-XiVokYZ1uEsK5qksB4SVw6ZGSauSHKQT5eR2J7WEvm14Obgim3GdDkRDupka_A1FYvZ0lWVF2AyRizKM8dlmgesw5f8tbiDB1wPYqUpGg7eQhcgviGNKyIAzAX7LxXr96tycyKrUXh8h7hBFR_dK82-QeNBGUaZyb482BTvWSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان ضد جنگ علیه ایران در جریان  جلسه استماع سنا سخنان پیت هگست، وزیر جنگ آمریکا را قطع کردند
🔹
صدای یکی از معترضان شنیده شد که فریاد می‌زد: «دست‌هایت به خون آلوده است.»
🔹
پلیس کنگره
هر چهار معترض
را از جلسه بیرون برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/akhbarefori/673933" target="_blank">📅 00:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673932">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e3a9751d.mp4?token=RbfUhtthpqxtJv5RcCei9cdUChY-w3Nw-BP_aRtiajjHBTSQC3XicG0b9LFi8yx_gXdtgjzl0ylQt9wzoMzZ4Sh3HLaXcM4c8Ss1qO-TTTdL8KW8jclC9-1rwcoN8rSiXOhO_rz31pnnLvuyfte6jB0ZaRBQGY0kM5lPUq58FfpgeBTuaR3XuJuAKL4kyuZd3uT9Punl5-r5tEMi4-4kOva1LJlCrS4uww4WCoTHTGKOiCm1TJqBik_KyW0vcoINjK9ujfsvHq4dQFJyNIywSMvGiJtePIDLbXvCS0mwRfb88mrfO4PA1p_qjI34qmlYvgELfzk_8CiwQl3kAPXkMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e3a9751d.mp4?token=RbfUhtthpqxtJv5RcCei9cdUChY-w3Nw-BP_aRtiajjHBTSQC3XicG0b9LFi8yx_gXdtgjzl0ylQt9wzoMzZ4Sh3HLaXcM4c8Ss1qO-TTTdL8KW8jclC9-1rwcoN8rSiXOhO_rz31pnnLvuyfte6jB0ZaRBQGY0kM5lPUq58FfpgeBTuaR3XuJuAKL4kyuZd3uT9Punl5-r5tEMi4-4kOva1LJlCrS4uww4WCoTHTGKOiCm1TJqBik_KyW0vcoINjK9ujfsvHq4dQFJyNIywSMvGiJtePIDLbXvCS0mwRfb88mrfO4PA1p_qjI34qmlYvgELfzk_8CiwQl3kAPXkMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر نزدیک از مکانی که در کوه ازمر، در استان سلیمانیه در شمال عراق، مورد هدف یک پهپاد قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/673932" target="_blank">📅 00:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673931">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: من اذعان می‌کنم که ایران هنوز هم بدون شک توانایی‌هایی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/akhbarefori/673931" target="_blank">📅 00:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673929">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GybwSWiyRBfl3Ns7iNItnP6IAzZKkaTqkTzIyEidQyib28P_yhnfmZ5Mj6jbsL4waD4GhR5LMWNAwy3NleKddYN4WlizCKN__qFOuitTvZh3sbO5nTksogpWkdmR0D2zX_VXdUFFFKJf6x2snFzR1zEnzeSEJR_Bnh1Bt9A29kITFhf1e3nzVgRVBW4gFDVduvgjs7ktN4-EC_SIngM0LyyqHUAB47UYoNYZz01BgBx7N8Z4VkCFV8wl5SAAFgFaGoQof84zT4LIl6f62oTRx3ZW0zZ6X_PGeBpP1IqFgyqsh8B_eJGIxBoUzPGp0Qa1NWGCQVhHISvcqqZbEQYMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/akhbarefori/673929" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673928">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3eFET-B9x3b5yaIpm3h2QcmnptDVYB2VrZs_8XmtVqk_OftFuQhdKe5OniluDEgNEMIguF7kaBcCQ-4DuQF6DkQ3FN9NHI7Ax6H_nsKlnp53PYeXPBybYeESWKVW8ksHzRpTUG-y8rx-dzF4uihyM36ObMJav_Ad53s1exMbRyYDUfPBEvJ5CTgRj3d_9wFvz-0ooX4r_bg65fXjgZXsOav4zI8Iqe525Gf8d2p06Hwcf3PlNzt9U_Uni4ZY7qG46uKuxVUCj_5qqOGA5SYeZqJItNZF7Kaf3us7jTkt1kPhB3IC0aj3KPWF9GO7wmiwAC5Xlz4gi7P1VKEk22fQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاتر تحصیلی شفق تولید انواع دفاتر مشق طلقی فانتزی وکلاسیک ،رحلی،و....
تماس
☎️
09129318455
دریافت لیست قیمت
@Ghamilou73</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/akhbarefori/673928" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673926">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): آمریکای جنایتکار مراکز هسته‌ای و حساس ایران اسلامی را تهدید به حمله نموده است
🔹
اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله‌ای بشود، آن را به عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم‌پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/673926" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
واکنش وزیر نیرو به خاموشی‌ها: در حال حاضر برخی کشورهای همسایه در شرق کشور با قطعی برق ۱۲ ساعته مواجه‌اند و در برخی مناطق دیگر تنها ۲ تا ۳ ساعت برق متفرقه برای تامین نیازهای ضروری وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/akhbarefori/673925" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673923">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=jBGQKRoJoG_6qin37v2642rDK25Z8zmM_fu_j_GTc8JjgE3F3gBikOOiCy7vcVsbYeS5YeKnErXo7ARr2K-v0Wi1gDs8A0mSDw7yVUwdPUKzSV5E3ainyhhyyZncxjGCBxrPw3RuzEIqY_vIaUlwTrYpF5tcSYLHkE5eTu5T1KdIWb3rbFENqKKIQWGW4L-tH9hpP9TAtOsUwUFY2VyoyRg04H4BUUI28LVaGw8ovFqazFXQ5ZhlPdzFL_ZvtkkAx5EOYWIQD80jSCa021bT1A77REbOrk0s1JzFGwws6ONAoUKJCkVpu2Xz8xKMSjPn_2LGC5equ1I3SqoRlwHqkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4272552a.mp4?token=jBGQKRoJoG_6qin37v2642rDK25Z8zmM_fu_j_GTc8JjgE3F3gBikOOiCy7vcVsbYeS5YeKnErXo7ARr2K-v0Wi1gDs8A0mSDw7yVUwdPUKzSV5E3ainyhhyyZncxjGCBxrPw3RuzEIqY_vIaUlwTrYpF5tcSYLHkE5eTu5T1KdIWb3rbFENqKKIQWGW4L-tH9hpP9TAtOsUwUFY2VyoyRg04H4BUUI28LVaGw8ovFqazFXQ5ZhlPdzFL_ZvtkkAx5EOYWIQD80jSCa021bT1A77REbOrk0s1JzFGwws6ONAoUKJCkVpu2Xz8xKMSjPn_2LGC5equ1I3SqoRlwHqkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی خطاب به وزیر جنگ ترامپ: شما چندی پیش ادعا کردید که ایران کنترلی بر تنگهٔ هرمز ندارد. اگر این حرف درست بود، ایران چطور توانست هفتهٔ گذشته دوباره رفت‌وآمد کشتیرانی در تنگه را به حداقل ممکن برساند؟
🔹
ادعای مضحک وزیر جنگ ترامپ: ما مدت‌هاست که کنترل عبور و مرور از تنگه را در دست داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/akhbarefori/673923" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673921">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=TPJrUgv8e6MNQgnUsZQW6gN_MRQp0vcF7WIkWRtEn_9Fn1Pesq7vphXpDz8UUkaddadzkHLVhL7ake4kTOFIv5lPuIcXc69FyX_z-2fNTxyhsjU5_pdVNLfRpDgDQpsv6HdIs7WqweVoHG0NUmzxdfi07lTNHOkSeragSQTNiwBiJ5n7ibQEE736wqk_xeYxlXK6kUecwUjbUFb9LNJKYuT7VbcbeVs3_xE4am7gSyI4I_IHIbCGbYeaklrXf08osrbyUa76eDnYBbnvGFdiJfx69S-XoikjDdxldJ0SbopCJozQhh5oeIhambv2ZVZDHWGdOVrZRRZoj6Kx3wHJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde16fff97.mp4?token=TPJrUgv8e6MNQgnUsZQW6gN_MRQp0vcF7WIkWRtEn_9Fn1Pesq7vphXpDz8UUkaddadzkHLVhL7ake4kTOFIv5lPuIcXc69FyX_z-2fNTxyhsjU5_pdVNLfRpDgDQpsv6HdIs7WqweVoHG0NUmzxdfi07lTNHOkSeragSQTNiwBiJ5n7ibQEE736wqk_xeYxlXK6kUecwUjbUFb9LNJKYuT7VbcbeVs3_xE4am7gSyI4I_IHIbCGbYeaklrXf08osrbyUa76eDnYBbnvGFdiJfx69S-XoikjDdxldJ0SbopCJozQhh5oeIhambv2ZVZDHWGdOVrZRRZoj6Kx3wHJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: آیا توانایی نابود کردن آنچه را که زیر «کوه کلنگ» ایران قرار دارد داریم؟
🔹
وزیر جنگ ترامپ: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/akhbarefori/673921" target="_blank">📅 00:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673920">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyzemymJEu5J9j1g_fq3obVsQKiOQdd48wk_R5b3mxFoq5qF8u6bfFDnd-OcY7UDWonnFMVbkT3gtRXqAzuixuohvxs5Y3vkQ9pGbcYzwDWCALo6brC-LKgiJ6aOWqWQ9jS_z8NDHw7as2U8bIlvff1xMDCVjnCqj65FXVJMqXDypL7m47bNJa7Ijt8cnom00b1A25R2EO-cte7BB1Dmoxh45NiHwDuRijYiK5SJ0KBmhqjH7UE5jNqxK-EukWhWEz22rODVHtvGZ9L81OmFJV4LAcL9NHKj9VC_dKlAMIPpSG7nTg8Nb3fAtgwYtdByCR6z6tqfXZe3AVzJG85ldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/673920" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673919">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJr10TIUEogfrtitFSxUJfrUEazEIGe8GNAotXmBfkvJEQByN8f5-0SK08sMWdt8Rg3mBLu4buwdPkaaDigj4RrDUUBKJR-eW7mtO2zNoU35wLnxUZ-LvptwZmQCVCW8FDKKnyCNUQ_FbpOi01KIbcnHZJ0eniTNSVcAEPwf_HQdDDvjhhsV5EVV7qn7YbjLGQIJjx_jAPzh0LC0KbVLiJCv8ikXQnBxny1caz4GyLGDVs1sEhs4iwdPg-zittu3X9kwxsp2ZN3gJplVdtT5IDcawExBZ9-Q-RNrIjBsIMPgW8mcdiEmeNHtipMQSD5CbQvwUeZNMkFYR5QLcKpEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه ترامپ برای حمله زمینی به جنوب/ ایران با این سلاح ها آمریکا را شکست می دهد
🔹
نزدیکی ایران به محل استقرار نیروهای آمریکایی سبب می شود که توپخانه ایران فعال شود و ثمربخشی چندبرابری آن را تضمین می کند. توپخانه به دلیل نوع پرتاب توپ و نحوه عملکردش قابلیت رهگیری توسط پدافندهای دشمن را ندارد و به دلیل نزدیکی به محل استقرار دشمن (در جنوب) ضربات سنگینی می تواند به آمریکایی ها وارد کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3232047</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/akhbarefori/673919" target="_blank">📅 23:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673918">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای پیت هگست: انهدام تمامی قایق‌های تندروی ایران، تمامی تیربارهای نصب‌شده بر روی این قایق‌ها یا تمامی موشک‌های کروز آنها امکان‌پذیر نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/673918" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673916">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddfd4c9329.mp4?token=gsbrYDoJvCQrMAnyy4gELd9Ci0pc9IP0IN3LHnVVnMBg5njziVz3FE95nz0zyc8JAdiTQAe96YHyyXJ9UOSxrXnCrxKcgxebCPVuaC_Dcmggjr_TB4R9xvGb3qh9TVyfw9pyT3cBmZvf9iK88CoR3Xft_nm11AWbXj-tIjjWc5vSM0p-F6sMt2sDA34paTC5PKBxQynwUF7bbNfsLVq2T38DdW8iYr2pwzhdKDjGRl0cMQVMI5S27uP914yeTy1aca0I-VsEK5EwupCRuC0nWOQYKT5sljFZc_wKRhfoQPlqe4rPsbxNsp9lEObTPM5TUtRixEkvE7WBn6a2859XEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddfd4c9329.mp4?token=gsbrYDoJvCQrMAnyy4gELd9Ci0pc9IP0IN3LHnVVnMBg5njziVz3FE95nz0zyc8JAdiTQAe96YHyyXJ9UOSxrXnCrxKcgxebCPVuaC_Dcmggjr_TB4R9xvGb3qh9TVyfw9pyT3cBmZvf9iK88CoR3Xft_nm11AWbXj-tIjjWc5vSM0p-F6sMt2sDA34paTC5PKBxQynwUF7bbNfsLVq2T38DdW8iYr2pwzhdKDjGRl0cMQVMI5S27uP914yeTy1aca0I-VsEK5EwupCRuC0nWOQYKT5sljFZc_wKRhfoQPlqe4rPsbxNsp9lEObTPM5TUtRixEkvE7WBn6a2859XEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطرۀ ایمان تاجیک، سخنگوی عملیات وعده صادق از دیدار با رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/673916" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673914">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: جنگ با ایران تا کنون ۳۷.۵ میلیارد دلار هزینه داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/673914" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=R5-trgeH_F0p5pFlCozucFODMwbkuTA9qIpnkDT7qdyf9QFGKT8aw754ykr_mpzvOuphlP7H1DNnJc7IEhMnP-oxe8Fln5cDL3bD1mS7khywsxYp9hbr0lNzXfIcjGUfEI9t9hgE9vvuR-6Y4IggkUaglXJAyvmX7NjnxNGRiQLOMHZztDxXuYZCtcBttfjYcUC7wfZI6eCKBXCB8h9c8ets3kgTa5pmJM4YkF70edb3SY_HBHUnUt0Ib89HuM1C3i99Ki4g-N_cwkpNLW1jmo5euyGYiStv0THTnQkv7LIBqmKa5ikqoVPmHv_uPck-HIb6Mer2_J4EGKUMnuPVzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ff5728bb.mp4?token=R5-trgeH_F0p5pFlCozucFODMwbkuTA9qIpnkDT7qdyf9QFGKT8aw754ykr_mpzvOuphlP7H1DNnJc7IEhMnP-oxe8Fln5cDL3bD1mS7khywsxYp9hbr0lNzXfIcjGUfEI9t9hgE9vvuR-6Y4IggkUaglXJAyvmX7NjnxNGRiQLOMHZztDxXuYZCtcBttfjYcUC7wfZI6eCKBXCB8h9c8ets3kgTa5pmJM4YkF70edb3SY_HBHUnUt0Ib89HuM1C3i99Ki4g-N_cwkpNLW1jmo5euyGYiStv0THTnQkv7LIBqmKa5ikqoVPmHv_uPck-HIb6Mer2_J4EGKUMnuPVzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌پردۀ فراخوانی که به‌ اسم انقلابی‌ها منتشر شد چه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/akhbarefori/673913" target="_blank">📅 23:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673912">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb25034032.mp4?token=hkM75rGSxeZEcs_IBE3yGNdi2AHChgJiAUxQxBpaJ1n-AvVRBDXdGBFyIV08exIv1zVCzBINsDegGkTFaZXNuSepcAL9Qyk4XZ-o4UfZv3j-2OiupeioUDJoiQYMx7V-yW3W7lJEQutQQf5aej4ep0BIbpWo0am_FO7NNsJxpjfb2iRrKdzXNTH5GryuLF60dmQx0Oc2IoAcn-B5dZs2yLWLALMMMNM3ax4RYoeSnksk7m8n1nNeECGXiS0LrF_1zZ04W6l3TeiQYttfwxYLnVVyc4LjZ0u2qFWMIWkzTK0JAM2EQ5mJIyxyn9CR5haL8hM0NYoDeZEM8guL-FX35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb25034032.mp4?token=hkM75rGSxeZEcs_IBE3yGNdi2AHChgJiAUxQxBpaJ1n-AvVRBDXdGBFyIV08exIv1zVCzBINsDegGkTFaZXNuSepcAL9Qyk4XZ-o4UfZv3j-2OiupeioUDJoiQYMx7V-yW3W7lJEQutQQf5aej4ep0BIbpWo0am_FO7NNsJxpjfb2iRrKdzXNTH5GryuLF60dmQx0Oc2IoAcn-B5dZs2yLWLALMMMNM3ax4RYoeSnksk7m8n1nNeECGXiS0LrF_1zZ04W6l3TeiQYttfwxYLnVVyc4LjZ0u2qFWMIWkzTK0JAM2EQ5mJIyxyn9CR5haL8hM0NYoDeZEM8guL-FX35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان ضدجنگ در جلسهٔ سنا، سخنان پیت هگزت را قطع کردند و فریاد زدند: بمباران کودکان در ایران و فلسطین را متوقف کنید!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/akhbarefori/673912" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673911">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlijnJ8EW09oJsobnvM7g_Z4hpLPPi4E7K5egDIZzHu104XYb0wsuoSrwf34yWFt1Bsw1gqHOJWuleakiWm8xZ3m83MpKKXvcTX06L0qhadvuh5byUMifJXW4wUUmvpxSWYKaE9uFtB9V6Pk1Cj6zkP5zBlKueU5L1v5FxM7wt4Y3a6XfuhFeAjXO0Fg5AgKB69luhpVaBbttTObaQRmwomRqDR03iIwD-Nn07DRboDNOs8AfXDw9Xfxfuck8Huaa6AxaHIVVHI9oGOqFxbLCHZ6dSiCSExAAYQFktY8_2yN2QLX6QgStLzSoRGNxMXhr37baE01a1gQ4DRXPLlVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار: ۱۸ آمریکایی در جنگ علیه ایران کشته شد
🔹
جنگ افغانستان: ۲۰ سال، ۲۰۰۰ کشته
🔹
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
🔹
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
🔹
جنگ کره: ۳ سال و یک ماه، ۳۶۵۷۴ کشته.
🔹
جنگ ونزوئلا: ۱ روز، ۰ کشته.
🔹
درگیری نظامی ایران: ۴ ماه، ۱۸ کشته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/akhbarefori/673911" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
