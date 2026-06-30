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
<img src="https://cdn4.telesco.pe/file/HtnMrrJ1lQeqaBJfVORtEqAYD1FzMl5-eR46MYMvY2NoziFLXbZyteJ5aV3F6m7RWX99xkXjAlMzccdjhd3sOiNZmaSezJDjku012F-lBnqk216XSOWqECb-N8-6Fla_3b0ybkf1TksxBx_PzePtgo08ACORPe3bn-VRZ_99DqvuxbSRUUvrVM6bztzx-pev0a9VBcaSuIYYqbCIUHzrNeRpRfoHhnuxPwz4tuOhR11v1dMHOOSsvEtIfY61rcHxzjcLbMYhNH15tO0MaMjgoHDn74zhdts16ihTwN4W6G2TqZ4EpQ8MGocn-dKt1-hQjsVH65wLeCGQsnTbH6yUcQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.18M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 10:19:16</div>
<hr>

<div class="tg-post" id="msg-664850">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
انهدام مهمات عمل نکرده دشمن در بندرعباس
🔹
انهدام مهمات عمل نکرده تجاوز آمریکایی - صهیونی در شهرستان بندرعباس محدوده دهستان سرخون و ایسین امروز صورت می‌گیرد.
🔹
احتمال شنیده شدن صدای انفجار، ناشی از عملیات فنی وجود دارد و جای هیچ گونه نگرانی برای شهروندان نیست.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/akhbarefori/664850" target="_blank">📅 10:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664849">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41fd695a5.mp4?token=hvbb5Oz23Skdj3FjHQVDUUVxJdEVKFWp96jn8mdKrP80GdQ_9EOJrOM1N5ITH10ZFDXITF7oaZFu9QRt2-bQiS0iXxX5JSY0mt2uMyrynfisRb9JeDmOg08rBoAmcLZ2SczXjTTmqKmCbo3T4G8jARKCH4WMiVh4iKAEmikOXMZaENODGqfofiQnA7oltXKe8MYwXNHzyQzRyZjeh28Wjkt0JfmqFiMgIj2a2EgpztYsw86ddlYv8UsbjwSrPZIReelgOcO4oC-EuYvKKW3P2dKZyMD2qp0Y8ZdjHhocYCYCHombjJCznSK4ALUR7N_Qq1vA1h3pVaxT9HGP15KveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41fd695a5.mp4?token=hvbb5Oz23Skdj3FjHQVDUUVxJdEVKFWp96jn8mdKrP80GdQ_9EOJrOM1N5ITH10ZFDXITF7oaZFu9QRt2-bQiS0iXxX5JSY0mt2uMyrynfisRb9JeDmOg08rBoAmcLZ2SczXjTTmqKmCbo3T4G8jARKCH4WMiVh4iKAEmikOXMZaENODGqfofiQnA7oltXKe8MYwXNHzyQzRyZjeh28Wjkt0JfmqFiMgIj2a2EgpztYsw86ddlYv8UsbjwSrPZIReelgOcO4oC-EuYvKKW3P2dKZyMD2qp0Y8ZdjHhocYCYCHombjJCznSK4ALUR7N_Qq1vA1h3pVaxT9HGP15KveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مراکش به هلند توسط دیوپ/ مراکش با حذف هلند، ‌حریف کانادا در یک‌هشتم شد
🇲🇦
1️⃣
(۳)
🏆
(۲)
1️⃣
🇳🇱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/akhbarefori/664849" target="_blank">📅 10:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664848">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6f773f03.mp4?token=ksAeDuauS1Uq8WmNGDUNyzdE7ntzD-VDsp3jQnCvThSSWG0i-AS7j8H6h5HdIFjpumdT9Zn6t84vo8Q2Y0QDAiL1r2Nwv_tINk6rx4JfwHH3jcy2qNekBQsvRtP1jIEzl_A9uXx--0gQ0x8ieLaV_hxP9FWpEY4E7AVe83PWR9UhN2Vtbzp5UzjbQWaObN9PlmG8NZKi20X8caVJv-j0lJb2IfPi3MiOimWg7sZ39rkgbdGa4NIOP_xasr3v5JH-HZysjeOA65BumJyfe9Vdwime66jKpzwrBeYB5fL4sdq6BoXO8LxX6udqp-ZMP-0jcVDZ02fAn4H6vQQOr3U8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6f773f03.mp4?token=ksAeDuauS1Uq8WmNGDUNyzdE7ntzD-VDsp3jQnCvThSSWG0i-AS7j8H6h5HdIFjpumdT9Zn6t84vo8Q2Y0QDAiL1r2Nwv_tINk6rx4JfwHH3jcy2qNekBQsvRtP1jIEzl_A9uXx--0gQ0x8ieLaV_hxP9FWpEY4E7AVe83PWR9UhN2Vtbzp5UzjbQWaObN9PlmG8NZKi20X8caVJv-j0lJb2IfPi3MiOimWg7sZ39rkgbdGa4NIOP_xasr3v5JH-HZysjeOA65BumJyfe9Vdwime66jKpzwrBeYB5fL4sdq6BoXO8LxX6udqp-ZMP-0jcVDZ02fAn4H6vQQOr3U8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خطاهای شناختی در یک نگاه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/akhbarefori/664848" target="_blank">📅 10:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664847">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp8C97t-43EJ1sUhiU8oYHeu_P-dFUIND8ht6Phg81Tlwbj8Qki2fTxXOitQer-En0hH5OUIAlXqoKluqF4pfhahjsUq-rLIaOqwcidHrkgdJWDEqIA3rX5W1gx6tdRiKOUHTz7pIQ-EdSdMLVJdAd6rjex91EZOSD-5Kc3bj9jHjK9vZkgkRa3V54ZYogrXpf8MG5-3KYV_YN8ZUH4PC55br2NUImZVAOw75wx82qglZc36cumEkJ9uhkUDGY3Y04MRSqYXCwHXMQhk6CxrEmR7HDBrjdT4z1ty36wo1-LuAQpKXvMCwhPXEgDC3uM7N04girvhKY1qdfjb0kDENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه زیبای جمعی از ایرانیان مقیم خارج از کشور به تیم ملی: اگر صدای بی‌احترامی از عده‌ای را شنیدید، لطفاً بدانید که آن صدا، صدای همه ایرانیان نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/akhbarefori/664847" target="_blank">📅 10:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664846">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ایازی: برخلاف حواشی، علما با مذاکره مخالف نیستند
ایازی، دبیر مجمع محققین و مدرسین حوزه علمیه قم:
🔹
برخلاف فضاسازی‌هایی که گاه در برخی رسانه‌ها و تریبون‌ها دیده می‌شود، بخش قابل توجهی از علما، روحانیان و اندیشمندان با اصل مذاکره و تعامل سازنده با جهان مخالفتی ندارند و آن را راهکاری عقلایی برای کاهش فشارها و حفظ مصالح کشور می‌دانند.
🔹
آنچه گاه به عنوان مخالفت عمومی مطرح می‌شود، بیشتر صدای گروهی پرهیاهو است که به دلیل برخورداری از امکانات رسانه‌ای، صدای بلندتری دارند؛ اما این صدا، الزاما بازتاب‌دهنده دیدگاه اکثریت نخبگان و روحانیت نیست.
🔹
مهم‌ترین سرمایه هر حکومت، اعتماد عمومی است و این سرمایه جز با احترام به کرامت مردم، شنیدن صدای آنان و مشارکت دادن همه جریان‌های دلسوز کشور بازسازی نمی‌شود./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/akhbarefori/664846" target="_blank">📅 10:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664845">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a72040862.mp4?token=VjkCF_rC__24MYQQYeHsgP9QrBcfOXQld5RF1tuddc0iDkoy2sWriGPJkRkTqMkWQj9urjy0vrknN5vm3Bd8_mrrm94UqnC9aZSrENToEFrFSxBo04ry6A3YiBeL3vqAZaJw-ycdETEwJVh4A2iGNFa-ErH17jnmbrv10TrXAdxNIE-T7wcN5U9xiPO0LMS9SNIGiqNx89Em1WCxXZ1uM_ILEr-qrKan1EkKANP5IIIWn4NrxGeOA0gDAZ49ROBQGupunzukfWkTiTD0KIeDDgk2Sn3Ppk5WShU5m2BvHVZycX1GQaWs9Tf64e6II7b97KKApSRjcHaXqPx5v7q4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a72040862.mp4?token=VjkCF_rC__24MYQQYeHsgP9QrBcfOXQld5RF1tuddc0iDkoy2sWriGPJkRkTqMkWQj9urjy0vrknN5vm3Bd8_mrrm94UqnC9aZSrENToEFrFSxBo04ry6A3YiBeL3vqAZaJw-ycdETEwJVh4A2iGNFa-ErH17jnmbrv10TrXAdxNIE-T7wcN5U9xiPO0LMS9SNIGiqNx89Em1WCxXZ1uM_ILEr-qrKan1EkKANP5IIIWn4NrxGeOA0gDAZ49ROBQGupunzukfWkTiTD0KIeDDgk2Sn3Ppk5WShU5m2BvHVZycX1GQaWs9Tf64e6II7b97KKApSRjcHaXqPx5v7q4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول هلند به مراکش توسط خاکپو
🇲🇦
0️⃣
🏆
1️⃣
🇳🇱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/akhbarefori/664845" target="_blank">📅 10:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664843">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
پزشکیان: توافق اخیر در هماهنگی کامل با رهبر انقلاب و حمایت شعام به‌ دست آمده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/664843" target="_blank">📅 10:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664842">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1970246926.mp4?token=hgI48mwr3Dj3PznGoDkWQlPGNpg6fnMWYkvMfLmZr_4yKdiVEGkK93rQWIbsL2ufpnKqleQiEWLU7QVzv5MTTic0ophwzm-zwtzz1Em7adsk_PUSbE_whG-jjGcg3eltxUOvtz0x8ulZgv2dzFTzQGHwYFnQN_M16j6FgnZANv7xZopzxX2A97jbN7Mq4b7KHAkS16FfLpf5i-8R9GUpSaR3udQ2i66MdUgw6-hJsJbqDPGugnsA7hLGBnW5jzVFCozJGfyRQP7tnyO18-IRUfRbvyDjmFzUL_934CsALmhdsnFz6bJxLghTK7ii2Tw8CaIBJX3_AXQK3d7M5O66vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1970246926.mp4?token=hgI48mwr3Dj3PznGoDkWQlPGNpg6fnMWYkvMfLmZr_4yKdiVEGkK93rQWIbsL2ufpnKqleQiEWLU7QVzv5MTTic0ophwzm-zwtzz1Em7adsk_PUSbE_whG-jjGcg3eltxUOvtz0x8ulZgv2dzFTzQGHwYFnQN_M16j6FgnZANv7xZopzxX2A97jbN7Mq4b7KHAkS16FfLpf5i-8R9GUpSaR3udQ2i66MdUgw6-hJsJbqDPGugnsA7hLGBnW5jzVFCozJGfyRQP7tnyO18-IRUfRbvyDjmFzUL_934CsALmhdsnFz6bJxLghTK7ii2Tw8CaIBJX3_AXQK3d7M5O66vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شادی راهبه‎‌های برزیلی هنگام بازی این تیم و گل سلسائو
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/664842" target="_blank">📅 10:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664841">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سرقت اطلاعات آیفون ۱۸ پرو مکس از یک شرکت هندی
🔹
اطلاعات محرمانه مربوط به گوشی آیفون ۱۸ پرو مکس از یکی از شرکای تجاری اپل در هند به سرقت رفته است.
🔹
رویترز گزارش می‌دهد که اپل به‌ شدت نگران نشت این داده‌هاست، زیرا جزئیات فنی محصولی که هنوز سال‌ها تا عرضه فاصله دارد، در دسترس افراد غیرمجاز قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/664841" target="_blank">📅 09:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664840">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQhxL0jvEAU_C8Kbz9KZUeN8BSt34fizKlMytMllLh7-ef_PEQiy4_SWonUHcwcfFeeiDJybWX7N1Q7s7Tg6rKsXfLeJEDI04-AgD_lvgiIGV9y4zfcB_YRG-emYAY2pKGG0S8hHMgrf9MpPr2QU63HaXkkgAUtWE5Dbij7alfNmYtJsF-yDjrJ4-CG8RC5EmE5bxFuRuiosEeGHUW2ZhXPhgiFvd-oemiZQ4Nfu2RyDvMJyE_U3XnFQtu99bRv-VQokr7NhOT4ermi0t8s1Rq8193uXR5eeQace6UHFA43kX5mLLUC-GRYEc1CMVoc_e5cVkyKFgpe57ODw9G5_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار تند ایران به فرانسه و مکرون؛ دخالت بی‌جا نکن!
آناتولی:
🔹
ایران با رد پیشنهاد مکرون برای همکاری در مین‌روبی تنگه هرمز، به فرانسه هشدار داد که هرگونه دخالت یا سازوکار موازی در این آبراه راهبردی را تحمل نخواهد کرد. عملیات مین‌روبی در تنگه هرمز تنها در چارچوب تفاهمات موجود و توسط ایران انجام می‌شود.
🔹
تهران از پاریس خواست از تحرکات بی‌جا خودداری کند چرا که این اقدامات می‌تواند وضعیت حساس منطقه را پیچیده‌تر کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/664840" target="_blank">📅 09:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664839">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
کیهان: این روز‌ها طرفداران «یک شخصیت سیاسی» برای اثبات نگاه خود در‌باره اینکه رهبر انقلاب گفتند «بنده علی‌الاصول نظر دیگری داشتم»، با بدترین شکل مسئولین نظام را مورد انتقاد قرار می‌دهند
🔹
رهبر شهید می‌گفتند «نقد کردن با تهمت زدن فرق می‌کند؛ مراقب باشید که کسی را متهم نکنید»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/664839" target="_blank">📅 09:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664838">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdmtZwCFgQWwdTJx6_s59Da1Ttle6h46B6s28ltwAHLNkQhrw_7IUGRTGK9Xf5mj3ZR7Rw402VlYP2_3RGyxoUR5ZZmyGo9IjvNdz5ncJgntRGZ93kUJlMQ0dwwM7Abx-LDvxLwKqRYY_rds9_U7QAI723dBuUh9FX5d6BXzyS0E4r3L2UesX41emfpILYgc1V2hYXRLJuiTtmP2EgWkJLqoi43wqVVTedWceo-RHXVbuDGa8jgwryfeaQDwZh0UBMZQYxQZFPEoECIq4dRfb2UjQVx-8bdryo0o76wM6FrnqdnM_aMEH74hCHf8c1b__CdDrFyQIrzc2J3I3P-onA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر نمی‌تونیم بخوابیم یا صبح‌ها احساس خستگی می‌کنیم، چی بخوریم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/664838" target="_blank">📅 09:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e1ff1a63.mp4?token=Vo_tALLn1mj34b4WANFydEYMNpX0W1ZQh9zGxv2RpIY1RNEn6kXAs5T4reTIg4pV8mWcp7uZ8LwbHORTMdot7v9ZgTCDYKr-6rbVVu0Y2W1mvovdEMmVjt3BYvYeLsGIszDzBr0cRiMr4gqWHSlCMxb7bkearuxmGDXQULJN7n5CgTeFmJZdHoxmptgSsY4pBmzWmdqYdpUIdOS5A3eaBtlJ7tD9DdTWK9y5POpDEUm1Z_JJ4teXH50Tq4DxodGZCXcW5jx8ma9oFFVG5a8CueCNxBb6DD71252aTz4XX2m-K5tHQv61CSDATXvT6NU44Gm_6jXOQ8DKr361Mx-wdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e1ff1a63.mp4?token=Vo_tALLn1mj34b4WANFydEYMNpX0W1ZQh9zGxv2RpIY1RNEn6kXAs5T4reTIg4pV8mWcp7uZ8LwbHORTMdot7v9ZgTCDYKr-6rbVVu0Y2W1mvovdEMmVjt3BYvYeLsGIszDzBr0cRiMr4gqWHSlCMxb7bkearuxmGDXQULJN7n5CgTeFmJZdHoxmptgSsY4pBmzWmdqYdpUIdOS5A3eaBtlJ7tD9DdTWK9y5POpDEUm1Z_JJ4teXH50Tq4DxodGZCXcW5jx8ma9oFFVG5a8CueCNxBb6DD71252aTz4XX2m-K5tHQv61CSDATXvT6NU44Gm_6jXOQ8DKr361Mx-wdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب و تخلیه اجباری شیعیان در حومه شهر حمص سوریه
🔹
بر اساس گزارش‌‌های منتشر شده، آب و برق منطقه شیعه‌‌نشین المزرعه در حومه حمص توسط نیروهای وابسته به الجولانی قطع شده و به ساکنان بین ۴۸ تا ۷۲ ساعت برای تخلیه مهلت داده شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/664837" target="_blank">📅 09:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
حملات جنگنده‌های اسرائیلی به جنوب لبنان
🔹
منابع خبری گزارش دادند که با وجود توافق دولت لبنان با رژیم صهیونسیتی برای توقف جنگ، جنگنده‌های این رژیم شهرک «دیر سریان» را بمباران کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/664836" target="_blank">📅 09:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664835">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66fb2b0eb0.mp4?token=lGuSfdbGmTO_OvL4znDAlZ33xnQJXJV3h6HqSMICaKFdVHCNbhdvp2e4tdHSHj47kujLKrQ1srhEAMSxMFNkKSbKlUrwE5oHd2ZUEfYroT_Fesftbg3Cf8nInHGAQxrhRpBFZl46wkl37Yy1x1TU1LeIRjq1WE_o17ELpa7SvpAMp-P1wLAMiUXwjdkQ6HAXvQapzLfzJo8my41WjzUPr7h1EFW8UbjabsY5MdITlTiVnKM7UrCcewkvGptM9axvqj9xxQm56_4GZ0vkPN24FupkOTwrI2DwdfRg5cTpbmoYDjCMgTFIHkO04ZakGU6FqoRVP5cBioKwaFr3EqbKVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66fb2b0eb0.mp4?token=lGuSfdbGmTO_OvL4znDAlZ33xnQJXJV3h6HqSMICaKFdVHCNbhdvp2e4tdHSHj47kujLKrQ1srhEAMSxMFNkKSbKlUrwE5oHd2ZUEfYroT_Fesftbg3Cf8nInHGAQxrhRpBFZl46wkl37Yy1x1TU1LeIRjq1WE_o17ELpa7SvpAMp-P1wLAMiUXwjdkQ6HAXvQapzLfzJo8my41WjzUPr7h1EFW8UbjabsY5MdITlTiVnKM7UrCcewkvGptM9axvqj9xxQm56_4GZ0vkPN24FupkOTwrI2DwdfRg5cTpbmoYDjCMgTFIHkO04ZakGU6FqoRVP5cBioKwaFr3EqbKVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
قاب احساسی اسماعیل صیباری، ستاره مراکشی‌ها بعد از صعود به یک هشتم در آغوش مادرش
🥹
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/664835" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664834">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bapW7JdEBGrgkuLMkvWB9t4Ey8hhWzKbwhxmkLdk1-ccbaS3-ioU5nkYgh1JcdnJy6tFo1zxLVrsDNbaIPW3_C9FTvAEzWkznrq18t3TWMpGNvr331w9NW0s6r4iaBe6VKuMyQN4xYZwg8z2G7aqI0DSb9CZ74wj-1b_0yJvG-M5K66UY5wYWuAaeWNgvZWi6sjbDCS5gjfjQqz-aXLpJfKWErDu7wRKYieDnWs7CmGEfWcK3UEXZvbtmYoU_B2WzoAVxXCeD6G7GlcY5AzOats6pESHMHMgRbnfjSZxFaSVsUpH5FPJnlpVNUnBKs3vk26pNaBMePwCvFFzHTkBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاراگوئه تعطیل شد
🔹
رییس‌جمهور پاراگوئه، در یک دستور به نهادهای دولتی و خصوصی این کشور، روز شکست آلمان را جشن ملی و تعطیل رسمی، اعلام کرد.
🔹
آلمان در بازی مقابل پاراگوئه، در ضربات پنالتی، شکست خورد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/664834" target="_blank">📅 09:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664833">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg0EhvCyG5d3aGXf-Y3t_1OhkFO204Lant0PBjGyRhdgfJ76rNSetAKK7NlMs4srEek_NMx02nknZibPaLQP1jbolM0GwiFAgvK7HRBiHe57Zd3OhATNiwg3F9crUJKwulcl0h1aDO3i5NYrVb574tzzR6U6RiUuHxOZu6lLMNy-YYFhP4UEPHiJ5dtumFqk9KoZx9hWJBuTR9Qr_6omFSUvtLHGIPojH95G9gWoZvQnRofH1GTGecBdKesdHs8PTEO54L6jLq0vBL-0V4BZnKtxPBgTSpGCKPELHqyDRhUYM-0SK_v-ZRljy6LrWdn3i7cqS2lMDvEXfuOsAMaY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی برق می‌رود، دخل مغازه هم خاموش می‌شود
🔹
قطعی برق فقط خاموش شدن چراغ‌ها نیست؛ برای بسیاری از مغازه‌های کوچک، یعنی توقف فروش، اختلال در کار و خسارت روزانه
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/664833" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664831">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c44222d.mp4?token=IKO5uvQWT9S3b8y2ecyCKiDMAowC1ryIHokROjqP9tn6yXf-f61G4OJR34KXtKBU5ETj17ErBWqW2R2uKkJL_bLmmBlMjwx0gJ_yVYn5h3tLAjlmEyv99NSQL-ojr79DFdnanrab8-pwlS6DyFEYmhWViqoekita-OjTva5TxAVukU47TwOkIUYtONzzfXUfd-b8lKVVlzikni6lcEJGJ6Stj3txt0YLVScJD2dlxHTfRXjvFOjVWonSVffU1KVzde1WXKTaroKOaTufb8ag_QJvriyR7g-Mij9c4FFIWNo-TFwj67eZvZOELErTLyD6noKjXGbvepfRi2EIUCXXVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c44222d.mp4?token=IKO5uvQWT9S3b8y2ecyCKiDMAowC1ryIHokROjqP9tn6yXf-f61G4OJR34KXtKBU5ETj17ErBWqW2R2uKkJL_bLmmBlMjwx0gJ_yVYn5h3tLAjlmEyv99NSQL-ojr79DFdnanrab8-pwlS6DyFEYmhWViqoekita-OjTva5TxAVukU47TwOkIUYtONzzfXUfd-b8lKVVlzikni6lcEJGJ6Stj3txt0YLVScJD2dlxHTfRXjvFOjVWonSVffU1KVzde1WXKTaroKOaTufb8ag_QJvriyR7g-Mij9c4FFIWNo-TFwj67eZvZOELErTLyD6noKjXGbvepfRi2EIUCXXVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پاراگوئه به آلمان توسط انسیسو در دقیقه ۴۲
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/664831" target="_blank">📅 09:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LG7BUS3rW-GLIDdkeWZXZMRfg7-TYnxab90tf9yL9KdnYrzLd5PgUSWnYEQR8ho2WZxuHJsVAgwf5sjC50Qz0lYdWfgRwg_RdNtF9mCy8I3lJxqhX5q0DS8PT8l-wPTk9_jMX2Ud36R188l31c0LMJDZABlKmGBa70EeYF48OJ7fUz9-mNKO-Ul0ldFqK-OcN9gZamnH9Rhf6-SjUiZA5kq6hamQiS6j22Qjk1fIGoUE0MhLVQKRsCvfdnVBhqUHemWGkwCvpFVxYbPHDBRyLcFtcpgBiVFpCFHKlBKKryD5hwaUn4C4_pji04Ln4TPlBn72quNHRnPXqG9Ms3YhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLvwaAnIMfne9VQHWPR88n_PCNzuDAm6hQWC2DDY7VysbY4J6mz3R4TVQqx9Q6QXdrKQR_Vn8MFMg2fQojF5SvCrAHyoSIrv1pfs-K-EGQ4XDcoWCFViai_AQ5TGdMvipUIy2beKXJ9D0HkSHW3wtwk_rbXCYDVijgbjUF6XtyH6-Ve3_slPkwneCLYpPzpSgh28FLmSN4ox54ganJItPGdkuDGdKo0CAnS7STZW7hc0xyC5mPllJs6-KmILspb6jOsP8van91-LB5hkEIcyGrGjrV_K7cIRZRRxhCbGs4ZBTO7lZy0jBbj9zY9V0ixNSe7W2isHbfNNgwd0k-lXVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
بازیکنان تیم ملی بعد از جام جهانی رفتن مرکز خرید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/664829" target="_blank">📅 09:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq2G04fmDEq_YlwxxBT9gugw1x4HDVKoA67Ac73z3l0O36tVYESvFegA7Lww2x-nTap6qEst-2EeFKCqpNJoP5Z-A7knvZvC4KEp743ArzmnKQL_ra5htI3abulpjDnMcwxcnUERugaq135UHnNtQi9VCwy6naJskzFYMum41-5ekUvDSxDvInGgdYe9iKF3KfIv6S54UH5zChzXkW4K9cu2Zi8_QNmQLz2MkHH-L_roYNRUiQ-wTWEgryD_1zr2n5ivkW7yIOFJiZVVTg4UIObPwRBaYaf349fA9fOq8GVODw1dQ-JIrFKkvmlMu3vvyg1rX1kYCni40HNWVtP7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین دیگر برای تو جای امنی نخواهد بود. این سرانجام ظلم است، دفن شدن در باتلاق وحشت و تنهایی
העולם, זה לא בתולה לך. נקבר ב ביצה לבד
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/664828" target="_blank">📅 09:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
مدیریت تنگه هرمز صرفاً در اختیار جمهوری اسلامی ایران است
رئیس کمیسیون امنیت ملی مجلس:
🔹
عصر مداخلهٔ آمریکا در امور منطقه به سر آمده و بازگشت مجدد شکست‌خوردگان، هرگز دستاوردی به همراه ندارد.
🔹
تنگهٔ استراتژیک هرمز بخشی جدایی‌ناپذیر از حاکمیت ملی ایران است و مدیریت آن صرفاً در اختیار جمهوری اسلامی ایران است. حاکمیت لبنان نه با خلع سلاح مقاومت، که با پایان اشغالگری و تجاوز تأمین می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/664827" target="_blank">📅 08:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نخستین شلیک موشک ضدکشتی از بمب‌افکن B-2
🔹
نیروی هوایی آمریکا برای نخستین بار اعلام کرد که در جریان یک رزمایش در شمال جزایر ماریانا، یک فروند موشک کروز ضدکشتی دوربرد LRASM را با موفقیت از بمب‌افکن پنهان‌کار B-2 اسپیریت شلیک کرده است. پیش از این، توانایی این بمب‌افکن در شلیک این موشک به صورت رسمی اعلام نشده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/664826" target="_blank">📅 08:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664825">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تمهیدات ویژه برای مراسم وداع و تشییع رهبر شهید  استاندار تهران:
🔹
مراسم وداع با رهبر شهید انقلاب در مصلای تهران، از ساعت ۶ صبح سیزدهم تیر آغاز شده و تا ساعت ۲۰ چهاردهم ادامه خواهد داشت
🔹
مراسم اصلی تشییع نیز روز پانزدهم تیر از ساعت ۶ صبح شروع می‌شود.
🔹
برای…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/664825" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664824">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBA-h8fs2QH2ajmYtq0JOHEuvZrG3oY_HaRhanneScR1LqE55rfz6rvNc7XUoYxOSPVHgGkwk57SkdbGsgB2UaHOAH68ggDh8mp-zcPpTUg3mgdf6FwXdac9dhs5Z6nE3EXm2WweASYkj0Nvy2Y-yaznHGw2Og0-cvuY9yKHsT7-pDf9jWFkZLdxi6tR0fSfnss1-nNrq0-DfkOcsaT72Mqq7Q6kfoBWnAcYy_DV6TMKrjmcYKWcMSHrkI35MvM5BWdH2ev6gG_sl5G4fMbsWDo29v9zt37oGY0L6e91KrBCV030nABRe3b8_KXV0aDTOv5u7POSe-Au_lLKVxSfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطرناک‌ترین جاده ایران، جاده روستای ناندل در آمل
🔹
از جاده هراز تا بالا ۵ کیلومتر مسیر که ۶۰۰ متر ارتفاع میره بالا یعنی به اندازه دو تا برج میلاد
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/664824" target="_blank">📅 08:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664823">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادارات شهرستان کرمان امروز با افزایش شاخص آلایندگی هوا تعطیل شد
🔹
آغاز ثبت‌نام زائران اربعین در سامانه سماح از ساعت ۹ صبح امروز
🔹
آمار کشته‌شدگان زلزله ونزوئلا به ۱۷۱۹ نفر رسید
🔹
گفتگوی تلفنی وزرای خارجه ایران و فرانسه درباره بررسی آخرین تحولات منطقه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/664823" target="_blank">📅 08:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664822">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3314d934e.mp4?token=lXUXVXrmmQZj8xrmkDJtU0AmcT-hQWRdk2rxdVgw1KWuZfeOnWFuB92IyTn0EbG37Y1-h8uVhCLc2A4V3gTpPcC3WPT9iRfmZefF1GKo9tX_tr0NAw1nu5SqQWiNIasfRg0JQ4QUCoJgxBVlrXRnzfWHc4Ko5XIMJ8INEYHxOmUc0n-l0StPVkwCvmMuxq-Vy8_WihdW9hDyz_LFs50MVBUsFqEgwo6cdyQhkWhkU51ly_cdGoLcQsfZ3hJLq2U-lNqlWyPeUORJpfqkCzYFKsq5RFaHh0U4pZqCN1-tXD1t8TcbHcI_9sxdDkbfVl4F1GEEdhoq_3DHsytywLe3KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3314d934e.mp4?token=lXUXVXrmmQZj8xrmkDJtU0AmcT-hQWRdk2rxdVgw1KWuZfeOnWFuB92IyTn0EbG37Y1-h8uVhCLc2A4V3gTpPcC3WPT9iRfmZefF1GKo9tX_tr0NAw1nu5SqQWiNIasfRg0JQ4QUCoJgxBVlrXRnzfWHc4Ko5XIMJ8INEYHxOmUc0n-l0StPVkwCvmMuxq-Vy8_WihdW9hDyz_LFs50MVBUsFqEgwo6cdyQhkWhkU51ly_cdGoLcQsfZ3hJLq2U-lNqlWyPeUORJpfqkCzYFKsq5RFaHh0U4pZqCN1-tXD1t8TcbHcI_9sxdDkbfVl4F1GEEdhoq_3DHsytywLe3KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش احساسی دختر ایرانی به کودک سیاه‌پوست؛ ویدیویی که از ۱۰ میلیون بازدید گذشت
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/664822" target="_blank">📅 08:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664821">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
دانشگاه تهران: زمان شروع و پایان امتحانات دانشجویان تغییر کرد
🔹
زمان شروع امتحانات پایان ترم دانشجویان دانشگاه تهران از روز پنجشنبه ۱۱ تیرماه به روز شنبه، ۲۰ این ماه موکول شد.
🔹
پایان امتحانات پایان ترم دانشجویان دانشگاه تهران نیز از روز یکشنبه ۲۹ تیرماه به روز شنبه سوم مردادماه به تعویق افتاد و همچنین روز دوشنبه پنجم مردادماه پایان امتحانات دروس عمومی است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/664821" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46e47cbd0.mp4?token=IP9poB-rfFcL9B9wI8NmW9a5jpsV2_LZ4vY6mvcdKm8cW-BaoBPaoSelJkXSQdMhjVvQ4KkxX6FrNLa60mTCRJdNJaeTV_KEnfVlArvcWoqQh3rhvNTc-XidWXG1AM__SKbogEbiR8-vl9PEtFihMZLiU2IspgABm_5iBz5Nne7x7fn5o8Akjm9z50fX6ECb8ZKx0HtYXqYvoi2gXd3zbRYMIDosk6kDnT4b8sSdGWmN2aKxeiDRTdgDcOAT5nH92nQVi-2lUrFseT5N01DNP7ADzk7duNV_ldez6oK8mhirBf5JoCJsspwY5cqSgGe3rxYq9v540lLEUfKSyRMIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46e47cbd0.mp4?token=IP9poB-rfFcL9B9wI8NmW9a5jpsV2_LZ4vY6mvcdKm8cW-BaoBPaoSelJkXSQdMhjVvQ4KkxX6FrNLa60mTCRJdNJaeTV_KEnfVlArvcWoqQh3rhvNTc-XidWXG1AM__SKbogEbiR8-vl9PEtFihMZLiU2IspgABm_5iBz5Nne7x7fn5o8Akjm9z50fX6ECb8ZKx0HtYXqYvoi2gXd3zbRYMIDosk6kDnT4b8sSdGWmN2aKxeiDRTdgDcOAT5nH92nQVi-2lUrFseT5N01DNP7ADzk7duNV_ldez6oK8mhirBf5JoCJsspwY5cqSgGe3rxYq9v540lLEUfKSyRMIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این تمرین، با قوز کمر خداحافظی کنید #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/664820" target="_blank">📅 08:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd8a86337.mp4?token=hPvUU2ED8dLt6T-bAEtua5wjSlXIp91nLWNnrk_KYF-hMQNHneo5KPFURLqWiIxKbToESLlRoSFAd1q8LzOlxWsR34NaIeQWBMvss-OZgFZVtz0pG3Yrhybn1X5ChS04Jt-aPS2nESpTnGbUJACLo1JsVgOYu_vn9r_JKSKbIdvoMiSQez46spwapz51tTw2pQuIxnJjUh8bpv9gVk_3d2J2p5qYK6KfGZodeYNpaZFEv6fTXS8rA-Do4spEEeAS-PX_DsdaT6MMN3xk2U4DN0Ku1bINJFWHC7igRuVWNqP07yFzOhTJ489IrTfkWeulx_sWhKxcw-zUPw8o5yk5UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd8a86337.mp4?token=hPvUU2ED8dLt6T-bAEtua5wjSlXIp91nLWNnrk_KYF-hMQNHneo5KPFURLqWiIxKbToESLlRoSFAd1q8LzOlxWsR34NaIeQWBMvss-OZgFZVtz0pG3Yrhybn1X5ChS04Jt-aPS2nESpTnGbUJACLo1JsVgOYu_vn9r_JKSKbIdvoMiSQez46spwapz51tTw2pQuIxnJjUh8bpv9gVk_3d2J2p5qYK6KfGZodeYNpaZFEv6fTXS8rA-Do4spEEeAS-PX_DsdaT6MMN3xk2U4DN0Ku1bINJFWHC7igRuVWNqP07yFzOhTJ489IrTfkWeulx_sWhKxcw-zUPw8o5yk5UjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هراس اینترنشنال از تشییع امام شهید؛ اعتراف ناخواسته به قدرت بزرگ و نگرانی از تشییع باشکوه و میلیونی
🔹
مراسمی که قبل از آغاز، این مزدوران اسرائیلی را چنین آشفته کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/664819" target="_blank">📅 08:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664818">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8wdRIwZPzVZaZW5AcHZeUja11zoUi4xlA-Oh_PzbsRum1p_EvAxPAFM0RMWp8FC0Nl9g2gwcPZdHCrAGKN9Cyq_VQUizXlprDmXYERns4jAl4h5IENl1BPDLDq6y2XyowvQWGTIhenc8np4gTKsR2iqdH65WUkGRGbcoD6Lbgmy63Fji2KswJmgovMq_5cyKl35pWQNWu-eKSxdKoksGezaADbpHX-YMi8zxFlAWGu6oafbL2jxxY8_T_DqE6Mm7WyBwJCiB3sXn2Uctx09DCAUzgvuudlc28VHrxo3XWyn4B3mAV7CySrwAp9ZmcCB76jul7DCD_PNWaw2e8bNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش محوری پایگاه موفق‌السلطی اردن در جنگ علیه ایران
🔹
منابع مطلع به یک شبکۀ روسی گفتند که پایگاه نیروهای آمریکایی در منطقۀ «الازرق» در اردن، به‌عنوان یک پایگاه اصلی برای حملات علیه ایران عمل می‌کرده است.
🔹
در مراحل پایانی جنگ ۴۰ روزه، این پایگاه بود که به نوعی نقش پایگاه منطقه‌ای را برای عملیات آمریکا علیه ایران ایفا کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/664818" target="_blank">📅 07:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664817">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
مسیر عمانی هرمز با اخطار سپاه از کشتی خالی شد
🔹
بعد از گذشت یک هفته از رونمایی کریدور جدید عمانی برای عبور از هرمز، داده‌های دریانوردی نشان می‌دهد که به دنبال اخطار سپاه، این مسیر اکنون با توقف تقریباً کامل تردد مواجه شده است.
🔹
از زمان اعلام مسیر عمانی در تاریخ ۲۴ ژوئن تا پیش از این تغییر اخیر، حداقل ۱۲۰ فروند کشتی از این مسیر تردد کرده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/664817" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664816">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سرنوشت FATF بعد از تفاهم ایران و آمریکا چه خواهد شد؟
محمدصدر، عضو مجمع تشخیص مصلحت نظام:
🔹
اگر با توجه به این تفاهم‌نامه تحریم‌ها برطرف شود و ما تا ۶۰ روز بتوانیم نفت خود را بفروشیم، طبیعتا این موضوعات در کنار هم ادامه پیدا می‌کنند.
🔹
حتماً بحث FATF دوباره مطرح خواهد شد و احتمالاً وزارت اقتصاد این موضوع را دنبال خواهد کرد و به سمتی خواهد رفت که ان‌شاءالله ایران از لیست سیاه خارج شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/664816" target="_blank">📅 07:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664815">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX5cBPHavGG-NND8d95EINvNP7MVXVOI3QECl4xKBUfNj5wb7rFrtsH2LzuLY3f7p9KMkrPqi5PrriLrMnv9XhDya2K0qsf0_9oTEksjIT89yO8_Fv49cjXzChvWqILXnNGByUgy2BMZYAjpm2WMIzdPIg1YiK64iU6bH8PBTPA8UAGXag5MqUT_4oS5tXLY8jXg6sVROCbhxZBL3pN3xFQL12Ufc8psU_icHpec829kfdE4m_Zt1G6MxATwNVZutNO80PqcL_DQ-KfGVVnTJkB5rAQwJ1JIVOq4hkiVdt60RVswaOF4FBopAyQuo1W4F0n8A8QuI6XyofN4-J8x_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدیدترین بروزرسانی نمودار مرحله حذفی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/664815" target="_blank">📅 07:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664814">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCukFvaOXz0BxstlNXOGLUk4F0HI5bkLGYfb_8JsXXbsyc63MRSqF8J8oM9j6XYxYBBEd1GlYkFRu0ZFNWwvhjHyW-OOhJXWIFzVqUbZKKnnuhV9Llby_qdqwYajaCcVpXNeTV9INmd9Md2y8cwn25_OHo4i5lWCtfHhaKIKAHbGBJu67Ac69vRML-wW5Cnf-KJvHZWkBkIEhgIDmWNQodgU6C3h1hk5djJuOjAVYDk67zNlYNPr2W9Jw5Y3OXvoti8m4k_HAG_41tdx8iMyNnK5d0102CbQKaFR5FUw3LKeZfmK3N1dpDN-F442MFF81b8pQNCiG12avzN-Q7TCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تصویری از سجده شکر مراکشی‌ها بعد از صعود
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/664814" target="_blank">📅 07:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664813">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
اسکان و فعالیت‌های تفریحی در حاشیۀ رودخانه‌ها و ارتفاعات مازندران از امروز تا چهارشنبه ۱۰ تیرماه ممنوع شد
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/664813" target="_blank">📅 07:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664812">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCMVqlwnBnIw1C-pVgVhJFnCCMsml38jeZs85hqtlMUe6GO9aCXolVcd98PxkrEi159jxCrGUXKUkSH2o2BIfHeAb0JGmMdlMVdZmiPpLMffuWFn6iFc7qb2Le3rpSwZ1D8J2dkBL0HYPKFJdIZJu3eoa-fTthNHZlC0-S8UmvOJbb8_LLGjNE1MCcLGdBH6GBxgb-Y8Kkdm_YNHFHYDa9An1j64oc4uHjG5MHOhSgnJQPdBRSxnuca7l6-bEo-SsdPcv3-ykun7dvbwSgxQQYey_6NbbirIq7bFX03brsnLh4Kb4ziIB_eK8gisTfv5CG_JstsX228kfLRlw0trlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت دو پاسدار در درگیری مسلحانه با گروهک های تروریستی در پاوه
🔹
به گزارش منابع محلی، شامگاه امروز یک درگیری بین نیروهای امنیتی و عناصر تروریستی تجزیه طلب در شهرستان مرزی پاوه در استان کردستان رخ داد  #اخبار_کردستان در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/664812" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664811">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سی‌ان‌ان: ویتکاف راهی قطر شده است
🔹
شبکه «سی‌ان‌ان» به نقل از مقام‌های آمریکایی گزارش داد که نماینده ویژه رئیس‌جمهور آمریکا برای حضور در مذاکرات با نمایندگان ایران در نشست دوحه، راهی قطر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/664811" target="_blank">📅 07:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664810">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K79hu-NxZFPMSG6tmG2JCUdZw5rmpiOQ9IlhODpaD7SlJLYh-LzczqnAm04lkhysMBNRdzh5761c4DH5EuxOaV4Y4HwJ3gUdYE56XcrZmh6ZoeFKoNRAI6Q8x4dFGFolDEPGUxQn5NvO8RG8MDCS3vBsxHYoRajvaY8mDBe6fW38zAgA8BwHNZ3nUWbcLoz85AH4EOf68boZFmxXTOqX8QVn_DS2um3Jff8vk15a4e4QPFL3ZGYzEAhGe3lB-80EeG1O41SKsZOiujR7J6HEs_KqCNJnhIKiXWvsFJVEb5MQKhXF2MMNGd-os9ESvCWO_ZatpdnFoLGEWijs6WZblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۹ تیر ماه
۱۵ محرم ‌۱۴۴۸
۳۰ ژوئن ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664810" target="_blank">📅 07:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e56e13416.mp4?token=DpBWMFqW3M_tWo76YhVUf-zw3VeojH64YAaxQrwfZdcyutcCa3Z3mL5Y4NuI6NqKd7Fg-kU6xsBt16CxLg25d4WZPpkmQBkwhaJYf1W_C8vfinOtUV0t6jTtriMRNkz7DMtVTn-GTfImOF1lr9UFc45mwFk1GQWwKQWwUErv12m4qlCd_7lBCmAbuNS_oZp2ExMnFwP37HuZGK0nyW_JmufwgqkfJGgSbQjet8zYhUPcpQdZGqBWdrkqlew95agqLyXdWDsD06YcvpxXCs1738zFIpiKX2DedmqVDrWoY0ShjR_IEX5vBBAKvgyr7ZIP8mZiYzD8qoJSWNA3f9W9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e56e13416.mp4?token=DpBWMFqW3M_tWo76YhVUf-zw3VeojH64YAaxQrwfZdcyutcCa3Z3mL5Y4NuI6NqKd7Fg-kU6xsBt16CxLg25d4WZPpkmQBkwhaJYf1W_C8vfinOtUV0t6jTtriMRNkz7DMtVTn-GTfImOF1lr9UFc45mwFk1GQWwKQWwUErv12m4qlCd_7lBCmAbuNS_oZp2ExMnFwP37HuZGK0nyW_JmufwgqkfJGgSbQjet8zYhUPcpQdZGqBWdrkqlew95agqLyXdWDsD06YcvpxXCs1738zFIpiKX2DedmqVDrWoY0ShjR_IEX5vBBAKvgyr7ZIP8mZiYzD8qoJSWNA3f9W9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروهای زرهی رژيم صهیونیستی به اردوگاه عسکر الجدید در شرق نابلس یورش بردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/664809" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664808">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
شهادت دو پاسدار در درگیری مسلحانه با گروهک های تروریستی در پاوه
🔹
به گزارش منابع محلی، شامگاه امروز یک درگیری بین نیروهای امنیتی و عناصر تروریستی تجزیه طلب در شهرستان مرزی پاوه در استان کردستان رخ داد
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/664808" target="_blank">📅 01:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664807">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91cbf495a8.mp4?token=Qla8ABc6DRflUc4AjYkSg1SRp1FSBvxkIMqs4IX4Ua_BVyW2f3PH6nZjJpd7Wb6q43P-uwDBhJMeo3EkhY9lbUtOj-aSiIsV9GxS0AeS6pZaKixtOXXMGP-xYurb4hlsQswVhokXzSXyoBEampI3Pk7pgGmiVADNgGuox2jTrkUxQG67HNUedjY7F3tvWdKIV_Gnx15u-G9AGupRzJUHN3GAfbXXoaGwfcmYWQBM4X-1R1tX7_BNFOnDtnnxmthy39O8DEaoz00JsmdA-ofgDtf8p3FNTvac4sF72vqNIn7KR6jpO0VVHX0FNaTBzVDITNaEeqXghS66VatDCpDtMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91cbf495a8.mp4?token=Qla8ABc6DRflUc4AjYkSg1SRp1FSBvxkIMqs4IX4Ua_BVyW2f3PH6nZjJpd7Wb6q43P-uwDBhJMeo3EkhY9lbUtOj-aSiIsV9GxS0AeS6pZaKixtOXXMGP-xYurb4hlsQswVhokXzSXyoBEampI3Pk7pgGmiVADNgGuox2jTrkUxQG67HNUedjY7F3tvWdKIV_Gnx15u-G9AGupRzJUHN3GAfbXXoaGwfcmYWQBM4X-1R1tX7_BNFOnDtnnxmthy39O8DEaoz00JsmdA-ofgDtf8p3FNTvac4sF72vqNIn7KR6jpO0VVHX0FNaTBzVDITNaEeqXghS66VatDCpDtMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین روش برای برش میوه های مختلف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/664807" target="_blank">📅 01:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664806">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c4b3af88.mp4?token=mYUuRZpGT7doAUh0CYCa1SS8PAL34x_H99SGz1GV8Gx1nKIPYFfGXh5YZh0u_MLeg4IZmSnvyq_gNmxZRJnB2drJnXhtdPlx_33g1VZcp1VndXNfbhoLeA3NbR5KMBrfMjMiJZSngq_7L5pXjZZjVbsECOkoAw8upFQTDL1p0NYCIE2kXmbfMsn9s4zdN62orjnzFfgdsaib0NhVCNWv4zsUZPTmSUXLLt1udwR7M5sXkjnbrRoHCZoFBQS4fLl54KOHpOGDEf_xvF6QDR8L1ubWamlCHAxx3HEqiLEa0BnzvDmZi9BOiip4BO_DzWF_ItPyZh2McNVWuMAZjZmBnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c4b3af88.mp4?token=mYUuRZpGT7doAUh0CYCa1SS8PAL34x_H99SGz1GV8Gx1nKIPYFfGXh5YZh0u_MLeg4IZmSnvyq_gNmxZRJnB2drJnXhtdPlx_33g1VZcp1VndXNfbhoLeA3NbR5KMBrfMjMiJZSngq_7L5pXjZZjVbsECOkoAw8upFQTDL1p0NYCIE2kXmbfMsn9s4zdN62orjnzFfgdsaib0NhVCNWv4zsUZPTmSUXLLt1udwR7M5sXkjnbrRoHCZoFBQS4fLl54KOHpOGDEf_xvF6QDR8L1ubWamlCHAxx3HEqiLEa0BnzvDmZi9BOiip4BO_DzWF_ItPyZh2McNVWuMAZjZmBnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از آماده سازی محل وداع با پیکر مطهر رهبر شهید انقلاب در مصلی تهران #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/664806" target="_blank">📅 01:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664805">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حمایت چارچوب هماهنگی از اقدام دولت الزیدی در مبارزه با فساد
🔹
«چارچوب هماهنگی» بزرگترین فراکسیون شیعیان در پارلمان عراق ضمن اعلام حمایت از اقدامات دولت برای مبارزه با فساد، آن را گامی ضروری برای بازگشت اعتماد به روند سیاسی کشور دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/664805" target="_blank">📅 01:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664804">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
انفجار یک بستۀ پستی در موناکو
🔹
در پی انفجار یک بسته در مقابل ساختمانی در موناکو، سه نفر مصدوم شدند. به گفتۀ منابع خبری، مصدومان تبعۀ اوکراین هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/664804" target="_blank">📅 01:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664803">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
چین: اسرائیل باید به آتش بس در غزه پایبند باشد
نماینده چین در شورای امنیت:
🔹
آتش‌بس در غزه هنوز اجرایی نشده و کودکان هر روز در غزه کشته می‌شوند.
🔹
اسرائیل باید فوراً در غزه آتش‌بس برقرار کرده و به قوانین بین‌المللی پایبند باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/664803" target="_blank">📅 01:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664802">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439f50420e.mp4?token=jTOxc-bR06mCZ8r6P_c3JH0l3NMqHqs24Hxd6n104_VQpCI08shBnj5AbWSZOhE8lNGqun8604amaD1LytY8v1zlAXrf32Hu-77nEipU0PJVXt1DRK-z2GChyOX2PEuq1b4VDblGxAP9XnivanVgUt3hnr8UG1LNVbX5e3-uwpuxDWZiyGnp21tPdqBBD_JHy9bsYXM1lZXVxgRDVxSsXvcEReqlDp_RW02dAkCDi9u1ftRxlyHMmATcw770rpGle9nKPaha8ADTZbaEIPsT9-1p5qibfv5Sijl0IcX5C3MIXdZaHcgVaZcgsApBvSbFFz5GIZ1GNE1_ywp5cWsMWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439f50420e.mp4?token=jTOxc-bR06mCZ8r6P_c3JH0l3NMqHqs24Hxd6n104_VQpCI08shBnj5AbWSZOhE8lNGqun8604amaD1LytY8v1zlAXrf32Hu-77nEipU0PJVXt1DRK-z2GChyOX2PEuq1b4VDblGxAP9XnivanVgUt3hnr8UG1LNVbX5e3-uwpuxDWZiyGnp21tPdqBBD_JHy9bsYXM1lZXVxgRDVxSsXvcEReqlDp_RW02dAkCDi9u1ftRxlyHMmATcw770rpGle9nKPaha8ADTZbaEIPsT9-1p5qibfv5Sijl0IcX5C3MIXdZaHcgVaZcgsApBvSbFFz5GIZ1GNE1_ywp5cWsMWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت به کره در حضور انبوهی از معترضان
🔹
هواداران با کوبیدن طبل‌ها، شعار «هونگ میونگ بو اخراج شود!» سر دادند و به سرمربی سابق توهین و ناسزا گفتن #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/664802" target="_blank">📅 00:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664801">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حدادعادل: رهبر انقلاب دائم مردم را به حفظ وحدت دعوت می‌کنند؛ از «علی‌الاصول» برداشت غلط نکنیم
🔹
بیانیهٔ رهبر انقلاب باید همه‌جانبه خوانده و تفسیر شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/664801" target="_blank">📅 00:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664800">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750487189c.mp4?token=hgkwPdXL8KkPMJ_vDFmDrPCZH6vqgy7GxYKmMNqO4NPL1REKHSBvov2Vu2-aFI0yVyqujGy8gcEEUDQU4VGqnf4GRZWEpctKewOevFBpT5xxuO9nIbrecKQN5xRCN4dyhgSxtRfsYbrVAPXrUhPIy9oinxuqN1nnb-X60hanZeVTeLjd7rmPEbIrXplUqXc3PLBlPK3aXfqDZoO5bHlC8nmvfP0pKv-1w7Eo56QdvecQe33b0q06vloGBHJwhAX_YN4ilQ9z060gjn3n4lorLqmIUCVlzXzlKO_WSPJolWKf79YpOOaPBmvQQd7Pf8e4ejAp2zmkdxpzgAosYGOfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750487189c.mp4?token=hgkwPdXL8KkPMJ_vDFmDrPCZH6vqgy7GxYKmMNqO4NPL1REKHSBvov2Vu2-aFI0yVyqujGy8gcEEUDQU4VGqnf4GRZWEpctKewOevFBpT5xxuO9nIbrecKQN5xRCN4dyhgSxtRfsYbrVAPXrUhPIy9oinxuqN1nnb-X60hanZeVTeLjd7rmPEbIrXplUqXc3PLBlPK3aXfqDZoO5bHlC8nmvfP0pKv-1w7Eo56QdvecQe33b0q06vloGBHJwhAX_YN4ilQ9z060gjn3n4lorLqmIUCVlzXzlKO_WSPJolWKf79YpOOaPBmvQQd7Pf8e4ejAp2zmkdxpzgAosYGOfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پاراگوئه به آلمان توسط انسیسو در دقیقه ۴۲
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/664800" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664797">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ChtFv6y6aE3XnoaSxxabdEb1ReKOuAv1wzVdwK99k_99-_84GxgYxlAghcyVjyEyMti87HV7KImauEnfdPURSF3dzgABL66YPdfr6nZw_RLEqhtw_ieVaLUOP5CrHEHmEJJ9HRO09RHKlUEDU1sII6E1LzG0xc8tRKrV6e6yBgAaQQg5RUgtQ-n-z1yuP9q6w4RTcIV97uFGafGTkyNNTWSNLmncFtYcgNWAt2jki_SqBVJr6CYK92OGMaE4XJ428KNNIQf8cYO44yy_uB5GcICSfW2DTuY-dkpuuJOP-CpTnrk9GYofEsyOzc3VaDo4iCXKEBcQIf5-tdSqlv7e9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVpcgOZKKyOIN7yMYWgLEkq5mOI9QSgjRavhpcmbYmLnyA4XyqveMT06aKrxb8GUptBaKgsMKipD6k_TZ3-e423chon4AN-8NOTRiVLwhLnR2xQulIUXsnS_BM2MTxJIDBntwk86IeOwU7f3y6firdXSH-979CN3wDT8JbekIMdWkeiqR3WpY2l6TdkggLiwW42LYqLVw8iwbCVKQPBjQ6xsQsa_m_ICHgAja63UrgUnW1Mong6D9zwJbC5lAdcHe_WGV7vS-D7UukjIk1uP2_NBsyQzD8InIaBqDOTvOsw6R4qijgq2W5yBB4lggB7qOtr426N7ggzp8N-0Adio3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3HSODwJ2yGO0bGPMhmIBDpOAOrfztlMTBYED7-bZ61pDycoK7Kx_opfe562Kx4BN0-vKs4Or5zdueSbZS4pCnGCVrIsa4VzF5pxs8E63VZjn42qOnYLt0fyTGEtC2DqC7mgYt3WyGxTAwZGjKmkWu3gYpxiksNpQE0b65JTm9IzQxbGxTGhz3GYlyHkkW-TfsbGNPlafiRCygHycyZkYPtBFO4g9Shm9hLYQZw6tNfJ-A8IY5s7By-RfbcpZnD5u979Gh6JSu4PNVaE8FUf4CllIQSG1V0YrVGlohxMRNNcLshWnoDue5Qs4eKUc2g_PNW9Jo8_hHz8pVPJec57sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر زیبا از ماه کامل در آسمان امشب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/664797" target="_blank">📅 00:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664796">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTZEt_Qi6aQjeanTmt9ZWPbkV2KLot_hOMn61o-799rRzbXE8rWBKOO9YSbWHgXGTzmpUooqPnLp_LxzVU8T-TG8DFHGkbwS_SSkJe1b6sgq7-qkmREIMQMd8p4s5Lkw-epHIeS0vjNtmmwbccE8CKG_H32qtREv1WDvKWnjzgoSLVAirLaP4v7u3dBjABAmzSWG7Yb0rYOMeMNqTOVpudjTabi0YpKsXUAdkko_Wqu43efvK_5Kke6FAhDs82sELpu5wfGjLJVI2tgd9RPq4gdjoszW9HXdyU13bp76a9HkDbmkUS3OSrmMf-vHo79dlz0Da3r1cjD0vr4urQSb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت رهبر انقلاب، نه یک اتفاق سیاسی، بلکه فصلی از حماسه جاودانه کربلا در حافظه جمعی شیعه و در امتداد آن است. مسئولین نظام جمهوری اسلامی باید بدانند خونخواهی قائد شهید، در واقع  خونخواهی سالار شهیدان کربلا است
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/664796" target="_blank">📅 00:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664795">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28149bc86.mp4?token=S_0RJjd4yp6z9JVndvOkMeUHgFvLqusYONgf-fAQ1DsQJKWoCdNiodKyVimmo3LVV_C-U9YW1jrzF8xTMrA9GVYr5iLT__XZD6dTt-RQj1QGNkTnBmhYJcso2YW5U6I-fVSNJXvDV6PTq7T5rCB84M20JgtQcDQVD1v_7caPoI3mOfeQH2VOqApNMOdmuJfSuK6npIGRayGaimahMSIB4XZIDXMa6iez76xgn_TdXPJHv7VtZLBmMzXm3F4Z4oKyireUbSKamapgDlnLreSgVqg6R9CPkzbIf73WpK1ERXZRWsHfFh7O2LQTuMNMwC0wmXaOxskK3vYIdgkRV-0wFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28149bc86.mp4?token=S_0RJjd4yp6z9JVndvOkMeUHgFvLqusYONgf-fAQ1DsQJKWoCdNiodKyVimmo3LVV_C-U9YW1jrzF8xTMrA9GVYr5iLT__XZD6dTt-RQj1QGNkTnBmhYJcso2YW5U6I-fVSNJXvDV6PTq7T5rCB84M20JgtQcDQVD1v_7caPoI3mOfeQH2VOqApNMOdmuJfSuK6npIGRayGaimahMSIB4XZIDXMa6iez76xgn_TdXPJHv7VtZLBmMzXm3F4Z4oKyireUbSKamapgDlnLreSgVqg6R9CPkzbIf73WpK1ERXZRWsHfFh7O2LQTuMNMwC0wmXaOxskK3vYIdgkRV-0wFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌صحنه داستان اسباب‌بازی ۲؛ شاهکاری که نزدیک بود هرگز ساخته نشود!
🔹
در جریان تولید، بخش بزرگی از فایل‌های فیلم به‌اشتباه حذف شد، اما یک نسخه پشتیبان که روی کامپیوتر یکی از اعضای پیکسار بود، این شاهکار رو نجات داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/664795" target="_blank">📅 00:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664794">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d58b8227.mp4?token=c4hYzOYY3JAcd5Gx97P0MfYwgmHq6clBoGt88KODYA71vV7Ku_0d0Z6rAhvkjMSE1dziZmZLdUjOmwaCTLuhyLvzXWElEgOEACJc1rZbrc1QoHJZd2BxFr9YNvYjnWz8RWd_ekwSheUPfhVJA2h8UJheRX2TK-aTTQJU3eCFCFTNIn_g162NXwAraKQr7p4_Z8xwAeWEKQHQ2ZMGdv-KGclOgyoS8uHxq0j6srtTZSRbRM3ns7DNPClMEEYnwEOxNgHeSemEC6goZuDA-SCwbvEgOkcebE85OWxZcF8e7saRdG4gET_s-M-7i7QqcAG3_GuAH9bLJjhHhBGBlqIrSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d58b8227.mp4?token=c4hYzOYY3JAcd5Gx97P0MfYwgmHq6clBoGt88KODYA71vV7Ku_0d0Z6rAhvkjMSE1dziZmZLdUjOmwaCTLuhyLvzXWElEgOEACJc1rZbrc1QoHJZd2BxFr9YNvYjnWz8RWd_ekwSheUPfhVJA2h8UJheRX2TK-aTTQJU3eCFCFTNIn_g162NXwAraKQr7p4_Z8xwAeWEKQHQ2ZMGdv-KGclOgyoS8uHxq0j6srtTZSRbRM3ns7DNPClMEEYnwEOxNgHeSemEC6goZuDA-SCwbvEgOkcebE85OWxZcF8e7saRdG4gET_s-M-7i7QqcAG3_GuAH9bLJjhHhBGBlqIrSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کناره‌گیری سرمربی کره جنوبی پس از حذف از جام جهانی؛ تلویزیون ملی تصویر او را تار کرد
🔹
کره جنوبی بعد حذف، سرمربی‌اش رفت و تصویرش محو شد؛ بدون توهم توطئه، بدون تهمت تبانی. فقط پذیرش واقعیت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/664794" target="_blank">📅 00:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664793">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYeMZn2r6VRIV5cplZHb_o7LeNm6Tz5cLryrmPmrDbvaxmZv4K7FULJyGot9S3jIxQoaUAzxzgtGhYjpIU1xpUVTFoGqCVJhnGFcXJe1cgc92eNWJ4lOywubsiseScYsrT8glmMX2dMwldHkHf000sXO1QgYPQeCO5v38kLXLLCiT3DggRAluocBJdZoAcSc8jx53KlM3p7YrVoPMm1Z-2agPBfQQ5-qbWn40L2q28uetXb2lpBbyeAXPNKoKphINPgoVR0b8ubKpvx_MxOmhBFS4wekjjtXEjwH-MjSHoHwbXHwTQSn7UsI_TMzftrahQ-jGCZEDSvQt5Q2TfB_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_پنجم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید بزرگوار مهدیس نظری  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/664793" target="_blank">📅 00:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664792">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5214eca511.mp4?token=iy6PVcTBo5klERhGpKvkAwj28qLAoECe0XJI6F63ulgVOgpxJmolJdPLX3JHzoqnS6P1EJWR-tsyNHqgsJs-toDOu50jXqptGmlCi59nTwmcwkqUsjhkvn48Fa_s7OHPBr9CfuuFNDha1SlRpcl__IfAB6PumPlDb5CugHzOUCWM6zlyRUorOaHtkTYIEq--M7uXOMAvRnERdrwcxOD0QefJHJEN56XFqo2XV21CgM6SP9gpAfPGPFSrpj8fMbQlfsedVmcikZPQkyvS5ytE7A0v6NqK5gmzUCxEOcGw_6HwQkPwvzkBd7G54YkFBnAMdeI2pYmx-pSKKRobFdsTag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5214eca511.mp4?token=iy6PVcTBo5klERhGpKvkAwj28qLAoECe0XJI6F63ulgVOgpxJmolJdPLX3JHzoqnS6P1EJWR-tsyNHqgsJs-toDOu50jXqptGmlCi59nTwmcwkqUsjhkvn48Fa_s7OHPBr9CfuuFNDha1SlRpcl__IfAB6PumPlDb5CugHzOUCWM6zlyRUorOaHtkTYIEq--M7uXOMAvRnERdrwcxOD0QefJHJEN56XFqo2XV21CgM6SP9gpAfPGPFSrpj8fMbQlfsedVmcikZPQkyvS5ytE7A0v6NqK5gmzUCxEOcGw_6HwQkPwvzkBd7G54YkFBnAMdeI2pYmx-pSKKRobFdsTag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس کودکان به شهادت رسیده لبنانی در حملات اسرائیل به لبنان در دستان کودکان در عزاداری محرم در شهر دیر بورن ایالت میشیگان آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/664792" target="_blank">📅 00:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664784">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnlNHMMsk7G2CO6L3diTiiX_Yu8iad7t-0GTYaJoPF72ZKKTGc69ohQPAK9zW5jN_JnmIDVmtOEJu6BXpD8Q0y1-knhfVaaKTDCz_GzHaPbViQ5t1DjKfNwQS1vNyB5zNz1ZByfqGj2eyYLFtfHwHXbqNrPHdSRAj1FSut94J_X64tEo3KwJNIYr-ouaat2XVP-PNk1hZ24XK8z4EPcMJTCVhBTCZcEOn2ombM1EtLQ30nRvxCJgLBcUTaWwSYR0wByT_cIhKbWPgAHABxogvMQFv87OaOTwIipUQXKiG80vJ3Y4nTJxE0AgRqp_MPR7e8OUUNwRzpNKZjr7pM7SnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-UYWlvj8yPgfIYp6DoMr5LoetSApTYcLYzb0fPodRz6uNLDstZ6_v8XcvsFiD3tVvr9LmcepSHWn3UyKNHQ_rC74R4oE3G2wqeUruvlbAUyo1yocWSJXG3bRFsmLwqr9_XCbEPxAK53KyVmFjKnwuhes5AqdeEO2qSA8TTOPEYfeFHNwYVsizCMN3E6qj9z1Y8i8dq6mfhd5KwBtLT95Kzr8aBpCboOaOpwM0WokoecNdUKK7MMQQ9aEWXwMED5qMl4NhxH3nhdCgNrk-zYFhhlvnsRwPMCpn1yUPQzyyFVpEA1wXpA7NFh2KeuRwvy9kOFMUOoZJKuDnPxbBvKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNBcJjMzTwBpkgtqLAREyCmDqqhJYV-1yLUfF9x8hCLQVVz7MRBckMFE6mgNFepNXMaLeP1E_XDT2Fzc__DrO1UHvScpcSM8do6ftGEKdTJF9ojHNPezgezUD2dNtbnvK5BpF0OxkjkBaIqD2Tx2hEWgfPwoOuBi4Aso6shJkhaA43OtgfiW4vpPQRC_dS9VCon49NlE2e6mw8Qz_KVKdMbkqNJ3774PuMKt4iTJ6uIxEeLjiEXka25Crh06KZ9DGXPx9fYJGY4XPEvnNWVa08PoT08bX6LLC_erw8G9O2vQD39nQZ0kW-WDMvYUMmBgY3FxE1NOlEIvAm7K67Xfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diTeBKWe70pfr4hsLJ05PBjdJfqamlzrJQD35fyq09Zpj-Y07f3Ndjum0uxuoszYr4Lpvcrn-7CrmxxD1Wn1RROdSvaM_3ku1BMjAirGTCOXtILvCpIwWx7SKhFVIRIfMms6DW39roHpr1l8l-En35uqzAw6C7iFlSbGB2p3RGN6buBoQ90T_oZK368C3LYhh3pJlA8ifU0HCtlq89P7TasVcxk96QGwGX11FCTN8uVM3dEv9tuVD2Nt2Te19aYSZH75HhlAIebbCc-Qza1Yv684SiSzUMfat-Wt8payOTyrZXtuDNuBWSijZ1XLhabUqdzeHT14GXjH4bwxpO6Fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2e6wNltHelZIJQ5-k6ZauvgwIons2Qom4RwmH50325TWkNrvK2IqGx6iS6_-E4SRJfUc6qxEkyiZJEawgHiWhMLrrF5L-EfQCaCB4Bb9TH0w4tRsXZ5ZmxWrltT9UOnUBPKM22uC2EQNNIonmjkLY9-ZKS6ayldKwaJ4IJ05h85cz41YT1gWtp1_1E9GR9FA1x9m93rTCEB4jRLu81XXOA-UhV4MluNdKHq_0wbVarwDK1vmosDpXHxa9EPstf4aMvQdjf3KCd_An2IRCMuOBskxh8TtY-WQydA9GMa0ZaFgA4j6y090oIbyXdyNhMG7YBcgPj7LVXittTzt12f4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUqGnmDAi_wRJLetNQsDluCXgZfspLVZUXBoI11E3-lMPr8XCNOkfdXKk_Q7yDFKoJcxRLZ3EcjUtd1Ye5P65Wb66EI7Pv--4rH1Zmj-_KYZAaYyjaxYTzsmPuAWmdxatnWDAEh5wIAlz4KevMMLB-kFhcGZGlIBMsEHVALDnI_iS_FRy387LPy3fJFlEK6tTERKEHWzso-gBWEXodmGomKvN3k4WQYEbhZscWCUnKEhYweLqVQdqBBxzW4q-DMgToqOUFl62qovEbNrMJggX4Re8P2jQU0GdtIFG8U23F1TELYonT943m0wz9-7PsaYTj6uLlRA5BaWQ52HZSMOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCUhamKJDdoReQbe5h8AEOrfOgxnwq-RyhPK2OwFB7semQa6phHbVbC3cofB_61d8Zwtv5Wr9qxDAh09WugKxx7r1Ela4XRQUJHbeBjcoCtmCTDPmqV97RrOvWh8ag4s_W42iRc1fHBJbGVDqAW8B4ES8dNMWRvJn9tIMCrelDrd8n4FLti00dpnYEsMqhXH7HExjICqAZmQ8O5mm_LSQo9OzQ1-Uvswf7spOJ-_gMTGxJSOyJvowp2ZYQxx1ls1nwrImQiaXhTNjzh4BXKWVSRXIO3LBRPNUDQcxiAThYPJmYWHQS30lHrxL7O_ZfDSMRTVD72qJG1i-Qt8kjem7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDZijZMdKKE0w2s3piPTnel9QneNCwwhAPyAWiUU_igY7Nd8w1AIGarhF1vCOch2Zg_cPalkMaUzpXiCCmNYrllQTUrEsa4EwWoJDoadX-BcAxMa0bTDOP5WmTElrVKfIgMq67PUdgbej8t0MX1NfJ7BDziCQWRVjRMxC-AcvAPlYPHdMcjZ6cAXvK-peUiyARKa8_HNB9hmOLmZ2zUtqMFrwKjDDiyZVlHLa_3kqRZ4QqeEJDg_HiZCsbqycuJGzgPKPBJdXs4_sUPLvQrdHpj73ObdTqrZQGvPObNPgxJlXRI3M6gWq4LxAgoC58EBSY_lobC3oGgpXbqHYMHozg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدام مواد مخدر سریع‌تر اعتیاد ایجاد می‌کند؟
🔹
سرعت وابستگی به انواع مواد مخدر به عواملی مثل ژنتیک، سن، سلامت‌روان، دوز مصرف، روش مصرف و دفعات مصرف بستگی دارد.
🔹
اما از نظر علمی، بازهم مشخص است که برخی مواد افیونی با چندبار مصرف اعتیاد ایجاد می‌کند. در این اسلایدها ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/664784" target="_blank">📅 00:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664783">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d4be0c04.mp4?token=jj0MvcVV-aNfmkSI37bDxVoyUooxo-mQ2oXc5Ap3Xwvvh80snQq6Td6c1qeP8NfaO2HuWvukcYtA5JMaAp2NvZ7qUTaLKeiWSqfLIgmbwTSB_J2um1TkEor-T0k-qIJX-rI-1JUeP3BaEaSrHoOGEmGe7em4ECIyh8urnW29ekTpHoea7ZdjgXrY9gd_yZM5OOH03sQpL_9EyZr0sLzZYgPzcxrdIxN9lHiGqWpbV8hQt_3BJOpcVnKW60ZcI-eiYVjrM3y4ux_UjeEA5LVKHT6jAmkSIis6qDTdlrx6rSfJjgBiGSgSXu6MlIz-veCc-EFa4djQpXN3XeNO_2Io_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d4be0c04.mp4?token=jj0MvcVV-aNfmkSI37bDxVoyUooxo-mQ2oXc5Ap3Xwvvh80snQq6Td6c1qeP8NfaO2HuWvukcYtA5JMaAp2NvZ7qUTaLKeiWSqfLIgmbwTSB_J2um1TkEor-T0k-qIJX-rI-1JUeP3BaEaSrHoOGEmGe7em4ECIyh8urnW29ekTpHoea7ZdjgXrY9gd_yZM5OOH03sQpL_9EyZr0sLzZYgPzcxrdIxN9lHiGqWpbV8hQt_3BJOpcVnKW60ZcI-eiYVjrM3y4ux_UjeEA5LVKHT6jAmkSIis6qDTdlrx6rSfJjgBiGSgSXu6MlIz-veCc-EFa4djQpXN3XeNO_2Io_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من با مسکن پول زیادی درآوردم؛ دموکرات‌ها لایحه حمایت مسکن را دوست دارند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/664783" target="_blank">📅 00:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664782">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
حدادعادل: رهبر انقلاب در پیامی که خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا داشتند و با بیان علی‌الاصول، نظر دیگری داشتم، دست مذاکره‌کننده ایرانی را پر می‌کند، ایشان تجربه برجام را پیش چشم دارند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/664782" target="_blank">📅 00:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664781">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
فساد بزرگ در وزارت نفت عراق؛ ضبط میلیون‌ها دلار اموال از یک مقام ارشد
شورای عالی قضایی عراق اعلام کرد:
🔹
در نتیجه تحقیقات اولیه از متهم بازداشت‌شده (معاون وزیر نفت در امور توزیع)، مبالغی شامل ۱۱ میلیون دلار پول نقد، ۴ میلیارد دینار عراقی و چندین فقره ملک کشف و ضبط شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/664781" target="_blank">📅 00:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664780">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYJGobtNO2v3oGfrrwUWyszuvDI8CtjBr9nq_qZsZ__D2XKXEFcrymAa0Gu4HBIaFO3EKHjyPq82KWjQSdNmDnssPDAVuh2auQL9FbmkOLnyU0ODOH8dFOvgTP_Qk1-xANiNoSZGSNjif3IUiACK9VxUPw1MifDr8f9Q9RE-TKU_D8uDeGjDZLl1R4kq7mZuTwnd3lT2oBt8l1BVyfiKisCWzcHYvjzEca6N0LfGR8ly5pyz3O_gwM_7ZtB5NZ4uTeaXIHotq5dR493FuhEy_Nle0njta7Sg2-qIURbUzus9eFzCXaBmMcpfSLTJKnjLWFSX5XE7XVaODnqAsbNRhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار حسن‌زاده: تا حدود یک و نیم کیلومتر از مرکزیت مصلی ورود خودرو ممنوع است #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/664780" target="_blank">📅 00:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664779">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
معاون وزیر خارجه: ما ایمنی و امنیت کشتی‌های عبوری از مسیرهای موازی در تنگهٔ هرمز را تضمین نمی‌کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/664779" target="_blank">📅 00:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664778">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbr79gEzP1j8JbF9RwttCXAHIf284KBPMKKwM_NafUswxTe3iXt4rVeds_2qfSvOAno_aT_rPbL51xLvbNgY5IHgm5SDBGpcBJHr0FhnxAT7-St7AqTcv41tivGJvabP1Rapbnsk0PMdG3WS2qVZHSjvbntFGTfAutSZbjxiBTQDrlFrUJk_glX42VPwsLuURv1quc_r3TJXevt3sOF7c5B0zEO8DVeRYY3LNFZ56diPC-dZbzfI5s0ZEoj6kcHfYi-fFBjVkrJ-TQLUk3VqtcCYf-oWA_KjTLDBa9rqyviWecygMwGFjIZNuzePjfj719sHY6JL_v1RbQLojHUQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/664778" target="_blank">📅 00:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664777">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFKgJwe4uQhCG5KBd058H-bT9yqkpgjlwj230BR-Jb4EXV_m4Ng3jpuTsLVwOaQAkS_5nrn9OLDcI7YBpJYAUp5B61-gvFs7xnQSfMImd8cXc_GtteN-yUtv4Cvd1tqZUnu73O2Od_QHoBs6EdIxtKPoq3fMrPD7cY2URmimxjM7uBnRmN6lwnrtYok9G0jsam39UgucOBB70gyzDOBMpU6fQ4BxvayuYZ-qsUK6YkrMh5Lwkz2BNeZ3s9hLCfFwf_1bs8pK-EgCHDQG0OYDgqRRO8rANuFxRVhgjyWqd_Ba2kjpl7zFrFkhf7KVMpAyJIjOyAHx4TEGhLQagvwS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: اگر طرف آمریکایی به تفاهم‌نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/664777" target="_blank">📅 23:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664776">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
تشریح جزئیات برنامه‌های ارتش در مراسم بدرقه پیکر رهبر شهید انقلاب
سخنگوی ارتش:
🔹
ارتش با تاسیس ۴ زائرشهر در داخل و اطراف تهران به زائران و شرکت کنندگان در مراسم، خدمات اسکان، پذیرایی و بهداشتی درمانی ارایه می‌دهد.
🔹
یگان‌های بالگردی و گروه‌های امدادی هوانیروز ارتش در مسیرهای پرتردد، آماده ارائه خدمات به زائران هستند.
🔹
بیمارستان‌های شهری و سیار ارتش هم انواع خدمات درمانی را به نیازمندان ارائه خواهند داد.
🔹
با گسترش یگان‌های نیروی زمینی ارتش در مرزهای کشور، امنیت مرزهای زمینی تقویت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/664776" target="_blank">📅 23:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664775">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
غریب‌آبادی: راجع به پول‌های بلوکه شده فردا و پس فردا کارشناسان ما این مسئله را در دوحه پیگیری خواهند کرد
🔹
یادداشت تفاهم در برخی بخش‌ها دارد جلو می‌رود اما در خصوص لبنان شاهد نقض تعهدات هستیم. جنگ در لبنان  باید خاتمه پیدا کند و نیروهای صهیونیستی از این کشور خارج شوند.
🔹
کارگروهی را در ایران تشکیل دادیم که نظارت بر اجرای یادداشت تفاهم دارد و تمام نقض‌ها را مشاهده می‌کنیم.
🔹
اگر شرایط  لازم فراهم شود کارگروه‌ها مذاکرات را آغاز می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/664775" target="_blank">📅 23:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664774">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
روایت حداد عادل از نحوه زندگی فرزندان رهبر شهید انقلاب
🔹
فرزندان رهبر شهید انقلاب در هیچ کار اقتصادی دخالت نداشتند، در هیچ بانکی حساب نداشتند و در هیچ شرکتی سهم نداشتند و به ساده‌ترین وجه زندگی می‌کردند و شناخته نبودند و جلو دوربین نمی‌آمدند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/664774" target="_blank">📅 23:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664773">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dff1JCuaZ4gr2vza6Sx100_Jv90TKWb6fJ_LPRe17Kwtdtef5x4g5DriBIH-XF6UG10XkSELXwtaHWhXVXSh1owLuLaPnGcCyQqKpjs0cKXfjId7yKR8_39biSr6H7bDDUaAD-eWmk36OMHppv4s5RoyYW36P3OUmadFsGVmkhFX6wiLFDdaUTqbgUkpDcft8-oCgm01zNPqLtBYmmI2zPZVstkA0lJlkfa--kJbr5TKT0CKuKAKcEQGyopiCvT32h33N6cDhymx_vOsUpR4cUkPM4NEjVp5OuIFRYZ8uQryU-y5f92IjI8KixNwyprGJY4vEygtrvVaFr2kUMwBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام نوع پسته بیشترین روغن را دارد؟
🔸
پسته آنتپ ترکیه با ۵۴ تا ۶۰ درصد روغن، بیشترین میزان روغن را درمیان پسته‌های جهان را دارد.
🔸
پسته فندقی ایران نیز با اختلاف بسیار کمی از پسته آنتپ در رتبه دوم قرار می‌گیرد.
🔸
سه نوع از پسته‌های ایران از جمله فندقی، احمدآقایی و اکبری جزو چرب‌ترین پسته‌های جهان قرار دارند.
🔸
پسته کرمان ریشه‌ای ایرانی دارد، اما به دلیل اینکه تولید و صادرات جهانی آن در آمریکا انجام می‌شود، در بازار با نام آمریکا شناخته می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/664773" target="_blank">📅 23:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664772">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سردار حسن زاده: زائران، فرزندان خود را در مسیر حرکت و وداع با رهبر شهید نبرند چون به دلیل ازدحام جمعیت احتمال آسیب دیدن وجود دارد #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/664772" target="_blank">📅 23:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664771">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
جزئیاتی از نامه ترامپ به رهبر شهید درباره حمله نظامی به ایران
👇
khabarfoori.com/fa/tiny/news-3226668
🔹
درگذشت معاون سیاسی نیروی دریایی سپاه بر اثر سانحه
👇
khabarfoori.com/fa/tiny/news-3226700
🔹
شغل مداح مشهور چیست؟
👇
khabarfoori.com/fa/tiny/news-3226671
🔹
دو هفته اختلال، دو هفته بلاتکلیفی؛ بانک ها وعده می‌دهند، مردم هزینه می‌دهند
👇
khabarfoori.com/fa/tiny/news-3226665
🔹
ویتکاف و کوشنر راهی دوحه هستند، ایرانی‌ها هنوز نه!/ تنش بین ایران و آمریکا در چه سطحی است؟
👇
khabarfoori.com/fa/tiny/news-3226479
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/664771" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664769">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cdecd7bc.mp4?token=FBOMkRnpRTYX3LBPDeTqwMtSgBHDciochcoa4rvWb0OZXS-Fcp3iIhSQx8iy0ciUrDVpd0Jfc0ZslQl5n_8IjEEoPHgVbxD-3a4xHnGygjF7iTMB2XIRH7-Ps4YJTTTbIWPsRf_M65hoJBAXo7flglPYwEPCcZ0ofURegbV_UhmYBVryMcUAoGF6qjAAal_GZuDtmm5ekFYv0HOXm4BCLJ38A4SC6hkd4rwd-IPrDmoXzLHAkZoYw7OOzCouMjog912uyrrSUYQFeSNjGQVZQaWnmhPTbn3BjeZ4nJnmgoXkJ4od-GfFK6AQBn8Exaf_6VDggZFqiocugTTkyY_CsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cdecd7bc.mp4?token=FBOMkRnpRTYX3LBPDeTqwMtSgBHDciochcoa4rvWb0OZXS-Fcp3iIhSQx8iy0ciUrDVpd0Jfc0ZslQl5n_8IjEEoPHgVbxD-3a4xHnGygjF7iTMB2XIRH7-Ps4YJTTTbIWPsRf_M65hoJBAXo7flglPYwEPCcZ0ofURegbV_UhmYBVryMcUAoGF6qjAAal_GZuDtmm5ekFYv0HOXm4BCLJ38A4SC6hkd4rwd-IPrDmoXzLHAkZoYw7OOzCouMjog912uyrrSUYQFeSNjGQVZQaWnmhPTbn3BjeZ4nJnmgoXkJ4od-GfFK6AQBn8Exaf_6VDggZFqiocugTTkyY_CsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدگاه رهبر شهید انقلاب در خصوص واردات از آمریکا چه بود؟
رهبر شهید انقلاب پس از توافق برجام:
🔹
از وارد کردن هرگونه مواد مصرفی از آمریکا جدا پرهیز شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/664769" target="_blank">📅 23:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
روایت حداد عادل از نحوه زندگی فرزندان رهبر شهید انقلاب
🔹
فرزندان رهبر شهید انقلاب در هیچ کار اقتصادی دخالت نداشتند، در هیچ بانکی حساب نداشتند و در هیچ شرکتی سهم نداشتند و به ساده‌ترین وجه زندگی می‌کردند و شناخته نبودند و جلو دوربین نمی‌آمدند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/664768" target="_blank">📅 23:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_a4qtW-tfv75IdD9L7h7p0XfjH5hsB-3-tlcH67Wl9zIPFgYlMUizHtb7QFDsv2rh4oJoJgr4JyR_zaRhqY7XEDqQ9cQ2xAXKA-NvE7dK6ObpMyIkrVK-NM3kefcYKb9HgXzHlWBZx7QQuWsnmFHjz3nr1wUMIvd0hFaNALWUzpu9YE5cbhnei6rf8miRfSa6hgMwTHfXiUKAB_CE2MV77_wmGBv_36ehslwcEYKv3Rtv5MMhT_VrVA54tJ6ctuDxHFG1UI85gN5w3wb-PQN0XUt0jySduXsuunQlt5Lpj-67zmfUcRqqGYfiU0c_7c-9m-KlBidP5KjT9dV5uzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولتاژ بحران
🔹
با آغاز تابستان، بحران کمبود برق بار دیگر به یکی از چالش‌های اصلی کشور تبدیل شده است. این در حالی است که وزارت نیرو پیش‌تر وعده داده بود با برنامه‌ریزی‌های انجام‌شده، خاموشی‌ها به حداقل برسد. اما با وجود معتدل‌تر بودن دمای هوا نسبت به سال‌های گذشته، بسیاری از شهرها بار دیگر قطعی برق را تجربه می‌کنند. هم‌زمان، وضعیت منابع آبی نیز نگران‌کننده است و نگرانی‌ها درباره تأمین آب در ماه‌های پیش‌رو افزایش یافته است.
🔹
تداوم این شرایط، انتقادها از عملکرد وزارت نیرو را تشدید کرده و برخی نمایندگان مجلس از احتمال استیضاح وزیر نیرو در صورت ادامه این روند خبر داده‌اند.
🔹
هفتصدوهشتادوششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/664767" target="_blank">📅 23:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85b1a0a04.mp4?token=VnKJeHv3NC2_IeQWUM5-UGVfu4YeKx26sySp91UzrdaeTmgQ9NUqCgDZSz1la9lT285cP7maJNyzEd_nZoyvKFq2R__fFPkwYBficzSkyH0LJ7L6nQFDdUKkhXGvO5YnxLO0TF7Di6qPPnd7X-yTvrQhrbcPC-LyhAsW-1TxrR6G4fpGvHiO_t_l_-rRDOtUHROg6MCG66AYfH_Gch6Z6RQ5MbrEcfy2-6HvWo39Ods_WsXNxi-jpGTRFmr_E7S3jUO09NFHXOz9rmOyf9W_ob5xlIwxqqCFI9j1m4mElE5PUrN_GLPpt62xxPYeGpbiSw12PCUn7gDEa1O2h5idBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85b1a0a04.mp4?token=VnKJeHv3NC2_IeQWUM5-UGVfu4YeKx26sySp91UzrdaeTmgQ9NUqCgDZSz1la9lT285cP7maJNyzEd_nZoyvKFq2R__fFPkwYBficzSkyH0LJ7L6nQFDdUKkhXGvO5YnxLO0TF7Di6qPPnd7X-yTvrQhrbcPC-LyhAsW-1TxrR6G4fpGvHiO_t_l_-rRDOtUHROg6MCG66AYfH_Gch6Z6RQ5MbrEcfy2-6HvWo39Ods_WsXNxi-jpGTRFmr_E7S3jUO09NFHXOz9rmOyf9W_ob5xlIwxqqCFI9j1m4mElE5PUrN_GLPpt62xxPYeGpbiSw12PCUn7gDEa1O2h5idBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرکت بزرگ و مشهور انیمیشن سازی پیکسار که در آمریکا قرار دارد ، دیروز یک انیمیشن از خلاصه بازی تیم های ملی فوتبال ایران و مصر در جام جهانی فوتبال ۲۰۲۶ ساخته که در آن خوشحالی گل رد شده شجاع خلیل زاده بازیکن تیم ایران نشان داده شده است
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/664766" target="_blank">📅 23:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e3d25120.mp4?token=P_1Y2Lp30kLqUnEea3thV-ydjKTHLjOBCcaiQVtdbDA2CNUW2Wk4wlSugS67ewQSDh7euMzXKIoVJfPHNfrJZ732KI1e3dtJO4tV5yVHb29gdEUEyrc_Rqbnidw3_k_WRkAkPqizt5HdQhgq9eOgehmmLD2s4_SeyC_FsACWfEuy8aBTVl5ad3DnAZ_R5yFRoFOpQCP0y4habsgOpCoNj5o_ftfUUigj2ly78Dc2QwQp9S0Z6TZL4AkiMewJqFPAkBzb2rgR5ohDUqyx85SFkBSZHK7cTTsA-3VwspWRIJP2EduOVRVgiW_gOU6L14uF2oAnqSCq847Z8NMnJtofQ2NTOH_vwup9ZfNR0HJl-qSvtYZEUd6V8F-icqt7NQQdtLyFXuc56KONxm1LWb0lEp99NF7lL7g5LDi1iFJVxd08n6Ze8R20FnVa12PSRAJQIW5FAUQBQnm0Wp7u9aQPjqfdTpEdQkyOB-mD_OsmOSyMDbiUpcRTWiUSADyoe1d260N__5mrNCqmlpXq2BuhxZRAaAj9VJG0JT8-BJ4o1Z2p8rXKRZKZvJ1t6BtV3i7yWqHQFNktI03rQ6N5AbJZ9T77_yaeMzV-gZS5ipd4HOyuSZTWKZgnOg8CUf61I35qmA-NjXTQpbTWgw6eLEtokx9KXKKIugLfbxth8-qiIaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e3d25120.mp4?token=P_1Y2Lp30kLqUnEea3thV-ydjKTHLjOBCcaiQVtdbDA2CNUW2Wk4wlSugS67ewQSDh7euMzXKIoVJfPHNfrJZ732KI1e3dtJO4tV5yVHb29gdEUEyrc_Rqbnidw3_k_WRkAkPqizt5HdQhgq9eOgehmmLD2s4_SeyC_FsACWfEuy8aBTVl5ad3DnAZ_R5yFRoFOpQCP0y4habsgOpCoNj5o_ftfUUigj2ly78Dc2QwQp9S0Z6TZL4AkiMewJqFPAkBzb2rgR5ohDUqyx85SFkBSZHK7cTTsA-3VwspWRIJP2EduOVRVgiW_gOU6L14uF2oAnqSCq847Z8NMnJtofQ2NTOH_vwup9ZfNR0HJl-qSvtYZEUd6V8F-icqt7NQQdtLyFXuc56KONxm1LWb0lEp99NF7lL7g5LDi1iFJVxd08n6Ze8R20FnVa12PSRAJQIW5FAUQBQnm0Wp7u9aQPjqfdTpEdQkyOB-mD_OsmOSyMDbiUpcRTWiUSADyoe1d260N__5mrNCqmlpXq2BuhxZRAaAj9VJG0JT8-BJ4o1Z2p8rXKRZKZvJ1t6BtV3i7yWqHQFNktI03rQ6N5AbJZ9T77_yaeMzV-gZS5ipd4HOyuSZTWKZgnOg8CUf61I35qmA-NjXTQpbTWgw6eLEtokx9KXKKIugLfbxth8-qiIaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ر
وایت حداد عادل از نحوه زندگی فرزندان رهبر شهید انقلاب
🔹
فرزندان رهبر شهید انقلاب در هیچ کار اقتصادی دخالت نداشتند، در هیچ بانکی حساب نداشتند و در هیچ شرکتی سهم نداشتند و به ساده‌ترین وجه زندگی می‌کردند و شناخته نبودند و جلو دوربین نمی‌آمدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/664765" target="_blank">📅 23:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664757">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z05Jig37ucz4jojwBFKYRAMPHRdZeb4ixVrEHTFfVL2f2TNZQqSQfjZR93LEJ_7koHML-ZTK9SSicBkSPGqiPOqyfPFCq5zwnFFhGvddnypI09l7CT-Su2piLU8u8Q41PULRQPBaayInXWwKYPcl00LPWR3-NnCWFgBoGsgcM2CzmTqS4svIFia3vZBGR2ooHU_VCi6JaolVsPYMkeAnV1Kd9rCvMMqX6pQ6BPSsQG7MhxC7RCuls-L-iAXyZiQPy3VHKx-yfUbOPAc8-MVcFZ6MqnZWj85eblJlH8ZHl9sIu2_EoUvveLVmE2o_Koz-4ryDAsEQo6jAMFODhuf3cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taHCMtW6XXP7wr9vGnSdxWHvLXaak5MorJ91RLNv0UQgdO-_geCmIc7gscGJqq1VIkRO8746yachFX1OU4VUVD-XbBPwdCG7pOCA3cjyQiMPsf_e-xc4RtHhDU1dJOq1TdOel_b3tqEjKaURZr55pMt9Jm24IGG4xT6xLNkRs2sIP9X2gD9dBMTIAR7E_q4eg-MolwWvLt0ghPOt1-xKVlX0HFBObBomxsB6OEifY3DxdzlfFOG8uVMr4WbiT7BjjGpN2Xfl1OxTUVR1IzbpGkVHoALvNbCdWPFHAFPN-yrSeb48CvTgrU1BX-ACA-JCs8O9IzmusyTpaeHU1neRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuQbrj3E-i1mX-In1tugFyT8DJGIX36VAxJrorVbcQ87I_Vh01_k16zh539luhBDzfxuSwU7ThVHbVlrwY439-zVoDidA4OgRTEjDwV7pjq-WSVbVJHZj8Kn0GI6KwdDAYiIR-3obV7mP9dvfWdmCucfSjQzbYTdlGXRQOivxAL1Joq-yTN6T-lrDrCzEYb05WfscLwc3SuV7itBmqfaD-8IkiCV8ThuZmzO_NSYHQh4jKbrBJhMPcEg6u9FsTBnFTHnK6K3v4NPCf2ez_z3ZFvfdPSUDPCpitKVAJo3GfIOCWvcYl1cXOalTMjcBD42pGL6wxmFeirh_1JFUEVJ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9486bb21c0.mp4?token=j6dQNjvARBrInnvWZvvcGaNKWrSE1HAuTvVN9ORSXtb_IwhWMgHB4P6jrjDp0FXpmiWLMS0eE35Jc80ba831dSTCr6Ljk2yyD9tnAfOhTU0-wYFqdd0c2TPuOT10YGhoAxnAYuyK3Kjx_VT8t1PA0AQoyXhX14YkahMmTw1FjGXH1-WNDt2brV1MUKfhKq3kmdnC3cQ7E-tUop27L6P8gGUuEb2vd9tJWlRhrDrv9NjukguXYrqeNE2Ulo4EcOvXLD1vySncv7D-ci1Js5gilfGIWS6UFmCgV_w_1AViMUYOSHB7d1vR-N6yvaaJtsKDXJtZZQdYk0wVEKnkBs00LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9486bb21c0.mp4?token=j6dQNjvARBrInnvWZvvcGaNKWrSE1HAuTvVN9ORSXtb_IwhWMgHB4P6jrjDp0FXpmiWLMS0eE35Jc80ba831dSTCr6Ljk2yyD9tnAfOhTU0-wYFqdd0c2TPuOT10YGhoAxnAYuyK3Kjx_VT8t1PA0AQoyXhX14YkahMmTw1FjGXH1-WNDt2brV1MUKfhKq3kmdnC3cQ7E-tUop27L6P8gGUuEb2vd9tJWlRhrDrv9NjukguXYrqeNE2Ulo4EcOvXLD1vySncv7D-ci1Js5gilfGIWS6UFmCgV_w_1AViMUYOSHB7d1vR-N6yvaaJtsKDXJtZZQdYk0wVEKnkBs00LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروهای امنیتی عراق همچنان به منازل نمایندگان عراقی میریزند و حجم زیادی پول از خونه ها درآرودن
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/664757" target="_blank">📅 23:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664756">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHpJ1sQGSitmrVFbO1q3993Z6isEji77ZpNIeN0-lSJxKh87kek39dKhL7dFNz0wxvHV-BPKVixRhQCtViRK0XTARO_zxbxFJT6AgC8mfnTj0PW-OiSdsLR3vNDlDo4LDH1qRNgyyTiAy7MNvD8CTDdszPFm8AsRK501BTQYUbozuL9XxQoaaRux_WQMKgCb4PCReJiir5I-wyXsplfOlnjkAhXXOqcc1gevnqB2-xl9afrRLRTAlz3kZcRQMGOMBqPHYIAUHD6HkV3Nx9co6KvWh-Zfhy07GgVHshBSYBhsEMbUJg_YIjOEJfR-ZgZIqIXRcjnyFOmgTP3uO8Us1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پوشش_بیمه_ای_زائران
و شرکت‌کنندگان در مراسم تشییع رهبر شهید
صنعت بیمه کشور در راستای ایفای مسئولیت اجتماعی و تامین آرامش خاطر مردم، تمامی شرکت‌کنندگان در مراسم وداع، تشییع و تدفین قائد عظیم‌الشأن انقلاب را تحت پوشش کامل بیمه‌ای قرار می‌دهد.
به گفته
#موسی_رضایی
رئیس کل بیمه مرکزی، کنسرسیومی متشکل از ۷ شرکت بزرگ بیمه‌ای (ایران، آسیا، البرز، دانا، سامان، نوین و آرمان) تشکیل شده است تا پوشش‌های بیمه‌ای لازم را در چارچوب قوانین و مقررات مربوطه عرضه کنند.
#بیمه_مرکزی_جمهوری_اسلامی_ایران</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/664756" target="_blank">📅 23:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664754">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk36JGyUWu0-JuHroOsSmQ9ZzJA0-t4Ul_upxrSahIZMj7B7PRFQ3l95GL9r30LNJNZ9owEfo5Zr7N2IPQOmjTPMJKIhv8lYJPl6szqY8pZ5pE1jSOB9CA-fy2kadYG7s_NVNtBL9CDf4vzWtLMjPENtZRsm06anPskPHZNefR3Jyu--it05Cbyq3LG9kRXXRVHSDK9WzaosfaWLvU_STl5hGgEPIendZ7dis92MMgM9NFoNA6ErzKnoq6RTmr11zm-6jgxs2_dmA6pkvP13-_39V2pY0mmJ_SbAi32KLHqKl1oL-Dn6zUVY0F2navYQcCdXYnazcwZOScVgdMTNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جای نیش هر حشره بر روی پوست به چه شکلی ظاهر می‌شود؟
🦟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/664754" target="_blank">📅 23:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664753">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EICh9_ixIls5u6vC5stgkgXgf-nD-aPYyr-xsPdk4q4wmMUgFOynaWJBJMWSdyHC-IlhPegIdxNjay-aLa6G-EtGhXkIB_mXLJGOQHaEzLynbaCy1t9WGH-N40wnpERC_ER_aQGSumZEZazcT6vp6xwUCFqtKboDE58dLwxlGlvitLceP1XUWR5ZxPLV-3rCxTdNigeVPTpCR1zZWCVhdU05UBKs5uB5_aJQ6efNgUAR_gIFBt8IyTdZ3J4N8EaD0pRsSW02bSaermD8f6dVau2Vmv8uB4DEqSyjspJ2Zbc9niia4y7iBGdW-ub8Tiej4lCW_0hHGMsEvI5oSJcG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد رسانه ورزشی USA TODAY Sports از نحوه میزبانی آمریکا
🔹
فیفا با اجازه دادن به رفتار شرم‌آور با تیم ملی فوتبال ایران، سابقه وحشتناکی را رقم زد. اکنون میزبان‌های آینده می‌توانند همین کار را با هر تیمی، از جمله تیم ملی فوتبال آمریکا، انجام دهند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664753" target="_blank">📅 23:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664752">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H93PwDth3_7Yi-3MkVB06fb5hC7sRwhlEbNYp8xPJqgBqJwyDCtkBWuNxEBmmgubXfrDW1XUirsiQKTkD2kkBGcYfXvkyEX3dsX_OGrmBBYmb8Mo7x-wKu7AVJ2JtIGw3AT7r43KQSybz0vDsmgRoWdl2NboA_zwhbLFfKTqOvHHmRaACWoisdKe9bKt6VkRdsebUSW9z5OE1K7EZ9qZzS_O3DW03WgmKvoWMOK9lHd-jQa2jKBCj1P5dZGoXCnaSWn8ZW05FG1RWg7b4md5jjnxkFJYKYY4D4snirFjItzKNYj2S-dYNTstCpwiblXd7TgQrjDi-qSXyYw-2SjvZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهره جدید آرمین زارعی ملقب به آرمین 2AFM که در فضای مجازی بحث برانگیز شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/664752" target="_blank">📅 23:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664751">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
خبرنگار آمریکایی: ایران و آمریکا در قطر با واسطه‌ها مذاکره می‎کنند، نه با یکدیگر
خبرنگار نیوزنیشن در ایکس نوشت:
🔹
یک دیپلمات آگاه از مذاکرات به من می‌گوید که فردا سه‌شنبه، استیو ویتکاف و جرد کوشنر، در دوحه با نخست‌وزیر قطر و دیگر مقامات دیدار خواهند کرد تا در مورد مذاکرات با ایران گفت‌وگو کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/664751" target="_blank">📅 23:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664750">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d42e15cf.mp4?token=v8klMh0nG_-SSiIAvIZz2ya-2-E8yMZfswEjaWTk9N0Ay6V8LSmtw2-gxBpZgsz3B3d77XliFurFYOnJ8JbF4K3dYvhIX5O3olIogkBeUaRJgHzHJ0BZSSl1HaxsNjGQcd9B4NsFtDFTugg8pQS7Zwq776Dw8qjC18lLXTcNxJUnaoFzEkvntQerABbjKQMCWkwOmAxJXyolOwUFaMk2eZNciYsd84188pIsf1vhEwmPkFFC-1VSV5dwQ-uhR5CtWZLprO76BHmbu9Nody8T65p0goDkMZKVzDK9F89FzsgStZ-QKAdKhAcxxJIX_80EtnTCf1v9VFxWZjz7bIjrTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d42e15cf.mp4?token=v8klMh0nG_-SSiIAvIZz2ya-2-E8yMZfswEjaWTk9N0Ay6V8LSmtw2-gxBpZgsz3B3d77XliFurFYOnJ8JbF4K3dYvhIX5O3olIogkBeUaRJgHzHJ0BZSSl1HaxsNjGQcd9B4NsFtDFTugg8pQS7Zwq776Dw8qjC18lLXTcNxJUnaoFzEkvntQerABbjKQMCWkwOmAxJXyolOwUFaMk2eZNciYsd84188pIsf1vhEwmPkFFC-1VSV5dwQ-uhR5CtWZLprO76BHmbu9Nody8T65p0goDkMZKVzDK9F89FzsgStZ-QKAdKhAcxxJIX_80EtnTCf1v9VFxWZjz7bIjrTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ارز صادرکننده‌ها به کشور برنمی‌گردد؟
/ مدار
این گفت‌وگو را در آپارات ببینید
👇
https://www.aparat.com/v/jmrz2dg
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/664750" target="_blank">📅 23:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664749">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c9d96687.mp4?token=u4CfzENRlZUydwqL5KR57ROhoc4RZzFfvl_T3D4g5rnKQlkfJkSafH1dHDeNOvNh-4WjdyBszKktKK4Pmm62telPHInU5ewAOqs89YtwHJ_Z-UlHX22r-6x70Azj80UEf1BHsxRF7Mhjv-qCGFlVE-Ed2yvu2D_G1r2DpMEnXjsNm48FifvRHKJU19RfjyX2JS7B1RI-NnZVaxi-xlCdawgNSJja2n4XAvpw2NlAK-0tOY7A94gc28h-WUwo3MfLpXOaCMKeKjvqsWqrOHfI6O4YpL-DmYhZxG17prfmCNjoqi4-ETFmB2x40NiekCwu-OG9hZST2df4vqgqf2TqIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c9d96687.mp4?token=u4CfzENRlZUydwqL5KR57ROhoc4RZzFfvl_T3D4g5rnKQlkfJkSafH1dHDeNOvNh-4WjdyBszKktKK4Pmm62telPHInU5ewAOqs89YtwHJ_Z-UlHX22r-6x70Azj80UEf1BHsxRF7Mhjv-qCGFlVE-Ed2yvu2D_G1r2DpMEnXjsNm48FifvRHKJU19RfjyX2JS7B1RI-NnZVaxi-xlCdawgNSJja2n4XAvpw2NlAK-0tOY7A94gc28h-WUwo3MfLpXOaCMKeKjvqsWqrOHfI6O4YpL-DmYhZxG17prfmCNjoqi4-ETFmB2x40NiekCwu-OG9hZST2df4vqgqf2TqIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من با مسکن پول زیادی درآوردم؛ دموکرات‌ها لایحه حمایت مسکن را دوست دارند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/664749" target="_blank">📅 23:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664747">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای کارشناس انرژی: نزدیک به ۴ هزار مگاوات نیروگاه برق، از مدار خارج شده است!
محسن میرافضلی، کارشناس انرژی در
#گفتگو
با خبرفوری:
🔹
۴۰ درصد برق کشور در تابستان توسط کولرها مصرف می‌شود که حدود ۶ تا ۷ میلیون کولرگازی در کشور وجود دارد که بسیاری از آن‌ها غیراستاندارد هستند.
🔹
نیروگاه‌های فجر، مبین و دماوند که مجموعاً نزدیک ۴ هزار مگاوات برق تولید می‌کردند از مدار خارج شده‌اند و این کاهش تولید شدید یکی از عوامل اصلی قطعی‌های برق است.
🔹
به دلیل خروج نیروگاه‌های کلیدی از مدار، بخشی از برق مورد نیاز صنایع از طریق شبکه خانگی و شهری تأمین می‌شود که خود فشار مضاعفی بر شبکه وارد کرده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/664747" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664746">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e6a460ac.mp4?token=f6bPGHWnauTE_Hy0tbH31qmkS83eXoIHQlOwUusrGqzCBqzqzgR4-_hkxq_T-r1fdcyH3PTAtaS1yX88WmrApF8_KEdm0A1Qoty-xYtUfWz_vCyqnbtrvI_UySl0KZDhY_KNqogSRBk-tvklJAvM9FlkhmDuUSPUsvcnOKvBT0fvNnCn4TlIAjKlHjwxq8Yphdf_jUjtszlyjjfIv98ud58qTz4sovdHHJtvjHsnPxt6K7PZlpxpk_jzUeXCLgGaIqbZn7n8Q-EK-K9WxmypVocatl5CNTFd53NcjaDdnS-lUwf7UcO23jU6lXAfWgdOS9sZ-M5sM938doWyqy-oTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e6a460ac.mp4?token=f6bPGHWnauTE_Hy0tbH31qmkS83eXoIHQlOwUusrGqzCBqzqzgR4-_hkxq_T-r1fdcyH3PTAtaS1yX88WmrApF8_KEdm0A1Qoty-xYtUfWz_vCyqnbtrvI_UySl0KZDhY_KNqogSRBk-tvklJAvM9FlkhmDuUSPUsvcnOKvBT0fvNnCn4TlIAjKlHjwxq8Yphdf_jUjtszlyjjfIv98ud58qTz4sovdHHJtvjHsnPxt6K7PZlpxpk_jzUeXCLgGaIqbZn7n8Q-EK-K9WxmypVocatl5CNTFd53NcjaDdnS-lUwf7UcO23jU6lXAfWgdOS9sZ-M5sM938doWyqy-oTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ متوهم: ما تا حد زیادی با عقل سلیم حکومت می‌کنیم
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/664746" target="_blank">📅 23:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4430f5d6.mp4?token=d-rYdy6nov3SPq4fxi-k8kgZZFmpO9yX5BtV1TFOGhDX0apAAKd02tSA41fh2a8Qu6CIXdcCeB3ColvS08KnBXe5ala59M_LB6_3TTKxIQw0L-lZCl_y_HWu2EdUG9bdeTvl0jeyEbWl0_yU7SGKI0RqwIvtLixWVv84IPjlH7sMAAg_KUE0dbq62cf5_HC8SK_dDmkXiTh27U_vaxveG61gFWJLMhcSs0Coe8g4z9lg5Y-pp1emsl0ghf3JowFnMVOdMZoPYkOfkllQbNEEBWEiWN9ccyf7nIcpzfDU4dDLmkyTTyYqb2oEZkbniiO_xc1fzXQM389MLlP5vV1KTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4430f5d6.mp4?token=d-rYdy6nov3SPq4fxi-k8kgZZFmpO9yX5BtV1TFOGhDX0apAAKd02tSA41fh2a8Qu6CIXdcCeB3ColvS08KnBXe5ala59M_LB6_3TTKxIQw0L-lZCl_y_HWu2EdUG9bdeTvl0jeyEbWl0_yU7SGKI0RqwIvtLixWVv84IPjlH7sMAAg_KUE0dbq62cf5_HC8SK_dDmkXiTh27U_vaxveG61gFWJLMhcSs0Coe8g4z9lg5Y-pp1emsl0ghf3JowFnMVOdMZoPYkOfkllQbNEEBWEiWN9ccyf7nIcpzfDU4dDLmkyTTyYqb2oEZkbniiO_xc1fzXQM389MLlP5vV1KTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناراحتی ترامپ از حکم دیوان عالی
دونالد ترامپ:
🔹
حکم رأی‌گیری پستی کمی تعجب‌آور بود. این به مردم زمان بیشتری می‌دهد تا به‌طور غیرقانونی رأی بدهند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/664744" target="_blank">📅 23:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664734">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf7UF19uqj0UWOTHpWtM9p8fEY8V_0vo5kQrFBEzSkENbYK0myCNWpwkdUwcWbNHm49qtonex7NZV5rru2t_PMk96NxL8D8ucAKXaxiwkpBCy7_JRKqdcvfx6tNCt80VQRsR9s4tCA_SAv8Bu4o4S6ipqtZl8zlPO5W8hBgCZ3-aF0XlWPmFypBae75qX6Ilta55xvtdt3cY53aU6tsPw2jWm25bsiaDs479ln9tiIkfuzaXQeVwYzx1DPCdwHLbFH2O8O-2_14mft42rUtRL_irsEEqS6uspfXkUzTF-saUkGIMJ5vJ-LKOqH8mi40JdZ4jG2CB3yqy3M_ZPPc_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gG6wWUig92SzDedKyU-4CJqvGIAhyft_61SyPKo-cxJK9JHbDtHyaB-aPSzLfnvWBAyj5lJktjT2Mc5iOZ4qth78X-naokWuK7LIVQUlNT8-kIxfgGE8ucx77ScfupAn80zz0Trfr39S_VaK7wSLkzMJRcVgZXG7K858qviL9oHEHarpCpXFBoSGt18gS3SawaizBFIJi7EBzZ1M43JL_V89fyJjEQf9GsrHi9DEwapyWsAut-a-m1-r4xTBGE5i9yxcU2uqXp0sYV7ln-PFkbuOchPhTMuZYg_WJVtdkWZEmIRygz6oM1BRXoKNpoFfWNw_-3zqehPxsH_OyW1QoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JedtTP2nHmV6enyleidWZQl1HlOts944ePHddhAwl3VxhDra-uDcBtLjSbhm7RCNChuqfz0nq34ZXOMfj6a1wAR7EDDD8YPqSecR5d2D1i-SNhYW5rP4YtBrUIKW74cG35VLPzh8usSNW0zDNgL2qIrj6fs3LrEiKMPNxsyFY7mKGbxGNSXbRczs2WHpaRgjFMeYemL4SVgL6p7x0TlIlC6rwwXttfrn4RyBQwXaVcdwt2RaywkFL9iAtyPpNqbCPdy7OIyt1aFEXg90dA92GzhepAiIuSuSshoThDoAtqxv7DzQgMwBi4XVBMoQkf0YIL8e7SXw9qFXVM9e4U78Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRKPy9NnnWjM9nlONSps7jIams4D8loiBT8lhp-M9kFRiwQZis821kt0eOF8N0ip2wfRuc5xgZkPYzbKNxGzfC1WQWUoEFVrv3F6wy547Z8II3mU6QL-fj0vDWF9KzSUzIFKs3m-HnfYsrIo8K7nEIjoNzYRPuDtNiGRR2KQINRC7BNl_xbqki-k5DFonmeb8ITpFhDt9rpANkWAHGDt-pzNMVlKvwHbQ_7rLUQJ4FCCnmRp-TMydv5JoWYr8nkztz1HfMW4-0clDllvJicnoUKJOxuFpKIDefdsPssXvzWTKtozaQwLlTWonLhwjWfxJhUTcTts6nZYSHxrig1OJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXrfxo7rXeQVqd_I_N7b6s1KgFTuH2lfth9_tJNbKSiSsTotNSa4hQu0lxALC1CtrZb_l6K8gJzfdy9CosyQ7qnWRvQ3JAog1tLNwlx9fkLNJ4_nMh7TJ73df7DVS7sfHM-hgyAtel94RR3ZumfJSzA71ZjUyZDMI_9BGq8vn36k1rLbzps6Hf_ApzLB3vRdcnHvtDY32tjj7YMpX_7Tr-DUfEeuS4FgpeC1OgluHGM7tQdMhJL6LdiDzkbT8f-lmSFs6t4jiGN_cGsVEFnwZxIyCghXtCqgMEdfEU2eJ7vnBNkwdJl60KZscUy0aGzmNSqouXD8eO8qHpLvoY6swQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNnu5hT46GetxDWrnaNo8MbzP9tdPdqjolJwad_ikVkt3tHmzla8_vCiN3OYJm3fT6MIs9Nyfms6ydvVZhil9eXQjOrHst2dxWb3VLu-zzHjfVQi-xr7UI-2VRJ-Budbhniv9lM60EGhG93tppnAFCBWFAufZx4bAJriJBd0LYIMJu81ZtWlkTgfecUf98P_XnOJbCb3-n0CMijhsitXb5O8BQWMcP-HABg5hPLyPwStM3cdTE3qRUkyS-kej1OUuL7pwZFnjy50o8c66zYP8Ofk5eeF59bvn19tlaJCxk7pLja6npSzFokqhMdjS0v2yVRpnbDU2PSMDa52KBIA7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ebX1TFKJUrqYaqmNP-8VyNeefNYTur05FGX-Gm2xLbODAqBb3kAoezNpcLQ2fnYh8VgLL68X7hlJra_MjV4qjCyHZvSEFXcR4KwNUlvgT5VzvBn6W_xAjikDc1UVgvaAGeyJkmlGLoSMmj5gynyV9GFgY01WL6vgaKEbvNY7HYb6gX5v711MdQmmelmX1RvY0VX4q_Uvck0q14FBuvh6Kn8QepQh90cemWrZ3sc0jK7dx7ebZ2KFLRS-wDP_CB0bhmL3n5So9ymp9TZOFBGb0FU-Rqk5yb3PlA-EJsES1ycL7377g_yhfrAwY7b2twknPvKDfPUaNEQRI2erZMSAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EG02L5JH4WCztBAeSk2nwjVrsvFCg_mWXM5ZIalwkLdqH2c-uNxZqLTGITh87UKDqiXVtdTg9l0ZLX8cSp7EOZgTaiPSs1oDkCU-2tMmgBjxErmrTxwIf0ghcLgis0T8CCQpPPZ0oxNiBxYIx4L74CBsNBthw_ws6TZz4CD-G5RP6sJfPDWBbVxl3qnw6ZqDXxH4Xa6zl9WKM9rRmpHZM5l4mEs0odofYFfqfIec6Yu9d7uroNJo6Iic91rq4njF0GTJDyNCy3zY9gSz13Eh_9cqFjuzivhGecelFvJ7JQbJHLnyoXvdxOx3TxH8gYFADlVnnF0-NX5kUkVYAAXorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOTqCPkMi7zoKJzpO0O-vfXuxU5i-lstJ2jD6-HEvtNIetVrOM_LHYzaO-JTDRYf1aKPhLQEckFI09UhqCjAqW4MmVCT4WQIP68CHZz9QGqk3hsw3F5yjy3CypDMl3VGeoDvOb7QP975AWRNGcWL-f-KhAIOm7y4ugQJD1yzJBKJQs89hdtjbs0HxGyZpnZzjd2_I3BIs27-3X0M22suPvvdN2vDffmXkD6xe0a4U2snzT7BkyByJ_KOasIFmsOtkeKJVpazZ9CvbvlUUfaFZhlg0f2rWAZ62iJV7Nzs8YDLXKDZs6luwpZ-waL-TLVjt4Fhua3kJYAwxGwyp0wERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxZrhGio-NKJGbFL0R4MhWIKkBrfnkHDUKE638K2RSvdzwMbfETEq6yQSlgJY7ul-_SyQVx2a3ViVJQi3LiMIMm_repj5oh-wK62etZEYEZpL7T23OqxPwcqvQVr5ozKFSkM_VI2A8mMaSqN6q1yslLM08qg9bLfahan64s7vxPBq1mRotpiw4OR-4N7XoZidLEr5LDFR0lA5o_MponXITqJRivZ9iKVQYhR8LQhmx2jmeH_J9g2WlYXwJQOElsNvXf1EzAtSjTUExiyOH1aV9b7580blOIhykJG6au3GDXqX36lnjcvx7yopTlMQONgsuxoE5qn9ZOQpasLT65CNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منتخبی از پیام‌های ارسالی مخاطبان خبرفوری درباره اختلال اخیر در بانک‌های کشور
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/664734" target="_blank">📅 23:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664733">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سالیوان، مشاور سابق امنیت ملی آمریکا: طبق یادداشت تفاهم، ایران بعد از ۶۰ روز می‌تواند از کشتی‌ها در تنگه هرمز هزینه دریافت کند
🔹
طبق یادداشت تفاهم کاملاً واضح است که ایران تا ۶۰ روز نمی‌تواند حق عبور یا عوارض دریافت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/664733" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664732">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8934d1061.mp4?token=bOhm3e7P_OYsoRIY3yL2nsh-YNPP8B2MoqsnJDBT8C0FqPs1JHGrrwjUmyDQtHfQeK9867QThKUxzPd3A44h0iH-pE2Ep7PAacB2qsyY2xVDuPF9zbiOaT1lCE5a4NHBgp0XiqJ8HmgxVkV54z6I8Z2CodFHtGMJR2LNhbYgwUCvgLwWpnOS9DTfIgAYyPtKvDauulsYKyHFSyHUTPdma3katGJnzcROQWKYQHnOVygA5pIFItjsgOL87O9UHTf_7vZLB479L6InmFGWNTfoyF9bj5t6uSJofS32wIxmJL7B1Yk-W408KaUmaxcOVSpSz7-0mJUh7DP269_sccoRQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8934d1061.mp4?token=bOhm3e7P_OYsoRIY3yL2nsh-YNPP8B2MoqsnJDBT8C0FqPs1JHGrrwjUmyDQtHfQeK9867QThKUxzPd3A44h0iH-pE2Ep7PAacB2qsyY2xVDuPF9zbiOaT1lCE5a4NHBgp0XiqJ8HmgxVkV54z6I8Z2CodFHtGMJR2LNhbYgwUCvgLwWpnOS9DTfIgAYyPtKvDauulsYKyHFSyHUTPdma3katGJnzcROQWKYQHnOVygA5pIFItjsgOL87O9UHTf_7vZLB479L6InmFGWNTfoyF9bj5t6uSJofS32wIxmJL7B1Yk-W408KaUmaxcOVSpSz7-0mJUh7DP269_sccoRQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دربارهٔ ایران: نشست دوحه شاید مهم باشد، شاید هم نه
🔹
خواهیم دید
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/664732" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664731">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4KP3le_DJIv0QLv4tapIPtHJ-a0_QGI8q3OqLbdWdFCjR7EgzDUpl__k3vnwLSBG_MwBe84ry7GpDoI2e1p2DCxm56cyJhZ800bt96LXKHW7kW17pSN11vKOcrSmoZGPiRPZ6cDZrlFZZGTSbR-CFpk2i6RZ9mglZ6i_mGRhXx6bXMMOl0PI-4wsgSg3BScmwMrOn8YBkz7ofTL1JLlXqYK8keg99p66o70cKVEDM3SG1sFAbD7o663geu977Ky73newwVnhtU_KR2wmHJo1Wuv43Ql1j96CeT3ULIzrgU47Au6VsvNKK9AVcfRywONixucIeUNvU1Uv7KEFKKL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
سفرش با تــــو
چمدوناش با مــــا
باروبندیل رو جمع کن
امکان خرید قسطی چمدان با
اسنپ‌پی
😍
خرید از سایت
https://baarobandil.shop/
باروبندیل</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/664731" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664730">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyK-61kHQTbn2ZmG_5VhaJb0p06Y9Wo7WODHpPprQ32dfNj32ewZfo0od1ZNWNPEM3Qn1TQ_c5TVyq-K2j-7pXmxfTlCAikvr77a2oh-YPlwLZxA6kAcQCiJX4N3PO81WRaTZchCBrJ6vTE731WW7wmbE21TMUvyuiV6ZjFT6wtdteMa-TldWJzXwvLeswGPEytU9lKOu-ff6n56quzAr9DEz38qPm_XnOMr7ByIuJ9CnorIbxbE3oLZDE3pdGjGWKn-mgcMyAaBtdX8v_2ubPEw-0hW0QXYzkF5EP8zlOonXCK_CkeeLSZyGH5zqKbJnxvAgZCGSl-9aZhg-HDPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داروسازی دکتر عبیدی از داروی جدید ترکیبی کاهش چربی خون رونمایی کرد
به‌دنبال ۱۰ سال پیش‌گامی داروی روپیکسون (
®
Ropixon) در کاهش چربی خون، داروسازی دکتر عبیدی از جدیدترین راهکار کاهش چربی خون خود با نام تجاری روپیکسون-‌پلاس (
®
Ropixon-Plus) رونمایی کرد. روپیکسون‌-پلاس (
®
Ropixon-Plus) از ترکیب دو داروی کاهنده چربی خون با نام‌های رزوواستاتین (Rosuvastatin) و ازتیمایب (Ezetimibe) تولید شده است و باعث کنترل موثرتر چربی خون و افزایش پایبندی به درمان به دلیل سهولت مصرف می‌شود.
داروسازی دکتر عبیدی از یک دهه گذشته با عرضه رزوواستاتین (Rosuvastatin) با نام تجاری روپیکسون (
®
Ropixon) توانسته است به پیشگیری از بیماری‌های قلبی-عروقی در بیش از 1/5 میلیون نفر کمک کند.
برای مطالعه متن کامل خبر روی لینک زیر کلیک کنید:
B2n.ir/zy8686</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/664730" target="_blank">📅 23:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a4caf891.mp4?token=Q5As_dOM1fqfhmL4WjxnNkVZFmyEVb2EG8iqnYhyUr7NgEJwtt7LSQMGxpEWdDqzYX4x5eBxAxgxjd7q8DkVsQON1Q3Y0fj6JsC3HpMPDk_3Ngd6drXJm60c924OrteYQgnEJRUIkLok6eaKdnGYLAHqj7O-5zDjB5YxYZAkQ-8iHT3MPLQEc-sK8OTPUleehC7FddvgLl27H2q9KaTGk_o5m5wJKukIUqm8Ir1NDk4Af--VJgOMlQYNM09ay_0aOYDtHgvKXNNG45tFlCUn6BmcDkPx6rppgaKPZwtZ3N6m8PapoUe1NzpM0uFH2GB9BYZtgg8uOpnj2jOuIBBG_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a4caf891.mp4?token=Q5As_dOM1fqfhmL4WjxnNkVZFmyEVb2EG8iqnYhyUr7NgEJwtt7LSQMGxpEWdDqzYX4x5eBxAxgxjd7q8DkVsQON1Q3Y0fj6JsC3HpMPDk_3Ngd6drXJm60c924OrteYQgnEJRUIkLok6eaKdnGYLAHqj7O-5zDjB5YxYZAkQ-8iHT3MPLQEc-sK8OTPUleehC7FddvgLl27H2q9KaTGk_o5m5wJKukIUqm8Ir1NDk4Af--VJgOMlQYNM09ay_0aOYDtHgvKXNNG45tFlCUn6BmcDkPx6rppgaKPZwtZ3N6m8PapoUe1NzpM0uFH2GB9BYZtgg8uOpnj2jOuIBBG_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقض دوباره
حمله هوایی رژیم صهیونیستی به مناطقی در جنوب لبنان
🔹
جنگنده‌های رژیم صهیونیستی در تازه‌ترین تجاوز خود به خاک لبنان، مناطقی در جنوب این کشور را هدف حملات هوایی قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/664719" target="_blank">📅 22:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664718">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
نمایندگان مجلس کنست اسرائیل به جان هم افتادند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/664718" target="_blank">📅 22:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664717">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2jbdM-jIbAkLUrZpkq_1JoYL2cqFTn62X1pcGJxMkD7Z1dYHaLhOqCfz0rA2Gr1ONCw5n68SwJUXLUmhNc7MdB_CiUMUlknZAat4Bt1rRhRjAhFGqGXPX22P1TIgJ85eZSx7V47fEvixwQvd5lZWtDkrhKBfomWzCiNCN8LsIXioQ5IdCgXc1uAuoZ8dVQAPnmvXQ2aO9kWGT71iWBd_R9t2_7Hu6UXdr4xmJHM2FNMfODj4Wes9zCiVoKhP5WoVnDf3YspsCi-4sdkf3vaprElwr4k0eiSobCvZC88QMHLAxtXaSjPzHLSJoBS7J4voKIU_-FH1BTmjgBSSpz2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سکوت، پایان ماجرا نیست؛ آغاز مطالبه است
🔹
مطالبه مردم روشن است؛ پیگیری، پاسخگویی و اجرای عدالت.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/664717" target="_blank">📅 22:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664716">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سردار حسن‌زاده: امکان ورود ساک یا کوله‌پشتی یا وسایل حجیم به داخل مصلی برای مراسم وداع با رهبر شهید وجود ندارد #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/664716" target="_blank">📅 22:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664715">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
آغاز تحقیقات دادگاه لاهه علیه مقامات امارات متحده عربی
🔹
دیوان کیفری بین‌المللی (لاهه) به‌طور رسمی تحقیقاتی را درباره تعدادی از مقامات ارشد امارات متحده عربی آغاز کرده است.
🔹
این تحقیقات در پی اتهامات مربوط به نقش این افراد در بحران سودان صورت می‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/664715" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
برنامه‌ریزی مجلس برای استیضاح وزیر نیرو
امید نصیبی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
قطعا مجلس برای استیضاح برخی وزرا برنامه دارد و یکی از آن‌ها وزیر نیرو است و توازن و عدالت در برنامه وزیر نیرو رعایت نمی‌شود.
🔹
عملکرد منفی وزارت نیرو در بحث سد پارسیان موجب بدبینی بعضی افراد نسبت به نظام و عصبانیت مردم شده است.
🔹
علت به تاخیر افتادن استیضاح وزیر نیرو این است که باتوجه به حضور او در کمیسیون‌ها مشکلات برخی نمایندگان حل شده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/664713" target="_blank">📅 22:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
پزشکیان: برخلاف برخی ادعاها، در مذاکرات هیچ امتیازی خارج از چارچوب منافع کشور واگذار نشده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/664712" target="_blank">📅 22:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664711">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9UFeAmNtze_H6sEv2W6STch3QroMxowRQ1EIg5hiqkIL1XOuJOFRhL_x_3VASH8t-w0FXCDswmYin62A5NkyH9ZC7gcnSTE3pNfsHyXPisOGmPHDetTUw0DVB21JjqFxpnXuWQEC1JGR5msd74ps06iFtol3wVhf-H6bINYu6DV7HEZT2A8FwTUKkfvXoN0fr5xKWoS7-v0yWO_vVD-_GJNlDqZnrjDO5aJV5ffcHhptfN5_xC3GZvqAEQ8Xuj5WUa35iSt6oqQI49wI6ZxIKZtHJJXX589A3CkSAnWXZMPAreA1Q7ULPSJHFZn1sf6Bl2hZI9tkPB1i0A025u1tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
سردار حسن‌زاده:
🔹
طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
فرایند برگزاری و اقامهٔ نماز نیز در این طراحی دیده  شده است. در واقع، این طرح، طرح وداع و طرح شهادت خانوادگی امام شهید و خانواده‌شان است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/664711" target="_blank">📅 22:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664710">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بیانیهٔ مشترک عمان و فرانسه: ما بر تعهد خود به منشور ملل متحد، حقوق بین‌الملل و حقوق دریاها تأکید می‌کنیم و بر اهمیت بازگشایی تنگهٔ هرمز پای می‌فشاریم
🔹
بر اهمیت حمایت از کاهش تنش منطقه‌ای، تأمین امنیت راه‌های دریایی و مبارزه با اشاعهٔ سلاح‌های کشتار جمعی تأکید می‌ورزیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/664710" target="_blank">📅 22:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
پزشکیان: برخلاف برخی ادعاها، در مذاکرات هیچ امتیازی خارج از چارچوب منافع کشور واگذار نشده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/664709" target="_blank">📅 22:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
کاش پاتل، مدیر اف‌بی‌آی اعلام کرد که از زمان آغاز جام جهانی فوتبال، بیش از ۴۰۰ پهپاد غیرمجاز را نزدیک استادیوم‌ها و سایر اماکن ورزشی رهگیری کرده‌اند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/664708" target="_blank">📅 22:33 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
