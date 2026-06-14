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
<img src="https://cdn4.telesco.pe/file/b1MYv6YLwpoFWyMIZLBnPD24CLM0L6ugBUnV5nML0E86Oj-FgEFl9ymInWdlKKR_-Ycew9KbdKaPahTliDaGpJIe6LLmmefVconyty7BS-0pH7yPzcanNNue2J0Q3J0TV26bho4OdromKBv4oOyT37Wub6YqrwuQ2p3YngvXGKzr6MmZJAyTzKvpXL7oA8d2Yc858W67ZA5slhWZyAADBLbz0zQPapc9RQgdiFmsFTHgT_J99AVYN9XIGk2-SQdtXEzfcpoijZ25y2pE4OqQyH48kPg9hHorqA6YjJnpQHHg7zS2KlVK4tsxMYNVXYoNC28JVXyCUk7YirZzJF5wnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.55M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 15:50:01</div>
<hr>

<div class="tg-post" id="msg-659301">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c79a541a.mp4?token=ckYgrfiPymZluT8uSSgFRibJGFpyI_3CKVkZT3cfUvMb7f25KPxI12xCj_QpraRa-2sgMlZKnOkxmGL1Ni_8rNvNvkX0tOx40LTbEOidqOHs_I7guBcMR00T7gpCARnPi7e4BwNQ8_kz1AGmli0NMhV78_LNBjcTJqkG9b19EgBAn22HOnhyzypEOUaVKqoqApe6FZaeeGrl9WNXGkfVoTZszQ4KvHMoSkJRfoCt05wpZjHTuXk9A4iUpR5cY086ZdWIG-f-N9ySc0bmPt4Qer51GwJiPOLt1DFIbrJtbeMHBk9VPKarZKCq33CTjPmHS6IV1-CM3bzvTRhwjpbUgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c79a541a.mp4?token=ckYgrfiPymZluT8uSSgFRibJGFpyI_3CKVkZT3cfUvMb7f25KPxI12xCj_QpraRa-2sgMlZKnOkxmGL1Ni_8rNvNvkX0tOx40LTbEOidqOHs_I7guBcMR00T7gpCARnPi7e4BwNQ8_kz1AGmli0NMhV78_LNBjcTJqkG9b19EgBAn22HOnhyzypEOUaVKqoqApe6FZaeeGrl9WNXGkfVoTZszQ4KvHMoSkJRfoCt05wpZjHTuXk9A4iUpR5cY086ZdWIG-f-N9ySc0bmPt4Qer51GwJiPOLt1DFIbrJtbeMHBk9VPKarZKCq33CTjPmHS6IV1-CM3bzvTRhwjpbUgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم درگیری‌ها میان معترضان و پلیس در کشمیر پاکستان
🔹
به گفته منابع خبری، درگیری میان معترضان و پلیس در کشمیر تحت کنترل پاکستان طی روزهای اخیر ادامه داشته و شماری کشته و زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/659301" target="_blank">📅 15:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659300">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu8Yki_WOHMSgQQdJpq2ufvbmX2z0YsZWMO_qapkrTd-bb2lfW-lMe35gxIyvUwErbqjUgt38Ilu0xYr1XG9PAy_upSdfCJFliOUypgZliiXR9SJJL_NEc2WhJn21LqoY9AYZrWbqhXzNSgT5wEhW-hpQZBviEfyNg0TM0zgx68TytI7oHqKNDTsdb2_rFZjFdurLeAsmHHsWZ4lllagMPPTRDNNlDqMPayPkDylxquIGDWCP79qN8367gzcgSuKxaDNeiyIHdMufJnNlswi2ZxezhsK_zZrCrqOXRvLKBuq95gQJbeQlKnYM-nM2W0G6pndw071TcX6y59TSZnp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رسانه‌ اماراتی: امارات ۳ میلیارد دلار به ایران داد تا حمله نکند!
بیزینس‌رکوردر:
🔹
دو منبع منطقه‌ای گفتند که امارات موافقت کرده که در مجموع ۱۰ میلیارد دلار آزاد کند که بیش از ۳ میلیارد دلار آن قبلاً تحویل داده شده است.
🔹
دو منبع دیگر که از این توافق مطلع بودند، کل وجوه مورد نیاز را ۲۰ میلیارد دلار اعلام کردند و افزودند که این اقدام در ازای توقف حملات ایران به امارات مورد توافق قرار گرفته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/659300" target="_blank">📅 15:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659299">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbRo5iHqO5hE35xbXQrQS12717Q78RZ8W5Bug78FgGIY4I8a0nPGSU5D2kUkcQZdux-T6HrQtLdyzyzaTtxMhk4jimHrs9ztoXQXOwf1uobg-v5HO58samk5icjxmOPxWSu24T3lpOWnHsbPaPCPY1u3CvDRQAod6pUgmwAW8Io4foXgk1616JafX3H4obnR4CIXDJjDgS1RsIZ5et9_mTdGlwnSdcWe41iGxSRGRWCmOhuQiUkNTfv2PFuoQCvrXqR34WQXmGQdZOxHDJNN6ZZ-BYQcUeiNN4LL73TkAcP5DrlANsuhY83nfnF_hVl8-uHOjtHlVdooeg0i_UtmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کم‌خوابی به خاطر تماشای مسابقات جام جهانی طبیعی است، اما هواداران کدام کشور بیش از همه دچار اختلال در خواب می‌شوند؟
🔹
ایران در رتبه یازدهم.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/659299" target="_blank">📅 15:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659298">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDdRkZ6_XSpM84jvYSmGCvg9YYG56Tg87Uyoi3ixSFri0zFAzHNEl1YfHOdQWUEpxehsoI9r6N7Yid7KM-cHvGDR3DAdifp73eNl-9tlyAIOW_oo1wuoQUw1Kk-8zTJ9raZrfxQ38EZ8yOUutchwa9U2pihYFqjNQzaXehH0mRKO2jkXeJ_fCgp7iReCk7BZ-14O8dDTkoxmNdtx3f6a93RUaD4dyeOXXi8CN-Mzk8H2bn9ibvxujNPPiqocHLs448Yg95sh9j4x1DrMcCFKR1kLYaibcn5Vwy6ZDQsv5Ntzuvi3xti5pGwW_VeE0H_GXTySrpKZkfFKRtKYggeruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعم نوشابه‌ات فرق نکرده؟ شاید این آخرین جرعه تو باشه
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/659298" target="_blank">📅 15:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659297">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566ae393cf.mp4?token=JHRzsgQHmdGwRFgTHFRzNxByefMKT-iHBp8hRRlU6ydJ5z4n-EHwpd4lTIYWy_oEnHcJy5LL3TOsGfF-XmvK12IZtc-CHtRy25A99DhTn0ywRrwHnNlpUPLK9N3JlLByijb9KpAkOsqfked6wHcdRwJrfYgxpSG7KOHIq1g3GBC0hgId8XZlxfUlg0qcJAwJFB-2Tcu61W8BkFC7sQ6jLmU90uFimcNVGbWt7608KMW9afD4VVp5dQV9ELkYVxpkMtU71zURyeH9XYPDqR2HKGG_Mu_PCxSxLCU8MfwWoJ2pX495_0lJomigUbPNqQCCLHZHwBQJOeD8DoGXNhOhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566ae393cf.mp4?token=JHRzsgQHmdGwRFgTHFRzNxByefMKT-iHBp8hRRlU6ydJ5z4n-EHwpd4lTIYWy_oEnHcJy5LL3TOsGfF-XmvK12IZtc-CHtRy25A99DhTn0ywRrwHnNlpUPLK9N3JlLByijb9KpAkOsqfked6wHcdRwJrfYgxpSG7KOHIq1g3GBC0hgId8XZlxfUlg0qcJAwJFB-2Tcu61W8BkFC7sQ6jLmU90uFimcNVGbWt7608KMW9afD4VVp5dQV9ELkYVxpkMtU71zURyeH9XYPDqR2HKGG_Mu_PCxSxLCU8MfwWoJ2pX495_0lJomigUbPNqQCCLHZHwBQJOeD8DoGXNhOhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه سقوط هواپیمای ترابری نیروی هوایی هند
🔹
تمام پنج نفر حاضر در هواپیما کشته شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/659297" target="_blank">📅 15:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtTeYuXlw0N3bzlgGbC8wuW1S3ORUCEm7jqnLK9ToY3yRpdhRd8WtO3U55nY55lZK4ThPPxHlpIO4f9cwwtYXU55CIzEzopXZEUKbjCgHfkrM3KPz8mF3C1V577U3JHN2sk4uPzURJZ37lDJD-r6lVNvTW2s10HbSK-K5UVqvJPuzhfMEu-fU3eCwiK2Jm71j-jJkpcDrWCcs9r5F2LFRUPQvK2CgrASKR5xHMZ-XlB84RifORhO9UpY-Vh3oOmcNk6uGxaj2Yj0PhwKsF9wHmTrtEYl0XykdXc5MA_KzEEhmsg8iiOeTM9c9pZ_7Yj7_RgnWjsMtA5ys5ZWiINcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: مگر می‌شود موضوعی به این مهمی، تحت نظارت دقیق رهبر انقلاب نباشد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659296" target="_blank">📅 15:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
زیاده‌گویی کانال ۱۲ اسرائیل به نقل از یک مقام امنیتی: این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد
🔹
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد.…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659295" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659294">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آماده باش رژیم صهیونیستی درپی رد کردن خط قرمز ایران  رسانه‌های اسرائیلی:
🔹
رژیم صهیونسیتی از ترس واکنش ایران به بمباران ضاحیه بیروت و موشک باران سرزمین‌های اشغالی توسط ایران، به همه تشکیلات و نهادهای خود آماده باش داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/659294" target="_blank">📅 15:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659293">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHw1ytwNt1KhwnSNONtLcdAfuZK2lWVSnzHoA6Nb2sXr4-Pd21ZaLFGqMTpW7QT4W-sriwTdXab996RbuaDnS4TJvbIHjY6CgXiT52wYUbvYB-EtVjC6VX95-ul-jAQyGgrruPUtGYNDGlVv2837RvFhZz7rUMf5WQwo0hd4YHKxHQjtleoS73HdzIxRaL3PUG1b2XS8hjUV9QEMlbomm65z_wqMt2zScAjaWZe9IRYX2ZwPhoqKS4yF4FbbS304wsG8HZN52vcZWGQmiJXgTDNeLKtg69gGpSyeLckvniKR04PoRBSCCtmPmg6xkPkzx5jUMxe1EshqvHl9HSoweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جاسوسی برای ایران با ۷۴۰ دلار!/ رسوایی امنیتی در اسرائیل
ادعای تایمز اسرائیل:
🔹
یک شهروند ۴۴ ساله ساکن حیفا به اتهام جاسوسی برای ایران بازداشت شده است.
🔹
«رنان بن حایم اوهانا» در دوران تنش‌های مستقیم ایران و اسرائیل، اطلاعاتی از جمله نقاط ضعف بازرسی بنادر، مسیرهای احتمالی قاچاق سلاح و تصاویر اسکله نیروی دریایی آمریکا و سواحل حیفا را در اختیار یک مأمور ایرانی قرار داده است. در ازای این اقدامات تنها ۲۵۰۰ شِکِل (حدود ۷۴۰ دلار) و از طریق ارز دیجیتال دریافت کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/659293" target="_blank">📅 15:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSHunX07nqYZpTxnx2Hx3ofa0ntDgttemLrsUIgZj7cax0XKQZtWAokzZKlIR8pbxLvsSSv_Fg_xYJdTDap-t3BMs3QQAeNXgofUpFMg39Byb-Ua9q19pJWpyJzJu5MNA5gyEjfpVPfydwMhVL6OD9jaU0HOFLHezEFZtMhPL-gs6bNiLsFEm7J3HBDjM1EjmrK_MlWNabY-GSoRzDCWLXQAF1MCgDPpWrEHqab4B7EahyhUoS_ip_YnhErMyQdYNXvHA5Q2foi4exLt6wfVf2bOvU3frea-LtqfFpOHX2-msi9oiKOPXkKwPYy5EX11ZA-q7RgxC3STLD3fpnCVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
غول لبنیاتی شستا در راه بورس؛ دوشنبه منتظر «تادیکو» باشید!
🔹
خبر فوری: بورس تهران بالاخره زمان عرضه اولیه شرکت «سرمایه‌گذاری کشت و دام صنایع لبنی تأمین» با نماد
#تادیکو
را اعلام کرد.
📍
جزئیات مهمی که باید بدانید:
✅
تاریخ عرضه: دوشنبه ۲۵ خرداد ۱۴۰۵
✅
سهمیه هر کد: حداکثر ۲,۵۰۰ سهم
✅
نقدینگی مورد نیاز: حدود ۱ میلیون و ۶۰۰ هزار تومان (سقف قیمت)
✅
روش عرضه: ثبت سفارش (بوک بیلدینگ)
💡
چرا تادیکو مهم است؟
صنعتی استراتژیک است‌و سود آوری بالا و ریسک کمی دارد
در شرایط بحرانی کمترین آسیب را می بیند و تاب آوری بالایی دارد. نواوری و دانش بنیان از ارکان اصلی تادیکو است
🔔
یک قدم تا خرید:
زمان دقیق ثبت سفارش روز دوشنبه اطلاع‌رسانی خواهد شد. برای اینکه از ساعت دقیق و استراتژی خرید (سفارش‌گذاری بهینه) جا نمانید، حتماً به سایت
tahdico.ir
مراجعه کنید</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659292" target="_blank">📅 15:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659291">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868f7e306b.mp4?token=ppK0W_AeS7FLr_xySbaXDfYvZNBgo60PVP-yGEXCs4aq7rF_s0-A_8rj0ETefc6fP_DgpsxMRvE2c5CzEekZ9dEULl31_ECj_aanpOsQXto3Cq0Bmv1YKiGEANDHzcEdy-PLHTeF8NOSm37wT5X6K_9Zr_FWrktyNFX__EIphBYaXHfFN8ZlqqPdIeV5IebjSywCk1L6hnznvieVic7Ps4KOkMx6fGCnISf6_JchJvup3_Iq197UHnTKUIWkPIGLPMjGL0ZKJkcs66uLi9ZA4E2B0E2E_r9-HTX6SkLgQa3HJPrilDvedyxpFA9Y1Q-sqaGD__65Aehd4K9COqrqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868f7e306b.mp4?token=ppK0W_AeS7FLr_xySbaXDfYvZNBgo60PVP-yGEXCs4aq7rF_s0-A_8rj0ETefc6fP_DgpsxMRvE2c5CzEekZ9dEULl31_ECj_aanpOsQXto3Cq0Bmv1YKiGEANDHzcEdy-PLHTeF8NOSm37wT5X6K_9Zr_FWrktyNFX__EIphBYaXHfFN8ZlqqPdIeV5IebjSywCk1L6hnznvieVic7Ps4KOkMx6fGCnISf6_JchJvup3_Iq197UHnTKUIWkPIGLPMjGL0ZKJkcs66uLi9ZA4E2B0E2E_r9-HTX6SkLgQa3HJPrilDvedyxpFA9Y1Q-sqaGD__65Aehd4K9COqrqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم حضرت ابوالفضل (ع) در آستانه حلول ماه محرم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659291" target="_blank">📅 15:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e11a7f2f.mp4?token=I8dorTJGax3Oh2xkexlJDwEs8bjAZxwqXCwPKjAJdM4LpW1I_9PO6eFeU_CvMWbLCcuaw-hL3kkbi-KXr_0L_g20YqN11eWd1qniL8AY7jYuIV2E4oz_1SoXLeceOKNLvPdPJs012JeMDzTcxnfqDlbuhc3BJnsMTMIX2SUmdhh_Ll4Nc2_XST4c-XS_XaUJPMtbycNsdoX-6IDtSLTtu53GxPtdKu2ORe-B-2oTiZ7BaONgpXQJr-PPnAvtXnxcKeva3YFpj6BcD0bCjRWuMYxJIFNMylCNwlrP83W7fCu0-ADumYuZxL_6vZ0ZhRyI1wN9m_D9oOFq0j7DUGIuPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e11a7f2f.mp4?token=I8dorTJGax3Oh2xkexlJDwEs8bjAZxwqXCwPKjAJdM4LpW1I_9PO6eFeU_CvMWbLCcuaw-hL3kkbi-KXr_0L_g20YqN11eWd1qniL8AY7jYuIV2E4oz_1SoXLeceOKNLvPdPJs012JeMDzTcxnfqDlbuhc3BJnsMTMIX2SUmdhh_Ll4Nc2_XST4c-XS_XaUJPMtbycNsdoX-6IDtSLTtu53GxPtdKu2ORe-B-2oTiZ7BaONgpXQJr-PPnAvtXnxcKeva3YFpj6BcD0bCjRWuMYxJIFNMylCNwlrP83W7fCu0-ADumYuZxL_6vZ0ZhRyI1wN9m_D9oOFq0j7DUGIuPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حواشی حضور ایران در جام‌جهانی پیش از آغاز اولین مسابقه
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659290" target="_blank">📅 15:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615ef428a8.mp4?token=lNdQ0yqzMN_WTscnN7XwzdbCWdiGw26-2h2HqboLdlHJzDUCCHak7hE2MsCMCUbuE-PNIHlK1cjK8TH0TzPbpkdyC2KTH_UUg-ZxrJW6tuRS3IjuOUR18h2refvMTaxOPRoTaMfkHnEnoIAeOCK0z4XjLs7W-tCuAsl3wkxCzwY9DzxdZ0RJrmkcrAASDqRVrmc7Pxg5AvQIpQUKYxW2fJdFPyH5NiiIYtO_WriN545kJYkTocfoMXKXbqtqA4Nru17viSMvSByqLiz8lRA5YG-V879Nb6G09f0MV06BVK8JIa-Rf68Lyv7K74Cbly0nI1f-V_rgc0SJ1njHosDHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615ef428a8.mp4?token=lNdQ0yqzMN_WTscnN7XwzdbCWdiGw26-2h2HqboLdlHJzDUCCHak7hE2MsCMCUbuE-PNIHlK1cjK8TH0TzPbpkdyC2KTH_UUg-ZxrJW6tuRS3IjuOUR18h2refvMTaxOPRoTaMfkHnEnoIAeOCK0z4XjLs7W-tCuAsl3wkxCzwY9DzxdZ0RJrmkcrAASDqRVrmc7Pxg5AvQIpQUKYxW2fJdFPyH5NiiIYtO_WriN545kJYkTocfoMXKXbqtqA4Nru17viSMvSByqLiz8lRA5YG-V879Nb6G09f0MV06BVK8JIa-Rf68Lyv7K74Cbly0nI1f-V_rgc0SJ1njHosDHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی بسیار تماشایی از طبیعت فوق‌العاده دماوند
#ایران_زیبا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659289" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0a7191a0.mp4?token=NF4ZNDyX72fUE1V6RCdcTBnVGLyAO0kHX1XrJTj2DSpTmHUmVeTVJFNBZ9rz4jQHx4AcdWZqxNErPdWYxPByCeln5kh3i2qnpUIM1sbs-m9qo-k58gMQKdSPHag8HJLYKVPxZfcYgpvOcZGFCpV0-GskR6Pm-yOjaPgk41wmDLpPfm1zwQ32k-6VSpJvaRc-rvC6DK3HmXalxChB2V0fOrbDuapt-JQ7pMHXF8grIcf2_b7d_uOObEWcET-t5Yx3js04b61p0n01XVAhQH1Dfy4h-C3NRYxNQH3bJHkJ34XcymVoEZ5hTZqB30kUD6Xc5qBgLyjeOAGUCW07H8qKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0a7191a0.mp4?token=NF4ZNDyX72fUE1V6RCdcTBnVGLyAO0kHX1XrJTj2DSpTmHUmVeTVJFNBZ9rz4jQHx4AcdWZqxNErPdWYxPByCeln5kh3i2qnpUIM1sbs-m9qo-k58gMQKdSPHag8HJLYKVPxZfcYgpvOcZGFCpV0-GskR6Pm-yOjaPgk41wmDLpPfm1zwQ32k-6VSpJvaRc-rvC6DK3HmXalxChB2V0fOrbDuapt-JQ7pMHXF8grIcf2_b7d_uOObEWcET-t5Yx3js04b61p0n01XVAhQH1Dfy4h-C3NRYxNQH3bJHkJ34XcymVoEZ5hTZqB30kUD6Xc5qBgLyjeOAGUCW07H8qKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات  وزارت اطلاعات:
🔹
یک هستهٔ ۴ نفره گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکه اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659288" target="_blank">📅 15:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659287">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 معمولا بازی ‌های تیم ملی در جام جهانی را چگونه دنبال می کنید؟</h4>
<ul>
<li>✓ پخش زنده تلویزیون و شبکه‌های داخلی</li>
<li>✓ اینترنت، گوشی و پلتفرم‌های آنلاین</li>
<li>✓ پیگیری نتایج بعد از مسابقه</li>
<li>✓ خیلی پیگیر فوتبال نیستم</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659287" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
آماده باش رژیم صهیونیستی درپی رد کردن خط قرمز ایران
رسانه‌های اسرائیلی:
🔹
رژیم صهیونسیتی از ترس واکنش ایران به بمباران ضاحیه بیروت و موشک باران سرزمین‌های اشغالی توسط ایران، به همه تشکیلات و نهادهای خود آماده باش داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659286" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvbkCKDip8bDpHn3Zkd82UyGLuikwxE-J-5mTUI3n-EoNg1C6QBQg-0YlJqgLLMZkESleczD0NFaer2IY6b-3oLI_oSVsWB9nRJ6vZwbKI0qgrkO-C4PdZPo8wSwOw2bOdbF0Oj7kDHD5zuCNsX7MUgCOiVKRuI7VhQP4Vo7ZlE55BBWuJkplRsly_SNr3XLuyNzwJBEBokUNXfiCrs6V0hMG9gUn24y9rKAVftBksF9TllaQgLUJ8d_jrgdCUlcrDSf5xM5mylOCrTOXn8fVlLgjzIYJNYymMwOqky8bzb0a5irQ_yv-kkq44kmAjMZRTl2rOPs_U6gCCOrjP9OLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستخط منتشر نشدهٔ رهبر شهید انقلاب در ابتدای قرآنی که ثواب تلاوت آن را به شهدای جنگ ۱۲ روزه هدیه کردند
🔹
بسم الله الرّحمن الرّحیم
شروع در تلاوت هدیه به ارواح طیبۀ سرداران و دانشمندان شهید در جنگ اخیر و دیگر شهیدان عزیز این واقعه در سحر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659285" target="_blank">📅 14:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به ضاحیهُ تاکنون یک شهید و ۴ زخمی بر جای گذاشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659284" target="_blank">📅 14:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659283">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
عراقچی: امنیت منطقه نمی‌تواند بر پایه نادیده گرفتن ایران شکل بگیرد
وزیر خارجه:
🔹
آنچه تصویر واقعی قدرت ایران را به جهان نشان داد، تنها توان نظامی نبود، بلکه انسجام ملی، ایستادگی ملت و حضور آگاهانه مردم در صحنه بود؛ سرمایه‌ای که امروز پشتوانه اصلی اقتدار ایران در عرصه دیپلماسی محسوب می‌شود.
🔹
تجربه جنگ اخیر نشان داد که امنیت منطقه نمی‌تواند بر پایه حذف یا نادیده گرفتن ایران شکل بگیرد. کشورهای منطقه به تدریج به این واقعیت رسیده‌اند که امنیت پایدار، توسعه اقتصادی و ثبات منطقه‌ای تنها در سایه همکاری، تفاهم و در نظر گرفتن منافع مشترک همه کشورهای منطقه از جمله جمهوری اسلامی ایران امکان‌پذیر است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659283" target="_blank">📅 14:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7piSX4-Fr0yPDL0xtGE_IGIBMBF52HETqJxdaF1QQH4o9dxCy6qXsB7QLj9XQAoUiN_RE_nXKnrpaEu3p0uitVH_CRfyMiYib7L2RZDL5Ak3Lrw0_lGCA9mVBF6_7pgPUgMhUOs7zjr1mZZNVra9Fb4NFPvWq3N9Iz32hrjN6utnVkAzoAT3RNoqBkKu2PpSMj3dFQgoxtEnDA8D_g_x7EZzGGgCKNtQIGIeUASNhdwSVPRH57oF_bRoKV_COZM6z1ZVZT2CBFqvH-8jk6yaqHv9CqoYrlyCYPDjCq0PTttMo5zctUEObvaijgmYosEGwA77DBYFU0HqP7lTyJdEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال ایران برای دیدار با نیوزیلند
🔹
تیم ملی فوتبال ایران در اولین بازی خود در جام جهانی ۲۰۲۶ صبح سه شنبه ۲۶ خرداد و از ساعت ۰۴:۳۰ به وقت تهران رو در روی تیم ملی فوتبال نیوزیلند قرار می گیرد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659282" target="_blank">📅 14:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📷
سلبریتی آمریکایی پرچم ایران را به اهتزار درآورد
🔹
«جکسون هینکل» اینفلوئنسر معروف آمریکایی امروز در تمرین تیم ملی فوتبال ایران در تیخوانا، مکزیک حضور پیدا کرد و حمایت خود را از شاگردان قلعه‌نویی در جام جهانی اعلام کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659281" target="_blank">📅 14:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e288b78.mp4?token=Vx4bJ3LTe_lHj7rnY-13tL3sq3hQEHd8Kq7XnQpZGD-Lk0kKQiZ4I6FQJI65aQeptjgmUaRt1h2otdEHEyhjyVhvSjBYKLfi93HyJUzcGg6fWcjxZ0gRKhQt7kFmUSFmcmgeza6Yg13SnSB4VAMpUKB05OluY8eqqdpVGf_k8LekCw5UaycZUJYGxTQ41ywrGGVwqdLS36Zg8bbMXocAv-F45VyuXlto7dyAZsANMIHwQz7nI9Cw-mNX4mTHDEZcJPrLK3ae--RGgi-v22109Vsoxy_weFNOdVvb5-OFDjCbj8HUG2abJs3v72AWgFAVfhGa__XNIRLs5oAUHlBRbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e288b78.mp4?token=Vx4bJ3LTe_lHj7rnY-13tL3sq3hQEHd8Kq7XnQpZGD-Lk0kKQiZ4I6FQJI65aQeptjgmUaRt1h2otdEHEyhjyVhvSjBYKLfi93HyJUzcGg6fWcjxZ0gRKhQt7kFmUSFmcmgeza6Yg13SnSB4VAMpUKB05OluY8eqqdpVGf_k8LekCw5UaycZUJYGxTQ41ywrGGVwqdLS36Zg8bbMXocAv-F45VyuXlto7dyAZsANMIHwQz7nI9Cw-mNX4mTHDEZcJPrLK3ae--RGgi-v22109Vsoxy_weFNOdVvb5-OFDjCbj8HUG2abJs3v72AWgFAVfhGa__XNIRLs5oAUHlBRbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگۀ هرمز تا اطلاع بعدی همچنان مسدود است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659280" target="_blank">📅 14:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659279">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
تصاویر منتشرشده توسط ارتش رژیم صهیونیستی از لحظهٔ حمله به ضاحیهٔ بیروت
🔹
کانال ۱۲ رژیم صهیونیستی مدعی شد که اسرائیل یک مقر حزب الله را در ضاحیه هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659279" target="_blank">📅 14:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659278">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۶۵۳ اصابت در تهران و آسیب به بیش از ۵۰ هزار واحد مسکونی در دوران جنگ
علی نصیری، رییس سازمان پیشگیری و مدیریت بحران شهر تهران در
#گفتگو
با خبرفوری:
🔹
در جریان جنگ، تهران ۶۵۳ مورد اصابت را تجربه کرده که ۳ مورد آن مربوط به حملات بامداد پنجشنبه به پایگاه‌های نظامی بوده و خسارت مردمی نداشته است.
🔹
۵۰ هزار و ۸۴۹ واحد مسکونی آسیب دیده‌اند که از این تعداد، ۳۹ هزار و ۴۷۲ واحد خسارت جزئی، ۸ هزار و ۹۲۰ واحد خسارت متوسط، ۴۵۶ واحد نیازمند مقاوم‌سازی و ۲ هزار و یک واحد نیازمند تخریب و نوسازی هستند. روند تعیین تکلیف و بازسازی بخش عمده این واحدها در حال انجام است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659278" target="_blank">📅 14:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659277">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به صور لبنان
🔹
منابع محلی از حمله هوایی رژیم صهیونیستی به منطقه «الحوش» در شهر صور در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659277" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659276">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c876708ff0.mp4?token=bDcyoMXB0zPmf270Q3OBfW9tKrpNXoRbvxvb2Sf14zaQb14URiByvhL55BwBkvkc-Sy9Q23QKd5yHfWV5LcABg9vVNqe4S1QtYnI7rzYKUnWYGbmvQ0S879uMs56DnbGK5noTQl7-LJj7sNgrrAd-7kvTHqtnS-lfH10FujlKuxetM348UqdSX5KzQkn24HrymCtv_PgNMyywehdgPVy_JZ_S_uC4sEh2USpiO9vqXhuaNE3msmoVsv9NaE5j9LJ_ZxLT_qKblGeAkR074QGfBn27M6YkhFQMlRWmeUI-aueKW_eLwY_QAJCI6lIj8aD19EdLr24IC8UYYowfJwmDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c876708ff0.mp4?token=bDcyoMXB0zPmf270Q3OBfW9tKrpNXoRbvxvb2Sf14zaQb14URiByvhL55BwBkvkc-Sy9Q23QKd5yHfWV5LcABg9vVNqe4S1QtYnI7rzYKUnWYGbmvQ0S879uMs56DnbGK5noTQl7-LJj7sNgrrAd-7kvTHqtnS-lfH10FujlKuxetM348UqdSX5KzQkn24HrymCtv_PgNMyywehdgPVy_JZ_S_uC4sEh2USpiO9vqXhuaNE3msmoVsv9NaE5j9LJ_ZxLT_qKblGeAkR074QGfBn27M6YkhFQMlRWmeUI-aueKW_eLwY_QAJCI6lIj8aD19EdLr24IC8UYYowfJwmDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سخنگوی ارتش اسرائیل: زیرساخت‌های حزب‌الله در ضاحیه بیروت را هدف قرار داده‌ایم
🔹
حمله دشمن صهیونیستی به ساختمانی مسکونی در محله الغبیری انجام شد و تا کنون تعداد بالایی زخمی به مراکز درمانی منتقل شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659276" target="_blank">📅 14:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659275">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
حریری، رئیس اتاق بازرگانی مشترک ایران و چین: در سال ۱۴۰۴، ۱۸ میلیارد دلار واردات از چین داشتیم
🔹
پنل‌های خورشیدی و لوازم جانبی ساخت نیروگاه خورشیدی در صدر کالاهای وارداتی از چین بوده و خودرو به صورت قطعات منفصله یا ساخته شده و لوازم مربوط به ساخت ابزار الکتریکی از دیگر اقلام عمده واردات رسمی از چین هستند.
🔹
اقلام مصرفی هم در صدر اقلامی قرار دارند که از چین قاچاق می‌شوند./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/659275" target="_blank">📅 14:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659274">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از مقام ایرانی:  بر اساس یادداشت تفاهم، آمریکا ۲۵ میلیارد دلار از دارایی‌های ایران را از طریق انتقال مستقیم نقدی، همکاری میان کشور‌های منطقه و خطوط اعتباری مالی، آزاد می‌کند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659274" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659273">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خدمات کارتی بانک ملی تا ساعاتی دیگر وصل می‌شود
شرکت خدمات انفورماتیک:
🔹
ارائه خدمات حضوری در شعب بانک ملی از ساعتی قبل آغاز شده و خدمات کارتی این بانک نیز تا ساعاتی دیگر برقرار می‌شود. بر اساس این گزارش، تا ساعت ۱۳ امروز بیش از ۷.۶ میلیون تراکنش در بانک صادرات با موفقیت بالای ۹۹ درصد و حدود ۳.۴ میلیون تراکنش در بانک تجارت با موفقیت ۹۸ درصد انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659273" target="_blank">📅 14:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659272">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
حمله به ساختمان ۵ طبقه در ضاحیه جنوبی بیروت
🔹
شبکه خبری المیادین از حمله هوایی رژیم اشغالگر صهیونیستی به یک ساختمان پنج طبقه در ضاحیه جنوبی بیروت خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659272" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659271">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c7423cdc.mp4?token=pwOfdY9vlw9fUQw5_EK29QPUIMiYm65d-XtZhUpnbILVvp6O3A6_JJ9kXPL4Koi9pUmXGQ_mLoDuAp2clIgcZpBYqVULtiBTD_OFUkGK3YcG0azKRNi84rqh8IvOinSU9mWYP9JX5DDdXLOxJ_NQ45XSIkAZz8EX4FYkoq3EO0YWZxg_uMx1LlWzTWJPuMNxL1cgJzdQeTPY9266Kh061kZB3SqiyGCIeZlnFGQgW8fv47kTucgBopIra3s7NclyDCekLBcgHspwo1hcF2__XFMntFdQz_sT9LpUZwMiHz5vtUDrrRmYp0ZDuUPJidV7uHrqZxemZqE1pQLs94G8gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c7423cdc.mp4?token=pwOfdY9vlw9fUQw5_EK29QPUIMiYm65d-XtZhUpnbILVvp6O3A6_JJ9kXPL4Koi9pUmXGQ_mLoDuAp2clIgcZpBYqVULtiBTD_OFUkGK3YcG0azKRNi84rqh8IvOinSU9mWYP9JX5DDdXLOxJ_NQ45XSIkAZz8EX4FYkoq3EO0YWZxg_uMx1LlWzTWJPuMNxL1cgJzdQeTPY9266Kh061kZB3SqiyGCIeZlnFGQgW8fv47kTucgBopIra3s7NclyDCekLBcgHspwo1hcF2__XFMntFdQz_sT9LpUZwMiHz5vtUDrrRmYp0ZDuUPJidV7uHrqZxemZqE1pQLs94G8gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به ساختمان ۵ طبقه در ضاحیه جنوبی بیروت
🔹
شبکه خبری المیادین از حمله هوایی رژیم اشغالگر صهیونیستی به یک ساختمان پنج طبقه در ضاحیه جنوبی بیروت خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659271" target="_blank">📅 14:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659267">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzFa17A6K6Sd1w4IZ9Qi982ndi7TisdE2mjLK3m9f_XjuwHikOXz_B8_rlArArOimYSPaMLzUfHlJ8KutaTAetieaOF73exERCkIwDMrSCmVGfFbl7_fgqHZwnnPvLCxpk_22PElR-5grh3gI-lM9bDyfvmKBZFb6UeYRUaoa_AT2wNT9se4ZWI8yIjGEI47NviolDM3J1tJGWNWfm-qkwjSUZmk5G6bgC2Dw0bTkQXl9jE63v53nbGb-R2s-iAv8_lFfZGBgsjQ1Zurlrh5iz7CsBYnMVNoRzLg8CxgBKGjEh8dehLMInO6z3hJba1YgExaYsIAv-jczpqInbkCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/is5wgJds4Q-iWoE-6Rh6ote5XZ-nqtRMbp-S8K94gTzoqpHZFWmkjmm4qFAWG-J0x32RTYFktBv-9Y2c5gL_RrdcUhOlfPRxFPWYDQF0wO24ATO13vnzD--jg5VzxPYBn6TTtI-AHH39zZcxORCMzVRLfirSCSbVfZT8nEeQ2Nu4fXG2Stal74jEL9ZTO3ryUE6kLY9E5wC4ghNVg0D5IE_T0h-Rbc_hD7-YiQ3IkybrpB4gRNvbyf6NuHiODh-OK6cwzVc5QJcp4YuoOgV0MX7W_I7Q5GzudOgBoyE7YwsHji3gpJDIefd0OEaNPhSuJVx_C9_AKDBZ_vx9zu8HyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p70OCOwsTlp18Opa2G7M4U2X-B8NCh0OblopvAf15DWSAoi_2wxssVaY0907Bcd8mqQTWOtzWG4LjXx8TiVUjag24ScZuC-jjnTbnl39EVdfs57HE91XJyDcst_gDF4eGYwmzWzwnUk62hsje2gTm6xdlmjWFUGYgLJGn3IR7VqifCUyu6voO68akFQA0Lkh-MHKn59bRAZ6pqt4mDJFsWGc_s9lDIqfW1WzrfmwdpEWgXxjPn1lOHjY_P-cJ5TTOZHVng46UOvmXumD2Lqd6QOc1x9kPqjzv7o9VulEBYOP_rko64TAW2uchZxZLGBvqqVhboNi_Czw9pYS2kytSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdN13eIrFwOr8VL2ipdsufHtkgfE_HKfKqdMduqR2g4l1vZMElaEJ4vXkmzNga-lYpeuS-k5iQO0mluZbfXcxmJvTwMdSltszA0p-xQzHXrWuHV2hI3c9sB8mNApbstI45Mp65KfQs7HtlJoWb47tJrBnhFHgpf8GcEEGb37-1RE0Dhglhnv14K08-oXc3UQ18aSUp3JjRcArda9uA37RjeOzd-cC2DpWglanDAUmv2Dxbz-t_CQycwHCG8HV7udfeam9WnkHdu1gvIpPEAHEW-RAug2BykZV5iCD-D2Tz0jA6TLZtbUpGmXsEn2xYc1AOUfa46YvziMqdEwzwOyYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از محل مورد هدف قرار گرفته توسط رژیم صهیونسیتی در ضاحیه جنوبی بیروت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659267" target="_blank">📅 14:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659266">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae8cb26f2.mp4?token=nAJpFp32j2t7KU6hfhX7t_C7Cg6YnT52xNNkpI-uC-OnVuz9UeqAxcD6GSSloeK2Xzzpv48qRfab1jr0woctyxmYKw9-6LTsIfsIq-IdmpQSYTIsrs3GGVK6bXnev3Vb-UWzOb3W6kWzMFHx4ZqB4v08XlRq8HCvucnz_qJ72PKSIKti8IrDMtYTvHnNdPv6KuOehKAOFYl_Do1WwKwgU_pMJ9yhpuO4OlY7Q_FXIb0Qy1EYfRh-g1gozT-8qk6UBdV9rLnELK_GkPvjggjWhWgolQY6_BTSMLADmrjICJVuMBMsCbKx6Fpuok1ODFxFw_zBQSZ9Y2T6tLrkTDQ06x7dt7ayZ9ruXPk1_ON0dTkhsYeX-1smXqW0Z1-RKT040gqeSJIHnsNLfXexXdWGfvXFtEzGLssksf06nadfBq_wTrKOkxWHBxrvTVlvLjzZGbzgmJZ4dnsOd0xmjqA0hEYG7y7WpUywn7EYNe2QG28N8gE3iJkAeUAeAu-maF-bkg_sjXtVgZQZwXowYCKXzQ8tosfHhoXK3Abu1JFqke59w1-yhblbYAn7tafN4nWlRkQ7XqMfQz16d6cUdWJr5x70HsuSunadqkjPMQcAyvuDmHjcPN28cdWiG1yazUTefzB2yrLWBCtApRPzX6_-enuXz3l0veQ04WHFS0df0pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae8cb26f2.mp4?token=nAJpFp32j2t7KU6hfhX7t_C7Cg6YnT52xNNkpI-uC-OnVuz9UeqAxcD6GSSloeK2Xzzpv48qRfab1jr0woctyxmYKw9-6LTsIfsIq-IdmpQSYTIsrs3GGVK6bXnev3Vb-UWzOb3W6kWzMFHx4ZqB4v08XlRq8HCvucnz_qJ72PKSIKti8IrDMtYTvHnNdPv6KuOehKAOFYl_Do1WwKwgU_pMJ9yhpuO4OlY7Q_FXIb0Qy1EYfRh-g1gozT-8qk6UBdV9rLnELK_GkPvjggjWhWgolQY6_BTSMLADmrjICJVuMBMsCbKx6Fpuok1ODFxFw_zBQSZ9Y2T6tLrkTDQ06x7dt7ayZ9ruXPk1_ON0dTkhsYeX-1smXqW0Z1-RKT040gqeSJIHnsNLfXexXdWGfvXFtEzGLssksf06nadfBq_wTrKOkxWHBxrvTVlvLjzZGbzgmJZ4dnsOd0xmjqA0hEYG7y7WpUywn7EYNe2QG28N8gE3iJkAeUAeAu-maF-bkg_sjXtVgZQZwXowYCKXzQ8tosfHhoXK3Abu1JFqke59w1-yhblbYAn7tafN4nWlRkQ7XqMfQz16d6cUdWJr5x70HsuSunadqkjPMQcAyvuDmHjcPN28cdWiG1yazUTefzB2yrLWBCtApRPzX6_-enuXz3l0veQ04WHFS0df0pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماکان کجاست؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/659266" target="_blank">📅 14:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659265">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d4a213e37.mp4?token=X-WJ4z508DJugwegz0HVhg4h3GPlgeRQKcbud9STSPrO4blzh2n31tDQ1gPIMYNZXEbZt0i7eEJGiYhG2y6-2yq3jqwI0tOJQIKLm6o3mt2eF2vXmPNgvGNmrXxgH_z3vR4nAAEc80vc2qilvNzp-8kKXKwSNrESty0A1AsbG1rcoztOPePVtmlutavlG1TCRVOHeOs_IcWJ8J1XUJe3t3QD7ScEl9N2D_VveDorafW7VgGbTdWll_gde3h9O8vdQ5GSsN2hs22_DHPJ4vm-xrfvkwStVaofMtcQ7raQ2Cim6rkg13LSyv2wLnMW1BCrHjCWwmhwD0pb3ZjgSaw3Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d4a213e37.mp4?token=X-WJ4z508DJugwegz0HVhg4h3GPlgeRQKcbud9STSPrO4blzh2n31tDQ1gPIMYNZXEbZt0i7eEJGiYhG2y6-2yq3jqwI0tOJQIKLm6o3mt2eF2vXmPNgvGNmrXxgH_z3vR4nAAEc80vc2qilvNzp-8kKXKwSNrESty0A1AsbG1rcoztOPePVtmlutavlG1TCRVOHeOs_IcWJ8J1XUJe3t3QD7ScEl9N2D_VveDorafW7VgGbTdWll_gde3h9O8vdQ5GSsN2hs22_DHPJ4vm-xrfvkwStVaofMtcQ7raQ2Cim6rkg13LSyv2wLnMW1BCrHjCWwmhwD0pb3ZjgSaw3Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قلبِ من این وطن است...
🇮🇷
♥️
#ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/659265" target="_blank">📅 14:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659264">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS8zQGLDwLjo0ckt4m309w0LhAMuK0tTUJahyc5gXx6DewyjmXYGdzbCj5W11kO-9A2CyXRut9sOoRyzzK3oGGTKgsXUoBkyZjZZ37oYNEja36z3muoBsIuOhN3_RgW8A-XrSyAaJk0O6gxhXHj8dPBnRE64ZfwHlGdg_lYUhL0LXQeBH7tBqGHJ9tiwaAa3lZwf7_Qy2rQHBeI2O2cx2-Ec3dB6E3KiDo9hbks2a6wK9KUM5tXgSkLdGCmega2vDULbYPTkFLmyK8t-VaU8o9K5CVBRLwkxOm99kDv7jPAFgyH_pTxMYjcYb_MdTmuimUKRli4A5bwht98vQH-pMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین فرصت انجام خدمات دندانپزشکی با شرایط اقساطی ویژه و بدون سود
🦷
💳
کامپوزیت ونیر و لمینیت سرامیکی
✨
ترمیم و عصب‌کشی دندان
بلیچینگ و سفید کردن دندان
🦷
⚪️
به صورت اقساط تا یک سال
📅
🎁
آفر ویژه فقط ۲۴ ساعت:
جرم‌گیری با ۵۰٪ تخفیف
🎉
❗️
ظرفیت محدود
رزرو و مشاوره:
📞
09150156363
☎️
05138112425
📸
@asha
(
https://t.me/asha
).dental.studio
🌐
ashadentalstudio.com
(
http://ashadentalstudio.com/
)</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659264" target="_blank">📅 14:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659263">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e85d2e96f.mp4?token=ZCbz4su6dB2-Q1gov5VXh5MiChCkQ-xxQDM4Jexib0k2DeX2rX8dN9wkJnuLqzonwmGMdfHU4V_3Yw75VsyXIzBPrbPWe6zm0zvhJ-rsiRqLSXHPOYk5QWCWaK88IJ1C0FX_NdZSFArOwF3kwyc43iCC3utuNaZVOQWWpMcJUR3f67Uc9Vdx6MXbZNeUJWJo1ttxJztE5wdpmFos52ePu3jNAVj2di74MCNNYadlbMDUmCPCuXzLaeItIzK3ZsU33Ve4l3b4YVD3VG6Vw7XQJrwz1eYpPSPZjYzT68zEZLwzD0r8D8_wHPoo2sDY4XDdOYgowgqzieGsMqW_ex0AZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e85d2e96f.mp4?token=ZCbz4su6dB2-Q1gov5VXh5MiChCkQ-xxQDM4Jexib0k2DeX2rX8dN9wkJnuLqzonwmGMdfHU4V_3Yw75VsyXIzBPrbPWe6zm0zvhJ-rsiRqLSXHPOYk5QWCWaK88IJ1C0FX_NdZSFArOwF3kwyc43iCC3utuNaZVOQWWpMcJUR3f67Uc9Vdx6MXbZNeUJWJo1ttxJztE5wdpmFos52ePu3jNAVj2di74MCNNYadlbMDUmCPCuXzLaeItIzK3ZsU33Ve4l3b4YVD3VG6Vw7XQJrwz1eYpPSPZjYzT68zEZLwzD0r8D8_wHPoo2sDY4XDdOYgowgqzieGsMqW_ex0AZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از محل مورد هدف قرار گرفته توسط رژیم صهیونسیتی در ضاحیه جنوبی
بیروت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659263" target="_blank">📅 14:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcrOjdeoHa7_8DV87rlEI-4zp5oSq-I-FIhIoitdhIJ60hjqoQk6GuFcomI_dorfdPdhTCnHnyDakvZb1Jp45vDNWRkQJ7TAvGflb-UxNdK87RB_cUzpxb-v1i-jYgvIFa3htPEVJkAZ0YVSpZ19P_3oYx79cNJEDu4nAOS0QGcQq39mVcH_YHZbMzKn6litxhiDUEQ9r3Fp8yevuvX7Pu32fQ3xXK1bjK5Buk0RwfBtG3zspKpEDWm_mqFPmlFmuLcyOu4-lp2_gi904KMYm1_w2srjXt0yBzFAM5h1Y1fzeO5lEJWmZYaglJDoefzEM02HoK0eAu5EWzEg5NausA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsqFdvnIYYixbJxtOid-TCUEOgB79xVZKTrncuU-n6i0mmOLlrSOl4XdMLiBu5WxgVH_f9SaW1805IMvQNyui-vFBHWQmNXcJ7dyYe5TswA16wcdwNhVKdrI6f1MgPMqxqpIKXWbBMkFjMbcZs0tuQ7wP9p1VOvIO0e8yWrGgbyuXlNF5c69iRYw_-ALWLTC2qAHXhAIUzTDYm8dqigYaQjiNjXkUfxvszjILbWx1b_9v8zHU_PUEzgpVYi0jCiKvuzuwy3aPNHS1at0pRG-cI4KEbwV9oy_SdYW2xNyb9pBnlj1nWIHmsx-bux_l0v6P65DUR7vR_qrnArzm8IOqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db832997e8.mp4?token=Kc7qRL77YtFxKSzgZ4va2FK_u-40aFRfYwxNnrI-YOqGPW4xFfFsuJZZOZatjpcFrLxjsZtS02zoSuaByR3QeOPloBtve9jGNFndNiI5IBAlFx54jsas4CoiB12r7aCNUPMtZZmOKKjNkB1S2rpdwsL7CczG4_u3IWzlZe9kfdfL0Zu7CaRj1CTE-zEoaWGt8RUMDlVYEHnlVeQ7bX3rhE95w1siO6D0_y_VMMX_527PtRhtv5QRBF5N2mjhjtPFDG91FD0G83FBX8hXTJn3oTEjoPm9CPiKKfp5LP_SYwNG30NQaUyJj9dE79cKTlMOj2xAkJd4ExejTOJ5SGb3Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db832997e8.mp4?token=Kc7qRL77YtFxKSzgZ4va2FK_u-40aFRfYwxNnrI-YOqGPW4xFfFsuJZZOZatjpcFrLxjsZtS02zoSuaByR3QeOPloBtve9jGNFndNiI5IBAlFx54jsas4CoiB12r7aCNUPMtZZmOKKjNkB1S2rpdwsL7CczG4_u3IWzlZe9kfdfL0Zu7CaRj1CTE-zEoaWGt8RUMDlVYEHnlVeQ7bX3rhE95w1siO6D0_y_VMMX_527PtRhtv5QRBF5N2mjhjtPFDG91FD0G83FBX8hXTJn3oTEjoPm9CPiKKfp5LP_SYwNG30NQaUyJj9dE79cKTlMOj2xAkJd4ExejTOJ5SGb3Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به ضاحیه بیروت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659260" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5931c2cb.mp4?token=HNacvoBknKi1hR0D9M6xCuJ6k9NcjoBMKDV6rRo0RNUxU-o78Y78ZQnTpbDkf7kCqmONZeHFpP-RE4UGAKUYmOC3qY4Y9hRFBUqVW7ZUO57sDilHTRodiIdr110vLpMRPU3YigjgioaOdVVxgnuN9rWoqju6vYUzVBJjHzoo2dST_NjAAiKuxcnpco1uIPOQ0plcQxk19N9MU-qxiwPQVWRvfBOwa5dluBIrUtH9_rtg3r8vlY4oUfmov0kSAOVfyMwdzQH6Rn9t4ITcazOzfrHvXCsRXPXCyCZoonhvvqWwNwx5pCms6dSKLsWE03CYRu5cs13AimaLVREvots_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5931c2cb.mp4?token=HNacvoBknKi1hR0D9M6xCuJ6k9NcjoBMKDV6rRo0RNUxU-o78Y78ZQnTpbDkf7kCqmONZeHFpP-RE4UGAKUYmOC3qY4Y9hRFBUqVW7ZUO57sDilHTRodiIdr110vLpMRPU3YigjgioaOdVVxgnuN9rWoqju6vYUzVBJjHzoo2dST_NjAAiKuxcnpco1uIPOQ0plcQxk19N9MU-qxiwPQVWRvfBOwa5dluBIrUtH9_rtg3r8vlY4oUfmov0kSAOVfyMwdzQH6Rn9t4ITcazOzfrHvXCsRXPXCyCZoonhvvqWwNwx5pCms6dSKLsWE03CYRu5cs13AimaLVREvots_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس شبکه افق: ترامپ اعلام کرده نه پولی به ایران داده می‌شود و نه تحریمی لغو خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659259" target="_blank">📅 14:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abR1kVuDH6vjL-6ontejl5ZtchKXvybyhDQsgr8726YGLR_f20IeCSv78efPnMWtMpTRVKjr-poS3iOX1oPTHhnQucv1hoV_ABJu54aqhzFL95jNdf0snaZYOyH-FXhJFNZeHj71KLZsBJ96BK0ZJ897NBIJmrEtCmkWkQhNHaLf-C-DkpDI3qVz5uyamCyXDP4CaevMyOeuRnQJ3J_ztUGtDVEkOaotRE1Aw_H282LjfXZWuitIRydvWgtZTCWSrxux8wYWMYHd3TypLAAlbPjeiZg5NsERX_r2NHR-ejzeMjZxfukpW1tsfULltOQMoBOLHKMZLXDysLj2ML2VjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به ضاحیه بیروت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659258" target="_blank">📅 14:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات
وزارت اطلاعات:
🔹
یک هستهٔ ۴ نفره گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکه اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659257" target="_blank">📅 14:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از مقام ایرانی:  بر اساس یادداشت تفاهم، آمریکا ۲۵ میلیارد دلار از دارایی‌های ایران را از طریق انتقال مستقیم نقدی، همکاری میان کشور‌های منطقه و خطوط اعتباری مالی، آزاد می‌کند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659256" target="_blank">📅 14:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659255">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOtMtg9BUnTjrCretkBv48P7ugiYFL_v5PRFdmj4N8JKKgY5jbTqdqzY9yRVwD1QSYbGR75nI65WV1WwXkSM1_npZkrcwvoLRKlh5Y0JefRiqSGG-HF74i5UnfXMKmrXxD3stP89URcs_LE1yNfcvw7zhgAqtXnNamlHQXx68kNHuTrlyaZIAOkZNzI9VHLWfwaT5dyn9H4hmv_9OCZODNWfBYg4k4L-sF3_CyTuXrOwv30PuarROVpgG-Xs6b7QHfIByDsIx7lO4mJL9f17CNUMmnR3Sbp8ZhF5jp6Y2UnR-bF6H6RdzZkN6upG9IeQve4lo_VqZ6BCZRcIrD6mOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشکیل صف خرید ۴۰ همتی در بورس!
🔹
امروز یک روز تاریخی دیگر در بازار رقم خورد؛ ۴۰ همت صف خرید در پایان معاملات ماندگار شد و حقیقی‌ها با قدرت ۸ همت پول تزریق کردند.
🔹
ارزش معاملات خرد به ۲۰ همت رسید و ۹۷ درصد نمادها سبزپوش و مثبت بسته شدند. در نهایت، شاخص کل با یک جهش ۱۲۲ هزار واحدی در ارتفاع ۴ میلیون و ۸۱۸ هزار واحدی ایستاد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659255" target="_blank">📅 13:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659254">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآوش</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22853fbdc2.mp4?token=PM6419WX8aRfQJsQaoc6M5ZULaCEMlQaf3AGdPYAKzt3Nhh8nRqHf6q4V-wJmea6iWIdiO7R8hlDkgF3HhspPI2NJp8exQZbNR9QqBhIaHngXb7sCU2P6_OJD6q3kQxiMsvueJ_aFYYV-Dy8hgXQluBaKrEWTUqdr2lJ36Q2bMINzNdQxqj9UuwGp5wpFKefnznzRktf0-GJ92Mb509coqkcgvW25UfDfzjmOZklbPeVdohjfa3GnzmThlsoIK7wENMaCbhfhhkrqUXFwKnbP0YNaIxdI5KECkwW2c9U1mTzwtH_V7gVMaDEsIR5nL2bGpqm1iVHFUgo9AoQ1Ip0mCLUq3dLY8tqLISXgrryCRbktJs16C-zXvOb_lsi_FBdBb65a3FsPwda5Yg5QHVOSHv2CxdkfyCVPvrIhrUME3ug_s8zNO2IcCiytonu9BHm0Ssq4HcIGm53pP21Ni5bAAVbCfisUwO9d_Udv2Frc10wIjeKnrTbP4UYZvCb1eqxSTnvMrjGuEBUpBQl7-xQ-1vPsUbsz4treUTWWeuq9gul_sdtSNifnG3n7UzBDFlj9WvOIjeuD_xeJLuhuwJ0cf7lTjZvz3vtIhFQas0DAIt96JXO2TJ6jhzaj7k-xUwDFI1NOmerF_uIJ_5HtGjBNYH1csCcxy-CCcoPy3387nI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22853fbdc2.mp4?token=PM6419WX8aRfQJsQaoc6M5ZULaCEMlQaf3AGdPYAKzt3Nhh8nRqHf6q4V-wJmea6iWIdiO7R8hlDkgF3HhspPI2NJp8exQZbNR9QqBhIaHngXb7sCU2P6_OJD6q3kQxiMsvueJ_aFYYV-Dy8hgXQluBaKrEWTUqdr2lJ36Q2bMINzNdQxqj9UuwGp5wpFKefnznzRktf0-GJ92Mb509coqkcgvW25UfDfzjmOZklbPeVdohjfa3GnzmThlsoIK7wENMaCbhfhhkrqUXFwKnbP0YNaIxdI5KECkwW2c9U1mTzwtH_V7gVMaDEsIR5nL2bGpqm1iVHFUgo9AoQ1Ip0mCLUq3dLY8tqLISXgrryCRbktJs16C-zXvOb_lsi_FBdBb65a3FsPwda5Yg5QHVOSHv2CxdkfyCVPvrIhrUME3ug_s8zNO2IcCiytonu9BHm0Ssq4HcIGm53pP21Ni5bAAVbCfisUwO9d_Udv2Frc10wIjeKnrTbP4UYZvCb1eqxSTnvMrjGuEBUpBQl7-xQ-1vPsUbsz4treUTWWeuq9gul_sdtSNifnG3n7UzBDFlj9WvOIjeuD_xeJLuhuwJ0cf7lTjZvz3vtIhFQas0DAIt96JXO2TJ6jhzaj7k-xUwDFI1NOmerF_uIJ_5HtGjBNYH1csCcxy-CCcoPy3387nI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش مستمری، تکمیل متناسب‌سازی و پرداخت منظم؛ پاسخ تامین اجتماعی به فشار تورم
ترمیم قدرت خرید بازنشستگان با نسخه ۱۴۰۵ تامین اجتماعی
در سالی که فشار تورم و افزایش هزینه‌های زندگی همچنان بر دوش خانوارهای ایرانی سنگینی می‌کند، تامین اجتماعی با مجموعه‌ای از تصمیم‌ها تلاش کرده تا نشان دهد که از کنار دغدغه معیشت بازنشستگان و مستمری‌بگیران عبور نکرده و همچنان در پی حفظ قدرت خرید و ثبات دریافتی گروه‌های تحت پوشش خود است. افزایش مستمری‌ها، اجرای مرحله نهایی متناسب‌سازی و استمرار پرداخت منظم حقوق، مهم‌ترین نشانه‌های این رویکرد در سال جاری‌اند.
https://avash.ir/n/Rjk
@Avash_media</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659254" target="_blank">📅 13:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659253">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-7fGHGYv4mIsNVK5YKwsJUZyJzFaza4ZJfF811aAe9MAZG7eUy5Xe4D0A5V-SsZ4mq6tKkNcD0rYRmQeoa0nxHIWxGDjF_7lfi7kzbQrefj5YtRj9X6fthbDFo31B-IVz1RQ8IzKQIkohIFdL3K2F8bVP12Pvq8ZMC5g3rChtP8Drh-uGhyeuQiKp3Zs48JOYTvloOtRFGMG3uvSRtqauTh6xLD2Ix8_r3hIARckbL6AcN1Q6qbauWVOxWpriMdlonw4cYUFCEtl0vu3CYnm0a8Xd8MOIN9VxvO1vrIy1giWFWTSQtQHdkL3VbQFza2lBub4Huq3DNTYYTX6neBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر توییتر: چرا باید کودکی مثل این مجبور شود بقیه عمرش را بدون دست و پا زندگی کند، فقط به این خاطر که یک سرباز اسرائیلی دنبال سرگرمی بوده؟ واقعاً دلخراش است که چطور این همه وحشت بدون هیچ مجازاتی می‌گذرد. کوچولو، متأسفانه، انگار دنیا برای تو اهمیتی قائل نیست
😔
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659253" target="_blank">📅 13:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=K9-qYEfE3nY674_2-D4VI_uB2YeJh8PSyco_Gdm7mAh9yBlp514_RBIGFkceeafcvmalpfEjNQ4M242MoeQ40fvKcEYXLHXYT_1Di9JYyyjCg-lG7dhnp799vqDOHmivOLYV3wD4AJhyfmOG23oPwzke_Zl0dpTS7-KdIhfmsEiJd5nVez_rihNTa-VDH-3H3p3nYDYyitsskn0C1Tw5HgkNvG4L8JzqOAknBMnUWeNkXLERmewd33rPCkvkl4hAdyU4uw-ra7OIhsxNLDvSn1NorSokaEYHBGn7zfEZY2wZpC-NQEzkjNOL3BvqGl_AvEogM-6KvhLJS92-pkXWvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=K9-qYEfE3nY674_2-D4VI_uB2YeJh8PSyco_Gdm7mAh9yBlp514_RBIGFkceeafcvmalpfEjNQ4M242MoeQ40fvKcEYXLHXYT_1Di9JYyyjCg-lG7dhnp799vqDOHmivOLYV3wD4AJhyfmOG23oPwzke_Zl0dpTS7-KdIhfmsEiJd5nVez_rihNTa-VDH-3H3p3nYDYyitsskn0C1Tw5HgkNvG4L8JzqOAknBMnUWeNkXLERmewd33rPCkvkl4hAdyU4uw-ra7OIhsxNLDvSn1NorSokaEYHBGn7zfEZY2wZpC-NQEzkjNOL3BvqGl_AvEogM-6KvhLJS92-pkXWvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس شبکه افق: پاکستانی‌ها برای میانجی‌گری به ایران نمی‌آیند، بلکه مرتب پیام تهدید و‌ ترور می‌آورند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659252" target="_blank">📅 13:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX2KiT4HeL-fN8pJOAAjsReSlFtMUXGNUCvTrx4MvJiIN9iqJdf6sb7Llb2JbU0df6CqWVRj3G_Aa3WtKpUf5G2hQKcIlBQDyQXwySbKwtVGtmLhF3r1A54LT19_ZwVsFujKWw2bsPN_rHazzaJwvxAItOYoNhqgtfK2NCoXoM8z7feDTdcffPEwESz0Nv9ZRQdQI8i-xE8EojCTW_VeErK-g1uqmkGB96oqS4WJjRBceGIckEK_NhePFEFvCovTNge1U_csWmldCe1uUHL8s_GYMoOBpykRS3ENENN1Cnqk2o0ppu-ypWUmWuaGnney5hoV_2sCiRayE90zoImtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/659251" target="_blank">📅 13:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhhBPmUG27Duy_sAoFaMip9eudxc-2o4o585dbohSEk5JFdVgM1IKLnAN5dJcOXQxFmmtMhp48AL-3JCRchj4TpZOhojLHWzdYgEV2ovOG9cUfXm6v0VwbtfkHfUtaTYc7F5m4kCIb_IxXJk2PUcMPNiJ3tuyZgxMHpOxkzLkPwmh2wGBBYx3wefgHdA8n7zw-PX3MRgwA-ETPBPjG5W6GA7QC07kUSOPByJgRKWWYEvu-ecBmCStB_nrj-_PbC5zkMfxpymbMcSrWluUoiS5JO2E7Iew0PreG0DZPrL_Xj-QLr0CI4mldI0Uzo5iTJeEOso2-QkyJ1KXrGVq9gJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۴ خرداد ۱۴۰۵؛ ساعت ۱۳:۳۰
🔹
افزایش خوش‌بینی نسبت به توافق احتمالی ایران و آمریکا، بازار طلا را وارد فاز اصلاحی کرد.
🔹
بازار طلا امروز با موجی از ریزش قیمت‌ها روبه‌رو شد. هر گرم طلای ۱۸ عیار در کانال ۱۷ میلیون و ۱۰۰ هزار تومان نوسان می‌کند و سکه نیز در تمام قطعات عقب‌نشینی کرده است.
🔹
هم‌زمان دلار پس از مدت‌ها از مرز حمایتی ۱۷۰ هزار تومان پایین رفت و در محدوده ۱۶۹ هزار تومان معامله شد؛ عاملی که فشار نزولی را بر بازار طلا و سکه تشدید کرد، در حالی که اونس جهانی روی سطح ۴۲۱۹ دلار بدون تغییر مانده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659250" target="_blank">📅 13:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
والیبال لیگ ملت ها؛ صف آرایی ایران برای بلژیک، امروز
🔹
تیم ملی والیبال ایران از ساعت ۱۷:۳۰ امروز در چهارمین دیدار خود در مرحله مقدماتی لیگ ملت‌های ۲۰۲۶ به مصاف بلژِیک می‌رود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659249" target="_blank">📅 13:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بخشایش: احتمال آزادسازی ۱۲ میلیارد دلار و لغو تحریم‌های نفتی ایران
احمد بخشایش، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
در این تفاهم تنگه هرمز باز می‌شود و به خاطر رفت و آمد کشتی‌ها تعرفه‌ای اخذ نمی‌شود، اما بابت خدمات بیمه‌ای، سوختی، محیط زیستی و...ایران می تواند عوارض را دریافت کند
🔹
به احتمال قوی ۱۲ میلیارد دلار پول‌های بلوکه شده ایران در قالب کالاهای اساسی و بهداشتی دریافت می‌شود، اما ایران اصرار داشت این ۱۲ میلیارد را نقدی دریافت کند و آمریکا گفته است در قالب کالای اساسی؛ در این مسئله اختلاف نظر وجود داشته است.
🔹
پول را متناظر با انجام تعهدات ایران در طی ۳۰ روز یا ۶۰ روز آزاد می‌کنند. بعد از ۶۰ روز بحث ایران است که روی غنی سازی هسته‌ای صحبت شود؛ ایران قبول کرده است آن ۶۰ درصد را زیر نظر آژانس در داخل رقیق کند.
🔹
همچنین روی بحث ۴۰۰ کیلو اورانیوم آمریکایی‌ها می‌گفتند به کشور ثالث منتقل شود، اما ایران می‌گفت از ابتدا در داخل می‌توانیم آن را رقیق تر کنیم. فکر می‌کنم لغو تحریم‌های نفتی ایران انجام می‌شود، اما تحریم‌های ثانویه و تحریم‌های کنگره شاید ماندگار باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659248" target="_blank">📅 13:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
امضای ۲ مدیر دولتی غیرقانونی اعلام شد
🔹
طبق نامهٔ حسابرس دیوان محاسبات به صندوق بازنشستگی کشور، تعهد و امضای مدیرعامل‌های «شرکت آتیه صبا» و «صنایع شیر ایران» واجد اشکال قانونی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659247" target="_blank">📅 13:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای
العربی الجدید: تهران هنوز توافق را تأیید نکرده است
العربی الجدید:
🔹
ایران هنوز تأیید نهایی خود را برای یادداشت تفاهم اعلام نکرده است.
🔹
به گفته یک منبع آگاه ایرانی، احتمال امضای توافق در روز یکشنبه منتفی است و بررسی‌ها در داخل ایران ادامه دارد؛ هرچند ممکن است تهران امروز نظر نهایی خود را اعلام کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659246" target="_blank">📅 13:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420013fdd3.mp4?token=SZ7TtaFhbhdwUzwpnpAZulBTJago5ZUe03Zoy2eDg8eqwFDuw5HAfYrBUaLwxknxnpxlAI4TBNJFRWfjl9Tt_fJ3rqUrOIxShss0QqCw-GISU7-NeiGIZbAf_vOmeTGL3upSGGwt6cJ5QuHfzxlJ45Hpi-ztNmZdIg22S-EH9laDLkJOZvK8jh1lLKfE6_lhyvOo3OuxFpFqdKn8U_VpkckjC2wAPiYPugAVBeQi8imD_5nwign1nvM3miYAlvpsjlAo7Mtc4DYfeK8lZoPmQkwP7IBrPXOiGiYC27HFhrxUtx4-OIudqMxHy0AO_-aZeCweHyiRQshiSpu_48ZYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420013fdd3.mp4?token=SZ7TtaFhbhdwUzwpnpAZulBTJago5ZUe03Zoy2eDg8eqwFDuw5HAfYrBUaLwxknxnpxlAI4TBNJFRWfjl9Tt_fJ3rqUrOIxShss0QqCw-GISU7-NeiGIZbAf_vOmeTGL3upSGGwt6cJ5QuHfzxlJ45Hpi-ztNmZdIg22S-EH9laDLkJOZvK8jh1lLKfE6_lhyvOo3OuxFpFqdKn8U_VpkckjC2wAPiYPugAVBeQi8imD_5nwign1nvM3miYAlvpsjlAo7Mtc4DYfeK8lZoPmQkwP7IBrPXOiGiYC27HFhrxUtx4-OIudqMxHy0AO_-aZeCweHyiRQshiSpu_48ZYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط مرگبار یک دختر در دره ای در برزیل بر اثر اشتباه پرسنل مرکز تفریحی
🔹
در ایالت سائوپائولو برزیل، یک دختر هنگام اجرای طناب‌جهش (نوعی پرش با طناب) جان باخت؛ سازمان‌دهندگان این وسیله تفریحی، تجهیزات ایمنی را به او نبستند و او را به داخل دره پرتاب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659245" target="_blank">📅 13:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWCjw0X8ZR7nU8H4VqM7NxPRwpNNrDtQ6qwDwwPieaDZ7kV4DZRxCZinEomYGjCyAxp4VLDM4hPHxP-eQweaFTRl_lE-xwP9jXEHArSI7lVFvTEUdhbk5efbzca_FMvE07Bz3JIVSdwAmBdrUi1id_jutZ0STNmEj6qu9qnihtj3rtANdvsj8CM4t_bDYRn5PL5HH1F6skk4FxtK8MnQ6V86AdUhcKxEQEyaGJFjDxk4-eqOrGiQqbDMsauDWpHl1BKbUREc9SIlI6Gqrq9iBYXWXKs5ScokjocQNk0W9m0Lo73q94ktlDIDRj3NhxQI28bkoMGhU47PFX07H8DqYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد خودروهای فرسوده ایران به بیش از ۲۲ وسیله نقلیه رسید!
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659244" target="_blank">📅 13:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
خروج ناو هواپیمابر شارل دوگل از منطقه
🔹
ناو هواپیمابر فرانسوی «شارل دوگل» پس از پایان دوره مأموریت ادعایی خود در مدیترانه شرقی و دریای عمان، در حال بازگشت به پایگاه نظامی «تولون» در فرانسه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659243" target="_blank">📅 13:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdO656ujeZGWWKAh7gP4ZTaAYVksjgeCH92MK66HjILv15CWxTQKEJZmGky7E6vSvOXsxsGbDCyqoZ9VIzyf2W_UyERBlow2szSKH5HM5SwKZ1KW3wP920ugHp79BaB_mQdJXyzDPkBgPxUoYng7vd8CrwMI4WkLFE81ImNFuIacc3tBJREyb_09QlKOgMsnxhM5u4y_9SdmuMxVOue9BdBxG_wq0YOhaTonaooQ_0x2m8cjzZgeo6XhfFXvySouqXNqQaH7LElSmGwadiAB0WlYxb1lSrCKztwcs6lM8ouPGd3tI1Iv544lO51cjV4cbGyuWzNPuf2aryL4COF1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضاییه: دشمن به مخدوش کردن وحدت و انسجام ملی چشم دوخته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659242" target="_blank">📅 13:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حاجی‌بابایی: دولت وضعیت استخدامی معلمان را تعیین تکلیف کند.
🔹
آموزش و پرورش: امتحانات نهایی از ۲۱ تیر برگزار می‌شود.
🔹
شنیده شدن صدای انفجار ناشی از مهمات عمل‌نکرده در تبریز/جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659241" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2583a92d5f.mp4?token=vEHOlmoQr3FYU1hgpiy0yyTKBmwJ2MkygIVkYQVAOoHg3bLwYgsp2wYzUvEEUHokTb9dACVZm56hBcfTYYt_ua6FxsDF_3d12i6kZY-lxC1g3K9VJjgs-_ASMVaud2-fHXQSK5_2GQulL3KZ6_2GBSx_m7zo22F7KrSfEwqHTPr9Q2QJiuJYegZmX64rLCq1_UzXe7kvYNhrCPh_7iLxB6v2a8dukCghgYuphbosag0TrTPZuUhowiannsG7dcLicaV6BCD39leizwjZFRhcQzemgX7l-Og4rgYfpRAm1aZ5mTO1Wjug-5zQXMoYXpMJivBqHa8GwUBdVO8Fzp2JYRM5UvZVfPZs-nLD3db-4SpPoT9wsp5TV-KHWQPsWATy3iaGSsbC0orAA1Q5ze5021eH6BhRCRdbBfut3XByg2XRu_p2wZRtkylN5uoEzJaAnz0iv5-UyYMBK81jsKxlMYhRonpt56uCY9GvXbBH6kQdP_3w5YZKe7oM2-djBf_OHVDmPw-KgW9BM7VScDPS5_h7-YrN1JUjMpDlNGL8VP5oJkXOPW3mHAkjP2vl6sXN2jO3TrOXsvjnQbWI1FUfEwlIt0_R2y2Rgw0j-i7w5UClB7XDKEMYTdPw75MsCsnsjQTs3PTwKfVUIKgJ8QDR1pNIlDglfpXRJ-gPQAvhI18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2583a92d5f.mp4?token=vEHOlmoQr3FYU1hgpiy0yyTKBmwJ2MkygIVkYQVAOoHg3bLwYgsp2wYzUvEEUHokTb9dACVZm56hBcfTYYt_ua6FxsDF_3d12i6kZY-lxC1g3K9VJjgs-_ASMVaud2-fHXQSK5_2GQulL3KZ6_2GBSx_m7zo22F7KrSfEwqHTPr9Q2QJiuJYegZmX64rLCq1_UzXe7kvYNhrCPh_7iLxB6v2a8dukCghgYuphbosag0TrTPZuUhowiannsG7dcLicaV6BCD39leizwjZFRhcQzemgX7l-Og4rgYfpRAm1aZ5mTO1Wjug-5zQXMoYXpMJivBqHa8GwUBdVO8Fzp2JYRM5UvZVfPZs-nLD3db-4SpPoT9wsp5TV-KHWQPsWATy3iaGSsbC0orAA1Q5ze5021eH6BhRCRdbBfut3XByg2XRu_p2wZRtkylN5uoEzJaAnz0iv5-UyYMBK81jsKxlMYhRonpt56uCY9GvXbBH6kQdP_3w5YZKe7oM2-djBf_OHVDmPw-KgW9BM7VScDPS5_h7-YrN1JUjMpDlNGL8VP5oJkXOPW3mHAkjP2vl6sXN2jO3TrOXsvjnQbWI1FUfEwlIt0_R2y2Rgw0j-i7w5UClB7XDKEMYTdPw75MsCsnsjQTs3PTwKfVUIKgJ8QDR1pNIlDglfpXRJ-gPQAvhI18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی جذاب برزیل و مراکش
🔹
🇲🇦
1️⃣
🏆
1️⃣
🇧🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
▪️
آینده‌ای طلایی با سود طلایی
▪️
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659240" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
کنکور سراسری ۲۹ و ۳۰ مرداد برگزار می‌شود
وزیر علوم:
🔹
کنکور سراسری سال ۱۴۰۵ به صورت قطعی در روزهای ۲۹ و ۳۰ مردادماه برگزار خواهد شد و با توجه به زمان‌بندی جدید، به احتمال زیاد دانشجویان جدیدالورود از نیمسال دوم تحصیلی وارد دانشگاه‌ها خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/659239" target="_blank">📅 13:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
منبع آگاه: تصمیم نهایی تهران دربارۀ تفاهم‌نامه در دست بررسی است  یک منبع آگاه:
🔹
ایران هنوز تصمیم نهایی خود دربارۀ تفاهم‌نامه پیشنهادی را اعلام نکرده است.
🔹
بررسی ابعاد سیاسی، حقوقی و فنی پیشنهادهای مطرح‌شده همچنان ادامه دارد./فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659238" target="_blank">📅 13:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
هشدار سازمان بازرسی به بانک‌های دارای عملکرد نامطلوب در پرداخت وام ازدواج و فرزندآوری
؛
اخطار قانونی صادر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659237" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei8PXk53ubTNRVcCB7WARMxxUsmM5HLA2frhtU0Ke7jLRXPzJe0UUdt2tXrKSs6bZDQ8dAx829j-z_QMdYwxHBnlwqtiKh8OSye9QuLzol3b_1ZSoayvzEM0zmo7QN84_OROOH8wUcvcNXLz5_gpBlCfgmNEU-xBE32J2_ao1ui-0Xgg19HwoqoP5P7UYWUShBCv6txcORv83XEmdOYUDxhwjWzOHayjkEDpM_x7jO8VS23nz-5TkD-UrfNmBFM5GQADnIpNE1mNnfzH5raXgXCA4mLbBO0xOnB0j7eZf-EqkKHIuIvpnIXNlKefxTnHoTiJ3VW8bARAuqf27yp8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ دقیقه‌ای که آب ۳.۵ میلیون نفر را تأمین می‌کند
🔹
با کاهش ۴ دقیقه‌ای استحمام یک میلیون نفر، ۱۱.۸ میلیارد لیتر آب ذخیره می‌شود؛ معادل نیاز اصفهان و شیراز. در جنگی که منابع ما با فشارهای اقتصادی هدف قرار گرفته، اقدامات خردِ جمعی را در خنثی کردن نقشه‌های دشمن دست‌کم نگیریم.
#سنگر_آب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659236" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM5JaZDX1f64SjxgYNlfaP0qCXHEtOE0plGwXI1smrkvWONbHu2sdE6HhssHQxVrmTWzrPQGHMM4uTJCdngoxBkrYP6a_Nb7rxJxZPEIIzZnZYttNjH0fUZKe5PxHpvr9EDPbxKIi4HEEgrFJyePJVnEEdVOQ2HAPOWl3RpcILKRz6VhuRKRhg3z1tc0sd50yDt4nC0Lay3EOdmPOKTlpEJk8c4WW9eErXEJLQgCt9qIs9YR0cal_0QqkWKyOjAGzvcTB1Cu6wS-zPYkyFP4kNhorXSRF-jM1yyXbsecH5jWfE6KPhDqHnNnjVpUWWLzcEs-aVhENgNh2OwI_XFEUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر با تساوی مقابل سوئیس، اولین امتیاز خود را در ادوار حضور در جام‌های جهانی کسب کرد @AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659235" target="_blank">📅 12:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659233">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bfd5ffba2.mp4?token=a0Tp5tVozcOF_HfftgQx6X-I25Y-xoGnBP7ixDFs4h064hneuN5Y92TFzFnQ1akk-6qmOBlnb3OaSo55NBB8QBE83JQXF8ujLj_zQvH7cUjouUJZ4xsGbZLhADD0phl9ASlYU8MDI-tUMu1Rt_ej60M3fOscZfTkaHu3HoWpCO00EZZZNlEp8IiHsk7gBRCcM_wy0Q1qs-cALYM-T_P5OUeCaJXiZmgGvG4R4c_4wL3eRDwTfuHRwxk9FKYYx9HEHSMNUMEaDMOpTWcdoq1VZURPBG-Y3S46_zsx_Qh70p1n1a3_j2Og1UuTd_UQiW4DoSu5HyexUJp9wWRSaNQ_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bfd5ffba2.mp4?token=a0Tp5tVozcOF_HfftgQx6X-I25Y-xoGnBP7ixDFs4h064hneuN5Y92TFzFnQ1akk-6qmOBlnb3OaSo55NBB8QBE83JQXF8ujLj_zQvH7cUjouUJZ4xsGbZLhADD0phl9ASlYU8MDI-tUMu1Rt_ej60M3fOscZfTkaHu3HoWpCO00EZZZNlEp8IiHsk7gBRCcM_wy0Q1qs-cALYM-T_P5OUeCaJXiZmgGvG4R4c_4wL3eRDwTfuHRwxk9FKYYx9HEHSMNUMEaDMOpTWcdoq1VZURPBG-Y3S46_zsx_Qh70p1n1a3_j2Og1UuTd_UQiW4DoSu5HyexUJp9wWRSaNQ_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمدین آمریکایی: تنها کاری که آمریکا می‌تواند در مورد ایران انجام دهد این است که دمش را روی کولش گذاشته و فرار کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/659233" target="_blank">📅 12:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659232">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3ceaef5a.mp4?token=jOoh34hPU16Rxdw_ePKClTSZfn1VaUkiBYVgoLcICc4vqckSvx8mvcX011okDZq_79_9mh6tVIWoHruj2bEu26fOJPR2Q_HfXm6Y4siuntpJ4pRjFhTl9NtkHXOHrvzwQnJnNKRhonmm6IiPA5uUp5FIaKT3oikeg_tT_V-I6-SCAT5pZnZfnZ9ILJqaHw14QjW_z6xezCMGZuLtMWYW-nKPRlv25m4UuJF6Uixb05oxtUCQnIj8BZouP_apBCBotd829n4RXld3oFqoxHOs_41HFQKi6iykEa7an40LHi5bKl1r4VAL5i71o6j_elPdp25KaIM59rwP-x3Ijf6CyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3ceaef5a.mp4?token=jOoh34hPU16Rxdw_ePKClTSZfn1VaUkiBYVgoLcICc4vqckSvx8mvcX011okDZq_79_9mh6tVIWoHruj2bEu26fOJPR2Q_HfXm6Y4siuntpJ4pRjFhTl9NtkHXOHrvzwQnJnNKRhonmm6IiPA5uUp5FIaKT3oikeg_tT_V-I6-SCAT5pZnZfnZ9ILJqaHw14QjW_z6xezCMGZuLtMWYW-nKPRlv25m4UuJF6Uixb05oxtUCQnIj8BZouP_apBCBotd829n4RXld3oFqoxHOs_41HFQKi6iykEa7an40LHi5bKl1r4VAL5i71o6j_elPdp25KaIM59rwP-x3Ijf6CyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشن با نقاشی دیواری بر پلی در کالیفرنیا!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659232" target="_blank">📅 12:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659231">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
مشکل خدمات بانک‌های تجارت و صادرات رفع شد  شرکت ملی انفورماتیک:
🔹
طبق آخرین گزارش‌ها درپی اختلالات به‌وجود آمده در ۴ بانک ملی، صادرات، تجارت و توسعه صادرات، مشکل خدمات کارت های بانکی بانک تجارت و صادرات رفع شده و تراکنش‌ها با موفقیت درحال انجام است.
🔹
موضوع…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/659231" target="_blank">📅 12:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659230">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO-VDV_JbByoNHlMlgc38K-FREOQRagFFC_CuitUClzCj0vBj6jm2lmQohjuKIvw_RSu4GfD33OsWlA1YBORDN_eQNrR9YFfJo5ioRhzmfvv4tiS-7mKceAV1mL-WVxPTPRUvFujYibgWLtruWtpYSz6c6iDbCnIjY4eHg7bUl03MUBUjRbzKxSXNoiKDQaKlBiL5WYw_V4iij8HrQgIyTg8QWpzH9w5qqHl0Yy5CDvo4YHZ_qsUo7zk8J3BOSfZ1CfsK-aaoNJW0V3lCdIFWhaIhRcAl33tGOQgQt-i9AnkZw33HeZaNcjQcJkSH4XyYPb0pUFkEi5Y6PJHRnJxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس از ۴.۸ میلیون هم عبور کرد
🔹
شاخص کل بورس امروز با رشد ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید و یک رکورد تاریخی جدید ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/659230" target="_blank">📅 12:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659226">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae92df0369.mp4?token=MRr47eVQBuCLuAklazw9aRud7NeprxU8YzQzH_ov7AL-Ih1i4fWsWluuCCoemzKQrHBN3Bt0sTxBzZellxRmzv79gVwOv1OTXDw5r6FQ4aEZxRs8OnyY0FvpvdsMgxD4GYHGXivF7gxZanbhYoiX9EiSZgkAAJo6nnoUbD_5713CcuAKtq1Sm6u9Q1J1z89J3QBFxhBVJXj5lVoj6Qz3UACULkyGruzdzWKnpkIBgSW28nM6aIa2Jf-8MIQWtrCdelKeqadjnCDT88sYAI01wmU1ceHD7YoHFJQp8IewHd-yfxjdNmqjjtrsnMOSlmz6OfFg7WPGBeJQbyXXSTr4Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae92df0369.mp4?token=MRr47eVQBuCLuAklazw9aRud7NeprxU8YzQzH_ov7AL-Ih1i4fWsWluuCCoemzKQrHBN3Bt0sTxBzZellxRmzv79gVwOv1OTXDw5r6FQ4aEZxRs8OnyY0FvpvdsMgxD4GYHGXivF7gxZanbhYoiX9EiSZgkAAJo6nnoUbD_5713CcuAKtq1Sm6u9Q1J1z89J3QBFxhBVJXj5lVoj6Qz3UACULkyGruzdzWKnpkIBgSW28nM6aIa2Jf-8MIQWtrCdelKeqadjnCDT88sYAI01wmU1ceHD7YoHFJQp8IewHd-yfxjdNmqjjtrsnMOSlmz6OfFg7WPGBeJQbyXXSTr4Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق‌ کردن زلنسکی از حملات پهپادی به روسیه
🔹
رئیس جمهور اوکراین با انتشار یک فیلم اعلام کرد که پهپادهای این کشور در عمق خاک روسیه به یک تأسیسات نفتی در یاروسلاول حمله کرده‌اند و این عملیات باعث اختلال در ۶ فرودگاه و اعلام هشدار حمله هوایی در ۲۸ منطقه روسیه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/659226" target="_blank">📅 12:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659225">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4dd5e434.mp4?token=DtVhXG7jXkEFez0P87llOaXgIeifl3c7pqOqqr-dsupr40MHSwBggVx26vnZ329WPDPOgXDCvTTqcocCMUAimxJvKUif0BYIycWme86xvnuRK1dOIRBzIjILdurvVhTzvoPfA1LbcLaiNKn9DGsrAIrsZOxLziwDzm8C3eXPuJdUm8SwiYklyLyOw6lHoBokZm2ln_GSvy1_mWghQE2X96vMEm3vQUPcYl0Nkk_hzGmYHNu9o2IlnltVyeKNCHdk9-N_cdkEnYfF7-RhyC-NBnmRur-BkDBamPWXL4Dp3zJVliYBJrR4Q18blF7-AICQ6C9szLRCdoLhm5Ku2u3CwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4dd5e434.mp4?token=DtVhXG7jXkEFez0P87llOaXgIeifl3c7pqOqqr-dsupr40MHSwBggVx26vnZ329WPDPOgXDCvTTqcocCMUAimxJvKUif0BYIycWme86xvnuRK1dOIRBzIjILdurvVhTzvoPfA1LbcLaiNKn9DGsrAIrsZOxLziwDzm8C3eXPuJdUm8SwiYklyLyOw6lHoBokZm2ln_GSvy1_mWghQE2X96vMEm3vQUPcYl0Nkk_hzGmYHNu9o2IlnltVyeKNCHdk9-N_cdkEnYfF7-RhyC-NBnmRur-BkDBamPWXL4Dp3zJVliYBJrR4Q18blF7-AICQ6C9szLRCdoLhm5Ku2u3CwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حزب‌الله از حمله به سایت نظامی «بلاط» متعلق به ارتش رژیم صهیونیستی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/659225" target="_blank">📅 12:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659224">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuHEtakyfiNDvVUbhuJ_nyyBSfkxkk6L5UMeRpJ1SNdEHDExfPqJt_x81k0TLr6c1GNPUBHLb6i2q7oFdh9wBsyApD87Qqr1s3EKV3Bz00WJw1PgEvaOaP6KBHm8TMVRMZto6OmudTB58hzvAS5WDz1ibvJKcsSEFBlpvHb-ceyx1ZFTSqUVSJ_3R8vCpX_zjGhI5sPrxkvMqLugsn34iddHvdQezwHNsQoLt9334ylBrkOlCK7avM8Ov9GFAyohnD1Ui9XS8ecdZNEthiiGyXdJmku9Fl9-SZfbLmQltrVR6c9Y_n-MX_OH2Q5eOLDCa_33oIvsJvpJfHsM7NXJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای تشخیص طنز، تبلیغات و خبر جعلی #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659224" target="_blank">📅 12:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659223">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
انگلیس صبح امروز در کانال (احتمالاً کانال مانش) به یک نفتکش متعلق به «ناوگان سایه» حمله کرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/659223" target="_blank">📅 12:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659222">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر راه از تخصیص سهمیه سوخت و لاستیک به کامیون‌‌های فعال در حمل کالای اساسی خبر داد.
🔹
ثبت‌نام آزمون کاردانی به کارشناسی ناپیوسته از امروز آغاز و تا ۳٠ خرداد ادامه می‌یابد.
🔹
انهدام مهمات باقی‌مانده از جنگ رمضان امروز در سردرود آذربایجان شرقی/جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/659222" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659221">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb865ba92.mp4?token=UBpJl9DjbEuDbMDvKwSYP3WBKu8PoOjvvIt28aALCCTgXlf2J1T2bv1xNeZS4PdCb5p-i3J9Mfyp89fKo34kEl8vaEhVvGeLaykwMzHZSirWibvxru3290wpS920MH8mgMRu7q2XbunNYwk6HHIBAb3ybNLQVSFz8tTQXBIBZGHGRz78NH2q_wWS-ts6MMSRkczBIzM9v8sTiiBzYFzBbfWv-rxNV-TVaHdLeD91TIMeNBJUenkEjEuGHlnicIsAQ0aRum9a3-H0N8tnI7-EWEufGFCFyES_8Fmteh9qvbVbCUMfitX_gbSEqs6xnArd7sntBe0WzJUtKgSInx_tGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb865ba92.mp4?token=UBpJl9DjbEuDbMDvKwSYP3WBKu8PoOjvvIt28aALCCTgXlf2J1T2bv1xNeZS4PdCb5p-i3J9Mfyp89fKo34kEl8vaEhVvGeLaykwMzHZSirWibvxru3290wpS920MH8mgMRu7q2XbunNYwk6HHIBAb3ybNLQVSFz8tTQXBIBZGHGRz78NH2q_wWS-ts6MMSRkczBIzM9v8sTiiBzYFzBbfWv-rxNV-TVaHdLeD91TIMeNBJUenkEjEuGHlnicIsAQ0aRum9a3-H0N8tnI7-EWEufGFCFyES_8Fmteh9qvbVbCUMfitX_gbSEqs6xnArd7sntBe0WzJUtKgSInx_tGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان تلخ مرد عنکبوتی یمنی
🔹
«قعقاع بن عنتر»، کوهنورد و ماجراجوی سرشناس یمنی، در جریان انجام یک نمایش خطرناک، تعادل خود را از دست داد و به داخل یک دهانه آتشفشانی سقوط کرد و جان باخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/659221" target="_blank">📅 12:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659220">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808b08b6f4.mp4?token=tHWyG8DJO7QQkcVn_4Ltk4mlmqiKSnCmJpgwyzPnUo-RYb6ahPthn0sSn6dNYIOY1Y9aZ7el1aA6syGwfwfj8sP6ZcFPLTt4-1meC9iVc4khGzJWl6xTSaJDZNPghB1S9ls24FTmA3ONVM2Qeld--oRWEV_tMAK7nqVb3q5VAblLevK8z1Z-bQBJvKecBSoeJZfZjuA2gYPl4ncdmfS9oDmESvinMVV3MlX02yJbpp5gqVDG5VO3Qyq5qrYcweE3VdKDQruU0sfmMbmyLs6opt2iB-5SlOPyxsJtaI70pfzPeNt2fnb0ZAEhmtipq-PerN162l89E7e0sKTwmbjnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808b08b6f4.mp4?token=tHWyG8DJO7QQkcVn_4Ltk4mlmqiKSnCmJpgwyzPnUo-RYb6ahPthn0sSn6dNYIOY1Y9aZ7el1aA6syGwfwfj8sP6ZcFPLTt4-1meC9iVc4khGzJWl6xTSaJDZNPghB1S9ls24FTmA3ONVM2Qeld--oRWEV_tMAK7nqVb3q5VAblLevK8z1Z-bQBJvKecBSoeJZfZjuA2gYPl4ncdmfS9oDmESvinMVV3MlX02yJbpp5gqVDG5VO3Qyq5qrYcweE3VdKDQruU0sfmMbmyLs6opt2iB-5SlOPyxsJtaI70pfzPeNt2fnb0ZAEhmtipq-PerN162l89E7e0sKTwmbjnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق‌ کردن زلنسکی از حملات پهپادی به روسیه
🔹
رئیس جمهور اوکراین با انتشار یک فیلم اعلام کرد که پهپادهای این کشور در عمق خاک روسیه به یک تأسیسات نفتی در یاروسلاول حمله کرده‌اند و این عملیات باعث اختلال در ۶ فرودگاه و اعلام هشدار حمله هوایی در ۲۸ منطقه روسیه شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/659220" target="_blank">📅 12:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
قطع دو ساعته برق در راه است
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی:
🔹
توانیر امسال اعلام کرد ۱۲ هزار مگاوات کسری برق دارد در حالی که سنوات گذشته بین ۱۸ تا ۲۰ هزار مگاوات کسری اعلام شده بود.
🔹
برآورد ما این است در ایام گرم سال، حداقل دو ساعت قطعی برق خواهیم داشت./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/659219" target="_blank">📅 12:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659218">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
زمان برگزاری آزمون ارشد ۱۴۰۵ تغییر کرد
سازمان سنجش:
🔹
به‌منظور فراهم کردن زمینۀ حضور متقاضیان در آیین وداع و تشییع رهبر شهید انقلاب، آزمون کارشناسی ارشد در روزهای پنجشنبه و جمعه ۲۵ و ۲۶ تیر برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/659218" target="_blank">📅 12:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659217">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksBElsag9c4AptEMksjIdDEXq5D0cP72_Rr_hFpXbstFsL7e7-SZaCDGYZyvxhWMM8W6awuF-Gb2salpPfQbtp8SmsONN3nEwqP-viL_ROyBmZOKFFlZTd9YcHf_eeg_Xo-lWyqJzM9vJy-QKTVlRcyGEG08lF3x_o40NNslwiX5WweAYB2cqb1T17wRpf9pEJ_rsoi7aobOMzFKSFc-s47gOSPbslb2Blf0Oh0AdB571SMLqCMrrXjp_3QX3-S9Jd0ggyOIiTiBUd4qkCeSx2RR2SAsGIaBgKbaExhiW7F6CpW1irIrulrV4doVOT4P74lNw8FyfGHXteMlxHmhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارزش دلاری بورس از مرز ۹۲ میلیارد دلار عبور کرد
🔹
ارزش دلاری بازار از مرز ۹۲ میلیارد دلار عبور کرد و در تایم فریم هفتگی همه چشم‌ها به هدف ۱۰۵ تا ۱۱۰ میلیارد دلار دوخته شده است.
🔹
امروز سفارش خرید ۵۰ همتی در پیش‌گشایش بازار تب و تاب بورس را بالا برد و در حال حاضر ۸۳۰ نماد بورسی معادل ۹۹ درصد از کل بازار سبزپوش و مثبت هستند.
🔹
به نظر می‌رسد موتور بازار برای صعود دوباره روشن شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/659217" target="_blank">📅 12:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659216">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWMjUDJV3MEvb8mEcT4d9Z1yFX02LJkFgfqR7gIxaKSF2juva36tZ_QBAW5mRLlj_PPp1JJcjzGL1CVWeKZrpoRYsIf4d5h6B7zKTHfnR3peX_j2pAiIgsFvu6QnnQB0GgDcqN-l3ecPz4XGiWppfBQW_uZRjF2iBb46hnKtEdT6mRvoSST2RdhOw_sq1EBB5-8I3fSKfkkVhmiiCIDgJzCZZKjIpt7m2zoA0epQrs8KqcL4EFVjn41qs6gaPvbkub3Z8HBSUkn1RtYW0C5DSyaUcBvPA_tnxKfi19hEJCh7yhEioUUnYjIofAzYxKtZVmwyQV_nrFRFv6p6P0NISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیدحسن خمینی: تخریب مسئولان عالی‌رتبه کمکی به حل مسائل نمی‌کند
🔹
کشور با دعوا، اختلاف و سخنان تند به نتیجه نمی‌رسد و باید به خرد جمعی و تصمیمات کلان نظام اعتماد کرد؛ همان‌گونه که در دوران جنگ با اعتماد پیروز شدیم، در دوران صلح نیز باید با همین رویکرد پیش برویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/659216" target="_blank">📅 12:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659214">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa16d263ca.mp4?token=eBx38funACo3kaPTb5P8dmfAIkC6a_tm5ZIfi06PYQasKvNSUqQwM6UbbNqFhh5BOmenrcmtjtqz_V_tS_H3xBKsHM9Q6ljapUmWzWtT4umf8wX8G7DllqbsvICcn02Q4B0pHq1sRPq4wcQd7J7wCkWUn-QuuZfi-5dTiOKzC2rg570X0qAp5_XMsaQEBINoP9_ujZjLQgE2TVUsq-N5UMMVCnsp5sO0-fBjvnw7Ho-s2LT86pmGvVcGIe4V9hzpTfJ11vdqUKcOlrwJ1w5upw0Z8aEKuWisH6wC4VhEwV-UJKKzEUyibLI3XkjXmOkBdIwcgZDY2MmwXPZKl-Euyq2ypL8Sp3bHnGI6wp500PSTcVst4bwgpcmLf_4nEONGs659kQ3YLpbQxc6tjSd5I81b7BjjNVCfelvB0IVdWpdXaGYONuIKuslKZKgVIBQW9cCpJfRNFCmox8DBDwp_Eox0Swurnv6Ly1vQ6wWVNPeJu5xT4U7OlcfVg3bcOfp6IjvqJnllx5J0Bx4ZWcc0HwhdChz5Sw7r5fkMLS_whV1wY3CvAg-mjIZ__Z38A9EJAzhPQIeBgeo8sFKtCpA0YFr3S-zqzt3j-TdhcoWwGnEo5_1JjEse9CpQaFVbVVkWkYIRGlMK93feHZc0Ru0Zoxddqm7P5u0Ro2SVy2gBmoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa16d263ca.mp4?token=eBx38funACo3kaPTb5P8dmfAIkC6a_tm5ZIfi06PYQasKvNSUqQwM6UbbNqFhh5BOmenrcmtjtqz_V_tS_H3xBKsHM9Q6ljapUmWzWtT4umf8wX8G7DllqbsvICcn02Q4B0pHq1sRPq4wcQd7J7wCkWUn-QuuZfi-5dTiOKzC2rg570X0qAp5_XMsaQEBINoP9_ujZjLQgE2TVUsq-N5UMMVCnsp5sO0-fBjvnw7Ho-s2LT86pmGvVcGIe4V9hzpTfJ11vdqUKcOlrwJ1w5upw0Z8aEKuWisH6wC4VhEwV-UJKKzEUyibLI3XkjXmOkBdIwcgZDY2MmwXPZKl-Euyq2ypL8Sp3bHnGI6wp500PSTcVst4bwgpcmLf_4nEONGs659kQ3YLpbQxc6tjSd5I81b7BjjNVCfelvB0IVdWpdXaGYONuIKuslKZKgVIBQW9cCpJfRNFCmox8DBDwp_Eox0Swurnv6Ly1vQ6wWVNPeJu5xT4U7OlcfVg3bcOfp6IjvqJnllx5J0Bx4ZWcc0HwhdChz5Sw7r5fkMLS_whV1wY3CvAg-mjIZ__Z38A9EJAzhPQIeBgeo8sFKtCpA0YFr3S-zqzt3j-TdhcoWwGnEo5_1JjEse9CpQaFVbVVkWkYIRGlMK93feHZc0Ru0Zoxddqm7P5u0Ro2SVy2gBmoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخریب گسترده در جنین توسط نیروهای اشغالگر صهیونیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/659214" target="_blank">📅 12:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659213">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
اعلام جریمه مخدوشی پلاک در پایتخت
معاون پلیس راهور تهران:
🔹
جریمه پوشش پلاک ۷۰۰ هزار تومان و جریمه نداشتن پلاک جلو یا عقب و همچنین ناخوانا بودن پلاک ۴۰۰ هزار تومان اعلام شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/659213" target="_blank">📅 11:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659212">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس انجمن تجارت الکترونیک: نگرانی درباره دارایی‌های دیجیتال بی‌مورد است؛ تحریم صرافی‌ها شامل کاربران نمی‌شود.
🔹
ستوان سوم حسین رسولی در درگیری با پ.ک.ک در چالدران به شهادت رسید.
🔹
وام بازنشستگان تأمین اجتماعی افزایش یافت و از تیرماه پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/659212" target="_blank">📅 11:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659211">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98197c2078.mp4?token=h6c1BhZiBvTL2oyV5-PFw9qx-LbVR2lGMFQ8ms4Ll_Bzz_TbTPtCHwnnWqQ0TbXKuRvqkSxZ8VX2BeRPDlVge4kGavvae9KGNMXyrnTxAjF15eMMHgfd_YiwV8X-TQGbWC3-6pJOvLev-tZkt6AAxgI4brVki0ss4yrEzcBySaLDe8REzmUHUlHDzkwDdq8R5GpvMRyYT6bImHir-KY4o6E34Ubw9ZMABqkv4dE7CSxsmyZEJYmI-zXu1PZYfRLG07RhFoO3fTeIybm88QXEJu2AlwH6oq6LZ_0m95l7abMbmtDlRDi3C_mW6G_eFAG0DAdQxtS_ki52iC_kbm1BQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98197c2078.mp4?token=h6c1BhZiBvTL2oyV5-PFw9qx-LbVR2lGMFQ8ms4Ll_Bzz_TbTPtCHwnnWqQ0TbXKuRvqkSxZ8VX2BeRPDlVge4kGavvae9KGNMXyrnTxAjF15eMMHgfd_YiwV8X-TQGbWC3-6pJOvLev-tZkt6AAxgI4brVki0ss4yrEzcBySaLDe8REzmUHUlHDzkwDdq8R5GpvMRyYT6bImHir-KY4o6E34Ubw9ZMABqkv4dE7CSxsmyZEJYmI-zXu1PZYfRLG07RhFoO3fTeIybm88QXEJu2AlwH6oq6LZ_0m95l7abMbmtDlRDi3C_mW6G_eFAG0DAdQxtS_ki52iC_kbm1BQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلاتان حوصله یوتیوبر معروف را نداشت
🔹
واکنش جالب ابراهیموویچ وقتی اسپید(هوادار معروف رونالدو) اعلام کرد پرتغال قهرمان جام جهانی ۲۰۲۶ می‌شود
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659211" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659210">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arGpOfInir8dh9IGlHPkhcqjjsRJ2ly7_vHhkNCiVSPURWk2buH2PZ6ZsDbpmJ4i2BxsgyG_2Csvtqgr1FpUMQASW_AY-aaNFO7XMR4D8A9ND1JVX5OAkzUJqm0mbE-053wPKIqwQyMp2QsosrNqAWcmA0Ew0ct64T-JQKaa6uMikZoixjjsQhQGjPGEL0uNlzFnlodPa1No3cPo00X0IxQnBdwS2cKgf8fi-h0oPMIpwYq7F6CnBFV6b_g4ZXbdqnS5LFi_W-_-9EL_rKv12mAXWlhz53ZHhavKBVWrhPryZ5SPfH3L16LYem6GjW23ceCrxmNyoDUwToDYwDRPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ کشوری که بیشترین مصرف نفت را دارند
🔸
آمریکا با مصرف روزانه ۱۹ میلیون بشکه نفت در صدر جدول قرار دارد و به تنهایی بیش از ۲۰٪ مصرف جهانی نفت را به خود اختصاص داده است.
🔸
چین با ۱۶٫۴ میلیون بشکه در رتبه دوم ایستاده و با سرعت بالای رشد اقتصادی، فاصله‌اش با آمریکا روزبه‌روز کمتر می‌شود.
🔸
مجموع ۱۰ کشور برتر جهان روزانه بیش از ۶۱ میلیون بشکه نفت مصرف می‌کنند؛ رقابتی که قلب تپنده اقتصاد جهانی را نشان می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/659210" target="_blank">📅 11:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3J-OQF-R8adso2phOzbSi6tNveauro6xSw3omWcNaeMXEBIOJCZtS0UFTRXTdGxCMoer9Hj_GdQSqy7W1aau81rfB64m-QeSozp2hSDe3vNoK5E2M5Y3RP1Bz4oY-7BNz8fdzYI1Y-KEe2mOXhloBJroMX84SytWeV-Tng35O0OWx2rxnXkkNnM0CW5fa0NCiHwK4b8pE0teS9Tgki5UvpXq--ZQCKJeYy4b2A9lLqP3Z3SCkv-eqO4XFq4EujgLhOlUC_ro0iGw-srTt6A5e0BjpdyF_9n7jt_93lgHkFQtc7dFnmhe6sL1y05zWlPXjFHGBdhM8iIwoRUXUrNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2V9PGWgGNyEOArPxb9lN4mxovDDjiMJBaHL7h5dwLbVx1RE2WKaerulpTwwcDvY0Sdg4LI1CXj6QTa1nEaaD0GPPGFxY9A91UFYCTgGvtQI_Q8bKVGlRFEuGOJAXFpSzveCJvy4i7SihosL5MgBKuZs6Ltq3BBHfB29DyEh7QpI36ENuj8w0U9Qlp9_tyBGnvAcfE5XC3x_RpUOyCQ-qFLyhJq6gjoQ0zC4KBrxyJU7l1ijVLtA1GPWnvEnvhxhHvltfV8fgiYip_TY6U9H2O_ZyCdLhGPskEaPkBzGJBnTJeu_fWBRcI0NPlT1hH_9Tpa5v90CVU_FFX-UrLmcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHvBUzOTkuI2CbyjWfsMbNiud28EiwfdJw5FKzUZD57Q21azQ-1eEoCUXRY33Fe4lyahTrZxCeFjuB3t7zXTNW7W21BprZ64_WM67Z29p81QwEs3YWrZJn65XwFxlEo37lW-4SoxQ276vTFJUaT8bgQNO3i4kpYL_xB7tT2ZaxEqEs_9TQdSyKe6y54wh9QFDjmNKHplFDS5ii6vO2JoiB1KWVh2mNIIBQvwnXGEUoTrlvxfTsq3SMrB7eE_h_9TSg1CNL1vG9Ay9VIftT_Qx9jZWjT_BfWtkKIUwJbmnIsV717sq903v1AC__1JJVTM4cqQgQxQKB9VyE7UB_kb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJcntOSt5wjmu90lJKzZDpZrZYpsNT6_gb5hhFZvq8TVFGVKRzFD-x8m6dhjYmy2OAtviYzeC9hems2DWXiuXRv_AclqL5OHfA4kqIIllVqAm2Wuh9WG_eZluwAPIEd2pPbbEnFeShvWUw4KJvnc85c0kJ83Dp6IXGpMy7yX8CBoz4BWrUUJPb-WRE6ATGXlNBzLByrWrINapq968BpJnMJjhRk_6UryrZ4STbuKIv4GGGaRrpkwCn92DY1m-pms4aaejWs5Ff6n9Bd37SGtR73T_zKHs43joi_K4sM3v3pmDlTcdWz_AUEsGi_7CCyUZUTWxh4FlHtn247-9KO2bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر جدیدی از ماکت اولین آیفون تاشو اپل فاش شد
🔹
تصاویر جدیدی از ماکت آیفون تاشوی اپل منتشر شده که طراحی آن را در حالت جمع‌وجور و تبدیل‌شونده به تبلت کوچک نشان می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/659206" target="_blank">📅 11:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
بورس از ۴.۸ میلیون واحد گذشت
🔹
شاخص بورس تهران در نیمه نخست معاملات امروز (یکشنبه) با رشد بیش از ۱۰۶ هزار واحدی از مرز چهار میلیون و ۸۰۰ هزار واحد عبور کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/659205" target="_blank">📅 11:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وکالت‌نامه‌های تعویض پلاک تا پایان خرداد اعتبار دارند
🔹
رئیس پلیس راهور فراجا، از تمدید خودکار تمامی وکالت‌نامه‌های تعویض پلاک تا پایان خرداد ۱۴۰۵ خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659204" target="_blank">📅 11:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
مشکل خدمات بانک‌های تجارت و صادرات رفع شد
شرکت ملی انفورماتیک:
🔹
طبق آخرین گزارش‌ها درپی اختلالات به‌وجود آمده در ۴ بانک ملی، صادرات، تجارت و توسعه صادرات، مشکل خدمات کارت های بانکی بانک تجارت و صادرات رفع شده و تراکنش‌ها با موفقیت درحال انجام است.
🔹
موضوع در بانک ملی ایران درحال پیگیری است و آخرین اخبار اعلام می‌شود؛ در بانک توسعهٔ صادرات هم شعب آمادهٔ ارائه سرویس‌های ضروری به‌صورت حضوری هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/659203" target="_blank">📅 11:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
مبلغ کالابرگ و یارانه برای اقشار کم‌درآمد اصلاح می‌شود
معاون وزیر امور اقتصادی و دارایی:
🔹
دستگاه‌های اقتصادی مکلف به برنامه‌ریزی برای اصلاح عدد کالابرگ و یارانه به‌ویژه برای اقشار هدف هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/659202" target="_blank">📅 11:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659201">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b2e17333.mp4?token=WvMvKwGC8MHQTX-EZC2uNI8YBcWK5Fm-BVUmyeomVHC182QBckYPVg1GBlEmVBBqRX5oY4GyKWKMcRycP5dG76p8Bzsq_8009aGdrdb_kKCc87CUYJhUaDadjpj2hW15mkQdr2Z5Dp8AqER3pwnLZrGymqeCreer5ayOGSxuYE9c2HeK23LSR7OnccnEiM0OHoiRc2doPuPCcJarElcXbTsubnIp7ZEi3zCzBTQQYRCUbTzs3rRGgguy3HL3Ux3IrRS36RRZaGNl2fJCXYIPzwGM3edoosDtCOLj-H1xFjLZaiCxrLDNpc3WAsNaVh2yBxKmm5V-Rx4rUmU4KzXfDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b2e17333.mp4?token=WvMvKwGC8MHQTX-EZC2uNI8YBcWK5Fm-BVUmyeomVHC182QBckYPVg1GBlEmVBBqRX5oY4GyKWKMcRycP5dG76p8Bzsq_8009aGdrdb_kKCc87CUYJhUaDadjpj2hW15mkQdr2Z5Dp8AqER3pwnLZrGymqeCreer5ayOGSxuYE9c2HeK23LSR7OnccnEiM0OHoiRc2doPuPCcJarElcXbTsubnIp7ZEi3zCzBTQQYRCUbTzs3rRGgguy3HL3Ux3IrRS36RRZaGNl2fJCXYIPzwGM3edoosDtCOLj-H1xFjLZaiCxrLDNpc3WAsNaVh2yBxKmm5V-Rx4rUmU4KzXfDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۴۴ سال انتظار برای یک شاهکار...
🔹
یکی از بخش‌های اصلی کلیسای Sagrada Família در بارسلونا، شاهکار معمار آنتونی گائودی، پس از ۱۴۴ سال به مرحله افتتاح رسیده است؛ بنایی که امروز به‌عنوان نماد صبر، ایمان و نبوغ معماری شناخته می‌شود.
🔹
ساخت این بنا از سال ۱۸۸۲ آغاز شد اما گائودی در سال ۱۹۲۶ درگذشت و پروژه ناتمام مانده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/659201" target="_blank">📅 11:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4O2noF8uZ57_c07ryl4usgeTz7XgJ37D7u-dedjUmhlrbLUwEntYl6YE-vDAnhZS8DRyDckgjAQAM8kiG9mEar2mog11X_qcqFkWIgIp5OF2pg42F8NR6QGOV6JoMedel1yi7cCL0G7H_0gPp2L8e7zUIA3Mx8SdV_RylE5xDHwvXR90GfZlak3COuQwsF3wq-f6BQXMbpW49QIZUXhT9V9JJkwFuFtkwubuvo9Lb59xHxhYXfFH-RQwsJ_XiDCWXlXpwO-vzGo9e9uxjPOn9bc_XiEWME4LDUOQQkRUIZKavyd_etNDj-doQEN0u4KjsM5E_40_KkGbn_LK0dOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جام جهانی در حیرت قدرت‌نمایی تیم‌های آسیایی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/659200" target="_blank">📅 11:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
منبع آگاه: تصمیم نهایی تهران دربارۀ تفاهم‌نامه در دست بررسی است
یک منبع آگاه:
🔹
ایران هنوز تصمیم نهایی خود دربارۀ تفاهم‌نامه پیشنهادی را اعلام نکرده است.
🔹
بررسی ابعاد سیاسی، حقوقی و فنی پیشنهادهای مطرح‌شده همچنان ادامه دارد./فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/659199" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659198">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
حمله تمام عیار لاپید به نتانیاهو: برنامه موشکی ایران پابرجاست، تو بازنده‌ای!
🔹
یائیر لاپید، رهبر مخالفان، از توافق نوظهور آمریکا و ایران انتقاد کرد و در توییتی نوشت که «هیچ یک از اهداف جنگی اسرائیل را محقق نمی‌کند، حکمت پابرجا می‌ماند، برنامه موشکی پابرجاست و ایران می‌تواند برنامه هسته‌ای خود را بازسازی کند.»
🔹
لاپید ادعا می‌کند که این یک «شکست کامل» از سوی بنیامین نتانیاهو، نخست‌وزیر، است که اسرائیل را به «کشوری تحت‌الحمایه که در مورد امنیت ملی خود دستورالعمل دریافت می‌کند» تبدیل می‌کند./خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659198" target="_blank">📅 11:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659197">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5a5fc9c9e.mp4?token=odhGsg_OOklQV9fkf946KOvAeEZU7bPMLOibbFPZGmaRS_1ZW3ytPMwrMXc2ZvviTQHZaGjSNkL217dBgJSUP3H7wkyMKE5u1GZY32kboeP2xjM4V0TutrQtvN-V0KepdO5OYC7mRzapsNHVzVPqeZUi-gqnVl8WfUzbgK3c1ihENcHuroXE4IFwAnuL8N9SZl7-XvblYhVDg-WmnAxl5awP1kRGLDgc99y86k1DsoI1MoHDJ0tIdHyOyI6mpDt_eHDMy80H4yP9ygFbbwmUI8fjOhX4mZklHZxsLS7kXODYNSvKXkfMGMLZjwMFRt4IwNsaKoSlYzCGS2q7KxML95YFmpYG_4vAwbzxMhEZKiKJwNAyoD6Hf8I2fUxxC2fiVy7oOFU1YuKUOoUhquK5eSE0gKkZKXHzyWBGgsXhiqDFIeMb4W7UBitNborzNrDUlRnH0rDK7P2jRgx3HtiK2ywFtnBxhTFL41Yu9z__s1cP_bv67Sq-JR5dmMICcY0gOLnwm1nkB6-cgiev47X0MO59uoH-aqkVvPraYwjVLPFfdN_iLOLzkyExjSxBBiejhX3OOqWmcWYlQxCrui322hQ086FbG9r-DaXU5O3ayIoqAMQGtuXhPKpB72vI_5WUxRq7qeMTphSEyGNhT-zW4BaGPjjyB0Hi-smmktTNpK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5a5fc9c9e.mp4?token=odhGsg_OOklQV9fkf946KOvAeEZU7bPMLOibbFPZGmaRS_1ZW3ytPMwrMXc2ZvviTQHZaGjSNkL217dBgJSUP3H7wkyMKE5u1GZY32kboeP2xjM4V0TutrQtvN-V0KepdO5OYC7mRzapsNHVzVPqeZUi-gqnVl8WfUzbgK3c1ihENcHuroXE4IFwAnuL8N9SZl7-XvblYhVDg-WmnAxl5awP1kRGLDgc99y86k1DsoI1MoHDJ0tIdHyOyI6mpDt_eHDMy80H4yP9ygFbbwmUI8fjOhX4mZklHZxsLS7kXODYNSvKXkfMGMLZjwMFRt4IwNsaKoSlYzCGS2q7KxML95YFmpYG_4vAwbzxMhEZKiKJwNAyoD6Hf8I2fUxxC2fiVy7oOFU1YuKUOoUhquK5eSE0gKkZKXHzyWBGgsXhiqDFIeMb4W7UBitNborzNrDUlRnH0rDK7P2jRgx3HtiK2ywFtnBxhTFL41Yu9z__s1cP_bv67Sq-JR5dmMICcY0gOLnwm1nkB6-cgiev47X0MO59uoH-aqkVvPraYwjVLPFfdN_iLOLzkyExjSxBBiejhX3OOqWmcWYlQxCrui322hQ086FbG9r-DaXU5O3ayIoqAMQGtuXhPKpB72vI_5WUxRq7qeMTphSEyGNhT-zW4BaGPjjyB0Hi-smmktTNpK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شو اسپید متوجه نبود که تمام مدت کنار زهران ممدانی، شهردار نیویورک، در بازی جام جهانی نشسته است!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/659197" target="_blank">📅 10:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659196">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd17cd5474.mp4?token=u7V93XYjoe0n_Pe-iGlzO62YxrbIdX7iTsNNIs0D5OQZ8jrP_nvQ--KSQuyrZofZ9sjES7iL91zjRh_bDdkBaEfkPTQGuLU_TyyX8H1G_EvAnn0ifPauktSaO9Vl8YXyxzgB3rMpbBIQW-5uPMD8RlGGDAYty0okr0aiwS6umCaPEmuZP1umV_5DzPxUSUQrCXI3AIHas6gG5gMeZCI5tArc0l9VkCoSZxiw8vM3WSDlOZhsd_HRfSEQRp_EVc5zxRK6PA5LReX3xvMnOdYRAU3Sf-1ekNx-cuss7cGWEf37tWD_8QHN70YlyuZj_-LZc7LwI_gye7gfMe1Ktu-r6rHSLCF-uS1k1LjahhSrDTlwepjBHTQ5ZK_9nAvnx1-myLxz1qI3Ab7ikynqAL7OP32TpWA1V_N5X847LIk2NjLxzyPxXIlH9WHXW11wkMwrd3kEfBEryiqfgbHakFUEivpprJNmmZEnNDPATpjkbcRZRLDf46jLddWZdDjdeAtX0_zGEZT6o1UEh7uX_V04ZwJxOneWspsFVadaC6L7aKQiRBVDTTpPnN8KmAhbT1jz0rlIgzzFkmi-b3kOeAqnhXURJLkBj907YLdCUs4kzP9TeNLWOLSGKMwejbnSzsrFYGM0Ua4PE7aun3IVbu7JAUDe83kfMVYhGDT7bcvhY6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd17cd5474.mp4?token=u7V93XYjoe0n_Pe-iGlzO62YxrbIdX7iTsNNIs0D5OQZ8jrP_nvQ--KSQuyrZofZ9sjES7iL91zjRh_bDdkBaEfkPTQGuLU_TyyX8H1G_EvAnn0ifPauktSaO9Vl8YXyxzgB3rMpbBIQW-5uPMD8RlGGDAYty0okr0aiwS6umCaPEmuZP1umV_5DzPxUSUQrCXI3AIHas6gG5gMeZCI5tArc0l9VkCoSZxiw8vM3WSDlOZhsd_HRfSEQRp_EVc5zxRK6PA5LReX3xvMnOdYRAU3Sf-1ekNx-cuss7cGWEf37tWD_8QHN70YlyuZj_-LZc7LwI_gye7gfMe1Ktu-r6rHSLCF-uS1k1LjahhSrDTlwepjBHTQ5ZK_9nAvnx1-myLxz1qI3Ab7ikynqAL7OP32TpWA1V_N5X847LIk2NjLxzyPxXIlH9WHXW11wkMwrd3kEfBEryiqfgbHakFUEivpprJNmmZEnNDPATpjkbcRZRLDf46jLddWZdDjdeAtX0_zGEZT6o1UEh7uX_V04ZwJxOneWspsFVadaC6L7aKQiRBVDTTpPnN8KmAhbT1jz0rlIgzzFkmi-b3kOeAqnhXURJLkBj907YLdCUs4kzP9TeNLWOLSGKMwejbnSzsrFYGM0Ua4PE7aun3IVbu7JAUDe83kfMVYhGDT7bcvhY6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوت دیدنی؛ گل اول برزیل توسط وینیسیوس در بازی دیشب بین این دو تیم
🔹
برزیل ۱ - مراکش
۱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659196" target="_blank">📅 10:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659195">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea5ec3ad9.mp4?token=Pp0y2Vs2J7aDltYywM6ZwFldhgRfPJwceo0mo7nc0EevF7HQgAtpna17d89hoiD3iJmtH5kIbxk3gyqYegKOsONRrA4rafrYcSQvT2wJMmHJccxwDzy4-I695RGzoyl2nZEpx1szyEP78P8xAdVaSy6ja6sDV6p7dZkPyuBc11TYEN_AakKccbQ8dXJZEr45zBSzuj6ah_5c-N38Wv-toMSbIc4ZIfLEBXNizmAgwICitxlkch0lrcd6dx70DE1ukCTad9ZLB17U44LrTLGQockiYu50410WeG8daOeYItPCdlRxtqu8dNFRO-PKHcSqcgZSwOI3L1elHY7J1Xj5YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea5ec3ad9.mp4?token=Pp0y2Vs2J7aDltYywM6ZwFldhgRfPJwceo0mo7nc0EevF7HQgAtpna17d89hoiD3iJmtH5kIbxk3gyqYegKOsONRrA4rafrYcSQvT2wJMmHJccxwDzy4-I695RGzoyl2nZEpx1szyEP78P8xAdVaSy6ja6sDV6p7dZkPyuBc11TYEN_AakKccbQ8dXJZEr45zBSzuj6ah_5c-N38Wv-toMSbIc4ZIfLEBXNizmAgwICitxlkch0lrcd6dx70DE1ukCTad9ZLB17U44LrTLGQockiYu50410WeG8daOeYItPCdlRxtqu8dNFRO-PKHcSqcgZSwOI3L1elHY7J1Xj5YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مراکش به برزیل توسط اسماعیل سایباری در
بازی دیشب بین این دو تیم
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659195" target="_blank">📅 10:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659194">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a411a8ae.mp4?token=v3HcfkDkYChmTm8psL0Mgu0le_cMvZgWjj71bV1VgFfLNXNmhWBO6uVTIOXEOOrnHvNhOORvL0HLp51SIjXt8L03WetziKye4RjQfCcvSDAXw1bmPwFCSbMbZx1Kpv_Z_8JZOUFjrVEhWjwMkiGcOmNn0Ot-kU6tEY_Jr_2IWhC2UOcTeOWVJQpYqrhqg5ubtZqztwOgV87LEbymekPIUAio6ZQ2vxymbHYgucP-1eOUbU48vQmKd5L5bXjPX0eaCDGKILyFg0Tb9X3ZbpjyFbjRlTqALpbRAyORRdYZ4kvfMBkod1e2TYzPox_SGsiMZgRC8E_rZHxgmvl0k8Mw8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a411a8ae.mp4?token=v3HcfkDkYChmTm8psL0Mgu0le_cMvZgWjj71bV1VgFfLNXNmhWBO6uVTIOXEOOrnHvNhOORvL0HLp51SIjXt8L03WetziKye4RjQfCcvSDAXw1bmPwFCSbMbZx1Kpv_Z_8JZOUFjrVEhWjwMkiGcOmNn0Ot-kU6tEY_Jr_2IWhC2UOcTeOWVJQpYqrhqg5ubtZqztwOgV87LEbymekPIUAio6ZQ2vxymbHYgucP-1eOUbU48vQmKd5L5bXjPX0eaCDGKILyFg0Tb9X3ZbpjyFbjRlTqALpbRAyORRdYZ4kvfMBkod1e2TYzPox_SGsiMZgRC8E_rZHxgmvl0k8Mw8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسابقۀ کشتی در آمریکا به میدان جنگ تبدیل شد
🔹
آمریکا از سال ۲۰۲۵ اقدام به برگزاری مسابقات کشتی آزاد تحت عنوان RAF کرده که در آن خیلی از ستاره‌های مطرح جهان هم شرکت می‌کنند.
🔹
در یکی از این دیدارها چیمایف از روسیه به دنیس از آمریکا لگد زد که منجر به درگیری نمایندگان دو تیم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/659194" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659193">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: مذاکره‌کنندگان قطری برای نهایی کردن تفاهم راهی تهران شده‌اند
🔹
شبکه آمریکایی به نقل از یک منبع مدعی شد که مذاکره‌کنندگان قطری صبح امروز در هماهنگی با ایالات متحده به سوی تهران پرواز کرده‌اند تا به تسهیل روند نهایی‌سازی توافق (یادداشت‌تفاهم) بین ایران و آمریکا کمک کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/659193" target="_blank">📅 10:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
انتقاد البرادعی از تقلای ترامپ برای بهتر جلوه دادن توافق احتمالی با ایران نسبت به برجام
مدیرکل پیشین آژانس بین‌المللی انرژی اتمی:
🔹
ترامپ به‌شدت تلاش می‌کند نشان دهد که توافق جدید او از برجامِ "باراک اوباما" بهتر است.
🔹
در حالی که به نظر می‌رسد این توافق چیزی جز بازگشت به وضعیت پیش از بحران نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/659191" target="_blank">📅 10:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای الحدث: یک نشست مجازی میان هیئت‌های آمریکا و ایران با حضور میانجی‌گران پاکستانی و قطری برگزار خواهد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/659190" target="_blank">📅 10:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
الجزیره: ایران هنوز تصمیم نهایی خود درباره تفاهم‌نامه را اعلام نکرده/ می‌توان انتظار داشت که توافق امروز نهایی شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/659189" target="_blank">📅 10:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
معاریو: ایران پیروز بلامنازع است/ نتانیاهو شکست خود را با سرافکندگی اعلام کند
روزنامه معاریو:
🔹
نتانیاهو باید در مقابل افکار عمومی بایستد و سرافکنده بگوید که من شکست خورده‌ام و حتی بهترین دوستم (دونالد ترامپ رئیس جمهور آمریکا) هم برایم ارزشی قائل نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/659188" target="_blank">📅 10:15 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
