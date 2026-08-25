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
<img src="https://cdn4.telesco.pe/file/CNoGlY32KlQEyH1R07cQGT2ieZH3v4eL2WPNNiE6emna2bPfHvWmFDCqdj7TS7vQmdQdkrqpD516ONQOAePBl4yr3HbYVQRapflXXpMJzM85O1ZfujGbQk2wYrW4Ll-oNpcVJukhSOYYaDT7wa_MhJcwbNRcAJQmiMaVqU0MEvQTGG260z01EnKAiW9FwiZUHiEyPMI7SWHsdErtKZlVOrS7D3grZimzG6I4aXmhOjXVizTmLeesVddA_T1NBRyl5PTNp7NVAb4AGXaockfQipl8qj9mvVBu7e5iKp3DG_WLoQWNzDMl0R9c3dndIShrEpzPthlVK5myFpZji6YV4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 18:41:38</div>
<hr>

<div class="tg-post" id="msg-684248">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hs2E4wGSNA_wk8CbpEXg3G99x8W9Ubjp94Fi7yjIVBdDJjFw3x4rFUh3UuERToUGSP1CMK08N-tL18uAQorVpkW96lV13v9Z7CJMsT1R74x5LuLYyG5DLaButIPvtmpaZnbLyMhbdGAAPPbyl-LYUkJxM60siYwjlRH8paHecGAhkhdzddQag3jtMn1DzzLebeyOor7Sa7N-gHGC5rWQckZatI4ucOuLInVVL2REIbIngHGJHClR48kb4ICYs162mrC0UU3VL3k-1S5FBI9JIvjwrvdq1JZlJH0G18blBR-O2D25SHrNnCYJMuiIfnR1E-L8nwLYmf5Fm8kFCGwk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USrL69gO4I3e-e0ICBwrZsEmu-A5BGTEUKnbklaQPBkmaRHRUh9FnQMJb_9gpH15yDP6AUiynpFO5X6cmeRTsoi7nR-JBjRCaAS8mjv4Kk3w7sbL7gpQidARBoHQSqSWrr-zR6Kg4wEUvY4GQnI2Fl2yBKgoFhxVXWtQPZy2qJF5Ovnx2QkgWRllXVBhCXhFPuHNvVU5E59Y0yzDzrOTO15tHdN0mh8OaCjAE89GrhGkjrKBw7DHWJfUzh5xQhDe1VL54aVKFe6YsDurvLaHCcoJim-K_Fk2_c3l_Q_cvNBue_RxwjGvf6ZZ2r7rEOSWXJkUuGHS5eEcPR_ESG_y2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLVG6J4mRFp5tvCw54aJ-70lnZ_4GS8xThSxlLbpMojH-RCcb2NbKnhad3PqdmHC7cGgpMmBAGSDn0FrXBZkfKpep3f_H3W3XzWvo0LGCH861M4kmA5nChISGVsBYfuzr3yrQmR7zZk_tUwB7p-M9fBSv0hDYc6aZh5Dx8glqDYG18dkmpmnSe9IuYvit5HbqJ1jniZqC7ng4GAct-Mq2WDU1SFcld2dV7cYUcMkit-zkFxfzIefDxAR0-v33F-mB7xi4N88uFV6ut8OOoF3Xeymh2jjrlqmPrdOwQj4FrkFo7p9yEWX90Ntm9aoQIklmFqfaMV1puyCNI2luoW4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHRv4m4V9ygbWyW_x5sCDQf6uEPgnBxPe6rIEMfQ_37f1SVoIpfrOnrMFWdCGIkgi9xvauyOZC4P6pdQeuv6-tKWM0l2lR_CkyalMMMk6zmRHHU1iarIsjfbEKt8jEAFnFQzKJx_b_VsByCwzoeYbN0EGlD9OqgbZvERAyUpVd3QjNfwSik1kJGq8jGutIuTKpVh9W-gpP-1gQop3vGHT7BqKL9wAkxtwTZpRa1DMGMAHkvD1R8YBHXZL0W2s7xRYZBdmLGZwEK-EW_rvvD6JNALzW0dU9aFoCopqLew-bD3hpTgXUNxlw8Q-nudPztU7XPAnT9Zxh6415pa02yfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6PkBPha4_UBz4G8G8p-9pDbS7DZ-fide7iWnzRggjJofToh0napo-NVuiIVaIvL-n-s4VStwOiFtrsLQiNXaVxhaLwUic17tK8g5Kf6Q3mRQF2VJllMWQk5LcJkxkWgvhaoILryhy_bjfbpCLJNWrpRf5xefZA1sEfUGqxDyiKdaGXj6k3kqzvAXUdo5IRWyCpEQTCm12EIcY-MCaG-NvNO_br3P2-XSr663AGV2dfNJpg2UjkwC9xlT6EvmuJkY0fqiYdy5dOnWdZaUpMr369GNAykrLti4syEIvmwHuOEn3PnqkXzVyWQm1w-gktYcUSUtxEovwyqEDlXyk1iTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgTIXw2s8A2CWqBPlJrQzJx10qMYjLzH4v6AIU5aS3uYwsREumBtt6Al9CyYkJFsrd0rIf_h8714cW1sYwGpH_zr-ZFXrGAO-UFashgoB-r_kuS5hlfAY38L3Ed13j4Rng_cZ7Dtpox85iIMsrUePHoIu3yUlfABKfempemTWrIQXLYu0k-erF58pLCIyxZeQy2hAxp4e8YggoLMlbnbqFFnjcUb2oU592K1Z1Kx8Cki3_cnuDJTk34dd3TTC9PvXFKcIlknzU334lU9a2kcnbnCyECKmGVQ1xdrG0W7pvg6FoPuPOcNwHU7wGgGFnkDgHWZCrf0K-p4cuKvgnhsnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۶ مدل خمیر در کاربرد که خیلی به کار میاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/684248" target="_blank">📅 18:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684247">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZzFyLw7-Am2yzxd8ebj04aZ5yRK4Z_hyxaT3CLU_n1zD0e2amaUyH8CXX8rhuXo5ZX92-IyOcG3Qk7yhvpVPgubKQIv8kGdc-MVXR2u6fF3bAIur50nEVlYjf6vUo_DRvmQfuK3dsz963lw6-FE-qEBiBUgjm3-0vkPO4_60I2eOp-HVCzax1UWO2WzDIukmh3T10csdEvaNERwlnvGFWf0nlOiqxPtqsFvVIi8O69E6lJbl6ZyK7H9gmvIX3ytBGopl1ahySFtM8aDDLknU5Snd70tG_AE9j30Lqg7jtWqkxYiSjiBgoUST_YgoUgx9J6_1una1OrDBNbpZEcZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
♦️
عارف: تنگۀ هرمز ملک ایران و متعلق به ایران است
معاون اول رئیس‌جمهور:
🔹
نباید اجازه داد افرادی که حقوق دیگران را نمی‌شناسند یا همه چیز را با تفسیر خودشان معنا می‌کنند، درباره حقوق ملت ایران تصمیم بگیرند؛ این همان چیزی است که در فرهنگ غرب شاهد آن هستیم.
🔹
مردم از ما دفاع می‌خواهند؛ دفاع از ایران، دفاع از نظام، دفاع از ناموس، حیثیت و منزلت خود و همچنین نشان دادن اقتدار کشور. این یک راهبرد جدی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/684247" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684246">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پزشکیان: امضای توافقنامه از روی منطق و آگاهی بود نه از روی وادادگی
🔹
تصمیمی که در شورای امنیت اتخاذ شد، مبتنی بر خرد جمعی و تعامل میان سران قوا، نیروهای نظامی و سایر بخش‌ها بود. اکثریت با در نظر گرفتن اصل حکمت، عزت و مصلحت، توافقنامه را پذیرفتند.
🔹
هیچ یک از افراد وا ندادند، چرا که همه آنها توانستند جنگ را اداره کنند و در برابر قدرت قاهر اتمی جهان ایستادند. بنابراین امضای توافقنامه از روی ترس و وادادگی نبود، بلکه بر اساس منطق و آگاهی شکل گرفت، اما عده‌ای کنار گود نشسته‌اند و مطالب نادرستی را مطرح می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/684246" target="_blank">📅 18:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684245">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ترامپ: کره‌جنوبی حاضر نشد در خلع سلاح هسته‌ای ایران به ما بپیوندد.
🔹
کاخ سفید: در حال حاضر هیچ مذاکره یا گفت‌وگویی با ایران در حال انجام یا برنامه‌ریزی نیست.
🔹
پروازهای ایران و افغانستان افزایش می‌یابد.
🔹
مسیر شمال به جنوب کندوان مسدود شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/akhbarefori/684245" target="_blank">📅 18:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684244">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
واشنگتن‌پست: ایران طی دهه‌ها تحریم، شبکه‌ها و روش‌های پیچیده‌ای برای دور زدن محدودیت‌های مالی و تجاری ایجاد کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/akhbarefori/684244" target="_blank">📅 18:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684243">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot5w8-P5TPw8XOvyKH7yKVpYGeFOEJ2ECj3L-0ytmZnV3V9XrY-wcSjFaSOQW60zeAxpJp1XrynH4P5Fo0ueq5uztQjtrvGG0QKhmICu90oFGV_FhBrBkIoAI2dgJ_ujaXc8ZKT5F7cj1ylQBoO4aZMUXWF6pUr8DSn8sNOBQqRqKFcNhIub6S8K6GClsLWnE-dHMb1Jlupw7HS5vdSu2iJCW_VdZY5GY1HdhIA3jKLD9Q2uxrVZSI1XS6Dh0ack6Gne5hZQvi5edLsfV73Y9EG4f4llZbmVNlr6zASivb_TXMyijvMvBFSayNx3eTw9d4Xj_zUEjBx5Pb3uh-VHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانگین ناوگان مسافربری هوایی جهان
🔸
بر اساس جدیدترین آمارهای جهانی، میانگین سنی ناوگان مسافربری هوایی ایران به ۲۹.۳ سال رسیده است که فاصله‌ای دوبرابری با میانگین جهانی ۱۴.۸ سال دارد.
🔸
کشورهایی مانند کویت با ۸.۸ سال، هند و عربستان با ۱۰ سال و قطر با ۱۰.۲ سال جوان‌ترین ناوگان مسافربری هوایی جهان را دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/684243" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684242">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ترامپ مدعی مین زدایی کامل تنگه هرمز شد
ترامپ:
🔹
نیروی دریایی ایالات متحده به من اطلاع داده است که تمام مین‌ها از آب‌های بین‌المللی تنگه هرمز برداشته و/یا منفجر شده‌اند.
🔹
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدیدی کار بگذارد، بلافاصله و به صورت سیستماتیک منهدم خواهد شد.
🔹
از طریق نیروی فضایی، ما هر وجب از تنگه را زیر نظر داریم، همانطور که کوه پیکاکس و سه سایت هسته‌ای دیگر که قبلا منهدم شده‌اند را نیز زیر نظر داریم.
🔹
سیاست عدم تحمل در مورد کار گذاشتن مین با قدرت کامل در حال اجراست.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/akhbarefori/684242" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684241">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBW0YVREZHxOVtn-dMN1bSsC53cIvMyOTEzX_FcJGWN5kS7NScJuSmtCEnJv1kRB5g481KwXOoCWojZPAS8OBn4fJdR8Yl6DEh7U7w9GYNVyW7UvgAwBNnScLUKWYBbfbpO7e-Xfu3M4aKn3bUqtyj3rmkD1X4BVT_A-ocKLfMBSBSEk2SDSuqV3hj8KXDYkJEFlN3DOA0PHB2SP4Jk7R_3Cps9Vd1RpmyptcNx8EFNfJR-27EBoSNX0RyWjoydgPrjt2OGZoWYVNU0infwgWfybQYJo-ZEfgoRTMnIrBroXFDGB4U2drIs6USIWNpBcKuiaZbIo_zrevCfKRhdY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشتر افراد اعداد کسر و ممیز در انگلیسی رو اشتباه می‌خونن، بیاین خیلی راحت یاد بگیریم #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/684241" target="_blank">📅 18:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684240">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52ecbb56d.mp4?token=lNgP00oVY9x1QFGpHwDUjGQaWUFdiogRg_UguYiJNUW16BlpcmTWnSSbQp5CIEqLRFg1_brgy3YRW_Ihzy8ChBzxxFU3kXnGWxTFdME5PeR_7tlYRGJLXUgq-qA_S9Fox3XdK_p4LvvFFRxGjyRKgGqRhR8R2Nq4mslFu9OLi7N_wDNHvLVBq5IjFyJFIGj0F-VcpBwipSBCfuzMvnxP7sW4OZ04N1ipZ96I6SU7k3mgGlvRtThqRNdG7SnltHZjfp1ZOGCpKfLYFnloF5yzfGldZQ6XeK_X8wmsGuwM8_YrU6mH_b2ieK6iMOX47QlWtLOiutDtePAHO5N7W_2iug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52ecbb56d.mp4?token=lNgP00oVY9x1QFGpHwDUjGQaWUFdiogRg_UguYiJNUW16BlpcmTWnSSbQp5CIEqLRFg1_brgy3YRW_Ihzy8ChBzxxFU3kXnGWxTFdME5PeR_7tlYRGJLXUgq-qA_S9Fox3XdK_p4LvvFFRxGjyRKgGqRhR8R2Nq4mslFu9OLi7N_wDNHvLVBq5IjFyJFIGj0F-VcpBwipSBCfuzMvnxP7sW4OZ04N1ipZ96I6SU7k3mgGlvRtThqRNdG7SnltHZjfp1ZOGCpKfLYFnloF5yzfGldZQ6XeK_X8wmsGuwM8_YrU6mH_b2ieK6iMOX47QlWtLOiutDtePAHO5N7W_2iug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقدام تحریک‌آمیز وزیر افراطی صهیونیستی در مقر آنروا: «حالا من جای مدیر نشسته‌ام!»
🔹
ایتمار بن‌گویر، وزیر افراطی امنیت داخلی رژیم صهیونیستی، با یورش به آموزشگاه وابسته به سازمان امدادرسانی آنروا در اردوگاه قلندیا واقع در شمال قدس اشغالی، علیه این نهاد بین‌المللی دست به لفاظی و تحریک زد.
🔹
بن‌گویر حین ورود به دفتر مدیریت این مجموعه با لحنی تحریک‌آمیز گفت اینجا پیش‌تر مدیر آژانس آنروا می‌نشست و حالا من جای او نشسته‌ام.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/684240" target="_blank">📅 17:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684239">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نیروی زمینی سپاه: ‌اجازه تحرک زمینی به دشمن ‌نمی‌دهیم
فرمانده قرارگاه حمزه سیدالشهدا(ع) نیروی زمینی سپاه:
🔹
دشمن در جنگ تحمیلی سوم تلاش کرد با ایجاد شکاف و نفوذ در میان مردم، شرایط را به سود خود تغییر دهد.
🔹
ایجاد ناامنی، کشاندن مردم به خیابان‌ها، نارضایتی و فراهم کردن زمینه نفوذ از چند جبهه، از جمله اهداف دشمن در این تحرکات بود.
🔹
دشمن همچنین تلاش کرد با ایجاد اختلاف میان اقوام و مذاهب، از جمله میان شیعه و سنی و کرد و ترک، انسجام اجتماعی را هدف قرار دهد‌.
🔹
آذربایجان‌غربی و کردستان از جمله مناطقی بودند که دشمن روی آنها حساب ویژه‌ای باز کرده بود و تصور می‌کرد ‌می‌تواند از محور شمال‌غرب تهاجم خود را علیه ‌ایران آغاز کند.
🔹
ارتش، سپاه، بسیج، فراجا، مرزبانی و نیروهای امنیتی با هوشیاری و آمادگی کامل در میدان حضور داشتند و اجازه نفوذ و تحرک زمینی دشمن را ندادند.
🔹
نیروهای مسلح با جدیت و تمام توان آماده دفاع از کشورند و با آمادگی کامل در میدان حضور دارند تا اجازه هیچ‌گونه تحرک و تعرضی را به دشمن ندهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/684239" target="_blank">📅 17:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684238">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d98341d4a.mp4?token=mfdPd5PWL4tJodqukdNgC7cyjmwxWIe4-Fl372W8WoGbMTEW1RJW30lrPdr3nUUGIRZKaTmxPV7Paw5SzV83kYcmKGeoRwznwXhx3GGr3WSI4KRPdS-14trkyf4fczBOAN3Lz0MKuEAibgEjh6S-lUiZPKzKDkMX48Uq4MWURBvYCQLFXareQ6cI-AMulHz8BKVrp5uUMD_X63OZxb2O8ueEsnf2lDbWmNM4jRbQ-L6uVcl3wh4Yc3i1zY7ummBpGmf-KwHDrO3lcV3qTW1WyBih19aisBQI-wM2on4hDc42pvv15KX2T0o5oVwawOFrjIE1Q62CIhqtb1qNSN_hMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d98341d4a.mp4?token=mfdPd5PWL4tJodqukdNgC7cyjmwxWIe4-Fl372W8WoGbMTEW1RJW30lrPdr3nUUGIRZKaTmxPV7Paw5SzV83kYcmKGeoRwznwXhx3GGr3WSI4KRPdS-14trkyf4fczBOAN3Lz0MKuEAibgEjh6S-lUiZPKzKDkMX48Uq4MWURBvYCQLFXareQ6cI-AMulHz8BKVrp5uUMD_X63OZxb2O8ueEsnf2lDbWmNM4jRbQ-L6uVcl3wh4Yc3i1zY7ummBpGmf-KwHDrO3lcV3qTW1WyBih19aisBQI-wM2on4hDc42pvv15KX2T0o5oVwawOFrjIE1Q62CIhqtb1qNSN_hMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طول یک روز در هر سیاره چقدر است؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/684238" target="_blank">📅 17:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684237">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6031ce11b7.mp4?token=EgtLuRCPZpAzzfxsVizW1u0xTnJ1K8eTnN5g1Aa3Y1uvFEEjliEmwDz7zFI9VWme4VfZzD2p1R_7jzI2YEV7fiCC1AoTnRAWEWEZsjXJ97nIdgMavN2AU3z0nw9TNSoTbfRqFuJJqhmjs6xP2NhnBfdfaHLdhCOg64nFofCVVlvbzOUpJwYSWvVgZd6TI8NcqJFVGLRpH7MFXhyP06OsCal0jLJ0x0Blg7-JMNHPdKJJYMkaz9agA5Td3EfCU41aOtivIVNwx7S_0jGRM8yJYglgtjO-NPvUFWHPjV8BCtHeotfAIxUNx7EMaXykmBF9HS75jFavr1ERWvDp9gmPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6031ce11b7.mp4?token=EgtLuRCPZpAzzfxsVizW1u0xTnJ1K8eTnN5g1Aa3Y1uvFEEjliEmwDz7zFI9VWme4VfZzD2p1R_7jzI2YEV7fiCC1AoTnRAWEWEZsjXJ97nIdgMavN2AU3z0nw9TNSoTbfRqFuJJqhmjs6xP2NhnBfdfaHLdhCOg64nFofCVVlvbzOUpJwYSWvVgZd6TI8NcqJFVGLRpH7MFXhyP06OsCal0jLJ0x0Blg7-JMNHPdKJJYMkaz9agA5Td3EfCU41aOtivIVNwx7S_0jGRM8yJYglgtjO-NPvUFWHPjV8BCtHeotfAIxUNx7EMaXykmBF9HS75jFavr1ERWvDp9gmPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تندباد شدید، تریلی ۱۸ چرخ را در لوئیزیانا واژگون کرد
🔹
وزش بادهای سهمگین در ایالت لوئیزیانای آمریکا، منجر به واژگونی یک دستگاه کامیون ۱۸ چرخ در یکی از بزرگراه‌های این ایالت شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/684237" target="_blank">📅 17:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684236">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
نیکزاد: قیمت بنزین افزایش نمی‌یابد
نایب رئیس مجلس:
🔹
مقرر شد سهمیه ۶۰ لیتر با نرخ ۱۵۰۰ تومان محفوظ بماند، سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا کند و سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان نیز به ۱۵ لیتر برسد.
🔹
نباید برخی افراد بدون هماهنگی، نرخ‌های بنزین ۷۰، ۸۰ یا ۸۵ هزار تومان را مطرح کنند
🔹
نباید با اعلام نرخ‌های جدید با اعصاب مردم بازی کرد/ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/684236" target="_blank">📅 17:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684235">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
رهبر انصارالله یمن: پیروزی بزرگ ایران نتیجه استقامت در برابر تجاوزات آمریکایی اسرائیلی است
‌
رهبر انصارالله:
🔹
از هیچ تلاشی برای پشتیبانی از مردم فلسطین و مبارزانش دریغ نمی‌کنیم تا وعدهٔ حتمی الهی برای نابودی رژیم صهیونیستی محقق شود
🔹
تأکید می‌کنیم که در کنار مردم مسلمان ایران هستیم و به تقویت اصل «همگرایی جبهه‌ها» و همکاری میان محور مقاومت ادامه می‌دهیم.
🔹
عربستان فرودگاه‌های ما را بر روی مردم‌مان بسته اما فضای مکه و مدینه را برروی صهیونیست‌ها باز کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/684235" target="_blank">📅 17:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684234">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اختلال گسترده در شبکه‌های تلفن همراه در اراضی اشغالی
🔹
گزارش‌های رسیده حاکی از بروز نقص فنی گسترده در زیرساخت‌های مخابراتی رژیم صهیونیستی و قطع ارتباط بسیاری از مشترکان تلفن همراه است.
🔹
کاربران در مناطق مختلف اراضی اشغالی از ناتوانی در برقراری تماس‌های خروجی و دریافت تماس‌های ورودی خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/684234" target="_blank">📅 16:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684233">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رهبر انصارالله یمن: باید از تمامی اشکال وابستگی به صهیونیسم خلاص شویم.
🔹
قطر: تحریم‌های آمریکا علیه ایران یک‌جانبه است.
🔹
شمار کشته‌های زلزله ونزوئلا از ۶۵۰۰ نفر گذشت.
🔹
وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/684233" target="_blank">📅 16:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684232">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تسنیم: مواضع و شروط ایران درباره تنگه هرمز به طور شفاف به واسطه پاکستانی اعلام شد
یک منبع نزدیک به تیم مذاکره‌کننده ایرانی:
🔹
برخلاف آنچه بعضی رسانه‌ها گفته‌اند عاصم منیر، فرمانده ارتش پاکستان که روز گذشته به ایران سفر کرده بود حامل پیام تهدید یا پیام مشابه از ناحیه آمریکا نبود
بلکه به دنبال باز کردن فضای مذاکرات بود و به دنبال این بود که شروط و مواضع ایران را به طرف آمریکایی منتقل کند.
🔹
در دیدارهای صورت گرفته با آقای منیر، مواضع ایران به صورت شفاف به طرف پاکستانی اعلام شد.
🔹
بازگشت آمریکا به تفاهمنامه اسلام آباد و اجرای مفاد آن که شامل بند ۵ یعنی ترتیبات ایرانی بر تنگه هرمز می‌شود، جزو شروط ایران است و این موضوع به واسطه پاکستانی اعلام شد و طرف پاکستانی به دنبال انتقال آنها به طرف آمریکایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/684232" target="_blank">📅 16:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684231">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
دستگیری ۸۴ متخلف و کلاهبردار کنکور سراسری
جانشین رئیس پلیس فتا فراجا:
🔹
۸۴ نفر از متخلفان و کلاهبرداران مرتبط با کنکور شناسایی و دستگیر شدند و همچنین در جریان برگزاری کنکور ۲ نفر که پس از تصویربرداری از سؤالات، قصد انتشار آن در فضای مجازی را داشتند، حین ارتکاب تخلف شناسایی و دستگیر شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/684231" target="_blank">📅 16:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684230">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682ca1fe88.mp4?token=ZzW5JVrMtURj2DAP0v8lanWOGdwuyc_zvCagAdwJp2cTshox3mXSE20crWXeQf8GsrxGIq-dzdpHlCbbzJxdthcohR4rdnn3jYL7mOyJtZHViTGaBWq5s-Hh--nfJhYgmsN3ABZC-epx3VwRnzvX7TTYOo78bNVstE1XryfNuDftMY2rTS-NBNfsuCX8etyxFx4erXCLC6Ajk32ga914Vd_tj-WQcrot-UgSh244BXQs-rhYlns6va4sxOC5TZuGvGdx38T03jdwDqFrLym6Npo8jSL2xxiL-m2UVpBZPmnCMVoA8UkSYjtOuPojk-goI-4PEmF_6QNxvQ9e3TqSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682ca1fe88.mp4?token=ZzW5JVrMtURj2DAP0v8lanWOGdwuyc_zvCagAdwJp2cTshox3mXSE20crWXeQf8GsrxGIq-dzdpHlCbbzJxdthcohR4rdnn3jYL7mOyJtZHViTGaBWq5s-Hh--nfJhYgmsN3ABZC-epx3VwRnzvX7TTYOo78bNVstE1XryfNuDftMY2rTS-NBNfsuCX8etyxFx4erXCLC6Ajk32ga914Vd_tj-WQcrot-UgSh244BXQs-rhYlns6va4sxOC5TZuGvGdx38T03jdwDqFrLym6Npo8jSL2xxiL-m2UVpBZPmnCMVoA8UkSYjtOuPojk-goI-4PEmF_6QNxvQ9e3TqSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
از هزینه‌های زندگی تا نگرانی از آینده؛ بازتاب تجربه‌ها و روایت‌های شنیدنی شما از موانع ازدواج.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/684230" target="_blank">📅 16:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684229">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-b2TcP-8KTeHOvGh2Jve6ObLw0Xj26EZmwRNZtsH9qjWmg3gzManh3FC6Ri2YIpvFtmennR7a7o0k8FYBpzlAHD5oj1DgQAbytEhhtBTMgT51WrwAlyfJz9xSFn1wu0jjZqzoMmgCXX05sO1GOgUj_oSkFCyQ04sZC7h4F7JWTO-VjtQ_da73pH0KyzZWHmLJPlFit2W33C-SrgeiLXUqHg_mkGujxOZXprf0SLVXTRe8hZjytFFgv2LDnVoh8wHUl0QC6riLoSRUhJlmyRBNdz3RtYDm8v6shOl3aWQwMpLl2FaB-UBj1GZcSuYbQLUEq3ZcSnYe-vVBT9X43TeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استیو هانکه: آمریکا کنترل تنگه هرمز را در دست ندارد
استیو هانکه، اقتصاددان آمریکایی:
🔹
سال گذشته، ۷۴ نفتکش در ۲۲ آگوست از تنگه هرمز عبور کردند. امسال، ۵ نفتکش در ۲۲ آگوست از تنگه هرمز عبور کردند. ترامپ دارد مردم را فریب می‌دهد و حرف‌های بی‌اساس می‌زند. آمریکا تنگه را کنترل نمی‌کند. ایران کنترل می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/684229" target="_blank">📅 16:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684228">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bcf58e60a0.mp4?token=CzkgrzhUAUGO0MbCKRr-qe7NNwwL19YSmOiS4gjYy1RjMN_wOEPDR28FkbumHW7O1B8C5unfvXCP_mObbRR_w3pE1bhQO1RpJ9q_H1R-yfwVceaHt0EUCHcFLZqN1ewW1cN5Hdqe2N-zh7tjCEOhyh5IcGMDqFDPnp3MrH9sZ7A8ijPQQoM4AJK-C5xcmwbaEuY25-EkFWsPpGyELWMSK33DLmRIIkg94C20juB9W84MjOZHrbLIOr0vbXmNo3JuyfxCL-0xffynFn7ega_HUCmSA_Ay-Cr1anrl9_6nMW84o3dWd-dPPa4a8ye45_UHcSnw0pbxFywT6GXnz0JSqmD_FK9uZ65fxS6_VKrq7jij71yMiLPLft6uIDvykjK40eOKHYojMs5sWFaAbPR3idq8g2NnLkp6Q1XsWzXskD78z8uwVaqnmbGm_6MHW0_w8aaN3itwEH-_HkFa-ceqElcqlchUexFtiiEOYMdhdM5LDaq8OmW7fFJPY-nGx6C6azJID8AOlqFb3-KXHUS0l3LKTV0EUhJSFizHqXm0s9e22R_Gi4foq4Vu36jcEPCgV7fa1-HekN2-uNubMmoE1G6b1HcxbW4FICWhPcFd0vyMopWK4VXBThm677W7UNgGL-axbowRXmDBJaSA3_7JMV7LBJSFq8GT7fEKkvbgWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bcf58e60a0.mp4?token=CzkgrzhUAUGO0MbCKRr-qe7NNwwL19YSmOiS4gjYy1RjMN_wOEPDR28FkbumHW7O1B8C5unfvXCP_mObbRR_w3pE1bhQO1RpJ9q_H1R-yfwVceaHt0EUCHcFLZqN1ewW1cN5Hdqe2N-zh7tjCEOhyh5IcGMDqFDPnp3MrH9sZ7A8ijPQQoM4AJK-C5xcmwbaEuY25-EkFWsPpGyELWMSK33DLmRIIkg94C20juB9W84MjOZHrbLIOr0vbXmNo3JuyfxCL-0xffynFn7ega_HUCmSA_Ay-Cr1anrl9_6nMW84o3dWd-dPPa4a8ye45_UHcSnw0pbxFywT6GXnz0JSqmD_FK9uZ65fxS6_VKrq7jij71yMiLPLft6uIDvykjK40eOKHYojMs5sWFaAbPR3idq8g2NnLkp6Q1XsWzXskD78z8uwVaqnmbGm_6MHW0_w8aaN3itwEH-_HkFa-ceqElcqlchUexFtiiEOYMdhdM5LDaq8OmW7fFJPY-nGx6C6azJID8AOlqFb3-KXHUS0l3LKTV0EUhJSFizHqXm0s9e22R_Gi4foq4Vu36jcEPCgV7fa1-HekN2-uNubMmoE1G6b1HcxbW4FICWhPcFd0vyMopWK4VXBThm677W7UNgGL-axbowRXmDBJaSA3_7JMV7LBJSFq8GT7fEKkvbgWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکار بزرگ در پایتخت/ گزارش خبرفوری از سرنوشت تلخ گردانندگان بازار سیاه اموال مسروقه
🔹
امروز در مرکز پلیس آگاهی تهران، پرده از نقابِ یک شبکه بزرگ از سارقان و خریدارانِ اموالِ مسروقه کنار رفت.
🔹
پلیس آگاهی با یک عملیاتِ برق‌آسا، زنجیره‌ای از جنایتکارانی را که با کالاهای مسروقه، آرامشِ خانه‌ها را از بین می‌بردند، به بند کشید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/684228" target="_blank">📅 16:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684226">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f2484b4d.mp4?token=CoMVnqhqMr_bhQNqBoGVTNZdkscwCS9c1XK6Gqea2Ld7BhkDTRw8uKqrPWdXBbKis1fgWyoldyirF9H9mrqipm5OIz4aNpBkpWY4nhzA9Ivw4MgFIgzTN44TpSuSJScikehCwtHpy5irtHlgGVVzZrJUVeh_Y8-EbjIB09CM013i8P7a5dQnxg0m1KK-PGPbbS5LD8fa21S-Vbvrv7kEqZlixbYM6bEyABHvCAqkRlXIeU8-sdHiYk2emv0jJQnblMIc41H5ZevUi1XIQoJi3jjRCVCSH13xw2Fu-5hGgIlK9HFhkm1JRFlFZUpNSu91jjvP60k2u66tk_IwR0RuCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f2484b4d.mp4?token=CoMVnqhqMr_bhQNqBoGVTNZdkscwCS9c1XK6Gqea2Ld7BhkDTRw8uKqrPWdXBbKis1fgWyoldyirF9H9mrqipm5OIz4aNpBkpWY4nhzA9Ivw4MgFIgzTN44TpSuSJScikehCwtHpy5irtHlgGVVzZrJUVeh_Y8-EbjIB09CM013i8P7a5dQnxg0m1KK-PGPbbS5LD8fa21S-Vbvrv7kEqZlixbYM6bEyABHvCAqkRlXIeU8-sdHiYk2emv0jJQnblMIc41H5ZevUi1XIQoJi3jjRCVCSH13xw2Fu-5hGgIlK9HFhkm1JRFlFZUpNSu91jjvP60k2u66tk_IwR0RuCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن باشکوه یمنی‌ها به مناسبت میلاد پیامبر اسلام (ص)
🔹
میدان السبعین صنعاء امروز شاهد سیل جمعیت به مناسبت میلاد پیامبر اکرم اسلام (ص)-به روایت اهل سنت- بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/684226" target="_blank">📅 16:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684225">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ایندیپندنت: پدر ملوان ناو هواپیمابر آمریکا در بازداشت دولت ترامپ
🔹
در حالی که جاشوا آویلس، ملوان ناو هواپیمابر آبراهام لینکلن، بیش از ۹ ماه در خاورمیانه برای ارتش آمریکا خدمت می‌کند، پدر نیکاراگوئه‌ای‌اش در فلوریدا توسط گشت مرزی بازداشت و روانه بازداشتگاه…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/684225" target="_blank">📅 16:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684224">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آماده‌باش سرویس مخفی آمریکا برای حفاظت از پسر ترامپ
ادعای سی‌ان‌ان:
🔹
پس از پخش ویدئویی از تلویزیون ایران با عنوان «بارون ترامپ را کجا خواهیم کشت؟»، سرویس مخفی در حالت آماده‌باش کامل قرار گرفت.
🔹
این ویدئو حاوی ادعاهایی درباره نظارت بر دانشگاه بارون ترامپ، وسایل نقلیه همراهان او و مکان‌های استقرار پرسنل امنیتی مسئول حفاظت از او است.
🔹
سخنگوی سرویس مخفی به سی‌ان‌ان گفت: «ما از این ویدئو مطلع هستیم و در حال بررسی محتوای آن هستیم.»/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/684224" target="_blank">📅 16:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684223">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd86e0708b.mp4?token=cR0nzUKPrdsIxOpRqOEfggE5wbROKWxdyReYhmnRb5noZyRHa-IFsGjKB9wqF7WJDIoLJOs-Er6zL0O0ULcwN4vupp1cX7CabqJ2fPST3c7Zw6OiQ6XU-vKDxTQpUG98-pj8GDI_0fbXjDABkcBf7AON7V3kY4DO3Vb77678RmFff6QdmUc2aLeh1LHlDgzIYSsZ7TXQbKp9nDJS_FhhVtK_83My0_Ui01zvCNPrejZ9PAtY2cy76A6ZltZljnCQhnSd-sBt9on5qBRQdWxzR9q6X2yRNQmSC_SHjNKciKphwMtfFB4zQXk9MoB60G_ZoPuOhox9MwvmQW4U4VRwc4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd86e0708b.mp4?token=cR0nzUKPrdsIxOpRqOEfggE5wbROKWxdyReYhmnRb5noZyRHa-IFsGjKB9wqF7WJDIoLJOs-Er6zL0O0ULcwN4vupp1cX7CabqJ2fPST3c7Zw6OiQ6XU-vKDxTQpUG98-pj8GDI_0fbXjDABkcBf7AON7V3kY4DO3Vb77678RmFff6QdmUc2aLeh1LHlDgzIYSsZ7TXQbKp9nDJS_FhhVtK_83My0_Ui01zvCNPrejZ9PAtY2cy76A6ZltZljnCQhnSd-sBt9on5qBRQdWxzR9q6X2yRNQmSC_SHjNKciKphwMtfFB4zQXk9MoB60G_ZoPuOhox9MwvmQW4U4VRwc4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سواد مالی و مدیریت پول مادران در خانواده از چیزی که فکرشم می‌کنید مهم‌تره
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/684223" target="_blank">📅 16:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684222">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سی‌ان‌ان: فشار ترامپ همزمان علیه ایران و کانادا به بن‌بست خورده است
استفان کولینسون، تحلیلگر سی‌ان‌ان:
🔹
ایران پس از شش ماه جنگ همچنان مقاومت کرده و کانادا نیز در برابر فشارهای اقتصادی واشنگتن ایستاده است.
🔹
به گفته او، مشکل ترامپ این است که فشار آمریکا می‌تواند همان‌قدر که به طرف مقابل آسیب می‌زند، برای خود واشنگتن نیز هزینه ایجاد کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/684222" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684220">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnrDbjQTdtd3dxRzZ8q8LuEMa2sjAHKw6R56MEz5uVgH9ZGvVafQUAbz663VZaVr9jooI0YCunvEOkVn3mBSCTf171bA1tTOFEPF8elqPvI50MgI8DIm4KFC3j04I9wQhgkvJuVZziw8Bu1N8_yHuFRb6g7ETBmpLPRkgvlQzfTsU9Pru4__psx9TAf9Qx9-SIB-hqKozEqs6jNte_8ZCfTnm4NgZ0sXbeJqNJagRikBjcELU_wHpXOQKhRayyd1dftbWOx9yhWcjqDD9pu-XGRdCEykQ11I4TLDgw_ZAOQyAIryaFTWFRTrsDcSH611OUgr7eCd-35QpyhhV9_C_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ کاری که ممکنه باتری گوشیت رو نابود کنه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/684220" target="_blank">📅 15:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684219">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5w6WHICnO3ZIdSA0kKPcdh7-SFHPR9PXQ8qnKjNRMPc368CLL5hvzR-gsHSbmEoNB8cezl3P4LT7x0NpWjC9G2G_eFDjTnb_kUoBcCU24CYBcf2gsrRmYoHWgkjPogzWpgeilZcvKW6FK1lXIkNWxHcyuH6jmPtwwTKYuE8reJqt6gsnSp3ySBRjSe2cmaDJZ6ee33fsJglk6HTPIzqimJQ41U_Yc2WV5bsK3PTnBziC7zoXAkSljaM7OXb0_W2q-iY7okavXuCCQcQ8e8_P1llbQFrGxUx8u-TNP9fjL3rXkzhnLY64qVzj0MWzZRPBBxtAprg9KA2_IG6iJ5QCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگ‌ترین عرضه تویوتا توسط هماتلکام در ۴۸ ساعت به پایان رسید
🔹
عرضه ۷ مدل از خودروهای تویوتا توسط هماتلکام با استقبال گسترده بازار همراه شد و در کمتر از ۴۸ ساعت به پایان رسید. این خودروها در سه کلاس سدان، کراس‌اوور و SUV و در سطوح قیمتی مختلف عرضه شدند.
🔹
در جریان این عرضه، بیش از ۴ میلیون بازدید از محتواهای مرتبط و صفحات فروش ثبت شد و بیش از ۲۳۰۰ تماس با کال‌سنتر هماتلکام انجام گرفت. همچنین اختلال کوتاه‌مدت سایت در زمان اوج استقبال، در سریع‌ترین زمان برطرف و برای کاربران اطلاع‌رسانی شد.
🔹
هیوا میرزایی، معاون بازاریابی و روابط عمومی هماتلکام، این استقبال را نشانه افزایش تقاضا برای خودروهای تویوتا دانست و از توسعه سبد محصولات و اضافه‌شدن برندهای جدید خبر داد. هماتلکام همچنین تأکید کرده عرضه خودروها تنها در صورت موجود بودن خودرو در ایران انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/684219" target="_blank">📅 15:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684218">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jviRSZaR3VmgeluuCiYS4zb_T0N5gqAzvCbQV2rCkK9K8-yxS_OV78LQQkYpptV-O0jPPHKcAiJy2vgL5JcD5P_RXYvk1lcyoVkwLEUHElZh7HkKbRtMW3CQ4KXmzPFiP0V1EgrXTaqX9uWMlsl6MY5N2T-cKCDgMqhIUW2jGIBwedMqbt1K79A-yNowWv2hcxOHBWNGSwmDR8K913lbsCJfmNZSuFRa0JFud0v5LA2kMHmlmlo8_POggRw26T5sYUmp5CAW3xZPmQ4962S4K867P-qV65ODuHqS05rv7t4BPRVS0S6E_4X9b75m3U6ZtoaF0zeWC8ta_AL8Q0JCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت کاهشی شد و به ۸۹ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/684218" target="_blank">📅 15:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684217">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قطر: تلاش‌های ما برای بازگشت ایران و آمریکا به مذاکرات، ادامه دارد.
🔹
عراقچی با همتای عمانی خود در تهران دیدار و گفتگو کرد.
🔹
وزیر امور خارجه سابق آمریکا: نتانیاهو نه فقط در آمریکا، بلکه در سراسر جهان به اسرائیل آسیب زده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/684217" target="_blank">📅 15:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684216">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e9fc883c9.mp4?token=hInm5-yeHjEpKeW2VYhcZSBFCU60KSxIlKfJLHsTLtudGitbkBlyQp5BD1FNiKvrRQEhN6H2BJrtO6cqn3y_QpoZDfKMwMO8RvsbRTkLFiIlwwj1DrSbkc7cs4T4Ic7o0HvxwcbrtAU3HsyncRypBZWfzeo8ysvyWPuIG2fEc3FG5CNgueVfITg4ldRAC6h5BZbbtNCiPtZzPmkj_Xax1SvEKpR8-9VGDSexco2T711dxjvYanrVdmfzy7ubWfZ1mC2E6tFs0oFhehNPZEWBm4ssHS4qDISjNpjbGzbForf6L53YTuT3-Oqve5W3ot4sqMZ3bQGRZwXZvNZkRSSvyAcLpJTeB4I7YC3J4vyDeoxrkxIoydHWCyck5qixNtG1-20TBseKLk28S-DgC86UEooIOuFto-aUXaNTLXocGFnMa-uAciXTcLilu2VGVSuJ06CtCybaHz34SNlSCcwMe9dj0Nv4hsTXrdXTjzN-GdLbFFv4r0LtBRF0kMOlU1X55CLGOVpuyGxRwSN35M91qGdGZc_4DmlDkM9ZLCp4UzKn4XhNJZMsnVwFw1f3fBwY_-Bq2OC8Plqb_2VQF_GzHXcCzcjbIMwQlpZLHRNGfUZAZyLGAHjWaYt5LYajdLv1JxMMfw8j0fd_faNkzt97RjNlQNeiinRRCQN82Vc3Dek" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e9fc883c9.mp4?token=hInm5-yeHjEpKeW2VYhcZSBFCU60KSxIlKfJLHsTLtudGitbkBlyQp5BD1FNiKvrRQEhN6H2BJrtO6cqn3y_QpoZDfKMwMO8RvsbRTkLFiIlwwj1DrSbkc7cs4T4Ic7o0HvxwcbrtAU3HsyncRypBZWfzeo8ysvyWPuIG2fEc3FG5CNgueVfITg4ldRAC6h5BZbbtNCiPtZzPmkj_Xax1SvEKpR8-9VGDSexco2T711dxjvYanrVdmfzy7ubWfZ1mC2E6tFs0oFhehNPZEWBm4ssHS4qDISjNpjbGzbForf6L53YTuT3-Oqve5W3ot4sqMZ3bQGRZwXZvNZkRSSvyAcLpJTeB4I7YC3J4vyDeoxrkxIoydHWCyck5qixNtG1-20TBseKLk28S-DgC86UEooIOuFto-aUXaNTLXocGFnMa-uAciXTcLilu2VGVSuJ06CtCybaHz34SNlSCcwMe9dj0Nv4hsTXrdXTjzN-GdLbFFv4r0LtBRF0kMOlU1X55CLGOVpuyGxRwSN35M91qGdGZc_4DmlDkM9ZLCp4UzKn4XhNJZMsnVwFw1f3fBwY_-Bq2OC8Plqb_2VQF_GzHXcCzcjbIMwQlpZLHRNGfUZAZyLGAHjWaYt5LYajdLv1JxMMfw8j0fd_faNkzt97RjNlQNeiinRRCQN82Vc3Dek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراقب باشید! آن‌ها با «قانون» به شما حمله می‌کنند!
🔹
آنچه امروز پلیس آگاهی از آن پرده برداشت، یک کلاهبرداری ساده نبود؛ بلکه یک «جنگ روانی و حقوقی» بود!
🔹
اعضای این باند، با لباسی از جنسِ قراردادهای رسمی، به دنبال خودرو نبودند؛ آن‌ها به دنبال «خونِ پس‌انداز» مردم بودند!
🔹
ترفند آن‌ها ترسناک است: آن‌ها با تظاهر به مشتری بودن، شما را در تله‌ی قراردادهای «حق فسخ» گرفتار می‌کنند؛ جایی که شما با امضای یک کاغذ، در واقع دارید اجازه می‌دهید جیب‌تان را تا آخرین ریال تخلیه کنند!
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/684216" target="_blank">📅 15:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684212">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q45kwsRgofpKZs3k-ixUtxwEhCW9vjryPB4aWhhPEX9lHmmza939uGEW7EvUEl3JlOCOA07su0GwSx-9IeqTwj_rFayM_m4kD3cBHatNnEQWNoCmhFc8l4PaOrrnijb4rfxzyaONaBadmMITzNXxYm4G7HkGMsQd4XoPjd4kZUEoKOuObFJFEoPjVg_pTMJ3mxl4GQ2XJgakOggBYd44wfmVcFS5BVmqzQ7tDzO4TEhtLbqZV_uuIWin_-w1n0l3mPHSZKssTSGzqA6xq65E62btbdet34XrJe49aUIMWApktM_886DrV9IbOXloUJPEEJqAiSCYh7K7N1gtlGalQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XL5mQhIC7nlOgGP6It6afKwHGf5Q57kOYPZdQU3bE5CH_unQ8r8VlI_fnzkkVYcyEQFV3IPw-8f91nmGd33YFoPfq4fOLjHWX3ptKb5Br5WfZb5waboRyaFmBl9ntkU4yTCj8ImIgtHeZEeuDwRAhAZ5Tly0l-ZkL9crw8Qqog7dc3wPw2hwBiEbBWL8Q_ZYipkVLdZJOy41ce91UF1nD37Vgm1nOb0cvDjK8qQGaxTeYp6nBfK3UP21RIPYMIqPfpqqIDo2yKEUOzdj_sX9EWt1D2TpeRznrFEJpuRz8f1xW4lw6mdxL82uHJX83OsEdGi-C3Zh9JHpLxSGXDRLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjZ4p9Q3T5TcB9cPwMKQikxyBuyxRZyGS8-d0mOPLEJnoKs3P85N5ksk_VkwDU3aY5MhADX3rOW50zHfGs_AdH9EhtDTOkwuOp1Q-ui5Th_wyFAemC__4Xv_1JUpknie4exMKTNfGfzUzyuhxMt5jg-bp0moeP6bSmxWLuM_x0A2u5qV-WhoohnJ3MD23aQ2K3PVP33ZCGhkA4goD1yuQ6M9WlDc5XMpbnlTa36FNjXmFlJB4lHDkL7Jhbj0pcVEAsA7l-tXugZQwgT5G962zMuJBZWToJn174zlj56d3zd-IMSKfs1JwgBQg8MVXhydqv7GUGoC3bRh1Ln72eLxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsXW7cgUVvktP475A1m5Qv8uzGmbJSb--0YvvXIVkhnKvgXToWRdSu4Jzr-pW2bu9nffslrpS5P7rQWO1j524VPtUmQnpVCKpFaIpS_k2BiCSGzDvFJ90wBBXKWxP5yUG4Vw8V3fDP2kSTO_VbCov90OuhKZAFTWdfcFpBd1ZFwrQ9bOiD24HpjoEPCgOlRbCeewa2hmLAqW5Bz-RKzwdDQtuOMYxF_Vxq-SkzBqXWlEZc2cTmN3puvHPTsWjXrMjFAYBDqcQw7bH-WKKoD6VmdeUEeFmcvYR84M0lP7JhSNIA_rTmfu0x9_fIgap5bvtg9a-IyujON-COrLtwELDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استفاده از گوش‌پاک‌کن بیشتر از این که بهداشتی باشه به سلامت گوش‌مون آسیب می‌زنه #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/684212" target="_blank">📅 15:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684211">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3X0qHFAC88rbXSXQOg6dI9Ro9y0dYTVYVTbIVlfA1d9hiiI-0HReMV8d8gNMHNm54Xa8QfcYRipUNqxF-ioDFVsy_WfWEv3pUaAQ8pkIcC9BKzOak3kFbdAV4Zwi88-Onqo5bmWM4Vs6QxWlm5-039TXPNCaXokBN_sMwlh0WfE8lf0Krxo982XNi27vZ-AjgZsyxDg5U9wDc8wvmp417bB2SG5ZQdv0JtUq5NgMCeEEB9sUL7SiBtYNKM3EfAkqGnvRrI37KzEYxCLeSB5m6iHs5JMLoKeR4w2_C-LFLO0XaSPOcQvebYictTInYhxak_LlPe0HavLsj54l90asw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از ظرفیت‌های علمی تا حکمرانی نوین؛ مأموریت معاون علمی در کرمانشاه
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور در جریان سفر به کرمانشاه، از پارک علم و فناوری استان و شرکت‌های دانش‌بنیان مستقر در برج فناوری بازدید کرد.
🔹
حسین افشین در این بازدید ضمن آشنایی با ظرفیت‌ها و توانمندی‌های شرکت‌های فناور، در جریان مسائل، فرصت‌ها و قابلیت‌های موجود در زیست‌بوم علم و فناوری استان قرار گرفت.
🔹
شناسایی ظرفیت‌های علمی و فناورانه کرمانشاه، تقویت ارتباط میان بازیگران زیست‌بوم نوآوری، حمایت از شرکت‌های دانش‌بنیان و ایجاد زمینه برای نقش‌آفرینی مؤثرتر ظرفیت‌های بومی در اقتصاد دانش‌بنیان، از اهداف این سفر است.
🔹
این برنامه همزمان با هفته دولت و در چارچوب رویکرد معاونت علمی برای توسعه زیست‌بوم نوآوری و حرکت به سمت معماری نوین حکمرانی علم و فناوری در کشور دنبال می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/684211" target="_blank">📅 15:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684210">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz1gwEyuyrXP1AB0qozsq2Pvn2gwnl7gxHdrrM2ehDeKrlzlrgwq4ju4-67y9kqQYlAEGDQQET-RTXu_MZ5Yc4fusi_cbTXAmMzz02IZ3OLYvGviiI2kZzwtgD3a-BUoR4c4_19fFwYqv49wLE9z-eR7yHg5AaoZv9BbM0X2PTJ0V_rCGeBD5AFQhYnocQlkWFcwnaHP-iU9WBPzaTr9K5wtSQuptpygXXXAWZei2-IUoVsiuz9-9OkEEAei_sgvGbAHw5Ip3uTIZ6ckvAlft2WLmFmCe5pEnbpfl56SWDPmwRx8GrR2Erdt7-H9tJRUAFA1jsOFkTkTkQZpLqV1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
واگذاری سهام «سیمان تجارت مهریز» در فرابورس
⬅️
نشست خبری معرفی سهام شرکت «گروه صنعتی و معدنی سیمان تجارت مهریز» با نماد «سمهریز»، با حضور مدیران شرکت و خبرنگاران بازار سرمایه در فرابورس ایران برگزار شد. این شرکت در راستای سیاست‌های دولت در زمینه واگذاری بنگاه‌ها، توسعه نقش بازار سرمایه و مولدسازی دارایی‌ها، در فرابورس ایران عرضه خواهد شد.
⬅️
مدیرعامل شرکت با اشاره به ترکیب سهامداران، برنقش کلیدی بانک تجارت به‌عنوان سهامدار عمده تاکید کرد.
🔗
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/684210" target="_blank">📅 14:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684209">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ترامپ دوباره توهم زد؛ ایران حقوق نظامیانش را نمی‌دهد
رئیس دولت تروریستی آمریکا:
🔹
ایران حقوق بخش عمده‌ای از ارتش خود را نمی‌دهد؛ وی مدعی شد که ایران دچار یک بحران انسانی است که باید متوقف شود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/684209" target="_blank">📅 14:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684208">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
جزئیات نسخه تازه مصوبه مجلس
🔹
بر اساس ماده‌ی ۱۵، همه‌ی اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند.
🔹
تولید اثر هنری بدون مجوز از نهادهای قانونی کشور،…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/684208" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684207">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سارقی که گردنبند دزدی را ۱۰۰ میلیون قمار کرد
🔹
در این ویدئو روایت پیرزن مالباخته از شب حادثه و اظهارات عجیب سارق دستگیرشده  را در
#گفتگو
با خبرفوری ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/684207" target="_blank">📅 14:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684205">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUU0dI7OZ5NZ91cCc6h3G5u2YbSKJ3rArVjwXDc3xuujV9vw_qmSbFZ4u_6U9dKVvEVQPqc3-Lez2_Ermwx84vh9Az4oI535QgBfSnidzlFcvxpWbpQconpeJV44Zhs80oS-2FkyEiSI-rc7RHm1EOFS7A__DV1Q0gljLS0PL_TiQ4e82A2a30wkfY2o1xz3TsGQsdLzThTeRNw3Tykx-czawxtRk1NzoaJY1-SB59iHnWfSsYPHoxo4UwrIU4mURUxLx2KWqbwtvHw1P2VOuCOvwRTEpyn6nwTWGH7Jx8mdQ04dlhA0gfV8BsPZpNKMK3USwjyRfox7b5I-rK9cng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس، معاون ترامپ: باید به یاد داشته باشیم که کانادا یک ایالت... ببخشید، یک لغزش فرویدی بود؛ واقعاً اشتباه لفظی بود؛ کانادا یک کشور است!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/684205" target="_blank">📅 14:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684203">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEIwhkpEl3PVzz8PGd8zs9e5Qw4SotXbL3qWGJvdRKMiZ_bPtpofuwFLzxHxbUi6HkkC5RsNQ0x7WC6SgVNtbwOVQzpn_M3Ac12CzoRpMVVmwKqNRiSf606z1JS1Dv6lEjGPPLAvjVnK1HnWNkCoyg3jerHEqJSwsOsVjBD1cttmK_hCwhdalSzgAuo2fSauGDmuhQBIe7YmMkaSEUMz1KMc3Jaz-Umcc4gvG8JeEayO-2EmZS-a3L5IdCT7XQxkX_qDER6jKHLBzOo8aefnzw9ZEA2y70wJRGmdDmdyOBqj2yuKTHNsm1WtWhGlaw3NeWd6dRviHouWul1KXdDSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکسی‌های برقی بابک زنجانی به آبادان و خرمشهر رسید
🔹
فارغ از تمام حواشی، پرونده‌های متعدد و دیدگاه‌های متفاوتی که حول عملکرد بابک زنجانی وجود دارد، راه‌اندازی ناوگان تاکسی‌های‌برقی دات‌وان تریپ در منطقه آزاد اروند را باید یک تحول کارآمد زیرساختی برای مردم جنوب کشور قلمداد کرد.
🔹
شهروندان خرمشهر و آبادان که سال‌ها با دشواری‌های رفت‌وآمد شهری در گرمای طاقت‌فرسا و فرسودگی وسایل حمل‌ونقل دست‌وپنجه نرم کرده‌اند، اکنون فارغ از کشمکش‌های رسانه‌ای، ذینفعان اصلی یک ناوگان هوشمند و پاک هستند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/684203" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684202">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین دلیل کاهش استقبال از سالن‌های سینما و تئاتر چیست؟</h4>
<ul>
<li>✓ کیفیت پایین آثار</li>
<li>✓ عدم تنوع ژانرها</li>
<li>✓ افزایش قیمت بلیت</li>
<li>✓ رونق شبکه‌های نمایش خانگی</li>
<li>✓ ضعف اطلاع‌رسانی</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/684202" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684201">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
مدیریت هدفمند عرضه ارز، بازار دلار را تعدیل کرد
🔹
بانک مرکزی با تنظیم هوشمندانه عرضه ارز و پاسخ‌گویی به نیازهای واقعی اقتصاد، روند بازار دلار را به سمت ثبات و کاهش نوسانات هدایت کرد.
🔹
این اقدام در راستای کنترل تقاضای غیرمولد، تقویت آرامش بازار و صیانت از منابع ارزی کشور انجام شده است.
🔹
تأمین ارز کالاهای اساسی، مواد اولیه تولید و نیازهای ضروری همچنان با اولویت در دستور کار بانک مرکزی قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/684201" target="_blank">📅 14:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684200">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNByrrhWdEe-JRD4s7ZhQr9C4PCsdfuFDtNr9uESDlFYXf9KOouBpSPR4qLYsAq0aWwu37RJi0trSUUU5GHsTYAKQg5JdwASEONka2lb-3KVPqAaabn9p_3jpkkn3GJjeXIy67RLmv0PmZiKOn0-ZDmDUXhvkRC75JArKanXl7tqv0YeVvPdT0ueLxqC8KG0FEJAmV1KPuXJVkrQqmCp_pLUzAmkice_Jc5Ht-fMLjK4_n3Wx9g06KEU2AlgYL3c5gYMv1UH30CNnC648p_hXROe3D3O5hZq93cahXmuVm_hybu0Hc-2ofSikA_aYISx3d58sTeZI1zz7sFl6vHMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/684200" target="_blank">📅 14:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684198">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e71e6b12e.mp4?token=QI5KuqpgJa2G9p1yTtVlzYKRXes1i5g7W2Eoe0StNYqO4YR2QXfAc7UNhI33zCfxDlHlt0tMe4C4-r5McS6rQJIZ8cFRm2u7qnWsM_4AaQPJ_7bNufnuHNjG12ItyQFhS4KbJTOulp7CTV4x6l1NlbzEA5SmmsPk0v-fkdUbhaGYKVlwZ2svbYMsHjHhjffXeWYJ0F1CLy7y0tqXul5r4PtrMhgnAqZYlUqIMFyYfIIlT-j1eA1AE1RVxpQBr73hDzmH1mJnlTJuNV9YNh9ByJKAeK0hW3kJtIOupWjnG4mVdTasH_ueU8ABESv_mJlzg0M9JQJeTYtvlnLTRT4Lpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e71e6b12e.mp4?token=QI5KuqpgJa2G9p1yTtVlzYKRXes1i5g7W2Eoe0StNYqO4YR2QXfAc7UNhI33zCfxDlHlt0tMe4C4-r5McS6rQJIZ8cFRm2u7qnWsM_4AaQPJ_7bNufnuHNjG12ItyQFhS4KbJTOulp7CTV4x6l1NlbzEA5SmmsPk0v-fkdUbhaGYKVlwZ2svbYMsHjHhjffXeWYJ0F1CLy7y0tqXul5r4PtrMhgnAqZYlUqIMFyYfIIlT-j1eA1AE1RVxpQBr73hDzmH1mJnlTJuNV9YNh9ByJKAeK0hW3kJtIOupWjnG4mVdTasH_ueU8ABESv_mJlzg0M9JQJeTYtvlnLTRT4Lpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با یک بشقاب و سوزن، مدل لباس‌های قدیمی‌ رو‌ عوض کن و لذت ببر #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/684198" target="_blank">📅 14:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684197">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: آمریکا دیپلمات‌هایش را به خاورمیانه بازمی‌گرداند
🔹
بر اساس یک سند داخلی وزارت خارجه آمریکا، بازگشت دیپلمات‌های این کشور به سفار‌تخانه‌های آن در منطقه که در جریان جنگ علیه ایران تخلیه شدند، ممکن است از همین هفته آغاز شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/684197" target="_blank">📅 14:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684196">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
سامانه امداد تجار اتاق تهران؛ همراه هوشمند کسب‌وکارها
🔺
اتاق تهران با راه‌اندازی سامانه «امداد تجار»، بستری غیرحضوری و شفاف برای ثبت، پیگیری و رفع چالش‌های کسب‌وکارها فراهم کرده است. فعالان اقتصادی می‌توانند مشکلات خود را ثبت و از حمایت‌های قانونی و بسته‌های حمایتی دولت مطلع شوند.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
https://digitalchamber.ir/emdad</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/684196" target="_blank">📅 14:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684195">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjjVIc76rCFyJzwZWkU76a26EFuIr6kEnu8njIYSBfmCjPr0xGa1WMV8SY00WDDxz1taM4AeQ_JEej8K12WYL2cgn9RA0vtPj2PTiHkaR_ZoEmKKa1Bo2fCvn5WG55txuh0UjJU-nP1LQ027VDBa9_0FrIhHkAa7X19sD3S0_BVJcbrcIXDOw6qyQMS86EgYJQL8YJLJqlkE-qYDUuy-ZvrCUVlBiBQDaPaCBOGuVPfnCw2pePiaJewzngXJ4z3GO88Lp7pNi_MdMOPKRJRWAU3JtFR1HSnxGS4rIE61VElFWQMHB8EIyQuKZ2XmWEmBSvTyKk2UKblcXmhKiaPr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به اطلاع میرساند شرکت توسعه منابع آب و نیروی ایران قصد دارد ۵۷ دستگاه ماشین‌آلات راهسازی و سنگین خود(شامل انواع جرثقیل، تراک میکسر، کامیون، دامپتراک، بولدوزر، لودر، غلتک، بیل مکانیکی،‌ پمپ بتن هوایی، بونکر سیمان، تانکر آب، تانکر سوخت و...) را از طریق مزایده عمومی به فروش برساند.
🔹
مهلت دریافت اسناد:
1405/06/11
🔹
اطلاعات تکمیلی در سامانه ستاد به آدرس
www.setadiran.ir
بارگذاری شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/684195" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684194">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای الحدث: فرمانده ارتش پاکستان به ایران پیشنهاد توقف محاصره دریایی و لغو تحریم‌ها را بر اساس تفاهم‌نامه ارائه کرده است  الحدث به نقل از منابع آگاه:
🔹
واشنگتن در ازای توقف حملات گروه‌های نیابتی ایران، پیشنهاد توقف محاصره دریایی و لغو تحریم‌ها علیه ایران…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/684194" target="_blank">📅 13:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a712ce05a.mp4?token=bukpgLbnLEMcP5EPbCF51ADILIZ0arZ6euRZSP6QK0vAmjLV8dcRO9ratbEOShGHePu4GPM0WIUEJiyHjPskq4HbJjBtObQhiCYXyqJxlt7_A7chaiTQ2pdYJM8bDD4S7Gn_gqsO6BQUKdVTXZU2ZzRnYl8lWD-Wx3l2AdknBdvNw2ouPwwDhnyRzGmtCYS5T6zmaXJaMf2ZkwqXS6d4tIy49K--CRUCnCjOWB8o5tEd15kZRXWBQBUoLT7m3RYpJHY98_faMQdHzBQY_rGKZUUtW7oVdGmDlFMqX15VWZFoLjmfZ9Np9C3GHWqyrC-WOYWhyYef_3QfLJjF0vvisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a712ce05a.mp4?token=bukpgLbnLEMcP5EPbCF51ADILIZ0arZ6euRZSP6QK0vAmjLV8dcRO9ratbEOShGHePu4GPM0WIUEJiyHjPskq4HbJjBtObQhiCYXyqJxlt7_A7chaiTQ2pdYJM8bDD4S7Gn_gqsO6BQUKdVTXZU2ZzRnYl8lWD-Wx3l2AdknBdvNw2ouPwwDhnyRzGmtCYS5T6zmaXJaMf2ZkwqXS6d4tIy49K--CRUCnCjOWB8o5tEd15kZRXWBQBUoLT7m3RYpJHY98_faMQdHzBQY_rGKZUUtW7oVdGmDlFMqX15VWZFoLjmfZ9Np9C3GHWqyrC-WOYWhyYef_3QfLJjF0vvisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا اواسط هفته آینده موبایل های کشف شده به دست مال‌باختگان می رسد
سردار عباسعلی محمدیان، فرمانده انتظامی تهران بزرگ در
#گفتگو
با خبرفوری:
🔹
ما قول می‌دهیم تا اواسط هفته آینده تمام موبایل‌هایی که کشف شده به دست مالباخته ها برسد.
🔹
وقتی میلیون‌ها تلفن همراه با قیمت بالا در اختیار مردم است و در استفاده از آن دقت نمی‌کنیم، سارق به سمت سرقت وسوسه میشود.
🔹
دوربین‌های سطح شهر می‌تواند به ما برای شناسایی سارق کمک کند.
🔹
اگر زمانی ناخواسته با سارقی مواجه شدید حداقل خوب ببینید و خوب توصیف کنید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/684192" target="_blank">📅 13:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حالا زن در خانه چه کاره‌ است؟
🔹
زن هوا و بوی خوش خانواده است؛ یعنی حضور زن در خانه آن حضوریست که علاوه بر خودش، برای خانواده هم مهم و حیاتی‌ست و اصلا بدون این حضور، خانواده به معنای واقعی وجود نخواهد داشت.
🔹
«المَراَةُ الرَیحانَهةُ و لَیسَت بِقَهرَمانَة»…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/684189" target="_blank">📅 13:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684186">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d8c30461.mp4?token=ktwiDvQxFl2PdLNxDKs-l9E2ijO9beI5zvwXNfVO5cC_SRP0xrJfHXb11AgMKvQwjNTeXgdCYGF3QspkJYh2ZfSduYGo-tj6cajk-yiQRh2Fr1jtFkXOAYJ4yjFYSAOyJ3xLXW-dWfKCVv6p2Sv6BPhVJZU1PP1h8Vcz8tfNeWc2bzGgndLLjnIuVGjacAfIhNcxVDoOQSHYzo7aNDgMazcj0p_m7lYjc9kei8qkwhZDSWnC117DjDYTT-KHhgLBxfGtPKSzAPoXyokU9gx3_Lu0U1MjRJyVcLON8SSeM0jaeA5Mk-YXMJGEYyqnEsQ59TWz8HDn44zwTDTeHHYgOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d8c30461.mp4?token=ktwiDvQxFl2PdLNxDKs-l9E2ijO9beI5zvwXNfVO5cC_SRP0xrJfHXb11AgMKvQwjNTeXgdCYGF3QspkJYh2ZfSduYGo-tj6cajk-yiQRh2Fr1jtFkXOAYJ4yjFYSAOyJ3xLXW-dWfKCVv6p2Sv6BPhVJZU1PP1h8Vcz8tfNeWc2bzGgndLLjnIuVGjacAfIhNcxVDoOQSHYzo7aNDgMazcj0p_m7lYjc9kei8qkwhZDSWnC117DjDYTT-KHhgLBxfGtPKSzAPoXyokU9gx3_Lu0U1MjRJyVcLON8SSeM0jaeA5Mk-YXMJGEYyqnEsQ59TWz8HDn44zwTDTeHHYgOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پادشاه جنگل‌های هیرکانی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/684186" target="_blank">📅 13:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684184">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4d927062.mp4?token=TEDktf_sWsmFyRNA-rKOAdyv6dnm-CIb-u2ZE6r_d48KGsj1ZY2v5SL0VwnnrG6MGh8Y9FDanEdYBsiny6_YBAJndk1jLjf5ncpmqXHMjcCAiD22cXjJc7fIxSvp5OoZRaP1ltRk7V5wldjYTAzPdvVQDq3rLVhwtZPZPK-k_L7oEvxrqbzB4klctkNtkFao4JHlefzId9OlMoXeSMk4UoXwZYtuS_gOWHlMPflrd7uw1x5q86WbjuI-5DqlloOn0afhCwKwZE3HDOkeY8YG_x_vMzvWVAMUx5rJ4HPLUQoXxmd6Bg6dsql5LtUjUxHSaQiriwYPorLrEt2n50pUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4d927062.mp4?token=TEDktf_sWsmFyRNA-rKOAdyv6dnm-CIb-u2ZE6r_d48KGsj1ZY2v5SL0VwnnrG6MGh8Y9FDanEdYBsiny6_YBAJndk1jLjf5ncpmqXHMjcCAiD22cXjJc7fIxSvp5OoZRaP1ltRk7V5wldjYTAzPdvVQDq3rLVhwtZPZPK-k_L7oEvxrqbzB4klctkNtkFao4JHlefzId9OlMoXeSMk4UoXwZYtuS_gOWHlMPflrd7uw1x5q86WbjuI-5DqlloOn0afhCwKwZE3HDOkeY8YG_x_vMzvWVAMUx5rJ4HPLUQoXxmd6Bg6dsql5LtUjUxHSaQiriwYPorLrEt2n50pUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیده‌نشده از اصابت موشک‌های سنگرشکن به ساختمان شیشه‌ای در نبرد رمضان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/684184" target="_blank">📅 13:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره کلاهبرداری با جعل صدای آشنایان
🔹
معاون پلیس فتا هشدار داد کلاهبرداران با کمک هوش مصنوعی می‌توانند صدای افراد آشنا را جعل کرده و با درخواست فوری پول یا اطلاعات بانکی، افراد را فریب دهند.
🔹
پلیس توصیه کرد پیش از هرگونه واریز، هویت تماس‌گیرنده را از طریق شماره‌ای که از قبل در اختیار دارید بررسی کنید و رمز، کد تأیید و اطلاعات بانکی را در اختیار کسی قرار ندهید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/684183" target="_blank">📅 13:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684181">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e70222e5.mp4?token=UOv-Sk3F2AxlUyRcamkwi_VpWQfPHDCFQ-aFl1ecCVhfQ4YBQsnDdxPD6rXuAP7SjOWSpcSF2ZS30qRhMJu4WkcaOpR2h7KakRSMNY5_DLRYNuTMxL0s53SlW_uYqJHB3fvhGlF0ewcz7AEm53XkPGu1A5UA5sL1awL1odkcTeK1o7IZMG5J1zm1Iu1pPkTtmb52RM54NWj8ZptaFX3zY-3CRGPpiKC0LrFUqrJ4PoHG_Sz_S5_6TlcPDbXmf7jBssCIh5zpjXNr1dlq7hF9OsWo1CXWV1UbumbXAVZ2asCc-OZV6lq8XKapHEqeXNPzVzqiIfTbYbtL_6sMdItLzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e70222e5.mp4?token=UOv-Sk3F2AxlUyRcamkwi_VpWQfPHDCFQ-aFl1ecCVhfQ4YBQsnDdxPD6rXuAP7SjOWSpcSF2ZS30qRhMJu4WkcaOpR2h7KakRSMNY5_DLRYNuTMxL0s53SlW_uYqJHB3fvhGlF0ewcz7AEm53XkPGu1A5UA5sL1awL1odkcTeK1o7IZMG5J1zm1Iu1pPkTtmb52RM54NWj8ZptaFX3zY-3CRGPpiKC0LrFUqrJ4PoHG_Sz_S5_6TlcPDbXmf7jBssCIh5zpjXNr1dlq7hF9OsWo1CXWV1UbumbXAVZ2asCc-OZV6lq8XKapHEqeXNPzVzqiIfTbYbtL_6sMdItLzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین: با تحریم‌های غیرقانونی آمریکا مخالفیم  سخنگوی سفارت چین در واشنگتن:
🔹
تحریم‌های یکجانبه آمریکا علیه ایران مبنایی در حقوق بین‌الملل و مجوز شورای امنیت سازمان ملل ندارد و پکن از حقوق و منافع قانونی شرکت‌های چینی حمایت خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/684181" target="_blank">📅 12:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684179">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
لحظاتی از دیدار صمیمانه سرلشکر محسن رضایی و فیلد مارشال عاصم منیر در تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/684179" target="_blank">📅 12:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684178">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOyrtkaYZHUNqgbL5wulRXE-ai9aa_pymeDDaWkD73UOIOWe5DZsTznJsoIzZcrEubjNaLbvRSVnO7nuje67E_FAvtUURUnjmPLE_yT_n-dUK5hhqC0rlA6-N22VJfaG19p421WJDrHKGlj9CvxbMdzQMuXR80wp5RSwGZbMOeYJS2SHusghQBLjAQuwGPaflO55jOhUjjNKKFgngDWHJhZlzfcExTy2TbNfC-3CY9RtnabRaPWdu-aaONt5StJ2DXadrR5pRam642eklMm7nxuAiIze19lUTWbz3JysiFhPDOJkbOb3ZXkXZJG2bybu1ZHp6qT4daIVnkeer0Xccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/684178" target="_blank">📅 12:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684177">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_fcyk6fflA2R3EJkdbts1EjPc-PWswL1s4-qoeA149MC_XgODWEsjvQuUI-IhYiKOK2GqfU69wDBC2MYircN6IyrN7SdBv5Yen1WqYHZV2iqtR_JeXB0c3d7G5NtvBbkSPjQFdbb7jossuiviRvXEoddVlPEt3SqedUpB6pgmUAV2gV8x5yTUExMC3dddIfAdDYHKaJUf4BQmYwFDBCADiHF_j2CFB-lgfYg6XKI5jYcg-0utQIafROxb9V64BuYYF_AUWNDw9z4QjVGqxAL-p9j33qu28mvEko188R2wNTBnFL4lF8LRTIn7SOasQ-FGNzS8Fdi93YWLvFHK9aOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمهیدات جدید بانک مرکزی برای تقویت عرضه و مدیریت بازار ارز؛ تسهیل خرید اسکناس برای فعالان اقتصادی
🔹
بانک مرکزی در ادامه سیاست‌های جدید ارزی و با هدف تقویت عرضه‌ ارز، پاسخگویی به نیازهای ارزی فعالان اقتصادی و تعمیق معاملات رسمی اسکناس، تمهیدات جدیدی را برای توسعه دسترسی متقاضیان به اسکناس ارز در شبکه رسمی بانکی به اجرا می‌گذارد.
🔹
بر اساس این تصمیم، با توجه به تقویت ذخایر ارزی بانک مرکزی متعاقب اجرای سیاست‌های جدید ارزی از اواخر سال گذشته و حسب ارزیابی‌های به‌عمل‌آمده از تحولات بازار ارز، از روز سه‌شنبه مورخ ۱۴۰۵/۰۶/۰۳، کلیه اشخاص حقوقی می‌توانند با مراجعه به شعب بانک‌های عامل ملت، تجارت و صادرات، نسبت به خرید اسکناس ارز تا سقف پنج هزار (۵۰۰۰) دلار با نرخ توافقی اقدام کنند.
🔹
همچنین اشخاص حقیقی نیز می‌توانند با مراجعه به شعب بانک‌های مذکور، نسبت به خرید اسکناس ارز تا سقف هزار (۱۰۰۰) دلار اقدام کنند.
🔹
این اقدام با هدف تقویت عرضه ارز، پاسخگویی مستقیم‌تر به نیازهای ارزی فعالان اقتصادی و تعمیق معاملات در شبکه رسمی اسکناس انجام می‌شود و ظرفیت عرضه ارز از مسیر رسمی شبکه بانکی را افزایش خواهد داد.
🔹
بانک مرکزی همچنین اعلام کرده است سایر برنامه‌های مدیریت بازار ارز نیز متعاقباً اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/684177" target="_blank">📅 12:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684175">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
عرضه ۵۰۰ میلیون دلار اسکناس بانک مرکزی به شبکه بانکی؛ آمادگی برای افزایش عرضه متناسب با تقاضا
🔹
بانک مرکزی در راستای مدیریت بازار ارز و با هدف تقویت عرضه اسکناس و تسهیل دسترسی متقاضیان حقیقی و حقوقی، امروز نخستین مرحله عرضه اسکناس ارز به شبکه بانکی را آغاز می‌کند.
🔹
در این مرحله ۵۰۰ میلیون دلار اسکناس در اختیار بانک‌های متقاضی قرار می‌گیرد تا از طریق شعب منتخب و صرافی‌های بانکی به متقاضیان عرضه شود.
🔹
بانک‌های متقاضی تا ساعت ۱۳ امروز سوم شهریورماه ۱۴۰۵ فرصت دارند حجم مورد نیاز خود را برای عرضه در شعب منتخب و صرافی‌های بانکی به بانک مرکزی اعلام کنند.
🔹
بر این اساس، تمام اشخاص حقیقی و حقوقی می‌توانند با مراجعه به شعب منتخب بانک‌های عامل، نیاز خود به اسکناس ارز را از مسیر رسمی شبکه بانکی و در چارچوب سقف‌های تعیین شده، تأمین کنند.
🔹
بانک مرکزی اعلام کرده است در صورت افزایش سفارش‌های ثبت‌شده از سوی شبکه بانکی، آمادگی دارد حجم عرضه اسکناس را متناسب با میزان تقاضای ثبت‌شده افزایش دهد.
🔹
ورود ۵۰۰ میلیون دلار اسکناس به شبکه بانکی در نخستین مرحله، در حالی انجام می‌شود که بانک مرکزی بر تقویت عرضه و پاسخگویی به تقاضای واقعی بازار از مسیر رسمی تأکید دارد؛ اقدامی که می‌تواند دسترسی متقاضیان به ارز را افزایش داده و از شکل‌گیری تقاضای هیجانی و نرخ‌های غیرواقعی در بازار جلوگیری کند.
🔹
بانک مرکزی همچنین اعلام کرده است این عرضه محدود به رقم ۵۰۰ میلیون دلار نخواهد بود و در صورت نیاز شبکه بانکی، امکان افزایش حجم فروش وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/684175" target="_blank">📅 12:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684174">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4awvj_M8qPDhER1BHbXoauzvRio2HU86LJON5pWOuHBBSNPU9IaZ3D4xZXaUYVaFxK6MtmVOiVvop0TyMUsGirPwvZngg4Pbctr6_bxKoFJmasPcw4aWCrdq2D9OHY747nm3Z8XkdtYfqeehVrMfsVc7pAOUc7Ubv7xkR6JLAUyIwX8RHmZU7Bt8ggwUX69bToigojsASHVTTWEVMr4bhB6lXpocFADCp26Dj67IHZ3vfNgs8tbf_eM4pzeCE6WaDv0SkrOjUOlaAPQ02ZrGKb64m4PD-ol3DhxybM9rk9XIzbo-KjnEUGEdTqbjPG_av3bjHXta2zEY5HgBuYCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروهای داخلی ۲۰ درصد بیشتر سوخت مصرف می‌کنند
🔸
مصرف بنزین خودروهای داخلی حدود ۲۰ درصد بیشتر از نمونه‌های خارجی عنوان شده است.
🔸
در ۱۵ سال گذشته موتور جدیدی در خودروسازی کشور توسعه نیافته و ضعف فناوری موتور از عوامل اختلاف مصرف سوخت است.
@amarfact</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/684174" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845a0dd0f0.mp4?token=AwReGE5FO_5e-Q0c_cI8WX6dPzT7d-KeqcJlzxFT8TDu1rZ_sNhNkTycDk1pnI-mQKUUX78cEJpL7krNiN1U6uptjcbrroCURcZVA5gHrIelvPPriDePnp5FYnuRi-4Zzq3_-Mo3ds1WiHtnOtqtiTL74MXxNmMzxOFWtBjF_kobn8PwW5dZ_JW3nAbtmerhr-RX2_P9HFp-ifmB5mgrP5DPhYq_-NVryF42sb3JgLgroxF24xA-LS14O-EXPeKvjvucsCO1t6DZtsklJNm6r-ThJUFVsOatez9-VeclkGhDscq1dY5hd-SOEswQqd_iIvIwGlbM8bwwqNy7gw8tLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845a0dd0f0.mp4?token=AwReGE5FO_5e-Q0c_cI8WX6dPzT7d-KeqcJlzxFT8TDu1rZ_sNhNkTycDk1pnI-mQKUUX78cEJpL7krNiN1U6uptjcbrroCURcZVA5gHrIelvPPriDePnp5FYnuRi-4Zzq3_-Mo3ds1WiHtnOtqtiTL74MXxNmMzxOFWtBjF_kobn8PwW5dZ_JW3nAbtmerhr-RX2_P9HFp-ifmB5mgrP5DPhYq_-NVryF42sb3JgLgroxF24xA-LS14O-EXPeKvjvucsCO1t6DZtsklJNm6r-ThJUFVsOatez9-VeclkGhDscq1dY5hd-SOEswQqd_iIvIwGlbM8bwwqNy7gw8tLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس، معاون ترامپ: باید به یاد داشته باشیم که کانادا یک ایالت... ببخشید، یک لغزش فرویدی بود؛ واقعاً اشتباه لفظی بود؛ کانادا یک کشور است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/684172" target="_blank">📅 11:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684170">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d754d5d97.mp4?token=Rm4poEJBCOCCO8zAQxC21LnHwSW77kvBghMUUQlUWU-tm8MpF219rSYE5SMGrhsbTef-eKvs30wtl_UvCD1-rR5JrKK-WxmASaWsIocqvGHDPVnQXLFQzqwHR202mOFGH9sZkhg-fBzKvr8PLJhSPmXT58cp03kvkEa9oFE-mud7zX0pmFRPrdytOLK2ZtaqNRk0wh6eqUYwO1TN9kmNSOQ78OaINHcWS9N8F8ahNG4FzNlHYGWuH5r0J4WC1LOEsjEtKQYHNKBG02gURifJCZ7JAQoRAVzv44eo7oZXmKKkaSybLPCzcCG0hI0UDlXpsO_4--JgGr0hq46gCuV2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d754d5d97.mp4?token=Rm4poEJBCOCCO8zAQxC21LnHwSW77kvBghMUUQlUWU-tm8MpF219rSYE5SMGrhsbTef-eKvs30wtl_UvCD1-rR5JrKK-WxmASaWsIocqvGHDPVnQXLFQzqwHR202mOFGH9sZkhg-fBzKvr8PLJhSPmXT58cp03kvkEa9oFE-mud7zX0pmFRPrdytOLK2ZtaqNRk0wh6eqUYwO1TN9kmNSOQ78OaINHcWS9N8F8ahNG4FzNlHYGWuH5r0J4WC1LOEsjEtKQYHNKBG02gURifJCZ7JAQoRAVzv44eo7oZXmKKkaSybLPCzcCG0hI0UDlXpsO_4--JgGr0hq46gCuV2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابلو نقاشی نیست؛ لرستان همیشه زیباست
🇮🇷
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/684170" target="_blank">📅 11:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684168">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3a673c1e.mp4?token=XldwbjvfstYH4qge2_S5_rOYQZje-dVEFxMbvRnmqMU8cjEDXe7vuQywQhuC18I55NHrBbChnp2obkQp-3BaVQmYmReKGprWLm6S4RKs-3587i7LLKO7Js3EY__nHzLU0MBLMf2oYErboAG4HcDTY_HnoSaGS-dwAsfN9pF200l4L1Fm4YFGrIcKRI7KfM4JdtxGPw6aJJ_NIM3sIRctEtJ0mUOOPf5ljQprS7KGBnXYHRrFmKxDFbRmvEjlsSgeJbnuaRFg19qNmeLzG4JKYPRwUjK8nFsf2f4AKfn2RQ2AM1czBAocJYbBnn0sKAolFSvkKK25RJGNTSn_nuZInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3a673c1e.mp4?token=XldwbjvfstYH4qge2_S5_rOYQZje-dVEFxMbvRnmqMU8cjEDXe7vuQywQhuC18I55NHrBbChnp2obkQp-3BaVQmYmReKGprWLm6S4RKs-3587i7LLKO7Js3EY__nHzLU0MBLMf2oYErboAG4HcDTY_HnoSaGS-dwAsfN9pF200l4L1Fm4YFGrIcKRI7KfM4JdtxGPw6aJJ_NIM3sIRctEtJ0mUOOPf5ljQprS7KGBnXYHRrFmKxDFbRmvEjlsSgeJbnuaRFg19qNmeLzG4JKYPRwUjK8nFsf2f4AKfn2RQ2AM1czBAocJYbBnn0sKAolFSvkKK25RJGNTSn_nuZInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
بازتاب تلاش و خلاقیت همراهان خبرفوری در کسب‌وکارهای خانگی؛ گام‌هایی استوار برای چرخش چرخ اقتصاد خانواده.
🔸
مسیر راه‌اندازی کسب‌وکارتان را با ما به اشتراک بگذارید؛ در یک پیام صوتی ۳۰ ثانیه‌ای نام، شهر، نحوه شروع و نتیجه کارتان را بگویید و عکس کسب‌وکار را هم ارسال کنید. روایت‌های منتخب در خبرفوری منتشر می‌شوند
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/684168" target="_blank">📅 11:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684166">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=rXCqNPRnW-8AEkYsTNcuPOTpfz5LC47bwEcQUPY1LSCBqGRKIaZenLYv1j8oMql9xmwtCj0f3Ffc_I3As57or4DaVIFJJKvv3dkx8FDCqU5mI1DR_nQirovEd81v3veTyiVHgg0YNuM3PckOXknSTpfZClxGlEUKNme7t5GyMkAHpuCejTO7Emjv01nD8c4N9IEh35ETcTS6Y-AFU0noWTnmiUqnxv_g7A1EBUAWbSmzLC1vm9vnwSPor1QyTobCxWx8KXs4fs3iTkNED72-CMUXEm9gNp-5KNjHqhSP4MgznOLn70OpvN3jyNbQsVqWAddjqTAI2-7VgW2ylJfRsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=rXCqNPRnW-8AEkYsTNcuPOTpfz5LC47bwEcQUPY1LSCBqGRKIaZenLYv1j8oMql9xmwtCj0f3Ffc_I3As57or4DaVIFJJKvv3dkx8FDCqU5mI1DR_nQirovEd81v3veTyiVHgg0YNuM3PckOXknSTpfZClxGlEUKNme7t5GyMkAHpuCejTO7Emjv01nD8c4N9IEh35ETcTS6Y-AFU0noWTnmiUqnxv_g7A1EBUAWbSmzLC1vm9vnwSPor1QyTobCxWx8KXs4fs3iTkNED72-CMUXEm9gNp-5KNjHqhSP4MgznOLn70OpvN3jyNbQsVqWAddjqTAI2-7VgW2ylJfRsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد نامزد مسلمان سنای آمریکا علیه رسانهٔ نزدیک به ترامپ
السید خطاب به ترامپ:
🔹
تو نمی‌خواهی دربارهٔ قیمت بنزین صحبت کنی؛ نمی‌خواهی دربارهٔ قیمت مواد غذایی صحبت کنی؛ نمی‌خواهی دربارهٔ‌ خدمات درمانی صحبت کنی؛ نمی‌خواهی دربارهٔ این جنگ تجاری احمقانه که اقتصاد را نابود می‌کند صحبت کنی؛ جنگی که در حال نابودکردن ارتش خودمان هم هست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/684166" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684164">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyYaIGsGPANFQ6OhPTZUvCXFKDF8LIxIjEBGvCDQamIcQ5fAguofRE1BB8NtHz2Hb5Hv6HFvPN-k6_PsmVT1vJye1f3_jcI4o8ob4hg8e9CAoNkmezAeCYlDZ13GtZ_CjF1V4if1uJN0BcTYk_6YPIOeWxV8g-hVGxKpYDWTS7keDpCYj4JNgAqkkHEgEEkyZaaKd44ddQa6OnqkoYpu3EAuql8NWIAzCRUCB817twaSiezqTF7Y-FZmBsLRMNKLcgEu83meEOMCN3yfUUIU2VMwQJMSlheKnGRKWdiR1DaVcjNLvP1bTlG5VDVM7kJMTtis8kj0m6FbY3HBSIdfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhxoASpHy3I4FoLw9v8cCuVj9xogo0NiIhz7Q4Z6sPawQK15Sw5ry8HIip1Dvxt2pYp-cANrD5DmdVLZ-r_pzfG_3TRxvHse8ovIgqIVpMCIG41a-YS9tq_1nsG3kNHfGyBeMNXJUhJIagiCJXTuDdAhfn7TNNVeZRYa9ljPHfOBCeKU3JX-4v4_l_12xFzwzbBlzBSbnmGD_efyNjqP7svKiG7nfT0PoOAOF0_uOBN7phYsnUH8FWTtxycDtwZNaAGZ0Dlwm-v2xdvwIiMjm6V6Pv5ugENTbNZRFFy3gOEtKt-tcOWgxZzvd3iFIlDPTpoVFXBfgbAMMH5eM96ZAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نویسنده سابق گاردین: مصاحبه درباره حکم سنگسار سکینه آشتیانی ساختگی بود
🔹
سعید کمالی دهقان، نویسنده گزارش جنجالی گاردین در سال ۲۰۱۰ درباره سکینه محمدی آشتیانی و ادعای حکم سنگسار او، اعتراف کرد مصاحبه با آشتیانی هرگز انجام نشده و متن آن را خودش ساخته است.
🔹
او بابت انتشار این مطلب عذرخواهی و مسئولیت آن را پذیرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/684164" target="_blank">📅 11:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097af909b6.mp4?token=KwdtMT4hAMfvWU1zlqTKzVy8a-1bep8k1R7qwKuwdUllVUs74oQflWYz26yJq0Isv5kBh6x6P1_RDSOl8oqTpIhK9bJ0gTGh29cLEm4KeOphQsftp96i5EXD78uVXDu1UEteCAZABLlFcU88DUGIU327VBFqvpw_DnQLvh1t4woTiLqd1whNDRL_8GFdvCYJDx8-K4xXmdv7Bk4Bc4gf7aCuhbXY4bXeKomzApqeIGBjPoeT56Ni3O7VLrvToCmPL5Z8jeymE7X_3ClTzGQ2dlLdQJPVojcKiaKCYaWfsiOrL43d1webLUoS_KmZ_LYNJMWc8PvINxpFEEldkX0fwa40Yq5r-BIpZVk-Byq2WdbJY41BfBENAp2ShFJeaXWm8XdF7jSpx-kx6tCyaBSIDOiybah2c4Oozl1fF4VmcFQiePsNwTRa36ZgKqmgCP14CAU_E_kOvTbiqiw1sbykoZMCtDdCdQT5f9LS2Ttv9RaGy1zwJXvMFY5QhprxYKXZvdwfSb8R6HSwhXCf9YGh3q8Qi01Pxo103L7xILgjh8_qTjE8lUQNT2uMexwNGIp9yY-R9odBA5wW_UAS9DbBR60r-L-XyvUFJUuvrgdR3JxW8anbKDyJXVJYg5k8KJRZVQQU0JrpAJ7ML3WcrS2xjSbP_oGSW0FV-hC1HNOdW3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097af909b6.mp4?token=KwdtMT4hAMfvWU1zlqTKzVy8a-1bep8k1R7qwKuwdUllVUs74oQflWYz26yJq0Isv5kBh6x6P1_RDSOl8oqTpIhK9bJ0gTGh29cLEm4KeOphQsftp96i5EXD78uVXDu1UEteCAZABLlFcU88DUGIU327VBFqvpw_DnQLvh1t4woTiLqd1whNDRL_8GFdvCYJDx8-K4xXmdv7Bk4Bc4gf7aCuhbXY4bXeKomzApqeIGBjPoeT56Ni3O7VLrvToCmPL5Z8jeymE7X_3ClTzGQ2dlLdQJPVojcKiaKCYaWfsiOrL43d1webLUoS_KmZ_LYNJMWc8PvINxpFEEldkX0fwa40Yq5r-BIpZVk-Byq2WdbJY41BfBENAp2ShFJeaXWm8XdF7jSpx-kx6tCyaBSIDOiybah2c4Oozl1fF4VmcFQiePsNwTRa36ZgKqmgCP14CAU_E_kOvTbiqiw1sbykoZMCtDdCdQT5f9LS2Ttv9RaGy1zwJXvMFY5QhprxYKXZvdwfSb8R6HSwhXCf9YGh3q8Qi01Pxo103L7xILgjh8_qTjE8lUQNT2uMexwNGIp9yY-R9odBA5wW_UAS9DbBR60r-L-XyvUFJUuvrgdR3JxW8anbKDyJXVJYg5k8KJRZVQQU0JrpAJ7ML3WcrS2xjSbP_oGSW0FV-hC1HNOdW3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اون چیه که مثل یه شربت خنک وسط تابستون به دل میشینه؟!
🍹
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/684162" target="_blank">📅 11:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684161">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b84d78758.mp4?token=q-Ywizx8rBGt8WEebBLRssDhNjN7sZX0Oth1VnVU2GESZdLue30is_ITzXYPLAnxQoK3kewupRPthFkota8joMHFuAK_JDS3xe9XYcbwzEu9n6Ht3UcPaaxea0aX3a-uOSAMRq9nviFsUh1fXVRnQWQx4vremv9hZ0TwdIJ_CU1KUWx_Srk8X4SGjn4CYZMBvbMGwtU759R8MnF071GozBBf1PdTbbmSM9Co4rX6x3DzPSQvgR2yydt7GTmjWwgS10kPZnnFAOZ2PiRQuYgy8cDdYF-bjKB6buNxT5cqgRBtQPseqghKm_cKnBf9bDx-eIG_pg1Ecjs5Ga7LWrjAgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b84d78758.mp4?token=q-Ywizx8rBGt8WEebBLRssDhNjN7sZX0Oth1VnVU2GESZdLue30is_ITzXYPLAnxQoK3kewupRPthFkota8joMHFuAK_JDS3xe9XYcbwzEu9n6Ht3UcPaaxea0aX3a-uOSAMRq9nviFsUh1fXVRnQWQx4vremv9hZ0TwdIJ_CU1KUWx_Srk8X4SGjn4CYZMBvbMGwtU759R8MnF071GozBBf1PdTbbmSM9Co4rX6x3DzPSQvgR2yydt7GTmjWwgS10kPZnnFAOZ2PiRQuYgy8cDdYF-bjKB6buNxT5cqgRBtQPseqghKm_cKnBf9bDx-eIG_pg1Ecjs5Ga7LWrjAgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبدیل دوچرخه معمولی به دوچرخه برقی
🔹
هواوی موتور برقی جمع‌وجوری طراحی کرده که به بدنه دوچرخه متصل می‌شود و چرخ عقب را تا سرعت ۳۲ کیلومتر بر ساعت به حرکت درمی‌آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/684161" target="_blank">📅 11:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684160">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEb8UmQuZImhxdpHseMkK92OvleHXHNDG0QeCAsdQiHScr9wBgIz8ST6wHtbk_aP3JDc_5C9KpX3XZK_V7pcTODxkgs-SiBm8deDHM8FOFBpPZIc2mCaMu6a-Lg7WE6G490BtuFcKL8FHt4o1caAKIOYyBmeTy6TlskNmepvJU77RNxLxFoNB6-nUpnCid5r4nMfeCs1EYLgXm_bUMsRThm4lEfE1ObtibqBzZ9xwqfANqbxZwS8zNXckzxZwUM-Vr0w31mRclsR1akbftCgqLUQZl2OTs9ratMWrQGs28MqctMMxQ2kNFG1Ud5HKu86JyRpmGfKguVVfPWTbMEicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار مدیریت بحران نسبت به ناایمنی «بازار پروانه» در اراضی عباس‌آباد
رئیس سازمان مدیریت بحران شهر تهران در گفتگو با ایسنا:
🔹
بازار پروانه واقع در اراضی عباس آباد از لحاظ ایمنی خطرناک و پرریسک است. سازه‌ای که به این بازار اختصاص داده شده، برای این حجم از تردد مناسب نیست.
🔹
خطر ریزش سازه دور از ذهن نیست. ۱۷ عامل ناایمنی‌ در این بازار شناسایی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/684160" target="_blank">📅 11:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684159">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr_jw2xvKo_RsmdIRx5CsT358YWmQZv42-JxbzRwNG-gzxnsbKGx-2NNFPDiHv-Y1VPmhIKg1rjjy6xeUuxKn0YMcC6uGAG50-9IOI-JiPhctld17BAwilwDD1llYnYS7-w0qs4tycoi2ph7pNa_PWd2lVBKjKvsHfdGXZVhjOR37J2tH2YS4brGPu6oFseynXNhaGnNAJ8A1J8Rd8FbP8x6ShdVCPr78hSsZ6W-UXIbdrLEdQCGnRH4ZorWSf3vIzVDOyBtEID0CHucb1_5fJrRCSwDymSIqB6wg5t0p5yUyJ70FKT2-kNuPmOh4uSYxKipjJnDx40LG80JRVKKpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهوه رو اشتباه نخورید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/684159" target="_blank">📅 10:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684157">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/684157" target="_blank">📅 10:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684156">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
آمریکا مبادلات ورزشی و دانشگاهی با ایران را تعلیق کرد
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) با انتشار سندی اعلام کرد که واشنگتن فعالیت‌های ورزشی و تبادلات دانشگاهی با ایران را به‌طور نامحدود متوقف کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/684156" target="_blank">📅 10:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684155">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e288783b01.mp4?token=oorkRMs5rdi_S8tRRo2mV0P7y5zIdeQowjgZJYFnsvbKARk4CXbVH6_pko_iLwNCa8MrzkWCf15KrZ7GaGRvpRyWjEPtn6Gs2EM1SdJBupXuEdcjbKkfT3BzeMaz_DG4n51prLBCVY5ytiaWNzz1U4p745aI62yYJyC25iC6SngLAXgFZdV1szOSqhiot-QESWRYup_VWzAWz8IUT66yrRlSEt8q1S7KV8ISjo-2bahrk2K8JwEDlwKSdyswxqF_Lnzlp-EqPXn1EMfUH1QRNm2xFZNt-w9NuY2vd3uDL32VqLyIHcWMHYA4GL2qWuLj5Y9dF0tDyq2f7RJQvZYOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e288783b01.mp4?token=oorkRMs5rdi_S8tRRo2mV0P7y5zIdeQowjgZJYFnsvbKARk4CXbVH6_pko_iLwNCa8MrzkWCf15KrZ7GaGRvpRyWjEPtn6Gs2EM1SdJBupXuEdcjbKkfT3BzeMaz_DG4n51prLBCVY5ytiaWNzz1U4p745aI62yYJyC25iC6SngLAXgFZdV1szOSqhiot-QESWRYup_VWzAWz8IUT66yrRlSEt8q1S7KV8ISjo-2bahrk2K8JwEDlwKSdyswxqF_Lnzlp-EqPXn1EMfUH1QRNm2xFZNt-w9NuY2vd3uDL32VqLyIHcWMHYA4GL2qWuLj5Y9dF0tDyq2f7RJQvZYOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک محافظ نتانیاهو به هدفی نامشخص؛ وحشت در تل‌آویو
🔹
محافظ نتانیاهو در خیابان‌های تل‌آویو بدون دلیل به اهدافی نامشخص شلیک کرد و شاباک این اقدام را قانونی خواند.
🔹
شبکه‌های اجتماعی و رسانه‌های اسرائیلی تصاویری را منتشر کردند که در آن‌ یکی از محافظان بنیامین نتانیاهو، نخست‌وزیر رژیم صهیونیستی در حین حرکت کاروان در یکی از خیابان‌های پرتردد شهر، ناگهان  با اسلحه به هدف نامشخصی شلیک کرد و موجی از وحشت و سردرگمی را میان مردم ایجاد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/684155" target="_blank">📅 10:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684154">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f637191d0.mp4?token=q7KHcfElprjWZBr3dvj74I44gP4SZV43OaxKknzfNuBf5358HsVXfDcU3lFhGf7EXsToS0N-teyblsIg9AvTaTRWYsgwehJA4ZpuMxXBnGevzO3yfsn0s4aR2NiUQY8KGOPe6WnP3ufR0gzfljvPvgHepJtAz7NBSKsG9kkKB8pVLe8oAxk65Tj6EZj51AbrPv4AlPDyp9Fnr-M5NIWdXFBGOvQ0sg297f8W7OKMlLpb1sUKmEgaF1cP6oEHKAmqeOFDzNmYbE_qQsmaX0KPtQt3czxrsnPnGMDHQthk9wMyN5tJ7zKJelmq64ITCyZvi6uI4xlN4zntMVc4TGus3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f637191d0.mp4?token=q7KHcfElprjWZBr3dvj74I44gP4SZV43OaxKknzfNuBf5358HsVXfDcU3lFhGf7EXsToS0N-teyblsIg9AvTaTRWYsgwehJA4ZpuMxXBnGevzO3yfsn0s4aR2NiUQY8KGOPe6WnP3ufR0gzfljvPvgHepJtAz7NBSKsG9kkKB8pVLe8oAxk65Tj6EZj51AbrPv4AlPDyp9Fnr-M5NIWdXFBGOvQ0sg297f8W7OKMlLpb1sUKmEgaF1cP6oEHKAmqeOFDzNmYbE_qQsmaX0KPtQt3czxrsnPnGMDHQthk9wMyN5tJ7zKJelmq64ITCyZvi6uI4xlN4zntMVc4TGus3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاهبرداری از خریداران خانه در پوشش مشاور املاک با آگهی جعلی
پلیس اگاهی تهران بزرگ:
🔹
متهم قبلا در مشاور املاک کار می کرده است ؛ با درج آگهی جعلی به مشتریان تصاویری از خانه‌ها برای فروش و اجاره ارسال می‌نموده و سپس از مشتری بیانه ۱۰ تا ۵۰ میلیون دریافت می نمود
🔹
این پرونده ۴۰ شاکی دارد که طرح شکایت مطرح کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/684154" target="_blank">📅 10:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684153">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hobZJHoEj1VhZaW-BLEwJ6En7DfYg3xWcZTb39vuHSrzcr9bqrNzF5BRXxRzgy-vTs56ukEX2Mubh0Bo-8fWCPJY7phtViLww2Qlmkg6aoPMFDosCWHLuvBQUjV1uCOb006jzojGtLo2NYw7qjODzVAupOF5xMkwLQxy9X7_xeKZkNBOgoGJzgi-yVLsiirp_Hg_WQcVaNOAxZL3-Frp3GnOzCi5dgv2yslRSzboxTpTkV4s9V1QOq7Px3MnP0C0ilpaVZjR4W3u9FdzMznY4Yez1Vglb5SsNp6ILSfNFoYI1NUWFztO2yWy__scpe1iswxdkLQXhFSRw-mylV81jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا
🔹
عکس روز ناسا سایه زمین را در طول ماه‌گرفتگی به نمایش می‌گذارد.
🔹
حفره غول‌پیکری که در این عکس می‌بینید، سیاه‌چاله نیست. این سایه زمین است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/684153" target="_blank">📅 10:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684150">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ffe97176.mp4?token=EW4w57ja5HP4354bk5cA4-tedpMdbQSzJA-GggnrpC3FTxBxaWWAoiBb7ANwW7GzbWmjvL1k93croJodP618u2vks5ta-atxKOk5dJgcJ9Hdf6xQSr7msbIisEwhc5SnAysQIijowBE_ryBKpLqim3iCsh0-0FvPw-rB8wq61hgVD-S7p9-pLel2hTtI1AM_7JAKokAnEOiZxhTEvEEXIAGfFdomWnTTSQL13Fw91vtr8eQTBU9SOpoQhZt6-PddjoM6TD6u-ZZw8Cu_xDXvceHoJCZEKM_hjGdKR_tI2y8x6oMVx-mMdqTAUkb7l6Gk1EVjqdL0IvaFFzFbj42nHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ffe97176.mp4?token=EW4w57ja5HP4354bk5cA4-tedpMdbQSzJA-GggnrpC3FTxBxaWWAoiBb7ANwW7GzbWmjvL1k93croJodP618u2vks5ta-atxKOk5dJgcJ9Hdf6xQSr7msbIisEwhc5SnAysQIijowBE_ryBKpLqim3iCsh0-0FvPw-rB8wq61hgVD-S7p9-pLel2hTtI1AM_7JAKokAnEOiZxhTEvEEXIAGfFdomWnTTSQL13Fw91vtr8eQTBU9SOpoQhZt6-PddjoM6TD6u-ZZw8Cu_xDXvceHoJCZEKM_hjGdKR_tI2y8x6oMVx-mMdqTAUkb7l6Gk1EVjqdL0IvaFFzFbj42nHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکبار هم که شده این مدل زرشک‌پلو با مرغ رو‌ درست کن، مطمئنم پشیمون نمیشی
😋
مواد لازم:
🔹
برنج دو پیمانه
🔹
مرغ ‌پخته نصف سینه
🔹
قارچ ۱۰۰ گرم
🔹
سیب‌زمینی یک عدد
🔹
زعفران
🔹
نمک و فلفل و پاپریکا و آویشن #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/684150" target="_blank">📅 10:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684148">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8eabf04f.mp4?token=h20cu588hpMbynAmi04v8Tl8CU_Uz8Ddseaxma7lxc5crpaIg3P1UHDGGIgPldtKA-xc96tf-W0vh64hyzydqo4XWKiy6ZGAyBMZSHblDoEWkSoE6XSB4doXKUMNr3_qPg579JJhyBL0i1TQjNNViWON77FGSgi-_7OElW1QnRujyJEJhUValANLABECWuF9CM5_b80c3EYhf3ub_9nKW7wpl5iDyP0u_1S-GNCVMQrtAofLfJjT-xbhnmxfLt3ZlIH-Jns3ldRmC_jtYd-ObyG3PWCKxy3KiV1XyfWxSSlfDlez15xKGgRlFV10os3zeGW1vPJICdEnZRt2COJSTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8eabf04f.mp4?token=h20cu588hpMbynAmi04v8Tl8CU_Uz8Ddseaxma7lxc5crpaIg3P1UHDGGIgPldtKA-xc96tf-W0vh64hyzydqo4XWKiy6ZGAyBMZSHblDoEWkSoE6XSB4doXKUMNr3_qPg579JJhyBL0i1TQjNNViWON77FGSgi-_7OElW1QnRujyJEJhUValANLABECWuF9CM5_b80c3EYhf3ub_9nKW7wpl5iDyP0u_1S-GNCVMQrtAofLfJjT-xbhnmxfLt3ZlIH-Jns3ldRmC_jtYd-ObyG3PWCKxy3KiV1XyfWxSSlfDlez15xKGgRlFV10os3zeGW1vPJICdEnZRt2COJSTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت یک شفق قطبی سفید نادر در نروژ
🔹
شفق قطبی معمولاً سبز، قرمز یا آبی است. با این حال، به‌گزارش ناسا، اختلاط گازهای جوی می‌تواند در صورت همپوشانی رنگ‌های مختلف، رنگ سفید نیز ایجاد کند که در نروژ این پدیده دیده شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/684148" target="_blank">📅 09:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684147">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBzYb2Mwpp0cvTxBnrmET3klUtdmo6u9TRdU5LldN6LC465vaB9LrhF-UPC27QSG5PkFAkEuy6AFD8yIrEmVVV1AeqOtvE9RaLyUw4QncKZEZ5CVV4jLbPWP9aflFLdM8eqk_Y5klqFdQIHoOIyjdSmHUSH6MzvADxxzeNaBku5ud1oTcADAxCwbB5A-DBwd5l7sDD6hXLHannnlA4tiP0J81jBbOy_BMLUocIazECKPcl9P5BGEnZsMDDzNfaAnREKhxN1HypiYcCg7UIIXy49d-ns30s2X43JwMcrPoGaNSKlQ12Xr0Od_bODrp84zOQhDXk1Qry23gwcCJPZsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرشچیان: ممنوعیت واردات لوازم خانگی؛ شوک به بازار و هزینه جدید برای مردم
احمدرضا فرشچیان، عضو هیات نمایندگان اتاق ایران:
🔹
تغییر مداوم مقررات واردات لوازم خانگی، هر بار یک شوک جدید به بازار وارد می‌کند و در نهایت، هزینه این بی‌ثباتی و گرانی کالا را مردم از جیب خود می‌پردازند.
🔹
ممنوعیت‌های مقطعی واردات لوازم خانگی، تجارت را گران و کند می‌کند و منابع کشور را هدر می‌دهد.
🔹
به‌جای ممنوعیت واردات لوازم خانگی، باید از ابزار تعرفه‌ای استفاده کنیم. اگر واردات لوازم خانگی به نفع کشور است، باید پایدار باشد؛ نمی‌شود امروز واردات را آزاد کرد و فردا دوباره ممنوع کرد.
🔹
از مسیر کولبری و ملوانی هم باید از قواعد مالی و قانونی همراه با پرداخت حقوق گمرکی تبعیت کند.
🔹
مجوزهای کوتاه‌مدت سه یا شش‌ماهه برای واردات لوازم خانگی می‌تواند واردات را چند برابر کند؛ چون فعال اقتصادی تصور می‌کند فرصت واردات به‌زودی از بین می‌رود و همین موضوع «اشتهای کاذب» ایجاد می‌کند.
🔹
فرشچیان: تغییرات مقرراتی باید به حداقل برسد تا بازار لوازم خانگی و تجارت کشور بر پایه ثبات، برنامه‌ریزی و شفافیت حرکت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/684147" target="_blank">📅 09:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf914bc14.mp4?token=GUopI-CC3dL8zWiIW5v6qz-DVn7M_OkDUyuT8PDZfpYMF-atQjiA_rH6ljZ8h_XsGspCxs--NVpjXJohGc6FOgCba5OWPaatDCxr0JnFGwsRudQla3Ht4NRa4If9oINDt5OoTq9dYmb6UxC6Zk5Wvb46sDkZ7YgkL0xaOVOuDGyEdGvLCcG-pz_PEVDWOmFIMIqCVgckG6onqOlpgqSnX6YqsQdvKldB4jl3XPd3m70vImHwlVZZeE3m_aVslPq6FOCGedqqZYPYGpeKgMJ3BvV2TizsmErPIcbtxagJLt9RN9zJH5HOvsOFztNCCsnzCEyd0NByGqvmQVztuAltRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf914bc14.mp4?token=GUopI-CC3dL8zWiIW5v6qz-DVn7M_OkDUyuT8PDZfpYMF-atQjiA_rH6ljZ8h_XsGspCxs--NVpjXJohGc6FOgCba5OWPaatDCxr0JnFGwsRudQla3Ht4NRa4If9oINDt5OoTq9dYmb6UxC6Zk5Wvb46sDkZ7YgkL0xaOVOuDGyEdGvLCcG-pz_PEVDWOmFIMIqCVgckG6onqOlpgqSnX6YqsQdvKldB4jl3XPd3m70vImHwlVZZeE3m_aVslPq6FOCGedqqZYPYGpeKgMJ3BvV2TizsmErPIcbtxagJLt9RN9zJH5HOvsOFztNCCsnzCEyd0NByGqvmQVztuAltRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگ‌ترین شمش طلای جهان، با وزن ۵۲۱.۲ کیلو در استرالیا تولید شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/684145" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684143">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
آغاز ثبت‌نام مسکن استیجاری تهران و مشهد از فردا   وزارت راه و شهرسازی:
🔹
ثبت‌نام مسکن استیجاری زوج‌های جوان در تهران و مشهد از فردا آغاز می‌شود.
🔹
از ساعت ۱۲ روز سه‌شنبه ۳ شهریور تا پایان روز چهارشنبه ۴ شهریور متقاضیان مسکن استیجاری زوج‌های جوان در استان‌های…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/684143" target="_blank">📅 09:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684139">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
صدور آرای متهمین یکی از عجیب‌ترین پرونده‌های قضایی سال‌های اخیر کشور در استان هرمزگان
رئیس دادگستری هرمزگان:
🔹
حکم قطعی محکومیت افرادی که با سرقت از خطوط انتقال سوخت هواپیما، اقدام به قاچاق آن می‌کردند، صادر شد.
🔹
متهم اصلی به ۱۲ سال حبس، ۷۴ ضربه شلاق، ۲ سال محرومیت شغلی و پرداخت بیش از ۱۴۴ میلیارد ریال جزای نقدی محکوم شد.
🔹
متهم دوم نیز به ۵ سال و ۶ ماه حبس، ۷۴ ضربه شلاق، محرومیت شغلی و پرداخت بیش از ۵۷ میلیارد ریال جریمه محکوم شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/684139" target="_blank">📅 08:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684138">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3472337bdf.mp4?token=uV8xHfE6RodWP1Q1gh9MEM9V8bO34OMyzMKYWUd5CB0YAsiEUgPpI59huWY9rL9h-2aX-ap_v7jAJc2Uy0mczQh1V8NSJ5zotU-1w8am94ckM7ZfWn8ZIszVn1Gc1R7QFG8LEWE9Vf47PaqOokfvI49AEAC9hiK-6UeGEDiVdFsfBBa6C9YoQ_Tfyui_zR245v03TdKrojOhKV4rsjr31HoGSrAh3MUDVkU_5HXyl52oIjiR9achT70R8H019kgPH5oaMGUwYl14YkZXQkRjnkqZI8LNJSjL2xZASNyEKjTiBA5FQA5fxUUSnFywmHAHSNikA_iu6Fu-CmzAakIF2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3472337bdf.mp4?token=uV8xHfE6RodWP1Q1gh9MEM9V8bO34OMyzMKYWUd5CB0YAsiEUgPpI59huWY9rL9h-2aX-ap_v7jAJc2Uy0mczQh1V8NSJ5zotU-1w8am94ckM7ZfWn8ZIszVn1Gc1R7QFG8LEWE9Vf47PaqOokfvI49AEAC9hiK-6UeGEDiVdFsfBBa6C9YoQ_Tfyui_zR245v03TdKrojOhKV4rsjr31HoGSrAh3MUDVkU_5HXyl52oIjiR9achT70R8H019kgPH5oaMGUwYl14YkZXQkRjnkqZI8LNJSjL2xZASNyEKjTiBA5FQA5fxUUSnFywmHAHSNikA_iu6Fu-CmzAakIF2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارت زرد برای یک ربات فوتبالیست
🔹
در بازی‌های جهانی ربات‌های انسان‌نما در پکن، داور به خاطر یک ضربه خشن به یک ربات کارت زرد نشان داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/684138" target="_blank">📅 08:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684135">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wym1hmDtyT14FLHOhh2s8I2oCbfzQM3U6Lrjf5aLEa_NDqHb3CAv58C-NYgr7Gb8xHZHrngffa54LpaTSdv9S7QpqrFEBnKZIiLNNYzRhdhH3gQU9j5QxAFyzubtFYo7nU3XwvIBMR7JTOU8nNHU3ckpf45gPElrkoRVfdDq6DUSeWC46K7TKF86zgJG3L7t-KtydWvnTQCMxMfp-TTp-ZhglraXVitdiBBZidxZiXDfRqYKNznDmIVY7wlEno2CHInqXShK3RRghjt5dc-p6IrAljyNMgz8kVXAPPliAkJ3L71hJqH3tC6686BnA6Fkl-8M9C4p8uDnVRd-K4QyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میلر مذاکره‌کننده ارشد سابق آمریکا: طنز ماجرا این است که اگر آمریکا وارد جنگ نمی‌شد، تنگه هرمز باز می‌ماند
♦️
در تاریخ دکمه بازگشت به عقب وجود ندارد و در نهایت، خشم حماسی به فاجعه‌ای بزرگ منجر خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/684135" target="_blank">📅 08:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684132">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3623ddd23.mp4?token=AcDGMcwus_P9DPRotzwDnuD2SIUiyowfua9wc5SKyi_0hMo_Bbe3MxCCp4J4ur5dqA_1ECx6XDs4J-jvox5RWvNdFMynj-jvnjAogsrM_NdCH_Q9MaApEG7nvJGEKcMtgdgoqK72HGCsAvzKDlB8TYKgB9A3Yz3NTKpAOHY9eJJNN2scc9Nt9WuYmCE8CPMA_AYt0ZC2iC3XHYlghaaOdjZBr6eHUYJOZ807pArzP6YMSjXBKgrrhSDb2OOJlQHcsEOwvJGm90GkBFhHe34dExGaDP60FPjEIeCyiQC8UhrrjXUYL-E3ZgRBfwCWuya2RcMXxYc0OeRg-B_LbBJXkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3623ddd23.mp4?token=AcDGMcwus_P9DPRotzwDnuD2SIUiyowfua9wc5SKyi_0hMo_Bbe3MxCCp4J4ur5dqA_1ECx6XDs4J-jvox5RWvNdFMynj-jvnjAogsrM_NdCH_Q9MaApEG7nvJGEKcMtgdgoqK72HGCsAvzKDlB8TYKgB9A3Yz3NTKpAOHY9eJJNN2scc9Nt9WuYmCE8CPMA_AYt0ZC2iC3XHYlghaaOdjZBr6eHUYJOZ807pArzP6YMSjXBKgrrhSDb2OOJlQHcsEOwvJGm90GkBFhHe34dExGaDP60FPjEIeCyiQC8UhrrjXUYL-E3ZgRBfwCWuya2RcMXxYc0OeRg-B_LbBJXkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیر مرد ایرانی: حتی اگر مجبور شویم خاک بخوریم، هرگز ایران را تسلیم نخواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/684132" target="_blank">📅 08:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684129">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70ccf903d.mp4?token=Kq8brE9vkslIhjPE2r46HX4sqVgUjPAc3DHaYK4DJHMFKbDBRAf8pQtvdwzwC2VtoPHtWJKWg1uWUE6l394nxXDlbTi5nbBJyuaEbfZF9OGKmEIrBmgfV3k3FfQs5_q4f-dwHl2nGQCwiGvQB0Iesc7IcX9fMDr5yrd_1D1TYi_QNq0fBm4-aGAHHyDp8YIWmk4Pqi_klX6qe7BEgwGQatlDRt9Zdo64fY554ZG4kcKf67d5hFdNoSFufqXUSSPJREzMIycrhpE_nW6gWvyayqe5Byn9EDgzB8wS0Q-__AiqhBrgKCDWMtZZ0l8MO8VyVG4m1Amygnz7N87878zJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70ccf903d.mp4?token=Kq8brE9vkslIhjPE2r46HX4sqVgUjPAc3DHaYK4DJHMFKbDBRAf8pQtvdwzwC2VtoPHtWJKWg1uWUE6l394nxXDlbTi5nbBJyuaEbfZF9OGKmEIrBmgfV3k3FfQs5_q4f-dwHl2nGQCwiGvQB0Iesc7IcX9fMDr5yrd_1D1TYi_QNq0fBm4-aGAHHyDp8YIWmk4Pqi_klX6qe7BEgwGQatlDRt9Zdo64fY554ZG4kcKf67d5hFdNoSFufqXUSSPJREzMIycrhpE_nW6gWvyayqe5Byn9EDgzB8wS0Q-__AiqhBrgKCDWMtZZ0l8MO8VyVG4m1Amygnz7N87878zJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرینات اصلاحی برای قوزپشتی یا کایفوز #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/684129" target="_blank">📅 08:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684126">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8enAKtTQtCTyITOA7O5JaO2q2RQxKoVxpibBdAXaD_EOrr2UQnAWgPG4631Htw8n2Gxqa7pbIAkYj2Ts5cFBwdsw-ZR6nj6x8hn5W74Wkr-2zquk6lUtwPTMOYq0k7QPo8oQcGyOzSMMuNc2EK5Y96_TLBAFFsznwAqTsEO0MpfayTUe5FzLbqvp2zjfH3N5K02xrYPELYMFUDP6Ra9DqXE9gg5Gfv8gt-h_hhBV-8JZ2XEzc8mJ37lsdz6xbDzc0N00uyS0ptlnFe1Hhr0uwEAWrrhSW_Q72yA_xPJebdk6pKUTfG_AOK8Ynnw1Turrcuf9JnoJeZrXqktTwegYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بامداد امروز؛ هدف قرارگرفتن یک نفتکش در تنگه هرمز
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش در آب‌های ۱۷ کیلومتری منطقه «الشیشه» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفت و موتورخانه آن از کار افتاده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/684126" target="_blank">📅 07:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHImDcCWXOpnSkIT-upZ43BbTVN5uRmyJs1jmVDU_f5Ue2xKfQXEF4lPN2SVTjqeZJmOoZEGaMXbiWXB3C2wz9OxKE5zkdRZX-Yb2fv8m924gSzThEC7P1Qvu9sG6ijlYDt8PYnCNM-BPpQ8THcFa-FORIIYSPSEdMueCwx6diLXeLLUcgX2ytZ_MSv6DWjuq8wtxmnhJJTo8YcA31w0I3q6rSG7GKf48YAtIX-lk-EtuLW9nXhUQGjBgQ3FqolDbS-jGREMWxl4WtldCOaNEJxkEezuEtcpJRQi2CBwlMgcczRahmGGCmyrm1FbLQd79uyYaigYgEyz2L_DaD4IGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این کلوچه‌ از بطری پلاستیکی ساخته می‌شود
🔹
پژوهشگران با استفاده از مخمرهای مهندسی‌شده، پلاستیک PET را به ترکیبات قابل استفاده برای تولید مواد غذایی تبدیل کرده‌اند.
🔹
این مواد با فیبر و نشاسته ترکیب و با چاپگر سه‌بعدی به شکل کلوچه درآمده‌اند.
🔹
این فناوری هنوز آزمایشی و پرهزینه است، اما می‌تواند در آینده برای تبدیل زباله پلاستیکی به مواد غذایی در شرایط خاص مثل فضا یا مناطق بحران‌زده کاربرد داشته باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/684125" target="_blank">📅 07:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684121">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8gB0mHTVAEpi1ev7JoAiMbZwZaLOcFDMGT4HygDOSNYvjRr0uSxH67X99oQfyYv86CnVnMGRi2y3aVzabasZ6dcvIQqwcR7FlwFh73CgEv6eleHm96UHbDM6PcfQ4rYCHUypG2JqmkTnIFesIsFNvHjd5kNEhm9f8snokEVGpJzJv0BzXBPQAy5ogo4sRSuOrfiRL13KmYpwJpeytUsv0oLuj1v52pQuJ9wqMH4d459E5-2CCYIe9fErCLs8pY23OfBQVn_1XJksXwg5kV8cb2M9vzFhMpl16zYiKHRrHO6AOjf8lUbUiobEVlC9tE0uPvUdXhkuK-oUYc6_8jfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۳ شهریور ماه
۱۲ ربیع‌الأول ‌۱۴۴۸
۲۵ آگوست ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/684121" target="_blank">📅 07:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684119">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwv7Q6k_13QhPJExip6CoQLztGYjEsI-iGb18WKw7YVC_gt68_PiKV8c0yVpoXpHs7YUkZyjvbbMcfISM2oyfOKlkq-SlEq3LDoEPKsR3ko9Dunn0_Uby-DpmwO6e1whjIIjOnmK_hX6N_mPrdP9sdhT35GeA5cHIv0appaGC55B9CRcgLDG2Rh8w23V8hSkgGIwJ26KZ6GMzCOX8tGx86CksY9yneZg6MH8joZGo0RqX1ZxGdtLnDVLOSk4bJSMwcJbiD0neDCjIKVnBTkxZtG9ZDby04k7_kXHx3IRl6f43ziR1WwlPM_dTCWbJDcWdbn4XiKmoSSrLJsWlPoI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
سلامتی رو به شانس نسپارید!
فشار خون بالا معمولاً هیچ علامتی ندارد، اما می‌تواند خطرات جدی برای سلامتی ایجاد کند. با یک دستگاه فشارسنج خانگی، هر زمان که بخواهید در کمتر از چند دقیقه فشار خونتان را اندازه‌گیری کنید.
✅
اندازه‌گیری سریع و دقیق
✅
قابلیت تشخیص آریتمی
✅
تشخیص فشار دیاستولیک / سیستولیک
✅
حافظه ذخیره نتایج : بله
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
💰
قیمت قبلی: 1,698,000 تومان
🔥
قیمت ویژه: 1,398,000 تومان
📦
همین حالا سفارش دهید و با خیال راحت سلامت خود و
عزیزانتان را زیر نظر داشته باشید.
https://memarket24.ir/product/brief/41275/180124/</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/684119" target="_blank">📅 01:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684116">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6_LdznMtw4UQxNHrpdwaBrABHNHSXFXxikgXxx2j-DVApsCensHcFPeT35O8AhMIA5x47-Ar7R4iG8XGa5Z8JYAIxo_uGVJ_CyrDk2YdSz4L2OLOLbS5mMbFv2sPZpwGc7ir3YTVZIAeNeHVuy3hlDrpoWmDkRMBTnptDOuFQbyesQFOcGCt86GFR002cynB4FXtKdWcXi1P9Csq4wY5KTTz0XfQowhbPsj_MaddSX0oHSG1FiIPFBjRW3gVmvBRhHhh6ctFTh18s5Bk1houDtS9sxok3UqBHvlf9Jfr6pOqt2CCmbEbcPZRVZFiWV0mfUDtwB-4KBQmRWQTjdItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82af1dfb6c.mp4?token=DZhENg8Tai9mXjrL4IcnOcRFPz8bb-TIjHylIgPg4DDc-XsK2aztG2DfUMrzjlh6HsEaSagleWOtI_snK797TcuT-yWsbb_EG46LhJPPH-qe4kt7aO36dxxL53TvIY9wxjYNuazt1uM995OjxK2YE2b2f5_qkxCS8SQzySRY662bdMZ0v-t6_RASjSX_GKu1jEAJJKHVONyqn90hZwDyui2FuBqxdeExyNEdIWJ2iA9K3_ekSi-J0a9dL5pG2kG0ghh2LAvu-VXq8VeB7FvsNlN_fAvbr5vLKfxw2JPX2_hdMGMHsmQ_9MHxEb-X6A_UlmmqCT1zABWhSG5P3IQk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82af1dfb6c.mp4?token=DZhENg8Tai9mXjrL4IcnOcRFPz8bb-TIjHylIgPg4DDc-XsK2aztG2DfUMrzjlh6HsEaSagleWOtI_snK797TcuT-yWsbb_EG46LhJPPH-qe4kt7aO36dxxL53TvIY9wxjYNuazt1uM995OjxK2YE2b2f5_qkxCS8SQzySRY662bdMZ0v-t6_RASjSX_GKu1jEAJJKHVONyqn90hZwDyui2FuBqxdeExyNEdIWJ2iA9K3_ekSi-J0a9dL5pG2kG0ghh2LAvu-VXq8VeB7FvsNlN_fAvbr5vLKfxw2JPX2_hdMGMHsmQ_9MHxEb-X6A_UlmmqCT1zABWhSG5P3IQk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش طعنه‌آمیزسفارت ایران در آفریقای جنوبی به گزافه‌گویی‌های وزیر خزانه‌داری آمریکا درحالیکه بدهی آمریکا از ۴۰ تریلیون دلار عبور کرده: مهار کسری بودجه توسط وزیر خزانه‌داری نادان آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/684116" target="_blank">📅 01:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684115">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قشقاوی:
همان جوانی که پهپاد ساخت، می‌تواند اقتصاد را هم متحول کند
حسن قشقاوی، سخنگوی کمیسیون امنیت ملی و سیاست خارجی در
#گفتگو
با خبرفوری:
🔹
همان‌طور که جوانان ما در حوزه آفندی و پدافندی نظامی توانمندی‌هایشان را به دنیا نشان دادند، در حوزه اقتصادی هم باید بتوانند این توانمندی را نشان دهند و آثار تحریم‌ها را خنثی کنیم.
🔹
همان جوانی که پهپاد ساخت، می‌تواند در اقتصاد هم خلاقیت و توانمندی خودش را نشان دهد، باید بستر حضور جوانان در اقتصاد فراهم شود.
🔹
اگر کسی ۱۰ کارخانه دارد باید تشویق کنیم تا ۲۰ کارخانه داشته باشد و اگر ۲۰ کارخانه دارد بتواند ۱۰۰ کارخانه ایجاد کند. نباید در تولید محدودیتی ایجاد کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/684115" target="_blank">📅 01:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684114">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9872e711e2.mp4?token=paBRwtuB69F503kpVPuQ93OXGbcPUk1Qhfvn_Wk414vlpAMlxuj61td6P4qk7PSFQjWKqxn9hykF_CH-3mtbQX2smamxABOUu3-Np2Q5q-E64qhRgnLrJZAniUCTX0PGH4XjNcGTzj8BkiD24y9TxOZXSHYvwkNiEgXVD5qwvfgxi5LRUmwoQ_i-N8MfOtY4ID6UXEFbqmkBYAReF17jSR8e_qQ2TAzLa_tjz8SzttkVtMkcyTljGUxQZTJK5a_Jo7n_0MFbDahi0lG5IgYNUyBinG3wbuwfuetKW9RZUqClyPvxQ4lEyujBica3rUI7ef6errdfsf7RRZXobwwxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9872e711e2.mp4?token=paBRwtuB69F503kpVPuQ93OXGbcPUk1Qhfvn_Wk414vlpAMlxuj61td6P4qk7PSFQjWKqxn9hykF_CH-3mtbQX2smamxABOUu3-Np2Q5q-E64qhRgnLrJZAniUCTX0PGH4XjNcGTzj8BkiD24y9TxOZXSHYvwkNiEgXVD5qwvfgxi5LRUmwoQ_i-N8MfOtY4ID6UXEFbqmkBYAReF17jSR8e_qQ2TAzLa_tjz8SzttkVtMkcyTljGUxQZTJK5a_Jo7n_0MFbDahi0lG5IgYNUyBinG3wbuwfuetKW9RZUqClyPvxQ4lEyujBica3rUI7ef6errdfsf7RRZXobwwxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس سی‌ان‌ان: ایران آماده مقابله با تهاجم اقتصادی آمریکاست
🔹
شبکه «سی‌ان‌ان» در ویژه برنامه خود در خصوص جنگ اقتصادی آمریکا علیه ایران با «جاستین وولفرز» استاد اقتصاد دانشگاه میشیگان و سرهنگ «سدریک لیتون» تحلیلگر نظامی گفت‌وگو کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/684114" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrUxArsxXAh0oMR9GFgMTBkLcJSdnhG-ugjTgg2AHokSPOIxnejqpr0q4WdhvCw827lBbhlK6_Cq8W2amt7by3yJrbTehOC5Co-6FkGHmlKif4ptDPnnNiHCqeMAUvxJQsihvuvXi-iG3InIlGbvMCnQyxoROMVoarkwwf52YT6Jh_vdQOMmbzC1JE3e1gpA_4d6losGpquSDMnnpmFnDkOtTTss3mj7YXG9Gc_k49pzFnGaDkeaB-0uQ64721giYWgqGvAE4PrRQ_he27GLX5-v2TT-d1v16kL7Nb32YDP2uDasQz8rcQyPfsbgSQiJVuLq-2ZHpq1Oeg-s-Rln1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی، تحلیلگر سیاسی: در جریان دیدار آقای عاصم منیر و دکتر قالیباف، پیش‌شرط‌های ایران برای بازگشایی تنگه مورد بحث قرار گرفت
🔹
میانجی پاکستانی، ضمن انتقال دیدگاه دولت ترامپ، موضع ایران درباره مسیر پیش‌رو را دریافت کرد؛ نخستین گام در این مسیر، اجرای این پیش‌شرط‌ها از سوی آمریکا است. به احتمال زیاد، عاصم منیر اکنون موضع تهران را به واشنگتن منتقل خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/684113" target="_blank">📅 00:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEwAJ_etfMM8nR2dX8qOSSzd_kQtp3dT8g6NUeqir7P8sqr_jWrIwn5qx3Oku6MGX2B9YdRbTwyBsYsKrCT0kL07K-QpBpTaGfsRjTgYdJZFp0tzN4BdZ1KaE30WNSFTUKofPDEC5-f7P70QRqHL8XUprwWtfNThun5yi5l0U3w3nRR6UACOre1WUn-RnB7Sq9WK5I0fJoiYkDNMYTnt4kHpOK_7mOo0him4FNgDPQEFVk36hJ78dWrt2Mf8QAY546_vAkiJHtsppDtl9YrDsVdMY3FDG9CodUsPkGTJzdPtOjg9oedk9g3vRXGNm00AORdhRfL7nrU0MsMqXabSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه GBC:دونالد ترامپ در مسیر تبدیل شدن به احمق‌ترین رئیس‌جمهور در تاریخ ایالات متحده قرار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/684112" target="_blank">📅 00:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LALPFwJcS-Blpaz8mizV7SDurVc4u0XHfyaEGylED0BnnnoGwqXZWKT5F0RrmZzfVkdLEvQAGxtJnhzy6XLjqJXTEavGThONcYHkendu66l6XEr6o0rksozeD-90Qto3BMu6BoXNdVwQZFsTjFczpH781uIhRiVRVzfQPhgfLDlBv8spzMQ5wh3gkSGZ6WsnPi9FcuxqFFSgg13N_1L60Z1pCsTFsEA8tkavuCCCgQksGE2hCvffOGJUZ3CWgI4IZXKMjKL6VhR9p9oqkeN32SIMbPhZmjHRHEBHcgUiZgVsGuq13B262lg-37QLrsM50ugSCIdyyIrIt28jxDMRoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آنسا: جنگ در ایران به ایتالیا ۱۲ میلیارد یورو هزینه ایجاد کرد
خبرگزاری آنسا:
🔹
ایتالیا اعلام کرد که با جنگ در ایران، ایتالیا با هزینه انرژی نزدیک به ۱۲ میلیارد یورو روبرو است.
🔹
افزایش هزینه بنزین و گازوئیل را در دوره شش ماهه تقریباً ۵.۸ میلیارد یورو تخمین می‌زند. هزینه سوخت ۵.۸ میلیارد یورو، هزینه برق ۳.۸ میلیارد یورو، مشاغل کوچک بیشترین آسیب را می‌بینند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/684111" target="_blank">📅 00:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آمریکا احتمال حمله مجدد به ایران را رد نکرد
🔹
وزیر جنگ آمریکا شامگاه دوشنبه مدعی شد که در صورت شکست خوردن جنگ اقتصادی، حملات نظامی مجدداً علیه ایران از سر گرفته خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/684110" target="_blank">📅 00:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684108">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmpbAsjfrCCN1dR7G8QBvPwVPWO8S270M6xV9E-hvs_QiiiB2tdXNe53YusnwB2WVveZ5upgayRTk6AUvcYfb1lCbHNnnnafZvvZsy5wds6h1lrC2NM9j8rrY14raj46W-Gr58GENI7lu_JbBBfNO2IztcvYOBYEPg2MTaDpa-Q_mOWZQiLofP7-0vIrofypesc-Kx4_xrYABMIgb7pXC9C8dSOtW4n3LtPI1BZHbFL5DV9hwLxXEqdoebYdw8knEa_rWZMOvYQG_i_D_4-U1RqlSYXo50Cr_4HzEXMYx7Ax1qYg72Khwga1txYmx_ZNyaRYdTU-fDV5RbWcuSbCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از ترک سیگار چه اتفاقی در بدن می‌افتد؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/684108" target="_blank">📅 00:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684107">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZo0wFzpbKnOptJuRc8KzS2Ohbot3_dzlp8HxMbs8qWyTPBKe0gcODkn1v5M56xeZLA6e_AHq1-Ej0K7SXLeMKCaEBIRVqMZ9BFpQF6xrDUhx0appm3ob5CgSetKTnSan5RD05BqE1kTtqB1AC5InkLYK7D52f3EPJScQhUuFBf0q1nC5fEQ7e0TNgpSfS8cueadMxczD5iKTNHUaQeluSGQBE_MuoSptUSXmBSSHvqQRTw1LhwlDXHehL7M0sSaYm5gzDRlepogaitlREyCknuiaHP1acvQfAsUiE3OlUjxzx3K6gvfZTmeCOh5GAK1p4HMer5Qkwc9CrbpcREz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/684107" target="_blank">📅 00:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684104">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چین از جنگ ایران و آمریکا سود می‌برد؟
حسین قاهری، رئیس اندیشکده مطالعات راهبردی ایران و چین در
#گفتگو
با خبرفوری:
🔹
چین از جنگ ایران و آمریکا سودی نمی‌برد، شرایط فعلی باعث شده چین از ذخایر استراتژیک خود استفاده کند و برخی پالایشگاه‌های شمال این کشور فعالیت خود را متوقف کنند.
🔹
ایران ششمین صادرکننده نفت به چین است و چین ترجیح می‌دهد نفت را در شرایط عادی و با قیمت مناسب‌تر خریداری کند، بنابراین چین برنده این ماجرا نیست.
🔹
چین در کنترل قیمت نفت تعیین‌کننده است، استفاده چین و آمریکا و ژاپن از ذخایر استراتژیک نشان داد پیش‌بینی افزایش شدید قیمت نفت محقق نشد و این کشورها با این اقدام از نوسان بیشتر قیمت جلوگیری کردند.
🔹
اشتباه اصلی ایران در پنج دهه اخیر عدم تعریف روایت مشخص از مناسبات با چین بوده است، در حالی که کشورهای حوزه خلیج‌فارس امروز روابط قوی‌تری با چین دارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/684104" target="_blank">📅 00:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684100">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1F9KHhQ7xVBF5Yv31RvKkrRRH57hZ0LdrrOdT-mQ7WfvXiIjNS78LM2eZcSNkdzlufvcA-T89gqI5YoejyEUIJ5074owUXtlbldV8coJwrLKB-tvDrsmN0FnzVJA5eTj1eP4JEEn24uTqbtPpFpC1FVmAYgFCJJQR3LQwPtlN3-_GE7TJmp6N-_fUblN0ArZPUjTW7XFm9EIlihDx_kwt1Ebk7uRzmLqmIr2HIS4gr_g5i2KE7Vd-Z3dxx7r16-Xym_5AFyJx9tUX_y03O6eV2Dy-0h5pZIORqrS1zZ6fgwYer75Py6LN_Fyp_zgVy6_kXVpc1OMCleMEkytixolQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/684100" target="_blank">📅 00:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684099">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crklh0DdEPn0giZeFLkFkY4x6IUIxOOGHXjq2fJzrmXH_0BLBdxx-KoJlyIRjjLUd4_LIesN9EDclcEp-Y455wIoy3H-5f3DltWgbO1dU_ojU4TBe9sXIolSZ4vR4UdgVIEGM0shU5JM5egyhPnFPBEo4b6CmltnJc6gFw-vpu641Lk1qr6CIImJmEm1bepGGf3ICt6RnSuXWNfGycVSTJrMUm0vcOZXnm8C0muhjDLiCsGs22rWw92AN_zItLebBcuJpOI4tlRopzA9mspwd7IWKhBnk53P4uNGtCrKBaYG186lTxrDv1jJJ0BwSvAeSd87R8wpOlr5IrXhM9qBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر صمت: فولاد خوزستان یکی از قطب های اقتصادی کشور است/ سرعت بازسازی در این شرکت قابل تحسین بود
🔹
سیدمحمد اتابک روز دوشنبه در حاشیه بازدید از خطوط تولید و روند بازسازی خط تولید فولاد خوزستان پس از حمله دشمن آمریکایی-صهیونی، با گرامیداشت یاد و خاطره شهدای…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/684099" target="_blank">📅 00:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684097">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/472a78c05a.mp4?token=BfBX2YEK_tSsX6Eb6KCFp8RbZMFTWH2Q7pVxzVeVV77Q4sLDWaEVboa071fKCT9ao1EF7FuSKskzOtziUUpWLfcd4mL7u-iP3yVI4QmUK6aXZJd40t8W7SAcacrcVZNOaj3cBxXXTXFvoBnfCT47D4k40NDVPvTQxRXaMivvij5O_pAz7T1Z-x-uqcYUP6_ypE95g-J8H-eDiizAMLPqFypixGpZKgE3R1sOmsV5p22oSgy9w183r8ThSI9FQL0ePWk8qRGhLjhUdC1CumxzPLBWOZu6RcuFtEE-3ohPJkQJ0YggnhQKRIjn6Vj9zD9jODhxsa4BI53FYitEJ1qjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/472a78c05a.mp4?token=BfBX2YEK_tSsX6Eb6KCFp8RbZMFTWH2Q7pVxzVeVV77Q4sLDWaEVboa071fKCT9ao1EF7FuSKskzOtziUUpWLfcd4mL7u-iP3yVI4QmUK6aXZJd40t8W7SAcacrcVZNOaj3cBxXXTXFvoBnfCT47D4k40NDVPvTQxRXaMivvij5O_pAz7T1Z-x-uqcYUP6_ypE95g-J8H-eDiizAMLPqFypixGpZKgE3R1sOmsV5p22oSgy9w183r8ThSI9FQL0ePWk8qRGhLjhUdC1CumxzPLBWOZu6RcuFtEE-3ohPJkQJ0YggnhQKRIjn6Vj9zD9jODhxsa4BI53FYitEJ1qjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملکرد احتراق خودرو از پمپ شدن بنزین تا خروج دود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/684097" target="_blank">📅 23:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684096">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
جنگ ایران روزانه ۶۰۰ میلیون دلار به گردشگری خلیج فارس ضرر زد
🔹
بر اساس گزارش شورای جهانی سفر و گردشگری، جنگ اخیر ایران باعث شده کشورهای عربی حاشیه خلیج فارس روزانه دست‌کم ۶۰۰ میلیون دلار از کاهش هزینه‌کرد گردشگران بین‌المللی ضرر کنند.
🔹
نکته عجیب‌تر اینکه حتی مقاصدی که مستقیماً درگیر جنگ نیستند هم با افت تقاضا مواجه شده‌اند. اگر این روند فقط ۳ ماه ادامه پیدا کند، بین ۵۰ تا ۶۵ میلیارد دلار از گردش مالی صنعت سفر منطقه ممکن است از اقتصاد این کشورها حذف شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/684096" target="_blank">📅 23:47 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
