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
<img src="https://cdn4.telesco.pe/file/rRy6W8AufzNDyFrtxpqDP6zFzqvpCBS-O9HoYtZBgn6QEBoXSEwfqn9x4vVifIL_XE1JFYNXSXyfPOiaMqmlrXrjFq2B3UIlL7HYKnywPp4rHXXW4D_sA52x626WjCh8hMlKHbYg15Ay8W-xHnAh5FAtv2z1B8Kuwk11j0L8pAxKjPcv4waqGQAWOc7f9byRIGbBfpb_gH21hN12oHtgiY-JAyJfD0XzauWYpo9anXwXtknPqGRRCKxx3Xcs0NDgdPXsARtcoZDxbioDeKOk2v1KFu_lzgGWPBgo-r3wIzL1igCcAQ-pe-mr-30_QjMsKnhJETWxuGEW3BqdR40REw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-694314">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سازمان هدفمندسازی یارانه‌ها: حساب کشاورزان شارژ شد
🔹
این مرحله از پرداخت‌ها شامل کشاورزانی است که گندم خود را تا ۶ مهرماه به مراکز خرید تضمینی تحویل داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/694314" target="_blank">📅 19:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuVYu7vL565xAi-vbdpWZEUlJYpeeRkhzBMu63xDRfVDZz0nTHa-bWnT7BxE4XX9E1OdsX25dYbeiGWwPe9zeMBEv6nm8y1i1c76dbj3u-imKBpMky8LdnwY4-QiLXO4uw15VX7o70X6071aCm9YA2mBtUQ7FWukwQhwvYXkHmkkrgha6FbEGju5EzX9tJqvzcVhuM0PGLe0bCoTBaQR-6m_poIlJt96i6p7fMeA58p7aj7r5YpRbu-BCouK01UJBG4cN-OYYP5MDylrS_JyeYAzx70EsN30JvPUP1y6ex5hpLbg-oA-d14TooV93sz6QYMnJG3SJS2D_HEe869uhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین راهنمای بالینی ایرانی در مدیریت سرطان‌های زنان مرتبط با HPV، با مشارکت انجمن انکولوژی زنان ایران و جمعی از متخصصان این حوزه و همراهی داروسازی دکتر عبیدی، پنجشنبه ۲ مهرماه ۱۴۰۵ در هتل استقلال تهران رونمایی شد
🔹
این سند با هدف ایجاد مسیری علمی و کاربردی برای پیشگیری، غربالگری، تشخیص و مدیریت بیماری‌های مرتبط با HPV تدوین شده است.
🔹
در این رویداد بیش از ۲۰۰ پزشک و متخصص از سراسر کشور به‌صورت حضوری حضور داشتند و بیش از ۴۰۰ پزشک نیز به‌شکل آنلاین در برنامه شرکت کردند.
🔹
دکتر بنفشه ایزدیار، مدیر واحد سلامت خانواده و داروهای تخصصی داروسازی دکتر عبیدی گفت: « برای اولین بار در کشور، یک گایدلاین تخصصی برای پیشگیری، غربالگری، تشخیص و مدیریت سرطان‌های مرتبط با HPV با همکاری داروسازی دکتر عبیدی و انجمن انکولوژی زنان تدوین شده است. این اتفاق در ۸۰سالگی داروسازی دکتر عبیدی، نمونه‌ای از نگاه ما به سلامت زنان و سلامت جامعه است و نشان می‌دهد که این مسیر، در کنار توسعه محصولات، ادامه دارد.»</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/694313" target="_blank">📅 19:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
غیررسمی | رصد شلیک چندین موشک‌ از خاک ایران @AkhbareFori</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/694312" target="_blank">📅 19:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
غیررسمی | رصد شلیک چندین موشک‌ از خاک ایران
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/694310" target="_blank">📅 19:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694308">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
عرضه ارز تا سقف ۱۰ هزار دلار برای هر ایرانی
🔹
فرآیند عرضه ارز از امروز آغاز شده و در مرحله نخست یک میلیارد دلار از طریق شعب منتخب بانک‌ها و صرافی‌های بانکی عرضه می‌شود.
🔹
افراد بالای ۱۸ سال با ارائه کارت ملی می‌توانند تا سقف ۱۰ هزار دلار ارز دریافت کنند.…</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/694308" target="_blank">📅 19:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694307">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCho6Pl7Q7Lsh9dnuFy2RioT6qVE3yC7YidMaKg3JWQkQqzKzF0tX6WbcsswCZKvQlzSNVGNOAyAGxq0wdLY4BtvcfXp0s5lJUICjgQDTchgLQRx8kbPSoAGWmLqKpy2WHuAk-IoEJQ78MyZx4d4CSGln1GSvmXwS5A9FOBT7H-pQTLj1vTI5lWOdCHoBbQ_FZyxqNgWwVrjBxgnOa6zwy8G0AWgG2thqLyauubxG_fTR_3qx8DKcH4UpOi1NYJy2LoLbjZN8umKAgUkl_WGDaxIUMJn-QYMZwtyH5IFui8bqqWTG-GHx32vEpz0Y0OZJ2zZNREkcuPZb9Sq9cgbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری مجید واشقانی؛ عکسی که قدیمی نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/694307" target="_blank">📅 19:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694306">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGY8X7VQxhs2Y_4Xx7HlAeFjGvlRGp2ueMeh24ykfpB5scuZ_AuevXoPOJaGkRTPGOpZSIFkzQOZvzFzRRG3vYClrdYInq9BfnHm2H7ZCg4bK7iEmKKlY3WYVVzN1QUGM2PezCOIkakZuPrUoJr3ddRwanJ9rD6gECflrQnf6eGoBr6_n7Ao9tb6I-Zv4dgSrktSMNHxGQO_-Bo2fn-N0gj3ytUfw0B9ytg4cn0l8bjhBpYBnp-xGX-cLHKvZKGQNhdIQ93oFvu83EY1vPdVWHbAC_Girwg_wwE3s8u6U4bkIPi19rTWPTs4yvCJH8yINRGCR4H2mLyYgO0pZIx9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناخن‌ها صحبت می‌کنند؛ نشانه‌ها را دست‌کم نگیر!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/694306" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694305">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twLsUkpjWLOCSJDRGRfdX6FGsTOksbW453n-iXAsagP2Ktyw858zH5YSAhRYVJdoYv_aFvOm2c9Ooxlqh04PzcoRR8Pfh9RoqKl56vDa0btW23in_ICyEnTCdjY0iWjOu2v8RthQ55TlKsJqbUXVMUnskOu4qKolurlh8dJGZ38zOJH08M3xcRo610Yzteh1Mi0FDlk1x_T8cqV_tGEyHFzblIy0sHKeFpLyN--cMh96ON2LWqxrSfJG0okF86VMI8GY_kPzKY-47ycv1FA5djegT-iIsLDqK6CidSZLfp07ASSkZ-6fDE2UdU_iaxTLITq2TDt-z6iIy9RnBZ04ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصت رشد فروش حضوری تا ۳۰۰٪!
📈
اگه «فروشگاه حضوری» داری، وقتشه با اسنپ‌پی فرصت‌های بیشتری برای فروش بسازی.
😎
💙
فروشگاهت رو به خرید حضوری با اسنپ‌پی مجهز کن تا میلیون‌ها کاربر فعال، راحت‌تر ازت خرید کنن. می‌پرسی چرا؟
🛍
✅
تسویه نقدی و تضمینی در ابتدای هر ماه
✅
دسترسی به میلیون‌ها کاربر فعال اسنپ‌پی
✅
افزایش قدرت خرید مشتری
✅
کاهش انصراف از خرید
⌛️
فرصت فروش بیشتر رو از دست نده!
از اینجا ثبت‌نام کن:
👇
👇
👇
https://l.snpy.ir/j8wvi
https://l.snpy.ir/j8wvi
https://l.snpy.ir/j8wvi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/694305" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694304">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23998377d.mp4?token=Cm3Mm_d393DpPHxyQo-tnUk6OfBaJ7alPol-HODChOoSNkku7Su0LYQiLW90OE2_ertTPyReUsEgnrPYRG9O7yvi2tfzdQjXFs62eOSAUx797fh18FlbYkFxbNSyC_KCj_lS43A7cNcDJSBZ7TuUmAvENeosMl7tlbrBQXknCtF25qT1uzxqpPMtRjiS_aUorAxmAkDtnSux5ljlC0CNRkQxmVMX2tzMIBlf-P8OLjioCsrykM3W_li8b9PoE7KuWXMmlf51dbBTCBDzsrzLTQ1cj8JC8I2wFna_hlfoA5_02Ka_11hLz_X6OoKhYV9GsmICYxZbckHN_SRYo2jmNIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23998377d.mp4?token=Cm3Mm_d393DpPHxyQo-tnUk6OfBaJ7alPol-HODChOoSNkku7Su0LYQiLW90OE2_ertTPyReUsEgnrPYRG9O7yvi2tfzdQjXFs62eOSAUx797fh18FlbYkFxbNSyC_KCj_lS43A7cNcDJSBZ7TuUmAvENeosMl7tlbrBQXknCtF25qT1uzxqpPMtRjiS_aUorAxmAkDtnSux5ljlC0CNRkQxmVMX2tzMIBlf-P8OLjioCsrykM3W_li8b9PoE7KuWXMmlf51dbBTCBDzsrzLTQ1cj8JC8I2wFna_hlfoA5_02Ka_11hLz_X6OoKhYV9GsmICYxZbckHN_SRYo2jmNIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت اسرائیلی‌ها از این نقاشی‌های کودکان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/694304" target="_blank">📅 19:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694303">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/694303" target="_blank">📅 19:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694302">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVSfNNga4Q5GsFXlAAybGObSCltvHVI1hksi8z4Uz2NpnREv2_iwBUWO7kC8Ixcckrg1BjFEJgan8IY8lV50iDLi3imgt5A7YUZOPJYGK7O2e4PMHXdqWyNliQFtY6b7HXugio7GW5-MT9IDuzGf-HN5Yvh8aQLKk3JJF0v2IHqdTrZ1H9M4CqzzZQd4OcWMVitPOS8Ey4GmPLrbbSrFBNy9trmfiMVs419Drqjz43A0kcP_EPe9blkp9ienU3ONMQvwIqeWsJBdHWCG4icHRHStSSMl-IRLgt1ndRQyrfr3galbPuxHC4RU8-uhRFIm2_VHdFzP8CJmNuOEjxlcaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسم‌های جالب دوتا از روستاهای شمال کشور!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/694302" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694301">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
معاملات شبانه تتر متوقف شد
🔹
صرافی های رمز ارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کردند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/694301" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694300">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
،
شنود
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/694300" target="_blank">📅 18:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694299">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه‌ کوثر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrugopOJDgiwlt9pKzq8SXFM98XLm23F7b7fqi4vG-k0SUtVk4iWu9v-p3r6gAyKaG_ElpCnLKGeVsPnT85NyRGYVTYbcNjuZ2WfwRIcv7BeKGuy9fpwiRT5Jdq9lnaOriMajNCT-76VN5M6ab7RKZOQtPIMgeWI6iTZaza85OYL_5F3CpU3cE_Os8won1fvDv_DsTwd067kHdcRBEexsN8wvCN1IK_A1tevSD9Qt-5Q1Cy1f_AKqJTXPEQgmQMxEdsv5NPN28pxDiBKg3IAa9bASx82n87dbvUehi58Q3pkOCb4BKBn5tdwF01Y5_DFMwU7NIOoroV1b80F6eUBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد خیره کننده ۲۳۲ درصدی فروش در شهریور ماه
عبور پرتفوی شش ماهه بیمه کوثر از ۳۷ همت
بیمه کوثر در شش‌ماهه نخست سال ۱۴۰۵ با ثبت رشد ۵۹ درصدی حق‌بیمه تولیدی، بیش از ۱۳ هزار و ۹۰۰ میلیارد تومان به حجم فروش خود نسبت به مدت مشابه سال گذشته افزود و مجموع حق‌بیمه تولیدی شرکت را به بیش از ۳۷ هزار و ۷۰۰ میلیارد تومان رساند.
به گزارش روابط عمومی و تبلیغات و اعلام معاون برنامه‌ریزی بیمه‌کوثر، بررسی عملکرد سال جاری نشان می‌دهد شرکت در  یک ماهه منتهی به شهریور ۱۴۰۵، موفق به کسب درآمد بیش از ۱۴ هزار میلیارد تومانی از محل فروش حق بیمه شد که این رقم نسبت به مدت مشابه سال قبل با رشد چشمگیر ۲۳۲ درصدی همراه بوده است.
یداله عظیمی در ادامه افزود: بر اساس عملکرد ثبت‌شده، ۸۸ درصد از حق‌بیمه تولیدی بیمه کوثر در رشته‌های غیرزندگی و ۱۲ درصد در رشته‌های زندگی محقق شده است. در میان رشته‌های مختلف نیز، بیمه‌های حوادث و بدنه بیشترین رشد فروش را تجربه کرده‌اند؛ به‌گونه‌ای که حق‌بیمه تولیدی رشته حوادث ۱۷۱ درصد و رشته بدنه ۱۰۱ درصد نسبت به مدت مشابه سال گذشته افزایش یافته است.
ما را پیام‌رسان
بله
دنبال کنید:
‌
✅
کانال
بله
‌
‌</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/694299" target="_blank">📅 18:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694298">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">😀
تکذیب درگذشت مهندس میرحسین موسوی، نخست وزیر دوران دفاع مقدس
😀
به دنبال انتشار برخی شایعات در فضای مجازی مبنی درگذشت مهندس میرحسین موسوی یکی از نزدیکان ایشان ضمن تکذیب این خبر گفت که نخست وزیر دوران دفاع مقدس در قید حیات هستند و شرایط عمومی حال ایشان خوب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/694298" target="_blank">📅 18:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694297">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
شرکت هواپیمایی عراق: پروازها به ایران از ماه اکتبر (۹ مهر) با مبدا نجف آغاز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/694297" target="_blank">📅 18:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694296">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
الجزیره: آمریکا احتمالا پیشنهاد جدیدی برای توافق با ایران داده است
🔹
به گفته یک تحلیلگر، واشنگتن احتمالا به دنبال تغییر زمان‌بندی اجرای توافق پیشنهادی با ایران است.
🔹
لوسیانو زاکارا گفت اختلاف اصلی بر سر نحوه اجرا و ترتیب‌بندی بخش‌های مختلف توافق است.
🇮🇷
…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/694296" target="_blank">📅 18:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694295">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3Nhio57trQA7vGWPxWe1vVb3NmEgfFvrT8g0LmktElQzeuCqHIb7jCTPjK-13nWar8dudY3-62dkhrOl4IbG0gkTbJdq-7AnH4I8n87rCWC4NVgb1Ltj3_0TKiixH_HyC6B0LhT_sbmM0P3IjABzTqusO3ZNdRbUrmoZSRPfs9T-1cMD-q37rpRn2Jhd1wpvr-gmWxqSSMJpIibxlq-7GFrK72cq9mKmxf9Sn5tdgREhjLG42Sz8dEA8ZydiH4KVtFX-XqZPSiKzIrZsPBFnUw-oJlH_5up_4yzJOpLKm1fSOv455sS4riRHiz5eo6huUVY8VmzoYiGNKtQRLdqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ خواستار عرضه ۴۰ میلیون بشکه از ذخایر نفت آمریکا شد
🔹
موجودی ذخایر راهبردی نفت آمریکا با کاهش حدود ۱۳۰ میلیون بشکه‌ای از اوایل آوریل، به حدود ۲۸۴ میلیون بشکه رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/694295" target="_blank">📅 18:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694294">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-G49bBSiin9bYkrkoi06j0gaaE1o6GmRFhLGJwte_nOA7ZJp-fQLkeU0EXFj2S41xUYzVTBFE1IWhvRQz-T2hyxM9LKntFsy3dIv3CBpMuv6WzxNacz1V1HAsMcFljFEVPnzQi3srzNdaufRks959ru7izi9oHhO0m-Mauz7Mxf_DIHfWKYlQ2CDZ9r4zhmvfvNHfgkkqlXq0OIWfjxAflYOe7s3DDqxwgLINAIA_G2cWtmEMUVGZFOuWYgrui20CHYfowFwOgD_zVByqWnIqjaDFLZ9HlAKMLZV36GumxR3oRzUfP9H3O2FjcHesJvv518eBk7XjM9pmByRuCXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع ریتم‌های قلبی
❤️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/694294" target="_blank">📅 18:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694293">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCgOtklgpQUM16dS3_KLGjQR8u1iSe3an9AI0ncjfI0IT-5VtLOxy-rlB4sNcaahXHeSGa3Zjb8hRHAyqZXULbkPQHjUcHWRQg1AevsCA8skypgAZtCEwSWmkWSCcebOEW6GoeJy8SL6qdhawZO6tdAQ5PILFjBxWdwALy2Cq7NUMxCPod9Wnj7Bum3P6JuNjN19wzp5hlGbYibHpaaXlxkpmhRDrlDsyMQWTYm9bm7UKeJ5Thq-x9iXGi1-i421Zyot1BvAXFC7M98EMAxN-AH188xX9G1sqZ6oINbhxvcjvXpJqJK_uT6u7wMhKASy0VcQ5vvNqtJoXkaLyrlvKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری مراسم دومین سالگرد شهادت سید حسن نصرالله در لبنان با حضور حجت‌الاسلام پناهیان، حاج حسین یکتا و سعید حدادیان
🔹
همزمان با دومین سالگرد شهادت سید حسن نصرالله، دبیرکل فقید حزب‌الله لبنان، مراسمی در مرقد «سید شهدای امت» برگزار می‌شود.
🔹
این مراسم با حضور جمعی از چهره‌های فرهنگی، هنری و ورزشی ایرانی که به مناسبت دومین سالگرد شهادت سید حسن نصرالله به لبنان سفر کرده‌اند، برگزار خواهد شد.
🔹
حجت‌الاسلام پناهیان در این مراسم سخنرانی خواهد کرد و حاج حسین یکتا به روایت‌گری می‌پردازد؛ همچنین سعید حدادیان نیز در این برنامه به نوحه‌خوانی می‌پردازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/694293" target="_blank">📅 18:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694292">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
قیمت بنزین در امارات بر اساس سازوکار ماهانه قیمت‌گذاری سوخت، حدود ۱۶ درصد افزایش می‌یابد
🔹
قیمت سوخت در این کشور هر ماه با توجه به تحولات بازار انرژی بازبینی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/694292" target="_blank">📅 18:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694291">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اخبار تائید نشده از شنیده شده صدای انفجار در شرق عربستان سعودی حکایت دارد/ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/694291" target="_blank">📅 18:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694290">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اتحادیه اروپا در تازه‌ترین تصمیم خود در حوزه هوانوردی، تعلیق پروازها در حریم هوایی عراق، لبنان، اردن و ایران را تا اواسط اکتبر ۲۰۲۶ تمدید کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/694290" target="_blank">📅 18:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694289">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
داخل یکدونه قهوه چه خبره؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/694289" target="_blank">📅 18:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694288">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاجاره ویلا | جاباما</strong></div>
<div class="tg-text">اینطوری سفر برو
🤖
✨
از رویاپردازی اینکه کجا بریم و چطوری مقصد رو انتخاب کنیم تا  اینکه واسه سفر بعدی چه پلنی بریزیم؛ AI  داره کم‌کم وارد بخش‌های مختلف سفر میشه.
توی این ویدیو رفتیم ببینیم پشت قابلیت‌های جدید جاباما چه خبره و قراره تجربه سفرمون چطور تغییر کنه.
👀
🏡
ویدیوی کامل
👇
https://www.jabama.com/landing/release-1405-summer?utm_source=telegram&utm_medium=social&utm_campaign=jbtg
@jabama_com</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/694288" target="_blank">📅 18:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694287">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5e99798a.mp4?token=B4V4r2UGVn_QrB0VG3muVNnJyysD2yVMsHBZThbPjXbbmuV8esfKx93MWrRLS2AosAacb1ELXytyHvpLD9Hf_ycRnG9hsAov_kyEndUs9eqpYsiocQuYPemf6NWTLx6y_Ogy4Pwf5r6kGhawaarAqiYKl9RpP0YbBQjwyjgWl7RUR_6DiFZmo-bqeR_7mInsXMLz1G4F4kGBYSaGufaiYYqZ9_0nOD6bpmsgpMWFiAlcGuFATBczS6sO0uZwoi7L2YpTwVAPL-TlotGcOiCDWNhjHvUFrjqqx5X8Xuh6WLXvpEwB8xaUTR_fNEeubW0sAK1DL1rZ52uGo72JMvPQgSXJe5pIqvqbbCS3y3KV2H6j2P9vFLxRbK96Bs5YRuvtmpcnIFixIn1gl_hvklbU3RhGdSCBzGfGcoUm4j-n5-Uk0e9AHfaVsmBZm6Jf_9iTbAKTQXbzJvHF5TS4SErtWGmxJ0AAxezqoA5U2JUDmvc4h7meG74qVIAcmjt4rfxuXm3FQ_s2SUzXfAu8kAWa2edLZAmTJk65D6DoLA9hYQ6ra2n7WCsAjNMCuKRnf5hZwdwHJow-zGBi99NZ9cd_fqdw7N4culIibRPwvnuWKFTdUG4WZLHDZXZfFWgjWp9FySJMtEnQiaJulaLLg0kYB0ephZZJEXKbOPQslfdZrBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5e99798a.mp4?token=B4V4r2UGVn_QrB0VG3muVNnJyysD2yVMsHBZThbPjXbbmuV8esfKx93MWrRLS2AosAacb1ELXytyHvpLD9Hf_ycRnG9hsAov_kyEndUs9eqpYsiocQuYPemf6NWTLx6y_Ogy4Pwf5r6kGhawaarAqiYKl9RpP0YbBQjwyjgWl7RUR_6DiFZmo-bqeR_7mInsXMLz1G4F4kGBYSaGufaiYYqZ9_0nOD6bpmsgpMWFiAlcGuFATBczS6sO0uZwoi7L2YpTwVAPL-TlotGcOiCDWNhjHvUFrjqqx5X8Xuh6WLXvpEwB8xaUTR_fNEeubW0sAK1DL1rZ52uGo72JMvPQgSXJe5pIqvqbbCS3y3KV2H6j2P9vFLxRbK96Bs5YRuvtmpcnIFixIn1gl_hvklbU3RhGdSCBzGfGcoUm4j-n5-Uk0e9AHfaVsmBZm6Jf_9iTbAKTQXbzJvHF5TS4SErtWGmxJ0AAxezqoA5U2JUDmvc4h7meG74qVIAcmjt4rfxuXm3FQ_s2SUzXfAu8kAWa2edLZAmTJk65D6DoLA9hYQ6ra2n7WCsAjNMCuKRnf5hZwdwHJow-zGBi99NZ9cd_fqdw7N4culIibRPwvnuWKFTdUG4WZLHDZXZfFWgjWp9FySJMtEnQiaJulaLLg0kYB0ephZZJEXKbOPQslfdZrBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای آمریکا در حال ترک عراق هستند
🔹
انتظار می‌رود خروج این نیروها تا فردا تکمیل شود و ۲۳ سال تجاوز و اشغالگری به پایان برسد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/694287" target="_blank">📅 18:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694286">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/694286" target="_blank">📅 17:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694285">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
الجزیره: آمریکا احتمالا پیشنهاد جدیدی برای توافق با ایران داده است
🔹
به گفته یک تحلیلگر، واشنگتن احتمالا به دنبال تغییر زمان‌بندی اجرای توافق پیشنهادی با ایران است.
🔹
لوسیانو زاکارا گفت اختلاف اصلی بر سر نحوه اجرا و ترتیب‌بندی بخش‌های مختلف توافق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/694285" target="_blank">📅 17:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694284">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0EP4hekFfjA4Hkm0pm0Q2y84TEqcVAU5pT-N75fkySdBq8H-crvzEq67kzVpx5SxSFuGz2AqPxNKxF6X_PRqZUeCXD8H5OpCtWddwd9woKNA_w-NStupJ8cPUBy8PaHqpj2wVOHFayMiR7vyQv4VXoagoKqZvOEU6k6prGFjjfUPRmcdEuI0ewADbf8cVNXIteqyzsRcFENrvahbe-QHPqwUxAGZDyI7mWg_z3K6rj_HHOt4MA0eW3HXHpXQKHkz5_qc5m7jH81EPCZlDTa4HzVXYmo_eQu0Kf2jHFTMcyZCpMq1zgQcdT9HteI8AM2_kojMi7WQv21Ed0sPfzN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: میزبانی از قصاب غزه پیامدهای مثبتی نخواهد داشت
دبیر شورای عالی امنیت ملی:
🔹
همان‌طور که میزبانی پایگاه‌های نظامی آمریکا برای شما امنیت به ارمغان نیاورده است، میزبانی از «قصاب غزه» نیز پیامدهای مثبتی نخواهد داشت.
🔹
از جنگ اخیر درس بگیرید، از آغاز جنگ دست بردارید و از طرح ادعاهای بی‌اساس درباره جزایر ایرانی خودداری کنید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/694284" target="_blank">📅 17:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694283">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31cb6d497a.mp4?token=mkVgYhyTLUae8k7SLKh04NdRt-6KQR_DI24NiPVGMYOhbibE_Oqdd-IbIi4RKRYSKGbLFaFxoLXqKrVccoagtzU5UocrzD6NfZ46cJKrMx9GxoCMnzVGzLmxv1_uyj71pOTcrs-e3eijRGGHjwPuN3u9tc2Oj7eFq27csXf48xoErmmkBt66jsH0LNbjVTUJ3qwOnNVY2bjBiNznalShIEYLKFUGVMSZBJ6GdHOMXURSr9KEaXCAGa6OfdANTw50_mUWXIOyY-Q3XZgQDuYrjL14vai4P0z6CFqGQiIPgLdRac5NTa14bjuxp7jWt_g8JmrTXlAIb2Pp6bKlHui2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31cb6d497a.mp4?token=mkVgYhyTLUae8k7SLKh04NdRt-6KQR_DI24NiPVGMYOhbibE_Oqdd-IbIi4RKRYSKGbLFaFxoLXqKrVccoagtzU5UocrzD6NfZ46cJKrMx9GxoCMnzVGzLmxv1_uyj71pOTcrs-e3eijRGGHjwPuN3u9tc2Oj7eFq27csXf48xoErmmkBt66jsH0LNbjVTUJ3qwOnNVY2bjBiNznalShIEYLKFUGVMSZBJ6GdHOMXURSr9KEaXCAGa6OfdANTw50_mUWXIOyY-Q3XZgQDuYrjL14vai4P0z6CFqGQiIPgLdRac5NTa14bjuxp7jWt_g8JmrTXlAIb2Pp6bKlHui2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش شدید تگرگ در سراوان، سیستان و بلوچستان
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/694283" target="_blank">📅 17:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694282">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بانک مرکزی در بخشنامه‌ای ممنوعیت اعطای مستقیم و غیرمستقیم تسهیلات بانکی برای خرید طلا، ارز و رمزارز را ابلاغ کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/694282" target="_blank">📅 17:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694281">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
فورچون: ترامپ و ایران هر دو در محاصره‌اند!
رسانه آمریکایی فورچون:
🔹
ترامپ و تهران تا انتخابات میان‌دوره‌ای در یک جعبه قرار دارند و هر دو محاصره هستند؛ ایران می‌خواهد قیمت بنزین در آمریکا را بالا نگه دارد و با بلا بردن فشار بر آمریکا ترامپ را تسلیم کند.
🔹
ترامپ هم می‌خواهد با محاصره اقتصادی ایران را وادار به تسلیم کند؛ افزایش قیمت نفت منجر به بالارفتن تورم در آمریکا شده که این موضوع تورم بازده بازار اوراق قرضه را افزایش می‌دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/694281" target="_blank">📅 17:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694280">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMySZtTXf5_sxOXLL1WUbASLU16IYnZoaImxWHQEDZT6ouoLGMneLVIlqdeQD3Wp5q6ZRLVbEMJW_l8_AG9uY32aOcFvPSk-QKoZofziWapz3lWr_2JZ71IxnFMydF7ZtbU5jVn3KjHuj696jThM_mw1dCyp0YcMQBFCOGFxJi9F1lElcQ8EcnDGtKlRkeRKT6yAvnH23t1apFu8P0aG_ksVB0qnU1sHSkz8O1zZw5dV2jndduljlABcMmD1iMbG_IXquD6qZ1RNDFN8tfA1S5RUuV4m7HMWdLT351HJVT_42ZJVfl0jJ7MM5IE4HFjYW2yFbua2nUyuYDPIgYen1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر خانواده‌های شهدا و ایثارگران از رئیس قوه قضاییه/ عدالت، چپ و راست نمی‌شناسد
🔹
جمعی از خانواده‌های معظم شهدا و ایثارگران با انتشار متنی خطاب به حجت‌الاسلام والمسلمین محسنی اژه‌ای، رئیس قوه قضاییه، از رویکرد دستگاه قضا در رسیدگی به پرونده چهره‌هایی با گرایش‌های سیاسی متفاوت قدردانی کردند.
🔹
در این متن تأکید شده که معیار دستگاه قضایی باید قانون و مستندات پرونده باشد، نه نام، جایگاه یا وابستگی سیاسی افراد.
🔹
امضاکنندگان همچنین نوشته‌اند جامعه اطمینان دارد که در دستگاه قضایی جمهوری اسلامی، تعلقات سیاسی در برابر قانون تعیین‌کننده نیست و هیچ فرد یا جریانی نباید به واسطه موقعیت یا نفوذ خود از دایره پاسخگویی خارج بماند.
🔹
در پایان نیز از رئیس قوه قضاییه خواسته شده این مسیر با صلابت، شفافیت و استقلال از فشارها و ملاحظات سیاسی ادامه یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/694280" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694279">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
عرضه ارز تا سقف ۱۰ هزار دلار برای هر ایرانی
🔹
فرآیند عرضه ارز از امروز آغاز شده و در مرحله نخست یک میلیارد دلار از طریق شعب منتخب بانک‌ها و صرافی‌های بانکی عرضه می‌شود.
🔹
افراد بالای ۱۸ سال با ارائه کارت ملی می‌توانند تا سقف ۱۰ هزار دلار ارز دریافت کنند.…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/694279" target="_blank">📅 17:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694278">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll1RgpMl87RXijMClvikAYwQvwHTtnrEGBxoBSOcsC6AQDiDvbusmZRU4Y92-11uW0i_RjhGl3RIbutG_vhlgRHzjPjvAwpqozKnB-4VTapHxyKMWot6IRxD0BBQfLNMpASQuozqrQZfrvGMcRDKRXkzqLkPwkI_5J-yiFVIib4LAni1iaGJvxlPP1hvhd2NZRwY-ZyJKMSmObvL4VUguQmgIlWmnMMX22UjJw5V2Yxt8BwunULW4ZUPgtOYwvtlOyqITq-yB5lV5TJlqrhx-dnHl-EQhIrizg0orJdZD6v7GZTsXE2TqCF0VtnDe0z8fP823j1_zon4t7otr3zwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرفروش‌ترین کتاب‌های متنی سال ۱۴۰۴
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/694278" target="_blank">📅 17:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
رئیس سازمان بسیج: جنگ تحمیلی سوم زمینه فروپاشی آمریکا و اسرائیل در ذهن مردم جهان را شکل داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/694277" target="_blank">📅 17:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694276">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نتانیاهو: مقامات عربستانی خلبانی را که به همکار خود حمله کرده بود، بازداشت کردند و تحت بازجویی قرار دادند
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/694276" target="_blank">📅 17:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای خسارت نیم میلیارد دلاری سرمایه‌گذار ایرانی علیه کره‌جنوبی رد شد
رسانه کره‌ای جونگ آنگ مدعی شد:
🔹
یک نهاد داوری بین‌المللی، ادعای خسارت ۷۷۰ میلیارد وون (۵۶۶ میلیون دلار) یک سرمایه‌گذار ایرانی علیه سئول در پرونده‌ای ناشی از تصاحب ناموفق یک شرکت کره‌ای را رد کرد
🔹
این پرونده مربوط به لغو قرارداد گروه صنعتی انتخاب برای خرید سهام عمده در دوو الکترونیکس در سال ۲۰۱۱ بود.
🔹
این وزارتخانه اعلام کرد که هیئت در این پرونده جانب کره را گرفت و به دیانی‌ها دستور داد که حدود ۴ میلیارد وون برای هزینه‌های حقوقی و حدود ۸۰۰ میلیون وون هزینه‌های اداری به کره بپردازند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/694275" target="_blank">📅 16:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
چرا
سازمان هواپیمایی ۵۰ بویینگ MD را زمینگیر کرد؟!
دکتر کامبیز بابایی، مدیرعامل پیشین هواپیمایی آسمان:
🔹
حدود ۵ هزار شغل مستقیم در صنعت هوانوردی کشور یک‌شبه از بین رفته است.
🔹
کاری که آمریکا با تحریم صنعت هوایی ما نتوانسته بود انجام دهد، سازمان هواپیمایی کشوری با یک نامه انجام داد.
🔹
درباره ایمنی پروازهای MD ، نامه‌ای برای کسب مجوز پروازها در سفرهای اربعین به مسئولین عراقی نوشته شد و انجام پرواز باوجود هوای ۵۰ درجه عراق بلامانع تشخیص داده شد، اما اکنون چرا این مدل هواپیما ناایمن است؟
🔹
مشخص نیست چرا نامه لغو مجوز بهره‌برداری از هواپیماهای MD را شخص مدیر سازمان امضا نکرده است؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/694274" target="_blank">📅 16:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f087f7eb4.mp4?token=fxKOwoan8OJSILzUWpqdfCQooqTM0s3984DLi7rfKGS0AUmA3rox7jeru6W3AkoP4c7aWu1w-wwt5Du-xYNk0Xyq4R8MtbUpZp-yoYF06ZtLJkET8lVCVL0LS8IlVR7SWWvv2hZUORrvmKV5vQGirQpB8wRdjpLLcUl2zogyj-zYLvUQkcHJprTl6lNXY1IvlqDp6DbP6HFdYoN3feEI7ffSA6UZqLlPd7WyjxpEgJstNfqGXlXBbKDClQhamf8b8c1iPpaVudt-Xa73HkfNRgOx6rvGWFFLBXZDKWKTC40iBDqhgCH75pmQnYwceBfNcl-ehPAIql7F76cqutGPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f087f7eb4.mp4?token=fxKOwoan8OJSILzUWpqdfCQooqTM0s3984DLi7rfKGS0AUmA3rox7jeru6W3AkoP4c7aWu1w-wwt5Du-xYNk0Xyq4R8MtbUpZp-yoYF06ZtLJkET8lVCVL0LS8IlVR7SWWvv2hZUORrvmKV5vQGirQpB8wRdjpLLcUl2zogyj-zYLvUQkcHJprTl6lNXY1IvlqDp6DbP6HFdYoN3feEI7ffSA6UZqLlPd7WyjxpEgJstNfqGXlXBbKDClQhamf8b8c1iPpaVudt-Xa73HkfNRgOx6rvGWFFLBXZDKWKTC40iBDqhgCH75pmQnYwceBfNcl-ehPAIql7F76cqutGPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصویر از بیژن مرتضوی در تهران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/694273" target="_blank">📅 16:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694264">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3dyuJMCEirISL4fts-57vqJhbB2nPlx_FhwGp5MPG8EYh768cPaGcem1VoCCdJBEFnbjIlqCCZSDzCMMwWbMd4-N5gr2k8BidNIkrbwFCPy5C7PFt1Uo5V2GoTyY6Hca73cWBc13UYDAk1zEjOYz5Ykm7puCaFckKzUQR3wjyD3T3509UoWvOxdEbX646ozDW2GDTzNFHJp9iK7XLqZ1rnE9PEki2VLdWdKAwzWqwLMuwLFofb9ZiYh0Bz03lznqyy5k3qTB9ICn3-kkj2vfj5Amfa3QkFEx8i3OlOryng8U0RobChX9TMetctqAGkij4Ndx9mikOWI9NU8K9t5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2YvgIDpwv6HwusGyrDqnDUAogc2XoT4u50vEgFbbWkzSyGj7FpMLbRmOvKY7bZ0FHd2AVvSiV9fTabq5oZxyeM15ZGfaq_bJ_Hv55CRwQNSoIeFDEvfJ_Lam328qnX9wqd_fiU0IXlkfWSyQHQGiNq5-XWVsRy_jCw8YN6sfmt1WdOHvToBXQHKA0wye_2b6ZPW-oKX17o9CwFIAjDLhS7S-HcwAli867012DhAZL6FwkzteNtbS96ygXn5Hen2ysDTpSb89z7M5BYR6ESf5QY1xBs8a9tG7zTqBgB2Tn_zv5d7m9szqu8n21Wd9Yxt3U2vQ0Orxtn9J6Htn5QWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/la9ZPEjkfWXOs9w1jDTFQbyn4kL4cOsuMASQYDCqPb01k3eY7MdmTE9ACEoNtknfioPMRIc4XKBaYDf9NxrNXbxgCV0l-biyltNa8PEv83B-JOeWYnY3MrM50gx1Yt_p6Onn4HbVvQYsgaPk36ECoK7NYh2P1MuD0O1ay-3RRj2GdGN2CDLXkSNzwpQEtPkYUVgVPuu2PSrszOI8nKBuYCt6Ic5ZmFD4JLsVxMyPGSk00vxAmJD1fo5CMYTGAUL3DmfYzOCzMUJ6roYHiEMjJo7N6lD-ZIxDjY3BgltPKeLhj1RjzmrDzhxelexoIvvlAe254cCuM01P9oo68TWY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iw0ADZzp9QtT6mQfiYW2lTKMs5kL_D7Q5wOMSTolr0cRBZZyK2DL-IMYJRj8k86cAI6oLa-VfQ22z8mz0-C2PYYnQsjAcW1XGM4gzM6-nT2YxBzgRfZoLGhOzQ3OgkeyG4-hQSXaIuknXJrZJcqboRpDAsWRX7ePYvR7EvvZPM7d_BwqzuH5GU0k4YyTTTJRrQnEw89BIWaY2ksp-tX8S-efYHZiJ2VFn8b61tGCSQDqbgNxTCvYb3gAEBz9BxTO8-kdLXEVxojaiICZtHyG0CLWYJ193AMmDJYmbf1qYd4o3Os5ifWtiGy28kL0phqKjy4ybNRqWoMPBI1QTfhDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpvI_IOd2QrOX_xJ606xf2wvECV1BEnjOkyLeUGSnHbIuJ0MVGiOBSG458e6Nir-u8QvFJjioG4Sx9MAQYK_U2VtJZxfqHIXbhsK0EFm7EYodd9NZ3s1Kc8c2UzS8zgoL322vRqqEKGJ4WSLVh1ZgZ9dKEjyavL95x4_8i63zmeJFmcuAwz17AJFMDcI0UyXmKdDLZ6-tJxSOqTID0VVE489B51ZNGC8U2dxwaLj59YGp-QsLMRoK5ao4FC7_wMKUTyCpor3mBJ-XGh3gSonAH5xVjvZbmdgf_S84HJjHjPWjLygp4nsA5OqxWU3H2TcrcIewbsQCc3n-ZKm5DefuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ek44wqEld2iynpcBlZFarKAQvre6Dq2SAAAqzPQYgTOlZPcKBN8EW0476lmFrH_cKEMSAFrzuAEQRci5dqfXh7N2sRe_MyGUsJQ9wQ0WK4g3K_cCsuK9c7rVhf62kfLPtHMxgHj0IkuZrZ7fDeefi99eaJXEcJYDIjNt4BrfSn4AtWa1nIvkJ-IRdLd-D9XF1v4R9DZ6q7Oji7IAntbiHpaqmlIkPkMmEtFFuiIcD1lOm622uOxbGv5V7J6v3WR1nyWQ7bTPOwNowdaHYqSU9twNAQOGEYt_angz-3YgoECrI8G5XK5OKHQGCYztLYZWOYzw2Lh4yWF2jIE_UOiRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5mWakTvZPhkIUqlIeDfK07bt-fybpuTFPExCrQY019IF5Vv9QZGdIn-ePWjE4bHDRboZkd4BoJ6LiPzDbU9Dgmn_YYnKznS0m8l4kHcouWteWSb_81cKZFp9YE0N0ygWCLhI7KLemS4kmIJDX-m6YhOr0f4Ew7TbK5e0gOL77cBJ8UBA4-gAYfNU58mUoi2G68oytycicIzPtLOeGucLpEEWXEp9PgNMiTf6gzlLzMW74vIbUIHjs_N2qlBP4__eNcjvr9iUGSN4opQbkvHhoK_YdSc2t0NdjwCOfo8p0JmdNWNd95xtxDQYdpY05Cy0As_FpVEgUQGELRkNeXbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7RyubTbU71MYfNxJWc5s_N88HOUHnF1JoBtBhVPje4_n6tK-f6vY11tvILAxnf1VZgUZV5LseoaI5zEGYgnZ8MSmdtMlZxtY8xZiMHnDnScesJSw5esqFxI6YU7t0ntSZpyW58wclHfOuqs2Mcrtbr0hrnoOOAMCu9dBjDJmKJoyabMjI3n0zdYks8eGJblNMHAjM9La1E8QL6_e8P4ZB7DhnGw-2X3VI58YHyroxk_fpvm7JnoENp73NnBGUQYuAOmtPF-B1rbutDlJN2Ce5fAVFCZgI_lifa9Jg3DqkpZ0ENhr9J5EXzvT26QjIeRsF2hpZBJE5gtP8GzP091ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fey-ach5EAONvUV5MDHFrrSLSXQHs5-ucC9EG4teB5S-mi-CjBqP_UU4JJy8JNMZrsaHpVPqD4Y6ZsHL0oigknH12y6o3pIIokmx2idezR2EwRZ3FU9gxaDvjHZcq-NMXWJOrA66_1d0NaJZ0rnBTtWaoYRZRXdM54jXubqcmqJEJQ_ENZYWVfriEZYbzScQikEWEye8v7nEPM4ADMB1KDLKVdZOFRmly1DwuG7yYWkU4sA-Yi6NkKhr_fz6l21uGLyENb4Wv1HYRHhdWZzPrP_IlAt1yRYYVxCQ_NYy8rgMENWNlQfQkwhjIHiz-4GWJvzmBThUmnGgjyEhDrnT0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر مدل دامنی رو چه‌طور تو فصل پاییز و زمستون، استایل کنیم؟
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/694264" target="_blank">📅 16:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694263">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507b5a8148.mp4?token=ffgSjZT0qOOmC8vK6S7Kx6q7s08sbl1HKPVpKpEcb9RXopS9Wte_med1ISz0QAuHnPJmp6T0uoqP63FCW38_b000ueP4jSxMBZhsSLbOenlZrKaKF5iZKuc5A0nQvZJHO0hSlRW6KtBUHnJ8gbWi62MG44btZroLxYdgp5EsM7MS_jxsKgA8z-1JuUsSe2moMxsvDmngFAZ6zYeJ8kpwRcWaidKnX1ON_50p-WBT50mHZ96oAkdi2ELnJHjEOQMoBWyVXaPitVkQyCZ5YXk9rCZCzIY0A9OB0a-SHu2E2IGFXuAxm8_R5rSBHNl9TCuZUyHoI3ALGY_BaNHz9Z6VsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507b5a8148.mp4?token=ffgSjZT0qOOmC8vK6S7Kx6q7s08sbl1HKPVpKpEcb9RXopS9Wte_med1ISz0QAuHnPJmp6T0uoqP63FCW38_b000ueP4jSxMBZhsSLbOenlZrKaKF5iZKuc5A0nQvZJHO0hSlRW6KtBUHnJ8gbWi62MG44btZroLxYdgp5EsM7MS_jxsKgA8z-1JuUsSe2moMxsvDmngFAZ6zYeJ8kpwRcWaidKnX1ON_50p-WBT50mHZ96oAkdi2ELnJHjEOQMoBWyVXaPitVkQyCZ5YXk9rCZCzIY0A9OB0a-SHu2E2IGFXuAxm8_R5rSBHNl9TCuZUyHoI3ALGY_BaNHz9Z6VsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس شرکت سعودی آرامکو: شرایط فعلی انرژی وخیم است و در بدترین وضعیت قرار دارد
🔹
وضعیت انرژی وخیم‌تر هم خواهد شد زیرا اختلال بسیار گسترده است و تنها به یک منطقه محدود نمی‌شود.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/694263" target="_blank">📅 16:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694262">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پرواز ایران و پاکستان باوجود فشارهای آمریکا همچنان برقرار است/ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/694262" target="_blank">📅 16:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694261">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLzgTUcuy5Bmq81HDvsJ8rik0BvAsoF8SjFD1DC9vUcI1ikQNCY3dHhnYL5RGmLVKt-OgIk1nIu6nqlQnnoR9O2SRjJwg8ddQ00xXCbDCtwVark2eBLGUXjhPTTyfCdPS8LB0RKbhhypcVBlcqIfnprKJMA4NuhZEXR9xzQIA1i55WcW3xJk214va8JJClw3pPbKY-u1PTUe40p_7nTHMJ46BwbiyF9dipf3u0mM7Cw1N8LUZ7K91yMny7SYuWsB2GvlewajwVVxtUMBhRU2nTbfUO--z8NJrbzle57M16gogVaQbQVlACTP9Q_hRNdJSyMyAXL8eDh0mvF0axwbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با بخش‌های اصلی گوشت گوسفند آشنا شو
🥩
🐑
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/694261" target="_blank">📅 16:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694260">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxNc2i_PKQjpdYvmgV0a0LoYY1RBODrmmRtTKnj8GZtzd7wRwK9_OABEuoRzsWUOtEXLpjgDpgA0VPPkinZ1B1bGqL5na4NTcQpP-ReAkv8iG2RIn_7NEqdvnecdSCB52yhz3amq_a_cEeAtyqwHG4g6A8zw4aCcENubpBk73IcXOcOGviAsRZ1lomTxBWXVr8UaLrm37L4ZtAlqkYdpP7OfEcRsXBBBIomwaJADWQzFOUFhqdX9FcuFc9URK9VtJgwYixLKJh1gnZS7md9lKpE65USa1WY_6fUJeQhhCy_L1m174M_tidiREPdfj0EtT9IFvdBU5rZh7umQMaAL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
اقتصادنوین به رکورد تاریخی ۴.۲۸ درصد در NPL رسید
🔹
نسبت تسهیلات غیرجاری به کل تسهیلات پرداختی بانک اقتصادنوین به رکورد تاریخی ۴.۲۸ درصد رسیده است؛ رقمی که در سوابق دو دهه اخیر بانک بی‌سابقه است.
🔻
اطلاعات بیشتر:
▫️
https://enbank.ir/s/mfabbna
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/694260" target="_blank">📅 16:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694258">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhvF8VnGBcg_hivHGqnZD60-Iuaa4gHrNn3InCe56WBF6X0Pnqo2bXla2p_9ApXfZjlIBg1C6_1i4ncAJD_uTXPiOwCsBTuSp-7ZSjxWJkz7WDFevWhGn5UJMaNptHpXDfkZk7-0paNmJXMmAcBDqSQ8lc9Tq3OkoUdq4YEt4fv6nc5v6YVlqLigtwB6GpWlKbK3NcdD5cnAyWmPI9kId7653-Ok-Hs0OJKJSofkNIDAlb7nt9cli1_Qdej0VeUy89GGE_HcVv2Ddjo78AxBM8fOigsVWl5tLGPwkyIyTZILAq_ULkAxYKMqAnFviILBVqw6eq08-hIF05TSfuq_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی وارد ایران شد
🔹
بیژن مرتضوی با انتشار لایوی در صفحه اینستاگرام خود و در فرودگاه امام خمینی، خبر از بازگشتش به ایران داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/694258" target="_blank">📅 16:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694257">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOHLpRCTGCiDO1adyx7Nw1L1g6YcZJPCnz3iezfqvOqIvKrmXiZrfqIZcJoC67jibbMWFgr0dhbVskSh9khbcX9aZdomHdR6PE7_x4i-IBoSWoMb7l2IuNuJ4gFQjQm-CIgw04t4W2IFTiv0FWURCLG2ImRtu6JmFJH-2XxUcIyyD98Ri7QZPGzAAPfje7b7FloFhoXFYhs7IFYFTtvsPhzljcCcgC8bp3FKMWy7plOnRD-PxRGI-jj7TGPiXLH_aMg02mR2AOzQpSxJbTEyfU8JJU__DAVfUnIm031D4kU4JFp7mcYklYgYMTOS-teY0HuiRLQmztt5mXyGtsWUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نظرسنجی جدید درباره ترامپ؛ جمهوری‌خواهان وحشت‌زده شدند
وال‌استریت‌ژورنال:
🔹
در آستانه انتخابات میان‌دوره‌ای آمریکا، محبوبیت دونالد ترامپ به پایین‌ترین سطح ثبت‌شده برای یک رئیس‌جمهور پیش از انتخابات میان‌دوره‌ا از سال ۱۹۹۰ رسیده است.
🔹
بر اساس نظرسنجی جدید، فقط ۳۷ درصد عملکرد ترامپ را تأیید کرده‌اند و ۶۱ درصد با عملکرد او مخالف‌اند.
🔹
نگرانی اصلی رأی‌دهندگان، اقتصاد است که ۶۰ درصد معتقدند سیاست‌های اقتصادی ترامپ وضعیت اقتصاد آمریکا را بدتر کرده است.
🔹
جمهوری‌خواهان با نزدیک شدن به انتخابات میان‌دوره‌ای، از کاهش محبوبیت ترامپ وحشت‌زده هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694257" target="_blank">📅 16:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694256">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
‌
تورم سالانه شهریور به ۷۳.۶ درصد رسید
🔹
طبق گزارش مرکز آمار ایران، تورم سالانه کشور در شهریور ۱۴۰۵ به ۷۳.۶ درصد رسید؛ تورم سالانه خوراکی‌ها، آشامیدنی‌ها و دخانیات نیز ۱۰۸.۸ درصد اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/694256" target="_blank">📅 16:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694255">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
منابع عربی خبر از حمله به شهر نفتی بقیق در عربستان دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/694255" target="_blank">📅 16:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694254">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117dd53865.mp4?token=Xy5uOp-jCPmho2EbUXImQunrD5-Kl2zdbHhaWH24z6SOT7Gtgg6luVkA9U1VUO4EN4ndHF0c1iY8KV1yiE-F68OEUbbbe289PbFHIkgsOfd8XAYp-hnz_RM8U8ehhPtpCQeezEjP7AwHagBbSMVkV0GRoRYI0dvl2UnZ4zODmxdi8o0SIpYkB5bWskN2x2Aq5HJWCMedU4Bp2cLmIJ2zvwQXo2ZC5Mf5fNgRPr-eQ6ZTTS2SMYWAfGpmC7L4Ixa59iJdxRsxizmDW-SZlkKEUP4NYFrvv2YNwDljZ5wDTehtVStmjOpPn7HBsTWKWTFCq5I_BKtZPlacNpUOakJNpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117dd53865.mp4?token=Xy5uOp-jCPmho2EbUXImQunrD5-Kl2zdbHhaWH24z6SOT7Gtgg6luVkA9U1VUO4EN4ndHF0c1iY8KV1yiE-F68OEUbbbe289PbFHIkgsOfd8XAYp-hnz_RM8U8ehhPtpCQeezEjP7AwHagBbSMVkV0GRoRYI0dvl2UnZ4zODmxdi8o0SIpYkB5bWskN2x2Aq5HJWCMedU4Bp2cLmIJ2zvwQXo2ZC5Mf5fNgRPr-eQ6ZTTS2SMYWAfGpmC7L4Ixa59iJdxRsxizmDW-SZlkKEUP4NYFrvv2YNwDljZ5wDTehtVStmjOpPn7HBsTWKWTFCq5I_BKtZPlacNpUOakJNpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بال‌های سنجاقک؛ شبیه شیشه‌های رنگی ارسی‌های قدیمی
🦋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/694254" target="_blank">📅 16:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694253">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
هدف قرار گرفتن سه نفتکش در تنگه هرمز در روز گذشته
سازمان عملیات تجارت دریایی انگلیس:
🔹
شمار نفتکش‌های هدف حمله در تنگه هرمز در روز ۲۹ سپتامبر به سه فروند رسیده است و هر سه نفتکش با پرتابه‌های ناشناس هدف قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694253" target="_blank">📅 16:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694252">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
چه کسی دستور رئیس‌جمهور را زمین گذاشت؟ طلب ۴ میلیارد یورویی بخش خصوصی روی هوا
🔹
حدود ۹ ماه است که ۴.۰۷ میلیارد یورو از مطالبات ارزی بخش خصوصی پرداخت نشده؛ این در حالی است که رئیس‌جمهور سه ماه پیش بر تسویه سریع این مطالبات تأکید کرده بود.
🔹
تداوم این وضعیت می‌تواند توان بخش خصوصی برای واردات، تأمین مواد اولیه و کالاهای اساسی را کاهش دهد و زنجیره تأمین کشور را تحت فشار قرار دهد.
🔹
حالا پرسش این است: چرا با گذشت سه ماه، دستور رئیس‌جمهور هنوز اجرایی نشده است؟
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/694252" target="_blank">📅 16:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694251">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مرکز جوانی جمعیت: ۳۳۴ هزار نفر مشمول کارت امید مادر شدند
رضا سعیدی، رئیس مرکز جوانی جمعیت در
#گفتگو
با خبرفوری:
🔹
تعداد مادران مشمول طرح کارت امید مادر از حدود ۶۲ هزار نفر در مرحله نخست به ۱۳۳ هزار نفر در مرحله دوم، ۱۹۰ هزار نفر در مرحله سوم، ۲۵۷ هزار نفر در مرحله چهارم و در مرحله پنجم به ۳۳۴ هزار نفر رسیده است.
🔹
مجموع اعتبار پرداختی کارت امید مادر تا مرحله چهارم، بیش از هزار و ۳۰۰ میلیارد تومان بوده است.
🔹
در طرح یسنا نیز طی سال‌های ۱۴۰۳ و ۱۴۰۴، تعداد ۲۷۰ هزار و ۶۹۳ مادر باردار از سبد معیشتی این طرح برخوردار شده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694251" target="_blank">📅 16:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694250">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a798cfcc3.mp4?token=qRYmqAZ-R5IpORgYRFs6p9JkvF94KOWFW6eJxJGQ2ba1Zjrph03L61P9cZ7f6Y5eGHT2JbR56TNWniCMIk-9IpqJdAfcsEm7RQ8E1FXuqyJLlv5opT9P75uAOW5O3kdn4wEiB_YQApSsOmjVTxr-4EVDj0kPztnGuVG1Fp3QNBu5Z3RZMV_heo9807ZqBof1jBy1b_teVRmHuJ9Nl1lTYxBhkZZDfR_nDdt5I6aapyS9bGO1fEjbfTr4xS2Lzjb4l0N71vU14XHVhAJV1V_vFzLMiTnIkUnVd9_I7dAWA85PazJeHEF2bCyIk1Z1zZ9DcMxOcR_qDxcbZj55B3hO74FlmRc60ca11avgf7F5Ms3xQ7BOUTGSW9VUyCEJmLLZwYGrrgUjMYXHJ9XwupoUUeOmUcxIcZLTvdcwmpZBZCmMlripplqnVDmkFWcDeMXpKewXSqpM-4Y1LszDoy_6fa8zLBid3h2YgNXE_vTzU5qLMiMbVP-GlWIgB5ECFq1iZnuw2wr-6hchShwl-SLEp3_4Gx7MY7qVAPJ_Nfx9oweL5Rn_WwEqlUjknx4bWzwveG1W3_GNNmGiTCkiaXfGkzlYUfNiY9u4s4AJhNh1l9TfXcVzHj8ExwrSECQCYZXAv740NkixpQ57iUb2JXhrFKZg5CPRE0KBUDOu8SJdXp4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a798cfcc3.mp4?token=qRYmqAZ-R5IpORgYRFs6p9JkvF94KOWFW6eJxJGQ2ba1Zjrph03L61P9cZ7f6Y5eGHT2JbR56TNWniCMIk-9IpqJdAfcsEm7RQ8E1FXuqyJLlv5opT9P75uAOW5O3kdn4wEiB_YQApSsOmjVTxr-4EVDj0kPztnGuVG1Fp3QNBu5Z3RZMV_heo9807ZqBof1jBy1b_teVRmHuJ9Nl1lTYxBhkZZDfR_nDdt5I6aapyS9bGO1fEjbfTr4xS2Lzjb4l0N71vU14XHVhAJV1V_vFzLMiTnIkUnVd9_I7dAWA85PazJeHEF2bCyIk1Z1zZ9DcMxOcR_qDxcbZj55B3hO74FlmRc60ca11avgf7F5Ms3xQ7BOUTGSW9VUyCEJmLLZwYGrrgUjMYXHJ9XwupoUUeOmUcxIcZLTvdcwmpZBZCmMlripplqnVDmkFWcDeMXpKewXSqpM-4Y1LszDoy_6fa8zLBid3h2YgNXE_vTzU5qLMiMbVP-GlWIgB5ECFq1iZnuw2wr-6hchShwl-SLEp3_4Gx7MY7qVAPJ_Nfx9oweL5Rn_WwEqlUjknx4bWzwveG1W3_GNNmGiTCkiaXfGkzlYUfNiY9u4s4AJhNh1l9TfXcVzHj8ExwrSECQCYZXAv740NkixpQ57iUb2JXhrFKZg5CPRE0KBUDOu8SJdXp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو هم همیشه برات سوال بوده که اون سوراخ ریز روی گوشی‌ها چیه؟ #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/694250" target="_blank">📅 16:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694249">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN7Xswxo-wTPxTpIMN2yeGxDKak7OEqXar7isKe8F2-Y0mX1scDYy3Ss3rAERjTPkmTXY6tT89sc-BcWRGZ-U2hruvwsp5w-VdNjXBQMgmaqNri8rAZGCaucYXSdINwpcXbZKYWuVjj4C8f-zfl87FQv5ocvRNSU7PMSy7eLtlv9kh6B0aVS1Z20FmnXzT2swqSQYc1ZwosEPkMFkNYW_N5ICsbjiVeFOTvsKBoTjmDD6wqyhkxxOQ67-QIuE0x5qYMiyAjHPJ_yD2nMjgGHW3kQpInblrgUQMgCGzkLyhFd3emiW7aILOwgZPxOFDhQ9dPR1OoQQ24da7Yi6FdUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی وارد ایران شد
🔹
بیژن مرتضوی با انتشار لایوی در صفحه اینستاگرام خود و در فرودگاه امام خمینی، خبر از بازگشتش به ایران داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/694249" target="_blank">📅 16:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694248">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMilli | کانال رسمی میلی🟡</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDDl3bjKg7xmoi7xrxUpkfOyd7TYDZzErD_DB3uKNPJBnm1-vIR4PC4If0eyeoGNSScSdMzpT2Wyq4FNAAgpzTs_WZSwGVJ8M6aO158Qw-Krhv88OM7vOFLSGLlQ8ZsbaERtcAQED9diruIWOobnqhLZUz7bavRAtTEEuxr2mBDhr0qqOMKmgfs5DvGFyz1320-fkqXjzoWVpUVaKepY9lVn5uMS6jYRRHKNxKsATM51EGYYoKMMEirBL01m2FwzI-PZanLVdUkpFHwHUkyLetx3kRrRO7pDy-7s9ettS_LIuX1U9RvqUu2gcnO7WaLnxhn-U2OQJUU-Zd7bpH5SmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پیگیری‌های میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد
خدمت تسویه و تحویل که به علت مسدودی دارایی‌های میلی در بانک کارگشایی مختل شده بود، فردا عصر پس از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت.
همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
🟡
میلی؛ اپلیکیشن خرید، فروش و پس‌انداز طلا</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/694248" target="_blank">📅 16:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694247">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkO_J0yLjx76yrxa_Ln8117aRuSPjIfLkKOvnxQ8KkUzvAKzQa-q7DiETBHuo6GIToXq_xIiZcLmN7P1bekxUw4BY-4hyxFzS7vk-bKYNX5qDBsshsRbdgwQhfjV5tm0sTszioX0Mq4H_tyIBHnSlluq5sjkxoFH3VjdxjPETGZISehB-4f0LRJsr-fKHAwXeJOIjzT-q7zlxZ1JOht96GMxsr6azIUCyDkWwJ1v4oMVE0f8ltOamkcVK-TRTEfO60f1hYplF8Hwa7CPK3-JQb6FVlQ30VM1HiQIbZD47UcER9A13RzVaOq-vN9rch6IUV2RJulyGz1NbNQXs1nIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بوئینگ ۷۳۷ کاسپین همچنان در استانبول توقیف است؛ میراث پرهزینه مدیرعامل سابق کاسپین
🔹
توقیف این هواپیما به بدهی ۱.۹ میلیون یورویی بازمی‌گردد که از سال‌های مدیریت مدیرعامل سابق کاسپین، باقی مانده و به‌دلیل تأخیر در پرداخت، ۱.۲ میلیون یورو جریمه دیرکرد نیز به آن اضافه شده است؛ یعنی پرونده‌ای که با تعیین‌تکلیف به‌موقع می‌توانست بسته شود، امروز به بحرانی چندمیلیون یورویی تبدیل شده است.
🔹
سؤال جدی اینجاست که مدیریت وقت چگونه اجازه داده چنین بدهی سنگینی سال‌ها بدون تسویه باقی بماند و جریمه‌ای نزدیک به اصل بدهی روی دست شرکت گذاشته شود؟ پول‌های کاسپین در دوره مدیریت مدیرعامل سابق کجا هزینه شده که تعهد ۱.۹ میلیون یورویی پرداخت نشده و امروز شرکت باید هزینه چندبرابری آن را بپردازد؟
🔹
نتیجه این مدیریت امروز مقابل چشم همه است؛ بوئینگ ۷۳۷ کاسپین در یک فرودگاه خارجی توقیف شده و اعتبار شرکت و هوانوردی ایران بابت بدهی‌های سال‌های گذشته زیر سؤال رفته است؛ آن هم در شرایط حساسی که رسانه‌های معاند و دشمنان کشور منتظر کوچک‌ترین حاشیه علیه ایران هستند.
🔹
مدیرعامل سابق باید صریح پاسخ دهد چرا این بدهی در دوران مدیریتش تعیین‌تکلیف نشد و چگونه ۱.۹ میلیون یورو بدهی با ۱.۲ میلیون یورو جریمه به چنین آبروریزی پرهزینه‌ای ختم شد. مدیرعامل می‌تواند از شرکت برود، اما مسئولیت تصمیمات و بدهی‌های برجای‌مانده از دوره مدیریتش با رفتن او پاک نمی‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/694247" target="_blank">📅 15:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694246">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
مصرف ۴۷۸ هزار کیلومتر رول کاغذی کارتخوان‌ها در یک سال!
🔹
هزینه مصرف رول‌های کاغذی در سال ۱۴۰۴ به حدود هزار میلیارد تومان رسید، رقمی که پشت آن، نزدیک به ۳۰ میلیون رول کاغذ قرار دارد.
🔹
با توجه به اینکه هر بسته ۱۰ عددی رول کاغذ ۳۱۰ هزار تومان قیمت دارد و طول هر رول ۱۶ متر است، در مجموع حدود ۴۷۸ میلیون متر کاغذ مصرف شده است.
🔹
این عدد وقتی عجیب‌تر می‌شود که بدانیم طول کاغذهای مصرف‌ شده معادل حدود ۱۲ بار چرخیدن به دور کره زمین است!/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/694246" target="_blank">📅 15:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694245">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
استفاده از کارت آزاد جایگاه‌ها با رمز ۱۱۱۱ متوقف شده و متقاضیان باید از طریق کارت بانکی احراز هویت و رمز یک‌بارمصرف دریافت کنند
🔹
این تغییر فعلاً فقط در جایگاه‌های مشمول طرح شناسه‌دارشدن اجرا می‌شود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/694245" target="_blank">📅 15:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694244">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47c83f0bd2.mp4?token=E8neGbn3F54Pnj1jQyXb4Fz1StN4lq2w3DYi0ymI9Bz-dwj43nLUucLN9bzEcTVJ84NyZEBVP7HOkn7sb1_v9kUbcfaINFXeK8Qg7mzUHBxSdRZ5pcSDqTMThu7thbF9bBMUu5rOcwA6li0sj1vf6Tn5TfICi-RDdy_caLRPIYxoMKvheiVfHLUgc7M640gjlYNpbZB8juUQq5u9EBeRCIvRsvVP0-K9GD6_gsTZ9JZZTZKCyVicXTkRWO_sT4a9T2kd1r7TE4guoPSleM0T7XNZKrgIvkNBPFahg033dpdESBlzXVEGnBQVNCPDQQ7kIwoeX3-5_E5Rq5zWt5UD8CrtJ372CucLZ6ojDi2pb4WUn1VVaKc8sbsNE5CCcT3VgP33jBJ6kt_3ZdhTeSFsTCbish7zj2ReGrJf7pVYR3JBb-hFSN15VT4ba-55SHjvjL_XCrm2NrKIXWWIdjolUVkFZ_8JP9j_bD6-nzlkBc1M8gDG0p1CtlDPbV5D2hsZUwf7DXlqjSqCTSRhEe8MYp5CGHGUSXw9P3sqttondajMD5RrVnmRSaMAgpsqaykvGqSMWlf6lypPHsnxZdunGNOo6FeYistxwg1C_aa679J5qJnAFbpifG9pryWubhvUSO8ZlGnVNwKLDaQHVakvmNRuFOV7wJp8xqNSNs3eRn8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47c83f0bd2.mp4?token=E8neGbn3F54Pnj1jQyXb4Fz1StN4lq2w3DYi0ymI9Bz-dwj43nLUucLN9bzEcTVJ84NyZEBVP7HOkn7sb1_v9kUbcfaINFXeK8Qg7mzUHBxSdRZ5pcSDqTMThu7thbF9bBMUu5rOcwA6li0sj1vf6Tn5TfICi-RDdy_caLRPIYxoMKvheiVfHLUgc7M640gjlYNpbZB8juUQq5u9EBeRCIvRsvVP0-K9GD6_gsTZ9JZZTZKCyVicXTkRWO_sT4a9T2kd1r7TE4guoPSleM0T7XNZKrgIvkNBPFahg033dpdESBlzXVEGnBQVNCPDQQ7kIwoeX3-5_E5Rq5zWt5UD8CrtJ372CucLZ6ojDi2pb4WUn1VVaKc8sbsNE5CCcT3VgP33jBJ6kt_3ZdhTeSFsTCbish7zj2ReGrJf7pVYR3JBb-hFSN15VT4ba-55SHjvjL_XCrm2NrKIXWWIdjolUVkFZ_8JP9j_bD6-nzlkBc1M8gDG0p1CtlDPbV5D2hsZUwf7DXlqjSqCTSRhEe8MYp5CGHGUSXw9P3sqttondajMD5RrVnmRSaMAgpsqaykvGqSMWlf6lypPHsnxZdunGNOo6FeYistxwg1C_aa679J5qJnAFbpifG9pryWubhvUSO8ZlGnVNwKLDaQHVakvmNRuFOV7wJp8xqNSNs3eRn8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شناگر‌ها در مقابل بدنساز‌ها؛ کدام سالم‌تر است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/694244" target="_blank">📅 15:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694243">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تهدید روسیه به حمله اتمی!
🔹
روسیه هشدار داد که هرگونه تلاش انگلیس یا ناتو برای محاصره منطقه کالینینگراد، با واکنشی با استفاده از تمام ابزارها، از جمله تسلیحات هسته‌ای مواجه خواهد شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/694243" target="_blank">📅 15:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694241">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عجیب‌ترین وسیله حمل و نقل دنیا
🔹
فونیکولار نوعی حمل‌ونقل ریلی کابلی است که برای جابه‌جایی مسافر در مسیرهای بسیار شیب‌دار استفاده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/694241" target="_blank">📅 15:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694240">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlPsCBU_VqABofE1YLm9B6H1NyR0MxgywnYBvBgR7-OC9Y9Bh-SvF2u1-xhPLZ4WrBoet9gppcbBnqj0WnGBm7ioHlmy9fSOP22ljQwyQvi3e3QEEtnRKpgRGWd1y4hrcPkxie98xWU8lL578cQrsLO4y5Oqnbx2pRKmXNrDktflJf2RAAzVMFLfUbdvsX_dVe4eGfV68pD-73gKZrqbtkdthwZaSZ66es9uESDRp2nvb8XZC8RuAXptp9CwtZzc32bBtkc7XVgJbhvHB55KOGzgsPpdwTI3jgjdFcQGlOyXd04siwnu4oIfGGvTQkmxsjhq0mo8gId3VuLYNRBs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاصله تولد هر نوزاد در کشورهای خاورمیانه
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/694240" target="_blank">📅 15:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694239">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
دقایقی قبل گزارشی درباره صدای انفجار ناشی از شی صوتی در محدوده حوالی کلانتری ۱۹ واقع در خیابان جمهوری زاهدان دریافت شد
🔹
بررسی‌ها برای مشخص شدن منشأ و علت صدای شنیده‌شده ادامه دارد./ فارس  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/694239" target="_blank">📅 15:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694238">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evH1phC2NVTdEA5AregRQtzPDbCeH6Zeh8xJ9wMIHrynTpwe5hkxP9wRrSWbgHNje568Y3NlfrGBRHhdU9iVpbILIcTvG0prc7XdJSPOVsqK8k6h0YeYBWRpjyPhLVCKRUd5Tn35LWG5opA5L4mbv5Sx_-QghUcNgaK2jq7WwpBBsFIKIt2-jYOPNg9C0MAc3pgCRlLfyhHOFWPLhwfDHDRhv5vvnZExGZqrPl7VepmypD8r6NRF4pXxlEJd-TllNSL8GEZIuaQ4RI6YyQ8zRUKdEiRzqxHFRaJAw040X2U9x7kdyzbL9Gj2tfc8jRuDYEtQxlrxcPJKpfielOJDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار عجیب فروش کارت سوخت؛ تا ۱۳ میلیون تومان!
🔹
در آستانه اجرای طرح انتقال سهمیه بنزین به کارت بانکی، برخی افراد کارت سوخت به‌ویژه کارت موتورسیکلت را ۱۲ تا ۱۳ میلیون تومان آگهی می‌کنند.
🔹
خریدوفروش کارت سوخت غیرقانونی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/694238" target="_blank">📅 15:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694237">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
دقایقی قبل گزارشی درباره صدای انفجار ناشی از شی صوتی در محدوده حوالی کلانتری ۱۹ واقع در خیابان جمهوری زاهدان دریافت شد
🔹
بررسی‌ها برای مشخص شدن منشأ و علت صدای شنیده‌شده ادامه دارد./ فارس
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/694237" target="_blank">📅 15:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شگفتی بازار ارز؛ افغانی ۴ هزار تومانی شد!
🔹
قیمت هر واحد افغانی در بازار آزاد امروز، هشتم مهرماه، برای نخستین‌بار به مرز ۴ هزار تومان رسید.
🔹
افغانی سال ۱۴۰۵ را در محدوده ۲ هزار و ۴۵۰ تومان آغاز کرده بود، یعنی در کمتر از شش ماه، قیمت آن حدود ۶۳ درصد بالا رفته است.
🔹
این عدد شاید چند ماه قبل برای بازار ارز ایران عجیب به نظر می‌رسید، اما حالا به واقعیت تبدیل شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/694235" target="_blank">📅 15:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/694234" target="_blank">📅 14:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694232">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1c176dab.mp4?token=fa8VSkUhnlnDa3u_D-qLWh4TgOyi3IUdWE_bBUq0S6gIj8w_M_Ok9FeNWOuv3R_XZAMyJerGl5DeGI1R0a1eM_dPD1aBg2tNynddIjFzJ6Y44KGQ9Qhbgn7Gwy8-U8EvBeimwDjQqQZlteqHPOdMTbZvkmR4bVKy6VN4uUHtWxtZDNs-rhzm7kyLn70A_HjYTRTvRyEPpBcg54kuJ6QRojhqJedJ26n9yDQ_X06x6mAH9Dl7tGY85HGjgZ9LKAtCd1aBy3Fp3heq04KSY43uxfYuZb8RT1dYyvSNfM8W99x9BCTQpdo6rlpHjwnwNb5Etgq7Tp-p23qhgzi5i3XzoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1c176dab.mp4?token=fa8VSkUhnlnDa3u_D-qLWh4TgOyi3IUdWE_bBUq0S6gIj8w_M_Ok9FeNWOuv3R_XZAMyJerGl5DeGI1R0a1eM_dPD1aBg2tNynddIjFzJ6Y44KGQ9Qhbgn7Gwy8-U8EvBeimwDjQqQZlteqHPOdMTbZvkmR4bVKy6VN4uUHtWxtZDNs-rhzm7kyLn70A_HjYTRTvRyEPpBcg54kuJ6QRojhqJedJ26n9yDQ_X06x6mAH9Dl7tGY85HGjgZ9LKAtCd1aBy3Fp3heq04KSY43uxfYuZb8RT1dYyvSNfM8W99x9BCTQpdo6rlpHjwnwNb5Etgq7Tp-p23qhgzi5i3XzoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: شی جین پینگ، رئیس‌جمهور چین، به نظر می‌رسد از ایده جایگزینی نام «نادرست و ناموفق هوش مصنوعی» با نام «دقیق‌تر و معنادارتر ابرهوش» خوشش آمده است #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/694232" target="_blank">📅 14:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4630746a9f.mp4?token=h8A87zN5cEDyEa6VLdRYAHKOmSvwKbApAM9e4sOEd4iMPyTf5DSzdAjA5g3HtoHnrjczGpvZePb01noQwxlVN75_Adsow1i6-n70_gwAerkR_MuoTi_WcM3z5LJ8qTtQgkz5hu37c2jdg1yzm3H-Rl3fDKfOWiAd-iyIIR6wqyPs9isLK9JY2u9mDuPP4N6cAViCGNrMUTLBH-bCprHnHcG1lXdOBz8c-TxeHLSvRXr0YeAe1F3pMmY6B7nznJYXfwEMNgy8WEpSbxS6yhuZ0F8OwA3Xqnt4BZ3ExLtvbGzR0T9aaCQakzgzTIKvKEqUIlKuPaBGjSbF0a9kQcrf4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4630746a9f.mp4?token=h8A87zN5cEDyEa6VLdRYAHKOmSvwKbApAM9e4sOEd4iMPyTf5DSzdAjA5g3HtoHnrjczGpvZePb01noQwxlVN75_Adsow1i6-n70_gwAerkR_MuoTi_WcM3z5LJ8qTtQgkz5hu37c2jdg1yzm3H-Rl3fDKfOWiAd-iyIIR6wqyPs9isLK9JY2u9mDuPP4N6cAViCGNrMUTLBH-bCprHnHcG1lXdOBz8c-TxeHLSvRXr0YeAe1F3pMmY6B7nznJYXfwEMNgy8WEpSbxS6yhuZ0F8OwA3Xqnt4BZ3ExLtvbGzR0T9aaCQakzgzTIKvKEqUIlKuPaBGjSbF0a9kQcrf4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بخشی از اعترافات همتی و نیک‌اندیش، از لیدرهای اغتشاشات خیابان طبرسی مشهد  #اخبار_مشهد در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/694231" target="_blank">📅 14:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694229">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رئیس اتحادیه طلا: به نظر می‌رسد افزایش قیمت‌ها حباب باشد
نادر بذرافشان، رئیس اتحادیه تولیدکنندگان و فروشندگان طلا تهران در
#گفتگو
با خبرفوری:
🔹
با وجود کاهش انس جهانی دلار در روزهای گذشته، عامل اصلی افزایش قیمت‌ها در بازار داخلی، نوسان و افزایش قیمت ارز می‌باشد.
🔹
مردم باید در این مبادلات صبوری کنند و در بازارهای هیجانی، به‌خصوص زمانی که اونس جهانی در حال تغییر و کاهش است، وارد نشوند.
🔹
این حباب ممکن است با مدیریت بانک مرکزی نسبت کنترل قیمت ارز، پیش‌فروش سکه، اخبار سیاسی و عوامل دیگر، کاهش پیدا کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/694229" target="_blank">📅 14:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694228">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
فرودگاه تبوک عربستان: کاپیتان هواپیما و کمک‌خلبان هواپیمای فلای‌دبی‌ مجروح شده و به بیمارستان منتقل شدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/694228" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694227">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxxLt1LQvf3tj8ImWJik97EVfiM20dpWbnJj4nUutMgdLw8aJJ5h-jnaKTZipRugjdGOXTShRIEwIfx2yxoto4SSfcP3ltjPMi24fsntTIWlwvCQdnuKKLjnbvwOZGYHPOaD6qdggkRE07O6AwE1pDSQIMi7JV4tWztCJ_0VunQHBPd1HvBU3n7ir9ydNZ5syRtqLKoFua3OS8LPsIlWlCp92-1dRzMzGps-t1dMlFBhgbD7mK9KkAzTzt9_VPa6br3Xmd0tIEm3qReEG914FgGcswIVhcjliqTw7MY8M6oFIliN7NjVQkEzZWYIGtfwroyZm854M3j-ZsNHpQWeng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ اشتباه رایج که بعد از غذا خوردن نباید انجام بدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/694227" target="_blank">📅 14:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694226">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stHP36ucyWlQniSQ9CyWGj51JtpImT8SDUlfNc05XiyZoUiLnTMBZ5lyDLFucOF4OSxjwIYv4M65denQp_gNml6Ek4mSiUV545d_BDKAHf7Ku4bY7G-nCfvoMQ-fPj43SoOaSjC4dWW95OyGOUqGPwl2l4cEsvG5xSDNyrNybOXE7BlP3dloXK1J7XTXYqZID_M90XdPhCpVdxQYOR_pYcWMOJoW8NeIvrGWVPvvd6iZSg0l4qNuzrg7ySNI1Uq-MfQS5ZTVKqpnwF2pnY4I0t98DRjLpymVh8iRJ27g3A3XczwU_4AxY1rbvf_lCe-pGkULUWgxzVotoC3-Lr4oWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زینب قیصری، نماینده تهران؛ میدری قبل از استیضاح، استعفا دهد
🔹
نماینده تهران در توییتر نوشت؛ توصیه مشفقانه به دولت محترم، استعفای آقای میدری پیش از طرح استیضاح در صحن علنی است؛ ادامه این مسیر و طرح جزئیات استیضاح در صحن، قطعاً به مصلحت دولت نیست.
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/694226" target="_blank">📅 14:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694225">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyFa5aqzdsnGoKvvedTWaTFcVcp2zkcRJO1rbINK4ANeXVp3SRsm5-UAKrdjB68qCcXbwhXJvWgM389fJBlfRSUgapBFKxstRIaXx5ZlNQKSUrxVE-FbKUGbp2MVxuR-x0ezIRyAUNAvc8HUxFeSblnDfk-LZtB_wQFev1tsvaGr73Lj8VYc6JdHcHhpscT6LRHfi-eXfgUh4plAkzty_tQkr01hmYOgAAizHkFXvIDAoEXwjtB1kRr7cTjokdNemqjtrXf8-M8jePn50dmaaitAk3U5WBzt5m4jT729g-bjESWuL062BNc2ZD22hFtTPB6IubxYWGjUgcNsduzKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سامانه ناظر و افزایش اطمینان به بازار طلای آنلاین
🔹
رضا اکبر، قائم‌مقام مدیرعامل طلاسی، در گفت‌وگو با «دنیای اقتصاد» از سازوکار جدید نظارت بر معاملات آنلاین طلا، تحویل فیزیکی و عملکرد طلاسی در شرایط بحرانی گفت.
🔹
به گفته او، «سامانه ناظر» خرید کاربران را پیش از تأیید نهایی با موجودی فیزیکی طلای پلتفرم تطبیق می‌دهد و در صورت نبود پشتوانه کافی، اجازه انجام معامله صادر نمی‌شود.
🔹
طلاسی حدود یک ماه است که به‌صورت داوطلبانه به این سامانه متصل شده و
نخستین پلتفرم‌ فعال در این زیرساخت نظارتی بوده است.
🔹
اکبر همچنین تأکید کرد که در طلاسی، موجودی فیزیکی و معاملات دیجیتال به‌صورت لحظه‌ای رصد می‌شود و کاربران می‌توانند طلای خود را از
۳۰ سوت تا ۱۰۰ گرم
به‌صورت فیزیکی دریافت کنند.
🔹
پشتیبانی ۲۴ ساعته، تحویل فیزیکی طلا و تعهد تسویه حداکثر ظرف
۴۸ ساعت کاری
از دیگر مواردی بود که قائم‌مقام مدیرعامل طلاسی در این گفت‌وگو به آنها اشاره کرد.
🔹
او معتقد است سخت‌گیرانه‌تر شدن نظارت بر بازار طلای آنلاین می‌تواند به افزایش اطمینان کاربران و شفافیت بیشتر این بازار کمک کند.
ادامه مطلب
👇
👇
👇
:
https://donya-e-eqtesad.com/fa/tiny/news-4298495</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/694225" target="_blank">📅 14:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694224">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Unb27G4X0yMWVWkexYkhDCbvRekJwCF60JAM77iG-ro14UZtLNSMmaPqd2grkEqY7rJ7Sxo65T_jbmDBweLxE51IE9cXi77WoC4VHYPrB110g3QU23mPYBA0F-6yWAQSCdRYvcwL2KN7-rM_1r79w3oYtXU2K21ZqLJ_cDXYrtKvo-Un4b4i3Mou8dRsNO26UjCGaT_Oh3U_mtYhybQHUi9mtvdX1haePcxb61yxBoJoxQ6yaq9diCUXADZdFRH6Dh9dmm4i1T7CmW2A8Mtz4tJv8mcpQT8BWmAEkt5gFzWC11Xri9Zjy67hzpusg3mT7WetLx2YYBsXviv5-GaSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بابک زنجانی: این فرد کارمند بانک مرکزی در زندان از من بازجویی میکرد جاسوس موساد بود و روش‌های دور زدن تحریم‌ها رو بدست اورد و با خود برای آن‌ها برد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/694224" target="_blank">📅 14:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694221">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
فرودگاه تبوک عربستان: کاپیتان هواپیما و کمک‌خلبان هواپیمای فلای‌دبی‌ مجروح شده و به بیمارستان منتقل شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/694221" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
پرواز ایران و پاکستان باوجود فشارهای آمریکا همچنان برقرار است
/ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/694220" target="_blank">📅 14:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2882107b28.mp4?token=sfynZhsOv3Iwe4VhlDHvm68t1ogVsRcckblMBx1sfLQaHEadOPQiElkojHyEsnPABtcNmzZ2bj2mK5hk7jC2U-o1xONdSG7XD6VYUnXltTHWBw9YzOhgEtwW35DyRvTTcCTKLLWiqVWSp3nkL-ImST-HQa8tKLipivdFIB1vy_9NcOkwXg9Zh9yhR5QbJbtQ6ps60wG3kNaM1ERTEW-NZEl9Sn3wqrwLtbIF8YFTuWqbYUN1u5LTn-4HVrzW1wU31T29JyuYLLSiyjRQ0bWRmqIqSyxH46bALVAYvtRPZTU2lAT1qyIYs0HzaivE8Ae-zqQNKBqgvjA9UsH4J84gWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2882107b28.mp4?token=sfynZhsOv3Iwe4VhlDHvm68t1ogVsRcckblMBx1sfLQaHEadOPQiElkojHyEsnPABtcNmzZ2bj2mK5hk7jC2U-o1xONdSG7XD6VYUnXltTHWBw9YzOhgEtwW35DyRvTTcCTKLLWiqVWSp3nkL-ImST-HQa8tKLipivdFIB1vy_9NcOkwXg9Zh9yhR5QbJbtQ6ps60wG3kNaM1ERTEW-NZEl9Sn3wqrwLtbIF8YFTuWqbYUN1u5LTn-4HVrzW1wU31T29JyuYLLSiyjRQ0bWRmqIqSyxH46bALVAYvtRPZTU2lAT1qyIYs0HzaivE8Ae-zqQNKBqgvjA9UsH4J84gWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی کاربران فضای مجازی با هواپیمای فلای‌دبی که منجر به لغو پرواز به‌اسرائیل شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/694219" target="_blank">📅 14:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694218">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41eb750efa.mp4?token=STSr6sP-G5i3jAdcWlTNeecjLo1sbcIMIohrnNONQF7a5XvlU05KghdW4YwKrNfLsVJ_Q90Y_yMw-a3r5eVxaWm3wPbGotyDkm9NSQyie7zJaoTC9Lhv6cPN3mLrUwhvpfXdQYjj7RRCkawk9BVUjZn9kxRm8jm6xRk2O076OugNzdMZwtiM2hXQIluD66xlF_6eip8jk2lkM3TDsQB65j2pu4PdQ8PFcViCAyR_WJ36np1M1pC4s9gEUjIatjES7Ll52YEKihwLGVB0ssH6REqAhwukVWlRFV4wwYgeR0SAP-_OXL-1zXinMnI3m4Z0NCoIAOhyVEPmJSU2eF0wFTBsTcQmOeYz8YF0GqrkPP2LtXm4rKCFBV2OnQ7WgDdUL05h5nh6NbkFj4y76k-ihINfpr7jzX7w-_DocgpObEbbi9BfmFrsViS2_e-AiOzY3foaW-DQE2Q_rOJs8lHO9TBXSAAXVAOaWXwP4HRXARKrp0FI1_GWK2z_3GqY_J55Jjs3yUdq3_wU3iEPpfySSSXAx_bu98Vd4S1VFo1MHoukGXzSDBVGYVYrgODIcbIAZsE_ucKz54Lb2xYRQ86pxw9J98TwAQUcdtd63yYNVSbfSDin3rx7nhYl88jlIemKYrMUPLenv1EmaWR2bdwaV8ZdUgg2Kupiu_aPfREdyG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41eb750efa.mp4?token=STSr6sP-G5i3jAdcWlTNeecjLo1sbcIMIohrnNONQF7a5XvlU05KghdW4YwKrNfLsVJ_Q90Y_yMw-a3r5eVxaWm3wPbGotyDkm9NSQyie7zJaoTC9Lhv6cPN3mLrUwhvpfXdQYjj7RRCkawk9BVUjZn9kxRm8jm6xRk2O076OugNzdMZwtiM2hXQIluD66xlF_6eip8jk2lkM3TDsQB65j2pu4PdQ8PFcViCAyR_WJ36np1M1pC4s9gEUjIatjES7Ll52YEKihwLGVB0ssH6REqAhwukVWlRFV4wwYgeR0SAP-_OXL-1zXinMnI3m4Z0NCoIAOhyVEPmJSU2eF0wFTBsTcQmOeYz8YF0GqrkPP2LtXm4rKCFBV2OnQ7WgDdUL05h5nh6NbkFj4y76k-ihINfpr7jzX7w-_DocgpObEbbi9BfmFrsViS2_e-AiOzY3foaW-DQE2Q_rOJs8lHO9TBXSAAXVAOaWXwP4HRXARKrp0FI1_GWK2z_3GqY_J55Jjs3yUdq3_wU3iEPpfySSSXAx_bu98Vd4S1VFo1MHoukGXzSDBVGYVYrgODIcbIAZsE_ucKz54Lb2xYRQ86pxw9J98TwAQUcdtd63yYNVSbfSDin3rx7nhYl88jlIemKYrMUPLenv1EmaWR2bdwaV8ZdUgg2Kupiu_aPfREdyG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معجزه اقتصاد روسیه در دل جنگ و تحریم
🔹
پوریا فتحعلی، کارشناس اقتصادی: در حالی که روسیه با
افزایش هوشمندانه ذخایر ارزی قبل از جنگ و پرهیز از «ارزپاشی» پس از آن،
اقتصاد خود را بیمه کرد، ما در ایران با سیاست‌های تثبیت نرخ ارز، میلیاردها دلار از ذخایر ارزی خود را به باد دادیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/694218" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694215">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1AfKaqGoovVJsnsPkdN4kgXwZ8jeFVVOXucboqqV8xGxnjNf1qTKNSHD9w_88RzbjCajGfigKbec7lv7UND5uBChojNlgPQmwNJGklVV-60LsDQcwfdpMD1VVSafUK2UAzEveF2pJnxEvTXkB4-GOBspY8wR4s9RLpgCWRyNFh8N4Acx_9xbUuyTR7qlg0abSyq07KwP76EQXK3cRobuejp83Y70pDeUk2MnoqWYnw4c-NHe5BBcCAtZd31IMFUAYBf6MovVGu1bEkHX4lYTXYhfjsCDb2OrVukIksNXDo1kTPdGv3nuSrILQuXF49O8gW4mHVOdWRZ-wWw3ilR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار یک فعال اقتصادی درباره خطر تکرار تجربه سقوط شدید قیمت دلار در سال های ۹۷ و ۹۹
🔹
اشاره شاکری به دو برهه ای است که نرخ دلار در بازار به شدت بالا رفت و مردم برای خرید دلار هجوم بردند ولی بعد از ثبت رکوردهای تاریخی قیمت دلار به شدت ریخت و باعث شد بسیاری از مردمی که سرمایه های خود را به دلار تبدیل کرده بودند، متضرر شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/694215" target="_blank">📅 14:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694214">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bfa48ff71.mp4?token=LxHEvkzANBHzVmHwE2XMtxPdjf1JWb_YGCK63ikSzCnDWftnt1h23htmz6s91WI5JLj5ZG_fH1-ZoTXk6dGq94Ldr3BkEdhTHHQJdXP0zO9DVUDFNS5W2ggLOz_52kXnPH1fLL0lF1VG6ZDf_MxPeE85vzMtdjYz6gh1ii1nBxjcNHTpi2lZqPQLZFqrtNPj_7cHMPluRUVac3hf5JzvxZGANoNjczJxbhFVERsdkk41SMCVCsbXSGP0rpKInsvDSysWExALRYbAglq-SxO8OcrotrIXNwXZBJutvgOBW64SicskAB2v8IRYHy2JXCGS01LALGjsEAu5bEBywkG0Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bfa48ff71.mp4?token=LxHEvkzANBHzVmHwE2XMtxPdjf1JWb_YGCK63ikSzCnDWftnt1h23htmz6s91WI5JLj5ZG_fH1-ZoTXk6dGq94Ldr3BkEdhTHHQJdXP0zO9DVUDFNS5W2ggLOz_52kXnPH1fLL0lF1VG6ZDf_MxPeE85vzMtdjYz6gh1ii1nBxjcNHTpi2lZqPQLZFqrtNPj_7cHMPluRUVac3hf5JzvxZGANoNjczJxbhFVERsdkk41SMCVCsbXSGP0rpKInsvDSysWExALRYbAglq-SxO8OcrotrIXNwXZBJutvgOBW64SicskAB2v8IRYHy2JXCGS01LALGjsEAu5bEBywkG0Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی مجلس نمایندگان آمریکا: کنترل مجلس توسط دموکرات‌ها «سناریوی کابوس‌وار» است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/694214" target="_blank">📅 14:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694213">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
عرضه ارز تا سقف ۱۰ هزار دلار برای هر ایرانی
🔹
فرآیند عرضه ارز از امروز آغاز شده و در مرحله نخست یک میلیارد دلار از طریق شعب منتخب بانک‌ها و صرافی‌های بانکی عرضه می‌شود.
🔹
افراد بالای ۱۸ سال با ارائه کارت ملی می‌توانند تا سقف ۱۰ هزار دلار ارز دریافت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/694213" target="_blank">📅 14:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694212">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C84lQDK3UmmPv8QEa-GDQYB1GEkN_-HEJQSzT9sOy5exFVRUJs5zJsmofc4ecFHjbCOoPGCLl5ObxqJgFQ0pdYVjMzoYqCBd75wn2ZtNWa5RoUUgwZnagYsbz9orsxxe2XBJD1OjuBk8MyEMxAAUYjLq-IbnLFz2E3zuIAWAApzVVEDrMJacoCpyd-xFa-XwTmOgpWAOex17Fu8MED1_RjNGwOB1m7-Z8w4EBqW2jqkDCezytIASVcDhwVzvhhZxUq43jhvm5mBgp7rqAjgH0-CMfmnDZBchZbf5kfk44nCOLUzGQAgjxH5uKURMusPhTY9qFDZCMBv0v9Io7ProZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه اماراتی: ایران با میم فیلم «شعله» سازمان ملل را مسخره کرد!
گلف‌نیوز:
🔹
سفارت ایران در هند از یک شخصیت محبوب بالیوود برای حمله به سازمان ملل استفاده کرده و این نهاد جهانی را با دو شخصیت داستانی بسیار متفاوت مقایسه می‌کند.
🔹
در این میم، استرنج، ابرقهرمان مارول، را در کنار تاکور بالدو سینگ، شخصیت نمادینی که سانجیو کومار در فیلم کلاسیک بالیوود شعله محصول ۱۹۷۵ بازی کرد، قرار داد.
برای یکی از این تصویرها عنوان سازمان ملل متحد طبق کتاب‌های مدرسه و برای دیگری سازمان ملل متحد در واقعیت درج شده است.
🔹
مقامات ایرانی از آنچه تهران آن را پاسخ ناکافی سازمان ملل به نقض ادعایی منشور سازمان ملل توسط آمریکا و اسرائیل توصیف می‌کند، انتقاد کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/694212" target="_blank">📅 14:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrjFLantB3_JcDY4iTricWxwGcDgjMVLCy8rv-MsO108mqmNEWy71lnFk07VT6wVvA7wb2aO4KdqC7e_aOsHipj2-dBQ3I-1ueEaFynlIFpKkk05zlWkcxqefY71USRz4M6GdPUiBFfpZce66eXizp2FmjNzO16FMooj9GKxDj3UonFU50wj068LOtMtE9gLb-5iqgVeSY_2QxYRTq5dlNR_SgyvoK8zF5P6U1uaz26iQApmyLtMhKBNVS3P1O96va2a7Ky34G7sXdZROvTQPGNM5uXpFD-ZZs6vXeFbCSonXncJdO_pbo7DiHniwUw8g3RywaIm2Gfz_d5nFHaeRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دستور آزادسازی طلاهای میلی صادر شد/ دادستانی هم پای کار مردم آمد
🔸️
تسویه و تحویل طلاهای مردم در اپلیکیشن میلی با صدور دستور بانک مرکزی برای آزادسازی طلا و رفع توقیف درگاه میلی آغاز شد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/694210" target="_blank">📅 14:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694205">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ew8ICoAiyBrVFm1x415ArMYfRP00CcnUTxidLuHPusI4O1f71xl8yKzr6j92yEtwshtj2TgnyJDWyc2z3YoaQjf1Pladkzzo6ztiug6UkEzR3YI-egtpGsmIx7nRofNTlbG9tE6_C-qqGIKLtKVjaHGzkB7oJ48mXAqwBkyr5dAoNOZdqEPOBlCn_mCznFh_RMlpxV1ZBDqDvaKynfnMQ_CBLtz8gkb3kaDXPG4Uc5sz4fVVHIxmlhoq6IGyVxUBH2RNcm8S_2KLvZaNtqSsI_H2d_egijboIZtuXgVima1KK3G1bYhX-GMRP24cUP1NEIsMvBRGZ1NQ0GDPq_1BYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLc8woVzqfomFrRGp_O2ws8IOAlG5vwhzIeTUHYpICS54zSxo3u44Q3em1Rlw-Dx3ifEvpDBYa6qurXgTtHkh5zq-wa-uEzDaS8-DtrcDA6Wi2pOU81LGjTGf5tWcyCeKjVngh0EXj8Ck8Re0V-6N82QIK5VbM6pNkvdRB90FLsc6fftpSAYmxrhqxK2K_AfP_QZFYLvSR5V-EhFRNuDIyW9bPlKj4yghsNNTenqrXQRw9R5m-MIAYqiogFD5A3brq7hMelBcWBBx38N-iiKjxqoebCjWayXsl5_FonYCzCCQNQOm6R-3Zh2FoKoix0Jjmj59MfCWtFt4iRhx5ty_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBPv822Yw2lZ96UGyWk3Xofqeza2fJwqm9zJ17Ae7MHImOpxCCF9fIep3NMAx_oOvG_vN4kEl4bzRQjNlZx96yVxHPQ_lrgfcOMX8XDW2qxvI5N-p59IbdAgV_K-vUujGy7745ukrvxSwdSIttxIXj4RIOak24dZbpZNthYLA1dOGwcjcdVTeP0iSrXxOhufiGILO4kQ02lGfNMNybZ9nrbpJZsek2YhPLd4WFQPEbdEyaGQTD74l2wnSvW7lg4QP2QDgK-xMOZH9eaB9oCF8Zir4FK4NuPcOcGA1UT3c5bcUId2AIrq7d9kp1Nps9_bMMOXwT3nVg_Dc6kcslWTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5ZEJuBPfVns_QeC1DUC0zbbRtpVOy3MsTErAckaQrQk_EHyFAkFDEsbiLiYyP8tupMUlP9mUM5NW97-edEQqG2KE_Vmsm5HbX6nKZfB1cES4uybDeRTzNshu_LVfEP10ti0eZtrEX6U0N9pHAKC0C9aGqzxae2dc3AmDxNL02L4hbq3H2JMaYxBTZgjpr2zfnWbV_8AEeqoxkxhosqrmZVZTkF4p_8mQTUltlqdQIwwP4SSozYBjTLEnh76Kmd5SZcw4EMEMeJW-tIc5iXSgKV6x6ls2C1C0KatQldrDo-7NOrEc6e_4joHz7RvcjimwwuWRNg4PIADu2tVzBjuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZGEkojkizK7C7nRxIR-g9JU0XAFs1n-rWdjYppGp6zUYF2EjstnZnx57lphzYFdn7M_XzT7y-UYgiGowVg3iFpd-dUjw8itAZkCcIQe1N__eholhNV_Z6lPyWFxPnvg--VuwjATNcABWrBMVWdAYpE5IzQizCBmXL_msAnTg1jroL5KArELWdfcgsiuaRp_qVEM7PxCATDBDT6UtAemWK56tIZqNANEg-cN7cxDxKR1Y36Mf5a8xHNr7BBQKQc2aXvfczWkMAlqeF_KFbm_Qx-8V7hK0NgYuvkhkZgLPu5l1s_5jPt5foQwDiiSY6ciRP2eQ5CHpdwWMYj0z9hzmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کجا سرمایه‌گذاری کنیم تا بازدهی بیشتری داشته باشیم؟
🔹
در شرایط فعلی اقتصاد، سرمایه‌گذاری در کدام بازار می‌تواند بازدهی مناسبی داشته باشد؟
🔹
از کارشناسان اقتصادی مختلف درباره فرصت‌های سرمایه‌گذاری، میزان ریسک بازارها و گزینه‌های پیش‌روی سرمایه‌گذاران پرسیدیم. طلا، بورس، صندوق‌های سرمایه‌گذاری، مسکن و سایر بازارها؛ هر کدام چه چشم‌اندازی دارند؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/694205" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694204">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d3c2cba9.mp4?token=WQzvKuuLKi_4zGPYuw-B0RrRnqXSJwb5GQ2GgqbnbAMOsec-s-Gde1-hJzjPcKS7F0E9SXsfFPJMFTJN1WjqAhn5W4iKsDZHxzvtHcHLnFu0HxpKTcPDCy3fy_m1Y8jMn7WCxDptreeCYh55fw7Sryb6uCf9IoIXibT1ZVBJvjKBn9nFAenLolwdmYh1KfG4vT4LNKjsJjeDCBg0CB-YTPpcv36R05bz8KVAa560EfPZt1j-QxLjO0VPkqgvP8l6dUrt1HrsHovwSZZmPNPTFtaPjt6UgEuFNKTktLN6Y4H4JsZG1jDBT_lIFAheqMn3LU3iUbG1RJt-BY9h4G_W4DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d3c2cba9.mp4?token=WQzvKuuLKi_4zGPYuw-B0RrRnqXSJwb5GQ2GgqbnbAMOsec-s-Gde1-hJzjPcKS7F0E9SXsfFPJMFTJN1WjqAhn5W4iKsDZHxzvtHcHLnFu0HxpKTcPDCy3fy_m1Y8jMn7WCxDptreeCYh55fw7Sryb6uCf9IoIXibT1ZVBJvjKBn9nFAenLolwdmYh1KfG4vT4LNKjsJjeDCBg0CB-YTPpcv36R05bz8KVAa560EfPZt1j-QxLjO0VPkqgvP8l6dUrt1HrsHovwSZZmPNPTFtaPjt6UgEuFNKTktLN6Y4H4JsZG1jDBT_lIFAheqMn3LU3iUbG1RJt-BY9h4G_W4DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یدیعوت آحارانوت: تخمین‌ها حاکی از آن است که حادثه رخ داده در هواپیمای فلای دبی یک اقدام تروریستی بوده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/694204" target="_blank">📅 13:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694203">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
یک پرواز دیگر دبی به تل‌آویو در میانهٔ راه برگشت
🔹
پس‌از وقوع حادثه و فرود اضطراری پرواز دبی به تل‌آویو در عربستان، منابع صهیونیستی گزارش کردند که یک پرواز دیگر از هواپیمایی فلای‌دبی در میانهٔ مسیر دبی به تل‌آویو در حال بازگشت به دبی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/694203" target="_blank">📅 13:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694201">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1675b0d347.mp4?token=Pb67-Ge_nV4sw39QnR_8Zu1_IFZSZCh5UDuJkjM7eRSpuzzSl8NKevGGs9xwVHA8aIziIwqf540wUNZRdA70let03t459pAqW8j7DlskoGNETxeUTWpy3If92mS8EHIQ2VebGEfmpXWYwLEFS9V6fNtAUvtSk6K0KlKxIowacGlioGN3gKXqc4nxQS8bIav1bGi14ffeS8Wv4GRT49fhBNDXdrsqhmx8aWILWa96vbua7dR-sFCBhuZIXrEtxue7JLCFIzjbkZibfZEwyn4YFO4mZYZcE7DpB0QP26t4EMwMoCM9FAy5hPi1A1l4QLQt4SnHnNTuT4h8SDSdjuqy5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1675b0d347.mp4?token=Pb67-Ge_nV4sw39QnR_8Zu1_IFZSZCh5UDuJkjM7eRSpuzzSl8NKevGGs9xwVHA8aIziIwqf540wUNZRdA70let03t459pAqW8j7DlskoGNETxeUTWpy3If92mS8EHIQ2VebGEfmpXWYwLEFS9V6fNtAUvtSk6K0KlKxIowacGlioGN3gKXqc4nxQS8bIav1bGi14ffeS8Wv4GRT49fhBNDXdrsqhmx8aWILWa96vbua7dR-sFCBhuZIXrEtxue7JLCFIzjbkZibfZEwyn4YFO4mZYZcE7DpB0QP26t4EMwMoCM9FAy5hPi1A1l4QLQt4SnHnNTuT4h8SDSdjuqy5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴
هزار متر سقوط آزاد
🔹
این هواپیما در جریان حادثه امروز، از ارتفاع حدود ۴ هزار متری دچار سقوط و افت شدید ارتفاع شد؛ پرواز پس از اعلام وضعیت اضطراری، مسیر خود را تغییر داد و در عربستان سعودی فرود آمد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/694201" target="_blank">📅 13:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694200">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
تصویری که ادعا میشود مربوط به هواپیمای فلای دبی است که آسیب دیده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/694200" target="_blank">📅 13:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694199">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp3pN-bR6u_tMr3ero74RKTrs6_5f_vgUAIMWeYA_QjNBtT6o9YoRO0-Twy-0kJ3Di-ejJYtXLtd5Aa_t3dJgLs91fUz8jAt0Cm16uVHMItfDa_VyMgLqd5UUbEMqMVsSdikFKc2kHNdr_YGjUeHm4fOlLJNmojanSdG-Gl1cWF7axkUUUv58Kw2BLsZXa72HY2CMI_wAqorPqJYiaMOBITNvA97doZjMp1PmNzmL-kgU1nRMRMCH3vAhHPcyULQZ5GsO1TqNBfgucwwf8p3V1gV4-E89R8r5YHH_IniWl7L8X1LvANYAQ206QtZI528IfugWT6J26piSZg1mUVIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیرماه امسال در شهر علی آباد کتول استان گلستان یک پسر ۱۷ ساله با یک نفر درگیر می‌شود و او را به قتل می‌رساند؛ حالا دو روز قبل پدر و مادر این پسر ۱۷ ساله به همراه برادر کوچکترش به خونه مقتول برای گرفتن رضایت می‌روند که آنجا یکی از اقوام مقتول هر سه عضو خانواده قاتل را با شلیک گلوله به قتل می‌رساند
/ ایرنا
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/694199" target="_blank">📅 13:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694198">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbDiY76QUWvPKwDxlVP3unSYzZma0b-EgKPKiIQ9P8kNMOrO8oLOJ3S79XkL8zqsLcHI1jYJGdDVzFidok5upMMtYyny3nUeUR_uHfZ3W7kgbLy6jQQ_9F0J1E95Bj72w8PhbhY1V9soTcqvo6Xc2exl8KwWmuUlWPQRuoewqBlMgpbIypQMZbtpLdYw7UPjzgNyrtVh7Fvsoa4t3YDZYfKJrOQ-m9XcHk5d_GgFDhntt5i_H__pNhof8z7mC_Q12RfgGsgSjm7HD7tiQDfO9OXJMJk92aAJMFHh18n7kG3WxsDQ77IRMtBkVwfV8PgM2pTnJOcVRSKyg1LihzQVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: خلبانی که خلبان دیگر را با چاقو زد و قصد سقوط هواپیما را داشت؛ اصالت عمانی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/694198" target="_blank">📅 13:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694197">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89ee93e5c8.mp4?token=XXmOQ3Y_-lYviJTx-viXST1eAKwajQKv8SC4Dn1s4CVqHOuqRrzqH-RVWOBT516HRzQHHNbto-RxaPPae_MpPRmgwHd0wjVYpWvwkl7VzvZYUwYynFycbbUjmFnAaXjtf3Lwno7vsmAF_C4M0kVR1fXQ-j_xF51kHbvfVGmcMmqC5cVIdPkf0NqUTq2LBt1qciZSIYytY3ICT3EMHucd_zomVVhW6b8CsFJH4hxsRj7ndlEfcrvOpEWbDAGzaIjMrTGDt20h1ZwXhpKDigv0YgMK8gOI3pWhEFVcw7z4AGvj8ziWn_WyrhSPf5F-7fNY6bZtnRSIPKDrV5hfydCCXqLqwfX3td-aSrtBqKwwdRWI3EoscDYuQVpWRCj18sc169aVjdFjBENoPE0ccdjxGLhtItUpGEWqULko6mYi9fqW0JlYRFrWwU3bcd2rjnvUDQ2AmtSOYSVf_vMYqcTVBMesjx4dkUJKShFzoWIyH3O4pCnxzKpDuqIl9xkkfjXRg_ZFHdW3lhHgFcl798UWUmLkgahD2KcePf4mid8QNMRnec2CLOd1O4SfcIJ-Ny4-6CUhGMfImAYGvta3xTk1S6tXHHpGIR5n1LTRhZIQ6paKfJ2ekrEg7zDYBW9t7cqfvqRhRd5A-AnyYdmekoBbYZGyV2pXVl_lWUkXtkB5_70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89ee93e5c8.mp4?token=XXmOQ3Y_-lYviJTx-viXST1eAKwajQKv8SC4Dn1s4CVqHOuqRrzqH-RVWOBT516HRzQHHNbto-RxaPPae_MpPRmgwHd0wjVYpWvwkl7VzvZYUwYynFycbbUjmFnAaXjtf3Lwno7vsmAF_C4M0kVR1fXQ-j_xF51kHbvfVGmcMmqC5cVIdPkf0NqUTq2LBt1qciZSIYytY3ICT3EMHucd_zomVVhW6b8CsFJH4hxsRj7ndlEfcrvOpEWbDAGzaIjMrTGDt20h1ZwXhpKDigv0YgMK8gOI3pWhEFVcw7z4AGvj8ziWn_WyrhSPf5F-7fNY6bZtnRSIPKDrV5hfydCCXqLqwfX3td-aSrtBqKwwdRWI3EoscDYuQVpWRCj18sc169aVjdFjBENoPE0ccdjxGLhtItUpGEWqULko6mYi9fqW0JlYRFrWwU3bcd2rjnvUDQ2AmtSOYSVf_vMYqcTVBMesjx4dkUJKShFzoWIyH3O4pCnxzKpDuqIl9xkkfjXRg_ZFHdW3lhHgFcl798UWUmLkgahD2KcePf4mid8QNMRnec2CLOd1O4SfcIJ-Ny4-6CUhGMfImAYGvta3xTk1S6tXHHpGIR5n1LTRhZIQ6paKfJ2ekrEg7zDYBW9t7cqfvqRhRd5A-AnyYdmekoBbYZGyV2pXVl_lWUkXtkB5_70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پلیس امنیت پایتخت: با افزایش ۲۰ درصدی، ۳۵ درصد درگیری‌های خیابانی تهران متعلق به بانوان شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/694197" target="_blank">📅 13:30 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694196">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
افزایش قیمت برخی خوراکی‌ها در شهریور ۱۴۰۵
🔹
در گروه گوشت، بیشترین افزایش قیمت مربوط به ماهی قزل‌آلا با ۱۳.۹ درصد و کنسرو ماهی تن با ۸.۶ درصد بوده است.
🔹
در گروه لبنیات، تخم‌مرغ و روغن نیز شیر خشک ۹.۳ درصد، خامه پاستوریزه ۴.۷ درصد و کره پاستوریزه ۴.۵ درصد افزایش قیمت داشته‌اند.
🔹
روغن نباتی جامد تنها قلم این گروه بوده که با کاهش ۰.۱ درصدی همراه شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/694196" target="_blank">📅 13:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694195">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34ef18c0f.mp4?token=StAkIbbrtiSk8kLs8f80AprjZi2pZn7UyRfjvT7as-cDmdpH-BOq4k_imi1OB8mgs9pVFXkPv5VZmK73RMe_6hQEJ0NnqPjFY3zUpFK6BVaq4UtVaCRy5Fv6YsDy5PRxsaKMgyKu2ec3WlKsNmo__ytItP8JNJ7IvWxdDHdPORmuwpg0dkVBQ05mz0DaRIdsEmU3EhWmvFffp7_PsSpv4GsUBHkrpS-y1PAKAVV0HMoMV7Ep1J8qWWekkXkxXc1wlaqd6fdVPWVX0JnGELFfdxZp-znDfd2WfSO-zVoUNvqlso5sSnBb70uzsDbVmRiKRwP4q-8yoeCowFJOVmDqnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34ef18c0f.mp4?token=StAkIbbrtiSk8kLs8f80AprjZi2pZn7UyRfjvT7as-cDmdpH-BOq4k_imi1OB8mgs9pVFXkPv5VZmK73RMe_6hQEJ0NnqPjFY3zUpFK6BVaq4UtVaCRy5Fv6YsDy5PRxsaKMgyKu2ec3WlKsNmo__ytItP8JNJ7IvWxdDHdPORmuwpg0dkVBQ05mz0DaRIdsEmU3EhWmvFffp7_PsSpv4GsUBHkrpS-y1PAKAVV0HMoMV7Ep1J8qWWekkXkxXc1wlaqd6fdVPWVX0JnGELFfdxZp-znDfd2WfSO-zVoUNvqlso5sSnBb70uzsDbVmRiKRwP4q-8yoeCowFJOVmDqnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه بعضی از مسافران به علت فروش بیش از ظرفیت هواپیما، توسط یک ایرلاین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/694195" target="_blank">📅 13:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694194">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
افشای سناریوی جدید موساد برای فضاسازی علیه ایران
🔹
بر اساس ادعای منابع امنیتی ایران، اسرائیل قصد دارد با اجرای یک عملیات تروریستی و نسبت‌دادن آن به ایران، زمینه‌ساز موج جدیدی از فشار و اجماع بین‌المللی علیه تهران شود.
🔹
این ادعاها در حالی مطرح می‌شود که طی روزهای اخیر نیز گزارش‌هایی درباره نسبت‌دادن برخی حوادث به ایران منتشر شده است./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/694194" target="_blank">📅 13:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694193">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY4TALK0Bv_0Lm-uyhlJVp2YpbTeKZIf2Gjf4Y8b29aPuIVCWHLr_N2Q2-YY06E4vsm7ynGv4MrhidQkLVJKstj8nB0ouHxYmNpWLWxmbi7cuxbmOt37-Arj0Ut1uIGTwvBDk49dpuO7hVa2SKdOpQdf3I56XaasdSps7cgjdZY4cpZa5OaVX8elPFFrRB4t4S7wAhDPxRSLHYchsRBLEO2ptvxoJsXa9nGmpQ_MkELNq5un43hO70K2ZagYEfhDJGlkKkzyPWbaYa90_AwWcgP7Hc1dnAFnWR8uC8xuYwVxbZW0wPWefbxx-bFL_qDTqFi4qaChzRb4pvdda62NuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشتری مداری در گیلان ۱۰/۱۰
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/694193" target="_blank">📅 13:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694192">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شوک بازار موبایل؛ قیمت نصف گوشی‌ها بالای ۷۵ میلیون تومان است
🔹
بررسی ۱۲۰ مدل گوشی در فروشگاه‌های آنلاین نشان می‌دهد ۷۰ درصد گوشی‌های بازار بالای ۵۰ میلیون تومان قیمت دارند و کمتر از ۷ درصد مدل‌ها زیر ۳۰ میلیون تومان پیدا می‌شوند.
🔹
همچنین نزدیک به نیمی از گوشی‌ها بالای ۷۵ میلیون تومان قیمت‌گذاری شده‌اند. میانگین قیمت گوشی‌ها در یک سال گذشته ۱۳۵ درصد رشد کرده است.
🔹
در میان مدل‌های پرفروش هم گلکسی A17، A07، A16 و A56 سامسونگ بیشترین تقاضا را به خود اختصاص داده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/694192" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694191">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سخنگوی سپاه: در هر ۲۴ ساعت در تنگه هرمز درگیری نظامی وجود دارد اما مدتی است که آمریکا پاسخ نمی‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/694191" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694190">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu39uCC6QtkII10zeRMskuOf9tek0Hf0ofhvXgqLYz5KOgVgJw-oEnDBE1bMXrMlIkpYjlkmA9kZOZcR6YuCYHb0qXTsxMklvIg_CTI5mzldIDLXM8nXHykdo0NlDuNSCoGmew9JA9sIVXd82YBwzEwGFXX9CiY757tB_Ub-8JtwB8NF7MSWfYG5tNxETNxnQVRZcU4LaHoIpsEWixoeaUadU0mEt4EgIZcPmGG3-1qvU7F_WC3AIpP1oAs89v-1YlCD0u_ljYn_v-l1WkJeUvUedleipgIJSzWLyKPVal6-ayTQoA26yHNjx5vNgtMuy61SPzjvGaRAN0MfDbzlLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی انگلیس: یک منبع موثق گزارش کرد که یک نفتکش در تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناخته قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/694190" target="_blank">📅 13:06 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
