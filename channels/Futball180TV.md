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
<img src="https://cdn4.telesco.pe/file/O4yXg3uUySvxP0Mg4CCsMoQgBR1_meuFPrzg50ntr43055xuUILcM-Wgtz5lFgDbJpjoBD3qlvIbHFkaM7GDawEGodiFnY7eYSW-nDuoBPzNwvYakulSZEgGHzTWRSHZf12gqP9HT3KaGWFSHeD1ATnx5Wp5G7EKw4X7lrQPmXztgKBIQdZpEH6i-69jynifp8qHEq3y8JrtDoU64_hSnDT923GidIxU427yFePV91x78zII6PnpSMEY7xUihmngaHez6Vkjbg0AkBSuNn4t_uzqIcFfyWjD4A8kN3mDsw9ca_Vr7tiiU_jOPryuUAy3ZwABzz1sA6ctA_IFJqlkYg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 126K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 18:07:08</div>
<hr>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🔷
جواد نکونام سرمربی سابق استقلال از طریق ارتباطات خود با افشین عبداللهیان مجری سابق شبکه ورزش که نفوذ گسترده‌ای در هلدینگ‌خلیج‌فارس دارد، خود را برای سرمربیگری فصل‌آینده استقلال معرفی کرده هرچند که در این میان تاجرنیا قصد دارد با سهراب بختیاری‌زاده در فصل‌آینده ادامه دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/Futball180TV/90212" target="_blank">📅 16:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkpK8U4X9BoBkLi2XIrWPfegBUU-iGkTpsXSQVrZdHkziwRir_Tw7GiVTSjIj6Jg1cKs67VYpL4K3lLdJZSVpQ5TstoMnUtT2na0TGJrdx2EAK7tsp_IcR7C0l5GabSb_aaBWuGfPFxKk8fJ9cHdE3aB1jto3An3QNirF9-JsviIBObwLJBg4d7qks9cWC8I1s0xy8btocpkKjgF71lD8uPxv6ID8nmeZSol7XGj_BvlAq0V0UHztEtNO53Rpo-74z_WLsHQ1NvTIlDs-7Rm2lkEq3FRiOLYi1rV2xzV65yD7nQcsqTfPp8upJOn2wtPau5sM8QKK1RRB1TYSeWgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست تیم‌ ملی اسپانیا برای جام جهانی 2026؛ بدون حضور حتی یک بازیکن از رئال مادرید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/Futball180TV/90211" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/Futball180TV/90210" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ستاد راهبردی فضای مجازی صبح امروز موضوع اتصال اینترنت بین‌الملل را مشابه دی‌ماه سال ۱۴۰۴ مصوب و به رئیس جمهور ابلاغ کرد تا در صورت تایید نهایی،‌ وزارت ارتباطات موضوع اتصال اینترنت را اجرایی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/90209" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=KrWyggHqbh3sZudn6KW_6MghLx0euA9lM8kBFF47NkQH7U9C_mz-oMZfwPqdssQq61zjAYY8_nU8cy-hDYqIBFIV66UulfQrvWuPC0Z8zi3-uILhFSKN0-IRuD5UnK2pbX1g9UY5nUIXRKlrdjyzXpDfgYbth6S8UnbU9f3YZvT0Ax0P2Zwjmrbru3s1I9R2gKkY8ZGNTm5j68KGRqh-Y5ZEFgWyKw4LNldKsPeXgaytfu7oCsU5MyJXE3Je5Kkg8qN1oG-LwU-VkedjS544mQ4xQ1yp3J02KUkWfz77_MytFNJe6CKG6ydVLTh4_s81Lcyt2Hug7O7CLrYxei4UsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=KrWyggHqbh3sZudn6KW_6MghLx0euA9lM8kBFF47NkQH7U9C_mz-oMZfwPqdssQq61zjAYY8_nU8cy-hDYqIBFIV66UulfQrvWuPC0Z8zi3-uILhFSKN0-IRuD5UnK2pbX1g9UY5nUIXRKlrdjyzXpDfgYbth6S8UnbU9f3YZvT0Ax0P2Zwjmrbru3s1I9R2gKkY8ZGNTm5j68KGRqh-Y5ZEFgWyKw4LNldKsPeXgaytfu7oCsU5MyJXE3Je5Kkg8qN1oG-LwU-VkedjS544mQ4xQ1yp3J02KUkWfz77_MytFNJe6CKG6ydVLTh4_s81Lcyt2Hug7O7CLrYxei4UsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین ریکشن‌های پپ‌گواردیولا در منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/Futball180TV/90208" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90207" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/Futball180TV/90207" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJPnqqHmVgE2u0BwdTtDIkHWcJP8MunfKYk_nsCoxOw89p652xdJ7IZw-rM_nlpUvfOtcxPzoUJMgUKqvPU8XFbzkWdSIDTdHpQcprIxVyyCXbQ38jPIhpPhTqqR1g41ylOev1qf2tYcqYcBqU1rPWlGl_et69lW_0tEFq3JP2SKBJWaMhpt-rD4ERsOoim1JbbZ04eB1gkYleAl_yUUmPtgTtC70meNfSBUcEPgvVwWED6UyXV9q_OwZDZNE0qgO5xiXkbwZBQQtbgkyoTf3qAIm0A-x5AfBOpQ4dikOnUKa1n7Xkiurtu99YZDzZDZ3dgcUODqmhtqyLfMKL_Cxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/90206" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940870b589.mp4?token=nr175n4iKAJ2HpX6UKgRjtAo7NQdu9NsCtjwpN7v_fZ0Exh-j1F5itJPPfnzserkIPfYPps877KFITxGSglnpWYkjk4FLTZUqPYiLgY3LijvGq9uVDjGRCXAzrjjBdt0lqlQZA_rlxXyLAeNtbZir1EzAcohmhn9Ag1HLJXaKcJJCeLFh0UFmXuu_NLmZNJvtVVwGGn20QQksuyLfMFa1C2Xr_7nnan1p9yo_yCqpH-uT8Id8cWU9lLz3tE6X6j6kXTWJ3hk-AfCTawNqnLapDTWjnGWqGQ5OOw1ZDjmgGVn0KRTgsVLpbaULgVOOnyFUOh2CG60auaB4wjXIugLOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940870b589.mp4?token=nr175n4iKAJ2HpX6UKgRjtAo7NQdu9NsCtjwpN7v_fZ0Exh-j1F5itJPPfnzserkIPfYPps877KFITxGSglnpWYkjk4FLTZUqPYiLgY3LijvGq9uVDjGRCXAzrjjBdt0lqlQZA_rlxXyLAeNtbZir1EzAcohmhn9Ag1HLJXaKcJJCeLFh0UFmXuu_NLmZNJvtVVwGGn20QQksuyLfMFa1C2Xr_7nnan1p9yo_yCqpH-uT8Id8cWU9lLz3tE6X6j6kXTWJ3hk-AfCTawNqnLapDTWjnGWqGQ5OOw1ZDjmgGVn0KRTgsVLpbaULgVOOnyFUOh2CG60auaB4wjXIugLOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیگه محمد صلاح تنها قدم خواهد زد.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/Futball180TV/90205" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=Jsyq9ic7347W3zHaAhAAmZo9ABSLFE8vwAr-jceFdmhF7pNeHnLD-4s_KsRTay7c_Wp0yEPotb222THmpZfnzpzXdu0NZ8OdGD1leet6D7b8cWPC_7oMeqGgMOMGH_vF8IfH7fdkJMrYxik3jDSU5IhzdpnTHcrjHV8VuijN1FubKxTqy1iWUiyfewpqE026ilTULWyQ3ZijRCbhUrATKoWrRvESXZS9hhC5rTbaOFJ-6ZBt78_5Ia7XrgN8rB8odjjDZfBdLVcWtZ7K10HP54gZz3K85FBirak3oZBjbpfLEqMpIpBXzgkUZf5v7FT_hyJoWfjyh8fNa-ap1-eeAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=Jsyq9ic7347W3zHaAhAAmZo9ABSLFE8vwAr-jceFdmhF7pNeHnLD-4s_KsRTay7c_Wp0yEPotb222THmpZfnzpzXdu0NZ8OdGD1leet6D7b8cWPC_7oMeqGgMOMGH_vF8IfH7fdkJMrYxik3jDSU5IhzdpnTHcrjHV8VuijN1FubKxTqy1iWUiyfewpqE026ilTULWyQ3ZijRCbhUrATKoWrRvESXZS9hhC5rTbaOFJ-6ZBt78_5Ia7XrgN8rB8odjjDZfBdLVcWtZ7K10HP54gZz3K85FBirak3oZBjbpfLEqMpIpBXzgkUZf5v7FT_hyJoWfjyh8fNa-ap1-eeAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت لیونل‌مسی در فاصله ۱۷ روز تا جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/90204" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76980eb486.mp4?token=emilLiu6FPCoEBAq7v5fdDRc-jPhCss3yyKD7j-oUXKyFll2bNNeTG0Sx-Ah6yCzlRxH4L-GEw2FiOLj_w0vvkkr5lqN0ni8oB2pWp4RWfU5CO3EAQL3goBcVasAyXSN42-KmjaQ-2xyf0uE6KUW_ri7PADQdEj2-gVWqtxsh4sn8hNbJrXd9DffofyDrhMaHFt9OoyRAkXGh44xmwCoJnbQWeNVfAQA8r1rgt61UjwckLQD5etQA1Kb04BzkyIsUnGSRZ-aS0PVz4i0IDkbmL5_9Eb1xrzhKScFQL10DXgu3LqYazkrSLPRPz2kXO2VFTFoa_Ncf3prpwVBk0uUVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76980eb486.mp4?token=emilLiu6FPCoEBAq7v5fdDRc-jPhCss3yyKD7j-oUXKyFll2bNNeTG0Sx-Ah6yCzlRxH4L-GEw2FiOLj_w0vvkkr5lqN0ni8oB2pWp4RWfU5CO3EAQL3goBcVasAyXSN42-KmjaQ-2xyf0uE6KUW_ri7PADQdEj2-gVWqtxsh4sn8hNbJrXd9DffofyDrhMaHFt9OoyRAkXGh44xmwCoJnbQWeNVfAQA8r1rgt61UjwckLQD5etQA1Kb04BzkyIsUnGSRZ-aS0PVz4i0IDkbmL5_9Eb1xrzhKScFQL10DXgu3LqYazkrSLPRPz2kXO2VFTFoa_Ncf3prpwVBk0uUVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ در گفتگو با بهاره افشاری: امیر قلعه‌نویی واقعا غیرت و معرفت دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/90203" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90202">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90202" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/90202" target="_blank">📅 01:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90201">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAtCujC-2E2pJlia634ejqXgSmqFBXYkIqf07w8jYy-rHGuAZLalcFDy0K1EqlFqp6Jg43Qy7Yk2-tk2VwXjGW3tnzxH_P538IFc3BYp2d20nA6F8foRHlyuyMN7fd9sLS3SVFlxxgto7-VvSSYTTKyNtRhzW6TEJMeFOJNI5pT-C_76LDrJ0mbhEYqjfTUPkJmnPgOScEiX1pAI5QurJoO4OwtWCre-RCNHwAixulsuLycq4-GnLPy4AINILXfg7P0Ug-DI60e-h08bjK3tZjPCLj20cPM9OrY32OIIXf-B7bwtDPvXXMmVhpOXF31MuPV2PiKQxPXbKZ-leblxVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/90201" target="_blank">📅 01:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgzny8jd-yJ8RvVYYOpwzH3JDWSqKvWfj9eWa2Es-ouVl-EicGbPGHtH0Y04S3NysfZzzBILiLF-s5MNRi0L7rljQeBXJqmrd_TdCGObPj9sqiv5LEOfNQV48F4nFaAyqMu7W0MkrWzucevB0NEpzwRSdwSgfJ5g-pGDESMUaxLNhwyqURW1ktObtljkNr3kR03zzWOEzafS0Cq6wX9sInYBqf-br_xmIzK1KeNwiIGHUlCcRqVVIseM3Yu4za6b-Zgn007fOQnQ9OMT9C6TTvgKlVvu56Rxv-vYbOXD81MJoc1VAlEne_9g32_UgX-nX_TJ5pvyNFito7vv_GeTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش کومان ستاره النصر در دوران باشگاهی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/90200" target="_blank">📅 00:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=FyFuacQJ5ESORwV875O6tHJdZHRlBVSQQCUdRh56WCFYPfg4G3HVt2N0Wv0gz1SotCE5jlFLlVMLBoS-8z519O9LQTuK2wp3YNaofe9vLLmWr8hX0tu8JNsbdLd9KMLIOqudR1UL3Z8Dd4-tAC8OQjFkmVIvB1wof0XKg9c-d8yy-qrfyjGTJA19fRz6VlxIsnazOgpfDYQEDDAddAbN9ltBM6pmuYEpAVoQWWFKvdOU6Lvga7DUxjUVf8-MvW6_BBp3Go1VSnr5Q_T5UgiMlS5-ridS9uPOvxaYdSUT61wl8goYqXXYH98HqaH4kRVhRpYTYAIgjB1S-FJCvJL0Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=FyFuacQJ5ESORwV875O6tHJdZHRlBVSQQCUdRh56WCFYPfg4G3HVt2N0Wv0gz1SotCE5jlFLlVMLBoS-8z519O9LQTuK2wp3YNaofe9vLLmWr8hX0tu8JNsbdLd9KMLIOqudR1UL3Z8Dd4-tAC8OQjFkmVIvB1wof0XKg9c-d8yy-qrfyjGTJA19fRz6VlxIsnazOgpfDYQEDDAddAbN9ltBM6pmuYEpAVoQWWFKvdOU6Lvga7DUxjUVf8-MvW6_BBp3Go1VSnr5Q_T5UgiMlS5-ridS9uPOvxaYdSUT61wl8goYqXXYH98HqaH4kRVhRpYTYAIgjB1S-FJCvJL0Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
بازیکن تیم‌ملی والیبال ترکیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/90199" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90198">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbyMBvnGKpzg9A-PBQtC4hIIhVbZdBYHoWfBZ8C3He48mUvHRWsRISwZCpW9HMeebT7o9imrsEo6yhr8MJX6ykl9ykV5npWrXS6nlEFl1JPQ7aINWU7sgYvUMvPdto1tl0H4JSJVqJARbK5Ih8oKUKd_n_ahh1I9e_bz4-SsMFPbndoe_oDt_-M8MAIXk7Po9OpavFvBpvbpf6cryPp4uAGn97HjVBx7ITinMWYM7rwEYuZYM9jEyFBIZBvgEyXsMgZRdrdV3mHsYk_9Lj0wg-crmhl1vEmS9WCbUgAgWFZwrDxfuMArrXetJu9hIjXxunU7_vuWY7xRcBZWA_n2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه رولان گاروس
✔️
⏩
با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۵ میلیون ریال بر روی رقابت‌های تنیس آزاد فرانسه (رولان گاروس)،‌ بدون توجه به برد یا باخت، مبلغ ۵٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/RG31
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90198" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028fa17067.mp4?token=UggP1asIgweloB95RX99eh2kNIas4uBvuid55vMe_lY6y0zcqQNFgISqige6DS97FbcS34xaueWUqZKUxaQAJUXqzjgIxAb7O0nvBp6pQblcZFZ1eXuNnHHOtqMNRnmZQ92oblFX4_BjbuZ84jqSdah5gp8QjF5z1ED3uE8pO3Jo9WNWE_gKyXoR1w2K0FbPjm1F_a8FKNzwJQQsZYeApTQmMp4uK7NV1VpTEly_3NSulCL9_8d6w1Grr91utsG5AvBw-dAGMN9KAmrpSC-mwWegsGHhbtI1ep97c5T7Tvd4PSrdNIzucGtShtC4FTfNXya7Jo2J4ASiknLEANgF-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028fa17067.mp4?token=UggP1asIgweloB95RX99eh2kNIas4uBvuid55vMe_lY6y0zcqQNFgISqige6DS97FbcS34xaueWUqZKUxaQAJUXqzjgIxAb7O0nvBp6pQblcZFZ1eXuNnHHOtqMNRnmZQ92oblFX4_BjbuZ84jqSdah5gp8QjF5z1ED3uE8pO3Jo9WNWE_gKyXoR1w2K0FbPjm1F_a8FKNzwJQQsZYeApTQmMp4uK7NV1VpTEly_3NSulCL9_8d6w1Grr91utsG5AvBw-dAGMN9KAmrpSC-mwWegsGHhbtI1ep97c5T7Tvd4PSrdNIzucGtShtC4FTfNXya7Jo2J4ASiknLEANgF-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیشب آخرین بازیِ دنی کارواخال با پیراهن رئال مادرید بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/90197" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90196">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90196" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/90196" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90195">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koT5RReVaJhMJ_pvlsVGfHjrZeigDEJ4aIuWuD1rqrmZ5e7-IlDsasFgBXHjYzzo9D6ebT-vR9w4PKrSEZHo738hiVyQfxksIS1433ELJCzCazstR892NZ1tA0qDZmOCp9hxsBlz7LFbmpQltIVzIB-TC3DhOXzcS_AcERF2N-dixqHj11Oa7pZOFNve2IGP3HWBxIIrekyEVsmWOjd4bzJyL7q3FDr5ZkRQz1SCjxX5tH26uBtC3SjVV2K6Kg_TJcYhPhusFkX_Z8P4Sf2NgVDjsWOt9utP6uqAApXE1Nd9-FhPMF8cjQFUrm8I_LrRPdSRb_8lJnfuVKpd7bI9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/90195" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=HoqBc4kLkBSQqaRgvsRchvcQptYwtE3N1A1gZN3raSshsDcVXIH3DUz51312cunLvu_t-7u4pagUJ-rczUmh8YSX-1oKrln2sUSxYNrpoFbuMfLq-wwf1-7SqvuRma4sEMrSgi7D7ITRGpLv1BQO3T0TJcRyX1qF377RTJtJBwHGRsdThGDKJsg8Qkuw5MHXuk48m5u4vQwWMkg4Tma6WkwiXmLyHHo1OAbtR6mBjGR_a1oFzHiRqBEbwpZAsWk_r7xyCXP22RDpCJ2MLEiLPayCBwqt3OTlUpXzwXLtMsf2dvgwuqT6jVyFjVp9UbuGbJ7WePHZOjJvpJD2gIGQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=HoqBc4kLkBSQqaRgvsRchvcQptYwtE3N1A1gZN3raSshsDcVXIH3DUz51312cunLvu_t-7u4pagUJ-rczUmh8YSX-1oKrln2sUSxYNrpoFbuMfLq-wwf1-7SqvuRma4sEMrSgi7D7ITRGpLv1BQO3T0TJcRyX1qF377RTJtJBwHGRsdThGDKJsg8Qkuw5MHXuk48m5u4vQwWMkg4Tma6WkwiXmLyHHo1OAbtR6mBjGR_a1oFzHiRqBEbwpZAsWk_r7xyCXP22RDpCJ2MLEiLPayCBwqt3OTlUpXzwXLtMsf2dvgwuqT6jVyFjVp9UbuGbJ7WePHZOjJvpJD2gIGQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهناز شفیعی :«می‌گفتم ناصرخان یک کم کلاس بگذار و با زنگ اول تلفن را جواب نده اما ناصر قبول نمی‌کرد!»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/90194" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
آکسیوس: تفاهم‌نامه ایالات متحده و ایران:
🔴
- تمدید آتش‌بس به مدت ۶۰ روز.
🔴
- هیچ عوارضی از سوی ایران بر تنگه هرمز دریافت نخواهد شد.
🔴
- ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد. ایالات متحده محاصره خود را تنها پس از برآورده شدن این خواسته‌ها توسط ایران به پایان خواهد رساند.
🔴
- ایالات متحده برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد.
🔴
- تعهد ایران به اینکه هرگز به دنبال سلاح هسته‌ای نخواهد بود.
🔴
- ایران متعهد می‌شود که در مورد تعلیق کامل برنامه غنی‌سازی اورانیوم و حذف ذخایر اورانیوم غنی‌شده خود مذاکره کند.
🔴
- ایالات متحده متعهد می‌شود که در مورد تدریجی برداشتن تحریم‌ها از ایران و بحث درباره دارایی‌های مسدود شده ایران مذاکره کند.
🔴
- ایالات متحده هیچ نیرویی را از اطراف ایران پس نخواهد کشید. خروج نیروها تنها پس از رسیدن به یک توافق نهایی در پایان ۶۰ روز رخ خواهد داد.
🔴
- جنگ بین حزب‌الله و اسرائیل به پایان می‌رسد – به اسرائیل اجازه داده می‌شود اقدامات پیش‌دستانه‌ای برای جلوگیری از بازسازی سلاح‌های حزب‌الله انجام دهد؛ این شامل حملات هوایی و پهپادی به لبنان خواهد بود. «اگر حزب‌الله رفتار مناسبی داشته باشد، اسرائیل نیز همین‌طور خواهد کرد.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/90193" target="_blank">📅 17:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqcDN4dl8Jy5JgGMB4VJE4vdUhXzzgNO9mnd1NKUwWeHFj83emNd7ijSHiUxi_b4fSBws1DtmWIPO4of4yV6ElgSAd4_4CmjJGOBIj1sHvKYYoH0DELDX5R5W1nTGhZE20-Q53GE5R_D9fjRNWfornWOvqULD508W-rQSgkm10nquPYyKQPQ6o6CZ-0zjQzEVbFhvhSqx17xWEj0qEeyztaDiN0FZrZgPCzKB-wE5Xim0f_nRfGmRRVKtpQpIaSf15lVCyaUQnNKfOGWrXNcyN6_Knfhf_A662r8baSb-pHAVP7NyOzWSRMAOAgE3XRVEaqk1C7Za40rVgiBuEyw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب مشترک داکنز نازون مهاجم استقلال و روماریو اسطوره فوتبال برزیل در پاریس؛ هائیتی و برزیل در یک گروه جام جهانی 2026 حضور دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/90192" target="_blank">📅 17:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihJY9QJ3v2XgziaMOIYlrqkrAmkCVPKyXyqTXQ4a5xuPB2SJTYH-4HCw2mbQHR8E4bbuxYQmm0116veLwrPHWFnQg_2u8uF7xOICyseysJifcUTCc1pEg5e6xvF9w0BpIzrTyXj6kzP9YhkzRJZgeTREmldzqNu8QTURNl3_-2rpwNxwcnicry9mcdsFIqkZ7Zvsb7N4nWV2ZiAVxeY2QdVt_rOa4NWzk8FVXhTHJAKwxDso3rrT-QOR4ohyhyBYN0bt5N5k7Kbly84yELDC-b-X3X9zhmZTBwKMijXnL_7w4nIyLfslNxo86omgVjUCWaKJM8qeYOzq3O1BuSuc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: خدانگهدار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90191" target="_blank">📅 16:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67618efab5.mp4?token=f5Tqk_Kt9WYKvx-BtnPLsarDjvFkM2rATWUdiXs_lTSI7e-UOGJk-VabsnnQdWzT-3NHb7X0HI74znO8OUzwXXma-_bCWT2r2PQJxFyjtH107ljL4RF7LTS4jbb4i82015dhUYnwfB9NlMxs3rkwgIdCwxxvK4FsyfHZoT-IyuzunLBU68sOSuZcEWkUOxht15pYo2qthn86Gu39ZYPhb15PHZI7Rxh7gt78dY1eEtcXO9pdN3LaW-UMVH81uvYqv8fii2VNfrXUiXyAakE_xS8fw_9Kb2myIc3k9hdTfpGSskumZWk0sAGTudvIxay5bdnFhthKgNK_iSVVs3hb-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67618efab5.mp4?token=f5Tqk_Kt9WYKvx-BtnPLsarDjvFkM2rATWUdiXs_lTSI7e-UOGJk-VabsnnQdWzT-3NHb7X0HI74znO8OUzwXXma-_bCWT2r2PQJxFyjtH107ljL4RF7LTS4jbb4i82015dhUYnwfB9NlMxs3rkwgIdCwxxvK4FsyfHZoT-IyuzunLBU68sOSuZcEWkUOxht15pYo2qthn86Gu39ZYPhb15PHZI7Rxh7gt78dY1eEtcXO9pdN3LaW-UMVH81uvYqv8fii2VNfrXUiXyAakE_xS8fw_9Kb2myIc3k9hdTfpGSskumZWk0sAGTudvIxay5bdnFhthKgNK_iSVVs3hb-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر حجازی: دامادم گل زد، تیم ناصر سقوط کرد، دخترم گفت طلاق می گیرم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/90190" target="_blank">📅 13:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90189">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/90189" target="_blank">📅 13:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90188">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tP2vCsqqGEcXYxgqogrDlsf3nXdtSiDsaNfNO_UgBCHvrTH3t-zqCVzHi3YyoE9jSJPlJn4-Ipr-DF_a6nxpJOo7S59Sy6-DHOnyhaA2AzDN5aOugPfeNY5e-QYvH2zRpJmH0RWsTY3Xe3WaaVAFKJM2Tx09jeCLJduv429RJGWaNmMk9Oxlz-lt8Y03yk5ssw3eFdO6C2uacyyP84R8k7WXRm2JEIZsLNONw8Hjv5YY8e5erY1BfdH57lMshEu3qH8L7YtCfuUD7IQG51G3wwx0vNEVFsIztMlgzJET04y6uUKzwBZtxdYTKOG-aep9-B2jDaSwSPSv8dKdG9bxaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
قرارداد «PSG: Champions Contract» خودت رو امضا کن و با قهرمانان واقعی یعنی پاری سن ژرمن و 1xBet درآمد کسب کن!
💰
پیش بینی روی PSG — جوایز تو در انتظارت
⚽️
🏅
شما در
Level 1
می‌تونین AirPods Pro، کیت خانگی PSG و جوایز دیگه رو ببرین، و در
Level 3
نینتندو سوییچ 2 یا حتی iPhone 17 Pro Max در انتظارتون هست!
😎
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90188" target="_blank">📅 13:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQBQVTjqYI01eSU9AXrRs8VdYacIgDA0t2_hdqExNpgVyy3nRn98rxLUZmmY9kzrxdD3pmeJypn5GJoqe5v4ehbrp-0ZwYl3SKihOU99gfefWsTgq2v5JUKkfy6PbfY-mN4jnNcWGPyll1qk57rHpP7Yt9bS6nJ4PV7snNSZIb5Ei2SX1H9Z41QYZqnEGlKCCYG7F9R59ub0CI3zYxwpEsyGjiDezKghVHbbLKoOnwd1hyOp9nnWVH_M1PwCmJwd4RscvLLTPBZ4q44iZd4oyjGu9e0CcWcO5KJ-U8Z1gUWylVXTRG__eYFIE9wlo0qL7i05sQ0RZWIG8w-saQ6T_hRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=gsW4AuhjN2pGabPVrE8CeG_ZntAjPXFtsndQnI_Xcc_wAl561PemUkuHJcOkV-1eBMDYTSVm8F3p-C-GbNGu4bdKGqflwCwTdPy2sOG5ZnAElf5K9dvsiMkQ1jZqjPPTS1XMOvBTDd_ZRrmVxhDTsbG2OMXs2yGExggsGXZ99WdHKXhGy3mWaAaKoN7K1lN9H6LsJ30F3R8X8Q1iugN0Q6zQC3blIQc-L66X6L0gDyawE135hYW5JUH0dB9M8Xf6Y8aC6iaEVFG_rvzwKxhSu3rdqV1ZutSGIFRFZ33QQnJ6fR8coUPw2pNr61t7CZOMF-oRCnJeRc6MKWA2jjIlQBQVTjqYI01eSU9AXrRs8VdYacIgDA0t2_hdqExNpgVyy3nRn98rxLUZmmY9kzrxdD3pmeJypn5GJoqe5v4ehbrp-0ZwYl3SKihOU99gfefWsTgq2v5JUKkfy6PbfY-mN4jnNcWGPyll1qk57rHpP7Yt9bS6nJ4PV7snNSZIb5Ei2SX1H9Z41QYZqnEGlKCCYG7F9R59ub0CI3zYxwpEsyGjiDezKghVHbbLKoOnwd1hyOp9nnWVH_M1PwCmJwd4RscvLLTPBZ4q44iZd4oyjGu9e0CcWcO5KJ-U8Z1gUWylVXTRG__eYFIE9wlo0qL7i05sQ0RZWIG8w-saQ6T_hRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت همسر ناصر حجازی از روزی که شُهره به همسرش پیشنهاد شام مشترک داد
همسر حجازی: هم خودم را باور داشتم، هم به ناصر مطمئن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90187" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
روزبه‌چشمی بدلیل مصدومیت از اردوی تیم‌ملی جدا شد و به دبی رفت تا مراحل درمانی خود را طی کند. احتمال خط خوردن این بازیکن از لیست تیم‌ملی برای جام‌جهانی وجود دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90186" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4hBHMbVrOPcSwipmHYoXwW0t9DVgczuP5tdaXu_gjTmZ0oX5pYY0WcN8kCqlyvhRehbAx9ODe7KKqX0aZdaktMVRL0tQh1Osvgy92Z4tBIG4h5IrG1DwPsc5zc3ZsvESahD3t62D--PmC-oDpe_bgCqhj6QeCvdJ27ptY00Zsr24l0oB8pYs0uAasOsw5D8wMPnU8Rec-qLPqGLNCybESdx88TjEZKLmFRhLZj-3mN_z6UWkvrxSbojDvWr-goF88Rj-9wnymhZT-Y8ja59hO1x25Gty2T6bVhCG0_8osrCmzq1kEZZRYTa71Bo36-iyyGz3nJ23y2BtvJ0ufq7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس ایران پس از شایعات توافق:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90185" target="_blank">📅 09:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=LPaWqxjjvosuIAcVWxWZEfeUQOSiEaQmRd42xofOZX3KoIFktsgRuA155RUgq2UbCPoWVM8WcL-Etihf0pFomnIES5u7geBQTyxvnTOrC9aSw0imcG7xStpMmTr_S8iNNiLw86IfvpbaaZY1KCNEdg9wNrgr4qMk4I1IwAbhbCil9j7d0DNQoqwRLyAoFuTPE2nzO5OWL8VlSjp3Kco5jmxCYsT5ju_HNX1vk_PonVAUYkTlP0xpEgVy8Mjvo-EMZiFXcUn6bHBoz_yl2KaR-fPhSBUz_civpPd_6Ne-lSa8Yq9C-uWHsDJUtle24fdohYD-0-H7kLptGitDSfJAHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=LPaWqxjjvosuIAcVWxWZEfeUQOSiEaQmRd42xofOZX3KoIFktsgRuA155RUgq2UbCPoWVM8WcL-Etihf0pFomnIES5u7geBQTyxvnTOrC9aSw0imcG7xStpMmTr_S8iNNiLw86IfvpbaaZY1KCNEdg9wNrgr4qMk4I1IwAbhbCil9j7d0DNQoqwRLyAoFuTPE2nzO5OWL8VlSjp3Kco5jmxCYsT5ju_HNX1vk_PonVAUYkTlP0xpEgVy8Mjvo-EMZiFXcUn6bHBoz_yl2KaR-fPhSBUz_civpPd_6Ne-lSa8Yq9C-uWHsDJUtle24fdohYD-0-H7kLptGitDSfJAHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی باشکوه کارواخال از رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/Futball180TV/90184" target="_blank">📅 09:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90183">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90183" target="_blank">📅 00:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90182">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjwpgvrczTw2QQVbWHsCO7hMjWHf00iu64tbE16H9Lkc84bAtF6BVmRJDEBHtCqHyMC-__523Qk8Pfn944mCXXBO0kZKUijT3FFSHNNAFZvUT8iUcnnQirKqHPZ7iW0z1pwMi0Q2_nTMXOdREZN65_Gp39yEPOPmNtgivLV3IFJp81oLPaW98YEoGH7wEkdj7-nVzC408TB-tdNAwNlpIAJcrIm2KtfpET0BFwa3yYS8pxQUN-kKQW-UXOhC59bJmd6OC-X8HPFvD6qkUHpZxGh2l-Gs94Fh7SqoSPbShUu_r7jWOCAlFAsEyDsMo4kUtk8hzk0qTgzhj03WyZEFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90182" target="_blank">📅 00:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGmaSPWAYU9TDbSYUkI0OYgrUjtlxjyarptJOg5yiAeOMusZN_BTrqzz7NhuQaqs4bQ_QX2qhUDNdRop6BgPGtVOWv4D0gBDKWh7k90fXgaIFXeMXIZcNNzT678vE8fOQthyvyqxWv4HIZu3AGI6Min4rYs_Jxpq9EsQ5zQxItRJEfDhmdup46a49wJF5tyzMSOF1b4_yDjAfhkz1vdFBLD9CIuKnqvEncSMjlIy8Klir6kZnUZB-fl2nkPBg5LwxdNfKr2VRJDiAYgaqoUXijXtBk02JlcHGmGCLZpCbMFYKTdAERvUcPJtsyS9iGILifzLDxhs5U0F5a2T8m-nDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
ترامپ: یادداشت تفاهم با ایران تا حد زیادی مورد مذاکره قرار گرفته و در حال نهایی شدن است و به زودی اعلام خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90181" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXcqMQYEkROWKyoDvvya_VXXW3dna5vH9j9VziAdC_Ynqn8hqXtvz-GpmCd_ZmCb6AncmfxaJErTPkmJqjXb1VyVNNkx43QRO7zqDaus15nbV7gqxLaxDGhO3EUb-p3q37TLUTSzYHOFSGInay47gX_4D1YhNHrE5YOaTcblgSGL3adcuKwjyCvhyldf7B5zov8h9Fnit3KkPsaecWpEvwBSCLo7L-8h2w_MzR7HVjxXl1zISIxqkN3P9IRMB_Q1Xu0_he0qlRZg5UGYRVJ2APkhe1IyGYXe_wxS1lQxgDpEkzIJfGkmzAg29qwMx7a2SWW3BNYogQ8tL4N0P7SZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تیم‌فوتبال زنان بارسلونا با برتری قاطع مقابل لیون قهرمان لیگ‌قهرمانان اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90180" target="_blank">📅 23:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDJ016vAOoDsEdmcwrvdoJviRkFyIoEz1B1yxqRK_HMS5BxZjT2RWKnewrrZvFTgZyZybnKYaImSWahqL0MrCUVhUdMNj8Vt1vJeSVe19JPmZW2TBenP6sZPpJjJOGTg6-HHRJ50yXg0FJe9R55-g12gBORM5qZdcwIGoylI_zca9uc8rgDpzP0mkObpiKZIvo-G0oQafb8IY2pX96nDL6WkaStC4Avd8PMgxky4NmjDr4zrLmMjjZvC5bmg3ywBMRg0f2QdjKpy0-mj9783sSe-GSir7KlHdDn_P550Xmtt58RGCRnOhfrSjTbbhvq3EVKOwOdnCbBrwwLlouNM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون درگذشت پرویز قلیچ‌خانی را تسلیت گفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90179" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90178">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XftRP8DmtphCiUzJeEADo-NiaOo2RTVCFQrY1xvRe2mzIolrEpezafq4ZAvDRgT263SwDc6ho7RBT1U-iVclNS0BwXWZhclxXDQSZMA_FrLR06yfJozdJpODrkozKaBoxidoXOihOXB3U9xrOcW3ofUIUjicyWjYHHD2mvWuKqJQtOQt4Cywd-2pM2nQVYflDIBQjQrjQfMrcFLGDCDwjhpsqZWFKBa3eKP5M5qWtwOx3d4fOShQ3eAYOzCkxmXypAvF4hZxZwSz8UKMZKD8GiapqkLiDo_cazMdR-BzCPoBhQ3qM_pbF0KC6JUopo_f_XJ_jBaSBOSoRjOz-31R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تورینو - یوونتوس
🏆
سری آ ایتالیا
⏰
یک‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه المپیک تورین
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
تورینو در ۱۰ دیدار اخیر خود در سری آ، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
✅
یوونتوس در ۱۰ دیدار اخیر خود در سری آ، شش برد و سه تساوی کسب کرده و فقط در یک بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر تورینو در سری آ ۲.۹ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر یوونتوس در سری آ ۱.۷ گل در هر بازی بوده است.
🧠
خروج را از قبل تعریف کنید، نه وسط هیجان.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/90178" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=RElFilN8JOYpM7IEqHGqSWW6yibb55MokJNJ-k6h2DU5taDON1YIsCVdv8ahnZVRoIeGtW62rAIWElhDg-BGMECeT1h_d0VGj0rPGRNMChYCbgwz6LZmWpfWXMITjojdolEw41fr_-YCGPqJwvXsH4pQIKVoOD7t5KukcseG1-CJ1JqTkag5Ynk_jOwU2Q2CChp8cFFTla3TEYpRuSZdLOhMZ9mMdGJLw5ee0Ts2vjAAu86MB0t1QBMNYi3a1XZ-UHFfymqEpSAQ8gdhS7O1tk1xer7tYNpI3WzVGWHJemhIPuodV5ZszcS7m6vD3SVBqQ5IUyYwLpL9kpwlM_dgRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=RElFilN8JOYpM7IEqHGqSWW6yibb55MokJNJ-k6h2DU5taDON1YIsCVdv8ahnZVRoIeGtW62rAIWElhDg-BGMECeT1h_d0VGj0rPGRNMChYCbgwz6LZmWpfWXMITjojdolEw41fr_-YCGPqJwvXsH4pQIKVoOD7t5KukcseG1-CJ1JqTkag5Ynk_jOwU2Q2CChp8cFFTla3TEYpRuSZdLOhMZ9mMdGJLw5ee0Ts2vjAAu86MB0t1QBMNYi3a1XZ-UHFfymqEpSAQ8gdhS7O1tk1xer7tYNpI3WzVGWHJemhIPuodV5ZszcS7m6vD3SVBqQ5IUyYwLpL9kpwlM_dgRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
افشاگری همسر ناصر حجازی؛ علی دایی تمام هزینه‌های درمان را پرداخت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/90177" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGsPTLsG2_gKkbJWYkkIT5_SGy2VQrHvBsB89Nh24yVf0pdtf5FDn4K6ws_JyTJOycnLuxWnsvm_H2B521RxM46Dg_P7X9tY7Gkgrt3BBbD7a3d35bgadeHdQ5VgrFxLXRPpXAN3h9jX0eK2TkwV-IFgqfsqacAHcn5CLsbR-eE1Lf8WaLPiKH03EzM4nG2BwxjlXIX1YEX1Ivwj_Cx_6xb_cZSTnwlyWOZmFdfhq_rcLp34P0moMBJamSz8gE_mF9dL8W4bj-Ash62Z3EZ5GvuuE6mzVOEpYlj0PN6hTNsZTcjGIz_eDJgcleKUr0p57-Ap2Fyg7xtPNQxgUTE5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مائوریتسیو ساری با جدایی از تیم فوتبال لاتزیو سرمربی آتالانتا در فصل‌آینده شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/90176" target="_blank">📅 20:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=VOhJvtT-gCjOWS0mPXYTk-ZnBb9h5lP16N0yHJQGOCPzFz_FyBTP0JzjveQVobtfebQBxFNd2NcDsR2on2KMIpV7HagXrDpeiXWAyDolhrarSTh54gfOCHCPgiIG5N-xB20V1X6MaiO7ZYla_7asjVsKpnaa2IUl0_RWQIhPHc44iiEfDLEJrM7GQFvSwl8S0kq5ZPa76ozWFqti6LkffIPRWvB2Vkp3IMOEsNIV7bnm2kHOvlSyjsyny7pNEEqOcNfKWHqT4LCKjjzAmbdifGxpJAF8ss6_mdWu16D335h_u7W6onnJJsn7G3CIT7VEEPMk3HzGQpXWM79h6V5TCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=VOhJvtT-gCjOWS0mPXYTk-ZnBb9h5lP16N0yHJQGOCPzFz_FyBTP0JzjveQVobtfebQBxFNd2NcDsR2on2KMIpV7HagXrDpeiXWAyDolhrarSTh54gfOCHCPgiIG5N-xB20V1X6MaiO7ZYla_7asjVsKpnaa2IUl0_RWQIhPHc44iiEfDLEJrM7GQFvSwl8S0kq5ZPa76ozWFqti6LkffIPRWvB2Vkp3IMOEsNIV7bnm2kHOvlSyjsyny7pNEEqOcNfKWHqT4LCKjjzAmbdifGxpJAF8ss6_mdWu16D335h_u7W6onnJJsn7G3CIT7VEEPMk3HzGQpXWM79h6V5TCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهناز شفیعی، همسر اسطوره فوتبال ایران ناصر حجازی، گفت حقوق بازنشستگی او ۲ میلیون تومان است.
او در ادامه با انتقاد از وضعیت مالی در فوتبال ایران گفت چرا باید کارلوس کی‌روش با پول این مردم به سطحی از درآمد برسد که بتواند برای خود در پرتغال جزیره‌ای بخرد، در حالی که ناصر حجازی در آن زمان حقوقی بسیار پایین دریافت می‌کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/90175" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90174">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90174" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/90174" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90173">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvhE_9_gOf_tpLoRYToVrU68H_6G1-RvvQHHZJZreM6zVBVsthXueCdjSM4xwi56N-JgHID7YTksp13W0gWhC5G8VRtFIGGJA4VLYEmU9CGDHvUjvq-6aYJ8NedoVjnzC85fLpH2auRetTJ38NDDGBImjWmQwrHTQgQ6SxMP4bmJRQkt8OG2wQ0cb6f_n5CeoTw1u59J_rmSnIbv_x_N7DOLqtko73ab7kZ7ILlp0Fsn_cGkk1sEpqHiMn01evWAtdJWan0Dyfqo0B4LEQCX0w_aPCw1IyiYvnzBy0c2zaM7avmPaDzw_GGWNivtzqsxn0bTQ9wL0kQ0tOtgKBL0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90173" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=JE3qKxZ2aUYGWoV5eYhJ0zaUfvbhxqQJVxRJVc-6Jqr1Z66hzN1c1Pg3TB0Y1tv0ZyRJ2Wx-cd1a_2H3ranT_kJBQNdowgc5zSoua2YwVtoSjQbZxt7QZ9LFq2owvLVMei1c1kYDnmghqNJPEdPsbuZuNMhbDlfmRGI11Y7GJ8lcyE0FTscmVKwm7D5Yxki1H7PSW_nZ7cSY9eLyPDXQY0vEU5NXnrQnk0n3E60WdiDWB8ytuJcARDTXaX8JWtuQL8YHTb_PkbBblmO5WA1F66cQVvLKgOhQPzZQslgaHJb1IWx5kWd1q0DOePFLx6xs2dFJAC_b6PdQ8LOJe_Cgng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=JE3qKxZ2aUYGWoV5eYhJ0zaUfvbhxqQJVxRJVc-6Jqr1Z66hzN1c1Pg3TB0Y1tv0ZyRJ2Wx-cd1a_2H3ranT_kJBQNdowgc5zSoua2YwVtoSjQbZxt7QZ9LFq2owvLVMei1c1kYDnmghqNJPEdPsbuZuNMhbDlfmRGI11Y7GJ8lcyE0FTscmVKwm7D5Yxki1H7PSW_nZ7cSY9eLyPDXQY0vEU5NXnrQnk0n3E60WdiDWB8ytuJcARDTXaX8JWtuQL8YHTb_PkbBblmO5WA1F66cQVvLKgOhQPzZQslgaHJb1IWx5kWd1q0DOePFLx6xs2dFJAC_b6PdQ8LOJe_Cgng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دوم خرداد، سالگرد زنده‌یاد ناصر حجازی، اسطوره باشگاه استقلال و فوتبال ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/90172" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxR4DxZCzjs00SiSKhrNxP_-qdT5tWu2huZ4AqF7vuS_1r2Ff6VJ0MBAx5O7x0u5tZQcbCiMXVkieOwMrZgnMzq5RhrJVWIfxmLWHV0t4kic7qqQDCOJSR1qGhsCifbePiUfACsnEuSGJKb7fF8CVPBOhaaizcs_SGXpSL_w3EHQBs0CpMRHjqSgvE2cY00FcMxdSF29QHB9m6fOGl2gxhimeW1xxk4WLhpA6UqgcnTLQj1vR0L6FuXxS8KvIOR3IL7fy1aS6SzLQJsk6i-BWNxJ_3Pjxn34kAnUfSPDB7OfBlVc8B0CAN4lMfWKH7qgJ0jv27pzufx9QheD4ZuBpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
تلخ و ناگوار؛ درگذشت چهره افسانه‌ای فوتبال ایران
پرویز قلیچ‌خانی، چهره تاریخی فوتبال ایران و یکی از بزرگ‌ترین تاریخ این رشته ورزشی ساعاتی قبل در حومه پاریس جان به جان آفرین تسلیم کرد. قلیچ‌خانی متولد ۱۳۲۴ و در 81 سالگی پس از ماه‌ها تحمل بیماری از دنیا رفت. او تنها بازیکن تاریخ فوتبال ایران است که سه بار به صورت متوالی قهرمان جام ملت‌های آسیا شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90171" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLU-W_HLNHKHABoutm2HUCkw7hT3kXUbPahSXWDBLGXyaZk6vzRKQeUdZ8XcuuFY6Yja3SSq7CznALs-IVRP9mMfM8FxujsL245yMMkZX6IgDbK1ACMun2-hnL8gS8ppTGAfGLvKXwTJN6gLK1f_gpr0NYTkWfenIPBoYVF1XacaDFvZ8i5pNCaL-UdZD1ijW_McO45F9iBOhg6tCJGTqIFfpRsMNhAWBJgPHoWb4yPtGVEh4NS_bAQUAQjhqev6E_t47BQekL6up9LAFuEeJTKm4z_d3CK4BWXhG-wJSibuwqFKovTDzMIvvkBacAaFUdQXx-EAZ_x8hVOF2wa-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
عکس جدیدی که ترامپ منتشر کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90170" target="_blank">📅 17:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=fpqXxubn4UVC70vHy7BupMa1_3Bt-AG_Ad9Fp4-LeOtAMPVCwCixn46K1BFR3YVlXgkybhat4dnechEayJnoRpgSmNmVwtYT7c6eROjfND4dqjf5aAI7WCr1PUXTwPBUe5Ij7Nha5n3gYnAJqAFEgmya13IS3rxMm6MO5joweWOQihrL9VlfHIq3Z-bKl0nrqtx5yXi42w2NzQyP0ACWLZI1rmwXGgNfHLdWJbEUJMzuDQwhweKnsjIL6Ih9oKzm8A5Ce6ZiF-71k6TSOinp05vwExn7b7c9yDX23kcfwdQ3oT96QAH-CrL2duMob0TuQu6emS7SVXVfTU4CVpNDew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=fpqXxubn4UVC70vHy7BupMa1_3Bt-AG_Ad9Fp4-LeOtAMPVCwCixn46K1BFR3YVlXgkybhat4dnechEayJnoRpgSmNmVwtYT7c6eROjfND4dqjf5aAI7WCr1PUXTwPBUe5Ij7Nha5n3gYnAJqAFEgmya13IS3rxMm6MO5joweWOQihrL9VlfHIq3Z-bKl0nrqtx5yXi42w2NzQyP0ACWLZI1rmwXGgNfHLdWJbEUJMzuDQwhweKnsjIL6Ih9oKzm8A5Ce6ZiF-71k6TSOinp05vwExn7b7c9yDX23kcfwdQ3oT96QAH-CrL2duMob0TuQu6emS7SVXVfTU4CVpNDew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پادرمیانی همسر ناصر حجازی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/90169" target="_blank">📅 14:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDinbxyr4yraYmomu0eJKBpR7CsX8N8unQK1A6doKjsJ0egcKTXh_v7gRz-DaRt-mF_3EFJCh5818uuiar9EvhsrrMRdzsX9_N9P6wA6jy90fycjw_t1sf2mALbnjwbaH6M6cRwNn0-CNv_-UAK_pMPcKygS_C3E15i5gz4amlfefNlOfuvcHyQejpjs1pIzi512yhKoMbph0kOBN-6Zj3EmEc4AG2XzPZymgjPCW85JIStl6b4QRhRu_YY6iqocl98LXjvk3U8uMdr90BGrI8RlE4XL0E68UuVmNsw_ROCtHNW0qxJPE97lmFGgHL4kHy3i9WrWQEg0gcXINPwYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو فرناندز به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ پرمیرلیگ انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/90168" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0ve_x5whulE_UnEluNLSG8AT5qWAp0cODIq0xtpZW623OE0e8lPLSG0NnXGivXkATkczlimiNuQTD9uwWWEGYgHXocWeL_7yurZ-8Szgqf9x13fGdQeWODPKUlETDcMbo28vLf6hB00JEcAiQp8wXOUzs_Ip9T_Q2uTY6uMOga_uW-R265IA4qHLYyEMFym4iFH7kaxagm6gmR2HiuCIxNv4Volivc7SPr4QzGrcsKFx7Nh8tPfBQwXZYQ4N-FpS6YKbdt5jD8kHYm9HaP_aKWW44MZMWfam8WwUk620MY0TiycIT6MS9_0DPwrMIPMeQTBEoXXl00wHPdjEKL3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گستون ایدول (روزنامه‌نگار آرژانتینی):
🔻
فکر می‌کنم ۲۰٪ احتمال داره بره آرسنال، ۳۵٪ پاری‌سن‌ژرمن، و ۴۵٪ بارسلونا.
🔻
اگه بارسلونا واقعاً می‌خوادش، باید این رو با یه پیشنهاد قوی ثابت کنه. تنها تیمی که واقعاً قدم برداشته پاری‌سن‌ژرمنه. بهش قول یه حقوق خوب دادن و پول کافی برای مذاکره با اتلتیکو مادرید رو هم دارن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/90167" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90166">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90166" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90165">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVh9WbI3dg8dKGJW1IA2dUhb4oW4e1VIXyfingt3mKZr9aD8d8h5nDExa-KQr8j4FQfb7L-jiHtMxpK_JrNrD5wgGDKV1Ku4R-V1gDaupC0MsXejtiAicpS1Z7Q6KaMkDxH4556R-lz62e7IB5S8KhZYd15NOrBF7xoucivS5iyBi62_wFVDuxNx42rsxhwDgwjUzBRWQydTr4IQzLARCMjiVyOT7V_vfTU-h6FJmZZ-au8uRQERzjlGhZvIeQitHWW3CF3VtrMUHjxGsac9nWVu_CVY4ypmZzP8PZkToG1mbDGZ57KmuMYJgNSov8FPnCiSoPSHSlBGX5QsCJCvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/90165" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=W1jbb2ZRS4CQ4eWuhGb8JAgNu7VtWuq0VQLR3UKHl4EaD5IIHGHDfflvv0uajnmkIaUC3P67u0ETNdTvmFy1fvWcNV9LGdRy3eA02z5JPQVQfsPDH1XlHtABacvykHDyOf4drn_7ge6CKs4IbfEJhIcVUycFgoOJ2v3cUp6eYSj1BR2W4AlI9aFdRy-tA_TsMlDhInouj8Vx7ZpVoVxakYqEIbMP-LzYeyanlTw76QipDkPaP9SAfD2y-NMG0CHZTY2YpDnFVAKX8de5V0TdG7MYn1MPl4EQmdtK6bGVGdJw-CPrqMilaJZ04OeDwGTz0tKUrgYznd6aQl8aua3NnQueqqbem4vJSBBSmnufJFbZq6dX-n09JeIgkOkgGYJbmZn64V_wpLZDVd580p-WCUwsuXG8gzuvzmU4hA1IcsSHIbEmQcao2Igod5UpMRrAJhwKySSdwS3IqSSWhuxoWlnyc1t86xgmAG7y_0U4LPGioL6YtoCdUHv5kw2xdvDOmuN-_5G8CD9Q0_huldAc4ztocJ8FuyX1rWTIBVasrxFf2WOhYFLjZmHp5eoYkgZo1WlIerNWaSQtiE5z0A25v8MDVWi4hNhjHQz_0ZvR3L3ACP2HKd5gyd_RGFQ9Zg2p5frbQo9mGz8sAITwLeX97h_xTBHzx-oWJtUTZ7YMDm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=W1jbb2ZRS4CQ4eWuhGb8JAgNu7VtWuq0VQLR3UKHl4EaD5IIHGHDfflvv0uajnmkIaUC3P67u0ETNdTvmFy1fvWcNV9LGdRy3eA02z5JPQVQfsPDH1XlHtABacvykHDyOf4drn_7ge6CKs4IbfEJhIcVUycFgoOJ2v3cUp6eYSj1BR2W4AlI9aFdRy-tA_TsMlDhInouj8Vx7ZpVoVxakYqEIbMP-LzYeyanlTw76QipDkPaP9SAfD2y-NMG0CHZTY2YpDnFVAKX8de5V0TdG7MYn1MPl4EQmdtK6bGVGdJw-CPrqMilaJZ04OeDwGTz0tKUrgYznd6aQl8aua3NnQueqqbem4vJSBBSmnufJFbZq6dX-n09JeIgkOkgGYJbmZn64V_wpLZDVd580p-WCUwsuXG8gzuvzmU4hA1IcsSHIbEmQcao2Igod5UpMRrAJhwKySSdwS3IqSSWhuxoWlnyc1t86xgmAG7y_0U4LPGioL6YtoCdUHv5kw2xdvDOmuN-_5G8CD9Q0_huldAc4ztocJ8FuyX1rWTIBVasrxFf2WOhYFLjZmHp5eoYkgZo1WlIerNWaSQtiE5z0A25v8MDVWi4hNhjHQz_0ZvR3L3ACP2HKd5gyd_RGFQ9Zg2p5frbQo9mGz8sAITwLeX97h_xTBHzx-oWJtUTZ7YMDm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
یکی از جذابیت‌های فصل آینده لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/90164" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
⭕️
شنیده می‌شود کشور آمریکا ویزای مهدی طارمی، احسان حاج‌صفی و شجاع خلیل‌زاده را بدلیل گذراندن خدمت سربازی خود در سپاه صادر نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90163" target="_blank">📅 11:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWLYuYnxfivCrBXCnrGAbGcsMOONV8b1FvaSJwCBH-Ji-t8NtnPLiP7HXoGPxJOJDSnuxqE9yR1sUN5Lota8ztj4bBep1fKwAVcZXbeLA6wLwXBA2-7SB7zx0BBEsMJMPbfyxZl0ToyAcw6xPHJFAx1Fav5412vtvdMU5S2z-WZIVR-n2FeJSA2IW_RELNBJtxiW1LWV5BvGJ-bi8msEs7kKZHQFyPknGFAKqn5xNGJZFEV8UHEx4YyAPpkt9x8y2wCH1spfxvfeAlxoLy2n3whCgi-fHr4F73WcdFqX8i1VcW6YFzOg-NFVCK7xBM61YREFb0Ua4FpbyypRkLTUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توخل: این فقط یک مسئله ساختاری برای ایجاد تیمی متوازن است تا پنج بازیکن در پست شماره 10 نداشته باشیم. حتی اگر این تصمیم دردناک باشد، معتقدم که برای تیم ملی انگلیس تصمیم درستی بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/Futball180TV/90162" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90161">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90161" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90160">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q33krzt_byD9efk0y1LND4113feDEAi9HLUXSnhMf9ZWuPd8m7V0kM3dF6JKRgvH_fxFhQcA81ljNmnjQL2rTp42waJDqq1ikJOFiq_N8NXmz_Ela2HOEwtxAXRHdtll5-ff8zKJFvvGuPDt6D2dEmfWu9xol_X2KtQMdKAlFglL3a0kSCxORZfvfpbMyFYx76TFy6FgjeYgWXG9xTmFp7nLOG52icTRtlgbVceJRkpQbR36cY1uAsqZx1OTttUEmH9WYreR4jpQlVwCVotO8B8i00xuV-kEb_FjW0liYRHQYWi9Tw1m90goxgbuh_oD1nCKZYb3xDTavwttx7AQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/Futball180TV/90160" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=nadHo6BhChE5OtQSARXYDtZ1znNs86Q_K-KNzgPrgqNUWpofcsur1aaSUB-NWu6V02-eVDtII9itZxAK9hhBCnKeor2gj9nfPe8HYNYxkCZqdPyjerjNArUje4cRbaDMSBEiwIAHGoCzDczm78YokoG1jyZG6BREFZIpHP_Ks6zbOqO9RUVrQx5ZOGI3eDBPzLG3s0vMm1cMqCu67ilwZATzcCfYnLCu2gJPxvDab1hiJ59h1BtTP8e2OkAEKdoquEw7-27zHvSqsZJL7zJQo_13toJa9Vpk_cCNguBts3WkG6UBS5qSftcEi3gkQJ24Uster6MPeTn37wbfAQArVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=nadHo6BhChE5OtQSARXYDtZ1znNs86Q_K-KNzgPrgqNUWpofcsur1aaSUB-NWu6V02-eVDtII9itZxAK9hhBCnKeor2gj9nfPe8HYNYxkCZqdPyjerjNArUje4cRbaDMSBEiwIAHGoCzDczm78YokoG1jyZG6BREFZIpHP_Ks6zbOqO9RUVrQx5ZOGI3eDBPzLG3s0vMm1cMqCu67ilwZATzcCfYnLCu2gJPxvDab1hiJ59h1BtTP8e2OkAEKdoquEw7-27zHvSqsZJL7zJQo_13toJa9Vpk_cCNguBts3WkG6UBS5qSftcEi3gkQJ24Uster6MPeTn37wbfAQArVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ترامپ در سخرانی امشبش:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/90159" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA6U6_LPhRcU9_-8uAsmpUH1kdNokXtZ-ED_u6dnR3wpJdcWapQMbSy16lHTUI0ctHNarLpjo15ID4hmICYFtOUe03UpMH4Jl_xGKho8EUgSU0SPu-xmEhZSDZH-nXSmmmITx-lSz3V7ekQmx2xxUZwsNtUM_0fwdB8mSGynFdh-QCoeIkVBTBXOsxYoGg-tEE3QudtlT5hWQsLJ-ARWrhJ9JIoIwcYigoGSjPXOHcZ_Q6L1b5U0g-NFtv_aRTpU3X7du9UbGtdzsUR6szC5jGmabWL1eS-88B4cNNmlsOKbF6phGZCUTARWPKj3RJpiKcBX7_onynNeClUB-BkYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به شاهین نجفی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90158" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90157">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfqtC14prZKn6kWCdqmL1QznvhbSDPAGbIQYQIO8gI7lrakEcBnpp8O9khZUvhNkxWwtxzv15C3829EwoDCTyaRj37RfB2Kqn4Idqijpl9omz4jnHnwPhh-ZGp8PydEgF61kHf0ThEa-ylr1My2ojSg06BYJIgpv5DW3mRC1GzXqfFujx-Rb-hLz3H1MTlY90qkNwgrw6X8cPaeIjr_76-wapYEJ0L4y21Uvnn4BcjopfSRn5pO3XBwMFH-3Z3jtvPKNv4C6-e5GSq42HlJ9PwxVsKsd9S3fs_j6mao4lX9zrpad6Zi9HmMCZqNr1XiD6x4fo_bQxH9JVqQN5AiB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید - اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
⏰
شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه برنابئو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال در
۱۰
دیدار اخیر خود در لالیگا،
۶
برد و
۲
تساوی ثبت کرده و در
۲
مسابقه شکست خورده است.
✅
اتلتیک بیلبائو در
۱۰
دیدار اخیر خود در لالیگا،
۲
برد و
۱
تساوی ثبت کرده و در
۶
مسابقه شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر رئال مادرید در لالیگا
۲
.۷ گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/90157" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCjsstsjXq5vYMOxEwtUdajF3voJHgs2KEWAIyJzevvP5vp80koazaB7J-v2gIZdK7Fi_mSz3ZzRYvt9VTICsz3MNubRy-o_ePPn2ws2Vd0bBmrzb2bRyH--iinNtXB9o1wQm-9qJgSLG9lZXJDLNvyzsj28GQGcmxxChRJruj5jA8E4q99f39BvBHNGfmdnTOfwL_qgcZ-aM_lwZLV5g8katd_79tB-p8xwJnj5phmUBxh7-jVq9GGBUGpCpRun7VsptATTCaFL1A0ppGFFOFeQ1BQkSVbTawwRn-QFNgMMpXKJnFwOYYW_XokFH0bXdE3FjNGE3OXQs4pJm1GFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwsBRbLGu3p10nDokmvb70dpETk9kv7il1LNOvngg4jPwixFy4b4y0WUqwFCtzlx3Pw1BcLoS30gwYhUs7TRlvf5PU9gP7iaW5AxR0XZLeeUmjvONrtq9BZB2CV9iqBYvLNdNuhdZU-doqMo2G5gT1oprywV8aL7HCxAnK40c58GhCc4rtxx-og-FmhG6yWfsCZvuON0CGLQoGhPp3t1e0OYsreVSVc7mXSnEvhfz6Tk_oSeQoQnYLnTvtHRyaGEtFsu_YSa68OmHAj2IrnLC8HjIKBs6_TeQQuI0prY_j800C9NE_yLzkeGj5T_gpjwoKoxREjvHMzvoX6y9ziKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZviqFamzR078RovRb5MWHKI5H4gxNbkqilWvzKTreO0itTGPJVJaI_OFc1ryj_PwyHmht3HCu2060Hgk4fRiEgGBReG4ICoYGjkm-gjR1_fnRWMUXIf0hqreOELIGWnkSpT7d8w6oos3qaaSXHu_g_zz6HvfeaD2zzvQJBlq8QfN7ZqT815nWzsAI8PpuNfW4FIOR_tTg02u_Tbv5VsCHSwTNJh3KrMMIRQIfiG-APNONiZoK8PGksbXRaFF2GC8VZb03R40V80rWI0_4XkkNEZIAqU-0S_A5Paxtg_xUKPP2XeVCQqBZkHWnnjTjyqoxTSbQPVEjWCWsJ8Aefb9CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عناوین برتر سری آ تو فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90154" target="_blank">📅 20:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90153">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90153" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/90153" target="_blank">📅 20:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90152">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vns2yVFINv8URa5HDn9WYerGwDfoqJ6yxe-oXHIE3CVpmEKSc3ARs-xxfnGULfxpqZewOFbSf5OudouCjSsS4RI67tG-fcXmep4lfgYhKWJjpgTAUSviWBmpA1Zej3wNf_-DyS0rY0cgo0PRe0X1dmc_ONc61dF-9gk6-Gt-nIecZtcT6JttSxEZSImKpeXHkdXQ67gUNGNyT32WXiZNv6GjQ-oYPqEZ4WPh8Jwa9TIsZsIRUw5KKk42qQVUYFDCF_1iTjl__HV2TD6iZDUATPCzB_ZSeYEl66DTgdxiR9pzw-NZKlkXwHTmlGnsXw4tkzezEV-9yDOkULW1x1eImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90152" target="_blank">📅 20:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند/ سفر فرمانده ارتش (پاکستان) به تهران ممکن است آخرین تلاش برای جلوگیری از بازگشت منطقه به جنگ باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/90151" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9x3UmT9LLg_hpiZwuv-fgWVI7H6b8k9ORAXV7xOERPqpQNxinhvGRcKMVZkNWH95uL1rDzRdAWXPLBQGvSLPah8YFo4QCUC8hQ0Sqqtc1FQjygZEjDtkBvLg4qb6GPeZl29GDWuHm5FNqS_-8iL49MWSvAYtQ-XfLNgRbgeReOyV_BfAFEjgbakOdemI9AB2UoeQwNJSebtm1pvvIUGAUwHVRb5nj5HCZtsTLBeDrxR5VocT4TAh4pbNAkpUi9mQdCLYXV2ThH4CuJhEcwVR_0Jlyjx-zEiXhKSpLfdjdFS273QZojV-FNsCZR9PYS9UEpCMm3CpZXM8u3n81-Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ کیت اصلی بارسلونا برای فصل آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/90150" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90149">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/Futball180TV/90149" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🔵
باشگاه استقلال مذاکرات مثبتی با آلومینیوم اراک برای جذب محمد خلیفه سنگربان جوان این تیم انجام داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/90148" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC7_fjJ5eOVn3s-lpZsILIGt3AVCzWooGrUvVDJFSUqhDzJZNWtj6_NQQElXGICb1oHbz_yPJ6Xj_c1RP_9zViWSBNm25VayM-zcpjZFhsGlcK0J6BW92A1tt8iJzL_Dn7pzMHHFqNZRzAge36ktPFw1rmv7H4vMIORoPrLobOKH5LgfpiKCTWaa_hbHyY063MoRSv6Krn_II-uOy9V2ka1PCgRAfFLaE7MSIyWPCmXE7Li9RnjctbqRGOMqy2oBCUXzWiEdyNck983OdOk-Up3i86i0Pb74usU30iSpOrIrSmIa_urlYzGtk4nqiOT3j98fm8jnyEK_vhkWXxjbBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب‌منتخب بازیکنان خط‌خورده انگلیس از فهرست توخل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/Futball180TV/90147" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6PiBbuERCK3ekf0Nm5f9B-Zju7LMJEP22NqILsUjTHCq7HVK5npNJq-m9bc-fbCDWmQSVMIcfDBJOelMfahgJkf9t-cmoK0RjuJNI1CbiSEcRTMUbjBEyP4WIfxIX0hLqX5UwQG_usPTOTw61o4o3iIONHn8MN8mMGFeYtUy3YhGh_JUj0XCXeFChuOr_jVCNwBwCO28Y6t6dt9hY75S-u05mthmiw970MCtSxxhhWwhmr08o-FukyxDOFJhj_jPolTbrfDrvR0bN0ERDtPbUzNO4G5dbemm0SwTFY9-ttS3ystBDEtexbtYgDlaCy3nale23hbI8Y-j133g2xWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی دوساله رسما سرمربی دائم منچستریونایتد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/90146" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AibFSr2LWnnBoHIweE1OMBWuATn-n92m3sNA88HiseelS6EqKbF-YK9hCHYQvNNnEe7H-qK3VqAX2Nm0YKAuwf44Dj-QDBG2EGW9-cWGO0cfnApNDuFkm4qH3g-PSRrFC2_koSCpliztnq8A-4e9YyqfpPxWXBVJlNPpJf5WLY5tb41R35OgTaCl86wfp9EtfMw3ARVMtoZdqWKeaZtsFn7Gm9gKp5AEgjImd4Gg8IhiuzEK_xts2AyWVQrqDvgntB-tQUsxW5FD0a0dPA906RVZzcrAjpRXoFawkM7SpEGapQMFa0PtWJecl4EdH8M2E6k_rCY6RTGr_SvEQonHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ پپ‌گواردیولا از سیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90145" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90144">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90144" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90143">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJw-ZPdSt0saUG3W6IgbxZ2jGue-gVccWgTucYD-gOOXhPVWJtDuUSKu9hf4fbEjX7QZZLQu61g-kzYxrvnbGh8U9WIvD_WlBEhvtQX0GqkNfAP5SmxU9Sve1oKxH7eJzQ3AVYj0BLMl_NoGTY8l2LfLWQmI-9ZifaRGmgeRg6tG8505YM_2-o-YwDcV0fDUHsDn1qptT8OXHAGMBEAHZXYoIJtBW7B_7UoKwCRMdx0NOzbenQYk-N0NG6LRcciDwhO6p48EaeWI0jz8mwWdzQ295HcsJE-QAAmvnQv8UuAKz2TPSCanpfYkk72PRGM2-XwmBzzPRLC0eBFupt7cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/Futball180TV/90143" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/90142" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFwyhrfefDyzLAYXDmUHjujuKySlPEuAqV1yb-laMhVhtutZoiH5XMfSqejNjWlZtpm0_UqZJLGupyhMHD6eKT19ie2LMfR2uhFMj4WVXzFuJbxjxosYeD0nDBYUHLRbApH5jt30GMycCUp4SsUm1_pGA5XKzaQjKh0bHF45-COWQ5f3oI3FtfutwktqFW2l7MecqqTvKYr-dVR0FMhV5OEvut69VI_0nB7N2qYSk9TfuaMrWZ4JoxYCPZ_ullEXQsVHSPywqIQuHDZCrqT9jZ00VeDIoUa8n4-f_56jHwzl_darVoPZPn3S9cMMeshX-aJMQ7uogyLBkPcokVADcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/Futball180TV/90141" target="_blank">📅 12:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇪🇸
آربلوا: با عشق و احترام فراوان،‌ فرداشب پس از بازی رئال‌مادرید را ترک‌ خواهم کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90140" target="_blank">📅 12:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🟡
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/Futball180TV/90139" target="_blank">📅 12:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/Futball180TV/90138" target="_blank">📅 12:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90137">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAG2FqJ79sivJT3_OwTpUDlPzWJ7Q2pS0os6FPPIvXTgW4nLXE4PvsFsrh3JuF7Ip_p5wAzB91z_Tmj2bavJ41KcDK7RbZCeUPUpZKFjj_VI3vzKDim6IEWh30yMrg3po7w49j3GbhcuqoJsGETHS66IK6Mqej1VbPg_T_A_bgJGOMs1znFTCxzQrUZChFURfHBFuswD_z-SVzvILsXFqy037oGzmIupJutgzOUR6urztqJ_h2KAkt2_crvTzFfN0bDWwg0KvL8fOK2b_uP3_mbnq0aeITgTzaYuICduUciGdtMu96N2dlOF5tffgvBtYO8-HR6iMlkFVC6wmlkNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کیت‌اول تیم‌فوتبال میلان برای فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90137" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90136">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90136" target="_blank">📅 11:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQP1Ju8e2A3pYLkX-Pa1TkDmvgGRpKkipgXv22rqKinLr35OdCO3mhHc7dvsLGHQENnm7lKrXbbJdjNtGUZnFYU1C33diaKxlIrtaBOE1RkhEIL86RJuXDPBL1lf8d0l0TxIE9NZZ8AQVix1GLSac4bUIj_yGjGibm7BBtmBKBk9SYgEU3de0hxn53nN_cDkzp51vOg28b66c2X2An8SGlyL1TNXGcrXfWme8d1TUZHghmKE3TgJmIXkdsBSTfUsFHysOAu_HzoeZiCYSM3GX3LrL4BmwDHVD-8R3Swz9J70HlFyLmZw_VcJnoA7qFXOy09i2c4KyWySPc0h_MB-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آرنولد ستاره خط دفاعی رئال‌مادرید از لیست انگلیس برای جام‌جهانی خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/90135" target="_blank">📅 10:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRQsaKIbcMVGEuM2kvlY4cA2MtTt9ZWT1nGUq6zcA5Q0QwJNpv8ZH-jb6HJQZtvGARHwLh-IGUPLUyGgQ2bWc1wwhSwigxalmQVGdrlASbZV54CHv-DAo4aNI-bPT0XbTjahTjPeAe46m73f97vv2IzYHO1hOWF9iT5Xw1A4w0ognrlXjlXaGimGVMiXZHuQgC9a1n3mXuYx_XXlULI2a7R-fFhTjXx0YuXfvVboZaxVi5KU1VIZihBvjcQYGicGwO5E5vc30SrXOeAN7haLnEQPe_NTEF-oatkYumXGILyg_TAtHf7mn70vSdzZhB5alS1YQuUkjYVTmyp9twy0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه بازارهای کشور در اردیبهشت ماه:
دلار ۱۸%+
💵
طلا ۱۱%+
🥇
بورس ۱.۷%+
📊
مسکن ۱۷%+
🏠
خودروی داخلی ۴۵%+
🚗
خودروی خارجی ۲۲%+
🚘
بیت کوین ۱%+ دلاری
🪙
اوراق بدهی ۳.۳%+
📜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90134" target="_blank">📅 10:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90133">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90133" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90133" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90132">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkWieytQWjQ8fUZi_b8Xse_-k0A3KRe80TAs_bPmOCRQJEW1NLvqrZ4HrW2uKqKbCKFWb2D5R_nUkqRitCieMHpu0nMa4eyiqbPbkBk0g3Zrw8mb_vvzq4493tfpt7lRWylu3ir8evVr45yn0lDlRFRIYuko5oZbmoHrsToRC692HktpFY3PTE_ou83DRPK5xYSFrtE7H7imq7qGAOitoYNCE4RylpzivK8qlry0Xyp7RFGUqPqJgtsKTy7I6eU3IncqJ3HWL1RUmzF5WtjL1KnDCzw-0swe6OAbrlJ3IK2rt9AJNT3TGzH5yCCPO5IBnkCVWYw93WC4Ukg-L71LZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90132" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90131">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhV0akiuarEr3HPbbPmkojZ9rI_DDOsnXoXEfw0dqaeByf5vQRhPZGqVGxSjkHxm1KcTbrypAzWV9irvzaDm4hNangkzVm6CMJEqZD937wWS-2KLNjAcNjUZVLMWMaq6F8cGvCEb4BIPqYANWJ63P11FSPnyszyrFITgvQwfawj-pjNbPpycocXJrTqUQs_cyPMG70myXtqyfJvDr8SNlS8MUAGskKO1h_-kN98yuN7LNSW-b54cvHPfXxGT440eeDlJxyL_C_SVWnazWihtbPqqKF3HzalpcMEhjXD5olWG2RvQQbWjIicn_Qly92R7XQqA8DD352rMRdtQvt_S3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/90131" target="_blank">📅 01:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=WVNvixibFuEgE9QUdGEZCvvmDu-YboE665a-Z6PzQ-z7haX83O7oDPsdLppFrCdiE7F1i-ZdVMY7WEvDJDyiR_DhmCMwTh6Yw2-ENFJ6Kzesfm8BJk6I2RX0DOIwupe_qt5mXUvW5CpY0ORQNfhNKkQ2HPpDTlurE2zz1amdMaDjTYzyE4SeU7UE6cidktERnAsOP1YbJ0owfgA2O5x-W73oDa7P6Le5yGu2C1zc1gU-2kaJQqcasf1SmwiRShTgwHqxoFTflDRZBOyQZy0obtUnNPJPSlkYILTRBfNoWgkliAx7BDYXMKCA_z6PRBwIjK0UL5j8A9L8Ss6VoRD-Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=WVNvixibFuEgE9QUdGEZCvvmDu-YboE665a-Z6PzQ-z7haX83O7oDPsdLppFrCdiE7F1i-ZdVMY7WEvDJDyiR_DhmCMwTh6Yw2-ENFJ6Kzesfm8BJk6I2RX0DOIwupe_qt5mXUvW5CpY0ORQNfhNKkQ2HPpDTlurE2zz1amdMaDjTYzyE4SeU7UE6cidktERnAsOP1YbJ0owfgA2O5x-W73oDa7P6Le5yGu2C1zc1gU-2kaJQqcasf1SmwiRShTgwHqxoFTflDRZBOyQZy0obtUnNPJPSlkYILTRBfNoWgkliAx7BDYXMKCA_z6PRBwIjK0UL5j8A9L8Ss6VoRD-Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2ALYuCXT2zmz9TkdLycEv7Q-V8w_KlJgsI45m50HrKRjPD5OfUi8D5DGQlloRCJsBmJfeD_lRs-P1U2rlUyUHn1HEtqKqJLqvz5Qo3R9bIfYghW8jqUq1RMvrIpDeZfLroD937JPL-iv1aMvtOhfxxWgcF02_9AwZTblg_33gG5LqNb-S5slh89detvR6I7VnSJASYxJAEHgvn3VdqOvAkAB9cSYBxgUjnLyOeCFYcDaxqBoQI8FhQwmHztRKVEa0eW7BTLQM2vVakwJeipBFwE7Zlcw5gAySeuL1hbH2UaokRNv2VMlK3FURF3Xw6ps9zDiHMf_cONgqw5stVwaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3EKSnS5MrjAjE_nse5yt5y9-ajZWUzP-5c2qn-YlwQBLVSOxIihBTIglLn-ktH2A3JIgT9wzV8CGQz9RWTH6VdKT-PraVVgi_s-bd_aj8gZGhJwir9M1T-vpVNP8qfKM2-H3aufWVA1KSKYZPAvBWxX-T4GscNXtlYeJ19gIv6Iggd4nwUrZBCFyuttJGf64NaQL21FFEeW867U_5eRLjt3s9jMy01cwBn7sHmWDrhAVkUC1RcfABoQGWD-TXyUe7YNvJ9YCOSpEqZCZT5mnnHlqLI-rBPs79TuKT3y47k8fr_xVLEu4AGdyhDNNoER6pngrvzhk8Aq34heLMzwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیم گل کریس‌رونالدو به جورجینا همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/Futball180TV/90128" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=oEnA9E_SyPpuA6Ee8VbG6bOIFXV30BUfr9dF0nlKcMaTTAEQupSIY_LTYibKS_9VdRVNapaFBOEWmq0LXW8NkERwT7rCsvdFG46aKx5ujlpvkelt8xspsvi5fOOPhIqjKh1ihns0LSh1WTW9riFhyVojwzrS6iVsbxCJnBTauIXVskz6DngsgB3GcjRD8UHWu3AE6t6Z1mQvdc8V6MPkLqS9uunSml_BQp2Xjnma4Uo820PVCsbl6BD4DmI2qeT-XF_wUwwKxxgFmcbBv3FxsJY6xOcrifAKea7ykW2YnsOL09TcQf-nTGL-SeDUbHTAvxwCQ83_vhoeAmGGg_jUdCnLtAufye1T4cyR82iodX-UXpzsZvYa5PcmoFd2ZH3jI0V2MXDpfBeCkGu--sx_YfL0gbt2d-fOlsLZqU2bKHInTK4QFqjN8DaRbFjbL-VNkadNrSf4-KKPlCN0pfEzowGfuCDrXxZycIliYTQdmZdX99IfS4k7CdM5jmLbn150ZqW4WtCd3KFD3VNWHGpPCIQomCmbmKY0esn_0hw2NmgQJ99ktGyAzWDMXEZZc7AgsNaLifVMy668yR4HD7iyAGhd7Gj41qUiJAtXe3LSB1UoTScKWodci_fcC-RDZk6KiIcJ2EQxwb8NOhjb3qgUUUGki4KPzb-5xU5ka1_XITs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=oEnA9E_SyPpuA6Ee8VbG6bOIFXV30BUfr9dF0nlKcMaTTAEQupSIY_LTYibKS_9VdRVNapaFBOEWmq0LXW8NkERwT7rCsvdFG46aKx5ujlpvkelt8xspsvi5fOOPhIqjKh1ihns0LSh1WTW9riFhyVojwzrS6iVsbxCJnBTauIXVskz6DngsgB3GcjRD8UHWu3AE6t6Z1mQvdc8V6MPkLqS9uunSml_BQp2Xjnma4Uo820PVCsbl6BD4DmI2qeT-XF_wUwwKxxgFmcbBv3FxsJY6xOcrifAKea7ykW2YnsOL09TcQf-nTGL-SeDUbHTAvxwCQ83_vhoeAmGGg_jUdCnLtAufye1T4cyR82iodX-UXpzsZvYa5PcmoFd2ZH3jI0V2MXDpfBeCkGu--sx_YfL0gbt2d-fOlsLZqU2bKHInTK4QFqjN8DaRbFjbL-VNkadNrSf4-KKPlCN0pfEzowGfuCDrXxZycIliYTQdmZdX99IfS4k7CdM5jmLbn150ZqW4WtCd3KFD3VNWHGpPCIQomCmbmKY0esn_0hw2NmgQJ99ktGyAzWDMXEZZc7AgsNaLifVMy668yR4HD7iyAGhd7Gj41qUiJAtXe3LSB1UoTScKWodci_fcC-RDZk6KiIcJ2EQxwb8NOhjb3qgUUUGki4KPzb-5xU5ka1_XITs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل رونالدو در دیدار امشب النصر مقابل ضمک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90127" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=JrMUdc0lXMBVHTXt2zwK13Wjs0Ydkn3mETAZxgQWzH4Y_ZXrpbnUtqxMfsYjqnc7VR3VdiyhSJZyrPInoiXY1vuPRGxJnMY4AsbPVbIlczxEypQla0OByGZjIYGa-yQuN4Eatx-jQKhNVGOAyGyBlJet5nOuETcArmbIiIOwMzY_4ndbeA4qZdnofxMjRG5S2hUs8dLJKuvoXSLqXSQvElC_JDqwmJsAyMAWpaolj3ze3ioY3ajxo0Zck_5f0LDMSJjFfcpIYGzsqfwVHtBHqf6nl620A9FhXeCV2PPGEu__bCq6rI-8MZCQk_0VDXIbEGJdQwDeva_jaVYZ0Y52Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=JrMUdc0lXMBVHTXt2zwK13Wjs0Ydkn3mETAZxgQWzH4Y_ZXrpbnUtqxMfsYjqnc7VR3VdiyhSJZyrPInoiXY1vuPRGxJnMY4AsbPVbIlczxEypQla0OByGZjIYGa-yQuN4Eatx-jQKhNVGOAyGyBlJet5nOuETcArmbIiIOwMzY_4ndbeA4qZdnofxMjRG5S2hUs8dLJKuvoXSLqXSQvElC_JDqwmJsAyMAWpaolj3ze3ioY3ajxo0Zck_5f0LDMSJjFfcpIYGzsqfwVHtBHqf6nl620A9FhXeCV2PPGEu__bCq6rI-8MZCQk_0VDXIbEGJdQwDeva_jaVYZ0Y52Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرگل کریس‌رونالدو برای النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90126" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS_RhiV1eqvx0HownTZny3udmIqax7iGwVIImZURXvDdNYnZ6tDzboXuQb8553zUfgwjSF4IvAVutmZvcKkK03eYYrBGIhqbOxqgDZw7qMBEt7vhw-5uT7h5lBbEXBoSJtduUsVCnGsglM-HDbhRVFom6FULFkluayMXgjK9mQgd3hQRw1c6yJukyd26w_Km2Lmm8ZjW0x5JGrAVW42hq52ZHMuk6tUrunLG4a-Gx6DWT-0xJgkhJVi3pCvaMZjCrlF05JwnYtWtgwR_hw9V5aUjZeN26urWnVcHRAgo4KpX-RdEVzY-DlAhuSBHhmPjmu6OK2dKrbCdKcCGFoqDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
فیفا قصد داره جام جهانی ۲۰۳۰ را با ۶۶ کشور برگزار بکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/90125" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRSas3syCT3BQ_33xxnRJKh7xaUAgkGEsowJYLwIeAy0wbFDYPlUzHpxiKfewUv6ATL_gH153_pdh6UYSpiGQE5QN-MBgkRS6aDVLO6JIJFapGVgc24NY3VDYwS7XxcggXY8DTbAVDxgymEjLUnOyfs2k3Wn_yMYT8NuuhiToh-TuNAbFVHgi8Hw-505FesTte5-VCUDlC9j26UVsodprp6RBVbOsWr33cxD2vMwXiq_T_fzqDFAiXthB3zEFb4fd9Q3N9rKgx2bhQB0PsWH5xBTT-YYYxygwSfDRWmXlC0gwTyrrTA_NfuB75fv8JXdF_0u07Xjqfe4T68IFw1IYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوس‌دخترهای لامین‌یامال در سه سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/90124" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90123">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90123" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/90123" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90122">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz1iR47ammyAIUzBa83tXgVBmfrm43d6A-lrPoTLcS0KRRr_6Lk6v24hznsC157Z1iV2uI2Vw_IkKTCVDB2pfLXNMd8WTQyp8nXTffe3UQryggw02iuZxj9UrkWr-ZMuJQRBA-1d52mERaSXtHZaiyXg1a3-psanDupVCoeGFzWN8wJEghT78gKRGBKItnJw77JgL9y0Azat-ydBGCHd2lgvHhNS8mbWi1VYjmWygY1ykOB69uwNWTV98sYH8-fdn6wzsM00UR_zW9-cEADMHVzRs1VyQMHSxprJNWONtDTVOyflqaPqAFVcLcAKTMWa3rKXxvwrtQskpfIeqUiZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90122" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCjQIjmRmEDMvw5pcTkFBH3pVEiJaySRVfHnuO2KlHUkRZ7AgfewoGCIymizdHBkW2pYW4LdO5WQtxfR5lEZUObJS6xgfAgwpGEXXzhcUJDvDcE_SNRqbLZxvf7Ja0JpQ_2XcmL21tzFRtqZG112THbd7EUiBy2J2vgPku-q9KVnbzSi-R_UefrW3mWnTmdLpmOJGEunCVv2K8AGLNA4i5gtYGUl5IExexAFGEekj9XtjiVVyIzgCHjNJUrJvvoaZVpPIO9d0H7f7ZBSOi2QBjPrunnAxkR9Zba-MFKZc_sdt6-9IGCAwcmtrj8VJpBZDB3qiFJpwyQTUaiwcucLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
لیست آلمان برای جام‌جهانی اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90121" target="_blank">📅 18:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvKZR67ENSgCyq8UPTE3N-iMOakAQXZ6X1cMNanBFJ-6pPsd6ITKZ6lFYaKDrez1E7p1OIa1xVKXfKflmB4CD1mHMvTH7wgHWi7wU07hviMKLF-WSB5xv39pO1JKUY7347xalbbCmFcVhUEnKJO-wbqGMzacc-lq0BdvduuUy64SdwYRZVP3wntif0OQCJrXr9IftL6x5J-xKrIf0dWJoxRqJKJ_fXC0v-raevCoA6bgK4H2ZcB-M1JFbBY9TmjoQD9nmh9p5luELlcWe2yticzZOWZSXSoK2N7Arv4_ibaQFNfqjkLV-6V8Ookyvpi3DOZ_3GudTd_8Fkcq4R4pCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آرتتا به مانند آرسن‌ونگر‌ پس از سه فصل نایب قهرمانی، بالاخره موفق به فتح پریمیرلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/90120" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNIOBLwL10YFzyLJY5xHySRzMHFhXrPQtar_5-N_U3pVPQ0YxbLpxLc9CPhj0VgT4PbjpkDjOsPu46EiIfh2y58cwFkJcKi-rpiBxFf0d6ka2O3vjtZZUpuLcJDboJO3bY99IdmkTPqII_1kRw1EKZEjGmXtGaWLWNZRg82IdE3vV2Cp3tI-X9-aq0-a3sh-m2FoA5gJ2S3-s1b8TNa7iV3mfgwgXHauCg0y1WwGZwJtYEZqZWM1OB_tc0Cj-_T7Nleo4g3OqdDoZ9JzETpKSYr0IF-15PLwGX0KSsbk1LMLfOhIckmnPDd2bSJ2Y76E84d_IHmh39D7uhZJsshJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی جمهوری چک برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/90119" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90118" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90118" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INYXR8komlbLPWh2kaxkeyNJVUPAuJVkl9otj5AeJxwAG2lvLuuDqwQgeLhS6fDMmlNORYijLy0cqrUQhBorltBV-r056GCsMs8lRFY9fOmMkIPnJ1PGuUhTDEP3mRan6LEQlIhnVlQa6mN7ym2Qij3VNSlVc-A2_Hv0AbCKJ2OnmSSADlYueLH8YPMhNKv7MrpP_EVeIfJJiJuwQltCmK6tQCbglf8TQIa206TpWc8t1XrahsOZ9M0K091c7i0o_uiDzO8ZXgDVni3eHQSbAYImJC1reO3kLuKnJP1fP9skZZclWV-CRbbyApjDy9vCL_l66pOngpZhHMMYNnMnWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/90117" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
فرمانده ارتش پاکستان، عاصم منیر دقایقی پیش وارد تهران شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/90116" target="_blank">📅 12:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-F-FQsSgC57NisqLYZ1yNW9mTw9XcxXtubQgGdGF1UvVCBYdCJpyQvajr8PHNkmLOzwZcH9cEMfmE_Gt230xOy4wAVhr7HgQRIh-RSUY8nffzLK1LwED5Vi62EFhoNFm4q51w9KGCZCdmPbWRvUZyIT9p1VFsjBuml1qNUQsxVTdDGXJl0WpYE7z5VTtjTinRn-sdoxg3KYdiKFqJG_i5HxC61xviXw0wu8PO_2U-dD6aU6dnZQRD_n_owBHv5D9FTRtJMonkgjgo49J9DnG2656RY7ZsiD8ZTtPlShKUG8Eio_NH2fACtDzEEi-nIQwFredX-eV3lmyKql9pwZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه کریر فوتبالی لیونل‌مسی و رونالدو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/90115" target="_blank">📅 08:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90112">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TasnHyAi6s_jHLj_IPRFVmwkRSObRtDyS_lMvoPHa09usyIdeorRqQEklnnelA4wYqmpXJhvNX67wOSeeVJziHqGGm9DxWrsIOV00xUtJOk9m-1TBAI8z1lkNwKXusGM9hN9hF8koHLFEs_x5q_qbLXl8Vi5bhXKU2WtH_EYciAjvhPa-Imb0FMg4kql5PG6IWyVZWbPxmLgLLdpfV0NVQYlJDdOJLz88YLWAh3q-DSfL4grhFHPtwubjjCW41V2j39ZRHFlgFY6r4yk_flAtCr6Gj0Ro3pmEu-HgyNTbmAyZ6SztDWlGMRS7173clZPff5lOa2ljtphasOKe1DiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل فرایبورگ قهرمانی لیگ‌اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/90112" target="_blank">📅 00:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
👤
برخلاف اخبار منتشر شده، سردار آزمون بزودی قراردادش با شباب الاهلی تمدید می‌شود و‌ این بازیکن قصدی برای حضور در ایران ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/Futball180TV/90111" target="_blank">📅 00:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
چند روزی منتظر پاسخ ایران خواهیم ماند.
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای هر دو طرف انجام دهند.
اگر پاسخ‌های ۱۰۰٪ صحیح از ایران دریافت کنیم، زمان، تلاش و جان‌های زیادی را صرفه‌جویی خواهیم کرد.
امور ممکن است خیلی سریع پیش برود یا چند روز طول بکشد، اما ممکن است خیلی سریع هم به پایان برسد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/90110" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4sVkZniYOQVyHA9Ip45mouedGk4UGpZSneVvZ9_LGhTCtT11zd5oKTeyUHncVLQsg_twNUGUrpL1VRyVDTgEC6oJ74A0I2ZdxU0XdoJBuU0ZPLpqCAdIrdyC8NCvUHLAoDI5cxePboQ3690CbsKPWKPi_T8GXULg34bxpJHYYykNwXu6AscPbSXbHFzauYwdZ1poQwe0PYaWzPZxPcSyocD_I1p2BsUC2Bi5eOIgtD4wFi91yBc-H5hEG6oqik2Helo5ZEeFjdM1Ty6lg8VMBpBrEuLsMf6UDs8Gae87E6lqNlpXyujZfPEL1q_m4HfXYZ8brLNkhxKqpo6m4p0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون: ایران هویت، قلب و افتخار من است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/Futball180TV/90109" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
