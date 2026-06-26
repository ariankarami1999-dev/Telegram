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
<img src="https://cdn4.telesco.pe/file/LyLoFLyYXGeMF1-U8Rc7d3TONzdHlDAb_OXp7RWjoBOWu16lwyqF7RpJGsu154LhCmF3zrOPD5ipwKIBtgmzUILn1F10Z3uK6e1XFSPX-WoY691eJuRQSephI2_uEEcbMq_1Fu-qlspNxzpTVfRRjw4S7zN70bk8Ft2BAZBlAd_XhAjUUYVa6kWZrx6g6sHRJQpDEL_zle7qdhbehh4MVVV3Iup9m-EDZjwjKr6Jebz_EyVYDmH9D3iM2OyH2OCLtNfi32rWImI7XKsk-3IJn2lfR-BigLwNtsi5F8X-Ca-QzZs9o9cCsxb2uNuAeca9GqpU5cJ3KENa-gdgQ6lyOg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 13:45:33</div>
<hr>

<div class="tg-post" id="msg-17999">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/17999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_394
🗓
june 26, 2026
✔️
تحلیل گزارش PCE آمریکا
✔️
بررسی تقویم اقتصادی روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SBoxxx/17999" target="_blank">📅 12:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17997">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwxwkTcNZulxEXnmzPkCCAUh1e-gsxpIAluzdSv6F8w9o5tR5iTDMjEwGSlj03bszpXiDZAH7eDMn6bnlv_s13MYSgb3iQlmOwoR8PDBadFeA2S3McGUYlwGY0huebvX0qrALtVQXzYjFqMzxcI4HCLnA7PG9I6XZtE6C6vSwer42gU8NRzW65Ckn6S5aLhoeXNVaf8FwVG_rm1K2b6dH2d3DVFTjFBdHjTqLp3PYy7KhBB7ALABFzbmU5N9vftdIlZ7D-v28JJ0WYUcuxtyA3GCdpD8pve0hzBIsUCGpaKnngXiGUoyZTMAioME1n_NWw-QIshGmK-Y2cfaK59hHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWvsOsdUV-eIl8O4fd4jRpWeYOUcDUVBsetGN3RmLrOfm0ViyeLizUQgCt_oSHzqFwCpKqxXzjh6Q-SYx-dl0t_40aSF7mD2BednoK-WKDeTxGKRhZwJlUNfZz4tF4duTduvRlkUwZXG17bLWcGIj_G6gYLTzEaD7Nm_vOQz-wrPaJS0YFBw5QA0IZDs68qhhH6xGfHXObiJoezH3Cr3TqLLWMIZRvk01Ptx6zCC_fvsxPc5YruTcdmqyz6H-iMLlrBb_dOkAx9IPy5iCNW_hS_XbV6ROnmdPprBvr17iFQ5wjooW6KU_LcMaT_uAGyLKnwxqTFpAt7bT8w1UPVJ7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه وزارت خارجه ضد مواضع مشترک آمریکا و کشورهای عرب خلیج فارس</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/17997" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17996">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پنتاگون در حال بازنگری در استقرار خلیج فارس است و جابجایی نیروها به اسرائیل را در نظر می‌گیرد
طبق گزارش‌های رسانه‌های آمریکایی بر اساس تصاویر ماهواره‌ای، ایالات متحده در حال بازنگری در وضعیت نظامی خود در خاورمیانه است و در پی آسیب‌های گسترده به پایگاه دریایی کلیدی بحرین، جابجایی برخی از پایگاه‌های خلیج فارس به اسرائیل را در نظر دارد</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SBoxxx/17996" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17995">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بیانیه قرارگاه عملیات مرکزی خاتم‌ الانبیاء (ص) :
تحرکات و حضور جنگنده ها و هواگردهای ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران را اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/17995" target="_blank">📅 10:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ حرامزاده تا کنون همه ملت ها و رهبرانشان را — از کانادا و مکزیک تا اروپایی ها و عرب ها — تحقیر کرده جز:
— چین
—ترکیه
اولی را به خاطر قدرت خودش و دومی را به دلیل مجیزگویی رهبرش
برو قوی شو اگر راحت جهان طلبی
که در نظام طبیعت ضعیف پامال است</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/17994" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17992">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یونجه و سویا واسه من
تنگه و دریا مال تو</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/17992" target="_blank">📅 10:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17991">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بوی گندم مال من  هر چی كه دارم مال تو</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/17991" target="_blank">📅 10:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17990">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">#نمیپذیرم</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/17990" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17989">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ:   ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟  برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/17989" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17988">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ
:
ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟
برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/17988" target="_blank">📅 09:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17987">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">📡
ترامپ فرمان جدیدی برای ساخت کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ امضا کرد
دونالد ترامپ با امضای دو فرمان اجرایی جدید دستور داد تا تلاشها برای ساخت یک کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ سرعت بیشتری بگیرد
این اقدام با هدف تضمین پیشتازی ایالات متحده در رقابت با چین در حوزه های هوش مصنوعی علم مواد و شیمی صورت میگیرد
همچنین آژانسهای دولتی موظف شده اند تا سیستم های حساس خود را تا سال ۲۰۳۰ یا ۲۰۳۱ به رمزنگاری پساکوانتومی مجهز کنند تا در برابر حملات سایبری آینده ایمن بمانند</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17987" target="_blank">📅 01:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17986">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17986" target="_blank">📅 00:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17985">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBdH4kxk7HaBJQH-NWrCx_x2C8fzTKhL_invrEDRVPl6k3zb1e5aPJ_PZTdTXs5eRZ8IpyKys5GtSlWp6AwPvBv_gWn8HCAeBBV8Ef6VDNtjO1qybTNLyICEBu_9DxdYDRDNJsFCMuI6HpyGxyeRIg5KaxrYEszcr8xRWRc-sL57jcuSKKbwmLQczbgMg52xF4vNJHW2KUoAxgtsv6oMbKCSMa6Q-d6TNQm83dlHcvPAee0nswhgLfAnlINmEk-gZao01EzAYD3aabMkTjcaX8mXwLAhSoSdxx5Vzw-1Ec_wdjJi7QcIH5b8N0kn-uT_70oprly2fyTBw7DKO4mSmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا پس از انتشار این گزارش، حساب بسیاری کاربران ایرانی مسدود شده است</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17985" target="_blank">📅 19:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17984">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.  @Milita_Camp</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17984" target="_blank">📅 19:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17982">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17982" target="_blank">📅 18:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17981">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7wmvzZ4WRUS9J3bsPRiTuRHoEFeb2CtpK4XtnyfQSYHu5GY0Ng4h4gT16ZWdC1HrfBLds5v1BkL6Jh6-K-CBcp7XoBPt8hk3jiVcfzKtnb-27PDthobXG2C5eG1hRk7w2F2Lt_fjObx2Y3Ma94iOqg2Tc4oT7yBFOL2H_hVbqsLnXPgBvNi69e3naCWF4RUsXXrj0RO5UNfhe3N28koIXgjvcfofOFmDQFd0krPHaJtSfjdugojPUEFW2Ztn5Gf9mZH2yCRTOGKRkW9GCHL3RspBNTRQ-JhL5TnzXeigmVZq6w1wapxLuLOnZQRiAlw20f1ay_IcaNKCvlbqbNMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- نیروی دریایی سپاه پاسداران انقلاب اسلامی با یک کشتی در فاصله ۷.۵ مایل دریایی از سواحل عمان درگیر شد.   این کشتی تلاش کرد تا از تنگه هرمز از طریق مسیری غیرمجاز و بدون هماهنگی با اداره تنگه خلیج فارس عبور کند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17981" target="_blank">📅 18:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17980">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17980" target="_blank">📅 18:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17979">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVyqK4-UrdCOf0oUp6gzGeP72ehIZ6Y1lK7TIO4LYnfkf-QiXWGHp_LMp3mTrN469lsEHZ9hUvzGziNplRu_BD07Evgo4hTHmhHzxZKyCQU9tPGeYIFRfA1qWMaeowNEwhVsGrD5Dz4JzVTbzC4Q-AujprQPLo5qPFTn3n3FlThjSsiurSAfMr_W_d6suC_KjoU_nXZAl1YlCywVFBcrtQwtJ9dCGMxB6pCL1XQnhbd-0MotQ06TJrkW-Zei5fIEsbESAPtUoizwbcfYmsazOahhFQTB2W3KhWT9mMQpKIS_v5V_qZ1_A9k2oWEEj77kFks9DjqmMwlwl0WoVQw_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/17979" target="_blank">📅 15:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17978">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMILITA CAMP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIg5QR2YecHWu_ffip9_CYTDoz7LLrHzZMxfiEkruwYqkp6-oVrzMHoReIvmTfzCXPHVk76pWmp_jJf7f9YdFSDOxiru8TVVp-OGULKKVNYhFQQephte5L6V2puf7J_ffKrAlI18Aaif_1YTU9sWN03dRN9HRyCu-35CqCwgkNAT2PmfYLvNWEs2UR4KFyu8synf4-R3kl0gHN9TsxoDsLdKjVmJIE3haKneA7r4bF5QuEeV9LYR4ER3SY1zc-X4yrWzWly7Ad99ji1JF2v8McLNKIj2b4bz7Ftm3QLgBdXdFhBITDtwJYSAXL_BF2dRWEF0TYhntlKihHGfanCjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.
@Milita_Camp</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17978" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17977">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17977" target="_blank">📅 12:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17976">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل قبول و کاملاً خطرناک است.
🔸
به اطلاع همه می‌رساند
تنها مسیر مجاز برای عبور از تنگۀ هرمز همان مسیر های اعلام شده از طرف جمهوری اسلامی ایران می‌باشد
، و تردد شناورها در خارج از این مسیرها بسیار خطرناک و ممنوع بوده و اخطار می‌دهیم از هرگونه تردد در خارج از مسیر های ابلاغی جدا خودداری نمایید.
🔸
هماهنگی با نیروی دریایی سپاه برای عبور از تنگۀ هرمز از طریق کانال ۱۶ الزامی است و
با شناورهای متخلف برخورد خواهد شد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17976" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17975">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.
پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17975" target="_blank">📅 12:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17974">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به
گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/17974" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17973">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17973" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17972">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/17972" target="_blank">📅 07:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17971">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ درباره اردوغان :
او دوست من است و از جنگ دوری کرد.
می‌دانید، او کاندیدای اصلی برای ورود به جنگ با ایران بود.
شاید در کنار ایران، چون همانطور که می‌دانید، طرفدار  اسرائیل نیست.
و من از او خواستم لطفاً دور بماند، و او این کار را کرد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/17971" target="_blank">📅 00:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17970">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=HiT2s4D0Mdc3sSMh1JPrpLSZO1sP37XGL5OXYvE_AX9llU_11u4KKVT4QItgpfEA15zuyjs2r-6VolOxd3A6lcmflR_x-v8pwyF4cD84uF15VlzE2XoXBGfy6L9APGAxIZcjC8OOkCyxpEAhGrb3WH75NT8sQuJ7jc3x6Lk2Clgq1M8pGo7IXK6c6QmKA6AX4T0zzGwcxQkitjOuHV-eDz-30xAoIQstknpbv8ji-_8e-O_d1CCwoVcDWadue-BOqzMckdcsoLdOSo5Of5Mh9cUIg_nOpR-fqqggIFCeRFKUSr1HXi4vfjU33Isgj6u9-hZiy94PIknmIWUTN0DiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=HiT2s4D0Mdc3sSMh1JPrpLSZO1sP37XGL5OXYvE_AX9llU_11u4KKVT4QItgpfEA15zuyjs2r-6VolOxd3A6lcmflR_x-v8pwyF4cD84uF15VlzE2XoXBGfy6L9APGAxIZcjC8OOkCyxpEAhGrb3WH75NT8sQuJ7jc3x6Lk2Clgq1M8pGo7IXK6c6QmKA6AX4T0zzGwcxQkitjOuHV-eDz-30xAoIQstknpbv8ji-_8e-O_d1CCwoVcDWadue-BOqzMckdcsoLdOSo5Of5Mh9cUIg_nOpR-fqqggIFCeRFKUSr1HXi4vfjU33Isgj6u9-hZiy94PIknmIWUTN0DiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17970" target="_blank">📅 00:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد  جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.  ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17969" target="_blank">📅 22:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد
جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.
ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17968" target="_blank">📅 21:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">#USOIL — W  در تایم هفتگی به کف یک کانال معتبر هفتگی می رسد و از اینجا ریزش بیشتر توجیه بنیادی ندارد.  این یادداشت را هم بخوانید.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17967" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lctlbwo6AjyN7r_40aWPxNCFVR0MvTPKlsrn3FMiVAqnKvtkWFCVdnRCEl6O3_nLl01G9TuQCGnRi8Ru8KzH1FMLIbPkDHlZ9esSXG_xK34AnIrExJ8wEPNcg2kfP9t68PJw59qFH59vGcRLQgDlJOKBcTCcQr7X5zos1wn3t9PxipcXS-zdgmGt9GgG0bUWNqAW1ELsTtjvG8OM2pQaGBNBfAw7qW7Et97kyh7Cx0D6bIhFLBSjDcx07ZzPdC331AJoDM6VGhJ9UXWol3YUJrUDgpmMvDRmzth3wwXjhUjWE7hUhyHlrFJ4OOUDcDyw1aQeZfIbybXexkC7QeNsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — W  نفت همه رشدی را که به خاطر جنگ ایران تجربه کرده بود برگشت و اکنون در حال نزدیک شدن به نقطه شروع حرکت است و زین پس دیگر هیچ ریسک پرمیومی برای جنگ در قیمت لحاظ نشده.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17966" target="_blank">📅 19:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دلار 166 هزار تومان!
بخشی از این رشدها به خاطر کثافت کاری ها و باج هایی است که به طلاداران داده می شود. وقتی اونس سقوط می کند دلار را بالا می برند و بر عکس.
تارگت های 240 و بالاتر همچنان در دسترس هستند البته اما  این رشد دیروز و امروز برای این است که گفته شد.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17965" target="_blank">📅 19:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY1R-cwb23LrVyeqn0cqMgKDaBeMuLibtFzb7iVKYVhi3nDe9RG8pwo9lez7sRYwkb2gWROYXmTsd-zkIWY2W_U4jFdR_Xn0pT_81DtQKpAYd2cticlNsbxhvqrlWj5EtTPQLckyn_eaUZOR5D4aps8fnWFgkCW3JdNLqAVt_se3ZB06vTAaBJjhAw6aI4GMqBRLPirhMuutmKALxyGqzWGoViG5w-tOtVm26_WjLBmDpez1rhJ_q3yoqTUxX6F_QkU_vxtqtE1kFeHkSeAkc0onY9W6KxLIybO8ZGyL9tdVkBaZbFHKsqH6SfZ3SEGOoqzADelocP2FB4Jg7BovHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17964" target="_blank">📅 19:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17963" target="_blank">📅 16:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17962" target="_blank">📅 16:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رویترز:   سپاه پاسداران انقلاب اسلامی سلول‌های مخفی در عراق ایجاد کرده تا حملات پهپادی علیه کویت، عربستان سعودی و امارات متحده عربی انجام دهد. این سلول‌ها از جنگجویان شیعه نخبه عراقی تشکیل شده‌اند و مستقیماً به سپاه پاسداران گزارش می‌دهند؛ بین آوریل و مه حداقل…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17961" target="_blank">📅 16:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17960" target="_blank">📅 16:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epy42LoeNSNLS4ImmjxsS8rtuVdCOSu3zEpTYRBXZXwJX31FOC8jCUtADgynOqNpkI4JAdKt4Vo86WLgtBAllIwqZcJ9ivDmFezYxoWx9N-VzK1ysYzcd90Et-XMZ-nHfN0Vp8RkEBPecN2eJrVpUB_JKATjrjo6lVYt8FYoXPFhGya2-iBRqN1wL2vma7eR9NtJTIQ2C0W8mozrayw6B-IlDOSEhYan9O6O3TJbAS0WEq3D1kPt5fzEJbQJjGyU0cHF10SYBw9MtO7Ctvho1r24bxKV0PDSOBXg9PDwsJXmcQ8Zd_dN9Y5dExuWlRft5OxSA3vWsjPheBWXP59glA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  پس از یک سال رنج زدن، شاخص دلار به صورت کوبنده ای رهسپار تارگت های اعلامی شده.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17959" target="_blank">📅 16:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7WgStiK9NCKeauY4TKebfF1Un9UZI79BCQDOa5b8StBesETSZhBVVvkT98VB0kPJggNKlnt3sk3nj7Z1mHBX0ty33lhNppVObAr36ap_bjXC4-s_flfLVzq4y6hYrALiokUVURMQc8OGtZEJajIYUDph3aIrlF2oDvn0TRXZc-W9l4SKgJnR_eXGhtuTHWqhotZxKAaFD2SiC0tfeV4ApFjErwM6Wzg9kjLMapIazRsJ31p6a8gkDe6fL_Qe_R1sR9nkFXQWaWLj1T04btsvMyTrappyYXgyI3ysBQ0Yx6sZZOueMASXjpaRN-5RbvwY8Ow0FE92Egf9rRg8rsebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  رسید به کف کانال هفتگی!  از این هفته فروش دلار که ممنوع است هیچی، خرید هم در دستور کار قرار می گیرد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17958" target="_blank">📅 16:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: ۵۰۰ میلیون دلار در ابتدا برای خرید کالاهای آمریکایی به ایران داده می شود</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17957" target="_blank">📅 15:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=s5wA8hNuGmoarTKCPLDk-MK00EAGk5exzoidIwTAFCXFbn9nR6rSTY4_hnKUq-seHQvEok7Gvu-sqGeBVbQms1lwJ_0Vx6fjDIRbaEdniKM125qdsT8L9WYZkGrNx_Sz8EOLPbn33Q8U7csQCIvWxEcZj7jX-337Q1R_fQwlNNGGiAgN5U8P90S1pOENSEppco4yCLVL1rwFlakqEeUt53zFk6w2lLaiqPMBQtHk8FsmDREztykPD8il4CdTUvks0Ikn-_QPrQnCQKF1-NfazEexsSKCEdHAArbPXQTWWLLCi-tgeLzQPO5j0n_PKTMmw2SkogkEy_ohFNTzykp9EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=s5wA8hNuGmoarTKCPLDk-MK00EAGk5exzoidIwTAFCXFbn9nR6rSTY4_hnKUq-seHQvEok7Gvu-sqGeBVbQms1lwJ_0Vx6fjDIRbaEdniKM125qdsT8L9WYZkGrNx_Sz8EOLPbn33Q8U7csQCIvWxEcZj7jX-337Q1R_fQwlNNGGiAgN5U8P90S1pOENSEppco4yCLVL1rwFlakqEeUt53zFk6w2lLaiqPMBQtHk8FsmDREztykPD8il4CdTUvks0Ikn-_QPrQnCQKF1-NfazEexsSKCEdHAArbPXQTWWLLCi-tgeLzQPO5j0n_PKTMmw2SkogkEy_ohFNTzykp9EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17956" target="_blank">📅 14:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یسرائیل کاتس، وزیر دفاع اسرائیل:
«حتی اگر از سوی آمریکا درخواستی مطرح شود، ما از لبنان عقب‌نشینی نخواهیم کرد.
دویست هزار نفر از ساکنان [شمال اسرائیل] هنوز به خانه‌های خود بازنگشته‌اند.
ما تمام رهبری حوثی‌ها را از بین برده‌ایم، به‌جز عبدالملک الحوثی که در تونل‌ها مخفی شده است.
اگر او در تیررس قرار بگیرد، کشته خواهد شد.»</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17955" target="_blank">📅 14:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwuI4-6ygm7zsBMbVglMW_tt3uosG6fkDDllKbtoHafssHsDGmY7FyX9m_bsKyLDqBd5pjC_VRG3u8plvYU4H4XfC_wBys12nqbnuCiEzvH0dHrJ_HGwrUzEGTJpe30j15mGcLz0C86VCEIM7w1Lv-91D8tWD57Gz1Qyal82o0MXaCandW79jd112KN-khhCpztJDw_8cA8XdalNhwOYciKT_2UryF1ID0L9rWs-CgiceAeljxgvVkaYunyH5MGWp9vOh3r-925sIcP0pjvMi9uLXVqNSBUNiUUblDaKCL2GNZ1nihJfwVP5D3Vw13UVkH9Nw6fpAFyGVd04qochVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17954" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHX8UEzJCnzljh_K_FNTLidnEkw8ZRauAcEzwMk0NAx_WmbsO5nmjCgAI3vD78OkJS-qDjADP5PcCOA14SqpSMN5DCtBo60CUrm-oP2zUmyj8T-_KDe4IFVZU3QZUQg0omVSQmPcRVmnESS5dHc3Tt4cN0AQO22rsg_YZZOvZXwujzrJsYkBBJ2-VZ8l214ZGPFnaCmNCntmPdIStMHy7yWelKpI5IfnOuq9xYozVw6UDJeANlLCpcjzmDyOtsckpGb6Y3zCfNsq3yzRm0rE7Oc4kCEIi-GIjRTb1d0KsCCDQ8BtZ1MjJVBurs7wX-wLNcELEpysezNgxUuiELSnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#طلا
بر اساس نمودار، احتمال ثبت یک کف دیگر پیش از پرواز دوباره قیمت بالا است.
بهترین محدوده خرید میان مدت 14.2 میلیون تا 14.9 میلیون است و تارگت حداقلی 29 میلیون تومانی فعال خواهدشد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/17953" target="_blank">📅 12:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:  ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17952" target="_blank">📅 12:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">برخلاف تصور رایج، «لابی کشاورزی آمریکا» یکی از قدرتمندترین ائتلاف‌های ذی‌نفع در واشنگتن است. اما این لابی یک سازمان واحد نیست، بلکه شبکه‌ای از انجمن‌های کشاورزان، اتحادیه‌های تولیدکنندگان غلات و شرکت‌های بزرگ کشاورزی است.  نکته جالب اینجاست که این لابی، برخلاف…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17951" target="_blank">📅 10:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17950">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17950" target="_blank">📅 10:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17949">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:
ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17949" target="_blank">📅 09:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17948">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتحلیل و رصد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=tSTEMvYIWPzYK7d8CuSUeZolitVH1Exv3qj4LB9QW-3Ga96JAeLbaElKniqe76VeaUYk0DkbGLEm_Aqt1nU140bGqSosFzsp59sHCeFhHrK5BKEu1C6cM4Ct6YvAX9tTexBjwGDZl-oiMmZmfTcTVkE319kmx3rLfLHRFkschf8jp0YuvCwRCFpur9MOE8FgNrm6Lcx_OOxf62E5VcYVTyrorLyDACfzGAeTkfJqLz0ESErEI1w2JEHJWdR0jVwVHD-FM8hjEqxB2ZHhmkVsyVtWkx5vEblfyERnn0N-O-GPMAEh_QdY4ffONBYdO8Dx8QOFbqoRBrktkQ0eFlIbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=tSTEMvYIWPzYK7d8CuSUeZolitVH1Exv3qj4LB9QW-3Ga96JAeLbaElKniqe76VeaUYk0DkbGLEm_Aqt1nU140bGqSosFzsp59sHCeFhHrK5BKEu1C6cM4Ct6YvAX9tTexBjwGDZl-oiMmZmfTcTVkE319kmx3rLfLHRFkschf8jp0YuvCwRCFpur9MOE8FgNrm6Lcx_OOxf62E5VcYVTyrorLyDACfzGAeTkfJqLz0ESErEI1w2JEHJWdR0jVwVHD-FM8hjEqxB2ZHhmkVsyVtWkx5vEblfyERnn0N-O-GPMAEh_QdY4ffONBYdO8Dx8QOFbqoRBrktkQ0eFlIbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!
پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.
ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه ولش کن. ولی مسعود هیچ رَقمه گوشش بدهکار نیست و فقط بیل میزنه.
@tahlilvarasad</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17948" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17946">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⛔️
کارشناس اسراییلی تشریح کرد: ۸ کانون تنش بین ترکیه و اسراییل؛ ترکیه ایران جدید است  یک کارشناس اسراییلی با اشاره به اینکه تنش بین ترکیه و اسراییل به بالاترین حد خود رسیده است، به بررسی ۸ کانون تنش بین طرفین پرداخت.  ایتان لاسری بر این باور است که اسراییل…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17946" target="_blank">📅 23:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17945">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نخست‌وزیر پاکستان، شهباز شریف:
«کشورهایی هستند که می‌خواهند توافق را مختل کنند، و من می‌گویم که بدون ایران نمی‌توانند موشک‌های بالستیک داشته باشند. استانداردهای دوگانه قابل قبول نیست و منطقی نیست که برخی موشک‌های بالستیک داشته باشند در حالی که ایران از آن منع شده است.
یادداشت تفاهم (MoU) به مسئله موشک‌های بالستیک ایرانی اشاره نکرده است».
«این یادداشت تفاهم به موشک‌های بالستیک اشاره نمی‌کند. هرگز روی میز نبود؛ هرگز در دستور کار نبود.
طرف ایرانی هرگز نخواست حتی درباره آن بحث کند».</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17945" target="_blank">📅 20:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17944">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17944" target="_blank">📅 15:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17943">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر سابق اسرائیل درباره ایران:
هر بار که اعتراضاتی رخ می‌دهد چه اتفاقی می‌افتد؟ اینترنت را قطع می‌کنند و سپس هیچ ارتباطی وجود ندارد.
پس کاری که من شروع کرده بودم، فرایند تهیه و قاچاق ده‌ها هزار گیرنده استارلینک به ایران بود که اجازه می‌داد اینترنت و شبکه‌های اجتماعی وقتی قطع می‌شوند، ادامه داشته باشند و به اعتراضات امکان هماهنگی و در نهایت سرنگونی بدهند.
متأسفانه، دولت ناکارآمد فعلی اسرائیل این کار را متوقف کرد، همانطور که تقریباً هر برنامه خوبی که ما شروع کردیم را متوقف کردند.
و وقتی اعتراضات رخ داد، آن زیرساخت وجود نداشت.
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17943" target="_blank">📅 15:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17942">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17942" target="_blank">📅 15:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17940">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWxezgX-fNSxAydsUVXcGGZxCWwyLwSVJ2My15SNAaG3dlL2o0RC7nx0km7lwkj6dSKCqPT7WsWJVp1nF3ljer8o8kF6ZEu5KHA7tamuspuYYJl8D9dlV2_gWsH2xyQhA7OGvi_1xf8dLT8CMBiqYGxGqD7bdwML47LD4FVoE3mNdSSTeVkvz5vlqV_xwqjdRq58rozkO8msn7Xop7d0phW4E5zEEj_ht2k3tCjFhWaOJOBK_MQyxrXL6NLgFRLLyBa8mj9yL4mFQlewxyKneZwqWfuvyCcHUpY4IXt5klzlHIloFPPaQcYaPKufmTuKHk7A6TU-Lh5vve6Ym2evbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyKMiPuHLAuoKCMIYjhPt1BPN4sLHh-0mwcXR6BYuyvkUFWOq52_LPQPFq-j4OEWX6D4XX3O8dCEf-fuH0Ood739y93nQOZs-W4szRASRxv8y2xf1CgWCsjFJl1kqawYv1tCmh4xxODgDcVXIS7asukcNFdoA577kdzNDfL039in8MIKeNPA1mNvSekA2iAAAWQ_x_Ldb2S-AZ1JIFPrKviEIGBShHy9ZWj996sKKXjvfuwHzIZHnl4sD4L0bguOCiMaU3R4Kd9jvHf4E0-8XTiOoNcQINo2q_5klW-6pMNP3Qc2gAYAyitwkBfaf9mTCZET5C3BQLYGLwpMGHcBHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه جلو میرویم داستان رابطه مسعود با شهباز
دارک و دارک تر
می‌شود
پناه بر خدا!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17940" target="_blank">📅 15:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17939">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏
امیر پوردستان: آمادهٔ عملیات پیش‌دستانه هستیم
رئیس مرکز تحقیقات راهبردی ارتش:
🔹
در دکترین تهاجمی، عملیات پیش‌دستانه نیز تعریف شده است و چنانچه مصلحت نظام ایجاب کند، ممکن است با انجام عملیات‌های پیش‌دستانه در عرصه‌های ناشناخته، دشمن را به‌شدت غافلگیر کنیم.
🔹
نیروهای مسلح هنوز بخش مهمی از توانمندی‌های خود را عملیاتی نکرده‌اند و دشمن می‌داند که در صورت ارتکاب هرگونه خطایی، با پاسخی فراتر از مرزها و تنگهٔ هرمز مواجه خواهد شد.
🔹
در یک ‌ماه اخیر، ما چند نوبت تا پای جنگ با رژیم صهیونیستی رفتیم؛ لانچرها آماده و دست‌ها روی ماشه بود تا در صورت عدم عقب‌نشینی اسرائیل، جنگ آغاز شود.
🔹
تهدیدات قاطع ایران سبب شد تا آمریکا برای جلوگیری از گسترش جنگ، به رژیم صهیونیستی برای توقف تجاوزات به جنوب لبنان فشار بیاورد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17939" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17938">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">توییت ترامپ در مورد ایران:
با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17938" target="_blank">📅 14:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17937">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🟢
طبق اعلام معاون اول مسعود پزشکیان ، در راستای برگزاری مراسم بزرگداشت رهبر فقید جمهوری اسلامی ایران ،  13 و  14 تیرماه استان تهران و 15 تیرماه کل کشور تعطیل خواهد بود</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17937" target="_blank">📅 14:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17936">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17936" target="_blank">📅 12:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17935">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارادوکس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6wxMpCNusIXAD93SbZpwWPM3FSrdhutTnHsXePqp2kpeAKwur1LiTJ9SBHGRSJ6DXDR6tzvqJZPTBBnYqb4juDJFFCohXE2bIKR0ttzdLHpsFRb3A3P4BSb4iGKNZSoVTWHizkiGO0ykB29YrWbBVh2o6j4wpM4JO88w-mHfBneIet-qyJJ4aeETx339AicRXf-3_33bgseEEBiuf5jLxwZRJZzDCy98yW2Lbwfl_Og4e60Umluf-PDnBMIIc1kfDwSQaUiXMI-yrFfa7aOdsErhNobF6-T3Jz8FCBg5yPSi9Fh0h9fwcJ_Ov78mvIm7UyzAu40sdGnccwaqrSkTMH3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6wxMpCNusIXAD93SbZpwWPM3FSrdhutTnHsXePqp2kpeAKwur1LiTJ9SBHGRSJ6DXDR6tzvqJZPTBBnYqb4juDJFFCohXE2bIKR0ttzdLHpsFRb3A3P4BSb4iGKNZSoVTWHizkiGO0ykB29YrWbBVh2o6j4wpM4JO88w-mHfBneIet-qyJJ4aeETx339AicRXf-3_33bgseEEBiuf5jLxwZRJZzDCy98yW2Lbwfl_Og4e60Umluf-PDnBMIIc1kfDwSQaUiXMI-yrFfa7aOdsErhNobF6-T3Jz8FCBg5yPSi9Fh0h9fwcJ_Ov78mvIm7UyzAu40sdGnccwaqrSkTMH3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
⭕️
چگونه نام تاریخی و ریشه‌دار دریای کاسپی (Caspian Sea) با یک ندانم‌کاری آقایان پر مدعا خدشه‌دار شد؟!
یکی از تلخ‌ترین لحظات تاریخ معاصر، روزی که حیدر علی‌اُف، رئیس‌جمهور وقت جمهوری باکو، به ایران آمد و در دفاع از نام «خزر» سخن گفت، حال آنکه سید محمد خاتمی، رئیس‌جمهور وقت ایران، نتوانست با تکیه بر اسناد و مستندات تاریخی، از نام‌های اصیل و ریشه‌دار این پهنهٔ آبی همچون «دریای مازندران»، «دریای طبرستان»، «دریای قزوین»، «دریای گرگان» و یا نام بین‌المللی «Caspian Sea» پاسداری کند.
او در برابر آن ادعا سکوت پیشه ساخت و حتی با صدور بخشنامه‌ای شرم‌آور، این دریای کهن و ایرانی را به نام قومی وحشی و بیگانه، «خزر» نامید؛ نامی که هیچ پیوندی با هویتِ تاریخی و فرهنگی ایران‌زمین ندارد.
⚜️
@paradox_p
⚜️
پارادوکس
⚜️</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17935" target="_blank">📅 11:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17934">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFSGg7Hi_bUWJaFGRIxaPmj7t1ik26KxOVriKzMToaHyYvEq9-10qhqk-ThM2-rrdagvMRhAjQdkgsOfmpdeyayiWDUBXmqrheMdfsGFiQe3SxA5m5MDy_bCV6yl8JScAV8BYW1eZR8ENiWVJle8cWUfW3SwDO0_YcYzvmSif8fOIw0qn_xu_h-2drEHQgEOa_sTOWKpoNJXgjy_IDji5YDR9CCd0v5kNbo1wCWgzBCqhp8Xkapp_fkl7HaM8TX0uMTHiq9D9pPdGrnUpbWXwez1uZuoFd0ulZO7QzHqnrweofy0_2YpBhp37rKPkJm7WnA2P8c2JP5IqT3pFNAwww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت استاد!
از تبیین کوانتومی آفرینش و پایان هژمونی دلار با ظهور بریکص رسیده اند به رفع نیاز جنسی با دوغ!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17934" target="_blank">📅 09:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17933">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17933" target="_blank">📅 07:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17932">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17932" target="_blank">📅 07:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17931">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزیر خارجه عمان:    به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز پایبندیم.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17931" target="_blank">📅 07:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17930">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:   آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.  اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.  ما می‌خواهیم شاهد همکاری ایران با کشورهای…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17930" target="_blank">📅 07:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17929">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN9cty82Cg8Ptw8TWD9cv7t9hpVu-Nw2RPmtLc1iU4Xg8NF5uYzi4m3UjUsW_5GXeQpRNy6l_QzlrvdZuTI4AUiyMMOpHjgxrYlQdMTB-irTg3a3ks7vUIz9WBkiJ01X5E6lPK4hy0nKGePYOjjrrrdoBrKPFa44A1EFH4f1sJJoJGoBeYtGG3gsRl5Y_i61ee-Mh1Btu4p9tp_9cfixp8zPRd_D9DD2WbMJVRJuVVWMym0ylQIfry53ZcO_176ocZpZE5_0hmK2Nt1gY0fHNa-JL53UhhdWP08Qr8ZCq7iFUvYFkYO1IpT8VREQC5tjnHIsq28fuZCkAhaMjSkI7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی رئیس بانک مرکزی:  ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/17929" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17928">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17928" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17927">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17927" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17926">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل :  بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17926" target="_blank">📅 23:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17925">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل
:
بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/17925" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17924">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx2_qgIkuPUFXS7XUBD4Zk_mbzZ6w7xmjsVGg5bdg9lr98gSjusswbee7mILlkqr_DUUyFGwkaSKJB4xRqzwcUkAuegOCQ6dvVEM1VOC1QxOAyHe8yPJc9yIGuccz708qIYCYMjla8y3DLlMsPXC-ZBmE6r6H8p-3xkDW_HhVUWJOEi4BGn-lxXqTvEMDVgzmcU9XfHvv2-ixrKnwI-MYOVESeC1giGBm8wgo0B3M7jTX-2tIsetcB6GHkj4htNVfyrech8mnW049o7HNfD5j6SmvuKvUl0x0rrq2EVSmSht_7KMSO6Sts9m5jncX1TnmEXCpb_MIm1YW9YMUWmMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوستالژی هر ساله ما آغاز شد…
جای کیان رویگری خالی…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17924" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17923">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی نکند، به مذاکرات باز نمی گردد!   ایرانی‌ها اکنون تنها خواستار توقف تجاوز نیستند، بلکه خواستار خروج (نیروهای اسرائیلی) از جنوب لبنان هستند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17923" target="_blank">📅 22:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17922">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هند قصد دارد موشک های کروز سوپرسونیک BRAHMOS را به ارمنستان ارسال کند</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17922" target="_blank">📅 22:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17921">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ:
همه کاملاً آگاه هستند که ایران موافقت خواهد کرد تا بازرسی‌های نظامی انجام شود تا «صداقت هسته‌ای» را برای مدت طولانی در آینده تضمین کند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17921" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17920">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خوش‌چشم، کارشناس صداوسیما:
آمریکا خودش تاسیسات ایران را نابود کرده است و حالا می‌گوید در بازسازی آن‌ها سرمایه‌گذاری می‌کند تا در سود این صنایع شریک شود/ به جای خسارت دادن می‌خواهند ایران را استعمار کنند و ۵۰ درصد سود صنایع ایران را کسب کنند</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17920" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17919">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مرندی:
🔻
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی‌به ایران صورت نگرفت</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17919" target="_blank">📅 20:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17918">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17918" target="_blank">📅 20:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17917">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLlDJiAKQI68yijP1Oi6ll6St9-TXK6maVgWpv7Eg7RjzoOnMG7SDMT8ltxrVBqD8y51-pOhDQbzmfyr2zVNjWDFWcKf-ASRJ7S5XyQcsHESHVDLBOlrkgociKoTrPcJtncv6kTDBe37YKB9eMkv57js4myMKZUPwPkTlG0jq-ufOTAP5Fhzh_f2i8XmvBfAUDJE_OChBO9EqnEg6kk3TGGfkIZAvlEyh8BD5zUrnnYkx4yeHcDYSbqUllmAkqSPrG-izBiBiSxmYzvfvyub05V4MSuHUeeH4JfwhGrD9csz-7-f3bRVewONx1ERz6wi-jPunj9BeUJardqtAsSU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17917" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17916">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خردمند کسی نیست که بتواند میان خوب و بد، خوب را برگزیند، بل کسی است که توان تمییز خوب از خوب تر و بد از بدتر داشته باشد.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17916" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17914">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWjFmiUFUHzYtHF0Fl3AN1sZr5DsBpvGw0lMlmPkbg0K3YYJ9MH5U_aH0GHzE8swjCJZ7FuwlV2-laKEZ4HxN0TjVUWXnTTRBnc9H6_iEmcoaXmNA0cXAWTOKZapBSlHS2wI_IKER8pkyV3846ysbiHjgvANI7vDOypkkqnygdIJDKZR8jdafBEEJ_bW7IcJRSS8oqYnUtGl-CYK3jqagIjknn2UXW-U74o9QKFdthxG9_QApxEx5nd7AlPSlnih1EcOP3E0jgNlQuB48olMAikm1AiNnamS8MstFO2V4NXOibNhJaplZOR3KGebjc5yoHQPbHVMeMMVAfoceqDmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvpfKGidHyizV9owx2WtdIkXXj2s1BNfNp5eUqnM9T6nJ8TNSvb_pE_xLIxS9i470WRdXum5G0RcbsOcmz0a5w3HIGX996I6f63V9nnTvJHBaqZhOoSELg2bYIMhQIHrPoqJXtlweuBOvIJY9npvnQdFlmy2vq3cIByLIVZ1b5BW1N8ua6cXOLYt5cCUd4c0kAw-BHVix1KGGbnWFjK8ApHNiQv7_ChSHNVLd1b5MJLAtZVZMBtporNrgGv2LxdY88qAED6YFewI4cbuSF8-PnkTL_MF_lYMsCxY0U7MOQHsgrwHtVnCiHWwRJcgCTqrhZOvq0oum3ksyYlWFFMRqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمیگذاریم اسراییل بزرگ تشکیل بشود اما خودمان دنبال توران بزرگ هستیم و این نشان می‌دهد چقدر مادرقحبه هستیم.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17914" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17913">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmzCCxK2TCOfmNNry5yq2OBqUc9Bs48ADkXqOjlQUoCWAuhJpkDtdznz-CVysuWEFBsZxuUoQzkju305YsRabgFoHipfSG0u6xcGjNf8ZuxR2xR1xV8kKRf1g8TYShm71mslltrSlEjNFASjSywQFPBSjt65NRv6ZbMHzPw58Ge83nfTWkQysnh6MhGqLV_8D1FrSwThcrkH165n0zoiN4WbUUQAbTMBT5y5IKG2jdIt3BBGrkLNcA7ECBEEXV6_wi190a-8xBywn6__S_ALNVAzNwa1YSdqCZdtDQM30El09ynAuW-_BxolIVhhPOSmBnfobwJ5yZBY5KSQl3xuNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو دشمن اصلی ایران
این‌نقشه، راهنما و توضیحاتش امروز یکم‌ تیرماه(۲۲ ژوئن)‌ از یک کانال تلگرامی نظامی اخذ شده است. بر نقشه و راهنما متمرکز شوید:
"کوریدور خیانت؛ تمام حملات هوایی به تهران و حومه، از این مسیر و به طور روزانه انجام میشه... آذربایجان، ترکیه"
کاملا درست ترسیم کرده و نوشته است. باور کنید در جنگ‌های ۱۲ روزه و ۳۹ روزه، تقریبا هر شب و روز‌جنگنده ها از بالای سر من میان البرز می گذشتند.
ولی این کمترین سزای حکومتی است که حاضر به گوش دل دادن به پژوهش های بیطرفانه نیست.
بیش از ۲۵ سال پیش، پژوهش های طولانی مدت و استراتژیکم طی دو جلد کتاب با عناوین: مقدمه ای بر ایران و همسایگان (منابع تنش و تهدید) و کتاب: مقدمه ای بر تقسیمات کشوری(ج یکم)‌ منتش شد . کتاب هایی که نه تنها سرداران آن را خواندند، بلکه مقدمه ای شدند برای اجرای پروژه اطلس استراتژیک ایران. پروژه ای که بارها برای سرداران فیروزابادی‌، شمخانی، باقری، سلامی و ...سرلشگران زنده گزارش شد.
میدانید چکیده کتاب ایران و همسایگان چیست:
دو دشمن پابرجا و اصلی ایران ترکیه و جمهوری آدربایجان هستند.
ولی کو گوش،شنوا.
#یدالله_کریمی_پور
#karimipour_k</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17913" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17912">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWa6wrxoaAwsw6LGu8DqGww9-hRfwTYKQ1vea6eaCvn3msMOWD4qnDFyZc7z6PBKQ3tpCX0R2WncHUC1zNSDj9DdYWBIr9JxfbFdzWVWU46E9FvUYg4T6-u5fEJc3XSFtNgTGW7T_7MBhr3febDlRZMSV-B4oZK8HUQKs8wqsDIDPbX0SWfvo08HY4iypG-EyEs18ESgc5K9SuoI9eNeqwjJklf6g_LymCCr5nmjeGwq0kTUn9cb1AoCxh0IqL2QmpiS_iZRoQeQVCet3xwl1xWNwaVmC-1no1FmVZGiB7kcnIcjVw-WXTjGjQodhNLEV9uNn9rRZaDHsg9gNQ4THw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17912" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17911">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17911" target="_blank">📅 18:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17910">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17910" target="_blank">📅 18:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17909">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17909" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17908">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-0lWRLwTyzZ8q9Tjs6X6SPoTLjfOQ4ZIOgzpnMWm8RP9k5kJGH-COGFN5aQypAqxiyywkvGKhPyDnCC4xHflVgAiSalr1XdRJdwyQOo0kVQ5m-2mTXqcfUbDvshjtrtDiJ2j4k_f5uWPytpOdq62L9Ly5y9vqDD7rDS8PkeQd_VeID3YPmPGc5Wv38OL3uuRj1F-qCM1v-I6IN-7P60JNwCYrUP0kst3s95aFb1ltjVywsPA1UeKfOoMWw_3yWK6a1X1P8frB2Q0byZsc6GgGMsWKmwOu1ubWDhon__fOvKNVrtrZBu-psVIM8_ChnjHm3pccWPrtI-J9q47Pr97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
یادداشت تحلیلی: آینده بازار نفت در شرایط جدید ژئوپلیتیکی
بازگشایی تنگه هرمز و توافق آمریکا و ایران می‌تواند فشار عرضه نفت را کاهش دهد، اما بازگشت تولید به سطح عادی زمان‌بر خواهد بود و رقابت تولیدکنندگان دیگر را تشدید می‌کند.
در سمت تقاضا، رشد اقتصادی جهانی در برابر ریسک‌هایی مثل دلار قوی، نرخ بهره بالا و تنش‌های ژئوپلیتیکی قرار دارد و همین باعث می‌شود بازار نفت وارد یک دوره نوسانی و چندعاملی شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/17908" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17907">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:
آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.
اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.
ما می‌خواهیم شاهد همکاری ایران با کشورهای خلیج فارس در سطح بالایی از اعتماد باشیم.
مقدمات برگزاری نشست‌های خلیج فارس در دوره آینده برای بحث در مورد امنیت منطقه‌ای در حال انجام است.
موضع اصولی قطر رد هرگونه تغییر در وضع موجود تنگه هرمز نسبت به آنچه قبل از جنگ بود، است.
چشم‌انداز ما برای تنگه هرمز، باز بودن آن و آزادی عبور و مرور از آن است.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17907" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17906">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrTE89hcYUlsvjFOqF0_H2aRmKb4HEGcehvhfUtmzt5P1lV59S8SqmmTgp5h5Y4I3Lez3J2oebIJWKKCo4yVK6ZqU9Eo0hUqme7i4F_HwaQECfocVk5QtYItxT_cyu-CJbdZC2ynsSauoGj_QSZ12_AuZA5eYzdK3dp-ASs3MYXhL8navMk149IqfaVAeuRFjL7MYchojzUYQO68SWDnvH6t1FJ-20QgsKnoVGvs8b1aR-RBXMTkQcur0x0MHABhp2lVnUrU4v_hirqF6GssTHHQ6NbVJLAPCINi6GjvVOM-1-705inahJ1D2wn2QX5Ag9G0ipJhg5sa3-f5DgaWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش احتمال وقوع رکود اقتصادی در آمریکا به ۱۵ درصد پس از توافق با ایران طبق تحلیل موسسه گلدمن ساکس !</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17906" target="_blank">📅 15:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17905">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17905" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17904">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17904" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17903">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جی دی ونس:  آنچه جرد کوشنر و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپی است. اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17903" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17902">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17902" target="_blank">📅 15:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17901">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جی‌دی ونس: ایران مذاکرات را ترک نکرد؛ ترامپ به اظهارات تهران پاسخ می‌دهد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره گزارش‌های مربوط به خروج هیئت ایرانی از مذاکرات گفت:
«ایرانی‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم چنین تهدیدهایی در شبکه‌های اجتماعی مطرح شد، اما آنها مذاکرات را ترک نکردند.»
او همچنین درباره واکنش‌های دونالد ترامپ به اظهارات مقام‌های ایرانی افزود:
«دیروز به ایرانی‌ها گفتیم وقتی وارد چیزی می‌شوید که نسل ما آن را "کری‌خوانی" می‌نامد، نباید انتظار داشته باشید ترامپ پاسخی ندهد.»
ونس ادامه داد:
«وقتی آنها حرف‌هایی می‌زنند که درست نیست، ترامپ هم به آن پاسخ خواهد داد.»</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17901" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17900" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17899">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17899" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17898">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را بازگردانند</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17898" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17897">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17897" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17896">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17896" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17895">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17895" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17894">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">— یک منبع اسرائیلی به سی‌ان‌ان گفت:
«اسرائیل در حال بررسی اعلام عقب‌نشینی‌های نمادین از مناطق جنوب لبنان است.
عقب‌نشینی‌های نمادین شامل عقب‌نشینی برخی نیروها از مناطق اطراف خط زرد خواهد بود».</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17894" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
