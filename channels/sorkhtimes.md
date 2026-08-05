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
<img src="https://cdn4.telesco.pe/file/Ld5yOJa3tejneW6IZaC3-_A9lmwM09Udc1Fk3IzUxZOMXg_c0gBR4qf2DC2-1wo1kajZhDpTboOnJla1NW5K82A6KW9B15gQ2BszbeQYB2QTCNogwr1kVGjhDFASYEf_uYVoQg9zOERambTSIHoGmd1ihTD5C-WcbXljyWhxrgJE0La7WDSO-VthSekJKNM9I4-A1Kcbi-U_pGfVE5yw0oY9Ff5PdWlgyXLOGShUgW5Q5hWzFb14vYWRXfYJrCFDU12HHFDQrD9a0McG-0d16TvQKFlwWLYHcQ6Flx8zDzdzVqNJgtEfoz751FafbyY087ypwFhwdR8uiRlIrb-8tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 15:51:59</div>
<hr>

<div class="tg-post" id="msg-137388">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddNaTLfplu-1LssXOlTHTZfdIZrgMHXWkmiXh9xh1L6oQ19VS79zDquP2-YGd1AEA1Rk88gsin_M3Yv-8jPw-oPduonS88ddRk_Jh7uDswDrac9mNpYMXn_SBtip66gmIrsEB_kWnxAyYbICG4HeOrMyaY8xdU1nQhCAJKrbTci54LF3CMBgneucHIFnwRKbwWIykJieUTJUaFHLs_IZcDgNOdhmsldCNK9iRLZd4CP0ibl0L8-wTOBB3Xpn66UujxyLE1sHV2VtKvJXDmik1sHW-bRyGXuRSdceo9jbZAHo3pREg8TekvKdA-MC12RPCEkz-zy3QI9AWWa1mbUr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
⚡️
پس از شارژ حساب کاربری و فعال شدن فری‌اسپین‌ خود، وارد بخش بونوس‌ها شوید و ازین فرصت چرخش رایگان نهایت استفاده رو ببر!
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/137388" target="_blank">📅 15:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137387">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
❗️
🔴
رامین رضاییان و پرسپولیس!!مدیران باشگاه پرسپولیس صریحا تکذیب کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/137387" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137386">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⏳
⏳
با پایان اردوی ۱۲ روزه تیم فوتبال پرسپولیس در ترکیه، بازیکنان این تیم امروز طبق برنامه در مرکز پزشکی ایفمارک حاضر می‌شوند تا تست‌های پزشکی پیش از آغاز رقابت‌های فصل جدید لیگ برتر را پشت سر بگذارند.
⏳
⏳
بازیکنان خارجی پرسپولیس هم که مرخصی 2 روزه داشتن امروز…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/137386" target="_blank">📅 14:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137385">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚡️
⚡️
مهدی تاج، رئیس فدراسیون فوتبال: تلاش‌ می‌کنیم تا فصل آینده بازی‌ها با تماشاگر برگزار شود/ تمام بازی‌های لیگ با VAR برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SorkhTimes/137385" target="_blank">📅 14:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137384">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
❗️
🔴
رامین رضاییان و پرسپولیس!!مدیران باشگاه پرسپولیس صریحا تکذیب کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/137384" target="_blank">📅 14:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137383">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⬇
⬇
⬇
با‌ارزش ترین تیم‌های ایرانی:  • پرسپولیس: ۱۶.۵۰ میلیون یورو • تراکتور: ۱۴.۳۰ میلیون یورو • استقلال: ۱۴ میلیون یورو • سپاهان: ۱۲.۸۵ میلیون یورو  • نساجی: ۷.۶۳ میلیون یورو •  خیبر: ۶.۳۰ میلیون یورو • گل‌گهر: ۵.۹۳ میلیون یورو • فولاد: ۵.۸۸ میلیون یورو • …</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/137383" target="_blank">📅 14:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137382">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
❗️
🔴
رامین رضاییان و پرسپولیس!!مدیران باشگاه پرسپولیس صریحا تکذیب کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/137382" target="_blank">📅 14:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137381">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
شاهرخ بیانی: رضاییان با پنجره بسته کلاس گذاشت.
🔹
قرارداد رضاییان با استقلال 100 میلیارد تومان بسته شده بود و بعد درخواست 200 میلیارد کرد. مگر فوتبال ایران چقدر می‌ارزد که به بازیکن 200 میلیارد تومان بدهند؟ اگر به بازیکنی چنین پولی بدهند، تیم بهم می‌ریزد.…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/137381" target="_blank">📅 14:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137380">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b74c6288d.mp4?token=JSqO0oROLRYLRCmCYiz-SVLYQ9gDIy3YsTatPyTyzlyQPxCw5Zdp1cYn3PlLm9uQ81oBcaSWGsNvmYK7vnqhPaAbGmykQbfLwKs7V4mkXlDTQp5a0Os_PmZWrd38B4AfMTj8_HqRa6-YjSk-EeoRYZTfHNJevAWWoAOUNiqbLxGQvY3Gvv_VU-P5kpXfCvhwVL7rFw1zNUEeDa8fKuPesi0kEVTnaoQcVQ2F6NETMkAUgO98IzvLxdZdcEMd29tn__WPVaS8PN0AcYWCvh3zevPYuDqr5V9ltfBCs_hj8XB-su0TktzhvPIoiJRU7k8Lp5iB5G62zLeulAxxdej3Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b74c6288d.mp4?token=JSqO0oROLRYLRCmCYiz-SVLYQ9gDIy3YsTatPyTyzlyQPxCw5Zdp1cYn3PlLm9uQ81oBcaSWGsNvmYK7vnqhPaAbGmykQbfLwKs7V4mkXlDTQp5a0Os_PmZWrd38B4AfMTj8_HqRa6-YjSk-EeoRYZTfHNJevAWWoAOUNiqbLxGQvY3Gvv_VU-P5kpXfCvhwVL7rFw1zNUEeDa8fKuPesi0kEVTnaoQcVQ2F6NETMkAUgO98IzvLxdZdcEMd29tn__WPVaS8PN0AcYWCvh3zevPYuDqr5V9ltfBCs_hj8XB-su0TktzhvPIoiJRU7k8Lp5iB5G62zLeulAxxdej3Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗞
🇮🇷
🤍
فوتبالی: قرارداد امیر قلعه‌نویی با تیم ملی به زودی و بعد جلسه هفته آینده تمدید میشه تنها شرطی که داره اینه باید ژنرال تو جلسه قول بده که در جام ملتهای آسیا ایران رو فینالیست کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/137380" target="_blank">📅 13:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137379">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT_ZBdn0K3Qc9YeCk7_Dp8G9luBjJ3_GqUJjEo8pynjzc091nvIhvF3Zabi_YBAEJZzu9AR2MxFHi06Gjy4lJMKrlddfC0zVyDRNbQrgMNeuORq7n8GbbsqbMkHpvwn0AhBAnuyIaNPE3YPawRqdyVsyikS_y3qslmHzqq5wZdez8fbjyVQWVBGpi_4l7nfpNsCushd34eimeVwqcl6NYKeRjo_f6nKjfXpFmVVAGjYZZwei2a24SWQXt8ox2hZj79rchwuF4-sUncrrHMQzxqWZworck96BiqFVnVqmg6fhwOdeBUp7QEw175-BFRpFGgZGUt0Mw43rd8mAA6CIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
🏅
مقایسه ارزش مهاجمان تیمهای پرسپولیس، استقلال و تراکتور؛
💵
پرسپولیس: علیپور 1.7 - سرگیف 1.2
💵
استقلال: سحرخیزان 900 - آزادی 300
💵
تراکتور: حسین‌زاده 2.2 - مغانلو 800
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/137379" target="_blank">📅 13:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137378">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
یحیی گلمحمدی با حضور در تمرینات دهوک عراق به شایعات حضورش در پرسپولیس پایان داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/137378" target="_blank">📅 13:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137377">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHoN9HXV6sctdN8lvk_dk0Iwktbn1XRSaz5P83Vx5ixfxqlW5NMmJi-40pNp-QBPs8k0PWYZoaJK0tiaACYOQzQiTWxxKEmX-NztVSjtcCbAKEg4lW6LjinJUStpbzxm7Q5O9EJTl9BfjJqjP1EP5zwIcR1MqUSo8xQnOaj3U0DZhLVYRJdOIjYDEWcW0IqaZf3ccQhOidy3nsQj_2ZFKZqtAt-7gKM_Dye0cqB9GKpIn6V8BjYVsR4a2BCSWXgfgS3MJyAxCxufYOWCZ5oYF9j_DM6GH74g862TlA2VLQ01bUpjvEUMsyopkIEDZmUGagRl2RGgtIkmg1Np1WSN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
اعضای تیم پرسپولیس با حضور در ایفمارک تست های پزشکی را انجام دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/137377" target="_blank">📅 13:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137376">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
شاهرخ بیانی: رضاییان با پنجره بسته کلاس گذاشت.
🔹
قرارداد رضاییان با استقلال 100 میلیارد تومان بسته شده بود و بعد درخواست 200 میلیارد کرد. مگر فوتبال ایران چقدر می‌ارزد که به بازیکن 200 میلیارد تومان بدهند؟ اگر به بازیکنی چنین پولی بدهند، تیم بهم می‌ریزد. بازیکنی در سطح رضاییان 20 میلیارد بگیرد، کل تیم بهم می‌ریزد. قرارداد رضاییان به اندازه کافی بالاست، حالا برای استقلال ناز می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/137376" target="_blank">📅 13:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137375">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
منهای ورزش
❌
بعد از هشت ماه نرفتن بچه ها به مدرسه
❌
فوری : مدارس امسال از مهر باز نمیشن!
❌
+ عمران عباسی، عضو کمیسیون آموزش مجلس:
❌
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
❌
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/137375" target="_blank">📅 13:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137374">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4HIfn763k8Q85W5ZtVXOKa8C25S2L8gDj3FyXAQysDhXL5gNDuqpBgO79IiMvVsIabuoRMbumy_yZxj_SwIEvPAOvfZy7lb_405dUHZ50m2SpyMGR9A0qE2QZYNhKBtc-XiXfSGCUl40nPOkkvSA_HvViK7Oa4AeSBbn2If7gf8Nb7pr_U4GtLbdG00h4u9TxckgKaw5_iKXtus3qpfmsmvw1svE7ShmG0gUHxvcno2H18A_kHnE-_-hPcVfBGf4ymGnnNaat2bTSUDd1p1lN3g2UUUffrSM_MC5r1--uuMQuavCnqZgNotr0Fmp0NEY1QbHUx2Ztd3SdQ-QxvDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
با اعلام باشگاه استقلال؛ رامین رضاییان رسما جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/137374" target="_blank">📅 12:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137373">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd-M-fEST1M_buV3rRnz-BMk3Gtr_nOI7R5bKd5vDnRc3lY1u-ZH0Tc090fQDdewd0350DY97fLPnh2OZ9gBITD77pL-zSM2SfKkif1M3bhdr-_MLeuUJG8DD0ysXqC9V_4zyjtznsQS3ij9ybwHaMRi_uHoCH7Qrhi5SBtu5IYh3DsHzXZT-lAzDHEQqJKGYtkGmpAxYUUV8jlnNel1s76EV2Ngmgii3IyBdFLx41G_a-plwq4odLFVDDlho8HybypHlr4vlsh8WVraiV1SoqCOfMJrhHw--PrM_uzuyDm4be208SzLOgXpyo3hyZcV-z-7iwsCYpdu6glS4_49nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Boca Juniors | بوکا جونیورز
🔵
🟦
اولین کانال و تنها رسانه فارسی بوکا جونیورز در تلگرام
🟦
#DaleBoca
🔵
🟡
🔵
🛡️
@Bocajuniors_Ir
⭐</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/137373" target="_blank">📅 12:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137372">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
رامین رضاییان به باشگاه پیغام داده دوس دارم برگردم./سپهرخرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/137372" target="_blank">📅 12:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137371">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه خانه‌ای که در اختیار بیفوما و گرا قرار داده بود را از آن‌ها پس گرفت و این دو بازیکن را به هتل فرستاد؛
🔻
اقدامی که گفته می‌شود با این هدف انجام شده تا شاید آن‌ها ناراضی شوند، قراردادشان را فسخ کنند و از تیم جدا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/137371" target="_blank">📅 11:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137370">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/137370" target="_blank">📅 11:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137369">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
امین کاظمیان در حالی اولین بازی خود با پیراهن گل‌گهر را تجربه می‌کند که شماره ۱۰ گل‌گهر را بر تن کرده که نام تیکدری بر پشت پیراهن اوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/137369" target="_blank">📅 11:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137368">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه خانه‌ای که در اختیار بیفوما و گرا قرار داده بود را از آن‌ها پس گرفت و این دو بازیکن را به هتل فرستاد؛
🔻
اقدامی که گفته می‌شود با این هدف انجام شده تا شاید آن‌ها ناراضی شوند، قراردادشان را فسخ کنند و از تیم جدا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/137368" target="_blank">📅 10:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137367">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
❌
رامین رضاییان با انتشار یک استوری تلویحا جدایی شو از استقلال اعلام کرد
🔹
نکته جالب اینه که خیلی کلی و راجب همه تیمایی که توش بوده حرف زده و اشاره به هوادارای یه تیم نکرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/137367" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/137366" target="_blank">📅 10:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✨
✨
✨
پیمان حدادی:
🔴
🔴
همه امید داریم که امسال بتونیم جبران مافات کنیم. در حال حاضر تنها تیمی هستیم خارج از ایران اردو برگزار کردیم. سعی داشتیم بهترین امکانات و بهترین بازیکنان را به تیم اضافه کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/137365" target="_blank">📅 10:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⏳
⏳
مهلت ۴۸ ساعته ادعایی ترامپ که برای تعویق حمله به ایران گذاشته شده بود ساعت ۳ بامداد امشب به وقت تهران به پایان می‌رسه و فعلا نه خبری از توافق قطعی منتشر شده و نه خبری از تمدید مهلت تعیین شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/137364" target="_blank">📅 09:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
رامین با آسانی هم به مشکل خورد
⚡️
رامین رضاییان و یاسر آسانی یکدیگر را در اینستاگرام آنفالو کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/137363" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0xmjuG7MstFl4njl8J22yHdhZwPebTSXJPwykNbiOM9VdVmneZeoaSusS0C0CSZI2n3kBUVwACrDPL6DwjOoJrC_sab2v3GpGIyrX14P5XAUdfizojE_z5lxuNuIenyzBk8_uryOvLYo9XhZLnhsDV8qGx6MG_cCj4z6LRkZUoCpL_sg8MF-FD8fP_itfJJaedmcXO3a0YSkOZAqnbsJHf-oi7iJUnudgVWiPzbCnxOboIc9nLpXZoGno8dUculBRAFJC99eft-BZi7ONy93Zz5dlPtn714ubacsZ_QKkF-95-5mKhGp0zeLcRM_iOWMLBdanZo5R4KVkDbCpeuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین با آسانی هم به مشکل خورد
⚡️
رامین رضاییان و یاسر آسانی یکدیگر را در اینستاگرام آنفالو کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/137362" target="_blank">📅 09:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
قدوسی : پرسپولیس بین قربانی و حسین‌نژاد قطعاً یکی را جذب میکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/137361" target="_blank">📅 09:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhiA-n_IhQI3rTwxzVidsFzv5he2dB8JbT6_E_5wITuFZj5zCS4kU_QOisMo2VoTxqfWQ2gp2vMuoNO2tAAKzgY9HkUs_MiKAomEXrFyuaplR7DUORP_pDl9TUWcj8Brg701NKMW2-YWo_eqI3WsSWO8HhfYrhkJTOGcs_dcTAz-J6O6XI-cANM8nyPa8clHFMcMekAFbAJ25zknKGv8YVxNCx3bbIhWa1iF6qowVXPNSwTb8dJCIAxocK1-vkTgSNJvXCtuzmSWUjEFgH_neUTE_iCgv2c2sZKnRd1QAg6Q4R5A6vBno3CAWSH6AKjtwdcOgjvWod8yKbI6usyvOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/137360" target="_blank">📅 09:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=RHChDCLVL7_ekUTHyCLBlp9gqwrqmFl1wEZ_H0OGlPKSMlUxI3JVgpUg6tl_cn7bBfzj-vw5zMBvi961HJION0ci6mr37rplv184Hrh7Q1AOztYAOG-M_i_5jP7e0g4ND6Jb-1RUuW8aj74uuLF9djfAR0ZuEziqXC_xYHFMsjAVKntO8eBe9gKNpAO8fjSEpLS7GQ0jF4x8MbLFoNL6R_la2ei327bpwsfNdCxDEK3mT5jLbbaqIjBTUcdYplXqQGJCXJMA-fxEXArvXmPuXKpqTCUGIyuES_7RZEnkzeJiW2tvTsTlYTYtXqmnk83YEzhizesPdacJgsS17ISEqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4988f1ce4f.mp4?token=RHChDCLVL7_ekUTHyCLBlp9gqwrqmFl1wEZ_H0OGlPKSMlUxI3JVgpUg6tl_cn7bBfzj-vw5zMBvi961HJION0ci6mr37rplv184Hrh7Q1AOztYAOG-M_i_5jP7e0g4ND6Jb-1RUuW8aj74uuLF9djfAR0ZuEziqXC_xYHFMsjAVKntO8eBe9gKNpAO8fjSEpLS7GQ0jF4x8MbLFoNL6R_la2ei327bpwsfNdCxDEK3mT5jLbbaqIjBTUcdYplXqQGJCXJMA-fxEXArvXmPuXKpqTCUGIyuES_7RZEnkzeJiW2tvTsTlYTYtXqmnk83YEzhizesPdacJgsS17ISEqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power x1000 فعال شد!
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ چرخش فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
🔹
پس از واریز، بونوس از طریق نوتیفیکیشن داخل حساب کاربری نمایش داده می‌شود و از همان بخش می‌توانید وارد بازی شوید؛ نیازی به جستجوی نام بازی نیست.
🔗
آدرس ورود به سایت
اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/137359" target="_blank">📅 01:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137358">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbc_kTbsG5j0fwV8PSoetfh9mDN2uu55LJ54ZIHV0zm0W2e2wI9xdDvQyNKfHtKL_j5ciXa4F4oQRPBZq9LdVwKee-fb5i0XUA2tGAABru6XOuh514WviUSRhe-x5m4_qiPZYqnaoM6Ne_cVGakVK_ehRSr6RPIgSJgAaZeVvRowLsOMLslfX7PZTFw1wjCzCD0_NXIp_ORm9bvvXEQam48FB383e4GiW_Ro2a6gW0JNL-kfaME0dHZkuRP9cwc8NV2UHMebkozLFI0bJHHRwACseF_PIbyuGDL2sgR20KpRqhfv7cj7y329vi5SUehLSuLJCLK2sWl0yag1XiC6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
هفته‌اول لیگ‌برتر خلیج فارس
✅
🔴
پرسپولیس
🆚
شمس‌آذر
🔴
🗓
تاریخ شنبه 24 مرداد
⏰
ساعت 19:30
🏟
میزبان ورزشگاه سردار آزادگان قروین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/137358" target="_blank">📅 01:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137357">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTh9-0vLCVKytJ5Rt8Qe0CQeqN9ZTP8-05DagupNOkqGN7FB8zxy3K8U64dIqVGWeiQQlXlI25aQiddJKSy0sDdKYp8v1nTJtc-mJHB4FjGoKSVXNA4Q22b6Kf9HlJ5sVfVhUGisHer-3PSE8wgPmHfWXWtS9G4JWwvW73cToZIG0nJ4w9Sm0bq8V9pOO1sKoUb3HozLNjMcc8sbW7JNpdYF924qJoD2ekxQnw2SUoLf8ECRcxsdFoSqE1obteL8KR6dgisM7n2cgpFub4002g9OnnQ7IJ3I22Dcj9cKNRg_lEsxPvuaBhShzzJAQAdQ07DXgLIT9VgB3kjJNUgKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت انگشتهای عجیب دیدا در مراسم تشییع بارزی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/137357" target="_blank">📅 01:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137356">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🔸
رویترز : فقط چند ساعت از فرصت ترامپ به ایران برای باز‌ کردن تنگه هرمز باقی مونده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/137356" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137355">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/137355" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137354">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⏳
⏳
⏳
⏳
روزنامه‌ همشهری هم نوشته پرسپولیس شانس خوبی برای جذب محمد قربانی داره و مذاکرات برای مبلغ رضایت‌ نامه ادامه داره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/137354" target="_blank">📅 00:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137353">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
❌
رقم شوکه‌کننده و عجیبی که فولادی‌ها روی هدف پرسپولیس گذاشتند!
❌
بازار نقل و انتقالات تابستانی برای ارتش سرخ با ارقام فضایی به بن‌بست رسیده است. بر اساس آخرین شنیده‌ها، قیمت درخواستی برای رضایت‌نامه ابوالفضل رزاق‌پور از مرز ۲۰۰ میلیارد تومان عبور کرده که…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137353" target="_blank">📅 00:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137352">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
ترامپ: در حال حاضر درباره بازگشایی کامل تنگه هرمز تا فردا با ایران صحبت می‌کنیم. این آخرین فرصت ایران برای دستیابی به توافقی خوب است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137352" target="_blank">📅 00:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137351">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
در حال حاضر مذاکرات برای جذب قربانی جدی‌تر است و با کاهش مبلغ رضایت‌نامه‌اش، شانس انتقالش بیشتر شده. درباره حسین‌نژاد هم فعلاً مذاکره رسمی تأیید نشده و پرسپولیس فقط شرایط او را بررسی کرده است.
🚨
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/137351" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137350">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
محمد قربانی به مدیران الوحده اعلام کرده است بین تیم های خواهانش اولویتش پرسپولیس است و میخواهد راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137350" target="_blank">📅 00:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137349">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
فووووووووووری
🚨
مهدی تارتار ظهر امروز جلسه ای با پیمان حدادی برگزار کرد و نام دنیل گرا و تیوی بیفوما را در لیست مازاد پرسپولیس قرار داد
🚨
قرار است مدیران باشگاه برای فسخ توافقی این دو بازیکن اقدام کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/137349" target="_blank">📅 00:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aESdXcKOPzGT_LIUXIMS2WX_BAN5AZ2sNGP9BJMJjvB_ftbH7nTdAOj2lW_W__8t0AA0CYpy7ZbFpc94IFt_fBenimQjuCVFzxG6QvM4SdzENj4GJ7m96k9i-cn2jveVVTYaYLcOMqyimGjkR7W-NWywXbUOd3ciEcErrL3O9aOxyrujYUpfdWDUI9S-COIyonQOK6x5saffRF1ZiUMkNmVWTfROh23DT32AJ1d_kNT4lULfkw2vekY71O7C0lxSoafih36n6qyPr2bDjd46m5cOTtEhd205oXw-dpWEGu7tkj-Yl59_FroO2ZDOqfDjFZDcBciU19YgIded1c0JKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
💣
🇹🇷
یاغیز سابونچوغلو: ترابزون اسپور ترکیه با صلاح با قرادادی 2 ساله به توافق رسید
😕
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137348" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
دو آفر باشگاه الوحده برای دریافت رضایت نامه محمد قربانی
🚨
پرداخت 700 هزار دلار  دو قسط 350 هزار دلاری طی دو ماه
🚨
تخفیف برای پرداخت نقد  600 هزار دلار
🔹
مبلغ رضایت نامه اولیه 2 میلیون دلار اعلام شده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137347" target="_blank">📅 00:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
همشهری آنلاین:
🚨
مذاکرات پرسپولیس با الوحده برای جذب محمد قربانی و پرداخت مبلغ رضایت‌نامه این بازیکن ادامه داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137346" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
قدوسی : پرسپولیس بین قربانی و حسین‌نژاد قطعاً یکی را جذب میکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137345" target="_blank">📅 23:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U91LyRVUDO1xsyzwYFhIIPtPnhsRzPgMMjzLaUO8s_f1arFIWdTHRmY8PoTMpz2H2H0hetkZ_YwLT-ghK3w3M1G2zeZfBwmMwJKBIM3pgIFL2xYCX8w73TNsTJG_Zu4H1YO6vijR16VDE0b8NYIC50CIezYL0mC1Xc2WEDDn4ifZsznIHQK2ybXpar52dmVKL9yXzx-wAWEzyjiYpKeHAza9uQqSRx_FKhpmdYcd3f7i3PqajOA9q4r7ytUF0J1E22tfz3iTXiPiYuCpfFZOGpIR6lowfmLXJow2-N062V6P8iUSHZefGGRns83AACX7dOFc801pIpv5Rh0QWzPEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قدوسی : پرسپولیس بین قربانی و حسین‌نژاد قطعاً یکی را جذب میکند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137344" target="_blank">📅 22:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137343" target="_blank">📅 22:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
ورزش سه: مهدی تارتار از روند نقل و انتقالات پرسپولیس راضی نیست و مدیران باشگاه پرسپولیس دارن لیست خرید شو روز به روز کوچیک تر میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137342" target="_blank">📅 22:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
مهدی تارتار سرمربی پرسپولیس: از مدیریت باشگاه خواستم که سه بازیکن جدید جذب کنه تا تیم برای‌ فصل‌ جدید تکمیل شود. در پست‌های دفاع میانی، دفاع چپ، هافبک تهاجمی بازیکن جدید میخواهیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137341" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137340">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
✔️
محمد جواد حسین نژاد امروز هم تو بازی تیمش بازی نکرد و نیمکت نشین بود
🔴
گفته میشه حسین نژاد دیگه تو دینامو نمیمونه و قطعا در این پنجره از این تیم جدا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137340" target="_blank">📅 22:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137339">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
رضایتنامه حسین نژاد از 6 میلیون یورو به 1 میلیون و 500 هزار یورو کاهش پیدا کرده، حسین‌نژاد جز استقلال و پرسپولیس از ریو آوه پرتغال هم پیشنهاد جدی دارد‌ ولی اطرافیان حسین‌نژاد می‌گویند اولویت  وی همچنان ادامه مسیر در فوتبال اروپا میباشد
✍
ورزش سه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137339" target="_blank">📅 21:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس با وجود باکیچ ، خدابنده لو و پویا پورعلی گفته نیازی به جذب هافبک شماره 10 یا شماره 8 نداره و بدین ترتیب حضور محمد جواد حسین نژاد در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137338" target="_blank">📅 20:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137337">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚫️
⚫️
⚫️
سرمربی باشگاه پرسپولیس به الن هالیلوویچ هافبک کروات پاسخ منفی داد و حضور وی منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137337" target="_blank">📅 20:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
❌
فوری از ورزش‌سه:
⬆
مذاکرات مخفیانه استقلال با رامین به نتیجه رسید و در صورت حل آخرین جزئیات مورد اختلاف رامین به استقلال برمیگرده و در ایران میمونه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137336" target="_blank">📅 20:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoG5ovxBeAFtL61YSYmByL0jlBuQ94wVdgDAD7zzjpJgHUSq9U9lJ8v1skTrjFI5zBHJ1aqESGQButgVhBueMnVf_1wntFs0CIRlIHgYKyjgvFh8R3clYTCR8o4WQgz-RNWz44WzG10S8br_fZcXU68YHRleg2bGFit6GP5V7PDwHn0prRsCswX8Qa7qurC-m2m1cZ0CiyHv6Vk-1mErUlqdGuQN_HTw0duItlchwcJhvQ9feny3Icj86qLtpmZultt4BUkrhf-dMKPtgNNx9avWPLFbOMDApgDs4ys39CnRABADkLsxKdPUvQdlRVWTBiEjbT6HYu0B0wBv_ro_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
⚡️
پس از شارژ حساب کاربری و فعال شدن فری‌اسپین‌ خود، وارد بخش بونوس‌ها شوید و ازین فرصت چرخش رایگان نهایت استفاده رو ببر!
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137335" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
فوووری؛ باشگاه فجر سپاسی شیراز بازی مقابل پرسپولیس در ۱۶ مرداد انصراف داد.
❌
❌
احتمالا نساجی جایگزین این تیم برای بازی دوستانه ‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137334" target="_blank">📅 19:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idsq2uoBQgVI2mD1JZYmezgZBNmrWOFL1ou2pSinNexkYtD_HgdTjOmabIBnedMBRzl8wvWQFXApFj4blJpAOQBT2DEHUuh-hxvW8F_8irJohwK9J4rpe-4J4nID7gD27ekGpoXLsgfYtTQ-Eiw21S1XEvKmwVmG1j_wXNoMJeUMx45_VKV4VUMDrf17CAHg3Ct-oo5URZrcCbpUYOhjH9o_Yk5R-4WIJg1mk2-g4gfXJwmfO72MbzAsL2vt1muAEDE_UUqsdV8wQ8N3HTaD8XnAD0qWSJZmbjKeI5nJ8pV9L3zWPt5UaWQqI_mxOy8JyE4PFfWiYH_bStveL7Tn_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
#
رسمی
؛ علی نعمتی مدافع‌ سابق پرسپولیس و فولاد با عقد قراردادی دو ساله به تیم لوسیل، قهرمان لیگ یک قطر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137333" target="_blank">📅 19:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
❌
فولاد قیمت رضایت‌نامه رزاق‌پور را برای پرسپولیس ۲۰۰ میلیارد تومان اعلام کرد!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137332" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyOv-1LgLu98hH_409NvsGBWDqUp5o1j5R8x4A8wSc5TFdqCThrXYwux9w7x78j4LRmni3_kFFqwurGp36FoVulZOr1E15MqLbtqhUiuwpiT6G9B1oKe4S_IgQM-BSbmlOs90J5ho322eIyCXGuZgc6StfI9YG1LbG21iEuKMAU9rWcKftAun_D8XnSqt_FMuULqw8xHAaGmW1aWcYickz3r5gj8QBwUXvc1A7gH3oMnPIVPE1iLs370PNcPAweouzoX0C4rKEIyEeo936CiWoXF4FMBKOQDhzedzo-qq7ymbB-7HNo-dTrcbNMCyj2TiNABkhT-xA0fVbvdLU_RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تارتار نه از جلالی و نه از عیدی راضی نیست و دفاع چپ و راست میخواد
☹️
☹️
☹️
///فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137331" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
15 روز تا اولین بازی پرسپولیس ورژن تارتار در لیگ برتر مونده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137330" target="_blank">📅 18:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137329">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
🔴
🔴
🔴
مهدی تارتار تأکید ویژه‌ای روی جذب محمد قربانی دارد و نام این بازیکن را در صدر فهرست نفرات مدنظر خود قرار داده
🔄
🔄
باشگاه پرسپولیس همچنان در حال چانه زنی برای کم کردن مبلغ رضایتنامه است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137329" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137328">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137328" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137327">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
فووووووووووووری
🗣
باشگاه عصر دیروز به جمع بندی رسید که باید برای جذب قربانی اقدام کنه
👀
مذاکره با قربانی و ایجنتش که رابطه خوبی با مدیران الوحده دارد شروع شده و امروز با جدیت بیشتر پیگیری شده است.
🎤
حسین قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/137327" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137326">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
محمد انصاری که در تیم جوانان ایران به عنوان یکی از دستیاران حسین عبدی فعالیت می‌کرد هم اکنون یکی از گزینه‌های جانشینی او در این تیم هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137326" target="_blank">📅 17:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137325">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔄
🔄
🔄
پرسپولیس به فولاد پیشنهاد بیفوما + ۸۰ میلیارد برای رزاق‌پور رو داده که مطهری گفته اگه یکی از بین علیپور، سرگیف یا شهرابادی رو بدید میزارم جدا بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137325" target="_blank">📅 17:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137324">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gusKX8SB60Vs_gbTASm5B3WQIImRtLuliasnZ-YXsxyWyDVZZ-WIQdhhLau2vJNIUoGuT3ncWJum1bqZij9jug3zhSh5vvzLv4KN-27uhshfC14XLIZZIq3_fGLyu0uTGXSEQDF4WOdY10gFtLMX22if1i7VEaxqCzFmchGuGKsOOUlSDWj3vvnjZ5p_j_b93ThonwxRs-5qRSOxAth6p-BCRLkVYv9Gg7uRXNxzxE1WU2jbA-BK45v7mOM9lPjr_gDzb5miMq3xWaXYccnbIlFLTOApRDw0ENirHK9gsPvKNvSU2oozWwdbE7j0WN4uf_1RjZlcBD0oZMqKmsVZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
پرسپولیس تنها تیم در جمع تمام تیم‌های لیگ برتر بود که اردوی خارج کشور داشت و بیش از ۸ خرید جدید هم به صورت رسمی ثبت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137324" target="_blank">📅 16:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137323">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
❌
❌
کسری طاهری: وظیفه‌ی من بازی کردن برای نساجیه و درباره بقیه مسائل باید مدیریت پاسخگو باشه/الان زمان صحبت کردن درباره‌ی اون داستانا نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137323" target="_blank">📅 16:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137322">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
فووووری 360: رضاییان از کیسه جدا شد
🚨
🚨
با توجه به حضور صالح حردانی و سامان تورانیان، سهراب بختیاری زاده با برگشت رضاییان مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137322" target="_blank">📅 15:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137321">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔄
🔄
🔄
پرسپولیس به فولاد پیشنهاد بیفوما + ۸۰ میلیارد برای رزاق‌پور رو داده که مطهری گفته اگه یکی از بین علیپور، سرگیف یا شهرابادی رو بدید میزارم جدا بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137321" target="_blank">📅 15:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137320">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
با اعلام ایجنت رامین رضاییان، این بازیکن از استقلال جدا شد
🚬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137320" target="_blank">📅 15:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137319">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🗣
🗣
🗣
عبدالله ویسی سرمربی ذوب آهن: با یک بازیکن ( امید عالیشاه ) وارد مذاکره شدیم برای یک فصل از ما 130 میلیارد خواست و من جلوی این انتقال رو گرفتم. ما تیم جوان هستیم و نمی‌توانیم چنین هزینه های بکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137319" target="_blank">📅 15:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137318">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
❌
طبق شنیده‌ها: سید مهدی رحمتی سرمربی گل گهر سیرجان موافقت خود را با فروش امیر جعفری مدافع چپ 24 ساله این باشگاه به‌پرسپولیس اعلام‌کرده‌است. رحمتی در این پست قنبری شاگرد سابق خود در خیبر رو میخواهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137318" target="_blank">📅 14:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137317">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
❌
ترامپ: در حال حاضر درباره بازگشایی کامل تنگه هرمز تا فردا با ایران صحبت می‌کنیم. این آخرین فرصت ایران برای دستیابی به توافقی خوب است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137317" target="_blank">📅 14:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137316">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r800nnudDsTXc24B2JmTsJpfTLpgkUnU7p5wTMKEGkNj9jFsTGLJTZlhEJuHaJfZL2PyOB5c_kv-yamW8k0BihAtdvZcf-PtUyOMrfdfR17nsKNF11_xx4ncFU6wDy1R24IrC9nirAv5tZziuCNFttBKdhKUxAgCbPL6WkBYx-UiINpmtZ1tXEivVe2l3NJjLtjBhTvK6HcgekWcR2THKeN1w0aI34yet00aeLQlNPAXi3WJoxneMohzR4wuRDPrcal3AEnvVRhbjsAVCK7rPV5AZwuaEjyfEg45Tzem0vuPdCilIT3Ybe6Mns3nDfHD0I_ymOtazIsCUPhJ2W-4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد برای صعود؛ شبی سرنوشت‌ساز در لیگ قهرمانان اروپا
⚽️
دیدارهای امشب مرحله مقدماتی لیگ قهرمانان اروپا با رقابت نزدیک مدعیان برای رسیدن به پلی‌آف دنبال می‌شود. تیم‌ها در تلاش‌اند با کسب نتیجه‌ای مطلوب، شانس خود را برای حضور در مرحله اصلی افزایش دهند و همین موضوع می‌تواند بازی‌هایی تاکتیکی و پرتنش را رقم بزند. انتظار می‌رود جزئیات کوچک و عملکرد ستاره‌ها، نقش تعیین‌کننده‌ای در سرنوشت این مسابقات داشته باشد.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137316" target="_blank">📅 14:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137315">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
10 باشگاه لیگ برتری صبح امروز با ارسال نامه ای به سازمان لیگ خواهان تعویق 10 روزه لیگ شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137315" target="_blank">📅 14:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137314">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
🔴
🔴
ایمن حسین مهاجم ۳۰ ساله تیم ملی عراق، در انتقالی آزاد با قراردادی یکساله به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137314" target="_blank">📅 12:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137313">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
آخرین وضعیت ایمن حسین ستاره تیم ملی عراق در ترانسفر مارکت که درحال‌حاضر بازیکن آزاد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137313" target="_blank">📅 12:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137312">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
تندیسی زیبا که باشگاه پرسپولیس برای امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک ساخته بود و‌ این بازیکنان برای دریافت این تندیس حضور پیدا نکردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137312" target="_blank">📅 12:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137311">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند این فصل سرباز هست./ ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137311" target="_blank">📅 12:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137310">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX7m54mfhzutW5iSX6hvUFYzpnCP_2cNhjGMEEB5hjP7W9X9wZhwqzGtnmj4FamnFhuO_NDRbIguNLjjXxlXLXXB46DwfDYveY8nKhY0P0r8AzKqzOz7vdqrgWpnRI0mywQnI0hKvEQZkIXdUyZ3YiL_IBYj0WAttKrDGNFdAHXTme2NDREPu7t-_Q6QfxWKZ8McDKJMA2maQ_fdsCSDP4k9zdk4VZfbayLn1zxjpNTKVy7vS1Yz4qhy7D5TVmui7lq_EDem1YR_a3NZtCH9mwskZe_3loZRXOdgcO_-t0rtjZT5VQV9HLvf5HDuOGdrcjUtOa2CnNdzQgj86BpwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تندیسی زیبا که باشگاه پرسپولیس برای امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک ساخته بود و‌ این بازیکنان برای دریافت این تندیس حضور پیدا نکردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137310" target="_blank">📅 11:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137309">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚠️
⚠️
⚠️
مدیرعامل باشگاه گل گهر سیرجان :
⚠️
⚠️
امیر جعفری مدافع چپ مدنظر باشگاه پرسپولیس قرار دارد اما تا این ثانیه به صورت رسمی با ما مکاتبات نشده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137309" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
✔️
گفته میشه که تارتار بعد چند سال بالاخره جاسوس تمرینات پرسپولیس و پیدا کرده و بدون رودروایسی کنارش گذاشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137308" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووری
📊
📊
خبرگزاری RB اسپورت روسیه : مذاکرات پرسپولیس و دیناموماخاچ قلعه برای حسین نژاد جدی شده است و امکان توافق طرفین بالاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137307" target="_blank">📅 10:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❤️
📸
تصاویری از شادی بعد از گل علیرضا همائیفرد پس از باز کردن دروازه حریف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137306" target="_blank">📅 08:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
🔻
🔻
ترکیب پرسپولیس دوباره لو رفت؛ تارتار هم دنبال جاسوس می‌گردد
➡️
➡️
➡️
فرهیختگان: سرخپوشان روز گذشته به مصاف تیم پیرامیدز مصر رفتند. اما جدا از مسائل فنی، موردی که ذهن مهدی تارتار و دستیارانش را به خود مشغول کرده است، بحث لو رفتن ترکیب تیمش یک روز قبل از مسابقه…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137305" target="_blank">📅 08:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74903f0977.mp4?token=l-Uyx1-4ACh_-FlmfrSW1uJnaOvsO1Q7XcghDaaiy19kzQGD9Y9_Dzi_V8ZuSkKo256daFUQNbxl8XfO_NbrUoQwKfbjT3KfgvwBvV2gd34ueT3JLP6ct3s7COgeuEQAfYtXKRcAIkxKCIr6akDbguXbXz_kfoEwF7TGl1BrdYAT6ch3sBpD98-V3ApEqTQEKWndbPC00nATAVqXeS1TqdieDdvNc4lN86361mZcwfITXtkDHB5tWwM54QnTb8WkZ-ajoao6blgtjF3G9-dpy-FYDR4MQTWvjcvU9VD4CEJTkA_lJLxEVjIUUATUd1uKHKWdvT4NdXoDnC3tKzj6Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74903f0977.mp4?token=l-Uyx1-4ACh_-FlmfrSW1uJnaOvsO1Q7XcghDaaiy19kzQGD9Y9_Dzi_V8ZuSkKo256daFUQNbxl8XfO_NbrUoQwKfbjT3KfgvwBvV2gd34ueT3JLP6ct3s7COgeuEQAfYtXKRcAIkxKCIr6akDbguXbXz_kfoEwF7TGl1BrdYAT6ch3sBpD98-V3ApEqTQEKWndbPC00nATAVqXeS1TqdieDdvNc4lN86361mZcwfITXtkDHB5tWwM54QnTb8WkZ-ajoao6blgtjF3G9-dpy-FYDR4MQTWvjcvU9VD4CEJTkA_lJLxEVjIUUATUd1uKHKWdvT4NdXoDnC3tKzj6Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
فرا رسیدن اربعین حسینی بر شما عزیزان تسلیت باد
🏴
⚡️
الهی به حرمت این روز همگی حاجت روا  و عاقبت بخیر باشید
🙏
الهی آمین
🙏
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137304" target="_blank">📅 08:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3AB3sQfAkOv4x_6K0ous2qvlDQFVAdHRBtaGQa-cKgxWh7BhLZ5MtBS1PgFMcx-OwlbvKUnwg5hrQnza3PUk3SScjsQ4GZDgG6DdkNAtkP8nePCLWZ922MEBAxhjdGqyrvsLA6impWQRbh56KhbQwZlaawUlp5U-BmEns0ChtbjE1gdf3F7v38UKrNMOibkPVOPGkhQS-M0O79IEkM_WzMyUktyR1CXpBTDdR0tIulldeuOVjjO-9JAoXVUlZjzXMGK3ZsMOL0tL8sRxQQH3xq7LH_8RUFfxL_mPUOiC9Avfr_0cwzfTrJp7JYqCwNINPrd8dDjWDuV65KqBLJg-uKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3AB3sQfAkOv4x_6K0ous2qvlDQFVAdHRBtaGQa-cKgxWh7BhLZ5MtBS1PgFMcx-OwlbvKUnwg5hrQnza3PUk3SScjsQ4GZDgG6DdkNAtkP8nePCLWZ922MEBAxhjdGqyrvsLA6impWQRbh56KhbQwZlaawUlp5U-BmEns0ChtbjE1gdf3F7v38UKrNMOibkPVOPGkhQS-M0O79IEkM_WzMyUktyR1CXpBTDdR0tIulldeuOVjjO-9JAoXVUlZjzXMGK3ZsMOL0tL8sRxQQH3xq7LH_8RUFfxL_mPUOiC9Avfr_0cwzfTrJp7JYqCwNINPrd8dDjWDuV65KqBLJg-uKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137303" target="_blank">📅 01:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس با وجود باکیچ ، خدابنده لو و پویا پورعلی گفته نیازی به جذب هافبک شماره 10 یا شماره 8 نداره و بدین ترتیب حضور محمد جواد حسین نژاد در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/SorkhTimes/137302" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
گزارش تصویری / پایان اردوی سرخ‌پوشان در ترکیه!
❤️
تصاویر منتخب از آخرین جلسه تمرینی  ارتش سرخ در اردوی آماده‌سازی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/SorkhTimes/137301" target="_blank">📅 00:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUEwEhXYrbKcFfJ5weZWNdAqngwsCyYonPl3PllB4DGQM1b2SASwSD3OhmFn9OCW7E9LzIjHSUpWSZ8HaLtknflwT2cHz8D8kYpfHQKomdVO6y6ggB3hv33lvIycSejUSXdpc4SesqAQyxQKZRNlQ9hOrA0xB1vAyZwKbSJIRCe5zwYdocCR12K4kKdlymP-O5gwY52MydsAlMfna8wfPj0D2RRvTWWdn-YpHLsVyyBknKoggOhQLAUllfq80N6fq4h7ZhgQdaZITnzSwz6ysKxjIhGlZpffc5WVuJKBAe4I_f1aGIx6p573C_wcKkRyGyYx85T6AnXF-6YGXM-DKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
با تصمیم مدیریت باشگاه پرسپولیس زمین شماره ۲ مجموعه ورزشی درفشی‌فر به نام شهید ماکان نصیری نامگذاری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/SorkhTimes/137300" target="_blank">📅 00:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137299">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCxH5tnOtq27gQ8HulGX0Plh_BSTX7xI0gwKDVBHR3i8WduOtP2fC5hWLLYE4LBjG908kOKA_nqGyy29R5G-1x1Jvd348bESZQp_tKv6_4u2STcCnylO-1yH07Bx3QEp3Jt6R6Ej-j1l__996nYRNFiuy7PsFvep_4qUzl3nFoqf7XHOjeCopOY0HLYpyvlbJVY0K3Q2nSkXTwVYxum0IEXNxXFYuEdgTfgdLk6r0gYdJzXebFe699c0jH3ElCTc_RBGmqZ7ddFyBLdtkc8BepkZhWmycNAOCNqD21l6P8wJ4LMkVeigAQNx947wI2lcbstYJRjXhlrTCkYEkibu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
با اعلام ایجنت رامین رضاییان، این بازیکن از استقلال جدا شد
🚬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/SorkhTimes/137299" target="_blank">📅 23:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
احتمال تعویق یک هفته‌ای لیگ برتر به دلیل درخواست برخی باشگاه‌ها افزایش یافته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/SorkhTimes/137298" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
❌
خب ظاهرا پیشنهاد استقلال بهتر شد و پستای استقلال برگشت
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/SorkhTimes/137297" target="_blank">📅 23:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137296">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚠️
⚠️
امید عالیشاه به ذوب‌آهن پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/SorkhTimes/137296" target="_blank">📅 23:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137295">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNzq9WUK2kIMW8CGku3Z0dWptSp-4njcO01HEXFIwsrmiBMaBg5agoU20BNDcLfIKEPE_rxNm5Ooz9R2Dbetzum9mJ5kDa9Hn8FalQvD9yARtVeSloDxY3XUt-MqtjCNWRBS6hnfvbl2dTDA8l2sSAnSEUVlGCzcJmBAmNQmuukLfbaFEzloXnoAuqivgaG6Ncnsrw66hSQnbu67aBHsHoIG0Zjjt4DD04m2AyHBFYvs1ae3RR7q-r82IIIESoI8PWRzG5XYsAzzx4UL0GewwolnXKmCqQ0QPUXXCAqV0P6aE6EZHhoPqmyHyDBh4KxLzxandKQOHG8vbzNbS9V81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
احتمال تعویق یک هفته‌ای لیگ برتر به دلیل درخواست برخی باشگاه‌ها افزایش یافته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/SorkhTimes/137295" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137294">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
فووووووووووووری
🗣
باشگاه عصر دیروز به جمع بندی رسید که باید برای جذب قربانی اقدام کنه
👀
مذاکره با قربانی و ایجنتش که رابطه خوبی با مدیران الوحده دارد شروع شده و امروز با جدیت بیشتر پیگیری شده است.
🎤
حسین قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/137294" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137293">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
✔️
شرایط ایری از نظر حقوقی متفاوت با کسری طاهری است.
✔️
اینکه پرسپولیس همچنان دنبال کسری هم هست یا خیر و اینکه نساجی حاضر به انتقال فقط ایری می شود یا خیر نمی دانیم
✔️
تارتار بشدت دنبال جذب مدافع میانی و چپ است و ظاهرا گزینه ای جز ایری و رزاق پور ندارد.…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137293" target="_blank">📅 23:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137291">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
فوری/ ترامپ: به درخواست ایران و کشورهای منطقه، حمله رو برای فراهم شدن زمینه توافق، متوقف کردم. ما کاملا آماده حمله بودیم اما حالا مذاکره می‌کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/137291" target="_blank">📅 21:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137290">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
قرمزآنلاین: دانیال ایری، رزاق‌پور و محمد قربانی سه خرید پایانی پرسپولیس
🚨
🚨
باشگاه همچنان برای جذب ایری و رزاق‌پور تلاش می‌کند، هرچند فولاد فعلاً با جدایی رزاق‌پور مخالفت کرده است. همچنین با درخواست دوباره تارتار، مذاکرات برای جذب محمد قربانی پس از کاهش…</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/137290" target="_blank">📅 21:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137289">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a103c22f7.mp4?token=YEFTg6W-I-uCuW5b6oLqG0kvUyfw-kUti6491ypKGUNq_JhIXc-nIlBvCKYaZ-K76y7Vr4oEe6SCqCXdD2KyEdGbfx7EJTP12BJOZ4WjaMehVtzlc66QC2wmh3G7NevHQDTCJdMUr4OhbbZ3c-LRzc8GRFH_BO4Wd0nkK-G16Z9r2ue1nfnZ8QoElCchD7JV8A8EvL1jrdMJsTBK87TvRdwl5rO9TQZqDp7BV9f5GzpPvB2j5hr-jT5LIj9oYNYcllWfSw7-2sx_8qvJabqsBtXVsjcAo4DcHDl7mICrNZ19d6eSDFFYgVT3qcDcwqbtFhIPnrSdjZyx06NDasRVkRCfC01P-KbOw3IfLFW__Jq8DcbN63DXmv7XD0cP4_4bY72EXPqYoYGY5KslHro0MN2tK965FUq0g9ftiRTRHEf9r3SsAi8-wv92qI6yGMDMG0TB-wBqD30omvudcifhtdOl1-deNQzzlbb4bDWRdHXAIV23H_C0BCj-05mpwmxARFM6xIMgR4AnLLGBk4nfsRECWCBLLW0ejGYPYguf6IuL3tnHFRe9SPZVFoSBPOce6Kd9wu34cRKxQ0YuTdtQRgJadiueNu-owtzRfqUwocUXgqFClYHEJ7UrZv4LrPLx-kZa9hRrKI62sLXDUKyPIyDhVRZjAlaESxGYsvqOAHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a103c22f7.mp4?token=YEFTg6W-I-uCuW5b6oLqG0kvUyfw-kUti6491ypKGUNq_JhIXc-nIlBvCKYaZ-K76y7Vr4oEe6SCqCXdD2KyEdGbfx7EJTP12BJOZ4WjaMehVtzlc66QC2wmh3G7NevHQDTCJdMUr4OhbbZ3c-LRzc8GRFH_BO4Wd0nkK-G16Z9r2ue1nfnZ8QoElCchD7JV8A8EvL1jrdMJsTBK87TvRdwl5rO9TQZqDp7BV9f5GzpPvB2j5hr-jT5LIj9oYNYcllWfSw7-2sx_8qvJabqsBtXVsjcAo4DcHDl7mICrNZ19d6eSDFFYgVT3qcDcwqbtFhIPnrSdjZyx06NDasRVkRCfC01P-KbOw3IfLFW__Jq8DcbN63DXmv7XD0cP4_4bY72EXPqYoYGY5KslHro0MN2tK965FUq0g9ftiRTRHEf9r3SsAi8-wv92qI6yGMDMG0TB-wBqD30omvudcifhtdOl1-deNQzzlbb4bDWRdHXAIV23H_C0BCj-05mpwmxARFM6xIMgR4AnLLGBk4nfsRECWCBLLW0ejGYPYguf6IuL3tnHFRe9SPZVFoSBPOce6Kd9wu34cRKxQ0YuTdtQRgJadiueNu-owtzRfqUwocUXgqFClYHEJ7UrZv4LrPLx-kZa9hRrKI62sLXDUKyPIyDhVRZjAlaESxGYsvqOAHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حمایت تمام قد حسین خبیری از حدادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137289" target="_blank">📅 21:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137288">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHAQK5v9v1mnWT30IY_uyHx45frKEsNKqnx0tSAKkwnkqM_mKw8hOQWEf6y9INiP-0GyLKICbVg0B7XjM8tDfIUABdN2IiZpo12W_8xDS09vscfS7ev5WR7n1hFG-XqIqrKMvHvypSCDPgo--JYjkwzi2N2qspxnbeX4lqHaLIG5RbqYIl0Kh0a65_gS-XliT0S2fE1yO_OWbPA7XXKM6565jbnz8zVLnrBg8XWSra_pHmSlNV3P60d27WeNgJqpKY_uDEv4snQDzvdNBBIAgOj8xYrgswxynLaR4husBxrEuNHUfG5MSOmTAK9RTuZf9TilaWrr4tMN8qy9fP6JpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
فریتز در مسیر قهرمانی؛ جودار به دنبال شگفتی در فینال!
🎾
Rafael Jodar -
🎾
Taylor Fritz
🎾
تیلور فریتز با اتکا به سرویس‌های قدرتمند، ضربات فورهند سنگین و تجربه بیشتر در دیدارهای بزرگ، شانس اصلی کسب عنوان قهرمانی محسوب می‌شود. در مقابل، رافائل جودار با نمایش‌های کم‌اشتباه و روحیه جنگندگی خود نشان داده که توانایی به چالش کشیدن هر حریفی را دارد. اگر جودار بتواند ریتم بازی را برهم بزند و رالی‌ها را طولانی کند، این فینال می‌تواند بسیار نزدیک‌تر از حد انتظار دنبال شود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137288" target="_blank">📅 20:54 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
