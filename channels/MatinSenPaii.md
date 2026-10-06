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
<img src="https://cdn1.telesco.pe/file/lFeoT09pnOBJHJOonf5e-tp6dBhjxgx6XUvJ8G0qAl1xEGiDsUFulGRZbDukptJzrYFJg80LVXAQNV0RF19IziyNzeV61WSIjdmjoJk5NdQu9yk3ioXJAkAxavA-ZL57r3ZjpqNSPh7ZMt4rqXvUYjFLaamdsxI2UbkeHT5ydnP2mcGqQGqpg3BwcP8E-3_GbUszkdpIKxfwZlkbAbx5KqGVKinxF-dT6Vo2k-uPw86U5RbvUxU_kWBZddsbcnqUtC8mvfVp1szgA7YSBuQq5kXzsrL3ZMy-h2-y8OqVllukngc2fWGN6YJIZth-3-YLm75uV8iQUvXDAiCDi70lwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-5524">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه قابلیت خفن به Cursor SDK اضافه شده که بهت اجازه می‌ده هوش مصنوعی رو حین اجرا هدایت کنی. دیگه لازم نیست صبر کنی تا کارش تموم بشه؛ با تابع run.steer() می‌تونی پیامتو به نوبت بعدی اضافه کنی و مسیر رو تغییر بدی.</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/MatinSenPaii/5524" target="_blank">📅 08:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای ترجمه و کارهای روزمره‌ام، اکانت آنتی گرویتی کم آوردم
گفتم به یکی از بچه‌ها دوتا اکانت بهم بده
توی پنج دقیقه بهم داد:) اصلا باورم نمیشه
و چقدر ارزون. یک دهم کلاد یک ماهه، 18 ماه داد
هرچند خب استفاده‌ی دیگه‌ای داره کلا.
اگر که اوکی بودش و نپرید و اینها، معرفی میکنم</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/5523" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArasTey</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo7r3eToHQ7PzO2drF9IISKBXVuF7PmfNYePr1PG3jZM6ZoFGRj-n6c1hYyDsl9HWZN_sfNjFuZFfLzTLCqDnReBWkD2QYZe-yfFj1QGz1mAaJqu9uRU4sNxNi_2IA1ugW7MjR5NhOulwHf76fuXtv1y9-aTE5FWyZdZirKnYb1LQ_Tf2YW0c_bsQv-czabavwDPMFA8ODyXXWqpQlf_kHPnjSXdT4_XO4pI5mT5XyYSWtIzvj589XYJ9rrbVIkj0RrVpP5J07sx136k3zMomZv-zoNwo8Xq8sQAidCJa1a1WP9nkgLM3ijlQdDKVWZAqn2yzc9HjWBCR131iP95MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه آپدیت هم دادم روی
بهینه ساز
که الان میتونید خیلی راحت ECH اضافه کنید به کانفیگا و کارتون راحت شد.
ArasTey.Github.io/cf-optimizor
Github.com/ArasTey/cf-optimizor</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/5522" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال همراه اول:
1. CDN/WORKER with ECH
برای اتصال به یک کانفیگ cdn/worker از طریق ECH باید ابتدا از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و در قسمت echConfigList به طور مثال مقدار:
cloudflare-ech.com
+udp://1.1.1.1
را وارد کنید.
2. CDN/WORKER with IPv6
ابتدا echConfigList و cipherSuites را پاک کنید، فینگرپرینت را روی chrome قرار دهید و سپس از یک آدرس IPv6 به طور مثال 2a06:98c1:3121::7 استفاده کنید.
سپس در صورتی که دامنه‌ی شما فیلتر نیست، finalMask را خالی بزارید، در غیر این صورت finalMask را باید tlshello-0-len (همان مقدار متد f&f) قرار دهید.
3. WARP with IPv6
از قسمت add aether ابتدا پروتوکل را روی wireguard/warp-in-warp قرار دهید، نوع آیپی را IPv6 انتخاب کنید، اسکن کنید، بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
جمع بندی راه‌های کنونی اتصال به کلودفلر بر روی فایروال ایرانسل:
1. CDN/WORKER with F&F method
ابتدا echConfigList را پاک کنید، از یک آدرس مناسب به طور مثال
188.114.97.6
استفاده کنید، finalMask را tlshello-0-len (همان مقدار متد F&F) قرار دهید و برای فایروال ایرانسل حتما باید cipherSuites را روی semi-python (همان مقدار متد F&F) و فینگرپرینت را روی unsafe قرار دهید، همچنین دقت کنید که مقدار ALPN را درست انتخاب کرده باشید (http/1.1 برای ws و h2,http/1.1 برای XHTTP)
2. WARP
همان مراحل فایروال همراه اول، منتها روی فایروال ایرانسل میتوانید از هر نوع IPی استفاده کنید.
3. MASQUE/H2
از قسمت add aether ابتدا پروتوکل را روی MASQUE-HTTP/2 قرار دهید، فینگرپرینت را روی semi-python و finalMask را روی tlshello-0-len قرار دهید سپس اسکن کنید، و بعد از پیدا شدن آیپی اسم انتخاب کنید و سیو کنید.
////////////////////
دقت کنید در برخی مناطق سیم کارتتون میتونه همراه اول باشه ولی فایروالتون ایرانسل باشه و بالعکس سیم کارتتون میتونه ایرانسل باشه ولی فایروالتون همراه اول باشه.
سایر نت ها هم معمولا از یکی از این دو فایروال استفاده میکنند.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n5FywmdaQk2qSwoQ-_ARTAdYx3CR8Kt_NgZ0N5WZDpJnGDPVysmtZ7oftEP_tHiQb8RaDJquVpIfEwEZDF8YKLn584QowHP0DlhMLg_rkp-F8n3HBTvpMeZCsKM2Jyj57GbXIFUpYs8gy9r8rmJ3I8NFJCKSplkkZZBOFZtG2qjMXNfaXankn8zOKEd419ILnQXSPnNzwXU0fV3h7kHmY1LoFXYGqm-NEBVDhzrXf1PTHAdk3rDDtapOuOhQymnni5Mr0IH5RT9rSvxLTMbPck-6ddZrx4bQzgCujKib6k5ZZ_QjdUoOzrXaAiS2mitZbS--LL2lB5PE5ABwrQvX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IG13hE2vZd3Gm1u8lgFqvGMNvtVQlhlfoNO7wknYbIh7HFTU4JOYxJY2hdXGtsTSSM17sCeWNDzYn6KiEJCa-zffL_Beuz3sQoQdIvuDMmbizZIxMe5i5x4ZxWL5g97f9QkWAcO87l07fOuvXXYE-pgiFzjMpmk98GIyNCHJZ5EmNNHs1M7DS1gZcp4ftzBSigoqGalZ5Y3qkZeP9kpOspO5icquGK36UYisPVmi9wRP_HnVuUkwxnc1vTi18DxBuaI2Ehx0hm1-a-kRgw8pj7tPDoTSwvewFCE8lz8ECPudgBAwPmkm42SDUUUSQEJiDEjqcE265czoGGheisYBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QjwaQfD4oA_Vo7worOjv1jCDm8a1mQrxDLj3BTZbMHGpAGcSXU7gqD1aFqJ1rpCDlXDCHAyH_RJdVgssxPON9tpSAgJ9fT3uoh_ALXJc3mLSVtYVWPOPx0ZVeQCjjbGUGk0s6Ky9lCPZPWIJpf16PqU2QtC0dIGKoD78GUZL-z6q1En_0wvSnKL7i8-p03J8lnc4NQFcE0Nxgi4CVlgMcWG3DdRaOs8bXr0OaMPnbMaBWn9ejuaYPuHYVu87Q2DbAuqcT9W25SReKE2s3lo3gcKnPNCrROdFuTfdfvj5rpH0ff1ZOsTc7Sr2p8OrA1s8D1oRQ8QhfTEIM1oYp3E-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/plPVGcSsf4FF-kQkw9eu0EYwNQH8LKix8TwIG9wK7n2scS7EhqSn3nKsWZsnTlxQVpsu0OoZ_t-YZjzk-mOEkRS4Y92jLWqEZF9M1JGQERJqbd878137m5TzcKP4gNIObFfPav2lipI_aS6_PhISzKPpaVtbul9Q6mgVz6mClkk5HBZcFAgq1zNwheNJmYM_sRyGOJ0tIYwFrJIcEHRP9uEvC4JFZxTmNaou8bmPUfNPxzE4H56ta45tbqQzbY6HtQsdgpEYr2VrMeYeVNmmiAesGROH29gd3_5pfAK6tDKdWJj1zU_eJB-64TWXp3DDW6K_BV90ExOk-fbRf1OkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_rPabP-EHdTQfbRL8YmHjMbWNfStiv0BBCcDha4JKf4Lmyk2Njc7YqhECllUq0W552q19JY-llrMxWVK0fkJTCmdDXQ2IsVTCcAMporJ4hyJ8_mTuWJDODRTc0_zYfw7GQPcDWbpaSMH1NujtMTd0AzvxQienem4CK51hlclw932RSToRV9YQDjnQ9xOGmQiYMT0r6Bz_7I5NqeE5XDfl4AMmspoJAl_xTPV3Vy5_a42aHkGmn53_G46nQbPsNZXD34JAvr9aoWqPrKq_erv8iAwrhuaerk9ePLISRvjTNqAN9m0dMvVqlpsMmU1zIo16IlOpcPL8615NGCMn6hoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l5H9Ze3jDeIptlsSDklYtQBgWVvAyIN2-_bwske7qr_FwNCgsYBTIsvijgB4wZe2Z_9BP1CiVC8hNhq-tWhym2z0XLeBTvx1hDBs8Bw3SGl9u30aG2eEK2dvUUwe8R0RsAkzaMnY7kR1Cr0Ocst43s9VHYdexLGInkRhb7TnOMihrC2wfamKMwKK6KRi6zR4IE7r29ySVUFwWzWe-qXodAJQREBr42EnNwB4omTCAUYlKqwoYEM_Vb93lOf_uSCskucK05Dr3WkY3fLSEhvPOc8MPLg4WcCbT4Umq1OJjyNOb0U9Tp4VaTlIXCUVSYNHRCZq5NM-a4JaKmSKYH-FAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده.
توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل.
توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی وصل میشه ولی وقتی میرید جایی که پوشش شبکه وجود نداره، گوشی وصل میشه به استارلینک. یعنی همون اپراتور قبلی ولی با آنتهای فضایی. واسه همین اپراتور تلفن باید فضای فرکانسی خودش رو در اختیار استارلینک بذاره.
حالا در مورد ایران قطعا هیچ اپراتور ایرانی‌ای این کار رو نمیکنه ولی لزومی هم نداره حتما اپراتور ایرانی باشه، مثلا یه اپراتور امریکایی میتونه این کار رو به عهده بگیره. اون وقت شما وقتی دارید شبکه‌های موجود رو جستجو میکنید، اسم اون اپراتور رو میبینید در کنار ایرانسل و همراه اول و غیره.
یعنی از دید موبایل شما انگار یه اپراتور جدید داخل ایران فعال شده.
ولی مساله اصلی اینه که توان ارسال از موبایل به ماهواره خیلی محدود و ضعیفه و حکومت میتونه با ارسال پارازیت کاری کنه که ماهواره‌ها نتونن سیگنال کافی دریافت کنن. حتی توی مسیر ارسال از ماهواره به موبایل هم میشه پارازیت انداخت.
تفاوت این تکنولوژی با استارلینک اینه که توی استارلینک امواج رادیویی به صورت مستقیم ارسال و دریافت میشه واسه همین شناسایی و پارازیت انداختن روش سخته ولی امواج شبکه موبایل توی همه جهات پخش میشن و میشه راحت روش پارازیت انداخت.
من مخابرات بلد نیستم ولی اگه کسی تخصصش رو داره بهتر میتونه نظر بده که آیا روش عملی وجود داره که بشه سیگنال به نویز دریافتی و ارسالی رو بهتر کرد یا نه.
ولی میشه گفت توی مناطقی خالی از جمعیت که پوشش شبکه وجود نداره و در نتیجه پارازیت هم نیست، این روش جواب میده چون پارازیت پخش کردن توی همه نقاط ایران اقتصادی نیست.
✍️
aleskxyz</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OREVg8_p86p1yOUy_JDROHlMBO3-7nCzlKKnLTeWsijSWS0rFgw3InB5rRTkzr28Aqs9H6VYmhkkQ4GVlGM6z9JD9KMHK0k6Z8Br53iVbohtpZ3NSO8ZfPQtPvfSGahPyZsaf79qUcsv-SvCopqlV-9nMiUORgcRobXR0nTzLEynhu5hmD5V10n58MjOaEOTsDaeNFjEV01Y57KQ7hHPL23bs6UBujGwyMjIHBMlSvzgzc2IhK--2AFna82ZbbOiwtYM2AoR3D6yfow2RenXIgtIIwLfNDbYplyjJHi-m289xadgwMaOAaO4_K-5vkW_Iu5QM-nzDDKa6T4wIm9Bkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jt8gSDCUiH5S_99ziAHjdXbOj6Zd1bHBdxSSK21D2dXKcJziCj-vad-KAC3-cv7x1z9PmeXY_C8CjUfezuallDE_iHRILHiDFih1jND4w_suMOuOT_o3SBLySIZmdz4y5a4ZZKiVm2c-kZaHJGf421mRHLgJsUmWtpMUMgZ5I_hD8M3ZoxJM7XcsOOYn9fAng4zrvTVHuQp5HqTd8ERGa54D5I8ZR0PuwP3VkjzQo2vBFbLHYMaCVthsKQKSt6NGYjuuj8v5gKSRzxE3BDPtXydSwVSnL92Kjw1ZQFr41EH2m0x9syrmfw-fVolpX3iBzwg5Q6RavK7WA50uhAQMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AdiQN5DLLtEUqDK_S3Z--g0swJlfrignkz2TXLVxp2brfQYLbFcCSPr0aOX_XJfIKtXTWFsqb3UlUeWSCvHRL9Hi7htP01DrGc7zG31Kk_kzB0V-gVmVixN3JXOkNVQ_PPu7pOYTh8MMbC4Uwiu1hgrWYwF-OYyktnBU2nmfrjYNdiqCABcS5_d5oJrxn469NaZmOeJd7jDY0v8iofvbFtbFkjrOTd_BYwc5KyoAon0gQzVwxi1WArFwmEtqpe_c2NS8ijeaCsIqIiR9bn1ajwYWLKmDSFxM33TLsNkjrWuMw5hNDn-kwxoOkC8nGbH_KG00KWG7Wj7nnMOeFgN1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه SenPai Scanner v1.1.1 منتشر شد
"برای اندروید، ورژن قبلی رو حذف و نسخه جدید رو نصب کنید"
• حالت متنی برای صفحه‌خوان (NVDA / JAWS) و افراد نابینا(ببخشید از اون سه عزیز نابینا که درخواست داده بودن و انقدر طول کشید. این آپدیت رو به خاطر شما خیلی زودتر دادم
❤️
)
• قابلیت Anti-DPI: ClientHello تکه‌تکه می‌شه، همون کاری که توی PattNG انجام میشه. مقادیرش هم قابل ویرایشه
• حالت Gentle برای اینترنت‌هایی که وسط اسکن قطع می‌شن
• Paste کردن IP / رنج / دامنه و شروع مستقیم از فاز ۲
• ذخیره و ادامه‌ی اسکن بعد از قطعی
• اندروید حالا همه‌ی قابلیت‌های دسکتاپ رو داره(برخلاف نسخه 1.1.0 که دیشب فراموش کرده بودم. این الان 1.1.1 هست
😂
)
• نسخه‌ی ۳۲ بیتی برای Termux
🛠
رفع باگ
• تست سرعت مستقیم همیشه fail می‌شد و الان نمیشه
• و Stop بعضی وقتا روی اندروید کار نمی‌کرد
📥
دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
این نسخه‌ها تماما روی گیتهاب بیلد گرفته شدن(مشکل اکانتم به لطف یکی از دوستان برطرف شد) و دیگه شبهه‌ای توی امنیتش نداره
👋
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t5675K_8bt59oMusVNyEMQBUbq3ro2hxaDpYnIQxBx3Zn1uR9UtiTneLmistkU3mtDwpj9Ea8zLnezrZoEFovcWbZagUtJob_2n6-fXg4Tf7F_rKEJJ09aFHzSCVYBLfLPVC03ST9qNPavbNQsv6vGhxc8_3pQC4PjYnmcT3Ma5MV0qrJ7TfYU_hV00U9L7gDA_RxRZrQSc2ScBx2TQfnl8ysxhiYKFQUQQrZWuLUOJ0WO1bRxc-NB0wmHDVOFIH0jHELH2oSQN6ZvZPGjZ2kVHk4NfV3pwRi-eym0QR7Fsn4jvwcQ5G3tEcQpGEzTBxTPM-whYsfCou99_N5si1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sRKV7Rdep8-cXyaPIGGnRUAU2VT9TXtAaefRYJBHzQjjeIYrTZx1igMu-CZAasFZkeSY2TPPyCgKUHNpQ2xc2rgiV3PqtJH37LVHg4P-imak5X3ub5SRPe8iWjt3URWeleen6d2R1tf0d8hB3iNXXYZrYPKFMpVsyM376enmxrCo2Dbz5BN_Qt-Hg9G8pbUt22yb2qxt_lcHDZHR7PNy0N7W9nZXej9K4JBlbdMcfLQqcKas_d9nGU893lm-lIuzpcYuUQN3Pvevggr19Fp8niqiLycUW0hB8ffdNgzZ-9OdH_ylVxC3OiQORMme8eIkYVJ0aNn9AS7o0Eyb3M29dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cW34fjnwi-K1xz2OgopkREHCrh43lb3SHqhnSCNvTMj6tIgXzebpfIbHfvX9V3cKgvUHWATNMolvIjbd9MfbcBeX2szNFynHuOh9zWpGRfRujcu7cjZghhP4VLrEw5fNwh1LeHQE06gS7aLER0bRGf-1yfPBFIuphzSgpdlMhUcvHwp98O102LgTEvW33R13GY3p6aFeni92HA9O-2FIXApEB6SU66P7XIoM3dQrPza1cVyHyTyyc6ckhrDGro6DKe9MxYr0eUvscudrII3uxRG98ygboBeeKESU5SNTW7ctk6721zupLSZUtfv47kDA8CPZXgMqx2bjEgCxLnKE3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=RfMQUpwRJSsrCrvDTXsbQ9qW6dlin1O2lrYvpem83lwfz7IxMdCoWMdSt1p58-cHA3cYdbTuY3H1Xcf6py9zcL0zCVNm65UnlbT_0XCXeBZYmVAozG8Ikb6Dh0p0mUiX6nwMlolbI9TTVkU7_04E2kI778hEmeRWaWbOoUHqqnHMKpPXMy1civhjdERuFcfw_No1vO3VyeFMyHKiGMaTPlaWKRlT-gIKk324dKcxsByFm9hw_RvVrjchvJ1G4gMM-owMHh1YWrX9q7auDnL88yeYqrrFfny_nQBcMTZc_Ns7Hnq_ZgYGhHau4JFIC18CgWFVpS_Kji-EIiOVF2qL9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=RfMQUpwRJSsrCrvDTXsbQ9qW6dlin1O2lrYvpem83lwfz7IxMdCoWMdSt1p58-cHA3cYdbTuY3H1Xcf6py9zcL0zCVNm65UnlbT_0XCXeBZYmVAozG8Ikb6Dh0p0mUiX6nwMlolbI9TTVkU7_04E2kI778hEmeRWaWbOoUHqqnHMKpPXMy1civhjdERuFcfw_No1vO3VyeFMyHKiGMaTPlaWKRlT-gIKk324dKcxsByFm9hw_RvVrjchvJ1G4gMM-owMHh1YWrX9q7auDnL88yeYqrrFfny_nQBcMTZc_Ns7Hnq_ZgYGhHau4JFIC18CgWFVpS_Kji-EIiOVF2qL9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqWXxstgBkFqUwaKkoIfbbJ5WCPXFiV2I3_DxTbhyUVe_hTzF-_ikOtBuYVO_iby9bdTKAu3rEH0Ehpm3H1nb5DB_ntBda_mVHTAjjqrFBB9mQarW0lAjFZrcqt0FF-Z-E7e9Qq15dPnFBMsC2qDmr9GND3DPItOQeHwbyDyVONMlMZiBWRqozEthAzvakJeSwGxCEXepV9W5uDFh-422Uxb4AjUPaWMltGrzOVDaCRaJc7wwXWwWGREVTvO-y2H7PewVO3DJYKVPO16Puur0_7SUfdVRP_nhvbpVVN5_8TvHLayTyfSIaVst6haBwfnmtRC1dzdKDpvRzEbfCxZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N4yiAiX1hQ1DiWDGE36ZCUxooc2C0BnA5Q6gStbYPbiKJEQE2PQDYTq_TS-_M_HWJpekyViK4AtCO7nSzE8YRSi3qtnjjqJm0cIPGXD76ngamIc1FDOT78t3BCVn1N--h1YVTiggehj-mBAYcinanECeXli7hxX2LUeQ6dslh-GRufptCMsFloFXhhsTnAd-bbhcgU6fwyyoxqwKkxHuKEtUFNSJrUOIiVb1RHc0_yZcidk3K0OO1XJS9dpasMqk6PtAzKZUa1SY7s5iqj72q1F1KIHfgoD66KjFrA3krY-GU-a869U4DQjaQyQvayJRgv3mXolCNiVKYOoKx91Rrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OTGH412uW3TLiu63h0DcxeTeuw9mhlDjCggCiI8VQa_MRa2ECgUDbYsVUgoBvoRaQbt8ltl4XPr01wxJOhtDThQD-48dmWKdNfiuYIywATimxyR8B0QElChPXy2iKpFVolY3tHuP_ERa-0BttfkxHN3EvdiGVH1sRYCy1ifAl1yYcvNmwHIUi3iev8JvmPKf_BhCnZ6CI8ugBj11fK7BppPKuD5x2Mo-1_ofNo59Pywc6L6DjHgtnxsmxDE66TzUbHsYrH8DtMYJdTTCqB6vx5nEN538k7xBoFRmOkudkSdq2CtDoxycQMOBDspMWHLc_nZzhFZFmfTAazaFO85Eeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EKd60J9laPrG_5pssHD5oofIQrzpECbWasygaQ1JKH4KFO4Yw8LO4tFPAszlQ5Al0xP3bFdYhpU8_A-p4EeEv9angppbG6ZE23UrY3QwVJ5KVKjADlLLRH_O0liZnp7-JmAatCtji5_5XpoTRAvrTU-Y0qc5t-elQnKMiNNON8jllbE6JthIt0sC3Gl_oN8c1BupKxlL4fpv0Q8SECk9BqW4rDZ6KlRyFgelguLar7ZbX6arjlnB86GTvnRDMU8nH981c0Y6shbeLOxV4-Xzil_2xg7TVDUPi2QEaT92mDV48iaZMJasShjCD8R3fM7mu8RhgKpLASueG52dYnHB6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SreFoFafXqzGvg1Eicxbp1ISK_oETKjIvKq25trst_LEPKBRZNZzgvACgNt-N9c3h8uVHYFOGXMe-JnQxCHvnbgu2Dqb4iyK93aLnq4tgn23O6mB0Z7uuDYPJwRX6IdRJyzqR5M9dKHrYoUUGfNZ1EILCMBTylf4LXj2EjZpfxyRjl98MdzX2zTnqFaiZrzQt06kfjiCdcWUwP1ZPMGzfCbBs1XlFoM096MF7OsEEkFlgUVDnueBKoh69qTXhh5IceB3fu5qyyLyYSHq39vhfpotcXO6Iiqc3gZ0_ro848gHIHv7uAK-DjHBDTLQFL4MaqWG_6kp1GAnty7IjUrkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YrgvNwnaU9babAR42rT_jRy0V5yj7Ju9KPnR9MLcZ33-T3OnHEuu-cd1Bw0knXfthPl0FjQKDgUb3I9V2gzYQoIbEnhPTLIs_ud2_jyOCzFbNA6JGCYKVj2I6UDCk5-IJ43cJUJshwkvJ9f_HZqDUEjBUwqqelFcbBPNccKTTfenOHksKzGvrSpk9l2TOLJWJo9HcMp1c8jq3o5NH6WRMzHeMkA5MkKukVdoMXbeHKzDvpjaMr_tNcydjRorLDVyL4o7SxsgEtK4uezNO3ZZELbM2gxIJJp8XBznjhcz4r033lt_4xU8gx5v5GGlVnj4d_h7R7qkkefn6-AI7OREhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDeq9aO3reSTYFdv76clObdk2nK4qV-UL_s5jYvDkVCS_yZLO2T4HBiLCS-8pQIlpjZM6wJYlCkccykvFTzfHJYwcYW4Ctoh9ue1KH_A5Cc63PrAPxtYiP1er4VDryPYHjztfmxzPzXJ8wlL8G7O_I4syNlFl-sSl4Y653MmUsyjF_KPYMlg4m166uEQfoLaeBEi2Nl6-BNKmVkh5hGPPlD6Z1s2E3V5c4W8PxgyESe-EclZEwD-4bCTs_3Gs3BdU8oQYADTe4SNjsXnI_ufTnWURD-KLfBABc-BOOcO-h0JD4NXNieg2vIArbpwjLO4T9zEQWkTM1cl5bjTR99Tow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S072xGbvXu9tP9UUZVYIjHyKt-u-Y8ZW9aZh2BvYlPQklLEWJMus_gT4j_2ZGxGq9E-nkvqyxBip_Usl3K2SmYmxJ4WvmCW2LDhY4nMh4aFY5HR7C2Hoj82VabE4i7PvD2w1crc3_TWTq5kwHJgzp7euxKDp5IiSONchZIa7WgVRkFPJ1LQpTr-76ZlpOQStOC3sXxYOWRHiB3K7mCB666E-28R3a2DnrpDAGZd763Dxy9O_netgS-s35cDK7MEdXZWcVCovmTJ8H8r5kRw_zh_GLlPn5b2sQwZHBI0nWEd7dv9LPkJ-1VGzfCBLAnyAC2MObrq2_WTBa0ydtxUkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LucFPiueuXgBcrMMVlFGOWrjL7tSTBeuI7rBYkx8L8wSjboqDz1g2N-71aoVdEFEh7hMauO2pjGfydndGECY5JUpFY1SyGhjKLUUXTwtkX4dBYkwGzcU5OkWWYOkM8_FeK2nsqzPxri0SvF3UrbHA471DsG4w5QATD36ZgDQOGVIX0OyDpmLImj6xycdhM-7Rjz8Rv9YK8yGpAKS7eNHzqowOKvh86x3C6Ps1kDcHFiClBeY15M7YOs4UiGAsApQByR5L-smUC8tVlkwH7Ab2TpevcNmNl2Ifp3tT_66A7_Zy-LctO6SchYmixL9xMHT61mPm0jnFVdnrmPll76ymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ixYgdzLvPQ11uQVBxv7ogulNNxb4YQtSOURSDppiHtxoyJb2W3Hco1wLdXEMYXRlRN44ymO81h-q-KutinCVbhjsVmP9iTuiDr18VNwMu7L9yRXNbM6e7cgg8JNQs2G7ozpMJih2rNfyQkbFslNXNZgcjTtGg7edmutrInJ5EI5yAmaGiPOLeHDD1tQnjxTmufFQ8IVQ-Onrc0XFZYoNR7FUO5SwKXpMX94zwaGcK0C3rIJMzx3vvlN81OCPX_bNprLKTQTrP8WkQvwY3WAupPIPMeSeS2uPc6mG-fOOZCEpLp50AsSQaKNxLRPyrNyCOTiP7bVf90isikJi0RB31Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jiX-GaTl_n2hpVqiohbJU1ZqRHhwcePi56BUlTet_L2ZTT4kFIwmId6VzFmKTBLZjsGjjQA4dJMKTpuH74ksxNgba7LEYIKyCtHL9SF5ZIWwumq_s0yX4e6Nbuq00rRuh3ASVhcSA3EOpCuhFmcWp7CTlcQ3ZEGPkOlOw9ws5DEFuOJKSZcgvOERBJXHcZoAVwv0T5rNtc-KLtPbtr9OWwsotuumKWqcpSF-Ij-Nd1mPP-Fditpm7F_SM4EZxcZ2CpGGsbGV0wYrU_U_K8f7QUpBxpuBDqukMe0XSabR2t4ca4uRw0S3K-IOL3lVT5Z3x97gVUaREp0zltXT32FGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLSxziwAthHZDi8aTFYxSwcb_aZDIqGgsm1kPK3QxiT5fgEJVd50Ddtedo3p4de-5qzuwKeTf4YwJ_fyf5QsWEbJDxo4olFWHWIKJxT35xMSa450gNh8eEDDhnET8w68Pr8zZWdOmIsxvzpHhPR4ZSADZ_Dffbh_pxUb5xFamiC3R6rOUelpoX3-4ggopKMaIpKSphG1_m9b3K5UFLxctv8dOFgtFSAxaySwqpMmuSyohqpHfmlQx1aXMiIsZCGcuXbOTVfVPavkORUSGcRw1WJ21lvX8KDLT1LEGnjRtisBgX33ep3rCm5xaF65oTH9bfU8SzXn1POHk5YvzwXQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m6_fnAxqxFMs1I7gFcuKBFpo9O0Si-8dGbSnAf25EQ5aZ9wUy5NneTmlUgUOwU3cBmRwu9lRHnc3oVogP_S4UhasCDVtCQZzQZ6fF5PwKR7JGLkF0Snl7d7n-lEf07rDtSzS1J7M2SPOmPCU-V028Fte7Rd6J72c2sNCVuYr7Xv5K1r_Hq2o5FQtE5g2qzpTsilaUegaQATbymJQh-LprEUuRPW9U_F4_4k--Mad_6hCaI-EAaL8VAD6ic0janFdCD3o8OLIMVvQS_Z8zAKOSczfN6ggvdLNsY4QviJQ74y-SP2x2SlLbNRObt4i3mUsvh8Rmq-v97HN0czo4Ad6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXA6wMOnRZYbSxHekMw5Exo386uQiC7OMQOYGTuru0ENIlgBeDsDdOawvTiVwQVIU94lsKITg8ZQF3_ZAwXQTV7YRQM19qj4_5uAXzqFapEfY_XZwE4IwMUXL_eYUJYgCUKqQPG2ypWnZUmcYgn0B24nGRZmz24amTumBFMDwYO-ApTgIQxPnN_nJzXaeVs9xQ0c87c1fJ9dd3bAhpKSYXtNpxW99ac77OOmQEO0j9XK1mM4ynBycsNzAMg2TQ3fhqQH4TQcUXw4iCy6bN59Lf9APv-A7qxSP_hI1bBN7i4J8p7SOWF9e40EBfwekVAmdN4MX2PLNVesisPHP5omnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BkduDqMBwgKiWdPwXz2uGtKetygydXKiWm9_DpqMViBwnG4Bex4OnQJElJh7XqWY_AO34qxG_qj8Apsg2LA_OtEtUSpT3aTM1h0L0I7VPxs0_7yICeDfJMZ8gjnlTXQXP3e1poh37kO9fiVokpNHgdMhAUvHwFCOCwgHizcA_hBBH1gXyJzkMGEmO1RVS-UWsGkA6YsTO8nyDcmagpVownrwwwnHDzTQZ6-ATwS6Q7nDT79HcJqeunIK3SXOhV1v_4Rmr9WS29J6twANkb2seYd9sdBUO5YuxArrOcYhzRFirjvOTCkRQ9lCJhdLeGmWe6uMhw9zVi5TEIFv_PbtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sFzLw-4G_UB8Gj7rZ-1An7Rdodw88Q75873WhExLKDyg9yCFtaZ-pj__yWx-bfQ6_oRVw6CwAbg3EjjI63-HYe4Zksg6xvI3yEkBQFOaORk9AukjqsTsb-OW4jcV20mXz4x25rsWEvcodV5QprXdSlGIf5r5e5Jfic42lyl8AtUTZht6ntwGWLYb0DmXOpfjAj-ZCJV81a6mhBngPmWemYlOCPZGG1TFFKKQcYPXN0axCQloEBjtYG1FtTEPaeVG29eVV0VKzsSFMn7V3n8827w_QlsDk4rxWpWhZT8EBRYSZptR0WgHdMm_eLnIbjs9DDia6Hv0caRIg-vJCypkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ldhu79amjuSI-9ryuP4bYJBSt1ia4l3cDJtNlyxI7Hamcke7WuMFhz3wN7o1xr4rm3wOCNr-vGPXF4T1As5nFXuoTEyP7R2jBqaynoWZphJMnTYUSnCb5QEaBFodY1_2lPUVfcyAu9NOypzW4xa8zUbZ5Rvu9CFqAPjCMsQmVxTqJe64qfYr9pT1v61QiXB3wJUnaK0_rR0rx_86V2_skwjigoGWQbqvry60kZOP41zrSWotvelfKlmV-AxyTJqgBrM3pWnhOUsFfJLgQOrYILqoPpMa7SfMitr-DLkm4dhBL0Dd5uY86sJw5bb63pNhk4dw-4xIFc6BZo3XQ9-UMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bG9M-N68sRDnuw3bjejspruBcQrTgDWyODLRbAVzMNmHT68u90_s6tvo4ZHNe5wrQHSYKuhfPAK63-Is1hFQOKUFNvsFfAHJ7tBKf2I3l9fNNPSwzSiKzgSKGOx8azOhOVXb4F1AbGTUAR70n-2U0w9vXaV1eriB7f9cCoDrdUygdH2TVcKt0rqqNvtw3Kkkg6T1aQDFSA42Dx3fPHrR_SI65SnXtpJt5N351bpdrfN8D-j_gaB-5Av5NJrlBgaC8plkUdSpf7wNY_2vLsWOfAjElZMxbzI5iBzjt0ramXoRroJ8us16c858sdAqrarzbiiU2mP0EhxCanQ5S8B03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fTFeu0MtanruGIPFAXCPXvDgW8GSOh49kPTD1NodK31QNS_jCJ6AEYq5OWj78DAgyUAiE6Y8Yu02ECVoHrojv3vb0zwG9MwOe5XUg7RHQodcbpL13hMnDj3-Jbik5FZFwtW8xOTM0tkrjhvQ1elk2hjxckm7agXS0kflIHTAyFo1E5HstJIfwWcwmWuBACHReUbvvolqant9foPj8FxtvSK9sih_zRjSFNbvzHSjWh4bAqgI58E9g2-eH8W0X2JK9h9vzLm6SDJbUO2homquAXZdGN521T1OMFCty8O5FTJDQd2rzudDsVZ7qFcakOHhKxzy_5NrjMnCQv5fHya4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgG9t6hVss5zbEzK2AKH9AoMLu0GIQ4CO6v94vxiDXFI9tTnKX_T6e_y84Ikeoed6YFEWtV6cZRtgWb0TfbIKGsR9kzUq0ITyoj2LNWjaRCp1-SnROqcnmhSJf0KSKG5T4b4UtrjIbxYLO_qysJH3EB290SRZ3_BLIUNlThNGebFcAuDvxXzbrbUnwJ6EbZU26jZN7v8U2_BilzFSEBik5RBkopYg5dVWvU60aHdync3qERLe3wsPr4PeEdz-_VFdXBIsy5mOZNnInBsNZxIq56GjfjMEee4_0gqoDOnskxF0szoS4prryqmJ_ccYHszVOUVwvPTpqpM1Vj-Os3e3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I4QtaFQBtDSjPfDlGEu6N_FZoj13ZzPf8K908CpxJFCxhLxPj0P7KaBElCNR66btRxBFLMoWgjlcZGWMS-8MQL6C6c3GJs0dI8hW6hN0NqmjJjueEItpgXNw27uWvOuF1qLdB02sVHoldBhyYZpcplFwsouURDq09OcNebeiPp7K0JNimabYOv2-KRXSqVcnr-fbFHtiWvWzicAFqgeNNB1tn9LqlDQhUVWHL6ghyht5CoByZIukm5GhFB-4PbW7dsmRguGYji7rLe0uvTueAhi_Om3-2jXVfMEsCCLuf6zWEw8oKWE8BoAdnraHnr5cPVohWbVQHtj8E3owOQjZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YAKb5XxVheD26e1MbN_rGadJlEJ-hI9wfmEKFOjBNXSqELxIrVIqrlc3TIIdBZ7ywWp6_r2zP0ESFVoqoZ6M4-lhGZFHLgXjuoh-2T96ZLimwhDWYHI_J_Y_4WxnozmJXGgcqvk6-BQ7sfPnBkVyelrNUqrBLv1VZVQKru1n7xOfaK8qwbe-dHjn2ZzO-_9PA4sXMNWMbz8sphqwYbVB6yX0VkaNkebgOgX-DfK2-cJEGvvXiMLwi6bT_4b0A2kSwCbUjXnsb3eiXnzR2C38xLeLQ-d4RO7MwJZa9_VQ5zkKXM50MmNCDrMGMyXG5bHUfX5c8GaLlsK6MeC1903ZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EZF3Wu7w7rbv7HPDFRWHDyZO7Y7OzEVgl6L3fCxkPY57agHLeWBcEUbLIFcqECEx4LaYzXxArwFTKCqQMAOiBTvGYs_yKg6wdkODNr8ZucESK6Yvta4N2F4g0w9VyzKZYBFmLNpxhhL2fJDFh36t8b9ZadwLlN1BRwI6q7_76GHIPW0tgc_U4C41NvX_Q5GbpNIoE-1WrX6XSPXI-Io6KBSU7FePcPmrcYFsdYkYex1ZQB6RLALHaa6elq85I9F2C7QEKiO3tjhM1kMGa_Dp3Iy7feM7Qctmc6-DhfVJlujTwksCeAtGwCksRFDk6_ITK3BQlpOzl8yLYGpCFM-Eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kPT29b19LqqVz7GMZ7-uwJJ0En1_DCfgXBKtEb1CQOSIyCFxe207sn6KZU5Gyc50JBdGZA69jxViGXjSGa32h__8HvoDpQuupRb-3MBJkL0ldrtQAx63h4DsFpVniLUxDIWHPJ2WC-8ZXBkppmJtyl1mRWc-1AI90M4CvnyJs9eVfhUo6JqdjZLu4s5hKi3vEP9GLBGyMAc9mhBO7Vj1lz4t1gvZU62kv0oYR_XnKkpjiBrV3jiIGe1UQFjY1_yloHu_QQhxcFzblgcEdYD6rOi-V8TWR8Hv91VRV539M4Dc210QZSwDCMylKK8WpN2_GJS-fWTZv-ooPHrlq01WgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G5Kz2iRzSzv7B-z4btmq6i8ZSUvsxvBWGkVFdLiCzX7yqvlm5XAGQ3v1l3Mt7KwFbBmCO6sAsGjhVkVm74UBujZFGLUB86vXkB7QC6cMpN1HSGJlq63l2X82q3vMdrh5Dbb7rev_MQAhxU9Qlu1Zg-b437IafL4GfkW_P9TlXXXq4ge7swyx7xI2za_ser35G7Q6NbO2guUj4xodjT1H9zFbNJ-NMG9LYWz_nrJVE--CChqkrq_LI8_dslzzuhJrL7UyoNkXNfCalOl16SKgS0vNdBW4a2RurJLfcnKqSHmY90HAz0iwBg28hi3OSQbcoGDc2cvKEdxxm97MSxvvfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=SeAOIlFfJRKRd3v4SVdz15ge4FU6mzqd-pV2Yl7pO675WsPtPDFzL56zDTJeuYv3_aJKJza3p_PWfFRuguQy1DLJZFhHbV1ad7IBuYIvVVDUL1HUjrXX1ZDU0caEMbQYSHuJga5CQ55t-lZftGR4M0qk_Ru3w_yr47tHLhv82Vqrt_G6nTQPBF4rjJFhCmxx8nqGHPQHkG2zsj00ltvPxJ6n4lucu48VpymNhyMjqQAyElPSDiPCpPIW4ZKgPwhESePkl5zTGRvgSMNlvhVdBl7X7wbmVHJQsWRPNu1XUkP0IFCtVzf4UyZ0zQm7J0LioSK_55G_UMEPo9z6P50DJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=SeAOIlFfJRKRd3v4SVdz15ge4FU6mzqd-pV2Yl7pO675WsPtPDFzL56zDTJeuYv3_aJKJza3p_PWfFRuguQy1DLJZFhHbV1ad7IBuYIvVVDUL1HUjrXX1ZDU0caEMbQYSHuJga5CQ55t-lZftGR4M0qk_Ru3w_yr47tHLhv82Vqrt_G6nTQPBF4rjJFhCmxx8nqGHPQHkG2zsj00ltvPxJ6n4lucu48VpymNhyMjqQAyElPSDiPCpPIW4ZKgPwhESePkl5zTGRvgSMNlvhVdBl7X7wbmVHJQsWRPNu1XUkP0IFCtVzf4UyZ0zQm7J0LioSK_55G_UMEPo9z6P50DJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eNjs4IVwdx1jQrA1sU1IAbF77y7_sgq2zJr5RsUkzXQjr4mS66LIiMBAx6E3a7_K0Xj8_aNWnznngtxvxepxeHAkK4TGSKjMqUdVftF3-TMFoEFgM7ydawupQL9mc4TEA1Pm7oRPRQJAh6w53Cse0k9FBtMhYcckG1UnSILPcsDTCafJkivV5lxhODsXgrM2IgPTv6Rq7uMNIdt2s2pYbgVeWzJDwyx8Cqxh6PGuPyZDgzB14TregjxJkIafDRtYuTGrTp42hE-4F7d9cGO-65OER7_TUQOXzIORoey2TxQjIhKP1fKNbIwFCwvJZDhCOYpHGspkPE1ra1GJkjItsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TF0m47BLnao0Q7_hl5tOfDDXQW3AGfZwO2rJYlXY-ylfCrlVE8BM4NNqO0mjZh7fhmQR8B-JbTEklIIvnuzvkbOOdwl9nHx0IE33W9KJYTwxC70N_BInGGCy46beLfuBtVIsmjiPgHZjLyE-sefETPBUH8K8y6kXQCTYduNFyvU48jidJ6i_Qjs3mxL7tvoJVjFQ-pA5SvxQfjuVicyRxnfUHabG-oyyEoavEOhuubnq2LbtQ9mVaA844HJuIazw942dWcbZl3j9lGQ36GZxgtH_tzbvQ0oAiM7Qpac2VzdS3OWitFTb2pvZUphh_o-lV1TNEDpM4ZKXC3ktKzJx2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJLzjlFBQcxPT41qK3adObKWdGZm1JnbQT22ePiZVgVcUyXz8xE2KBdK0dZ8B-ZdmjGx8szyS8AWb--m6xGYtpivMCMVyJHoKIH6p0Z7WxD4ahKSFT0JNoRcefqdrOVtu5-Fy4HMfDKNzMCRw-WRqgBy7XT_ZjLXYjeuPjdlBPGCLjmqmwTlerwpAw147e5JXgBxdFhDBUcQS_H-AbCzLMZD5U9xgVO04oJsmZ56gKoYrIa_oxPwYsvEyhnn4Sb06C6__gCjNg8pNZKArxDwAT8UtXZmZxGgPX3pxRPaBPY_H18eNX2YjlXqBP4Y7fyfeWoNfX3FNhQeJGwUGIEFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EcHV43b7eZdqgrDMom6LpcuNyQo-fXHmckwIfN4-51nuJDwslVLE2IuBqJoKWJMhzG1JeLsI1f9GeljB_IxIk6Nv8aLOxYlIK3Gc_qQI-QVSy7YZ18zwv-niDKP0LCoPPruCKC4TFsN-kyHQOkBuMhDwB_V1ftl_lp2BqtQxrX9IqnsPZ2eNiBXVA-HKQ9mwpZHB14aaBeNDi1bzsiy05fRINIwaGmmVWYlRWkrbPZjOnOJ2iR5gQzNgcIX7m1EQTbo90sR5TUNWsPrAI0l-8s-nbldDb63HJlg4fS1rd_m4CgcQLoyDuud8jiMEJjGi8UPdrXCe4UmLVhEWl_DF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o4uT14RSynSk7GgEyDaiqrbKdM_-liBFmCoEcTXeqtI4A8STfcytUpHLvs-gafuk2q93wMd3S1J8LCb0hKWCzGBtJx8MYyf-EeV3UgrJHwTQAftf9ArHrA7N9FwOzPOd1-AFz_pFw2gjyHqcB54uKhLCvB6acg-TT2cVjWaz2hfYPBT-3P8GJvVZy8Aa9jiAXQ8oh5o1BU_2_Z1Et3VH1yH9cZHUvct3HsQ0IZZwCtKh_5J8aMMaGZ5eO2AmUL7Ukf84AjPnHNLQvJbXoUY03VWdy1Lw1SrB0r84NzbgLqJDYbJuKpxoawvbJVtO-KGgd_UPe0aAGfh1XVv3oMlWnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gcIZkeAS8ajNBvjwvXl1VeXQx4pSwv59Khq52KZLqnd4RpuWCcRUMD5ErtAUksKh6t1DpTlOgBKqiNJ_Oj0A2NIF_odvLHyNNb9tlGnmcxRsgntgecsMNPf8KDD9UACXHZMn1vS1iBkQfo_PKEARxX_Sdp3Qtu6GgVB9UsH__qJ-G7KWri_V7C-4BoSJmKLPHaOtHLcogNB8Yg1pr1pGG_cfP-n8M2P_xi-MDlvrT8HKi58iwTDuiVlyb6ml1_DdcCHwKOJHKbPvKBkIHH390RGtXRY9vGsGa7zdgMS9R1b1BewChC6rX5E5dZKYxRFKJFjaYYqRjwrtaWlbuMwJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hAsCGCeU6-VnyJB5Prxd1YMK6e-28szkbodrWwTLoh757GJqRA5gGRxgaS500hUB9fmrF3RvpVRzew-IdMZ-ZTFNh2JmlidpjQBPtjkm1ynqA2KtmKFatObqkXCiqyRZgJxeaHz42WprhAMIbex2hB4uc8WLzXo2iplFyxCL_sAuEDSOaoMYky7wXEgORGRpGsRR0MJr8JyjPrhabmBRI95Ht22up9Ps5bXwIdkwXh0n53cLeyq9DMlriWArJe2f928X1X7gFIjjCXISBbuvreO7rKtIAK-nZqIcT86g9ncsv_4xjXnBJUUtKRg9e5FjWOLqM5Lmup9lyyKsMEl30w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=pBII3c1vsnq18vlMKeJrItpxR731LZJS5AyRj4eEOUrHBvlNkw_2T-VqBY5S4tGcIExEHiKFxwkg7ZRvKy3tk-F6DKe6QKbBcPlBhVLjnRvYz0AgO-uAIGmDDHJDaDbtdvKdm0tqp4Bivya1N_Cj6OFbbnCsBH-S8KZqPcMoale-fu2MPOknz4df2YQLImATLr9AYXYN8-o206i5-EYBdd8USV2Ry20wd4fWuUcXPp0p3AHFJiqIrmqhRIIeqjjZI2MOgm7MpCCQGRv8YhluNein9451JabSmJUsT-2vN1VZ2PLqMNDwGS89BWuAkIGdHyVW4gE4BmR1REumcOLnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=pBII3c1vsnq18vlMKeJrItpxR731LZJS5AyRj4eEOUrHBvlNkw_2T-VqBY5S4tGcIExEHiKFxwkg7ZRvKy3tk-F6DKe6QKbBcPlBhVLjnRvYz0AgO-uAIGmDDHJDaDbtdvKdm0tqp4Bivya1N_Cj6OFbbnCsBH-S8KZqPcMoale-fu2MPOknz4df2YQLImATLr9AYXYN8-o206i5-EYBdd8USV2Ry20wd4fWuUcXPp0p3AHFJiqIrmqhRIIeqjjZI2MOgm7MpCCQGRv8YhluNein9451JabSmJUsT-2vN1VZ2PLqMNDwGS89BWuAkIGdHyVW4gE4BmR1REumcOLnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f7zSiLbSpM-rHYCqzJ5UykgnRGT-yzPYRfaYYpbjKy3-qC62t__bnvxF286xXYlncDbzYj9JR0CL3nEnyNNhcTuqLns6DSwUaobC5oSHo-kVBTRKnE7fd6pQBF5CwGHZrsCJ_PJ2nwhaFXDAWGL8-fHZjQWefkrKndQJtPL-pqhjsT5a2Wz5Ps3ML5l6ipX9D9RjiJm3sXVy2ybrmTliGs_waRM-X6sJsBD8ELyo3iedo3g_K3UUPmd0b6ZDiR6nRa7-NzMMiYTRk8rjG_HqD61wOtJIR54b4E0Z6u-Z0fuE1PFqDqvcQUwH0rxJbD2t185UF-zznLndBWFbmHPKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h4sce3xW_trP8K7RE3KiNxwFFCyo8gx-_LNp5QJ281UostruDfkIUNcpX6gg7c11uHIpfI0f-ixmU_8VM8ye6yYLFH2Pc7I5YsJDmlX4D84QkA8dwZgqDYACnEpqlr4Fzmr483rn9_Pk7EPdindTsclOtN4-lOg5ASB21gFKG6aF6D1dEdMI0h4q1lnCU1P43tDwzoOr4lDAGQrxAeRW36kyusLj4jX3ySdBhK0uJEcmpuhkvhl0VQhAKXggxMy4LMwAgw23MOidFpAimC0QAa2pfn5aaYh_BhUmizWh8rrOUTlVaQLvE8rA1qA0psTcWwHtYxU6eSyZ17wGh-uzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YtMSn3E6qAv6SLfgv24Zk0Tdy7cbkrRb0Dv5zrcegfHZ9m95CXCacMWen3FxeF1Qy98BQE4qf6PG4VVuNVKdiHtwCgaJz1E9e9a727iXlduMkRw1F4zjWvYh3ovOGlgXgFYs1xPS26JiVU46ld5lxT66sDqAQM4gpZ4AL7NoMfdyMKqiPtSoFNOmgCluDrqo_qnQkgtOKhdZgUQqjoVsGAhcOI8_vXlqAa3IFTo6cj_DlBuxAJ2jAco2MzFzpNkU7xlxcIDI_yFlmjDYiBswOi7WcYHQ0GrNAoiSHH1dOzlak_h0PRXhmqsvoqx-xbEKkL4yc7qGlLPRzgf0UD8qfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V2OVFzktNdmxqge2h95eB0VpV-QUaGao5SHPrHy0WG2PPC_FLOT1_Pxju-p2XwrVTulZJH3UNewMgZ9Ni4d43TGsBEx_JDOxsBdQ2ptSbM8tStRQFY8XbP58Db0ls9P6OYKjZUXaEcfRddHe8aPz3zu2tpKq3ikbdzTO-kY8DcgY3_-bjSzrBn8npeSr-A5P1WdXXPdE1bipv2rmHMhRnpZSdvIKKgCSOUxgaezSi7Pu5qMqk_IV2bYLlSbC9Tlr1FpJqj0aspbh-TxabFvImsYocf5yY3DLBV8dEQRMyNi_8lIwGiRYJ8DcCBvJoUtNrV4WZn0UzDDpa8a1xUT6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=Eg5JnRbmRyVc6iyMflCo9CNduu_J4-rtkqc6UrqdFtDc4F2xSBVYImSgjO_1RGUwYRDU6t4V6zXL33ZvMmwM_GOvcvFrT424KsX4R-N3RlOuO-h9OlIKFy4j0CcEXtbGy0h3-RjzN371BjONmvNSr_r7qzeWU1I5UumQef3odxpzycDIBt5-dU1F4X62KNXIjg70llzippArX4sgXroKL0R5Exm5B2FB0C61eIldFBTh9b171j-9-cz1Lbm6b6hrlh1iF4kQiijMZ-bcuDFLv5SdJKLr-sbOHEDrmjMbrLV-8aYo15Fay3gfbtxJ0bPNJNN2yOdiQt3YZX-4OZiyIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=Eg5JnRbmRyVc6iyMflCo9CNduu_J4-rtkqc6UrqdFtDc4F2xSBVYImSgjO_1RGUwYRDU6t4V6zXL33ZvMmwM_GOvcvFrT424KsX4R-N3RlOuO-h9OlIKFy4j0CcEXtbGy0h3-RjzN371BjONmvNSr_r7qzeWU1I5UumQef3odxpzycDIBt5-dU1F4X62KNXIjg70llzippArX4sgXroKL0R5Exm5B2FB0C61eIldFBTh9b171j-9-cz1Lbm6b6hrlh1iF4kQiijMZ-bcuDFLv5SdJKLr-sbOHEDrmjMbrLV-8aYo15Fay3gfbtxJ0bPNJNN2yOdiQt3YZX-4OZiyIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=Ovj3LktcGJ9yhobnHd4vVuRsdH8OWM5udPI8m6PnxnaRyXEzcvsAp2z3zZKQzgyawc4a-fI_PlNvgiG5SzwbHNUhqChClIczszv4xRO_tG0GclJ1g1UNibkOhmqObqVbSXCEm48oXnklXT5ctIhIlZSzuZp2vXWDgmvpw0qixQZOcHV8X5j75yFKUcOKTyz-rrTsS7l7jxFf6z5SU2R8BqufnsHFJjKJRFqut1CBU1iFHjWdv6is2JCaBdt7Sd7QkQpdJcg7AtMmGxYlaujvbzesJ_igi_fEw3If6gTZ-N-ubR9o0HRobSAt_os6Trmi6vOVAMduzcazmxejDFqsMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=Ovj3LktcGJ9yhobnHd4vVuRsdH8OWM5udPI8m6PnxnaRyXEzcvsAp2z3zZKQzgyawc4a-fI_PlNvgiG5SzwbHNUhqChClIczszv4xRO_tG0GclJ1g1UNibkOhmqObqVbSXCEm48oXnklXT5ctIhIlZSzuZp2vXWDgmvpw0qixQZOcHV8X5j75yFKUcOKTyz-rrTsS7l7jxFf6z5SU2R8BqufnsHFJjKJRFqut1CBU1iFHjWdv6is2JCaBdt7Sd7QkQpdJcg7AtMmGxYlaujvbzesJ_igi_fEw3If6gTZ-N-ubR9o0HRobSAt_os6Trmi6vOVAMduzcazmxejDFqsMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OmcpG2nrsdWA6EmmS1OkacIcJhWUXh0KNh0feJtV5QfB638sT4Nw65Ek1Ey5Zkdr3RRDuUlq8lkpWU6FzIx91dv86yT9SVnCRHCiMDl5hDHFUZ3lAwoYT7-g2UErCg0Rk5lgN9_8Jygv6zKQ6LwNsy1N3aldKwRa1404yZVHBDYG2il4MZXP0gCqVpybLIeQPni3UJGdj5_Dd6RYPsj60-s6jFvM80TFZILCI9Y1fYdwZZSiupsrAdGJqxDIuE-c1oVqaZ3YcSgQnH6HPSyyVXcPqr4Sa0tX6YyV6a7Dv1704rj3jDDZf44PLctwV9MTlwn7PoxCsxyxoBIHsTrc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hZgQCxTjf5FjQnrv7mFIiTc_S0cakcQ0oWd-oHWWV3EPdYbiwOrmHqvhcqbDjUvGwx-G3R1SKF6X9yUjjhgpY8qsiUuhHmg7ybWOKfxOFzm8pAgXzsvaDwGYLA7iyKbB9aN8jkgszlvVyFZuiM-PSsaslNNOcG54q1aNuoqbJRvHzETeGjEB0HyuVW0yTrN394DAAvPna-E0cJ91OqPUIQDGh5lCu-ljm-pGK3Nlzie13Omiauogx9MQ0Uttp4kOQYn_p8mfterrAhfmePtU3ZUesk1ba5NbmrXPGvW19vRy7fY7ItrcxHy5O4gMz5kLqwjoa7sPZ5Kq86u8uqRsuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uMX75TRK3EnkStNJCBX_m7TZ-c_b65r7OME8IbC_8ba8ounv4ALTfunUIgh2D5MXqA7r2hFcsp18AqNK07iluVIa2YCeOentiJe5UkLXHql2_UxUROrAyrC5DJVgc0NXvM9cB9alMSy7WBTY8fBEGWhBh3bqREkCY_mh_OHPhCm-BS7AZOAmYBlN6Snqkls04DMyh69KYz7Is-kNOJVW3Ww6xaCDm0hGKyU-yP7TKFmv0wyEy_acWMyGslrocypmml4e4V8bQWNxL8p4WzQ1P_qWL204L_-KmrJJImqQ1t20BXwC2SXFxDFzcvYpfUYtzaize0-LTEEEt3B9KsnilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
