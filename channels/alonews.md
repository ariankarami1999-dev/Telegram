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
<img src="https://cdn4.telesco.pe/file/iaWB7MDc1dHliDQK12R5YMtpS238bEoVQnNmumkkh5omoqvLj2TpbFhntFyrY1BwfcoB6ArxdbAZXEDqeB9LWNS6t54FGSftMwMuLJi5_sOemfddCl_4bHYn_zchxcs5LyzsRZnPUMUbxy5sNyNdZzfG54q6JgQ7-ftSrGH971jdbih_FWRw1YBJm-ZJ4PjlyJv_MgyQUqrTasQLPaZJ1unYqYCE-v2Se5XK3xpOs6-pjAUj9XMydxpgpHmramLfzXouAvVa2tBwiAX_l12-vaL2Xeb6OQl6gnWhRSyBQsWsGx3fB8H3LRmDel7pSr1QrYwSACwg8c3MhWx2cC2aug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 988K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 23:45:18</div>
<hr>

<div class="tg-post" id="msg-143091">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKDv8WbpemiXCR-YhIlpBzmDhG1_Rt0Y_u4__IlWKB9Jw67eD3769OFo9yZodvjSVBoCBLC2eEsr9-bzSYQN4vGlUjXpjcAYNsM7FFOtrA55JUJbTzrJBPVL82dRuclMZgyVIP-CoBBgiKBlS76U-t7pfLsefhX6vcocPQ9llM0nHzy7F0mRsC-grXOy2BYQTil2vmA4wwWxC6ITpuKKtJA2uiTwxyyUq5JAFayBAo3B76rXFoGve59jQlAfAYdjIy0sbugCpkyDTOcX_kOmxuJJG9otT2umUkh61ODUubAACjqeAOYTBlI_-mgqglJxPNHBtcimVBBi0DXu9MW9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی جنگنده‌های اسرائیلی، تپه علی الطاهر در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/143091" target="_blank">📅 23:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143090">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
حسن‌نتاج، نماینده بابل: ما نمایندگان نسبت به بنزین ۱۰ هزار تومانی نیز معترض هستیم، اما دولت به دلیل شرایط موجود بر اجرای این طرح اصرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/143090" target="_blank">📅 23:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143089">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
گاردین: ترامپ برای هرگونه اقدام اقتصادی جدید علیه ایران، ناگزیر خواهد شد شرکای تجاری ایران، به‌ویژه چین، را هدف قرار دهد؛ همین مسئله رویکرد آمریکا را دشوار می‌کند
🔴
سفر رئیس‌جمهور چین به آمریکا در ماه آینده نیز ممکن است تلاش‌ها برای اعمال فشار بر پکن درباره واردات نفت ایران را پیچیده‌تر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/143089" target="_blank">📅 23:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143088">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
به گزارش فایننشال تایمز، اوکراین به دنبال کسب مجوز از ایلان ماسک برای استفاده از پهپادهای مجهز به استارلینک برای حمله به سکوهای پرتاب موشک بالستیک روسیه تا عمق ۲۰۰ کیلومتری در داخل خاک روسیه است، چرا که کیف با کمبود شدید رهگیرهای پاتریوت مواجه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/143088" target="_blank">📅 23:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143087">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تصاویری از پهپاد های فیبر نوری روسیه در حال درگیری با نیروهای مسلح اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/143087" target="_blank">📅 23:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143086">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
سه تا از گیم پلی های لو رفته جدید gta 6 که هکر cyberleek ساعاتی پیش گذاشت و چنلش تو تلگرام بسته شد  برای دیدن کلیک کنید
🔴
اگه دوست ندارید اسپویل بشه نبینید  @TitrDaily</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/143086" target="_blank">📅 22:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143085">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1ApP8FsNlX1YPQtMOighCUTHfMpXbaeCxBKUWUjVdZta572K1-HJI0EAXGpEpSNl8FAf0tsE8pRgs2IAJaTMWNgbrVpT0Hei8ZfY0O7AeWMdKJG0MD6YpK1ekkusozJDQAIzDyF8ffWswQcgpJbtqh-xlbkqa-Kz-1xdH9ub_aH4nVP3L3YobfhQLsJmKK-Ol4IqCexzXryoikAyqGh9eNvXlkrtDTJEQ09f4sFvXYaMP-z8dNLqUpS5EWZt8IlQLQON2jZg5YB5ynGQsK-G7tOA761ULhmAeN6VD5qfC6_C3UCBV4-qarCSctFNhqPxPpwpRgYcMVBy3bTynctBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر یک روزنامه سازندگی:
صادرات نفت؛ صفر
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/143085" target="_blank">📅 22:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143084">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1b5z16pvZaYcFK5iLX6FfXiZzjNOQku6fYUfsPiXTgg4iZdWeFhvuNnLv2qhNbShoZbqyq1ixTBn3UyMBqsUJU-1C65YxmGjBldAkoKoB69YEciOR25JEaVEnWCbKPk4NgKBjksuKu1_RHYBotqs5iYXy6DGYUihXgkrFdA6WlL27UIxCS5zS2beMjLqc1ENPBljoFKvhbBfzkiGdnug6TuG6f6LPBPzOG1d84wBHak4OAVr0tivELFVrnKALK8_tL9CuWs-Iu7VZUEkbe0I6xEaFxfVJMUAdRV_GdsL2YLqPTHa-1adxZUEeTpSh5Mt1tz5cB8QFwlQ3HqQJXLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت‌های نظامی گسترده آمریکا در نزدیکی تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/143084" target="_blank">📅 22:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143083">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نخست وزیر عراق: قصد داریم تولید نفت را طی شش سال به ۱۰ میلیون بشکه در روز برسانیم
🔴
بستن تنگه هرمز چالش بزرگی را ایجاد می‌کند
🔴
ما در حال کار بر توسعه صادرات نفت از طریق بندر جیهان ترکیه هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/143083" target="_blank">📅 22:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143080">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH8J8ZAI2ek_kTG3Zcrk78ZAsHO7csUZcpWqobTp8R13CMxscC_UE4ILm9iZ_mJG-G-j3M9AIcF_D4xr8mL0p-5fe38YA0wq4kn2Mr_EATnNShU8OWJN8n0ejI0yO-IkSwGTS4uN8cDVWy43jQ_kw3_I3x8OjYr-xMqI73imK1clVK4QWAXV8Ou0GH33kF8E3E6fEjME8iuZvQMOmv8wd6eH9UeMZCJ18OAqdSoW4NaaG4WQq0NWKwRiWbmKQhBuQW4e-3VqwdTCMDd-EKl4LikQRmGpyixs3Fa-VA5AW8xJzb8Wt147zSTX5BIa8BgpGsfMLeLhElOa2zfxmmqOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iixdTFUrj5aVpkeiPBlLn6IS-RQFQOiVCpDcdrJyZmaoY3c7GBDuGQqjmnrSxGGc-_IdxXhcA3toZP2SeJaAJsS8JXIrMxaJBkTiOZU9avl4d6wMgm9OHojKVK2p6PTLF15sx23tsCMPt8n0pNTzWweCiakZq_VhPr9gq-FD7iGzO8C8D6xC5XEaOcacgLmh-rRWq_i0eX7fMtxh9w65jDLKwxtAeYbXLFDXH_0kLrRUFTtOUICy35T8XDpN7wPIMTbRb9fk2OUwy6Ae6TDGpMNjEt-ZLb6m-feFS4zpqjl59sr-eHV7RwLazrgwFvjpnK4By3bCI6lJ8cIlKnbTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpqDHSsN-NXkNBJBaEA6Tuw84_84g42IDIWmn03ijD48PZdpV7yUb4jfsYsSyVqPgGRYXmVE0Hu45S0v0zR2ScMXn7TQxFZm1mZa6aHnzY8ooaV26LCD958aFaTq9GPshI2T0FCvCCzuxlQ0i8P6B96PcYPbTSx4crisoZ0umdh4H9_r1P48gJejfCRWy__sKM78FA-VsI2XzkPhw92xWE5VXZXevl7Ym8WDWJ98jHUBkN_FIqFFRC2oKDJSOWsWwbHbIpPGQPReVTdBw-UKK1l6kFLGYEKkv7NK386i9UsE0zr-wjQNwPMGQzbsuvJB6wnQcZ9vDktCgK2lHwSY2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک پهپاد عمقی مدل FP-1 متعلق به اوکراین امروز در سواحل دریای سیاه، در منطقه کارابورون، واقع در بخش آرناوتکوی استانبول، پیدا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/143080" target="_blank">📅 22:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143079">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
الجزیره: هیچ نشانه‌ای وجود ندارد که پکن قصد داشته باشد تحت فشار آمریکا خرید نفت ایران را متوقف کند
🔴
پکن وابستگی بسیار شدیدی به نفت ایران ندارد و اگر واشنگتن فشار کافی وارد کند، می‌تواند خرید نفت ایران را متوقف کند، اما چنین اقدامی برای رئیس‌جمهور چین، هزینه سیاسی قابل توجهی خواهد داشت
🔴
تسلیم در برابر فشار آمریکا می‌تواند در داخل و خارج از چین یک سابقه خطرناک ایجاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/143079" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143078">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e316f6b04.mp4?token=Kc4qz6SX9T4NwR4yHrSETAOen98d3LRFL2_VBQDLKzs3bw-q-NXH_Tc2IcBnD495SOqbzWpm06l_Hcfqj8y-4ZiWTkbIgCyHP1Rftb4seaZdv2TGhjyOdxZ83F-AX4z_d0PFUMRr3Jb3zs4MMNDu61gWkXatLTwlcWmeIRtgihaWJNDNx4aq2ZPuyZopo0yCzhW403SC5KC2eipa7XZQM5OfVgUbTYaRImrC5OZswCfn6U_KgyrkLlblyfJsvpxdRTUNLFr2yEwEMXYSKCZzRnL1IHwp5rlCFUNPo46o6kEXiLQC1B3dkztAAOJ7TYOMGyndNKwB2nxyojcPTS3PVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e316f6b04.mp4?token=Kc4qz6SX9T4NwR4yHrSETAOen98d3LRFL2_VBQDLKzs3bw-q-NXH_Tc2IcBnD495SOqbzWpm06l_Hcfqj8y-4ZiWTkbIgCyHP1Rftb4seaZdv2TGhjyOdxZ83F-AX4z_d0PFUMRr3Jb3zs4MMNDu61gWkXatLTwlcWmeIRtgihaWJNDNx4aq2ZPuyZopo0yCzhW403SC5KC2eipa7XZQM5OfVgUbTYaRImrC5OZswCfn6U_KgyrkLlblyfJsvpxdRTUNLFr2yEwEMXYSKCZzRnL1IHwp5rlCFUNPo46o6kEXiLQC1B3dkztAAOJ7TYOMGyndNKwB2nxyojcPTS3PVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: ما هرگز در امور داخلی عراق دخالت نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143078" target="_blank">📅 21:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143077">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_TBIDc_EL5Dm_fdxrM8zU-ShmqPt7XTNPEHzScQIvgG-90Nik-kasiL6Wr7_cgWkHp5IhGevOYnLkAiIMWP6TeUl6yITa2j1Szjj6Uhd40QUC7dPtQ9BbObO96ZYt1UgeBKuHCMcdtUVCoNY5P4sjSRVtN-lFgJRqpY8ndIaBxX7EiA058_E3wz1Iu86e6lmEAT9mWAK4MoIpfZgiKzJ8zA2aSq1_Xoov_iK5I3X1e4YhjXj1JDBhV6Ro-AKIdBV5SjspfkR1Zbil3V5y8HA9zTpQck0d0zl2Ndcle3UJ4RXHLfo6pi5f2blZqRyF1q6z42ZOCPxYV8mrTDiTrwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس وایرال شده از پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143077" target="_blank">📅 21:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143076">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXlcFiH76aBZ2tu-Z5or2JorkLUYzA2KQmMEbiw9IMBYKOFtqiSM9LplPvPM0iHdexG3J87uJoTJ5KKpzA8d2J8DO6U8ZnU5UL_AG8_40d-J3cyfp6SzdUbPDyjWxJJl4VI8vq6P9z-XoO7J4Pjm0aIJAZ1cj77S0nZwomRibNUWDBY5NqdYZ-lYYOituqLtwdM7tkl0E_Y4xB5vzeGhxd5Pyu8e7xixAOhUus9YXTMcAhVuFQi-YvBAu7_Zw7_bUpm-vSPTKrd70Q6vpvsD2X-eM6YMnQKW_pI0XLWN4Hddclzu-1HODpvsBpIBGS2Ns50oNDga3cT8idAtnFU1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف و هیأت پارلمانی همراه وارد تهران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143076" target="_blank">📅 21:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143075">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNyBWOb-Ktl12Py9gMANZAaXbPj6RdjwjoOpt04DuqQyawy8JDDJHDoeJvlhbAxrPUGJF4bDVBqc7zfprzthAvIy8yy68tSLdE1wqJozfM45UKICjUJOymo6vFS-07AnBUhxXZNdVBxIGoI1ivAlFdGu33S100RM1d_WhLMgIQFz1aNkKNN31-puOk4WiVR0AyuGN_J0EYVb2nXXRE7haIIZMlPCMEWsZv0G24VH97IbE225WKGYrMp7A_-_jiy1UXwqXyjR8nR-hwUEsM0jEu1jovOy0Kw3IUYGbvOREuoRrL8Ku4ZzVQapK8eXb-Du_7DZBWHzcQsUAaEDS1Fkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازنشر کرد: رئیس‌جمهور ما به ایران هر فرصت ممکنی را داد تا سرانجام رفتار خود را اصلاح کند، از نقش خود به‌عنوان بزرگ‌ترین حامی تروریسم در جهان دست بکشد و به کشورهای تولیدکننده بپیوندد. او درباره پیامدهای ادامه مسیر غیرقانونی و وحشیانه‌شان به آنها هشدار داد. اما «رهبران» آنها چیزی جز رفتار تروریستی و قانون‌شکنانه نمی‌دانند و اکنون رئیس‌جمهور ما به وعده‌های هشدارآمیز خود عمل می‌کند. این‌گونه است که رهبری واقعی عمل می‌کند!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143075" target="_blank">📅 21:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143074">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da64c04333.mp4?token=aDJCHkk0mtfS_TT4lkR8k2GHZKXrfGHx4-9pC5zwr8Ko351htRE4ykusW4dh4hktWC4Et-fhciUPLrdDMld8ezZbaHHg2_UeUbpTI2qGSYlDoGgba4h7Y__cFyiYHBZU4ZHWD_P-pyWvQ3xZa1X5YcGftrvz6XrdloALT242zHRqDIPil9WrfFa00s3qHJ1O5LFtCAghx4UuFW6-tDWlFSLshPgEz5kCvN92iG_0rLPjg08sfHJQEDKvzihdaBP4f1EdYyagKZr-pnXghnwLqY3YRJMVo4-P_rVD6tjGj_Li2dCZ0ugquvNrc1xOnKjqgrmEhJ1BIoRxibe5ypTDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da64c04333.mp4?token=aDJCHkk0mtfS_TT4lkR8k2GHZKXrfGHx4-9pC5zwr8Ko351htRE4ykusW4dh4hktWC4Et-fhciUPLrdDMld8ezZbaHHg2_UeUbpTI2qGSYlDoGgba4h7Y__cFyiYHBZU4ZHWD_P-pyWvQ3xZa1X5YcGftrvz6XrdloALT242zHRqDIPil9WrfFa00s3qHJ1O5LFtCAghx4UuFW6-tDWlFSLshPgEz5kCvN92iG_0rLPjg08sfHJQEDKvzihdaBP4f1EdYyagKZr-pnXghnwLqY3YRJMVo4-P_rVD6tjGj_Li2dCZ0ugquvNrc1xOnKjqgrmEhJ1BIoRxibe5ypTDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: سیاستمدارانی که با چند هزار دلار به واشنگتن آمدند، پس از دهه‌ها خدمت عمومی با میلیون‌ها دلار در سبد سهام‌هایشان از آنجا رفتند.
🔴
شما چه چیزی به دست آوردید؟ ما چه چیزی به دست آوردیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143074" target="_blank">📅 21:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143073">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
مدیرعامل شرکت نفت ستاره خلیج فارس: استفاده از متانول در سوخت در کشورهایی مانند چین، آمریکا و اروپا تجربه شده و این ترکیب هیچ آسیبی به خودرو وارد نمی‌کند و قرار است این ترکیب در ایران نیز انجام شود
🔴
پ.ن : ماشینای اروپا و آمریکا کجا ماشینای ما کجا
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143073" target="_blank">📅 21:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143072">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKkQqnDlo8AUP6Ys-LDcmE_6NBkK1YFo8UAZ0Q1lLd92remfIb_G6aV0rZdB2mRYiozABevieVchdws1OheI6IVxHLLbpEfVGn6-pE4JhoDsxnp_Y_TqtMeB4VttacOAkSMfKZnos1fkkW9Kl_IMsMR9sgqRpFOS2F8xujIGR7YGW3Gb3GQjpgE7ZVHwA-9LuTDdkWiEXINZWSFVqOxFxTwax5dWNCRR8mvI8MX5lhEZDpx6JPTj2dsDaYKzp87Rf_JQNKED-nC1nnsMd8A7K-5dppEZjwpCaKG3_HZRvVcjd5l8exystsf4snnBEE8cBTInK2fik44KUlU_FM54Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصویر یک کاربر شبکه های اجتماعی از مقایسه وضعیت سد کرج
🔴
بهمن ۱۴۰۴
🔴
مرداد ۱۴۰۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143072" target="_blank">📅 21:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143071">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkypN1Lmz57P2_JJYKR4hJD4Y7eMnZYJoinwEFXa_wPoMhusQsLf5bbZ0UxLValToIWytrk2s2ulxr5XPhvlhdunIwGCECnj6Aj023U3CW1_-2-KsDBb0yA0vLnPt8byvq84ESVZ_oQOLZydj_tyjV0z3Bkgq9I0m8goKBWrfze6VC84SjJFzW95BSXl-v6lT5tYZ_BRCpoS-fbxoCyJ66gyJTBFH7WpLWOYs9Seigy0mvHIhpSRh6c4fSw8HEKg2DarX-1nSJ9C91LJyezud8fGDtk8n4qwaM-7xAXaUbVPwezT7JGCHtd07AQcalz_6zuFzHJTxLIBFJE3gjRFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا اعلام کرد پرتره ترامپ روی سکه جدید یک دلاری چاپ خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143071" target="_blank">📅 20:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143070">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فرماندهٔ نیروی دریایی ارتش: به‌زودی در پهنهٔ دریا درس تاریخی به دشمن می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143070" target="_blank">📅 20:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143068">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkIBuRkD6qXT4HrHPE_iIOSmVUhbI4F_xnkyyX1u4FhdkfwV3OOiIZCEcMQwVMoTBl0hmZ1tOtiHmSFpQKQuYtRIkNprmqHs36cK3DlVxgZSZ_VrjWLvxWCJPyQRLU3t0XiyCUimaPoeIEcuQxI1NLerZ0slwcuvNnEfmTBhMkFLrbAlynr-tzOwEKT3yI4w7S3tCIVGzUBrAtLiXcwa8j524dJ-TNv_WciW1MsmAzirbvCZbEdAarA_OIPaIiOlI6by-Zz5Gl2kep20vIj1BnVm0c5x_Qrc7eZaU6IfdKFdrxFDs3LM_IJAZVowuPvr4gWvEWSVf3WHzs2XkvMn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی انس طلا بیش از  ۲۰۰ دلار دیگر گران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143068" target="_blank">📅 20:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143067">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
قالیباف: تفاهم‌نامه مفصلی در حوزه امنیتی میان ایران و عراق امضا شد؛ ایران هرگز در امور داخلی عراق دخالت نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143067" target="_blank">📅 20:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143066">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
خبرگزاری رسمی عمان: وزیر خارجه عمان و عراقچی در تماس تلفنی، درباره آخرین تحولات و شرایط ازسرگیری گفت‌وگو و مذاکرات رایزنی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143066" target="_blank">📅 19:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fptbjflhdbbxcfzb7PiNpLdq9HuCZAM9yPm3lhOnv_LqyfdEUkLqoiirTinWcfj-9EGAyEtpIWkorBIaGor7QWIvkzYZge8aJu7wCMOSczXisVJaR-s9af3HnaHbZZgN_oBJcCLEhIhmSxIqWdczLci8jNyS89RQgQcgdtWKwTxlKv47S3jqc0pvfyKetjASEPl2b2ixybQKRPFhQIp2WwyPDQJr5QlNRfjpxi77wWjPY2ewseanhA_zp0tMB1CV7i_qwMfhIg5r9pMBtutW75PVA-r4zVz8DlTzFT6lau_0SR3_eX-eHoHosFcE0V_QvsSRrI9jsgx9uqyH9OQj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش توپخانه اسرائیلی به شهر بره‌شیت در لبنان، در محدوده منطقه امنیتی جنوب لبنان، هدف قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143065" target="_blank">📅 19:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143064">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS5HDXdVVxx7Yg0DR7y6wMiFzkeoLHB7AKFiIfjNke8D3Kxqzu_yBodcVVVyLexyzKiJ-GY7vtymYV-QfrV_V08aXf1Q90K1Ij_t3_clAPGIO2zeIzl9grzx4BExrWOc-jmHQys1ajxWtU50k1k93wDBgZEa3Nf77MRQDmplLfw9w475wtDL5c_Lp1OLuV1GgM34T4G62AR8HycjVN6El7iBHi2OUi0nBhzS8u2jTQjsDLKYZPHzc7Cmxo5z3Mu1Oe_m2l6JQym_M_KfuQASZH2jECAAMibsNZTnM25UXFu3S7yx2WQciKGgCNq5yUGEHTsBm8uQyaJNRQcAlmmP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس، ابراهیم عزیزی: آمریکایی‌ها ثابت کرده‌اند که زبان دیپلماسی را نمی‌فهمند، بنابراین نه تحریمی را برداشته، نه منابعی را آزاد کرده و نه دزدی دریایی را به پایان خواهند رساند.
🔴
اما تاریخ نشان خواهد داد که با زبان قدرت، نه تنها مجبور به انجام این اقدامات خواهند شد، بلکه با عذرخواهی از سرزمین بزرگ ایران، منطقه را ترک خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143064" target="_blank">📅 19:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143061">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRfyu7VUpiC_Y1Bsb0s-vYYWIyYB67wKONsqXccZQ0D4TiCAGtC2H7nbPtU6aRxtWj-EMm6c52j5-DS4ae4wYMCUgG4HrwcDiHGAirjnYY_lj7IuQhohoGm5V0zunkBmOeN47VyWBMG3TUWPkmAADxTsy111qC_kDVDCrEYDjfLXjhx4lJkMh8_w182dkUiazQLAr-1zGpzxdou7hWg6jLN2zNz3D86LWJFuWItPmXYKnLVT54fT9KLeQ3MjN_-IgbFR4P6-XzohKCQ9i6AhK-FHD2Ghm53ls-4UqnI23z7TZO80b1Xx8uIrJVwLrh0A9tEPBvN1SdZMwNt23ao46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQzFdW1lk7aP0143MGdwhiOdEhDhzF9LwB3TlpDV4pwBzN16vbNCAohbCQiR27MHr10ujMHPLl14koqtRlLU_zQ80q0C6uw76ddh05zDEyGOZiEZzGq4TfQlawoclO18YddTIwsevzXpGN0T1o_GkHZx_TBpDwNYFAGiToft3LRGxFbIl9ObOjausnqmmX_raWyA06Xzwq8SDBHZQn5pXXmdcYCbsyanFY1r0M-l5SiZFzeLjYocVNeZrKl3MdtcfIWllOyVZzjV0MQNfzJzxKA3Ij2LT72VN6Lf4xW4t27gEsOA_KSvHqOkwl9UJC6zosx0DFuumhOzveo3TN80PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ro0aIbuOihPBCH6LqlZQp9_cqWFe_e2JstWBlMZEwqMl5eH7aPCuYWEvixVEe_3qu37ZC3ON6muR6_TAujmfh-E7e5XenCa0GWJ6ZC8SvAyrGhLCffEDaapQfLOuVgkK3VeqDrwhJXfxdQQlENAqi_gBzJC-ONdcuyvFUKsWaQHQp-z5fXJAuwoz_02D3jAsL849g3TZjoRHS9iCSLkWKsc1CZvYKDGFHwdML3JxJ7Kq2oZaflL2PzgGr9Gy9STe_Cgwbdb5SyeW4zMuVKnmhPngroBdYtTpSm40KISQCA6j4wIB2F7AmZbNNL5imX-O-aeU6e7btZ6oceWtFrl7tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علی  دایی برای تولد دخترش یه هدیه حسابی لاکچری گرفته؛ یه BMW M2 مدل ۲۰۲۶ که گفته می‌شه حدود ۲۵ میلیارد تومن قیمت داره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143061" target="_blank">📅 19:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143060">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
آکسیوس: بازار نفت دیگر مثل گذشته به اظهارات ترامپ درباره ایران واکنش نشان نمی‌دهد و معامله‌گران اکنون بیشتر از مواضع سیاسی، به واقعیت‌های میدانی در تنگه هرمز توجه دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143060" target="_blank">📅 19:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143059">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
العربیه: محمد بن سلمان، ولی‌عهد عربستان سعودی، برای انجام یک سفر رسمی عازم فرانسه شده است.
🔴
دفتر امانوئل ماکرون، رئیس‌جمهور فرانسه اعلام کرد که انتظار می‌رود  این دو در مورد تنش‌های  غرب آسیا گفت‌وگو کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143059" target="_blank">📅 19:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143058">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سید عباس عراقچی: ۱۴ سال پیش: «سخت‌گیرانه‌ترین تحریم‌های تاریخ.» شکست خورد.
🔴
۸ سال پیش: «فشار حداکثری.» شکست خورد.
🔴
۵ ماه پیش: «استسلام بی‌قید و شرط.» شکست خورد.
🔴
امروز: «سنگین‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
🔴
ما قبلاً این فیلم را دیده‌ایم.…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143058" target="_blank">📅 19:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143057">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گزارش از شلیک توپخانه و حمله هوایی اسرائیل در المنصوریه، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143057" target="_blank">📅 19:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143056">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSNM8-7bsL0PE1t3XJ3eAs1ik8xNF4ll8YNbf9zQ_PZJ5YEk6K4qYTkgsQH8DVt99gmbV0VRJMoASGRWbpkpEciREDYSHy-6hpC__vVp1J4Md71ydBCBTgF5XwonwJKrqam-JziXQHGOEwSgehS6xbBxaMHypKGp8MxFz6Jz2S_xNEG-w1GRrI7vrwUYobWqID5Rz62R-zYsZoahUZPV-SsvWKlT9-hbTzTH2cJXw-2pjwyEiUrqonUqFOUyYp5ACM2_aKVaiH82xbxoBhY59F19LjBE34tLsRsvl5cNSXdFU-ZyhAjdcjUnFxvHaWKFZcbw6mEwgysNiOD_rLmLyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید عباس عراقچی: ۱۴ سال پیش: «سخت‌گیرانه‌ترین تحریم‌های تاریخ.» شکست خورد.
🔴
۸ سال پیش: «فشار حداکثری.» شکست خورد.
🔴
۵ ماه پیش: «استسلام بی‌قید و شرط.» شکست خورد.
🔴
امروز: «سنگین‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
🔴
ما قبلاً این فیلم را دیده‌ایم. همان بله‌بله‌ها. قلدرهای متفاوت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143056" target="_blank">📅 19:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143055">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر کشور بلغارستان: بلغارستان تمام اقدامات ممکن را برای محافظت از پایگاه هوایی بزمِر[متعلق به آمریکا] در برابر تهدیداتی که از سوی ایران مطرح می‌شود، اتخاذ کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143055" target="_blank">📅 18:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143054">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b2c4df98d.mp4?token=P1VG7wpndNMIxPC9yJhSPF3NXNqb6vXYXMg9UC0AuW3BOgFUVs3AU_YAcZH71Y1zT338BmMzP4huUYmRl1W19fkrZbupmv5jsm3x8i-5U0Qz4ss27R4ygAUklPMLT2UOWwRj_zmIUeh0kE3jv-h9tBlXd9LLE7cgsLxzPqTfl6uYQAcAqpYdEw86zMvc6NxbstvmvQgib3iDQ-cUd7x6ATKZB7nSJc8nnlQVffw7a3mYsQi1MtvbVROfS7Gz1WbAOQNl7HFjlqHnEWUrZF_BoASkyvCLoJ2n0lvB_gkX1sC8vU67aETXn6II2leNE1SvWiw5SdyPv_3JIdDUf2NZ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b2c4df98d.mp4?token=P1VG7wpndNMIxPC9yJhSPF3NXNqb6vXYXMg9UC0AuW3BOgFUVs3AU_YAcZH71Y1zT338BmMzP4huUYmRl1W19fkrZbupmv5jsm3x8i-5U0Qz4ss27R4ygAUklPMLT2UOWwRj_zmIUeh0kE3jv-h9tBlXd9LLE7cgsLxzPqTfl6uYQAcAqpYdEw86zMvc6NxbstvmvQgib3iDQ-cUd7x6ATKZB7nSJc8nnlQVffw7a3mYsQi1MtvbVROfS7Gz1WbAOQNl7HFjlqHnEWUrZF_BoASkyvCLoJ2n0lvB_gkX1sC8vU67aETXn6II2leNE1SvWiw5SdyPv_3JIdDUf2NZ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی اوکراین به پالایشگاه نفت روسیه
🔴
پهپادهای اوکراینی به یکی از بزرگترین پالایشگاه‌های نفت روسیه در پرم حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143054" target="_blank">📅 18:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143053">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل: اردوغان یک دیکتاتور یهودی‌هراس است که کردها را قتل‌عام کرده، از تروریست‌های حماس حمایت می‌کند، نیمی از قبرس را اشغال کرده و تعداد بی‌سابقه‌ای از روزنامه‌نگاران و سیاستمدارانی را که با او مخالف هستند، به زندان می‌اندازد.
🔴
او اکنون به دنبال…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143053" target="_blank">📅 18:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143052">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
روزنامه تایمز آو اسرائیل: فرودگاه بن‌گوریون با شدیدترین اختلالات پروازی در جهان مواجه شد و میانگین تأخیر در پروازهای خروجی به ۷۰ تا ۹۰ دقیقه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143052" target="_blank">📅 18:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143051">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU8cRIV4IQJXzLXMHnC_MEv2ugMaMsN3-ulEGht5g00PK75CvFEjstr5csvJq4gf7gH-_vr_Qc8yAs901zNjaptkspSST0KmoSpY7ZZZmlC_RBC7P5X7ZAtMBm-7_vBD7HLIcbmpD_6Aj7xRVGeFBv8DdOXw6RGA1Rfpr9fZpB1e6MP1bxW3kl9rJnUxEn27WdNYWgZ2JQFAJHT8uCz6eyvCvKD9Fz1tz_sAWDlxyuvFWREjDV9_2KMIpo6zdUrPFhc-Z71x39zV8ByZkmeQxv8wxnR8SXj2UBMsID8wjqFgvxwtmBk4bDG80uR54DiHSSsOzssp3lneNbJtE-hZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل: اردوغان یک دیکتاتور یهودی‌هراس است که کردها را قتل‌عام کرده، از تروریست‌های حماس حمایت می‌کند، نیمی از قبرس را اشغال کرده و تعداد بی‌سابقه‌ای از روزنامه‌نگاران و سیاستمدارانی را که با او مخالف هستند، به زندان می‌اندازد.
🔴
او اکنون به دنبال گسترش تجاوزات خود علیه اسرائیل به سوریه است. اسرائیل این موضوع را تحمل نخواهد کرد.
🔴
تلاش‌های مضحک اردوغان برای ایجاد ترس در رهبران و سربازان اسرائیل، تنها دموکراسی واقعی در خاورمیانه، به جایی نخواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143051" target="_blank">📅 18:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143050">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سنتکام: از اوایل ماه می تاکنون، نیروهای نظامی ایالات متحده به عبور بیش از ۶۶۰ میلیون بشکه نفت خام از تنگه هرمز کمک کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143050" target="_blank">📅 18:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143049">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjSnfWUOIHMkku7F3kgu01DGDQXYP78_El8jnchW82kuKRQwTvXbbLAR4Qhs06xz2yx6kTabigHgmn5Ed0bM3Rvj0ex3BqN5_GcHnvh0_kCIG86XO35FQCewhR_OvIJXHjTRjkGdNvus8HZYtB3Jo65JOPdoVyzv-xLpgdynn37YVN5JzLbyBbZ9jRXxKMWoH4EFR2WbMq9F0jXpAN9-uryK51eyoH9Ew9cj7USl_3uF0KVAZVXvgUfERcnlIKZF56BCO-F9wWqPzhDIQocFWZuSTvTMk_8J4Jpaf7IWywUBZqJZ_LFNK9HG7bMSeCTsqIyysLVGITauxo9bbn-Umg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلمان اعلام کرد در تابستان امسال حدود ۱۴ هزار مرگ مرتبط با گرمای شدید ثبت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143049" target="_blank">📅 18:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143048">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781f58184f.mp4?token=MgFsqfBZLDyO_ruHMX-TyUCSwPJ0Nduxw6zozDrONBN6Sczk7gc4VsR_vGiAFbiQybyiU-2qpiu2sYl5QU3z6sejb8GHyyOfpxPRdfhQtxh6e6AeilNHUIKK40q2EZUMUwUSdemhkds9w6Z08YX5avRXK9Gbv3z6BufpHqNYmEI9x1_iuQiYXNYpoq0YtgScRoP7b21kiQ7jIXkQQZB6rasn-0SZf5qIk-nzo0PBi5i0cByppcMBGVtTRWDXULR6qee4gDXzDZbYGphLxhVti3reTH10pTv69P3HBS26hUdjuZdhnzeTcGu5t7ORbSKKvC7-CngM3NhzVmdQcGHEYoU1YCwL6b5qcafKTS_0_iCnQct8MVOdv6rmqYR2afepgn4jqq5P9wnnMU5CYa2xKKq6s__bt9Qib2hH7pgQs54E8aVy4e6p4NAYTKnrUoK7QcWy9KvrbVqfTqtoF1keOyX7M3DGOa0urv7hWIPH5fOPb0k1jZcSinambJlaaYWLPCPyvjRPGAPoT07mFNGNtei6g3tgRvmva7Bzcx3s4dCnWCnf8fauQeEQ1FMTT42y5bPp241xuCgIbhfF06v0rAq7Q3LoJRRi96o8LilWZySHJLh9qsaTEmucBeg8adlgwmCWpQzMuQC4pZNyn2oB-x7YP5VDBpYWxHzbvgiiqD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781f58184f.mp4?token=MgFsqfBZLDyO_ruHMX-TyUCSwPJ0Nduxw6zozDrONBN6Sczk7gc4VsR_vGiAFbiQybyiU-2qpiu2sYl5QU3z6sejb8GHyyOfpxPRdfhQtxh6e6AeilNHUIKK40q2EZUMUwUSdemhkds9w6Z08YX5avRXK9Gbv3z6BufpHqNYmEI9x1_iuQiYXNYpoq0YtgScRoP7b21kiQ7jIXkQQZB6rasn-0SZf5qIk-nzo0PBi5i0cByppcMBGVtTRWDXULR6qee4gDXzDZbYGphLxhVti3reTH10pTv69P3HBS26hUdjuZdhnzeTcGu5t7ORbSKKvC7-CngM3NhzVmdQcGHEYoU1YCwL6b5qcafKTS_0_iCnQct8MVOdv6rmqYR2afepgn4jqq5P9wnnMU5CYa2xKKq6s__bt9Qib2hH7pgQs54E8aVy4e6p4NAYTKnrUoK7QcWy9KvrbVqfTqtoF1keOyX7M3DGOa0urv7hWIPH5fOPb0k1jZcSinambJlaaYWLPCPyvjRPGAPoT07mFNGNtei6g3tgRvmva7Bzcx3s4dCnWCnf8fauQeEQ1FMTT42y5bPp241xuCgIbhfF06v0rAq7Q3LoJRRi96o8LilWZySHJLh9qsaTEmucBeg8adlgwmCWpQzMuQC4pZNyn2oB-x7YP5VDBpYWxHzbvgiiqD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند در تجمعات شبانه: هنوز که از بغل بیت رهبری رد میشیم بوی گوشت سوخته آقا میاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143048" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143047">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHw7SFHaKb4uS6G-yhQhP8Z4KiYLiXenggfTfS86ZDCwxF9LgQ8hf0LP5NsluMnm0i0MLGltkeXvMA8zn6QtgSc5Y_AA2yXEsdN1CpoyehCmT1gFun8Vq32OT6HdjK5Tk_ARBor7r1kbpROLXD2FbgF2jUblnRkGGWOPLQfPLjeWOn7l5WLRnUGWIYFwnT9d4XjP-V0k6s4iPjNeW0JRSVvm4WD_CZgpShHnBg6v24IFMIhyzMIiQTnPGjj1yD4xU_uuvtPfA7UAcgZ2I9y60V3tNT5ajwoM4V7IqJvwAgio-XFxBgMsNlKi87OIFO-jtcJR3XphIa89WabeyAMksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش سی‌ان‌بی‌سی با استناد به فرماندهی مرکزی آمریکا (سنتکام)، نیروهای نظامی ایالات متحده از اوایل ماه مه تاکنون به حدود ۱۳۰۰ کشتی تجاری در حمل بیش از ۶۶۰ میلیون بشکه نفت خام از طریق تنگه هرمز کمک کرده‌اند.
🔴
میانگین حجم حمل‌ونقل در سه هفته گذشته حداقل ۷ میلیون بشکه در روز بوده است، اما همچنان به‌طور قابل‌توجهی پایین‌تر از سطح پیش از جنگ که حدود ۲۰ میلیون بشکه در روز بود، قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143047" target="_blank">📅 17:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143046">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf64a4853.mp4?token=nDYfZ2nv1-gtrhnRBQYRT8npngf9zEEXu0z0hG2ZpJrbj1pLdtKW0ZTCqSiAzVQyD_nR3p5iNJb7cHrbjTypD8JyzwEPPuj1MLzpkbuj7GyeOk7oAO44cJxcFE0oh7pRcyNSGyg-fKi_2g7r7K5k7xKNOa6SqIVac7wUZDQB0gEFme-6s9q1gLeqfQnp9TLworM3_jfXizwLp-iBe8v1636i2oxaV3eQxtOFpD7s4T2_DqKykQxDn4YZ_o0Dw9w1vCirg2WYxC0R8Tf90cfsR5uE_uzWT62oPC1NHB2kzH5VKmaXgk2LxVBOx5u7Z93RtB-xKUIgnrJKXNmPrsyIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf64a4853.mp4?token=nDYfZ2nv1-gtrhnRBQYRT8npngf9zEEXu0z0hG2ZpJrbj1pLdtKW0ZTCqSiAzVQyD_nR3p5iNJb7cHrbjTypD8JyzwEPPuj1MLzpkbuj7GyeOk7oAO44cJxcFE0oh7pRcyNSGyg-fKi_2g7r7K5k7xKNOa6SqIVac7wUZDQB0gEFme-6s9q1gLeqfQnp9TLworM3_jfXizwLp-iBe8v1636i2oxaV3eQxtOFpD7s4T2_DqKykQxDn4YZ_o0Dw9w1vCirg2WYxC0R8Tf90cfsR5uE_uzWT62oPC1NHB2kzH5VKmaXgk2LxVBOx5u7Z93RtB-xKUIgnrJKXNmPrsyIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های روسیه مواضع اوکراین را در منطقه خارکی‌یف بمباران کردند.
🔴
جنگنده‌های روسیه با ۵ بمب FAB-500 مواضع موقت تیپ ۱۵۹ مکانیزه اوکراین را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/143046" target="_blank">📅 17:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143045">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
میزان عبور و مرور از تنگه هرمز حدود ۹۰ درصد کمتر از سطوح پیش از درگیری است
🔴
مسیر عمانی در تنگه هرمز پرخطرترین گذرگاه است و از ابتدای سال جاری تا ۶ اوت، ۷۴ حادثه گزارش شده
🔴
کشتی‌ها به دلیل حملات و نگرانی‌های امنیتی مستمر، بیش از پیش به مسیر شمالی در تنگه هرمز روی می‌آورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143045" target="_blank">📅 17:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143044">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
لهستان سفیر اسرائیل را به دلیل توقف تحقیقات در مورد مرگ امدادگران مرکز آشپزخانه جهانی احضار کرد.
🔴
لهستان سفیر اسرائیل در ورشو را احضار کرده و از تصمیم اسرائیل برای بستن تحقیقات خود در مورد حمله به کاروان امدادرسانی آشپزخانه مرکزی جهانی (WCK) در غزه در آوریل ۲۰۲۴ که منجر به کشته شدن هفت امدادگر خارجی از جمله دامیان سوبول، شهروند لهستانی شد، ابراز ناامیدی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143044" target="_blank">📅 17:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143043">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMolLM3mijBDnU0d6z4aQ7SYZhiRAJRGi-hWRVG3IdW7CkjeUDQW53C7XzjD_Dvn05FQWOVCtHLldMmyJgNnXqO7HY4S3JBCLmeBBm8zkF_2XveTNRm3G9VG4BNr7weYhqufTlI9pkcsDEYltpxK83gq0EKpQYz-Tz2dIAqLS78wU0wiObEk3cIAVgFIhRviEasXzyXYN0K28gb1_ccIB_RHVJpxTi3Bg_x-ymgj7cnkUg5ch73Cz4-L4rkmfuovTRMghyzDu4Vgb5YDKtRtHvgV_s2CnAZctMpvcAsGi7uWBDG4rE4hM1BQMqCQmmGT6VzHib52BhYGNU4TrHn0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت در ساعات اخیر چند بار به 94 دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/143043" target="_blank">📅 17:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143042">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAnA-M6athWiSmT7kENZDxRDZD9e8FX7BcMpTgnUWnZ7CHuSkMEOtJJsSTJ0JOTt2d0sK4kBfsS4f3JDv9kViv42trbpDkK39tlDW81ZLOJ_C_DQ7k-FV8T5AhpwOk2tTdBJ8R-594Zhc00wFXPPB8TCBK6jqozGYGoOgkmQTQxcpD-KmJHFGRSBwip0WEmLem8Nfcdh3hNXQKrr8X1Uzn0RXad_0u3WYvugvLenZCWBynFbVpcRBFaQkOwtPEqP4wfZl50RLyGLxt_TPhSiubI5mcu3Rz5PaI0cNzcalCeQ7WgXtExFYuow6rvIZ1xEIvG-gsR98CXTR0Dk6XVMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالی بافته شده در عراق در سال ۱۹۷۰ که خلیج فارس در آن حک شده است, ۱۲ سال بعد از دوخت این قالی، "هیبت الحلبوسی"، رئیس  پارلمان عراق به دنیا آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143042" target="_blank">📅 17:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143040">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6LshsTZFbYc7NKBuL0GhQtdiWnTaisFvD7uwwTOX9rox6XP-k6kVwf9DOZqYUDJPYbIpXetS3sDoc4A_csFf4b6vToVbTKohy3d-T_g3c7MuPNTNJB_DpFEdfoH6l8jXKriTSJsksRU0gmZCa2MeYbc-Wjd4uvSlY8Mc_ohR81OtpQhoHdAEaQVNe0gv7bIUf1CtNHdTVMGFIDD8KLvt1at3QbE-cypCyHMRH3etQrmlQalVImGbClTDunoSB0fMMO6Y22mnlreWZHSr4A-p9iama7hWava77nnoeYwGFgRLDnYWrMFIvjPualw00SojvazyKhlifje88S5Y133Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم در اتحادیه اروپا به ۳ درصد رسید
🔴
نرخ تورم سالانه در اتحادیه اروپا در ژوئیه ۲۰۲۶ به ۳ درصد و در منطقه یورو به ۲.۹ درصد رسید.
کمترین نرخ تورم در میان کشورهای اتحادیه اروپا مربوط به:
🔴
سوئد: ۰.۳ درصد
🔴
جمهوری چک: ۱.۳ درصد
🔴
دانمارک و مجارستان: ۱.۶ درصد
بیشترین نرخ تورم نیز در:
🔴
رومانی: ۸.۲ درصد
🔴
لیتوانی: ۵.۴ درصد
🔴
قبرس و بلغارستان: ۴.۴ درصد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143040" target="_blank">📅 16:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143039">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
طبق گزارش ها، ارتش اسرائیل تمام بالگرد های نظامی آپاچی خود را از جنوب این کشور به سمت مرز لبنان و سوریه منتقل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143039" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143038">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMZ_zFyKl1f_3HT5okCOUxqxdO03_RDgJfqFQ-SiVyUzI95tQRjesm1yAboJH_wxNybgIxEw9op8MSZCGhUlzWKI8JBuYSkTOx1XWGQYd8cHZqVoMFvVzKuTTw4os3Ew8QmOmTPTFLuWicVZaqOyaNROdBB5Aa1zovxOZ9ukCYOnikEoTjQF9xZenRKeV9Rs5HcVG8E4LwAKs-3ilgsPBDqiDsmgBLTGLxtf-Mljl1q_mZK8mIfBrUkF9OvVJkqiqrtWQP8tSw_YULaavEXf7kfmgOiku_pr904WgLfRx6psiM2aoGmktTImnegl-Jp1XT4EX8tCgvi_iiIA6zOJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: به قدری اسلام رو ناب در کشور اجرا کردیم که آمریکا میخواد اونو از ما بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143038" target="_blank">📅 16:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143037">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy410GwbDFZxDeoR6jGVnPASYhx3NZC2_qsuKPCdo7PtFVVIs9Do4aeDQ5T3N7eFKR0aX-5PZqkLxtabJ3oo9saEsI7jwO5bNngxYdmWEkMG-EUclHSdkAQKFdl9xHwfvFNfHK9BQ2ELFUAEWyCeJvzFRNMiLqZzOVj8rV8iQG9-l4gNY61TCrG7xTXSTTuziuho6DXsmF-pSUbuhV-qejI5JTzUrgeHGwnaQZk41SDOgvpVesLldZ3tG6kT1FkCe7hBsj_hKobOs5u4aHkA4qtF8KsPqqyPTt1oiyC_ndTJLHKV747fFKx4DCVc36qA-P-2k2It5njV4RLqHwLmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز: نباید تسلیم بشیم و باید تهاجمی باشیم، بنزین و .. هم مهم نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143037" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143036">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_J-uCInAgukmqsdOdebWO_74tsE93RYW5fvbfqPa_brImIos3YCWB1tu4hVXOI0iso7n5NViQ6anHEAe2vnEqe6KT_ve009GKcWyDBnsMVVT7WyV2sb-TILtI1bhj8i1MTX7dTJwo_M0cSA6Ii4TTl1yUDrFA66kutMZz08nfhad2PcK6wMsu158smszIHexgnmFwAT4ojosR6uUbLgdKV87WG9zdiGDjt1vG-AaC5ErZ5zIJrhJfYN6meAt1ccoOTyAIhSxuEk4oRl2D3-w2X45j5Wldkr31lM5KL8oR4EQYmAfO1pECt9chppBI9_SLHZWZgzKRmDGTv3D5rDVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان:
حرف از صلح در شرایط فعلی یعنی تسلیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143036" target="_blank">📅 16:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143035">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کانال ۱۲اسرائیل: سفرهای اخیر و پی در پی مقامات ایران به عراق بخاطر بردن دلار در چمدان برای گروه‌های عراقی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143035" target="_blank">📅 15:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143034">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef3638ca.mp4?token=QhO6P7LdI29-ww2f4hKnqT5NLi7BY0vZrul-qD-2v0W-wFgufRunXIjABxvwQu2NNBXOmhmK9od1YNOmSiRLSQpb0nSSIkk_9LvcTiTCmKcC42_WEJ75BtKHV_0FGQowJamhgGJ3MrR0_IA9WGzuslo2T_kBeJlLaRRGbYFWi9ExrKf6xqj4f0jozd69esVRuEVga9q3ghpjOTOnbS-ryp88Z5qXaFTWXSeHJKq06UyTsxC10HcuCV9XMQeI37kysZIp7g4YaYacKqnWssDdRruMx6zL7wgN3cJFlJTwjDRb8sSCxN4GEK2Xq72XnYkVNBL7ewHYE1pip7mItehA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef3638ca.mp4?token=QhO6P7LdI29-ww2f4hKnqT5NLi7BY0vZrul-qD-2v0W-wFgufRunXIjABxvwQu2NNBXOmhmK9od1YNOmSiRLSQpb0nSSIkk_9LvcTiTCmKcC42_WEJ75BtKHV_0FGQowJamhgGJ3MrR0_IA9WGzuslo2T_kBeJlLaRRGbYFWi9ExrKf6xqj4f0jozd69esVRuEVga9q3ghpjOTOnbS-ryp88Z5qXaFTWXSeHJKq06UyTsxC10HcuCV9XMQeI37kysZIp7g4YaYacKqnWssDdRruMx6zL7wgN3cJFlJTwjDRb8sSCxN4GEK2Xq72XnYkVNBL7ewHYE1pip7mItehA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو حتما ببینید
🔴
تفاوت واقعیت و توهم، توهمی که سالهاست سفره مردم رو تحت عناوین مختلف خالی کرده و در آخر برچسب‌های ضد میهنی بر مردم ستم دیده میزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143034" target="_blank">📅 15:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143033">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=SvhuZCxkdumeZ9iKdjF1c66Z2IEcFEGNsShqv8x8Kfk1AR_B_3JNCb6oUcB4I-i3DvJIAU3F9fwFjTBJmb4lgQSvXE2ptpn97Y1KqTfM9K2W47eDaNyVhuGQOcg8a8WikPNSr8Hcn3d740tV9OQtTbqA21ua2PpyS0XRPvFS3Ndbw-pHFVOEAgNPmFzGZuFsAje0Qxy758M3QBGI6GZOq5H4F95h-19dBgkWwpr22LY-eJR3dzOznQBJ0wf4DcfuYa2lEMlucDMtcv4EYghdq5Oo9HDW1tQXwuz6LmsSCgB5Jh8lIx20BETdhmgIsFzayhIQgdGQB1Vv2h2mMJaTLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=SvhuZCxkdumeZ9iKdjF1c66Z2IEcFEGNsShqv8x8Kfk1AR_B_3JNCb6oUcB4I-i3DvJIAU3F9fwFjTBJmb4lgQSvXE2ptpn97Y1KqTfM9K2W47eDaNyVhuGQOcg8a8WikPNSr8Hcn3d740tV9OQtTbqA21ua2PpyS0XRPvFS3Ndbw-pHFVOEAgNPmFzGZuFsAje0Qxy758M3QBGI6GZOq5H4F95h-19dBgkWwpr22LY-eJR3dzOznQBJ0wf4DcfuYa2lEMlucDMtcv4EYghdq5Oo9HDW1tQXwuz6LmsSCgB5Jh8lIx20BETdhmgIsFzayhIQgdGQB1Vv2h2mMJaTLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نرخ تورم در آستانه 100درصدی شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143033" target="_blank">📅 15:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143032">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
دولت ترکیه حکم بازداشت نتانیاهو را صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143032" target="_blank">📅 15:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143031">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=i6I8FzBn5msMX5xpn73HN3UeSmSY7wv1DwtABuYjCyrhpngjPGwFBmPZTz6WfVxIhYtkBc20v8Txa1LuPTIUbsa6z1FQQCKyc_URdKd_b-6UP5qCBY_0YF-GiILplviznwd_D8AcbOmXvENM69vmqJSsy3KN6xZxlMN0RmbNpY3Y6eUOJv4XbwfiMVvnx2YYRlUhoUM3HArFpI6_l1_u7DpWEt9-Yz52TPpNhb-8hQ0Q6NlRCJrEqIS0D0hMhJ4psIwXVq8YaQA7uQbCqkUq1Gdv-Lp3LzJbD_wm3blf_prtuHWQ5-Nm6vFh1me3ICNyCj-GlcnqgZTqnWomIuucBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=i6I8FzBn5msMX5xpn73HN3UeSmSY7wv1DwtABuYjCyrhpngjPGwFBmPZTz6WfVxIhYtkBc20v8Txa1LuPTIUbsa6z1FQQCKyc_URdKd_b-6UP5qCBY_0YF-GiILplviznwd_D8AcbOmXvENM69vmqJSsy3KN6xZxlMN0RmbNpY3Y6eUOJv4XbwfiMVvnx2YYRlUhoUM3HArFpI6_l1_u7DpWEt9-Yz52TPpNhb-8hQ0Q6NlRCJrEqIS0D0hMhJ4psIwXVq8YaQA7uQbCqkUq1Gdv-Lp3LzJbD_wm3blf_prtuHWQ5-Nm6vFh1me3ICNyCj-GlcnqgZTqnWomIuucBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خانعلی زاده: آمریکا درحال فروپاشیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143031" target="_blank">📅 15:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143030">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
این خبر قاطی کردن متانول با بنزین یعنی نابودی موتور ماشین‌ها و ریه انسان‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143030" target="_blank">📅 15:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143029">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
عقل عرزشی:
+باید با همه بجنگیم
_خب محاصره شدیم و گرونی اومده
+تقصیر پزشکیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143029" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143028">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
حالا این وسط یه سری عکسا هم پخش شده از جورجینا و اون پسره
💢
مشاهده تصاویر  فقط قیافه پسره
😐</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143028" target="_blank">📅 15:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143027">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKVXZ_mGCbyqmi7lRruVWyVL-Xdvtl6dwUlPPAZO9YAW_I8bJPDl5Ta_q1SFrxpq3-W2tXRWC4e4lC9hmNF9m_GXF9_J0XNSdIlhNXXNOBgEo7Hr-9z7Uzl2mTh_hO-8_0myEcn02pqSvX1StdBdKWCs7gHI0D_bWD7Si8ygXG--J1Ndb93eJ1OdvPMDeuuRp-C7Lxd95f-BLJLwVmPNcyZsLeSdyMdobY05y408bCaZAN_YGMIS6D_uqDtD0R7nwEjxr6XJSaY4I3lPkmEwRKSHjyuCBNik2i1ir94dcES5tFh2wCk87UQeOeRxfsWdIuwig_3Ks2IMwjBa6Ymc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاج گردون: آقای پزشکیان فعلا بنزین گرون نکن چون اگه مردم اعتراض کنن سرکوب سخت‌تر میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143027" target="_blank">📅 15:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143026">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
چین و امارات بزودی یک رزمایش مشترک هوایی برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143026" target="_blank">📅 15:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143025">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYmQDkHQ-m43rv5vJbNVqtQS_oLvlKZkJSBwqjMS9RMwThbBFIzA9Z0yk0tj_n0vQFioUWvS9LEA9zBETLxM4uccmK7a-pypMLnUwhtDao60lYTUdD_Hy0DuI3nB93V2ybnzfnHQZ7ZPTfEflJPt9WL-yA2Kl0zMbfPporhtTDxoHSaNUix8aqM4Nm-e3EEVXf9yGS178QvC-nqqpfvFeb9YNPprZqwZwjSo2Bs-3U-rVl7m1rNkCvZXv0JS4kHq4YB45uD9N0Jz6VsIPsofmgmCgjZOZ_cHL1_9bUOkmjZ13fKmPZzgD_-dd47vRzwbqb5tjTKkQ3T_VUGZ4JaAhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دستور دادم قیمت گوشت چرخ شده برا خانواده های کارگر آمریکایی ارزون بشه، این در حالیه که تو دوران بایدن قیمت گوشت خیلی سریع بالا میرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143025" target="_blank">📅 14:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143024">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
طراح طرح جنجالی مجلس: بر اساس ماده‌ی ۱۵، همه‌ی
اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند
🔴
جزئیات نسخه تازه مصوبه جنجالی مجلس: تولید اثر هنری بدون مجوز از نهادهای قانونی کشور، موجب ۶ ماه تا ۵ سال محرومیت و دو تا چهار برابر هزینه های تولید اثر خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143024" target="_blank">📅 14:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143023">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پزشکیان: قیمت بنزین 130 هزار تومان است، چه کسی گفته است باید آن را 1500 تومان بفروشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143023" target="_blank">📅 14:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143022">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سخنگوی دولت: درباره قیمت‌های جدید بنزین هنوز تصمیم نهایی اتخاذ نشده است
🔴
پ.ن: اونجای آدم درغگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143022" target="_blank">📅 14:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143021">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879faa5c66.mp4?token=dlKd0TYbV1lPLFl2Lt05thzlrYeMOpqTiuY8SJKPRu282KNGZf9opo74fkWHphi5UDFrRJEB5BlhnCjcBlRz7Tqja2JgsWucP-9ut-XDXQaPcyD3qVR6qEukNXw3ucicdeTpyHxmmhWNoMZrAv2UgMY2RaOwRerzki9SqmfsmLUTffdymA9f12fGFosaeJTmaBYaUVZ21hq48xB69OVcvkkP-IWhLesuWu3EnJ8MK0Zev4riD98CfWRY04wzSVhoAx0PngUy_Qqmi5OUG3shocFzYJQ0bzpZ3M1g0BsdeDZEfe3HqGHU448pFWRW3M0KKwNBUS86AB83ZUaRwv6tfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879faa5c66.mp4?token=dlKd0TYbV1lPLFl2Lt05thzlrYeMOpqTiuY8SJKPRu282KNGZf9opo74fkWHphi5UDFrRJEB5BlhnCjcBlRz7Tqja2JgsWucP-9ut-XDXQaPcyD3qVR6qEukNXw3ucicdeTpyHxmmhWNoMZrAv2UgMY2RaOwRerzki9SqmfsmLUTffdymA9f12fGFosaeJTmaBYaUVZ21hq48xB69OVcvkkP-IWhLesuWu3EnJ8MK0Zev4riD98CfWRY04wzSVhoAx0PngUy_Qqmi5OUG3shocFzYJQ0bzpZ3M1g0BsdeDZEfe3HqGHU448pFWRW3M0KKwNBUS86AB83ZUaRwv6tfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساشا سبحانی، پسر سفیر سابق تو ونزوئلا: اگه باباهای شما کارگر بوده و هیچی نشدید به من ربطی نداره، من دارم عشق و حالمو میکنم و بسوزید و حسودی کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143021" target="_blank">📅 14:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143020">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee4976979.mp4?token=ocDd8D05H9LS9mzhYVe2D2FDXaCcC7LK232mcq-TAbQe_Peo-FY5QwdDr1FL9fwZLSAClNLovr6OTRkYW10_UJrxchuQgzhxBrTQ_M8grZYmgX8msNehCH4Zejtzn_4VS9AUMTEk6LrME7Gz13gSha2i9FzCAzD-CKuGDTPfP6tmvqTgJvONASnzIA34LKtbuyF2QB-MxYzeMws6vuE7EiHxGaezx5OLwn5VEyjLjLgUZ4SS86jOEUsexu61a1Xc6WoBJ5t1D1JKOexCsvw7ke_a-YoR9f00LziCizLQRugyja-PD4zVsGQqsjcHUKOii1d7Xi876XEE6SnLZBIlVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee4976979.mp4?token=ocDd8D05H9LS9mzhYVe2D2FDXaCcC7LK232mcq-TAbQe_Peo-FY5QwdDr1FL9fwZLSAClNLovr6OTRkYW10_UJrxchuQgzhxBrTQ_M8grZYmgX8msNehCH4Zejtzn_4VS9AUMTEk6LrME7Gz13gSha2i9FzCAzD-CKuGDTPfP6tmvqTgJvONASnzIA34LKtbuyF2QB-MxYzeMws6vuE7EiHxGaezx5OLwn5VEyjLjLgUZ4SS86jOEUsexu61a1Xc6WoBJ5t1D1JKOexCsvw7ke_a-YoR9f00LziCizLQRugyja-PD4zVsGQqsjcHUKOii1d7Xi876XEE6SnLZBIlVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خواهر پژمان جمشیدی: برادرم جوونه و با دخترا حال میکنه و نوش جونش، عین بقیه جوونا داره عشق و حال میکنه، زحمت کشیده و باید بکنه
🔴
پ.ن: منم جوونم و دوست دارم با خواهر پژمان عشق و حال کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143020" target="_blank">📅 14:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143019">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=GJwXQKSQZ3GUBuJXsuYexIWZK7dP_TJxFunHQA7nhel1irdm7kApIgnAUWLl2FQRCvoFD58Do1fiu1nz0i7iAi53hUHVUF0rLOVVkU3uZhuKVQMygZOvQ2OgSFNOx4tLXulgCEM2MJJQim0e12rRYmITKDpRZCotNnCwEW-9D-DC-qCdUJbAVM3lkMwNP0XqPwX2N5idJBhElqGBe_sHl0ebvHhuoBsKpwt87Xm7FJI_BQXM5ZVI_-ZSpC_2nNLb9OmHCKYEGC6I0_tXrP8_w1CfnuTQZXbYW8OLo-ypmrQ3HX-Xvu1YNJgQOZIYk86k2uqg1rBeNcVnEBM9Z41HpWfYim_rIe-ffRRsJoyNMoffGJC1dph9XqCUU-5-Xi7bn0tn4Pd4y_kWCxiN1esXNADczGHI1LIX2WOgKlVIX1KgUxF54mnYPtSElhU9ssrvDTqyLmd6Cktn2jYivKzakoyP2cKCpz757N7EQo5AeU-zP-JLp6sz6mmxLaOPiNQQwKrBy-kEdG93UL62lqnNMoAHEM14yFb5MAE9oLcIxMq-2QM0QCofuqKyQ0UfGCQtcTF3qVORN6aQ0xva8fUQSGInHrhKKOaBsgl9pIGLUUUqe5IAO5CFJLciHM1PeJlKQdSbv0sCLqDivEcWa9kvraVPBvYxfDBCTdLtH0eHdRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=GJwXQKSQZ3GUBuJXsuYexIWZK7dP_TJxFunHQA7nhel1irdm7kApIgnAUWLl2FQRCvoFD58Do1fiu1nz0i7iAi53hUHVUF0rLOVVkU3uZhuKVQMygZOvQ2OgSFNOx4tLXulgCEM2MJJQim0e12rRYmITKDpRZCotNnCwEW-9D-DC-qCdUJbAVM3lkMwNP0XqPwX2N5idJBhElqGBe_sHl0ebvHhuoBsKpwt87Xm7FJI_BQXM5ZVI_-ZSpC_2nNLb9OmHCKYEGC6I0_tXrP8_w1CfnuTQZXbYW8OLo-ypmrQ3HX-Xvu1YNJgQOZIYk86k2uqg1rBeNcVnEBM9Z41HpWfYim_rIe-ffRRsJoyNMoffGJC1dph9XqCUU-5-Xi7bn0tn4Pd4y_kWCxiN1esXNADczGHI1LIX2WOgKlVIX1KgUxF54mnYPtSElhU9ssrvDTqyLmd6Cktn2jYivKzakoyP2cKCpz757N7EQo5AeU-zP-JLp6sz6mmxLaOPiNQQwKrBy-kEdG93UL62lqnNMoAHEM14yFb5MAE9oLcIxMq-2QM0QCofuqKyQ0UfGCQtcTF3qVORN6aQ0xva8fUQSGInHrhKKOaBsgl9pIGLUUUqe5IAO5CFJLciHM1PeJlKQdSbv0sCLqDivEcWa9kvraVPBvYxfDBCTdLtH0eHdRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو جدید از زلزله شدید چند روز قبل کلمبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143019" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143018">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
👈
استفاده از متانول در بنزین تولیدی ستاره خلیج فارس تایید شد/ احتمال افزایش خوردگی در برخی قطعات خودروها
‏
🔴
مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
‏
🔴
انجمن خودروسازان ایران پیش از این در نامه‌ای هشدار داده بود که استفاده از متانول در بنزین سیستم سوخت رسانی، باک، فیلتر و پمپ بنزین، لوله های فلزی، واشرها و قطعات پلاستیکی را دچار خوردگی شدید می‌کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143018" target="_blank">📅 14:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143017">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
الجدید: نخست‌وزیر لبنان، نوفل سلام، تأیید کرد که هیچ تاریخ مشخصی برای دور بعدی مذاکرات بین لبنان و اسرائیل تعیین نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143017" target="_blank">📅 13:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143016">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
پزشکیان: جنگ باید در یک مقطع به پایان برسد.
🔴
بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و آمریکا در دنیا منفور است، جنگ را پایان دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/143016" target="_blank">📅 13:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143015">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نخست وزیر عراق: برخی گروه‌ها سلاح خود را تحویل داده، ارتباطات سازمانی خود را قطع کرده و به حشد الشعبی پیوسته‌اند؛ با گروه‌های دیگری نیز در حال گفت‌وگو هستیم
🔴
هیچ قصدی برای رویارویی نظامی با گروه‌های مسلح وجود ندارد
🔴
اجازه نخواهیم داد این کشور به عرصه تسویه‌حساب‌ها تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/143015" target="_blank">📅 13:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143014">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
عضو کمیسیون برنامه و بودجه: مشکل بازار کمبود کالا نیست، بلکه گرانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143014" target="_blank">📅 13:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143013">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
اعلام نتایج اولیه آزمون سراسری در اواخر شهریور
🔴
رئیس سازمان سنجش : تلاش داریم نتایج اولیه آزمون سراسری و پذیرش دانشجو- معلم سال ۱۴۰۵ را  اواخر شهریورماه اعلام کنیم سپس یک فرصت یک هفته‌ای برای انتخاب رشته در نظر گرفته می‌شود و  پس از انتخاب رشته، مراحل معرفی و مصاحبه رشته‌های دارای شرایط خاص و شایستگی  پذیرش دانشجو – معلم انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/143013" target="_blank">📅 13:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143012">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
یک سوخت بر: اینجا تو بلوچستان نه شغلی هست نه درآمدی و ماهم مجبوریم بنزین قاچاق کنیم و الا زن و بچمون از گرسنگی میمیرن
🔴
حکومت ول کرده مارو و پول نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/143012" target="_blank">📅 13:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143011">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اختلاس مدرن مسئولان نظام و توله سگ‌هایشان
🔴
30 میلیارد دلار ارز از بیت‌المال به چند شرکت داده‌اند تا خودروی چینی وارد و با ۲ برابر نرخ جهانی به مردم بفروشند؛ با همین پول میشد کل شرکت bmw المان رو خرید!
🔴
فقط مدیران خودرو ۶ میلیارد دلار گرفته؛ تا از شرکت چری که کل ارزشش ۷ میلیارد دلاره خودرو وارد کنه و سوبله توی ملت فرو کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143011" target="_blank">📅 13:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143010">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سریع‌ترین ستاره کهکشان راه شیری پیدا شد.
🔴
یک جرم کم‌نور که به دور ابرسیاهچاله «کمان ای»، ابرسیاه‌چاله مستقر در قلب کهکشان ما می‌چرخد.
🔴
این ستاره که S301 نام دارد، در سریع‌ترین حالت خود به سرعت حدود ۲۵ هزار کیلومتر در ثانیه می‌رسد، این یعنی این ستاره با سرعتی بیش از ۸ درصد سرعت نور حرکت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/143010" target="_blank">📅 13:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143009">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab4f4f325.mp4?token=moapf8Qip4kOMJgEAv5ICvas8LBGSf4_9pHG3y8TCuw4c-34tyJvgLBujJXO0HYprtsoprgtYijejoqAeDuLx-EntFFpBIPrBlKLmk5SlKEvi5Hos18M4xeLcLy_HLX3S4oOwY5DQB4zrnIVHZKBvAOOziu2HTHPZuxtUGPjN4J-WTdpZRhIXRh3Ae1rxdeYji1G5G2jdjKvyBTJue5JLC0MJi2DAN7KVZ0-ZoDmmPK2B3ZeY24whv44JDN0iINqeVz3Q84WlBBF2Zq7a-3BMgW3aqBnl3JLUAsgNy4XLQlJezDEBGGsa5qI7JBw4v3VXbwuH6_lfVA_GLmNUgnhQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab4f4f325.mp4?token=moapf8Qip4kOMJgEAv5ICvas8LBGSf4_9pHG3y8TCuw4c-34tyJvgLBujJXO0HYprtsoprgtYijejoqAeDuLx-EntFFpBIPrBlKLmk5SlKEvi5Hos18M4xeLcLy_HLX3S4oOwY5DQB4zrnIVHZKBvAOOziu2HTHPZuxtUGPjN4J-WTdpZRhIXRh3Ae1rxdeYji1G5G2jdjKvyBTJue5JLC0MJi2DAN7KVZ0-ZoDmmPK2B3ZeY24whv44JDN0iINqeVz3Q84WlBBF2Zq7a-3BMgW3aqBnl3JLUAsgNy4XLQlJezDEBGGsa5qI7JBw4v3VXbwuH6_lfVA_GLmNUgnhQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هندی‌ها به کامیون‌هایی که گمان می‌کنند حامل گوشت گاو است!
🔴
ده‌ها راننده کامیون تاکنون جان باخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/143009" target="_blank">📅 13:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143006">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1tANR9EtM8djW1RVQMPI4LQ-5HJrTr99FWYhPQTqIYAZ7mfMEM44CsXaDTIPy94sSJH2R8vPH0X2PKzBhHqa6SqccHGYN9b00wbz2g2t0Djka_g7jERK2y9UOtEBGcpUOsKj2XO5gE8E14QEzN5l552-nrzx19b-VWnDuVFxojHupPn9-mwm2ZWQACpIAUbDyuu3oJuf6u2gOg9PON1Hk1gXk9imKhIml8XQTVHO2cV282-w46XZ-TqS0pAQjhaoFoVWVs0xcX89nlbX2k73KhBNH2I0_K_knyDIdBov_Q3NWhYgu_5OtPa1a9wYaDoUb5yNwawd0KqsnIwfOxLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrJIh_6X2ViAuNjA8P2CLcghbOTr3IGaZ8SqaAP9FP43myrcu4bc8_ZDmmVV_GKEKKqSc870zK0jgQf49LC1gVGhbL11P0TMl-y6-_JZJnAXCLDpoUMw2Y8mpSS6w7mfav995n-SqIsYFyoSKCDETB7Z1d3FwqYo5nciZrpKSFAW56fdmRpHSEa27_xMcmnngJ3jpvxqE9OEeX432hriIGsMNuwZN2R9eE4S3fVr9sl99LOo_pOfsvQWshg2qvACrtNEcXyzEvYTFeqW2-ieoAzVVq-AmlO8mRAo9gFVwZJgX8u1RQB0NAF45ZV6CKnXmRQgdbRxHx4zxfBFzWFnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yloya2fvrplw9vyF6RcsndoBrUEBXvTt68h3rba_uX51jVBKLQAccod9VImQPkvCa6z7XDSIFpCt8xVSZ6GAxC3svM0OE016Ip7tlkOTs9DH-p_p5ODxrt0SCVGPOsOarXk4JNtc9FMtLnGUuNexJWvORUm6w60ZHVWJ4Q60zbkDEl7gumAylAZ3PbYi0k-BH43hPUN-yV2ykzYkkd2ChjHH5mfeEMkItgCH7nyCXwmvmQjbbBHZboRwfcvGbzoMa9KIBYwwerbQot03J1qFmTEV8zLb1pTblxk_J1TkY0d8qc0oliQH3Nt-WHKJEfJPzqmmsr_CUZc0O4ru-KJNMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143006" target="_blank">📅 13:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143005">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnAEHjY2tXptNB-GSLwNX5aXyj67cbK7BKNG7ba1s_oMJ6SLkHU_t7-W4837Ec8vyZrRogtcGeIU_p8jnAOVbyPdr5PNT4ImeoTXqVm3WbD6CkA2F15UysVCObOD-nPEIXBU35TgJvYfRHlS27ae0uZmsr_0YS_hM2thr5MMwesp-co3IVUCDW6bxn9TVYypmXFbm-8V59Slf0gUoTm4Ub6LK9UstV-9eKnkV36K5LPofrFbXKJwcX6mKNcTLLLXbe4-7iy8aqP0REexmFiDlkldFujADUCNxsu-aNmC62iEUX-xEDSoUiqAi4YOHDN0r6rTa1-Svei6EVQTHU6rIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک تانکر نفتی سعودی از تنگه هرمز عبور کرد، این بار از طریق مسیر عمان-آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143005" target="_blank">📅 13:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143004">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwmapTb0EzaK_2Ek1rtYTfKPMntI6I4m38UQiHD1wzcLUZCasvjXLbTMo66MEMOddaU1Zc_JtfTwm5WwKdoH57esJeio-_-S-_o9BcA970i6I4ooyNGnTBs3geDEnTCTq0lsBo3d0sWI6MmvmbfUW5z9kzeXRtaqGjO0FvaGxrqU0Dj_ZKryIVhwkySv6vVG3nFiMBfuk8J3VxpzpWRDH6INJwokhvyO5yWKFl-A6phNuEBersl-JK8wU-B1rQwrtMGHF2N9VuhkrAoo9X5H2LvIfhoyFQqKKIm0WML5ExcxyRxBG1MJZEUE7ws0uqezwABSL4vEfIwobyqIpeNoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143004" target="_blank">📅 12:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143003">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
قالیباف: مسیر مبارزه ایران و عراق با آمریکا و اسرائیل ادامه خواهد داشت
🔴
آمریکا و اسرائیل بداند که وحدت بین ایران و عراق هرگز گسستنی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143003" target="_blank">📅 12:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143002">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بیت کوین 79000دلار شد
😐
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143002" target="_blank">📅 12:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143001">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بیت کوین 79000دلار شد
😐
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/143001" target="_blank">📅 12:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143000">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4d99d90e.mp4?token=XdOipTZbMcnA3rSM8KN0u3o9RMVT3W1CJHQXKhUCwFTtpIfVBCQUoYoH48Iqo20iIR-hL0QAAPN4kh_I64Qvn7e5NnWJMYVLt046JLyz4aBpfmao_cNL9Hr1a7Fz86iIJ9TpT6g3YgIGBec4RYeul43shjcfWWHXWcpHLt3b6iRYPSk-wbiebAsdBmmkog-FuTYsMBZGNY83Hi2rzX13SfUgvkvUhQ53b5zbOvKFSXwowpvtEin6HXd99HjXiGmA9TaLUnZTbmTtl7b5FX9M2vyPuYMHltTagX9ipFOMSUESKvycGKKPYo-pVCeSDMY5xm1NExR-BmN0kHPhCrk2VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4d99d90e.mp4?token=XdOipTZbMcnA3rSM8KN0u3o9RMVT3W1CJHQXKhUCwFTtpIfVBCQUoYoH48Iqo20iIR-hL0QAAPN4kh_I64Qvn7e5NnWJMYVLt046JLyz4aBpfmao_cNL9Hr1a7Fz86iIJ9TpT6g3YgIGBec4RYeul43shjcfWWHXWcpHLt3b6iRYPSk-wbiebAsdBmmkog-FuTYsMBZGNY83Hi2rzX13SfUgvkvUhQ53b5zbOvKFSXwowpvtEin6HXd99HjXiGmA9TaLUnZTbmTtl7b5FX9M2vyPuYMHltTagX9ipFOMSUESKvycGKKPYo-pVCeSDMY5xm1NExR-BmN0kHPhCrk2VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تبلیغ بستنی میهن در کشور امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/143000" target="_blank">📅 12:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142999">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsCRWVJdc4QBvGW3gzT0Zgld5ndYnq4LI_AAqwFFUqbOS_whFwBVoyJwd5yB8twr1L-ekj7329LYbtXg7m37biuTr2sS7ClRDB4JKCQ12Q6-UgsexkG9bSF7oeU9lr5c81KB9Oe8d2XF8nj61Nd3CKe2bvmrSit9Ivt4ai5-7dkGD-yTTNexbmeNiyUx8BeviLjMK9gBmOxI_8YmR6nH2M6Qqvs-DP2TGQQRqNQ1pBP-dIAhtecYoURsoDW8E6YBIApUs9nWhXcjtBbL1M9Gew7viY9GibMcIx8kPKRiOxH5-JJNTO0JRQKw_Fxq6i6m1fXFviI_2siVVH0UcZ_dMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ای‌بی‌سی‌نیوز: FBI از احتمال حمله پهپادی ایران به کالیفرنیا خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142999" target="_blank">📅 12:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142998">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c16ebc80a.mp4?token=R8DhPlWT2oaoGv90-A0DllutNvy4a65gzYHai70UbXRHFFiHHzSsYwvFy5n3HyjpbagrDIh52mS4z8rZInPrmb-XzTmy1lauup7-PaJeIY9mo-C7h5iQDKp4Lm2-dVSZhvW5i_Kj3rn6-60SvM8XgWyYwYK7efI4ktUj3vuUoBb5IFL0_lpwA7e-l3obqpCqR1OqMKGzZH2CHY0_GyHvu43U10JsO-0li29xBktQzwYqPMTcEuISD_i__5Z-0zQ2InepgDbBTRdTVAKJDN5hBNeahmYHg1WsdvKbbWtfBgDqmiaRsTjdHi-CbEV84BHF52i5iNKhetISztAn2pSmew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c16ebc80a.mp4?token=R8DhPlWT2oaoGv90-A0DllutNvy4a65gzYHai70UbXRHFFiHHzSsYwvFy5n3HyjpbagrDIh52mS4z8rZInPrmb-XzTmy1lauup7-PaJeIY9mo-C7h5iQDKp4Lm2-dVSZhvW5i_Kj3rn6-60SvM8XgWyYwYK7efI4ktUj3vuUoBb5IFL0_lpwA7e-l3obqpCqR1OqMKGzZH2CHY0_GyHvu43U10JsO-0li29xBktQzwYqPMTcEuISD_i__5Z-0zQ2InepgDbBTRdTVAKJDN5hBNeahmYHg1WsdvKbbWtfBgDqmiaRsTjdHi-CbEV84BHF52i5iNKhetISztAn2pSmew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک: تلاش برای بازگرداندن بینایی با تراشه مغزی
🔴
ایلان ماسک اعلام کرد شرکت نورالینک در ۶ تا ۱۲ ماه آینده نخستین آزمایش تراشه بینایی خود روی انسان را آغاز خواهد کرد.
🔴
به گفته او، این فناوری می‌تواند در آینده با انتقال مستقیم اطلاعات به بخش بینایی مغز، به افراد نابینای مادرزاد برای دیدن کمک کند.
🔴
ماسک همچنین مدعی شد این فناوری در آینده ممکن است توانایی‌ هایی فراتر از دید طبیعی انسان، مانند مشاهده طیف مادون قرمز و فرابنفش، ایجاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142998" target="_blank">📅 12:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142997">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afZybpBL8fIABJF6rvsSdFcLsQxiAc6D8ygq3YjhAESYJW6I2pDfO99LH0MdhSvxV7qe2OyfCDp-4QScenYGe7EhgvJtfepqFLtB0D6hW3EOytsbsUrmd3FCkRPxlQ3g_IFi90OraxGq6vbBWR39u-FhcuUThVYiM3xRwgmeUURN1YJ0N12T9MTx5ACPWLKydKzRw0kOju-4KXUWz85NpH8rsLDvofqXKVsn4HapzRu18s6gJE7jZlxnM6XteMQHJfKeacHFrkGYoreUM7C1rQyiqPAuHRW4vCeuF4lwOlgUNUs3UlXQwcaRJt3sLqskkQVJfYY5GYSWXt59pbGSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجید شاکری: پاسخ نظامی ایران به حمله اقتصادی آمریکا ضروری است، هم معقول است؛ هم به موقع!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142997" target="_blank">📅 12:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142996">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
معاون وزیر راه: هزینه بازسازی پلb1 نیازمند تخصیص بودجه‌ای بین ۲۵۰۰ تا ۳ هزار میلیارد تومان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142996" target="_blank">📅 12:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142995">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230ca39aff.mp4?token=sWV4J4YSwD3vWW-uM0bRrFBuqEhN-Q_Q3oUYpU4Z013dwgQWBr_A5MH2vrq8F5ZShmaSf0cGuH3K72CRlOTqe2LMiHdT9Fnk5Gnf4ATus978OGa0KIElsR-RDSK777GtuCh5G4tSiXgFwnXaG2N0iH-1o5zrJJbaL2wKa5ii4No9bpgBh4Ab9F6ifFLWiJ15m8B-5j2af8OBJZ6WM3DgszDRJsyafOsUrH4e4kIDjxCqePMPIt3tQIOyJukb28y39XdMPFVESLH4ERykVKEpQLEwi8VIA-MK9hKaZzgE8l4EoEMHNODcTP40_xlDysVE0QlN2fKRoSSnE14dguWi1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230ca39aff.mp4?token=sWV4J4YSwD3vWW-uM0bRrFBuqEhN-Q_Q3oUYpU4Z013dwgQWBr_A5MH2vrq8F5ZShmaSf0cGuH3K72CRlOTqe2LMiHdT9Fnk5Gnf4ATus978OGa0KIElsR-RDSK777GtuCh5G4tSiXgFwnXaG2N0iH-1o5zrJJbaL2wKa5ii4No9bpgBh4Ab9F6ifFLWiJ15m8B-5j2af8OBJZ6WM3DgszDRJsyafOsUrH4e4kIDjxCqePMPIt3tQIOyJukb28y39XdMPFVESLH4ERykVKEpQLEwi8VIA-MK9hKaZzgE8l4EoEMHNODcTP40_xlDysVE0QlN2fKRoSSnE14dguWi1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از آثار حملات هوایی ارتش اسرائیل به فرودگاه ابوالظهور در سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142995" target="_blank">📅 12:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142994">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc041fd169.mp4?token=D5Fci2fEjKRPXJy72uWGvRhWcZrWoMryEKHjJbDsHicLEfkhX5OCn_XahFmMNccsUECrDGffXQJxTlB43DHMhsUqLngMEGL3FVikkbQv_Yl-NaBh45Gzka1Rt8OEiQp8vQRHACSZnohMebUOp2-MlD_J3VjP68bBwJmCPFj_FCYJJ4ijN8811dPOrQtSJXjRZuG1ZqAblESmpuG2-JQIqoHSjITAwPjWDcQvLHY5JW3lXKb2bhA9IId1a1VpodpZmMSXvoyG4JljomEvQOVI_aIufBYXOJWWkhMfhqvAd8JMquw6Azbi2bfuG8ihX81OZaqXYFgwqLRAQc0rlpwkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc041fd169.mp4?token=D5Fci2fEjKRPXJy72uWGvRhWcZrWoMryEKHjJbDsHicLEfkhX5OCn_XahFmMNccsUECrDGffXQJxTlB43DHMhsUqLngMEGL3FVikkbQv_Yl-NaBh45Gzka1Rt8OEiQp8vQRHACSZnohMebUOp2-MlD_J3VjP68bBwJmCPFj_FCYJJ4ijN8811dPOrQtSJXjRZuG1ZqAblESmpuG2-JQIqoHSjITAwPjWDcQvLHY5JW3lXKb2bhA9IId1a1VpodpZmMSXvoyG4JljomEvQOVI_aIufBYXOJWWkhMfhqvAd8JMquw6Azbi2bfuG8ihX81OZaqXYFgwqLRAQc0rlpwkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم از بمباران هوایی اسرائیل به شهر باعراشیت در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142994" target="_blank">📅 12:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142993">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMXqlxYQq4qHMUZrNaXRgO7eelzgkkaEv6Dfsqt9xY4gbVkhcEUwtOE75WptYG9BgXnuYLyDzyIwaV23TdmE7fFKdXn4XI4aK_EOz3nLdHnfEmG5PBiXyF5VgeOnhgcAFQM9mhtN6i2JsQ-Ue3pz03rrBvrBaDbzfDNCkzvuhInQfvv0yh5BH5ZrXbbpPH95-oseFJp45_qxTfe06UIhQ1uJ_XyoYNHHdKy8OGuH1lf8R4utnQr1e6G2oGkxZEKPv8XRYA8gXl2B5bRBJAGnyywG8VBBYVTp1bwk3UUVACEdvgdPyA50AZ_3Z3D7chRcUTvoSGRDGPWNsAt4C18bBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیلی به شهر بااراشیت در جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142993" target="_blank">📅 12:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142992">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
پیشنهاد اینه دولت کافور وارد کنه چون عده ای با دیدن مو هم تحریک میشن
امت مبعوث
❌
امت
حشری
✔️
🔴
یکم ب خودتون برسید تا بتونید زن خوشگل بگیرید تا چشمتون دائم به زن مردم نباشه! وقتی شبیه گوریل هستید قطعا گوریل گیرتون میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142992" target="_blank">📅 12:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142991">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLJlEZqR-fzEtKlXWA95Y_tPw7zo-wL4q68S3yJC0wGkeec1tMm2PTSR_scpiUP9D8IPO8cxw760RT7t7hwpYUvWkg47qZJuknjPOkFPkcT9HdNkC7Hup3R9SZib2k5PSb194XwxuNaws1DXFfNL_Uw1i_DaDXuWbt5EYnz2aVCxhCn1SRp89v48nogv9oLoX-DKikXWMTqk1PM1B8hcrv7g8Bw6M4OVURah9WIjOgv1O89Xn4Cn-O8MIwkguxfisKzRQZ4-KWYpJZ8eGNHXfl14IvVVd-lvoSNT50HhM5TFhrOmo2pOP_WH71s-CZge6nBcIjLhx0tHQ8UWUHiiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
میزان محبوبیت روسای جمهور آمریکا در تابستان پیش از انتخابات میان دوره‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142991" target="_blank">📅 11:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142990">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ستادکل نیروهای مسلح: پاسخ ایران به تهدیدات نوین ویرانگر و پشیمان‌ کننده خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142990" target="_blank">📅 11:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142989">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv-Ki4bGH9Hjq5T2foK9qyDpya5qZG0bzaND9ona5lYlQ6N90wR6DprzTtAsGe7onM1Mx71gu-hMawpQE3q9QyOxxVjhJjlIHSUUeLnz8v4Yo0TXHcpQR3WUzSEj-JqYnCZvMPMHCqhgryVujnDzQftiqKvSDxMOMidEuyNOYof0mO9WiXoULpO0ny0FyYgParUO731Rx56yegHaaU5jBfrll8x0775RDiFoy6_Al1zU6PC9RzPxB2WLpacG8Cg00Sp_Gg0wuGWDuEuFQGiRhi6I8UkavwhQC9vgR114tyDCMebj9KPyQ_R6H_fyrs38NN6_HR8v6kNvR_jYZbtaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پر بازدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142989" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142988">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قاسم روانبخش، نماینده قم در مجلس:
قاسم روانبخش، نماینده قم، از مطرح شدن طرح خروج ایران از NPT در مجلس خبر داد و گفت این موضوع در حال پیگیری است.
🔴
او همچنین با اشاره به مسائل فرهنگی مدعی شد برخی جریان‌های غرب‌گرا، حجاب را به «دیوار برلین» تشبیه کرده‌اند و معتقدند با برداشتن آن، موانع دیگر نیز کنار می‌رود.
🔴
روانبخش تأکید کرد نمایندگان پیگیر موضوع حجاب هستند و از رئیس مجلس و رئیس‌جمهور خواسته‌اند نسبت به این مسئله توجه جدی داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142988" target="_blank">📅 11:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142987">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JkZdR2rFMzcioq3Qyn_AM7M0SfZK0LxyQ2YMmgECTVwM-5-R1ghSxhKQoGcgPWd0-RJ9cTF1l2BjVF2-i1mp529KuxmuBN52CEqSGyDoeLWlVA39owITdm4Bxo7unk4xewEMdlNAE2hz9bC998Abi8SV9lvoZ_G4a18_KUXHyfEx37yMSNOrJJcCKQsj4aPpWGM5Fokyx9ow3IS-Hd_EMmLxwm57AX_aWLjHSAax20KM6fDmhGl-EZ_QPii3_y12CwXeGSfZrbcsruJI2fF47e22V1-F9qxc5a9UnlTWo_T4u17_zm80dSSjADQ22AsiBUoCLJ-ilIEvoVre3CEkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه نفت پرم روسیه در پی حملات اوکراین حال آتش‌سوزی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142987" target="_blank">📅 11:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142986">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رسانه آمریکایی سمافور به نقل از یک مقام آمریکایی و یک مقام کاخ سفید اعلام کرد: دولت آمریکا معتقد است مذاکرات ایران و عمان چند هفته پیش شکست خورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142986" target="_blank">📅 11:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142985">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
👈
منتشر شدن فيلمى در شبکه‌های اجتماعی که انتقال تجهیزات زرهی و لجستیکی ارتش ترکیه به سمت سوریه را نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142985" target="_blank">📅 11:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142984">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزارت امور خارجه لبنان: وزارتخانه قبلاً به سفیر ایران اطلاع داده بود که اعتمادنامه او پذیرفته نخواهد شد و ویزای ورود او تمدید نخواهد شد، زیرا او به عنوان فردی غیرقابل قبول (پرسونا نون گراتا) تلقی می‌شود.
🔴
مجوز اقامت سفیر ایران، محمد رضا شیبدانی، در بیروت قرار است در ۲۴ اوت ۲۰۲۶ منقضی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142984" target="_blank">📅 11:03 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
