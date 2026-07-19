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
<img src="https://cdn4.telesco.pe/file/RB7jsSRsErKHaUH4E-YOuKK3iyxmnVoDJal7tEXsd31ndInj26JdZsN5DWeodzvKBtGxD6DhtlgS8hrJvD73NdOjjOLUKrbpTM_7XNfqmF5pTDPAjb4w_K1-hI9hVkJULmpqMaG-2IpysWUr_ayMm75Z9iXmgD5aGb8EYGGxzFCXqAlTDQoMP2jaY-iWdqYPqmQ85RhXJ-CwcpKVuk9pxOaWTVHApNaZuRqRlpGuS-QO0fYJOOTyuANU7zNNY0wOi4q3yznZSP2z-0UaOd5HOf2M0d_7jd-J0C2DbO3evPWQNHBazSG0QwoI9UVO3vqaB3S3IivPRDW2lFZJCLndWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 162K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 11:07:53</div>
<hr>

<div class="tg-post" id="msg-68521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
در هشتمین شب متوالی حملات ایالات متحده، نیروهای CENTCOM با موفقیت به تأسیسات نظارت ساحلی و پدافند هوایی نظامی در ایران، قابلیت‌های دریایی و انبارهای موشک و پهپاد حمله کردند تا به تضعیف قابلیت‌های نظامی در ایران ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/news_hut/68521" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
جدیدا تو جشن های تعیین جنسیت دیگه خبری از ترکوندن بادکنک نیست
الان پدر بچه رو میکنن تو منجنیق پرتش میکنن تو بادکنک و آب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/news_hut/68520" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇱🇧
پس از ترور خامنه‌ای، یک گروه از حزب‌الله تلاش کرد تا پسر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به نام یایر نتانیاهو، را در خانه‌اش در میامی ترور کند.
⏺
سازمان امنیت اسرائیل، شین‌بت، این توطئه را در آخرین لحظه خنثی کرد، زمانی که این گروه از حزب‌الله به طبقه زیر آپارتمان او رسیده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68519" target="_blank">📅 09:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68518" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68517" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BA-6FGctFNYRpd6hMy0xGM_gk5VYoIghPIDR8TJVKeoBRIfwGobA704WJi_2f89GPeChy8HPsDDXeTmoAW8RkhSf9l5XtULmhKuLagBMIT8lkwu4VJKHPR86NlsCeDcT6XYh9DLg23vcQH3IqIstv_7rj-10MMZQrrouCCI-w5OoBVhQAEaOtcod60dXI5eDRkOk0cSFl-REqNvhLpt1gsoAdR0hawn-Vl4Yx_8Buz80RCQftfGbVFJvQJXMQH_9QArdLqQCaVAkwd47CjyfU1lvkhCkcMUHCFf625yP7iEbD0U-9GaY3AcIzRX-RcaJyRTjaOEANBJaYPnMYKqJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr0fI8WKVu5xLfh6Y40N6WKTfz9tOwfieHTR5-WZEVWuRPLRrF07-g3zslo22gNxSQcllLCQPEhWdr5wJRHiViV6nrcYlciIpXGV2A-lAeybwnDNAkoNztjLE3avwJXaLHWYRP0DrkMw_-mHDFAeFMtPzWLg8mqggYDaINbN6xqLN4SsbAh6AeaIi-LDVVttATM-PTvgzB6woTG-FQwF6J15247lyx_RtRL_hhDzmExJbKsyITz_MS9N585BwS5jiLsVtwgpg21vfB3mz55rD41jdgWZZfhvYXCm0lx-weSoVejtH2qiNOPaypDvICc0xJ7X_XTizrjqbdQlhaZiuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
حملات موشکی روسیه به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68515" target="_blank">📅 03:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🏆
رده‌بندی جام‌جهانی فوتبال|انگلیس برنده جدال بازندگان در یک رالی تماشایی گلزنی؛ دشان و تیمش در روز رکوردشکنی امباپه و اولیسه با مقام چهارم با جام ۲۶‌ام وداع کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😃
-
😀
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68514" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
تسنیم:
حملات نظامی دشمن آمریکایی به حوالی حاجی آباد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68513" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68512" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
دو انفجار در بندر‌لنگه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68511" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
صدای جنگنده در آسمان کیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68510" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68509" target="_blank">📅 02:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68508" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph-wYO6kmrLWyjEc8ZM63zlPKSmi9rTGSG_YaXEb3D65vfio8WF6mciqTyhj88U_lZ_YH4MyZgw_V7yGZIlyzMdR2YwgPYqq9J7DBu5IbeswbouLMPhM75IKcQQxoZIZHw71x_WmZQqn3Ine7fVj_hODaygPk3ZhPRQMc_U0g6q_SX7bccSykLLBz2TL38zhbRUsDE5n4Llh-BRFCaRm7yD9_QY_LPsX2wBFxiz6wpYvEpn46oQzylomdM0fNVBNaIgwqZLdJj4DRYVwHD7_U4fuaFVMIe_6oahsiJQVFmawN2fIzsg79jwqd0GCDMuHgmvj66h1SJqRMNhDq2at-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ عصر به وقت شرقی، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و تنبیه فوری نیروهای سپاه پاسداران انقلاب اسلامی است که شب گذشته به نظامیان آمریکایی در اردن حمله کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68507" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام اعلام کرد دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68506" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm9llfHlOia3Hzh2XeNhHNa8_JxSZUmcIU_sP5iPn1FcWTnyHNB5mByMQj8JNKL8my83wLFg5U1NdBCzzD9WU6-oCaI0gIYiSM3KjJUvOomXH3x9eLbBNxq8_4rnNp-qOSHDlmMCerLLQ0x7d1Dq3QnkgVR_acHCj4vvG7kls_P_Sx4No_44Ref_OmQhTt2s5Ny4e74YgSrQTch5H3L6-rs3pGZ0JYCjC6ZAqUxbsBUSsbJYrDVrZWb_qdKqSuiT8w4whyriu8QQvO0ivGEqkKX72EPayqUIK3HGyIne-ieLJ68hUQdIPfvh7W_682dNL5ONBj-hbqxIjhrtu_3fgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
حداقل پل صراطو نزن بتونیم رد شیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68505" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d09qu6YZZXi5nODoudor4e0PapBzI3KNVDuv4HBLfjqcIXUOubnrjIjY2U-M4fOjcLDGESD-Fz4UM5ABlouaQAreW8f-KNM3bcINw6pc9HIMq7xDUgt94g6kXVzd9uyi5qbfrbKotQLixG5IaMXzA-TuLEucSZwqKk01tDejMfskeK0CPhEo9hMvkePx3iTpZgVPNwL7xCJa__8FDKT42qKNUMKA6p3ivJNMTQqqmRzU8igYklsnVFFx91nHu4GU8E5AZ8VxXqRmKCw5QxH55YfktTiNIXPLjtna2emJZ-iTQ2m2zgoR0gaaZfmq4YtP75-Kh61LVBjf5TX6NSXsnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijQj3P7viDxAtLJwJ6QTPOej5dtwcPfDlCgAuS9X07VhZ5I0-0-2OLUxWQsD0zjwzt307NVtOufzfkLeQr8kdR66GFL0etjF92ikm8LzeSImY6Mc_PiBIn8g2t-6FClnNRwP3C9wNAPI4-CDaIAgarECIH4bscEqpvJ9TVpqBwAomFBzQIZDasEvjk7tTUn3fD-jNv10V7UdiyF-ylnOU4bvJXa2zM0G8K2bP6ejVt0qnqeGW2gycAnoI5rrmsyAJtL-NY2Ot8hHbgvK8KdrbMycdWo-FZHofWBg8KOnbEJqsbWn0YSUfr0A47xag3xjpCNGIkzx58lq57owaie3fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
امارات خواستار توقف فوری تشدید تنش‌های منطقه‌ای، بازگشت به مذاکرات، حفاظت از کشتیرانی در تنگه هرمز و پایان دادن به حملات علیه زیرساخت‌های غیرنظامی است
🤟
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68503" target="_blank">📅 01:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرنگار: ایران اعلام کرده دیگه به تفاهم پایبند نیست نظرت چیه؟
ترامپ: خب بتخمم
#hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68502" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68501" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68499">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5Wg3kiQisLZH2zWXtKiQDVpJZxJ4FIUMzqxJecfrTmA_XJmmzPMd7dl8dMB4E5n4EAJm4ng119bx7mFbgGmd2aTql0YguuJwhLEEyYd2346bOKFf3gX2wa9s9FQePrrTWLVtXzgJOH5Zzm6B59jqlgVRCdGnfWsalvFvcfesLAmY7fWgD7EllVnT6ZQsM6rAdrbV-t4He7UpX1f5B-_jgParGEP14j_T9JwtN7ExCDG2UmWv1uhCmu4eR2vKQ59pXoa7UZKCiIp9Q4wlZYyHn1nftd5IXI0nPKO-ewnla0VNeZg_a1xW_mMoFIkeSEKUR7Onuq9IDaSzhpZpzy8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eu1MviEu2aX_-mIjClk2Isq_a7QCbTlI7MnTRSMdiVIzzWDAxED6f3YJWRAAKSPbuNpEo7NhQur0oel8xLxaUVL5zKftV_0YaGkfg-s4ZIxb6Ke2LPLqF93Hc5q4p7EkFySnSgNBskBYUu09s9WiNS1vU-gRTjSwe1kmtBHKUV_gnXXek4UkU6Rndhx1CTJj20bqnQQmcwyEjt3zi9xcXLzQ9kjMagUrF_jQfZw96j7DEBLRC5GYY6IKk6GPNLtp3wNp5g6Bs1gmcbqMSy_SxyQ1wky2zc-ZuAzhKZ-CsMjWCrpAKKj3IbeoftF_w0-KDzqnTVQs5TDqazt3K7axRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68499" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68498">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRP-bUQdm1RznP8WO_madhLZf2YUAMpMzUEeEXNJUWiDD91laScn0N_ZcsfL_VjGDlaTAMKqq3bwy0W7mdJd-scjQT0ApaQmlaGEEoaJPqf2731w3Y351q4HX60FgvGzeuOm_Pk5OmNz4l0e3NrbDQBFQfevoQVhZWlW3DGr3dCx7GLe2IaV3zKL2DfogZ5uwYoGXIxckqpJt7AP62K-uCbQiFy82AiTutiE2brTvMPcLDBxc-DK2u7kGv9Vbi37DIcW5cfRb-UhuqVF7qeDuFqmb3-Cjx9y9QXybkd9ESnQ-y_2X6yYOOdfZmsQbKZvvYDVV5EveHbs_ZdzKD8-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
دونالد ترامپ، رئیس‌جمهور آمریکا به «نیوزنیشن»، در واکنش به کشته شدن دو نیروی نظامی این کشور در حملات ایران در اردن:
«بسیار غم‌انگیز است؛ اتفاقی بسیار تأسف‌بار است. ما از وقوع چنین چیزی بیزاریم. آن‌ها در راه خدمت به کشورمان جان باختند.»
او بار دیگر تأکید کرد: «ما هرگز به ایران اجازه نخواهیم داد که به سلاح هسته‌ای دست یابد.»
ترامپ همچنین اظهار داشت که برایش «اصلاً اهمیتی ندارد» که ایران اعلام کرده دیگر به تفاهم‌نامه (MoU) پایبند نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68498" target="_blank">📅 01:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68497">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3ALfJg7gC67hvOWgD-l-Ol1_323p41wF8Y1HofGe2fiXM5DS4yUsEq24wSYpPHPgOHn-XqBzLBlixJ-HSyQWrtZEpuI1e6TqU2UlKOO9tzy4wlaU_JKPhuRHdQUOpdZ0tj-E80eClLrYFi3XGrN869ASLbQL_MRXqr7m-Rku4WoAYzXvBdXDx-ZRpyCBewxxX8dyUcmlmaTxs4rsPiBkOLK0mg2qYW-h3raE5we2HdxMnvDM_lguB2OtPWzi9f6gSk0Gv4TutpULKsYa5GpMfIZv3ggGxeWJAcQRe5q2p_JY_Ze_509yeu_jPsyj-LAd0yEa-9bRypD9B9-poRmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه المیادین گزارش داد که در پی حملات ایران در خاورمیانه طی هفته گذشته، ۳۰ سرباز آمریکایی مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68497" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68496">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
بندرعباس زلزله!  @News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68496" target="_blank">📅 00:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68495">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
بندرعباس زلزله
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68495" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68494">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXAanpW8V-aJe3RaMSCTiul1U8DM2kyaPbYyglfYNo3u22Nz5hQ9ivnt3Z4Q5DSOyRbJe_vAEO3DldjI6x8gICm6Xgh48XQwGbaLujw_Y5okjxuuzFLOyIsGcyXPTY1SI1v6DELgY7lfL7p6f98EYO7vbD1HUu_AJnvwS9kEC_9oXNteETzpPPufBXXTWTYFStWbS2i3OdZcOrwypo7FELHVQgxA6rZkvm_NbVFmyunV9WyYbMGuVju-FmRpBn0G8JBvqjiJtNRVr_fezaK1b0HFXX8FpUOPM3gO07bB4-tDKkY1HmvVIe6aPN3vXptgKwwMpwJYaRUfQQzGXJDBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز: ایران در طول پنج روز، چهار حمله علیه نیروهای آمریکایی در اردن انجام داده است.
اولین حمله، یک مرکز مسکونی در پایگاه هوایی شاه فیصل را هدف قرار داد و تا پنج سرباز آمریکایی را مجروح کرد.
دومین حمله، یک پایگاه شرقی در اردن که توسط بالگردهای بلک هاوک آمریکایی استفاده می‌شد، را هدف قرار داد و به چندین فروند هواپیما خسارت وارد کرد.
دو روز بعد، موشک‌های ایرانی به پایگاه هوایی موافق سالتی در ازرق اصابت کردند و حدود ۲۰ سرباز آمریکایی که در پناهگاه‌ها پناه گرفته بودند، مجروح شدند.
یک حمله دیگر در روز جمعه به پایگاه هوایی موافق سالتی انجام شد که در نتیجه دو سرباز آمریکایی کشته شدند، یک نفر مفقود شد و چهار نفر دیگر مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68494" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68492">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIJ0k3Kqya0ZQc0ObkM-6K3Ko4f9fNnSWGg_bss2YSRFpgXWZnPA2cWK5yux9i81d0vssuDMyu04qpAgX27AhhOjJ_gboEQYs-HiJ6p9ZLRBpjJlM022mpY720GtBhgMWxHN4dQwbfgCyV4r-3EO14eVl5F752l6xbHjh8LcSwQ96_4gDRqOFNIMA5CHRSpXcE1xF3LUpJWLNApaNhae7Yxur97RAxgpKP4IFpzOKnk-rzTpsgArEXtfgE_e_wNdxnqpaeJaQ4ELaUodhh_k7JkOKsTaS0Az4jOq1GMWe5kgH8uotLHBAcqLUJ7bD5nsYTYYDGhHdbKNcg7x2zayPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیومدن؟
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68492" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68490">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ttukNf19XBcrMu1DnjiYY5LaTBf60CQXwVEVhK1BqRB2iM9fbe6xxA55sA-hxi3-Pt3nA4_oNLlqMm1Jn93X_6MjHf0IcFfyMpjUYLK722qWEnrh-z0koipLrsGhqJkkfIYG0NNHrqFakJZxg7bFiFe52h6kbagUJB04PAMXN1Nnyr4jNQCnpvtCU1z3cn6psdIvqfwL3Fx9_5naV-h5wW-jXo2OwCakTeK5TyivGBdPCWat8rZ6X3ipIv0go1-BeHM_DuvPSikN3hQUME7tz-4HF9wJpS65kaBflKOCseQ9oR3Kprzs6B-9J-NmhVVvE56Sa3InizjdLd_If_TNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/REJ2NUikQjzqxsXh_m7bERlu9r9lvEiN9BT6lPpCbieu0wxYQEDN9zsgi2NY5nrZIuFnyDHNk64t_GktCx9eEp8_KUFsGdLYUyBrtvLb8yF_pvOIQSi6iyvfXJslm-OCzvL4C3WWVslSkJGHmoNn9H_1VEEcd8rfl05yuQI3W304ZMUSCq4Bnz4ONq4A0Y483A8NB9E4ks-OkuQZ1IVVtI0jNICxwKzX43LbqIPgLv9ucTK-fVkaLq5mCF5iEuHH_fh4T-NV8GD3p9zsgSdCftlVK62dJs9VB5AEooyYN-YSE4S1fuNgiA0ewaUPg0_d6C6nQ2omz6TTbbcIeN5k4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیلی افشار دوست‌دختر سابق تتلو و پویان مختاری هم این وسط تصمیم گرفته پورن استار شه و یک کانال زده تلگرام که ورودیش 2500 استارز یعنی معادل 8 میلیون تومن پول می‌خواد، البته محتویات کانالش لو رفتن و کافیه کلیک کنید رو لینک های مدنظر پایین :)))
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part2)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part2)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part1)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part1)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part2)
🔥
🔗
مشاهده ویدیو های لو رفته جدید
(Part3)
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68490" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68489">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اماراتی های کاکولدزاده خواستار پایان درگیری ها شدند
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68489" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68487">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=ferWlw6yZ75UCVH4n_ae7220f4CwAle5gtz3huuO-Xip6ZyhTO5PmcD_u7VczfwYicNULEIKLoPO4YJZFAnKdyrYofvXcFtKvguaSlVrGqPK0J9UEtH16b3X8QLsdkVlPJCTeza0uZPYw6y6I9iMomQ3hGJjubCqaUm3rcrA5PwiIN0G6RU4o774tyjGzv25sCjVmnqTe19Os0yQWyu-ko5mej4l_m6pWwx8XolszvAaOXJn7zTQKbgEQN5kr3M3urigx4e-fktWerQnTRaj2L88Jj9YUTUTISAH3CSS7cBzJuBTgdMYwSxfs9dt9rJpMjSkDAFwkVUJtNRzU1RdwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=ferWlw6yZ75UCVH4n_ae7220f4CwAle5gtz3huuO-Xip6ZyhTO5PmcD_u7VczfwYicNULEIKLoPO4YJZFAnKdyrYofvXcFtKvguaSlVrGqPK0J9UEtH16b3X8QLsdkVlPJCTeza0uZPYw6y6I9iMomQ3hGJjubCqaUm3rcrA5PwiIN0G6RU4o774tyjGzv25sCjVmnqTe19Os0yQWyu-ko5mej4l_m6pWwx8XolszvAaOXJn7zTQKbgEQN5kr3M3urigx4e-fktWerQnTRaj2L88Jj9YUTUTISAH3CSS7cBzJuBTgdMYwSxfs9dt9rJpMjSkDAFwkVUJtNRzU1RdwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایونت ورزشی، ۲۶ تیر؛
پارک پردیسان پونک
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68487" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68486">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام آمریکایی به شبکه NPR گفت:
«رئیس‌جمهور ترامپ دستور داده است که فرماندهی مرکزی نیروهای آمریکایی (سنتکام) در ساعات آینده، «دروازه‌های جهنم» را به روی ایران باز کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68486" target="_blank">📅 23:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68485">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=Ikr_M6sZjzTiOO5o2iVQGqu9avvIfdE03RaAR_Yf4cCW4eTjX4QWsN7ltI6EeqbNkGHI6qBHoFDFBSCh23IVcJL64BxDC1RkWxoQMmgb5OmEnJRs7khQtRZnlLtKWEYABCgi2aHC6rLgPj-C0jl9gsm73A7T5ttg-3Er8_XXgbwDjIFF2ZEg3a8oQZQEeancv4Yf1mk9J9jRw5rZZ6coQfwBNTwKkj5cbuzwfy9x5-K2e_p1RTGEzXW8y_qVsCWTwltj_XuqGDcKgS9yYLrxVOBLjrUZ9_armIyaGecqlWe7807yThi-0lvh6qw-W-DqYYMRR4UjrVQlGWMstvAc5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=Ikr_M6sZjzTiOO5o2iVQGqu9avvIfdE03RaAR_Yf4cCW4eTjX4QWsN7ltI6EeqbNkGHI6qBHoFDFBSCh23IVcJL64BxDC1RkWxoQMmgb5OmEnJRs7khQtRZnlLtKWEYABCgi2aHC6rLgPj-C0jl9gsm73A7T5ttg-3Er8_XXgbwDjIFF2ZEg3a8oQZQEeancv4Yf1mk9J9jRw5rZZ6coQfwBNTwKkj5cbuzwfy9x5-K2e_p1RTGEzXW8y_qVsCWTwltj_XuqGDcKgS9yYLrxVOBLjrUZ9_armIyaGecqlWe7807yThi-0lvh6qw-W-DqYYMRR4UjrVQlGWMstvAc5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که دن اسکاویینو، از مقامات ارشد تیم ترامپ در پلتفرم ایکس منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68485" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68484">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68484" target="_blank">📅 22:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68483">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇱
نتانیاهو شیرِ یهود برای آرژانتین در فینال جام جهانی در مقابل چپول های اسپانیایی آرزوی موفقیت کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68483" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68482">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68482" target="_blank">📅 22:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68481">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ پیت هگست: خدا نگهدار قهرمانان؛ فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68481" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68480">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖄𝖚𝖘𝖊𝖋</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=hJlEUwbEm_tcvy_TD9VRm4t2x5CREGIhWutgyq2ZtPllSsHknmY-O0wnGhOJLTckw0mJxIhGTpXnCLJ4Hiow9yLmTAb9OJDs5yypPhrQBCi3YhnOGCA6lM0l8wQOgQiSBJglPq83I70KmmcPtxZFt_n07bKACwMH8Cz6tVWDgY1rGIRmNwMXaFYq-YmRZPfQDrS_pA_VqZHu2K0rmlGhYV_CjdK80REa94lSZmawEgk1qU5XT_F1_4hQ69x1TW82FAaJ6ks9iVwkjJMUpm0GcIVkHHijiqdjRUo8zXVl2Pr7s0VqwiM30pzdow93o9JI4xAhY-92AHQh0FYonDULlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=hJlEUwbEm_tcvy_TD9VRm4t2x5CREGIhWutgyq2ZtPllSsHknmY-O0wnGhOJLTckw0mJxIhGTpXnCLJ4Hiow9yLmTAb9OJDs5yypPhrQBCi3YhnOGCA6lM0l8wQOgQiSBJglPq83I70KmmcPtxZFt_n07bKACwMH8Cz6tVWDgY1rGIRmNwMXaFYq-YmRZPfQDrS_pA_VqZHu2K0rmlGhYV_CjdK80REa94lSZmawEgk1qU5XT_F1_4hQ69x1TW82FAaJ6ks9iVwkjJMUpm0GcIVkHHijiqdjRUo8zXVl2Pr7s0VqwiM30pzdow93o9JI4xAhY-92AHQh0FYonDULlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش پیت هگست به کشته شدن ۲ تن از سربازان امریکایی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68480" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68479">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=fcXgDOffwCv5sI1BIL4WRtBeg5kBMJoQNKRKvU_-gh__WsjLAZ8K7COv_PGhf_BJics6dJC32hGpc2WeyVlr9S5jUvHAzSi9EaSdaSxCZvgtLr0gtZfUeRPCE4jtbn5KMELc6Cw17hNU2vEntU30I6VpB4L40NFhVWUqp4TxKhQkuFwsJaMuMQe2eCp6sqgoMiyfFV17ZdLvouRRAh5K7qUYBnrGY8PDs2TksGtxfu6zBn6pKvOioTqxYIP3Rb24kizOqIUOI1MlEqEU6ZeVOYxBxMWmqecFo3mYR_luCMnQKN7f-FhE6aKaDcmEh0h7EAS68L75zyAq2aV2BWesTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=fcXgDOffwCv5sI1BIL4WRtBeg5kBMJoQNKRKvU_-gh__WsjLAZ8K7COv_PGhf_BJics6dJC32hGpc2WeyVlr9S5jUvHAzSi9EaSdaSxCZvgtLr0gtZfUeRPCE4jtbn5KMELc6Cw17hNU2vEntU30I6VpB4L40NFhVWUqp4TxKhQkuFwsJaMuMQe2eCp6sqgoMiyfFV17ZdLvouRRAh5K7qUYBnrGY8PDs2TksGtxfu6zBn6pKvOioTqxYIP3Rb24kizOqIUOI1MlEqEU6ZeVOYxBxMWmqecFo3mYR_luCMnQKN7f-FhE6aKaDcmEh0h7EAS68L75zyAq2aV2BWesTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه اصابت موشک‌های بالستیک به پایگاه موفق‌السلطی اردن که گویا منجر به کشته‌شدن دوسرباز آمریکایی و مفقود شدن چندتن دیگه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68479" target="_blank">📅 22:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68478">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیش‌بینی می‌کنم که حملات امشب، از دیشب هم شدیدتر خواهد بود... #hjAly‌</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68478" target="_blank">📅 21:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68477">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">همونطور که پیش‌بینی می‌شد، دامنه حملات امشب گسترده تر از شب های دیگه شده و حتی حملات به یزد هم کشیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68477" target="_blank">📅 21:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68476">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=tUkzL8pZe7zPQetdSyzLoGqTOc3p1Z2f_bVppkBngdUPD1KMX0QJkW6AV6bnsKEE3z1jJ3BNloQl2Nt23mj6os6oR7p93I9StLAJPdwY5CCMsnH6kNvnNpy1ToUoXZvKvY_-zu3JrcOmfpov_J1Z-CbRZhIzZ80syHte99lhZNTA_nsT3_NzH8BO695NtJsNgFo3gnguja12mXZd6JIFjO9pw4wLrN8Ac9BYXprCsoapWCRjWjibbnWXGWgh0kI2wwmTVWoyk6SKJDjFjF-jGUZBxs4LfUAOWeXYkxOxhh_aq5OEB-EPVtkzAg4SmuF6IIYJxsajExusSJG4QQ-Uxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=tUkzL8pZe7zPQetdSyzLoGqTOc3p1Z2f_bVppkBngdUPD1KMX0QJkW6AV6bnsKEE3z1jJ3BNloQl2Nt23mj6os6oR7p93I9StLAJPdwY5CCMsnH6kNvnNpy1ToUoXZvKvY_-zu3JrcOmfpov_J1Z-CbRZhIzZ80syHte99lhZNTA_nsT3_NzH8BO695NtJsNgFo3gnguja12mXZd6JIFjO9pw4wLrN8Ac9BYXprCsoapWCRjWjibbnWXGWgh0kI2wwmTVWoyk6SKJDjFjF-jGUZBxs4LfUAOWeXYkxOxhh_aq5OEB-EPVtkzAg4SmuF6IIYJxsajExusSJG4QQ-Uxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
یادی کنیم از این سکانس که ترامپ چند وقت پیش در تروث‌سوشال پست کرده بود: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68476" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:  در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68475" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68474">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_QQFWn3DikAIygiEMN4v_zyJLLWQCjm-HwmGUCG07hqL3CfoBU9t9iXClQpzzdJ3czEA-rpgx8NBREVdXR405xciOobrlxWneK9AlncrC0EuAOWd05iXVQBJujy4D2CFCAN6nXdu2H_CB4uCu2SLl-h-q69BFNzD0nTXoKGkvmlulsOFT67rxFZ9BLywB1Kze6ab8dN-4FAimI047outYQ8JZfPWGaGw6eDj8pa79uHPtXMP8HNMgeaZ7WYtOLLsvTEXLxHMofktdn35XFrxr_0W2QBQ-AU2_qHfSrV2x2QXB2C40SjBo_FScjMzWmel4fq1TisXbLF8Vhi6kB-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.
همچنین، یک نیروی نظامی دیگر در حال حاضر مفقود است.
چهار نیروی نظامی آمریکایی برای مداوا به بیمارستان‌های اردن منتقل شدند که همگی تاکنون مرخص شده‌اند.
سایر پرسنلی که به دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به محل خدمت خود بازگشته‌اند.
سنتکام به احترام خانواده‌ها، از انتشار اطلاعات تکمیلی — از جمله هویت نظامیان جان‌باخته — تا ۲۴ ساعت پس از اطلاع‌رسانی به بستگان درجه‌یک آن‌ها، خودداری خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68474" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68473">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=ljpUcPDDJQfqDY0JOwAZYqhCZKLpjmSEIUdEnZAaa6ShAdH08OF7y6jXo3V7cbo4xpRjFt21bTYd3uKauXd00KdI6eEUPNc0b4yPi5sHs2fE7_kipPQjhldTjSbXyeKSTLmYYjWDDB6KAEVx5r7Gp71OjydLOByT8lqqQNmYXhPgqTjM7YFrvn6BT6oPVHC6mUGe3oRzL6jqWtt2e5UCFEDB7kHx1BaEy7togbJSZZui4nLYcsnpujTivNH6bASk-mlYU5uNW4k8UWIK1bm3mAuurBjdu74To4DFBBi1DpSQGN15H4B_DWibZGMaye6KWZlAu0jIliNVZggkh9-irg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=ljpUcPDDJQfqDY0JOwAZYqhCZKLpjmSEIUdEnZAaa6ShAdH08OF7y6jXo3V7cbo4xpRjFt21bTYd3uKauXd00KdI6eEUPNc0b4yPi5sHs2fE7_kipPQjhldTjSbXyeKSTLmYYjWDDB6KAEVx5r7Gp71OjydLOByT8lqqQNmYXhPgqTjM7YFrvn6BT6oPVHC6mUGe3oRzL6jqWtt2e5UCFEDB7kHx1BaEy7togbJSZZui4nLYcsnpujTivNH6bASk-mlYU5uNW4k8UWIK1bm3mAuurBjdu74To4DFBBi1DpSQGN15H4B_DWibZGMaye6KWZlAu0jIliNVZggkh9-irg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
اگه حملات آمریکا تا چند روز دیگه ادامه پیدا کنه، وارد مرحله تهاجمی کامل میشیم
اون موقع دیگه فقط جواب حمله رو نمیدیم و حملاتمون گسترده‌تر میشه همه جارو میزنیم
آمریکاس که ریده به مفاد تفاهم‌ نامه و همرو یکی‌یکی زیر پا گذاشته و عملا از تفاهم نامه فقط اسمش باقی موند
آمریکا از جنوب لبنان عقب‌ نشینی نکرد، توی تنگه هرمز مسیر غیرقانونی ایجاد کرد، به حاکمیت ایران احترام نذاشت، به سواحل ایران حمله کرد و اموال ایران رو هم آزاد نکرد
دیگه نه روی کاغذ و نه توی عمل چیزی به اسم تفاهم‌نامه اسلام‌آباد وجود نداره
اگه دوباره مذاکره‌ای شروع بشه، از طرف آمریکاست و اونه که دنبال نوشتن یه تفاهم‌نامه جدید با تغییرات تازه‌ست
اجازه نمیدیم نیروهای دژمن از تنگه هرمز رد شن و وارد خلیج فارس بشن، چون امنیت کشورمون به خطر میوفته
🌅
قبول نداریم آمریکا توی تنگه هرمز، که گلوگاه انرژی جهانه، نقش یا حضور داشته باشه
آمریکایی‌ ها منتظر موج موشک‌ ها و پهپادهای ایران باشن چون ما جواب حرف‌ های ترامپ رو توی میدون میدیم
فعلا سیاست ایران اینه که هر حمله موشکی رو با همون شدت جواب بده
انتقام خون فرمانده شهید و شهدای جنگ رو میگیریم
آمریکا میخواد با محاصره دریایی، مقاومت ایران رو بشکنه
ممکنه دوباره به سایت‌های هسته‌ای حمله کنه یا بعد از اقدام نظامی، ایران رو به مذاکره با شرایط جدید مجبور کنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68473" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68472">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68472" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68471">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=drLYxriB9D28IqGzP53YAgJVszZ8ytJBnTsXP-suP-titF85oCFqNMvmZHQHW7bbMMKbFSsU6NltfYkuHKf_VEJxlvu6eSL2dNIP18KEEFhGQwzv_hcWCnvKg9Vf-roA9IGgmp8RQ3SdkRF6AwU7eZWyzRRMEfsLWFxYSw0Ikkidz3f9UgzuvCeEa9U0H_kGGsbVO64bLlxM3Jt7pqf5cKM52uK3XZd6f_ZqjCOztRo5N_rp4_zG-EAp03vujPw3jbQHryf8QVdaABDjlqBgI6Mosi85brW0h7Q-0xPnqqF12fQCuAu3y1BwRKeYqmgsp-rhmIimcNWenlOsQF4lww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=drLYxriB9D28IqGzP53YAgJVszZ8ytJBnTsXP-suP-titF85oCFqNMvmZHQHW7bbMMKbFSsU6NltfYkuHKf_VEJxlvu6eSL2dNIP18KEEFhGQwzv_hcWCnvKg9Vf-roA9IGgmp8RQ3SdkRF6AwU7eZWyzRRMEfsLWFxYSw0Ikkidz3f9UgzuvCeEa9U0H_kGGsbVO64bLlxM3Jt7pqf5cKM52uK3XZd6f_ZqjCOztRo5N_rp4_zG-EAp03vujPw3jbQHryf8QVdaABDjlqBgI6Mosi85brW0h7Q-0xPnqqF12fQCuAu3y1BwRKeYqmgsp-rhmIimcNWenlOsQF4lww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68471" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68470">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی مبنی بر وقوع حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی، در فاصله حدود ۱۰۰ مایل دریایی به شرق شهر الدقم در کشور عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68470" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68469">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
تفاهم‌نامه بار دیگر ثابت کرد که امضای رئیس‌جمهور ایالات متحده هیچ ارزشی ندارد و هیچ اعتبار ندارد، و مردم ایران درس‌هایی فراموش‌نشدنی برای دشمن آمریکایی دارند.
امروز، "شیطان بزرگ" بار دیگر بدون هیچ پوششی، چهره واقعی خود را آشکار کرد. این تجربه تلخ از جنایات و نقض عهد، مدرکی جدید و قاطع بر دروغگویی، بی‌منطق بودن، عدم شایستگی اعتماد و فریبکاری ایالات متحده است.
اکنون که دشمن آمریکایی در تلاش است تا جنگ را شعله‌ور کند و هزینه‌های گزاف بیشتری را متحمل شود و اعتبار خود را بیشتر از دست بدهد، باید بداند که مردم عزیز ایران و جبهه مقاومت، درس‌هایی فراموش‌نشدنی برای او دارند. در این روزها، شجاعت رزمندگان اسلام و جوانان مناطق جنوبی، نمونه‌هایی از این درس‌ها را نشان داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68469" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68468">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای ساعت ۲۰ پیامی را منتشر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68468" target="_blank">📅 19:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68466">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
هم‌اکنون زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68466" target="_blank">📅 19:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68465">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYg2tTsOMCOveVp327Mk5suy5SpbIkS9_9DNL5GmhEcVGdRYmMtzhX4D8D3GXAysNsNtf0a89OfOw4h8NO7ZQscz0k1eYn3HGiPnPjBKj5TglBjBvEBpJwSJvi6E-ib_7XQVvmAHwpFV4y1CUVGkECsYkLQJDGYUHeIMYTWy4Va8MMvpiKO4XWrMbbFBG_UoIo1R8QjDjdbMk0uTZiKtS1Y2rdVPh44TOcrNLMK8Ig1q9FWpa6hdl-U3xf1f7AJXo3ZSZ1mmguwhh468PvXZI3CAJdqEdYmZpGz_6ZRxIhgjMc8NqqXyV0Sb-bRJ0RjYXAWn0uUagKXSE3vfKUdMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68465" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68464">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68464" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68463">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=lN1oW7CGVXqYaWhuiUrEVWh4-QGGvkuYgmonHHbbJSyzQrgIQFHNDpJcrWwuUOv3KaCr0PmLpTCY_D7xYG2CcOuq-_W6GZCHD-lCWoHTTY7pv5Lq9RVVybL3mF-_tINPfB9vhd-NlvN7VSDrMxfAsCKgaQ1tJchQVeqcFkSIcirc6grYFCoqty6Ctc1MKFfVxCbGsci9nlwhxK968DfwMHb3EaaZY1X_CnYV8AZNKlbv6Tczv-c14zwdY1u6TF_KDBZBos6TMWWP6Hyu7w1pFcQo2nrhrUiWi5Yg0N9gvgGXOmfXbi72CUmdW8L9P4u8CtNId8ArTFmwmi--VxeXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=lN1oW7CGVXqYaWhuiUrEVWh4-QGGvkuYgmonHHbbJSyzQrgIQFHNDpJcrWwuUOv3KaCr0PmLpTCY_D7xYG2CcOuq-_W6GZCHD-lCWoHTTY7pv5Lq9RVVybL3mF-_tINPfB9vhd-NlvN7VSDrMxfAsCKgaQ1tJchQVeqcFkSIcirc6grYFCoqty6Ctc1MKFfVxCbGsci9nlwhxK968DfwMHb3EaaZY1X_CnYV8AZNKlbv6Tczv-c14zwdY1u6TF_KDBZBos6TMWWP6Hyu7w1pFcQo2nrhrUiWi5Yg0N9gvgGXOmfXbi72CUmdW8L9P4u8CtNId8ArTFmwmi--VxeXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این ویدیو کامل نشون میده که تحرکات هواپیماها های ترابری امریکایی از سمت اروپا به خاورمیانه بشدت افزایش داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68463" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68462">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGICV4b2khGB5gpDWx9WLVmhz5QLN1F4FQajbu0Im-pR5B1DKb9f4ekxTjo3aDc1iLYfM7Vq-otW8I9tN1n0D2DXjKd-HlmK5F_oRLkGMEp8WXx4d36haLog6tcyYdazeZF_93wobPX42lB-Mx6aqWzY-IceW06eL0X6B_ylhfC7hvqkKLkGbPRnBoqH1Enai5e-PTN_Fa_faD2DWLNPPBs0ER8R33GNaRuLFhyl3FZYwmP4KWWQZZsjDj24_4q6Z690GCtqsfabQYHQiWF5JF-BqIJjVYLbrtLibSLmS54IhQLwakf_LPkfHQWnzyO0VJi9RLpw8PDHaN1YkohZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68462" target="_blank">📅 18:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68461">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFviXoWFnszEIPa-JQSTpVOUVAeHeNolo7VhgShHxBPA71mxbASCxeb0zVWmGhpyxMty-SAIKeJ8QvwPHBuQJLaGIqzIE6E2s8nYYKylTVaU20VXoSEE5Ik-kgan7-SZt3yp_dQmLPo6XQvpuOs-ZWGODv2RG6w07WAGV42xZKT65nMlsgaS0tf9LakJETL_Bs0vX3Mft3Gmejqm37J1cEfJcAG5TqSpm8npxOlteJ4gb0eOuWjao9mn2M0PF4aQ8jTQsLtNArLxH9q2BkIZvawk7q8m6-NzXfOGCTXOewB9mmw9yvOOga_KB-y0HDAY03B-GDK2qWuWQU3u_Lz5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نماینده مجلس:
بنزین گزان میشود؛لیتری 10 هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68461" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68460">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:  «اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68460" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68459">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:
«اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68459" target="_blank">📅 17:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68456">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=i1xh-t5bJ1Sry95uLnVBk2jSn5bbxY3UE5UNVGzpYNsty5EyZoXkiVEe90ipnw2HOTZC83EvnqWSvV7WrlB8KLr-uJPB-D4QUQmXzyB231xokaooBxOnwvSb3HuolUzBq0LgMxWymuzMpuCEEENAS4BtMkNKVPJmzllpII1JlGSk34dNmttsR-nRwFbRHhCvxaRPn5jaHI7glxqyejROS9R9TZRR4htgSoC02u0GGgA2VXP5CvDl_TBj7At45rdKG2QM3QPf6q3GsJQ8Fn44HBzDWOC_isBJWOeGqWIMFOpmjUwzn8uTcclmAMAwLFF2oJVBOzYiz9vmTHs-XTFJ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=i1xh-t5bJ1Sry95uLnVBk2jSn5bbxY3UE5UNVGzpYNsty5EyZoXkiVEe90ipnw2HOTZC83EvnqWSvV7WrlB8KLr-uJPB-D4QUQmXzyB231xokaooBxOnwvSb3HuolUzBq0LgMxWymuzMpuCEEENAS4BtMkNKVPJmzllpII1JlGSk34dNmttsR-nRwFbRHhCvxaRPn5jaHI7glxqyejROS9R9TZRR4htgSoC02u0GGgA2VXP5CvDl_TBj7At45rdKG2QM3QPf6q3GsJQ8Fn44HBzDWOC_isBJWOeGqWIMFOpmjUwzn8uTcclmAMAwLFF2oJVBOzYiz9vmTHs-XTFJ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی در کویت به دلیل حملات موشکی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68456" target="_blank">📅 17:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68455">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwxjqfgIsUhHnVeqRX_kCHSIyix9WwdrNDl48Hba8pBoC7J5EtBWfrQtQIH4reyelM5yOPmky0Q8-Lk8ttDXbCs2P9RVjboKsfkbQfkIGY6QgnqsJupL-ioKsf32amQ13gRgmQF4EISxVPAzfTl94O1QLyQ-FdvWsGuMXN2TCZbkdoqjIUQ0UbL9JYhiQeJPFL4U5klDm7vZYY0KXXIHJmJ5dgmRw4fV7HG8eHew9mNTi0c9NXt-Gm1Xlo8jwQgwm4h2xJKlhFDhAdacmrXIiL_-s2o9fW90Aaa5q2DZKzl0KmlmiltSwwsHLAdcUGvZ9tjXSHY8lz-W3n-uUcdYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛معاون وزیر امور خارجه جمهوری اسلامی، کاظم غریب‌آبادی:
«از این لحظه به بعد، ایران اجرای تمامی تعهدات خود را بر اساس یادداشت تفاهم، به حالت تعلیق در می‌آورد.»
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68455" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68452">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00f574479.mp4?token=RkQe5-_QWj-a8uUqOAGqh_04nFsUGOJoVQfyTlGen3szkhE6pQne1OEbNf-CPuKKKZDshQdPGG_EYLbp0s-V_c3TUhVQyFN3vBIr_NOlDE_RKAMsOvvYcDSjoFYroBc2EARIMD0VkRFQCoEijjChbyQvi5FNhR7bQuawZg7u_wnEsyzmODvl9s17UkLFBLTHa633nrKMz2Qp7KQJPgPD0eUBk3ptJEcLTPdicAxtivW7aTJ0RqDe5Y77I-nuq6l-k-DAcmb5YhmoQGArbnKf5ZG6HWbSXk1TcL2zqGPBFNaIaqh0fZilv7AnYQtgZvNpLRpUV9kESVq-WT8uZe6V-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00f574479.mp4?token=RkQe5-_QWj-a8uUqOAGqh_04nFsUGOJoVQfyTlGen3szkhE6pQne1OEbNf-CPuKKKZDshQdPGG_EYLbp0s-V_c3TUhVQyFN3vBIr_NOlDE_RKAMsOvvYcDSjoFYroBc2EARIMD0VkRFQCoEijjChbyQvi5FNhR7bQuawZg7u_wnEsyzmODvl9s17UkLFBLTHa633nrKMz2Qp7KQJPgPD0eUBk3ptJEcLTPdicAxtivW7aTJ0RqDe5Y77I-nuq6l-k-DAcmb5YhmoQGArbnKf5ZG6HWbSXk1TcL2zqGPBFNaIaqh0fZilv7AnYQtgZvNpLRpUV9kESVq-WT8uZe6V-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
چند روز پیش یه ویدئو از یه پسر نوجوون وایرال شد که از سرکار اومده بود و داشت موتورهای یه نمایشگاه رو با بغض نگاه میکرد و حسرت می‌خورد؛
⏺
این ویدیو خیلی دست به دست شد و نهایتا مردمِ نازنین ایران، تو کمتر از یک هفته پول جمع کردن و واسه آقا یاسین موتور خریدن و اینجوری سورپرایزش کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68452" target="_blank">📅 16:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68451">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون جنوبی:
همه دارن از جنوب صحبت میکنن که دمشون گرم ولی منی که خودم جنوبم نمیدونم چی بگم.
درمورد پمپ بنزینی که یکساعته داخلشم صحبت کنیم یا مثلا درمورد برقی که الان رفته و نمیتونم برم خونه صحبت کنم
درمورد ماشینی که نمیتونم خرجش کنم صحبت کنم؟
درمورد وسیله ای که میخواستم بخرم و امروز صاحابش 40 میلیون گذاشت روش صحبت کنم؟
یعنی حتی نمیدونم از کجا شروع کنم
ببین قبلا به موجودی کار نگاه میکنم میگم خب بعدا این چنین میشه اما الان تخمم نیست
الان میگم بتخمم ک میزنن نهایتش اینه منو میزنه و میمیرم
چرا برق بقیه شهر های دنیا نمیره برق ما میره ؟ ما اضافه ایم ؟
بدترین اب و هوا و اکوسیستم و بی برقی و جنگ مال ماست نمیدونم از چی باید بگم
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68451" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68450">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiyPh-2uhi6phih_la730_uLwBUG1M0O0ZT5YQzMdwgLVVKnHBg8eyENG2t-LE48uz5X8cXVXvBBDtQ0AuxG1aDIw3DB_grlLWF2Yqo0b4chKS9YNu-X93LwJPPxOwRrCmKEr6J0Nxtm4zqPiVz9HxVLgxs4bLj3XtPmfRyiUgRveOFdcQyIlWjvZm4CA2d8tWf4Q2aMzBmzc2E_5noEZ6Sb4MnNZ_InkpP5dNxYG6AHONhoxWfQceEjveOFMLMOzrkokX45TTQW93_8Nuojs4F-M_3DrKulfGycEfIBFPj0JqYa3t1i2r1Msh1kNu7vBmGhaxZvlZou2ixY2lEKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حکومت داره به جانفداها زنگ میزنه که بیان آموزش با اسلحه ببینن و برای جنگ آماده بشن
😂
😂
اگه کسیم بهونه بیاره که مثلاً مشکل دارم و نمیتونم بیام، میگن اشکال نداره، بیا آشپزی کن یا کارای دیگه انجام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68450" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68449">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=XswxFJPaZtbcXYfwKWjMhKX0hMRS8FrhMV2QHU76XZ95yAnJm0HVaXjtccoNFffCRp_eWBg2GWcK_-PbNBvzMbkFh_6-D627_DGHJ9nQUvOdV_gAGesd_CYUFr430FcCc1uwt9RxMA-2ZTfcqgHncWuPllpteQD8jYkiFUm_9Faj_cPCw8UFN_bn3UanYCHC5ctBoSk39Llsv6PXWbZlz9rCwgFHXEMjb04WLe8owJI9BG0hkegbOFxj12zgb6-U049LtjNnhp-vtGSMDp8_ZhGhmvWvmtzUCj9lqx0VLECcXpSmEJWg3GPQoFpoSVFQMOa8b9CHU5p5cKzgG3AcwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=XswxFJPaZtbcXYfwKWjMhKX0hMRS8FrhMV2QHU76XZ95yAnJm0HVaXjtccoNFffCRp_eWBg2GWcK_-PbNBvzMbkFh_6-D627_DGHJ9nQUvOdV_gAGesd_CYUFr430FcCc1uwt9RxMA-2ZTfcqgHncWuPllpteQD8jYkiFUm_9Faj_cPCw8UFN_bn3UanYCHC5ctBoSk39Llsv6PXWbZlz9rCwgFHXEMjb04WLe8owJI9BG0hkegbOFxj12zgb6-U049LtjNnhp-vtGSMDp8_ZhGhmvWvmtzUCj9lqx0VLECcXpSmEJWg3GPQoFpoSVFQMOa8b9CHU5p5cKzgG3AcwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واسه دومین بار طی دو روز گذشته، جمهوری اسلامی به نیروگاه برق و تأسیسات آب‌شیرین‌کن تو کویت حمله کرد و باعث آتش‌سوزی شد.
کویت حدود 90 درصد آب آشامیدنیش رو از طریق آب‌شیرین‌کن‌ها تأمین میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68449" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68448">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOVwd7AUOvlZNMn0JYQyqb5hUygJ0G3TnNTGhVpLXYC4w_6s7oArOhrpIl2QVAkMQlyXKVMZyz6ftU8RmoFMYb6l3fZ8C8kTu2FaASvVO6MNXa5sTNJLzpwrnccdX7PItNa6AL-0sX4pYFFrIOOYX5SsTb2ZX7t68D35C0RFaLnEFyqQujYWdtCU6HzmpN0NhtCsSnYbm47qrkBMgL1FtJuJCzFYDObEouEC_xfvor1INTAYlRU0XsQjTwHpyxCGLQV7g40lZ71pkhQDWkHutpQDg4R-0jA7W6OOZxq1FocnDlJUo68C8c-8qUTxe6oQgvoXiilF8viq2sh2dfzZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68448" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68447">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68447" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68446">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=B6lVAeaAA6i3xS41NPVbP7YjxPfM2CjZ964BhG9o7RLk0gDBsHbcZ4FWBXVHjagsaDIkn5TGbMMoATW_lZO1mO6nq4iLuivgFkDQeUKA_6Ji_oFdnkYpdeic9evH5HGpgCEM94qKbCF9tQQ-GddoShuFDKTiUCIaC7pJTwHWz_DQigezQXfQyip1LIkb4PeSZVCRjbwqMXQ4FqEY-36x4T5NKJM7q2JkZqaQ9wIlAehO1RJzJbqefNfrcmfvDUtzLbIzaw4yGmMv9MLLllBZMNpGAljIevEAcmfV3DLiP7r4sUyCCUErxRC_Y3OSwiCbkneGsteSRz14zDM53mUIcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=B6lVAeaAA6i3xS41NPVbP7YjxPfM2CjZ964BhG9o7RLk0gDBsHbcZ4FWBXVHjagsaDIkn5TGbMMoATW_lZO1mO6nq4iLuivgFkDQeUKA_6Ji_oFdnkYpdeic9evH5HGpgCEM94qKbCF9tQQ-GddoShuFDKTiUCIaC7pJTwHWz_DQigezQXfQyip1LIkb4PeSZVCRjbwqMXQ4FqEY-36x4T5NKJM7q2JkZqaQ9wIlAehO1RJzJbqefNfrcmfvDUtzLbIzaw4yGmMv9MLLllBZMNpGAljIevEAcmfV3DLiP7r4sUyCCUErxRC_Y3OSwiCbkneGsteSRz14zDM53mUIcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68446" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68445">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⏺
وزارت نفت کویت:
خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68445" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68443">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=ErDGgnr6lYz9XtbzCx2pP6keCYMMCFFLsBWbU4b5SiUEDaLOhnTY8FeaiJMzwjihzRMKVMJOTjfjcLxRjsI4bkVYwYRA7iNyLKQFGTJ7GgDHl5FpET_CLbtckO6u63dRQdw6Sa63NAdShq52BQsR4xGxw9iD4AvAqh7BrGwpqMF3vRRX3LD7Z7CVh2EX_cjagxhCMDsGjeKULgQ9jzcVKdkdWuTjDsIRajZ3TqaMp5pnBWRE30Q3YtHyFdbvmWa9r40_GTKlNLXOCzINUhJ-wwIYvnuuMSE_1dDLhPbDiCv-kuLTQBNZ_sMNXLuR6e4I0g2-857TIBRNTirZP1OorA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=ErDGgnr6lYz9XtbzCx2pP6keCYMMCFFLsBWbU4b5SiUEDaLOhnTY8FeaiJMzwjihzRMKVMJOTjfjcLxRjsI4bkVYwYRA7iNyLKQFGTJ7GgDHl5FpET_CLbtckO6u63dRQdw6Sa63NAdShq52BQsR4xGxw9iD4AvAqh7BrGwpqMF3vRRX3LD7Z7CVh2EX_cjagxhCMDsGjeKULgQ9jzcVKdkdWuTjDsIRajZ3TqaMp5pnBWRE30Q3YtHyFdbvmWa9r40_GTKlNLXOCzINUhJ-wwIYvnuuMSE_1dDLhPbDiCv-kuLTQBNZ_sMNXLuR6e4I0g2-857TIBRNTirZP1OorA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موج جدید حملات موشکی و پهبادی سپاه پاسداران به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68443" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68442">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=fTFKW7MEsHYCxByIc6OHl5ptzduPSs--5WkN0lq_i0OHUIiJMl9zbOHLy_2puBWuyradu7k0tXrqxLXC_b_j_r4ECQZeNIdc2RHP15GV23VtZh7-2b83AF1V-rJ5xB2zLzVDfaNI4jMjhBb20R4OAKBpLrV82lQDdibb7Cjclfj747g1v7grGYj6YacPEWaZYtd3V9hj7D1frkf3l6AlVGn3doNoR4HDDAqJW4sbvzltNDi9-qwYHZxPNCvP3qUikYwVXYUsYfBofeICeFfaSZdY_3fFkeowZO992xbwnmmNCr8priW0gLIBCgfbAcUwB7-3CIodsv0m9ybOIy1fvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=fTFKW7MEsHYCxByIc6OHl5ptzduPSs--5WkN0lq_i0OHUIiJMl9zbOHLy_2puBWuyradu7k0tXrqxLXC_b_j_r4ECQZeNIdc2RHP15GV23VtZh7-2b83AF1V-rJ5xB2zLzVDfaNI4jMjhBb20R4OAKBpLrV82lQDdibb7Cjclfj747g1v7grGYj6YacPEWaZYtd3V9hj7D1frkf3l6AlVGn3doNoR4HDDAqJW4sbvzltNDi9-qwYHZxPNCvP3qUikYwVXYUsYfBofeICeFfaSZdY_3fFkeowZO992xbwnmmNCr8priW0gLIBCgfbAcUwB7-3CIodsv0m9ybOIy1fvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپهبد خلبان نادر جهانبانی؛ میخواهم شاهد پرواز گلوله ها باشم
🫡
نادر جهانبانی (۲۷ فروردین ۱۳۰۷ – ۲۲ اسفند ۱۳۵۷) سپهبد خلبان نیروی هوایی شاهنشاهی ایران و معاون فرماندهی معروف به ژنرال چشم‌آبی بود.
وی بنیان‌گذار و سرپرست تیم آکروجت تاج طلایی است. از او به عنوان یکی از بهترین و برجسته‌ترین خلبانان عصر خود نام می‌برند.
نادر جهانبانی دانش‌آموختهٔ دانشگاه خلبانی نیروی هوایی روسیه و آموزش‌دیدهٔ دوره‌های خلبانی جنگنده‌های جت از آلمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68442" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68438">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=AtdAKzY2vUr9TjduuAQ48Menq9ijiCSiqa368N_xb88pMnd-CFWMuNjmyFA7zH-z_wqDnJuyDyT0iwgRrkw1dsH0cB_IVaT21vSh5qWWjS2eWU0meKZYp0xFC10hNA_CGNrZ8-n-Lx0nJhDNyI887UqIj-p1wDcfiU4X3e7Tvga5kjCpUK1SIc6kcceOE9FnsyBoSJM910-TkH1641Fy7RG8rPGZWayj_hwQOhLHxz0LdT8bHn7aeKDnjYRtmoGe0qgIgqj2eT7m4zTvSm0UbXImDCQTtYJj0ldGRIx3y_ljZSItjXdzfUq49AtAazBLfGDtY4VkCbjwKQQ0qyThvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=AtdAKzY2vUr9TjduuAQ48Menq9ijiCSiqa368N_xb88pMnd-CFWMuNjmyFA7zH-z_wqDnJuyDyT0iwgRrkw1dsH0cB_IVaT21vSh5qWWjS2eWU0meKZYp0xFC10hNA_CGNrZ8-n-Lx0nJhDNyI887UqIj-p1wDcfiU4X3e7Tvga5kjCpUK1SIc6kcceOE9FnsyBoSJM910-TkH1641Fy7RG8rPGZWayj_hwQOhLHxz0LdT8bHn7aeKDnjYRtmoGe0qgIgqj2eT7m4zTvSm0UbXImDCQTtYJj0ldGRIx3y_ljZSItjXdzfUq49AtAazBLfGDtY4VkCbjwKQQ0qyThvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
🇷🇺
حجم آتش‌سوزی در مسکو پایتخت روسیه بعد از حملات پهبادی اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68438" target="_blank">📅 13:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68437">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=gcH0G0fbnm0iy2xwhOg_nrAjFtGbMSqyxBLgISxdPTGMf0NPTaRz7msKWSCqrj-gKop1urnr10XVv4LoSTSJFbWSAJ4lHRrigr-ZU9pmMnIl4v9_irvY47c8_x38aa5O3M808MeB87jm6w_ki8-uqPstj7J_rjXph-MG0UsI_hjrUjyvo00EhhKDldcYVpND7e_UaYoD4RpKl0hoF-fsZdCHWEZ5PYbJKIg_JrAiNRWtW_pd9IjPWBr6abyYvW2N1qRTbhIBH2YSrTTkqUYpaJi-PvA7NR5SxRwFvlMRMxcE--yttPrFVwZ8fvgERIisQwxkf7gZd3Ore9rS8wAdTCQ-KsgHCGhEG1-lbfgsWCsCxJ9DTHY1OXTHr1MwT5ZGYSxQC-zKl7eMh3E9KDPNUbFHvFfHKqsmzACeGWPtz_uDH_bQj8W-zcYNsChC4oNWurOTrmMd6uhNgrg95aREb2nvLrN4LQHr0VxYeA2MV_Edh5LTl17KWTiIwNzjE7S-N_D6qoINKg4yAghWznQhqCEvIjr8iU171slSBGr4P8-9zYamZ74IP7b9IzjzAsCEEYkXnW_w02EizpcGTguDBKN-bqhwhapOa5ST2zQDQZwvv5snnuZ4oZOW1g9SeOzypMiTiQ8WQqtcUgktOqz6T0v7m4766phEarAxP5imo5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=gcH0G0fbnm0iy2xwhOg_nrAjFtGbMSqyxBLgISxdPTGMf0NPTaRz7msKWSCqrj-gKop1urnr10XVv4LoSTSJFbWSAJ4lHRrigr-ZU9pmMnIl4v9_irvY47c8_x38aa5O3M808MeB87jm6w_ki8-uqPstj7J_rjXph-MG0UsI_hjrUjyvo00EhhKDldcYVpND7e_UaYoD4RpKl0hoF-fsZdCHWEZ5PYbJKIg_JrAiNRWtW_pd9IjPWBr6abyYvW2N1qRTbhIBH2YSrTTkqUYpaJi-PvA7NR5SxRwFvlMRMxcE--yttPrFVwZ8fvgERIisQwxkf7gZd3Ore9rS8wAdTCQ-KsgHCGhEG1-lbfgsWCsCxJ9DTHY1OXTHr1MwT5ZGYSxQC-zKl7eMh3E9KDPNUbFHvFfHKqsmzACeGWPtz_uDH_bQj8W-zcYNsChC4oNWurOTrmMd6uhNgrg95aREb2nvLrN4LQHr0VxYeA2MV_Edh5LTl17KWTiIwNzjE7S-N_D6qoINKg4yAghWznQhqCEvIjr8iU171slSBGr4P8-9zYamZ74IP7b9IzjzAsCEEYkXnW_w02EizpcGTguDBKN-bqhwhapOa5ST2zQDQZwvv5snnuZ4oZOW1g9SeOzypMiTiQ8WQqtcUgktOqz6T0v7m4766phEarAxP5imo5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حاضری به عنوان یه جان‌فدا، بخاطر مملکتت، بخاطرآب و خاکت بری بجنگی و از مملکتت دفاع کنی؟
🇮🇷
جان‌فدا : آره، من بخاطر مملکتم جان میدم.
🎙
خب الان بیاین امضا و اثر انگشت بزنیم که بریم خط مقدم جنگ.
🇮🇷
جان‌فدا : من بخاطر مملکتم جان میدم، ولی الان کار دارم، شما برید من بعداً میام.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68437" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68427">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dRPWWvCyfmbCzK1oPmUy-1Pmmq4GEhZk0sjbSn8ulMa9UisrrUkC-9S8yHHIHHmfi0lfs0pmGsI05zZGO9tauYm0oz7or7fxgYlbwZmBqk--I-ndvdY3HVqoG65d50nx1ghcUwjTdB0DNyS0HcrjAHALT1qnjfdIMqPoKbl542p_d67lS8wLrSOVzyDa_5a4rtZBcxMfwhslKb67HE9LcPhS6M2zuG7WDj2vYU597j79p_nTLyHZ0R9yZsoEjn4R0FB2M6Y7JYyT4XVSw-C3l11659nNgUNu6wMFnB1SdoxozpF8kAX5ZCNyqInsEKPv4JumFgDafO7mEB-aQfeAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPa1NSoLi-kv4tZPgkmgnAcTah9grXUWYVnMK68jlvf0MMfEobKaWZl8SA0e1H6yuRwaikJU3m2mSHwSYyR-pjZZfdv8FLV-ecx3dBJ9Z9aZy4vMi3xSXj6_cHpDb3md64tAH8Np33xM_8t_4FL0BhQi7kZGp4x_LmKS1K4_U88zb5EA1Oa8RKnVmKRDvvJYZbLFNEDHQExwfdNheUKMcaAgNWXSw0X8Su7TyKtvz3mFBPbgiyY8WRZMf4jgC8RiGTSSGUK54tylLJdBrSANWvBjg64zM6jNpEOQWJJBIFQ7VV4DYI7c1Ggx1o-hDm-lUnTc3dsxp-TN5NVLG-aMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2-wzinmciRhKhFcYzHIvYpf3C9RXnWFKOT0k1KcEEV0t1hr05_6lbgTEvfi2Qaa5Kp1bUXjRuHw1pZufR4VSECvNMTRdilpsfAvYZHCCu5uHpX7YcYYWrNdTHBSxfRN87aXYf08DXrl9OdMnVXUaB0rSgnwj4eE-EyPUa5V0PGWuBHx4DD2KeN8v4oBYxYCbinRnea-K3sLjaySg-Tb7XYB-5HVFgDVg9VBlhxFZ9MA8yLxtHpkBt13g0n_cE95bBxLaPEfTv8RIaIWiWokPEtu0ZnikOb3DK1DoJaCt7tEfNtYwBQ9-4TF5E5L0TpIWlLoocwzkovO8P3m0yyyIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIZqZfXPZg3pX2GBeI0VU9uGDCxITFrDuCZkXO2NAvoQ8BSYH-EC3pYHPWBAYdGgoDYbqM8sIRHBQ5qL-r3Nswq6PIbmD1Uj6Uo0_FQ-JlP-GZai-jh0cUCCo439f-7Qgw7XuItn-1G3atxi2azAGR0Gi64bHweHUvbff7U6U9ol41r5VJhjzb4zMpXi9jQvbHKxgtoekuwz2EKz7PvIzvQU9Lp9A_BYIw2oQVZgadOkpeQPTzfStxKMT5YMPCYoMPV0UHc18uBqWjLyxHolHjVorq5bUJjqSb1wTzTZ5PcfzpYGMg15daGYSyBFPEOAOGJvS6mTbvb67W5ScmWUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3Q6Ja-sU8U1xI7yNFGrqdlMOiYsqEa7J_A93PXe31hicC28IiCDHJVdEqj-1LHz4FoltKgy2Y_Gp7HF_8TgSsLwtVZ9qEsiZOcghDgtAlEB0XMlfMQUQYv_dFWNkZXC1Gc9qRcWwynf2HWke7cTw7tesN7OzJwOna-X-UsM5sAh0mEFyxvlsUnwtYCgH6noi_ywqqHFXVga7BDylHuvbTnPk3flRNPGcBkWu95H_770SwPFsPdbvDCfKITq9fL9F2IpbeMZfFvjf7VYit5ZSovuRBMH-6wsRNooqYERwPHl7lrMYdv8UVqVfEKS3DlOP7R1haj6IEZ7eBqTkRm_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqZdCVI6qFm_6H4ytiP-9flatCUbshRCE6UCfB9zthBgphSa8_zYDKa8lAOuTvoKLxpbeFI1RXgN4RE3lt_eMquSMgc8IT_sCL3OJ19ZW1OdkO6ZqhAB753RvVvY8BQj7jimtbGnfXnQ6Im1bECZiczQYMSN7WnXjxaMBQbnRfkStyqfz3BsWbqf6XM1RXxR1PDTDFBstwRiMcyZidLJd-5Tb7qr7WvaEH4zbJ3Ak1_xFBY3GJIOLKcasOszaWeZxSLdS3E4Ix4A7BatH7UwwdAF5-t10k_o16txBCjQr_DcTpyUAxjIcITuWRhTRGSCCLijOyFd4NvRHmJ18Wf-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bivs2zaOe_ia9mZx5jGTn6hPVjBQq_-cfzjS8a80x5GLs9CrB6CoyCQ29gcjgqCY1e6Kk6ExmbD6ouXqZLZpExf17_Khhcll_IsM_7RD9TKn46eizt5KJ2CyWdlWX52v1m-oy3R14iroH4WYG8qaNFRQz4rCV7hlY6E9-b3ojXygChe5vgcKlQeCbrayudwYKRSyud73Et9ZQSEgwEbXNT7ldCDRPgsmTkhIuT3yNut8l0kf-gtgWti9t6cXUvhKCxyjEto1GbS9eMxBiSoglCd-1tAKW6RE1hEOj-kv9ThR4ZMU_TFtAz6ZOhWGP74Hh6hvmh2SAh6KFcIi1mJNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJ1zOM0CiuZGLeXw9_RXQ5uMUtDhXhvSid6fJa427Q6jX0zdE-U5c_TK0eRlOAVwSxSruS5M0fxhZpCrkua3RPMfRUJdTOJb2YZFIYMXMswxgvHjpx5Ijm0dxTXP9_mhf1uZfav97GO9aCak3d-f69iU-g7KKBA7dFb_qCWyZSnlYE5KrEpxMVl5-lyACcdcXZoHHJxsBe74uIFJdgc_e6o0LX0aBWXoHtGxySFLNy2X5EJRXsuvBkMP9kg2m5Dq30HRSrZpoiNgigNgP95xSPojAy2dO7JnMVoP4XVKVEyI-enjXmLwYumu2atYXbU3KvZUyXgIJ249EBaUOeZ4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZHterhzMQJfK-rBBEThUqfz6h5UrPLy21V5nsu9YpjqjLgZTKseh77hV-s_YPEEyCtE6BgDPgovZDU5XBoukF_6C8nT_5szb8iP4VUmym3KxavJXnuhe2lvh-baW5USgfsqWuqvfm2Nl3d4czKuDD9spaZyeGWcOLWDx2eUy_LfHE7y3sOIcRHVvZNK42i01Y6outqwVL9WGKztxH0xpv3OkRMkqO1sKXXgSf_haG6GbBQx75LnhfhWrJi9-no9UsJM4MDfBJohnJHlj8ClVum2kapEfRPzMEIE4QAJCnyZinXmzguBrJRtYqBP3_uc6jK3vNcDE-38iKJ0ZPPRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ct1d2XsdOz5GxXBmFLvBErsGKhDm_e2cc99q4RU3wzJATWU7S9jwYaJkLaYNV9D4pkFuhGwmdz0vn708AQk_kcH-_LrPpKlnloZeMFg8lwPYbOBC5gZGhHIkXSlUZHyzVfVee7BI2aVMgM9a3tMGZP_2vKuInfB_YBlB6PLTK-TlXzwE2T-DFjcoHshyZLbfs-LxHF0IlXuonlttFonmYh1Ob4UrV1296c02fz1D8POxl5Zrc_b4-oBMkU1zgS0vCMal5sHMqZpc9IOxBEOPTg-569YJIqRB2MXHCv1xJ_hLTijpGgTwQ8mEK0gP0j1dALgJhccjRVbBkYtO3_-EwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آب‌شیرین‌كن  بونجی جاسك تخریب شده
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68427" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68426">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=ZB-qF5TSvzUX3jZk1SZhUpUKppn8HV69WQ3eV81KD-wULcSX3DowejWsnFLQpr03D1fycYpT-b2B_L-e41SRrkT3ZbEDiS5o584jiX1fEKw0OUnD9tf17cyQI-HkKNEv0VoOx1PKFrmHFa7Q_Z84Mmesx26VkFKQC_W9BIEYnIHr8O7PRNcyl9b69TwrmjOZki7qjWSyKEM4kNfCzUFFHJbATnb7l1K024nBcKRd1-3f347WkbhJr_P5VSQZlDqEJlo8Jn-skoOqCrJOlcCpQ--ErdORcP4yqWCr4ynnD0_ye-nkF849dmbL1UwIQMtNdYQ4jRfUss09kbhUxRs6rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=ZB-qF5TSvzUX3jZk1SZhUpUKppn8HV69WQ3eV81KD-wULcSX3DowejWsnFLQpr03D1fycYpT-b2B_L-e41SRrkT3ZbEDiS5o584jiX1fEKw0OUnD9tf17cyQI-HkKNEv0VoOx1PKFrmHFa7Q_Z84Mmesx26VkFKQC_W9BIEYnIHr8O7PRNcyl9b69TwrmjOZki7qjWSyKEM4kNfCzUFFHJbATnb7l1K024nBcKRd1-3f347WkbhJr_P5VSQZlDqEJlo8Jn-skoOqCrJOlcCpQ--ErdORcP4yqWCr4ynnD0_ye-nkF849dmbL1UwIQMtNdYQ4jRfUss09kbhUxRs6rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تونل گلوگاه، در حملات شب گذشته آمریکا آسیب جدی دید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68426" target="_blank">📅 11:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68425">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68425" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_meBgEf-q8igE4w0CStwD647qY_eB0LIsoNNh2DzAi8k02obQsyf8l3GyYLHs5aU02LQIVT90-5OUfLp9m-0o8EQhshZYqQjvNq6gR8rF8401EVOjlMQKdJsfshHzOVIBtMHOzH4GgleY1Yz80CHiWpgmMW2vBuh5zXF7IG-HBs2JpQVXG346cpHr7X8tbm7g6ZbuOTl8yU95mZlEKplnBubTeBwu3exAVisviIe8k-ptlFgRujnb-ym9J_AOIgV2idUdx231dkvA_ppgiicSa2XFM6XeK6z2cBkWeS8vlR0mxCSljJ0M2u7v3HDME8zcb9Sni1j4BuyqciAPeftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است که دو نفت‌کش در تنگه هرمز، پس از برخورد با مین در این آبراه بین‌المللی، منفجر شده‌اند.
✔️
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران، نادرست است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68424" target="_blank">📅 10:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=jBS9zu3YNr3ZKrWmd98Ox2T4jh9xpr5dHW7tCoM35tJLXVq_T5Dm5kP3y-VqcEFk7TUudJTf3GLwbR0jdXcw-j49YLgEXeOgm4TsTizzNNS-GIYu31FDJSGWE-nLfcaNpVnzpBCEQAbtIbcGJKzpzfMpP64BA-ltdZB4zF09SN-u0HBkRr5EpbWwPOV-sZvFyI-bmbnBsG3tQWm6FVn18KC16J6CPykczc_Pdqb7FP2ipuBxRTLSjYCRixxCFZErkJuXsqpWWePAli29y4BJ8xBuqGolMUAt865oa4YM87W5gEho2nNbH6askuyFSkoyuqOJceEdwcqEeD28S5DL-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=jBS9zu3YNr3ZKrWmd98Ox2T4jh9xpr5dHW7tCoM35tJLXVq_T5Dm5kP3y-VqcEFk7TUudJTf3GLwbR0jdXcw-j49YLgEXeOgm4TsTizzNNS-GIYu31FDJSGWE-nLfcaNpVnzpBCEQAbtIbcGJKzpzfMpP64BA-ltdZB4zF09SN-u0HBkRr5EpbWwPOV-sZvFyI-bmbnBsG3tQWm6FVn18KC16J6CPykczc_Pdqb7FP2ipuBxRTLSjYCRixxCFZErkJuXsqpWWePAli29y4BJ8xBuqGolMUAt865oa4YM87W5gEho2nNbH6askuyFSkoyuqOJceEdwcqEeD28S5DL-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68423" target="_blank">📅 10:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veau8sx14BDbj8C-u6ekX_S9GYyjwktcco0KwdutL7gdhJGx4wLVwWH_aHmhK58BBAwImQezgYKgGNFdN7QduXYOkh9RCqSg5PAZPnKHYuuCP9vEsEc1uup5A06n2D62ySwe9zbhoyDIqzuZPsvkDB-Ep4eHrN0L1fqQcfMjUV6Dysqmpr9YZAIcyNPL-_S9_g4YG92uYANFSM70GD0qTM2x9MGXph66Lz5ZZHgiHZMTkvlzpk7-PiWkgt7cLgrfwbvO0olG7WEj_5kXFaF7GNkVWYnroZirD3Hftp80Ef8KvyUwoFth0wFa3a2ejKmCX6AVIU6FuhadO5D2myAD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اکسیوس:سه مقام آمریکایی و اسرائیلی اعلام کردند که دولت ترامپ به اسرائیل اطلاع داده است که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند هواپیمای سوخت‌رسان دیگر به این کشور اعزام می‌کند.
پس از آنکه روز سه‌شنبه چندین طرح نظامی جدید در جلسه «اتاق وضعیت» (Situation Room) به رئیس‌جمهور ترامپ ارائه شد، او در حال بررسی یک عملیات تهاجمی گسترده علیه ایران است؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
از جمله گزینه‌های در دست بررسی می‌توان به:
⏺
بمباران تأسیسات زیرساختی ایران مانند نیروگاه‌های برق،
⏺
انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف مدفون کردن عمیق‌تر اورانیوم غنی‌شده این کشور، و بمباران تأسیسات زیرزمینی «کوه پیک‌اکس» (Pickaxe Mountain) اشاره کرد که گمان می‌رود مرکزی در حال ساخت باشد.
ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد مایل است با تشدید درگیری و وارد کردن خساراتی سنگین، حکومت ایران را وادار به بازگشایی تنگه هرمز و پذیرش شرایط هسته‌ای ترامپ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68422" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsI7TLThlQOo5qhQ1axgQCNtFDlnjeeFtRtJwul91Z2k7nr1cCZeScKm_YOd3fsPjTLujJ1TXH0vgi00wKyG9ZgN8F3cAWPM7GaqWAphkyK1DG1T3KQfXhfOv5tAPkRNpMVoBZTfQ5RwfRBSv3CBe82v_w6daTxlbug182WvILw81EQogUmWYxExDA8jHJC-6qVPpiEGNuHjlCdzn3b1mlfYtG-E7baZu32hE26iUpIF9dn-dBkxTEqR7vhbUcH83cPqQpK2qh8pYVvOI7xtecZ4AyS4bRrkQQeSk61GDhJVgNTwzC62d-zEJpOmT51ZQstV8N9t7GDcfsfEoNii8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvxGKKvluEB-NLt5caWeJYw7EAzgU1n7sX0sAZoBnCfEPQGCcPpSmznDpEgRBYn1JgyJdBJFhnLZvi4Jy_9mfBg09llFbp4957USPsAN_JghCLEjn7hIMOb_dSxvQysxXKbrltCRSgYpDLUYT91Pbg0Pn_PcPDoNSirWKybaENv-SQHs9MXEVNsBKNFv7mS9wqhS-njZ38IsXjlWpKZRscU1ARGKETzWNPMsyMKL6IY1zP74rdHdwv2BOU3r3ff10BaSTi2oXjmqgJ0smc-dRWRwVYq9YK5AQsF9fs_vR-wP6xIMupSr346rNrrQONg6L9lUJNY_iY0jB1vo2hzsRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgVdKFmeMqEvUiVCy6-ONZceCvTUugFqgu4N-AQZhE76DL2bF6zlkh4dJeoYzNYCLAzuKYtDKLCextIaTJmUh9HJZx9FkzFLbVrs9um71HUoHG4W5ddpM817CEWGN_zWNYZt1oKxWrD-x3wxXhKiQ1J1jP82RWLZM18pGlhQ1yA-2ED6e7bEbYAb-MWAieWKS7vq6f6ihASsfeW5WzhuEHt08s2lxAgh7mbBYr7h1jKvrXAfcBqfpqoxsQGxdEsKShvgKCFBTIrc021sh7HyLeHT3JEaeyqD-AecD--M01Z02righDN2EjEp2YH-WXUpgmbU-HdTvLspZzT-GZ5X3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=lUl8qVyyxva0VYNgXkaAL_2nC1zCGZbmwnnmnuaBjUKkL3iZThJ64l2vMGhHJdAsaA2oLvxqQ-XNQkdmi6GFM6Zl27q4ShDw_ByAJFktA5IsYwrUBh5arFZPn9yt5HOBbPVRXLLbi_rhDurXUwtR2GDc2DjLhAiIyUZVqJPlRcBlhDsnv4mCFhvufsqLyJGO5e125_g0M5E4g285-rokUTb9aqSAILsHb8Ryxn89xJMwroARe4AmoYRGrb7CTZlWjzgHAenk4EgbBaFfG60c0xBol66V-vVgJKXKQEXydQT-VETa21DF1Qj3FWh9r5FNdRl1FYSafSJvq7JoycNLAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=lUl8qVyyxva0VYNgXkaAL_2nC1zCGZbmwnnmnuaBjUKkL3iZThJ64l2vMGhHJdAsaA2oLvxqQ-XNQkdmi6GFM6Zl27q4ShDw_ByAJFktA5IsYwrUBh5arFZPn9yt5HOBbPVRXLLbi_rhDurXUwtR2GDc2DjLhAiIyUZVqJPlRcBlhDsnv4mCFhvufsqLyJGO5e125_g0M5E4g285-rokUTb9aqSAILsHb8Ryxn89xJMwroARe4AmoYRGrb7CTZlWjzgHAenk4EgbBaFfG60c0xBol66V-vVgJKXKQEXydQT-VETa21DF1Qj3FWh9r5FNdRl1FYSafSJvq7JoycNLAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQuTywQLo1bR_tsJT4kpenKChiGc7KUnt_x0ebgMdIYgBxjuyfkIVB0l1Z9ErUJB-71iYeS_SmSscMhnYxYOOLDnEY1yi6oZZH2j0yb22ReR6dLEl8_ehpBnc2eQhX5iJTKr5hL9_3UwZYhkcTzzMdcE8it0vj0uw3w3FkIO4DGAXG2pa5T3BU1T-IMLqjmXDj8cV1xA4KHFCFj7UZFEpvoeiMdEaCVpVV5hUV1tnq9w9Rjv6CvS61E2Ip_i5yk8vwDICJhtZ9yda1i2AcjvBvrdgeTuIh_NzrRsHq7bYaqrUHRVNUjoprW-38cLf86bsMiLyxUhUFcoOWGvrgANSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68411">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XplaBWO0KutsgHdN1H12nSiONgdfqV1fwrsLxOt4sU3ato_dejLX3ZJd11T7UWO__h90b9LueRU1XRKtIUPkNIkukZDz2k0AWnazDGYh9tpB0wnFlh036Ujvb8-yZVCRRski3nxBZroD47z6toFnyG58W3oPVSi5HwnY2iky0orVw_u-UhzdY5B47dSzFBKBBTMN__vQN9amIowfOHZqahBBWH_x7GbH-Ka7J9GcNbZyj4a2YPF3mV47-1Rn1aoVcJekIOSZBWpFWAk5WVGAgLnYuFE4K-_PGdiU-O3EZud7H7UskiA6toGBVHnu4oPJ4jH00gq7UjEH3NZf2G1wQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پل سه‌راه‌ میناب به‌سمت رودان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68411" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68409">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFGh-T3WKRVUzs4mUF6ZGFYUsvjZU1HaGthLLDNkYDCiqJy9EF95e-f-zZzCQxP389KDJLyxOjEsncXIZ2NQYIbLSx0iZrfQNP-f3YdYuzvrvtg6VLAta52rCQf4X0GCR1iPyZ-wvfbx3Awr1whUclQ2VVRVkIpEp_ZnDxrhIxFqSXRKwGjtbF9dIRn7g9Q50zMCnuKIwl0aDNlCUmOY9TWTjxyJg7NZm1Kev-pXhWZEpgGxcxrmtLJuojGrio9aM8w__UNIakdukF3qp9e5Pn1IONY4WmUkXBgj-rgGT11tjH8co9tgt_nHXA8YmNCfipoT7HXFBn1FXMzTOyd7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Io_eyigLVWh4j8gP15zpOBToawR7kvx8uwV8RVBHjHjVoawgJncRJHAPiw6mVm2-evMTuVhCAK-iI-N_X2Ft97ZzGtxdB3Czkodvg8fVyvoag07Vd5NL6jk-20eqy5sglO-oK5qTbHjh1Qr-mSHMLbj0lW4hywl6d2Ehv6HKWRB6j2udr_RglMn-jLiaECzZIGV1qIoOdW2_LfBheGG4TkvowqF5p7G_v3Vv9uNRjBUGqXdo70j2LNsS8usmuEjq9YY-GlNn9tTyTYW1BzXly_4Zrhom9oJuvoYiFqmrmK3QoAnW9DieBtZJgT6hw-zj_2_1CmzGWAa-nEhVzdw2dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ارسالی از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68409" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68408">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=Nl0ppuDe4UXHnwFgV_gjSRJZBIjzxRg15eQ985Jw5DpNW38nu_EZW_L-HDqO9pieCzE2fvZ4-gYvz5wLMATb4SqUhowQBhwWYxEQf2NRY6ChcaS8kOQWPYKdGDYI1zM8hJ_q97yzeE-_Uv025MPKeX_1t-LlT7JCHBDf-Y4WCRAat8YCSxlwdYNs_YagRPWvczQwJjX8UDwqyAOHQnLa8i80fWjdCfLhy8R0wFBkXVt-9M7Jn5EGyg7rLFkjtSDXRp2xwFlKskZS34hxkFQxZ4rWk3dRoqUsa4YdYm6-P3Y0jUKJZ2NmzkjRdjdu36JmV42wg_G78yewICdPedUJCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=Nl0ppuDe4UXHnwFgV_gjSRJZBIjzxRg15eQ985Jw5DpNW38nu_EZW_L-HDqO9pieCzE2fvZ4-gYvz5wLMATb4SqUhowQBhwWYxEQf2NRY6ChcaS8kOQWPYKdGDYI1zM8hJ_q97yzeE-_Uv025MPKeX_1t-LlT7JCHBDf-Y4WCRAat8YCSxlwdYNs_YagRPWvczQwJjX8UDwqyAOHQnLa8i80fWjdCfLhy8R0wFBkXVt-9M7Jn5EGyg7rLFkjtSDXRp2xwFlKskZS34hxkFQxZ4rWk3dRoqUsa4YdYm6-P3Y0jUKJZ2NmzkjRdjdu36JmV42wg_G78yewICdPedUJCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68408" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68407">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
دو انفجار در خرم آباد شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68407" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68406">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از تبریز موشک شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68406" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68405">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=SwHIynBlqyHymOzPp6H2leb81k0LcsSEnQSRBLM62Wk52p1yRX9XPhkCebe1OxVd3_d4DcXlu71h4gs98KXVoLzvSAIK-OZ_rliWx6lK3CPPm3sFlVKe5RhJobN1LAfwkvYojjxIWhd6yua3GA0jDdb5mCCMGd_o8WAXJ_4f-1rSlJUzTb10xz3mgCk4HntnHQxr3Xzqwn6GPtGrUMqIV4Oze117fShNetZtO7rJ_LjluiNG7MFoRQD_lO-PEHD9isUiQf9IhkPEU9KcLRPXxYKhiFC13KoU42cYUx6Cu66NK-DN-22B9qkL9TJQsWLruc5sO03Ny4suvqRX4-zVLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=SwHIynBlqyHymOzPp6H2leb81k0LcsSEnQSRBLM62Wk52p1yRX9XPhkCebe1OxVd3_d4DcXlu71h4gs98KXVoLzvSAIK-OZ_rliWx6lK3CPPm3sFlVKe5RhJobN1LAfwkvYojjxIWhd6yua3GA0jDdb5mCCMGd_o8WAXJ_4f-1rSlJUzTb10xz3mgCk4HntnHQxr3Xzqwn6GPtGrUMqIV4Oze117fShNetZtO7rJ_LjluiNG7MFoRQD_lO-PEHD9isUiQf9IhkPEU9KcLRPXxYKhiFC13KoU42cYUx6Cu66NK-DN-22B9qkL9TJQsWLruc5sO03Ny4suvqRX4-zVLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند:
پل گلوگاه بعد گنو بندرعباس و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68405" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68404">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68404" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68403">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
منابع داخلی:
چند محور مواصلاتی هرمزگان در پی حملات آمریکا مسدود شد
؛
⏺
بر اساس اعلام منابع رسمی، تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت به دلیل حملات دشمن تا اطلاع ثانوی مسدود شده است.
⏺
همچنین پل «شور» هدف حمله قرار گرفته است.
⏺
بر پایه این گزارش، پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرزه، نیز مورد حمله دشمن قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68403" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68402">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac032oUtXKljnqMcON5SPwPhlVa_Du7SZ5AU0vUFReTpbGHeLS3ByW0susxNI1w7W0X7OA3nEmfPi5NGCLd1ujgzXjYtqXhFBYssz2R6j4waFdQ5jlukpLmHoD8ifFrxjAHYN6DqhSnE4gIyxaMe_6m9Tyz6r3bYgmbz98X2ftvy8G0HQuZTUU9MACJ54_H1DQQXxIPb7dq8IWlyV_ybCDRMXeEq2imqIXbCivmF5rlMNlPJaibNInntFJSC5gGB6-jKsL_VEbQfsuqE6QT-goYSJq3sv0pTaUfh9Tp2rJ4eDWbLtJ8_P0LuSdZBEUEX2-UlStpLM8os1h1eo2kTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پل مسیر بندرعباس رودان هدف قرار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68402" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68401">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871564b347.mp4?token=eZp4qvwlam8XKWC6otyZ8EbOL6iGodB0bXdTPdebaSgkcFmtc9jEntBtg0JlDvlBILVTE0Sr7Pv5w9VqEMF_km0y4rNLhJdbLgiLloxtORUMlH3s4ZAx8iNNXDmA9gHhBF8auu_KwfD11nSDTTvjuSDJAePI5Py1ubKcZtZ2uX4AmXd6CzbhGx9I8Mpyjs0agrI9Ae7WnNK1Nxeb6lqgUksgyTvn-26EIHFXzUsClouRJR9cKJ3X49I91IpyBm63ouiRmd8EFRUBy2hyz66uzrF3ZFsou1HBefjXCVynLNy3FHYGf76xPR-stPcD94FLWn3xf7YpomzZ5BkOvoz9gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871564b347.mp4?token=eZp4qvwlam8XKWC6otyZ8EbOL6iGodB0bXdTPdebaSgkcFmtc9jEntBtg0JlDvlBILVTE0Sr7Pv5w9VqEMF_km0y4rNLhJdbLgiLloxtORUMlH3s4ZAx8iNNXDmA9gHhBF8auu_KwfD11nSDTTvjuSDJAePI5Py1ubKcZtZ2uX4AmXd6CzbhGx9I8Mpyjs0agrI9Ae7WnNK1Nxeb6lqgUksgyTvn-26EIHFXzUsClouRJR9cKJ3X49I91IpyBm63ouiRmd8EFRUBy2hyz66uzrF3ZFsou1HBefjXCVynLNy3FHYGf76xPR-stPcD94FLWn3xf7YpomzZ5BkOvoz9gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره پسرش بارون:
پسر بسیار قدبلندم، بارون. بارون عاشق فوتبال است و یک بازیکن خوب فوتبال است.
نمی‌دانم، سرعتش... من گفتم، وقتی یک بازیکن از اسپانیا، آرژانتین یا فرانسه از کنار شما رد می‌شود، بارون، چه اتفاقی می‌افتد؟""چه اتفاقی می‌افتد، بارون؟"
او گفت: "بابا، من یک توپ‌گیر خیلی خوب هستم!"
من گفتم: "اما بارون، اگر او سریع‌تر باشد، چه کار می‌کنی؟"
او گفت: "بابا، او هرگز از کنار من رد نمی‌شود!"
"من گفتم: "اما اگر این اتفاق بیفتد؟" و او نمی‌خواست به این سوال پاسخ دهد.
به نظر من، سرعت در این ورزش بسیار مهم است، شما موافقید؟"
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68401" target="_blank">📅 01:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
تسنیم:
حملات مجدد دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68400" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=cZlZTvQTw1K4Y0ZFEfjmoSM1XDMwZEYp4sPxAXKiwWr6IVNgcaLchoTMQrXcHbG4fG2ZrrjZT7oMdbVZNN9Sb47dPgfBGX_m-AkSc_HPXrirdcf8ywWMTTDeAZcNP0uAfRCvC4TmqNoM0CRkoJ0RNWSbhgMyH5VH6fbERR_merJ9l9efpHZXzOeDQKZ02_XMl7zQ2QFmQv3q5omVlbX1g2JhfHWg9tvwuGGNtiRjzZmS6Azn-xQ0e-zH3aw_HErlc4ucR_OXQDXoQmiDueQM1R4VKVqmW-mGKXSbassdL6gw2mopeyN1tltcxYs8J77Tz3W5L4QWxSDMTKTVilJoJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a69d92f06.mp4?token=cZlZTvQTw1K4Y0ZFEfjmoSM1XDMwZEYp4sPxAXKiwWr6IVNgcaLchoTMQrXcHbG4fG2ZrrjZT7oMdbVZNN9Sb47dPgfBGX_m-AkSc_HPXrirdcf8ywWMTTDeAZcNP0uAfRCvC4TmqNoM0CRkoJ0RNWSbhgMyH5VH6fbERR_merJ9l9efpHZXzOeDQKZ02_XMl7zQ2QFmQv3q5omVlbX1g2JhfHWg9tvwuGGNtiRjzZmS6Azn-xQ0e-zH3aw_HErlc4ucR_OXQDXoQmiDueQM1R4VKVqmW-mGKXSbassdL6gw2mopeyN1tltcxYs8J77Tz3W5L4QWxSDMTKTVilJoJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دموکرات ها در انتخابات تقلب کردند، و من چه چیزی نصیبم شد؟ جام جهانی نصیبم شد. المپیک نصیبم شد و آن‌ها را به اینجا آوردم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68399" target="_blank">📅 01:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68398">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در لار
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68398" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68397">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
دو فروند کشتی نفت‌کش با عبور از مسیر مین‌گذاری‌شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68397" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
