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
<img src="https://cdn4.telesco.pe/file/lLXwe67IM6q4i7_wEk8EmefCQz56-Kpj1Lf9O9W2WspQKQZWCsldUdzuc7CCDCUQuaB8J52mhtscpBf8okUALc9CiW8uTxZ8EBJMY6_QZEGurLYODtEiQ5aSUEUvTaVTBw3pXK8J2Tg5bPGPq_lMw6tT-osUyXNVwhOZxU7wM2MSx9WpMmGkIwXPF1QlgT6xlKqxpg2PdE-Aq27ogBKYRPrbxfxe4NsCSv54w-1Wns0hsUGLFBQnzAse9GoP8AdG8fiTTmCdsNKAJMj4Mzs1m8-OgYVsYzsv-5es8sF50Od6QZ1C6oDFNcv3H7ysF1eUMbSE7y1sM1zmvK_vw2UZ6g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 00:38:49</div>
<hr>

<div class="tg-post" id="msg-446080">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
حملۀ اسرائیل به چادرهای آوارگان در جنوب غزه
🔹
المیادین: در‌پی بمباران چادر آوارگان در شهر خان‌یونس در جنوب نوار غزه، حداقل ۳ نفر شهید و زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/farsna/446080" target="_blank">📅 00:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igr9HVqmsSRP6B2bZFN5a84FRvwsdQFUVn91YlMNwd5xZWQddkQBeuLq8N6nRPBmHLgYypDJtzP10pD3YS_P15KmCbif5kDwxd8-MoZM30uPIMggRDu_kYja8yz-pyF1N5HbhB6YaVtX6f-_V92iNTttvlf7U8RMXWYJ9t_PG4gzmK97MPi5cilUcg85UoU8WYWRfIqlJw2l_NMX3l0boGd1dYWk9mDHUExgfJlWB-gTEhfkj_XGxJq2Zho5lTGAhzJThN-2-7DPPr7S7G8exdWFY39rcOUcSUCDYK2z_o_2WvbSpUlcYqvM7cdSLGjZWk5k2BtaA8AC97Zb9vUJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود بی‌دردسر یامال و رفقا
اتریش برای اسپانیا حریف راحتی بود
بار کج شاگردان رانگنیک به منزل نرسید
اسپانیا ۳ - ۰ اتریش
@Sportfars</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/446079" target="_blank">📅 00:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e55c2f97.mp4?token=WSXogf41kaYmjKC6g978e3HeX2rj4Jk6Z6MTANl754Nlm3mJRuJyC6GZw9kcAH4PKGGfhqToy7fuQRSjvZPvkVdOCaH8jGVLXbNdAictfhJ9J_a7AbhozbjKQsTIW3Bi3t42TuUma21BY4tJT-Fdpy6bONyYBTiI6vZ7qisNfkTF9MueqRhvkta2L3b6Ye-7Yx44fisoEIj7bjV3_HO99bO1FLP6Wo6GpqrieNz2H8aqYAzUXvaBsLlQjJOYS1tfAv2qy2ky2fJiTk7FNK470X2gpvZzXi6Ne0KxUOGNSZ2BevBfxhOEoEQdrad4ukFs9gzqTMUmL9_Zobhb4AhVCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e55c2f97.mp4?token=WSXogf41kaYmjKC6g978e3HeX2rj4Jk6Z6MTANl754Nlm3mJRuJyC6GZw9kcAH4PKGGfhqToy7fuQRSjvZPvkVdOCaH8jGVLXbNdAictfhJ9J_a7AbhozbjKQsTIW3Bi3t42TuUma21BY4tJT-Fdpy6bONyYBTiI6vZ7qisNfkTF9MueqRhvkta2L3b6Ye-7Yx44fisoEIj7bjV3_HO99bO1FLP6Wo6GpqrieNz2H8aqYAzUXvaBsLlQjJOYS1tfAv2qy2ky2fJiTk7FNK470X2gpvZzXi6Ne0KxUOGNSZ2BevBfxhOEoEQdrad4ukFs9gzqTMUmL9_Zobhb4AhVCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم اسپانیا توسط پدرو پورو در دقیقۀ ۶۶
⚽️
اسپانیا ۲ - ۰ اتریش @Farsna</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/446078" target="_blank">📅 00:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446076">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZ9bSQeyqikSU3m-NUyhloBAB8MgG97uFHc59cNuCHytbL1-UAw61ApmI7An7wxLKnxodc-Bk-lRPZXBGlQGvsqiei35OPCarqdTK8R-F_ZqQgMOg5oA1tKKANpQB0Bzyysivf4CW_qhmqAAr3ue8Jw1J-cT8dJNkTPMhC1SpyQEe2grpXKxhLIng2uFbjQZ7guBsmWblqPigrHHcUqdu1l55Nf5z0wsZ1-LkrtARyY7OFmtr1rCswk6KTNjFCkUoeFFXMmLWhvF6o9vfh9XTqXMU2Ya44nfoQsvJH8MiqRqmvZtRWirEIJw4RZj0_miH8g13RtucgI0wKvCeYxd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFaMH7x9DGVRHmclA7umcvXUDieAbF_GR_WBnnH4Qs_L0s1Q3KSPe8cRaPQX5hqbzRjaAMJXQM5gWZs40iq7IKeb55ErGOedHIRzDNTv3013a2ZUTiWgieOuWMM1sbHAOWa-ah2adQ5pxyC9b8zwVD6DpodELWYJ2yUeKZF3qGJGJZGm9w0cM-SpukhgExlXl9SJ9V6Re5qe5Jqwf2jWt0AAEvWl8Xkf7Gpos4QzW2uaiPxpgacKzKwIu_FBF_zmZXvK6p98qUVj90qXlgTq8e3pymTe6UWkSFZL0ISGkKpoFyB1LjygEB4wWj6zdLkI7icj5nb8atvy20t2kQvYHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور سردار وحیدی در مراسم وداع با پیکر مطهر قائد شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/446076" target="_blank">📅 00:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446075">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t500-C9L7a0UtEaLMC8Os-rbF7Ambz5JAABDMEEHEAw4vWm0oHz5DKxCf1yLrLlufHF-sBJ9D8REwJSUJQThQxMLb56kNB69S7cJctRf2yd1iZcAAjdC__zp2fVwT6aQzTHxmOjlK-cAkuYyLu68dTWRV4zebl0fateVbPVm10q74KVuXxjvxMljvVRrY2T8Th5NkufbSDHjZNjA3xNy1pNAmK__NvOevSAhWvwNhYhzYQdvQB2NXZsqbwdLUh0_ZsCMSOW2LWgRFB63lTDS-9yrJ7AtVQPjUemwLgn7PkF_T7Yh7ErBPkAWihnu7afMVx7zzGgCC18HfstRItE5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نان و نمکِ علی(ع)
🔹
عقیل، برادر بزرگ‌تر امام علی(ع)، به‌دلیل بدهکاری سنگین به همراه فرزندانش به کوفه نزد امام آمد.
🔹
شب‌هنگام، وقتِ شام فرا رسید. عقیل که گمان می‌کرد به‌عنوان برادر خلیفه، سر سفره‌ای رنگین و شاهانه خواهد نشست، با یک شام بسیار ساده (نان و نمک) مواجه شد.
🔹
عقیل با تعجب گفت: «علی جان! تمام پذیرایی تو همین است؟! من فکر می‌کردم در خانه خلیفهٔ اسلامی غذاهای متنوعی پیدا می‌شود.» امام فرمودند: «مگر این نعمت خدا نیست؟ پس باید شکرگزار باشیم.»
🔹
سپس عقیل به امام گفت: «من ۱۰۰ هزار درهم قرض دارم و برای ادای آن به کمک تو نیاز دارم.»
🔹
امام فرمودند: «من چنین پولی ندارم؛ صبر کن سهم شخصی‌ام از بیت‌المال را به تو بدهم.» عقیل گفت: «بیت‌المال دست توست و مرا به سهم خودت حواله می‌دهی؟» امام فرمودند: «از بیت‌المال چیزی بیشتر به تو نمی‌دهم.»
🔹
وقتی عقیل اصرار کرد، امام علی(ع) پیشنهاد عجیبی دادند: «اگر عجله داری، بیا شبانه به بازار کوفه دستبرد بزنیم و قفل صندوق‌ تجار را بشکنیم!» عقیل با تعجب گفت: «علی! به من پیشنهاد دزدی از مال مردم بی‌گناه را می‌کنی؟!»
🔹
امام لبخندی زدند و فرمودند: «چطور ربودن مال یک نفر دزدی است، اما ربودن اموال بیت‌المال که متعلق به همهٔ مسلمانان است، دزدی نیست؟!»
🔹
سپس امام پیشنهاد دیگری دادند و گفتند: «اصلاً بیا ۲ نفری به بیابان برویم و راهزنی کنیم!» عقیل گفت: «من اهل راهزنی‌ام؟» امام فرمودند: «گناه راهزنی در بیابان بسیار کمتر است از اینکه منِ خلیفه، دست در بیت‌المال مسلمین ببرم و مال مردم را به برادرم ببخشم.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/446075" target="_blank">📅 00:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446074">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fc02174c.mp4?token=pzkN0l8uzJekLIdRW7035bZc_lDOvyO6ZYKYxqUpt0ccGqGfhfnHxTDIgL9EqPKJ2Pfc0r2n7TDHcFRimDAYsM3hDQaDAbBzj50rCIQQRJ_UbhDTNcbpEfeZnD-3GBbMzFbK9B6o1Hxr-d4TYxJHyQxKH-S-zvM7T1Ot6Q28ZKKSzq8LQDqCh2sC3Jai6LC9nbto6jOHpZrIhjHQ5fLRYY306MZMAluZEcZ7Nb8JWU1KXbDKd_SVjN25cqpiRfd0euMjcSoGi_gFEliQOnqjMY_a0N-HBJgqUw3XyA9stQWFtXkMiKX6Xuq2SFC77MpHzHR6vVLAmjsS-TzAygdKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fc02174c.mp4?token=pzkN0l8uzJekLIdRW7035bZc_lDOvyO6ZYKYxqUpt0ccGqGfhfnHxTDIgL9EqPKJ2Pfc0r2n7TDHcFRimDAYsM3hDQaDAbBzj50rCIQQRJ_UbhDTNcbpEfeZnD-3GBbMzFbK9B6o1Hxr-d4TYxJHyQxKH-S-zvM7T1Ot6Q28ZKKSzq8LQDqCh2sC3Jai6LC9nbto6jOHpZrIhjHQ5fLRYY306MZMAluZEcZ7Nb8JWU1KXbDKd_SVjN25cqpiRfd0euMjcSoGi_gFEliQOnqjMY_a0N-HBJgqUw3XyA9stQWFtXkMiKX6Xuq2SFC77MpHzHR6vVLAmjsS-TzAygdKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به اتریش توسط اویارزابال در دقیقۀ ۳۶
⚽️
اسپانیا ۱ - ۰ اتریش  @Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/446074" target="_blank">📅 00:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxNU7ho8epNolUcwOt7j4IWW1D9OgZC-zfqa13RkTPCaKzlYjSQedjtm3hCvAHWQBLkbmYHe2gOsKNFxQNNAFHKm4cmD7p6_kh8e5wTdyp8vY3L9EtUPvcZdvIvXmfv2QNcYJORkUw7GldUJpNA6ZSDeFSvxpgzBAoIhREIQOb7Qn1pf5jYOX0Ff7xZehjhCzH9YfMtY2bYaMedmzFlxVPH6_i1EhLGJGEYwwuCI9QUffr6vCAKR-qQ4rlZxrPpmseeVFDLxEs2mPFoQHTqhiaoOuvU9yVHlsVeQFGUyqRxT7rVrhPosT2b-zFmLwKetriLuAjt6m6UYohth6Tti0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| جمعه ۱۲ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/446073" target="_blank">📅 00:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446068">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oANhnbPeIEOlQSbCyakJoLdubMfq1ktXJU0n5dClyCYUab6_B3cR1ApDRV2UH58BPv_-GelSAI8nVX2bSIoTx08Lrg3Sgx98Krm9uF_U7RJReUDN52Y8BOvPB0U5kPvP6VH_16Zx0rgn3ES-VIRv9yemOfjUDW34-nTHSS18nOnTw0idpq0NDAtiRIOLZUm3sKhVIoZYrXNUTS1mS-8qi_zmLcDYRW1TlJA-F9m322aDwA2TdIQVEnWvetvh7qXEm5V7qIx00HsN_K9f6e-F--iciSwf8mqsbRXDOFrTgt_KXvZybGEmvkU2UmXdGU91_cXMi6aBKISqFe1O0AVIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HpRTH21_7nIfjUraT77PyGF6u8Go-SfpKalFMzYgY-Kj01XIeW1Rsgkx6573FuRHNNX8OSMIIuWuy8fEPeXG9yztvF4NSJOpB6nsqc818-OU9UUUwKo-_8xZaoSZtsljsTWKAvFfKva62DV8S7VOGs4uPx7kmdnsbIulTqerFqu3xVv7bEgqZfgM6zEqVrnTE_RaXIzAC2qup0t2n3NClwBSrf0E7NGT0CGCFBVR77UaH8zlg1it7etXOgfNBKKmCnjjXne4vFAkmg_8kriRb5PGuWCycO1gr0RFD4l26YeX4PQw7_TeR9b5dH6UdUV3D7IsN7OIcehyCffJiZMP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqqMkfVzYbHO9fzhKLjvJKEVdMi2Ph9ItnoYt6yHM9RM8FMP60vA_QrV-wyZPG7y-BGGLBIRJMrVAJ6Ubx9eXEsv36nd_8oOxEtwd3IbzngLDe1xZUHL3cXZvuwRSlMVMlNVWZO0mqfCaqkxizjh9NN_IsEqtxxBZyXzEtARYUDWhC1u85rUQcPG4T0tgV-z1TxZEoJAcr4FGJ5pTBaEKl4t2JL-QTeZKqpYaTWt4qFaBRCKzazXB86zOpdwMHB_pVAhaRRGZ223U_qc5pyGnAcFIqHB6H78-6lYTuagl4nujVWJrxAdMomfcdfgZm3k0I20_Dg0x8y21-dhitGnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFvdGQuE29Zm-Bzz3mdQx2stdU5SGzL6cCw9zY7wBGdlKTeEV6f7ViDMEM0xNrthvDoQAaNOk_JoaMTL9c5jKWoQbqxnDkPDAGzbIEHp4Nbg8xM8U8aN5OQLuUphmnBJj5Fwzakfwxnhf8ohdoHKjGM26ArX6b1PrXwOPfNgvih7WubHHOzDVCYxwenJ5uWyBYvS0G-S93PHK1VIuu3Fl6vIu6f3R8df-3bsnVPoznOOgr3XomSCbowFZKYuF8DxU-IQg_7PmEUcK0b2FOlgfxJAEysw1G-7r6ndk3FwgCoEg_ySg9dCxZ4232yqrRtsJIwFdxhX3e3J3AxxSkymUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmRQ3RDvA2JuuYoDaSSJdY6XK5g0FrFtaZKSoV07NbHW_0ns2FKuk9k4g4nFXA6E3oyJkYjOnpjlvnkTd3Rv4scoQDdswZJ05sDUSPAIGLHXwHkhB-M2QFUwfhcGOJDMT6OeKXvRt54OjN45lOhZ8wYKQbfhgLR7VppPdKvIRYx8zUo1AB9O16AFXB8OdOMPEbXmDELjp0gRRKZAiPVUyh7MMcUVZXjcK2dWHdEnfOdN5hutpk-x02mTiaXfVubdaG14edRDBd6Xj_k-AW4q_n2Hs9mHuD7_r571lbGk26wiQT7oML-63284SlYvtdHHRb2PQkEPlVKjh1EP1WvVZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
لحظه ورود پیکر رهبر شهید انقلاب به مراسم وداع در جوار حسینیه امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/446068" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446067">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etA4MnQ86o2LhZVvOs0rL_uxQ9-RIqvxK7yVvX2V4ZSsXtvrfUPYSYY2lOkEHPQC9qX9_qJvFmKFKjpQD4v4Lohrub_HvEVJSfB3anavD58BJ3gjqooElZnNb_y-jINHb58MAv9IMRxXMsenBehfpdyWzvxQCepDslz1twblIxWcjyCGj9C8lkdJg0BCgXamVn1oaysPL7-DDIdAWn26lF1NrLZj7kTZ3I2_nKrDe_y7Z7jNNjVmMVtVXT3wA-034UtzTW_JNBnsmUHR7UOBNBh41kovz2Ae6-jhJ_OdGho7pNjvUoKNZs2ywHvsdgv0BDCFNDsiGfdqce43fgC4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت مجدد گوترش به ایران در تماس با عراقچی
🔹
دبیرکل سازمان ملل در تماس تلفنی با وزیر خارجۀ ایران ضمن ابراز مجدد تسلیت در پی شهادت رهبر شهید انقلاب، با ملت و دولت ایران ابراز همدردی کرد.
🔹
طرفین همچنین آخرین تحولات منطقه‌ای و بین‌المللی، وضعیت تنگۀ هرمز، روند اجرای توافق خاتمۀ تجاوز نظامی رژیم صهیونیستی علیه لبنان، تحولات پس‌از امضای یادداشت تفاهم ایران و آمریکا و آخرین روند مرتبط با مذاکرات جاری را بررسی کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/446067" target="_blank">📅 23:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446066">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b661961b4.mp4?token=g_pjnRP4evUIyj4eyJKtK0itobNVgDLPicZpoHcSTZU-G_RFCMnY9KU4DuiUbufqcQsAMNyNilVJOiqSWnmspjbKgL_eP76mbRpOqdwuPBGrWbIJnTqiC7iBReN93gWiW7V9q77HQvWagwFg72K5C0QdgW1gVaQkakCMSSeYOHEHK5poaDTZFkFq4pd8vacGorPg20v4fRyz_bBVtY3Ar5jtgsWSztmQFBQObBfTvYo8xwinBy2EJRxPURonIR1inW-SQ2DjFzZpotgyG5UVBcD2sLGsjRi4DHbvxq1fnyMnsGB5AQ-lYqutMki0jx_vYURLRlDuaJsLymSeBBDRZFzam-IipFEcg30nvTrJUDbDWoYYw5rXCgN-lHS7bBNWH94UXsJYTDzg3qijLorH3Xl7FAp4ajF_PtTMzqmsM09sj6y0_qNbCMgxI1Q2Z5T6Ev3Z1wozqEGkjVetdb8-pPsLn_GT9eweiP5wTmeB5tG1HfDK2yGnb_ErvTyTRB5gR3PwjQgFqRt3tJigLyU7WxNNNC9b4UAPACNa82LR4Ep0BzvQlTlunk9siVKwciTRgyWkNIWGVZiAaYseI6qkFqxEExKq3gztv1kq48uX9t87-8CjFWO0m7aGD5vaIsK3yJaVvwYV5SgbqgPUjj_jN1oz0kY7vSfCfxJ_BWdleps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b661961b4.mp4?token=g_pjnRP4evUIyj4eyJKtK0itobNVgDLPicZpoHcSTZU-G_RFCMnY9KU4DuiUbufqcQsAMNyNilVJOiqSWnmspjbKgL_eP76mbRpOqdwuPBGrWbIJnTqiC7iBReN93gWiW7V9q77HQvWagwFg72K5C0QdgW1gVaQkakCMSSeYOHEHK5poaDTZFkFq4pd8vacGorPg20v4fRyz_bBVtY3Ar5jtgsWSztmQFBQObBfTvYo8xwinBy2EJRxPURonIR1inW-SQ2DjFzZpotgyG5UVBcD2sLGsjRi4DHbvxq1fnyMnsGB5AQ-lYqutMki0jx_vYURLRlDuaJsLymSeBBDRZFzam-IipFEcg30nvTrJUDbDWoYYw5rXCgN-lHS7bBNWH94UXsJYTDzg3qijLorH3Xl7FAp4ajF_PtTMzqmsM09sj6y0_qNbCMgxI1Q2Z5T6Ev3Z1wozqEGkjVetdb8-pPsLn_GT9eweiP5wTmeB5tG1HfDK2yGnb_ErvTyTRB5gR3PwjQgFqRt3tJigLyU7WxNNNC9b4UAPACNa82LR4Ep0BzvQlTlunk9siVKwciTRgyWkNIWGVZiAaYseI6qkFqxEExKq3gztv1kq48uX9t87-8CjFWO0m7aGD5vaIsK3yJaVvwYV5SgbqgPUjj_jN1oz0kY7vSfCfxJ_BWdleps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه ورود پیکر رهبر شهید انقلاب به مراسم وداع در جوار حسینیه امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/446066" target="_blank">📅 23:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446065">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13db40e712.mp4?token=H5HdFv7bxkyn0GAtUKz4oWfnmQVV__cTv0cK8q3tt57EKJLup8lTTk0_y5Hhfd45unFMvbO57RS68cwU0Jj9AjKq9APFIwHUbK-s34S4km9RlXDvuVGbFNHGBe1NAhhNtlQN5QtnpiIYcch6epG6y6q3Zrgi3WQOEdtxQWGgxQOEKO26bje-sWH5dst4E9DiddcZlNjmz4PISCEA7fF3sMyI_XIvkaE53EUPCYpFYvDc6h1WhmvYTXJYKsNG53OURx25Tnh4PA_Fcmp-kRQaoYb2UaM67cj0i7BOWaaJE10-PXv-K2kh--jHlkXPZBMPA-Xat4cE_iYtq4MvUi_jeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13db40e712.mp4?token=H5HdFv7bxkyn0GAtUKz4oWfnmQVV__cTv0cK8q3tt57EKJLup8lTTk0_y5Hhfd45unFMvbO57RS68cwU0Jj9AjKq9APFIwHUbK-s34S4km9RlXDvuVGbFNHGBe1NAhhNtlQN5QtnpiIYcch6epG6y6q3Zrgi3WQOEdtxQWGgxQOEKO26bje-sWH5dst4E9DiddcZlNjmz4PISCEA7fF3sMyI_XIvkaE53EUPCYpFYvDc6h1WhmvYTXJYKsNG53OURx25Tnh4PA_Fcmp-kRQaoYb2UaM67cj0i7BOWaaJE10-PXv-K2kh--jHlkXPZBMPA-Xat4cE_iYtq4MvUi_jeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی امام‌خمینی آمادۀ مراسم وداع با پیکر آقای شهید شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/446065" target="_blank">📅 23:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446064">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5a56810e.mp4?token=rT0xlZQjt_oeQTvZ8QPjHc-iGTTUy3-fU39qbM9Dxy5fNga3MNvrVMu4d7Cb1OSsCHhdchBwfxTR1GYLqGRzwLHU6kdRF_Wo85dhCqCCxkJWAaJ3AmKNFxjxkxdt5qpWclvI2eXg8tcIpn3EQz-U1LP3HqX5WsY-LmkRnIXyX_VgTcr-DIUZu0j6vIaQQspNkwzBLMCwjQnQDd6GNDUQp386yXDor8YkxlEnH41-BPkWgxLMWxiipc25s97a0_RbBb1gwv6gO77dwod-ZCOa7WP_PE13wVXppGkRWuQDd4usDsrE5LUSRCtjsdTRjuj8Mjdt2DAIpjnTlrXXtjQwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5a56810e.mp4?token=rT0xlZQjt_oeQTvZ8QPjHc-iGTTUy3-fU39qbM9Dxy5fNga3MNvrVMu4d7Cb1OSsCHhdchBwfxTR1GYLqGRzwLHU6kdRF_Wo85dhCqCCxkJWAaJ3AmKNFxjxkxdt5qpWclvI2eXg8tcIpn3EQz-U1LP3HqX5WsY-LmkRnIXyX_VgTcr-DIUZu0j6vIaQQspNkwzBLMCwjQnQDd6GNDUQp386yXDor8YkxlEnH41-BPkWgxLMWxiipc25s97a0_RbBb1gwv6gO77dwod-ZCOa7WP_PE13wVXppGkRWuQDd4usDsrE5LUSRCtjsdTRjuj8Mjdt2DAIpjnTlrXXtjQwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به اتریش توسط اویارزابال در دقیقۀ ۳۶
⚽️
اسپانیا ۱ - ۰ اتریش
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/446064" target="_blank">📅 23:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446063">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شهادت مرزبان هنگ مرزی سراوان
🔹
مرکز اطلاع‌رسانی مرزبانی از شهادت سروان نبی‌علی اکبری پس‌از تحمل ۱۰ روز رنج جراحت که حین خدمات‌رسانی و پشتیبانی رزمی ایجاد شده بود، خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/446063" target="_blank">📅 22:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446062">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW-uQ_C1D8hPOpbl-xcEYLAjHB7lYCZPEBwUGjvdTbLqc5sOWe78xNEF5Y1ZC4aeTq8VLoOW_tpOp0FIiS4YhmcejDU80XJ4UkrkTHpoxSp8osT5PveHaFrFi5SbtRIG8OvdF1ERa04SXZ0r9tNWN5A8Agnjdb4smKADyUfxXE3M_iXBNiAYYaokOTk2voWOOAp_RVvlbXgTRkDtAAZBzhrcsV1e1yU0yZQRq-dV1xdDKeA9SHeLuNpNP-ExvsN6wG7cJKBM1R7fNNT9KWzzYN54z9Z9anOhEHXOYdKTFMPCy5j7ylEn2fwKAXt0j5wTghKf9VK-YaUB0NUfj4-XtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏀
ایران انتقام بازی رفت را از اردن گرفت و صدرنشین شد
🔹
تیم ملی بسکتبال ایران در مسابقات انتخابی جام جهانی مقابل اردن پیروز و صدرنشین گروه شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446062" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446061">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5tKBLeLjfSEmfQH8Z_s_6H6Ly42uXYSi4Eh186h7UFKb9cLqwAiNAlMiOXAGl7vie9SMZoWGp-WvX8u61ktr0l7hyBEtvlaRNkQgufIrsEaW_gv5mJbGmEiNx-ygC7VEw8pWsQ89NxuI-o474Mj3ZlTChPpNiiGXBpARKdiVrQi2onjW7mDnh3NA6hR9EaglR4WPvw2pcrYAMJ7oYj-2M0QiXLRebKfij8YrkzgnHesgYNBK4wluLXsIbNQHr0ghhjRMiyOl74cmzCd3if0KemRnAWJiX-2veT-65szd4iF4VG8l0vm9IudwHtISCEWL7E6zUeJOMCEpX_VHqbNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور اسکوچیچ در پرسپولیس مصوب شد
🔹
در شرایطی که طی روزهای اخیر اخباری مبنی بر منتفی شدن حضور دراگان اسکوچیچ در پرسپولیس منتشر شده اما پیگیری‌های فارس از منابع آگاه حاکی از آن است که این موضوع صحت ندارد و روند مذاکرات با سرمربی کروات همچنان طبق برنامه در حال انجام است.
⏺
روز گذشته هیئت‌مدیره باشگاه پرسپولیس در جلسه خود حضور اسکوچیچ را به عنوان سرمربی جدید این تیم به تصویب رساند و اختیار کامل را به پیمان حدادی، مدیرعامل باشگاه، داد تا مراحل نهایی مذاکرات و عقد قرارداد با این مربی را دنبال کند.
⏺
همچنین طبق برنامه‌ریزی انجام‌شده، قرار است متن نهایی قرارداد طی امروز و فردا برای اسکوچیچ ارسال شود تا پس از بررسی و امضای آن، این مربی کروات به صورت رسمی هدایت سرخپوشان را بر عهده بگیرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/446061" target="_blank">📅 22:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446060">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY2c9tTZCXuSmarVt1jgQZYV7j2hB5RF9BLoK0HlZ-r-hL4k7wDVqFvMker6eoo-lrHaZG_Yh0qEMCGdnQdBu0_mpfuJJX2Txu6IKH4p9rJ-ieobh8vOrWonEKOMmVUw3RfIL_GE61haxTX7vtXa3f4MuoxZFtp-tOlnotCocZkKENUOwRfS6KbfIbg9yZJ2iWbD1H16EgqWLpn0ywftY5XiAIQVjLEc1nqCTwJWUj9-YclsEPULFkRxxGzzQTS6SGFUN9yXJC5AUAKS3A0Ut73ada2Fx4gzNRwzdcFU2WcJoqbzMOphrj46D39Evxhf9BEQMxlW9D5xmsmnCSaxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پاسخ عراقچی به سنتکام: صلح در منطقه وقتی پایدار خواهد بود که بدون دخالت خارجی باشد
🔹
وزیر خارجهٔ ایران در پاسخ به ادعای سنتکام دربارهٔ رهبری گفت‌وگوهای صلح در منطقه توسط آمریکا نوشت: آیا فرماندهی مرکزی آمریکا برای منطقهٔ ما امنیت به ارمغان آورده یا ناامنی؟ پاسخ کاملاً روشن است.
🔹
نیروهای مسلح قدرتمند ما ثابت کرده‌اند که بیگانگان حتی قادر به حفاظت از خودشان هم نیستند.
🔹
صلح در منطقهٔ ما تنها زمانی پایدار خواهد بود که فراگیر، همه‌شمول و بدون هیچ‌گونه مداخلهٔ خارجی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/446060" target="_blank">📅 22:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446059">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
بهت خبرنگاران خارجی پس‌از دیدن مردم در خیابان‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/446059" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446058">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e606ffbff1.mp4?token=GFZ4OTpXNnPORxznd2y0a8s3dGMRRK4wW4BA4c6FYiLVMh-ekpQWLKJlYCdN6P7rhwMoc-klUCO9lQiPrMTgVorK5P3PEUDD6Q6zLVA_6Q7WNdEjEm-a3PsWkfP0PaMkgSmLkje_13vxNIQJTfxnPtgcELZhPAR-5FWkSZSqC2EayPZRcVLBhXCJeB6skmhotXwf99MQprS_KcXBysW_vm5g4n2p9OU8H9osmsLumk3Xxlrujy4v1t7AA0fYs1eqT25_D9XdJKhydKGIrz6jxIqEXfp2SW7Gd_WIP-NBM1-qtHfcgxh0YsiJblv0MZW-epNWQjFX0-g54eEgvJvDSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e606ffbff1.mp4?token=GFZ4OTpXNnPORxznd2y0a8s3dGMRRK4wW4BA4c6FYiLVMh-ekpQWLKJlYCdN6P7rhwMoc-klUCO9lQiPrMTgVorK5P3PEUDD6Q6zLVA_6Q7WNdEjEm-a3PsWkfP0PaMkgSmLkje_13vxNIQJTfxnPtgcELZhPAR-5FWkSZSqC2EayPZRcVLBhXCJeB6skmhotXwf99MQprS_KcXBysW_vm5g4n2p9OU8H9osmsLumk3Xxlrujy4v1t7AA0fYs1eqT25_D9XdJKhydKGIrz6jxIqEXfp2SW7Gd_WIP-NBM1-qtHfcgxh0YsiJblv0MZW-epNWQjFX0-g54eEgvJvDSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیرکل سازمان همکاری‌های شانگهای در جریان سفر به تهران برای شرکت در تشییع رهبر شهید انقلاب با عراقچی دیدار کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/446058" target="_blank">📅 21:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446054">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlNz8VFwcv8mOcB6arGdIpnnZz7WlJZl2etycbuHiPs-ZHKHftuodHS4a0qdilHQHzRXZReeT2qkvnkHf0paA3XQX_aAYP3IA4DmNF6d8zMHQ6CrD7TRp3DgGl3h-WNYwzsljrzp4h3hLPIgroemK6xqWtWjDaVoaw1CL7a6lkQCMHkQa1u1c1AMChcFMZcRmhuRaxgVIwpv1q63c06TZZloMrt1ag5fXIhaA4si-hwAfrRLniqZb_YvGHXVtaD8ns2dYTR_ih15GJb9mraqaZJyOiEqWezylrQ7qb-f9fr8Hs-e8GKPfShOPvbEw3iFO13B7IbYcehNVZKlWvGCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPnufhH9ix2WNf7VwNOkffPn_sI-IwL4_x8oMG_xk7uyyf8RxyJflXj9a6MtywZ5eSGXtBjA9osfqJ5OSL3XVWtUxUwLA46SQvNSrTC-lWWlM3J5dITX_K_3eQiXSw6cHIpNiIZ8Gj4YSn8ChB7jsrdZbMj4iByBj7l6iH_rzJbnhVD9sHKqkMPQpqCd-OfeWAYsePZQTzRYu32sGOVEpFni8txqUMB1pKko0XKQ7bNB8vuI1pXomxmXiQg9DKTDOXCqgPuKEQLC8wR28Yjllh7XNiCIeFWkFqqTTC71qdRsSW8tEtw0mU23xcM9P6mFPn66WFZhsbhywjbJl0dNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLWPqlmJFQ1ekcNnECJ9uvTZqVH-sQLdZxkujm-8xwPD9FZJ6cuFWMaRmqvvjyx8pDl8oJIONQeon-CoeKlZdPyV3Da9SDozwIR4gwc7jBGdkEAipdZWR4kU9pzVjNq8BNmlaA8-Nh2QOOoz2RvTQHi5GRCXbPFZ2ZKtgT2uhvyNFoUzZfNtuw3S85tUxkxIHMWYUnPvOi7fE-woZme0U6MekrgLYKg6Czs3YuI2Ks9XdYP0y-rblKY86Bwq4210pHBBKAXWK-0kRwQ4l1pZuvTphOVSQBSlOZkIy7m6Ekttm_GngqQSb_AWtksiVw86CwPo6EeodrAUEz6VwBezGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbdeQf4NSh5nTOylCR6isJYQlwaW0Lx1cI_yfPfT9ZWgwTybrj0-kYBRT7xpmZP-qLDBELf_m_u-XV6D7MTIP0rKApBKsKPjjDlhZN7ETyOgaZW0fidygx17aFEA7eNMyOj8ChSomqz51poBEvMwkX22aQ1zypSyF5hA0vRvXMtqLhy7PaNr1C9gnXozBc6F_g4r7w_zf9ufQBRvkdVsdCrBWqUS0UH5kSIJdWVXct2XnXYMG6MfZ0uFJe4zPGTI05v3GRDiUi42DDL7gMZA_XUVGazXmYwv-xqOSuQNsgSos4VRD1C30-1psqCMMKOTn7sJXQSNqosrt_7RLnOUwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار عضو جنبش امل لبنان با قالیباف
🔹
خلیل حمدان، عضو ارشد جنبش امل لبنان که به‌همراه جمعی از نمایندگان این کشور برای شرکت در تشییع رهبر شهید انقلاب به تهران سفر کرده، با رئیس مجلس دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/446054" target="_blank">📅 21:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446053">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b21e0bb7.mp4?token=ncFp9c_hKSKBe_xSLtGE52FQl100cgA7SozDlzNjw97UMQVslJtmLOR1qKC0U3UDssiAb7p61hUtnsgu2jX5IOgIjxcY2bLcDZEsva1q4HoUEf9EtAJZbH7RzduPe1Qh5U_OOWwFTrzTtBgyQx81axspBbYmVVcFzu2TXIlZio5-RXgVgkSMAY5ucLCcLSFqLZfYlDfqGtixB-toLciFPWFeYWaFPwBTN07K9vKZlvkOn55y6dA5Y2M0_N76yQCF5ciz-pVpHgWpiXpENCFw3LxLJ66CUMeEGTe8dNSDW8EBkkcJwEv5JOlcwvugRTFnMvSZbhFPm5aGY6CWDSgcMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b21e0bb7.mp4?token=ncFp9c_hKSKBe_xSLtGE52FQl100cgA7SozDlzNjw97UMQVslJtmLOR1qKC0U3UDssiAb7p61hUtnsgu2jX5IOgIjxcY2bLcDZEsva1q4HoUEf9EtAJZbH7RzduPe1Qh5U_OOWwFTrzTtBgyQx81axspBbYmVVcFzu2TXIlZio5-RXgVgkSMAY5ucLCcLSFqLZfYlDfqGtixB-toLciFPWFeYWaFPwBTN07K9vKZlvkOn55y6dA5Y2M0_N76yQCF5ciz-pVpHgWpiXpENCFw3LxLJ66CUMeEGTe8dNSDW8EBkkcJwEv5JOlcwvugRTFnMvSZbhFPm5aGY6CWDSgcMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون دولت شهید رئیسی: حضور حماسی در مراسم بدرقهٔ رهبر شهید، نماد پایداری ملت ایران خواهد بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/446053" target="_blank">📅 21:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446052">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
تا ابد یادت هست؛ در کشورِ ایران...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/446052" target="_blank">📅 21:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446051">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48c46c71a.mp4?token=c5QnRYtxMU8x2t1OnrAYbXKrWyEBb4mUQKuwsIqVL3LAopc_swH1ACp8NIOmYLkjm6pdVmTcEQgYyXkSl2kJEMn0CQ3yK7c7hyQKNFM7XMN0DGMtB4KTwUiq7AeHxtV9JDyli5uJTzZ-VGwQLlY2hp1e80kZ8NJHf_boful9mIqQiUDB1Cx0C68sb14jJH1BAJ9UnCMcGnJb8cPAchhTFHpGkl5wgO-te0puMKEwuaZgfNjpQboVvpdUfZryKYRbsrgDhysQNQRASNX-HIaNll6pyAM_9lz39RW8NlC0V4vs3nNOtz7d2sszkIUaYyP2cbBufmve8wr51DCFIV65nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48c46c71a.mp4?token=c5QnRYtxMU8x2t1OnrAYbXKrWyEBb4mUQKuwsIqVL3LAopc_swH1ACp8NIOmYLkjm6pdVmTcEQgYyXkSl2kJEMn0CQ3yK7c7hyQKNFM7XMN0DGMtB4KTwUiq7AeHxtV9JDyli5uJTzZ-VGwQLlY2hp1e80kZ8NJHf_boful9mIqQiUDB1Cx0C68sb14jJH1BAJ9UnCMcGnJb8cPAchhTFHpGkl5wgO-te0puMKEwuaZgfNjpQboVvpdUfZryKYRbsrgDhysQNQRASNX-HIaNll6pyAM_9lz39RW8NlC0V4vs3nNOtz7d2sszkIUaYyP2cbBufmve8wr51DCFIV65nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: دفاع از نیروهای مسلح وظیفهٔ من است و با تمام توان از آنان حمایت خواهم کرد
🔹
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند.
🔹
بنده معتقدم اگر بار دیگر نیز چنین شرایطی…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446051" target="_blank">📅 20:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446050">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac390ee1.mp4?token=nu-bZkwffsvw8m3JfW-eVvGvU95HTQxDGO1UlI4VZFWcrCaaVG0dcqFQNkdKaGhAdJ0Z6X3UkmO_PvJ2XTle4l3oRZDAjyH1EzzYtRI2Ri82dCLIu84LY3vWTw4ze_7X8skD6qDMOUsdnRnDX6Msprs4U7I1iR_erEORMeXk9jjgKz1hk7XtzAKPF2IYbVwybWOcBaLrL3BWzWOaPbspuW1zti0yCFDJmertkQQdS5PMX7YoRV4RwvxaR80wsRH7PGdCZMbWPu9Ls0aABkA_8yCmEYqkOrBRCKviq0oUUiWls8NL6sj-B7KkvhqmWjC9IzRst-9ER5h6Oly1uuKM_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac390ee1.mp4?token=nu-bZkwffsvw8m3JfW-eVvGvU95HTQxDGO1UlI4VZFWcrCaaVG0dcqFQNkdKaGhAdJ0Z6X3UkmO_PvJ2XTle4l3oRZDAjyH1EzzYtRI2Ri82dCLIu84LY3vWTw4ze_7X8skD6qDMOUsdnRnDX6Msprs4U7I1iR_erEORMeXk9jjgKz1hk7XtzAKPF2IYbVwybWOcBaLrL3BWzWOaPbspuW1zti0yCFDJmertkQQdS5PMX7YoRV4RwvxaR80wsRH7PGdCZMbWPu9Ls0aABkA_8yCmEYqkOrBRCKviq0oUUiWls8NL6sj-B7KkvhqmWjC9IzRst-9ER5h6Oly1uuKM_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
در شورای‌عالی امنیت ملی تقریباً همۀ اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446050" target="_blank">📅 20:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446048">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116b02a266.mp4?token=CrEdMFEn5k0cTSsToa3opbgX9CV8gZsk1DiYg1ZH4mWzORZysdfs3k3FpQNKgMfi65rLHQzjEUOuKe5SQ0Mu5OvNYLOTlglquUvr67pOY3qvoJCg_JeTaQum1b__Q9o3tdf7lQvEqvKrii6-PkD-b7ny-p1WGDhrQ38KbPv2fDrReASShQqbB5H-Nkcesqajs-j-mdGM9XKw3YhwG8QRo6c4GyTNaEiPnKpbv5U3uSrSrXgeoDL_6h5TCJvGJCSYECmq1RpnMrudvj2gXwwsEnlUQ0C1eWKvmpEtbIqWm5_SVi7oxNRLit7qTjqLwiyC8ct5A5ye_8524i1t2XX0RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116b02a266.mp4?token=CrEdMFEn5k0cTSsToa3opbgX9CV8gZsk1DiYg1ZH4mWzORZysdfs3k3FpQNKgMfi65rLHQzjEUOuKe5SQ0Mu5OvNYLOTlglquUvr67pOY3qvoJCg_JeTaQum1b__Q9o3tdf7lQvEqvKrii6-PkD-b7ny-p1WGDhrQ38KbPv2fDrReASShQqbB5H-Nkcesqajs-j-mdGM9XKw3YhwG8QRo6c4GyTNaEiPnKpbv5U3uSrSrXgeoDL_6h5TCJvGJCSYECmq1RpnMrudvj2gXwwsEnlUQ0C1eWKvmpEtbIqWm5_SVi7oxNRLit7qTjqLwiyC8ct5A5ye_8524i1t2XX0RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانشین معاون سیاسی سپاه: سردار شهید اکبرزاده از برجسته‌ترین راویان رشادت‌ها و اقتدار نیروی دریایی سپاه بود
🔹
عزیز غضنفری: این شهید والامقام خدمت در نیروی دریایی را آگاهانه انتخاب کرد و با اخلاص، روحیه جهادی و مجاهدت مستمر، عمر خود را در مسیر دفاع از انقلاب…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446048" target="_blank">📅 20:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446047">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDlS_rsyyGHyvVlGqv9vfGYuXBgjIcHuEp-CFTb4AwXjHngKkYq5-imb6FlX4-WybQM86wior7QM7RndoBbp9McYSILQ1lFRIq-X40s_uTYdv6P1vVNOU2hbx_WaK0S801tc6bjBkiKd_V2-oSnlRMk7EF2vDhAVRvQP08amXHHWLvT6OB9GiWdfEX9Hvt5YUHrbWJkCw108WLX33bTGOvqsyH6WFIfOz9gr_NSv8ioUGh0OmYGpxtjqTmZjuzWlXAC5n08TfCdTzpuhKrhzOrpAdocc8Wg_tyTQUbYvX5cDtIyEpNdailtleEHdQhoBpzlstn0xLIgXPjmd6rQ86Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آتش زدن مزارع و خانه‌های مردم لبنان در دو شهرک بیت‌یاحون و حدّاثا به دست صهیونیست‌ها  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446047" target="_blank">📅 20:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446037">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5pPRIxzeKDw8S1zhATAiHZ1zic_xMuiktUxtG3VpexR4zo_rzyBbVvbXonhan2aBqmVkYL5o01gzqHjtBZEiJ_1aWfw0rG4c8ke3_FhquopHqzMl3y0TVfsBHSZLYSOqYgxRNE57iXxEGJW2os_EV_TkjBfb-AOBME6v46TnJdWJsk9eNnARrBM0RQMl8TfmpHcT9XYAUZgKEOR1veoVNPXY4s2191aDZsbj4w_TPxUapRwzK9iRt6cCUj_JIa8-BjJk_mxWtDHhDil9LSNZL8D8H7xShZfSImXExtk3qe7ebNjPkScJbvXbthi8BYaBACw-3S0_H9PTmAkfda9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPcNRme1QIYvo4W50wnjqjPhME67pCDMLkG2dHIRz7LM0xP1FelxqC47jjfGK1Y7sc6CTx0vUAgTkOzrn1zHMjMZOHZYIu5XSBAeZZAmHRrqe49l32mocnsA5k_hHm3Wr7bZUFT49zwnQ1_kL9SiJ5NIAkpkdQy2tnIddU6_E14PSezVfxm5YUy_86LUZdRpFT0s6ApKyzpDVQceKSiqCUUSv7TrVUYQnIsIrtUs1VTNTkDSFMIlgHjySS4PwIyIVU8FKbq4M1GNL-ILqqp9J7fyDWC_c5ftvUnxFq4Ica7ZQWHSobn9NcA1DKxi5Ya3mqsUz0M5CIpynCl0LONAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSBlNAtJtfFiYCSce3buWExowrDyhTegSFnmHCZ-KIkvP3rg7OiGRcsHAObcWhwIKf5yXjHrG42omkkYfr3epYduCNv1fWJfb2Djr0mgRdcC8eQV_NZb5buK-ltei191ign00J3iT998UwqsU1i56CYQk9l0Fs3cIZqNCjXLpG94al1n83NzcWxw74IJaic8SqDL55fZWMtKLGKu8hNKaxE2lHWZuuTgI389VFYCO1Xu9_jXjqFqu4tne6nrGmjqORU-yjvVeMrGDIMxlWZXwC6rs9aP7XZ58jM_Fz17nl8XteXLTVNjk0TIJyCYbiLGlFXWSkt406YOv7i9mrx6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpFLfyhReK_q2sGDTQ-rtmXfel7m1NWT9a4TFx0LKRaveWKxNE7BmlFFAShVEjiMrWP3nZopaNMcCU7V1Fgr6MuMohB8BoZDqmPRoP4-gpCdOYaIPrSHMKd_uGys5yRUTZM_u-neyf1isRp2I7T3WTjDBx1h97a2JxkHhT7FI89kOjYEGsvsuZ0m9m460wrq0uX1gC8-8aXHj6NlMr0bh0TfjeDLgjYbFhE6iQf34Tr3W0yiBYrTfPMcP4ft2HgaE6RXp_hIz_rU3HTqdj8AsAuqBuAVGGmwtU4WShQmYCQk7ad2B9PjzTsVcyatTm4disA2g8BNGAIocxqKv7LnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-uG214fOnyTuTjfOj6638iqZRwMQJu19YLOGBdpdUNxO4BHbKMx9ufww4oVVmUokdDGRqw-Kd9_pinqM7RRPtPB1Y3z9IsVGCfvovueLRvqLhrXA0cjQ3xWo5X-tUthXHqUOg8EeodbOdwIRog6IY2zorVHg0e_G3Gjdy-rpWo4r1C-Cq_GdEY8ZTVraaRkcOwD0dQgU5SErLkJMJ3lZUoGI5OFTA8gYXpPFItcSaR0DNFDeijWozvmUW79CMT-5PnUuKKDivZ-HUikO6k3BkAiFkhTe7PSJewEsIZSm7XWCeC3cS1tULo-anF_fRppc2DljIuUMirxAl2j2iGu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrZhZIUVUpaduGk2sNqzdPL05CDRne9OZ41kEEkbS_t2c6lMV_QIS3PusXORRRNMNRqBRbp8-SRmZNzyCLTq3Uompb77E-ps5u-UHrWZ3la2__4TNviQbZxGzyKyVi-uUF3ajtHLpn1elK4wrTNg6MDhk-DZQKVXnGdvKqcq3ZgkuA5uk-8Dpw5NJ9IHi4PJlBJxR-sCsk2ymXFuRXSUn7gcfcpWGeJnLIQaFAYBA69l7PnR1FQ6VDvJR71XpFz94WNKs1yeY0-QDjq-5TFjCslDADlZfhWJPRe3_SktGxvkejyXoYqEHFLtCme1UH5O_h3grdYbqT_Ixa9JXyWk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qeiqb_ZvtXcscdYjb15b3FdfM1-_VYY6vcaY1vw6Km5LDKDdYmj67Mdn9XGf9PRl-kpnIKJFSc8ViYu99B2xY0oHhDorJnWfTiyOzCEX2zt8lmGPnOpGdpnM-EbQMpkMUXypw2_zgENpeGLKnahL5hcetfg6bklu64UxpSp_jgQBk7-lGL61r6Gvkjqpx3Vwe1rs3SsFGcgrSd_EnViy0zJ7toVQlHJVe8UoMveD_-ISmt3PEUAPZYXBIU8sPkc6yqGXOQJnqaRSVTa5871YQqsn6Jj0muE3-633ve3GEoPxW_iaeD4ICrw7noBVAUNDELrjOdGRj3y2vXNLg2VfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQ3417wpnVCNYzEC8rTmT2y6qKZu1q35q3F2GQ5g1mnzCKv8rkb3wBJj2CTMRiucDPaQEdLUevIrlU_0vw2Yok18dgjqizvG8XX8BF47Xsi0NjdKWSIxLr6Axr3_6KbjuhHH73V1KtV_DhejEv40-WrtHaHftTYzXjgkLO2mgK2hGOFPGP1MTtwP8fGTZ8CT_xqt6lNcfHH02WV1DVveotplpm_R0NLeKr4e6_86-BY_PgxwzFPbRB5bkMoQxTAyeVE6hygzUusDfjnHv4qNQUGOhI-FOYuFrWAf2hK3ySaheQ_L6qG49asB7R-WoQuSeT5-hiHCqNWsBvAMKANqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJ2XZI8tneQAqT3CJaAgW-p5juEFBfg2_XiwephdNP6Xut5sJyjzdDx8xw6le2jTaBgtyc4l31ZVyWZXocZnphKccacrcBK8xDxOV_MvnWt0tDzKaVUAOpAzcq6c8oc0m3vgPaD6J7HIZIfnB9xrG_bfNmhsm0XpzklpLQTqD8a-yLeYtSH28-WRLniM21KBAmXRarkns6IVOyJX5_5IMD3efpG0YLdOIQYI_wU4V8n-q31HTe_nLGH3RAZb7Sq42fB44b_RJBlO3DUuGyftdH1RH2xUpcrFMmhqnYqcD_eH1JA42opgDG2HlYSZh6ItK-FFcuVuJZk2IJ6TEnDDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2l-OdNNsmkm-6eErW-Bo3Jzbn_u7T7EG1Ev6z9Qo0t2EyTmt7YQvw4ZPfM2LUr2Y8fmyxn3y9l6xfpVFg2lc7rHx-CBxPWzMOc1FIBa2HylYvXC70q0_4jepYtZ8YJsLI4qEAnTF3IpdQJMHSXVLUts0HdSzzv3Pj0xYGDgU5i6Q6MBkLXJlENLtKVeSYbe1K4brzzMTlBPMzspiMfePdvGGZW9MBVhLtCpA9WBtwfnZs2QYbVDO2_vrlj4ypkWTVEt1BB2S_DAkgWxWiefyVQ5TjP3Rz-yNnSCfgTXwml4pb336U6yyBtzHgzPgm_hlBjp6gqSLwWGnuZIiRh8Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اینجا برای میزبانی ۱۰۰ هزار زائر آماده است
🔹
در آستانهٔ برگزاری مراسم وداع با رهبر شهید انقلاب، منطقهٔ گردشگری عباس‌آباد تهران برای میزبانی از ۱۰۰ هزار زائر آماده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/446037" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446036">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیانیه جمعی از اعضای مجلس خبرگان درباره تحولات اخیر و مذاکرات
🔹
جمعی از اعضای مجلس خبرگان رهبری در بیانیه‌ای با اشاره به پیام اخیر رهبر معظم انقلاب اسلامی و تحولات اخیر، بر لزوم رعایت خطوط قرمز نظام در مذاکرات و هوشیاری در برابر ترفندهای دشمن تأکید کردند.…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446036" target="_blank">📅 19:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446035">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQlnxN5Izbdf-8pvFbqhof1XONlDkKaFfBVXp7cQx06tzJbIWWRPJYIHLknopLyYDkr187iWutDhRt1cg-X4saWGKh6IdH-EvcDR0sRcdnHovugOzPtgRup5nsaNaQKPT4VaIwidFY3vVycDzqZezgURL4OJWIF8F3MJDXdbdha9PzSC_H0j72FQoohe7z4ZxIxTGjKipQag2ZT95pdRZyOdwDV6MbrLaMVI0HU28G72bt6W2np32M4tkKaoi4qN0FcrWENcoYabwKwlM8QHMVmSlWbX1AAug2_zQMZtRSwlyOPJwmUHjPMss_6HmUURBi0w5tOX4XQFhMukDs5SkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دختر سردار شهید اکبرزاده، معاون سیاسی نیروی دریایی سپاه: پدرم پیش‌از تشییع آقا لباس شهادت بر تن کرد  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446035" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446034">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f1e3a93a.mp4?token=d6rhbnTKwmgwPn6NoEaGEXfrLMIztCyAxPbTI8-4nSqLF8XfJgybgyVUby_hnIehaN-PQGsoe4snTNW0jS1HCx-rqb7E_IWbAyPrRzwbxA8ALu3jUHabLbUl-dILXjrEuMMlvuWU4YiFZks0bv1rFu3nhe8y4Sm6PH2-y6BvfUUm8DeCpHKi2qLD7qamokdnlyel1xvGIFYJLhONiLvtcq1Nx49RYo-ZNhgARmTFScdguaxuhQ_E0p1Ufr9Gyic0gjXlUZ12Ml9iEBI5ARLYC8r3fhb58BBIQNVYaCH5T5UWZYsitpOgzZuxCXPChfT_foOVbQviG0pJFX0OfRG0uUMFHXH746-HfKVO2EmWWCUWExgSOjL8rUVfJ3i1JHIL-dYVsikK_qo7Lpt30_4JU9DO0-gZfdocRrK49UnKwYtpKSCOde8nSLua46UQWgj5SWs2NH4p5GhHIlt_VQDFs0VSy55baRtURVEs0Zk5DpLUhwKhB3SRFEqLDi0jamP1AmSWNPf2zsr-vXMYr5l9-YF7xoxBB1AO-d_fxxumKEjLkfapdnBmJOr9m7blif-cmMBLbVZ63wQcnYt9lKq-m9BjZXtnrwq0wBSR33fWc0JMYV5ZxOmAZHVyTx7vhbtd2zSEA4gX4p56JZUJd9ZOfbFnNIz4zfa5Ccisz79b2IE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f1e3a93a.mp4?token=d6rhbnTKwmgwPn6NoEaGEXfrLMIztCyAxPbTI8-4nSqLF8XfJgybgyVUby_hnIehaN-PQGsoe4snTNW0jS1HCx-rqb7E_IWbAyPrRzwbxA8ALu3jUHabLbUl-dILXjrEuMMlvuWU4YiFZks0bv1rFu3nhe8y4Sm6PH2-y6BvfUUm8DeCpHKi2qLD7qamokdnlyel1xvGIFYJLhONiLvtcq1Nx49RYo-ZNhgARmTFScdguaxuhQ_E0p1Ufr9Gyic0gjXlUZ12Ml9iEBI5ARLYC8r3fhb58BBIQNVYaCH5T5UWZYsitpOgzZuxCXPChfT_foOVbQviG0pJFX0OfRG0uUMFHXH746-HfKVO2EmWWCUWExgSOjL8rUVfJ3i1JHIL-dYVsikK_qo7Lpt30_4JU9DO0-gZfdocRrK49UnKwYtpKSCOde8nSLua46UQWgj5SWs2NH4p5GhHIlt_VQDFs0VSy55baRtURVEs0Zk5DpLUhwKhB3SRFEqLDi0jamP1AmSWNPf2zsr-vXMYr5l9-YF7xoxBB1AO-d_fxxumKEjLkfapdnBmJOr9m7blif-cmMBLbVZ63wQcnYt9lKq-m9BjZXtnrwq0wBSR33fWc0JMYV5ZxOmAZHVyTx7vhbtd2zSEA4gX4p56JZUJd9ZOfbFnNIz4zfa5Ccisz79b2IE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پارک ارم در تب‌وتاب میزبانی از زائران بدرقه رهبر شهید
@LorestanFars
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446034" target="_blank">📅 18:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446033">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60ef9d66d.mp4?token=Z26CBEBoPFbXUeZskU76gzieps_8zEj2m3AuDK6ab3irPTSGleIU-KkcF7qX-SaVz0oE4QkQqjSL6IqRD1BxbAzUw-ZmMOJuzX78DkMLywGHPcZz2sKKgTv2_OmFeoJC3dQG2uN6muKaypVYPMdMjs5LyopZZR1_aVmnyTdd2yFOztBRcu_ev4PIaDRJhkb_fCdG3S85cRFmhr-AYRENr9mHH0FpoeN0jzRmL_47woTQgUZ3T-PSC6zWJb1gw6XdonzfF-9ctu4cxUOpuyD2O9AkUnSWCmlVONWDIp3SwDyH4qr6Yto8pd-oicH4hKMcNklez6OI-aI4zZNt9lerog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60ef9d66d.mp4?token=Z26CBEBoPFbXUeZskU76gzieps_8zEj2m3AuDK6ab3irPTSGleIU-KkcF7qX-SaVz0oE4QkQqjSL6IqRD1BxbAzUw-ZmMOJuzX78DkMLywGHPcZz2sKKgTv2_OmFeoJC3dQG2uN6muKaypVYPMdMjs5LyopZZR1_aVmnyTdd2yFOztBRcu_ev4PIaDRJhkb_fCdG3S85cRFmhr-AYRENr9mHH0FpoeN0jzRmL_47woTQgUZ3T-PSC6zWJb1gw6XdonzfF-9ctu4cxUOpuyD2O9AkUnSWCmlVONWDIp3SwDyH4qr6Yto8pd-oicH4hKMcNklez6OI-aI4zZNt9lerog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از مصلی امام خمینی در آستانهٔ وداع با رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/446033" target="_blank">📅 18:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446030">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jt_b7CWpzIre9i_APyJlEDTJU34Ih9BAHFANvqzD7A5GEw0E1ZzuA_rAPc0XIgT1KxcAfQPOOUDZeUH0YiIGKNyhNNM22RZY8jq9S7H29AP3R-TDUToi2JMOQlvNF9JwJqhhSgY3v9aKi1dOP9pjQxztD_GovW0FHBGOtK2SNlVAQYafED8ZJqqv9xPaMze3FFgMt2XOJsnNjBfPQxFDcqT2ltrxFsp4bSpiqlLyuaEG2oAwh-C0Dt7dPvq4b6JtG3HTgCWiSFShewIYi3QJ7OGhSY2N4A7N2SZyKPC6wnfx8q1wyqCIrxp-xYEgVTBtKESwE7LL17vzjT2X6P7oFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ak-H4Tirb_GNvqKf_5v2-avRi_Wbq5L5rKmPSRpXYeYiFZtZ-p44DPNFCeLsxxcCZ8B5nbIckgVKreXpAVKNb_YbWRJViEi0TXUzP0P7DePT5xb5T6u2mtG1r-_1jWO4u23ACmF2fqDCwUI1jVWDGf322HpWSbzV2nrdKUfsnaCHdppPPKXPYLicpiAEKs5HGSTQyhwryZ7oG2GmWo94J9D1BSMxJuCSorGndaedlhrINT4gelgGVbp-Q0paUVfvUYyw5DIi6bsDyKETPdRvoQxEAdSbGBmmqPPmsgoj3ff7iwXevwHdeB__Dqq_jPPNCydsOtaLvibSs5bkff3Hdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbXzWNi1bM-DQ8w8FMdrQJrdEoVA9SeHLaVsjmTl3ufKchUb-4QXGe8IvXSxtOuhSnMR5DmjgH3tXxnLufvWb6RQ7yrs9axgCEZoHcquPH2f8CZscANkFK0RYHFIqmgsk_yRSI6cPxo1PjZ2d3ax3c1umQiCBdc6NjVUW5o3e_28dYx8RLAB4W69O3nbrejDvtWihdTSpZWN3Hws1RXBsNtckeDY053Clhkhr34eXsHKM2l12Qqls7IMRfVbGQyknHSMjHip7pr2xNdiumC0lTWPxYlbkj4a33bVL_mRbipGmVL87cOXbcPJM555iFiev-wQiBaB1KyRP6qxm7oScg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر خارجهٔ افغانستان که برای شرکت در تشییع رهبر شهید انقلاب به تهران سفر کرده، با عراقچی دیدار کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/446030" target="_blank">📅 18:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446029">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52aaac282.mp4?token=ObwMeKAOW8tojbDHU2KIrqLDvRMTU79wck6bk51ebX52SHRaqguoxcmh80TtDhK75-lvpYxSAUeOqyqjTXvskj0d0uruAKvELbqnSUkEk9D2axmfvzhnhQrJX29xLCTHbaD1btq3zNnOvMNWe84g5PO45xI6qbHLKGODErHMCSl_ndrcc0Ni20jgDFsu_3k7iQoXXfJ5ziM9aIhfcNu4CP0Pxk3TsPrbr5RO3yXSF5_u8TwILmdWjQicLILJGHZ1AY3UjlrTiwtK1fQ4M0o-gqw7S26JmCyzpta-Rywmw8ngVrNpfTGp3C2Y_9ERUDm72qgvGkFfJ90EZu0MdSlc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52aaac282.mp4?token=ObwMeKAOW8tojbDHU2KIrqLDvRMTU79wck6bk51ebX52SHRaqguoxcmh80TtDhK75-lvpYxSAUeOqyqjTXvskj0d0uruAKvELbqnSUkEk9D2axmfvzhnhQrJX29xLCTHbaD1btq3zNnOvMNWe84g5PO45xI6qbHLKGODErHMCSl_ndrcc0Ni20jgDFsu_3k7iQoXXfJ5ziM9aIhfcNu4CP0Pxk3TsPrbr5RO3yXSF5_u8TwILmdWjQicLILJGHZ1AY3UjlrTiwtK1fQ4M0o-gqw7S26JmCyzpta-Rywmw8ngVrNpfTGp3C2Y_9ERUDm72qgvGkFfJ90EZu0MdSlc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران عزیزانشان را اینگونه بدرقه می‌کنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446029" target="_blank">📅 18:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446028">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL1l_B0tH-r1x-SEB5aofBNfi82r_JFa-4a_UHhE0r6ylW7uTKmNOefb4UXPGcTq1TrEGZvj_9UPJISd30nAKUk2bBZ1dGHsuqBI_rkoS1f1XMqimFN_Fb5BFk5e14pYXn6hhlrpbQOS_HTgMtwthaY5g7OcC4xdY3z1_hXnb6Iv2QrOXsYZCkwLOHbnlSvd4j-1acqw7VQBBmgJeTEnS50gbEAp7QtaKqBEPmDZiagWe1A08jN0oOK2yvvSRQ5sh-aDf2V9LZ2e6k1Auv92gA8oBVxuSfpqquubgO0Y06Ea2OVn8sx_FyQhwBx72Tg8DGIXz-iwrQ9DZ582Av4McA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام جاسوس و عامل شهادت فرمانده کل قسام
🔹
دستگاه‌های امنیتی نوار غزه از اجرای حکم اعدام جاسوس وابسته به رژیم صهیونیستی خبر دادند که در شهادت چندین فلسطینی از جمله فرمانده کل گردان‌های قسام دست داشته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446028" target="_blank">📅 17:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446027">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
جزئیات حضور مقامات عالی‌رتبۀ کشورها در مراسم ادای احترام و آیین وداع با پیکر رهبر شهید انقلاب
🔹
سخنگوی وزارت خارجه: از صبح جمعه ساعت ۸ صبح مراسم ادای احترام و آیین وداع با حضور تعداد زیادی از شخصیت‌ها و گروه‌های مردمی تا حدود ساعت ۱۲ ظهر برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/446027" target="_blank">📅 17:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446026">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a3266a08.mp4?token=qZp3p2_PAs7E6eAvsZcd13EwafJrxoUHpRVXDMweyLktQ-mHorvM60luNZgHqLanew3lC-YK9hVjywDpfQKxh0HZnsjEIcjjgQIkepkuHedoEG9Vt7UAcCyWa56UnpTzOI4b5Nqkl9SUIwc34J2J_01ruC5mXvpNFLfGJQzQ65vc3IWr8-WEZ4QSemMFEhtvH6JVTirb1R_ubhIZ9Tu-oysJ6HesCqoymHOMarqjguuS9GTOXdaTn3V-YDvAUsAapPgn0bSEBPbBB_q94Jb0OMlzQmst18SpUJCyc2bL3-RDRiz2JIen0M0uq4GQGmEAW9ZOmkPLy_q5DYEtS5rqmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a3266a08.mp4?token=qZp3p2_PAs7E6eAvsZcd13EwafJrxoUHpRVXDMweyLktQ-mHorvM60luNZgHqLanew3lC-YK9hVjywDpfQKxh0HZnsjEIcjjgQIkepkuHedoEG9Vt7UAcCyWa56UnpTzOI4b5Nqkl9SUIwc34J2J_01ruC5mXvpNFLfGJQzQ65vc3IWr8-WEZ4QSemMFEhtvH6JVTirb1R_ubhIZ9Tu-oysJ6HesCqoymHOMarqjguuS9GTOXdaTn3V-YDvAUsAapPgn0bSEBPbBB_q94Jb0OMlzQmst18SpUJCyc2bL3-RDRiz2JIen0M0uq4GQGmEAW9ZOmkPLy_q5DYEtS5rqmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار جوانی: شهید اکبرزاده زبان گویای نیروی دریایی سپاه در جنگ رمضان بود
🔹
معاون سیاسی سپاه: شهید محمد اکبرزاده در طول جنگ رمضان در شهرهای مختلف حضور پیدا می‌کرد و به تشریح پیروزی‌های رزمندگان می‌پرداخت.
🔹
حضور ایشان در آن مقطع، به‌ویژه برای نیروی دریایی…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446026" target="_blank">📅 17:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446020">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استان فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7-IbwsVEKW7axjvRhgNw8BkdZEv9omb86PGrJPUrQnGKXaP9UqFUsVGzGDhswI8G0nSRGdpXkEt1xnHLAMUb6A2Y07aIR4Lufsb6agYFd3F1lIGDM4YH4TWvXFHgOwItNBvdQCy2QGMdugPXOu34lQGMF56Va_gJIx8M0PLo3BKzWUf9ysgWmoaiAi1bllnPiZZEk_OYCokMmHJzDsBcgdbOpkYoQIAW_E7_yVgTIySipSay9YQzCoEZMj0TBDD19YjKFzyU-6ajrX5zodWSgR2tko3lD67kG4PxmQ9A1zp38gdWmDOND2G7cURjL7r8yt1FwpOJEKq3waoVIQsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fH3sEDaO5iqgLyFDhQk6EgdA2qHuPGDw-xEe43kfzUmkw4abyLSwje3IQNNXMU7VDZm-N-Rt9RR-GQh46bWbW37znZOAAfs_i9QviWeTEwmRlq-xO3dxsntCw7Vyjvpa3ZHoP-oD5IGSpCq5uX9wv64afo6MO31QSQxumoUfdpSZin9WeGcxmN1XUgwuZCh6jHAnXI1rfIZSku2qrW7foh5M08Yi8EtexEbv4TokUNhFSLItUbNHWdpfFLiog26tjeXhD2oG-9X-jASNEGdlrCkNNeAIalv0AvwA5qtKOfKN4_C7siJq5z-rce0rpI7jmIABJ5r0x5nXEgQ14r1X2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UkueUqTqk0fqQdYqyU7vrfNW_3yc_PqYCZ3UlpHop3Xwvfk7Ngco9A-FeIn7FGhm7rqMMyFZor93vUbSu98MLbhWliOb5YsWyO8ogxW7ddvhpFGJJP3MvjF9OIvQeFvz-WbYkzdKwL-gRS8ZLTNn6161qjqYWzRsa8Q0b98y4cYeqT4guBHJFuzrRT9wkmz-7K8cUbBLrI2Khp8mj0OjK_12Uw8C_kyc_cJHkMDirpz7ur-P2z4_Ao-to44byMDIeJTojIewvnTq87vkpwuMAcptLkej3PvbIZHq675Bc59kSB-Eoi5Hr2KQth0M6hX3fmQ77Q06MMMYiXQlj8YMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdX7HkGEMFpjzXd_raOIbS-5HvENliRrxhr4ijjahgdeirxkqWMcDojZcRZSPh00jmm0iq5pfmZREjih_yCaxsthlGBkMI3agOnK5I1N5jdxR3SVQC0T9Pw2_NczOsdkjnfiSl2yAQHq0vYYY_xepG7WvWeGEcWOyzU6SGrB_tvWcqAeqaXYVQo63NhW64jX_2AQ-bPAqChcpjeXET9xDAuQM9xyVmkl1FolADABa3913ej3QTwTGQX7OxZg1SytjG82erWLFDIMJj-jy3KRFGZoOqYEdH0trjhqDcvJoelrmv0MSLMyhnBiCuGx18tWIB_-oslt3WRZb7Yh69cOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aifnQ8pnha6Nk52oUUzdiV0qPriTHlKjmYh-W73IS9sKJ54znsYijhO-Cyiq4oBUBNug1SCXZWaCW_k4Qb12VsKWeOZhk4vGo9gPwZaoQtR2TuhGPrgdCEcbeaRWoRNxYCGJfF_U3qJ9zK2vsK4d-lNiPjqwRckbcmcUXWs4UCqqK8aZ2bcWAo_CMNaWYSVcNYoCt_uzRFFrE_kF0lLUoe-rIP4usMFce0glSVzL3aZLZIZSnZFCdCd6kUgdKYhP-KnF4bB8GlIHgCBsWO-BQ_mGCVVlVV04Hu5knbDUrjhAxQ_teZAPJnja2El-pZIE5tkJkTIXjyFlcBJpwkmPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APh4rdg1VPXC25FUWqfRy8iPi8t37KZ54lYH1hsdcYb3_CNBmA-HxQ9moHDzJurZUIX_FXCGljYL2Q7Z2uwME6yAhKgrO8O1hXr67sEWjsnufAgduLBQB5sxE7V44LsRNLmTBlQdrnlOVJ23AWAPl5ul2d_92HqTw8jYvEN9sbH0bzcvlIC3o2DwusxSyuEjfvET48Zzjnu40XSe8plHFYqfC6_bwQkgGyYjEyVgpTcUb2mNfD3EcqC4GF85Ok8JgTF7x2zt-zl7slyrHx7DIxVofJ6MtSwNKteJx-Vaqeac_iY0ABDHAQUEZ9teaHfzA7RoD8HmepVDBiD7BIRSpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌ها هنوز آن سفر به شیراز را روایت می‌کنند
🔹
در آستانه وداع تاریخی ایران اسلامی با قائد شهید امت، هنوز قاب‌های ماندگار سفر شهید امت در اردیبهشت ۱۳٨۷ به شیراز در تاریخ این سرزمین به نقش بسته است.
عکس:
دریافتی
@farsnews_fars</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/446020" target="_blank">📅 17:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446019">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed06b2f9d.mp4?token=J2NVrjnykMjGX7N4ej_F6-GpbHIqShc4bZ104nq4a3dZxZdZDy8gu9eSPrlE3E1Ir90ncSR2l3KD48BuLteAsBHnotwssCr5sGaRTuW_GhnHQOvEU3xYqszgkn2SD74Nit_82WjYKRZvWlgMnrBf8940jAGw38eR8gLmQpLoC7fOjlIQ3H4BGfCXqZdESQINrvHynrpgZuFpQjmxsmJvP_WLtjaW3TVUxYYWlKrJQEDKGAkhwwJq6Mva0nFJtZXYRjWT4Bv7RSFyczr6mhxObHTMQtpI1foskKWD5m5OPxAUOZ02nPGYD-kdRGOwbjUsoB4vWBNcUHmkApSZUyA7XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed06b2f9d.mp4?token=J2NVrjnykMjGX7N4ej_F6-GpbHIqShc4bZ104nq4a3dZxZdZDy8gu9eSPrlE3E1Ir90ncSR2l3KD48BuLteAsBHnotwssCr5sGaRTuW_GhnHQOvEU3xYqszgkn2SD74Nit_82WjYKRZvWlgMnrBf8940jAGw38eR8gLmQpLoC7fOjlIQ3H4BGfCXqZdESQINrvHynrpgZuFpQjmxsmJvP_WLtjaW3TVUxYYWlKrJQEDKGAkhwwJq6Mva0nFJtZXYRjWT4Bv7RSFyczr6mhxObHTMQtpI1foskKWD5m5OPxAUOZ02nPGYD-kdRGOwbjUsoB4vWBNcUHmkApSZUyA7XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعر افشین علاء در وصف امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/446019" target="_blank">📅 17:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446018">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Apzle_vVDVZm0vs1YWksS1CULuAeVuiWaSeCBbbP4WAapre0BxlYTSLFRXHeq0vpCp2x6-vFRETcwXXI55b5xSAtPLnnY7P_6Z_JLiWT-RlpL6tK9WkRlFjacyvOZ1PlyXxT9qa4fn8WNpDd1s_8QsL-TYs0xUwbndes0__eOgeMoNpZyNyGHKAp3sBtpe6cmYrtEA6PCG1dvmyS20dALv-L0ia6E3UCGEtydiQxeyPJw5B57P5Jp6fAIp4GxbtxE2lF21a7Nclnaz1Dj23Axi0M8JVynF4yiCuKuTAIRL82TuX3DYDACRA6KQfeuuK0_AxrbqS1zVipKahWm2Ncmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت بدرقه با شما
🔹
کشور در آستانۀ یکی از متفاوت‌ترین و پرجمعیت‌ترین مراسم‌های تشییع قرار دارد. دل‌های بی‌قرار، شهرهایی که آرام‌آرام رنگ و بوی بدرقه گرفته‌اند و تهرانی که خود را برای میزبانی از خیل عزاداران آماده می‌کند.
🔹
این روزها در شهر شما چه حال‌وهوایی حاکم است؟ اگر میزبان هستید، برای پذیرایی از مهمانان چه تمهیداتی اندیشیده‌اید؟ و اگر راهی تهران هستید، از آمادگی برای این سفر، تصاویر کاروان‌ها و حال‌وهوای شهر خود برای ما بنویسید و عکس‌های خود را با دیگر مخاطبان فارس به اشتراک بگذارید.
🔹
شما می‌توانید روایت‌ها، تصاویر و ویدئوهای خود را با هشتگ
#روایت_بدرقه
در فارس تعاملی منتشر کنید، از طریق پیام‌رسان‌ها به نشانی‌های
@Interactive_Fars
و
@fars_ma
ارسال نمایید یا در پایگاه اینترنتی
https://revayat-badraghe.khamenei.ir
ثبت و بارگذاری کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/446018" target="_blank">📅 16:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446017">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">درگیری عوامل انتظامی با تیم سارق مسلح در زاهدان
🔹
فرماندهی انتظامی سیستان‌وبلوچستان: لحظاتی قبل، عوامل انتظامی با یک تیم سارق مسلح در خیابان بزرگمهر وجانبازان زاهدان درگیر شدند.
🔹
در این درگیری مسلحانه ۳ سارق مسلح به هلاکت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/446017" target="_blank">📅 16:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446016">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
انفجار در دمشق
🔹
رسانه‌های سوریه از زخمی شدن تعدادی در پی انفجار داخل یک کافه در پایتخت این کشور دمشق خبر داده‌اند.
🔹
خبرگزاری رسمی سانا گزارش داد که انفجار در منطقه حجاز دمشق رخ داده و ماهیت آن در دست بررسی است.
🔹
تلویزیون سوریه: این انفجار در منطقه حجاز…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446016" target="_blank">📅 16:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446015">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRvEqwcNmHnCOyOC9A-t02-jSEkaieooYBZO96PCk_7jp6lHD_KcYUUHqzHeexbBVVqTFa2mXle8kX9md8alclQmvah3CufLLyhPmMyXhtD5JDFe0TKDXXfqkqbiuDv9xrTQcHjn191OsfJI7yC2V5VaiXBxasbBDWi7S-0RQ8Q2zoMmLg3mZh1_aGejH1H4ZrsnZdNjLhRDYhZ-i4TyGMNNnxdSOFYcpk-H-ktDjiM0lA2eCXheEtb7maQ8nv6fzqcLQUN_1mr842Q5teEBZGb9xQr1ncb8Jk1xJnvqptoN3JSBpvi5te-gDNSizpt6xL4S9MTITaARlWYI_bHyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جلسۀ ستاد برگزاری آیین تشییع رهبر شهید انقلاب به ریاست رئیس‌جمهور  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446015" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446014">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e2e685bf.mp4?token=gEhs4Efj5bl-xiyZY3dL3pgmojxmKocG1rHgmolItnljxykcB_yG1vToRmUY-I-oBiGQT8cnJyXUxkh_IQ7IVDkCr1mQn15u8hNOTmAzJAzfjoXdG4gg3WwpYq3QTlxH87nLm7cqNUHRsnKkz1P-mQokuOpgY1p4qIm7ILBD1fz2ZRp7c8B5BvRI46fQJlIrFQ3XAsctqL1D0JmNLGCvdc-S6r2TrekgekSKOJtRKoBSMTBcXt1nPw36ygFFBZfS00Q8NexiZo9ecDn6vygRTmHBi0HTwbecHDg9J3ZpclC9Nhba4urDRCmgLr915Qqhz4XoO8_voc1CBnMn8d4pDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e2e685bf.mp4?token=gEhs4Efj5bl-xiyZY3dL3pgmojxmKocG1rHgmolItnljxykcB_yG1vToRmUY-I-oBiGQT8cnJyXUxkh_IQ7IVDkCr1mQn15u8hNOTmAzJAzfjoXdG4gg3WwpYq3QTlxH87nLm7cqNUHRsnKkz1P-mQokuOpgY1p4qIm7ILBD1fz2ZRp7c8B5BvRI46fQJlIrFQ3XAsctqL1D0JmNLGCvdc-S6r2TrekgekSKOJtRKoBSMTBcXt1nPw36ygFFBZfS00Q8NexiZo9ecDn6vygRTmHBi0HTwbecHDg9J3ZpclC9Nhba4urDRCmgLr915Qqhz4XoO8_voc1CBnMn8d4pDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده سپاه تهران: آماده‌سازی خودروی حامل پیکر مطهر رهبر شهید به پایان رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/446014" target="_blank">📅 16:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446013">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">استقرار ۴ بیمارستان سیار نیروی زمینی سپاه برای خدمت به زائران رهبر شهید
🔹
معاون بهداری رزمی نیروی زمینی سپاه پاسداران در گفت‌وگو با فارس: چهار بیمارستان صحرایی تخصصی در شهرهای تهران، قم و مشهد مستقر شده است.
🔹
دو بیمارستان صحرایی ۲۸ تختخوابی در تهران و قم و دو بیمارستان صحرایی ۶۴ تختخوابی در مشهد مستقر شده‌اند. همچنین ۲۵ پست امداد سیار و ۴۰ دستگاه آمبولانس نیز در کنار این بیمارستان‌ها برای ارائه خدمات درمانی و امدادی فعالیت می‌کنند.
🔹
بیمارستان‌های صحرایی مستقر، از تمامی بخش‌های تخصصی و فوق‌تخصصی شامل بخش‌های بستری، CCU، ICU، اتاق عمل، رادیولوژی و کادر درمانی مجرب برخوردار بوده و تمامی تجهیزات مورد نیاز را به همراه دارند.
جزئیات فعالیت‌ها و خدمات را
اینجا
بخوانید.
@Farspolitics</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/446013" target="_blank">📅 16:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446012">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b5a61604.mp4?token=PgdX-KEKUK4kQGzkcG9tO0EvTjKB4iJWAQECfp-dmWh9eEylnUBIUPrVnKfB8D0DOWH4ItnHB1h03L7YCSSv2tn686DCDBHUonP2nuZDYurHWB1wsN0pO0FuaCCgFR05AaxllCJ7lQNONasxkoaZ0qvB-x939_0qZ5E4cKMjSwK_qWqoavAN2958Oo77fWb1nntVP92ZX5LqEwIPZiB6jDPaA_yOfJv_hQmsyPLil85l9j-JFiPtUAID1AozmeowG7cfYSVAjGoTypxkYcoFLIG8Ufywf8-weM6-yYVIvr30VjUB5Bk_ZnEt37zi2VWmOlDvB1XdhmcbOob1FkdRcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b5a61604.mp4?token=PgdX-KEKUK4kQGzkcG9tO0EvTjKB4iJWAQECfp-dmWh9eEylnUBIUPrVnKfB8D0DOWH4ItnHB1h03L7YCSSv2tn686DCDBHUonP2nuZDYurHWB1wsN0pO0FuaCCgFR05AaxllCJ7lQNONasxkoaZ0qvB-x939_0qZ5E4cKMjSwK_qWqoavAN2958Oo77fWb1nntVP92ZX5LqEwIPZiB6jDPaA_yOfJv_hQmsyPLil85l9j-JFiPtUAID1AozmeowG7cfYSVAjGoTypxkYcoFLIG8Ufywf8-weM6-yYVIvr30VjUB5Bk_ZnEt37zi2VWmOlDvB1XdhmcbOob1FkdRcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش‌وپرورش: امتحانات نهایی به‌هیچ‌وجه به تعویق نمی‌افتد
🔹
رئیس مرکز ارزشیابی آموزش کشور در برنامه پرچمدار: آزمون‌های نهایی طبق برنامه برگزار می‌شود.
🔹
امکان برگزاری آزمون‌های نهایی پس از کنکور وجود ندارد.
🔹
در نیمه اول شهریور نتیجه امتحانات نهایی به سازمان…</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/446012" target="_blank">📅 16:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446011">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=DjaWSo3AyL7eRQltpAOS4ZEGZOivdwUIbh3uonBX4RCRcC4ZspWNi_gRj-2A4tyQNMTQnWnT1qVPvTQu2JMWF8j8lSI7QXeTY1Wu8bpiunWdaNiopWW7B49Pej6OITRvgfnRHaBiUkjACXqX03A6Z8V4jYwUvj1vxF9tdlr_3vdeqH8AdyyPt-_UOXnlUm_w1gQPlcKCL3OO1TonFjPOkZnqhrj34gd1lniBd-96OLZiLq2BwHkOR0931M-V9DUSO4qASoz9_B2kBsCjAxGsZoPmz0Ch2PCNnsTo8ULoLBs3XDtUY5LDpVSrwmYdaU-ih5_74wvOsOfQx19FkJY17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=DjaWSo3AyL7eRQltpAOS4ZEGZOivdwUIbh3uonBX4RCRcC4ZspWNi_gRj-2A4tyQNMTQnWnT1qVPvTQu2JMWF8j8lSI7QXeTY1Wu8bpiunWdaNiopWW7B49Pej6OITRvgfnRHaBiUkjACXqX03A6Z8V4jYwUvj1vxF9tdlr_3vdeqH8AdyyPt-_UOXnlUm_w1gQPlcKCL3OO1TonFjPOkZnqhrj34gd1lniBd-96OLZiLq2BwHkOR0931M-V9DUSO4qASoz9_B2kBsCjAxGsZoPmz0Ch2PCNnsTo8ULoLBs3XDtUY5LDpVSrwmYdaU-ih5_74wvOsOfQx19FkJY17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاعیهٔ جدید آموزش‌وپرورش: برنامهٔ برگزاری امتحانات نهایی بدون هیچ‌گونه تغییر اجرا می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/446011" target="_blank">📅 16:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446010">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دعوت فرمانده کل ارتش از عموم ملت ایران برای حضور در مراسم بدرقۀ پیکر مطهر فرمانده شهید کل قوا
🔹
ملت شریف، پرافتخار و داغ دیده ایران؛ شهادت قائد ملت، امام امت و فرمانده مجاهد و معظم  انقلاب اسلامی، حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای، (رضوان الله تعالی علیه)، آن بزرگمرد صبر و مقاومت، به دست دشمنان کینه‌توز، آمریکای جنایتکار و رژیم غاصب صهیونیستی، داغی عظیم بر قلب ملت ایران، مسلمانان جهان و آزادگان عالم گذاشت. دشمنان قسم خورده ملت ایران، در اوج خباثت، گمان می‌بردند با این جنایت می‌توانند اراده ملت بزرگ ایران را در هم بشکنند و روح مقاومت را از این سرزمین جدا کنند اما نه تنها به هیچ‌یک از اهداف شوم خود دست نیافتند، بلکه ملتی مصمم‌تر و متحدتر از گذشته را در برابر خویش یافتند.
🔹
رهبر شهید وفرمانده معظم کل قوا، در تمامی سال‌های پرافتخار حیات خویش، الگویی کامل از شجاعت، بصیرت و پایمردی در برابر زیاده‌خواهی استکبار جهانی را به کلیه آزادگان عالم ارائه داد. آن مجاهد بزرگ تا واپسین لحظات عمر پربرکت خود، خط مقاومت را با شجاعت و بصیرت پاسداری کرد و هرگز در برابر تهدیدها و فشارهای دشمنان، از راه حق کوتاه نیامد تا میراثی گران‌بها از ایستادگی و مقاومت، به جای بگذارد، میراثی برای همه ملل آزاده جهان که هرگز فراموش نخواهد شد.
🔹
اینک بر ماست که با حضوری باشکوه، متحد و آگاهانه در مراسم وداع و تشییع پیکر مطهر آن رهبر شهید، پیمان دیرینه خویش را با راه ایشان و آرمان‌های انقلاب شکوهمند اسلامی، تجدید کنیم. این حضور، پیامی روشن به دشمنان دارد و به استکبار جهانی، یادآوری می کند که راه آن رهبر و فرمانده شهید، با اراده فولادین ملت ایران و در سایه رهبری خردمندانه جانشین شایسته ایشان، حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، با قدرت ادامه خواهد یافت.
🔹
اینجانب، به نمایندگی از کلیه همرزمان خویش در ارتش سرافراز و مقتدر جمهوری اسلامی ایران، از عموم مردم شریف، خانواده‌های معزز شهدا، رزمندگان و همه دلدادگان مکتب مقاومت دعوت می‌کنم، با حضوری حماسی و تاریخ‌ساز، قائد شهید ملت و همراهان شهیدش را بدرقه کنند و بار دیگر به جهانیان نشان دهند که ملت ایران، در برابر دشمنان تسلیم نخواهد شد و تا آخر ایستاده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/446010" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446009">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzPwQUDxeW84w8hl_24U-V6rznYD98HSMgQFcrfPkr6JAdFu4sVoBpJt0XDNOq1hxK0HlV8KZb6OX4qMTgseEgHN5Enq5s1ZwCahfc3Bv71MW6xSp9uqAZZfyXCXiNV8-3tk9gVR67vo05uhX2RyDn1t557j0BQ4pj86BvHYeVWkuCRhRkumtI94C-fqhnriE1KrcXI4qtNVWnWs6LcWTUy7ylipgrUxsBnmXNz2SFjvB9d25rB4DZDxMJVL_Nhg6z4JEnnWnOafb5txINCgfOxcxexMw3fDMhTWK6sbfrzvBm-fJmi6QUcwYurvPbpByoOcJdIw5oS2LapBCKms9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرنگی‌کاران جوان ایران قهرمان آسیا شدند
🔹
تیم ملی کشتی فرنگی جوانان ایران عنوان قهرمانی زودهنگام رقابت های آسیایی تایلند را از آن خود کرد.
🔹
در جریان رقابت‌های ۵ وزن نخست کشتی فرنگی قهرمانی آسیا در تایلند، نمایندگان ایران صاحب ۳ مدال طلا و ۲ برنز شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/446009" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446008">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89260fdff2.mp4?token=MAJx9EIPEI0BYRGMvCyCUrvOScCZVJgUO4vxNyo4u6_Ii7NiUwfwLhKBYrnKehj2gFMDlCft_BTbnWJBGGudgQdvSXn68r7sVbpNJ3VlCSmGiVKV2f1KxEZk9vLimWm2hKgbT4b25v4cU8ggNe76u1WQiST1h6mSPHCg3tQJymZTLZdXuj0MpYlUFjSqgdfrRAJScmVoKkgoUTnXYXewjh6gRTj2_sotrsMpdh6gHx8xiWf67XtmThNDsfjUlsh_P-7Ym1oIsXODWs7-hVPmKsynVy26fkjU-zuglFczHw-qx_4N75SULqi3hfgC7tnmtSF8l4RjJskvw_whnLxSaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89260fdff2.mp4?token=MAJx9EIPEI0BYRGMvCyCUrvOScCZVJgUO4vxNyo4u6_Ii7NiUwfwLhKBYrnKehj2gFMDlCft_BTbnWJBGGudgQdvSXn68r7sVbpNJ3VlCSmGiVKV2f1KxEZk9vLimWm2hKgbT4b25v4cU8ggNe76u1WQiST1h6mSPHCg3tQJymZTLZdXuj0MpYlUFjSqgdfrRAJScmVoKkgoUTnXYXewjh6gRTj2_sotrsMpdh6gHx8xiWf67XtmThNDsfjUlsh_P-7Ym1oIsXODWs7-hVPmKsynVy26fkjU-zuglFczHw-qx_4N75SULqi3hfgC7tnmtSF8l4RjJskvw_whnLxSaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انفجار در دمشق
🔹
رسانه‌های سوریه از زخمی شدن تعدادی در پی انفجار داخل یک کافه در پایتخت این کشور دمشق خبر داده‌اند.
🔹
خبرگزاری رسمی سانا گزارش داد که انفجار در منطقه حجاز دمشق رخ داده و ماهیت آن در دست بررسی است.
🔹
تلویزیون سوریه: این انفجار در منطقه حجاز دمشق در نزدیکی کاخ دادگستری  رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/446008" target="_blank">📅 15:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446007">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اطلاعیۀ قرارگاه برگزاری آیین وداع و تشییع رهبر شهید انقلاب در تهران
🔹
۱. حضور وفاداران به آرمان‌های انقلاب اسلامی‌ و ولی امر شهیدمان در مراسم وداع و تشییع بی‌شک بزرگ‌ترین اجتماع تاریخ بشری را رقم خواهد زد که چشم جهانیان را خیره کرده و موجب تسلای قلب حضرت ولیعصر خواهد بود.
🔹
۲. خادمان شما در همۀ سازمان‌ها و رده‌های مختلف‌ نهایت تلاش و آمادگی خود را به‌کار بستند تا بستر مناسب برای حضور زائران گرامی ‌را در مراسم وداع، برگزاری نماز و تشییع رهبر شهید انقلاب آماده شود و چندین شبانه‌روز است که همه امکانات لازم برای این امر بسیج شده است.
🔹
۳. هموطنان عزیز تا حد امکان برنامه سفر خود به تهران را به گونه‌ای مدیریت کنند که از حداکثر ظرفیت اسکان و ارائه خدمات به زائرین در تهران استفاده شود به عنوان مثال سفر را کوتاه کنند تا تعداد بیشتری از مشتاقان شرکت در مراسم بتوانند حضور پیدا کنند.
🔹
۴. مبادی و جاده‌های ورودی به پایتخت همواره باز است و هیچ‌گونه منعی برای ورود وجود ندارد.
🔹
۵. زائران گرامی ‌اخبار و اطلاعیه‌ها را از مراجع رسمی‌پیگیری کنند و به‌ویژه مراقب شایعات و اخبار جعلی باشند.
🔹
۶. پیش‌بینی و توجه به محدودیت‌های ترافیکی در سطح شهر تهران و حفظ آرامش در هنگام حرکت همواره توصیه می‌شود تا برنامه‌ریزی حضور هم وطنان دچار اختلال نگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/446007" target="_blank">📅 15:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446006">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd8fcf393.mp4?token=ao3PW5REuC8nvyL9kV-ds4t9I2SAlAbnmmwrS-p1qYM3I2crnBvA8CfxiDKW6vo2vm5JjjS4qS7J6Kpnboi7H6nXDPRpiz9TCGF6BSjoIS9QyVxrR9x6Ls5hFtl0Hm4baJ3xBPGKUSxt_gvcGdZWbUGTAX0nUTmlGUmYkoMAkIw-7OhR_sLdQVk7Vlc0tmy-6FSLH37v4kkd-CW15j23Rx-cGwHTQAiZqGGPdfC7uV1--TKxBRuzGzNUGi1gJjJkSw3RtQsmnjp6cy5njCR1bXLSOyOdCr6dl3YM58KmjHYzJLmvL0coZZhjCfqjU8wM9IE1F7SNVra4AR8v1EcSF31tajRl6WpSOt__ZDJPNM7rISHi2AFqokOZRBSilTCePQTxYXjl8wtJeYOsSdw1sQV49PWf_gfqxFdlAM-lYhgHUZOH4VtgSSU28DZTjbJR4mcxhhVrXF-rQGf3mOmyN2K8b5C8qClGhH49Vl4hJvCUEEqCz9QPxJyy_lemQS27qSi9dCFzf4yeR2rmvbNFjKGUQH6wQHhaIhkG0mazFYZflLkYg8r_Cv90ZMhlBKz_vwajCM_bk-XwAPLCiRwHqOIEui93GJa2Qiq-JuACaT571BtoI6EhPc05SKjyi7R2qjyJJGikplF54Fc_5YS9-7PSd748PSLNMzp6abVdZY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd8fcf393.mp4?token=ao3PW5REuC8nvyL9kV-ds4t9I2SAlAbnmmwrS-p1qYM3I2crnBvA8CfxiDKW6vo2vm5JjjS4qS7J6Kpnboi7H6nXDPRpiz9TCGF6BSjoIS9QyVxrR9x6Ls5hFtl0Hm4baJ3xBPGKUSxt_gvcGdZWbUGTAX0nUTmlGUmYkoMAkIw-7OhR_sLdQVk7Vlc0tmy-6FSLH37v4kkd-CW15j23Rx-cGwHTQAiZqGGPdfC7uV1--TKxBRuzGzNUGi1gJjJkSw3RtQsmnjp6cy5njCR1bXLSOyOdCr6dl3YM58KmjHYzJLmvL0coZZhjCfqjU8wM9IE1F7SNVra4AR8v1EcSF31tajRl6WpSOt__ZDJPNM7rISHi2AFqokOZRBSilTCePQTxYXjl8wtJeYOsSdw1sQV49PWf_gfqxFdlAM-lYhgHUZOH4VtgSSU28DZTjbJR4mcxhhVrXF-rQGf3mOmyN2K8b5C8qClGhH49Vl4hJvCUEEqCz9QPxJyy_lemQS27qSi9dCFzf4yeR2rmvbNFjKGUQH6wQHhaIhkG0mazFYZflLkYg8r_Cv90ZMhlBKz_vwajCM_bk-XwAPLCiRwHqOIEui93GJa2Qiq-JuACaT571BtoI6EhPc05SKjyi7R2qjyJJGikplF54Fc_5YS9-7PSd748PSLNMzp6abVdZY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«دکتر ترامپ» برای منتقدانش نسخه پیچید
🔹
رئیس‌جمهور آمریکا در شیرین‌کاری جدید خود با هوش مصنوعی، این بار در نقش پزشکی ظاهر شد که منتقدان سرشناسش را درمان می‌کند.
🔹
این ویدئوی حدود ۹۰ ثانیه‌ای که در حساب کاربری ترامپ در شبکه اجتماعی «تروث سوشال» منتشر شد، شامل اظهارات ساختگی منتسب به شماری از چهره‌های سرشناس رسانه‌ای و هالیوودی است که از منتقدان ترامپ به شمار می‌روند.
🔹
ویدئو با تصویری از ترامپ آغاز می‌شود که با لباس پزشک از مخاطبان می‌پرسد «آیا شما یا یکی از اطرافیانتان به سندرم ترامپ‌هراسی مبتلا شده‌اید؟» سپس می‌گوید «علائم این بیماری می‌تواند بی‌وقفه ادامه داشته باشد. خوشبختانه، من دکتر ترامپ هستم و برای آن یک برنامه درمانی دارم».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446006" target="_blank">📅 15:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446002">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nm4hM1_DYSx5sTYZjAHFZQjIHvIQPMBZ9OEwOTF4c9K_C51g1SYuBWme-w0jBLDcTGTpK9QewDxhn2n7G33W5fyh6uYme17VKJK3DkKZf_hmOcWM8cH2Se-pfYJDEqpJE62n8xh8QTH4MAGOdwkGHjBevjVFmCVX4DHU3zdts6tQ_R0mn6KGIjuTnz5-JcHvrKRwiYEqHHw7ZQpXlJLSeh1nPvvVhplTAAyfYmdhEjwNMFHIU8_jhn5nWzz-PnVrmH8tfMwWC_MN--qmLGO7ja1TzfzGEsFJbd4JLV3E_PdSqL3Bo8pvezauIXf38kX3rYTuDALf3d1g53s-o3mtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Znpuwv-0aaSm2W5t43QcdJjhEW18weltkGeYKJr6K4mocJcZzLjWJ15yzygR2NxyGyyLfjYVuHa-C-H166hdr3uuXmywIXZjspjwdl91kv2Vc2x8DMeP0QNwiNbbHsAwGwdj606heuI4gb24l_Oa66dIqz23ZZYJEGnkddFLDccGEP3K0n5QNvBGMwVQGK80eFUIUcfbCt1mAZMO_muJV7-asb3NZ3qj38GSqpzMcJYhPi6oQh7kembJ0C-gXyVB0Wu5zyk4FcQM8HHTHh85NBmssq0VqMSrUpxoQO2w1ob6bkzHctOyKI3py0O4RLxYRGEwz8VrI9mmcGIgV2n6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PclGfc4LlEBV51ZkqXwwXMbU01whcIzVHCe01nhRmWIoRGUbRSAmlOXRx6GcAlL1iDO0Mkrt3dMoEVFthxDS_xEEt0Ggr8sDRzyyREwyPc7VaVZoRn7o_I0UDI-wPJ7aCz4hG5gA3zxl7PGStHu9F_trXg6yGolvIboiMBSJVQxBFUy4fr70_0KILFojSkvYVlknT1sNho0fPBTComTMX1DXFPxttVeghia__McpU2lZcelEnAD-EoEl_t8XnL9RSlHayr1UHZFZ3sD1bSilUU3v8U1DK1PJp-w3R6jp-NVMeUbJpJdc9qfV8dBdooBe-YHdLn2eV51V6spGWlAPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRlwYWWsQ6Sq5jRYnZZFpJJh6nuUP5Ik8blW-OuNMBc9UMgkBHeKxBhAYtQUGPdUrFi4WRDL2o2t8B4GYeEhFcdz9gE21vZCkSTJxRvXS4QQHw5Bb9OXSo6Leqz6AEXAOSk_QO7oI7oM30io0uKoJ69FoHAvC3fxHLV9Ih3qAn4eQdOrwkfYe7pgzsc8wSvEjkBtRvM_VD064QnWUGZgDLAfyc4nd_R86jUTJD-Irl4m27MKWb8gvNI41LajNdRY3sJvIpCs0FECo7yQYJGiB_evF5YJWYy6GdfSGfJcZFHraWlN5S-mrWRDmeOZDfs9q1m7BYsQ2PLxJx-QK0oiDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلسۀ ستاد برگزاری آیین تشییع رهبر شهید انقلاب به ریاست رئیس‌جمهور
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/446002" target="_blank">📅 15:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446001">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3zU1RDhXojuv6LYrRTy15xBrf-RnV_-Ym6eA_bhuy5OL2PmzhgqNBE_GxYcDdHfDXjBWsFf0PamhAyL4eacEhKWhMl5NiHCbrxSb-NrGq_CcQrqorCKzEaX0xJhJ1CgwJktyvAbm95KwPHIwKKgdLadcc_hnkc7jGjVGAI-8oeYeaQ6JeKnOgPlWHRv-vxVOtKfBqv18Vt0s57qLpOSQHxVOzZVb9jnUoc-rq6Zz3n7mlrxt1AEUs46OrV_NK9mbzD-26XnrBzHxIWEYSSak-Vzur97oH9FvsseoG0zJ1DwFv0GqUqEbaoz3mK4hU_Gy_hHBrawKtYraZbmpK1a3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه راهنمای زائرشهر چهل‌سرا در جنوب مصلا
برای مراسم وداع با رهبر شهید انقلاب
🔸️
استقرار مواکب پذیرایی، بیمارستان و آزمایشگاه سیار برکت در زائرشهر چهل‌سرا در ضلع جنوبی مصلا و خیابان بهشتی
🔸️
تماس با سامانه تلفنی ۴۰۳۰ برای راهنمای مسیر، مراکز اسکان، درمان، ستاد گمشدگان و مشاوره روانشناسی
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446001" target="_blank">📅 15:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXDzF4yxJ4bA0cPgEHkbLFumRlHfxdo6cKaJpBI5HqsA0YW0NaLUdHflbC25ZH3vDV-ewdYrKYFJGgGRitE0TS7vW7CW1Xm5eYx1DeB4PPD00mJ1ig7PfjxVf642lSlNC3JU04qAUwOIKT9GbVJUZYgZAdbpQQY4RKFfHMefRgj-B5ftZ_4buJlAM56hkR2PGSlPn6eVFMko2Rv3U9Fn0kbleZ-z76bcDUQiTSij01hvBz646-MqhIeyjcdOMC4W8md2O0aLy8TafIkvUQ7gJui6GHzF-oox7c8osLQ7VopHPl3ngjG8DBzQ8TVkogYZaLFqDy3T10qx4cJnoHFCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/446000" target="_blank">📅 15:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/445999" target="_blank">📅 14:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تکذیب قطعی اینترنت در روزهای مراسم تشییع رهبر شهید
🔹
استاندار تهران: شایعات اعمال محدودیت اینترنت در روزهای مراسم صحت ندارد؛ بلکه زیرساخت‌های ارتباطی با استقرار سایت‌های سیار اپراتورها به‌شدت تقویت شده است.
🔹
همچنین ظرفیت شبکه‌های آب و برق مصلای تهران به شکل قابل‌توجهی افزایش یافته و کاملاً پایدار است.
🔹
علاوه‌بر مدارس و اماکنی نظیر ورزشگاه آزادی، ۷۰۰ مسجد مجهز به برق اضطراری و مخازن آب، آماده اسکان ۵۰۰ تا ۶۰۰ هزار زائر هستند.
🔹
در صورت نیاز، بیش از ۱۵۰ نقطه در پارک‌های بزرگ تهران (مانند چیتگر) برای برپایی کمپ‌های موقت و اردوگاه در نظر گرفته شده است.
🔹
تیم‌های درمانی و بیمارستان‌های صحرایی در نقاط مختلف پایتخت مستقر شده‌اند و خدمات‌رسانی از مبدأ تا بازگشت زائران ادامه دارد.
🔹
عملیات بی‌سابقۀ حمل‌ونقل با ۱۱ هزار اتوبوس برای جابه‌جایی زائران در نظر گرفته شده است.
🔹
در حلقۀ نخست اطراف مصلی تردد هرگونه خودرو و موتورسیکلت ممنوع است و زائران باید پیاده تردد کنند. پارکینگ‌های بزرگ نیز در ۱۴ مبدأ ورودی شهر آمادۀ استقرار خودروهای شخصی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445998" target="_blank">📅 14:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445997">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95167edba5.mp4?token=FxGX_NIl_um4CFJ5OIM3Zkx0__4by10CiEGSMocHZWtXb8tO8h7QJnyOFdwjjzXf8nkV0cgEIjsrcbZdW6-9T7hU5GWjx0MvQjv_LK2dlF9hMgDRXDplE4W-ydQrHIB_9jJGR833fz3WK-_b_Y1g8ER-HhUQijMB_nWCNMv4ZdYMvMAWCxnM0pbQWGC35kSvdfaT_bmYjskesUSpO1JRUEac4TecxaA4lsiJmYyFHD23PHVlbEz2Wj6CRcEoQ8qA8UALg6zwwzq7JQS4GpK6_oDeysMVHelR9FW1gcPJHKGT1ZinA1iG6u-Y9PT6O9purWB3Pq7izMTtpXi2BhZx-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95167edba5.mp4?token=FxGX_NIl_um4CFJ5OIM3Zkx0__4by10CiEGSMocHZWtXb8tO8h7QJnyOFdwjjzXf8nkV0cgEIjsrcbZdW6-9T7hU5GWjx0MvQjv_LK2dlF9hMgDRXDplE4W-ydQrHIB_9jJGR833fz3WK-_b_Y1g8ER-HhUQijMB_nWCNMv4ZdYMvMAWCxnM0pbQWGC35kSvdfaT_bmYjskesUSpO1JRUEac4TecxaA4lsiJmYyFHD23PHVlbEz2Wj6CRcEoQ8qA8UALg6zwwzq7JQS4GpK6_oDeysMVHelR9FW1gcPJHKGT1ZinA1iG6u-Y9PT6O9purWB3Pq7izMTtpXi2BhZx-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی آمادۀ میزبانی عاشقان آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/445997" target="_blank">📅 14:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445996">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار خراسان رضوی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4806cf0329.mp4?token=vA21-g5DqregFjP_amD_D4lUUrvI0XvlLyy0fuQSvGGJbutKHzzfJHAME_Pn7fz-KxjiLar812Bv5dRg6RPsj0u7kpX0qpXtLz4zjpf95TJCpXXqjzEmtdOpnlf8T4xjmD2GSFq0JK9JYipFR7Rfiy-h8zClRTvFMFOuulBw4K3F2PceefE4OUKaF-OO56WRuEiEt74mNIWmrTAxUXmDYv9Royu_ctn60r-4sbkZ2TxchTaitCWPBo86T9JUeSjNzmm8-Mxl6MpuAKPwJiuJvhUICB2wwAebd6bwwCAFsdtF_kY74UZj7kbleEcQ5c344ZYpQgB-XQPRbTBVXWLaOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4806cf0329.mp4?token=vA21-g5DqregFjP_amD_D4lUUrvI0XvlLyy0fuQSvGGJbutKHzzfJHAME_Pn7fz-KxjiLar812Bv5dRg6RPsj0u7kpX0qpXtLz4zjpf95TJCpXXqjzEmtdOpnlf8T4xjmD2GSFq0JK9JYipFR7Rfiy-h8zClRTvFMFOuulBw4K3F2PceefE4OUKaF-OO56WRuEiEt74mNIWmrTAxUXmDYv9Royu_ctn60r-4sbkZ2TxchTaitCWPBo86T9JUeSjNzmm8-Mxl6MpuAKPwJiuJvhUICB2wwAebd6bwwCAFsdtF_kY74UZj7kbleEcQ5c344ZYpQgB-XQPRbTBVXWLaOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم رضوی در ایام تشییع رهبر شهید محدودیت تردد دارد
@FarsRazavi
‌-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/445996" target="_blank">📅 14:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445995">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFfrg2OALQbaOYS0tXiv752YqQTUtoYAy8Upug4QXnKm0m2sWhbphiO8ZwGBVJ2kPTnt7Ph6zgwBu3HZ5LfU0Arp5OpMnEKPYNPHRW6tmzekRxtMLbv6bV8ngW2-zqfn4-2Rsv3b2kfTxWXI9RCsQGeEeWXsnRGtlh6o0fKBijECBvi7g7kYWcnrDH-W46IVCZTSFhp_LsT2gQOrX9NeHyW0Z9MeTk1cI7ebInJBk982EuVKcute8KnOvOrv8gYeW_ubgxJ4hqypkSGLXJSVB_zn53WW-SZAwA0TR7y-4QulgVK4B7XB4pN0BTTURl6sg2-YErCafUpvP01uAhvZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی از آمریکا مجوز تولید موشک پاتریوت خواست
🔹
در پی حملۀ شبانه سنگین روسیه به کی‌یف و مناطق اطراف آن، رئیس‌جمهور اوکراین از آمریکا خواست به اوکراین برای تولید موشک‌های سامانه پدافند هوایی پاتریوت مجوز دهد.
🔹
روسیه و اوکراین دیشب هم به حملات دوربرد علیه اهدافی که فاصله زیادی از خطوط مقدم جنگ دارند، ادامه دادند که تلفاتی در هر دو کشور داشت.
🔸
ستاد کل نیروهای مسلح اوکراین اعلام کرد که در حملات شبانه روسیه ۱۳ نفر کشته شدند. در مقابل، مقام‌های روسیه از کشته شدن چهار نفر در حملات پهپادی اوکراین خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445995" target="_blank">📅 14:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445994">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eab6aa623.mp4?token=IhPtiZSWnl_-Vv-b91mpzt3-I8_PAON894zAoMO9IugZC9X8RaR0aNfLS8Opx6v_gev6I0Z6IoNCJHWp5M7uumlx6SLZ8WviBcvCU5u7m53LMGg9MPFhdVN8pCUxLssMNdb021mPJY3iyzno8qa3o74i7rjaHuclOiTZGl3tlfzr-DONG2OpzHHigtoJkdChPwjO3mUTfaufh9SDnNZ1hOzbXwo5QR8973YX64H_kdm5SggTTsUtHr_XvMmYlImP5u3aNcBM2u-jAIFIE_B0Yc5lJR6yRsf7oP71975M4Ar0SUB2o36jDrgohbMr3ka__AWzxAg1wqqaHI2c-47BRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eab6aa623.mp4?token=IhPtiZSWnl_-Vv-b91mpzt3-I8_PAON894zAoMO9IugZC9X8RaR0aNfLS8Opx6v_gev6I0Z6IoNCJHWp5M7uumlx6SLZ8WviBcvCU5u7m53LMGg9MPFhdVN8pCUxLssMNdb021mPJY3iyzno8qa3o74i7rjaHuclOiTZGl3tlfzr-DONG2OpzHHigtoJkdChPwjO3mUTfaufh9SDnNZ1hOzbXwo5QR8973YX64H_kdm5SggTTsUtHr_XvMmYlImP5u3aNcBM2u-jAIFIE_B0Yc5lJR6yRsf7oP71975M4Ar0SUB2o36jDrgohbMr3ka__AWzxAg1wqqaHI2c-47BRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی آمادۀ میزبانی عاشقان آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445994" target="_blank">📅 14:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445993">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1926cb1a1f.mp4?token=b0T8F9l668RV7_6Vjs4obeTq6wdKBakIpv9TaXxZvgusMVdWb-6A8fzvKKjcxazaYi8UfQYzQJoPP-3OMEPBKz7hyqjNcR84-jlTBjY3hw3Dn-Ltht0OSSUnrKFUK0zhhlmhSt8E4GrJ7RTln9W5uxho5jnmHGhmIoaLV3enAIIhA1NkNxVGRr3w7axziq3UucgfzKL6qdwwHm7SV00kM7odpuRGslam70W0TWc663mXZkxQH_Kqok3vBaMZv7FP665ycp7atXojTKEnXma8b4iUgggMRMNyOXaqOgI1TruordLNnhLmo1O6m7x5C8AKk-7aALSpniytAcTYUEFJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1926cb1a1f.mp4?token=b0T8F9l668RV7_6Vjs4obeTq6wdKBakIpv9TaXxZvgusMVdWb-6A8fzvKKjcxazaYi8UfQYzQJoPP-3OMEPBKz7hyqjNcR84-jlTBjY3hw3Dn-Ltht0OSSUnrKFUK0zhhlmhSt8E4GrJ7RTln9W5uxho5jnmHGhmIoaLV3enAIIhA1NkNxVGRr3w7axziq3UucgfzKL6qdwwHm7SV00kM7odpuRGslam70W0TWc663mXZkxQH_Kqok3vBaMZv7FP665ycp7atXojTKEnXma8b4iUgggMRMNyOXaqOgI1TruordLNnhLmo1O6m7x5C8AKk-7aALSpniytAcTYUEFJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ روز مانده تا بدرقۀ آقای شهید ایران
◾️
در آستانۀ مراسم وداع، تشییع و تدفین رهبر شهید انقلاب و شهدای خانوادۀ ایشان، خیل عاشقان، خود را برای این بدرقۀ ماندگار آمادۀ می‌کنند.
◾️
از ۱۳ تا ۱۸ تیرماه در تهران، قم، عراق و مشهد
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445993" target="_blank">📅 13:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445992">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJCm20NbpHZLmLh5BXu3QmfdMjXFyQxqkYAUqgzOM0VY6AuqGLcAr8v2SHX8S5lVHExWqG1woyQbjSJ4iy-wDlhfVcgcGuJFN3GoOLg5boduIaEKqmvtlpki7kF4JPWREjtnFWvSj2muTPF8toCvw8z0YJ7iDSRl5n2MtOPBdzoE1RUV0vtTQXBx3GTXjcIIOu4rbPHmpYAbByGqHE4qaVETS_5M3LiGEFyJFhRNUH-7AoJucsMFtHDEtyT39WuxjCnSOTwXiOdinPRYHaCyB1hJw3HkHxqNssoF3SPjm1fW95T90X47HowIfEAVfU0NovBDn3-y9h-Q8p7CCOB7UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445992" target="_blank">📅 13:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445991">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723b049525.mp4?token=kJ-c0ErsWmHQJf7gJcoqUq771QIpaKz2uT51dJIKmjkTllaqHyXnsB1yI70xkRduqnJw786UB094i2gMb5EKaTCEXxXGzFOHfm-l15U54R0xhQp7WbtuOBypvT_zCWvm7-4CxLTKViu9-SYkjzLhbFJGBBuKv7aHcx-ywvbsUJ_8Fr30vKXSBBiUuJMZLp4Zgpw_NnkYYH5q_R0AS4xWpBYvG2ZHhNnnZK8igydmMOhl3ZRL-dCYkUd0WyNzVZhH2pfbSwtzVGuVCJPugGhAsuO7NHuRiPgJAn5r-sXb3HGzN9SuCIEUJbaAMvpzx4ApX_r3ZOddKwIuuyesez_CqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723b049525.mp4?token=kJ-c0ErsWmHQJf7gJcoqUq771QIpaKz2uT51dJIKmjkTllaqHyXnsB1yI70xkRduqnJw786UB094i2gMb5EKaTCEXxXGzFOHfm-l15U54R0xhQp7WbtuOBypvT_zCWvm7-4CxLTKViu9-SYkjzLhbFJGBBuKv7aHcx-ywvbsUJ_8Fr30vKXSBBiUuJMZLp4Zgpw_NnkYYH5q_R0AS4xWpBYvG2ZHhNnnZK8igydmMOhl3ZRL-dCYkUd0WyNzVZhH2pfbSwtzVGuVCJPugGhAsuO7NHuRiPgJAn5r-sXb3HGzN9SuCIEUJbaAMvpzx4ApX_r3ZOddKwIuuyesez_CqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات حضور مقامات عالی‌رتبۀ کشورها در مراسم ادای احترام و آیین وداع با پیکر رهبر شهید انقلاب
🔹
سخنگوی وزارت خارجه: از صبح جمعه ساعت ۸ صبح مراسم ادای احترام و آیین وداع با حضور تعداد زیادی از شخصیت‌ها و گروه‌های مردمی تا حدود ساعت ۱۲ ظهر برگزار خواهد شد.
🔹
بعدازظهر از حدود ساعت ۱۴ مقام‌های عالی رتبه کشورها و شخصیت‌های سیاسی در این مراسم شرکت خواهند کرد.
🔹
از حدود ۱۰۰ کشور اعم از شخصیت‌های سیاسی، روسای دولت‌ها، رؤسای مجالس، وزرای امور خارجه یا نمایندگان ویژۀ دولت‌ها و تعداد زیادی از شخصیت‌ها و گروه‌های مردمی میهمان خواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445991" target="_blank">📅 13:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445990">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978f022180.mp4?token=Gn-AdoyJcu8p0UJQPidfAERZbPDKagDKXFdsruWygq7F2IZEw5vHJ6N00p0Y3Bh2tMHSsZ3RsONIjC2h9lDOtzIxUN9YgbfkI0RlRJJDdAlNBTIJlDAzmj_EtpDP32vlv3cuT5xvRNFL0PsjHDJQa1_HyrBfKSuJBWQ1od5X61cMv2ve9dyP5Q1ZneiRQl-q7miuRAiQGc3F2B0kYM0L9NYDJ6OpMyvScmxBmRKu5k7yXRo__Zy-KHkHN0uDfwLUuLqPZFD4GTALnbr_xWMlgfnXudOQfn4oAM4y_eAN5SsSLqhYEt_vk0s3D5_wRFjAvDf5e6LGHj0AsDT_6yQ0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978f022180.mp4?token=Gn-AdoyJcu8p0UJQPidfAERZbPDKagDKXFdsruWygq7F2IZEw5vHJ6N00p0Y3Bh2tMHSsZ3RsONIjC2h9lDOtzIxUN9YgbfkI0RlRJJDdAlNBTIJlDAzmj_EtpDP32vlv3cuT5xvRNFL0PsjHDJQa1_HyrBfKSuJBWQ1od5X61cMv2ve9dyP5Q1ZneiRQl-q7miuRAiQGc3F2B0kYM0L9NYDJ6OpMyvScmxBmRKu5k7yXRo__Zy-KHkHN0uDfwLUuLqPZFD4GTALnbr_xWMlgfnXudOQfn4oAM4y_eAN5SsSLqhYEt_vk0s3D5_wRFjAvDf5e6LGHj0AsDT_6yQ0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کف پایش را هم گشتند
🔍
بازرسی بدنی مسی توسط آمریکایی‌ها روی باند فرودگاه
@Sportfars</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/445990" target="_blank">📅 13:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445989">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SorbvzLR35PrAcZBE-k694jDglWzn9PImX9S10ZBok_XTh9CYYsBzzjMZQ9gFVGFeALXl7D-S2DjzOji41YafuP0yLzUZ7Te0B9jT3Mze42C-mTdlJoTPSfUD61XZjNpqk3DlwTQmbaOxQTWXOiKdmQ-Y_3v4q-EeiQ9Mvv0lYZVZpq9hPLf6_NbRPR_NxQi_dcCqq919jX8nk-eWebDcNFzWJZ3W1K63fnXee25bnpE_9yUPsYIaDwEWP-DeLNI4g-rDERpfqXZnkWEyhi6kw_9KTDj9XbWjC5H3eXU3lAPm_ZWrbC9EPGQcoCp17_COsYxKRfyqyLxZH4H_LkesA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ۵ نفرۀ گروهک منحلۀ دموکرات متلاشی شد
🔹
در پی ورود یک تیم از گروهک منحلۀ دمکرات به مرزهای شمال‌غرب کشور در روز گذشته برای اقدامات خرابکارانه و تروریستی، با رصد اطلاعاتی سربازان گمنام در آذربایجان‌غربی و پشتیبانی آتش رزمندگان قرارگاه حمزه سیدالشهدا نیروی زمینی سپاه این اشرار در کمین رزمندگان قرارگاه حمزه گرفتار و به‌صورت کامل متلاشی شدند.
🔹
در این درگیری که در ارتفاعات مرزی شهرستان پیرانشهر صورت گرفت، این تیم پنج نفره به‌طور کامل منهدم شد و اجساد آنان به‌همراه انواع سلاح و تجهیزات در اختیار رزمندگان قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445989" target="_blank">📅 13:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445988">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGO79RooN-fOXyNccMtGw-NGnUjRdTB8OWvm9iWuatkZQVoSz3CTbYEhRGUyo7rHLUyw4JKaMgrfZ24ewrphYNGtjO6njaHfs1MSc3bLCGnlbualHY8f9mNYyR-MEiutbFpPDVuq8SteqYOCUyNCVpt-Jk_xzizVocuJFAEtEbzGN7VIh7ldz4waD9NRilNqQEeJxKb-1ISh0SAA354s9HJvOkllvUIbAAuHNdETMHgsvGIT2wTRkvCl_WYgo2C5KLpNHFr2eLBSYt_yKHO9zMlJ0Ee2FY7bSn_I-rNTVexXbz7JlGgl2W1fqTvWtj3ThjpxC7ieejvpT3ZAtFyl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: برای بدرقۀ مردی که تا آخرین لحظه استوار ایستاد؛ همه می‌آییم.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445988" target="_blank">📅 13:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445987">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVnUwg7TEvbdtR1CdArYmC60rLglLMM-CM84FmhooE9FWzBwy1sBRq2-PjUnG0w7X1-CTQUhTiLJ5X_coLlkMALDcEp-sKT1LV3bG7eSJObMtdtj74nsokaQbUYoypHxS1jmC9gjPOid3PbB7QNwW9PPT91KwNt4xmivYEUJLCIISXiaKK7XlBNQTnt3rqT97d4jeVNwDqgVXpJidz5XTPqY6KuzG5N3Fchl_FK9AFUh-MhXra0GbOxf7e6Qumc8TEkhkUEW1FBCLSVyGw_hnLQBzhxkcbZ0xeAmQ5b3GqDdHi7qzCC2T3CUn25T3ORl0DoykRFmDdzqyl43sNBwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده ولی‌فقیه در سپاه: شهید اکبرزاده پاسدار حریم ولایت بود
🔹
حجت‌الاسلام حاجی‌صادقی: شهید محمد اکبرزاده انسانی وارسته، متواضع، پاک‌نهاد و پاسدار حریم ولایت بود که بنا بر گزارش‌های واصله، در جریان فتنه اخیر و در پی جنایات رژیم منحوس صهیونیستی و آمریکای جنایتکار،…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445987" target="_blank">📅 12:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445986">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ab685976.mp4?token=RPAKZa-cb2VPOSMFmGP85HcvBG6GonWZTRf6Nxfnn14I6a0UMVVVAyfedBiOTNX_6_QbE2CucMHKagpGbwaZ8-eZdmLKuMw-tBP0PizYnImSQDyxtvLtKHfut1KhyJQRxV1r_yUsLP3M_S64VhB9rAWQ5TpZD3pjonSNjDAkTMoVMeqFtPyOb8I4nVz3eYfNrs_Cgj3A9Ut7IJ1fOIvIQ-fjjCd-o-63nDrOJ_EJQebjEV3R3P_ezyP0LFD5ZzOch7Ye-0_2CKinqmRxRy7HORrCh185JO7ZfyYwuya9xYFP1pXPk_xeMksoRrNaHFxSZS4LtTjaPT7XP7tai9isAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ab685976.mp4?token=RPAKZa-cb2VPOSMFmGP85HcvBG6GonWZTRf6Nxfnn14I6a0UMVVVAyfedBiOTNX_6_QbE2CucMHKagpGbwaZ8-eZdmLKuMw-tBP0PizYnImSQDyxtvLtKHfut1KhyJQRxV1r_yUsLP3M_S64VhB9rAWQ5TpZD3pjonSNjDAkTMoVMeqFtPyOb8I4nVz3eYfNrs_Cgj3A9Ut7IJ1fOIvIQ-fjjCd-o-63nDrOJ_EJQebjEV3R3P_ezyP0LFD5ZzOch7Ye-0_2CKinqmRxRy7HORrCh185JO7ZfyYwuya9xYFP1pXPk_xeMksoRrNaHFxSZS4LtTjaPT7XP7tai9isAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجموعۀ چهارباغ در ضلع شمالی مصلی آمادۀ مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445986" target="_blank">📅 12:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445985">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_epNcvYHeC_Tz5mEv7kiZUbN8bZB9Crr0ceCsUqtJ_Mc_p8q_0zu-Vd3aaDPmopVtHLJns0k--n97bYnjqqev3B0t5KP0k_Wi1LpahuZufBIz32KNG-K-zsm2whgZp-O92Falm-4PZKN45x1XizBTh0V3d55taah8W4ihnCPZZ8IB-bMZ436fJ0ZeOF9c1yeR3PFi_r4nBaVN200Uj_by2zhIDPnPsdoE0vw4ZQco5KkVCIuuI1BnguBScAtl-rt0nj0HNkDYVnHsk_7YgSSmzP04W8Oikx2Y7YZ9eMRIKkQjyVIok_VYo4y2-hisZ5OC1wTobjs1p5hnCOa3185g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🔹
پس از وقوع…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445985" target="_blank">📅 12:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445984">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
قرارگاه مرکزی خاتم الانبیا: هرگونه دخالت آمریکا در تنگه هرمز با واکنش قاطع و سریع نیروهای مسلح مواجه می‌شود
🔹
تنگه هرمز میدان بازی آمریکای متجاوز نیست، بلکه قلمرو حاکمیت مسلم جمهوری اسلامی ایران است. امنیت و حفظ ثبات این آبراه حیاتی، خط قرمز نیروهای مسلح…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445984" target="_blank">📅 12:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445983">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
قرارگاه مرکزی خاتم الانبیا: هرگونه دخالت آمریکا در تنگه هرمز با واکنش قاطع و سریع نیروهای مسلح مواجه می‌شود
🔹
تنگه هرمز میدان بازی آمریکای متجاوز نیست، بلکه قلمرو حاکمیت مسلم جمهوری اسلامی ایران است. امنیت و حفظ ثبات این آبراه حیاتی، خط قرمز نیروهای مسلح قدرتمند ایران اسلامی می‌باشد.
🔹
تمام شناورهای نفتکش و تجاری موظفند برای هرگونه تردد امن از تنگه هرمز، از مسیری که ایران تعیین نموده است، اقدام نمایند.
🔹
هرگونه عدم تمکین و خروج از مسیر تعیین‌شده یا بی‌توجهی به پروتکل‌های ناوبری جمهوری اسلامی ایران در تنگه هرمز، با پاسخ بی‌درنگ و مقتدرانه نیروهای مسلح مواجه شده و امنیت شناورهای متخلف را به خطر خواهد انداخت.
🔹
همچنین، مسئولیت هرگونه تلاش برای دخالت در امور امنیتی یا هرگونه اقدام مخل در تنگه هرمز توسط آمریکا، تهدیدی علیه حاکمیت ملی ایران تلقی می‌گردد و با واکنش سریع و قاطع روبرو خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445983" target="_blank">📅 11:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5paAfnNVRuMGuSUtv4BPelI64CSkN4dZih2DqzkFyojGBEFy18VM7R4QuGOu7As17fU_QlDgmHauwBcQgO31K2c2yITjmr1nIWPcknuvjb263Rfb4XuDWNA1Yp_wwf3V7A92uNYxqBxJ7D6OhXoi4BgxTpZz6nWgcohAmiJw9vJgnMPqaaGyiXIo86e4rfTai8gYks-DjQcZoF2o8-rrY-NYbQ_pZA4JN3ln-gaOzb9DD3WpLNFMS_a28UWnmFHAb0rQlAJ2MsIY-wvCuIHYDMQR9sQOusVMJ1Q6XWGyVl5QwVdM4d9AuzSEfy-HPapeOLz3aEHY_u-HmaKO8IGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXHpiqM9i8_Rb8RHmkmvG7jk6fRJJMBIXeqBUng9GsOGcbpMvzoBI6YHT507LAC4_ownE9QrUS3tSUvuWjxIwOdlQ-af0yKYepcDV9pTZKn8uX9SZhI8Dg-EqP3upRnOOMBEQXiz2xV_0qftluhCH7SvPl6gQCvVuKz-NQtzZkkqA_N_xFSPGxQ5WBUqKCeRFULisiRD2Zrh7RPHMXKg3Xij0nSoYYtI3Hc2gQe-QtayBZF9wQi3XjI-m6M92ezkBJGAV_sM7aCA-5YYezbQHbYrSFSZO5-PgMCOmhRjd7eZKHXIciAtWbwQYBslny97cFzUzpCvjtthQv6vC-MAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efj2ax0Fxtc7bHFotJZMrWoFPuHppy-n_hWx9bYhyf2jcw3RX-xtxqQXASD9ihQ4lIQcdT_SACIIZrgSXD1dchVjYjFyxpqJwyQSwmIWpfKlZ_CskOlu-O9wh1TfbixHxcf9pUanRznkrZAA1mAoW-Qp2900EznMOngcGpDFP-0vuCZudQbQwXIAbP6KCZ_qf0gAl5Q3Dchte3kp6uKTQ7o5Kdmalq05PvNPIJVIaqah_Z4CIcMTe2kfovXfPtl16pcSctcmFZ_MOADBezW9QljIM7PdRfUk2ox76KQnc_D3bfqmbb6TiQkTUHU6dYUHthwzusqFp7DJiXPMbuSb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnErD7tSJlcjlZM5CjgVojSqrf840tAkXyBNjMBwOsPLosqK47vMNZZ58MuUoBpLwOtxIdgD1oed2U3iv6_x3h4QhhAUrSEOZoqFjjE1yO6ZgGe9xf5t2LZEFedVGJMbVbNx-N0tQHr61Qh_uLzMRitPo4esyflZvOIDYMh6hiLRYL4xNfuLlQkP3YSbvRZJYUdFq2TNO30biWgLC93iLo0RCo_vBNxHgH5dbesNVrx0XwPvIuUH8bG3JvEdR911G8MOb-mRcWpvJXTJT_SxxrBtcMMSCXHzFxa8-DyC0OxvfvQJdxmwQmnn82z36uhDd4GFaR36NWgBYCBg8KDaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0NcnwFSasbGOn3wv9TtkboKaKX3_GP-2sx7ld-1JxW6Mlgzj-yX-rWRpt-b7QJULMjzdRHt_Pr1Rxr6eTMaK63jsJtic8-ooREVdtu2SDqN5b4ukHjWP6VFwKTBF1IRknEDWFFgOdhMemvG857j4c8a-g3Wv1tyzE1BTwxQkjAg9zy4OScoVoMUKPD9gcXAAWg7Bivmu2wHPUKHGrHjoC3QfbqGGxYv7a_LURlilRWu8XJ7eVQ5dJPCoBm8GXMOX2Z7IHuKYqZ-a2gycZYjcWdOfGNLkA9AjSqKB_6ONQA6LdQ7TDEEPmC6weyEzMDSjVKE5CjXfzlQloamhOKTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uS7r_6tPJhWce75K7MwuWf8fXoj2TfbwARGKdwwjWAZmO0v1WhrS9jMFlJksNLFdLcVQ8U3nhdZr27xyYnJ-tc0Mkybh8KRWiAcBpJImQfaB9_x1sIRfXyYk3aR_C1qrbBGVjDSVZsnP9aKW2y1HFkYFAUBbsRtBPqC7rm0mCdXDC5U_elGCUFkDR3xiloN5uO8dFCzjDIFbA9h6TykJA3rKNm5fQ6n8ZP2ioN0Nses-xZ-e6vtN0oCEc8epPqtQ34hBuCSIeDuhdxxkRw_rSeCfV-_RhIHFBCyxkUgBiSM5AxVnm3VdmJzHvAnAzf0Cd7MTCXAiuJkaEHWzis55Uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برگزاری مراسم وداع با همسر شهید رهبر انقلاب
🔹
مراسم وداع با معلم شهید خانم زهرا حداد عادل، عروس رهبر شهید انقلاب و همسر شهید رهبر معظم انقلاب شب گذشته با حضور غلامعلی حدادعادل، خانواده ایشان و جمعی از همکاران و دوستان وی در مدرسۀ فرهنگ تهران برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445977" target="_blank">📅 11:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b20a211.mp4?token=hKvHcccT9aPrtolXYLnFhgPJNW6RwEWGjFedYixd8J2b3jUPCUV0VZo75BFxa9EdI-yH6EBXHNUiNlTpkFNvdGHtKgDUGm_cjfe0OGfFBeeSyyuJFtBTE4q0TeSIIcjD7eFVE_XL_EHLaPzIVQLTRgdfEQAPAwJYu0yCpSCEle7LIFkT0MFm4HKWwQSiDLfaUtrkn6uwAG2SpiwtSfvEpA4okJhjawFcuUZ_noudOXWi5tLEERNR57v9PUluJaBTjMKKrWU-E4qaZLzoSQC2VJV25CrDiPbMpvSZbz4MHN7LMRw8UUYLDkTXodxiR3RXyieZogyPhvFzatIFhrIca10_eOVGN4G43yLtheqVUODthhtbcHsfOHdvShh5m1NU5HXwcU9bBDCB-K71y0bIVDIVbEJCaRK3FM7C1Bb5JQTD_yBtkcSqLjKBjJ6_oKMiY3XjMWoNUtEx9gSKR3xYaWQG5Y-0yFeJHIdlcm2iuy1k_-bn0ZqW-cmqxipia4DPz5Tz_ZFBiAjT3hxMcgk2-dGLzPFBTnIB6bJ03YdHpCRgCb31-drmPvV2inZW_3t22N1y_e2dtubKE5SWWnOxdg9sKR05BM0D53K11ECUWhlSXeVXoopC8F6SlsPVaJB4zskjH5XXcJHEfzKQgogDTE7ixh8frd8f__MmDyJXXrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b20a211.mp4?token=hKvHcccT9aPrtolXYLnFhgPJNW6RwEWGjFedYixd8J2b3jUPCUV0VZo75BFxa9EdI-yH6EBXHNUiNlTpkFNvdGHtKgDUGm_cjfe0OGfFBeeSyyuJFtBTE4q0TeSIIcjD7eFVE_XL_EHLaPzIVQLTRgdfEQAPAwJYu0yCpSCEle7LIFkT0MFm4HKWwQSiDLfaUtrkn6uwAG2SpiwtSfvEpA4okJhjawFcuUZ_noudOXWi5tLEERNR57v9PUluJaBTjMKKrWU-E4qaZLzoSQC2VJV25CrDiPbMpvSZbz4MHN7LMRw8UUYLDkTXodxiR3RXyieZogyPhvFzatIFhrIca10_eOVGN4G43yLtheqVUODthhtbcHsfOHdvShh5m1NU5HXwcU9bBDCB-K71y0bIVDIVbEJCaRK3FM7C1Bb5JQTD_yBtkcSqLjKBjJ6_oKMiY3XjMWoNUtEx9gSKR3xYaWQG5Y-0yFeJHIdlcm2iuy1k_-bn0ZqW-cmqxipia4DPz5Tz_ZFBiAjT3hxMcgk2-dGLzPFBTnIB6bJ03YdHpCRgCb31-drmPvV2inZW_3t22N1y_e2dtubKE5SWWnOxdg9sKR05BM0D53K11ECUWhlSXeVXoopC8F6SlsPVaJB4zskjH5XXcJHEfzKQgogDTE7ixh8frd8f__MmDyJXXrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده سپاه تهران: خودروی حمل پیکر مطهر رهبر شهید به شکل ضریح حرم امام رضا(ع) طراحی شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445976" target="_blank">📅 11:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445975">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a87fdc50.mp4?token=PH0oN91HSy9xvqhNPIZsZfZr-DJvGelkSBfASXe0URpUymcHt1gO9ahrqhhMiMxQ5xK37kl8R8ElheHmpKY_7UD-v4uQR0hsRu5jLrItcY-zjCaFEkrHFg8v-m5d2dKF8N16CsMz0GQ0lkiaYG5onR8e9fbHBz55PFaH4UD2g6hnxYq1fG7E0K6DlI2uV1QaeKPlmupdGTffSzlsP0GM-pAxKw1SQhZkUshk75XcqTa6MdHnEboyBshhtOWslQGNVGot0N_CwXk7P8-_ZT3APAuerPhnpJbgK_gZrBXK5pm1IjkLj9URO9lYvVFL_TB0JBLlzfxFKa2nsa3_LqCpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a87fdc50.mp4?token=PH0oN91HSy9xvqhNPIZsZfZr-DJvGelkSBfASXe0URpUymcHt1gO9ahrqhhMiMxQ5xK37kl8R8ElheHmpKY_7UD-v4uQR0hsRu5jLrItcY-zjCaFEkrHFg8v-m5d2dKF8N16CsMz0GQ0lkiaYG5onR8e9fbHBz55PFaH4UD2g6hnxYq1fG7E0K6DlI2uV1QaeKPlmupdGTffSzlsP0GM-pAxKw1SQhZkUshk75XcqTa6MdHnEboyBshhtOWslQGNVGot0N_CwXk7P8-_ZT3APAuerPhnpJbgK_gZrBXK5pm1IjkLj9URO9lYvVFL_TB0JBLlzfxFKa2nsa3_LqCpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائرشهر امام خمینی(ره) در ضلع شمالی مصلی آمادۀ مراسم وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445975" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445973">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124c09411b.mp4?token=kInxe-pVi3ofAWFQt9zpW3tlqK98QotqgLSG9286v5S1_vtZZZDM01GvAFx6b0cmfapxfrw3Ja3Wtpvw0Sb9v_IWy2j2Ji3Dk9w7ymAAGIIV_y7ES9LU1gjWP8Cvo2pKXCClQbPiMHu6gDam_MtRa0f6NaYAlcJmvxwVNV7UKrbY3Qj_WvZ6OiN7OncyfySw6k_djt88fokx-F1_cg_hLdjKKrjRLqsbSiX1_dpWsxC7bcpt6P7-3zKvLDCFMdoDKgXz6LfvwFDcEMawXHp2jXOfiLqBIttxFGs2fVe3TQPs_cKG1J1Zubuxzzbg6ShM9Aaj1s_ajFFJ2bq8kZo6VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124c09411b.mp4?token=kInxe-pVi3ofAWFQt9zpW3tlqK98QotqgLSG9286v5S1_vtZZZDM01GvAFx6b0cmfapxfrw3Ja3Wtpvw0Sb9v_IWy2j2Ji3Dk9w7ymAAGIIV_y7ES9LU1gjWP8Cvo2pKXCClQbPiMHu6gDam_MtRa0f6NaYAlcJmvxwVNV7UKrbY3Qj_WvZ6OiN7OncyfySw6k_djt88fokx-F1_cg_hLdjKKrjRLqsbSiX1_dpWsxC7bcpt6P7-3zKvLDCFMdoDKgXz6LfvwFDcEMawXHp2jXOfiLqBIttxFGs2fVe3TQPs_cKG1J1Zubuxzzbg6ShM9Aaj1s_ajFFJ2bq8kZo6VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف تریلر حامل ۷۶۶ کیلو تریاک در استان فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/445973" target="_blank">📅 10:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445972">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قالیباف در پیام دعوت از مردم برای شرکت در آیین تشییع رهبر شهید: باید برخاست و ندای خون‌خواهی ملت را به جهان رساند
🔹
ملت بزرگ ایران امروز ایران عزیز در آستانه خلق یکی از بزرگ‌ترین صحنه‌های تاریخ خود ایستاده است، روزی که یک ملت، با دل‌هایی سرشار از عشق، وفاداری…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445972" target="_blank">📅 10:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445971">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محدودیت تردد تهران-شمال و چالوس
🔹
تردد در مسیرهای شمال به جنوب آزادراه تهران-شمال و جاده چالوس از ساعت ۹ صبح امروز تا اطلاع بعدی ممنوع است.
🔹
در آزادراه تهران-شمال، چالوس، هراز و فیروزکوه مسیر جنوب به شمال ترافیک سنگین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445971" target="_blank">📅 10:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445970">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1xp4vCqQK8Du4ExJNpdTwzLQd9KRWJaWRhyK1_a8Czxkx0VzBGbRQzldeOrb8HOPv9NVJWqtgthuTBnMy0qBlVGVe0DiOaA_r1Ate7bZtGxpxkTlHHwAJ6uJKuz3ENikWboQnUYB24326YW6HvyGtIQT39N36OWX_Eq-RN4eR7hUevteg1oKckZ-KH5nmxFN5HLPCEWP2Q9hDslLJacQgheT1wl88EJxHLXTF4mYzokNXkwr1tk7qB3CpeaCOLJM8oxEonUqnXh1VvgLzSVOXZAN5Pv5Rpk2BwyyOoiOkWD1S4UQpAea4hb5pX2WgdFsbk9-hR0XJ_ga1D7XVUDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران در آستانه میزبانی از بزرگ‌ترین رویداد ادبی تشییع امام شهید
▪️
آیین بزرگداشت بین‌المللی شهید آیت‌الله سید علی خامنه‌ای با حضور شاعر برجسته فلسطینی و چهره برتر ادبیات و هنر مقاومت، استاد تمیم البرغوثی و دیگر چهره‌های شاخص رسانه‌ای جهان عرب؛ به همت پردیس بین‌الملل سازمان هنری رسانه‌ای اوج برگزار خواهد شد.
🕓
جمعه ۱۲ تیرماه ساعت ۱۷ الی ۱۹
📍
تهران، شیان، میدان شهید تجرلو،
مرکز همایش‌های بین‌المللی کشتیرانی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445970" target="_blank">📅 10:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445969">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzlh5_sluka39awzrJise-bWxmu3JJ4-ucjFSvLNKGJFJNSeQPnMjrx4qriGHmlhAPjMSlYSQCkCUDzB-9vJ70XXm-A34McYpmmoiFxWfSJfPzxsgPP1DqJHR5IUC1l3NRgZmNJuXtgUmw-SBAP-LhA6p3Bcu14KoBiz7nCDGJzj6G5GbxtJKdSjRe56GzqEb5TJ--g_VYce8zewMS1T9PL2SdSMvQ9SMYsffhiQ-HwadQMcbbiXsozy7HI-pyjAiFFemcCTLqc4O3tT0q49BYKwUWf-3rb2E2ZfPz2RlMCwOuJrfDWsE-l3NONvdwYLsiGmfJnDFUX0iXGZTH2R6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
پذیرایی موکب بانک شهر از عزاداران مراسم وداع با رهبر شهید انقلاب اسلامی
🔹
در حالی که ملت معزز ایران و جهان اسلام در فضای پر از اشک و اندوه، خود را برای وداع با رهبر بزرگوار و شهید انقلاب اسلامی آماده می‌کنند، موکب بانک شهر با هدف خدمت‌رسانی به عزاداران و تسهیل امور میزبانی در این مراسم بزرگ، در یکی از نقاط پرتردد پایتخت ، آماده پذیرایی از جمعیت عظیم مردم است.
🔹
موکب بانک شهر با استقرار در محل سازمان فرهنگ و ارتباطات اسلامی (ورودی بزرگراه شهید همت)، مسئولیت پذیرایی از عزاداران و شرکت‌کنندگان در مراسم وداع رهبر شهید انقلاب اسلامی را بر عهده گرفته است. این موکب با بهره‌گیری از کارکنان داوطلب بانک، به صورت 24 ساعته، ارائه خدمات متنوع به عزاداران رهبر شهید انقلاب را در دستور کار دارد.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/445969" target="_blank">📅 10:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445968">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/445968" target="_blank">📅 10:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445967">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgR5rba7H8SwgJyx20OFSHNw1akjDukN8YadKsIDYW5_jGBu0ScKY5Q5QPifL7xjwnPEwa6NdzTa-H9xhKYe6ag-sBy7bP8clliJMmUeNovTgMoDSkpur3P1ql5mG1itUtVLiaQ4AmQ1J4FSt-9YRzXqzCFP8ViYA4oBfTJ-ZLYvG2N5ptEGE_9qtFmcVixa2Flyeg-cBwuNTJzHrOqMEo82VxWL4Kr0qgrZHUd-HE7xNkv85XwSRvkQFwFfVxPwplNwo-iVmSrVzGpai-bJwWBJzxR3Quja5EhMDBPZ04xSVfvI9PYKBzoLSh-K62p0jh7oq7KR4DM_mjbTCi-hNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف در پیام دعوت از مردم برای شرکت در آیین تشییع رهبر شهید: باید برخاست و ندای خون‌خواهی ملت را به جهان رساند
🔹
ملت بزرگ ایران امروز ایران عزیز در آستانه خلق یکی از بزرگ‌ترین صحنه‌های تاریخ خود ایستاده است، روزی که یک ملت، با دل‌هایی سرشار از عشق، وفاداری و لبریز از داغ فراق، به بدرقه بزرگ‌مردی می‌آید که عمر پربرکت خویش را در راه اسلام، استقلال ایران، عزت ملت و آرمان‌های بلند انقلاب اسلامی سپری کرد، مردی که به نمایندگی از ملت شریف و سربلند کشورش هیچ‌گاه در مقابل استکبار جهانی سر خم نکرد و تا فتح قله شهادت مردانه در مقابل ظلم و ستم ایستاد.
🔹
تشییع پیکر مطهر رهبر شهید انقلاب اسلامی، حضرت آیت‌الله العظمی شهید سیدعلی حسینی خامنه‌ای، تنها یک مراسم بدرقه نیست، تجدید میثاق یک ملت با راه پرافتخار شهیدان، با ارزش‌های انقلاب اسلامی و با عهدی است که نسل‌های این سرزمین برای پاسداری از آن ایستاده‌اند. عهدی که با اشارات خمینی کبیر رحمت‌الله‌علیه با صاحب‌الزمان عجل‌الله تعالی فرجه الشریف بستند و تا آخرین نفس پای آن ایستاده‌اند.
🔹
امروز چشم تاریخ به ایران دوخته شده است. حضور میلیونی و حماسی شما مردم بزرگ، جلوه‌ای از عشق و وفاداری خواهد بود، حضوری که به خواست خداوند، این بدرقه را به عظیم‌ترین و ماندگارترین بدرقه تاریخ بشر تبدیل خواهد کرد، حماسه‌ای که عظمت روح یک ملت را به جهانیان نشان خواهد داد.
🔹
از همه مردم عزیز ایران، از جوانان پرشور، خانواده‌های معظم شهدا و ایثارگران، زنان و مردان غیور این سرزمین و همه دلدادگان راه حق دعوت می‌کنم با حضور باشکوه خود، صفحه‌ای پرافتخار در تاریخ ایران اسلامی رقم بزنند و بار دیگر نشان دهند که ملت ایران در لحظه‌های بزرگ، یکپارچه و استوار پای عهد خود می‌ایستد. باید برخاست و ندای خون‌خواهی ملت را به جهان رساند تا دنیا بداند ملت شریف و نجیب ایران در مقابل ظلم و استکبار سکوت نمی‌کند و از خون امام خود نخواهد گذشت.
🔹
همچنین از همه مردم شریف و فهیم ایران دعوت می‌کنم همچون همیشه، با روحیه ایثار، همدلی و مسئولیت‌پذیری، در برگزاری هرچه باشکوه‌تر این مراسم بزرگ یاری‌رسان خادمان خود باشند، باید یک‌پارچه با خدمت به زائران و شرکت‌کنندگان، رعایت نظم و آرامش و همراهی با دست‌اندرکاران، تلاش کنیم تا این حماسه ملی در شأن مقام والای آن رهبر شهید و عظمت ملت ایران برگزار شود و این حماسه تاریخی به عنوان سندی انکارناپذیر از استواری ملت ایران و آزادی‌خواهان جهان در تاریخ بشر به ثبت برسد.
🔹
امروز هر قدمی که به سوی این مراسم برداشته می‌شود، ادای دینی است به مجاهدی که خود را وقف مردم کرد و هر قطره اشکی که بر این مصیبت جاری می‌شود، نشانه پیوند عمیق ملت با خادمان صادق خویش است و هر ندای وفاداری، گواهی است بر تداوم راهی که با خون شهیدان آبیاری شده است.
🔹
خداوند روح بلند آن رهبر مجاهد و شهید را با انبیا و اولیای الهی و شهدای راه حق محشور فرماید و ملت بزرگ ایران را ذیل توجهات حضرت ولی‌عصر ارواحنا لتراب مقدمه الفداء و تحت اوامر رهبر شجاع، دانا، دلسوز و داغدار این ملت، حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای حفظه‌الله در ادامه مسیر عزت، پیشرفت و سربلندی یاری نماید.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445967" target="_blank">📅 10:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445966">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a220e92f7a.mp4?token=p0TxrEHZm1Uh_StN0SyjhWz-ZAuauKpringgW0Xm5HL-g-20q2QipiZ5IdZZ23FsuurJPq275K2k1xKNC0awyI3jNC5owM4o1vjGta0UAw-YZdSO40o9XJ45maJGvfbr9qDJtLSn6U2sXeHhJVQbwkWS9ZG3MOmI7MYpEUj94MBmNyFBRgj44EPmgzUqgtR-Z2748q6-9GO56-q6Zi7KcjrldeT-fr1LJCghFnc3cHHGvopVmsegripEZzQx1mDNDsOw2IShL0r_Aon6moBr3WRa9BSyhbVCPqUbIUj_MXWujoPpW7Subbez1XYOYFp-8iAGo-ugJyu6tBvbCnbhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a220e92f7a.mp4?token=p0TxrEHZm1Uh_StN0SyjhWz-ZAuauKpringgW0Xm5HL-g-20q2QipiZ5IdZZ23FsuurJPq275K2k1xKNC0awyI3jNC5owM4o1vjGta0UAw-YZdSO40o9XJ45maJGvfbr9qDJtLSn6U2sXeHhJVQbwkWS9ZG3MOmI7MYpEUj94MBmNyFBRgj44EPmgzUqgtR-Z2748q6-9GO56-q6Zi7KcjrldeT-fr1LJCghFnc3cHHGvopVmsegripEZzQx1mDNDsOw2IShL0r_Aon6moBr3WRa9BSyhbVCPqUbIUj_MXWujoPpW7Subbez1XYOYFp-8iAGo-ugJyu6tBvbCnbhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم مهیای بدرقهٔ رهبر شهید می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/445966" target="_blank">📅 09:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445965">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baadb9236f.mp4?token=DMzU1DwZHu7DecAi3AlUS4Zk0walRkSTDJz1g8heynfviQTFzpE5wQ-xJO9YbDEGtkqMrpG0o6qPbhF87iDBDKUMfVipP4N11rDZokVMyGXvy1_-96Idf2N7zJiixvq-7gToceKy-toq3Q638gAE9iqFcBgGuNbn9KA1rroB6D3xJOj38hh5ZnRELCGlyJniaKGp_fWjmw7EPzZWMyK7znh1QQq3dwm9NJuuoogWVpBECdZ2mKh9u9otFlE32gPT8GaxPVnEB_-doWtbcVVbEQtWKIaTr2Pwlv7eIRBEYYilHvjvm0YZBF8OxGyXVHfVJORts6tCpBgDuiawm6aj9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baadb9236f.mp4?token=DMzU1DwZHu7DecAi3AlUS4Zk0walRkSTDJz1g8heynfviQTFzpE5wQ-xJO9YbDEGtkqMrpG0o6qPbhF87iDBDKUMfVipP4N11rDZokVMyGXvy1_-96Idf2N7zJiixvq-7gToceKy-toq3Q638gAE9iqFcBgGuNbn9KA1rroB6D3xJOj38hh5ZnRELCGlyJniaKGp_fWjmw7EPzZWMyK7znh1QQq3dwm9NJuuoogWVpBECdZ2mKh9u9otFlE32gPT8GaxPVnEB_-doWtbcVVbEQtWKIaTr2Pwlv7eIRBEYYilHvjvm0YZBF8OxGyXVHfVJORts6tCpBgDuiawm6aj9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دل‌ها آمادۀ بدرقۀ پدر امت
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445965" target="_blank">📅 09:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445964">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364498c1b4.mp4?token=e-cG5e0WJY53V-BHblK6mX7qkPt0FpyYXnk-V83PufYjIR3LGysnHy9flcwU6yhD4p40LrvDwjDcu57OlD_pbeSEanc5Z4KzfgPVufOJ0iua13_bxQR226I2vYTGs5nJ_pKpBjzkf_EBUmkuxC-iXo08kodNoBcIdK-p5T---K9TY5O35XwciW4RF8QArIn8AFbs4I1Qjl31FfWyZWCfxiKZYBAVK4aKNzZL-m0HadnXAzQb9_jkLpoD3i2iIIxR7un4JDc_AT28gtLH2wO0uOTgX1uwGxo7lye_pD8DOzr6o45VwuyuYKuYVWfJUCoT1mhuyHEG8Fk2yqKjAo5FWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364498c1b4.mp4?token=e-cG5e0WJY53V-BHblK6mX7qkPt0FpyYXnk-V83PufYjIR3LGysnHy9flcwU6yhD4p40LrvDwjDcu57OlD_pbeSEanc5Z4KzfgPVufOJ0iua13_bxQR226I2vYTGs5nJ_pKpBjzkf_EBUmkuxC-iXo08kodNoBcIdK-p5T---K9TY5O35XwciW4RF8QArIn8AFbs4I1Qjl31FfWyZWCfxiKZYBAVK4aKNzZL-m0HadnXAzQb9_jkLpoD3i2iIIxR7un4JDc_AT28gtLH2wO0uOTgX1uwGxo7lye_pD8DOzr6o45VwuyuYKuYVWfJUCoT1mhuyHEG8Fk2yqKjAo5FWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین تصاویر از آماده‌سازی خودروی حامل پیکر مطهر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/445964" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445963">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۶۰۰ خبرنگار خارجی مراسمات وداع و تشییع رهبر شهید انقلاب را مخابره می‌کنند
🔹
وزیر ارشاد: حدود ۶۰۰ خبرنگار و نمایندۀ رسانه‌های خارجی در کنار رسانه‌های داخلی این مراسم را پوشش خواهند داد تا ابعاد مختلف این رویداد برای افکار عمومی جهان روایت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/445963" target="_blank">📅 05:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445962">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71fe17f30.mp4?token=HIuhJvDL9V7JIDnsEj7dVUlMRMtzP-TvH1daxxscFsCA3g5z3rZrzjrS4hRqBfkdP01dqMB5T7rFKS0ofVXUcu1ukXdDfDgaFsU5opIpx7TnuqnSa40F-TIS0Tvo3ssoCEkRrMy8uZZ6DoDOuHh2sK097xZ9caiazqIsjZoYZJGmsGZOV8gvX7ISfBe8odluk19uoLoCls_B8BwF-ikWAaW2x7qwIE2PkLHO6YZpI4GE_5_OuBDEg2Usug2EaX6H8OrKa_23duAL8Yqn3O5T0nU4To5ttkQPKe-eoTLp_skxvqPhWkcZnqngDoURevtjhJ16zYYiaI-dbu53Wj_JMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71fe17f30.mp4?token=HIuhJvDL9V7JIDnsEj7dVUlMRMtzP-TvH1daxxscFsCA3g5z3rZrzjrS4hRqBfkdP01dqMB5T7rFKS0ofVXUcu1ukXdDfDgaFsU5opIpx7TnuqnSa40F-TIS0Tvo3ssoCEkRrMy8uZZ6DoDOuHh2sK097xZ9caiazqIsjZoYZJGmsGZOV8gvX7ISfBe8odluk19uoLoCls_B8BwF-ikWAaW2x7qwIE2PkLHO6YZpI4GE_5_OuBDEg2Usug2EaX6H8OrKa_23duAL8Yqn3O5T0nU4To5ttkQPKe-eoTLp_skxvqPhWkcZnqngDoURevtjhJ16zYYiaI-dbu53Wj_JMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرود پدر ایران
🔹
تصاویری ماندگار از رهبر شهید انقلاب، به‌همراه قطعۀ موسیقی وداع
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/445962" target="_blank">📅 05:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445961">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بلومبرگ: عبور نفت از تنگه هرمز، ۱۰ میلیون بشکه را رد کرد
🔹
یک مقام آمریکایی شامگاه چهارشنبه مدعی شد که حمل و نقل روزانه نفت از طریق تنگه هرمز، از ۱۰ میلیون بشکه فراتر رفته و ۵ میلیون بشکه نفت دیگر هم از طریق مسیرهای جایگزین منتقل می‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/445961" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445960">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/facVrfe8rt66B4zYB61kkx_HdK_COt6cwrHRy33WjAdEknx2Xw1WhLtvUcgAdCvDyvmmxvk20UACdZC4I1T-5tyaWegRBCXZea_TnfOdwszbAv2rI6S6LBrg5h83EUl1D2-Z3HQ78a6j1PyeiVoOb9cO0A3cpEuNzCtUhQDI4FC1VQ9cB0YtSt_8O1Y2KAFRdlEtT_tPtfqS0HMiSYDkt9tDAs8DbQQzmYA-EzCwORGRwsvoXh74ZU6Od_Hp_yadhbs_u5wl5CEcY1poFNqeS5y6Zh4d8LKWKYM2Wm77BQO0F669m9aDVqb8YxRDUmPQ1EPzNmh37TbBFAbtIl-mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رئیس دانشگاه علوم پزشکی ایران:
تمام خدمات درمانی در مراسم تشییع و وداع با رهبر شهید انقلاب رایگان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/445960" target="_blank">📅 03:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445959">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGxtTYEbxl9q1Ly3_kS_ozguZkkIvJaqB1YOsG5XBWOVvj6DUmnhXHY4UYSUSqchnHZuNJJ8HuJsQuYruOGSGMlaTXmTRa9DSnZAz-dK7p1a772Gs9cDysp5tVIASxt8CiDKfVgPI8AUsz0SsJwsFWQK-LZGXo8twZvDsfAANapsxy39rwKviztPxilOVpSmdV4vB5SNajbr-dcDKbfU20Wy3qOfiOabzIk_Bo2JDgaJSjxx_xWcrzMSugOkVqQqbmiW6ZdDICGb5VNTewPpQq1niO4-Dz8PiWPpyRnMe5BgMYwRgN_4mVByLC7VygIQSxBCjXI0VVBId0LWybmtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده‌سازی ۵۰ میلیون نان و استقرار نانوایی‌های سیار در مسیر تشییع رهبر شهید
🔹
سازمان بسیج اصناف: با مشارکت اتحادیه‌های نانوایان سراسر کشور، ۵۰ میلیون قرص نان در حال تهیه است و ۱۶ نانوایی سیار نیز در تهران و حومه آن مستقر شده‌اند تا کمبودی در زمینۀ نان احساس نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/445959" target="_blank">📅 03:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445958">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5f5092e8.mp4?token=tgRP-WnnOKTFTxDpMBaACDzAsu197eJ8THkMUd_Dtgg9Qnv-NekTFU8PiKiomh6GKmJGDKDupUW25SM1kXYb2o3Bw_l0B6oipvtlfooB5q1q79NbXtgPRPHFj1DwZC4ebmDmoqnznVsIHnqpWGcvwerGbItQbES74Wzf8VYyosWwcaz0Dt83iNqMjvVhrqwD6NG37NZeAqIk2Xk5BW1qjIZynrARm4u8MBxwTcSmMTYg53AubgkCz3O-ogzVhrvGMbf2idn-D3A3N-mondjkyPqEJBos1vJ_BFkPib-edoWpbdhkNL-VIKzszKyRnoFZ9MNIsrRohK3lcU8EYFNgnZ5YwNDwyRRGjv7i5dW6lPd784FFcRcZ9tA_T4hcK5YV_ECtEwTEtyB1v0UnRRqW8rDyHnzSEaEKGDyDuKXHSbkQwkI7mRId3UKXMRbeFnVDduzGNQb98pxHUpjJ2VOIPlrS2gDwL1ka9lV7QfuP7lRzkWNs-27HE38N6DraUaCF2Vp917NGqoHsEPi-ojWwNSG0Y5iaYmEAiPPyS5-Y_LHFT8nV_9qYCVAllCJTFVkEAvBA2J5NqgRWYDMaptcD98IS6qu5p2jXL4vL-Bk3pEyD8uChOWktLSQpH3lKpIoXMAzrYOrqYzWDQXraZshDtbrf2Vl_2hn0D4gbfBbK7D4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5f5092e8.mp4?token=tgRP-WnnOKTFTxDpMBaACDzAsu197eJ8THkMUd_Dtgg9Qnv-NekTFU8PiKiomh6GKmJGDKDupUW25SM1kXYb2o3Bw_l0B6oipvtlfooB5q1q79NbXtgPRPHFj1DwZC4ebmDmoqnznVsIHnqpWGcvwerGbItQbES74Wzf8VYyosWwcaz0Dt83iNqMjvVhrqwD6NG37NZeAqIk2Xk5BW1qjIZynrARm4u8MBxwTcSmMTYg53AubgkCz3O-ogzVhrvGMbf2idn-D3A3N-mondjkyPqEJBos1vJ_BFkPib-edoWpbdhkNL-VIKzszKyRnoFZ9MNIsrRohK3lcU8EYFNgnZ5YwNDwyRRGjv7i5dW6lPd784FFcRcZ9tA_T4hcK5YV_ECtEwTEtyB1v0UnRRqW8rDyHnzSEaEKGDyDuKXHSbkQwkI7mRId3UKXMRbeFnVDduzGNQb98pxHUpjJ2VOIPlrS2gDwL1ka9lV7QfuP7lRzkWNs-27HE38N6DraUaCF2Vp917NGqoHsEPi-ojWwNSG0Y5iaYmEAiPPyS5-Y_LHFT8nV_9qYCVAllCJTFVkEAvBA2J5NqgRWYDMaptcD98IS6qu5p2jXL4vL-Bk3pEyD8uChOWktLSQpH3lKpIoXMAzrYOrqYzWDQXraZshDtbrf2Vl_2hn0D4gbfBbK7D4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعضی‌ها دینشان گلبول سفید ندارد!
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/445958" target="_blank">📅 03:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445957">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">محل وداع با پیکر رهبر شهید در مشهد مشخص شد
🔹
شهردار مشهد: محدوده بدرقه و وداع با پیکر مطهر امام شهید و خانواده ایشان در مشهد در ضلع غربی تقاطع چهارسطحی آزادگان و در محدوده بزرگراه حضرت سیدالشهدا خواهد بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445957" target="_blank">📅 02:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445956">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وقوع چندین انفجار در پایتخت اوکراین
🔹
رویترز به نقل از شاهدان عینی گزارش داد که صدای چندین انفجار در کی‌یف، پایتخت اوکراین شنیده شده است.
🔹
شهردار کی‌یف اعلام کرد که پدافند این شهر درحال دفع حملات پهپادها و موشک‌های بالستیک است.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/445956" target="_blank">📅 02:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445955">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzczy55HkU7BxHX84qMHx9UuwpCaFpiItHAUYyWxNerLgf0TaBtcXaNgJS0HJ4ZcXp3sDd1pBFNbfynY5LSCfBTQWX7CE6YyPD9767l6fdsueq3-0Hlw18BusCtNQLnVGIpSWnPNl_llfO1rhAblQWTM3BLKWjm3-tE_PWxDxNIcfRcSVOj9jGTXW4xI6BkW97jBjTZXCbXQkW3T5K0d69NlleHlRDBibt6wP0Ki0-QWfmwEZQ4LEKCrOVstRTNg-0dOmidpz5rfM2wvgDsvspvfQSRym7eEHIMZP1TXBve3LO2fZOd-N232oNZ1ZFYnr_Hv38mP1PaopAyak4L3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نمودار مراحل حذفی جام‌جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/445955" target="_blank">📅 02:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445954">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
حملات صهیونیست‌ها به مرکز نوار غزه
🔹
منابع فلسطینی از حملات جنایتکارانۀ اشغالگران به مناطق مسکونی در مرکز نوار غزه خبر دادند.
🔹
به گفتۀ منابع خبری، توپخانۀ اسرائیل مناطقی در شمال شرقی اردوگاه آوارگان البریج در مرکز نوار غزه و اطراف پل وادی را گلوله‌باران کرد.
🔹
همچنین پهپادهای رژیم صهیونیستی در ارتفاع پایین در شهر خان‌یونس در جنوب نوار غزه درحال پرواز هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445954" target="_blank">📅 02:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445953">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubSoh2CHAd5s3Ll1MMvTgwii-bcQtKIZNtnvQoX3AHhDLA9ml3mFpM8cOnzPZzOaqEskikcBI3h2PEW1RcPXlgPpMQJKa0oef4v3Uc3596xmPLQUCeA3CXAeRq-xh62S0plxNrxqjwKVVy3Blhng-P6qKcOFiH6U-RJXImSuqR3jYFj1bMykDDKcvYSr2dC8cB5rV4tnUZ49OkaMIB_2lT_7UYagwMdmQe9-tNAI_hLcpM7oAmsm5HYe6P72yGC-0WKH2HA0e-yuDJ9CNMMBdIUyHINRSWhjtul926twYodIgRxF6-LyNvlUnTWCu0u5u52dZQbkrGNRu_ZU7nBxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلای ژاپن را سر سنگال آوردند
عقب بودند و به بازی برگشتند
بدون دوکو، بدون دی‌بروینه، با تیلمانس!
شوک بزرگ به سنگال در یک‌قدمی صعود
بلژیک ۳ - ۲ سنگال
@Sportfars</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/445953" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445952">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به جنوب سوریه
🔹
منابع خبری از گلوله‌باران حومۀ شهرهای قنیطره و درعا در جنوب سوریه توسط توپخانۀ رژیم صهیونیستی گزارش دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445952" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445951">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جزئیات تعطیلی واحدهای قضایی در ایام تشییع رهبر شهید
🔹
تمامی واحد‌های قضایی در استان تهران در روز‌های ۱۳، ۱۴ و ۱۶ تیرماه تعطیل است.
🔹
تمامی واحد‌های قضایی در سراسر کشور دوشنبه ۱۵ تیرماه نیز تعطیل خواهد بود.
🔹
همچنین تمامی واحد‌های قضایی استان قم در روز سه‌شنبه ۱۶ تیر‌ماه و استان خراسان‌رضوی در روز پنجشنبه ۱۸ تیرماه تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/445951" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445950">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
برگزاری مذاکرات فنی غیرمستقیم ایران و آمریکا در دوحه
🔹
رویترز: گفت‌وگوهای فنی ایران و آمریکا به‌صورت غیرمستقیم در دوحه در حال برگزاری است و در این میان، قطر و پاکستان نقش میانجی را ایفا می‌کنند.
🔹
نمایندگان اصلیِ ترامپ در مذاکرات با ایران، یعنی کوشنر و…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/445950" target="_blank">📅 01:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445949">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎥
دلنوشته‌های مردم در «کشوردوست» تبدیل به نماهنگ شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445949" target="_blank">📅 01:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445948">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrniQv1lwJXmk0fqooJjC6p4FVSMH4MHwiOSxqaIATUmQLZEKEwwI9TwJREli6NyAKCH3u5RPsOqgX-UqyQ38G89IbtX8cq_mpK4DoCfJvUJQrSMy7eR-x3dNPCBDEMk3FmVc4YZXAJKbo4mjAWqs8NByUewHBdCyEqGg_dnU2eJVxlX-VeT_q_2wNG0IMiB6U6PBabIuMniFGAUb7pSE8b2J6hAX2V2a410GnrNJpTxj1ZD94PrIS5gzO29TUEwLTRkAap1lKfKI7Tp7V-JVVXGx2l1VArj5sHmil27Mm0UNIgf4c1PA2mZyKB7Z8kxk5XaYmqYP_1lbCprdb2xnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی محور هراز پس از ریزش سنگ
🔹
مدیریت بحران مازندران: محدودۀ پنجاب در مسیر شمال به جنوب محور هراز که شامگاه چهارشنبه به‌دلیل ریزش سنگ ‌و به‌منظور حفظ ایمنی مسافران مسدود شده بود، بازگشایی و تردد در آن به حالت عادی بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445948" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445945">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd491fc278.mp4?token=VUmSYXJVUDCPeWIsk3fbPvUQGNv45J4hGAWJxtfirNI_8HzBvBPTum_HwQny6KJXAxJB1N55nMEmzcv1FP6S5hbqV6mV7CyO7iDhOUPI3jvxhf3Hoq1R6SlX6UJZmTpyFxXXTpP1hvbnSeqOiWoBikccGOkHxVeiiKoltUBHySWq85Fezzh5k8-lfxrIaYcw6BQhLX0e1tKF5r_bfM_u2qb95C_4yMVdsP4a8lC_SNDu7-nxXajbjDVOQXLVX3mdgWpqg4-IgRWpbY9ksK3g6jwJKxV4VD-HEaqoI7z7iEvCc2rYil6N1j5M8jar4syrzbno7kcb3a0g68cw6Q-w6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd491fc278.mp4?token=VUmSYXJVUDCPeWIsk3fbPvUQGNv45J4hGAWJxtfirNI_8HzBvBPTum_HwQny6KJXAxJB1N55nMEmzcv1FP6S5hbqV6mV7CyO7iDhOUPI3jvxhf3Hoq1R6SlX6UJZmTpyFxXXTpP1hvbnSeqOiWoBikccGOkHxVeiiKoltUBHySWq85Fezzh5k8-lfxrIaYcw6BQhLX0e1tKF5r_bfM_u2qb95C_4yMVdsP4a8lC_SNDu7-nxXajbjDVOQXLVX3mdgWpqg4-IgRWpbY9ksK3g6jwJKxV4VD-HEaqoI7z7iEvCc2rYil6N1j5M8jar4syrzbno7kcb3a0g68cw6Q-w6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از وقوع چندین انفجار در یکی از مقرهای گروهک‌های ضدایرانی در اربیل عراق، پس از حملۀ موشکی و پهپادی خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/445945" target="_blank">📅 01:04 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
