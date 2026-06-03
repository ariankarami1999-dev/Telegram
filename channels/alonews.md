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
<img src="https://cdn4.telesco.pe/file/Kk6zki0WAcTQH4lrISgtfPA8VutdwbqykJx-bZhBubUujfcBmzthiU4JZT5B9h3aOflFpk-lM5L7O2bWA4oRBCmq4YKngJlJvOl8W34wUMqirm0GSm_WuOBXivBx0fQnjodfS2amdTNxfHDE-ReRpZQHLAsM5kLfq_lER3GktdXTfMXTnACo3wKNp1eneo6i9ATUGry_kF-mJUxLzxypRcTmscCJjv_IsFGOiXkQOOyHtSoGVM3BSKuYxd67Yw6hEXEZvTLpDYjGVSABZkdG4hfd8hbnaezcmWALMFPETl342Y3BYHz4wUFGOlbjNqBb8sZsrg3Sd1unUySRKqXaTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 958K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 00:03:17</div>
<hr>

<div class="tg-post" id="msg-124928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ: سی‌ان‌ان یک سازمان بسیار فاسد است، با یک خبرنگار فاسد که درست آنجا ایستاده است. هرگز لبخند نمی‌زند. زنی جوان و زیبا، هرگز لبخند نمی‌زند. من هرگز لبخندی بر صورتش نمی‌بینم. او را می‌بینم که با نفرت در چشمانش ایستاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/alonews/124928" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ: آتش‌بس در لبنان با آتش‌بس در سایر نقاط جهان متفاوت است
🔴
اگر توافق کتبی امکان‌پذیر باشد، ما آن را ترجیح می‌دهیم.
🔴
ایران موافقت کرد که ما وارد شویم و اورانیوم غنی‌شده را بیرون بیاوریم اما سپس موافقت نکردند.
🔴
نیروهای ما آماده‌اند، اما بهترین گزینه رسیدن به توافقی با ایران است که بدون کشتن همه، به همان نتیجه برسد.
🔴
ما برای اولین بار با حزب‌الله صحبت کردیم و آنها موافقت کردند که به اسرائیل شلیک نکنند
🔴
ایران علاوه بر اسرائیل، به ۵ کشور در منطقه موشک پرتاب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/alonews/124927" target="_blank">📅 00:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها به امضای اسناد نزدیک هستند. اما برای رقص تانگو دو نفر لازم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/alonews/124926" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ : شی‌جین پینگ برای چین خوبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/124925" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=ZJO0udzzctW6Ose3YlP8NPgE_84b0rsFT-eS9j3ok__NihoZ52SybFR_cgG3bkDathIe2fDkwZitVEpXMHGhM-i1NtzxAxCKhvOd1_0dkA0TNFb1hqg1siIqzrHMNBFj5ssDKufcSni5w5Cj1cKsbK2n3Nfgswp04thgPzIjtAtz9DLcoOqXxVKktHMzn-x6M8PtfMy6HG1JG9p0SxBjHdzxNzOyO3Y979NL_kgqI0PQ-96xB0jxyhpZO4a2BHcdMAUZFC7F_bmU5iy9zTatzuUNu0u9-p5zipx3Pwr2jEkjP-YuCiQoFtyx6Q11JeRJyhnnWNAeQYWLGaaintwIHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=ZJO0udzzctW6Ose3YlP8NPgE_84b0rsFT-eS9j3ok__NihoZ52SybFR_cgG3bkDathIe2fDkwZitVEpXMHGhM-i1NtzxAxCKhvOd1_0dkA0TNFb1hqg1siIqzrHMNBFj5ssDKufcSni5w5Cj1cKsbK2n3Nfgswp04thgPzIjtAtz9DLcoOqXxVKktHMzn-x6M8PtfMy6HG1JG9p0SxBjHdzxNzOyO3Y979NL_kgqI0PQ-96xB0jxyhpZO4a2BHcdMAUZFC7F_bmU5iy9zTatzuUNu0u9-p5zipx3Pwr2jEkjP-YuCiQoFtyx6Q11JeRJyhnnWNAeQYWLGaaintwIHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آتش‌بس رو چطور تعریف می‌کنید؟
🔴
ترامپ : تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/alonews/124924" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae195d9e59.mp4?token=pU_yuEKUaF7gudOhEpACUi3IM387USMV682YUzsQzPaFgTYKqcfm22jVVa3Dv2yzzSx0GI2Qk4zeBwKBZpj3ytqxXgy6vA2TA1kn8SvYRp6DOm8w9iaXdOjEP0uQ1Zz3IJQc42Lz98POozzo8uoufhcMZ_w9wVCxwDU9QDuPG9swQ4I4yJDnRV1O-CtIsdEjdDWOc2NKXwuoZjrhqaBOczykX1RO8udeoXsGi2GDCHx4eacqYL1zkeDVzcIsiufsOqRifulqFgnAYnnyhyCpttzSs2hp4PuYEoCALHFfTDHsDyH9G3lBXQcbQ6syJLJFIOJfxCALBx9R9oo2YNagTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae195d9e59.mp4?token=pU_yuEKUaF7gudOhEpACUi3IM387USMV682YUzsQzPaFgTYKqcfm22jVVa3Dv2yzzSx0GI2Qk4zeBwKBZpj3ytqxXgy6vA2TA1kn8SvYRp6DOm8w9iaXdOjEP0uQ1Zz3IJQc42Lz98POozzo8uoufhcMZ_w9wVCxwDU9QDuPG9swQ4I4yJDnRV1O-CtIsdEjdDWOc2NKXwuoZjrhqaBOczykX1RO8udeoXsGi2GDCHx4eacqYL1zkeDVzcIsiufsOqRifulqFgnAYnnyhyCpttzSs2hp4PuYEoCALHFfTDHsDyH9G3lBXQcbQ6syJLJFIOJfxCALBx9R9oo2YNagTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : با توجه به حملات ایران به کویت، آتش‌بس با ایران هنوز سر جاشه؟
🔴
ترامپ : ببین، برای هر چیزی یه دلیلی هست. ما شب قبلش بهشون حسابی ضربه زدیم، حتی دیشب هم همین کارو کردیم.
🔴
(بقیه حرفاش به خاطر مشکل صدا قطع شد)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/alonews/124923" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: ترجیح می‌دهم ایران را نابود نکنم، ما میتوانیم ۲ تا ۳ هفته دیگر ادامه دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/alonews/124922" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: پریشب و دیشب به ایران حمله کردیم، ضربه خیلی محکمی به آنها زدیم
🔴
شنیده‌ام مذاکرات با ایران خیلی خوب پیش می‌رود، اگر توافقی با ایران حاصل شود، می‌تواند آخر هفته انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/124921" target="_blank">📅 23:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJ5ZfBj_xWSxM0nyw06ntTauAxGD8ybUxm6C6C4Xqqc996Dx7CVHN0helTeqJoUAcaDzdr8N6-MNoqjoW9_9y8TEzizGS6pTPDqekckXqZEnwDeG4YcPsq8yCTL-c5AYC32g57duynDBQdjDUehdy9ol3RkMgXOFuSw_ij1QQI7hRDRZ6DRqEx4fg09REZgXxBtEEhE5jblGe-W5X44vOiFt6hEB77u1xP1MFCH1lLE4TMEvh5wZrhiClv8jD5OvblylM6f_HxihMIsWk9AZqa6sb6Vcdd5DfhpKkVJmXQn7eOr6I24absHntx4HQ-XmPljCp15K9ZT_yReoXuk70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اتریوم به زیر 1,800 دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/124920" target="_blank">📅 23:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نیروی دریایی ارتش ویدیویی منتشر کرد که نشان میدهد موشک‌های ضد کشتی به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک شده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/124919" target="_blank">📅 23:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گفت و گوی ترامپ با امیر قطر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124918" target="_blank">📅 23:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu5mdFzM52o11ilF5oidPuu0oxdZ0XNcA10M0z7HZPSaOzr0mLA8R2m43Es5ES-MOrqAOFdM-pVUQCKJGvKuNLMLZwkLqbnPFWnXC9u3GXju-DDU40NrJbuWKjVw4CUAoLjJGCUu_-cVtAcEOpQpnqRhIO4S6uIEzpAVR_KkBLoc9-VVfY09AHQ-ou_UnhSkOdK1iGvMNhPwDU-ej8NggzfvN24CCuO9R7GyM2fYMiQpveZa7ETuDG9RjJH1PS_uq2Tn2-T0TDmfI5u8wjW53ZF10ETV40uohV15Zg2X4q4XJQ6RbOiuZQQ0jmLmgyszsatyHQujvMsR7XCmNcYl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای واشینگتن تایمز: دفتر بازرس کل وزارت دفاع آمریکا در حال بررسی عملیات خشم حماسی، کمپین ایالات متحده علیه ایران برای از بین بردن تهدید هسته‌ای تهران، است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124917" target="_blank">📅 23:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQtLAkZZx3_8uApRHhWm0cG6-hy3msXYNoTioLsXnrEaFonkQ7Kaw1IMgEdvnh6o14KZwZUTX-w5hdfg28K96yPx1GF2WKp7njuedh1Pn9chdSrUBGlskt9ygyahV-O4tPgXSv365vLiGyQtrLU_jBFep7i4kxc9Et9JuKZpB64uxgjXUyBIKQtLJgAZDYgE_ST2O3v4kHBWkt6SglmIWwjg17X2ALhZl3Q6LQ5MplxQJWmgN5JAHahRXi4t19SHhRi_jbpXLm6yTiqA0APo_PD_plb7hLLXg0hFfc2N2CF7HRv02M5Wxv3U8d1FLvZFoLfnTJz9ggW-CnunT6ZiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: ترامپ مدعی شد ایران موافقت کرده که سلاح هسته‌ای نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124916" target="_blank">📅 23:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQUwg1GV-jeBbU8AW9O87ggWYJLl415Ll3b7B1DPRsyoQJyZrxnI9ek46DjPLPbymImQkO-o7vvBUeC8HHmqXvhdn1RwO6Y5-_p7R6X1HxBizDmPrMt-ZWT_0KFX2iqZJgzkWOGyiNBWEbkKKSHVjmI5DykY_T1S53cP1MkBXkx0KXdfiT9qmOLXpmCBXSlea2S_JpYd4bGJbg2LmzX3ITolLKRlgJpW0cIDa6ozc4icECT6jRZA-aC_Aa7CmS3pGAuxfjESK1oH8lV-ZNCrKLuiCP21pBD7RlKFGp3Ydlejhds-9HKnFssNmLySjK3LaWpVA-wuskXzp84Ffe1Lvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من بلافاصله پس از رویداد UFC در کاخ سفید به اجلاس G7 در فرانسه خواهم رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124915" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
صدای انفجار در بحرین واربیل واقع در اقلیم کردستان عراق شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/124914" target="_blank">📅 23:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی سازمان بهداشت جهانی:
ما در کشف وسعت شیوع ابولا در جمهوری دموکراتیک کنگو بسیار دیر عمل کردیم
🔴
نوع جدید ابولا به واکسن‌های قبلی پاسخ نمی‌دهد و ما در حال تلاش برای یافتن راه‌حلی برای آن هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/124913" target="_blank">📅 23:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت دفاع: با تمام توان در مسیر تقویت بنیه دفاعی کشور، توسعه فناوری‌های راهبردی، پر کردن هرچه بیشتر دست نیروهای مسلح و صیانت از امنیت، استقلال و تمامیت ارضی جمهوری اسلامی ایران گام برخواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/124912" target="_blank">📅 23:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/124911" target="_blank">📅 23:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cL8e0yEI5zZh85UAPezglKly4vvdJxd_Sdmtlke0JQTg2wDV6jWFQD56y-tlofHI9SLWCxrKu562MzJliT6JJuRh8wvRGEbfl0M8DyO8xzkE35Xe1be8BBShOAlpElH08iWUVdcTMzXl_p8O4Qsj6Ea0UmLepjaOw22jzHVQ3onYuY9tYdICPfdLpKluaLgrtdEio72o8k7NNCmk4XTjaEtzmJ2_QMCcfbCwlBK68-CyfI1-tPoJ4dofAwOVQ6J1_rpUPaWwQjsQ9muNgahR6QEPNxKWPxhRa9KFllyaWRkc_ELw3Udyv1tcpmvs4gCVru3lD4KzBIVgPQZQx0HQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124910" target="_blank">📅 23:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت کشور بحرین به دلیل خطر احتمالی آژیر خطر را فعال کرد و از شهروندان خواست به نزدیک‌ترین مکان امن بروند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/124909" target="_blank">📅 23:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHIRUgqu-2o9KbTZeK0PQ-td97iqVQ9zoZNrlTP0Hb61XDMT8UGy_XwMnCg975IZef0XfaFqJqftWosza28WRIjG59DIUKw9sZCSXLrbOmfJGqM-yUak274U3Ni3QN8Zz0VLIUKv75qM0B_RUKOIZBq243WYmTVt_gFeZqLwtwu4UgrnliO9XY8Hpp3U7BJ_TtUxAADGq2NuAqW_jynumbLklUNvwxU70l0Hyiy1hd6yN2D6bwqCoG1nQPBdANOmkPYeKAPVtcZouJVDRB-jvgUrMcoA-vJbrEoVZXvjxDI6LIKgbrsFGRvayTPhxxNJyZiMwKRyBV7wKy-qnWwIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس:  یک مقام آمریکایی گفت مذاکرات اسرائیل و لبنان با میانجیگری ایالات متحده هنوز در وزارت امور خارجه ادامه دارد.
🔴
این مقام آمریکایی ادعا کرد: «مذاکرات به کندی آغاز شد اما سپس پیشرفت قابل توجهی در مورد یک طرح عملیاتی حاصل شد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/124908" target="_blank">📅 23:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
صدای انفجار در بحرین واربیل واقع در اقلیم کردستان عراق شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/124907" target="_blank">📅 23:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نیروی دریایی ارتش ویدیویی منتشر کرد که نشان میدهد موشک‌های ضد کشتی به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک شده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124906" target="_blank">📅 22:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سخنگوی سپاه: تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124905" target="_blank">📅 22:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124904">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghEI1FFi5mRIjgUhep69pUpXwBzwQP46x4o4K1of_-TfvlfB_QDpBWeo8WSCrGoD4VOZcVi0_6zxZO99Z4OubBCLc-F8dUPahwTgT2CcLw3MesxEbhvaeS1bWdr3xAPlNY8ZdZLPrwLWYg_HYqam8efKj6aX1R0gak1TF4FAuIIJTA5S_BsFyuQVZWQ5Hzx2mCkJib6X5SElXbBUiRas5EOreOe5mb8XLeIOU7ZDQDBprC7z7F0M9AqEG766ziiqvaJpC_kPkYlXr_4o-xbXVGuJaYXZ5imPh1o6uj_qNExL5VYB4TdRDezv8vkggvckLAiMBNf_d2ifruZ_40ladQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌‌ان‌ان : غرامت مالی یکی از اصلی‌ترین گره‌ها و نقاط اختلاف توی توافق با ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/124904" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124903">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cfe5e8eca.mp4?token=lOjPK095h5_goA2NWgXVV6xA8vZXTOLu3xXMoJnLBMiHBNuvbmkXKTMz1USO8i5ZrjCtfhXZfBW5LOqLlEuhs_xOelgZhr8wpAcWiL46HzGg2eaYZnYsyAE0pvViu-KQGrDkDL0FPF7tzfLMSDQ-6zAq4Qfq4f4xmaacfpuJgJX5bbPTpkB5SKhxrR5gbFAHvtws5WwvcIDRv9iM1V6hc5zezfTfaEL8dGNUwM5eS9WZOoIjlFtctNU7VS_MhN8KIemwWdEzgk7YUQutHecnOqS5qmi5W_lHKWCE2JpJkbROC1t2C0fj372tIUSnqDo7PIzj1-PYVaCkikw8QB4kWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cfe5e8eca.mp4?token=lOjPK095h5_goA2NWgXVV6xA8vZXTOLu3xXMoJnLBMiHBNuvbmkXKTMz1USO8i5ZrjCtfhXZfBW5LOqLlEuhs_xOelgZhr8wpAcWiL46HzGg2eaYZnYsyAE0pvViu-KQGrDkDL0FPF7tzfLMSDQ-6zAq4Qfq4f4xmaacfpuJgJX5bbPTpkB5SKhxrR5gbFAHvtws5WwvcIDRv9iM1V6hc5zezfTfaEL8dGNUwM5eS9WZOoIjlFtctNU7VS_MhN8KIemwWdEzgk7YUQutHecnOqS5qmi5W_lHKWCE2JpJkbROC1t2C0fj372tIUSnqDo7PIzj1-PYVaCkikw8QB4kWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی ارتش ویدیویی منتشر کرد که نشان میدهد موشک‌های ضد کشتی به سمت یک ناوشکن آمریکایی در خلیج عمان شلیک شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/124903" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124902">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
فارس:
نیروی دریایی ایران چند ساعت پیش یک «مرکز فرماندهی و کنترل» ارتش آمریکا را روی یک ناوشکن آمریکایی که قصد داشت به آب‌های ایران در دریای عمان نزدیک شود، هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124902" target="_blank">📅 22:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124901">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
عراقچی: لبنان در این جنگی که توسط آمریکا و اسرائیل به ما تحمیل شد هزینه داده است و ما هرگز مردم لبنان را فراموش نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/124901" target="_blank">📅 22:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124900">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHTIWlL2JUX-WZIp_T_Nac10iO0Y0Od1qRtKalf5c5xm65lMIYmL9Zyl4RlILxzRRjuk94_TPZIeQNpILzV94STTCr6NcXwyR8yKPSFoGm-ybUUIiRELVM4gJ8FPwWI_IVBx7gdZnotOyIwaH7-y9-QopIvNPQLIKsJIvAAPAdfHp56pO2xO_x5IZZffhaPEvGCmv5tWoBTxCepqb8ONN_xHbx4xeXGIKfztH_gk4yZ7i9Uwol6mgIc2ClWorrzbLXT6v2MPB5Fw1kQb8WJ9Qf-HhU8yzkHntZNMKwjChw9s6QPc-xMEIFR3W16w9RY6GW4LlrO0wTP9nBnUGNdm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تاج: ویزای آمریکا را هنوز نگرفتیم
‌
فیفا گفت در نوع خودش خاص است که ویزا صادر نشده است.
اگر در مکزیک حاضر نمی شدیم برای رفتن به کمپ تیم ملی در آمریکا به مشکل می خوردیم.
به دو نفر از اعضای تیم ویزا داده نشده است
@AloSport</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124900" target="_blank">📅 22:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124899">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💔
جاویدنام شایان شکاری ۲۰ساله از رشت
🔴
‏توی کوچه با موتورهاشون این بچه رو دوره کردن و با گلوله به کلیه و لگنش شلیک کردن، بعد انتقال به بیمارستان ولیعصر و عدم پذیرش توسط بیمارستان به بیمارستان رسول اکرم منتقلش کردن اما در اثر شدت خون ریزی ناشی از پارگی عروق و شریان اصلی رگ جاویدنام شد.
🔴
دانشجو، ورزشکار، عضو تیم ملی تکواندو نوجوانان ایران و دارنده ی مدال نقره ی آسیا
🤔
عرزشی حرام زاده این تروریست بود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/124899" target="_blank">📅 22:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عراقچی: ترامپ اگر عاقل باشد، هرگز به جنگ باز نخواهد گشت
🔴
اگر ترامپ با عقلانیت حکومت کند، هرگز به جنگ باز نخواهد گشت.
🔴
پایان جنگ در اختیار دشمن نیست و هرگز نخواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124898" target="_blank">📅 22:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124897">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo_b9kEuklqLpDq1eNKCGMak87Zy6MVgXXATOW9Sqx4khpa6Z4gh68beD282Atol6tOt6Hm1ncrmSRF25twwsEyUwQGC7DYll2vbGt5LzCZa8qtDrlmsoMeZNUcEMI8raSCAh62_OlsztdE9MtHOZu6i2yP8JEwq318TrqUkDFUAe9AAJY-3QiKiucQPPFeUSXd5lJtpWimupoQKq9vtg5Y-QlTsMpXLQrE8slsLTNx6uaGNGIFACGqHK6Eh9DpmgrozEKybQQcd61uddhlg-rJmZBy0nO8JgGCArz_sAOOXl4NEHfiIiQDto8qUocmSbySNGk5TuHgO2b-8OAw0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124897" target="_blank">📅 22:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124896">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
عراقچی: وضعیت نظامی ما اکنون بسیار بهتر است؛ چراکه توانمندی‌هایی ایجاد کرده‌ایم که در زمان جنگ در اختیار نداشتیم و صنایع نظامی ما به شکل چشمگیری فعال شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/124896" target="_blank">📅 22:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124895">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عراقچی: تماس ها با طرف آمریکایی قطع نشده ولی خب پیشرفتی هم حاصل نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124895" target="_blank">📅 22:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124894">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
عراقچی: آنچه جنگ را در دو روز گذشته متوقف کرد، در درجه اول توانایی مقاومت لبنان و توان نیروهای مسلح در ایران بود.
🔴
در زمان حمله نیروهای اسرائیلی حومه جنوبی بیروت، موضع قاطعی اتخاذ کردیم و نیروهای مسلح آماده پاسخگویی شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124894" target="_blank">📅 21:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124893">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
عراقچی: لبنان را کشوری برادر و دوست می‌دانیم.
🔴
ایران هرگز به دنبال مداخله در سیاست داخلی لبنان نبوده است.
🔴
ما دیدگاه‌ها و ملاحظاتی داشتیم که آن‌ها را بیان کردیم و حزب‌الله بخش مهمی از ساختار سیاسی لبنان است.
🔴
در آتش‌بس، از نخست‌وزیر پاکستان خواستم که عبارت «به‌ویژه لبنان» را در هنگام توقف جنگ در همه جبهه‌ها درج کند
🔴
امروز در مذاکراتی هستیم که برای دستیابی به یک یادداشت تفاهم با آمریکا انجام می دهیم که اولین مورد آن پایان جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124893" target="_blank">📅 21:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124892">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679be3bc8a.mp4?token=en0c8qCxHPHDa4UquQvTJK-udpz3n7q09Kb1F6Dh-rE17j9QYjPtLn9Rg985QhCRAEkzz73FRjVGQSUl89Zd0khMffRAOTgcKk7EvqwG_7q8jkQ1mKjeStpSxFSE3NfTJJqj_J6MSjFmUQP6hwfJDaUmjp-6ALtDG4n7BbbZat54XRL1suWj_WJ-WhmZGXrP4i0NyOwlWVJW_RjcuhKKxsQQmvwrtFK3NIRmMeWlW5XL2-af9Km59Qm_R1pWqghesF3Tqft-HrTaadsZXOY8JNHiNsa7_owjko0v32uTEPK2psTeqj4KLOCgBznAv0n9NaVbf02tPAWCJ3LeQfzSMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679be3bc8a.mp4?token=en0c8qCxHPHDa4UquQvTJK-udpz3n7q09Kb1F6Dh-rE17j9QYjPtLn9Rg985QhCRAEkzz73FRjVGQSUl89Zd0khMffRAOTgcKk7EvqwG_7q8jkQ1mKjeStpSxFSE3NfTJJqj_J6MSjFmUQP6hwfJDaUmjp-6ALtDG4n7BbbZat54XRL1suWj_WJ-WhmZGXrP4i0NyOwlWVJW_RjcuhKKxsQQmvwrtFK3NIRmMeWlW5XL2-af9Km59Qm_R1pWqghesF3Tqft-HrTaadsZXOY8JNHiNsa7_owjko0v32uTEPK2psTeqj4KLOCgBznAv0n9NaVbf02tPAWCJ3LeQfzSMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده مک‌براید: فرض می‌کنم می‌دانید گرینلند بخشی از دانمارک است؟
🔴
مارکو روبیو: فعلاً همینطور است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124892" target="_blank">📅 21:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124891">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / کانال 12 اسرائیل :ایران پیامی به آمریکا فرستاد که هر حمله‌ای به بیروت منجر به شلیک ده‌ها موشک به اسرائیل خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124891" target="_blank">📅 21:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124890">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی سپاه: تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124890" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124889">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
روسیه: ایران بارها اعلام کرده در پی سلاح اتمی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124889" target="_blank">📅 21:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124888">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb6a3f5f2.mp4?token=dll2s2toZa92HBN9AEt5WotMyzfCBBpw6ukr-LmItKmARcWygOpTbZS-BvCdZZ5y--3J9G-vlxVV2YaF6AZW2MiTd--W7xl0bq971-BhX1dSEVmOavalz1BdHm0k09OSeY-1yPt4BtwCBrgMbd81aMEe88b8Bc_zuILDyVckjijVnp3a8c94ujFnLS8PQQI10GdthJTle8Jv3dQEzGicidc33suXoeEB7kgTAVVctBTwm7ZdSCnUDFOsSXGSm0xGbjRwpGQkZgxwnUz0wPfbbwz5VVnVtv4LEaAwTVXVLxo4z1VXIgN2FrmDId1xIByWcBR6MqcdjEy0V4ajRZtY4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb6a3f5f2.mp4?token=dll2s2toZa92HBN9AEt5WotMyzfCBBpw6ukr-LmItKmARcWygOpTbZS-BvCdZZ5y--3J9G-vlxVV2YaF6AZW2MiTd--W7xl0bq971-BhX1dSEVmOavalz1BdHm0k09OSeY-1yPt4BtwCBrgMbd81aMEe88b8Bc_zuILDyVckjijVnp3a8c94ujFnLS8PQQI10GdthJTle8Jv3dQEzGicidc33suXoeEB7kgTAVVctBTwm7ZdSCnUDFOsSXGSm0xGbjRwpGQkZgxwnUz0wPfbbwz5VVnVtv4LEaAwTVXVLxo4z1VXIgN2FrmDId1xIByWcBR6MqcdjEy0V4ajRZtY4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیرو زمینی اسرائیل تصاویری از تخریب یکی از روستای های جنوب لبنان منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124888" target="_blank">📅 21:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124887">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
جروزالم پست: کویت پس از حمله جمهوری اسلامی به فرودگاه کویت، دو دیپلمات ایرانی را از کشور اخراج و کاردار تهران را احضار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124887" target="_blank">📅 21:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124886">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ccd72fe8.mp4?token=ABvxaspZ4AoPH2mo6ktnh-dB5jv1dkcSiOkS3GmdHxwIbACWXMZyUCMSzlG6tP3hD3p5sDbaYrjUJ4KGQduJblDXBJAKcrCXvaNMLQHAe0MRC7GDcB-LRUOxOB6wj0Hj41mi2EUz38e2x7ZTB1ApyRY2PUpmqm3_5p8KpQzKeDwDBm0xRemrhXvu2FukICgGZ5cXr736Obuc7gaGh9X-RS2qZtbu2HEjnmDFsPAlbjoiQzAXExFNZ4JANyrsV3Hz-bYV7pdPO-rd8dc-UjbQcNrjFlT2DzoDWa-_KQgSbZtxdqgy33NY9xX6odOx_fGcYH3UIGTCaxV9cDjr4-cxeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ccd72fe8.mp4?token=ABvxaspZ4AoPH2mo6ktnh-dB5jv1dkcSiOkS3GmdHxwIbACWXMZyUCMSzlG6tP3hD3p5sDbaYrjUJ4KGQduJblDXBJAKcrCXvaNMLQHAe0MRC7GDcB-LRUOxOB6wj0Hj41mi2EUz38e2x7ZTB1ApyRY2PUpmqm3_5p8KpQzKeDwDBm0xRemrhXvu2FukICgGZ5cXr736Obuc7gaGh9X-RS2qZtbu2HEjnmDFsPAlbjoiQzAXExFNZ4JANyrsV3Hz-bYV7pdPO-rd8dc-UjbQcNrjFlT2DzoDWa-_KQgSbZtxdqgy33NY9xX6odOx_fGcYH3UIGTCaxV9cDjr4-cxeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خودش را یکی از برترین نوابغ تاریخ آمریکا نامید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124886" target="_blank">📅 21:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124885">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGTkM62xjTr-5rnFu1d897uxDNoYM4df91OKBnRcCP6yVAnNrLsMnctsdqglk1tleBjFcPhLhlyKR3DU6qooijeWZ8Uxc2Gon3-oC_h-vyuit6LHpLY0fDERTRMPJGos77gTiZcry2nOdJLGamN0q53oWSCFNDInlP-Y2hQ5aU1QIGJTEj11IrNijAUn9SFwCDLt-oJ5gQHpiMMKEmE4dXrFpwJMHrumtOKuvs22sUWz9SAb9qQ2iv1K_Tc9SUUNIIBispk_jPg-2PhH-LGH6X3z3bpGMgzqoojCMA4J9GB7q1iB0ZHjTrDdE7LZvxc0NsBfnOXjVAcKSzxWoTc2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دست‌کم ۴ فروند تانکر سوخت‌رسان نیروی هوایی آمریکا اکنون از تل‌آویو و پایگاه هوایی شاهزاده سلطان در عربستان سعودی به سمت خلیج فارس در حال حرکت هستند. قرار است این هواپیماها به دو تانکر دیگر که هم‌اکنون در منطقه فعال‌اند، در کنار یک فروند آواکس E-3B نیروی هوایی آمریکا ملحق شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124885" target="_blank">📅 21:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: غنی سازی 60 درصدی ایران هیچ توجیهی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124884" target="_blank">📅 21:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124883">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای در تیم مذاکره‌کننده ایران: دلیل عدم موفقیت مرحله اول مذاکرات اسلام‌آباد، امتناع ایران از ورود به مذاکرات هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124883" target="_blank">📅 21:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124882">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2ff479d5.mp4?token=oOI2pW62YTEYmpehU5U_vzGbWu0MeR4G6jM6osTHOcXFnREjPP5RL8YerN80uYyQ3de6bWf5zWTSNJFgzg8F5UhVn28m7aDZ1d52ThFCkXSNwl1xMlfs5GCRnTdV9I4l3Am8ImpeQmd_LbmjyjojB8tayFKDytcwpK8qpxlAjqLQg1qu7i9KZ5Aaf4hMzygFPeRM3me4CtQ8T6WhuGpx7VS1kGmLGvpuurOtb4dWFWtFTM6mT0eYducXsFtBIzqW94olkn3nselPLAXX4OXq9BDYptbUp2YlCwOxWC9Nf2FVw1dbUGB5TV9SvluaLDqEKvcvm6Or6ABk6_ZtFIbecw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2ff479d5.mp4?token=oOI2pW62YTEYmpehU5U_vzGbWu0MeR4G6jM6osTHOcXFnREjPP5RL8YerN80uYyQ3de6bWf5zWTSNJFgzg8F5UhVn28m7aDZ1d52ThFCkXSNwl1xMlfs5GCRnTdV9I4l3Am8ImpeQmd_LbmjyjojB8tayFKDytcwpK8qpxlAjqLQg1qu7i9KZ5Aaf4hMzygFPeRM3me4CtQ8T6WhuGpx7VS1kGmLGvpuurOtb4dWFWtFTM6mT0eYducXsFtBIzqW94olkn3nselPLAXX4OXq9BDYptbUp2YlCwOxWC9Nf2FVw1dbUGB5TV9SvluaLDqEKvcvm6Or6ABk6_ZtFIbecw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدهای سقوط هلیکوپتر نیروی دریایی سلطنتی در دوون اوایل صبح امروز.
🔴
سه نفر از پرسنل نیروی دریایی سلطنتی بریتانیا در جریان سقوط هلیکوپتر حین یک تمرین آموزشی جان خود را از دست دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124882" target="_blank">📅 21:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124881">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2236543d19.mp4?token=qiQMLkBfkz0y0uRRdjKup1fRADTLngw2NO5vbn9Xe5gFZffwxD4dATRJyoPzttyIvrE5LPMHwPdOLhmfFseSp3gsWwtX8x59Ex_6QEatWLFQljgKJ0rdcyJRpQyR0nsjU93zaaCp-jgpANRzIWpxyU-2n9qh_x8FNESTi4zvNsTY0d9VXUBNZ0xO-bRdFEtdmHfxW42iyMQ2tAzE9n2IRD8eqzOwXMdABSquo5IYrnFwvT1ApGeHeSWTK8Nx13RLyxUADal0j_t1-778chTAUICGwUa7qMOpfKAeZXgTJo13BiGzwbM2LYKHYYjoz8pFbBGAMxLnoCFdiandLjWXCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2236543d19.mp4?token=qiQMLkBfkz0y0uRRdjKup1fRADTLngw2NO5vbn9Xe5gFZffwxD4dATRJyoPzttyIvrE5LPMHwPdOLhmfFseSp3gsWwtX8x59Ex_6QEatWLFQljgKJ0rdcyJRpQyR0nsjU93zaaCp-jgpANRzIWpxyU-2n9qh_x8FNESTi4zvNsTY0d9VXUBNZ0xO-bRdFEtdmHfxW42iyMQ2tAzE9n2IRD8eqzOwXMdABSquo5IYrnFwvT1ApGeHeSWTK8Nx13RLyxUADal0j_t1-778chTAUICGwUa7qMOpfKAeZXgTJo13BiGzwbM2LYKHYYjoz8pFbBGAMxLnoCFdiandLjWXCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون| رعد و برق در غرب استان تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/124881" target="_blank">📅 21:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124880">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فاکس نیوز:  «جمشید غومی»، مدیرعامل یک شرکت فناوری در ایالت کالیفرنیا، به اتهام تأمین تجهیزات برای برنامه‌های هسته‌ای و نظامی ایران بازداشت شد؛ وزارت دادگستری آمریکا این خبر را اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124880" target="_blank">📅 20:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124879">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نتانیاهو : با هم انجام دادیم، تو نزدیکی و همکاری‌ای که قبلاً هرگز نداشتیم
🔴
باید دوباره بگم، رئیس‌جمهور ترامپ بهترین دوست اسرائیل بوده که تا حالا داشتیم؛
🔴
هیچ‌وقت چنین دوستی تو کاخ سفید نداشتیم، او از همه جلو زده، و این شراکت خیلی قوی
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124879" target="_blank">📅 20:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124878">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc68640c6.mp4?token=Fompo1x1qfjh9-6cfqOcinCY_gj4NNuRnkHUipJQI3nZMw_vu3zkV_22qhznm-aHW7fvOQe8L4VAKVenBGjRtNDnS2zscPSN6lZB2XTVrkUa3-f55wpB6RfeCilUbGNt71fSzAIEfkhmuTbw9bNByR50AB98kjnQfCVRF7qLIAaHb4UdfBEALWk-e193cobum-hpVyGfJSrM2Bif1rXQ2M2oa0kiN1fLj6i2A95XrqsrpBbyqpIESf7qyxcpAgyIKf0K0MK8glr69H7rnb1FuZDO-oJMZ86OVLkrJjwkUNuNoz5FOJKiCCMbW6WFmdtKFvSEUGK9G8u9rSAm0N1Omw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc68640c6.mp4?token=Fompo1x1qfjh9-6cfqOcinCY_gj4NNuRnkHUipJQI3nZMw_vu3zkV_22qhznm-aHW7fvOQe8L4VAKVenBGjRtNDnS2zscPSN6lZB2XTVrkUa3-f55wpB6RfeCilUbGNt71fSzAIEfkhmuTbw9bNByR50AB98kjnQfCVRF7qLIAaHb4UdfBEALWk-e193cobum-hpVyGfJSrM2Bif1rXQ2M2oa0kiN1fLj6i2A95XrqsrpBbyqpIESf7qyxcpAgyIKf0K0MK8glr69H7rnb1FuZDO-oJMZ86OVLkrJjwkUNuNoz5FOJKiCCMbW6WFmdtKFvSEUGK9G8u9rSAm0N1Omw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : با هم انجام دادیم، تو نزدیکی و همکاری‌ای که قبلاً هرگز نداشتیم
🔴
باید دوباره بگم، رئیس‌جمهور ترامپ بهترین دوست اسرائیل بوده که تا حالا داشتیم؛
🔴
هیچ‌وقت چنین دوستی تو کاخ سفید نداشتیم، او از همه جلو زده، و این شراکت خیلی قوی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124878" target="_blank">📅 20:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124876">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvS3_lLr5dhEPBRFtfMaims3lEzC8veMpCPUFgcZe9Ik_z_hrSWqc8kj7xMMeWOEGUHVV5McvwTrxtQJdbBRa4ky2w71p2IA_5qmHPKVB_nWEcXrTjNZs3ctit7ejdzJyY-jILPWZkPGGQloWM_2ztB4pumfTnMj7u0bidAbn8VyyEsyAsYKON2c0HblwEhDtlY6iqv7_r7dINyrHYGyn4bdOzfK1g-YKDDw1AZlvKZDIN5Fva8NcO22QAjfKrUra0KRFUqy97IDfU-NvkooFaSpNV1Y91yQixrFoDCBNgAm3ckFzy0KbugujTdb4m8GN-cO4wh7eghYVxj9HgCLpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194eb7223c.mp4?token=VLVWK7rVKolP1Y-lCP1fsFptcK17SUSinvYshLOWLRptwn56FBZdWWneJuOBsEKZP64omg84VLHCBuHFsPI2GQ8hIzlXcMuwoHnF0pf2VEyHKPoeOUPwefvLVOSQDsHdWsLYYCYMQ0YAEYc-_nU2rR4dDb9NwOSDtqhWtXgH7hxttEnCE6oWv55rL6AtXDYCmoR1Joga0-O3aPREUFei31stVNx4wETxsN8KHYN5HjDYk5usRSUGmMSmTO5Z5-BxIyLiH0up-B8-F5t6GlzjYqKKcE6Yf03TSI5AMPsQVsHmQ1lUACrqGOWn8_oa3l2RMHWkZkvLn5McaT49qFwXVBcFFdzIjeA5UwCdj5EqcEBPfrLG0ksakTWqg3iI-HW9dsdMsZKXPeiSO06T8nh3Tld_xKyeJCgnSi0y6s3Rc2HGI0UXAHHheBMaKWXV1HM2pv1my2Oi51hYSK-GwsQmC2mbNBT2BYi02YkvkhgUtwh4_Zl03TymRBg36wwxljuAjLMDoY7x2MVUHAxYx7AisSgfLPyC3Hku2qxjVU3D_Bk9XK4sAV26M3GOkG20GRTW-EqrMsIC-RVdlFQXTFGTkcjqRoXAUgJjfp_EWvyoi2opcqx8f9zDrFqdNPgVoR_BHGJx-51N2KTI8ebCci4vgkAmCBhvE7AY9DO-rN6smQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194eb7223c.mp4?token=VLVWK7rVKolP1Y-lCP1fsFptcK17SUSinvYshLOWLRptwn56FBZdWWneJuOBsEKZP64omg84VLHCBuHFsPI2GQ8hIzlXcMuwoHnF0pf2VEyHKPoeOUPwefvLVOSQDsHdWsLYYCYMQ0YAEYc-_nU2rR4dDb9NwOSDtqhWtXgH7hxttEnCE6oWv55rL6AtXDYCmoR1Joga0-O3aPREUFei31stVNx4wETxsN8KHYN5HjDYk5usRSUGmMSmTO5Z5-BxIyLiH0up-B8-F5t6GlzjYqKKcE6Yf03TSI5AMPsQVsHmQ1lUACrqGOWn8_oa3l2RMHWkZkvLn5McaT49qFwXVBcFFdzIjeA5UwCdj5EqcEBPfrLG0ksakTWqg3iI-HW9dsdMsZKXPeiSO06T8nh3Tld_xKyeJCgnSi0y6s3Rc2HGI0UXAHHheBMaKWXV1HM2pv1my2Oi51hYSK-GwsQmC2mbNBT2BYi02YkvkhgUtwh4_Zl03TymRBg36wwxljuAjLMDoY7x2MVUHAxYx7AisSgfLPyC3Hku2qxjVU3D_Bk9XK4sAV26M3GOkG20GRTW-EqrMsIC-RVdlFQXTFGTkcjqRoXAUgJjfp_EWvyoi2opcqx8f9zDrFqdNPgVoR_BHGJx-51N2KTI8ebCci4vgkAmCBhvE7AY9DO-rN6smQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام سید داوود امامی میبدی ۳۹ ساله، ۱۸ دی ، میبد یزد
🔴
علیرغم تلاش رژیم برای تصاحب مرگ او بخاطر مذهبی بودنش، خانواده اجازه ندادند تا این اتفاق بیفتد.
🤔
عرزشی حرام زاده، غیرتت رو دادای، شرفت رو دادی، دینت رو دادی که اسلحه بگیری به سمت مردم خودت
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124876" target="_blank">📅 20:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزارت امور خارجه انگلیس امروز چهارشنبه به بهانه ورود یک پهپاد روسی به رومانی اعلام کرد که سفیر روسیه را احضار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124874" target="_blank">📅 20:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
خبرگزاری فارس، به نقل از مذاکره‌کنندها :  ما هیچ توافقی رو قبول نمی‌کنیم که لبنان نادیده گرفته بشه یا از معادله حذف بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124873" target="_blank">📅 20:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05cf1b4b47.mp4?token=DRVxmkG742-_Uc7LIplu5DmNqSVpASDH_mUml7BfuNYjNmEPIgaqXxvd6nR-FTNU5OC5771R2sT_QS9SozEUcY0L8jz3AlIwvYBzhFpfWOc0kNtuD4oeDEeyuDszjjU5yVuwkIrdHN3obgN9NcAgFR5FHpRtMbfajR6gy8azVIlZJTqbm_uB1biIWCrStl4cEgyhxRQ3XqNUnAVdtm3nv4shBPiRZCFTTgd87XkF5l1FHmlyj7S3Ub_HZMxZfp0iLiahhOtDRJzJYTt7Iy0p-kuaKo7T3-2fZdEO-B1wSg7XbXFzQbeNNFswhUkwNXSDhkalyPSOBtMbTID1aIY3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05cf1b4b47.mp4?token=DRVxmkG742-_Uc7LIplu5DmNqSVpASDH_mUml7BfuNYjNmEPIgaqXxvd6nR-FTNU5OC5771R2sT_QS9SozEUcY0L8jz3AlIwvYBzhFpfWOc0kNtuD4oeDEeyuDszjjU5yVuwkIrdHN3obgN9NcAgFR5FHpRtMbfajR6gy8azVIlZJTqbm_uB1biIWCrStl4cEgyhxRQ3XqNUnAVdtm3nv4shBPiRZCFTTgd87XkF5l1FHmlyj7S3Ub_HZMxZfp0iLiahhOtDRJzJYTt7Iy0p-kuaKo7T3-2fZdEO-B1wSg7XbXFzQbeNNFswhUkwNXSDhkalyPSOBtMbTID1aIY3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : اسرائیل آمادست، آمریکا هم آمادست، ایران داره با آتیش بازی می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124872" target="_blank">📅 20:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124871">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نتانیاهو : ما با مردم ایران دشمنی نداریم، ما با این آیت‌الله‌ها طرف هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/124871" target="_blank">📅 20:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124870">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
روبیو: گفتگوها با ایران درباره غنی‌سازی اورانیوم و بحث ذخایر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124870" target="_blank">📅 20:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124869">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: رابطه من با نتانیاهو عالی است و در مورد مسئله لبنان بین ما توافق وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124869" target="_blank">📅 20:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124868">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
مقامات اسرائیلی: تخمین زده می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124868" target="_blank">📅 20:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124867">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiPLgWX_HdO8eZGX7OH8Lk3cIbYilaKqqdnEJFmqQFULXCBJ2yUUMyz085F99AMIjc-Yhu_I38PDZvgEUOqBYE7K8gsi0HzaqSzJF41cyn171XdyIOXToVwSZi7NEa6agDkpjn8p39hfCw466MqXzOTC2TtQDp0lV5VlQIUTxpM9Z44h3BURzPeTckuPTp2iG1NgS2sTV3CsBoR4bJ0hkEijww_L54gxnpXn7QpHRhPEe08OhRnO3ZACPHJ9Hmk3JdC10F6_iYV0HY1tlZJDZdy-no-XrDZhiIgLZwmLT7qvsT-uYAdIh-zXoS5DPGG7tVWbTcEWHw-b6Ij3eVk9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری‌ابیانه: نتانیاهو فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد!
🔴
علت جنگ آمریکا علیه ایران این است که نتانیاهو علیه ترامپ آتو دارد و فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد و نتانیاهو این را اهرم فشار علیه ترامپ قرار داده تا هر کاری اسرائیل می‌خواهد، آمریکا انجام دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124867" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124866">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
روبیو: تحریم‌های ایران کاهش نخواهد یافت، مگر اینکه غنی‌سازی اورانیوم و اورانیوم با غنای بالا را کنار بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124866" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124865">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450fe35b73.mp4?token=RTv581s7h3Gh51AR3L7xp5tKIqJuNMgjwFPWZ36J6aQHYsLvUpJdAcUrLKjn8tZusgSaqRBa7MkDiFsTfU_pl4wiyzf_aUQwotwR7yeluoUzQmkwvDg8-J9X7pn8dLR1N0YWxnJDt0EDSxjM-tF148OgdNxmRrtGCVqefdJd0Stnb0_5atXNn6FMg894qGOLOBaG0YGbCuQ_JnmtXdjM-nfRK06YJd9sde3gPHhOfRXpoFiTU4y2CbBWDe7kImsg5Ap4rJDWHl8HOElKkz-L8kGPWfAMY0wUskqbhhZX3VN6RhSMMsREI6p21AYmZ60pwYEFRo8PDPU_xMLwCUFMHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450fe35b73.mp4?token=RTv581s7h3Gh51AR3L7xp5tKIqJuNMgjwFPWZ36J6aQHYsLvUpJdAcUrLKjn8tZusgSaqRBa7MkDiFsTfU_pl4wiyzf_aUQwotwR7yeluoUzQmkwvDg8-J9X7pn8dLR1N0YWxnJDt0EDSxjM-tF148OgdNxmRrtGCVqefdJd0Stnb0_5atXNn6FMg894qGOLOBaG0YGbCuQ_JnmtXdjM-nfRK06YJd9sde3gPHhOfRXpoFiTU4y2CbBWDe7kImsg5Ap4rJDWHl8HOElKkz-L8kGPWfAMY0wUskqbhhZX3VN6RhSMMsREI6p21AYmZ60pwYEFRo8PDPU_xMLwCUFMHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: ما هنوز در ناتو هستیم، اما ناتو به تغییرات قابل توجهی نیاز دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124865" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4735e0d3d0.mp4?token=mEBMGmqB4QhPHPj-W5mJmHtinY6jv0WosCr-TKVVW8OUNsvj_Q0wXz-JGNmepzBWGK60ErVfIkRNOwTLu0qkzyLjcL9G6QZLhuIQHFef68-C5xwNFYtrtXK5OGYVfOSTnjcAkuujBg5wa79TYYxV9_ALUfRZ5nEKnM06EjuFb6bxQaD8EsuNW9xRRzqjX5ci8OMrYmehEeIJF6F3KAF5xw9sIZEJ2Hztz9uzAT_OBPyEC6rp_fvIUceg0cpTZ7HsQ_qwRIVVD7zlRhwgnT2zQxDZPDHLhLPvwBvbuqE8kRKYu7EjV0bVbo7uAADnL3fUYv4ZQOZ6CpZs2MdILY-qFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4735e0d3d0.mp4?token=mEBMGmqB4QhPHPj-W5mJmHtinY6jv0WosCr-TKVVW8OUNsvj_Q0wXz-JGNmepzBWGK60ErVfIkRNOwTLu0qkzyLjcL9G6QZLhuIQHFef68-C5xwNFYtrtXK5OGYVfOSTnjcAkuujBg5wa79TYYxV9_ALUfRZ5nEKnM06EjuFb6bxQaD8EsuNW9xRRzqjX5ci8OMrYmehEeIJF6F3KAF5xw9sIZEJ2Hztz9uzAT_OBPyEC6rp_fvIUceg0cpTZ7HsQ_qwRIVVD7zlRhwgnT2zQxDZPDHLhLPvwBvbuqE8kRKYu7EjV0bVbo7uAADnL3fUYv4ZQOZ6CpZs2MdILY-qFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: خود ترامپ در نشست بعدی ناتو در آنکارا، ترکیه حضور خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124864" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
قالیباف: دوران تهدید بی‌هزینۀ ایران به پایان رسیده و هر تجاوزی با پاسخی پشیمان‌کننده مواجه خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124863" target="_blank">📅 20:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RwdY5cUxynGTfZ4BzG7kn2qyBOipBykB__yOevi-BOVlTmu5h2_SJk-L0TW05GEH_4LLiKC8-0hJz685fdAh1OCKvF7O8LyPcOVHkrmpL2MGZ0P8pLFwcBYpxLnutG2QHPu2WmmdwAbeyNvmgy77qYzU13hgOXX3pd8vAgonODt41b7PfOi4usz2Pn919HRGBXjAfGOenFQwiAw_y4hiI20ZZKFwIbYAdXbYbYFh6JwC9hwb6-jOJpnNk76188nkPpONV87Wl87fIep3FRVWDKrAnWu_g-b_8qKhJaVyDL1pykkqXxEOg79smsJJkUkrHKJOS5GI3VmgOKmeWL033Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار غلامرضا جلالی رئیس سازمان پدافند غیرعامل: علی‌رغم همه انتقادها، برخی از اسرار کشور را افشا نمی‌کنیم، چون اطلاع‌رسانی عمومی در برخی موارد می‌تواند موجب ترس و نگرانی در جامعه شود
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124862" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل: هیچ برنامه‌ای برای آتش‌بس در جبهه لبنان وجود ندارد و عملیات تهاجمی ادامه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124861" target="_blank">📅 20:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر صنعت : با دستور مستقیم رئیس‌جمهور، تمامی موانعی که منجر به توقف خطوط تولید یا معطلی مواد اولیه در بنادر می‌شود، می‌بایست برطرف شود.
🔴
امروز نیز خط تولید، خط مقدم دفاعی ماست.
🔴
مسائل و نگرانی‌های موجود در حوزه تامین مواد اولیه و واردات با همکاری تیم اقتصادی دولت در حال تسریع است و اجازه نخواهیم داد چرخ تولید متوقف شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124860" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
روسیه: مذاکرات ایران و آمریکا باید به ثبات پایدار در خاورمیانه منجر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124859" target="_blank">📅 20:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124858">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
به گفته برخی منابع: تصاویر ماهواره‌ای جدید نشان می‌دهد که در پایگاه آمریکایی «علی‌ السالم» در کویت، یک آشیانه پهپاد یا هواپیما تخریب شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124858" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf324326a7.mp4?token=Bfh78W6_vFYubqMDqs0A9iX4s81vobu5xpdC5FZ7o12tB7hMZR0k9GmqeBVlKGPNqvAovshuNTVo51J2gltknwKj5o8VPgeeY7-qvYtIsqM4In4lBRixQ9plUISMOcgYZ4AnlGIZKSAEms0CYvCDDHGPeS2iP6xo_E_KqEl9iJtdB2rKnNA1dWd9zkY0MxaohWtmDRofr0V_ysBBTZ4hmlb_cJgJPfjBmYSwJkKOaRT6Z6SekaLXhX8dANVmzZhuZQzkeYDilEL_bHyiccAPWAAe1j-opYTvaEVQynqCwRpBy9U0_t_BPn9BB47awTeXqFa93sVmbkdTy9gDZ4QdJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf324326a7.mp4?token=Bfh78W6_vFYubqMDqs0A9iX4s81vobu5xpdC5FZ7o12tB7hMZR0k9GmqeBVlKGPNqvAovshuNTVo51J2gltknwKj5o8VPgeeY7-qvYtIsqM4In4lBRixQ9plUISMOcgYZ4AnlGIZKSAEms0CYvCDDHGPeS2iP6xo_E_KqEl9iJtdB2rKnNA1dWd9zkY0MxaohWtmDRofr0V_ysBBTZ4hmlb_cJgJPfjBmYSwJkKOaRT6Z6SekaLXhX8dANVmzZhuZQzkeYDilEL_bHyiccAPWAAe1j-opYTvaEVQynqCwRpBy9U0_t_BPn9BB47awTeXqFa93sVmbkdTy9gDZ4QdJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله فیلمی منتشر کرد که نشان می‌دهد یک پهپاد FPV مجهز به دوربین حرارتی، یک خودروی زرهی نامر ارتش اسرائیل را در حومه جنوبی یحمور الشقیف در جنوب لبنان دیروز هدف قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124857" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124856">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی در گفت‌وگو با شبکه اسکای‌نیوز با بیان اینکه از موقعیت مکانی ذخایر اورانیوم غنی‌شده ایران که در جنگ  سال گذشته هدف حمله قرار گرفت، مطلع است.
🔴
او ادعا کرد که این مواد همچنان در همان محل پیشین قرار دارد اما دسترسی به آن به‌دلیل خسارت‌های فیزیکی دشوار شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124856" target="_blank">📅 20:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124855">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فارس: تاریخ برگزاری آئین وداع، تشییع و خاکسپاری رهبر اعلام شد
🔴
۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی
🔴
۲۳ خرداد/ تشییع در تهران
🔴
۲۴ خرداد/ تشییع در قم
🔴
۲۵ خرداد/ تشییع در عراق
🔴
۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124855" target="_blank">📅 19:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124854">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فارس: تاریخ برگزاری آئین وداع، تشییع و خاکسپاری رهبر اعلام شد
🔴
۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی
🔴
۲۳ خرداد/ تشییع در تهران
🔴
۲۴ خرداد/ تشییع در قم
🔴
۲۵ خرداد/ تشییع در عراق
🔴
۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124854" target="_blank">📅 19:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124853">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: هیچ پاداشی در ازای امضای توافق به ایران ارائه نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124853" target="_blank">📅 19:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124852">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea964f03e.mp4?token=llQCMWho2_baxkPfK1wVZhc-XclJeJFJT_U7caAgmBOFUC00QGoON29YrLFl7mEsW0AJl-sm26I_oPCdTSh98t6-GAIvHsfozI5pQ61R4IaQgbOPAIvlLvzzxoVMOuoHKOTX9krPisb1BPYZKY7pNVfzuAj5xQmohDa8kCf_VIooSs97TB2oEWQiCLaI7LGmiZ-j8nX4kXm3G9nSvr99NQ2ycIA7JQD-St9C0-K8mhC-34smUY3y47V7LPU01qIfbnEfjtoy1fruKoQoMYSK2n0hupJgZTEYkTbGhPvmzmDrKGt9CocNlrSXzt5NEnCdEcIfBwUtkP7-gHzllbE6Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea964f03e.mp4?token=llQCMWho2_baxkPfK1wVZhc-XclJeJFJT_U7caAgmBOFUC00QGoON29YrLFl7mEsW0AJl-sm26I_oPCdTSh98t6-GAIvHsfozI5pQ61R4IaQgbOPAIvlLvzzxoVMOuoHKOTX9krPisb1BPYZKY7pNVfzuAj5xQmohDa8kCf_VIooSs97TB2oEWQiCLaI7LGmiZ-j8nX4kXm3G9nSvr99NQ2ycIA7JQD-St9C0-K8mhC-34smUY3y47V7LPU01qIfbnEfjtoy1fruKoQoMYSK2n0hupJgZTEYkTbGhPvmzmDrKGt9CocNlrSXzt5NEnCdEcIfBwUtkP7-gHzllbE6Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقال گسترده تجهیزات و جنگنده‌ها از طریق اروپا به سمت خاورمیانه ادامه دارد و ظرفیت نظامی در حال افزایش است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124852" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124851">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHQzz_K5DPgQELPsKFgu3zJiRgtT_sZZiJoNxJQduRRvfnCwb9Yq8elm6CPyNIwQ-UPPSv3cukGsBaDdoh9_6bQAugg5UDybi0T3vrYOGcb6suFog7x5SizvbsnS61GjJYPDUZW0kcLlOYYuFqDo5_zFbgzisZ5VZkVPsP6m7mLRUnHseEx-UrpnN_9PvXtiw-GG78ETMYfeRKWrDqPpwl_F1O4l_v4w6JtyHmPB76jin6wSGU2WAfRimHraFV6wUFBm9ybwSl7X5cgIYMyGeIWwfbe8qbTiAJG2-owfyy7bdLRRXcm1wi_HAUF9lGuD0q3Tl5JBLr4ElmRyetY0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثروتمندان فوق‌ثروتمند جهان کجا بیشتر می‌شوند؟ / آمریکا اول، چین دوم
پیش‌بینی می‌شود بین سال‌های ۲۰۲۱ تا ۲۰۲۶:
🔴
آمریکا حدود ۶۷ هزار نفر به جمعیت ثروتمندان فوق‌ثروتمند (دارایی خالص بیش از ۳۰ میلیون دلار) اضافه کند که بیش از هر کشور دیگری است.
🔴
چین در رتبه دوم قرار دارد.
🔴
هند هم از نظر تعداد و هم نرخ رشد در میان کشورهای بالای جدول است.
🔴
لهستان، قطر و ترکیه سریع‌ترین رشد درصدی را تجربه می‌کنند و جمعیت ثروتمندان فوق‌ثروتمند آنها بیش از دو برابر خواهد شد.
🔴
این روند نشان می‌دهد که خلق ثروت به‌تدریج از مراکز مالی سنتی فراتر رفته و به اقتصادهای نوظهور و در حال توسعه سریع گسترش می‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/124851" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124850">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس: توقف جنگ در تمام جبهه‌ها در صدر متن توافق ما با آمریکاست
🔴
اجازه نخواهیم داد آمریکا و اسرائیل خدشه‌ای بر اتحاد مقاومت و ایران اسلامی وارد کنند.
🔴
به پیروزی مقاومت معتقدیم و ایمان داریم با فهم مشترک و تلاش هدف نهایی که همان نابودی اسراییل است، محقق می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124850" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124848">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBZP1d20ZjYg2zaj8VXKd5bIeFXYxODRlPk8UEhqov78wCrxQjNziAdYHiySu1Dq4RVjks_D-UgebKXLaFfY69qLoT5WSZPDtWQsiR-gwzBJGeigH2l-ZkMi4Euxhz7nvauHI6cE_fi2CAFgyY4rF20KKD6wzT6PpIzDwmSC5ltPgEdXWlWYZ26ZakllAGwE1TSLlqG20RWIxVVCX9-LH6VYUjSJ6aswIIaWvfoGGSJ0oDtEekXgQHUUn2bQCSBrS9WxsojpKVymeZQk4Xq7B9-EYZAnuZ0W6apLsOTT9B3gRXTvT1kDPFh_Or6MZRnsJ64_zFvxQxIEXKNCq12Q5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23753c660.mp4?token=IhIs_1pke82LDOMJSlr1Zwuoe2bgVBQf0wZh7bQXtfghCTuNvNQVgIiHt6wxFIy7djqA_UEMEy7hn14O0Mho4Uj1rDMwPeocvgmKUOoRin9zRJgonY5Oz_yJrWaqc7PKaOVyXFPHslPfAZf0eJ6NDI2MF7hnxITMD0u6C4SSku-bCad7JBr3mt9lnpRFpYTy68unGc9-S68uCKBCeXeLZQN1KvlIZWVbc34umL-9iDbC5f9ArVNLkcmBAfaop7Cg8BvVSCapoWO9WAvIo5B_IqyQe2_sAM_mMYr2BBpcaAF1894dkMR0v4yUCNQpinTkeJkUIeDDq7W50xoiKKbDuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23753c660.mp4?token=IhIs_1pke82LDOMJSlr1Zwuoe2bgVBQf0wZh7bQXtfghCTuNvNQVgIiHt6wxFIy7djqA_UEMEy7hn14O0Mho4Uj1rDMwPeocvgmKUOoRin9zRJgonY5Oz_yJrWaqc7PKaOVyXFPHslPfAZf0eJ6NDI2MF7hnxITMD0u6C4SSku-bCad7JBr3mt9lnpRFpYTy68unGc9-S68uCKBCeXeLZQN1KvlIZWVbc34umL-9iDbC5f9ArVNLkcmBAfaop7Cg8BvVSCapoWO9WAvIo5B_IqyQe2_sAM_mMYr2BBpcaAF1894dkMR0v4yUCNQpinTkeJkUIeDDq7W50xoiKKbDuYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام محمد جعفرپور 25 ساله
🔴
محمد به تمام آرزوهاش رسید، حتی به آخریش.
🔴
خط آخر: «من فدای ایرانم و تا توان دارم به ایران و ایرانی خدمت می‌کنم»
🤔
عرزشی حرام زاده با قتل عام کردن مردم عدالت علی رو میخواستی به نمایش بزاری؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124848" target="_blank">📅 19:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124847">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
واکنش چین به تهدید تعرفه‌ای ترامپ:
جنگ تعرفه‌ای و جنگ تجاری به سود هیچ طرفی نیست
🔴
سخنگوی وزارت امور خارجه چین به گزارش‌هایی درباره پیشنهاد دونالد ترامپ رئیس‌جمهوری آمریکا برای اعمال تعرفه‌های اضافی ۱۰ تا ۱۲.۵ درصدی بر کالاهای وارداتی از ۶۰ اقتصاد از جمله چین واکنش نشان داد و گفت: پکن همواره با تمامی اقدامات تعرفه‌ای یکجانبه مخالف بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124847" target="_blank">📅 19:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124846">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت کشور بحرین: ۱۵ نفر عوامل مرتبط با سپاه بازداشت شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/124846" target="_blank">📅 19:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124845">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e58f8442.mp4?token=uVCx3pNunqZJm6Pk8KoGu6MVI8uAwf6mKQ-AttZqQ4nMWaE_7p8OmxIvLxqI5G9h9TDQk9jRCPUtijcZRgUbfK6kaZnu7quib4a_aLb5HLQYQRBLBTyZTLxakypTD2W_fEnwphjTcvCvtyLpbqwwG9WCcfR12CnXkGsi5eOTkDhR1vZBUxoP6TBp4nYCUFoPI_OJWk8vi4VbTiNYevvgyMuIDwOwr_XcbbqItXDOsBszoIZQK9L9Ehrygc2zJ-2GpXVBCMBWTcGsPh0hVXHqnirpql1Ok5wZ29afJBhMPCfOV6WQb4iqQ-ZlnFcdZLDSE3asKI5KtjzOpYAE5BK7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e58f8442.mp4?token=uVCx3pNunqZJm6Pk8KoGu6MVI8uAwf6mKQ-AttZqQ4nMWaE_7p8OmxIvLxqI5G9h9TDQk9jRCPUtijcZRgUbfK6kaZnu7quib4a_aLb5HLQYQRBLBTyZTLxakypTD2W_fEnwphjTcvCvtyLpbqwwG9WCcfR12CnXkGsi5eOTkDhR1vZBUxoP6TBp4nYCUFoPI_OJWk8vi4VbTiNYevvgyMuIDwOwr_XcbbqItXDOsBszoIZQK9L9Ehrygc2zJ-2GpXVBCMBWTcGsPh0hVXHqnirpql1Ok5wZ29afJBhMPCfOV6WQb4iqQ-ZlnFcdZLDSE3asKI5KtjzOpYAE5BK7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیم جونگ اون رهبر کره شمالی با تیم فوتبال زنان ناگوهیانگ ، اولین تیم از کره شمالی که قهرمان لیگ قهرمانان زنان آسیا شد دیدار کرد
🔴
واکنش اعضای تیم بعد از دیدن رهبرشون دیدنیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124845" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124844">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb8a354c14.mp4?token=HVOioWhrz6xGgHtSAG0ocq5_2geaAtflKR4rLWPefLnkS1T_LhAI_r_L1KvtZeR_iFWnGRuR8QJ0l6753chIWDUQYGJYvosIRz5W6KpsA-LWKyy8hAsvfDIj1tz35OjMzbnARRP-S6ZszO7n55E-ydTcbFQMB67GLZ0hicf-0rTFZVuFoNh4gxXquFl362C1QptFQA6N2cn93LG5P09N70uF2tECiE-9umb3pFHn0g-X2QI4lYqy_Gn-vLAigz5GnVMjaDKc_Q0V9jbwHIqczOiqELfTe_tCseWPydg1BamaeEPeAmMT8MruGIH9U4pCJ9zUZw28IYgCGR3dF83abA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb8a354c14.mp4?token=HVOioWhrz6xGgHtSAG0ocq5_2geaAtflKR4rLWPefLnkS1T_LhAI_r_L1KvtZeR_iFWnGRuR8QJ0l6753chIWDUQYGJYvosIRz5W6KpsA-LWKyy8hAsvfDIj1tz35OjMzbnARRP-S6ZszO7n55E-ydTcbFQMB67GLZ0hicf-0rTFZVuFoNh4gxXquFl362C1QptFQA6N2cn93LG5P09N70uF2tECiE-9umb3pFHn0g-X2QI4lYqy_Gn-vLAigz5GnVMjaDKc_Q0V9jbwHIqczOiqELfTe_tCseWPydg1BamaeEPeAmMT8MruGIH9U4pCJ9zUZw28IYgCGR3dF83abA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله فیلمی منتشر کرد که یک پهپاد FPV مجهز به دوربین حرارتی را نشان می‌دهد که دیروز گروهی از سربازان ارتش اسرائیل را در حومه زوطر الشرقیه در جنوب لبنان هدف قرار داد.
🔴
پهپاد FPV مستقیماً به صورت یکی از سربازان ارتش اسرائیل اصابت کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/124844" target="_blank">📅 19:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124843">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5578c6acc5.mp4?token=tEnCMSQ1nI1Rf-l_X2huZsLvK4L-QhBfOu9z7FpEKvMBs96lKpZtsTvQcihgm_PZhAt3E-cCnFu4KnMNidRKT4b9Tp1W09pQP8-YiJ6HTBmP5xV28Em6EbHZNyBiijNGBHwXntsDeD_WIu3mR07GfymE20dWYARB0kBOxvsnkx6jsZX9TDjYZy_hVGwiKt1jmApUgr_dTwILAmWWRYdQVU5ONbxfuYBsWl8MG13mt0ODrci3lZGjHwNPtimUaRKFS9UDwrfA_fJE_Wp94OmkiWNIL5GiPymSzzL7qe1tgyrzD_BhksV3tplaC5hBov9shCAulLWt8ObvHhOy4Cl3jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5578c6acc5.mp4?token=tEnCMSQ1nI1Rf-l_X2huZsLvK4L-QhBfOu9z7FpEKvMBs96lKpZtsTvQcihgm_PZhAt3E-cCnFu4KnMNidRKT4b9Tp1W09pQP8-YiJ6HTBmP5xV28Em6EbHZNyBiijNGBHwXntsDeD_WIu3mR07GfymE20dWYARB0kBOxvsnkx6jsZX9TDjYZy_hVGwiKt1jmApUgr_dTwILAmWWRYdQVU5ONbxfuYBsWl8MG13mt0ODrci3lZGjHwNPtimUaRKFS9UDwrfA_fJE_Wp94OmkiWNIL5GiPymSzzL7qe1tgyrzD_BhksV3tplaC5hBov9shCAulLWt8ObvHhOy4Cl3jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جیک سالیوان، مشاور امنیت ملی پیشین آمریکا: توافق هسته‌ای بسیار شبیه توافقی خواهد بود که اوباما، جان کری، وندی شرمن و افرادی مثل من سال‌ها پیش مذاکره کردند، اما ترامپ از آن خارج شد.
🔴
ما به چیزی شبیه آن بازخواهیم گشت، در حالی که همه این هزینه‌ها را پرداخته‌ایم، در حالی که اصلا نیازی به خروج از آن توافق در وهله اول نبود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/124843" target="_blank">📅 19:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124842">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
الجزیره: ۲۴ ساعت آینده برای «آتش‌بس» اسمی در لبنان حیاتی خواهد بود
🔴
به گفته منابع سیاسی در بیروت، این ۲۴ ساعت بسیار حیاتی خواهد بود و در عین حال، ممکن است بسیار خطرناک نیز باشد، با توجه به این واقعیت که مذاکرات در بیش از یک مکان در حال انجام است.
🔴
چیزی در واشنگتن و همچنین در قطر در جریان است و تلاش‌هایی برای رسیدن به یک آتش‌بس جامع در لبنان صورت می‌گیرد
🔴
آنچه در ساعات گذشته شاهد بوده‌ایم، تشدید تنش بوده است. حمله به یک خودرو در جاده اصلی بین جنوب و بیروت، بسیار نزدیک به بیروت، در منطقهٔ خلده، و پاسخ حزب‌الله با ارسال پهپاد و سپس موشک به سمت شهرک‌ها و شهرهای شمالی اسرائیل.
🔴
این ما را به نقطهٔ اول بازمی‌گرداند، جایی که قبلاً در آن بودیم؛ هیچ چیز واقعاً در حال تغییر نیست، بلکه فقط بر تشدید تنش افزوده می‌شود.
🔴
حملات به چندین شهر و منطقه، به‌ویژه هشدارها به ساکنان الخرایب، که در شمال رودخانه لیتانی قرار دارد، بر این واقعیت تأکید دارد که اسرائیل می‌خواهد مردم جنوب لبنان به سمت رودخانه زهرانی حرکت کنند، رودخانه‌ای موازی در فاصلهٔ حدود ۲۰ کیلومتری از پیرامون خطی که (اسرائیل) در گذشته تعیین کرده بود (که به اصطلاح منطقهٔ حائل مرزی خود را مشخص می‌کرد).
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/124842" target="_blank">📅 19:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124841">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عراقچی: هرگونه اقدام خصمانه با پاسخی فوری و قاطع مواجه خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124841" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124840">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نتانیاهو : با هم انجام دادیم، تو نزدیکی و همکاری‌ای که قبلاً هرگز نداشتیم
🔴
باید دوباره بگم، رئیس‌جمهور ترامپ بهترین دوست اسرائیل بوده که تا حالا داشتیم؛
🔴
هیچ‌وقت چنین دوستی تو کاخ سفید نداشتیم، او از همه جلو زده، و این شراکت خیلی قوی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124840" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124839">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
این فقط بخشی از جنایت حکومت در 18 و 19 دی هستش.
🔴
هرکدام از این جاویدنام ها عزیز یک خانواده هستن.
🤔
عرزشی حرام زاده از عدل علی بگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124839" target="_blank">📅 19:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124838">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
فارس: تاریخ برگزاری آئین وداع، تشییع و خاکسپاری آیت الله خامنه ای اعلام شد
🔴
۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی
🔴
۲۳ خرداد/ تشییع در تهران
🔴
۲۴ خرداد/ تشییع در قم
🔴
۲۵ خرداد/ تشییع در عراق
🔴
۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124838" target="_blank">📅 19:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124837">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نتانیاهو : نباید ایران تهدیدی برای اسرائیل، خاورمیانه و آمریکا نباشه؛
🔴
سلاح هسته‌ای نسازه و ابزار حمل اون رو هم نداشته باشه؛
🔴
نه فقط علیه اسرائیل یا پایتخت‌های اروپا، بلکه علیه شهرهای آمریکا هم
🔴
این هدف مشترک ماست، برای همین وارد این مسیر شدیم. همچنین می‌خوایم دایره صلح رو گسترش بدیم؛
🔴
همون‌طور که من و رئیس‌جمهور با هم در چارچوب توافق‌های ابراهیم انجام دادیم.
🔴
پس هدف مشترک داریم. گاهی هم، مثل هر خانواده‌ای، روی تاکتیک‌ها اختلاف‌نظر پیش میاد. اما همیشه راهی برای حلش پیدا می‌کنیم
🔴
ما به‌عنوان دوستان نزدیک این کار رو انجام می‌دیم؛ ممکنه صبح با هم اختلاف داشته باشیم، ولی عصر به یک اقدام مشترک برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124837" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124836">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الجزیره به نقل از رئیس ستاد کل ارتش اسرائیل: آماده‌ایم فوراً به جنگ علیه ایران بازگردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124836" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cwl9fYIAKaJXf66nGY9qaXvQ_v4Qi62TmvcXylkBqlC9t2j3WFtKx7KkUcnhPIE7ITEBwVp9b6tkdV5bwASAkIIvW9TVxZu-qMgWxMLkn17AEcHh9vV550qLw4ifEU9FGtZuVR5kdopP_iwvibLKwFm0nR1lk1utrKRz39-IikvJ9wMfvHE7aD59nF_DFMyaeA85e8FBhsQ8tw9V6QmEEL16FBFMnQ2J3U7IU3Jddo0DsuGYRCWnyCuv7u1HvvCX_yy57tVt4PmOfH9BNkJqu2uh1eX2FztNcfrjkY8PFrx2C6pVHqf7vWVo_ZpxfzaIkEYJYfM1h_GycAaf298c6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbV8Ur37-Fz0R64in0E-P376ShkCXeMLYfvfVcga3Eb41P2M2Z8aBqOg2fL7yodzi3Wfq8HkXIebK-OFn1IFEVqtSrzO44y9AVttvnc__b0kYc8OvoOM2YWDaW3W4fCvdqLBuNd3kIx2zEoWXCBeEhx9iwp_qlIbo91Bh-xOn_eiZWhNG69QrfYfAPsBvYv6UCbAJIRfzqvFKulQNc2ot0pXzuYaYa9_7AqazYwfLBCwWXdITp3KyiwNNKTZOxSy1XI4QqcUq-_yf0nNnafoGeLKL6v5P8nTboHGdFYen_W9e1dXmwBSzY0IpO_7FmTmMHDZoA--0NHRgbM2ANwppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEdDQRYJuFSaRg9GxB8--z_rc28YYLtellJxF5yFdyOf9iq7hfoV567cqpD2zIsA0YmfF3SiZMbnn6IbDpXHEIc_WA-IRZPnq1w5vYuLkq7CUieEmXKFDM8D153L6q33jNuQ5HHtO1PjRh2kb3b3k1YDH8-dUonjCCrv0TiJ1v0GdhSGQlZrzaKfxYGDICDP2B-xjQDlj3XfotzAmpWvuEC1-4ME0fYugCgFX5K0nkoLt8wm0f2FoZegSS8TaB7ImqbdAiDmNy9ko3m667y6wH1BzRbPmW2IVGzclcNAZfG0Rt3rI0tHz2AB3RP2iJ2aQxg2D5WFDD20JjXOAC7Q2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیل ساعاتی پیش مناطق «باریش»، «تولین»، «الطویری»، «صریفـا» و «الحنیه» در جنوب لبنان را هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124833" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
زلنسکی: من آمادهٔ مذاکرات مستقیم با پوتین برای پایان دادن به این جنگ هستم، نه اینکه در صف بمانم تا همهٔ درگیری‌های جهان تمام شود و بعد نوبت ما برسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/124832" target="_blank">📅 19:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1ca0ddb0.mp4?token=If74748DqvoFFQjdrFDziyQvZUev_uqn_MGqTWFi5WDyCehCrB5C0-fwZpUneeyX4OycDCQtjgT_GgrBvyX0q4ZT2rjLxM9fr59Ut1GuA45M_Vp194fxpp-0Jd8syfrMZgS363X9A6vK4CfnSbR8uH_EYjEL4QJ3Ri5xYfbPGE6FfNUH9NopLlxpDolnDdTLiFR4EStUyX2EmGXVd1mKWCEbRwkV9N_ezn_mV-DwMJwLN8BVKxirERAIKHYChxUkZTWvMjhNnQAaZBxOQ5ZtEPMO5hUWNJH758NVHaO92g-vaQ76d-R0bA7kb8nvuo_H8A9vvK_OC_5nIGnUXWdotA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1ca0ddb0.mp4?token=If74748DqvoFFQjdrFDziyQvZUev_uqn_MGqTWFi5WDyCehCrB5C0-fwZpUneeyX4OycDCQtjgT_GgrBvyX0q4ZT2rjLxM9fr59Ut1GuA45M_Vp194fxpp-0Jd8syfrMZgS363X9A6vK4CfnSbR8uH_EYjEL4QJ3Ri5xYfbPGE6FfNUH9NopLlxpDolnDdTLiFR4EStUyX2EmGXVd1mKWCEbRwkV9N_ezn_mV-DwMJwLN8BVKxirERAIKHYChxUkZTWvMjhNnQAaZBxOQ5ZtEPMO5hUWNJH758NVHaO92g-vaQ76d-R0bA7kb8nvuo_H8A9vvK_OC_5nIGnUXWdotA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی:من هر روز برنامه سفر پوتین را دنبال نمی‌کنم.
🔴
ما فقط به حمله به اوکراین پاسخ می‌دهیم.
🔴
فکر می‌کنم حملات ما موجه است.
آنها باید بفهمند که اگر به استفاده از پهپادها و موشک‌ها علیه ما ادامه دهند، ما نیز همین کار را خواهیم کرد.
🔴
اما ما فقط به پالایشگاه‌های نفت یا اهداف نظامی موجه پاسخ می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124831" target="_blank">📅 19:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نتانیاهو در مورد توافق هسته‌ای اوباما با ایران: ما به ایران یک ماه مهلت دادیم قبل از بازرسی‌ها. آن‌ها تمام مواد هسته‌ای را خارج کردند، تأسیسات هسته‌ای را تخلیه کردند و همه چیز را به جای دیگری منتقل کردند.
🔴
آیا فکر می‌کنید این یک رژیم بازرسی خوب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124830" target="_blank">📅 19:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb62a290a.mp4?token=um_-RoLkbpXktt_76D-TEWezw9JH6H9AHBX7N_Rs81Yk0Z4WlGfiDu9FrylyzSvbPnQMNqjqqwc-9pcro3f3v8qSMA9t4th-3k7VZUNoNINNPf0ihX1UcBNcsr73_H-D3nFlFfaN4vek2ZjVjL_Zqu-2oedxKP5w2VfSuE8GfyDeAx-zEcTywgo_T1A3s4fB5ssozEMbpntKXt4w7MWZ-4G_C-jv8qWSQzqGAtDdJnBFug_lXBk2gUEBcaPxYazuVSXh5T3i1jfCXXJtl30ByhR3Z8NxAlXA_BxI45PHWcrkkSIJ2-KHDAPv41wp4sSWXFC31GZvrj42oPQGK8ZaEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb62a290a.mp4?token=um_-RoLkbpXktt_76D-TEWezw9JH6H9AHBX7N_Rs81Yk0Z4WlGfiDu9FrylyzSvbPnQMNqjqqwc-9pcro3f3v8qSMA9t4th-3k7VZUNoNINNPf0ihX1UcBNcsr73_H-D3nFlFfaN4vek2ZjVjL_Zqu-2oedxKP5w2VfSuE8GfyDeAx-zEcTywgo_T1A3s4fB5ssozEMbpntKXt4w7MWZ-4G_C-jv8qWSQzqGAtDdJnBFug_lXBk2gUEBcaPxYazuVSXh5T3i1jfCXXJtl30ByhR3Z8NxAlXA_BxI45PHWcrkkSIJ2-KHDAPv41wp4sSWXFC31GZvrj42oPQGK8ZaEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تیم غیر ملی جمهوری اسلامی
🤔
شما هیچوقت از مردم نبودین و نیستین بی غیرت ها
@AloSport</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124829" target="_blank">📅 19:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مرکز فرماندهی مرکزی ایالات متحده می‌گوید نیروهای آمریکایی ۱۲۵ کشتی تجاری را بازگردانده و از ۱۳ آوریل، آغاز محاصره بنادر ایران، ۶ کشتی را متوقف کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124828" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9cdc097f8.mp4?token=UZssD4V8LawWf90e95tBVXFS8loi8kHfYKRImz1mcDnYhn8N-E6isyDJ7I8W2emYCokF_Gr5EHxR1LawCE_VbiP-RVKQfAlTlSVHwn_CBay3DsgPj7wHm5RY8FYqXdYgH0E9HQ_ofsMaiSxPpxDO3EbLtGhof0TLVBJL-qcu1sXjgiuYokrUaOYZaK1fby2gW6NuKHHNulpxiq03bgnVfR04I3hb1LKbKuLPvvEn9Jq4-ofSAsZQJmd7cczhkfIGnHNDhp1hXaXMoZLg8QauhgPJMrCZWYuwdP45u_BinrGxoyzLHNy5pNLnBODPbdxCotAoSsk4IRIpUt-3yAFyWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9cdc097f8.mp4?token=UZssD4V8LawWf90e95tBVXFS8loi8kHfYKRImz1mcDnYhn8N-E6isyDJ7I8W2emYCokF_Gr5EHxR1LawCE_VbiP-RVKQfAlTlSVHwn_CBay3DsgPj7wHm5RY8FYqXdYgH0E9HQ_ofsMaiSxPpxDO3EbLtGhof0TLVBJL-qcu1sXjgiuYokrUaOYZaK1fby2gW6NuKHHNulpxiq03bgnVfR04I3hb1LKbKuLPvvEn9Jq4-ofSAsZQJmd7cczhkfIGnHNDhp1hXaXMoZLg8QauhgPJMrCZWYuwdP45u_BinrGxoyzLHNy5pNLnBODPbdxCotAoSsk4IRIpUt-3yAFyWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران اگه توافق ۲ روز دیگه ادامه داشته باشه:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124827" target="_blank">📅 19:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نتانیاهو: مردم در حال توسعه منابع جایگزین هستند و در حال حاضر در حال توسعه مسیرهای جایگزین هستند.
🔴
به جای تمام انرژی‌ای که از خلیج فارس عبور می‌کند، مسیرهای دیگری وجود خواهد داشت.
🔴
بنابراین به جای تمام انرژی‌ای که از خلیج فارس عبور می‌کند، همچنین از طریق عربستان سعودی به دریای سرخ عبور خواهد کرد. و فرصت‌های دیگری نیز وجود خواهد داشت. می‌توانیم آن‌ها را مستقیماً به مدیترانه ببریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124826" target="_blank">📅 19:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نتانیاهو: هدف و خواسته ما سرنگونی جمهوری اسلامی است اما به صرف انتخاب و خواست ما این اتفاق نمی افتد و ما تلاش داریم مردم ایران را کمک کنیم تا خودشان این کار را بکنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/124825" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
✅
⭐️
فقط گیگی 8 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/124824" target="_blank">📅 18:54 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
