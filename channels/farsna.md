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
<img src="https://cdn4.telesco.pe/file/S-2EFMzQGVX19sRpBdCmUZrykN_iwFmGpwyhL-A3p-CNqGhunzpvjCOVge9HY0uXpklIxHl03puvd3_XPCKFtgas8vsJMU6rYwN73KY-zEtYYLqw1_rWdlYoajYNyf1OL_HATq0Uo4H9Batpb7YoB6assDn3TcHcwdSI3xI1vzHr5b30QVbS2SaRZe1g1RV4j6ygJqSjQYXSzeiIgOf_oxwPGQfkuLKJzBeFh70mWZiuq__ptvUSNP3CjEghodgqSE0gDVrD2UgLknMdqS4y-2FJGGzqmyqkVg-GbG8W7XhoTmb38k73zpqvj-hehO5uqbJyyJQYm5Fe7tE5X-dZMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 02:17:12</div>
<hr>

<div class="tg-post" id="msg-465158">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2d20cccc.mp4?token=TuMAHeStM796Bm179Rbut4mXDoyYVuI6OmK_t5ncDbQmwAdf12oUB8Wy0KpLhfIOuhtI-FrUmR37jwu0gi8TnzmWLxt-JQgkflIaRkOiJ8PgoZJRMJGRH3K626lElxSAbAHjEn6xEoy0mDSmZRBqJI6znODoRH3o608BKk8R6arw8HEFycRtA4hV7mTVUhjE4rRCkONSVOXM__zdCBDK5Xmg1TMxy2svZwcjCT96zw1rht_5lPg_1uo0bgUG2c1ZYhUxb2ZUHOuq8k48h2-GEbugT5tVA_IeP7pTjso37vy0p6DEH8PAs9w14pgMpA6Upn3pvlcCSGflfIVvObwBHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2d20cccc.mp4?token=TuMAHeStM796Bm179Rbut4mXDoyYVuI6OmK_t5ncDbQmwAdf12oUB8Wy0KpLhfIOuhtI-FrUmR37jwu0gi8TnzmWLxt-JQgkflIaRkOiJ8PgoZJRMJGRH3K626lElxSAbAHjEn6xEoy0mDSmZRBqJI6znODoRH3o608BKk8R6arw8HEFycRtA4hV7mTVUhjE4rRCkONSVOXM__zdCBDK5Xmg1TMxy2svZwcjCT96zw1rht_5lPg_1uo0bgUG2c1ZYhUxb2ZUHOuq8k48h2-GEbugT5tVA_IeP7pTjso37vy0p6DEH8PAs9w14pgMpA6Upn3pvlcCSGflfIVvObwBHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی مدعی انفجار یک عامل انتحاری در حلب، پایتخت سوریه شدند.
@Farsna</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/465158" target="_blank">📅 01:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye_1dScuttBswuvgWCcCUILqmU4qWeii0HdXQGWGS3PNmVGe90C9o9uZfnkcua7yFYxGT0cKBbE6rA76mlcEo_XNnaqC6YSznf3P15auVY6vskYgptmPWjQiVuUlM0ly90e8GJ3_Oy_Gaa2hLb4dkC9amNLkol2120v4QupKT6lsNl4cE_4NXuagj5jRdT1ViX1WMECQBYzjBhMAtO7NCCGV89vpJ0sSh9RAQm3R5dzglG1KB7MPFHyAyu6gjksqQ1eAIAW16tajJmxEL8mxzdmJFGKNNo2kE3KZB3IOo7mG39u-MvomxljkCAHXUb1sL_cQI2gQlhVTKLAisyW0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ گزینه برای سومین بازی تدارکاتی تیم ملی فوتبال
🔹
تیم ملی فوتبال ایران از ساعت ۱۹:۳۰ امروز دومین بازی تدارکاتی خود را پیش از جام ملت‌های ۲۰۲۷ عربستان مقابل روسیه برگزار می‌کند.
🔹
با این وجود طبق اعلام سخنگوی فدراسیون فوتبال، سرپرست فدراسیون در جهت انتخاب سومین حریف شاگردان امیر قلعه‌نویی، به تازگی با فدراسیون ۳ کشور وارد مذاکره شده است.
🔹
قرار است تا ظهر امروز پاسخ نهایی یکی از این ۳ تیم به فدراسیون ارسال شود. محل این بازی احتمالا قطر یا ترکیه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/465157" target="_blank">📅 01:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465156">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvkpYnZ_ZXPGXbSMNVZG_5bvp9SCbesEsPa1KtJtKT2FtX87qK1tEkwSHlZVmUtta_tSxZhWvw7kwMIgWBPkN49K8TAUmgOK5UxxyCGYld5AQm9AyI1UHP7lYZEiwSE_ZtELGIdqDIZ8X3hvoPu9Bw3WfvYEga09mBf4lgXKXtmrIEgoGVuqujYbnojUoYKSHULmE3O9f3YflQKT1T64CL4BxTqVAgOmmSRNxdm0fSY6TJwk_5sivqXUIsnt--_WpQF0EFyT-neUMTpZFe6a3Pq6AOHbcUMCa50dxJ2yHASKL5W7rTGPZUBV4BBgAywdyDeAZgOT5RJRcoNnBEK9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو در سفر به امارات با بن‌زاید دیدار کرد
🔹
شبکه عبری کان: بنیامین نتانیاهو، نخست‌وزیر اسرائیل امروز در بحبوبۀ پرونده افشای هشدار ابوظبی دربارۀ عملیات طوفان الاقصی، سفری به امارات داشته و با محمد بن‌زاید دیدار کرده است. @Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/465156" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465155">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9RTxNAw0WWvDFrexXqFNOKCt-1c_r16GUHer8htjtlq-JE_pp7gv2mUUhNxrfgvokmo0n70A9VzuzOoE-WYk1U01j7WhdPmMjp0uWDxyAloNEh6z6ozNOHcyyINnqiDwmp_aczewYoWCIryI2naObh2_8XF2RVRKnQiuKgkfdNNvzDrmOCLjecaZI34qJ5CYuWOl8mhgyCIOviulsyTVloWoLo9fmt-L2c4pDmrXhCwtyRA0JMcrlWGABMD4D85UiPEkEK9Tc3_FeucZ9hrH6RVwk_YlEVfUOkxNpU8iBXwxsH0Kt7YUVudLhRsxc57sTLCj0316rlNYoMf_Ef54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس: تا تحقق شروط ایران هیچ اقدام دیگری در مذاکرات نباید انجام شود
🔹
روح‌الله نجابت، نمایندۀ شیراز: ما در مجلس اصرار، تأکید و پافشاری داریم که تا زمانی که شروط جمهوری اسلامی محقق نشده، هیچ اقدام بعدی و دیگری از جانب ما رخ نخواهد داد.
🔹
هرگاه نشانه‌ای از ضعف کشور منعکس شد، دشمن نه‌تنها از اقدامات و خباثت‌های خود دست نکشید، بلکه تهاجم و رفتار تقابلی خود را نیز تشدید کرد.
🔹
پس از این همه جنایت و ظلمی که آمریکا در حق ایران داشته، هر فکر، نگاه و دیدگاهی که تصور کند با کوتاه آمدن می‌توان برای کشور صلح به ارمغان آورد، سخت در اشتباه است.
🔹
آمریکایی‌ها نمی‌توانند با قلدری و حرف‌هایی که بزرگ‌تر از دهانشان است، راه به جایی ببرند. ما سرنوشت، منافع خود و منافع مردم‌مان را خودمان تعیین می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/465155" target="_blank">📅 00:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465154">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۱</div>
</div>
<a href="https://t.me/farsna/465154" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#روایت_شب
|
سرزمینی که هیچ‌گاه تصورش را نمی‌کنید
قسمت ۱
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/465154" target="_blank">📅 00:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465153">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk5G-gAKf3HUfUUNqLgyLER8efJeOnx4nkKh4cxzcr9ptOq_zy3qN-9VeBIop1FXXBEjJNAqsbNYZBWTlMByt7brH7TT935HdF_2-96M7NHwWjlIUVo6RA6zw6TjiCT2dcYpIY8eHbcQ0ypWX7JxbLQuGXABs9X2OcH6BdmDRa729n6EMDzNK_l5X7_JvPik92aJX7yg-Hjy1oIAaPFeQmgLsY0jpf37Kt5XjxzQ4bFfq4moYVzrimY2emIT0r3OedRLyKZqNjbXbuF9Kuq6eppq5yb88qNzXfh4kB5vfWNwwNWZRBF6WU69LTFv2yD8mosck7GwxG3wtbUBVBEWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/465153" target="_blank">📅 00:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465151">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doEtO3ldut4abs0-vKe4BXrK9zx_NB_6agtEspPu4f0cTPf3jDO-qzMKTuOLqhbB2dZGHHwHhuGlCd8UVmEXGcUuN5Gco4mF4TBmMTumpBQhn-hu1HN5RPiZ8lzGfIADSTvB0Xs-Zz2qlduBVUZT4-Tztom9No49WBeHowRXFnZqZ0HwUijaEFplz4sRe2ZoEJ8RP160JUiUfZ7WL1yUcAVuK6-BVgH4BLTBI7fXpI4tPKrTlZbQebW_u0swZoD7IAiODIPEx5qmtiygNcVOmTI6RErBWJH1G8PYtFU_HG72lhUYVC9H7u0ccLrx8IzTvLstxXSSujIGRS8GkGozzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترفند هوشمندانه برای کشف دزدان خزانه
🔹
روزی جواهر و مروارید فراوانی از خزانهٔ قباد، پادشاه ساسانی، دزدیده شد و هیچ‌کس نتوانست دزد را پیدا کند.
🔹
قباد برای جبران این خسارت و یافتن جواهردوزدان، تدبیری اندیشید؛ یکی از شاگردان خزانه‌داری را پنهانی فراخواند و به او دستور داد که کمربند شمشیرِ جواهرنشان را بدون اطلاع بقیه از خزانه خارج کند و در جایی مشخص خاک کند.
🔹
قباد با او قرار گذاشت که: «هرچقدر تو را بازجویی و تهدید کردم، انکار کن و نترس، من هوایت را دارم.» شاگرد دستور را اجرا کرد.
🔹
سپس قباد جشنی برپا کرد و در حضور همه، کمربند شمشیر مرصع را خواست. خزانه‌داران به خزانه دویدند و چون کمربند را نیافتند، باهم درگیر شدند.
🔹
قباد همه را پیش خواند و سراغ کمربند را گرفت. وقتی گفتند گم شده، قباد آن شاگردِ طرفِ قراردادش را متهم کرد و از او کمربند را خواست. شاگرد طبق قرار انکار کرد.
🔹
قباد دستور داد او را پای چوبهٔ دار ببرند تا اعدامش کنند. شاگرد پای دار گفت: «اگر مرا ببخشید، جای کمربند را می‌گویم!» او را نزد قباد آوردند، امان‌نامه گرفت و جای کمربند را نشان داد.
🔹
دزدانِ اصلی خزانه با دیدن این صحنه با خود گفتند: «وقتی پادشاه با هوش و تدبیر خود دزد کمربند را این‌طور دقیق پیدا کرد، حتما دزدیدن جواهرات را هم به‌زودی می‌فهمد؛ پس بهتر است جواهرات را سر جایش برگردانیم!»
🔹
دزدان تمام جواهرات را پنهانی به خزانه بازگرداندند. قباد وقتی دید جواهرات برگشته، آن خزانه‌دارانِ خائن را برکنار کرد و افراد امینی را به‌جایشان گذاشت و با این تدبیر هوشمندانه به هدفش رسید.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/465151" target="_blank">📅 00:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465150">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8879383c95.mp4?token=JnzPj49ah4VwTKLj08tny6KwaS5hilnlzJvT9Gq1o7iVzhTGXJfTXtwINuEjUhrdvaIijVNkhmYjbDL4FiC-I4TkxEmTepNCdB8zHAc9pQTx2rPPGSarTmtmlL0O2egx8UXsyohTcBrjALt1Ihq-Vrv-3l3bJ96oV5nZG12uO8RnGPv64qGN2R0ehuB1VFVta3qkAg4nSgcHNpDRY-h9iEgyuKUWcWQWCUVdHIz9ZQJo-Ldm7wmSO65n_yhA2HRcVEBFKqf3N5-uZMCybrE6zio0HP5vyH127qtsF-ciemvNjZJoV1QE0V5IjS5VCm_xfH3LyBQx7oANI6Rsk9PSJKvwhgUca_iV6VigVxswwlBADytduKE1YPh5fCYpwFJq88oFRsvV01kJcPrPV-QnP8UQDHJoOy9Vq2vS5VkfSAOl0y4j5tO23C7cfqq40ouv7ragjvSu74OxIrBYkgijwq_VIQpCAVCnqqKRZszV6nZHjW3CRxC9q_fqLV7Bnp5wyIbl0YPVN4lyyxjlShwiRwFwJ_R3v7pI7mS3rdHH77vNTjZXu-zYj_OH5zXuSckXsjd27Cf7fvkqEMWCrLoof7BV_nH171qQdTdWLhXUAIQcFSI90pWxIvPFmP7Xo_w5rwVdzmDnX-ZVp7XEd8a-JwzBfIdRh4uCbTZUQ25FFKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8879383c95.mp4?token=JnzPj49ah4VwTKLj08tny6KwaS5hilnlzJvT9Gq1o7iVzhTGXJfTXtwINuEjUhrdvaIijVNkhmYjbDL4FiC-I4TkxEmTepNCdB8zHAc9pQTx2rPPGSarTmtmlL0O2egx8UXsyohTcBrjALt1Ihq-Vrv-3l3bJ96oV5nZG12uO8RnGPv64qGN2R0ehuB1VFVta3qkAg4nSgcHNpDRY-h9iEgyuKUWcWQWCUVdHIz9ZQJo-Ldm7wmSO65n_yhA2HRcVEBFKqf3N5-uZMCybrE6zio0HP5vyH127qtsF-ciemvNjZJoV1QE0V5IjS5VCm_xfH3LyBQx7oANI6Rsk9PSJKvwhgUca_iV6VigVxswwlBADytduKE1YPh5fCYpwFJq88oFRsvV01kJcPrPV-QnP8UQDHJoOy9Vq2vS5VkfSAOl0y4j5tO23C7cfqq40ouv7ragjvSu74OxIrBYkgijwq_VIQpCAVCnqqKRZszV6nZHjW3CRxC9q_fqLV7Bnp5wyIbl0YPVN4lyyxjlShwiRwFwJ_R3v7pI7mS3rdHH77vNTjZXu-zYj_OH5zXuSckXsjd27Cf7fvkqEMWCrLoof7BV_nH171qQdTdWLhXUAIQcFSI90pWxIvPFmP7Xo_w5rwVdzmDnX-ZVp7XEd8a-JwzBfIdRh4uCbTZUQ25FFKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانباز وطن، پای ضریح امام رضا(ع)
🔹
حسین محمدی، جانباز ایران اسلامی که در روزهای جنگ تحمیلی، پای لانچر، دست و پاهایش را در راه دفاع از سرزمینمان از دست داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/465150" target="_blank">📅 23:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465149">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owX4WsqURntvMJiUHlaTOmQQPhaGILl_nQLYODWUTjnMUaOS7O0HmVayuYVbgIRMkBjor2jgxPY_BWrPQu3LG3xXUQ5N6PJb1QHKYUcdj3LRGMEsmi71GXPshp1SaBj7V8kMvEuGHYlCkXCHaWtPdK7hz3sTe9BviCiyVxCI9yac6p15MyG5aaZYGzJsxMvdsHDtSWThgwIG9mWeiLqWF_WWQzdIxKbLWOpkUn9Npxx-Iva0rek4Mr86h79pHcXP8t_gt1D1PdUM1pAnVPje8eLluxxRD0BL5mcuvs4Kvni0jHoB9wdxWKr37Cz5oZq0cqyq2Xe6eM_SpQPQmxFEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق اوراسیا در خدمت بازار روغن
🔹
گمرک ایران بخشی از سهمیهٔ واردات روغن آفتابگردان گلستان را به گیلان منتقل کرد تا محموله‌های روغن در گمرک گیلان معطل نمانند.
🔹
در این جابه‌جایی، سهمیهٔ گلستان از ۱۰ هزار تن به ۲ هزار تن کاهش یافت و ۸ هزار تن از سهمیه باقی‌مانده به گیلان منتقل شد. با این تصمیم، ظرفیت واردات روغن در گیلان از ۱۷۰ هزار تن به ۱۷۸ هزار تن افزایش پیدا کرد.
🔹
هدف این است که واردکنندگان بتوانند محموله‌های خود را با تعرفهٔ ترجیحی تجارت آزاد ایران و اوراسیا ترخیص کنند و واردات روغن با مشکل مواجه نشود.
@Darsna
-
Link</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/465149" target="_blank">📅 23:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465148">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ-Mv5Elwjm0wdQkAD3Dk_JrZMUUkcSRIDR4Aw6jUjjfcuHIfW6FRlYymROLDt5jbYa3IsMo-a0LWctVkkDeE9WqceIyVQ6_vGtRLAWz_MJipKLXyeXJ5UmDtSM8kczvnrI5MnhM--y9FP6n7fHsj1Egww6fjLwtPpbpANVg0yS8skV914Vz9YhgKvjDzMgpuvqTXzrKSlFBYloKBxOYzyr_MjTru94nVdaJNVny0u96qIcNTR-c2alrS0KgcYJZUuDCmNNepTKnPXNrjHVbi9OQ1ASX02rEcdBZt5C6myKyR7GsDvuZ0OTPo6_NyFAAtGYZevb-cF51ut9a73UHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کمیسیون امنیت ملی: آمریکایی‌ها قبل از هر مذاکره باید تعهدات خود را اجرا کنند
🔹
سعیدی: تا زمانی که شروط ایران محقق نشود، توافقی در کار نخواهد بود، آمریکا باید ابتدا شروط ایران را بپذیرد و به تعهداتش عمل کند.
🔹
تجربه برجام و مذاکرات اسلام‌آباد نشان داد که نمی‌توان به وعده‌های آمریکا تکیه کرد.
🔹
ایران اهل مذاکره است، اما مذاکره تحت فشار و تهدید را نمی‌پذیرد، گفت‌وگو باید بر پایه احترام متقابل و رعایت مواضع ایران باشد.
🔹
ایران در برابر تهدید و زورگویی کوتاه نخواهد آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/465148" target="_blank">📅 23:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465147">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8630b43d.mp4?token=FEHLmQsC-e5Fu8VrLwMyodxcgBakTVkK1Gp5Il-_2TMaO7nl888yphjj8J4RbdY4M3pDZkdE-b16Xux673NJqiUX-fCQk0LOrB37xsPtVZ6oAL020kEIDKdrQOOoMVdLyrmr_viNEpVWEvRaBNJYjTonObOsQMR0JeM1B1mGWT7bTt8RTAn-Kce9ImHZLjFryzRDsjWEU7AI-TL7jWDqxwjDU53o9pOOn9dPzKvmietRFC9a7lWPfCi5d0cOeoeFXCJjCdWiFXWDljv3LlGjVzdHZfUIwLcVFFGo0iYGGeL1h8lKZzJqS1E6qA2EBlBVyBl-BErjQ2ELf7950ceQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8630b43d.mp4?token=FEHLmQsC-e5Fu8VrLwMyodxcgBakTVkK1Gp5Il-_2TMaO7nl888yphjj8J4RbdY4M3pDZkdE-b16Xux673NJqiUX-fCQk0LOrB37xsPtVZ6oAL020kEIDKdrQOOoMVdLyrmr_viNEpVWEvRaBNJYjTonObOsQMR0JeM1B1mGWT7bTt8RTAn-Kce9ImHZLjFryzRDsjWEU7AI-TL7jWDqxwjDU53o9pOOn9dPzKvmietRFC9a7lWPfCi5d0cOeoeFXCJjCdWiFXWDljv3LlGjVzdHZfUIwLcVFFGo0iYGGeL1h8lKZzJqS1E6qA2EBlBVyBl-BErjQ2ELf7950ceQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«خادم‌الرضا» عنوانی که آزادکار ایران برای خداحافظی انتخاب کرد
🔹
امیرحسین زارع قهرمانی است که حالا برای پایان مسیرش نه یک رکورد، بلکه یک عنوان را انتخاب کرده است؛ «خادم‌الرضا».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/465147" target="_blank">📅 23:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465146">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8GXudFGTkBKQQ8pSz41PO5PLbBPzyAVTC7WSjnsadYld-P70hrRZkmkA3yd8ZcFPnpja4fDaF2sbtrD0PhLMeXIUi8i8-gOGav284MtS_wO6JKfxhUdInBo4-Ezp6qBPAYwnePUDcUPmVlRnvAN-Acd7LpVb9gUdofkKkE5RZT_SOXQCQ8DMXkxTgSts638RFIIwihSobHUFss19irSH5g0GUyDs4jo_TB3EOXtnA35PYHmgjnUuM7pL4keFOXQN9QjPlVWQQ99BGqxGxRCReLswp02PFeg6GdmewgfEjHaZS1OfisUp6omZ_8btr7IahnVi0C_Ylx5LQ8Rjm08CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی: تا اجرای تعهدات آمریکا در تفاهم اسلام‌آباد، مذاکره‌ای آغاز نمی‌‌شود
🔹
عضو کمیسیون امنیت ملی مجلس: آمریکا باید پیش از آغاز هرگونه مذاکره، به تعهدات خود عمل کند. تا زمانی که ایالات متحده شروط و تعهدات مورد نظر ایران را نپذیرد و اجرا نکند، مذاکره‌ای را آغاز نخواهیم کرد.
🔹
در اسلام‌آباد نیز شاهد بودیم که قرار بود به محض امضای توافق، پول‌های بلوکه‌شده ایران آزاد شود، اما این اتفاق رخ نداد و آمریکا بار دیگر بدعهدی خود را تکرار کرد و نشان داد که نمی‌توان به حرف‌های سیاستمداران آمریکایی اعتماد کرد.
🔹
دیپلمات‌های ایرانی در شرایط فعلی هیچ مجوزی برای انجام مذاکرات دوجانبه یا سه‌جانبه ندارند.
🔹
حتی صحبت از مذاکره هم در شرایط فعلی منطقی نیست چراکه موجب کاهش قیمت نفت و در نتیجه کاهش فشار بر دشمن می‌شود و تاب‌آوری آمریکایی‌ها را برای ادامه فشار و دشمنی با ملت ایران افزایش می‌دهد.
🔹
در شرایطی که ایران با انواع تهدیدها، توهین‌ها و فشارهای آمریکا مواجه است، هرگونه مذاکره پیش از عمل آمریکا به تعهداتش، غیرمنطقی و غیرعقلانی است و با مصوبات و سیاست‌های بالادستی نیز مغایرت دارد.
🔹
انتشار اخبار مربوط به مذاکره عراقچی و ویتکاف باعث نگرانی از شعله‌ورشدن دوباره جنگ شد، چراکه تجربه گذشته نشان داده که هربار پس از مذاکرات عراقچی و ویتکاف، جنگ آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/465146" target="_blank">📅 23:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465145">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8973d873cf.mp4?token=YX8AGrcbhYZG3y8-SnPh3Zzc13d5_YIPRp8734G8wNSaBkxyx4fvHTZtfL0SS8Zls_4qXHqOPvKjQPfdHO8RQ_GbikCYU53LN5PtLzlEDRUj5GXGSEi34BydyRT_Sb6xTbQwSLjYTqKLNhRNq5adAwoghqHRa-YJO8WAP21qhFFAQGDuK_u9oULpx_QGQpls4814qrRWhgt34bkrfX77COO-_JMg58fw4FTgJVh8rzXljk1S9wS-o-NErqRMuyGlebHXBCWi9AKCQtBLJiW3tezLi4WjZ3vbcdhhGD6pOm2JwOc6twV6iqv0renq2nU-klcR1g3rRvWFhrwesVOArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8973d873cf.mp4?token=YX8AGrcbhYZG3y8-SnPh3Zzc13d5_YIPRp8734G8wNSaBkxyx4fvHTZtfL0SS8Zls_4qXHqOPvKjQPfdHO8RQ_GbikCYU53LN5PtLzlEDRUj5GXGSEi34BydyRT_Sb6xTbQwSLjYTqKLNhRNq5adAwoghqHRa-YJO8WAP21qhFFAQGDuK_u9oULpx_QGQpls4814qrRWhgt34bkrfX77COO-_JMg58fw4FTgJVh8rzXljk1S9wS-o-NErqRMuyGlebHXBCWi9AKCQtBLJiW3tezLi4WjZ3vbcdhhGD6pOm2JwOc6twV6iqv0renq2nU-klcR1g3rRvWFhrwesVOArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاریخ‌سازی حافظان سنگر خیابان در الوندِ قزوین ادامه دارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/465145" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
۲۱۲ شب پای کار وطن؛ احساس تکلیف کاشمری‌ها تمام‌شدنی نیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/465144" target="_blank">📅 23:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71c93c333.mp4?token=Ktm3g3c6Cm2hDi31cSWSMz_MOMdHIlz4DEppqJ9SRKpenvLkQswg4L0dDB7moWXZRobPCznTYGvDMOb7GNdRqPAeM00tt3NyyDn955w1najgPjHfDANzETHicPX92rb5jMz4E9-DqHDvy8fgZ0G8BaFnjEztCyjEnva3jF20u796k_YVC_EaEAZGkavy10MkHJOCj4XMHT1i1FFCGWJr_wZnV0faSLQ-vibK3WHEe92v3iudeGIsitncCNdLuDEl1-5o9HD_qU-dnCD4AfUmmn_niYaYxqMvNuGdZFjMlKMLa6jHBw6-mnpdAJwYPEICKwZjD9hJ-5iqcjHnRZi_7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71c93c333.mp4?token=Ktm3g3c6Cm2hDi31cSWSMz_MOMdHIlz4DEppqJ9SRKpenvLkQswg4L0dDB7moWXZRobPCznTYGvDMOb7GNdRqPAeM00tt3NyyDn955w1najgPjHfDANzETHicPX92rb5jMz4E9-DqHDvy8fgZ0G8BaFnjEztCyjEnva3jF20u796k_YVC_EaEAZGkavy10MkHJOCj4XMHT1i1FFCGWJr_wZnV0faSLQ-vibK3WHEe92v3iudeGIsitncCNdLuDEl1-5o9HD_qU-dnCD4AfUmmn_niYaYxqMvNuGdZFjMlKMLa6jHBw6-mnpdAJwYPEICKwZjD9hJ-5iqcjHnRZi_7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضدحال آمریکایی‌ها به زیباکلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/465143" target="_blank">📅 23:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbae476c9a.mp4?token=KbG95ELXsS0uLJsl4ChNLQBhl7F0VxJI4ZU-bts9Z3k4_gTlXE_cTK3HVqccVyUAoSIFANmHX5IEBzFoD4rh9YPFC10vi0EZHNoc6BSsPwYFRisAt6k34srNTu6fpoqEvzzZPtyPTcZTNKDkeimBzavIxBJwQ6LqaZqoasl5f7701szBQCDDPhbrFS8f3Z4c1x1bN9yd3lOdENZdE20pIIBW0-95flUCW_5ab-7eWfQPiQSQeaXz4Jqm0nFAQ0XERS3sbN4e4rB6XRuOb6UJTGPetbEuGH5T45WYI-3U6xFkLFiem-88rcFtFCAuStkSpnqjmlgywkxfjDHMx4VMnn4J3XTZh4kSbr1OQmkxGT6tVIG9KXn8r5bghYefj2vK9UJqL5KL7zbaS8pTXrNkXlcM-VOh2_ylCpFw-gZDIhbYE2IYlRONYt6p15IihL-upSqYbIh-sd7n984_G557cjPk3RAIRy6yBcAqhWNe2bQe1bKr3NWQtpG6syjUP5jGkEuAj6Uv99aM9gX1PSIRhxlC9P2bNxUqiqbzTl8_aKPGKq_XvZdj5flcYb0CoFx0vdXVBVAMYb4WgKmHL_lMJGhwHSUJz0A5nZLBMdztNVhA8uBTxRGJl6S2Wtgz9XXiMUmJQMLxW0eI8hCqEzPlGASQuXhYBGSZ9Bc2b7IFGp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbae476c9a.mp4?token=KbG95ELXsS0uLJsl4ChNLQBhl7F0VxJI4ZU-bts9Z3k4_gTlXE_cTK3HVqccVyUAoSIFANmHX5IEBzFoD4rh9YPFC10vi0EZHNoc6BSsPwYFRisAt6k34srNTu6fpoqEvzzZPtyPTcZTNKDkeimBzavIxBJwQ6LqaZqoasl5f7701szBQCDDPhbrFS8f3Z4c1x1bN9yd3lOdENZdE20pIIBW0-95flUCW_5ab-7eWfQPiQSQeaXz4Jqm0nFAQ0XERS3sbN4e4rB6XRuOb6UJTGPetbEuGH5T45WYI-3U6xFkLFiem-88rcFtFCAuStkSpnqjmlgywkxfjDHMx4VMnn4J3XTZh4kSbr1OQmkxGT6tVIG9KXn8r5bghYefj2vK9UJqL5KL7zbaS8pTXrNkXlcM-VOh2_ylCpFw-gZDIhbYE2IYlRONYt6p15IihL-upSqYbIh-sd7n984_G557cjPk3RAIRy6yBcAqhWNe2bQe1bKr3NWQtpG6syjUP5jGkEuAj6Uv99aM9gX1PSIRhxlC9P2bNxUqiqbzTl8_aKPGKq_XvZdj5flcYb0CoFx0vdXVBVAMYb4WgKmHL_lMJGhwHSUJz0A5nZLBMdztNVhA8uBTxRGJl6S2Wtgz9XXiMUmJQMLxW0eI8hCqEzPlGASQuXhYBGSZ9Bc2b7IFGp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۲۱۲ میدان‌داری سرخسی‌های خراسان‌رضوی با حضور مهدی سلحشور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/465142" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFl0SwLyzKWb79bqPpbb-I-Zp56l-25QadHoafpgeOBFwPW32NvW-kCr0JdDDWKyxIt4WrZHUkhSKDfdhH_NzfbbHLKmAQq4MeVpa3RzSS6CYAssA6dKBJyKZ2HFygIqnVLcNv-WEjOPOJcqllQO1zi7WH58u9myvrsaywTeEeOV9nfB7_ONSoaxXpG_aDXNNgsfvrHcwjWA588-l6cVwH3OWrLewvAHubM36KWr8y-xq0D9TJjZnEkJf0v6HjRCwA7C_s2iyNsh0jigRDe-L7kMcadhB-s3mTqYXowCsZB8QkaAi6AtwX3EJk8UhxEtY_OEerSKovUZxEZauNy0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب‌رئیس کمیسیون امنیت ملی: پیش از هر مذاکره‌ای، آمریکا باید شروط ایران را بپذیرد
🔹
مقتدایی: اکنون نباید عقربه‌های زمان را به عقب برگردانیم. موضوع هسته‌ای دیگر در کانون یا محور مذاکره نیست، بلکه اکنون تنگه هرمز در محور و کانون قرار دارد.
🔹
آمریکایی‌ها اگر شروط چندگانه ایران را بپذیرند، از این مخمصه خودساخته بیرون خواهند آمد؛ اما اگر نپذیرند، مقاومت ایرانی چون چکشی بر سر دولتمردان آمریکایی فرود خواهد آمد.
🔹
بازگشت به عقب و برگرداندن موضوعات به شرایط پیش از حمله آمریکا، نه عقلانی است و نه منفعت‌زا؛ بلکه می‌تواند آنچه را تاکنون به دست آورده‌ایم نیز تحت‌الشعاع قرار دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/465141" target="_blank">📅 23:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de508afd9d.mp4?token=OyFaCfzURwpM09XsXDOWywt2969K21afU1KTkAOGRmMYmunBRVKwbkJNue8_g2YW98Ky7jAwDcp6REDEHt33AFf-mMEQkU2WOW6p7ueIQQvcw5uV3b3m1I8WirB_NZ_HINPIz3_TVcAmr3wR7RtOWvfEPdPMWT2RFoIEmq7NHFjXB7-ARjgEiHFEe7YXmAgGzxs8biMs5P5p8BwQyuQ9q4421GgYdzOyDc-n22UzYmnD6lQ8n3vhTauTFPT_q7qbOlPxqdBS-i-odAWNSqA7I_1QTKYX5-DYE4_j3wOvErVaj7RJFj2mfhJtQIcnnhBrCt7blwLkl6P4uyAhGnIljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de508afd9d.mp4?token=OyFaCfzURwpM09XsXDOWywt2969K21afU1KTkAOGRmMYmunBRVKwbkJNue8_g2YW98Ky7jAwDcp6REDEHt33AFf-mMEQkU2WOW6p7ueIQQvcw5uV3b3m1I8WirB_NZ_HINPIz3_TVcAmr3wR7RtOWvfEPdPMWT2RFoIEmq7NHFjXB7-ARjgEiHFEe7YXmAgGzxs8biMs5P5p8BwQyuQ9q4421GgYdzOyDc-n22UzYmnD6lQ8n3vhTauTFPT_q7qbOlPxqdBS-i-odAWNSqA7I_1QTKYX5-DYE4_j3wOvErVaj7RJFj2mfhJtQIcnnhBrCt7blwLkl6P4uyAhGnIljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مانتوهایی که به‌سختی در بازار ایران پیدا می‌شوند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/465140" target="_blank">📅 23:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fccd8f7385.mp4?token=JWMyUbfJtcS7e1PpOOqXZ-yxlTYiGRIjBkRnrDZo_DJM1KCnNjd_sJ0Sze82xuXAscAovRlR3zFx9-CWl9b4Ccp1LGAoETGD-fPIC939HTUHHKVFKP-Ml7qgiGmEW4C-NqS2l_xlzHSWtdBWgaNNevXSbNc5nlAAyatsd6J1N9TdQ_SxvExKJZq0gnJ7tgX1RObLtW4-rtvuPx_j8CYkvioHLiN5ZbLxU7NiaXgYzb8aLrnrGA_Z8iRQyXiFYPdjCeQbPRCs_5FiIwflicSweIhaiDAMW_yfTV_5qVyiH86BcJ7LXHM0hT4wb5FGWyvEh3ancvhU85WE4BTVU0LEaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fccd8f7385.mp4?token=JWMyUbfJtcS7e1PpOOqXZ-yxlTYiGRIjBkRnrDZo_DJM1KCnNjd_sJ0Sze82xuXAscAovRlR3zFx9-CWl9b4Ccp1LGAoETGD-fPIC939HTUHHKVFKP-Ml7qgiGmEW4C-NqS2l_xlzHSWtdBWgaNNevXSbNc5nlAAyatsd6J1N9TdQ_SxvExKJZq0gnJ7tgX1RObLtW4-rtvuPx_j8CYkvioHLiN5ZbLxU7NiaXgYzb8aLrnrGA_Z8iRQyXiFYPdjCeQbPRCs_5FiIwflicSweIhaiDAMW_yfTV_5qVyiH86BcJ7LXHM0hT4wb5FGWyvEh3ancvhU85WE4BTVU0LEaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا مردم شهرکرد جانانه پای عهد خود می‌ایستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/465139" target="_blank">📅 23:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465138">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTtO7ZBlC6Y3jEgLj3tmcsNV1kSoWs1IkPhZ9QBvilRXh5pfDuHD75wmUI6UyUVl0kYeLYIx7iGX0P1wvU733pysb0ZjekioIIKrmPO73pE5039iDNoVYRinVeFE5VR8Iypr6oFTYRGEwXYPlXBre4jQ6lEMxkvRmCxfIuCuVdj_dpKIzrvODCqj0aikjdASWY_mzlxjLq3dZxMdqqjGO_5BXDXULm_s-I876GQ4GltrSL_893yEXMBZfWFH9P-ViEnmLji9H7IZk5zOGVaAkQG26ujC-Ud_QGT8yJx3Uo8RkSL9SNozV_3DH3LKWKq5XCztpt17Nplnq0woXm3dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروندهٔ غرامت هواپیماهای ایران در انتظار رای لاهه
🔹
رئیس سازمان هواپیمایی کشوری: «در دادگاه لاهه و ایکائو (سازمان هوانوردی بین‌المللی) برای خسارات جنگ شکایت ثبت کردیم. ایکائو حق را به ما داده اما منتظر نتیجهٔ لاهه هستیم.»
🔸
پیشتر وزیر راه‌وشهرسازی گفته بود که حدود ۱۰۰ پرنده ما در جنگ رمضان  آسیب دیدند. ۸ فروند هواپیمای مسافری هم به‌طور کامل منهدم شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/465138" target="_blank">📅 23:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465136">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a090dc8a.mp4?token=gxM05sX9JZceeKjy9lPRn1-CpN3QsVR9Igzv7-MQieKKwBwOb4DUxweG6JzFlecBrm-4fq2DO_UJiFqtc6KWMQ0tH0gmLdLSrpVTSf3Q6e-hCLRTaDskzAgvETDZJG6EBs33b_yOXpBGIlm3SWCkGd37DJ4cOsqM1cAYbkDRhcz0nbMX7Lk6hfdMqOSAKqiSDxM3Yo_FcGvwmSZ7MfNu1y06c1e-AfqJH4O2ce65F3FE22QzoFrjIUgxsEJttxz4mPQ9yRAR7PKL8PW9UiT_erhhVUfYTrIAIIkinmRwnLBpbVeENaszFEmIpfNlDqA7kp9FkMMktbd_w6QbxKh_B5bsPbksOHPQfhEV2H6s3ddH-9Huxp4afOV28l5y6DtaiSY2MMgeuKVO_PEyLIdYmLTaelAG5RMMvPS7L0B_i6qbdnu9LMFAM4cAwkEachr1s0w9RzKXwOxsCbHaeeSuDt1rtKvqCyRQhfkIO_ahBgKDfxJanq-voSSbTUSudZqzeceQGd_CFEwPs9zIX9fwslOtGagpcqCyboplOx7vLAIlhVZr6yqmtOH9hiDKtqShapsLr9Zu7531HqaSdyCyp8j1FH7TGnSpRKVz29dRbyvmZf9BB9IQAHZImQR5tv65IaIZMlz-ZhuGQLn2JwaSFLfCN6zfrGxTs7wrvM49Rmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a090dc8a.mp4?token=gxM05sX9JZceeKjy9lPRn1-CpN3QsVR9Igzv7-MQieKKwBwOb4DUxweG6JzFlecBrm-4fq2DO_UJiFqtc6KWMQ0tH0gmLdLSrpVTSf3Q6e-hCLRTaDskzAgvETDZJG6EBs33b_yOXpBGIlm3SWCkGd37DJ4cOsqM1cAYbkDRhcz0nbMX7Lk6hfdMqOSAKqiSDxM3Yo_FcGvwmSZ7MfNu1y06c1e-AfqJH4O2ce65F3FE22QzoFrjIUgxsEJttxz4mPQ9yRAR7PKL8PW9UiT_erhhVUfYTrIAIIkinmRwnLBpbVeENaszFEmIpfNlDqA7kp9FkMMktbd_w6QbxKh_B5bsPbksOHPQfhEV2H6s3ddH-9Huxp4afOV28l5y6DtaiSY2MMgeuKVO_PEyLIdYmLTaelAG5RMMvPS7L0B_i6qbdnu9LMFAM4cAwkEachr1s0w9RzKXwOxsCbHaeeSuDt1rtKvqCyRQhfkIO_ahBgKDfxJanq-voSSbTUSudZqzeceQGd_CFEwPs9zIX9fwslOtGagpcqCyboplOx7vLAIlhVZr6yqmtOH9hiDKtqShapsLr9Zu7531HqaSdyCyp8j1FH7TGnSpRKVz29dRbyvmZf9BB9IQAHZImQR5tv65IaIZMlz-ZhuGQLn2JwaSFLfCN6zfrGxTs7wrvM49Rmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۲ شب؛ روایت مردمی که خیابان را به میدان ایستادگی تبدیل کردند
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/465136" target="_blank">📅 23:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465135">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در سفر ۶ ساعتهٔ نتانیاهو به امارات چه گذشت
🔹
رسانهٔ صهیونیستی «اسرائیل هیوم» گزارش کرده که سفر دیروز نتانیاهو به امارات ۶ ساعت طول کشیده و در این سفر، رئیس موساد و رئیس شورای امنیت داخلی رژیم صهیونیستی او را همراهی کرده‌اند.
🔹
شبکهٔ‌ صهیونیستی «کان ۱۱» و شبکهٔ…</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/465135" target="_blank">📅 23:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465134">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
مقام ایرانی: انعطاف‌پذیری ایران در موضع هسته‌ای نادرست است
🔹
یک مقام آگاه ایرانی به شبکه پرس تی‌وی گفت: «گزارش‌هایی که برخی رسانه‌ها درباره انعطاف‌پذیری ایران در موضع هسته‌ای خود منتشر کرده‌اند، نادرست هستند.»
🔹
این مقام گفت که دولت آمریکا در تنگهٔ هرمز به دام افتاده است و برای منحرف‌کردن توجه از این مشکل، موضوع هسته‌ای را مطرح می‌کند.
🔹
این مقام افزود که موضع ایران در مورد مسئله هسته‌ای تغییر نکرده است و تأکید کرد که هیچ بحثی در این زمینه درحال انجام نیست.
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/465134" target="_blank">📅 22:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465133">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌همه بازداشت‌شدگان طرح بمب‌گذاری فرفورد، تبعه انگلیس هستند
🔹
پلیس انگلیس اعلام کرد که ۵ مردی که در ارتباط با طرح مشکوک بمب‌گذاری در نزدیکی پایگاه نیروی هوایی سلطنتی فرفورد بازداشت شدند، همگی اهل لندن هستند.
🔸
روز گذشته رسانه‌های انگلیس مدعی شدند پلیس این کشور…</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/465133" target="_blank">📅 22:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465132">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cde3ac3e9e.mp4?token=fkSuukVPFC5rZdFiYtJN4qj_Mdji-ZEdZb72qontzbMNtmdN-uWv93F-b19aBpYZfnrscjTaYxONljZwFAgbWP3gDOsTutB4nONnjcWq_4IVI87vAan-5P2nQjQLjKK-Gl1FnQeJBtvfPJHp-XAOg4v0dEjYi7SK4h7jHB67grIOQqQqdYvIndX36d8Cfthpxq6nASVZ6NDZOT6OfJ16e_ZQmUWyxgHTO_H0lnXPwfRaecac1J9YtRwqnsb9BZaRCeVjAt-EPMtzJZyh6snTn8QETf4PsDje6wJ9JpCBPG5f40x9bKWFy6bXPvF6kPLn3nAGsZVTymVhcjihsMoGXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cde3ac3e9e.mp4?token=fkSuukVPFC5rZdFiYtJN4qj_Mdji-ZEdZb72qontzbMNtmdN-uWv93F-b19aBpYZfnrscjTaYxONljZwFAgbWP3gDOsTutB4nONnjcWq_4IVI87vAan-5P2nQjQLjKK-Gl1FnQeJBtvfPJHp-XAOg4v0dEjYi7SK4h7jHB67grIOQqQqdYvIndX36d8Cfthpxq6nASVZ6NDZOT6OfJ16e_ZQmUWyxgHTO_H0lnXPwfRaecac1J9YtRwqnsb9BZaRCeVjAt-EPMtzJZyh6snTn8QETf4PsDje6wJ9JpCBPG5f40x9bKWFy6bXPvF6kPLn3nAGsZVTymVhcjihsMoGXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: دشمنان بدانند بحث انتقام ما پابرجاست
🔹
ما باید بالاخره این انتقام را بگیریم؛ در هر جایی یا زمانی. @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/465132" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f11e72571.mp4?token=Cnn7UQtxGxL8y43sY4TpF2a8HzKZ4hJ1uF8qyEz5qFrVvm8amjk-rXVKgMw43RhCbg3yGKtK0N2902qbF_wLlY0QuxaLmaBOERXhbjsadElXIFoQld1n7wtXbta0o67HJI4NDd6i5p4ymy-ksirTZtMuia81U9HZdJ9r5lgig1d4EHebq0lgnZd-DTEXw2FzGz1CSk8-fssK57B4S9Cutzj0j7Gir0PLJqnX-u4BI2WLglLO2Dz12ajpsyPGnm5IrWpuKiTJhBGMXCu2zhTEqXHyhBPpOOxLIKzQ3cVnTwuAVcnjQ_NsmOu7Iqh1_nD0RgvztrQvHyDnWMrRItumbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f11e72571.mp4?token=Cnn7UQtxGxL8y43sY4TpF2a8HzKZ4hJ1uF8qyEz5qFrVvm8amjk-rXVKgMw43RhCbg3yGKtK0N2902qbF_wLlY0QuxaLmaBOERXhbjsadElXIFoQld1n7wtXbta0o67HJI4NDd6i5p4ymy-ksirTZtMuia81U9HZdJ9r5lgig1d4EHebq0lgnZd-DTEXw2FzGz1CSk8-fssK57B4S9Cutzj0j7Gir0PLJqnX-u4BI2WLglLO2Dz12ajpsyPGnm5IrWpuKiTJhBGMXCu2zhTEqXHyhBPpOOxLIKzQ3cVnTwuAVcnjQ_NsmOu7Iqh1_nD0RgvztrQvHyDnWMrRItumbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: هم‌زمان با مصرف سلاح، سلاح تولید می‌کنیم
🔹
هرچقدر موشک و پهپاد شلیک می‌کنم جای آن را به‌سرعت پر می‌کنیم.
🔹
کارخانه تولید پهپاد آرش را زدند اما هنوز درحال تولید است. @Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/465131" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465124">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFVMmsuEncGYlkgz-4KJrkgHoHw3JlZ_CWeTbZgnQuJ_1IB1ugUj-dmtVHk2hfIvfs_5UUHxnLdpsvArxrVXfPTVpj0US7YR79FLuShoX_aacLpFP8PBg51JC0oOTp5BG39uG5TROBT641S8ZOo7hJ_lvIAO8xHbPzVh7WpUiNQ75vSRlAgwH53aVBqq0bq3O59_tdADBOH-ZpNyoa1xsS3CS_G8TNsrbCFyjcf00hvjdpdAyTAX2J1HaclBitRVH1uTnmOPVwez1P3qjqvyDyTAMrfzm8xjUu2dqj-yZKQs9SwYVVVLsV1sclWofJHVBSqQu_A1fg2-LFU8_dh8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgzQnmYlK4BT6LzrbDHwvVQnT1E9FGw0E9Lg9K3ec_viNJ0o8-Y2Z86gyKnqeQGby9AanjJ36VVko4XXkPJia0h5145Zc4u5qd6G8PaqnTxj5PHs8NsfLCmDs76HL8WIdNGE2x-sNhc9KUJWRzOmOfh3InI1iJednHnb00kzrpRcteQAAWxlOL94Y-pjPTbzca7NqLXD6eE7iK-YURkoNznmnmTqTDN2pmnfXOAOuHshmwCxu35x-2Bo8ha2eSMCaf5y8QlquEctAIRNqPnQ8ydn70Sp25cOwQDqhDxenZXTtYwQfulMHJOBSsfK7ogIaQ8gbDq5CrpCVXyq8ftvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2D8g7nQTg4Vy9N1WchjC3fMs9nGaEPYmDxEfGaSTopg4APqAsUoLChsBrSjI7DiLlPJ-Rb7OH5JYy16OigBWnTza-j1ausPmhlgnf6--_KZL3FRJIpD5QQAtJA8mLBFJJNgfOXhg6Y5cJ3uUejJmjqUAXE3WmzPw5NAAlmKnR1IVDCqeSUazql2AtDQcGKo-UZ07yLJS4t-cOIjr_UzR32raZKKNxMZzDalVWZed7pDaJouTvPk3_Z2lF2KHWse_fafTLlDoiMt3XSLTEezCw7DDTK4fx__LWZP3dX0YW2Tgn526lH48FgdLTFNNT0gRjIFr-L5vqSvmbwHzMtEFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jV357cnN5AVN2sqiaKBCX8efTdYg09bu_P8a1lVdNTzUj6wSNu7KN-HsZ-qj0KhnRSOJ69CCy2CXmZcHFsetrIG7yReYnMNo53dskv8gHcRINlvdEm4m7ycXyEX1g6oHhX-NW3k6-hdF04THpp-QBiD6QKI02T0wqPSVxiqn2zUi3OBYB51yvJCq1SwAbCHEfzlLMHeFSHKnvmsf-TqljOpW2A0C82AhUm0Or6xTB99xyGFp840huAf9CDdBFJT1vC-9yNT54y3_c5pPMFPRncXeZt0Ztv5ZnTmf2dA0iQRAtmryUmTE94W4ezx4tfjhrRON2Pl7_41vzU8JZFkcYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKDAL4cWdnVPhCQG8Hs5eRAxz2WpxrNGP8sLUyVai8rQ0PJp4fDYJTayrJmp4SBN0vP0SBuZi3qits8zVfChdU-yteW1VPy1Up37LudDNwPfIc3CAAQB56Kit2FhBRTDp82MVMVeHoHhOutSzj-1CW81up1xVlUi3mVGfRqzpc7Kfo-D6sF9RXl8z-cICAsK7yDuzCo8xX_ez6eUqe5JiKuKqb_LoyKe8WE3UbnkghTesqmoRqzFFjYUNpewe37ysxK_BR8LygArD4thJL_lyYW1fQdRiwbZjmI-IsoprzrUepIYyW5JT7wxy4eVjx247Eas0GL0fO4oubH9u_0IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmwz1gPt2IrGhTClENwhCJQmwAQtyOXNKH55YDPeRbenlR3p9NI9YOYwJvovl05npUlCoPgKrSrQl8EFL-Wr37emudWKJRP2Rg0NzNWAXW2b7RmZPM6HHHQ3kOVIbbrgeW3P6H9wwWilYIqAlt8r1lBl_ed4TIiPj_j7550bYMZc_dcSm59HRtbEkoWaDPDOp-FAPbYGDIxKHqabvEqgGJcy8R6meXXYRVpHgp_2SFtBaYDxgZfFTQfa1F0I2MNt3ZEE7pzZ9KjFrAz0sUNDamXJ_iFgTuQiSNo64iRi_-3hMCHKci9x3eOjOJ1iRQeTu2WfqwYlP2VXNLnuiOY96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tqs13UzFHRUX3px7MeDYI6lVRlBUhQjDotMjGT1_kUq58AwJ0VLF-XyQfe_dr7C9wfX2IsTCjRgOsDuX6ZEnxUbyH1n3W-GGdGlKuLBD_bwT9bxfEPmO042_ACroaZ10GLywCBP4eHgmaejciQgoDA6vGzFAeMoBKj_lhLwn3ipEzrOm4blvWM7P4u_E6ePQlbqoeIdcd5c-YPULL2cR9-3xmR7rbg5O9BswzS5JDwD1gz73Q9kbdrZo3xDSsGrtmPoJ7Y1zQJWQckJSbfdOWjra3u4JaUufrvnvT1hN4wW3oEmbnu25FXrH7H28DsUYA8HHTiDh1kFvWqEJnJsZ5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زندگی در هرمز جاری است
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/465124" target="_blank">📅 22:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465123">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2e0ab091.mp4?token=iYfe9EGndOJ452m1E-W4w7zQxuGacRQni2v-mcSUYqVI3U54Yz1vCNm_W-9PMlt1d2mIhIvTuDEnqAQmr3FlPrObr3I9ait37hEHnr_lo-zj2NMYhv89XxRgDhhCJ18tu_aCrhwVjxmmOuT27nTjG0IrvY3uTZ6gCXce3Fnu_qdowW_AnKS5naqM6IKdCcdCFRG-LQP939oZA8qHtC362-HjB13iWZU7tfjOfO51yijdIm1GElnVak5_T7bYO9uUhQGzX6951y5BnvMrIwfZeY5vwDZdeYHdn_8VDhXEXmFpTjZ8FBzSKT5vKu1AcGd_aigXfnhOF3W02VPsnEskqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2e0ab091.mp4?token=iYfe9EGndOJ452m1E-W4w7zQxuGacRQni2v-mcSUYqVI3U54Yz1vCNm_W-9PMlt1d2mIhIvTuDEnqAQmr3FlPrObr3I9ait37hEHnr_lo-zj2NMYhv89XxRgDhhCJ18tu_aCrhwVjxmmOuT27nTjG0IrvY3uTZ6gCXce3Fnu_qdowW_AnKS5naqM6IKdCcdCFRG-LQP939oZA8qHtC362-HjB13iWZU7tfjOfO51yijdIm1GElnVak5_T7bYO9uUhQGzX6951y5BnvMrIwfZeY5vwDZdeYHdn_8VDhXEXmFpTjZ8FBzSKT5vKu1AcGd_aigXfnhOF3W02VPsnEskqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرت‌زدن ترامپ این‌بار در جلسۀ کاخ سفید  @Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/465123" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465122">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ReudYK30IXILkZLbs8NjaEHpYXAPRFYPZWB3BIM52jDiVDNlyl3rMkLBS4MvMvGNo7UBQt2_qiZZ6maOxt1kfDxRGA_NfSyGVVtvru7ZSFbBydmdMf3DmHLk-FIHlTcM8nsKPqC2ZXXHrInmXX1NdGvZ_0_0cFxkOAx1rbqgaDLBUXVIk0vpBTcU9nf23uR-NY9vidHFAGF9YSFqqL_QwyQ7CM70pj4fsVHKHYdx5qUo6VHT8Sc4m30Vd-Z5KsQ4OcnbpxeNTNTd_edpw6vCk7Snw-pmi2PZC9ePbWStk2thFds12zUxGk90C29hfm22RvEJ7LIQAAVtLhqYzlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان جنگ بر سر مادرشوهر!
🔹
کشوری، مشاور خانواده می‌گوید: یکی از پرتکرارترین دغدغه‌های زوج‌های جوان، به‌ویژه در سال‌های آغازین پیوند مشترک، تشخیص مرز میان وابستگی ناسالم همسر به خانوادهٔ پدری و احترام و محبت شایسته به والدین است.
اگر همسرتان این ۳ ویژگی را دارد، خیالتان راحت!
🔸
مهارت نه گفتن
🔸
اولویت‌بندی و مسئولیت‌پذیری
🔸
مرزبندی شفاف در عین صمیمیت
🔹
شخصیت سالم در گام اول، خود را در قدرت تصمیم‌گیری مستقل نمایان می‌کند. فردی دارای استقلال شخصیتی است که بتواند در مسائل کلیدی زندگی نظیر انتخاب شغل، محل سکونت و مسائل خرد و کلان، بدون دنباله‌روی کورکورانه یا وابستگی فکری به دیگران، نظر خود را ابراز کند.
🖼
اما هر رسیدگی به والدین را باید وابستگی ناسالم دانست؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/465122" target="_blank">📅 22:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465121">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e89c6541e1.mp4?token=oxnpIIvyaSaaLQi9xBpyFdNAF6182qKEVuhvC-6HzTrLJ4qKOcoTblrfy-0e7INW2soati7gjJHkIZl1KTW8jmy7k-3sX3s_waWHWoN17Vn8x5kR6qx636IuAvFc7gXe_h0ldtk5cQekhrDor1nbVA4OHkV-4h7az3gjJx9r2v9FHk17M4gT6jgLuIj5y9Tj3Otv-51JwBf4VJpHqnguCfNRyKLWgn-KrcmexNE2c4UkPQsX_nRtr8ypKcu0ZJsDhW2_GwtCRsUDQiDoV3G-KszvxBhoE8ISBbTIn_-t6XlUYqopDEYJ4MUTUyNuL0MI-Mh3bfkLr3qOvBWGAuBi6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e89c6541e1.mp4?token=oxnpIIvyaSaaLQi9xBpyFdNAF6182qKEVuhvC-6HzTrLJ4qKOcoTblrfy-0e7INW2soati7gjJHkIZl1KTW8jmy7k-3sX3s_waWHWoN17Vn8x5kR6qx636IuAvFc7gXe_h0ldtk5cQekhrDor1nbVA4OHkV-4h7az3gjJx9r2v9FHk17M4gT6jgLuIj5y9Tj3Otv-51JwBf4VJpHqnguCfNRyKLWgn-KrcmexNE2c4UkPQsX_nRtr8ypKcu0ZJsDhW2_GwtCRsUDQiDoV3G-KszvxBhoE8ISBbTIn_-t6XlUYqopDEYJ4MUTUyNuL0MI-Mh3bfkLr3qOvBWGAuBi6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: حاضرم با همین جوانان فعلی به جنگ بروم و حتی نتیجۀ بهتری از دفاع مقدس ۸ ساله بگیرم  @Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/465121" target="_blank">📅 22:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465120">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e0457462.mp4?token=LWHLHW97YYjDd63di7tr43tdSPtIDHMF0G4WvW2Q4_OX86eVrvNXVecz0MbdIbPCkrSmxe-vf8j31LscbKFx2mwUrDHf2cWgJznt85EuCOa6IfEk948ABVGgVLcZUwPpTaN9FUr5AWRpQtri6QDmO7o9Js9MBsMUiDQ2gOuNUHn8jvBPvYmwtYULedag7XW2luN-85wlv_Tk1UP3PlhB1rLTaqyywK0_kTWfdhhnS5uxtI5PMKv-zJSOv_-g2u_uS0oZuVY9dieCch6lQze7qZk8aifhyc-vt4d0DQo2HxZqlJFTFgFSeEJjfXLLstFyd18PRR2IP63DrKghLVo3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e0457462.mp4?token=LWHLHW97YYjDd63di7tr43tdSPtIDHMF0G4WvW2Q4_OX86eVrvNXVecz0MbdIbPCkrSmxe-vf8j31LscbKFx2mwUrDHf2cWgJznt85EuCOa6IfEk948ABVGgVLcZUwPpTaN9FUr5AWRpQtri6QDmO7o9Js9MBsMUiDQ2gOuNUHn8jvBPvYmwtYULedag7XW2luN-85wlv_Tk1UP3PlhB1rLTaqyywK0_kTWfdhhnS5uxtI5PMKv-zJSOv_-g2u_uS0oZuVY9dieCch6lQze7qZk8aifhyc-vt4d0DQo2HxZqlJFTFgFSeEJjfXLLstFyd18PRR2IP63DrKghLVo3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرت‌زدن ترامپ این‌بار در جلسۀ کاخ سفید
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/465120" target="_blank">📅 22:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465119">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c01f8887cf.mp4?token=juPYlWT02TCumb69OAsc1k4kv2egc9nIQZfipxIRuPMxfagjnyJV5gbg6yHJ6XEskqTWPt52VelDiqjD2Cwsx_9T91V-mHV76wIzKDkNmMZct_jMRsB3Rjwe7ivWu_cqDjy2vSfoHPP-sbR5NWX4iSrWrvWbkqBVDpsL3RfOjZEVnu-02FSBDeMOuNsgZzMapUCEp_A-8UjeYSPk_GPpSn86xVrx6A0Hc9gSrbqzo2hznWragQx3NQ1GFCKpjmhoc4KWQPHRJYQI7ApC3wByZdstJHfvHblgxlDC9xcB_rNB86Irm4cMULOArkP0mTn7kd5IT6J7rmA8vCyJqonb9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c01f8887cf.mp4?token=juPYlWT02TCumb69OAsc1k4kv2egc9nIQZfipxIRuPMxfagjnyJV5gbg6yHJ6XEskqTWPt52VelDiqjD2Cwsx_9T91V-mHV76wIzKDkNmMZct_jMRsB3Rjwe7ivWu_cqDjy2vSfoHPP-sbR5NWX4iSrWrvWbkqBVDpsL3RfOjZEVnu-02FSBDeMOuNsgZzMapUCEp_A-8UjeYSPk_GPpSn86xVrx6A0Hc9gSrbqzo2hznWragQx3NQ1GFCKpjmhoc4KWQPHRJYQI7ApC3wByZdstJHfvHblgxlDC9xcB_rNB86Irm4cMULOArkP0mTn7kd5IT6J7rmA8vCyJqonb9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: جنگ ما جنگ اراده است
🔹
دشمن دنبال ایجاد خلل در ماست اما ما مطئنیم ملت ایران ایستاده است. @Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/465119" target="_blank">📅 22:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465118">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7eeebd448.mp4?token=SaMNZ8k_xbgDbMXC3Urnxo7ILG8jHtwjuRmpZIUR0_AVAe03DXXQ4YkrPr126qwUPXxZ30xa2dPrdgw1vlppUdmNwA9b5IX2XoWsvv86Sp6nAIak4FOtLSN-Y4M5MaRJIWTtZxjd8yfm99-raVxnUryletyUBHljdRzaUDNpkl3gwQCPktw9kbQRBJ-Y9txr-crHoW5WYqqaalk85j0phflySxYCxGdsE_-4Va1m-dqPkMmDu6rkDxDUj4u1IAReGh39EsAOGHoI-c_mzydvyQxDeCYGha40FYHz1A0vGopUmtazwaDKFbSwjaW776x6bXodbBpAOTvCKEmnb8ciCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7eeebd448.mp4?token=SaMNZ8k_xbgDbMXC3Urnxo7ILG8jHtwjuRmpZIUR0_AVAe03DXXQ4YkrPr126qwUPXxZ30xa2dPrdgw1vlppUdmNwA9b5IX2XoWsvv86Sp6nAIak4FOtLSN-Y4M5MaRJIWTtZxjd8yfm99-raVxnUryletyUBHljdRzaUDNpkl3gwQCPktw9kbQRBJ-Y9txr-crHoW5WYqqaalk85j0phflySxYCxGdsE_-4Va1m-dqPkMmDu6rkDxDUj4u1IAReGh39EsAOGHoI-c_mzydvyQxDeCYGha40FYHz1A0vGopUmtazwaDKFbSwjaW776x6bXodbBpAOTvCKEmnb8ciCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: امکان ندارد ایرانی‌ها بگذارند دشمن وارد خاک این وطن شود
🔹
ملت و نیروهای مسلح آماده هستند جلوی ورود دشمن را بگیرند. @Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/465118" target="_blank">📅 22:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465117">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a4ce3f84.mp4?token=dnK44dRPhiPpi1HLDYGngdBPF2n1kWYPQ3iIMQzeLsQwM1MVaboMJp4AUDlmtXmN1BKPTrKlXxAKDrEqeweR9zWm272FuA-UL8t5ZhJ0Jf4IppH3NqyLgGBJCFyFqodsh6wuFzwNYhxrcU85BGr0qlvPS4-JrH60FaY-TAMhHWETe5PiYoRB6gjdptLND35-DrXHSYr0aWb-5jxA2zRWbNCiyU_GdBKjSMoq9wYh9QoqxuenK8JmeB6B6uCtXyyHUKoUrmNqIOzj7IXzHFHQIXxon5TqaDwFrd2laV2H5HqXP-pxPYGbt4DmS6lL219aQWo2-nwiNPP-XL_kXRpkdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a4ce3f84.mp4?token=dnK44dRPhiPpi1HLDYGngdBPF2n1kWYPQ3iIMQzeLsQwM1MVaboMJp4AUDlmtXmN1BKPTrKlXxAKDrEqeweR9zWm272FuA-UL8t5ZhJ0Jf4IppH3NqyLgGBJCFyFqodsh6wuFzwNYhxrcU85BGr0qlvPS4-JrH60FaY-TAMhHWETe5PiYoRB6gjdptLND35-DrXHSYr0aWb-5jxA2zRWbNCiyU_GdBKjSMoq9wYh9QoqxuenK8JmeB6B6uCtXyyHUKoUrmNqIOzj7IXzHFHQIXxon5TqaDwFrd2laV2H5HqXP-pxPYGbt4DmS6lL219aQWo2-nwiNPP-XL_kXRpkdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: تسلیم در قاموس ایرانی جماعت نیست
🔹
ملت ایران تسلیم‌پذیر نیست و ایرانی‌ها اجازه نمی‌دهند کسی از بیرون برای آن‌ها تصمیم بگیرند. @Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/465117" target="_blank">📅 22:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465116">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23302f6569.mp4?token=OzZpd7Q3DkO8uVhhjpwIkQUxcKCyoY6VbV5WxaMX6YZBthP4IsN3agYYFiIIDwprS2CKSgGsBjM5pVz1fHXb5hcwiFvcLSZmuL_HMH2vNqQoWJ_w_aqrU1_hGLmVOfO7-oJAX3jOVzH8qzQkWy9nFBRymjb9AOB8gTZg1lbuXkGobNXgeQRgmsr6cMYahkU8vpt3VKxnzfuWa4E2UjsMm68JorLHKmocgF61P_rfogmLOvVQP1h5DVmeh5HP3mXFWiuLrJXfUz9Io0rxVCkxxpReaRFINnS1QZ4h9MrzR5qgVZo8BhefPDToCWLBds6LqALbTzmUGe7ypExRxz-3sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23302f6569.mp4?token=OzZpd7Q3DkO8uVhhjpwIkQUxcKCyoY6VbV5WxaMX6YZBthP4IsN3agYYFiIIDwprS2CKSgGsBjM5pVz1fHXb5hcwiFvcLSZmuL_HMH2vNqQoWJ_w_aqrU1_hGLmVOfO7-oJAX3jOVzH8qzQkWy9nFBRymjb9AOB8gTZg1lbuXkGobNXgeQRgmsr6cMYahkU8vpt3VKxnzfuWa4E2UjsMm68JorLHKmocgF61P_rfogmLOvVQP1h5DVmeh5HP3mXFWiuLrJXfUz9Io0rxVCkxxpReaRFINnS1QZ4h9MrzR5qgVZo8BhefPDToCWLBds6LqALbTzmUGe7ypExRxz-3sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: تنگۀ هرمز بسته است
🔹
از خلیج فارس تا شمال اقیانوس هند برای ایران است و اجازه نمی‌دهیم هیچ قدرت دیگری در این منطقه قدرت‌نمایی کند. @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/465116" target="_blank">📅 22:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465115">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e549f4f88.mp4?token=nKmproJzdU4Zb4j6AW368h-H9iNVa0V9TciH2P26F1mA7ypdGv94hfXFtgeZXdFesRuGNvgS05fbl2WKdMYKPwFvdDNTN5SdeJZfDEg7BQyMEvqVGUZU0blqqBMiAmPHrTTtZiC643DLbUl0HTMgbizy7AO7YtCcoxnTu-VgfpkgpicOfrkJ49cr_94oBNEYOhAZYhuW0lt6CiPM01FV5g0ZWg8ORSkx5p0nGMl3YHnL-70HVebIYDX1TDEIs_fikwtMeSEwUs65mPE5JZqNw0AYzRgYPTOp8QXqWBQD5B2GYkjRtWH7h72EbabkslQSMydmp4RzBPwe9zRLD4ippQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e549f4f88.mp4?token=nKmproJzdU4Zb4j6AW368h-H9iNVa0V9TciH2P26F1mA7ypdGv94hfXFtgeZXdFesRuGNvgS05fbl2WKdMYKPwFvdDNTN5SdeJZfDEg7BQyMEvqVGUZU0blqqBMiAmPHrTTtZiC643DLbUl0HTMgbizy7AO7YtCcoxnTu-VgfpkgpicOfrkJ49cr_94oBNEYOhAZYhuW0lt6CiPM01FV5g0ZWg8ORSkx5p0nGMl3YHnL-70HVebIYDX1TDEIs_fikwtMeSEwUs65mPE5JZqNw0AYzRgYPTOp8QXqWBQD5B2GYkjRtWH7h72EbabkslQSMydmp4RzBPwe9zRLD4ippQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: مهاجمی که به اهداف خود نرسد یعنی شکست خورده
🔹
در هر ۳ جنگی که به جمهوری اسلامی ایران تحمیل شد دشمنان به اهداف خود نرسیدند و این یعنی شکست دشمن.
🔹
صدام فکر می‌کرد زمانی که به مرزهای ایران برسد از او استقبال می‌شود؛ ترامپ هم فکر کرد مردم ایران…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/465115" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465114">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537d31073e.mp4?token=l8tTs23ND_N9ccnauBzVnd8XPFtsOyHCT0rW1e4sPCheWDQDXSkTvhDpzHnR1L1LUsmmQ21wFk8M76d0keYgYG08-Z1lnxLcPTm8EZs4yFGPOaUHVVwmp7EZV1OSAryx6axw4liZTnADPWzLJQRl6KhHTa1XHaykCvmslLpqN3ggaKKpx_fQJ9QgaxVq-UPii40O20ECLVI7lJuvw0olPtQEdZfBgtW7TnoHnoqYM4yh3nD7EWnr4ALhkqE68gv50YX5vkodcoH7dBFRLV5dKXo-Nr0cefsn8Hv1Kma7Qp_iPwvUP5-aACEjTpR5bjNCLVoIAwmrDKd0mLKZEYM2tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537d31073e.mp4?token=l8tTs23ND_N9ccnauBzVnd8XPFtsOyHCT0rW1e4sPCheWDQDXSkTvhDpzHnR1L1LUsmmQ21wFk8M76d0keYgYG08-Z1lnxLcPTm8EZs4yFGPOaUHVVwmp7EZV1OSAryx6axw4liZTnADPWzLJQRl6KhHTa1XHaykCvmslLpqN3ggaKKpx_fQJ9QgaxVq-UPii40O20ECLVI7lJuvw0olPtQEdZfBgtW7TnoHnoqYM4yh3nD7EWnr4ALhkqE68gv50YX5vkodcoH7dBFRLV5dKXo-Nr0cefsn8Hv1Kma7Qp_iPwvUP5-aACEjTpR5bjNCLVoIAwmrDKd0mLKZEYM2tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: مجلس طرح سه فوریتی خروج از NPT را بررسی می‌کند
🔹
نیکزاد: ما اصلاً به آژانس و مدیر فعلی آن اعتماد نداریم؛ چرا که وی صرفاً بازدیدهای ظاهری انجام می‌دهد و گزارش‌های منفی علیه ایران ارائه می‌کند.
🔹
طرح‌ سه فوریتی خروج از NPT در حال بررسی است و بعد از اعلام وصول همان روز مورد رسیدگی خواهد گرفت؛ البته مجلس ابعاد بین المللی آن را هم بررسی خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/465114" target="_blank">📅 22:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465113">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128ab20b4c.mp4?token=CEI9QCQr-ATyxJvPyKU6nvlIMLG1dj89ZyBtJr9qCzsBhAJU8BY_sdLpJHMD7cypZgUNeWntkY3zH61ASk7b1grUVHTHMdZbJPe8tDP_3eI_uNpPjicDJrKtdnvqvaSDn7nbGeBBgyzktH8pwt1QDpLwgELYqbVfwmVTQppPQj3qeVgCC2099PpNbbdNYqKIa5bAJM2uHfqf2CWpXUUsSKIz0WCW2WzECdeqUZIPfiA2kodumm4wISQWYl97Cnwoxfs93uKMmQ_h7A4iY3z3uys_y5rposIeiVQ7oMBpoBOoNKfZxA-bNNKilTSDsDlwTpYd_RWz2fVMho3w4FaS8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128ab20b4c.mp4?token=CEI9QCQr-ATyxJvPyKU6nvlIMLG1dj89ZyBtJr9qCzsBhAJU8BY_sdLpJHMD7cypZgUNeWntkY3zH61ASk7b1grUVHTHMdZbJPe8tDP_3eI_uNpPjicDJrKtdnvqvaSDn7nbGeBBgyzktH8pwt1QDpLwgELYqbVfwmVTQppPQj3qeVgCC2099PpNbbdNYqKIa5bAJM2uHfqf2CWpXUUsSKIz0WCW2WzECdeqUZIPfiA2kodumm4wISQWYl97Cnwoxfs93uKMmQ_h7A4iY3z3uys_y5rposIeiVQ7oMBpoBOoNKfZxA-bNNKilTSDsDlwTpYd_RWz2fVMho3w4FaS8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: کشورهای حوزۀ خلیج‌فارس در جنگ ۸ ساله به صدام امکانات دادند و در این جنگ هم پایگاه‌ها را برای حمله به ما دراختیار دشمن گذاشتند  @Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/465113" target="_blank">📅 22:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465112">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac75508d5.mp4?token=KRTdQcCuXgIYTsdnNYiaZGQo2_IvMzWuR4G7X0POZhP14X0ZBKwrkQhAgFUBsFkIOsOLLZTyfgV9TwrVFKe26AbHhFfigfezZQD9td_LTgONhqTayi1hakV9Hp7VApVI2hXMEVlRjs9XNNy3rlZF8XXCPZXofmS_aKe3KMlENZVmnW8MqqV78SB5T7mJbjeVFj-u_1N8snW8ttb5svoSA7cfmEfNFs8i0XP5tPokrVDdB_ES0uT3t8AsEL6fI0ugnnigkEMzyTGDVs1dNa8mzLNrXeXA6Z_IlvLoWYww1_Aj2t5z63AxWwZL_MLCGkXtdAQn83eeHHSrZwpswNaPQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac75508d5.mp4?token=KRTdQcCuXgIYTsdnNYiaZGQo2_IvMzWuR4G7X0POZhP14X0ZBKwrkQhAgFUBsFkIOsOLLZTyfgV9TwrVFKe26AbHhFfigfezZQD9td_LTgONhqTayi1hakV9Hp7VApVI2hXMEVlRjs9XNNy3rlZF8XXCPZXofmS_aKe3KMlENZVmnW8MqqV78SB5T7mJbjeVFj-u_1N8snW8ttb5svoSA7cfmEfNFs8i0XP5tPokrVDdB_ES0uT3t8AsEL6fI0ugnnigkEMzyTGDVs1dNa8mzLNrXeXA6Z_IlvLoWYww1_Aj2t5z63AxWwZL_MLCGkXtdAQn83eeHHSrZwpswNaPQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: کشورهای حوزۀ خلیج‌فارس در جنگ ۸ ساله به صدام امکانات دادند و در این جنگ هم پایگاه‌ها را برای حمله به ما دراختیار دشمن گذاشتند
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/465112" target="_blank">📅 22:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465111">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJjSH81f0Sp6xjeR7YcFsRznS_rY3n13D6igx5JiIlIEPjXQ10nbrLbL0FE34Old7funXphnTIKE62LZOgEPnRO2liti6jbwanOor13Cw22RJhAAZ9JBTM88zoH_D8nVqyb7VbiZTwrtHB2_oKMTqg3RbIYTo8uEgduanydxPEzkNY22g9z3ZKPM6XnpnhvKooud479xGTPRtoVt8lpswklncQ-vLZ8QKp4P_MMO9-homXCUJumrj_bEEOm_fbDAl1TY_SQjJ2amDOy_exuIYA77gh5zRAehpliQ0KxlZoC4mETjEx-tKncc5jJ2oJmmOVqlaViEQDoAhs470V59jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نامۀ آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب به برادرشان در دوران دفاع مقدس
بسمه ‌تعالی
🔹
خدمت برادر عزیزم، رزمندۀ گرامی سیّدمصطفی، بالاخره پس از مدّتها که قصد نامه نوشتن را کرده بودم موفّق به چنین امری شدم.
🔹
جای شما خالی، ما در مشهد پس از زیارت و دید و بازدید از سبزوار بازدید کردیم. استقبال مردم خیلی خوب و دلگرم کننده بود. امّا خوب، جای ما هم در آن محیط صفا و خلوص و عشق به خدا خالی. ایکاش باز هم توفیق پیدا کنیم و در آن مکان الهی حضور پیدا کنیم.
🔹
بعد از اینکه به تهران آمدیم من دائماً در صدد تهیّۀ کتاب درسی و اسم‌نویسی در مجتمع رزمندگان بوده‌ام تا اینکه دیروز موفق به اسم نوشتن شدم.
🔹
قرار است همگی چند سطری در ادامۀ این دو نامه بنویسند و من از طرف بشری و هدی هم سلام میرسانم. امیدوارم در پناه توفیقات حضرت حقّ انجام وظیفه (بطور احسن) را بنمائی. زیاد وقتت را نمی‌گیرم و تو را به خدا میسپارم.
والسلام. سیّدمجتبی
چهارشنبه ۹ مرداد ۶۵
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/465111" target="_blank">📅 22:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465110">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
چند سال است نسبت به وضعیت
حضور اتباع افغانستان در ایران
و پیامدهای احتمالی آن در حوزه‌های اقتصادی، اجتماعی، فرهنگی، امنیتی و انرژی نگران هستم و حتی این موضوع را از طریق مجلس نیز پیگیری کرده‌ام. بر اساس برخی آمار و برآوردهای منتشرشده، شمار اتباع افغانستان در ایران بین ۷ تا ۱۰ میلیون نفر اعلام شده؛ جمعیتی که از مجموع جمعیت چند استان کشور بیشتر است. سؤال ما این است که چرا درباره ابعاد این موضوع و آثار آن، بررسی و اطلاع‌رسانی شفاف و جدی انجام نمی‌شود؟
🔹
چرا
حقوق یک کارمند قراردادی دولت
باید حدود ۳۵ میلیون تومان باشد و
افزایش آن سالانه بسیار کمتر از رشد هزینه‌های زندگی باشد؟
در حالی که قیمت کالاهای اساسی و هزینه‌های زندگی به‌شدت افزایش یافته، دخل و خرج مردم دیگر با هم نمی‌خواند. بنده با درآمد ماهانه ۳۵ میلیون تومان، ۲۷ میلیون تومان آن را صرف اقساط بانکی می‌کنم و برای تأمین سایر هزینه‌های زندگی با مشکل جدی مواجه هستم.
🔹
من از اهالی روستای
پشگ، بخش چاه‌دادخدا، شهرستان قلعه‌گنج کرمان
هستم. مردم این روستا با مشکلاتی مانند نبود آب آشامیدنی، جاده مناسب، خدمات بهداشتی و درمانی، دوری از مراکز درمانی و کمبود فرصت‌های شغلی مواجه هستند. خواهشمندیم مسئولان برای رفع این مشکلات و در صورت امکان، جابه‌جایی روستا به محدوده‌ای نزدیک‌تر به جاده و مراکز درمانی و همچنین واگذاری زمین مسکونی به اهالی اقدام کنند.
🔹
با گذشت نزدیک به یک سال از نصب
دکل ایرانسل در روستای اکبرآباد رشتخوار خراسان رضوی
، اهالی همچنان از تماس تلفنی و اینترنت پایدار محروم‌اند. دکل به‌جای اتصال به برق سه‌فاز اختصاصی، به‌صورت موقت به برق دهیاری متصل شده و به همین دلیل یا خاموش است یا تنها ساعاتی از شبانه‌روز فعالیت می‌کند. اهالی از
ایرانسل، اداره برق و دهیاری
درخواست دارند هرچه سریع‌تر
مشکل انشعاب برق دکل
را برطرف و آن را به برق سه‌فاز اختصاصی متصل کنند. نصب دکلی که یک سال است بدون استفاده مانده، علاوه بر هدررفت منابع، مردم روستا را از یک خدمت ضروری ارتباطی محروم کرده است.
🔹
برای احداث سردخانه و صنایع تبدیلی به
ستاد حمایت از سرمایه‌گذاری و جهاد کشاورزی
مراجعه کردیم، اما نزدیک به یک سال است
با موانع و تأخیرهای متعدد مواجه شده‌ایم.
این تأخیر باعث شده هزینه احداث پروژه از حدود ۶۰ میلیارد تومان به بیش از ۱۵۰ میلیارد تومان برسد و عملاً سرمایه‌گذاری برای ما بسیار دشوار شود.
🔹
شما هر روز اعلام می‌کنید مدارس دولتی حق دریافت شهریه از دانش‌آموزان را ندارند، اما از طرفی بسیاری از
مدارس دولتی سرانه کافی دریافت نمی‌کنند
و هزینه‌های جاری آن‌ها عملاً از کمک‌های مالی خانواده‌ها تأمین می‌شود. حتی اگر سرانه‌ای هم پرداخت شود، به گفته مسئولان مدارس برای تأمین هزینه قبوض آب، برق و گاز نیز کافی نیست.
🔹
خواهشمندیم موضوع
صدور کد استخدامی اعضای هیئت علمی فراخوان‌های سال‌های ۱۳۹۹ تا ۱۴۰۲
به‌صورت جدی پیگیری شود. این افراد دارای ابلاغیۀ رسمی جذب از وزارت علوم هستند و تمام مراحل قانونی جذب آنان نیز در سامانه یکپارچه جذب ثبت و مستند شده است. با این حال، بسیاری از آنان ۳ تا ۶ سال است در انتظار صدور کد استخدامی و حکم خود هستند و برخی نیز با اعتماد به فرآیند رسمی جذب، از شغل قبلی خود استعفا داده‌اند و اکنون با مشکلات معیشتی مواجه‌اند.
🔹
حقوق من ۱۹ میلیون و ۵۰۰ هزار تومان است
. به‌خدا شرایط رفتن از کشور را دارم اما ایران را دوست دارم و بارها تا مرز استعفا رفته‌ام و دوباره پشیمان شده‌ام. من تنها قطره‌ای کوچک از دریای همکاران توانمند آموزش و پرورش هستم، اما با این میزان حقوق واقعاً تأمین هزینه‌های زندگی دشوار است. خواهشمندیم مسئولان محترم فکری جدی برای
وضعیت معیشتی و حقوق فرهنگیان
کنند.
🔹
برای خرید مواد پروتئینی
با کالابرگ به چند فروشگاه مراجعه کردیم اما فروشگاه‌ها می‌گویند به‌دلیل پرداخت نشدن مطالباتشان از سوی دولت،
دیگر کالابرگ قبول نمی‌کنند.
🔹
لطفا مسئولان مربوطه توضیح دهند چگونه خودرویی که حدود پنج سال است پلاک آن توقیف شده، همچنان امکان تردد دارد. از سوی دیگر، چرا شرکت‌های بیمه هنگام صدور بیمه‌نامه، وضعیت پلاک و مالک اصلی خودرو را بررسی نمی‌کنند و اصولاً
خودرویی با پلاک توقیف‌شده چگونه می‌تواند بیمه شود؟
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/465110" target="_blank">📅 22:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465109">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cc2f59eb.mp4?token=OYuv62zhrEleh1k2OtxxgVlF__cDZCW_04WL229Q9W0k6otp6WwHNKPU4ZRue5xF65ZbPBFgEqRqmB-9UDPMTvtKZAA26AOlC5k7p_tqj8xFE-xjo9VxVQDNgLG9LqiCdE00LfGeXNcTOvvECGbOmMMGXY2Jw8Tx2ffmScjwvbuayTmRsEDWtc8OWBXTOiV44uLslw7xzWgJXRf7N6Bp1hPPgAbBGlh6HH-i_2hMYpQEbA79pcYuZ87UV3WHCCRkn4c9jZstA1ukwp782RbGMFxNEdqLtcUFZYZ5GcZfQ6yygoQtZ75IwdJaf39acxXTMPxYPKPRix_APPiXPjCD7BrAqvY8La3Dh89rtHRbmoBc78inK06IEKYL5LBe8sUs16orl8_hpMRO7pOuroZfQRo4Sdpy3YsRjvpx_7JjlTNVDWQLaOHZ4O3TLxEZdiABHBFZR_sD75yl5ZcIHjutkcYuiaZM96QKB70U84_cqAxNNIFqyRgIt4E93q9a-ApidPP0sgK3c9vQfV74R4-oy-dMCmZSjPSH7nwRUVmG1RnumlawtRr0AVsDbKOf9i6quVJhy9GFNrFUCd5O8EY7EPGYzeMxRu6-1rm8mLa_TXrvHYNCwU7kunyo1A_eAYuaLBnSw-VFXla0GVZ3zR4GgyvcYFj1vAQtuDFBMyznAak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cc2f59eb.mp4?token=OYuv62zhrEleh1k2OtxxgVlF__cDZCW_04WL229Q9W0k6otp6WwHNKPU4ZRue5xF65ZbPBFgEqRqmB-9UDPMTvtKZAA26AOlC5k7p_tqj8xFE-xjo9VxVQDNgLG9LqiCdE00LfGeXNcTOvvECGbOmMMGXY2Jw8Tx2ffmScjwvbuayTmRsEDWtc8OWBXTOiV44uLslw7xzWgJXRf7N6Bp1hPPgAbBGlh6HH-i_2hMYpQEbA79pcYuZ87UV3WHCCRkn4c9jZstA1ukwp782RbGMFxNEdqLtcUFZYZ5GcZfQ6yygoQtZ75IwdJaf39acxXTMPxYPKPRix_APPiXPjCD7BrAqvY8La3Dh89rtHRbmoBc78inK06IEKYL5LBe8sUs16orl8_hpMRO7pOuroZfQRo4Sdpy3YsRjvpx_7JjlTNVDWQLaOHZ4O3TLxEZdiABHBFZR_sD75yl5ZcIHjutkcYuiaZM96QKB70U84_cqAxNNIFqyRgIt4E93q9a-ApidPP0sgK3c9vQfV74R4-oy-dMCmZSjPSH7nwRUVmG1RnumlawtRr0AVsDbKOf9i6quVJhy9GFNrFUCd5O8EY7EPGYzeMxRu6-1rm8mLa_TXrvHYNCwU7kunyo1A_eAYuaLBnSw-VFXla0GVZ3zR4GgyvcYFj1vAQtuDFBMyznAak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری بروجردی‌ها به یاد شهید سیدحسن نصرالله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/465109" target="_blank">📅 21:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465108">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsnzKMmWIpb2hu4FFCsV6YnosqW5Xq6PSUEZ6zrlZ-U_S2CKKEF7S0l9tyMGljlzQFsoSBql77jPmTuiK_XwvnU4VS4WtoqRriCKUWqhpV6vGZp6LPIAvjWzOrDJdIF6tx7jxQd51Ne70Mx3a2hCBXR8TUggfR660h922UgWUdsivd_TCL-z1NnsFkWvetWDRen6XZA7bKjFsvgDVXtjfJ2B3s7s_hL5GsOHAtM1cx7D9yqaxeNHg09GJ8ughj3W8IksPFWznjRRrwqt5O0Q5PVKVWSeaCbXGwDA8QyXKVpLm2Tg8FxbhC8CUcvHDFCgajzI8HNqCp2lsHkLMuwnOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران در نیمۀ اول امسال یک سد لتیان آب صرفه‌جویی کرد
🔹
سخنگوی شرکت آب‌وفاضلاب تهران: اوج مصرف آب تهران در روزهای گرم مرداد امسال به حدود ۳ میلیون و ۴۵۰ هزار مترمکعب رسید که حدود ۶۰۰ هزار مترمکعب کمتر از رکورد سال ۱۴۰۳ بود.
🔹
میزان صرفه‌جویی آب تهران در ۶‌ماههٔ امسال به اندازهٔ یک سد لتیان رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/465108" target="_blank">📅 21:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465107">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3b4129d31.mp4?token=NlnDEHCALH1J6S0aG8x5HpAwIVZ239RZZlyYR4E1DRMm6ZarUs3QDWqdHjNzKhYsjIBKALaD7-XOtSAtUdYSIhXN8KCUo2CuA8s0Pka55JBY8hID4B9Oo2TZZ9ObEgJVdybFf8rtqKzWFKXuvOYPC31sIBO7sAvJa3A8A98t1IL9sdhGSPN50DifppqFcjrmexTt4-8occVmqm_pc-nkWRMvs7jZf3-bj6CJyngDAnH-NVHdeORZZUTH4xT16Vouz5-RcW_yh2X3c-5JVHIelNDPuwzil_yLeFFIfOtXytpVoNZKdVtS8dJZKEjZW1tE5RBXT6z77rPEgsuLtb5rOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3b4129d31.mp4?token=NlnDEHCALH1J6S0aG8x5HpAwIVZ239RZZlyYR4E1DRMm6ZarUs3QDWqdHjNzKhYsjIBKALaD7-XOtSAtUdYSIhXN8KCUo2CuA8s0Pka55JBY8hID4B9Oo2TZZ9ObEgJVdybFf8rtqKzWFKXuvOYPC31sIBO7sAvJa3A8A98t1IL9sdhGSPN50DifppqFcjrmexTt4-8occVmqm_pc-nkWRMvs7jZf3-bj6CJyngDAnH-NVHdeORZZUTH4xT16Vouz5-RcW_yh2X3c-5JVHIelNDPuwzil_yLeFFIfOtXytpVoNZKdVtS8dJZKEjZW1tE5RBXT6z77rPEgsuLtb5rOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی از وقوع انفجار در خط لولۀ گاز در دیرالزور واقع در شرق سوریه خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/465107" target="_blank">📅 21:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465106">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb2x6VljiwNEC-pGEsWTIQAJJg5Wztie4UHKhhri1UQ9hOevCYh5CrSZfwpGERRG-kPgNI8BvlZCtfYLRmM01eRvmbKgvmF3L6wWqMpUVqJk1q_1ZFmsoLhCRA7vWkQOCS-HDtAe6BZu_BdxzrQXsvn-Q9DV9wBu5xO48bOQTh_3nl-LPhCL953aKhCGx7SBS8FZID43X5yHIX-mwXVdvTp1ieJGqbTMPj3GxPD_Dg30yZhwDDP108OQRx4KOPLvaGPlT96VUP5URn0-FmXESMfylq6m2UvhnmpEDcgPPurfZl_sLk2gyyLPLchHpKuMy5qSP3XMELlWUW52_c-1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق: پروندۀ حضور نظامی آمریکا تا دو روز دیگر بسته می‌شود
🔹
سخنگوی نخست‌وزیر عراق: نیروهای آمریکایی و ائتلاف بین‌المللی قرار است تا ۳۰ سپتامبر (دو روز دیگر) روند خروج خود از عراق را تکمیل کنند؛ بغداد همزمان بر کنترل کامل اوضاع امنیتی و پایان حضور نظامی خارجی در کشور تأکید دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/465106" target="_blank">📅 21:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465105">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e74ff2b8.mp4?token=QNSbrSefcHxPU4F9S5M6EZ1zzVsek5MZJgFSwrwZQR21A_gP4IlgGobOgIvQi3FmyenI7MdI5p_FNbDKwC8g4M_AV3DSFomGhHXtDBf9Gahi2obs2QV14Z6L63psCLNaw3xLDClmeXVaGgB34xixPQKW865btyNzkGRXMMXNP5ZuEWMUT0ZMJAsohJvFYxlL8etBGY8-EEOgdaa2P4N8rpG5IXo1Di5BTUm_xBzn123zMW1ApgN_hxBJbWjmlXGYMEqivpfnPyUQpgsHx66qoG_Zd9ReIGrrDCrakOzeYu-EwT2uB3LfxhcXGi31A73_blQ7Q5Hcx2C4FLDLAW9b6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e74ff2b8.mp4?token=QNSbrSefcHxPU4F9S5M6EZ1zzVsek5MZJgFSwrwZQR21A_gP4IlgGobOgIvQi3FmyenI7MdI5p_FNbDKwC8g4M_AV3DSFomGhHXtDBf9Gahi2obs2QV14Z6L63psCLNaw3xLDClmeXVaGgB34xixPQKW865btyNzkGRXMMXNP5ZuEWMUT0ZMJAsohJvFYxlL8etBGY8-EEOgdaa2P4N8rpG5IXo1Di5BTUm_xBzn123zMW1ApgN_hxBJbWjmlXGYMEqivpfnPyUQpgsHx66qoG_Zd9ReIGrrDCrakOzeYu-EwT2uB3LfxhcXGi31A73_blQ7Q5Hcx2C4FLDLAW9b6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای فرزندان مسئولانِ مفقودشده در دفاع مقدس
@Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/465105" target="_blank">📅 21:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465104">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjzgrWytyc5Wo4u4y3p3a6-H5KoHX4f8HTJW7c7c8ZzLQpCbZZ89mQpPjvHZCLiT8r8zHX3dWtVD1s6iSXcE8K92CPlP8bC6Bj7hRRLD2XJh6rE8YKxtjnreYiZ1F9eqROWX2ZPpZterCzVnYWZ1ccF6yjFo4DeHeh6kHIFQxCoGBVHgXNZWREpevVmapLLE0GxtgU1LDIaOpgjO_5PpeukgAkNWcV8CpskHz1R8XMfzgk2jiZE-lvnAttMzohRNi5W4R6qeJODETHd92BaPB0APLcuyYZLaeLYU3Sd_SbEpibrCciOK2KqgrAnAYL5ZdcW8es0KKY54kBOkITG-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ خطای استراتژیک اصلاحات که به ضرر ایران تمام می‌شود
🔹
یکی از الگوهای تکرارشونده در منازعۀ ایران و آمریکا، هم‌زمانی فشار خارجی با شکل‌گیری مطالباتی در داخل کشور برای تغییر محاسبات تهران است؛ الگویی که منتقدان جریان اصلاح‌طلب معتقدند به‌جای آنکه فشار آمریکا…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/465104" target="_blank">📅 21:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465103">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dc75bdf8.mp4?token=Ws-mMwBDQxgP4Z9hCIH7nNnlE9cNXuX8goKIvMFI0zqXMLhD_bkWfk9aWlbyx2N02gpp54U_upQRi2g7DifKUi7mv9jDXyJRQrOUOJ-OOpRwJ0uDsR4mtqxDvk9G2xNl7-hSjQM2NRH79OAuPZjsWgIPun6rYUUns_D3kjh414NUBrMfdQ0Mbp60GB467Q5-ay3QH4MySxEapg5ACJUe-OufkPZIEZ4sYUPp94tKf1aCBpH-ugIDfFb8ZnNlE9vg2n5FJYLWR1pcH3Evkwf_iyRpCJ3UrYjYxWGBFlvaN7tN5VvvVicFa5oPZ8vowiS9VOyV7qatILUZ7ySHR9qTKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dc75bdf8.mp4?token=Ws-mMwBDQxgP4Z9hCIH7nNnlE9cNXuX8goKIvMFI0zqXMLhD_bkWfk9aWlbyx2N02gpp54U_upQRi2g7DifKUi7mv9jDXyJRQrOUOJ-OOpRwJ0uDsR4mtqxDvk9G2xNl7-hSjQM2NRH79OAuPZjsWgIPun6rYUUns_D3kjh414NUBrMfdQ0Mbp60GB467Q5-ay3QH4MySxEapg5ACJUe-OufkPZIEZ4sYUPp94tKf1aCBpH-ugIDfFb8ZnNlE9vg2n5FJYLWR1pcH3Evkwf_iyRpCJ3UrYjYxWGBFlvaN7tN5VvvVicFa5oPZ8vowiS9VOyV7qatILUZ7ySHR9qTKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام  شاه ایران به سازمان فاضلاب انگلیس
🔹
در زمانی که مردم ایران لباس‌های خود را در جوی‌های آب می‌شستند.
@Fars_plus</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/465103" target="_blank">📅 21:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465102">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌  حمایت سران حکومت عراق از بازگشایی فرودگاه نجف به‌روی پروازهای ایران
🔹
سران قوای عراق شامل ریاست‌جمهوری، نخست‌وزیری و سران دو مجلس از خواستۀ دولت این کشور برای معافیت فرودگاه نجف از توقف پروازهای ایرانی حمایت می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/465102" target="_blank">📅 21:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465101">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR21TA2HutZzVJHksCTZoGtJNFLyiaAaNen717GHnbc_yIUwW9Id2RrncIbpE0Y9uT1ankyueSfIwSLSZwz-uvSaOdkhMwle35DKgipzm8jjhcQXSXmbGs-bJx8f-u45H1Q8kX45eHw0xVh1WvWAQSSTyBxfHcedBMF_nqS7v4uVIPQWNypqPB1LqoSkSWE64sAAb89mLQfAA6JIa2SVzjIWiR3Ulc-3xw9lMuewBRqqDWiBY_2jBdOj2JVKIN6a4SC3ENLtK9OmdtOB9NklbMyvqICPvTaEMqqTFmsxbjgVG1Luyog9_EXSurJGhyV6isSyasnzN1j4Q2gIfJacQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر، عشق، پسر
🔹
نامۀ‌ای که رهبر شهید برای فرزندشان آیت‌الله سیدمصطفی خامنه‌ای در هنگام حضور وی در جبهه‌های دفاع مقدس نوشتند:
بسمه‌تعالی
مصطفای عزیز
امید است سالم و شاد و در آن محیط صفا و خلوص، غرق ذکر و توجه و سرگرم خودسازی باشی.
البته لطف خدا شامل حال تو است مثل همیشه، و انشاء‌الله بیشترین استفاده را خواهی برد.
نامۀ تو را بعد از برگشتن از مشهد دیدم، ظاهراً تاریخ ۲۷ تیر را داشت.
اقامت من در مشهد هفت روز بود، نیمی به کار فشرده و نیمی به استراحت گذشت. جای تو در هر دو قسمت خالی بود، بچه‌ها را با خود به نیشابور و سبزوار بردم تا آیات و برکات الهی را در اجتماعات بزرگ و پرشور مردم ببینند و عظمت مردم را که رشحه‌ئی از قدرت خدا است درک کنند.
درباره‌ی خطّ و ربط سیاسی مواظب باش در دام بحث و مجادله نیفتی که نه دنیا دارد نه آخرت. گاه کلمه‌ئی ارشادی بی هر تعریض و تصریحی علیه این و آن بد نیست، مشروط بر آنکه امید ثمری باشد و الّا فلا.
اطرافیان را به تقوا و ورع و عبادت و یاد دعوت کن البته با توجه به این درس که کونوا دعاة الناس بغیر السنتکم.
ترا به خدای عزیز حکیم می‌سپارم.
در مورد توصیه‌ی مطالعه و کتاب، قدری توضیح بیشتر بده تا انشاء‌الله بفهمم چه باید کرد. ۶۵/۵/۷
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/465101" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465100">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA7sJvZNoARU9B5jFo_OEqD_IvWw3mUJRc4xt4kHgRPmPZlQr-8zkVqhrszT4GsaSnlBwxYPgRaER1CCJwfGo0t-RcagmQ14VEGlfjGoY7_1xz91meeTI-0vxfvDZp4MFJuCajau39ARRnZ9F5p--ejnBrgcQbLBM5hojWRteZILAEx5ZcDYro7nsUGE0TbYUhrirn2mhdZGC6DwdbFsOGCuUj8fXy8xy-Q5EJ9jPIYEpJ_i0DGRZm89710ePNEH0J24pPnOYgRs96JZuZ0NkJVQ2f7MAWURAhIsWs_PzykEnQ4mwuGrpy9-SAggKkrhbYwyeNH3lPpgaGyEytdlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۱۱ خبر امیدآفرین در حوزه‌های اقتصادی، فرهنگی، علم و فناوری و زیرساخت‌های کشور
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/465100" target="_blank">📅 21:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465099">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q24RxBAq5PRPaP_KmwHaPgKUvDjsjWfcg3GKtjDiIOnjHrvoAG5IyN8YfBpYiES53XINzf6Ghr5Q51rCF2zKZUlbQHiWnCgqXoCUZw8UR_pyKaxezHythcDnmgo3yJo9EkL0ZBr2U4mah2HgsQFxtsO2gsecFESQ79pDoQBgZGayNtqms_6xJfpIdrAXIOP5CflM4KJ-ibkh_hdmQ92g3ekYBl4q8V0EF9vwHZEvQhjjE7mHxYL4HvxEZZwFafvvTojn9tC6xkocsWf8kOc16AEqYgDn7iLoLxH0KQGcoIhVGyYkKxNbBRsaRb8Wyre3-izHgkIUMuOcMyEEnrnhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کُند بودن پاتریوت‌های آمریکا برای مقابله با موشک‌های روسی
🔹
بر اساس گزارش منتشرشده در نیوزویک، صنایع دفاعی روسیه در ماه‌های اخیر تولید موشک‌های بالستیک و پهپادهای جت‌موتور را افزایش داده‌اند؛ تسلیحاتی که به دلیل سرعت بیشتر نسبت به پهپادهای قدیمی‌تر، فشار بیشتری بر شبکه پدافند هوایی اوکراین وارد می‌کنند.
🔹
طبق آمار مطرح‌شده در این گزارش، روسیه در هفت ماه نخست سال جاری ۵۸۷ موشک بالستیک شلیک کرده است؛ رقمی که از مجموع ۵۱۱ موشک بالستیک شلیک‌شده در کل سال ۲۰۲۵ بیشتر است.
🔹
در یکی از حملات اخیر، نیروهای روسیه در شب ۲۶ تا ۲۷ سپتامبر ۱۷۰ پهپاد به سوی اوکراین پرتاب کردند که ۷۶ فروند آنها جت‌موتور بودند. مؤسسه مطالعات جنگ نیز گزارش داده است که روسیه در حال استفاده گسترده‌تر از پهپادهای جت‌موتور برای حملات دوربرد است و این روند در ماه‌های اخیر شدت گرفته است.
🔹
ورود نسخه‌های جت‌موتور به زرادخانه روسیه، معادله دفاع هوایی اوکراین را پیچیده‌تر کرده است. رویترز نیز گزارش داده است که این پهپادها با پرواز در ارتفاع حدود چهار تا هفت کیلومتری و سرعت بالاتر، فشار قابل توجهی بر سامانه‌های دفاع هوایی اوکراین وارد کرده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/465099" target="_blank">📅 21:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465098">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd110347b8.mp4?token=A6y0CQhNHuoamqyNfi44YcUiP5ME_5RGkpfWIEWMYLisyfS3fnnptUyTMRQByQit30b-PMlD8MemUVh4dyt05cwZLo0hCB2jL2fOC9IaXszIPtufPyI-YIBKxSqcOl_Jd5sUwfOQRmNVKL3Xhs_-lpNoV127NAYdQ1ZaXQHtBRKKcZum7CjYvdWDOmap358Mw-NgUSB9spUT4NbWq9vMK9TFMgE1Y_mAmUnn0KmaUE8xrIoCNIThCSUEB4mo8kQQi0A0Y5pwm_FnOoidDhIE1ZMc2fQeRJ3NGcJUMPRO1S21ht4SVdrdDxz7TvafMnzVrSTRAd9t1HrKDOrnSKItBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd110347b8.mp4?token=A6y0CQhNHuoamqyNfi44YcUiP5ME_5RGkpfWIEWMYLisyfS3fnnptUyTMRQByQit30b-PMlD8MemUVh4dyt05cwZLo0hCB2jL2fOC9IaXszIPtufPyI-YIBKxSqcOl_Jd5sUwfOQRmNVKL3Xhs_-lpNoV127NAYdQ1ZaXQHtBRKKcZum7CjYvdWDOmap358Mw-NgUSB9spUT4NbWq9vMK9TFMgE1Y_mAmUnn0KmaUE8xrIoCNIThCSUEB4mo8kQQi0A0Y5pwm_FnOoidDhIE1ZMc2fQeRJ3NGcJUMPRO1S21ht4SVdrdDxz7TvafMnzVrSTRAd9t1HrKDOrnSKItBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعضای دولت روزی چند ساعت در فضای مجازی هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/465098" target="_blank">📅 20:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465097">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93afcd2ffa.mp4?token=Do_U25MxRpOgm9tMVd8dO5yp0NJdK3-oksNhV16J_9CZIW4YAqF9MIm6G9sunibAkckvwi-rHkjuorHG8MZ9rXlghiWIM39s8IjdOmAMAcWji47EbREiDvTihojLxLGqAluWlk1V_R39r5Chn9dH6UAHIygL4fclNw22o29AtaD60omRez7RCmjJnJqqNsqR51o3hIdFIPVe8Z64jeZQXBCYCzLjOvY3QpqxL3aONhwFp31kyvnZhhG0d9A_l5L8B6oyBtW6spq-v8oHdGbsEcJyMT3Gxk4Efu9A8R_dt3GSvbv77zUcNoxPf1urj-nNTbwW8_WyK9hIa9c1iIOUbl3y8fx7PkSWo3NPVC-X8zTtZTVtx-A3KR6PQgYyzndUNsd25UJhFilvR1EyqUk45jXAxzEZy1JJ7UOgNe29cJhNDMdxac7YmDUcA92I6ZkW4fnNx8nWKjOTt3XhoNGmlAoolbdJndVixGIUY0-7rkkk6u8lbdD8gauAivlunkKEWAYUZKjKBz_UYv7bogOv5qa7ZSwMRt0HJ-nVQ6yPqhMW7-XUTTJwksphf1s4VtEjrjfvFczxAHBOSneUTs46SQl-FuCA-pv7nza-_waF-RRMcAjCpoA7OsNrga7MxxGKHtwMQQF0SPtWwJniFsFNxlXFeknS0OVx2E0PQRPSc3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93afcd2ffa.mp4?token=Do_U25MxRpOgm9tMVd8dO5yp0NJdK3-oksNhV16J_9CZIW4YAqF9MIm6G9sunibAkckvwi-rHkjuorHG8MZ9rXlghiWIM39s8IjdOmAMAcWji47EbREiDvTihojLxLGqAluWlk1V_R39r5Chn9dH6UAHIygL4fclNw22o29AtaD60omRez7RCmjJnJqqNsqR51o3hIdFIPVe8Z64jeZQXBCYCzLjOvY3QpqxL3aONhwFp31kyvnZhhG0d9A_l5L8B6oyBtW6spq-v8oHdGbsEcJyMT3Gxk4Efu9A8R_dt3GSvbv77zUcNoxPf1urj-nNTbwW8_WyK9hIa9c1iIOUbl3y8fx7PkSWo3NPVC-X8zTtZTVtx-A3KR6PQgYyzndUNsd25UJhFilvR1EyqUk45jXAxzEZy1JJ7UOgNe29cJhNDMdxac7YmDUcA92I6ZkW4fnNx8nWKjOTt3XhoNGmlAoolbdJndVixGIUY0-7rkkk6u8lbdD8gauAivlunkKEWAYUZKjKBz_UYv7bogOv5qa7ZSwMRt0HJ-nVQ6yPqhMW7-XUTTJwksphf1s4VtEjrjfvFczxAHBOSneUTs46SQl-FuCA-pv7nza-_waF-RRMcAjCpoA7OsNrga7MxxGKHtwMQQF0SPtWwJniFsFNxlXFeknS0OVx2E0PQRPSc3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از خبری که افتخار مردم شد
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/465097" target="_blank">📅 20:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465096">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39deba18cb.mp4?token=Uw6Z5FQBadQlMZOh8yydrGio--zQfEW19NjecUcN3uKRqTbob9l3xQO_p6O-Ff8OMZH-la7IQrjjvxJKoaG03xiY8i4yRKQ6f_zTDjkds_gCwr4orh1cyEmFtoXPat28X0bL1vUZi5UY6f8wBDeOSpsWp3n7SfVUa-Xher5MEpgBiztrvH6jPuMKo4Myr_kK7dbQq7M2xCT0K1aCFy1qsOnhmMFZzBz-r5GkdYwBqVdvO1l1TerbEb0qDKXKQt82qV-wHweRmMhN218s99dFbyG0ZjvTEhXCyHBkNerilvA8roRcEsPZ0c8L7ukm57_3ZfkrOnRJ7sy98WsGBr4zKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39deba18cb.mp4?token=Uw6Z5FQBadQlMZOh8yydrGio--zQfEW19NjecUcN3uKRqTbob9l3xQO_p6O-Ff8OMZH-la7IQrjjvxJKoaG03xiY8i4yRKQ6f_zTDjkds_gCwr4orh1cyEmFtoXPat28X0bL1vUZi5UY6f8wBDeOSpsWp3n7SfVUa-Xher5MEpgBiztrvH6jPuMKo4Myr_kK7dbQq7M2xCT0K1aCFy1qsOnhmMFZzBz-r5GkdYwBqVdvO1l1TerbEb0qDKXKQt82qV-wHweRmMhN218s99dFbyG0ZjvTEhXCyHBkNerilvA8roRcEsPZ0c8L7ukm57_3ZfkrOnRJ7sy98WsGBr4zKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دائم دنبال عیب‌های خودت باش
🎙
امام خمینی(ره)
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/465096" target="_blank">📅 20:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465095">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f50f2464.mp4?token=dP9AxQZeWmU3368yW-3esPP_8t2FM43lUY3C3CY_aeQ0i2gdDn6wcwPCN1ZxMiZDLPXaXH3e0aX_DUpBBWD7SqkB7-KqBtiTc8JCH0zhxBBHKEM4pLWb1CGefvAFTkOgJbRWENqX6Tqv53R_G49Ip2Jn_YJ88N2C4QXMWapp3TgN5fKDoiOuUUPPRBvfddlD66RI8JBKi4wKZIXCetFgtYVA9-z5Ho_9JsMnlUG-ho8VAdAowzJNOnaX6Y-uzJWkAmOGQP25OyfTb4bkcNx39xpotCQhJprcj0A7lpIp3Kbt2FpbSGFO3JM5teFpA91WpuEvqMreclmU32kN8zdmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f50f2464.mp4?token=dP9AxQZeWmU3368yW-3esPP_8t2FM43lUY3C3CY_aeQ0i2gdDn6wcwPCN1ZxMiZDLPXaXH3e0aX_DUpBBWD7SqkB7-KqBtiTc8JCH0zhxBBHKEM4pLWb1CGefvAFTkOgJbRWENqX6Tqv53R_G49Ip2Jn_YJ88N2C4QXMWapp3TgN5fKDoiOuUUPPRBvfddlD66RI8JBKi4wKZIXCetFgtYVA9-z5Ho_9JsMnlUG-ho8VAdAowzJNOnaX6Y-uzJWkAmOGQP25OyfTb4bkcNx39xpotCQhJprcj0A7lpIp3Kbt2FpbSGFO3JM5teFpA91WpuEvqMreclmU32kN8zdmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان‌فدایان در «بهار» همدان به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/465095" target="_blank">📅 20:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465094">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba3591ff8.mp4?token=myp_dz1Jp4zTs8dXu6XO3zPREFoBTKEZROYAg4IYzcETF8OATOghmQ-Fl_kzw_091S7g1sbw-y4z-Ctc0OAN2VMn6OHD-hh8r6zCeLoBJ4oCyE34yaxI0gFBdJTpLlDhOzKj7_AUFqCxzNhO0OEf_fDZivOPQ8k0X-fqDZSrka214Z5e-IajzYftX4vXwSE481WqUze1BXsudFJ7I65XNv-VZrhtsqFhTnunAFqPAR0Kq4QhBSlBhkphpZ6_YG5mqrMdSMl6zXIM8LddzZ4PMj109PxvqRzgPtqIMf5PprbNRoEu4zcPHATJy50DigertSRwRLwOUY5swVCVfTJglQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba3591ff8.mp4?token=myp_dz1Jp4zTs8dXu6XO3zPREFoBTKEZROYAg4IYzcETF8OATOghmQ-Fl_kzw_091S7g1sbw-y4z-Ctc0OAN2VMn6OHD-hh8r6zCeLoBJ4oCyE34yaxI0gFBdJTpLlDhOzKj7_AUFqCxzNhO0OEf_fDZivOPQ8k0X-fqDZSrka214Z5e-IajzYftX4vXwSE481WqUze1BXsudFJ7I65XNv-VZrhtsqFhTnunAFqPAR0Kq4QhBSlBhkphpZ6_YG5mqrMdSMl6zXIM8LddzZ4PMj109PxvqRzgPtqIMf5PprbNRoEu4zcPHATJy50DigertSRwRLwOUY5swVCVfTJglQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه‌نویی: با سبک جدید به مصاف روسیه می‌رویم
⚽️
می‌خواهیم از بازیکنان مختلف در فیفا‌دی‌هایی که تا جام ملت‌ها فرصت داریم استفاده کنیم تا مشخص شود آیا به عیار تیم ما می‌خورند یا خیر.
⚽️
متأسفانه در بازی قبل به‌خاطر شرایطی که نمی‌خواهم بازش کنم، فرصت حتی یک…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/465094" target="_blank">📅 20:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465093">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a929b803f.mp4?token=XRK6g6eNV2udpypNa0NSJaLsYkpLXzxks0kaZBVH3c_sEu1ggnmtnoQFPpjWO7heCeS4fY9s06ZgSs9AYxydQqwBi4_r8Bz2A-rZM0scklgWeM0DqOcUfddagTJcQpKVhUF5SwnNqK8Kf60jUnY27oa5ZliIw_bIF5pdTopcBbPm5Ax4ey2dCk_bVlr_RPez8hmWgxokhEvYiz1sk5vSMVCl4uQ4ZCD4geyGPACPilI_E1ARjqwJrDK_Mk0IZaIXEabP_5aZIREg0t0snO-HC5NgFL4MOjnN0dDiEorR3NxTYDWfFMV9VkjqTDMdBJZhVCg2Hz7yo9uVGPQkPHOjPWhICwf-yakHMnosqg_s8eDInrMs1E8qhy0VgqWOXB1o7O7zFjgCHPKimTJKP7hsObHQAidyoQKBQyfSsDnsddwv7H52R6ednI-EaHVS-7jsqyP0Z7aUCUYAcaNOMKhNDquSF_IxpEfUBMJGY1SmU8sYvFInFTQdPuvBmMT3YNtga0u56IsH0sDMiurG8Vcl0Q3sFuLw8Uy8F8QmBeJyv37mBpxJR-_JZ8Rse0Fzr2yPLm1CeUoetaWHs0n7x67jcWEcGcfUpdOHWsWdErlOiZuLpl3EeXRJbDi74CCnWvy1qKym5vq5a1ErBkggkWF53gd23FP6zqUV7V3IhPq4NEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a929b803f.mp4?token=XRK6g6eNV2udpypNa0NSJaLsYkpLXzxks0kaZBVH3c_sEu1ggnmtnoQFPpjWO7heCeS4fY9s06ZgSs9AYxydQqwBi4_r8Bz2A-rZM0scklgWeM0DqOcUfddagTJcQpKVhUF5SwnNqK8Kf60jUnY27oa5ZliIw_bIF5pdTopcBbPm5Ax4ey2dCk_bVlr_RPez8hmWgxokhEvYiz1sk5vSMVCl4uQ4ZCD4geyGPACPilI_E1ARjqwJrDK_Mk0IZaIXEabP_5aZIREg0t0snO-HC5NgFL4MOjnN0dDiEorR3NxTYDWfFMV9VkjqTDMdBJZhVCg2Hz7yo9uVGPQkPHOjPWhICwf-yakHMnosqg_s8eDInrMs1E8qhy0VgqWOXB1o7O7zFjgCHPKimTJKP7hsObHQAidyoQKBQyfSsDnsddwv7H52R6ednI-EaHVS-7jsqyP0Z7aUCUYAcaNOMKhNDquSF_IxpEfUBMJGY1SmU8sYvFInFTQdPuvBmMT3YNtga0u56IsH0sDMiurG8Vcl0Q3sFuLw8Uy8F8QmBeJyv37mBpxJR-_JZ8Rse0Fzr2yPLm1CeUoetaWHs0n7x67jcWEcGcfUpdOHWsWdErlOiZuLpl3EeXRJbDi74CCnWvy1qKym5vq5a1ErBkggkWF53gd23FP6zqUV7V3IhPq4NEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قانون‌های جدید برای مستأجر و مالک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/465093" target="_blank">📅 20:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465086">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JbBnij4wC4hnq7Vo1z3xHipRWNua4Z3ermvR7_jelA1oaSuAfss_sAMMQo6t2dmZMxlQ7O2lxysW_gOSJjnron-my5tslYrKxKYbiBvQ30v7D-w0_XhqDyAi5wQBFZUFN9QgrRqMZfMbH6xzH5wnMlk_0P-5RgPgmVPm4hhExmKP7jTukvzz0bEByqiaEI52Zsl_TqG7dRhKNU7v8PVWBnAZH1Pj38NinOdE26U7zmsNzqr9lKQuPmDK05Mko_9TnQOBhBVBuIZ9pdIWskugvFiCQEDMeEQakyqq5gvny71rS2q9f-s3YLOMojt7uGB3Qu4KdCggrAUsfezoNXF8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AAjbykief4osA65l3lf87pp-RH5yYVsSf55shKS7ezklYs45munCpVvEobYsg8lu8m_1mmmnqhLKEiYYlBGN05bgvgg2_zeB1cMOsL_S5KSNMVhWBNKTKeWDO7jQTV80oLNCmxHWPHC_qAwLwpW4qnD8KbyVnohprln2Zb-HIeaKsW3I8972nUr9Yel15p0ytID0X8v22CXgvFtjalanCBSNZWqCfqKGHAaxPuZL4foqV3vWhcQ3IK9fsdW32fOljLx6H1DZI_gw5yf_BtYdbSPPmg1bYtM4MyFLwmdG5mClDqZh0fN-gfdobBjdirSlIwFSx9pDB4QTf792W3U5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQZUgSKOO1Enwwt-H2FZh8UkC2gQUlGv8JBVT9Q5N4zI9g49Py6YMlSIwmMme0461BIqG8ocQ1EGsbutBcBg7LjovpG2YvgznAE_nJ1zLPe1cb49WnLTyZXgNYWwFPHu_vrADmlNbdtvaGUgNhiITsdLfj_B1z7agY6wOaSZh9Bh4qzwAu_BdIqtpZgdJALwGtzt7SrnxbEd6ujwcmuf8iNXOKu-L0EWYFPfOyiBHukrGgw-QzkRUJv_q5-YVD6jPafASgnm4kNnpnwm_kC24x7K6EaExz2T3Gy9_LmaE4IDLIO_ZRX6JmogMMEKtvYYEFl32RJwcQjiAzsIuwBMOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdCd2GoYOhGOivih2sEw74G9tANC8bqD19m2mrcTZyzgLVvz387lGhNYegUjBcftn-67PPyMDo7pijrz8aGTfJ3HjtqZous4c1p0POx2IaTECcAIuebu2k_C6rgRjopbGu7pC0Y6v45Pi-7WH4tqHz-hE0pudkGRLMNRDecMkpj5uK1fo3nlvQ6t9kGDG5UApHznLwbgfy22Qdv-aO801ADesyXj6FV_OqXGcqXTXl3vZqLU8lz3HQdP_EWambI9soY95hhc9SrgzWYvmuWeIdoJF5kvqyzKAzQpuvdF95i2Gk1ZCFlKEIGHBDx34grOImJ_6XKXeB9RVtEvGAj_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZcNxQ2BHzZmc_gBYervJZ-yw3K8AiYYrIqhYT_07P-HAoFQzZLkEax__FZNMRrNcviGPPBtvBK150Y-9L15akOScAd99z0c7ftu4TvxbAdE2VEh4IfLULBechsZXyyvxlvND8ARZxv_J4FJSBqiJ1U4k8CE7omH7F54_xarskAqy97H-WVbawDaKsTQT6oiq93AwtLWUHRLbjbWzbvWaRxkz8SnbWiAe-QlNErxyXjwBoA1QO54xtv5CtXalQHXRvIZs3py1LXTGFTHyGPqGUeam37qau4Twp4LHhEawXtMMi7oXfraaZ7xOB2uEAzPPo2VCHG5VmQ862cbgeh40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N46Nhi14yZ9QyFG3m0hiXqXpgVGSfI7yVwKQ6pHn1IbUfoyyOBySS46lYMFV0WRfcLTnSCKnHfCzrW5Yk8bnrDcApbpniVvJ1h_BGOQGSqqZpJJZOpMMuuFEiCyd38l9ONPEdVB5BWw-TJM9O7m_HZZkSD07-WRcLXXi8xHYMEuOgAE_a6RL3VwiaHh6ZONg5S0dbjy_m4r-0ui5E9hgJbCmb79BPiPIbuMLqOsCSgMXqLPv_-v1IjYGYSB26R2MgMMvOjFfNev0e7MjLujzeczmln3vWWJC53y_hw6aD6ggh_oFRiVEvnI14eWFk5S5f7mi9oRqO895OLrrqD9DKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTPy3f0_fxG4Pk55RZ7ki2LripMuGBCu_X7N2auf8SudtCjFc_XvRCyUp-WsEAExp39QZ4xzVNVJLRF-_h1CJIOVT8N7SIQqxgWNq6MTX_zseIQPhT5tVAiD_5DOZlWnJkyBShHUJznzNYRSyFOh5hZUumkZ68zhTUbUpW1VJyN-Na-PdMF9tWHZhzvmYSBQvis38J0ZZICCVOP0wQPYSS8nxgKyPyOpDbhycV9qZb-uQgaTHpFla6N1nZrHB7CpJthEtzDMXqC0Ncq7tP98KHhBEUthRnd-pGb9IkOwjQE5j4OtX-rCKkllAFBquR25RYxm4-WWrCv76kHSmjq3Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقۀ شهید جنگ ۴۰ روزه بر شانۀ مردم یزد
◾️
رزمندۀ بسیجی محمدمهدی رضایی صدرآبادی درپی اصابت ترکش طی حملات دشمن در جنگ تحمیلی سوم دچار جراحت شدید شده و پس از تحمل دوران سخت بیماری و کما به شهادت رسید.
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/465086" target="_blank">📅 20:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465085">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEEch-dgxoRm5XAuMsdwagOfZodQUMa_bcNTTkg1F3N3Oeps-d-VcwB9JFE1dEsigJ0jpexctiZVhXyb1gDqRBvPr9e2GlQwrqGU-fSt-Lj58zOAJ0Bn2G0c2QBY6kdMq9_jDk8DiZs5ByiZyFGSZJ9hrIfOSmlgJI6mT_mDHJX7M0J8BicrSp3v4ZIl18t459y8o1VkR8GsPNlk27wSdmSBjXl-Fh4J5BuIfj9vCdJ--X86lsqcmbQLm4H2C-OSIk-8mV4VWTzDlwz_2ZJGt6skkuxTaaOGG18P1v3IqK72yL0_1BtEPoiab96Zyn4Oh7tuUEla47WawcyUnMBhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درحالِ کاهش ذخایر نفت آمریکاست
🔹
درحالی‌که قیمت نفت در مرز ۱۰۸ دلار معامله می‌شود، وزارت انرژی آمریکا دقایقی پیش اعلام کرد که ۸۰۰ هزار بشکه دیگر ذخایر راهبردی‌اش را روانه بازار کرده و سطح این ذخایر به ۲۸۳.۶ میلیون بشکه رسیده است.
🔹
آمریکا ذخایر راهبردی نفت را برای مقابله با شوک‌های نفتی ایجاد کرده بود، اما پس از بسته‌شدن تنگهٔ هرمز، ترامپ ۲۸ هفته است از این ذخایر برداشت می‌کند تا قیمت نفت را پایین بیاورد.
🔹
با وجود این برداشت‌ها، نه‌تنها ذخایر آمریکا به کمترین سطح ۴۴ سال گذشته رسیده بلکه به کف عملیاتی ۲۵۰ میلیون بشکه نزدیک شده است؛ هم‌زمان قیمت گازوئیل رکورد زده و بنزین به ۴.۴۷ دلار رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/465085" target="_blank">📅 20:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465084">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ ‌
🔴
سفیر عراق در ایران: فرودگاه نجف تا ۲۴ ساعت آینده برای پروازهای ایرانی بازگشایی خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/465084" target="_blank">📅 20:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465083">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb-lQR5chu5fPrLeeYO6oIHp80KBoUgq2jUAOOHKnlta16_-NoI38BwCr-rA0xa_vQ4ICOqtZx0mpapm9yGHVzrmIKJGLwnxnMJ7vDsttZghKaHSiLqn2oYqUfrMNDcfHh9cPV8lIaYEoV7Fo5tFQxW7Krv7IGGq0febs9-QYifozpW1wDHoRoeTKP5O3E7_cm5VQ2cicha6abhgBHfDml9giqdJppnT9Xn3MP8HE3nhjfy2prAasJUVsvXtpOM2bRLGOq_HL-Kx41tUqFeu4P_NTSczcN8-KhKEEcCz7zVxzxHtYXLk2gLPfMHWrfuL6ZS0fO8FT2EMpX3U6FzgKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگزاری جام حذفی به شرط رای مثبت مدیران تیم‌ها
⚽️
در فصل جاری به‌دلیل فشردگی تقویم مسابقات باشگاهی و ملی، زمزمۀ لغو جام حذفی شنیده شده است.
⚽️
مسئولان سازمان لیگ تصمیم گرفته‌اند که از مدیران باشگاه‌های لیگ در خصوص برگزاری جام حذفی «بدون ملی‌پوشان» نظرخواهی کنند.
⚽️
در این میان پرسپولیس گفته حاضر است حتی بدون حضور ملی‌پوشان خود در جام حذفی حاضر شود و سپاهان هم خواستار برگزاری این جام شده.
🔹
اگر اکثریت باشگاه‌ها با برگزاری مسابقات جام حذفی با این شیوه موافق باشند، این جام به احتمال فراوان برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/465083" target="_blank">📅 20:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465082">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56844090bc.mp4?token=OW4gXY4zRZ3DrCxhsVYhfCk_HPC-4NoNgH1TGLqzASKUJwhzeUvC-gRVJmmmxdnnXSsyxf4iMTyjMERcy4C1JJGO5SHLydZZvU-hcIDBM4U_q8JvyaULXrUKEB-46AAPQKxilqBy5OIFPIVN0yy8M1LUUPp8B-lmKBgkoek9MUXCHpbgfVEozlCZZG1omFM_8GnO8hxqWAnH3VJ4pflG59oJXvEPzIWgXpynxHDJV3gsGmfmoVrIAs3WZiupmTe5u-nUBaZzg7PwBk25o7IRIAGwMXTqPOD8ZZrQS-MtsTJgpPnLhGRo5GYKkZKAbcrxUpYyCDCD3hkki9N02dWAHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56844090bc.mp4?token=OW4gXY4zRZ3DrCxhsVYhfCk_HPC-4NoNgH1TGLqzASKUJwhzeUvC-gRVJmmmxdnnXSsyxf4iMTyjMERcy4C1JJGO5SHLydZZvU-hcIDBM4U_q8JvyaULXrUKEB-46AAPQKxilqBy5OIFPIVN0yy8M1LUUPp8B-lmKBgkoek9MUXCHpbgfVEozlCZZG1omFM_8GnO8hxqWAnH3VJ4pflG59oJXvEPzIWgXpynxHDJV3gsGmfmoVrIAs3WZiupmTe5u-nUBaZzg7PwBk25o7IRIAGwMXTqPOD8ZZrQS-MtsTJgpPnLhGRo5GYKkZKAbcrxUpYyCDCD3hkki9N02dWAHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید عهد سربازان نیروهای مسلح سپاه و ارتش با رهبر شهید انقلاب در رواق دارالذکر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/465082" target="_blank">📅 20:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465081">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca84a6939a.mp4?token=vV353Y6-HvtMJXJWNfq2vnea18UPPG7gglineYrHRmS92ttR8zG3e28Pgw8jDL6j8NpJdYN_-a2cWCav3WCGuikQEGlLHnah76pvRga36YvBXa98v1Xh_y7RQNQ5fA2mVW_oCJ-d_TmHfqSLvm8wVGwYxYrUrVjcm_So50_eHL9_p_SJJOeu6MLODPikxrIKDxQRvjdju2Yw3_putsfhW8q54RGKGKJ0tQL1UmJ-oHf4mhI3CF5_EeIlZ-UbuDi_IPbcdGnKrIPbh4wToU7DGy8S-VTMNpV38AM1knQDPi_1w0Jvk3vY7S01zRVOyMkH7PoxuoUAozpV_sM_1irKFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca84a6939a.mp4?token=vV353Y6-HvtMJXJWNfq2vnea18UPPG7gglineYrHRmS92ttR8zG3e28Pgw8jDL6j8NpJdYN_-a2cWCav3WCGuikQEGlLHnah76pvRga36YvBXa98v1Xh_y7RQNQ5fA2mVW_oCJ-d_TmHfqSLvm8wVGwYxYrUrVjcm_So50_eHL9_p_SJJOeu6MLODPikxrIKDxQRvjdju2Yw3_putsfhW8q54RGKGKJ0tQL1UmJ-oHf4mhI3CF5_EeIlZ-UbuDi_IPbcdGnKrIPbh4wToU7DGy8S-VTMNpV38AM1knQDPi_1w0Jvk3vY7S01zRVOyMkH7PoxuoUAozpV_sM_1irKFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تجمع عراقی‌ها مقابل فرودگاه نجف در محکومیت توقف پروازهای ایران
🔹
مردم عراق در پاسخ به فراخوان جنبش نجبای عراق در مخالفت با توقف پروازهای ایران مقابل فرودگاه نجف تجمع کردند. @Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/465081" target="_blank">📅 20:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465080">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3GqPdgAtvt965sOZJqCJCnDATeeRWmWrlQBxInlG-IYT-0YOLl6CKvRvb65WbYj_PF6WddPlDSwm3g02fmDVcd3FKHlSr-MOq_uKJKO7_n_Qy1qqJ4BljhKaa_Odc_7KxBmVAYH2NYQt1BU0VQ_2ABP6bCbExWyoB2OUxPWTLfiU2f0kguf9AmRJJN90yuAqozHMQyFqLgH1yREaO-nQqiOYHQ-IgUAzzWkjZ_TOJELIt_x5PGNkHjNmqZRsUsAdvrJwe58_9c0ldMvlRsaazrA6vn0cqe6UIgQESJu2unQHhGxfa0cRRXtb41ZNBAFoNCKoh8p5_mZaS645P_hgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: از زمان انبیا کسی به بزرگی شهید نصرالله در سرزمین شامات سر بلند نکرده بود
🔹
در این مجال بسیار به‌جاست که به‌مناسبت دومین سالگرد شهادت امیر قهرمان عرب و نماد بزرگ جبههٔ مقاومت، شهید عالی‌قدر جناب سیدحسن نصرالله قدّس‌الله‌نفسه‌الزّکیّه، یادی از…</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/465080" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465079">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVgSJoqrWz_APDJZr00TeP8uM3KHyepdxTM6pItsAR68EIbkc41frKsFEnOu6D9nqVpxlyOY7K3Be3W5Ngo1bqYZtSjM_PdSSMYKnK6jG1Xi-9FOwE8CmLNW7lKwIJlqh_1nr44oGmTSPhnudjccsLWPfeTz7UIHgEJ_Q5e98h_BtsohBuusrgIaA29-JOmMMNpCW_mIcPaPLF5gci23o5QzTHkAmHcCAj496U6keBmSZGbvn8l8dd8XE2hoZRZrt2qiyrzokHRTfmDwyqvvI-e3Spp38_uFyDxM0bmFyqr2SrdX8pt2b6Ri-RYcIehBFcXaCuYUM9eg02D1XI2IFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران باز هم مغلوب گربه سیاهش شد
⚽️
ازبکستان ۳ - ۱ ایران  @Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/465079" target="_blank">📅 20:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465078">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJM-CGAInwtBr9XwD6BXg1McDyjCgTj_3sXrLw7Gal8I2aJmr450J37i2XWLYhfzwKkJRpUikl8Q3QHO42E4tYEL2I0m2HeN3to3jP18VQHTbbsgaaOmGeSAPJAOzg8wTwVseulIigVob6uFss0vlq6IIUuWADJdJ9_vO_HgQcVRMyJJKA8-YSs8mjTgEnqP07bbsrH63CE0j6dhiSLIGoeK_TRFfBNYzAf-Zb1DZa9-OZUQmJUNAQbyxTKudjtCEhWTqEOQ7z8siduoBr58F2RStFv8QXQ30VRm3X8a7hAmdE5HaMEIrEJrChgAcpEcwe5cnHSZkU43ULUlyciwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هند باز هم قربانی آمریکا شد
🔹
رویترز: درحالی‌که سال‌هاست هند از خرید نفت ایران به‌خاطر تحریم‌های آمریکا محروم مانده حالا هم به‌دلیل آتشی که آمریکا در هرمز روشن کرده، نفت ارزان روسیه را از دست داده است.
🔹
دهلی‌نو که ۸۰ درصد انرژی کشورش به واردات وابسته است حالا بازهم باید به‌دنبال منبع جدید نفت باشد و معامله‌گران می‌گویند که به سمت محموله‌های گران‌تر جایگزین رفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/465078" target="_blank">📅 20:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465076">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWLpqq6ZKbBMWCJMM4UW3DQDsh8-YQUOSREsG5oaPq_Lu8_KWOcsdI-Hmzq8M6LZnKoZkW3C7FgZtZJCenYGXbaQuHQuuTW2hzNUDvghZ9rCfZCx_tvYHdAXv3QStKsigptiKMoerUxtrCWIXZJxk2OE7Nmn3fRA760vaTp6-WmceDBp26DK8HXYmHDUHuI5iES65xOjyQ0BAPsPl6XkX5fskswcIAgHwC40e1S9j_9ptU7NJPO4EFP3QPv5OqdxRETIw7PMJpBq1npQoMe-3iCZBfEtmpNH573TZHHTFfQpoQplZ4aHkm_4siekxumD2vyTCCcwnphakZ5xQKs8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fd8c8a9c3.mp4?token=Q5KwrHHSjd_d6_fjGFbXBQGOZf0R64lY0ZKHr_8nqh1DErIqsccOLbo1UIABohhFk0KgGiHNeEdYOBKgHN4u1JaDqQnGYNvayw8GvVX5jxlAt9wU86DLacjFsUsPOJMPXAM2KED4pocyafanhXtmHMTOdpKDe3LEuwpPJ9nGX3D95WL2HUmE_90eo_Es1r44No7SbYYA3u5fjotIk9fsShK7bC-inczFkurdxIvdXD4w9UHjwKwYLzjIHPxzDOr31hEhn5gRMGTVGwaxvr6KdYyq6lzRYJV4ZFZgK-o4b6SGD8-I6ch24DVEb5YrHsR1LQG4qcbLBDK1UXskKm_VKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fd8c8a9c3.mp4?token=Q5KwrHHSjd_d6_fjGFbXBQGOZf0R64lY0ZKHr_8nqh1DErIqsccOLbo1UIABohhFk0KgGiHNeEdYOBKgHN4u1JaDqQnGYNvayw8GvVX5jxlAt9wU86DLacjFsUsPOJMPXAM2KED4pocyafanhXtmHMTOdpKDe3LEuwpPJ9nGX3D95WL2HUmE_90eo_Es1r44No7SbYYA3u5fjotIk9fsShK7bC-inczFkurdxIvdXD4w9UHjwKwYLzjIHPxzDOr31hEhn5gRMGTVGwaxvr6KdYyq6lzRYJV4ZFZgK-o4b6SGD8-I6ch24DVEb5YrHsR1LQG4qcbLBDK1UXskKm_VKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازیکنان ایرلند کفر صهیونیست‌ها  را درآوردند
🔹
در جریان مسابقۀ تیم ملی فوتبال ایرلند و تیم رژیم صهیونیستی، بازیکنان ایرلندی با انجام چند اقدام بازیکنان صهیونیست را تحقیر کردند:
🔹
کاپیتان ایرلند از دست‌دادن با کاپیتان تیم رژیم صهیونیستی خودداری کرد.
🔹
بازیکنان ایرلند به‌یاد مردم غزه با «بازوبندهای مشکی» در مسابقه حاضر شدند.
🔹
بازیکن ایرلند پس‌از گلزنی بازوبند مشکی خود را در دست گرفت و بوسید.
🔹
این دیدار با پیروزی ۳-۰ ایرلند به پایان رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/465076" target="_blank">📅 19:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465075">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5Qj87Fyi8FZudDncPQxbto1tD1AIjm2P2Rui4AQ90TQxOBCpEqA8zsurMX9u9soRSwGZI9iyBJej4UFIQZ1x-TMlTnrSYSQY9Sehi3L4PFhiPVI55T4a-IYK0NQXG2v-MvhmwtPTZ3mE9az29hgJMMI07Zdog8herjWZPcTcPGLTgQwqCYJvkAkCnIb-2pSbUeJjE1TNrt4eHK5ZwJJS8P0f4e_kkRIxOPmQoRNe9FrSFh2KQALpEr3abmgQokhBxutEE2owz760ukQ7nwx2qQGCi1a8FhiVBJGpDZsiMfbUA-zTjdw85oCY87ZXbjOeiqUSD4kPIj1V17llwyXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک
‌
صدایی احزاب اسرائیلی؛ اجازۀ تشکیل کشور فلسطین را نمی‌دهیم
🔹
یدیعوت می‌گوید احزاب صهیونیستی که در انتخابات پارلمانی اسرائیل شرکت می‌کنند، بر سر توسعه ساخت‌وساز و گسترش شهرک‌های اسرائیلی در کرانه باختری اشغالی، هیچ اختلاف نظری ندارند و همگی بر جلوگیری از تشکیل کشور فلسطین اتفاق نظر دارند.
🔹
به گزارش این روزنامه، احزاب اسرائیلی مخالفت خود را با راهکار سیاسی که یک دولت فلسطینی در کنار اسرائیل بتواند به حیات ادامه دهد،اعلام کرده‌اند و در این خصوص، هیچ تفاوتی بین احزاب حامی نتانیاهو و احزاب مخالف او وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/465075" target="_blank">📅 19:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465068">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6U4QBt1yi4lAltt4HohhNSh3_eBR6A8KX4fzf3qxYC-S8dnxC8vR2YvBDwCYpH3vp3oSBcMPUzE8iDbW871hZ3tZubGhVJtD99yS4naEAOJbJhOUb5SACdOAhD1hbW9f95vRLV7fAsQPS-aa7aLOmNEvlRdUGhAqn-Z_f_Q0y0GyrAWoUFkLwyLJdcScoAJS162CaGOa1UI2t6mPB_f4gvcf-VyBpKtTrIsTa23Cw3FfD1iuC4xi8fcxMbE68KpTjnm_XZUArVSNehAoUby3yP99LXCuWljJlXqDCb8JlNlwhr6HvJgPta8tspKaVBKFbtZys3a3EBu6grmxceGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1pbAkv1CZwNo-b7ZR7nxp7g50Uq8HwpRan3DY-sdCOO0UK-NIpaFeHrAaYpxmdIw7xcuvki9W79ucp99kjqYH1CnQJ-XWKDRz-x-4ymoHbM8ULdn0lpSBJwP7ZeihcSNJRjTYdGZo2EVyhEr1YNfqNaAnwmhry-jcfEBqRXocnFSsRoB2l2KgNtezLnbsyLJJinAbyMake38w27g8gwv9dJLMz6xH9TtlwEvI3bAubTaHQ2Ef3DzFiaA9SCVdG8IUoY9ARlsG5hjo-D6X41OixX06uYQpxtHyrDMs9sBgR78s4Avry1GnF1_3m_vNXgUFK-a07OoKyBh9_Sf3meXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDJ78pUsWknv4NU29mCFgzUoLeAEJ0uA-RW7LwY4c3rTu56etNc1bVJ9926eF_C9_mqZi07ogFi0ROX8cSU1ZtB-1Y2w_TSmaNjVGREnyfZmaecrS2bdYFhMqlgP7L2EMFd68HkASLutPP5uhnlyId02hetKc4VlVrPHdt2qMkv4H2aAVnGqKDf9oP4YILW4rosZt3t2e0mqgkW2D5k-_JVOUy-FjxP19A5j1cDJh4inns8iAptcBBfdpjnyaZfj7P6BYLrQQsYLBp03AyhsCkLHzqQSdHNs92k_uFAEe6U54SuLQlUvkUKzXuqNC0Yh6yRRiygXnRIcoVWtoHUkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUfx_Vgi9LbsqVkehCPxVHTOe32CfFaBLnFo6_u4Ek3yxT0oxaKwtlOmL1DXnqdOjaqnRSrcNc80va1GeHaATwPPKS5Busz251yiwXNyqB1hR1J0keF2dMZ_xXpF2sGvFibtwcW0uCaVMGNFOQwrr0-5oL2duwbSI6IKDNHrVpET0mOu82fFHRkJDXUO5cXA2yJhKqZ6AK9ivJ8GOwRM1STqmsfGHnqgETNJLOr-bH0r5nkbOSYKSHocfXYSF0rxO1fefEj209T_uNtIG67gWa5uwalSVMR7ah9QzhmP5B-95usaDjj3OgKOU-TiMYsD4-dC9LLrE7AjxdMM6XU7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdypMKeRzI3djOaC192-7V2dLd54fTJJYyfLCqIQ_-IuKH7A4T-6JPmp31Ry1uv-6t-S53-51rWDxyM2waX_kKoI3HlSrS6EuS8bSu9rpkaVOqxlvz52DWONNu9lyXIKnxDjbnYKOD1PQJIjvxDN3JbZ19a_iTP2-WcUR7UYR5PNcdl4GQ2tskyFJVgFERGy97juikImhksVHj3G4r0mOJELJX0hdQm_BPu2LqFgmS_zvTHDs3R--blUhiFr_aZSGEmYVCNqK5Jkv3aUthr5AxB_edLIOkd1g0RULsLZBp4K6fzr2hiGBusPQ2jhuxh6FykTtoTvOHu9M2l4hlUBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdy64perouQu9_zcx3i0nJ6sDi--RUPA05aJUocs42HVFJYHjyoxH-VheSWFi9L-usCuBisbr2RM0HvFWnRihtIPNjKJS0-32X8WGwurQin2YFv9SrQwZwuiU5b8zIwGglD_kpm8Ma4h10MN3dP22SEMBoURShYGkHNniKRfU-gpExPY7lMouzWsX0ALzLpji2I1siA_coWR318cmuOqGnBpf5bp2uFuXlbP6Z93B08qQivALA-nQqkT6NzwrSYWj1R7vHGNYFgVvWJXhFybA5DrBAKx2Q0nQUrrBg1CThuiG_7htyWbsV074Wq_aPlYC6X8aXgfjwQq8180sY7BGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhMBdSgq-klYfiQa0QcCLNH2JWVG6bT438oFoZQ-l9wYYOb5Gkg62eNUsTvbMTt2N6TIzjT5KMw9EoqSKVyWHYUtFD4-v_9Yot5PgEjOUEGY7e7UQ8fpTkA1lM35mtTbFWKhYCKtV-SvQOlaY2pIWfQg6-iLHrgvV-scdD779Uip1-RmSz-RoLVF3PyZkylU-OeE4q-E1a6V8ejcjXt18XY0hwq81CcI_i7SGCuG3dqlGCzIvrjQYhOITrFi2XfACtwW2GoWu37wCkWgyHwdudDEX2pU79CboOLRZYPkQuGD8Uj-fG9uTAKlAK-BFZQOjH4UnHkc-xCOyPa5iTfupA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اینجا ارگ کریم‌خان نیست
🔹
بنای تاریخی بارده تنها قلعۀ برجامانده از خان‌های ایل چهارلنگ بختیاری است که حدود سال ۱۲۷۸ هجری قمری ساخته شده‌ و از نظر شباهت در نقشه‌کشی و نمای بیرونی نمونه کوچک از ارگ کریم خان در شیراز است.
عکس:
عاطفه گنجی
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/465068" target="_blank">📅 19:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465067">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
تاج: سرمربی جدید تیم امید تا دو روز آینده مشخص می‌شود  @Sportfars</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/465067" target="_blank">📅 19:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465066">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpHbHL5Ysp-GdRov1bI3hpWhXiufz6ozFPwRDxPhkK8kg1O5WOVMOqOf93d1miotUs4c217D9j3amxxF1xeui-JWEYNrug6z_I8b4zIMOULPzAeh4iww65zgJRGVkw9detU5TICg5bjrbei9aaj66kfBm0xyIotzRS011mBVUbpiTOr6l0dduQmOBMShlv8w7Z9LVVrQWOq4r2HDtTh6oRpmB_rOywXvKgpG8ylltQK-W-_LPYhEHu-9Jeq9t0xsLTVOTT5TMccJaguHeDtOSvXHj6K6Gs0kg_TmK6wSaHppeRjzxlx5hMFgsL9XIGZeeUZa0qPBZwvqCDXwn2TgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست: پایگاه‌های نظامی آمریکا دیگر امن نیستند
🔹
روزنامۀ واشنگتن‌پست در گزارشی دربارۀ آسیب‌پذیری پایگاه‌های نظامی آمریکا در برابر حملات ایران استدلال می‌کند که جنگ جاری، یکی از فرض‌های دیرینۀ راهبرد نظامی آمریکا را زیر سؤال برده است: این فرض که پایگاه‌های آمریکا در خارج از کشور، به‌ویژه پایگاه‌های نزدیک به مناطق درگیری، می‌توانند در برابر حملات دشمن امن بمانند.
🔹
واشنگتن‌پست پیش‌تر نیز در بررسی تصاویر ماهواره‌ای گزارش داده بود که حملات ایران از آغاز جنگ در ۲۸ فوریه، دست‌کم به ۲۲۸ سازه یا قطعۀ تجهیزات در پایگاه‌های نظامی آمریکا در خاورمیانه آسیب زده یا آن‌ها را منهدم کرده است؛ از آشیانه هواپیما و پادگان گرفته تا انبار سوخت، هواپیما، رادار، تجهیزات ارتباطی و سامانه‌های پدافند هوایی.
🔹
به‌نوشتۀ این روزنامه، میزان خسارت بسیار بیشتر از آن چیزی بوده که دولت آمریکا به‌طور عمومی اعلام کرده است.
🔹
این روزنامه می‌گوید ارتش آمریکا اکنون باید میان ۲ گزینۀ دشوار یکی را انتخاب کند.
🖼
اما ۲ گزینۀ آمریکا چیست؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/465066" target="_blank">📅 19:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465065">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUU4OTEhwjULYztBdJK9C9rPADp4koAXaPo7qiD83i4E2Vs8i2FM3FG2whsK_lP2sqONUCZXp-YD_Juy36Qfnla9MmAimFN1QT6u_WR7ZQVmtq9WLTSJnJI3nIeeE03Y1Q9aTygMi8PcUeFtj-zKvPDXRFMmTYDGK8PyZlLSCRor8aMv3YNF4Y_k6zfKcxUo7Oq49eWtdgRJetKEH9J8QJ_ulmZ8llqh40XSk4NKpM-Eda-2hGXvAz71-FQAwgGAmyQoDbvhZWURmS-tQQOoG3ItPDonMJXwwRgw3NIBh-ymkL84UsCDsGtPZExIjeL8h98cUytmaEPbQ9eQu4EIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: کاخ سفید گابارد را مجبور به استعفا کرد
🔹
درحالی‌که ترامپ استعفای تولسی گابارد از سمت مدیر اطلاعات ملی آمریکا را به بیماری همسرش مرتبط کرده، خبرگزاری رویترز به نقل از منابعی نوشته کاخ سفید او را مجبور به استعفا کرده است.
🔹
گابارد در سمت مدیر اطلاعات…</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/465065" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465064">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-oatZCWWMcPk63FxcHaBtwbsrMYrh5hr_W_3wVtG_kEem6BncMuu-XSycAiJ0ecCHp3QS3m_Lauyviez0Eb2IQ9WnxfxqB2F2My5_cDw6L3A6D7wu9mZtMT6J3UGx3qrvmETR_cE2CIGZ-f3ROwNRvArl2Kk_KOTKAPLvxhmC4vdCV0TzYtc-QPWBN8ybOAMQ18k-HDcWk-0UWAAXQU3VWdKVHW65hi_n2QemViXdYId3_tA2zSSJxeX4apnseUKkIA-6QwWHzfKz9wIeBPdcswdIRCYRFrSCvK1kriNoyL9YPWyMIJKX7wYXjiNxU3Eioaogajr8WOMFqj1iDaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستادکل نیروهای مسلح: رزمندگان ایران و مقاومت به هرتهدیدی پاسخ ویرانگر می‌دهند
🔹
سرلشکر عبداللهی: دشمن صهیونی-آمریکایی گمان کرد با حذف فیزیکی سید مقاومت، ستون خیمه مقاومت فرو می‌ریزد اما محاسبات دشمن، بار دیگر  به شکست انجامید.
🔹
جبهه مقاومت، نه تنها تضعیف نشده، بلکه به یکپارچگی راهبردی آشکار و پنهان رسیده و راه شهید سید نصرالله در لبنان، فلسطین، یمن و عراق و اقصی نقاط جغرافیای مقاومت و حق طلبی با صلابت ادامه دارد.
🔹
نیرو‌های مسلح ایران، در کنار مجاهدان و رزمندگان مقاومت اسلامی با آمادگی کامل برای پاسخ قاطع و ویرانگر به هر تهدیدی علیه امت اسلامی ایستاده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/465064" target="_blank">📅 19:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465063">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuYeTveG0bWCiXN3ooZzPRInxleHMMH6BPIVvvoRFuY3z1B8RfSJZDnaE4b4-0ZWxHnnH1saCm2Aon2g4wsk0zeeNKI1xiVz6R9xzO4veNs_2Dm6bDcpXXd5rwHPpPRWUbQSXxm_44PuPyCSuh2W2sqrbvcby9VKJK9J9FQhs-cYhpkqqhHMATQRsY8XwyM81McgaAfWdfg7sfRFXsz1Z-k_4HT_7lHNasep8nHzcNbFrgjo_FMMaGHqa_oXjl9zMO2Y1DMIQDGidHkGvc0oNNJ-bLsG8iUuEv2BVJh_R2kU92VVhevU-RQr4F37eBGnOgQ1ELjbice2Qp6F5BpCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عالی‌پور طلایی شد
🔹
علی عالی‌پور با مهار وزنۀ ۲۱۸ کیلوگرم در دوضرب، با ۳۹۸ کیلوگرم در مجموع هشتمین طلای کاروان ایران را به‌دست آورد.
🔹
او ضمن دشت مدال طلا، رکورد یک‌ضرب، دوضرب و مجموع دنیا و بازی‌های آسیایی را به نام خود ثبت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/465063" target="_blank">📅 19:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmfXm9ILbqdaxku4ieQ0TvhB1hBqAd6rRUYn9FHhQQ-R7vpiShFUtWUsexuufZAtfQ-ocWEGQbi7N_GY7V59layO40p8TYXhR3fRPEVz7yqTtteeehDAWok_52hbiT6GJJYkqmt8Qe99JsYXik9Mrg5UO3h70a6k9T-1KDw2_f5i8hOXRgIkHQBCECn8d0R8KPOS_2TcSTa3HrxMGu2nD21iohw70B5RiuhM_qF9mTlwjrkVJoUxXwbepHZplLmyp1Qn2CdfsaGVFr_wodiiTLgMBLT7kOTCm_iD9YRHeOPVgIvsH6UmJNhLfVsq3DO0-4h3AJ-RSARjxHAtGdXelA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی اصلاح‌طلبان در پازل فشار تحریمی ترامپ
🔹
واشنگتن هرگاه اهرم فشار را در دست گرفته، به این امید بوده که بتواند در تهران، به‌ویژه در سطح اجتماعی، بازخورد و اثرگذاری همراستا با سیاست‌های خود مشاهده کند.
🔹
اصلاح‌طلبان هم بخشی از این پازل را در داخل ایران تکمیل…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/465060" target="_blank">📅 19:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۰.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/465059" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۹.pdf</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/465059" target="_blank">📅 18:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab35bdcd98.mp4?token=VEE3eAc6IKrt4APBvpBSH3OZ6d9GuLnTWCfC16VGTBBwnayQIbsWACjQyRSdM1LqzM1x6fgeV1-BgTxAUCDqcb3QsFzU0HVLuDYIszX4VPoCll5cC5yeVY9CDOnoiFFEV160waAnFvfK50m9xPD50eX6nGODBopowLiztwkXzKTFO4nfF4ExRJ8m2S8-kq0jPn3OjmpUs3dk6FlUPqur5_c9weIYNj6gb82s7HS3KciQRCcC9exwSLnML8Sn1W-NlCAArmRUseTpkCWRax_LlTtNNXENFstvxHVCpyQxToG1H1igAsPhl9rVE8NmL3HJimma52JDdwCtTMYZCz_4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab35bdcd98.mp4?token=VEE3eAc6IKrt4APBvpBSH3OZ6d9GuLnTWCfC16VGTBBwnayQIbsWACjQyRSdM1LqzM1x6fgeV1-BgTxAUCDqcb3QsFzU0HVLuDYIszX4VPoCll5cC5yeVY9CDOnoiFFEV160waAnFvfK50m9xPD50eX6nGODBopowLiztwkXzKTFO4nfF4ExRJ8m2S8-kq0jPn3OjmpUs3dk6FlUPqur5_c9weIYNj6gb82s7HS3KciQRCcC9exwSLnML8Sn1W-NlCAArmRUseTpkCWRax_LlTtNNXENFstvxHVCpyQxToG1H1igAsPhl9rVE8NmL3HJimma52JDdwCtTMYZCz_4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیگر چشم صنعت به قطعات خارجی نیست
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/465058" target="_blank">📅 18:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a12cf0201.mp4?token=bb25JC4DCeXSDJWkhg5aQ7Q5JXEIxySo9rtTiR8PSBxyNxqvOsbGC2raenOxKWee6TKUQDcJ_dsjQ5E55T8D0qieqEYXN85AFmrHT628ptavsNnE-rEjQuaZq0XBRjA6daivg_GruuW1BBk5zCqRtQC4wBwFVHrMkAEir-nZY07CKrg02WmBYW-ZRXoGl_PTON4CVCrLhbKo-ygcHGJ8ceOFpR65E0XDKG7oxryUmzcHcZPwjlhsEciBtFKfIrDQde0B0GaeN37UTJBY924wfoq_8_hBitbNzbsSYejqWjMhjo9dXZ5f_VVyPaRkuKLKWqsE-zWtKTsP6-LZnxXy8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a12cf0201.mp4?token=bb25JC4DCeXSDJWkhg5aQ7Q5JXEIxySo9rtTiR8PSBxyNxqvOsbGC2raenOxKWee6TKUQDcJ_dsjQ5E55T8D0qieqEYXN85AFmrHT628ptavsNnE-rEjQuaZq0XBRjA6daivg_GruuW1BBk5zCqRtQC4wBwFVHrMkAEir-nZY07CKrg02WmBYW-ZRXoGl_PTON4CVCrLhbKo-ygcHGJ8ceOFpR65E0XDKG7oxryUmzcHcZPwjlhsEciBtFKfIrDQde0B0GaeN37UTJBY924wfoq_8_hBitbNzbsSYejqWjMhjo9dXZ5f_VVyPaRkuKLKWqsE-zWtKTsP6-LZnxXy8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کالابرگ بیشتر برای ۳ دهک اول؛ مطالبه‌ای که مردم مطرح کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/465057" target="_blank">📅 18:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">دشمن چگونه روی دوقطبی‌های داخلی سرمایه‌گذاری می‌کند؟
🔹
دوقطبی‌سازی زمانی مسئله‌ساز می‌شود که اختلاف‌نظرهای طبیعی سیاسی و اجتماعی را به صف‌بندی‌های «یا این یا آن» تبدیل کند؛ مانند «جنگ یا مذاکره» و «معیشت یا مذاکره». در این حالت، مسائل پیچیده کشور بیش از حد ساده می‌شوند.
🔹
مهدی ترابیان کارشناس مسائل سیاسی معتقد است اگر پدافند انسجام و وحدت جلوی این دوگانه‌ها درست عمل نکند، ضربه می‌خوریم.
🔹
به گفته ترابیان ماندن در این دوگانه‌ها، ماندن در برنامه دشمن است و این دوگانه‌ها آسیب‌هایی است که ایجاد می‌شود تا تصمیم درست نگیریم. ما باید اختیار داشته باشیم در هر لحظه متناسب با وضعیت و شرایط، درست تصمیم بگیریم.»
🔹
جنگ و مذاکره لزوماً دو گزینه کاملاً متضاد نیستند و حل مشکلات معیشتی نیز تنها به یک ابزار وابسته نیست. سیاست خارجی، توان دفاعی، اقتصاد داخلی، تجارت و دیپلماسی می‌توانند همزمان بخشی از مجموعه راه‌حل باشند.
@Farspolitics
link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/465056" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجار و آژیر هشدار در عربستان؛ حملات یمن به جازان و نجران
🔹
براساس گزارش رسانه‌های سعودی، طی ساعات گذشته صدای انفجار در شهرهای ینبع، جازان و نجران شنیده شده است.
🔹
گزارش‌ها می‌گوید صدای انفجار در نجران و جازان پس از شلیک موشک از سمت یمن شنیده شده است. این دو شهر در هفته‌های اخیر نیز هدف حملات یمنی قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/465055" target="_blank">📅 18:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465053">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594628ec59.mp4?token=YkQ8rBCGBs7BLEk5C9uTaWZqN6DdZ3oIShkf5KJjteTxWSW_dgJAI5jDX6TCpHKME34TxVYAoTJ-I4DwhI37RodPj16m3q8idKm73W1pnfZC2-c4PXal8mVMPwaLCoG1AtCmjcxgfra0Z8BFFXmdeQlmT2t3XCp3vmH078mGqivX2eU5Aw1tsRgRoDD0OqSlonkj391wuF17gxOATtLHEEMAiIbuGwuYPv5g14XX02w9mfTU78EaVKjhtMc1lh_8oQ6jpbooB2GXGz9x7YDsOkAMKQy_JWFCtG-5x7Uv0JqXGAudNQc2DkwlvBbJByURBXE1c__IMjWYBNj0ccbTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594628ec59.mp4?token=YkQ8rBCGBs7BLEk5C9uTaWZqN6DdZ3oIShkf5KJjteTxWSW_dgJAI5jDX6TCpHKME34TxVYAoTJ-I4DwhI37RodPj16m3q8idKm73W1pnfZC2-c4PXal8mVMPwaLCoG1AtCmjcxgfra0Z8BFFXmdeQlmT2t3XCp3vmH078mGqivX2eU5Aw1tsRgRoDD0OqSlonkj391wuF17gxOATtLHEEMAiIbuGwuYPv5g14XX02w9mfTU78EaVKjhtMc1lh_8oQ6jpbooB2GXGz9x7YDsOkAMKQy_JWFCtG-5x7Uv0JqXGAudNQc2DkwlvBbJByURBXE1c__IMjWYBNj0ccbTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تجمع عراقی‌ها مقابل فرودگاه نجف در محکومیت توقف پروازهای ایران
🔹
مردم عراق در پاسخ به فراخوان جنبش نجبای عراق در مخالفت با توقف پروازهای ایران مقابل فرودگاه نجف تجمع کردند. @Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/465053" target="_blank">📅 18:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465052">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a637907dd4.mp4?token=bjUiLCkXvdAsDgnuu_fbNTjQgcqhDMGXoy4pLSV7a2XMfT9yrKmiwXggp0inqZyOhUwnalJDPjKZBAcvEQhbcMJ3cqGm8gbDRn8-vd8qo0HW5lg-4rV0ETKDxv2D2AMjm1kuHFNCka7EdmfuPMDEIdEgKinLpcSiFp_Hy3yPi1j3OFGjFKsUCpdRhLBgOiW4aiaUDg2Ae0R6kA1rJlEQauEhz8f-bCWdFZ5feZFBn3fAZmv9KCkF06VmYv0tBPE7XenazxxLX95_1hFMpVK8JeKFwoFeOReMN-dlpR9Me3hvOvClTCWMq6gkllPp4EHWYVBSAviH0echyjMekdzu0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a637907dd4.mp4?token=bjUiLCkXvdAsDgnuu_fbNTjQgcqhDMGXoy4pLSV7a2XMfT9yrKmiwXggp0inqZyOhUwnalJDPjKZBAcvEQhbcMJ3cqGm8gbDRn8-vd8qo0HW5lg-4rV0ETKDxv2D2AMjm1kuHFNCka7EdmfuPMDEIdEgKinLpcSiFp_Hy3yPi1j3OFGjFKsUCpdRhLBgOiW4aiaUDg2Ae0R6kA1rJlEQauEhz8f-bCWdFZ5feZFBn3fAZmv9KCkF06VmYv0tBPE7XenazxxLX95_1hFMpVK8JeKFwoFeOReMN-dlpR9Me3hvOvClTCWMq6gkllPp4EHWYVBSAviH0echyjMekdzu0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاندار تهران: خطوط ۸ تا ۱۱ مترو وارد مرحلۀ اجرا شد
🔹
معتمدیان: ۱۵۰ هزار تاکسی هیبریدی و برقی در حال انتقال به تهران است که این اقدام به کاهش مصرف سوخت، آلودگی هوا و ترافیک کمک می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/465052" target="_blank">📅 18:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465051">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7ZSjkRR5Sj3Ny4RQ0KOV_ExAWpZuvrMGysv2OjesfVNxv8q0Uzf_0SV1IrlR6fi_duQJJyrbXdkKpKFwZlLExb9crJPIHTAT9YAZnQAoI4nzvBHhgczqRSWn5Ez4M2W-heFL0Ox64MxH2jKY4cWrL3Ly8zoTSx3e55BcRCU596SZPH-aaXr4kWeh59UEsRYb2MmoTiy8FVtqBiB0_ddiXFLT1tWIjqalCW9LVvgrMOXks_dOVh2xEMPWIJcY4sAC_OzHbCfVgECToasQFzc_7XE1XUaaZNO6hzkAOQ85g0s2eGJrSnA4CYPc9v3xkBe-q6phvf4LzK7uY8PrB0-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان جنبش نجباء برای تحصن در مقابل فرودگاه نجف
🔹
در ادامه واکنش‌های منفی به تصمیم دولت عراق در توقف پروازها با ایران، رئیس شورای اجرایی جنبش نجباء خواهان برگزاری تحصن گسترده در مقابل فرودگاه بین‌المللی نجف اشرف شد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/465051" target="_blank">📅 17:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465050">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRmx9Sf2PHl-Hv5EdI_AK5K1PpE4TYEJu-2eUpxWuI34O489fh3Syj3vbsg4YZq1F4aOwDKw9MQJTp9C41AF1r4JsULRaNMroJmAoYMBicsZ6kRNZgIPxPyvaUsUsubica6wVZGBaVqErdJUpdHfFSMqijb5JKkLlkR0U3iVu2vVW2TJagkwNeU0eC_TvMUoEK-PRtrLizW0KDtBibBP3XmZhuZ4b5ILRqowqI6v3iEuKcJTBzDQpsKYnxiVqoPWqcjpgT0mlu92JmlqFwi1Jqp4Xhipn1p0F2MTBP5_MJXyragFEdDGtEGuEIDgP_k_vtGlL-x_vFwtXVP0FpvJwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: شهید نصرالله، مقاومت را از یک گروه چریکی، به یک دکترین بازدارنده تبدیل کرد
🔹
شهید نصرالله تنها یک رهبر سیاسی-مذهبی نبود؛ او یک استراتژیست و فرمانده میدانی و جهادی بود که حزب‌الله لبنان را به نقطه‌ای رساند که معادلات امنیت اسرائیل را کاملا تغییر داد.
🔹
سید حسن نصرالله میان میدان و مردم، ایمان و سیاست و آرمان و عمل، پیوندی ناگسستنی برقرار و «میدان» را به ابزاری برای تأمین امنیت پایدار تبدیل کرد.
🔹
دشمن تصور می‌کرد با حذف فرمانده، مقاومت متوقف می‌شود؛ اما غافل بود از اینکه شهید نصرالله، ساختاری را پایه‌ریزی کرده که متکی به فرد نیست و امروز نیز با قدرت، بازدارندگی خود را حفظ کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/465050" target="_blank">📅 17:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465049">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvvlgqVIUgJ_KXkEygaBuctxZtBpqRAzgK-rcNUJEnLXacbbrDgstQ1Y8n6qA-g9-xlfBcBma9Yyxujd-GlcdHPN3Ba4BI3YXThigPXaBFh-oCdoZt4OKWGRvIBh1x5djrXePEgTBatEDFFPzUgXOQucJZ62ofYgz-VNat7So6ZdEOY9wEidu9DC-DirHxcj6snZlNEbbUda723FMBkOT_TYzLBnh6uq2zp6rMNbq3Ea0vPC9SBvc8_dO0CS4DvQ1hNbVJPLA70f-WxLr7tcP0UE8CZNiNez_7HWLot-_bUUQ2v9ROVlksOTDcrJXw8yH4k1WXSxbz1fQxCyilnuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور ویژهٔ فرمانده انتظامی کردستان برای رسیدگی به رفتار مأمور خاطی
🔹
درپی انتشار تصاویری از برخورد غیرحرفه‌ای و نامناسب یکی از کارکنان واحد گشت در سنندج، با دستور فرماندهٔ انتظامی کردستان، بررسی موضوع بلافاصله در دستور کار قرار گرفت.
🔹
مأمور مربوطه به ادارهٔ بازرسی پلیس احضار شده و تحقیقات درباره نحوه برخورد او در حال انجام است.
🔸
در بررسی‌های تکمیلی پلیس همچنین مشخص شده که رانندهٔ خودرو فاقد گواهینامه رانندگی بوده و شرایط او می‌توانسته برای خود و سرنشین خودرو خطرآفرین باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/465049" target="_blank">📅 17:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465048">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYOPOX7-8zbsIvVK2wy9wMCmoHLR_CcyD27ZyYx73CXax-aoZEqom0FWl6YPWCsRn4lJ_DyKhux2o-r4-dfBW_wpD7Itqfwm3XNbuVm1vPHXnGT7C0qwi3QQsVJ9i6kdadCB7IN91UA6la-XesQthu2djm2SGEM4oj3j3Dba0nWUsDwAI7pCbwGAjhDfuuYJKsh0Rq2nqW1Dv6fvXCN8FWGL0ekq3kA9L-UoGVXx6ndor_ixh1lBWwXhtjY9G-RDO5NR4QImhcm-zQcHBlHAu4wL576f_IC0xCwEKJTAXKlSMXyumaT_-zxAuR24yt8g9Hxu9zH4jhKbhB1HbpfhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای مقام اروپایی درباره عملیات‌های خرابکارانه روسیه علیه این قاره
🔹
«کایا کالاس» مسئول سیاست خارجی اتحادیه اروپا امروز مدعی شد که روسیه در حال برنامه‌ریزی اقدامات خرابکارانه بیشتر و حملات علیه دموکراسی در کشورهای اروپایی است.
🔹
کالاس طی نشست خبری بعد از جلسه وزیران دفاع کشورهای عضو اتحادیه اروپا در بروکسل، گفت: «ما شاهد هستیم که روسیه در صدد ایجاد تفرقه و ارعاب جوامع ما با هدف منصرف‌کردنمان از ارائه کمک به اوکراین است».
🔹
وی با بیان اینکه اروپا باید اقدامات بیشتر علیه روسیه را بررسی کند، اظهار داشت: «کشورهای زیادی خارج از اروپا می‌گویند، با روس‌ها صحبت کنید نتیجه‌ای حاصل خواهد شد. اما این مذاکرات نشان می‌دهد که روسیه واقعاً به هیچ وجه به صلح علاقه‌ای ندارد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/465048" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465047">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc78520c8d.mp4?token=O_TVc44p1b641bmA4FHPnobFlBLuVX_Nv9b_3u0dFERX4goX5PD8rCurr3YUDCFirPOA969mAyX8-KQ0JfV9cI7BS6edQq5vqI-0lMKvUpjDMQRvXREeVEXeUJoSvbVuHwIqibHLQ85phAOtXu76FqA2kohWOlmt2NB1H53P7E74yiCnSOZzm7sBIpKJHesEyar0cVdyoimT_tsWB_uxaMId9yD2tXOkxK74GQOA_cgL0JDmbsU1TeeN-qjVdUrlLjIilBlkJTcjS4u1kG1I-KwdfWEgU5K7-vYHHmE3-_g9okGQa5vug54xn4-7l2eq8cXi4IpKSCr_AO5g82ixxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc78520c8d.mp4?token=O_TVc44p1b641bmA4FHPnobFlBLuVX_Nv9b_3u0dFERX4goX5PD8rCurr3YUDCFirPOA969mAyX8-KQ0JfV9cI7BS6edQq5vqI-0lMKvUpjDMQRvXREeVEXeUJoSvbVuHwIqibHLQ85phAOtXu76FqA2kohWOlmt2NB1H53P7E74yiCnSOZzm7sBIpKJHesEyar0cVdyoimT_tsWB_uxaMId9yD2tXOkxK74GQOA_cgL0JDmbsU1TeeN-qjVdUrlLjIilBlkJTcjS4u1kG1I-KwdfWEgU5K7-vYHHmE3-_g9okGQa5vug54xn4-7l2eq8cXi4IpKSCr_AO5g82ixxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاری‌شدن سیلاب در روستا‌های فیروزکوه استان تهران
🔹
درپی بارش شدید باران و صدور هشدار زرد در فیروزکوه، عصر امروز سیلاب در روستا‌های طرود و گدوک این شهرستان جاری شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/465047" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465046">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌همه بازداشت‌شدگان طرح بمب‌گذاری فرفورد، تبعه انگلیس هستند
🔹
پلیس انگلیس اعلام کرد که ۵ مردی که در ارتباط با طرح مشکوک بمب‌گذاری در نزدیکی پایگاه نیروی هوایی سلطنتی فرفورد بازداشت شدند، همگی اهل لندن هستند.
🔸
روز گذشته رسانه‌های انگلیس مدعی شدند پلیس این کشور…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/465046" target="_blank">📅 17:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465045">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKEwPaYEaUP1nJWsu6WBh5BbtsKo-GinH4HsSBiRjfjrtxcpPst_rOPqI2Il-h1x9dzTss6MxB2rq-1_5Y-9CnW_51z3vuKAdr16vLr1fAhy_YNUnOIqsGXxjIp5Rove1WDbN6qUQxD45HXUuuCKqgOKPmxR2yvMdVIWHGcO6FLOoomm6CgWbKm0lor_yL7rQZ7eHD1pKII2rdf5svabrQ0AzyFe1N94gv7YkdvusArKdWv4RXRV2FNO2U3oDx6Me8Gfk3DHY3vZvr97AN2Xw1S_eGEjv0nuTdm87bAcMD2reSbq1L75OCFsVvOT7p_hBT7IDSSjCVFsUmT3KGR7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام اسامی برندگان نخستین روز قرعه كشی جشنواره جایزه محور «دیما»
🔹
نخستین روز قرعه کشی جشنواره جایزه محور «دیما» از بین کاربران فعال و احراز هویت شده این اپلیکیشن برگزار شد و برندگان خوش شانس روز نخست این دوره از قرعه کشی ها که به مدت ۴۵ روز ادامه خواهد داشت، مشخص شدند.
🔹
در روز اول این قرعه کشی ها، یک برنده جایزه ۵۰۰ میلیون ریالی، سه برنده جایزه ۳۰۰ میلیون ریالی، ۵ برنده جایزه ۱۰۰ میلیون ریالی و ۹۱ برنده جایزه ۱۰ میلیون ریالی به قید قرعه انتخاب شدند.
🔹
جشنواره دیما در سه بخش روزانه شامل جوایز نقدی از یک تا ۵۰ میلیون تومانی، هفتگی شامل ۱۲ دستگاه موتورسیکلت و نهایی شامل ۲ جایزه ۵ میلیارد تومانی برگزار می شود.
🔹
در قرعه کشی های هفتگی جشنواره دیما، ۱۲ دستگاه موتور سیکلت (هر هفته ۲ دستگاه موتور سیکلت) به قید قرعه به کاربران این اپلیکیشن تعلق خواهد گرفت.
🔹
در بخش قرعه کشی های روزانه هم، ۴۵۰۰ نفر برنده جایزه خواهند شد که شامل ۴۵ جایزه ۵۰۰ میلیون ریالی، ۱۳۵ جایزه ۳۰۰ میلیون ریالی، ۲۲۵ جایزه ۱۰۰ میلیون ریالی و ۴۰۹۵ جایزه ۱۰ میلیون ریالی است.
🔗
برای مشاهده اسامی برندگان
اینجا
را
کلیک کنید.
@mellatbankiran</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/465045" target="_blank">📅 17:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465044">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I25VfkFpetPlqhQyMAPG83txpBHI08MCzHQydPZ-lwDMBB8o5UqeiBmpq6BIepXyZrHbJtr6aNCvq8Dt4LvSk3xh4q2Ci3v2egeYIX2Fke_NQUf2DH65QmdccxkSf1S4UKD4LHdiBcvGWqi0OKQXkzSog1etpXuyaylk4oprpvILRfTXzPFFZ89QIdZzPK-0kUKJ_VW6cn6W-02MYCv2h2yth2PkryWBYSW9gotDleRQC34iOUld0CJmBWe00iJi_5-Mwhqs-z49DM7FgWqzk4nvKSqrw-2KvwhQnOpsAQOv2aJIRN1K59q2pdmDdOhvU2JicC-VGTRy64fU3rW0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💍
پرداخت بیش از 50 هزار میلیارد ریال وام ازدواج از سوی بانک شهر در نیمه نخست 1405
◀️
بانک شهر در شش‌ماهه نخست سال 1405، با تداوم رویکرد حمایتی خود در حوزه وام های تکلیفی، بیش از 15 هزار فقره وام ازدواج به ارزش 50 هزار میلیارد ریال به متقاضیان پرداخت کرده است؛ رقمی که از رشد 72 درصدی پرداخت، نسبت به مدت مشابه سال گذشته حکایت دارد.
◀️
به گزارش روابط عمومی بانک شهر، حمایت از جوانان، خانواده‌ها و اجرای سیاست‌های اعتباری در حوزه ازدواج، فرزندآوری و تأمین مسکن، طی سال‌های اخیر در زمره محورهای مهم فعالیت این بانک قرار داشته و آمارهای ثبت‌شده در نیمه نخست سال جاری نیز استمرار این رویکرد را نشان می‌دهد.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/465044" target="_blank">📅 17:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465043">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/465043" target="_blank">📅 17:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465042">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnLrNd2-h6sxwksM-jXjmx8pDvepHs_takoR8HXdOuRbneGgmhl82V3T0Zr1eiP-W6nuRhM8Ekz0jBf4XmT4c6rAm_Y9dmJUu7Y3f6QB2-PdotrHEpmdAeeWMzxRuvVfsZ6GAnhORlsRYKLjjGvEE7sIw5yjqytPCDzBe0qH4Z0Dn5aO0ksz0PNWSQLMh9Sl1GeVZvlEG_24xTutL7bO0JLGQhG2Vb7U7NiRicCM5tbdc_D_GlhTinMgobuos4gnicvKCzLEjm40rXubUqivc55yaBlP2BBB8Nuyl3npXR5KsR_erkJrvrxmk_puPigiHjMirHgpIEoATYNU1aCf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات کوچه‌‌بازاری اصلاح‌طلبان برای تحمیل نسخۀ تسلیم
🔹
زمانی‌که ترامپ تازه از برجام خارج شده بود، برخی از چهره‌ها و جریان‌های سیاسی دلایل بسیار ساده‌لوحانه‌ای را برای این عهدشکنی مسلم دولت آمریکا مطرح می‌کردند.
🔹
تیتر «موشک‌پرانی سپاه» در آن دوران، شاه‌بیت…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/465042" target="_blank">📅 17:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465036">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-LclmrIZEI3aEype0ucltH0Q5N-7PCEmvNGp7xhUfdK5NHwNWow5-q9ZGJalN_UoXOpvnMSXjSb1HFLCnyfk9T27j4hVu9QiLIuVYSNf68hMhWm3aNKj6RNFlHyO4S-ILdAuTLwG0OJrEfA10ZY2aLKi8f65Wwd5OzNDx7nrevjjSSJkNvdSvliXAr-XQg8Ly-PTSTgsRbL87VDi_E9g9odLmEeo-PjdKiSHhgpFEGP6Pfk5eKcs6YwkwTRHmmU-GeISLbmVOePlKtftIsBjP63GtAmxZLrWwD8AeBrttmAEWe9k34zsrcHm1AUbcIuT_wPVP5jk5uID36qFOvv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUfPmx0er9bogNKxmGp37gUg3rH-Lv5PEPVua_2EXxsje3De1bxIcVL4ztaikS6HcxsGHtI3dyAfI-iTBu2m3rUZ47DUezexibQqZaiLTaaTFs-SKbCGYcI4fDYn1Zpt-RTPAR9qI3RwTYNLFX2UC7vpG5r18HlSYp_uRjbl-ex66JQcUjx8CQjSNOC0VPZaU4ivDwqBBeU548JiVuL7VVgdqtPLQD1sdlYvPph14_m_lI_-aBz-qaVv0a0Kk-Gpv49ecCi_WdTUnNc1DIdW5U3Mw_49GtGM2oroYiRPiBCOB54jIhadL9NL1r8Bb0RcP7L69gGVKxtcSdaa-Ruf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCjemiEIzBQlQJVVExrQ1V7fC-4SJhXVtVqjUXAVWXKv9hJjrQDUI01b8sb0mE-5TC08g45evDvCm-4TFilfTeEtpDRA255mDA9h8NnYUOjwFLWaDpze7puk1I0SKg1Z9UmwI8U8aneog-NKeLw5rLIIChAhxJfPNOy9jbUWFT96f5MSRKzTYROdVi2ukJWPD2o7JlcNcx3V7ULA3IDAyZpCGWKD5x9vltU-jeiOpUn1gyjHzXsBkydZkfEU5zgeVg9XVc7syLQdrDpfelp9CyNpfuaJLpFinIQm0CnTBTebKRAmfWKsZF7fBgiUFZR4cBYKTF5OElnbKBxEJBRxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsIsDs4hdsT4Erlo4pCE5HSjnmVEMHrpptG2bSwSAV5fi-19uD9ItLrUeRv0YWOK8SwPUkmN_4kkrtwJ4Unx5hoDeeM9ygaP6u-cs6uZAHe070L5qNLcQ6eZEtGhI8ZBTO9bmKYAS5ilYKtNHNME2bc_sDs8OvsKxPMz5AoSEJJo2tkCndPFB0qsrEHp524wdO03vVyNlBGuzeVt7p3zIdIAIECKMMmGGwRGtvU9rY44itQC39nIkBCd-FSaHmeS_Mc4rZaInP4hWOBsIpiDbvjdJu5INT-txptZl8Bjslao_8wgbBOGDAE7orERTH1jBXOKHPgf_3VGdXhVcpkBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYX7lvuGO0otQdroUkc0Z1ML4qKoHeVkDswxOG5xfBirb_YspUrhc8pTq82_Za-rDFnhlvziLNr-cKBwbFVapDezn28au1RQMhOdLMaUdOlv7ZtELnCOt10PZTxqcGSwRIeGJRxAoc1PiAhTfHlIv8BE3d2QHfhPbR6vwMgZlLSpUjYBHpe_3BU1iW1Nrg7SEVbE_AmUhR7lHXU-o9p8MSC949NMidRFNvJRHwZaxbd2NWZ42OCd2i0Tx0nO0PzHEYULyDZTSRiUZgkv2JSdL9i6HdFV1PxPCvwS6e3MfYMw_UPAmI6abTKlUnkOt9lI2CsxFfrXmrD9Hqur37zs-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-LclmrIZEI3aEype0ucltH0Q5N-7PCEmvNGp7xhUfdK5NHwNWow5-q9ZGJalN_UoXOpvnMSXjSb1HFLCnyfk9T27j4hVu9QiLIuVYSNf68hMhWm3aNKj6RNFlHyO4S-ILdAuTLwG0OJrEfA10ZY2aLKi8f65Wwd5OzNDx7nrevjjSSJkNvdSvliXAr-XQg8Ly-PTSTgsRbL87VDi_E9g9odLmEeo-PjdKiSHhgpFEGP6Pfk5eKcs6YwkwTRHmmU-GeISLbmVOePlKtftIsBjP63GtAmxZLrWwD8AeBrttmAEWe9k34zsrcHm1AUbcIuT_wPVP5jk5uID36qFOvv6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار سرلشکر صفوی با خانوادۀ سپهبد شهید رشید
🔹
سرلشکر سیدیحیی رحیم صفوی، دستیار و مشاور عالی فرماندهی معظم کل قوا، و حمیدرضا مقدم‌فر، مشاور فرمانده کل سپاه، به همراه اعضای دفتر حفظ‌و‌نشر آثار رهبر شهید انقلاب با حضور در منزل سردار سپهبد شهید غلامعلی رشید، ضمن ادای احترام به مقام شامخ این شهید والامقام، با خانواده ایشان دیدار و گفت‌وگو کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/465036" target="_blank">📅 16:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465035">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fc1499b84.mp4?token=ny-nYqaGQaHU9eyC8ool5ByjkSN2NuIjuMTFl2EOGnFevNObqZww3f5p9n1YUNex9uNG-F3TILPlP37p7U3N0Obqs6RloK2CdoUFAVjxcANgKqO53m4fKEJGqzkub937_UVlV7FfQCexNpl57mrZSaGt566yQqDTLA_d-X1eTL2asahaO7Sm8nLXA1dVPJTNjMsLvlHYiQ51cVBybiyuLhqjlB64n8ZYyLverpRDkNNt6C36OFUq0SKhoZ3CVRyXlFBTCmQ5OAMxE_h_tOMcKN2-UF34MQ8PxKYL-F5boGHwXIZEnSO8NZEhs87qYlhDtmzozktDHaM1G0b3HVEJ_G5LTtztTr1GHXlYDQEYpLNJCCfp4XxmX_se6MOlXKU7Lgm2zqVER8zTKzgt1AV4VirVLNsNmXt6uUF3IbZ_lMfTsBEafNo0CC-lqB387SiMwSLJvo2x4TtjPXTBrjU2UC3g5ke95AIEZh9JWLVfBw_P3rlOjTY3fNbhGZ1rTPEjfhp434gAg5YUi3-RaHBVOziEZzwdh9Pq6KN0PmzT9JAltJlh4Xr6dZS-jp9gArYyO71gH8kGWIsT5kDRMiacfU_1oPxbi_tgwMeJjidQZDF9ZN_DNxjD8b7w5T7P8FFXePAdw4ocVFpEKj_C98R7qrxLa9wjAgtVikeJpeqeHzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fc1499b84.mp4?token=ny-nYqaGQaHU9eyC8ool5ByjkSN2NuIjuMTFl2EOGnFevNObqZww3f5p9n1YUNex9uNG-F3TILPlP37p7U3N0Obqs6RloK2CdoUFAVjxcANgKqO53m4fKEJGqzkub937_UVlV7FfQCexNpl57mrZSaGt566yQqDTLA_d-X1eTL2asahaO7Sm8nLXA1dVPJTNjMsLvlHYiQ51cVBybiyuLhqjlB64n8ZYyLverpRDkNNt6C36OFUq0SKhoZ3CVRyXlFBTCmQ5OAMxE_h_tOMcKN2-UF34MQ8PxKYL-F5boGHwXIZEnSO8NZEhs87qYlhDtmzozktDHaM1G0b3HVEJ_G5LTtztTr1GHXlYDQEYpLNJCCfp4XxmX_se6MOlXKU7Lgm2zqVER8zTKzgt1AV4VirVLNsNmXt6uUF3IbZ_lMfTsBEafNo0CC-lqB387SiMwSLJvo2x4TtjPXTBrjU2UC3g5ke95AIEZh9JWLVfBw_P3rlOjTY3fNbhGZ1rTPEjfhp434gAg5YUi3-RaHBVOziEZzwdh9Pq6KN0PmzT9JAltJlh4Xr6dZS-jp9gArYyO71gH8kGWIsT5kDRMiacfU_1oPxbi_tgwMeJjidQZDF9ZN_DNxjD8b7w5T7P8FFXePAdw4ocVFpEKj_C98R7qrxLa9wjAgtVikeJpeqeHzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
من هم می‌خواهم پاسدار شوم
🔹
آرزوی فرزند شهید جنگ ۱۲ روزه در نخستین روز بازگشایی مدارس
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/465035" target="_blank">📅 16:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz5SmoNtXKlhEAYom0FVkWPUD40JEcI-L_1dq0wgMkSUyHpHzUrp2iMlyZ5g4aTO0ayNwxaR4nLDV-G5ZcJh725KDF3ZGBAL34hUfVDnEV0Ux17nJPBSbTYNnY2hlmKssw0zcjrPFhA5OL-zeAMxMjbVUIwtwx2hXx7SX3FD2ZRBjR3Z-Np0JS68OvUjruBrB5HV_13v8sX0FvoYVD5D6_1J4Hi33iZ1UM1slix8a0qxLUrDI0TstI_9mZCHsW9mwKdxahqPkzKP2SlMo7IAM6jNtCpvqngZAuAHhWoMi788SgOUCwpuMEd5YVs9rY-gTfPE32X_jLsTX4wc35latQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتهام‌زنی علیه ایران پس‌از حادثه در محل استقرار بمب‌افکن‌های آمریکایی
🔹
رسانه‌های انگلیسی مدعی شدند که پلیس انگلیس در حال بررسی ارتباط ادعایی ایران با یک طرح مشکوک به بمب‌گذاری در پایگاهی است که هواپیماهای بمب‌افکن آمریکایی در آن مستقر هستند.
🔹
رسانه‌های انگلیسی…</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/465034" target="_blank">📅 16:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465033">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTAp4CL_9ybECp9Uqd3471Lt6IViPJ7vKQWx9eJ9vZlsnBCgqlphiQ7CtPeALhA54CwRdJNPz38G6JAUbdIZqSY32s01mYtDz7MdTk10ddDgKYUsal2xC8eyBdHBRcKzMCIGeTjEYOYqeodEy9586VHPvsLt-6g2P1sDERf8ZUebnuWgL5DytWZyFjQ105MC4f93OUbQbikhQQ3iKM8Ma2b-vN89SLOT6ap8PxhSmme3dYLv4J2t0OT6WePJnB-uYmVFQgC1iT9AYI0OXjoKFccDPwSRj-WR_gXSgtDX4gnW7-2YL6LEp7qjKLQ0MSCI6-bno7N528pWoW7uvkzk0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دارایی راهبردی هرمز، نفت نیست
🔹
تنگۀ هرمز فقط مسیر عبور نفت و انرژی نیست؛ کابل‌های زیردریایی ارتباطی و انتقال داده نیز از این محدوده عبور و بخشی از ارتباطات دیجیتال منطقه و جهان را برقرار می‌کنند.
🔹
تجربه کشورهایی مانند مصر، ترکیه، اندونزی و سنگاپور نشان می‌دهد کشورهای ساحلی می‌توانند از این زیرساخت، علاوه بر اهمیت ارتباطی، درآمد، فناوری و ظرفیت‌های حاکمیتی ایجاد کنند.
🔹
در ترکیه، درآمد حاصل از کابل‌های عبوری از تنگه‌های بسفر و داردانل حدود ۵۰ میلیون دلار در سال برآورد شده است.
🔹
در سنگاپور نیز تعامل با صاحبان کابل‌ها صرفاً مالی نیست و انتقال فناوری و همکاری فناورانه مورد توجه قرار گرفته است.
🖼
اما کشورهای دیگر چگونه از موقعیت جغرافیایی خود در اقتصاد داده درآمد کسب می‌کنند؟
🔗
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/465033" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465032">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35f1bf6a8b.mp4?token=Mq3Zb7asQIkawqcpxjRhNI9sBwlYAY-g_7y4AEDz1DWPQcNR3H7a0wW-Vhxj53OswQtDu39TGA0lfdGhCFw4r9jA22q7tBdGF05hpI6P85CUQa9gnVj6y6hzJhtJusG8dq0z3z2MGPEt8dEXIo51FvhvvjuVkPNcgTsOLWBtty8piwMdfycaY3rDTmMSj55LYCRvF1YVhpCwK3bdIGf1NQBtrPdVDMmvbcS-yVaoPvsR4QqflBBhNBixlYCqCrtIZGPBiyCXXzQIpN5SPUZrZWTE0FeL5BocPzDqUi-VSY6a_m5ju0-Pg3gADZanp98kX7BUDSNKeMtTx7qbo_Tn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35f1bf6a8b.mp4?token=Mq3Zb7asQIkawqcpxjRhNI9sBwlYAY-g_7y4AEDz1DWPQcNR3H7a0wW-Vhxj53OswQtDu39TGA0lfdGhCFw4r9jA22q7tBdGF05hpI6P85CUQa9gnVj6y6hzJhtJusG8dq0z3z2MGPEt8dEXIo51FvhvvjuVkPNcgTsOLWBtty8piwMdfycaY3rDTmMSj55LYCRvF1YVhpCwK3bdIGf1NQBtrPdVDMmvbcS-yVaoPvsR4QqflBBhNBixlYCqCrtIZGPBiyCXXzQIpN5SPUZrZWTE0FeL5BocPzDqUi-VSY6a_m5ju0-Pg3gADZanp98kX7BUDSNKeMtTx7qbo_Tn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوشاد حریف نفر اول دنیا نشد
🔹
نوشاد عالمیان در نیمه‌نهایی تنیس روی میز بازی‌های آسیایی ناگویا مقابل وانگ چوکین نفر اول رنکینگ جهانی از چین قرار گرفت و ۴ بر ۱ بازی را واگذار کرد و به مدال برنز بسنده کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/465032" target="_blank">📅 16:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465030">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌ ۴ دلیلی که عراق از تعلیق پروازهای ایران متضرر می‌شود
🔹
در پی فشارهای ناشی از تحریم‌های جدید آمریکا علیه صنعت هوانوردی ایران، پروازهای میان ایران و عراق تعلیق شده. دولت عراق درحال مذاکره با آمریکا برای دریافت معافیت و بازگشایی بخشی از مسیرهاست.
🔹
مهم‌ترین…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/465030" target="_blank">📅 16:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465028">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn2C35YGAhx9UQIeJU_YNGLveJyg9-YF-x0umy4lzmQgwD4csboyF3_LYuO7xBes3aOyn8IYbN18nB34udYB16Gv-gin4h9s2D2hcTpFIL18uZwTe_VhLQzCOdj9V5E-0qX-H6WdujjQ5dQ3s5aG9eUnbN0SF6Yhv-zQ_MA030aktYPqJDgZIiofWuOi78UzBF_sc2yoaRKp1LwJ7_ZDIj4VxbUZPsg5B8Ul7dmZfs6iHdlxlJjkcmr5LXbhB0ID2R-5kZrfsh8dk61t8zEQpWkc-x9eHdWgRMFP2fV3yXPkav_pY80VM7R3wA0ypjJ_7fTQvuyDm4n_4cVjAyEgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم صهیونیستی خبرنگار پرس ‌تی‎وی را ربود
🔹
پرس ‌تی‌وی: نیروهای نظامی رژیم صهیونیستی خبرنگار نقا حامد را در یک ایست بازرسی نزدیک به بیت‌لحم در قدس اشغالی ربودند. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465028" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
