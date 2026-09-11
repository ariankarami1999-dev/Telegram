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
<img src="https://cdn4.telesco.pe/file/tPVn1E0soenCJ3URMz9I4P3xk9ENxS2_WwisrRXleQ6OGEpRhOCP8nwuGFsXkkRyXXdRDwMvJN7brd7sp8aTZLxvPpzZJSlnD_zefN98_3n5frcE2zUHVXgHxTJvZ4zD8RTtuyZM3-p_z2xX9Jvr3sZ_9uBFZy0KA_yAKW-pehZIgv1ede9VO2aAj-S-rIAloE6v6Z3eMPtHuzDOYfwd0IKZzBXp8sYtEF8U_dukQzAabuKhrxrLcPvkiONx0ADXPE8MZxT9151anlbh07rMlmjkorxJ7CTPhp-6ILsAR-XZDy60lmZHrELn5qCqChVSEO_VtflIki4d4uLtGvm7YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 09:45:45</div>
<hr>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال ۱۴ : سخنگوی IDF، جنرال بریگارد ایفی دافارین، به عمق شبکه تونل حزب‌الله در تپه علی طار در جنوب لبنان وارد شد، پس از اینکه نیروهای ما کنترل عملیاتی تپه و تخریب زیرزمینی زیرساخت‌ها در منطقه را به پایان رساندند.“این شبکه تونلی طی دو دهه ساخته شد، با بودجه و هدایت توسط رژیم تروریستی جمهوری اسلامی”، دافارین از تپه‌ها گفت. به گفته او، زیرساخت‌ها به عنوان یک مجموعه مدیریتی مرکزی و به عنوان “مرکز مغز” واحد بد حزب‌الله در منطقه فعالیت می‌کردند، از جایی که در عملیات شمالی کراس، عملیات عقاب، و همچنین در جریان نبردهای فعلی انجام شد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/22844" target="_blank">📅 07:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935a8bd7c0.mp4?token=jB9VfNJUMGLAUbnEpwLLxc20e_ki6_5WKVIIuwkM9tkojYPDWhFYziiIUXWsDRnzhXLIH2A6Go1g8EA-Hv63ujgCLQt8TPB-w_zWB3pIdhO60FeMNfHxN_3OiwYg84BTPRY8_ZOANh3-RBwGYtMlRQzA3ciSzT6Tx1eWiUdbTbQXoDG0uLe2ma0ePAw2glcIFm6zmpnJ6PE7PI7uHorpT0-GR9eJ1_IgMe5WUG4leMpugq8lW_lkKSr5JRyUeJgheEHI5ItcqZpMiQnpZQGD_8lDhoqXsc6d8WKhYcc7xbRp-Jx7yiSRqmg7ZwG3f97JgdY5gSs9dq6gYLNMZSCUMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935a8bd7c0.mp4?token=jB9VfNJUMGLAUbnEpwLLxc20e_ki6_5WKVIIuwkM9tkojYPDWhFYziiIUXWsDRnzhXLIH2A6Go1g8EA-Hv63ujgCLQt8TPB-w_zWB3pIdhO60FeMNfHxN_3OiwYg84BTPRY8_ZOANh3-RBwGYtMlRQzA3ciSzT6Tx1eWiUdbTbQXoDG0uLe2ma0ePAw2glcIFm6zmpnJ6PE7PI7uHorpT0-GR9eJ1_IgMe5WUG4leMpugq8lW_lkKSr5JRyUeJgheEHI5ItcqZpMiQnpZQGD_8lDhoqXsc6d8WKhYcc7xbRp-Jx7yiSRqmg7ZwG3f97JgdY5gSs9dq6gYLNMZSCUMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ شامگاه (صبح جمعه به وقت ایران)، در سخنرانی خود در شب دوم و پایانی مجمع ملی جمهوری‌خواهان در شهر دالاس ایالت تگزاس، به اقدام نظامی برای جلوگیری از هسته‌ای شدن جمهوری اسلامی و تنگه هرمز اشاره کرد. (دوبله)
@WarRoom</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/22843" target="_blank">📅 06:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac2ec14c.mp4?token=v5pCdOUnYvmuwazNZejcZ_4Dlttee35LHij_rsc6_k5y0Uqaoovz-K49mVvTWq4PvwNXGyuZkgWTL_jclWzZBe3Jv74YkN3ZlHxXGiO1keckGzL-sOa6l_x6-cMYcKzDMqhwY0aI0Ps4M7RlvQVyo1HWmAoGuhOFeOGSRRfPxsjlrE5HLupOKZ959vZjqenE-ddRnhfjSwLAZ4bNSXcx9nCBa0P1WqXDrVWh1fH-wLjeImuLGU3heQG3YF4mEd9llO2F3ARPKnrKk9HyQGIV7Ud0gAHJEEiw-6h0ruTDXZLhzlCfT9gpyT9-WyP2WtAvrE2IvJLiYzNt6Ai1jqw6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac2ec14c.mp4?token=v5pCdOUnYvmuwazNZejcZ_4Dlttee35LHij_rsc6_k5y0Uqaoovz-K49mVvTWq4PvwNXGyuZkgWTL_jclWzZBe3Jv74YkN3ZlHxXGiO1keckGzL-sOa6l_x6-cMYcKzDMqhwY0aI0Ps4M7RlvQVyo1HWmAoGuhOFeOGSRRfPxsjlrE5HLupOKZ959vZjqenE-ddRnhfjSwLAZ4bNSXcx9nCBa0P1WqXDrVWh1fH-wLjeImuLGU3heQG3YF4mEd9llO2F3ARPKnrKk9HyQGIV7Ud0gAHJEEiw-6h0ruTDXZLhzlCfT9gpyT9-WyP2WtAvrE2IvJLiYzNt6Ai1jqw6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکی
.
خدایا کمکم کند.
جمعیت :
خدایا کمکم کند
اوه! حالا می‌دانم. حالا، می‌گویم که تقریباً همه… می‌دانید اگر رأی ندهید چه اتفاقی می‌افتد؟
به جهنم می‌روید.
این را می‌دانید، نه؟ باشه؟ به جهنم می‌روید. و من نمی‌خواهم چنین اتفاقی برای شما بیفتد، پس لطفاً بروید و رأی بدهید. چون باهمدیگر…
@WarRoom</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/22842" target="_blank">📅 06:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe1f11f1d.mp4?token=cUm6x2Js2sh7MURfzPcT7bmP4-qjYzwUaLcqjhPhdDYrXLiMFzJV64ww4VFW8GmXsAftyDmHjZ3wqEq0PnHjQq-P4AmgWd2-UmuuQguTruaC6mDA66rRRaCJNr9uP-D60TRNi1S6pMqmlGav6xAQj9FULuNTrQMjbcrcigEABsn26D_nH9HYLAwy65-NI-fStaEddsKQcVp64WAG74m0Q2S_tPqe0hIHhx-bvaKqQNUFCaXa-TlCEy2Rey6QAtVYaPajRuOX4PuMzYb4ydTk6Cs2r3SNy9ot6wGBYjUsgMAUK0m8UHLLmiDEpigVqInO1FnaUv8FTHg_2oQTAHQ7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe1f11f1d.mp4?token=cUm6x2Js2sh7MURfzPcT7bmP4-qjYzwUaLcqjhPhdDYrXLiMFzJV64ww4VFW8GmXsAftyDmHjZ3wqEq0PnHjQq-P4AmgWd2-UmuuQguTruaC6mDA66rRRaCJNr9uP-D60TRNi1S6pMqmlGav6xAQj9FULuNTrQMjbcrcigEABsn26D_nH9HYLAwy65-NI-fStaEddsKQcVp64WAG74m0Q2S_tPqe0hIHhx-bvaKqQNUFCaXa-TlCEy2Rey6QAtVYaPajRuOX4PuMzYb4ydTk6Cs2r3SNy9ot6wGBYjUsgMAUK0m8UHLLmiDEpigVqInO1FnaUv8FTHg_2oQTAHQ7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس:
اگر ما وارد ماجرای ایران نشده بودیم، شما الان می‌توانستید با خیال راحت به سمت پیروزی در انتخابات میان‌دوره‌ای حرکت کنید؛ با ۲۲۵ کرسی.
ترامپ:
بله، خب، شما این را نمی‌دانید.
مجری فاکس:
آیا پشیمانی‌ای دارید؟
ترامپ:
نه. من اصلاً به کلمه «پشیمانی» اعتقاد ندارم. البته آدم همیشه می‌تواند کمی خودش را مورد سؤال قرار بدهد و درباره تصمیماتش فکر کند، و مردم هم از من این سؤال را پرسیده‌اند. اگر قرار بود دوباره همان تصمیم را بگیرم،
دقیقاً همان کاری را می‌کردم که انجام دادم. توانایی هسته‌ای آنها را از بین بردم.
@WarRoom</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/22841" target="_blank">📅 06:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb5e8b4ba.mp4?token=XpHWLZQmbqrg-ruE5P__plu7SGg7Nt3Zhju0TmNydZNlbw_oFBuypks3NHeUZdNafVBqqm5Mnv0iCrAmngOV3VBZ9IqPzak3jJuoKWZoQv8IE4JaFVsgwYn0NABBXP5GiOQq3n0sDRFNkAMzLOH61w-nV6uHZ3Aj39iPGJLprDXus_WGtPhyZHBrYsZq3m_ANU-sv55wGClJjaZA_vTZBNvXj8JPQZjsWfB68t57MvsSqlAHU95kHAsowpxjl0LwZRsSDSEWDy8oRFgz0CXBVHMN3993OxJjnkYUsNclYPQkFP8OVHL5lf6QW7t2ZpjkE8OyH_U1DbGS2y1MyND5IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb5e8b4ba.mp4?token=XpHWLZQmbqrg-ruE5P__plu7SGg7Nt3Zhju0TmNydZNlbw_oFBuypks3NHeUZdNafVBqqm5Mnv0iCrAmngOV3VBZ9IqPzak3jJuoKWZoQv8IE4JaFVsgwYn0NABBXP5GiOQq3n0sDRFNkAMzLOH61w-nV6uHZ3Aj39iPGJLprDXus_WGtPhyZHBrYsZq3m_ANU-sv55wGClJjaZA_vTZBNvXj8JPQZjsWfB68t57MvsSqlAHU95kHAsowpxjl0LwZRsSDSEWDy8oRFgz0CXBVHMN3993OxJjnkYUsNclYPQkFP8OVHL5lf6QW7t2ZpjkE8OyH_U1DbGS2y1MyND5IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران سلاح هسته‌ای داشت، ما تماس می‌گرفتیم و می‌گفتیم: "قربان، آیا می‌توانیم با هم ملاقات کنیم؟"
ما با آنها بسیار متفاوت برخورد می‌کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/22840" target="_blank">📅 06:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbf0f4f2b3.mp4?token=FUFmzxVKcLmPAMFE9d5nfc2odzFyNmtrdO9BY4wJwN7gx3IfInlns-IF3Tz9BXHHkpebpLS18MJMsVrzFnKuEgTO9uZfQNex6bE9nqE5Uq3g_DzYHDD_yGXG-9y1RB8Odz8qFE_saTZ1oJ3loO7ELHy7FYlIrruVaEPWB-uVpeXPE8JGR90hgnYmov8p0tWTii_iExba3efQB8ZLwY7cTaIdYi-73DOlu4zdSiF6mK5wF3hge7cEYAFMCEJT5DNzgz5Aj65FAfw9NycHOy0iprdcxFUBtCaf1KBWJupZPxzb_heOvFmyk4AzY8BaT1Q4KjZ5HFUXwT9Z_mKB4In428AXCVj_n2GuK8iilvhCaSFk2aid13cCkeeXi40lNL56ZJEH6riJUx46ATQj47yZSH-a0HqcIlGkbqm1umB0_Bm6l-3-Ez9tnQNnb2b6HgiQ-3-fidJB1nebufXRrVZA51WAmVvnIBir4rd4JKbxZexlruXFh3D7-ynMHv5FYB_UaD2E_Fski9xx9LyxuQb52cPg-9THzn9gfRyEzQKyIrnE_1Ad52-6HNy09EvB_FIWcVz_Eh9fw9Rsayf8_RRWz9-qJTRGBv2_C5cKGqidYpnDFz0Kw3W1c7eF2WevvateX3pMFel9MZhO_XQN2gqeRYhCcF-5qKDoBy-1aJaaoYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbf0f4f2b3.mp4?token=FUFmzxVKcLmPAMFE9d5nfc2odzFyNmtrdO9BY4wJwN7gx3IfInlns-IF3Tz9BXHHkpebpLS18MJMsVrzFnKuEgTO9uZfQNex6bE9nqE5Uq3g_DzYHDD_yGXG-9y1RB8Odz8qFE_saTZ1oJ3loO7ELHy7FYlIrruVaEPWB-uVpeXPE8JGR90hgnYmov8p0tWTii_iExba3efQB8ZLwY7cTaIdYi-73DOlu4zdSiF6mK5wF3hge7cEYAFMCEJT5DNzgz5Aj65FAfw9NycHOy0iprdcxFUBtCaf1KBWJupZPxzb_heOvFmyk4AzY8BaT1Q4KjZ5HFUXwT9Z_mKB4In428AXCVj_n2GuK8iilvhCaSFk2aid13cCkeeXi40lNL56ZJEH6riJUx46ATQj47yZSH-a0HqcIlGkbqm1umB0_Bm6l-3-Ez9tnQNnb2b6HgiQ-3-fidJB1nebufXRrVZA51WAmVvnIBir4rd4JKbxZexlruXFh3D7-ynMHv5FYB_UaD2E_Fski9xx9LyxuQb52cPg-9THzn9gfRyEzQKyIrnE_1Ad52-6HNy09EvB_FIWcVz_Eh9fw9Rsayf8_RRWz9-qJTRGBv2_C5cKGqidYpnDFz0Kw3W1c7eF2WevvateX3pMFel9MZhO_XQN2gqeRYhCcF-5qKDoBy-1aJaaoYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه دعوا شد ، صدای‌چند انفجار @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/22839" target="_blank">📅 06:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c36615a19.mp4?token=Fe5_qSfA7OjNB7K3pv_5ifsfmwxFikK3j-zsX6OomHZdb_Zj1vwVB4-GJ3R2AmbNHNeuk3ZiqLBGtAf5ni28OFV83UbuBDd0mbsPGPEVK4f2l5c4D5eDin3ZQPtoqw8ynlMX6aUlXaDfrHT6GVMXEIn3MVJcWiKMbNkJM30OKkmXsuCdLR1xM-hjvaSbyuVbtw9uvGLlCfKXTnJQedQd-6haHr0751iP3Sl9-aY2rkg1zdCXdahMyqOaQwPQ31GIN1hCaCnfzJZr4OvRUO-2r_bEtVWE27GedmRakpvCj_csdf-DeLLJXk6EW6d9yPkHUtidL19xxm_h23bARFU2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c36615a19.mp4?token=Fe5_qSfA7OjNB7K3pv_5ifsfmwxFikK3j-zsX6OomHZdb_Zj1vwVB4-GJ3R2AmbNHNeuk3ZiqLBGtAf5ni28OFV83UbuBDd0mbsPGPEVK4f2l5c4D5eDin3ZQPtoqw8ynlMX6aUlXaDfrHT6GVMXEIn3MVJcWiKMbNkJM30OKkmXsuCdLR1xM-hjvaSbyuVbtw9uvGLlCfKXTnJQedQd-6haHr0751iP3Sl9-aY2rkg1zdCXdahMyqOaQwPQ31GIN1hCaCnfzJZr4OvRUO-2r_bEtVWE27GedmRakpvCj_csdf-DeLLJXk6EW6d9yPkHUtidL19xxm_h23bARFU2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس نیوز: چگونه ایران می‌تواند موشک‌ها را پرتاب کند، در حالی که ما آن‌ها را نابود کرده‌ایم؟
ترامپ: آن‌ها همیشه می‌توانند موشک‌ها را پرتاب کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم دارند. البته ما آن‌ها را سرنگون کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/22838" target="_blank">📅 06:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22837">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI3VEmJPClTgqtoo99SsbWOatYP_L3o3XnyHolCbqklUjj717pM1OtJoBG63vdOMiXiMfTu5d_vMdzGkQHk7xYKgggstmgkfNTsT0un00NxGkxKslp4HVw4q6OxmcvSNa6vdbGXyvHGVLXQ-V9eDvCbDUFYtcTgS2cpXa7HrDEVE6upbdcr2jb8svf9RISGGW05_2FHOqgu4xouyETla5MB64BuckCBXE0fI3gBFPzFFji2sF07SXjxK3CZhT0GzP-tY1StuTFkuvm9rtMU3I_JVXRskpRuTQJ3V-215TJlTrGNl-bC7O5lfw7pPjgo-GuE2-BJYB-e37tvVrtMa3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا : دو شناور در تنگه هرمز، در حدود ۴ مایل دریایی غرب «خصب» عمان، مورد اصابت قرار گرفته‌اند.
یکی از شناورها هم‌اکنون در آتش می‌سوزد، در حالی که وضعیت شناور دوم همچنان نامشخص است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22837" target="_blank">📅 00:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رسانه های اسرائیلی : ده ها جسد تروریست های حزب الله در تونل ها پیدا شد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22836" target="_blank">📅 00:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو : امشب بزرگ‌ترین پایگاه برون‌مرزی ایران یعنی تونل‌های «علی طاهر» در لبنان را منهدم کردیم. مأموریت با موفقیت به پایان رسید. سال نو یهودی مبارک! @WarRoom یاشار : آتیش بازی سال نو به سبک بی بی
💥
😂</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22835" target="_blank">📅 00:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22834">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b3b329e59.mp4?token=KQVHAsqz-jh1BO0QaCQJXywAPYZalCsHUwmPUb1QHXaTuVP-oHf02BY_2cVhDMh-DRpvSbJPCiBOyWLa_kjke4YWpNoUhD28e_Ty7YgOR7DuOa5vKmM2w5dAEMA1fNcIcEzBBtQ3RxnfIY_0d2-H4ImSHYRG4rVOpOhihry0NnNtcFVks4sjt8AfOoBvocrTB5HpqoACpo0Y8dqw0OddIqTp83GU-LyZlzFqB7N7ABO1IkSc0rkWI6bviBkReXw8LTvs3Qd5OLK13tcx8yBUWQzhbv9th10igKY6T2c_F4saCRjoSL1rp_83Dfkq4FcRySUmYGFuZkS1tDOYUs24bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b3b329e59.mp4?token=KQVHAsqz-jh1BO0QaCQJXywAPYZalCsHUwmPUb1QHXaTuVP-oHf02BY_2cVhDMh-DRpvSbJPCiBOyWLa_kjke4YWpNoUhD28e_Ty7YgOR7DuOa5vKmM2w5dAEMA1fNcIcEzBBtQ3RxnfIY_0d2-H4ImSHYRG4rVOpOhihry0NnNtcFVks4sjt8AfOoBvocrTB5HpqoACpo0Y8dqw0OddIqTp83GU-LyZlzFqB7N7ABO1IkSc0rkWI6bviBkReXw8LTvs3Qd5OLK13tcx8yBUWQzhbv9th10igKY6T2c_F4saCRjoSL1rp_83Dfkq4FcRySUmYGFuZkS1tDOYUs24bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : امشب بزرگ‌ترین پایگاه برون‌مرزی ایران یعنی تونل‌های «علی طاهر» در لبنان را منهدم کردیم.
مأموریت با موفقیت به پایان رسید. سال نو یهودی مبارک!
@WarRoom
یاشار : آتیش بازی سال نو به سبک بی بی
💥
😂</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22834" target="_blank">📅 00:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیویورک تایمز: پشت پرده ونس ترامپ را دور زد؛ مستقیم از فرماندهان ارتش آمریکا ارزیابی های دقیق از جنگ گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22833" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا: آمریکا در چارچوب «عملیات طرد اقتصادی ایران»
۱۴ فرد و ۵ نهاد
مرتبط با شبکه‌های نیابتی پشتیبان
کتائب حزب‌الله، حزب‌الله لبنان، نیروی قدس سپاه و شبکه‌های دور زدن تحریم‌های ایران
را تحریم کرد. افراد تحریم‌شده شامل
علی حسن فرحان اللامی، حسین احمد حسین الضحیباوی، محمد امین فاضل علی الشیخلی، کرار محمد قاسم الحریشاوی، عباس جواد کاظم التمیمی، عبدالله ناظم لعیبی العامری، خلدون ناصر مریوش العباده، مجید علی‌اکبر نامدار المندلاوی، عبدالحسن علی ا. نامدار المندلاوی، حسین ابراهیم، عبدالله همیه، غیث حسین وهبه، مروت جمیل زهرالدین و امیر المکانسی
هستند. پنج نهاد نیز شامل
Al-Brouj For General Contracting، Ain Al-Iraq، Shams & Bahr Trading Company، YIM Exchange و Gold Pro SARL
است. آمریکا مدعی است
شرکت شمس و بحر مستقر در دبی
در انتقال میلیون‌ها دلار از عراق به ایران نقش داشته و برخی افراد این شبکه نیز در انتقال منابع نیروی قدس به حزب‌الله فعالیت داشته‌اند. همزمان، دفتر کنترل دارایی‌های خارجی آمریکا اعلام کرد روند
رد اکثریت درخواست‌های معوق برای مجوزهای اختصاصی مرتبط با ایران
را آغاز کرده است. همچنین OFAC از
تسویه یک پرونده به ارزش ۱ میلیون و ۴۲۷ هزار و ۲۳۰ دلار
بابت ۳۹ مورد نقض تحریم‌های ایران خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22832" target="_blank">📅 23:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed5786f00.mp4?token=nqQzhbuSyNVM-I0cl7ERht_A3ojjvUpWAjaGaCrOxiWlrRbj5NqkFj92QnM9-jJp0musdzZh31z2ljAHFa-B4WrS0GOu4JbIBmC8BW3prvzXL5-OgRkzdyMRx5FWzkxQ-652W6jaT7lXYP1HtRAPgI8MvRBbiSz2k7Ixp-dApYXIuYk5SGX20qrohFMZpBCFvUPdowF5Gmugk2KgoiwxWt-rStKtdXJpJDe8GYAAFn62EMz8ZH1od4pk9vUZj-TmgHJlKHSqRWv-sY1ULgLtQQb6Uydq8rwTzsqFoqbgYaxzqPcTDRfw7PUacn_Fnl2uq4GaOwpeo_n8Ud_bseXp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed5786f00.mp4?token=nqQzhbuSyNVM-I0cl7ERht_A3ojjvUpWAjaGaCrOxiWlrRbj5NqkFj92QnM9-jJp0musdzZh31z2ljAHFa-B4WrS0GOu4JbIBmC8BW3prvzXL5-OgRkzdyMRx5FWzkxQ-652W6jaT7lXYP1HtRAPgI8MvRBbiSz2k7Ixp-dApYXIuYk5SGX20qrohFMZpBCFvUPdowF5Gmugk2KgoiwxWt-rStKtdXJpJDe8GYAAFn62EMz8ZH1od4pk9vUZj-TmgHJlKHSqRWv-sY1ULgLtQQb6Uydq8rwTzsqFoqbgYaxzqPcTDRfw7PUacn_Fnl2uq4GaOwpeo_n8Ud_bseXp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه انفجار از دید سربازان اسرائیلی
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22831" target="_blank">📅 23:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یک منبع آمریکایی به شبکه CNN گفت:
تخمین زده می‌شود که صدها نفر از نیروهای سپاه پاسداران انقلاب اسلامی در داخل یمن حضور دارند تا به حوثی‌ها در مسدود کردن تنگه باب‌المندب کمک کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22830" target="_blank">📅 23:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزارت دفاع : به زودی گوشه‌ای از کوه‌ یخ صنایع دفاعی ایران را می‌بینید.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22829" target="_blank">📅 23:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/045dcbc8ef.mp4?token=Au9QE3LZplQwFosJauwGPr1HM0KS93cuuu0ssDBhwqP9oCJi3UJjyM39DN-SuCosfNi_V-30u7WiQqswVPjbxYL5OcB7Vn3J2zVrDOLDs5jo0LS_UEP-2IxaxTmTukBZGGN_6sR16rAamOFun-c9D1yAMLIUom3-WwbiVgXoiLvjHyqsFZ7M5843JWf3WW33OFnWVCtrZMF7DDl-c5iJtHg59v-SSPwbU-KaGDHONUvvmzuJzU-BvgDV-9U9cCutZIj-XvoXIub6FQ9hXzWm6o21KElWVG07FdHgan_UCWhnkx2Fi5qUF9RipPOlpV2s2I0tNnA6c2ya3F6Lo_j7pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/045dcbc8ef.mp4?token=Au9QE3LZplQwFosJauwGPr1HM0KS93cuuu0ssDBhwqP9oCJi3UJjyM39DN-SuCosfNi_V-30u7WiQqswVPjbxYL5OcB7Vn3J2zVrDOLDs5jo0LS_UEP-2IxaxTmTukBZGGN_6sR16rAamOFun-c9D1yAMLIUom3-WwbiVgXoiLvjHyqsFZ7M5843JWf3WW33OFnWVCtrZMF7DDl-c5iJtHg59v-SSPwbU-KaGDHONUvvmzuJzU-BvgDV-9U9cCutZIj-XvoXIub6FQ9hXzWm6o21KElWVG07FdHgan_UCWhnkx2Fi5qUF9RipPOlpV2s2I0tNnA6c2ya3F6Lo_j7pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لرزش موج انفجار حاصل شده از انفجار تپه‌های علی طاهر از دوربین مداربسته یک خانه ،بنا بر گزارشها، این زلزله ۴.۱ ریشتر گزارش شده.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22828" target="_blank">📅 23:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نیروی هوایی اسرائیل شهرک‌های «المنصوری» و «زبقین» در جنوب لبنان را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22827" target="_blank">📅 22:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">به‌صدا درآمدن آژیرهای خطر در شهرهای ابها و خمیس مشیط عربستان
سازمان دفاع مدنی عربستان سعودی از فعال‌سازی سامانه هشدار زودهنگام در برخی مناطق جنوبی این کشور خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22826" target="_blank">📅 22:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وحیدی: خدای ما خدای زنده است، خدای غربی ها خدای مرده است
.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22825" target="_blank">📅 22:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تلگراف: ایران برای نخستین‌بار موشک‌های مجهز به جستجوگرهای الکترواپتیکی را علیه ناوهای آمریکایی به کار گرفت:
مقام‌های آمریکایی مدعی شده‌اند ایران در حملات اخیر به ناوهای آمریکا از موشک‌های مجهز به
حسگرهای اپتیکی
استفاده کرده است که با بهره‌گیری از دوربین و حسگرهای نوری می‌توانند اهداف متحرک را در مرحله پایانی پرواز شناسایی و ردیابی کنند. ایران پیش‌تر موشک بالستیک میان‌برد
قاسم بصیر
را معرفی کرده بود که طبق گزارش‌ها به چنین سامانه‌ای مجهز است؛ با این حال،
استفاده قطعی از قاسم بصیر در حملات اخیر هنوز تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22824" target="_blank">📅 22:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22823" target="_blank">📅 22:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این انفجار یک زلزله ۴.۱ ریشتری ایجاد کرد !
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22822" target="_blank">📅 22:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">توییت جدید سفارت ایران : سرآشپز رضائی در حال پخت و پز است. @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22821" target="_blank">📅 22:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش اسرائیل: کل سامانه پدافند هوایی اسرائیل در حالت آماده‌باش کامل قرار دارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22820" target="_blank">📅 22:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDmmOK8coYv5yAbEH5-30oJSBvK6XRhXeb9Wz0fTELRWp0VBLS9gYyBVvQth3IVFb-RKffCqgmkY1kmx6oP9-FI2uanVOHxHLjUYzFv1Dzu0Dtk8w5cAUGmt6DayIuOoZ4jEcDv29WJuvFRNu9SE-b2TswO9TFS9hPa_SUbv1Lzj550_seFF8rHBZ7TtONhlUD9V46djNg_r4DISajA3SHYzyc8DcoobxlcM7rBB2TBT8NYvkOmzra3RnQHqZlPqpvjuJBC9_xvmE5OtmEIqB2tCytBp6m8czsVYmWKAhN-CGUzd8voK7VeCTZZkpqbJjW6CGT4W3OgkbpmTEiks-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان رفتیم مرحله بعدی‌کمر بند ها رو بیندید ، آیا رژیم اشغالگر جمهوری اسلامی جواب میده ؟</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22819" target="_blank">📅 22:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22818" target="_blank">📅 22:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بیانیه مشترک نخست‌وزیر و وزیر دفاع اسرائیل درباره ارتفاعات علی‌الطاهر:
بنیامین نتانیاهو و اسرائیل کاتز: «به دستور نخست‌وزیر و وزیر دفاع، نیروهای ارتش اسرائیل
زیرساخت‌های زیرزمینی حزب‌الله در منطقه علی‌الطاهر را منهدم کردند
و ایجاد منطقه امن در جنوب لبنان به پایان رسیده است. این زیرساخت‌ها که طی دو دهه با بودجه و برنامه‌ریزی ایران ساخته شده بودند، قرار بود به‌عنوان پایگاهی برای
تسخیر الجلیل و دیدبانی و شلیک به سمت متولا و کریات شمونا
استفاده شوند. با نابودی آنها، ارتش اسرائیل به
کنترل عملیاتی کامل منطقه علی‌الطاهر، در سطح زمین و زیر زمین،
دست یافته است. نیروهای ارتش در این منطقه باقی خواهند ماند، از بازگشت حزب‌الله جلوگیری و به نابودی زیرساخت‌های تروریستی آن ادامه خواهند داد. اسرائیل همچنین اعلام کرد هرگونه تلاش برای آسیب‌رساندن به غیرنظامیان یا نیروهای اسرائیلی را
با قاطعیت پاسخ خواهد داد.
»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22817" target="_blank">📅 22:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22816">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22816" target="_blank">📅 22:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">استاد بزرگ شطرج، نتانیاهو : نیروهای ما عملیات خود را در تپه علی الطاهر در جنوب لبنان آغاز کرده‌اند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22815" target="_blank">📅 22:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595c3ab294.mp4?token=SJ1aMg59GfcluuJJLezCUcdykivd0Oh84X0HCftlog7uX1nKgo-bQRa2Sq1MCZ3dGhB3mbzyUpXfPfdiOOVn21io5n158vrxsI6CcKMTkvqiSiOYAaJm2qLt92JhB4bWaFmoQQA9jw9cCocSU75L5ObOJFh1jK-rlLE1wbaFxGhWltMGZswvmzydHeB9wygNh6XEl49eFW5S4suwouE_q86BKmDH8EfQ_z02DFjd_lzXpHNf-DzSNbNuH4X62065zn5_hu9rhFPmzIfVbuYOixoMqGO6_UZi3gcgv45xpmPBBNVgeen-fDDys5Z6Vke9tjyS-QNlOVcTEGQh4gryUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595c3ab294.mp4?token=SJ1aMg59GfcluuJJLezCUcdykivd0Oh84X0HCftlog7uX1nKgo-bQRa2Sq1MCZ3dGhB3mbzyUpXfPfdiOOVn21io5n158vrxsI6CcKMTkvqiSiOYAaJm2qLt92JhB4bWaFmoQQA9jw9cCocSU75L5ObOJFh1jK-rlLE1wbaFxGhWltMGZswvmzydHeB9wygNh6XEl49eFW5S4suwouE_q86BKmDH8EfQ_z02DFjd_lzXpHNf-DzSNbNuH4X62065zn5_hu9rhFPmzIfVbuYOixoMqGO6_UZi3gcgv45xpmPBBNVgeen-fDDys5Z6Vke9tjyS-QNlOVcTEGQh4gryUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل اعلام کرده است که بیش از ۱۱۰۰ تن مواد منفجره برای تخریب زیرساخت‌های تونل‌های واقع در زیر منطقه "علی طاهر" در جنوب لبنان استفاده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22814" target="_blank">📅 22:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/646f9ab553.mp4?token=Pc8lD0mxBGdWSpB8umVER7KFk7OG_YaQnJHAtGgOBpkhwrc1diw7DfiCviHKaLVDBiNdJYtf5MWpMzX9rdcXBULC-YZnuImuXITfqqn4bBP8cF1Jb1mV88Ymym9A4k-afNGjzL1yAhoWgCG3ZzNR8TZBejFg-sIAhlY1AsL2Zy1W1-IGfmDl_gQQJm3z484qpuJoAl6NZd2P8ldH3G9viC_Ostf6VCYjOai2_WFQhlmXYf5NcA3lW4EjC0wQPjiLuhbHkJ1zYTqzVkZsp44ABjMEinDUP08AYI6N3QyBgpMPpbjRYBwteE28SLzOu_Mm8aCAOapz8evcO3nbsyd7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/646f9ab553.mp4?token=Pc8lD0mxBGdWSpB8umVER7KFk7OG_YaQnJHAtGgOBpkhwrc1diw7DfiCviHKaLVDBiNdJYtf5MWpMzX9rdcXBULC-YZnuImuXITfqqn4bBP8cF1Jb1mV88Ymym9A4k-afNGjzL1yAhoWgCG3ZzNR8TZBejFg-sIAhlY1AsL2Zy1W1-IGfmDl_gQQJm3z484qpuJoAl6NZd2P8ldH3G9viC_Ostf6VCYjOai2_WFQhlmXYf5NcA3lW4EjC0wQPjiLuhbHkJ1zYTqzVkZsp44ABjMEinDUP08AYI6N3QyBgpMPpbjRYBwteE28SLzOu_Mm8aCAOapz8evcO3nbsyd7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل: آیا ایران واکنش نشان خواهد داد؟ پس از ماه‌ها عملیات، نیروهای اسرائیلی کنترل ارتفاعات علی طاهر را تکمیل و زیرساخت‌های تروریستی این منطقه را منهدم کردند و اکنون برای مرحله بعدی آماده می‌شوند. همزمان، با نزدیک شدن به سال نو یهودی، سطح آماده‌باش…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22813" target="_blank">📅 21:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رادیو ارتش اسرائیل: فرماندهی منطقه شمالی ارتش اسرائیل، دقایقی پیش شبکه تونل‌ها را در رشته کوه‌های علی طاهر در جنوب لبنان تخریب کرد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22812" target="_blank">📅 21:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22811">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ada8c06b7.mp4?token=ExpnjyylfWqVmv7SaWl3phUOti4Sfv6kUMk140rCH4MbgBmkpPqZHbekC-Gy2CQ-DoGDKHckA6pEsFwzg8bvTx1FiJx3AGKvec12Ckne7Tgh9FuZQZStWJgp_Wv8WlEYsB91iBdstR3hh-JZeR9wTOe7ki2UT54NcyDNAcoXwlqMOBmTMZyD9YFKTGiDV1CEFfCvKhBSODQysAEzIJoz3QvRX71fYG0lfG7Q519bHLNdsYD_A86lXvmv9GZUxOhxB7cqNyEZL-qbYwKOBNLbvLxJdnZvTUrzXBS4jKBycN5AtuLm3LD4GYJ4y3nd_Z7jbp5y9deSDlNhtqfHO9uIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ada8c06b7.mp4?token=ExpnjyylfWqVmv7SaWl3phUOti4Sfv6kUMk140rCH4MbgBmkpPqZHbekC-Gy2CQ-DoGDKHckA6pEsFwzg8bvTx1FiJx3AGKvec12Ckne7Tgh9FuZQZStWJgp_Wv8WlEYsB91iBdstR3hh-JZeR9wTOe7ki2UT54NcyDNAcoXwlqMOBmTMZyD9YFKTGiDV1CEFfCvKhBSODQysAEzIJoz3QvRX71fYG0lfG7Q519bHLNdsYD_A86lXvmv9GZUxOhxB7cqNyEZL-qbYwKOBNLbvLxJdnZvTUrzXBS4jKBycN5AtuLm3LD4GYJ4y3nd_Z7jbp5y9deSDlNhtqfHO9uIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی تایر ترکید
🤣
با ترکیدن یک تایر به دنیا آمد و با ترکیدن یک تایر از دنیا رفت
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22811" target="_blank">📅 21:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22810" target="_blank">📅 21:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوست بیلیونرم ترجمه خبر زنده : ارتش اسرائیل عملیات انفجار تپه «علی طاهر» در جنوب لبنان را آغاز کرده است.
صدای انفجارهای بسیار شدیدی شنیده شده است.
برخی از ساکنان جنوب لبنان از وقوع زمین‌لرزه خبر می‌دهند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22809" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کانال ۱۴ اسرائیل: آیا ایران واکنش نشان خواهد داد؟ پس از ماه‌ها عملیات، نیروهای اسرائیلی کنترل ارتفاعات علی طاهر را تکمیل و زیرساخت‌های تروریستی این منطقه را منهدم کردند و اکنون برای مرحله بعدی آماده می‌شوند. همزمان، با نزدیک شدن به سال نو یهودی، سطح آماده‌باش…</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22808" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۴ اسرائیل: آیا ایران واکنش نشان خواهد داد؟ پس از ماه‌ها عملیات، نیروهای اسرائیلی
کنترل ارتفاعات علی طاهر را تکمیل و زیرساخت‌های تروریستی این منطقه را منهدم کردند
و اکنون برای مرحله بعدی آماده می‌شوند. همزمان، با نزدیک شدن به سال نو یهودی، سطح آماده‌باش اسرائیل در تمامی جبهه‌ها، از ایران و لبنان تا غزه و کرانه باختری، به بالاترین سطح رسیده است. در همین حال، مقام‌های ارشد اسرائیلی هشدار داده‌اند که
اگر ایران حمله کند، اسرائیل وارد یک جنگ گسترده خواهد شد و پاسخ آن محدود نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22807" target="_blank">📅 21:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22806">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ به نیوزنیشن : هیچ هواپیما نظامی آمریکا در حمله موشکی جمهوری اسلامی به اردن آسیب ندید
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22806" target="_blank">📅 21:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ به نیوزنیشن:
اتش بس با این رژیم برای من تمام شده انها آشغال و تفاله هستند
پایان رژیم ایران نزدیک است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22805" target="_blank">📅 21:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211b7eee90.mp4?token=oIuScOvE2M1VtqFb4UrIIHmhEcDwq3zvlKlgVfdImi8lVLEfL1PCqP_cuh-VXpibVQegIFCq8tcL0Mg-3ZpNnby51pv-ZLJ6kTjo9ZdbK941bTys8R95rAFcvN5K5-81hwCE64be924_pWkuNUeNeMcakYhQ-ZoxRtDMygCYAXJgNCEPYRCgWiMMY4vHos8GdbgqJBZCEdCGHVezvbr_52MKskqdLUULj3_vnQLYVBqjzuW2vfiB6zyMrZHkjnn1WwS9D5auMJx5iqa1fJJCtcWZJh-REirzncwh174LQ0uYpLdntsZUt1YF8OhzWSWbM8fb8ftrBJrNbs12rT9cRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211b7eee90.mp4?token=oIuScOvE2M1VtqFb4UrIIHmhEcDwq3zvlKlgVfdImi8lVLEfL1PCqP_cuh-VXpibVQegIFCq8tcL0Mg-3ZpNnby51pv-ZLJ6kTjo9ZdbK941bTys8R95rAFcvN5K5-81hwCE64be924_pWkuNUeNeMcakYhQ-ZoxRtDMygCYAXJgNCEPYRCgWiMMY4vHos8GdbgqJBZCEdCGHVezvbr_52MKskqdLUULj3_vnQLYVBqjzuW2vfiB6zyMrZHkjnn1WwS9D5auMJx5iqa1fJJCtcWZJh-REirzncwh174LQ0uYpLdntsZUt1YF8OhzWSWbM8fb8ftrBJrNbs12rT9cRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: رئیس‌جمهور ترامپ امشب اعلام کرد که ایران در حال تسلیح مجدد خود با سلاح‌های هسته‌ای است. این درست است. پس از آنکه توانایی فوری آنها برای تولید بمب‌های هسته‌ای را ویران کردیم، آنها دوباره در حال تلاش هستند. من اینجا، در کنار دیوار غربی، پیش از روش هشانا به شما اطمینان می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران سلاح هسته‌ای نخواهد داشت. همزمان، ما به محور ایران ضربه می‌زنیم؛ نه‌تنها به‌شدت در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات بوفورت را ویران کردیم و اکنون با ارتفاعات علی طاهر مقابله می‌کنیم. چیزهای بیشتری در راه است
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22804" target="_blank">📅 21:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e85bc0602.mp4?token=cCgnc_chWdxp_UFg6hPnOxbOkTPaSdKvLv-bGV-lexcIp_x-COggS1rVU56bYVByHSLy8g_iPdolU4f2K8GFItYVEzhsuxRQYtDd-I2p1G7anMlCMpz7wN7EHmxdSESSnmIK37huYEdoalFg1JWeAALm4bDcRWFF_-_LQ6XzbXZDKzyUeUu7ZuDXmu_IL7XBkknJNg5btHpMI6FzKAhJe5ej1N16SB8X3APtd9w2uiF1TnpQ9sV3OUrpRciZdA7SSGqb-sKPdfOoc63aMqrwaOXx0BIKbS7M1dr9llrMx55kXDk_co1Z152KBVlf7eO-MfPHXzXzuEeq5ijyhymcxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e85bc0602.mp4?token=cCgnc_chWdxp_UFg6hPnOxbOkTPaSdKvLv-bGV-lexcIp_x-COggS1rVU56bYVByHSLy8g_iPdolU4f2K8GFItYVEzhsuxRQYtDd-I2p1G7anMlCMpz7wN7EHmxdSESSnmIK37huYEdoalFg1JWeAALm4bDcRWFF_-_LQ6XzbXZDKzyUeUu7ZuDXmu_IL7XBkknJNg5btHpMI6FzKAhJe5ej1N16SB8X3APtd9w2uiF1TnpQ9sV3OUrpRciZdA7SSGqb-sKPdfOoc63aMqrwaOXx0BIKbS7M1dr9llrMx55kXDk_co1Z152KBVlf7eO-MfPHXzXzuEeq5ijyhymcxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنل های عراقی با فیلمی مدعی شدند چهار بالگرد آسیب‌دیده بلک هاوک که با حمله ایران در پایگاه هوایی موقر السلطی ، اردن آسیب دیده‌اند و منتقل می‌شوند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22803" target="_blank">📅 21:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مدیونی فک کنی‌ چنل رو میبینن
😁</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22802" target="_blank">📅 20:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ca539957.mp4?token=oCesrjrMteyxeUawhvk68AAfquTAk2eViNjOpQXXeVJniYfhtfos_ierXzIXUdBggZw-EQzqhgDoMYBd_vdY0JGcoZm73C2trOFA8wovciwKW-oNtX_A_r5ustsEudZX91aV3BlnQjrQ83WASB0chLUBDYEir647WJdV902UceWQEWTmmiOJm4EwgPkJKUMHHIsdEy7f0_2Tivo7DQogIlG4xUB6SN1tFBoVV9p9WJnBl3Te0Uh9k2tvR_j_gFhkyhs-eEQ4l3nxVsOh7V-H70TKaJ5Mgf147lQrKYuOxCw20sFbcYWlP1ByqO_kwh4mv6nIGz6RJl_aV-sMDnjbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ca539957.mp4?token=oCesrjrMteyxeUawhvk68AAfquTAk2eViNjOpQXXeVJniYfhtfos_ierXzIXUdBggZw-EQzqhgDoMYBd_vdY0JGcoZm73C2trOFA8wovciwKW-oNtX_A_r5ustsEudZX91aV3BlnQjrQ83WASB0chLUBDYEir647WJdV902UceWQEWTmmiOJm4EwgPkJKUMHHIsdEy7f0_2Tivo7DQogIlG4xUB6SN1tFBoVV9p9WJnBl3Te0Uh9k2tvR_j_gFhkyhs-eEQ4l3nxVsOh7V-H70TKaJ5Mgf147lQrKYuOxCw20sFbcYWlP1ByqO_kwh4mv6nIGz6RJl_aV-sMDnjbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : شهپادی که سپاه چندین سال به دنبالش بود و یک بار ۴ سال پیش اقدام به سرقت کرد ولی ناموفق ماند، توسط دیدبان اتاق جنگ شکار شد. این یک شناور سطحیِ بدون‌سرنشین از نوع «Saildrone Explorer» است که شرکت آمریکایی سیل‌درون آن را طراحی و تولید کرده…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22801" target="_blank">📅 20:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رویترز : پیشروی حوثی‌ها در سواحل دریای سرخ یمن با هدایت مستقیم سپاه انجام شده است
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22800" target="_blank">📅 20:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وال‌استریت ژورنال: ایران بار دیگر تولید و مونتاژ موشک‌های بالستیک را از سر گرفته است. بر اساس این گزارش، فعالیت‌های موشکی در چند سایت زیرزمینی از جمله مجتمع خجیر از سر گرفته شده و ایران در حال ایجاد مراکز جدید مونتاژ زیرزمینی است؛ هرچند تولید هنوز به سطح پیش از جنگ نرسیده است
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22799" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgcNKDvhPHltiLcLDzQOhnqaGnhIFLswDlPXjh6kW_i2FppJzqWYkthZUDiJMbTI4u-aYhB53vsH5DFV_m-8WFscLjKHW4ZygpmBEUUGdYni0sJUMv3wPuA7ts3zM2xPNbZjsZK2Q0Ck-mLLRVhTR-GtfFtnHi7efS7-IofpKhqgFPnZeLO-ox4AhbhxF66Ngyz9JEedVVV1Ekyt70qi86zytJY1RybpfgoUg-xn2ajfSLLqT0J8IidBHw9zhUyCFWHtGNVp4Y4wWMuw2XH22RM1WM15hqd779WN5S0YNkjAam1OOWjLg-rEv96OEUJUGMXJB95hvY3pZ6jzk4r4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: بیش از ۵۰ کشتی حامل کمک‌های بشردوستانه اجازه عبور دریافت کرده‌اند
همچنین یک فروند بالگرد نیروی دریایی آمریکا از نوع MH-60R سی‌هاوک از عرشه ناو یو‌اس‌اس رافائل پرالتا (DDG-115) به پرواز درآمده است؛ این ناو در چارچوب اجرای
محاصره دریایی آمریکا علیه ایران
فعالیت می‌کند. از امروز، نیروهای آمریکایی
۹۶ کشتی تجاری را برای اطمینان از اجرای کامل محاصره تغییر مسیر داده‌اند
.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22798" target="_blank">📅 20:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22797">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐠𝐮𝐚𝐫𝐝 𝐣𝐚𝐯𝐢𝐝𝐚𝐧</strong></div>
<div class="tg-text">یاشار رفتم چسب قطره ای گرفتم هیچی توش نبود
😂</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22797" target="_blank">📅 19:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22796">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شعبه آلمان بانک سپه ایران در پی اعمال تحریم‌های اتحادیه اروپا علیه این بانک، امروز وارد فرآیند ورشکستگی شده است.
این شعبه که در فرانکفورت فعالیت می‌کند، سال‌هاست تحت محدودیت‌های مرتبط با تحریم‌های ایران قرار دارد. بانک سپه در سطح بین‌المللی نیز سابقه طولانی در فهرست تحریم‌های آمریکا دارد و آدرس شعبه فرانکفورت آن در اطلاعات تحریمی آمریکا ثبت شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22796" target="_blank">📅 19:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نماینده چین: اصرار بر بازگشت تحریم‌ها علیه ایران صلح و امنیت بین‌المللی را به خطر می‌اندازد نماینده چین در نشست شورای امنیت سازمان ملل با موضوع ایران: ما از بیانیه روسیه حمایت می‌کنیم و معتقدیم اسنپ‌بک به پایان رسیده است و شاهد غروب برجام هستیم. از اینکه همچنان…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22795" target="_blank">📅 18:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر دفاع اسرائیل ، کاتز خطاب به مردم ایران:
سال اینده در تهرانی که از سرکوب و استبداد ازاد شده باشد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22794" target="_blank">📅 18:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه 11 تایید 2 مخالف (روسیه و چین) 2 ممتنع  این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس قطعنامه…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22793" target="_blank">📅 18:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تنگه دعوا شد ، صدای‌چند انفجار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22792" target="_blank">📅 18:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
11 تایید
2 مخالف (روسیه و چین)
2 ممتنع
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس قطعنامه نبود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22791" target="_blank">📅 18:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22790">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تولید سوسیس و کالباس با ۲۵۰ تن مرغ تاریخ‌ گذشته
در مشهد
!
مدیرکل پشتیبانی امور دام خراسان رضوی گفته
۲۵۰ تن گوشت مرغ
تاریخ‌ مصرف‌ گذشته استان، با مجوز قضایی به
سوسیس
و
کالباس
تبدیل شده.
مسئول مربوطه هم گفته این مرغ‌ها فاسد نشده بودن و فقط تاریخ مصرفشون گذشته بود و چون امکان توزیع مستقیم نداشتن، با مجوز قضایی برای مصرف صنعتی فرستاده شدن....
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22790" target="_blank">📅 17:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نمایندگی ایران نزد سازمان‌های بین‌المللی در وین: قطعنامه جدید آژانس بین‌المللی انرژی اتمی علیه ایران، باعث
تضعیف بیشتر و در نهایت فروپاشی نظام جهانی منع اشاعه هسته‌ای
خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22789" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22788">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رویترز به نقل از دو منبع نظامی دولتی:
انصارالله یمن به دو جزیره حنیـش بزرگ و حنیـش کوچک در دریای سرخ رسیده‌
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22788" target="_blank">📅 17:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسکای نیوز: مشاوران رئیس‌جمهور ترامپ در ساعات اخیر، فشار زیادی بر او وارد می‌کنند تا جنگ با ایران را با شدت و فوریت بسیار بالا از سر بگیرد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22786" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بلومبرگ: آژانس انرژی اتمی وجود فعالیت هسته ای در سایت کوه کلنگ ایران را تأیید کرد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22785" target="_blank">📅 17:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سر جان ساورز، رئیس سابق MI6
به فایننشال تایمز گفت:
«فکر می‌کنم این وضعیت چند ماه دیگر ادامه پیدا کند، اما در مقطعی فشارهای اقتصادی شروع می‌کنند به اثر گذاشتن بر حکومت ایران.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22784" target="_blank">📅 17:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22783">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ca6SKt7rPS8M76Qg-PVPVQJEu4i_3pCr_OiynYierbBWDNjQl-gTi50J2tyNM4EenRKiDlCMC-lFO00ImlThyZhndlUHUnFBCoE6MgEJoxLujLdtl0NQRLiUOrPMhTJGiO93OAqTIm5o-bI4JuAQaFPpzTugTxpgOaC6wil6VSTtViVbAM31ymS_5sgAD1MyxBlVnYivEz9YdcuxoGigcoybQedcn59X6uRIdvQe2ipvQ1Vsbz67UFUeMmG_zWXn2NuWK6dzqoDyVjrQUqLtpAUCkaaL6BEj2hcThk33ivaeC8E4LxSGhvCgvFUzIfbB7mvh-mAS6MlnXd8jUTeXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت از ۱۰۵$ عبور کرد نرخ دلار تتر هم ۲۳۶،۰۰۰ تومان در این لحظه است
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22783" target="_blank">📅 16:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9w8yH4WjrbudZMFWw1ql2OWi_U368ntkg568V0An2nIbofY0lENiJT6ZpxKiSKL3gyc2HoxeSdWnGuzoCnwJnuvhwb_ARj7gw_rVk94Z7F4GrXIARxoQYGBsVLPpyAE0Y_2oCPUmWBWhcFGmNDQnHbUa156kZcha_Bt9sTY8IKzrjeZ5nC-f2T-TUAzXZI5MpPMQVI84TRcvhwZtXYDpx2eFxQGt7CPQlug0HFCeegAFIZbXeOM_jHcIw-x958cQs8s1YKKzfaXsdulJ1LxuAB6YfyfgVLlDC5a7lE-87EnwiZemsWIx1cJTUtT9_9oFp5XhmJOjPyVNNWtY496qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی:  همین الان پرواز هواپیمای پارس از بندر به شیراز بلند نمیشه
میگن جنگنده دیدن فعلا حریم هوایی بسته هست
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22782" target="_blank">📅 15:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILA8ORtPrgXiMxvjym3fc3TLaacL9F6V9N7n4PhxDfO7ufikddCaXZJnSu-_S-W0M168z7-HzCqsJHVzfj9n06DrvrfsBYw6ZQSFmnT31uDmaoKVNGPDVk5kC0OiZUlXWndLhHqpKJz8zdsywFJEepkIgMg6wJWUc0WarIAFsDyKQaBZKKJ4dRVeeJRrPkIs-enoBL8CLyDl6DZ4zbtkvY_cYqybSrjISiTzsJ_t9bUZWrIERqwqqU7X54FiDbFcm3uWGgzbyyv3fYpb8ECMCSoTZ84XBO4kqbZvXUs7X2V8coYu2PwKQzUVuQLP9RNiSbZxVxQajA526hBz3V3J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود جزیره قشم
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22781" target="_blank">📅 14:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2AEn5KYMuKKgfqwbfoPIWn8xhJiItZ1R4g9fxGoIUroLNeiNvJWIMvGp8s_r4BmXXI62XJ5On2c6Krt0OZGOJAAvBQ7crq1I9dXZs-PLahFGhRlA0M4tQLsL8MzhK1V-tqoUhHKGY_3cnZ8guXRsRWijX7eIJ9TV-iMAYY7vno6qG9Py1WzzC17QehbSf_-KPS_6Ap8BgoOmMsn0AlyP8MG8vrPfL5cauLa_jnPeiA2NiHUEhcxrNViOfjTMil6KLDdDkTkjprPn1wtJhfacadiDokR3dxubbmnJJ5Wrgt7ZWilv_uGvdR17RuzZmJOPHwlHZuAVRzHoV3SFHTVgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : اسلامو علیکم یا کوه کلنگ
😂
دقت کنید جاده رو از وسط کوه اول میبینید که میره سمت  کوه دومی
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22780" target="_blank">📅 14:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بر اساس گزارش‌ها، ایران از فشار محاصره فعلاً دریافت
۱۰ درصد هزینه حمل‌ونقل
از کشتی‌های خارجی که محصولات انرژی را
به ایران می‌آورند یا از ایران خارج می‌کنند
، متوقف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22779" target="_blank">📅 14:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک شناور گزارش داده است یک قایق تندرو ناشناس به آن نزدیک شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22778" target="_blank">📅 14:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b971e734.mp4?token=pBTciBP7ZYtgHbOPSXo4XoGht4Rc4VQUk9O6TYgrqWEgFAWTaE8gLUgdqDSnhwLbzU3DeeP1-TLDbuKfYcoGd6CUD4a2B6oDcR-tiLPB_dN-Fe60JSHz-XIe5TJIabGlkDd3SGtg8K1skMPA-7HN_a8mHRviYoMTFM169ZC1Z7OM_Q80RGHlu2-YuI-4n9BoQt6TqxeMbJlL6v9r9aKKZSsF_TMFa4RBuZrOcekxcDjWV49oGHmCwicF-yDmqdi2TFn1fpFrZKY16pEGwiypiqxgKOw2r7f2Sid8TIBlpwyRSF-TLH5n9QuyrBfOofCg4QSN_BSsk-HFJmTpInLpWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b971e734.mp4?token=pBTciBP7ZYtgHbOPSXo4XoGht4Rc4VQUk9O6TYgrqWEgFAWTaE8gLUgdqDSnhwLbzU3DeeP1-TLDbuKfYcoGd6CUD4a2B6oDcR-tiLPB_dN-Fe60JSHz-XIe5TJIabGlkDd3SGtg8K1skMPA-7HN_a8mHRviYoMTFM169ZC1Z7OM_Q80RGHlu2-YuI-4n9BoQt6TqxeMbJlL6v9r9aKKZSsF_TMFa4RBuZrOcekxcDjWV49oGHmCwicF-yDmqdi2TFn1fpFrZKY16pEGwiypiqxgKOw2r7f2Sid8TIBlpwyRSF-TLH5n9QuyrBfOofCg4QSN_BSsk-HFJmTpInLpWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر عراقی ها در مورد مجتبی خامنه‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22777" target="_blank">📅 14:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb7f0cc7fa.mp4?token=T75uEQjC3LWhCBfA9fqUR-mpT4llIdGVFvDnkx9hsut-G4YnjXrGhR2bUu3T27yKmhS2mkF1-m_pLF6YCJ-Luy_ZxSD_JU_DuP9zxF5c-HpyoaPdiWXSZi2SHN2H_hxQHcBNcx_hICrxfUKhCwlSkvgfgmUpgySJM4RE6R2nfsYzqJ_snFvSZqkZf7k3qaLj99LbXkfce3L_ZTqe-R7Ur4AoDSNoZ0RMTEKMLfzqVeGPW3V4nnh6oAsLn63u1x-AkVrhTIGntfZhKlS6V5Db4av2ek570h1_7ME-V3J5LWovtxuz96Af9P3QX9DjcSH1TKFlNVh3CGC9dqwH3r3FcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb7f0cc7fa.mp4?token=T75uEQjC3LWhCBfA9fqUR-mpT4llIdGVFvDnkx9hsut-G4YnjXrGhR2bUu3T27yKmhS2mkF1-m_pLF6YCJ-Luy_ZxSD_JU_DuP9zxF5c-HpyoaPdiWXSZi2SHN2H_hxQHcBNcx_hICrxfUKhCwlSkvgfgmUpgySJM4RE6R2nfsYzqJ_snFvSZqkZf7k3qaLj99LbXkfce3L_ZTqe-R7Ur4AoDSNoZ0RMTEKMLfzqVeGPW3V4nnh6oAsLn63u1x-AkVrhTIGntfZhKlS6V5Db4av2ek570h1_7ME-V3J5LWovtxuz96Af9P3QX9DjcSH1TKFlNVh3CGC9dqwH3r3FcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک آمریکایی که نقش سیاهی لشگر را بازی میکند از فصل چهارم در دست ساخت سریال «Special Ops: Lioness» ویدیویی از پشت‌صحنه منتشر کرده که در آن بازیگران با
یونیفرم نیروهای ایرانی
دیده می‌شوند.این یک سریال جاسوسی و نظامی آمریکایی به نویسندگی تیلور شریدان است که داستان عملیات‌های مخفی سازمان سیا و نیروهای ویژه آمریکا را دنبال می‌کند.
فصل دوم
بخش مهمی از داستان را به ایران و تلاش آمریکا برای متوقف‌کردن انتقال دانشمندان هسته‌ای به ایران اختصاص می‌دهد.
فصل سوم
نیز دوباره ایران را وارد خط اصلی داستان کرده و یک مأمور ایرانی در ربوده‌شدن جو، شخصیت اصلی سریال، نقش دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22776" target="_blank">📅 14:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش ها از وضعیت محمد ناصر العاطفی
وزیر دفاع دولت حوثی‌ها:
«إرم نیوز امارات» و «أحداث العالم
»
گزارش کشته‌شدن محمد ناصر العاطفی را منتشر کردند، و آن را در قالب «گزارش‌ها از کشته‌شدن» آورده ولی تأیید رسمی ارائه نکرده اند.
«یمن شباب»، «المیثاق نیوز» و «أحداث العالم» حمله به جلسه فرماندهان حوثی در البرح و حضور العاطفی را گزارش کرده‌اند، اما مرگ او را با تأیید رسمی یا مستقل قطعی نکرده‌اند. همچنین یک گزارش جدید از
i24NEWS
حتی می‌گوید ارزیابی‌های اسرائیلی احتمال می‌دهند العاطفی
زخمی شده ولی کشته نشده باشد
.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22775" target="_blank">📅 13:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFBqxAVgOXmn3L6fsnxMvXoWW-njfZmKRKX0SIOuRG23H4xnA23KufTZx60TbNuL7cm61cDBeRJNsGxI7pvpsQTWzzEnq4vM4dL5zA8N5l0moIj5hI4gmV4Eo6jbNnvflytwncKgkV5hGmoB3jI5SVOKIuWEIwArClFubfvwoYKUbM3Mz-lF0mdM_hub-EVwJ7gB9uS_Q4dkB6VJtuiGFCQJ0gsnwOTQazH_HsRWN9Z2Fe9kvlbXWhI-k4Yb-duJb5XGnZEs6DXTGJjkS5uLLolZ5zLlciW9VFOD3ZAIn-5X3JU8xEDN8KFJD5KIyFflf6CFGla-hhv3lpkGs8hgLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با بیشتر شدن فقر  در جامعه گوشت گاومیش هندی به سفره ایرانی‌ها وارد شد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22774" target="_blank">📅 13:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22773">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وقتی شما مشغول ساختن عکس‌های دهه هشتاد میلادی و هویت جعلی با هوش مصنوعی بودید، رژیم آخوندی ضد ایرانی با بی‌رحمی به جان
رباط تاریخی سبزوار
افتادند و بخشی از هویت شما را نابود کرد
این کاروانسرای دوره صفوی که در دوران پهلوی محل استقرار اداره امنیه سبزوار بود، و ثبت ملی هم شده بود !
تخریب میراث فرهنگی یعنی تخریب هنر، معماری، تاریخ و بخشی از هویت ایران.
لطفاً به اشتراک بگذارید
@WarRoom
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/22773" target="_blank">📅 12:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وال‌استریت ژورنال: دولت آمریکا خود را برای یک درگیری طولانی‌تر با ایران آماده می‌کند؛ از جمله با ادامه استقرار نیروها در منطقه و چرخش یگان‌های نظامی و دفاعی. هم‌زمان، طرح‌هایی برای تشدید فشار اقتصادی و منزوی کردن ایران نیز در دولت ترامپ مطرح شده است. بر اساس…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22772" target="_blank">📅 11:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وال‌استریت ژورنال: دولت آمریکا خود را برای یک درگیری طولانی‌تر با ایران آماده می‌کند؛ از جمله با ادامه استقرار نیروها در منطقه و چرخش یگان‌های نظامی و دفاعی. هم‌زمان، طرح‌هایی برای تشدید فشار اقتصادی و منزوی کردن ایران نیز در دولت ترامپ مطرح شده است. بر اساس این گزارش، جی‌دی ونس، معاون رئیس‌جمهور، و مارکو روبیو، وزیر خارجه آمریکا، در جلسات خصوصی درباره احتمال طولانی شدن جنگ با ترامپ گفت‌وگو کرده‌اند. نگرانی اصلی آنها این است که ایران بتواند در برابر فشار نظامی، اقتصادی و محاصره دریایی آمریکا مقاومت کند و در نتیجه، پایان سریع جنگ ممکن نباشد؛ به‌طوری‌که در بدترین سناریو، درگیری حتی تا پایان دوره ریاست‌جمهوری ترامپ و در ابتدا ۲۰۲۹ ادامه پیدا کند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22770" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ : این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.  گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22769" target="_blank">📅 11:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جنیفر جیکوبز، خبرنگار CBS: چندین هواپیمای نظامی آمریکا در حملات شبانه به پایگاه هوایی موفق‌السلطی در اردن آسیب دیدند
؛ منابع این موضوع را به من و جیم لاپورتا اعلام کردند. یک فروند A-10 تاندربولت، معروف به وارثاگ، مورد اصابت قرار گرفت و با یک بال مفقود بر جای ماند. حدود هشت فروند F-15 آسیب جزئی دیدند و دوباره وارد خدمت شدند. نیروهای آمریکایی در اردن برای دفاع در برابر حملات ایران، بیش از ۳۰ موشک پاتریوت شلیک کردند. این آسیب‌های شبانه پس از آن رخ داد که آمریکا در واکنش به هدف قرار گرفتن یک ناو نیروی دریایی آمریکا توسط ایران، به پنج نفتکش ایرانی حمله کرد. در پاسخ، سپاه پاسداران انقلاب اسلامی مدعی شد که به هشت نفتکش و دو ناو جنگی، از جمله پایگاه آمریکا در اردن، حمله کرده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22768" target="_blank">📅 11:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102d5064ec.mp4?token=HpvBlLCG7eYrDgnBeSgdSve6k2Wk4RcBW3ORznqxe1ZeUOxcp5DKId1RUJq8Z4WphWocLtvuNzn_DdARI-Q1iFZH6vD8pW_bpMWEd3qyqHH4a64w53d4k-KRMXZi1s6y6PWCDN5nM9w1KzUJ5M8zz-9wjnzfrpJUxMFBfvxC0GBf-kopdfqOLTUmjr3ydqaTOUANR87fkpJBOeSfb_o7NvBPdz2jqBzR7lgw1jxV8QLZm8sNh43srLP4sxRdRAa7Ozxz3p4s2oIQniVLCrEoPhIUNTV3YwnUJcpCiUO8-xhUHs5UeOIpE1wi-G7Dbs-LLKyahj8an1IGovilha77-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102d5064ec.mp4?token=HpvBlLCG7eYrDgnBeSgdSve6k2Wk4RcBW3ORznqxe1ZeUOxcp5DKId1RUJq8Z4WphWocLtvuNzn_DdARI-Q1iFZH6vD8pW_bpMWEd3qyqHH4a64w53d4k-KRMXZi1s6y6PWCDN5nM9w1KzUJ5M8zz-9wjnzfrpJUxMFBfvxC0GBf-kopdfqOLTUmjr3ydqaTOUANR87fkpJBOeSfb_o7NvBPdz2jqBzR7lgw1jxV8QLZm8sNh43srLP4sxRdRAa7Ozxz3p4s2oIQniVLCrEoPhIUNTV3YwnUJcpCiUO8-xhUHs5UeOIpE1wi-G7Dbs-LLKyahj8an1IGovilha77-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «فکر می‌کنم باید نام تنگه هرمز را به «تنگه ترامپ» تغییر دهیم.
خانم‌ها و آقایان، اعلامیه‌ای در این‌باره خواهم داشت. آن را تنگه ترامپ خواهیم نامید و مطمئنم رهبری ایران از این موضوع بسیار خوشحال خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22767" target="_blank">📅 10:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167df781a6.mp4?token=E4NqR3t6uDpx6vLU7kDEpVlaovcAZHhq0Cz8EPx3dc6mZxYtrl6ePmPcR5R98wRi5tOzoCGLlqchxrw-ccvI2BkjLGf-MtGcjbCqsF8Dc8rOAOM7q91NX7vLYQcSgKeFre-a4ZvIi9_v7bfMNU5naF9Z1ezAv8BUtaOjSwEKf6SlIWpk020OiBgJetb7KKLYp1PAWWZZGOY2S62vPdIopiyIsOhAx5Ia4d_07MAZZt5E7AZiEzzz1z74PRaL-yeWlVX0DN3GAzW-4wWsP-OEcaNxKpiQkYBx-_vjcVuKQ34kV-T6_2va5SCvlPpQSqmQ7MozMvcm1r4i0eqsbFX1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167df781a6.mp4?token=E4NqR3t6uDpx6vLU7kDEpVlaovcAZHhq0Cz8EPx3dc6mZxYtrl6ePmPcR5R98wRi5tOzoCGLlqchxrw-ccvI2BkjLGf-MtGcjbCqsF8Dc8rOAOM7q91NX7vLYQcSgKeFre-a4ZvIi9_v7bfMNU5naF9Z1ezAv8BUtaOjSwEKf6SlIWpk020OiBgJetb7KKLYp1PAWWZZGOY2S62vPdIopiyIsOhAx5Ia4d_07MAZZt5E7AZiEzzz1z74PRaL-yeWlVX0DN3GAzW-4wWsP-OEcaNxKpiQkYBx-_vjcVuKQ34kV-T6_2va5SCvlPpQSqmQ7MozMvcm1r4i0eqsbFX1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: «دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای B-2 خود به تأسیسات هسته‌ای آنها حمله نکرده بودیم، آنها همین حالا سلاح هسته‌ای داشتند. اگر آنها سلاح هسته‌ای داشتند، من با رهبر عالی ایران تماس می‌گرفتم و می‌گفتم: «آقای رهبر، حال شما چطور است؟ کاری هست که بتوانیم برای شما انجام دهیم؟» نه اینکه مثل الان، حسابی آنها را بمباران کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22766" target="_blank">📅 10:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ درباره کوه کلنگ
:
«به لطف
نیروی فضایی آمریکا
، ما می‌توانیم همه‌چیز را ببینیم. حتی می‌توانیم نوشته روی لباس آنها را ببینیم؛ محمد الفیاض، محمد العزوری.
می‌توانیم آن را از فضا بخوانیم؛ باور می‌کنید؟ از هزاران مایل دورتر.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22765" target="_blank">📅 10:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اورشلیم پست: گزارش‌هایی از انفجار در جزیره قشم و مناطق جنوبی ایران
اورشلیم پست بامداد امروز گزارش داد صدای انفجار در جزیره قشم شنیده شده و همچنین گزارش‌هایی از اصابت پرتابه‌ها به مناطقی در شهرستان سیریک در جنوب ایران منتشر شده است؛ جزئیات خسارت یا تلفات هنوز مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22764" target="_blank">📅 10:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یورونیوز: آمریکا عملیات اقتصادی علیه ایران را تشدید کرده است
همزمان با حملات نظامی، واشنگتن فشار اقتصادی علیه تهران را افزایش داده و تحریم‌های جدیدی علیه شرکت‌ها، افراد و شبکه‌های مرتبط با تجارت و حمل‌ونقل ایران اعمال کرده است. یورونیوز این اقدامات را بخشی از تلاش واشنگتن برای منزوی کردن اقتصادی ایران عنوان کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22763" target="_blank">📅 10:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آسوشیتدپرس: نفت بالای ۱۰۰ دلار باقی ماند
افزایش قیمت نفت ناشی از تشدید جنگ ایران و آمریکا باعث کاهش ارزش بازارهای سهام آسیا شده است. برنت روز گذشته برای نخستین‌بار از ژوئیه از ۱۰۰ دلار عبور کرد و نگرانی درباره تورم و هزینه انرژی در اقتصادهای جهان افزایش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22762" target="_blank">📅 10:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فاکس‌نیوز: حمله موشکی ایران به پایگاه‌های آمریکا در اردن ناکام ماند
یک مقام آمریکایی به فاکس‌نیوز گفت حمله موشکی ایران به مواضع آمریکا در اردن «بی‌اثر» بوده و تمامی نیروهای آمریکایی مستقر در این کشور سالم هستند. اردن نیز اعلام کرده بود ۱۸ موشک از ۲۰ موشک شلیک‌شده را رهگیری کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22761" target="_blank">📅 09:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز: تردد کشتی‌ها از تنگه هرمز به ۷ فروند کاهش یافت
دیروز چهارشنبه تنها ۷ کشتی حامل کالا از تنگه هرمز عبور کردند؛ در حالی که میانگین ۱۰روزه ۱۴ کشتی بوده است. از میان این کشتی‌ها، تنها یک نفتکش بسیار بزرگ حامل نزدیک به دو میلیون بشکه نفت خام از تنگه خارج شد و هیچ نفتکش ال‌ان‌جی از تنگه عبور نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22760" target="_blank">📅 09:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcd7646c71.mp4?token=SCfjmzyQD3MxZmpOTOIwXjHCuJwKg4VzEYulO0FQnJxBoC3LpJHQCaWqf1FOmEYavCH3D5ZSs5zWyglkOiVOI2TfoDz9rniI5KHQQ8g5s7rJpo7ySed_5mhMgspgOGfd91N7tLiaRVUsDWpKMDGVcbtLExFwVoSERU14IaepqhzgpR6wyk25Rd2qdEzik_evz9-wr5ay1tQPw2eCMkDOJFsrhqD6OX9Q9F6J2rfoMiWTkRHn47x4mejFgNHYiCC9mrDvuFBytet2Xur-x_BZHc-AcvFFkC7IME2m_iivHHLomdxtks7zoyUwXfvqWHHiViN14zuzfL4T32EO1K8pgYoKiUr3icEdtrxRXmUSNehP_Y0qMw4O9w4HUkUKqW2NyneaYlkhiCEYU_5or4i7QCql_0nwKmLMkMMvmtvnT8wfgSqqL0CmvD8VDuWCp8ixCV97L8LT1JOeL78-p-Jcvi6gz5T9WIYaPlVUWvBQDjB68zFx89d3RR1TDkZ8vgdu3fbV4iCILLSlSN8O7423BP9zQg6AqB1gw1ADaHmOfsoSRYP0QFXY6MDgC4LVixax-EwN4VouB5BVyhWmlhkEKpwjDrxFfD8l3jxtKpgwJQ7Ai3eXJFHKEmmTlxSzWU3v_38yd-qmXe9cwO6olyr8UAH9xgnJVZxdW6h9qPxeUdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcd7646c71.mp4?token=SCfjmzyQD3MxZmpOTOIwXjHCuJwKg4VzEYulO0FQnJxBoC3LpJHQCaWqf1FOmEYavCH3D5ZSs5zWyglkOiVOI2TfoDz9rniI5KHQQ8g5s7rJpo7ySed_5mhMgspgOGfd91N7tLiaRVUsDWpKMDGVcbtLExFwVoSERU14IaepqhzgpR6wyk25Rd2qdEzik_evz9-wr5ay1tQPw2eCMkDOJFsrhqD6OX9Q9F6J2rfoMiWTkRHn47x4mejFgNHYiCC9mrDvuFBytet2Xur-x_BZHc-AcvFFkC7IME2m_iivHHLomdxtks7zoyUwXfvqWHHiViN14zuzfL4T32EO1K8pgYoKiUr3icEdtrxRXmUSNehP_Y0qMw4O9w4HUkUKqW2NyneaYlkhiCEYU_5or4i7QCql_0nwKmLMkMMvmtvnT8wfgSqqL0CmvD8VDuWCp8ixCV97L8LT1JOeL78-p-Jcvi6gz5T9WIYaPlVUWvBQDjB68zFx89d3RR1TDkZ8vgdu3fbV4iCILLSlSN8O7423BP9zQg6AqB1gw1ADaHmOfsoSRYP0QFXY6MDgC4LVixax-EwN4VouB5BVyhWmlhkEKpwjDrxFfD8l3jxtKpgwJQ7Ai3eXJFHKEmmTlxSzWU3v_38yd-qmXe9cwO6olyr8UAH9xgnJVZxdW6h9qPxeUdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس نیوز : ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. منتقدان می‌گویند رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند
جی دی ونس: رئیس جمهور ترامپ می‌خواهد شهروندان را در این ثروت عظیم ناشی از تعرفه ها سهیم کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22759" target="_blank">📅 09:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4bcfd6f9.mp4?token=sHWB3M0zVo1hirsFlvT06aJlN02yrjyZpw13IAdRUi8SivXnmWWYIeD0-Ish11QTDXs2FpGgYJRTNwLdkfAOJiDuHi7XBd8LI2sMRgRh6QKlJzDJZjWJ7o6VCtAW4Qs-1BIpJtGQRxnQBE2c6B9nYmljb9gfSzC5Ir44o85VxAp1NzaYXhFjs3622CcyUwJp3jCvhqxtCLO7HGxK8f7z5_OWPGgSxiTSNBQHlBpqMsq6izVzJSfLyVca74Uhu_dVBl6vA2P4_xQJ3xKYt1YtVMu1f2E21sE_GCmWdLbei-vriJYZp6De22aoC8k8HkixQXn7EQgH4teURlWjT2vzDXnYRuAeeH_hgP_W3_dz74IrFEQhbPBMQmUW5Hhy3rTnWPOwBDuat_fYPt06JyIIrXGltN4w_ApCXmPYdQ8W-T9Zgu06sPnQd_Yb0wUefUdKZcLFmg8x_GXsi5djU3MR8vuAZYe7E10DibCCgYzW2U4j5KT1DtGunqsP2tk_U_f7d4FUyaR_hRJonafCN1iXnKRX9QF4Y9vOoJC9rEJo5TSwrSesSBxGILpUcYgDWrOg6Aq-XYbITHerms5drX58Y7q-5I97n1VuhcOPnE0hG-TjO_NP2xxWl0gvbdZPhiet7d3DkmbEuLrGtGL6EOHnrqDlB4_9sRuze5_R4rn-N8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4bcfd6f9.mp4?token=sHWB3M0zVo1hirsFlvT06aJlN02yrjyZpw13IAdRUi8SivXnmWWYIeD0-Ish11QTDXs2FpGgYJRTNwLdkfAOJiDuHi7XBd8LI2sMRgRh6QKlJzDJZjWJ7o6VCtAW4Qs-1BIpJtGQRxnQBE2c6B9nYmljb9gfSzC5Ir44o85VxAp1NzaYXhFjs3622CcyUwJp3jCvhqxtCLO7HGxK8f7z5_OWPGgSxiTSNBQHlBpqMsq6izVzJSfLyVca74Uhu_dVBl6vA2P4_xQJ3xKYt1YtVMu1f2E21sE_GCmWdLbei-vriJYZp6De22aoC8k8HkixQXn7EQgH4teURlWjT2vzDXnYRuAeeH_hgP_W3_dz74IrFEQhbPBMQmUW5Hhy3rTnWPOwBDuat_fYPt06JyIIrXGltN4w_ApCXmPYdQ8W-T9Zgu06sPnQd_Yb0wUefUdKZcLFmg8x_GXsi5djU3MR8vuAZYe7E10DibCCgYzW2U4j5KT1DtGunqsP2tk_U_f7d4FUyaR_hRJonafCN1iXnKRX9QF4Y9vOoJC9rEJo5TSwrSesSBxGILpUcYgDWrOg6Aq-XYbITHerms5drX58Y7q-5I97n1VuhcOPnE0hG-TjO_NP2xxWl0gvbdZPhiet7d3DkmbEuLrGtGL6EOHnrqDlB4_9sRuze5_R4rn-N8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر جمهوری‌خواهان هم مجلس نمایندگان و هم سنا را پیروز شوند، به‌دلیل موفقیت اقتصادی عظیم ما، به هر شهروند بزرگسال در ایالات متحده
۵۰۰۰ دلار
پرداخت خواهم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22758" target="_blank">📅 09:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تتر ۲۳۷،۰۰۰تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22757" target="_blank">📅 09:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح…</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22756" target="_blank">📅 04:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSINA</strong></div>
<div class="tg-text">این حروم زاده ها کی میرن رفتم ۵ لیتر بنزین زدم شد ۵۰ تومن
😐
💔</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22755" target="_blank">📅 04:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4a9d76473.mp4?token=XQv3OFcOweUTr6KL4-LKZo_thLhzzp1lZsVUPN5F5le8Ku3SK0XA5KYuhpItoH6emmQpA3aYotRF0VIkUijEqCA7c_jqs17KUAoKvkkBaN1Ht0r3Nj_9FhAiJQyxRuj-KCeRt-v5faWcfMv32luYIMQ26SszzSJVctmUot2OWh9f3Z6i0w7kq6m704oQep0Gar_sk5Z6TF4QaMhzZ_jtXZ28t-130gthkBR4KQneOb2H5_-lm5SJSgdNztV51dredRCURpFoPET7UbxdDr1XMdQaLKvS6Q96aesklqlgYhiw4K0xY8eGJJJFeTlJEovbLjj-8m_BNwed3hN4rORfBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4a9d76473.mp4?token=XQv3OFcOweUTr6KL4-LKZo_thLhzzp1lZsVUPN5F5le8Ku3SK0XA5KYuhpItoH6emmQpA3aYotRF0VIkUijEqCA7c_jqs17KUAoKvkkBaN1Ht0r3Nj_9FhAiJQyxRuj-KCeRt-v5faWcfMv32luYIMQ26SszzSJVctmUot2OWh9f3Z6i0w7kq6m704oQep0Gar_sk5Z6TF4QaMhzZ_jtXZ28t-130gthkBR4KQneOb2H5_-lm5SJSgdNztV51dredRCURpFoPET7UbxdDr1XMdQaLKvS6Q96aesklqlgYhiw4K0xY8eGJJJFeTlJEovbLjj-8m_BNwed3hN4rORfBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22754" target="_blank">📅 03:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromabas</strong></div>
<div class="tg-text">سلام
یاشار من عصری از خستگی و بی بازاری و کلافگی خوابم برد بازارم نرفتم خداگواه خواب دیدم. مانوک اومد تو خوابم. اصلا بهش فکر نکرده بودم ها. گفت فقط ۱۲روز دیگه صبر کنین</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22753" target="_blank">📅 03:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22752" target="_blank">📅 03:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22751" target="_blank">📅 03:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22750" target="_blank">📅 03:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22749" target="_blank">📅 03:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22748" target="_blank">📅 03:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فنر رو بکشید !</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22747" target="_blank">📅 03:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22746">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دارم یه کارای میکنم از قلب واشنگتن دی سی ! تا کی‌تماشا ؟! خودم دست به کار میشم ! در چند روز آینده متوجه میشوید !</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22746" target="_blank">📅 03:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f949e07910.mp4?token=wBFd34g3jtMSio2d6-p1uD7UGcLnTXI8UhUx4M5raNiM4FSxOcBdLYUOiuad5-0MURGFfOXscdn661qY-YJ8nDP-J_vnT89-jtNYPelyWz0ghKzEag5zA0XM2vaKb3hhVMVmoeNBsGNCp9YSKm_W5XUgl9bJTnO8_DaAgqAaN4Ku38Je8icNuXuQ0mleNoCOi3hwbxZ6rFyayPlyZsVeTzShUPuWWdVcARrhd1UpDFrahHydTTTjfj5QrDyQKvxYT-GQ5K_vi96hvVsWLk4Ra1rys9s_d74vYA7vj2CL2jV95wrf_CvVU0g0G2zjAOntGXYbb9-bByEthOxYwQ97WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f949e07910.mp4?token=wBFd34g3jtMSio2d6-p1uD7UGcLnTXI8UhUx4M5raNiM4FSxOcBdLYUOiuad5-0MURGFfOXscdn661qY-YJ8nDP-J_vnT89-jtNYPelyWz0ghKzEag5zA0XM2vaKb3hhVMVmoeNBsGNCp9YSKm_W5XUgl9bJTnO8_DaAgqAaN4Ku38Je8icNuXuQ0mleNoCOi3hwbxZ6rFyayPlyZsVeTzShUPuWWdVcARrhd1UpDFrahHydTTTjfj5QrDyQKvxYT-GQ5K_vi96hvVsWLk4Ra1rys9s_d74vYA7vj2CL2jV95wrf_CvVU0g0G2zjAOntGXYbb9-bByEthOxYwQ97WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه فریدون فروخزاد و مانوک خدابخشیان را ادامه می‌دهم، نه کسی خرج من را می‌دهد، نه از کسی می‌ترسم.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22745" target="_blank">📅 02:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD6piNMF2RuUWbNTCc_PNfLu0Hqc0cOwXu06mjUouMAd74tr6Tnt4ajAAZQfQTa8U8baEVa9zL_ebfuZLPDZH7I5pH_Nfxy98sqv9XDmZzcWEzGtt1TvLjolTe_7YpCSQK7seB4Jv8iynH049bnIZp5E1_qRwglWBqukypevxqhNfJekOfSeJxFOUH8FGxPdI7P8uJDyWD77dKl1I1a8xSS0gfeW19yj3o-AeklFBjeSbf0Zlq3UrTZZaHyL6lfdFstR8Xm5L4QFL1f22vUhSun6wgMon70jssc2llZWphRvLoh1yvlaWXTEQhpxXlq1aG6EHv9yJ9gukRAJ9ftNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت محدودی خلیج فارس حاکی از ، همچنان در جریان بودن عملیات دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22744" target="_blank">📅 02:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22743">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آیت الله بی بی سی دقایقی پیش گزارش انفجار از میناب و سیریک گزارش‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22743" target="_blank">📅 02:35 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
