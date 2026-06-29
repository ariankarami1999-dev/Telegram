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
<img src="https://cdn4.telesco.pe/file/GqPjsC8fnTI1h9DSArFKyY88nYzUyyqvjWsQ9SxBq437Fzqp6aUmPkOzzCCvCjBeI9U-uXU46NGm5xnS74JDk9LkePyhw7gqtSqVaQUyilEEjGwGvnwlM76e6qplViV5nMBE-raX6lXOYOamZqtTgQbb90ofL95WAgHHk8SKvE0D-2VxYbHqWln6CXD-YFQl9kqn318MwjgNS-EqBsXp0PCivfHOEZF7Eay7rTI_77WzYe7_Z4r0oCop7Ewxw20CGSCH3GSUe0x4uXQts37EeIFxRWEc-HQcPgaK9I7K1hIcS5f_WczzseyajQklgbf5zvz1s9kjF3JwrlzTECDrXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 218K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 00:35:10</div>
<hr>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=ao3Q96S8gPg6ZLJqZrhvlMVBt8oWWFs9RkY017XfhAv5gzvo3ZLP18KrsQbI_LvI5VKi-WJi0Y8ZHoycjWYnZbLPB6ioMmSiiIBW45-uX68Z2s8-6fROqTV7eVOcxuV9wmXRuHZp9Xcn56p9ezdbIqURyJg9-Y5gIXkryJL1YMgqzcmHD82d_QoN1uzkQM8_y16751px-jU8WqmErKAlVSN8EFmK85lxhc8LJck41382o0buP5ok0SnMsfZFLC7PscpaDZEXDOpN7qHMZfA1LDfNIiUmFUj2AF2n5JHmNaPkhJYRJ-bETh0Uku3hk_yRQJPyvOzioT5_bjJzYl2rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=ao3Q96S8gPg6ZLJqZrhvlMVBt8oWWFs9RkY017XfhAv5gzvo3ZLP18KrsQbI_LvI5VKi-WJi0Y8ZHoycjWYnZbLPB6ioMmSiiIBW45-uX68Z2s8-6fROqTV7eVOcxuV9wmXRuHZp9Xcn56p9ezdbIqURyJg9-Y5gIXkryJL1YMgqzcmHD82d_QoN1uzkQM8_y16751px-jU8WqmErKAlVSN8EFmK85lxhc8LJck41382o0buP5ok0SnMsfZFLC7PscpaDZEXDOpN7qHMZfA1LDfNIiUmFUj2AF2n5JHmNaPkhJYRJ-bETh0Uku3hk_yRQJPyvOzioT5_bjJzYl2rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=JKzAjanDdNl2xJcvfvXyjFLMPYYukr9HY3FPW3eWiCEfiW8wmXORPAOm-sSn8QiKYSO8Z-S65RGagixxD8kdTwRBzfWdfrc6qEA28sh4IkA7jclpEUFzw8orCYW7_odXcrZzbNb6YAr7gBQSafxICeWJEs_eMRSv_pssDwZtDi-NkPB76EarRj7e7_1KGmzXXaz-zGkGNPbsVt0IWfHVRexOQnZM382tGelFwFoUIHToh-aflzVTxIhCr5dE1ehHQo3KJ8wXzLFe3eUjwSSWIFHiz_cO9OiOgMqMaCsEe8DxwhO-tIu1ahvEQdR2-vt7hQ9pZ9dohNuYFVjpQNKtSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=JKzAjanDdNl2xJcvfvXyjFLMPYYukr9HY3FPW3eWiCEfiW8wmXORPAOm-sSn8QiKYSO8Z-S65RGagixxD8kdTwRBzfWdfrc6qEA28sh4IkA7jclpEUFzw8orCYW7_odXcrZzbNb6YAr7gBQSafxICeWJEs_eMRSv_pssDwZtDi-NkPB76EarRj7e7_1KGmzXXaz-zGkGNPbsVt0IWfHVRexOQnZM382tGelFwFoUIHToh-aflzVTxIhCr5dE1ehHQo3KJ8wXzLFe3eUjwSSWIFHiz_cO9OiOgMqMaCsEe8DxwhO-tIu1ahvEQdR2-vt7hQ9pZ9dohNuYFVjpQNKtSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=WsSVg9SGkGh6OyCr3hlsChZ9wWfjJ_O30djDa0tFNXzt0P2dt3J1wRYAOuELt5TC55qtg_qxS7NEbeSl9JKn3jqJpoBRPnaH9bNiY6cYdUBtNTvTRNxdrlWIjF6vhimfAHtkbyyIuF7DiC8FzXa6bHaAKHPxb8aYFLPnyEUFWxDaSlukRsbxRRyzWRXrxtbka1LxAdhUM0G3XYIUPHbRezEUG1nxdUrFe7vM57Uso19cz6aK3kghHLj4kz15Ogk4KscPgX_rI1Ue8QcZxyfe-iOYpioqn0pmrRDn9W3hbIouOlG3piiXFJymzcSWDAQSMN8pUYk-T54FikFgnIhpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=WsSVg9SGkGh6OyCr3hlsChZ9wWfjJ_O30djDa0tFNXzt0P2dt3J1wRYAOuELt5TC55qtg_qxS7NEbeSl9JKn3jqJpoBRPnaH9bNiY6cYdUBtNTvTRNxdrlWIjF6vhimfAHtkbyyIuF7DiC8FzXa6bHaAKHPxb8aYFLPnyEUFWxDaSlukRsbxRRyzWRXrxtbka1LxAdhUM0G3XYIUPHbRezEUG1nxdUrFe7vM57Uso19cz6aK3kghHLj4kz15Ogk4KscPgX_rI1Ue8QcZxyfe-iOYpioqn0pmrRDn9W3hbIouOlG3piiXFJymzcSWDAQSMN8pUYk-T54FikFgnIhpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCite34rmVbWDL0teE1VDERgz6RvYHFaL5IZ_ZCZRDvrLc8PUlxQ3TnfWU85txWMquADBn-fil4vsPAmdef9fCGQ4OYOX4fqoi8JcKpnONihCj17jGAAh38cv6tuD-VgBoqA0S1B9EzfO_spbrCoPnqKjx4DFhPlZoqr9-w22QGQslRM9NRfVKBiZ5_3e0slCZ8RBi71KhKisot0yzFxDnvgB__cJgb7MQ-wbrLyOO6pPObm1qfUEHX2nV3sb70pTCscbZAVM5dp69_ABU5mWwO522_nb_mhzBpYCpyhn3z960KU8p9KQQ7ANxnvpSWLFLEdIOwIe8dc1LcGZczyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=W9K0aaYzXKkogDC09EjsQrHW--IFmjI_o48cJxhPaSd641tXIisW2oAvqK9TXl0Ue4aS7MScn-ZLeVpPVubM22a6jWmcGUZN143JyTNaipCwMjd5AyEwVFDA770k4P_t_pZR71FtWSxh_avclzi4r_b3lrJbIBZ6rw632lLN3ZsrvQ0LJPUPFUV0dFQP3QbHaCBgFMPjZLQN_SRhuHaXwq3Dm2Y8DQfTqFFjFSIpwUZLPmi_y24hsrHWLXbqLtTctZeH3MC2_uvX5lgZe4fCCpGCTLZ0xAYPPf07J_0apBjqrVNfo7rWyQcm4bKu27mjrmOMlQQifpvNDsWaBo4v8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=W9K0aaYzXKkogDC09EjsQrHW--IFmjI_o48cJxhPaSd641tXIisW2oAvqK9TXl0Ue4aS7MScn-ZLeVpPVubM22a6jWmcGUZN143JyTNaipCwMjd5AyEwVFDA770k4P_t_pZR71FtWSxh_avclzi4r_b3lrJbIBZ6rw632lLN3ZsrvQ0LJPUPFUV0dFQP3QbHaCBgFMPjZLQN_SRhuHaXwq3Dm2Y8DQfTqFFjFSIpwUZLPmi_y24hsrHWLXbqLtTctZeH3MC2_uvX5lgZe4fCCpGCTLZ0xAYPPf07J_0apBjqrVNfo7rWyQcm4bKu27mjrmOMlQQifpvNDsWaBo4v8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kC_qbp_ehhZLKouky5yBMjqgqFbbPuC9QpgUYObg-JPm3C-GNvdNtAWCLw7g6BavAdS58gs0ZTV9dKW3Y6viVzY_ncD_p8TkqrtTPwmXJEy3sBozLcDS7EmOJpukd083i94iHbJzTytA7OFHVPv6p6EDbFiRWGoBavDYsue6UqvG70tls0qHCKsiSQ-qBEWcGLRGvCe6KlNYZ5cTCDUXE011x_ZLsm4GZg9Uj90YSx554UV__5GrJxpLc5Jy7Hw0u9j49FRE8siBdGvssMTf1Ec8-tV74z0G0NS1QoG3q3-iRmDm_XQKruTrIzWBrf94fyUCa_HAi9fz_clbJCDI4EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kC_qbp_ehhZLKouky5yBMjqgqFbbPuC9QpgUYObg-JPm3C-GNvdNtAWCLw7g6BavAdS58gs0ZTV9dKW3Y6viVzY_ncD_p8TkqrtTPwmXJEy3sBozLcDS7EmOJpukd083i94iHbJzTytA7OFHVPv6p6EDbFiRWGoBavDYsue6UqvG70tls0qHCKsiSQ-qBEWcGLRGvCe6KlNYZ5cTCDUXE011x_ZLsm4GZg9Uj90YSx554UV__5GrJxpLc5Jy7Hw0u9j49FRE8siBdGvssMTf1Ec8-tV74z0G0NS1QoG3q3-iRmDm_XQKruTrIzWBrf94fyUCa_HAi9fz_clbJCDI4EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZQ1Eu_c7uc0qLfFMRBbg_5EnQUhrhw6-mQB_l0sK15qH0JL6lHrNRyxFmQvt_emo0xCYYusi2_fpbfg4CgJgXYfRVEN2siVv-C5AY3--xrRVvP_s6600S2jm2fe3zI54HseA-XDr-VcRySrRhPm4IaXZm5ryRsJwfxGu0qXLFWc2qKj_H6yRnX9RkASK3xDszs0mWoRtcqTcBGTizmlki6Tgm1fmGHKbYDrTeUPGPkrXFktyo-t-GrvyiLR4uTnnd582eYoni7OKwPqBQpcOFE5Kcj6wD5ORbhhnbdb23miYvCmn9M7YCwH_QvmKUAmnPuI3UX3_7aaBW08PlbXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Pp5CvmChm2_VFJ5bi61zJSdsWFw_bFPJwiK8WO3inktA2wqBbQc6B8h5Im-KmCfkcjIGvbSEfBT-gr5s3UCLM8OUos5F52Q6sHOA-d2eERkbzBbkslekOqxnpssrioj1ygXKFc20rMvfVEyrbGkn0yDRjyhSEt2ifcJR3rny3JdU_zig-ZWAwRc8m4--sFtT-zKBBvo-wntYrK_c00spE7oE_pIPM2z6RLL-l0iBsOwhLy-_fqZ3bdL3b5WDNnVa6A6Uj0JCnsg_4dpei9CHW0zssFemDybPGG-3j4hR34_kAwuHKaDA4kn-Qb-T-i8lA3XO4Ibt8-IKUWG33R8NRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Pp5CvmChm2_VFJ5bi61zJSdsWFw_bFPJwiK8WO3inktA2wqBbQc6B8h5Im-KmCfkcjIGvbSEfBT-gr5s3UCLM8OUos5F52Q6sHOA-d2eERkbzBbkslekOqxnpssrioj1ygXKFc20rMvfVEyrbGkn0yDRjyhSEt2ifcJR3rny3JdU_zig-ZWAwRc8m4--sFtT-zKBBvo-wntYrK_c00spE7oE_pIPM2z6RLL-l0iBsOwhLy-_fqZ3bdL3b5WDNnVa6A6Uj0JCnsg_4dpei9CHW0zssFemDybPGG-3j4hR34_kAwuHKaDA4kn-Qb-T-i8lA3XO4Ibt8-IKUWG33R8NRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4O0MwHF3GmuG9-4-GBdtOHGa-JbZnz8qlhK7Z8IVeniTihw0j4XZSh5CbwRu6fyAO80I025IiwMTXd2Zf0W3XUwKLyQVieLX4khthgrfZRhtmb3XxmEHnK9XD0uPsvmY5bUE5QZLkbhWoWUvZykDtKVoyZz16qzsm-uPDP4DOoQBOxNBwjLHvty-KUCEgJfsWVyEjTkUtk7CcXnwjN32iSJ2t5d-pMe_i-lyYDQaJs4WOaX17dgOLiAPyCJuABhjivEcbCtPukMY9Ngg0Hbv2YnuEp59HVcIvQDz7QdoMeNa7m6H7WDWHdrimgUUtDGTurh45Mb402Lr9ZshrsPeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=sFXhCu7IXspHxMQwXoNuo1GRc6PG-YLrVttlIRN1Xq8iKsb1w7JEUWafom8MfI-eoJ7bN4yobLO4vBpWFheNtxYxey5xC1tPCG12ofLd1MCpPsAm0WdqzwkSHjph3vhVYUSyx3BK2Zi3YYFDKtgCJps2CEbgl2zUDJZ_nxnVvhqbJketFAn83iqu5HgtQqosnZMzlT7KFPgfRHv0oOqnAAF65k7_1Nn4V2WxQvs9mWE_PnLD0Ur6ngLDVKwvTQ5iQgEONLkEye1Yr8PICjeAAJyqzlwJJfwoun-2oiRtMejDvhA-nSb-PhrLAzvbdkl96Qow8v_egxDAv4bz217Bb4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=sFXhCu7IXspHxMQwXoNuo1GRc6PG-YLrVttlIRN1Xq8iKsb1w7JEUWafom8MfI-eoJ7bN4yobLO4vBpWFheNtxYxey5xC1tPCG12ofLd1MCpPsAm0WdqzwkSHjph3vhVYUSyx3BK2Zi3YYFDKtgCJps2CEbgl2zUDJZ_nxnVvhqbJketFAn83iqu5HgtQqosnZMzlT7KFPgfRHv0oOqnAAF65k7_1Nn4V2WxQvs9mWE_PnLD0Ur6ngLDVKwvTQ5iQgEONLkEye1Yr8PICjeAAJyqzlwJJfwoun-2oiRtMejDvhA-nSb-PhrLAzvbdkl96Qow8v_egxDAv4bz217Bb4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=aWX1Kd0xnyv_FbRl5uQoj9L_tG9cm21uD42z95tHvzAl-Vb_6aXCSF6bN_OCzCTTsJBGGUMREi0vWUVhTqGJST0zmAFqHTa0Tx3wkFTY9y8Cg030ARykwUz0AQE6tmI63q3B0aMZk0kEMkcYE2CS4IeG-q5T0ocW-VTcO1nVrmUfykqO_8ThCcMAlaZF65o82wxAsrRf5t-1Cf9VcwRQzA4pu7TNGn7tDFe2VykzyB3nNlyJkR5pmla7UrAkAcD07GIwqCo5-MKqYrVc2oeIHUMNxdUnsROnGXXWfAh9ED8d86w25taGpTJngxmHDcCWcdV2Srw3jSm9LrU3cbuevw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=aWX1Kd0xnyv_FbRl5uQoj9L_tG9cm21uD42z95tHvzAl-Vb_6aXCSF6bN_OCzCTTsJBGGUMREi0vWUVhTqGJST0zmAFqHTa0Tx3wkFTY9y8Cg030ARykwUz0AQE6tmI63q3B0aMZk0kEMkcYE2CS4IeG-q5T0ocW-VTcO1nVrmUfykqO_8ThCcMAlaZF65o82wxAsrRf5t-1Cf9VcwRQzA4pu7TNGn7tDFe2VykzyB3nNlyJkR5pmla7UrAkAcD07GIwqCo5-MKqYrVc2oeIHUMNxdUnsROnGXXWfAh9ED8d86w25taGpTJngxmHDcCWcdV2Srw3jSm9LrU3cbuevw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=bLXjwm27Lb33g4glsWa1W-gVxQAJTH0_L1b87zrD_k6eLkXKkB65I1BP9qHho7f5YjbvrluTlm_2oBMoBMWI7aTdeh-5_iwUoelHA4lkglDiYViZ9q2yLLcEfpG0RFwNZZo_R8ySThe1p5KgmcMPW69WFbvGUOc5cen92xyvYVtXLKhCuT8KhJjcNAaWrfpdhepcDTnlAD1eQUcekoVjO2K5wxJ6Y7tGw7vH9CUetYUx-9qDz2MLh2ZWfVnvRhRWsWEKpT7NriYAt-ySaTUqbL2vnO-9Xis5QroEyT_iQkGqhC4nlyFR_ZYDgdJedvJ1ZdSeNZeY6p85gjyT6w7MEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=bLXjwm27Lb33g4glsWa1W-gVxQAJTH0_L1b87zrD_k6eLkXKkB65I1BP9qHho7f5YjbvrluTlm_2oBMoBMWI7aTdeh-5_iwUoelHA4lkglDiYViZ9q2yLLcEfpG0RFwNZZo_R8ySThe1p5KgmcMPW69WFbvGUOc5cen92xyvYVtXLKhCuT8KhJjcNAaWrfpdhepcDTnlAD1eQUcekoVjO2K5wxJ6Y7tGw7vH9CUetYUx-9qDz2MLh2ZWfVnvRhRWsWEKpT7NriYAt-ySaTUqbL2vnO-9Xis5QroEyT_iQkGqhC4nlyFR_ZYDgdJedvJ1ZdSeNZeY6p85gjyT6w7MEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=WaRHR9_-tQ2vSMqAHTQheZJv8VCKZOoG7WIJ8z727-Junb63NJssxAuuPuE3pI5Jtbf8dTG2N4OGQK4j3cnHWjh_YwZ_dX59bHWyHNhhIeUzPOxx9SyMdz7U2oKaB6PyBQupUUz12cdKmNmzLNb04HLwJzgWwT2xMqsnwHu3ysQ-F27bKujQeUpDVeqMMJQKS6i5rMhXvcxLePnxbW2hsjd-alaqYwDojCXWMccBjdJWUyjavfyMrNr1NfcwoIhDjo-7TLLZ5gjs-tBCl5jX0ARZD2sLxXmxcOjH9IZka44j17qUTsHr1Z63aCsVTVlJGR8UufMrrrgSIu5ai4lX8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=WaRHR9_-tQ2vSMqAHTQheZJv8VCKZOoG7WIJ8z727-Junb63NJssxAuuPuE3pI5Jtbf8dTG2N4OGQK4j3cnHWjh_YwZ_dX59bHWyHNhhIeUzPOxx9SyMdz7U2oKaB6PyBQupUUz12cdKmNmzLNb04HLwJzgWwT2xMqsnwHu3ysQ-F27bKujQeUpDVeqMMJQKS6i5rMhXvcxLePnxbW2hsjd-alaqYwDojCXWMccBjdJWUyjavfyMrNr1NfcwoIhDjo-7TLLZ5gjs-tBCl5jX0ARZD2sLxXmxcOjH9IZka44j17qUTsHr1Z63aCsVTVlJGR8UufMrrrgSIu5ai4lX8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=mCAyh6JCj2KwFEC6UdBUN_3VL5cUFjoCnlUNRpgq0M7ylXxdCLWs4IjZW4Sb1oQXt-wOc1_siHZIx5QX0lZgNDera-Ud5Wvi0NNdW1SYbKdgfBowF8FZc5UGnoTfiUDQGmN5GVIpL_5iIQLCoWfyl0_K6CLVojB6mcPq-ymeGKoEwbJksWHR69PmvxYI8UAHLjUtIS52C6pdg38EIvrmMJg-CBH8zmUzymsCRI5cp4QqIDoZZBelz4hDAR9qFkuW-w5OvYiopn_Fy2EZPv65mToRYSqNuIEQdtT35N12Rc4FOP-ZsAPTzAxmatxi2XkXKSxO5R16zhYMDpTm5COMBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=mCAyh6JCj2KwFEC6UdBUN_3VL5cUFjoCnlUNRpgq0M7ylXxdCLWs4IjZW4Sb1oQXt-wOc1_siHZIx5QX0lZgNDera-Ud5Wvi0NNdW1SYbKdgfBowF8FZc5UGnoTfiUDQGmN5GVIpL_5iIQLCoWfyl0_K6CLVojB6mcPq-ymeGKoEwbJksWHR69PmvxYI8UAHLjUtIS52C6pdg38EIvrmMJg-CBH8zmUzymsCRI5cp4QqIDoZZBelz4hDAR9qFkuW-w5OvYiopn_Fy2EZPv65mToRYSqNuIEQdtT35N12Rc4FOP-ZsAPTzAxmatxi2XkXKSxO5R16zhYMDpTm5COMBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=RonKPUjP6T7WmSo-Y-_vXcKSaUCzYbNBPqQ2IDQGYkkxyREgvfjg8Q8Dyeqgk7lGBYwmUVO6GsxhEECO1ZY0vcjUmHslc3Uo56Qv76vYrQP0HmGghIaMSUrQA6qH7lAKPC1boCkk7XNpGfOxSnbCU9hwmVVX3UhQV8aUwEWVDrBMPh0CM8t_Bym8X1dZCdVTMXG3f06-NWLFeeU_kW2pZbipOk8cZ7erf-SrUvp9jVnu9CGE04FzUOgDV0xIk00u41YT0tGeUe8LuI0oD2NP4NvqYr3kefYFCplhXImIBWu52VHjROYi5zZNAA7iSp_RIesG38FnINoqLSFDmKl0Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=RonKPUjP6T7WmSo-Y-_vXcKSaUCzYbNBPqQ2IDQGYkkxyREgvfjg8Q8Dyeqgk7lGBYwmUVO6GsxhEECO1ZY0vcjUmHslc3Uo56Qv76vYrQP0HmGghIaMSUrQA6qH7lAKPC1boCkk7XNpGfOxSnbCU9hwmVVX3UhQV8aUwEWVDrBMPh0CM8t_Bym8X1dZCdVTMXG3f06-NWLFeeU_kW2pZbipOk8cZ7erf-SrUvp9jVnu9CGE04FzUOgDV0xIk00u41YT0tGeUe8LuI0oD2NP4NvqYr3kefYFCplhXImIBWu52VHjROYi5zZNAA7iSp_RIesG38FnINoqLSFDmKl0Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=BPLc6_2ms4X03eDVQCSuygjGXj7orD1K9-MtkQ9dmeGDfV9GHJpypbSD-fkR03ZDRBE4Exp8diOu8yyVjWdia0_E4eyq0Rmmkxhu_DY3Lxp8DxATNCpORYlncQhzTl7q15aZawPtnQ1XNS4eyUcQFiDN5VTMz8JFlgyU06LpjvPEPn0MgmM-W2lgHuygHTYTMOUnETz6GSC66hL3bHjWkpvxf-0bYH-90WsiBNpaXQ9Mjn2eBN-qU0lSkvRbSujgnUQxgzZAQL1PiBAvulpZfedibzY_1cTjrHRi0MMyXNPp2IslDycANZ6r1RN2lpiVoAH79eI-kLutFbozV-Sv4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=BPLc6_2ms4X03eDVQCSuygjGXj7orD1K9-MtkQ9dmeGDfV9GHJpypbSD-fkR03ZDRBE4Exp8diOu8yyVjWdia0_E4eyq0Rmmkxhu_DY3Lxp8DxATNCpORYlncQhzTl7q15aZawPtnQ1XNS4eyUcQFiDN5VTMz8JFlgyU06LpjvPEPn0MgmM-W2lgHuygHTYTMOUnETz6GSC66hL3bHjWkpvxf-0bYH-90WsiBNpaXQ9Mjn2eBN-qU0lSkvRbSujgnUQxgzZAQL1PiBAvulpZfedibzY_1cTjrHRi0MMyXNPp2IslDycANZ6r1RN2lpiVoAH79eI-kLutFbozV-Sv4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcooEuKYzXSrS5sDVJzabcHgqG0EcdBMB-Y_JCg3C8Krzl4HvTlej8Ah9ieEJa-8oYkYj2cwe9VS_IaGO49-r-nz4K81ZWeyNxxzRsI4bGKZ2vSTdmKzKJHBv_FQzj7JjmEThHj4B8z18N_2fR6mQwUKRmorjZIEKs7qPAW9711LLLYqYM5jFfVHOMXzYF8_E0pUF0Evdl8OC9Xh0G2s4Fwpbkt0woRxE_PCNN1oVQ7atZbvwSzWrp8KfVTlqKPOP6VqiZ3gPU5vV7pzGSrFdp5cy2K8AE-xC1BWg6DObrlrBt5X9UtPF1vrGQyGAf_Mxw_U_ZPX4nrEufemfFlhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvAWQOB3BW8T4ymxZPewVht-suAOEY0VhNtFElOrOGmuyOLW9oFxDjeURwGT389U9uOwLHXGOzeXLwnbBPoXk0hf-keFWGD90AByY48T6o7fn7ZL4I3Tf0GugsfZQzmEYGDHrma6_g4a48h2gBgjVhzQEKwtccuQ9BfPby1yNReaHPRg0zE20KVFu_hmGnoXakrdF67izpePXwsTzk4tAqq3ThX6-K_POSrM1YcMgcBnociD21P1UVXl2s_IvzC2IQDhkJZdHp4sajpAbKoayBfcjwOJFxUDyvOyCIkH1MQq6BgYz3qhmpH-wtrHPaV1Sip2-iu4mleR8h6UzhltmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJaClYjKO0L6sz5k2pvSIgqfOHsCTOVkNnj-JoLTJZhvZjy2P5d2xYwcG9i3OIWW4c5f2RX_VGD8BmORvz98SXWn94jClTC2feC8vYYj05rwXFphJislmHEZilDB4SkMyhobI9xbc9MkU3VKeJbQEJqXsTU5SIhiaK98jNdi4zKXI9ECIeartK9DGpVIKIZVKAovMtd3TDFshVBua0Tb6NzI7YXT_-zf-FQUzGFCUlg9S16xMO5PDyRg-7RS5_4QGpUtCzLuAYr5JjdqnLpGU93wQTXNlJ_xEG48-KjJcVy_XJQjF9AarChWrkuKpedwtN3SdBOlmgrJoe3pPk0xOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=h88R8fOVgPkVfkXo6vfzXKq08IPEjefGeQb9BySxn6l9AfnF2ncTmtiI_id9Tc6HyfGN7uRwoiVeYnhR4H2DnxHzR8tov6Y-zcpkrxn_zzP4qgcShSNh1n4dg5sV99yM67rZ4tV-ujC_7smosUVuZtUibHVFGC0DyKR7uEKBy43LqoFQtTz6ebU-SCBzveJsICqzZrcmcrxkmnXZ1I-qbOmxPCUZpxMdusYixaNxQHBGJoMAJAE011KNpn3msdrMFCXdlTThmPzm-9ugZpxmnde_FP-GtdEfcYblGgKgudboXFZkQLEjolLE-nqFQtNsPwEddfoSDg0jEKQmv-bLMxFYg5KrgfqS4D_dl_W8wu08J4rrnsYijEyaSGwRb-MExq-QFbwpG_u5vw-OvFPWo3kE-X97-lgYpVB7iPSEe7sBzoiwvZVV72h6gFPivrE9PVZUb-AVGcMBGDWJVMLnV0qEjyuj6wI5hsqJJUa5gdmOCWiH-HuuH2CSsB6HhjdLc9SDcfsVUPSDisfmJfT8W8bO1NIiTnTKhw8RclnFtejP881QAGm0LSKuMint9arEH-3bQZ2KBUoxuHPA3HVsUPuipz_nfoJzyOuR7v3HeTyDQgQNhfgMhJALWuJUFk_F7LozAuhhKSHeLlm65rc7xRF9qZ4zazXPa51oh46kX-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=h88R8fOVgPkVfkXo6vfzXKq08IPEjefGeQb9BySxn6l9AfnF2ncTmtiI_id9Tc6HyfGN7uRwoiVeYnhR4H2DnxHzR8tov6Y-zcpkrxn_zzP4qgcShSNh1n4dg5sV99yM67rZ4tV-ujC_7smosUVuZtUibHVFGC0DyKR7uEKBy43LqoFQtTz6ebU-SCBzveJsICqzZrcmcrxkmnXZ1I-qbOmxPCUZpxMdusYixaNxQHBGJoMAJAE011KNpn3msdrMFCXdlTThmPzm-9ugZpxmnde_FP-GtdEfcYblGgKgudboXFZkQLEjolLE-nqFQtNsPwEddfoSDg0jEKQmv-bLMxFYg5KrgfqS4D_dl_W8wu08J4rrnsYijEyaSGwRb-MExq-QFbwpG_u5vw-OvFPWo3kE-X97-lgYpVB7iPSEe7sBzoiwvZVV72h6gFPivrE9PVZUb-AVGcMBGDWJVMLnV0qEjyuj6wI5hsqJJUa5gdmOCWiH-HuuH2CSsB6HhjdLc9SDcfsVUPSDisfmJfT8W8bO1NIiTnTKhw8RclnFtejP881QAGm0LSKuMint9arEH-3bQZ2KBUoxuHPA3HVsUPuipz_nfoJzyOuR7v3HeTyDQgQNhfgMhJALWuJUFk_F7LozAuhhKSHeLlm65rc7xRF9qZ4zazXPa51oh46kX-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTPWhZ5OhLjWKMb01H0Wagq-b0zXfzgJYodU5n8-anbBsipEyHgTq_BpVBoB5wocVMsXqeyNrnnbqjNHEnK6DYWXvc22kDPahddwubDFnOvX-MrGVb6Zx-YLQ4p5JM2T1sIWG-FEyIIWHwN8exIJ6UxXJHLVU4sEgnXmEcNh6zrGXChJSOsbYVndWzIfe_WMrQ1UGrGjoGlgUzyH_CWUk7hxkLzWyLqjSKRoEOK37dd0knXq5NXdn_5ei93tdhp7cV80gppZ3oZc0bJRP03Jhrdj8Zc_xL5LeNWpU373_rHdLCy-Wc9_ax7VBosf9kI9nljvu85PtRx3WtxgjYGyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=ejc7J9z9OqUBJg0QpCgJvbeldS1DE-BArNGPQS-yJQjxQQYUm1oB9FQ2p9AGbatjWQfbLUzaPNMp33CYBrGQUVhjiyLKzohVpRstUzF1Zn9ugPWEDwYphbV79aXXqkPIWYZyfRFOD59WoM3Jr8Gvs7tqxKaYp5ZfbFQXy2XHLmLF343H-R3WcHq8Ywwm9ONzxrqW7GffghueNSkXQeRQInqjsEF8I1aVpOtDSsBTXQo_foMWCq3-rQe_yWTJsN7SvQW3n_g2xnFd8wlRHEpzYczrHGXhS-WA6j4UuxiX_HHzogVPE3epxyOE5LaduljE6BfzFpst7B8Q-D0BH7S8xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=ejc7J9z9OqUBJg0QpCgJvbeldS1DE-BArNGPQS-yJQjxQQYUm1oB9FQ2p9AGbatjWQfbLUzaPNMp33CYBrGQUVhjiyLKzohVpRstUzF1Zn9ugPWEDwYphbV79aXXqkPIWYZyfRFOD59WoM3Jr8Gvs7tqxKaYp5ZfbFQXy2XHLmLF343H-R3WcHq8Ywwm9ONzxrqW7GffghueNSkXQeRQInqjsEF8I1aVpOtDSsBTXQo_foMWCq3-rQe_yWTJsN7SvQW3n_g2xnFd8wlRHEpzYczrHGXhS-WA6j4UuxiX_HHzogVPE3epxyOE5LaduljE6BfzFpst7B8Q-D0BH7S8xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=J_c25oXN6z1AxFf2qoPDDyoLcsYxXFQL19qi9bTMlT6kelDeRNRY6K7NZozP_IOBTHe3zkIzZ0yxYEUt8z-oUV31XX5mWOeBb02E9dLWrSFVAzaH2FKHbCVYpg2yrk-eAJ2wjlVi6BPvYguwvYRbn4HJjQ9p1WX6NTfPnS1qEmaVIjAeiNCPfxReV5HLahIb6qYXobn4a0ZLME8a3Ba8Fjz_QSo1i7NQoEVZRXHM3oQ7JHrCKVFCAspH8ZpD8L8gx8OBycCtKf54nOj-XK-khRR6-9OyboCWeiI205pm9s55NRGiInIWkOLLanlVg89lDvCjIHat-f2qoOETCTE4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=J_c25oXN6z1AxFf2qoPDDyoLcsYxXFQL19qi9bTMlT6kelDeRNRY6K7NZozP_IOBTHe3zkIzZ0yxYEUt8z-oUV31XX5mWOeBb02E9dLWrSFVAzaH2FKHbCVYpg2yrk-eAJ2wjlVi6BPvYguwvYRbn4HJjQ9p1WX6NTfPnS1qEmaVIjAeiNCPfxReV5HLahIb6qYXobn4a0ZLME8a3Ba8Fjz_QSo1i7NQoEVZRXHM3oQ7JHrCKVFCAspH8ZpD8L8gx8OBycCtKf54nOj-XK-khRR6-9OyboCWeiI205pm9s55NRGiInIWkOLLanlVg89lDvCjIHat-f2qoOETCTE4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=qdWvOrVKcH3aw7VTRXRINpdKzpy7FNJ1IMgK272muIhNCbCxcG7O6ixdrVFfxz3Hqe2VKfBwm7AakAaFsJv-si9-o9eRUh_lye7QkYhUWCQPxVPuUKHkbvI5MWC-04Bz8gvVzsuFO0f7z4UVy1wAbPojberFDVQYcrM1x2006hFmfKEVqF8URnwKGCRInOZ4X2y9wgxCe3UeL0_hP6rs7TViSOCxlYdxALqR4QDZmEMOCpieJHF87iKcFhOIvjJK8nat6YsFCq04D26lN6z0p_5znExTYEpEWzrgS2R4K3p_8XbtTTxJkFp3ko5nLBpYWXM7ADMmmBXgEObRy2L5Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=qdWvOrVKcH3aw7VTRXRINpdKzpy7FNJ1IMgK272muIhNCbCxcG7O6ixdrVFfxz3Hqe2VKfBwm7AakAaFsJv-si9-o9eRUh_lye7QkYhUWCQPxVPuUKHkbvI5MWC-04Bz8gvVzsuFO0f7z4UVy1wAbPojberFDVQYcrM1x2006hFmfKEVqF8URnwKGCRInOZ4X2y9wgxCe3UeL0_hP6rs7TViSOCxlYdxALqR4QDZmEMOCpieJHF87iKcFhOIvjJK8nat6YsFCq04D26lN6z0p_5znExTYEpEWzrgS2R4K3p_8XbtTTxJkFp3ko5nLBpYWXM7ADMmmBXgEObRy2L5Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=SByiViV4BnVf4DJOWilIq4spU5gq07ttVUajRFU3Ss8F0uG3o1xBK1Z5vvJHorhEoeJ5B4tBqzVU7-NtoAHQSaCpeGvJXwQlLsOfDXHvYSqrI9y_OFtuf3_djOvU72ymJQ6HDq2mtKkjR1JhixYiaM86bMp-4XMXAZZhwUIwB_GrW-nOTCHRULna3pQecpEcwWSYS6SlsdRgBvMDYl4PyVZb5odboT-_GkQHd_XfbO4o3yZ4kA3AhXdyj0Tw7UV4ZlC6d2_mdjcjMkLgQ9XbNHuYe747GUu-l46PV2p_hOIJN4TKYBiCxtJKjZ2mRbuLFyq56DBnPcRV7mq0O3N8xYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=SByiViV4BnVf4DJOWilIq4spU5gq07ttVUajRFU3Ss8F0uG3o1xBK1Z5vvJHorhEoeJ5B4tBqzVU7-NtoAHQSaCpeGvJXwQlLsOfDXHvYSqrI9y_OFtuf3_djOvU72ymJQ6HDq2mtKkjR1JhixYiaM86bMp-4XMXAZZhwUIwB_GrW-nOTCHRULna3pQecpEcwWSYS6SlsdRgBvMDYl4PyVZb5odboT-_GkQHd_XfbO4o3yZ4kA3AhXdyj0Tw7UV4ZlC6d2_mdjcjMkLgQ9XbNHuYe747GUu-l46PV2p_hOIJN4TKYBiCxtJKjZ2mRbuLFyq56DBnPcRV7mq0O3N8xYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExZsJ0VZF84VO_PZVpY9GLzCTWJ2ynsozjwyDS_CyX7ikwG_w0D6D_SWWHfgnIcL02NRBZFiBbw6Z4qaWAKbpi9yOAaulWLx3ky-bzlGDZRkUTVgjZy-ailg6KvgqYPj_hyn1V-aoUdj6cXq2615XU6L1jk_8hBtWipBYDhK77x4wvbwSXgKyZymsoHwRxsQ6dcnvWMBy2pBI5wV4ynwLeln403i4dvUjeFOeMeQ2SOUFRiHUsgQ-x0PjmNqKNrbhys7_coAA0jQcEm1lH9MrpBNXIHqXRid33ypek0bWao_9MyUTshDA1z9P2XtY0VSMq5H_e2RzmZ8WVj-lGvPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X9wQuVc0QFcLHEqjPEm9XqvF7_XQ4PkDh3300SWfnBD1QiwMqDdQ6A1-JBeGQl3Db8vgZZ76NtxJgne1SFkJC3dQ976to6Y8B4Le7lYzs6UxE4j8dOSpw8rOWwAOU916Zv6R-iz33kBvNLBqtvO5R3q_bFx3WQ6kMvB8MYt4-n_lHYBbvrfTxDXaHiYd_vljLh0jXBf9faTyH5IJJTOdFZLSJ_6gqFsi72xWWvNyZIIYAPNVtZgqOKZJluNXX0eNzA0oEYb9gk6shI3jykSsxCIUgueaoq8kZ1lTrZzG3UuxPRHFm5KGNF707XXkcHsqWFRuJDH-oOJvOk-WHi0LcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=i9WIrwdTFVD8sQRqI6YT7KsmbzSFkZIGQlLElQLcIXpT_qhcS9NV76o-y1TmOLpD9mFg9rlsw3JnTb51JI8YeQ0jhQj3iHQm85B3fGFy_qu5xQbrop4We6ez45DbbDWiys2lAu4vT4pQG9fcNIoDrU61Hin-vZo-Z6VC9RCkvcQEguJiTqtMcXb7VMW_qndIPBXlieBEIVo4pdkuyyTJqs81fAzf7NJTrOuKhYc4RS8uZe53EdAUUTYAAD6cWUWZ4EnBsccucHAoXIL3x9ZXP05eOvRHHwDW7nhugAjM3Z4sl6bkL7oqyXGhQVGjS2NI-FBP60Ksn-kT1b527RjiwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=i9WIrwdTFVD8sQRqI6YT7KsmbzSFkZIGQlLElQLcIXpT_qhcS9NV76o-y1TmOLpD9mFg9rlsw3JnTb51JI8YeQ0jhQj3iHQm85B3fGFy_qu5xQbrop4We6ez45DbbDWiys2lAu4vT4pQG9fcNIoDrU61Hin-vZo-Z6VC9RCkvcQEguJiTqtMcXb7VMW_qndIPBXlieBEIVo4pdkuyyTJqs81fAzf7NJTrOuKhYc4RS8uZe53EdAUUTYAAD6cWUWZ4EnBsccucHAoXIL3x9ZXP05eOvRHHwDW7nhugAjM3Z4sl6bkL7oqyXGhQVGjS2NI-FBP60Ksn-kT1b527RjiwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=vwT7FwH97s_pYlYc-Xo3Ghr4Qgs_-qUCUSxnQY-RE6H1hXWG8aWdQe0K9frqn2s7TeeB1a1K8H7DDr_7h__vYAo8WCQSFU2GCK7fYEeQYSkO-GD98FfYZD4TrNyk-yVSab9sqMhJBP5DV4tTaVhyYhhWnTSOmUz4wq1D2dZWb_CK3MlyJSPqnBH9yQg4lNa3U_yGlQ_PDLTFysG2MhYRE0KyRCrGpWpe52k7lvDD_HDXMyADbwI1o_3AB4L_6oJMykKSOAPc1DrwY4QQh-fGd20L96gEPdgewtqUtVunJQjxHsDuRdmIbheYCtH8xZn9P4hBhQMD0d6zt7k2PupaMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=vwT7FwH97s_pYlYc-Xo3Ghr4Qgs_-qUCUSxnQY-RE6H1hXWG8aWdQe0K9frqn2s7TeeB1a1K8H7DDr_7h__vYAo8WCQSFU2GCK7fYEeQYSkO-GD98FfYZD4TrNyk-yVSab9sqMhJBP5DV4tTaVhyYhhWnTSOmUz4wq1D2dZWb_CK3MlyJSPqnBH9yQg4lNa3U_yGlQ_PDLTFysG2MhYRE0KyRCrGpWpe52k7lvDD_HDXMyADbwI1o_3AB4L_6oJMykKSOAPc1DrwY4QQh-fGd20L96gEPdgewtqUtVunJQjxHsDuRdmIbheYCtH8xZn9P4hBhQMD0d6zt7k2PupaMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxk7rSdIYTziZHpJDhGSFawozPChSyBbLE5SkYXHmNved_1gByTl5UtyHEgBDxTQihlziHZEyUNqtYJTYC1aCvtjbJdI0Djzg4VYZj2F2aKrLyehlEe7hel6DT0aGjQFhpEQMFEgLNqgpSFJ1GobTpKFHww4Ll9eIFWcX4vDpPPu7ns-mW_7zD5hGwP2Bu9iU4PZB80a_DEyOEEIt8URT34kaIM4r7GQErgzc7TsUY6wLsz6XgOS9TagP0Aq9C5cmH4Xtuj9-u62q3wo_HhLmYy3plz5IVFsNmf5UQUEVzqWlYr57Xj5ggPUbaip6s81IpFhr_7vPGrZDHcOzRRc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=R-r5q384JmcPWL5Y1ZH5BdP9Vyh1qG45k2_aN48GFxTyiY7yJs7YoaGkIusb-VnVD_rwwxg4jFzFJwGedPQ0O-wY5hJm1RFqPBPt8SOQHcOKgJ3Utbci5IwvHm8r4CuShDpJFzzPQn9hAd2IUMcLwDHp03u6dhmGxen6in9AwM5kpzWfpwx0CHy5k7VuDK5tWaYHExiyUe7CPCZkelQtpw77wOXk6zAyldxUvlEWQfvJard8D8ODcuGGLO9IU05FnuGNYstSKN8N9-tJewp9fOQOj_a2oKL7anDasbtl25Xx6G7Opi-drxQXC9vpWnZMe4C3pOuBTZt9waOU59qrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=R-r5q384JmcPWL5Y1ZH5BdP9Vyh1qG45k2_aN48GFxTyiY7yJs7YoaGkIusb-VnVD_rwwxg4jFzFJwGedPQ0O-wY5hJm1RFqPBPt8SOQHcOKgJ3Utbci5IwvHm8r4CuShDpJFzzPQn9hAd2IUMcLwDHp03u6dhmGxen6in9AwM5kpzWfpwx0CHy5k7VuDK5tWaYHExiyUe7CPCZkelQtpw77wOXk6zAyldxUvlEWQfvJard8D8ODcuGGLO9IU05FnuGNYstSKN8N9-tJewp9fOQOj_a2oKL7anDasbtl25Xx6G7Opi-drxQXC9vpWnZMe4C3pOuBTZt9waOU59qrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=OvDMJT-QotX6dvEmokUA55lbvJELRNUbN5EZSUxS1yoqFgjM4gWtTnDAaqlJ3pZImcTF3FLKNUo03__TZHYalsbSrAY3zuh-rJwG1ksJ3amh-dSfYm00B1g6vtnEfBZZYwwouZxs1Gc-rvUnzPXq7VI1Zh-GfQEoXxVcnU_Im0H-Sl8azw8PrmYZdw9kLFTXSJcxvPq0nLtp3M8r6jhOrPVGBVXPvLjKqvmwXf0ff7dInUGnsfoLm1RIyDT-IExITjcA8VSHf1ruqU_Hq-Q8Gj_QCmMKpsUscMavhyufbbLXmux4qMo3358wzqxAsLg9PH703SP1rSjswPLWr5ubIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=OvDMJT-QotX6dvEmokUA55lbvJELRNUbN5EZSUxS1yoqFgjM4gWtTnDAaqlJ3pZImcTF3FLKNUo03__TZHYalsbSrAY3zuh-rJwG1ksJ3amh-dSfYm00B1g6vtnEfBZZYwwouZxs1Gc-rvUnzPXq7VI1Zh-GfQEoXxVcnU_Im0H-Sl8azw8PrmYZdw9kLFTXSJcxvPq0nLtp3M8r6jhOrPVGBVXPvLjKqvmwXf0ff7dInUGnsfoLm1RIyDT-IExITjcA8VSHf1ruqU_Hq-Q8Gj_QCmMKpsUscMavhyufbbLXmux4qMo3358wzqxAsLg9PH703SP1rSjswPLWr5ubIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdVAf7VHL7wmYzhb652IsSacg3Gl_L39SAzMFcnjZqojD61qXwdUCwLCel8uWVoBfM0Y4O-svM207Ubb5ZVNOs71pNmzSbzBSKo5zam6hFJol3sHvrwKo4vMZzab9_TG4t7mEhrjkDCIl2nQSylwnHHamFmTRN4pUpB41htAayuMScMpH8bi8nsHU48l7UC8Sr3QpdkYc5XMVOo_zpjpwpnHU_6IMCr_4aypl71bnRbiIkRqniYn_9DSMt_yXwhUDdcOHVnuWIM-U-MCQwcNKeAf5HG-afIgqGpmPPqlomVyU78PFPA9_322E2sEAnGsF0_kW8BjDBhWcuK0LNnHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbjj-v1w-GoxIDnQrp4jphh-eOV-xaQPw9lswmR1zm7hL2oMAGKECd39N78HxPKylID_UuCr0Pn6gDDKGLv3mw1aOh0WEx8YZa7hjbhseIfz3NherDW0Zy9UDNDdLZ7RhYHJGSr_xxIu_fAJs0YaxyxDhrr_T92zhcEadSCrwMwmQhK7Xk86nXyAxyVdiCw0mgCcsVuWyAvZHa4sizIF0ROyngaH9bR31hcq6UEGvw3u7fh5x5DPLqXq3UewSbwb15EJJxSVX-5F02PTatoHBEk4WC3yhD1GyzoRJG9LIlW3n59PHqXR5_lgRQiUF8b3MupPQtn9WpB4sQdb9bNo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tyVhykC9cuhBiwjzQB98f4U5geSp69aah9b1iaeHv8-2kmUO7lC4p-az78jqZV4ztVAiXK4y9LevvHoRpgGbGdDGfsxbYwd2xJhpHNbIKonJ3c6MVeo2lmsx9Q0EG2rlBt60HhnnEetrdrRWsPWgT1l9_C2PcJNNMuJRaLWdU_6JJAWrGFWJJ9s1sTj46A1-VJQDEdSmXoJc2T8eQGJew4k0rOEVvD5UxJf_zaoTLiM17i7v3dUTYaqrrX2Kj4n1kxbhuPUWlxTAruun4GQd91VsmxFfx5JtHnAyG1JVjJJO7YwKWa_OP_Qp8hOwJ_BFk3mJT6k48fsZJozOwYRORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=o-mBRRk2e5Ayw6uRwbrQdC9z0QQV-bD9KoEcAulrhEI82YWwjKjOTd0Uunebfv8jQAQ-2sqdRHmKkEeQqKLXZIRBo2T2sopsJXzOMH_VcQ5RR6kIx4xHq97rXYDNUaAYB1j_P1YZzvI3rE0pZgTCCv61TifjeLTHsqn1p3begQ5LoFSVc8gjn7HzxeTIWeDS3DGPBaKoCSwxjRPH03TV2lEhRY7sO6Yj1pJTAF60fLhJ_Ce5wUgXEOYDspkpfUwmCGO7ebox0anQrLJ8Z9i_H1NjemQ1C_qiUb75CvNcoj94hbC0cMrVe0-wPuTcQFUmundJkx2i7uBmkWe25B4TEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=o-mBRRk2e5Ayw6uRwbrQdC9z0QQV-bD9KoEcAulrhEI82YWwjKjOTd0Uunebfv8jQAQ-2sqdRHmKkEeQqKLXZIRBo2T2sopsJXzOMH_VcQ5RR6kIx4xHq97rXYDNUaAYB1j_P1YZzvI3rE0pZgTCCv61TifjeLTHsqn1p3begQ5LoFSVc8gjn7HzxeTIWeDS3DGPBaKoCSwxjRPH03TV2lEhRY7sO6Yj1pJTAF60fLhJ_Ce5wUgXEOYDspkpfUwmCGO7ebox0anQrLJ8Z9i_H1NjemQ1C_qiUb75CvNcoj94hbC0cMrVe0-wPuTcQFUmundJkx2i7uBmkWe25B4TEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUyN2HL3OgtbeJe14n70p7JcrtF8ZTHtcf4UZ6AmmtqDXDWvWffYdCSqtH6R1zijeZ1iQ8IOiYmA6QsVb6UiIQbdlooskwn2yhHyrNxLdh0gvL4wFyR9KSzIw0BZw9CdRMwgfRBVEiBFAHtBF1uFnwD5pCvDZFWJiQ1qqTO4m0xfZ_5cMTTwHU0ann-7fay3vfP8fdmqVPnfDDf3ldP7tMpEtGx15_mBRcAw72_8vtiH-WDVEBXkkRh-h_xPvOennJyJz63Hoeh_myixt6zo2j8RceapOxvTBerKtUzFq92-sReZROVO79fN2jQDFjuDHGHy3Gv5rVCcMSAftkEOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcM1g6sA-nlBrk0QE6jY-7NaJECLI-PL0DIaMYPhE0MFvxdmS2HtqoSkre7Z7eQHiWMBoG1f4yZbGfa3fS_IWdA2xVvo1XxDi-4UvFx2c2wjlSzGq-dS3yPXL2BZNjO1lMVOWsZ1yp54VuT7hEP4SZj8HwMvtUM2Au7wZQQb4-w7RwMLG-cUjVq05xPTPmTeoHDPks0Zmt4f7tE83YgCUtz5a1oRfL64riYuxpaAOjwMF_IJnXj9XExPOQTG4xi5isPuHCSB9n-gl6jZCSI9M6CM9wMlRD1T302kxr5o8rr3_Cf1a4jPtVyGc4JBs7_KkwbY9sgHpTMdc289g6zU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=E-M8iEU3iJUUK-cuuILPlDoC_K_73fBx4wpPpqwFTQ1x8ph7cqe1lt_ug4-VjV8GpvzbidmLkNgES7vWPERypEtfffeoLRxBRjFMw6tCXXUgg401JtncuNbluZmJlwZ74xvHz8ANOWEsBKC42JiZsvpICHFy0J2DXXmFHSzGmYIQqLypo9p0B8y_jrwlbvx5dyWwO60ijNpTFnob5BV0q1XN-J94v1H83vYcwIT7Zpdg9TlJb9wsHpMpLak7ZHGMQ53giLROiMY5fAzOUJtGkJ8RsFeulii4JbgIojC0Wi2T8eFVMZd0ucT5TCyN3E1Wy8BJ711uy1yaQ1gA5HpQyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=E-M8iEU3iJUUK-cuuILPlDoC_K_73fBx4wpPpqwFTQ1x8ph7cqe1lt_ug4-VjV8GpvzbidmLkNgES7vWPERypEtfffeoLRxBRjFMw6tCXXUgg401JtncuNbluZmJlwZ74xvHz8ANOWEsBKC42JiZsvpICHFy0J2DXXmFHSzGmYIQqLypo9p0B8y_jrwlbvx5dyWwO60ijNpTFnob5BV0q1XN-J94v1H83vYcwIT7Zpdg9TlJb9wsHpMpLak7ZHGMQ53giLROiMY5fAzOUJtGkJ8RsFeulii4JbgIojC0Wi2T8eFVMZd0ucT5TCyN3E1Wy8BJ711uy1yaQ1gA5HpQyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=f5j2rX1-HaCcG_3iNNz1x1xM5ozhXpic1p6T82en7qGVLL51Cp4a2S3h5-qLnuF7vtQomIK2uSocF5TppFS45EYgbvd8DZITkNP3ErTKieXiYZGlv7qBV652hwD0T-RHAxWAST__x59MZ3__VLmrwSeRAeIe2fMqkiYYypG82nDISu52lWiJ2RAtfKBxso4BInSZRl8LEw0sxXHqiBe8-RrrWfiA_iuKcC2LdbB_xN1bOU4ZlW5phHrfALTOhO-9e6dwCVQBL_KlfNEazlXsJ6ABYVYZf2avTPaQLTCKCeUYL9BNf7px1IHbFcHUp_Bjg2sOfih_9YfO82Yds8eYJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=f5j2rX1-HaCcG_3iNNz1x1xM5ozhXpic1p6T82en7qGVLL51Cp4a2S3h5-qLnuF7vtQomIK2uSocF5TppFS45EYgbvd8DZITkNP3ErTKieXiYZGlv7qBV652hwD0T-RHAxWAST__x59MZ3__VLmrwSeRAeIe2fMqkiYYypG82nDISu52lWiJ2RAtfKBxso4BInSZRl8LEw0sxXHqiBe8-RrrWfiA_iuKcC2LdbB_xN1bOU4ZlW5phHrfALTOhO-9e6dwCVQBL_KlfNEazlXsJ6ABYVYZf2avTPaQLTCKCeUYL9BNf7px1IHbFcHUp_Bjg2sOfih_9YfO82Yds8eYJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=sR_2coGEb_llabvr57e4XYRdGWLEzMloOfMs98wQrdqI47WqcuZfk66FH-c0v5pwjlGxurQwgaEyw7l68DUhlsX87y_3fW-atlsM7cUCbRjyVhiJ34_o7NdNJYPsOf5inFPP_cWPNH8wkn9YZJoUwr6owWXrsTAk8_Iijk7jgSE4qtZrlLQUKKSQi6GR5TyepgN8SxazYHp0KBWW3jLdGw2tDCcgThrr58NxiOQpv8VxmG65mh74m0ASq2Vq772ObQhmQLtEFcJ29a9pZ7LQ4RTU0mH51QRHijfub635W8GnBAE8Kc19sS3pCjkDXYeNU0WDrWENgbDzoo9C4zz3fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=sR_2coGEb_llabvr57e4XYRdGWLEzMloOfMs98wQrdqI47WqcuZfk66FH-c0v5pwjlGxurQwgaEyw7l68DUhlsX87y_3fW-atlsM7cUCbRjyVhiJ34_o7NdNJYPsOf5inFPP_cWPNH8wkn9YZJoUwr6owWXrsTAk8_Iijk7jgSE4qtZrlLQUKKSQi6GR5TyepgN8SxazYHp0KBWW3jLdGw2tDCcgThrr58NxiOQpv8VxmG65mh74m0ASq2Vq772ObQhmQLtEFcJ29a9pZ7LQ4RTU0mH51QRHijfub635W8GnBAE8Kc19sS3pCjkDXYeNU0WDrWENgbDzoo9C4zz3fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=ZEPRoGyOGMF6_lF_kNrLEhwbEqxsPyLUxGq1Zib3LoYr_kN-A30A2CdBmH-qlH3P2eDjHaUyiK4XASPHVIvbvv6t67JrFVhzoHGsh80JFttMgh0WfkiPiZTKVlYXiC78na8bChT6V4tgHwTUlRV5ViTcc4tKzAph6tsIjAB9EBbRIW6czg8uyNKSpIZrlGAdlIK8W-MolgggqNoqdSh4ooZeohfhp0yMY9Oc-EsdpvKUOeY2zgTUJyeeWxqn03DloezQpHO20K3DN1cOWMr5rjFuUBFUXVcK014vt0TN7xjyfGwy4JaxMEyZ4Qa3slJhUqyomsq7JTDUXkIWeD4sfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=ZEPRoGyOGMF6_lF_kNrLEhwbEqxsPyLUxGq1Zib3LoYr_kN-A30A2CdBmH-qlH3P2eDjHaUyiK4XASPHVIvbvv6t67JrFVhzoHGsh80JFttMgh0WfkiPiZTKVlYXiC78na8bChT6V4tgHwTUlRV5ViTcc4tKzAph6tsIjAB9EBbRIW6czg8uyNKSpIZrlGAdlIK8W-MolgggqNoqdSh4ooZeohfhp0yMY9Oc-EsdpvKUOeY2zgTUJyeeWxqn03DloezQpHO20K3DN1cOWMr5rjFuUBFUXVcK014vt0TN7xjyfGwy4JaxMEyZ4Qa3slJhUqyomsq7JTDUXkIWeD4sfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xut32UpDSxD8B_xBEpn5FrxuV5mKV5NHTRZNJefwLgyrv9Isy5CyuUt5dSLCHYvid0JXmNiRD7ok4qorufLhs4t7JzvOBDH2dJpnZMaSClo6uZSPwXljxtl7WkjnGNBbmd8HAKOS1NHIVae5TLQaozgzr17f5owTUcv1HMZmKZGhlcnjbzLBDxQ2cfG8BcTrVWSxri9HMqGTh4ZR4ZeV9esmPh7u4h5qRCRtaGwZdcBGrcWkg_ILmn_XuBSt9dtbnAwRqAaSPHahgI-likWGULa24Y2ml6pTM133kOvGyGk6e71_86FiIjTuGVaJg5BTq24gsFij3TsXYnnBakWuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=Tq_gw9ik_VqQYSssDSripFcTkOIbX1OuodUeU9kFQP8sJb_1Lfz2PU5iKK5ffokvOoq83g8nMbmRNbtKovTTC-3CwfKusgfk6J-D2gPvK6MjNdmthHw30Ix07lNn3jVmZHNJDXL4glvZ8fwzbfEiZy6aGkZaYZ8v6K0_1naCt-S1ZEgejv9WqYU3-jbqSzlt6qm7S1esaZUI0TmDaCnhegsDrlzUZKKBXBUh4UsfWvXm1V5Z_VV7O06Qz_XnzJImV56FZ2PH2u2apGs2kRqfLi_BFvimrHAbUzaVU0_USur86ZOYSLsRdRbBW82UL0OUIhxoSYuc4tV6rUog_MdLCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=Tq_gw9ik_VqQYSssDSripFcTkOIbX1OuodUeU9kFQP8sJb_1Lfz2PU5iKK5ffokvOoq83g8nMbmRNbtKovTTC-3CwfKusgfk6J-D2gPvK6MjNdmthHw30Ix07lNn3jVmZHNJDXL4glvZ8fwzbfEiZy6aGkZaYZ8v6K0_1naCt-S1ZEgejv9WqYU3-jbqSzlt6qm7S1esaZUI0TmDaCnhegsDrlzUZKKBXBUh4UsfWvXm1V5Z_VV7O06Qz_XnzJImV56FZ2PH2u2apGs2kRqfLi_BFvimrHAbUzaVU0_USur86ZOYSLsRdRbBW82UL0OUIhxoSYuc4tV6rUog_MdLCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=TvYkCTUDbnOF39mdKLNrdIs2HHUzbbVRnDwGjx9CE9Mhg-JyUYFG3UAByHOymCQ86I3Gg4d-Do0Dg4oftqsnLm5KSPukFLDocHqWVVaun8pto29bSy8IRP0OO_c9-6pfMz75VDpUojjfXKa9SxavWhIs64bf-0ZlV_MGmMk9OfHYzJ6-tSNBL4EFe7-UnMZuLovj1XEgjqDN1khmchi8PmxA22hP_gIMZfFsMtpfzat_8C-HcxBeN1kLifuEh7lCVLotmMqkMz2FQS34DYR0uowzz_zMM23mx1qcXYss468RFFoJ4gvJiDGWreyvHVYw3W_ezEf7mpGR_jrNCOG3jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=TvYkCTUDbnOF39mdKLNrdIs2HHUzbbVRnDwGjx9CE9Mhg-JyUYFG3UAByHOymCQ86I3Gg4d-Do0Dg4oftqsnLm5KSPukFLDocHqWVVaun8pto29bSy8IRP0OO_c9-6pfMz75VDpUojjfXKa9SxavWhIs64bf-0ZlV_MGmMk9OfHYzJ6-tSNBL4EFe7-UnMZuLovj1XEgjqDN1khmchi8PmxA22hP_gIMZfFsMtpfzat_8C-HcxBeN1kLifuEh7lCVLotmMqkMz2FQS34DYR0uowzz_zMM23mx1qcXYss468RFFoJ4gvJiDGWreyvHVYw3W_ezEf7mpGR_jrNCOG3jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdNa8sCI1X7mdt7ev40zQWTLI7l7L-zcS4r7dYQfvYk69lrC8qrHtlD4BIr4_JHv9kVZoR49nDPD8wsA5Qr8H4vcIP5mUYDtsvk3L17EwWDH0g0zl5WSHQEfo7sQjnIIxZJu8knULTL4x2I-oJaikHaZ3nTEV1VtqjgpliW1Yb9dHz-GuhMd1rXirSFHPZRwIF3zJwVy--IDAc6B9tgvBFflCzSb602sHyPE8LSyYZpeG5csCejrxDvbkusX_8PpIu7wzCx1Ycxtk74R2nqjbBzJhcNElWSoOxtSvmBt31Bd0OOViOyIbrpval3EKs2IGnF60J_2gFF6Jb0caCfamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsqooHkRG17tbsyY0Ho0GR6A5NaW-dz4sncZp-RUfPSWGjam3B-4BflB8sVvTAJLd9vmbJjTcTb9xnrPXaX7sAOn1K5w_d__SAquXBTZTYCnnVozjFF3xBRe5RKMAaAPObibX72Y1tE4S1e23WpYwqA5kM6gIMBS5lRGDtBJbQ8txqwQ_XGnRlpSBIoD1wCqIoVjl_PCXVlvnmTkoQlLFp2Kv3qxIfFCq6CA2axIDRdYb0aLbjGAiCzy8uQ2UsAUKvY2LTBiAnvshsuQl8Vc14QtFHrVJRFePOc7tmdvFQSDvtXp-FxtTzSVbu5xZLf8uEyX7aQUQ6tnLnxuEL0Kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EejKv5a97RY-ZU4Eq87tJGA-ZXSh_RAXNdYZKDW3hYYIlQ8l2x77lJR7wFfUCoqYB7sl7GAknmuAD2rjtEsohLd_p5xOs8oTwUqKrnb_qKyox5_5dQaq2zRhl7T1QuX-9hlnNHWpFCRMue1FXnVkZ3YKNYjTy4tNrt8hQDfQXWZMfdyyOGO6JYWDf-Lt5CwQDcY0bKHvca37ac6uEio5fZmM7OMScTbc9u16cyCAvW5CDd6wg_wAOxd4SzNZnkWRHM0fgpJKcav59irkr3JmxGiZIjco2ZUr03UjRh9wkD30hC-h-K-kUBsjtkByeIgJB4h_E50xRKTHnVfb-7oIZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=eWUij68zEDmUyEgDvagmv2T6VnrhSAiQ_BjmX_5nl7xz0ha1uwnRXv6b_oOnXxVFcxg9FWW3O0tLCHSJaisPbxtCCw-_Iun0gORskDy_U9vhM1_aWvvMk7DYwx0T_6vP9dfyWieACSeXKgZcjiJiWNomvaKs9-S4NI9rrfJbj3n_HQKG5yzj23fcnOaePDmPEQuFmqu77z17H7QVXzd_n4vzGMQ5bxazCVdbmRXdCj57MTGJi4SZCyTB5ICwVBzWAi7gORhZtFiRIrsEtN8JkQlJYCvAm3DgpB5GEsj6cQ_i7UhZmso-Os9JLWNb8aHHQnF5wICrfbogqwGQ11GgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=eWUij68zEDmUyEgDvagmv2T6VnrhSAiQ_BjmX_5nl7xz0ha1uwnRXv6b_oOnXxVFcxg9FWW3O0tLCHSJaisPbxtCCw-_Iun0gORskDy_U9vhM1_aWvvMk7DYwx0T_6vP9dfyWieACSeXKgZcjiJiWNomvaKs9-S4NI9rrfJbj3n_HQKG5yzj23fcnOaePDmPEQuFmqu77z17H7QVXzd_n4vzGMQ5bxazCVdbmRXdCj57MTGJi4SZCyTB5ICwVBzWAi7gORhZtFiRIrsEtN8JkQlJYCvAm3DgpB5GEsj6cQ_i7UhZmso-Os9JLWNb8aHHQnF5wICrfbogqwGQ11GgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc9uNIS5jZQgkbyWIcF_SFdT9YuHfwVV3qAwFu4o_yjLx2ZeUbDw-EkfplMUyrB1IBKFtG82sHwbGGmQ4MmW9CVVRO19sEz894Zq_gRQDQa1tn-6UB3u5QPV5aVtmiUMToABhGklTTfRJo85OcbYBhpYHg6Jjhd-_wCqacXQzI1zPz0w2RdmvBysu6J-TitXd7X-yVaQU2vhRqMB2xrBip9y-lrwU3dNMvWSwdcSZiPh2Tj2M1TtQcYPCvUjFnqiIVlHCxAuqwdV5Uh6YMDg0OncsuGsj0yO6IrrBUCjLjcuH4JxU-g-nZ753pUfFMA6StufqbjVRl4ufLIAazvZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=reOvjMutzVoTbkqIVoi-WOXuiKOdA8FNhvS__cXlVWs-TeX5tMZEiF_mNSJs8X6HVWWTdiwuHV47QsPg_lZ_s83Ofj4duijJjH1u8EmrQAABEY_ZgOMZti3jSsiWUI6dVE32Efp9E95dgkqj6xttLHRPzVjvu2IO-kIOsEa6UR49aYX0ZUTGqTiY03eaPudfTl0acCI48L1q6LZHHZ6TDvbe4sYZpA2Bx9Tf2gh_lpWavvWnp2N7b5-CWaNVKvLhno1cFCWX2ZCrOulTuYTN9XUl-O5JRw9pa4qGvIuClEy-02YRVgoey1URvPs3k-PELn95X0Gz6oxe8MdqThXe0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=reOvjMutzVoTbkqIVoi-WOXuiKOdA8FNhvS__cXlVWs-TeX5tMZEiF_mNSJs8X6HVWWTdiwuHV47QsPg_lZ_s83Ofj4duijJjH1u8EmrQAABEY_ZgOMZti3jSsiWUI6dVE32Efp9E95dgkqj6xttLHRPzVjvu2IO-kIOsEa6UR49aYX0ZUTGqTiY03eaPudfTl0acCI48L1q6LZHHZ6TDvbe4sYZpA2Bx9Tf2gh_lpWavvWnp2N7b5-CWaNVKvLhno1cFCWX2ZCrOulTuYTN9XUl-O5JRw9pa4qGvIuClEy-02YRVgoey1URvPs3k-PELn95X0Gz6oxe8MdqThXe0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=MIunXjGMZ3b1Qprr7apflxbwDhWF8Jfi8Uy_8x5BcBj_5nK2DxQZENiDfwr_YmyDhHXsKj3u9S2vN6xj4_OqfXf5zcUU19iZm5u086nxsbtnATiVoFMOl8nyrc-BxQxJro_sLPXfU3sNg8Sm782Ku7kmSCecY6oSRTDFe2UubHCVpg4yl-2ZR8qh9HmBJpWjMMdb1XmsipS2OfW8PMriwKAMxURhyhxvNDrgAPPckg0a_LEamXYWcBf4dfPpQC5aMAI8FUItfWITD08jHt3a-wlQsue9phSn4O48y3x0RYrXedmkEnTY7iEbS_cJ9BY87AlIc59Y_4KikWFOrdrg2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=MIunXjGMZ3b1Qprr7apflxbwDhWF8Jfi8Uy_8x5BcBj_5nK2DxQZENiDfwr_YmyDhHXsKj3u9S2vN6xj4_OqfXf5zcUU19iZm5u086nxsbtnATiVoFMOl8nyrc-BxQxJro_sLPXfU3sNg8Sm782Ku7kmSCecY6oSRTDFe2UubHCVpg4yl-2ZR8qh9HmBJpWjMMdb1XmsipS2OfW8PMriwKAMxURhyhxvNDrgAPPckg0a_LEamXYWcBf4dfPpQC5aMAI8FUItfWITD08jHt3a-wlQsue9phSn4O48y3x0RYrXedmkEnTY7iEbS_cJ9BY87AlIc59Y_4KikWFOrdrg2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=e_zjz2MUxLkB9TXyAlN_ipXKOu7VrlGEQGzQe2NRW5MCtrnroa0zXgX0AyLSxgItM5z8x8R5gwZPL2FkIIj61_1opd7WRjGcTGN_lZlk4MIy2zLN9yQYzoeNrNNBAVqg3pYahckaBXqjjdSK2oibJESXDBp2hqQCAtwqymjZZ3lyMJRBm11lgJULRRFbWyDBaqz235F5jCG6Bmh6iME4e_IFbWvBpoV6eHsfutCSyUZzp_Qj6QiGa-uvE-3EkVM9eJiySve489o4loPphH9zx5ho9U_t0gEHfWXP5gx5ZXBf74ShiKiNqSUPHJ7OAU2FY5Z_tkN5NnVxDEJMC7KBVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=e_zjz2MUxLkB9TXyAlN_ipXKOu7VrlGEQGzQe2NRW5MCtrnroa0zXgX0AyLSxgItM5z8x8R5gwZPL2FkIIj61_1opd7WRjGcTGN_lZlk4MIy2zLN9yQYzoeNrNNBAVqg3pYahckaBXqjjdSK2oibJESXDBp2hqQCAtwqymjZZ3lyMJRBm11lgJULRRFbWyDBaqz235F5jCG6Bmh6iME4e_IFbWvBpoV6eHsfutCSyUZzp_Qj6QiGa-uvE-3EkVM9eJiySve489o4loPphH9zx5ho9U_t0gEHfWXP5gx5ZXBf74ShiKiNqSUPHJ7OAU2FY5Z_tkN5NnVxDEJMC7KBVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Z7jbg7lmx8ZkREPs6DMHZu6KkJm2J6k27xXJzGO04J_jnTd589AgnGhTmwnEdmB2AKJbOvoydmudT6P8MO8FgynL9oCYFDA2kvWpwOJgd-uGHPcLl_h-WXmdAHTCEOxiHnYFEBKqTCcwtkI0gh4l1OaxNRtD55RZ_MZX-yM_3eerZaVymM6JZ1bc2gHOdEzEDQbqzo1QdhmwTXmz2asKXDYgA9ikMlDhsq7kvEs-LLIzQMKKIK758GPAiWiOXvP4pPvPdWC0jv3ioCbfGQGwe6QJm7o5D-V0tbxgOGdRD49MJFee8UzNdiGhz7I0OmlytXuMzeEWsLsOdBwaUxdxZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Z7jbg7lmx8ZkREPs6DMHZu6KkJm2J6k27xXJzGO04J_jnTd589AgnGhTmwnEdmB2AKJbOvoydmudT6P8MO8FgynL9oCYFDA2kvWpwOJgd-uGHPcLl_h-WXmdAHTCEOxiHnYFEBKqTCcwtkI0gh4l1OaxNRtD55RZ_MZX-yM_3eerZaVymM6JZ1bc2gHOdEzEDQbqzo1QdhmwTXmz2asKXDYgA9ikMlDhsq7kvEs-LLIzQMKKIK758GPAiWiOXvP4pPvPdWC0jv3ioCbfGQGwe6QJm7o5D-V0tbxgOGdRD49MJFee8UzNdiGhz7I0OmlytXuMzeEWsLsOdBwaUxdxZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnWMkKbfENb7ou_tpsI9cfsPVdXWLxbhhgCZspWq5SKf-BkgRFy1fZOuWj_D85AecqCHbos28CkuJE7ifhflstWgzi07w78vsMjBCkKBk-BJh6fRo4uSGtBwI_UWOr7o_eEUpf_0cHiexboCPoQZp9YHVKDd5ZuVugw56h9D0fOg6gMM1a2We3_lCtL50Ky0k_Ilkh2-I0JLBPb_5JcgsI6cNJ1l-uDpzcgPeiYMsjnCwEAxPPFYvlNYhz69lg2N-hiU9FuLWsU3cAPrr7YM7Cc9aXsizgPXecczGqCbNiXkA37645Uo3ItsrVhM7vPoBNZWx31ea6xiSI0Yab1d4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj9Udn_dave19VDW66J_UrWyKdkrIeetek_qBi1OZS2QJ2cHcmJPdCRbxTVa_NtzzMHm8MJQ6xMIZpqIYXYx7HtaLwh1yie4TxPdSbChDtiVTMCVtKumgKx8xNSk6q4IzH-9pcM2QPZZN3bHuj8FxY0EnWV6VD5Zk4OfnmYcSK_S3nWj_DJaAcLUZW3tbAF5h0CTkgnMhrAFr6G_8uT32y11iGoex8AbMSoZ0hCeS2pr86Upl6DLI799J1248AEKF0YrZDMe8bV-Bzb6Flyq3LxesPdZOCibzPmn7HgAUADmJwxes-D3tOfInGoFdFP9aAqo9mCoK9BB_NLHceICkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=PDMwH8LMMCppggVbvTrK-lf9kg4w1NesXegl4826VQ2BBwQgBlHpg0fCLCs_ggEIXHV_zfxVP_LgPIHMmoV1F89Vxe90vPQ9EvBDMTRLgdhYi64axlSDmFa938DdU14erAZPZfGXMbnwKiy5x-MNLd6DOo66ab4Qf0FYUn9DTjR3Lb1l6e5bRolvRRTwbzI8X1NKgjZ0gR4U4K5OmbjISShplomkI5Hk-l7ng9HYkUd81h2jsIqr70_K5RkjvkU2kgdgIoUHTizoXG6ecRSRO89jsODdxM9f_4Fb0AISlRYEwf9B3GHG_cY9BjVnng5QlZ4GbTgJ8-l0Kk2GSMTt3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=PDMwH8LMMCppggVbvTrK-lf9kg4w1NesXegl4826VQ2BBwQgBlHpg0fCLCs_ggEIXHV_zfxVP_LgPIHMmoV1F89Vxe90vPQ9EvBDMTRLgdhYi64axlSDmFa938DdU14erAZPZfGXMbnwKiy5x-MNLd6DOo66ab4Qf0FYUn9DTjR3Lb1l6e5bRolvRRTwbzI8X1NKgjZ0gR4U4K5OmbjISShplomkI5Hk-l7ng9HYkUd81h2jsIqr70_K5RkjvkU2kgdgIoUHTizoXG6ecRSRO89jsODdxM9f_4Fb0AISlRYEwf9B3GHG_cY9BjVnng5QlZ4GbTgJ8-l0Kk2GSMTt3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=CTwzrtsJTjnbhtBtihQpoYA0BVxAtqKohjaqeO3bJT9kYYpgmZ4-cNmbJirhBG6gImynzm1g1l_saMbd3u24TlIXY-FkjGqRwhXExApYSkELRpwHvV5Nr7rHsg2InKptRXdcDlbYCofnjZJa_FUua7ppU3KpvnZ0tZgtu6_fHK9StkPTs5gtgNAceMUzEA9s-doTz4mzP88lXga_7LzkW11oL6ni88vjB_gmT_AWEn-fkFNsQHdK6ofsnDzqYWQ1wxrwUZGdHIQZKr_k79pv_Gd5vnf37dNvW0YDQM3bCRIBFT_YQ3444Kpn_15-ZhK_D4IMWFBETkkiZJyC_JlzEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=CTwzrtsJTjnbhtBtihQpoYA0BVxAtqKohjaqeO3bJT9kYYpgmZ4-cNmbJirhBG6gImynzm1g1l_saMbd3u24TlIXY-FkjGqRwhXExApYSkELRpwHvV5Nr7rHsg2InKptRXdcDlbYCofnjZJa_FUua7ppU3KpvnZ0tZgtu6_fHK9StkPTs5gtgNAceMUzEA9s-doTz4mzP88lXga_7LzkW11oL6ni88vjB_gmT_AWEn-fkFNsQHdK6ofsnDzqYWQ1wxrwUZGdHIQZKr_k79pv_Gd5vnf37dNvW0YDQM3bCRIBFT_YQ3444Kpn_15-ZhK_D4IMWFBETkkiZJyC_JlzEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvq42gZlIDDihAdhHUv9w9NWvdvkH2iRUA9MxeYQHJRndUTM-xKy7Gl-JOx7HYL8FGOBg_cYKAm4Kccb4IZzVL0yEXfRR81n5SHGKnl-FZcLrgR-EInhQIsl2jG0AF2nPUvEMvbGVBsa8K8gihi3FHmRgD951tlrJEAwanL7aaHs9hi26zgVSQabgmQt4a-OTD1x-HRwJZuSRAHRs_5edVpOsQvcdhe6RUuZftLQphsk7MNkeyp1CYoa6g_UTeqIeqXbwSzI6QYhjP1LqOld0Orud22fOTPU_-3uXX-1mOJGkwWPuZ9BkU5fy8KTLVMtarevORRfZlUO4kBntI94vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=Y9gl--ga7falBwtuy-fR2yL_n7HiBUO32aLdO24Tfe57TfanHgPmoY73IJr_u1e2RSw5A5WNlIR1SVk6Rfk7lh_uh2jvvN4ujENUtLH7Ctq88s_2CoWDT12w2o1uooFk1vnKvac5IcfVvs0EuVpM0lIyVSEg-bPQcVwxbiAgwK_evxKA6kzqKXuC4bXz3H8xjrLEtGvyL5FypndM3ZZt6xNCRNrfFl3Qttq7whxuzsE6BJgoV-lBiATdxnZrn1ZDkGCOz-bk3oqZn3D11aY7PPWozZamxbQqK8bHaqJEVdx8oJsICL1uy07bM10iEarrSopRUelPa1tHxv902iapfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=Y9gl--ga7falBwtuy-fR2yL_n7HiBUO32aLdO24Tfe57TfanHgPmoY73IJr_u1e2RSw5A5WNlIR1SVk6Rfk7lh_uh2jvvN4ujENUtLH7Ctq88s_2CoWDT12w2o1uooFk1vnKvac5IcfVvs0EuVpM0lIyVSEg-bPQcVwxbiAgwK_evxKA6kzqKXuC4bXz3H8xjrLEtGvyL5FypndM3ZZt6xNCRNrfFl3Qttq7whxuzsE6BJgoV-lBiATdxnZrn1ZDkGCOz-bk3oqZn3D11aY7PPWozZamxbQqK8bHaqJEVdx8oJsICL1uy07bM10iEarrSopRUelPa1tHxv902iapfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=hBw72Gii8J9hgv90PWy-EDAeYr2nrF_AuZW0IiyvJDTkqg4NzuOFbRz1BW3sM6MxxIYI30L33zlh9n8mhBdgGvZ6B2JW8sFE1nQq7H_5SvMA2kdD8ZZ6eqmkeEUH-xHo7NVvqyRkhxCVIZs0aBEaR_ei8y7JoA27ShxQkHMoXdPgGyuswZFuaqNuxzuAvXQb3IA2AaJORFfZmIwqgafv-c3JhZSMKfAt_Ypq6yFyx5o0oTacBSqw_lmuLrFlisF9QRCGSQb9wmjXXXUUDN7_5UETldAO7Mt_LhhOiKu5IQBwosxEO_OKS8smfizNsoFBsnSvA9OkM6nelaEeCcFXsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=hBw72Gii8J9hgv90PWy-EDAeYr2nrF_AuZW0IiyvJDTkqg4NzuOFbRz1BW3sM6MxxIYI30L33zlh9n8mhBdgGvZ6B2JW8sFE1nQq7H_5SvMA2kdD8ZZ6eqmkeEUH-xHo7NVvqyRkhxCVIZs0aBEaR_ei8y7JoA27ShxQkHMoXdPgGyuswZFuaqNuxzuAvXQb3IA2AaJORFfZmIwqgafv-c3JhZSMKfAt_Ypq6yFyx5o0oTacBSqw_lmuLrFlisF9QRCGSQb9wmjXXXUUDN7_5UETldAO7Mt_LhhOiKu5IQBwosxEO_OKS8smfizNsoFBsnSvA9OkM6nelaEeCcFXsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=qU8nxyUZghx8U45EN2Y66qrm2WOrQWYXGaOwTl5C-m3NoBTpinQkCGgdubOME6Jz26fL7dEn5rbBpzjTrZQ8r3xVd6uhpQHgjDy-xVQ3HryYaG88iV-udln_sUP89KRbT82I5VOBP6mYlU6ZWCAIg8JmmeSLu2Yril-chJD5HUTkgKT80SS9yoXjX6UBDLu8imXgbpKftS9dbRSWbZrJbFlrY7Nx82MlcRsGtyjcr-TscxaNgzrGEGO6S7to7Dt3ukoFgJSouP7FA1Qe6zyxO3U_T-RJwUv25tDjcbDDAlugTvNpvxt4T461cJWtW9Lq9j1M73Cw9DHnYKavPy3YvA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=qU8nxyUZghx8U45EN2Y66qrm2WOrQWYXGaOwTl5C-m3NoBTpinQkCGgdubOME6Jz26fL7dEn5rbBpzjTrZQ8r3xVd6uhpQHgjDy-xVQ3HryYaG88iV-udln_sUP89KRbT82I5VOBP6mYlU6ZWCAIg8JmmeSLu2Yril-chJD5HUTkgKT80SS9yoXjX6UBDLu8imXgbpKftS9dbRSWbZrJbFlrY7Nx82MlcRsGtyjcr-TscxaNgzrGEGO6S7to7Dt3ukoFgJSouP7FA1Qe6zyxO3U_T-RJwUv25tDjcbDDAlugTvNpvxt4T461cJWtW9Lq9j1M73Cw9DHnYKavPy3YvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM_vgslklNzwf6GWbovJweCeushGsdl3PAim01K9jIkVoqqBirhhQPX2Bm3-SVtTX_vtOCQpb64ciYG113spCGV1Bbf1E_zwSc0RQlhviZuLBxCKCsSZbJQVNv6jl_6eBWV0uiRXdnBcsF2IbA-k272xFwGke7cS0LZFMXulMihr0Igpn4POmObJtoj_JV78TM6dAwG7ORzER2u-l3lxXENV8WNMjANzCStBeLYJ2w092bvHjAh8_YLtRRQCR9xZZ_X7yRDLDZsptJDVabXVfBDh5HQfNaSK7RdcrT-wZRlIjpNnMTYh0quMFmyxPvm_VrmgZ74qOtx3-_vcmO3ZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7v1fjDzrvUxOeyM3jI2VpVmkYMx1Gg0KueeUJBlypNGavPBkIZqTWCpSBW5pT52zLLCvShrRB7cXIX3dnvckvQ8N2FNoG70L8XNqCvN9UUqkWSLqysvNd-_HdYPN3d1TxHpqa4tcOqAmI_-qTBQ4lSMRTiG6zGq9mnab6JDdMGu9PBztP5bTjSwOp42qE0s4lOIUlAD98kZIlVDMzLjlVNEKNPRWDu8Aa3Qod8g-9XBE3pcRr58tQo_QiPu0Mu_du4mSqYYJSLv7KHuhf77dNIdmWSYaKaZO5akrrwcu7RYM6jU6xNCwg-w6YFF11grMFbC4VvOoucq9oH1Zr1yDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF2beswoo6fpJ0qdniBuWy36R59449I-8aUR19SlSDfI_4UddUL9FgDI_U-6-eraMZPwzGXptzXpNpzp_qPbJbZLAyxudMzlZQS9TbDHWiHLib6Jh_qWkGlxiUiFraSWwcamrwsRhc-Ytd70pRi0ok9QZbYibxTa75b2hm_-cP-JRKpOpoTI92Pxqt6OqhiqPzwCoaFMkgHPB8wVAoHPbqnpGpo52pb33HmzdO_Vs2qxvJI9mxsOJP02YqsQr760-JbpL6CxQSM_JVJNpRvzFcbkpcioL78ChxV-a-R4yFVwzLPjMeyzh-XGz6K1pmiNePjxbWGX579qTIQikGVuSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfpifaBD3UOX7E7B8PEPbky1ms40vGw6VIT7JER994_r7iFehxAF08BO78fv6wXQPs25vSdaC9MUL6dqMO_QRZJ70UtQdJOl8Qg79nRB0J011odYQpXTh2tV3LoAlckgP15NsAShNmti_WkWkhrYN4GyZU0ylpwo106M_4pnM5xHHOXIqCZJ8cJZ63he5oscupX2JVIgSQnsZQNrGJKMA5Owlo9oGPCW1BF1zWGU2X1ZKyYvBaTT6ijk24Jm4RmIvEK1-JAkCjOt9LxIxnUt8sPUF6yjFaaYnjmTFdqSPRVL4jGbKQ1cvo4r5CUlNoBcBraVBpPxViDu1GBk4X3n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=h_WAY8S4HkB34AjTETSAenCzHKNC11teiyewniKWIcjBhYf8nzM6-bjcfdJMO0y1E4jxdqa7lUUNdGjZKs_DRNQ_gygokBxV1kTIc6_-wqqm6HsJ2Kbc2YR1wUC2OSbk_KRwrERDTiNVnNJd_o6oNWc1CYPJWysHfBb29Kc_ZqfUcoZ0CXVTRA91R-QQw7gjihDWtEEeaYjxX1pO4EufPGMdZ2R-35-eHnI1Wd72jCktlDOS7IlfPxSCWV-ZKJ5gZ-DAvTJVnowKBCEmGMMtNbadVlPUDdIpVEkhl8d38S5G2hozKiJdbvtgRcvTsxMgy26IgJyubt11HHZHDjpjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=h_WAY8S4HkB34AjTETSAenCzHKNC11teiyewniKWIcjBhYf8nzM6-bjcfdJMO0y1E4jxdqa7lUUNdGjZKs_DRNQ_gygokBxV1kTIc6_-wqqm6HsJ2Kbc2YR1wUC2OSbk_KRwrERDTiNVnNJd_o6oNWc1CYPJWysHfBb29Kc_ZqfUcoZ0CXVTRA91R-QQw7gjihDWtEEeaYjxX1pO4EufPGMdZ2R-35-eHnI1Wd72jCktlDOS7IlfPxSCWV-ZKJ5gZ-DAvTJVnowKBCEmGMMtNbadVlPUDdIpVEkhl8d38S5G2hozKiJdbvtgRcvTsxMgy26IgJyubt11HHZHDjpjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9c-SaMFHkhAhM0AHHTNkyazm-FfZsWlRv78F7kjf7uafors-u5BheDC-TWRRZtlh6wt8TXt-xSwqWvw6ylk0aicGZNuGlQPqXEKXBl8P0P4IalOP0K3--R0LI2Bs3LMu4jP3D-9aBjcPwb03N6Ok-jPlVbbi9jB_nKUq-LUqoFseiNZFfxn7jKDmgZM0UUa3OmW7VmazlZBCFlws8hc1m6k5newriT4-lglrMUicKXNyjWZ4YESKjuQrzPYpFkuSVm8fQOeScBa_-9Jj12FYr4dnf2aDZK8hdrY_yB5EGNNIZj94HDEuh5asyvToPROIr7-ocYs42JFMctQGLecqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ah9qeaqdWr1GAg7Wnxu9OcJRVfESaD9p1zGFi5TqKZ1Fw-qdf4uP5M0RE5HOriMUs649lhduSmmq_2qHQarZswt7TtqbCIlBseSbCaLYuifhB7NKZw7FzdsQXLSz1Ewq7HJ0VfPATDqAR2L9mLB4gPXuNv7mty22Vx1cnuy8zUmkscH1l16HNeRzrYiZHa0WNgG1v-L7kx917rgmaorpqlCkbq5Fd_j5fSgL0YTWIPlE_4WQhI7SNLvSU5HriEPxrD6zySCt3yG_5JvJ8nLcaGjalqheKzi2pDeunvnVp9GzV6-BZ9dJmTk3gT4-7Asy8eAv5Lyl2MWyWf2Ika6vdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwbZW5oSdldjgWCcNAQTlnOp8W78oQgTN_mzdfrnQDrvj82TmlLPcJn0x03P6lPmFpuCqiVUoGuPTTMoBgTClafJRXBs3hEfeuMKIoyBVqWk6oGRTZM1AwnuMiFIUTDGaBqDWDfCa9JcpfrKSQUAp3btnfo_lrapo8teLEGdWifx7COATuBuzFA1tv0bq4MVgJhaVPD2PJj2BF1PIvZgaqgZSFdAip88Tea3aV9BxGHOOGkDp9PcbwsWKt6kDknllmXIwxaGBh_mpEtLHFVrZnPdfzeNEGef8ehLt7M32xLkBQ6R08vR6IHxO0GDFY2sVLBdk8Xzd6iRZ2VcFTlYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKuloTvTrlyvoiaXfldtAW6BlK9hHQlI9d-efXO2Icdo9QZzYXgQRo3f-lAIksUjw_QMAmY7uUHtkz_p0jvJWPfTmFGoYDtXRc1FKY7b8ebfQRkFfnqVMv2cYPOptP_6ljDkqoM_MVDMLlzN8UA5CwqT31aZXSi1vSG403M3ydNce6-G1IX5EVAYMf9mrca6dO5EO7uFF3747NlOdyTE2UP4GomYFdDnBlnbhUabmCkAbRAnWcm4Gfbr-1IgEpQshwmV1LsPgJ02Sxv6CHH7ZdASiB_5KQwgW90LBeXvT8-6Plfqv4zU_IpRAPlGNN2m1ny2rXyq-mHAOO5HHbUHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
