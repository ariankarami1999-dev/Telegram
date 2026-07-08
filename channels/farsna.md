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
<img src="https://cdn4.telesco.pe/file/BmCTUcrabdTrpcjKLd0_GrR-Y2ZaWa7NbIXqmXOKND7PTUYW5VVZj_w2fOkGmzFf3v9x78k4QFLdk6xQUf_jUcG0xPqqrH3eHFGhnQCvlR3L2k21QxCQ6rca5-9xBrx-EGMa-GE6uIirPwBGu39ieFmn0PLupRSM7pbxNU3AMlcaJYjF4jfUUzni-lukD5w4HRS0gl-LzRGPMJaJzg1QrknzCgjLkI2oERLxGQphOXp8rYOTbnaiPNKqrhfCdNTdByxP9SvFzj0SGKcj4dOxRWJ4zVlq8L5IkCjSERi0NA25avgrrnqyBA-jNH9c5xvsAXR8lfIIdQfF-wc3tUIvdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 15:30:20</div>
<hr>

<div class="tg-post" id="msg-448310">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc79e99234.mp4?token=Zz4sEkOrVIMplMp5VwnC41UVAt0C2YdFMwuiHRXuduRDyvy-rvktJ1--RDpYxflFomXRmA3JrhgAdTQh-moJpAicJWO4QyJBfiunsMn6gRAEWZj7n4nn_qb2YcfXtB8Hby_sYq1MBmnMBCYmkY87hlt3l5upyZZ0d7zT2eGu9T9XDK9zjXVmxnL0auYIttZtRkJKFtXpvGgKgC9Ne9-5CtLCkCYuft6PrJuVGZ-qBy2_0l7YnUAXUlF-DrWOU3s5E05VcZAmoCQx7zHupIO34zkaXccGCCsg98WKp7ZRBR2ytpZ55jqAptqa7bFrqkAQ00kPxggHGJ-Nq_AfsnmEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc79e99234.mp4?token=Zz4sEkOrVIMplMp5VwnC41UVAt0C2YdFMwuiHRXuduRDyvy-rvktJ1--RDpYxflFomXRmA3JrhgAdTQh-moJpAicJWO4QyJBfiunsMn6gRAEWZj7n4nn_qb2YcfXtB8Hby_sYq1MBmnMBCYmkY87hlt3l5upyZZ0d7zT2eGu9T9XDK9zjXVmxnL0auYIttZtRkJKFtXpvGgKgC9Ne9-5CtLCkCYuft6PrJuVGZ-qBy2_0l7YnUAXUlF-DrWOU3s5E05VcZAmoCQx7zHupIO34zkaXccGCCsg98WKp7ZRBR2ytpZ55jqAptqa7bFrqkAQ00kPxggHGJ-Nq_AfsnmEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تابوتِ پدر می‌رود از دستِ یتیمان؛ تا در بغلِ شاهِ نجف، سر شود هجران...
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/448310" target="_blank">📅 15:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448309">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad06aa37c.mp4?token=KvBhKXBru2mrYuviDA_DDb7FzC82-emdJw20W4HKuvKnzsrrdSCMLbSRBFumzNkSxLKa7DI2fIzFai7nkCMSZbJD5o-XzyplupExC5XwGQXvcK1XLIVFjnrzQxvbF9BSNBCohbqpQLeUsi_33dQVrJSraf-0ngFbD1BsHd3fApOx16maJs9e-xV_4kE9i0VEFRD9nygoUtrPrvmaLGYEDrXchy-8Byo0X64-y5ozsosZO8X6OGxzxqrNwBeUSdgrwcEnMaoTAj5h9OCwV0xdYF6qrcXpipmFB2GvLcmM7Krh7ZMHvFoiazMa64NIFYlgFLwKxebhHCF5XdHIOxZL2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad06aa37c.mp4?token=KvBhKXBru2mrYuviDA_DDb7FzC82-emdJw20W4HKuvKnzsrrdSCMLbSRBFumzNkSxLKa7DI2fIzFai7nkCMSZbJD5o-XzyplupExC5XwGQXvcK1XLIVFjnrzQxvbF9BSNBCohbqpQLeUsi_33dQVrJSraf-0ngFbD1BsHd3fApOx16maJs9e-xV_4kE9i0VEFRD9nygoUtrPrvmaLGYEDrXchy-8Byo0X64-y5ozsosZO8X6OGxzxqrNwBeUSdgrwcEnMaoTAj5h9OCwV0xdYF6qrcXpipmFB2GvLcmM7Krh7ZMHvFoiazMa64NIFYlgFLwKxebhHCF5XdHIOxZL2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات ناجوانمردانهٔ آمریکا به حسینیهٔ امام خمینی(ره)
🔹
روایتی از سرگذشت ۳۷ ساله‌ی حسینیه‌ی امام خمینی رحمه‌الله در دوران رهبری حضرت آیت‌الله العظمی شهید خامنه‌ای رضوان‌الله علیه، به همراه تصاویری از حملات ناجوانمردانه آمریکا به حسینیه امام خمینی(ره)…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/448309" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448308">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
تصاویر حملات سحرگاه امروز نیروهای دریایی و هوافضای سپاه در پاسخ به تجاوز و عهدشکنی ارتش تروریستی آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/448308" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448307">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae82bf5111.mp4?token=tDSDzPopaXZCpVdBrJKZLKaHGYFQwspVJ9neZOrH9N_AkFMdVJW9NCOoHDbz_FH_1tgjLVKU9sgTC0K93ED3JKo8B6gOfSzefp1HdeI6bXZSYc-LSf8RH0fbXRx5ArNgXQiBG1HC8CVBlFfO5bBCawoi10LHtm8ciJyZw_Z3Vpdf0ZyA2fjVsu4QGw3E_BAitKuiGP0fSBBJAeJY2sOTHY1rVrRdO_BFiH8xSY4S4lfc1YcJ5oLTi1Ad9OGJ9wqpKX4S-Z6uKxGZ3iIMIGdsdcY5ILHTu6JNjxb5jdrP5t7GVLi_S7gjSZr1eotzz8ZCyaF8Wi2a7q_VkBMoKW315A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae82bf5111.mp4?token=tDSDzPopaXZCpVdBrJKZLKaHGYFQwspVJ9neZOrH9N_AkFMdVJW9NCOoHDbz_FH_1tgjLVKU9sgTC0K93ED3JKo8B6gOfSzefp1HdeI6bXZSYc-LSf8RH0fbXRx5ArNgXQiBG1HC8CVBlFfO5bBCawoi10LHtm8ciJyZw_Z3Vpdf0ZyA2fjVsu4QGw3E_BAitKuiGP0fSBBJAeJY2sOTHY1rVrRdO_BFiH8xSY4S4lfc1YcJ5oLTi1Ad9OGJ9wqpKX4S-Z6uKxGZ3iIMIGdsdcY5ILHTu6JNjxb5jdrP5t7GVLi_S7gjSZr1eotzz8ZCyaF8Wi2a7q_VkBMoKW315A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر شهید امت تا ساعاتی دیگر وارد کربلا می‌شود
🔹
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر رهبر شهید در کربلا از خیابان ابومهدی المهندس تا حرم امام حسین (ع) تشییع می‌شود.
🔹
پیکر مطهر آقای شهید از اولین ساعات فردا در مشهد تشییع و به خاک سپرده می‌شود.…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/448307" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448306">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1A6-jh32xZzERt9P1x_q2HYXkRrorS3wobAshJd1zJ9SiCIUENsOcF6ItrHYDOYaxcZDLXA3PeZhyGp3X_F1p-mJVzEGKRVXNN35c4hZcXNBVyuOG4tGtk47sodHwWWBIQeisTSxjbHjW2tQEPSd7447EasegRUdkshuKoW7SEcTJXWxgyjOC-DrkC0LqMN6w2tNQBju68Ir4mvsNWCxFPtjRNql_XxHALOqSLSRDSc91Dos6c-g6fpEK0AQ3it53ExbYyTMUYgCUVwSxPav0yOYqXsOHdgaxpKs2QTUyCZQIFFFs1owEVxPYXuKPsOLikVlawRC8jSxWcU6rMe4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید بیش از 563 هزار تن فولاد در چادرملو تا پایان خرداد ماه/ رشد 18 درصدی فروش
بررسی آمارهای منتشره سامانه کدال حاکی از تولید 563 هزار و 27 تن فولاد در شرکت چادرملو از ابتدای سال مالی (اول دی‌ماه 1404) تا پایان خرداد ماه 1405 است.
بررسی آمارهای سامانه کدال حاکی است از ابتدای سال مالی این شرکت تا پایان خرداد ماه 1405 در مجموع 4 میلیون و 368 هزار و 576 تن کنسانتره آهن (خشک)، 668 هزار و 436 تن آهن اسفنجی و یک میلیون و 747 هزار و 812 تن گندله در چادرملو تولید شد.
این گزارش می‌افزاید: مجموع فروش چادرملو در این مدت 505 هزار و 187 میلیارد و 283 میلیون ریال بود که در همسنجی با رشد 18 درصدی نشان می دهد.
5524 میلیارد و 838 میلیون ریال از فروش این شرکت از محل صادرات بوده است.
سال مالی این شرکت منتهی به 30 آذر ماه 1405 است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/448306" target="_blank">📅 15:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448305">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBM7EWXe7waE3JiDdc3YE5f0IdrkrIq-3wdXXpJIj_3KoMrB_FJU30nVj0x659-a26YkJUxzky5a-B6Xe2K8dnG0r-My7GTTXPMkv9zOAleij9dYIxVVp2dOmE5cv6AJlsJax1fLwfzCH5hGrfviQ17PBsHpDz6JpbKPEM4rXammXqCEwqtBLZW8juFAq08NqbpZms1e7FVlNAiVCJqUp8kYoWSarZf--_Ck7JWN5zUw32V8ENgHyn6cyokkjerZkzgi2H2NhQx5h9l0zwfPkI3SCgEhK0pRxwjPFJ5me3RFYL-5MFjtkld-fjI_TyLyDCpnD9AvctjwN59x6nvqFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/448305" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448304">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/448304" target="_blank">📅 15:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448303">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
تصاویری از حملات ناجوانمردانهٔ آمریکا به حسینیهٔ امام خمینی(ره)
🔹
روایتی از سرگذشت ۳۷ ساله‌ی حسینیه‌ی امام خمینی رحمه‌الله در دوران رهبری حضرت آیت‌الله العظمی شهید خامنه‌ای رضوان‌الله علیه، به همراه تصاویری از حملات ناجوانمردانه آمریکا به حسینیه امام خمینی(ره) که برای نخستین بار و همزمان با سفر رهبر شهید انقلاب به کربلای حسینی منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/448303" target="_blank">📅 15:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448302">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e6f7d8e2.mp4?token=bP9PBACEMtiwP77wFKJ5hZcRZSiPf6wq3EElbrWKNhUszHqBGiNYxXughEYC5AkTTrK_kQrgF3KOMdpcYEnJrWGpI2IDTBPNhg4hRzPhR8JHXx7L2LolKneReTXCjy8vqu5KiGXbeqNl9wQrECnJnFVOGfU2Cided7eky0vZ3NmNs4FShBH7EJul9LK0A5H2V7AF325xMWozG6gv2i9fpJwUKN7wUr8XgiEjfTeBXv9026vr4iI8iDNzYedqxDQJBNFq25M0VQouckzA8p-nRuADczy7iObHATOXxw2lfUETymwIr40YQVqzgeHFkfBJ7PynJAXRVK73DnjMoJCsuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e6f7d8e2.mp4?token=bP9PBACEMtiwP77wFKJ5hZcRZSiPf6wq3EElbrWKNhUszHqBGiNYxXughEYC5AkTTrK_kQrgF3KOMdpcYEnJrWGpI2IDTBPNhg4hRzPhR8JHXx7L2LolKneReTXCjy8vqu5KiGXbeqNl9wQrECnJnFVOGfU2Cided7eky0vZ3NmNs4FShBH7EJul9LK0A5H2V7AF325xMWozG6gv2i9fpJwUKN7wUr8XgiEjfTeBXv9026vr4iI8iDNzYedqxDQJBNFq25M0VQouckzA8p-nRuADczy7iObHATOXxw2lfUETymwIr40YQVqzgeHFkfBJ7PynJAXRVK73DnjMoJCsuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا ایران باید پایان رسمی تفاهم را اعلام کند؟
🔹
از لحظه اعلام آتش‌بس تا امضای تفاهم اولیه و مذاکراتِ پس از آن، مقامات ایرانی در سطوح مختلف بر یک نکته اساسی تأکید داشتند: به آمریکا بی‌اعتماد هستیم.
🔹
پس از امضای تفاهم تاکنون، آمریکا بارها و به روش‌های مختلف،…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/448302" target="_blank">📅 15:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448301">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b4b4ed9f.mp4?token=JoCjg95rPh1D6gRiFe-h0h52IoV_ZqnZvwDuNVmWjoUPbgN2Y34qjYohCjSEoTAqUx52KZw99vJSjEcAJ2dn_QxuSMtNqxx9JC7ryhtYxl5N7mBSJl0fit0lU7n2rVet7eFMATqadS6RojUg1UrcTkJDalIX4hPTxiSrFtZcpmvx1FS7Rund6CrD9iBEsV6sMgSzDkwjGIRniF0gkFieNYTfmvmsrGAVxmozs1eKKWZ9V6IqiFxMiZ0F2NJiJ15d3okOWPJGR0T173aUAekZkNH0Alw_E6_iahYbgSZo0FULp26IG6icK760l6lGFSiScJTroodGl0qOAwUGbAV0spy0wPB9X77o1ItiJPqPBQgdaEwTlQ00IU4_K1eJwOSTVglSlDYQszh3NStLs41xN-Dm1CpxlJwvUyoUhf3fQHMSseDw8q9gOoTKDsKkFToPT31wm7g8vioVvwMHtPeFbth2-L1J9g8j0VGGjBPpR1wif0xTzES4BlpiEPJW3j4Z5uYjTLALtCX1YYNq67J2K5NoCDQE4EcQXACjEGpvmfHXAlqdkOlwtukbwx-aNX7F7TsBZb8eHBErf9RFnmN06DmLjl3OsNog1eIdHIipGpOt7lfcLkaLeF2IxWkAR4hS-VR5JrFM6Yy6FAcJHk1nbp7WUkuKmvntcbiE-ySSQ3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b4b4ed9f.mp4?token=JoCjg95rPh1D6gRiFe-h0h52IoV_ZqnZvwDuNVmWjoUPbgN2Y34qjYohCjSEoTAqUx52KZw99vJSjEcAJ2dn_QxuSMtNqxx9JC7ryhtYxl5N7mBSJl0fit0lU7n2rVet7eFMATqadS6RojUg1UrcTkJDalIX4hPTxiSrFtZcpmvx1FS7Rund6CrD9iBEsV6sMgSzDkwjGIRniF0gkFieNYTfmvmsrGAVxmozs1eKKWZ9V6IqiFxMiZ0F2NJiJ15d3okOWPJGR0T173aUAekZkNH0Alw_E6_iahYbgSZo0FULp26IG6icK760l6lGFSiScJTroodGl0qOAwUGbAV0spy0wPB9X77o1ItiJPqPBQgdaEwTlQ00IU4_K1eJwOSTVglSlDYQszh3NStLs41xN-Dm1CpxlJwvUyoUhf3fQHMSseDw8q9gOoTKDsKkFToPT31wm7g8vioVvwMHtPeFbth2-L1J9g8j0VGGjBPpR1wif0xTzES4BlpiEPJW3j4Z5uYjTLALtCX1YYNq67J2K5NoCDQE4EcQXACjEGpvmfHXAlqdkOlwtukbwx-aNX7F7TsBZb8eHBErf9RFnmN06DmLjl3OsNog1eIdHIipGpOt7lfcLkaLeF2IxWkAR4hS-VR5JrFM6Yy6FAcJHk1nbp7WUkuKmvntcbiE-ySSQ3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر آقای شهید ایران میان خیل عاشقان در حرم امیرالمومنین(ع)
🔹
پیکر رهبر شهید مستضعفان جهان، با عبور از رواق حضرت زهرا(س) در حرم حضرت امیرالمؤمنین(ع)، به‌سمت کربلای معلی رهسپار شد.
🔸
رهبر شهید انقلاب، آخرین‌بار در ۱۸ سالگی، یعنی در سال ۱۳۳۶ (۶۹ سال پیش)،…</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/448301" target="_blank">📅 15:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448300">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXuILknt6LwWJEpHbIQp4peN4NQ2QRovACDNIdwsyZs9_QWlryFhmUM1fQ0iKr33IUnjy0qi6YskAbZ-McTF9WkwmM9ixc6_niTnD4m4rDtCIPzKYyPMtDWPZ7DNr4H5G6LMt8U_n1KKAKLtHO8wcbJv0UbKUygK8da5rPejcy7PYLPnJLTLSL66pV8TqdSJbAs-R1IU2qGM-1orKi_wVEqbVN4KtcFy0p0LbVN7TxnLYW5s1Im_4E1iRxNCkLgSD8Mj1eGWXbB4m1m-vcaZNOHJx3U9xg4tx9aJ8bpLlEXL3-d5ItU1cuwFJg3jbkRdMSBJFMb_AmF_5EhAaqIVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ایران باید پایان رسمی تفاهم را اعلام کند؟
🔹
از لحظه اعلام آتش‌بس تا امضای تفاهم اولیه و مذاکراتِ پس از آن، مقامات ایرانی در سطوح مختلف بر یک نکته اساسی تأکید داشتند: به آمریکا بی‌اعتماد هستیم.
🔹
پس از امضای تفاهم تاکنون، آمریکا بارها و به روش‌های مختلف، بندهای متعدد این تفاهم را نقض کرده است.
🔹
از ادامه حملات اسرائیل به لبنان و توافق رژیم با دولت این کشور گرفته، تا حملات مستقیم آمریکا به جنوب ایران و منحصر کردن مصرف دارایی‌ها، به خرید از کالاهای آمریکایی، همگی نقض صریح و آشکار بندهای اصلی تفاهم بود.
🔹
با این‌حال، آنچه ایران از آن بهره می‌برد، فروش نفت، رفع محاصره و فشار برای کاهش حملات در لبنان بود. از روز گذشته تاکنون، اقدامات آمریکایی‌ها به حدی رسید که حتی همین منافع را هم از بین می‌برد.
🔹
ترامپ نیز در ترکیه تصریح کرد که تفاهم با ایران به پایان رسیده و در تازه‌ترین اظهارات توهین‌آمیز و تنش‌زای خود، ایرانی‌ها را «یک‌مشت آشغال»، «سرطان» و «بی‌عرضه» خواند و مدعی شد ایالات‌متحده شب گذشته «بیست برابر سخت‌تر از قبل» به ایران حمله کرده است.
🔹
باتوجه به رویکرد رئالیستی در موضوعات بین‌المللی و لزوم پاسخ هم‌سطح به نقض توافقات خارجی، ایران نیز باید پایان رسمی تفاهم اولیه و مذاکرات پیرامون آن و مذاکرات آتی را اعلام کند.
🔹
در یک سال اخیر، آمریکا تاکنون از مذاکره به‌عنوان ابزاری برای حمله استفاده کرده است. همچنین ترامپ کسی است که سابقه خروج یک‌جانبه از برجام را دارد و تجربه دولت روحانی نشان می‌دهد که باقی ماندن یک‌طرفه در توافق و پیگیری آن از راه مذاکره یا قوانین بین‌المللی، سودی برای ایران نخواهد داشت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/448300" target="_blank">📅 14:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448298">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4268fce83.mp4?token=WUheEtuGkU59g28W2Sp7Bg9vGqmm_qR8hZp0Vo_vvlUPG04mqsZQ_UjsNAln9WX1LqegG5Psgof_D4ANHAmL_lndiOsyoPkX8EHG9HnOsyYLPUv4AJKvlIbMfELSLUnfM8_25LP_IMiaYvOTDL5aFHbNVjqFsmv9N6A9fVjJtMqK1gahseqRODKCPVM4rKD5sVrMYrXeVJ7o1C1QxXy-2Qc6mVspIF6Cbr6JBu-fjTUjz9l0H3TknJW5AW4F-Yc2nAqhyQC34RGrDTkXxCjHBru-T6vR2FPqYFU-VRrjb0rSD3en5VVnwZiOtTfZUjI94I08nT7gyBbAovc6qeGYhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4268fce83.mp4?token=WUheEtuGkU59g28W2Sp7Bg9vGqmm_qR8hZp0Vo_vvlUPG04mqsZQ_UjsNAln9WX1LqegG5Psgof_D4ANHAmL_lndiOsyoPkX8EHG9HnOsyYLPUv4AJKvlIbMfELSLUnfM8_25LP_IMiaYvOTDL5aFHbNVjqFsmv9N6A9fVjJtMqK1gahseqRODKCPVM4rKD5sVrMYrXeVJ7o1C1QxXy-2Qc6mVspIF6Cbr6JBu-fjTUjz9l0H3TknJW5AW4F-Yc2nAqhyQC34RGrDTkXxCjHBru-T6vR2FPqYFU-VRrjb0rSD3en5VVnwZiOtTfZUjI94I08nT7gyBbAovc6qeGYhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیرکل ناتو: حملهٔ دیشب آمریکا به ایران کاملاً ضروری بود
🔹
فکر می‌کنم بسیار حیاتی است که آمریکا با قاطعیت و قدرت واکنش نشان دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/448298" target="_blank">📅 14:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448297">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wtg7h5RmbI7JlDOmF_tta-DDxgZFw3NVUqD3CfWK7KRMq-4rvS402phaa6KNSQD9jmt9yNrGPoEK8OIu-kq7qbluSvFgEdSeFPR8kJ_xwEnWposH_RGrjjVImWi8keF-Wr2zmYC14QuykJfnfDMLrAII7HdJxaE7o_04cl1VtLnvw0qdRmxkvRga8V4b-9-AQ18aHRlg-bszO0Vwp6CYdXiuLgwc8WD6jJJnvlpb-pBTzlPrSctEkch8rqhRgsOhgagY4v-9DQsQxbnzNLboK6v2Y3YrVszxsUNjo4jDIA0fJGP_LLuy-5iemqIkZcMZB4vAHi3ehQ9XX4LvDiKkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزامات راهبردی ایران در مواجهه با سیاست‌های خصمانۀ آمریکا
🔹
تاریخِ رابطه‌ی ایران و آمریکا، نه یک فصل، بلکه یک کتابِ تمام‌عیار از پیمان‌شکنی‌ها، نیرنگ‌ها و ضرباتِ خنجر از پشت است. از کودتای ۲۸ مرداد تا برجام و خروجِ یک‌طرفه از آن، و از تحریم‌های فلج‌کننده تا ترورِ سردار سلیمانی در خاکِ عراق، آمریکا هیچ‌گاه اخلاقِ وفاداری به تعهد را رعایت نکرده است. هر بار که لبخندی نشان داده، پشتِ آن نقشه‌ای برای فشارِ بیشتر بوده؛ و هر بار که بر سرِ میزِ مذاکره نشسته، در پس‌پرده مشغولِ طراحیِ توطئه‌ای تازه.
🔹
در این میان، یک تمثیلِ ساده اما عمیق، از مادری که چندی پیش کلیپش فراگیر شد، همه‌چیز را روشن می‌کند. مادری که می گفت: کودکِ دو ساله‌اش یک بار از پله‌ها زمین می‌خورد، دیگر هیچ‌گاه او را کنارِ آن پله رها نمی‌کند.
🔹
کودکِ دو ساله، تجربه‌اش را با پوست و گوشتِ خود لمس کرده؛ اما برخی از ما، ده‌ها بار زمین خورده‌ایم و باز هم دل به وعده‌هایِ رنگارنگِ همان دشمنِ کهنه‌کار بسته‌ایم. این‌بار نیز تجربه‌ای تازه ثبت شد و به‌روشنی ثابت گشت که علی‌الاصول نمی‌شود به آمریکا اعتماد کرد؛ نه فقط به دلیلِ آیاتِ قرآنی که ما را از اتکا به شیطان برحذر داشته، بلکه حتی به حکمِ عقلِ سلیم که تکرارِ خطا را محکوم می‌کند. تا وقتی این حقیقت را با جان و دل درک نکنیم، مسیرِ اشتباهِ گذشته همچنان تکرار خواهد شد و هر امیدی به ناحق، ما را به بیراهه خواهد کشاند.
اما در صورت تجاوز دشمن چه باید کرد؟
🔸
۱. قطع کامل صادرات نفت از منطقه
🔸
۲. بستن تنگهٔ باب‌المندب در کنار تنگۀ هرمز
🔸
۳. «هزینه‌زایی» و کشته‌گیری هدفمند از آمریکایی‌ها
🔸
۴. تغییرِ دکترین دفاعی در راستای بازدارندگی حداکثری با حفظِ ابهام راهبردی
جزئیات هر راهبرد را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/448297" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448296">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZl0X-0CGVlQCwIJJDcQo5Zu3JCin9RoCDHP5brOO10XmbxERYIJ7yRy_xUPciIGVVQn4oZ10SKHPtgqYUCACFPjFUUz8HQKcpOoJVloerb2CY5XdcMqdUAwOdTFZW0rWYY9JlLSGRvFwQfUiYtiYqWtU6YeHPuaqswxMuQjPkaehf7urWkzfv9azzZY0-mQFXF046dYWRoF-0obKQ5hT2ZObpIvcgbg-exCkV6qjKOh7UJa65tSZVwcGg9gnUkPvC59iKIzdu42GSdos2V5plPWLOnryHlzA8mvWop8UfNrBagomQirMPLIClpV2kFC68_-w5SO1zF0lFrFYtZuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جلسهٔ هیئت دولت امروز به‌ریاست پزشکیان برگزار شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448296" target="_blank">📅 14:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448291">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aG_BabfKh2jryfnXNuT4DFghYmC5vkShm2j8ACjos87Z0ZdsrZSuvVnjUg2yB6ghYfQuZOO8GVo-yMO8whYCN91WWwbJr6tu3nAs8Th2J0N-J0KmUpg1yaXSGJAH0o7D3h3Yc7ZVtiecK0RbwAtMlqq19Ubnpx5048C3hLvl0UywCdfrDSf606S1aisVWUAQdTUNnXFblZbwhRHkJI3ngBQ0DlXDB2GoJAbIiaY2AKE4cbTEOSRL4JJLPerKl7KHNJu2OlY1B5XHA8UEp2rEst1tcJIMztMbf31wLo-BCD0pg2kNW--C0-tsHSXqvEHSyZbZmGH-pXoBIBNie7VCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qupqh2WRCkfLOXGwJayGx8c-4KLybpk91oCZnRJH66QsIz53fvlAMVte0yQSojoh5kbxosOxzd7p7mfs965SmeqiDg9y24iiQ4_kjKBocApYX7dUWtAE0-l5Wy2glZm8An9eFNChr9QJGSsTGuHcGqGVqD-JQ7FRx_5t0q15OomwxrBqgrrR--1UfNvldoy-W0p1L1eAVOuTO7mgHhkv0JYr2BtPfUOxof0EGBap35FYujZWUyW1zZSv2SCh0QxobOkuGOC5odEMhV-yIz8StWi8Jzn8PNnmGJ7OTd-9ifdrSL7rTaiL2SZLIXZFy4iEoJsg4GrqgfWBEo1dd9tzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KF6CCEu0YlPEI1Ef6JUIpnzPhSL6nkjrl4zdkZaxZktDslrT7AAe5wUfrZoCC8UD47qZhS3fQ82VZz24Rw5TvHnglmvIfSZLnbN1RTqICKDaEQ4dhVhBHlniZzxjjt16JrjJcB3Bz23hNHLTUP6nzTKlRrzeEWEUoTc7z8oFlIRmWLyc0SZcU9oWT02tyFL23I2lxpL9QjXdcgM75dBZgTYiyv9-LACAOETy7pFmuiubBhRrcxQ69EpSTbl0WP_iIg9uucOOjCP6Qz3pzozevD9MqVpdvyoJnPAJs5f9aBo_rYYezb3Uwzb8N0DYil1nbHuH_K_snycjzv2MT84QqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZ1oHKKif-l1ezMA0EUWEhDNDSpsyZ8NwuPWZcO286-8sQcLgzbFDlCIwQo6FAo67mvXrWX4RGr_ooHqFtWP2AbkBJNRup-u_2DHKvf7E-hJcFFsdt_ymi7whxmKrE2lapPhK-IlbzL_INKAVHkbBMTbXGPiFZg5P2Y5esyqD0g1oBS56t4e2TQJ5v3MwSWTUdtyrsP6I922I198AhcBzMO7hKix6pozmuqkOyyQ8fKBla2Tzri6ewz-eM8gCUsR22co0nfwNF6vT_vO5uHLKeWse3Nb5Xp5cgyW7YmWU1aTNevnVdU97Su_b-bksf73ldP2TvUEi75unoJX1WX_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWW0uJqXkepGrokSB9if44kQ_SD3sAGlVvGrY4Nfk5hwU-i9BhvMPPwJG2eoFhFsOPv43HGFEzBaJSj5FFV3Jo46nzNtHQnYj5bE90MxUvwV6K5jRsQDmR-HV_9oSVvVrljflW3idfMnIYqWjJrAhjU7d60TVLtpAZBXryuB7LmRKrfmSK7NcXu2lxfRWWvE7t95rdkqy-S4IdP_SxWj5WB-j7Bn7DJyNti-cpWewp4vFp2_-giQGyFtPEiWkSmzQZRgpAq0cy2b816GW0SmJAtneqih2A0c3cUZHKWSh1JhpqIioct3GphQP5yGvko6zjLQBKUfNV_IIolIDzXcMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلسهٔ هیئت دولت امروز به‌ریاست پزشکیان برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/448291" target="_blank">📅 14:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448290">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b65b53704.mp4?token=OG5zIurWuTP5ZCjqamw9-HX-6MNh96HxTQkVYrWoYSHtCZ5Sk5F0D1-EtOHGCSxH4kPoVTuA3p_Yy4K0t-sgo5WLTZhyxkcJk82590YRSjx8NTOJ9ZzZYhfO_NymNFK1AcgwkMpnW8HSHMIuZRF3ixqnV3IAztjxUrjFBvY_mfhzXoX7mC4F1KS9LBKO9xdk7COUjUd1cYhq7N6L5l4dCo7P9bgrmClBDsbniz4tssiwzabGZ9NEzyUC4NhpLVGkzNrkjNKpsErDILHqz_dAhURlBNDRKAftCJ_DsVx2h7T9huBYJNYpqtEvNzjRFrvsRGdaC9w97kUs53aVXzcokw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b65b53704.mp4?token=OG5zIurWuTP5ZCjqamw9-HX-6MNh96HxTQkVYrWoYSHtCZ5Sk5F0D1-EtOHGCSxH4kPoVTuA3p_Yy4K0t-sgo5WLTZhyxkcJk82590YRSjx8NTOJ9ZzZYhfO_NymNFK1AcgwkMpnW8HSHMIuZRF3ixqnV3IAztjxUrjFBvY_mfhzXoX7mC4F1KS9LBKO9xdk7COUjUd1cYhq7N6L5l4dCo7P9bgrmClBDsbniz4tssiwzabGZ9NEzyUC4NhpLVGkzNrkjNKpsErDILHqz_dAhURlBNDRKAftCJ_DsVx2h7T9huBYJNYpqtEvNzjRFrvsRGdaC9w97kUs53aVXzcokw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پاسخ اولیۀ سپاه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
🔹
سپاه پاسداران: به دنبال حماسه‌سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی‌سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448290" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3fec6920.mp4?token=ONeCHlbXmoI4zxYbStqYVlz0Kpm4BTKu8GyOB7B3qYRBOFJZcoTMAqB9dYns2sOSXLtHgWIhFeLQMZQKz2dbdlv5cBhcv83_FmC_utOyvsIISo9PPFNB77CLBBojJoVrY_0U_96g8rNQK2z-Q2He-L7aVAQYoM3Der0FuGGZH3fVRt7N6IIYVmh5TV0KnZBUwfBXt6k8mrhupCN5wryl5wTiMXDDyMu19y2MnS9sQ9MvlzyZFTDeadmNNKTZZycWwpwo3GQ51Uh_xeep0x2TBKj9UAcUw8xvW1ODIFbj6OsFykTVN3mc-xg1ut3BzZ8Yp5wYmUPvDhdZr6OxnrozU3WbCcFhNdGPWQ_RdvHFECZpzR6QdE1djgyYge3NjPMEj-IJIibVu2bQNHMCUqKXUfiZzkgVVBRBiYT_sWwN8hW0lczbSoXVPy_fqhGIoBq8SbpcRgaUj1BEBRpz0boaaEBiROlsCnVhyWDuvO-Wbc8Xiorz60zgymvAooF8VtXVCHtdgIsNoFCrjbG_NOEOXYknTQaIuyoEUiua051EFJXUnzsEYdNzkdj_FKqYfrPZ_e1qzC7gXutFyR4hnTCHFu-C4uF1tOZjZjKHa9Wm0T7gwt9TchtgmDA_1-RlUBxyzBZeNwuepgvs9-n3y8a_xZpcakAbgtjUH5P2LPQtFTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3fec6920.mp4?token=ONeCHlbXmoI4zxYbStqYVlz0Kpm4BTKu8GyOB7B3qYRBOFJZcoTMAqB9dYns2sOSXLtHgWIhFeLQMZQKz2dbdlv5cBhcv83_FmC_utOyvsIISo9PPFNB77CLBBojJoVrY_0U_96g8rNQK2z-Q2He-L7aVAQYoM3Der0FuGGZH3fVRt7N6IIYVmh5TV0KnZBUwfBXt6k8mrhupCN5wryl5wTiMXDDyMu19y2MnS9sQ9MvlzyZFTDeadmNNKTZZycWwpwo3GQ51Uh_xeep0x2TBKj9UAcUw8xvW1ODIFbj6OsFykTVN3mc-xg1ut3BzZ8Yp5wYmUPvDhdZr6OxnrozU3WbCcFhNdGPWQ_RdvHFECZpzR6QdE1djgyYge3NjPMEj-IJIibVu2bQNHMCUqKXUfiZzkgVVBRBiYT_sWwN8hW0lczbSoXVPy_fqhGIoBq8SbpcRgaUj1BEBRpz0boaaEBiROlsCnVhyWDuvO-Wbc8Xiorz60zgymvAooF8VtXVCHtdgIsNoFCrjbG_NOEOXYknTQaIuyoEUiua051EFJXUnzsEYdNzkdj_FKqYfrPZ_e1qzC7gXutFyR4hnTCHFu-C4uF1tOZjZjKHa9Wm0T7gwt9TchtgmDA_1-RlUBxyzBZeNwuepgvs9-n3y8a_xZpcakAbgtjUH5P2LPQtFTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر قائد شهید امت بر دوش زائران امیرالمومنین(ع) تشییع می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448288" target="_blank">📅 14:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa5a06b43.mp4?token=MD6X-Ph0ENglPcAwRM3XtcDqEbryef1HdXWGUmYKPdRwWpi_cBvhADdKJbDudzP3ADh3zwBSuQbGrQQ_PyL1K3Zv-LdWf2QyU1TWK3F5qCAVPh7sQ1Ueb3DmB-Zwm66dUSmRw_-cOMoO3LtPImxOviFaDIYvYHeBMeYxFimuUVsRAqfCkH3tUe5Ob5nLmljOOKqB4p9EFOeY02ftUSX133sdf_s6zmq1C0t07bDfYhNt49M0zQgdb81bksSH0OCefFDvnXOg3r09jzZf8dfBNheozaMyrAMfAv2oESWTWsI7f_1pEVRAp-CqS5FoNS8iT195XYcgRG8wnASmQ9ZASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa5a06b43.mp4?token=MD6X-Ph0ENglPcAwRM3XtcDqEbryef1HdXWGUmYKPdRwWpi_cBvhADdKJbDudzP3ADh3zwBSuQbGrQQ_PyL1K3Zv-LdWf2QyU1TWK3F5qCAVPh7sQ1Ueb3DmB-Zwm66dUSmRw_-cOMoO3LtPImxOviFaDIYvYHeBMeYxFimuUVsRAqfCkH3tUe5Ob5nLmljOOKqB4p9EFOeY02ftUSX133sdf_s6zmq1C0t07bDfYhNt49M0zQgdb81bksSH0OCefFDvnXOg3r09jzZf8dfBNheozaMyrAMfAv2oESWTWsI7f_1pEVRAp-CqS5FoNS8iT195XYcgRG8wnASmQ9ZASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر رهبر شهید انقلاب به حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/448287" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14423561e8.mp4?token=Gr-lfraBUCiNLKKrHgPi5AD8CtBxxWfDcYi4dOnlm1n3arwDzBor-gyAU2hzGHE8Xe9TtfW04me2QCvIafC_3l_nz4XKrvhweVWlcFxfNY7nAFEyz9y084zXv9mZhdexfFjGjK5cXHZt-mee3xrNehameT3-I1k7CE2j6nLPqioAIigs7qB-pUwpY7ygJQznXLqd2Kg7yUHPtZhqzjv8UpNYNK4HtFCbF4RjFs4y9R4HZgrbqSFbn8qs1ZV_zSpGmXS1gSKDT_dKGh1U0vxASAmgASr2GAwRrCELE5iB65UUm3KQP0IlblfEZZKCv0d8JbRnTCVujJarl8tbTCXcDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14423561e8.mp4?token=Gr-lfraBUCiNLKKrHgPi5AD8CtBxxWfDcYi4dOnlm1n3arwDzBor-gyAU2hzGHE8Xe9TtfW04me2QCvIafC_3l_nz4XKrvhweVWlcFxfNY7nAFEyz9y084zXv9mZhdexfFjGjK5cXHZt-mee3xrNehameT3-I1k7CE2j6nLPqioAIigs7qB-pUwpY7ygJQznXLqd2Kg7yUHPtZhqzjv8UpNYNK4HtFCbF4RjFs4y9R4HZgrbqSFbn8qs1ZV_zSpGmXS1gSKDT_dKGh1U0vxASAmgASr2GAwRrCELE5iB65UUm3KQP0IlblfEZZKCv0d8JbRnTCVujJarl8tbTCXcDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد شعار هیهات منا الذله در حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448285" target="_blank">📅 13:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448283">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb35562f2.mp4?token=DrrYvUzcpFFrnksaW7afBDAZdxiS47dSEDKiyUlfGgpA0MXBGex2GsmFqXgu_ka1Ass_PkpbCWZbIPfFtwCrxHMXMQ4ezETxOibgoJMFnmzGdiPYQ5AuykMbQOb2bHYcHMisqe88_MkYZtWwqALwfuhLZY3DxgD_kpTMKh1Xlik0UVlPbgb1U6Tf21MmGYM2Y3Tf4XxSrZqErYCzDWDesQKu_fDsa0Z0l5SIRMNHzHJ52HCYSuS_v3AAzoZOzu1YzJSDCb3iC-1C_SHJSVusEdXhavcO6R_LMAkdNpv2-7zps-En0exMMhnttZHmfHVjci5m1nkFc0VcsJzXp0aW3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb35562f2.mp4?token=DrrYvUzcpFFrnksaW7afBDAZdxiS47dSEDKiyUlfGgpA0MXBGex2GsmFqXgu_ka1Ass_PkpbCWZbIPfFtwCrxHMXMQ4ezETxOibgoJMFnmzGdiPYQ5AuykMbQOb2bHYcHMisqe88_MkYZtWwqALwfuhLZY3DxgD_kpTMKh1Xlik0UVlPbgb1U6Tf21MmGYM2Y3Tf4XxSrZqErYCzDWDesQKu_fDsa0Z0l5SIRMNHzHJ52HCYSuS_v3AAzoZOzu1YzJSDCb3iC-1C_SHJSVusEdXhavcO6R_LMAkdNpv2-7zps-En0exMMhnttZHmfHVjci5m1nkFc0VcsJzXp0aW3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللهم انا لا نعلم منه الا خیرا
🔸
لحظاتی از نماز آیت‌الله حکیم بر پیکر رهبر مجاهد و شهید انقلاب اسلامی @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448283" target="_blank">📅 13:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03fdde108.mp4?token=AUT1Qu-8FbifXbcdRQ11MviANX-kMVXNn7P7NkyaP4W5bpZQeJNC59kumVd7fcYzG2h4k1OXRFQpmN6UijXLJwR2cEKtJ3R5_sv_V836bzdr3fufWb63fiY1EngxbG1R1s0dDi7F96My-ZX7YRocBq9o5ulCp6fGISPCE7ACVGuvHmoNCmpMlmjYbW_OPGAPzLz8AYbnGrQtBQg_-pHg_m9tA0j7czxkxJItd6yX_yLsKYWGVE_SSk5F5x54Ge_dAKQzLtYYnXhWSHff4G2__QuAgqmv1Ub5z0tVgp2DIXPFEmFv5OCigpiZ5gjCBBwUHaovEbrYa5VU8i7UmlW_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03fdde108.mp4?token=AUT1Qu-8FbifXbcdRQ11MviANX-kMVXNn7P7NkyaP4W5bpZQeJNC59kumVd7fcYzG2h4k1OXRFQpmN6UijXLJwR2cEKtJ3R5_sv_V836bzdr3fufWb63fiY1EngxbG1R1s0dDi7F96My-ZX7YRocBq9o5ulCp6fGISPCE7ACVGuvHmoNCmpMlmjYbW_OPGAPzLz8AYbnGrQtBQg_-pHg_m9tA0j7czxkxJItd6yX_yLsKYWGVE_SSk5F5x54Ge_dAKQzLtYYnXhWSHff4G2__QuAgqmv1Ub5z0tVgp2DIXPFEmFv5OCigpiZ5gjCBBwUHaovEbrYa5VU8i7UmlW_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای زائران حرم امام حسین(ع) ساعاتی قبل‌از آغاز تشییع
رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448281" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8be57da6.mp4?token=XeiVC9egfaDwUwhCaGIlTrFtSOFxtFP2Cv6IJ8GH0-ruYk7xXxA_ykVID4hJNgNgZpKgC22Y9xmb9cRdXOdkW3PvQn3pAzkKJvUD1E_OiVdwqv3hW-7r7HI1NaDuKcGcgoeqBclRY1twuLymZRukSg0UInpv11kW4aoT4gxz37y--GtnjKu6DJdGoLdtkM1rsnsUoNI3RvY7K1FiXIT8K7zH0Ej7EoJOR0ecgTnsGtPo4Ghd0SvjDOrJjKZ4zCv4ATp5quEJqXxJks-ITqouZf4pKCcx-QIE7riha7xxeVriBYJ4QzTmEKzHKhBoCIUz24C2qDkYVifb4qM8xOdQrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8be57da6.mp4?token=XeiVC9egfaDwUwhCaGIlTrFtSOFxtFP2Cv6IJ8GH0-ruYk7xXxA_ykVID4hJNgNgZpKgC22Y9xmb9cRdXOdkW3PvQn3pAzkKJvUD1E_OiVdwqv3hW-7r7HI1NaDuKcGcgoeqBclRY1twuLymZRukSg0UInpv11kW4aoT4gxz37y--GtnjKu6DJdGoLdtkM1rsnsUoNI3RvY7K1FiXIT8K7zH0Ej7EoJOR0ecgTnsGtPo4Ghd0SvjDOrJjKZ4zCv4ATp5quEJqXxJks-ITqouZf4pKCcx-QIE7riha7xxeVriBYJ4QzTmEKzHKhBoCIUz24C2qDkYVifb4qM8xOdQrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شروع نماز بر پیکر رهبر شهید توسط آیت‌الله حکیم در حرم مطهر امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448280" target="_blank">📅 13:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448279">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/218707fb30.mp4?token=FTHf7604BfY7u_2ri3GazheMB5CWziHIRvlOvZzPu7O6pwdGSooQySHYp7lqLlLqZjXISONg8fTI70kY-nBmeroU43iNKCXRIkowsj38Bl0lf4dXWXJuHFe22eD3A1fwIiR_Qlfk7if24x1UvDp9b5HRVngJY-tsreYxBG5jKwGw1jGaLvcDUMkzCI5EPhwbC3pZtS6CSvtjm8RY06t42hEOgOdFyswD8_zqZ3FxlVYfnBSmk-fGnnaDpWZ5mSKewp7Ek8HcqQmWt3glHvG4a26s7JESoDVo34DGaos1_SLRKkA3dSwcULvECnnXiwdDye-z2l37wVCB6CuDM9zFxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/218707fb30.mp4?token=FTHf7604BfY7u_2ri3GazheMB5CWziHIRvlOvZzPu7O6pwdGSooQySHYp7lqLlLqZjXISONg8fTI70kY-nBmeroU43iNKCXRIkowsj38Bl0lf4dXWXJuHFe22eD3A1fwIiR_Qlfk7if24x1UvDp9b5HRVngJY-tsreYxBG5jKwGw1jGaLvcDUMkzCI5EPhwbC3pZtS6CSvtjm8RY06t42hEOgOdFyswD8_zqZ3FxlVYfnBSmk-fGnnaDpWZ5mSKewp7Ek8HcqQmWt3glHvG4a26s7JESoDVo34DGaos1_SLRKkA3dSwcULvECnnXiwdDye-z2l37wVCB6CuDM9zFxDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت امین‌الله در حرم امیرالمؤمنین برای آخرین زیارت رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448279" target="_blank">📅 13:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448278">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77adac8641.mp4?token=kFq84Y30fFIfhqJleLGebJHHkte6rArA8Lu5PutCPX_IjMjwS1NkpZMke6CeJT9NLn58igsTvBcFLhqURp4dHTNobbGJnWW-cFZF_jRwyQSsa6el6R85Lyb8mebB643FSGQfZ3oxgCPmHtlRCH4ezKjnNHk2EZbD96F8dRv3fQ7oA0PUQXhlcPYad-iDjTWyE5pF9EtHbnb6-F-dNgz_B71Jmq4KwVB82WedqYWHPoYartsAk8A3ilqfoGgxjY4krYnQAf9PnNmTAyqtLvPjqCNfr0iBLWSi04pfA2wlRaS_5zHRT-ZH77FnxNBH6Dej_mxmQqK07D862DDd1j9-eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77adac8641.mp4?token=kFq84Y30fFIfhqJleLGebJHHkte6rArA8Lu5PutCPX_IjMjwS1NkpZMke6CeJT9NLn58igsTvBcFLhqURp4dHTNobbGJnWW-cFZF_jRwyQSsa6el6R85Lyb8mebB643FSGQfZ3oxgCPmHtlRCH4ezKjnNHk2EZbD96F8dRv3fQ7oA0PUQXhlcPYad-iDjTWyE5pF9EtHbnb6-F-dNgz_B71Jmq4KwVB82WedqYWHPoYartsAk8A3ilqfoGgxjY4krYnQAf9PnNmTAyqtLvPjqCNfr0iBLWSi04pfA2wlRaS_5zHRT-ZH77FnxNBH6Dej_mxmQqK07D862DDd1j9-eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت سر رهبرمان آقا سیدمجتبی خامنه‌ای ایستاده‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448278" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448277">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32f5bc389.mp4?token=P5fyrmneAN0573fD-pLZToTR-NnCrTH09x_VZUb2EZh76xKa95iYH_1g0BiuRkH5FzdSEMcpFGSV7q6SaUdAZQvBGgavorf-lgC0cxcClrXmKabqnZR4GNlgTBKU4VzxjX4eljfB1s2ln7ZR297hFJPfkXHH-PiUrlvUC9zMM6eSii0THzGcXdzXw__iIa6-X2O7MlFhXQhJS-JE41Q-6hjxLeOJDCh3asitSdD91PHTr88Xa0-rPDVJHcdW05bUvdAMQowgKAmHK9_ZDA-BKjn5Hw_tPiV8cGqYqt8wTAC6Nq8lMHaZ3DhaZj8FOixJS9Os2BI9uaLP7weyQEb4zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32f5bc389.mp4?token=P5fyrmneAN0573fD-pLZToTR-NnCrTH09x_VZUb2EZh76xKa95iYH_1g0BiuRkH5FzdSEMcpFGSV7q6SaUdAZQvBGgavorf-lgC0cxcClrXmKabqnZR4GNlgTBKU4VzxjX4eljfB1s2ln7ZR297hFJPfkXHH-PiUrlvUC9zMM6eSii0THzGcXdzXw__iIa6-X2O7MlFhXQhJS-JE41Q-6hjxLeOJDCh3asitSdD91PHTr88Xa0-rPDVJHcdW05bUvdAMQowgKAmHK9_ZDA-BKjn5Hw_tPiV8cGqYqt8wTAC6Nq8lMHaZ3DhaZj8FOixJS9Os2BI9uaLP7weyQEb4zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید به‌روی دستان زائران برای انتقال به جایگاه اقامهٔ نماز در حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448277" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448276">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
وزارت برق کویت از قطعی ناگهانی برق در نقاط مختلف این کشور خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448276" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2edb7d3fe4.mp4?token=VYfLMmkDuXhgSs52FpGJQCuKCR-vaZST8M3L1aR67c4HRvsdjP--tl6odfSDusqAFQY4sMgorEinG1dyAAcqKJz1QQbceIYPzA-xdX6r8ZfVvhEnGHntJS8FTrm3fUbj6ExHirUOagEC6i_KRfQsinLFUA7FCbn_abkqseJrmNfhDZtq7ZHsXhHYEP9E3jZLDgZkctP-WuGJwRujmuabGBKxMog9V19-CD_PstQyMRn-N9-NdOJVhRLqJldJL6rd6UMT-zcH0i-6YOM1mmVs0SxRP6rCV2HXdLmLI-1xxCh8WxtmzHqwEhorrwhg6ipPW2RVlAC3rhKS1zb_sjyzUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2edb7d3fe4.mp4?token=VYfLMmkDuXhgSs52FpGJQCuKCR-vaZST8M3L1aR67c4HRvsdjP--tl6odfSDusqAFQY4sMgorEinG1dyAAcqKJz1QQbceIYPzA-xdX6r8ZfVvhEnGHntJS8FTrm3fUbj6ExHirUOagEC6i_KRfQsinLFUA7FCbn_abkqseJrmNfhDZtq7ZHsXhHYEP9E3jZLDgZkctP-WuGJwRujmuabGBKxMog9V19-CD_PstQyMRn-N9-NdOJVhRLqJldJL6rd6UMT-zcH0i-6YOM1mmVs0SxRP6rCV2HXdLmLI-1xxCh8WxtmzHqwEhorrwhg6ipPW2RVlAC3rhKS1zb_sjyzUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید به‌روی دستان زائران برای انتقال به جایگاه اقامهٔ نماز در حرم امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448274" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5390d35ec5.mp4?token=UB6yujeCDPe5WC59EOlAUoPJaVxpeBkq267LN99t6PkuszaYJ6KyGpkA-1773__OoMCfEnjjXUBvUkNX2-nBVjWrBjpSECCAiwNaMJX0vbJBR4VO1DicHRAbKbV5mHuKzoXXaBhR022quqWfsshmuLYcedn4Jzqa7IxdwPg-yhb_WxWj7HG6uOWvStZW75UuYuA3dnovvBRclHSzIaBK35PoCli7vM_NAoIeSF-WLB9uajODaLVAygVuA5SVo4a04HuY6XRfR7Eg4yBRlodaNKeGBCm6H-RwMbD9l8GsYi_D8_E_jS44iuOAPfMrzqpdnBoTU1ZaJJg7nynJIPIaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5390d35ec5.mp4?token=UB6yujeCDPe5WC59EOlAUoPJaVxpeBkq267LN99t6PkuszaYJ6KyGpkA-1773__OoMCfEnjjXUBvUkNX2-nBVjWrBjpSECCAiwNaMJX0vbJBR4VO1DicHRAbKbV5mHuKzoXXaBhR022quqWfsshmuLYcedn4Jzqa7IxdwPg-yhb_WxWj7HG6uOWvStZW75UuYuA3dnovvBRclHSzIaBK35PoCli7vM_NAoIeSF-WLB9uajODaLVAygVuA5SVo4a04HuY6XRfR7Eg4yBRlodaNKeGBCm6H-RwMbD9l8GsYi_D8_E_jS44iuOAPfMrzqpdnBoTU1ZaJJg7nynJIPIaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریادهای «لبیک یا حسین(ع)» در حرم امیرالمؤمنین(ع) در مراسم تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448273" target="_blank">📅 13:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448270">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFw0U-UKcKoUqK1Qm2uj4dcth_sj1L7diXlE0FAHy6p72P8Q-gB0RzvWMGPH9gKNPHcsUwklvRTLlH9uCSJrdsUb1jZ2RIJSqdsomGPH14SGHUCHDgw5mBK-LyNQL57VdTOeNAmC50uXfVwP1RX1ikTQ4dgvc-6NJn7lGpCDc3ZvaVslOQIG-7DgJtWmeMCTo_TRYgWLxie4u5Q58INKgC2kF_65Zr4FAKh1o7mYsCQBSQwYfPspLgJ4fOlIcU-cHySyHPUX-ufaLlf8agcW8sUzUmxRQOHGf9sptkdURlrc9iVCQzqUeEBdHrr9rgfIluAWaPAqi-ITE0bvxtUdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیریت بهینه مصرف انرژی در پارس‌خودرو/ کاهش چشمگیر مصرف آب، برق و گاز در سه‌ماهه نخست سال
پارس‌خودرو با اجرای برنامه‌های مدیریت مصرف و بهینه‌سازی فرآیندهای تولید، موفق شد در سه‌ماهه نخست سال جاری میزان مصرف آب، برق و گاز را به شکل قابل توجهی کاهش دهد  ، اقدامی که در راستای افزایش بهره‌وری، صیانت از منابع ملی و حرکت به سوی تولید پایدار ارزیابی می‌شود
بررسی اطلاعات منتشرشده در سامانه کدال نشان می‌دهد پارس‌خودرو در سه‌ماهه نخست سال جاری، همزمان با مدیریت فرآیندهای تولید و اجرای برنامه‌های بهینه‌سازی، موفق به کاهش مصرف حامل‌های انرژی شده است.
بر اساس این گزارش، مصرف گاز این شرکت در سه‌ماهه نخست سال به حدود یک میلیون و ۸۵۷ هزار مترمکعب رسید که نسبت به مدت مشابه سال گذشته ۱۹ درصد کاهش داشته است.
مشروح خبر را
اينجا
بخوانيد.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448270" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448269">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/448269" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448267">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384f20b858.mp4?token=Sy_KgWNQoWaKvM1a8VkLmFETtmJ1Hngx1LY-qNDkSqYaXK7InUtFWlAblUte7o9EIRtQwa8o2uv5rbidhPpmGK5IH_jCAguAFhY_s2rl6jlP1JFAfAtSDStIRE2Y0YthEsShGw6YzSlrcy2Xu5qTEb3DxElJvT4g9SzFWHSta2ZXnQHCrFjfFAgJil2vN0OxUc-SlcsGA_edyOaGT1u5BXaum0H8QZRxeABGlqUUiluciT5sh3JyTXdIuZqeYAMMwaggDDw21QGJz_4uqULlCqzStioVaHeAzI_GhltevS-PWMoTMEIdMRBYVKxkAAuq53B5I1cGxJEGNc9wvKOvQEcd-2f40JX5C_snHZAIuBZMxKCzpb4IOhalACRVfWW1RplAyMQTWLc80hui5L40f4bxd63yZOJOMksy9vNKv1E6DVLSlfGxRW8nzLOglxR3s3TkHYAoDCZwkNuBdIiS-qU4RCgrl6QXWZ07BdTowjIkh0lBEbTlHdbtVCM5M80N-DOYFkYIF12-2G3M3UVFgYs6CSO2EYJv_yUDG_A-iPrhxZQwCtJhDbKkgNaXDZlUqfVMrsZaiKvM7mh24-M47mP-KBtbWM8ntVu019uns5xy7OUFkf-eT-TOdNe5qqZCD_Y5OIXEG6rL6MWbzU3ZQDo5-oj74Sg729j-3LK7yuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384f20b858.mp4?token=Sy_KgWNQoWaKvM1a8VkLmFETtmJ1Hngx1LY-qNDkSqYaXK7InUtFWlAblUte7o9EIRtQwa8o2uv5rbidhPpmGK5IH_jCAguAFhY_s2rl6jlP1JFAfAtSDStIRE2Y0YthEsShGw6YzSlrcy2Xu5qTEb3DxElJvT4g9SzFWHSta2ZXnQHCrFjfFAgJil2vN0OxUc-SlcsGA_edyOaGT1u5BXaum0H8QZRxeABGlqUUiluciT5sh3JyTXdIuZqeYAMMwaggDDw21QGJz_4uqULlCqzStioVaHeAzI_GhltevS-PWMoTMEIdMRBYVKxkAAuq53B5I1cGxJEGNc9wvKOvQEcd-2f40JX5C_snHZAIuBZMxKCzpb4IOhalACRVfWW1RplAyMQTWLc80hui5L40f4bxd63yZOJOMksy9vNKv1E6DVLSlfGxRW8nzLOglxR3s3TkHYAoDCZwkNuBdIiS-qU4RCgrl6QXWZ07BdTowjIkh0lBEbTlHdbtVCM5M80N-DOYFkYIF12-2G3M3UVFgYs6CSO2EYJv_yUDG_A-iPrhxZQwCtJhDbKkgNaXDZlUqfVMrsZaiKvM7mh24-M47mP-KBtbWM8ntVu019uns5xy7OUFkf-eT-TOdNe5qqZCD_Y5OIXEG6rL6MWbzU3ZQDo5-oj74Sg729j-3LK7yuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پایان فراق
🔹
مرجع معظم تقلید شیعه حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای زائر حرم امیرالمؤمنین علیه‌السلام شد.   @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448267" target="_blank">📅 12:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdXuC8AqY65RJ1V6APGtUHb7h3AoxbXfbrfdcQYK5-1OTN_-OWIpYwhzPbuJsUH5OdvOM9aJ4DeOu9aNwq3vHfqzDleyv9p5ttgn_AdjyCHn6djvp3VzaDISF2me6ZHjcyJRrJjABZOr02qG23Y8ggGPL2hpMhfWiOgZb8boDW3O8F69-2GwJPiosGZ8HydbDrB6nZPr8wquIH4U6pZsgz5_gzML13ApVnk4NK6T2GhK9V-PzPDeCBJrQKQaEmy47HMyGvMZJL09KdA-FpnN4g6-9ZHriI84MkFp-6p83lbTwhH9jyVqU7yUAmGxM2T1R08z5161dWLkv7ds6yQdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: ما با قاطعیت بر حقوق خود ایستاده‌ایم
🔹
رفتار دولت آمریکا به‌عنوان میزبان جام جهانی بازتاب‌دهندۀ سیاست خارجی شناخته شده این کشور است: زیر پا گذاشتن قوانین، تحقیر رقبا، ایجاد موانع و فریب‌کاری.
🔹
ایران چنین بازی‌هایی را رد می‌کند. ما با قاطعیت بر حقوق خود ایستاده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448266" target="_blank">📅 12:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRKfoTlLa5RumUZxT0FeVdZ-BJ-7edHjLmfyfMs-BswjmaozlPjSNcTntrFes6ktSqhE7_MDpU-Cc-LtWmNmfPWV_Lp-Mil_tJBWzFXtjMAEK9nktW8TSQ6O1HeQe4T3hf_KvT4c70a4_ri2DE7IT7OUFw-08QFO0zbW-ES2VGVe2eme_2kCtTyD5I0UdQWh_I3nGil2QhHGdHxYlaaMwX4oBSWDEKGXLYWfEOhjebNhcmDc_iUnX2llGqdFdnZdP5L6i-qSzMSGURE9sDj80gaYD0NU5-rlJjaqEc4FWUtowcjXu8yPS_VXXHHDHSMoqsfvxN6D71LIHT9P4fCKGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تشییع پیکر رهبر شهید انقلاب در حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/448264" target="_blank">📅 12:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_hioUfShc6cNieEgCCW1JKbMI88kBk1v8NyHJwgzOgBxekVn8XhRnKNSjaDrA82G3WdxWyDmZYLdcN6x5488f86-wwjewZr750sU6-5GfVm0o4apVaTWJgLDrGxe_pRr2musDdvDlQypFhASwerrpfPTXHMguC8yqB-T0_g4dacuBL780W0Q-GV4SxB0SJdP8qeFd5858TRO8DsSiRqtWHU95y2D3_qnjSI56194ogCoz_l7_MTtqYHqjuQhKl779Oh2IoEcWFPoHWSdHiiTe3Qsr-faKz71r32Kh7qu41RQ10SdjcKd-ecJTZfvD6QUJDRWZ3S6rAY9DmouXueAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۲۰ هزار واحدی به ۵ میلیون و ۲۹۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448263" target="_blank">📅 12:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448261">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIdLdI5tAiKVzlHWINMDmtTwWSaAni85KOqRRuZ9RyRAze27g-GKrQ-iWrSy7bAfe1SSCmpfs57ZA9-BrbsM-krhGeyMqUIxKt0A-Kd2mx1vrxwvkr21nIKU6Ud8z5FI8Hx3IGLYa17CofYg3C4wKVK2OO7NTp-qf4bWvB2OzYCj1kBMkxxHM0LHRLHhmfK-1ZmpwcTUWPwjwcNVAj6AnkAm9R58teRF7B20svxvNmld7CsWNKq_2uWKeKYNs5h6Lsl6SydAB8svIO3ya2z2agEdgkBu9ahY80CbB1lg8CZ6qtsnNTT7HehtdXQZukn4UOxUoo7WhQflA19O29uifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ آنچه لایق خودش بود را به ایرانیان گفت
🔹
رئیس‌جمهور آمریکا پس از آنکه ارتش این کشور با نقض تفاهم‌نامه، خاک ایران را هدف حملات قرار داد، اظهاراتی توهین‌آمیز علیه ایرانی‌ها مطرح کرد.
🔹
دونالد ترامپ در تازه‌ترین اظهارات توهین‌آمیز و تنش‌زای خود، ایرانی‌ها را «یک مشت آشغال»، «سرطان» و «بی‌عرضه» خواند و مدعی شد ایالات متحده شب گذشته «بیست برابر سخت‌تر از قبل» به ایران حمله کرده است. او همچنین اعلام کرد که یادداشت تفاهم با ایران «مُرده» است.
🔹
ترامپ گفت: «دیشب محکم به ایرانی‌ها زدیم — بیست برابر سخت‌تر از قبل. یک مرضی توی مغزشان هست. آشغال هستند. ازشان متنفرم؛ هیچ‌کس دوستشان ندارد.»
🔹
رئیس‌جمهور آمریکا در بخش دیگری از سخنانش با لحنی تهدیدآمیز افزود: «آنها یک مشت آشغال هستند. اصلاً ازشان خوشم نمی‌آید. وقت زیادی را با آنها تلف کرده‌ایم. بی‌عرضه هستند. بهتر است فقط کار خودمان را بکنیم.»
🔹
ترامپ که مدعی است سال‌ها هدف شماره یک ایران بوده، گفت: «آنها می‌خواهند رهبر آمریکا یعنی من را ترور کنند. من سال‌هاست که هدف شماره یک آنها هستم.»
🔹
وی در ادامه با استفاده از ادبیاتی تهدیدآمیز گفت: «باید سرطان را زود از ریشه درآورد. نظر من این است.»
🔹
در پایان این اظهارات جنجالی، ترامپ به صراحت اعلام کرد که مسیر دیپلماسی با ایران پایان یافته است: «به نظر من، یادداشت تفاهم با ایران دیگر مُرده است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448261" target="_blank">📅 12:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448260">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2152e5282d.mp4?token=uk_I6puEsQEcXqZzEBiR0Ru9kz7HMVlXqVHF46cS4bIZbNfGoIf9D2DOxhs5eKGEU0QRQEtExXDGLAxDDxXxdS7Ymck5Q-VJw3Gxo-UnGRS4LDg3cXWfxeoi8k4OrxR_bTDjsU8ctR3Edu6ayQ1OCRrg8CukZX8yKGO7OTf6p_u0S413Uw7tJIV7vYvZNgATA7jLC-aoXFkfwHRhdz-aRxQCdFkr2wIEtcfULbQK2x2bz-OzSIzUFEfRI5DopYgEQjjwRBM5I8BW0mm93j4TgcsKTH-aZsPlteHonBJDUEwse7ycaIvTcoLsHHt8k-UNqfkmbeFJSo0kWuY3PrOTQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2152e5282d.mp4?token=uk_I6puEsQEcXqZzEBiR0Ru9kz7HMVlXqVHF46cS4bIZbNfGoIf9D2DOxhs5eKGEU0QRQEtExXDGLAxDDxXxdS7Ymck5Q-VJw3Gxo-UnGRS4LDg3cXWfxeoi8k4OrxR_bTDjsU8ctR3Edu6ayQ1OCRrg8CukZX8yKGO7OTf6p_u0S413Uw7tJIV7vYvZNgATA7jLC-aoXFkfwHRhdz-aRxQCdFkr2wIEtcfULbQK2x2bz-OzSIzUFEfRI5DopYgEQjjwRBM5I8BW0mm93j4TgcsKTH-aZsPlteHonBJDUEwse7ycaIvTcoLsHHt8k-UNqfkmbeFJSo0kWuY3PrOTQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آتش‌بس با ایران تمام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/448260" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448259">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1UBzRxvixp_J0ae2nTbegUIskaDbPD0MseCo0J8803NW2Kou-41QqP0F8jGU8w1J7q9v8fBl_UYeOwIa4bZoeadETtKlcwtc8-xpnf9pzA6UGaCkmAclEEsrBMICuyz8U0I_bbu1QYMk-kajIxW8-0sATygoxuO18eJBK2t8TyO7s8z3TVTgB9YqApPRpeGYCt_Wtz7ohMrT9dz84Id3bd-fAiGjbUEGcawVzvu1yrKS7h_mfmpbOD3yO9xQP6Qyt3FdBb2pcZlkK-aQkM4qE8PuposRpRsukSZfeeuO0cTBTWJ1KbxBKDFWuDIXdylNsanfKijkc9dNmVSdATF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور فرزندان مرجع عالی‌قدر، آیت‌الله سیستانی، در حرم امیرالمومنین(ع) برای شرکت در مراسم تشییع و اقامه نماز بر پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448259" target="_blank">📅 11:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448258">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941931326b.mp4?token=Lwva1DHRrqdwDz400eJifeFltztdTh5hyeKyLIvB08lzf14y-Zkz-_4rWGSiWC74He7txjEGAelJvuctqwXVbYPQ5IMNwuctVEItn0w2m39658bvjYQweKdJy4t4EFP_3hRkEzFObigd0SwOwQoeCv9ymKIsliirBZXUzv3b2B_MuCmrmaTf1gUusxdQmOfYK0rpHeWhZy2R5PYsNHkAdVsohrdxcwv4jjEIddlk9AmKP0IyfP6eroRLcnbkMU9k0Q9QLxYPBxw81l8z8DIBAaxULp7ubk5Oy0LB0sh17Ig0swgi6dFHUF9a5hH-Nt7sxKnNxKcxOpiqRi7sbnMd86iYxCzQ8Ppvb9aTZKvlskD3VOEKP1EZKbq9dSl2weHYVjGKEY9AnkpG8wnszMT5ejlyOrYrzlJ5-EzM6spubT9i0PkmyPGRLZI4hUCCFsDAbdMhRivAbjllCx8VbHeDwvcb04x0vMNrhV4pRQG-knEhFYlV_wy_EAX7gOoowGowSO2e2MtRnTs7lm6lCFYtRfLlOarXrDPUAgEG-jEO53DBGpR1C8mwI9EdGYhzMQc4YNZRqLeDzfLt-B4mmVceaqEjggC3MfgzTukhW6JlXs5FwS-oLKKohpex-PY-m9VfCZFkoyIiZnvPyC09b56WCodkEmytffqc-hirDp-h4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941931326b.mp4?token=Lwva1DHRrqdwDz400eJifeFltztdTh5hyeKyLIvB08lzf14y-Zkz-_4rWGSiWC74He7txjEGAelJvuctqwXVbYPQ5IMNwuctVEItn0w2m39658bvjYQweKdJy4t4EFP_3hRkEzFObigd0SwOwQoeCv9ymKIsliirBZXUzv3b2B_MuCmrmaTf1gUusxdQmOfYK0rpHeWhZy2R5PYsNHkAdVsohrdxcwv4jjEIddlk9AmKP0IyfP6eroRLcnbkMU9k0Q9QLxYPBxw81l8z8DIBAaxULp7ubk5Oy0LB0sh17Ig0swgi6dFHUF9a5hH-Nt7sxKnNxKcxOpiqRi7sbnMd86iYxCzQ8Ppvb9aTZKvlskD3VOEKP1EZKbq9dSl2weHYVjGKEY9AnkpG8wnszMT5ejlyOrYrzlJ5-EzM6spubT9i0PkmyPGRLZI4hUCCFsDAbdMhRivAbjllCx8VbHeDwvcb04x0vMNrhV4pRQG-knEhFYlV_wy_EAX7gOoowGowSO2e2MtRnTs7lm6lCFYtRfLlOarXrDPUAgEG-jEO53DBGpR1C8mwI9EdGYhzMQc4YNZRqLeDzfLt-B4mmVceaqEjggC3MfgzTukhW6JlXs5FwS-oLKKohpex-PY-m9VfCZFkoyIiZnvPyC09b56WCodkEmytffqc-hirDp-h4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر قائد شهید امت وارد حرم امیرالمومنین(ع) شد  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448258" target="_blank">📅 11:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448255">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-Fb2IsLSBdf2lKfWf5xmX7-H6ZKVH0SQeWBco-rdBkGFgGVmXtolbBg3aN4rjC3W253y37eh5qIs0tYIcEKQIQkr5QURoB7oFuZby5EKxApXkaNBXSEgtMsd-wql9ck4fLofVqjFDie29tLG4Qas92T0ji2nyULZTAbFtmN7d58_2yaZdll8I5DT6MjbROsJEnGED20S9sNjMLankpjSqmLMQojyyUibtOqe2RGvu7BYtw-nty3tnaLXh2At1zybZXXPyODRg2dxUrtm8dhml1T4gn8wcwp2-16-n3-UiXrlLpSsYuoTv1jywGL2cVL1DnpksmLdtFFsOeOvAyHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKHC6zbPWWD_Ps96WuD5f_nlhJW9cPK2EtjbHvyUcBaeGZw2zcvjZBT-6Jb8aHeSXhIuizEww8Fse_2hEvoQQdcv3FCxokgct65m-Z7hMtpepv52lgMjFGXtKolU2VdgzzVKclyqTc3m1SZrr6hnQmlh59Q4Kfh2yF92PdLwbHp3KXEMCj5l4EqskQrhlnjLjcZauVFTcrx03BmFhP8mc_7kd-M5ROC2gCstWbVSEDVHlmgtZn-MA2PCCHe7l-OlqY2_IpYqmP6J8MKUwhXbOOCRN2lSEGBdrRc7hLhrJQ3zqOp5jcKk_Q03cU3658r7lxlSw3giw4_V9nsOvIkfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RapszbVn6tn-qjzuoGVujQo5OY4lI9HwkLzj2TrAZNEMbg5s5DW5fawNAgYV-t-z6LybtqHqwMXEgHAECsJYc4wNI4q7y7h-cXZ-Y1rPa3pNnqpNATLyHbQuKYvoLatk338EJQh0gFnTwbiqJKibait9kb2WBGCN1D1CbFtLx1YJS5YKueOIzSYGrBnZuhJAZ2EnnJDDEuBnQWsm4P4XseP7vRP1xEXJszb38-AfoxgY4PipvCMRFY0stoFE3hWeByEA6hz41t82YwKTzvdzA1qeXVumKOYKF6izPnzJjxhNMR4upGZU7Ep9hOiy87cpsTLcaaeS-28o-YwR4w6Mpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک فروند پهپاد MQ9 در آسمان خورموج ساقط شد
🔹
سخنگوی سپاه پاسداران انقلاب اسلامی: در پی تجاوز هوایی ارتش تروریستی آمریکا در سحرگاه امروز، یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند هوایی سپاه پاسداران انقلاب اسلامی در آسمان خورموج استان بوشهر، مورد اصابت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448255" target="_blank">📅 11:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448254">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lir8zXa1SD6GOXOAqnpBRj52S4sbp_3nv8C4h6i27kqRjxkSnNnHvuZmQJfWpRTftWYEoDealTo20DTgt0JC59j4xefP5miqEvzqSYL0EvEK9XovlrETxd4XLoz1S6eoRnJA_UfAASStNL-LhZxBoc8PjxybxI87YK6Ku8tjhFGtxV7-c1jE3_-wyp2VqLZqvCoq0iU7snto-TFeUz3DfbR4jZWApLe8QT6b2WLJSkoExM18FI_GO5PHE62BO57AXLJSlbGBhjDsVP_MPQ1-OGJxuBTHPUSWKv0fxo9LIJJX0-YZatct0A_qdrMhdmkOpKgNeLxMkdTgwhQ8gzp7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عراق، وداع با رهبر شهید را روی تمبر پستی ماندگار کرد
🔹
وزیر ارتباطات عراق مصطفی سند از انتشار یک تمبر ویژه برای ماندگار کردن مراسم تاریخی و باشکوه تشییع پیکر رهبر شهید انقلاب اسلامی ایران خبر داد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448254" target="_blank">📅 11:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c7638b76.mp4?token=X2l99Sc5RKHaB8PT-ARg2v1ueCaM3BsCIxmaabeeYCv_cigBCOvLmIpT2DTbp8u3AUhkQIDsgumbgotPnxjmowJU4KhZ94z1vyHqd8tqFm6Q9nwMpyRsfQYHaTEpObegGti1Z99OPtUWuZ0KYLRmfLgLIQxknr6nItyv6xvmIzOqY57Q9444N6b3zv0QT_5SM_5r-ToSGHJOT_Yp5KfgEr0gQQd6yNt7iP8lSsnsaqN-eqBSPxwp3YbPhBVWubQLowPWpdSNgZfuZFrdSav06rJrdyyfy9zF716gok7qGM1a_7dVDqLY33E659gsodxaMnPGbSPVCzFw5lLqJZ4ocCqOrvGF3VVulszNfBdkffH0HplnWQEQpsHK4TqH3Nm7kpd8W_8gPKRbrw3GVEhhB9kRqLofAPIOiKtd45P_eLZ38yUIi4UL94PGPBephVqttpig4Nq-bf_IZjf7JT61tJYP3UJXdLCYaBPzbtmWaIsZWcxRmEszHtxauoxgsMP-kzmfGjAeCFhonsMIYxOK_BKaiQv-uAMh9iPgShXK5sjNTIQRbLaXA6ZO600_3Q8l0Nl-DfJ5QgAirW2OMl-p6_Fxc0o7jWR3ZfxVUMasXsYKkmwTz1fBRxUtB1_6Y3efcNxmBvV5V-0GJ8UY2w_8xqYYygmaijYUcH9zv66RCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c7638b76.mp4?token=X2l99Sc5RKHaB8PT-ARg2v1ueCaM3BsCIxmaabeeYCv_cigBCOvLmIpT2DTbp8u3AUhkQIDsgumbgotPnxjmowJU4KhZ94z1vyHqd8tqFm6Q9nwMpyRsfQYHaTEpObegGti1Z99OPtUWuZ0KYLRmfLgLIQxknr6nItyv6xvmIzOqY57Q9444N6b3zv0QT_5SM_5r-ToSGHJOT_Yp5KfgEr0gQQd6yNt7iP8lSsnsaqN-eqBSPxwp3YbPhBVWubQLowPWpdSNgZfuZFrdSav06rJrdyyfy9zF716gok7qGM1a_7dVDqLY33E659gsodxaMnPGbSPVCzFw5lLqJZ4ocCqOrvGF3VVulszNfBdkffH0HplnWQEQpsHK4TqH3Nm7kpd8W_8gPKRbrw3GVEhhB9kRqLofAPIOiKtd45P_eLZ38yUIi4UL94PGPBephVqttpig4Nq-bf_IZjf7JT61tJYP3UJXdLCYaBPzbtmWaIsZWcxRmEszHtxauoxgsMP-kzmfGjAeCFhonsMIYxOK_BKaiQv-uAMh9iPgShXK5sjNTIQRbLaXA6ZO600_3Q8l0Nl-DfJ5QgAirW2OMl-p6_Fxc0o7jWR3ZfxVUMasXsYKkmwTz1fBRxUtB1_6Y3efcNxmBvV5V-0GJ8UY2w_8xqYYygmaijYUcH9zv66RCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر مطهر رهبر شهید در نزدیکی وادی‌السلام و حرم حضرت امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448252" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63c078ceee.mp4?token=tCpUQs-N5E7KT1CW3VXr-uZWHcE5kGH9bNygpmcl2BQjlVxLWaMmrjVGOyOPCw3HqFcQHht7B6vreaN0PYaFTfTve0YUuQQfhc544A6ehVaGujP_BrmK3gdQ3MgGZrMNUc4vQaguUqU1cyzHJY099GH2-E8Bb0rY-EDnqAE-laNV4IBnyLVm2h5Tvq_yUjqnv2GSHftXCPUiRdiDQe5jNdBV6EzIIVcxUrPphhd3gW7UbXdaN2NOYMcfrpfbEmmtIpH1kTLyzooCUTct6wYvBdCggIw-YJzA4STxuYekfa33dILXfmsGKy_yXwzgl7Ptq7dl4jQ6RSb_skqJnvn2Bl2Cnnthpb-l35zY1ZDA1KXTKw-Uiy3WI4sM8EEP1Z_0V0Ac-iL2f8VX31dI3Le4CbyhdD5Ko-qhR3cAyPGSxLmHqGeuXTWPKoPamSDh3qH_84-7ISTgDxym4RifCgIzxyTJYsjxs3kUyM9u7jE-CSRRVJlZMMZ9zYvDXgQc_ObnQvrvE4rS9X4P38W09FUDNKpSLKAs1M-l3zSLWMdtS89dBrUY97wvQ7yQXW847mPc1REFlb7LxauuVe7I9Ay-aIhr92C4uJ4Sc-Uf9mKieFklvfLKwap_bh8pZALQ8l71l7DZM8C3Fn6vqSnkfg429KG0PtEbevI18J8_cvxqoss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63c078ceee.mp4?token=tCpUQs-N5E7KT1CW3VXr-uZWHcE5kGH9bNygpmcl2BQjlVxLWaMmrjVGOyOPCw3HqFcQHht7B6vreaN0PYaFTfTve0YUuQQfhc544A6ehVaGujP_BrmK3gdQ3MgGZrMNUc4vQaguUqU1cyzHJY099GH2-E8Bb0rY-EDnqAE-laNV4IBnyLVm2h5Tvq_yUjqnv2GSHftXCPUiRdiDQe5jNdBV6EzIIVcxUrPphhd3gW7UbXdaN2NOYMcfrpfbEmmtIpH1kTLyzooCUTct6wYvBdCggIw-YJzA4STxuYekfa33dILXfmsGKy_yXwzgl7Ptq7dl4jQ6RSb_skqJnvn2Bl2Cnnthpb-l35zY1ZDA1KXTKw-Uiy3WI4sM8EEP1Z_0V0Ac-iL2f8VX31dI3Le4CbyhdD5Ko-qhR3cAyPGSxLmHqGeuXTWPKoPamSDh3qH_84-7ISTgDxym4RifCgIzxyTJYsjxs3kUyM9u7jE-CSRRVJlZMMZ9zYvDXgQc_ObnQvrvE4rS9X4P38W09FUDNKpSLKAs1M-l3zSLWMdtS89dBrUY97wvQ7yQXW847mPc1REFlb7LxauuVe7I9Ay-aIhr92C4uJ4Sc-Uf9mKieFklvfLKwap_bh8pZALQ8l71l7DZM8C3Fn6vqSnkfg429KG0PtEbevI18J8_cvxqoss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر مطهر رهبر شهید در نزدیکی وادی‌السلام و حرم حضرت امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448251" target="_blank">📅 11:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448249">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4d5e4c30.mp4?token=Z8d3JlFozLV_xVljpyJcGaJsoq0xqJSAMBK7lykOY6h_CGPUsrPrgfLi8F0R8HSC0QLXiwPVc8hrPsUCiEWe7J7dFwLiLhZdU0xwePWDOKNMTYVNZXp2ma2qh8CtXGNNNnu7t_PfqM5IPtDRvx1pA_IH0NvbBeTPu2pXI6Opin9rgVEeEfdfQzjcu5kXHKOs6aRfcm_vCulWlFiMIzcFzX5mPuHlbyjnzOlzA-jcrf0O_5sXZHlQvuCtUXZq71IhNLyqSjhHAIbWanQhDk9_vZLBQGNwUhldbE2-2w17xQ7R2GmcqwBc9fQAcloOjQOIKcHd4waGUAHxOo21QseF2hXkZqULHxi_qRbOgd5-Grnt1LNHRH99WH3zc1utUwLtn2EJdYdQiS8yq2llUgzLuVp40spHXn9spxlm9YWwZFozRmiDbcNqkfryTK4qAdtpqAubjr0Ap9esgoqqLZ8BEuSCr_GrMh9jk5tjnlHiDY7YzODcmUjqCIxxTvxVwQ2OTIbnLV7KTZmRoMfktopmmA_Z8mOqn_fsPCsrZAcF4krSrO02ji4nJaJuCLLGdUXO47SsMcPKJ7dssceLx18KszYwY6cKM5p07eP7I0Q104cy9potLcKp8bjEUl6Xt1rgysYr1PFlWFrAN-z-z7lDgESaFh4JvaXa2NnEkBAVNu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4d5e4c30.mp4?token=Z8d3JlFozLV_xVljpyJcGaJsoq0xqJSAMBK7lykOY6h_CGPUsrPrgfLi8F0R8HSC0QLXiwPVc8hrPsUCiEWe7J7dFwLiLhZdU0xwePWDOKNMTYVNZXp2ma2qh8CtXGNNNnu7t_PfqM5IPtDRvx1pA_IH0NvbBeTPu2pXI6Opin9rgVEeEfdfQzjcu5kXHKOs6aRfcm_vCulWlFiMIzcFzX5mPuHlbyjnzOlzA-jcrf0O_5sXZHlQvuCtUXZq71IhNLyqSjhHAIbWanQhDk9_vZLBQGNwUhldbE2-2w17xQ7R2GmcqwBc9fQAcloOjQOIKcHd4waGUAHxOo21QseF2hXkZqULHxi_qRbOgd5-Grnt1LNHRH99WH3zc1utUwLtn2EJdYdQiS8yq2llUgzLuVp40spHXn9spxlm9YWwZFozRmiDbcNqkfryTK4qAdtpqAubjr0Ap9esgoqqLZ8BEuSCr_GrMh9jk5tjnlHiDY7YzODcmUjqCIxxTvxVwQ2OTIbnLV7KTZmRoMfktopmmA_Z8mOqn_fsPCsrZAcF4krSrO02ji4nJaJuCLLGdUXO47SsMcPKJ7dssceLx18KszYwY6cKM5p07eP7I0Q104cy9potLcKp8bjEUl6Xt1rgysYr1PFlWFrAN-z-z7lDgESaFh4JvaXa2NnEkBAVNu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر قائد شهید امت میان سیل عراقی‌ها تشییع می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448249" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448245">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
پاسخ اولیۀ سپاه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
🔹
سپاه پاسداران: به دنبال حماسه‌سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی‌سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/448245" target="_blank">📅 11:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448244">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌ ۲ مقر نظامی در بوشهر مورد حملهٔ دشمن قرار گرفت
🔹
معاون امنیتی استاندار بوشهر: بامداد امروز یک مقر نظامی در شهرستان دشتی و یک مقر نظامی در حوالی شهر چغادک از توابع بوشهر مورد اصابت پرتابه‌های دشمن قرار گرفتند.
🔹
تاکنون گزارشی از شهادت و یا مجروحیت بر اثر…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448244" target="_blank">📅 11:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448243">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGLswwzln4f8MVZdnxpShc0LWfNT6qRIw3ZwrwL_hGxKhcCOWWQU_tEFq_-9zztttQdxgaxlNvF1PDm_YHtC7e_yTSGQk8a9gW3zPRw8882qRp2cIpv7qI9ly3Y306RoxTTiFLbEhqLiHEaT0A5L42VbUqExNtWypp9YxP4xhPPD62YT6maEAWOB7Vqa9aaoRxFtBiRDq_v9fvXJcCSwvFFQ7cBZXsuzMC0uLhC4aHUsKs-3pwdP8eolHa8FruqrltzSHlJ9LiT05jQX8opMuuKiwyvTLkRXb1S5BK3E6W9ulvshktljuizTPNdylY3eOUIVJERPE5UN8YamM-ypSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قاب ماندگار از تشییع باشکوه پیکر مطهر امام مجاهد شهید در نجف
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448243" target="_blank">📅 11:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448242">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43cab6ff92.mp4?token=DGKo_X1r2JoXAJxn-4ZmtQ-9zTRkqakWxiBAyaGSaiOlpK6I1YtKOlcvnfqQeMU1JLRLXE91zkukN5O8OMSscqmiG6b7QSQBtfeSJ3PZmHs8Gz69f_x5-wqtW1Bbxpu-FmxBab_1jArRxTswlAEePnuS-OI1Ptxg3blF_3VLXtIkDILPzFDEi5hHFpZZ9AQ2IPf-ey87-HpKjMG_m65vFSAt72-D2jTqrAEs7omNQzQBc1bXeqPSlUmWlir_9XByE8AWPI7TUpa1zRA8wK0x6NWyFygLk2rXZDNE3X2tzRLl6gAjmDT3cfHFF5BiF_vtOJhKH1WD-RpdE0DrpgVFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43cab6ff92.mp4?token=DGKo_X1r2JoXAJxn-4ZmtQ-9zTRkqakWxiBAyaGSaiOlpK6I1YtKOlcvnfqQeMU1JLRLXE91zkukN5O8OMSscqmiG6b7QSQBtfeSJ3PZmHs8Gz69f_x5-wqtW1Bbxpu-FmxBab_1jArRxTswlAEePnuS-OI1Ptxg3blF_3VLXtIkDILPzFDEi5hHFpZZ9AQ2IPf-ey87-HpKjMG_m65vFSAt72-D2jTqrAEs7omNQzQBc1bXeqPSlUmWlir_9XByE8AWPI7TUpa1zRA8wK0x6NWyFygLk2rXZDNE3X2tzRLl6gAjmDT3cfHFF5BiF_vtOJhKH1WD-RpdE0DrpgVFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
| شهید زهرا حدادعادل، همسر رهبر معظم انقلاب:
من سال‌هاست که آرزوی زیارت امام حسین(ع) را دارم
▪️
امروز کربلا میزبان امام شهید و شهدای خانواده ایشان است.
@rahabri_plus</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448242" target="_blank">📅 11:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448241">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJD50gdhk3MwA7vupgWYjkxWN5WKGFb29netAxsQrex69BtQv0G5pkpxyt5qxcZbw6oq6Y1WHvZXRIXGjWwW_1kzkF1ITDHgxb1E0y6KfKoSY2Dlay5Ntp44uIwyNC3_uc_DbHvLbHV452mM1to6CL_I5YeJCA0SPPXYHMrJyzOtISh_kXYvsDlnKuES4M4PeDwyhTmzVKbnufuT1cSayTSw_wpPfRf2eVSBM8LKTiyV9OFgf7lZRyGqlGMjuddTRIZLce3Vyi_n7UQbKWg-fYxYS9NFR4CbtJjEUWowAZLNzILEX9AwOQdIAbwxPLLqtLNx_RWQ3Arb3G6_KNknmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس نوهٔ رهبر شهید انقلاب بر دستان عزاداران عراقی
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448241" target="_blank">📅 11:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448240">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bdd01c45.mp4?token=ESfIC5nc53QEcxibry4Cl16RHkQNJcv6ZXHw2FoSkT8BKJbi_dIPPUNaET7CHjdfW4xOkGPlAFomAIQJ7JVNwsSrqWkKX3DeBw_mG9fRdYspfNFaSb-q4qs9yLdjS5wC8utG7s6KHFqYTwOfn3UndhrcwtI6W-L4XZV0FQ02-ygWH8X6ZHe3tpsHDrKajOY7_QV7QRk-zfsg2et4vq1zb_tUgTZ0rYOYzhopR2Ov5kycbVTAW2-XTrZJIyUKHrv6zrRK7KRoE-i2CW4OWwZyv-ywYxEqlQPUPlwmGXBtMDjLm8ozjhAGwYwzOXMzOag77q-ArMts3h5M7Sk-_5qJWpe8juIdAm-zSfHvbGrE4RbOeIxFcgwb2vPP2vBjP9fZOuSv4pT8EnEFvClqKroAOTJeuWpAkkRFbotSAbPUbNKCROO85jN6W0BihU1_WgV-RvQui6FsNTSxPHkg94lQ2aqh9vIJJPwVyBEFyildemZuQOPqb5Dkm7Y9GUeD-oScWkFTGJk7FhYyPhSHLx7jJGCHzzep_X-_IUFZghFjFRc7Gp3bJHtH6aM8o0X0yQCae1ylQMS0U3kV0cZ7aDq92nxoiLJzVcGAFSMdzaOe7ac6qjAzPX9T0zwuXfSuh6dMimtLi719jhCaT1illiAO54JY6Ws81cpbf9xZBTUy05Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bdd01c45.mp4?token=ESfIC5nc53QEcxibry4Cl16RHkQNJcv6ZXHw2FoSkT8BKJbi_dIPPUNaET7CHjdfW4xOkGPlAFomAIQJ7JVNwsSrqWkKX3DeBw_mG9fRdYspfNFaSb-q4qs9yLdjS5wC8utG7s6KHFqYTwOfn3UndhrcwtI6W-L4XZV0FQ02-ygWH8X6ZHe3tpsHDrKajOY7_QV7QRk-zfsg2et4vq1zb_tUgTZ0rYOYzhopR2Ov5kycbVTAW2-XTrZJIyUKHrv6zrRK7KRoE-i2CW4OWwZyv-ywYxEqlQPUPlwmGXBtMDjLm8ozjhAGwYwzOXMzOag77q-ArMts3h5M7Sk-_5qJWpe8juIdAm-zSfHvbGrE4RbOeIxFcgwb2vPP2vBjP9fZOuSv4pT8EnEFvClqKroAOTJeuWpAkkRFbotSAbPUbNKCROO85jN6W0BihU1_WgV-RvQui6FsNTSxPHkg94lQ2aqh9vIJJPwVyBEFyildemZuQOPqb5Dkm7Y9GUeD-oScWkFTGJk7FhYyPhSHLx7jJGCHzzep_X-_IUFZghFjFRc7Gp3bJHtH6aM8o0X0yQCae1ylQMS0U3kV0cZ7aDq92nxoiLJzVcGAFSMdzaOe7ac6qjAzPX9T0zwuXfSuh6dMimtLi719jhCaT1illiAO54JY6Ws81cpbf9xZBTUy05Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ ورود آیت‌الله سیدمصطفی خامنه‌ای فرزند ارشد رهبر شهید ایران به حرم مطهر امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448240" target="_blank">📅 11:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448239">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af855b823.mp4?token=ogvzG3Wd67fO9zZpOnYX5-UNXCwF2vWHZRPuQUWrM2LwAu1iti08vXb2s9w1XPvOLbnjczY-pofhSiCSSAZyBBo_2MLgKVYXh-vB9Zf0YR3E0GA3YJ9YbsPhWJ0ZCLoFian--28n4t98a6-DBy3I-AG_pYgPDgTeQ9UPGRmhlnWADXrXFH5xm7QeB2Z54CUWgrQ20toYsb6QQZA3fVDt8NsZAEiupmON45goqWXV6WckQgWayMKT1YvaJoCgiDDjHzPQe_0ooeAKPm5I44EGi1ASXs4SpFc1F8s4XwVBUKIscvmSvn_Pk9AgMqN7PjL849r79gG4qY7dKB5iqGD6ICMKfCQcGrKOaRJVjAnq2-sAPSd7mmwqNW1YzlxUj25maV-FbvQ_hkkz5VPKPPsZ1bW7yMDk7pdY4wxrXwUuJXByf0vcQ4KBEsaFxnSTOOP5YgzyfBgfNC-vzMU7PnAXIGxAmsa0eypJDtimo-OTYTXQsApsS0WRt81z4GOc2J9SlrKuaTy7pIDnHV_FFqk85mx-Vry8izf2ShYxYoEbsLc4PrOW_V2FlgU4Wt8gw2j8OoU94G_M-Bppu4S5z13iZ7PhTBDJXH3XfP66dRB9fB2rjMePhzUnwv1izFWdBHN3N1iR_CPhk_gkammIk_MYJZKiAfrPgwLi-9_3BYXtyrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af855b823.mp4?token=ogvzG3Wd67fO9zZpOnYX5-UNXCwF2vWHZRPuQUWrM2LwAu1iti08vXb2s9w1XPvOLbnjczY-pofhSiCSSAZyBBo_2MLgKVYXh-vB9Zf0YR3E0GA3YJ9YbsPhWJ0ZCLoFian--28n4t98a6-DBy3I-AG_pYgPDgTeQ9UPGRmhlnWADXrXFH5xm7QeB2Z54CUWgrQ20toYsb6QQZA3fVDt8NsZAEiupmON45goqWXV6WckQgWayMKT1YvaJoCgiDDjHzPQe_0ooeAKPm5I44EGi1ASXs4SpFc1F8s4XwVBUKIscvmSvn_Pk9AgMqN7PjL849r79gG4qY7dKB5iqGD6ICMKfCQcGrKOaRJVjAnq2-sAPSd7mmwqNW1YzlxUj25maV-FbvQ_hkkz5VPKPPsZ1bW7yMDk7pdY4wxrXwUuJXByf0vcQ4KBEsaFxnSTOOP5YgzyfBgfNC-vzMU7PnAXIGxAmsa0eypJDtimo-OTYTXQsApsS0WRt81z4GOc2J9SlrKuaTy7pIDnHV_FFqk85mx-Vry8izf2ShYxYoEbsLc4PrOW_V2FlgU4Wt8gw2j8OoU94G_M-Bppu4S5z13iZ7PhTBDJXH3XfP66dRB9fB2rjMePhzUnwv1izFWdBHN3N1iR_CPhk_gkammIk_MYJZKiAfrPgwLi-9_3BYXtyrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری از حضور باشکوه عراقی‌ها در تشییع قائد شهید امت  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448239" target="_blank">📅 10:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448238">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مرقد رهبر شهید با نظر رهبری معظم در مسیر زیارت زائران خواهد بود
🔹
تولیت آستان قدس رضوی: در بررسی مکان‌های احتمالی دفن پیکر مطهر رهبر شهید انقلاب در حرم مطهر رضوی، ما مکان‌های مختلفی را شناسایی کردیم و از هرکدام، همراه با خصوصیات، جهات ایجابی و سلبی از رواق‌ها و فضا‌های حرم مطهر تهیه نمودیم و برای رهبر معظم انقلاب ارسال شد.
🔹
ما پیشنهاد داده بودیم که فضایی مشابه مرقد مرحوم شیخ بهایی در نظر گرفته شود که به‌تدریج ماندگار گردد و بانوان و آقایان بتوانند در آنجا حضور یابند، قرآن تلاوت کنند و مرقد رهبر شهید را زیارت نمایند؛ اما ایشان موافقت نفرمودند.
🔹
رهبر معظم انقلاب فرمودند که مرقد شریف رهبر شهید انقلاب را در مسیر زیارت قرار دهید تا زائران در مسیر تشرف برای ایشان ذکر دعا و فاتحه داشته باشند.
🔹
امام شهید متعلق به همه ملت و نسل‌های آینده است؛ از این رو نظرات و پیشنهادات گوناگونی از سوی اقشار مختلف دریافت و بدون هیچ استثنایی همه را منتقل کرده‎ایم؛ و هر جا که تعیین شود، تدفین پیکر رهبر شهید با آمادگی تمام انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448238" target="_blank">📅 10:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448237">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک فروند پهپاد MQ9 در آسمان خورموج ساقط شد
🔹
سخنگوی سپاه پاسداران انقلاب اسلامی: در پی تجاوز هوایی ارتش تروریستی آمریکا در سحرگاه امروز، یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند هوایی سپاه پاسداران انقلاب اسلامی در آسمان خورموج استان بوشهر، مورد اصابت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448237" target="_blank">📅 10:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448230">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6nofXHxhwBndvrRyjjTuQYSbWtNGoQ-SdRD2ydzQ-LhS5DeFonIxxf4tU24tqG7v8dWvy8Gc_TwLKqjSTB1Pvq1VCGSw75ctO0RF5kDuDezItUZoELtxXi2dC2vqPW6GA9EV-azGIRJMWTngR1kx-DEFCT4Q6QktXDb6dZMJ6iUqukv_NpbMKtTSvRW_eh3v0XQP1QzdDiLnS8-ISP_2rnV1GciMc_Qnyoa9fWFsSgpdM2n4pmK6porI8P6diEY4q2K9CsKvZVURGIMdbAyyiyhPb4VoDC26TQjJPRLmtALHN0rQIdGo2zgSFJ9wxVikBMMd21qHz2djcLBuAPBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfmW_9m2kzu8wwyhoKXaGAR4gedbG7SXhDZPlPyAUASLyhF8Toib4zy9oCgFAGTA5iHJ_slB59VqrY0KE_bobiiJu6vK_GalP3WJlfzezGfF2q3jykWUKft0dQQKdgER5RXOeC_EPSDFqXZxaOssnsdn0w9GEIfu6Jy8jEk4PE1VbfVrDPoUKfmidUeVqPPjaC9_jnisXIvSmnWmavn8WTLLebITTqEBo5Ht3zwewiBceVoSarHBh4MLe0WQPM8dWMJYy5UwjarIkhNRcR0A1Fuk-Rn2HDJbF_eKkp3uWWXkT0MD83jvXnNqChSjh02h80gNmKa8cDcKQniDlC1E7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8Z_9bUFeGVT03J1x2pY-EBRPL1hwdut3hULHMc5WN5O5fO54ldLd90RCgpWH9IYgSyZiUfyG38QW5kthRpv8jxbC85uSEiOcRlqaBJpROEU-p4exUfhoeolyTBwSfCOy_SIrkv2d1a2WDNnf1B885jIE4i2Mt5feUzFSp5pMqA79UZ00P8aaxwP7bn4cSQhbCB-fR5SqHRMHaJ29KPjlRN3O2m5Rxt2aLIUhZ1XoyDT0-Dsly_YUq4YIkU3jObRPUInspVKKwiPaUWVNj1cRu4iWH0tRB_XE86daI61Jqfn5Lko_3emM4TsrCdZIgnwlAj0tJnksmMfeuhJSzOYRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpvX5RD7jn_9WsovtFl53Xf3g2Sx6gEMbxBrA4g8iReKDElD44Q6QVlpkf9eY7B3UTQpItx4vH0CZHt_Ew5N3whSn2yhGZ4vsmUVdgtae--dMkMkTgYBYxQzimqVNKX_D9DFYrWFZT9rctA_v0SSVMqKmDfE3ef8uQS2DUzinlUCVqpKOfDuYcQ09hSFbAe5D-OQvDkeRuXhJt_NotQG2drs4bw98Bhf-xaoH_FPq_6bMkyog5S_is5tjyK1hyCfbSx3ZUk2n35f3ICCRdVk1LHCN_FVK70qgOA5MIOvH6E5hHvJ2RybaP48cdb5cbPN-iM8I75No7A07uYbrUc27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7C-muo-0L5H9JxGntVrwr8TGC505CmDWIQcKdOdMxTP5Sl9vNT9T6MPSwoLSzp-dg9_DLil8_gfhC06EHIi_nv9vXmGIVhlznRAEn5dKvY4iJ15OflFTNhj96758rzJv9sVnK6DUnLzthrpjl0A_Lub9kmgmaVAbcJCJYhvoRhnebP9jMPW42bzjuc6MqGVT0sRenQMu_Cf_NWGgzLMPLq5FCASUWA--RHMglf3Uf_30pyFN54Wcx8s-pT2WzsluVL0isu0O0dSO2FmvCySsA0VEhOBN2sjc7Nc9VqR4tk1ecZiqS_KrG07NMGgF7c1ChsAfhMv5vea2WLVpuhhqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_RQBqwKXaCrlLiAmxB9OtEActeijITWyeWRvPy_4QuWVtGdayaeo5Ooa-ImLrDUKG4tZbFKKCCjcH5DqI-YzHG_r-0Ji-wUiG8Y7HgeDOYfJK20pQJHNT5agZxDMvP31KBbFS4y5CcWSv7uuleppx-IKOuDIlre5ENldo_xuuNZdqr2cf0774ANspaKXP8NA3-4nTl2zLIDQAdMaCFN94qORbU0pQJgTSjTRZixAHVBrVgJ0bSFObN18O5ux38EWhptqVCwBvpZfj1lMiHSmKNTjjx5lU7Nj-t2FbzgWW2-Lf8qWbdhNoXruTkmti0FqAOdCsTTsitgF0Sxnue7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7PoS69lEMnn0U81PP5LlN-EvWI34xIHcUkFO6V8xk9aJddvaAJMvDr0b-cJUV6OO1ocv2bDf9CFP7r7t7XIKXKqcdv44-wXiwA4uo9ZeYWhriFfAjCAPT1DuuGwJlqOtl9vctFmN5V-tg3GWQHhxsVj7tCgHm7_sOKKsYAxAGpqKZm22URcvHKatbmBybf_d3U2iemR3cUIb9ADwb2Lnv9lUi3vjh31YSX75V2YriYZEsEJQCNQkqBIjlU7kcckhjPFhwdrOxLK4SOEqsi339BYxwHrPh-Z1zdp0T5Uz85gzUWIjPAHxsVBbduGdIPLatS_5muQXXO6PxyFvFsGzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حضور باشکوه عراقی‌ها در تشییع قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448230" target="_blank">📅 10:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448229">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6df936eea.mp4?token=mgu0jspV438B9eqMAmHBQOnHxq3az1q9v_ZWUX5qZwrOlHp8a30d9SpY-pxUIhmdRJIJuefpdDH-4X-F7u4lTz4oEDi-HURJ1WDKc90qq_RkRht2s-iH__TGuuJMnmcsM594c29J1arJ1AWT_QCImhzLCjB7kVDlO0Z6pr6NXpak2VQtiibp5Cz_zV7Fhz2V0PXspyByBSXmgJ0tPV3PC3GKo0P_DUT9AZDRx7bRb4M4pyyWQf0NjE0twflEKSrgxn0s8JPdGGFcS8cKvvtpWt2uJx3D3wnkEwtsZbiX_1PwMdSFVDBRzbXoTmOWrZzHOFOREFDRP5VkN9meuZ22EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6df936eea.mp4?token=mgu0jspV438B9eqMAmHBQOnHxq3az1q9v_ZWUX5qZwrOlHp8a30d9SpY-pxUIhmdRJIJuefpdDH-4X-F7u4lTz4oEDi-HURJ1WDKc90qq_RkRht2s-iH__TGuuJMnmcsM594c29J1arJ1AWT_QCImhzLCjB7kVDlO0Z6pr6NXpak2VQtiibp5Cz_zV7Fhz2V0PXspyByBSXmgJ0tPV3PC3GKo0P_DUT9AZDRx7bRb4M4pyyWQf0NjE0twflEKSrgxn0s8JPdGGFcS8cKvvtpWt2uJx3D3wnkEwtsZbiX_1PwMdSFVDBRzbXoTmOWrZzHOFOREFDRP5VkN9meuZ22EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مهمان خارجیِ تشییع: اتفاقاتی که در ایران دیدم شوکه‌کننده بود
🔹
یک خبرنگار پاکستانی که برای نخستین‌بار با هدف شرکت در مراسم تشییع رهبر شهید به ایران سفر کرده، می‌گوید که «تصویر ایران در رسانه‌های غربی با آنچه به‌چشم خود دیده، بسیار متفاوت بوده است».
🔹
او دربارهٔ تجربهٔ خود در مواجهه با مردم و فضای اجتماعی ایران گفت: واقعیتی که من می‌بینم، کاملاً مرا شوکه کرده؛ وقتی ایران را دیدم، متوجه شدم آن روایت غربی که می‌گوید «مردم هیچ علاقه‌ای به حکومتشان ندارند و حکومت به مردم ظلم می‌کند» اصلا به این شکل نبوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448229" target="_blank">📅 10:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448228">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYh2BBMUKSbfOD3GhNbEF2pNR7P-Kq9oqgYLPYZ-Ed_F8tnw_wOYOj4xPTza9ngQVzRpCSRwWhgO97zdhtQp0dqiTjO1Aw_QAXRw-Q2VGjpEkBFtNBpicYPkQT4IpQ6_-aT4MjhvaHqBvM3zX7g8srPlACG-EO5EuVc2xSSzMGo6unXAxiQ9MDHeS1zdZQpdjBjmlIpJs_KRJg_o-9j0FouNsbR7j6LPT9PcuVBu1OX9X4yNkMKsSN-LElYygozA3V0oGIKpn0hbDVWviAXT1G0TIuqoeYAs_NfjD6E9ZnozYPD7I-Gu118KAf-OpEnVOfEBWelRTcb1y6oMYxNVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سیل زائران قائد شهید امت در میدان ثورةالعشرین نجف
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448228" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448227">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae5e4f5711.mp4?token=PE7TbfHI7s7xsU20F2H9DHRfECv7sgmun8R6lALh4ilFHEiD4_8EfbnKDeCpgA6NYmpIBK2vzCxjgBv7h-4TM8nPCW4NgRTypISqfh71wyXcWjX19O4rg9xDa7m87o9clZnW-7pU22AvW-Lm1Cie4V5U0pX2M_VHl5NfLxVv9_9ip3_tuMde7mhDCzqndcmIIMqj46zoBiEMLcoGBzMuOl9O0OXYl75vsSDlzDIKIIDH8wlF2v8THloLBKLrFfyTsjNbbLmfJUCkNO7t0FjLkCacNQ9ZEVFq89j0TfLb124CANmGGPzXhaR9oaIn_zHWsrPOvTBSTGY1MQg9bf3HeAePAGVeyQK7JYbgiDA6QDo-kJNg66PEd_xIZ9-ilI1P2Foh_6rmthVXWgR04gEN3MI1douXjK57VUdLa2L0minn6_K4gop0mRQXoJ21Ab6rFHAAmUAn1_DFJknsWFa7jvotpiCkjgcXNE4dA2bmagH9H4sa_GVx-x_r-LNKG2ikgfxxzEBNbhnhweNbjDcOgsFivCK1a3_pekyVPznjkarwwXV9pfNfeypM5f6DSJ8gpsyqW3I8kZ3UVoJ9LqZ4Pci0fZxzcmMt_JSCQ4_OOaC0_Nsddal3G6gzGHqhMaxVbQJHXhmP4kQzilKb8xzB4AUlTZWFbXlfyNesUARbE0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae5e4f5711.mp4?token=PE7TbfHI7s7xsU20F2H9DHRfECv7sgmun8R6lALh4ilFHEiD4_8EfbnKDeCpgA6NYmpIBK2vzCxjgBv7h-4TM8nPCW4NgRTypISqfh71wyXcWjX19O4rg9xDa7m87o9clZnW-7pU22AvW-Lm1Cie4V5U0pX2M_VHl5NfLxVv9_9ip3_tuMde7mhDCzqndcmIIMqj46zoBiEMLcoGBzMuOl9O0OXYl75vsSDlzDIKIIDH8wlF2v8THloLBKLrFfyTsjNbbLmfJUCkNO7t0FjLkCacNQ9ZEVFq89j0TfLb124CANmGGPzXhaR9oaIn_zHWsrPOvTBSTGY1MQg9bf3HeAePAGVeyQK7JYbgiDA6QDo-kJNg66PEd_xIZ9-ilI1P2Foh_6rmthVXWgR04gEN3MI1douXjK57VUdLa2L0minn6_K4gop0mRQXoJ21Ab6rFHAAmUAn1_DFJknsWFa7jvotpiCkjgcXNE4dA2bmagH9H4sa_GVx-x_r-LNKG2ikgfxxzEBNbhnhweNbjDcOgsFivCK1a3_pekyVPznjkarwwXV9pfNfeypM5f6DSJ8gpsyqW3I8kZ3UVoJ9LqZ4Pci0fZxzcmMt_JSCQ4_OOaC0_Nsddal3G6gzGHqhMaxVbQJHXhmP4kQzilKb8xzB4AUlTZWFbXlfyNesUARbE0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چفیه‌های عراقی‌ها به پیکر رهبر شهید متبرک می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/448227" target="_blank">📅 10:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448226">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d703c4cfab.mp4?token=FGEJM6lliGbupW7avvpr-Sl0_6bNI6h-Idoe92r-Ay3BeTvBG1udYsSOBRGCij0Z8IVNF3wYCtoCPXKbk41ZHnEi2MWmycG8oK-C1KUh3xe4A6d6cexgw0Gz_QEnwfTnw7oG5B4mkVvtxJ6ZnxzLkbUqC3E7dbcEZ1PRwhIjNYagCU01CB1uh_7ucooaR1pAlbym3oX_jIdF0833h5gQMOW3pBJXhikyFbFFdmsTi9a-ibQHLqo4IsBIYIj67DXLgd3_RfPFMIdwQLmk-5z17jtgDSJKGr34RrsUlcGYMm6xPIE73-jtxcrBT2Y3RHK2T0uizqp2fNBKv91Y3QmkjgOrzqH85jl5EKNpmw6RtWdSajO5COTUbKAIOiwzZCJAOEMczuqnlHSxM6AjhDhKD5qdwu6tVDHGtRLsSVAInRbIfslONg_kYktrxykH4Xwz2_6QgKJikP2lLW08duTiFh3DzB-YnKhtdhNztJeGZ1-qd0JPJV04J9aaABsgYzIUMsH7XYoJFn_F6rVfqDTnF5PEyacFRwnE0qlOfURHBX15G5k0NOPod1AyN5tAjWrl2immnZ4umzdPpbRZgo0gmlnhkbtgN3aNRaHEcbwROyd_BrWT8ML7aAsdag0woYMhSzIk2oKHD1DiS9HLboXvCM9YSH6IiRgz2vo5aiwKMqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d703c4cfab.mp4?token=FGEJM6lliGbupW7avvpr-Sl0_6bNI6h-Idoe92r-Ay3BeTvBG1udYsSOBRGCij0Z8IVNF3wYCtoCPXKbk41ZHnEi2MWmycG8oK-C1KUh3xe4A6d6cexgw0Gz_QEnwfTnw7oG5B4mkVvtxJ6ZnxzLkbUqC3E7dbcEZ1PRwhIjNYagCU01CB1uh_7ucooaR1pAlbym3oX_jIdF0833h5gQMOW3pBJXhikyFbFFdmsTi9a-ibQHLqo4IsBIYIj67DXLgd3_RfPFMIdwQLmk-5z17jtgDSJKGr34RrsUlcGYMm6xPIE73-jtxcrBT2Y3RHK2T0uizqp2fNBKv91Y3QmkjgOrzqH85jl5EKNpmw6RtWdSajO5COTUbKAIOiwzZCJAOEMczuqnlHSxM6AjhDhKD5qdwu6tVDHGtRLsSVAInRbIfslONg_kYktrxykH4Xwz2_6QgKJikP2lLW08duTiFh3DzB-YnKhtdhNztJeGZ1-qd0JPJV04J9aaABsgYzIUMsH7XYoJFn_F6rVfqDTnF5PEyacFRwnE0qlOfURHBX15G5k0NOPod1AyN5tAjWrl2immnZ4umzdPpbRZgo0gmlnhkbtgN3aNRaHEcbwROyd_BrWT8ML7aAsdag0woYMhSzIk2oKHD1DiS9HLboXvCM9YSH6IiRgz2vo5aiwKMqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلم کوتاه روایت دست
از مشهد تا مشهد؛
مروری کوتاه بر سال‌ها مجاهدت رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448226" target="_blank">📅 10:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448225">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⬅️
موکب بانک شهر در مراسم بدرقه پیکر مطهر رهبر شهید در مصلی تهران</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448225" target="_blank">📅 10:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448224">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448224" target="_blank">📅 10:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448223">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb5206ff4.mp4?token=WgoMso0CdTV-oUZdI2bpf2A78IxhurME0xsc701lPxemYL5-H98CfG-g3yqyLl2-sLwoKRKzX5Droi9TOM_0VLSRYAWwG_KBIYJqVgO6op_lVee2NwoHGO6VzU-w42sgmCm02_6RciKMUC7UfOXdORoDxcdfzDcwkV39G3qfF_eDxflsIjcyQSs1neaNCzZ14tG6Jo7ywGQ5bBV3b-qjquF0_yd-7D7umjksTl_NopgFK8m_fUYdLn-7WJPkxDmL0pDpZ7WyX9FGWVyUSuqc9K9vIYAqMpcFBbiRO_0Vjoh-vm_3LVTyrZHuLIvccofQjMiaHKHw14yHulXz1o-oOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb5206ff4.mp4?token=WgoMso0CdTV-oUZdI2bpf2A78IxhurME0xsc701lPxemYL5-H98CfG-g3yqyLl2-sLwoKRKzX5Droi9TOM_0VLSRYAWwG_KBIYJqVgO6op_lVee2NwoHGO6VzU-w42sgmCm02_6RciKMUC7UfOXdORoDxcdfzDcwkV39G3qfF_eDxflsIjcyQSs1neaNCzZ14tG6Jo7ywGQ5bBV3b-qjquF0_yd-7D7umjksTl_NopgFK8m_fUYdLn-7WJPkxDmL0pDpZ7WyX9FGWVyUSuqc9K9vIYAqMpcFBbiRO_0Vjoh-vm_3LVTyrZHuLIvccofQjMiaHKHw14yHulXz1o-oOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر مطهر رهبر شهید انقلاب به میدان ثورةالعشرین نجف رسید
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448223" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448222">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31db43fc9f.mp4?token=jZd3NJ620FRGUA7J59Nhb6Ix3syZvJGvqypQcFpDY_lTfocruRDIY8xYxLt7aZcOtAUPHQPJkES1uOZWcwUGW20KbbtqPriLv4B6zQSoRjtAK7hw-_UqgebCafKakjXBWwz-H1PNOprJ-f0-esBtKZUfDJ3lcCj2TTLoePc6tcP4qfgHZq7neyEhwN_vXE67z03iY7JjtjQ3gPXfA6DLMTQjWgXzr3Oy8RwDtQVLhpHjKXp-Jjasf9OEEEnKMM6L8n003RCaWBZGIhaaQdAs28cbZx1AACFPX6pIulaZyKqapfzZS343pVQ70wUN67f-eRVXczhCMBXLThYs5Wfjcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31db43fc9f.mp4?token=jZd3NJ620FRGUA7J59Nhb6Ix3syZvJGvqypQcFpDY_lTfocruRDIY8xYxLt7aZcOtAUPHQPJkES1uOZWcwUGW20KbbtqPriLv4B6zQSoRjtAK7hw-_UqgebCafKakjXBWwz-H1PNOprJ-f0-esBtKZUfDJ3lcCj2TTLoePc6tcP4qfgHZq7neyEhwN_vXE67z03iY7JjtjQ3gPXfA6DLMTQjWgXzr3Oy8RwDtQVLhpHjKXp-Jjasf9OEEEnKMM6L8n003RCaWBZGIhaaQdAs28cbZx1AACFPX6pIulaZyKqapfzZS343pVQ70wUN67f-eRVXczhCMBXLThYs5Wfjcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابراز ارادت مردم عراق به رهبر شهید
انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448222" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448221">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVBJch7JUaCXuoDEkpEW4XJ4BJx6Ce2zjnuxGs-KVvL7lVGTqmTPb_K6Ty_g-7Znpz5UoBhbdAHTJI6oAJz_EwGLrBX1Yc-Xq5r-VlacjrKbdjZqm7AksOZPOZEinSsjTVkiZAfP7m-8Cbdzwu-BHQggBAg-ciOwgpDs5Tr78jmH97s8TFSBiVhWui5oO-URv76qhu7HIIE803_oHO3H5kp2m9eXyGyZlMRjbwwORQFliSsT4zVi2fdT293hEIpGKqZ79-7q6H8ToY6iAf1GsohLnP0yriAuq5Kh4V5UUzAFTaBuP4m77EtvSYwzYNatzX19Q36NUgdLb-WGpH-Aog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه: نیروهای مسلح در دفاع از حاکمیت ملی ایران دریغ نمی‌کنند و مبدأ تجاوز را هدف قرار خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/448221" target="_blank">📅 10:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448220">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an-h9gT3h3axtfXYkyUH-1DFlU4dtrJFwNIO-fNcyN5lgaNDBVdf8aoWii_Q3AxqFrZ7chTHROfA77DpnAp67ayRaK4aEqNzoUqS62Lek9f_6NfdfQUuxNBiUcoRIiakTe1FTpUS4jGuTx4NA114yBV6M70rag_B2K-AJ98YFS-3vwiIExSJ_n6VryRiAjrKKB18GEY_DKyAUl9RWLbpqbURCj1gAEno_jYntgqVRFppDOYUCkmIyiJm1Z-fhGiixMc4_GT0XlDs9NR4pna0U6hTQylC_gbMlyLmaGD8-fP60eNPBKMn9Rj0C3P_2LXmpfj_JQtrIJab-yvqSrp1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پدر و دختر به زیارت حضرت عباس(ع) رفتند
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448220" target="_blank">📅 10:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448219">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/560f9383fa.mp4?token=t8b-x62XztWqCdqJ8S7C9pHmAymXcejMRW_ogVN2XwK-rA7MuVsRjKgSf8XCL9GeX_uLWYulCSFCXOjI6Y4BLoZe9ko6G0e9jfY_Rt7dxYg0Upgff6j3pws5g6POZxFruQy5uQgsXzwyD3yHm3gyKxBWt7S0tH13LsAl6Gx74IP9b_D352oFM1O5OGTobXX4GODqkf1jK_y-rzqMHXLRaSYq0EQiVkE8HgRtJxlIDQ8RnOq6CNs3JaaWBgnxKNNLHaXCN2w2xWI61ad1hLDUrw_3jrb63qQHkgrea22MAJ9oEo5HJ6UEIOShpwtZ6G0guGGY7ljY4fr5dYUFTlBVJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/560f9383fa.mp4?token=t8b-x62XztWqCdqJ8S7C9pHmAymXcejMRW_ogVN2XwK-rA7MuVsRjKgSf8XCL9GeX_uLWYulCSFCXOjI6Y4BLoZe9ko6G0e9jfY_Rt7dxYg0Upgff6j3pws5g6POZxFruQy5uQgsXzwyD3yHm3gyKxBWt7S0tH13LsAl6Gx74IP9b_D352oFM1O5OGTobXX4GODqkf1jK_y-rzqMHXLRaSYq0EQiVkE8HgRtJxlIDQ8RnOq6CNs3JaaWBgnxKNNLHaXCN2w2xWI61ad1hLDUrw_3jrb63qQHkgrea22MAJ9oEo5HJ6UEIOShpwtZ6G0guGGY7ljY4fr5dYUFTlBVJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم حضرت عباس(ع) همزمان با حضور شهدای خانواده رهبر شهید انقلاب در این حرم مطهر
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448219" target="_blank">📅 10:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448218">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
قاب‌هایی از تشییع و اقامهٔ نماز بر پیکرهای شهدای خانوادۀ آقای شهید ایران در حرم امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448218" target="_blank">📅 09:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448214">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DG7uj_sP4LiugJGsy3M1dji_lMImxxDuC9bWlAzp8dFPPtTJ8FyED16jpfqLh-97JFQXJac8Ix1yPBNzyFyoYAWVKoznmtkIhCKoQDnhCtkrK3YFsswc3UxsBo0eHIjculbuL3DscMZ88BpIx5bHJJh3NOCFysyFJkXH97HSI8w1Xzv99yHZ6MO9lEs6keIc7Azc4eqodAe8KS2gfe2bp5tB3bzwqGphlhv1uYUQ1Hs4uZjnSKQ5a4o7dBMOUauRfJxeoy6VVwuxd9O-7YU88kniBetL09Ib9O1HIbF1sSvdfJY4j3nbAjsG9KSz5bXxYcsVbP_f0hEbbPWji2cSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KER2a6CahIv-T1Cyg6efM7OuOTcFiawCLNlJNwTjgs9xUKn_CGEpHCpL57aKCpv9uXul7THeRuYT0AlfLf_4TGHxHzdvZaniaWKEvvDuqTTYSZfqBZ4VLWDnMq84DICzzE8QmK1FjTRlWtbSb-VcOknuiWTJb_xpMUQrwaze0qzi_gX9n5CCX11vf00brVW0c61Xn5hGncemwx89SPjIyjQWWLHmr0PG5teKmbX8KWlv-cuPU3hRHm7iSEfcyKy3HoFvwKZOnjp_U2bvFO5vmNqRaMUoxS8GeAqkHQxeaEfEX2vUhPlIfREwgTgQRaM4bRTdAEGhrT50f0X5Qfpddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZsSyn0gcmrLw3rFtLVU_43qtrrpu7sL2I_c0CNuBrglvN76tA66h6HUoPr4NXkl3WL4j7XPxdOZ3C7Xt-D5Eu0rTqwFUndcwe2zwqVdOpFPPBap7MwbD3vScwXndqaamFihK4zhWjAJn4uZm-bpcIkJ60QLDl-NmgcR3m4JlSTtf8jnLCDoUKVGL7NIRINGmH3bIyMdWnIrqm6SSmAuhe1AQ0L3nP5mJ-Eje_Zkd4xlfLjuHWti9btyOmgLu9tpH2U52VQQb9ggRPdcjdNQ07zh9LmNbWwp_4v2pu_99a5EadtZa9NKUtTwsO0DiToHkLpXi83wnalPQN39BJuZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPjy4cVhrNs0uCXPINflp2NBjLTyPmauaRcz5AgfUe0B4JKxnCemN8-GwFUI20gGD2Jx8xuInRQ7LTUambto9A4DAUIblrz9aDXiZ4u-0nivla1Nh_PbWj8sEd4D1OcD-2hIkNBm_VdTUuTGuKkYIaAxauZSSaRmQTyNGOstOStlAF5QgbEQ0W1I5rWi4X9fXiCdLcmowoAkkEP1x48dYEv3xNtTTE2n6cTBzUksdmyJ2Ji6SiCanv1hfUzpNnxHYEIEtYYRx_0CyoTEkWslEMAa_SIlPj4popTq20iOtXGEArUjpu5oAg8PBqaN95QQIuB530m47H6Ur5rW1esJkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان راهی نجف شد
🔹
رئیس‌جمهور، به‌منظور شرکت در مراسم استقبال از پیکر مطهر رهبر شهید انقلاب، دقایقی پیش تهران را به مقصد نجف اشرف ترک کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448214" target="_blank">📅 09:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448213">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
وزارت کشور بحرین از فعال‌شدن مجدد آژیرهای هشدار در این کشور خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448213" target="_blank">📅 09:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448212">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77abfe5693.mp4?token=hm71hZvy8k3ObJ2yil5K_5cwOzszTbDlbSUaVIsnklgLIl5a4CusBHI2i2P7bgspTEFt3BqDxZ6NCtBbEcj46sr9AQzaMgLL-qglhJP3fL7s7X-o5OGC34OqC-6m9CZkpzcM625cdsGd6k7YPXoTo7YX12gAJg0YH3b4HIPCrbNWjjy04zDTLKCNx6KZzDtTDc35pleUPcsKxvCOrs8WVwGlgxD1eysjCs18isBcne_bRWhBMJCeWAX9R6b7gpY5KDgxKahJLAray9qJqLrwmdE6A0KbnNrV8jUUsi7g14gVftCyTTZVQJz7Go2I9gDac618mD0RKue-74SrX7xEYjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77abfe5693.mp4?token=hm71hZvy8k3ObJ2yil5K_5cwOzszTbDlbSUaVIsnklgLIl5a4CusBHI2i2P7bgspTEFt3BqDxZ6NCtBbEcj46sr9AQzaMgLL-qglhJP3fL7s7X-o5OGC34OqC-6m9CZkpzcM625cdsGd6k7YPXoTo7YX12gAJg0YH3b4HIPCrbNWjjy04zDTLKCNx6KZzDtTDc35pleUPcsKxvCOrs8WVwGlgxD1eysjCs18isBcne_bRWhBMJCeWAX9R6b7gpY5KDgxKahJLAray9qJqLrwmdE6A0KbnNrV8jUUsi7g14gVftCyTTZVQJz7Go2I9gDac618mD0RKue-74SrX7xEYjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب درحال حرکت به‌سمت حرم حضرت امیرالمومنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/448212" target="_blank">📅 09:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448211">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f901b9982.mp4?token=fviiSbPAbL-976pegcD_lPsaMdZJHM9J_cooop6tDOpCJXiclSN2udmIL-UAbFucaMKLsR51Poy0Hc7B9r6ZujhC2xDlmb5zh7TIgCaOl2jhiqajPKy8r9KykP3Pu161OrkzzW9qYRP-URP2N0qHla2M6H7Y45m2U1_5d9zFf-8NV4LHfc-bnN7K88R_ZJEkiA1HAzLX23yy4hq7_kpt138R-gtKn4RJVtp5QZFz5nDx_xWtOEcqwgx_0JvaTeuGqALna7urnRsra-BQuhdh6wFRszXoYFsqCSXwEUb6EueGji74-4eErRkPQugzMTKci8Wxlv39-lteveo8176IGVyRK0Najjg_dkmL6dUVvJd6Bnnz7mN0NsYhXjdkIxWVqRKm7rDzFdjlemTEP0QDvCRy_ZBIiMZmBjg7cuhZxHRzSksBo_itNplskjvVHzS1GD7gwPWqshsvAM3mm0ca3ZKgKPUwdu4B3dklYDZ5pF-tk9bb-qbNMzUahvMeNO-uA2keqft7lWEjAKo7nVlC-JY1YqahSvLzZJSY1z9Yw-PtD3IQ1C9oiGFI1Xkj7MNirub2jIomWHNx1x4Wv9kdDO3YZNDgX6ndNB9emi7a-gwKZYjl3EzAjN20_WS5uNVDRhgAu72RTFmnMJiZQxoT668MogEkPz2DO6ptRCQfFts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f901b9982.mp4?token=fviiSbPAbL-976pegcD_lPsaMdZJHM9J_cooop6tDOpCJXiclSN2udmIL-UAbFucaMKLsR51Poy0Hc7B9r6ZujhC2xDlmb5zh7TIgCaOl2jhiqajPKy8r9KykP3Pu161OrkzzW9qYRP-URP2N0qHla2M6H7Y45m2U1_5d9zFf-8NV4LHfc-bnN7K88R_ZJEkiA1HAzLX23yy4hq7_kpt138R-gtKn4RJVtp5QZFz5nDx_xWtOEcqwgx_0JvaTeuGqALna7urnRsra-BQuhdh6wFRszXoYFsqCSXwEUb6EueGji74-4eErRkPQugzMTKci8Wxlv39-lteveo8176IGVyRK0Najjg_dkmL6dUVvJd6Bnnz7mN0NsYhXjdkIxWVqRKm7rDzFdjlemTEP0QDvCRy_ZBIiMZmBjg7cuhZxHRzSksBo_itNplskjvVHzS1GD7gwPWqshsvAM3mm0ca3ZKgKPUwdu4B3dklYDZ5pF-tk9bb-qbNMzUahvMeNO-uA2keqft7lWEjAKo7nVlC-JY1YqahSvLzZJSY1z9Yw-PtD3IQ1C9oiGFI1Xkj7MNirub2jIomWHNx1x4Wv9kdDO3YZNDgX6ndNB9emi7a-gwKZYjl3EzAjN20_WS5uNVDRhgAu72RTFmnMJiZQxoT668MogEkPz2DO6ptRCQfFts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
پیکرهای مطهر شهدای خانوادهٔ رهبر شهید انقلاب در جوار ضریح حضرت عباس(ع)  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448211" target="_blank">📅 09:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448210">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfHn-kZNyrl945N7AI2PJN-nV6X9XKcU6B59n1K4mSMiguA3WGz7m3ECBGYWngKAv8mM1W6qv_7ALdz8xjvK4jePx_3pcuehWhfOwMhKuVF-NWleC1xqxFiO1usO-m1tUWoeVlljoUsnwg5iWigYD4pjafYL1cAuClbMkAFVhrhypIiXB0_R6pNqD9uxauw4vxoxPxba14OlG0Pq1WvI47raDZA2r0pg_S_1Emxesz1uq6gS3u0hpzyivanq72hFZ25ExzApnYMW99DKBiIRzzj4hJifrzymNacjqN552VFuqGOo0WOqi-x8J9APXZfpjYXN7utyxCpzjDVp1bUT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیکرهای مطهر شهدای خانوادهٔ رهبر شهید انقلاب در جوار ضریح حضرت عباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448210" target="_blank">📅 09:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448209">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
خیل عظیم زائران در تشییع پیکر قائد شهید امت در نجف
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448209" target="_blank">📅 09:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448208">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42c7bf30ae.mp4?token=tCVRiOZc5J9QDOcE0G7-V9D59vMEhWjjp3qH42X_BQilKC7x0B4dczPOnXiUmtIvGxF_JCy-7tZ7Vt9j9iWYJ-ZlDs_SeFR-7HtDGidxk0EoaZb8mhWoFbw3Uv33i2iz1TurH5k1aVtFjjHhuJ3DioK1J5CFL98tzviB1RzO0U7mFfYI5NHijsrBMU2at-7RyOfuX0ZQyIY1K-1JE1_0i2eLUTPu1idfYnCLpacIM-4THRqF1cIY25XPWPkKz9bJQLkTyyj6BeHcIJ-tos_c99_qUtSBUlxBMF0DN21uXA1wSUfKnCiDghnA6W3JoTChR7bmoj4Akw-7VIASYHo_6V7dCCOWdbcPjbkpPevYoEAAfaJbw-H45GSeegCMq0dMnOo1fRRJ6Dm6X9mvGwHAcePT3Y5y_JvTxGkeIeAXgJxs-AEa4XYWy6U779AEaCL7fXs4Jc2SSjh3-HVFF3PH3b0J18RQKqRVQFYO-Y9azFM65vRKDBxou-lyxw6DFoVeR52XgIV6fYYPau2ZS4NcHurFS_xlIwrDpbErCSwyQ3yg4IsihzuRS55qgpphRqYUzmiEZXX6sGirxQrCnqaeBiMo1Zr5-k0BrZ5AkWkdyAGHH-mQf73mY_r1k8_KH6rHri-fFx5cYGbwUtDU8byBZS48J-zuC8wZBiJ2t2ficgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42c7bf30ae.mp4?token=tCVRiOZc5J9QDOcE0G7-V9D59vMEhWjjp3qH42X_BQilKC7x0B4dczPOnXiUmtIvGxF_JCy-7tZ7Vt9j9iWYJ-ZlDs_SeFR-7HtDGidxk0EoaZb8mhWoFbw3Uv33i2iz1TurH5k1aVtFjjHhuJ3DioK1J5CFL98tzviB1RzO0U7mFfYI5NHijsrBMU2at-7RyOfuX0ZQyIY1K-1JE1_0i2eLUTPu1idfYnCLpacIM-4THRqF1cIY25XPWPkKz9bJQLkTyyj6BeHcIJ-tos_c99_qUtSBUlxBMF0DN21uXA1wSUfKnCiDghnA6W3JoTChR7bmoj4Akw-7VIASYHo_6V7dCCOWdbcPjbkpPevYoEAAfaJbw-H45GSeegCMq0dMnOo1fRRJ6Dm6X9mvGwHAcePT3Y5y_JvTxGkeIeAXgJxs-AEa4XYWy6U779AEaCL7fXs4Jc2SSjh3-HVFF3PH3b0J18RQKqRVQFYO-Y9azFM65vRKDBxou-lyxw6DFoVeR52XgIV6fYYPau2ZS4NcHurFS_xlIwrDpbErCSwyQ3yg4IsihzuRS55qgpphRqYUzmiEZXX6sGirxQrCnqaeBiMo1Zr5-k0BrZ5AkWkdyAGHH-mQf73mY_r1k8_KH6rHri-fFx5cYGbwUtDU8byBZS48J-zuC8wZBiJ2t2ficgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع باشکوه پیکر رهبر شهید انقلاب از کوفه به نجف
🔹
پیش‌بینی می‌شود پیکر مطهر رهبر شهید انقلاب قبل از ظهر امروز به حرم امیرالمومنین(ع) برسد.
‌
🔸
پیکرهای مطهر خانوادۀ آقای شهید ایران ساعتی پیش وارد شهر کربلا و در بین‌الحرمین بر روی دستان سوگواران تشییع شدند.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/448208" target="_blank">📅 08:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448200">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448200" target="_blank">📅 08:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448199">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USfx4oTaxbyDf-4HjRXcgkC-mNzOssiZA6IuKqpxsooDlFacj3WIwX067aq9VPymvIow7O6zz1GkOeYLDyF1-k9u9G4TSiv26wsTkZj5IHTph7kxC2A3t37G6XRE5_o_HiIx_KiGLjzTmfG-6Won5RI4s6gwM3z-bboOTk7DxkA3o_WzddVM181Nw8ebBESbIQtZEePxqvVk_q_yuCnc0DMiLCuACISKy1GsaYflGN7EpchIulalxgSGb0NKB_JahWNfjYSCt26dOVRorEmvo4e5JWb80yez53m5oP3ZqYQrMF8QHEDVGJCKStIxtHNH4IT6O3_tnaOC8Hr_KpXVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو گروهک منافقین بود، اما حالا در تشییع رهبر شهید اشک می‌ریزد
🔹
«حالم ناجور شد، دوام نیاوردم و با اولین پرواز برگشتم ایران…»؛ این‌ها را زنی می‌گوید که پیش از انقلاب در آمریکا روزگار دیگری داشت...
📎
ماجرای تحول این بانوی ۷۳ ساله را
اینجا
را بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/448199" target="_blank">📅 08:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkOy47wc-fMttwOjY210kF-ILQw5QzcNwKtka889SgBktnh_5wUaOgrHnmLLTO6mN4SkizH65OGNVlNEurasVttL3rXxQyMTorUTnB_BFw5OpTevMl0vmsd89q19OZI0a2xPfC0a7YSx45cCAaZCimd_b8Ord05ASA5IAxAx4oSRZWR0XlWMFsXndeMSyPY7D1MZQkiNcU_jDeetyseTeBifbLcPEb-5Kv9AKL6rJm17KltDsjPE_13zxGs2a6F9shF6KUuNksHvzxpv_W7h9DDQDqtyWsOkflB_Xx0sZA0phbb7xC1TlZGAHAzGgvICepaI2yINMjLX48z2HVnSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">التماس رئیس‌جمهور لبنان به ترامپ برای خارج کردن اسرائیل از این کشور
🔹
رئیس جمهور لبنان شامگاه دیشب ملتمسانه از آمریکا خواست که برای خارج شدن نظامیان صهیونیست از جنوب لبنان، به تل‌آویو فشار بیاورد.
🔹
جوزف عون، که تسلیم‌شدن به آمریکا و اسرائیل را به مقاومت در…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448197" target="_blank">📅 08:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chgN71gykqYJG-Uvkjomax_W2rBpq51FYRxkJVNSQjBYW7F6VO5KqjvHGtjTKqyrJG9nGsfekXbkFplvZXuQALuzf4K28ilADcYn8fMp9h_b6lCD23HNlsGjzYF217L2G0AYW9-RqlUtfF2WVmfgmqdIgbnEv3OPRw6MUEGeDK4LPjSoeq4g4G5xJt6a0vqAKd-5CfVVG-_G5ZjWWyxcPVx9YmOq4qN36XgnO1MnM0RS3m-jAeCRAXTyQeL3WVCKckrcoJbiE5CGp8-X6VbSXLrStdJfRsYtLUC88r2nmpHxIApjuORwMTqIPfGyMmMQ8eVPx9HnvWCrHsHTwbUQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قابی از تابوت رهبر شهید انقلاب در مراسم تشییع نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448196" target="_blank">📅 08:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
پاسخ اولیۀ سپاه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
🔹
سپاه پاسداران: به دنبال حماسه‌سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی‌سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/448195" target="_blank">📅 08:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448194">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b86b1890.mp4?token=Kp8QsahTIqSUDK-sibVobhUgYVineg1kgJz8jXJ7_fhhsDTGNZBfRZjonJnvRv3vsn9_AC03M85m6wxgDAuDz5nJNTEIjkJSi07XzATEKk6bjHScWstZdIl-O8n7eeocGtOsB3Jtcxr27s1HoZx4Gc4fKyGj22UQllWpBBaF6YYNLiOxbIjz6oXgQoAluQu0Zpf6xEC-eG1iX8oo-FGSBzNSgNaApMZrNtG8JFELPg-gmFAVMZQQfjGWFxdVuHRFUH7YZsoJl26j-bkzYSpjt6Wkqiy3wrUEstg_4gU_CjDpsBI3DgI4VZFsFDJ1stLQgD7s9oQoarFjQq9Ol6HRMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b86b1890.mp4?token=Kp8QsahTIqSUDK-sibVobhUgYVineg1kgJz8jXJ7_fhhsDTGNZBfRZjonJnvRv3vsn9_AC03M85m6wxgDAuDz5nJNTEIjkJSi07XzATEKk6bjHScWstZdIl-O8n7eeocGtOsB3Jtcxr27s1HoZx4Gc4fKyGj22UQllWpBBaF6YYNLiOxbIjz6oXgQoAluQu0Zpf6xEC-eG1iX8oo-FGSBzNSgNaApMZrNtG8JFELPg-gmFAVMZQQfjGWFxdVuHRFUH7YZsoJl26j-bkzYSpjt6Wkqiy3wrUEstg_4gU_CjDpsBI3DgI4VZFsFDJ1stLQgD7s9oQoarFjQq9Ol6HRMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ندای لبیک یاحسین(ع) عراقی‌های حاضر در مسیر تشییع پیکر رهبر شهید انقلاب در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/448194" target="_blank">📅 08:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448193">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">◾️
المیادین:
استانداری کربلا حضور ۷ میلیون شرکت‌کننده در مراسم تشییع پیکر رهبر شهید انقلاب را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/448193" target="_blank">📅 08:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448188">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MORhSp2xPAGqnk2b3ckylnplSt6rgSP5_Tiv3GFIRgCZgsk8VwLvZFnCDYtZcloGD-_onKVbHdayC-yPoz8hQMOCAe4cjMF4SVbB77yK-DP4V4v7P4nv797ibtBe6umP0IqZiU5_DstRAVXPXylsM7oAfy4LNVM-aIulYRPJkn0UvsoVZZDgZlEm77VE40Y0_0GRgj54f89qwr-KH8WRjAOGH5k6x0nYySSKONkPYqSSOxhtEfDIBlLqkzZvCaNZUzs7mDCqcKjxvqE0JOxcxzjDdqMk3KcH2rmn5hCEOFXccVnlbfM8sPU37IX7Dodnzsn5tChOLiSyfj7DcPn9ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKLIarKs3GLtnu5mnYFFP1zP7S9OK00dYaI1LniSoGy3aPxFosJiIzxdNy622ykbAZkmRcKsk-Y7na_24oIXoKKbvOxWAIO6uUV_Os6AwEKxwIcP5AeOGhZMEMKvNxfsOj6NKUwPrSzFY3wt_7Dn5M2Y_s7jp2v6AHq-orgZR6qKIChnjDpOJKYUSfMfi8BgOBMERWMBiVjaZV66nYW04bcCCGUOv1Y1e7CSOmjJJc0qHTxWCqiM-6_FGz_UtbaA3NVS7vZKu4P5Y7-ZdDQThFAPZATBrV_miOcw8SFHRb-iwZJ1LF7athrJdvgv432nj0JPc4GBXi0M8-ZCHgIYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDP3pcaGLFRBvnHqecNpqwUXtO2grDvtJJ5If5kAWDFESRStQ1iamj2HsgJoDIRQi88BFKi-BWzN1CwsZQ122lhLn8VArudGPoitrOehfsd0qegW6oNdRbW-kiOjHAPdN24qNwPt9t19kgHjjTLkBMsLmq-pv4o0usARDTp21opJ9M2jp449wGou5gkafKS_MLWIvp097dHjI8pZTuD4D8PLTntXlLzWPXDU8i_ruo_puNEFc3-X35cGsq52Whnrcx4UrtQkD3NLIlS97cl9AZUYzfCZHFLJxG2BeE5yISdIuVMutxEmc5sjiNlN_l7MROaBr4wfi3Ut4WDhT9QQSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3TXd9hnu1M1XsuG9ql8A2-WXBtjOpScLAXOjV5HI_n8ukMT9B7rOlT_0TI1B7QBOG30GYyy5v-omgCUF-MQqWx1WhkpS1-wBek5-LjOPZHQGaoQtNrrxibqtIhipB5OJ8u7f9In1ZWLAeYcTfHBlstuNqcjCDWdlJxuYvDCDpZ0hJeVQh7wT6NO5tfHYrGg4TDSO1uyNwp_MKll5TIPsJANK9DBjXBNHeEOrACLxww3nu0V1AQVvxnD9-m9JDdj1N3ofdsetsXI0oeMiStN16ejgviW3kfZnvU6UVlIOgZ8GyWyz7fczssvZKcOUp3OiWzqf6-ZdTtpC1b5fiqtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAeEDdoIfZN-vjhp0AkRhz9h-gnp0FNiy0eGmQ0UMi8JHRmwfEzAsoWjR4ihaOyGdf41I9mmVNptLpgHZ1vsI9ULNPKWFgrE6uL9hfN4pQjusjMdXySJQ79ArY-5oqqhnvgLFuKMAa-8m9MosaLQi51lXpl-kOlV5rQDUmJvSRFgguYfcUSM7hvh6O_w1wQZOHA90UNwdtjRrV_3j105vaTHZ5HGToUO2XOZUn7RuUQLjBe59UBB-Vs3EZWQH0GIVYni06se3gLM63itQMjvqrSzN6Oea2n5GNRLGPbgGmuUgMpGamfwGMs-dyIbqk20y04_jYmwBT24lY9o68mihA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سیل جمعیت عراقی‌ها در تشییع پیکر رهبر شهید انقلاب، در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/448188" target="_blank">📅 07:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448187">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9800658183.mp4?token=ncWI-TyQD1PwKzE8E8hEiRV-xcNkIZOuM-_5pd_8VAyCUi1nyXl41HMkF8uw9KwzPJ1tIPe5G9hpEA9H6hjuViyZUaGR-m5552Vn1MidUNI4IY8NkyQdb_OtqEaWUk8d_TzrPZPksdVV41-5mUJ2ZFGzgwhpqxvZ0ehAIXduYkKyPtpNmtVf9xtl4nWgpVJCwVJmaLlOUAXgHfoosSoE4L831Rdg3fHlVHsmgXdqyIQQUJdxTldFIewo0otCGb8kR-Gp_JFVYEqBeScifnTm4nU66K7WytS_42JdyxEI_35Q1ljjj3s2YY6yAtuzwjjyszIhcLoKfIIWigx9aK3ldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9800658183.mp4?token=ncWI-TyQD1PwKzE8E8hEiRV-xcNkIZOuM-_5pd_8VAyCUi1nyXl41HMkF8uw9KwzPJ1tIPe5G9hpEA9H6hjuViyZUaGR-m5552Vn1MidUNI4IY8NkyQdb_OtqEaWUk8d_TzrPZPksdVV41-5mUJ2ZFGzgwhpqxvZ0ehAIXduYkKyPtpNmtVf9xtl4nWgpVJCwVJmaLlOUAXgHfoosSoE4L831Rdg3fHlVHsmgXdqyIQQUJdxTldFIewo0otCGb8kR-Gp_JFVYEqBeScifnTm4nU66K7WytS_42JdyxEI_35Q1ljjj3s2YY6yAtuzwjjyszIhcLoKfIIWigx9aK3ldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب در بین خیل عظیم عزاداران عراقی در مسیر تشییع نجف اشرف  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448187" target="_blank">📅 07:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448186">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d414d1b2.mp4?token=Cb3LS_LaFTkyxv21iSHGZZyG7rSGZwzxlvw60ikilIVJP6YzWDhCWkliApvKORgitKxXeUX26OuCvCbIIUGrwbvmWmdStQ0LgZ7qGhQCyRQaTpAlQCEzZA8KxVpU-ZSsGj6S7tlk_jqldbK7mdNt5MFngQqTS7tglmQlrVZcb9KzCA-tUBlxKSxxWOCR7clzEClKCuC_gehh70NHMAcegv09xmsPPS4wpzVKWLZYyDM5USgWbEMvUYGbknMDSORJaEmr5-OsgJTwYojFFktpC6yx3ozS8Y0trgOf_Jjl3cJ0ObJhJ78MfxRaQPuqeDadsHVfePWNPd0bA5xeSIPYsh3TFruuTmnbapoc9V9JQHB2WhnipUkTUkx8gJNNSMBqd9UzIDCFh9sEAfyEWlJSftUDMvhm6BvRQmGB8keY1m5tGXR12fWHnHNjEMIQeEqTPnWxooDJM6XWumckv6Yja3uqYlm3wvycaKpnrFMPq_HPxEENStSbI0WYzmZd5Ddv1StzEYxpnmjMHpUhY88iOmkFKTXLqWODMuXs6G_zb79_Amlwnoa_7DmkCVvdOU43kNifLJWGA2pR_h2oSw2PFZVzad5FkdGClaXMnqrIIM2CVuyK6isWLG1VL93JaS-t8WlmKVcdnADyaxCyxVtZPbAfu7zt973OTgtLdj9c9T4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d414d1b2.mp4?token=Cb3LS_LaFTkyxv21iSHGZZyG7rSGZwzxlvw60ikilIVJP6YzWDhCWkliApvKORgitKxXeUX26OuCvCbIIUGrwbvmWmdStQ0LgZ7qGhQCyRQaTpAlQCEzZA8KxVpU-ZSsGj6S7tlk_jqldbK7mdNt5MFngQqTS7tglmQlrVZcb9KzCA-tUBlxKSxxWOCR7clzEClKCuC_gehh70NHMAcegv09xmsPPS4wpzVKWLZYyDM5USgWbEMvUYGbknMDSORJaEmr5-OsgJTwYojFFktpC6yx3ozS8Y0trgOf_Jjl3cJ0ObJhJ78MfxRaQPuqeDadsHVfePWNPd0bA5xeSIPYsh3TFruuTmnbapoc9V9JQHB2WhnipUkTUkx8gJNNSMBqd9UzIDCFh9sEAfyEWlJSftUDMvhm6BvRQmGB8keY1m5tGXR12fWHnHNjEMIQeEqTPnWxooDJM6XWumckv6Yja3uqYlm3wvycaKpnrFMPq_HPxEENStSbI0WYzmZd5Ddv1StzEYxpnmjMHpUhY88iOmkFKTXLqWODMuXs6G_zb79_Amlwnoa_7DmkCVvdOU43kNifLJWGA2pR_h2oSw2PFZVzad5FkdGClaXMnqrIIM2CVuyK6isWLG1VL93JaS-t8WlmKVcdnADyaxCyxVtZPbAfu7zt973OTgtLdj9c9T4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
قابی متقاوت از تشییع امام شهید در نجف اشرف
@rahbari_plus</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/448186" target="_blank">📅 07:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448185">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81706a78c5.mp4?token=Z4CxIMQQ2ctiXz0o-pN9VjNdLUhqCEt-6hLNXdyMMOQ6PYZcg9RbFr-L7ZxWtTYochFaWmpfnlxgP7yVkE-oRrBc1vECT5ItyVoXNNnbuI7zkttayQnJtvCUXQbLYYNMW3HoXifiVjFOvf_2gcJf5BgyQRK6ADs4Q14hCAjNBVr0jHhaOnxWURs4fgXAuiHObUnMGUHBnIF8yM0OdpjcaN0BR4TjI8QUGLPRrF4h4hbRinqjnL7OW3mhM3nxXP11NAe-rLO83neIOEPx41gEJJC21FC-ULeVsW3XPsoGT63HonQFyY7rEGuSwMbyGgwLxWRV7IlJT_EBK8yEQSGfkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81706a78c5.mp4?token=Z4CxIMQQ2ctiXz0o-pN9VjNdLUhqCEt-6hLNXdyMMOQ6PYZcg9RbFr-L7ZxWtTYochFaWmpfnlxgP7yVkE-oRrBc1vECT5ItyVoXNNnbuI7zkttayQnJtvCUXQbLYYNMW3HoXifiVjFOvf_2gcJf5BgyQRK6ADs4Q14hCAjNBVr0jHhaOnxWURs4fgXAuiHObUnMGUHBnIF8yM0OdpjcaN0BR4TjI8QUGLPRrF4h4hbRinqjnL7OW3mhM3nxXP11NAe-rLO83neIOEPx41gEJJC21FC-ULeVsW3XPsoGT63HonQFyY7rEGuSwMbyGgwLxWRV7IlJT_EBK8yEQSGfkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب در آغوش خیل عظیم عزاداران عراقی در مسیر تشییع نجف اشرف  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448185" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448184">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff90c9a8d.mp4?token=nqYO_54gnLq_CEj3ZiBaS2wO-imo0awCPaxCQcs_Gb4_f1eDgId-wON5W2LEmv4-hKTorkNSeMGXjz7AkjpklLNwr5U6jZe9HaPLnaaynTiFecoTx2gh07Qmg8XeKvyx7gX2wxF35kk8rat70P69eoPy_L3KXnoKuFDGAYOLHXqUarchsdSx1bokxmcIRCXqs1zAfmC7nI8SU3UKmPV7sAe_7nnWcBLs2QSC1gBzrRMxIkw_yxZY2u6fHpJp_aLvLPHx6cwdmRVGAV2gly8TE3BeFpxtuiPqRpCDHGWlNoAyeC_Sgh7IRrK8vpuPLG7t4YmzraPmwVNOreNwWGBcKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff90c9a8d.mp4?token=nqYO_54gnLq_CEj3ZiBaS2wO-imo0awCPaxCQcs_Gb4_f1eDgId-wON5W2LEmv4-hKTorkNSeMGXjz7AkjpklLNwr5U6jZe9HaPLnaaynTiFecoTx2gh07Qmg8XeKvyx7gX2wxF35kk8rat70P69eoPy_L3KXnoKuFDGAYOLHXqUarchsdSx1bokxmcIRCXqs1zAfmC7nI8SU3UKmPV7sAe_7nnWcBLs2QSC1gBzrRMxIkw_yxZY2u6fHpJp_aLvLPHx6cwdmRVGAV2gly8TE3BeFpxtuiPqRpCDHGWlNoAyeC_Sgh7IRrK8vpuPLG7t4YmzraPmwVNOreNwWGBcKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب وارد حرم سیدالشهداء(ع) شدند  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448184" target="_blank">📅 07:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448183">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5e5d36e50.mp4?token=QSuu238B9PcrmRC_5_iBoJGyzWKYWckxIpDsA8uEA31cx0L3U9ZItjNSfVSUJGuAxkVU6dweoI5B3e9H7KoQF7MEzSpB9-1VHjf3-32exKr9VUESRhXdpoY7ZFJhaPhCJRuawakvOEZDoU4yolbTkaLR3_HHHEKzHD8IwlQuCINW8JuGm7oH2adYH0v9LEdPSDBc1FAr5Np49U1slcJ6V0WnaCsspUQlWPWFr1ZiyE9Y7QNF2Z8KufEHQaQ_oJkrFqD4FX4DcKU-kZS_KRTCA4NMIPNmcVAH438LWEY86cOTD8Ip76dr4YR_vw2mUH-QiKw8LED31ZijhiC9y66vVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5e5d36e50.mp4?token=QSuu238B9PcrmRC_5_iBoJGyzWKYWckxIpDsA8uEA31cx0L3U9ZItjNSfVSUJGuAxkVU6dweoI5B3e9H7KoQF7MEzSpB9-1VHjf3-32exKr9VUESRhXdpoY7ZFJhaPhCJRuawakvOEZDoU4yolbTkaLR3_HHHEKzHD8IwlQuCINW8JuGm7oH2adYH0v9LEdPSDBc1FAr5Np49U1slcJ6V0WnaCsspUQlWPWFr1ZiyE9Y7QNF2Z8KufEHQaQ_oJkrFqD4FX4DcKU-kZS_KRTCA4NMIPNmcVAH438LWEY86cOTD8Ip76dr4YR_vw2mUH-QiKw8LED31ZijhiC9y66vVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب وارد حرم سیدالشهداء(ع) شدند
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448183" target="_blank">📅 07:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448181">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yky9SwtjtC5QVsmj1x0dTrr5fRJVej69ZcAWolEqfio6KSBVwJsSuEQ47dBS6qIROCcB7CRnVDoUrGk6PBhlntD9vRxXKdAYPFAArQT9N3qepnIuFNLAzsJs_LsDkuj87Azmi-ZpJNQLsLn9-NW8gknJvSW-NxjBhMgfxWv8flNpjJoT-LxajvNRClfCj-zZazm5UlTl7HosQf6t6GRXhOrY2d2jbOWkGAEUIjMYGjbPO5LSbSnXu_8xApCdtIpG4cgYAMNsrE6yA24u3ILhNcbd_cCoewQK_K3QPTTroJLzZYWKTIqH-KXouYn6lY5WdyqD5c4XZme2EkDa__0EZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej7mx6NAM620RpTqjYnWNE2cZKBY2enWCwE601J6u69LfhxD0ZWbQKyzdRJyYrhlp9qJrf4yzeaZ8ZYBpi2WJmJBzkW37_6A-vECfUETy3JqQWJtzU_TKcJstDQRm9xtqizbelXJqZaJFgQwr_Sc3MHR8ucBRITnh82K0h95TjgIublek0Ztw8amahnkdDUYQ8tf3ecuDVnHGQPFZFZCSkFtbC29W9RaQwkfeaetKlwBPSwB9WkGGzlIf1piFunlPGtsaOorQnf2dAkPuGzPY4ShLUSydCOdJNO_-ZT66R0mIKdj5pRfYGjc8NabGazLg2mZBUR5J0T2q5HvqM_h3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور شیخ ابراهیم زکزاکی در بین عزاداران رهبر شهید انقلاب در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/448181" target="_blank">📅 07:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448180">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
پاسخ اولیۀ سپاه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
🔹
سپاه پاسداران: به دنبال حماسه‌سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی‌سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر آشکار می‌شود و بازتاب جهانی خیزش عظیم و میلیونی ملت سرافراز عراق در بدرقۀ تاریخ‌ساز رهبر مجاهد شهید را شکست بزرگتری برای خود میداند، بار دیگر عادت پیمان شکنی خود را تکرار کرد و وحشت‌زده برای تحت شعاع قرار دادن این رویداد تاریخی، ارتش کودک کش و تروریست آمریکا در ساعات اولیه بامداد امروز با تهاجم هوایی به تعدادی از پایگاه‌های ساحلی و ایستگاه‌های غیر نظامی در سواحل استان هرمزگان و ماهشهر به طور آشکار آتش بس را نقض کرد و تفاهم اسلام آباد را زیر پا گذاشت.
🔹
در پاسخ اولیه به این تجاوز نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی طی عملیات مشترک موشکی و پهپادی، ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در بندر سلمان، منطقۀ پنجم دریایی بحرین و پایگاه هوایی علی السالم کویت را در هم کوبیدند و یک پهپاد MQ9 دشمن که قصد دخالت در عملیات را داشت، سرنگون کردند.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/448180" target="_blank">📅 07:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448178">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5gzUFBdpRwq6D1PhZQ9ACu2I85b2Hkvqud8FPlM0H1N71GFbSOJ-rilMiKFQ5Mc0BwWtx_9WaXwlj-Yfj0RMhHTT5QRb_DtlgErdnv_BCO3r58c3FISbBs0I37HacBFDd4R_4rCbiXddrpuuzjs4yAQGTDh6eD5lNdvvVho0Px9RTlJ6xdox0sq2TvAYzQb683CDGkasRRVRalHn0wVuC2c8XhAfViBdHhLTET3iENZZeeO0iWqZZ9q7lGZAD0DbtQx53XZBE5LBd6C72b1HP2_uPOLJ2NH__obJjBZrFB8twqK7JDOUh45JvligS1Z10eDQMACkUa6eCQIE0bp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fdf85d21.mp4?token=mySI70RcU0uoJOT-vgYNrvy4yxV-jH8GYhU5mu9HWtakDgDUvEbPpitdZR4tbTHAmAIdZn15JOu6N2AhahJSur19Pn145ney25MuXDoatIctzcho-jTkoIs5fCYcUq5m4yBmvQJadygGCM1hx2Z9oGt0uL9rk6oX2-R1SCiuRkZ2aRxAQpyeiO6lnO4asLTL8zeApPGhDs2PRTvyADSxsTGcJiEfqZWp_JiPHWgpMGcvzq1JRthlvZERasCNi8D7Sw-A8UOLrY83N7Tc5hRYrevU4G2SMqW4wwsh2HPvkJUUJCoIgKkwzdFekGDDGK4zZdxwnVnb4ScvMqpG6lMyeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fdf85d21.mp4?token=mySI70RcU0uoJOT-vgYNrvy4yxV-jH8GYhU5mu9HWtakDgDUvEbPpitdZR4tbTHAmAIdZn15JOu6N2AhahJSur19Pn145ney25MuXDoatIctzcho-jTkoIs5fCYcUq5m4yBmvQJadygGCM1hx2Z9oGt0uL9rk6oX2-R1SCiuRkZ2aRxAQpyeiO6lnO4asLTL8zeApPGhDs2PRTvyADSxsTGcJiEfqZWp_JiPHWgpMGcvzq1JRthlvZERasCNi8D7Sw-A8UOLrY83N7Tc5hRYrevU4G2SMqW4wwsh2HPvkJUUJCoIgKkwzdFekGDDGK4zZdxwnVnb4ScvMqpG6lMyeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر مطهر رهبر شهید انقلاب در میان جمعیت مردم عزادار عراق در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448178" target="_blank">📅 07:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448177">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4707ad6fd.mp4?token=jtcFxM2LH_9uDgZZW8VzjeAj3FeC2DXgDmfOs0j14E-AW65RAQPo7WzWt-AWZpWoj_ec3xGw1UwBxxUecsYtkMvRtur2Vrf__e6bGMRBBnCPR1gLwqJ9B7PhJxHsntbNM9CLdsFnxHm253RfwVe3lCPhLP2DZKtICGqsIS47SJGBhSR8nHA9kMHZmh2d-pMwbjqPyaAsbW7O5vHY4I5ifV9YtxT9zxRGOVRouSaxCrIZUSp52hAnvIf08xy2Kspq4kLo5iAj0q9b3Aey-dYaF_YXaho6zMIcQXkpPftfAh5nmN4LUIp80LyDGhtugLDtAkkYV-ExJd9QWpdJPmg6iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4707ad6fd.mp4?token=jtcFxM2LH_9uDgZZW8VzjeAj3FeC2DXgDmfOs0j14E-AW65RAQPo7WzWt-AWZpWoj_ec3xGw1UwBxxUecsYtkMvRtur2Vrf__e6bGMRBBnCPR1gLwqJ9B7PhJxHsntbNM9CLdsFnxHm253RfwVe3lCPhLP2DZKtICGqsIS47SJGBhSR8nHA9kMHZmh2d-pMwbjqPyaAsbW7O5vHY4I5ifV9YtxT9zxRGOVRouSaxCrIZUSp52hAnvIf08xy2Kspq4kLo5iAj0q9b3Aey-dYaF_YXaho6zMIcQXkpPftfAh5nmN4LUIp80LyDGhtugLDtAkkYV-ExJd9QWpdJPmg6iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از سیل جمعیت عراقی‌ها در تشییع پیکر رهبر شهید انقلاب در نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448177" target="_blank">📅 07:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448176">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب در آغوش خیل عظیم عزاداران عراقی در مسیر تشییع نجف اشرف
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448176" target="_blank">📅 06:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448175">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
برخی منابع از شنیده شدن صدای چند انفجار مهیب در کویت و بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448175" target="_blank">📅 06:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448174">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یک فروند پهپاد MQ9 در آسمان خورموج ساقط شد
🔹
سخنگوی سپاه پاسداران انقلاب اسلامی: در پی تجاوز هوایی ارتش تروریستی آمریکا در سحرگاه امروز، یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند هوایی سپاه پاسداران انقلاب اسلامی در آسمان خورموج استان بوشهر، مورد اصابت قرار گرفته و ساقط شد.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448174" target="_blank">📅 06:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448166">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vr0SiGClrTaz65Oxn5rK5Af2-7mhnHL-0indNGRf7iQ3XDz_ncc7RFJpQZXExtYFPL5O2fTMMLT1neCE35LN4nyt0IK0Rjmx5xa7T6K6YQ5r7r0_zHMsf7MhRDAygi8zZsOzjKdGRoO8s3WNsmb-RjB32bM9YRhdpnS3PJxuTezqyKdJqTGeAf3YUn3wKO4C9hokiglglEVUKQiFsg6c6a3S3uUy0tnjIrNIkQhJnf0RZRYqL-R4ubMT53XuTJcP-9k8ePxFUQ3sWZHdYW_TE2d6PAcIgiqpLcaE9Rt6MjIZ6G6psHz8AG25st42fzovhrVCPjlV48NHGNxOBiY8fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_IV8Gi_X1nzgrbOO1FwJzdW63f0ysaxlBGpKXtIB9HEXPqsRmXQYyukceAUvFjGEWcGQb9UzyTXb0enRQLXeWQI3MfD4WJosIyeTvEZm4VXEpDsWHF2GI9BrNZs36313ljmcs1tXr8uoCn4q-5jFiV9bFiM12GfG1EyhxGg3KNQBbGMBDVtDsxwCqIWuaH6btFV0i9Lh3wdjqpNOaZmluiaOSyN3PioNpHBfT3Q2auyivszCz_YL4QkuJZa9NBYKJ21GkZnRkdsYYK21KJsYfrpi0lL7R31vpU6ZQV2Jt08IwKq1OT4qXuTDcjdnjhKDrw_rZYgOzegQHVmvMRSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBazNGq-9ulab6pi_FJCqZU2BIPra4lFe3lAGyxKlJcYA5dVC6rg3j0cNrEZjPba1r6gVnu6C0Whil5Co2c9XbFDdpn1NdGVpSnMoQtMtPBI9qLSE1EqpxgohNkcyMyVmfr_hCtZqbQtim-Gs4B3Bb4YQMDXL4eSxxl5vmwpQZGOhoKrmE5d4-gnjnwBE6NXvcDf6ptEGm0UQl6TQeHu7KfaqSNBgSWtrxsnbXTHQr3C9855K_oNup_XuPOReXcz8lMl3XqKRgK7F_8UVRaagKTe35H725ob-P17PYQzcOLLYu-3QSD1wZh4cnR57RPcgErdc5sOYCnD4iYnCc8-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bc_EbFu09aJ6FWbRYD9UjHFarMLrkxUOq4JWPoCnpNWPAZBM8TbuzUCUsC0l7UMhpZo7ZEjkhViY6Gnbd2GUivaiAh9LiW1LrcvBuGCa4zEvY4A763jq1VmanfnGg7Ec7yQbP5YPjc1nYRx43vUXRQ6Tb6czQrhg2m2mxmEhuPSx_HRNRoVgiszeY0X2MjZDzI8neA_A4TCItuWwpxx0oBCoUK1Rdxmsgb7YEdJ9ulcsjHnQ4jyWJZxtM_3HpoXs336TEYHL2RDHZM6QdWxj3aBPrRLqcBUXgxRFZplVOYY_P5ic-fohmrenc0ugmp9Lidf8TlHHEkVLlayG8xyHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtUqmJkW_Vs7IgiaZ6r6JY9WGdYyjELK_FRxXnsSLnVhfVn71kmW_VEgo-ai6QZh8NirDLVgi5i3xbjKRK12OUYukMZjRZw9tXqJYaaOsBBxi511jiVsMBTqdZDalvxnaFJ_orx5fckHS5hxsjbBCtLA-iIID3m2RZYgRcB5v2X_JUGmZlq16RBxuHiQH1ZNLbvWM1yE83eSbHeedQAO8GTM3vY30cgX4bYV9zcd1T43XwbILQswVzidVKFvqmlW9nl4kKXhqT0bI6muiGsiQt51hjN9sl-wUw6T_h0biqOyQFPP5zlREfzjX-32fWfXaeom78G54aPte2Akb3TMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQ_IR3rmmEOEveGCrypQtnjoZcsYXEwv4ygpZZul7FJjfG__3geG0baJiB5vc-19edfmFdFlNhj5d1yUtrRSX7sbm3CNCDSARuuBq44gJKBzBE6L9TrADiNaSxIxCfp0ZJAS-21gfMRExOFJtQ-T-jugiYfqp3SMOHCwtyOW3NI3xd9_-c5EB_6BNaTNsNJBkt-jl8urCtFQrCTNfUTOOUXf37PVKoRkiJil57T_hTHAGPb5rM5OeT_94JKkhiQrJAeWWcRgK1gTn11P973GL9ncr2o4WArzfpOyZOZFdu3EtAq4TsN9NXPOtGd7tlPklraJAdOMeKz1JYbI54ZGOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rg2JcC4GYv5mzrERzR8H041QE43L7VE4DlARI-fdBZdZQ-0L9OfN0brv2wNo2vL2Ig_-qKAQt1BtlYNquc-8ReiQb2S0PwxTy6eGoOtQj5_bXUcvsNdUmoVa8dVfQuxn7-YrG2k2sOp3AO_EUCaFvyEPvRayz2ALjKf_JaPWqlRvnhUwsgqoMLjD5vs0VGa4-T0y7ATsln4ftlLHtGVE87rGA9A2s9XAcm57L3uSX_UmGvqyvGx4-cxDnGhVRJ7NkrU9MEFomZQouhyEwCskYikdBi3pk7zh1P_VuNm-0RO8uyorIIX7b7FyJuVy9GYRIW77a9F_jWirz3QZ6aDUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1TEYm3r5TFqhpd_Q7crYBq9I98b8dKXXDbqBqwRNg6NOYTrN5Ofr3FNOr6vznoRjd-u6NqzOMUT0joMMaGVFMlzKlSAwcZANESPZKWklTxSBHNFvxs8n4fa6gDY-nbEOa6bqoJ0g4JcaAHzP0Y6DAGHHB6EMUZY1KiYaCF2CTpfPW-9we5v9GnJvwaRJaYh7bV7EhdA0qbN3e06zmCXl1HJrqI1E-8J-dCCotRBJbMJOdOUTSo3aoNkt_JV-thQHy3Jj5376aTJ9UsYb5tmMNXBx3-gnkMaTIeb4UQZIT1fQKPD0DZ5J54HRNEV93I14nJcTQXocM-W2HZZoOvENA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع و طواف پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب در حرم امیرالمومنین(ع)  @Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/448166" target="_blank">📅 06:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448165">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7688a9660d.mp4?token=Z2Kbm60Hq4SbY75lqCc5k5-JQYo48CnTYmEhtNE5lyip6ivSUzfqG-R0tWISBNGmPUuvVyHhHG7IxEFXQgQZ9WHHb1HE3ssMZ35uBUaBXXZFfrVF-Ex0SF75II5dRIYXgmlA6ECQ3sCUbeHY5FlsuesVv8VW9XnQnUVearwVWloqmpiXVmfuCgMT2mLW2vnYngWcbq8oKGD5vuZk-I5kfdkinhdI-0X92PxDFsd8QetoeFH45m56iNZY70DNfabhLqHaQm_cvYEGkf0IEGShuogAXpmhwJlV-zL_VXaIXuKU60PlcB-RKkBmaxaPE2boBVAervQDaHkPkKgVG5FKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7688a9660d.mp4?token=Z2Kbm60Hq4SbY75lqCc5k5-JQYo48CnTYmEhtNE5lyip6ivSUzfqG-R0tWISBNGmPUuvVyHhHG7IxEFXQgQZ9WHHb1HE3ssMZ35uBUaBXXZFfrVF-Ex0SF75II5dRIYXgmlA6ECQ3sCUbeHY5FlsuesVv8VW9XnQnUVearwVWloqmpiXVmfuCgMT2mLW2vnYngWcbq8oKGD5vuZk-I5kfdkinhdI-0X92PxDFsd8QetoeFH45m56iNZY70DNfabhLqHaQm_cvYEGkf0IEGShuogAXpmhwJlV-zL_VXaIXuKU60PlcB-RKkBmaxaPE2boBVAervQDaHkPkKgVG5FKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی خودروی تشییع پیکر رهبر شهید انقلاب و خانوادۀ شهیدشان در شهر نجف عراق
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448165" target="_blank">📅 06:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448164">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsI-LkcH7iNTVDD1aJb2nrwkcmKvaCAeAAVUJoiyniGHLC7kNehyxK7Q5nfi5Km4Ffso5FoDhLw_WWUwSMBKngTurqzIRHSq2ptr_w_5357M5i9pE1wHS91id2_EA3a4YJmgBWyAJCjcxBeaBiZmNbB6eNrp6sMzLdlx9nmp6GK0X-DPvUvxjSTgtmPvXfdIMraup8J9jueIlScVSP89B_zre_F4sYCxPVSuIqX-FrBCMXEjrF9rQ4pG84dGjwI9ubY0Vt45Ur6p1eXF8-2h-f9v6vZSolX01z2sDZn8az2Cr8IrXznDMq_JY_WtwnBVJWlwLCaDFDzU4wwGaAodlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: دورهٔ قلدری و باج‌گیری تمام شده است؛ ما اهل عقب کشیدن و کوتاه آمدن نیستیم
🔹
کلیدی‌ترین موارد نقض تفاهم‌نامهٔ ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگهٔ هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار تجاوزات رژیم صهیونیستی به لبنان
🔹
دورهٔ قلدری و باج‌گیری تمام شده است؛ راه به هیچ جایی نمی‌برید. ما اهل عقب کشیدن و کوتاه آمدن نیستیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448164" target="_blank">📅 06:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448154">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5Tl-bt8jUctIc0I85K9EqzbRz-xDO6FNH1LysN4R3WenIe3w5ucA49O74YLiHpvBWM8GtTMpNHghE9GAwicdcNMX22UkUWfq4hqI-bcOBMAvihZkMNzyj9ssfLN9aZIuJ4V6SU_Efu3L9FnmbdaPvFWvEe1vr-JF6AbhL_sLFlyiDcPSOtE4O9KbygU6fhTTSX2oCsblrSVxu4ETgWppj5IF5_zVVX-WVKc6hu2QhFTQ7E4Rd91LRunj-2Z88tqolnMJvMIHskh-UeXRuizN8X9jpHhN2EIm2kqorSFsFo4SGE0qG0Htjtgi9L56yEj7CMbNPuQuYq-nwBktblq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCP1hoerR212W7PZistAvWAwz5GTRkyjC6N1OFZYDr05g-1B8lD7TzKqKAbFzNgRttm6HE5gb12gjInbctOJLyLtu9Umbval5noTCa0G1L5kE0p6DBOkquvIBNxVD3TLNF6sQxqnLO_S3tWfLryu_98EVBXxy-IKrDO33U6PP20NNepZCbojp3WREC-FOuLKrT758yJuWTCzWjw7uy9k2RIjuHD0qtgE-4aRFOf8danbioU-SQN7V0XoY4xwibmXhXotHxayC_z4plDbRIpdJ7kjWPdOneiqXcdjV6YTSXevUpXdm1QqEY0LJTwRFs8y7Ti9XOJHI1gnAJAjbPOocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDpkRV7OWoaLuegJ8vN6Vr5BR7il5g-PfYyMrvdtqMAYRXi9KsJV_HvsYa2Sw_eXIjQDHRIHzXqLS87vQDPiwyyjzBgDuJmh-HIEojeMyG0Kax2Pf7LpyTXT8SQY7PrbururDRlEpO2Io6EF4UytqSI7lh2EM7wOqP_xuiS8pC29SUWtwus34MCiVd7jxW99SqDgYRfbFXZCotnRBpMe9fmnsuc4EsfuOaXFbv1oF6XUaTYN9OcVpTQs-TddUjH2-tkMnecf9LO1qIu2qxJPUP0uUm8VtPhslfegGgCvzbEdsWR_fwuc79GJRqUVy67cUbHAqwbbTGB_lJJoEqYh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEBohpGv-LzVEBmXDVJGprJ-H6hg4Auk2NxIOJ9CXx0x3yzBU7w6NA09IWIEb4u2w9xBjErKRiMC9cLWwjPsMlfR3hQpZZYLAZ_lD-bvtm85sgA1btJWBzRPLXSPKvnCML7RI-4Q56iceoptFvZ-KV88Jjs488NPoKJ-4J0xejCcoF7nNjWqV_Db-jTNgMjEWZZc8Iv4pV6rKcQdNSI-NYt467nC9Fg22StYGCUej8bW8eflfJ8GcWc5CW_dicfkvGjd-NRaEsjy8oXMgf5ZypRz5EVwGVtod8BrKUqfo5SQ7B-Y3I5Re3pCsmv6LzDUP_koMI7zuc8F-wvQ4lnREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJ8YdG_I5v_nnzx6gT0zmZ-y6AxCPuOGuXyc-oX0I5TnPsbwSjduanEsK1nZdsoUXRw4tU6NI8uDn1PTzChyyinmNKhnHXwpts5r8-lawJOW6itzWX8F7-G7ZcstOAwsV9N4Ep4C1cFL6p9PZ-8kPJCv99t5H7XsZtfIHg5BbsoaXrVaDj8UlTKAxNs-W-0EJZuUa2NWdJTCdjUuInj4J2cSzFBC5I9WhGAFw3IuokIjDnLdurfwuFxBOtrAuVICef8Y9QBhPEl5iV842q6TpUy_mzvcnxbKphjJBTxJPcgkDYOH_A4mmOda5ieloBQk_pYZabfv7a5vcOmPmWkybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFxN1tovVz0p6sDbcTa-3VGQyFb7roFlPioGQqmbyHoFwAEwgwQ5XJuoLkn1j4r6UYTmxdbqfSb7uTkKyxX4YwunyRYPBro5H5wkAuoCHFxar1OR-31xmAiv0BY17Xy19WZh4rq1nSe6EjeLVCHNG4OGuQr7WaImQ35roaUot9MMEjM71XRTQ3VV73bsac5zlCEe3hZpCuek8z7EUV8uknVK_L6Byh9V0BWMPshDT85v_CL_S5tOYhhEnmUL73vRhMbY9wUY6d83yu5PxW5E5Q1VMcJoJeumfjclU7UXS0j5FJ1dwoH8PaJq2_UpQ5kd0Ar8hfhCuu80A85YdTeopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqC3PHt2u6O6Oa1frf7GF6yQ78spvOfaMLG1q8SosJN_YVtLW74L2cpaO1meAClVq-Sr7-5gmnraTpChYHesZpgAhKO8RVo1CigHC7LO4vNN48-Ry6KCStny5Lw4aNZscQnojH8031v6tbYCtP7e8uxa00j2vxL5UWEdZyetekSe-XSS-qEpCMYW0NC_sABhEqOA0XKkpC_OXJk5Bp14I3LAbKLkODIZpa_goKRXGocjKmPZioCrvIgPj78ZmHk4OBNQRm3PfgvI_UGe-v0SrT0BYO2tgiQ1oPJuP5EhJXHBHTLX-0tMwy15Mia4tmL2BIXsOFCrzjRNu6GkLXZi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMQGXGtHvgAtWI293YgGja0QLeXIX05gzOJoJ670zStmmSL4ED2n9Ddo01J7J0mGqd8yxETNvxzRxFcFMU5_ov6aBa9maynsEmQcYeGb4VXiG47i4J1khhVHTLVquFHWqpdqG2yBacLuRA3Rhgy2cpqIEG8UUvNoilnIMdS6h6RKEgXj4JtaZO7iHMlcB4DwkT5Xla00ByoKLMXmTN50Wsf94gDfEGUdW9KNTbImj4P5f3LjgaIrrzgGxLT3qqmXl9mgx42qP1sisxF4i-rSkr4Cxz3DAJ_J7wTo_A-c8qko5k5j326uHD46CIvgJzbbyA2fH9Te1oWKxt0ocfQtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rymv4ZWoPYdA-5IrqPDsxSdiJ-zCLtMIVPVrSBZMFYkcDOlTJw9diOIl2DoFfgmptlDL4XgVjrgsgGZrK4G3DZZGZnVQ5aGcc-sk_lwlMql6ytA-TLtX1t5-rBpSREdvZFlVaNiIg_qR1SiEf-xpDFr7Jp5Qcc9gfGHK1LIx1iAI2wZwfbldouNQCOM9W_KU5sC6trr_0kB3adM6Owh1n0OanV5xmIRpOLVx2HiRpR94GkACdoi6j-XtC8_Xd4Xjh-1SyfU3C4Q4XfaIH5N-W-vFtse2QAq7T69a2OG-0CPV-N2gfvTBiqrVrmJqSqES_ZAl8_Y5twTlBjDMHdfMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jI_6Xz_ckkJY6rxS6Gla_lbHoreCAwaO3oOPVC9L-hMX5ctM12sROoBtQqS0rs4Hg_z4iP1qmUJTF2ESdHl5I9yJRrAK7ul9XssVpS-ji-ekcianBAhZBTWN-QD6_xTuIVVe-E_XqPGn9BrQYylFrzVwkUydiao-mgZKpH7L4CIl1Yo46c8vLIvydNrGpDOUsUrCrrBlKfX636e4kSzNP6AjQJtcLSChZkfpDQoG1ukreG16hhWLRrNOzoE4ev8KCus5pLr6q09OgoUMuHHqXFESEZKrpsm4l_ryrS_I8bWxrODArRJWntfS3jcAoLc6e-hnvVpqPlWINJyuz6beRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
طواف پیکرهای مطهر خانوادۀ شهید رهبر شهید انقلاب بر ضریح امیرالمومنین (ع)  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448154" target="_blank">📅 05:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448143">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf867b1801.mp4?token=R001IhCLOxgjJ3DGK_warQynCEbwUDMeWmqdEinP7YhoF6QHEtuFWj0L_jOqIs2X8SW6YULlpanXh9d-sJ6-uGXR-Xr0RYy0MeJmQ4o1GSNJ0YNTxKej2m2f4A-nmbSzA3nfry9Vl0pRwNn8pslvETl3IvY6c2PPUH0nPLY41uXgmRe5kpW8-R6vL63rfAUCfg_8ARWARyfdvoiWdvbiVjLE7QdbyDJW4o-ki6F80gWxrBYZb1K1Y1IyZEQf5R_LUHBmM5rS3lO059XfxnLmS7oZbgj1uVDpBe5QHAO506Ib0EXQoHAo8hqYkenNvXVML6HrDraGd2IJeTHtLl65tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf867b1801.mp4?token=R001IhCLOxgjJ3DGK_warQynCEbwUDMeWmqdEinP7YhoF6QHEtuFWj0L_jOqIs2X8SW6YULlpanXh9d-sJ6-uGXR-Xr0RYy0MeJmQ4o1GSNJ0YNTxKej2m2f4A-nmbSzA3nfry9Vl0pRwNn8pslvETl3IvY6c2PPUH0nPLY41uXgmRe5kpW8-R6vL63rfAUCfg_8ARWARyfdvoiWdvbiVjLE7QdbyDJW4o-ki6F80gWxrBYZb1K1Y1IyZEQf5R_LUHBmM5rS3lO059XfxnLmS7oZbgj1uVDpBe5QHAO506Ib0EXQoHAo8hqYkenNvXVML6HrDraGd2IJeTHtLl65tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیل عظیم مردم عراق، دقایقی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448143" target="_blank">📅 05:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448142">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB_NZU48MszmLl5mPPhRMblUObYSL_HEGdjBtvn5mDU1ze3DIrfZJk71qcE_sputapmuu72XjS5GjdxGmXOyIwGjgZtUVzwl4yOQDXbjV2ib3rk3NGBSTAlqZr4YG9GcgMvIK469QkoGMQrO6jajJOelGlW9vumMoLOBwXaEQPU8tXFYpGZCRVCc0qUD4I2oYJ8tK4tSMUDD7s9OmyX3AOwNwtKsK6hLtHyNMV7qhcx5Bv0RcA0JKSedeOVR6h_0ocvV6fjbB0G5YuFabZqMzjw3jyqFEPKr_O5X3gNcAQ6O5irSih2FXX-HN7KYWpa3EGQxdNmhjkxzpbUPyKCOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
خیل عظیم مردم عراق، ساعتی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448142" target="_blank">📅 05:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyoFgmTAOReSoqdJbNh8deMf6JC9shXcxisvWZUl-E6H--6xEOnUHT2JES83j_OApbOAtKnFGj_kvQzbdzwahqz8zPn_d9Fs_EZTiTOlCUW0_fapi6QhHZQ4uwcGjNzvOm-LA1weStVMNeMrDAr_k9YKew8C4msemYKfTzQzETvbKPb8110Z957xwVCyrjUs-IdZfiD0-NgKHvcOoLZIaRHSI8IsTPFnWP8TILrIYcFsGI8LpBD3pZDSBRzt_dIKz1PV7TsC-K6xD-PdbvK0MDy2Cc0dR3po30FfhI5NQbh2ve2XggIn2WK0jiOfG-M9tyL7YHA2sKl-LxUq0m8MTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqf6ZpTSAl6TtOSNnVGSEQAx45F3goSgOW61Njv50C_vqt6c90wOZAEdUieNXe72TXxOc4bbECFpu9ybI1iLJa-nlU2fUkn18IEwJ0Kq6R8iGkZ-CIfO2wkjGnnC9zAUWTju9bq9kMVdC8oyjDmHx1U8M8Ex-iqZ6TJY6Jk5caJXpHFC-1YVe0iPbzpgnAZ_6d9qBwMvesVXaFE3DRkyg-QxfYDySYIGoX13I0AYdR6OLpDGuj40trTq-g5OFWiDZe8FjcN8AAvYPBr_8LaiW3A9l3NPL-zPpW2SSSy8pdN5BMspQXm7Il9pOzQLFSwrm_TI20AEoK1MC74YEjWpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyY9ScAkj85QBXv4ynXS_kNBSoXCrfa7rEuQWP6KJzHF7Jh9X6bAD_3_v0FnPMt07edYUlMRPAa6S1MkKANSEsSpI1IhrO5nO4VjSycHqW0Jh90dsW93E0DGWg2jPREtrD6DbnpK2RofNuQAqnD8gHWGS6cVq-OtPEvSHYKqRe6OqL21_rwHsi3SwXwL5YOlgBYLW5RexHJzXCmlkjLqXXs1SKj7w4JLqMvCG0RMEroolwe-6Uxg1khSxHp0g7huTAP5y4xj5syMqA3fPwRJm_s9T7bFDDSovxpW7nFMVAJDMZ-lC4A3qJMNLO9x9hF0AsuHjObBcasF72Eu5ovmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HWFkdncRsx8aNT9WkiNq3swGoxxpb54ud59SxyauRJgaS841ifQNdNZQU5K2whBWLBQ_vYmPuaawJeneUFPumW8h6bTd5_Ny2gvXMa2cgSKzvVxErH8dnXD9D4TV6NQyQS9mV9xFfTeN_B1Ez-6f5W2LDQ6KHLse5kWeqa6P0XvUhOabrz_QB-8SAf7jwmhaWkKiVk3Ql7cRwqT4U4OM3cb_log1EaTH_d9WznmD8BygZYoBaa6oeeFc3h5Sn5ZMq9pMP8ttXhppjDMtEAtouPsV9_525rASLDwTCqh2eB5ANuw7iygyK1f0IShqFTbbTySrYluWpowidyLhs-HLcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای نجف، ساعتی قبل از آغاز مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448138" target="_blank">📅 05:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سنتکام مدعی پایان حملات به ایران شد
🔹
فرماندهی مرکزی ارتش آمریکا (سازمان تروریستی سنتکام) گفت: «ما دور دیگری از حملات تلافی‌جویانه علیه ایران را تکمیل کرده‌ایم».
🔹
در این بیانیه ادعا شده است: «ما بیش از ۶۰ قایق کوچک و بیش از ۸۰ سایت را با مهمات دقیق هدف قرار دادیم».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448137" target="_blank">📅 05:26 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
