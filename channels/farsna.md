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
<img src="https://cdn4.telesco.pe/file/VWO0aYo5UMUIwy2PHfdffMSbs8YezV9vByp1BbOH-Ox3ECudvjb2TsMBQ57IqFKCW_z4b6zkQx9pSaIBwRKj83s7yEd2WzZuNfK0r6d_hZ0OnnMUlvZo5MbrfphaAPqnPj9e-bQAUSpzGDiFL-pLlg4y4zuilH87_Rw1wMohHqmD6ke0GxFlt7HYw0YtDhfRD0RhstgSMeF_GktDpSheJuHjedIuPzYQjwT4S-0UlpAxE80DTk53CT0WrsSui5wwPpDXhzuf_70V2mwllCIuI-AnilgyCG25qiYwmZtww9wcF8J4fzRIiGTAKAL5ZO_XGfKkmIWW45b-x4WoecKkhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 01:59:37</div>
<hr>

<div class="tg-post" id="msg-450531">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
اصابت موشک‌های دشمن آمریکایی به حوالی بندرلنگه
🔹
استانداری هرمزگان: در ساعت ۰۱:۳۰ نقاطی در حوالی بندرلنگه مورد حملۀ دشمن آمریکایی قرار گرفت.
🔹
گزارش‌های تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/450531" target="_blank">📅 02:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450530">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قطع برق نقاطی از کیش ناشی از مشکل پست برق است
🔹
استانداری هرمزگان: در جزیرۀ کیش یک پست برق با مشکل مواجه شده است و باعث قطع برق یک منطقه کوچک شده که به‌زودی وصل می‌شود.
🔹
حمله‌ای به جزیرۀ کیش صورت نگرفته و برق دیگر مناطق کیش پایدار و مشکلی در این زمینه وجود…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/farsna/450530" target="_blank">📅 01:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450529">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35174e301a.mp4?token=Ek3eE3jq8faYjAMolyjp2zkvTO9jR3sqkY3GiUCYNlpd64iGmyhm1ZwA6CGfDF6JhoH2CKAJqSWPGzmotHUju_ElWUl_Be2Tgl2Ux-IDOBeuKUTDm-L9vm7HmfTX1h0d4_8I_IZqWb05TFDD0KOe1g2qlxryMu_sGb94acQeLeC39dBEzsN1P5eKDsGsMStVCC_ef8GsxeTsnMEYFVMjLSQ_Ns-4NYMproJJna0ZUApx_bQkFyV5LAFyqAlVSnKwQNHD_Qd_3dBYthH2-PK8Cgrn93NCdDV5ywZwsswX2xnrUh0vqgPAnYnb9T8Uf3-a_RrZOfqhri70PVXWjx-ayw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35174e301a.mp4?token=Ek3eE3jq8faYjAMolyjp2zkvTO9jR3sqkY3GiUCYNlpd64iGmyhm1ZwA6CGfDF6JhoH2CKAJqSWPGzmotHUju_ElWUl_Be2Tgl2Ux-IDOBeuKUTDm-L9vm7HmfTX1h0d4_8I_IZqWb05TFDD0KOe1g2qlxryMu_sGb94acQeLeC39dBEzsN1P5eKDsGsMStVCC_ef8GsxeTsnMEYFVMjLSQ_Ns-4NYMproJJna0ZUApx_bQkFyV5LAFyqAlVSnKwQNHD_Qd_3dBYthH2-PK8Cgrn93NCdDV5ywZwsswX2xnrUh0vqgPAnYnb9T8Uf3-a_RrZOfqhri70PVXWjx-ayw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رادارهای آمریکایی در کویت هدف قرار گرفت  @Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/450529" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450528">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
منابع عراقی: برق بیشتر مناطق اربیل قطع شده است.  @Farsna</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/450528" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450527">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
حملۀ موشکی دشمن به پایگاه‌های هوایی و دریایی بوشهر
🔹
معاون استانداری بوشهر: در حملۀ دقایقی پیش به بوشهر چند فروند موشک دشمن آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/450527" target="_blank">📅 01:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450526">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وقوع چندین انفجار در کویت
🔹
منابع محلی از شنیده شدن صدای چندین انفجار در کویت خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/450526" target="_blank">📅 01:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450525">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
منابع عراقی: برق بیشتر مناطق اربیل قطع شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/450525" target="_blank">📅 01:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450524">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5a285a11.mp4?token=c6Om5EvCUMLzb_F9uz8jo6ivduJ40m_U7WHdFQr6Tp6MONLWIEOm0guneod4LT14y60728Qr1ExGhHkuxBhL-CaYQdcGLXBLqPT7mi1oofclj0yP_9-WMGWbfqLhmw4Ht571iLvCY_ZDkc0FI7vai0eS4DmQTGYrfywlOpEaWj4BkukemL1axQZcKndpHWlno5dN5aJwh1KSovprlZD9R4Ow4NEqbBXR7crYegl21zaia3hN-f3t1MxDbEHXJkvJ2rZZOcKaJNc1_MI-oNGZDup57imsgYRV6DEUK9dLrTJ2SCKTyHV9ISiOQ7gLPxxpwi1K4EO3c2AZ67LPgZcaJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5a285a11.mp4?token=c6Om5EvCUMLzb_F9uz8jo6ivduJ40m_U7WHdFQr6Tp6MONLWIEOm0guneod4LT14y60728Qr1ExGhHkuxBhL-CaYQdcGLXBLqPT7mi1oofclj0yP_9-WMGWbfqLhmw4Ht571iLvCY_ZDkc0FI7vai0eS4DmQTGYrfywlOpEaWj4BkukemL1axQZcKndpHWlno5dN5aJwh1KSovprlZD9R4Ow4NEqbBXR7crYegl21zaia3hN-f3t1MxDbEHXJkvJ2rZZOcKaJNc1_MI-oNGZDup57imsgYRV6DEUK9dLrTJ2SCKTyHV9ISiOQ7gLPxxpwi1K4EO3c2AZ67LPgZcaJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رسانه‌های عراقی از شنیده شدن صدای انفجارهای بسیار قوی در کویت و شنیده‌شدن آن از بصره خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/450524" target="_blank">📅 01:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450523">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از فرودگاه ایرانشهر پس از حملۀ دشمن آمریکایی   @Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/450523" target="_blank">📅 01:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450522">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قطع برق نقاطی از کیش ناشی از مشکل پست برق است
🔹
استانداری هرمزگان: در جزیرۀ کیش یک پست برق با مشکل مواجه شده است و باعث قطع برق یک منطقه کوچک شده که به‌زودی وصل می‌شود.
🔹
حمله‌ای به جزیرۀ کیش صورت نگرفته و برق دیگر مناطق کیش پایدار و مشکلی در این زمینه وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/450522" target="_blank">📅 01:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450521">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به یکی از مناطق ویسیان در لرستان
🔹
معاون استانداری لرستان: دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی را مورد حمله قرار داد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/450521" target="_blank">📅 01:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450520">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40e8f652c.mp4?token=W9mTSweTS0jTPHnuPTrxRbfgfB3PwjqKF2PsYL0pW4xOs0MIT4ihpXPwN8Qj30lkeFwPaRgmRdZo76wyQgu3T8llulCexPv07807ZHX37Dnp4fcvwdAEbYHU3zyoGBlfzcWV3SwG_L9Xlc-n1eVqxxCA38hAW_kkUopi6vlaA7OyPI7h2ovzXsSJ5k_sQuqZsVAVI4aqbYfuz9ZeMd1pKTjxopkvrdxDKuIx8P192qvcKaxbzSYZ9hw6AlHQPeEaWXAzdINn1mGwAZIPRrIT7cb4pFRTGRy7nADff1Cbe-_bXioJ-H-dx5dGBHucuwgkA1fYD0-3UbEPShjaMwO8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40e8f652c.mp4?token=W9mTSweTS0jTPHnuPTrxRbfgfB3PwjqKF2PsYL0pW4xOs0MIT4ihpXPwN8Qj30lkeFwPaRgmRdZo76wyQgu3T8llulCexPv07807ZHX37Dnp4fcvwdAEbYHU3zyoGBlfzcWV3SwG_L9Xlc-n1eVqxxCA38hAW_kkUopi6vlaA7OyPI7h2ovzXsSJ5k_sQuqZsVAVI4aqbYfuz9ZeMd1pKTjxopkvrdxDKuIx8P192qvcKaxbzSYZ9hw6AlHQPeEaWXAzdINn1mGwAZIPRrIT7cb4pFRTGRy7nADff1Cbe-_bXioJ-H-dx5dGBHucuwgkA1fYD0-3UbEPShjaMwO8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملهٔ موشکی دشمن به حوالی ایرانشهر
🔹
دقایقی پیش موشک‌های دشمن آمریکایی به حوالی ایرانشهر اصابت کرد.
🔹
اخبار اولیه از اصابت موشک‌ها به حوالی فرودگاه ایرانشهر حکایت دارد.
🔹
هنوز مسئولان دربارهٔ این حمله اظهارنظری نکرده‌اند و گزارشی مبنی بر شهادت و مجروحیت بر…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/450520" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450519">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8947f1210.mp4?token=X6L-vqmxm8ayD8YyiZ90wewcwu5NBgzkllSA4Bpf6AbZhS9DNaykhq__w8Pcjy93Pg-U6eLxHR2eQy3FzKz-OgHFdvX0TtvJFBiTZ4RVBtYJ7Oc9T4hXpnx0dbnvTZbn0Lf3fY4fPCqk6sF0sNEMrLRFgYBmHRSTNvBiGrwyUJGF3S8XMhCO6_ViODWQ0WW3lYr0gXWX5gJhDEMIKS3dtN6c5GZMp8xQtV5OUD_kL6PlyDEUkcPm2XmT1ekMFDt4I0h-ixccwkGDPaUbkTTvd33DTMMo9TqSkVPKXu8inbNeWJI5kRm1qO_wOa887g7zM0gwaxfZTIEnuoGs5Or9IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8947f1210.mp4?token=X6L-vqmxm8ayD8YyiZ90wewcwu5NBgzkllSA4Bpf6AbZhS9DNaykhq__w8Pcjy93Pg-U6eLxHR2eQy3FzKz-OgHFdvX0TtvJFBiTZ4RVBtYJ7Oc9T4hXpnx0dbnvTZbn0Lf3fY4fPCqk6sF0sNEMrLRFgYBmHRSTNvBiGrwyUJGF3S8XMhCO6_ViODWQ0WW3lYr0gXWX5gJhDEMIKS3dtN6c5GZMp8xQtV5OUD_kL6PlyDEUkcPm2XmT1ekMFDt4I0h-ixccwkGDPaUbkTTvd33DTMMo9TqSkVPKXu8inbNeWJI5kRm1qO_wOa887g7zM0gwaxfZTIEnuoGs5Or9IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلی آخر را به دشمن بزنید
🔹
شهید حاج قاسم سلیمانی: چه غیرتی می‌تواند کنار زن و بچه‌اش بنشیند و بگوید به من چه! اهواز را بمباران می‌کنند که بکنند؟
🔹
نه این مرام ما نیست. این دشمن سیلی می‌خواهد؛ امام(ره) فرمودند سیلی آخر را به دشمن بزنید.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450519" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450518">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
حملۀ هوایی دشمن آمریکایی به بوشهر
🔹
حوالی ساعت ۱ بامداد، بوشهر هدف حملات هوایی دشمن قرار گرفت.
🔹
هنوز محل دقیق اصابت‌ها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/450518" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450517">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
منابع عراقی:
یک پهپاد ایرانی، سکوی پرتاب موشک‌های آمریکایی را در اربیل هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/450517" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450516">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به انشعاب راه‌آهن بندرعباس
🔹
استانداری هرمزگان: حوالی ساعت ۲۴ ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی مورد هدف قرار گرفته است که متأسفانه در این حادثه ۲ نفر از هموطنانمان مصدوم و به مراکز درمانی اعزام شده‌اند.
🔹
این ایستگاه در مجاورت مناطق مسکونی نبوده و خوشبختانه خسارت چندانی به تأسیسات زیربنایی وارد نشده است.
🔹
تیم‌های امدادی و آتش‌نشانی بلافاصله در محل حاضر شده و اقدامات لازم جهت مهار وضعیت در حال انجام است.
🔹
از مردم شریف استان هرمزگان درخواست میشود ضمن حفظ آرامش و خونسردی، از نزدیک شدن به محدوده ایستگاه راه آهن و ترددهای غیرضروری در این منطقه خودداری کنند تا نیروهای امدادی با سرعت بیشتری به وظایف خود عمل نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450516" target="_blank">📅 00:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450515">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9KnhMB6fN8ItUHnaktHB3QX9FJedctkZgg5k9F13_8ZpFes_cBOhPGOHbM7KXRoVfHr8T6TAlDXZL4ngl10Hfy4Sxj44EdR9gLqOVVGeRxP7GsNJVRUHF6HAHSKMHMgOgrqYqL_1etBysGeyl1jAh2f5lqDId4-s-q8OUnW_toH9dInpUh6H3P-_0li9vTFNZOYgGN2nwGNYunQNCg_1JQ6WYt3wT4cE8pp8z6W_vjxdJTGrGGcjtCT7ExlNshK8h6gafoI6qTRzz0qw3RHyzHTGeRFqTKqnTcHot6koyewPiscFQI6fMfgQWoyAjPh936v-JH_nD1SwpMWpfb75g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌های تأییدنشده وضعیت اضطراری جنگنده F35 بر فراز امارات
🔹
برخی گزارش‌های تاییدنشده حاکی است یک جنگنده چندمنظوره F-35A در حین پرواز بر فراز امارات متحده عربی وضعیت اضطراری اعلام کرد و کد فرستنده اضطراری بین‌المللی ۷۷۰۰ را فعال نمود.
🔹
این گزارش‌ها حاکی است این هواپیما در پایگاه هوایی الظفره در ابوظبی به زمین نشسته است.
🔹
کد
۷۷۰۰
یکی از سه کد اضطراری استاندارد و بین‌المللی در هوانوردی است که روی دستگاه
ترانسپوندر
(فرستنده خودکار هواپیما یا اصطلاحاً
Squawk
) تنظیم می‌شود.
🔹
وقتی خلبان این کد را وارد می‌کند، یک هشدار بصری و صوتی فوری روی صفحه رادار کنترلرهای ترافیک هوایی ظاهر می‌شود تا آن‌ها متوجه شوند که این هواپیما با یک
بحران جدی و آنی
مواجه است و به کمک نیاز دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/450515" target="_blank">📅 00:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450514">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
تهاجم دشمن آمریکایی به یک نقطه در اطراف شهر بستان
🔹
معاون استانداری خوزستان: دقایقی پیش یک نقطه در اطراف شهر بستان توسط دشمن آمریکایی مورد تهاجم قرار گرفت.
🔹
موضوع از سوی نهادهای مسئول در دست بررسی است و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450514" target="_blank">📅 00:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450513">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
معاون استانداری خوزستان:
انفجاری در شهرستان حمیدیه رخ نداده و صداهای شنیده شده در این منطقه مربوط به حوادث حوالی اهواز است که پیش‌تر اطلاع‌رسانی شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450513" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
حمله دشمن آمریکایی به پل بندرخمیر
🔹
حوالی ساعت ۲۳ امشب پل کهورستان در شهرستان بندرخمیر که پل ارتباطی میان بندرعباس به لار بود هدف حمله دشمن آمریکایی قرار گرفت.
🔹
عوامل راهداری درحال ایجاد راه جایگزین برای این مسیر ارتباطی هستند. @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450512" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450507">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivEFu96AK6UcP2UMMAe1LTzIKHMtpx263Nqw2ONyyyUXO_Wh0iiLHnwPwC7O9Btf3EixdfQnA03EYfA7IJhwIM_d6ZN59CuBdXULD9AkJuBWNGCfgD57uh6ub6MgBidW9tlelLfVYQy7yeN5cP1QnYyefA48EZayO_zmyPn5mgk1iEkAhDrK_DdTknZWnSnRAzXT960ad3CJuMRalUsXocyhOO5yCyXUwXX6H-3n-kZGsOi_FPHHkzUKQFV7oFVnxjHaSuuVbo9HMTRsn6SVDPJ0hi5Mot6k_eBjjpuxd95-FHt9-wNlDKicJyHLbn8X-pk60ohdTylGboYvdByZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bYSsxT4iQmSIL0ASBRBbEMxP-xe3XW8lcQVqjtvYxoU3ObEfUQ2M6SH-AlYqN4KOTM4O0JKcOjZa5Oz1mm-JG3rDFQ3S6bTE0W9OSrduxuqgVSv4vKPVyPEd9EF440bDZek2auc49xrP0ngwdFMOzVhaynBH0EZyPIKvyX9eykA8dsFm8q5Ttre0ivz_Vx6xuvQtZ2Ruri3TEcMCR-CRpBOlJwVhjI9dyuE5RAFbf8XH9GhTUh19SRtd949cZufoAPtOCoKYyWwAVezmFrS98YHSC5HOLAalwrcwBRfNVTVBiK-V0ejuesE_q9J2xoURCJgfLmDnMUQDP0mZPHVGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2HrBsBIRrZ6-qzDhVB9EbMOp76hMuX7nzK49DHAtkbAiZz6Mb--2r4kVusGiAZFm7h8WUxv-vgwbi13LDgbT7QItGqNL0szVUQFAq3HpCwZx6yn5vKbLSmwW8xrKXLMAoWYZAyx4gAwWBzUvzmNEHQxdFpBop4aqHQDGCHuAagUyyFhDVINLHWtt5lmzywbwbYC7yOZA8NJxJ_R9dd85GPXbYB0-mnbO__anSJa8ilmVALnWh0sWRj1H8fsmJmPFc3y20wtPcFzgmErt4gMCk1e2S3ExcJS8TCy6yD2LZsZFyd6sMDiaho5NVBtSZ-PmqGwdpTCv_nxCoTOtbroLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3vpwDEU7U2xE2bVH-wXVd9uukEvfGIFXQVCKFUYiXg5vOUTnSSJM54J7oP-Tr4Xb-ZR021Bkh1N0gDHdYSUWAIUVQ8DeZ4bBHB0HaLnIxbmpRQvypSU05I4VnnqSt5hSYNxs4yiZyqGnUa-LJagLlCh9LP3ut4hn7LSEKuBDMRf55GmZRbyOBy8uhNPc49GLFzx97nvyxWoevxtwQmaCqiSUEu4G-jKvMrcY-9wdHrGn0MzCbJAXo4qVF-pgyv-c4nm5qjBFcFvpmJ4DnCMQNs1ro1H37rbuf_AZ3G_glLfxauDc71PwNcb24omH4blL5b0-7Y8xUXkYPZAPPT2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5RokxL-jiGjhvOoCQvDV6qwLF9794iXap8GuVmRFbalxJS05s26nvyZaZcXOPxFOqqbZFmggBTkWgV6iwusiUEmayjl7FGKSlukCO_8awju20yNgzPSTkgMFlDKSExfvdO3NUoG6fH93c2lrK26vYQJhSx9z4ynjesXfKQN_WXQCj2ETxGRVFgBZPRCFeV3ZnuTQOCjTvwcYE95vcvVduJX2OxZ_95I6_DmNP8S2Knd_IZJYI3DDsLKg9FN9ZulSqtnpGdFQVhtNWIX2-gSyY4Yg-V7I7bpH161esdGqp-fS4Z34IdhEwtAQtu0CCsKQXwxacgYT5kVctG3Vg0tMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت رهبر شهید انقلاب اسلامی از سوی آیت‌الله مکارم شیرازی در حرم حضرت معصومه(ع)
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450507" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450506">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جایزهٔ ۱۰ میلیون دلاری مقاومت اسلامی عراق برای کُشتن ترامپ
🔹
مقاومت اسلامی عراق با محکوم کردن یاوه‌گویی‌های گستاخانهٔ رئیس‌جمهور آمریکا علیه فرماندهان شهید پیروزی علیه گروه تروریستی داعش، اعلام کرد که ۱۰ میلیون دلار برای کُشتن ترامپ اختصاص داده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/450506" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450505">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
اصابت موشک‌های دشمن آمریکایی در حوالی سیریک
🔹
استانداری هرمزگان: ساعت ۲۳:۳۴ نقاطی در حوالی سیریک مورد اصابت موشک‌های آمریکایی قرار گرفت.
🔹
گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/450505" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450504">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌ مجروح‌شدن ۷ نفر در حمله دشمن آمریکایی به بندرعباس
🔹
استانداری هرمزگان: درپی حمله دقایق پیش نیروهای متجاوز آمریکایی به محله مسکونی تپه‌الله اکبر در شهر بندرعباس، تاکنون ۷ نفر از هموطنان مجروح شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450504" target="_blank">📅 00:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450503">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
رسانه‌های عراقی از شنیده شدن صدای انفجارهای بسیار قوی در کویت و شنیده‌شدن آن از بصره خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450503" target="_blank">📅 00:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حملهٔ موشکی دشمن به حوالی ایرانشهر
🔹
دقایقی پیش موشک‌های دشمن آمریکایی به حوالی ایرانشهر اصابت کرد.
🔹
اخبار اولیه از اصابت موشک‌ها به حوالی فرودگاه ایرانشهر حکایت دارد.
🔹
هنوز مسئولان دربارهٔ این حمله اظهارنظری نکرده‌اند و گزارشی مبنی بر شهادت و مجروحیت بر اثر این حمله مخابره نشده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450502" target="_blank">📅 23:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450501">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9a9831c0.mp4?token=KPlQEqXhRZYwPMb91Br4Fap0crAzi2AZHixTywjBemCir8k3HLgy72qBshyWIOvcOhGa1M9F89I_hgrpgXl1hcQxfsDFeH1aBAx9K1_QgBr3aq3XvVaST-sDVWZqc2czvOCS2k_fYzHhivcESQ8Trj5Ms2PWngG_iwFUXAB4-KtkoFI6OtMPsTHIMb3wl5efNxgCGJIuT4im44MW0nHrUKmhBeTvk5MdP1usZiaEOvSwFp0ImKpPpTTL3vNCe3aXcrOEreQEj4Py7B0dLDbhTFpK-QEbZ6I6xFP3azDercePhsa4bEzf8Gudw8h2PSNhbNUKmngWei8upzoyUQLcglRyTXUNqW6DwQL5TRrBhugFEXF0BTaxL2LyzJL4eWuk2Dm-ltQUHF98ICkxDkdaBdpmFW4bjwSzHDf5TeIb4UbmPlPaPDGBZVn6_AIO9pRs6T-CXqNbFqRrQsMJRSm_TbOSLd6PJFfwc8i6ilHKctIjsc_sgAeZJu1AsQNWNZM6E0ly23Tb3eTYsGF2npGIdzf9HfZo6m2uZHcDhwUD_ZshriWxAdd_euUb9F342Y738OEvF2gEaR9EBCE4X-55gEPGLoJAvSaacXsjCqwvvC9Jp8dCpRw65Rc7GR5VssKzWwxM2QOSVNqzaPqXwnSGbry4skAVxDrFI-ihXi_Pxok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9a9831c0.mp4?token=KPlQEqXhRZYwPMb91Br4Fap0crAzi2AZHixTywjBemCir8k3HLgy72qBshyWIOvcOhGa1M9F89I_hgrpgXl1hcQxfsDFeH1aBAx9K1_QgBr3aq3XvVaST-sDVWZqc2czvOCS2k_fYzHhivcESQ8Trj5Ms2PWngG_iwFUXAB4-KtkoFI6OtMPsTHIMb3wl5efNxgCGJIuT4im44MW0nHrUKmhBeTvk5MdP1usZiaEOvSwFp0ImKpPpTTL3vNCe3aXcrOEreQEj4Py7B0dLDbhTFpK-QEbZ6I6xFP3azDercePhsa4bEzf8Gudw8h2PSNhbNUKmngWei8upzoyUQLcglRyTXUNqW6DwQL5TRrBhugFEXF0BTaxL2LyzJL4eWuk2Dm-ltQUHF98ICkxDkdaBdpmFW4bjwSzHDf5TeIb4UbmPlPaPDGBZVn6_AIO9pRs6T-CXqNbFqRrQsMJRSm_TbOSLd6PJFfwc8i6ilHKctIjsc_sgAeZJu1AsQNWNZM6E0ly23Tb3eTYsGF2npGIdzf9HfZo6m2uZHcDhwUD_ZshriWxAdd_euUb9F342Y738OEvF2gEaR9EBCE4X-55gEPGLoJAvSaacXsjCqwvvC9Jp8dCpRw65Rc7GR5VssKzWwxM2QOSVNqzaPqXwnSGbry4skAVxDrFI-ihXi_Pxok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی مردم قم به شب ۱۳۸ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450501" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450500">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8b1a9f5a.mp4?token=b2oa90uPU_FTBcAqxeQ0vCFYDtbbO7E8xChEDSgvampuMoKOwF8os-m9_32TZUPvqv60o3-Lr5EznDSaxESAkLpAY092EJUb5NYrEYlAEVIFmsXCTGoBiAgQPNBEqgEk-AV24K4dqZ63zeeTkxp67-TlGFLvigQ_V86dx4B3hh42rLAChJICUzAOJ4uRwyPtIN_UdG6TTZsiGtPtVPhDjQFHjJ9fpXcfZyalsm5iBs_FiiXCe0BScqSiGGva6HJjVgkHbMD3psf5It2CaOYVX0xnuhsFlOEDo69xZ_Yekgkne_hO5E7DcjT6TuAPCcXQOURaQBom2J5qNqVa85YYVwyUgQ-LVR7O6jviQbQg9YfVbTvJWpBaMvqbeq6eIUAes-xF4MPkqejFVT9AuGdrodhqoOemlA26cy3BarPj_xv4q__7SShLD1n0gUfeAXC4SYsWnPTfjgX-ncRWqxPETMbyDS5GmyfIYk0kZxCQ4GDQiowxPwLOuF3dyaKnHrr8uJkZDSAU5IZCbfKa7Wm4eaNLd_jC0c0o7xciHQfUxwi0WjDQIKnFf_Q9xM2DYmlBBbR85vYjb1rlWFn7G4Ku33RilgFOs-vIYWNzC2D8pqBKZLY_uzjfD1E6GNtrqhQWPYM3pSKsGV9ypZuLobi6ZMiDc3Qm1vQKJzXZrHyUFZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8b1a9f5a.mp4?token=b2oa90uPU_FTBcAqxeQ0vCFYDtbbO7E8xChEDSgvampuMoKOwF8os-m9_32TZUPvqv60o3-Lr5EznDSaxESAkLpAY092EJUb5NYrEYlAEVIFmsXCTGoBiAgQPNBEqgEk-AV24K4dqZ63zeeTkxp67-TlGFLvigQ_V86dx4B3hh42rLAChJICUzAOJ4uRwyPtIN_UdG6TTZsiGtPtVPhDjQFHjJ9fpXcfZyalsm5iBs_FiiXCe0BScqSiGGva6HJjVgkHbMD3psf5It2CaOYVX0xnuhsFlOEDo69xZ_Yekgkne_hO5E7DcjT6TuAPCcXQOURaQBom2J5qNqVa85YYVwyUgQ-LVR7O6jviQbQg9YfVbTvJWpBaMvqbeq6eIUAes-xF4MPkqejFVT9AuGdrodhqoOemlA26cy3BarPj_xv4q__7SShLD1n0gUfeAXC4SYsWnPTfjgX-ncRWqxPETMbyDS5GmyfIYk0kZxCQ4GDQiowxPwLOuF3dyaKnHrr8uJkZDSAU5IZCbfKa7Wm4eaNLd_jC0c0o7xciHQfUxwi0WjDQIKnFf_Q9xM2DYmlBBbR85vYjb1rlWFn7G4Ku33RilgFOs-vIYWNzC2D8pqBKZLY_uzjfD1E6GNtrqhQWPYM3pSKsGV9ypZuLobi6ZMiDc3Qm1vQKJzXZrHyUFZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنگر خیابان در کاشمر برای ۱۳۸ شب متوالی خاموش نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450500" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450499">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48fd0a2fa9.mp4?token=aivDsJv7o5SebuwCrxH5-t6xSClzScQLcGMzTC4RDwTRO0uN3gpHu8uMq-kAEJ6PBGsOyJuGw6m5UXAS3y-PUaXt3h2MArtYxhQtmvV12_jhgw1IVfHNbYo5wXBkVkZe8oW9_utVHPG-cp5UYf-7pSQUtNFJlIbWs35Uy2YpGg_A7Pc9HXwRFkJn9Y2mzqRRUqkb9hYaJGdurqgj7odCh2Tv3jxUkXsycUfdXo-576WtgOsN6kCfYZTCk0FkWY1U_j5WloWDK07zOsV3ddsCi6hks3R-1ckKKi5HRVX3EgCb9dWXGhBtfvzeU-BWImVuqWD0UmHGP-VExg45hrz5MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48fd0a2fa9.mp4?token=aivDsJv7o5SebuwCrxH5-t6xSClzScQLcGMzTC4RDwTRO0uN3gpHu8uMq-kAEJ6PBGsOyJuGw6m5UXAS3y-PUaXt3h2MArtYxhQtmvV12_jhgw1IVfHNbYo5wXBkVkZe8oW9_utVHPG-cp5UYf-7pSQUtNFJlIbWs35Uy2YpGg_A7Pc9HXwRFkJn9Y2mzqRRUqkb9hYaJGdurqgj7odCh2Tv3jxUkXsycUfdXo-576WtgOsN6kCfYZTCk0FkWY1U_j5WloWDK07zOsV3ddsCi6hks3R-1ckKKi5HRVX3EgCb9dWXGhBtfvzeU-BWImVuqWD0UmHGP-VExg45hrz5MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تولد ماکان نصیری در بیمارستان شهدای لردگان چهارمحال‌وبختیاری
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450499" target="_blank">📅 23:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450498">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBlTkIeg3u_EAiSoYrMDMPcZKBO624GRH8o3rUBO20vFMHgyTlsoJlnpM8NRoMILs6bVw4vvy5ORb5UUH51ugMAXKGe0-lVF9RMclLwJ-5WNC97fPfVqJIAZ_XoD42iAHYYwgiLrE-PAtozB7zOjj9qwMto703YEsGHGhvbhw6WmCN_Qp6lOGxSfpscwP7-G3kby7mihKpRjvmZWs9ykl_EqP3zFcWHnG5HiNBzM5W0htIbKNB5ZXpI_gnPJNYMaSs_r6rthH7529IdmQEphF3KqDnYtXauze7heGwhXkqv6eSgYqunPue8IZgUa7DGPnEeXU1PnW3O7LKqW-KHyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور سردار قاآنی، در یادبود رهبر شهید انقلاب در امام‌زاده علی‌اکبر(ع) چیذر
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450498" target="_blank">📅 23:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450497">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
حمله دشمن آمریکایی به پل بندرخمیر
🔹
حوالی ساعت ۲۳ امشب پل کهورستان در شهرستان بندرخمیر که پل ارتباطی میان بندرعباس به لار بود هدف حمله دشمن آمریکایی قرار گرفت.
🔹
عوامل راهداری درحال ایجاد راه جایگزین برای این مسیر ارتباطی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450497" target="_blank">📅 23:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450496">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538444c44a.mp4?token=cC0Smbgd7pgXNZ91FRU34dzB17guKb9qDcFHwLulUD477RclnEkJJpbpr1pWHUEtfuEjEER-1Pmeqfq-lR8BKguySbVjgxxfBsAez6FxJPKYcS9HjOfcgPV6U8UxRM7sIF1TvcryF-w7rHCAvuMu69QrTVBopqB77BajHCy6S0ZIJ_ySW-udN84nqXabnyiinHvW10vJjqWBT8-4pxRoFxFNQ1e5YJ-iEeF2iecOzZSf1htH0UvHCkWAe14mE31SP1ydA-Hlyg_sibtS_6mYnygXbUwFa4gE8TL4dqLHqKI9MsCNcJg1PJsqvUD_ka0eqb9UCgjcaSNXN5VfB6M-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538444c44a.mp4?token=cC0Smbgd7pgXNZ91FRU34dzB17guKb9qDcFHwLulUD477RclnEkJJpbpr1pWHUEtfuEjEER-1Pmeqfq-lR8BKguySbVjgxxfBsAez6FxJPKYcS9HjOfcgPV6U8UxRM7sIF1TvcryF-w7rHCAvuMu69QrTVBopqB77BajHCy6S0ZIJ_ySW-udN84nqXabnyiinHvW10vJjqWBT8-4pxRoFxFNQ1e5YJ-iEeF2iecOzZSf1htH0UvHCkWAe14mE31SP1ydA-Hlyg_sibtS_6mYnygXbUwFa4gE8TL4dqLHqKI9MsCNcJg1PJsqvUD_ka0eqb9UCgjcaSNXN5VfB6M-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اطلاعاتی از محل‌های حضور رئیس‌جمهور تروریست آمریکا
🔹
در این مکان‌ها دسترسی به ترامپ امکان‌پذیر است.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450496" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450495">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5037abc23.mp4?token=Pd6yomA4bC8p4glAYdRgOv4VaP_jxPucJGJW0P_j3z3xXqW_ieeJB2pS8JVTB_bWT6UJekE-CwPjjP7c9vW4d9ud5YBjrOowj4ZohqwsHgMO5QFyOxKoVCM4iru0wcO2GLLLKWx3xHxJgSGPUM4Z2_WRwz-snaJFYF7uYNGb-G-qdrQ31QGlTv_aXP8ezUOVuB0ZidYIF_EOglMTvbXJkEjEkSzM2FddysCsxfvjyCYZMef1qbpUUHsafg_vY2MNt4FeK4JYy2qyxEuZEFuihCZoa9jkxMCzaulu5HVK68sqKrIkK0aR8ufKVSd7EOYb8-k9keE-t0Fv9wRCZXCYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5037abc23.mp4?token=Pd6yomA4bC8p4glAYdRgOv4VaP_jxPucJGJW0P_j3z3xXqW_ieeJB2pS8JVTB_bWT6UJekE-CwPjjP7c9vW4d9ud5YBjrOowj4ZohqwsHgMO5QFyOxKoVCM4iru0wcO2GLLLKWx3xHxJgSGPUM4Z2_WRwz-snaJFYF7uYNGb-G-qdrQ31QGlTv_aXP8ezUOVuB0ZidYIF_EOglMTvbXJkEjEkSzM2FddysCsxfvjyCYZMef1qbpUUHsafg_vY2MNt4FeK4JYy2qyxEuZEFuihCZoa9jkxMCzaulu5HVK68sqKrIkK0aR8ufKVSd7EOYb8-k9keE-t0Fv9wRCZXCYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران به ۱۳۸ شب ایستادگی رسید
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450495" target="_blank">📅 23:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450494">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgXgcFmijam9_MXkoZgIaOTJNmZSsY--0PZoGCdtrLcAVZrl5Vv8TijpJlk14HIFVXVTcB1qDLzHFvOBvlV0hfD6MLCzR7v73tulekYPWTFDPlK0gBmn_c0YM_6TpWjNIULYBPTMYhZG3lyoQhxpz1f6Au8_zovtJxlAJQNH1mIItzaIdDgfZEik-tRPOIegXs9befU4HidGNk7T5u4Q-_LQlk_aXxWTeBqFvDm65R42M4g_VTDjxtaYJIthUiSrXACHpY-7cChyH-50WKDISAP2GYhQRWbVilOJPUUhC2KhhaTwM6P7Y5ozbYTue3NPOzXHPvcZ6uuZexSZj6Teig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ما ترامپ را می‌کشیم
🔹
طرح جدید دیوارنگارهٔ میدان انقلاب تهران با تصویری از ترامپ در داخل تابوت  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/450494" target="_blank">📅 23:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450493">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2edea5ea02.mp4?token=sSmodUxFgQmLgGJ00U50b3uL9ayYHI9v5h6Uj6R8Vai5YY55PGvc7e3U64DwDAjX4ui1NPa8MMcJTKeL6rB4tzVHCWF0K680phabKZ2MfTUCBbcqqWOLkIftHF_kU_TsrI992CMygz0ZOenvsFIVoJED1F7l5ejmb2M5cbtEZd6Xl5btKuelZ0Qlh186GvItQCYan6s_Em7uilyV8Pj0Pi_DM3HQ3Au0mkcZ7QxVRKbIisx3zwoVIchGMyp7Lfikfd5C7yswiDqffTqyzyiXtlMZsP76FfFcCJYb6dduazoTnnIWZr6fURuLkuS0_O8VwJHYWFpMMq-WpBCvIYGuCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2edea5ea02.mp4?token=sSmodUxFgQmLgGJ00U50b3uL9ayYHI9v5h6Uj6R8Vai5YY55PGvc7e3U64DwDAjX4ui1NPa8MMcJTKeL6rB4tzVHCWF0K680phabKZ2MfTUCBbcqqWOLkIftHF_kU_TsrI992CMygz0ZOenvsFIVoJED1F7l5ejmb2M5cbtEZd6Xl5btKuelZ0Qlh186GvItQCYan6s_Em7uilyV8Pj0Pi_DM3HQ3Au0mkcZ7QxVRKbIisx3zwoVIchGMyp7Lfikfd5C7yswiDqffTqyzyiXtlMZsP76FfFcCJYb6dduazoTnnIWZr6fURuLkuS0_O8VwJHYWFpMMq-WpBCvIYGuCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسداللهی، کارشناس غرب آسیا: اگر انتقام خون رهبر شهید گرفته نشود، خواسته یا ناخواسته شرایط برای حملات بعدی دشمن آماده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450493" target="_blank">📅 23:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450492">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991331afe5.mp4?token=lfaVNSpGyI2D4Iefr_pjFFd1u26dbRaQYbyMrt-4hX7YPQLmXpF90EV5kEb55JgBwAj3szGDu4fwcqWRphJu4qU7lUjh0VYG7qVTmC9qrU4CwwSMWiTk_nysdi4A1m4QdrxNlbfQohpn3TXVwB0_Ovgk9aKqzplvktu_V2pyDObLKUOIjhbV5-qjja_NQDcYvSe7KIIVE6naRSiQ55e4L2ddeRsmZTtqSXWsXea_kVG2NN217X8zEX8m7fngd4La-cBDmlGd5_CVfb9xHP3igs3UKoLuT_37aFRo5I0xORTQkLNO3l2RPNXyQ26PA6KET7vMxszCuA5YHiepg3ZRuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991331afe5.mp4?token=lfaVNSpGyI2D4Iefr_pjFFd1u26dbRaQYbyMrt-4hX7YPQLmXpF90EV5kEb55JgBwAj3szGDu4fwcqWRphJu4qU7lUjh0VYG7qVTmC9qrU4CwwSMWiTk_nysdi4A1m4QdrxNlbfQohpn3TXVwB0_Ovgk9aKqzplvktu_V2pyDObLKUOIjhbV5-qjja_NQDcYvSe7KIIVE6naRSiQ55e4L2ddeRsmZTtqSXWsXea_kVG2NN217X8zEX8m7fngd4La-cBDmlGd5_CVfb9xHP3igs3UKoLuT_37aFRo5I0xORTQkLNO3l2RPNXyQ26PA6KET7vMxszCuA5YHiepg3ZRuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سخنگوی ارشد نیروهای مسلح: براساس تدابیر رهبر انقلاب و تصمیمات شورای‌عالی امنیت ملی، نیروهای مسلح تا ابد از مدیریت ایران در تنگهٔ هرمز دست نخواهند کشید.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450492" target="_blank">📅 23:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450491">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در قشم به گوش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450491" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450490">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b09a4689.mp4?token=rL43JJ8YG9WtotJq55l1aj2sf5xOIh5clao2ARfszTOGyCQTt7jKlR2JpmpTzOTkKzEAkT9ZHzGXA5Q2KG_AG2M72OJ0T4A-nevr4Sja4y8PVZzzhlNy0NsPoMzSE-nXiVCLrfStCfaGRTVSm4BO20wp18yHDVcQQIGqlua5I9PQhqMtyNqaCQg2mLmVQF1NXn_4cOI--S2lJ2puO-pmT4YD4F2zNFIGWltvN0Nwj_nc22TtVUePIYcj8z32VxDd_EwqJZdBZth8-beonqbNYmILSwsUPA_C5gOsFuH3GmuJfKcaUQMokhN3phJFRPc_eHGW_fEDa9ihYsVdmlrV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b09a4689.mp4?token=rL43JJ8YG9WtotJq55l1aj2sf5xOIh5clao2ARfszTOGyCQTt7jKlR2JpmpTzOTkKzEAkT9ZHzGXA5Q2KG_AG2M72OJ0T4A-nevr4Sja4y8PVZzzhlNy0NsPoMzSE-nXiVCLrfStCfaGRTVSm4BO20wp18yHDVcQQIGqlua5I9PQhqMtyNqaCQg2mLmVQF1NXn_4cOI--S2lJ2puO-pmT4YD4F2zNFIGWltvN0Nwj_nc22TtVUePIYcj8z32VxDd_EwqJZdBZth8-beonqbNYmILSwsUPA_C5gOsFuH3GmuJfKcaUQMokhN3phJFRPc_eHGW_fEDa9ihYsVdmlrV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام میرهاشم حسینی: ترامپ نفت و ثروت ایران را می‌خواهد
🔹
امیدوارم به‌زودی خبر مرگ ترامپ را بشنویم.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450490" target="_blank">📅 23:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450489">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
اصابت مجدد موشک‌های دشمن در بندرعباس
🔹
استانداری هرمزگان: در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت موشک‌های آمریکایی قرار گرفت.
📝
گزارش تکمیل پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450489" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450487">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فرماندار بوشهر: در ادامه تجاوز دشمن آمریکایی، دقایقی پیش در شهر بوشهر صدای ۲ انفجار شنیده شد
🔹
براساس اطلاعات اولیه، تاکنون هیچ‌گونه مجروح یا شهید گزارش نشده و ابعاد مختلف این حادثه از سوی مراجع ذی‌ربط در دست بررسی است.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/450487" target="_blank">📅 23:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450486">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">اعلام زمان مسابقه پلی‌آف لیگ برتر
🔴
با اعلام سازمان لیگ، دیدار مس رفسنجان و صنعت نفت آبادان برای تعیین هجدهمین تیم لیگ برتر، ساعت ۱۸:۴۵ روز چهارشنبه ۳۱ تیر در ورزشگاه شهر قدس برگزار می‌شود.
@Sportfars</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450486" target="_blank">📅 23:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450485">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ac037364.mp4?token=fqaFI4DtJ_bUJPyt8P2HGnogKne86DjuKovBk43MDceCMuSZwrYrMdqNStj9mfAq2NYsWG2cxTCqrXTuysv9gjoB0eA4UBhkTg5X_-_mDJvzoH7pTdgjrV4qSjJhjCBRX6GKEgDSn36XFWGQQ5TSNxp_3xGAKEOD5Ikl4qCPf0IqcXia9WSAlTbTqN-u2n9JQUtfLanSGjYA0JNVEw8E-3s3rUAtyu8gmiFE50ocFRjd-CqQdwh5KTN42WpnOvWTo-AsSjf6Whq25duow_N--7eEy9h5q7KRNtn-LKnBAhc1CD4Iw5KBUY8vk5Mpeq-XsSbj_3-cUPbLjBnJhnN6Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ac037364.mp4?token=fqaFI4DtJ_bUJPyt8P2HGnogKne86DjuKovBk43MDceCMuSZwrYrMdqNStj9mfAq2NYsWG2cxTCqrXTuysv9gjoB0eA4UBhkTg5X_-_mDJvzoH7pTdgjrV4qSjJhjCBRX6GKEgDSn36XFWGQQ5TSNxp_3xGAKEOD5Ikl4qCPf0IqcXia9WSAlTbTqN-u2n9JQUtfLanSGjYA0JNVEw8E-3s3rUAtyu8gmiFE50ocFRjd-CqQdwh5KTN42WpnOvWTo-AsSjf6Whq25duow_N--7eEy9h5q7KRNtn-LKnBAhc1CD4Iw5KBUY8vk5Mpeq-XsSbj_3-cUPbLjBnJhnN6Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌
🔴
سخنگوی ارشد نیروهای مسلح: اگر آمریکایی‌ها در منطقه نباشند، قطعا تنگهٔ هرمز مسدود نخواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/450485" target="_blank">📅 23:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450484">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: تنگهٔ هرمز منطقهٔ سرزمینی ایران و عمان است
🔹
آمریکایی‌ها باید جواب بدهند که چه‌کاره‌ هستند و در خلیج‌فارس و تنگهٔ هرمز چه می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450484" target="_blank">📅 22:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450483">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
سخنگوی ارشد نیروهای مسلح: هرگز به آمریکایی‌ها اجازه دخالت در تنگه هرمز را نمی‌دهیم
🔹
مسیری که ایران در تنگه هرمز تعیین کرده ایمن است و هر مسیری خارج از آن ناامن خواهد بود و کشتی‌ها در آن آسیب می‌بینند. @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450483" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450482">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24e4dd2af1.mp4?token=RAHOIRTl99R93W5_D1ChrwNBiiJfAnSv2zTwR7QkyhIHG5CWfofH46aw5Lmw8SYH1HecHaWzYP5eFHjSeVF2d0XCfGc81wgxdi8YC2obpBRL6xfoflPCuBu6VTq6fnd1Qb5BpO2reW3SHZjs0fElpvpdvYyMIPHkx7AFVM1WVBbhbQcRMXEEYEESjBlCua3hN21ATyphOdf97_bd6h-2EhRzFCspdGYNKBRm57_j2IECOt6oQvF-BTrzy6aFUv7CtZevX2wFtUKwSOZeN83UPs7P3UbkPXljZPqkKu2oJY58TshMFaZ1xM6nAhJ8t2w7Xy8iLOJBf68Z1635Aa05sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24e4dd2af1.mp4?token=RAHOIRTl99R93W5_D1ChrwNBiiJfAnSv2zTwR7QkyhIHG5CWfofH46aw5Lmw8SYH1HecHaWzYP5eFHjSeVF2d0XCfGc81wgxdi8YC2obpBRL6xfoflPCuBu6VTq6fnd1Qb5BpO2reW3SHZjs0fElpvpdvYyMIPHkx7AFVM1WVBbhbQcRMXEEYEESjBlCua3hN21ATyphOdf97_bd6h-2EhRzFCspdGYNKBRm57_j2IECOt6oQvF-BTrzy6aFUv7CtZevX2wFtUKwSOZeN83UPs7P3UbkPXljZPqkKu2oJY58TshMFaZ1xM6nAhJ8t2w7Xy8iLOJBf68Z1635Aa05sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: آمریکایی‌ها گرفتار شده‌اند و راه نجاتشان خروج از غرب آسیاست؛ زمان قُلدری و یاغی‌گری آمریکا به پایان رسیده است. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450482" target="_blank">📅 22:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450481">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: آمریکا و دولت جعلی صهیونیستی حق ندارند در منطقه باشند
🔹
تنها راه عبور در منطقه تنگه هرمز است. سال‌هاست آن‌ها کشورهای منطقه را غارت می‌کنند و عامل ناامنی هستند.
🔹
حاکمیت جمهوری اسلامی بر تنگه هرمز عامل امنیت بر کل منطقه است نه…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450481" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450480">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در اهواز
🔹
معاون امنیتی و انتظامی استانداری خوزستان: دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن آمریکایی مورد تهاجم قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450480" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450479">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfs1GJ8XJspXg2o2fCqPbJjkpD53BA81dSOCICo4tysPWzihjfu_rVEM-IN_A74z3FHEFrRh7rX2bzb1cTxVTBX9g0_iRXhJIPlzMw97H6yJIm-Dd99nxvZuMwv6_-FFrL1NMRFHA-OlJBnA_0g93u-CCPqEtuynOb2N6gWjl_C0qdZVmRCnE1p5vpAiIzZ_L8yBf1v0gSoWVlFpwDQ5eMch1OdXeCSTmuVIEeodVG-yNZ5N9SAONXnMzQwgyGrAi_CE9Z-PEQyllx_-HShTbYIAVs3yPoJGrkjK-1aCpxyv4bt1rIvMIhM_Mc1B-J59LkEUAvCM-ONpG1UvX1uPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غافلگیری آمریکا از شدت و ماهیت حملات دفاعی ایران
🔹
تهران‌تایمز نوشت: آمریکا که طی هفتهٔ گذشته با واکنش شدید ایران در هدف‌قراردادن پایگاه‌های نظامی و تأسیسات پشتیبانی خود در کشورهای منطقه مواجه شده، از طریق میانجی‌ها از ایران خواسته که حملات تلافی‌جویانه خود را متوقف کند.
🔹
روز دوشنبه، کمتر از ۲ ساعت پس از اظهارات ترامپ در مورد ایران، دولت آمریکا از طریق یک کشور شرق آسیا پیامی را ارسال کرد که در آن از ایران خواسته شده بود از حمله به پایگاه‌های نظامی آمریکا در کشورهای خلیج‌فارس خودداری کند.
🔹
به‌گفتهٔ ۲ منبع نزدیک به فرمانده فرماندهی سازمان تروریستی سنتکام، آمریکا پیش‌بینی نمی‌کرد که ایران با چنین سرعت، دقت و قدرتی پاسخ دهد.
🔹
یکی از دستیاران ارشد فرمانده سنتکام به یک مقام ارشد نظامی اماراتی گفته که فرمانده سنتکام در طول هفته گذشته ۳ بار قصد خود را برای استعفا به مشاوران نزدیکش ابراز کرده بود، اما درنهایت به‌دلیل نگرانی از واکنش غیرمتعارف وزیر جنگ آمریکا از این کار منصرف شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450479" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450478">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: ما می‌توانیم سال‌ها با دشمن بجنگیم
🔹
قدرت ما در جنگ رمضان نسبت به جنگ ۱۲ روزه چند برابر شد و همچنان درحال افزایش قدرت خود هستیم. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/450478" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450477">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: از زمان اعلام آتش‌بس، جنگنده‌های آمریکا حتی یک روز هم تنگه هرمز را ترک نکرده‌اند. این حضور مداوم، اعلام جنگ است. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450477" target="_blank">📅 22:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450476">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: ما بر خروج آمریکا از منطقه تاکید داریم و تا ابد از تنگه هرمز کوتاه نمی‌آییم.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450476" target="_blank">📅 22:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450475">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: اگر به زیرساخت‌های ما آسیبی برسد همهٔ زیرساخت‌های منطقه هدف ماست. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450475" target="_blank">📅 22:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450474">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
سخنگوی ارشد نیروهای مسلح: دکترین جمهوری اسلامی این است که به دشمن هجوم خواهیم کرد، باقدرت
🔹
اگر می‌توانستند ما را از بین ببرند، ساعتی صبر نمی‌کردند. بعد از الطاف خداوند ما قدرت مهمی به نام مردم داریم که دشمنان این را می‌بینند.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450474" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450473">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
سخنگوی ارشد نیروهای مسلح: امنیت کامل تنگهٔ هرمز هنگامی برقرار می‌شود که آمریکایی‌ها نباشند.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450473" target="_blank">📅 22:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450472">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
سخنگوی ارشد نیروهای مسلح: امنیت کامل تنگهٔ هرمز هنگامی برقرار می‌شود که آمریکایی‌ها نباشند
.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450472" target="_blank">📅 22:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450471">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae263e6bef.mp4?token=nDaYmBM85pif-3g9fs7HBiB2qotbUiFvtN_CI_mxOYt02wevsqJrM-gVrsFgzqzOU_yEaCucanV922YBoJju7h7ZNhInWmFx6ZNMZyrNq_srb5F9L4rB1yy0okEHfI3k7bWYlUMkAanH5Ktmmkql77BZqOvqgJBvgaFAnQHpRtN1xT-vV9vVfJTR41hRLqK-_c6w6zpxT1O1vIQXpWqH-93hf4Gp8a0LvO5XH5SmidwXUD8qQmtm84EF6md5tLme9XuklxKq71Jq72QvpSdCp-apJrxEBCmInDn9DJGHb6vrMTWuXebq0rAxRJcbpboktqu59LScoaXvFWaZstkm6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae263e6bef.mp4?token=nDaYmBM85pif-3g9fs7HBiB2qotbUiFvtN_CI_mxOYt02wevsqJrM-gVrsFgzqzOU_yEaCucanV922YBoJju7h7ZNhInWmFx6ZNMZyrNq_srb5F9L4rB1yy0okEHfI3k7bWYlUMkAanH5Ktmmkql77BZqOvqgJBvgaFAnQHpRtN1xT-vV9vVfJTR41hRLqK-_c6w6zpxT1O1vIQXpWqH-93hf4Gp8a0LvO5XH5SmidwXUD8qQmtm84EF6md5tLme9XuklxKq71Jq72QvpSdCp-apJrxEBCmInDn9DJGHb6vrMTWuXebq0rAxRJcbpboktqu59LScoaXvFWaZstkm6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات حادثهٔ اتوبوس فراری در خیابان ولیعصر(عج)
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450471" target="_blank">📅 22:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450470">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قوه‌قضائیه: هیچ زندانی آمریکایی از زندان‌های ایران آزاد یا تبادل نشده است
🔹
بامداد امروز دونالد ترامپ در مطلبی از آزادی یک زندانی آمریکایی که به گفته او در زمان دولت بایدن و در سال ۲۰۲۴ بازداشت شده بود خبر داد.
🔹
ترامپ در حالی این ادعا را مطرح کرده است که…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450470" target="_blank">📅 22:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450469">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قوه‌قضائیه: هیچ زندانی آمریکایی از زندان‌های ایران آزاد یا تبادل نشده است
🔹
بامداد امروز دونالد ترامپ در مطلبی از آزادی یک زندانی آمریکایی که به گفته او در زمان دولت بایدن و در سال ۲۰۲۴ بازداشت شده بود خبر داد.
🔹
ترامپ در حالی این ادعا را مطرح کرده است که با توجه به بررسی‌های صورت گرفته هیچ زندانی محکوم و یا جاسوس آمریکایی با مشخصاتی که ترامپ اعلام کرده و یا با هر مشخصات دیگری از زندان‌های ایران آزاد و یا تبادل نشده است.
🔸
البته سابقه توهمات ترامپ در اعلام این‌گونه اخبار فقط به این مورد برنمی‌گردد، او پیشتر هم در مواردی از جمله اعلام خبر اعدام قریب‌الوقوع ۸ زن زندانی در پی کودتای دی ۱۴۰۴، اعدام یک پسر جوان در کرج و … دروغ گفته بود.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450469" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450468">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سنتکام: دور جدید حملات به ایران آغاز شده است
🔹
فرماندهی مرکزی آمریکا با انتشار پیامی در شبکهٔ اجتماعی ایکس نوشت: ساعت ۲ بعدازظهر امروز به وقت شرق آمریکا (۹:۳۰ به وقت ایران)، نیروهای آمریکایی برای پنجمین شب متوالی موج جدیدی از حملات علیه ایران را آغاز کردند تا قابلیت‌های نظامی ایران را بیش از پیش تضعیف کنند.
🔹
این حملات در حالی آغاز شده است که نیروهای مسلح ایران در روزهای اخیر در پاسخ به از سرگیری تجاوز نظامی علیه کشور، چندین پایگاه و تأسیسات مرتبط با آمریکا در منطقه را هدف قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450468" target="_blank">📅 22:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450467">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
استانداری هرمزگان: در ساعت ۱۸:۲۰ و ۱۸:۴۰ نقاطی در حوالی بندر عباس مورد اصابت موشک‌های دشمن آمریکایی قرار گرفت.
🔸
بنابر اعلام استانداری هرمزگان، در حملات جدید آمریکا به استان هیچ مصدوم و یا خسارت به زیر ساخت های مسکونی و تجاری گزارش نشده است. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450467" target="_blank">📅 22:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450466">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65ca8369d.mp4?token=QnVZe4dtGHSLnktexMJJoVuJFtig_afbtEVVKi3i4kT05ZM9VhppRAne9cqSObG6RUmJ29eRC0POH5b_fsQED1CWfD2PNfjbqR5JSMQ2Prfb7ig3jeVkgzYRHiF09oxCzZ8W2RMiakVcEtUbedH71tMWXlUlLusz2_Y8omYG7VNkb3SbP9tRwhr7_8heAYT3OvxPIeNFWMcCuojanysAAkwUTpVoGqTJJPqX-drwWtYuep0uRUzWsqZI5Uqblyyjmac3Th5HsJqZJJ-m9S1x4d0TfYocTs4ktGjJwLb2C6xLeqKbj2HZCv-qpE_K3GRRAu81J8ORzDvN3WpZrjPUJgo0UAjStd3QSnaFXrmc4qUYyXdDIbESrqGZBf-pWxMo66VioirzoE89U25JLo7P-1SPrIaQ3Rb5VZE6zupFjqGW89ht0BCAAqg-nUIot1TrR0K1dIw7LQUDs_0BAvhcgUsGAmlWWAnG_zddvVOxA42wfKTYUWazNbkBVsHIRCYqMStgYaIfdU5a1ils0I6loQ-siwPP9mmxfBxGEbIs8NBJE5S66t_blZJrvp2o_ceAV-hTQJpXWMz2M4oEKa0oqNWaMHAgjSeX51KgbhLJg_gv8LvOopJM5Q3liejalO8sq4ko4BQwukFzn2X3mJnMSS3Ozj-RZ9sMYFb257K_UXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65ca8369d.mp4?token=QnVZe4dtGHSLnktexMJJoVuJFtig_afbtEVVKi3i4kT05ZM9VhppRAne9cqSObG6RUmJ29eRC0POH5b_fsQED1CWfD2PNfjbqR5JSMQ2Prfb7ig3jeVkgzYRHiF09oxCzZ8W2RMiakVcEtUbedH71tMWXlUlLusz2_Y8omYG7VNkb3SbP9tRwhr7_8heAYT3OvxPIeNFWMcCuojanysAAkwUTpVoGqTJJPqX-drwWtYuep0uRUzWsqZI5Uqblyyjmac3Th5HsJqZJJ-m9S1x4d0TfYocTs4ktGjJwLb2C6xLeqKbj2HZCv-qpE_K3GRRAu81J8ORzDvN3WpZrjPUJgo0UAjStd3QSnaFXrmc4qUYyXdDIbESrqGZBf-pWxMo66VioirzoE89U25JLo7P-1SPrIaQ3Rb5VZE6zupFjqGW89ht0BCAAqg-nUIot1TrR0K1dIw7LQUDs_0BAvhcgUsGAmlWWAnG_zddvVOxA42wfKTYUWazNbkBVsHIRCYqMStgYaIfdU5a1ils0I6loQ-siwPP9mmxfBxGEbIs8NBJE5S66t_blZJrvp2o_ceAV-hTQJpXWMz2M4oEKa0oqNWaMHAgjSeX51KgbhLJg_gv8LvOopJM5Q3liejalO8sq4ko4BQwukFzn2X3mJnMSS3Ozj-RZ9sMYFb257K_UXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آملی‌ها در عزای امام شهید امت دستهٔ عزا به راه انداختند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450466" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwSHptS0Ex4U76WC-KQ3AG1LEyUpAdYY7KCDryvtT7hMywdTsBTRZ54RluS58UJ8u8TGN2X8TljcjVzqjNA-B9M1xMQxrS9sMGDrWomPYU9LwsFgVDt2zkgwioplLh6lh58Ih1jbz4bCITONQocC1mjjw9MaPs0d53JtOppnzpbx17gRw9tgGzetg1CIq9oUkIL3ymLDI7EmiJ9KPMLfQWuwbvNuO3Klyj2ciKcjcqtra0AQvXjxrodDYql9P1Kfq2rRZE1OoZqaPG7Rz5QKQWvITHzNV--LLJ7D4BWZDXaFctL1CFtIe93VNsJBDDEhRIFYr7fnsC0ZBL5vK1bqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQn1T2D0AtHdIWbxFekngyiWI6zk1qFOnNnyATCqThl_0fZtixPyRMOMei8h5q-eEahlpr-v7D1cSK9s3IA3w8nXxM0L5dbNjiT0W5QECSSaKvG532S0bKeu4PPwoLyUARBYHYkJEIsjP6bCVAfkCRdoDM18dJf7_jyxRbURRreGkmN5HCIcWiDrpCLy9QrM6TtO0pNmAnC3gQ9X1ow2HxHlZUuaAeQAikSz40PST4Sa_w_YwNLCYtiiw-7m1GJxsMqAvz8szJQq9Hj6rlme5jsnm0OPPe97wqGGKya3_tlfhy3bzIb-eCt7JXtEHuvnTdV2GC_HK8LaCV79NjZeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_8m34wfR07_9O-rvrgimzEvTBli09_4hEWfrpVM9u5v1Uy6YNJjCK5aJ2CK3cCJ7ydpl7t5NhQYYYWDtYXSlNNxT4Q0OU0zpzCk2qu1sjGA_TzWtVcQmfd22aHs4dQX_osOquqjayn7YI7_WMr-YnVdL-p51k-TOu_lKKAH-4ExpfZNNJYV1NNk9wN7Df3pe-bJ1BwfG5bXRIuQpGaD-2fa6Ab06YQW76sWL6ICb_X2eMPt8CSM_yTa_4QX75w8XhmqrmlGsK_iP245z6SDnu0ekvDscTi32Q8a4XTWdG0d-NoagJlpxKmt1NhC65rdjfReUYBo4GscskoOviqD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itiZHsYN7q3w3cJXfl_eRzLxD0ofCSMm3YYdMzCgwRkNHK2xFjYgAqQyHqhofEkhB1dVYIOFH-OHE_-n-8l3Mcr1ovx5tKngtWfDVOVVEWvJAFzQvVk7WdNP3bqwIW9gl5esFo-YVxXBinLG7nBZTfHGMXmpn-zykxe9XrT9HKDGFYSPqqnXBq5FF4zWWfXkQ_PfiG220vDi6ydpf775wIOvjs2zEjcZQE8tVYB1C8zUv-5Nc7SuTMHNTWOjG7Mzg2sguA-vlFrhfJ-htJxEszY1OfdTgXfCWL0LHdyw3C-elepK8GObAhlSZ3ttGZBADf9FKcGcQUV5ZOUR-uGp3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvF74Z_Xh-rG9PedAV6vWa1LCmFpZPMp5u3oKhAXwKI4vOuIR53aOCj4FYbT8D4_2ccRoXWdqdd5Wm4K8ulTJ8OxbShewuFL5UTBFa87aRrm_UJZSOsEJ_L4zclCazDgKjBdq9JqvlWFapDtAAGyDadvCvnhtMQITgc_jMjaOGdLZzvEWn-eT2P2eLPiTHQ5F5icJ-uQSpasLRaCqB74EUJupx-O6G1-Z2xtin4bmCSWcTBfNVQASDrhYA8BytuZSaeIVXIc1SK4QIR2h0KGBsqEihTL9m30gUjZlVJ3uIJ71IdbOh8OzUIOX6bD1MTuwJnK2Iw-ecMYC4VeR-XZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClNp1osKkaMFvcW15NxH0xKISFc3DTkSU_PmBB5eXo9l3_Ef-1B41a85CyPWkCjAdQVVPlDLDQqujDsUrw1ZlKttcPTRJm7nYzaoBdo44guA6UQIeA46QQuIYPeVKCC6_maaCOv6oknQrydoizFYzD1DqasccK521rTUNqMICRlbKBpILsG14SiU1i8Qk1YJwIXkDj2j4mC0F-Mr-bhzAkpLjZdfew4IOfaIT8DjRqmfUwgCSOebfCbRkhpBDx_hSYbhOECAgDk5YxeBn65v28g0svtQcq8rt8mm8ax8oeExdS1Df9Wr3y7DjY_Ij70cAJBcukXlA-ih4DfZ-A6yZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHKo9LgYnimUjM5zhbiD95o9i-xohd7IG6B1RRMuQf_IaGZ731HnliikYMBA8LinK9Ie-PMGMIa73xM6xlPiK-q9nAKTADUfUndyCdOoo3KgqGqeHa9fn2Y8JS6C5ICXsMOkyUWy4TVdttGvELRfgK-QFB0O2wpV9Oq_H5u2vDkL47IgSpTAsw9NgtxuYnpoKJVjJPpMhahujhQANu7KKytu86Ur3ZDEXpZPbcbFZTKIUGZv6HiGRJQ09FJNGNiIAYlnnx8CiJjtSyhgQrzle5a63fBVbhW9F-Y3tbBgRoOD0b9gTOlOez9N-XHEA330vVgx4xj5UTs26Q_9m5FVzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مجلس یادبود رهبر شهید انقلاب از طرف آیت‌الله محمدی گلپایگانی در امام‌زاده علی‌اکبر(ع) چیذر
عکس :
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450459" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450458">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHNO1JKT5UegQ2WHnVjwWs2FYrsJDVbKOK_2QBIqg3jp5Lh83h66rLjXo9zcH0w8lbmtbHTrsQdeQo8GpvUX70_33Pqim-iK75NXTRWP9FjIPgZVLqQLEncebu3DPaINY4HP2SJD2AfSm9jcNCeJyowSH6WEMPYTgh0KnqJ0p9EqP7kD0rANRRBAXSkqnjreLOs1_KihuTlwSDrWErWXIyLpjRM0Bvys59cA_WhZXgoHnk4QpiZRo_78XEX8H0KHboS5EfUe_hfWFjOVZAmDVITzo8WMK7OtZVpdnXfc0kdMaFlau3FEEElqWViwabwhG0Si0ML2TL-j8cJ0DsHN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنجال مالویناس به لیگ انگلیس رسید
🔹
در پی جنجال ایجادشده پس از پیروزی آرژانتین مقابل انگلیس در مرحله نیمه‌نهایی جام جهانی ۲۰۲۶، درخواست‌ها در بریتانیا برای لغو ویزای کاری بازیکنان آرژانتینی شاغل در لیگ برتر انگلیس افزایش یافته است.
🔹
ماجرا از آنجا آغاز شد که چند بازیکن تیم ملی آرژانتین پس از پایان مسابقه، بنری با مضمون «مالویناس متعلق به آرژانتین است» در ورزشگاه به نمایش گذاشتند؛ اقدامی که با واکنش تند سیاستمداران و رسانه‌های بریتانیایی روبه‌رو شد.
🔹
در همین راستا، نیل گاردینر مشاور پیشین مارگارت تاچر، خواستار لغو ویزای کاری بازیکنان آرژانتینی شاغل در لیگ برتر شد و تأکید کرد افرادی که چنین پیام‌های سیاسی علیه بریتانیا منتشر می‌کنند، نباید از امتیاز کار در این کشور برخوردار باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450458" target="_blank">📅 21:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450457">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e896554a.mp4?token=QWQDLpY5eCQY75QtaYOXa7Y_kfiRgesN3gttJ3U1-436ED2viLNW_4oLuhReo306wdLQ7RgR6CHwCOrxmtBhrg9RsGy7GvT133INRGbzCSQ7oez5cCAIiNF4crillVhxBc0xboq0CNO1BHLDwfLXvagBxAayOrYQWMZpQZ2iV365NLXwcZDc4Fc84C_ObpQi_44kRmzuKknB1uyicuaHgBJsc-mgIpRY3Fe4nXzE7ScuK4FZLKoYTwSUXlv3e0p3NdVKatOJ07wNtCEO1a6rm2kQhmSv2H94RsDMZbz2K2v-RLtNme7B2CbZbqkJuJc_CIhaQ6Si2ttMFmn91o2Z4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e896554a.mp4?token=QWQDLpY5eCQY75QtaYOXa7Y_kfiRgesN3gttJ3U1-436ED2viLNW_4oLuhReo306wdLQ7RgR6CHwCOrxmtBhrg9RsGy7GvT133INRGbzCSQ7oez5cCAIiNF4crillVhxBc0xboq0CNO1BHLDwfLXvagBxAayOrYQWMZpQZ2iV365NLXwcZDc4Fc84C_ObpQi_44kRmzuKknB1uyicuaHgBJsc-mgIpRY3Fe4nXzE7ScuK4FZLKoYTwSUXlv3e0p3NdVKatOJ07wNtCEO1a6rm2kQhmSv2H94RsDMZbz2K2v-RLtNme7B2CbZbqkJuJc_CIhaQ6Si2ttMFmn91o2Z4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا؛ پیمان‌شکن از زبان خودشان
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/450457" target="_blank">📅 21:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450456">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWVk8FLx6ku_74M-Wgk6PciJvegmkSNBLOf3HGbYgk2EchTBggJEd9F99oJ5nqNiaJNqjkr-Un6OUd_uk7BkroHr8OlwpmcwiGZB4nnkp5LaKCNzjBBfevzz5Hdj41udUP3TSn_nsWD_ChawbMz0lnJEU7Ffm5-RPRw50MdanX_CwdbTHM06A0tKWE2smfU7eexV6-UjML7vc2xJ8SsOh0U2QvWJZ8lfSD9_2Y2x0o4Ya5ARF1kw0nb_IaoQoDqqeJJDGF2D2U8Yf7wQsRll4q-jqwzbqrAmrz7-sGEl-5yysuKklaD9bw2-GG559iXlJ6QMBEt9B2aXfJJPAh8_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همدستی اردن با آمریکا در حمله به ایران
🔹
داده‌های رصد ناوبری هوایی هم‌دستی اردن با آمریکا در تجاوز دیشب به خاک ایران را تایید می‌کند.
🔹
طبق رصدهای هوانوردی، هواپیمای جنگ الکترونیک نیروی دریایی آمریکا از پایگاه هوایی موفق السلطی برخاسته و هواپیماهای سوخت‌رسان…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450456" target="_blank">📅 21:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450455">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2K7iRipLItDog5A41owciYRSuACWSYu3iXnhcPMwtH_Sat1lGCXylFiMF1qzaKqpwfW9Beh3DbrvPE9dwbqGOTSA9fI-goT0n858OsxXQxKsuZgMZJgE_LpI7yZTFiTuPF7NSw9pIbtI0-h5xd7dSOGjmxRnoB0Rv_x1rOE8lFQSVh6yI9sGIa1XF4ev1EZs8mWFLQOtLuDHC_UCGqfdYEAwMoZLYVv28o9jSDNp2PArAgGAFl4gTsjCsp-G3I_PQav0vemW6DFHpG2TaesKvdup-uymZMG2ZLBQS3l9pWFW3J__vVTAnVgAPdvDmxjGaNhLEOgNul1wTl0lJdfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر مشارکت در حملات علیه ایران را شدیدا تکذیب کرد
🔹
دفتر اطلاع‌رسانی بین‌المللی قطر در بیانیه‌ای گزارش رسانه‌های اسرائیلی درباره موافقت دوحه برای مشارکت در اقدام نظامی علیه ایران را قاطعانه تکذیب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/450455" target="_blank">📅 21:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450454">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1838d3d8.mp4?token=CWgwUz6ghPpMFs0hSI5tillqaIxYFpiCZ67QlJwPoMcckxOp2kcPHszi_pCszlAXxB74yf9tp7K1viQwjMTT5W_RCXsCSYF-QrQNFanMNNFoe6wf21tPwUXjVfgLGg2xXEh4ymsSjCTnXBv-JvMyQ1Ov5zFozGOMd3_rdO4Layr_blcIt3iM3o5-SHDGyQhWEO1LguF4JXydFkSsa0lmd2Y2nayV47i4wc5_MRTgfCq9S_D2oOMIpyYIG-ehfempplpXcxBpL99m9v3fR2HW32LYrlLx-VjKNN0xiU6Vxk0ZvXuJBt9HjWjZwedXYVUBhW2p-i0RhSqe304B_vIPqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1838d3d8.mp4?token=CWgwUz6ghPpMFs0hSI5tillqaIxYFpiCZ67QlJwPoMcckxOp2kcPHszi_pCszlAXxB74yf9tp7K1viQwjMTT5W_RCXsCSYF-QrQNFanMNNFoe6wf21tPwUXjVfgLGg2xXEh4ymsSjCTnXBv-JvMyQ1Ov5zFozGOMd3_rdO4Layr_blcIt3iM3o5-SHDGyQhWEO1LguF4JXydFkSsa0lmd2Y2nayV47i4wc5_MRTgfCq9S_D2oOMIpyYIG-ehfempplpXcxBpL99m9v3fR2HW32LYrlLx-VjKNN0xiU6Vxk0ZvXuJBt9HjWjZwedXYVUBhW2p-i0RhSqe304B_vIPqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگهٔ هرمز؛ خط قرمز امنیت و حاکمیت ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/450454" target="_blank">📅 21:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450453">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8adda2e4.mp4?token=hMg4az4VNyZRs9PlEGww-IJgddw5BohhEhNQWn-AqEsDgMXkaA6puKotSkbVnN3RBccIxvd1AMMIbstDVp5I1k24hQCjNFvRqXNAFivY7wRxnaWUMC6YuSQ5aJqJHi1JXNZp_8xi1wOqbDuFI58N3ZnM3s5RE5Fw7CN_ztsuqEf39NfdgPAXXS-659Vj5moSXFQpFDnwV3rCh1Q36dJQYYtMR25zji0Sw_iDYIgnUoXndoCE3G5KS28igOntH5q4v6GjIQ_uqxzgbGUxz8OjIvllTery8H8M88emdKliI04KooQnKLY2DExwrRdfTfMhH-nFP4ZhOtHMRJuYY-s4jpmuGp9Ud_RhGBH_-YoJ3ZfSMqXKrRZK_I57XkLiF3tdhm7XxuWNsmjOCRPYXTdf8QyRsfpyD6wFxAUHJ4AfM5qwjOET9QEN_PwPcq_Fz_dubWu-2nLbSHcmpPWZ_lsSSXyRCA1gIM4g24c92G4lQweX5do10Fsw2OM4eornOH_bKUrWNtx-VsOytrVQI3NvuXmRzzuge3HLC17_pvQWnfcKZLsz6xB14UP10TQzVKGYQKvTVkjDC4EqDh-97vqrzC8GjP_bARn7eUDKwUDH48Vdk_9iFqjGmvPfWfPdswPrijr-PrvjYzTpD3lPzhS8Jd5rdXNHvcxo2VCibmfrDrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8adda2e4.mp4?token=hMg4az4VNyZRs9PlEGww-IJgddw5BohhEhNQWn-AqEsDgMXkaA6puKotSkbVnN3RBccIxvd1AMMIbstDVp5I1k24hQCjNFvRqXNAFivY7wRxnaWUMC6YuSQ5aJqJHi1JXNZp_8xi1wOqbDuFI58N3ZnM3s5RE5Fw7CN_ztsuqEf39NfdgPAXXS-659Vj5moSXFQpFDnwV3rCh1Q36dJQYYtMR25zji0Sw_iDYIgnUoXndoCE3G5KS28igOntH5q4v6GjIQ_uqxzgbGUxz8OjIvllTery8H8M88emdKliI04KooQnKLY2DExwrRdfTfMhH-nFP4ZhOtHMRJuYY-s4jpmuGp9Ud_RhGBH_-YoJ3ZfSMqXKrRZK_I57XkLiF3tdhm7XxuWNsmjOCRPYXTdf8QyRsfpyD6wFxAUHJ4AfM5qwjOET9QEN_PwPcq_Fz_dubWu-2nLbSHcmpPWZ_lsSSXyRCA1gIM4g24c92G4lQweX5do10Fsw2OM4eornOH_bKUrWNtx-VsOytrVQI3NvuXmRzzuge3HLC17_pvQWnfcKZLsz6xB14UP10TQzVKGYQKvTVkjDC4EqDh-97vqrzC8GjP_bARn7eUDKwUDH48Vdk_9iFqjGmvPfWfPdswPrijr-PrvjYzTpD3lPzhS8Jd5rdXNHvcxo2VCibmfrDrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواندن زیارت امین‌الله توسط احمد واعظی در ابتدای مراسم بزرگداشت هفتمین روز تدفین رهبر شهید انقلاب در حرم مطهر امام رضا(ع
)
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450453" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450452">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccfddfba7c.mp4?token=kKfHpm-vveuG_cqqTgKVeqwqxJiTE3qiIv6a5a3B6O6kfLeMD14ZGtBsGeLwwCx-oCXk8PMmpof06kTfZCrl2rU-vaOBIiQCl5N_0AjMFXhT3JIiJhF5_H0-VD2ys6PYGvuOdrYhe4bqW-5rQ9SNQGIH8yiunbHx3ZyxVAWKo9LuUIf3tLzzafkpUUC_jCZREmb5ch9G-R7m0uH3F1pdV9-mOaO62sLdjW6lU5ckJnUzCOS4h18DwJdUOiAmTJ5rEoI05D_pQQTvDEWTOwsGip87PD8JMgr1IsgBgwzAyT0BBXGWWNT2gEYDIzft3IXLrtVFlR-sauEtKtkExboKLhobNLGQehRz8-WyLdlk_O-pkDaj8fUiH9nez704X07pIOWpegM8EXGlNwtEC1Ujnh5KMDBs4i-liOXsttod_CFw74PMRE35ZBWB98CbOqjos3W7uYG2kgJ6YJ_3AaUDthVWHx6P6R5FsyJjOVE7nOb8qHjxYJKIHrsz82rghE3U_CJG3g2095PjfUftZfCK-40Gkkpc2ZCimOcDTFpS79J8wK98Id0YQ7PzuExzrPK3kMqMo2d7phvXb4z1K1u5dEnAfgimQhmL1JSX7m1sg-KNPOjwz8Ce-V2vLR1jNMp-MJza7t1FjhNs_23Xt-n7btuIQvQ0RNgrgK3A3jOz4HI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccfddfba7c.mp4?token=kKfHpm-vveuG_cqqTgKVeqwqxJiTE3qiIv6a5a3B6O6kfLeMD14ZGtBsGeLwwCx-oCXk8PMmpof06kTfZCrl2rU-vaOBIiQCl5N_0AjMFXhT3JIiJhF5_H0-VD2ys6PYGvuOdrYhe4bqW-5rQ9SNQGIH8yiunbHx3ZyxVAWKo9LuUIf3tLzzafkpUUC_jCZREmb5ch9G-R7m0uH3F1pdV9-mOaO62sLdjW6lU5ckJnUzCOS4h18DwJdUOiAmTJ5rEoI05D_pQQTvDEWTOwsGip87PD8JMgr1IsgBgwzAyT0BBXGWWNT2gEYDIzft3IXLrtVFlR-sauEtKtkExboKLhobNLGQehRz8-WyLdlk_O-pkDaj8fUiH9nez704X07pIOWpegM8EXGlNwtEC1Ujnh5KMDBs4i-liOXsttod_CFw74PMRE35ZBWB98CbOqjos3W7uYG2kgJ6YJ_3AaUDthVWHx6P6R5FsyJjOVE7nOb8qHjxYJKIHrsz82rghE3U_CJG3g2095PjfUftZfCK-40Gkkpc2ZCimOcDTFpS79J8wK98Id0YQ7PzuExzrPK3kMqMo2d7phvXb4z1K1u5dEnAfgimQhmL1JSX7m1sg-KNPOjwz8Ce-V2vLR1jNMp-MJza7t1FjhNs_23Xt-n7btuIQvQ0RNgrgK3A3jOz4HI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز در آزمون کارشناسی ارشد چه گذشت؟
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450452" target="_blank">📅 21:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450451">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99153d6474.mp4?token=akVlqH6ltaFPCBsOYvcJzxqIOB8O-R8FYlG92tRYfj8dqdN3Aevl3wI8qAfLPP3f0SAGn7QgZyuEHNtvRhanHj9bvLcNZJKvD5j3JOdkbXcKSINRdIK2wNrhvMN9jk-oO3bBdmHgDKp2IOEheS33v1Euz4vtxk_jumYWFKYeYVC-thpqD_4DQEFRd6UZAC6Tjq_kT4UvVMEEQnK88g05Sjma4al_TnM99hyleO7GsE3sKqNH3SK0Nqb2mcpjLdv63PUulbLIfF-OXJDONY1WSS0jqtYb-KVPiKEVN70PzYJGXKnxzfxqb82M4zkO--Mfr4DHtkADy_MxTIBE7myXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99153d6474.mp4?token=akVlqH6ltaFPCBsOYvcJzxqIOB8O-R8FYlG92tRYfj8dqdN3Aevl3wI8qAfLPP3f0SAGn7QgZyuEHNtvRhanHj9bvLcNZJKvD5j3JOdkbXcKSINRdIK2wNrhvMN9jk-oO3bBdmHgDKp2IOEheS33v1Euz4vtxk_jumYWFKYeYVC-thpqD_4DQEFRd6UZAC6Tjq_kT4UvVMEEQnK88g05Sjma4al_TnM99hyleO7GsE3sKqNH3SK0Nqb2mcpjLdv63PUulbLIfF-OXJDONY1WSS0jqtYb-KVPiKEVN70PzYJGXKnxzfxqb82M4zkO--Mfr4DHtkADy_MxTIBE7myXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای دود سیاه در آسمان بهبهان خوزستان چه بود؟
🔹
درپی انتشار تصاویری از یک ستون دود سیاه در حومه بهبهان و گمانه‌زنی برخی کانال‌های فضای مجازی درباره وقوع انفجار یا حادثه امنیتی، پیگیری‌ها از مراجع مسئول نشان می‌دهد هیچ‌گونه حادثه امنیتی، انفجار یا اقدام خصمانه‌ای در این منطقه رخ نداده است.
🔹
فرماندار بهبهان اعلام کرد دود مشاهده‌شده ناشی از سوزاندن غیراصولی زباله و لاستیک‌های ضایعاتی در اطراف شهر بوده و هیچ ارتباطی با مسائل امنیتی یا نظامی ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/450451" target="_blank">📅 21:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450450">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dde642eee.mp4?token=dSnwiq27m9rOv9jdVMRp4NsS4H6JswuGx142kBeNn8c6D4m1TDJpgMP09VKQ4-hl419tXRdEezcNri_s3F8ewW76HR9J8_T8sXazvUh7w9Kzeb6VJdPYIcLQAsf0k6t4avximYxn-ikeRL95N1oggiV5djbwEc-oeHO4630mEQ1yLb56qzasoqsQWpVzntTr-UriAzwaROTRP4W_toUf295H2_ec2v7VlcRCxOGxDcP0Cc4_wwAxUrtVpI2Rjish8ak9TCyPWThrnlIegRzjZBe4qb3IQ5ENmwGrThqSub-eYkS8ifqnEeDk02OUTh_v9TLAVM-D36f6K-ZSOf3x6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dde642eee.mp4?token=dSnwiq27m9rOv9jdVMRp4NsS4H6JswuGx142kBeNn8c6D4m1TDJpgMP09VKQ4-hl419tXRdEezcNri_s3F8ewW76HR9J8_T8sXazvUh7w9Kzeb6VJdPYIcLQAsf0k6t4avximYxn-ikeRL95N1oggiV5djbwEc-oeHO4630mEQ1yLb56qzasoqsQWpVzntTr-UriAzwaROTRP4W_toUf295H2_ec2v7VlcRCxOGxDcP0Cc4_wwAxUrtVpI2Rjish8ak9TCyPWThrnlIegRzjZBe4qb3IQ5ENmwGrThqSub-eYkS8ifqnEeDk02OUTh_v9TLAVM-D36f6K-ZSOf3x6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت آب و فاضلاب: پیش‌بینی می‌شود در تابستان مشکلی برای تأمین آب نداشته باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/450450" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450449">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8e6476c6c.mp4?token=QcHDxFUMILQrngMH6Fi5IuTI_medWdV4GEu2lcYwShN14fqaOPe4HJ0xi8B56t2WxCZd1Th0mvJOhfa-Twm4WEg2xwWA0CwR3JdUb3cEuiq0IZIIRKTpnRUj8uD5sbiI6Bf6I3bU43nkllzcEHr-Gw9UO7EF7pZiMBJ6D6da0qLOjUXchwjpQQYaawhlQxcBaZdj0O13Fy9evvto9GmnDUTLIeIOfbYLTiXpM1GBSYBXooLhC89P3b45pKMGAxbVeS6u5VtagHw7nxF4BfR8rFlwZahF5f0850H2wej3MK1ZUKjia6R8lLWKjC96cERR8YjVs3qP1htyo8Lnx9pKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8e6476c6c.mp4?token=QcHDxFUMILQrngMH6Fi5IuTI_medWdV4GEu2lcYwShN14fqaOPe4HJ0xi8B56t2WxCZd1Th0mvJOhfa-Twm4WEg2xwWA0CwR3JdUb3cEuiq0IZIIRKTpnRUj8uD5sbiI6Bf6I3bU43nkllzcEHr-Gw9UO7EF7pZiMBJ6D6da0qLOjUXchwjpQQYaawhlQxcBaZdj0O13Fy9evvto9GmnDUTLIeIOfbYLTiXpM1GBSYBXooLhC89P3b45pKMGAxbVeS6u5VtagHw7nxF4BfR8rFlwZahF5f0850H2wej3MK1ZUKjia6R8lLWKjC96cERR8YjVs3qP1htyo8Lnx9pKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارمند هتل محل اقامت سربازان آمریکایی در عمان، هدف‌قرارگرفته‌شدن این هتل توسط ایران را تایید کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/450449" target="_blank">📅 21:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450448">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13957b8c40.mp4?token=EZ47Kiekq8ufTtZFxwzZ6a7F82Ia2xw4NyY9tJS71KHTLQh7UjZiKCx2GZiYeD4k0NUNAkYDEdL1X8GNUNLSxrsHHk27T-6VgAo48eJPSlBEusOFl0tMMxjtHRtvdmm80WmyJhGA3c5HjTvcuymoVRCFOB2vzazaO4k12NEIRJ6cFBQCo2aVaFUH8NRjDihbFXrF6q7OL0aZhFehWxP7JsMEYPmgxvpCCUhslPw6uzGxVbFZEtDEs47J5lF3U3ZaAjDJrbVjDs6cmPxpQxn08Gzdk579MBOX5N3asZ1fWA5LKMF8JgBt7N-0Xefy3zH_p4fkO5CTTaNvW7Hw34bj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13957b8c40.mp4?token=EZ47Kiekq8ufTtZFxwzZ6a7F82Ia2xw4NyY9tJS71KHTLQh7UjZiKCx2GZiYeD4k0NUNAkYDEdL1X8GNUNLSxrsHHk27T-6VgAo48eJPSlBEusOFl0tMMxjtHRtvdmm80WmyJhGA3c5HjTvcuymoVRCFOB2vzazaO4k12NEIRJ6cFBQCo2aVaFUH8NRjDihbFXrF6q7OL0aZhFehWxP7JsMEYPmgxvpCCUhslPw6uzGxVbFZEtDEs47J5lF3U3ZaAjDJrbVjDs6cmPxpQxn08Gzdk579MBOX5N3asZ1fWA5LKMF8JgBt7N-0Xefy3zH_p4fkO5CTTaNvW7Hw34bj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی ستاد اربعین: معطلی زائران اربعین در گیت‌های مرزی کمتر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/450448" target="_blank">📅 21:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450447">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUfe-uopsoDpaKVYqR7FFWI7deyiTARLsdIQ9Rx8zeRL_rQUy717XqntlFPTwUwrLao3W2qqfTvfaRhv1GL855-6VkmVfS5FBlHxCuDQ8CXa1OpA8id0WRA8w7BM-50uDeS28--3MSWaR3nsIKLEr8y7UvKa74RKfHZe6IzyEU32eY3c67aqrDCEDmycc7QylmROVhw8LO2AxiNn5Jm0zOd4dVCPtkgO9DYPTu-T8GBEK_GRIwPre0rSAiTxTMasxeVIShh02i9kZFHcKs-H8P2qGZEq5Q_JFAn5P0mi9Nqq3c7J8vgccglpjHA8OC2JGSlEOCFwqZFaNSCPVHiZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک اسرائیل به عربستان برای مقابله با پاسخ یمن
🔹
شبکه المیادین به نقل از منبع نظامی بلندپایه‌ای در وزارت دفاع یمن اعلام کرد که نیروی هوایی رژیم صهیونیستی در تلاش برای مقابله با پاسخ یمنی‌ها به بمباران فرودگاه صنعا، با سعودی‌ها همکاری کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450447" target="_blank">📅 21:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450446">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e308ddab4e.mp4?token=KutiSkyxvQYDxT22vPKtXn1Gx8p3YHGiBY8qxsiDvrCUjh5TqxHBRIS2Z-CWJakJwAhvO-FP0Jct7eB0rVJObp8bLkZ4WIEy34L5bb3BwK7sW3a1iwZpt9igOkwQanoF57FJboTrmpImUQ5UidZaOSCLU8AY-t66W332OAEHx-HHK4y17RyhiQaxEX1xH-J8fK2JjkxXx-7hFdURuxL1Lb1XHINDzDwuI6e4dY4eosqE1xRguu1Apm5yhN_7zM6yin3fEE29-UMrenQb28H5TocGQwc_S7SHsiKgFGoQgB4TZAuB4iByWCKClI2c9OOteSpABboc4fUIpgyBVwZpOYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e308ddab4e.mp4?token=KutiSkyxvQYDxT22vPKtXn1Gx8p3YHGiBY8qxsiDvrCUjh5TqxHBRIS2Z-CWJakJwAhvO-FP0Jct7eB0rVJObp8bLkZ4WIEy34L5bb3BwK7sW3a1iwZpt9igOkwQanoF57FJboTrmpImUQ5UidZaOSCLU8AY-t66W332OAEHx-HHK4y17RyhiQaxEX1xH-J8fK2JjkxXx-7hFdURuxL1Lb1XHINDzDwuI6e4dY4eosqE1xRguu1Apm5yhN_7zM6yin3fEE29-UMrenQb28H5TocGQwc_S7SHsiKgFGoQgB4TZAuB4iByWCKClI2c9OOteSpABboc4fUIpgyBVwZpOYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این سربازان هیچ‌گاه پست خود را ترک نمی‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450446" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450445">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
آمریکا تاوان تجاوز را پرداخت
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/450445" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450444">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dfb3af009.mp4?token=ZE-DVZc5BjfEA52RaN-0xG9KOpeGuu-rkZWpqS4xrujf2laaxJr-ezNDXkEWXtftPI5LNRDuvOkWyU-EnA-fYYRg5YkU0XKq0usFccp1h0XhtVHsNeF7TZzFCrBLcdusYn8hzHasDeJ572yqnxtaWhWtfTzmSJqR9OehMUDO2VGk3rIDuJA7S5ZZojZlIkggaEBKsXsbri13JaRD7mfkWyQ3Y9J1Bu_kD4I8u5OSHUDp1B3O2a2t8My49DgT6pCaEZBb0Z-byNU0i8ZDLuBe9emKIaKezK4duV9YwNINjBliWycf1NiLi-3pCfHgJ_c78DCRCzGa-0jAxkGup3M4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dfb3af009.mp4?token=ZE-DVZc5BjfEA52RaN-0xG9KOpeGuu-rkZWpqS4xrujf2laaxJr-ezNDXkEWXtftPI5LNRDuvOkWyU-EnA-fYYRg5YkU0XKq0usFccp1h0XhtVHsNeF7TZzFCrBLcdusYn8hzHasDeJ572yqnxtaWhWtfTzmSJqR9OehMUDO2VGk3rIDuJA7S5ZZojZlIkggaEBKsXsbri13JaRD7mfkWyQ3Y9J1Bu_kD4I8u5OSHUDp1B3O2a2t8My49DgT6pCaEZBb0Z-byNU0i8ZDLuBe9emKIaKezK4duV9YwNINjBliWycf1NiLi-3pCfHgJ_c78DCRCzGa-0jAxkGup3M4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شواهد جدید از کمک امارات و کویت در حملات به ایران
🔹
انتشار ویدئویی از یک حملهٔ پهپادی در بندرعباس، بار دیگر نقش امارات در تجاوز نظامی علیه ایران را آشکار کرد.
🔹
در این تصاویر، یک فروند پهپاد از خانوادهٔ Yabhon ساخت امارات در حال پرواز بر فراز منطقه دیده می‌شود که نیروهای مستقر در محل با سلاح‌های سبک به سمت آن تیراندازی می‌کنند.
🔹
این تصاویر در حالی منتشر شده که بررسی‌ها، هویت پهپاد را تأیید کرده و نشان می‌دهد ابوظبی، برخلاف ادعاهای بی‌طرفی، در حملات علیه ایران نقش عملیاتی داشته است.
🔹
همچنین؛ بر اساس اطلاعات و تصاویر منتشرشده از کویت، این کشور همچنان با در اختیار قرار دادن سرزمین خود به آمریکا، به‌عنوان مبدأ تهاجم علیه ایران عمل کرده و مبدأ حملات موشکی آمریکا علیه ایران بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/450444" target="_blank">📅 20:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450443">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3f1bb656.mp4?token=jDTcvl3_X2BRjmITizo9cewU2HVdYEt75nRh_jtx5U_Rr2nUVVRQsL2gRnOsxRtcjxSYIyGBoXn5XX1_mWRSj781HcZW_uLyltJWgef0Kvy6p6eL2FgYJw3bfgGKgmSn0F9XpCLA-wvSevOt4tadJ2b4xfwOy7HzNqKSyeOzTHoKkVQ9bEAOEqTuXaZEcEoA_bzIuT1q6BMdBLInJ4gj4T9wOu8Not9AxsrFqQrzts80xGD4gMycUWqO9K4nkqMh5YL2TXiw6xHBt6qhhugytdm_zWYkDCov3Wt54XpwbT-4iVxg83GYfq3zUu4ts29H1brYtIsxdFKEhMTeHXYTag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3f1bb656.mp4?token=jDTcvl3_X2BRjmITizo9cewU2HVdYEt75nRh_jtx5U_Rr2nUVVRQsL2gRnOsxRtcjxSYIyGBoXn5XX1_mWRSj781HcZW_uLyltJWgef0Kvy6p6eL2FgYJw3bfgGKgmSn0F9XpCLA-wvSevOt4tadJ2b4xfwOy7HzNqKSyeOzTHoKkVQ9bEAOEqTuXaZEcEoA_bzIuT1q6BMdBLInJ4gj4T9wOu8Not9AxsrFqQrzts80xGD4gMycUWqO9K4nkqMh5YL2TXiw6xHBt6qhhugytdm_zWYkDCov3Wt54XpwbT-4iVxg83GYfq3zUu4ts29H1brYtIsxdFKEhMTeHXYTag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آلمان حریف ملی‌پوشان ایران نشد
این‌بار برنده ست پنجم ما بودیم
🏐
ایران ۳ - ۲ آلمان
🇮🇷
۲۵ | ۲۶ | ۱۸ | ۲۵ | ۱۵
🇩🇪
۲۲ | ۲۸ | ۲۵ | ۲۰ | ۱۲
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450443" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450442">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9547638aa.mp4?token=Vd8CBQl179CRNH7__5SRfeQvGtcvoFsEqatScJ304UAXcsHrFgq_mj2Ii0O5oxRd4ybNEikcaSq5uhbJvoFXNLWqgxsW0LkiEzBBnQbQE10fV2oJerW_vhYLH0XRLyMJVTEQ5rfpV8BBL9yGzDK0qHmu1rRgwx2iwYLJkJcabPQxiuABlJqz6v3cvJ1iE5wTeNctpZwXhKcxMuBU1QDKBkSYkJIcZI5CnkKnAeHBC2ci_0a3_aD4UAtFSId3O_U8OxWNBES_Ldm4_I7hpxoNgWNAhoDMDN-I75_4QsbUMFkLj1fNw8mTUU_ygJKz8MSesoNCiZ22x5F3oxTk6kgOMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9547638aa.mp4?token=Vd8CBQl179CRNH7__5SRfeQvGtcvoFsEqatScJ304UAXcsHrFgq_mj2Ii0O5oxRd4ybNEikcaSq5uhbJvoFXNLWqgxsW0LkiEzBBnQbQE10fV2oJerW_vhYLH0XRLyMJVTEQ5rfpV8BBL9yGzDK0qHmu1rRgwx2iwYLJkJcabPQxiuABlJqz6v3cvJ1iE5wTeNctpZwXhKcxMuBU1QDKBkSYkJIcZI5CnkKnAeHBC2ci_0a3_aD4UAtFSId3O_U8OxWNBES_Ldm4_I7hpxoNgWNAhoDMDN-I75_4QsbUMFkLj1fNw8mTUU_ygJKz8MSesoNCiZ22x5F3oxTk6kgOMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس ارشد حوزهٔ نفت: در مدت اجرای تفاهم حدود ۸۰ میلیون بشکه نفت و فرآورده‌های نفتی صادر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450442" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450441">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97eb8935c8.mp4?token=va2GS__7n9gjosgBzgAi7QejbLhhcsEEgP7hbiL4VYD5ltVEv54QUk6XlMqhq79-fuEkmX3_lLoc0Ne58Ecx3FN79UteaSFwxPfWS4N8Q757Tx3jHGHJF-G-9yqHQOt-NMS-OuaPjr5AsAWA4P8gBkYMkVzeH2WCtPpezx_2IOMUzJtXnI1r-6oyj_CAyX0COkmdq9GggDrXYuMmLYIOooFqZFdbxgByrNBa74Gnw56yyah9bbC-UV1msEsSsGAO27oKAjKeNHf5ApJv2HHIhkRzVNzJaMY8Y_lw1v5vj_fLtxC2L8b05yrf3uqY7u7t60e-Z8h8wrRIPGlSfxbing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97eb8935c8.mp4?token=va2GS__7n9gjosgBzgAi7QejbLhhcsEEgP7hbiL4VYD5ltVEv54QUk6XlMqhq79-fuEkmX3_lLoc0Ne58Ecx3FN79UteaSFwxPfWS4N8Q757Tx3jHGHJF-G-9yqHQOt-NMS-OuaPjr5AsAWA4P8gBkYMkVzeH2WCtPpezx_2IOMUzJtXnI1r-6oyj_CAyX0COkmdq9GggDrXYuMmLYIOooFqZFdbxgByrNBa74Gnw56yyah9bbC-UV1msEsSsGAO27oKAjKeNHf5ApJv2HHIhkRzVNzJaMY8Y_lw1v5vj_fLtxC2L8b05yrf3uqY7u7t60e-Z8h8wrRIPGlSfxbing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ جزئیات حملۀ بامدادی آمریکا به سمنان
🔹
سخنگوی ستاد بحران ناشی از جنگ استان سمنان: بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی دشمن قرار گرفت.
🔹
نیروهای دستگاه‌های امدادی در حال انجام اقدامات لازم پس از وقوع این حملات هستند.
🔹
خوشبختانه بخش‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450441" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450440">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c674f4f5.mp4?token=LNOTQK-k__8NartoEe9jqPhbNwdrhPS7xBpxEhj3kBtygLjkLejCDXr50ZkpksSvHcs-UM-IfqBm-4DgKHQZp8PNsFRY2r75tHB83MtO_Ap7qxJ-AbGKWF7fzSXHfkgJIvJPqNgya1JhjIUx_e_7TVMgxVqznJSK0kb2WKujIlzMeFpvgjEqsadcfPGYLr-M1MADL-rlHxxSbzXin0PlMS8r9tP62V8TYJl3hZKOMs_YHHxHwpYMVk3O6yZJlNx1y4kzN2YD1U0zpjySt9W2C_UQtcoJun374p3SJN000bpuVTUKfxAp_ZeKnssS5Re-aXbxxxBkTeCRnMQrgjq9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c674f4f5.mp4?token=LNOTQK-k__8NartoEe9jqPhbNwdrhPS7xBpxEhj3kBtygLjkLejCDXr50ZkpksSvHcs-UM-IfqBm-4DgKHQZp8PNsFRY2r75tHB83MtO_Ap7qxJ-AbGKWF7fzSXHfkgJIvJPqNgya1JhjIUx_e_7TVMgxVqznJSK0kb2WKujIlzMeFpvgjEqsadcfPGYLr-M1MADL-rlHxxSbzXin0PlMS8r9tP62V8TYJl3hZKOMs_YHHxHwpYMVk3O6yZJlNx1y4kzN2YD1U0zpjySt9W2C_UQtcoJun374p3SJN000bpuVTUKfxAp_ZeKnssS5Re-aXbxxxBkTeCRnMQrgjq9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
حملۀ آمریکا به اهواز، بیمارستان بیماران سرطانی را از چرخۀ خدمت خارج کرد
🔹
دانشگاه علوم پزشکی اهواز: به‌دنبال حملات دشمن به شهرستان اهواز و وقوع انفجار در نواحی مجاور بیمارستان، این مرکز تخصصی به‌منظور حفظ امنیت بیماران و کارکنان، موقتاً از چرخۀ خدمت‌رسانی…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450440" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450439">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da6ff51f.mp4?token=oGABHZr3eNgN96jv401U1X4vp7mj2UOoYqXNIERaIVXRNhftZ3NZmuxL4wEKweKh2tNu9rLba-vXDdvqaqOj08SBa9hjNd9hXNCuze6QID_IAXi6OFwPhBTm1YDi9IcPJbkClw6HN8HVb4mgVhDMUoGzKHm-C9OU54HK6dheWWIVfHe3pvraMdVfRBxAcdlsowtehwMgw4T1AeWdai55eBKDBXlVCVzSEzxW0e6_RM2bdy9RJB9GoOXzsAG2zlaHBPeOhVUOsaAbmC9d025fm8BOTHSLh5pcN0Zc1FiQai0D1dGtyFEW3hg6gaLnfbZRXGRbl_BQu5cbFe-_Bq219A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da6ff51f.mp4?token=oGABHZr3eNgN96jv401U1X4vp7mj2UOoYqXNIERaIVXRNhftZ3NZmuxL4wEKweKh2tNu9rLba-vXDdvqaqOj08SBa9hjNd9hXNCuze6QID_IAXi6OFwPhBTm1YDi9IcPJbkClw6HN8HVb4mgVhDMUoGzKHm-C9OU54HK6dheWWIVfHe3pvraMdVfRBxAcdlsowtehwMgw4T1AeWdai55eBKDBXlVCVzSEzxW0e6_RM2bdy9RJB9GoOXzsAG2zlaHBPeOhVUOsaAbmC9d025fm8BOTHSLh5pcN0Zc1FiQai0D1dGtyFEW3hg6gaLnfbZRXGRbl_BQu5cbFe-_Bq219A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
توپی که نمی‌افتاد، به نام ایران تمام شد
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450439" target="_blank">📅 20:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450438">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
رویترز: لحظاتی پیش صدای چند انفجار در شهر دبی به گوش رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450438" target="_blank">📅 20:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450437">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6110e06d4.mp4?token=I4fMCnWY0PmKD0nJbyWcbSHf14WwOXU_da-tEY8ogAJBAP7iqcPhMbfR2x_Lq38MvmgAY2LSLI2QHPJvwGp-YXVN0EddiDMSHMYIKu1Y3URPD17SrW0FM9EKBMmM5tx3Io_b61pHY1rhxcgmYGeHzKTbrBcgVTQfLPo1fiq2Nr2tHgfTF9yUlpsc50VNHvQjRPgyo08FIuK9W-5A0_NBE6JWKpJCBzH5zEuBb1lH-tG1W2lByJ2I-Axg-JIIZsxa0_wMbTfzwgTDU7JyPfJcNgKgNHxkAcL8EvQ7BMDylgeLzBlJVILuqW_QNnfnjXOPAGT_ugc2bfWTJPAEgqYrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6110e06d4.mp4?token=I4fMCnWY0PmKD0nJbyWcbSHf14WwOXU_da-tEY8ogAJBAP7iqcPhMbfR2x_Lq38MvmgAY2LSLI2QHPJvwGp-YXVN0EddiDMSHMYIKu1Y3URPD17SrW0FM9EKBMmM5tx3Io_b61pHY1rhxcgmYGeHzKTbrBcgVTQfLPo1fiq2Nr2tHgfTF9yUlpsc50VNHvQjRPgyo08FIuK9W-5A0_NBE6JWKpJCBzH5zEuBb1lH-tG1W2lByJ2I-Axg-JIIZsxa0_wMbTfzwgTDU7JyPfJcNgKgNHxkAcL8EvQ7BMDylgeLzBlJVILuqW_QNnfnjXOPAGT_ugc2bfWTJPAEgqYrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نگرانی تازه برای فینال جام جهانی در نیویورک
🔹
در فاصلهٔ چند روز تا فینال جام جهانی، آلودگی هوای ناشی از دود آتش‌سوزی‌های کانادا نگرانی‌هایی ایجاد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450437" target="_blank">📅 20:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450436">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l94ZmgYDOw14wcZQVS4dg9qJWtGrMZCtThKNQSTBF7FgtrxHtueFajgd77LFbT08TD1Mqkv9vic4JMYqBqo3ZWNoRcsvZ0XEKhSe1r93uaZOgc_a9DfDOUuqx890RVd8GT8V5v1vyQk7GVK36BIWkjFKCZqBDYi9jyUwrImq9Iklp23Pqoc-1wMnSeC656xDUcfgud9tC-VKRc33u3NBdjO2n7imEQNeXKp9WD4yWjTjz3aNeZ6fL-TE37Mh5CQgK0irM53g23xkk89Zt52Gqy_P87f-TTzXxo_0AX5cGAvHq4V1Guv5M5k2wMauP8DSDKU1g9JXwT33NVoznnHQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف معاون ترامپ به ارتباط اپستین با نهادهای اطلاعاتی آمریکا و اسرائیل
🔹
معاون رئیس‌جمهور آمریکا می‌گوید اپستین «به وضوح» با عناصری از دولت پنهان اسرائیل مرتبط بوده است.
🔹
او به‌وضوح با بالاترین سطوح اطلاعاتی آمریکا ارتباط داشت. او به‌وضوح با بالاترین سطوح اطلاعاتی اسرائیل ارتباط داشت.
🔹
ونس در طول این مصاحبه پذیرفت که دولت ترامپ «کاملاً» در برخورد با اطلاع‌رسانی‌های مربوط به پرونده‌های اپستین اشتباه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450436" target="_blank">📅 19:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450435">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQwdtlhf_UZUNGH6ir0ItE9H1N8g_vu3Oa2eLSB9FWfhcpFt3sgbkA0muWIKsi2RvpyHbLjTO15dW6xbTKmnclGVjvLj9hM90iFApEG5u3QS3TyPS-7lIwejakJuXutvN0cBLo2ESF5ZDxh4VP0xX7u01A3-1SdDdMTxIvUdcH1ML4J7ab2Eyz6tX2wisv4NGFfIZ9LwiUBtzHVSp4oixwva4co_H8NqIH6QJxOivK7zlP35Xb3DKpGjNSVFiT6d9KtaHIMLqLqhZKf4a2fbg00EG5Bd4kEOQBERNTp7L8q-sRPAO3JYcQZ2-rQG4xq5frtICdGJUUwxOEfB88XbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: دستان آمریکا به خون کودکان ایران آغشته است
🔹
وزارت خارجهٔ یمن: هدف قرار دادن محوطهٔ بیمارستان کودکان سرطانی «شهید بقایی» در اهواز توسط دشمن آمریکایی را محکوم می‌کنیم؛ حمله‌ای که مقامات ایرانی را مجبور به تخلیه آن برای حفظ جان بیماران کرد.
🔹
این جنایت نقض آشکار حقوق بین‌الملل بشردوستانه، به‌ویژه کنوانسیون چهارم ژنو در مورد حمایت از غیرنظامیان در زمان جنگ (مصوب ۱۹۴۹) است.
🔹
دستان آمریکا به خون کودکان ایران آغشته است و این جنایت، ادامه جنایات آمریکا علیه آنان به‌شمار می‌رود؛ به‌ویژه کشتار مدرسه ابتدایی دخترانه میناب که به شهادت بیش از ۱۶۵ دختر بچه انجامید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450435" target="_blank">📅 19:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450434">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJEMImpiObEmvtbL47KVY0PkYk7_G-Tq4mIqnd3tA3MnnXXoUuH-s3q1LCZ6dmhI71KmBesKEM60qY3RX75MgZ6SGKIMeYI3r6FtKXH0V0j2wt40C-V6G70Eqy1uUcl0HuygVAQOr0IbTI5-FJjv87EYshwZjXjv-1GKZZUr2wlVwjo05K09P6JmDOMMc0Qq0lo6QyYcizzUVEoNim8jpelvl3d3mzZxvjUrklwVB7FIDmCed9wEnmpgGBTz5cAgqJA3YsxucEF_1hsU6mexQmKdPFhbrdu0rpCqesSlzr5MXF11HKQ9JozRS2Avdi8VHZp8i1hHvxKqiLB9_7XSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ترسیم نقشه راه بانک ملی برای آینده توسط سیفی؛ از توسعه زیرساخت‌های فناوری تا اصلاح مدل کسب و کار
🔹
مدیرعامل بانک ملی ایران مهم‌ترین راهبردهای بانک برای عبور از شرایط موجود را اجرای برنامه‌های گسترده در حوزه اصلاح مدل کسب‌ و کار، توسعه زیرساخت‌های فناوری، تقویت بانکداری شرکتی، افزایش اختیارات شبکه شعب، بازگشت منابع و ارتقای سطح رضایتمندی مشتریان و کارکنان دانست.
🔗
مشروح خبر…
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450434" target="_blank">📅 19:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450433">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilG8waf5NYNAfs2c4DliQrOG3Aoudd6_vNfNQf1Nf-QGeRpeg1PaGafNGg2AmPRUtra8vjsWhu_LX3yQaiIR0b-OC2Kfw5ua6I3UIkTjp_OsNvOx8CoeDGeDUrSax90YckGHPU_mAATxrL4SaAuYQ1c3XvTe1YmIi0asESzoinpvbfQrlt7xLvMX6FW5HKk7o0wLlDlowGLOFe0jb-pbsgAkYLXRApFnUyIZk1XN2ktzQm_8MWkc1iG2Gmi8eafkbJpjN5ZsAoAT7rQ9rH-u1WpnEz3AoP6gzQnVJLYXJnKEXVvNA6dcbG7WA1ksSBgHf1Kv50wns81NGFViS7b19Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/450433" target="_blank">📅 19:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450432">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/450432" target="_blank">📅 19:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYAbuRbXqVQcIc27fXSVxdr1GIedMXUno-T2Gs06AnI4pPdla863R7fAZMNupjSdWbkegrnQrdtNF06qh3M0dwCyuVK9jQOzc0ewmdC5xXdg9IiIbEePDndz5eRvbvRC20eVUJYn45Qt2wEKEwKfpiwzSZYvkgHX9660OLc3EjSYUZHOax7iv9M5jVgISHTvQR7kd38itQMWrar5hg0OgOvnH8CAprG2IwmbKeTiOvtV4wSXCkebZI2S0dZbvq1RH1dUzLY1KNVWbANOFfc4CtJBXjJ3n88VOM4qIfKO8DXrMXfB15Jj9a4fBitmVrqXZSaWJxAW7mgma_47nPWPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از کمبود موشک تا رکود؛ ۴ چالش ترامپ برای تشدید درگیری‌ها با ایران
🔹
در حالی که رئیس‌جمهور آمریکا هر روز فهرست تهدیدات خود علیه ایران را تکرار می‌کند، نشریه نزدیک به کنگره آمریکا روز پنجشنبه نوشت که اگر دونالد ترامپ مسیر دیپلماسی را رها کرده و همانند گذشته تجاوز نظامی را از سر بگیرد، با خطرات جدی در داخل و خارج از آمریکا روبرو خواهد شد.
🔹
جنگ علیه ایران حجم عظیمی از مهمات آمریکا را مصرف کرد. فرمانده سنتکام برد کوپر در ماه می (اردیبهشت) به سنا گفت که تا قبل از برقراری آتش‌بس، ارتش آمریکا بیش از ۱۳۰۰۰ مهمات جنگی شلیک کرده است.
🔹
ترامپ پس از امضای یادداشت تفاهم اعتراف کرد که بخشی از انگیزه او برای امضای تفاهم‌نامه (MOU) با ایران جهت بازگشایی تنگه هرمز، خطر رکود جهانی در صورت ادامه کاهش ذخایر انرژی بود.
🔹
محبوبیت ترامپ، به ویژه در حوزه اقتصاد هم‌مسیر با اقدامات او در ایران نوسان داشته است. این موضوع باعث نگرانی جمهوری‌خواهان از این شده که درگیری در خاورمیانه چگونه می‌تواند رأی‌دهندگان را در انتخابات ماه نوامبر (آبان) از آن‌ها دور کند.
🔸
شرح کامل این گزارش را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450431" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450430">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اصابت موشک آمریکایی در حوالی قشم
🔹
استانداری هرمزگان: در ساعت ۱۸:۱۰ نقطاتی در حوالی قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.
📝
گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/450430" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450429">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c29363757.mp4?token=NFOZJAym93Y_qo-jtVUN5e9oBOl2XBvMIcqJIve6QMbNIaJGjX5tuxCah5wMtTKtBw_OSoZdhgNC_-ghBi_C92WxiTPTUiGiJCcuCI2Lu8gVN57Vv5ZJZ4ydRHZ2tsXY5RXzwtDrJK4BvqbkyAELYloTmMDShNa3b4FrJjSoSvWNPCBYM04gKsEaXxYN6-soiLOqZcq1UdYz7pETQRHE2J3EmaQFw2eyAxZsg-v4IcB5gQ4oOoGzTab6WxAOqA_nMni9-9Sit6-ZKT7aDxXjmU1zB_5ZEFhFly8607sZNK0zXrCiZ_a9a7QGWGSa9qbjQ9bfgDQhRX6YSg3rOESM3QMT0HwO8aHpN8LMptreEtlX3gJHDTxhHObzKs18ydjYXO0yXV6vzIOrRWYr1BRXtnQZprdC5hGhwzQp1kqOyWKb356ElRyPdura1FeKGzVcGzDOmegCKlgnJREjyHzETaFvGJqb_fIxtk0IDqbtz7HBvC88wN_twOoJqrM97uIVXmWwoFL4RasuvySWR-vk5nMmZs1jv-7lQKblHAeKnLT2rVOAyS-mZZYdOtmGs5mDdpRv2ZUNzo6JCGHikTm6BTK3rDSjBsE_U7nLMy2l8pbhL5OYWFz_AUL0n067Dlj7ThXyDXFZxHkooaSssJTocKSdOjQfsSmyy2C2kNZuqkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c29363757.mp4?token=NFOZJAym93Y_qo-jtVUN5e9oBOl2XBvMIcqJIve6QMbNIaJGjX5tuxCah5wMtTKtBw_OSoZdhgNC_-ghBi_C92WxiTPTUiGiJCcuCI2Lu8gVN57Vv5ZJZ4ydRHZ2tsXY5RXzwtDrJK4BvqbkyAELYloTmMDShNa3b4FrJjSoSvWNPCBYM04gKsEaXxYN6-soiLOqZcq1UdYz7pETQRHE2J3EmaQFw2eyAxZsg-v4IcB5gQ4oOoGzTab6WxAOqA_nMni9-9Sit6-ZKT7aDxXjmU1zB_5ZEFhFly8607sZNK0zXrCiZ_a9a7QGWGSa9qbjQ9bfgDQhRX6YSg3rOESM3QMT0HwO8aHpN8LMptreEtlX3gJHDTxhHObzKs18ydjYXO0yXV6vzIOrRWYr1BRXtnQZprdC5hGhwzQp1kqOyWKb356ElRyPdura1FeKGzVcGzDOmegCKlgnJREjyHzETaFvGJqb_fIxtk0IDqbtz7HBvC88wN_twOoJqrM97uIVXmWwoFL4RasuvySWR-vk5nMmZs1jv-7lQKblHAeKnLT2rVOAyS-mZZYdOtmGs5mDdpRv2ZUNzo6JCGHikTm6BTK3rDSjBsE_U7nLMy2l8pbhL5OYWFz_AUL0n067Dlj7ThXyDXFZxHkooaSssJTocKSdOjQfsSmyy2C2kNZuqkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف‌های بی‌پایان عاشقان برای تجدید پیمان با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450429" target="_blank">📅 19:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450428">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67340c5ecf.mp4?token=RjwUEou8rUmZEYqQAFnuf8p1Q76c-u-0L3Hz-Qfq4cyXkda9YAZu7w8jR16sdbLl3AwmzUSkj5U55nfzEFGmgz-OjtHThjYSXca_504wE0XdCRLTIwuzEZUe5x22AU7m077NA2V7T4LzJFJQexyACXsD-JdyZmN0vv1guBxBcaIoIQdHBJGGBrQlw4ZkMjDBS3-s1SQ76tcdeCWyJ-l4rrC3Xg6DOSPTCyVngAbnQKmTs1-LTH4kaoJeAWdBltHP3wcaj48vzV2wa-f3LsrvitURC2idX1xlL4-l8N4hYWGQeb-yaeZ_5tzFjv29WajikdeotMpa3dNd_Pf72GgI4zTyqSIWN21WxkoH-4bak96sMJ8ltKWtBTExkz1-wkHIYQxwAS-3-GNULgQd4rdjd9835PlTEFPK_I94TjAJabhNn5kHtklzDImeob0ioDSVTQ0ae-7QlI85tTpYCsXg0zLOFxTjtbXhh63AMG_imcr-P6u-9I9MHiGMHjVqbIfTy0bMb1EFAj5O7HhQfva3BQTFp-MFXdgizFw4258X6vX92VACjb1G4OVtK9bm9hG2tPsgbmOM7J7YAEahmgrCnm4ry-5Hwqj9bUQvQWeYCK6x8rDHqH0mscZzPr7YtSx0WwgM70GbUNLWhwJCyeV9BDnxQ2cdI-ybbzyVM0EpYIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67340c5ecf.mp4?token=RjwUEou8rUmZEYqQAFnuf8p1Q76c-u-0L3Hz-Qfq4cyXkda9YAZu7w8jR16sdbLl3AwmzUSkj5U55nfzEFGmgz-OjtHThjYSXca_504wE0XdCRLTIwuzEZUe5x22AU7m077NA2V7T4LzJFJQexyACXsD-JdyZmN0vv1guBxBcaIoIQdHBJGGBrQlw4ZkMjDBS3-s1SQ76tcdeCWyJ-l4rrC3Xg6DOSPTCyVngAbnQKmTs1-LTH4kaoJeAWdBltHP3wcaj48vzV2wa-f3LsrvitURC2idX1xlL4-l8N4hYWGQeb-yaeZ_5tzFjv29WajikdeotMpa3dNd_Pf72GgI4zTyqSIWN21WxkoH-4bak96sMJ8ltKWtBTExkz1-wkHIYQxwAS-3-GNULgQd4rdjd9835PlTEFPK_I94TjAJabhNn5kHtklzDImeob0ioDSVTQ0ae-7QlI85tTpYCsXg0zLOFxTjtbXhh63AMG_imcr-P6u-9I9MHiGMHjVqbIfTy0bMb1EFAj5O7HhQfva3BQTFp-MFXdgizFw4258X6vX92VACjb1G4OVtK9bm9hG2tPsgbmOM7J7YAEahmgrCnm4ry-5Hwqj9bUQvQWeYCK6x8rDHqH0mscZzPr7YtSx0WwgM70GbUNLWhwJCyeV9BDnxQ2cdI-ybbzyVM0EpYIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود اولین کاروان اربعین حسینی به سرپل ذهاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450428" target="_blank">📅 19:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_2r1StHGsGTU6v4b6E3p_JFMQInmIcLIA48VK0qRyp-ycaORQCG7Y1e6CohS2LXQ8WVYxEjTY8199tvC7OqCj74gsp9JpJwd8DbW2ZQogq5-mxUzMNfJ-oKioXDbKGhEWc4ft47p2cCdeFVceXxViH7TvP1zoZLcHnQmKqhyKZuuyY0toBWx4uV8B8s5Y2cuCi7rtuXcSUyXbOIrRmtD6THEiiKDgU2-wknR80AcOgwxtlvvcBHyHhGvDDJfhzeO3H0h0u-GrI5N2dqrl_JDr4gx7RJbOTCtH-8zKOf8S37BdupGksihr57AYPlyPVTEqFwoWArkMwUNxadFuybWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce1H4dTCxhOduerxEQyFU-9VuJr_x-A3e43jLQZGk3LHgUARxVEwFpI4OAT7jAUK6csrx20srjWPZkQf8cLvzNoukroEoMMfYoo3y32OcUKhx55_7dOCAySGQ0cSlGXKjeUhTtmEmqTHZ0riFJroPF37qkfXTNDmryauATF4bAp-4pwgOhCdShbfyp1gM10rDEQRMFf6U932ImFrsfPS4T0ac1YEMBjEUEV8Idg99GuC1m3e7rqtT3S4-5veyGBs8IuURA6JyBB-d3a9DJXJPXklnKuPC8JvVxaxRj3RH_kqpKiIkQRlglebg5-5ad6hkHog3ZJt39VrKqfa32ySJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
بیانیهٔ وزارت امورخارجه دربارهٔ حملات وحشیانهٔ آمریکا علیه ایران و جنایات جنگی ارتکابی
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/450426" target="_blank">📅 18:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450425">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9Zd4vg3WPo5Y3h_JS5ikmJCRCRxc4QJiCxB9-_Vio_y8M4t1E67g_oaupEiLhjUNJqvnTh1qFu7FcZhVZFIfWxIUuCyURA5sKVacfEvNAfBAZIP_A5m5B4aMKU8XvO-2IMzJ_oGB3u-EtryBpaKuT0ezUzFfJjvkPlcFExUwFBTyAAoBn29ciZvBDTPsn6LrUKsjRrhGUp4E5lHRrXSPRJlSlqXRndj81Alh2fjpsOuPlZptXgDwvlJDdPOKh0eZ-xon7neA6Si8zuos9EFCpnlUZWtHs6xqDzoD7f1rzchi13NxUY0yPeQXSSAG1nsdmHtjF4yWGvIkjHTHpLsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدهکاران بزرگ پای ثابت بانک‌ها را بشناسید
🔹
بررسی آمارهای بانک مرکزی نشان می‌دهد نام برخی شرکت‌ها و گروه‌های اقتصادی طی ۵ سال گذشته به‌طور مداوم در فهرست بزرگ‌ترین بدهکاران کلان بانک‌ها تکرار شده است.
🔹
بانک مرکزی از سال ۱۴۰۰ آمار وام‌گیرندگان کلان شبکه بانکی را منتشر می‌کند. بر اساس این آمار برخی شرکت‌ها در چند سال یا چند بانک بزرگ‌ترین بدهکار بوده‌اند و برخی دیگر نیز هرچند در همه سال‌ها رتبه نخست را نداشته‌اند، اما همچنان در فهرست ۱۰ بدهکار اول باقی مانده‌اند.
🔹
در میان این بدهکاران نام برخی شرکت‌های زیرمجموعه خود بانک‌ها نیز دیده می‌شود؛ شرکت‌هایی که از همان بانک تسهیلات گرفته‌اند اما اقساط آن را پرداخت نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450425" target="_blank">📅 18:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450424">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اصابت موشک آمریکایی در حوالی قشم
🔹
استانداری هرمزگان: در ساعت ۱۸:۱۰ نقطاتی در حوالی قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.
📝
گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450424" target="_blank">📅 18:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450423">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">📷
مراسم گرامیداشت رهبر شهید ازسوی آیت‌الله سیستانی
🔹
این مراسم باحضور حجت‌الاسلام شهرستانی، نماینده تام‌الاختیار آیت‌الله سیستانی در ایران و جمعی دیگر از علمای قم برگزار شد. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450423" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450422">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حملهٔ پهپادی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار اعلام کرد که پهپاد ارتش رژیم‌صهیونیستی منطقه واقع در بین النبطیه‌ الفوقا‌ و کفرتبنیت‌ در جنوب لبنان را هدف گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450422" target="_blank">📅 18:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450421">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaD6S01uXW7o9Ml2Sednf9KvanYExYxkM01JvPcagReMAUEpyWujdk5dHapiBYLaYkVvUIrLHlJFme3v56IilWSG24a1Ul8F9WkRobnOF20WMbDFUWJ2th4nkr4fx_mLAV5olvmeBmIupI3DCnPOY9jPO8DWsgbmN3npMCqXh-vrDxsc_bN5hha-i6cfWtPRMf2VLN6hpdcsBtMTqd_HqmSca_Zv5ZUgizB2zUqG_yo1jao-iAdlV0lbwSH1aAdc-i2JahH-_65Aqqj1r4X0yb4NBqAHFp6LQi683-FHnSsR9puj5G2-k8Fr8skW3Y5s7cigcU7z8y3lF_QjfVDmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضوابط جدید واردات و عرضهٔ خودرو در منطقهٔ آزاد انزلی ابلاغ شد
🔹
سخنگوی سازمان منطقهٔ آزاد انزلی: مطابق ابلاغیه رسمی پلیس راهور کشور، از تاریخ اول شهریورماه، ترخیص و شماره‌گذاری خودروهای وارداتی به نام اشخاص حقیقی امکان‌پذیر نخواهد بود.
🔹
همچنین پیش‌فروش خودروهای وارداتی با پلاک مناطق آزاد ممنوع اعلام شده و متقاضیان باید تمامی مراحل واردات، شماره‌گذاری و عرضهٔ خودرو را از مسیرهای قانونی و تعیین‌شده دنبال کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450421" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450420">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0JLHtM-7TCZ7P9LuSjVCTFvFs8mMPQPfG7uMQIP7NUwDDFR-Kzc3ikBQq6JMaZXkFJBIZABUFBM0KZfco0wjOb7GUsVmtP2WSja3ibSU0iZjFQRx8OxOqV4eo41abXersRSOjFX26_QE9oas4B96-nQw_9EuJ5HytLgbGWeWLI1zOGaTm-Z3MhOeg-ctiiwvlE-GG6vsVO6P-xoKFOUnyzgorF4UvSqltOObXARUdM47HM1vv6gtHMqdRtHhN4XrvHg0SV0NoPBVrqig-w13fJ8yVB7v1kgfxBeHy6lPQa6l7gArywuJb-Z1gymEsP7cQUiFHAejsR8YP5OfA_4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنجال امنیتی ابزار برنامه‌نویسی ایلان ماسک!
🔹
گزارش‌ها نشان می‌دهد ابزار «گراک بیلد» به‌جای ارسال فایل‌های موردنیاز، بخش بزرگی از مخزن کد کاربران را به فضای ابری منتقل می‌کرد؛ موضوعی که نگرانی‌هایی درباره افشای اطلاعات محرمانه توسعه‌دهندگان ایجاد کرد.
🔹
گراک بیلد (Grok Build) یک ابزار برنامه‌نویسی مبتنی بر هوش مصنوعی است که توسط اسپیس‌ایکس‌ای‌آی توسعه یافته و برای کمک به برنامه‌نویسان در محیط ترمینال طراحی شده است و این ابزار با دستور گراک اجرا می‌شود.
🔹
پژوهشگران امنیتی دریافتند این ابزار در برخی شرایط، کل تاریخچهٔ پروژه و فایل‌های مخزن را به سرورهای ابری ارسال می‌کند. در میان داده‌های منتقل‌شده، کلیدهای SSH، رمزهای عبور، اسناد شخصی و تصاویر نیز مشاهده شده است.
🔹
بررسی‌ها نشان داد حجم اطلاعات ارسالی بسیار بیشتر از نیاز واقعی ابزار بوده و حتی فایل‌های حساس مانند «دات‌اِن‌وی» نیز بدون حذف اطلاعات محرمانه بارگذاری می‌شدند؛ به‌طوری که غیرفعال کردن گزینه «بهبود مدل» نیز مانع ارسال این داده‌ها نمی‌شد.
🔹
پس از رسانه‌ای شدن این موضوع، اسپیس‌ایکس‌ای‌آی قابلیت آپلود کد را غیرفعال کرد، وعده حذف داده‌های قبلی را داد و در نهایت «گراک بیلد» را به‌صورت متن‌باز در گیت‌هاب منتشر کرد تا کاربران بتوانند کد آن را بررسی و با اطمینان بیشتری از آن استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450420" target="_blank">📅 18:05 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
