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
<img src="https://cdn4.telesco.pe/file/IFGohYSVqMW-9wqVmU-P_GkRKqeLmVWqn0wQS7Q8P9GTrN2zPGfJlpcNI0KY9ZJ-1WG3napKAPuqzzwD9PyD3vHUwzdPbVe4O2lhSJE2bPxaHY3jwHb16-WnaJkH6meWnJsGFqdtFS4k9b0Xf1HW2qSn0HMGw0Y-Uu16eU8n-V0-SnbAocpkPngNzZmmUJfIDdkSIg5rQNAh0qzHvE2pRbFEKekK_35dyh6t8E6IDZJW8DdX2PM9_l_lBoXQQNs7pmAdIbczQdLN9Q5BYHo0lpILm7frXrD-xNJ6RCSBJbDgiTQkkGEb2r1Bsacci1LNqAzphnAlIze2kH9eTO3DSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 436K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
<hr>

<div class="tg-post" id="msg-30728">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Abepv0N5T_tmkgjBz51EAxqqwaedaJ5pxlLWLZbFHN-IezWsPX3D1SvVO-4C0ur8zv6n7iqE8bn98586yKFtb4Q8yIed3R1ZKmQlHxio7LQNC6ph9Tvn7MPzQWri8YlcPFHd2vls13XpH9YOFhOWGGS58WXtJ8CFwZNgzVFpAI9C5VbR2bTTrXSfSvH6H6vjvgMINNxlMN39vRKlbcoOWm9MJgsg6ZI2eZqPSntBiZiogxj0X3PYqOv3467eQSJGCa0dFyLdSTY_r1d2x2p20qbXBeqbH6ytSbRUEBs7pXkUaBHaXG9a7l4OpejZHSRU3o2Yj0WH0g4AM0xeGnN7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/30728" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30727">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz3Ssv-2QrEn-Px3Cup2Ah_ZtB_VIdA9pPnCfbd-duhUjPYWZ-D4X9iUWtTVK77mtJAzuy5MSQ1upkKXM5e9wRqNQurt4806QVCXhGQHA21ZWEas_3htESwjIcwZz49oU-Dwe6dIdfSlI9HLv_b7gNmM_UN4B3lC2j97BlNOs7X_QCprnOxSQT_r630_A-reaLGU7gL_kntroOX-0eAFpTBjphqdR_oYXtcWm2dhEk3epfxWJ-jwI2sFdK0wlhEkCgoGNbc8eOvQ2LjKzninuluL0wlAc1-hl5CaIH2xyjoybL82Vb2mjAjvYpI3dXScsZ22ueBZc3-GDn2VOUcn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لئونورملکه‌آینده‌اسپانیا:امیدوارم یامال برنده توپ طلا شود. او لیاقت این جایزه ارزشمند رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/30727" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30726">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCzneA69Xz6480lRq5cd4pKB_TyvpUu3e0aeFuGJIV2znw7xL7W7ZgXJG-70Upn7Svf1DLMGLAaJvvI4vjDqsIBDZGW9fGcZJxISEdrYuc9xsA5wXmbKA_ZrvmTWj5_ALHmOztHHeJDxB9YQE1RyHhCWp8ahE3rbAse-hHMH7ijX_JfksU6jVwXdqiAJ7kYaW9IImjY9A6dnilRm6qYU5RXSVW179nTiXRBN5fzAKAlAbgE_WA74mUn3sJRMMXJaprcFdUkR10wfokyRx8LwcYQSNjYVzpmwefhBTXIFryGT5YXMlk1yoM4mViQPzdQ2zL0Zo2Yhn8A8hPJUOXvs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/30726" target="_blank">📅 12:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30725">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=rsK3UyqiqkAVRyLwO0SWiOisOWlegiClIGvzR-1vHSCvB4sHQhJs4qQMSKXpkk_nEfkKcVWYHr8QwnEnmlWqnyi19i616KRcCH7_-5tzNZ4xbzPVoPL5egxBhNmLH0RZx3WLAERrDvGAwWIIXb0GvvkF_-_HoXgOuvMX_kanzObZGeq3tbJdPxeVB1GtyhUl_S41s288M3hzsbOvrArVQpwGRHdI747EPVDU17CqJ2JjYUbMzHyA2L0_o_5StTtz-iCnr_SwvC2dSmIJmr-a8GUhhJsSqXDKcq6OG8ldfBpHKdIVf0DA73K8-bVf9vxA-ezYzxdqnhvh0N_jggNN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8b65b7df.mp4?token=rsK3UyqiqkAVRyLwO0SWiOisOWlegiClIGvzR-1vHSCvB4sHQhJs4qQMSKXpkk_nEfkKcVWYHr8QwnEnmlWqnyi19i616KRcCH7_-5tzNZ4xbzPVoPL5egxBhNmLH0RZx3WLAERrDvGAwWIIXb0GvvkF_-_HoXgOuvMX_kanzObZGeq3tbJdPxeVB1GtyhUl_S41s288M3hzsbOvrArVQpwGRHdI747EPVDU17CqJ2JjYUbMzHyA2L0_o_5StTtz-iCnr_SwvC2dSmIJmr-a8GUhhJsSqXDKcq6OG8ldfBpHKdIVf0DA73K8-bVf9vxA-ezYzxdqnhvh0N_jggNN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیرتولید محتوای شبکه تماشا: درپایان سریال امپراطور دریا؛ باتوجه به‌درخواست‌های مخاطبان بار دیگر سریال پرطرفدار جومونگ پخش خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/30725" target="_blank">📅 12:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30724">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQd_igHBeYN2fx5sMWAhWaIGWVGnS72tLKFLG5bzvqoPplhRSZdil1_px47eSxlsyTM-FtrKgNbxxOOBfmYDWaoWiPTMUJZpasS7Lpk4EQdXU6CzB4TxDZ5fEpNiOzerGhw0JZ_rSMYI1uGYxVU_KHh5cTiQeNn2iV6ca-yYdtY0ph02coAHC6I4zIAq5IbWk8zxzf3RtmK7x-IA8HBw8AjCICdCyo5IJ7v50mBC5zbZCp80Wxn_PgeIJbp__-PimnAXNtBZSPIZLA9ieuGzTutxKQgpducDkT9yIN9EAA9TQTMhXCqU_FSJWpd5K8KyarxsR_GK19WYZSD9SZ7r9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛
محمد حسین کنعانی زادگان کاپیتان 32 ساله پرسپولیس از طریق ایجنتش آمادگی خود را برای تمدید قراردادش باتیم پرسپولیس درنیم فصل به مدت دو فصل اعلام کرده. قرارداد کنعانی در پایان فصل به پایان میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/30724" target="_blank">📅 12:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=TgM6ejXwQ5B9Y2M2duLnBslSYPWRVlVSqrco_wVi1PGKm93xwphSLjv-3rjupEAGFENDCtVjijr_nF3xRQE7u-uxGCvWm58bOys_RU7QVIDSSeCErICwwhe2dtyRLq-BaMlTY3rO1UfJ217Yi9Ypj0-7bTY-Sb56N08pdP-3qSjg83LbpaCPi1QtUz3e3BWyyaP_drOvPLYKE_dfOGtEKkTp-3YqOTrXq-I7Y4PP7LdLxNZo_u1bkebSK7yXnuP5_-UzQe8YbKhU4Tau-7Nky2QQFOtC2sTI_LBGG6WtcKyn5YamTTGFHCD0fKLhWRaKLY_giUkdJqtSrmjcGg_pQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3853d1925d.mp4?token=TgM6ejXwQ5B9Y2M2duLnBslSYPWRVlVSqrco_wVi1PGKm93xwphSLjv-3rjupEAGFENDCtVjijr_nF3xRQE7u-uxGCvWm58bOys_RU7QVIDSSeCErICwwhe2dtyRLq-BaMlTY3rO1UfJ217Yi9Ypj0-7bTY-Sb56N08pdP-3qSjg83LbpaCPi1QtUz3e3BWyyaP_drOvPLYKE_dfOGtEKkTp-3YqOTrXq-I7Y4PP7LdLxNZo_u1bkebSK7yXnuP5_-UzQe8YbKhU4Tau-7Nky2QQFOtC2sTI_LBGG6WtcKyn5YamTTGFHCD0fKLhWRaKLY_giUkdJqtSrmjcGg_pQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/30722" target="_blank">📅 11:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9tdoX2OpabLG-muLR3Hy3hStqbD4uQAzWcPf6VJjilj7Lvxrk_1m9nPC6AFMnFMxp7rxEE2ySxU7z448oRYg8Xq9kY1bSEpZjRHSYr5RJFXjy6QOd6G4NA8dmLHevn8BC9i-UszPlDpBRIHNWI80fO3dnLQgL3enjxwyX_B-FCS-C1BzOJd4eTECtaiQmTHmsyLjsD6eqpuP26dMlU9BQDSSZDZiEXZAXur_KnhrxeDOxq7Msg-3T3G3GLVsXpJnVt3xZgQQ0UFWavQyCglfBEdRNq2oO8hQWppeCqsCxWoNNfyhbrWp87_MHHWfZVTtg4fu0L1G_bYMa1L80ytcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/30721" target="_blank">📅 11:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOZI4sYRUOkquk236OQsCEINvZ9VOW5arKu0J3D7kBmwQF4JZ4evzupD-uy_4pq1BEO0BTBlrVM4JvPqtc_7Hjgn_bLkXGt4H7moIhslNHFzxvFzkJo63D2oSWohEKarezxJGtx3aUs96LcgrORRKRy12udH5pugb0kzDFUkZ5uCPUouKfDCTaw_hYGbvsWt_CP5WU9a_onlZLHP6q8FvkDp1Sk1WlyUGWBsK3yhY4YCuVxyppOpuFxeVvyrBqIo4MTuWvPAzRAp0MmJ29CeYgqlf6OSjd2lo2XczfhkoemfIVKhDFVhn1zYAvaCb_PUVElniLk-H4Hl8i6OHWMKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
تیم‌ملی‌برزیل امروز ظهر در دیداری دوستانه بمصاف تیم ملی استرالیا رفت که در پایان به تساوی یک‌بریک رسید. رافینیا در واپسین دقایق بازی با یک پاس‌گل دیدنی مانع شکست سلسائو دراین‌بازی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/30720" target="_blank">📅 11:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPsGGefK4zv8MDvUsG_YgipeGTeu1M9Hy62ngBt1rbZrg0i9hkl24Z5IC1d9Ut5RQ73AaiUz_clTfySG7pT3Efp3CvpvZN58TBQhfP3d-AdDT3PwymHUkd_UiU0q8bWB8WtGmEJHGWMPtBm4b9QFYMv-RvQqPo5WKGTuYkrdqN5tpRtF4mkeVgT_kqQUdbrQ7HIk5a8JHSrFq5L7EKctAc_H06Qz6UYfFyvwnOkz824-NEp5GNHBU-CUTe-vIJhGYkkXiKAES0K8gilSMURKJIXAUtj92g3C6wPVpQiydl5c-Q-vk7p0Mck14viYMiWRwclGmDu0rJ_R2siOl5qgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با حکم فیفا؛ باشگاه استقلال محکوم به پرداخت مبلغ 30هزاردلار به مسعود جوما مهاجم کنیایی سابق خود شد. آبی‌ها 40 روز فرصت دارند تا این رقم رو پرداخت کنند و پرونده او در فیفا بسته شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/30719" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeyN8IXIInBhA5XEvRdhScJ3GXMChjRYLT_o03GAjlpEvhSnuQenzS--g1UJTAH-kHkLs-dVN2xnE-h4qnophiaGUFzWNg9Hp9_3v-qm2J_1CzUlcudORcSw5NH2R0QagG8UtbKtmgRO-i4Jsm_gE13uNUlr4h6UQkveqNyXLRYXJiZvbHWoNHT1otc5EH2y7NkitnZnkA1ZpfifyxNamaH4oq_Gjn1P3eCf3mYUVQb6ZQP3mBowlS-m9jl-8wvSm7nIGEjspInrsuZ60L5q_HHTN-dJoQ0ZmMMJwI6WEVMwj78b2caFzBxayxtlW0X054udmBQeg3f5yf6ahoa2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد اسفناک تیم قلعه‌نویی مقابل 50 تیم برتر رنکینگ بندی فیفا؛ هفت مسابقه و تنها یک پیروزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/30718" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#آپدیت
اپلیکیشن بدون فیلتر(WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
✅
سالها فعالیت در رده بین‌المللی
✨
ویپاری
🎁
نسل مدرن شرطبندی
😮‍💨
پاداش‌
100درصدی
اولین واریز</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/30717" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30716">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNx6mj19Drw43OvdxRqgWAxC_oaBaMYi4hh_aQRInbOmfb45Kj4XT6pV-VPxA_RdrGqODwpGlZHOlUOo9JjTcTMeFwV08mbkt1ISI-HfTn73Of1u_vNrYTmMjiW0dE6-ZPS0ydLXvF6OwlpXcY5SIe9k0atMWfRLd0EhfBy--mcOmqNr_w38GbAsGmTQ7FohPRFudqzboxWMvfE_xgmO9rPzJpfLTn0UOQ8euMlvxFQvJ2ji6bEgQZ-Uwuqd5KvXaygnEKSsIJqKmNCYqruhKZo2jjiv55Ec50OjM_tbZ5e0nMl7_wST9OOtwdcKQdc8lloN8-qgx-QTqhfMjvDMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
میدونی چرا حرفه‌ای ها سایت ویپاری رو برای پیش بینی انتخاب میکنن؟!
🎁
┅━━━━━━━━━━━
✅
4بونس روی چهار واریز اولت(به ترتیب ۱۰۰٪ ۱۰۰٪ ۷۵٪ و ۵۰٪) هیچ سایتی همچین بونسی بهتون نمیده
🍷
برداشت زیر 2 دقیقه بدون احراز هویت
😃
درگاه شارژ ریالی پیک پی
⚡
تا 25% کش بک هفتگی
⚡
هر شنبه 100% پاداش واریز
⚡
هر دوشنبه 50% بونس واریز
⚡
باز پرداخت 100% شرط های اکسپرس
✔️
بونس 1500یورو + 150 اسپین رایگان کازینو
🔵
لینک ورود به سایت(با وی-پی-ان)
🔽
🌐
www.wepari.com
🌐
www.wepari.com</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/30716" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30715">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pft2oHZOEbt6YDD99qyaP3MhZPlKy66J3NpU43M8MjKoRl3HMVGRf0inGe3k1e7Rgk0GwFI8KYKC1hCgY41CUZ5RMOI1rL2f0mpA-6FttHLFH4LtxOqcHd1R5b8J7lNqsDRnTw990NAMK6aksKKkAfQQ4ygjIB1vnMIUkh-HVAipf24xLQlUnJg4pJ_7rOuHoivgIwPcaccZwNfkBfQRvPulHu7cGuf0RP_d_kw6_b9kQ2p206iChHuLRjNyVrWbD1AWXBgHD9VKL017NUYOnKWlE7W2e3oFChw1BFpKebbYJOo5TBrI57EAF0HcDWDZBQ-nmYAVI4v1SaX-c6oNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/30715" target="_blank">📅 10:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30714">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HimijtSpLSVH8vLFkljjRZXIQvF8i_fiz6_SHhqT5I4fkUb35uiKX783y71_gQyDDmGKEmU0oeLWLJqiquDx20YPL5co71qA6NAVEQdG5B93r_2VoNIrA2FsZaUJYaXwiM__M3Jt3uvsKraH9r8Oqr5ly12gZ4CBwcGWwmAQFK6zoj2KCzVvF1MFUuqhe54s13r3oa62thcCq7bSjId71NqpzhlYNwY78vg1t10n6Rwf-Ff-Q5nqpGZbtpyMj4kcTOcuDdXOL2IXSa6FiW2G32mNcwHK_Ig_TsKLDjW6JsXK8-4Hf5-HHOtNkK-ldqi2U0KY1wSikiJQLTZ0_3Dswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/30714" target="_blank">📅 09:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30713">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=djR0BYidg0e7j1NRhtW8pe_zwICIaM7JxFMOYf6LMjvzDeBNxytISIpHhZxL3Ijaj8gQYUtR_Dbl7FlCs8u0HTnYcnRnhgP9rqUUkK-JeGTgXywfJbfWA65oLdKmbZSoOYnB4yWhPg1MXUZrNTtsvzf6immvqVPuhTCKEKap4rUtk4WMyRHjXJtutmy2PjCFCLHGdlEVao7gDf44SgaLK_J8Vv1MWRIaKVqX6hPZqfXgS4JczRlcIFsrTLwwFwKc4mI_rHwUi7GW_184JC3sbuIJa58VkwBgTkVAvNOHjF9oHaRsvYyTwpsh0626pFad2X1UCXLEpo40J034uO6l-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22806bf3d.mp4?token=djR0BYidg0e7j1NRhtW8pe_zwICIaM7JxFMOYf6LMjvzDeBNxytISIpHhZxL3Ijaj8gQYUtR_Dbl7FlCs8u0HTnYcnRnhgP9rqUUkK-JeGTgXywfJbfWA65oLdKmbZSoOYnB4yWhPg1MXUZrNTtsvzf6immvqVPuhTCKEKap4rUtk4WMyRHjXJtutmy2PjCFCLHGdlEVao7gDf44SgaLK_J8Vv1MWRIaKVqX6hPZqfXgS4JczRlcIFsrTLwwFwKc4mI_rHwUi7GW_184JC3sbuIJa58VkwBgTkVAvNOHjF9oHaRsvYyTwpsh0626pFad2X1UCXLEpo40J034uO6l-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟! دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/30713" target="_blank">📅 09:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30712">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=dOSdqZZhDCt5i82yUiTjwzVCNqqtKFIlH8L7tR5tk0y5AFdFIboE77AGb22zxGqDmdWTJeJE1UC-3XOeagEGRyFLS1sBELbj4RManY_DwjGNlyq_kHCggAt444T4ln6EmEUVeGt1P6z2PE0Ev6NgxtZGisQ6sM9_rU1xXaCU99Mx-koISOdW_eHM2iYdRzZzQ1nNLHWdcoHk7uFuBJYHvCB5MfWvs5EHIU819RUX2W2TFn2cJVSR-PpIQTbckqL4ZcXeYeUYh79WXpzFcopIx9FC416TAEh-unoYb_DLsYHvbFO7XNEZMwKwmi8EwcaXdE8MZU_bJmktJ7DhQEpA3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd646dbb0.mp4?token=dOSdqZZhDCt5i82yUiTjwzVCNqqtKFIlH8L7tR5tk0y5AFdFIboE77AGb22zxGqDmdWTJeJE1UC-3XOeagEGRyFLS1sBELbj4RManY_DwjGNlyq_kHCggAt444T4ln6EmEUVeGt1P6z2PE0Ev6NgxtZGisQ6sM9_rU1xXaCU99Mx-koISOdW_eHM2iYdRzZzQ1nNLHWdcoHk7uFuBJYHvCB5MfWvs5EHIU819RUX2W2TFn2cJVSR-PpIQTbckqL4ZcXeYeUYh79WXpzFcopIx9FC416TAEh-unoYb_DLsYHvbFO7XNEZMwKwmi8EwcaXdE8MZU_bJmktJ7DhQEpA3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درفوتبال پایه تهران چه خبره؟!
دعوا و درگیری در لیگ‌برتر نوجوانان تهران دیدار استقلال و شاهین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/30712" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30710">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVEz4doFd0gVvJoPlQq1BbvwuRV3qvYvOsGt8wajHaIbEFHvIe0Xcc4YJlsZhX2BdRczEVfrdESmn4shVv2P24Y8nPz27ueIc7l6HKCTXThlUNEn9Nf5YJt5Bq66caVKE3ITG4ofHIxFbgB5q0Dh22wbV5cILJf_F_RxpG589zYxum2aOY3KJpSjTd7c0YRxohh6OyM0nluSpxhelAaWTgOqVgW5JK78_6-Lvw2vM93jj_Hyv894Dgj-YKL0P2fsEjgeCm9bSqgLFU68VbSKmz_XILDcL2ny87MU7mgBWx1Z4ow3-fDp0xclLgaejzgAfg57Ms6XrnldoZGW64MPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف تدارکاتی شاگردان مائوریسیو پوچتینو با تیم ملی شیلی در سن‌دیگو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/30710" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOpq4hEmenhJEBMmQRjrJO3PsyLyDXlYp6y1GWoEUbuVIpR3HQ0qxh7tRdKObSrce7xfjEdjRt93NxrIEYcc-7oz0uQgqxUje-BNzz3j4fo7GzSKnsnVpx953D67a3pw8Tec4cg_YUDRozzukzKkFe6e3LPncGRX9zE83jhZczyGi985-cEiqu4_AqunhLy--g019PmKDVAgpGsYmND_VuJi7qih8Kin9rPzxp_hykhb2RLztUEoWZLeo5s2rC_zyV3FaNk4mRoSv0pvwJ6M3bJt_bZG75zBoelk8SmKnkf0-S0YJDRnDtIG3eZl1995Fv3L9ZInB4V5dGkCvEpZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برد پرگل ماتادور‌ها با درخشش یامال و دومین‌باخت پیاپی تیم قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/30709" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30708">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7U1hiYILN-Yv87uYQNFayQOOK3giWZSCz0_Co9wqGs1-tDpGaMjYIG6uGWUbmd1w6yAsRt1paVgCnRlAyzNJELO2l7vTaJL1WEbuIuBStdC1MFRPIEa9Dd9xcrn-9EOl2d8JSw1cZScpRSzN9ed3pmlkfCnB6p38Yrp1ZtTlbeGx4k0dAlkT_XTC0wD2fHJVcTpzNZGl4MycRH-2ezzpInHG-H1AX3WES8y8Z64KbqVmgBkF6DGoJJuoLXSQDfQCo-XGp0GTX5n_9EZ10q0Tds5SrlTz67JjRKtPw4M87ztftm8n3lcZHTEqfXG6o45u4jEo62WTGJnO9Gm7xBrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج مسابقات تیم‌های آسیایی روز اول و دوم فیفادی مهرماه؛ ایران بزرگ‌ترین ناکام این فیفادی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/30708" target="_blank">📅 01:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30707">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIATTGQJ-vfzr9bfCCqngfArnX43bxbIIYZqFN0pkl626vl3fcIGjXUABF0xCo1cTZ8062-mWoA4zevs8sI5zVLmXu4sECO3OK10w1OTuETVvLMIqLAQsJ8zFFoQNxvVVy2YbSnu-7_zLwQSIEjpHcqDO_NvEQrkcweRsTAVdIekxpApcKDfdYolzXEpsHrqQhxcZanHctdiyQecMU0Cc9MKzAItkKtubsrP-SBSp9KltqP4igkIwMw-j5Bj0nGgRDRe5hlQWFQNwhEf-1PwO64XMY8Ljzp2nKI5DgH5BN3X6EIeELHzbtQ3xPJ--yFA35vnHJVbAWI-Z6iQcudeag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/30707" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30706">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuEcZEqMcqFvqIEyGJFUnYtudlOgcLrmrCCOQBGhmY2nOjx2xh_3p29PtwOLl6pYDE5421HhJfOFAjOcRQnnpFYYVGGe4FJr_B-w56aT7o6q8vEHi-K55TzWn3lvEJdaUWNxWYeTI526q-blxQrtUcV-YWh5AX0Fqmg4Q9_B9UQTKYK0xyz7hsEWEwPNhodgyFhMe98nMSQ-ZXnfY5BPGjMUHApGhFvQefFXDotPkRTBcti6ofnDzAFGTHnid3npYa-3RX6nmFWq57VhAgS9vPcrCm6LxxAvjECXLo1VhDX91bgQdYp70uMVghRCVCb6O6FbSNJ2b6THaRuwej3k0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با شکست امشب تیم ملی مقابل روسیه؛ پروژه اخراج امیر قلعه نویی از هدایت تیم ملی آغاز شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30706" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30704">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1smZ2P12HRfRCZXhtmHEZoPc4g8KQJkaxJ-ExL3eHEH8xH09BV8ouCWDGuad2SE5eAAvhSImzvnCkMLHEVosjGY47-R28_B2vcNkFi3Fsz0olt00RcpT-YDRwxdQc8nCU-SP8WUu-YHjQ8J3oXbh8Emc5bPfM5alGVxhZq1Y4VHcbHkjUuo_oPj1ILjvZBnDEUVOAec-2TIXUvtLyUDVs0HsazHo8lFRyo-q-TA_hRMHa-B90TTcdYVuxcPKzVpS2KzNA8a6AVhQQIVoGAJlJPF0dwCtVH2NowTpXCqp3yoCZCphIB9lnvJ-550I5z_OpZQvBb4Q-aDQ7QhPOjsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ طبق شنیده‌ها؛ فرهاد مجیدی اگه اوکی رو به فدراسیون بده حتی ممکنه در جام ملت های آسیا رو نیمکت تیم ملی باشه چون تاج بشدت دنبال اینه اون رو بیاره سرمربی تیم ملی بکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30704" target="_blank">📅 00:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30703">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های اروپا؛ پیروزی ارزشمند سه شیرها مقابل جمهوری چک و آتش بازی تماشایی شاگردان دلافوئینته مقابل یاران لوکا مودریچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30703" target="_blank">📅 00:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30702">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY9nFbSN7hmuz_7tGfdXAXsRGxsmBR2Hgsj-IUv7rqpcLvVHaBUvOuVdWFEe2tU4MpoH-UsI3URH9dKlLNCVC7Z-hTmCmrNATz2vFV0zWSNZc9vUiO_1hK337BzfkGiVrI0p-wUOVdD3xNSUhoaFfP3kamE23BCR-iT-qaso-BsSpg7rhRgmlErqMQ6Muj5-5Vr5DHe1xl7r_Y0UyRWUAdTG5g5PxOEg3aY3sUtuA6o09dSsLVH1GQlxzFUhvJzyijVhVkHiManll7v6uHKPxrX1sHLxqsSaiMF3hBB58DC5i_iqWEvLhYI2evhv5XpsncsRxiKOAATSgFZGpb4bSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30702" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30701">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c014a889.mp4?token=h_kSMZsOU-km52jlx1SRzIrBqKJCD7ddq9Jxmf_LIRKFWYofv4TDLRgJWdMva9YV8pY6-ObyX6_gVehFMCEV8lVMpq5F1CvymRppmeJPtnJUsHViC_zlu7t-Als_uDcfjbcmy42cMukH2f_bTMa5_h2igvO2ScTuUCT9OSMY_rygyDywn3VLh4Hx0Ir-7fimexZ3FjeCNFN4SExHGrxunRa18yNx8FnXKiGGrCky2rg1_jb19JLUR0_mcIHHBexf6HHv7kwcKkP2p_5zMXRaCxCWnZlUcDGZgAopdlXgf4l2N9EbzZezaHzjVFDBcUznWnm7_iKg-owXyIFAMUK_WCCCvaGTHilORZVzSmtvQ6yjomnxyBfxDpQ0HhXt1LP6kd2MpVblD9IbNDtP32GXK_ABWF0LX53IyWJNWkH6PxbeZK9H1si5j8JHkKLnqV-c8RHC6nf0jIM6UERHMKNqXvizX0RXeOs_XOTEOlfatfnSBsthqkRX8tNqCPKFhQExAW_2HPNCRybOCvKOIA4f20t9iAauXk87e1xCfvFFWHNaC7F4xzghREaZg7KA3u2tKj7mUTEaGW12VcUWPIK9o8lusyHd9Qp7xEFgxS0n6X8DCE0Ou7YuKWRBu68yR2-0V8gt5UI1-NvY6ysRpbcqknwXWQjmMpN5S2UUfUC3Ei4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c014a889.mp4?token=h_kSMZsOU-km52jlx1SRzIrBqKJCD7ddq9Jxmf_LIRKFWYofv4TDLRgJWdMva9YV8pY6-ObyX6_gVehFMCEV8lVMpq5F1CvymRppmeJPtnJUsHViC_zlu7t-Als_uDcfjbcmy42cMukH2f_bTMa5_h2igvO2ScTuUCT9OSMY_rygyDywn3VLh4Hx0Ir-7fimexZ3FjeCNFN4SExHGrxunRa18yNx8FnXKiGGrCky2rg1_jb19JLUR0_mcIHHBexf6HHv7kwcKkP2p_5zMXRaCxCWnZlUcDGZgAopdlXgf4l2N9EbzZezaHzjVFDBcUznWnm7_iKg-owXyIFAMUK_WCCCvaGTHilORZVzSmtvQ6yjomnxyBfxDpQ0HhXt1LP6kd2MpVblD9IbNDtP32GXK_ABWF0LX53IyWJNWkH6PxbeZK9H1si5j8JHkKLnqV-c8RHC6nf0jIM6UERHMKNqXvizX0RXeOs_XOTEOlfatfnSBsthqkRX8tNqCPKFhQExAW_2HPNCRybOCvKOIA4f20t9iAauXk87e1xCfvFFWHNaC7F4xzghREaZg7KA3u2tKj7mUTEaGW12VcUWPIK9o8lusyHd9Qp7xEFgxS0n6X8DCE0Ou7YuKWRBu68yR2-0V8gt5UI1-NvY6ysRpbcqknwXWQjmMpN5S2UUfUC3Ei4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد سه دروازه‌بان تیم ملی ایران در فیفادی مهر ماه؛ دو بازی، پنج گل خورده، صفر کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30701" target="_blank">📅 00:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30700">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMBIcXtmNtPxAKk1dKFTkBmlnuqwQKnkCAHjeHcNVE5PYJr3sPuWx-TomeLRiSNAWjMrWc56nUe5r_aZifG6qv0Wx3EgHT7CAFt2uYNmjQpmZIV1kQ88NFrVgn2XipbwpwoJuUOTGAKRvL8_OB7l8fjCrG8NA1vCj3nYhsCxljHuSa9NGNzHD_B7fqwM4CdXpxU4hnZbRwz4MGT0GEwuRScTz5vhBHb12FovMovRmslTH0ISPMovm5bJGkySjKE2qKIHNmauJ4Bzyo76nhRR6ymZrucCCF1-cC8tBW7qey0wtKpnHITA_j4P4cbFdEfgNKrOI-aZUjNh_Yj3SjgSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30700" target="_blank">📅 23:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30699">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4PUbPaDTT94eIzfwj_F-T35uImPOPJGkhIxse7fYOYnJkCPUxrdrWoJCO4LyVQO8NDWD4zdH69p1fXpQ-kKotlq7ecP_B2ONbA4CFTchU1yJAPQNXSLRdEeupcSLvtq_33NVyVI0riQJn3g9o2pUfHNYKBL1RubFV9hCj8JfxppJJ11fzwMy8640PP-tkpibxDWCtA655up56yJm85Vgu7Oh1uC0-MH3sGY2CMuoStIcHD2eIgZDE0gPJ3E2gLbqj-KMTlxX77Ohl00akhRqvl2_VvzoeKMsEE1-CH-AQOzwL-eUu8jT2Etlf89FxZaEEyY7fO8mUEeHz8jE0uPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30699" target="_blank">📅 23:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30698">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42de6680af.mp4?token=Cmpul-cCXyJqqkgPyFvG-UxJELxBrxJOB37h7UbKaxxtWCQQjWGcMhr5gLupB40FUIB1-Vjgo3kxKZsu9JebL_vR0PY80f_XT3cDzP9XF2cj2Y_gHEPF3vkrze9-xsYTkVvGToY_JEFiiN5dbSQFQQyk_4FylvoDwCWTYbxic81WyHoI9C02dVFuDGbgk5L6UkFx1TNTwgF_rgraqDl-npKI_JvlkgjwshP5U6tulnCfZ9iY0QoP_VXynCTjRPscqmaJi7lNjKXRPGc4O6rMMPSFgxAJgUzgKhw8HKZPwBoTLL6w62-Oohyd2vFP9AhWSEzPZszHrLzK8TKQvhrPrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42de6680af.mp4?token=Cmpul-cCXyJqqkgPyFvG-UxJELxBrxJOB37h7UbKaxxtWCQQjWGcMhr5gLupB40FUIB1-Vjgo3kxKZsu9JebL_vR0PY80f_XT3cDzP9XF2cj2Y_gHEPF3vkrze9-xsYTkVvGToY_JEFiiN5dbSQFQQyk_4FylvoDwCWTYbxic81WyHoI9C02dVFuDGbgk5L6UkFx1TNTwgF_rgraqDl-npKI_JvlkgjwshP5U6tulnCfZ9iY0QoP_VXynCTjRPscqmaJi7lNjKXRPGc4O6rMMPSFgxAJgUzgKhw8HKZPwBoTLL6w62-Oohyd2vFP9AhWSEzPZszHrLzK8TKQvhrPrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛
فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30698" target="_blank">📅 23:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30697">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi_tOKOcmJ_qzb2jBjkSavZlHduFXCgcyaXjf3htxne0WxPpUratuiXDeyJrdMJWLAVbWWq76Vy1euNZcLa16neHbXVKwfCGcEXMI8OEVtbDddLZQM77XBSc8aKmRwYsUfPleBvdMbT1g97LoMWp_GBM8Qh88rP12A-2uupk3PUic8gTfmAHDDQ1uBcpyD0ZVTnYMppBhq80MRSpCGQmI0_0_9-r5H2BzPgWKXP8Z8RUekAJ8_jhiVtpiQPARHhS-d1qQ2XtSf3YAW1qh-Smlmo0smORX-0EKZq3br5fpDP_A26ud1kAMmPKoa6Jdd60WEYJVNLKQ4SJmGAiEqKa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توپ طلای امسال یه‌وضعیتیه‌که از بین گزینه‌ها هرکی بگیره هم حقشه هم حقش نیست یه جورایی. کی میبره بالاخره این جایزه رو امسال؟ سایت های شرط بندی میگن شانس یامال از کین بیشتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30697" target="_blank">📅 22:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30696">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVVgPu5yMFpDWwmIP3qMVBZbZWrg58LIgsi6Tj9M03Lzzw9XL5MUq3gw8onxhTkD9V3QACbMTHyF2IWwqRtX7g9emRLnPd5r4HQR6NPqykjz7DYgBP2V64lT4vmITe6du9DUI5FMzXqYUDR0YeRayU2NzDr8EidzH0lhSR5jjBnyXbIpp0MCS-Mm8LXCMfLTdVlVERAEXfykSYnZzqQ8TW9e4ZYvLZf31lXRhC5xLxA-QqaF4uY7-5ZEV1wF3yODY8QLBMXCH804K7CdvhBCB_np82GvZ8zqGZgeOVkCilltFq_aFbu7suEggJpis7EYQUL9FGpmW5Ypt6WeyMNFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی؛ شاگردان امیر قلعه نویی در دومین بازی تدارکاتی خود 2 بر 0 به روسیه باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30696" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30695">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZkKX9KIQvov0Td0ktNAReet2THfmlVTg4dO434VgMErKluDHkH13R_V5d10hUeAPLa5OReM9SpEwGmowyKZXyt1zeqlMVckXRBd9imrv_FHGT2kpseuV5SeTYaDlBawPabk6DZ6hGiE5_4drTzA_oM5H_7hd56Xc4VPQii_TPwGcDxRnyPShFPuuHr8v29JNwYLlNfKvAF5JZMgqHRQZI6we3iS1oBAZKSfYYaRmFLA3sH5X7Htjj5XbnM2UyxeEskFmFfBMC_STX9brSLvIEPRsT-rATBRKdMBsVbNW5iopWGVX_lsR_rcO81tE2pte5Gmlce9T58QGrZIwoBjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره ناراحت قلعه‌نویی روی نیمکت تیم ملی؛ حقارت سرمربی‌تیم‌ملی فقط اونجایی که از یکی مثل سعید الهویی که هیچ‌کارنامه و سابقه‌ای نداره مشاوره میگیره. یه استعفا بده هم خودت راحت کن هم ما رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30695" target="_blank">📅 21:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30694">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=pa6zAmizOuB7sx1z5OE9JilX9bQIAU6iWwKqhSkx1ChDqP1-8OBaEjuJiwN2rKgXXQKV4uEHpJW8PsL4Y06cq76TstLEnNoq4cGCy9XxLlFXyZqiCf1Gvksif7GdjSkTJO5ANYPFG71sFxvkYMUQ4xnRLaTrhMJo2MPg4a5N4TmKPO0sfpdvkCw4_aV7CIszswDgu0QWJn_49aZ2kFOuwo7oZ_qgVniScGf_eaBEo6-J6pOLdEsiVTgHTxWlHa8zFgdMoUsj7ypY841SVltTJSkNuYfD8hmqXU1v4M0BmAnn-bhNbVjnw5wZOGx-F0ZTS9G5UUB9d1-jwg8a9-pctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=pa6zAmizOuB7sx1z5OE9JilX9bQIAU6iWwKqhSkx1ChDqP1-8OBaEjuJiwN2rKgXXQKV4uEHpJW8PsL4Y06cq76TstLEnNoq4cGCy9XxLlFXyZqiCf1Gvksif7GdjSkTJO5ANYPFG71sFxvkYMUQ4xnRLaTrhMJo2MPg4a5N4TmKPO0sfpdvkCw4_aV7CIszswDgu0QWJn_49aZ2kFOuwo7oZ_qgVniScGf_eaBEo6-J6pOLdEsiVTgHTxWlHa8zFgdMoUsj7ypY841SVltTJSkNuYfD8hmqXU1v4M0BmAnn-bhNbVjnw5wZOGx-F0ZTS9G5UUB9d1-jwg8a9-pctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار نیمه‌اول دیدار دوستانه ایران
🆚
روسیه همراه با نمرات بازیکنان تیم ملی در این مسابقه.
‼️
سیدحسین حسینی با نمره 5.3 ضعیف ترین بازیکن نیمه اول این دیدار دوستانه لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30694" target="_blank">📅 21:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30693">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCAygj28hWv-0Y0KJMX6P0pBjtqYNMDa3aLQcBOwNTFOInsoiJlQCTquEtMuC9rZB-l7MieKzVmTiEopcfK1-DIr3SRyjN9LO0Z3TbVj32nwJkoFgEICFgGOuZt6FBUeXGwoIPMfNWUH-iVgDoAQKSurhrIeG4VT4-xphwz3VzGhCAMzhvFdDf4ElcFNGNLzP6E07lzZH9qgOse_hxhUIbsa6OurvLX-qCO972ezNeckmH9GfQn168LK5GoCOR70NI4_Ur4Vg8JE10nj1vTOTcds-BvcDbzfyfd38exW6iZtSSIZwMw5nw7cdl-ZHODxy5geaAG-XRDF319vwDDscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30693" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30692">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JejV5PSQLXN5rRO_9_qIkpXSZl8_Wq11oB9hCoiDhrdWO3NjLjH_gOj_N4BVMVtyOonioLPnpWs31buYitqL21DyN3Pq1tk-P4VBFDDg_Fqf6lABuI8JfRhcFjyVpLNgn6Xd8HMS0WHQGMTNR1GsfyoexlBiW9GxeG9WMKKHZLlDsBlEqvRPK6PvvYXEwdal0UowS0UgSMIPldeW98nqVRbcaWHQ9lQ3srsWNqGyhwqS3VyHXU6zpM4glsuUZG1gtwKjcHIj2o21o7UGETAb2_QY53Mf2S1Z83GUwxk6Jyu7N1-zU-MkrUqPKWwhOFCgNe23ievIOsDsTsmPMUNROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30692" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30691">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=aGxQih-fMjS6mcGT3xTtE8OSFsysU_swUy8RTNyAk7Y-vBH3N9wTf2oDyQ-XqXfnCcnwEo6RdWmDqReUsgh3AMzpUPhdIhBVRX-6DAY7sNEJSXxXDvrg_C3uLvMeR1i55rNtXQQ0PSIXWXwD-lX5AwXUiPNeGC2CV7pDZq31KJb3bMw5c14L82fFZKtnIaJIFFN2Zk6SggslQRc5JNHqHvRm0nNL5DqkT6LOzgBcUvcFlbt3zS6F51CepdN2cZ7HJqaNbeoMAMrDErrgzuLwPFlm2m0pZ1xg09R7h1SJmViuBTzFcgYRFckPhgD5P4hZy6fg60I3LoSneOZtFnHTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=aGxQih-fMjS6mcGT3xTtE8OSFsysU_swUy8RTNyAk7Y-vBH3N9wTf2oDyQ-XqXfnCcnwEo6RdWmDqReUsgh3AMzpUPhdIhBVRX-6DAY7sNEJSXxXDvrg_C3uLvMeR1i55rNtXQQ0PSIXWXwD-lX5AwXUiPNeGC2CV7pDZq31KJb3bMw5c14L82fFZKtnIaJIFFN2Zk6SggslQRc5JNHqHvRm0nNL5DqkT6LOzgBcUvcFlbt3zS6F51CepdN2cZ7HJqaNbeoMAMrDErrgzuLwPFlm2m0pZ1xg09R7h1SJmViuBTzFcgYRFckPhgD5P4hZy6fg60I3LoSneOZtFnHTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله ژوله به قیاسی و قلعه‌نویی؛
وسط برنامه زنگ زد به قیاسی و ماجرای مهدی قائدی رو پرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30691" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30688">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHmhuyUJRH0dKi4cdC_Pr7kcSS4-8Wzsco1YiWwFpGqc3yPihDjNA0ZJSmdFZaAxmbAb-UjwRVZyHBsci99L7kRE255fh4DsSf1YotJdOZIM26QPujwixCOGxEHHTDGH51KkcTCAsVZHaMBWjGgwtxKbBbuShHgAXa110EixRb8NYmkXKBgkdzfzZ9uAmf7yyAF_d5QftVX2q_gjsUNy95Fus5rHV1TZtkFOLc8nnsB7ugBWlF07Sxozs98fdvpJCytPX_X9_rywl6fRCZMnObJMYzYzn2Bw-YcSS-VRZtEl67jPjERmlBguxYLxJVBiWHrGVtwYmRQ59wpmaHwhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBSw9dZij9YjG-jp1txJ2CFWcAyK9JZaVGmk3ADpwx2PATPvyoyBAieHqexoang5RiEETaagfrtnOMSGt9w2smWtfryv3AUb75CxqtGPhzDZ9KupQt-FJVdjeTzrWGOWYPlTNrs0Ye2f9sapwIbE3c6chCU18UgaAnhc8ah4ETRMTO1tbQC7OczVGQIQWvPDiMIugVq9DriYDOvQM_-Vrvx_suZBT3X7lLLBJJxoohligrHHNRBDrFKHtPfvkb38RfbEkUlk5qH13UjgsmJeZbxomOxp-Y0YDdFmzfAx2qZlfrLKHmVtHx1QfKZ_FB3yDuVBYWBO6k7m42C1De5h_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دومی رو به این شکل سوپرگل خوردند؛ گل دوم روسیه‌به‌ایران‌توسط الکساندر گوگووین در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30688" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30687">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=s8FuYUPGj9cAVrX99EzN-fUDnTtYa9S_AkCrQqpwlfUzzsd6HGnbCcxtuFIlGzZTxkm1bZ9sVqiRrozZeqnJLOHWjnevgNoZ2FZkhAdb5NiFAkxsHtZ2op4x7KDcIs_beWDS1ig6ZeXqErgFT0n1OC4tSEuuT0iCxPE5jf89FJrpd-Ax6EpmwGoZd-TzxrtVytHxxgSL7uwFtSxNhEEZAuWCO0MUxeewz8K3VO9dEpuzOoDf01Ug0-DX-mwvOTVtJbMd4slAhaveTsRYSabOOt-1LZfiLJ4S0kRXH7uAl1hzGDd1ZvzH1_qYX3oQi6jBrmVquTecpKYzyKQ-r2WNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=s8FuYUPGj9cAVrX99EzN-fUDnTtYa9S_AkCrQqpwlfUzzsd6HGnbCcxtuFIlGzZTxkm1bZ9sVqiRrozZeqnJLOHWjnevgNoZ2FZkhAdb5NiFAkxsHtZ2op4x7KDcIs_beWDS1ig6ZeXqErgFT0n1OC4tSEuuT0iCxPE5jf89FJrpd-Ax6EpmwGoZd-TzxrtVytHxxgSL7uwFtSxNhEEZAuWCO0MUxeewz8K3VO9dEpuzOoDf01Ug0-DX-mwvOTVtJbMd4slAhaveTsRYSabOOt-1LZfiLJ4S0kRXH7uAl1hzGDd1ZvzH1_qYX3oQi6jBrmVquTecpKYzyKQ-r2WNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولی رو تیم قلعه نویی خورد؛ گل اول روسیه به ایران توسط الکساندر گولووین در دقیقه 21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30687" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30686">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2afda25603.mp4?token=TX0mTDFLP5HQE4RW8W1ltV4bOoNf1MMIl2LluGDA-ClpsyytVyr7ZjHKKbV-YuVPFe-d0_qTzwearFrRf037DDooPs9uR-miJDpvsB41vSbgoY6C5CKxojc5ecgX9NhTP_jNjyT1mzK4xkhNzW1O523ISNIe0c_GAAeyZbCURtMRqJ5RNqDkErqANOucoYUBx9LOlNOLxXsILiMXrpm4gJxlGlwyq-MY6iMCtg1gHKhynjLMFOuu8Oje4QNzm_3j9CES0n8GqHjot1s-kX6VIoUo9B6cLSf2ItBvZ2GvGysmAXSgrLCUObNlvj4iB0vEjI968wO_gIw5w_JAPnWngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2afda25603.mp4?token=TX0mTDFLP5HQE4RW8W1ltV4bOoNf1MMIl2LluGDA-ClpsyytVyr7ZjHKKbV-YuVPFe-d0_qTzwearFrRf037DDooPs9uR-miJDpvsB41vSbgoY6C5CKxojc5ecgX9NhTP_jNjyT1mzK4xkhNzW1O523ISNIe0c_GAAeyZbCURtMRqJ5RNqDkErqANOucoYUBx9LOlNOLxXsILiMXrpm4gJxlGlwyq-MY6iMCtg1gHKhynjLMFOuu8Oje4QNzm_3j9CES0n8GqHjot1s-kX6VIoUo9B6cLSf2ItBvZ2GvGysmAXSgrLCUObNlvj4iB0vEjI968wO_gIw5w_JAPnWngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30686" target="_blank">📅 20:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30685">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKHDarsg67XMb08l7RdtjCmJq5tljUYf5ICE3sYGSafPPOEFfzc8hDetX7dvCU0-nxW944NRfTunq-0e7Wmcb_jjQvSKmycyb29BiK_tWoHB5drpYdkdsAU302grjUTugXlxAe3L9rgMY7hrDvDo9fdJRCkFMwm8nNVw61COmvECL0qsY66m4iYr9LpZtLTFpT96ILmxAQxZU34T_60NgO5LVD4RwGc1JQRhyAIiiMIKzquhiYGXqqDpvXzGO6XNhPjxF1ThWLn6aCqrs2ZW406Jvck8hkFSdPfHEgnjNEM_Gj9QJ-5BeY4Lk4KJ3UrRGV2C0WWISc0I14rpO8yyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30685" target="_blank">📅 19:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30684">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn1OFM7CODKMzdomTnBrjWsqJfiTLFthHiR0B_QHtJD2QDUunZ6478QbtdrZYup8U9H9t23CAt5Vpm-5YJtx5TnpceLPx1GVUKhvYrat5XCAIpoyMliydehBnKDLT1RVRQc15OYAkIP14iBuWkXxUYn0gl1MifqborchzGABpKBranfzJ46-ZG5O7S3_kBIoh61F5ABPEi9WhW8rg2CMqDJ3g2ZtJJxQP8h9k3bW0XYYBCkSGB9YYkU3NPi_OI8UZ_WgTfI_S8WDq03GyM9l1i4qCWzwLr2S2_Q215hrDlNqN-BD61SndkTzVuLSqE4mX8gRCunREaMop5ZSKBzdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30684" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30683">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_oUjQik2GOXQxhER5QH4PS5z-KMPkEJkDj8ESl_ZDNWOIEbgbr_4mtGVIkckopGuqK48Uev60I8zI0pemSajijJ_30puWMdcnlGQfoFv4BWBZMYHRVYKnO7lhx_ICcknn58McaTsESralrBq47du42t8IU81Wtu0A-_kQPhPIm6yj86nsckTqTI7b-BEYVPr0UKzcMSC2_jtGkXxBuAxVzxVLDUo194CJr2FIDT-XCYDAZXJdpq86arGu8De-v74ZevBoTvqNhF9MkcDa30oVwZmeuCLGc-PZg6u24UHWHSVtaN7l3azq2n-fpBEf-jUmhEzgIqglEobcGFWLZKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30683" target="_blank">📅 19:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30682">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1xsMPhE4GeUuZWkJFz0qFRkq8-TiZKkHwOJdicL9QkOhmnEH10WySPFW9INWbKk4o6JRu9oZkCVjX8X2DNRQ_Hdul0aDhyaEdEjJQz9b2ycgZBTXfkr_ZarXpS_s_fvZNbg1BqIY7bHxUoCPPCxvURKOnDgO0D2gaTSokjnyBRyvgraQvGPoT9CcHQGfSgE-Y1NWsyXMvq4d92-_BgF_rozfPI8ZeH-ftYRtfLXP83WUODpVjBgAdbJtOaBXo9sdhpcHCIBoyuB4AJTXDpPTyVG5jiNQZpfhXeqllljTES-8-yLNOZhxSMbkYxm7eVSnMHbwDX1W62JFTXGxr3gaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30682" target="_blank">📅 18:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30681">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZGpV6dKE7ALndG9hEuNnBSOLN8ZX6GzSGFRF2QX6QPUmAQW15HcCIcgwEAY06mn5AO2rXLMReaflT5oiWFKWEAXFZT-DG-WDUB7pe-KQcwcULqxsAOYU1SV5bD8OYz5w51AHxpYlwk_qnFAv20qlxkqef1JYdx77c1844CDxydMKvYC7RpSV7P00Nzi74spf8pmmf-1_oyhGK07_vk9jNk56zFu29eXMju8IllAkScRsoPjnF24pCwppSveP_f_Rt0LHkckTyax-ZyNvqYPOy3m-hZom8MGmgnK0scXhuItwpirnk-ZQ-u7uwt8jxKlHFzQyNWvNhVNU5SY6d42JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30681" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30680">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKny-cjtOHc4X1--BcqEHlBs27Bi79pfKSIa_N5dSxDu7lAo0mzBBJiLGjeb6EkTetPGVC6hDaAYaO0g-mAFddt7Iu2fnDAT2CbKpVNTLVkmJyu_hDxxEH5iPFLvsA5RthGREvjmuLYg9KMfxKN9iLKHXqU7_-KP8oeoiKfEXv4pJ2gcAwzOJiy3bkEI81UYL4p6z3dgZFt1HojVUheUls3BHFyF-g5rBzx8bvjLw92OXqykv-SWBZp1eSyfeKLYKyiW_DFSrbB8VcuXMXo2AfXC5jIhgpRR9uZvJtQAybX_Ey1xV3ysn_WiPsWMGVIJAcG0VRxNbF6OitZ3EChjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛
ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30680" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30678">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-llfwoRKibYtMVx5UecwAP4RALeBkzA2LXP8quZr07x4EJ99Amvkn_yFb5_YRH16Cc_ACRrer9Oocf1TGX0owklR-l-AA18lyC-OqgMbU34qYZAd7aO4Xq0lITs1ORAvAaC2AbTFTL0EFwqy3j6dyhaFc3QH0BcC9bNjVfR7seJtjMSexYuJJ7mJy29vbZ-VMUprQOAoULBMMNeKvxHR0ApN6qA_KLmL_eVuSxfeEMO0D5wBqdb7dF2Al39cAmBcKixF8OByxyFA6TVhvlu_qVSHlL0cTkmv2_IqCLT2QEYjGPtJIh-eVsmkxQukWG50ScZ7o5PxMjKP7DAL3cbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAJRt8b5KbkimJsFo8b7l-jICKQNlTCFap_ppOVlICx7EW2OBKbu0_rSg5H8KpHKKdMVR2CTKPaSkn6M_gbqRToQjUmxztpvdgPFfibd0FzwB4oCS1WjUrN_WY3_s9ncX6vgrBhrpo_dudlHMZRyp1FT7WkkrJpnPEUU_-a5bI5nhHtE0c3qkegeNtkBvzpqgABTH6-y-9v6a362Y0RhAfQTwf6d041dMHvlVtcACQMbJBQ4hE-JEMFZps_nEhuXZ9yj3qLxC1gPXaisWP7FnC9yQLIOPyEu4OrINbnuEQfO5jdtRA7hQfy0jhOnYxUejLCXqXZ7qGiBjC8b-BnUTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30678" target="_blank">📅 18:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30677">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=AydTMoS0B9wMvrg8TJWr9bGuG-ucXxzsKeXQ_boGPEDpBMaM3TX7RzflajbJzQdNEBLRWzd4M-3s2cncc72siyCdjX7RFletuv9uhJa3p53AO8cSC7DccAgokH6Jlc7q4kosqGhSPbkCZrjYB-Mq-conYX6_icawUzDc2-doYMaMrFKRp4CmRGSIX0WVcv5NjAzyw35IrHrewP0M_tZdbPqvnCqvHCSsY8DVCpXuO1p6s7ph5dBisWC7kwETByzhao1Fb04SqR8tvxViVXfnf-FcyBEfjwNlnCuBZrn5e2YQDV_4OPSmo0IBWsZIpWwQvuuf96NZjPYj8fbj48WuQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=AydTMoS0B9wMvrg8TJWr9bGuG-ucXxzsKeXQ_boGPEDpBMaM3TX7RzflajbJzQdNEBLRWzd4M-3s2cncc72siyCdjX7RFletuv9uhJa3p53AO8cSC7DccAgokH6Jlc7q4kosqGhSPbkCZrjYB-Mq-conYX6_icawUzDc2-doYMaMrFKRp4CmRGSIX0WVcv5NjAzyw35IrHrewP0M_tZdbPqvnCqvHCSsY8DVCpXuO1p6s7ph5dBisWC7kwETByzhao1Fb04SqR8tvxViVXfnf-FcyBEfjwNlnCuBZrn5e2YQDV_4OPSmo0IBWsZIpWwQvuuf96NZjPYj8fbj48WuQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابوطالب‌حسینی یه‌تیکه خیلی سنگین به ماجرای حضور خداداد تو مدارس مشهد انداخته و لحظات با مزه‌ای از وقتی که دانش‌آموز کلاس اول اون مدرسه به‌دنیا اومده رو نشون میده! عالی بود از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30677" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30676">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30676" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30675">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
قسمت اول اتفاقات بامزه فوتبال ایران با اجرای امیر مهدی ژوله بعنوان جانشین ابوطالب حسینی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30675" target="_blank">📅 16:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30674">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGkVKWMsWct_ZgODx_VWSGh2hD8Qv6VvjHGDbJKtofD1jio48OgYH8DvrJwnZAoFWhwsIuA4Br2Cvy2RWNOoNFJ2O4RlO4wqfF3QrHYIRP5c_VKKnj7b8x86UpcOn6pfMyYLNxLilRzVNtWMNW_bi_vf9Vf_wDRSb3cu8mGzuO8yVfVMBYFCpEAiMlK-1rIJHfOTc3rxtA7-01mKseDZ2ex0qdJ1NXHuPnOTKpY8fkm9GB_MgPfugrRFvNwsKXqBc0-3AGjitDa03QoTienfgJ7fGf5HN8TUXrrCj9wbBX7UT1dvE_3CUx8nDQoWyGhEcoHS7k5lKj5xpHrmnziulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30674" target="_blank">📅 16:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30673">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNfNhREIXED4GvXZFB1Wo8xhnwN5nZnkQef9VHuBuA7_oBgNCrkKENhBTTiHFGdBz39huOCMeNsj5_aCP8hcX0W6yeqUaJhaolgpGnAjyA5i47ORhsiHLa4-1GQYU7p6EjG3ycJ6cMHMK2MeqvRWIUvTnII5Xecb-OPM21zG2z70hyaPAlqPzGB-xhEbiNY6UZ4BQLhLoMHN1UNzzAKVp5cHINKc1Iiu449Jh2XT318ki_TDxjyHIwm1o8J2buoeEOGSH0ed08lcJBueOp0h2mQGy2kneIvQ-jaI18No9sQHOpkqJD0SpGzbiwYf_BiOO1IW2WEtHM1X6oQLzGpuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30673" target="_blank">📅 16:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30672">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF-gI_r3kBSHI96aW-mbe9Axl629K3gL0Gi93k4g3gZIOG2caH4qLX6j7hGpZdhTush5lxHjVsVVWlGF_TIySh-38-LdRBOGiF8ryCHRQS2Irp2KXvUIYy4Z8uiQyNRhiVZjt1XfQuX39ab2XlmFDfY6SzSCvbu0tWzZMv2gsH8lkB2sNUBUOSw4LlliJxR6Z__cZc3eElYZ33I287FMjhY6Z95i_Jo9pKptC6N8_DVh4vUE2NfPmtEwVm9WVgwMFp6E0gBkSMoDpqENZnRJuo_SwxZdmxC6o_PCSGCUYmS9q_teegJ9oCDBg_2Dm9rSkO3zgzqEPirgKm78DNxZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علیرضا بیرانوند دروازه‌بان‌ملی‌پوش تراکتور: با کسری‌هایی‌ که گرفته‌ام کل سربازی من پنج ماه است و احتمال زیاد به فجر نخواهم رفت و در همان تبریز به‌پادگان خواهم‌رفت و با تراکتور تمرین خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30672" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30671">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEm0zFm43HnrG7tGcsfksSW60dM54pOYqpFd8lwuD3_s27S2jfPdxE2v_BzUdeWkS5_l2OJYcGq5KcyjVQZdcLm5cdEZaMWYduUbu_oPdh1lhBQOXUf1TQ61CD7r9uPbMTRCJ4T0DQuLG8ycSB4y2HD9wp5KJYaOvawxJC9e5pdAd5AzbqVcl_tnwwfCgif7I-2pzk6pPOBTzoyULbeiqMkrChpLiZuV2YdtnTGn5Ob5NGx5_Y6TaK3HtnVb_GWoYW5NLL2Acdn_5YlX7bWd7n9cgtN2a-rpqlFMuwDm2w4bCkfkuG1xjJuOCL9O_6B1id67ejKyL9g1l0pzzlOQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ باشگاه استقلال از روز گذشته تماس‌های خود را با ایجنت یوسف مزرعه ستاره جوان تیم فولاد خوزستان مجددا آغاز کرده و قصد داره این بازیکن رو نیم فصل آبی پوش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30671" target="_blank">📅 16:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30670">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6x5i6FoYpcPCjLln5j64keiOvdFeVjutKYT4ZjcgJSDW-Eev3TqgGky2Lwbh8FRy7UU3yJTN-FBnjbr1G2eHDll7z65s62cpzDy582VIRMs8pDeT4cLXvbn5siXVxbBVEvqmqTJAvWla8S2-7JGK4dDm4WjCTzA3x_TWAh8utbn-NEcUPCPXYYGlFglwe0MwLa7Lwpu3yvH4gi-R9DzMeohjQd9ssEgveM8DA6MMefTSuNrCk5jz-zdLNZSyGriJIQx1cyuivCqM2hFFfk-vcR3VA8jOfznz7buhmp3kbibnKLJ5nNuBaT7pWmB9yHmDAfr8zwxzKuHCsAv3gQmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رافینیادیازستاره‌برزیلی بارسا در این فصل در تمام رقابت‌ها؛ 15 گل زده و 4 پاس گل؛ دربازی امروز برزیل هم به دلیل درد عضلانی تعویض شد و بزودی‌میزان مصدومیت او نیز مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30670" target="_blank">📅 15:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30669">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APD2MmHtwqazxcFgyjEUoqTvzcMkQegMIztVBy-qWSu7Uro6X1_SByWuLWkqCo2YbFpjD4auaEqy-eJmwywCpYtnZK5H1NIPChZpX9KdJ7Seu_hGlMSQBqgeIrRhfufYe5XwIwTehAL8HFMvgIICQ25c3jMBE2omJOKXgWbbXL7GDNa0PxVwBFZOfHvhBrEYyo5OecNBmgvGbTukmEBdEKsz-tCPtJc1rF0asiLS0nvF8afX8wRCjFqCOulvZSVGMlX4bTnxkQfGkf3gTdsLm9EWTQzubbMkOO89_OY3hdVzzDqu6tY2kXo3jbVntOiwnTx0TN0IJtMY9xqZdU8-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
تیم ملی امروز در هفته دوم فیفادی برای دومین مرتبه پیاپی امروز ساعت 13:30 به مصاف تیم ملی استرالیامیره. بازی‌اول بزور مقابل کانگوروها مساوی گرفتند. امروز بااین ترکیب به مصاف استرالیا میرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30669" target="_blank">📅 15:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30668">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmFBINKOgV-Cti53k3NFIriy8wAAz2JOpCxj1KmJk7ifxUdJTCA4FVR5Y6oLlGVR2JdQztA04P0FEwF5KM59WuvgpWITbM1lK7PI2GV3QUafnUHrBiTEoDUpvVvOGL1ywhvlpiJtElT0PJpBaFNzPOW8Jlo1C_UXcjbktUJVRqC6VioRyl72NcdctetUCejUTCu66yMdZ7n1D6HeYZqMQkVsr3qbVKU48h9-WbLVzwXGLw7cIHOblUikzYgkAL-63m4xiHTAPxqvpI3JcwfMru0dMtlDc-qLQqUQFgPujPGKdE1L6NSDO0MioKqf_9EYbZum4o8r5fVIChoE8sgxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30668" target="_blank">📅 15:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30667">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVkmLqkYaNDmLFA8XFj3esxcLl5CGd5RlGJ8kQm2PZvQfMuoTfF4grjtBYiDEy6KcSZbb9kUz1d3l_uDmhsU-AgrauX_qam4A6S76qX7JjRSR5jP-96673hLeeCt24WsXOKC-rTOOIUFQBNLf5k1R5t2ZckxZkqQNHRgHbRAFKOVbxvlRrz1JWPdn5GQFinnThE_TDvMGJOjao_I8MTq1UDRUENNNqXP9mibhgOxupQ4dxISdxZMV4oSA4Ec8eze56B-OB-CNBtiTkJs0GkpW3tQmCJv3Eandh_DDz7ZzJro80xPtJA9IGWPNkGEdkP5ylJQHb6lwmwunnMUZpCdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سه خوشحالی‌تاریخی و به یاد ماندنی زین الدین زیدان سرمربی تیم‌ملی فرانسه و سابق رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30667" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30666">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
ویدیوکامل‌ویژه برنامه شب‌گذشته عادل و برسی اتفاقا اخیر فوتبال ایران با حضور یاسر آسانی ستاره استقلال و دانیال اسماعیلی فر و شهریار مغانلو دو ستاره باشگاه تراکتور؛ اینم یجایی سیوش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30666" target="_blank">📅 14:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30665">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
ویدیوکامل قسمت‌دوم برنامه فان و بسیار جذاب ابوطالب حسینی؛ عالیه حتما ببینید فقط رفقا یجایی سیوش کنید بعد از 24 ساعت این پست پاک میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30665" target="_blank">📅 14:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30664">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX-v53cPOqnG2FBxMbcGmeT1CBBCPyznz1mbxEWCMB4T7pBXTQ1uxTugLHWWfdckpCN-BQ0Q59fiXIkNBN88JNLmmIjY2KVM5yW6nTz-nDZHiZGMIjatCx1xV3X-FdK93e3rjXo7UGmQ6ahJ5F0qOSQrTzvuZ2aUpdwdIfZBMbe374_c5Ybi5seOMwGAvDOwxbsWq_uwa6w7hk1H1PnWaJgK8w9wg_-SQBif09Ipke5ipS6PdtYBkv3nSyJAPWeQhwff-kRi11twGZ3cTsXbq01JrdoOici6-rlfYmACmqTra0dc2GraP5YkEYnW0MyIfRgfW3eeKNt29KHfL8B8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30664" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30663">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=rObU0pNTTZ6BgRYM-rHt54W93aVWVJyLypIht_4vfc7uTFm0NP8KR-lhBA5lM5xkabhOLdiCffPhVsxfG4oGnmrezNRZ2tl4p8hwpYI6ftSZMK5o_wBAPWNyAdgA0YxMUNb9wlgVYyl6gPAa8_s_QUIFbpLe88WxfbqKR2hHGAs3onabkOi06PIbH_AtOs1Q_KCtdhINYF_wff8_3GFhJ5mibUECRxH2qNvOHJIfzSkXvr7f-9zI10b8ipaBtmRWgtY6JwowHotWKZIEkNKa7C7zRgQJk88soLs_6kFDVNMqdtUEGTH5h7h3t7KJ1xPUMm48Ny51lMqbD0BsOz302A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=rObU0pNTTZ6BgRYM-rHt54W93aVWVJyLypIht_4vfc7uTFm0NP8KR-lhBA5lM5xkabhOLdiCffPhVsxfG4oGnmrezNRZ2tl4p8hwpYI6ftSZMK5o_wBAPWNyAdgA0YxMUNb9wlgVYyl6gPAa8_s_QUIFbpLe88WxfbqKR2hHGAs3onabkOi06PIbH_AtOs1Q_KCtdhINYF_wff8_3GFhJ5mibUECRxH2qNvOHJIfzSkXvr7f-9zI10b8ipaBtmRWgtY6JwowHotWKZIEkNKa7C7zRgQJk88soLs_6kFDVNMqdtUEGTH5h7h3t7KJ1xPUMm48Ny51lMqbD0BsOz302A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30663" target="_blank">📅 12:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30662">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5uvmT0T0LfMxFWYmg16HJpU6kgMDgnXnIju3QqxdF6ioV3SUT-SEotlKTxFhBUPQkPr2Qdfm5b2YD0PQO3aurtOFDMWT0jE_Wnwgr9Qba1war1l_RYKbNOSwH9AcO0740B2SLGOnGsm9Jlc4bWi-C6IUKLeGy6egz4MproDid_tDEZPYmEk87QfmyeRc8wEwXZnrWB36KZwOCLrNXdkGiuBIkknNSYSD0glPSldj0C2TcjMu8e6GSsE5yAKMDgK-qkj0sMtEgiLdlL8cscjs0TZ1vTeAi_UIAnAT3fKMlRjJ_GvI0vwpPpQ2th0WC3S7Murs0e-x6CsRXWVhZtzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30662" target="_blank">📅 12:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30661">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=m9Xzi9STZa0OC1KVUENy_R-WtWS6FhNUHbfybv7ijHI0_zNN4Rh0NuKtzumw05-vhKdann5oScbpnmdlO_XDhIB-pm0rlxnNqvlMQjftf8fU6wGpF1NDNKM3qbYLdveaVkuYHaRmMe3TFrdKfk2itih6dcm11BoMK6pAZu8yVamrqF__B11T2KcidtstLuWx8gW_i6n8vOCs2B-nw5VjWzx0qUSV9RYpnFfZS1z0YC09rxa9p3tj95jA5GVjEWNtnCRqGvBLwzlcPi5uuwNLR9th0LLVAl6d6kh6nFKrzu4I6xESIuSQ8WHsiBoQ-qV05sRzJvSs0NbA3sutpY1TWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=m9Xzi9STZa0OC1KVUENy_R-WtWS6FhNUHbfybv7ijHI0_zNN4Rh0NuKtzumw05-vhKdann5oScbpnmdlO_XDhIB-pm0rlxnNqvlMQjftf8fU6wGpF1NDNKM3qbYLdveaVkuYHaRmMe3TFrdKfk2itih6dcm11BoMK6pAZu8yVamrqF__B11T2KcidtstLuWx8gW_i6n8vOCs2B-nw5VjWzx0qUSV9RYpnFfZS1z0YC09rxa9p3tj95jA5GVjEWNtnCRqGvBLwzlcPi5uuwNLR9th0LLVAl6d6kh6nFKrzu4I6xESIuSQ8WHsiBoQ-qV05sRzJvSs0NbA3sutpY1TWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارتاکاشته‌از لئو مسی فوق ستاره آرژانتینی اینترمیامی از یک نقطه در کل دوران حرفه ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30661" target="_blank">📅 12:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30660">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHqagnPATAZWplE0p4BL_OZrFsA2ok0ejsL-_A-cWZUcbHYlapDsnK3pTrT0kl6VgjHbY0syuVcCgBdNgrCF9Ag3MCvhoYNEgXyV84qHo0Ona1Zduuv3MTpXOEv5MH9cz0qwgniZwj1EcraH5yaV5MMFZDfdjcbGPJQnGqFWT2BJZ2UrbaTJ2NEaBxe_9qJOLPQS_UU4nmeKKJQWtlp49CN58UY9KkFbhR_npAD4Y3FQOgx0OdqFs8NcHb5X_Je9guO7QH-CwBeLxtMoXxWISrx3kXOvdIwk9-nf9p2K62chCRlk173N4pu0242YVB612gwZoB5tRMeM2MN4Txi_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علوی سخنگوی فدراسیون فوتبال: از سوی چند باشگاه لیگ‌ برتری پیشنهادشده‌که جام قهرمانی فصل گذشته لیگ برتر رو به شهدای میناب تقدیم کنیم. به زودی در این باره تصمیم نهایی رو خواهیم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30660" target="_blank">📅 11:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1H7MBOcEkq0PQxvsjuc60O-0CxpKrl6D6Dr-EqU9YafFLhDriAoLCrZRZcgwYMGQ1wEAq7qsoefPwzJtMRSkpcly9_ADB1Z1E2q1GVHnDnrYZg3GnfB_WjpX6a7lR8JwnY0BOIRBheLcrxg0c25X-QTBngDUJPYfK6G3ihbVtksQA0a3I8SJtLiMqHh7xyL5TTzw9GdehdU4sMsqI-Y_wsE_JECSKDgborDiEyO1nWJVWtm5s40tmcPABxrbAw-hPzoZ0de8MbkoL__UhsXG-6DnEd_IybWQOnUHi5BnpE0E2JumnIONOpWUuJV3naKqC4lBA0qZvgHl79K8LTyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زیدان درباره خوشحالیش: دیدم اولیسه چند تا دریبل زد و باخودم‌گفتم الان گل میزنه. به گل زدنش ایمان داشتم و وقتی گل زد، خیلی خوشحال شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30658" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=u57cWZbu4c21lWe1oxfyYmrmAePWSJIDCrZmqFaUOJHTgColvB8UD40lROH4m447Sw3L0Z-s3UVkFkHUIE-st5dVKGCMJrIifvoyKUlGJlsyk3A2Y7Vyfbh-SacqJcyg4qS1oYuXXlW9Id4FIHtpcsUMZR1PQUzpFq3EXM3U0e_qw10wh8aHtVmU6OMsD-5Tmk3cfqn2fxOdI-inhjyYfTSfYP8uuyRiFM5XH27aUbsfR0hUEaJctVUha1FbKcx1RjCAHxBuqNDQV-vjx0OVFE1gLb1n00dMszSi7ojiQBNr5UqI6mtXWBPMirlB5Q93_hUdXWyNl4g-xtfmQ56Ca5vY-9paGCiM321HtGTY8wphawETOfVhHrCewmrHT6JPDXc-V4qHkwplt8AgxjU9ni6TJWurVbUecTMUe-4Bspd-smxmcesA2XthaW3SGhoxUeHPAB0U45euFYzXqGOOdmuJx3Ej7R7XWOYLNhQYgbitmxyeOFRtZX2z1gzyFuXA3E6nI6gA7If4wHJwzk6DWMdvdjg0Xpx16tXB59kf4C4oaQeiYpzDP77yu4254gpbFBqVT3BZQoNEcyKaIlaNUFWzrU1QeLfkZDy5EkL_rxW4uOTGXR2m0p8v6GtUpBK_9G3OsqxYlzskJWUdbZSUCiVba8DvQhZcRMe_jnEqP4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=u57cWZbu4c21lWe1oxfyYmrmAePWSJIDCrZmqFaUOJHTgColvB8UD40lROH4m447Sw3L0Z-s3UVkFkHUIE-st5dVKGCMJrIifvoyKUlGJlsyk3A2Y7Vyfbh-SacqJcyg4qS1oYuXXlW9Id4FIHtpcsUMZR1PQUzpFq3EXM3U0e_qw10wh8aHtVmU6OMsD-5Tmk3cfqn2fxOdI-inhjyYfTSfYP8uuyRiFM5XH27aUbsfR0hUEaJctVUha1FbKcx1RjCAHxBuqNDQV-vjx0OVFE1gLb1n00dMszSi7ojiQBNr5UqI6mtXWBPMirlB5Q93_hUdXWyNl4g-xtfmQ56Ca5vY-9paGCiM321HtGTY8wphawETOfVhHrCewmrHT6JPDXc-V4qHkwplt8AgxjU9ni6TJWurVbUecTMUe-4Bspd-smxmcesA2XthaW3SGhoxUeHPAB0U45euFYzXqGOOdmuJx3Ej7R7XWOYLNhQYgbitmxyeOFRtZX2z1gzyFuXA3E6nI6gA7If4wHJwzk6DWMdvdjg0Xpx16tXB59kf4C4oaQeiYpzDP77yu4254gpbFBqVT3BZQoNEcyKaIlaNUFWzrU1QeLfkZDy5EkL_rxW4uOTGXR2m0p8v6GtUpBK_9G3OsqxYlzskJWUdbZSUCiVba8DvQhZcRMe_jnEqP4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30657" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30654">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOa1lLp21vPPri_Rz5t706UQw6XHL_bMnecqZ4oejkAHL37LhcOeyl4YyqyJrD0MKjyLTsKq7y432MDYifd21X2JFM3AyNy-cG2g2MilCxvZoZ8J40ndVa4iKCtqs_jWGJHXsVUrt2mH4F3U37cnGYQbGuK6CiM0oIDnLsCd2utmw6EnN1VmH_12QWX2xvYjC7dTaTdCH66uelJVm0236k6L_843zMYm3K09vD0hewg1QC5jCdvnYwRyE7tSrznorwIqXNWg0jBdiNP9WERUHQ2SAjGD9HBndG2Ef6L6OpnwDEACrCyAJVAafeKl-glWbGYIp1M_7sfLp9esFb8OIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30654" target="_blank">📅 10:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30653">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-WKvc6fOuqB-hIF3Kj810pWs767ba4fszCz3hyCYfx8Iy1s09AIAa12LBH80EJjnczAX4As0BYOqCPzS4dcEIi3uTNJKzq8sZc1Ujiyzm2OKdj9KLEG-0z1LduwpFSYPNH9lOT2S9Bwkn3e8MIvWDY0a-czWECaqSaZtCcIN4__NgNY6JFd_c1S_JuOv2_f4cbcb3Hiw_9y5GZqGJvYsPJxJiAzCMCltke9oqzGaS8hvEU696B1r0x6-wxuaKp2MAI2j9WxPe7FBR_JBzrhtnUAfQsQJCKVF-Wh-NaQaOuArGa3mqfsCxangF6PLSMWgpPEaMzAu-utnBP1FYXGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدار دوتیم استقلال و تراکتور در هفته هشتم لیگ‌برتر به احتمال‌زیاد به جای روز شانزده مهر ماه روز پانزده مهرماه در یادگار تبریز برگزار میشود.
🔴
سازمان لیگ این پیشنهاد رو به دو باشگاه داده تا برای بازیای‌آسیاییشون‌که20مهر برگزار میشه بیشتر فرصت استراحت…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30653" target="_blank">📅 10:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30652">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2czPChqPY3Jva5IkjRzXW4uOxGEFYYl2tE7MiqtY37FZan7o6Xvaoyzh1m0mwQvlPXeOyHNEtCdxrZ5a4GY223_lGWYXagapqvjT2d5rDqHUMVRPvJUcqNyVX_BGPc0MnHcVzQFeV75Xcs_PLNyrWDoZ03klm4UaapcE_Pzq6nJ9MjwozDe_0N-GpWMlTTuhh6hGbe5sUPfndWU1MY563b13T0UqswSI3DJ5yGyIR3KyHgeyg6JS_CDmDITHLQaJB5Q5pApp9TsOg7plccp5gprv9QLbA-ZfhDpJztgFGnRrTvkbgSC58VjEPmsSy2XQghIorxp33z0f4aiiNyK_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30652" target="_blank">📅 10:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30651">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=u5XGiyS-M2bvc8devpBBBRtm9DZnaNdTeUZABCbK_1Vulaeib6ukag67sdtymaEZUv6UWZTwe5ZQckdhv5b-USn_Lr5bdDr7IAF-Wrhf9kYk8AOBN5IF1OwbXUmaJ02Qz9uCULCigPL80kayCdx02NiPFc2ni2VjhPencKU8ud-rX7DSyVt9E1kH4P7fv2JgiL88MFvDRX0whIhWX9cY_FfznnDQiUhWLW5lqiZj1h3YBzxoTFWtSZLa1Er7vtKUCjg-lWaOkfiytNxt5gBsR6Z_nZ8QDbl1_0f0QVZ1SvKjiXxbWHu6Hi_i_L02wVAwAIAqVOfnHCj_D06XcL2ysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=u5XGiyS-M2bvc8devpBBBRtm9DZnaNdTeUZABCbK_1Vulaeib6ukag67sdtymaEZUv6UWZTwe5ZQckdhv5b-USn_Lr5bdDr7IAF-Wrhf9kYk8AOBN5IF1OwbXUmaJ02Qz9uCULCigPL80kayCdx02NiPFc2ni2VjhPencKU8ud-rX7DSyVt9E1kH4P7fv2JgiL88MFvDRX0whIhWX9cY_FfznnDQiUhWLW5lqiZj1h3YBzxoTFWtSZLa1Er7vtKUCjg-lWaOkfiytNxt5gBsR6Z_nZ8QDbl1_0f0QVZ1SvKjiXxbWHu6Hi_i_L02wVAwAIAqVOfnHCj_D06XcL2ysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه های سنگین و پیاپی امیر حسین قیاسی به امیر قلعه نویی سرمربی فعلی تیم ملی ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30651" target="_blank">📅 09:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30650">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD9rUY9V_F_JROz2vt6VxsPG5dR9ojoNOKRzz_r5RNBiGzZS1qT232MBg8KAsxLqpleimYp93a01yaQ8jf-Jeayjuoq5axSZvEBLZXWod1efghQYsMcB2JcYOo8lKUKvoMcAxDiEkH728atihOYlCzxr7rT0T9UvrgSy_p1WpW_zBOSU4FCTZyKDoEzhJhLnhT9Ps1d28EfiJvyLD4AAe1PzDtMCBfkaI2vskMcCjlG3o3wrYIHNz8ZpiSF6NONKijWbkD7GzG5iSMx_Hpd3VrYFIQnAJNV7dMhTo0q3ntbRlCByB42WfiVgnw0firCm4KbJFTJjr2ZS6meLhxyhFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ معاون‌ ورزشی باشگاه استقلال: جلال ماشاریپوف بازیکن‌قانونی استقلاله و قرارداد او اصلا فسخ‌ نشده که ماهم بخواهیم قرارداد جدیدی ببندیم. ماشاریپوف تنها به دلیل مصدومیت از لیست آبی ها خارج شده بود و در نیم فصل به لیست اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30650" target="_blank">📅 09:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30648">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2pTab5zXvBhbt36UcBNCE4Z9BvV5rGcNHKLqqZ2bQH7fhfC5q9myPqLgLxtVraXVq_NlcOUDdbReflNjtIMdJbOEvpMn6Iy_ZCbEartmkZI1-MiSy7dYvFjV5AGXlbEptHa43K66UoGvLmQJvyIOLDVp2e_tmQ1TeZ9pJGQ8YKyB7NnSZeEHxfaOgHcPJQ0oRbTMHDiv2f5byIAuhc6wH3nJovAla70bhcO-fPqeIopigH7bzXzHDdLfmwqTE-QT8DU_TkaZMNXQL8CgbmKzp4ygVOt3Tujj23XTq-49kKT2m9GBsxmoeR4dE93D4_sZ1XARKJUcL62uUd5LGSjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30648" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30647">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFGhRN8aInTiZHUoDvzyW9pAovhjtfz8TW-Do5f94ajmm2OFIJW-AxxVi_SUpBVrGwgylz-12aIjs5D-1OT7_VeccJJ0wZu_qCyEneGj2fa05jggB-1A9f_wcWjeJX0BqK7lFxp0A1Q52mUES39zriFlVQurK-L1aZ7pCSbm802QqsekXHAWXOIXvpf1tSCXYN_PNyBBEBZEyzLcuoBaDLVqdPbI5Id0BqwxjIlDYqRRg8ZDhyFy6ZSdbWZtIuj3QjIFeG0dxdAQtOn6DIxZ2A_diy_VjMjoH9_gGqoGiiOk5W5oqVQ3O8JD3el36HCYZtny7_Hpefi8BGzapu1cXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
دومین‌بردپیاپی خروس‌ها با زیدان و بردقاطعانه آتزوری در خاک ترکیه؛ برای اولین بار در 40 سال اخیر فرانسه یک مربی تونست در دو بازی اول خودش دو برد و دو کلین شیت ثبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30647" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=c22UqL7lIUpIGlcJQIPiAmyqAMHcIkdgZZXBT0Gq3ykWZRW6jXtOrVZw-ipz_XLyIBVFBqpfs2rVKYOmg2QlFS-NKpSOiRAxrMrgRxJE4y9wDZV41GXONJ1yKWBxJBull7jdYzVKjRzCq_PmutfDT9Uq1gwefNOcBL5gNzSPCocRbOORYdpHuxavxeAQw7wj1Qcc4Cg6UFWSRpCE4K2AoLbLYZ84t89lp4v84nn8MymqcqHykcYRIyYDdQsFaGitn3U_-PLQk1FbN3yh5jNF75Go-ZpmrxDwctm1yikHcLbNn01U_tNVBgA2_1GKD3RXRc9pEzi9hCgK6GqLsWjhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=c22UqL7lIUpIGlcJQIPiAmyqAMHcIkdgZZXBT0Gq3ykWZRW6jXtOrVZw-ipz_XLyIBVFBqpfs2rVKYOmg2QlFS-NKpSOiRAxrMrgRxJE4y9wDZV41GXONJ1yKWBxJBull7jdYzVKjRzCq_PmutfDT9Uq1gwefNOcBL5gNzSPCocRbOORYdpHuxavxeAQw7wj1Qcc4Cg6UFWSRpCE4K2AoLbLYZ84t89lp4v84nn8MymqcqHykcYRIyYDdQsFaGitn3U_-PLQk1FbN3yh5jNF75Go-ZpmrxDwctm1yikHcLbNn01U_tNVBgA2_1GKD3RXRc9pEzi9hCgK6GqLsWjhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#تکمیلی؛ گل‌های دو دیدار امشب ایتالیا
🆚
ترکیه و فرانسه
🆚
بلژیک در هفته دوم لیگ‌ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30646" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30645">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=PHRfuegbXywE6_pYUvYmRNsPh8aQxh2ITC5lo04SzDlqg6rNpw9YI-oBeh9Q3EngIETWtbhKigrFBG8aKZvV5uubrQtRipc5SKjAG63Jc05pqvDcw66fRokRQ7OYdeDhWbkCQBksgVlPI6xtnL1wjXnn3zDN73rPLFOsR0DcPudJaZ-qUwfuf8ybnhxq5q8SSfhAMqemUufmsAmDUjtwKRPLiRqlayZdvbfRCZuRcshQs-WJOGoAxZ2g4brbN5pM1l6a7JFEWKBD6N7U6XyvUEXPXS4MbmHO9AYnMndRmMwEWo98IbuLb1rDgZ2_2zeiVNAMEikwkabvTUFrIkpY7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=PHRfuegbXywE6_pYUvYmRNsPh8aQxh2ITC5lo04SzDlqg6rNpw9YI-oBeh9Q3EngIETWtbhKigrFBG8aKZvV5uubrQtRipc5SKjAG63Jc05pqvDcw66fRokRQ7OYdeDhWbkCQBksgVlPI6xtnL1wjXnn3zDN73rPLFOsR0DcPudJaZ-qUwfuf8ybnhxq5q8SSfhAMqemUufmsAmDUjtwKRPLiRqlayZdvbfRCZuRcshQs-WJOGoAxZ2g4brbN5pM1l6a7JFEWKBD6N7U6XyvUEXPXS4MbmHO9AYnMndRmMwEWo98IbuLb1rDgZ2_2zeiVNAMEikwkabvTUFrIkpY7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل باز هم تو برنامه‌اش از خنده منفجر شد؛ خودش خراب‌کاری کرد کم مونده بود که تبلت 300 400 میلیونی‌رو به‌چوخ‌بده خودشم خندش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30645" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbkiynt9WfJ1QknrV42m48_KC5wrRvmphDoHNBLItZ0Eql4sO8CSqH2-1-VNH9-IunFDm8e2chLgf5I9Jxz8FvQ2sToeqSpiHMZEQgi_bFKXkpbOvWGlb31Yjz6L4Ht3-DDOOw5x4xnU_stmpOJN1ZkzjNisyBlB_kIQJiThrdgQXIPdFWpQabshHrEAOjuBHUcqMXCP0Oqj237nl1Fed3x5_ekcfvLEZpe5dti1o1hfmLbTXDV0kg_3DgZRP0BHlFTGPuRURZfTcP7zT-462_Gl2N2AIEuAs5tOwrDlkKPWTdzqzhb69KAt1DCQ2D_Y942kSO9OJ5nAUAs_pC-80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ علی رضا بیرانوند در جمع بازیکنان تراکتور از جمع شجاع خلیل زاده و دانیال اسماعیلی‌ فر گفته درصورتیکه معافیت کامل بگیره درنیم‌فصل راهی باشگاه استقلال خواهد شد. این‌ درحالیه که کادر فنی استقلال فعلا علاقه‌ای به جذب دروازه بان 34 ساله…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30643" target="_blank">📅 01:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30642">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJT2hRoLuKYowRzZbgPlpZL9r_CAm4BqslqlXoH7cf_4M0fBSXi0EevQl0V8hDvDjhyIbwMygW0EijLM6w2LFgL3euI5gLsJMUyNdqcOn-jirXeFhTZEguOKKcxn758VtH9xnaIF1yXMTHLyKs7QRHBylMqYv4_tjaHb9IUoDaK7qjvVgeOooKGkRrggbMKo87w5lAMrc1s96fOLMBbEsQk38UYtuixK0p4asxkzDxcUqmC8DNBddb116K1zstZHiL3i_HlnfAspFV8yW8kIhDVgdJNeHrr8SybqvICeRJPO6yUQh8idxglPNd58bDf82swa8MsXLxeD-TxUyGOl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30642" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30641">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30641" target="_blank">📅 00:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30640">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baUCDQGbLBMe53fPjMBrwwB34XObAGvuLHl4DA-gbp3Y1RRsmPocnviIwdll0eFFMwsejnqOUd5WYyR9VgUMKpD8VB-BhfDLlzqsqVJ2yFF0GM3BxK0XDvMWVWPQGyY3mkgLVHRdnjQqZY_1al16kgY6BpdUysDqbFQiCgnA--Jtih1K18H6MXal5_1B8T6YFSJCsbtY6LB326yPKcB-QPoSEW99NyEVryzeubn2rspuBG85PP4yvX7rJaq6kdKb62xQvQ9f7WpNWfx7aehdr6L2tiYzusbWN1HjisvbLjrjbLLIDaP6XehTbYrt1BxV2I1GwoidII84wsmJi4NQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30640" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=pkfl9ZfpImLY5Fl9Wwti5z-MDM52Tl3tdHuqzcK6btuUoJD6-oCMC9gzJg8CaWP9H_s4ZODkX5ONdXhVY4wjuGCFHA5g3d16PH9isGfg0gP2F0WY6TpjqGYILB44zz0uK6nJ9Jsn9SbPPTYhicmYaVSPM3XG2X_RbHYao5mDlCixRXX_tMTAkgbu1yUUdsFlS4AFgQ_vwWuw7CWEcHUBzEklZmLtmya2JBbW1timNDDxoFhCjLJuD-imagmxcCisUXXDUWPKTaH5OKVlIUIKn34jWnbSbquPwEJquBS7UcW8Ois7WSR-07u92O4SupugrH7qQ_0rqenRyO0GCe5ltg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=pkfl9ZfpImLY5Fl9Wwti5z-MDM52Tl3tdHuqzcK6btuUoJD6-oCMC9gzJg8CaWP9H_s4ZODkX5ONdXhVY4wjuGCFHA5g3d16PH9isGfg0gP2F0WY6TpjqGYILB44zz0uK6nJ9Jsn9SbPPTYhicmYaVSPM3XG2X_RbHYao5mDlCixRXX_tMTAkgbu1yUUdsFlS4AFgQ_vwWuw7CWEcHUBzEklZmLtmya2JBbW1timNDDxoFhCjLJuD-imagmxcCisUXXDUWPKTaH5OKVlIUIKn34jWnbSbquPwEJquBS7UcW8Ois7WSR-07u92O4SupugrH7qQ_0rqenRyO0GCe5ltg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛صحبت‌های‌احساسی یاسر آسانی: بااینکه برای تیم پرسپولیس و هواداراش احترام قائل هستم امامن‌هرگز به اونجا نخواهم رفت. البته که من میدونم شما پرسپولیسی هستی آقای فردوسی پور! جلالی گفت من باپرسپولیس‌بستم توم بیا گفتم هرگز. اگه استقلال من رو نخواد از فوتبال…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30639" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwR4jPuXzudRxU-O-mtjYqvR_ISuLm2d_3DNNWz1m18qgg3jqNZuZYNSqqoXmQpoORTHxQmhjIne7qR-C6Bh9ihhMfF31KRzaIpQPHeJITRIVDhM4kK8vwHHKKWlZn4taZjT0m7ncOaDhtRlCQE-qJu-Zej_Bhl6QR7YXSEfbTfSLrEcg6vbxLrTPM_E7htyNBbFFk-ngZFWt3M5OK6YiO-sfmmtJMW7Yi8zXex8kMSgReAVIRf--eZxY5UaA-tg1XfoDcPhmvFdZ-lEfMCgaz-DFWRfUSgEoLHaajnhpv2OoCHci383-JxOjymkZMfeCG-rNuULLP0xN0GHXX-Uhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30638" target="_blank">📅 23:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30637" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیاناتوسط یاسر آسانی: باشگاه‌پرسپولیس بامدیربرنامه‌های صحبت کرده بود که به اونجا برم اما گفتم علی رغم احترامی که برای این باشگاه قائلم اما جز استقلال نمیخواهم در هیچ باشگاهی بازی کنم و در استقلال موندنی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30636" target="_blank">📅 23:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=F1hcbyyMm8zkBNQIliMQu8Gs734wWBpej-j2idIDOuAmMhVHfaCcowVN0-mFROyel_0aQE2DM5ml69butdtP3M1eKFYkTKRSRnGtjhL5ZgCkQ2JSkUsTZgMe_BZjR-011ASOyTMiWBlV2vDiti34Plj9KT73WlToaXqqV6GTvIVVrKjAPNZOpMaMvxDZ2AZXSCVRe5aoRF1T3ghFhHXw7y8ck4iIKAM0sijG7SnwV2z3mylPpOrSzjsElDjn920BEMDkEYEEJZ5vs9m729zHOYV6OdKX3L_WEIt0Tjum3cGHWyiFhoi5RI6dzWMZbu9Rg3rOz8plvEgi9YfsQWZ6gz9ejct8eheYFiURqe4vhyc6zuFt4BkFcqdU_VpiyX6EnYAQTf-zuvNI7kFrz6nf8GKMngRub5-H894o_1HByjzZEQN0VZDqXGN1Y_KFf3r8s5WI9Jb3S5tIBM6ODqiPPlZ90cXy3J6MTBdpS9J23qICvn6g9-kcIqA-HXUxfTLtm9rxMDArtKVYte9c8cyBrYbIEsEY5SsA_S8vUbV32QRX_pm2tHF3p2PIZZX5PXESoelSrgF9zAQBR9bg_jZi90GDRvrtyRb8_KpoAzgfhfauXQy7NwSYOfdxPFmpeDgDuMKk0rxCER0Ue9CKoDuwN7TLDfN3CTA65CN6Lr6CyGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=F1hcbyyMm8zkBNQIliMQu8Gs734wWBpej-j2idIDOuAmMhVHfaCcowVN0-mFROyel_0aQE2DM5ml69butdtP3M1eKFYkTKRSRnGtjhL5ZgCkQ2JSkUsTZgMe_BZjR-011ASOyTMiWBlV2vDiti34Plj9KT73WlToaXqqV6GTvIVVrKjAPNZOpMaMvxDZ2AZXSCVRe5aoRF1T3ghFhHXw7y8ck4iIKAM0sijG7SnwV2z3mylPpOrSzjsElDjn920BEMDkEYEEJZ5vs9m729zHOYV6OdKX3L_WEIt0Tjum3cGHWyiFhoi5RI6dzWMZbu9Rg3rOz8plvEgi9YfsQWZ6gz9ejct8eheYFiURqe4vhyc6zuFt4BkFcqdU_VpiyX6EnYAQTf-zuvNI7kFrz6nf8GKMngRub5-H894o_1HByjzZEQN0VZDqXGN1Y_KFf3r8s5WI9Jb3S5tIBM6ODqiPPlZ90cXy3J6MTBdpS9J23qICvn6g9-kcIqA-HXUxfTLtm9rxMDArtKVYte9c8cyBrYbIEsEY5SsA_S8vUbV32QRX_pm2tHF3p2PIZZX5PXESoelSrgF9zAQBR9bg_jZi90GDRvrtyRb8_KpoAzgfhfauXQy7NwSYOfdxPFmpeDgDuMKk0rxCER0Ue9CKoDuwN7TLDfN3CTA65CN6Lr6CyGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30635" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y015zZSTZoEsDeWB_vH0luYsiKddlezGsOzh7IIHar8GAAr7hFcOZTy2aSRXLyLx3Emz6LZdlCtJMCOMFEt9AvP9hGZno0md2eLoAr6FL0mSOmzrlzYnZ9mQ_PHbdkZ4P9fD5cStXTNhFG8tfaWnMFQhJWzGQQuJknR7i4P_DU-NSR4vOPqHy3kW-ywi8XjvuyVhnNuQC_BEm7_i-arU-lgS8mL7U2enk2Z5QXy1-UlgJy0mChH6nnTlKoTXcUljYwZwMF8bmN2WksXSXGDSex-sP8i96HGmm3SDtUTO59G_9XIMJh5l2RdCIodp_HE4LeYKUsaEVSWWo-1pQ6DmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30634" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHe62peDufQlSJJqaheeL6_D5F_Tj1Vb1feP3ofpbtX6UNs3R1a_5tNXn4WR8ExHqY6MaBPvwFPzXgZiEAwW1WBJe_8DbWpTPH4_tl2gcak9A1mmEg4hTgS3V9LAIEiMIuoLfUjJY086dKZhcmav9UMXjhI5wBfqZ1fkAfkhtX7eZ3JqCcUCP2hVkB7Swuf4_orENLNP0-uUFpuYkiWAb73Uo0fEN_J62-od_9BHmcyUYi5gi1JKba4xPvkwUjnHh_BaN3fyvugwlOEPpXdfJBew2fJt7ispIK2lgO0I3Sx0B_dR9MqY4iQUdRYmDCwN_rZ8Gok0u2NEE8T1nnd7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30633" target="_blank">📅 22:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=YMCEGefKK9gIrp5JboS6i2IGr-fMSjmQ2rrsuJq7yZWU4C22a7CoDr5Vama2m0jbP-FNFHyNdUcjDkH7C-Bw9NLQoAPOQOdFlzKVlynNoYFmmH42wmyz3DHH_6BVM33QX4oSOsZaOjp_S9Tn6zfoi-8s_ZkqJRsEJjMj3uU3ntQsl7Vew1ladzn6s2m3W8ruh2_oMCUWX-sIq9CB4sps22L9eP7O6-q8w4Quu-Ssn9LWTGeMNhkyHt7e1zId1Wq7vI8UWPAeoDqB6eGemRnJ5e23xo2SXksJOsYzDyqpvCwWpxytjekiZbw03B2EYf4Q0hN_TKNcnLp9X8XH9fyMgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=YMCEGefKK9gIrp5JboS6i2IGr-fMSjmQ2rrsuJq7yZWU4C22a7CoDr5Vama2m0jbP-FNFHyNdUcjDkH7C-Bw9NLQoAPOQOdFlzKVlynNoYFmmH42wmyz3DHH_6BVM33QX4oSOsZaOjp_S9Tn6zfoi-8s_ZkqJRsEJjMj3uU3ntQsl7Vew1ladzn6s2m3W8ruh2_oMCUWX-sIq9CB4sps22L9eP7O6-q8w4Quu-Ssn9LWTGeMNhkyHt7e1zId1Wq7vI8UWPAeoDqB6eGemRnJ5e23xo2SXksJOsYzDyqpvCwWpxytjekiZbw03B2EYf4Q0hN_TKNcnLp9X8XH9fyMgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید سردار آزمون: پاراگراف اولش رو بخونید. رفته متن رو از هوش مصنوعی گرفته دیگه فکر کنم یادش رفته قبل از انتشار ادیتش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30632" target="_blank">📅 22:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30631">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO4zMW4TeoDOj2SPDYbC82ZbqVuB9d_-jRQnkMk9FID_APNwpnLrSGn0hVBUwYtjo9C_cTpyXw6vigDZOo_bbJqwChkvEMo3hcP0ll5SDGQn0Y3T7rI7bbHW262v2ai1Qp6A4UxGk15r5n8GzXudnV6QVSoh-ZWyefsWiLXosA3YrkyLwYI0llle2F6PCunnCc0VENFUnxyJBKvwlEg6QWF6wgBxLu0iZEkl7yJ8ITrvcyfoAlPD28KmuM2TFHs-T6x0CbIzKLvP51D6D56nrFUP-XUy5Xj2MsN6KF0n8C4uHEn8_yf1U6VlthtNg6BHn6DvBlPPSg2iobxLUiEMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنی که یه زمانی در دورتموند آقایی میکرد و به یک‌باره‌سر از منچستریونایتد در آورد و کم کم افت کرد در سن 26 سالگی سر نخواستنش دعوا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30631" target="_blank">📅 21:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgNoh1zJlvTTzQAXCd8XICsg9vHXo6tx4DUEjkdXqtGglU50whEFIoqidWrpcJ9wpapmmevG15FYyDC5zDoJn89Eu3bm2Ml4oVFtWnxMnn10mzoq4CPTuNlMpeiRUcwXVTKj_w06ZGgc78rql2NmP-xDsUwrdFa4dNWMjwXFOIWgY-afmNT1xsk-QSdzOoWRU0abuOD1ZMercjXUlrhEAYom9pWqwUmoRIGL1mkhVouFqQ26m1dRXy5LA2bFLx2XRKfVdCzltYvZLc9bk5xKho0oH0At5zWlCQnbKeTF9Es2yPm0zYPuxqLTXW9zDY6a_XvftixHSsxQEfG-qUgaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رای‌دهی‌مراسم‌توپ‌طلاسال 2026 دقایقی قبل رسما به اتمام رسید و از این لحظه به بعد برنده توپ طلای 2026 مشخص شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30630" target="_blank">📅 21:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30628">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbEy8ZA-QLQFRzSL7gZU38W0_GRfaX55_0JtCZuO6ioqiIeXovo9a6-fW3lAH6JNb2SAp4j69maN1R3S0bDTeU8Gw4iuoUEAUEYJk5ipSmGbMmrp0eZ6q8A-UjJC1JbiSIY1FzFYYUEYmlF5LGNVUBl796l09VncXgqPjZPNGIWEW2eBdmugeVqig9181AFpmFB7GRYPSkTVhkLoarI9Qqlmk4wWbr6jmypXC8GezszGMBT0UM2-Qd74LCNcjPD3-v6YbAlwFTJWT6Nketakhn837MpMAvKPRQiGwUb8W5BaNKNfin2F_aNz-b7GgKzxMHsxHIbJAG5HwMjm-bYu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMMjtqnkVa0CWNjsmBl05dSJItnywlVttdMAB5tJc6aQtBXWmjQFPfu0K36n_c8rxwkKLAwZrEce5K4dARBELwrpIuGf7dmQPouxDzYSDfPH3WR-oCQw80L3m6NsHhJ1wSiK_Xl9Xy-refpioRNJjVQvb6GG1o2ngxmUKfjNVmz9X_TFM36lwMwni1MWc-PPjO64pM-ahy47oUV1Lc-GYwW_IiXE2vKlYp1haNSCVREKy-wmT4c5qigyMGnydSd-lizlh7QCZ6oxIW9vRnGoxlD2xhCZ9kRY2vq5WEQkzjVSf0XxioD3UQ8scHvgXrIdiOVgyHJFISpshat9O5IWdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30628" target="_blank">📅 21:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30627">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPAV-rTM56hLwGq_O86Pb4HPl7gWM9gUpdJGG9ZPSDTg0plQ7rh2MS7-EZDFnGvmnMsfTOevcK7VQsxpBC5Ks5Wq8dPsbHICqq_sFQU_1jT9U067IihvZ34PSHl94G9lop7jFffBIG6Do4sDStsAiUcJJ95Sv7Mkk3L75Ew3jQJXJRGbT5jN3VVuRJtwrfOT7XXqFeLq_UpqiNQBYpkcs1dXgXXHkPz-GOVR_pCvxA6ctOqza7wa90d4qrDVr8DoynuBK6J-3Eb6n0HLeS2nBcvm8gdZ_CfRe0VHIZ8IGo8-CEThbDQ0CH5NQcsesFlGzJuJ0Fm2ZLnfQljDPxjMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌نهایی‌اعضای هیات‌رئیسه فدراسیون فوتبال برای رای‌گیری‌درخصوص اعلام یا عدم اعلام قهرمانی تیم استقلال در فصل گذشته لیگ برتر از دقایقی قبل برگزار شده. تا ساعتی دیگر نتیجه مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30627" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30626">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIvfnXBBZGkGDRofHzC7ozk90qb4x1Oc5N2HyvrwcFqUSzsYQrY3lYgugUQIMn_Jz__PZMBgjJrRcSbnXkHFXsSH8EtPN6Rjae60SjSzuiLCJPM8F579vOza5A0pOjit8IbRfNQN3z57CUFXIiBemzxSaPSiZ-I6eGzSbpRSUcujWRAty1Vj2m0akszLK4xP6Bs7hFyBbuFY7yDz556_NPCcqATJ5TWlcjBrXwCwQ3_L5tJUz-05IJ_uZ3SDGz4ZUFH-_KN_AD-y0GBgltsrnL-bZMzwL00aS71k8kFjMcJfmM8KU255hkRShse2wyfRhmGAg8SXALwKsR0IH5s0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش تیم ملی ایران داخل ترانسفرمارکت به 25 میلیون یورو کاهش یافت. یه‌چندوقت دیگه تیم های اندونزی و اردن هم احتمالا از ایران بالا میزنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30626" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30625">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=dGZdxPDGMywZw5otyqtA2_5ELhOwkiFr5DaHZtNlZhxD40IXG1_nnJb5tCs-jZ3S88SaSMF3l8lw0yqSGTWZJO9bcqbWjHOact1LRsy5rQYYfal5AkOv2Lpah5QT1WHsj9pmCHW1Y_KgwxKNJ8dgoXZP3vTbP7p9Y-rvVw4cUCT2909LcJ51LLOMAFsSnhVL5SRCBPunAlSJUhQYw10KYf7KH8_n18vCbRv9SimWEGOQz6Sw1dZU9-ZL44kGSauTGaUb31Mf2x4QXOImTLNfo6pAio41uln3qBJMXApkA8EUQwuKAGwR7drhttW9_ZqH74riPzeOwb5DW2Ouvl06-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=dGZdxPDGMywZw5otyqtA2_5ELhOwkiFr5DaHZtNlZhxD40IXG1_nnJb5tCs-jZ3S88SaSMF3l8lw0yqSGTWZJO9bcqbWjHOact1LRsy5rQYYfal5AkOv2Lpah5QT1WHsj9pmCHW1Y_KgwxKNJ8dgoXZP3vTbP7p9Y-rvVw4cUCT2909LcJ51LLOMAFsSnhVL5SRCBPunAlSJUhQYw10KYf7KH8_n18vCbRv9SimWEGOQz6Sw1dZU9-ZL44kGSauTGaUb31Mf2x4QXOImTLNfo6pAio41uln3qBJMXApkA8EUQwuKAGwR7drhttW9_ZqH74riPzeOwb5DW2Ouvl06-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حرکت زیبای رونالدو برای هوادار نروژی
؛ یک‌‌ هوادار تیم ملی نروژی پیراهن تیم ملی پرتغال را برای گرفتن امضای کریستیانو رونالدو به سمت او پرتاب کرد. رونالدو هم گرم.کردن را متوقف‌کرد پیراهن را امضا کرد و دوباره به هوادار برگرداند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30625" target="_blank">📅 20:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30624">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=HwQ6LC68X0JPtZ9BEXblP-pE_UwwvfF2FOCirOTrbyw96U8Ofvz4arXlFFW1oBsQFCY-dnRvPXWL6uyIbnzsY0qiP_vCVqEYBQn6uJJN4EPkPGdBqupp0jblp447ITM-3phtzErMdEMEvv7wllVPsNZTc6qyzqsQNRpv9HA-jSwDmVUmODBQN7VGqjoiyd3AMNQUtsMl47uZZ3Mdl9UQldqOc8AqUlr6-sD-fJNq1L2HVQ5YKp4BrEfoO1mIhs0rSpEvUFuwLFSxdVl9X8pJm5ErCKItlH4-xFlOpvKThln1QtRSSvwhLn0fKgNMZYQVa7dOp5QQB4BENuwqx7rTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=HwQ6LC68X0JPtZ9BEXblP-pE_UwwvfF2FOCirOTrbyw96U8Ofvz4arXlFFW1oBsQFCY-dnRvPXWL6uyIbnzsY0qiP_vCVqEYBQn6uJJN4EPkPGdBqupp0jblp447ITM-3phtzErMdEMEvv7wllVPsNZTc6qyzqsQNRpv9HA-jSwDmVUmODBQN7VGqjoiyd3AMNQUtsMl47uZZ3Mdl9UQldqOc8AqUlr6-sD-fJNq1L2HVQ5YKp4BrEfoO1mIhs0rSpEvUFuwLFSxdVl9X8pJm5ErCKItlH4-xFlOpvKThln1QtRSSvwhLn0fKgNMZYQVa7dOp5QQB4BENuwqx7rTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30624" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30623">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aobFyzS1dQJY6WAH7ByrG9Q6XADzyUW10HiXirMiOwibwdiA-n44HqCHCUeZbkCxR-bwOQDvUrnNw83U6T5qxa2psAEYW_HTuy19Ag6Uqd_vut2SlTruoAJNGo9GqDQTF99CwmLKrt0NOt0gvipgYMIktA2juhQQToZOLfW4XL9HrmIkAumE-fAcYXgB9pGsuptRitcJUs6931o9OzhTmiio29JpGb3-gOOdaWovZgpJ18Vr8hgjlEoYsGO2HjyrsKussJ_nRF5iM8pUy4az26mn5OD209ZVWwupQgBROwwr97Sar7rLl4Jzqlg_nn6WR7B5nHvN7JV5JLLqkiFiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌آاس
:ژوزه‌مورینیو پیشنهاد سرمربیگری تیم‌ملی‌پرتغال روبخاطرپیشنهاد رئال مادرید رد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30623" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30622">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJQYpMdMQABVjssjmO-bxERE5Mr7GalksQA96ynMnd6Wkz9vKWYN3e2ubjN7xehzdQvtJx5r0gTpyUxeNsqmYMf0r9KdHTYjGwNasarMmr_aihreTPSP0WYEzAq9w0GNAWrouR1sqwU6GtziFvVSesz6lZ-bqjWNz7O6Z1xI3Xadhe02_xp0Yv8RMaTQOnG6S4lJPQkj-W7NbV7NKbC4Dw86e61n-hZ9dVBkMqDE05AFm5olE7eIXtzkqogQYhcy2RwUIGu8BWZBKblt9kmabbhcRwysLTo2zW1UCUVUWyAk3yIkPIjU-bLe61zIq1iJMM8bHp8nGO-yIcyKuo_v79zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJQYpMdMQABVjssjmO-bxERE5Mr7GalksQA96ynMnd6Wkz9vKWYN3e2ubjN7xehzdQvtJx5r0gTpyUxeNsqmYMf0r9KdHTYjGwNasarMmr_aihreTPSP0WYEzAq9w0GNAWrouR1sqwU6GtziFvVSesz6lZ-bqjWNz7O6Z1xI3Xadhe02_xp0Yv8RMaTQOnG6S4lJPQkj-W7NbV7NKbC4Dw86e61n-hZ9dVBkMqDE05AFm5olE7eIXtzkqogQYhcy2RwUIGu8BWZBKblt9kmabbhcRwysLTo2zW1UCUVUWyAk3yIkPIjU-bLe61zIq1iJMM8bHp8nGO-yIcyKuo_v79zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
ویدیویی‌بسیارجالب‌از آنالیز تیم ملی فرانسه سبک زین الدین زیدان در اولین بازی با هدایت زیزو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30622" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tt7J7gQURtytnFa6s4MXjR5J-3yhUVESNLIayx1_vSu56THptAo0rtHlQlOaRhdTbUZIklt5cQ7TbuJ0qAMU83JUvTyXKaFIPQHT3xqrF2pSVXWlY4tBrGBSKL-IYut-9zWfVsVoUocvpNgL6i0ICKwBtcn-3WUwBMOkid9L02KxVbyy59bKJo-Y22h_hViQOHkKa88EqoTCARDJZKXieQbhaoWVeKqpsk6UnCWN_qRLxD7er4vjEGgweFutSGF_a8Vm4gHvzaRhEWxHjCcszsGtLX2qvrk89BtliK9ceyJQjs7XJR6jjsGR4pZxpO1_jzDsUaU0q6WffZ94Xn6i-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fa1cgzvdlCQpQBHLXtKM3F8IjveNx2-k_D_CV63LI0cDMnWL5SW82iPLVJT5yH_vJuTYwgwtW_S9R_aoENNXjEn1j6hnLQ3aXCB8EW-dX0r2zAw8e831HS58wG7H5dZ_wxxBPw_WZ_1-kzex7eMlGJe5FMAH4Pt_7kLNhd55fr3V9V4ZGxUB5Mc1SqvmUsg4Mykvbz2CYuMboJTMYRf0HHg4Jd2u749OLlsRwbQ3lVvAaA-cPE6m2rCPmHeNwygTTBLkf7ACq_89V2Q7sYt-CA8SZcUBcGEy8tYg0zaH9kV2RCAR7JZPHuuzzqtI6KSm6CtsrjpaqR6IF6sgVZ9Dwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
جدول پخش‌زنده مسابقات ورزشی در شبکه جم اسپورت در هفته پیش رو..! این پست رو یه جایی سیو کنید که مسابقات رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30619" target="_blank">📅 19:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=PEIUMXE4lcl8hatjbpdEqME2zKMnaCIpJpkvre9iR9O3CVkk7WSivN5-ifbjWOaSVg-iDbwwfB2wAbvEoSp9ytp8TG_6akZz4u1F7jou4rzUHSSIdYWm-rgJHVf_ixW_9rtpVdiYCQKJi76YFwKVZPD-LXpasTNOIRFsUnpxsH-hjzA1HRxrJAHJGssGdlm_kF8aDKNWXM_oj8mIS2houj86WmbewKx42790tkEg7b1J6kur_rMBFwlWTQ1tcWT5SMpbjfjed7v5Hf3jHfB-k_g4RrX2X1Tghv5QgdEaa5YhlgPPW6zZy8gWKC4IpRmUJkWVcIHcC0aNDfgcLwGddw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=PEIUMXE4lcl8hatjbpdEqME2zKMnaCIpJpkvre9iR9O3CVkk7WSivN5-ifbjWOaSVg-iDbwwfB2wAbvEoSp9ytp8TG_6akZz4u1F7jou4rzUHSSIdYWm-rgJHVf_ixW_9rtpVdiYCQKJi76YFwKVZPD-LXpasTNOIRFsUnpxsH-hjzA1HRxrJAHJGssGdlm_kF8aDKNWXM_oj8mIS2houj86WmbewKx42790tkEg7b1J6kur_rMBFwlWTQ1tcWT5SMpbjfjed7v5Hf3jHfB-k_g4RrX2X1Tghv5QgdEaa5YhlgPPW6zZy8gWKC4IpRmUJkWVcIHcC0aNDfgcLwGddw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتیجه‌حضور تیم‌ملی ایران در ادوار مختلف جام ملت‌های آسیا؛ سقوط تلخ پرافتخارترین تیم آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30618" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLhlKxpRfmzG77sRlUBeL3adIHFsTq9EGkY-icQLcFcSQKiggYH9ScX2SQR9KzhMXW8l5Ihw4L-J3oZRppQ7xKIFP7KTadL6-CZJWJzAI40Qs3wlMYasTcRY0855RQIKyl0n2dfc43AAVGdnXc44_R6m1wPeNzj8y4IZj8VmrNjaKGHhblcj-roXRHsRsgUT9c2xxyZMmK-pvWw2Pg6ORsH24LM5eX8ounuBxpe8DQaIu0MK9rZf4euJ-0MZDRAkcJexSy6tqV5V4XIHNZ8zt8h7BzdvVPRWHbe8La4sbIaS-b2IuGxCTD0MLJ5QCWCw8qxKo_kDK-CUXeIZhcfuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30617" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyvNji2jOwtjoOXDH94F2k5DRk5sAnQjIwaIY_J-4TmaV2LV9_8ldYn1Ij0chGhR8ICvfNcZ8C6JaB-tuTno9kChdAQJkAS6vd3nqz_5KD8X99J8kPEDVtLIOgXgNQkAmgvOYIehfWD6zfvs_jHzvNyw3wbdcl2Z_ZIxHlQBRWDQEB5Ny9RJ3EsXCjYXdAgMwFJ1EuWCiYATp2NUKFOcPWDMJ4VACXyo9tqulV3NmkBpgD0574iE0-OnyGKl65K0T1guoviySIu3gIzzNFPHfmyKCB9VuE-RVnB_iVGRHkFHJ07MyZgsS-3z8KqT9gmtn7kxdFgFhSyE9nv4_YJxzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی
؛ ژاپن در دومین بازی دوستانه اش دو بریک ونزوئلا روبرد و اروگوئه که در بازی اول به ژاپن باخته بود چهار تا به کره جنوبی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30616" target="_blank">📅 17:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=dBQPlvu0CNUma4MWXJCQQgdYg03syiF0goIBr5RZUXPR9xYYk21lhC1TKHvy-LlnjbpBWhtm2m-vLF0dfJtNoO8fAXRANs7a_oqCztqxQ3uJE8AGPLGPCE2ODUe0ZHj4P7qczeFaQeNm8RyYgK3EVCVcqIqYl16wmroMu909oIq_JQ7ALSz-wIS0iBxk2TWecb10tqksYgOpMHqSvmYIjdNMuTW68otuGvjiLAYs6CWkqqiVjfdNNNCJUqoeS_NBM8BgF1No1k9VCWRzMyt2tWPaM8jMrwF3kkenkfZnge0eC7dcPZ1PzrOX34lSMkowYuhymhJS2iSmAhpAbEwxbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=dBQPlvu0CNUma4MWXJCQQgdYg03syiF0goIBr5RZUXPR9xYYk21lhC1TKHvy-LlnjbpBWhtm2m-vLF0dfJtNoO8fAXRANs7a_oqCztqxQ3uJE8AGPLGPCE2ODUe0ZHj4P7qczeFaQeNm8RyYgK3EVCVcqIqYl16wmroMu909oIq_JQ7ALSz-wIS0iBxk2TWecb10tqksYgOpMHqSvmYIjdNMuTW68otuGvjiLAYs6CWkqqiVjfdNNNCJUqoeS_NBM8BgF1No1k9VCWRzMyt2tWPaM8jMrwF3kkenkfZnge0eC7dcPZ1PzrOX34lSMkowYuhymhJS2iSmAhpAbEwxbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های هادی چوپان درباره از دست دادن محبوبیتش:
حس می‌کنم دارم کابوس می‌بینم. این چند وقت چیزایی دیدم که خیلی ناراحتم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30615" target="_blank">📅 16:49 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
