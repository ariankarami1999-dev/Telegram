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
<img src="https://cdn4.telesco.pe/file/HfJSe5UwFFZCVarDNV4cpzw61oFwxuhTFwli7f7-ySw-nr3JxE3ZFo_TqCwp8xTwdv7wFIvEVbrFe-Ja3-pQltjwFHhEEkrpde7phhDhm2aWcqRtnRRSTJjoQcnUmZ9p4jfV2w2bAf5lZ_WAhpujYwZ9vhpvB0Cv0UKHt3TWsJDA3LJiG8VZ-g6rAoQ5ZnPp05fv4mrXrfjNXvRI96Y4K-4VuuAu0CcmbLhZPPCR73GYTdFjBwgWSVElPig96_LljM3K2FDBglrE5XycboJEEnifvRPxGIf4ahhiZIc2JgJIhz0o3YS8DEzT9JHf0jIIeb0c3ylQ3pJqeS3sLhTcHA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-82892">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دلار هر 10هزار تومن که گرون میشه ویلسون 10تا ویس میگیره میگه "شما رپرای اونور آب اصلا چی میگید چاقالا"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/funhiphop/82892" target="_blank">📅 15:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82891">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امروز در کنار دربی تهران، دربی شمال هم بین نساجی و ملوان برگزار میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/funhiphop/82891" target="_blank">📅 15:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82890">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/82890" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82889">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0kuqz6LcTpvM5s9eWRqYlZ7JP5tFlAXU1v4kue2aO5bBMA3-4Gf1u8n4G5Loff-jF7b-Wj71pyimc-oI5ehxsJP2S3U7cfNe6fCz0oINtUoQaHFnt0tdhiO1QpT7HrijP0kFK0OJGq566WRBGHAbYZEc5lMsjulHrTDXl02U1lhc_1Jyg_vvhKWWnWiKBE7t9de2Bh5j_Jt1A_Jrnd8Pw8wqkAOUCz55UAkad4XdAIJBnPTn6KkXokyJ7t0dFxkGOTVILEo6RdMzvltPtwoI607Ms6PWyCsD_Hwq1TgPC2GfPIN3E9v1qiWuqjLQiFm7VxhlmY6584gvHxzQpD5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/funhiphop/82889" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82888">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فان هیپ هاپ بابت تشدید تنش ها در خاورمیانه ابراز نگرانی کرد و خواهان توقف حملات نظامی شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/82888" target="_blank">📅 14:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شاید باورتون نشه ولی زمان اعتراضات 401 دلار ی چیزی حدود سی هزار تومن بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/82887" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcAIV_6lMNGqYyzO1RkPeU3EjcpwI4nMNM8Qry6fQSm1DUTqqj5tZLZjEQU-3qp8LUy23i_nBj1cOEjhjebFchQQ3AnZrQD_rN3J8wafwXU-lbdL50YeSp2JYMoYgU7rI5NqD8hqq2k1DHoLqV50a42mlsIDCwpJiXZLTWIossJJl-5RhyXmaW6kNpQwe10d3ni1XpnvfIw9iaOjhhaOJ3qV8wEGVdwPxUVX_gbRHKc4nNVSkmx-ez6gUBKBVW-0MBhnm0KhYrUxVlu93sw7s8kN4gsUx4s28QF-91FToTWf1SJ-Lm6oqAY0UxAWzsOaFt5zAkem3VZe296T6VyoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مال دیروزه امیدوارم الان گرون تر نشده باشه
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/82886" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_OPnlf0_jBb6OoBQ-vpReKOujOxHdZ_yccqDpcv6Sgl3Hra1TG_H5zEVj0GUD6nVHhQIRe8opePjF0lci-w1z_zzHeMD8N93UUUfNOidkcjP69S5zl_lRdbPhgKOOtoi0-1P50Fnwv5U51FbRdbjfV7OI9lgXpUwFgl4q84qOmiMhyweiuRL6ZK3sHh-QdPMMc6FGdXCK5H6xvnWWSyJMoKMn5n4jgshHe1mEhpzmVmb4fdPmdBpka4f8eujBW6-1-U9PxEpnizfw9ATJCzIPydqfkwKpoZh6XL3R0rE7q8Sj7J36C1JMQYFfVaXMQhQH8W036Vth8nlVyRPhEOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استقلال
🔵
-
🔴
پرسپولیس
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
چهارشنبه ساعت ۱۹:۳۰
📍
ورزشگاه نقش جهان
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
استقلال
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
پرسپولیس
:
۴ برد، ۱ تساوی و ۵ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر استقلال: ۲.۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر پرسپولیس: ۲.۶ گل در هر بازی.
🧠
برنده واقعی کسی است که بر هیجان خود غلبه کند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/funhiphop/82884" target="_blank">📅 13:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82883">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQgBw1iFDkjguk0LeuYrMSVlm1dGbbqA2WNkmKO38hOT2o_IE2QuOKF1SOaFkYaOQq4kIkefLv-Roe5UJiC0xLJp3Op_bHovVTvzNfgfinvtM5cIkN0Yg8h4fmyF5ltv50G7uJVQAiVns2o452XNRooUvpg02RCNoj-FLAzFxtzz_IylsR3cH8EXPmP8bj5BrHj_KRW9mSsSQ_ROZ4K6MVb1j2NVowjPAkeC0qOLENVnpZvBp3cZfN1X4ZBh-qRBoOxfWN4WSFf9aT2lCmcOeU_TWttHcYil_x7A2U6dqMDqWljHNmAKTJhpXA67fr-nax0X5oUISm4VfVejG04MOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان حاج‌رسولی‌ها و آرتا میرحسینی به نام "مست سر صبح" ریلیز شد.
SoundCloud
YouTube
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/82883" target="_blank">📅 13:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82882">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دلار 222</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/82882" target="_blank">📅 12:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82881">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82881" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82880">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انشالا هدف بعدی سر زمین فلسطین اشغالی باشه
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک‌های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82880" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82879">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تو وکیل آباد مشهد یه ماشین به تجمعات شبانه زده و ٢٠ نفر کشته و زخمی شدن
یه خبر دیگه هم از شیراز اومده که فعلا تایید یا تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82879" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82878">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82878" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82877">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری مهر:
موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82877" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82876">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaYTX-CIuf_P_CYMf4ts_xJdqoR6uuQWP8uv_G95JLmy_Fh3_eW0wkNpJc32RUC0EE8vqtOWtjgJVmqNjw7Xmcs92w4noXmJJRRPdLxOR48YSTPcBMhmtUPwWFV-f3F9lT40aNLzumdr4HY_RCKOIdleQlOFITLrOELvGD7a6x0DjRfUtDvlCTvkmxxW63XHHmZB-oqZpFHc4CEL2AgYG8II4aQzWX_vs0McgGxxTDSzpanhwpQqpwvv91LVggWCJThViIem42nIIhO2IrhBvCBC1as4BUsydShjCzymKvBHkIM59HHtU5GngjKsRqJMmWY7WhBq2h2cmfBVWUsNGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیب ندارە قهرمان، تو همین ایران خودمون تو مسابقات مسترخایەمالیا شرکت کن،با ترابی و بیرانوند و خلیل زادە و علی اکبری رقابت کن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82876" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82875">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAq5MXg1K5jaVN2kQBPzg4ga0mUkrB_G_dp-frdtAnn69-nKJAeQunOXQpd-dWeN3DD8sYAAACfiD1q6CCI1qO5UYmsUxVn7K4HPHpSYauZQd_5_KyEjCujwhgJ07CA2XDezs0WlW_YQyVZixkh8KC9a1Gc_3sbsOOLXT5dpoUSj-aDk47lMOT0uZZXkDwFJ3Fkx0gQuZEu9Tka3zlKOl4owHELr2rsyfOgozzO3AFkPe0qGZ7nT4IjD9P4scDKmwLlDs6CEPKkFdiww9vP52fQ5MIHEiui3EdMike13q8vY9U9NAoPhuii0HWN3F-IWu3NU8OiSyp5CeDWkS7XMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بشر خیلی خوبه
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82875" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82874">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn5k3-aIGKPTSuZusKE6xRMbxPG5vLahUm9gcbBXsU-sIRQOLeKuZ68ts_HYEFyXPVuz3uPaSsPkSxduj_vxqH50EaY6Fqq2G_Xw_QO2DgieKnrZTmLHASQkYjSzZgmTnzxfZQVIfv_xqaad7Vh4m0im_Td61AlZVMlYuskZCOk60mWUmHOn08QJlcL-fz8LpWEc99rZgRoWHsCrcYogEGPb9HUfwrRZfI9JyyXKyKBbDZPZEtqR3NiIhYO53OwU1tN8of-IzCVctMM9csi84uVr7Oy__jFw2S644MLNeczT3D3vLQqaxveKyt_hb6Qj3CNHAup6_Nvjz-2XcP7Cyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کاوریه گوسفند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82874" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82873">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجار در عسلویه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82873" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82872">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار در عسلویه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82872" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82871">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فرودگاه جیرفتو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82871" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82870">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Vn87vg0HQyyxS98WJvpvyo-uKiL_73vKDud2UOEbu32VQzbZTNteXN8e1anYQYYp0MGLQmG9-AKWm-jxHcE2vkIMUVcuUaeSO_nxdzbO-8w5ZEaBYQJCtQdWuk2e1KUNteOkaCh6v13l_7MYaqZ_6hZYo8HEdV9HNPttNRpERdsIpenHkiHhMMU-jGh9r2Y9bafZ9mUqKjVXl5j9RWXduATGn5CtMBU0CveQOtB-BQ82c99P1RWv87fUt4zTaRb3U-oHiXiw8TTUz4AjvenIuZ0eilXPBr04KlHzrbjbXqiiITTG0OPOKC533zV3RVZGr8SziUvyquYqQu652wzzzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Vn87vg0HQyyxS98WJvpvyo-uKiL_73vKDud2UOEbu32VQzbZTNteXN8e1anYQYYp0MGLQmG9-AKWm-jxHcE2vkIMUVcuUaeSO_nxdzbO-8w5ZEaBYQJCtQdWuk2e1KUNteOkaCh6v13l_7MYaqZ_6hZYo8HEdV9HNPttNRpERdsIpenHkiHhMMU-jGh9r2Y9bafZ9mUqKjVXl5j9RWXduATGn5CtMBU0CveQOtB-BQ82c99P1RWv87fUt4zTaRb3U-oHiXiw8TTUz4AjvenIuZ0eilXPBr04KlHzrbjbXqiiITTG0OPOKC533zV3RVZGr8SziUvyquYqQu652wzzzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82870" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82869">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">زدننننن</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82869" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82868">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.   Soundcould  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82868" target="_blank">📅 20:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82867">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj3kzBp9x3y0PFXVC41w62Xnw4RctO3xT0FElyKmB2uvPJkWu7dEUuHAArQDCj9wgi6IXNz6Eoxvd7fRlLFRRmmATsf-2f3x1zAw3HLqQcDx8H-QMQGD3OXml2xZvGkNBylISJXs_VZ30hg0jRMw8f1PvdXvkTeJMwpHP41JKJvKTJrsCUTbODHez1CC9RaohPZHhSOdMqk0mTuNg-RwFKqifmL7l1Sz8Z9Z6BO_64Cb9wpvi5TJxDLUQvcMM8f0Y4_482RJdCP7fmtU6JQQI2i75i1Lzw7ILEPlK6eHaINYjAfkTH5f6r5gNmJ1kDXCBW8FwgXBAq8QqehAHczO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82867" target="_blank">📅 20:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82866">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بندرعباس صدای انفجار اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82866" target="_blank">📅 19:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82865">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فکر کنم اعضای وانتونز رو یا ایلومناتی کلون کرده یا پیشرو جن زده کرده، لاشیا همزمان تو همه پلتفرم های سوشال مدیا دارن پشت سر هم پست و استوری میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82865" target="_blank">📅 19:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82864">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNHdbLHA5R9necrRFIXm0YcUBz9vfu0NraiOHVwtpEujamxEDtWIk07orY6m_ZOt_SzSBYANpGn0wlfEXLU7zwooBzw4M6eWfjSYAJfrGaTJOiz3HKfQldsJG0lKKp43k1Gu7HlxOgMee1MwySj34HtY3nG9yhFWE-d5_sJLEnLZsbUYGYlrBNLH2wIyXcyRjr8W2eZWg13D-Oula01agTzWmAklGxCsXKZLZNnyfdHvRkGKp7Rp0ttv3oXTRibfn00Tunu0e_Cqlpo1axRYgt-pacS0fMDp8w-NUNXLtYh_8OXsHIGcz45N_VHqPeYYjWBGlqdTkCgvlvdePfSzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگید چرا دیگه به سجاد شاهی فحش نمیدی، دلیلش:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82864" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82863">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJcKJohPOpfUlnDpxFs-Ji2GiCzIsVdKIt6NnN0qYfROQLcoCM4Mvd-w9Q69VuIIOGCuZljdZ4U4m8AtPv5TkJgAcpsayWmhV4WiRt61MD5NsIB-evD9iq0w0T_aBL0BlMujkY093blAxgNEjORW3qrC76rsQVJ-97U550u2y_yAIqvlus1VkviYrBCJLjSJpWIJMsM8FtD1QjCOt0dYVCke97z9remrcXgZUiw9R6i7JWlhBgTJRmcYLBD27mif1fpMbzx1CQhAtax0gfOTyiuSzPjZmVUjTQ_4FwsoRdYmP3c4b-sl4VvmrY30D7Jg9N5OfaQ7BYxxAK3Ux4WP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82863" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82862">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgTYmoZYBJ5USQRhNos5VBBHcCgjtNWkjUvJjArn70HQ9CxEliQ80Pz7ylUPtMak2-7kZO8A3bvND2JuTe-8kOOyxrDASC1eT76YstOEqXNpWoLf6FYIfOa6gLHvnXpsbdOI6bawdfWd0rZMGFkYbVOayyaHKjgCUbUrSnQ04vjoq2GrkTQkr2aFR4sU4gEcpN1e-X_j7TNksvAaUgII79p1aEHGJfDDt60iCNV00p_zyzFNwuxuCiiBnzkpKhxYVYXfCd4_U65aHKXasEFrYsmja0NsuvSCRabyoas24Y05nl59BujnikBMNfRErN981VwSVJnQ8Ofh_9nM7LuA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر کاری که دارید می‌کنید رو همین الان متوقف کنید و سریع برید از بهترین تخفیف ثبت شده تو تاریخ بشریت استفاده کنید چون کلا ۶ ساعت ازش مونده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82862" target="_blank">📅 18:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpBaBgEp5ixkrGN598HXX56rcnkx-i-kTnUOeVeJbx1zsAwGDDFniUqoFKDtfkCGh1qlHB0tamff5Q9TC85tXVUDwaNIV7zRkGZU99A-enWs6BF2TW3kL9fA4mn2vF3WeXORrhdnp0vrYqeaQFrmQYYO-j02qvDzZtg-jahhPGoq3EnrwjCHI1LDynTclmudVeKH1tLQ6JrMF33zQi13PbIcUhL9seD96daIjxiuS-6bZqGhSEz0wsJlxqtzE_Zn-HU5m7HGzt1dTHZrpd-ViaIiU86LPF7DZT2gSMfQilXjIaz_P2jkw_refXb7y5q6bocqDVf6jNbfFuztewtRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فان‌هیپ‌هاپ هم فانه داداش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82861" target="_blank">📅 18:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAQ1eVnzehttRp4P_IOWZ8cApdZxgRDULu8zpLF7dT7_PEIWEH8CiUKM1smnKeEOydmk1EF8CEe7nPs72HPmqXfwDge6mig26tlc02_5qwt880j6759_GG742w7gSNNEFYxjiwH2GqaqwO25SlxwjllBCipkg_qlVPxWjdI6TBX_bx_p8HcA1-oQB-L0rQav1e_SJtHnYuVKhcYtvHYpbX1ra1X592nyCCGft2RJE68Z6PDMOijFskF0khXN0llEVNZ_Fl6GkKU-ADNiEt8Bfr2vOgiV0bX6d-NysCKhd-A_G1ITOMxm8kSz3XxCRjwryU8nhrDQvBkIYrW8ZDRCHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82860" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82859" target="_blank">📅 18:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82858" target="_blank">📅 17:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسکات بسنت:
ایران تلاش می‌کند از تنگه هرمز به عنوان یک گلوگاه استراتژیک استفاده کند.
-این تنگه برای ایالات متحده یک گلوگاه نیست، اما برای بسیاری از کشورهای دیگر این‌گونه است.
-این وضعیت در عرض ۲ سال تغییر خواهد کرد. در ۲ سال آینده، تنگه هرمز به یک مسیر آبی بی‌ارزش تبدیل خواهد شد و نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82857" target="_blank">📅 17:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستان چون این روزا قمیت دلار لحظه‌ای میره بالا و شما هم که دیگه براتون مهم نیست چون سِر شدید، هر ۱۰ هزار تومن افزایش اعلام قیمت جدید میکنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82856" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f513feec.mp4?token=P_cG5L-J5ze5ykLbgaT7FqOKXGJgVe3PsO4mfsLPO3kDLa6iAvjFHCpXUEXEohXu4va70XQlbCeoqkXM2XcbxjHyFPIYLuu44e79R9oHkz-tI-nJXWGfb_92XSXxonTS8vW-8znorYMEtyMlwOfD7nUl3u90gfRxAwkvWZVDgixiutRUjKoiaA0rzGsEqIVb7w5TnK_vpD1ImNigoHMgRzCoB4DjmWcN27z6H2kmEbOSq_ZOLf5hLekZBocOgCm-6dFmyqYch6t_gyd3Y_VWzV9O3GeuTtd8GGUC-nB4aPqgs6IVCKMwOFuGiX5AdhG24OuR__ts6qTSEXTJEG0H0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f513feec.mp4?token=P_cG5L-J5ze5ykLbgaT7FqOKXGJgVe3PsO4mfsLPO3kDLa6iAvjFHCpXUEXEohXu4va70XQlbCeoqkXM2XcbxjHyFPIYLuu44e79R9oHkz-tI-nJXWGfb_92XSXxonTS8vW-8znorYMEtyMlwOfD7nUl3u90gfRxAwkvWZVDgixiutRUjKoiaA0rzGsEqIVb7w5TnK_vpD1ImNigoHMgRzCoB4DjmWcN27z6H2kmEbOSq_ZOLf5hLekZBocOgCm-6dFmyqYch6t_gyd3Y_VWzV9O3GeuTtd8GGUC-nB4aPqgs6IVCKMwOFuGiX5AdhG24OuR__ts6qTSEXTJEG0H0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکار رو یادشونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82855" target="_blank">📅 15:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به طور خیلی طبیعی یکی از دیگه مقامات نظامی آمریکا که میانه رو بود به دلیل اختلاف نظر با هگست که تندرو تره استعفا داد(اصلا هم مجبورش نکردن)
این استعفا ها قبل از شروع جنگ ۴۰روزه هم اتفاق افتاده بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82854" target="_blank">📅 15:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu5A1_RYtW0rsRSl4kFovTRK2mTIGPhGh9N3gMhDSlZWlcw6zAocLlytSpgkO7rDAU0Yumk46sC_ZRUK50m6T0f2PVOX4Knb7T3H2-0OHiCJrJjTv3vL7yRj-X_IMJe3_w95m7wv5D95XJ4dk7hPfzi0aGbUuaEoVpfYWY66Mbz1vBhleXEei314hXaPbZczPbXw5cFyWugDNmOloQkSPFYbthDhuzoBeHwEs6uUBTWuTW4O-Eef4A39cYymbwfs_6EFPTnxW6CCcPdtiWNoSBxDt5ezTDtiRkvLJKIQuP7J5pfUw8p4zvOokCJcFD204_clM5anCtJL0SIWHFM8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوام زندگیمو بزارم رو این
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82853" target="_blank">📅 14:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82852">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=b_K48OvUl5ADaWircEN7_OL37v33oT0GUuMlLe_BWIeoaa14ax4V_JJKrZdYaZdCl-aul2B7E6YU8sIjmwPWoPwfJlhzcQKUjVv-TazkkQIFJcCosKF1XgBe8VfV4QZeIkIK19r16l_6-LJfdFzG-DD_zvX5fVwyHd5IcPvrwTuPXuz7t6m4RSkOL5At0dJsm-N18r-dWZ08Ffzm9vUhvUNSDJuV7Y4bFUvBe10tOSWJQN7zoG7tY1INRjCvVpZaZ4jfdWaEeleiNWAwY2pbweitStukp7pNUYlmle7zz2i9b6vgn8NhKeca8U-dw367ILmHv9Hr1wkQcQTYnuMvvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=b_K48OvUl5ADaWircEN7_OL37v33oT0GUuMlLe_BWIeoaa14ax4V_JJKrZdYaZdCl-aul2B7E6YU8sIjmwPWoPwfJlhzcQKUjVv-TazkkQIFJcCosKF1XgBe8VfV4QZeIkIK19r16l_6-LJfdFzG-DD_zvX5fVwyHd5IcPvrwTuPXuz7t6m4RSkOL5At0dJsm-N18r-dWZ08Ffzm9vUhvUNSDJuV7Y4bFUvBe10tOSWJQN7zoG7tY1INRjCvVpZaZ4jfdWaEeleiNWAwY2pbweitStukp7pNUYlmle7zz2i9b6vgn8NhKeca8U-dw367ILmHv9Hr1wkQcQTYnuMvvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بنده خدا در پاکستان داشته خودروی بدون راننده‌ای رو که خودش توسعه داده آزمایش می‌کرده که با ماشین پلیس تصادف میکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82852" target="_blank">📅 14:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82851">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش : با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82851" target="_blank">📅 14:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82850">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش :
با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82850" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82849">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOR4D67UYmHH7eLvT8EqPfy2KxRhrhsANU7gKHpvnKMjZ3dq2IJtEOzRI6j7kp3ziCNFSciuOVBjyktK-h0prDyr6Sv99xDx-WP5_eXw_XWiteSnyChat1p9gEN7vMqvmnfg7odggRH5QSZJJHi1ynmBhzcy8noDwN4_Uqjby3u_bXP7lA4_zbOkqcsK73Jtt-8ulEvau6_l3inpUGBTo6oRoKbyZmSJTrrCKexQmkSIfeCE4yrD3UiEyzNh2pxjm-cyQp7wXXAmQfpiWJD37cH7R9ac1y31OVN_Prv6nPHmrWXstvOoc_mRFq98sxDyUfmgoCSr_RB0galuHmvzkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82849" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ69DU6PPXS8Du9ZAOifGzpDDshngAtNf3UYJuwd7JbEyquVZF8hjoYwnSLx_ZaKsd2rFHMZuhexiTonREPePvnIQXmNwuaq6xVBT7yDRD9cotQWrUGmcj5oZ_kzJ7Tyf4-PPw4xZzhKgjIyBvHcsO1WOl4y8gfyj0Lh2i93CD6x-l9BRJ7htTnBqgNMoytac70Ui5FY1Jsin6EDBNIg2GeBmOvR_WqBFxDdaLk69vjzmZ9hrPoxj26SoVrLqm2W0lsuUGOJNPIB939XMUWm_SDLsJXObmtzkwiviWlG0qeFbod51fiWN1P_kyP-axcKyitVZAjSjbUd41VVT_iuVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من جای نخست‌وزیر کانادا بودم بعد از این توییت کل نیروهای نظامی کانادا رو منحل می‌کردم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82848" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=AR8d9vP2iHnPKJ4zUVHNeegDhFnaIuT0H0qyQkg3FALKMoe291WpOj9-2Etwh0yAKHFGMr5BIkfU9Ism-YKk2YVVlRr4_n6zxQvLULZ7Z2I0rOd_Bz_pwfsUGMYwgSSj9v2f7xFKHsEu-TFMYTMC2Wcr-4S93LKvlBPcoZfAZ61IdXnfXnkkJJRaYo7XvAER74lB2r0tlpDV0cPMDUAUgwzk67tQoRK34VOwjrjBsZLUGeHy-ISfns2DWQ6jma0GY0yZyEcalalbHhglpXEZgNkHRY6VdkAE8fK39QSLe4_N3ksFXW4xwnSpLkopcQK56g_UHvef6wIXV9wNW8TX_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=AR8d9vP2iHnPKJ4zUVHNeegDhFnaIuT0H0qyQkg3FALKMoe291WpOj9-2Etwh0yAKHFGMr5BIkfU9Ism-YKk2YVVlRr4_n6zxQvLULZ7Z2I0rOd_Bz_pwfsUGMYwgSSj9v2f7xFKHsEu-TFMYTMC2Wcr-4S93LKvlBPcoZfAZ61IdXnfXnkkJJRaYo7XvAER74lB2r0tlpDV0cPMDUAUgwzk67tQoRK34VOwjrjBsZLUGeHy-ISfns2DWQ6jma0GY0yZyEcalalbHhglpXEZgNkHRY6VdkAE8fK39QSLe4_N3ksFXW4xwnSpLkopcQK56g_UHvef6wIXV9wNW8TX_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری اعتراضی سنگین جهان پهلوان هادی چوپان در واکنش به حذف شدن از مسابقه ناعادلانه دشمنان و ناملایمتی مردم کوفه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82847" target="_blank">📅 12:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi13Jyv5bS_2oXcwQu5nPgx7eL33tAAIPDMUpNg0W8um8-ChRHQPuttBi5bHDHNCTVpP4J5hz7fxADBRlnLkk-D3HbgtKEj71opkOr4D24jpcGOb3lspAcq0QHxViAoS9ZzVPQfPDJYlq_E-SjKZFNrckaHAs_RkxBVuLRfQvp09iah1HFiwiyTF673JYwuEcTh6PYlbUew70dAw2dCkv1T5dIpLclDaCsP5E6OdxNe10qN88ywxgTl4w-cZy7e5rTKUD-_ATkh4naWYSMvnSsMBMSxdd9Nl-HJ1eEr6Q_-D6n9U28QOdVxYbIa7uhkirwsRnwVttAuny6j42wSctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیپ لام جدید تو اروپا متولد شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82846" target="_blank">📅 01:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کصخلیتی ها.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82845" target="_blank">📅 01:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82843">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhS3SPUEMUvBlEv78mUwXOeLXsoqpGKKXJXFxL3vax-bemn-SynLTfckTI2Yt2zNlC2sBD6nzApKsBliA9mAEx59GEfDn-KZXkkOBq1T2nZcx0OU2R6lUR3M4vWEWw3dJl3OySUAv8aC6234fjis7f-Sh1j6eeIg14lRRn3r99VPSlOTwLEjLy5uBqkRlMNADGGkvEE9V_oyhdaH3RE8d-mV31lZiGYTU2k5kPI4bEmjbNo8gh8xhBxChrIWTrcfyYNfmptkI1-E0x6MLW1EF03BuaSIq74c6nNUHAGamCIno9ESnHH04qTwCQkuGJlQhljoarE5UlvGlCt8WOiaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=qsAWyjT-iZ_gft0wfQ9GkZvojvyXiBCyrWGc78EdDQdd_OX8SgA-ZSlNA1K2kb1mruCAZ-_SlsYZfiMV8w9wQuKtVhDxyiHquMIHYD1vR_vpKmrq6Q7ZYhHhNSpAPFqpBR9GMLL_2zhuA27n2fqlPmv84ExUitaS1IuGeGCxHqOdPaeX4s1bcBP5LnrdEnBLVavMhLhJn44-ryGsdfzeZToEmk2F8izPPfvXoVhmmjd8CX-QdoR7d4BcKi0bqPox5If4WzajqUgl6U9huftGg5nPVQmHPUbLiKN8iBL4MuKu2eNBbydR4LTKIu46k_i6uglF_KnOOsveTo7G1yScnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=qsAWyjT-iZ_gft0wfQ9GkZvojvyXiBCyrWGc78EdDQdd_OX8SgA-ZSlNA1K2kb1mruCAZ-_SlsYZfiMV8w9wQuKtVhDxyiHquMIHYD1vR_vpKmrq6Q7ZYhHhNSpAPFqpBR9GMLL_2zhuA27n2fqlPmv84ExUitaS1IuGeGCxHqOdPaeX4s1bcBP5LnrdEnBLVavMhLhJn44-ryGsdfzeZToEmk2F8izPPfvXoVhmmjd8CX-QdoR7d4BcKi0bqPox5If4WzajqUgl6U9huftGg5nPVQmHPUbLiKN8iBL4MuKu2eNBbydR4LTKIu46k_i6uglF_KnOOsveTo7G1yScnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پیشرو داره غوغا می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82843" target="_blank">📅 01:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82842">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حالا که ما رفتیم ولی ارتتا مادرجنده به این کاری که دارید میکنید فوتبال بازی کردن نمیگن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82842" target="_blank">📅 00:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82841">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhawUKIKLB697h3TzRayDbTaQT7HCrcqvxm1oP9cgKOBNlNxaGttyYFdlpia00_zflk_aLWqCyUtYMrqBvbEZZj1NkWlol-_HFu6u5ja5PUSt-q4Ufw-_b-XYGz5h6WEyyNsnyRYkCMTfc57gg8WhjNXRdogz7LZtu8wZBiKVAz21RNQTeVbBvXJgDsitx7H6Ji-fqnfpue-bhm2x6dTQunP0wT4jaaJPzbzpy_qAUpPdBmAYHc_aT2944Vavk4NsSVVa2HiQVdvTTai00spX7_RfnxFmxojawXVoLkG-9VqqTj0DFfF3A-IDfwxEIn2ew_YA0eIp0O8OzKMlW8WSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خایه ام اومد تو گلوم</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82841" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82840">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUCOWZtLgt58Xhmi179qS9J8FPygrMb4C8NW7aqEw0TIXDuuryHXP516U2WEjGOaXaBb94GPncC3ctcYaHpVx3_AY8T02W9Zwp5hVs7JeJWdWVYe4lHgOEMEVbawNGo7ErMUd2JfUshbBepZBuAPlDadhet6hemNCujsezF81bnv1rEXNERF5GlMcFciqceabc6rJK4dokxJUIjOFhasPYZSkCiFgNUYpS3EMFK6_-CRXc3eiNHDK-1kNm9UurZFMmPllb9tuQBCIuN-RtRLbO1P6ioMAn1bk75hriDAmqoOuN6A8LoInpIVTCzRBGNi8wHiHCT6qa1OHwmkz01ZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشه یه نفر بتونه انقدر اشتباه کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82840" target="_blank">📅 23:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82839">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNdlI8aNVk8cBxOQU635xW51kIsP6HbZWb-7vBm2tw1LI8jMytX7D4fQtnhEaJ21ZjiGzy4d5UTWpc479eBW0DyinpNMSHxHeJQfPR-IUhc7-edP2I4V_IgubddYlit6a8OaJgA2tt2_ht0k2s0CFQScHDWneA3retWWPmOoN1cGKYET3Y2LL1PFOkK0Q7c4xAjJ4fuYY7Z32rx7-AuGV5mrCAuY0InROKZkTrtfYHTIUizJxEfoTFiJRrG3KdmWUQPuU5P4WQtMc5fGPh6X_9mUTTDYWJ8QlCgeDo_hVKoIGzmySCRcjoSuvchHonvRHVVVE-AeJYnQbujGw0Y-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این چیزا جی تی ای رو پی سی قراره دیر بیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82839" target="_blank">📅 23:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82838">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پزشکیان در واکنش به تذکر رعایت پروتکل‌: بابا ول کن پروتکل رو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82838" target="_blank">📅 22:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82837">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پدافند جمهوری اسلامی یک فروند موشک به سمت جنگنده F-35 شلیک کرد، اما موشک توسط جنگنده دفع شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82837" target="_blank">📅 22:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82836">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcz-LGuc6xu2WZ0Qk4Nvjz8-tobnk9ELCQ4VQvnSxCOBCD85UN-rh0j_sS5q1pWG1rren5Bkm-GIVEvTk8lkrajRCiNktNcK2x94r6jcmjZYtkIreSdxrCJ6_6R2tKV2Jxii_nQlSqB7WcSl4MW6Exw63w8_h1IyLhOGucrjvP-lBOeCBmGmSYIJnGT-3u2tHcBjEbps906Xh62v0k-I9UuQgqZQlIVKiV6hkKuZykxpsBG4d3MZgrDMXTpSs2Fazpcw6vWDdnm0iaaYtIBGYPD3JK2UtHSpiO93jqnP5bcPsdFLimquv_LU10oYr8I8WBOc9GBfmhzSbWPytQhXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بیا تو چنلش بگو دکی پولمو بده بخندیم یکم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82836" target="_blank">📅 21:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82835">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ گفته میخواد امشب جنوب رو بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82835" target="_blank">📅 20:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82834">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSikKt2Qdu3ezlvR1iRewN9LaxviCl52Abqkm9U-ZtpqkEqRJut1FR-DUTEFQE5r6uAALygPLRbN3OOmL1iyMX7JzOCCrwPuRK9eWopZ0jA3erht_z9a02RBDYPOjuvI5iYD3L3oUZ73FFdoJjgCkmVGsbCn1lREdvA6CMDHztZ0K531lt1kTEzGg8I2Xrpc9PkqT1Bb8sU0DjvrqO-Fs6A1BbM3kh-q7-IevtuxGSUIzFkXMO65bz3UheJUz_vEsbhRkb0UfxVY3OLv2AWlb_HvIwfLkac9wVUuO7hQu7cINC9fRngw4aNtZNiJkIDq9JzuNftdk1n7b6lgy67djQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82834" target="_blank">📅 20:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82833">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82833" target="_blank">📅 19:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82832">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دالر ۲۱۳
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82832" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82831">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1knRD9xqr81gT3AME3z0iozNcOinoBFX_c8rzvGhkhwJfLMXP5Bg7XdB5GfvrnnzuchlQy5Ffs-QmM08FVL2sFKJY6a9F_b1NRXpCQfADVfrSCz58n5xQ-JnD2spXHI3T5tnwZRTQhtmPyYMYV7Vzog7eDbVh_grdViBEqkejzcndf97XQb5bDun770IOmWWBjHILoi9eSozgB6Jokmh5RSNj6zL5hN6uCKLrVre5JBhQCy4RFWMQ3bp8LH20o1qyYQWiRPMXl056xdz8ZVtUkfKMYm4F-r-yIa2JqIS3M0XqlNr_vySyMUXsFaofePaRHfK9K5fG0dpyfanhSdTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی از بازی های ملی خداحافظی کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82831" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWcO8U6-TVsl8PcXk8sR_arhMcgo9ryWZ3cNftlPOXFOJ9S2oWHy9QrSZ3eQf3Xt_nv5k65rbzEVp7cPBZTKoFIqfaAX4v04zhFjc0a2V7x8ybeeGCYljd85rt1LIRh3PdMUyJCPUAnapnJyNE3drzyBFIwEI8_lJts87hEZbhjgFPoGkO95fy9cwuNXUUAl6GCy1PFRk7N8W0eDpmH_dhF9VgHrEhlA28HuewXJBEjEg_3pgSt0DO7rD28U-Y-4bnhphx1nmgdBkrJkI1zIBJv_digZS0e6wV1WtMhqIxQnY7LMrcagXQMeVLrPJabyYBmI_ciF9wH87KZMlZnr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخندم و رد میشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82830" target="_blank">📅 18:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82829" target="_blank">📅 18:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82828">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شما یادتون نمیاد ولی یه زمانی میگفتن تو ایران شاهین نجفی گوش بدی دستگیرت میکنن یا اعدامت میکنن</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82828" target="_blank">📅 18:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=SB5N35P11x9cccjBHuIs6C_GW8ER7HBvFamci8p8v8VaOKMS5WZ9fqHzzw7Kdg2sHy1EGzlXIRPr-oBl1yGnM5fKrmc82ubE8vzm3EYWBabp7W5brnajI0GbBOb2rrYSkYF49IR-NWsaDaqqU5nCny89AD7MnSEcSrgZayfN37nTAYDr9Qrl5QuxBOoBY8jq6mCagryMnQgY4nL4aTpJ7fXSC1DlpVdfU923M2AP0EjCYjBy1QC6FAETdmFOE2Ygk7wCTXvHEs3xQG0wzp_IKkDIEJZUiPH7TR2ZRHgipPGQg3krR0UZ-_yao9v1upvQDTmbnl0EygZttVgyc4WalQzRN5V7cZHJxDRePopekOkXooP8rDtKXX3VgQPVU3zuh8T3y5NwdrnUif-ucn-xtSeCDq8Vgtx9CUwfkkRuHWDRbTS98EEHLAE7OVClgwWwpgrJQrRPZxkex9vLZRiu_TL8EHkcFLOuSaLqKwXMuyT6PIUEGDjkmyN_EIkN-3WYnaZYuPrQSjVUnexnhqRLEuzStdcy_ct-N918-g3PtjJ8iE7cTULC9KMB5xubz2SkXpD70-BsRpA-nKZeOOTzNDo5R8OAfeYg6WKeL8I3TUTMLEYVInL1wBbHHn0AixompEZfsyWVa0hlPSEdfR1CcaMvNuYtxpbKNq_tk_GqBno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921c1bee68.mp4?token=SB5N35P11x9cccjBHuIs6C_GW8ER7HBvFamci8p8v8VaOKMS5WZ9fqHzzw7Kdg2sHy1EGzlXIRPr-oBl1yGnM5fKrmc82ubE8vzm3EYWBabp7W5brnajI0GbBOb2rrYSkYF49IR-NWsaDaqqU5nCny89AD7MnSEcSrgZayfN37nTAYDr9Qrl5QuxBOoBY8jq6mCagryMnQgY4nL4aTpJ7fXSC1DlpVdfU923M2AP0EjCYjBy1QC6FAETdmFOE2Ygk7wCTXvHEs3xQG0wzp_IKkDIEJZUiPH7TR2ZRHgipPGQg3krR0UZ-_yao9v1upvQDTmbnl0EygZttVgyc4WalQzRN5V7cZHJxDRePopekOkXooP8rDtKXX3VgQPVU3zuh8T3y5NwdrnUif-ucn-xtSeCDq8Vgtx9CUwfkkRuHWDRbTS98EEHLAE7OVClgwWwpgrJQrRPZxkex9vLZRiu_TL8EHkcFLOuSaLqKwXMuyT6PIUEGDjkmyN_EIkN-3WYnaZYuPrQSjVUnexnhqRLEuzStdcy_ct-N918-g3PtjJ8iE7cTULC9KMB5xubz2SkXpD70-BsRpA-nKZeOOTzNDo5R8OAfeYg6WKeL8I3TUTMLEYVInL1wBbHHn0AixompEZfsyWVa0hlPSEdfR1CcaMvNuYtxpbKNq_tk_GqBno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Send him back
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82827" target="_blank">📅 17:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82825">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iuo2MMmDMDfa-om8Zv03ZTT-dqRZY0kT1WEU1OrkADuM2UD94hjtufLEbhNguFJp4NVaw4fFQ5FiU2fkx_DRbZbDVIh36hDZX5qhmuTLTKTXupAyTu9fS9mxHao725gSZ4D7f195WCZzzbGDlr4kzCzd3M18xlav7TaqXUseTAbrZ55SIjKYou6x3_XrV3bQBiSMVuluz5CdL6WLFuPtXvnX9OcH5MrsrJfS3JXl9s8i3DeI7zihJJwxKk5HJW97P_GuOEffHmff8iSpONvXOZINtwxWBbH7_8UgzJ4j4Dlbm9cbAnXFgpd7FIQSj5TuILCbLEnPkQ2UwyKY6nmfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاش اون گوشیا رو بکنن تو کونتون که انقد تو خیابون از ملت عکس و فیلم نگیرید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82825" target="_blank">📅 17:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82824">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=Yvf2nUeZfMH2QYLT-LIYAyBvk_u5wk1CpYzq0BhveIOYlNQsP_ipRSpYflSCxJKDtVKlWSr-tGzX9PhtGLjyEBzq_2F8ZB8fQ5XOFWOfdAxr49oa-707D40vyEfu8DC6pXQzyTsQ1hLKGzrksrw2kU3XWoTrlX126v2gexihbK_BmLAZP6JurLmdMVdJYxsMfkoEuwLE_eCiHRh-BYe4zeohHjLPry7tLYJBrAKX4GsxdBu7fuQ6N2J16SMRo8Ex1wCnTKw27KIyn_ErUBmkMOJ7qfze3SYegVILMPbQKI3Y6t2EQ5E8v_A6FRezSlxcfVb1C8OP_hdIKhITmRjZEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9062dc2e0d.mp4?token=Yvf2nUeZfMH2QYLT-LIYAyBvk_u5wk1CpYzq0BhveIOYlNQsP_ipRSpYflSCxJKDtVKlWSr-tGzX9PhtGLjyEBzq_2F8ZB8fQ5XOFWOfdAxr49oa-707D40vyEfu8DC6pXQzyTsQ1hLKGzrksrw2kU3XWoTrlX126v2gexihbK_BmLAZP6JurLmdMVdJYxsMfkoEuwLE_eCiHRh-BYe4zeohHjLPry7tLYJBrAKX4GsxdBu7fuQ6N2J16SMRo8Ex1wCnTKw27KIyn_ErUBmkMOJ7qfze3SYegVILMPbQKI3Y6t2EQ5E8v_A6FRezSlxcfVb1C8OP_hdIKhITmRjZEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشآمد گویی فرشته حسینی به میهمانان شوهرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82824" target="_blank">📅 17:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=cH7zXtjPX2-xUPe1gMvHo0YZJ2sAxtGfWAB5JnmGLn6czMRqJZwXtDboQoCGI3bSCDbA4uz0DFcL9tEZZLUQFzRDw4hWOn91HjlzWVXMsz7SUPKufgpk7QJ4GGHMOYE0fxgSABieRbw76L2ehdJCc5qEvGlGBvCOnN0-4WnvV5P1ASv0nHaw5rIMBWCNfd-h8sqfag5cKSLF0LtErAMqPtcK58EgxfQiZFAtflZpRh8iyUBRf9dZOVvxJuPDYBlnA7Q-aUWzCJUsG-oTXlL97DTZEV-YNB3NR-CRsZiU6DTYZ3PSw2pkcNKoob1tWUuyYrCHFqaJA-YWBdA9kGdWSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f3af0f50.mp4?token=cH7zXtjPX2-xUPe1gMvHo0YZJ2sAxtGfWAB5JnmGLn6czMRqJZwXtDboQoCGI3bSCDbA4uz0DFcL9tEZZLUQFzRDw4hWOn91HjlzWVXMsz7SUPKufgpk7QJ4GGHMOYE0fxgSABieRbw76L2ehdJCc5qEvGlGBvCOnN0-4WnvV5P1ASv0nHaw5rIMBWCNfd-h8sqfag5cKSLF0LtErAMqPtcK58EgxfQiZFAtflZpRh8iyUBRf9dZOVvxJuPDYBlnA7Q-aUWzCJUsG-oTXlL97DTZEV-YNB3NR-CRsZiU6DTYZ3PSw2pkcNKoob1tWUuyYrCHFqaJA-YWBdA9kGdWSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی جدیدا تو اینستاگرام ترند شده که مردم  میان میگن قیمت خریدشون چقدر بالا رفته و آخرش میگن: «من اصلاً ناراضی نیستم، چون اگه ناراضی باشم میشم عامل موساد؛ پس من خوشحالم!» بعد هم شروع میکنن به خندیدن یا رقصیدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82822" target="_blank">📅 15:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC5_Nuyw5cXGek9HEFFFloN9Tm9TnwROkVZlava10YI_mB6pJbl1OLssMZtUmRe0CWuc_9_0evomCDeGdYLmwV1iTJEDRI_MXapcv5s_TR_N3LMLbozR2MLhTgPed_xyZuqpkRHYIMMgKOCNyA2BaDW2TKlO_QZCJDVoPnwt_sn4F-uM8I81kWoPF8WutJJZ0BqqVtcfd-5R0ALSA5tdCc9R-O_LSTkd63XVoEzNiSEqPRZTTWaQAB3DvHLA_sEnJbKO8irYKzQwaj_7318nDokUrTz0BxzwAaCG3AtuAoIHQc6CN4CQ-4fhRBgkAjMum8TOsu5ktS6KgFNJ_dBTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون لحظه واکنش پی اس جی که تصمیم گرفته امسال بخاطر تنوع سقوط کنه:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82821" target="_blank">📅 14:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbtwHbYToE1Egnra4kjYVbUKCibMC3cfgQwbFalZsi5aJD-xpuTX6eTAMQN4u0w5oW0ZpZpWmHp0taxVExWlxpN4oAQlEl5hPb1iQM_uDpre-vZj-IwmeoexPBdatFFXKU4VSC5V8yYawHbq2Fs1DifucLp1X-NuLvMwp7kKDlqMI6bY6FWJw2ljXb75_EaHJYodLg1Y3xVm4Rsv93vnWfduH71U4vC20NFqh37Mwcthh1j6pId9DTUdt2621NFOHq_SScdHbaI7gV-jAPjHJVVaqrD8LPHjJdUzIGNselApiFNAqWQr_pXbaZUWMhWv_FSaVfjMn_Lbeynxib3LRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوس دارم بدونم مالک این برند کیه و به کجا وصله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82820" target="_blank">📅 14:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82819">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">روبیو و ونس و امثالش کیر بسنت هم نمیشن حاجی، یماه نشده ترامپ ایرانو سپرده بهش فلجمون کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82819" target="_blank">📅 14:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82817">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeoUY0AQSYuGn6V2YSpRTXkEFhb5rUNhmiFYePlQ0jKJwSVA5f1fiHAcj3gOew22TDDVlbmi7Ol5WynBhlK_7DWVMSgdGSeNunLUYGcdBevpZL3mXEF9QUFVHXeBzL3vCAYq7gQyB96BdNcZrQ98zVTVuSaSoSlHQTboCL0nijz_7wh9sX7cPvj5Tk6GUhOW4-kbvkRASN-3RJKR9Qn1arYiso_jxhOXR1e2bpYrgSrg6EtgqFnYfpsALRjvz8HKw-eKZ4r7rEIpky-8WJhLci4phcRgEb57ROHzGU_TsmgXmcZtV8d5AQ-chDYrRqqTuDmMY6MpX2xNrNZ5vYsR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cdn-IZ-LgLK9EuGFHIFKWK9uTLylXsGFfjETbdP6XNKh58UXWGwfzW61F88G6a5brscc28sGeyis6SrqH6xYSsLopLWwA1ustzVq2YpOGjNp4B5lOC02GJXhP3fVq4OPLyh4rbUCwttWl50haUpDsyS55_V_p1SDuErzFQ_v4opRgKyfa3AKHV8CZB94kNNuagNYcCCv49ChQ_2Cf_4xZhSd5HPJc1qCZ8GuVxSkfVWGFhONIcnMgv5S0vVAYkqFmBZHyR2xsMvac5HT7f-jqcppIeEV-5ZcwOeUnQAiWVI2Uy1h8hVQrFDS8y-qf5DmR5J7lYyCa2hgbva21-XFbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کسایی که بیشترین فالور اینستاگرام رو دارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82817" target="_blank">📅 13:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82816">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این گربه هایی که صب تا شب تو گپای رندوم میو میو میکنن بیان براشون گپ اختصاصی زدیم فقط اینجا میو کنن
https://t.me/+CAwWLYMxGAU5ODU0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82816" target="_blank">📅 12:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4Ubfj6CyCtQ7B0xNLZZkAZOWvu9KhQ7ZmEwKp5SAGVp823FKDT7CC9G88eOytPqB2we43S2uUtJLp45gfcKvrCRmabZs4w2r6SsXhqGXLMQBzZ6wnQbPztPnAEs0nPE1GvFZ1b6VgSB56EndafrWAACk7uW5Lkl8ARiYFMZvquo_lVNm5amOplFNQ0svhY38--Pm06xHKu5c8Nykmr-4BVWgkuiY0DbR82z98Q3RfVGKZg20kmb4km4g97iiE8FmBQ2fz6KkVcH_krzKqtntoYDhuQ7EuqMYpbQAXOxSIxITl2yoYSoDbvy1Hwmxrx1jIQvgK2go3ml4IuMXRIwnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من به شما چجوری بگم این سلطان قیمتش با اف ۲۲ رپتور یکیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82815" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دوستان عزیز جود خیلی هنر کنه میتونه با فرمین مقایسه بشه، انقد با پدری مقایسه اش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82814" target="_blank">📅 12:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtxFVDut3fuJ0pgNZnHr3uAGi_UQd1ArJWjJywTipGoGvi-DuXdWoxg9Tch_m3dV0BKuNGn7MlYHhKaAwGCG0pgACHaLIuI9FXaV5LgChaV1eic9Tq9Hq8S2K0R0wFLqfVGt4gJ8DbuZbpBvm6V6y3SkEcd3kw-M6-Nkk8jNFlBVOxBrFJTUz3JkWcemUolCY6Ffvcl_TL78MoZhTVCpLN9rlZ5gNWzcNV0eckpdsFAJTZzq_3bX_eAF7P7b0ydRVeZ1Jr5DLUhTQkvmTKmfB6FFO884bd2QBG9JDnnAr6kFPeIKyZMM2oo1YDNeN3uF8aZyEsGGSimiKULWZYXT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میترسم از خونه برم بیرون بیگ شگی بیاد بگیرتم ببره باهام فیت ببنده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82813" target="_blank">📅 12:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPOaatvXgdB0hP7z03yIBWm4kH_48pks_UzMhHcI2bBTjhQF-h48tej5llUEF-fk-VnBhhRDJ5GxRlKx4JRDD3nSrMgdJZHw2fac33ojfUtOJwyVY5Vm9KDx7kJ-cMZ1IGkz-bjwm6lt2LreZoHLdBkRVBlXXy7LBi_UzJPFusU5K2HzOhBNfMcs7NZ-ZEIK5vIXmp_wZETBypQXCP2aBSKqbMREPEH5W1_alFpjb4LxwoGrUhkkGxqEc56vLX7OiHzb8id9X7XLqtK94MKXjzYISMhYd-MGFnpbZcuWhM_hEpG0wxynVKdBADFZsheYm1O9eHdYeaUdB_gcyvYo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی این بنده خدا رو از دهه نود بکشه بیرون به زمان حال برگردونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82812" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82810">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZI1rWMYXm0P-LxVLWrxyhERgxuwzKSlmkqu2-XDyITe9Yol2cbexFEpSpA1Hsh-Ur1-6gNyKav6bmqK7X1If1yoLStMuGtf_OcqnjFLjgIZBqGGvBKz9W1yUVNZJVfZ8UK6GE5wQpEH10i1sfXYRqDrNkqV_2-pDIfGHzgfcyGzOAwEft4KN-Ajjbxb3rukYm7IfIhJhJWY-XlzrHOtjpS3GmeL42DbnUImkr6YYHnTpynw3vk5IbJZPdtUMHsyx-GFVV6-25XtYb2QojnS2Cg9hCmFlnux_uuiVtLL6ZLsIrTOWG2ETkl1LD9oLTI81ijXeBVcCZeHj79NJ53huEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید خانوم منظوری دارید؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82810" target="_blank">📅 11:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82809">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq42XVOyVYqsWYs5d_NVAp-PtMp3XiTuyjy5J25YM6lNDOM9yKfIEnOwIILIQOGZwkTO8vG4D-t9fx4bQuUvA-68KftXlbCM8oL0mjmGxHfjPk9_aGMbrumTAvugBAaZLtCc_ZlxeuG5JtasdYz4bgkGIWxqsU0NAwSpjCIPGhvDxD-fFLYelEtwbuJIkdLSMr-WQUQMGXZIPMaFcYNiMnqNv_DxQhgut854QRYY97NI2xn89VYFGO6PdU5KN_wTyBYfjRKApu3q2BALKyaWocWmeV0DObk_sdgv5RQdIdms7t_N4Bibru8TFir_MBTOtVpVXbkqCNncIb2qEcOAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیلی که باعث میشه بتونم این مدل مو رو از استاد بپذیرم اینه که پسرش اوتیسم داشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82809" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82808">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">میگن تهران زلزله اومده، ما که حس نکردیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82808" target="_blank">📅 07:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82807">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار ۲۱۱
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82807" target="_blank">📅 01:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82806">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/82806" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82804">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مجید بیدار شد داره از خرم آباد موشک میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82804" target="_blank">📅 00:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82803">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ توئیت میزنه میگه قرار بود با اسرائیل یه حمله بی سابقه کنیم ولی دقیقه ۹۰ جلوی حمله رو گرفتم و ترجیح دادم مذاکره کنیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/82803" target="_blank">📅 00:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82802">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مجددا صدای تحویل ذرت و جو آمریکایی در لارک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82802" target="_blank">📅 00:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82801">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#فوری
سازمان ملل:
این آخرین هشدار ما به تمامی کشورهای درگیر است. اگر دوباره دست به اقدام خصمانه علیه همدیگر بزنید به صورت شدید ترین حالت ممکن نگران خواهیم شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/82801" target="_blank">📅 00:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82800">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اونایی که میدونن امشبم جنگ نمیشه ولی الکی وانمود میکنن جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82800" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82799">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تسنیم: حمله آمریکا به لارک ۲ کشته و ۲ زخمی داشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82799" target="_blank">📅 23:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82798">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پرتابگرهای موشک کروز ضدکشتی سپاه پاسداران انقلاب اسلامی در لارک هدف قرار گرفتند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82798" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82797">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آمریکا پایگاه سپاه جزیره لارکو زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82797" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کوروش یه چنل دیلی زده همه رپرا رو توش جمع کرده
بعد یهو یادش اومده عه آرش سرطانو نیاوردم، رفته پیویش لینک بده دیده عه لست سینش لانگ تایم اگو عه باز یادش اومده اصلا زندانه طرف، پیش خودش گفته خب چیکار کنم حالا؟
بعد پاشده زنگ زده به زندان و صداشو ریکورد کرده گذاشته چنل.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82796" target="_blank">📅 22:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">می‌خواستیم به ماشین ۲۰۶ برسیم
آخرش به دلار ۲۰۶ تومنی رسیدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82794" target="_blank">📅 21:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82793">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACDlW90YyqGOWqpKbVgm8uq3CF2Nf4V3t2vjJFUgo_Wsf1JS25hh6CNohAVrvKn2i9CRLkUiu2-vpr-Vd-FKn_Fzaul37aEPhWotSZzycnZ72MNlRhBd5ypn5dIT86BeZsofiJhIK-x4cUHfBwGvDjfXAJq9dVVw-KgMeySxoR_HcYiV_YOWCjSmW0Mcukugq7dR5yREOeNrn63GYgM9ZcfM7gi4Jvu1QCy6QO3DGRzkdCXZE57eyqXF2mRUg_varoyYPJLiWEVmL9mBfeU3xJwE9O9uW_v0Z-NnmUd8nP6pjpuFzsFzDlgCSu7p_Qu1rEmOss0EKXBUch5pCwY0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه تاریخی چرا نمیرسه به قسمت تجاوزا محسن نامجو، بابا خیلی عقبیم بدو.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82793" target="_blank">📅 21:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82792">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gharibam Bahat</div>
  <div class="tg-doc-extra">Danial Moghaddam</div>
</div>
<a href="https://t.me/funhiphop/82792" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82792" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82791">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clM9lJXFrouibTPsiPTtSwqaEWwlXatOg2Fy5NU2zo_BY3RYyagXiw5KFPKcbBjdrr0wo_fLHQ8B-FrGkaSkazsMEj5b1Ii5ewM4IsgzmyhT92W0Tds8oupShmU6wGcZx7B6RYZFevbMT17PFVnrdxhsCwLXGcYk_eO3dV8tHf8sTHGt4gGP6VZiI8RRWYmW0au_VGFrmmaEWHgZs0Q3g48LvWCNqdgPMwhbLhhDDtx7CrVlCxA-KTz-tjfI4n1Pb6HtSCkOBGVH-dHom2XzycrWAzhKXkCD799ky-txW-ep3lXImwc6CUkVVJHrsrWC2sr1hmh1A2ONQkdYWqOY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید دانیال مقدم به نام غریبم باهات
از آلبوم خط مقدم منتشر شد
https://t.me/danialmoghadam3</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82791" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82790">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.   @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82790" target="_blank">📅 20:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=DnZOVJUpXqwJBhhAvDbGLo8tosfLRRHyqS58YCX1mK7df1RaXTL1dreyhbxgX70W_krAx8kJVA7sqRx1-2ysTsX3zrUkL28fuA2-_Rjh3vQRakw6oG-mJa2A6f9qQ2aypBBmJlpM_j0Kbv2wmLTkjn7lvmlNkXFdMINR9VcayOtzyVOGTbXNwHfUiuQJapG7Z0w-ck9RLhAvvsbN0Jwzc5HaCsqfmXt-QbBXGoMhMhizqICWYf3nzl-jgDxAcguSLBYqg77nLA1wIqEXnjVXRsLy1ZPBu81olbiApkzXaaxtRs1SVk97D7Fu7Zz9mCbpeYx7zq4LPyiJhrmODKAyXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d776d17fe4.mp4?token=DnZOVJUpXqwJBhhAvDbGLo8tosfLRRHyqS58YCX1mK7df1RaXTL1dreyhbxgX70W_krAx8kJVA7sqRx1-2ysTsX3zrUkL28fuA2-_Rjh3vQRakw6oG-mJa2A6f9qQ2aypBBmJlpM_j0Kbv2wmLTkjn7lvmlNkXFdMINR9VcayOtzyVOGTbXNwHfUiuQJapG7Z0w-ck9RLhAvvsbN0Jwzc5HaCsqfmXt-QbBXGoMhMhizqICWYf3nzl-jgDxAcguSLBYqg77nLA1wIqEXnjVXRsLy1ZPBu81olbiApkzXaaxtRs1SVk97D7Fu7Zz9mCbpeYx7zq4LPyiJhrmODKAyXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان می‌تونم به جفری اپستین برا خودکشیش حق بدم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82789" target="_blank">📅 20:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=Ykaucxu1jm1oXJ-svPBzyIRq7S6IUp2A-kug--jDriCbCU6tNzpRCO5HM-477MCa-d1Y1rgFdltpAO23F2tnIqPpWEDhz09SUIQVY9qv1cwXZqlk-nVON3HBQrQK6utuaWqjgPgcOg0wOYzLLLRa2GI5Wch2u7ELdOWsQqaQQXyMsOtHwZUES6YJAt-RU8F-8VpTnCUXKQpPhCsLZwa-13ErVwgQZvpyBwEOXquZNvd3bm0V8dgCH-bDYqOydaQgm8mEa70EtomUMhCQdr-E8GyOQf54yeIbmjLT-6umLYiEmlBBGkwIq9UO7R2YIvrRSR1D_7P8gKhwmaqLbr5fiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9b9dca48.mp4?token=Ykaucxu1jm1oXJ-svPBzyIRq7S6IUp2A-kug--jDriCbCU6tNzpRCO5HM-477MCa-d1Y1rgFdltpAO23F2tnIqPpWEDhz09SUIQVY9qv1cwXZqlk-nVON3HBQrQK6utuaWqjgPgcOg0wOYzLLLRa2GI5Wch2u7ELdOWsQqaQQXyMsOtHwZUES6YJAt-RU8F-8VpTnCUXKQpPhCsLZwa-13ErVwgQZvpyBwEOXquZNvd3bm0V8dgCH-bDYqOydaQgm8mEa70EtomUMhCQdr-E8GyOQf54yeIbmjLT-6umLYiEmlBBGkwIq9UO7R2YIvrRSR1D_7P8gKhwmaqLbr5fiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور ارشد و جنایتکار و نادان آمریکایی، تد کروز:
من بارها از ترامپ و دولت او خواسته ام که به معترضان سلاح بدهند، تا مردم ایران بتوانند با کمک سلاح، کردها را مسلح کنند و اجازه دهند معترضان این رژیم را از قدرت برکنار کنند.
هدف این نیست که سربازان آمریکایی وارد عمل شوند، بلکه هدف این است که مردم ایران این کار را انجام دهند.
تصمیم‌گیری درباره اینکه چه کسی در دولت ایران باشد، از وظایف ما نیست، اما وظیفه ما این است که بگوییم دولت ایران نباید توسط یک حاکم مذهبی افراطی اداره شود که از آمریکا متنفر است و تلاش می‌کند آمریکایی‌ها را به قتل برساند.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82788" target="_blank">📅 20:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dknOQx8ojOAON3X_hfEDafjDCEhqP4V6ls9qLrA9XvnKp3rKw-VqKf97OQ4Pv5GvYwisubiWxHyAZURiEZcCY23uQ9CKPWtx_DBGNxmiAcBl4sCAQ-xh6935o5dqN6xHfp-EL-Riv2Ilcz8IuDs6-Ai997oMB5tHZmE82yEaQehbwugYQvQXvcNtVANlRheG584ieui_5EZf71FxhaL6rctNovlB0sdYbh59mG7fZwi5PGjlK2JplMMXCusBDkUxbe8gWxESowT4gvHTT2BPDoDN8GkNYBk1cPrqBVE4CF5y-C7wLoSa3elHudhUziyFi5ON-XPoTM4-UhT2LvjzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82787" target="_blank">📅 20:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzzKY-g_G2tNm8DeXrWVBZr_znDbaTH84FDrCk66KXNlIc5RD8icc6vZ3P-fKhl7KWikqIZ-raNUwzeee33KcsY6bi0Q--o_YR80ImSkvSP5PjV9GoCG2vo_IFJ0CMA1LtC8I8lMCzHEd7z66u8Wyl3XCBHrF6fgSkC9ABaVRlkue0PNascO5_jZ2J2S_v_5CDLNWCE_rhkzKg_zYK3i3SiGgjhTqaAYMlFpsQTn6l_DAkqsefPnkyRMribua3hwDy8gytPvnp85cdE_8dYi0c6hYg2T9rUD1e4zIBx3B_gNMq-fldA1cQjRE8DYoGUDeTXkBBdJQgDNcrkiuE8Bsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زن‌نامجو: به بهانه بقالی رفت بیرون ۶ روز گم شد بعد دیدم با چمدون من ایرانه  مشتی حداقل الکی میگفتی میخوام برم مسافرت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82786" target="_blank">📅 20:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82784">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M14du9pZhIS5eQOwNl28TuGa1Gd9mSrjrfleiiFqIrovoLyKigwZ5C_lflPp52MlrRYRIVaah37aOiurNA3EmDUkMOBPEFOfD3WVcmhYLOanjuBavTLd7FuV7UFpSPMtYL3n9wldelkYV9Clb9ia07BINRfaZ1nCoQkw9k40cu9JAci_6ETLZK6IuLcGMi8gAN0o2Xs9I_VwF00hoGMwsxAPv26m64FFrg2oCL_7-uKHS244DuY9ICgIZKo-PxkdAr6YEhmxhwfRVF_TE5hN1YWL0CcHnK8LHjusAb59OLF9XojRDbxR__jkaPXGoxH2eD2IVsEAiFGw6zmh0006yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-BVT9ziLOpcYl5Gq6wI-lVvB0qcmC8DS5fA_nUwm244oWoonv_h-aU-im72vQgqlxMTqmKgTUSLRzaxQH-GAYWXSvOdlxYYytM0rxjZPUnuFKM10thG1h__7WA5Fkk9plfc7Cm5fip2dhB_AdEKnPZZZHMhYRt3JuFw61NI-dlKLxtWJRa8qeNaRp59v0ePx4cVs66yJ9Id4dWPlFMuyFxm3L2jpj2sap2hL5j65ANaGNSTRMUoJIiByfVlDYz0tg_5HvKjeKH1KBRVLNpRoGv-gDUzTAvqqprLraqNtSFPFY3yXl8NDW0L6FNcTklwZ8KAl81Mm38paiBuBgld1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتظارشون اینه مردم فتوسنتز بکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82784" target="_blank">📅 19:46 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
