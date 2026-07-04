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
<img src="https://cdn4.telesco.pe/file/AHGVQRwjnDu03HUwWlU4xv9qrO4mqXSA4GbV7LdAWpu_K6-zmu0mf7aJZC2_g1a5smW7j10hAuG8WGeG3lGx2Thza6BncWJgD09iAEby4D7qXKp6lKlqd8ksVVRX4Iu65Alfv9hW_xGqf0zNixFO3glg_cBDXj2YWIS4NEDVeraOCxhVpein-Ti4wSjrKGYzK4XPT-JblbLR8vPR-pLox_zAEJDE-JEnZsvdpElwXOd-cE0JAfDSVKenK7NMYNtctEfs0Cy3zV_y9cRSmcV1NpAEMeoEYdGpoMD1-IkB5BjFeTMwA8DnbWMNvR7BNybUt6HVidqZx1WXaWSKqc1zBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 11:38:00</div>
<hr>

<div class="tg-post" id="msg-666272">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
افزایش تولید نفت اوپک با بازگشایی تنگه هرمز
🔹
طبق یافته‌های نظرسنجی بلومبرگ، تولید نفت خام اوپک طی ماه میلادی گذشته با ازسرگیری صادرات تولیدکنندگان خلیج فارس از طریق تنگه هرمز در بحبوحه تفاهم‌نامه ایران و آمریکا، افزایش یافت./ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/akhbarefori/666272" target="_blank">📅 11:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666271">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQQscHkXuhLtCkSQCBEabOV2tsMxtcmMi3Yo6xscppdmsfv1yjO6HlMP6tEtVmzKrN8_SkbPDoYW95TEvep_gV-xxuYxdm8qyMlvnCJ0DVhqQlP3Wf1ndbn_xD2eEsyyhwxfgeTgGOUXmEOEuTogAXcDyESyJ4JZzqBtaJRwRCCmuUGybai35RXueo0xKrO3s9eNDaZZR3TJC1UQnNF9bTNrHrpkO6dEdQOjhuCOf-TfhjeNsYi1-GwHv5YiOG1jY1elZmzC9ru-mPjecoVQbMrlyvkjQ0VEUImEHHWBs6pfpDaY2JPBk47faIV8yXAsBDeo4vJmJr75KiSbtZbDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
فراخوان خبرفوری برای مراسم تشییع رهبر شهید؛
«بدرقه یار»
▪️
مخاطبین عزیز خبرفوری، برای شرکت در فراخوان
«بدرقه یار»
کافیست از مراسم تشییع در شهرهای تهران، مشهد و قم عکس و فیلم تهیه کرده و برای ما ارسال کنید.
▪️
سوژه‌های پیشنهادی:
پرچم ایران
ثبت لحظات مراسم توسط مردم با تلفن همراه
حضور و شکوه جمعیت
فضای مراسم و جلوه‌های معنوی و حماسی تشییع
▪️
آثار خود را به آیدی زیر ارسال کنید
👇
#بدرقه_یار
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/666271" target="_blank">📅 11:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuYcqnTn075Wc_g06G9ZyNZYl5RkLz8YPHEsa3yJYHnPs4DMIOa6hRZleLodKbYGGgJlS6KZx8mFsVs92OXkd4xS23vzeuFPmoHA5Icj-3EjAzSnmzW7hBDZikiQ-tgcixXcRVXSoMyBr4H6qX3xG3eiMihEGpwcVNtaQS1d-fBoLdZvr0KKEATcoTs5dHyfkzzHBCfKnUr93XUdLHNAOVnSF4r_h5jxhD7BvUeweGasQxpTTBk1ItjrRrPkPi5p27YgCtimzIK9vdvCGWEOVxy3dfZoFkhBZ1tx4Tmuo_r0LZBQ8frZBE_AjvgUz3KKT1Ay09bijwJZhhGuxef4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای انواع پلاک خودرو در ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/666270" target="_blank">📅 11:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7eEzAn92SJ4o_kmJc4JFFoaIsPYGWxuzT9tdrpj3XhT5piTE7t7Fe8AqFzYfChlhEsW373YTcGsFOiRlyUISlxLLErz9EpF-lF-0JApf5fj850bLxF1Z-Umaeocda5wQQ5C1a8LpUifNVd106Hw9BqLJyZF6iz3BKWcXdECKs-_WdXzVYFn7izzShGCReQwvvmspRyncOt1bidjOZElNRLJGBw5eJzNaP_tnsE2Fbj7AbcgjoZ_3x7land9iKJSncaDQ454BF2S9ro-YOryPozm5rL4xmyg9IeOxNTdQYQoaSXbVzKEeTpQlTzUTaR--uTZHPc2RUjCj-iu5dFCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این بار، قرارمان یک مچ‌بند سرخ است
🔹
پارچه‌ای به رنگ خون؛ نشانه‌ای از عهد، وفاداری و مطالبه خون شهیدان.
🔹
بیایید در مراسم تشییع، با مچ‌بندهای سرخ تصویری ماندگار از وحدت و ایستادگی ثبت کنیم. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/666269" target="_blank">📅 11:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef946d3a0.mp4?token=hUG5L9HlCYMya37eC1cKJ33mXhuNOtJ1rZ6ja8Gt9pWYD3AT3WklWZqSv3CVF9xTfR77cxk3lQsEBxht5183drCoArSsseGJ1Pw8ilCwDqW0SEQIzbIDI1gy3j2G1cQKQ_l997qV9q2LsYl6ahvS3qhr8faW32GfnIZKbdMUlQWXkIjHA3kJ6ONxxCkTT3E-5iYTOgAYi6_gFhANKInemoU3qDhFi1x-2d_wAVVTUVCLJvt3HIqHjCx4-jZpsdBmVS3a_DTa1Sntv4KGH0yRlcn05p5b5YVx8BzQP3qLMzQ8CUArbceu_Hqiz9ova0IyPZiHTk-SBobTESIHJq74VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef946d3a0.mp4?token=hUG5L9HlCYMya37eC1cKJ33mXhuNOtJ1rZ6ja8Gt9pWYD3AT3WklWZqSv3CVF9xTfR77cxk3lQsEBxht5183drCoArSsseGJ1Pw8ilCwDqW0SEQIzbIDI1gy3j2G1cQKQ_l997qV9q2LsYl6ahvS3qhr8faW32GfnIZKbdMUlQWXkIjHA3kJ6ONxxCkTT3E-5iYTOgAYi6_gFhANKInemoU3qDhFi1x-2d_wAVVTUVCLJvt3HIqHjCx4-jZpsdBmVS3a_DTa1Sntv4KGH0yRlcn05p5b5YVx8BzQP3qLMzQ8CUArbceu_Hqiz9ova0IyPZiHTk-SBobTESIHJq74VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود مردم به مصلی با آیین خاص برای وداع با عزیز ایران
#بدرقه_یار
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/666268" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرفوری
pinned «
♦️
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
🔹
خبر تعطیلی شهر تهران در روز سه شنبه در حالی منتشر شده که پیش از این سخنگوی دولت، شهر تهران را تعطیل اعلام کرده بود.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/666267" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666266">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiVndAVi008dKG9kVXwTRnRjFRUmJOTi3-YXUNx7L0S6x_b8mKEyL21t89LGmELz7GgFtOx4WMoQ1vJ6RcAnyUWUFki0ZL7YpJOVxRuHh4pAsnQ6VVb1uttaCu8aeWa7WJo4L1tOhGJaX9D_udPMVLFL3Qhho_86Oebs33nwwRqZQX10urVeV378R9qnDHjLg2zglJ-vDYdq7_BsjDlv9OS_u2C-9Hid761U6raMAx9k5GDU4RiX5592LElfdLHEhZaYQdPdAaHUJyXrw0JJbps_DgCsCUMW3xR4oeXj7ChifVU-e1z49uXTwGRlzcnFx126-ASUOR2Z4qp1c7emVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت غرورآفرین شهید مدافع تنگه هرمز به آغوش میهن
🔹
پیکر مطهر شهید والامقام حسین ستوده، غواص و مدافع حریم آب‌های سرزمینی و تنگه استراتژیک هرمز، پس از ۳۲ روز جست‌و‌جو در دریای عمان، به میهن بازگشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/666266" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666265">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aeb6f1e8c.mp4?token=hGuf5cXjVGjdmoUyS_diZlZI4HZZS1ri7sV5rTVnrgLC4v_5ly3sKc9XffcpZda_6TCW19P0h0ksGtgx4HQm5KB3x1L21DHocfh9GOMV2kaU8D2j0fuqaFnRvGViy4RM0jv1i0KTJrH_nqEwrjz5fXFrHRPAPx18oqLBKUR8gowTAfJpZ8qDzEDrmMwURzn1o-AqTkATkCN4NoAt1C0tMjqhwT4gqEpoi0w8SIuaUu-CaEwwJFfx7XN9xja5PkBRDQGeG4ST06JfZO-xPdQP5xOP86ahgnGi1HvlVjbJ9qHXgtah5DTWfKwVJ7iBnaV3Xfm0KFqpVOhP8mrpUUrSAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aeb6f1e8c.mp4?token=hGuf5cXjVGjdmoUyS_diZlZI4HZZS1ri7sV5rTVnrgLC4v_5ly3sKc9XffcpZda_6TCW19P0h0ksGtgx4HQm5KB3x1L21DHocfh9GOMV2kaU8D2j0fuqaFnRvGViy4RM0jv1i0KTJrH_nqEwrjz5fXFrHRPAPx18oqLBKUR8gowTAfJpZ8qDzEDrmMwURzn1o-AqTkATkCN4NoAt1C0tMjqhwT4gqEpoi0w8SIuaUu-CaEwwJFfx7XN9xja5PkBRDQGeG4ST06JfZO-xPdQP5xOP86ahgnGi1HvlVjbJ9qHXgtah5DTWfKwVJ7iBnaV3Xfm0KFqpVOhP8mrpUUrSAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون حال و هوای مسیرهای مترو منتهی به مصلی برای وداع با رهبر شهید انقلاب
#بدرقه_یار
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/666265" target="_blank">📅 11:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666264">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آلمان، ترکیه را در کنار روسیه و چین در فهرست تهدیدهای امنیتی قرار داد.
🔹
انفجارهای کنترل‌شده امروز در ارتفاعات صفه و بهارستان اصفهان انجام می‌شود؛ جای نگرانی نیست.
🔹
شرکت نفت روسیه: پهپادهای اوکراینی یک تأسیسات تولید گاز در سن‌پترزبورگ را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/666264" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666263">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رویترز: ژاپن می خواهد بعد از ۷ سال از ایران نفت بخرد
🔹
ژاپن، کره جنوبی، هند و کشورهای اروپایی پس از تشدید تحریم‌های آمریکا در پی خروج دونالد ترامپ از توافق هسته‌ای ایران در سال ۲۰۱۸، خرید نفت از ایران را متوقف کردند. در سال‌های اخیر، چین اصلی‌ترین خریدار نفت ایران بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/666263" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666262">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04b415aa5.mp4?token=SufgC2vH3aKu68O89bVtpefM4lFNdrzA-5VkhmoMF-9ozj5iYT2l-D5gaF9eKT8dE4I1modwJyRy4GxMNNrwAGvwMUJYRLTVxIsKfDY_2Bo53Jrt0k8ZfxLB96NYHiyKkPAKZSSXr7Uosjtc-KimK7VGill6xIhaOA-Spo3jW2Ngm5Fq5AGgPIaBDNOZsNP1-vMnsiYl4UTz9zgitPg3EoSmq88yiEk-qpwfXE7fUBboDCRJCxGwPjPpDt8aI573LFwW40_WsOsA80ubnp_oDErLDFZIfROlcbfhDfJyY4xMD8rXhaOgTc8kGXM7nvwV8uZUq5XBceYkrfM1r4fLgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04b415aa5.mp4?token=SufgC2vH3aKu68O89bVtpefM4lFNdrzA-5VkhmoMF-9ozj5iYT2l-D5gaF9eKT8dE4I1modwJyRy4GxMNNrwAGvwMUJYRLTVxIsKfDY_2Bo53Jrt0k8ZfxLB96NYHiyKkPAKZSSXr7Uosjtc-KimK7VGill6xIhaOA-Spo3jW2Ngm5Fq5AGgPIaBDNOZsNP1-vMnsiYl4UTz9zgitPg3EoSmq88yiEk-qpwfXE7fUBboDCRJCxGwPjPpDt8aI573LFwW40_WsOsA80ubnp_oDErLDFZIfROlcbfhDfJyY4xMD8rXhaOgTc8kGXM7nvwV8uZUq5XBceYkrfM1r4fLgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رستاخیز خون‌خواهی
🔹
گزارش خبرنگار خبرفوری از مصلی تهران هم‌اکنون
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/akhbarefori/666262" target="_blank">📅 11:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666261">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d98b5acb7.mp4?token=SiIalaA6s8xmbCFm7Jo50S8TasfEsNnTq0KDDA1lYBMFP5NrGRYGUE6f_MxQhhvEQza76CU36HMZimNFuFDT5T1BIZxzXP68x6LHHTOPa2WBgAhqItuC451NDV5EgQBFyZeGtu19hnlqm0R_adG3f9lBE1z6Qf1dI2Z9lYqrYE3qVQQM3y7JDKBF07cZpE_JFoE76oiUlS_LlRAvHX6e3uXdUlgMC5WOmwev4ZEvnz-hh1FHPVwe6eg2vm_GmmUjf889gLJI2lvkodMiPu3IYiuIviJxrTKC4fCoYud6PW7wi_tHWKLshRJF5b7vmJvAYmjnHcsKt-VqaWbM1GTnDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d98b5acb7.mp4?token=SiIalaA6s8xmbCFm7Jo50S8TasfEsNnTq0KDDA1lYBMFP5NrGRYGUE6f_MxQhhvEQza76CU36HMZimNFuFDT5T1BIZxzXP68x6LHHTOPa2WBgAhqItuC451NDV5EgQBFyZeGtu19hnlqm0R_adG3f9lBE1z6Qf1dI2Z9lYqrYE3qVQQM3y7JDKBF07cZpE_JFoE76oiUlS_LlRAvHX6e3uXdUlgMC5WOmwev4ZEvnz-hh1FHPVwe6eg2vm_GmmUjf889gLJI2lvkodMiPu3IYiuIviJxrTKC4fCoYud6PW7wi_tHWKLshRJF5b7vmJvAYmjnHcsKt-VqaWbM1GTnDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری، روایت مردم از حضور در مراسم وداع با رهبر انقلاب: پسرام رو آوردم که سرباز پسرت بشن
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/akhbarefori/666261" target="_blank">📅 11:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666251">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjOM287_lR6oMmuYwq2G4X0L7cFdRitKt9JyuN2wMfj5Ja3xJNmweqnUYMcAKwhC9gJ-H1Vyvz08HLIVnCSeuwJaq28Yziae-rYwam4L6hvP-W_2sKe0onlo7NAHiyvBgYt3uLbhE9aZTuV_928r-H_hQit9IuagzXBsC8F6OMSGtjFXJN0PFLDAzNxY42Gjq6rx7JciWy5tAjck13pN_B3Z9MR6m42ZqleMBKuNFHaRq2snHHcOODzXrmEMOmAPWWWuG64HkTBmEZAgC0q8b2oWsM2nGU8jyDTAygylQh_q3GoDQtbrQK26NZDf9qK9QbqLbaUrLBTQo9cq0ZQgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jnl2Emu375srp36nlhjUB8YF8qcm6lHmOkEKHnxGmnWBNzRLlIlDocT5GSuJk8IDZpSJzvNCv99l-13XYp56dXNVnAQbdtksaQtzzGKzr4mcwCmBktVCWesRsR_-HJco-S2KPTi6Bl-sV6Z5eIkKLpDr_8e9JU0V8wE5ZAZKnH1jRfYIa2x8LEoGS2Ff-ZhcIdFgEWLDW2N-He2MR-yC7-rDRgbBR6rU_MS-g7zzk4IFVvn2RzYUiXfIxLkWumbiJ-KW_dvIrBFcPf_iMX5eWmgR2S2Li5OptfePFUXWGe0HKAA6aNOEzLfZkGMiP4vMMQ1Sj_AS4M05onVrX0YozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPmRFWgIVq6Gx-W9GUz5MlDrwoXKH5QWhi14gJGpg4NE2Wrgp3g22Ks1DNmEFdrZxDOpXaNoDjMxe3x70VfqYOE8wtQC9yjH66flCozQeQEFU4mSU7obYA2ACSrQ6HZJ1cq9tVGL-AJssBkgNpYdMRcPZm5dHyywErjs7pfyg59L7H_HhFiqYXAt12HLzHKfqy1gy2tXT_GAJ9_X6jbqssg2MLrxZr58XpVnX1mvAkcpQus34b7C8yP68ZgFfxmuqAB-jxNliHnj4a0YGzqW-Nt5er7y7rA05sRiU8qdR1JGiXhiSOK9BAGfLD-d-XNURVOmYEScKz7lIXncBX3MVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVY7_LTg7sXfyxq8rU3Qwd6Tvq91Tszec8Khz5eWTXsYCwqmShRm4qxP7IXGojxGQ-gwjN1xwUucVOgtaUpTzCgNlTTJsLH8TUE2dXFg1MWukCouWg8M3r37SFJEmuxlhS4jLHb6SAyMriDMzMsdxw3TszShq93aNDChlfPT2yj4bn3GY2adHxMIe1MQAcVSdWHUavsgUHadqM7vVZj93gl43Y9qtEmOnBWqK19zXefSdpx_40y92ZZ24XeTtcft8OoGNcqMflc2q6XkKG7O6D5J50PVV1t2ibxL10F-bZ5mmk_UzmzUrXoocroguPfFh03tPG-ayiypK-iwk3oHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWWm_3glqPoi85u9ij9_H47XrOEdAkuqL6edECTATazpiy99vwf4d51aII2ZgHlaLeZDbNYqjZkG-fMWqd9wiwuDCk3LN8Y-iDzHM50GOUYsC0toiK4nJSwKpx96etgB61pxjvbaaeMfeLpXAEDFc0w5Tv4mfuxnGisaF_GcICOT32LGuqBkHPHpxzo7_pTkO92m3snjfltcIljSJg3DjLEAHlmixqficWWKl9M5iEDn0ylwOnwfMYi860rVaAltD8GwXmnBg6j2noBKDLCFd6UZgTftpeceEuGkdl9JKHLIG75OaGIsHeYZ0JHAbQtWp4agPMvcqWtV8RK4BbRyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCN-PcjiWJcphTa4rkczsXYRUjw_qqu6zNlRRZ9UCSQa5wY5t2qqH47nBFnpQ89gg4C83PGbTZ7g_ZH9b0F5kZ6y38bg8tno2Aa9JEEmA4yk9G1VAfjr-cqUm6vKrZKRYyPR3QKw8v5rXhEQOZGlINIFfIlYW-6_PbmDvpqmCDbUGMTM4wGDw0EEJK8zVLOp5Kqx453ra8qaYpazJ2xvCxR69eg-uQeYB4NgqOpakQ0kUraCZDcnSJNprt0BQNSqXPeiIhUnQak7I3jCEXTlw9huNI09RG3NH9Eqox14aLDE_QuUNl6atEOShLO8XVkPKW7IBobBwCVbq0oFLbxQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quRNbDtgUhU577yXUYqCYLfnI_uDc6dr-3o4cCWPlv9FkFN27kaoxM38ZJL_TT7GFkKHgYTptk0ANqwVNnboU9X3uzvmsciZcxeygyrEFWH93c63OKp7I1pV52TLQeOhq3XqHs715DajNw9bnzQ4xuiTNx-yzzAnjSaAI6tEcGehSLuNv4F-k-ZMpzqWFZwZWJQH5348uje9r1c7p-RSxn5Y4bQQ73UUvfM4_9A-JSqcVQwyI_gTNlZjClenjj20HPu0OPwOjIPfMbQBTXRejsfT-Ae-o8E-LmEA8CDoLSieylKz5Mdhl6OP4iQlUl9Xuus0dRjNZFURggmqSCYU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMPYz4-i_z0VS0bXzw6aAFbZLw5TmsJlwdjF8prziskVARWgsAsmuPRWWhMJVPu6Xfy9S0V305YHxMCbmTAM_5gqWhf1NymK5HrUNtThvyLvp10TgzUcHyJR-S1Z7XpBvI3x3h1ca5EkmOzcoZtLbucw-MqWzoKuT1Kc9cZOYf_9eN8W7mgrDTidMWSMQhgXIJEkuB6kLamse4Kp4EjpEd9alDLI5BtdFtZQ7tyUlSy99GEMzIgOWWtG3dQQa7OD6uZ1QvBN6ng1Atq_gOQyR4ILONN7-gfMw-0hqDGXgUACzjMlyxHsqsgcpTv5Fvag46v7IjoDmh6wCAr__82zpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLRp1U0dYR3VpJz5ge18AAVCpJMron1ZxzNsrFLO3rOAhYLqLfWgN7YqeaJtLulA-BoixqTtnJhIB2r6-a3YIRi6m8Sq6vUThPvZhUtcS4XbHNi68SjEFondz7cTD1cHuHEdOx6t1bBBA98ldR54K2ZM3lKmHO1nrzzMZ966x8WlZqv1aH8wEqxYdvIxRFZLc_Bl2JaE-bx4yrARx02HA9xp2UwD777SpFzTY5UTANggjLbDpNkTKJgp5_P1ZmJCcl40UgW9kuFi5o8aPHdyWIVuXCnbTFR2GHqXOdcm0uD0ZTXMX1qK2dDnWKgOa2jCc1BdfJYfQfzf08Pr1GQwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTG8eeixJAch9xnW1WoiHUMM5Fc0Jv_M8nqqUTy_5tPW4U_sDQH_qxDAdMyJYTdI9uPX-fMQIk8epVdqhk2wLOrDOd6_GHAo0xzx-c3vHNc5pF3mOOe6KSV8OLpH2H8xCazK7pIQ8uN-3MAFHEw5EiGeclGCtGO88nW2tCnPHLtfduUH54k38pvxehUDEOVfBv3tMrEa_rmHjggJCQxei5CQSGRPFlbgkWAUiZoU3LeJI2ywaCo2TJaUi8gHDsXwaAra2tjDzBVVJ0-2mjgQEF8OxfFUpMYh--TOqmzVkk6lBIPq_76bspL9m7OyIxSkSDVpKiN679-PxixrICHvlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم وداع با رهبر شهید در مصلای تهران
🔹
عکاس: زینب سادات اسماعیلی طبا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/666251" target="_blank">📅 11:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666250">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
وزارت اطلاعات: انتقام خون قائد شهید و شهدای مظلوم را از جنایتکاران آمریکایی‌-صهیونیستی خواهیم گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666250" target="_blank">📅 11:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666249">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkHwwJExQghvYIC7vHtbcIa4bdwGWZO0YlZbXSmnqJBz3PVFHeuZhrv0q0Wx0Mwsv2gBXVsSb2_BWCRUgdtUp_ROKPfEbV4fLRw-7D4uara-jSibwjBUDmIHfP9oZgIL9bmuEcFPuPEb9-ay1HTtIaIupu17N52BCW_3DE3eIJklP6k1zlqrbSMWuBmrkLQy_bwJ-QSu9z7Ve-XFhgJvB1lshrSpqIoALv-DMEaifM3PUpB_6AKGqp66QnkXEmHnEqCdMcybvhC5-iQ3bc3RbpWHCNBSuv-TLtarnyR2pllPXgGHsPITeR7fZK_3z_2bOV0Baa-hm0UvHvtXzCEp8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان اقامه نماز بر پیکر رهبر شهید و خانواده ایشان اعلام شد
🔹
فردا، یک‌شنبه ۱۴ تیرماه ۱۴۰۵ ساعت ۶ صبح؛ مراسم اقامه نماز بر پیکر رهبر شهید و شهدای خانواده ایشان برگزار خواهد شد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/666249" target="_blank">📅 10:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666248">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
امنیت عراق: در مراسم تشییع پیکر شهید سید علی خامنه‌ای در عراق، منع آمد و شد اعمال نمی‌شود.
🔹
نخست‌وزیر گرینلند: ترامپ از الحاق صرف نظر کرده است.
🔹
۵ صیاد ایرانی محبوس در پاکستان به کشور بازگشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/666248" target="_blank">📅 10:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666247">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_Gn2U16ouEyFNEauvuBwHKWxVfWCG02nJh4YWwcZypIry0R5OTrtibAxUlyNmZDgjXwN5mBPnbyAWoJIxqkZGRV7QBmOHpmRX_X2o5LPMoD8UZlWK2Cm38R7OnI3Ocj0YowjpeSe8v9UILLEqcwu4dw3nnUTQE0c_UVRF9EWGZl9fcsRP4Wpl3Xc83HbXECYX9TNuaugTsPaes_-YsmXunfb9bo1VkB4SnKqdwGPcdOVa59jHmpkUjQBw_kkH9oiTRpVOeICZ2OLJ7MvyWHp3RJ-VVS6m2OOm_NcuyPTlU7-qqIr7QdyGSIYa1_KVpqdYPonq_XH9eulH2Qu88uCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نگه‌داری شارژ تلفن بدون پاوربانک!
🔹
چطور در مراسم تشییع در مصرف شارژ گوشی خود صرفه‌جویی کنیم؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666247" target="_blank">📅 10:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666246">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0sVOfKyqQuxV7VlmX5rbVDfrdcAMXSRDtLnnpXTG9riChI1yte0rlNtrEHaec8eYuMwrPgy1J7cF-Osz58PdU6F1-HPZ_aR-EU6eY6LYSJEuzyoOUB_Sq7x7RQeFnGOeCe1ESn-GFYe46M-aI4hwW9Facu8Y8lMIbpk4vr6eFBqpMJd69frzJ7mrKjR2z8EQtENaXtVysP_-53S9aYRl98UkX0-cTh8maM_Uz4oXbhrOvdFmY6asrsP-sQUQg6sSBbxth8G2_JEKhKm8QBLhwlqbXyamq18uZL80JWQ1fm5rDMYakCt3GiukThSEiVT58MKksfsQlMiUz_S8a_Whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666246" target="_blank">📅 10:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666245">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تعطیلی سراسر استان تهران در روز سه‌شنبه اعلام شد
🔹
خبر تعطیلی شهر تهران در روز سه شنبه در حالی منتشر شده که پیش از این سخنگوی دولت، شهر تهران را تعطیل اعلام کرده بود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666245" target="_blank">📅 10:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666244">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3me4_gHd9xRORO5vKVNfdDwHcnX7uRWWRjuFAFbp9mCh3WwBpQpugI63ctmP4j7jIQpXJwNrp-gVjDEkTU7QBPaE6xhmbAgclRx-zAVZIzHAfByDTffs-DX1ZvTAiaiAlG0HRoo1xQxB1-qaIhy6S_DwiO6kd6fcxBJvi2FRvo3KRfRXqRPe6EU4CdwtJ82KNgHjJ0HPlvPy7186q7daLrUJC3qvEDWEV-BV-up9JkwhHkw-pJbBeF97MzBiNXhSjRVYvZlBJka9zTm0Y8yX73e-lqMpUzDpAsC7rkMdhdm90YXfvesRn6bXlwSnW3a-CQu7rJRB9y1KP35ky7ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری که رویترز از مراسم امروز در مصلای تهران منتشر کرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666244" target="_blank">📅 10:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666243">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR5nTPX0dhwbIRF-4zIuJT9XOQXBgOjib_C7OkqVI-Id4LD2mO4wkWavgqcQFOw2DAraMqpiff2WFIVZiOh3iwB4jGkGMljp18c5zwZ1N8gIaR6Zcrkj4VtPp-c0OxbnI8TceXnZVHC2sQWsWCeBFtJeRpzdJ1jBBw2_meMX7t3xOf5Nw3ujkRwXx89p7j1dx4pdcopE2SRjmg8-fwqiwgYfWlXZheJcMqFQpA-pdlxtRqHQKHF9SOMwlLBhZFSkCswy2XEXgaJ0PHHPf5P39AhYxjEmYlbCuT5AaeHa69NpgRfsXlWbXSWASrqJjF5FOlc6m2v7qdMD7mqtLkIqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تی‌آر‌تی: عزاداران در تهران خواستار انتقام شدند
شبکه TRT:
🔹
هزاران عزادار با حمل پرچم‌های قرمز، نماد انتقام، در حیاط مجتمع مذهبی وسیع مصلی بزرگ تهران جمع شده‌اند. شعار «انتقام، انتقام» در محل برگزاری مراسم طنین‌انداز شد.
🔹
مقامات ایرانی می‌گویند انتظار دارند بین ۱۵ تا ۲۰ میلیون نفر فقط در تهران طی سه روز آینده برای ادای احترام به مردی که سه دهه و نیم کشور را رهبری کرد، شرکت کنند./ خبرفوری
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666243" target="_blank">📅 10:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIaX3ZzeuMbsAPA11znf9T7gZ-l0RKzEcaDEet3lJEw8dis8ZtmACf6xXYbg-pyNC-FUbpZfyn8wZPsV0zXRKk-QTZCuEiCKhqOuBaubtuovSgCJIRGyE_Xj2jJlZltqmTebEuFfvQp8_0jXMLNrzbadStUxoQEzJLIdlQHi8eT3OtN4ExYSbhvg7aF8N8Q0bptLMwGrCmCyT3KovVC1k4gemxcJjqMARVsSOCOcTPP-q0TDTPCSjoRb35ukKM9UViA7qw2XF_RLLOhp-ODR_TTzurKIG-R8xaZJsO4dXxgcNJo4Qf3-4ky4tR7byffFncLZf2qYAxZ8BPU-lBmDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم منتخب مرحله یک‌شانزدهم نهایی جام جهانی ۲۰۲۶ معرفی شد
🔹
در این ترکیب، نام ستاره‌هایی همچون لیونل مسی، هری کین، کیلیان امباپه، مایکل اولیسه، میکل اویارسابال و ووزینیا، دروازه‌بان تیم ملی کیپ‌ورد، دیده می‌شود.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666242" target="_blank">📅 10:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6afe047d.mp4?token=BEC__lbzVwP2Cp3uOFS-dAKYmVFueYX19I6VzzFKXaw0Mg5Hx7z8y504PTN4zsStlmA8cM1zXFT8XkiAphnvnMP4o7pfU8ZTiv5cb06U5YaZgpS5JgnNf4SoYVjJSwR0yBQE9uwoJJP-lH4YhojHUjSeoRBz6JEZ_HEq3yLKc0HHEqxZi_Rntt2bKXmcey1YC9Y8ANREwtm3ivuYYyEOimowmlrFE5XJby7XS-_aEQ_h04kTE3YlyGMLEDlF_4LalbRNw6DhUX2-FCgNmNAKllYWKbx9ogs2Vk7UXgUD9puZX0VHd9_dcN9r9GzWECRcgAIwAuHSuxGm73U8Im5YIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6afe047d.mp4?token=BEC__lbzVwP2Cp3uOFS-dAKYmVFueYX19I6VzzFKXaw0Mg5Hx7z8y504PTN4zsStlmA8cM1zXFT8XkiAphnvnMP4o7pfU8ZTiv5cb06U5YaZgpS5JgnNf4SoYVjJSwR0yBQE9uwoJJP-lH4YhojHUjSeoRBz6JEZ_HEq3yLKc0HHEqxZi_Rntt2bKXmcey1YC9Y8ANREwtm3ivuYYyEOimowmlrFE5XJby7XS-_aEQ_h04kTE3YlyGMLEDlF_4LalbRNw6DhUX2-FCgNmNAKllYWKbx9ogs2Vk7UXgUD9puZX0VHd9_dcN9r9GzWECRcgAIwAuHSuxGm73U8Im5YIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آرژانتین در یک ماراتن ۱۲۰ دقیقه‌ای به سختی از سد کیپ ورد عبور کرد؛ گل سوم برای آرژانتین
🇦🇷
3️⃣
🏆
2️⃣
🇨🇻
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666241" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99a04365ff.mp4?token=GtA77zTcihsMNUnjaD_IZuZNb05bQmh9nrAkR_U5rX6ya-QQqlTzlWbOftdj1XGHOaG9QxyVDZ6AAnwfYV7gui8tRXb7ET1vCehV3vEaoS7dgc213JrW-bkhY_BjB2yxAoc4aZusvELuP8fNFR5y_OjHp1JBEv3jS8GTgQFPDjaJtg0F7Y0g1iLzdqaPCOqL-qd-rmORLmAsRuuAbn-BQpMN8HS5bAg0Ox-9UF9YbEZjAkpCQfaqhPbcuz0TDZjMuhI8dOB_8hLyhpB8r-0sKkFYlXVpzi1H7TK-1Id22VyxLHvgLT8K5StOYlraKZC1YzeY9bLbhmbQ4UM6y_z3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99a04365ff.mp4?token=GtA77zTcihsMNUnjaD_IZuZNb05bQmh9nrAkR_U5rX6ya-QQqlTzlWbOftdj1XGHOaG9QxyVDZ6AAnwfYV7gui8tRXb7ET1vCehV3vEaoS7dgc213JrW-bkhY_BjB2yxAoc4aZusvELuP8fNFR5y_OjHp1JBEv3jS8GTgQFPDjaJtg0F7Y0g1iLzdqaPCOqL-qd-rmORLmAsRuuAbn-BQpMN8HS5bAg0Ox-9UF9YbEZjAkpCQfaqhPbcuz0TDZjMuhI8dOB_8hLyhpB8r-0sKkFYlXVpzi1H7TK-1Id22VyxLHvgLT8K5StOYlraKZC1YzeY9bLbhmbQ4UM6y_z3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زن اهل کشور بوسنی: ما پدرمان را از دست دادیم
🔹
زن اهل کشور بوسنی در مراسم وداع با رهبر شهید ایران: ملت بوسنی تا آخر عمر مدیون آقای خامنه ای است، ما پدرمان را از دست دادیم و اکنون چشممان به پیروزی و قدرت ایران است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666240" target="_blank">📅 10:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2601907e81.mp4?token=CkiVd_J8VpG6-Ci-37LEozs2UU6W_0Wia-k6bbbjWgXk4UPtaHqYdH4JRaRBLcy3IEAhfUpBG6YOKuppvjsGILLQoTBpvsExwErMem8G2nK8KbqT7oFFGaorB--WMdmcUuWxouMZDSfgWyV0GyT3Hpv_AMQ5PmBls8jxAEFSmAVM3xShysn55MeZSYFAq0tDP1rcu6SEwxl0cIl6VrcRCBZQJSiVunFGYs3R6znTAFfxtghNVxh4w6MOMKuZi7i562r5xTIOdmDBhJZunm4fmnWYxCxCxCvzyTYx2G7lPGK-oyt5RS_lItBzTEdfvJZKo1aPyCKqe98SxV2qJityzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2601907e81.mp4?token=CkiVd_J8VpG6-Ci-37LEozs2UU6W_0Wia-k6bbbjWgXk4UPtaHqYdH4JRaRBLcy3IEAhfUpBG6YOKuppvjsGILLQoTBpvsExwErMem8G2nK8KbqT7oFFGaorB--WMdmcUuWxouMZDSfgWyV0GyT3Hpv_AMQ5PmBls8jxAEFSmAVM3xShysn55MeZSYFAq0tDP1rcu6SEwxl0cIl6VrcRCBZQJSiVunFGYs3R6znTAFfxtghNVxh4w6MOMKuZi7i562r5xTIOdmDBhJZunm4fmnWYxCxCxCvzyTYx2G7lPGK-oyt5RS_lItBzTEdfvJZKo1aPyCKqe98SxV2qJityzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم کیپ ورد به آرژانتین توسط کابرال د
ر
دقیقه ۱۰۳
🇦🇷
2️⃣
🏆
2️⃣
🇨🇻
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666239" target="_blank">📅 10:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666238">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b799a87d.mp4?token=vWA2JtQJPNtuvxUh08m2zZk32DaTcC0yGttJde-Rr02g7rliw_6VT7m8K6TKG2QiwTWgsfq2S7Ylh_wxN5JHcZhUbYpdNidgmef511uvKl5FHc4PUnkcW_VfH12iFZpZMd_3hixb5Eb_G1MMNrEPqmPDEvtfQ2By2BX2Fx66qv8olFi4erAB-VZWRRgBcmdN9fH5SQv-SDCreZnWk6-L8fXtPpXGoq7IGhoz50mHGofgjMz_gNI0FNX_RTOWp3Ua5JpyEwNnma818Tl007zgvRE_fh9YII6hv-1EYDOmIVFI6neuFU1Gk02VJ3mtwqHxCaXmUgTsGl_78glzg49Hvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b799a87d.mp4?token=vWA2JtQJPNtuvxUh08m2zZk32DaTcC0yGttJde-Rr02g7rliw_6VT7m8K6TKG2QiwTWgsfq2S7Ylh_wxN5JHcZhUbYpdNidgmef511uvKl5FHc4PUnkcW_VfH12iFZpZMd_3hixb5Eb_G1MMNrEPqmPDEvtfQ2By2BX2Fx66qv8olFi4erAB-VZWRRgBcmdN9fH5SQv-SDCreZnWk6-L8fXtPpXGoq7IGhoz50mHGofgjMz_gNI0FNX_RTOWp3Ua5JpyEwNnma818Tl007zgvRE_fh9YII6hv-1EYDOmIVFI6neuFU1Gk02VJ3mtwqHxCaXmUgTsGl_78glzg49Hvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام‌هایی که تهران از مراسم وداع مخابره کرد
/
از بی‌توجهی به تهدیدات اسرائیل تا بی‌اعتمادی به آمریکا و آماده‌باش نظامی
🔹
گزارش الجزیره از حضور مقامات منطقه‌ای و بین‌المللی برای ادای احترام به رهبر شهید انقلاب
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666238" target="_blank">📅 10:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666237">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ba57b304.mp4?token=MognXGS-H4R6qipVd4dX6tcC_EvfaTOa_aHo4qWPaVH9YS6H8GEtwSTDebQMwbZD3ClvdZ4ndOSEQVEak0J7bUSMXX_bgDIOxLL4YA57Erhm1dfyOW1KDbYM9swmOwzOIRRddL3fAIQl0T2hiLgdZ2OYYCaPiEp-0dxqsGNH7394K3CWMGUWXhK3-KTjb19QrVoRwNScse1pcD4PQMJQauzeOXggdz1agJMWr-1Lne4yBkvxHU5Sehi_87zEtFR50Wpv7Mpxjz38OGjYstr3YKSyPF1l1mPU_eM81drRnG80QT7Kr5ypqcUSAfpWR3GunoxoGu6Q_ooKhWkGhZf83w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ba57b304.mp4?token=MognXGS-H4R6qipVd4dX6tcC_EvfaTOa_aHo4qWPaVH9YS6H8GEtwSTDebQMwbZD3ClvdZ4ndOSEQVEak0J7bUSMXX_bgDIOxLL4YA57Erhm1dfyOW1KDbYM9swmOwzOIRRddL3fAIQl0T2hiLgdZ2OYYCaPiEp-0dxqsGNH7394K3CWMGUWXhK3-KTjb19QrVoRwNScse1pcD4PQMJQauzeOXggdz1agJMWr-1Lne4yBkvxHU5Sehi_87zEtFR50Wpv7Mpxjz38OGjYstr3YKSyPF1l1mPU_eM81drRnG80QT7Kr5ypqcUSAfpWR3GunoxoGu6Q_ooKhWkGhZf83w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیش‌بینی CNN؛ تشییعی که می‌تواند بزرگ‌ترین مراسم تاریخ معاصر ایران باشد!
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666237" target="_blank">📅 10:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666236">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c2d402b5.mp4?token=jZB8l5qkXOw-qXdLUA8pwyr4Yd1g13JbbOGNuN40jBu0rMj3wLEakOYYrxgyHKyu7NHtfghrfDqe8g_tF8CoakApmxlKIpWL3RYDCrIFdIUZWiIxms2iJBnjVIifJwZmkG9ee453fYPhr7kZpKTb30aCPJGB8qhtDilrmnerYBvU_T9hejAHfDMiDtM8ed7gEV2hVFJvY84YfCoWfUN0LODbNIS2pe1HuYnh-y4qInqbV9cuBjqhYSNridMj5r2eNcEC0AOMVyHE3sbXWbA_6UX7ev5inzY1MgT0kagnOIvFmFVBnCV-ymXDn7z9EobrHwlPJjb8vsRY32PERYaAWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c2d402b5.mp4?token=jZB8l5qkXOw-qXdLUA8pwyr4Yd1g13JbbOGNuN40jBu0rMj3wLEakOYYrxgyHKyu7NHtfghrfDqe8g_tF8CoakApmxlKIpWL3RYDCrIFdIUZWiIxms2iJBnjVIifJwZmkG9ee453fYPhr7kZpKTb30aCPJGB8qhtDilrmnerYBvU_T9hejAHfDMiDtM8ed7gEV2hVFJvY84YfCoWfUN0LODbNIS2pe1HuYnh-y4qInqbV9cuBjqhYSNridMj5r2eNcEC0AOMVyHE3sbXWbA_6UX7ev5inzY1MgT0kagnOIvFmFVBnCV-ymXDn7z9EobrHwlPJjb8vsRY32PERYaAWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به کیپ ورد توسط لیساندرو مارتینس
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666236" target="_blank">📅 10:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666235">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwLU9CBRgx3xFovO7ZxrIhklBGSWFsA9oqN7CMGVwqbimKZ_-mCSXi307yMOF_32wYKYi6LOFvhwlJi0lITXNrbpwJWBiNzk9y4ZdlkQlK0vb-FEhBqsvYWnxIrEZCl86pZ5Qr2a8mNA5lzj3PQKSwZT7x6LBtTrkIFqN6aJ9P1JC-wRfA1O4dr_PQMyJU6SKeUfKrxvNMmXfy8syaKJi7McDDvTwe4i87903-34j_gXSvf41cWBNoZ5DLb0SCZQfasD2E0QlIoRMHW2rRaRHFkWtcDEPSN0t4JHTitinfs_MfNdLOcjUMy9HBfknBO3f_5_-ku6DYh9DB6NBA22sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار غریب آبادی نسبت به هر حرکت نظامی در تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666235" target="_blank">📅 10:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666234">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d5bfdddc.mp4?token=rW8zjAXfgFh18f8bmTBe0GbKTyzdK1xg7DdpPmS7cptEQ4A_Rh3LMbhbCzwYkT4q2n9_Rf_9a8YRfi2g0hcRFwYGjKbiz95PZlPMamyJeX_QfuC4S8pSTNSxOIBfyHWmPH2pWKy4TURoV5o793_zaTP8r10jzxgvNgHSBRF1lVrbjbT85-kAw0IGYVfV1CGIkNsbfL6Yae7z-A1E8C6kPrVa5AqkjiobGifpC7KtTUGBr4hWz95c7kQ3DyfWTEGJpZ3i1Gtwig5WFV9YtDZI2X9Zy_8OFq22wsOHrJykfO3FB8QF-V2xUFDaIr35hfv4qscDBg--p8Jtm9o4KY_DIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d5bfdddc.mp4?token=rW8zjAXfgFh18f8bmTBe0GbKTyzdK1xg7DdpPmS7cptEQ4A_Rh3LMbhbCzwYkT4q2n9_Rf_9a8YRfi2g0hcRFwYGjKbiz95PZlPMamyJeX_QfuC4S8pSTNSxOIBfyHWmPH2pWKy4TURoV5o793_zaTP8r10jzxgvNgHSBRF1lVrbjbT85-kAw0IGYVfV1CGIkNsbfL6Yae7z-A1E8C6kPrVa5AqkjiobGifpC7KtTUGBr4hWz95c7kQ3DyfWTEGJpZ3i1Gtwig5WFV9YtDZI2X9Zy_8OFq22wsOHrJykfO3FB8QF-V2xUFDaIr35hfv4qscDBg--p8Jtm9o4KY_DIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سی‌ان‌ان: مصلای تهران غرق در اشک و فریاد «انتقام» شد
🔹
رسانهٔ آمریکایی سی‌ان‌ان در گزارشی از مراسم وداع با رهبر شهید ایران، مصلای تهران را غرق در اشک و فریاد «انتقام» توصیف کرد و نوشت: هزاران عزادار با سینه‌زنی و شعار، پیکر آیت‌الله خامنه‌ای را بدرقه کردند.
🔹
این شبکه آمریکایی به‌نقل از آسوشیتدپرس نوشت: جمعیت یکصدا فریاد می‌زدند «حرف ما یکی‌ست؛ انتقام! انتقام!»
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/666234" target="_blank">📅 10:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666233">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b28c8fbce.mp4?token=TRNspOQL33K-Y3B1ycxXHzkvZaNtZfi69YBKKoZ5VPyOYnUYnyQiM6GcS_n73AgLy3srtp8Ex44N_Zk0l7WablnqoSiU48leDeMxsY7Mz3y6YO-FH8QCmgYaTPKf3jm_o-JvqWBwVg6Cp0_A0q725sa6x49CWxKyd51RSySqRQpzaqeR9R-lU-rDpHQjnWSLIdUBvXHU4zZa6OVdrdQwgfvlvS9qfBUuPqe7daP_6cdcghf8WdNAfrFcPqUUUoFvGBIs9ssRXWzFl894VPvjwH8z7uIvHjv6u5EhqcXBPysrkplD6PQZ0AL0lsDGPT-RbVo4ZT5x66EHvXJmCxyrLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b28c8fbce.mp4?token=TRNspOQL33K-Y3B1ycxXHzkvZaNtZfi69YBKKoZ5VPyOYnUYnyQiM6GcS_n73AgLy3srtp8Ex44N_Zk0l7WablnqoSiU48leDeMxsY7Mz3y6YO-FH8QCmgYaTPKf3jm_o-JvqWBwVg6Cp0_A0q725sa6x49CWxKyd51RSySqRQpzaqeR9R-lU-rDpHQjnWSLIdUBvXHU4zZa6OVdrdQwgfvlvS9qfBUuPqe7daP_6cdcghf8WdNAfrFcPqUUUoFvGBIs9ssRXWzFl894VPvjwH8z7uIvHjv6u5EhqcXBPysrkplD6PQZ0AL0lsDGPT-RbVo4ZT5x66EHvXJmCxyrLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول کیپ ورد به آرژانتین توسط دوارته
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666233" target="_blank">📅 10:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666232">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8bed2b7f.mp4?token=Z8XgCK-MHk3rDPZCe_eQvC05gPYmYKRoTXUreZJCBKuvV54-rCB9l7WDmeDBlhQL0bjZs6WT6s_6o9v88ALmtw3XM_f8uKDGrGSzOHa5orDBHkt_4UQHMSm54qDt3leBYigY_P2oDyWEcR8yIY96gxwGAkQDeYiXjNDgi5SoDnYUHOy5Y9CGfy-K8n3vSeSNwfvDnnrxDKtH-TD5XxBrY5AqV-vOyp0J4sUiPHhHEIHyPdB0bGKHchUXVfiuGZ3pXixjJzpFz6015w-mvkgpxcXO4EEfx-gfVgDK3frRw-zi8zjtMgT-H1_-5gZSvemTITEiYkk-AVjRQ9z7S55y-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8bed2b7f.mp4?token=Z8XgCK-MHk3rDPZCe_eQvC05gPYmYKRoTXUreZJCBKuvV54-rCB9l7WDmeDBlhQL0bjZs6WT6s_6o9v88ALmtw3XM_f8uKDGrGSzOHa5orDBHkt_4UQHMSm54qDt3leBYigY_P2oDyWEcR8yIY96gxwGAkQDeYiXjNDgi5SoDnYUHOy5Y9CGfy-K8n3vSeSNwfvDnnrxDKtH-TD5XxBrY5AqV-vOyp0J4sUiPHhHEIHyPdB0bGKHchUXVfiuGZ3pXixjJzpFz6015w-mvkgpxcXO4EEfx-gfVgDK3frRw-zi8zjtMgT-H1_-5gZSvemTITEiYkk-AVjRQ9z7S55y-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به کیپ ورد توسط مسی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666232" target="_blank">📅 10:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666231">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4mZ_kkt9pxVur1rCFaX4p61jWhSYqJIqlVy1HRa2BnNpoyPZX7_j3cO1JtJNwYkmRJjZ8jOTkP4uledukUCt4iGXqTuv7Y-7CS1S6Nr0Pr8DwztridM7eRBcss8uc9Ugwe7VxHfDJphmZM1YGqM9z4_YGgRmJbjFB8YuyB3JI9GjjE9AcFEvT9Wie7r923GVxIB13-gfHIBq4Rz9a_1ancuMU3UKlfyNqJyCljTQaKMDmU9uo_6zoSh3LIm60CF4rwYXRqVKUWIG57Iu0wNHj6NVgdPgUcZAdpB5L0PhFd8HGWw_LJv257oa0axjvxPdGXuvkTwpwNuBZHPp59iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیونل مسی به اولین بازیکن تاریخ تبدیل شد که به رکورد ۳۰ بازی در جام جهانی رسید
🔹
یک رکورد دیگر به نام او ثبت شد و هنوز هم ممکن است تعداد بازی‌هایش را افزایش دهد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666231" target="_blank">📅 10:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666230">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeBSh_WaGxhLHCIo9t8EkETAHsZpQCFWrzXbm7mnQ08AOY0EGLZYIiktecFlK1-aDZWfgEAcwhe0cF_mASIV2lkvrefRQ-gZlMRBuEWQhOFMe977M4BnvM5kZzXmrTKEkKiPk7Tz4WACi_cgOECEpHmU-cKlPAeAEl7g4csbgqfKlllBrMw-WvMwDcg23QQLEVdJ83BNHwbMC13pV1WPJ-lNvUmVzQQIXOKsW0ZCtyXfeD-IEc3hmC8AWM9_MwpGqj9hev98MTH7_lg7xpkI-dsx7GAZ-cAH8Fus_t_YXTSo9a76l_DZxHTz0O2_C1LPuIMblTuxvg_7nJzQlEENtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موفقیت شما بیشتر از هوش‌، بستگی به افرادی داره که باهاشون بیشترین وقت رو می‌گذرونید #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666230" target="_blank">📅 10:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666228">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
بیانیه مشترک انگلیس و فرانسه: عمان موافقت کرده با بریتانیا و پاریس همکاری کند تا اطمینان حاصل شود که آب‌های سرزمینی تحت حاکمیت این کشور، برای کشتیرانی ایمن هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666228" target="_blank">📅 09:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666227">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFyL_71i-LRduc0jJTwY01s5hM85unn_KBzvxC4NinLwbPA1vHICn1KlF8lIx8rTIdxKlnOhFXzJ0rrzEpKPhA9sKPJrnarH7LUC45wa7KM_8n593D2l7ijxFvDPBR2M3ZkngVzkVXmuAiv1na4o0J652YR4kYN734nS5JT8WlTysYa81yHZ7R_IRkiAzAqEHoDKZHxdE6XpMiPjDOKkclNYpTQM23QDLO_AsZDDiQu-cqNb-wMhAe2wDNTIZV2Ym8k5BI7mF00aYurexbjpeMaYDSqp58vIb4DomWOzjgnrTZK_DKKFFMwATi4Lbs1BlTJNqRupxvQdy-vr4rlp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تابستان بجای آب، این نوشیدنی‌ها رو مصرف کن
🍹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666227" target="_blank">📅 09:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666226">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2a46e92f.mp4?token=b75SW2rvEbEhJ45v3PfjbnOG_Fag5FWQY_RTn_30RYp1MrRvZWrSs0tc5cRjIVk8ZWAsXeBipZFlK5Yr0nyE05JwMdBoy-MnGK01CZNKS11Akfhjq3Sc_5FcY-nnPTpTO0Y59CtFF-ZEvDdqYnu6v0WXeNHzlo2QFvsadN5ZJfjNUC_ggxHBum3tEoJYcrAXS5Vfb0L2eXXkjgE1c0AfBezLv0oRDeZjwVsocd4nf39yeo1UAnDapTyKRnJwwyiBhlWwwFsihY1Kqq5L9-_pj9bC6zNtm1-YHnZT4Qngwb-qdYo82P3Yz_tVekbEonARbLE0b-RmEVCrZQ9XkQHAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2a46e92f.mp4?token=b75SW2rvEbEhJ45v3PfjbnOG_Fag5FWQY_RTn_30RYp1MrRvZWrSs0tc5cRjIVk8ZWAsXeBipZFlK5Yr0nyE05JwMdBoy-MnGK01CZNKS11Akfhjq3Sc_5FcY-nnPTpTO0Y59CtFF-ZEvDdqYnu6v0WXeNHzlo2QFvsadN5ZJfjNUC_ggxHBum3tEoJYcrAXS5Vfb0L2eXXkjgE1c0AfBezLv0oRDeZjwVsocd4nf39yeo1UAnDapTyKRnJwwyiBhlWwwFsihY1Kqq5L9-_pj9bC6zNtm1-YHnZT4Qngwb-qdYo82P3Yz_tVekbEonARbLE0b-RmEVCrZQ9XkQHAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو رفتی دگر ماه و آیینه خداحافظ...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666226" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666225">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
انا علی العهدی
لبیک یا مهدی
🔹
مداحی محسن محمدی پناه در مراسم وداع با رهبر شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666225" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666219">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8b6eak_Gq-MmiH7f4ZItN5zF90EZVKAAeQKvf3nmeaEGK7klpNtGwGg653H53HKpMnMAQrSlpjIpYBLtQ0k3V4u4bLCz8yRigBglJ2BLdeobCfswi7YP0_y24SQKYfI0WgA7li_aLuKDyNYhgJl8lS87_Y2PPgJy-guADj5sdAb_XYuZ_7p3N6GTvf2p5PZG7ZsYkTT-XCiaWVathkpFXedrx1XwzMKKONDY1Kk9c0TS57Fy2A1Ts8DoBYK6LFEykfVXkIylkYQTUSHmM-a3gDiwERQ865HyaI3ektFpvVW6Um10ubs86KaQ8kn4wBBhaTmSjB8DPXyidfEON8QEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toLZs8Szia9A_xDSJd13M20bl_lZYDTc4wlKR5y_f0bR-jne5qRvM5C8_ohDRcuOiUYBVPNKZ6Ye1Y8rPZCFzHPNELasyI0HXINx1oes16z9g8PGHhVa5zKDaYG2HoDLICEbkHNIa89MNo9c8jH52sdt3ECSi2g-uRorRyS9j9DCZ1-RNkte8G8OjSxLGYH48auJScAzI3JHNXxSQ5Na502izzkG8yGMA63sosyw7T5ZCvaphSEYp195xpXtoEpG1jP19Lu0n7Q4t7vNCZGvkChuyWzKnMMwQu8hHyYRCQqRr_rxhDsVmh_qUwq0VMJ9Mvy1pqHvOPXs0NtOfx9YJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCT8IWTMrNhozRAARJefWMIuL3xAkfaEvdDrK6ailKzNrFg42VBsPFlAsxlnhYPk1ik4Ms3G-3_4-V25L6zh5I7pzxPqX-NA7VxcPyv3-iZaojhGsMG4gbzZaTWFMV2yrVVdefYip2jq64jqzWOrzI9nbFnrfhNusvovs3hetdRHWjYwsQssv5uUjzAbaBlYzdWE7CXbWTfqrXLFWAdWljdbVifI1_6CK0KZO26bN1tDaHx4-0QRL22kN1HG3gHeq0BPAgF2FyWRk0yqdC8XDiTqm5dgMoDDJnGOBXXunxusVynaOeiuCGFbS6iE1vqez4xvOxdeGPtCgkPi1UM6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QB7wml_HshNabYSrBFheZIO0yqciXIzM91s6kuaeIL7SiBUUhZUxp0lfPvaXRKUfSXPBc-20fXp5fYaCDcZ6otCKV0QY_CseDriZWIcUEy3IjIlVNI0Ok1s_Apgsp_fxBvSVrzoIFbwoKLi-55peD3SpabB4zEe1Xf3Sx1kSmb6TrJmF9MVsGW4vud6n_R4ZJItnLteHdXzxfP6Rhwih_13rQ-NBTp43zfRbQNAWXMH29JSz4cJeOMs4yPhT5sQlJ8vUUFaiLfzKCY2j_DkZ7ik5xIL2CLxcFsXy-c29zP14N7fpNwJ4TOy6jCeGHF5eTZMEwaldwyKLP7M1mAOKMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d98adf9726.mp4?token=BYnKTwvSJ8XXHefJnONAK-Y-zVtfoPWyUNbj_vDJFkKR9PIK0FtZZHMNcEjxDRaMUuRQmdDf7ghzcWbrRZfiitD27jDjVlM6P-hvM9x7YDduwXxiDPGqUNStyhl356e7L7LDa-1WzY15RSbaz8WBA7Q0KUTzi5pFik_Jw3auAE4Qd1PU4CNSLJg2GNRql5NP_u5lSRYAThp5NZSHIsluky0KTaAHNw8N6vz1hW31Hs8MN1upwmyD6sctIhQRI3QpgaW43bIyX9Wphg3swDIVqFYdfqMZNITeGCm6ma_6sCgqm6KY3CbKeBWrVqmirNM4X-6BIUegVsgMpihkAe6Llz7f7aNCCZZcLvQbKxB1TFARvg3Rq6Gg4GmvC9n7dHTVB_1FHWOQx3e-T3pr4Cd-GDEclI26h4-4QRJsOJiubgETY22T_MwM-a46ZUN5dFUiseTMeRg8SVJXHfIygHUUT9kWeUjWv-XpP1828cLzKfI6ixM49ztlmcaHzZtzb_tRGCDYBczzoblsaVtWwjb4b4RCv2CljM3_gAQ4qdHPGFTWAP2rZUOld2RoqRtAbFtxu8O_yOumrAvU6b6IpdmeHeYdfC-owATKdLX6W3TkZNfHwodEe_CGpE1IFEbrsPGSbdXnfQ3bGz39MxeyZA7IcbDj_UDqPk536Q3gYFxV47g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d98adf9726.mp4?token=BYnKTwvSJ8XXHefJnONAK-Y-zVtfoPWyUNbj_vDJFkKR9PIK0FtZZHMNcEjxDRaMUuRQmdDf7ghzcWbrRZfiitD27jDjVlM6P-hvM9x7YDduwXxiDPGqUNStyhl356e7L7LDa-1WzY15RSbaz8WBA7Q0KUTzi5pFik_Jw3auAE4Qd1PU4CNSLJg2GNRql5NP_u5lSRYAThp5NZSHIsluky0KTaAHNw8N6vz1hW31Hs8MN1upwmyD6sctIhQRI3QpgaW43bIyX9Wphg3swDIVqFYdfqMZNITeGCm6ma_6sCgqm6KY3CbKeBWrVqmirNM4X-6BIUegVsgMpihkAe6Llz7f7aNCCZZcLvQbKxB1TFARvg3Rq6Gg4GmvC9n7dHTVB_1FHWOQx3e-T3pr4Cd-GDEclI26h4-4QRJsOJiubgETY22T_MwM-a46ZUN5dFUiseTMeRg8SVJXHfIygHUUT9kWeUjWv-XpP1828cLzKfI6ixM49ztlmcaHzZtzb_tRGCDYBczzoblsaVtWwjb4b4RCv2CljM3_gAQ4qdHPGFTWAP2rZUOld2RoqRtAbFtxu8O_yOumrAvU6b6IpdmeHeYdfC-owATKdLX6W3TkZNfHwodEe_CGpE1IFEbrsPGSbdXnfQ3bGz39MxeyZA7IcbDj_UDqPk536Q3gYFxV47g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع در نروژ همزمان با مراسم وداع رهبر شهید ایران
🔹
همزمان با آغاز برنامه وداع با رهبر شهید ایران، گروهی از دوستداران جبهه مقاومت روز شنبه ۴ ژوییه ۲٠۲۶ در میدان "گرونلاند" در اسلو نروژ تجمع ضداستکباری برگزار کردند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666219" target="_blank">📅 09:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666218">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj9M4EvhNaGbwpxfLMpeFYYQCd4PCSv0F3jGP7hz5RDpYjhf05AREqCIVU5_I8lvNDKTI7pOty8L0-hc1VOIJaAL0PzH1nD1C363tAKbVkg1VNKX83y2tJgjhgFWiMvEwosBBVyufpJJq098FZjbmt1mQYsjsvOd0V6c4NEA_nzvR9a7dxFZU-rH5TxCVGDGy6eL-kSUX4AlNK8h_oR9pOSm3AiwgM6y5IXgUvhMtzPH873FO4DhOwPBxKfQgRJFO9fODHiVrDiD0DX2PgqGrpod1F0U7U-W7oq6mIE-jBTw0pW4bc1KqIsPyG5PPpQkb_bWPMe1CdsA_SvPDMgKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: قدردان همراهی ملت پاکستان در دوران سختی هستیم
🔹
رئیس مجلس در دیدار با رئیس مجلس سنای پاکستان گفت: مردم پاکستان در روزهای سخت و خوشی کنار ایران بوده‌اند.
🔹
رئیس‌مجلس سنای پاکستان هم گفت: من چشم‌انداز روشنی برای ایران می‌بینم و با پیشرفت ایران، صلح و ثبات در منطقه نیز رو به جلو حرکت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666218" target="_blank">📅 09:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666217">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f01cffa58.mp4?token=NJA56uAZoRYGFJmV9P_MrYpEvVSYbtcbww7ba8tzukSCr-8jL3SaHPMIldK_ih7XxgUkBzzsqw-ueeTWTvJ-XufzA5qS8nlFI6gYLGFOIz2WLvT5Xx8M_G5lNQ10k2G5zlmz_eGk44IDJhZIUNWYwYzAvrr9ezssK5oXgGZZ6U8LdT3W_JOiwNH2gpF-YZfj_DcFYXZQ4rQufZqc1E4mMujmchsWP3MGNQVT8et9VYYlzFYiZL_S0T_5SUzkV4g_ILLFdR1B0qvdj7Grv0JDnEf6CaY0TXmA9NNium9ITThLfPiBj-nBxYqfC362P3L3-L_Zrvuj3khSbV1K8ZaPsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f01cffa58.mp4?token=NJA56uAZoRYGFJmV9P_MrYpEvVSYbtcbww7ba8tzukSCr-8jL3SaHPMIldK_ih7XxgUkBzzsqw-ueeTWTvJ-XufzA5qS8nlFI6gYLGFOIz2WLvT5Xx8M_G5lNQ10k2G5zlmz_eGk44IDJhZIUNWYwYzAvrr9ezssK5oXgGZZ6U8LdT3W_JOiwNH2gpF-YZfj_DcFYXZQ4rQufZqc1E4mMujmchsWP3MGNQVT8et9VYYlzFYiZL_S0T_5SUzkV4g_ILLFdR1B0qvdj7Grv0JDnEf6CaY0TXmA9NNium9ITThLfPiBj-nBxYqfC362P3L3-L_Zrvuj3khSbV1K8ZaPsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت زیبای رونالدو برای پسربچه‌ای که همه‌چیزش را در زلزله از دست داد
🔹
پسربچه‌ای که در زلزله خانواده و یکی از پاهایش را از دست داده بود، با پیام ویدیویی کریستیانو رونالدو غافلگیر شد؛ رونالدو از او دعوت کرد تا یکی از بازی‌هایش را از نزدیک تماشا کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666217" target="_blank">📅 09:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666216">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ade56c25.mp4?token=Ss4mj_hftUYoO2lHP6Jn6XPF-aiQzYGNh4KtLDl--wlTgxm7l1EXEz5DtspIEVG5KlGb0xE0IZvU6S6dYgQZhkBuDSQmAHxWBu-YSqYMZDIZVJeith6oPWpeJKFoJmrcHGkkz6cGyhTe7ZL7OGmekdleBSvjB9q7szSd7GriX8pGjl5Xk2unUH-R3xAPxsmx3JOo4Cy9sc5FMzajVT9KtqUrJvTxMkQMAPwJoS-nXHej-0jSKTvcNLtIKxoB2OxAM2Up5pd-c6XybCYO0o6dDgs2cMJPsy5G0XIxlouNX_3I-BYhQ_UD_dFryF8XOysGi0Q-3rS-iof6m0idT9ZOgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ade56c25.mp4?token=Ss4mj_hftUYoO2lHP6Jn6XPF-aiQzYGNh4KtLDl--wlTgxm7l1EXEz5DtspIEVG5KlGb0xE0IZvU6S6dYgQZhkBuDSQmAHxWBu-YSqYMZDIZVJeith6oPWpeJKFoJmrcHGkkz6cGyhTe7ZL7OGmekdleBSvjB9q7szSd7GriX8pGjl5Xk2unUH-R3xAPxsmx3JOo4Cy9sc5FMzajVT9KtqUrJvTxMkQMAPwJoS-nXHej-0jSKTvcNLtIKxoB2OxAM2Up5pd-c6XybCYO0o6dDgs2cMJPsy5G0XIxlouNX_3I-BYhQ_UD_dFryF8XOysGi0Q-3rS-iof6m0idT9ZOgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رمضان سال ۱۳۹۸؛ ویدیویی وایرال شده از دعای رهبر شهید انقلاب با حضور گسترده شهدای انقلاب
🔹
در این فیلم علاوه بر رهبر شهید، قاسم سلیمانی، محمد باقری، سیدعبدالرحیم موسوی، حسین سلامی، محمدرضا زاهدی، محمد پاکپور، عزیز نصیرزاده، علیرضا تنگسیری و مجید خادمی حضور دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666216" target="_blank">📅 09:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666215">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EicL3o--_zmojIdXWkVoCn0JIOOItbO9Mrst8yqiXeIj70JSHGhDaCY_4cAxq-j2tDm2TozZPNP8JJ1c-nSkiyqFEZB38QEYTdbnwUi5En-3HZRAZim6r4pN9Tw-FMxle46H52CNGbc48grc0sYmGFZWH1MTa0feaxBGTSeakSBGXzSsMD5lwCcFWZ0uBxBDKLGvlIUN58ZEg35RiUosX2RsVIFZCKpzYWNZ2fqQzM_rTpjToIjJTuPYPWcyahL9CF8jLU6bKRCtY8PK9Qxj4PkcFjnOffpXQ8tSvOrJkCyCpxAna28Foy19vJ7djv3LE1C3Jw2TT3J4_q0MBweSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور پاکستانی‌ها در مراسم وداع با پیکر مطهر قائد شهید امت اسلامی در مصلی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666215" target="_blank">📅 09:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست‌ کافئین | فصل‌دو،قسمت‌شش</div>
  <div class="tg-doc-extra">حکیم خیام</div>
</div>
<a href="https://t.me/akhbarefori/666214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
♦️
حکیم عمر خیام
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «خلاقیت‌های متقاطع در کسب‌وکار»، «مدیریتِ فرسودگیِ ذهنی (Mindfulness)» و فرار از «سندرمِ اضطرابِ آینده» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666214" target="_blank">📅 09:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25918ae43d.mp4?token=HtbWoIi1z66DGU95ISmIldsiE6VOn_IAX1m8E9SAH41gPC0jZ4ZTAG05gxiS3Zu4_7ve8Osq47Oclo8ZSvdj1WU0yegg8c3H0g4GkjxV_rVsix8VUy6s3MDwn6Z_jizRLRWD-4NE1SRB_bEiP_pjMQXBYuX2ESECk-gEkeOO3MWzFcQl6wba9HvKsaRg4q46pKcHUrVIgRlnZQ6fi3WUL6DVDBVDhhVzbdtsnY3BWZlc_DTJYGmSz6GPYLQze0W2p2K1tyfrfn2jGdC_ir76qqHiZN_G0dPReD6yxzdXCFRPb7y2Q9d2fCVdhRT4Hjkessro0oxH_NGOx2yo0Crv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25918ae43d.mp4?token=HtbWoIi1z66DGU95ISmIldsiE6VOn_IAX1m8E9SAH41gPC0jZ4ZTAG05gxiS3Zu4_7ve8Osq47Oclo8ZSvdj1WU0yegg8c3H0g4GkjxV_rVsix8VUy6s3MDwn6Z_jizRLRWD-4NE1SRB_bEiP_pjMQXBYuX2ESECk-gEkeOO3MWzFcQl6wba9HvKsaRg4q46pKcHUrVIgRlnZQ6fi3WUL6DVDBVDhhVzbdtsnY3BWZlc_DTJYGmSz6GPYLQze0W2p2K1tyfrfn2jGdC_ir76qqHiZN_G0dPReD6yxzdXCFRPb7y2Q9d2fCVdhRT4Hjkessro0oxH_NGOx2yo0Crv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حکیم خیام و تفکرِ چندوجهی
#پادکست_کافئین
| فصل‌دو،قسمت‌هشتم
☕️
🔹
ابرنابغه‌ای که نشان داد چطور یک متخصصِ تراز اول، می‌تواند از قفسِ تخصص‌های تک‌بعدی فرار کند، دقیق‌ترین محاسباتِ ریاضی جهان را انجام دهد و با دکترینِ «زیستن در اکنون»، اضطرابِ فردا را کیش‌ومات کند.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/mxf2h48
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666213" target="_blank">📅 09:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666212">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
درخواست استاندار تهران از مردم: فقط یکبار در مراسم  وداع و تشییع رهبر شهید  شرکت کنید
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666212" target="_blank">📅 09:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666211">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ee473a0fe8.mp4?token=ukO-U8DRIl93oOmAo5AdRcgpZU47jefLWxK87Ac_EYrV-qt60uVT8VGFJETauRDduM_xkp-d594KLv2KgeUpcQBUzwOUb2wrb3w7bzMCj6-qRGvUa88yUrG0w-aCUVBZyN3L407EsD6DCDp_WAti6ltNUN5CUABYNInYEb8detPXL4JEcMVRK29aT2lw-pyj1JmHATP_r-XdVemFpej_VUHrIFqrtFxT-rwQSFyeqe8wPPecspmhXN1tGzKWUWC9b9YNVIVuFU9P9ca9ZPdd_zQAIOuVpiPJ4ylS8w4G97XfFYXME2ninSrQkj0GBYxV70dg1qISXD67sl27GIP-2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ee473a0fe8.mp4?token=ukO-U8DRIl93oOmAo5AdRcgpZU47jefLWxK87Ac_EYrV-qt60uVT8VGFJETauRDduM_xkp-d594KLv2KgeUpcQBUzwOUb2wrb3w7bzMCj6-qRGvUa88yUrG0w-aCUVBZyN3L407EsD6DCDp_WAti6ltNUN5CUABYNInYEb8detPXL4JEcMVRK29aT2lw-pyj1JmHATP_r-XdVemFpej_VUHrIFqrtFxT-rwQSFyeqe8wPPecspmhXN1tGzKWUWC9b9YNVIVuFU9P9ca9ZPdd_zQAIOuVpiPJ4ylS8w4G97XfFYXME2ninSrQkj0GBYxV70dg1qISXD67sl27GIP-2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما بعد از این آشفته خون امامیم
ما بعد از این زنده به شوق انتقامیم
🔹
شعرخوانی احمد بابایی در مراسم وداع با قائد شهید امت
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666211" target="_blank">📅 08:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666207">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_PJHDvXhB1K4H2Sff9AKE6dOaVi84GFQAHHUGjvMmHaZlorQMkd4v5kVwT0OsEGPs2KjmSJ9lvmsS9c_VGejBLl9Geqw7CV4_-eHBJyEdhi2unj9QiSzsXNgRkPahq6Xv23eN4zZQvRwKZaGAPg6GEKxuVBAD--SirMSQn5iuA5Fxo_QkToLqLnUpE1EHaEHHzO8MXGnLfx5QWdKSUnp5SXj-ijZPXKLj0Kchs5j5OROEgcrXz8TY1z_53V2TvMZy3pt3uF9phFgSjpI22ul3ulBlGluEsJUBChmUFuU6mg3fswH454dIpqTRZIDvYZcMhXU6NEgw4dPqJUmI58Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gq8TXfixi_vjJBp_kXUD7v_pNo2QE_e-B9uDsUow7OqiXVIL9ojCC77aES04cvzAWvuUJsqJPnHxiTGJnBl65CZNY2sFVeuyUfZID4Ncw1SJJzb3S2LibjDCGIWZW66srXfutJoCasHu7yC6fC_ODzACNxWoK0pfRfjZpIgQ_jQqoaKWsHa9lNtQO6B2GU3C28-OuS7TYmAzuaIKyeugI1NFY4QaOt4MneiJko3i91g-Eg8KiuYo1fddgdI35m4EBxAAOdExQkdO7Uyo9AkN1cCEQ43XoUhyB_Bh-AuHfQ3qFULFkmtLhKqTKiy7GzxfjJgkH6G08kkNXasnYZaBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOcBgtwM-CeLMvK7paeG5Cpd9bsr0lVfXfAibWfn1MbuMtlHmShmXaaIbHOnsbPU1XTOx86Xemo_4nzJMZg6SoDqAIvsNLkXzBwO7r5Zz0IxA8QUE-AGkrqC3iNYJ4ZOupSKcTcfkXftu0kYgvcqTnVtStos1rEA_NTTiQfrjrgyMWC7EpAjNVP-1RpuqUUkHFZX718jA6-9EKGIA7zYts7ZnMp2P0AOUsepzz8grPFC63qFl9EO_1mOeiGuGnaUryuw5Rti54E-1X8WqP1y_cCwnuEciNtPEYI5i_fzGQ_DHHAVij_gdZLM_tletgw2Q6jKj7B1Q395lxtBqAa2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzSXwgN6j9oSU_XVYcegDgPKOxkLgLjZMWl60OyjxJQBNnHTVAoLQQLN61YnCPJzOY1OLUpQ08I1ziztIpbf-TefGGbFhLwFORZMu22xLGYZBE1Fm-R5We71yj8-UTikCJ8yaY6uyXXCVldzChKLodwUukOAhzlao7ah1lpiRw7zU61htldokQ4_lnLxLiAme8rlbLDtexeU2UnWaffxdDLDe4Xk5tBTttRC4XTMIQO2sjL4YGLi1VYnulzIWJ62bBTNcdM8x93MVv9XinaeGOCyDy058rI2fT1S0v6Gk4fpSarnWSaDGaYDNaI0QjKxpLOeUf0mJV-83QnZW8vh9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برگزاری
مراسم تشییع نمادین رهبر شهید در نیجریه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666207" target="_blank">📅 08:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666206">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نمایندگی ایران: آمریکا هنوز از پاسخگویی به جنایات خود امتناع می‌کند
نمایندگی ایران در سازمان ملل متحد:
🔹
۳ ژوئیه ۱۹۸۸، نیروی دریایی ایالات متحده پرواز ۶۵۵ ایران ایر را بر فراز خلیج فارس سرنگون کرد و تمام ۲۹۰ غیرنظامی سرنشین آن - از جمله ۶۶ کودک - را کشت. رئیس جمهور وقت ایالات متحده به جای پاسخگویی، خدمه پرواز را مسئول این حادثه دانست.
🔹
دقیقاً به همین دلیل است که فرهنگ مصونیت از مجازات امروز نیز ادامه دارد.  از پرواز ۶۵۵ گرفته تا موشک‌های تاماهاوک که به مدرسه‌ای در میناب حمله کردند و ۱۶۸ دانش‌آموز را کشتند. ایالات متحده هنوز از پاسخگویی به جنایات خود امتناع می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666206" target="_blank">📅 08:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666205">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRYPgysRhMXBfoLF1ItcHRs5Y05qrdHyN06nwrwWvmGQtODViqrMxFeLn1k62hfXv6g0x8GG3KVpC55BsvmxwiejLCiCrhJoniJAjfsEFvQXraq4_BKPUWF5_sSpWceNU9RlTeGs9HGZxkaC4p9WwNC6xwg0BRJy84R2Y_Ey1JizPTFFZ94m9lf3c1y1SdtnkNxNqJXLKEtYbUL6Lo-aZEL9mra2_O62IT-AqAatxA_ktrRJQ9IOFSfGAPTAsLJjtGIwjVmvzwVzu8FByirLUEaGsIkU-UdSQZ7BDv6DN8WkKXB-zsMjVqSN329k9TRvdZaeegQWPZ8iwImQf5hNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز سخت خبرنگاران؛ عادت ندارند مصلی را بدون رهبری روایت کنند
🔹
نسترن دادجو
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/666205" target="_blank">📅 08:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666204">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع محلی از حملات توپخانه‌ای رژیم صهیونیستی به منطقه «ارنون» در جنوب لبنان خبر دادند. گزارش‌ها حاکی است نظامیان اشغالگر این منطقه را هدف حملات سنگین قرار داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666204" target="_blank">📅 08:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666203">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1221868c.mp4?token=UeQBod6cALkdfiNxnYvWOgVPH6V1Bu6GfFhZO1uRqrPbXAYksbgE5fKe-d2B6U6KfMG0ic_KiBWbeLCCadC3WNu36inLfYMsjBipydqY5FtFFLrSlXBg-3Kb_pyghTF-0bezLMFXzfe--UOOkFdjz61IJSOpEVMsd-uKLS_-1lkB-IudVJT9GJfExuFE4vhN9za26I4A-stiJzOnm9-ARs_a9noDG2OwxYcvjJZlMm_g_GT5nmthH6f-KxmFSLwUVoqsNVLgQ6hpd3AVWTej_XEF74Lw6qy71neBfWH4c-VH5E2jBp2-a5PGMZhJia4f9yubK8oeqwIXuAB0dzQk7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1221868c.mp4?token=UeQBod6cALkdfiNxnYvWOgVPH6V1Bu6GfFhZO1uRqrPbXAYksbgE5fKe-d2B6U6KfMG0ic_KiBWbeLCCadC3WNu36inLfYMsjBipydqY5FtFFLrSlXBg-3Kb_pyghTF-0bezLMFXzfe--UOOkFdjz61IJSOpEVMsd-uKLS_-1lkB-IudVJT9GJfExuFE4vhN9za26I4A-stiJzOnm9-ARs_a9noDG2OwxYcvjJZlMm_g_GT5nmthH6f-KxmFSLwUVoqsNVLgQ6hpd3AVWTej_XEF74Lw6qy71neBfWH4c-VH5E2jBp2-a5PGMZhJia4f9yubK8oeqwIXuAB0dzQk7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یالثارات القائد الشهید
🔹
شعار خونخواهی مردم عزادار در مراسم وداع با «آقای شهید ایران»
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666203" target="_blank">📅 08:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666202">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meoJgnJSJYYqDoyFqSYszi1M8iMkl83G5xCYZ-6LVGzknqLL7_6FVzgd7j5qltgCXGyemMbdBIufNa6Cvuoqmii2hpJm7gRaL3OG6vCOa3G5kZBiDDBxQTq9ByLxIAF_dp8tg1r_fXwkgIgaVz9VuaeBDpCKlUiGMlCF6co-HRrAJoGxDpPom1tOlBJJGWXuJ19wR6f44dGKeB-isXHXQI8RY0woqV3Puq19DxaYg1r2Itz6RiacN9TI0doKl_bp7h86SDIvnr3F1y5FOpTjeBpxrw9Yh8fnEGinI-A9R5Ythb71u2p4FrEQHr8SI0lLAMFhhV03gziz42cV3_2LdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم کشتن ترامپ در مراسم وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666202" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666201">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD9xgGGVlUFkUceayMUxx9J17THAtmF9WZmqsEtGl4h5diKlwGVqFEvalxxbmw3GUC6dZJux5YbTYZU7l-HvevuIdyjeTXjA1tWmRYRLHyMnyw5mIouAuSfFXZkQ7ybz7L9qUgLgE8opDqi514tmwXo0AD5osCtWnQCKd2_Jtlbdq-_Zew5Ff1Vs-Wn2kYgDTlCYnahxxnHVkQFoJhD_XQw2MbbW68eWvOuxGRqfutuUQyOlzj8I3Brd5VMD8SSE2avjUlg1AuuXAIHvWM2Ot7NXAVbKaDPRdim2Dezq2eL3n0L7JA8dDE6slXLrTED_dNlY6otvAZLXnl7HUCobvwOjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD9xgGGVlUFkUceayMUxx9J17THAtmF9WZmqsEtGl4h5diKlwGVqFEvalxxbmw3GUC6dZJux5YbTYZU7l-HvevuIdyjeTXjA1tWmRYRLHyMnyw5mIouAuSfFXZkQ7ybz7L9qUgLgE8opDqi514tmwXo0AD5osCtWnQCKd2_Jtlbdq-_Zew5Ff1Vs-Wn2kYgDTlCYnahxxnHVkQFoJhD_XQw2MbbW68eWvOuxGRqfutuUQyOlzj8I3Brd5VMD8SSE2avjUlg1AuuXAIHvWM2Ot7NXAVbKaDPRdim2Dezq2eL3n0L7JA8dDE6slXLrTED_dNlY6otvAZLXnl7HUCobvwOjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاشا، در انتقامت بشود کوتاهی
کَلا، زمین بماند علم خون‌خواهی
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666201" target="_blank">📅 08:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666200">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032448e94a.mp4?token=mA8qYJXYcm_54_FBG4IAfvgTyLYPeNoAQblvANHUTKviWGgiTtUXJemjFvI-u-uumV9OBlqCex3KMLma1T-iFH77dJCoEY3_etbvL-tkkooyt2qN4ow5MyrHaUkpsh5i6z3771IgVOvDKh43l2X1BSF82BuNBNd8prnK_J2BKu3wrX_CrzX4AAyU5jpT049V3ayX0A_O-gY_FynDk2GRISY3yBM6w_DOY_bYXzUTsAtrhOvmYWMETjozXhXdi92wgbk1MJIw_3GO2iXPinoOezEjNrOfEVLg7vgyKCw7gR2mP3uEp4g5zDZrnqHZ-5qEl8l80cb4n_Rp8dXkSaAL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032448e94a.mp4?token=mA8qYJXYcm_54_FBG4IAfvgTyLYPeNoAQblvANHUTKviWGgiTtUXJemjFvI-u-uumV9OBlqCex3KMLma1T-iFH77dJCoEY3_etbvL-tkkooyt2qN4ow5MyrHaUkpsh5i6z3771IgVOvDKh43l2X1BSF82BuNBNd8prnK_J2BKu3wrX_CrzX4AAyU5jpT049V3ayX0A_O-gY_FynDk2GRISY3yBM6w_DOY_bYXzUTsAtrhOvmYWMETjozXhXdi92wgbk1MJIw_3GO2iXPinoOezEjNrOfEVLg7vgyKCw7gR2mP3uEp4g5zDZrnqHZ-5qEl8l80cb4n_Rp8dXkSaAL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: «ایران می‌خواهد به توافق برسد؛ آنها به شدت مشتاق توافق هستند. ما چون آدم‌های خوبی هستیم، به آن‌ها یک هفته برای مراسم تشییع فرصت دادیم.»
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666200" target="_blank">📅 08:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666199">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e5351b53.mp4?token=bIQDium1CCyZOLrYLbEHW8ZHnTh9FDE3Z_z2cvhMfvXAWAG8NpVJzZjixFOnYeuII4ddu_hZvvloJzbqEqQmcPICOhd662m-EUTJzmteCl6jmVzXzZMpZRvLaMALc7me3noBKj7IkSXm4aXWONgTD0TSTD0ISGL3z1uBt_78XM5Y8joA47-LWojIz--XvYtSnyifa0UyAXrNXrTrrWmdJYQyALI2eDwmxyAA9GTLPsfKc7HC40uDHquWA3z9ObsuDKmtdsYuJQEKn4__Aae6LSf4fuZaqz3OoMO2MWFU6cAMWZOmZjHCy8xtZcJuU0mMycIZQBpF7R81Ehbo_5yk6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e5351b53.mp4?token=bIQDium1CCyZOLrYLbEHW8ZHnTh9FDE3Z_z2cvhMfvXAWAG8NpVJzZjixFOnYeuII4ddu_hZvvloJzbqEqQmcPICOhd662m-EUTJzmteCl6jmVzXzZMpZRvLaMALc7me3noBKj7IkSXm4aXWONgTD0TSTD0ISGL3z1uBt_78XM5Y8joA47-LWojIz--XvYtSnyifa0UyAXrNXrTrrWmdJYQyALI2eDwmxyAA9GTLPsfKc7HC40uDHquWA3z9ObsuDKmtdsYuJQEKn4__Aae6LSf4fuZaqz3OoMO2MWFU6cAMWZOmZjHCy8xtZcJuU0mMycIZQBpF7R81Ehbo_5yk6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار یک‌صدای «لعنت الله علی اسرائیل» مردم در مراسم وداع با پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666199" target="_blank">📅 08:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666198">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d21bb4459.mp4?token=M7uOo-qepaKzqL6Msl28LTt8DNvDA1LMTYIcn6xkYoKZLnAYsJRxoqCqGbgoKJKjQL0tQTOLBwgbvWLbDE9JIpeAhzFVFKG2qAzVyWQTSdky0PAKlvCxhIiad9zjZpHkyhxd5joBplkR3MKwG5p4h3N50DCMgAYKnOVeUvgSyqcDIF3qEfKBNFVXpalmGj4KgRHdF4hF2P6YwnCr_0S1ATljp0DbBLf8a5A-PxuC3dT9o-lU5PRZCdvsKVGjjeyWGFuTC84trzxi675b3KhyB2fRJsURaGB4RB1EbMGor1QM3NFv-Q7dmgZsxAGMPLYC4GkTdsnmpIf7-6lvrLcxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d21bb4459.mp4?token=M7uOo-qepaKzqL6Msl28LTt8DNvDA1LMTYIcn6xkYoKZLnAYsJRxoqCqGbgoKJKjQL0tQTOLBwgbvWLbDE9JIpeAhzFVFKG2qAzVyWQTSdky0PAKlvCxhIiad9zjZpHkyhxd5joBplkR3MKwG5p4h3N50DCMgAYKnOVeUvgSyqcDIF3qEfKBNFVXpalmGj4KgRHdF4hF2P6YwnCr_0S1ATljp0DbBLf8a5A-PxuC3dT9o-lU5PRZCdvsKVGjjeyWGFuTC84trzxi675b3KhyB2fRJsURaGB4RB1EbMGor1QM3NFv-Q7dmgZsxAGMPLYC4GkTdsnmpIf7-6lvrLcxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت اصلاحی تخصصی برای آرتروز لگن (hip_arthritis) #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666198" target="_blank">📅 08:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666197">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نکاتی برای حفظ آب بدن و پیشگیری از گرمازدگی در مراسم تشییع رهبر شهید
مدیر‌کل تغذیه وزارت بهداشت:
🔹
سردرد، سرگیجه، گرفتگی‌های عضلانی، تهوع، افت قند خون از علائم گرمازدگی هستند. شرکت‌کنندگان در مراسم تشییع رهبر شهید در برابر تابش نور خورشید قرار نگیرند.
🔹
پیش از شرکت در آیین تشییع می‌بایست بدن را هیدراته نگه‌ دارند. داشتن یک بطری آب به شرکت‌کنندگان این مراسم توصیه می‌شود.
🔹
مقدار کمی نمک برای تامین سدیم توصیه می‌شود. استفاده از نوشیدنی‌هایی مانند ترکیب «آب با عسل» و «آب و مقدار اندکی نمک» به سلامت شرکت‌کنندگان کمک می‌کند.
🔹
همراه داشتن میوه‌های خشک مانند توت خشک، برگه هلو و برگه زردآلو توصیه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666197" target="_blank">📅 07:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666196">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
متروی تهران از امروز ۲۴ ساعته شد
مدیرعامل متروی تهران:
🔹
تا ساعت یک بامداد روز سه‌شنبه، ۱۶ تیر، خدمات مترو به‌ صورت ۲۴ ساعته و رایگان ارائه می‌شود
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666196" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666195">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e2332db0.mp4?token=CL6DoKCn0E77ch2B1V6H8egF6RsmxOAa1fjGM58-azClg-HesyhFtQazkBkjfQVhHFWGQj6PPs5SSyEg5EZgEPQG0RzJa0YB6Bsd72P7ZaHyGnJ20Xv1q01O8Kch8B22pnQ4uYtfw3DTIiwAWuCNTvi684G1fxiOsuD4HIlEUav0FajRSopjvjPIM-Z8-xLNnxS2x9f5uRSSgy8XCLGfsrxju8yOuUMCSQ025WNpT2I2UcMtBnSCyDv_-JhX9kGXDRZEIm482d6A3OpR7vkpXC0EZ5mAkKZsesl3Nl_L0HBz4B4GqYBBTtZi5JjLaFJDWxyHmIxiTPWfBORpD0n4PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e2332db0.mp4?token=CL6DoKCn0E77ch2B1V6H8egF6RsmxOAa1fjGM58-azClg-HesyhFtQazkBkjfQVhHFWGQj6PPs5SSyEg5EZgEPQG0RzJa0YB6Bsd72P7ZaHyGnJ20Xv1q01O8Kch8B22pnQ4uYtfw3DTIiwAWuCNTvi684G1fxiOsuD4HIlEUav0FajRSopjvjPIM-Z8-xLNnxS2x9f5uRSSgy8XCLGfsrxju8yOuUMCSQ025WNpT2I2UcMtBnSCyDv_-JhX9kGXDRZEIm482d6A3OpR7vkpXC0EZ5mAkKZsesl3Nl_L0HBz4B4GqYBBTtZi5JjLaFJDWxyHmIxiTPWfBORpD0n4PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار یک‌ صدای مردم در مصلی: «انتقام، انتقام»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666195" target="_blank">📅 07:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666194">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13d158d39.mp4?token=DukTmsGc1gInhHgYAgRBqTtXYTJnBRKcfV5G3nK9nvpDWRAIJZLJo_WJJL3IadpmvMzueLI7ANrZvxfZ0RMPftX3vKU9B6E071gmCwOOu5_b9fm-PVsKWDdAZKW_i5JRFobs1et3DJnx5spkb-RhRjiCsxeyNgN7xve_ZjJotTOpwnj3nq4RlR1E5oLJhEGy8yvvx6yGHD5mOm2ih4aMIUVfoB7nR0uZUmmVm8PlI2Xuxm4BsKb-NB-KjkPkMuReTUy1ygMrm4Bnuo6NmMFQC6YXOuqiOtwfvUoKWhevz8JP8rPVpvtIWWq3vLYaq9Nqx8N77JLF8O73LTGZeZCx1x_dADCEPVPG9DOzWcG34mXg7pW32z7MlCfmUH8G5DqexFiUgfnmCfMwnL97w9sijyWkwOw2e7JZcSqX690BLeYKquP6afXzY1tyiq49Yvk4yqG5lc88tvsflOVT0K0gXQFiK0e57BWW8ZXXdI4CMFLLV06uHWLMc8Heqtw1GS043SOycGBAOr2ExWQjQu92yY3nUnQZ0hn2GTu9d_06CBFPWo5wwKqIMxiH8DA_zVExIBYmiUglqB4zBn7-dJ9haTqjv2eonPcCiUV37fjB8rDU88ESKdZsY3a2BEx0jlIMOeLeMb2aHiQ8XlWCVWnDVFm3LxKodprvVMsQHz9Ovz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13d158d39.mp4?token=DukTmsGc1gInhHgYAgRBqTtXYTJnBRKcfV5G3nK9nvpDWRAIJZLJo_WJJL3IadpmvMzueLI7ANrZvxfZ0RMPftX3vKU9B6E071gmCwOOu5_b9fm-PVsKWDdAZKW_i5JRFobs1et3DJnx5spkb-RhRjiCsxeyNgN7xve_ZjJotTOpwnj3nq4RlR1E5oLJhEGy8yvvx6yGHD5mOm2ih4aMIUVfoB7nR0uZUmmVm8PlI2Xuxm4BsKb-NB-KjkPkMuReTUy1ygMrm4Bnuo6NmMFQC6YXOuqiOtwfvUoKWhevz8JP8rPVpvtIWWq3vLYaq9Nqx8N77JLF8O73LTGZeZCx1x_dADCEPVPG9DOzWcG34mXg7pW32z7MlCfmUH8G5DqexFiUgfnmCfMwnL97w9sijyWkwOw2e7JZcSqX690BLeYKquP6afXzY1tyiq49Yvk4yqG5lc88tvsflOVT0K0gXQFiK0e57BWW8ZXXdI4CMFLLV06uHWLMc8Heqtw1GS043SOycGBAOr2ExWQjQu92yY3nUnQZ0hn2GTu9d_06CBFPWo5wwKqIMxiH8DA_zVExIBYmiUglqB4zBn7-dJ9haTqjv2eonPcCiUV37fjB8rDU88ESKdZsY3a2BEx0jlIMOeLeMb2aHiQ8XlWCVWnDVFm3LxKodprvVMsQHz9Ovz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصلا نمیشه باورم...
🔹
لحظاتی از شعرخوانی حاج مهدی رسولی در مراسم وداع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666194" target="_blank">📅 07:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4w7OmmOY5sX3NK4QN-K5Pio9h0ztZGVuYFs0pX6ra923rzyJNhN6nFGHBCz_tFNU3JLoNReTemumgOIk2iGmVmC6kVNhjmWq406Q-LRbbO8la2fpz0Y84NTZsxhoUPcXhVnGezuLxsZChKHUPnrdMAaKR83TD7r3JITQWNvQloNM1HAZ4bjTkvIF_bwbARyaJVbR2THgupPXOBXJRaOLyHG292XOoLwf5lvYyOuV-vjjqsG-P3LZjpggpmoyPlqBVNPZtJGc9FmMvmISSR_h0WfPMDdX2wy0CehQ_mozBgM_OIXxi2nkLFdWS6l0JPGkx4ZjJTy3ilVhGWdisB3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف قرار گرفتن تأسیسات نفتی بندر سن‌پترزبورگ در شمال‌غرب ساحلی روسیه توسط پهپادهای اوکراینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/666193" target="_blank">📅 07:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32082aa377.mp4?token=cqUXcQjtajkC-z7LTF1V_Bz0_pwsSyS_t4matsNx5DzBYd2NjodBJJhzlr_aypRJP8hFqMFgaW7hvJHX_qo0jZiqB652qQh0YcZikCvRHZa0J4x8LnzG1mJtbJFu3vBDuhlTKDT87pszScHFF9A-RnhTUkNxOlUZ2Fc_be_geuKRji8t9yJvNocnO93td3jPyMEOgRhWOdb0fBUVO6K36jAxNPt78Bde1QAXBjc1AnXzInfH9x3_MLG--gxeOu4fif0iacE_EXphxcmbmxR3RZVsFHUQpZlHuLDvkpm7sC1WCxk9QkpARVN1HrjrAGzNeODP_9ViBYCGcMRHceegsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32082aa377.mp4?token=cqUXcQjtajkC-z7LTF1V_Bz0_pwsSyS_t4matsNx5DzBYd2NjodBJJhzlr_aypRJP8hFqMFgaW7hvJHX_qo0jZiqB652qQh0YcZikCvRHZa0J4x8LnzG1mJtbJFu3vBDuhlTKDT87pszScHFF9A-RnhTUkNxOlUZ2Fc_be_geuKRji8t9yJvNocnO93td3jPyMEOgRhWOdb0fBUVO6K36jAxNPt78Bde1QAXBjc1AnXzInfH9x3_MLG--gxeOu4fif0iacE_EXphxcmbmxR3RZVsFHUQpZlHuLDvkpm7sC1WCxk9QkpARVN1HrjrAGzNeODP_9ViBYCGcMRHceegsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
و اما آخرین دیدار
.....
لحظه پخش صدای رهبر شهید انقلاب در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666192" target="_blank">📅 07:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db21ec429.mp4?token=GdQUcUWo9bRn4iJF1-TM1_0rIHgDPMrzzrmbdUUOvzwYuAfit6DCILeuvRflkujVkP61mEbtoFVrJyx5fhb6kS7dz-UIQSTl9SKSZdjzotLEJn1fJgjzNVUfXpliuVZyRee1mHrSg2DX_zTJ3UObhX1vVTrlkIbPbhaQCSGvjGULB3DaE5y_irAMd8SehfYVfnq_BueN3FyfpAUJC5kUd7NEy5McJHcYMWNzc1V7Zn2PR-KS6p1A6ZC5wnIyM8u38i_sut4SpMKqmb-j5QhsuFlx0lf_2xBarDbwcUf13q-pTl2bFbLPIlC7KxTD56AfgswqbCHqr3vXAn257wXhWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db21ec429.mp4?token=GdQUcUWo9bRn4iJF1-TM1_0rIHgDPMrzzrmbdUUOvzwYuAfit6DCILeuvRflkujVkP61mEbtoFVrJyx5fhb6kS7dz-UIQSTl9SKSZdjzotLEJn1fJgjzNVUfXpliuVZyRee1mHrSg2DX_zTJ3UObhX1vVTrlkIbPbhaQCSGvjGULB3DaE5y_irAMd8SehfYVfnq_BueN3FyfpAUJC5kUd7NEy5McJHcYMWNzc1V7Zn2PR-KS6p1A6ZC5wnIyM8u38i_sut4SpMKqmb-j5QhsuFlx0lf_2xBarDbwcUf13q-pTl2bFbLPIlC7KxTD56AfgswqbCHqr3vXAn257wXhWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای ناگهان عزم سفر کرده، خداحافظ...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666191" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1I9Yb5Nj1XPe4h9Vrxbo6RyqWsddyf2rTRYUNGCiN-ILe872T_fx21MWdQYvTnFKSTL3k_1mPIJj6LHM56Gh1znO4fU5z2392_BsS4l2kKHt0KAvr83HavlYFj9OfqiljLTKYUCfWbTdYBsNuYjnMTaBCdlk2atnnwHunSYRmToLctJpyjAtXAWNNCpGMuJT-Na3Z61jz_xvkmH2mBzWOqFOHD4h7cgG_7HO-nF4lfr2F764ZAhzqwMihhDGSfB3pG6JGfQVrr7zQtB1ZWd_-dmGTPi3j4XTo2HWsEXYdz-eOgj16r8x-csI9VJInkUR2dk1Q6M7MMtxylMNfPBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرار گرفتن پیکرهای مطهر رهبر شهید انقلاب و خانواده گرامی ایشان در جایگاه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666190" target="_blank">📅 07:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce199e3827.mp4?token=t5i4dxK-Rf5IZN4FWus-W2dmtaMe8JpRRwmPkwb2uyCNpJEsBIPmsVKFRwjrV4hMtcQws83KBGVLGHu2q0iMJ0TDv2lFx-GuQQzqmWkAOanTadB1X8h-pchGqT1Z99yJn0CLMnEWHD8XvMjWQUThzulbQwlO-Hwe-anKoAOLkVm63TpvLnsbGPIIZJrs7fUSXroi1o_L_nufYQYGSxWsN9WPvINpmZOZyY-FlMNhTif6p3BJR-8n1UAePMK4HVcG7VtKz8zJNINnNMBMoJBmYkGecybXwZJUpqI5JYyJkubecUGuZOUW_OmeSlAXJdr1PM0L0vGzdY-D6nafLGcd2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce199e3827.mp4?token=t5i4dxK-Rf5IZN4FWus-W2dmtaMe8JpRRwmPkwb2uyCNpJEsBIPmsVKFRwjrV4hMtcQws83KBGVLGHu2q0iMJ0TDv2lFx-GuQQzqmWkAOanTadB1X8h-pchGqT1Z99yJn0CLMnEWHD8XvMjWQUThzulbQwlO-Hwe-anKoAOLkVm63TpvLnsbGPIIZJrs7fUSXroi1o_L_nufYQYGSxWsN9WPvINpmZOZyY-FlMNhTif6p3BJR-8n1UAePMK4HVcG7VtKz8zJNINnNMBMoJBmYkGecybXwZJUpqI5JYyJkubecUGuZOUW_OmeSlAXJdr1PM0L0vGzdY-D6nafLGcd2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری ماندگار از وفاداری؛ با عصا آمد تا با آقایش وداع کند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/666189" target="_blank">📅 07:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090512834a.mp4?token=nsq3y8gGIGzVKJZ6fUFHVfVrs_GUwweIMx73tr6y3Zj4VdOZOILVWowLZBWfPF70GCh18BIYoFFOJKSOaJZ3hpI-Pwr8UWcfKLSp3UoAQfFxIzeF2vRP8TuvfeJ84fbQ4qplGc1iy6pc-3CjsMfoLuxLDRJlm0db7IMzw34JWS_tFhAQgBRfsiYLKptt0F-9qZWlYFq0a3M4kz2TCneYV2BclTTU_TG86U6EDC7PCWQgjeq1ZppalOAeFTnSafcCStSXbBe6mcHOdTO_NAU1P8kpUb647CAfWhcNzqEVreULrec4esyLY65bPlVO6XTkiuNkuXiXaGttNAQvZFj6mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090512834a.mp4?token=nsq3y8gGIGzVKJZ6fUFHVfVrs_GUwweIMx73tr6y3Zj4VdOZOILVWowLZBWfPF70GCh18BIYoFFOJKSOaJZ3hpI-Pwr8UWcfKLSp3UoAQfFxIzeF2vRP8TuvfeJ84fbQ4qplGc1iy6pc-3CjsMfoLuxLDRJlm0db7IMzw34JWS_tFhAQgBRfsiYLKptt0F-9qZWlYFq0a3M4kz2TCneYV2BclTTU_TG86U6EDC7PCWQgjeq1ZppalOAeFTnSafcCStSXbBe6mcHOdTO_NAU1P8kpUb647CAfWhcNzqEVreULrec4esyLY65bPlVO6XTkiuNkuXiXaGttNAQvZFj6mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین ندای ای پسر فاطمه منتظر تو هستیم در صحن مملو از جمعیت مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666188" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4f7f5387.mp4?token=VUZ04HanBhDWPQX9IgJkLAMZuvDcIzR9dTt0OwnZ2ATUxXmGhQpoQBnhgMECAzWqgbDo9NvQMEiobS4N3f2TKbp8ukCSMcmEpxsIfqeJgADGySo0pWKFyQLwJYHmi1EC36-rN59Mp5neK8vA3EcAv-1u2UxOR_lcjiYRu3WsvLN-ocIbvOwskro0Qo6nKlsJ9q-U9B-5aFQLhqzUbeJXE2YEm0kwiZNzr1fMlOQ_kdh7eYg9hOrG-Ihw4TD04G4Px9VKMfnzQ1AlvXTSmMsqiV_m6hXKSZnqOakeQoSJtkSbmsSWIN-1jgueiJaXfzCaxMaeMSTB4mDO3zJdMxcl_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4f7f5387.mp4?token=VUZ04HanBhDWPQX9IgJkLAMZuvDcIzR9dTt0OwnZ2ATUxXmGhQpoQBnhgMECAzWqgbDo9NvQMEiobS4N3f2TKbp8ukCSMcmEpxsIfqeJgADGySo0pWKFyQLwJYHmi1EC36-rN59Mp5neK8vA3EcAv-1u2UxOR_lcjiYRu3WsvLN-ocIbvOwskro0Qo6nKlsJ9q-U9B-5aFQLhqzUbeJXE2YEm0kwiZNzr1fMlOQ_kdh7eYg9hOrG-Ihw4TD04G4Px9VKMfnzQ1AlvXTSmMsqiV_m6hXKSZnqOakeQoSJtkSbmsSWIN-1jgueiJaXfzCaxMaeMSTB4mDO3zJdMxcl_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت بی‌پایان در خیابان‌های منتهی به مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/666187" target="_blank">📅 07:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666186">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8c335e616.mp4?token=k0OHEbu-YIYILvrbYeHNY2VTv_CJT6IeJzPq9E7yekUpPHzs1edVRg_gqDr_m8HbuLpN0Xc_6ZlxhlmAibVmDLQ97fsxB9HUl6raFB7BTsGZJGG_c5zCliCeDZOY2rAC7VuDiEXn6nryFUW00ceA4ORA2A7L_yupgmUKLlSCbw46R1SYioNJDWMYypUL1Sg8HPf5az88WCnWFTFotNsJSw061QBe8WgEbxOTE7H3il_7J7V87wDzaALaS2RH2lsYqIKMC2NypWyerLPY3bmzxBkccYnkk66pveuq7UcCWT-SZaWtOgrrqIldFMihcclJXth3rT_7QDwIoSwU8f7d3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8c335e616.mp4?token=k0OHEbu-YIYILvrbYeHNY2VTv_CJT6IeJzPq9E7yekUpPHzs1edVRg_gqDr_m8HbuLpN0Xc_6ZlxhlmAibVmDLQ97fsxB9HUl6raFB7BTsGZJGG_c5zCliCeDZOY2rAC7VuDiEXn6nryFUW00ceA4ORA2A7L_yupgmUKLlSCbw46R1SYioNJDWMYypUL1Sg8HPf5az88WCnWFTFotNsJSw061QBe8WgEbxOTE7H3il_7J7V87wDzaALaS2RH2lsYqIKMC2NypWyerLPY3bmzxBkccYnkk66pveuq7UcCWT-SZaWtOgrrqIldFMihcclJXth3rT_7QDwIoSwU8f7d3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این جمعیت عاشق داغدار با پرچم‌های یالثارات الحسین برای دیدار آخر آمده‌اند...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/666186" target="_blank">📅 07:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqCqAROORw-VXYXjC8OF138tdmNv0EgyqKHnQWtGjE-MoPyO6HGSdnvJEh837m0snKVVgULsDNa-FmaJFJZapF3bNeMrPBbw_NxvB1hVhZC4X36INyxzZk7rdS_jHvypxfCU15v4JqCZrEYArcLSEekUNb73RiI81ASS4PCKX8qy4OyTGE9JozyNXrBPPlsLO4oJbuLGsdk5WU0wH3KSazCsWQwe3uhV8V08r7G7VOoYFfzlEsE9_OCzB60d1gtrRAS27chP3zPQHk3JH-SYv0dDW2Ev-XVPwDPYB-wpNp3FB-u8S_HyHf0ozTJXJ3Qpidg1YlSluHR31E8EhpMzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tELJ7CMWs2L49m8dW7-c9J-a6L8KqPEkINJDmZd_KWAuRgyBUnVnsvAp89jvq95CjyKp6ga82gV8kw_I5T51QUrJYZyUJKaKJPGew3v_-7AxXioCFSoY5M8joGgBZEU862Oy-1gxfZz-k9qeGV5TPwbOYg23gzksux88Nf4Omj9IjL3v162yGHY3eZY6haPXGvyRwL7l4Ls9cb0yevm1lT961vfzIy03LcKrD490tJ3jb_CzNNErDFrY1hBJw7cJC8JsJ-mL9YgLPzN6HphlTxFL6W8EnNN7MhRJjhdkoRdFORD_Bybf5n77A1RW2Oex_4JH9tez_Dl4E-BSbEEudA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ مصلی امام خمینی (ره) تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/666184" target="_blank">📅 07:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_HC8eS_UdLjK3YneTp9DbK81vr8m2BN85iahdxPT6lG7I-x0bnpIfNqBA8YtZDZ6PV6wJZxS8or2iEEshYV00vCkwsm_uvVl3w0eJiwM8GKnzLbG_v5GhXvcyPHfQ6e7q6holx65nTjhN8ePe7tz0DOQytLro-RtwV5kztlSBZr_aX3_j5JpO86xvSYOuv9UNhlGNt_2prZJzqxGfNKbiDbSDK3tbZwp6wZpxquPKdPGBaJK_S7Wgp1FEuCMvP-vQm3FC5q75SuCL_wxawThzkv9aWlYmNONQsDBLzeoZHRqXX-WPfIwjgjCvVfLCp1HfRZwoqZ1ukSMZkK4j-DwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار جدید مرحله حذفی جام جهانی ۲۰۲۶ با اتمام مرحله یک‌شانزدهم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/666183" target="_blank">📅 07:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666182">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25dfa59cbb.mp4?token=L3Yx4_gTbXj1ZOW6Zg_1c9DCwiDYKJ3RE7CZtBrFv1zfE35NwjoDQyUraMOE6dys3lv_oSLPX74kCYaAx18_prEjl9R3OBAt6hnCDH9HgpPjXquVlzHCpHhfcvTb4L-0jCrtASq4v895H0zNTpz4NRfCqZtNd6B8BumnCPOAIKSmlNObvnF_sgwXy7wSNtPyOVgMRmBX8Nr8nXbKugHr3ufke73rLFGHBB67ZIFkpRN3YXgmuumje507dWfBOZ0fZRPmCynE69WWJSv5GrU1y_jIU2XnRZPyNIHoGZKrRw5z_htMTLnfpPbgY_wvADx22_SeXEpnIo4W-Gf4ye712g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25dfa59cbb.mp4?token=L3Yx4_gTbXj1ZOW6Zg_1c9DCwiDYKJ3RE7CZtBrFv1zfE35NwjoDQyUraMOE6dys3lv_oSLPX74kCYaAx18_prEjl9R3OBAt6hnCDH9HgpPjXquVlzHCpHhfcvTb4L-0jCrtASq4v895H0zNTpz4NRfCqZtNd6B8BumnCPOAIKSmlNObvnF_sgwXy7wSNtPyOVgMRmBX8Nr8nXbKugHr3ufke73rLFGHBB67ZIFkpRN3YXgmuumje507dWfBOZ0fZRPmCynE69WWJSv5GrU1y_jIU2XnRZPyNIHoGZKrRw5z_htMTLnfpPbgY_wvADx22_SeXEpnIo4W-Gf4ye712g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع رسمی مراسم وداع با امام شهید امت با تلاوت قرآن مجید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/666182" target="_blank">📅 07:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666181">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c898339bc.mp4?token=LzbE9-_iOY-CcaN5Pq10dnS_uikUlm9FVVNzseD7I2LJ9KtPf_sblkX-vG9uU2RYFmA7wr2gLccArEBmLebpj4oq1ls_raEo-_9cxaCgp3rwVxetkY_u3FNIa_J_jsQ6K-qwucOac6F5_v43KOREvKNK8YxbdqmWisOhbso2he1BsngIywh_pqqlX48uHG96TqS1r-bD4gujvOWjn_iN-mvKpnUc0rwnk4O0llMo7BtXXSQ_TW1wbqXptyq2WxJvIDl7D8EEkgvS-aR0wPZ16EFCQpt8WpDZPkmbam61fGOf7HSfDiOaVSgo8rvGRIlRvtMOKNRhbMUVqH3lJCFz1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c898339bc.mp4?token=LzbE9-_iOY-CcaN5Pq10dnS_uikUlm9FVVNzseD7I2LJ9KtPf_sblkX-vG9uU2RYFmA7wr2gLccArEBmLebpj4oq1ls_raEo-_9cxaCgp3rwVxetkY_u3FNIa_J_jsQ6K-qwucOac6F5_v43KOREvKNK8YxbdqmWisOhbso2he1BsngIywh_pqqlX48uHG96TqS1r-bD4gujvOWjn_iN-mvKpnUc0rwnk4O0llMo7BtXXSQ_TW1wbqXptyq2WxJvIDl7D8EEkgvS-aR0wPZ16EFCQpt8WpDZPkmbam61fGOf7HSfDiOaVSgo8rvGRIlRvtMOKNRhbMUVqH3lJCFz1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم یالثارات‌ الحسین بر فراز گنبد مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/666181" target="_blank">📅 07:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666180">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr5T4RbYMJx9nkcz9Xl22aAbIPXGZn0u2aNZnBmc_p7-Plb_4RSSjP58XykZKlrUXLn4sz4_fNiyLyhaxmU3XvAmULD5uT0LSCuKJsNxOf2C-GjSer8vdMZAX_FxvL1k-f2rx3EQeUZQSTAZ6nCkNYG08I7cXrmm0l1UiLG213gvBmgCiWBl7HNwm6rr3DXk0EdFbcsNsMb4RpzGiZ0g83blfKxCcsmMo0MsoCPlU3tGnk6vIK3aiGcM-kHFxfi9JQi-zr4NYxIuZJwJQBWISUZewb2d9oBpbN1VUrhhTgGyrOtWNIH-HDMa59qNQ3PQ2NYj1c893mDClMB_gKnzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیتر متفاوت روزنامه لبنانی الاخبار: «تشییع قرن»
🔹
روزنامه لبنانی "الاخبار" با انتخاب تیتری متفاوت برای مراسم وداع با رهبر شهید انقلاب و حضور مقامات ارشد کشورهای جهان، از این رویداد با عنوان «تشییع قرن» یاد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/666180" target="_blank">📅 07:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck-5SFIrlCcDrnePMGyO-2s15qfrw-7B8LUYYwwhm2KFPx3ahzluQXOlu7fxcg-XLWsNZZlRAGpHM-weV6NKdZOnerqqFDayqx9s4uGVzJ0jLjgaLUZvuA4WRDIpj9NRGH9IlMMrhtGMGIITSLXmbqs-iX9Gah64FSa9WPdLeoPZ8INzyAH301enrqWvWw6fIFkBy4-36BbHaBJcPSc6tuANL9eO_3an9UC6smNP3-viwHdIWKS7lst0Dbh7aY3gwY3CHxG-63v-gkywkc97liL6q1dFqO3HGhf-XYukfneaB6_7KX7pj96ozn6cGkhswKiGWrmUGytIHNQBEbUl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهمان گرجستانی اولین روز وداع با رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/666179" target="_blank">📅 07:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666178">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نمایی از جایگاه پیکر رهبر شهید انقلاب در مصلی تهران برای وداع مردم ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/666178" target="_blank">📅 07:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671d6d7cfb.mp4?token=nv2VFA7znHB7djwyVOejcC5bALT9CUSBi5CqYsdH69u_UhOWdo-VkPpN6zLF8VwJxwQc9086icuYIqPLltCM_5Fl4tTE3VsLW2pJlbaEdzHfOd9vtpB2jSjxw8hAN15OeRZWY1RDo7OqICUT_ZrDyNfVQ2OFELrTXVxhv8gSbiUiXK4xUtirZMs1cqgTHiGh8F8vRXT5DsHxFWiPQcES9YPvRfoxuM3CnbZ5h2WOiKkD--ZLtx-Yb6X-IuY8nUT9yGjA_cyY23N_03LSiykcTJus7sMS-bcthuawz6Y6W0KSzdT98DQdgxHCbsRRApDIwZVrF3nF0pvGhI43FNmXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671d6d7cfb.mp4?token=nv2VFA7znHB7djwyVOejcC5bALT9CUSBi5CqYsdH69u_UhOWdo-VkPpN6zLF8VwJxwQc9086icuYIqPLltCM_5Fl4tTE3VsLW2pJlbaEdzHfOd9vtpB2jSjxw8hAN15OeRZWY1RDo7OqICUT_ZrDyNfVQ2OFELrTXVxhv8gSbiUiXK4xUtirZMs1cqgTHiGh8F8vRXT5DsHxFWiPQcES9YPvRfoxuM3CnbZ5h2WOiKkD--ZLtx-Yb6X-IuY8nUT9yGjA_cyY23N_03LSiykcTJus7sMS-bcthuawz6Y6W0KSzdT98DQdgxHCbsRRApDIwZVrF3nF0pvGhI43FNmXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور گسترده مردم در ساعت ابتدایی نخستین روز مراسم وداع با رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/666177" target="_blank">📅 07:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666176">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfF7G0IHQHL5C9XXVOncbnTHZh0lptR6-RYV3dZpXbg7DLhvO9DgpR8ho74ATHrbCiKm9UQTAhKLB5aUrh84iAtL-EXenHTOi6_E6x5sSTUQe1qCIRYSwPptCVHy7sPTG9r0ECA4zzhJHJ6QlhyWYJqDY0j89xjC8PTyHCRz_AWJJevkkN-X36H9zz1CsI1m3FnVsMWLFNKNGsLVpgK_wQsDGa1vGOAMlOJrxzwrabH0OsbMJJP0egLXoWsnFsFJ_EE2t2-tMZRyQ2Xgzgugrzdq1KT-e-hPJP6hcWt-k8o1HCgZO4_Bj4plGZC-jBCMNx1Kisu4a3ArqA1fDvxRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۳ تیر ماه
۱۹ محرم ‌۱۴۴۸
۴ ژولای ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/666176" target="_blank">📅 07:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666175">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d543c6c364.mp4?token=qp5NYpcoM6Xpp3cKtuODzFVB2EY8I5KpUqp2_-Wi7554-u2nrYsUl9kuV4SljZ6aF3C1lpT4i1tNyR5penlP-EkgdtqBZBJxNi3jWKUU-xk7yV-vAb4f12LRTomc-DT21YiE0HiriqmkbI-wofLNzCNT8NlbcxhvWD2OciUHWawfO57EqKW5p9lbbL4AE9RDBjNfrU11z2mckPuFOp1CG-Kqps13iMOBNvotl-HtU5Q3MJKhx29UYb8O8izgYkFJKrdrDqU_K-D015V2NSknzF0pQxom4Ro7-0tgjSR1YcaOmafpFRRzMWEZyvq4IBrytR2RRhcY49R5J0Bl7gMozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d543c6c364.mp4?token=qp5NYpcoM6Xpp3cKtuODzFVB2EY8I5KpUqp2_-Wi7554-u2nrYsUl9kuV4SljZ6aF3C1lpT4i1tNyR5penlP-EkgdtqBZBJxNi3jWKUU-xk7yV-vAb4f12LRTomc-DT21YiE0HiriqmkbI-wofLNzCNT8NlbcxhvWD2OciUHWawfO57EqKW5p9lbbL4AE9RDBjNfrU11z2mckPuFOp1CG-Kqps13iMOBNvotl-HtU5Q3MJKhx29UYb8O8izgYkFJKrdrDqU_K-D015V2NSknzF0pQxom4Ro7-0tgjSR1YcaOmafpFRRzMWEZyvq4IBrytR2RRhcY49R5J0Bl7gMozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج قاسم برات مهمون اومده… آقام از میدون غرق خون اومده…
🔹
بدرقه آقای شهید ایران
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/666175" target="_blank">📅 04:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666174">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چهار نشده در را باز کردند و غمی عظیم به حیاط مصلی سرازیر شد. غمی که آدم‌ها با خودشان از گیت‌های بازرسی عبور می‌دادند و هیچ‌کس نبود که غم را از شانه‌هاشان بردارد.
غم به‌جای این‌که تقسیم شود تکثیر شده است، با همان وزن، با همان اندازه و آدم‌هایی که داخل می‌شوند همه خم‌خم راه می‌روند.
دعای عهد از بلندگوها پخش می‌شود و آن‌جا که می‌خواند: "إِنَّهُمْ یَرَوْنَهُ بَعِیدا وَ نَرَاهُ قَرِیبا" به تصویر آقا نگاه می‌کنم که زیر یکی از ورودی‌ها برای مردم دست بلند کرده است. بعد فکر می‌کنم که قریب به زبان ما چند سال است؟ برای ما که توی همین صد و چند روز صد و چند سال پیر شدیم.
به سکوی مراسم که زیر ایوان است نگاه می‌کنم. زیلوهای آبی، پرچم‌های ایران و آن صندلی که روی قلب‌ام نشسته است و ده‌ها هزارکیلو وزن دارد.
آفتاب هنوز سر نزده است و من نمی‌دانم امروز اصلا خورشیدی طلوع خواهد کرد یا نه!
🔹
به قلم مرتضی درخشان
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/666174" target="_blank">📅 04:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666173">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kw6R4bjWL7VyhPUZoQ0-EpNmIEPxYv99lF918-lQzFb8rpMJM3PFEJqV6BsveKgYYlTDs3g37s-Gh5z6b34Bj00kdmuM1AmK1EVgQgJRrbz3m-ZKWjCbJ2keTfF6gfM-MZNy13nLW4Jaxt9jtJbFMHi1msxE9W76sNxZ2orhgSJ0fUixZQcbfxhtS1TQ3mT5t3paql_TC-krwpB3oUBdprcKBnnZ9JScAICxgLaxuoiDkUtm4TjUK5lfvkATmSCvw5F4MBFRS-8ChXDkN8A59xKnw6oYTuxR5g1NgZlMz0G5k-L0BXNPJRyQN2r9p2DBTH64QlK0Hk0tKAQUz5ELMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و زیلوهای آبی رنگی که آمدند تا برای آخرین بار فرش زیر پای آقای شهید شوند
تو چقدر با وفا بودی زیلو..
💔
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/666173" target="_blank">📅 04:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666172">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=gc7z-3Fsugc9T4TVB401hnfCmOL-w5S4nqkNlA1IRyU1xUiWWTH6M6TUPhA5iA4Cm-711pmA3hbUcSRHgsmHU2NCnMF5kx2FtVbzIao2sUzWGNLX1DTtrB0rsxE0sQQo_SafYQodeEUx53i8D18tAcWdKRRsrQOVjSoZn8AJagMmSqXoUCnWN5JzsOjDIHiEQ1lpM-G_9LLXdJcSTcmuBo2ZQlZfYbZlgMhDCThvTAPTlwY-QTgP3sQlfGGOtZQmQ4vPL4n7L6tnz0k4TwtfsXZNSl9VmZysTRrgTEN-kJ9P6gLYgqaSGHhZf8BVtxD7AeAlbgkcbdqVyVo5l8uNhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=gc7z-3Fsugc9T4TVB401hnfCmOL-w5S4nqkNlA1IRyU1xUiWWTH6M6TUPhA5iA4Cm-711pmA3hbUcSRHgsmHU2NCnMF5kx2FtVbzIao2sUzWGNLX1DTtrB0rsxE0sQQo_SafYQodeEUx53i8D18tAcWdKRRsrQOVjSoZn8AJagMmSqXoUCnWN5JzsOjDIHiEQ1lpM-G_9LLXdJcSTcmuBo2ZQlZfYbZlgMhDCThvTAPTlwY-QTgP3sQlfGGOtZQmQ4vPL4n7L6tnz0k4TwtfsXZNSl9VmZysTRrgTEN-kJ9P6gLYgqaSGHhZf8BVtxD7AeAlbgkcbdqVyVo5l8uNhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه‌خوانی نریمان پناهی در حیاط مصلای تهران
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/666172" target="_blank">📅 04:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666171">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c5542627.mp4?token=MtZP1y_V_cX7yaaj1g9MnblZG1F1NYVlvkOpR2PmEx0uYydWEYmo02QUkVU9OOtSIeH7oJrruSgtBDDV1B5Dn19NEctrR16nYC-o6CYEKQ_mZRiT2ZmGA-3bhkXkXuwRDQU_8Ddk_zD8XlbQrD47Tzd-8EsP644_sM99VaGwv46DaA6v69u-0BRXsR72eH1iXCiL07N-v8IWBLCFtblZX4-H1p-1AFDL-svB41kA9lijYFaQ3g8ehOHMKUivhCbk2n9IkS6SOfVw7AbR8v0GNwvdPRvbir3M64lqQpgok3tSCCaN106juV7ted2z-zWG6UmCg0holrJcqgCOIGsY7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c5542627.mp4?token=MtZP1y_V_cX7yaaj1g9MnblZG1F1NYVlvkOpR2PmEx0uYydWEYmo02QUkVU9OOtSIeH7oJrruSgtBDDV1B5Dn19NEctrR16nYC-o6CYEKQ_mZRiT2ZmGA-3bhkXkXuwRDQU_8Ddk_zD8XlbQrD47Tzd-8EsP644_sM99VaGwv46DaA6v69u-0BRXsR72eH1iXCiL07N-v8IWBLCFtblZX4-H1p-1AFDL-svB41kA9lijYFaQ3g8ehOHMKUivhCbk2n9IkS6SOfVw7AbR8v0GNwvdPRvbir3M64lqQpgok3tSCCaN106juV7ted2z-zWG6UmCg0holrJcqgCOIGsY7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در مسیر زیارت رهبر شهید، کوچک و بزرگ وارد مصلی تهران شدند
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/666171" target="_blank">📅 04:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666170">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
درهای شمالی مصلای تهران هم باز شد
🔹
درب های ۶، ۸ و ۱۱ مصلای تهران در ضلع شرقی و درب‌های ۱۹، ۲۰، ۲۱  در ضلع شمالی به‌علت ازدحام مردم پیش از زمان اعلامی برای آغاز مراسم به روی مشتاقان زیارت رهبر شهید باز شده است.
🔹
مردم در انتظار ورود پیکر مطهر رهبر محبوبشان به جایگاه تعیین شده هستند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/666170" target="_blank">📅 04:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666169">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOsQqCVXhZZiizw1wkdlqUehwH0mUINhDy2D8o235g5XAt3bYfogiPkEOAPFYv_yBnR9Vek0YVNp2sc0OZRgUAzpZW6VVfoQgsELAe6AqIhbkNXv4RNYKviGzjyucKuDNx7RLhJOzmxBn_jiVp4QBf_QzFGRF_fsXlgnbyoDM7wyrC2R8bIMrGW8FHgQ-_3B9R3Q9jP_2nH5dmmWd8VueCbOnz1KBplw2jzamwc_95nYxOlyJuCSGSdjJiZXdy3DTMrCvX2Lot0Q8Q1UU5aTEEYGmO9VDe5DerCGP5k0CqOAImZ9OtbFhG2gGzHaSXi7tIKHYscTJwfFzNLbR_6g7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی از فراز جایگاه پیکر مطهر رهبر شهید انقلاب و افزایش تدریجی زائران به صحن مصلی تهران
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/666169" target="_blank">📅 04:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666168">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA1FiLsfz3lmECj1kEw9wl01fdgYnksei_kTRUGDwy7pG0kKmOAODAlpBopsRU8I1Z1ED0BwCuON50OBA-OBtv8UmhSktZ5TUCzBDGTcNmbFTOG8N2iPA8M5K9kIa3W71S5rhwo0gwvjRIUIQPsdN2u8zelYVIFZIDWrb58LjZboJGzFbVBhH9vhvy_PZotuzGB039wor5B4K-s2anftRbkg3jj8qQMGsQ5aOLHx_BL3TuE0Ag6uu5OcxqtA1Q5pKBEjYASB00pkDu3XRWAW60bQZ_YRFdamGP55T2b_4Bvq-4yJmn1lKE2WplOmdxEgmMAMnNCteee1-Q5DnqHn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دقایقی قبل رفته رفته درب‌های مصلی برای ورود مردم بازگشایی می‌شود
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/666168" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666167">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51b0270fa.mp4?token=CAvF_C9SHw84xMxw9KwTkT7W4pSva6RT1YUH2HC6t6fMjALus6eJBfo-ya-z_tfSzPWeJlXMkFwyTTBiqOXiRzcP0PEiGYdPSWvDtUhD_Gap4aQS4ZQFxSEszXQHe_GPc56hzrfuOJcqyzlShIY3we2knZ3riuLzxRCwlbUlXbhTZMrG92Kv8SPRoJUTz6UV2sxkAkWRyvkEcFyRcM1RXvRcYnz5zLuGO73I4Vhdht01n1MNX8f95EpNyCrgiTQ0RzezoDGhLVbpoYoQxstpyIUmx7z8GEERktV1IIvkK_y06YM-3IQz2D18DSz4dxeQUvnvBHQXM9YMk_UdExg_VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51b0270fa.mp4?token=CAvF_C9SHw84xMxw9KwTkT7W4pSva6RT1YUH2HC6t6fMjALus6eJBfo-ya-z_tfSzPWeJlXMkFwyTTBiqOXiRzcP0PEiGYdPSWvDtUhD_Gap4aQS4ZQFxSEszXQHe_GPc56hzrfuOJcqyzlShIY3we2knZ3riuLzxRCwlbUlXbhTZMrG92Kv8SPRoJUTz6UV2sxkAkWRyvkEcFyRcM1RXvRcYnz5zLuGO73I4Vhdht01n1MNX8f95EpNyCrgiTQ0RzezoDGhLVbpoYoQxstpyIUmx7z8GEERktV1IIvkK_y06YM-3IQz2D18DSz4dxeQUvnvBHQXM9YMk_UdExg_VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج مهدی رسولی: ما در آستانه تمدنی‌ترین و باشکوه‌ترین و بی‌نظیرترین تشییع تاریخیم
مجلس، مجلس خاکسپاری نیست؛ مجلس قیام لله است
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/666167" target="_blank">📅 04:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666166">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr8wvGm6M_NiWOTQvFSnkwl0oA6b4e-BaBhzpE3Olo8LfMC4iJK7hmoz_wRB63FnQBh_V4XHtkBdAOc51HyjkWrNRl4nqPlhbfePNZYyMntuqnwWFk6mQfEP0vlANQenMvzSym6jHDZSeQQNU4MA-UMuCGYrfV0vmEFE7Ya6oTh4EhkSu1xB7m5A3UOn02g2d9k5_UcoTbD8DbaXdYX1WSw0AljPjU-zGhAGty6Re5AhHTjWuYiRfKBYxXM_a0d_jUBC6kBAvVjQgAP91_spMOJwlzieEzxXPNCVmXFrM-9svHORdFGLWNZ7atj2fPnAztcYGZvB8ZaYC0bzC2boRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه مسدودی خیابان‌های منتهی به مصلی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/666166" target="_blank">📅 01:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666165">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb537e4fe0.mp4?token=NUS9O-n3SJ7n1NmjMqoRvkWS15SZFHMYUXVnorPJA3PW0r17drxfaH1kTpZYpSgRH80vhuoiIMlYDsoSv2PPCiBu09N3fLpjf69vE0C1qout4gsgtnlp7B90_WCvMzMP3WrKalT4Gnes40kBxCEu4YZ71o6Jn-LYTnuBG5UnzMPMMzSKKqyuJyTcZyUZQf0KpmYN0TdQ0VQM2TxwVDumasunYsS0kCWiHo_hMaycPjDR45nY-V3JvI2YSoNBcCW9ZDnYxn24Gpc0FrEZqDdk8qfYv7vZTgOikO4YA52jKIHvb3MUCsTF-tJKRWcdtziv7GBKZa7SWls03hdy814p-T4rSPBMz5IkxaLkKwXhFUBz8ZeNr1NqXJjagwT_cAwIXt_MHEFH9eKz_V3mbBgmA8r1z_RPaqzehcpJ2ip8afmtwqZErJVKMcy-6h_FE_5gCgC1Nt_krZBgtF_hJoJJ3tpa5BRj2gAa-IFgMLdPWK7OQkBh3C44uYu6miUZShYPx4smSfSty_7ys4krbbhJb_--0tUDwkL99qlz-6Vq1vI8ILwKmFuU2SoVc3BeZnbK-y2cFDz1UwcyG5ZeE3-XKeXAe7GYRd0Z6F5Ub7aGsqUZ2AcuzERLHBT7_BaJMvKvzLOMuuHuyuIYeXFe91BeOtUqvUl1i7BhPxnMHIKALbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb537e4fe0.mp4?token=NUS9O-n3SJ7n1NmjMqoRvkWS15SZFHMYUXVnorPJA3PW0r17drxfaH1kTpZYpSgRH80vhuoiIMlYDsoSv2PPCiBu09N3fLpjf69vE0C1qout4gsgtnlp7B90_WCvMzMP3WrKalT4Gnes40kBxCEu4YZ71o6Jn-LYTnuBG5UnzMPMMzSKKqyuJyTcZyUZQf0KpmYN0TdQ0VQM2TxwVDumasunYsS0kCWiHo_hMaycPjDR45nY-V3JvI2YSoNBcCW9ZDnYxn24Gpc0FrEZqDdk8qfYv7vZTgOikO4YA52jKIHvb3MUCsTF-tJKRWcdtziv7GBKZa7SWls03hdy814p-T4rSPBMz5IkxaLkKwXhFUBz8ZeNr1NqXJjagwT_cAwIXt_MHEFH9eKz_V3mbBgmA8r1z_RPaqzehcpJ2ip8afmtwqZErJVKMcy-6h_FE_5gCgC1Nt_krZBgtF_hJoJJ3tpa5BRj2gAa-IFgMLdPWK7OQkBh3C44uYu6miUZShYPx4smSfSty_7ys4krbbhJb_--0tUDwkL99qlz-6Vq1vI8ILwKmFuU2SoVc3BeZnbK-y2cFDz1UwcyG5ZeE3-XKeXAe7GYRd0Z6F5Ub7aGsqUZ2AcuzERLHBT7_BaJMvKvzLOMuuHuyuIYeXFe91BeOtUqvUl1i7BhPxnMHIKALbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میزبانی از دلدادگان در چهل سر، محلی برای استراحت، پذیرایی و خدمات درمانی عزادارانی که از سراسر کشور به تهران آمده‌اند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/666165" target="_blank">📅 00:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666164">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgjxVjvGw0GsbL4ahmi3IukMcVF_hrKpFJ62PaOF_6aRrdBNxu4PH2ABX-7E142NQrzbn8liz6sU3BIzKs9EwRMD4WTRtF5PKqkzGebqTGY9TBGsgLJhD8p7JmdrY0JR2XHxgFDqO_1_SlcPsxEIbSlA4BBsnc9M9eCZPI5-cMnovrRJcSTPS2Bo2onTKhGJER4EN77OvqIgF5n4iv8C9OZ5h7-9dPrBvKW6almtn90ugfFHKkPJwDCrDqzue8fUWrGE7hvCcGgLtKJOnrDVs_3fVUBO_bbI1RoAJkSdxcdHZT5fPxdOzYtrSUS15T3UklKPXAE4ZG9VcXpDEHPv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های صعود کرده به مرحله بعدی جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/666164" target="_blank">📅 00:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666163">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxoL3poJaa_wkICiDJeaEQ_KusXJYags5mbuDYmBs-XPW1pqUeT_rRh6xD1EyAC5nk_0oD3RxHiyh26yz6gaYOIlng_rZ8666NlOpyyNFVpHrcsx0-O5-Mawfcz-hlk4kkkbMpoPIfiVBbQeh3ZaH6-3tnOmapxoA7LGJ96lGePqBnY2JRGlk4Du2LihkjshtausXhux_M7HAAn5QwDnPrxS5qJcrOq4zA6MOB55FL-9yG3KeWLQEhG7aY9_nRnp3JEY3YYoTSRn8mYC7eNvEytWFsUJq2rFUpqDKFDy6NNq0UVkpQ6vMnMxa4en1K2CvCGlIglFZ4GTe6o8sUe5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقریبا تمام جهان برای مراسم تشییع آیت‌الله خامنه‌ای در تهران حضور دارد
ایتن لوینز، روزنامه نگار و تحلیلگر آمریکایی:
🔹
به‌ معنای واقعی کلمه، تقریبا تمام جهان برای مراسم تشییع آیت‌الله خامنه‌ای در تهران حضور دارد.
🔹
روسیه، چین، عربستان سعودی، قطر، صربستان، هر دو کره، ونزوئلا، گواتمالا، گرجستان، ارمنستان و کشورهای دیگر.
🔹
کشورهایی از همه قاره‌ها و با پیروان همه ادیان گرد هم آمده‌اند تا در برابر امپریالیسم آمریکا متحد شوند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/666163" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666162">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
خودرو شخصی به مرکز تهران نیاورید/ برخلاف جهت جمعیت حرکت نکنید
سخنگوی سازمان آتش‌نشانی:
🔹
از مردم می‌خواهیم از آوردن خودروهای شخصی به داخل شهر خودداری کنند.
🔹
مردم با استفاده از ناوگان حمل‌ونقل عمومی به محل برگزاری مراسم مراجعه کنند.
🔹
یکی از حوادث رایج در تجمع‌های گسترده، گم شدن کودکان است و خانواده‌ها باید در این زمینه دقت ویژه‌ای داشته باشند.
🔹
مردم از قرار گرفتن در کنار ستون‌ها، موانع و سازه‌های ثابت خودداری کنند.
🔹
به همراه داشتن آب و تجهیزات محافظتی ضروری است.
🔹
به هیچ عنوان برخلاف جهت حرکت جمعیت حرکت نکنید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/666162" target="_blank">📅 00:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba94eddbdb.mp4?token=omvxc8ybsT63rsOEYqJ53YvLt_wcc7G7BnWpYSjSTypJSaEY5fXGn96N0CRDpRpDPTMVdwhum0RPQsvFkf6nvu6XSwy8Z6bP9W9ckfRe6tRcg2zgna1ldV5yLrTSaHeyIKrFjXRRrfY0bWlcUfKxYR3L__YyPre3dJLEELvsTwNadtaoPCx9Cv5w-EF2fonF6OBtXEmbahyIodEGTAao8beiT0xv7uWfnkcxYVkcz9LvtBiE1uJiHw7zd-sfj0TahiKelJhCkVkSdHSYTCjcuhjDG9_BSPbScLO2z3v9BymOi875af9U7Xemr2Nai73DOd-lTM6QPdftqecJc-MhYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba94eddbdb.mp4?token=omvxc8ybsT63rsOEYqJ53YvLt_wcc7G7BnWpYSjSTypJSaEY5fXGn96N0CRDpRpDPTMVdwhum0RPQsvFkf6nvu6XSwy8Z6bP9W9ckfRe6tRcg2zgna1ldV5yLrTSaHeyIKrFjXRRrfY0bWlcUfKxYR3L__YyPre3dJLEELvsTwNadtaoPCx9Cv5w-EF2fonF6OBtXEmbahyIodEGTAao8beiT0xv7uWfnkcxYVkcz9LvtBiE1uJiHw7zd-sfj0TahiKelJhCkVkSdHSYTCjcuhjDG9_BSPbScLO2z3v9BymOi875af9U7Xemr2Nai73DOd-lTM6QPdftqecJc-MhYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو دوست داشتی با این شخص دیدار داشته باشی؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/666158" target="_blank">📅 00:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666157">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or5Dv8cH9QZX8LfnocpWc3yH_wWVmSrcsPVN3uRyfDCcldMLKr8HZ2nqExsRwHgj-BrPWLr0ggyNqf3ZpTkuPAk6epWaViE9_8_2Z_83wcxH7lL5b1bbclIfr1PiRkLReldKbH9R2o1xBqf4Yrj9Q7A_EkYXVudtmQKcw9Lmqq2SFHCJINcwuz2-YJY1bOvqvDJnRLt5_TtZI7Sm9nt_SwYQGftff6iEauyti8rQ5lhjq09nmKQz5XdsoNUBYlLloUwLnWQnkwEdc49Gu3-pJtaaiqCGu9kbHEC1nd5qfV6JkcQiqUbXrU3Gj-jwUihldBgJTewY6bq_xJNjTUO2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مصری‌ها در ضربات پنالتی صعود کردند/ آخرین نماینده آسیا هم حذف شد
استرالیا ۱(۲)
مصر۱ (۴)
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/666157" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666155">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290eeb6909.mp4?token=a2Ui4qt-Sloz9Mx-c_BhD6D-zWFoNRMMfi91ZvfTyoVGWxpSwE-uG_zhFaLlHarREox9gadIP1Iqij1Az465AfWSdd_nkO9y2Y3YYAWYU9eBnGz2HW2XvaD9pDCgUxMa8tahC9QSDCw3plUSyM70tUO6YkqQ8NMap6HrG_KCSCy02Lu6xvJlERezC4uK9PgWCkBcPhau7Vi2633HchZY5sS7eGNoZSr_Dsxxwz_LhKU9g-mYSL1eeAtukwCbzJct2D_C38lgCHg0T0D3eM5P4tL3lsq0FVXSlSaAI_fM4USx3qPyUCKqxOHqCJi2JHu2c_vk4DnoPDN_0JZpFIF-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290eeb6909.mp4?token=a2Ui4qt-Sloz9Mx-c_BhD6D-zWFoNRMMfi91ZvfTyoVGWxpSwE-uG_zhFaLlHarREox9gadIP1Iqij1Az465AfWSdd_nkO9y2Y3YYAWYU9eBnGz2HW2XvaD9pDCgUxMa8tahC9QSDCw3plUSyM70tUO6YkqQ8NMap6HrG_KCSCy02Lu6xvJlERezC4uK9PgWCkBcPhau7Vi2633HchZY5sS7eGNoZSr_Dsxxwz_LhKU9g-mYSL1eeAtukwCbzJct2D_C38lgCHg0T0D3eM5P4tL3lsq0FVXSlSaAI_fM4USx3qPyUCKqxOHqCJi2JHu2c_vk4DnoPDN_0JZpFIF-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه اتو زدن پیراهن مردانه را یاد بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/666155" target="_blank">📅 00:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666154">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7490dc516f.mp4?token=MIYVTrELfkNtBQ0KAIOgvJsREbyxuQSygwCDd82_25SGD6NLrF6rs7RmzQNoIjDhYdEInJgw0Q3h7UijI1rDfOLOr91t_MeyKSm0Va5SXAvkWJFmmT7lWGsOF5QYrxoP14yERB99pEcAuoJq4beg_7GjYjHC-byuUOO720WZVpEP099wWYA13RaxqvxQ4t0n_zvguELcbCzecB_Wicesk_jDDGjuUFnfz2vPmFgqg6aUiqgwPeOBF_-mmS35J62B2iwf3TRaf7tHgYg0ZlwlcxZcsfQa-fyOZC-8ZxV6MO-aKMmwdkAzLrIqzSvLvjyXBbuHWYtWdFSam160h1_2X4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7490dc516f.mp4?token=MIYVTrELfkNtBQ0KAIOgvJsREbyxuQSygwCDd82_25SGD6NLrF6rs7RmzQNoIjDhYdEInJgw0Q3h7UijI1rDfOLOr91t_MeyKSm0Va5SXAvkWJFmmT7lWGsOF5QYrxoP14yERB99pEcAuoJq4beg_7GjYjHC-byuUOO720WZVpEP099wWYA13RaxqvxQ4t0n_zvguELcbCzecB_Wicesk_jDDGjuUFnfz2vPmFgqg6aUiqgwPeOBF_-mmS35J62B2iwf3TRaf7tHgYg0ZlwlcxZcsfQa-fyOZC-8ZxV6MO-aKMmwdkAzLrIqzSvLvjyXBbuHWYtWdFSam160h1_2X4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار CNN که مجدداً به تهران آمده است، از جزئیات مراسم تشییع رهبر ایران می‌گوید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/666154" target="_blank">📅 00:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666153">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aadd1e25.mp4?token=Q-XxJHkqXb0ntD3VZGk0gW_C_ZLksB509bAvzhl1UJz_MOIhYNu8wXRnLWro4_QPxiBqOMWaL42FB2-PTrnJFLRLqVTFFAkooN9UriLl_TWbZApPleeqW_LGwoMibvs0oIntZoRH6ZnPTLtnoxu1IiWGx2TLBtGJHqDYKnob612napdG-D5dw54a7TBlJoryUx6cqeChWveXKYi8o0g-sFTUgadHoYi4mLH9ZbbbtAh9iNsSdZmBWJ9hjToq9tgenkgWajnd0n6El9UCH4PiY7VGc0Ge7phADKc_5ct1qKguiHf5-zInFVIPxpUpN6MeNWHSQfG7JG0AMlmmr08EhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aadd1e25.mp4?token=Q-XxJHkqXb0ntD3VZGk0gW_C_ZLksB509bAvzhl1UJz_MOIhYNu8wXRnLWro4_QPxiBqOMWaL42FB2-PTrnJFLRLqVTFFAkooN9UriLl_TWbZApPleeqW_LGwoMibvs0oIntZoRH6ZnPTLtnoxu1IiWGx2TLBtGJHqDYKnob612napdG-D5dw54a7TBlJoryUx6cqeChWveXKYi8o0g-sFTUgadHoYi4mLH9ZbbbtAh9iNsSdZmBWJ9hjToq9tgenkgWajnd0n6El9UCH4PiY7VGc0Ge7phADKc_5ct1qKguiHf5-zInFVIPxpUpN6MeNWHSQfG7JG0AMlmmr08EhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی محل استقرار پیکر رهبر شهید برای مراسم وداع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/666153" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666152">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpAQDV8iIlxzqrgp--5m8KONF-PZuYq9KyX8WXuPxyygJTKdEqFuFsxZnGR7YTcOAcm83g1JawRlTUHKVXvLZhN4aiqpw-tgvrrytAGOdAJhFIw4p1irDouv67BYobROFpkynuwcq-4maVnl5N4vy3uwgNOCorHfO5oXbFmFXEO9s2ZJwOsNWLpBq5YK_PzAhxP02a2gB68yynaWQ3IoJ9cHoB7RKHm24GLAgE2uY6LbUrN2tJq3VKEJbx_pHPUIFy0II9pYJel2HfpA-gE1mWgVkZKYa4IyUQzrcdSa5qaefoO3BovuBxsEipFrmpIP-9nL7oCdXgkGapX6hYxo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد هانی در تاریخ جام جهانی رکورددار یک آمار تلخ شد
🔹
محمد هانی یک رکورد منفی تاریخی ثبت کرد؛ او پس از ایوان ووتسوف، مدافع بلغارستان در جام جهانی ۱۹۶۶، تنها بازیکن تاریخ جام جهانی است که در یک دوره از مسابقات دو گل به خودی به ثبت رسانده است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/666152" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666151">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار گیلان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5baacd183.mp4?token=X8h8yacHSVdxaiHPtV7kF9dBmeK1nUPfvKuo_jBSSx-T5PiLZocXDb8IBZru2HozGvqGx2iDU1lwdkJS46xD_TlNRifgG909Za5NbPqPFXZseRRjWzo40RchLj_5ji2jNLZsYUrMTWjEFMItSi4Iyx8cCqkFfhxNYCnA7iJWHYtFp-yqK4kOLK-uTrwsbIcP33ocFXISovjU_9dkT2xITG6YN6Rvu961Q1Clc-r8wklYllxRHHkeAGqwt6_ESp6AoJkBVU7Z9xjCcxdmP67HJ3fIwujIxspGgdSxW8qnkZsUqrPEaieBX7-sp5GSP2nxnaGz33yq_uNCbkdGuRXf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5baacd183.mp4?token=X8h8yacHSVdxaiHPtV7kF9dBmeK1nUPfvKuo_jBSSx-T5PiLZocXDb8IBZru2HozGvqGx2iDU1lwdkJS46xD_TlNRifgG909Za5NbPqPFXZseRRjWzo40RchLj_5ji2jNLZsYUrMTWjEFMItSi4Iyx8cCqkFfhxNYCnA7iJWHYtFp-yqK4kOLK-uTrwsbIcP33ocFXISovjU_9dkT2xITG6YN6Rvu961Q1Clc-r8wklYllxRHHkeAGqwt6_ESp6AoJkBVU7Z9xjCcxdmP67HJ3fIwujIxspGgdSxW8qnkZsUqrPEaieBX7-sp5GSP2nxnaGz33yq_uNCbkdGuRXf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب رهبر انقلاب به ایستادن مردم در زیر باران در هنگام سخنرانی ایشان
@akhbaregilan</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/666151" target="_blank">📅 00:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666150">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2uE6nKR_5d7NPdPI4adzh7wdkQ2RQpyCGBlzbSlQb2_1tft7VdMWos8meOAlDkFdq1MQrUIAqdWNRb871STSoC8sw4PVhk6BE-nL-jA0oDzRupceNFQuT_bAVeE73PcW0A-oP6WjE2pU99D6FoJGOTXoGHB8cL5OhS4rPiMRtWz6KlpogkPMRUJdkrec8Y6QpaptiMVdllbd0PFMXxIFWMklnAZfz82wRIauMIKas4Ugh4shkK0sUafM8Qg_PtsybOmcOPTVMDB3dq-mboZNeE9tdOOWY3zRZsGJm9ImMvXZhXe65Ur2XrHOujaohoKv5vOmXutRsUvvwZxx2tIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرخی این مچ‌بند، یادآور خون شهیدان است
🔹
با مچ‌بند سرخ در مراسم تشییع حاضر شویم.
🔹
تا عهد خود را با راه شهیدان تجدید کنیم. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/666150" target="_blank">📅 00:01 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
