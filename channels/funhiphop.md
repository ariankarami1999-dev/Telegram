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
<img src="https://cdn4.telesco.pe/file/fe7zuIXW4-1Taw7Fh9wd-BmMrI6_JcLaEX1sHH2nexdbvIfyeLIqk8cKCKaoN6KYk99QsJ6ChkqwP8gc5HphuTFZQMmvaTDNSxDodXVQ7dFEKqOIF3-Z8QbLj0ueOcKRI5N4TakGJQ4F25uUkmUp3O4z2j49Z9NyWSgD-W3sI4k2BRmJFCqpVWim3Q5pB-tugdhgjtNBEXFd5z6eLuEXyDgy6OsY65moca9tw_a07qPDsv3OqIYSuKQ4YxbwHdH6ErTBKB8AK7JGxd-nBUaquwE3csGNxForoLvvgkfW2SW70YbhQrbUHTNaGKiXm71ZHwwnuSjHBx9Atj7w3K-MUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 256K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-84403">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=Zx5xwCHgG9pCvcUY6gUIHJITF0w4P0fdJkub_mVld5MaZAqPNLAtAV7vAy3v_-gQ2iUvOrEpKqAg5PAdFtX-lSYkEAaS42sMoIarx6ZYm7dv1wjs3xFa_IKVummuumb7nztWSLeEVQUCEiUXfSYtkeA9-VfPyvU1uDg-w2ctdzKLbJLbQaFYn6lK8xUrLgr5h6TiLqM5WMfNW_UV7S5RU_hANjKsOI0_XPb76moc3Pum1s9mf2aS_T7dFKm8L8GlHUpBcMNvJPrhvIFUgALFB6nm_4dACWeV6c7wMlH1W5-898B1gIWoStheMNaP_9Z_ButQ-8NhfxfJMmwMo9FHWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=Zx5xwCHgG9pCvcUY6gUIHJITF0w4P0fdJkub_mVld5MaZAqPNLAtAV7vAy3v_-gQ2iUvOrEpKqAg5PAdFtX-lSYkEAaS42sMoIarx6ZYm7dv1wjs3xFa_IKVummuumb7nztWSLeEVQUCEiUXfSYtkeA9-VfPyvU1uDg-w2ctdzKLbJLbQaFYn6lK8xUrLgr5h6TiLqM5WMfNW_UV7S5RU_hANjKsOI0_XPb76moc3Pum1s9mf2aS_T7dFKm8L8GlHUpBcMNvJPrhvIFUgALFB6nm_4dACWeV6c7wMlH1W5-898B1gIWoStheMNaP_9Z_ButQ-8NhfxfJMmwMo9FHWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواشناسی یه بالن فرستاده هوا یه سری نگهبان معدن فکر کردن پهپاد آمریکاییه با برنو زدنش.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/funhiphop/84403" target="_blank">📅 14:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84402">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3FeGyi_AhR9xdC1slgN6rqNG7IT-byXZw4-XCI2F84Ipg8t4QvIWMOFmh2KkMJqRzG77ppw_frZqTFPAvOdJLXpRRf_bUXq6c4tm4KNvJrp5yMmqkrVH_GjjcJKRYG4Ev1CDjp4ulR_7G0Zsd3Mf4dLA4OdYL7g0janSzcQPk6ImyW5IbmDaBbMcmpTZT_jUNQWFymyMb82AV4dfis-qr56J-39dIxAnxK4a6HLmwdY-VUiyBeJQIr1lihqNQ1YZ_uKsAQycDaN6x_z7Bw90GnOjHGAaCVIia3b7Q_E3O0StpGFW3hjgsaAd3kgavFXxukGmsaN8mcmdIR5-RUj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی تو ایران هروز شوکه ات میکنه...
دو خواهرزاده، نسل دایی ‌شون رو منقرض کردن!
چند روز پیش تو خیابون آتشکده اصفهان، یه مرد میره به طبقه بالایی‌شون که خواهرش اونجا بود، میگه صدای سگ‌ تون ما رو اذیت می‌کنه.
ولی اونجا اوضاع بد پیش می‌ره و دو خواهرزاده (متین 29 ساله و مرتضی 35 ساله)، داییِ خودشون رو با چاقو زخمی میکنن.
دایی چند روز بعد میره ازشون شکایت میکنه و این دونفر هم به بهونه گرفتنِ رضایت، وارد خونه دایی‌شون میشن و اونجا انقدر بهش چاقو میزنن که کارشو تموم میکنن.
تو همون حین، زن‌دایی به همراه دو بچه‌اش (پرسان 6 ساله و پرهام 12 ساله) از راه میرسن، این دو جانی، زن‌دایی رو خفه میکنن و اون دوتا بچه رو هم با چاقو، می‌کُشن!
در ادامه هر چهار جنازه رو به بالا پشت‌بوم‌ می‌برن و سعی میکنن با ریختنِ آهک، این داستان رو مخفی کنن ولی نهایتا پلیس متوجه میشه و دستگیرشون میکنه
.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/84402" target="_blank">📅 14:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84401">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قیاسی سهیل پرنک رو دعوت کرده برنامه اش، سهیلم با همسرش رفته، اونجا گفتن باید یه اسکارفی چیزی بندازه رو سرش بعنوان حجاب، سهیلم قبول نکرده و نذاشته برنامه رو ضبط کنن و زده بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/84401" target="_blank">📅 13:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84400">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Winter Is Coming
بابک زنجانی: زمستان سخت در راهه، اما برای ایران، احتمالا یخ بزنیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/84400" target="_blank">📅 13:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84398">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhUHP-iNtJK6cSOCXOSp3cXt2utMzVPdQFRHkdyXRobCcg1xjmXz-7MWIuhwKJ_1fSbOSGpe-imPgvi66iMZTCigEnXUzRDz5UWf4535GBRicMe3fcAkjbI5bzwdSa0wV-igDjSarh7KsEP7oxkR8q8lSqurzBh3a0YPT-LfllG6PddZDdtQZKnPuuhdWw_P-p2i6hXwOdXWXI1dwx0e25PicNnxDDHZMkB_Wtcz762eFuzvmqpA9F5cA0_36Ug7IxhRSaRowrTfLHclV0-iT4swrJw4qaWX0FLr2plG0ZB_5aTIvKB4Lp1nuyeBvKHiKLy5wzv0b9cGWYGxx2vYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظهرت بخیر ایرانی
-دلار:۲۷۲
-طلا: ۲۶۶۰۰
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/84398" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84397">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=jdPRoSaMLEbK54xI45YwgqAeaxWlZqoJe9awufaXFK8j4ilUy1losXiwtC9rc9COcO0IqySazhlfhzLqDQZJ7TiLHQBETOm-qKsCtREva4aQohjTYyQHDErlbJWx63nk9NE4a91oIa2CRaM_4dehv5-xVi5s6e4gNj7HMReu-4NB-XEQc3n2TF_qyjVjao5T05wharAUMpZBKB2oxgeVRt-hwyz9ygb-JNGOkXtrJiSWCpBi7jb71DgDDyg0D94tqtSfUV9KXdNUEpXbtRb-PXJKxrJRHI-teARauMY8HkovPCwxWh4FAFv3WqClODm2EPuhJ4LIwjeJgWqHoXFV5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=jdPRoSaMLEbK54xI45YwgqAeaxWlZqoJe9awufaXFK8j4ilUy1losXiwtC9rc9COcO0IqySazhlfhzLqDQZJ7TiLHQBETOm-qKsCtREva4aQohjTYyQHDErlbJWx63nk9NE4a91oIa2CRaM_4dehv5-xVi5s6e4gNj7HMReu-4NB-XEQc3n2TF_qyjVjao5T05wharAUMpZBKB2oxgeVRt-hwyz9ygb-JNGOkXtrJiSWCpBi7jb71DgDDyg0D94tqtSfUV9KXdNUEpXbtRb-PXJKxrJRHI-teARauMY8HkovPCwxWh4FAFv3WqClODm2EPuhJ4LIwjeJgWqHoXFV5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/84397" target="_blank">📅 12:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84396">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFVahtAJByTNjGfWzaWtve9dh4Oczu4kAMcdUcas4WA_mRp379cNF_38MTgyDvhU1GllBYY885yeyh2OgGVZuAWBsJ4wKQDNCuAyst5gCHv-vgLlqMvRrw1dK6aXAYBLgMaBEwvgq1MMDamgd7HhOs29GpSAzsr61XsgNsZD9Da9K7-GKhdYTg9Q1Nxgf6HvICqoW7eoH6Z87t8Ps0ZKXG24hmYlsrL3SyC4beBMygzJhhw8Z6i5q4wHe_mNjs_0RwUmNR68AwyAm9m497ScfCfDAAeKG8UzhSXWI2pjA1af-jf1AsSY0pUkm19ClNh29Y2VjjmbDnLTtPE28RHIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
روزمون دراماتیک شروع شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/84396" target="_blank">📅 12:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84395">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8EsyRbUuENhBLQUD3oVVI9EcH2iVnTsxLETWCNpl-Wn5fEwK8GPjxVlVHa1zLlovhgjQXA_3G6bLQRPp_YNAoifgFzVwVIaFFTbJ8-dc22xIa6Lk11D4e-iKIhXoC5jAC4xcIxy2FG9powrFQlNXEpWs2x7rRnXMVyzxuw9Y6b8KoOzalItxIF5Gmvr2WeqLFHsD3jjnA8-PQvBByxWTB1Rcg39sHBAEJ251_Aq3zfE7_aBFhA72Sa20SZyFBCFIeQcALHvbpOIVg2vM5SsOUNOye1NffGN4KzTDlIir8IHhZIieByvSwKZpAFICHpv7QTxVNvGNduJclg9YQeouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشین جدید ایرانخودرو به نام 207 elite
قراره از این به بعد اینو فرو کنن به ملت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84395" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84394">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/84394" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84393">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ0JkFmocF7qIiE4JHWLp7DPU96h6l7QAImVEnw3GOhMon1p6J7tiq3sshvefva224PdBTqZUJstyupLc8Pvb5K_V5ns1s07yRerAwzNM8jDpq-6vcWrzBP6wDv64edKBtwDQSlinb_hwr_IKn0OlH5vJfL02Eul9bPFJmX3uup7AsEHrc0RiHb3cRMdV1afOT3VHrulmkq766feP9Tje5iCUPBE_oMoKUGbNJvxR8bZrDiwPB5-UReONtN_nZL8Kraj063dxL4siJRhjGNXsBfOd_uVxI_qnYM8ci3hYoEhQyhm25FKvZ9FAo32MKp93HYE-TqcaJaNPUAH8TJcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - بلژیک
⏰
ساعت ۲۲:۱۵
🌎
📲
رومانی - سوئد
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R12
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/84393" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84392">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=Vx-5c8ZaPrltyC6x0qvPEFyyyryliy3enhMspD26EPz590263CROqCz82yXj9vHVNInsRd71ZfLqczynkSMywJLlpKjpdQkNBQvxqnYZ4jqBow-N1WmZmjxplde7WFQd8mDgQJwucMojScCk_cyunxJitTPxeaQh42rdyBvFqQKkYfbqHkJE1d3WFiv-Xgay6TCnjuOPmrKbFtKUWkmdt0vTtgXi0Rkg4ZHQHNuE_2aqYnKYnEVC1nfJ8yu49u2pKMVUmWGaxNFEN3lTxotAxcI3WjAHoGOmTKY2gMdQvJOOHRwQnWle_E5TJGOzioD0e1SfBEpu-MVEUkg3EW3BnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=Vx-5c8ZaPrltyC6x0qvPEFyyyryliy3enhMspD26EPz590263CROqCz82yXj9vHVNInsRd71ZfLqczynkSMywJLlpKjpdQkNBQvxqnYZ4jqBow-N1WmZmjxplde7WFQd8mDgQJwucMojScCk_cyunxJitTPxeaQh42rdyBvFqQKkYfbqHkJE1d3WFiv-Xgay6TCnjuOPmrKbFtKUWkmdt0vTtgXi0Rkg4ZHQHNuE_2aqYnKYnEVC1nfJ8yu49u2pKMVUmWGaxNFEN3lTxotAxcI3WjAHoGOmTKY2gMdQvJOOHRwQnWle_E5TJGOzioD0e1SfBEpu-MVEUkg3EW3BnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتش سوزی در پاساژ خلیج فارس عسلویه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/84392" target="_blank">📅 11:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84389">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پاشید برید مدرسه بدبختا</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84389" target="_blank">📅 06:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84388">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSVWO2NLXTE8QtVGmnFye6FxdCSd1HQMM69Q_mHbIMmOuRxZ_aMYxsxPbUJKZ2h8FA9Tr6e-Ghd5_A_3f17sJrGkCXWHGeQ-qvimqh3A8AFL9HvxmFqGpwqFk6p5ygfGAOwNFhy4IUWUOxwxHYqkvOW4hWrg125GSRWADF5FHwbwMmZL7_CX8tFUb70ac5HVPnwIZUi2L8uoH_JjlH9XclWPz4da36gGhZuY2hO5qJW2bMJVkOcpZo40jDQ1g5LBpXOm_pe751af0Z3JweFbv90vy9UAGCvFWxEQox6tp7wVRQCcSCi3NjHZsN2sSSA7_JF1EDnPDFMU4GFUHchhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۷ دقیقه نگاه کردم اخرشم نبوسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84388" target="_blank">📅 02:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84387">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFshw4bhdZ7bZQek6Sbp258WF2maY0IgcN6hmMkwP22H1HPNXLD_QBHp1YbdtAMtVzrzac5h63osYaJUwtqsKurMJQLct3RgXdukBPhVX7AA_1oqYDSy_5bTX-bAkRt6zTiGpozLpP4vf5vv5MxFoMEz7QzvfFdTLdSqqJH0ewoJfk3n4KbauhtK0BpOc_zzDngPN40GpN48_vUa97nRjSbiSwZ9cWyz25A6xP0mK6-pcr2dCQ6NB1WUs5EyJHPtcPuRrB0SAdp7DSPhYacGJYJA9m7zQL-uJyY1djXmSCrwyNcMQ1-CEqvMKE8UvOojfmm4u51BcmTa8895WZRPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84387" target="_blank">📅 01:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84386">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=IrjN7_sow9saThdSKQPqIqBhYq6Js2H3eYrAcOLO1ME7qfB5GV-W2gct_ihDusvjmtpzaSGCEuEB-GRWVF2X-w8NKnOHEgq7FIH4HKAY2KllzCa1Mnn4skI16-QRiO11F5Qi0YgI3Ciwe8PaZTu9TWwsEKlzgSl_OxLrkjczFBdP1lVkgriCJTHlbuc41orqQEYpQhxSjamf1bOmVsiCXu175dhA64l2KzdAhWMCRsqAM_UDZOqZs4zhc_fVAycTgOxN72iim6qa0Zry75szyWYJmsVvHzPLGdZsJX6SyzT-8zsFueRdOscLiigliBQwSFZ14GpbNsPpONnaQMh3jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=IrjN7_sow9saThdSKQPqIqBhYq6Js2H3eYrAcOLO1ME7qfB5GV-W2gct_ihDusvjmtpzaSGCEuEB-GRWVF2X-w8NKnOHEgq7FIH4HKAY2KllzCa1Mnn4skI16-QRiO11F5Qi0YgI3Ciwe8PaZTu9TWwsEKlzgSl_OxLrkjczFBdP1lVkgriCJTHlbuc41orqQEYpQhxSjamf1bOmVsiCXu175dhA64l2KzdAhWMCRsqAM_UDZOqZs4zhc_fVAycTgOxN72iim6qa0Zry75szyWYJmsVvHzPLGdZsJX6SyzT-8zsFueRdOscLiigliBQwSFZ14GpbNsPpONnaQMh3jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رعد و برق خورد به نوک برج میلاد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84386" target="_blank">📅 00:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84385">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پزشکیان: نوک قله ایم و نزاشتیم فشار اقتصادی رو مردم حس بشه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84385" target="_blank">📅 23:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84384">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=gVtsQVI7Ylv9Lh046Vc0U1pRYykec6ehKbm3Gahv4A6BZzwLkT_rf4QIudK9Vah-1mwJIZ-sACD7I8-2pKMohWuIadPKp4Qh8_GSRgAgNgtNwdwEKrsXgA3DJ_uo9F1UYLaQ7Dswcb059-Rs5FWyyhxdWPEcQ1Na4Ts1eZksgqA_ebMHt-QhjIicTUiYwDsVCclwYTAOYm7L_ZHUtotFaecFEfuuyNox27YeT8kCSZ7rfIRM31n_GryZnktM72h48jOypk69nZb8KCSyicq_S3jL3lz7Uo08Ra_oHMNzCBzoEMcy389fOkkNpDWnIrh04o2Wt3jO3OhdTOKkqkGtlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=gVtsQVI7Ylv9Lh046Vc0U1pRYykec6ehKbm3Gahv4A6BZzwLkT_rf4QIudK9Vah-1mwJIZ-sACD7I8-2pKMohWuIadPKp4Qh8_GSRgAgNgtNwdwEKrsXgA3DJ_uo9F1UYLaQ7Dswcb059-Rs5FWyyhxdWPEcQ1Na4Ts1eZksgqA_ebMHt-QhjIicTUiYwDsVCclwYTAOYm7L_ZHUtotFaecFEfuuyNox27YeT8kCSZ7rfIRM31n_GryZnktM72h48jOypk69nZb8KCSyicq_S3jL3lz7Uo08Ra_oHMNzCBzoEMcy389fOkkNpDWnIrh04o2Wt3jO3OhdTOKkqkGtlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر بیژن‌ مرتضوی: به جای نفرت‌پراکنی بیاید کمک کنید ما بتونیم از پس عکس گرفتنای مردم بر بیایم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84384" target="_blank">📅 23:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84383">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">توپ طلارو واس یامال اماده کنید</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84383" target="_blank">📅 22:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84382">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گورودن با اینا حرف بزن نزنن بعدیو</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84382" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84381">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXHqMnAZKnvmZgfgcibtotMUAuOcm5v2pkdrqWyV6eaPRqKz5jf0zMQHlYmqkFsh-4vMptXMnUP2S7YdCKYUKhYHrIy3SjpcrGvKUR_hnnBMmraLo9fTMkA4oVkG-njD6d3BLQLbx9xzXPXMvRYjc06su3j5AshKOx0e53Sds6ouTgkfqy-ndOdlFJ1hgMJY_9Zzmhxx-9i0ozcGE4jzkaYJfCObolCg9Shffi9S-WwcOqOD_P8vbVjgNQCDkI-PJ9FZahMhYRfB3OXKLuMFHLB_tG9hLhXMYQqC1DNL1YN8LBnHDy_xj-9yMoUDlurDhbelS73vJPLifpJHICodww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته های سردر اتاق رتبه ۱۳ کنکور ریاضی ۱۴۰۵: دوست دخترم مادر شد من هنوز کنکوریم.
پ.ن: بیت بالایی شو هم کونم نمیکشه ترجمه کنم تورکای عزیز تو کامنتا خودتون کارشو انحام بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84381" target="_blank">📅 20:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84380">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بلینگهام داداش لوییز انریکه رو میشناسی؟</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84380" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84379">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YedkJHb9jPYv_BFjLoLPbORNek4AE9CXCOW_Z6kAqKTXQdGwJNms3MacbOomGHFeibqiR4cIj2YKbO-X6fx_Slhwkrn-4sFwaM8nY1V2GGiFiWepKy2sBvwLEyUoqT6ohI4tV12pKxh7xpfDOZXPYnhfoidG2a5lqBH_1zYtgbpEwy3zCkfAWin4g2V2mtKDSbFCc1Sl1mno2CPk7TJ_EHvo01IfiAHqAsgIniN6bDAnc_bd9-2OBZPWexYSXREjO8akYlArWgx2WJcitbESblUdZz00EUal-MQIuEKEatpOYr_ipZrzyJP1EjTM_q6534911KRqqNTgIn9FIU79xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84379" target="_blank">📅 20:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84378">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترکوندی شیر
به دستور بانک مرکزی، نمایش نمودار قیمت تتر در صرافی‌ها متوقف شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84378" target="_blank">📅 19:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84377">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=bQxZiuELLBTBwkzWh7zPRRBmnmo5gzzS77SBOHYEDHUEfbM2sFRrChVotR4kOZnMpDyDoVAaFS1SxnU4PeT8snVOYlcCyhW21boXkDnBM7TivwVFYaDvIfXSPPReMC4v_DDJdDfKJeCferYtTAWwYUlFAYIajUByR9EsTRMVWnN3LYNrDG7CYcgdydFZHsgjsuGjharJUPaugm_g8GKxUGa1ejodmSgH2w_Tjl7kvSyCYeVEumY9YpyslFEge1WCa_kcjv0kwnVbQN6dSq2cD98r8FwO7nODeDTuZLCNSzrOhftat-gXmgsZmORBm0EiB4AvUeaaiYCv2XJZq3pvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=bQxZiuELLBTBwkzWh7zPRRBmnmo5gzzS77SBOHYEDHUEfbM2sFRrChVotR4kOZnMpDyDoVAaFS1SxnU4PeT8snVOYlcCyhW21boXkDnBM7TivwVFYaDvIfXSPPReMC4v_DDJdDfKJeCferYtTAWwYUlFAYIajUByR9EsTRMVWnN3LYNrDG7CYcgdydFZHsgjsuGjharJUPaugm_g8GKxUGa1ejodmSgH2w_Tjl7kvSyCYeVEumY9YpyslFEge1WCa_kcjv0kwnVbQN6dSq2cD98r8FwO7nODeDTuZLCNSzrOhftat-gXmgsZmORBm0EiB4AvUeaaiYCv2XJZq3pvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چرا هرچی خز بازی در میاره بازم جذابه، خسته شو دیگه کصکش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84377" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84376">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حالا سریع و خشن هیچی، باز خداروشکر از دوره ای که ملت با سری فیلمای یوری بویکا فاز میگرفتن رد شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84376" target="_blank">📅 18:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84375">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwTP5bOPhP5kL6dsiTO8h17W8nsZeQTT7k6WmY15QRx07G5G-NaOmevA5-rjlKfl2_chBjXhYSeERmtjX82y5Og5c7LJQ7cxqKbv0DfNul87gA4AWSayJNqpAuB7XaMTafkuOKYOn6MkBQS6TZcVUooUQsUFUEoHlSpgHKbB7Y6WI4aXDv9MRrRF3vXq5SpBffpqduxhS8_76cEIBb_jO50QQBDozgY1QHcF0cKjI7BWvM9byRkIeaHfY5ClKZeZN6lRLvePnqyn1dC6LfCYoXEW2pIp006uTPlIJiWNX8GwZYjxu_SlIhj0MHU8rSYq668TsbcQWGP8lv-wwwWw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شید ناموسا
سریال سریع و خشن در دست ساخته و ۲۰۲۸ منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84375" target="_blank">📅 18:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84374">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=rVyb0dzNXUXB5YDIhbOCSXM6MGHy1B8XsMkVRlFWlI8TS5GNxc-4NjpS7ffA6FhnETsmeNCybU443Z-zRqs9fmCV_9YzNcWV0RTaGnnO7ZRdbux-ImNbA7WWwHXZ3pd_TQEB_yqf9GvAsg6MWoSGkWoa7bLVIBQ9s0zWp__cGF-O6GBuIAstub6PMavL4z4XLxJom27ralDPJ7ZybkH8vorxJLdRxCn94P1hih__Xv_iEpejZ6_M8dDMAOor329zlS5n_pMoWlatpniM7bWQskDDvdBAGWZMKo1zZ6n15GBJWI9iXbi2PWt2Fi_Od3bDBqyczXHfhvi2KF9mYWiQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=rVyb0dzNXUXB5YDIhbOCSXM6MGHy1B8XsMkVRlFWlI8TS5GNxc-4NjpS7ffA6FhnETsmeNCybU443Z-zRqs9fmCV_9YzNcWV0RTaGnnO7ZRdbux-ImNbA7WWwHXZ3pd_TQEB_yqf9GvAsg6MWoSGkWoa7bLVIBQ9s0zWp__cGF-O6GBuIAstub6PMavL4z4XLxJom27ralDPJ7ZybkH8vorxJLdRxCn94P1hih__Xv_iEpejZ6_M8dDMAOor329zlS5n_pMoWlatpniM7bWQskDDvdBAGWZMKo1zZ6n15GBJWI9iXbi2PWt2Fi_Od3bDBqyczXHfhvi2KF9mYWiQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دست این پیجای ادیت اینستاگرام
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84374" target="_blank">📅 18:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84373">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">روسیه: به زودی میزنیم پایتخت اوکراین رو کص باز میکنیم(
چند ساله میخوان این کارو بکنن
)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84373" target="_blank">📅 18:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84372">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aySvMuiukOi84XB777aclXULa5yw0RRF9Xud-GNg3o_dbsSzlezbd4bGAWTsPezyQdYorhQDf_c05wlVtUgOQm2AkMEHG2IOmhAHMkriQPVz4w0NzUcY-UGsmvENeMpbiOzwW2xmgl1ns-7yxquSN1MFvGBBcmdDBclh77YoS0MkjYWLE7YKB9nRdNoZO1PtUKBluxfAGh0TU7e79CNcKpyhnzD6fiduCBWZzS9-XguBxvJ72mPKLG_9gT2O94aUrU6aA_7k4MN-jsNroVD9JNwhxiPV2hyZZ1Bo_zPjX3EkacjYTeoljYy35olPVCFT5LjrPKeDvK5g4QM0BeImnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا منم با این تصویر موافقم، به نظرم قاف باید برگرده به خیابونای تهران یکم جنس اعلا بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84372" target="_blank">📅 18:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84369">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عجب هواییه پسر، امیدوارم عشقتون تو این هوا بهتون زنگ بزنه بگه ما به درد هم نمیخوریم خدافظ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84369" target="_blank">📅 17:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84368">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qts9kM6_tdn5tNvUeuuq8gADpXjGXxBHH-M6yYbnkv9pWZ_q8v0K1CC8bg7-gtmO_Aq5k0IT2cipo8rXcs9kZ4NqcVTYBp9hTqocy1F79vQOoiKpK8yhS_UeQAV0XBuM6xfjuOmvxytdEfhYUO99FPiYBV3IupwgrS3zGGOx8A1HSSvNt5rARv4n0pBdcxet7i-uD7fPu0Yuzsau5mpZFzf2ptPwkkcRg0f7YjBOK-mikjCGgv5mopbe60cNG3_nCsWCDUVr-iKXELzBEbxqn-us0MOZeM73ueo9VwuixEhR1Z_vxu9g9K0uc5qoZYIBK0UqMNIK-RIx4G6xmPFuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال the gentlemen پیشنهاد میکنم ببینید فصل هم ۲ تازه اومده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84368" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84367">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اگه مصاحبه فرهنگیان دعوت شدید همین الان بلاکشون کنید، بعدن میفهمید چرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84367" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84366">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این میمای کنکور چرا آپدیت نمیشه، هرسال موقع اعلام نتایج همین میم ها تکرار میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84366" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84365">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84365" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84364">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk1iyzdtE1orgX1mY5GhF6y6vdeH8EvJCdCO3tS3jcZ551WrC94Vcz6RBSHTYlwCb6nH4dz83qMqOUE3uIRMgvCtayQvDbSr3EVB8s6swUvkgllC654eCPBVGU1dijpjpCUTlxR5gpS67foCUFPvTM_4zFzfQaHTnM4ugtFt_H3ZF0ZrFx6-0_NWMIsYC9C3-WxoGEmOaP7L_LFYUcqyZmfpmxwXJLNIAQhAC7HVmkhANLZllEYR8XoAkxV6QF3pBg4I4fYa0Bgf1EPww0pBs8Ot0JfV7xZkP_fKxkG6hUWJpKn-83W9fjR_1YwACRxKAa9zv99G9wgsV90CwmIPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84364" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84361">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ik-7VwS5QIswV4lu78894fKwVT9gmZNWaFQES6vBH8iLpp4oCjS8RxZ0KoLVGlpAiCPvvRpa6E-xfQZVmSxIJXupca3pGOEZ9bCFXdd_in11YIeyot3dfvdckkvJLop6CMOhsHWKdWRhklsGDzdD5FF6hNluAdA-Mt_KtJYNQ99SEyfEpcG12XVWIEbUirZPeGeD2oFdC5SrFN7_RZrQ_LzPdwdzYGwVM9-Om7IJGqjCL6yNqEB4Kv1AXyBKwHH9qnhi0zKjQJiqgyRfqW1z32WLbzPHxVYFVtUtP0euOnsk8mjsS1uk4oAH9ngC0THwatonM5y_Y74s2micpTdLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84361" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84360">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTileKhersuk🐻</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO-QHAn3Jm2THP43KwfA-ohm1o4BzWt-M4DvQT00cEomeoKgwzHstW9TTOBy7COTQ2dD29MAIZkWoggiocJ1SrCOvDcY7eSHcbQ18NzGpgJZEGiDwwqTD4R663Dn-OrOmpWLuFgbfHlAng2CWh24AoRl4p7mrdtAWXaDakqLZQ3PCBCqQURsd4DCG0GM1FH3wFJ8Wgj71cOklz37lj7tD8v8OJmB3LddtbY4xSipHryK0jY8VaYXMKdC3uiT4HMAaPB2vZiRzCcykHjxU82GYRjwhIcm5OhIZWiN4Xo1kbo5-xpLBKq8lj8ue-xwSTk3f6OVrvIW_L6v6dguYjl99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر خوب</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84360" target="_blank">📅 16:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84359">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتایج کنکور اومد
بفرستید ببینم چه تپه ای فتح کردید</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84359" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84358">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جردن های تولید اسلامشهر که مسخرشون میکردیم هم دیگه زیر ۴ تومن پیدا نمیشه، های کپی ها هم شده ۱۵ تومن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84358" target="_blank">📅 15:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84355">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بسنت اومد گفت تو دوماه آینده دلار ۳۰۰ هزار تومن میشه، همتی در جوابش گفت آمریکا هیچ گوهی نمیتونه بخوره
حالا دیگه خودتون حدس بزنید تونست بخوره یا نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84355" target="_blank">📅 15:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84354">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستان استرستون برا کنکور رو درک نمیکنم
کنکور فقط قراره انتخاب کنه یه بی سواد بیکار باشید یا یه با سواد بیکار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84354" target="_blank">📅 14:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84353">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LJqsPp68bqq9CnFhwhQ9aLH6lhmPtdYsj9JMkaYg3lPh5MhrGzzMOX1y_LgXrPSHA1FveX-5FNgpo8yP0XhmZMuymHsUgWDuy744QjlSpvH4Earu8Xm2A6iNght0Hu5bh0aAIrrgkLl6B8JD5p5dT1C89g13Y4c8ImDodn3JGSkc57bg0mCJqyz_HsZH-AbDjSYJOuoIjJfNINun0Ymz-WxALci_phdfvLTJ5z8qgu3BEaoNZbt9dNjRL8m6_pvUnSDmC0ffy3P4ZstUVGLm6uT8T2NiMZHTQezmHJ15VwAQ6CkL7MgvQQWN6dbV6m371r-WgzNf1kyyRODPq-NDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنشنال یه گزارش جنجالی منتشر کرده که میگه یه جاسوس موساد به اسم «مهدی نادری جهرمی» وارد دانشگاه امام صادق میشه.
بعد از یه مدت وارد سیستم حکومت میشه و انقد خودشو حامی حکومت نشون میده که بهش اعتماد میکنن و نفوذش بیشتر میشه.
انقد توی فسادهای حکومت و مالی دست پیدا می‌کنه که دیگه از موساد پول نمی‌گرفته و حتی بهشون کمک مالی هم می‌کرده!
حتی توی یه مورد به یکی از نمایندگان مجلس ۳۰۰ سکه رشوه داده!
طرف توی انفجار کارخونه موشکی ملارد، شنود فرمانده‌ های سپاه و نابودی برنامه‌ هسته‌ای دست داشته و در نهایت از ایران فرار کرده‌.
و یکی از مدیران اصلی برنامه معروف هفت هشتاد بوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84353" target="_blank">📅 13:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84352">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هروقت میرم اینستا میفهمم نسل چهاری ها بیشتر استعدادشون تو بلاگری بوده، شانسی رپر شدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84352" target="_blank">📅 12:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84351">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیگا ها و فلسطین فن ها فرانسه رو دارن بگا میدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84351" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84350">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG4Pw1LVcJU27U8sBkgkqIMMRohkLnn99_mZz2g1zYl4_pzpDbM61sF5GKI1iwrJBrbXynP_ML12Y_n1xiId0bWbT1RPPrSOiZI8QnfKag6Ryx83cap8x13mDSRlH4hvcKkD6EBm3F4Ygc0HU9zG7hJHKrMYY9F2ioD0Zw11S8aA5SfB05HUiIncsGlXM33oSM1DHH12bk3Z-ft2aeo7qNv_JBBbuM9h-hm21qmijJD-4iA7L7Of8vTbzdw0T-frHt3qr35C4VK5Q1yotoEmoLBiuHJzmi-wdjE2HbdHMHmMMWAztvHXeUq6eQ9eksfH2kphA5e0EgUDDy7SFJwE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا کیرم تو این اکسپلور
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84350" target="_blank">📅 09:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=orOV2WhzXA1i2cr30wPLebpjyrVOo35X3ao7nrUn9yjqbnxErEy4o7xarl1GyqpJ-MuDqzduGKuQpM9ie1UErNdrRkx5Bbz0bgpfvCPtRbN5faOnbBxkSUTHFJ3IYqGdcTXlwqy-LNh3beNcsfoOKpOrPdYrI3Zp-Rznfc0znbdGghP5662ImOFpVCJbkYFWzudie30j6ACyau0PiOZkdb8H6wMDm6DGrrmf3iWuZTbEWKHuqL0tFx945J1siiNiEbogk270EUzTm3Vbb6ThJTICgGjFhTzwpuoKhMVYfE6nBDB5Mnq9-Co-9JqBNvaWvEKC9YwrvaLOc1afeWaeuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=orOV2WhzXA1i2cr30wPLebpjyrVOo35X3ao7nrUn9yjqbnxErEy4o7xarl1GyqpJ-MuDqzduGKuQpM9ie1UErNdrRkx5Bbz0bgpfvCPtRbN5faOnbBxkSUTHFJ3IYqGdcTXlwqy-LNh3beNcsfoOKpOrPdYrI3Zp-Rznfc0znbdGghP5662ImOFpVCJbkYFWzudie30j6ACyau0PiOZkdb8H6wMDm6DGrrmf3iWuZTbEWKHuqL0tFx945J1siiNiEbogk270EUzTm3Vbb6ThJTICgGjFhTzwpuoKhMVYfE6nBDB5Mnq9-Co-9JqBNvaWvEKC9YwrvaLOc1afeWaeuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش هایی از آموزشای جنگیری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84349" target="_blank">📅 08:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84346">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=ujJ-yCC61LwCjqq4YEJr4HUlZBj9GgGH50AV-XNAcfVQziqUH7eQzK-LzPTnilBQylLRuXqLf_fJfCJ-9Ecrb-C9h8WckReP2l8gqsz9Af2plolVrDMQ3tIcBo0-kWcs9nY8NPPJINGCBCrNVgSZEae6bcCdxmhFQrp3VYy42MZAHUkC8BSuWdIxjv2leSssKxrT6wxMsYbV-5GF6eWt4ZJUOK_Db7wNIrcMvbBesbUmuc--5u6zsp8gyLrrVgEWSZP83szvE9Kw1DPsfYH3zhyoKtj8YRVK_2ZBfL5W8XFuP5BDB88VbpDaOamnMPg76tccdyWlNzBPeonNjel6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=ujJ-yCC61LwCjqq4YEJr4HUlZBj9GgGH50AV-XNAcfVQziqUH7eQzK-LzPTnilBQylLRuXqLf_fJfCJ-9Ecrb-C9h8WckReP2l8gqsz9Af2plolVrDMQ3tIcBo0-kWcs9nY8NPPJINGCBCrNVgSZEae6bcCdxmhFQrp3VYy42MZAHUkC8BSuWdIxjv2leSssKxrT6wxMsYbV-5GF6eWt4ZJUOK_Db7wNIrcMvbBesbUmuc--5u6zsp8gyLrrVgEWSZP83szvE9Kw1DPsfYH3zhyoKtj8YRVK_2ZBfL5W8XFuP5BDB88VbpDaOamnMPg76tccdyWlNzBPeonNjel6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز خوش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84346" target="_blank">📅 08:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84345">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUr38jxC9BFF-zca3ywr4pS092nz1kfodqyu2RwAnbTobirV3DDcp9_IlcHWnz2EVPZX8McMqAr9K8YfsxA1iubniKpA_UXygwWNayT7aU9J0sQFvNMLLjUaHxlT4RUCIGrtolELz-Ih7l8UXRxRVs4FtAS-ltRMcv1KOfyYk4bp6xdq8C9cLC7L8cTdOlmNZHg7ONEyBtOgFhjPDOXhS52HK2g1YeWaAoq2fFEQxHLCIXkTN7snshKyDYtAt1A93VKV6jmk2iN85GAy5B4nBiA3phYSmI8z6UHZODC3vTuyYXSzcA8RphSaQ9nV1LTQ_iwr7AuoGtsTB8SSNuBixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84345" target="_blank">📅 01:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84344">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgDqSHGT4U0ljRu4DV9gQXne46JFoQewN-WPC9wuL4Isor9bMVIr5B6VbYWoxJwO_QQptFQdi4Kh2CHczXbVHeCeAtTx6GstO9AgzvopR7-Bq14ElEkC96GQpSt9o9aXTNax74-Kd_EXQ8VD4B806Ucnd0ldCQuSGVEm-Q_Wof6qOuCevXO28RDhJ9bMrOaYE5Y1FbmTpRBPLBnTEkkgQKAqbU3-qC8Sup9y_RI7hz-tLeRFfIaeGh5DazFNM7OCWRszBQ4ybYgperiXKq_sYi2O8jwmKC2WUBTIhI3JO0pyn4fgprBQ0b04ebPPEnP9LfaAgvhGh1bzob-YsoJPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Batman: Iran knight
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84344" target="_blank">📅 22:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84343">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=sATeLC058UlM31rKlBFofK4gjnEZNbA_Wddp9vJA1sbmKiu9YeLQJQUd3PZ021IiYhtnRovkkzNRnQGSBK_qgauULioGcL_K65o-TJ6-fjZ_SLrdwT4k9gMtD5g7iI2N0XW4Lgt7wfQTS5gh9JQgTa3FtB8idRKn76rHhRgWB0LWKPFeR7dtpHx6fep-yPiwHMZJxLsVEGo6hfDR92KjgQDAPFlR4V2VOSc_D8nQjoUyGB3UW5StSTddLPPZlItrmODFrpD4Q-R7uk6tdz_EfNxxJw3_kguqW54QYCa4-O39Xsd0YM8rnLJmmzERpEHAE76jU74cv0I57X7QWs4aQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=sATeLC058UlM31rKlBFofK4gjnEZNbA_Wddp9vJA1sbmKiu9YeLQJQUd3PZ021IiYhtnRovkkzNRnQGSBK_qgauULioGcL_K65o-TJ6-fjZ_SLrdwT4k9gMtD5g7iI2N0XW4Lgt7wfQTS5gh9JQgTa3FtB8idRKn76rHhRgWB0LWKPFeR7dtpHx6fep-yPiwHMZJxLsVEGo6hfDR92KjgQDAPFlR4V2VOSc_D8nQjoUyGB3UW5StSTddLPPZlItrmODFrpD4Q-R7uk6tdz_EfNxxJw3_kguqW54QYCa4-O39Xsd0YM8rnLJmmzERpEHAE76jU74cv0I57X7QWs4aQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو کمتر دیده شده از رپرای رپفارسی که ریلز با مضمون پول رپه منتشر میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84343" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84342">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLpVsqv0hnkk-TC7mo5oXQ8uM36rvoVYjC-2U6BcjkbgbWx5UbE04XBJc6Trf_hyokc9r7caNo7FLy7uOcQmNMq5A5MaVhl12ql-rJcALI1sJfravrU1JWNo1lj7432PjBQfZGNBxgPRaQgrn74Dpw00oYBHykqw65cOpJ3pfCLXZF0ORC3CWXhsLGYEzJDPamHXZ_eyM-wpT_AVc63UE4IkivS5qZffyfBWkehkXU-0hzHpDieMWl54dkN6xSHwufElr30YUV2GrAVDT_sy39ksspY-cXk1iF25MURY7JihTk6rlp2i0xMlZ97Ts7WuEbU8Qy_CTqSlrw4hvWs8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خلیج_فارس
جهانی شدیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84342" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84341">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چه عجب آقا دانیال تصمیم گرفت بعد ۵ سال یه موزیک خوب بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84341" target="_blank">📅 20:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84340">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84340" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84339">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u29jyiSUu1gfBDuQPvob2XufXoRECvgQ0LCEQu3lSywhoQrom1xHcgx6Hzb9-KvrYjLcmGzyLfntr6wLAnqgjE0Tdqx7FF46aJEVBcsE2UjGZbWTT0Yl_u6q37MlO7MRq76pNM20n4hylPMyn-mXNG0EZwi9SbHFayFcCt9Z58DfqsIATtAj0FhO3rfRUeG1znlcvvskCYatAeUhI8tuoXalsMyB2DJVxKFhoQmTaXr6fU5xNaz7S4PzprsaKFOREtvD2xz2H1_oF8xTJevPW2UNuu1Kg2znSxawnw4ePU3VLH_9wDTPEklujLQ17pBfvp5AAddz4O1SWAx9yNyHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84339" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84337">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7ol3t1H6HnVmP847tq_UzfMhGPxoGwj1SchrVbLyvuWU82P_Ee8UXBh_nUJADfpU4KKHrBGEYoM-JCI4A4zyNU-X71gKkGDoOaBjsGHPuOJvaWWuZ_7-mBMZ-Vz9eFJTKM0FDLA1mJpuLdJybvY201so0irsqllDFFXykEhBpT_kg7G08U0sp557H4ZOX8q0oAKMcfzq8GtzoiXAxUbtunbFATaWA1r_wCTE5r4Nq2TmG3RSu5ARrHtrdzfVj3WIZAzQCF3ujA7_1jUs8l9ZbXJv2bi-MdFy7IKqdVAEsryhqX-PyF6vXQezElNugidkVzWR-gvNk5ljpahe3GLzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=uaAHo9vtM4OaUDIlEPcyciwsCozLcop9Pq7QCiOFlJf_5BkpZ9nU1OGYYTjPZ_JL-9fn7bAKuGA1wElA_Nt5KZ_sC-ZdD0iZd6HoG63FloXXwBhRHnRQnvTRqeI7Y2TNal6ajS8vLdXRvNE7thwJkSepEc1C5T03lMTLlyNF8F5ptUBH3081e5Q8Qg1xg5EA3mnqDfdIxkR-yK6tRIZ3Y0Wpy-94QRimHIc3GtqMSbjbp0qeUd5o2OisW1PIX4OJEQV0dR3ac7hWh5ieWzHxE4IPR8Mcqam2LGm4231RZOL8q9vyBTHZrqVvq6UuNClv9L7ldgO0zyeoYDz13yFzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=uaAHo9vtM4OaUDIlEPcyciwsCozLcop9Pq7QCiOFlJf_5BkpZ9nU1OGYYTjPZ_JL-9fn7bAKuGA1wElA_Nt5KZ_sC-ZdD0iZd6HoG63FloXXwBhRHnRQnvTRqeI7Y2TNal6ajS8vLdXRvNE7thwJkSepEc1C5T03lMTLlyNF8F5ptUBH3081e5Q8Qg1xg5EA3mnqDfdIxkR-yK6tRIZ3Y0Wpy-94QRimHIc3GtqMSbjbp0qeUd5o2OisW1PIX4OJEQV0dR3ac7hWh5ieWzHxE4IPR8Mcqam2LGm4231RZOL8q9vyBTHZrqVvq6UuNClv9L7ldgO0zyeoYDz13yFzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها یاسو دیدید چقد متواضع و خاکیه؟
یاس:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84337" target="_blank">📅 20:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84336">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26448031d.mp4?token=AwQ3hLJpXD4B8Kn9mUg6wL5O593xqzbN2DxH6rfdN3KnbWCFoiN7q4O93KTbJ6MpGam9xBF8Ix1qX8l6XPUlY5KL-R6bKR0c-HtuVGPYpJuDEsLyWSwrC2eF-ZCimZUL3F4x2rutIbbYwNeq70w8ptCUqugiYapd2C-Dnx10_biMTTFKzGiONb28uASjou5i_7_TAeKehIhZABqbp-hJ33h7tPwuFho_9uS0Aax3w2Pc6SvRSi4gpd9S45sJ6s9-ijB06Vxxt_FwubQVb3Whjr6soSs-1ws-Gv9WxA2qt9TZW36jCY-ZObeDun2uDiMJgfSCV2GMI46TIaSghPxdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26448031d.mp4?token=AwQ3hLJpXD4B8Kn9mUg6wL5O593xqzbN2DxH6rfdN3KnbWCFoiN7q4O93KTbJ6MpGam9xBF8Ix1qX8l6XPUlY5KL-R6bKR0c-HtuVGPYpJuDEsLyWSwrC2eF-ZCimZUL3F4x2rutIbbYwNeq70w8ptCUqugiYapd2C-Dnx10_biMTTFKzGiONb28uASjou5i_7_TAeKehIhZABqbp-hJ33h7tPwuFho_9uS0Aax3w2Pc6SvRSi4gpd9S45sJ6s9-ijB06Vxxt_FwubQVb3Whjr6soSs-1ws-Gv9WxA2qt9TZW36jCY-ZObeDun2uDiMJgfSCV2GMI46TIaSghPxdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برام سواله یمنی ها دنبال چی میگردن که با اسلحه ها کاری ندارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84336" target="_blank">📅 19:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سلطان حمید رسایی را آزاد کنید حمید رسایی را آزاد کنید رسایی را آزاد کنید را آزاد کنید آزاد کنید کنید  آزاد کنید را آزاد کنید رسایی را آزاد کنید حمید رسایی را آزاد کنید سلطان حمید رسایی را آزاد کنید  #سلطان_آزاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84332" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فان ژوله غیر فان ترین شوی فانیه که تو زندگیم دیدم</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84331" target="_blank">📅 19:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpl_M_E0Zjk9C9I18oP6kcXsUX5w7RYJu_eHOi2hg_IPvmSlNSAZrAJfwwdVfgkHnjN8RbjD8pvvoVrS8McHGoQuV1QFBvi-cv5sfrAnSqXxTnWQErWVJq39hucd4QxVz_g9NbpZSDzgD9bsB9FaG20mDMcHisJBiTMB9MXMWyOaxaaF1VeFfj7tnlH7A7zzZ3UvTYNitNsueyzlZdLdChPFjVglOXEmmoevks1-RYlafVgPJpjpLODYfk7RBBgsBRKwAwlOvbAH7Ddl9OcjY4RYENEMjE2kWTWtUgIkLzAMhHwOQzfmCxUTd1w9P82AW_wAkKydk5aFDsOmnUdq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران حتی تو معروف کردن کصشراشم پسرفت کرده پسر، از این رسیدیم به امیرمحمد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84330" target="_blank">📅 19:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LA6_5YrGdYA5QANHIUWhORmckSB8AN6NUwtEWMq9uLdz8Ppq0fvhIWHVTut0oE9-8IAX29YOWzfYzHJR_CEBRw1lD9wObawsfIPPTAISh1GWeef_tu3jF9GIvKnTlIQq5nS8T5voHJiYEq-DoGW5sqPdm-tBWce3p7jWbLwLE31CECHCeSzJUbgijRcJfrpUnNKp8V4QxBgiQO0-qKWQ-G34IJx3i1lgrxw8jLdCujkD58Vi-WkCeDQuC4qTEsphfVHZs9eCppRgp5cxlKoDI9JmpKoS0TK7BQuUQAGspCwxymZawMD8jeJiLbcf7QVYhYg94EnhLA0_02oZ7XisZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oa0TEOVLxPAd8GSy9nA_iclwUm5kUj4t5RwaVhfFGP6uw96rbKuQxrpydVlTX0e2PFVel0INozaFht7Cz_WuWflblt-U__Mi4tYu7Y0krO-apBFVrkeSWDbSTOvR67xjqhlljMaa4HdHOoY_3DJcuanS6n_jTk2pA7eHVQ3n9MxF8eGuz2cjaf4QFxy8lws5_bBSjB6UH365UB91EqR4iJUeS9g0FQKjWLqY2LTAMLc7OMZZpnCFK-IsKXRXTCxdCx4abOmgRey0TRunKgs7yqb7d9QVtyM2ds-Bo06I3DTCrbsijLDK62MX0n8jYcfsUlihB2ARXyOacIS8MTlnuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترند جدید اینستا اینطوریه که دخترا دارن کامنتای کلیشه ای و کصشر پسرا زیر پستاشونو متقابلاً برمیگردونن به پسرا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84328" target="_blank">📅 18:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84326">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چرسی: شایع اون تایم برنامه گنگ گوه میخورد که من اطلاع نداشتم برنامه قراره از فیلمو پخش بشه، اشتباه کردیم ولی همه اطلاع داشتیم که ضیا داره با اون پلتفرم حرف میزنه که از اونجا پخش کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84326" target="_blank">📅 17:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84325">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=l8v6UXMpUfbmGfdUP1dmB8UengiGbau_pAiAKgU5GXlXl3AYtsoZrTUge2YcVL9iltQ7Mv6zHQb2qX7L_IoE7bn8dgTac3ZWrsYZklMGUXxXjd6009UV014SLhx5UpRdqzVklNq9vijFXMBJIBrkU4Z9SuiorrJFSosmSoDBG5tpc9fpGvtN3rEj8stNdqZQXqE2FnMhJk3vEPssRaHoWTEEMQjqJ4YL4Sj8O1fI_N1Zx1yKvytpIj0RxiVSoN0FmicwzMXML7HxKlKEF5M1xmlU_MK5EvrEGtNWz5kvgBAb_S2-J6Wpam6WJBQdAvQcEC-W3ZpgWyS-EsKkBcqwUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=l8v6UXMpUfbmGfdUP1dmB8UengiGbau_pAiAKgU5GXlXl3AYtsoZrTUge2YcVL9iltQ7Mv6zHQb2qX7L_IoE7bn8dgTac3ZWrsYZklMGUXxXjd6009UV014SLhx5UpRdqzVklNq9vijFXMBJIBrkU4Z9SuiorrJFSosmSoDBG5tpc9fpGvtN3rEj8stNdqZQXqE2FnMhJk3vEPssRaHoWTEEMQjqJ4YL4Sj8O1fI_N1Zx1yKvytpIj0RxiVSoN0FmicwzMXML7HxKlKEF5M1xmlU_MK5EvrEGtNWz5kvgBAb_S2-J6Wpam6WJBQdAvQcEC-W3ZpgWyS-EsKkBcqwUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی خدا لعنتت گنه بیماریت واگیر دار بود فک کنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84325" target="_blank">📅 17:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84324">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یعنی این گیر دادنای امیرحسین قیاسی به مهموناش برا ازدواج کردن اتفاقیه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84324" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84323">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دلار 260.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84323" target="_blank">📅 15:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84322">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84322" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84321">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شماهم جدیدا ترجیح میدید یه سریال کصشر و آبکی ببینید که صرفا زمان بگذره و دیگه دلتون نمیخواد سریال های طولانی و با محتوا ببینید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84321" target="_blank">📅 14:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84320">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqjhZ_DrsmUsA0xlDVNDbktktO-VZSaltjgbdwUDI2xKGiatx_G2yxabG2USNMz_mf74wv32EE2tkbu-LeLQ_IvOMdp2G0AuyG_mlqXMzEanWrtVv121vqClIIgBEIjPoZrnzJJtjlUTs18HCdEJLyNKAuwhKJKRK3L6ECi1RWPewM-g2X95i_2jGcdgLNtf-yMljfhaUxkWW9szvzV4ur1-x_SAWciuE44H9VfYRqSejodRw3A1JDSZ4QGZzLjb-dk2CmeqqrYB-wnQbh2CTafdGtG8OIrgx7bdwLQsx5bLYDP8RCw-7pVXw8SmO4PCcF0MMS6x9JIy71kPOwxBew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا بعد این که کریر همو گاییدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84320" target="_blank">📅 13:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3j4PUsnu1UQCZRhrB5gOZAu86nzjgLwTr-S7RUNcKazFkawqOKIbzBAP47d0Whx8fevSC9xg_gdBLFH9_VXOl1MZYOqDRYb1SWXuqjDkAbgAKR6n8e0rqXgxYtxNA7FxO83rE_sT39OCzhfsjjmVrA2RzOo7UHb3VbElmR-cEwydfIgk65rVWoh9yatxmT-zO8-4x4cLFG7l-3Q1acT-pM4cYboJCDTLgUxopixPTw9mBRRFiInLqS7B5ZTf8fRqxjIr9YT7nIDRjfTPgv8jAERmy7GDFV5NnoXXT3G7gw62i1SB9OHRhoYufgRnVoTtNkADb6amCjNBFSXLHjGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداروشکر داره عادی سازی میشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84318" target="_blank">📅 13:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84317">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=TUqu4AFDGI43ZM1VXFtYa_RAiGIpRk9EdyJTOaO1Fnl5GCRnQlnGolUz1yAnqZX0g6ZWcuFsfY_Gf_EYb8hXsheB4ou5fFT3h3VbVZvnekJmHl_aET5Ernt9OR5OltpVSMTqA88ty1XEN4M6PTLJkPJAnqhqx7sVDTX5LcLcIWIiYfIq3RdYt6VwwbzpBuOVh4e6dhy9i79oM2oZ_0eAim8z6Pl8LjAvaBkmU92eslYiV02l0-BjJ-s9WfcVWhjEokWFZb6aUeok2BqqGnYzkzb6I3SyaH41F13fveFp1ahnC5HGdP3MchThd53cQZ5BtI_bAC03v1Kd4Z_hAKcyCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=TUqu4AFDGI43ZM1VXFtYa_RAiGIpRk9EdyJTOaO1Fnl5GCRnQlnGolUz1yAnqZX0g6ZWcuFsfY_Gf_EYb8hXsheB4ou5fFT3h3VbVZvnekJmHl_aET5Ernt9OR5OltpVSMTqA88ty1XEN4M6PTLJkPJAnqhqx7sVDTX5LcLcIWIiYfIq3RdYt6VwwbzpBuOVh4e6dhy9i79oM2oZ_0eAim8z6Pl8LjAvaBkmU92eslYiV02l0-BjJ-s9WfcVWhjEokWFZb6aUeok2BqqGnYzkzb6I3SyaH41F13fveFp1ahnC5HGdP3MchThd53cQZ5BtI_bAC03v1Kd4Z_hAKcyCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر ایرانی وقتی میره رو کار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84317" target="_blank">📅 13:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=D66rsyHJkvCR62lCn7nGLAgMWkm5ljOvsHsn2Ytj0Ikm7PRTq7mpvFP6SSjusgD2DxFMqXyFWbEBOK1ytd_yyzbTi_oM2IzIJDejKvWiZt4ybxYKJByFdKLfeJQSJGG4AVd291acf9v8Y3ymxVUYNUo3g4ZJtXKIXFVyAC_7V0a65SjSyYuTZQ8qMAX7PJmwQNANFmoIQ5VU4Ug-b-OsOD4S58kh_Dq9ON-HFQrEt-QPd9F9TeK9EgbPEuCEbEXERrGR2bcfPXg_eoS1MPOY5prZkM7G8EADNsRNzmzY2p0PAqF6Fs4H9IgMKtVgwBTpDFaUpX4O833sGOG5f0zcaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=D66rsyHJkvCR62lCn7nGLAgMWkm5ljOvsHsn2Ytj0Ikm7PRTq7mpvFP6SSjusgD2DxFMqXyFWbEBOK1ytd_yyzbTi_oM2IzIJDejKvWiZt4ybxYKJByFdKLfeJQSJGG4AVd291acf9v8Y3ymxVUYNUo3g4ZJtXKIXFVyAC_7V0a65SjSyYuTZQ8qMAX7PJmwQNANFmoIQ5VU4Ug-b-OsOD4S58kh_Dq9ON-HFQrEt-QPd9F9TeK9EgbPEuCEbEXERrGR2bcfPXg_eoS1MPOY5prZkM7G8EADNsRNzmzY2p0PAqF6Fs4H9IgMKtVgwBTpDFaUpX4O833sGOG5f0zcaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقریبا هروز تو شهر های مرزی درگیری مسلحانه شکل میگیره و سپاه اینطوری یه خونه تیمی رو با rpg ترکوند.
امروز تو درگیری ها حداقل ۵ نیروی قدس-فاطمیون کشته شدن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84316" target="_blank">📅 12:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e0832652.mp4?token=v2Yl1Za63dbVzie-zl71hGdyN11AAyEIpP3Dd2VCw9ARm-dJSrusZSYJQQaflK5RIOo29llFK37sIoFXEju4-RxC2zYHovoSpr4M4bLDHtrzbzO7d8eeJXd7mi1ytY9S_V379kkcFIozkLt-nuNeovt2mZVWl69Nsqm1kjGyb_o1aU73NDYb7hHdnbthZK9LpUzyL3yw7kDI-Vlo8Mzd-BsByE6fHyVse2POwWQWku_MJtVMaXnkSRIkvkd3XzxYRIvn4ErX4jAGsp65_ag0kS_voTgjELKW78rJ6Gq6_KX8HH70Cc4aoTaQR7QYBFhpOsgBJwBOUfUDkaSlXoCkZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e0832652.mp4?token=v2Yl1Za63dbVzie-zl71hGdyN11AAyEIpP3Dd2VCw9ARm-dJSrusZSYJQQaflK5RIOo29llFK37sIoFXEju4-RxC2zYHovoSpr4M4bLDHtrzbzO7d8eeJXd7mi1ytY9S_V379kkcFIozkLt-nuNeovt2mZVWl69Nsqm1kjGyb_o1aU73NDYb7hHdnbthZK9LpUzyL3yw7kDI-Vlo8Mzd-BsByE6fHyVse2POwWQWku_MJtVMaXnkSRIkvkd3XzxYRIvn4ErX4jAGsp65_ag0kS_voTgjELKW78rJ6Gq6_KX8HH70Cc4aoTaQR7QYBFhpOsgBJwBOUfUDkaSlXoCkZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پورعلی : مجتبی خامنه ای شبا به صورت ناشناس تو تجمعات شرکت میکنه. دوشب قبل نیم ساعت اینجا بود.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84315" target="_blank">📅 11:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84314">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=FZcG-EbK1FWoVp3w1waz7iTYa5MS6Rte8A2YqVi-y-a7LScdPKnEGDjY987ItAYMw4ZznDkvRxQHX6u4zZ1Tt0aAVK_U7Q1to0TTp4lPq_2ZbKK6fld-KCK_mx7VjCHFGF7u3yjRMzPgYRVHAjTsA-SxbKlyyJBh9pzQpB_iH7nbzPGKsa3WHmNhG1y7S3RGhP26Nl84yIVrrWaolXtKFVB5ico_1pDmbAjXuIOiHj5kRx2zeJKYp68defTgwyf_7j10GB3jSC-6Ij1yKxgZ7HCKVhEx5bsqmZt7LBd_ACVV5rsDweqPBUaRodV-k7AwTWbkd9VuAUz1WgNV3pKPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=FZcG-EbK1FWoVp3w1waz7iTYa5MS6Rte8A2YqVi-y-a7LScdPKnEGDjY987ItAYMw4ZznDkvRxQHX6u4zZ1Tt0aAVK_U7Q1to0TTp4lPq_2ZbKK6fld-KCK_mx7VjCHFGF7u3yjRMzPgYRVHAjTsA-SxbKlyyJBh9pzQpB_iH7nbzPGKsa3WHmNhG1y7S3RGhP26Nl84yIVrrWaolXtKFVB5ico_1pDmbAjXuIOiHj5kRx2zeJKYp68defTgwyf_7j10GB3jSC-6Ij1yKxgZ7HCKVhEx5bsqmZt7LBd_ACVV5rsDweqPBUaRodV-k7AwTWbkd9VuAUz1WgNV3pKPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84314" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=nqsCd7-6YFrw8UbbfCPDQ5JERR5-HSgG1qBNP13lQyN9S5iisLmKYW-pqzuvuBr8npBRWuo-FaxhcXeX1cJ1vMwKiKY_madta6s3Zx_hp1BwMpqhA065xz9FNmytbkrphBwTkgV9NnpBHWkReim2T5iupYlW3EWpOMFHE3gtbGGQxUU3sl0ASVcO5hFhRfQ60p-8XWUyleGeU_EIQGjHPtPRoX-s_w_UNXUfOCpIOxeqDUZF4WHA20JPdcKIp4ZKCtosySqKtAzofUFqAWMzXJAMQhPszXtR3XXaT-7STplAZpBTMS0KhrrXJAIc0HJ-1OjXN7vuWlZS112UKZf1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=nqsCd7-6YFrw8UbbfCPDQ5JERR5-HSgG1qBNP13lQyN9S5iisLmKYW-pqzuvuBr8npBRWuo-FaxhcXeX1cJ1vMwKiKY_madta6s3Zx_hp1BwMpqhA065xz9FNmytbkrphBwTkgV9NnpBHWkReim2T5iupYlW3EWpOMFHE3gtbGGQxUU3sl0ASVcO5hFhRfQ60p-8XWUyleGeU_EIQGjHPtPRoX-s_w_UNXUfOCpIOxeqDUZF4WHA20JPdcKIp4ZKCtosySqKtAzofUFqAWMzXJAMQhPszXtR3XXaT-7STplAZpBTMS0KhrrXJAIc0HJ-1OjXN7vuWlZS112UKZf1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رپرای جدید تا حالا واسه زلزله های مخرب تاریخ مملکت خوندن؟ نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84311" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=bz5RkGbdKjZSrbwTBoyFhj3BYmX9StHn9x5GDD3Vvlqrf3oqx1k8JH8-XYDYuvFo9IhSXqOFRuskmP1GCVy9kzjvRHX7CM5qkIycQD5vUm793cpLD7kER8q6uOvJ5gt9etQ4Z20bK7EFtKRyVoap573T0NXvT1HSO6zpxaoQKtCKkgsbjYAyqwURvWkuDktANF6Nn1lcDHswnMt3S0-0sA1QhIXWiwB2aw_33p95GOL30_9hKlYyXRCygiUlP_gjt4SIOyDW-6FVVCngtCkPHxGjTuzdTHzirBZZt9BcT6Qa2kbbXZGz2bwH7Hu_TF5Vt6Qb_AY5-sJJDQaZZw8FwmZV3mSQP_vWWmTPCd26r4qmerbZWXDMhBsiINixnyioS8_2Wxheg5rIq67-_-sunEmyhkfQvRKhZV7-bpd9uUrWpPHfDrFHcY8DXABB8mlvMkKwlH9Ees1Wn2dSYJKnkASx52YLiJtIVgvM1Xyw-WT9sXa__oDMc77n1ChtvVlq9DO6-EdLARdSCqNG2NvSCKBX5_yB91lG3hVz6GscTjmEr1jQArawmrS1by9v6Cp6V9dQ6S2QcNtkYNETLqKJMMTKrohQlacLJXp_Kkm7frUOKVjTo2gSnqMb5JoxPda2E0z4tabEwmZIeK-lZ2HS0qBHSeDcVYgxHat1RR7Fywc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=bz5RkGbdKjZSrbwTBoyFhj3BYmX9StHn9x5GDD3Vvlqrf3oqx1k8JH8-XYDYuvFo9IhSXqOFRuskmP1GCVy9kzjvRHX7CM5qkIycQD5vUm793cpLD7kER8q6uOvJ5gt9etQ4Z20bK7EFtKRyVoap573T0NXvT1HSO6zpxaoQKtCKkgsbjYAyqwURvWkuDktANF6Nn1lcDHswnMt3S0-0sA1QhIXWiwB2aw_33p95GOL30_9hKlYyXRCygiUlP_gjt4SIOyDW-6FVVCngtCkPHxGjTuzdTHzirBZZt9BcT6Qa2kbbXZGz2bwH7Hu_TF5Vt6Qb_AY5-sJJDQaZZw8FwmZV3mSQP_vWWmTPCd26r4qmerbZWXDMhBsiINixnyioS8_2Wxheg5rIq67-_-sunEmyhkfQvRKhZV7-bpd9uUrWpPHfDrFHcY8DXABB8mlvMkKwlH9Ees1Wn2dSYJKnkASx52YLiJtIVgvM1Xyw-WT9sXa__oDMc77n1ChtvVlq9DO6-EdLARdSCqNG2NvSCKBX5_yB91lG3hVz6GscTjmEr1jQArawmrS1by9v6Cp6V9dQ6S2QcNtkYNETLqKJMMTKrohQlacLJXp_Kkm7frUOKVjTo2gSnqMb5JoxPda2E0z4tabEwmZIeK-lZ2HS0qBHSeDcVYgxHat1RR7Fywc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا لحظه آخر منتظر بودم بزنن زیر خنده بگن جدی این کصشرا رو میپوشید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84310" target="_blank">📅 09:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337199248a.mp4?token=tfmAaeOh6IDjSirYE7eLRrb0OAogvGgIiStturI94eghOI9X7RZw66h0YXVA1p8NDHMcdhSTiwEkt-TjW7IvTutP0pDU_mLuPVip7N7UdEQ4aEw9AnJcXxgglbTjBYOD0YvJgJ4uYtWiQmyjVT16e-5CA-umCrh4dlGBEI6Fp721CJ6Iuu2uFU5PBDbGI7CGDjp-6dCKf741kQKwRNnunW_N4TPCmBckA-Ibrjz_VSCQnkFdE3466XIuskHKrh_vEVTKSbHhdRVZX7_XqVfH92P0mvX725DPPkjs2KjH0vUVk_6j0jGj1wcSEKtUk7IkF5OIXbZUN_6WKplYEhoItQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337199248a.mp4?token=tfmAaeOh6IDjSirYE7eLRrb0OAogvGgIiStturI94eghOI9X7RZw66h0YXVA1p8NDHMcdhSTiwEkt-TjW7IvTutP0pDU_mLuPVip7N7UdEQ4aEw9AnJcXxgglbTjBYOD0YvJgJ4uYtWiQmyjVT16e-5CA-umCrh4dlGBEI6Fp721CJ6Iuu2uFU5PBDbGI7CGDjp-6dCKf741kQKwRNnunW_N4TPCmBckA-Ibrjz_VSCQnkFdE3466XIuskHKrh_vEVTKSbHhdRVZX7_XqVfH92P0mvX725DPPkjs2KjH0vUVk_6j0jGj1wcSEKtUk7IkF5OIXbZUN_6WKplYEhoItQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمدی شاخر : (شاهکار+فاخر)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84309" target="_blank">📅 08:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84306">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=f7AIUv25ToHbXrzC2Y8p6tvJywQs39_mXCRjIjdpqBm9IYd1gnGu7mBMjSHYZKnItDIIV1hNNbvoAtPS4Kh1MCipUZqkFhVjgtEOxzfQNiK9tYAP46YnPGYT85aJM2MqWW0f10WKdp5_MERSW1x4UaqpQfmmZHse2zmg5TiRU8R6mobwDWpym7GtzN203IiT5kHPqQWT02ANT2RqdWzrGzrbkiez1Fxj05MrBYlgGrHfmigv8_0_PurN_BUOsj-bzSzLKE2I9mmADFa_Vw4HUvsd0_K6XjGc7sS2pkEiXKpZf7rSk0JSNSwuYHZw-avOgiEkBSKf-v3QAsuBZofUGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=f7AIUv25ToHbXrzC2Y8p6tvJywQs39_mXCRjIjdpqBm9IYd1gnGu7mBMjSHYZKnItDIIV1hNNbvoAtPS4Kh1MCipUZqkFhVjgtEOxzfQNiK9tYAP46YnPGYT85aJM2MqWW0f10WKdp5_MERSW1x4UaqpQfmmZHse2zmg5TiRU8R6mobwDWpym7GtzN203IiT5kHPqQWT02ANT2RqdWzrGzrbkiez1Fxj05MrBYlgGrHfmigv8_0_PurN_BUOsj-bzSzLKE2I9mmADFa_Vw4HUvsd0_K6XjGc7sS2pkEiXKpZf7rSk0JSNSwuYHZw-avOgiEkBSKf-v3QAsuBZofUGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84306" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84305">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=d09j2G8nXWCpUIVG7PoPsMYjhq0PQTT27UOy_SkmuO0v8NslrGvUZYf_wUfkHmDhpU6R20SzGlnaD_phDVuL5uZSD38xf2MqO9W6KdZq99FvpCKtiycGkFLe3cMa7RSjOOrMmbW3xqcB1zoiKOSxk4VXpHS6aQeGRZ7Vh7zoFq3H5VmNyMnrgbG1aSlzxHOsUFcaUhVOAVFEWdi3jlnHao3q6-M2pM5_ZIkVkxWLg9r6o3LRTtxBiVTSkwCt-umNWsajf8MFQ41qF0rWB-i5vgGSqpBAX-s6nNK4DoLkLwsOgNm0IzgXZamEPshXpmC-ro_BpZ9RdcvtHVpPZkgBZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=d09j2G8nXWCpUIVG7PoPsMYjhq0PQTT27UOy_SkmuO0v8NslrGvUZYf_wUfkHmDhpU6R20SzGlnaD_phDVuL5uZSD38xf2MqO9W6KdZq99FvpCKtiycGkFLe3cMa7RSjOOrMmbW3xqcB1zoiKOSxk4VXpHS6aQeGRZ7Vh7zoFq3H5VmNyMnrgbG1aSlzxHOsUFcaUhVOAVFEWdi3jlnHao3q6-M2pM5_ZIkVkxWLg9r6o3LRTtxBiVTSkwCt-umNWsajf8MFQ41qF0rWB-i5vgGSqpBAX-s6nNK4DoLkLwsOgNm0IzgXZamEPshXpmC-ro_BpZ9RdcvtHVpPZkgBZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84305" target="_blank">📅 00:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84304">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNxP_Lm3zMZ1wjbEf8fOMGZi0saWEbhf9ZZqQi_3EEhHR-Dn4XcUxkKFOUfKfp-t_1keqil5qLr5mVUVrkLnGzNUe-DRhiy3r6s5u8I15M2WpX3c71OTu7-Ovkp6yS-tn9DXIMt-tOsxnEnrsHXrRph44BLALCGX1RrcJv5Fl5Q4PFY_KTRfGVxopMgnVBqST7js33f00wKEdVUY15SKBijfcd0190fwz5IpBG_g7TFIW5WO9Bwo8jpVeXM8gBnj2zJHD3PoCj1jMLf0_sK4G0thKYP8C8WG4fdXtfBzaW0_AJ50Uwy0vmuGzQYguKlLTM0H2ejzdwpBobmp7zERww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا دیدید بدون رونالدو هیچی نیستید؟ رونالدو بود دفاع میکرد دوتا نخورید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84304" target="_blank">📅 00:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84302">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دقایقی پیش وزارت خزانه‌داری آمریکا شرکت های ایران‌خودرو، ایران‌خودرو دیزل، سایپا، پارس‌خودرو، زامیاد، هپکو، راه‌آهن ملی ایران و شرکت قطارهای مسافری رجا را در فهرست تحریم های سراسری خود قرار داد و اعلام کرد بیش از 30 درصد درآمد صادراتی ایران را هدف قرار داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84302" target="_blank">📅 22:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84298">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43faf33322.mp4?token=DWdvkI0teyDoD5407ubmuxKb31JppJGs5cPibkEafTEm2jPcQowtzUTJmRFyJnQsukL6SSiS8WR8ZW68lsGsZ0AcUXpGjSayLQK0AfmYlVftn91B9gVVOEWNXKAv2jwkIWvAcOm_VBAbP3ISvBJIJa1AWISQFP4bTlNL7id-3NKv1QrzcTfbLrSNjtidkkQFiDvBs2k_Lt-CnL7Iwy8tt8q6CZFjzuABxPjNRSyOd_mvkd9qj3D4xILa6NmeZsOABReKqDNvTYMz627Ful_MJX5Ypqphb_FeXqqo6UbYrbS2V7K2TWeDIBw8DtsYQWfz_9mS0X6bX7-NSoLdu2YvdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43faf33322.mp4?token=DWdvkI0teyDoD5407ubmuxKb31JppJGs5cPibkEafTEm2jPcQowtzUTJmRFyJnQsukL6SSiS8WR8ZW68lsGsZ0AcUXpGjSayLQK0AfmYlVftn91B9gVVOEWNXKAv2jwkIWvAcOm_VBAbP3ISvBJIJa1AWISQFP4bTlNL7id-3NKv1QrzcTfbLrSNjtidkkQFiDvBs2k_Lt-CnL7Iwy8tt8q6CZFjzuABxPjNRSyOd_mvkd9qj3D4xILa6NmeZsOABReKqDNvTYMz627Ful_MJX5Ypqphb_FeXqqo6UbYrbS2V7K2TWeDIBw8DtsYQWfz_9mS0X6bX7-NSoLdu2YvdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید میلی گلد بعد از حواشی و شکایت های متعدد مردم با کپشن: این طلا، بخشی از طلای میلی است که خارج شده و حالا با آن، تسویه کاربران در حال انجام است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84298" target="_blank">📅 21:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84297">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">لیائو کصکشو تا ۱۰۰ سال پیش ۷ دلار میخریدن الان شاخ شده شماره ۷ رونالدو رو میپوشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84297" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84295">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2BM51J6pSsWmEn8Y8t9ZmaZUBrAtQw7Efrdq9_njNnyCwbZmYlJ2wgkAtJNnI_BLeJ270GsQ0PR3TD6e6d9WirCJxAb0fUZWstOdSqd8VxO12Npr1JttANQWpvmysuk5WSxmT7LAwVJOyszhwvwGITxvTCo70uG-FkzGk6PJ2L_Oeu2fXE0eTLPRN1AGhWGETFcXKaL2yb4B74w6-ukAaoeClkEcIdGFmnup2jujyfBDD30gFucpIHv8HmouNRX7bCUapJF2f4hYMg1zoMN99BNjWO-1LLViOCEwMueHmjejwtnSvTv4lZ9q3mVv_H9mKRKjkx9uulqMP-NU6c4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا جای این کصشرا یه شیر چای تریاک نمیزنن این شرکتا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84295" target="_blank">📅 21:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84294">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پوتین رسما ناتو رو به حمله اتمی تهدید کرد، ورژن ۲۰۲۷ کره زمین قراره هیجان انگیز تر باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84294" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84293">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پوتین: کسمادر هر کی که به ما حمله کنه نقض هم نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84293" target="_blank">📅 20:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84292">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مهدی چند ماه اینده این ناوی که زدن چند میلیارد دلاره
یک مقام آمریکایی به الجزیره: تا پایان نوامبر آینده، ۳ ناو هواپیمابر و دو گروه آبی‌خاکی در اطراف ایران مستقر میشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84292" target="_blank">📅 20:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84291">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖕𝖆𝖐𝖍𝖆𝖜</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHTLEFM1Bh3thtCtMPhnVOjXQNmmrD4x5l620f_qAmPwOJAwKAxxR2LUJbccZ8fR0NuImYxBYXpBS9JrwfX0UEPWHz_45sxe74oh3JENZezcSjszZx8xLP_B-1Y30QTdCy1jDVN3M1Hls7jHo4X-xOtuXelazlYExx_G7aY8yATHPKKafC944cx2g0yar3wPHsg3nI1SjnH9BRuGpBcsjUXgKmg6FD1l_8z1jI3UETQEY7C6mgwFHtdaMZnTnrQiqguQSJXuosxvLcpUlX2_z58HIt__PYk1lWt8dawyqgBjk37Z5Isww9El739COLXPM1NLAqL4j66-eko_sYqjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84291" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84290">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIXRDjw8q1p89hV3YqI4CbcbqAJgqPPXBV0f8cLcgB9nv9UJkZpqP_Pkq0H5cjxE0fGnVDDRLcd1Qo5LX5xvyW7TeRaLwYHhrjqwzMWAIy-JpU7Mj9ChtdieyTiXcCQ0dU0RqhKSe-RAaDzy1-LVZZ9wjhqsYr5rmFEsnJ5i5HNmMUEpAkRHmLQCCLWuRrQ3YZ2halNF8w0qRcaH7ngT77cP4n_Wq1Kdy7mPLHBBOWJOYLRJunpdqM7shaWuNbOa7GvP6FD-dWExpiyDnCIyHucs4Dt086-U1b4gyunOXQZRnFxSR2YfZltwXE37V5Z0Dl4mYefU5cK7SEZlE_iGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این فکر کردید امیرمحمد هرچی دلش بخواد میتونه بخوره بدون این که نگران چاق شدنش باشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84290" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84287">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVSKTHgf91eB_Q1sr4JwWTzzDQf0pRrXWlirhkAzmZHTR5fPKBbLBoJTOWmhm0If5kpuqXAVQ3lAqnNU5UMZByKh4bzxBBBnZnLcqqlg1w_IpxCWAD7faEgyjMo9Jj3fRGU6095MErhlEu2D-wf2GgtMwmX9S0Sn3YkDzkyoBGH_gtmWkN52svOzDik6GeinKK7eNQmV9dvjCYjrwrSGiyrDZOVimSB85iLYAzzOAtysCTAqJA7kqzlyP66vDs3MzLiWtKJXjF_37jFeJ0vvwZ4TxYgSWRs-Kw2DX5uPFSZmkLR7TdfakwBmzY1mK1UJCKAP4sqEy-7BztbRy1B9Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfyKhjWyuNz0t2TjcSEhTIPo-L1-TJFKZLio4n8WY4zMV62BHPLpjBQQ9PVyHyRZBGxCzlPwvj0h6GnTc-wkSywTtK_RYZ2aaaevRTepJ-evesK-rBNTiSG1yLJi2E8vPn0mhk-Rt1CkLFnEm7GCaYUAU2YQH9J48BNgjhKsVNPB21dAAvA8M92QHMv6iPnickKL5vnPrVCgfWNAE4JAs8peAb3-3xG_ib716B9ClgLhNTXR68J7uj1TNJhYFyad-Dd96tNkFkoyugUg0Zz-cG20aUF7jLl39Q_BzcxStm0xfln3IGaxz8e8JGF8pD6LaqTvUH7iQRTDuz-_TZTA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyUTF8K6v-oDEh7WUlgJHCOmW3pTkj8GrwnI7UyzVUwUK-iSe90-KROuCMBlWnzXgbwgttepJGCOp-6Kb9Uoo3UwLSY2Y5GP5x3qqjaFtqDoxiqOu3gfEU_Egp6KZDnpU43OhAMk1zSJ_H2AYBcpPy-3cCensG0r_jIqnmXfwed7SZVP4VNW1jsGqRm7xP1mUz_jijD9B3sODFstoWKMERqbgrVDLsGNHMHW0UPWxZPukLeVo9ov3jJaLcyG2m15b1D_VqjobKkDiwWKZsk9I6g8OXbM7sU7tlGDSLhgURVr7JNWQ0-nK2BHIFwweCs-7sgLn6NxLt1aTZT-MYfzVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریری یه جزیره رفته، ۹۲۹۱۹۹۱ تا ازش پست گذاشته اینستاگرامش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84287" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84284">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84284" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جدی باورم نمیشه یسری آدم هستن که موزیکای قدیمی گوش نمیدن و پاپ جدید یا رپ گوش میدن فقط.
فک کن حس فاز گرفتن با موزیکای سیاوش قمیشی رو درک نکنی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84282" target="_blank">📅 17:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84281" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKXhrI9bMSXy83-WUetIYwnbIZgVjoG0vW0TeoJF4sY-VkyE-kABWlTciKp39nt74EY2hLodxbPlYo_27UUq228T85uyb8BpZlXu3VrfXpHXEy8YnqG_a6Jy4wKioc4KKXo3Q-Aaz0souoCpuWhMEEkD8ZPr23uuiqMbOUOpZkJweFg40WPJQVHK5MbEnTXRU65f27QE6NnaFB7rJFJlnuwJ8vA8Qs5c8SY9AAdkp_jOmq2h_r7laswW8A50dVSPw1cp2IjBan79GbI4JN6IKAa6xpv5_AG-uUpj12VjS_VdAHNGT5aTi-EnHxrpTbNwVciXR5f5Ya74PBs3NqZm8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84280" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1ITCc2cqoOj_Msbcq-mQ5HtKq2J0CzgfGlFa0JfBuvU2AbP_OIwPeCcVOLPwsy2VAGTsexAB7KcR8FV-uUXZzh2mB9NkxZrWIpaoUoSRlaC4XLbuhZS0db9TIOKUQyU94rNYxz-Sp95MPFNv9HABEwdPoWbSw1p74InjojIE-0KNTvleaOQ5bh6Ph9LYCWzhoQFCkP0zmrvOuR-LMrHS_gymK4Nnfc-JRC8wWCojqn-tYbRIv4ul5OHsHzC3X-j_SQR-zbE-QWGL9aDm5UkKkP8qJ3Qk-4gW4j3tnj916CvvxrWdqDqHQZTWFxlIhYeUJICb943Vn4RR3YZnfDKcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی انقد شاهکار شوخی کردی که مردم با شماره ناشناس زنگ میزنن ازت تشکر کنن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84279" target="_blank">📅 17:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf_XAxi_PocoreT8RJ88FQ_xaXyuhvtlsbTKN2ee3EqeEU6eh4u405UpLKxvGJ0WOvHscDxv7TtGicJuoNo5xv6LgBaBfdTp3Rhd_Ke9Lmp248iUx2VlyjQvLe__5nOw27qHaIaakf0BvFaODxQMwr6C_LPOUiUD1fc91VCmZke4U4cAFe6kRDSOKza9KegJqMgJL32s7n4IEcenVYDlgwVxano5I-IQEpr1M7_dfqVWOH5_WOI298nr0C-8q2Csc0UQ4VCNaxBQHjFLM-wuBwgWp-CfodogXAB5BBkQMs-A2CoPLYCGNjR7wQR5u6-0Kaz8q25A3yZ4adMRX9gjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=Bf0Las328oxo0VStstrkOwPVwRP2rFZdoPwNW-XBnyoGXl5PrfV21ePMI4FUxCNJBr2VO-2LmMCVHKKM8NvDNi_mIlvaTh_c0_XCCDhhbadOdEcQfqbEfiJRomo4GlBsb7BScxj3QBlBFNGHVi18-tW7OCNVUp4gPNbE_WHEqfnueLobK14GW7_bCxWtnsjPyg-kV5NwJXGHptrpa0stkgRX0U_3i0gDY_ieuHxPonw5wTOKfJPqpPe-ziQZjQekdYIHFhDHkpHJM3izrdorQZR_cPINaEiFsjbe6J9vdnqgSYxyyGYAW3kOozNBtyrjCRZwmSabFSM-djPq39q1Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=Bf0Las328oxo0VStstrkOwPVwRP2rFZdoPwNW-XBnyoGXl5PrfV21ePMI4FUxCNJBr2VO-2LmMCVHKKM8NvDNi_mIlvaTh_c0_XCCDhhbadOdEcQfqbEfiJRomo4GlBsb7BScxj3QBlBFNGHVi18-tW7OCNVUp4gPNbE_WHEqfnueLobK14GW7_bCxWtnsjPyg-kV5NwJXGHptrpa0stkgRX0U_3i0gDY_ieuHxPonw5wTOKfJPqpPe-ziQZjQekdYIHFhDHkpHJM3izrdorQZR_cPINaEiFsjbe6J9vdnqgSYxyyGYAW3kOozNBtyrjCRZwmSabFSM-djPq39q1Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید جان ناموسا تو یکی دیگه بیا برو کونتو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84277" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84276" target="_blank">📅 16:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">واقعا فید کردن موها یه کلک مارکتینگی بود که آرایشگرا پیاده کردن، مجبوری هر هفته بری پول بدی بهشون وگرنه شبیه جنگلیا میشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84275" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کصکشا انقد به پر و پای بلو بانک نپیچید و نگید بزودی اونم پول مردم رو میدزده، یهو عصبی میشن فیلمای ثبت ناممون رو پخش میکنن بدبخت میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84274" target="_blank">📅 14:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84273">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9vNlDKfD8zhlmBux6rD1VCrISuf3Qpl3iBmGivQPVCPeRqTmGZNNcMSHQYf5VPkvIPN6M9k5h07rNSqZ2J1nAYBve2HpBzwkQt3IbzTIshESTmXiwd9yk5H3sX1xdIUqAqVsxyu77n0JOOwLgR2edBv7RIR8M-KTcoRH_lOh01PvTgHo45hit-G3Sk8sy-n-O0gkE_svNFHhlP_Qn3-wX--2HEFgCuz8ZoMItf6QTL2MiIHXJti_DCkA3AKTyCKo0jUj1c7KaiKbV01SZnzelx1D-rRtG0yqHPcmDyXAk2H4aJFSChd7FRUsjdhY99ouAhscxSZNQTzOT7wu37fkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بازی دوستانه دیروز کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردن و گفتن ادامه بازی زمانی برگزار میشه که فلسطین آزاد بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84273" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=J4CKA6fggUCqtdBYVVLRdd0KbpzUEvEDz_ERnT5utJ9jXvBlkZK572nMYn8g9OrXy0H4p6qQ-dt01AR44fFqAVGNRwbPHZDgjC_JUg4X-7SHRbN0XXCoCyFEU3Lr_RY0PR6skh7opOzu-xmqzsn_-k9POTN282nuc3QukxlXAjAX4TncEBhzrWvINNSonV5TAOdQnDPjIBcNY9pxhikdCRzYwvffUL-HZ3t_Lrf507t9TZYZuo2MWoGO2pFGm9FYxmsnbQ74OpKwk7SFnXd4f9mmeI5XK7G5rqOlME75hqcfrW6d4lbzF8924smhPdJ0TukXM9Ddsy1Q4xVinJ60DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=J4CKA6fggUCqtdBYVVLRdd0KbpzUEvEDz_ERnT5utJ9jXvBlkZK572nMYn8g9OrXy0H4p6qQ-dt01AR44fFqAVGNRwbPHZDgjC_JUg4X-7SHRbN0XXCoCyFEU3Lr_RY0PR6skh7opOzu-xmqzsn_-k9POTN282nuc3QukxlXAjAX4TncEBhzrWvINNSonV5TAOdQnDPjIBcNY9pxhikdCRzYwvffUL-HZ3t_Lrf507t9TZYZuo2MWoGO2pFGm9FYxmsnbQ74OpKwk7SFnXd4f9mmeI5XK7G5rqOlME75hqcfrW6d4lbzF8924smhPdJ0TukXM9Ddsy1Q4xVinJ60DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آ
مریکای جنایتکار با انتشار این کلیپ و نحوه شناسایی و منفجر کردن آدما با پهپاد، ایران رو به جنگ زمینی تهدید کرد
.
تو این کلیپ سربازای آمریکایی وارد خاک ایران میشن، و دو نفرو با پهپاد میکشن!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84272" target="_blank">📅 12:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84271">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84271" target="_blank">📅 12:31 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
