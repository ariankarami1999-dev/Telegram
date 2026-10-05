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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/MatinSenPaii/5521" target="_blank">📅 22:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n5FywmdaQk2qSwoQ-_ARTAdYx3CR8Kt_NgZ0N5WZDpJnGDPVysmtZ7oftEP_tHiQb8RaDJquVpIfEwEZDF8YKLn584QowHP0DlhMLg_rkp-F8n3HBTvpMeZCsKM2Jyj57GbXIFUpYs8gy9r8rmJ3I8NFJCKSplkkZZBOFZtG2qjMXNfaXankn8zOKEd419ILnQXSPnNzwXU0fV3h7kHmY1LoFXYGqm-NEBVDhzrXf1PTHAdk3rDDtapOuOhQymnni5Mr0IH5RT9rSvxLTMbPck-6ddZrx4bQzgCujKib6k5ZZ_QjdUoOzrXaAiS2mitZbS--LL2lB5PE5ABwrQvX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاپ مموری Muse رو کپی کردم برای Hermes خودم
یه کاربر توضیح داده چطور ستاپ مموری Muse رو برای Hermes خودش پیاده کرده؛ بحث اصلیش هم انتخاب پرووایدر، مدیریت پنجره کانتکست و مشکل فراموش کردن زمینه‌ی موضوعی بحثه. اگه ایجنتتون وسط کار یادش میره چی به چیه، ایده‌های توی تصویر ممکنه به دردتون بخوره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/MatinSenPaii/5520" target="_blank">📅 21:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/5519" target="_blank">📅 17:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/5518" target="_blank">📅 17:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IG13hE2vZd3Gm1u8lgFqvGMNvtVQlhlfoNO7wknYbIh7HFTU4JOYxJY2hdXGtsTSSM17sCeWNDzYn6KiEJCa-zffL_Beuz3sQoQdIvuDMmbizZIxMe5i5x4ZxWL5g97f9QkWAcO87l07fOuvXXYE-pgiFzjMpmk98GIyNCHJZ5EmNNHs1M7DS1gZcp4ftzBSigoqGalZ5Y3qkZeP9kpOspO5icquGK36UYisPVmi9wRP_HnVuUkwxnc1vTi18DxBuaI2Ehx0hm1-a-kRgw8pj7tPDoTSwvewFCE8lz8ECPudgBAwPmkm42SDUUUSQEJiDEjqcE265czoGGheisYBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استریم ما داریم میاییم</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/MatinSenPaii/5517" target="_blank">📅 16:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QjwaQfD4oA_Vo7worOjv1jCDm8a1mQrxDLj3BTZbMHGpAGcSXU7gqD1aFqJ1rpCDlXDCHAyH_RJdVgssxPON9tpSAgJ9fT3uoh_ALXJc3mLSVtYVWPOPx0ZVeQCjjbGUGk0s6Ky9lCPZPWIJpf16PqU2QtC0dIGKoD78GUZL-z6q1En_0wvSnKL7i8-p03J8lnc4NQFcE0Nxgi4CVlgMcWG3DdRaOs8bXr0OaMPnbMaBWn9ejuaYPuHYVu87Q2DbAuqcT9W25SReKE2s3lo3gcKnPNCrROdFuTfdfvj5rpH0ff1ZOsTc7Sr2p8OrA1s8D1oRQ8QhfTEIM1oYp3E-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا رو شکر اوکی شد
مشکل اینجا بود که سرور ایران، دیتای اتصال‌هایی که از خارج شروع نمی‌شن رو نمی‌پذیرفت. و با همون قضیه ssh هم میشد فهمید
و حتی تانل هم "اتصال" رو نشون میداد که به خاطر هندشیک کوچولویی بود که رد میشد
و الان اتصال از خود ایران به خارج شروع میشه و همه چیز اوکیه فعلا
این روش فقط mux و reconnect نداره اما چون فورواردش توی کرنله، چیزی برای قطع شدن نداره عملا.
همون آیپی تیبل خودمونه</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/5516" target="_blank">📅 16:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/plPVGcSsf4FF-kQkw9eu0EYwNQH8LKix8TwIG9wK7n2scS7EhqSn3nKsWZsnTlxQVpsu0OoZ_t-YZjzk-mOEkRS4Y92jLWqEZF9M1JGQERJqbd878137m5TzcKP4gNIObFfPav2lipI_aS6_PhISzKPpaVtbul9Q6mgVz6mClkk5HBZcFAgq1zNwheNJmYM_sRyGOJ0tIYwFrJIcEHRP9uEvC4JFZxTmNaou8bmPUfNPxzE4H56ta45tbqQzbY6HtQsdgpEYr2VrMeYeVNmmiAesGROH29gd3_5pfAK6tDKdWJj1zU_eJB-64TWXp3DDW6K_BV90ExOk-fbRf1OkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا Claude رو گذاشتم تانل بک‌هال بزنه بین ایران و هتزنرم ببینم چی میشه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/MatinSenPaii/5515" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم. متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5514" target="_blank">📅 14:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سعی میکنم استریم انتخاب رشته رو امروز یا فردا بریم.
متاسفانه تا الان هم که نرفتیم به خاطر وضعیت نت بوده</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5513" target="_blank">📅 14:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">از اخبار بی اطلاع بودم.. نمیدونستم صبح چه اتفاقی افتاده...
🖤
🥀</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5512" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ای کاش OpenAI این تیم مارکتینگ و مدیریت محصولش رو از کف توییتر جمع میکرد
https://x.com/MatinSenPai/status/2107032765916999892</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5511" target="_blank">📅 12:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCcnti6SZbdYz_XszyDvOS9Qoa7FdxXJzOH-T5blWvlNq5kN_DSggn4Chx0p5aLgL4YEN9YugAQcZaSZSzLdrMtKSbz1sxAQF2873QjGmBRHTYGkjbDdzHvKMmRG4_XVqGCi-UFZaVk61yqjuMiT8BtAbJpwhdvOhdlAdTQrvTFDvN2ryXySEN5V0Wtng8kTKok1O6gKieQc2mUDUzmMlO7tnKauUaeJlW8VWyTEC3124pxLU4fWulQArOfm1L2EEFMbP1eAT_B5GfCOPzbYJQM8wUMrh1KFq4_ZHDyEj2TvPHjx-WXhjfVQo4Xzqn9Gz3QuQyFWvC2TJdnUxQX1xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5510" target="_blank">📅 08:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l5H9Ze3jDeIptlsSDklYtQBgWVvAyIN2-_bwske7qr_FwNCgsYBTIsvijgB4wZe2Z_9BP1CiVC8hNhq-tWhym2z0XLeBTvx1hDBs8Bw3SGl9u30aG2eEK2dvUUwe8R0RsAkzaMnY7kR1Cr0Ocst43s9VHYdexLGInkRhb7TnOMihrC2wfamKMwKK6KRi6zR4IE7r29ySVUFwWzWe-qXodAJQREBr42EnNwB4omTCAUYlKqwoYEM_Vb93lOf_uSCskucK05Dr3WkY3fLSEhvPOc8MPLg4WcCbT4Umq1OJjyNOb0U9Tp4VaTlIXCUVSYNHRCZq5NM-a4JaKmSKYH-FAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jt8gSDCUiH5S_99ziAHjdXbOj6Zd1bHBdxSSK21D2dXKcJziCj-vad-KAC3-cv7x1z9PmeXY_C8CjUfezuallDE_iHRILHiDFih1jND4w_suMOuOT_o3SBLySIZmdz4y5a4ZZKiVm2c-kZaHJGf421mRHLgJsUmWtpMUMgZ5I_hD8M3ZoxJM7XcsOOYn9fAng4zrvTVHuQp5HqTd8ERGa54D5I8ZR0PuwP3VkjzQo2vBFbLHYMaCVthsKQKSt6NGYjuuj8v5gKSRzxE3BDPtXydSwVSnL92Kjw1ZQFr41EH2m0x9syrmfw-fVolpX3iBzwg5Q6RavK7WA50uhAQMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t5675K_8bt59oMusVNyEMQBUbq3ro2hxaDpYnIQxBx3Zn1uR9UtiTneLmistkU3mtDwpj9Ea8zLnezrZoEFovcWbZagUtJob_2n6-fXg4Tf7F_rKEJJ09aFHzSCVYBLfLPVC03ST9qNPavbNQsv6vGhxc8_3pQC4PjYnmcT3Ma5MV0qrJ7TfYU_hV00U9L7gDA_RxRZrQSc2ScBx2TQfnl8ysxhiYKFQUQQrZWuLUOJ0WO1bRxc-NB0wmHDVOFIH0jHELH2oSQN6ZvZPGjZ2kVHk4NfV3pwRi-eym0QR7Fsn4jvwcQ5G3tEcQpGEzTBxTPM-whYsfCou99_N5si1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLNTP3CLimk4P4AcYkafJI_TqOP0BgvaKVYhZqTmXeK9bZZMRldyfY0WVx4Vhb9hSs5Zy0lOW5tiyqRFMLFdxmqDg6DQZ1q-mtkzeho8PrT9TgyQeweeKkRgLKtaPhC5ZfsvX_eqyv_TXFGBMSMhYjEPnuysUQB6sW_71_1ya81G3YXPKIozYVgik-z3f1Ov5Ylm2dDg9qoHJU3hMxHm83xGy1Wd3BrFoczIFi6mnxWUMMvBmgBs7OEdhwQyR-qd_ofNgGOR8InnMuHyzBQC4RCiXEOQ-WgTO5ucfJ543ZQmCciWj39hWG8AhcSDCuGBmraCMTw7sbsr3d96Sk4cWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=RfMQUpwRJSsrCrvDTXsbQ9qW6dlin1O2lrYvpem83lwfz7IxMdCoWMdSt1p58-cHA3cYdbTuY3H1Xcf6py9zcL0zCVNm65UnlbT_0XCXeBZYmVAozG8Ikb6Dh0p0mUiX6nwMlolbI9TTVkU7_04E2kI778hEmeRWaWbOoUHqqnHMKpPXMy1civhjdERuFcfw_No1vO3VyeFMyHKiGMaTPlaWKRlT-gIKk324dKcxsByFm9hw_RvVrjchvJ1G4gMM-owMHh1YWrX9q7auDnL88yeYqrrFfny_nQBcMTZc_Ns7Hnq_ZgYGhHau4JFIC18CgWFVpS_Kji-EIiOVF2qL9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=RfMQUpwRJSsrCrvDTXsbQ9qW6dlin1O2lrYvpem83lwfz7IxMdCoWMdSt1p58-cHA3cYdbTuY3H1Xcf6py9zcL0zCVNm65UnlbT_0XCXeBZYmVAozG8Ikb6Dh0p0mUiX6nwMlolbI9TTVkU7_04E2kI778hEmeRWaWbOoUHqqnHMKpPXMy1civhjdERuFcfw_No1vO3VyeFMyHKiGMaTPlaWKRlT-gIKk324dKcxsByFm9hw_RvVrjchvJ1G4gMM-owMHh1YWrX9q7auDnL88yeYqrrFfny_nQBcMTZc_Ns7Hnq_ZgYGhHau4JFIC18CgWFVpS_Kji-EIiOVF2qL9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N4yiAiX1hQ1DiWDGE36ZCUxooc2C0BnA5Q6gStbYPbiKJEQE2PQDYTq_TS-_M_HWJpekyViK4AtCO7nSzE8YRSi3qtnjjqJm0cIPGXD76ngamIc1FDOT78t3BCVn1N--h1YVTiggehj-mBAYcinanECeXli7hxX2LUeQ6dslh-GRufptCMsFloFXhhsTnAd-bbhcgU6fwyyoxqwKkxHuKEtUFNSJrUOIiVb1RHc0_yZcidk3K0OO1XJS9dpasMqk6PtAzKZUa1SY7s5iqj72q1F1KIHfgoD66KjFrA3krY-GU-a869U4DQjaQyQvayJRgv3mXolCNiVKYOoKx91Rrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OTGH412uW3TLiu63h0DcxeTeuw9mhlDjCggCiI8VQa_MRa2ECgUDbYsVUgoBvoRaQbt8ltl4XPr01wxJOhtDThQD-48dmWKdNfiuYIywATimxyR8B0QElChPXy2iKpFVolY3tHuP_ERa-0BttfkxHN3EvdiGVH1sRYCy1ifAl1yYcvNmwHIUi3iev8JvmPKf_BhCnZ6CI8ugBj11fK7BppPKuD5x2Mo-1_ofNo59Pywc6L6DjHgtnxsmxDE66TzUbHsYrH8DtMYJdTTCqB6vx5nEN538k7xBoFRmOkudkSdq2CtDoxycQMOBDspMWHLc_nZzhFZFmfTAazaFO85Eeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SreFoFafXqzGvg1Eicxbp1ISK_oETKjIvKq25trst_LEPKBRZNZzgvACgNt-N9c3h8uVHYFOGXMe-JnQxCHvnbgu2Dqb4iyK93aLnq4tgn23O6mB0Z7uuDYPJwRX6IdRJyzqR5M9dKHrYoUUGfNZ1EILCMBTylf4LXj2EjZpfxyRjl98MdzX2zTnqFaiZrzQt06kfjiCdcWUwP1ZPMGzfCbBs1XlFoM096MF7OsEEkFlgUVDnueBKoh69qTXhh5IceB3fu5qyyLyYSHq39vhfpotcXO6Iiqc3gZ0_ro848gHIHv7uAK-DjHBDTLQFL4MaqWG_6kp1GAnty7IjUrkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NsaPq1voGC8OYNv5sZi9ENhzBh6KApirJLhQ9DwU_5R2tN1f1R5tLETSJxexYt_4gJNpXrT3LPAxRy6OefKz3WfwxqYuTR8UsHoCdlF3m6irBqbOUZKY1t-YRdCDSD92WWh6zUVqZhXDFgQijS92B0t1iHDFwa0b5mcgXlMamW0JCbe9qtPR-p1Hz28fDdVZZinwlRT6ocyL1OtVQbje1GQp6cRa2Pn1hwmAFEnhbH5uAhMCEms7i-GU0IjXqbT-HLP94LUvr53tIVSiJRFs3rv9ii58hBjSrZ8OlUmFJODB0_JnV5wQvGVb8yOV95CHHIMgY6gWYiCa976NW6dn-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs0CsrSm1ZQPZbCSqJW5YKdnK0dIAQMn3SV-s1LAPh1m7YAIadUrlo9eLFgnfDC3dmXfWHUcrYSHV6TzadIyQuO1vW16PA1hYAdrrle8e9VpgehUNW5Em5o2z29z3Fq64LTVK1SREOYIuE5WDIIcyoz6Rfr178PUmUNHC4KJ9fWz2--74VtdiVE-Trka13LOhbx85gM0QMTACiL8rHI-PvjfrCQ5Zt8AbLPp0cXZ7klQSTWxGvUIphUcysM7Bz2KVbtwG_D8Z9FLST70wCdMZLapLq5KzXziraSu0hm-skKsB5e6RAxLNbKWSeDg1gIfmUJ26S12TcHeTvIAWHGCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S072xGbvXu9tP9UUZVYIjHyKt-u-Y8ZW9aZh2BvYlPQklLEWJMus_gT4j_2ZGxGq9E-nkvqyxBip_Usl3K2SmYmxJ4WvmCW2LDhY4nMh4aFY5HR7C2Hoj82VabE4i7PvD2w1crc3_TWTq5kwHJgzp7euxKDp5IiSONchZIa7WgVRkFPJ1LQpTr-76ZlpOQStOC3sXxYOWRHiB3K7mCB666E-28R3a2DnrpDAGZd763Dxy9O_netgS-s35cDK7MEdXZWcVCovmTJ8H8r5kRw_zh_GLlPn5b2sQwZHBI0nWEd7dv9LPkJ-1VGzfCBLAnyAC2MObrq2_WTBa0ydtxUkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LucFPiueuXgBcrMMVlFGOWrjL7tSTBeuI7rBYkx8L8wSjboqDz1g2N-71aoVdEFEh7hMauO2pjGfydndGECY5JUpFY1SyGhjKLUUXTwtkX4dBYkwGzcU5OkWWYOkM8_FeK2nsqzPxri0SvF3UrbHA471DsG4w5QATD36ZgDQOGVIX0OyDpmLImj6xycdhM-7Rjz8Rv9YK8yGpAKS7eNHzqowOKvh86x3C6Ps1kDcHFiClBeY15M7YOs4UiGAsApQByR5L-smUC8tVlkwH7Ab2TpevcNmNl2Ifp3tT_66A7_Zy-LctO6SchYmixL9xMHT61mPm0jnFVdnrmPll76ymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ixYgdzLvPQ11uQVBxv7ogulNNxb4YQtSOURSDppiHtxoyJb2W3Hco1wLdXEMYXRlRN44ymO81h-q-KutinCVbhjsVmP9iTuiDr18VNwMu7L9yRXNbM6e7cgg8JNQs2G7ozpMJih2rNfyQkbFslNXNZgcjTtGg7edmutrInJ5EI5yAmaGiPOLeHDD1tQnjxTmufFQ8IVQ-Onrc0XFZYoNR7FUO5SwKXpMX94zwaGcK0C3rIJMzx3vvlN81OCPX_bNprLKTQTrP8WkQvwY3WAupPIPMeSeS2uPc6mG-fOOZCEpLp50AsSQaKNxLRPyrNyCOTiP7bVf90isikJi0RB31Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDmCzDyoW5icFskHRK9mtzYrkorcVU7eh0XTMrKpaxuhHC_Q-upAigHZn-DluEvA7my-p1yHqQx1wqZa0hNYTimOFwUC6Z46nhlHbVeFidGVXc_kKhkToFivA2dVcVb3a7XCoHZjJqvQW3KsTpYTl_QyJxRgigov9I9HY6fe_W5V9q3oU_rLjONXrT2SK-g0ScOnrlHdJTVoidRGH0ISlYj3Mu3mQYqOn5nDQYFvd6cHf49nd2c7JQ1pfoZw-FlVjfRqvB2IgBu6cBITqxYNhsbnRHpohy0F1ALul1YyXvRa4cacSWuI5foEDJd1uNQv5A_CH2xRU1kA7oCRB6Rj6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BkduDqMBwgKiWdPwXz2uGtKetygydXKiWm9_DpqMViBwnG4Bex4OnQJElJh7XqWY_AO34qxG_qj8Apsg2LA_OtEtUSpT3aTM1h0L0I7VPxs0_7yICeDfJMZ8gjnlTXQXP3e1poh37kO9fiVokpNHgdMhAUvHwFCOCwgHizcA_hBBH1gXyJzkMGEmO1RVS-UWsGkA6YsTO8nyDcmagpVownrwwwnHDzTQZ6-ATwS6Q7nDT79HcJqeunIK3SXOhV1v_4Rmr9WS29J6twANkb2seYd9sdBUO5YuxArrOcYhzRFirjvOTCkRQ9lCJhdLeGmWe6uMhw9zVi5TEIFv_PbtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sFzLw-4G_UB8Gj7rZ-1An7Rdodw88Q75873WhExLKDyg9yCFtaZ-pj__yWx-bfQ6_oRVw6CwAbg3EjjI63-HYe4Zksg6xvI3yEkBQFOaORk9AukjqsTsb-OW4jcV20mXz4x25rsWEvcodV5QprXdSlGIf5r5e5Jfic42lyl8AtUTZht6ntwGWLYb0DmXOpfjAj-ZCJV81a6mhBngPmWemYlOCPZGG1TFFKKQcYPXN0axCQloEBjtYG1FtTEPaeVG29eVV0VKzsSFMn7V3n8827w_QlsDk4rxWpWhZT8EBRYSZptR0WgHdMm_eLnIbjs9DDia6Hv0caRIg-vJCypkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ldhu79amjuSI-9ryuP4bYJBSt1ia4l3cDJtNlyxI7Hamcke7WuMFhz3wN7o1xr4rm3wOCNr-vGPXF4T1As5nFXuoTEyP7R2jBqaynoWZphJMnTYUSnCb5QEaBFodY1_2lPUVfcyAu9NOypzW4xa8zUbZ5Rvu9CFqAPjCMsQmVxTqJe64qfYr9pT1v61QiXB3wJUnaK0_rR0rx_86V2_skwjigoGWQbqvry60kZOP41zrSWotvelfKlmV-AxyTJqgBrM3pWnhOUsFfJLgQOrYILqoPpMa7SfMitr-DLkm4dhBL0Dd5uY86sJw5bb63pNhk4dw-4xIFc6BZo3XQ9-UMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g4st6aKZCucdYrXPqLzSnmytXk7FDrgZYSUDR3trqbOyQ5u82-83Rg1tHVKA6zgA2QjUXv53EAYXFK13vuhiFXhGoJXPTZhASskGsrV-aEm8o0plkYY5daFtQHH1fWIoG1sdFPUhiTh9esT33HXBNoRVoPl-Ukpmgh-1AxGLIGEbrFffUJa3pBaO52mLFqrHw4ydEvM0yn5yLQdUdws16pwJsngkZyzSR-7wMUvQ1jhstiJxk5OsrW2kLNYjwAEFdZXu1tpAXeo4uiSrDXuxbixvKhXIq1gxWH_JwnCG-Mytt8PkzsPANSNSEqVcV-iuC1BE18M4dB-xE0Y-qb9oqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fPrLT65rpyKcc5GEwPkEzWdsmf_OxiuKMA5HuCMkZpxlLku2Y9flVAPgu0uvB5kAoHfTzk4V6Yqnd66QOwH69OpSD9RlThqcm2rDr7--M9LKZ0yAFPQ7pdilxfyx6_kVj2y6wD9ApeE4qAEiavNpIFz2INnZmwk8Q-P4N4DDbaVhZHeupRRCG-wgHbLclgwSRYNN4oJut6fSWGG_UZKd6ExXLbO3StuzCA8gq2vMYTa_ObVAWT-tpskaZz6KA_mwihKc-FGK00W7yetlc6wQVnB16ajOAUhWqiEq92Cndp7HzBo6lBrqhd12K0o-Si_uuAvAynKZQpP_P06ajUbOqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/caRU5rM9dLJfeEkIxbGH8ee6HSTOcaRxOp5q9lFR4JWuYPe_HiNlgHI60VNgP_ukIzJG2SOVdgNPxSDwGB1mxtPix8D0JDqAWWqKnye39LY6L6PYCPiFo7rwnOLUunjA1SvJ73yv927V1uoAhslKcjaJJahkTFK_-43H92xfoOk8unsCE4p4jKsneIGRYaurBJnLMsI2a7PtuHIavdvBlB7V07jZnu06zOnTAPgaU7LMfXYMBKDtCm62kqACRwEO3_0t7lACyq4oT6FNAcGvPPLq_kiMTxcLG5IifM8inntIz_mC3xmClHECev3Tl0jMXuPv4R-jGxS6QNyTgDmcGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JLV8xZB5TUrU0aVzObFXX_C3WkLInh7-bWs8VKISE6q4lIauGDK7EPTZ4ZOmjkzqJV1Uwhd87IsgI9cJlTTvzV__JE7Eat_qLjprdGcSaxuxrk9DPoJZu6i6fIQu--He586iEmVhoyGelV7B4MzSp_nRdCfy6Ih7Unn7DQ-sqb404H_4T-jEsSTnijQ4zhILrSPToH9AbvMEPZkudH3YNWLMjRmTXoLwygzLnPaIJALuT-5CdDuK_-9O70oXh6rtsPRwT8Z1tgglTHHKN_hfacGf7FmJZs5JjihpTPvuVWwsCIW1gzbNikDI0L6vUxIoZYO4-a4yYorxwFZxNWir9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UocCfw13ybsTw8m3UDKBgakWpbjMgJmgx874dWE_qHxaTYcnbi7Zuzw0Wlpxos4T6c8F4kVL55ZGkRSld70jJUxxOp_QAAebmO7Q4sZwDQc7wt973dhx9GpfXQUnEmCLLEJ61zJ6d7yBg89Kv5mj_wcJ7lR6noRwxVhwIBECzSl-MQ9FWcNSyG18krTa_TLwtxigS0v5n9oqIsjS-h-rskYHSat9zS1CeQfEyvOF9rgt424DtYZO8M7-gSkyXvVZOfVQ7LD-iwoL_9iGp7e3s5tb5DhJwHPRmvpp3doOOVDNieLEokJqH585EVV8Mb0VGwD1bJPktmgRiEDj6OFzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l0nnZ_abTMyjFnImm0nZ4buM1cM5OzSFGQe1RsnRiASub0GHDRJEsAWDp-V3UexvSqVg7AoLWPG5FvWov2LKlb_6rJzKWO_-ZQjytLuwfkyZfyRtZIvs1oyMsQEoVgqPZ-Ra5DjwqHjO_RuEunlIKlCzgKdXYII771rlvVAP1_0cZqrmyGLqBMgCCe3Vi3A64CUoM7IKUP9PQhAh_J51rPZW21zg-XQPKRJaO56cu8Al7-zWTGFAzaX8t8qgX2H0GL1fAVrSDg79736WHjKD2sf_Ib4HY7tk1fUXp3nBveVxOD6jBeK-VFA1J_Y_1u6ke0lOTQI1yWYsMllCtXf2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SWsio9Lg3dYErEvSPja6229BOZ4ctAW_aH9N1uPumS2LYSC8jmUIW9rsK7OvBC-t2QvfL0ulny5M0OxVKdyqL7yaeTAt0kFwFonfTWU0uz3x3N-F-KO_SgLmaqEsfvPuK5JLGYuPllZeSXjWLwf26giO_VBTGov-Ah7FhbopvuQpAEeEnJIhKxxUYPrjzsQUY-1Y4JzZmxtNz1K1ZnqnT37QZ9IFsxLv_7t2MMH42h5rvU7pE-v8XpSE7SEM53ztrlhUxEkyMbfptLr_xZ5bzQWsEE4UIYTH1MIFwr054X5bW3D6s3Y4t5htVA5Qy24NKKV9WicazUjWGEDHMVYbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RyWyeyFhQlBVdRZ3Mo3yW-q74puup1T7aEt0iDuo7HzAAUccOm_-X0Y6hv_ZJnVCb8uVpqX1fqcDLrxpOadJKcCi-pq_k9dl53w6xzr5WX8hpTUadg5JCaf_ffag_VVQHPB-fRjPTjxzDfvlxHJ0yB8vu7R0ZvJYYFr5AaFoifeFZswAUyhztGZ0cuT1_bcSHRF3GeJLsuaJPBXtqXPo9DmcLyodbsikpPBWBEO2XEG8H61vvdIw4WvNZC3OqNyuu8dYUPhmdj9HWaA2OoUPNJxGpRYZYlbFVoCEeDrNW_538B0CvzgP2yynGz4MjFJhkPacMC3WsRSihauHAprfHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=FgJvuyH5UM3idb9ikty_okS4eBQoPk2JPEhgZQBKzoiy-14neNNNzpaY4OYL-ix0dKee2D7VpdolyUwPxk9BALiRV_pCoYQiT1eau5h_Ek1LNOJQrpaA5KyReprxSp_o0da4jGexmr5wnkDfpngf1V0EZIC7zuyyOShJ6d7dFraogUJ6pb2afHnzHpjLA-HdE7Cj3XTmwsnY6x-fWkwXhbs2Dpd7W1Cy9Fhjxk7qtvrV6yyZk1FKmG0XlP2hKcohU_wdoGnSr5Vu1428v17J_rSIkVo_6-PcHBmIHqtL4fY0D3ZZCPgKtUL_LbmmBwYPm9QaPvMZDB2JHvyok6NxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=FgJvuyH5UM3idb9ikty_okS4eBQoPk2JPEhgZQBKzoiy-14neNNNzpaY4OYL-ix0dKee2D7VpdolyUwPxk9BALiRV_pCoYQiT1eau5h_Ek1LNOJQrpaA5KyReprxSp_o0da4jGexmr5wnkDfpngf1V0EZIC7zuyyOShJ6d7dFraogUJ6pb2afHnzHpjLA-HdE7Cj3XTmwsnY6x-fWkwXhbs2Dpd7W1Cy9Fhjxk7qtvrV6yyZk1FKmG0XlP2hKcohU_wdoGnSr5Vu1428v17J_rSIkVo_6-PcHBmIHqtL4fY0D3ZZCPgKtUL_LbmmBwYPm9QaPvMZDB2JHvyok6NxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQEcIbhNfQ7VypUMHEEA2AGRcXt5562ZXjzJyErfrKB5ylfqnVAkvb1DFoaQAXGWJpArrOvRXecMbyxNEepjUTtpc-G7U_dDYdVb0nsrxfsOBuH6JAyIt3zJl9TBqlMvAtj50_RkjrL9u6BsK2EvzlWxZHiH66wgv9zaVz7KSY4wNuycI1HDmvVJhbJQ9OAwfDoFOA7EXp3hoboFw197cisFkwna3aehenN1eK4GVNfBlps7LUkhkk4AwUOIf-rgsjvxIaYIf6V4JeABOqCNGRG6Zyir_ntbHuAqn8iI-FJQnemmgZ_41TpG7oCmjsb5FMD1ihfJRWyb5mgCv8by1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHh8QC5IH_DWrm3MKvfPj3ljYihubzfPnzU9AoRiCvXrIGeMgAsqcsFWeuLTNr9oXWjrf-4wZPPxLd2qnkIem_e5k9Oil57mqiH9Ze2X2IDffuqXhMQBCphFGcX1nd77XgtEPLZYTN5_DWTWTXGPLuhJXQJNghPBapGCntgt97BzemrlKYytW6dOo5gPG2Ch_Ooi7AvmLx8vnWtzqw3zbZJrVmpqB19EW8rScvLzdHsaLnfSnt_B77fUQlRzbzvpyMQgPPptcW9w-k1fXBEkpqWtn7d-fCr5aqPDAChbT3FCsChP-nUFVZhoyyPRCTXfZt5952x2sDY1V1y18AquEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJLzjlFBQcxPT41qK3adObKWdGZm1JnbQT22ePiZVgVcUyXz8xE2KBdK0dZ8B-ZdmjGx8szyS8AWb--m6xGYtpivMCMVyJHoKIH6p0Z7WxD4ahKSFT0JNoRcefqdrOVtu5-Fy4HMfDKNzMCRw-WRqgBy7XT_ZjLXYjeuPjdlBPGCLjmqmwTlerwpAw147e5JXgBxdFhDBUcQS_H-AbCzLMZD5U9xgVO04oJsmZ56gKoYrIa_oxPwYsvEyhnn4Sb06C6__gCjNg8pNZKArxDwAT8UtXZmZxGgPX3pxRPaBPY_H18eNX2YjlXqBP4Y7fyfeWoNfX3FNhQeJGwUGIEFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PGS_Ly4iQmqXnWe0rq5KWHjDGRbCNDQCH-6_akklEDXAeNKPooiYbqFw7FZDfKwhDW8zpXkkKKS6FqvEHrMK3Jp9sRVjvAC7yxqTMr_lTG-1R2-wkzDQgnbWmVkxWUEVR-fT0MKITAKOWVNbr905yZbS3bUdd8iojW8KPvitM2PB3L9Q-Gv8WNBPMZAcvX5c-XOVKDpYP6nbcTwYfJd8R206jOYuTJz2DhU6c9j1vZlmjtgvwkoTzVWLTLCTRPh7LAaGZqZlMc7h31-OsUclfARo7pvDXwZJuNJQ9Smcxaw60soLq6ExsJWihDbLuj5hFvkDd_HMLWt02iHZEWfOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o4uT14RSynSk7GgEyDaiqrbKdM_-liBFmCoEcTXeqtI4A8STfcytUpHLvs-gafuk2q93wMd3S1J8LCb0hKWCzGBtJx8MYyf-EeV3UgrJHwTQAftf9ArHrA7N9FwOzPOd1-AFz_pFw2gjyHqcB54uKhLCvB6acg-TT2cVjWaz2hfYPBT-3P8GJvVZy8Aa9jiAXQ8oh5o1BU_2_Z1Et3VH1yH9cZHUvct3HsQ0IZZwCtKh_5J8aMMaGZ5eO2AmUL7Ukf84AjPnHNLQvJbXoUY03VWdy1Lw1SrB0r84NzbgLqJDYbJuKpxoawvbJVtO-KGgd_UPe0aAGfh1XVv3oMlWnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gcIZkeAS8ajNBvjwvXl1VeXQx4pSwv59Khq52KZLqnd4RpuWCcRUMD5ErtAUksKh6t1DpTlOgBKqiNJ_Oj0A2NIF_odvLHyNNb9tlGnmcxRsgntgecsMNPf8KDD9UACXHZMn1vS1iBkQfo_PKEARxX_Sdp3Qtu6GgVB9UsH__qJ-G7KWri_V7C-4BoSJmKLPHaOtHLcogNB8Yg1pr1pGG_cfP-n8M2P_xi-MDlvrT8HKi58iwTDuiVlyb6ml1_DdcCHwKOJHKbPvKBkIHH390RGtXRY9vGsGa7zdgMS9R1b1BewChC6rX5E5dZKYxRFKJFjaYYqRjwrtaWlbuMwJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q4FaDwnysdv1gLb_CLnWTS7_d3sJpRZ4A_W-ywj_IV7RtbMIYPfpqH8olZCnU6v3tEw6OzaMk-mqgAoHjWha3suK1nmH1qDTJDfM2rb-bPGEFYxUGJ75IBLhWQeJIbECDKaadGc0KiyoqK4Cy7VXYpnqywG8bYK6hvmSgluMQsYHYUuFuKXq74n6aivhlV-bvWJdJj9LgQphj1fuyewMSM6CVwnI54VZqARrBwT_eIKak9_1STH0eWIaPtaGr8oFPbzTa9F1j_23KTUmpmh4hKTwhsceg66hz8mPGx2dgmVYWsM_p5M6RFB3GiGNNbgEGPeamBtGl7ubYczU25UVXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=epYdUR7dlWQ9UsuCd8q0rawIK2IhPckN9eMbI6jzVHUhjop6GIbazj_kZwmaM4tjYXE2XBhvtZ6_qcz8L-iU8_PCH1NRm4JJalMd7tPNf6seslIULQa3kf9QUAIVjQQzikWdBwd-Qo2fvUAnAoFhU17QW48TIQiy4ofr2xoPJzo8c75l5vZYxBQXVqas2kgR5MuKHhqlxFL7eODi7WnnJupBoI-GETxoi8zf1A0Y8yXomL0h22OCUT5SGc7NOAfmx7XGtG9sp4a97kguMtkivYNbR6G2CA25ZETcjVWouAeEzlwqp7IxQ4YNYZPOz1Ws6Hvc9O8i81sWaUuTL8Pvhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=epYdUR7dlWQ9UsuCd8q0rawIK2IhPckN9eMbI6jzVHUhjop6GIbazj_kZwmaM4tjYXE2XBhvtZ6_qcz8L-iU8_PCH1NRm4JJalMd7tPNf6seslIULQa3kf9QUAIVjQQzikWdBwd-Qo2fvUAnAoFhU17QW48TIQiy4ofr2xoPJzo8c75l5vZYxBQXVqas2kgR5MuKHhqlxFL7eODi7WnnJupBoI-GETxoi8zf1A0Y8yXomL0h22OCUT5SGc7NOAfmx7XGtG9sp4a97kguMtkivYNbR6G2CA25ZETcjVWouAeEzlwqp7IxQ4YNYZPOz1Ws6Hvc9O8i81sWaUuTL8Pvhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sw1L-YqSgMJmMlnGuL7e-sGIZ0dHyDXF8leK0FVNS4j-VC6jf_TgTGL3HQfB9mrFLdOBOjybWL_4Kj2DvI3400HMZkyHUxN8LL_kr6VEcgbp7TlQVieDGAX83HJMaKgr3DGXijJM6RtWr1dOCgTP9YP-ZvZxDfMsij4UhuhkLN2QLckjxBUsX9wEOghnp-a6kHGvQgMFxPlqzgKr0VaGTCjjG4KszGZAtYkIuywAQDauUUdiF7URgUDUffPoHwfCm1CQuVMDj5rFNb-cy7hlQyjuwJfgh2zkLXvPx55WDbQvm1nl0RbOu5XiwOgl4U60Q3r6fXf3Yuy9BbEuNfWa3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E_qxpbGOMfAZAq_QgyGn5KT8TlebCq4jkoo3W7HfzemiNll7Z5QBzYaNCoXezWuq_Guz1okfZqe8LKhD2VZ1GWvE3VXnlGoKH6COQLqRNUCJtXFGyF7HqKZGu1g6ujyDibRUUCBdf0P1KtZP78WxJli4mztn61uOll3Z2f2KyvvhNk2_zBusYc6AzuvhCUOwj7fpNOXcl85CyLaKUROtSmfY-MMhA7yx1KX8lNhTXph3OzLMOyv2syFz9MCIyVph9UqSx4NBqdehDj_Fn7ikM8Ltzif8IP6cSwAjRYBV6HUfjvsrvD37Q1B93KzEnWAGQdnXsJyg3pl_c0zMGkmfaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X-vxWCscOhADELpKuLpx1W-41tD0rfn_zNhtBxxDofWO-yve_XuOVFM9X0v7cJ197D1AkAubPfLJNJBanJr-1sKhDOBhPD9I2rSUFsh-txiUblZm_oUje0Zn06STyHlSih2iiocfrp-t02iGURSmU9g0OFpYONeLqE7ZCwNQ6udVt9_UsPASAyfBKq0yX-LT6PVsPD3MoyRCZxZRskp2xEb49C8h0ONAhobORiRPTnbJ1hVrEVmtGa4DMZel40Lreu_zZgGjUF_D1ROo7j6EWiTKU7alw2tqwanInZUpmMQmRq4EGaeT84Cc7B1DL2NHk_IyQJPxzEwxAzgAQC1WUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MPrXg8k9qLJM8myrIJy4CS7sCBEDHaiaAq3AUXa9bmR6ODF9XLq2O1LFzxnoZ4Shu95h9753lTH_HPRCZ3c6sz88_4srUSYEsFgkKiUErZ3zwAuxx8yP52-SKpDGt_Ec91wqnTsH7T90HB-k0hUe18I6o8Bzomk6HfeEkrT2H_GkFqkDD5VWzlWPWo_25KeNHUT-rZ08ZnycWoreWY4JXriugf9ukfV6bTzlufkeVhIALwKcdqAQw5zMuCkHC9Gs4WP8awMKIaI__4TX5ffaW2cZ1CeR8DwJDZETBhTIVsVMTVrXHqYbFLfL-cTDj8crGF_ma6d90Jx8vyy8TSyy-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=R6sp2WYX3PcP772LfxxKLtZnTqjmFuCUzW7ODfsuz-Uy5jV9Wq-79im1o9y-utRreRvwFYjb-lFN1ikD0aV4iqdIWPpfsKi8v_YLTRlBhuWYaioaThOPi7d85qoA5W97GuC2tX7aiiRTv_SXfSnpW8ik-AB-2auOvESvWOsbfwFRa58v2hIk3QSdK3f_RLd6gh1Q9DG3-k7QhfMgGZ55aLAclp9m1phkTPtC1H2_6uLCEznjPCYc2QCwNEQXugxMfTRPTjcMp5e8z-Dz3-hJ7vpoex3fpQ9KUHATeRbw9bWg8TsLgs3hgEs5f86-SVbO0CArVNY1nb2bNnHx9hgh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=R6sp2WYX3PcP772LfxxKLtZnTqjmFuCUzW7ODfsuz-Uy5jV9Wq-79im1o9y-utRreRvwFYjb-lFN1ikD0aV4iqdIWPpfsKi8v_YLTRlBhuWYaioaThOPi7d85qoA5W97GuC2tX7aiiRTv_SXfSnpW8ik-AB-2auOvESvWOsbfwFRa58v2hIk3QSdK3f_RLd6gh1Q9DG3-k7QhfMgGZ55aLAclp9m1phkTPtC1H2_6uLCEznjPCYc2QCwNEQXugxMfTRPTjcMp5e8z-Dz3-hJ7vpoex3fpQ9KUHATeRbw9bWg8TsLgs3hgEs5f86-SVbO0CArVNY1nb2bNnHx9hgh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=N3g0jIbiW8mO7NWnkidb2ROz1x_r0gSuGVnT1VyOvgtUZ78UIjOr9uJ12B9ej_T3xGLvgsVBhHrprrHR14qqUnvQKYFox7bZ2a047XDAgk87DJvhbUBL5Dvy9DfafJZvh63TaJEw8GeJWPxI2M84li2W7iyXlO-U7CFrcpeg5B9-GIp1y1KQiWr3twI_bRLfOsWr33IJ7tEByNFh--IJl_1Cli24H_4E6t9oprSX9m51IstbsdH7dkO-S_HfPfHCXaaaiTw8eIX7SHEad3Ws8Fw6UwEKMTiXWDZ_6CZB2eJArWQ4stQO8ecNJ5vo0pS15j-0xfp1tFmLycvtGsuhDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=N3g0jIbiW8mO7NWnkidb2ROz1x_r0gSuGVnT1VyOvgtUZ78UIjOr9uJ12B9ej_T3xGLvgsVBhHrprrHR14qqUnvQKYFox7bZ2a047XDAgk87DJvhbUBL5Dvy9DfafJZvh63TaJEw8GeJWPxI2M84li2W7iyXlO-U7CFrcpeg5B9-GIp1y1KQiWr3twI_bRLfOsWr33IJ7tEByNFh--IJl_1Cli24H_4E6t9oprSX9m51IstbsdH7dkO-S_HfPfHCXaaaiTw8eIX7SHEad3Ws8Fw6UwEKMTiXWDZ_6CZB2eJArWQ4stQO8ecNJ5vo0pS15j-0xfp1tFmLycvtGsuhDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R9EXApZLsOR6_-vpTvmO5vY_PY1i7ELv2hM1L9axpXLLwNgl5Pn_PNNoxm9Rl7ItRCbBqS8uG_-6XBrmJL0Sya2JakOUrbdjJxsrzZuW1N9hV0mifxMbYJxd6LxxT3QYwn99keMr0X7PMYl2sGcT4pAk8E9581zypAoNwOtES6xTHq3dKhdevnVDdaLupJCdSALFeDjnT_Nq9ciUa_LC4byJm9gX9K17FyuSdkb2UnzP8cSiaGR-N9HOwpLE35kwD82f1PqCAeScL9TTL0nAEKaFQMyO1W4ilS4zEfJRXlqux5A2vukKsjbb3p_Uny8ZH5CreZb4EMM2L7OxSOhOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OwOeUZCELdydqRbdIgy0YqIKSBDME3I6XtQWpjeS7IwLH1Qr-MZjA2NwPBe-rNEwPMqpedmpYUpuhncZHMC38670FmPSsc_H_bTuaVuMezqsOribwnn1AsfpjQ4_lWpKocVJUEkOpPADZZS8XpR4tH8xN9RfBi7_kl73hD7kuz7I69dBgkPy1uBVcok97YlecitIe7sUBjl1NQnmI8Q24hlm_iP4DseFx_mpHypVrocWKoDAjRHcLOw3KFlZnNsas6coAeW93etNvl_4s64rZqmqpqnXxxSEm1RBoIHkhOSL1gn_CIJ3w9IjG-FSfvtu7qVkfHCGoRDRh0o2WIffBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/d769RhzWqRxFU7ggorqajnUOmvPxxkCAT7qxRVGM5Dy0I76fUEAzlS8LDnLzmEwjfCibdUqRwupaIgd3Mne7OANYp8hEYD6gtCqfWsyetRKRro74ZhNXa3kPYyCtrDzQtSTHwTZufJF1b7iHLs9Rw1TUP5ofypNdsK3AzZazMs7gkEZRn2Qny71DWw3jYg6S16a3_dkI8qM9-AP879T8_QEWoBmBZKUtd-SY3mqYA5qniRSvOC0CdI6r3jATqM4qqiwpqHhs23if7N1KAiLRAjZdlxABZN_ubwQhWXjCDybVhj0L4QJhOOhIYiiHxzQF7FVwLpM80vkEDlxxnxlA6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZmIn7GOjpYEp1Lr1-MZyYWwwtregLYD1qNK_c0AcFKbFi_5YDl3EqqHFnTosRzxlSf3NGJ4kZzmXmjTMNzVdqOyFAJnu7e-JzL8JsbfT_4H-V25GOdbvDNlLvVeOPpiNi3Stj0wDF0AEzWToK7EHO_zZrH6JvACvP8Ji7Q0-6Mo0VJmbeov94Jk2GrsNfQ7-YFQwME1425jy5R1E2Y4d_WRvTToZN7KkeTvRlD8xJ9gw9q9S4Tps958h3iQRo5raUtGfbaY33Cp40VtfUv3ffy7mmatU1wckJ3k9Evb-u1Q86G36h39dJ-1WLsg59nLWAbsb53e6jbmDOljA9jwfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fMsa_SXNKTggaBtnpk4yIf8iPy8z7XH9Cpkl6sjAhnLxsjgFQkXDIA5-8R1R1U1P0vJozBhNfots122NFzfOrsrIjZJZvB_b-9nueUxa11iqEccpF1dB-mU8b2H0WCNvxzqerAWd1xDyZY4384FT46nEk2oR30-xJCjOVu5JJIQXRJVeVA_TpRs3izzrjDGIz-rVwkq3NkZsA1MOa98VomGO3e-dwSilq9NLEUbxyxWbnr3_9RLxx_lvC9hhnmcX9kSdp6yEh0yS4D2t0NXXKpxw3okzbuVGc-4eg3ayo9-AssbHW7PiQfCU7C9lU8s7PQdHdlbNxH9i5OVkaH3wAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
