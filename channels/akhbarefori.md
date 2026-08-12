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
<img src="https://cdn4.telesco.pe/file/ijZjUCWOaUGUBrkIKEiBM-LB4InkCqHDMKWELpCmjfsxy8JxFwUGFngdG57_LyIojg-36d2Yw8HLDSX-KUJGfui_uvvgfNtXP_VBQmtISnAj81pi6z7Qozoiyw94bibFykJCTKqqJkHu65CJaXYFNoKgXd6cI_pPbvCLfPCO7_DjjUbla6uEe9qf-1006_dBPf7LCYzCSBXa70oB4rymLwaBjQqNNcSl3-aDmeNwJg-3aIOMAs96Un5AgIZUxgh3Zo1TGDxLERCTJI7_TYhKnmxqooRba0HBh5I_xXJFFtKH6coKxR_OOsSDYztMuWob3J1IfDWg_mLTnUCV30Ew-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 14:22:24</div>
<hr>

<div class="tg-post" id="msg-680569">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
پزشکیان: ایران به هیچ وجه خارج از قوانین بین‌المللی عمل نکرده است
رئیس جمهور در گفت‌وگوی تلفنی با نخست‌وزیر ژاپن:
🔹
ایران به هیچ وجه دنبال ناآرامی در منطقه نبوده است.
🔹
آمریکا و رژیم صهیونیستی با تجاوز  به ایران و ترور رهبرانقلاب و شهادت جمع کثیری از غیر نظامیان از جمله دانش آموزان میناب و تخریب زیرساختهای غیر نظامی موجب بر هم زدن صلح و ثبات در منطقه شده اند.
🔹
امیدوارم تلاش‌های دیپلماتیک ژاپن برای برقراری صلح و ثبات در منطقه ثمر بخش باشد
سانائه تاکایچی:
🔹
توکیو از روشهای دیپلماتیک برای پایان جنگ حمایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/akhbarefori/680569" target="_blank">📅 14:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680568">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVFsmsLOouKclHkASfk4o1-_bxTVpWmLGLInbTrlIe_VKKJXweOOR892fJ-LuDPSalbOatxghNP91vt2HYjGZm4fkiv7IVL4RBaG5T36MKHpJfr-cE8jmBII4wWT6PoGyLr13FefmDfNggfhlxVzMH6aEMipfT2XwGV9xTqCr_BOYl3ooajKsKm5PD2fSrlrD5FXdtqsvH27PW7YdO0IElEpNM3KHRzTVA_RE6vUd4y02wX_T3RAHWf-gzOTbUwM1XyIBxL2lHrBmYVdR9u4eObMQN79FtvRQB6FvI2mE7n2t9YAiqazUmTK0g5z_zp7QySRoFAIV15wUZCHb62maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قوی‌ترین پاسپورت‌های جهان
🔹
سنگاپور، کره‌جنوبی و ژاپن دارای قوی‌ترین پاسپورت‌ها
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/680568" target="_blank">📅 14:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680567">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd389e9e9.mp4?token=lQNx0K4uYQz51j29czRlRQkS1Cm4BJepnWSHfa8JbszbUuQQ3HBHAv82mYhca_lod-JM87VAvj4iyXaoh7ZpgHP286sOI_RvJVy5L9Bxj7fWgj8yNGSDiVTn1pjT2qBhxJ9aRqumtWsfYz7z4mDmHGM9f9NMA6GxJIyMXL8UuTFwkkJrJvezfoNd-In3iWWCIDABBH4jH7u_ifzaXGlzWBknwK3D7MQav19yw68Wpf3aKL4SxD3bgUuB41dzQob_YPT1qXurK7unLH5OscKEQhbKRf0kPggxOys1B4iAPsQ79mNWVfwa_S9opeAuUMsQDU3z25WTHcyjYR5KmtlCwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd389e9e9.mp4?token=lQNx0K4uYQz51j29czRlRQkS1Cm4BJepnWSHfa8JbszbUuQQ3HBHAv82mYhca_lod-JM87VAvj4iyXaoh7ZpgHP286sOI_RvJVy5L9Bxj7fWgj8yNGSDiVTn1pjT2qBhxJ9aRqumtWsfYz7z4mDmHGM9f9NMA6GxJIyMXL8UuTFwkkJrJvezfoNd-In3iWWCIDABBH4jH7u_ifzaXGlzWBknwK3D7MQav19yw68Wpf3aKL4SxD3bgUuB41dzQob_YPT1qXurK7unLH5OscKEQhbKRf0kPggxOys1B4iAPsQ79mNWVfwa_S9opeAuUMsQDU3z25WTHcyjYR5KmtlCwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجموعه میم‌های وایرال شده کاربران خارجی از پنهان شدن ترامپ در خودروی آشغال غذا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/680567" target="_blank">📅 14:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680566">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ونهم از فصل پنجم
🔹
در این قسمت دومین تجربه‌ نزدیک به مرگ آقای سید محمد موسوی که هم زمان با جدایی روح از تن مادر در حین عمل جراحی، روح ایشان نیز بخاطر ناراحتی قلبی جدا شده و تجربه مشترکی با مادر در عبور از رودخانه‌ای طغیانگر را درک می‌کند و بخاطر نگاه به نامحرم و دروغ، خود را در طبقه‌ای از جهنم که شادمانی شیطان بزرگ‌ترین عذاب بوده است، می‌بیند اما بخاطر آبروداری فردی گناهکار در دنیا از این طبقه رهایی می‌یابد را در این قسمت و ادامه ماجرا را در قسمت بعدی نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید امید متقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/680566" target="_blank">📅 14:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680565">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
لکه‌های نفتی به جنگل‌های حرا در قشم رسید
🔹
بخشی از لکه‌های نفتی وارد محدوده جنگل‌های حرا در قشم شده و نگرانی‌هایی درباره آسیب به این زیست‌بوم حساس ایجاد کرده است.
🔹
مسئولان منابع طبیعی قشم در حال بررسی میزان آلودگی و وضعیت جنگل‌ها هستند و منشأ دقیق آلودگی…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/680565" target="_blank">📅 14:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdbw_mViNRC0ZR2AbwyhkpDMBPuLFdO2pDGF5u2134di-chqF5qZLVbbLQWg2RngwLb76RrP1TWR614-FJ3BJhhvyybc8MX1mp95hMTnbXFPBqpd5iuiJbQR7rvS5Azsc6JaHfqSShRq0uStMxDS_KnafD6VhFv3YPe5Snv6pZ3_cBM7MrLICsrsDkTEAs9DzWF92PEgeZCZEgU1r9nfLAaQm8ytP6QGV9fow7WJoCI2tohJ5ZHz0MIixYVa6fbWL8IMMOOSafErvETll-6cNGAbX9DeVbPOunZVA8PjtSaHgAh6YopHHUXxMhyu244eCI15je-IRDHWeiAyi8Guzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس مجله اکونومیست، محبوبیت ترامپ به پایین ترین حالت خود رسیده. حتی از کم ترین محبوبیت دوره اول خودش و حتی بایدن، کم تر شده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/680563" target="_blank">📅 14:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
علی‌اف: کریدور زنگه‌زور و اتصال ریلی به ایران در اولویت باکو است.
🔹
بلومبرگ: امارات در صادرات نفت از طریق تنگه هرمز به عراق کمک می‌کند.
🔹
مسیر شمال به جنوب جاده چالوس تا اطلاع بعدی مسدود است.
🔹
آتلانتیک: ترامپ به گزینه اقتصادی روی آورده اما تاب‌آوری ایران را دست‌کم گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/680562" target="_blank">📅 14:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuqxxQDFdHkLlxY1EKYvfPeZO4t6xW2lBNeB_Zdo4jLUBAC7L-wm6xCbgbzAu6QmI3L2XhtT3xJfcACyTYg2sYCh3bMTWoZ_m_SJEhAhjrdYzzDJ3i3jyhESEabr6EGfBZ4RluV87l6-Ws0Zkj5MurW3-igkM44S97NEJyllu6IT_LezpdqfTvcM9FoRsXVfSevwlVMEX6cw9WCD4WGUtP3geR7DCUgamZyOwAb5CzOJl2oFm_6BWZmKYYJPvqRlIesNwYH_v8SIuMJpOdWBt_pFKE1wonsZTdLJnblc8BdlAx49r63ANFnmoXZ1HaIJTMIUrWNH-fZxCK0QeE9D-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال حوزه جنگ اوکراین: ترامپ در حال بررسی تغییر نام وزارت جنگ به وزارت تسلیم است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/680561" target="_blank">📅 14:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3Fz5gp9EJluFhrxOiOlmo4qwNN4OqHuME8qcWOrpAkFFZTIGtOLfAZGcpRwWjTEm-NkpSNwkNNjXUsg224DQJvZWoydP8Gw9C_5lltdbYRwwRsg7czmJr6Pxr9ch8LPmbZrE3YDYbhRCjsuuNk3_f5VRoMatabfZszIdMra50406crSU3uO_jaXR2qdZGzKqMIQLv92eHtfg_3_c26ps53W8CxPz9EZRc7LKx8gV5j1NCc8oeu_kET2R3HY2M3nCSeo161ozOZPbZaVxkNDeR6As6L1PwoVljCtudD8QBnmYy1fjWKa9p7RXc3mM8HPslMO65q1wsRZVbS5BNzChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ هگست را با خود برد، اما روبیو را گذاشت تا هدف موشک‌های احتمالی ایران باشد!
🔹
یک کاربر شبکه‌های اجتماعی با کنایه به روبیو: «مارکو داداش، اگر جای تو بودم، از این به بعد حواسم به پشت سرم بود.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/680560" target="_blank">📅 14:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNr5FcStelTtg7SyM8TgPe3F4mZHoy01HBkeUfPbbpwiazX40mu2YqBwIXwzcQEPn47kPNiE3X4lbIYeNUPLVGHIV4iY2wcwNDw7JhLExpxPGff8G0xuJ1vsZAooWqs3uPwbg8SWEM1QEtXkE8mjcD6UoV_0s1tISDDBEkWmo4Q58VECa1Sgsu8JJbH-huSYXt-s8PaaNY_jtLv6m0v97lmuCOZSA7wuIrzkpx1Hi_iyP65Yel-sOCkcdQ0JfeCTyrB0phNpKaZkbcfX04vyrY2CjUIH7lhKRLTV5RZ6Dv8ZwMRh7p8I-s0UC9-26_cFHi5XN87RlKiOm8ngcZiQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر مواضع مارکو روبیو درباره توان موشکی ایران
مارکو روبیو، وزیر خارجه آمریکا، در اظهاراتی طی ماه‌های اخیر مواضع متفاوتی درباره توان ایران مطرح کرده است:
🔹
ابتدا: «ما ظرف ۲ روز ایران را له خواهیم کرد.»
🔹
چند روز پیش: «این نبرد در آخرین لحظه است؛ آنها دیگر موشکی ندارند.»
🔹
اکنون: «ما ایران را دست‌کم گرفته‌ایم.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/680559" target="_blank">📅 13:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9YRHwablTf6_wxDcnFnA8zB5KXRcsmlfqro_MvmVfthQ8jZykVluQ8L1VpRLRYkF7zoajyU41z_3pLIXIBCBqQMKViy__GhDXtErFHywzlwroIPm7EutK1HOv-gNIjd1nQuncWOQRTbAYXTnZMJRFZPBdyVnZAC9T7rpPIxYYQgmruQB-Yj-nDlXqo0grV-BKdjAWEueLfwVWb-DrYeiYVD-Zo8YUVQu49I54vW7MNsYW1JaBkQeh74_YK4DW0LDLDojcyqSbKhb0PLvIVpxVYM69btSuTdGK81l4opWZLcufyvRet5ZpZJdx-X1KWbxEEzPPxnMBVp44qJfcaJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانیل دیویس، افسر سابق و تحلیلگر نظامی و سیاست خارجی آمریکا: این هشدار را نادیده نگیرید، ما مدت‌هاست ایران را دست‌کم گرفته‌ایم و در همین جنگ هم چندین بار تاوانش را داده‌ایم
🔹
وقتی ایران چنین تهدیدهایی می‌کند،  واقعاً به آنها عمل می‌کند. بهترین کاری که رئیس جمهور ترامپ می‌تواند انجام دهد این است که از این جنگ کنار بکشد.
🔹
ترامپ در «اعلام پیروزی» و بزک کردن نیز مهارت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/680558" target="_blank">📅 13:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB2D2X4p0zWE02mXf0v3gYjRla5aHn3y8MxCeSA2EIWcDaNUxQZLnZ5S7eJ-lIK2EwcDe5-AjgIFRYDTqrUF8Kwc4JDwddUwckBv-l7EqtHnR1tZ5D2t9sWwr-m-xZw7zXH63jkfh3MCYa_2CiAAmQhenRl7HO2Q8jBzoLvoC9MPu0cn8lhBsFQYqmiBTRHe70oY4PuPc7Ej1oIluPsE449JJeA-GABypYV1i80rLfJfFGlR0CNv_bTWyaOmM7XJWlg_DpfvzEXuU3wiipQV7SrCzFOH-p3ThV_DV7nZa1h_qEooleszlhJub1MQ5eugLAPXQ_vy5s22q-IQxyKViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وندی شرمن، معاون پیشین وزیر امور خارجه آمریکا: در آینده قابل پیش‌بینی و شاید برای همیشه، ایران کنترل تنگه هرمز را در دست خواهد داشت
🔹
بعید است اعمال فشار اقتصادی بیشتر از سوی ترامپ، باعث شود رهبران ایران تسلیم شوند یا از مواضع خود عقب‌نشینی کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/680557" target="_blank">📅 13:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ضرب‌وشتم مدیر برق عسلویه هنگام جمع‌آوری ماینرهای غیرمجاز
مدیرعامل شرکت برق بوشهر:
🔹
مدیر برق عسلویه و همکارانش حین جمع‌آوری ماینرهای غیرمجاز با هماهنگی قضایی، از سوی یکی از استخراج‌کنندگان مورد ضرب‌وشتم قرار گرفتند.
🔹
مدیر برق عسلویه به‌دلیل آسیب جدی به بیمارستان منتقل شد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/680556" target="_blank">📅 13:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo0DSuiO8R3i1KeTk9D6Ie-ga3McZZgYNRblLREAgo_cGx8VzEuqL-N4WKMwfqprAXLrvfknneqQG9iqhovV_IdUsmdKGv5Bk5EaH0Yqo1PlUTQ5NsRgTyxcCpiu7dMRMDU7FPC97RQpl2Q-KwGFlR0Gqp3UQb4Ona0nBi3vXA_I2JgnxCTtetXFCLoIP8JEw9rd-UDFC3ahU-XQwcUwITypn16QPRP-MugjWrwDuoTE0Wo1DeyawFvUnRbklj3A91Qyl4Rk3cyUnSyIKUElnw0rGiGI_xskvaAIAK9a0z99QTql2eHRPfegmj7NG1_7AUaoJG-IOPM4rMAIQ5Uwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طولانی‌ترین برج کبوترخانه ایران؛ چهل‌برج کلیسان
🔹
چهل‌برج کلیسان در روستای کلیسانِ فلاورجان اصفهان، از نمونه‌های کم‌نظیر کبوترخانه‌های چندقلوست.
🔹
این بنای دوره قاجار از ۳۲ استوانه تشکیل شده و حدود ۱۳۲ متر طول، ۸ متر ارتفاع و ۵ متر عرض دارد. نام «چهل‌برج» نیز به تقدس عدد چهل در میان مردم نسبت داده شده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680555" target="_blank">📅 13:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
۲۷ یوز در توران پیدا شدند؛ خوش‌ییلاق هنوز نمرده است!
🔹
پس از سال‌ها نگرانی درباره آینده یوزپلنگ آسیایی، شناسایی ۲۷ قلاده یوز در توران بارقه‌ای از امید ایجاد کرده است؛ اما همزمان هشدارها درباره کمبود شدید محیط‌بان، فرسودگی تجهیزات و وضعیت زیستگاه‌های یوز نشان می‌دهد این گونه همچنان در مرز بقا و نابودی قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680554" target="_blank">📅 13:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbcf87c51.mp4?token=fBLgqKfKwyeLq2DO-rgKDFEfQnf3uxiRbhZWiDSN1zQEt8sL0ZF6ntZfkoBLvma_bkdF9iExltLulH9N-TmARJMpvQp7-QW225jkx_j6dX0ltrO_zVIg0E_StLoqiWgk5SilAtyxF6XsYD7Zjffv_XO1KMArlaJyfMKgTvF3Slv1NeZ-v9ICxw9UR4Qafr5WxRw0QtTMjASmZf9xq9oCRKNV_zH3LdsZhNCMxT_lBtSzsh2Yjuh_FabL5gGy3taZKjFRDyWeMzsHxShdpyXRmqt_Bj7Oa25vZ-6bzJKMRRKQGM9hZZgJuMUZn68Hf7xtZM3CvcD-KcSd9HnfauGAiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbcf87c51.mp4?token=fBLgqKfKwyeLq2DO-rgKDFEfQnf3uxiRbhZWiDSN1zQEt8sL0ZF6ntZfkoBLvma_bkdF9iExltLulH9N-TmARJMpvQp7-QW225jkx_j6dX0ltrO_zVIg0E_StLoqiWgk5SilAtyxF6XsYD7Zjffv_XO1KMArlaJyfMKgTvF3Slv1NeZ-v9ICxw9UR4Qafr5WxRw0QtTMjASmZf9xq9oCRKNV_zH3LdsZhNCMxT_lBtSzsh2Yjuh_FabL5gGy3taZKjFRDyWeMzsHxShdpyXRmqt_Bj7Oa25vZ-6bzJKMRRKQGM9hZZgJuMUZn68Hf7xtZM3CvcD-KcSd9HnfauGAiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: بریکس باید از گفت‌وگو به اقدام عملی برسد
🔹
بریکس می‌تواند سهمی مؤثرتر در شکل‌دهی به معماری مالی بین‌المللی فراگیرتر، متوازن‌تر و مقاوم‌تر ایفا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/680553" target="_blank">📅 13:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzvsqcU4m_sj0aAGD88hyShT9RXLGcn5Ol8K0L7aCRBQoIOpm5Pzh-mmvn2Ut4QnOdwcCIvlq_7DGaGNc28sA7hFuXScF_B5mCgKRvah_hCNAI2RqStnRsGbeD6EqklVQIyu1xAGTwmHAp6OJQfhgLsv47zNqX_GD6KP7KguRIHYquAu_GqK94RRf4zZbCzIcYe948NwUydp-xYBSj3o14Tum0UIQDq9A5vxvuVX_Zo-w-MWplt1JnkhFOf2g4xDCrx2TnrnaZ1wfpTJWFxiSSg_JKqaiVaP5OXjs-TpjKnOsVJu85mxXfUPKE2mYiRSUs97FbSexraPgx7s-PndVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه رویداد نجومی همزمان در آسمان
🔹
امروز خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی همزمان رخ می‌دهند؛ یک شب متفاوت برای رصد آسمان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680552" target="_blank">📅 13:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اداره‌ فرودگاه‌های هرمزگان: فعالیت پروازی فرودگاه بین‌المللی بندرعباس از ۲۴ مرداد آغاز خواهد شد.
🔹
سازمان لیگ: بازی اول استقلال در شهر قدس با حضور تماشاگران برگزار می‌شود.
🔹
پوتین خطاب به اروپا: به توقیف کشتی‌ها پاسخ می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/680551" target="_blank">📅 12:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSPGZcL66O4N2OrFpkppQCFgywQcpfSM7XM5abZh1BMUTCj80B24cFqMF2y3eLrf1ZbtoIwKH7nhmhknqRxsNpLj_-3tOWEKj2n0b6auruLtJ0Rd3hUNXOqiaEFOJxzxiZ7gbFbkRvQxl4SLhESuqnzFnFDoLe53sTYGCriPYdnavemb0G9eoNg8OdPRAF5VTg7rdrq_HxZXqRLdaqbqmY2p6zNi7IzX1ZwpjqA78PJ8-gxlj1xEkJNMbBUvlLORrL-nKwUwY6Ov-CGD6EW285FW6KGTs3zWrOE0QxxPyYCE4VK0yjhWa1a5DaEYo_TvhU18hmuSQsEm-Gm1GgLn9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به بهانه مسابقه امشب؛ قهرمانان سوپرکاپ اروپا از سال ۲۰۰۰ تاکنون
🔹
۱۸ قهرمانی برای فاتح لیگ قهرمانان اروپا
🔹
۸ قهرمانی برای فاتح لیگ اروپا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680550" target="_blank">📅 12:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
لکه‌های نفتی به جنگل‌های حرا در قشم رسید
🔹
بخشی از لکه‌های نفتی وارد محدوده جنگل‌های حرا در قشم شده و نگرانی‌هایی درباره آسیب به این زیست‌بوم حساس ایجاد کرده است.
🔹
مسئولان منابع طبیعی قشم در حال بررسی میزان آلودگی و وضعیت جنگل‌ها هستند و منشأ دقیق آلودگی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680549" target="_blank">📅 12:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d72c32eb9.mp4?token=abJhs_g9kB9OmGclWTnBX_aXvPOm8sqZmPpji17e0GGsuZEmLYhRzH4sKgt38Oc5ihHYHfYMRolgGIb0idDWS-1Dw4EzH66EN5yKM40wAO2issLGJK3c2GZ2cIOVBOIONu3scH3Igxgdpf4mQWsLo1kjhBpi5CvdkMkBNJ6VZY-KQC_5j8kM-dELzL8BE--_3H_4WXwKc-1tJsvIf0NfNyc_PpVHFpLagXa_vGDzBWA0IhUAVxC2-WsTIShuYzfWWJEG6jQ_z128Uo3Sm3Z7K3Tz6bMxrzQTxFpHesZi35kA70T7bUDJ9WyuD4jrqWtmUOJaO57P0WD_F6dJ9nV0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d72c32eb9.mp4?token=abJhs_g9kB9OmGclWTnBX_aXvPOm8sqZmPpji17e0GGsuZEmLYhRzH4sKgt38Oc5ihHYHfYMRolgGIb0idDWS-1Dw4EzH66EN5yKM40wAO2issLGJK3c2GZ2cIOVBOIONu3scH3Igxgdpf4mQWsLo1kjhBpi5CvdkMkBNJ6VZY-KQC_5j8kM-dELzL8BE--_3H_4WXwKc-1tJsvIf0NfNyc_PpVHFpLagXa_vGDzBWA0IhUAVxC2-WsTIShuYzfWWJEG6jQ_z128Uo3Sm3Z7K3Tz6bMxrzQTxFpHesZi35kA70T7bUDJ9WyuD4jrqWtmUOJaO57P0WD_F6dJ9nV0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلوع خورشید بر فراز تخت فریدون دماوند
🇮🇷
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680548" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCGJ8Yh2jML18aXTHuszp1gfJoJFyOJC6Qex4tesSwJ0POuEtHL2uZoOb0dFiuCUBJcKYCwlWwrGH12rFhapVgIDNcaAlvpCcFDomb0nZ8ECPpB2ZzEAkxPWxQarlK3V97wdlLcDtq4rNCuJHWMYm7ONkJkBFdJ3IuJIdTbcD3HPjRhnO8j5aLE2CvdKGrkqCAZR9s_0X3K3CUWGR_ZhCVhk92asK3C9e2FUdr4BQaxFKgxKe3mqtGx9YfF9_3m9KPVC5DZZu3CIcpi-8k0eq_tvGh3abXEtB2gh4RZiR-_Dc9WQdEyPViXwdNvUKz6H2jwDGO1nTPu1H1PcFJleHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرویس دهی و خدمات رسانی متروی مشهد در ایستگاه بسیج خط ۳ برقرار است/ اتصال خط یک و سه در ایستگاه تبادلی
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680547" target="_blank">📅 12:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
لکه‌های نفتی به جنگل‌های حرا در قشم رسید
🔹
بخشی از لکه‌های نفتی وارد محدوده جنگل‌های حرا در قشم شده و نگرانی‌هایی درباره آسیب به این زیست‌بوم حساس ایجاد کرده است.
🔹
مسئولان منابع طبیعی قشم در حال بررسی میزان آلودگی و وضعیت جنگل‌ها هستند و منشأ دقیق آلودگی هنوز مشخص نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/680546" target="_blank">📅 12:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261223a0ae.mp4?token=JXy6R1alL4fX1gvcSpXasD3qvYpz62nxcSVT6mPt_4zAyJDNHTbU05g2RAQ-Pw9FEaKM7t7sPTKoUdykt7d3iviGFOBAgDNtn0s4-at7UWaepElj9VWLknta2NRbzJkOW9vAZ7XFegd8alxxrtHGkbugcAOUvIi1RAFsAeh9biOu6SH_DCtT9_akN7LaxD2M-fjL-3qWFywN6CifRmzKS88G07jJC7B6Te5twnC_V9iRBCupjA2JmRg854NQZtyHed6Jih3jdtJI47Q1pliv2b2zjBzxrsqmvCR3VwZRgRKlzwyHgU5H9_zN9-erenLTl9bA-8aLym9_Iog0yPipgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261223a0ae.mp4?token=JXy6R1alL4fX1gvcSpXasD3qvYpz62nxcSVT6mPt_4zAyJDNHTbU05g2RAQ-Pw9FEaKM7t7sPTKoUdykt7d3iviGFOBAgDNtn0s4-at7UWaepElj9VWLknta2NRbzJkOW9vAZ7XFegd8alxxrtHGkbugcAOUvIi1RAFsAeh9biOu6SH_DCtT9_akN7LaxD2M-fjL-3qWFywN6CifRmzKS88G07jJC7B6Te5twnC_V9iRBCupjA2JmRg854NQZtyHed6Jih3jdtJI47Q1pliv2b2zjBzxrsqmvCR3VwZRgRKlzwyHgU5H9_zN9-erenLTl9bA-8aLym9_Iog0yPipgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سیلاب در تویه رودبار دامغان
#اخبار_سمنان
در فضای مجازی
👇
@akhbar_semnan</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/680545" target="_blank">📅 12:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
حمله موشکی ارتش یمن به مواضع مزدوران سعودی در بندر «المخا»
🔹
گزارش‌های رسانه‌ای از حمله موشکی ارتش یمن به مراکز نظامی مزدوران عربستان سعودی در این منطقه حکایت دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/680544" target="_blank">📅 12:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
کشف پیکر مطهر یک شهید دوران دفاع مقدس
🔹
همزمان با شب شهادت پیامبر اعظم(ص)، گروه‌های تفحص شهدا موفق به کشف پیکر مطهر یک شهید دوران دفاع مقدس در منطقه عین منصور، شهرستان موسیان استان ایلام شدند.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680543" target="_blank">📅 12:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjYypX6ZmORjKqgug6_tOMNuLwKVr9MkZYE6AJvGOHRwOi4sxuWOVJ4AE0sVHlHbexmJenIonzGlsQepTOfU_UJ92UN08wcGD17WXcLZOqUllVip9PceyT1gqmcxdAHfUSwYaCEs8GcWHRopVJ3RwgldJ5TpULVxutQDc7OCv9gFcsNwNGmqT9eMYDuPuw9OOTGsaVHfC0L89re7_n5mAFM9O-juy3SksbHZqILRzSRb2jE1famSeSJ9im3fcuAlPrceG01oFJ_QGsx6Av-DZ-yGHhpVDE5TdTNBlDb-xCljpl44taPoQJu1lKYGlHpA4R_93K0eMvQi-wlldn6yYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقاشی منتسب به آدولف هیتلر ۱۹۱۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/680541" target="_blank">📅 12:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
هزینۀ اجارۀ نفتکش در تنگه هرمز ۲۰ برابر شد
🔹
کرایه نفتکش‌های غول‌پیکر مسیر خاورمیانه به چین به ۵۰۰ هزار دلار در روز رسیده؛ در حالی که ابتدای سال ۲۵ تا ۳۰ هزار دلار بود؛ افزایش ریسک تردد از تنگه هرمز و کاهش نفتکش‌های در دسترس، عامل این جهش اعلام شده است.
🔹
یک نفتکش ۲ میلیون بشکه‌ای با محموله ۲۰۰ میلیون دلاری، برای سفر ۳۰ روزه حدود ۷.۵ درصد ارزش محموله را کرایه می‌دهد؛ یعنی یک بشکه از هر ۱۳ بشکه.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/680540" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBT3tn2kPwhFZne2pGEXJK1txWlGd9FR2s5MNs4YuXVlYSzBM_6RVqzxw2f2iEk567-gA3cX3Dee1Ht1Itu8dpjnN4YNq72cCGsWg2_r_8KbHAJm4-yw0_gC6ZdvWdRCQ--jT-qJ-IFoJl0Jhe5vLV1ODSS1AZWG3S6aVUSnbsH41apWwRQcfjTWgBMzhR0_NeC2NXjcPC8L5fxg-Dihdn6slcpimm0omO7_-35fXuzQ_ClA-2iNSpUSr5oQW3oroOz7AhvVnxrTVGcCJ-eJZaMK79aL-QN1EU25sqQNEoOTgMbfFUpALmiD_Vc9sZsxe49JSwAJFxEnrM-UMR90iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلون میزراحی، تحلیلگر سیاسی و فعال رسانه‌ای اسرائیلی-آمریکایی: تمام جهان غرب به یک فاحشه‌خانه انحصاریِ صهیونیستی تبدیل شده و اگر ایران نبود، بشریت هیچ امیدی به آینده نداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/680539" target="_blank">📅 12:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سردار جاویدان: ادعای حمله زمینی به ایران توهم‌آمیز است/ مرزهای ایران امن و استوار است
فرمانده مرزبانی فراجا:
🔹
ادعاهای مطرح‌شده درباره احتمال حمله زمینی به ایران توهم‌آمیز بوده و تحرکات دشمنان هرگز نمی‌تواند اقتدار و امنیت کشور را خدشه‌دار کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680537" target="_blank">📅 11:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680531">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyExXOoCgyyWKX69md1imvE7nGmnqldbDOQXN7Rg1j0o3tZxpyVDbEbdnq4Sz6i9ET3k-Ze8o9Mazd77kG64qZi_I2K18dLQXw98dA3m2dhyIOcCg99-RlbUnDM9P7SEz-nbJKV7Tf5WBCKQSurPfqB1Ih3EEfa0m53buFl2hXImiJhqFNAb3RtEa4sAxARs3eu-5pDHSCRLlDI1YvumFV61zFQq33no55UHJgVz1sHAxzGNmUMWNpwf9rpwQENoop0dLlso-Romlt28ElZLhAIZmtD98GcMo9oUbEv_XFEs7LEXyUFmnvJzFr1jAHWBU-8sc_i7HECoFQ1GQyzBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5OVI_J00l-r_p1YFTB06wt0yi5PafDRAy9FGNF6lTEA84ciBlS1rIcDmJgICSq4FOJ6uOhWQ3-2NZ-ntsRC_Kf_9Q5qk0AJ0eJYlB5G03iPBLB_9FyoWi6_A7zX_tEXgBhf0B-995iJulopxAI538rf5Qr7QsuiTy1Vm53-jl7ekWeTdyfbWdcgc7KKTvAlsK6Uqi0SHn6TiSQXX0-iQ3S4qA0GoX8qLOaFTMb1AaGE8gTH3kkh-5mkLxcB1hnrYQjk9H-BUa_XxWljQ1LOhket2MAr2pqPsRFu87j8v2CC8jIH6eOrYrxOTiFYH14Vi_r63xyOsd2u_2DfOrQ0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIVfWfv_TsayUyqdsvFBmE_RQ0psEQTApZFOE24d_YzCuWhuShmd_aXtcKSq7tS2V0Ija8FiuUPaH2J8XymFudNkH8N77ga6S7mcdocsonEEeCqYvRg_52F3WWyFXdS77LQ745Ezy6NzWjNfW27D_hht8bRMGhXIayeGxBsK9uiMTenNNDWaI0_dC050jj0rR8pt1xoWnRv64P2UOH-STfFgy02Set22-jc5dbOU01B7pzY5wiBh7qZi7Y06qpKnXPZQ_r3AzRKtRRXLgvojF5AeB4ihV3reYfDumFLWqJLUNVksHukwlCdb-YqhZ0ea6CnMgT8bjZBRGI6ucHOlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5eIQqJqX9Bxcd3Whq7R5XbbKPWaISI-943IYm11IRzjF5rICfsXc2C2DtDtH1kImoauObMhTOU8BTezqxxE6X22LLq2w4aOqWQDri7S2u5eizLqYCANC6cIeu-hW3k9clgRy1XOrTj3TT9xkQnms9hWIajxUzLbieKN8jBMTWSFfwqtaQf1HWwRwhh9-Tl3p3zQAzPeY5MSfyPINFyl6nXcXQHjG3ao7MxTasiCYmd1lWL6hN6_zogAOLlbojLZr7Kg_3PziOUHMAEuc5x_36c_lZ8wv0xDxlZ7Cfp0KihzobgB23BOBUOb0vfFtuyl113u_tfBGY9sb4q56OI2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTy3huq-c0aVM6-Qf6mFRQEXItOTNe3XQF1jBY6QXUsWErthdnCdHo5q-r9QeBepAR1LoU3ifjjyJSCYh51xhHLKruey-KnL0X3qrRc1ES5z1Ao2spQH2O7QKfseAeVdkDasYW9IGiyCS4aV-W_yvK5rDHpN5f7TZarQ_y9l1AYUqy9TXbGOqhRsBuL_6O6YUFA17F2AAtsBpjxl6oX2LBxj2i0FIH4cQVPesNl108nSIMHv898j4_8xjXMxmyX9SoB9ut6-GXvnIHevodysZ-ee5PoPuxhMP_aafdgQnrhxkZ7AYbo18yU_RXAFiy2qGW9S1XBSQXJcUujjGK2Odg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvabj3dCO9NfpzsfWYP4RohUCl1aL4Cz5IX3qL8MtaFCcgKbavS2Y6fblQC2Lqd0vUHGFA41nxPUaY3Uq7no33gJM1Wh9lPujpQk7wAGkWwW2IvLKivqOza4CYDHcs5oD0nXUKtnrFvoCaCJs_qVmejYMW5O27Bk0Q-7F1yrA-EzGaAZRUg9baEBI25jZhq42eZcqPuxl_WOCrq2fWWFRlhY-_RWCM1QlW_94b8PF_ZCfRXvnAgZfAeb1fWX46yVuRNWhNzf0tZjsKKp1ZGmvICLS_estOE1if6Xv681nhn8VE7wDNEswkxInP8uuyCJ2kr9Y9zt7AoVmCOZDoQFKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تهیه و پخش بیش از ۸هزار ساندویج در بین زائران پیاده امام رضا(ع) در موکب هیئت قرار و کانون سلام
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/680531" target="_blank">📅 11:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680530">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680530" target="_blank">📅 11:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgswgjwAp0zZ7zXLGYsXINO1IngGz0s9S7XlyfLgqGFGFXUsg7jnnmgxOFuG5eRuDt1dyI__wYXlNJIuuRG5kJn3HGcwvpsdBG-hGodYr0Z7Ii7PbNRCAAdAmlfCOEh7sEI7FHGS2paPbwelbUeuxt38GuqQ9Z54Y2RmbhTQj7Y6wVFwRqnomnHuXF_4v-dSOED0QiouJdhwC29xtPlv_X-E6xami8q136WwWatHtgDRyDZgcOXB7dt-KEiBlzlAZhqu3SUI5534lApMhKPeqOTHC-lv3NeaG8D8z6efG6Yphnx29R1NeL4_FKEDY-slF_JO3Fd1qAxjao0ZGo91Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3BH-JAldyCa-k60ePC2Sl3GbrzMnMsy4Wk0eu-GU-LqerkTL1NvzRbWA6cSc6t3KVfWkfqxQpIhEoWBzH96tf5o-ikgUVIgO8JapNCCaQGIkPdFKjcBYbysR2Xqk9TRQUZyygHy42sKF7qxtPxoRYM5s0tdMdxlzBJ9ncoAmaVG-sW5ZYPTBnY9xfJ1W_3GR5Ea4imVF2KvFYDonyvn_5ZIT5xmoVIBOmqBFVRnIB62uk3eDnA8XocW21i593GRZsZ_GR7u_Lvisb_ByzOcCIzdD742nXnk2cSbyO83ABdTLaSrJVsnXjZEypIKqHfEGvpXmvHDgE35QH7JVx7hSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این یک دیک‌دیک نر (Dik Dik) در پارک ملی اِتوشا در نامیبیا است؛ حیوانی با ظاهری عجیب و بامزه که واقعاً شبیه شخصیت‌های انیمیشن به نظر می‌رسد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680528" target="_blank">📅 11:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680522">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqFQol-Ymy8-bu88HnshFpdybL0W0qV7qvoyL6_8ZjEvWCwUi7f3oaJtOV6l70pckK22CwQwOQtZ9Prc4iNaB68JpDkpShdXAovcr4OQ8MftTo9tVHaCe3LqzOUByF_GlZSa1WgZjxxxPY2KHxXFFahPggjCxB7msOwY33Z5nHFlUZkFJ0X5IWbxgJGKxHtC67PDoqkt9KBSrFhw37IpeEZ3ISvXMI7-gj8Bboab5BfaCJhSZ411dhHYrt1xCandNiRl6S2tUAIdmJol_f9kvkMYXRFlM-SDH3jHAb-M9p49hczusoutscZuUHG2Fqu6PogYoizUWrxz3hDnB1r5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af677bab1b.mp4?token=kO-983VCMM_LhDAFsHCb2C2EkbJUwLhutiZLwKMFOEpB9wAGCZ_drRggu4c6idLltjwsL0XnqbxAaJmXMrcxTLiv9J5XShH4hsmfnyWHaZUrMXuPnMaoXqxs6L9V8By4Hpymv8igK7eMt9Em7UBe2FmWvnfVndRZkBbbB3uRudlBTZQsCUrj91c7QB6bZny0fGyJHpDRgEn3Zti-hHREoFPNvKVjFhKx1ejLCCVKqfMb50TU4OtJriiSVHfM3KdKjk3IsYKGq6g_I7FhPnZ9Zl4vWFC6eQ6UW9uFffjN-G-JCTP9WcyYdgDWeqbdeXrz0dNUguGAc1_yqLjt0kagWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af677bab1b.mp4?token=kO-983VCMM_LhDAFsHCb2C2EkbJUwLhutiZLwKMFOEpB9wAGCZ_drRggu4c6idLltjwsL0XnqbxAaJmXMrcxTLiv9J5XShH4hsmfnyWHaZUrMXuPnMaoXqxs6L9V8By4Hpymv8igK7eMt9Em7UBe2FmWvnfVndRZkBbbB3uRudlBTZQsCUrj91c7QB6bZny0fGyJHpDRgEn3Zti-hHREoFPNvKVjFhKx1ejLCCVKqfMb50TU4OtJriiSVHfM3KdKjk3IsYKGq6g_I7FhPnZ9Zl4vWFC6eQ6UW9uFffjN-G-JCTP9WcyYdgDWeqbdeXrz0dNUguGAc1_yqLjt0kagWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های شهادت پیامبر اکرم (ص) و شهادت امام حسن مجتبی (ع)
🥀
خلقت چه لایق است که صاحب عزا شود
عالم عزا گرفته و صاحب عزا خدا ست
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/680522" target="_blank">📅 11:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680521">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680521" target="_blank">📅 11:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680518">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCMJgwoqg-ONbDE1lDcPZM0KPHIBDorDfhR5SxYsGuzX7lTbpNrV6uYcneMJD5JsZLKmtDu3SoURfZu4kF87TeEHcjfv_jq9kFPP6X9__SXHfyBZdhbn85X7X2Db53Q0nWLf7fz3IMN0chyTkF_ACkh6yAiTe_i2erZs2zwU2qTD6A5e4LTGdEe7E4eLMb6x-OnIY3yFaduGv25voLaEtDjY0yh5uaGGdMowfS-j_m6uVpaN_Y4w9yArng93bzdWWpTTjPkWIOQwf9ucPnS-BYJhnUTH_xTktXy8iHy-Mb9x3gMkLejc8F30S2a3bQTZqBIbISYb-khOv8bltUh5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب به روایت خودش: من بیست‌و‌هشتم ماه صفر به دنیا آمدم
🔹
من در شهر مشهد، مرکز استان خراسان، در جوار آستان امام هشتم، علی بن موسی الرضا علیه‌السلام، در یک خانواده روحانی به دنیا آمدم. زادروز من، بیست و هشتم ماه صفر سال ۱۳۵۸ هجری قمری است.
🔹
امروز ۲۸ صفر مصادف با میلاد رهبر شهید انقلاب است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/680518" target="_blank">📅 11:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680517">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p674YY1Pv4yAwXR9RT7g_aqdv_ZckjxawrR4O8CMTo4REEiWiUpYFr0D0rRlqkru7KrZiRPEAvUYj6lGDibwF73kes0h4kCQLebDsHSL4ND0zJcQILYFvsUpwTQjB-S9ii7HDDan3isTYznRTSdPXNhrOULA4Dyhk3xP9d2vV0xTAE0-NYXhGox9xwIbkOauNDt7lgjBn_o2T5SLjAl_Eo84Kmk0dGXqfjfCHctzmdP0rnhUE0tdiy0dghUmcI3Y2zQtE-BeXVTV3SSccKoQmh7uRm5hgLwFeAd8AXf_DOvfQkQJhb0tqQwKHTIEHXP1dpDgYkbk-BGoGtOKqkvJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
مراسم عزاداری ایام پایانی ماه صفر و اربعین رهبر شهید
◼️
سخنرانان:
آیت الله کازرونی؛ حجه الاسلام دکتر رفیعی؛ حجه الاسلام پناهیان؛ حجه الاسلام علیزاده
◼️
مداحان:
حاج مهدی رسولی؛ حاج احد سبزی؛ حاج سید محمود علوی؛ حاج امیر کرمانشاهی؛ حاج محمدرضا طاهری؛ کربلایی حسین طاهری؛ کربلایی حسین ستوده
سه شنبه ۲۰ مردادماه الی پنج شنبه ۲۲ مرداد ماه از ساعت ۱۶
و ویژه برنامه شام شهادت امام رضا(ع) ساعت ۲۱
📍
بلوار سجاد ابتدای بلوار اخوان ثالث</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/680517" target="_blank">📅 11:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680515">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3162146fd7.mp4?token=i3YbJVLpHF-H-vAFQ-6iwzLWSmxz-rE2y51sxaSN1yz5cdChDkrLM6oE3DvLkrEpzZilooIPUDyaDE8ge_B2RgmNSq2vNztVE2kt93n-ZaMC6wioW06Tbuaisa9u5wHq1McR-3Edu1drNnizPSr3GYYvYcJK_RJ7YS5K66hkxWScxvt16h-4UgOFRC41wovaTT1YFI5E3OGJc0JqhfN6fFZE9Kv6FCyyZqlJw8HBJa_z_Ril4ikGkg3eOS3TFB1s7SFlYX7dE-n3U8SU5qL7hPFp5zxcZSx6yrfHsews6qIuo7S5ZlQONUlpeQUz3ro76AYWM2u1KWhDpygs5qnyFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3162146fd7.mp4?token=i3YbJVLpHF-H-vAFQ-6iwzLWSmxz-rE2y51sxaSN1yz5cdChDkrLM6oE3DvLkrEpzZilooIPUDyaDE8ge_B2RgmNSq2vNztVE2kt93n-ZaMC6wioW06Tbuaisa9u5wHq1McR-3Edu1drNnizPSr3GYYvYcJK_RJ7YS5K66hkxWScxvt16h-4UgOFRC41wovaTT1YFI5E3OGJc0JqhfN6fFZE9Kv6FCyyZqlJw8HBJa_z_Ril4ikGkg3eOS3TFB1s7SFlYX7dE-n3U8SU5qL7hPFp5zxcZSx6yrfHsews6qIuo7S5ZlQONUlpeQUz3ro76AYWM2u1KWhDpygs5qnyFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استهبان؛ بزرگ‌ترین انجیرستان دیم جهان
🔹
استهبان با بیش از ۲ میلیون درخت انجیر در ۲۴ هزار هکتار، بزرگ‌ترین انجیرستان دیم جهان است و برخی درختان آن بیش از ۴۰۰ سال قدمت دارند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/680515" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlefbayesafar | الفباى سفر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyqUX58I42yxUjoWt7-csV3o9GFdg_LneH5WTILCoS50mX71xFPhdQLXDAkXj3S8STaUFdpSifb1d5a2COiFiKWiapeigG3w5ik52bAbJYaVSdCPrSv3kAio9RjKh9SNaTgk_owXOsK5R2au_xQy0XgEULCQKWNDmte3IL9dXVi7KR62h1hFGPJgBAFnGTxVbM5n7y55vY64hMolE4i--ftYNsfYzWnFDV6vSPjBZlCm9oaDpnfd8ABCWnVoWPdus2vvwSWfpJwfGKRoA7FaxztVrLrr2z7JMSgJVcjRvkC2W9MdGb3N7ujSeKZ0-079Dehy0OkQHVU2N1e_Vnv-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
آفر لحظه‌آخری مالزی | تخفیف ۲۰ میلیونی!
این آفر رو از دست نده
🇲🇾
قیمت پرواز از
۱۱۹ میلیون و ۹۰۰ هزار تومان
به
۹۹ میلیون و ۹۰۰ هزار تومان
رسیده؛ یعنی
۲۰ میلیون تومان کاهش قیمت!
🤑
🚨
این آفر فقط برای
۲۴ مرداده
؛ تا ظرفیتش پر نشده، رزرو کن!
✈️
پرواز با
ایران‌ایرتور
✅
حرکت از
۲۴ مرداد
✈️
مدت سفر:
۸ روز
💸
شروع قیمت تور:
۲۲۵ دلار + ۹۹ میلیون و ۹۰۰ هزار تومان هزینه پرواز
🛫
برای اطلاع از
هتل‌ها، شرایط تور و رزرو
همین الان با الفبای سفر تماس بگیر
با ما حرفه‌ای سفر کنین!
سایت الفبای سفر
💻
اینستاگرام الفبای سفر
📱
تلگرام الفبای سفر
❤️
☎️
۰۲۱-۴۹۳۵</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/680514" target="_blank">📅 11:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAZlCrRSokDkbPku_QvOg5nzodYhoe7QE7rcoJcHsijoi5s9wObbW_fyCEq4267BCOsN6B0zenb4Hpvui0lCBF3x7dkyK04JYxI4C4Eljz6Tt5JvhDx-8fGDinEz0sfaOfs4STeEAWflU6ovTxKffWscZlMAuY2sXWX3oa_ajsugEzqsLJ7FLsDT4aaFOPt0k4eZudaOYAU7orW1zwMW04dqjXqxHyRgFwOa9l2OhffEr4ISpmpyihX3Wek54MklMFuuhhYFTZdsj7d4LUrLJJYX0BPExu6IK0bFzFFuoEAgc25_SLczaxVPwQttHRld6SLsg1OPjzwZbix01oLuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nok5ACmBs6MwGsWt7ieiT4veoTMegRu0KgEbHVjr-UndNm77q3n559_bnP3qBEpxo4DAYtVo_HdcCG2dKyrGqUnPBoRy-zQJNt9PgTVB60cRoDqL1Szb_Nr2krkNp3u8UlUz9HgPFIPvTjtqcT-6VEsfgjDNd9t0yDL8RdT-GVo78T4ZGy7m-12yuTCtsD18bIWM6zzdr5yrB9DzD8BiIym4H_0yEyTbrMduRjRCMcmY4OzkTrrmn2myvRSJnGsVmOZKX4Hl8FB25JoCFQjMFCsrr0lYAANBqAORkMhhpEAlmh2xfWNTCBv1jzqeoEf3KBX9kcOU5A5qltpt9_fa3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxu_9w4ADb0W34dHLwLhUuQVgtLs5RAHSNgTtkEfnbYQeAOs5qiy5lXmO7awMv1n811yCv7cuEUSWk3s0BK859yuCCjvdm5twTR1l_ZMThejLPaBmfPD7BTcAZT9MbNN0XXO_cN9txZAbDs61lfGx4ak6QjxvtVA3PbRjCiBYKuoY_kANCD-c0nLg80XjWPe7rASTxhV_FuBy6yquCt9lNBf4eKym0pN9w42B2uBtLkkj4vB42wp53AJbkK6HBr-fIkSK2BITTX5sLjQphALb7djJHX59al_eSxMCwR224i_4N6E52FIqx8eqjbJSpcMSgeKTnSC7pqfZUa0Bi5LCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnLTM19Xv_vYRV1B7aCF1iFGr3Kz1TFATYIdmk16JmOWln-DuFKVnJDLS9bR4xpIBjMU3knFnQvBUqhzvbnu8DlfmmY2iRDqbS4zNF8JUZ3bGrYc6Rj7Nm84t0AHtPYtU6KfUoMfJrEYwcEqVB51FeIoouNcMaS5NsrUtc2xRn3oMUQh5y0UETgKVKsODPBrSQtsRqD1AhXVeX-PQxViKV_N7pBtJOrSnF3nz5RK_nUTyiVZ8615U--3wvMSGTl2SIgUBVApvPyXHGd_YICwKVpZ4nvrPvEqlqkzpD54Zbudq9AnEYrimUBP2U37FlZg1YdnajoGWxcVla-RETPoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BquNF3fZtSZSJYXwTj4HQgpiLGdSp1jAnFsSib5-iPZRSzPDX3wAfRhcu_De8N_EkSZRclSVEA08Ut1Q-pYclXuYlIi7Y-GFfwnP4cr5N1PBgQAwoVQyQ183uQExQi9atBolYwQHAx0bEPK4MQIf93WotjirZ_OOF-Co-uhDocRo9HKGpbHrzppUe_lDHQWDrg2eSXZXt79HzuRt8mzt7uKlKyYjtPvsRSmolBRz4pTxEhFJsV2vWzLEHCyCzWyCDornNpCCC0bbhmQeYDrTT7ACpL1g19ROZfV_n1jUFzWEloEbIkXhf8iu6FPwJpSzdg6xmCpg9Et1keE6Dbl1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoUM03krx41EGl11n6muV5qy_LIsk8BJPHWClBM6Pbc3O93OT4fWZkKR_g6AZrw0DrVX0QRyLvpg5nvNBP79dnRGSXw6IBcMH-YZftZkxauv-4qGW7aLU2gVJoBu_c00J6hxS2zMDfwV9nHlyr2C_bQR_o-jOYvyAKHQc9Nqb50-BYjKw8ApiHEpUV9BGfwooYWHov-fVzmwrCT9bhwT7DHA8ckuxv7yCKBflrlKfQtBfJ33LlZt1U6vK5voosfyrbudDmMG0AFbcs9JgE9Srvi_91WS2VbzLHzqFZhAL5KHrzJZJX2FaE_UF6T5KooOp-_abqFKYHkwDo0f-BWn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbKsnEZxMdnNozvkCfV01m5crUaamcKJrH5UhYKbrqtG6Radds_gaBPcudIBwUqxH5HfnGjecFFfLPfZe4T2VxodOHPzHqvrfEUQjlwTyTi5PDEGW71EjjxDTcS2K6KrKCLyOyCa-MQeAZ8Rj6rV6WrdveWTVePHfwWa2o0vdD_SKa-2S8TdyZwARtBZD1iYPV2QHzrc7Szw17jjhEzhR1DAOeqxGHs1nZnYnJKBxvYjxvqU8QedVuLjcqgooxLbRrfyEdq14ieN9i2ELOd01OeXMz7Dg0x3lEzymoWN2DJTmP_xfJKupwjew4LOQe5Cz1ae0sWKaI4N2n_fb2Ddrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUKYIlVD-wkllzoajN-3bOywzWK8ZWY5aZF1dapTXaKjW3ntq04WNjYGhlik9C9FGsonY3gw4eMX_d1KFPfQrU_Qj3h5cYI4jNXj-crk5mbM6GIoTyzTjf2FikyV_A9smph_GqUlhbO3hMGzytBz7lwSXNX-BcLFp0pd8VAuSn9N9ABcETXAl9l9R-K-pE81I6CdoypNo6DNqdw44afSaIqHlMZF1U5WQIJ2tCVLS-cz--UVPF04PcPzFYjCLinKD38oZM2TPulj-y3zFsOtaRv7hC4ftQBDVrNhC49uS6Zehw3CYROzB4ZR_Q2FlA6-t5ArerWvSA6j2CwkMwZDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0CXKio3N83yvMmnQohatqdkkoyhr3VZCddA3Q5dKK00lg2xo-MajPsxqjfrpqS2WQuOnJbqZ2Mcq1YIeFViZRFDR6ee8DichIuSw8koYS0Ot_-Kzy_f54v6Pb0FgFfSpx5yiT7trYmmOKvVB0ahGY5GdOJCSKrdSXXzB1kfHHfCNp4FZfeA4TzQGGraHYZFcnkwrA1k3tNsDtSrQXBoacrYyHk0h2GHcm1TO2HQ4UPKX9iCZyR4ZrdDBAk38gimL-9W2tWpliCZBFMKI4tF05h-SIkciYcTuBCqfYeDwY-hMbD6diTYsUFVBPzCtDHgEvzJ5UmaRKFsvunot30xbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خدمت‌رسانی به زائران پیاده امام رضا(ع) هم‌اکنون در مسیرهای ورودی به مشهد
🔹
در موکب هیئت قرار و کانون سلام در محل تپه سلام منتظرتان هستیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/680503" target="_blank">📅 10:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680499">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
مذاکرات ایران و آمریکا درباره تنگه هرمز به نقطه اول برگشت
ادعای خبرنگار الجزیره در تهران:
🔹
مذاکرات ظاهراً به نقطه آغاز بازگشته و توپ در زمین واشنگتن است؛ تهران ممکن است به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
🔹
با این حال، تلاش‌های دیپلماتیک و میانجی‌گری‌ها ادامه دارد و احتمالاً در روزهای آینده نقش مهم‌تری در مسیر مذاکرات خواهند داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/680499" target="_blank">📅 10:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680498">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12f75205e.mp4?token=be3nSY7sWOPCApxtCjBvilv0EWE6AuqoLoRAgZV8R-epgcjIL0_UWUOJwRR-Fj5YnSGKpswnM9PbEXTSxsCeZHAn0_uwAuOSiFE_Ao8p7Rr2V21tN8RY8fXPYLk8PN92nOmedB_zI0SQT2NKAEfMu6OVlsl9yf7lfaiIG8WiSmNS4r-Jcc2OBZTVaht_UvxwYurXsknfqLZEF0SSSvEdQY-fN07_7R7HPSXgQgblEoqWI5IAsafXBo4dww9xKfF0u7Y0jJwnaEISuLGX6064dQfhQgRo2VcsDAJ7L3vGFXXPh6f0jR9mU7lcjDXCnLxDLhuJmWWTK8-7M2TMi8OLKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12f75205e.mp4?token=be3nSY7sWOPCApxtCjBvilv0EWE6AuqoLoRAgZV8R-epgcjIL0_UWUOJwRR-Fj5YnSGKpswnM9PbEXTSxsCeZHAn0_uwAuOSiFE_Ao8p7Rr2V21tN8RY8fXPYLk8PN92nOmedB_zI0SQT2NKAEfMu6OVlsl9yf7lfaiIG8WiSmNS4r-Jcc2OBZTVaht_UvxwYurXsknfqLZEF0SSSvEdQY-fN07_7R7HPSXgQgblEoqWI5IAsafXBo4dww9xKfF0u7Y0jJwnaEISuLGX6064dQfhQgRo2VcsDAJ7L3vGFXXPh6f0jR9mU7lcjDXCnLxDLhuJmWWTK8-7M2TMi8OLKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطار مغناطیسی چین در ۵.۳ ثانیه به سرعت ۸۰۰ کیلومتر رسید
🔹
مدل آزمایشی ۱۱۱۰ کیلوگرمی قطار مغناطیسی چین در آزمایشی روی مسیر یک‌کیلومتری، تنها در ۵.۳ ثانیه از حالت سکون به سرعت ۸۰۰ کیلومتر بر ساعت رسید.
🔹
این آزمایش همچنین موفقیت سیستم ترمز اضطراری را نشان داد و قطار پس از رسیدن به سرعت ۸۰۰ کیلومتر بر ساعت، در کمی بیش از ۲۰۰ متر متوقف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680498" target="_blank">📅 10:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680497">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680497" target="_blank">📅 10:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680495">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2685de5d44.mp4?token=LB3VkCIA1Vo3bjeOddbpjph_1nGxM3ksGBTEmZpp6FBYT6Kp1FcLYubVBJcZPHzYtLchgUZNbTlxYcsM_OaFkabnnqNQ81_jtVELUNs62WHW6-65nGXcAklGertEKKh0PNeERxT-_jtxrEDrRYl5Nu3cLr2tplbhP8h-08p2FRPGa8TtdVUqXXlWya0Ptvs_lmPx6Myg80ffj1O-vjRxWQzURtYjGLY5jGvMP0V7l7xs4pFjjzRb0wV0usx37tcrLKnhQcjJ8shsMm305oVpnET9Ka4WLAwLXgEv0H4FRI-yDz4-LtPcHeKLhEn0vWrUkf3AXTzPi4TwG4daRyZHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2685de5d44.mp4?token=LB3VkCIA1Vo3bjeOddbpjph_1nGxM3ksGBTEmZpp6FBYT6Kp1FcLYubVBJcZPHzYtLchgUZNbTlxYcsM_OaFkabnnqNQ81_jtVELUNs62WHW6-65nGXcAklGertEKKh0PNeERxT-_jtxrEDrRYl5Nu3cLr2tplbhP8h-08p2FRPGa8TtdVUqXXlWya0Ptvs_lmPx6Myg80ffj1O-vjRxWQzURtYjGLY5jGvMP0V7l7xs4pFjjzRb0wV0usx37tcrLKnhQcjJ8shsMm305oVpnET9Ka4WLAwLXgEv0H4FRI-yDz4-LtPcHeKLhEn0vWrUkf3AXTzPi4TwG4daRyZHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون استقبال از زائران امام رضا(ع) در مسیر پیاده‌رویی زائران به سمت مشهد در موکب هیئت قرار و کانون فرهنگی سلام
@Heyate_gharar</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/680495" target="_blank">📅 09:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680493">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDgusxUAH8YLKqUHCTRyrdS5ljdUJPWRpmkkR51zj7pbPKF_-yTfLN2ZOfLifYO_W2dm3bLiw7TarU9dMnXG4ZEpxhOs1TdiurAMjwjYl2AR-UmbI0lkhnyvM7UFl7LhvTmIRobdK6-kuxFecOV1zyRfn5bAznIy_JF1G07hZUNT4B73RK9CVu9ci6z1FrJK9BtBz8A263_-vmZdyC92KU0rv5kJCnrdGvXoBcLOl4k3ncY3loItCaZ_rDm9hntth86dvBbTbDNOTQWhYTrwWIn19UwWN6KmH5F2r2bkMH1m1P7N_bbZLOX-nTgyrUBLs5dkBjpS5T4tPW-RANbehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار مصرف همزمان مکمل‌ها
🔹
کلسیم جذب آهن را کاهش می‌دهد و زینکِ دوزبالا هم روی سطح مس اثر می‌گذارد؛ برخی مکمل‌ها را نباید هم‌زمان مصرف کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/680493" target="_blank">📅 09:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680488">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5zmpkY3wqADoyU4nwEtsziNFYQEfN5z7mUOG0q5oLeuqHJaNhgd1S_F3kDc43wcyPsjkiJtL-SMuxf-uq0Ovs60ERFZVTKaFFCXXysP7JBc0yuUnwsoq5VoIOfavEmxIu1HrM21m4YIutLLzFGfPhXlN0ziicVAGh60twjW6OqBCGus32OCih4kcNqDrRxo07VcZ2w98eHptSALTqxQ0b4P6Mer53Qj5keTPzyvifPA2j6KRrud8DjVw0pr9x0OaWPDFqkbbMwaAzyVFoAG9_hLclnvlxwRFfB1A0ysE23bBN8QcLvrowpfgait9K_6KHvB_5EGUHfqqEcOfIgVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برچسب انگشتی، پایش مداوم داروی پارکینسون از طریق عرق را ممکن کرد
🔹
پژوهشگران یک برچسب نرم برای نوک انگشت ساخته‌اند که بدون نیاز به باتری، میزان داروی «لوودوپا» را در عرق بیماران پارکینسون به‌طور مداوم اندازه‌گیری می‌کند. این فناوری می‌تواند به پزشکان کمک کند تا دوز دارو را به‌طور دقیق‌تر و شخصی‌سازی‌شده تنظیم کنند و بیماران را از بستری‌شدن در بیمارستان بی‌نیاز سازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/680488" target="_blank">📅 09:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
هشدار سازمان غذا و دارو: با توصیه هوش مصنوعی دارو نخورید
🔹
حتی دارویی که برای یک بیمار کاملاً مناسب است، ممکن است برای فرد دیگری به دلیل تداخل دارویی، منع مصرف، حساسیت یا شرایط خاص بالینی نامناسب و حتی خطرناک باشد. بنابراین نمی‌توان یک پاسخ عمومی تولیدشده توسط هوش مصنوعی را معادل نسخه یا توصیه دارویی شخصی‌سازی‌شده تلقی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/680486" target="_blank">📅 09:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680483">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed5443e66.mp4?token=SHsLuOwgdJEajbMj6E02j7C4A6hBDWQuKvPqMNWTt6Gf_Y4obi5H-m07VfOtgAUEKkSLcwFipc3OQLUovQjSEwcBUFyLjDYdu1N-8_ndXC1J_qIqib482fEf4STFFWlyApAUwTABsF20maTje3v6fbD2cy8CsiP9y9hOjcTBwsZ9CZGI_b3hKcmbY72pcS82iDzotZiiriSzj3phTMQifnTKCu5T0cuNrd2K10Lnsw0Yzd0o36t9uQU9L6_9-PblUkSOO5H3arJZ6UzrP5Hdje_NQFV8o52O8u5muPsASrDmbJ7Mv05CbK0D_e2mSeWjmY0Lf9mX_G2JdXgByiqJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed5443e66.mp4?token=SHsLuOwgdJEajbMj6E02j7C4A6hBDWQuKvPqMNWTt6Gf_Y4obi5H-m07VfOtgAUEKkSLcwFipc3OQLUovQjSEwcBUFyLjDYdu1N-8_ndXC1J_qIqib482fEf4STFFWlyApAUwTABsF20maTje3v6fbD2cy8CsiP9y9hOjcTBwsZ9CZGI_b3hKcmbY72pcS82iDzotZiiriSzj3phTMQifnTKCu5T0cuNrd2K10Lnsw0Yzd0o36t9uQU9L6_9-PblUkSOO5H3arJZ6UzrP5Hdje_NQFV8o52O8u5muPsASrDmbJ7Mv05CbK0D_e2mSeWjmY0Lf9mX_G2JdXgByiqJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعداد کشته‌های زلزلهٔ کلمبیا به ۲۲۴ نفر رسید
🔹
تعداد کشته‌شدگان زلزلهٔ ۷.۴ ریشتری دیروز در کلمبیا به ۲۲۴ نفر رسیده است. کلمبیا این زمین‌لرزه را «فاجعهٔ ملی» اعلام کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680483" target="_blank">📅 09:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680479">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade0fc751a.mp4?token=sJyfWrWG7n6jXADmwSidMJgNFMpOPPTi4Ogl8ob52T87N9hatRlaiYxGh9oWk1rfI9WKjmiOrUgN_hbkELpRs3eWYJRmC0vJpxuOtvD8fT1l4LwwceKnmRxSsbPBV3_remYLv-cNjBYNZ42uwq4_eQq_XhVzMEBIIeZIzprOIPgctfctjUnQkn1A59KULT3N8oxslwcD2DWdr0PcNK-V-8fWA8i4qC6dxinhODeHZIV1ehZxzedIv9l2ZrePjNaagM3tpBPKwWVES4DhFscBWgXKdHBq8VtUx39thqekjdvEHzEM31k8R3-hxAwIqwfepqrwwVFWaYC5BQv39Wb5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade0fc751a.mp4?token=sJyfWrWG7n6jXADmwSidMJgNFMpOPPTi4Ogl8ob52T87N9hatRlaiYxGh9oWk1rfI9WKjmiOrUgN_hbkELpRs3eWYJRmC0vJpxuOtvD8fT1l4LwwceKnmRxSsbPBV3_remYLv-cNjBYNZ42uwq4_eQq_XhVzMEBIIeZIzprOIPgctfctjUnQkn1A59KULT3N8oxslwcD2DWdr0PcNK-V-8fWA8i4qC6dxinhODeHZIV1ehZxzedIv9l2ZrePjNaagM3tpBPKwWVES4DhFscBWgXKdHBq8VtUx39thqekjdvEHzEM31k8R3-hxAwIqwfepqrwwVFWaYC5BQv39Wb5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم مراقب خرید طلای آبشده باشند
رئیس اتحادیه تولیدکنندگان و صادرکنندگان طلاوجواهر:
🔹
برخی به دلیل کارمزد کمتر اقدام به خرید طلای آبشده می کنند که به دلیل نامشخص بودن عیار آن، خطراتی به همراه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/680479" target="_blank">📅 08:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680476">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: من به ایران اعتماد ندارم، من آخرین کسی هستم که به ایران اعتماد می‌کند، آنها دائما به من دروغ گفته‌اند
رئیس‌جمهور آمریکا مدعی شد:
🔹
ما در حال حاضر کنترل کامل تنگه هرمز را در اختیار داریم. آنها کنترل آن را ندارند؛ ما کنترل کامل را داریم. تنگه هرمز مال ماست.
🔹
شاید در مقطعی آنها دست به کاری بزنند و آن وقت نابودشان می‌کنیم. اما در حال حاضر، ما در موقعیت بسیار خوبی قرار داریم.
🔹
ما با کشوری روبه‌رو هستیم که ۵۰ سال قلدر خاورمیانه بوده است. اگر دقیق‌تر حساب کنید، در واقع ۵۱ سال است، درست است؟ ما چهار سال است که می‌گفتیم ۴۷ سال. اما آنها دیگر قلدر خاورمیانه نیستند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/680476" target="_blank">📅 08:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680470">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e163d5cec.mp4?token=eJ9fMa2anCaTa7c-7gC8BlLXgO-h5j_JzwveON-NPnApRrsdVOY7gjau9gsjOZ4v2B34uzlWbMncZJzRlooIeUwznJ2YX3hM1Qar459LI85NYu3it3Ss6e222qIykkW6H8OEOA6VP1KtN6rRm8R1PTIdr64sCTKM6MMVWL585bBtVlujroRBcZp1KNv36vWWeQhCEY7AoI7S1jV-cbCDIDABM3GhkNXUWSLG_jsMFcc1zOYxe2GLwzZ85XBhBN3lEmQdvpxGC6xLArb_6qaCugLfBCaKmAOdBNVm8D45Ut8sqL1oysdvDb02Hp23GjBWAYWE9vBHC15e9NtkGT--Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e163d5cec.mp4?token=eJ9fMa2anCaTa7c-7gC8BlLXgO-h5j_JzwveON-NPnApRrsdVOY7gjau9gsjOZ4v2B34uzlWbMncZJzRlooIeUwznJ2YX3hM1Qar459LI85NYu3it3Ss6e222qIykkW6H8OEOA6VP1KtN6rRm8R1PTIdr64sCTKM6MMVWL585bBtVlujroRBcZp1KNv36vWWeQhCEY7AoI7S1jV-cbCDIDABM3GhkNXUWSLG_jsMFcc1zOYxe2GLwzZ85XBhBN3lEmQdvpxGC6xLArb_6qaCugLfBCaKmAOdBNVm8D45Ut8sqL1oysdvDb02Hp23GjBWAYWE9vBHC15e9NtkGT--Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار و مفسر سیاسی آمریکایی: مردی که خودش را در کنار جورج واشنگتن و قهرمانان جنگ آمریکا می‌دید در یک خودروی آشغال پنهان شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/680470" target="_blank">📅 07:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680469">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e17cd8159.mp4?token=PkNkjExrRoS3USkb_7mO4n0jEm33ZF2gHsOn7H0DtDzd6sTeoaYXopWtexeWnJT5whuBaGJAXh_m8rVbkNSfSTE_p2SFs7eQ5-mb_ITnfH1ynKD3jEilVkSr0-2aaMNGlazG1hnfNxygxDA9biFFXnKK0TtKodYzhW7PrCVgX_K8Pqwtz-uJrm7ENaC6nBxk505R_hxxdsrIFGKOTQjxSQqj5mMq8D_FT4g8ePlRrXCBnNyNpKcoeZnMAlewSA6YazH3a2gOXQZVmUuvr3EMMSK_vaCFxA2VEkmRgHiaN_sHy4BDCYQ2tzEVm1KSjMbAmvcWB4Oefw1P_8r_AIrOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e17cd8159.mp4?token=PkNkjExrRoS3USkb_7mO4n0jEm33ZF2gHsOn7H0DtDzd6sTeoaYXopWtexeWnJT5whuBaGJAXh_m8rVbkNSfSTE_p2SFs7eQ5-mb_ITnfH1ynKD3jEilVkSr0-2aaMNGlazG1hnfNxygxDA9biFFXnKK0TtKodYzhW7PrCVgX_K8Pqwtz-uJrm7ENaC6nBxk505R_hxxdsrIFGKOTQjxSQqj5mMq8D_FT4g8ePlRrXCBnNyNpKcoeZnMAlewSA6YazH3a2gOXQZVmUuvr3EMMSK_vaCFxA2VEkmRgHiaN_sHy4BDCYQ2tzEVm1KSjMbAmvcWB4Oefw1P_8r_AIrOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش کاربران خارجی به مخفی شدن ترامپ در کامیون آشغال
📲
🇮🇷
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/680469" target="_blank">📅 07:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680464">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
واکنش کاربران خارجی به مخفی شدن ترامپ در کامیون آشغال
📲
🇮🇷
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/680464" target="_blank">📅 07:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680463">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAtlFrZK6ER2_WB8_sfDxgBd4XlvAId--W6hwV4E81dtjRTnxPCtAkPmX0QCfDedS45kSsv65FcXYUSvifTi5tiOMCtijJbNfkRncyX8ce99LHWcI1qcbdv7-BSNeK7Kke3SDq09CCoU52GMK_ZPetoo8xN18Zm6Rgsco7uUIG5OCV-d0XGvTs0yIFgKm3ydnJu5zLFlrXeF_1ohbNbdrhXt9WJgsIYFZR5gnymiCUjjgfHMQNjJ85wfc4jdOpQiMqM0VDmGVnfG1gFV_RJFip9Lyy3482hfc7LIPvJ6mGbwkga4Zxnhj5MKUgndSEXt-2XXcZcrDoshmutXHvujXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۱ مرداد ماه
۲۸ صفر ۱۴۴۸
۱۲ آگوست ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/680463" target="_blank">📅 07:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680456">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5171ee4322.mp4?token=PNP5eQpDWG5ZJaC2aCLMtnsx3CAAKfYd3uHOUFUHRrP7hBP24Frp1fIaMdHyUPNGkWNRKRV2cBKCQkj6eUWTzNzHau5OOsorDCECf46qbpamzT3iq99ZIOI_VFYMgBe7TWjmH903JeYi6b5EGjfWq6MJbT-Pq72zCOhd7uD6Murm8KwcMROxL-gan7nIV5XnG4dNVK7v5ts6sFZp5IgyrbH3TRuASzXVj93ZGeN5-EwJ77yAviAUHMpH2TPT6QNVAaeG6SwYlK6OyU_ys-fNs6mSbUyyja8ii5X2lg9dNMfKM927lqNeqHspX6IyuWUoKsU0QVppss_E3jJyrwpU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5171ee4322.mp4?token=PNP5eQpDWG5ZJaC2aCLMtnsx3CAAKfYd3uHOUFUHRrP7hBP24Frp1fIaMdHyUPNGkWNRKRV2cBKCQkj6eUWTzNzHau5OOsorDCECf46qbpamzT3iq99ZIOI_VFYMgBe7TWjmH903JeYi6b5EGjfWq6MJbT-Pq72zCOhd7uD6Murm8KwcMROxL-gan7nIV5XnG4dNVK7v5ts6sFZp5IgyrbH3TRuASzXVj93ZGeN5-EwJ77yAviAUHMpH2TPT6QNVAaeG6SwYlK6OyU_ys-fNs6mSbUyyja8ii5X2lg9dNMfKM927lqNeqHspX6IyuWUoKsU0QVppss_E3jJyrwpU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع آتش سوزی بزرگ در اربیل عراق
🔹
علت حادثه مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/680456" target="_blank">📅 01:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680455">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-q5aft8N8AggG0ih-WwRg05oUuvuQK2pNX8cmTebvQXsB3QoflhIQAsV93-cwYwe2_M1wAb0LWwXzsyQGDaVg6QZqRE0RbBp3JTpNl2RyOohAOo7pj7P0IWcfBUGVRJfU5gl2HBSj6mCOowstJF0t-hbKD5Yh0pykI9DuhrZ_Gd_F0QtKMECeijtaoRHVvXth_H6tM4joOWeWSZ0MKrfrm-R1TgAU7Ix5ulI5vQNcpf53WX5pchr80nIAWrLoMrFOrAoc8MqaqveMfViE-8--MUJYzLMNJxw3chw-rlE_Dti6ncZQE_r_h9MffQ_3EPW6OG2Vi_pZh9MCiZmw6sEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: کاش رئیس‌ جمهوری داشتیم که بزرگترین جوک و مایه تمسخر تمام جهان نباشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/680455" target="_blank">📅 01:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680452">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPzaGxNajwcm_Y0JhuKcHKBzBrhxWES2iDxN2RFC89Oq_L4tpB818Vk7qpx_KzwFCpu7K_p-33hb0qzq5PZ7dYBMlJMD1xyZTK3f3_nkksLeS8eMYfRSE2xj40nuCDBMrP53lA4BwFXyAZTgtWehMUgZXwettixfX5DviDPGmX0FCxntDcqCk4emK9BIsoU--y-qThGjOxreTZYuc8O8xRFyUzMEBugeEEtTrHYAh0x1fX11T8dBKa7Ge9sHZdRmIDkI_4SmEgnqGVKjQXwZRHZZkYCl6cmbrFf4py8qrI3_FU6m0182WVuaYQ0GdQk_xb-lgAcekJKRG5ogzpCOtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر ژئوپلتیک آمریکایی: توازن قدرت در خاورمیانه به‌طور دائمی علیه آمریکا تغییر کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/680452" target="_blank">📅 01:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680449">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3b82593b.mp4?token=iRyBsajB1p7PNKUI6AeLCeYyeUOBMz54DAG6JQ8untjNQjcHUjG2LDu4911qaH2oRgKtiIR2DdTflAkSc_AU1ToFsYOj-m0EbfIY_OR1iUtvNitoaUxnV8xXoa_cBeI6uNy6Dr4XeI3OatjHpA7KKmI7b5ReZw5yNxFjs5X5WxGpO8oOnqpxjB4ae_ftYaADYmBpESrlWU3u2blgFK6shaB0mXQJzeViXqkS2ATgNeV_RPEBoPnah-R73_VMOEYFockylAhaQK3TsAsrRCq9gVk3uw7aUaevGqlyPPCoyJEXk-mjUu364_Blwb1AdXyWt40Dcx_dB7MtK4fuBsD9qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3b82593b.mp4?token=iRyBsajB1p7PNKUI6AeLCeYyeUOBMz54DAG6JQ8untjNQjcHUjG2LDu4911qaH2oRgKtiIR2DdTflAkSc_AU1ToFsYOj-m0EbfIY_OR1iUtvNitoaUxnV8xXoa_cBeI6uNy6Dr4XeI3OatjHpA7KKmI7b5ReZw5yNxFjs5X5WxGpO8oOnqpxjB4ae_ftYaADYmBpESrlWU3u2blgFK6shaB0mXQJzeViXqkS2ATgNeV_RPEBoPnah-R73_VMOEYFockylAhaQK3TsAsrRCq9gVk3uw7aUaevGqlyPPCoyJEXk-mjUu364_Blwb1AdXyWt40Dcx_dB7MtK4fuBsD9qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک یک سرباز روسی که با استفاده از یک سیستم شلیک همزمان، به یک پهپاد اوکراینی که در ارتفاع پایین پرواز می‌کند
🔹
این سیستم مستقیماً بالای کامیون‌ها نصب شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/680449" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680448">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=p4oBf9Ba0XFNhVOhpvZUJOnCVL34PIbOVVvhO1iQFfNTucUf4BHzOI6lgIhj955Xah0RaViWW6R174glOZxLXEuAKfrikk23NGnEE5ErBJmfFLpYrn5DhZTYDf_BfCEYrn9FtYT7HI34VvzTnx_7nhf-GyZY9sB2wdJ_Ec6161_LGdh3O91eWxMG1Yc8hptSxNfZ3EY_zmal6vY3CSVrpZF44mJm8PJ39hLKfTQyiCUR-ai6_pXDrmoDtvmrNkJmtRoyDq4AwudyGxlByxWidXdydh-lGW5T7fAoPa86EdHj1DNQn7IKdPdNhr1ummphTXSKSN4TAyxmy2IkjSVYvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=p4oBf9Ba0XFNhVOhpvZUJOnCVL34PIbOVVvhO1iQFfNTucUf4BHzOI6lgIhj955Xah0RaViWW6R174glOZxLXEuAKfrikk23NGnEE5ErBJmfFLpYrn5DhZTYDf_BfCEYrn9FtYT7HI34VvzTnx_7nhf-GyZY9sB2wdJ_Ec6161_LGdh3O91eWxMG1Yc8hptSxNfZ3EY_zmal6vY3CSVrpZF44mJm8PJ39hLKfTQyiCUR-ai6_pXDrmoDtvmrNkJmtRoyDq4AwudyGxlByxWidXdydh-lGW5T7fAoPa86EdHj1DNQn7IKdPdNhr1ummphTXSKSN4TAyxmy2IkjSVYvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پارسال همین شب‌ها؛ خادمی سردار شهید تنگسیری در حرم رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/680448" target="_blank">📅 00:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680447">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27b1027df.mp4?token=P-cVOjHBWyYs3UQ-d3wqAUmMBaJXs_IfnGeWMnygTEv1HENUshZt7i_KJ13gQpZxkMjARDYNFiYOiKXE87L08FBNcKLfO2u2IUZh4zVAL6UIl3AGlqNW4OuDpXQ14-S1QlJHTtX4NwNrhq8QhqQePzs3TxgeDN4PoJJjvZNAWIP5RFg-zztaA0W7kdiDTIraqqlO8SYi_63zFpUtyemfufSU4AK53Wugs_uZS9rOOWOOcwW0eyPbKZr_C6xigHVOolOhvXfpR01CPM3O7-MDAABTBf-7vM0HM9I9A8jdb-OBe-HwwHL2cvJHmM3lhKOc832StTU7inal4hs4faSo9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27b1027df.mp4?token=P-cVOjHBWyYs3UQ-d3wqAUmMBaJXs_IfnGeWMnygTEv1HENUshZt7i_KJ13gQpZxkMjARDYNFiYOiKXE87L08FBNcKLfO2u2IUZh4zVAL6UIl3AGlqNW4OuDpXQ14-S1QlJHTtX4NwNrhq8QhqQePzs3TxgeDN4PoJJjvZNAWIP5RFg-zztaA0W7kdiDTIraqqlO8SYi_63zFpUtyemfufSU4AK53Wugs_uZS9rOOWOOcwW0eyPbKZr_C6xigHVOolOhvXfpR01CPM3O7-MDAABTBf-7vM0HM9I9A8jdb-OBe-HwwHL2cvJHmM3lhKOc832StTU7inal4hs4faSo9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند گاز خونت را مثل روز اولش کن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/680447" target="_blank">📅 00:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680446">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
درخواست محرمانه عربستان از یمن برای پایان درگیری
🔹
در پی ضربات موثر انصارالله به مواضع ارتش و مزدوران سعودی در یمن، ریاض در پیامی محرمانه به هیئت مذاکره کننده یمنی ابراز داشته که خواستار پایان درگیری و بازگشت به توافق سال ۲۰۲۲ ریاض-صنعا بوده و این درخواست را به هیئت یمنی منتقل کرده است.
🔹
این درخواست با مخالفت مقامات انصار الله روبرو شده است. صنعا پس از دریافت پیام عقب نشینی ریاض از مواضع خصمانه اخیر تاکید کرده است که به دنبال دریافت تضمین‌های جدی و واقعی برای تامین منافع ملت یمن به ویژه در مورد پایان محاصره، دریافت غرامت و پایان دادن به مداخلات عربستان در امور داخلی یمن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/680446" target="_blank">📅 00:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amq3TYxnD71vXd83DZc5UHPvDoLVwccrf8MHOP7an1qHYGtu6N59Ea9o5RovnU_STOBkNUJ27hN8CrJF9ub_qBLO_LBRYuLCcWMxibNSKENY71OSk6lOvJmm1M8SylZZKqsmfDV5SYomN4BrDore_7GoSQbmgPLKfXo8cO8xXAY4COCtu0qyg_JOSwRgiBJZWOJe4NCwoj72utGuaXpsnH7K4kYaqNKaH2yugC2jI-ReWT84bOpP0_ttGl2mKtl6gxZXAMJE4tDFpuG9K73PpOEQ2PHm8pTsZAzKIIrumBZv1Ojqzvi6lGffXB225zm01fiDIZudfjcCan4LYsT1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/680442" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680434">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
سردارنقدی: تولیدات موشکی و پهپادی ما تمامی ندارد
🔹
ما بیش از نواخت شلیک موشک‌های بالستیک تولید می‌کنیم و به دست رزمندگان اسلام می‌رسانیم. در حوزهٔ پهپادی نیز قابلیت تولید ما بسیار بیشتر از نواخت شلیک است.
🔹
اگر جنگ چند سال هم طول بکشد، باز هم موشک‌های بالستیک…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/680434" target="_blank">📅 23:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5981ac86.mp4?token=kc51Et97SxnEeoz0DsEINHVmEByflJbVMJkQH1s1Q32e3tX5wj1OhDUffdCY0iOKydK6LLO4Gd_Q-32kZ9UyCDKNfVgZ-K5piMON2uGt9p9KulXl_EPl3BO81uYWmTr4BuNpagWfrrpCM6NsNwi_h20WUWoe-VxvJgUmq1zdXgwcyKozLRfxG4UIfU3rr1W-lvIz2ReDGeT0kdXhLGATtyNkYIHX5dO7r8BGk9WQPVFgigMYVgsNLr_3puAZEBqRE9xLw2T8hEsKq1IPDC5rAA-Rgik7MODrLgmknZC2JqmssMyKODi23jQr8ccKYXIg5uNciGhzuVSg1hSj7uKqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5981ac86.mp4?token=kc51Et97SxnEeoz0DsEINHVmEByflJbVMJkQH1s1Q32e3tX5wj1OhDUffdCY0iOKydK6LLO4Gd_Q-32kZ9UyCDKNfVgZ-K5piMON2uGt9p9KulXl_EPl3BO81uYWmTr4BuNpagWfrrpCM6NsNwi_h20WUWoe-VxvJgUmq1zdXgwcyKozLRfxG4UIfU3rr1W-lvIz2ReDGeT0kdXhLGATtyNkYIHX5dO7r8BGk9WQPVFgigMYVgsNLr_3puAZEBqRE9xLw2T8hEsKq1IPDC5rAA-Rgik7MODrLgmknZC2JqmssMyKODi23jQr8ccKYXIg5uNciGhzuVSg1hSj7uKqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)| حاجت‌روا
🔹
صداهایی از جنس امید؛ روایت شما از کرامت و نگاه ویژه امام رضا (ع) در زندگی.
🔸
الوفوری را دنبال کنید
👇
#حاجت_روا
@Alo_fori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/680432" target="_blank">📅 23:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSJ6VPfK7UN7zgJuArVzchuabRlG9W-m2dIRyluHQR1iZ6n9MVE9btCwGDKz9hHJsVZvcZbMtloYHDEFHQ4iXZVa6_XGbWejXbQeWOkXfghZ6Nm4G2nbEy30TDqYbFCgZgYXoYeXgO-Tili5_sgaEht_BlL2-0snI-SwQ44INTUT4OUyeQBQt_3y_WENNvtm-dYwFU7xPmWdeqmPkqpYdlUppbY_u5cYweNb2sV4i3IgaqPrtyoOd_6m0b2sMxDSbKdQHzN-tw9mLy5ULJAX-7QZGBabhyBK3q8IOW0AjisG94VjXXmGONCXkUWJ2GzJ9McYpwfbkydabIiT10dAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ری اکشن جالب یک مخاطب به رفتار دیوانه وار ترامپ
🔹
بزار ببینم‌ درست متوجه شدم ؟
🔹
ترامپ صدها دختر دانش‌آموز را کشت، سربازان آمریکایی را کشت، صدها نیروی نظامی زخمی کرد، قیمت بنزین را سر به فلک کشید، ذخایر موشکی ما را مصرف کرد.
🔹
همه این کارها برای این بود که در نهایت به ایران اجازه دهد کنترل تنگه هرمز را به دست بگیرد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/680431" target="_blank">📅 23:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823f7565ed.mp4?token=qBrBToiMtckkbJTe1WucKYwWb-c6_a0m8S14fibkedCBJVPVhTE17pczTVJAcRtcdJ5DFoOXShOgqDLH7shmPV1bRbPoEZfbTXqrk5M119xEJ41I1EPw1D4Ty9OrFAuJSZeWfpFHWKgOqBWaIpWJUkZavtRn00c3AlUFjoECyZzdDj8jX9vzvDoAeeXP390kxxQUYruxsGVS3f-BvyEv3tOaZ4JTb52IKiC8vlO7XWsuRF8tcjntumq2Hm_7yLviwuvz-lATMZxwAqmwId2EZvAUfuS9rEccJFT1LvEh_8EMzEsbEJQBODRP4llCjWo7m66r-keoK03zSirONqTSQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823f7565ed.mp4?token=qBrBToiMtckkbJTe1WucKYwWb-c6_a0m8S14fibkedCBJVPVhTE17pczTVJAcRtcdJ5DFoOXShOgqDLH7shmPV1bRbPoEZfbTXqrk5M119xEJ41I1EPw1D4Ty9OrFAuJSZeWfpFHWKgOqBWaIpWJUkZavtRn00c3AlUFjoECyZzdDj8jX9vzvDoAeeXP390kxxQUYruxsGVS3f-BvyEv3tOaZ4JTb52IKiC8vlO7XWsuRF8tcjntumq2Hm_7yLviwuvz-lATMZxwAqmwId2EZvAUfuS9rEccJFT1LvEh_8EMzEsbEJQBODRP4llCjWo7m66r-keoK03zSirONqTSQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: پیروزی ما حاصل حضور مردم در میدان و نفوذ در جهان بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/680430" target="_blank">📅 23:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5tYcpeTkLQKidzLjfUnfKiTMiCpL14x2rYKjM7qgU3MX1xnO5S-OKnfSjB0bMEfEGIdF1M2PgKhaFlxWQRyC8N60ocCqqdeTYqPCauTEMtJSX5r31qhKR783xYEYtFnuwHs-FvNem7w4lDEi4ptEppwuKKVIaD3oLmMzKJaQ-0Hf5UD5C_gta4ITGDrLINT2fHXzu2aXLJcVqRyKqofcGVm9g9Kk_LxSKa-A76_8GGhWOBkmu8bP3ISeBlxmF00Et3snZWMlGSzCcLkZscQKsLZs81bUhfJuTZbuZfGIUYdIQnKttjAcbm4LAD2-Y4aTAdHirMqk19zt-3sLhTYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی رونالدو برای ازدواجش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/680429" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
محسن رضایی شروط بازگشایی تنگه هرمز را اعلام کرد
👇
khabarfoori.com/fa/tiny/news-3237163
🔹
ترامپ چگونه در یک عملیات مخفی از ترکیه خارج شد؟ | فرار با کامیون غذا
👇
khabarfoori.com/fa/tiny/news-3237044
🔹
عکس های خانوادگی حمیدرضا رجب زاده مداحی که به قتل رسید
👇
khabarfoori.com/fa/tiny/news-3236968
🔹
محاصره دریایی از جنگ هم بدتر است و باید بشکند
👇
khabarfoori.com/fa/tiny/news-3237132
🔹
بشار اسد به اعدام محکوم شد
👇
khabarfoori.com/fa/tiny/news-3237066
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/680428" target="_blank">📅 23:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200c140ffa.mp4?token=N6q7YURVHJiRh1spcRxhVzS13_chJRXwT2VSXfst-LjYwy2JoUptc4dtPaCrc2kCreQV_CaROk0zH6sbb4wfNW9sUuPPpsLDBAFNAR9_zjmE_ITSzuWSwQ997i3OQBzlv2-HsZt2602yx_VuT_ax-jFWBdD-FNYKIbCfPWBu3GVb50krVk857jRKhDtcsD19VMK0o8AnCrT0FKKb66ynDJNKVlcAzv3LITUPjpsnzImxy7GxQ_XADsw7i7JjelzEoPWEqPnKFLVkB2VXXIOQIcr_BljDZo42q2kFESVgJ_fXAbXcF5HI87jFVyuxpW44C4TAPZNIf3um6rlZIcV8TDXPcHuzE17VKtg01Yh7yJqNesX-RgdsL6J-8odzE79UtQVg2d9tMn5JTqla-MHuGq1sOqfZYQ693ds_NncFQTSy3tTliGBbwrggmEfwCyK4p7CUfERyCaC6C2gUo9mpN6AXYhaOR7ORR0oRuuGEeUqCjdw2ze199vZqhAJRB-XgHYckwUjvm1ssRB_daAlFfTfTSOn96h76vmtn8tF48Gq0ZOlj9C9pJF7jIvLN5Sg5HzJFeyr6itJzJhgAtbhxsRLFXqJmMeUVl1pUWRwC08CF2eYZaASjTiXFyTq7g-RINKp3UpWPbZbAKx41rzY9egO-BjCZ1Py9NRze7-YGUcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200c140ffa.mp4?token=N6q7YURVHJiRh1spcRxhVzS13_chJRXwT2VSXfst-LjYwy2JoUptc4dtPaCrc2kCreQV_CaROk0zH6sbb4wfNW9sUuPPpsLDBAFNAR9_zjmE_ITSzuWSwQ997i3OQBzlv2-HsZt2602yx_VuT_ax-jFWBdD-FNYKIbCfPWBu3GVb50krVk857jRKhDtcsD19VMK0o8AnCrT0FKKb66ynDJNKVlcAzv3LITUPjpsnzImxy7GxQ_XADsw7i7JjelzEoPWEqPnKFLVkB2VXXIOQIcr_BljDZo42q2kFESVgJ_fXAbXcF5HI87jFVyuxpW44C4TAPZNIf3um6rlZIcV8TDXPcHuzE17VKtg01Yh7yJqNesX-RgdsL6J-8odzE79UtQVg2d9tMn5JTqla-MHuGq1sOqfZYQ693ds_NncFQTSy3tTliGBbwrggmEfwCyK4p7CUfERyCaC6C2gUo9mpN6AXYhaOR7ORR0oRuuGEeUqCjdw2ze199vZqhAJRB-XgHYckwUjvm1ssRB_daAlFfTfTSOn96h76vmtn8tF48Gq0ZOlj9C9pJF7jIvLN5Sg5HzJFeyr6itJzJhgAtbhxsRLFXqJmMeUVl1pUWRwC08CF2eYZaASjTiXFyTq7g-RINKp3UpWPbZbAKx41rzY9egO-BjCZ1Py9NRze7-YGUcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر مقاومت کردید، آن وقت قلّه را فتح خواهید کرد؛ کاری که از بعد از زمان رسول خدا تا امروز انجام نگرفته، این کار، کار شما است.</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/680427" target="_blank">📅 23:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6cb1de1d.mp4?token=M7ev7awuO_1RUqYl2jRFUcjJGqXe5AxUrljIYevPSGuHwSFClujLipd9ZSl2M01OwC53POuWFnvu_4KhuAz6bGo8GTnDIfWolB-anVtlaiJd1fpaqiauNxZUwK4goAswdv9KKRrh1xjE3aC_7jIZ1U0KDW8oJL4G4DzQ75EX7hZP3VXCjHE_8wWZ4Ps_BxxXnicqeSK9PA8hhbH295Ka2BD4Hn2rFUvzf7y7hBlTR7eXzQP28cOsg9VkZuWnH7NAfoTZlPjzv4ZDhjAXgpR80WlThlhCqIxIXl8kXISl34rXPcGhpfU4jS8rvRRmjOLflI5QhCEO2Ce8gMo5uYrP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6cb1de1d.mp4?token=M7ev7awuO_1RUqYl2jRFUcjJGqXe5AxUrljIYevPSGuHwSFClujLipd9ZSl2M01OwC53POuWFnvu_4KhuAz6bGo8GTnDIfWolB-anVtlaiJd1fpaqiauNxZUwK4goAswdv9KKRrh1xjE3aC_7jIZ1U0KDW8oJL4G4DzQ75EX7hZP3VXCjHE_8wWZ4Ps_BxxXnicqeSK9PA8hhbH295Ka2BD4Hn2rFUvzf7y7hBlTR7eXzQP28cOsg9VkZuWnH7NAfoTZlPjzv4ZDhjAXgpR80WlThlhCqIxIXl8kXISl34rXPcGhpfU4jS8rvRRmjOLflI5QhCEO2Ce8gMo5uYrP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه پاسداران: سپاه باید آماده عملیات هوشمندانه در خاک دشمن باشد
🔹
هر موقع اقتضا کند و فرمان صادر شود، باید بتوانیم عملیات را به خاک دشمن، به سرزمین‌های دشمن بکشیم و دور از سرزمین خودمان بتوانیم عملیات انجام دهیم.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/680426" target="_blank">📅 23:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac585917.mp4?token=DIBfvQpPoylk2etr_Avck46CH3SQ_jq7qwuZXjBxB4jLwgkuN-oCLog4bK30SIWvHt2Qx4Z-rxNzRf7aZJWWT6COzFI4T6b_y5A0ChXOlkV3oUSced20IIjUBScUrztlhpoRlbOW3BCKKhmnEF3XSK7gVerAMFopBuXrAaiNeBhRE86tm2-kxGSiepPEyigunUSS5gCtA-ZC9WlTFKuyg7D5HtaE7FWrpY5RYctYuD-2nOmH22LrYZoEcTJylsuTAM-paJYuvbv0bqTTHBPbouxGO0zJkDorsAdUasP53QcFI_BYC21DJTvhoeV1fBITeKHudIlaG4QIwmWswSQpzLhHWmbPTMpjxILQ_T2Xo8queSIgRnehO5AKuONyumQVCskxChiZqBprVg3EHen4O5QN2sWnjUqikufetCWehVYW_rtqM0lsn6KM0Hm3-Zm5B5ZPDMOeXbmK7nBPTBbVMmoDlx5UZzyFe-0TKAKcbjwwvBwzezojQsKGhljkLEHv_gOAKBEayR-CHQJQFtCoJXLbFgthDts1TrWeBHfYSXRxFVG4RVjTLN2VE1UTPIEU-SKdwNJs0ENsFbVfcYJzt9_XRni3pgwbGeYeT1Z-1wu9GxsoRxxhUjPzsEKFZpgEo78I2m1BPJ3R-l0SQeqdilMrpDMiEuk8_fRzugAr-Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac585917.mp4?token=DIBfvQpPoylk2etr_Avck46CH3SQ_jq7qwuZXjBxB4jLwgkuN-oCLog4bK30SIWvHt2Qx4Z-rxNzRf7aZJWWT6COzFI4T6b_y5A0ChXOlkV3oUSced20IIjUBScUrztlhpoRlbOW3BCKKhmnEF3XSK7gVerAMFopBuXrAaiNeBhRE86tm2-kxGSiepPEyigunUSS5gCtA-ZC9WlTFKuyg7D5HtaE7FWrpY5RYctYuD-2nOmH22LrYZoEcTJylsuTAM-paJYuvbv0bqTTHBPbouxGO0zJkDorsAdUasP53QcFI_BYC21DJTvhoeV1fBITeKHudIlaG4QIwmWswSQpzLhHWmbPTMpjxILQ_T2Xo8queSIgRnehO5AKuONyumQVCskxChiZqBprVg3EHen4O5QN2sWnjUqikufetCWehVYW_rtqM0lsn6KM0Hm3-Zm5B5ZPDMOeXbmK7nBPTBbVMmoDlx5UZzyFe-0TKAKcbjwwvBwzezojQsKGhljkLEHv_gOAKBEayR-CHQJQFtCoJXLbFgthDts1TrWeBHfYSXRxFVG4RVjTLN2VE1UTPIEU-SKdwNJs0ENsFbVfcYJzt9_XRni3pgwbGeYeT1Z-1wu9GxsoRxxhUjPzsEKFZpgEo78I2m1BPJ3R-l0SQeqdilMrpDMiEuk8_fRzugAr-Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان فرار مخوف شرور مسلح در عملیات مشترک پلیس
🔹
معاون مبارزه با شرارت پلیس امنیت عمومی فراجا از دستگیری شرور مسلحی خبر داد که پس از شلیک به یک شهروند، با تهیه گواهی فوت جعلی تا مدتی با هویت جعلی در ایران زندگی می‌کرد اما سرانجام در عملیات مشترک پلیس امنیت عمومی و پلیس فتا دستگیر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/680425" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/894ec0af40.mp4?token=m4nHRzyYAYpmhOQ9fuUb36lJ5pCMmeTCIyM5wrIw2YMCmvqk6FP5uNIODWJOFrmOUF8gfHxh3PPOB7sKYnA5cnxf6wWUtGn5RVYgmaEwZOpK7m8JU1UGHvHwO85MZb4qsRrI7iULHX47ny7R0gcs0R7fXwCIIozbqVZg5fgf8hvI010mvbaSV8PYIG2AJKQguNathZP2CF4IGCyCBVCaBIbBu7-K_c1I9AnbY1nPZa3-t3_bIN7_x4uHLPojxRQaP1NPdu6ZxVL7cx8ahpzohwlGEcWbjrFfy6HXHFPE542MOKdsVRaNng3fYL3Ax4DLP3XE_Z46GrT0GgibrfYUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/894ec0af40.mp4?token=m4nHRzyYAYpmhOQ9fuUb36lJ5pCMmeTCIyM5wrIw2YMCmvqk6FP5uNIODWJOFrmOUF8gfHxh3PPOB7sKYnA5cnxf6wWUtGn5RVYgmaEwZOpK7m8JU1UGHvHwO85MZb4qsRrI7iULHX47ny7R0gcs0R7fXwCIIozbqVZg5fgf8hvI010mvbaSV8PYIG2AJKQguNathZP2CF4IGCyCBVCaBIbBu7-K_c1I9AnbY1nPZa3-t3_bIN7_x4uHLPojxRQaP1NPdu6ZxVL7cx8ahpzohwlGEcWbjrFfy6HXHFPE542MOKdsVRaNng3fYL3Ax4DLP3XE_Z46GrT0GgibrfYUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی، مشاور عالی فرمانده کل سپاه پاسداران: سپاه باید آماده عملیات هوشمندانه در خاک دشمن باشد
🔹
هر موقع اقتضا کند و فرمان صادر شود، باید بتوانیم عملیات را به خاک دشمن، به سرزمین‌های دشمن بکشیم و دور از سرزمین خودمان بتوانیم عملیات انجام دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/680424" target="_blank">📅 23:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680422">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7f7e509f.mp4?token=PU3gkR1_J2KP3zRMXWZvj424Vh89jACp0qCaSwOHRAghWEikf5XW-vSi-x0Md4ppNVW6ayCs79eTvdtjJCtHhKJu7uxyKEUzXGRMTsu1FZ9B6E33-wh9ZyE-ENCZi8I4f53KRIb7DjSCujU70xBumAeRgPAMlxdddXVEWFIy8ePSgtXha2UEhQCzUxJ44N_DjYf92GXMAfJUfPpy5PyGpe2Emp1VzTOk4eCM4BMT1GmimYTZFKpHAT16-lHRUAFihasTPHsKZsvJDaE6veuRU5jgDK_3p7hNS8rBpOQxcfynk3991irjMy2AMZSj0y4DcrbcbGT0IqZceeL2qXH-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7f7e509f.mp4?token=PU3gkR1_J2KP3zRMXWZvj424Vh89jACp0qCaSwOHRAghWEikf5XW-vSi-x0Md4ppNVW6ayCs79eTvdtjJCtHhKJu7uxyKEUzXGRMTsu1FZ9B6E33-wh9ZyE-ENCZi8I4f53KRIb7DjSCujU70xBumAeRgPAMlxdddXVEWFIy8ePSgtXha2UEhQCzUxJ44N_DjYf92GXMAfJUfPpy5PyGpe2Emp1VzTOk4eCM4BMT1GmimYTZFKpHAT16-lHRUAFihasTPHsKZsvJDaE6veuRU5jgDK_3p7hNS8rBpOQxcfynk3991irjMy2AMZSj0y4DcrbcbGT0IqZceeL2qXH-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: تشییع رهبری اگر در نیویورک و لندن هم انجام می‌شد، میلیون ها نفر شرکت می‌کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/680422" target="_blank">📅 23:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680418">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/839e31ae75.mp4?token=NOWhgm0Z_wL7N2WiajSzZKamRMcOZILFyrUe3Vs3Gz7xbuksY_Ukh9hyedqQJFEyU-ctRIy6Xa_CHUZOoFqQk7WoJI4yQkEdltr0OZp_vegdZUx1PaRpP8sfZRCCUH9zP55u4vP5nqYqw2qZQSIwxhvfFxBnaTyhG1OGA8O0oShj9efcXVzHGCjAN9iHedu3mdbvL0IEvx_JT7KriDiS4b8O10dKlMvcKtQjOx_0cm7J5jv_ZCb-ZudSupLtOpuoq-rP9Y2m7y-HAfEocL5QAi_qxVINOHZ7DETo3H8oVzBOuZM8eJzSX5EnO_QPKtv3IkImhO8dVQotLuUGrvIK6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/839e31ae75.mp4?token=NOWhgm0Z_wL7N2WiajSzZKamRMcOZILFyrUe3Vs3Gz7xbuksY_Ukh9hyedqQJFEyU-ctRIy6Xa_CHUZOoFqQk7WoJI4yQkEdltr0OZp_vegdZUx1PaRpP8sfZRCCUH9zP55u4vP5nqYqw2qZQSIwxhvfFxBnaTyhG1OGA8O0oShj9efcXVzHGCjAN9iHedu3mdbvL0IEvx_JT7KriDiS4b8O10dKlMvcKtQjOx_0cm7J5jv_ZCb-ZudSupLtOpuoq-rP9Y2m7y-HAfEocL5QAi_qxVINOHZ7DETo3H8oVzBOuZM8eJzSX5EnO_QPKtv3IkImhO8dVQotLuUGrvIK6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردارنقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/680418" target="_blank">📅 22:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680416">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
۲ مقام آمریکایی: ایران تنها در یک روز آمریکا را به شلیک ۵۰ پاتریوت مجبور کرد
🔹
۲ مقام آمریکایی امروز در گفت‌وگو با نیویورک‌تایمز خبر داده‌اند که تنها در یک روز از ۵ روزه نبرد میان ایران و ایالات‌متحده، آمریکا مجبور به شلیک حدود ۵۰ تیر موشک پاتریوت شد که هر کدام حدود ۴ میلیون دلار قیمت دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/680416" target="_blank">📅 22:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680415">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdcee01ee6.mp4?token=sas4b2Rwv2zFn3oF4TMZ4Qp8lFeZe-5csFwzWCQ4rdjIFuqWAN1Crc5QOCqL8MrZkVpvtM7EB5i56WE44bdJfXpEUeBZx7G4EmgKBkSGSXQ6DGNmp6uTF_BfVvu4jiT912PbOKLnITUAVfYXzyR3BB4TrCrng8Bw19jQwKk8RXVHnntIm5wIZg3cS_56YpI8gi564tZja1grefJ_GkB-MAkCZxhUPGQBvI-MeSSe_ii6q9WHtnZfcAOYRhaEF7WoFDUrE0tEdBeoWwmuGcVmanMLbm8vhRXBMjNTTJA5rkHjNk9iYqHePb7kcTNL8aM39arFgZirTGilXnbtGBDkKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdcee01ee6.mp4?token=sas4b2Rwv2zFn3oF4TMZ4Qp8lFeZe-5csFwzWCQ4rdjIFuqWAN1Crc5QOCqL8MrZkVpvtM7EB5i56WE44bdJfXpEUeBZx7G4EmgKBkSGSXQ6DGNmp6uTF_BfVvu4jiT912PbOKLnITUAVfYXzyR3BB4TrCrng8Bw19jQwKk8RXVHnntIm5wIZg3cS_56YpI8gi564tZja1grefJ_GkB-MAkCZxhUPGQBvI-MeSSe_ii6q9WHtnZfcAOYRhaEF7WoFDUrE0tEdBeoWwmuGcVmanMLbm8vhRXBMjNTTJA5rkHjNk9iYqHePb7kcTNL8aM39arFgZirTGilXnbtGBDkKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردارنقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/680415" target="_blank">📅 22:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680413">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFklQHzTPMdfSIq_qYSPhQt76emKEFzBW8gkIzHwOdazk-MoYz2L3KqqjMDbZxF6nJ1r_nLBQ979uNEIcO6tSeSTy36YAGpnNDppTNYUYMPNZwktasui_fE_8E4Ol793RoRVad9IXAphu5JNaqKGEE2rbxjukrvjSG1UUxm3YuTYUWt-CYC-ZRKqhMSK1pXHWkymVoW5XAhPfJRZNjg2BOPTALU4IXM-UGBykJcqb1K1vQqmc9bxL96iZWoKCGMD3-FJLU3vw43Xzd1RL0ccYBgym7ZwEgbyQYXnagzUTqwrGYE1ofwDI6F1pZqGmtRcLC90iqAAYucBT_5gp-ydPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI4xUoIC5rcaVK-TbW2nBtZ2y4V6Dt225etlvYlgYrckNV1HXdkD48YGtVDQxoNIGDZivrkDNR4SMjZboKMIIejUxoqRkHwREVGRSP1qftr4sqlCSEubv5Nfgu8zukVMjK-JmcVlkPFB14LOyXe4XnQnqXBWU6u6IiCAv4oWj2aixDltoka-31GsjnsCaqsMKpxqTHUajHbvYNEgbIr1R3-NDMJUn31uq9PNdafu3kMwk9hRfI_e08rptoSyPM2Cf8Bi3vauZsjC2b8B7F0ykjbyvtQeLbGiyk6NXPY450zYlAZ53-uGvmRrMi_f-4YVATk2aUKL8g6TkgVH1oOEIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/680413" target="_blank">📅 22:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680412">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbEKAjbRrWHblzm81dc7YAS0R1W1WthYO3gvtuWqSmWqg_O2EhIkxzOHlIO2kCnnVYDiERet9lRM_2r64WULqgqZCbiUIeoK5C3bRBoo7CwScro51KUrrWs2V4x_zNsIOXUSAuM72U2Mc10JO9HHeVkIdqv331UXnvnfR_1JEhmhehM-BXhzE5p75Cl54hbVnt9Mc3zsVRySBN_ixA1kxfvqZP9jM3tLsqHFlipOY8TINLw7HggpCssNOz_g65crFBoajj93eknRdcgpFJrE6W9gLH5EC6Vr2Fti51sdvAcObB2bBCTYW0ieWCWqGBbNBsBBQR3eaymjqIzv_ykdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/680412" target="_blank">📅 22:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680410">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
حسین پاک، کارشناس جبهه مقاومت: رژیم صهیونیستی هنوز نتوانسته بر تأسیسات مقاومت در منطقه علی‌الطاهر تسلط پیدا کند/ صهیونیست‌ها با آتشباری و حملات شیمیایی به دنبال کشف ورودی‌های این تأسیسات هستند/ ۷۷ روستا در جنوب لبنان تحت اشغال است و ۵۵ روستا به‌طور کامل از بین رفته‌اند/ صهیونیست‌ها برای کشف ورودی‌های تأسیسات علی‌الطاهر، فناوری‌های جدیدی از جمله سنسورهای حرکتی به کار گرفته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/680410" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680409">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1527d44c1e.mp4?token=RETPPdezjgSRnSKY8TipAt7DQmDhx3_Csz1Y0P65Qmb18WAzMpnLYmqcHcZqPpGnTTRXBpG29-W8u2aQ6TeuJAJ7Otonhi42SuP-pXBsiCyneSagtoAroj0jhRqF9g3_cwNuKnbP1nPAqppxpUgQwqzV7qgcuVPoG4yIroElvNUSOAU-Q8d1HHTmcWlpyD2iEYboxLFFvjvaPhkn4bOIvUzcuove7wpZ9ezryZ-4eYvuRteL1_GqTEjgQh4e18eTnRP7dijMrmJ0UorXKwxADx4k6AsWdsJPHWHx5HvSz2ngL_TpYjKUBbAGF-Cj-BnSgcqNXwjVWa1GFHuPUa_uDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1527d44c1e.mp4?token=RETPPdezjgSRnSKY8TipAt7DQmDhx3_Csz1Y0P65Qmb18WAzMpnLYmqcHcZqPpGnTTRXBpG29-W8u2aQ6TeuJAJ7Otonhi42SuP-pXBsiCyneSagtoAroj0jhRqF9g3_cwNuKnbP1nPAqppxpUgQwqzV7qgcuVPoG4yIroElvNUSOAU-Q8d1HHTmcWlpyD2iEYboxLFFvjvaPhkn4bOIvUzcuove7wpZ9ezryZ-4eYvuRteL1_GqTEjgQh4e18eTnRP7dijMrmJ0UorXKwxADx4k6AsWdsJPHWHx5HvSz2ngL_TpYjKUBbAGF-Cj-BnSgcqNXwjVWa1GFHuPUa_uDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار نقدی: همه تسلیحات نظامی ما بومی هستند
🔹
ارتشی که الان ما با آن می‌جنگیم صد برابر بودجه سالانه نیروهای مسلح ما بودجه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/680409" target="_blank">📅 22:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680408">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9565fe8c.mp4?token=VKCn7j4cMQyWWu3WGrP8htIup3U3xwHyXPjxuSLacZA7zDB5gZdbIWrOU0D9fP1JtY3tSd5rnuYGRA7n2BfsoPaq7X5I6BncekYbxTGqGfyksBC8ZSqAeT3LkYW0tyOD9rmG-NJtjHiAetqgYBdSI0depxiYxA03-pavjm8C_cZ3JGp-66NSVVVIMPbUA8bLd1OR7Vj-z32fvl9wQlv32hZTPBVZ1CLwFmg7wfobUpA_eJrDPj29dpNcQbDH4wtNGQxnvmBXw78Yi7w2fRqr9k-XzziMtHJj-ZhElnbI1kIR2Lje-vyVTslq6Nz7GDGn4_RqXzliNKARQcZCXh7_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9565fe8c.mp4?token=VKCn7j4cMQyWWu3WGrP8htIup3U3xwHyXPjxuSLacZA7zDB5gZdbIWrOU0D9fP1JtY3tSd5rnuYGRA7n2BfsoPaq7X5I6BncekYbxTGqGfyksBC8ZSqAeT3LkYW0tyOD9rmG-NJtjHiAetqgYBdSI0depxiYxA03-pavjm8C_cZ3JGp-66NSVVVIMPbUA8bLd1OR7Vj-z32fvl9wQlv32hZTPBVZ1CLwFmg7wfobUpA_eJrDPj29dpNcQbDH4wtNGQxnvmBXw78Yi7w2fRqr9k-XzziMtHJj-ZhElnbI1kIR2Lje-vyVTslq6Nz7GDGn4_RqXzliNKARQcZCXh7_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان عقیدتی سیاسی فراجا: در صورت حفظ یک جزء از قرآن کریم، اضافه خدمت سربازان بخشیده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/680408" target="_blank">📅 22:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680406">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ایران فقط نیم ثانیه به خلبان جنگنده اف ۱۵ سرنگون شده آمریکا، فرصت هشدار داد
نیویورک تایمز:
🔹
در آوریل ۲۰۲۶، ایران یک فروند اف ۱۵ ایی آمریکایی را بر فراز جنوب ایران با یک موشک زمین به هوای دوش‌پرتاب سرنگون کرد.
🔹
به نظر می‌رسد ایران از با استفاده از پهپادها برای ارائه موقعیت مکانی، سرعت و جی پی اس  به فرماندهان ایرانی در هدف قرار دادن آن  جت کمک گرفت.
🔹
خدمه هواپیما قبل از اصابت به هواپیمای ۶۰ میلیون دلاری، تنها حدود نیم ثانیه فرصت هشدار داشتند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/680406" target="_blank">📅 22:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680404">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1944e2df.mp4?token=HMglYr3pTIUGR6iumiBLPGQGTVOHg5bGlDRU5gxBnpBfW_OhJoNehAGGtzosVj2R8Bh89CNNrMlbsvfFKKqOSiUwv4015w4_TFdeVaZsPmj82_YLxdYLl3viR1wQ7OxYm3We8-as9aN5UCkSwVcys5XdZKqCEadrLth2sy-vcBbXqceESqqlHp7m-xtBHlkBgpcab9VJwUOW4iWRSkxHS4k0o8Hx9Z00HMs8kEVd6kgFeAbPjlImIwFfFBTzg3ecqt6iN8oF9yOa0Kb12iYiv6qeUMMd_rQoSdNcrKSA_prWsfjTVGhj65JmgNNXsaW1FV0Tzhbvj9K7NlE_nseNWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1944e2df.mp4?token=HMglYr3pTIUGR6iumiBLPGQGTVOHg5bGlDRU5gxBnpBfW_OhJoNehAGGtzosVj2R8Bh89CNNrMlbsvfFKKqOSiUwv4015w4_TFdeVaZsPmj82_YLxdYLl3viR1wQ7OxYm3We8-as9aN5UCkSwVcys5XdZKqCEadrLth2sy-vcBbXqceESqqlHp7m-xtBHlkBgpcab9VJwUOW4iWRSkxHS4k0o8Hx9Z00HMs8kEVd6kgFeAbPjlImIwFfFBTzg3ecqt6iN8oF9yOa0Kb12iYiv6qeUMMd_rQoSdNcrKSA_prWsfjTVGhj65JmgNNXsaW1FV0Tzhbvj9K7NlE_nseNWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در سالروز رحلت پیامبر(ص) مدینه سیاه‌پوش نمی‌شود
🔹
هم‌زمان با سالروز شهادت پیامبر اکرم(ص)، مسجدالنبی مملو از زائرانی از سراسر جهان است؛ اما در مدینه خبری از مراسم عمومی سوگواری، نوحه‌خوانی و سیاه‌پوش‌شدن اماکن نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/680404" target="_blank">📅 22:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jklkQvmSAzAJ4JRY32MPL1ZojZr1T6E-yi-3ruD21nr5IDlOM87QL6pkN8GRbeYc19jwet4or9T9AaX73JnhWI68jVMGl5ykvPs_y5bRRzsHCCl0lZpzKYgkJjTCR4JoaT1uNXsmM2Ff91dLXemUw50Pd6cGUEbuscQZt6qqakeYBgFfBSZR88dU9pzdful3Bj8NUi2qJFdyK7BZmPpLsHXjILl_kNXmSknzuvniFpJGBFHr8MFtsmQGplU-0riO88R4JZrc08UwIaKPMKzoHq5zqubOgefTuJl0qmrfP4mlsimZIVnwUUtab7GE_CgdTP_lNl4X4LOMRRHFukSrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر فقط تحمل سختی نیست؛ گاهی یعنی ایستادگی در برابر چیزی که دوستش داری
🔹
امام علی(ع) در حکمت ۵۵ نهج‌البلاغه، صبر را دو گونه معرفی می‌کند: صبر بر آنچه انسان از آن ناخشنود است و صبر در برابر چیزی که به آن میل دارد. گاهی دشوارترین صبر، نه تحمل رنج، بلکه کنترل…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/680402" target="_blank">📅 22:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680400">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/badcdc31e6.mp4?token=G-stGWTJlHvxCRU7gvqFj6NHBWSwPZdcx7eMGleI1ptQNcqKLRGTNVZLndy4JreWIux2g_s_teDleJl8G4HcWrC76lC2veex63hIBIh5s-8sB5sv0TtbFmrUrhfJggQcXdw7F1hRm5zYikP1iFD8LVL5lmCM6TtvWXfgweCPUacazh2OL6uwpiBPDNs4AaeD-p9W7H6sXzefQTOUYa_1lPDJV4ez_r0u0Idnfz1laomKKW1GZCwHYOMYPtMelM6dMPHacm_WdzyBdGSf0LU-nbDLN7muZ3FOT1LYU2qoglCM_cEBVCHQnSgKA_tq0R-HgBz6KG7HcWb3cg4R3nUazA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/badcdc31e6.mp4?token=G-stGWTJlHvxCRU7gvqFj6NHBWSwPZdcx7eMGleI1ptQNcqKLRGTNVZLndy4JreWIux2g_s_teDleJl8G4HcWrC76lC2veex63hIBIh5s-8sB5sv0TtbFmrUrhfJggQcXdw7F1hRm5zYikP1iFD8LVL5lmCM6TtvWXfgweCPUacazh2OL6uwpiBPDNs4AaeD-p9W7H6sXzefQTOUYa_1lPDJV4ez_r0u0Idnfz1laomKKW1GZCwHYOMYPtMelM6dMPHacm_WdzyBdGSf0LU-nbDLN7muZ3FOT1LYU2qoglCM_cEBVCHQnSgKA_tq0R-HgBz6KG7HcWb3cg4R3nUazA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان و سیل شدید در استان ژجیانگ در شرق چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/680400" target="_blank">📅 21:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680399">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e120af53ce.mp4?token=lMv1bgGZiuGw1SCIRQ6FrAYPcm9NDN4GFPskhxXZXAS1ftQtDdTQZYThPHDNEDCDPXHu0d5Ox5n-X_YuUAI8CIy3JOoOKAV-Cne8uRa10noxwY-tfAefztbuze0LambI8DgeOaa8t2utdlGBa4KYcynsStLIaYvMeZ3PDGpax0vab-CCaDWrAft3Z5qG2uRb30VncVTlsy2DSzEpTp_2RSLQBAIsDDlemJwdZSdXG6XmLBkCjbOoRXR0HL1usjrdhUMfxEsLw9aRZmWJEGWzF4ctRJntGW0_vzT18z0v2phykrqqcMMY8afjBhE_k0LbTJ9ASmlW-UwTfK8dhfVgyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e120af53ce.mp4?token=lMv1bgGZiuGw1SCIRQ6FrAYPcm9NDN4GFPskhxXZXAS1ftQtDdTQZYThPHDNEDCDPXHu0d5Ox5n-X_YuUAI8CIy3JOoOKAV-Cne8uRa10noxwY-tfAefztbuze0LambI8DgeOaa8t2utdlGBa4KYcynsStLIaYvMeZ3PDGpax0vab-CCaDWrAft3Z5qG2uRb30VncVTlsy2DSzEpTp_2RSLQBAIsDDlemJwdZSdXG6XmLBkCjbOoRXR0HL1usjrdhUMfxEsLw9aRZmWJEGWzF4ctRJntGW0_vzT18z0v2phykrqqcMMY8afjBhE_k0LbTJ9ASmlW-UwTfK8dhfVgyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبر تکمیلی گروگانگیری
🔹
در ادامه این عملیات، پس از رهایی فرد گروگان، مذاکرات با گروگانگیر در دستور کار تیم تخصصی رهایی گروگان قرار گرفت. نیروهای تخصصی نزدیک به دو ساعت با این فرد مذاکره کردند و تلاش شد وی بدون درگیری خود را تسلیم کند.
🔹
در ادامه، زمانی که…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/680399" target="_blank">📅 21:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680398">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlO0kYrZdBudTzU2pZ1iBDoejnO0vAVt75vSywgl0WLzVOhQ-MC6EIq93RgWOa8K7O0d5qPkRNslnNJZMC3s7_9q1gvgmbOU-zn4fO20hv0jHAS3LTaxHGcdlZVQ16EklLEy9TY1IbSrNbwgmsJDrG9-nosyRIS3uPH2RMselt_KBe0uCnYTIH8yMoGHVredvxpMe815jHrTyOcJQ7Ma46K7cUiyviroVM6M771T1qj5ea104DWMSB944zHBrLpvxWzish_ILGCxYrIe0Paah56LGn4wq5r8Ags_j5c2j5DkvpzsYBykYKMS9mMp1QlvZwoCQOPOCrDbcfS0blr2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آموزش آنلاین، رکورد قبولی تیزهوشان را زد
🔹
آمار قبولی‌های مدارس استعدادهای درخشان نشان می‌دهد دانش‌آموزان تام‌لند در آزمون‌های ورودی پایه‌های ششم و نهم، بیشترین تعداد قبولی را به خود اختصاص داده‌اند؛ آماری که از حضور پررنگ دانش‌آموزان این پلتفرم در میان پذیرفته‌شدگان مدارس تیزهوشان حکایت دارد.
🔹
تام‌لند به‌عنوان یک پلتفرم آموزش آنلاین، امکان دسترسی دانش‌آموزان به آموزش‌های تخصصی را از طریق اینترنت فراهم کرده است و نتایج آزمون‌های امسال، از موفقیت گسترده دانش‌آموزان این مجموعه در مسیر ورود به مدارس استعدادهای درخشان خبر می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/680398" target="_blank">📅 21:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680397">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b561de50.mp4?token=GqEfnug59RcdMPiwHlmzorblcnHnllIGtHs440pajJsTDCqxFpYrCdBJA8-2wmm6dJTaF6yClvonV3Zt4lipmuhPp3FwyJHnpD6ToQ-1DlassJX_J53ITVdPVmD9T863DKtU47bE3F20awWDaVrkDLnDR8FpFB3WQOltfjiUmwoEShtmA45p-z9NBOI2ToFQnP4S5N9SkMXn34-IgZ9esRoGR3rukj1bp3e_ZQYpOVQ56GOyOuzC7jqWwSYqNUt3tCW8a6MhJ559DZ0qaiB_yyXAL2P5_cfe7-ymVU_Szw_PiA-W96lcbu25ezirv5vvbnL82pPypJz6bPUgT6j-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b561de50.mp4?token=GqEfnug59RcdMPiwHlmzorblcnHnllIGtHs440pajJsTDCqxFpYrCdBJA8-2wmm6dJTaF6yClvonV3Zt4lipmuhPp3FwyJHnpD6ToQ-1DlassJX_J53ITVdPVmD9T863DKtU47bE3F20awWDaVrkDLnDR8FpFB3WQOltfjiUmwoEShtmA45p-z9NBOI2ToFQnP4S5N9SkMXn34-IgZ9esRoGR3rukj1bp3e_ZQYpOVQ56GOyOuzC7jqWwSYqNUt3tCW8a6MhJ559DZ0qaiB_yyXAL2P5_cfe7-ymVU_Szw_PiA-W96lcbu25ezirv5vvbnL82pPypJz6bPUgT6j-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از دیدار وزیر کشور پاکستان با رئیس‌جمهور پزشکیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/680397" target="_blank">📅 21:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680396">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
یمن خطاب به سعودی: به‌جای گریه و زاری، محاصره ظالمانه علیه مردم یمن را متوقف کنید
عمر البخیتی، سخنگوی دولت تغییر و سازندگی یمن:
🔹
ارتش یمن در اعمال ممنوعیت تردد بر کشتیرانی سعودی کاملاً جدی است و این موضع غیرقابل بازگشت است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/680396" target="_blank">📅 21:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680393">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRPVpJchX7_-ndHYyNFnMNDaeiDFfJ9SL0iSIJSWRhvZgPnqeKUIprQ-MXc0Qt1p1Ek1V6W5L6RRYohRo7zdNTEpaVtYq4QurT1HbvxCMdCaPAtwhJnHvzJfYL0cAc1MWEwhUbVfUs2HEyKM_XgJgiCuJpyqjDEeVrMZXuZZMUD2widiJjCtbiygigtfy0G7icT4mkrW68t6FqU60E0a5TKEC1SQ1jKeWHPph8OMdajxZQEZKQ45Wc0yVNIwFaXboSIVEgDDgBw-9tixG3RR-9n3J5MqAPbWAC4isrJQG7qLMxS7yZObEbCdDVse-aKBIGyy7Uf27ZwEIfygBCTuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/680393" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf53473d10.mp4?token=XSzVfKjWuSZDrupirnmg0Z5PlExXlbFHQ5GTTYFG0RVdB5hd0JQ529KDEvpuaxzWSudcIKIDSvmxvJ92riyDOTz0zZcZaKAfRTZlT0Jg0lN81QPdnaQgs1bihPLQ1pC-EG5IP07U68oTujIat_eHXmpWbTWPQmVLjcrIA9ot9o0oxT5lHsriYOiNxnqTq39B_OcJSg_azYh8r-3X-gDWqBhVHEX-7fiW1rz1phYDjudiCMO_NQQTJlhMfWE39ciOJfdJs0dQU8fi-5VHf2xrIqc-eyoLweqYldawHqF1u_CjLV1CKNrk9Sq7NHdvzNDOU1_kvCEMB1T-FNBntac3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf53473d10.mp4?token=XSzVfKjWuSZDrupirnmg0Z5PlExXlbFHQ5GTTYFG0RVdB5hd0JQ529KDEvpuaxzWSudcIKIDSvmxvJ92riyDOTz0zZcZaKAfRTZlT0Jg0lN81QPdnaQgs1bihPLQ1pC-EG5IP07U68oTujIat_eHXmpWbTWPQmVLjcrIA9ot9o0oxT5lHsriYOiNxnqTq39B_OcJSg_azYh8r-3X-gDWqBhVHEX-7fiW1rz1phYDjudiCMO_NQQTJlhMfWE39ciOJfdJs0dQU8fi-5VHf2xrIqc-eyoLweqYldawHqF1u_CjLV1CKNrk9Sq7NHdvzNDOU1_kvCEMB1T-FNBntac3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی سلامی گوشی را دست معاون رئیس‌جمهور داد و مشکل یک چوپان را پیگیری کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/680392" target="_blank">📅 21:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680390">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWP51GiyobBmkXSwu3818zo0IXruRu7IeF_LxLY4MJCBqiyQQt4UUJJJ8IIg2hFgP7Vu9LbfnsFFMWCpgi7wMSv2UpnrZyhk8TGQNcCeTiyNh5ZJlOe8GxLv0wvAfnOpva258piNoXRTDw4GaJfKxh9Umt364uZgH0DlzHIe8Vwo30zh782YVayhtJTTQtcvwRzttHrpbj82mQVVyPR3Uz3gAFOmMZOBE4CwoW8U0Sglpbm7xKR3zDez37v-1nmmjoLCDclYmJHKdHplhp-TG2mH7QrLeRKzYBtEcezhlSXFfjvKkOpU08ew3afjAaWT14dhhC7G1aVf_a5faNthzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله یمن به کشتی حامل تجهیزات نظامی در باب المندب
🔹
منابع یمنی خبر دادند این کشتی تجهیزات نظامی متعلق به عربستان سعودی بوده که هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/680390" target="_blank">📅 21:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680389">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMWi65xW8nDPG3LVWACd_hicXnl0pSk7cTQYSxznTm7WfUbWuRRmia1DFl_lCb3fThqYHoYqMfEAixEf2y2P2gh7hws18D3QDR7TJpfYZP1r9jFaemeUGyslHUDnlyuWrYXvE_yTLZj-V2Vz_XAKumGnjqmbpZfQOQrx2yqD8EbYsRzxqiXABoZruiPDGOC3e7O3_3rwMQH0oxRaQ2VfkyU0bK5QSTD1lEvruexGrwSwq3zME5WYgn_EBpYwM8-5rHVhEnnmv2KN1QwT__ky7pGXeXBjG7q2c4Z-v-uJAS2MLafNmKSiAYnlNXWYQo6bhpgJ0PcV5wND5hU6IZgQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیتی از ادعای مبنی بر اینکه
جت سلطنتی امارات امروز صبح به تهران سر زد و بعد از ۱ ساعت ماندن، برگشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/680389" target="_blank">📅 21:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680384">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIedKX-VQZRPcfwnAhw0MLAkDQdvSdriS712corFRh6tEk_vlXOYbjxHua1VH-7M28Z3XnRj9g3S4ZsVhU6hJe4s0oIKbSppNa_5ZR2BgQAXi1EkUWgGq_15tM5VCZN9-sv-EY1bXVZsg20hgcJLjxwTfoYx6VtxKFbn3oSnpjxP516SA4CznPE4UrTT2G08vhEFt-zurKbTNhU5hcM5pw8ze5EiO21Av3RaZzyczhMitdhT9FHL-Bb7Iz032Frbixpd_v0-BxCw7xx5a-rdEGe4Namp2-i6VA2zri4lXuVpoq3IMcVH38TJYPCUYOKngx3RYJ4h-npjuUJNc1RgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpGNOYrUI3TV-Cs_jmm7deYprTIm-aw3qULm5d_0cdEBLxASe4sqo37OFaZah8jDk2s8Q9oR0lKmK7wwbLTQE140xz7k4PmC9knCOsJoU1bW5ptfrg4Dy-f74b2sL1G7pRyxkMcthFbVjzKwflFsZA52gF9zRjfJOpAIQUU8uLxlRQRGTofvYNq0zSaNaVAyKi092f-bZjxqH72ZfyeEIghxc9gXEPzkNIr0EYhHUZoOrx-jSPD3T5aPTN2k5U414ZsZSrC5M87OupQlQi_uQD7DT4OFDHX-2mBmD3TF1-ZiK_10zOz2C2pFMWj3Dpf0g-1YEg-ZOYr-VbHIh5Xqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFY0tMYaJj8WgxJvD1ILFXtxaYUumpLvMaE56jWQ3gORy6wlgzlnogByascjhNf-zMf29ICPZ1MigGWuFw7C88S2RyDs3SEd2XHBfaEYV2yPdlwQ34TqddzZ6d0cvMbAAUjXCBaaRnRMNXb49LQouFTDg2yHBbNcsAJZt_zG0JsrW5kF4k-thdPzVObketezmunWPN4Yf_q3Nr4VwpnGeDujx0DQEfcg8gWG0meEXXGsykFQjaX1Vaw6ky8_mwCz0P48qJ2spON9fB8-zYQC651hPxShpRw3wngek81_Pemj3EGnzJEqMYSgyvEaNq08wlN0x-Fo2snRzN6xQBW2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vM01Djdtu3AI1sFDCezcG3GD6VeOz8nK29oy-tnFcumwQZ0amlfXlO3ywhUlxv9ab7QMXsdglSVlnxCUv_jpVilq4xyqJfsn8PTNhg3lo-pVQWiWwBO04o4g8hdXZBVG-8-ZXis431fntx5MYbTPfoIe8fiOsHaAfHdutWJXaedNHaE0QxoocBD9HJNhblG6tmbPl4jZp5gdw1s77ed8jHm4ZKlNS9JYPpbSihTBlgybkZ7z4qyOTloI63rAhNtguAcvZaIHwFK9VbTtn_MRdfcOkq4lsv-eZhQzvVeR37vRsAHXBY4LzxxBGmcp-7VCP1jO3dvX07L2DLClxoW9aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/680384" target="_blank">📅 21:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680379">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LksJWJORMcrPZm7p_DNMYEExqw_zytqqT3IIc1G6-BD6-6gBpQJMQNlGeTwlDlveP9rKKOvZ7y0CuPEd2coLIai7T_mdJylFA0b-0ixrfhONq-YJRL7PNOYq4vzOY-GFBoPCGYnp4wMIFEQ5dqfmhPd3JANuMyJxNlAQd-A307lj2sWwDft87Xx9IuRnZNUIxj35Z2oHQO-1DnF3eJzNkBDe3tXjtMOMJXUVzEah9QcSRXTDV57T_kmvbiDri6I1UedQJlAOxBFrm7QJPRA4BXq9P4zgyD0-SYYqNEkGe5-qYuPV804tpKBtkg56rc9BwNyuRiNkxo1omGtM25QZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبی که ماه کامل شد
🔹
کارگردان: نرگس آبیار
🔹
ژانر: درام، عاشقانه، جنایی، مهیج
🔹
بازیگران: الناز شاکردوست، هوتن شکیبا، شبنم مقدمی، پدرام شریفی و…
🔹
خلاصه داستان: فائزه، دختری جوان از جنوب تهران، عاشق عبدالحمید می‌شود؛ عشقی که در ابتدا آرام و ساده به نظر می‌رسد،…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/680379" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680378">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnt53cst-Twci7IzE0fRx0CJD-0Vax-8wipklbz4XibrHNAm9ifE5aqErvjySCHhDHTTkseIAGDt-ofaroALwkItkCxvfHwW2zsq56xuzjvXYOJoVlZUAsaL1DukvLSJIuHpw185HdtG0AtYEe2DCa2QvSiVAL1y0i6L35Ih77LjqM-pdG7_-NohLvh5nDSsJOO3GzxOzpdx74sHmvt59EDsCpkUNwNwrU_d5Ng7s-L-JtQMXCl8lcW6JHi016rAgrAv5snEmf_g92Vpny2l15VV1eET4NmFMgYK-dHzvXZyW5Qox3B3wgS3kBchOPrKEhNd0OMQoDTLfzYDjdKWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
با بیمه‌بازار، هر جا باشی بیمه‌ای!
فرقی نمی‌کنه
کجای شهری
؛ پشت میز کاری، توی خونه‌ای یا حتی در حال سفری.
✅
با
بیمه‌بازار
برای خرید بیمه
لازم نیست جایی بری
...
کافیه وارد
سایت بشی
، بیمه‌ها رو
مقایسه کنی
و فقط در
چند دقیقه
بیمه‌ات رو بخری.
👈
برای مقایسه بیمه ها وارد شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/680378" target="_blank">📅 21:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680376">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84874eea4a.mp4?token=hMDHc6rOYIMpDMb3NDqB_Ju6P8J9CuG72z-N9bldVIiDwO7jcXzEfMqTQlDgMkv-exm719F3Xe0j7h7wXmIjx8raBFp81heKaO68NrSrGudQQ32Joj21zaWVkEHrQfqJ1UIj_o6hNA7CUKvX-qgYRwP1WjNqfp_eTvbcDvlpeds0IQRhgLvFH6FWRv2D8uXWf3sRYpSSdVOFKGvBymG3Mexc9U0obwm9gQpsrqyDIa8fjNJnvOCiWgKl1G7os5WhpO3CYIbZI0PT5QQPjTkkoRkHKwzOorKp_IfY_6Xp3ByJ9QZ_H7sPH_yq6MSCKk8SUWUPiu4qLZoQQFkSsbbv4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84874eea4a.mp4?token=hMDHc6rOYIMpDMb3NDqB_Ju6P8J9CuG72z-N9bldVIiDwO7jcXzEfMqTQlDgMkv-exm719F3Xe0j7h7wXmIjx8raBFp81heKaO68NrSrGudQQ32Joj21zaWVkEHrQfqJ1UIj_o6hNA7CUKvX-qgYRwP1WjNqfp_eTvbcDvlpeds0IQRhgLvFH6FWRv2D8uXWf3sRYpSSdVOFKGvBymG3Mexc9U0obwm9gQpsrqyDIa8fjNJnvOCiWgKl1G7os5WhpO3CYIbZI0PT5QQPjTkkoRkHKwzOorKp_IfY_6Xp3ByJ9QZ_H7sPH_yq6MSCKk8SUWUPiu4qLZoQQFkSsbbv4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پالایشگاه نفت لیبی بار دیگر هدف حمله پهپادی قرار گرفت
🔹
عصر امروز انبارهای پالایشگاه نفت منطقه الزاویه در شمال غربی لیبی، بار دیگر هدف حمله پهپادی قرار گرفت.
🔹
به گزارش الجزیره، اتاق عملیات پالایشگاه مذکور اعلام کرد این انفجار در اثر حمله پهپادی رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/680376" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680375">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: عملکرد بانک‌ها برای تسهیلات مسکن، زیر ۲۰ درصد است
محمدرضا رضایی کوچی، رئیس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
درحال حاضر حداقل باید ۶ میلیون تولید مسکن داشته باشیم تا تعادلی در عرضه و تقاضای مسکن داشته باشیم. بخاطر عملکرد ضعیف برخی از دستگاه‌ها از جمله بانک‌ها به سمت تولید مسکن نرفتیم طوری که عملکرد بانک‌ها مجموعا کمتر از ۲۰ درصد بوده است.
🔹
هرکس برای مسکن ثبت‌نام کند و خودش رأسا به بانک مراجعه کند، بانک مکلف است که به او تسهیلات بدهد اما بانک‌ها می‌گویند ما صرفا به کسانی تسهیلات می‌دهیم که از مسیر راه و شهرسازی به ما معرفی شده باشند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/680375" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680372">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
اکانت متخصصان سلامت روان آمریکا در واکنش به پنهان شدن ترامپ در کامیون حمل اشغال: چطور ممکن است کسی تقریباً در تمام کارهایی که در طول زندگی‌اش انجام داده شکست خورده باشد
🔹
اما در نابود کردن اعتبار قدرتمندترین کشور تاریخ بشر موفق عمل کند؟
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/680372" target="_blank">📅 20:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680371">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
روایت سفری شگفت‌انگیز از طبقه اول تا هفتم آسمان؛ هر رفتار دنیوی در آنجا دیده می‌شود
🔹
00:11:40 عذاب دیدن برای جملات به ظاهر ساده‌ای که باعث رنجش مادرم شده بود
🔹
00:16:25 نورانیت عجیب و جایگاه برزخی والای پدر، بخاطر حرف‌های مردم در مورد او
🔹
00:30:40 دریافت پاداش چند برابری از خداوند در ازای بخشش اطرافیانم
🔹
00:34:25 بازخواست شدن در برابر اعضای بدن از جمله قلبم، بخاطر غصه‌های بیهوده‌ دنیایی
🔹
00:52:30 شکایت سنگ و درک آثار آزار یا خیررسانی به حیوانات
🔹
00:59:00 پاسخگویی و مسئولیت انسان‌ها در برابر دین منتخب
🔹
01:08:20 تردد همه موجودات از آسمان هفتم به کربلا
🔹
01:12:50 تعظیم و سجده تمام ملائک با نوایی دلنشین بر حضرت زهرا (ص)
🔹
01:22:10 تلاش روح فرد خودکشی‌کننده برای ورود و تصرف جسم من
🔹
قسمت بیست‌وهشتم (فراز و فرود (۱))، فصل پنجم
🔹
#تجربه‌گر
: سید محمد موسوی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/680371" target="_blank">📅 20:33 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
