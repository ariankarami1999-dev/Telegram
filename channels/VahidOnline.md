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
<img src="https://cdn1.telesco.pe/file/EYXh92vXE81YccbZ2mtJ-CPwT7Zgfa05xpDNW68MSXnmQlWvjDc6KwVupMD4Roo_CODK38GTz8mNoTzRjB1F_Uhz1V-ibmnopJj0VFx02DAzfR5DkPxRVfsJ5IvDJy-ZicSzkrGXk3vtUaE4FYD1O0PgeHj8VIEaNsy0sSmC9xbNoClxgMi-eypOzinOesJ1M0rT7Pjrjq64sdNO5xZsnernL7qHWxt2I4yPP0-hLY_BnwbuPjmhAq5uiPsvWh1X1gpK4nTlbfY63p0eeEY4g6V7N1w2gupi_CU__I_iBdv-2wD4ldufUDxszm3I6-qYBpamKbQhmkANeutaEjPijQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 03:28:11</div>
<hr>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
امروز، «هیئت صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و همه گروه‌های مسلح دیگر در غزه دست یافت. این گامی عظیم به‌سوی صلح و امنیت پایدار است.
این توافق، گامی حیاتی در مسیر آن است که غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای کمک به مردم فلسطین، از نزدیک با هیئت صلح همکاری خواهد کرد. هم‌زمان، اسرائیل نیز از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به‌عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این توافق، نقطه عطف بزرگی در اجرای طرح ۲۰ ماده‌ای ترامپ است. این توافق در مراحلی که با دقت طراحی شده‌اند اجرا خواهد شد. هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات» با یک نیروی پلیس جدید فلسطینی همکاری خواهد کرد تا مسئولیت تأمین امنیت غزه برای ساکنان آن و همسایگانش را بر عهده بگیرد.
یک سال پیش، جنگی خشونت‌بار و مهارنشدنی، بحرانی انسانی و گروگان‌هایی در اسارت وحشیانه وجود داشت. ما پیشرفتی تاریخی کرده‌ایم و هنوز کارهای زیادی باقی مانده است.
می‌خواهم از میانجی‌ها—مصر، قطر و ترکیه—به‌خاطر تلاش‌های مهمشان تشکر کنم، و به‌ویژه از تیم فوق‌العاده‌ام که تلاش خستگی‌ناپذیرشان این دستاورد تاریخی را ممکن کرد.
تهدیدی که در ۷ اکتبر از غزه سر برآورد، اجازه نخواهد یافت دوباره شکل بگیرد!
بر اساس این توافق، غزه سرانجام در اختیار یک دولت جدید فلسطینی قرار خواهد گرفت که به مردم خود خدمت می‌کند.
این تحول شگفت‌انگیز را که همه می‌گفتند هرگز دست‌یافتنی نیست، به همگان تبریک می‌گویم!
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/VahidOnline/77661" target="_blank">📅 02:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_zOSFFYdp3U3iH1yGs7IWhbS7an6SjSAe_r8P2m548wyMuiKYvo0LOp6G5tq5zqKJ6l3-Sm4rOF_FNVrtykb3PPQ2jss2yhYegdj-GzOyXTTUYLnoUqUDlB8Kfh0X-GG2QMAdfivlG--LfaPE550hxpmbN9aByKoEwrF6HA0W_SA5f-M6lbwilj467-4Ml1uD1GBuZZCcT9qziZQHHb0IAPlYZzB6yA-SpsCv5J929BobitzmawUWreJKHTlxAvY9M2WVdMJB6_D6U4ryByih_MlzKu9owECSRS6S1ctClWOhDoPzGobnpeLIRLjQbTdlC3GDuVBgDaDLV3P6VvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس اعلام کرد افرادی که به سپاه پاسداران انقلاب اسلامی یا هواپیمایی ماهان خدمات مالی، پشتیبانی لجستیکی یا حمایت تجاری ارائه می‌کنند، به تداوم فعالیت یک سازمان تروریستی کمک می‌کنند.
او افزود وزارت خزانه‌داری آمریکا به شناسایی این افراد، افشای هویت آن‌ها و قطع دسترسی‌شان به نظام مالی ایالات متحده ادامه خواهد داد.
پیش از این، وزارت خزانه‌داری آمریک، شش فرد و نهاد در ایران، چین، هند و روسیه را به دلیل همکاری با هواپیمایی ماهان و سپاه پاسداران تحریم کرده بود. واشنگتن اعلام کرده بود برخی از شرکت‌های تحریم‌شده به‌عنوان نمایندگان فروش هواپیمایی ماهان فعالیت می‌کردند و در حفظ شبکه بین‌المللی این شرکت نقش داشتند. وزارت خزانه‌داری آمریکا همچنین شرکت «استودیوی استارت‌آپ داده‌نگار» را به اتهام همکاری با سپاه پاسداران تحریم کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/VahidOnline/77660" target="_blank">📅 02:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
مصر دوست و شریکی مهم برای ما در منطقه است و امنیت آن برای ما از بالاترین اهمیت برخوردار است.
همه ما باید در برابر توطئه‌های اسرائیل و عملیات‌های پرچم دروغین که برای تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.
تهدید روشن و مشترک است و از همبستگی مسلمانان هراس دارد.
araghchi
پست قالیباف:
ایالات متحده هر روز دست خود را به جنایت جدیدی آلوده می‌کند؛ حملهٔ تروریستی به منازل مسکونی غیرنظامیان در جزیرهٔ قشم، ادامهٔ جنایات در میناب و لامرد است.
امریکایی‌ها عادت کرده‌اند که سیلی‌هایی را که در میدان نبرد می‌خورند با ریختن خون بی‌گناهان جبران کنند. تاوان‌ خواهند داد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/77659" target="_blank">📅 23:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJWf8wUIIAlqx4IBJdW_ic8Ght_0g8-kgjHjQiTC4sbQYm42hPB9PE5IucTQgDnYOv7Q3C2CuSLmSFzVG7hDqTm_2u0bW98zOIIfigebz4DVU3Wjyd-bBgYcXIkQfXhVZgt84ERnTxjInH4Ij6mjlpl658AoIZTaOSqI_Grtq37CAmCZLAtN6HG90IExEgYd1PVk0izx2CRjiqW3RTxBPbXsEMpT1_oRSxQbZkgsEIVKjWOe3fMd6eUoklbBVWFhpAcilwE0HcrUxff6xNxfLVY3Q7zUwer7dF8jnp8V_BYR_KgRoi54DfPNhG3Cdz5oKzi3TIa5NEJ61_CeHIurEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی روز پنج‌شنبه از طرح تشکیل یک ائتلاف بین‌المللی برای دفاع دریایی با هدف حفاظت از کشتیرانی و مسیرهای انتقال انرژی در دریای سرخ خبر داد.
وزارت دفاع عربستان اعلام کرد نمایندگان ۴۳ کشور و اتحادیه اروپا در نشستی درباره این طرح شرکت کردند. بر اساس این پیشنهاد، عربستان به‌عنوان کشور بنیان‌گذار و رهبر ائتلاف عمل خواهد کرد و مقر آن نیز در این کشور خواهد بود.
به گفته وزارت دفاع عربستان، این ائتلاف با هدف تقویت امنیت دریایی، حفظ آزادی کشتیرانی، تأمین امنیت مسیرهای تجارت و انتقال انرژی و حفاظت از منافع مشترک دریایی در تنگه باب‌المندب و خلیج عدن تشکیل می‌شود.
این طرح پس از آن مطرح شده که حملات حوثی‌های مورد حمایت ایران به کشتی‌ها، یکی از مهم‌ترین مسیرهای تجاری جهان را با اختلال روبه‌رو کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77658" target="_blank">📅 22:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=IxuYotTwSJf0iINL_fjOnPyXumWGBCyU883R9I_lpe9rwfNVDPEsfgXWtcFCc0B3bjIoK5ZKJRIBmjkXWV895comJVHuETa-lnwZCRNXGAvbRuoXGrnbWxVCtPL0lgE6se1kEyt8hJ0b0MJFsal7cC4XdpzzQP-BcuOZz8INsDRb5kuKNB6Tu0TqdunbkdfXc8WE4cyB2f8-YIIm5GCG9OnMcJglUfs0mhLoqSrR27lwdKIPZDKQM861uzRXYTtKHUlAUl61gQScQXbaNSEQ5Vy3dtsnbekLxGAVre2uMND5RXUU3LJZDEFIbnvRBzyt6jGlbQjwD25WZIQrU8TzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=IxuYotTwSJf0iINL_fjOnPyXumWGBCyU883R9I_lpe9rwfNVDPEsfgXWtcFCc0B3bjIoK5ZKJRIBmjkXWV895comJVHuETa-lnwZCRNXGAvbRuoXGrnbWxVCtPL0lgE6se1kEyt8hJ0b0MJFsal7cC4XdpzzQP-BcuOZz8INsDRb5kuKNB6Tu0TqdunbkdfXc8WE4cyB2f8-YIIm5GCG9OnMcJglUfs0mhLoqSrR27lwdKIPZDKQM861uzRXYTtKHUlAUl61gQScQXbaNSEQ5Vy3dtsnbekLxGAVre2uMND5RXUU3LJZDEFIbnvRBzyt6jGlbQjwD25WZIQrU8TzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر جاویدنام آیدا حیدری، جوان معترض کشته‌شده به دست حکومت، در سالروز تولدش بر مزار او می‌گوید که آیدا حیدری «شیرزنی» بود که جانفدای میهن شد.
آیدا حیدری، دانشجوی رشته پزشکی دانشگاه علوم پزشکی تهران، در ۱۸ دی‌ماه ۱۴۰۴ در تهران با شلیک گلوله جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77657" target="_blank">📅 20:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=QMjnISnyFffqY1t1ap_C4oihpOfpoDGi4Ryv_dZtEPzqIJXE8O7WXemyYXngJQxd5kX8IpaBQMv7d7-gY4Bk8JWJ_anPlieqbnLyMR-xFkLJGaIYdRyiFWlLZxYZ6svL8G_KaeoZnhzGqehzTrEO9cPV6gzaMYiiS6VvDUadvcLBdicoyfwgipEJhwW9FAfOTNkJpXykJPFjWlrciJSW-Pc750t0VOC-EIhKkw-7HbBko31P4r0k4bye6R_LF7T0WIH-OscHCBd2pG0hMFlPkzRv1iLCM1S1iL4EDk59SAoYhe0vfsJ2XxB3cgstHnpYcSvf5fBZz-8D3eTdC0t19w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=QMjnISnyFffqY1t1ap_C4oihpOfpoDGi4Ryv_dZtEPzqIJXE8O7WXemyYXngJQxd5kX8IpaBQMv7d7-gY4Bk8JWJ_anPlieqbnLyMR-xFkLJGaIYdRyiFWlLZxYZ6svL8G_KaeoZnhzGqehzTrEO9cPV6gzaMYiiS6VvDUadvcLBdicoyfwgipEJhwW9FAfOTNkJpXykJPFjWlrciJSW-Pc750t0VOC-EIhKkw-7HbBko31P4r0k4bye6R_LF7T0WIH-OscHCBd2pG0hMFlPkzRv1iLCM1S1iL4EDk59SAoYhe0vfsJ2XxB3cgstHnpYcSvf5fBZz-8D3eTdC0t19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
در چند ساعت گذشته، رسانه‌های دولتی ایران همچنان ادعاهای دروغین سپاه پاسداران انقلاب اسلامی را منتشر کرده‌اند؛ به‌ویژه سه ادعای زیر:
🚫
ادعای نخست: سپاه پاسداران بار دیگر ادعا می‌کند که مسیرهای آزاد و باز عبور از تنگه هرمز برای کشتی‌های تجاری خطرناک است.
✅
واقعیت: خطرهای فوری برای کشتی‌های تجاری و خدمه غیرنظامی آن‌ها، تهدیدهای لفظی و تلاش‌های سپاه پاسداران برای حمله به آن‌هاست.
🚫
ادعای دوم: سپاه پاسداران مدعی است سه جنگنده رادارگریز اف-۳۵ آمریکا و سه هواپیمای دیگر در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✅
واقعیت: در تلاش‌های اخیر ایران برای حمله، هیچ هواپیمای آمریکایی منهدم یا آسیب‌دیده نشده است. همه موشک‌ها و پهپادها رهگیری شدند یا نتوانستند به مناطق هدف برسند.
🚫
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام M/T Nora محاصره آمریکا را شکسته است.
✅
واقعیت: این کشتی تجاری نتوانسته از محاصره «دیوار فولادین» آمریکا عبور کند. بیش از ۲۰ ناو جنگی آمریکا، صدها هواپیما و هزاران نیروی نظامی همچنان در آماده‌باش هستند و اجرای کامل محاصره را ادامه می‌دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77656" target="_blank">📅 19:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cridu3KjSF2B_fJAD4bveGFZC6kwlVhIiWtX-8a0VuSsnppbTPLXcgijPEEccABgHBO0zVrx4aLo6sFigmZ_QHSyabJhha5zmSnwZsUP0fIZHWQFIYX5kYN7RMEIA99-yPhhOSOZM25xtgNDLyCySu_hVVUImm7N8yOzZEJJxn57jcgarIgu3lnD5Wwc74pcTsQicpfd3RT4u4XsSN8zQJWcHimtfsEIx3LNDMNgrfg4BYYWOpXTn6citiHkym5Is-90SRpHaC7YL7AE0AikyjPyWWVkSQ3kglWh7Rdyt_3DPkT88LargZPvKlbf2tQQl8byjdX3Mh2KXImhcZwabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=oWePPu0NzfULBlPyLIzthhyXOzH25bsyusY1BMjHMUYk_hp59Z9RA21d5whAX0Q5oKUsLRRVASBZY1o2LWhACgBd6rPK0y2KTyrxkRA5MiNNw4YqLR7JA1YTKVTOdK5858GBh00BMbc_EKZmJPrm-7U7tQs53NI5lxKAg9CAbZDTM0k5c_8r5SWvyiseLjKZl7cyfimIZRW7MdUd5ItO17oYpQ22Ny-_Aa5Xgq6bSfMWxG4BQbbheXxbx_5g1njnNVv6zSf48gdBI9182xP8N8E8v-fLt9SifPSaWyaR9yt2SFkZBK9XwuIxeEjrSWySTvfQtihKYdU4NowePZqvyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=oWePPu0NzfULBlPyLIzthhyXOzH25bsyusY1BMjHMUYk_hp59Z9RA21d5whAX0Q5oKUsLRRVASBZY1o2LWhACgBd6rPK0y2KTyrxkRA5MiNNw4YqLR7JA1YTKVTOdK5858GBh00BMbc_EKZmJPrm-7U7tQs53NI5lxKAg9CAbZDTM0k5c_8r5SWvyiseLjKZl7cyfimIZRW7MdUd5ItO17oYpQ22Ny-_Aa5Xgq6bSfMWxG4BQbbheXxbx_5g1njnNVv6zSf48gdBI9182xP8N8E8v-fLt9SifPSaWyaR9yt2SFkZBK9XwuIxeEjrSWySTvfQtihKYdU4NowePZqvyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی قدیمی منتشرشده در شبکه‌های اجتماعی رقص علیرضا سپاهی در اصفهان را نشان می‌دهد.
قرار بود او بامداد سه‌شنبه اعدام شود اما پیش از انتقال به محل اجرای حکم دچار سکته قلبی شد و به بیمارستان الزهرای اصفهان انتقال یافت.
@
VahidOOnLine
یک شاهد عینی گفت پس از انتقال علیرضا سپاهی، معترض محکوم به اعدام، به بیمارستان الزهرا اصفهان، فضای بخشی از این بیمارستان امنیتی شده و شماری از ماموران امنیتی در آن مستقر شده‌اند.
بامداد سه‌شنبه، ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو نفر دیگر از بازداشت‌شدگان اعتراضات ۱۸ و ۱۹ دی‌ماه ۱۴۰۵ در اصفهان، با حکم دادگاه انقلاب اسلامی اصفهان اعدام شدند. ابوالفضل سپاهی بادجانی، پسرعموی علیرضا سپاهی بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77654" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebec49421.mp4?token=gDh8ruyLQazXBeefOqfZKBK_0uCmLRlC1JjforFp756fFdbM0PU7SvcbHKB-MS90H3874du5jySRiISv-TXJWmfaBFbr7Mu6_JIlxqaY3cq7WvJYDaFAUFE4Tx8cmCmOvktmSxg8ucq4NhIHXNGXqYAts-eI098QCgkuzcpoF5BiERgTF93jsLvidY3lQRWNEPhqSdrPnCfUNEiDb7nr8V29qIoiMn6jGrYdDiOYENdh9p9V4oDSuklUkxtzv3Xd6zydkI9phWqWXLQqgZlXt8ROMgvcTxPQvw6qhsXFoP9T6rIoJeDYtWrqbbCRLk4TvFIpvJUYGVhFbmNKKl2wQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebec49421.mp4?token=gDh8ruyLQazXBeefOqfZKBK_0uCmLRlC1JjforFp756fFdbM0PU7SvcbHKB-MS90H3874du5jySRiISv-TXJWmfaBFbr7Mu6_JIlxqaY3cq7WvJYDaFAUFE4Tx8cmCmOvktmSxg8ucq4NhIHXNGXqYAts-eI098QCgkuzcpoF5BiERgTF93jsLvidY3lQRWNEPhqSdrPnCfUNEiDb7nr8V29qIoiMn6jGrYdDiOYENdh9p9V4oDSuklUkxtzv3Xd6zydkI9phWqWXLQqgZlXt8ROMgvcTxPQvw6qhsXFoP9T6rIoJeDYtWrqbbCRLk4TvFIpvJUYGVhFbmNKKl2wQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار خانواده جاویدنام محسن رشیدی خانی‌آبادی و علی ایازی با خانواده عرفان اسفندیاری و امیر حسین صفری ـ گزارشگر (ویدیو صدا ندارد)
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/77653" target="_blank">📅 19:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY6xQsuPa657VL39d8uVOgYVq7kN_jK_lxogcHwfAfp90P3GzyFYDz5ASG9ln7EvJmQ-0ys6C4pSYWugSf3BqQlTxua9eWj81SAG28aa2Ux_gM5NLOlBPVwadqu5SptHkkEIf99jzPBq0fc8ZIm5YnCW_6VoyVO6pDN_r8gNot-KMxtRfjR9L00gE7hkPzbhbx-JHi70T0ndH-eP_y965WmyAst359Q_KTVxawpFSpeZsbOAxHIEhNznL2ANFHoSYnkKwJV7IhITuI8F3fga2G6viwWce4FPvsdyHzDo-3JGEshogjMGdoImL5r_1aEpXxu7Np2wYBUY_J_cY71WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ان‌بی‌سی نیوز روز پنجشنبه هشتم مرداد، به نقل از یک مقام آمریکایی گزارش داد که دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در جریان نشستی در هفته گذشته از فرسایشی شدن جنگ، محدودیت گزینه‌های نظامی علیه ایران و دست نیافتن به توافق خشمگین شده و بر سر مشاورانش فریاد کشیده است.
به گفته این مقام مسئول، بر خلاف اظهارات عمومی ترامپ مبنی بر رضایت از روند جنگ، نه او و نه مشاوران ارشدش از وضعیت موجود راضی نیستند. یکی از متحدان ترامپ در این باره گفت: «رئیس‌جمهور کلافه شده است؛ او تصور نمی‌کرد گرفتن امتیاز از ایران تا این حد دشوار باشد و هیچ راهبرد مشخصی برای چگونگی رسیدن به نقطه پایان وجود نداشت.»
این گزارش می‌افزاید نبود شفافیت درباره اهداف نهایی واشنگتن—از جمله این‌که آیا هدف اصلی جلوگیری از دستیابی ایران به سلاح هسته‌ای، بازگشایی تنگه هرمز یا نابودی برنامه‌های موشکی و پهپادی ایران است—برنامه‌ریزی برای پایان جنگ را دشوار کرده است. یک مقام آمریکایی تصریح کرد: «ما پیروزی‌های تاکتیکی متعددی داشته‌ایم، اما بدون داشتن یک راهبرد روشن، با یک شکست راهبردی روبه‌رو هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/77652" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrbHlq5aOGgFbQCjBI77Sd0iMqcDIMkbUW5tFShINhUKcFwE7rK-HTcATjUTCgAR4rt9TbAvviWPfX336F3TQHN-5ErGLffmQYFKBcb41xw6J1vRqUyg5t0G8ZTyi3M_4XPcjqFw8zawTHNRChp-ytFynN0vdT9-vebT_Y6hkD1LfupEPE-5WTWv77_iMH9wsnAjQJtRi_WBwh-rn04tcVswx8B36uq4Fyy9Y5oT5XcOyh4nqHOgRGnQ5dOmxvFi6eNBVnKfPCSN_1PUOTwu9rCdXTs6ZpVoU8cCo2ke05Pj16VGyOnCO13rVUGWBPrSTdkPDIRKNXbpUNFUd63ipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌وزارت دفاع چین گزارش‌ها درباره برنامه آن کشور برای تحویل صدها سامانه پدافند هوایی دوش‌پرتاب به ایران را رد کرده و آن را «کاملا نادرست و خلاف واقع» خوانده است.
جیانگ بین، سخنگوی وزارت دفاع چین، روز پنجشنبه در پاسخ به پرسشی درباره این گزارش گفت که ادعای مطرح‌شده صحت ندارد. وزارت خارجه چین نیز پیش‌تر گزارش مربوط به این معامله را «بی‌اساس» توصیف کرده بود.
رویترز روز چهارشنبه به نقل از سه منبع آگاه گزارش داد که ایران قرار است ظرف چند هفته نخستین محموله از مجموع ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل ساخت چین را دریافت کند. به گفته این منابع، قرارداد مورد نظر شامل موشک‌های کیودبلیو-۱۲ و اف‌ان-۱۶ است و ارزش آن بین ۶۰ تا ۷۰ میلیون دلار برآورد می‌شود.
بر اساس این گزارش، قرارداد با یک شرکت مستقر در هنگ‌کنگ امضا شده که گفته می‌شود میان ایران و تأمین‌کننده چینی نقش واسطه را ایفا کرده است. منابع رویترز گفتند که قرار بود محموله‌های اولیه از شهر ارومچی در غرب چین ارسال و از مسیر پاکستان به ایران منتقل شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/77651" target="_blank">📅 19:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BaxP5WNz5fPoLux08cPHxsDWE0zojoES1qiGkLZeR3RQs_QmKhPsHhdA0fXGgOlG4pjDhkii83QbhsYEw_fCo-ilN2KGflS2ZvFKzOz9bB4YYTTe0OUt7AoAkREQKrAnxLxF5GgluNh1Po6qrevKbQ-E796Bu_KOQRfF9bJWxv97cn_i_Hsz2fgIQqIte_ipouDO0q5jqtj9pM48xD95lB0Q_0q6rX3dj7m1y6jspNq8yHzkUmcAbbMqyKUNl7V4v9MAdSFvaTU6t7_2zTak-2YuNPrVYlxBzJ8-3WRcmmyADZYh70UiUprlubqHBmwxlEOp944nivlcbRGbRmXPtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kPkL5ETWv1DV7N4uY9U4Pfm6G89Fo6CrEcBNQy9S_8TWdrlHqAkcuX__pjIt0YMmA-2hrTVHtlLbIhu1v0yW9-B1E2U-g4Y4sT0HpADvU6-v2JmjEj0YuM6VqCWAaotUVWgQkNGPz3ml3G2isEcho__ZtrxYv5wrpTbuJBNp2Q4acyvmM8G12K4II8AzeWhA4wJuF_g83RYDOVwZ4WYWCuNR7C1fvZ9k4Lm20K9ADaa7M2Rpc0MslR3vd-9moq8z73DoFObB_7R-3Ey7j-XoXL8-z9JLw5JkzUWoZICcGT3IucW-Zxfo6v6wJQFJDd1kcKFCPCJ9cjsRwbaAfdp5YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: با شکاف عمیقی که پس از کشتار دی‌ماه بین مردم و رژیم ایجاد شد؛ حکومت ایران در نهایت سقوط می‌کند
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در پاسخ به مجری ای‌بی‌سی که به او گفت طبق گزارش نیویورک‌تایمز شما به ترامپ گفته بودید که ظرفیت موشکی حکومت ایران ظرف چند هفته نابود می‌شود و تغییر رژیم ممکن است رخ دهد، گفت: این ارزیابی اولیه من نبود و این بیان نادرستی از آنچه گفتم است.
برآورد من این بود که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای اقدام کنیم.
نتانیاهو گفت، من گفته بودم که می‌توانیم شرایط را برای ضعیف‌تر شدن رژیم فراهم کنیم اما بر عهده مردم ایران خواهد بود که سرنوشت خود را تعیین کنند.
او درباره احتمال تغییر حکومت در ایران گفت: «فکر می‌کنم ایران از همیشه ضعیف‌تر و اسرائیل از همیشه قوی‌تر است، اما نمی‌توانم بگویم رژیم هم‌اکنون فروپاشیده است.»
نتانیاهو گفت: بگذارید یک پیش‌بینی کنم؛ پس از چنین شکاف بزرگی که به دنبال آن قتل‌عام (کشتار ۱۸ و ۱۹ دی‌ماه ۱۴۰۴) بین مردم و رژیم ایجاد شده، فکر می‌کنم که رژیم ایران در نهایت سقوط خواهد کرد.
نتانیاهو هشدار داد اگر ایران، اسرائیل را هدف حمله قرار دهد، «اشتباهی بسیار خطرناک» مرتکب خواهد شد و اسرائیل «بسیار شدید» پاسخ خواهد داد.
او در پایان گفت: «هدف من این است که مطمئن شوم ایران با این حکومت به سلاح هسته‌ای دست پیدا نمی‌کند. این موضوعی است که من و رئیس‌جمهور ترامپ هر دو بر سر آن توافق داریم، زیرا در آن صورت جهان متفاوتی خواهد بود.»
@
VahidOOnLine
نخست‌وزیر اسرائیل روز چهارشنبه در گفت‌وگویی اختصاصی با لینزی دیویس از شبکه ای‌بی‌سی نیوز تأکید کرد که دونالد ترامپ تصمیم‌گیرنده اصلی درباره جنگ ایران است و او تلاش نمی‌کند ترامپ را برای ادامه حملات علیه ایران متقاعد کند.
نتانیاهو در عین حال گفت نسبت به امکان دستیابی به راه‌حل دیپلماتیک با جمهوری اسلامی تردید دارد.
او گفت: «نمی‌دانم این احتمال کم است یا نه، اما نسبت به شیوه عمل ایران بدبینم. آن‌ها همیشه دروغ می‌گویند، تقلب می‌کنند و زمان می‌خرند. آیا تحت فشار کافی ــ فشار دیپلماتیک و اقتصادی ــ ممکن است این رفتار تغییر کند؟ می‌توان امتحان کرد.»
او افزود: «واقعیت این است که ما شریک و متحد هستیم. او شریک ارشد است؛ فراموش نکنیم که او رئیس‌جمهور ایالات متحده آمریکاست و من شریک کوچک‌تر هستم. اما من نخست‌وزیر اسرائیل هستم و هر زمان لازم باشد از منافع و امنیت کشورم دفاع می‌کنم.»
نتانیاهو همچنین از نقش دولت ترامپ در مقابله با «دشمن مشترک» قدردانی کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/77649" target="_blank">📅 19:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY3AMZBr2q0rgHPe9SyDObIkrXT-iHKqPTwbppkwX9WPCy48YMZBn8PGi9Dl4QaAKxUZNeL1evXQT85_u7VkC37r3ulpMk6tOxfvGzHtMXje_uGmKm3nTsTo73FY8b9WBbzvPrsyG_y-PZcxhr6Dt0moTSsNb1e7LfU8kxEwidxoBctn3_XPlTcCKHRl_D3uche3dKm5fZQQSAY9kYdx3rbbbt4LPK01WDe6gnFZVVAsFlYG8XDkle2Hh5q-HJk8N46kDAunKzG27RBdQ4LJXATnRcGiKb8SHJifFaTcMSK3LjoPzklHEVr99zXwhqn5bsijP29T9vg2hKHI80FV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار ویدیویی از ضرب‌وشتم چند زن در ایران در جریان یک پخش زنده اینستاگرامی، موجی از واکنش‌ها را در فضای مجازی به دنبال داشته است.
به‌ گزارش خبرگزاری میزان، وابسته به قوه قضائیه ایران، پس از انتشار ویدیوی این لایو اینستاگرامی با دستور مقام قضایی برای این فرد پرونده تشکیل شده است.
سعید راستی، معاون بخش «مبارزه با شرارت و جرایم خشن» پلیس اعلام کرد که این ویدیو باعث واکنش گسترده شهروندان شده و اطلاعات ارسالی مردم در شناسایی متهم نقش داشته است.
آقای راستی اضاف کرد که این فرد بامداد پنجشنبه، ۸ مرداد ۱۴۰۵، «در عملیاتی» در مرکز تهران شناسایی شد و «به دلیل مقاومت در برابر ماموران» دو گلوله به پاها و یک گلوله به دست او شلیک شده و در پی آن بازداشت شده است.
هم‌زمان، ویدیوهایی از این فرد پس از بازداشت در شبکه‌های اجتماعی منتشر شده است که او را در یک مرکز درمانی نشان می‌دهد. در یکی از این ویدیوها، او در حضور پلیس از زنانی که در ویدیوی ضرب و شتم دیده می‌شوند و همچنین از  شهروندان و پلیس عذرخواهی می‌کند.
@
VahidHeadline
دیروز بارها اون ویدیو رو برای من فرستاده بودند و می‌خواستند پخش بشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/77648" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXqM-DK97Nori2HuGML2uiIKtvRm5XOtNWJ92HddlqUXeCS_sm3FazeOFNr80w4GDN_3-kFBnyEYJM_yQS1bSpaBlUmcNdGClFRob7VGtSLbaA6sU7EQgcALrtw_IUSoawTE0hzgJrPMNZs5RAr0P65jcqFgF1spyY1aMHDNOTVMes5fseiMoiYD57kihH_ba2drMEjlbVpF7Ji9kZGCB5uJZ6u2Xrp1uBo5tmUXLlvLDbg36Ml2ZN6DFhXMH5rgHCGBzTj5_Df7jHdGHeuujf0C00ztk-rfPu6bvLV9afcDO7nc5uQTFqQWEvCIyJkLhlY8Z-xICkM3UU2SfBkcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی (آرمین) جنت‌خواه، فعال شبکه‌های اجتماعی، برای اجرای حکم قطعی سه سال حبس بازداشت و به زندان فشافویه منتقل شده است.
بر اساس این اطلاعات، آرمین جنت‌خواه روز ۳۰ تیر ۱۴۰۵ بازداشت و پس از انتقال به زندان فشافویه، اجرای حکم سه سال حبس او آغاز شده است.
اتهام منتسب به او در پرونده قضایی، «تحکیم مواضع اسرائیل» عنوان شده است.
جنت‌خواه پیش‌تر نیز در دی‌ماه ۱۴۰۲ توسط نیروهای امنیتی بازداشت شده بود. جزئیات مربوط به روند رسیدگی به پرونده و نحوه صدور حکم او به‌طور رسمی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/77647" target="_blank">📅 19:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMhxxC_M8j4bnfe02RUS15Uw4wr4U3t_Lv-UkStZWcf4Tn5YaRphxwC_MVSk_1LenO9KodHfjQ51QI-LVChgSjsxjmRiAkLEpia8icRM3Ld1wONYrvWx4anfAXST7_v8gEltAZDx6NK27iTQ7uZs_GUw2kF5RJzjBYCWXU9p-iGcKSb_e88wN-B6gYcdmjKDCtT-1hmIEsJqJgM47Br52VIZG5qRbYmJ_J4uxAo4BKE8nC5ZIWdsCk-gaPHJbIl5lJuAe_7Pwe7CVu8QMgWiatodkgQJ15-g0ZaEsOEU3d9YOPdRgLV5xwisY0YGYkWz-1J-AesjzlZ6ow84lIcb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران زنجان با انتشار بیانیه‌ای از کشته شدن سه نیروی این نهاد نظامی در حملات بامداد پنجشنبۀ آمریکا به نقاطی از ایران خبر داد.
در بیانیه روابط عمومی سپاه استان زنجان، به‌جز اسامی این اعضای سپاه پاسداران، جزئیات بیشتری درباره محل کشته شدن آنها و درجه و محل فعالیت‌شان اعلام نشده است.
این در حالی است که تا ساعاتی قبل، رسانه‌های ایران این مناطق را به‌عنوان نقاطی که هدف حملات بامداد پنجشنبه قرار گرفت، اعلام کرده بودند: «اهواز، آبادان، بندرعباس، قشم، بندرانزلی گیلان، کازرون و فراشبند استان فارس، چغادک بوشهر، شادگان و اروندکنار خوزستان و جزیره کیش»
@
VahidHeadline
پیام دریافتی بررسی‌نشده: در خود زنجان کشته نشدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/77646" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfTY0mjZXH02rdUddGtbkKwPn59CJEvJnBjfcyivQ9iibbEbMOSwqo80RLdl2v-ArWfMQwsIJcMHi-hevrzN4HAXrFW72jEe7_EsEZ9fsrI1iscNPUwyBKWNeeVg_B2MwDKrYvHFdXoMc5mSQcjmFwcuSLct22KjLb0Rq9xkezPQtNwAY6FWQOJMEWy2XneV66J9zIDuj7XRfLQ5E2IemsvvKPYdLt6DuWqRG9iVtvXeTgLuRZNhXbNPDbFmWzgh41gqBNJUVeWQNJEPsykyIqjQswMP5LjqPEbE-WpvqXxyOA64LkX6nTjPGOij7Cl1IiFtT5YBGHibbsr2Y7VDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران ادعا کرد که در حمله به پایگاه الازرق اردن «سه فروند هواپیمای اف۳۵» را از بین برده است.
سپاه پاسداران در بیانیه خود ادعا کرد که پنج‌شنبه هشتم مردادماه، با حمله به محل استقرار و سوله تعمیراتی جنگنده‌های اف۳۵ آمریکایی در پایگاه هوایی الازرق با چندین فروند موشک بالستیک، «سه فروند هواپیمای اف۳۵ را به کلی منهدم و به سه فروند دیگر خسارت سنگینی» وارد شد.
سپاه همچنین ادعا کرده که در این حمله «چند افسر و کادر فنی و تعمیراتی» کشته شدند.
این ادعاها در حالی است که پیشتر ارتش اردن اعلام کرد که پنج موشک شلیک شده از سوی جمهوری اسلامی را در آسمان این کشور رهگیری و منهدم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/77645" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhSyumxUDcoK1J2NAlBENQKpnFJm29jM_5AMJFcH1vUBpotLu2mIuJmxhaBBSp0emJsjmnOVkVUjhEbHADxkSrPiE0yTOxWkXbtWBqQiAtaJSSymBPxg1GwYWwZywFqMtPienbHYe_l3ceaF91saNfPGDcLv3QTbOfWk3digyFDpk8Er3ehh7PdsvhEZUj_964cgeGvvO5SzeSAP4aVAsIqSTN0XF3zTdDHVwWdmvlo7DuHarpKBJ34Y1v7TrdqGain-qq7hqCBPtX6jyRgFY3m87dzoQXlqS5c_wVA-Qby1OR8unxZRiLGbDmZfTnuzWAu1DsxALrksITJV4uJaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه ۴۱ دیوان عالی کشور حکم اعدام بنیامین نقدی، از بازداشت‌شدگان اعتراضات سراسری دی ۱۴۰۴، را که پیش‌تر از سوی شعبه اول دادگاه انقلاب شیراز صادر شده بود، تایید کرد. وکیل او می‌گوید با وجود ابلاغ این رأی، درخواست اعاده دادرسی به‌زودی به دیوان عالی ارائه خواهد شد.
بنیامین نقدی شامگاه ۱۳ دی‌ماه ۱۴۰۴ در جریان اعتراضات در شیراز بازداشت شد.
بر اساس گزارش‌ها، علت بازداشت او شعله‌ور کردن یک کپسول آتش‌نشانی در مقابل نیروهای انتظامی عنوان شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77644" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eL0JfetPv9oJTLhOEl9X02swtMHWNeH2aCjbCqTxRXh-dPdfZy7RkJvC7jBbs1Wo2Rq4yOveidSiWOmE4fDqbsQLK-KtnjS9Jg4exlv59BzXsvJTS8lPfZ3IlhhwFFgq04nJSbnrkA3Toc9hmeIW0KOOuL6lNAdUmwJpaJHMW99UdmMSUxPEIYQaftD-n6LntsnDp9uFv-Qkg9jb5UQrpCWLedEFIhrcG8z_SCC6H6PkTpRNFsmExMuerr6yjTxSOuOTT73aXf7wXjlM5sDN1NfXRvzVs--rLZXRPKyraBhPdmOdsPmYUVtgDHxbGzMHuTdJwyVMgfdI4rI6ui0YCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: آتش‌سوزی پس از حملات آمریکا به نقاطی در
#اهواز
پنج‌شنبه ۸ مرداد حدود ساعت ۵:۵۰
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77643" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0XSEXaCj3hzIa8LIIAwDPdlMN7Oss31gut3wBBqsNiPFMl-XpA6DBD1KFSOqQn-4_eD6p6q8Pf5x0McbGm00ARzxqfFwuMAg5KyrCz_da0W467gUstcmaPCIlsuRnx3Vd0svg2WV_X8JRckUTnC2g6HjGDf7KG5DUZ0c0CJkPht9gx7iPgrSrDJyo47To_yK4TZ699Cky8teZIBBVtKZGkY_8HP_y8ybHdq5rDDtnr-aa6BnmdxpUwJ6dALqI1uCesF0XswFo-fAdU3x6QB6_WREbC0_nPJLZV0g503OxqX8HV5KN5OgvpzKLDXaA9YUFpgvm2AvGLfDWLlKmywqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اردن صبح پنج‌شنبه هشتم مرداد از مقابله با حملات موشکی ایران خبر داد و اعلام کرد پدافند هوایی این کشور «پنج موشک بالستیک» شلیک‌شده به این کشور را رهگیری کرده است.
سپاه پاسداران روز چهارشنبه نیز باوجود توقف چند روزه حملات آمریکا، به سمت اردن موشک شلیک کرده بود. پایگاه‌های ارتش آمریکا در اردن از ابتدای دور جدید حملات متقابل آمریکا و ایران از اهداف اصلی حملات موشکی و پهپادی سپاه پاسداران بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77642" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=vAaToC_UlH-EN8euOQe14qqLFs-wfcBihBpMrr5CprOwgmyHYILyqXpRCBGcqcqX5n_i3qiN9cMDke2KQAkr7M_iqfBYP3tfOq5zwBK5kGjCwoZAmtypOZHe6Wxr-wTtftVKjkDgqGFcXEQzE1XeoQLhQYDX9tvWGgBl6ouEVHr7rAci6FXssyfAgW-4dObqyFt6FyDnClgOP5FWMjEfcd8FINa0Wy3htZMBV1_EaZBUCBnHfVwc2-QWqbEQuborI2vlnRRO8mO2Mz2Ii0KYr-M2m4UtUbKVLqpv9gBgyeg07JGU_ByFiHrcDT4SqZTJscmFlbQApGHbQ4R58bZ47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=vAaToC_UlH-EN8euOQe14qqLFs-wfcBihBpMrr5CprOwgmyHYILyqXpRCBGcqcqX5n_i3qiN9cMDke2KQAkr7M_iqfBYP3tfOq5zwBK5kGjCwoZAmtypOZHe6Wxr-wTtftVKjkDgqGFcXEQzE1XeoQLhQYDX9tvWGgBl6ouEVHr7rAci6FXssyfAgW-4dObqyFt6FyDnClgOP5FWMjEfcd8FINa0Wy3htZMBV1_EaZBUCBnHfVwc2-QWqbEQuborI2vlnRRO8mO2Mz2Ii0KYr-M2m4UtUbKVLqpv9gBgyeg07JGU_ByFiHrcDT4SqZTJscmFlbQApGHbQ4R58bZ47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77641" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nf4UsWh5ihDl9MFxITLtyt4qDrGQL2WppoVrYAM7H5M3Wk-zT2h8ZUFks2NkI9euInUCdgDauiY56qSgbI9Mz93XH-QQ2bBuwAFzDsP4jZIdE4cxsD_IwJdmCy8tAMJpR-N4dTfABpL2xA3Rjn7x27DQUIZB209nQ_aqYUiE9lYbq8Yb4wzKTHcBx-hcrRlX6Bo3It6hozX1DBq2Uu27hmBLs-r1tsjM3MOd2oa9z_qmdTY3JiV0PcwOCKsyTGlVXWN3Fr5QiE7oh5hhJPE1A66_kouRNS40ueOx87qCud885XMhakFWCIPFtjY90dTPUpWRw0n3wOO7XzaWaoMo7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف خمین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77640" target="_blank">📅 07:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pNkqAnm_jVWLNn3GCmkS9ufDCNhwBFLt3gXZkyzivkskv7PnZmrLUlWB7tnfIDJhHSZL7Sf4mO6ubEd4CPrOY7M5sC5PC9LH2bjdsnI1ZdE7p7IdUsYTG7gAZQBmcrO_cLBZnu4A-vbkCxZ_02uSX8BSTxjj8AawvGeLulVOeSnIiD-i9f80_BloF-YOpuN2XoEmOCd8nZCRlvn8TrNz6Q-Z8QeFVn-VErArZOWfPa_GCiGmB29SKQ-mQYyO6F05r7iwEGKzliI1G39zuJ8EKQ9thhy7fWIpuBWiACgPZfaPcRTfRs_Nk3sblr2LA8j6u-2VkKnLAY2fv_fWGf9pRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره پرتاب موشک از یزد
سلام وحید از سمت یزد دارن موشک میزنن
از یزد موشک زدن
سلام ساعت ۷:۲۱ صدای ارسال موشک داره میاد،
سلام از یزد موشک بلند شد ۷:۲۲
الان یزد 7:21 دقیقه  موشک فرستادن
سلام وحید. جان ساعت ۷و۲۰دقیقه از یزد موشک شلیک شد
وحید جان از یزد موشک بلند شد
۷:۲۱ پرتاب موشک از یزد
همین الان از یزد موشک زدن</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77639" target="_blank">📅 07:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWajCn4ce_KYinHZJPHYM3HxmWL6450wtNhjDYcUgk_R0o3VMw5X7DG8Det13cUlLeozb1_f_N3izW6VIA7gDYjy9l1AmQaW5pnXsxhZHU-22N0sMiJQmFGW4NH3DhRpb3cRYvbq42MIclANmhhmeYW7vGDKxkQfN-ZD3-1RAbeXAuBBYIbQDsux6gMdKm_jCLg-3n2MVDybZessMNzmv6qyWTLEGh_6VM5vmJFRMB-ut-IYeMdAg8YVM6-Etj90nfmsIee0HxMQH5hZrKkC45zXkXzpeRBTjqCmhE0nucM4j3pIuxKK8dFNgbA5-3S-844zxt5kAzBnVp1n7R1nng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال در گزارشی نوشت آمریکا در پاسخ به حمله موشکی جمهوری اسلامی به نیروهایش در اردن، بامداد پنجشنبه حملاتی را علیه مواضع سپاه پاسداران انجام داد.
به گزارش این روزنامه، با وجود گسترده‌تر بودن این حملات نسبت به عملیات‌های پیشین آمریکا، یک مقام آمریکایی گفت این اقدام به معنای بازگشت به عملیات گسترده نظامی نیست. امیدها به دستیابی به یک پیشرفت دیپلماتیک فوری نیز با این حملات کمرنگ شد.
ارتش آمریکا این حملات را «پاسخی قاطع» به حمله روز سه‌شنبه جمهوری اسلامی توصیف کرد. این حملات چند ساعت پس از آن انجام شد که دونالد ترامپ، رییس‌جمهوری آمریکا، وعده داده بود به این حمله پاسخ خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77638" target="_blank">📅 07:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=S2wkuh2KJ51k7KdQ55QNXdxrnoXv85Lm-mjEcRfEgHjHENeYpD4Ovip-qSopyenvHPyOoCsZQLzzFzeznjDJler8_1659T0VKnElPubaOoG2TkERTOkv4WPlOMcsGU92qM4Vgek7bWRPbjBlcDnLxAPr1eJN8WFRapTNKc5Qj5q-7WXK0UUzJfLqise2ZfBT-arDKNHSX2KQiwf1XQeNP3CDwIimpSTsCS5ydcrfnT7RknQ2N0XBVQe8J57HGgF0KLUyYmFDyx8AP1nNglSbD3zAelaJpDg8RH2BrtFxF7Z9deYYjNZR34MNW3iUQbLdARPHjxT0GA4sa4r0TwKVBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=S2wkuh2KJ51k7KdQ55QNXdxrnoXv85Lm-mjEcRfEgHjHENeYpD4Ovip-qSopyenvHPyOoCsZQLzzFzeznjDJler8_1659T0VKnElPubaOoG2TkERTOkv4WPlOMcsGU92qM4Vgek7bWRPbjBlcDnLxAPr1eJN8WFRapTNKc5Qj5q-7WXK0UUzJfLqise2ZfBT-arDKNHSX2KQiwf1XQeNP3CDwIimpSTsCS5ydcrfnT7RknQ2N0XBVQe8J57HGgF0KLUyYmFDyx8AP1nNglSbD3zAelaJpDg8RH2BrtFxF7Z9deYYjNZR34MNW3iUQbLdARPHjxT0GA4sa4r0TwKVBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا پس از تلاش ایران برای حمله، مواضع سپاه پاسداران را هدف قرار داد.
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۱۰ شب ۲۹ ژوئیه به وقت شرق آمریکا، در پاسخ به تلاش‌های دیروز برای حمله موشکی به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند.
تجهیزات و نیروهای سنتکام ده‌ها هدف متعلق به سپاه پاسداران انقلاب اسلامی در ایران را هدف قرار دادند؛ از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، مواضع نظارت و دفاع ساحلی و توانمندی‌های دریایی. هدف این حملات، کاهش بیشتر تهدیدهای ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه حاشیه خلیج فارس بود.
در ۲۸ ژوئیه، نیروهای سپاه پاسداران چندین موشک بالستیک را از ایران، در تلاشی برای انجام یک حمله غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند. تمامی موشک‌های ایرانی با موفقیت رهگیری شدند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در خاورمیانه مستقرند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77637" target="_blank">📅 05:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام‌های دریافتی:
۴:۴۹ اهواز انفجار شدید
انفجار های وحشتناک و پشت سر هم در اهواز
خیلی وحشتناکه
پشت سر هم
حداقل ۴ انفجار
اهواز رو زدن صدای ۲ انفجار
اهواز و دارن میزنن شدید
صدای انفجار مهیب توی اهواز ۴:۴۹
همچنان ادامه داره
تا الان ۴ انفجار بلند
صدا انفجار پشت سر هم ۴ تا زد ۴:۴۹ اهواز مرکز شهر
سلام وحید ۴:۴۹ اهواز ۴تا صدای انفجار شدید اومد
اهواز سه تا انفجار ۴:۵۰
سلام وحید الان ساعت 4:50 اهواز زدن
5 بار صدای زیاد اومده تا الان
اهواز رو زد چهار بار الان!!!!
۴ تا انفجار سنگین ظرف ۲ دقیقه
همین الان اهواز چهارتا صدای انفجار شدید
ساعت ۴:۵۰
همین الان اهواز نمیدونم چند تا افتضاح بلنده
تمام شیشه ها داره میلرزه
اهواز همین الان ۶تا انفجار
۶ تا پشت سر هم اهواز
اهواز ۴.۵۰ دقیقه صدای ۵ انفجار شدید .
سلام وحید جان ۴:۴۹ ۵تا انفجار خیلی شدید اهواز
وحید واییییی خیلی بد بود چندبار زد اهوازو
۴:۵۰ وحشتناک نزدیک ۴ یا ۵ تا انفجار شدید شدید ماشینا به صدا درومدن
ما همین الان با صدای انفجار از خواب پریدیم اهواز ۴:۵۰
اهواز ۴تا اتفجارشدید پشت سر هم
اهواز تو چند دقیقه چندین انفجار شدید داشتیم و طوری که خونه میلرزید و برقمون هم به یک باره قطع شد
اهواز به گلستان خيلي نزديك بود ٤ بار
😭
😭
😭
سلام وحید جان، اهواز اطلاعات توی گلستان رو زدن ما اونجاییم
اهواز فکر کنم سپاه توی اتوبان گلستان بود، سایت اداری. ۴ انفجار.
اهواز کوی سعدی بعد انفجار دوم برق رفته الان ساعت ۴:۵۴
سلام وحید،4,49دقیقه4انفجارشدید دراهواز احتمالااسنگرشکن بودن،
سلام وحید جان ساعت ۴:۵۵ دقیقه صدای انفجار پشت هم از دور شنیده شد
ساختمان اطلاعات اهواز توی گلستان رو زدن
اهواز سمت سعدی و گلستان نورش بود،برق سعدی هم رفت
من اهوازم جفت خونمون چندتا پادگان هست الان زدن چهار بار
خیلی نزدیک بود و وحشتناک
اطلاعات اهواز واقع در پیچ گلستان  رو زدن
وحید تو کل جنگ همچین صدایی نمیومد اهواز به طرز عجیب و وحشتناکی زد در حدی که خونه میلرزه نه فقط پنجره ها
ساعت4:50دقیقه صبح هشتم مرداد
حفاظت اتوبان گلستان رو زدن
🔄
ترکوندنمون اقا وحید
این یکی خیییلیییی بد بووود
بازم انفجار اهواز. ساعت ۵:۲۲
صدای انفجار مهیب در اهواز 5:23
انفجار مجدد اهواز 5:23
5:23 اهواز انفجار خيلييييييىىى شديد
اهواز دوباره زدن شدیدتر از قبلیا
۵:۲۸ یکی دیگه
یه انفجار شدید دوباره اهواز
اهواز صدا انفجار دوباره
وحید همین الان اهواز رو زدن
وحید دوباره انفجار اهواز
وحشتناک همین الان
اهواز ۵ و ۲۳ دقیقه همین الان شرق اهواز صدای انفجار
مجددا اهواز ساعت ۵و ۲۲
۵:۲۱ یدونه صدا اومد،۵:۲۷ هم یکی دوتا صدا اومد
باز اهواز رو زد وحید
زیتون کارمندی ۲تا دیگه الان زد
اقا وحید دوباره زد اهواز
اهواز الان زدن دوباره شیشه ها لرزید
😭
خیلی صدا و‌لرزش داشتتتت
هم اکنون  بازهم زدن05:23
5:22دوباره اهواز و زدن
5,23حمله دوباره اهواز
سلام گلستان اهواز باز زدن.. ساعت ۵:۲۲، ۵:۲۷
5/22" بازم اهواز رو‌زدن شدید
۵:۲۳ اهوازو بازم زد
سلام ۱ انفجار دیگه گلستان اهواز ساعت 5:23
چرا ول نمیکنه
الان یکی دیگه زدن5:23
ساعت 5:22 انفجار شدید اهواز
سلام اهواز وحشتناک بود گلستان سعدی اگه چسب نداشتیم رو شیشه احتمالا شیشه های دو جداره خورد میشدن
ما هنوز برق نداریم
🙏🏼
🙏🏼
انفجار های آخری بشدت به ما نزدیک بودن
آسمون قرمز شده بود از اتیش و صدای ویراژ هواپیما میومد
راحت میچرخیدن
با انفجار دوم برق رفت
۵ و ۲۲ دوباره زد همین الان
🔄
الان دوبارههههه
یکی دیگه5:27
دو انفجار دیگه ۵:۲۸
دوباره زدن وحید
دوباره زد
خیلی شدیده
الان ساعت ۵:۲۸ دوباره بد زد
اهواز همین الان دوباره زدن خونه لرزید با همون شدت بود
باز الان صدا دو انفجار
۵:۲۸ دو صدای انفجار مجدد اهواز
بسیار شدید و لرزش شدید تر شیشه ها
دوتا انفجار دیگه تو اهواز ۵و ۲۸
آقا وحید انفجار به شدت  شدید موج های بسیار زیاد در خانه
بازم انفجار خیلی شدیدی اومد ساعت ۵:۲۸ خیلی ترسناکه
دوتا دیگه زد ۵:۲۷
بندرعباس ساعت 5.24صدای دوتا انفجار وحشتناک بندر
پایگاه هوایی رو دوباره زدن
به نظر میاد یک جا رو دارن چندین بار میزنن. احتمالا سمت گلستان
انفجارها پشت سر هم شدن دوباره
بازم دارن اهوازو میزنن خیلی وحشتناک تر
همچنان داره میزنه
۵:۳۰ دوتا انفجار شدید
سلام اهواز بد دارن میزنن برق رفته مثل اینکه اطلاعات سپاه زدن
هر ده دیقه یبار تا خوابمون میره یه قلمبه میزنن
افتضاحه خیلی نزدیکه صداش
همه شهر حسش می‌کنه
اهواز، همون اطلاعات توی گلستان رو همچنان دارن میزنن
۵:۳۵ اهواز
بازم انفجار سنگین
همه شهر رو بیدار کرد!
یجوری اطراف مارو زدن که کل هوش و حواسم پرید حالمون بده و دقیقا ۱ ساعت دیگه باید سر جلسه امتحان باشیم ...
اهوازیم .
پمپاران در اهواز تمام نمیشه مرتب داره میزنه
سلام وحید جان.
خواهر من دانشگاه علوم‌پزشکی جندی‌شاپور می‌خونه. خوابگاهشون  توی گلستانه، روبه‌روی اطلاعات. می‌گه بعد از انفجارهای مهیب و‌ پی‌در‌پی اهواز شیشه‌ی اناق‌ها شکسته و   همه‌ی بچه‌های خوابگاهی هراسون توی محوطه جمع شده‌ن.
صدای دانش آموزان خوزستانی باشید
نیم ساعت دیگه چطور به سمت حوزه های امتحانی راهی شوند؟؟
🔄
دوباره اهواز رو زد 5:43
ساعت 5:43 دقیقه ی انفجار
بازم زد همین الان صداش دور بود
اهواز ۵:۴۲ مجدد زدن
ساعت ۵.۴۳ صدای دو انفجار در اهواز
دوتا دیگه اهواز رو زد
وحید دوتا دیگه
بازم زد این یکی لرزشش بیشتر بود
.۵:۴۳ گلستان اهواز دور بود ولی دوبار زد
دو انفجار مهیب دیگه در اهواز
تمام خونه و شیشه‌هاش لرزید
اهواز ساعت ۵:۴۳ دقیقه صدای انفجار
اهواز ۵:۴۳ شدید ترین انفجار از ساعت شروع حملات بود
😭
یکی دیگه
سمت شرق خیلی شدید بووود
دوباره انفجار در اهواز ۵:۴۲
سلام همین الان ساعت۵:۴۳ دقیقه روز پنجشنبه  اهواز و زدن
ملی راه هستیم صدا خیلی نزدیک بود
۵:۴۳اهواز ۲انفجاد شدید دیگر
بسیار شدید سمت کیانشهر‌اهواز، دزدگیرا به صدا در اومدن و خونه کامل لرزید
۲ انفجار پشت هم اهواز خیلی سنگینن انفجارهاش
شدید کیانشهر ۵و۴۴دقیقه
صدای انفجار اهواز همین الان ساعت ۵:۴۳ صبح
وحید بازم زد اهوازو دو تا ۵:۴۳
اهواز، ۵:۴۳ …این یکی شدیدتر از بقیه بود
5:42 صداى انفجار در اهواز
ساعت ۵/۴۲ دقیقه انفجار فوق شدید در پدافند اهواز کیانشهر
5:44 یکی دیگه اهواز
دوباره اهواز انفجار شدید ساعت ۵:۴۴
وحید جان الان دوباره صدای انفجار اومد دوبار پشت سر هم اهواز
وحید زد همین الان زیتون اهواز لرزید
وحید مجدد زد دو بار یه صدا انفجار دیگه هم اومد اما لرزش نداشت و نزدیک بود خیلی ساعت 5.44
سمت کیان ابادیم ما شدید صدا اومد ۵و ۴۴ دقیقه
همین الان اهواز کیانشهرو زدن
جفت پدافند
ما کیانشهریم
فکردیم داخل خونمون رو زدن
تا الان ۸بار اهواز رو زدن ۶تاش اطلاعات اهواز بود دوتا دیگه خیلی دور بود معلوم نبود کجا بود
انفجار آخر پدافند بود کنار میدان تره بار
سلام وحید بالای۸انفجار در اهواز رخ داد صداهای خیلی وحشتناکی داشت تروخدا صدای مارو به برسونید بچه ها نیم ساعت دیگه باید برن امتحان بدن گناه دارن اهواز رو ترکوندن
اهواز هم ۴:۴۸ دیقه هم ۴:۵۰ دیقه
هم ۵:۲۰ دیقه هم ۵:۲۸ دیقه
دوتای دیگه هم الان ۵:۴۳
مجموعا حدود ۱۳ تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77636" target="_blank">📅 04:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77635">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzdxv3td4MBtlpuu86j12mt5vIQPHznSAymMGqqePZ4xTx5xK5aKUuM98hP00N6L0wo-ehhkBkggaX-3Kqx1jT5RlbFNyfUWFGaq0MNckJRHpV-YyuEnjVaik6WoBjmwFR9PzbjHqyOu1RRRSYGQCjlvdvvgo5-ppe_iwk3dyeD-b0dU3bJBPBeIe9-YmdUQno2Rjte41B_LZ_lXvtL7UtIiENe2WP2fOT_wcGusyOWc6jkfLnIoN_BTv2fkdrmnYUgKcGvab4r0W1tCMgbokOrMQoNc3rpK3xdC02gs7VZaHk2wlWHVJ0OswCiEtEWG5mGAiR06BlPppznZ9keK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم، در پی شنیده شدن صدای انفجار در استان فارس، منطقه‌ای در اطراف شهر کازرون هدف حمله قرار گرفته است.
پیش از این رسانه‌های داخلی ایران از شنیده شدن صدای چندین انفجار درنورآباد استان فارس خبر دادند.
@
VahidOOnLine
پیام‌هایی که من دریافت کره بودم:
درود کازرون خونه ی ما لرزید
در نزدیکی کازرون صدای چند انفجار اومد ۳:۴۲
ساعت 3:41 - 3:42
کازرون چند تا صدای انفجار شدید اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77635" target="_blank">📅 04:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پیام‌های دریافتی:
‌
۴:۳۵ قشم دو انفجار
۰۴:۳۶ دو انفجار بندرعباس
وحید دوتا انفجار جدید بندر همین الان۴.۳۷
بندرعباس ۲ تا انفجار در حد لرزش در و پنجره ساعت ۴.۳۷
۰۴:۳۶ دو انفجار بندرعباس
صدای انفجار بندرعباس
دو انفجار شدید بندر عباس ۴:۳۷
بندرعباس شدید تر از قبل
دوتا همین الان
۴ تا انفجار مجدد بندرعباس ۴.۳۷ دقیقه
وحید جان صدای دو انفجار در بندرعباس ساعت 4.37
بندرعباس مجدد صدای مهیب ساعت ۴:۳۷
بندرعباس الان ساعت ۴:۳۷ صدای انفجار
وحید ۴:۳۷ زدن بندرعباس ۲ تا شدید موج داشت
الانم دوتا سنگین زدن از خواب پریدیم 4:36
سلام وحید جان همین الان دوباره صدای انفجار میشنویم
دو انفجار شدید همین الان بندرعباس
دوباره بندرعباس انفجار به همون اندازه ۳.۳۸
صدای سومی اومد شدیدتر۴.۳۸
دوباره ۴:۳۸
🔄
دوباره انفجار پشت سرهم ۴.۴۳
همین الان انفجار دوباره
درود ۲ دیگه زد ۴.۴۳ بندرعباس
چند تا دیگه هم زدن همین الان
دوباره ۴:۴۳ بندرعباس
این جدیدا فقط موج دارن
بندرعباس ساعت ۴:۴۳ صدای انفجار شدید
محله چاه تنگو درگهان چن تا خونه دچار آسیب شده انگاری ک زیر آوار موندن کسی بعد انفجار
ساعت ۵ و ۱۰ دقیقه باز قشم زدن
قشم محله ی نریمان،  زیرانگی و محله چاهتنگو رو زدن.. یه دکل هم زدن
سلام وحید داخل قشم محله چاه تنگو  یه خونه مسکونی رو زدن الان رفتم راه رو بستن معلوم نیست فعلا کی داخلش بود ولی خونه پودر شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77634" target="_blank">📅 04:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mMCXt5-_VSTL9YyS0798_28xzpa2m8ErSkTWcpph4mHzvL78TlDx4KiA4URu8bVJDqMy9dqnoFQ-U97Bvp2jfP8QzCulxCyDR5kvV_hyEJH24DRHPwWK2V9A-DrwD6zdU870BUdhytAXnm3WpId9TA9zkX34AWgg10KwOFdq2l78knF--SIEHaAExMyMtHnvfu_izGbkrJ_9YYl65BEVG_WwuYhyP-Qtur21hO0ckr0J4purNcNt8RFGzbBNuOxQhR1d_W3ug2PCaksQqu3zUxe_Hw700Uguyfy11kGDoT5Xb9Nxh1PA1zLsJTisMVnt2Y1mzY1KML-xGxqQRohj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای ایالات متحده امروز ساعت ۸ شب به وقت شرق آمریکا [۳:۳۰ بامداد پنج‌شنبه به وقت تهران] حملات علیه ایران را آغاز کردند.
این حملات، پاسخی قدرتمند به تلاش‌های دیروز ایران برای حمله به نیروهای آمریکایی مستقر در خاورمیانه است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77633" target="_blank">📅 03:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان بندرعباس صدای 2 انفجار
3:40
سلام ۳ و ۴۰ دقیقه بندرعباس دوتا انفجار
۰۳:۳۹
بندرعباس
حداقل ۲ انفجار
درود
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
۴ ۵ تا انفجار توی کمتر از ۱ دقیقه بندرعباس
سه تا انفجار ذیگر
همین الان ۳:۴۱ صدای چند انفجار در بندرعباس
دوباره یک انفجار دیگه 3:41
دوباره یکی دیگه تند تند دارن می زنن
صدای انفجار بزرگ همراه با لرزه زمین بندرعباس
3:41 همین الان بندرعباسو دارن میزنن در و پنجره میلرزه
دو انفجار شدیدتر ساعت 3:41
بندرعباس صدای سه انفجار اومد ساعت ٠٣:٤١
سلام وحید جان همین الان انفجار شدید بندرعباس
سلام وحید جان بندرعباس رو داره میزنه سمت فرودگاه و پایگاه هوایی رو
قشم ساعت ۳و ۴۰ دقیقه انفجار در حد لرزش خونه ها
قشم همین الان با جنگنده بمب بارون شد
صدای سه انفجار شدید در شهر قشم
بندرعباس رو زدن همین الان ۲ تا صدای انفجار
شد ۴ تا
بندرعباس دو انفجار مهیب ادامه دار
صدا دور بود 3: 40
سلام وحید جان الان ساعت ۳ و ۴۰ دقیقه صدای انفجار اومد قشم ،برق ها نوسان پیدا کرد
بندرعباس همینننننن الانننننن خیلی شدید یا خدا
همین الان که دارم تایپ میکنم زدن
همین الان 3:40 دقیقه قشم با صدای انفجار بیدار شدیم
قشم صدا میاد پشت هم
سلام صدای انفجار۳:۴۳ شدید تر از قبلی
۳.۴۱ بندرعباس صدای انفجار
یه انفجار بزرگتر تر
با موجش در و پنجره لرزید
بندرعباس ۳.۴۳
قشم 2 انفجار نزدیک شهر
بندرعباس الان دوباره صدا اومد و خونه لرزید ۳ و ۴۳
بندرعباس ۵ تا انفجار پشت سر هم
انفجار بندرعباس ۲ تا شدیدددد بود صداش الان ۳.۴۲
+ ده‌ها پیام مشابه دیگر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77632" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر انفجار
بوشهر زدن
بوشهر چندتا صدای انفجار اومد
جم همین الان دارن میزنن
۵ تا زد
دوتا صدای انفجار اومد
بوشهر ستا انفجار ۰۳:۳۸
سایت موشکی برازجان رو زد الان.ساعت ۳:۳۷
بوشهر، جغادکیم
همبن الان از خواب پریدم
دو صدای خیلی بلند
سلام ‌وحید ساعت۳:۳۰ چندتا صدای انفجار شنیدیم صدا خیلی زیاد بود پنجره هامون انگار تکون خورد
سلام برازجان همین الان صدای جنگنده و یک انفجار
وحید جان جم الان چندتا صدای انفجار با لرزش اومد
ٰ3:38
بوشهر دارن میزنن
درود، سه بار جم صدا اومد.
۵ انفجار بوشهر همین الان ۳:۴۰دقیقه
بوشهر -چغادک ۴ انفجار ۰۳.۳۷
اقا وحید بوشهر چند تا صدای انفجار شنیده میشه
ولی خیلی صداش دوره
سلام آقا وحید ساعت ۳:۳۸ دقیقه بوشهر رو زدن
صدای جنگنده توی برازجون چند دقیقه هست که تموم نشده و هی بلند تر میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77631" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان سه انفجار در کیش
کیشو زدن همین الان ۳:۳۱
کیش دم بندرگاه ساعت ٣:٣٠ ٢ تا زدن
وحید جان کیش ۲ تا ۳:۳۲
سلام وحید
کیش رو الان زد
دوتا انفجار
وحید الان کیشو زد
۰۳و۳۰ دقیقه انگار  تووآب بود
سلام وحید کیش همین الان صدا اومد
سلام وحید جان
همین الان ۳۱:۰۳ کیش صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77630" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=NzgiYWRjGoa8x7MLOP1wTrvW_TyB_jBPPtmFDWcia7TcGfjljV-9jePuL2qVbV13vtd2rbq_zJhEiRJrrgdE6TZsnbkXnwVwGkMAXJ9sWI8PWMYwbCSX2Tx_3X8Ku4_W6jIL9C1u8hC4FTfY_xZRl00Uaq9qteUF1O5dRGJo_tpmgASaxnpQjZXSrrBcLsSBFHcYQPFg71MbchdnFTjk7tVg7AScZC5faUSfhbab-ci-_8kZceYUW1GMyBVnui-XsZCbZI_LfwzpcIo9W9kGibb58rvVdWi_pGd0-aayra0Z0zE4cAxpdOt2-6xmrtrerp2sdAtnFC6UW6X8QxesgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=NzgiYWRjGoa8x7MLOP1wTrvW_TyB_jBPPtmFDWcia7TcGfjljV-9jePuL2qVbV13vtd2rbq_zJhEiRJrrgdE6TZsnbkXnwVwGkMAXJ9sWI8PWMYwbCSX2Tx_3X8Ku4_W6jIL9C1u8hC4FTfY_xZRl00Uaq9qteUF1O5dRGJo_tpmgASaxnpQjZXSrrBcLsSBFHcYQPFg71MbchdnFTjk7tVg7AScZC5faUSfhbab-ci-_8kZceYUW1GMyBVnui-XsZCbZI_LfwzpcIo9W9kGibb58rvVdWi_pGd0-aayra0Z0zE4cAxpdOt2-6xmrtrerp2sdAtnFC6UW6X8QxesgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
آبادان ترکوندن
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
صدای انفجار آبادان
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
سلام وحیدجان همین الان چهار بار صدای موشک شنیدیم آبادان ساعت ۰۳:۳۲
سلام آقا وحید تا الان آبادان ۸ بار صدای انفجار اومد ۳:۳۰ دقیقه
احتمالا دارن موشک هوا میکنن
سلام وحید، آبادان ساعت ۳:۳۱ پنج شیش تا صدای انفجار بلند شنیدیم
وحید سلام
۶ تا صدای انفجار
همین تلان ، ابادان
وحید سرساعت ساعت ۳:۳۰ ابادان صدای چندتا صدای انفجار اومد ولی دوره احتمالا خارج از شهره
حداقل ده تا انفجار آبادان ساعت ۳:۳۰
از ساعت ۳:۲۰ شروع شد
اقا وحيد صداي ٦ انفجار ساعت ٣:٣٠صبح در ابادان
وحید آبادان ۵ تا انفجار شدید ۳:۲۸
همین الان صدای ۶ الی ۷ تا انفجار از آبادان اومد
ساعت ۳.۳۰ بامداد
آبادان نزدیک ۴/۵ تا صدا شنیدم ... برای اطمینان حتی به دوستمم گفتم اونم شنیده
۳:۳۳ آبادان رو بیشتر از ۵بار زد. بیرون شهر یه چیزی آتیش گرفته، نمیدونم کجاست
آقا وحید آبادان رو ساعت سه نیم زدن شیش تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77629" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AGAZ1MFXUGFETUsg7RL7Lbh8Nm5wfHP-QJFDIM3ayYIdppd4T-fRmf7OQwosrJgMjwMSaiaIiF6Qjj7qsyAR0PnXX4rktU-RjkadurRs7aBwTDu3fwjhdJ4sntR_hSl5YiSdI_sjcTSqNl6O2WQ5GrxVs6S3ucAGID4DHtH5I326n9KgL91ZavYmy23cs-0j_ZEwJDqK64ER0gCa2GcvZXSZTI63uklSIg-h7-70fcupX8dwCDaad9qBTQC0-a7SkB-Rx8Ta3zUviZD1bZGadpexiGn8MsA0Y5j-gwytC2oSvNPAZc88fOORAJ4spdJyCK-ooP15zjG12pb53JQX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست خبرنگار اکسیوس:
یک مقام آمریکایی به من می‌گوید ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
BarakRavid
آپدیت:
بعدا همین گزارش در خود اکسیوس:
ترجمه ماشین: یک مقام آمریکایی به اکسیوس می‌گوید ارتش آمریکا روز چهارشنبه اجرای حملات هوایی در ایران را آغاز کرد.
چرا اهمیت دارد: این نخستین حملات آمریکا در ایران از زمانی است که دونالد ترامپ، رئیس‌جمهوری آمریکا، جمعه گذشته کارزار بمباران را متوقف کرد تا فرصت دیگری به مذاکرات بدهد.
حملات روز چهارشنبه در تلافی حمله موشکی ایران در روز قبل انجام شد که یک پایگاه آمریکا در اردن را هدف قرار داده بود. به گفته ارتش آمریکا، همه موشک‌ها رهگیری شدند.
محور خبر: ترامپ بعدازظهر چهارشنبه به خبرنگاران گفت که آمریکا در ادامه همان روز ایران را «بسیار سخت» هدف قرار خواهد داد.
ترامپ گفت: «حالا نوبت ماست.»
ترامپ مدعی شد ایران پذیرفته است که شلیک موشک‌ها اشتباه بوده و از آمریکا خواسته است تلافی نکند.
تصویر کلی: ترامپ پس از ۱۳ شب متوالی حمله به اهداف نظامی ایران، حملات را متوقف کرده و فرصت کوتاهی برای دیپلماسی ایجاد کرده بود.
حمله موشکی ایران این وقفه را درهم شکست و ترامپ را واداشت پنج روز بعد کارزار نظامی را از سر بگیرد.
یادداشت سردبیر: این یک خبر فوری است. برای دریافت تازه‌ترین اطلاعات دوباره مراجعه کنید.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77628" target="_blank">📅 02:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77627">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده از ساعت ۲:۱۹
سلام وحید جان صدا ۳ تا انفجار شنیدیم نوراباد فارس
۳ تا انفجار همین الان نوراباد ممسنی
آقا. وحید نورآباد ممسنی رو بد زدن
۳ تا شیشه ها لریزد
وحید همین الان نور آباد صدای انفجار اومد ۳ تا بود دقیقن
وحید جان چند لحظه قبل صدا چندتا انجار شدید نوراباد فارس
آقا وحید نوراباد ممسنی رو زدن
صدا هواپیما هم میاد
وحید همین الان نور آبادو زدن
🔄
پیام‌های ساعت ۲:۲۴:
اوه یدونه دیگه
یدونه دیگه ام زدن
البته دور بود
وحید بازم زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77627" target="_blank">📅 02:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیام‌های دریافتی شاید درباره پرتاب شدن موشک که با صدای جنگنده اشتباه گرفته میشه:
یزد الان صدا جنگنده اومد
ساعت ۱۲:۱۰
صدای جنگنده روی آسمان یزد
الان یزد صدای جنگنده امد خیلیم پایین پرواز میکرد صدای انفجاری نیومد اگر بیرون شهر زده نمیدونم
سلام وحید جان
۰۰:۰۷  از تنگه یه صدایی اومد مثل انفجار
شایدم لانچ بالستیک بود
ده دقیقه پیش از یزد موشک بلند شد
وحید جان صدای جنگنده میاد یزد
آپدیت:
پیام‌های دریافتی  بعد از انتشار پست:
یزد هواپیما رد شد
موشک و جنگنده نبود
ارتفاع به شدت پایین
سلام یزد جنگنده خودی بود
سلام وحید جان صدایی که از یزد میومد مال هواپیمای مسافربری بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77626" target="_blank">📅 00:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77625">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQb0B1WJjDPmYJYJFIYG2yRJN98B1MsnuxtPZIb8dQp2MnqJGXq-rNYFiFEKLkbaMx8DMp-djPFFs5iNBMD9TBQgV8uAT5OC0oi8Z72WmzomwlJILs1ZKYIf_hmR7VTy_zqT--AWQcCupQswYngrMoQNv5v5fax6rRVzhbbt1Uc7omt3pcPSzh5ilU981OCFdL04yOYUyaFREV9ZQyMzF96-JaQYcZpSFvOq9VkVw19nCtf1Tt0O1xx3ZPSD099nL1M4-cNXiM4yjp-3jynu2AtPAcWUjJrTT3_-xYECnwXrC_qqVnGhtTmgqxxDnylSGN_iILXzL8jLFWLS2jcm3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس نوشت «رژیم ایران که با سقوط آزاد اقتصاد و تورم سه‌رقمی روبه‌رو است، به‌شدت به منابع مالی نیاز دارد».
او تاکید کرد «ایالات متحده اجازه نخواهد داد ایران تجارت جهانی را گروگان بگیرد یا از کشتیرانی بین‌المللی برای تامین مالی «سپاه پاسداران»، اقدامات تهاجمی و سرکوب استفاده کند».
پیش از این، وزارت خزانه‌داری آمریکا چندین بسته تحریمی علیه افراد، شرکت‌ها، نفتکش‌ها و شبکه‌های مرتبط با صادرات نفت ایران اعمال کرده و اعلام کرده بود این اقدامات با هدف محدود کردن منابع مالی جمهوری اسلامی و سپاه پاسداران انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77625" target="_blank">📅 00:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c878874010.mp4?token=U6Yw2enzBlvg5oUEXhCX0yn_caZVIjrkHU8iHuaRZWminDKQjJh9Nk4XAkCyiTawTi8SW-3V7G3oRm9Wotn84FK8nQWDhDtKESHofAvIrqwxusfatj5jy0lrfWvribMUcIjnb7X6g9u9S2YI6IHt_1eEm4Cjd-X0JI1lnpYRB4qa05IBY4950qbHSCRYF4myoZALMLdGKNfBFQ9GZbonp3CHEA3UBoEVt3w-ipvtQ_hkhh_ofubWnW5Lh-THXyQrBuhMfjh1zzvGmx10D0P0wGy2I7EifHlAk9xF_jPRJC0yTA2ZNRrqYxRUearjP5Iz3fwiXClRWuS4_9gpf1P00w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c878874010.mp4?token=U6Yw2enzBlvg5oUEXhCX0yn_caZVIjrkHU8iHuaRZWminDKQjJh9Nk4XAkCyiTawTi8SW-3V7G3oRm9Wotn84FK8nQWDhDtKESHofAvIrqwxusfatj5jy0lrfWvribMUcIjnb7X6g9u9S2YI6IHt_1eEm4Cjd-X0JI1lnpYRB4qa05IBY4950qbHSCRYF4myoZALMLdGKNfBFQ9GZbonp3CHEA3UBoEVt3w-ipvtQ_hkhh_ofubWnW5Lh-THXyQrBuhMfjh1zzvGmx10D0P0wGy2I7EifHlAk9xF_jPRJC0yTA2ZNRrqYxRUearjP5Iz3fwiXClRWuS4_9gpf1P00w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از گفت‌وگوی ترامپ با خبرنگاران در کاخ سفید، ترجمه ماشین:
خبرنگار: در مورد حمله پهپادی به نفتکش LNG در سواحل مصر چه اطلاعاتی دارید؟ آیا نشانه‌ای وجود دارد که این حمله به ایران مربوط باشد؟
ترامپ: خب، می‌توانم گزارشی به شما بدهم. در این باره توجیه شده‌ام. این کمی از همان ماجراست، اما اوضاع رو به صاف‌شدن است؛ وضعیت دارد روشن می‌شود. در این میان، ما قرار است ضربه بسیار سختی به آنها بزنیم، چون نوبت ماست که ضربه بزنیم. آنها می‌دانند که این حمله در راه است و از ما می‌خواهند این کار را نکنیم. اما دیشب سعی کردند به آن شلیک کنند.
ما پنج موشک داشتیم که با سرعت ۸۵۰۰ مایل در ساعت در حرکت بودند و هر پنج موشک سرنگون شدند؛ اما با این حال آنها شلیک کردند. پس نوبت ماست. خواهیم دید که آیا در مقطعی به یک توافق می‌رسیم یا نه، اما ضربه بسیار سختی به آنها خواهیم زد.
—-
خبرنگار: در چه سناریویی تصور می‌کنید ایران به تأسیسات و پرسنل آمریکا در خارج حمله کند و شما عقب‌نشینی کنید؟
ترامپ: چنین چیزی را نمی‌بینم. نه، ما عقب‌نشینی نمی‌کنیم. ضربه سختی به آنها خواهیم زد. واقعاً می‌توانم این را بگویم، چون آنها در این مورد کار زیادی نمی‌توانند انجام دهند.
این گروه با گروهی که ما با آن سروکار داریم متفاوت بود. آنها قبلاً عذرخواهی کرده‌اند، اما باید یک ضربه‌ای به آنها بزنیم.
خبرنگار: وقتی آنها حمله می‌کنند، آیا همیشه پاسخ خواهید داد؟
ترامپ: بله، تقریباً.
خبرنگار: آقای رئیس‌جمهور، آیا این در پاسخ به حمله موشکی بالستیک شب گذشته به اردن است؟ وقتی می‌گویید نوبت ماست که ضربه بزنیم.
ترامپ: بله، فکر می‌کنم بیشتر به آن مربوط می‌شود. آن رویداد کوچک‌تری بود، اما آنها پنج موشک با سرعت ۸۰۰۰ مایل در ساعت به سمت ما شلیک کردند. خوشبختانه افرادی را داشتیم که بهترین تجهیزات جهان، یعنی سامانه پاتریوت، را به کار می‌گرفتند.
فکرش را بکنید؛ پنج موشک بزرگ با سرعت ۸۶۰۰ مایل در ساعت مستقیماً به سمت ما می‌آمدند و هر پنج موشک سرنگون شدند. چطور است؟ خیلی خوب است. فقط ما می‌توانستیم این کار را انجام دهیم؛ هیچ‌کس دیگری نمی‌توانست.
—-
خبرنگار: آقای رئیس‌جمهور، در مورد جنگ، آیا می‌خواهید مجلس نمایندگان پیش از ۳۱ اوت برای رسیدگی به لایحه تحریم‌های روسیه و ایران بازگردد؟
ترامپ: اگر لازم باشد، بله؛ هرچند راستش نباید لازم باشد. آیا منظورتان طرح لینزی گراهام است؟
خبرنگار: بله.
ترامپ: می‌خواهم ایران را هم به تعرفه‌ها اضافه کنند، نه فقط به تحریم‌ها. فکر می‌کنم این مهم است و همان چیزی است که لینزی می‌خواست. شنیده‌ام روی روسیه تعرفه گذاشته‌اند، اما روی آن پنج کشوری که به ایران مربوط می‌شوند تعرفه‌ای نگذاشته‌اند.
دوست دارم تعرفه‌هایی علیه ایران ببینم. این موضوع را بسیار قوی‌تر می‌کند. شاید بتوانید به آنها بگویید که به نظر من باید برای روسیه تعرفه بگذارند، اما برای ایران هم باید تعرفه در نظر بگیرند. این دقیقاً همان چیزی بود که لینزی می‌خواست.
——
خبرنگار:  رئیس‌جمهور شی به شما گفته بود که چین هیچ سلاحی به ایران نخواهد داد یا نخواهد فروخت. اکنون گزارش جدیدی منتشر شده که می‌گوید ایران قرار است ۴۰۰ پرتابگر موشک از چین و از طریق پاکستان دریافت کند.
ترامپ: خب، این تعجب‌آور خواهد بود. چنین چیزهایی پیش می‌آید، اما واقعاً تعجب‌آور خواهد بود. او خیلی قاطع به من گفت که در این کار مشارکت نخواهد کرد و می‌داند که من کاملاً ناامید خواهم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77624" target="_blank">📅 23:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77623">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اکسیوس:
پشت پرده دیدار تعیین‌کننده «بی‌بی» با ترامپ در کاخ سفید
ترجمه ماشین:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در دیدار خود با رئیس‌جمهور ترامپ درباره احتمال دستیابی به توافقی با ایران ابراز تردید کرد و درباره افزایش فشار اقتصادی بر ایران «از طریق ابزارهای نظامی و غیرنظامی» به گفت‌وگو پرداخت؛ یک مقام ارشد اسرائیلی این موضوع را در نشستی با خبرنگاران بیان کرد.
اهمیت موضوع:
دیدار روز سه‌شنبه نخستین ملاقات نتانیاهو و ترامپ از زمان آغاز جنگ در ۲۸ فوریه بود. این دیدار در حالی انجام شد که ترامپ همچنان برای دستیابی به توافقی با ایران تلاش می‌کند، اما هم‌زمان بازگشت به عملیات رزمی گسترده را نیز در نظر دارد.
▪️
چند ساعت پس از این نشست، ایران برای نخستین بار از زمانی که ترامپ روز جمعه حملات آمریکا در ایران را متوقف کرد، یک حمله موشکی علیه پایگاهی آمریکایی در اردن انجام داد.
▪️
ترامپ روز چهارشنبه در مصاحبه‌ای با فاکس‌نیوز وعده داد که پاسخی جدی خواهد داد. حمله غافلگیرانه ایران ممکن است رئیس‌جمهور را به سوی تشدید تمام‌عیار درگیری سوق دهد.
▪️
مقام اسرائیلی گفت نتانیاهو در انتظار تصمیم ترامپ است، اما به‌روشنی به او گفته است که اگر ایران به اسرائیل حمله کند، پاسخ اسرائیل فوری و قدرتمند خواهد بود.
آنچه در اتاق گذشت:
ایران موضوع اصلی گفت‌وگوی ۹۰ دقیقه‌ای بود.
▪️
مقام اسرائیلی گفت آن‌ها سه گزینه‌ای را که ترامپ برای گام‌های بعدی در نظر دارد بررسی کردند:
۱. دستیابی به توافق با ایران.
استیو ویتکاف و جرد کوشنر، فرستادگان ترامپ، همچنان با ایرانی‌ها مذاکره می‌کنند، هرچند در حال حاضر اختلاف‌ها همچنان گسترده به نظر می‌رسد. مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است که نسبت به امکان دستیابی به توافق با ایرانی‌ها تردید دارد.
۲. ادامه محاصره دریایی ایران
هم‌زمان با افزایش فشار اقتصادی.
۳. ازسرگیری و تشدید حملات نظامی.
▪️
این مقام گفت: «همه این گزینه‌ها را به‌طور مفصل و بسیار صریح بررسی کردیم؛ نه با هدف ترجیح دادن یک گزینه بر گزینه‌ای دیگر، بلکه برای بررسی اینکه هرکدام چه نتیجه مطلوبی می‌تواند داشته باشد. موضوع گفت‌وگو همین بود.»
نمای نزدیک:
مقام اسرائیلی گفت ترامپ درباره تأثیر جنگ بر بازارهای انرژی و اقتصاد جهانی ابراز نگرانی کرد.
▪️
نتانیاهو به ترامپ گفت حکومت ایران عمدتاً می‌کوشد از تنها اهرمی که برایش باقی مانده است — تنگه هرمز — برای وادار کردن آمریکا به دادن امتیاز استفاده کند.
▪️
مقام اسرائیلی گفت نتانیاهو نگرانی‌های ترامپ را نادیده نگرفت، اما به او گفت راه‌هایی برای افزایش بیشتر فشار بر اقتصاد ایران وجود دارد؛ اقتصادی که هم‌اکنون نیز تحت فشار شدیدی قرار دارد.
▪️
مقام اسرائیلی گفت: «درباره افزایش فشار اقتصادی از طریق ابزارهای نظامی و غیرنظامی گفت‌وگو کردیم. درباره امکان ادامه محاصره با هدف تحت فشار قرار دادن ایران صحبت کردیم.»
▪️
مقام اسرائیلی گفت در درون رهبری ایران میان کسانی که به‌شدت نگران فروپاشی اقتصادی هستند و عناصر تندروتری که معتقدند تا زمانی که کنترل تسلیحات را در اختیار دارند و می‌توانند از پایگاه حامیان حکومت پشتیبانی کنند مشکلی ندارند، اختلاف‌نظر وجود دارد.
▪️
مقام اسرائیلی افزود: «آن‌ها با مشکلات تأمین سوخت، صف‌های طولانی در پمپ‌بنزین‌ها و کمبود گازوئیل روبه‌رو هستند. اعتراض‌های کوچکی شکل گرفته است، زیرا مردم به‌شدت ناراضی‌اند. حکومت بسیار نگران این وضعیت است و می‌ترسد مردم به‌دلیل شرایط اقتصادی قیام کنند.»
پشت صحنه:
مقام اسرائیلی گفت مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، «درباره همه‌چیز» موضعی بسیار منفی دارد، اما مشخص نیست دستورهایی که به او نسبت داده می‌شود واقعاً از جانب خود او صادر می‌شود یا نه.
▪️
مقام اسرائیلی مدعی شد: «او زنده است، اما هیچ‌کس نمی‌تواند شهادت دهد که واقعاً او را دیده است. به اطرافیانش گفته بدون تأیید او هیچ کاری انجام ندهند و حتی گفته می‌شود یک بار وقتی بدون اجازه‌اش کاری کردند، عصبانی شد.»
نمای دور:
مقام اسرائیلی گفت نتانیاهو نقشه‌ای از سوریه را به ترامپ نشان داد که براساس آن، مناطقی که ترکیه در سوریه کنترل می‌کند «۵۰ برابر بزرگ‌تر» از مناطق تحت اشغال اسرائیل است.
▪️
مقام اسرائیلی مدعی شد ترکیه ۵ درصد از خاک سوریه را کنترل می‌کند، در حالی که اسرائیل ۰٫۱ درصد آن را در اختیار دارد.
▪️
یک مقام آمریکایی گفت برخلاف اشغالگری اسرائیل در جنوب سوریه، حضور نظامی ترکیه در شمال سوریه در حال حاضر با رضایت و به دعوت دولت سوریه انجام می‌شود.
▪️
مقام اسرائیلی گفت نتانیاهو به ترامپ گفته است اسرائیل تا زمانی که تهدیدی از جانب «گروه‌های جهادی» وجود داشته باشد، حضور خود را در «منطقه حائل» جنوب سوریه حفظ خواهد کرد.
▪️
مقام اسرائیلی گفت: «نتانیاهو می‌خواست این موضوع را به ترامپ نشان دهد، زیرا او گاهی براساس اطلاعات نادرستی که بعضی افراد در اختیارش می‌گذارند، به دیدگاه‌های مشخصی می‌رسد. اگر در همان مراحل اولیه راهی برای تغییر نظرش پیدا نکنید، آن نظر تثبیت می‌شود. بنابراین می‌خواستیم واقعیت‌ها را، در صورت امکان به‌شکل تصویری، به او نشان دهیم.»
▪️
مقام اسرائیلی گفت نتانیاهو همچنین درباره توافق هسته‌ای آمریکا و عربستان سعودی با ترامپ گفت‌وگو کرد. ترامپ به نتانیاهو گفت این توافق را در چارچوب عادی‌سازی روابط عربستان سعودی با اسرائیل می‌بیند.
▪️
مقام اسرائیلی گفت: «اگر شاهد پیشرفت واقعی باشیم، درباره موضوع هسته‌ای حرف‌هایی برای گفتن خواهیم داشت.»
تصویر کلی:
مقام اسرائیلی گفت نتانیاهو به ترامپ، معاون رئیس‌جمهور ونس و ویتکاف گفته است که درباره کاهش کمک‌های نظامی آمریکا به اسرائیل تا رسیدن به صفر ظرف ۱۰ سال جدی است. او تأکید کرد که خواهان پیشبرد مذاکرات برای تدوین یک تفاهم‌نامه در این زمینه است.
▪️
مقام اسرائیلی گفت ترامپ و اعضای تیمش اعلام کردند بازخوردهایی از جمهوری‌خواهانی دریافت کرده‌اند که نگران‌اند به‌دلیل حمایت از حذف تدریجی کمک‌ها، به ضدیت با اسرائیل متهم شوند.
▪️
نتانیاهو به آن‌ها گفت شخصاً و به‌صورت علنی رهبری این تلاش را بر عهده خواهد گرفت، زیرا می‌خواهد اسرائیل به استقلال دفاعی دست یابد.
▪️
مقام اسرائیلی گفت: «درباره یک فرایند ۱۰ ساله صحبت می‌کنیم. از پیشنهادها استقبال می‌کنیم و شاید این اتفاق بتواند سریع‌تر رخ دهد.»
▪️
این مقام حتی گفت نتانیاهو به بخش دفاعی اسرائیل دستور داده است روی ساخت یک جنگنده مدرن ظرف یک دهه کار کند تا نیروی هوایی این کشور حتی در صورت توقف تحویل جنگنده‌های اف‌ـ۳۵ و دیگر هواپیماهای پیشرفته از سوی آمریکا، همچنان قدرتمند باقی بماند.
▪️
این مقام گفت نتانیاهو نمی‌خواهد اسرائیل به «حسن نیت کنگره آمریکا» وابسته باشد، زیرا معتقد است جهت‌گیری سیاسی هر دو حزب درباره کمک‌های نظامی در حال منفی‌تر شدن است.
▪️
نتانیاهو معتقد است وضعیت اقتصادی اسرائیل به این کشور اجازه می‌دهد کمک‌های نظامی آمریکا را به‌تدریج کنار بگذارد. مقام اسرائیلی گفت نتانیاهو پیشنهاد کرده است تفاهم‌نامه جدید شامل ۱۶ میلیارد دلار کمک نظامی مستقیم آمریکا و همچنین ۵ تا ۱۰ میلیارد دلار حمایت از توسعه سامانه‌های دفاع موشکی اسرائیل باشد.
▪️
افزون بر این، نتانیاهو پیشنهاد ایجاد یک صندوق مشترک ۱۶ میلیارد دلاری برای تحقیق و توسعه سامانه‌های تسلیحاتی جدید را مطرح کرده است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77623" target="_blank">📅 23:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77622">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=TNziLfucrwkRbk4wIXCV92Odjd2rbMRwllveFflEIW1mC1mc8d6gSUfWsSsJVX2jYJWS6xXZwZMEai4LV87Pjq9fzg4Q21Q16X6aibo433jamwaifwIrg3TLy63ZKRX_xJ8qZsT943yHj0BIme7u-v_rpyAOKzs5KYiXzxCndoGt_7TrKe5TwU_rXJQqSq8_ffcjVBFhtpj15wNnI97LWztqSWi4ExOJouyKL8Ts9wLgL9bSgLe83w9sqRGWoTilLgTIsZq8pBymq2oXw5JbD78ySNK55PSpzoHShp9Eb3qakpXo6tCqdp1Yvnr4RHxRLLyGRiKrkQrQmab0x_CA9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d13dda12b7.mp4?token=TNziLfucrwkRbk4wIXCV92Odjd2rbMRwllveFflEIW1mC1mc8d6gSUfWsSsJVX2jYJWS6xXZwZMEai4LV87Pjq9fzg4Q21Q16X6aibo433jamwaifwIrg3TLy63ZKRX_xJ8qZsT943yHj0BIme7u-v_rpyAOKzs5KYiXzxCndoGt_7TrKe5TwU_rXJQqSq8_ffcjVBFhtpj15wNnI97LWztqSWi4ExOJouyKL8Ts9wLgL9bSgLe83w9sqRGWoTilLgTIsZq8pBymq2oXw5JbD78ySNK55PSpzoHShp9Eb3qakpXo6tCqdp1Yvnr4RHxRLLyGRiKrkQrQmab0x_CA9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی، جزئیاتی از گفتگو و تبادل نظر خود با پیت هگست، وزیر جنگ ایالات متحده که روز چهارشنبه هفتم مردادماه در واشنگتن انجام شد را به اشتراک گذاشت.
نتانیاهو گفت: «هگست در این گفتگو به من گفت وقتی به وضعیت جهان نگاه می‌کنیم، کشورهایی هستند که اراده مبارزه در کنار ایالات متحده را دارند، اما توانایی لازم را ندارند. در مقابل، کشورهایی هم هستند که از توانایی برخوردارند، اما اراده جنگیدن ندارند.»
نخست‌وزیر اسرائیل در ادامه افزود که وزیر جنگ آمریکا تاکید کرده است: «تنها در اسرائیل است که ما هم‌زمان شاهد وجود اراده و توانایی مبارزه هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77622" target="_blank">📅 20:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bR4wklAqigJGf93lYT1dZGHJLee2uO-0HMVl9zUQVyw-VSRfZVqB9YuC5Z4MLAU9M-Ujc6vYIrg3hbMyI1j6ivyrsCTzCAoerJMH4irXbmJH6m_gdu8gWeeraUe4a1_cUjykT8mIB7heik3DRJYfNCs6u7gcWsOl4eK5DwqK_0LPJGVn8rZvG0UuQbZm27e3l_SDc6XpsdLytUMuyvl2PUjchLEFMo5uzORsvD_YnrFe5v-m6fxn7Kpc5z2r8Fs7VwJpxCdj6vCc4fFsc8mWI8d3nuCA62WFTpvmX3xaU8YZ-dydvm91MqkRsXvdZmWG8PoDEg04XLt-wZ4dVD37AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از وقوع انفجار در پایانه گاز طبیعی مایع بندر دمیاط مصر هنگام تخلیه محموله خبر دادند.
همزمان، شرکت امنیت دریایی امبری و منابع امنیتی اعلام کردند یک پهپاد به یک شناور ذخیره‌سازی گاز متعلق به آمریکا برخورد کرده است؛ حادثه‌ای که به آتش‌سوزی دو کشتی منجر شد، اما تاکنون گزارشی از تلفات جانی منتشر نشده است.
بر اساس گزارش‌ها، این انفجار هنگام تخلیه محموله در پایانه گاز طبیعی مایع بندر دمیاط رخ داد.
شرکت امنیت دریایی امبری اعلام کرد یک پهپاد به یک شناور ذخیره‌سازی شناور گاز که تحت مالکیت آمریکا است، برخورد کرده است. به گفته این شرکت، در پی این برخورد آتش‌سوزی ایجاد شد و سپس به کشتی دیگری نیز سرایت کرد.
شرکت خدمات بندری اینچ‌کیپ نیز در گزارشی جداگانه اعلام کرد دو کشتی حامل گاز در بندر دمیاط دچار آتش‌سوزی شده‌اند.
امبری اعلام کرد خدمه هر دو شناور تخلیه شده‌اند و آتش تحت کنترل درآمده است. این شرکت افزود تاکنون هیچ گروهی مسوولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77621" target="_blank">📅 20:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B0nwoF3VXJqRn32roGZihC2SpCUX6pTvqpBZncPupPjYxyo1wr11bVa9FzHC_19z-3l1PKW3tOTR3YLffhmKlAFN326iqQivG03ZPW1sTwEiRMsyBMLWWvdc8ZR9fozPMnZ5eHNmxyMlzvvneqQtKZOPwxDOWpaG2aXzVjx3E0v-KPpmCl39dNk8B5WbLC8is-ImSwwbj8lWG5YLptDMFtUOQTkutln7ofR-FE05cNJIJb7zr9QgMaTzdKbHxTWqm0YcX_7rTh_5kuGoG02I1esulCbmw18ZayRjqXCqZsDYf9oBT-L_7TiuqWof_8STLknXK_eajH0t-RDUgUg2Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: پس از تهدیدهای اخیر و تلاش برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناه در حال عبور از تنگه هرمز، سپاه پاسداران انقلاب اسلامی ایران همچنان ادعا می‌کند که دریانوردان بین‌المللی باید فقط از مسیرهای مورد ترجیح سپاه استفاده کنند.
✅
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه هیچ اختیاری برای تعیین مسیر حرکت آزاد و بدون مانع ندارد. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای سنتکام به عبور حدود ۱٬۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77620" target="_blank">📅 19:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSaSeBD7FC_Qbe3e5WXQMKjL69koJ07D47NtiRE1x3NO81UqiUbCfXXBpsVW1L0yX41dO-OC1gMpG0udIfUEE9DbZuCi-3vetWfXpQ2p78asU5wBb1gwVP5xXP5VJqWpE-GutcV-kWDwU5zzdh5ro8QPytCEd6CeeC_EGklaVCnXwxcl853BQEbADy-TQpgUy3gNLsYWncA4Iai8fXwAM9QNZNjm13Z12mgb4p5U_-j-rqK87hNBjb8d4YXXmkjyk93D8j1mGmTpCjg66WNwixtIA4nyHa5nO7pM2l-b7qsJ8GYNMSQe7fOWGwqUXNtkym3bFaGl_4cyVoY83LniEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، نیروی دریایی سپاه پاسداران انقلاب اسلامی روز چهارشنبه هفتم مردادماه، اعلام کرد سه نفتکش را در تنگه هرمز به دلیل بی‌توجهی به هشدارها «هدف قرار داده و توقیف کرده است».
در این گزارش به نام این شناورها، مالکیت، محل دقیق حادثه و جزئیات تخلفات ادعایی آن‌ها در این آبراه اشاره‌ای نشده است، اما تهران مسیر جایگزین جنوبی در امتداد سواحل عمان را رد کرده است.
بر اساس بیانیه‌ای که تسنیم منتشر کرده، سپاه پاسداران تاکید کرده است که «مداخله‌ها و دستورات غیرقانونی» ایالات متحده از سوی شناورهای حاضر در منطقه «بی‌پاسخ نخواهد ماند».
مرکز عملیات تجارت دریایی بریتانیا، هنوز وقوع چنین حملاتی را تایید و گزارش نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77619" target="_blank">📅 18:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hUAEez913D6tEtvklVEeO_J2CCi9THRT7vE3VVDILxXTTw1N_aoKOiocZV2jxaDcFlhvvqNd1llGQlD-YvVtkLORtrdFIYuWuoB0xvXGWjxGz29ChZs8bt_v2I3TVk8fVm-4qCAEf5W5iBlrguvul8FLhXy-126RckF_gE7Ma-T4ex_QXWoCVwTPx1yu0xuidyI6omgKE9FkBCy2H5e5XzRJY30odilv9L4Kct6X7P-E6lzxYCNx8gi7tiQtlrBQpMGr7AcZ-I9D87J8FQ1lM_lEVTelN91rzbZqKpeAXIfN6g7a55yo1z1iYPPfRxvXtyXUzpHiKkZ0h_kIugsolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ دانشگاه ایرانی در رتبه‌بندی تاثیرگذاری تایمز ۲۰۲۶ حضور ندارد
در رتبه‌بندی تاثیرگذاری و پایداری دانشگاه‌های جهان در سال ۲۰۲۶، نام هیچ دانشگاهی از ایران دیده نمی‌شود؛ این در حالی است که در فهرست سال ۲۰۲۵، ۳۴ دانشگاه ایرانی حضور داشتند.
تایمز امسال نحوه مشارکت در این رتبه‌بندی را تغییر داده و آن را به عضویت دانشگاه‌ها در شبکه پایداری و ارائه اطلاعات از سوی خود موسسات مشروط کرده است.
برخی رسانه‌های ایران این تحول را با عنوان «حذف ایران» پوشش داده‌اند؛ تعبیری که اقدامی هدفمند یا تنبیهی را تداعی می‌کند، در حالی که هنوز مشخص نیست نبودن دانشگاه‌های ایرانی ناشی از تصمیم تایمز بوده یا شرکت نکردن آنها در سازوکار تازه رتبه‌بندی.
رتبه‌بندی‌های موسسه تایمز از شناخته‌شده‌ترین و پرمراجعه‌ترین نظام‌های ارزیابی دانشگاه‌ها در جهان است و نتایج آن می‌تواند بر اعتبار بین‌المللی، جذب دانشجو و همکاری‌های علمی دانشگاه‌ها اثر بگذارد.
@
VahidHeadline
برای نخستین‌بار از زمان آغاز انتشار رتبه‌بندی «دانشگاه‌های تأثیر‌گذار» موسسه آموزش عالی تایمز، نام هیچ دانشگاهی از ایران در نسخه سال ۲۰۲۶ این فهرست دیده نمی‌شود. رخدادی که در کنار افت مداوم جایگاه دانشگاه‌های ایران در دیگر نظام‌های معتبر رتبه‌بندی جهانی، بار دیگر وضعیت آموزش عالی کشور را زیر ذره‌بین برده است.
بر اساس نتایج منتشر شده، در رتبه‌بندی سال ۲۰۲۶ تایمز، یک‌هزار و ۶۴۶ دانشگاه از ۱۱۶ کشور بر پایه اهداف توسعه پایدار سازمان ملل متحد (SDGs) ارزیابی شده‌اند. با این حال، برخلاف سال‌های گذشته، نام ایران به‌طور کامل از این فهرست حذف شده و مؤسسه تایمز نیز تاکنون توضیحی درباره علت این موضوع ارائه نکرده است.
حذف نام ایران از این رتبه‌بندی در حالی رخ داده که دانشگاه‌های کشور از زمان آغاز انتشار آن در سال ۲۰۱۹ همواره در فهرست تایمز حضور داشتند. تنها در سال ۲۰۲۵، ۳۴ دانشگاه ایرانی در این رتبه‌بندی ارزیابی شدند و برخی از آن‌ها در چند شاخص توسعه پایدار، از جمله «سلامت و رفاه»، «آموزش باکیفیت»، «صنعت، نوآوری و زیرساخت» و «برابری جنسیتی»، جزو دانشگاه‌های برتر جهان بودند.
همزمان، نتایج تازه‌ترین رتبه‌بندی جهانی QS نیز از ادامه روند نزولی دانشگاه‌های ایران حکایت دارد. رتبه‌بندی QS که از معتبرترین نظام‌های ارزیابی آموزش عالی در جهان به شمار می‌رود، دانشگاه‌ها را بر اساس شاخص‌هایی مانند اعتبار علمی، کیفیت پژوهش، میزان استناد به مقالات، نسبت استاد به دانشجو، همکاری‌های بین‌المللی و اشتغال‌پذیری فارغ‌التحصیلان ارزیابی می‌کند.
در این ارزیابی دانشگاه تهران ۴۵ پله سقوط کرده و از رتبه ۳۲۲ به ۳۶۷ جهان رسیده است. دانشگاه تبریز ۱۰۸ رتبه، دانشگاه فردوسی مشهد حدود ۱۲۵ رتبه و دانشگاه‌های شیراز، اصفهان و آزاد اسلامی نیز افت قابل‌توجهی را تجربه کرده‌اند؛ به‌طوری که دانشگاه آزاد از جمع هزار و ۴۰۰ دانشگاه برتر جهان خارج شده است.
در مقابل، کشورهای منطقه روندی معکوس را طی کرده‌اند. ترکیه با ۲۵ دانشگاه در رتبه‌بندی QS حضور دارد و دانشگاه فنی استانبول به رتبه ۲۷۹ جهان رسیده است. امارات متحده عربی نیز سه دانشگاه در میان ۳۰۰ دانشگاه برتر جهان دارد.
حسین سیمایی‌صراف، وزیر علوم، کاهش سرمایه‌گذاری در پژوهش، ضعف همکاری‌های علمی بین‌المللی، کمبود زیرساخت‌های آموزشی و پژوهشی و محدود شدن فرصت‌های مطالعاتی را از عوامل افت جایگاه دانشگاه‌های ایران دانسته است.
شاهین آخوندزاده، معاون تحقیقات وزارت بهداشت، نیز اعلام کرده بود که محدودیت‌ها و اختلال‌های گسترده اینترنت در سال ۲۰۲۶، پژوهشگران ایرانی را حدود یک‌سوم سال از فعالیت علمی بازداشت؛ موضوعی که به گفته او می‌تواند به کاهش حدود ۱۰ هزار مقاله علمی و افت بیشتر جایگاه علمی ایران منجر شود.
کارشناسان آموزش عالی نیز می‌گویند کاهش ارتباط دانشگاه‌های ایران با مراکز علمی جهان، محدودیت در جذب استاد و دانشجوی خارجی، کاهش بودجه پژوهشی، ضعف زیرساخت‌های آموزشی و دسترسی محدود به منابع علمی بین‌المللی، از مهم‌ترین عوامل کاهش رقابت‌پذیری دانشگاه‌های ایران در رتبه‌بندی‌های جهانی است.
رتبه‌بندی دانشگاه‌های تأثیرگذار تایمز از سال ۲۰۱۹ با هدف ارزیابی عملکرد دانشگاه‌ها در تحقق ۱۷ هدف توسعه پایدار سازمان ملل منتشر می‌شود و تنها نظام رتبه‌بندی جهانی است که نقش دانشگاه‌ها را در حوزه‌هایی مانند آموزش، سلامت، برابری جنسیتی، نوآوری، محیط زیست، عدالت و توسعه پایدار می‌سنجد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77618" target="_blank">📅 17:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzSvIcXQt5x67qUTNBgCKjhjYhZsxb6ZWphXWfQf1sXXofdW7ZWzOxhR14YfokEBbaN9x1K8moASQomUutnhb_N_L_B4UwZLd7kop7wL-scOXucQ38LB0_niHMdXa8ir3Gj8x7MtfPEL6HzQ7kK4g7JMHf2th8EbuDzaWqXStwqzH1HRoZ-qpLWfCX8SwJ89Wq_JxCQYmoApL4AmjovuTzeCKviMPP6uWD9-_4SOtEAsj2RNvDmG-IC7PEhMiA8FGNb-xs7Au3TV860bKNHM98F0tPyUYS6Kf8ZMAK6tX3nhts11QSVgw23u0KZ9WJ_05WPO7okWalFwMMOBoMMfgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه پس از آنکه ارتش ایالات متحده اعلام کرد چندین موشک بالستیک شلیک‌شده از سوی ایران به سمت نیروهای آمریکایی در خاورمیانه را رهگیری کرده است، وعده داد که ایران را به‌شدت هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز گفت: «حسابی نابودشان خواهیم کرد. خیلی سخت به آنها ضربه خواهیم زد.»
این گفت‌وگوی تلفنی به‌صورت کامل پخش نشد، اما یکی از خبرنگاران فاکس نیوز خلاصه‌ای از اظهارات ترامپ را منتشر کرد.
@
VahidHeadline
گفت: حسابی نابودشان خواهیم کرد. ضربات سختی به آنها خواهیم زد و به‌شدت تنبیه خواهند شد.
ترامپ همچنین درباره حملات هوایی آمریکا و عربستان سعودی به شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق گفت این حملات با هماهنگی دولت عراق انجام شده است.
رییس‌جمهوری آمریکا این شبه‌نظامیان را «سرطانی برای جهان» توصیف کرد و گفت در حال بررسی صدور هشدارهای بیشتر علیه نیروهای نیابتی جمهوری اسلامی و ارتباط آنها با حکومت ایران است.
ترامپ همچنین گفت اکنون موضع بنیامین نتانیاهو درباره جمهوری اسلامی را درک می‌کند.
او در پاسخ به پرسشی درباره احتمال ادامه مذاکرات با جمهوری اسلامی نیز گفت: «اجازه می‌دهیم به گفت‌وگوهایشان ادامه دهند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77617" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77615">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=suIF9tc_-ghTBogStBH4zJJ2umnF1k0Fmv4Tf2VsfwwXGSCssN4B-9odWp5nXph_dw9EyyRxxol9o58JAR2HFw0j3SW97AvCN6Nd5M4IADpdK3Q6LSxAstIeVZfXrXYnNtnJL8NokoxLZD5k_N473ikOur-FIJG-CQqCjYKVXuS6UITly6RGWRJ1wZh1XmbSV_ggiZBBC1LTxmYgczo-rO2WRJZxnWt4Yd5Rj3dDBamhlngDBtPPX8s1P3-Qtra_JC3SnQ_PDw9umqyRGGZCjLwwYKWxnj-7SjpudhwUGDJlydvX-x4-TpO2Z_LmSXcdT93c9rM3WGg_7WRzaIsCuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/76c3174d20.mp4?token=suIF9tc_-ghTBogStBH4zJJ2umnF1k0Fmv4Tf2VsfwwXGSCssN4B-9odWp5nXph_dw9EyyRxxol9o58JAR2HFw0j3SW97AvCN6Nd5M4IADpdK3Q6LSxAstIeVZfXrXYnNtnJL8NokoxLZD5k_N473ikOur-FIJG-CQqCjYKVXuS6UITly6RGWRJ1wZh1XmbSV_ggiZBBC1LTxmYgczo-rO2WRJZxnWt4Yd5Rj3dDBamhlngDBtPPX8s1P3-Qtra_JC3SnQ_PDw9umqyRGGZCjLwwYKWxnj-7SjpudhwUGDJlydvX-x4-TpO2Z_LmSXcdT93c9rM3WGg_7WRzaIsCuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب گذشته نیروهای آمریکایی و عربستان سعودی در عملیاتی مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در شرق عراق را هدف قرار داده‌اند.
@
VahidHeadline
بر اساس گزارش‌ها، پایگاه‌های حشد شعبی در استان‌های دیاله، کرکوک، کربلا و نینوا هدف حمله قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77615" target="_blank">📅 16:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77614">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Esw5zvhrom_utdWZM3zogp-mu5yBOfOckumrQnANHxyayYkkx_knq7HyJOtN_o2dTGRo5NHIqpX3hzk8VCp2VxeNtgj5A4gEbDm3zNExWh4M46njFoL8W_NAojeUE5A9yE9JdRHBzwZ1XL05u6GUuL3YFHHwtvC5TgxljDzWWSzZU0Sur4ZBA2OzQ9dyAFprVksdedAHYkmGlQH3gfE7wft4QEHxN17foZv18zptU11ypt0-zrgq6RChqOHM6ZOTsMNJpBCMQLl-QDXNP-p14BH5DXnMo6Zmchu2L-2_mt61QZU-nxlUu1e23rqOQeKkfC4ZrmeunQAXdO3rXGVyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرحی را به مرحله بعد فرستاد که در کنار تشدید فشار اقتصادی بر روسیه، تحریم‌های مرتبط با ایران را تا سال ۲۰۳۱ تمدید می‌کند.
این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، هنوز باید در رأی‌گیری نهایی سنا تصویب و سپس در مجلس نمایندگان بررسی شود.
@
VahidHeadline
و  در خبری دیگر:
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) اعلام کرد ۱۰ شرکت و هشت نفتکش را به فهرست تحریم‌های خود افزود.
این تحریم‌ها بر اساس فرمان اجرایی ۱۳۹۰۲ و در ارتباط با جمهوری اسلامی اعمال شده‌اند.
در میان نهادهای تحریم‌شده، «اداره خدمات دریایی هرمزسیف» و «شرکت بیمه دریایی خلیج فارس» در ایران نیز قرار دارند.
وزارت خزانه‌داری آمریکا همچنین اعلام کرد این دو نهاد مشمول تحریم‌های ثانویه هستند.
شرکت‌های تحریم‌شده در هنگ‌کنگ، جزایر مارشال و چین ثبت شده‌اند و نفتکش‌های تحریم‌شده نیز با پرچم کشورهای مختلف فعالیت می‌کنند. این نفتکش‌ها به شرکت‌های تازه تحریم‌شده مرتبط معرفی شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77614" target="_blank">📅 16:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77613">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTbD1Qe-EV1h971CmJz5QvaxuacwgUlB075rCiOZaxR-3IFNlXvCsVX2r9JYOsog5N4gvr1sQYr0ukQll5eWZduCoCEfdiCKEYkj4yq1Kg9cg2sC_sF31ftyis3JSLJqwW_pJDyii0NUssEP0AwYNIknr09E7iYQUxVmvMfh5znkShnhYhuTNuz-Sk2lVld8NPS0568Bby_bpQe5BigVhq1yu-QirC105CEhpNi5qqsxtIKqUvpExDZAdwePnfSIMONqnTtiJIx749F-D7xOGhPRVzmp3R3oH4GK-IQuCwtDu48NvpbdrBoraxW5IbPdtFEZNVQeTDnDKVC9NBzEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع منطقه‌ای گزارش داد که حوثی‌های یمن در حال بررسی طرحی برای دریافت عوارض از کشتی‌های تجاری عبوری از تنگه باب‌المندب هستند؛ اقدامی که به گفته این منابع، پس از اعلام محاصره دریایی عربستان سعودی مطرح شده و می‌تواند فشار بر آمریکا را افزایش دهد.
به گفته این منابع، حوثی‌ها در حال بررسی دریافت عوارض از بیشتر کشتی‌هایی هستند که از باب‌المندب، گذرگاه راهبردی میان دریای سرخ و خلیج عدن، عبور می‌کنند، اما هنوز زمان مشخصی برای اجرای این طرح تعیین نشده است. دفتر رسانه‌ای حوثی‌ها به درخواست رویترز برای اظهار نظر پاسخ نداد.
دو مقام منطقه‌ای که از سوی جمهوری اسلامی در جریان این موضوع قرار گرفته‌اند، به رویترز گفتند مقام‌های حوثی در سفر خرداد به ایران برای شرکت در مراسم تشییع جنازه علی خامنه‌ای، درباره دریافت عوارض از کشتی‌های عبوری از باب‌المندب با مقام‌های جمهوری اسلامی گفت‌وگو کرده‌اند. به گفته منابع، هدف از این طرح عادی‌سازی دریافت عوارض از آبراه‌های بین‌المللی و افزایش فشار بر آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77613" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77612">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V822olabH7hzAJHfV83qqzj4P1h3wrhBibP3CpJ6TA3vVKaJoThFF1VWjk5mSx6_0m6NTudFAAC1jOllWA7dJ6fLTXYmlH-HQdYm9cMSqo2E2h4IA_SF2LrOla8xhDKMtk_-xikK407GQ3VEuhSM0qtKbXHnw8-qzt5LrIi-72FfGA-cXYMjBPasv6XQRDEQGCTnhctTWfyMzCleupnbSby0MKN0MujeteHKPhL3yR_k9_Hfu2a1PhP0TG-43f_MQC6YdgkfT1QqDpIr_QViWy7aX5BEHQmfnR3oKNboMKqwOE4KzwE5stSQpaIlvewGybDkmt5QEH2WoGgqvmES4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون دولتی جمهوری اسلامی گزارش داد منطقه‌ای در نوار مرزی پیرانشهر در استان آذربایجان غربی هدف حمله هوایی آمریکا قرار گرفته است. در این گزارش آمده است: «منطقه‌ای در نوار مرزی پیرانشهر مورد حمله هوایی دشمن آمریکایی قرار گرفت.»
پیش از آن، خبرگزاری فارس به نقل از یک مقام استان آذربایجان غربی گزارش داده بود موشکی به منطقه‌ای غیرمسکونی اصابت کرده و تلفاتی بر جای نگذاشته است.
فرماندهی مرکزی آمریکا تاکنون این حمله را تأیید نکرده و درباره آن اظهار نظری نکرده است. تأیید مستقلی نیز برای این گزارش وجود ندارد.
پیرانشهر در غرب استان آذربایجان غربی و در نزدیکی مرز عراق قرار دارد. این شهر پنج روز پیش نیز بر پایه گزارش سازمان مدیریت بحران استان به خبرگزاری ایرنا، هدف حمله هوایی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77612" target="_blank">📅 16:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/prWGmKWBHOLQamN_UJsZOziqD29rBgxTJw3pfap7vyycUjeT1TTCFsyGCftqhVK_EpmdYas5dirq9LAJg3MDdfcG7q00wylXr086EcMRz7GsKW7vv50u4llPM1cm-rX8hLOObNOC8EHgQnmfEzgi8g6hnomc8MkdFeqirzllqwPpzTQZhmnZuLZ2jbmj9YwJxn2QulJmnGDnBkF3wyw6RkpdvmjqleRY8gZos_p9xn-wbOSGoSnknF896f_FuWVdKj1K1Uo1pRafKUXQEUXJxn2LfAHhBTRWLoe8DPPPpZHohXiU6BGn89i_gBhHOtnJoi78a22nZQsGUKQtU8rJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر، رهبر جریان صدر عراق و از رهبران شیعیان عراق، با انتشار بیانیه‌ای از سپاه پاسداران خواست خاک عراق را هدف حملات خود قرار ندهد و هم‌زمان از گروه‌های مسلح عراقی نیز خواست با اقدامات خود به کشورهای منطقه بهانه حمله ندهند.
صدر در این بیانیه که روز چهارشنبه هفتم مرداد منتشر شد، نوشت عراق نباید به محلی برای هدف قرار دادن جمهوری اسلامی تبدیل شود و از «برادران در سپاه پاسداران» خواست از حمله به «سرزمین مقدس و مستقل عراق» خودداری کنند.
او همچنین از آنچه «میلیشیاهای خودسر» خواند، خواست با اقدامات خود زمینه حمله کشورهای عربی خلیج فارس به عراق را فراهم نکنند.
رهبر جریان صدر با محکوم کردن هدف قرار گرفتن خاک عراق از سوی هر کشور یا هر طرفی، از دولت بغداد خواست حاکمیت خود را اعمال کند، امنیت را برقرار سازد و مانع کشیده شدن این کشور به جنگ و درگیری‌های فرقه‌ای شود. او تاکید کرد عراق و مردمش بیش از هر چیز به صلح نیاز دارند و سال‌ها جنگ، توان و ظرفیت‌های این کشور را فرسوده است.
این بیانیه در شرایطی منتشر شده که از آغاز جنگ ۴۰ روزه، سپاه پاسداران بارها مواضع احزاب کُرد در اقلیم کُردستان عراق را هدف قرار داده است. هم‌زمان، فرماندهی مرکزی ارتش آمریکا (سنتکام) بامداد چهارشنبه هفتم مرداد اعلام کرد نیروهای آمریکایی و عربستان سعودی در یک عملیات مشترک، مواضع گروه‌های مسلح همسو با جمهوری اسلامی در عراق را هدف قرار داده‌اند.
@
VahidHeadline
مقتدی صدر در بیانیه‌اش به جای خلیج فارس از عبارت دیگری استفاده کرده:
Mu_AlSadr
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77611" target="_blank">📅 16:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvpZ-3Gr8H28oKZleaItFyVrtwUbos56IZh9SNdsuMqBfidj-xMJN3zozV5lD8f-DIlwz61NV6vRfclrK80JgO9NO4YAq2rRkDYxbh4p389-4vYVOzmzgu7G2UNfympVw7wJJgKy83-zbEK18YCl3Sidek8193gigrBR4uerIuH4F1bSFepGX1Fce5WjrTT8MtGnFiUwZP1NVMPB0ok5Ew4nunrRVYlq8XosZDVGOK_y765RjNo6ZhMZTWcQgWYQ9BnmhYWYBHP6iEk8KHfmDmxQiTXcoOTRPDeJZ1JezpOvOTARGKcIoRmYbdNYB-EUu-xGL4SvNE8myKmY5r7GhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ نیویورک‌تایمز، به نقل از چند مقام ایرانی و غربی که نام‌شان اعلام نشده، گزارش داد که حکومت ایران قصد داشت در واکنش به حملهٔ اوکراین به یک کشتی ایرانی، به یک بندر در اوکراین حمله کند، اما به‌دنبال اقدامات دیپلماتیک از انجام این اقدام خودداری کرد.
این روزنامه به نقل از این مقام‌ها نوشته است که انتظار می‌رفت ایران در این حمله یک موشک بالستیک با کلاهک کوچک به سمت اوکراین شلیک کند تا خسارت نسبتاً کمی به بار آورد و به‌صورت نمادین پاسخی به حملهٔ اوکراین داده باشد. این مقام‌ها گفتند که هدف حمله احتمالاً یکی از بنادر اوکراین در دریای سیاه بود.
بر اساس این گزارش بامداد چهارشنبه هفتم مرداد منتشر شد، مقام‌های جمهوری اسلامی امیدوار بودند این درگیری با حملهٔ تلافی‌جویانهٔ آن‌ها پایان یابد، اما مقام‌های غربی هشدار دادند که پیش‌بینی چگونگی واکنش اوکراین دشوار است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/77610" target="_blank">📅 16:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G9MnHPgIH_4-Ow3QxVd0ue918So6GICdTuCveIZt5-KsJGYh2-WKI6sPywPQHUQn0uFMHhTObUlx8fLW-ogB7tL6zQZts4T8tGvlzg4mKuuaLb6s70WCSwWD3Vvj-BTHLO8yLtaEXxGgOIKDE1su82fqUXcuIao9IwjtEYysgG-sBRPifV_lrOEYJHNH5kKnBKm4bpiEiCNlxYVWRjxZijopjCHwKYVPSKLVOiXEjp-M-pZBZV80cX3OOriX3bWiRgRN7DqAW_k-IOty41sgeekrOx8fBrWyeliIak2t0L41l7M_xS1V3xUqiW23zq97PGwjPWE0PDEkUJHb3U7ZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gMsgyzoNLZ1E0ePbEKh-BId4RVbnGr5Drz6myhckpcnLT6fNokTJFa0oK13W-FjoAv-g6N1b8zrWq7XOBGyzCfKUNhFk4w5yKN_aj2KzyZ44HNLFoYRoqJMqAKGDlKVI4iX_jc5dW9y1o3Xw14anMTvqb9ISSVhPy5vBPZlET1mWfV0qEtowYUhy8Ai5P9nlwz2pVWJnlgTL4RCVUIesR-oTAhKvs48R4TLigtJtba37yP2cJB8knnU-G0uHGXTNBnWBYT0JlxTu-kCDkPBEsSyvfybjhvMyGRvwppEBMOn0sDlNFq-Wa-x3mM37q_kwWkxLVapmEovOxP5jMf02kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برخی رسانه‌های ایران و کانال‌های مرتبط با سپاه پاسداران گزارش دادند که چهار عضو سپاه پاسداران در حملات منتسب به آمریکا و عربستان سعودی به عراق کشته شدند.
به نوشته این رسانه‌ها، این افراد در حمله‌ای به کربلا جان باختند.
بر اساس این گزارش‌ها، علی اصغر آستانه، ابوالفضل متقی، مرتضی اکبری و امیرعباس درهم‌فروش از جمله کشته‌شدگان هستند.
@
VahidOOnLine
شبه‌نظامیان حشد‌ الشعبی صبح چهارشنبه هفتم مرداد اعلام کردند شمار کشته‌های حملات هوایی مشترک آمریکا و عربستان سعودی به پایگاه‌های این نیروهای تحت حمایت ایران به ۲۰ نفر رسیده است.
حشد الشعبی در بیانیه‌اش این میزان تلفات را آمار «اولیه» خوانده و گفته است که دست کم ۳۲ نفر نیز در این حملات مجروح شده‌اند.
حملات مشترک آمریکا و عربستان علیه مواضع نیروهای حشد الشعبی در بغداد، واسط، نینوا، بصره، کرکوک، کربلا و دیاله انجام شد و خسارات مادی به تأسیسات و تجهیزات نظامی نیروهای حشد الشعبی وارد کرد.
فرماندهی مرکزی ارتش آمریکا در بیانیه‌اش گفته بود که این شبه‌نظامیان طی روزهای اخیر بیش از ۲۴ حمله پهپادی انجام داده‌اند.
به‌گفتهٔ سنتکام، هدف این حملات «تروریست‌های همسو با ایران» بوده است که سپاه پاسداران انقلاب اسلامی آن‌ها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان سعودی هدایت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/77608" target="_blank">📅 16:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=Qkd45U66EI3B7745ln5lKIUVqArCaz5KcC7juKuTj1niTbD0ekcD1PZKPJL2ECSBvdUFQolohGi7oaVTUE64TgyLAYlNryQA03Q7TqZuSvNh8f1SWjCZMufkQCZpi6zh-kTxd4of0-EoX9xEPMGkcwn-ZGRz_3LbytVKLqOVA6d-VawLI_KJHMPp3ygTmoiBpowB6rrjra51NcIVBUEhKqQikSv1RYfzHjpto3ZtdKIdP4OVUX18CW51fUpiR7zNdyA-xr663uhq3FTS0hIBgpXyrH9BFfobFs4drEhnP3yMKphlkosMFZr_YVfy0MoWVxAuRT0jDNVo5DRqXgqVp0UVxiFnPSsysHCPt8UxyCFjz5nRN7Ls0i-BSj6oxwhM3i-Rx4uBLqvMngFEzM9LjWJZV9N5s2tw05pdlRXztHnqTylcJ9VsA0v0ZIQCHyEoAhI1G_NMzLP8OGiyfbaUmpiU5etrZVE-GQG73V4BCR6LOx3C3MezPQziQ_PfmB1bvgfDPDGQq6mVJkgqGzN3NeYOBUxwnfCjd-9Pk2d_ZtVXZzZfEqhMInkqfR7tFszX1yd2vLxt50Khd1fyhIhCinf_i3wh98r4Qlg4aGXoZKww5iHSrORQA1g7Q3e0nXFfKPNNXLsBXewG1FzAz9cknXXatdUIn8pbjEk517I-1es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c924ab1dab.mp4?token=Qkd45U66EI3B7745ln5lKIUVqArCaz5KcC7juKuTj1niTbD0ekcD1PZKPJL2ECSBvdUFQolohGi7oaVTUE64TgyLAYlNryQA03Q7TqZuSvNh8f1SWjCZMufkQCZpi6zh-kTxd4of0-EoX9xEPMGkcwn-ZGRz_3LbytVKLqOVA6d-VawLI_KJHMPp3ygTmoiBpowB6rrjra51NcIVBUEhKqQikSv1RYfzHjpto3ZtdKIdP4OVUX18CW51fUpiR7zNdyA-xr663uhq3FTS0hIBgpXyrH9BFfobFs4drEhnP3yMKphlkosMFZr_YVfy0MoWVxAuRT0jDNVo5DRqXgqVp0UVxiFnPSsysHCPt8UxyCFjz5nRN7Ls0i-BSj6oxwhM3i-Rx4uBLqvMngFEzM9LjWJZV9N5s2tw05pdlRXztHnqTylcJ9VsA0v0ZIQCHyEoAhI1G_NMzLP8OGiyfbaUmpiU5etrZVE-GQG73V4BCR6LOx3C3MezPQziQ_PfmB1bvgfDPDGQq6mVJkgqGzN3NeYOBUxwnfCjd-9Pk2d_ZtVXZzZfEqhMInkqfR7tFszX1yd2vLxt50Khd1fyhIhCinf_i3wh98r4Qlg4aGXoZKww5iHSrORQA1g7Q3e0nXFfKPNNXLsBXewG1FzAz9cknXXatdUIn8pbjEk517I-1es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند از ابتدای سال ۲۰۲۶ تاکنون، اعدام دست‌کم ۸۸۶ نفر در ایران را مستند کرده است که ۵۶ مورد آن تنها در ماه ژوئیه انجام شده است.
🔸
زندان قزل‌حصار یکی از بالاترین آمار اجرای احکام اعدام را در سراسر کشور دارد. همچنین بخش قابل‌توجهی از اعدام‌های صورت‌گرفته در ایران مربوط به جرایم مرتبط با مواد مخدر است؛ به‌طوری که طبق داده‌های گردآوری‌شده توسط بنیاد عبدالرحمن برومند، نزدیک به ۴۵ درصد (۲,۹۴۶ مورد) از کل اعدام‌های ثبت‌شده در بازه ۱۰ ساله ۲۰۱۶ تا ۲۰۲۵، مرتبط با مواد مخدر بوده است.
🔸
از ۲۲ تیرماه، در پی انتقال شش زندانی محکوم به اعدام در پرونده‌های مواد مخدر به سلول‌های انفرادی زندان قزل‌حصار، جمعی از زندانیان واحد دو این زندان دست به اعتصاب غذا زده و برخی نیز لب‌های خود را دوخته‌اند.
🔸
با گذشت بیش از دو هفته از آغاز این اعتصاب، مسئولان نه تنها هیچ پاسخی به خواسته‌های اعتصابیون نداده‌اند، بلکه با اقداماتی همچون جابه‌جایی زندانیان و ایجاد محدودیت‌های شدیدتر برای جلوگیری از ارسال پیام و ویدیو از داخل زندان، در تلاش‌اند صدای آنان را خفه کنند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77607" target="_blank">📅 16:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77606">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رویترز: منابع می‌گویند ایران ظرف چند هفته سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد
▪️
منابع می‌گویند قرارداد شامل ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی دوش‌پرتاب QW-12 و FN-16 است
▪️
منابع می‌گویند ارزش این معامله ۶۰ تا ۷۰ میلیون دلار است
▪️
چین این گزارش را بی‌اساس خوانده و پاکستان دخالت در انتقال‌ها را رد کرده است
ترجمه ماشین:
۲۹ ژوئیه (رویترز) — سه منبع آگاه از این معامله به رویترز گفتند ایران قرار است ظرف چند هفته نخستین محموله از مجموع حداکثر ۴۰۰ پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که هم‌زمان با بازسازی توان دفاعی این کشور در میانه جنگ با ایالات متحده صورت می‌گیرد.
این خرید که ارزش آن ۶۰ تا ۷۰ میلیون دلار برآورد شده، یکی از بزرگ‌ترین تلاش‌های شناخته‌شده تهران برای تقویت پدافند هوایی کوتاه‌برد خود از زمان آغاز جنگ با آمریکا و اسرائیل است؛ جنگی که ضعف‌هایی را در توانایی ایران برای حفاظت از مراکز نظامی و زیرساخت‌های راهبردی آشکار کرد.
با خبرنامه Trading Day، تحولات بازارهای جهانی را بهتر درک کنید. از اینجا ثبت‌نام کنید.
به گفته منابع، این قرارداد خرید بین ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، شامل موشک‌های چینی QW-12 و FN-16 را در بر می‌گیرد.
این قرارداد با شرکت Zhongqing Baoshang International Investment، مستقر در هنگ‌کنگ، امضا شده است؛ شرکتی که به گفته منابع، به‌عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
ایران پس از ماه‌ها جنگ نیاز به تجدید تسلیحات دارد
منابع به‌دلیل حساسیت موضوع، به شرط ناشناس ماندن صحبت کردند. وزارت امور خارجه ایران بلافاصله به درخواست اظهارنظر پاسخ نداد.
وزارت امور خارجه چین اعلام کرد: «گزارش‌های مربوطه کاملاً بی‌اساس هستند. چین همواره در جهت ترویج صلح و پایان دادن به درگیری نقش ایفا کرده است.»
گروه Zhong Qing Bao Shang مستقر در پکن، شرکت مادر Zhongqing Baoshang International Investment، تا روز سه‌شنبه به درخواست اظهارنظر ایمیلی پاسخی نداده بود.
ایران پس از ماه‌ها درگیری، که طی آن آمریکا و اسرائیل تأسیسات مرتبط با برنامه‌های موشکی، پهپادی و پدافند هوایی این کشور را هدف قرار داده‌اند و تهران نیز با شلیک انبوه موشک‌های بالستیک و پهپادها پاسخ داده، نیازمند تجدید تسلیحات است.
این درگیری دشواری دفاع از مراکز ثابت نظامی و راهبردی در برابر هواپیماهای پیشرفته و تسلیحات هدایت‌شونده دقیق را برجسته کرده است.
واشنگتن روز شنبه به‌طور ناگهانی بمباران‌های دو هفته‌ای خود را متوقف کرد، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت اگر مذاکرات برای پایان دادن به این درگیری پنج‌ماهه شکست بخورد، حملات از سر گرفته خواهد شد؛ درگیری‌ای که در ظاهر از ماه آوریل در وضعیت آتش‌بس قرار داشته است.
تحویل صدها سامانه پدافند هوایی دوش‌پرتاب، موجودی تسلیحات پدافند هوایی کوتاه‌برد ایران را به‌طور قابل‌توجهی افزایش خواهد داد و نشان می‌دهد روابط نظامی این کشور با چین در حال عمیق‌تر شدن است.
منابع هشدار دادند که هرچند توافق امضا شده است، برنامه زمانی تحویل، تعداد سامانه‌ها و دیگر جزئیات اجرایی همچنان ممکن است تغییر کند.
بر اساس طرحی که طرفین بر سر آن توافق کرده‌اند، تحویل‌ها در مرحله نخست از طریق هوایی و از ارومچی در غرب چین انجام خواهد شد و سپس با عبور از پاکستان به ایران خواهد رسید. منابع مشخص نکردند که انتقال از پاکستان به ایران هوایی خواهد بود یا زمینی.
روابط عمومی ارتش پاکستان، ISPR، اعلام کرد: «گمانه‌زنی‌ها درباره دخالت پاکستان در انتقال تسلیحات پدافند هوایی از چین به ایران کاملاً ساختگی و نادرست است.» سخنگوی وزارت امور خارجه پاکستان به درخواست‌ها برای اظهارنظر پاسخ نداد.
منابع می‌گویند چین و ایران مسیرهای زمینی برای تحویل را بررسی می‌کنند
کارشناسان نظامی می‌گویند با آنکه ایران طی دو دهه گذشته سرمایه‌گذاری گسترده‌ای در زمینه موشک‌ها، پهپادها و رادارها انجام داده است، سامانه‌های پدافند هوایی قابل‌حمل اهمیت دارند، زیرا می‌توان آن‌ها را به‌سرعت پراکنده کرد، با تیم‌های کوچک به کار گرفت و مرتباً جابه‌جا کرد؛ ویژگی‌هایی که آن‌ها را در مقایسه با آتشبارهای ثابت پدافند هوایی کمتر آسیب‌پذیر می‌کند.
یک منبع امنیتی اروپایی گفت مقام‌های کشورش از چند قرارداد در حال مذاکره درباره فروش احتمالی سامانه‌های پدافند هوایی دوش‌پرتاب سری QW به ایران، از جمله سامانه‌های QW-12، QW-18 و QW-19، اطلاع دارند.
یک منبع امنیتی دوم در خاورمیانه گفت ایران به‌دنبال خرید موشک‌های QW-12 و QW-18 بوده است، اما او از نهایی شدن قرارداد اطلاعی نداشته است.
‏QW-12 و FN-16 سامانه‌های موشکی زمین‌به‌هوای دوش‌پرتاب و هدایت‌شونده با فروسرخ هستند که برای درگیری با هواپیماهای در ارتفاع پایین، بالگردها و پهپادها طراحی شده‌اند. قابلیت تحرک آن‌ها امکان استقرار سریع در اطراف تأسیسات نظامی، زیرساخت‌های انرژی و دیگر مراکز حساس را فراهم می‌کند.
تحلیلگران دفاعی QW-12 را ضعیف‌تر از مدل‌های جدیدتر خانواده QW، از جمله QW-18 و QW-19، می‌دانند، اما می‌گویند این سامانه‌ها همچنان می‌توانند لایه‌ای مؤثر از حفاظت کوتاه‌برد در برابر پهپادها و اهدافی که در ارتفاع پایین پرواز می‌کنند فراهم کنند.
دو منبع اطلاعاتی غربی و یک مقام ایرانی گفتند تهران همچنین استفاده از مسیرهای زمینی را برای انتقال محرمانه‌تر تجهیزات نظامی و قطعات دومنظوره چینی و کاهش خطر ایجاد اختلال در انتقال بررسی کرده است.
این خرید نشان‌دهنده تداوم اتکای جمهوری اسلامی به ترکیبی از تولید داخلی تسلیحات و تأمین‌کنندگان خارجی، با وجود سال‌ها تحریم و محدودیت بر واردات مرتبط با امور دفاعی، است.
رویترز پیش‌تر به نقل از افراد آگاه از مذاکرات گزارش داده بود که ایران به امضای توافق جداگانه‌ای با چین برای خرید موشک‌های کروز ضدکشتی نزدیک شده است. رویترز نتوانست مشخص کند که آیا آن توافق نهایی شده است یا نه.
reuters
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77606" target="_blank">📅 08:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Llni2_NFb5BWI7jb_Fw4ncKkM8EYU7DLoEp7N_gdzAFUtIM5DglpibFyhDxzhtmvZQ0wnm1fiHOjmHVXNEjOsXhQ9h0tDqnsHqz0IJA0V7zrodbhxsZpNwwSvkVCEmOS0ZGb2wC1G7KxwERBj0woIv7ZI79vFh0Ym0mxxZmEFwV6SGHbAic9Tyl7OzunFp6eX8j3WYdEXVr3tvjF0HeoBTab2Vs1jHvzsBik01TfYp9d3YxlQWgKP5lPlOI2sVsQ-M7PjiUMxZSLo9SBWPcrwXvlsBKwXq54eJLARTyBuSvNUU-CE1P7ycbULI5APc4JHMAjIhlXrKZB1CALhjuG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی ایران هویت خلبان کشته شده مجید کاظمی رو پس از چند ماه اعلام کرد.
نوشتند یکی از ۴ خلبان دو جنگنده سوخو ۲۴ بوده که در حمله به نیروهای آمریکایی در پایگاه العدید قطر هواپیماشون مورد هدف قرار گرفت.
نوشتند تلاش‌ها برای تعیین وضعیت ۳ نفر دیگر همچنان در جریان است و مجید کاظمی هم با آزمایش‌های تخصصی و بررسی DNA هویتش تایید شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77605" target="_blank">📅 07:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77604">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7tNM_CuSQqC84u4bIwocfy7bdGLBqsvPsjKSi4yY1Lz_hjapMK2RiHkipLuxHfpSCHGt1McH8CBXNDUJVFQvodhlIdet6oCskm6WssXEVXFrZX4_e7YczWEl5TrX9HFccEJtrRQL7dZ3w2Mvr4pQiYSKsk9vSZqNj13FKR80ZSjJ52LFXk6VvzKlZ-wgaramYYoCwPl-srx0m4Hkb77h91jAFBnavGTBovKled-mardyV0Q8UL4i-ofH0H7GW_aSy_OGHb55ZcZQAEt1SkBKp8cIBuEFFbmE8-Z-jmNWiSyRG13Zt9vHjS8jETSLo6F2Uj756AyStVyNvEVinpo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران، صبح چهارشنبه، با انتشار دو بیانیه از حمله موشکی به پایگاه هوایی و مرکز فرماندهی ارتش آمریکا در اردن و همچنین هدف قرار دادن سه نفت‌کش خبر داد.
نیروی هوافضای سپاه اعلام کرد پایگاه نیروهای آمریکایی در اردن را با چند موشک بالستیک هدف قرار داده و هم‌زمان نیروی دریایی سپاه نیز گفت: «سه نفت‌کش متخلف که به اخطارها بی‌توجه بودند مورد اصابت قرار گرفته و متوقف شدند.»
این درحالی است که پیش از این، فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار بیانیه‌ای اعلام کرد که تمام موشک‌های شلیک‌شده سپاه از ایران به طور کامل رهگیری و منهدم شده‌اند و هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77604" target="_blank">📅 05:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77603">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، می‌گوید دونالد ترامپ، رئیس‌جمهوری آمریکا، با اعطای مجوزهای لازم برای تولید موشک‌های سامانه پاتریوت به اوکراین موافقت کرده است.
آقای زلنسکی شامگاه سه‌شنبه در گفت‌وگو با شبکه فاکس‌نیوز گفت پس از دیدار با آقای ترامپ، با نمایندگان چند شرکت بزرگ تسلیحاتی آمریکا نیز گفت‌وگو کرده و امیدوار است زمینه تولید مشترک این موشک‌ها فراهم شود.
رئیس‌جمهوری اوکراین که روز سه‌شنبه در واشینگتن با دونالد ترامپ دیدار کرد، تأکید کرد مهم‌ترین نیاز نظامی کی‌یف همچنان سامانه‌ها و موشک‌های دفاع ضدبالستیک است.
هم‌زمان، سنای آمریکا با ۸۶ رأی موافق در برابر ۱۲ رأی مخالف، طرح گسترده‌ای را برای تشدید فشار اقتصادی بر روسیه و ایران به مرحله بعد فرستاد. این طرح که به نام لیندزی گراهام، سناتور جمهوری‌خواه درگذشته، نام‌گذاری شده است، به رئیس‌جمهوری آمریکا اجازه می‌دهد بر بزرگ‌ترین خریداران نفت و گاز روسیه تعرفه‌هایی تا سقف ۲۰۰ درصد وضع کند و تحریم‌ها علیه نهادهای مالی، مقام‌ها، الیگارش‌ها و ناوگان موسوم به «سایه» روسیه را گسترش دهد.
این طرح هنوز باید در رأی‌گیری نهایی سنا تصویب شود و سپس برای بررسی به مجلس نمایندگان برود؛ مجلسی که تا پایان تعطیلات ماه اوت تشکیل جلسه نخواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77603" target="_blank">📅 05:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77602">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxSkyqvvMbUVyah3DPlkmuDUkNCZZv1-_6Kxw2eVBKQl4zzchwCuNahGrXLsCy3vLgPvxgoSLaXOCB5etHZvdIDe1eELyRLAPIsuLe3T9-Tig3S8ZlvyEl8eZ94JZ_y3u4sXrG507v2A-K1wz7T5K4sGTb9bVOpipT9fSsCJcazEhz8c2z9nszP9wl1wmMH5HkWXKHxi9jBzwbte0BiTdQgqS3rLuMI1act0nd8Y3anLEacbCXqafCNNDqjBogA8466uBAHeP-sN5U6mvcFHerJjS0HpXJot1LLaCwLCzUr1v2HMxm8UyxvAmm15ooHPtLtb7Vcno9h3zNkzNV2zlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، با انتشار تصاویری در «تروث سوشال» از دیدارهای جداگانه خود با رهبران اسرائیل و اوکراین، درباره دیدار با بنیامین نتانیاهو نوشت:
«نخست‌وزیر بی‌بی نتانیاهو از اسرائیل، همراه با من و نمایندگان، نشست بسیار خوبی داشتیم. بدیهی است که موضوعات مهم متعددی مورد بحث قرار گرفت.»
ترامپ همچنین با ابراز خرسندی از دیدار با ولودیمیر زلنسکی افزود: «دیدار با زلنسکی از اوکراین افتخار بزرگی بود. موارد زیادی بررسی شد و این نشست بسیار خوب پیش رفت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77602" target="_blank">📅 05:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vL5acR22QC7iuPqIFenGhqZHppTRie7tieq-fJ_Ja-D0ssVeKmm6rrtn2Y5WSAzn9S7V00IGa2Xp85hvWFTM-v8bAJ4yAZ85vSCrphTutM_Ojsos0WORkHK2ppg6sIE_M87hTKYkHs2Wo_9u35ZIba7acoWwdbh3gHSvQ7i73Y_qUQdFcZEtBGE5r_CH37dUrp1xTgLFCjMOYJolp9ytNrmRq1uW0uaSOfG8s_M3wpq0zTk8MUU4O3VEcLyLij8L6KATxHXDC7IRaJxovg3I0SaVQ7G4sPopgTpBNg8dZL60JZnaWe2lFDgyTHeMoxyUYDc9Ygm8jWzXb2xCiO0Bmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر پست شده در اکانت سنتکام
متن پست، ترجمه ماشین:
نیروهای آمریکا و عربستان مواضع تروریستی مورد حمایت ایران در عراق را هدف قرار دادند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده و نیروهای مسلح عربستان سعودی روز ۲۸ ژوئیه حملات دقیقی را در عراق علیه تروریست‌های همسو با ایران انجام دادند؛ عناصری که سپاه پاسداران انقلاب اسلامی آن‌ها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان هدایت کرده بود.
جنگنده‌های آمریکایی و سعودی در پاسخی قاطع به بیش از ۳۰ حمله پهپادی هوایی که طی ۷۲ ساعت گذشته به دستور سپاه پاسداران انجام شده بود، چندین مرکز لجستیکی و انبار تسلیحاتی تروریست‌ها را در سراسر شرق عراق هدف قرار دادند.
حملات ناموجه علیه نیروهای آمریکایی موفقیت‌آمیز نبود.
از فوریه تا آوریل ۲۰۲۶، شبه‌نظامیان تروریست همسو با ایران در عراق بیش از ۶۰۰ بار تلاش کردند به شهروندان و تأسیسات آمریکایی حمله کنند.
سپاه پاسداران و نیروهای نیابتی تروریستی آن باید برای جلوگیری از واکنش نظامی بیشتر ایالات متحده، این حملات را متوقف کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77601" target="_blank">📅 04:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77600">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZcF4i9fRefsexfIbGAoidTI0Asikq-nbuqGtzGP22Ktk1JqRedm9TSvOxx-RRy4BWGmEOSCmJPRLi92tOqHdPPthgsY0zBLRAduQplTCfCBrlxUXJ0ZJUTk3iO5Pw0zZlsPHbfqS37-icINgkEPBtC-vS58JXwvw0YBNlMU2L_3IUVtuhD_jOdHAM8Gt4nDmsWyxLOTJIB6JPOFLw_jGeic7aB1xLlQJAJ-4xfQAnZOw6YWI7-Ktq0CKxJDWF4z4zkVwOjDIxOH9YHPU3Q7NVE5f0XOY7AAVaOTisQuBusu68_mgVuONYrZ_xIX9I0jwprhm_E5_KpwJAXTR4TL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد پدافند هوایی این کشور چند پهپاد را که تأسیسات نفتی در استان شرقیهٔ این کشور را هدف گرفته بودند، رهگیری و منهدم کرده است.
ترکی المالکی، سخنگوی وزارت دفاع عربستان، روز سه‌شنبه در شبکه اجتماعی ایکس گفت این پهپادها از خاک عراق و به دست گروه‌هایی که او «شبه‌نظامیان تروریستی مورد حمایت ایران» خواند، پرتاب شده بودند.
او افزود عربستان سعودی حق مشروع دفاع از خود و تأسیسات حیاتی‌اش را محفوظ می‌داند و «در زمان و مکان مناسب» به این حملات پاسخ خواهد داد.
@
VahidHeadline
خبرگزاری صدا و سیما می‌گوید که یک »مقام آگاه نظامی» در ایران، در واکنش به اظهارات وزیر دفاع عربستان سعودی، هرگونه ارتباط جمهوری اسلامی با پرتابه‌های شلیک‌شده از خاک دیگر کشورها به سوی اهدافی در عربستان را «قویاً» تکذیب کرده است.
این مقام که نام او اعلام نشده است، به این خبرگزاری گفت نسبت دادن هرگونه اقدام علیه منافع آمریکا در منطقه به جمهوری اسلامی ایران، «خطای بزرگ محاسباتی» و ناشی از «کم‌اطلاعی از اوضاع منطقه» است.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77600" target="_blank">📅 04:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YylQpZhHql7Ewqie1hGaOfB_GzY7y87vlj1tQgKYqo5OjJraB-diWmktSE2jKMt68bIbMlO3Q50RTyJ8f1M2H7WwGtGowNlrwhovhB7KLQ1-hhS0qIi-aVMJIp_pSm9UQXTUwrp1B4NQo0mPcgmg2IQk1eF63ysTvN5fFlzhryHgsYTxDNQGZiiiE_b1ZQGC8dHRlBFkOHkyuXJN-kcSMSZjbsjbV5STvfZ7V87SUgOFpoWUs9F2km7neOjYzfEI_zqpGxNEdZbcnYCAfxaoxT0U9sGHIbEJl87RUUSTGrnJuhz8zSz9e41momsPBFYK15y1P0lL2psP1y6QcAw-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرق آمریکا [۱:۱۵ چهارشنبه به وقت تهران]، نیروهای سپاه پاسداران انقلاب اسلامی چندین موشک بالستیک را از ایران، در تلاشی برای انجام حمله‌ای غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند.
همه موشک‌های ایران با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنان هوشیار و در بالاترین سطح آمادگی قرار دارند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77599" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I5Va05atL8PCKZkxfeQKe_6QfgHBCX_vKWS-wwXulv3iakG980JTQOAYYYpP19PkSLGrFMhKxYPhMU03lszY7aDb2lJyP5cZRj0LpesQr4e8k_eTDyouctxe-ILYsnU7xqbAzO6NrcdVRyTaKcXezN-Tnv_dFaJRtse3BoT1OFFiYttmGTxBVsSL0qx5MclpMml_l5e8npNm6VXVp4yVzrXxMrdU4wfXDDB6Dx3ZGaQUvulg5kdw9yGnOfc7_Lc4JYxlA_iY9LOXvsfy1UNSL8HhaknWDMdXpY8xyz0xnK0HVAguKqBK5BJ36l7I7FNgZWuIE8zJwsZX3oUD2xXHpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JB_fLABP5rk1t1T_MIdBpcLkUpWAXqrxL_o3tZ1p9x9k9gZGV6xabpHjwxYBwrm4oSQmQ4IDt74pXajoIDOsY81YtGQwnLRMaWNGP4AIJdGuubjZRBOudftvj-oU811J1uHr8o-9uoBkmapy3oc6VvoYW1e-vVjJQE5I88ivpw-08PwiL98bUtEPJMbgkZmn2aa3bYRbePSJdqC7XPTzW0uAFie0imqj3yZJv-hSqHhEXME6T5kOTtzbv7v6WU_QHu6d1GLvajg1vtMjEZyK7P-ndpUKdVFuPep-o73tX4VD75c38CMIRCRtJTfsxLAV7H8kLU1DxwJOMKZi1aLHaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=aTXl-Uj2dUeT2CFejYz_wWmj3-hDfqzOvRJZ1JGFXNi1td0ErrrulHQUcZvKRzi2gf1R_nGoccKRY_opY6J_29AxZ0ZvIWH-UMJkKfsVMHf1o-3oKQ7GopnqgU6h2fM4ODPsiEt7JHlrL4C6MOdaZqGuYwHYzacYDbRc4jXhXOWTIjUTVekegTGiiSXnxRgtrwONkhZo6setbOMI2pBdHJWOBITpSWNh070VcXoNjDag2DTVdd1Q7kUclKXhn2n_6virK-QpQCZZ5z3W2nWZaG0pkzDYix0MOJJtbCmxtX-6c2tMIe2FQ6obSSc-17DhCpt4sKEIsRm6zqDkgwGIKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=aTXl-Uj2dUeT2CFejYz_wWmj3-hDfqzOvRJZ1JGFXNi1td0ErrrulHQUcZvKRzi2gf1R_nGoccKRY_opY6J_29AxZ0ZvIWH-UMJkKfsVMHf1o-3oKQ7GopnqgU6h2fM4ODPsiEt7JHlrL4C6MOdaZqGuYwHYzacYDbRc4jXhXOWTIjUTVekegTGiiSXnxRgtrwONkhZo6setbOMI2pBdHJWOBITpSWNh070VcXoNjDag2DTVdd1Q7kUclKXhn2n_6virK-QpQCZZ5z3W2nWZaG0pkzDYix0MOJJtbCmxtX-6c2tMIe2FQ6obSSc-17DhCpt4sKEIsRm6zqDkgwGIKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'پرتاب شدن چند موشک از
#خمین
'
تصاویر دریافتی از شهروندان با شرح بالا
چهارشنبه ۷ مرداد حدود ساعت ۱:۱۰ بامداد
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77595" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oq6SsTEnAwPhIRCpxPsU4mVuW2qBAoDUScKQM8p5AfP2mtrpYyVK6b8gOrlEXwU01C0sodSHFV_jRlT4grwp9Jj7aKkO1PujpC9nRhQOfc2nW0uZLLmLiBm6izh5481brpF664TN29HqisBt6yOtdkHhw4Vh5OgL1ZpjSvT3lN8Xi9wIsjo81TBWYQALR0n9BZsSOG37IHfXv8IzmEIw-W4xSWehPlxj955fT30TFtIIFyR04gQLdjQGVsmNJaOwbSwKVjTlpNTk03CUs5HL9T9QwQCHvkM9NTGHxvqIg892KD2VakRge90VXZl5_Twls4Dl6De7LJfKzl4ZblWACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
از خمین موشک بلند شد
سه تا صدای انفجار
همین الان از خمین ۶تا موشک زدن
۳تاشون صدا نداشت فقط نور قرمز بود
سلام همین الان یک موشک از خمین رفت.
داداش
خمین موشک زد
ساعت ۱ و ده دقیقه
وحید داداش ۴ تا موشک از خمین زدن همین الان
از خمین موشک زدن
سلام،الیگودرزم،،صدا ۳ شلیک موشک اومد صدا دور بود احتمالا ازخمین بود
پرتاب سه موشک خمین
سلام وحید جان
سه تا موشک تو آسمون لرستان از سمت اراک دیده شد
صدای انفجار تو آسمون لرستان میاد
من ستا موشک بین نهاوند و بروجرد دیدم خمین نبود فک کنم نتکنستم عکس بگیرم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77594" target="_blank">📅 01:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77589">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=CHo_BCQ1Hh71SKwXsJlIJBeE4NjdF3CM5jsUaCFzPxT1osTUi-pm3k1Iefpw9vLFhLpeqyK2Z9kwAdNx12-FiLQT1mpdRR75PavMf8o6VvOdDDNlCdyA2GEgIWANs_ZZq5MfsF93S9rezQKibTbyTpeh6K0wGep-Ov1yh5LzmxHwbg_rCOU0jIPpLWGqNY5CqDqeItkTymChvmvDCEdaroFnezNI--BkecABKkr9VpcBOiVC8hwOshAOaCCbyobfjAWCeEXBhBxTgWle6KPUH-o9wap_QUWLgGC_l8nFoTet7YYdRCFXI0z0NIHkdWapMcRvk6ZLbOvSJuLXUYYQbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6b678bb6b2.mp4?token=CHo_BCQ1Hh71SKwXsJlIJBeE4NjdF3CM5jsUaCFzPxT1osTUi-pm3k1Iefpw9vLFhLpeqyK2Z9kwAdNx12-FiLQT1mpdRR75PavMf8o6VvOdDDNlCdyA2GEgIWANs_ZZq5MfsF93S9rezQKibTbyTpeh6K0wGep-Ov1yh5LzmxHwbg_rCOU0jIPpLWGqNY5CqDqeItkTymChvmvDCEdaroFnezNI--BkecABKkr9VpcBOiVC8hwOshAOaCCbyobfjAWCeEXBhBxTgWle6KPUH-o9wap_QUWLgGC_l8nFoTet7YYdRCFXI0z0NIHkdWapMcRvk6ZLbOvSJuLXUYYQbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم ادای احترام به لیندزی گراهام، سناتور جمهوری‌خواه که ۱۱ ژوئیه در ۷۱ سالگی درگذشت، در ساختمان کنگره آمریکا
به غیر از نزدیکان آقای گراهام، صدها نفر از قانو‌نگذاران آمریکایی در مراسم حضور داشتند.
برخی از رهبران جهان هم برای شرکت در این مراسم به پایتخت آمریکا سفر کرده‌اند.
سناتور گراهام از ایالت کارولینای جنوبی بود که چهار بار به عضویت سنای آمریکا انتخاب شده بود. او در سال‌های ابتدایی فعالیت سیاسی خود از منتقدان سرسخت دونالد ترامپ، رئیس‌جمهور آمریکا، به شمار می‌رفت اما بعدها به یکی از متحدان وفادار او در کنگره بدل شد.
او از چهره‌های شناخته‌شده جریان محافظه‌کار و از مخالفان سرسخت جمهوری اسلامی ایران بود و زمستان گذشته در جمع مخالفان حکومت ایران در آلمان حاضر شده و سخنرانی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77589" target="_blank">📅 00:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qvx7hLXY7PC81MTZT_Mcn4qP-5VPrzxgPNWJNv6iZefzgIDAp3gQgRJ6_fn6l12RmB0o8Q8JddnZo-Si3DXO-wHdy7nvdVE2_92BvwyzPCE343UMIL1Y6NrdMNH2kAVRFof0uiqWM4nOpacYUVHC1NO24SPmsipKBwZhZID2m-dXuVP0vu2bb36462cNk-gHto4zjVu4ZZ5edTwx4DIbEB9dtbwyA_AeEFOYMCguqFcHp_-a4FVaPv4kjWN7YxVfHyxjz279ZLWVpAn0E4cSmgZd2XJ0mrjK2V2mcto4iEZGBMntWQM5IJzaqVcBM4lm_RRtiZYc35E5Z5S887ibHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهنام نواب صفوی، ۲۲ ساله، خواننده رپ فارسی و از بازداشت‌شدگان دی‌ماه، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد به اعدام محکوم شده است.
این حکم با اتهام «محاربه از طریق مشارکت در تخریب اموال عمومی، تبلیغ علیه نظام و اجتماع و تبانی» صادر شده است.
به گفته منبع این گزارش، مهنام نواب صفوی دو وکیل داشته، اما وکلای او به پرونده دسترسی نداشتند و امکان دفاع از او برایشان فراهم نشده است.
همچنین دادگاه او به صورت غیرحضوری برگزار شده است.
مهنام نواب صفوی در جریان اعتراضات دی‌ماه در اصفهان بازداشت شد و اکنون در زندان دستگرد این شهر  است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77588" target="_blank">📅 23:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77587">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O3Ymdok3A8vH23NVow0SM8RUi_BXgfEKbCIFHvSpLUeE4EAr6Lu0nmYwstq4HNgtoC5H-i-XI_k4eBagRGiLeccWqlxZZUWgE0s1e9d4jVRBl9hrrC1CYd7zZDn3eOv-fucXmj0K9xoQqrp8HKDTPrnBb5Ln5W3XWPD2oOsjBS1S5GdsBYwzU4kow0MH2b_TO-2Wbffh6NLRMm38ksfDSwcKFvaNIkmGFZAmMZjcD0n6FbJF1Skho4zYMrx_7qY5rhidZASwJ8GFDz7oGekNavnqsuQLj3-ookYXnR4BkVLoJ_FuXAq28sxGXlQoVnKIEq9Tp97FfuG4Lx_Ga0IcOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:  برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.  بار دیگر تأکید کردم که تمام اقدامات…</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77587" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=EEu9p7Nh8r3PiK7nBvWjQp72GWNxHP9EmfKFoffql_ELwf_UXWwm26t1prFSbQUPexjL_2tJfpsnfl3TdmldSZ5uCtgd-8KNE56T_5hvZI1BqG0DzIzgxTmZ_7RyrTo-NUhzCPfUjflnpOlrubAgz6Gx7tuAY96LS8McSY5vS67pyoG4gS1ji-_ZMhQ4xCohdSsHk99_yd_eC2vyS_6xbF83JBLVqyvP8KsYUbK0G-PJoZv8AhIHIZ0ThdX8dQlvknD9xzEPjiGUPxvn58RG2TBD9giqRJX3LYaDBo9xEL1Wrqjt1BLyIHNXEseXu4bE6dDA21SN2FRIwjIEHSklog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54fee52c22.mp4?token=EEu9p7Nh8r3PiK7nBvWjQp72GWNxHP9EmfKFoffql_ELwf_UXWwm26t1prFSbQUPexjL_2tJfpsnfl3TdmldSZ5uCtgd-8KNE56T_5hvZI1BqG0DzIzgxTmZ_7RyrTo-NUhzCPfUjflnpOlrubAgz6Gx7tuAY96LS8McSY5vS67pyoG4gS1ji-_ZMhQ4xCohdSsHk99_yd_eC2vyS_6xbF83JBLVqyvP8KsYUbK0G-PJoZv8AhIHIZ0ThdX8dQlvknD9xzEPjiGUPxvn58RG2TBD9giqRJX3LYaDBo9xEL1Wrqjt1BLyIHNXEseXu4bE6dDA21SN2FRIwjIEHSklog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، روز سه‌شنبه اعلام کرد تهران پیشنهاد عمان برای تقسیم برابر مسیرهای عبور و مرور در تنگه هرمز را نپذیرفته و در مقابل، طرحی موقت برای بازگشایی این آبراه به مسقط ارایه کرده است.
غریب‌آبادی در گفت‌وگو با تلویزیون حکومتی ایران گفت عمان پیشنهاد داده بود مسیر کشتیرانی به گونه‌ای طراحی شود که ۵۰ درصد آن در اختیار ایران و ۵۰ درصد دیگر در اختیار عمان باشد، اما جمهوری اسلامی این طرح را ناکافی دانسته است.
او گفت: «ما گفتیم این موضوع رفع‌کننده نگرانی‌های ایران نیست.»
به گفته معاون وزیر خارجه، تهران در مقابل، طرحی موقت پیشنهاد کرده که بر اساس آن تردد کشتی‌ها در یک مسیر از آب‌های سرزمینی ایران انجام شود و بخشی از مسیر رفت و برگشت نیز در آب‌های ایران قرار گیرد.
غریب‌آبادی همچنین تاکید کرد سیاست جمهوری اسلامی این است که تنگه هرمز «هیچ‌گاه به وضعیت پیش از جنگ بازنگردد» و هشدار داد هر ناو اروپایی که به گفته او به تنگه هرمز نزدیک شود، «هدف مشروع» جمهوری اسلامی خواهد بود.
او افزود عمان همچنین پیشنهاد کرده بود کشوری برای مین‌زدایی از بخش جنوبی تنگه هرمز اعزام شود، اما تهران با این درخواست نیز مخالفت کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77586" target="_blank">📅 22:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=t27JGfnLw2NkkxTQO2CrkgJDmLSld2wenNsazoya-PJZViCH-KoFe-rJVqyFoH5Xvu_Jvrv0-hrRC5WWN3UW4KMq--CU18lWeSeoQ1OtSC12z7j_p4e6RCE_CQkTUy_KAb-nVAKhwLLpc1NmzGYcEQa0HttxkTzo7HsIuJ6XvbQoJbRWonCxjAVJt9OLxsXaDl3jymSOLl_zEpnDtu4CMhWLCD78Y1IgQBBruh_1Wc_6iOb2LVLGTRk3l_-Xg1Yq0g0I673FBxZOWm_YFykhZT-XYbHXiEJGXQIeHpxLidZ95CRZchDKaUXuEArfbdMT8vEbB4n4T314CPtNHXW0tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0bb06747b7.mp4?token=t27JGfnLw2NkkxTQO2CrkgJDmLSld2wenNsazoya-PJZViCH-KoFe-rJVqyFoH5Xvu_Jvrv0-hrRC5WWN3UW4KMq--CU18lWeSeoQ1OtSC12z7j_p4e6RCE_CQkTUy_KAb-nVAKhwLLpc1NmzGYcEQa0HttxkTzo7HsIuJ6XvbQoJbRWonCxjAVJt9OLxsXaDl3jymSOLl_zEpnDtu4CMhWLCD78Y1IgQBBruh_1Wc_6iOb2LVLGTRk3l_-Xg1Yq0g0I673FBxZOWm_YFykhZT-XYbHXiEJGXQIeHpxLidZ95CRZchDKaUXuEArfbdMT8vEbB4n4T314CPtNHXW0tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی که در حساب اینستاگرام خود منتشر کرد، دیدار روز سه‌شنبه ششم مرداد خود با دونالد ترامپ را «عالی» توصیف کرد.
او افزود: «این گفتگویی بر پایه مشارکت کامل، حمایت متقابل و درک هدف مشترک جهت اطمینان از دست نیافتن ایران به سلاح هسته‌ای و همچنین سایر اهداف بود. این یکی از بهترین گفتگوهایی بود که با رئیس‌جمهور ایالات متحده، دوستمان دونالد ترامپ، داشتم.»
نخست‌وزیر اسرائیل در حدود ۹۰ دقیقه در کاخ سفید با ترامپ به رایزنی پرداخت؛ دیداری که پشت درهای بسته و بدون حضور خبرنگاران برگزار شد. نتانیاهو تاکید کرد که «تمام تیم ارشد» ترامپ و همچنین «تیم ارشد ما» در این جلسه حضور داشتند و این دیدار «فرصتی برای تبادل نظر و هماهنگی ترتیبات مهم برای امنیت و آینده دولت اسرائیل» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77585" target="_blank">📅 22:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r1DDO4ZO1MfXlhL17nmYnYGpNDifajX0aCuILdttl_ow5lU2Jart2uqPdg7c5dMzayx9vIhaL4Hvbn9S3dzG8DJLEIbnUs5IAui_RavLVEcfAU5FAp74Ity4Yc_4X1T9xCLnEpBIzmiIy3vU6sJVtS0ximbXdfeQGLrasvTodMQLTXvCg_pwFW_6F_zOujw_T47LMH7lFlYN-MbUUck6w5HAXVWnHta5x_Cln0hyF8iominIfoTsgcJXdJeRxn6KImJJpfWBmHh7bWnLzS7s6W_WwFDOMsAOddfVZpMwVFQr-qjP9ntiqizSVgOC1kQEIqL6QPyNUC_eCzmRbVcDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر خارجه اوکراین، ترجمه ماشین:
برای گفت‌وگویی صریح با وزیر امور خارجه ایران، @‌araghchi، تماس گرفتم. دیپلماسی یعنی گفت‌وگوی مستقیم، حتی زمانی که دشوار باشد. تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش‌هاست.
بار دیگر تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن شناورها یا افراد غیرنظامی را نداشته است.
این موضوع درباره اظهارات ایران در مورد تبعه این کشور که جان باخته و نیز یک شناور غیرنظامی که در حادثه‌ای اخیر هدف قرار گرفته است نیز صدق می‌کند. هدف ما مقابله با تجاوز روسیه است که ریشه اصلی همه این حوادث است؛ و این روسیه است که مسئولیت کامل همه تحریک‌ها و تلفات را بر عهده دارد.
بر ضرورت خودداری از هرگونه اقدام تنش‌زا و همچنین پایان دادن به هرگونه حمایت از جنگ روسیه علیه اوکراین تأکید کردم. این جنگ غیرقانونی است و باید پایان یابد.
موضع ما بدون تغییر باقی مانده است: اروپا و خاورمیانه شایسته ثبات، امنیت و صلح هستند.
andrii_sybiha
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77584" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77576">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dRtFSq5zO1cs3FRw66rfTQMlLBy8c3PU1Twyeu6s3wBZfeK4be0UjZKPtXQ9JmmAQ4s9xUKQPPMymawRppWJ9d3TkeifWQSPHxDoPJjrmlYl6Q_3fotoBxAW1ak9Z7UqUC9-MTr-7picg2P6Pwxz5i57wWuxaVNJRXow6kteYEXSW3nEft6e2ZMUWxwuPsdbBQy8dRCj3tmpnbV-AfB2qNzgjRCk05Ndi7skOQV_bGjoj60JvzGv3d3BJUeVNiSNLwsIchmRYcig22VgtzJuSChistm35tjVGWd1b4prCvWk2CXzqBokc2vo62aCi6CzcPJ0CILU0hwtrkXWZAbk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jc7rp6exqLeS8tgLVVjLim9OrZFTf8dg_gGxbVHyuDImv3LuZZc0WbyayBxyuJJE5-k28XmDA8G7Vga7_9TK5KV0rT8Ln1A558GGmY4aIbRx3xcKJWE8f9QPInv-GhkbTZUwZVdym2H3st0RKLXaSz9kqwWg70zOVlM9RzRK2XUcCpMhB5oPedhFvZrfvncweGcbsghsZOfb8DbXDy0qT1h3x8_zPKVgcgFzRBieb9RfoSTEjvkXvs9JD8jLnQF6WtTbzI93vLem6ljC6rCEpQWATa8JVwn_AnrqHe6LwQ_pl5Ba7evqfADGNVurxksV3ayxRh4y1ikMYdcHztRm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aATo4zaqBQtSamzsYy01eFA-EGC3fy-8SxmgGGqpM-zPwOE9I12HNmYq8Jgl-BHLylLLeXysWSdffybVxc8HX_FPailHaCRA1GmxnmLaNSoEoelqarYyE1EuEirdJ0yN_v0MNy3lwVpvI3wctctHzzA-tSnkTwhBsog_rQcCDpJjGnuKagP2mjYTjvY3bB8uY95-r8TMJwkU334XegdnJnnM_mQiZ2xQ2PKxu2UjB7H1p3-vTxTCo5-BeBjnA24LPlGNMarude5cJcPzPNdNk6_W7n219A4s98vP1eKahcGYLU75DfSzKeaY9JE1dKGBu6sqDgfNq2u0C5GJikhleg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VlSLtvs7HUk-qcWi-8s6b70Gta-o3D2Hl9lDSAMuRLdGcQowaWSS8wWznPo4hAgazApddIUglBZahBRPzhcSm2T-B_-qpl8X1MKLHs5NWTcBSbSYKJnKcbI-ZMwuwiQH0jqT69iKJW465vgVAMDIp6eNMeuyjtEi2N-mCQnfziaxovVR9hOc7gnf1y9HeE-htN-Y3csCEdcYltxWx776Z_J0z2oxm8RPot2a0K6nzSYI-pZ2gFcDEtrZcTVhUwI0guTBekaNGCRqMO0ze84DNISE1dQGR2dxbed_du_IJw-yJvc275yvYTx5z-nrKGzdr58E8JTg5RZJaokLoU3cpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VnzdxQrmkZfrNYvkLaR1vUHobE8dcrZ16TS0teO3sEVgXuViiCR1tWQZZyl7znW9YjwMHZ-4AJktw5gUYh-TcJcUCaHwFqzBQI-dmlpbRl2M814sjFUrQch-mNnJYHE6cmLH5YWaocJslt-QHPTW7xTPiEBS2i73bD08SL4lZblE5lcmOHY802v2QY9iDwAADKw6971cfmDz9IWvHOyXc0XI0sZo1no8OEWywhalCr9l3TkRoBLDeCDgGIjJUNTsMoH4g_ZThDFMgPP1gnUkcDYtbvK4v7uUSKwknUJjyiKdePMWy6GnK5Zs5sC2hZQWuiJ9vkIOS5yoypINyg-fmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U62PqR46Q4kptWtBp_Kjf06zyFQXY6PYmYP9KErGLn5PJC85rJo7clxwUpwvGdI62ITfgBrMdziiSvtEWNeaJlAx09-HOi-YOnuaQ3Y51IeiXZ3rLhQRQp-dbLX0atBsggKfXL3hCtf3ac4KwI8asQ0VS0koGYDlCGgxgUPSJ6oQIf6hzcDCg43ZPrJJwugfQ7L57daGwEfHxlprQJoMmRLORup5GhkD_xENQwU3kbb37fsNRhnbYdF-Vi3U_ct325UU-0xfZzRNBYjhvV9A2iSC7v0uM08cZh-fgjms_7hfx_g7WjC7fFG-h-Gv8r_Yp1Q8KDUNO32z9iMMtuKaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TiqZFcpeCVCWFMhLqd0jf4kRLfFOJozndDAATCZJHBWSgfaFRoqF8UC93EaTA4Sa4SjwTdFquis9WuLoyU0eMx7kBD_4sDfXDm4mVmefKUO62gArTT1pffGjowfsCnRwo0hyhFuIk2HTG8M2Hr1jhO08lnPfd9oKoS1l5nEmYHcHokS4NV81XeHbeT_ig7z1FPx5FEa-YoFBT-F-79_5bBrdLvIj5qyY0AgeFgXzKZL6i2NmvLhwoOOHXsjjzwvONFxTZwLJKls7q5NiWzn0fdcLVYDVR-POwMY-Qg4QjNkrF741c7HDPS21yBtllQL9RvKHglhuue3Dt8M5eddk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H30fph98RaPvsWeKGVSn9UHzypJTX9WgnCwfkSrrFhXaumVWUamIAu0NCShPHeBuZu7s7rd4QF78JZll34MdCkqGxNw3CkHE5PEOI5zV5LLL9lMb9rS0JIpL3bHp-piGiaqlkNJL0j0SWtJnr-Nf_DUDKnZ8-6aJ5uOZ8UmsKAq8JUWpEAcT3MAL_TczJdWYHhBQZILOrQ89C3O3ODhREgJfNp2fi0mG1BBYuNn7LdQ4JxopnJve0z7w20sUNTYp-_wELP4Qr48JjEc78WQewCCPvu-YWucz-wAwsQEYMF9Ih-HyafiDYRU1OkILfXfjSnNSoa_EiIL5q0nKHpQczA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل روز سه‌شنبه ششم مردادماه برای هفتمین بار با دونالد ترامپ در آمریکا دیدار کرد.
این دیدار در کاخ سفید و پشت درهای بسته انجام شد.
دقایقی پیش از نتانیاهو نیز، ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، مهمان ترامپ بود.کارولین لویت، سخنگوی کاخ سفید هر دو دیدار را «مثبت و سازنده» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77576" target="_blank">📅 20:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77571">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nf_vBvPvHckWl67VahuYS5lEiKbBmPvg4tCmkU1UyXQNIeWbpsTtmE8Fxt_lHfQHK9RxvPs_lxgFbp372_hxx4eM8BO-oIg1sFmbmueO1f--8jJedmg3A4f-tpahXHZLDR7nAEJ-fCURlbWjy3jY6_Zn1LczJGfDvVLx_eCkMB3Vjdjg9kjpLYzcEv0vRGnzABb2mIhY4Plk0DX5iRG1ZTuWKaVFKfTWuK-GYsirXa3izmtn3mRd_keCypOqOFLlfizs0Q9ToLfh4H0dN0x6TbIqps4oivET7q5e_EqWr0JS36x_VhklZzVq9f9c9gri8l3mzsQtcLJFMrMo80sW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/brgo0SJ5v5wjsqRFhjn-qWu-jIpoVdKGZlE2ghAJQiGV7xHqcxnc0sjM_2KdPSnKHamoMYxNis39R8cCfhfyYaFDJ0iyrzUlagy9Uphh04EsNGgi30OLSum2wUCDEjhCWEwBGAeM1fqDPgXuFLwffHAe8LX-vRSpYK_lU0cyJdDkasnQvtLWVp3rv8p9bwfkgBsoMmmHUEai_pyOCCSEFXhF8FDcOdNyYiePdLROPuxDrzjs4dolqHocQKynKOhLNUReqnYuUhAAm9jmZeC0fS4gcyvMtEn0p0eEGJFrRzKN2-7kKj_VbyvhJpc-gQug22pcLf3gVtKtzIoU7eFnIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qsEtEoclIu2-qidYtGnM9kzR98mKGXimm_87jZj2de77-mQVSqto8oHSRfw_sQiGSPv4XTgYz1k8ExQB9xTYWx3zRwi5iBlyjeCNWmhtFrVB3tAjfeXstwGo94O4bXr8KEhFeBbrbTsjgrm0LgXofCX4XoLqtQsIzzm5R5CQNYxaPKBH6WsDt8dUBo_MnVDd_6qf-NYZmwf6N8-HipezlNOzy0WHgqHlXuB0csPvFJFL5yfuiVsf58Hfpo_2FQniJcwMgcaYbNsQ8nVU-5HvHOGWhwr2mzhFEyAcZfHxjgk4U-s7mOimU5SvNQOFG3eFYTnT2XIlGEtbSaSYBuWMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VMlylA1H9GdnR7d1Qg9Du1LLv_Ja8pBS3FrHsi2SB2L5UPErAA_s5x3nL3sHAyElQNhWx1349bilrqLxArRuV1jUBdbysVzTs2Gyhc_gSKBNcvpR04vwSZRDsQF6331Hsa7uIkdC_XnfLz2Q4a230eLMOPVNSrSLDZC5xHYXwiFdKEXt1sLUVgrf_hN_wIK8dGjt6Km3Jp8Tv-Jb28BgYhROt8U31M_LDBPGMjDwpcMbFdIljJEwmI2C_D6O1irVfAMfsZr4XixSckecnpBfwLKpZLiqJzoMsT0biK4DG2x1-t0b7G9R0Fi9QeXTLfUbmulOsmAsDk-fqLOdcpkInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HVdruyw7bQ_QmAQBLE8-mOv4226z47ljnO5YDWLRoz_9VKx7tRIf1ohO9GEiIL2yfERDEaY6iPqncUYH9U-rIHLj3dAOetA0q-vmkbHFm8HxHF6MAnNXyPvqItRyfg0MEeMsXtREfCRVTAiFCGVzLg2NZFvU2FUay6TRcZMZ-SF7E0Hs6K2spMx5ufwYfYy3PrZwuxUkx2bxx6zTewAYDkI_eCrlssOh2_RxNLcQi6bsrEwGo2AQYxeu4b_5j98VL0q0BvZzQaUhMd1txC0c1uSV9tqftlWda5vgHPjWAps7lumZMt8spOFIpZiPl3TkgnPf2H3hUCkMIlhh6RJd7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی در ۲۵ تیر با شرح: ترمینال مسافربری فرودگاه بوشهر و باقی‌مانده‌های یک هواپیما
سخنگوی دولت، امروز: فرودگاه بوشهر دیگر قابل استفاده نیست و باید از نو ساخته شود. از یک هواپیما که تازه خریده بودیم فقط دم آن باقی مانده است.
Vahid
سخنگوی دولت جمهوری اسلامی می‌گوید فرودگاه بوشهر در حملات اخیر آمریکا کاملا تخریب شده و دیگر قابل استفاده نیست و «حتما باید از اول ساخته شود.»
فاطمه مهاجرانی روز سه‌شنبه، ۶ مرداد، در نشست خبری هفتگی‌اش با خبرنگاران گفت در بازدید از فرودگاه بوشهر «بقایای هواپیمای نوی به تازگی خریداری شده» را دیده که بر اثر اصابت مستقیم موشک، جز بخش کوچکی از دُم آن، تمام بدنه آن نابود شده بود.
این نخستین بار است که یک مقام حکومت ایران از تخریب کامل فرودگاه بوشهر بر اثر حملات به ایران خبر می‌دهد.
@
VahidHeadline
یک توییت به همراه اسکرین‌شات‌هایی درباره اطلاعات یک ایرباس ۳۱۹:
عمر این هواپیما 24 سال بوده! سال 2019 هم خریداری شده بوده.
iranimerican
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77571" target="_blank">📅 17:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77570">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sx9M4Rf7IqPDLzkTNDnNeMUMsKN_b8CanyzKaboaJTvkJ-yyQmbVJWSXmdpqoaXW1DrxERgLljH-tyt8gLLs9fEaAfUduHDQtbY70rp-FfUd12IIYCDDfg3K0pNoNFkmYIhSIbuHUMRLcociHYcHUTL3fcCIVcC3YEjmzJgS-vYeqchz3vmblTtRzIrBkPzVWSN990_vssgt0D5KdtOY28bIrGPAr_MHvVNkng3-AR7qCWX8XZQuoC04-m3G5eCBKYKxW_lDxT8XDsbsnAmSNRfVprDzmm79CivFYp1E3SbRLpYqkdp_db-nEOTnjIJaHZSnPeDi0EYN4Gthq4FXTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های نزدیک به حکومت و شماری از مقام‌های جمهوری اسلامی در روزهای اخیر بار دیگر بر اجرای قانون حجاب اجباری و برخورد با زنانی که از این قانون تبعیت نمی‌کنند، تأکید کرده‌اند. هم‌زمان روزنامه «همشهری» با انتشار گزارشی، از قوه قضاییه و نیروی انتظامی خواست با آنچه «هنجارشکنی» و «بدپوششی» خوانده، برخورد کنند.
روزنامه همشهری، وابسته به شهرداری تهران، در گزارشی با اشاره به انتشار ویدیوهایی از حضور زنان بدون حجاب اجباری در سواحل کیش، مراکز تفریحی، مراکز خرید و برخی رویدادهای فرهنگی، این موارد را نشانه «حیازدایی فرهنگی» توصیف کرد و مدعی شد که ممکن است بخشی از این رویدادها در قالب «پروژه‌ای سازمان‌یافته» برای تضعیف ارزش‌های اسلامی انجام شود.
این روزنامه با اشاره به ویدیوهای منتشرشده از ساحل سیمرغ کیش، برگزاری نمایش‌های مد، جشن‌های مختلط، کنسرت‌ها و تغییر الگوی پوشش در اماکن عمومی، خواستار ورود دادستانی و نیروی انتظامی و برخورد با افرادی شد که از نگاه این رسانه، قوانین مربوط به حجاب اجباری را نقض می‌کنند.
هم‌زمان، شماری از نمایندگان مجلس نیز بار دیگر خواستار اجرای قانون موسوم به «حمایت از خانواده از طریق ترویج فرهنگ عفاف و حجاب» شدند. محمدتقی نقدعلی، نماینده خمینی‌شهر، مدعی شد «برهنگی و بی‌حجابی مانند خوره به جان جامعه افتاده» و از مسئولان خواست اجرای این قانون را در اولویت قرار دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77570" target="_blank">📅 17:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f9UEyDqEEGe1NEQPK8TGQ0Zifxm3uSJUQ5sYDz6L2vdoGv1DfH8CR1HvI2Z-knjDcGipwAQUWgHlBhbofz2CUlKG7VmecfxYHxdxANbOHvC8NDO6C8Y3hsNw-eSIpHZG7u-w8rJFbYiR2sCqUxIyZsXftucoHQPAic_c8fA_tpnUDq8A5PT7FWXZWopcAgQui8xTZ6GI056douCIv9-HPGmysLBAvT4cHMabl10ObODM0TXp8rptU5VgLxStwZk_UQLJSUfcVxT9Boj43d5KoyYCIWuk1azo-OZqJUBwLhZfezsxRRcwoH_7sFh9kttwq-5rgPQ6Z-SGy7mZs2gMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=B4MRUugT1Ge9h5lbaHvJHcen1E8qdKm0Uw4YeLNSwoQuWJb5FIMgqQ1KdtTX82hNVJa5SH3smDb_lEvVtR4r5XFqGLU9qV_uc1NKxvL_UKtHdJIlYab2ov9oAYljjwwPjPACjwNRM07KYHJ47gtzHhYcxxuaUvL-jlwms5I-cxqw-8XH8KYCx0sWPifLlYHn1qW8DXDd-lCUkXBw4Ydazgm6X0vNxfmNIW0KSh3rZAfF85St8wJliwIUcA--TNhYRRSwty-0KbSLJ49ltkRwnw7JDV8ux2ss2w_lNguHR2dypGDHxZQIvh8hzChgjQ0M_J35SF4KT7TAOCkUDFRnBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f23cdb858b.mp4?token=B4MRUugT1Ge9h5lbaHvJHcen1E8qdKm0Uw4YeLNSwoQuWJb5FIMgqQ1KdtTX82hNVJa5SH3smDb_lEvVtR4r5XFqGLU9qV_uc1NKxvL_UKtHdJIlYab2ov9oAYljjwwPjPACjwNRM07KYHJ47gtzHhYcxxuaUvL-jlwms5I-cxqw-8XH8KYCx0sWPifLlYHn1qW8DXDd-lCUkXBw4Ydazgm6X0vNxfmNIW0KSh3rZAfF85St8wJliwIUcA--TNhYRRSwty-0KbSLJ49ltkRwnw7JDV8ux2ss2w_lNguHR2dypGDHxZQIvh8hzChgjQ0M_J35SF4KT7TAOCkUDFRnBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر ایران تن به توافق ندهد، کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق را می‌زنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، روز سه‌شنبه گفت که گفت‌وگوهای خوبی با ایران در جریان است، اما بار دیگر تهدید کرد که اگر تهران با آمریکا به توافق نرسد، تأسیسات زیرزمینی در کوه «کلنگ گزلا»، پل‌ها و نیروگاه‌های برق ایران را هدف قرار خواهد داد.
او در گفت‌وگو با شبکه فاکس نیوز اعلام کرد که در صورت امکان ترجیح می‌دهد پل‌ها و نیروگاه‌های برق ایران را هدف قرار ندهد.
ترامپ توضیح داد: «من می‌توانم همه نیروگاه‌های برق آنها را ظرف یک روز از کار بیندازم. تمام نیروگاه‌های برق آنها از بین خواهند رفت. فکر می‌کنم حدود ۹۱ میلیون نفر باید بدون برق و بدون پل زندگی کنند. و این یک توازن بسیار، بسیار ظریف است.»
او تصریح کرد: «آنها می‌دانند که اگر توافق نکنند، من این کار را انجام خواهم داد.»
دونالد ترامپ هشدار داد: «می‌توانم بگویم ظرف دو ساعت، بیشتر پل‌ها، پل‌های اصلی، همگی نابود خواهند شد و نیروگاه‌های برق هم ظرف یک روز.»
او افزود: «اگر بتوانم از انجام این کار اجتناب کنم، ترجیح می‌دهم از آن اجتناب کنم.»
رئیس‌جمهور آمریکا همچنین با اشاره به تفاهم‌نامه امضا شده بین واشینگتن و تهران در خرداد ماه که در درگیری‌های تیرماه به آستانه فروپاشی رسید، گفت: «ما دیگر نمی‌توانیم اجازه دهیم آنها توافق‌ها را نقض کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77568" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77566">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hcSntZLvVnwarTPAFtKZHFQMBqwobgWGP7UZfl3N9iJJAeQxkuO_hwyPyh99sx_fry1LG4HW-654PQLO6NNLbW0HkgKxw-TBQxrPudKwBTynlZFizSeugpAPK4rDsz2qVl94darIUfXNn4Zg-_cy1ekLlYsP2c4D8nhmInYbM1jVB-bzQw21AMxdv4IsRbOfhRM4-zRHW7-dGcU4j-lsMzJoXELx5Vxd6IlCB3AdOKCdjjpR2UBJKQcIn3uEuZ-EZVhARiaL-fBVt1fEvtiW41cv89JpMxDrDD1LuG6TF7YrE9egMToFB4-4BXtLgdvNtdl9QYcveoYrFfDToZTMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WpVnOKaNcTgTCX2X2JzHrw0496DnYzMc9PfxEraF1SZkeEnrFMATS_QF-CSo4qdaG6ihwhlakxYDeYYDR9RlSwXc9F6DTr-gb-dOdwqw2TtB82h7w_2P0wzZNHPwKshu0O9QKug5cXsXLWV9XrPrg1Vtak_lXLka9cvBKllQzw4Mi1y5Y4cLHj8xONqQiNtLyYLI5nYSocN2CZ3yVyzDTysbCNFOXd-lC3vowGkV5dqsQ9yvMivirS3ghWbEmzSCxqjlk8waOR7JVgdEZJXPeVSujDCP0N9e6m8M-KCGWqrYAt2zJuwhRVYLZuyZohG4n-uFzAVhaadCfZJvUwDswQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل کاتز، وزیر دفاع اسرائیل روز سه‌شنبه ششم مردادماه در مصاحبه‌ای با کانال ۱۴ تلویزیون این کشور گفت که در هفته‌های اخیر، جت‌های جنگنده و بمب‌افکن‌های نیروی هوایی ایالات متحده از پایگاه‌های هوایی اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
کاتز گفت: «ایرانی‌ها می‌دانند» که این جت‌ها از اسرائیل برای حمله به ایران به پرواز درآمده‌اند.
به گزارش اورشلیم‌ پست، کاتز در این مصاحبه گفت: «امپراتوری مغروری که اسرائیل را به نابودی تهدید می‌کرد، فروپاشیده است.»
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در کنفرانس امنیتی کانال ۱۴ با اشاره به دیدار دونالد ترامپ، رییس‌جمهوری آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در واشینگتن گفت آمریکا در موضوع ایران منافعی دارد که فراتر از منافع اسرائیل است و افزود: «بسیار مایلیم به ایران حمله کنیم، اما آمریکا موافق نیست.»
کاتز با اشاره به آنچه دستاوردهای اسرائیل در برابر جمهوری اسلامی خواند، گفت: «امپراتوری متکبری که اسرائیل را به نابودی تهدید می‌کرد، در هم شکسته است.» او تهدید کرد: «اگر به سوی اسرائیل شلیک شود، با تمام قدرت حمله خواهیم کرد. ما آماده‌ایم با توان خودمان به ایران ضربه بزنیم.»
وزیر دفاع اسرائیل در پاسخ به پرسشی درباره واکنش احتمالی اسرائیل به پهپادی که روز سه‌شنبه از عراق پرتاب و در مرز اردن رهگیری شد، گفت: «ما می‌دانیم چگونه امور را مدیریت کنیم؛ آماده‌ایم.»
کاتز همچنین گفت که دونالد ترامپ، رییس‌جمهوری آمریکا، «درک می‌کند که اسرائیل از مناطق حائل در لبنان، غزه و سوریه عقب‌نشینی نخواهد کرد». او افزود: «هفته گذشته از غزه بازدید کردم؛ هنوز تونل‌های بسیار بزرگی در آنجا وجود دارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77566" target="_blank">📅 17:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77565">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ZqWh3ciJZNb0-QbXA9CAISnas0x9NvvaGFgivkn6luv_Oj0bNg7pLWxwsUe9Yp8Ns8Sw0n9ZEXbM-IvCWFMiHvSOBXqTyybPUEdCxytLCo7wqj5QPFAAvrhUDYLz4camW446l2Q_mrZnkc5VCC_WbXkvT5BaLrjigTqSra8XX-LMwdHAKrRUmMSnScRbfcgExzgtmfzUYL21q6H6EHcDXhcc-hHYiuNvYxtMRJWSVlJ1oipDBiwIq4rz5si1q5ANjafpG6EV3gj9OcPDiwIuRYZrD3qhIgxQMBvnjvTaUIoqqgdM_5k2MwAK-iLtZsnzfoI2lCNGl2P0vMZD4hGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه می‌گوید که حمله اوکراین به کشتی ایرانی در دریای خزر «باید به‌عنوان حمله به خود ایران» تلقی شود.
دیمیتری پسکوف، سخنگوی کرملین، هشدار داد که این حمله نشان می‌دهد که از بین بردن «تهدید ناشی از کی‌یف» تا چه اندازه اهمیت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77565" target="_blank">📅 17:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77564">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5v4md_YmB9v43LTLzyoF-i9oj5coSCqS4_CPS5s7JP59XLbclMCEvn0P5OOmKEuawWB52MmxPbiSpEad7Zv67WnHOr1UVME-F2-Ew4hYDgaTCCbDXs-2GDHbexwgXKJVQtfPkvPKgkDQyCT1pEMJkjbMfecT020yqAZfGE4fsGxsn3VKTZsBcBYSoAxaNXCwQo68f_Gwr1L2i-xvaE63JGmaGrxZeBn8zrRY_fTPM2eOgK-_CWja8QB3-W676ibmFAWMMncl_mszOTg-XrLOXSJNFyQV0XEOqhEWI1crL21nrxd9tgrp6phDJi8yAl9m_TiottltDZQD8uQtTFGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس برنامه‌های اعلام شده از سوی کاخ سفید، دونالد ترامپ، رئیس جمهوری ایالات متحده، روز سه‌شنبه ششم مردادماه، با رئیس‌جمهوری اوکراین و سپس با نخست‌وزیر اسرائیل دیدار خواهد کرد.
دیدار ترامپ با ولودیمیر زلنسکی ساعت ۹:۳۰ و دیدار با بنیامین نتانیاهو ساعت ۱۱ صبح به وقت محلی برگزار می‌شود. برنامه روزانه کاخ سفید نشان می‌دهد که این دیدارها بدون حضور خبرنگاران برگزار خواهد شد.
با این حال انتظار می‌رود که پرزیدنت ترامپ، در لحظه آخر اجازه حضور خبرنگاران را صادر کند.
برنامه بعدی ترامپ پس از دیدار با نتانیاهو، حضور در مراسم یادبود لیندسی گراهام، سناتور جمهوری‌خواه فقید است و نخست‌ وزیر اسرائیل نیز در این مراسم حضور خواهد یافت.
پیشتر نتانیاهو اعلام کرده بود که موضوع ایران در صدر گفت‌وگوهایش با پرزیدنت ترامپ قرار دارد.
دیدار ترامپ و زلنسکی نیز پس از آن برگزار می‌شود که شامگاه شنبه سوم مردادماه، نیروهای اوکراین شناورهایی حامل محموله‌های نظامی جمهوری اسلامی به روسیه را در دریای خزر هدف قرار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77564" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77563">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/afAXDHnx5rS1WZ6J1UXT33D0Zc5FfinZ1Dgn2XWP3rPMvPn-Vxx4T19xAtmCmC8HEo9rl6V7kf46_8tx8UR3GQBO-raG3sS1V0o_SDfblzK_z02TUXccJfze1PRR7wCU7gC819peuzOfafQqCzVub8lOK1Zk0cpJDRi7PRYq48RguVVhEGS5q2YVFvO5cHmnh3JQ3KZAtS1nt2ThQ2s2o9g_kV8azCCRFvDrHaOCKcKWcfGNfCS4PKjAqmd5MNNxIGpkzp7VZtdxBvTZyLK3Q0LoJsWAfaO9Wncs3VGpbtItiWiF-9pXtzj0nEsw6NkqkvyFBINYTcuDPRVx96PrdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاسین سرفراز، بوکسور ۱۷ ساله اهل بجنورد و عضو تیم ملی بوکس ایران، که در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت شده بود، به سه سال و سه ماه حبس محکوم شده است.
کمیته آزادی زندانیان سیاسی خبر داد، پرونده این ورزشکار نوجوان در شعبه چهارم دادگاه کیفری استان خراسان شمالی رسیدگی شده و او تنها در یک جلسه دادگاه، بدون دسترسی و حق انتخاب وکیل، به اتهام «اجتماع و تبانی علیه امنیت ملی» به سه سال و سه ماه زندان محکوم شده است. این حکم حدود پنج روز پیش به او ابلاغ شده است.
یاسین سرفراز از ورزشکاران شناخته‌شده بوکس ایران به شمار می‌رود و پیش از بازداشت، در رقابت‌های کشوری، آسیایی و بین‌المللی موفق به کسب عناوین قهرمانی شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77563" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77562">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sTdWZmKuupQXGmySDgxlC3D3FaLlbvozJ-WV5U83eR42F_vZUMALwiqaReHEeUwdjrAI82h3x9Bin5pIsUSBbRiJHBziaLW3wm-6nGVx-pVztMmSkrbiOlEAiPm4gCk5JG4SybYHmuZpkoe1S9SDhikz9Abj0CufVYBymrTt3bAmjELvFlnzVimQZuMjWlCov_Eone5EyB-t9StEJH2sojVRh8nd6gDZjrAYrESqnnxArogP3EhFl8rMDq2kQZYvC2n8l5h2sl9L-_qTxiLNS59pR3irRb63ul2m3qvrt2WfQbgp8j37wYaa9_mvmTOqqKZBvD9yWwXcCBZFvlB_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز سه‌شنبه ششم مرداد به نقل از یک منبع آگاه در خلیج فارس گزارش داد که عمان پیشنهادی برای ایجاد یک سازوکار مشترک منطقه‌ای با پرداخت داوطلبانه عوارض یا هزینه‌ عبور و مرور برای مدیریت تنگه هرمز به ایران ارائه کرده است.
به گفته این منبع که نامش اعلام نشده، پیشنهاد عمان مورد حمایت کشورهای منطقه است و بر اساس آن ایران کنترل انحصاری این آبراه حیاتی را در دست نخواهد داشت.
این پیشنهاد الگو گرفته از نحوه مدیریت تنگه مالاکا بین دو کشور مالزی و اندونزی است و بر اساس آن، عبور از این آبراه با پرداخت داوطلبانه هزینه در تأمین مالی ناوبری، حفاظت از محیط زیست و جستجو و نجات همراه است.
عمان پیشتر به طور رسمی اعلام کرده است که با مدیریت متفاوت تنگه هرمز به شکلی که ایران می‌خواهد موافق نیست و پیروی قوانین بین‌المللی خواهد بود.
پیشتر مقام‌های ایران تأیید کرده بودند که مذاکراتی را با مقام‌های عمان در زمینه مدیریت بر تنگه هرمز انجام داده‌اند. سخنگوی وزارت خارجه ایران هم روز دوشنبه تأکید کرده بود که در حال حاضر تنها مذاکره‌ای که ایران در آن دخیل است مذاکره با عمان درباره تنگه هرمز است.
دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که این کشور «مذاکرات خوبی» با ایران داشته و احتمال توافق وجود دارد، اما او هشدار داد که اگر مذاکرات به نتیجه نرسد، حملات ایالات متحده از سر گرفته خواهد شد.
در همین حال، عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه با همتایان عمانی و سعودی خود در مورد تنگه هرمز گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77562" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77560">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BpWnfm52R7S2FwT5ai8I9IxKJb9iLOIF_rYm9bW_M3D42o_NJ_vbgORtA8DB5nbe_auMvbtmesoh7aEkLPqjz6tIZRCuBDI9f3N9Ne71xAJW5H4EljoceGrEhtN52BVVtkOgex_DY0Tw_2LJ4mZ7P5Rp4HU91sURPQxSbhYnUEJ677mUNS2YEy3tPRJxPz-gIEH8Rlse3r71bpOcM8hjpKcFhadjSzGuc3d30R2DxDyAjp_41bCAWj9HuHV3_5SDrT9c9UncxXeHhPijmqynNvnlv5ZictWl6DIkXKkzKaBDhqFrNRXIy5gOFax95kGm2V7IX8npsklAA5YcEOfIvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rgXhlD7Wk0IwxmeElwrBze7XTf8YNQhQBXjzqwkvz1IVPNUVVJqJ-egWM-SP_XSn2kYpCUk3DJiu1ZVM6aMGYKNfM0nESPmmEK5y_aYgtBU59nD6vxYZ1Siah2aX7jZ6EnqXtuEzinYS4TSevFiNVF3I__7FX_FclacYkCUQ0smKBWs1wpT72zODbuY7mK_8S5NcHp9hz0TTE3EyuyjXGC2ij7gdYaQrHWOz4mImJhOV883-mWduG9IJ9qaB9VMnLgPNJW1USeDkxAl8_ojlPicAgM0hQHhXnMracACdtcgzTbQqjn63vgDNijJ-GIWxwG_AyZSB0w3ioxV20Y1rAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قائم حسینی، امیرحسین ملکی و علی دشتی، متهمان پرونده میدان علیخانی اصفهان، در آستانه اجرای حکم اعدام قرار دارند.
از خانواده‌های این معترضان دی خواسته شده برای آخرین ملاقات به زندان مراجعه کنند.
قائم حسینی پسرعمه گل‌محمد محمدی است که ۲۸ تیر اعدام شد.
این پرونده ۱۲ متهم دارد که علاوه بر محمدی، تاکنون سه تن دیگر از آنان به نام‌های عرفان اسفندیاری، ابوالفضل سپاهی و امیرحسین صفری نیز اعدام شده‌اند.
@
VahidOOnLine
شروین باقری، از معترضان پرونده اصفهان، در آستانه اجرای حکم اعدام قرار دارد.
به خانواده‌ او گفته شده برای آخرین ملاقات به زندان مراجعه کنند. شروین باقری نیز در حال انتقال به سلول انفرادی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77560" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77559">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K6r3Amiu-L53AxA1qdz8eVxcu0WmtkPx39zm1VU7wKDR6AVJnjI5VeHJF4XkTWGd5I5UJXA1EeTFJcAVqfhpj9zFMFcDS5YlxK3yA5XspODyLLFrbo21ErLkkqPFaXAh5v04fDNiMVy_Px1cK9m_sJlaIGRlMWPQT9Ek38cKXXLY8uTvBOL06RdAtA5fzkpJnTqFC4TbBOYmbf5fCxKTznTs-o9b3I73JJ8uxZYrft1UidL3MMIZeyXggXKV96I9EF_bOYNQCHOmvpEuesTCcFeRw-NnO-fKQDfbtd57YTt_0vlXGYQ_D0Hb5vCAYkgNtZNux4YoFXDT8ptLrrHZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع حکومتی بدون نام بردن از کسی نوشتند سه نفر از پرونده ملک شهر اصفهان اعدام شدند.
آپدیت:
بعدا ویرایش کردند نوشتند: دو نفر
آپدیت:
قوه قضاییه جمهوری اسلامی اعلام کرد بامداد سه‌شنبه حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو معترض بازداشت شده در اعتراضات دی‌ماه در اصفهان، اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 494K · <a href="https://t.me/VahidOnline/77559" target="_blank">📅 05:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/75dcad3a9d.mp4?token=tB0uJlEXnzxAc-bjyKceqVKnlUKoSoVlvT9yUxfkKX-jkBwAyraqUBHW9hkMIlplABEXnn-ZpO9z60S9FRFQ-2I8AI0vJ9JfbYDYSAM_aXg9HaNBqvinyJX60ZNJ4Yby4aY-vIWm2Mhxg0CuwREVOtfqAie8vzW06WSpw4F9Dv2z7SIi-MMf1Hy5E7F9yNblgZ4u9a7tZBqtVHverh3S_8tY_hcYMuVk5kPW3Dj8Ixol3qC58D2br0FcTRWqVQM5gejRy530Fhujif0u7wD7FpjcIoXOUSCx-krQXYgIEGpNZF6LioGo9kXmf9kzos6VSAFUH7CBeSN3ptjt2nDo5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/75dcad3a9d.mp4?token=tB0uJlEXnzxAc-bjyKceqVKnlUKoSoVlvT9yUxfkKX-jkBwAyraqUBHW9hkMIlplABEXnn-ZpO9z60S9FRFQ-2I8AI0vJ9JfbYDYSAM_aXg9HaNBqvinyJX60ZNJ4Yby4aY-vIWm2Mhxg0CuwREVOtfqAie8vzW06WSpw4F9Dv2z7SIi-MMf1Hy5E7F9yNblgZ4u9a7tZBqtVHverh3S_8tY_hcYMuVk5kPW3Dj8Ixol3qC58D2br0FcTRWqVQM5gejRy530Fhujif0u7wD7FpjcIoXOUSCx-krQXYgIEGpNZF6LioGo9kXmf9kzos6VSAFUH7CBeSN3ptjt2nDo5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخبار منتشر شده در شبکه‌های اجتماعی حاکی از آن است که خانواده‌های زندانیان سیاسی محکوم به اعدام و شهروندان در میدان علیخانی اصفهان تجمع کرده‌اند و گزارش‌هایی نیز از درگیری یگان ویژه جمهوری اسلامی با معترضان منتشر شده است
این گزارش‌ها می‌گویند نیروهای یگان ویژه جمهوری اسلامی با موتور، خودروهای زرهی و سلاح‌های سنگین در محدوده محل اجرای اعدام مستقر شده‌اند و اینترنت در اصفهان دچار اختلال شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 490K · <a href="https://t.me/VahidOnline/77552" target="_blank">📅 05:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/saBRfLixhksT9bzHPrpIvXW3WSDgZl2K3vkVfyFRa5YlKM3OY7D_ud96zBGUUHY06EpKFMmcsp3f7EEuy6p3nz3PMbVIPyUl0Z5ThP7jpkFBJpqsklP9CwWyk7D6xTD8RuZTJNgvG_nwI4XkpEkBIby0x5yRSF6uelB2i1-BrJh6ZrcHHDfTvPenmyjTf7tiVu1h-dBHlU3pWqia4iltmDcoAzWaxOHprSQ0R4U7p7tFhDw_TvMyIfo0aqTg1dBF5ZblIsUpidw-hPLPlyTdXlTs0GKlxx-89Bf87AgXgHA3l0iUX8FNxqyOGX9lbmyj3-IInV1ExR54_fLwV--Sxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LY_E1REbHZeKukSNG4dVjFDvYVWwVdaWVK3YUJx-nTyvAe6p8QIs_z6gwTC8_wX7HfuDBnr9RKjg2eyZLR8vXO64hu8doDdkU_SVpGW_zW4hn3UT_Dd-fLKsJNKtfVYi5oKtPvwlfyQLVav9v7PszzlfH0-MmYNte8LWt8cU5WQjXlglpC8CW6z79AuSG_9gPsG8gI3d9BgZtJcHENOuptyI-iMKcfoT8LsyH_try500PfXDifR7cStloqBAbZNf1Va1_Zx2Zrt1vW59enCnjEVAWdXnbO1UY522SfktbGhST6-HgfuKDllN34so52BEoqxgnBKTdNbPQsQ-3Hwv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BqzD6ThME0-mETiX2bbIbG97Tp7_L9p4uh2AJGGCKnyN3YO0b4Eqqh5VyOEflZ6WJEnAHTkeg77jRIK-3_u6ZYAUmeSdNJDPWFt8ARWekzCQurgvD2F9f6rOqLpO62ibasWbh4JAZrRhLAj2vn1URzX5RaSCqKmtcHEt_zHUJgKItf_oqF6MQyZGHIzhUsPewIQPud2Q6Dd0caGcAYCFSEORmDSnsiDGKr84r1At91ugNVNOWKhuZ0PQVIwekPYKXJIuJrFPaBiJ_HiH-OXgHfSgCkQIMslggMaJJ5ODh9NGILVyjsFqC8kOeylleUT0oFjBawJLglUfh9sz_58j6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Cl07NFx2DGT9hU2ASFMcXZanf12FCzcQSPsJe6ojiVC6K5dF8xkZPVGWAZFzB3_uOEMIdcsoMg2R3Psll8reGgSflryc19jUMMfEeTxnuDoo3hv5xNRvL44pdaWI7CR4fwtE5drLgky-Obls4Xz7Mh2M_VZGkX2sIYF5C2RSXfcc7a6PbJCBQANPhVdMM2wNYuJmVdjRHBQ0H1u_GSRwVFgSkT-K6lHuWxoArU2_CJkkqraOfIXNI0lapNqzLkp1oPmXSmaaKoCwZQQH049IoDDf_lEdEbSFZlaycxafV4T0a34vXB5OFiHvkPzeDRvo1bSXXeVeQwYi0HE3TnOIYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faf260cfea.mp4?token=j5WNA5WenJ6wqBXuC_8cr6630BY1GmuJYOXqgFlQHctXbWdILwVq9cLzglembOlfkMo8T1pt-PxPNiKl7-uR5kMAyHWSpFApIsPxKEgW6htgbqFp4N9o0DpB0d4eFGCxVH2W4r4c5aTMWn-k_3-C547GtmzO901oyNcpBECQTe7B2IQYIbLHA7mhTTMHlxG74zpMgPAq6mf2PSL_DmN2qAIsE4gcGnK2mYu6Bq9ESxvnkt15a0TdR-0R0uSPIUIBWMz-2HIaFo--3rvw958ByshPIiA2LEoRm_XM2LMDwtfM3Y5Ez46qD13rLBR85uKUlpvr-y3YtZb8DGkYpu6kKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faf260cfea.mp4?token=j5WNA5WenJ6wqBXuC_8cr6630BY1GmuJYOXqgFlQHctXbWdILwVq9cLzglembOlfkMo8T1pt-PxPNiKl7-uR5kMAyHWSpFApIsPxKEgW6htgbqFp4N9o0DpB0d4eFGCxVH2W4r4c5aTMWn-k_3-C547GtmzO901oyNcpBECQTe7B2IQYIbLHA7mhTTMHlxG74zpMgPAq6mf2PSL_DmN2qAIsE4gcGnK2mYu6Bq9ESxvnkt15a0TdR-0R0uSPIUIBWMz-2HIaFo--3rvw958ByshPIiA2LEoRm_XM2LMDwtfM3Y5Ez46qD13rLBR85uKUlpvr-y3YtZb8DGkYpu6kKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطر اجرای قریب‌الوقوع حکم اعدام دست‌کم دو نفر از محکومان پرونده اعتراضات دی‌ماه ۱۴۰۴ اصفهان افزایش یافته است.   «علیرضا سپاهی» و «ابوالفضل سپاهی»، دو پسرعمو که در این پرونده به اعدام محکوم شده‌اند، برای «آخرین ملاقات با خانواده» آماده شده‌اند و احتمال اجرای…</div>
<div class="tg-footer">👁️ 495K · <a href="https://t.me/VahidOnline/77545" target="_blank">📅 02:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=BGZrL-qWF01xa8omm8IsOruuUGZZbnmNlo9nMDfy0htl65cHCEPavurQV4CLcqfpspepniX31aRFaUQOU90-eCTOz-3aiYRbs92FhG-eOc7Wvn8WhTkkSksxzcOe5cKd7ov0VDaWjNYTsDsNwC1WA2aF9WZiUHkuxQV_BewSxudxHv6BhXs_hFoMo2uyh-Esd3-q-GF3SITy2ox-_dft0p8xx8fRqjvWpuW0gx3zvuDKY3SWuQhB-q6TU0t8VoukEcswIvPTWwaKBJuvK0IAmgVdQ0o-YPonMNIljr1_VeVta8lxMmhHzdml4W0PiAjSB6ChCXzo_3esuGDNehqyPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=BGZrL-qWF01xa8omm8IsOruuUGZZbnmNlo9nMDfy0htl65cHCEPavurQV4CLcqfpspepniX31aRFaUQOU90-eCTOz-3aiYRbs92FhG-eOc7Wvn8WhTkkSksxzcOe5cKd7ov0VDaWjNYTsDsNwC1WA2aF9WZiUHkuxQV_BewSxudxHv6BhXs_hFoMo2uyh-Esd3-q-GF3SITy2ox-_dft0p8xx8fRqjvWpuW0gx3zvuDKY3SWuQhB-q6TU0t8VoukEcswIvPTWwaKBJuvK0IAmgVdQ0o-YPonMNIljr1_VeVta8lxMmhHzdml4W0PiAjSB6ChCXzo_3esuGDNehqyPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از سخنرانی ترامپ در میشیگان:
- آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
- همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
ترجمه ماشین:
ترامپ: ... ونزوئلا.. پس از آنکه تقریباً ظرف ۴۸ دقیقه پیروز شدیم، گفتند: «اوه، حرکت خوبی بود.» خب، همین اتفاق اکنون در ایران در حال رخ‌دادن است.
مردم هنوز متوجه نمی‌شوند. ما نیروی دریایی‌شان را نابود کرده‌ایم. نیروی هوایی‌شان را نابود کرده‌ایم. رهبری‌شان را نابود کرده‌ایم. تسلیحات ضدهوایی‌شان را نابود کرده‌ایم.
پهپادهایشان اکنون با حدود هفت درصد ظرفیت قبلی تولید می‌شوند. بخش عمدهٔ توانایی تولید پهپاد و توانایی تولید موشکشان را نابود کرده‌ایم.
اکنون با ما دربارهٔ دستیابی به یک توافق صحبت می‌کنند؛ اما اگر ما این کار را انجام نداده بودیم، هیچ مذاکره‌ای در کار نبود.
آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
آن‌ها قلدر خاورمیانه و قلدر ما بودند. اوباما ۱٫۷ میلیارد دلار پول نقد سبز به آن‌ها داد. یادتان هست؟ پول‌ها را داخل یک بوئینگ ۷۵۷ گذاشتند و به تهران فرستادند؛ ۱٫۷ میلیارد دلار پول نقد.
او تصور می‌کرد می‌تواند به آن‌ها رشوه بدهد؛ اما آن‌ها در عوض با خودشان گفتند: «این کشور چقدر احمق است.»
نه، نمی‌توانید به آن‌ها رشوه بدهید. باید شکستشان بدهید و ما داریم حسابی شکستشان می‌دهیم. اما خواهیم دید نتیجه چه می‌شود.
اکنون مذاکراتی بسیار دوستانه در جریان است.
نیروی دریایی ما در اجرای محاصره چقدر خوب عمل کرده است؟ حتی یک قایق [نتوانسته عبور کند]. آن‌ها می‌گویند: «دیگر محاصره را نمی‌خواهیم. لطفاً، لطفاً، محاصره نکنید.»
---
ترامپ:
اکنون قیمت تخم‌مرغ بسیار پایین‌تر از زمانی است که کار را آغاز کردیم. خواهید دید پس از آنکه تهدید هسته‌ای ایران را از میان برداریم ــ که بسیار زود اتفاق خواهد افتاد ــ اوضاع چگونه خواهد شد.
اما افزایش قیمت‌ها ربطی به من نداشت.
---
یکی از سخنرانان همراه ترامپ:
۴۷ سال طول کشید تا کسی بایستد و بگوید دیوانه‌ها نباید سلاح هسته‌ای داشته باشند.
همچنین چندین دهه طول کشید تا مشاغل را دوباره به داخل کشور بازگردانیم.
---
ترامپ:
نمی‌توانستیم اجازه دهیم آنچه در ونزوئلا اتفاق می‌افتاد ادامه پیدا کند و اقدامی که انجام شد بسیار قاطع بود.
همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
اما هزینهٔ عملیات ونزوئلا، همان‌طور که گفتند، تاکنون جبران شده است. به همین ترتیب، در برابر جمهوری اسلامی ایران نیز با اختلاف زیادی در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز به سلاح هسته‌ای دست پیدا نکنند.
وقتی کسی می‌پرسد: «چرا این کار را انجام می‌دهیم؟» پاسخ این است که نمی‌توانیم اجازه دهیم شما سلاح هسته‌ای داشته باشید. همین تنها چیزی است که لازم است بگوییم.
اگر قدرت سلاح‌های هسته‌ای را درک می‌کردید، دقیقاً متوجه می‌شدید که چه می‌گویم.
---
بار دیگر می‌گویم: ایران هرگز سلاح هسته‌ای نخواهد داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/77544" target="_blank">📅 00:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ویدیوی مصاحبه ترامپ با زیرنویس فارسی در پایین همین پست
متن بخش‌هایی از مکالمه، ترجمه ماشین
:
🔺
خبرنگار:
درباره جنگ ایران؛ آیا از پیت هگست، وزیر دفاع، به‌دلیل توصیه‌هایی که در اوایل جنگ به شما داد و نتیجه‌ای که جنگ پیدا کرده، ناامید یا عصبانی شده‌اید؟
🔻
ترامپ:
نه، به‌نظر من او کار فوق‌العاده‌ای انجام داده است.
ما ارتش آن‌ها را تقریباً نابود کرده‌ایم.
آن‌ها می‌خواهند دیدار کنند و ما هم داریم با آن‌ها دیدار می‌کنیم. خواهیم دید چه اتفاقی می‌افتد. این احتمال وجود دارد که بتوانیم به توافق برسیم.
بدون کاری که ما انجام دادیم، حتی حاضر نبودند با ما صحبت کنند. آن‌ها هم از طریق واسطه‌هایشان و هم مستقیماً درخواست دیدار کردند و ما داریم با آن‌ها مذاکره می‌کنیم. می‌دانید، ممکن است اتفاق‌های خوبی بیفتد.
فکر می‌کنم قیمت نفت امروز به‌شدت پایین آمد. تا حدود یک ساعت پیش هم بازار سهام سر به فلک کشیده بود. اما نه، آن‌ها درخواست دیدار کردند. اگر عملکرد ما ضعیف بود، درخواست دیدار نمی‌کردند.
تنها دلیل اینکه می‌خواهند ملاقات کنند این است که ما ضربات بسیار سنگینی به آن‌ها زده‌ایم.
🔺
خبرنگار:
چقدر دیگر در برابر ایران صبر خواهید کرد؟
🔻
ترامپ:
وقت زیادی دارم؛ وقت بسیار زیادی.
تمام نوار ساحلی‌شان نابود شده است. تنگه در وضعیت بسیار خوبی قرار دارد و همین حالا هم در حال مذاکره هستیم.
می‌دانید، آن‌ها می‌خواستند صحبت کنند. افرادشان گفتند: «لطفاً بمب نریزید. دیشب و شب قبل شلیک نکنید؛ دو شب این کار را نکنید.»
می‌دانید، گفت‌وگوهای خوبی داریم. بنابراین خواهیم دید چه اتفاقی می‌افتد.
فکر می‌کنم احتمال خوبی وجود دارد که اتفاقی بیفتد. اگر چنین شود، خوب است. اگر نشود، دوباره به همان کاری برمی‌گردیم که دو روز پیش انجام می‌دادیم.
🔺
خبرنگار:
آقای رئیس‌جمهور، ارتباطات با حوثی‌ها درباره دریای سرخ چگونه بوده است؟ آیا نگران...
🔻
ترامپ:
حوثی‌ها؟ این مشکلی بود که مدتی پیش با آن روبه‌رو بودیم و همان‌طور که می‌دانید، حسابی آن‌ها را درهم کوبیدیم. بعد از آن دیگر هیچ مشکلی با حوثی‌ها نداشتیم. اما در حال حاضر در آن موضوع دخالتی نداریم.
البته ممکن است دخالت کنیم. می‌دانید، اگر مشکل‌ساز شوند، احتمالاً مجبور خواهیم شد وارد عمل شویم.
🔺
خبرنگار:
درباره عربستان سعودی؛ آیا نشانه‌ای از عربستان دریافت کرده‌اید که به پیمان‌های ابراهیم بپیوندد؟
🔻
ترامپ:
هنوز درباره آن صحبت نکرده‌ایم.
🔺
خبرنگار:
در صورت گسترش درگیری، آیا نگران کاهش ذخایر مهمات هستید؟
🔻
ترامپ:
ذخایر زیادی داریم. انواع مختلفی از مهمات در اختیار داریم. می‌دانید، بایدن مقدار زیادی از آن‌ها را به اوکراین داد و ما اکنون در حال بازسازی آن ذخایر هستیم؛ اما همچنان مقدار زیادی داریم.
از تسلیحات رده‌میانی هم مقدار زیادی داریم؛ بیشتر از آنچه در هر شرایطی بتوانیم مصرف کنیم. مقدار زیادی داریم. صادقانه بگویم، دوست دارم مقدار بیشتری داشته باشیم، اما بایدن حجم بسیار زیادی را به اوکراین داد.
وقتی من رفتم، انبارها پر بودند.
وقتی پس از اوباما به ریاست‌جمهوری رسیدم، او مهمات نخریده بود و ذخایر بسیار کمی داشتیم. من آن ذخایر را بازسازی کردم. اما به‌محض اینکه رفتم، آن‌ها مقدار زیادی از آن را به اوکراین دادند؛ ارقامی که هیچ‌کس پیش از آن ندیده بود.
بنابراین اکنون با سرعت بسیار زیادی در حال تولید هستیم. کارخانه‌ها در حال ساخته‌شدن‌اند و تجهیزات بسیار زیادی تولید می‌شود. به‌خصوص تولید سامانه‌های پاتریوت در حال افزایش است.
ذخایر زیادی داریم. هرکدام از پیمانکاران ما همین حالا در حال ساخت چهار یا پنج کارخانه هستند. وضعیت بسیار خوبی داریم، اما قطعاً دوست داریم از برخی تجهیزات پیشرفته‌تر مقدار بیشتری داشته باشیم. بایدن مقدار زیادی از آن‌ها را بخشید.
...
🔺
خبرنگار دیگری:
شما و نخست‌وزیر نتانیاهو درباره ایران هم‌نظر هستید؟
🔻
ترامپ:
تقریباً. بله، تقریباً. اختلاف کوچکی داریم، اما در مجموع تقریباً هم‌نظر هستیم.
می‌دانید، ایران طی ۱۴ روز گذشته ضربات بسیار سنگینی خورد و آن‌ها خیلی مؤدبانه از ما خواستند: «لطفاً متوقف شوید. بیایید مذاکره کنیم.»
اکنون در همین نقطه قرار داریم. خواهیم دید چه اتفاقی می‌افتد. اگر به توافق نرسیم، دوباره همان کار را از سر می‌گیریم.
🔺
خبرنگار:
رئیس‌جمهور زلنسکی می‌گوید روسیه تصاویر ماهواره‌ای پایگاه‌های آمریکا در خلیج فارس را در اختیار ایران قرار می‌دهد تا به آن‌ها در هدف‌گیری کمک کند. درباره این موضوع چه کاری می‌توانید انجام دهید؟
🔻
ترامپ:
بررسی خواهیم کرد که آیا این موضوع حقیقت دارد یا نه. از پوتین درباره آن سؤال می‌کنم. خواهیم فهمید.
اگر چنین کاری انجام شده باشد، تأثیر چندانی نداشته است، چون ما آن‌ها را حسابی درهم کوبیده‌ایم. این‌طور فکر نمی‌کنید؟
ببینید، روس‌ها تجهیزات زیادی در اختیار ونزوئلا قرار دادند. تمام تجهیزات ونزوئلا روسی بود. نتیجه‌اش چه شد؟ چندان خوب نبود.
بنابراین ممکن است تجهیزاتی داده باشند، اما اگر چنین کرده‌اند، موفق نبوده است؛ چون آن‌ها دیگر ارتش، نیروی هوایی، نیروی دریایی یا هیچ‌چیز دیگری ندارند. بنابراین نتیجه خوبی نداشته است.
فکر نمی‌کنم روسیه چنین کاری کرده باشد؛ دست‌کم نه در سطحی گسترده. اگر هم کرده باشد، بسیار بی‌اثر بوده است.
....
🔺
خبرنگار:
درباره دارایی‌های ایران؛ گفته بودید دارایی‌های ایران برای پرداخت خسارت کشتی‌هایی که در تنگه هدف قرار گرفته‌اند استفاده خواهد شد. آیا ایالات متحده مستقیماً به شرکت‌های کشتیرانی پول پرداخت خواهد کرد؟
🔻
ترامپ:
نه، نه.
از پول ایران برای پرداخت خسارت‌هایی استفاده می‌کنیم که خودشان ایجاد کرده‌اند.
به‌عبارت دیگر، پول ایران که تحت کنترل ماست برای پرداخت خسارت‌ها مصرف خواهد شد. خوب به‌نظر می‌رسد، نه؟ بد نیست، درست است؟
همین‌طور هم باید باشد.
🔻
ترامپ:
بسیار خوب، سؤال دیگری هست؟
....
صادقانه بگویم، با بسیاری از کشورهایی که بدون ما دوام نمی‌آورند بسیار مهربانانه رفتار می‌کنیم.
می‌دانید چه کشوری بدون ما دوام نمی‌آورد؟ اسرائیل.
بی‌بی دارد می‌آید؛ خودش این را به شما خواهد گفت. اگر من دخالت نکرده بودم و آن تأسیسات هسته‌ای را که عملاً در آستانه تولید سلاح هسته‌ای بودند، به قول خودم، به خاک تبدیل نکرده بودم، اسرائیل چند ماه پیش نابود شده بود.
سال‌ها پیش هم اگر آن توافق وحشتناک اوباما را لغو نکرده بودم، اسرائیل نابود شده بود.
🔺
خبرنگار:
نخست‌وزیر نتانیاهو درباره فروش جنگنده‌های اف‌ـ۳۵ به ترکیه با شما اختلاف‌نظر دارد. نتانیاهو با تحویل اف‌ـ۳۵ به ترکیه مخالف است. آیا قصد دارید به او بگویید...
🔻
ترامپ:
نه. ببینید، ترکیه برای من متحد بسیار خوبی بوده است. فکر می‌کنم او [اردوغان] کار بسیار خوبی انجام داده؛ در سوریه هم عملکرد خوبی داشت.
او دوست من است و هیچ‌کس به من نمی‌گوید چه چیزی را باید بفروشیم یا نفروشیم.
ترکیه برای من متحد فوق‌العاده‌ای بوده است. البته ترکیه طرفدار پر و پا قرص اسرائیل نیست. این را می‌دانید، درست است؟ او طرفدار بی‌بی هم نیست، اما ترکیه برای من عالی بوده است.
ضمناً ترکیه کشور بسیار قدرتمندی است. ارتشی عظیم و بسیار قدرتمند دارد و تجهیزات بسیار خوبی در اختیار دارد.
🔺
خبرنگار:
آیا نتانیاهو از شما می‌خواهد با ایران توافق کنید یا می‌خواهد حملات را ادامه دهید؟
🔻
ترامپ:
بی‌بی واقعاً عالی بوده است. نمی‌خواهم بگویم کدام گزینه را ترجیح می‌دهد. او نخست‌وزیری در دوران جنگ بوده و ما در کنار یکدیگر عملکرد بسیار خوبی داشتیم.
اگر امروز به ایران نگاه کنید، قدرتش فقط هشت درصد چیزی است که چهار ماه پیش بود؛ هشت درصد چیزی که چهار ماه پیش بود.
خواهیم دید در نهایت نتیجه این وضعیت چه خواهد شد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 469K · <a href="https://t.me/VahidOnline/77543" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ: اگر مذاکرات با ایران شکست بخورد، آماده «اقدام نظامی شدید» هستم
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز دوشنبه به اکسیوس گفت که تصمیم گرفته است حملات آمریکا به ایران را متوقف کند تا فرصت دیگری به مذاکرات بدهد؛ اما تأکید کرد که اگر دیپلماسی شکست بخورد، ممکن است دستور ازسرگیری عملیات نظامی گسترده را صادر کند.
چرا مهم است:
مذاکرات کنونی بر دستیابی به توافقی جدید متمرکز است که تنگه هرمز را بازگشایی کند و گفت‌وگوها درباره یک توافق جامع هسته‌ای را از سر بگیرد.
▪️
مذاکرات عمدتاً میان ایران و عمان انجام می‌شود؛ اما قطر، پاکستان، مصر و فرستادگان ترامپ، استیو ویتکاف و جرد کوشنر، نیز فعالانه در آن مشارکت دارند.
آنچه او می‌گوید:
ترامپ در این مصاحبه گفت: «ما در حال مذاکراتی بسیار جدی و عمیق با ایران هستیم. اگر این مذاکرات به نتیجه نرسد، بار دیگر به اقدامات نظامی بسیار شدید روی خواهیم آورد.»
▪️
وقتی از رئیس‌جمهوری پرسیده شد تا چه مدت حاضر است به دیپلماسی فرصت بدهد، پاسخ داد: «زمان زیادی نه. یا باید سریع پیش برود، یا اصلاً پیش نخواهد رفت.»
پشت صحنه:
ترامپ گفت روز جمعه تصمیم گرفت حملات را متوقف کند، زیرا کشورهای میانجی از او خواستند فرصت دیگری به مذاکرات بدهد.
▪️
ترامپ گفت: «همه کسانی که با ایران سروکار دارند از من خواستند: "حمله نکن."» او تأکید کرد که به باورش ایران خواهان دستیابی به توافق است.
در میان سطرها:
ترامپ در توضیح اینکه چرا با درخواست میانجی‌ها موافقت کرد، گفت: «نه چیزی به دست آمد و نه چیزی از دست رفت.»
▪️
او خاطرنشان کرد که پس از توقف حملات، قیمت نفت کاهش یافت و بازار سهام رشد کرد.
آنچه باید زیر نظر داشت:
ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
▪️
ترامپ گفت: «می‌خواهم با بی‌بی درباره این واقعیت صحبت کنم که اگر من رئیس‌جمهوری نبودم، ایران تا الان به سلاح هسته‌ای دست یافته بود و اسرائیل نابود شده بود.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77542" target="_blank">📅 19:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCx0g1kbH6r_-q5bjflqkuTFZCu9i180IrfyBfaBWoPrM2qMWYNVIB48fLZaPVWVm1Szga-9QLBlqU71HnCb-XmCYBgfIfPi8MCbYndrRUOvxiYEt-2zq37r2rVUHqjxcKioifkF2zY1XAQg5glsZHonSwzCDwT-juoj3cn-lEkqsNN0m9fNay4aApreEvH2UODizA8OGybIKV3iNothrwzUjK3vpErEkD3xmWB6opjbsMo_GygSUxdCMUPTIJCAX8-G_3vZN07FGri6PzghC0j5m2AXbasaGa1lLX3_IAtRqqKDCPb1SCRBL3uwYMOkf4NHqcTJW5xogZReYb9r-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای «حوثی» یمن، وابسته به جمهوری اسلامی اعلام کردند با استفاده از پهپاد، تعدادی از مراکز انتقال نفت خام عربستان را در مسیر انتقال نفت از شرق این کشور به بندر ینبع هدف قرار داده‌اند.
«یحیی سریع»، سخنگوی نیروهای مسلح یمن، دوشنبه ۵مرداد۱۴۰۵ مدعی شد که این حملات در واکنش به آنچه «نقض حریم هوایی یمن توسط پهپادهای سعودی» خوانده، انجام شده است.
در مقابل، وزارت دفاع عربستان سعودی اعلام کرد پدافند هوایی این کشور تعدادی پهپاد مهاجم را که به گفته ریاض «از سوی گروه‌های مسلح مورد حمایت جمهوری اسلامی» و «از حریم هوایی عراق» به پرواز درآمده بودند، رهگیری و منهدم کرده است.
به گفته این وزارتخانه، این پهپادها قصد حمله به تاسیسات نفتی در منطقه شرقی عربستان و شهر ریاض را داشتند.
وزارت دفاع عربستان تاکید کرده که براساس «حق مشروع دفاع از خود»، پاسخ به این حملات را در زمان و مکان مناسب، حق محفوظ خود می‌داند.
وزارت امور خارجه عربستان نیز این حمله را محکوم کرد. این وزارتخانه از دولت عراق خواست تمامی اقدامات لازم را L«برای جلوگیری از استفاده از خاک این کشور به‌عنوان سکوی پرتاب حملات علیه عربستان سعودی» انجام دهد. درخواستی که به نظر می‌رسد اشاره‌ای غیرمستقیم به نقش جمهوری اسلامی در حملات به عربستان دارد.
همزمان، خبرگزاری‌های نزدیک به سپاه پاسداران، از جمله تسنیم، با انتشار تصاویری مدعی شدند حملات ترکیبی پهپادی و موشکی حوثی‌ها موجب آتش‌سوزی در تاسیسات نفتی بقیق، یکی از مهم‌ترین مراکز فرآوری نفت جهان، شده است. تسنیم این حمله را «ضربه مهلک نیروهای یمن به اقتصاد عربستان» توصیف کرد.
با این حال، مقام‌های عربستان تاکنون وقوع حمله موفق به تاسیسات بقیق یا آتش‌سوزی در این مرکز را تایید نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77541" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXq6uXx62YF_s3bTXXyvM5OqwjSOIrGVDn6OX0DMETXNmxIKhMyiWlBZi8FRvl5MS7bky0mAbfLYwhbVFNCkCozuUlUyPWYCZI6lp8p4C69c5qVRBfPNWfOIPkooHwsmikJPdfl9_Tb8NM6SrgDc-sHf2X8AJyrqeuJyfZ7EeEM6JeDmTfA7MxDE9bve5HrgD2yeaVFsaDSFs_JGzBPLGAFMKAEvVAKZL4EZ5SawRqKycdmxSRnieOWH1n7zKpjse2z6_7bpKq3oNP8R-pZ2saSuE0p_GDuJZ2tqhCFu3Uphgbf07l3LJQQotOT4OflyRKwlSICPWH7QenbfUWV1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزیر امور خارجه اوکراین  در واکنش به
پست عباس عراقچی
ترجمه ماشین:
تهدیدهای ایران ناموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین سلاح برای جنگ جنایت‌کارانه مسکو ــ سلاح‌هایی که از سال ۲۰۲۲ تاکنون اوکراینی‌ها را کشته‌اند ــ به آن دامن می‌زند.
ایران هیچ جایگاهی ندارد که خود را قربانی جلوه دهد، چه رسد به اینکه بخواهد تهدیدهایش را با ارجاع‌های مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات می‌کوشد توجه‌ها را از اقدامات تروریستی روسیه علیه کشتیرانی غیرنظامی در دریای سیاه منحرف کند؛ اقداماتی که امنیت غذایی جهان را تهدید می‌کند. اما موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنشی قاطع از سوی جامعه بین‌المللی داریم.
andrii_sybiha
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77540" target="_blank">📅 18:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHwrfxitlgRi2o5N-cnzeqEVJ5CLRNl0ehrEYgN0xCdcECiEvku55tHYW4r9-Wr5X_d5Zo2aAiMiFAYxCEDOTszaOzS_mVNhuUmbk3TXs9ZWFuKJM5dV53eMRo9dCTKoFGQLI-2wnsN2C0n3PLSwKY1kG9VAyAC-YyK9jhuR1kUoXTG36MmEhoyWKixUsVfyPAMccZzJ4M_bhJi0cTJ06wKNLa4gdrhi_EVPCpJdgPNypTTsuX2IRfUWPbdviUKuHvuU0AT2ZmjrbDG8-QHU4dcHJ_EQWKHlydaMIT0lV7sHcKUAiVbZn0ysINntrAAH9rEgJevWKKRxMadfcMXy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی روز دوشنبه اعلام کرد که سامانه‌های پدافند هوایی این کشور، پهپادهایی را که از عراق به‌سوی تأسیسات نفتی در استان شرقی عربستان و همچنین شهر ریاض پرتاب شده بودند، رهگیری و منهدم کرده‌اند.
این وزارتخانه اعلام کرد که این پهپادها توسط گروه‌های شبه‌نظامی مورد حمایت ایران در عراق به پرواز درآمده بودند.
وزارت امور خارجه عربستان نیز این حمله را محکوم کرد و بار دیگر بر حق این کشور برای پاسخ به منشأ «تجاوز» و بازدارندگی در برابر عاملان آن تأکید کرد.
این وزارتخانه همچنین از دولت عراق خواست تمامی اقدامات لازم را برای جلوگیری از استفاده از خاک این کشور به‌عنوان سکوی پرتاب حملات علیه عربستان سعودی انجام دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77539" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g9ln7J3bh2wYgchqviau0OpYIupZNoXUc3DCAYuKgFtFteZFuVTNvMFm2Ar7g05swW2Yh0Vz1697-NKD52QM2wU0nrX7l1hpbtgtY_LMKLMg_PfBEvcuJ_2W6WO-YN0YDRfvjgVZzRNEafYmoHXAfeMnjUJaJL1di4gqHao_PlD4Ye8JhRW8ZKk43KW1X-WAd454-_rlTdJ7KYT_Z4mLYfJJL5JdZDwSy5MsG0cUgMNA99cy63_RtHiMYFSGciNtxGSAdZCl94uaBuHXNMsC7AQJN3BDMiqppUgTpQGq-r4lwu2ivwqTcVzm4pWh7ue790jTzi4oXiWlWQ50uR2IVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای مسلح اردن اعلام کردند که صبح دوشنبه دو پهپاد را رهگیری و سرنگون کرده‌اند.
این بیانیه مشخص نکرده است که چه کسی این پهپادها را به پرواز درآورده است.
کمی پیشتر، تایمز اسرائیل گزارش داد که ارتش این کشور دو پهپاد مشکوک را بر فراز مرز اردن رهگیری کرده است.
در آن گزارش نیز درباره منشا شلیک این پهپادها و زمان دقیق رهگیری آنها توضیحی داده نشده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77538" target="_blank">📅 17:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpa3mO6BR2BNceVWNxKhTcKc9TMhTAXiOpVNhawYYqaUmxjSY7mSI6Oo7ax-7ECzkglRj5fZRKRvy8gjNqb_W5SHClsmLKXUGfk4IlnFcKx1U7cAVWncEizo6sJcW-GR5WLoWAy30kj37-4uc2PLyqF3iqGL8e4yzgvpg79iDgIVwuXKkvcgnsrVePz_I2iilnzWhU08PyvzeILRQwdeO4B_3tamuEt3cBo49mRU1G4YoYECgBQpe2ze1yugCkE_8z7oFtX7YhPXW3aUs_aqtj0l4JcDCoOMtZLWWBS8QQ5bLj4YzUiIDWHRDeRXn0YDB-jTgHfHLdDnO0-7A4B1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«احمد الشرع»، رییس‌جمهور سوریه، روز دوشنبه ۵مرداد۱۴۰۵ در گفت‌وگو با شبکه «الجزیره» اعلام کرد دمشق با مشارکت چند کشور در حال تلاش برای دستیابی به یک توافق امنیتی با اسراییل است.
الشرع ابراز امیدواری کرده که چنین توافقی بتواند زمینه را برای دستیابی به «صلحی فراگیر» فراهم کند، بدون آنکه «حق سوریه بر بلندی‌های جولان» نادیده گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77537" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpzhS2eeFkTgIypADcmZuazWt1Tes0rZn8QP8-ibpiLvsTzZNj5-2PbN_6Fz_4StnroyrCOquSQMEOE5FtiADwwbQx6brLneCXmFuUS25LpsoC7AhG55A7owODqe7PMMgzJVSBSdc6nlLbxUn_U_IT-0w4jCP_viZCs33IjkmUsRfHnNfCXH7uAjvBgS3CLK3GbgPadkgoFxxDGEh0XX5VuwLuBxzJYGn925F-N4uFIdRC9_lyuGB0LHNPxBTlTBFzBM3eSZofWXvBA7ZL6i7lXjnJF39IZrzcDc7UxTXTKsU4ARl8xK04sJ6rmTT7xukwPoOaF5yLBWWmf981XbUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر پیشین اسرائیل، می‌گوید هرگاه دوباره به نخست‌وزیری برسد، «فورا» قطر را کشوری «متخاصم» اعلام خواهد کرد.
آقای بنت در شبکه ایکس، دولت قطر را «خشن» و «سرطان یهودستیز» توصیف کرد که «شاخک‌هایش را در سرتاسر غرب و حتی در دفتر نخست‌وزیری اسرائیل دراز کرده است.»
او همچنین مدعی شد که در دوران نخست‌وزیریش، اطلاعاتی را دیده است که نشان می‌دهد قطر به سپاه پاسداران کمک مالی می‌کرده است.
این سیاستمدار راست افراطی که از چهره‌های اصلی اپوزیسیون اسرائیل است، قطر را متهم کرد به‌دنبال «نابودی» اسرائیل است.
آقای بنت نوشت که قطر «کشور پیچیده‌ای نیست، میلیاردها دلار در یک شبکه نفوذ قدرتمند جهانی سرمایه‌گذاری کرده است که صدمه زیادی به اسرائیل وارد می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77536" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY4937hwy_0PPqEWJXJlKCwqGGqFsZlprcMV9UsWeUXcQhq7LPfL8V--E8wogM_PoZTEL4ngiTTDgkKWWAAzdYE5VE22Eh9Bul520Z6B0nN-UMBVzAXk2PMREThZRrFPHtNdXZJClL_8oNf8qqGkFRkqbiel3cVboGs06y69c3Jk-U_rRBgrzf7G13oOOeqkKTiqixAFg1pSpB9KXZ_UsiLybWkhocyOrWpONf_X5ssqXtTNAdszR2BluLDmbU4pLGIDb9udx3i9l6hYhZhDrInihp-XhoNHsVq6d8QgFK_Njuja_MCcIZxtYo2ZXMD__eY6KJFQkOBR40hUDqDkYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع بریتانیا گفت کشورش از اقدام تهاجمی در برابر جمهوری اسلامی حمایت نکرده و نخواهد کرد.
وس استریتینگ در مصاحبه با شبکه اسکای‌نیوز افزود این موضع را در نخستین هفته کاری خود صریحاً به پیت هگست، همتای آمریکایی‌اش، گفته است.
استریتینگ روز ۲۹ تیر و در جریان تشکیل کابینه اندی برنهام، نخست‌وزیر جدید بریتانیا، این سمت را بر عهده گرفت. او در همان هفته با هگست درباره امنیت دریایی در تنگه هرمز و تعهدات ناتو گفت‌وگو کرد.
او گفت با وجود این، زمینه‌های فراوانی برای همکاری دو کشور از تأمین امنیت تنگه هرمز و جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تا سرمایه‌گذاری در توان نظامی بریتانیا و ناتو وجود دارد.
استریتینگ همچنین گفت اروپا روزی از دونالد ترامپ، رئیس‌جمهوری آمریکا، سپاسگزار خواهد بود که قاره را از رخوت بیرون کشید و متحدان ناتو را وادار کرد مسئولیت امنیت خود را بپذیرند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/77535" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gVdDsc-IKTRYzN1fsWXdaKuqiMSJMx6mTIn5cUddInG48Edp7JhDvOC0774ehOQ647_Al_5unvLbCrXCKVSo7hjAzTqvahDIwvxNg8ER-XtaDYOkK5xAe9Aa6JKzlMRgl7F9iu3FiQDCYoEV67Y1i1aW_emsDH5pIy34jLO5NsP52KCLFNmsHx2_hrumZblEMNrsaA5oc96o_VaFGm1oPTUppFsPSQ2gLsU-DAGBT60MwLtbO7x3-hExrUq7nhJY6D7LhT7zHUE1r7tutHmdbc7qWJT2aK500b-HAEi-KozoUQ2LLFzY9s73QqDFEtt-Yxji-YzzdeCoL1zPHodGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77534" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH_FZClfMaT54LqL8sT8nJB3XMuYepOGRPjdLAb3k_Zt8sm2_XKQ3CmNCBOLnOdjWdAdmqfTsrLaHnM8gJ2wIoGxervitNF-YAcvTYEii2veNmTm7FqyMOfamE_vy6UQ_vJSMxq4gY0T3Pl9u_wqfqQP4BlKRKR_pq8Dw1-vABq1WTHbcNE9OETCjOM6RY-VOzhj6NbgqbEsF_O4LCxOBtMacM0689bckSoVgFSV5V_JXfxtSVljECNnF-r9C4c1ONpbsoYKMOw-crfIyfsWQMbYu-ND0B8ED2cEgQKRuABs8mLyzrfXVW6rlIb0bmKPWM2k9E-fce83-iyDOnT8Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، دوشنبه ۵مرداد۱۴۰۵ در نشست هفتگی خود با خبرنگاران، گزارش‌ها درباره درخواست ایران برای مذاکره مستقیم با آمریکا را رد کرد و گفت: «درخواست مذاکرات مستقیم با آمریکا اصلا با ژن ما همخوانی ندارد.»
او تاکید کرد که در حال حاضر هیچ مذاکره‌ای میان تهران و واشنگتن جریان ندارد و خبرهای مربوط به درخواست ایران برای مذاکره، «خبرسازی» طرف‌های مقابل است.
بقایی با بیان اینکه جمهوری اسلامی هرگز از دیپلماسی برای صیانت از منافع ملی خود گریزان نبوده، گفت در شرایطی که آمریکا به گفته او همچنان به اقدامات «ایذایی و تجاوز» علیه ایران ادامه می‌دهد، تمرکز جمهوری اسلامی بر دفاع است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/77533" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77532">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAD1qCd3UXCyAi1m6xFAz6gdOXkqwGpEl2d1M_oYZ71Cp7EUcQ7ppP-V5l5pMO68PLhn1p5geRYdvDkDJKRtdLPkieKjETqDc3Tc4pDMHwnQ7E6Zalh8NXkR7hnGnKPXUeAZTT_qhvM1RqX5jWSBUVUufLUBjzU5bpPN3kRZM6O0ChNXgPUfs_P3fxpBP1A-IaJvXxR5J54sW8XMHbSFwyLyPv88q2jgWQBeQddxmjIPvgCF1uofT27iINMWq8OmnbWdXpKPmCeJkBafrM9yG1ZZLh_KtDY1ETmjNCA4qvunGd646laZohwf_JM2TBvvgSRMH5IeRTp2s1qxzuEHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلویزیون حکومتی ایران روز دوشنبه پنجم مرداد خبر داد که سپاه پاسداران در بامداد همین روز مانع عبور شش کشتی از تنگه هرمز به قصد خروج از خلیج فارس شده است.
خبرگزاری صداوسیما در کانال تلگرام خود نوشت: «در ساعات اولیه بامداد امروز دوشنبه ۵ مردادماه، ۶ فروند کشتی متخلف با خاموش نمودن سامانه های ناوبری و موقعیت‌یاب خود... قصد عبور از مسیر غیرقانونی و نا ایمن جنوب تنگه هرمز را داشتند.»
اشاره این خبر به بخش جنوبی تنگه هرمز نزدیک به سواحل کشور عمان است که اعلام کرده تابع قوانین بین‌المللی برای استفاده از آبراه‌هاست. ایران در مقابل اصرار دارد که کشتی‌ها باید از مسیری که سپاه تعیین می‌کند عبور و مرور کنند.
خبرگزاری صداوسیما همچنین نوشته است که یکی از این شش کشتی‌ «دچار حادثه شده» است، اما تاکنون هیچ منبع دیگری این خبر را تأیید نکرده است.
روز یک‌شنبه هم خبرگزاری تسنیم، نزدیک به سپاه پاسداران، مدعی شده بود که یک نفتکش در تنگه هرمز پس از برخورد با یک مین دریایی منفجر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77532" target="_blank">📅 16:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77531">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6BX-2HKpBdhVF3Sb3FnF9AlNNpnOJnoP6ianT-LYsN-l7_j4xDdDsghz7XFrSgt9Q3BifxKbLJG8DsCX6wGgiwVL2maCShN9DYObpN_sFkUx00qOtjVDzkttnhyVRnr085STcUGNRWwUz-g_FkYdOkJurRNtNa_4iGtv5tjpTce1QYbKhWaVVIt_AhYcwHDCadjo5xHpO1CYTxtE75qnpWX9fYHpLCGTX2zPWRtBNgrOfVbfLWc5buqBM62nfIgJDagB54qhI6IQ35z8oG9maiL6Z2oFJ6TI25J23bjDtEcwczcHrk9ag08z5_DpHuUNat7T5biPcqcno4Ljl33Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت امتداد گزارش داد حکم محکومیت پژمان جمشیدی به تحمل ۹۹ ضربه شلاق به اتهام «رابطه نامشروع» پس از رسیدگی در دیوان عالی کشور به طور قطعی تایید شده است.
الهه محمدی، خبرنگار امتداد، به نقل از ملیکا پارسا دوست، شاکی این پرونده، نوشت شعبه نهم دادگاه کیفری یک تهران این حکم را صادر کرده و پس از اعتراض و فرجام‌خواهی، شعبه ۲۹ دیوان عالی کشور نیز رای صادره را عینا تایید کرده است.
بر اساس این گزارش، اتهام مطرح شده در پرونده بر مبنای ماده ۶۳۷ قانون مجازات اسلامی (بخش تعزیرات) بررسی شده است. طبق این ماده، مجازات رابطه نامشروع تا ۹۹ ضربه شلاق است و در مواردی که عمل با اکراه و عنف انجام شده باشد، این مجازات تنها برای فرد اکراه‌کننده در نظر گرفته می‌شود. به گفته امتداد، دادگاه کیفری یک و دیوان عالی کشور در این پرونده تنها پژمان جمشیدی را به تحمل ۹۹ ضربه شلاق محکوم کرده‌اند.
ملیکا پارسادوست با اشاره به قطعی شدن این حکم گفت صدور رای نهایی نشان می‌دهد «فضاسازی‌های دروغین» درباره این پرونده، پایه و اساسی نداشته است.
او همچنین تاکید کرد اجازه نخواهد داد آنچه بر او گذشته با روایت‌های دیگر بازتعریف شود و گفت از ابتدا این اتفاق را «خشونت جنسی» توصیف کرده است.
پارسادوست در ادامه گفت هرچند این حکم از آسیب‌های وارد شده به او نمی‌کاهد، اما در شرایطی که به گفته او اثبات خشونت جنسی در ایران دشوار است، احراز این موضوع از سوی دادگاه که رابطه «بدون رضایت و همراه با اکراه و عنف» بوده، برای او و دیگر زنانی که تجربه مشابه داشته‌اند اهمیت دارد.
او در پایان با اشاره به کاستی‌های قانونی و دشواری‌های پیگیری چنین پرونده‌هایی گفت با وجود مخالفت شخصی‌اش با اجرای مجازات‌های بدنی، پرونده را تا پایان پیگیری خواهد کرد و ابراز امیدواری کرد این پرونده زنان دیگری را که با خشونت جنسی روبه‌رو شده‌اند، به شکستن سکوت تشویق کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77531" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlnGQZxZyb85KJlxXBKE1Lyrrsu03sUA0s26sZmEk3X7zAGsk4y_7zKjUUJRR2XoBwiNh7O-Dx3GITiRiizGkx_5ZVC112sKF9YWTW-1TzQJx7wU9jg058wIXq2IMnQFUTbLH-jfpt2dYzbyk-Gr_B-mx0fVCuu7-5xI8lzH7fP5MYysmdwqbW7b8CpREcTcLXBzMGVRM5cQqJUt1tq-PeiWQwNwWGW8jhtLD9gFyeK4HI2kcg_FvYO4zpb5UXLGu0wNa4FcIjOthqntohmKVkarhXQiUKtxeF2Ts1pAB-DmHcsiCN3LIZKuJ3KHL3tgL1Pu_Z9Jl7GFoztI_iFaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش خبرگزاری «رویترز»، همزمان با ادامه وقفه در درگیری‌های مستقیم میان ایران و آمریکا، بازارهای جهانی روز دوشنبه با «کاهش قیمت نفت»، «افت ارزش دلار» و «رشد محتاطانه بازارهای سهام» واکنش نشان دادند؛ در حالی که داده‌های حمل‌ونقل دریایی از ادامه اختلال در مسیرهای کشتیرانی منطقه حکایت دارد.
بهای نفت خام برنت بیش از چهار درصد کاهش یافت و به حدود ۹۲ دلار در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز بیش از پنج درصد افت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77530" target="_blank">📅 16:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77529">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pddK7vvOY_YZFnHGHD2CxcdxgmDI9CT0_pIx_SN8oXOdEIXyQrdghi0isnVB-MHio6Le5uYkJtVcMqg4yzK1GkqrWkEPtO-btsilrS7rPxKSKGwv25jDI4hEDRbxbYVA6NAf1nESUjqbL6USlxHGU-h8FevAgtrqeXGh_hbr-PGnkOMC3thGDRU9wmZsnhpUNloQ1FMX1p3q5BpTHsSSIDgeDVoNj0lg7fJ_vZUK778cH2V8ndrZ86ya-Z_3oMUP1uhmEIcZFHU9-q9xUTjC23NU4pTKnbNp7nFs-s4nO69CPLlSWhaw568wVMWl5vR8BauM03GkXid_grfYNZatyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در بیانیه‌ای که به روزنامه وال‌استریت جورنال فرستاده، گزارش‌ها درباره کاهش ذخایر مهمات این کشور را رد کرد و گفت ایالات متحده «بسیار بیشتر از هر کشور دیگری» مهمات در اختیار دارد و میزان آن نیز «بسیار فراتر» از نیازهایش است.
بنابر گزارش‌های دو روز اخیر، ژنرال دن کین، رئیس ستاد مشترک نیروهای مسلح آمریکا، کاخ سفید را در جریان کاهش ذخایر موشک‌های رهگیر پدافند هوایی قرار داده است. این موضوع برای او نگران‌کننده است، هرچند معتقد است پایین بودن ذخایر مانع ازسرگیری عملیات رزمی گسترده علیه ایران نخواهد شد، اما خطرات آن را افزایش می‌دهد.
چند مقام آمریکایی نیز به وال‌استریت جورنال گفتند دریاسالار برد کوپر، فرمانده سنتکام، معتقد است آمریکا می‌تواند با محدودیت ذخایر پاتریوت و دیگر رهگیرهای پدافند هوایی کنار بیاید، زیرا در صورت تأیید ترامپ، افزایش حملات آمریکا توان ایران برای شلیک شمار زیادی موشک را کاهش خواهد داد.
کارولین لویت، سخنگوی کاخ سفید، و شان پارنل، سخنگوی ارشد پنتاگون، تأکید کرده‌اند ارتش آمریکا برای اجرای هر مأموریتی که ترامپ انتخاب کند، تمام امکانات لازم را در اختیار دارد.
وزارت دفاع آمریکا شامگاه جمعه کارزار تازه خود در بمباران مواضع در ایران را پس از ۱۳ روز حملات هوایی شدید متوقف کرد و تا امروز، بامداد دوشنبه حمله‌ای از سوی آمریکا گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77529" target="_blank">📅 16:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77528">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAGkOtgmiFRnKUEvDDwi7bZxi6Lm5-vXzXuTRFDhacShQjPtqBHfH9JmZTcaTLVhN9vvI5Sm8o9toZeDCzkEXw_BTMSD-zAbBbEpiVf2ClckHAlqre7b7qbsy63e7Vla2IzCu_sYkz3xKuj6wO89VRACFIPZdGhTnouRJkW-rFw4N1xL7Uvz-3lnSDM_7sZIz6NcAfVLYe1T6jJQkQuJsL2cRQBq8ONJV0NSILvd0HPLD_7YG5wiSkq8AUol66sEo6yq5C2HPmflDLbhALUTcEYM-N8RjCYh-1ZeBLgRA3RHDv7ry82a-jYYmLC40J1jfOHbxTz4OOExXvAMds4qgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اجرای قریب‌الوقوع حکم اعدام دست‌کم دو نفر از محکومان پرونده اعتراضات دی‌ماه ۱۴۰۴ اصفهان افزایش یافته است.
«علیرضا سپاهی» و «ابوالفضل سپاهی»، دو پسرعمو که در این پرونده به اعدام محکوم شده‌اند، برای «آخرین ملاقات با خانواده» آماده شده‌اند و احتمال اجرای حکم آن‌ها در صبح سه‌شنبه ۶مرداد۱۴۰۵ بسیار جدی است.
همچنین به ایران‌وایر گفته شده است که «سمیه افشار»، مادر علیرضا سپاهی و مادر همسر ابوالفضل سپاهی، در همین پرونده به پنج سال حبس محکوم شده و هم‌اکنون دوران محکومیت خود را در زندان سپری می‌کند.
اطلاعات موجود در حال حاضر تنها درباره وضعیت این دو محکوم تایید شده است. با این حال، از آنجا که چند متهم دیگر این پرونده نیز با حکم اعدام روبه‌رو هستند، این احتمال وجود دارد که افراد دیگری نیز برای آخرین ملاقات فراخوانده شده و در معرض اجرای حکم قرار گرفته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77528" target="_blank">📅 16:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77519">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/obRWQqbcMLcqGUtGRt-rFAtwxrn3X5FRmpEbG8mp86QK-GY7xS5GgslWqQs2yIH2AVUzmE8cj6b3na4FPgfD4JROZR9sz7lrO8S-Ug38KtH99SxhZBGtvEstBWS1Ai-Jbao5CD-wVz8_ucPonBHqTWJyXUgbESLj0cZWBwp_rVnrBrVpOgxqgCJ8K-CzF9rDQFutC5qPNduiB2gD76K5ynnyPBEfRvsaObhaYZijMSyiwDEbRAD6KOCLYR7uJjI7InaQaLQK0hJanpkorsWg9220xhYzEWAzn_4yFqn24wOnfKxETIUGTof5ngAhF6Unf28agcII7QDzs4xS7znPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W_eQwB59FA2H7JOiSi-LPMTsyvT-6x7WPqTUQLR4sX_xCjDCRvy_W80kti3VOllpFzTpvFG-JRLVuqUNso9bl2x-hIK_fHW1yZi2K3E3viTcDyhUqRS48AM1qDNcY-sYHOjtlbAdoSzWFwAf6ZRCZSRUfk9s_Q6k2H3QV4YkS_uHhMifMwoQiO_i0qNTs6MUsNEkCTPN3L7GGnHBOpUpobyDMAdAkYDJI_jAEZgKF7MDOav_66EXyMQlPbzEip5RjyI-Scf-pYv5TUizSs9R40D3MNdCf6S-e5PPF1gDZlRQF9TrkF0hD4AgEMeknAsP9dsfdPQYJSvtCNu5dqXhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QhUZb4V4KjHXVZ30r6MD-O1s48gcFF2Jgcl9vCqaaUm9zWceYNXd2gzy1pEbAShlSlE0lPRSpJqoxcPnkZfjxhKHPGtwTdFddosUUo2jTO-FW5tyKzgK5AFl4zIcF4n7Fbp94L5XJ1zf5wshSsnLz-Lk1SgyfuKb4Ihtgy2PGav7nYRm9l5lH0yI_cXJm_Vf9sUC0UZSUAG2f8ZkKIPoWUjklLj2LrD3pzQVIfWKjxLC-sbYWi0t-yCtSfbGrcuFpPQpZUXcccjYEDCjYUHb0Dv_ZWhKsgDzgTTfnK4mXjI4o0pf3bE7YMCP9l7ahen60DVmOm-y49OP7o-Dmt8jqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BeQdjGH_-Ka2XlBXlS_Dh1gLzyo6Qggd_wKt_I82RriG3-b0Bh1A1wAwFnRTTg3kD4qhmaGys-nf7DudnLTQ6tn1aU6vDbnlhZL-qAvQCO4y4s_D9xqMgpQOJwOabyzXjBG6_8AvgB_bcJ_Xbc7Qgk1Qc77lp6ouiywUbssoo_zZXANU4G3oJQYbUkAy9GZDTq0N8pGlpE2pJSUIcJoH5DnbHz-4aAU57URk8j2OLAU-8_0jUQJN9D_ecFcOClepODahbOIEJEc4o3Mn3FHIeS_1Y32Na_DQkOJ-hEOFzZYrHXQAGtMaEvJCTSQfQdUV3-YVZaUf2PMrf3v35KhP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ePxeSDl4M2Dd_HVeaJVOQRjw66wrMx7qhjaWTdf78nn2R_gk3F46xdyIQeayR6lgmAUMsYPXGvUzfTeFj1nddlMr293wI8dQ-JSo_WQE-wzOAYmAloUlyUcIQQT1B4lagEwNqYjO2rDuE3UnFGLb8r1_o6nLsiAqrWbkaUdJjhmUHbIAw_IxAoy8De2v2TvVAGJ2mwsvHRlmENsri35sPQXi4onwQNeSiVJ_KQx2m91HI3LxU06D-Wqmh4I_br1TE8X1sCz3u1PMADIcuyTYK9cv1qln1jbn4y-ZvV8cxlehD9mKghve9EVrjkuH5hTKesqkb3pG7woo2IxW3sGTSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DjyqeaNLt-O8hqh337i-I6qvbnfL-wRE1VUhwbbd1QCFljvrNNJaNSIHx6l63ahDKbXLLMsZwV1utA2Pu2yHYeSSVSMYgDQqswNf5sTglqfpBtw_YGfOizxFn7oFRUnEfPRT0waOK4-0YuKVgJ83fWjB37G7KgiFfj6i69vy3pwKO12l_MW_DEeUpcJfE2d1sP-3_HtSIVX8kydq03FOO8VDKzOsb877q5wMMWscUe7v9TBWy7Y7Zyr7o-scUYLUOuedhrr1s2yzw4Cq0CmySh3njopc-R5YTsw-G5kVysXZZzmLXssk4JA-8lmqcymtaW0PTy0VvU4mC1bozrBd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qyeKNy3i6TGCodXMelxE_ZTSURwEYnPcvI8w3izbR1NDxkl8LuIYgKOZ5BSIbj4zvMFGjfsIoz3XSCiNBBoRrPc9oKmd6ZVGTk-KRM6IJphTUKQu9mOEPOtCKe8f4MjAv0OvNts1lCL-D2u9c3QMe252xs2oeuTxTBxqd3QxDWIvxB5J43demSJhSYlg9St0ADigy7bSRyC74j3wipG415uSIbhQRNweY6-ermALJxwcBRH59kOzuMkG_0TGpz1PaWOVCzFxqMBPltUmNq6kUXarT4FFo1AIE6CVvj839CUaPwXVxPVqwIVUkPcr2jOEim8Twvqtxl1VGYR7INYgKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FElQ1q3P0eyaQFUkHxviiOpFIFxTUYbStKN3bNo0lhfb_RFHAOEomaCxZaB-Ht0t3S3pktR-tlg7sIj_eE1HpelV3t6pYWvp6Bccnmhlsj9CGTseEv7PyMUJNg74y-SNJDW4oJjvGCwsoT_fUtqw-9vSvxRuagF5dXkHV6sUqy4BNc-wN1YkDtiZ06khjtaSx-6MQHYEk71joajb5KB4OJssxD5dQ-vcqEGMFp_STyiOI2tw8ZstNbZPp2jB5s8VPFF488527BSVaSicc-2uqNHnt6pZzkHVmFv_XE9ZR8UMxvdNwybnT0NtHMdc21x3S_HefQDNRdAyjGLtmIuk4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hs5j5WoG3yCIscOfmMGkZF1rIH4x0NHNkj_UxoUaF2t22v3w1HEcSpZATCrmUfF-bQXiwIt4m1tSNXpQ5SvlH4iK-GNMCA1XusioGiaBbwqScVVIgEnxzC46GTr3uZbUeJKnH0Xn2XUHIlxMwAX_Pe4PAaQ-jXzz_k_53xUudeO1dvFDiL6_a_bB05ZzD3v8DwGm_kyRd8P2NNb_F-biK1RnGZ2gZdeYYBlqs_ylIUddO0oKlyRXyE7lTg_-0WDYf3L2VuIG9aa6xM6XRwzEGjkpts_Wu5ISaxv_iEh6_NQctcxKJnJzhfO2O8rB_8eSjQcQflew0-xQ8jxa4O-XNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه تصاویری ساخته‌شده با هوش مصنوعی را در «تروث سوشال» منتشر کرد.
در این طرح‌های گرافیکی که با عبارت‌هایی نظیر «این نفتکش اکنون متعلق به ماست»، «خداحافظ اتاق موتور» و «دیگر موتوری در کار نیست» همراه شده‌اند، صحنه‌هایی از انهدام و آتش‌سوزی ناوها و نفتکش‌های جمهوری اسلامی ایران و حضور نمادین او به همراه نیروهای آمریکایی بر روی شناورهای توقیف‌شده شبیه‌سازی شده است.
او پیش از این نیز تصویری گرافیکی از «حمله به خارگ» منتشر کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77519" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oycI1vqBnWP_UkFW-sElJh86EqnlohAdOZ_Guw4UJEcaD1YgDzgTfTwspVdioYMphnQz7gkALxr2q_LXQ9xBNZBh1AWu9RiV9I8tKrHagq1POzIvmwfzg4SqnalxRkVdpXeI6qqplRI7zjFVIezoeVCVsmuzPCDxKRcaB9OvLBgJJ2wSRgj0vY87gHu_uboBIsQuxm-_yfALLf4zQDLSqz6PoChXcJZoHisbxqNcHl62U5gx-Ma12CGNcH_9-SdRhOQk6iERbCb0M8LEts-KRSkIhMNzQpQcb2xiuHWqKHheRUxM1w-uLWRmjcpccJVM-AEIU17vZLURMBZzODDoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zv_TpUMSmLgC6b3sDTWVpvoFPqTQCcuiwRoRmTGHfebOOkbASou2Z4c-ygMYxJC2D5ALL3VhTfTbEb3bkjR4OkG44Sbs57KPrD7BZR_gloZ0o3Fe0HHDuFlbn10gme_-ugWRWWPk4wjmWNcfOu2uuTt4BbVv2eYOHTLKJ0cVd_hIb_N7Vg8WwzZVnZZKs3B6oLChxHx6oSVh6GSRXT7Ju2rHFyTvurTgXEFK-7GCfMj6SbiB4T6XvFIgtAxa12_7xqX3uHYixpNlIxw1Y3_4caG5pThbPT39cK2QBbE1Yt5uATEWT65EbMRpnRLRuYu_7CUdqv2Wi9I2arqdtv3Myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kACM39bQ40pUx9J4_9KSdXzQUvir1287wVCTs-xNiFbgDxtZ6DBWBT9g7FMEqSHWV0N8OqZ52cB8hA73_XxCnihLATWJXbsJG9dqw8jPaFkYFDzOvvDUq_JzkHHjVjhzBPYAawcVHdTNO2Bfl7b2r5U8A2Ry40wlx1gptFLt68dQZKxCjeGCbKjHXvZ-THnNXBDOnnyPW2oDXSexit560t944XJZLXIw03yCsti7fHwnuiHAVR7WdPyUTzW7abJ0zFivKbg98VagRBfHP_41Xul7eATJ48iHzkaHr3rdzgH1gxuLkZcSxdn4mrX5BtmJR6zH6SjAeEV6rypKMUyiqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g9oKdVnHsLfxhojEh2IeBRtOeGKC7iwpedbVKJPLFi5kqPmQqi8KrOE9CIuENgYPkib4yQWnzqXnC7BwsXBOx9FcfP6ku2Mo2X8UMymXi6lYeYJ6xjOhByCx02ttWHGW7GwvWGNbV4CRU7BtE3uUu_KjosUsF7oJzpBboDdtGlMJWnS8-vvZxiXo35fmJVJkse1Qc2o6WglzqcJbO0cXsf8_M91zruNxKtv-dFoGH-xTshH8-cm5H3aqGCHQ3_0zYTVzmG-Iw-ZkDn4B0MmsqX4QY7Z-RlitLMIvKLvriBg9QQttVliPjFLZiMRVSSMT2t6gM1p99c4pqcfYRXhLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eGaanCDUItlSkKKs9IDL7errt-XMTkuZuycazPDx9Gf6Rm6V3d0Huu47HWtfhQW1TLBoav-MgvJMGWDr0OF-krUa24VG27-wNClvHS43ol8D7VlnnqCZtoFj0NZx7a2PUG-pAzIC6H51_nqtwzPztWIhpks517l8t9wrxSrojhDHtcw4pPwsh7VK7H_xp6r5dTce3vQPBzbRAOcqClpbHU1hAz5kyD_CMnKIEjF7oDbMHpd__bC2Hz0CxYcm7HUX9nbTcALckfWKQg5BDEdEFB4kt0aIp-VZqvO6d-3GNFZ4sV_sfkkbBFx84v0qMNpao7XsB_ABYPyJMj66ZIsMDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حساب کاربری خود در شبکه اجتماعی «تروث سوشال» تصویری ساخته‌شده با هوش مصنوعی منتشر کرد که یک جزیره شلوغ و ویران‌شده در میان آتش و دود را نشان می‌دهد.
روی این تصویر عبارت «حمله به خارگ» درج شده بود.
ترامپ تصاویر دیگری هم منتشر کرد که با هوش مصنوعی ساخته شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77514" target="_blank">📅 00:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrkAnQEhbNZP3ozADuOXRo4H74sI8-EfVMAoAGGjIsTk9Jb-J9QiDAoXz5LQ4l9anTfb6Ybt_D2DsJ9i0o7zTVBb9j46s5-JxBJ2FGXmYB41Jn-IfikcVPeSHdhDEwLPdRvRZC1C-ZT2mB_G0bRT61nqolFzF7qD4kYNXG0r1GxsUkY74TX2wcz8zlA5zfCg-Hlo2G7yh4Y1X3fzDoCGb8K6pH0664k0BBciuhOxHsqI6hc5D4J7MxM9L8KrExAn6tQFoeuc_QYsozh0Iwfm9efp9Z9Dl9URY06EETTlDyTxIXUkbBFScmG2Xq5_2A4NRaUwgxg15cJE6GnWOZEIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از منابع آگاه گزارش داد برد کوپر، فرمانده فرماندهی مرکزی ارتش آمریکا (سنتکام)، به دولت دونالد ترامپ توصیه کرده است کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا به اعتقاد او این عملیات به سقف اثربخشی خود رسیده است.
به گفته این منابع، کوپر ارزیابی کرده است حملات دو هفته گذشته توانایی جمهوری اسلامی برای هدف قرار دادن کشتی‌ها در منطقه تنگه هرمز را به میزان قابل توجهی کاهش داده و بیشتر اهداف تعیین‌شده برای حملات هوایی نیز از بین رفته‌اند.
منابع آگاه افزودند کوپر به مقام‌های آمریکایی گفته است در صورت تصمیم برای از سرگیری عملیات گسترده نظامی، آمریکا می‌تواند ۲۰ درصد از اهدافی را که در عملیات «خشم حماسی» هدف قرار نگرفتند، مورد حمله قرار دهد. با این حال، او تاکید کرده است اگر تصمیمی برای بازگشت به عملیات گسترده گرفته نشود، ادامه کارزار بمباران دو هفته گذشته توجیهی نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/77511" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
