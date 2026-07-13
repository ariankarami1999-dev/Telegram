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
<img src="https://cdn4.telesco.pe/file/R40UbZuKXA7oHquC-G2mIX8M-XVY2G5K45mKiYWzmyM7Y8IC8aF2lKcOZKgPfQOhstpgzVBR84thxhnEadibitDgChbtUtpP0y7kzdVPWLkNL4pbosr9P5SN00hk0GFDiztVgAXU9SFR3MIM4wb8CwxTMKTnSbvWD4YfpxVIf5NU52RKCNZAYm46QpU9uTRmQn9AL6naKhUbevfmlH6QOUphOr-ChHMXJIPZPsOt5mL8yja3Isj8jFPcjw5FaIOPJrXqjqKeUX2qVogNzpFGSinYqLAe52_VYS7NoXiGTMcPsX_lP4g4se35PFVZL01yXA7KHth-kSkokaNx0LMZtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 178K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 04:29:35</div>
<hr>

<div class="tg-post" id="msg-67974">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👌🏼
تنها
#سایت
با بونوس های واقعی
😮
به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
✅
نصب اپلیکیشن بدون فیلتر
🚫</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/news_hut/67974" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67973">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIGRzh-ulHO6eaC8M-O25hSdO7eJh7zR2Rhu1R-iZjrBRxbgfm-pWvpQQAZ1cqDz3P3mOE4mGUtKSHgbm15d6ei7CyD7SO-WNSCKD3U8VkV9D2fGTFYpZTBZ0COFKnj8t4BGosSETzNa48jZnFCSKDoWn6_tATNjTE3aHuoiIXaNpfncDe2CMqUI9Mx1gJ1NdvPBzBITqtd8gzFOtLk6CSTHcRIc7EU2OncRbmgfQ3NzK1fn_rj4S9yldAHxMlnBrv1_j3zKpI7FMFMvA5CgaMEzmyAfeoL_h7NCnipclSEMbphyHiFFjuSYA6ffrZvxMhXDjIDG6KH8GhuPojvDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هر
1,000,000
شارژ مساوی با 1,200,000 شارژ در سایت بدون قیدو شرط
💖
💵
هر بار حسابتو شارژ کنی
0️⃣
2️⃣
🅰️
شارژ اضافی میگیری بدون محدودیت
🔴
اگر هم باخت بدی همون لحظه
0️⃣
2️⃣
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a22
@betinjabet</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/news_hut/67973" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67972">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=VtZ-B3zgxpA8lgbOo7rD0oGbreBEOxryTvIS0MFiibEeiOGsienWSXuWAFeImVGoPU7FoOmdDviMCqEHV7ZKbz1Un3VavNzkG7OftmIilVnaCVC982IRPfzzuVFzWxfpIlUmF9R-a_XFn_zrKxHfBIUkQ-BJzG_4MIqJKlVzevEEL2ePhCqxkUM6O3k9t0goj62FwKbh4KK7JUQsXaxbeweJ8kvLBlNlCWCiQfpOYVntkxEi6TSDAQVAbJ2g-3t5j1eXHOuIVN7b5qBpcW00xg9eYLOTKA-TiFlDWJr_xSJUibAyGw7f7AhueMstn0Xv0bVfGYB-GZVvow4-_DhEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=VtZ-B3zgxpA8lgbOo7rD0oGbreBEOxryTvIS0MFiibEeiOGsienWSXuWAFeImVGoPU7FoOmdDviMCqEHV7ZKbz1Un3VavNzkG7OftmIilVnaCVC982IRPfzzuVFzWxfpIlUmF9R-a_XFn_zrKxHfBIUkQ-BJzG_4MIqJKlVzevEEL2ePhCqxkUM6O3k9t0goj62FwKbh4KK7JUQsXaxbeweJ8kvLBlNlCWCiQfpOYVntkxEi6TSDAQVAbJ2g-3t5j1eXHOuIVN7b5qBpcW00xg9eYLOTKA-TiFlDWJr_xSJUibAyGw7f7AhueMstn0Xv0bVfGYB-GZVvow4-_DhEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به اهواز بعد از حملات ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/news_hut/67972" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67971">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
نیویورک تایمز:
مقام آمریکایی گفت که انتظار دارد موج بزرگ‌تری از حملات آمریکا علیه اهداف نظامی ایران در یکشنبه شب (به‌وقت آمریکا) نسبت به حملات اوایل همان روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/news_hut/67971" target="_blank">📅 02:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67970">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فارس:
دقایقی پیش چهار نقطه در شهرستان‌های امیدیه و ماهشهر مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/news_hut/67970" target="_blank">📅 02:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67969">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
دزفول رو چندین بار سنگین زدن
@News_Hut</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/news_hut/67969" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67968">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/news_hut/67968" target="_blank">📅 02:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67967">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=dSOgpiTrErMNVX4TAfxpHPep2UWuy5s2zgPV_PIP9oF33JUMxxMVW9zbhQPIZ1ZUyJrqiHAaxJwOJO-zk5eyIgFpLFwJAjQgK7aQc73jYnFlwsOq0xTAs5dMg1XogDNGHDe3ylIsM_xyiL9O-YI0Dzqmx9xTepXf1y3dkQfbc5uy8LqDIU-nldTeinFMkKiSu2HaThsXBDPnSknMirDgFy561wIe3vFUQE1RW-6aqhVmcp4GlimxueBPf6e0ZAU1qAhmxL8NKTFsAltO7bHT7LsHSn1mg1XvNlG_97xIIFegoZN1NF_mUxEGzZAJQ52mAHqrTPRhEXjfVCMdpaLyKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=dSOgpiTrErMNVX4TAfxpHPep2UWuy5s2zgPV_PIP9oF33JUMxxMVW9zbhQPIZ1ZUyJrqiHAaxJwOJO-zk5eyIgFpLFwJAjQgK7aQc73jYnFlwsOq0xTAs5dMg1XogDNGHDe3ylIsM_xyiL9O-YI0Dzqmx9xTepXf1y3dkQfbc5uy8LqDIU-nldTeinFMkKiSu2HaThsXBDPnSknMirDgFy561wIe3vFUQE1RW-6aqhVmcp4GlimxueBPf6e0ZAU1qAhmxL8NKTFsAltO7bHT7LsHSn1mg1XvNlG_97xIIFegoZN1NF_mUxEGzZAJQ52mAHqrTPRhEXjfVCMdpaLyKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال شدن پدافند در کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/news_hut/67967" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67966">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=jQNdc05gv8wVSZiHdH3Xh2cZ9CYotcVX58AQ_piM7HyTOC0I4pIxm4nmDkIIkrRwgHxFoPtKoKuRAUCUCxcNxaEtHnbvG-AbwQ_KRicYFDOgZarzcPMPPoAniO4Cm-XQYCwq9jrQMDRG7-xWzyeyrOW3zBGgTR5sxQ0W6V1QPkM0KqGk744qU1txTGh1zw984W13Sd55XMY6iLn3T_roIX212EE_hFmREhw18HxhRIfdfQQRKAhplXXFCw386ShybEKj3whvfz6cOeKAnz1-Y8YrVXSET_Dkj2OhshrM5ZC3C-GVMvAAjUttF8hiHLJKqrsZWuxvs4pn_qGEO0Osag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=jQNdc05gv8wVSZiHdH3Xh2cZ9CYotcVX58AQ_piM7HyTOC0I4pIxm4nmDkIIkrRwgHxFoPtKoKuRAUCUCxcNxaEtHnbvG-AbwQ_KRicYFDOgZarzcPMPPoAniO4Cm-XQYCwq9jrQMDRG7-xWzyeyrOW3zBGgTR5sxQ0W6V1QPkM0KqGk744qU1txTGh1zw984W13Sd55XMY6iLn3T_roIX212EE_hFmREhw18HxhRIfdfQQRKAhplXXFCw386ShybEKj3whvfz6cOeKAnz1-Y8YrVXSET_Dkj2OhshrM5ZC3C-GVMvAAjUttF8hiHLJKqrsZWuxvs4pn_qGEO0Osag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویری که ظاهراً پرتاب ATACMS با استفاده از HIMARS در کویت به سمت ایران را نشان می دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/news_hut/67966" target="_blank">📅 02:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67965">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
حیاتی معاون استاندار خوزستان:
در ساعت یک و ۴۰ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه نقاطی در شهرستان های بهبهان و دزفول مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/news_hut/67965" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67964">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
مسئولی در استان خوزستان ایران:
دو نقطه در اطراف شهر اهواز مورد حمله با موشک‌هایی قرار گرفت که توسط دشمن آمریکایی شلیک شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/67964" target="_blank">📅 01:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67963">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
مهر:
معاون استاندار مرکزی در گفتگو با مهر حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/67963" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67962">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=urY3BTa5Dp83e3Hbevk2OqJH2OUk5yZjg2mDAN1q3nAdnllrNsGoJ3M-g3FTX6vZP6I3Af009rRP65liaThNvaEAMLP69_4bZYL8IBUVtEG6uZz7YZ3rw5O157XXH2i26ZFF5XIu3JA4ma-6GJ7_ph3MtWPHDGi8Vy-liq_VrQv1upBan2mqTfihV9aOG2zrDLzkS8IgDlWylIbYnOPrjM6vDXHoF_dweCw5aYhxJvTjaj9yN6vw-STN8W-RVNXcFFkbwxW-mqMSXlo1W3_68z0f95TWahnoehbOTAoZR4l3YQvn6WsD6dfNf_OWyRh3Z9INdxonu7CJrmCgXAlyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=urY3BTa5Dp83e3Hbevk2OqJH2OUk5yZjg2mDAN1q3nAdnllrNsGoJ3M-g3FTX6vZP6I3Af009rRP65liaThNvaEAMLP69_4bZYL8IBUVtEG6uZz7YZ3rw5O157XXH2i26ZFF5XIu3JA4ma-6GJ7_ph3MtWPHDGi8Vy-liq_VrQv1upBan2mqTfihV9aOG2zrDLzkS8IgDlWylIbYnOPrjM6vDXHoF_dweCw5aYhxJvTjaj9yN6vw-STN8W-RVNXcFFkbwxW-mqMSXlo1W3_68z0f95TWahnoehbOTAoZR4l3YQvn6WsD6dfNf_OWyRh3Z9INdxonu7CJrmCgXAlyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67962" target="_blank">📅 01:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67961">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=TPonUo2pOt-zeP4veRyLYA-s8q3sahoQUY2n93M8C7ey6UhwPGktcdYMnRCpZxGHHhWbOEoiu1Tm0jPFfQmGSaEI1QfTtzumpCJ1VvZxqOBKG-ZjXyMXoQIqAnJPHRnfEn8240JLvAkGeSpDoy7Y0Jzqv3s0dKSBr8saYZmu4cPelpdNljgM-w2EUOgzItYQlE2fZT33y5jQqP_sXeENxbpQgwn2F87SlqqSXGtd8RtMARvMiVRbePiyMVxImPLkNqNGu_2tqYCZb9-BqsfBk6sapZgMfuVF5mjdVLSNuN4YuAwdIA1EfNiAir-mclLHk3Ew05itsoXF01ZpW1Ka3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=TPonUo2pOt-zeP4veRyLYA-s8q3sahoQUY2n93M8C7ey6UhwPGktcdYMnRCpZxGHHhWbOEoiu1Tm0jPFfQmGSaEI1QfTtzumpCJ1VvZxqOBKG-ZjXyMXoQIqAnJPHRnfEn8240JLvAkGeSpDoy7Y0Jzqv3s0dKSBr8saYZmu4cPelpdNljgM-w2EUOgzItYQlE2fZT33y5jQqP_sXeENxbpQgwn2F87SlqqSXGtd8RtMARvMiVRbePiyMVxImPLkNqNGu_2tqYCZb9-BqsfBk6sapZgMfuVF5mjdVLSNuN4YuAwdIA1EfNiAir-mclLHk3Ew05itsoXF01ZpW1Ka3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منبع عراقی:
موشک‌های آمریکایی از کویت پرتاب شده و وارد فضای عراق می‌شوند، به سمت ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67961" target="_blank">📅 01:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67960">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1E06meslcbtXPuEIQCOY5DBc4Vc2yqJ8WWyV6ZGHmcmIfp0dmmiAwQjciH-WS9KHKp6TxgKsJ3Z0NDY6fhAXfIRoKjHKGnlm4m-2fOnRxSAXg0iDMCOGuA1ROesWCS3Ub3uNz8j7rNU5K5eZcLdjaNxOtPAg7X5MR4WX_x32nwwXManLw02tzlslooiToO_vS-KCvrCSM_CTjU281-xVX3wTIzOaAuU6dZeidvbrLX5Y5wQKNmfmbYpKjcmXxXQ7RCS7k9ZDdm5OG1VudxhGgTl7bKKukKCqTHHaq0IKfU2a_D-r3LZB6JRB_9uv7gNtUvhqYE5Q_TvnTdI2isZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
ناخدا دوم تیم هاوکینز، سخنگوی سنت‌کام، به من می‌گوید: «در یک ساعت گذشته، نیروهای سپاه پاسداران به سوی شناورهای تجاری در حال عبور از تنگه هرمز شلیک کردند. هواپیماهای آمریکایی تاکنون موفق شده‌اند یک موشک کروز و یک پهپاد تهاجمی انتحاری ایرانی را رهگیری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67960" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67959">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
اهواز رو دارن شدید میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/67959" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67958">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
گزارش های از وقوع چندین انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67958" target="_blank">📅 01:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67956">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBQyMX5RaB_fae77_Ghmv8eWF1lqj4uDqIgCNVwxyXBZ_sBxPMRTyEMkH3fzEBu48W-341vSSx9uWzf4_sDVLUgYxnCgG0HvCH2S1Plr4K0vt2rAGqCSATpIUGsj7QGpIAVEqdbfQiQOPmrkwNVjrbyTuBq8yuSM82N8hJ7PeLorTHoCrvTX_t4tYwSfZUN7AGn1-R9u4ciDkVaLMkT2PeDhDffxjXPalJYHUXTKUd3Zo2SERZ-LcmrAKZzjG3T4fN1KbCtx0jk3SF7HCYYIinaHUzvu--UzY4960Z42Cn5sLrD6C_EtVmQGwAHl2H1umY2R7bEVhECyKlTJWRC3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=I96OuIiNq2WNNeB4nxs2hY9jxmyaHCDEPwhiSLqCzA0hSM90mtniuaedsd387C-d5kfeGJLgz33XVkvUuykOsy8S8Te_oBIa06OPgi7Is47SDA-XSCzsUVI8nmnqZQgmOWPWw6k0nvx5FQt0ua-g9SidtUOX_kmxvvjDTrx4yqvXqgiNio7JAxVdDnvhKvyPprR0ecLuP1DaNUC0hR_Drgx567Qg82FIY4Ro6WbbFMOYTgGhUcdxM_u6FBwck5JDtgl0Cbv_wfCzFCEUZy0aZqakcoz4Vh1XRn16n1g_jybqzVG-KWwvW5zzwK0whAc3g9Q8RvCUH5dhFzb2gNGpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=I96OuIiNq2WNNeB4nxs2hY9jxmyaHCDEPwhiSLqCzA0hSM90mtniuaedsd387C-d5kfeGJLgz33XVkvUuykOsy8S8Te_oBIa06OPgi7Is47SDA-XSCzsUVI8nmnqZQgmOWPWw6k0nvx5FQt0ua-g9SidtUOX_kmxvvjDTrx4yqvXqgiNio7JAxVdDnvhKvyPprR0ecLuP1DaNUC0hR_Drgx567Qg82FIY4Ro6WbbFMOYTgGhUcdxM_u6FBwck5JDtgl0Cbv_wfCzFCEUZy0aZqakcoz4Vh1XRn16n1g_jybqzVG-KWwvW5zzwK0whAc3g9Q8RvCUH5dhFzb2gNGpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویر مربوط به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67956" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67955">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBeHrAd🇦🇷</strong></div>
<div class="tg-text">توالت + دکل = برنامه طوفانی پیتِ پرس زن</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67955" target="_blank">📅 01:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67954">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :  @News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67954" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67953">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارش ها از انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/67953" target="_blank">📅 01:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67952">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYKDXQAd-ALiW58Epv-x9z5nLHXKFysrnOCjCi2g2Jnm01SIOpklZWm5LqdH9IwcVrfgvqKc1a0jSvZCrLxnX4zh-VWt-zzlSjM7IjnyaYV2U8NLwv77AXV5nxlDqvxRvldCpE8Cd8OIhySe8BbKeBObP15pbYq95B_s6NKMrYz_HjjE6vi7jPh55uuWuL23wZP6wvG51txNRyZM7SdQdoIHTylQsIGPKmnZ4ggOJaNYFyopje-ERGDFomEClCCpdgNbtvmXkyatjBQhP5_mg8WtAJAqer0ImGU3ygweX7kZbeTvzO2tnSWKucYNFF2g5jybSvhKIqKV5q6t7TPQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
9 سوخت‌رسان آمریکا در حال حاضر در حال پرواز در آسمان خلیج فارس هستند
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67952" target="_blank">📅 01:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67951">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzSqz5Zavpulqvhjx0loUWnEzLzbgJhMRPt64qSyLscg3Pqsm2wJJAemcUxOMpIJ5Q9f0rgE8fo1II6mrOSNVXPIDELalVuasDXydX0Jj9FHnvPemGSBht4OI8TcGHUC3icBtdB-YcXCjyL1MT7CLps1JdtFOPssZO08y1EIsqyvr-d4qPgYp5_jFWwgjGibLFfhzhR56gSz4GG2woDhej26oyeauIburclsa4LPX4Jco1v3PnTdoTRUVahlhdEuD4VC35sMv2tPfEszejhFSKpDKpbrZNkBwJ8yWlwuwdZPTVpiVaqv7c1NffDwNKkBPBS26E3AHeDl17ZsvfC7xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویر منتسب به انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67951" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67950">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivEhjiiM1al8QbMYZ8Z9ONMTdhtwXHebYifLOOwJL4-G1ZMPv-MegSBQ_P6NWRIZPe0LekpoxmYhwZ4CkhDDEAZOxKTAEg_1iBm1FCVOLtRKjjGyFE0uUfvagMKq-VH44EMQfiR90paWgqvWuPLqWQtJ4eKZNBEtJoJsYBYgT05RPv2GAM6JZ51itc04LkdiMQfyPkFOAlpiekZCt7jPywnb19uYFis6-Z_aH_YnT3g6nbAhDCBEqlgDzYw6WpWPmW4dlHc851YJZEeatb45iRZYBVzuFEpJi0-OadBEniVEUfONw3MaB7T7wrVsHvhRgAOZ7PMbIgq0cMq3T-dZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر من زود تموم می‌شه، چون:  صرفا حملات جنوب کشور هستند دلیل حمله هم حملات سپاه به کشتی هاست و این یه حمله ی انتقامیه، مثل چیزایی که دیده بودیم قبلا   یعنی در واقع حملات، کنشی نیستند و واکنشی‌اند  #hjAly‌ @News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67950" target="_blank">📅 00:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67949">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
❌
دو انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67949" target="_blank">📅 00:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67948">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67948" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67947">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyJgAwBnEijqO5IqvWWe3ugsLoJRoBwxOlL17tPzvK6_W76Ea7mUKLFq7GWHUJvP8F3tPmCZxs2ZVb_lPKd95O3TzhDfncW0PKJCXM9Xu-oAhFx4mdPOkOPOJYMcIm2zi1Kb2-mFIfJq9anmej1riCvzKlmfk-VfGNnUxaqCcssrQou1fuv11kvIoPcqYqu4NtDXswN9pd5XODJy-apk9abtTFUsIBbKacer7VUuPgm177xO_A3EBOEhestfp2ngSYA1FrLpqJ-G2oZ2EdGdmPq7HBin1240ZdlG8TEwT0FbSIyWhqoD1MJxQF_tjGqId3VkUBeOLVS-beazG6RqeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
ساعت 5 بعد از ظهر امروز، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به توانایی خود در حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور داده است تا به نیروهای ایرانی پاسخگو باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67947" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67946">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIJLneOgg6UA56tpibJ_282NWRf5P8bZWUDfd6sFeCDGVn3q1gzlsVns1s3mSlcs7R8X3ynM_KKuJF596WH2wrs5liTZ7UqOopwIIFQFC5YcXY83_e3VqyRepBKfVTCaoC1twpnK4vSIokTRoqsaYspRJpwQMsFX1Wuoxvl0vBJkCgWeB-F719dvV5AToHSB12OxKrGMQ8xJSoDeYGtrURtjlELDGSYfYszl9j6M_QeVZ29tqPWoG5pAQ4Ldn8Pc_m-db1XwuAbPte22ykhcLRYidXf0R7cRjcQ3DAWPQ50ud00q3mHUPJ-j0GohP-BD6YytmdFem5lJAWp2APMYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67946" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67945">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇮🇷
ممد سامتینگ:
اگه نمیتونی جنوب لبنان رو امن کنی،
پس جنوب ایران رو ناامن کن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67945" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67944">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67944" target="_blank">📅 00:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67943">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
❌
گزارش های اولیه از انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67943" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67942">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67942" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67941">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به خط ساحلی جنوب کشور آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67941" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
پنج انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67940" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
❌
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67939" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار شدید در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67938" target="_blank">📅 00:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67937">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
خب مثل اینکه شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67937" target="_blank">📅 00:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67936">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=W-0IAM52AnOhzI-UpTIbR3TsjmE-vJd-SvUyDXM0JmIzdOUXDRZvyj_JVGAYjF7rwRWUJ3LHEBjQY259quvoA5s_ej1Sf1lvdvOXgOdTvrVvt0T2td3-lPZZ34GriKlhSrVr4H8Lmm0wzXdlAAPzWzEou4YLvF3OweXpprKc2gVI2eoz9v3gm8DqmE05J3PayZlpKcBJhTwFeQjoRRKUbPjSUBORObEffldSLhWlgQVge2NORZpdAnYsABcV2hdgKGXc7csW1_csxYplGQ798-poGtoqOWhx8fvAnvnz_rhE1PRaUvub9-mxWA9AnwTDzUHdohk36eZSQo8m33u6Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=W-0IAM52AnOhzI-UpTIbR3TsjmE-vJd-SvUyDXM0JmIzdOUXDRZvyj_JVGAYjF7rwRWUJ3LHEBjQY259quvoA5s_ej1Sf1lvdvOXgOdTvrVvt0T2td3-lPZZ34GriKlhSrVr4H8Lmm0wzXdlAAPzWzEou4YLvF3OweXpprKc2gVI2eoz9v3gm8DqmE05J3PayZlpKcBJhTwFeQjoRRKUbPjSUBORObEffldSLhWlgQVge2NORZpdAnYsABcV2hdgKGXc7csW1_csxYplGQ798-poGtoqOWhx8fvAnvnz_rhE1PRaUvub9-mxWA9AnwTDzUHdohk36eZSQo8m33u6Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Rip
🫡
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67936" target="_blank">📅 00:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67935">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTbp7J_X24O3OJtuKsSw2ZHv7Fo7Co8VJZtmrV4JhdQGn-pPrRji9KeeP69VjSuXo7xfei0pP5eE66zjKqBdFBupQofgYgoc-Iv528jCGqhnBnhMlJbO056iGdspZK6nduHG8M_LgX-dZfddze0AvrGEzLMBpJq2rqxPrFhAvaFUaoCcYA5d0HTFpOK-bMqkzXn2JVIZwnoWHkylRsX_bwfX7uaRXmLyJWZzMhLihcOSxEZMsb77JIf7RZMLcZ7AAWVAR8TO6ZZOueN9txkEeB8f8DsZs-IOcyanc27jxr8JSe7ZmjhRC5MlX3JtrT7F5AkS-3Tf1eKqRCcmySpohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
❌
ادعا: دستگاه تبلیغاتی ایران امروز مدعی شد که سه تن از نیروهای نظامی آمریکا در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✔️
واقعیت: هیچ‌گونه گزارشی مبنی بر کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد و وضعیت تمامی پرسنل مشخص و ایمن است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67935" target="_blank">📅 00:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67934">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=vq3v7klb2DduuXEg96rByMCQxtb2a-Pmlu-pCZWPDWyrbGfUVy5CKvCbdURQCxPYVXqIIp7cZzmPzhqdV__wJwSj0hUN59tmjM6jjjdJSYIT84RpgqV5WZ6X1w7uOolGmXw0eDeKUHqJqyGm9abN5ksLEL_393KOZlRfwFOm0RPNE6dIyG9-GeGsLy37U9w71N8Bd-6EU5SlTb29NTSs2EIktJXywNlZrIyL70JGKhqkuG7Cce7dURuWkaH-2p_MQxZxJLvpOBuJNa9g92gMXeDPYkQayUYFFavZsQUySzzz_1L_snOn_1B54RbEHMZAo-LPUuXysN9S35AIepRP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=vq3v7klb2DduuXEg96rByMCQxtb2a-Pmlu-pCZWPDWyrbGfUVy5CKvCbdURQCxPYVXqIIp7cZzmPzhqdV__wJwSj0hUN59tmjM6jjjdJSYIT84RpgqV5WZ6X1w7uOolGmXw0eDeKUHqJqyGm9abN5ksLEL_393KOZlRfwFOm0RPNE6dIyG9-GeGsLy37U9w71N8Bd-6EU5SlTb29NTSs2EIktJXywNlZrIyL70JGKhqkuG7Cce7dURuWkaH-2p_MQxZxJLvpOBuJNa9g92gMXeDPYkQayUYFFavZsQUySzzz_1L_snOn_1B54RbEHMZAo-LPUuXysN9S35AIepRP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
سخنان قدیمی زنده‌یاد مانوک خدابخشیان در مورد لیندزی گراهام:
گراهام کسیه که به کنفرانس های محرمانه بیلدربرگ می‌ره
کسی که می‌ره چنین کنفرانسی یعنی از پشت پرده باخبره ولی اجازه نداره چیزی بگه
بخاطر همین لیندزی با هشتگ Make Iran Great Again می‌خواد به مردم ایران نشونه بفرسته
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67934" target="_blank">📅 00:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67933">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1TU8_d8sA0cMqBREG4hLKtGbe7VEKFV07xg65TSowvI9IBBLdVus042Me2KzQGwca5_RSI8Rs748-nFKj8Lb0nscddv6JI3vDswJCUb7rrk67qUNDAVx6ernVlaEd3C39EaUNtBLzQJh4DZmH5VQ-R-mQobVgX4DxZ030i28MbRXoOmg8sr-zlU1_HXLWzAUjey3WHAPoLUkOAShuMd_GR-xHVmTThUAbZADnliZ4H6xc3PZtspP9-g9rdrnSSyeF-a2QXJ2j6fSbzBw7ma_UejaPeHot1pE1RDljdwI8Wnx-zyilSUm7fuQIzBpNJqDWi7SmAkPtPeCtC6squ7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال   @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67933" target="_blank">📅 23:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iR6GW_XJfD2Rt_PG2TjqEqm8WPebjxd3x5VeD_IKh0nNaprnb3xCPrNLJac1KDSefTnbhEgLQJgB1km_7m_HsnTWsK7AOsJGFZiKGfzPL8V-n5qyWlCPn7CkxtCP08rsA_OFbC_dag1qWrRkVRHM-1rNStJfRqgBkYF03B8fM6aaxWNU2FhR5wfHqoPJquaPkod0j0CGaI8_Qm_Q2c5HBzpMjrymHxViyGpn9ePHP0uHSjs8p5UgggezbIr5m0w05FbU04KjqYqsAQuqQKvz-IIy7K7TDU8wyvbUZ6ZCQaq6QkbdiZKfBPKxjhFu7KFkVY_MML8GEs-tOdm1AxocBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjPLheQG-KlbONzYDK2AUtH4s5JH-YLUyDCpCpnQLqBe7ZmpM-DnphmkZxiHHFME-PD12jAe80iSP7lTxAxuw76gdiyPlAucdaRWWto8nPdJpiYVTW6FLjI_T_1IvJo-wjXyFN5LUV-UuKzeN03iMwbBUZ4UC-RkDlH6Ufi_-dahec51NcW_j7_k6VYG8x641ev9Q5waAFrYIDa2lgmkv9TtOBWDUUPiD2BHGxTnOlqHYMY4HvKggu9LDMpYsFQejLZsjTO1hKPpzWWDPwq1hr52H-5lwqvh6JdZAE6DOJpLMaaLj3Te_hFNqmZW6qXE6BL5UiX0RWybeFKIbDATYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67931" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AalxPY4otBZk6a4En7Dx3zaumiTvRtTk2BidDx6PhQZ093qvsbAtR7dAV0BOYrcbMgF5u3BI2jGMFjX4DIbECPIpYd9RZq5zLAocXmE126MJ8YMA4v2tuhjajG0ZtMM0HHH2YtxtYM1oB4ah00meLaFX7ETvD9_VQAdbCZgURR1sH2rJFtLn8dPetijZD4cTOGDUS5KpzBCSxvgp7xlxEsOEogO3ek9lMRpi4mMHNSyYLMMQUsa3qawX-1Zp2RH60cTIeb7qPBmUfCtjQD-g_rkOQDAYi6D4fWkTsRi2yRGFsl5u8jARTMnHj8GpIGMBYUVoVTmQc5kvtZSzEzeoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5YlkypWvWJbu48d1tWyXQLuVh91FBvrAwuYIgnYbCeZ4bFewj5V9IoTZ2IvGOL035K-ZJ3kLKgYlJqracI0mILHdEqtYsRrOBtycS4c0kLYQxYCs00WbKJi4r0TYxWWhn84zflSo_NKXoSp2OEa_-AKNKnq_AOWi62dvnwf4JU-oruvTO-_MPWOHIKUKeEPvm76RRKYHw8KMMnu0E0ykzCpjwC8xPL-GwKHxX7cMIdyd4hF4xvKBgSCLrkomFmcGvxrno9ogZcv8CSNZEY87IqqSG-uAlRwMcOSGkHxRK6nQJVe8kLqdcTt8KX6-mhGzgW2orCawR7745uvqKGJRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
🇷🇺
لومر، خبرنگار جمهوری‌خواه: ممکنه ایران و روسیه لیندزی گراهام رو کشته باشند، باید تحقیقات صورت بگیره
همچنین FBI هم وارد تحقیقات شده
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67929" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=Whyn_5mo4dAqkMnbf5-y7KULAUwdTTGWqx1EJJOhtZFXyFd9fUtZAAXzvOfIwnWsl8gPvto4j78E-sVR9pCjH-MauCa0gpeuySTK9T0cXJHNd74oMaugDOT7EOA5KGOTLrzogzzP3_COe572Vxi8naGbb9cV_mil7GbQ7bUp109Cyzu5XVbE1PKGALBr89DOWIf0f50CCqbTCyYIdePnGHAbKIOEQ2BGB2kQiUEIjaBsxMa4X-yq8hq6oba5azqPNW-FmYNqkpHnAwYO3arr3nB6vK-Iq723-vTZgmuNzewDTJ2p2Rigdu-qSu9SCh34fwXhEsXYmrTHCpwiPfVn0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=Whyn_5mo4dAqkMnbf5-y7KULAUwdTTGWqx1EJJOhtZFXyFd9fUtZAAXzvOfIwnWsl8gPvto4j78E-sVR9pCjH-MauCa0gpeuySTK9T0cXJHNd74oMaugDOT7EOA5KGOTLrzogzzP3_COe572Vxi8naGbb9cV_mil7GbQ7bUp109Cyzu5XVbE1PKGALBr89DOWIf0f50CCqbTCyYIdePnGHAbKIOEQ2BGB2kQiUEIjaBsxMa4X-yq8hq6oba5azqPNW-FmYNqkpHnAwYO3arr3nB6vK-Iq723-vTZgmuNzewDTJ2p2Rigdu-qSu9SCh34fwXhEsXYmrTHCpwiPfVn0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خرگوش نر به تازگی جفتش مُرده بود و میخواستن وفاداریش رو نشون بدن که اتفاقای جالبی رقم خورد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67928" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtoAyr_lay5ErF2lrfaS3lXQlakJWnEzv-tJZSnInRIJH9JND1RABSiUtr0lJa0eMkIERX18N6CesqXu-WAUQmxJCkJM3LC_hoUnX3jOty4oH2CxUShTrOuaYiTH4RTU-ECiHkO_tg4IPijBGUl9O7hfjRZLzESsw61wY9kvCy8w2199osN6PwTf6JlFSGigjZlloIIHodiQGbvA7EPHbR2qsboviFN3wHz2tM2jUni4Qd7bVYu24JgtueyBIgq6AuOvU0NFenduSSdBCmGWoN29nHtFoNiknZRv2K7gdka-2cmEzuD4Q9K11MNTjLfilGZZpN0k2VNZEj99mvV1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه های عربی وابسته به حکومت؛به تمامی شهروندان و مقیمان کویت، بحرین و امارات متحده عربی:
با توجه به وابستگی حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای پرتاب موشک‌های زمین به هوا به سمت ایران، از شما درخواست می‌کنیم که نهایت احتیاط را به عمل آورید.
در صورتی که هرگونه سیستم یا سکوی موشکی را در اطراف محل سکونت خود مشاهده کردید، لطفاً در اسرع وقت منطقه را تخلیه کنید و از نزدیک شدن به پایگاه‌ها و تاسیسات نظامی آمریکایی نیز خودداری کنید و از تردد یا عبور در اطراف آنها اجتناب نمایید.
از تمامی شهروندان و مقیمان درخواست می‌شود که این مناطق را فوراً تخلیه کرده و به مکان‌های امن دور شوند، بدون هیچ گونه تأخیر، به منظور حفظ جان و سلامتی خود.
پیش از این، هشدارهای واضح و مکرری را به حاکمان شما در مورد خطرات دخالت در این مسیر و درگیر کردن مردمشان در یک قمار بزرگ با سرنوشتشان، ارائه کرده‌ایم.
با این حال، آنها تصمیم گرفتند که در مسیر وابستگی کورکورانه پیش بروند و تصمیمی بگیرند که بازتاب اراده مردمشان نباشد، بلکه از خارج از مرزهایشان بر آنها تحمیل شود، در غیاب هرگونه حاکمیت واقعی.
بنابراین، آنها مسئولیت کامل تمامی عواقب ناشی از این مسیر را بر عهده می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67927" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8D00ijlgyxyRcSDswn21JO7vkgy4QVHV3zTfVgd9b9pnvIO51c39NdaoYybiHxEErr4-_0HeTR1CeUYS5BdDLMTJWYMjiBsMcj8ax5fWw_9dRLU5_eHTVW6Hp1O4_bIEQW3Rtvh2oyCbj2sQ7LyOxwDCIFMDZzdOgHbEZAiVbandkyvcKIYGAVWGFdPJh4IpMnBnYu8nOaiSvtcxHE9hsptOjgKdzJ9Rpik7s3sA3Qu8fttBNLyzg4yXNCNV9znCYJQHV6O9vcKDH-I8Mx4Lg5CAh4_yhvEAE_b0sWuch3fu9UeRy-5f9tuEUA2Ub09l7tlpefbudeliiswTv9lqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آکسیوس:
اندکی پس از تماس تلفنی با پرزیدنت ترامپ در شامگاه شنبه، سناتور فقید لیندزی گراهام در گفت‌وگو با فردی دیگر از وخامت حال خود خبر داد، اما گفت تصمیم دارد مراجعه به پزشک را تا صبح یکشنبه و پس از حضور برنامه‌ریزی‌شده‌اش در برنامه «Meet the Press» شبکه ان‌بی‌سی به تعویق بیندازد.
وقتی به او توصیه شد فوراً تحت مراقبت پزشکی قرار گیرد، گراهام با شوخی پاسخ داد: «الان نمی‌توانم بمیرم.
هنوز باید تحریم‌های روسیه را پیش ببرم، تکلیف رژیم جمهوری اسلامی را روشن کنم و روند عادی‌سازی روابط اسرائیل و عربستان را به سرانجام برسانم.»
سناتور فقید لیندزی گراهام تنها چند ساعت پس از این گفت‌وگو درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67926" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GL1fjW-gMmAYNzta1YXZW9oM9vOPOeDKBCVjjqiw4slkf6muMaXoyeexDMADZgG219wq6PRd0-91rlrHeOybTRLro5-sJHsqhjbbLc-hAy1Ldh9IjPSOSqiRzCAYGribJbAHTlxlL-oafuXN1fwD9DTw5S164UQNldffUdA-AyV3H9psDWn8hEp67s4e9tIJ5NlmmE6vyjLl7UFfkhUsiZ8RhThxF9Kgvu-V_V7G2zxsru_3QfWcj4fm1tbt4n-Povnr63K3jj86Cx5gP1uhcKK5S7sPwHzCwlroAPKlGmMZY7eeRPIcMR0qYeDW8vDqyUq4CMfyGmACWf1yLuPKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=GL1fjW-gMmAYNzta1YXZW9oM9vOPOeDKBCVjjqiw4slkf6muMaXoyeexDMADZgG219wq6PRd0-91rlrHeOybTRLro5-sJHsqhjbbLc-hAy1Ldh9IjPSOSqiRzCAYGribJbAHTlxlL-oafuXN1fwD9DTw5S164UQNldffUdA-AyV3H9psDWn8hEp67s4e9tIJ5NlmmE6vyjLl7UFfkhUsiZ8RhThxF9Kgvu-V_V7G2zxsru_3QfWcj4fm1tbt4n-Povnr63K3jj86Cx5gP1uhcKK5S7sPwHzCwlroAPKlGmMZY7eeRPIcMR0qYeDW8vDqyUq4CMfyGmACWf1yLuPKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کانال 15 عبری:
ارتش اسرائیل با همکاری همتای آمریکایی خود، در حال تمرین سناریوهای مشارکت در حملات علیه ایران است.
ارتش در حالت آماده‌باش دفاعی برای مقابله با سناریوهای مختلف قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67925" target="_blank">📅 20:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra87xl8jfzrkjyWJgdJiUe9DuyCGw3MzyYR9BxenGQuy1tD6fkvQwgTff4ffAljeCTecyvVL6rM58ynjoXSelTol6d70GJ0dlf5W9T41-ieh59XRVbA43OsKGB2IR7j6NdmTIfNutoV0Jm2RPxlpLRmnXPYkClMXAde40_9xHJ8NtGV3SjS-icjaEEZE26E3chIdWa4QlqBcUpmWSsQSQn-pEIYF6lj44KaVFS0NxAOI3bPWjbijcm0K_3CJQs6lNPr3As7furNBTWM25ONWOVv4fR1hGgtVzKVHwI87hKZ_czlfPeY3WwSCqwH0KMZMssfg9iqlxqOo-FcrkLDlZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8f7jEDwMbBc5Uc5CqnUEf2dLKS4neZAIynrdbP8qqrPDXqovQdre8xPiJPGkxCmcROyEwQ4UtVqypiTmCzf6brBUoy2dHFzYwaxshpuIc8SfFTJO_4TyJSLtFv3rzKIjYeuRVWORabOKk1ybxqBb5agFLBHDKGO5P9V0aXhKv5YwGsDvzUPUHt7Gyyy5tPDA4JwUewLH8VxYg2qDqbeh-K0_K1RF9KiUtX1oUucc7OIvx2ZLmNLrb1uKm7KG7f2qehyddaiG9KP73Ik9lGXJWTkhkrpKDepMESPCtOA1FDDRx5nPNwWvy50vGh-oj05Qdh4Y2-Qz5Du0AH-AftdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=lc4lP5NPArmAvn_2SddJloAvFIsx0tAf3GbXwoYcQbJjch0wMuyvOkYSuyBN0IkBvLAoRR3CRahHmsyp4FKLiWBBXSmsFtjfVz7ML81dnpI2GBFTbPCQFO3kN2_2yDYOkQyhKSjTozt5H54seu2mGXE_iwGqO5i72VfNyX7C0uKs_H87qxeskAwkxoevbRzo85Z6bJUoWOLN9vu-IXt4a5jSS7ukJ3yN_t51Bxcwyx09SKeYfkba4pmoxEM-KFRg3S0w-wx7EPvtzhMxhFr7iTtoOfu0eu7hnKhFQecNnYwdoX2dZ6IvKb8_n2l_KU0omOgv4BCzEWFg808RKdYPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=lc4lP5NPArmAvn_2SddJloAvFIsx0tAf3GbXwoYcQbJjch0wMuyvOkYSuyBN0IkBvLAoRR3CRahHmsyp4FKLiWBBXSmsFtjfVz7ML81dnpI2GBFTbPCQFO3kN2_2yDYOkQyhKSjTozt5H54seu2mGXE_iwGqO5i72VfNyX7C0uKs_H87qxeskAwkxoevbRzo85Z6bJUoWOLN9vu-IXt4a5jSS7ukJ3yN_t51Bxcwyx09SKeYfkba4pmoxEM-KFRg3S0w-wx7EPvtzhMxhFr7iTtoOfu0eu7hnKhFQecNnYwdoX2dZ6IvKb8_n2l_KU0omOgv4BCzEWFg808RKdYPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONzwFF1ViSZZ_22tcxLd_Hy_dmmXFP1AnU54XX4L2HLAgMFZgR9v77V4BOByttyfDVOlPHfVKU_iA5yIQ__v7jQ0iMIzf4q5fSFmg3vVh5b8GxTsCkv7ThqjFsMp7qus4RtHO3zjC1mylbmSwOFovbxMuQzQONn-_FljAFYMKbRZA0Kv8je_UfeWVTOTaFY3AcrqiBLGXI93mifQBWnUDv6YjWPJHuvoqE_YySugZCzqM_R5reUwkMP0IAdqVtBcuZ71tBaRWmimKnLJ_Kb7En8Jr5f8prYORBQeJvi2kf_OLJm8lNe_j3dTPqLRRYr2ycemh1arP9iLBBGeUjYc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=OQyuMFPJHKXnbblgWUgYP4ezo5epKY08eoLvmlzuPAEZdEWCQsP_yQwdem4ccrRAgr72AX5lGJVZ5P6qpQBOwsNQg9pN_nKO2LusZalQkv5TXAMKAnQt3xxg4DSd1Dc_OiDsG_2etXGfMauu-vnvwUzBOf9Sfo8tLojNKOmFAO0X9oFb0R_3UQQa_PWrzq6PCQQ6LUf3t-ZydiDSuVFrGW8c8SlGVjygC1FAM13mcIiuWD5jfcoJlZTEZ_JQeBcwr8zI-ig3g-faRAGISULFlEdoRTP-dz2XHqR2cSikGYZnPLUlWth1LkaGsVuDVcEyDHjSfMmyXXV_EdxwYBcd9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=OQyuMFPJHKXnbblgWUgYP4ezo5epKY08eoLvmlzuPAEZdEWCQsP_yQwdem4ccrRAgr72AX5lGJVZ5P6qpQBOwsNQg9pN_nKO2LusZalQkv5TXAMKAnQt3xxg4DSd1Dc_OiDsG_2etXGfMauu-vnvwUzBOf9Sfo8tLojNKOmFAO0X9oFb0R_3UQQa_PWrzq6PCQQ6LUf3t-ZydiDSuVFrGW8c8SlGVjygC1FAM13mcIiuWD5jfcoJlZTEZ_JQeBcwr8zI-ig3g-faRAGISULFlEdoRTP-dz2XHqR2cSikGYZnPLUlWth1LkaGsVuDVcEyDHjSfMmyXXV_EdxwYBcd9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
دقایقی قبل از فوت سناتور لیندسی گراهام با او صحبت کردم و "او به جز خستگی حال خوبی داشت"
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=nDyVDHYaY2XeNg8eAlcvHXxok62NO7VCsZL75LAbzUSG1T5fs4TrCOaYYNMZ_7u6yXG2NmWscSGSzZNF_iPVzOr6aA6VZpxja2GcuHJGsWvRqA_hEaNVHASxJ5Ilufs_Yo48XjAvklKkdy_hfDrjHOmkPETMwO1UqHl86h_fzJLQwriX-6CRM_c-Z7W0LvC5Hwuy62AVxMZ2ynSg5WvYotCbu8ssm8Hs8IBzTgDuVA3QqBON1k-pNN2h7-xtrp-OENvAwwRU7l7zaEKvCywekpgFIVbBQIzp6csDiCBw0TtSqpAB0ZnBXz8FAQbDst0qtIx20z3nPWsGah0LFbF0Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=nDyVDHYaY2XeNg8eAlcvHXxok62NO7VCsZL75LAbzUSG1T5fs4TrCOaYYNMZ_7u6yXG2NmWscSGSzZNF_iPVzOr6aA6VZpxja2GcuHJGsWvRqA_hEaNVHASxJ5Ilufs_Yo48XjAvklKkdy_hfDrjHOmkPETMwO1UqHl86h_fzJLQwriX-6CRM_c-Z7W0LvC5Hwuy62AVxMZ2ynSg5WvYotCbu8ssm8Hs8IBzTgDuVA3QqBON1k-pNN2h7-xtrp-OENvAwwRU7l7zaEKvCywekpgFIVbBQIzp6csDiCBw0TtSqpAB0ZnBXz8FAQbDst0qtIx20z3nPWsGah0LFbF0Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کویت کمی قبل
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIifafmDSEBBc-ViUPKz6RHQTT3wIkjG56uj3qMNJXkRz-PU2dtcEmCM5kq4UEOXMqJGKeUf0Ag2q8Bx5vT0Op8pq1XxQzQB4wzGs7WQ22TUlWoU4457WykFDVEq-qILMDRMPEsUH-iIMC2NPZeVwiV40NU1Z9b4jPV1mkU12K9nBHx8bo3H0S-F3-DWUSB2Z72ZQXGOALWSK2Dw24n9C3jkyqAWLkhy1eTgJC8aThlBNGcU2tMT6VNfAgzV0OnKLYu-yZ9Pvwv1iEFLhXINecu9WNGfOmgPCfv1KjW1dBvGLF_1a0csbwSyD3U-paifcsmGU7lVsAr307xxrhX2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=oBQxEyIvTwB13TLtRDP1zyWR5SQiHZA6a6Dc5kLpaAhBgvNIjaqG7UfQspU0CCAxmNoEbbJlTI2KFxon5V_pOg5Kx4HaT_8YAEFmIEu_RNivIIeowsNmusgchdflxrpfcYHzdeuaD3o-LJKIvewCTS5kyTCLdxvRxKsOqL-eK5ZiSCUMq5NgpHAXm7tr-dDBNcABjAW3mKctYrmKGG_EBqnzH4K2pmU8c-yIZ0eco7P_fs-QUbRGXN0Ebkl93vZjMPxuEf_h_E888xpE-HF7JdMO4haK_xt549Pyo4WCDmDyVluQrqpY7VnZXiWNAnBDUJSI3zIm_w1xgh4njryrSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=oBQxEyIvTwB13TLtRDP1zyWR5SQiHZA6a6Dc5kLpaAhBgvNIjaqG7UfQspU0CCAxmNoEbbJlTI2KFxon5V_pOg5Kx4HaT_8YAEFmIEu_RNivIIeowsNmusgchdflxrpfcYHzdeuaD3o-LJKIvewCTS5kyTCLdxvRxKsOqL-eK5ZiSCUMq5NgpHAXm7tr-dDBNcABjAW3mKctYrmKGG_EBqnzH4K2pmU8c-yIZ0eco7P_fs-QUbRGXN0Ebkl93vZjMPxuEf_h_E888xpE-HF7JdMO4haK_xt549Pyo4WCDmDyVluQrqpY7VnZXiWNAnBDUJSI3zIm_w1xgh4njryrSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پرزیدنت ترامپ:
ما آخرین جلسه را با آنها داشتیم، آنها دیروز با یک توافق موافقت کردند، یک توافق عالی برای ما. نه هسته ای، نه این، نه آن، نه هیچ چیز. آنها همه چیز را رها کردند.
و بعد از آن اتاق را ترک کردند. و سپس در عرض یک ساعت یک پهپاد و یک کشتی را به آب انداختند.
گفتم شما افراد مریض هستید. شما افرادی مریض هستید
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILJVbCDkgMHwJEhkqCwY2ibWVknrNI3ynRSAwwbI3JUX9L6afyWcMGydNVGdt9IrtWJ7Ze6L_p430oynbsxrtGWpDsNcvdtDq-ry1BJjrQ5kro79mhTJF5Wl4PtZQsJvDs-DW8-NgJPSILp2iE-iRJEuRUvP55V9IB7eF3G0uHiLc29scM2QbhqzqKjvNX-m4BaKFIM_KRwN50xuRJW6530VWlTETs-7Xi_0UT68cCenR5KAfENWeVn8j29FHmVsyjDFTi60Q1p0kZSlvfcOKUJ2_IJYDhkTuuEmfpEqEXpZs69HEfPGVFUlRMHaDDeYXxFQ0pFps4qQ3oie6JksLWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILJVbCDkgMHwJEhkqCwY2ibWVknrNI3ynRSAwwbI3JUX9L6afyWcMGydNVGdt9IrtWJ7Ze6L_p430oynbsxrtGWpDsNcvdtDq-ry1BJjrQ5kro79mhTJF5Wl4PtZQsJvDs-DW8-NgJPSILp2iE-iRJEuRUvP55V9IB7eF3G0uHiLc29scM2QbhqzqKjvNX-m4BaKFIM_KRwN50xuRJW6530VWlTETs-7Xi_0UT68cCenR5KAfENWeVn8j29FHmVsyjDFTi60Q1p0kZSlvfcOKUJ2_IJYDhkTuuEmfpEqEXpZs69HEfPGVFUlRMHaDDeYXxFQ0pFps4qQ3oie6JksLWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
و شما بدیهی است که یک شبه دور جدیدی از حملات را آغاز کردید. ایران یک شبه گفت تنگه هرمز بسته است.
سنتکام امروز صبح بیرون آمد و گفت تنگه هرمز باز است. کدام است، آقای رئیس جمهور، و چگونه می خواهید پاسخ دهید؟»
🔴
ترامپ:
"این باز است، و من نمی خواهم در مورد آن صحبت کنم زیرا می خواهم زندگی لیندسی گراهام را گرامی بدارم، بنابراین نمی خواهم در مورد آن صحبت کنم. قبل از تماس به شما گفتم.
آره بازه ما دیشب آنها را بمباران کردیم. آنها افراد بسیار بسیار شرور و بیمار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=VbsOHVR_6tvGgvV-yEQEIhWKwH_ZmT_z-5HGED2FZ19iyWaBI7sN2sxAP8LXotonlB9qFPJ_qhPxSgUSgY8PWJwOfSCNBG6TmVVLoWMTSd1HFhP1Vmty1TXqDUviwRSYJAkHiHxAa5a6vAa59G-krAq-8Y1O92YwyXM3HhlyVsKchpo-vWPzchsRIHWaNXN6D_pgttdJLk1WRylGf9TfnpDczH431_4L6yU285zCfFAnwjFR59F9XySk6l2IwSkonWK8YpFYijGdJFJwWr8FOuhkvtsK-fmjYEP7jFWgoTMVJg3XCOnTgW7Q4tyQoxZnjidw57mN88fokWGr23CjY5MVp5wj8hG_W9hmVGrhdEFCIDz2dNxn9k-b1PGxdVtU1COnlVHIQ0oqv7q43JWifmNzH-ZNyeZullXcWIpqQeIyoPZdx9N0MBKG3EHYcISDFUQ9e_RT112f6GN-EfDxKNdcX4QqdA5blRPDh4FA2y3pUj8yiHDBxFzRFa65i1b09_t6KYZakPxPi4NSKC_Gw4Xu-4PgVe-1ql12Cx2wacEe_AYLOc2ibJMolSQtpsH-wuanmeWgsIaS8Bn3wXnfN0fWti7QsGjywb10kGsbVu3Maf33XPoMTw5OF_Ks03QH-f1vnjn6h1-G4zGTQYywSNq-5Chn6CJmfvOXNxyZKr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=VbsOHVR_6tvGgvV-yEQEIhWKwH_ZmT_z-5HGED2FZ19iyWaBI7sN2sxAP8LXotonlB9qFPJ_qhPxSgUSgY8PWJwOfSCNBG6TmVVLoWMTSd1HFhP1Vmty1TXqDUviwRSYJAkHiHxAa5a6vAa59G-krAq-8Y1O92YwyXM3HhlyVsKchpo-vWPzchsRIHWaNXN6D_pgttdJLk1WRylGf9TfnpDczH431_4L6yU285zCfFAnwjFR59F9XySk6l2IwSkonWK8YpFYijGdJFJwWr8FOuhkvtsK-fmjYEP7jFWgoTMVJg3XCOnTgW7Q4tyQoxZnjidw57mN88fokWGr23CjY5MVp5wj8hG_W9hmVGrhdEFCIDz2dNxn9k-b1PGxdVtU1COnlVHIQ0oqv7q43JWifmNzH-ZNyeZullXcWIpqQeIyoPZdx9N0MBKG3EHYcISDFUQ9e_RT112f6GN-EfDxKNdcX4QqdA5blRPDh4FA2y3pUj8yiHDBxFzRFa65i1b09_t6KYZakPxPi4NSKC_Gw4Xu-4PgVe-1ql12Cx2wacEe_AYLOc2ibJMolSQtpsH-wuanmeWgsIaS8Bn3wXnfN0fWti7QsGjywb10kGsbVu3Maf33XPoMTw5OF_Ks03QH-f1vnjn6h1-G4zGTQYywSNq-5Chn6CJmfvOXNxyZKr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=ZvmWF7VKONIiNrKhPgtgyjCu_Pa6Aq_AuSVaDHS4_GcRxZ0b883reEeoaAYLYcR29sMnVlZevZDpmB3yR9YQLADPOIL-BR3FeoX4pa3FVQheDY9dtO-Z_dDTpDFxmGtFO7Excl-8Ua3FOiZn9VnanaUd18mPYJiVilrnp6yPLf5Mu5andhN-5YuKi0V3B5alnSZ08bKGO8wiTodsHAh5mg6RFgnUfWHzw4v7NWbnJsQ_qitciiN07gzC12WbiFpCAr2FgJTWMsttPhg_vWocCspsXNd7_QVi9QLsrjirMkQtdV3YySJANxk1OJPyAJ7PYFSGzUft8RFDr9A2HePqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=ZvmWF7VKONIiNrKhPgtgyjCu_Pa6Aq_AuSVaDHS4_GcRxZ0b883reEeoaAYLYcR29sMnVlZevZDpmB3yR9YQLADPOIL-BR3FeoX4pa3FVQheDY9dtO-Z_dDTpDFxmGtFO7Excl-8Ua3FOiZn9VnanaUd18mPYJiVilrnp6yPLf5Mu5andhN-5YuKi0V3B5alnSZ08bKGO8wiTodsHAh5mg6RFgnUfWHzw4v7NWbnJsQ_qitciiN07gzC12WbiFpCAr2FgJTWMsttPhg_vWocCspsXNd7_QVi9QLsrjirMkQtdV3YySJANxk1OJPyAJ7PYFSGzUft8RFDr9A2HePqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnzn_f8QP17OdvKF-QQsUfVq6zYcROJfs-SvO7LXojzMupmFpvpZTNB1WBwXhKRAdkIOwMAv54GD-BItuIWXc9SVpiV_TH-BvRt9G-lC96G5KaNRmR7oJcFC0diVyGSwE8NVobDbxZwpBLdC1HHUl0f_K2YALeOhdoL8yINT0gfIN_Zw3kzE2RL-crDMeZ9LXk8E-LkXgETBE4F6Ra17UPFDtl0gjle2MQssOVPJvQ3nR9mCViTPN1HRGoxZHkCEQ2kGywphn7BuGMFTyP61bOF7fuomR5UD3EFji2nsy3Ns6TRxMSsQUC7ORQiPTl7zNLCLL054Hr4zmejwUQkhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwrqi4Gq0JmwY5e9XOy1rrFahUwnsHeghMma-FU3g6Id4ip2_vthirD9fKhaI8ASQaUbqPhcx3yLFVIEXJSWVEf5ay6pRYTc6SLf0I5HPt70bk-wkajV7CXxejHHycSA2zLJRD7i4rrtHVH_GdUZIwzGarrr4bi5LtiPDifZGiPzzfvr9_rSuCyQnGAgl2R4Hcxi1K80CSJ46dxb_sNVo2emn9YI6WQ1yZWW7movivEQ95vkEzXBdHDNgko2k1neAx2-S64ts4NUTK1bSMc8T-185lTZAtOB5C_rCCVx1ZM94iI5X9Kg591g74daNJp1gzhzbHEBCP8w6op8BBfPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=F8VHoTUkgGx28dpmEvNPRrTOnk5qDA01cRMYFl3jszdnOAjG3BUGhENfAAA5Q6vcqXsW0BH1IyaYKzUPZhuNYiTTKjFx2HzIrt5U3tBZ6OGVExMvNjjfhqf3az8MUvw75rmsahHi5IuqrZgVptuoXfXXjntqUl3b_sojeNYp2rW7G4AGKtsFrx0lsJjlETIDrkJ_cffbr__8REo8UmhfUR4h9XAkHLKzvR-PL4fyxPMGS_tfUAnFGc-x8DkpMnbfLRxAqZswor5mvMrmJ97fItLYZCNf5bRhG4yZY39RjWhgd4OsGeHh-9aOYQ_bNoOSvpLoZJaoW74U0IGvIRBKsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=F8VHoTUkgGx28dpmEvNPRrTOnk5qDA01cRMYFl3jszdnOAjG3BUGhENfAAA5Q6vcqXsW0BH1IyaYKzUPZhuNYiTTKjFx2HzIrt5U3tBZ6OGVExMvNjjfhqf3az8MUvw75rmsahHi5IuqrZgVptuoXfXXjntqUl3b_sojeNYp2rW7G4AGKtsFrx0lsJjlETIDrkJ_cffbr__8REo8UmhfUR4h9XAkHLKzvR-PL4fyxPMGS_tfUAnFGc-x8DkpMnbfLRxAqZswor5mvMrmJ97fItLYZCNf5bRhG4yZY39RjWhgd4OsGeHh-9aOYQ_bNoOSvpLoZJaoW74U0IGvIRBKsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFdw40W9grpatxFeJ7v_7Wm4wGAld8aIG6kV-8KWs1a2BJpaUqK_YS78QTRkmB9esGrCVTJDioEQNDivKj5urfomolVVx8LG3MEPq0dMlVL0JjriegcWL6uWnp1xJnvUChuKd5Ag6nlnI35unLcw5tGyRFmSZ1NbFhBqs8KkAk6AkY0Ffe_7d4N5I6YOH_P13-5dm0wuy56nMAyTFeh0bDErsvALsMXvaGwR60k0Ci2YzMeBHiYwkrSe8l6V87Cl9I9SgP7pTyvox3fq-aNx9USMIRR20VsbzO0AhGRrAOSyI7FPsunkjhPb_JK1fqbmKzODWLw-UTQBabT4PnpIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=GfI5UdH4WV0Z2KCWv7rX1Kh5wcgVOZIb31et2klQR2yOUFcu2V_VjdWWMy-bq2WgovhH3NS3MwLmGNGL_8UkXTkSq4xmQAW_JHbmhqI7Lr8li3xrCTsYlzuy4Hwh6PLtfbSImUIy7YfatKJWAt7ThgQmdTOC8_gFo7SVDWfn8Nc3GxXAO08uJE5oC-4z_kYERLvj7whUWlYDhz-Flz7MCXA4Hq7szOo6OtxDZkUikq6ZWwJaVtLy6WqNfJYiyTwlUROiWbEpXQF6mH4z_Kc2B8ndGjpw0DFV3T2ipxasElcLdUPWc1-BiEyfChioqpkIZ55KfUicxSDK2cr6XA0whQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=GfI5UdH4WV0Z2KCWv7rX1Kh5wcgVOZIb31et2klQR2yOUFcu2V_VjdWWMy-bq2WgovhH3NS3MwLmGNGL_8UkXTkSq4xmQAW_JHbmhqI7Lr8li3xrCTsYlzuy4Hwh6PLtfbSImUIy7YfatKJWAt7ThgQmdTOC8_gFo7SVDWfn8Nc3GxXAO08uJE5oC-4z_kYERLvj7whUWlYDhz-Flz7MCXA4Hq7szOo6OtxDZkUikq6ZWwJaVtLy6WqNfJYiyTwlUROiWbEpXQF6mH4z_Kc2B8ndGjpw0DFV3T2ipxasElcLdUPWc1-BiEyfChioqpkIZ55KfUicxSDK2cr6XA0whQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpkdsex9WvAR3TY_7_N4cQqNIfxV4-KII3UIzXczsqTN2tDouFXyKkDSsxL_YhCKnfoheKUscBtfZN49QoSlR3HDcRxxlIQYr7G0AcRTVrcH1RnXAcEZKCFzNcB37P3QS3m_7htkqaz97YNxDVuzrvY67i57ooKBAmXnAYD4ulXYQ2Nysa15-547w9fzsg92lIqhuJwem0ZAQ7VI8K4uHPz-uWJ0V2-rvT3VZHk_8zQ2Ou02kVGnLy_5axUgOnYHHO-JfGuqku8iL3CbnY60CMuymYUDoqwm8CbUwfo8nAsveHNJ5Edo5um7GWTjTUsy8yvmNe4xblv8mNvIL2Qftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0JGOGY6Ej4t91IxGmC0Pqs8apjlKI9oLynVE-lTEMXjjteNqdoWuj_mt_37XK6CU8pneatmILRIWYnYrx36Td_w9jpb8WGmldpbwZEN-2QTdxFIqPIPQi7IsLq-NOb407ELFGgDAk1GBAGNii2RO9QAawsUjSp7QT5LWZ_WoTqB0hSGB4NYBv752oyzWIChhVai82ugN_LZ8q2ZCXT7NKsIisYDqkuD5wtSBjCwJ8G1zEvbPo8WDpw7y9R5pxdA2cy97H1caGR22ek0oPkJcaAomKSpF1IFra2lsSQeM3lveQhva_O7pbHBKFCiJZmItvG5nEUpS9tF0HG0IZKu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgG8rFmRCYEFUh0nsId9WAPKCYwW4Ms2g_9_NEs4CtUkOq307H7c-LX9ofEEEdSLs9HWWTKtSo6A2R8oiHrfzNfUJksFy1ZpPeNBRmpo9e6PbXWWrpGdU7vfT0NQHUoWvSVfDR9EEKFqNTck2ICsZmbGHyWMemcd-ZxzGDg7aBjRECTE_elLjqkyLF5EcYizGaMdOh84XFpKq3pug7pn3wkNvBzh5UgxguLMb5dKf8-onokn7veLFkmm3M3DFtIQpYz_s48jH9wKluDLTseO5FWg1buXN14k1yE6YjFd6hEuro_uYGbt6uyAx-7YR__J8OPYdQki-iSD2PMGPrDWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkN6m9Kb1fDjbwcLP66UApUf4rzIbRYMb52JhapQAn_svZ06Ee6-xlym8Yb_eCvbdKZuHySB4zG2K6L1uq8nECM1ibprofV7ioR8vW97SY6Z0S9WhPs1BupqMFEhH6bkp9mV1qHMTtuo2SCdjnMjDYAeImXaIL5ne9xDiNrmIF6x5Oy8rzxkBDekj2OdCslJ0XAvJgv9Fe27Drzzk1wYVmTm3LMCA4_3pBeKQ5W3OB5hwU7AXoGzwIo7R3nFO6u1j7sErHKlVY-DjqLbg4L2WEZU-rNoTbvLzxKkj5dshcdX6-j7WoYUauCEcB_4-xWFi3FF1b6rHbtmBUzA1EkXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD7qWdbehN0zujW_T5BzqZ7bjDFwD7y8GXg7NgV4V327ZERFQUavmIVgg8ell5M-8WDWJ-rJqI7Oo15IWKIGPfNfpDkLpD8oeo0eOKHn0iT9YwfdADYs1I4B7WE0KsQJL9PtkSpPSsKVmFKqn18HfD3xp55PBaISr6vAb9YiUPk2jg_W8TqYQjnHGOle2mmkM5Y1qZHyYLha5MF9V3l8ou_ORwi-8o1uKyA5H49CsYGhwjEJjcV20oReGTgz6GLnDVm5pW_6F3JeX355Qw62r3nSKX-tAGkBT4d2hZ9_-uNv756BPtgPmikwzA-cC_KjB4zQvPTdZllH8BgU6efz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7wPcMkNbnoFghzLfFnBI04cF8goWyTA4Cu1Css2l8p-EJQ9g64rD71tEVvI_--w36g3fwEjZE6MX_d3rG_2p5nz6mxTvwb4S8ZXPdJJbdkKQs9WKM-rG7gfmoraum3w7tvJJ78yJWQzlIQydymy7BYPheW6qJXutvJK4w7R6_vufpBaSK_ATCs1SdM6c_Du3irLoB_zVj_fDLA7JxCrQhjSmxHO9UsWKznxn9nWTcH4HpSt0aAj5H9rLcqs_NRsXNb1JTkVkCoFs-WzSOiN1C3ZUaukqwN6jqZGsHlyd-qEYMBqCut-fAD0JLaP4Yv5yEP-rFZnMRviNw-XL1SGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMucETpxHw7vV7LVPLYVXt_3Oq1UQDTJtwvFNqaS9EdeU8axHzMy-pwSlE8zCMBoeud6lxTayLjSWLyzawaU9gnBHjs_iLouSueX07Z5WS6hFXUjRJUGt8H_yaLv__Akw5CeO9wGN4Iff0E_PTpIOkT5Cg3z6XCoIAePS8xaLLR2ZUJjb3YcDnIG3EqOmTbrxpznBFmQmRtkZq9MAuwr8rPRwg_vhajmSi-Zm7RvZXquuNeM5cJTeS3v6ixyifYxbaNvKHs8rWIxAVQVW-_-zVtdF0j7BzE8Ee-JCZCX5r3cbm6t7iZ29DJQNkpXxUHcE7GqTo33UFh8oBldhtxzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2lqEe4VJd_3j0Fc9fry1NHPVu6S9H-r2Lx5ir791zCfaj83Ltroad4LK9pQt6ovQ66whAO7NCKOYZOg2pckfLrZdbfeIvu9lFlV8-pRTQiEOJO8o8Haic_Dp_tR8sLpW52cpgMQbWmBAIyxsJ0pv5js4JOynUzgBFRtE586RXJrz5_neJgcR_eFOO7I-QYrMizfb-lFejh5xJc9ZodMcGY58IaStpKLnguncYhHQHZ6Gfpib8dlUoabiu1oiPc39wbERAgNDmg55YSoFGdc72xIyuZV3ZTHXs5wsPECwGrtVE5seO5PM51RT6NOZf4Y4rGGp_JEWHgWEoVgs94xig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPe2E-wu_gPHJuu9HyIlhFOmPJhdO9MULfscXAbshwImUUHlXwucC5QVL-I9zxKkOUKtpX-WFcWH94c1E4QyonD0T9EyWfYUK7rQZtjl_OWpFpkcPVRpTCXEy3ke6_icbaL9qlCJXH4fwSUCOgpWdK5DoZVpaCyJ9IDDYK4VoOFswuKlK2lYxe29cDFXkWFijT3rcOZBsaBJ0GfQQldC0K6RH7I-daGyREXecjosRhvp1TEGVfNz899w_xZd04M3Y1j5Z84wQCMxOqL5oevURVTbNFQ1NvSBSnpt7GqZTgZLy6uosto1libL-T2BbXEGYZYFDjSu0aPJqEc-CCMvgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFa3mA_TAQ9vAqX_4woL7a0sZejtm5rl-CTOP7-JCWR0JPQvnpvTSecVNV9hZhDjHiFLZvEmNSUIKhwF6AwWwTAn-IjpFKQ3Ss0PgLhrb76vOrSsQSLwP3k7FGvZqqbucuE2KHEkC5SmLGt5VAa4r1W9we6_LMd6YULeSP6xErr3FQHTvqDzkaTPOwfoyPgJvE2G_DSYl5vQ0vcQOqDl8_oh43yfb2mgp7tyDiN7wcVeJFEu6lKD8uwbFvoK6mcFifUFRrDResdAHY4XQ-zYi9P9QSmp2eV6hI2FsAMePm_8SMWjdwmE00m1nioWhl-riWGlzF8BPedzRKcnuvnKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=h1SBHdyZwo0v3wqjmg1Kz72zWH0wrw5qU4b8x5yBHyqjH0OxNlk8mnLAKJzP2isribThpyt8LyW3TNM2rnNMD1GmfJxBdVEJkEgVZEt5x7S3yTi5DgFEikQ7xOTTmAEqMsaMj6ngYSACP7Juj0Cu5EjzuFOcby0_QimyHjH-i0huEEVP_eXnxVWU6VMR9UUQxkB8bWddrzGQSNv3fNMB-vqA5MW_44qIkRo8CqfO-jVvx8Y6rwwqsag4K_8i_1ECGxesPbSm9M8zJA853mTN4iofafPXIn8LcbVql0R0AYSiXSKAr_brk_Otscp2YwgR4XcpaFgGcxWxj43nS8o4dIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=h1SBHdyZwo0v3wqjmg1Kz72zWH0wrw5qU4b8x5yBHyqjH0OxNlk8mnLAKJzP2isribThpyt8LyW3TNM2rnNMD1GmfJxBdVEJkEgVZEt5x7S3yTi5DgFEikQ7xOTTmAEqMsaMj6ngYSACP7Juj0Cu5EjzuFOcby0_QimyHjH-i0huEEVP_eXnxVWU6VMR9UUQxkB8bWddrzGQSNv3fNMB-vqA5MW_44qIkRo8CqfO-jVvx8Y6rwwqsag4K_8i_1ECGxesPbSm9M8zJA853mTN4iofafPXIn8LcbVql0R0AYSiXSKAr_brk_Otscp2YwgR4XcpaFgGcxWxj43nS8o4dIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXllfdt38nJE0JFc2ZA1QsJDnppcHo0Q5LURCkcqgpkBxEDk-GpW5bMXIX3YFlCmGlf6QtcxT-cP-jJIKlO8FgStlJubNE-F5pPJkX9bJ3Wz80JvkTtPHW5S2Iw6lJRm-sVYeEGbEh2_T7ANiOTDKbwpWo93SnGSCm8LTmb9nfIjXpgRumVFul3aif3lkOllf073Fy5BcGZaDZRSYXtw_VDJPGBIPpTjqBjc4uPpjF0DeBjzUWcDRkGuOhgYOp59smwQ5LllU8Fuf2ONgadWettaeZiU9K8iyJSk1tXk81x-3mIfUwgZ8dSFvjmbEtQRRS9Yf7R_C8ufbbVOuLI0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=bQZfRlKtoNSf9oRgkxcCoQxXdDsQ0zwzd6PXGfUTrha16cQojRRsuDAsGwNoP0tl_qOhpDaaDER3VykMREyMvutJwPj6jZDiTEKbGcY6jJ0Y5325bcnUCmQ5ND5YRW3cWqN8_ykMAUQ02izEV96ibxdXwf1F_stWA5LDX9-rbR5Gv4k9-Nn3-7PiwQgicFRWjPUOifRgecvMVjS5QwLrOZf0F_y7MTnRaYuYx9Qe5mSyTX7dlXR82AKlyHIj_RzOY5Tecah4cLZziG3dU_RI5N_sANnhT7c1AYxr1eum1s9DfsCRbbxaVnB81S7rKAKng27Kem3WupqeF0pM_AZupQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=bQZfRlKtoNSf9oRgkxcCoQxXdDsQ0zwzd6PXGfUTrha16cQojRRsuDAsGwNoP0tl_qOhpDaaDER3VykMREyMvutJwPj6jZDiTEKbGcY6jJ0Y5325bcnUCmQ5ND5YRW3cWqN8_ykMAUQ02izEV96ibxdXwf1F_stWA5LDX9-rbR5Gv4k9-Nn3-7PiwQgicFRWjPUOifRgecvMVjS5QwLrOZf0F_y7MTnRaYuYx9Qe5mSyTX7dlXR82AKlyHIj_RzOY5Tecah4cLZziG3dU_RI5N_sANnhT7c1AYxr1eum1s9DfsCRbbxaVnB81S7rKAKng27Kem3WupqeF0pM_AZupQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=LhapXRBSO2qj9GZLI5XQ74fD3VNQOTXwUeKfzCw5ZpTnfznlM7_xykDniINE_GIGgcnvUAdjCjTvgiJqLrB4uVYfEsehG6A6-rGEsMmTwCqKz7SFeKnxjpWZDmf_3mNqnqGcUcinG9YftscMrUeeKP7vUtd4vYrruyiJ_lk5rMZYTF0iBQ6fLcpyWhSZKESO5O5pBM0iz4IsziuKHPC-7SUpCwOzAeI9IdY0m577wK1LFaEc5DB8yhM997e0Stp6vqIo3Fo6D4XvTWQWUxHDQvWvo8mB-CiOHLiR_f3y6a9o5r1uWXnjQU0oV4dMJpqop0VF0fmm1WdZwSO-K-FTHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=LhapXRBSO2qj9GZLI5XQ74fD3VNQOTXwUeKfzCw5ZpTnfznlM7_xykDniINE_GIGgcnvUAdjCjTvgiJqLrB4uVYfEsehG6A6-rGEsMmTwCqKz7SFeKnxjpWZDmf_3mNqnqGcUcinG9YftscMrUeeKP7vUtd4vYrruyiJ_lk5rMZYTF0iBQ6fLcpyWhSZKESO5O5pBM0iz4IsziuKHPC-7SUpCwOzAeI9IdY0m577wK1LFaEc5DB8yhM997e0Stp6vqIo3Fo6D4XvTWQWUxHDQvWvo8mB-CiOHLiR_f3y6a9o5r1uWXnjQU0oV4dMJpqop0VF0fmm1WdZwSO-K-FTHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=t1h2CLrDNtmkCQJMg2izX_a0dG4yqU8fnQS43xjzcagdavQrkWZ7C6bGP59Z74cZIxwunl2Ir0IA5ulQGlcgXtkCf-KrbMC9V5oiRNGN9rguuTx23Zet91R9-SUq5GeGidu0KUs5f_Dt67eENGS9W24YSVbWjgt0Rtg06j-yNgM8cRYSyQR1-uWDAJbHYGy1_bcTFNqivPlLkA3sRBYI-vWiBiPICdci15-AhNWKmFYtGhfuXKx1dQygs3sCm8vZ1L14YhtRDjPvtwSUWP7IJ4BpOOUixlQ_6Pe5UP_tWK55iuA0HzyyRiJ8Pkn0tEA-cWN_CdxWamWK2WkY-syoyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=t1h2CLrDNtmkCQJMg2izX_a0dG4yqU8fnQS43xjzcagdavQrkWZ7C6bGP59Z74cZIxwunl2Ir0IA5ulQGlcgXtkCf-KrbMC9V5oiRNGN9rguuTx23Zet91R9-SUq5GeGidu0KUs5f_Dt67eENGS9W24YSVbWjgt0Rtg06j-yNgM8cRYSyQR1-uWDAJbHYGy1_bcTFNqivPlLkA3sRBYI-vWiBiPICdci15-AhNWKmFYtGhfuXKx1dQygs3sCm8vZ1L14YhtRDjPvtwSUWP7IJ4BpOOUixlQ_6Pe5UP_tWK55iuA0HzyyRiJ8Pkn0tEA-cWN_CdxWamWK2WkY-syoyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKHdyXC6DyDoTJBywBuRCU6rT0-rnovhPHYNzJUVKfZBE5gVdD8g_3BhidJ_ieRzZMo5SxJVrrW0xzH6IU6x5NlXGAnoRQy8NBELX-_zC0GBzWyWrFhDoARZ5UQ5rNeu4bNE_FdNSzLxhU3VYBln2iobQttJNqRxf-ODdOxVVBIJtnxZ0i596biad9KilwKH4fI8IO9HWZTw5OByGIqmsgsAdwHaZ5cT-69jE_L5rRVtKTDbEn64rCMaqXTbcXaWty9b6TbWv2uliGQtby5tGvHdc0XkyYjehz83CVMddVWfgs0WwDI4CuN0rpOtqJLlfjHgb_i93SIJ-vV1Y0H3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfKZ52YLIeHbEv7rGtkV1dwLhKpVzT7K3kT0f3AH-rwcnw8cX_AmpZPXPgspSUAXI25jjZOywaMIHr6lUC98Uo3Kuu5n-hfCQT-XDc5q1e_tiLQKhaYQPQ9qQt3HF_H3JI867pihV-7ZCcH-2g5ev9L5LLV4qywXpdBB1DDJBkLDuXFpaM6JQvN_-gvZ6_s06ix3_l-IT6CPm1WTVh5walKucX55jsWakA7iGWO24vyz267t6iwSiyqwfozvc-HMWzNCU0SbKQ1s1O4zkjkpbtPhpxV4S0ft_5ZYjDE1RAetUyJO3mqsJNM6u6aszIZ0IGXjFPNyXDblkNLNf7Xr2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
