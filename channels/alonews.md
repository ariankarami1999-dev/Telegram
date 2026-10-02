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
<img src="https://cdn4.telesco.pe/file/Q5Nx13nVKqasMosJi2mG6wDrE9levHdQiWiZ8Bf7Q_UVUMyQ_fTzwUBWIvmnnUdu8GMAxH_9PdxSi5p7Bid3EwcqpUxf-qy6Vf466aPKv5ikdFLrPf4Vt5zzR_lIS9U7d0Mj_0QZY5iUMj_hp7vfw7yXuZLW7_or8D_6_N04sZgfBeCO3H-ni_C5en4G38aQPpG6C7P6r2X0XWswWLOdbXjp5AqN6AGTzNevyxDEsslF1VpR9-cCArnrvDDG-EiqkWUadLRrh-n7KD65DzJbqajgC-uQj2MMiJWT4PxK07ekUByF1UQdLLRYASfMNR3K-pOgbGmF6Nf9h0PIQqxVXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 23:31:10</div>
<hr>

<div class="tg-post" id="msg-150641">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b51715eb64.mp4?token=jrJqUcBIeZtfw3_URFQ3UeGET2HFcVrhbJHpFY9iRUlhyKnkEkX2sd0nPcP6O6xyrIj4sSDsgubfxoPRXxwEyYuMEFsXfvH-Va35agkGvXVHUcarv5vM_e3MZY2dtqQ3Yra-MOeQ8yA1Ow5FseCMlUyDhh0MgZORDJcoUmxHfh_8yL4ArapoFme3m9LDsh30joCLCks1wzosTrneuUk7tVe_cuOk3VjTqsUaMJb2ah_whp1bt0oQssClO7HIsKy7BayKdiA8FBV-oJuf87ZlLMcI-jO2Gv7pqC2AvgL3XMEE_fWr5laLFoDQ_r5OJjg3VrrfgbaW_vRq9ni8FtfUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b51715eb64.mp4?token=jrJqUcBIeZtfw3_URFQ3UeGET2HFcVrhbJHpFY9iRUlhyKnkEkX2sd0nPcP6O6xyrIj4sSDsgubfxoPRXxwEyYuMEFsXfvH-Va35agkGvXVHUcarv5vM_e3MZY2dtqQ3Yra-MOeQ8yA1Ow5FseCMlUyDhh0MgZORDJcoUmxHfh_8yL4ArapoFme3m9LDsh30joCLCks1wzosTrneuUk7tVe_cuOk3VjTqsUaMJb2ah_whp1bt0oQssClO7HIsKy7BayKdiA8FBV-oJuf87ZlLMcI-jO2Gv7pqC2AvgL3XMEE_fWr5laLFoDQ_r5OJjg3VrrfgbaW_vRq9ni8FtfUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موج کودتای صهیونی در فرانسه به دانشگاه‌ها نیز رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/150641" target="_blank">📅 23:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150640">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کارشناس صداوسیما: افزایش قیمت ارز و دلار ناشی از هیجانات بازاره و قیمت واقعیش این نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/150640" target="_blank">📅 23:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150639">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ایهود باراک :  نتانیاهو برای عقب‌انداختن انتخابات، زمینه جنگ تازه را فراهم می‌کند
🔴
ایهود باراک، نخست‌وزیر پیشین اسرائیل، مدعی شد بنیامین نتانیاهو در حال فراهم‌کردن زمینه ورود به جنگی تازه است.
🔴
به گفته باراک، چنین جنگی می‌تواند به تعویق برگزاری انتخابات منجر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/150639" target="_blank">📅 23:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150638">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOWC6Ih94oohBpNlpXHR9NCMwq9-lhLFYiyDWuzSZ1P-OWL7DKseWgcSBFCXSZ7LwI1tncl26Helhh1Hgm3vRUgiLuYlFlq90eIbn-BnbZ-75g6oqe1Omn_A2QkSfIGnUfiVg0o-oTVrFcUSGrUq1YqLNtLWsymfshwcFSGQnYJd3K2A5oKFuRcwl_ziQKcFqGGbievsTq715wDsyGp3FgILgUIVjz3gPww5Oma4_KV91FuQSJyLAardncAirewAbV9HHQKcUXC1c-MjfFvxscfrXa_kPzEn-RLiM7SMY3yTqi7wV_oK8vouY0bRYtD__QDrgQeY4_wLerEtuA1MHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آمریکایی: بنا به گزارش مقامات آمریکایی، ترامپ پس از انتخابات میان‌دوره‌ای در حال بررسی «اعزام نیرو» به ایران است، زیرا احساس می‌کند «چیزی برای از دست دادن ندارد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/150638" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150637">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pktCtAIKXwYbTpe8acDd5ce3Zv83GAmNI7k5teDiNn4HfbwJO4KRgc96fvsWm9s17KVblE1GO0P2oHy4XuiE7O-y4r5bz9ZP3YiTmk4N8rZUPoXlbaBjfC4f63Fbs5dxpb2G_acRKgz8B5XJ4Skmtpz_8XUgR3JxThOSTvnorHaKvAebZzGCRoYRn1kgphobuS4agk-TjkB9DhVUyCiSKmE1QFW2d64ojHa_xv8aHwVnuAt53kAv3oTDwfExV5VZNQ09Y3iD6sEz4yffbi6TRKua1M-j81Cz25hvYOCyr-gG25KWZYAK9XflAe8sZuaBfVhQpEXTjrWXyLuMFoSLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در تجمعات شبانه امت معکوس مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150637" target="_blank">📅 22:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150636">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8uqx5yZpyNTShTnlewd2ww89TpRN7vLevXr7f_fp9CRugQyskJ_lJSFyUSH4GgHmf9aM5mOiIwx1YFxepB3f3j_fPO8fqnPxxRzFR3ExbwbrDwYWNvsJ-MqP06_wDUiZgnzsjCXnN6S3Uonj1VKYxnglRBrfuFsh1k3ZMx5XNG40Ae0M8hvZ5yo_CZT2NRD63BGccjy1t6mIleAzsCkl_d1504ClwCVaDQOJY9mQqGvbWldOsZ2BYXxen2y41YfMyKcgF_VtwS4P5QjjXkp7Uy7o-vVg5YEok0mmYH8XB8VWcVokFpuMsPsWZvgCiJchEkPOHNYUwUP0tLJwi3IAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت ترافیک هوایی در فرودگاه ریاض اکنون متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/150636" target="_blank">📅 22:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150635">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رویترز: مقام‌های اسرائیلی قرار است از کمک‌خلبان پرواز فلای‌دوبی بازجویی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/150635" target="_blank">📅 22:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150634">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
طبق گزارش وال استریت ژورنال، سازمان هوانوردی فدرال (FAA) اعلام کرده است که نقص نرم‌افزاری جدیدی که بر هواپیماهای بوئینگ 737 MAX تأثیر می‌گذارد، خطری برای ایمنی پرواز ایجاد نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/150634" target="_blank">📅 22:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150633">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
فارس: ترامپ به دنبال انجام کودتایی دیگه در ایرانه ولی الان خیابون‌ها دیگه دست تروریست‌ها نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/150633" target="_blank">📅 22:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150632">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بیانیه جدید آمریکا و تروئیکای اروپایی
‏
🔴
آمریکا، انگلیس، فرانسه و آلمان با صدور بیانیه‌ای اعلام کردند متعهد به جلوگیری از تأمین هرگونه مواد یا فناوری برای ایران هستند که ممکن است در فعالیت‌های هسته‌ای مورد استفاده قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/150632" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150631">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qduw32hOsej-rSNh2c9SQTFhEl1iuyQmMfDVCkI9LRYZBy2l3Fqm4YQj4SMcT88H5FKNoH3Nn-2JxMXSerzpPKRNfjN62I762hD846CGJi-0hoS2bMcz59Bqd4wLAOgTX0DBD0pdI1e2Or-2rMpXCeY7nbfwXmJrY6dZ6gsRZfzZH4V43TBl6mzw8mBnBtQC8exmK7cf0USTBPnLKz7AWeBKxrRGvYfS-N5QekThdD0443ocPCf3Tykc1S4odaD3pv7fHYLhD6dKXdfe3rQSbmosTw7PUyXXs1YGzs5nobpzHWoyyq6tjj7xnZliHVdRrbsrgfAdRM7mG7vJJUAsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایتالیا اخطاریه‌ای در مورد سفر به اریتره برای شهروندان این کشور صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/150631" target="_blank">📅 22:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150630">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آسوشیتدپرس: شواهدی از ارتباط ایران با پرواز فلای‌دوبی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/150630" target="_blank">📅 21:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150629">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رویترز: عربستان سعودی بیش از 100 هزار نیروی نظامی را برای حمله تمام عیار به حوثی ها بسیج می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150629" target="_blank">📅 21:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150628">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKzW4XsysN0B0nOFLfSbfivD__d7u3rr3rtkwWBsv1tmn0UAq8y1JTy4GB6kL2w7eBl8e5TWtY64VjYEuqj-MNPBu2GI-27lk6eRUh1wroH4UmdR0ZTHBrqWXIDujU4fsWbM7wcXMY3aJu4Hca11rYgD6qIjuQSB5qb9hdZAQjJ8M39bUegz8_ezbNedja0CNg4CsbJA6NvDAipyTKzftY4fo5PlKb1LPAi_Q3D5Q0qLzkuqs986U0wesWGmEIdz68osVOPYhEczgqpJhjn9EQ7XqZ3PpkF_GuH5WxgRbMN5AsHYOQBr7A83XdEy1JTHFiCtirqbRjAYoffrfztvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/معین خواننده مطرح اعلام کرد بزودی به ایران بازخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150628" target="_blank">📅 21:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150627">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=ZZK-g8G-95Fwx8-2f2auOBPwL2VWdtYjU9BvogrKiOkCBYl0ZUa_hgBenw_j7mRFzuhxNtIDa9sv3TqyoEJjAjJkGqPbkW7HJReFOgDjlgsl4TKE7xqMiym8XJauIL8wJ3MFEQAcqAI4TJIwg-QlMtWN2rk7JjnC5SH6Mw3LWu31X-R9WADZqfhmmZXZGFFBs7DXtRkDQtbljWX7PPbZ3_HjPBrkiTHrlqUXmEsRAtGo81LjWaEyxNLpw1vUd2bBR6mJaIExl1CopkePN1PHhUUyCDSQL2ht2xEPvcQiAcnFXavwELxR4fWFm4yMds8_J0q8NQng452AO1ce4jMfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=ZZK-g8G-95Fwx8-2f2auOBPwL2VWdtYjU9BvogrKiOkCBYl0ZUa_hgBenw_j7mRFzuhxNtIDa9sv3TqyoEJjAjJkGqPbkW7HJReFOgDjlgsl4TKE7xqMiym8XJauIL8wJ3MFEQAcqAI4TJIwg-QlMtWN2rk7JjnC5SH6Mw3LWu31X-R9WADZqfhmmZXZGFFBs7DXtRkDQtbljWX7PPbZ3_HjPBrkiTHrlqUXmEsRAtGo81LjWaEyxNLpw1vUd2bBR6mJaIExl1CopkePN1PHhUUyCDSQL2ht2xEPvcQiAcnFXavwELxR4fWFm4yMds8_J0q8NQng452AO1ce4jMfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150627" target="_blank">📅 21:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150626">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6527247c0.mp4?token=aO8h5TZ3-R8lS69wxZSw5S45YXtnwLUUSt8VslwsugnO7hjqzhGutwC4fIiVvvpeqE65jQCPnQ2W9FxNm4t5H8KULjWw9yLSMBXqlz45Io7hSfTV9DLcORxqvBTLv1NIxUZeWexESw0NQwifMhweJd2V_IOmat8k55DrE3-B0QrSU2yGZ3gzeNIwGKQyf3c_xp6QaJCw3oWI_VSgtk3m327s7VMuVpNGhQ_96V5kEOj6x4uE22EtBaDmb-N0W77q_vjD-GKSfr7l-obVSGBXEBtrB-2D3YoMzLcToUPoVDQFy0abhmpYglYT1RqmCYe_o8zGcQd6D5o33f2F476ztUsbSAGuI7V7dSF2ftasWparOFuTrqxyB1_wavw8kLIS372D-saRdvjd0STzGZJ7oJ6uc6LxIZbRvAv2CU1g2g0PBmDBcJtVbpmSD-RujegF7C1DoRv9UCFuSHfOLi2E010s1uAJAvtiisMW7-qV7Drd0MWRT4B1e3ZK0Gy1KRTDmJpMtnJas3OX77eCZ_NH4b-Ltf8zE4V8e7Fr2rab3CSsVpUE1h8BQngNPWjjBw9lE_Oysv5OssQuVE_6qKWTABeiGBLl78Ctp52j_SL6I1VfuWjYqxSDJz74mwW126gqKHv54y3JsyyuWMlAT-3MRERBeMohYzVLiRsdW2B554w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6527247c0.mp4?token=aO8h5TZ3-R8lS69wxZSw5S45YXtnwLUUSt8VslwsugnO7hjqzhGutwC4fIiVvvpeqE65jQCPnQ2W9FxNm4t5H8KULjWw9yLSMBXqlz45Io7hSfTV9DLcORxqvBTLv1NIxUZeWexESw0NQwifMhweJd2V_IOmat8k55DrE3-B0QrSU2yGZ3gzeNIwGKQyf3c_xp6QaJCw3oWI_VSgtk3m327s7VMuVpNGhQ_96V5kEOj6x4uE22EtBaDmb-N0W77q_vjD-GKSfr7l-obVSGBXEBtrB-2D3YoMzLcToUPoVDQFy0abhmpYglYT1RqmCYe_o8zGcQd6D5o33f2F476ztUsbSAGuI7V7dSF2ftasWparOFuTrqxyB1_wavw8kLIS372D-saRdvjd0STzGZJ7oJ6uc6LxIZbRvAv2CU1g2g0PBmDBcJtVbpmSD-RujegF7C1DoRv9UCFuSHfOLi2E010s1uAJAvtiisMW7-qV7Drd0MWRT4B1e3ZK0Gy1KRTDmJpMtnJas3OX77eCZ_NH4b-Ltf8zE4V8e7Fr2rab3CSsVpUE1h8BQngNPWjjBw9lE_Oysv5OssQuVE_6qKWTABeiGBLl78Ctp52j_SL6I1VfuWjYqxSDJz74mwW126gqKHv54y3JsyyuWMlAT-3MRERBeMohYzVLiRsdW2B554w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مکرون: آمار بشکه‌های نفتی که امروز از تنگه هرمز خارج می‌شوند، در روزهای اخیر بهبود یافته است و اکنون، در مجموعِ مسیر هرمز و مسیر یَنبُع به دریای سرخ، کمی بیش از سه‌چهارمِ حجم صادراتیِ پیش از جنگ در حال صادر شدن است.
🔴
اوضاع در حال بازگشایی است، همه با عزمی جدی در حال اقدام هستند و ما از احیای آزادی کشتیرانی حمایت می‌کنیم‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150626" target="_blank">📅 21:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150625">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a60b7a2.mp4?token=KfFhdIHlD6N4Wi1W-GO2kJLnyC_3LDAviSouHeHUHuCBomCfQHHsXYM4HTJKishKICbSO2ArGLKxieMtyf2NjAjBTx7OCwopbI_TrAVUA-C6tk4QqRLacdFUwBtMxxbyHoIz3nRxwhuOKVKgpI-aX9pg0XRQdkUa89Gg9BJWmZP_fnoCYIVz_4X45qtH0IDGDctwzRJgJUIY3SVTqXMtgeg7lSu2pSAySVBsLMt6UR_cU0ycViUJAZDDGG6NJfZNbt3f7NfXrzKGxmDU-r_0P9PKABFZOpdEG3-tF3TvsQQhd7wyUIdrebO4djO4g9jj6tWQPYxU_FvOJ08mTdfIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a60b7a2.mp4?token=KfFhdIHlD6N4Wi1W-GO2kJLnyC_3LDAviSouHeHUHuCBomCfQHHsXYM4HTJKishKICbSO2ArGLKxieMtyf2NjAjBTx7OCwopbI_TrAVUA-C6tk4QqRLacdFUwBtMxxbyHoIz3nRxwhuOKVKgpI-aX9pg0XRQdkUa89Gg9BJWmZP_fnoCYIVz_4X45qtH0IDGDctwzRJgJUIY3SVTqXMtgeg7lSu2pSAySVBsLMt6UR_cU0ycViUJAZDDGG6NJfZNbt3f7NfXrzKGxmDU-r_0P9PKABFZOpdEG3-tF3TvsQQhd7wyUIdrebO4djO4g9jj6tWQPYxU_FvOJ08mTdfIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150625" target="_blank">📅 21:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150624">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
رویترز: عربستان سعودی برای یک حمله زمینی تمام عیار به حوثی های یمن در هفته های آینده آماده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/150624" target="_blank">📅 21:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150623">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: عربستان سعودی برای یک حمله زمینی تمام عیار به حوثی های یمن در هفته های آینده آماده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/150623" target="_blank">📅 20:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150622">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رویترز : ایالات متحده یک آزمایش انفجاری شیمیایی غیرهسته‌ای زیرزمینی در سایت امنیت ملی نوادا انجام داد تا تشخیص انفجارهای هسته‌ای کم‌بازده را بهبود بخشد.
🔴
این آزمایش بر شناسایی انفجارهای «جداشده» (Decoupled) متمرکز بود که شناسایی آن‌ها از طریق پایش لرزه‌ای دشوارتر است. واشینگتن چین را متهم کرده است که چنین آزمایش مخفیانه ای را در سال ۲۰۲۰ انجام داده است، ادعایی که پکن آن را رد می‌کند.
🔴
داده‌های حاصل از این آزمایش برای بهبود مدل‌های علمی و الگوریتم‌های تشخیص انفجار هسته‌ای استفاده خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150622" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150621">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: نمی‌خواهیم درباره احتمال دست داشتن ایران در حادثه هواپیمای فلای‌دبی، پیش از پایان تحقیقات اظهارنظر کنیم
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150621" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150620">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRXKExQ2nAtSGdYWAck-wY5aIWcP5UfVfXd0oU3gHEI8xikVoEZ99ue_FMmDFpA7C7BeQEC6UZKNxzr-j0vUbwL2TWZTKsuPOrsLjb5xE9wfMYNXDkt_BVHeVBLNvoVQhU3qmzR6HG2IJt7agdfaMIbvZ_GPAlBUWIPCUMpb3M9d-1xK-wAW3Hjr2yU2B2Vk8YF8XNu-H4c52C3RNWZbgbDMxgJFJm86MO6-aHhQm5g882CYOgvjHY-hsNR9KpRKsAGK2cWLpUhZYhkWT3np7eIBAV1moGSFdqap9bHdJwnEhVOXkyBWUYxC49YwXhfCzHNlYiYuwdwFOTQGsEJHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مغازه در بازار سنندج
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150620" target="_blank">📅 20:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150619">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
المیادین: ارتش یمن کنترل رشته‌کوه راهبردی راسن در استان تعز را به دست گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150619" target="_blank">📅 20:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150618">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLDmFA2aopBPaf6e6NajU8FTJ_uAs-t_bHNdgeyEfDwdzdt0AgtBciJgt1ThrB00mO6qiiftluBeBUct8g2Bag-5qdoij8ayrp0H9FuPuwg9KzZQenZtAhU1C17CmymWYj5ShnyQ6MYgDPbDGkr2zA_WQO_ZjkFe75ZXxFTzIwAgU_zr6lx8nimpJwAiknnIJ5NUvprB9oUmMvsD1YyfBzuhoDylPDnho3ZD6RAmlAb-73Uduh8b8IqnJND5GcmhxQ0_GXlleI6H_8cW0F9E0uEBn1te78ygNcwuRfAf2ic8U7YFrEm8KuDvv-z6ilGKBrC3IglrJIW9JWJt6GoUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکانت مشاور قالیباف: تازه ترین اطلاعات نشان می دهد عربستان و امارات نقش جدی در به بن بست رسیدن مذاکرات 10 روز گذشته ایران و امریکا داشته اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150618" target="_blank">📅 20:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150617">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بریتانیا: تحریم‌های هسته‌ای سازمان ملل علیه ایران همچنان پابرجاست
🔴
بریتانیا می‌گوید با وجود پایان فعالیت هیئت کارشناسان سازمان ملل درباره ایران، تحریم‌های مرتبط با برنامه هسته‌ای همچنان برای همه کشورهای عضو الزام‌آور است.
🔴
لندن همچنین ایران را به «همکاری ناکافی با آژانس» متهم کرد و گفت پایان مأموریت هیئت کارشناسان، نظارت بر اجرای تحریم‌ها و تلاش برای دور زدن آن‌ها را دشوارتر می‌کند.
🔴
نماینده بریتانیا در سازمان ملل نیز مدعی شد ایران بیش از ۴۰۰ کیلوگرم اورانیوم با غنای ۶۰ درصد در اختیار دارد و آژانس قادر به تأیید میزان و محل این ذخایر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150617" target="_blank">📅 20:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150616">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نیرو زمینی سپاه : با جعبه مهمات‌های آمریکایی برای سربازاشون تابوت ساختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/150616" target="_blank">📅 20:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150615">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: نمی‌خواهیم درباره احتمال دست داشتن ایران در حادثه هواپیمای فلای‌دبی، پیش از پایان تحقیقات اظهارنظر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150615" target="_blank">📅 19:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150614">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رئیس مرکز ارتباطات مجلس: مجلس نه تنها هفت ماه بلکه یک روز هم تعطیل نبوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150614" target="_blank">📅 19:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150613">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgiS3QBNqp1vMOT7A3WY0tNXdqdcXhEvqiFAGMKSoI3QwOgEqswzz4zF_lzzgE84_JwASMNYm6mKPCTb4p4MxXlNyBMqX15rU0prHvkv8yUq7i94nC6vRfWTJOIXsMOy9-epJqlR14eruQjSqaRGkpbcnoraiDhpWVcPYinw9jZXec5O2gCj3goiideHANckm0dW36m7z_6JRM6JcX8cdqgLMCBzGHShzDUH8FAc4dzQi2PfxPqGXcFcrihWukdmI_E7rcZHz3bNeFZlCERydoeTK_1SSinboYW9wcWtlXf6jcOKkCWtBoq9OaJXoc4kl4UQRCnau8mjviC-HT7_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: تنها شخص دلسوز و راست گوی مجلس الان تو زندونه (رسایی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150613" target="_blank">📅 19:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150612">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
طبق گفته مقامات غربی و منطقه‌ای، عربستان سعودی برنامه‌ریزی می‌کند تا به حوثی‌ها حمله کند تا کنترل تنگه باب‌المندب را از دست آن‌ها بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150612" target="_blank">📅 19:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150611">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دیدار فؤاد حسین وزیر خارجه عراق با وزیر خزانه‌داری آمریکا؛ ایران و خلع سلاح گروه‌های مسلح محور گفت‌وگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150611" target="_blank">📅 19:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150610">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش هنگام خروج از تنگه هرمز بر اثر اصابت یک پرتابه ناشناس آسیب دید.
🔴
این حادثه باعث وقوع آتش‌سوزی محدود و قطع برق در داخل کشتی شد.
🔴
آتش‌سوزی مهار شده و کشتی به مسیر خود ادامه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150610" target="_blank">📅 19:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150609">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وکیل: الناز شاکر دوست به یک سال حبس تعزیری و محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد
🔴
پ.ن : الناز شاکردوست به علت انتشار استوری حمایتی از وقایع ۱۸ و ۱۹ دی به یکسال حبس تعزیری و دوسال محرومیت بازیگری، محکوم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150609" target="_blank">📅 19:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150608">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
بیانیه دولت عراق: برای انجام روزانه ۴۰ پرواز از مبدأ و به مقصد فرودگاه نجف توسط شرکت‌های هواپیمایی ایرانی، به‌جز ماهان، معافیت دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150608" target="_blank">📅 19:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150607">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر خارجه عراق: بغداد آماده میانجیگری میان آمریکا و ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150607" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150606">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ظریف: روس‌ها نه فرشته نجات ایران هستند و نه دشمن، «شریک ارزان» شرق نشویم
🔴
محمدجواد ظریف: «ایران نباید تمام تخم‌مرغ‌های سیاست خارجی‌اش را در سبد یک قدرت بگذارد.»
🔴
«چین و روسیه باید انتخاب راهبردی ایران باشند، نه نتیجه ناچاری و بسته بودن راه‌های غرب.»
🔴
«وابستگی یک‌طرفه، قدرت چانه‌زنی ایران را کاهش می‌دهد و کشور را به «شریک ارزان» تبدیل می‌کند.»
🔴
«روس‌ها نه فرشته نجات ایران هستند و نه دشمن؛ مسکو هم مثل هر قدرت دیگری منافع خودش را دنبال می‌کند.»
🔴
«ایران زمانی در برابر شرق قدرت چانه‌زنی دارد که گزینه‌های متنوع سیاسی و اقتصادی در اختیار داشته باشد.»
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150606" target="_blank">📅 18:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150605">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb6bE75gIE4Re4jbrRu10SvK6vvYjcBGrO_97pBXFsuhoz6qsfHJm1TAyVqokKmG-9GzRlpUiP0q_75Qb5QVillQKHYFW6jJZLMzX1i9xGLcMFzTZ-2UjAlckFs3oX6FnIb4aBCWH6XDgCIk4JHfj_Agn5-zfbW9LAeo0kliEiFGRfjkbSGvfVKhtUehCzGqjoJxScSWUy8h6diQ4erD_1grwig-P9JGpER5kQCr_44IT-8Fz6yEaFLtqfP3bkBsACVCLIBsaDeuqmPDcvvB7uLKuLHEmerIdyzV_I5eQ_iE-XqGw4xZt68UBx6-ep7ry_TKvBwKXYJ54CpqbTyq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ترامپ متوهمه و تو عالم خودش خیال میکنه پیروز شده اما واقعا برعکسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/150605" target="_blank">📅 18:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150604">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnttKbbEf-msLIidQbO7DdtAVA1gTGxxFXbn81PC4tUsdpbYV5K6cFyPDKAtJoRq_eSq3249aR9-axFSM_WMHrx_WxrVI9HiKd9lmemzMGjivfNPgo5FaHNYYcY7IMCohOxaNRM48uXYuHP3JwU3OFFrtgzymtcTfGjF_90ikgljJ86dHb9EzN7SsBfRq1L-zrDlrWYYs5NkQs9W6MNxJZIfDMtNEAe6nYCDKQNw6yauXCfT2Uzjj4U2Z7L20uAirBRWtivU6f_YLn-Le1okZe6QEc9f4FZ0d_9gjR5o7etlBSdq_F3l-_sQ7YlGr6y2CalfpAAKE-qiGJVaYfrUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امضاهای کارزار درخواست ابطال اعتبارنامه رسایی از ۷ هزار گذشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150604" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150603">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
خانعلی زاده: عراقچی آن‌قدر در نیویورک ماند تا نهایتا با دستور مارکو روبیو، او را اخراج کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150603" target="_blank">📅 18:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مدیرعامل فلای دبی: به درخواست مقامات، پروازهای خود به تل آویو را موقتاً تا اطلاع ثانوی به حالت تعلیق درآورده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150602" target="_blank">📅 18:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
مکرون: گروه 7 قصد دارد ظرف چهار ماه تا 100 میلیون بشکه گازوئیل و نفت خام آزاد کند.
🔴
گروه 7: در 20 روز اول، عرضه گازوئیل از سوی این گروه و شرکایش به میزان زیاد و زودهنگام افزایش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150601" target="_blank">📅 18:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
آکسیوس: دیپلماسی ایران و آمریکا همچنان در بن‌بست است
🔴
به گزارش آکسیوس، مذاکرات ایران و آمریکا همچنان با بن‌بست روبه‌روست. بر اساس این گزارش، ترامپ به‌دنبال دستیابی سریع به یک توافق گسترده است، در حالی که ایران مذاکرات آهسته‌تر، غیرمستقیم و توافق‌های محدودتر را ترجیح می‌دهد.
🔴
آکسیوس می‌گوید بی‌اعتمادی میان دو طرف پس از اتهام‌های متقابل درباره نقض تفاهمات قبلی افزایش یافته و فشارهای داخلی نیز مواضع دو طرف را سخت‌تر کرده است
🔴
طبق این گزارش، ترامپ نیز نسبت به امکان دستیابی به توافقی پایدار با ایران تردید بیشتری پیدا کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150600" target="_blank">📅 18:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njkn7ZDsqMITkX1kUX-Q0yY0ND3v1parsV7sAfnD0Yx-MRHyuols1S2Xu8ytU_wupE3Ozp1MSiy9Tl_DgATn5_JMGcTOhktYodzL4QR3rGg2M7GkfOxA502Br0gTL-GRrpIia4acYSYmRrT-ezMxiauD4MXGKDlPgVrX1WZzkrOmakj3BqFRjdrPx702a7y0CLbqDBi2z4c6yx3ovL1u_xj7qEdW-dxCvNPV0MvltwjSKBPox25PrUNRc-2LtNDYGgAUdShWTTUNyCCRSTlJQVv_LrDrLggFFi3zbpltGQMRE5c_94Ehm6PCn2cxMfsfeWqoO5w6DCVyci19-_0SyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از تسلط بر منطقه بنی محمد، حوثی ها به سمت الزعازع در شهرستان الشمایتین در استان تعز پیشروی می‌کنند و بیش از پیش به التربه، آخرین مسیر تدارکاتی بین تعز و عدن، نزدیک می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150599" target="_blank">📅 18:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHnbcrurtZ7eXB0RfDftuzRZXwkfmIMMzqLsQHkYDqDCZaQ2Mc-qFKD-0zqSODYWIHxJj3SNEy3ZZ9J0OfuvmHu7Zg8k6U27sv_j8F9NmdvYNMZjjeO89l38Hhli3Pn0lEsyBhhqkbpj-KKtdAWgTiI2bgRwcBKv8PIIj76HQctRib8gEbdtfKYPEmyX-cQZHU-KyN8WsE0DVMcVHC3IUJ8z9NzV2EDEJBOH8TljaWkwU-viaeS7xhb8hb51IKq_2E6ZbP3uVABy5dJYmyl1cZgSuYsjR1IqXGQPkDoYsODGpw2Sm7zcPehdByuJKRxW9MOe7kpwexo4RbC6t8NEXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت ۹۸ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150598" target="_blank">📅 18:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=SfZJ8KBMsfx9rRD8C9c9tHX881-GZ1mefqDFl8P2PhOSekFABsDTt-wZzE5AP-uSJVsOX_pcnBZWhTAVh5alx-vhaJRp8hDApBTs8gLf8YHe6oTJDeuZI_GOwAZSqvPc5txiqThivSnZTYrg7VPmPkyyZyWg3O_bycWoZqPrvIvgUrxGUoeVxK5ok5NHmQVW-gBnGOAeIZNoNSJjSCzMgrVEs4VKarc6PI3FNm6JpWV8cLpk4e68Q0J6VZ3u4NcqwjvuDKXz-kp537A1hQICeMWztUYh2y3iCOLd_BUKs-FdaBadFULVxpzIASzM4twWxwM9M4hFPkX59jmLyUEhng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=SfZJ8KBMsfx9rRD8C9c9tHX881-GZ1mefqDFl8P2PhOSekFABsDTt-wZzE5AP-uSJVsOX_pcnBZWhTAVh5alx-vhaJRp8hDApBTs8gLf8YHe6oTJDeuZI_GOwAZSqvPc5txiqThivSnZTYrg7VPmPkyyZyWg3O_bycWoZqPrvIvgUrxGUoeVxK5ok5NHmQVW-gBnGOAeIZNoNSJjSCzMgrVEs4VKarc6PI3FNm6JpWV8cLpk4e68Q0J6VZ3u4NcqwjvuDKXz-kp537A1hQICeMWztUYh2y3iCOLd_BUKs-FdaBadFULVxpzIASzM4twWxwM9M4hFPkX59jmLyUEhng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه اخوند تو تجمعات شبانه: در پیروزی ما توی جنگ و ابرقدرتی ایران تو کل عالم شکی نیست؛ الان دعوا فقط سر میزان ابرقدرتی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/150597" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / ترامپ: «اروپا همین حالا موافقت کرده است که مقدار عظیمی از ذخایر انباشته گازوئیل خود را آزاد کند.
🔴
این فرایند فوراً آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150596" target="_blank">📅 17:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سپاه : آماده‌ایم به هرگونه تهدید یا حمله، فوری و شدیدتر از عملیات وعده صادق ۲ پاسخ بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/150595" target="_blank">📅 17:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بانک مرکزی: بازار ارز رو مستمر رصد میکنیم و در صورت ضرورت اقدام خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/150594" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
انفجار جدید در تنگهٔ هرمز
🔴
شرکت اطلاعاتی امبری اعلام کرد یک نفتکش با پرچم پاناما هنگام عبور از تنگهٔ هرمز «هدف اصابت یک پرتابه قرار گرفته و ستون‌هایی از دود درحال خروج از آن است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/150593" target="_blank">📅 17:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
قیمت تتر در صرافی های رمزارز ایرانی به بیش از ۲۶۱۰۰۰ تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150592" target="_blank">📅 17:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
کارشناس صداوسیما: تهران رو دوباره با سنگرشکن می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150591" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
حمله با سلاح سرد به یک روحانی در رشت؛ ضارب متواری است
🔴
سرهنگ عیسی روشن‌قلب، فرمانده انتظامی رشت اعلام کرد یک روحانی در یکی از محلات این شهر توسط فردی ناشناس با سلاح سرد مجروح شده است.
🔴
به گفته وی، پلیس در جریان تحقیقات به سرنخ‌های مهمی درباره متهم رسیده و تیم‌های تخصصی با هماهنگی مرجع قضایی در تلاش برای دستگیری ضارب متواری هستند.
🔴
مرکز درمانی وضعیت فرد مجروح را مساعد اعلام کرده است. پلیس گفته علت و انگیزه این حمله پس از دستگیری متهم و تکمیل تحقیقات اعلام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/150589" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: بیش از ۶ کشور خواهان پیوستن به توافق مکه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150588" target="_blank">📅 16:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نخست‌وزیر قطر، شیخ محمد بن عبدالرحمن آل ثانی، امروز با وزیر امور خارجه ایران، عباس عراقچی، تلفنی گفتگو کرد و به وی تسلیت گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150587" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c27ba562.mp4?token=J0s0nSW-HRdVaDVZeEZ4MgA5zdsSejOuY0AoCBauZoX8MqUSfDrpvWz77Z83tgz4HORV8c9sjPdim07D2ziqGLqhTh8QX7XQ2s2KDtHp9Gtz7i0o9gUQENes0xFlOdwTZdAQkM82EpY2wxoYnq8Z1k5VeBRgkLCQO_2HdrFjksFqW8NXoCYldLL6z00P013j8R57vmaOeQR4CP1szmKLn-K5YFfOWsfkEcNoGpIfEmpKLKpLSnCn5y5sHDgc5Xjacw_NS97ruxdrWfD_aCv0oR5A6n1q_awnsLJPxnI5u92_4YGxN6CctK9XjpVzkvGKkWzM3XqcKhAS6aFZddRBIrQWq7y0y96hW-NBTvM_VlSg-n_gNts2EAP6J3O2ezdmFixwko1An9-PYaCMEwBfd617ccPEo7l5u_vpCPoaQxyfaVZ6Fk5mJRDv_TVzqF3_-kJ-g7HeAT-apetpC6fDOigVY-tljsgqpkNYs2roGSRNcWcyfuSwRdBTvl1KDbEfjU6maeNzxZKPvwK0k8z5tx7eupKQ4Cn1U92tfVun5YJ0FrSWzws2nScNGXu5fszi0nIUcHYmKuhEbjnP9GVavEQB9h2Z00CH_JCY3k9UNbeONIYKdwCBqRZrBfnjGBj2QoI1ZkLRcFW2lIe4n1nzY13ewwRK_GuisafbD21rFoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c27ba562.mp4?token=J0s0nSW-HRdVaDVZeEZ4MgA5zdsSejOuY0AoCBauZoX8MqUSfDrpvWz77Z83tgz4HORV8c9sjPdim07D2ziqGLqhTh8QX7XQ2s2KDtHp9Gtz7i0o9gUQENes0xFlOdwTZdAQkM82EpY2wxoYnq8Z1k5VeBRgkLCQO_2HdrFjksFqW8NXoCYldLL6z00P013j8R57vmaOeQR4CP1szmKLn-K5YFfOWsfkEcNoGpIfEmpKLKpLSnCn5y5sHDgc5Xjacw_NS97ruxdrWfD_aCv0oR5A6n1q_awnsLJPxnI5u92_4YGxN6CctK9XjpVzkvGKkWzM3XqcKhAS6aFZddRBIrQWq7y0y96hW-NBTvM_VlSg-n_gNts2EAP6J3O2ezdmFixwko1An9-PYaCMEwBfd617ccPEo7l5u_vpCPoaQxyfaVZ6Fk5mJRDv_TVzqF3_-kJ-g7HeAT-apetpC6fDOigVY-tljsgqpkNYs2roGSRNcWcyfuSwRdBTvl1KDbEfjU6maeNzxZKPvwK0k8z5tx7eupKQ4Cn1U92tfVun5YJ0FrSWzws2nScNGXu5fszi0nIUcHYmKuhEbjnP9GVavEQB9h2Z00CH_JCY3k9UNbeONIYKdwCBqRZrBfnjGBj2QoI1ZkLRcFW2lIe4n1nzY13ewwRK_GuisafbD21rFoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، در مورد حادثه مربوط به شرکت هواپیمایی فلای‌دبی: با گذشت زمان، ابعاد این ماجرا روشن‌تر می‌شود.
🔴
این فرد تحت تاثیر اندیشه‌های رادیکال اسلامی قرار گرفته بود. او قصد داشت با هواپیما و مسافران آن، حادثه‌ای را رقم بزند.
🔴
ما در حال بررسی هستیم که آیا او توسط کسی فرستاده شده است، و هر کسی که او را فرستاده باشد، باید بهای بسیار سنگینی بپردازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150586" target="_blank">📅 16:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQaOiQCQycQzOJsrE9im5dpJ4FCoG2ll_a5F2dg4R8vnOOHjhw1ZE4rjrNnLfZk5OieFnjVg7mryiK9--q9ZBuvOwTaCB_c7ku7FAsmU9zZygJJh2DmnMtWXCmKndNVMAhr6EAg57SXDIKT5EV0NkvbzGmlXU4rUx-u_xYBEOknrPPdIcR_lQv8-bHN8nmiulRT3hVxjLrFjpxHM5W_kdSEwBJvwyNRLCeBgRQKy9G8g3hb-6zp8Tb9xBapQfhvAkqXzi7yj7AggKTASCDGAXv8mA2ZgGCL9PQI-lFmbnmWdA8vDxx2v0QDvH0-2YubNaRcAjck6YzUiVWEiIY8hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: توافق با کره جنوبی همچنان رو به بهبود است
🔴
ترامپ اعلام کرد: «بسیار خرسندم که اعلام کنم توافق با جمهوری کره همچنان رو به بهبود است!»
🔴
او افزود: «۸.۴ میلیارد دلار برای پروژه‌ای جهت افزایش برداشت نفت» اختصاص خواهد یافت.
🔴
ترامپ تاکید کرد: «تولید بیشتر نفت و گاز به معنای سلطه انرژی آمریکا و تضمین امنیت انرژی جهان در آینده است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150585" target="_blank">📅 16:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150584">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b27a0f37.mp4?token=DcaKEQW9ythfN5ibPQWJvG84-485QIv8Y1e9CGmG8heXxtZ9_BnYsJrVeM_RSMaEvyWdCtoIvbR-iTcCKvDcZtMnrJW6vpVp9PvGxmbE5DdNW5TUmdocGKrYkJ5dWT7yQB4YbIMgLqVYwTmAJXLhBmcpXo8niPjQNdq-dSisFqoYlZLHv1gCNGoEhK9fgjDO1GtXrm8YzM-O0Mog8JrB4Cs4OSoXdKliQF28kkCgjslj29hNOaVwCdTEZ5CvaLvFqoHjDtnafBq2-qH6z5DsGX_QUUO1IaGx3PCducz5afZ20l_dc6pm2dCNy7V_MuICYCkjZgL2lddTTrDdnQgwWSsAMJyoYuM52ke41GPnCysJtAwWVsjCou18tBeGuHkHKrO_evpNzH57tdmw0fFfdaYB4ruXPIC-bizHLBXxgobDDqBLiDzO2BEfWb46M3HiU6cVkMpWReUA5xgbxb160S_m9JJze5EOKwAytROSa34sG7L4RAOVoX7LDBorpDE5ENrsg1F6ZkKQcQlffFsXM750waoPS5QX6pYDaEZHESrxiI73JUSrzI1dQA5x3Hb9E5uH5kgfy9Yx6B750R9rBxGgAAPNlvfWEHsuXtbCSZmtY-uO6QPTXldASw2v-kI-Encff8P2rEQ_QN6dp7QlP5MTTt-mqppJicT1l7UOVEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b27a0f37.mp4?token=DcaKEQW9ythfN5ibPQWJvG84-485QIv8Y1e9CGmG8heXxtZ9_BnYsJrVeM_RSMaEvyWdCtoIvbR-iTcCKvDcZtMnrJW6vpVp9PvGxmbE5DdNW5TUmdocGKrYkJ5dWT7yQB4YbIMgLqVYwTmAJXLhBmcpXo8niPjQNdq-dSisFqoYlZLHv1gCNGoEhK9fgjDO1GtXrm8YzM-O0Mog8JrB4Cs4OSoXdKliQF28kkCgjslj29hNOaVwCdTEZ5CvaLvFqoHjDtnafBq2-qH6z5DsGX_QUUO1IaGx3PCducz5afZ20l_dc6pm2dCNy7V_MuICYCkjZgL2lddTTrDdnQgwWSsAMJyoYuM52ke41GPnCysJtAwWVsjCou18tBeGuHkHKrO_evpNzH57tdmw0fFfdaYB4ruXPIC-bizHLBXxgobDDqBLiDzO2BEfWb46M3HiU6cVkMpWReUA5xgbxb160S_m9JJze5EOKwAytROSa34sG7L4RAOVoX7LDBorpDE5ENrsg1F6ZkKQcQlffFsXM750waoPS5QX6pYDaEZHESrxiI73JUSrzI1dQA5x3Hb9E5uH5kgfy9Yx6B750R9rBxGgAAPNlvfWEHsuXtbCSZmtY-uO6QPTXldASw2v-kI-Encff8P2rEQ_QN6dp7QlP5MTTt-mqppJicT1l7UOVEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«می‌دانید چه چیزی شگفت‌انگیز است؟ اول از همه، برخلاف تمام پیش‌بینی‌ها، ما سه سال است که در هفت جبهه در حال جنگ هستیم.
🔴
برخلاف تمام پیش‌بینی‌ها، اقتصاد ما با قدرت در حال رشد است و در میان سه اقتصاد پویاتر جهان قرار گرفته است.
🔴
و برخلاف تمام پیش‌بینی‌ها — و این مهم‌ترین نکته است — ما در حال پیروز شدن هستیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150584" target="_blank">📅 16:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150583">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: نباید هیچ‌گونه هزینه‌ای برای عبور از تنگه هرمز دریافت شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150583" target="_blank">📅 16:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150582">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
امام جمعه اصفهان: مردم آماده فدا کردن جان خود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150582" target="_blank">📅 15:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150581">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: کمیته دفاع سیاسی استراتژیک، طبق توافق مکه، به زودی در رياض جلسه برگزار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150581" target="_blank">📅 15:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150580">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Thaqleg6gxah6VFR8RSodcGIj24DFaqUAJ0g9QHR-ubdUvblCXpSpcYuDJVvm0KuYZKI_UR7uwapA5qlSD2n8_UDkW1Ez0FwlqGgPhQ9raofwPb8R6TAqJpM0UBitmqq4kIqc29lGmxcHORL_REWJyqCzbDznF3DM9Vl3wCsASOQl5zP23ONWIp96W1YU9KIXg878fyJPWudprAHuqpJgz3G4C6tby4pVwMNLpdmKd6I9qWm6KdmNs9r3rlT89pp44H4cJkouJkpK4czeCBzPvuQz7wu8jHxF0z-EeLK2t5QWKJmDy1ePfuNwkYF0OrJEFIhnIHsRKLttUaxLrhlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقاشی روی دیوار سفارت امارات در تهران:
🔴
این صدا از آن‌چه فکر می‌کنید، نزدیک‌تر است!
🔴
شب‌بخیر امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/150580" target="_blank">📅 15:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150579">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDg83clZqiV3rxXtbkXDQXQU7uQgaVJV9rE7gO71Wo_OUWOlCGWjIDKetX_Gr2rFTkNom_FguFw8NpZJrPtiwb4GM0T5PySoIgPStQz1qBaqJDc0n-RDlOaHMyLV5fNbXnnBvLbalAyeggKqZ7hey9yUE9WCRGaNnsViRiQnlvIDFJKdeptdeXGzNfTdYfZXDeKUdmgYOPZBKEoibk7ruTdxwO2gJS5MriPgdun19Vy8OwDWeNcnJDYjxpsPBWKGeRu4dR9PBmVhYEvgjfp8sseuJXSj0JBMLCBkIwnQhAKNtPb53nkxNufzZoK_PSCocBTOHxiWkhn_7hW7COnvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای باری نظامی بریتانیایی نیز وارد عربستان سعودی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150579" target="_blank">📅 15:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE-g3hAzeHomF3qhhS0AQ2rEE9J7uUfSiNhZTaHXjvomHeLMf49wouPTobZg5U47aq1FQ7V6VN5rm7D7cs3dmMkTA1Dryey6wKeJ-sU6_BvU-wacV9LGDfXAhrU03gMODnUqiAAys1ftaUiyArLqP2iEGTx6yI4VtQJaV0bjW9VoIHa4XhOzJp_6TrIVLEtR3t3ZowwCMW3V-X1O0e290xXZQIRDLgl4MZyixBpRRsw5HmFK0UV8BxvI52pFECrIxeJxxgEQSWgQHte6HW2srUayJVZEf-iXwDekqX3Du7vCK8db54DahUdjHuUBPyMHky85OTS1lFM7XyafVtOMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داماد سرخونه حسن روحانی: وقتی شما پوشک می شدید، روحانی و قالیباف و پزشکیان در خط مقدم جبهه بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150578" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150577">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
دلار 260هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150577" target="_blank">📅 15:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDR94LJtw4bHpRtDtNKmDQ5oMwYSKBJynr6FrKIa86fZrAWq13WcdfIMdgP7l6HgJY6K6hXj0wI-Pd6azEXPhPQ4gjK7oZzETD_yKmwXH6AWJk6sG-ntxJU26jVXqkcJtknVRfyjPCiufhCIvoyYHllfGh6mxQNlm4si7BkZYvBWoiE7LLGDsQpUfT_NjmNmWH1KJf5SpDIqOelnQ-UauvmN7hUIyC18nUGuDbD2Thy_fdE9mOfSmhhk92TC7_aAR4RYT-zn6FxooI80G3hOq-IxmthDqWf_ozGetYIPYUuP_kotU0f41BTALj1po0XOuPo5KBHYUiUSf0p4GYOQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: آمریکا تا ۲ماه دیگه بیچاره میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/150576" target="_blank">📅 15:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150575">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فایننشال تایمز: ترامپ در فکر حمله آخرالزمانی‌به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/150575" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150574">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ae8f78b.mp4?token=udcFnfZpVfK41NDwJqsvmw8GHDplNRF6wEx8MHZFHT6JBGEohZBb-eP72mH8m4FJE7LRDESMwGLgJnLxru1CnmqyraSaQ7xafNcpv9szHB6fGtx2tEcO4sJ2PvreVRIxkTEaGbYES5FGZEWyWpRkIQmwD0qZoTQc0uds8qFNBo1nGwRYcc3zKvdGy_CbSv18KGj7ku3XOOJhWnQozjYTDPKQK13ewE3bRTAdzLvmdpmxczYGHwqQrsYG2957FTE-kAuDqr4NG7noBG6d7J9PvHyVt0UJoGNX0vOwQk4agoQ-ZGUlJNLFFOOee7PFcpUxvTp_GvIjYYHh1C2KglRM9CZR4Pad3RCxtTddx-q3-VXReZmSLtNO4BPwN_PKanpn_b0Cu8N200h2oO0gZh5yDGk9nOgrRnALyBH2Xdj3CddQ2M5h_Z243f3o2SGfp6p6k_5bacH5FuAWbyWEh7KyYsxtoEGxaQTOC4AKOmZFsUwoVMg8bN7OY37CrDm_7eyXrkl3rm1XdelKvZcF2F1AjppVKqhSXAG5SfaAIJEYhrmeiJBnPZcwRnAwhrMYeSiVtXPIvbsNrtFWvMPIOjhAkAeLVSYncesG6w4ot4EikvN8lckB5_abr27BC2lk7QEuOoUu8M75EUOEEhlm3JUqsFrtBWQfkj3lv_7d0TbP8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ae8f78b.mp4?token=udcFnfZpVfK41NDwJqsvmw8GHDplNRF6wEx8MHZFHT6JBGEohZBb-eP72mH8m4FJE7LRDESMwGLgJnLxru1CnmqyraSaQ7xafNcpv9szHB6fGtx2tEcO4sJ2PvreVRIxkTEaGbYES5FGZEWyWpRkIQmwD0qZoTQc0uds8qFNBo1nGwRYcc3zKvdGy_CbSv18KGj7ku3XOOJhWnQozjYTDPKQK13ewE3bRTAdzLvmdpmxczYGHwqQrsYG2957FTE-kAuDqr4NG7noBG6d7J9PvHyVt0UJoGNX0vOwQk4agoQ-ZGUlJNLFFOOee7PFcpUxvTp_GvIjYYHh1C2KglRM9CZR4Pad3RCxtTddx-q3-VXReZmSLtNO4BPwN_PKanpn_b0Cu8N200h2oO0gZh5yDGk9nOgrRnALyBH2Xdj3CddQ2M5h_Z243f3o2SGfp6p6k_5bacH5FuAWbyWEh7KyYsxtoEGxaQTOC4AKOmZFsUwoVMg8bN7OY37CrDm_7eyXrkl3rm1XdelKvZcF2F1AjppVKqhSXAG5SfaAIJEYhrmeiJBnPZcwRnAwhrMYeSiVtXPIvbsNrtFWvMPIOjhAkAeLVSYncesG6w4ot4EikvN8lckB5_abr27BC2lk7QEuOoUu8M75EUOEEhlm3JUqsFrtBWQfkj3lv_7d0TbP8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع آمریکایی: تیپ ۷۵ رنجر ارتش آمریکا طی روزهای اخیر، تمرینات فشرده‌ای برای نفوذ و پاکسازی تونل‌ها انجام داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/150574" target="_blank">📅 14:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzypHmTPsOoou_J8EgarnZ696EkaOUreBRkJ6I3QcLCkztWQnL7uC5yC_zK08c-Oc_-2iRi0ObySi9GCpQNRUBLJI0XJsMP4DZC8lGLFCEWY3F2JQ1czFioKjzdvHDTikZnScHp45mPUOD0MQYlNVwTVeJrMT0M6AJgO0mL9kfatMc49Ru6RC_6bQq4_f3IZyixssGEQemfEospNBc7faBllqVZ8YHb_0tPC6HjJP0dHQqTuMWd_VGU4RHGx7T2P53bQ84DkC28iQnxmeI7mkwJ0Vs9u2GjnFjjWM5BnE_rRsJ76JZdKZ4aMFeqzo6zzLw6mT6w2squdDE2nei-4oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایتن لوینز، خبرنگار آمریکایی: حوثی‌ها ممکن است واقعاً عدن را تصرف کنند و دولت یمنِ مورد حمایت عربستان سعودی را به‌طور کامل شکست دهند!
🔴
اگر این اتفاق رخ دهد، ایران عربستان سعودی را محاصره خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/150573" target="_blank">📅 14:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awMYFDkfS4Zum0SUuZjC3ZZquV-cTuUxkI-vDlfV1O7J_QTAtTYXAiC7XW8Lc6ZAJ0uLFRGFdSU9kr89Xtki9qB5s0pHorK2HuhfQEBARu7nfJcxplK6nssJg-Fz5WLhmRnazb3UIG4Loh4JyfkomddDuwkCQRVvX231SKrJTICII3wc_m0DwD32ysG5HG_WoS9VYd7b8fSlXwGbWklQAHl-rgYfvv-KMJTK4Fdit-owD__pnScmhj7QFjDw5Yk37MNfCOKzXXIFc4VEJxM4fB12PDrAbPCsjIA7c2GBrLx_K1GXZJhAGowXrRz6ZqWcuQG2bpoueMkFx8SCs8VYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی میگیم کشور دست نظامی‌هاست یعنی این! گزارش رئیس سازمان برنامه و بودجه به سرلشکر صفوی
#کره_شمالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150572" target="_blank">📅 14:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
دیروز تو اصفهان زندانیای سابق با این لباسا و سلاح سرد اومدن تو خیابون و علیه رضا پهلوی شعارهای توهین آمیز دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/150571" target="_blank">📅 14:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150570">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIDzPdBHWG-eizd2RCbd7koBN9Kf_OduWjCxV2cSPcv8gozgcraeBrtnrw6wLE3vm1lvmhqumbNaQ2yImHQkNLu03Md7PK01297F8AfSTq296xjMOdVoWt_jqF0HHBdrrEMNulDGObBPosKhmgCl2BNDAkdYWParXoAAmsm5clIeslGhtyZ-C19uMTFcbhc3ZuWzbBVovfI33K-Tix8H5AiVwTFS1OCTgCc6_YYnVybnQhmA07OfCePoliAYo-OfmINQPGYzSbn8UxkWKpA-_aycJVd39MPmV9Na0-LAUItNBkuGnkszf0GB00tqhuy15rCMh3_r1VQk5SrUpqHkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقدی: انتقام حتماً گرفته میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/150570" target="_blank">📅 14:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوست داری از بازار نوسان بگیری؟ بیا
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading
کانال vip هم رایگانه
✔️</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150569" target="_blank">📅 14:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150568">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
دلیگانی، نماینده مجلس: باید امارات رو تصرف کنیم و باید نتانیاهو رو تو امارات ترور می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150568" target="_blank">📅 14:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150567">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ca4cea2f.mp4?token=fnY9xl72WtpKf4eHnsIVE8kksiUSSt6SpZv1v73FoqyrHbS8HvjFZEJtNScPo2bsoI8QBBgDS7fhUmnuVT7ZCzdqo5qX-rZzjJB4CXQD3SZTAB_1bMHqQKQM-WnXTf9qvAUYScWjpLhzdZ8EQMUV1jB0jDifuAsgdhwUlrO9dDlh4gQL9Fr8aObDhzXbn5i3FX7KSKnCkFIazLPp0qESKy6hyViqmpkoxOtDthu285bw2xpzw11VAwzuyy4ll74UzHvcD6JGMkJP8B7v25nVal16k5YYXYdqhCBt-1NU_7JLW2if36K1u4c9E_ShIMLCTCXBtXg6iFSbvOwMC8WXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ca4cea2f.mp4?token=fnY9xl72WtpKf4eHnsIVE8kksiUSSt6SpZv1v73FoqyrHbS8HvjFZEJtNScPo2bsoI8QBBgDS7fhUmnuVT7ZCzdqo5qX-rZzjJB4CXQD3SZTAB_1bMHqQKQM-WnXTf9qvAUYScWjpLhzdZ8EQMUV1jB0jDifuAsgdhwUlrO9dDlh4gQL9Fr8aObDhzXbn5i3FX7KSKnCkFIazLPp0qESKy6hyViqmpkoxOtDthu285bw2xpzw11VAwzuyy4ll74UzHvcD6JGMkJP8B7v25nVal16k5YYXYdqhCBt-1NU_7JLW2if36K1u4c9E_ShIMLCTCXBtXg6iFSbvOwMC8WXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگ زمینی تو راه ایران؟
🔴
ارتش آمریکا رسماً گفته نیروهای خنثی‌سازی هسته‌ای همراه رنجرهای هنگ 75، یه تمرین برای تصرف و پاک‌سازی یه تأسیسات هسته‌ای زیرزمینی انجام دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/150567" target="_blank">📅 14:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150566">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 26میلیون تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150566" target="_blank">📅 14:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150565">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / ترامپ: شاید پیش از انتخابات میان‌دوره‌ای، وضعیت اضطراری اعلام کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150565" target="_blank">📅 13:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150564">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wrg5joykiJsSgkgRzZEFnzjlrRY2I_dpuYs95B0k-7MYNMURieFYRoo7eMkwMl8tlJ4MVzqcOidsQd5Ne_rVm7mZUEnppPPG4UqXpU_l6r5KCWgVqDR2byV0E9BCBSMVsqSyLJeXtr34Ts49_ePBcrcq-CQDHu2qeUSrOwZi9XXeGil_sgx1kO81a7PBKscdOKSh2m6KBFpnT_otxZx18A6Am-Jvfr_Kle4MCSoWNhB0TIyVEordaoyaiNA6W7Emo67m5cdZfHkWWDqk8h1HflLLEAsZB1D6OPfnHk0p4EWOeDgEKTMrE4FodETUaR8a18zp_qhb10kEMeqN2KcAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روسیه یک فروند هلی‌کوپتر Mi-8 خود را با اتش دوستانه بر فراز اوکراین سرنگون کرد.خلبانان این هلی‌کوپتر کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150564" target="_blank">📅 13:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150563">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dieLaWpyJHUbaIutbEJMsnBqSWtlzHoPKtBDuAHe_YMbm-LiTG-JI8rOOdXFJrMGk3lWxdc77HN0ebo1iwk5-JUMGMx73o07J-ST5trVkxAOZwhAWdO70wXijTWgflBQTj8ULxR-C1Uoj7tUXZDEfrHpXhcJlw20dOR9P9nmM9lMQFaSaGTa21_yrypLGxmdHokONcXWgpXYBQPDJ40t-Y0xe-5lw6VOpUxy2i_SNimQSh-AV4QLeYDABKmbi2qsDIgSg9RphI9W2iNDiSnXVOh8NMGh_cXOopvhi81s91o6N5qz1qEVG6MlxlwRgB_KmIVMmOVLk4I2jmZwoAQTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیران دفاع آذربایجان و ترکیه، زاکر حسن‌اف و یاشار گولر، در شوشا دیدار کردند و بر برنامه‌های خود برای تعمیق همکاری راهبردی نظامی میان دو کشور تأکید کردند.
🔴
دو طرف همچنین درباره رزمایش مشترک «قدرت اتحاد-۲۰۲۶»، همکاری‌های فنی-نظامی، آموزش نظامی و امنیت منطقه‌ای گفت‌وگو کردند و بر تلاش‌ها برای حمایت از صلح پایدار در منطقه تأکید داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150563" target="_blank">📅 13:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150562">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
معاون وزیر راه و شهرسازی: ما برخلاف آمریکا که همه‌چیز رو تحریم می‌کنه، با افتخار اعلام می‌کنیم آسمان ایران بازه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150562" target="_blank">📅 13:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عضو سابق شورای اطلاع رسانی دولت: پزشکیان به این نتیجه رسیده که وزیر نفت باید تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150561" target="_blank">📅 13:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150559">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOtIws1sOozd7L_TOsUWMmNbAs9EqvAQ7kGoAYUDPNKUHmXBmLgb4NAxHDQmb25S4Lo9WTWAHDvYd-NXxPFXUiljB-c1QlA9L4s077Ci7nGh6xvafszbBevjfJzpoIsheQuvF98p6u4VxdudJdc2guwVKSTdd3xMXCsSKHJg_BiLTr-Zz0BKtiB7kEQXTzGALbOQfJeuQeQKJuA-tmnyMZgl4ngSo-_XEA16PjDW2jE-htjpUdfiR6jAyMQUvfw-r1PsE577MCXtro-7sjC7s2NSRLJpHEwV96fsY7v48wamO20i7tQR3xhqX37AXHzFAKbNl9BJ5M3KTKuLo5uMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک برای دومین بار:  اینستاگرام فقط واسه دختراست، اگه پسرید باید اینستاگرامتون رو پاک کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/150559" target="_blank">📅 13:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150558">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4irPOfK60PkLkU69LupKdUeeXUSZm9bJJy5g5VVACqNJHgiVJCqUB8swiAY6bJTYPPJhv3NQS2NjC08brrAF5ZneA07PoXfIUG0w2yHLpphjnhNrkaNMzJ9c6kzUwv0IunTHFdbOjwwBaxTHW67yukRfoUsUcuyNzyyNWbqh2Il_-k4R4w2EqY7JYWt0NJfPRPixTvOURuJoF2Q9Jm4Z05T7ak3lyMfp9cM4HkLFCaT2TyvpyiTlImmwg9PHogBq5dSe0EtVN_JSS7mHPCIW0iCLSLIc_isxaehk8t8z0Iw3CwZNzyvbkDgntyi_p2GjtwB6k4fOedyT1q9ey9VzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی: در جانفدا ثبت نام کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150558" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150557">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: ایران قوانین را نقض کرده و هرگز حاضر نیست از جاه‌طلبی‌های هسته‌ای خود دست بکشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/150557" target="_blank">📅 13:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150556">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
هواپیمای نظامی سنگین پگاسوس B762 ارتش آمریکا هم اومد خاورمیانه !!!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/150556" target="_blank">📅 13:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150555">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پالتیکو: اتحادیه اروپا برای استعفای «فردریش مرتس» از سمت صدراعظمی آلمان آماده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150555" target="_blank">📅 13:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150554">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رویترز: فرانسه پیشنهاد آزادسازی ۱۰۰ میلیون بشکه گازوئیل و نفت را ارائه داد
🔴
منابع آگاه از پیشنهاد فرانسه برای آزادسازی ذخایر گازوئیل و نفت کشورهای عضو آژانس بین‌المللی انرژی با هدف کاهش قیمت در بازارهای جهانی خبر می‌دهند.
🔴
بخش عربی خبرگزاری «رویترز» پیش از ظهر امروز (جمعه) در پایگاه اینترنتی خود نوشت که بنا به گفته یک منبع آگاه، کشورهای اتحادیه اروپا در پاسخ به فشار آمریکا بر کشورهای این قاره برای عرضه حجم بیشتری از ذخایر گازوئیل خود در بازار با هدف کاهش قیمت‌های رو به افزایش سوخت، پیشنهاد فرانسه برای آزادسازی مقادیر بیشتری از ذخایر گازوئیل را مورد بررسی قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150554" target="_blank">📅 12:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150553">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-OcYHuvODT6vjHdkVkR3NadLeZztcizfD8pqyWCQ9ZIH0dcBN0t3kQwN_3PKQgbVcqaN-MYMDKZp6G-yGMtwt1Epm6CpshXAAAhHBLflaX19gTBsRCsYFtzEIChkpnckXxyyOfxs8p6BBZ46a2Ni47gN0Z8mvO-JMYj3qpfsCmSQSi1H7aNlfEuy4lbThscK6H1DWhIvwmrlca8zyEE8f5YtHFR0qe_1sKzMDwLUcUReDCGHOCkDYAWw8cyOwLD_yT4q_7jmJHd9jDE_3GP8QNwIRZqk2L2pq7bHWVsOu3HCvHbv3aod8LiJC4Ut9R9iWQYkbKQvdjLXfAU7lmkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، ستونی از دود غلیظ را که از میدان نفتی عین دار در شرق عربستان سعودی (یکی از مهم‌ترین و بزرگترین مناطق تولید متعلق به میدان نفتی غوار) به هوا برخاسته، نشان می‌دهند. این حادثه احتمالاً در نتیجه یک حمله از سوی نیروهای یمنی رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150553" target="_blank">📅 12:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150552">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEliTeMI9IH0AXe5eMfr3GEH65VMCTPNEStVdSYgMLCKZCa7ho87hFZn3GkVXTAkMcHcuwdzoWUwizRXh1G-mZwivzQ9bbqFuiwdB96VENCdDYXdaWKXQqjWyg3kqMVxXPiovt7oPWApkoVzRzBoaHb27gTj65KNiRqCYQSz2KSf1Dgb6Mxc42cHIGwsKXEmcaqzgGWLkZEtzBWvld1pl3a9ye0iINiaB0v6p5lnRYF43sltbVI55BXcWMJMvS8oQvqv0j-8WStjUlZf0wH_hNqbT88v9oWUyUcnbIjr4KojXx99Mcea2JosbA3Gjzi_HUDE3C33t_HZTZ6qUrVrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی عربستان سعودی حملاتی را علیه مناطق حیفا، الکدحه و سامع در جنوب شهر تعز انجام داد تا از پیشروی ارتش یمن جلوگیری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150552" target="_blank">📅 12:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150551">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gof3f4G-u2KiEjG90rhv1IaqNQVvQ5fS9aNmbQXXjVlivfQJkDgC3GgJgv6FZnDRX_VbXfS8wiD8aCRNN-X2wddGeT3-G1rpRmR8Dh1ZyLAkCFjt4F82f4AS1OEqvQlbzpjYI8pKPzrA_cSUPCpLWfEhxfTHopjzOw0NnsYFfVs5eGlKd2EGjrLoXJSfPKzA-ysZVJKJZcOr1WDV472bFl9KzLACYLOxtNyHDbw37WapnHXUuPIMXQlH5Rv0TRuGxsvbhK7fm5-4Vbq9-WXEMhSESd-Z4nS9s47bewMQuZMPuDuXHdEnLw63XGHz8AAQmDDSmC-CbnrFzkoKzvEcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: حجم صادرات گاز طبیعی مایع از تنگه هرمز در ماه سپتامبر به بالاترین سطح خود از زمان آغاز جنگ با ایران رسید. در این ماه، ۱۳ محموله از قطر و ۶ محموله از امارات متحده عربی صادر شدند که مجموعاً ۱۹ محموله گاز را تشکیل می‌دهند. اگر این روند تا ماه اکتبر ادامه یابد، ممکن است شاهد بازگشت حجم صادرات ماهانه به ۲۵ درصد از سطح قبل از جنگ باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/150551" target="_blank">📅 12:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150550">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
امروز، سالروز «جمعه خونین زاهدان» است
🔴
آن روز بعد از نماز جمعه، تجمع‌هایی در اطراف مصلی بزرگ زاهدان و مسجد مکی شکل گرفت و در ادامه درگیری و تیراندازی نیروهای امنیتی رخ داد. بر اساس گزارش کمیته حقیقت‌یاب سازمان ملل، اطلاعات معتبر از کشته‌شدن ۱۰۴ معترض و رهگذر در آن روز حکایت دارد؛ این نهاد آن را بالاترین تعداد کشته‌شدگان در یک روز از اعتراضات ۱۴۰۱ دانسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150550" target="_blank">📅 12:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150548">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNOceFAiSsnDBMW39MG95_utBP0sjugOhEUHq4l_eoBX9SQrrGkU6WaukMpzXao43AAfFRjZC0AvqegRWi5qnW2mK9FCjWLCSdlSrrzEHOkBoOyPkvIcla3Yuir5ZyO8reCO7_crXHOsvILI36i-2IhDyP6Jr5TKleeMcoq1iYl0OQ-DWYwN1MzMzc5hkbOU4UW8zLznonKP5kug5eE9qC94RXetEw7S7br2I_0lHXuyoqWCM0CoWzTpnWMIWowBo6XbvXD7hUI2N85Pty95J6sczd0hxCAwNldfYFOZMiLJY4Jz0f2yFyEWImB950PvQm5xFCqiWGJ70IwPeuvQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
در اغتشاشات و کودتای فرانسه تاکنون هیچ کسی کشته نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/150548" target="_blank">📅 12:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150547">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219d012c04.mp4?token=fd-yFMRisK9xzU-HnXIVDrDqNOA7d1FC-4GhxETzsQIvGll9p6GZTyecHCcp--NqbUDOO_uja3xpYC0oaG75X1xkr6YhOWrk7UBa15uvqgEJf3IJauh9oSjrxtNqQNOyh4nBJr1ANbi8LCybb49XY3a1jKSPNYtGe_fjyI4DfSZH3nzyDwqJOCCY70pmpnQggTJmjg5yrPIKtZzFbnvKnOIZ6ZWuoEUS6Oqp7lMdYLw6a9LLBMA8z-_lXbck0MiKk4xzmT4vMgCYJQu2n2lnuLc_PET25UVELey-2yVvzYK5M2jT92cb-Zq6SgpWzNvnm461cI1-nvA-WKK8oQDJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219d012c04.mp4?token=fd-yFMRisK9xzU-HnXIVDrDqNOA7d1FC-4GhxETzsQIvGll9p6GZTyecHCcp--NqbUDOO_uja3xpYC0oaG75X1xkr6YhOWrk7UBa15uvqgEJf3IJauh9oSjrxtNqQNOyh4nBJr1ANbi8LCybb49XY3a1jKSPNYtGe_fjyI4DfSZH3nzyDwqJOCCY70pmpnQggTJmjg5yrPIKtZzFbnvKnOIZ6ZWuoEUS6Oqp7lMdYLw6a9LLBMA8z-_lXbck0MiKk4xzmT4vMgCYJQu2n2lnuLc_PET25UVELey-2yVvzYK5M2jT92cb-Zq6SgpWzNvnm461cI1-nvA-WKK8oQDJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار هم اکنون 259,900 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150547" target="_blank">📅 12:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150546">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0ddVttuE3FB2sf-MUeFR5g5C4aORqcj4-FeriNKEPAwWsoCh8l4woi66wiEIY2VRqq1fzTR0M35gbJe6qBocKEj0WIYQ6Og0qeAc3V97KoFvWjd7McQnPVBBuqwEsQiTw_DsQKpxap98viozw3kIY_lU-7NINlsBe1tdYnROXWyo4BvT2Og5UoP0Ax6lXs3d0IYA5r3hseX6-k3JxUNX1bO-NRPyEWqPOsnqy5aqBFEFFVR7Idpa2pfNqrGduzfZRAJfzxvoYEPCiJxCvGwCNKdbGUi9TqeVxYZlAhKgMdZ16OtMr6sPolHOTou6EwVadGl7zgX8lOJ_J32JHVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین دوباره ۸۶,۰۰۰ دلار را پس گرفت و در تنها ۶۰ دقیقه، ۱۲۰ میلیون دلار از پوزیشن‌های شورت لیکویید شد. در همین بازه، ۴۰ میلیارد دلار به ارزش بازار کریپتو افزوده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150546" target="_blank">📅 12:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150545">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بزرگ‌ترین خریدار LNG جهان: انتظار نداریم LNG قطر به این زودی به بازار بازگردد
🔴
فعالان بازار نگران زمستان پیش رو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150545" target="_blank">📅 11:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150544">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=dcm2GgAzq_hTaJ_2nveuNXJeEezfXYoZxAZ85fr7C-TlKj0P_K8Ei-OhWnbvIHX9UvLg-C5w4YZIMCH-2V_CbDaWOI3KNjcjg3RiK0fddMH2YK-ow8rJsavO_OSq_SwshEfOvuffB8xzUMu_nK64EsG6nj_OfFHc56zc6OYxEqma1BiLjz5BMnB1LnEsiveJpNsR8DhjJPL7oa5SkFDMZ_46-T3lCxpnI2BJZntHU8cdWenHauS_BRrJSPW_fbv5QL2Zn4I1fi7PimD-C05yse4V87VwxSxRi89-4Iv3SpLiusSOK-lnrrSGGDHwGc8oCBcKwmQ2ofEpmS9A-7ilQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=dcm2GgAzq_hTaJ_2nveuNXJeEezfXYoZxAZ85fr7C-TlKj0P_K8Ei-OhWnbvIHX9UvLg-C5w4YZIMCH-2V_CbDaWOI3KNjcjg3RiK0fddMH2YK-ow8rJsavO_OSq_SwshEfOvuffB8xzUMu_nK64EsG6nj_OfFHc56zc6OYxEqma1BiLjz5BMnB1LnEsiveJpNsR8DhjJPL7oa5SkFDMZ_46-T3lCxpnI2BJZntHU8cdWenHauS_BRrJSPW_fbv5QL2Zn4I1fi7PimD-C05yse4V87VwxSxRi89-4Iv3SpLiusSOK-lnrrSGGDHwGc8oCBcKwmQ2ofEpmS9A-7ilQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: وقتی به پرونده‌های منتشرشده اپستین نگاه می‌کنید، فقط یک چیز کاملاً روشن است: بله، این دونالد ترامپ بود که جفری اپستین را به پلیس محلی معرفی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150544" target="_blank">📅 11:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150543">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsXwwmVBO_nDgqFly8U1ux22kRANXGw5QO9HVw_2GvD_CMDFBb19vbm79TUJAwsFWImuizXOcsPKJFbMBGDQCIzkf9wEuiQ6t5xp2gKDWqQUo2zuZs0VMYjxrI1Yp99cmXn__5bbTwHBfwtFXUiwwCqisF5DsbV0c-29P57ub1cds8B7wgtR7cN3tOLZJbSCrIwXqSwkEn6L23LJvr6bnHuw4jx96ssD6nv5goi7r0kbmpMxjwW5t-NhK15VUBMjQ85DsCXiVi7nfSbD9Dj31qMHWFt5cGPlIDHF5W3e5tcKLdmr1AiybHjLBmyFhI_mMJmNLG_IXRYf4uZwBxj4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جکسون هینکل: سفر مخفیانه نتانیاهو به امارات مقدمه‌ای برای جنگ روز قیامت علیه ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150543" target="_blank">📅 11:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150542">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=Ur5BjbBmmQa-a6ohv8UgTq2THeNFjWyhulw9VAvWih1T9zrTOkOnfmvKKEMoQerQRlPm8R40R33kCMIdVMkqHimhsmLcSsd4f4S9KgaC28jAT-67ONd-aaxCTdaHxdLVL7sq19zlozC0qSEM534-lLQfTZYivD0SDTwMCfdn7x8p8CaJDbltE6NH5FInz4F1IUordZES0fbCyBKmzfwURCMpFNf6x-CXl6nnXUpSz2Hx3Cv3U2LNZ7fBsOSoYrHG74Vzop4ehTAY6gNskIR-1u7lgir5wX3NbVjcbO5PCoyyJer6pMIlIFwC7RLlf4KIdTMxVV-5G_kYtfN2gLAqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=Ur5BjbBmmQa-a6ohv8UgTq2THeNFjWyhulw9VAvWih1T9zrTOkOnfmvKKEMoQerQRlPm8R40R33kCMIdVMkqHimhsmLcSsd4f4S9KgaC28jAT-67ONd-aaxCTdaHxdLVL7sq19zlozC0qSEM534-lLQfTZYivD0SDTwMCfdn7x8p8CaJDbltE6NH5FInz4F1IUordZES0fbCyBKmzfwURCMpFNf6x-CXl6nnXUpSz2Hx3Cv3U2LNZ7fBsOSoYrHG74Vzop4ehTAY6gNskIR-1u7lgir5wX3NbVjcbO5PCoyyJer6pMIlIFwC7RLlf4KIdTMxVV-5G_kYtfN2gLAqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور برزیل: ما اکنون نفت در حاشیه استوایی کشف کرده‌ایم/ ترامپ از شدت حسادت، تلف خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150542" target="_blank">📅 11:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150541">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
معاون فناوری وزیر ارتباطات: با این روند، در بحران بعدی مجبور می‌شویم علاوه بر اینترنت، برق را هم قطع کنیم!
🔴
به دلیل نفوذ استارلینک
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150541" target="_blank">📅 11:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150540">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2b8312ee49.mp4?token=IyqyvfDaTOfmjEhbqfiKgWjbHNnoUfAu4u5Oct0JXIUi5-8HQjAz_lAKUCNoQKlijNLfxxMuQA-j6yGEDOOMwd_ZHcw0P1yvXBTpcmOkb4C7b91fNCCWLh0BpO1Mz7dawiyc7PtM9prKcifAGUKoh5fk-POi3qKnWeHdEUoK4Vz_QNxDZOLcZzwGGVepz-bgAUf5Hje9Yoic0tBKsOxOF7YgP89t4rCQeFn3lVlFBPPQETVYY9OJAPh-bJOEf09M9jkSwdlhYqLqo_vtA4gZJnjZtMzI8VIBnvWaJfCePF6wwOBSaPLveHbiR0ar_upA41In42fvgXBUsTCky96fhIQET-CZVEtqu92SnFJCa-nw1SO1xAw_6ru-o2qoc8l0Nw6G4RPaOgS2kCPH4z3nRS2gfIyXhjQG9wUvPtH5bQlPX_UVxXI39SCxOFUyVr2khEO3RCvSbFaCUrFm-grxCSRPAIwSxfgabA1dLCgW_PnkOcR0fM_WnRpLpRlHL8C5FeIHk7_8p-O6ArbclEFit1S-PVKfX1kR2WpMADkLLXqLx9Y78HPczc-bwa2CJpHFsf-HW80wfqUfgsDdfhJp7UmfnLg8tTsJDyRM0g225tT4r0p6-914-0CJ6cJFvgXHpxH-MJ-9cWVS385iMwKyfkkzjhVmeVnpSl2oSn8-7u0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2b8312ee49.mp4?token=IyqyvfDaTOfmjEhbqfiKgWjbHNnoUfAu4u5Oct0JXIUi5-8HQjAz_lAKUCNoQKlijNLfxxMuQA-j6yGEDOOMwd_ZHcw0P1yvXBTpcmOkb4C7b91fNCCWLh0BpO1Mz7dawiyc7PtM9prKcifAGUKoh5fk-POi3qKnWeHdEUoK4Vz_QNxDZOLcZzwGGVepz-bgAUf5Hje9Yoic0tBKsOxOF7YgP89t4rCQeFn3lVlFBPPQETVYY9OJAPh-bJOEf09M9jkSwdlhYqLqo_vtA4gZJnjZtMzI8VIBnvWaJfCePF6wwOBSaPLveHbiR0ar_upA41In42fvgXBUsTCky96fhIQET-CZVEtqu92SnFJCa-nw1SO1xAw_6ru-o2qoc8l0Nw6G4RPaOgS2kCPH4z3nRS2gfIyXhjQG9wUvPtH5bQlPX_UVxXI39SCxOFUyVr2khEO3RCvSbFaCUrFm-grxCSRPAIwSxfgabA1dLCgW_PnkOcR0fM_WnRpLpRlHL8C5FeIHk7_8p-O6ArbclEFit1S-PVKfX1kR2WpMADkLLXqLx9Y78HPczc-bwa2CJpHFsf-HW80wfqUfgsDdfhJp7UmfnLg8tTsJDyRM0g225tT4r0p6-914-0CJ6cJFvgXHpxH-MJ-9cWVS385iMwKyfkkzjhVmeVnpSl2oSn8-7u0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تایوان نخستین ۲ فروند از مجموع ۶۶ جنگنده F-16V Viper خریداری‌شده از آمریکا را تحویل گرفت.
🔴
این جنگنده‌ها در پایگاه هوایی چیهانگ (Chihhang) در جنوب‌شرق تایوان فرود آمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150540" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150539">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
آکسیوس: گروه آمفیبی، نیروی دریایی پیاده‌نظام و گروه اعزامی دریایی سومین گردان تفنگداران دریایی، از پایگاه دریایی سان دیگو به سمت خاورمیانه حرکت کرده‌اند.
🔴
آن‌ها حدود دوازده فروند جنگنده F-35B و همچنین حدود 2200 تفنگدار دریایی آمریکایی ویژه به همراه خودروهای جنگی پیاده‌نظام و نفربرهای زرهی را به همراه خواهند داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150539" target="_blank">📅 11:25 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
