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
<img src="https://cdn4.telesco.pe/file/Ha5Mw-tKkwlhBAvnOVMDWHiSy7Z9-H2J0RmrqHiLMSoYS9urnK-lt7zz6EKOgzqEcSQZpc-J-6zHG1dFM7T2mVzEWCMynmVVWaT-dRPsSiR-1O2P9_ZHGuyixwlrpmjRetPXJ_Fzif1B5MXGoXlS0RNN6kgI8E6X99st8_9xbkzA0VO9ti79Ab5bOJ_QZpLix-B6KZB5YVVKt9jaO-0aWg4MkeMDH6Q9Cjyf4qnrELgkpmQVb2nKsYb_3E7lnECXSchb7LV1L6ln2CFkB8pTyE2zU_cm6FkJJTLkUFlayi8TWzo8C__976J0tFx3uYS-DRmYniwKIISNrk7Cso76lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 19:42:19</div>
<hr>

<div class="tg-post" id="msg-17830">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!  در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان…</div>
<div class="tg-footer">👁️ 467 · <a href="https://t.me/SBoxxx/17830" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17829">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3qLuFjhZuD_1tu-V7XP5z6UhQywbYce4bnbm941sscBExD4Sn3BGGLX37e-tFYKDtqrHFQuQnkXO-bIQ8xfN_oAndVjQPnmC13Ol4w_kfzVO9rxVwLLDOAqu4pWTl9ZwpF6t52smMblD6L9y8EKhkP5xzXg--XMCp_LjYh584soPivTWuUNq7yOZeQHjNT9vV4gMWhOlcOYZqNJZ3DHbG7dfjwfBurx5nA7IViIwx98ut66a41btwzdylLaWczIek99d1do9xD86x5b8Os9_8FX08LrbU4gqlLEi8G5GfpuqI2QVsKxE6vVTGhmgS8tDOIMTqk_vLtafMcOTqtmWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!
در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان می‌دهند. در هند به دلیل فرهنگ پسرپرستی، کمبود زنان وجود دارد و زنان اغلب در صورت اطلاع از دختر بودن جنین، سقط جنین می‌کنند.
در مرحله اول، برنامه‌ریزی شده است که ۳۰۰٬۰۰۰ مهاجر وارد شود.</div>
<div class="tg-footer">👁️ 489 · <a href="https://t.me/SBoxxx/17829" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17828">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه های اسرائیل:   عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SBoxxx/17828" target="_blank">📅 19:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17827">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkJLUb9Mcof_-pLYWUCe6Sl8FeLm4klXwFITZ88gjxUtajgu_N6H-_Xi73RS9QOot6fghGiPEftTMH0pbJKJ3YOjhpGdqZigyy1hxsKE557_oEXzx4Zeg5mOtkTV9uRexo9oX1Tjq7aq05L2h-29NhE00hPyWQujJ1YG-Gkw5FKTJrwVHkEKTqevk9K5DDCXL6-oxlkvMIQx7xY9ahhvR-hAHGJLJICdX8o45xvDzRfvfKdisl2Q21g97KYf59G-eflfpX551Pi5BXoGxb5oTrkZ7lrsnPlRI8bv4X5KN7_xJERRbxerK8hVlSAv4So1cJfX7rjqjyqPSgbUfBiVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عثمانی ها جوری مهمتچیکلر فوتبالی شان را بدرقه کردند که انگار دیگر نیمه نهایی در جیب شان است!  اکنون با 2 باخت 0 امتیاز دارند و بازی بعدیشان هم با آمریکای جنایتکار بی رحم است!  ُسبحان الله!</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SBoxxx/17827" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17826">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه های اسرائیل:
عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SBoxxx/17826" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17825">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/17825" target="_blank">📅 17:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17824">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/17824" target="_blank">📅 17:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17823">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه هرمز مجددا بسته خواهد شد.
قرارگاه مرکزی خاتم‌الانبیا اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/17823" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17822">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یارانۀ 2 دلاری خرداد به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/17822" target="_blank">📅 16:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17821">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4wMVdBRbmdz4CM_7-wPo0yjL7e1F3PxN9QHRFS_caYBtGHBx32eNmwucz_Rm_OT_7iX34IMvMawRnz32lMjJsRMPzcx5URz-KtVW6UX6hFyewI2E46d3TTsZYj3Yjj2hO7vCAuFPs2dcj5_fvYzXB0AkYPaqSL6INWvt6Nb2POOhnxEAcUHo9MaFG8T2QyR60lUPY5AhP-HboWEEam-C5otWzOG_9tBZ0mKVQmPe-Mp6teUwJGR9ysIda9ikBq5LBJyhRl_FpmxFBeKef8NMQ1fQ5JWrt1T7Fwoa_PM7P__lxMEsyoCXCIcFz_frilWN9AIMck5esHDgXBfKZBRYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لابد چون نظامیان می دانند درگیر شدن با ارتش اول دنیا و یک قدرت هسته ای با فنآوری بالا با توییت ریدن زیر کولر متفاوت است؟!
یک بار از بچه های پدافند و لانچر و ... بپرسید شرایط چطور بود؟!</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/17821" target="_blank">📅 16:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17820">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/17820" target="_blank">📅 16:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17819">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/17819" target="_blank">📅 16:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17818">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بخدا سوگند که ما هم خواستار ابطال این تفاهم نامه هستیم!</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/17818" target="_blank">📅 15:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17817">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlMoemk11qM8oAZEgRCnhNOkEOgj6S6J_kr1FYD9so0evtWLj75Xv3sy93s6f3V_lygm4XjnQMEH5VRDWg0C2KBnFLkFDqucyN8RHZL3hLE6en168cMXjykEujtKP6Lam6tSHDUgpE9c1sZxQ5tWbdpbf_Th0KNcF949oRhI1Fk__NNBmbN5EtKfUDAq4ilXF17Jzr3pxuw4jgA9E1h0CzpysVSJb2VD8I2TCLLJyu29nuUlgDJ3cmniNkws5cccdA3rO3MdPeoKXdaEX5ezsHBwP3Nbb7kOlwF2p_gz6KkQmoquwG_OXjUFM_xlgckVWX8FJgRhMoC0oDYNyNDTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/17817" target="_blank">📅 15:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17816">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/17816" target="_blank">📅 15:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17815">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/17815" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17814">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGKS4bafG2qrxBISQY9_ot0g_OlQ7-2elEAiZJZS36KFty7d1-eLck-yGDYVa3CndP4NRsYvJQ2D47lcviTN9CiUTGMqn03sk86yY-Ew2stWcW1USY0y9QxOyCyJHqcjube9WSYTZgB6267ms8S-DwsKWFyhPQNbw8sSzkVSDSBzgJyTdkdsqI5SjyIqIj6nIr2z44b0e0SHx6D_7m6iEglt11pRuArrO_0I_sVPbpWtNx6pR8zsRNI7-Ol594zshX4H8-MOsIDkldNhn4QWYRO5q2WB8P2COXUsBUhvK3t4j1B6VeElfajGKEWIRMjjCUVmgSvDcK8ybjq2vOQZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت ترجمه شده: جنگ آینده، جنگ سیستم‌عامل‌ها
دانیلو تسوک، رئیس مرکز هوش مصنوعی وزارت دفاع اوکراین، پیش‌بینی می‌کند که جنگ در سال‌های آینده با یک پارادایم جدید مواجه خواهد شد: جنگ سیستم‌عامل‌ها. او معتقد است که هوش مصنوعی در حال تغییر بنیادی شیوه جنگ است و در سه تا پنج سال آینده، اگر درگیری با روسیه ادامه یابد، جنگ به رقابت بین سیستم‌های هوشمند تبدیل خواهد شد.
اوکراین، که پیش از تهاجم روسیه در سال ۲۰۲۲ سرمایه‌گذاری چندانی در پهپادها نداشت، اکنون به پیشتاز جنگ پهپادی تبدیل شده است. این کشور از هوش مصنوعی برای برنامه‌ریزی عملیات رزمی، تحلیل حملات موشکی روسیه و هدایت پهپادها استفاده می‌کند. تسوک می‌گوید: سیستمی که داده‌های بیشتری دارد و بهتر آنها را درک می‌کند، راه‌حل‌های بهتری پیشنهاد می‌دهد و برتری خواهد داشت.
مرکز هوش مصنوعی اوکراین، که در مارس ۲۰۲۶ تأسیس شد، در حال توسعه یک سیستم عامل واحد است که تمام داده‌های میدان جنگ را تحلیل کرده و تصمیمات را از سطح یگان‌های جلویی تا فرماندهی استراتژیک تسریع می‌بخشد. هدف، ادغام سلاح‌ها و سیستم‌های داده‌ای در یک ارگانیسم زنده واحد است که به صورت هماهنگ عمل کند.
جنگ اوکراین به یک مسابقه تسلیحاتی فناوری تبدیل شده است. شرکت‌های خارجی مانند Palantir سیستم‌های خود را در اختیار اوکراین قرار داده‌اند و پروژه Brave1 Dataroom  برای اشتراک‌گذاری داده‌های میدان جنگ با متحدان ایجاد شده است. روسیه نیز در حال توسعه قابلیت‌های هوش مصنوعی خود است و از آن برای برنامه‌ریزی حملات پهپادی و موشکی استفاده می‌کند.
تسوک می‌گوید: سوال این است که چقدر سریع می‌توانیم راه‌حل‌های خود را بسازیم و چقدر عملی آنها را پیاده‌سازی کنیم تا تأثیر اصلی را در میدان جنگ بگذاریم.  اوکراین در حال حاضر بر اصل حضور انسان در حلقه تصمیم‌گیری تأکید دارد، اما تسوک هشدار می‌دهد که ممکن است روزی برسد که سیستم‌های خودمختار آنقدر سریع عمل کنند که حضور انسان، تصمیم‌گیری را کند کند. در آن صورت، سوال این خواهد بود: چگونه می‌توانیم با تصمیماتی که سیستم‌های خودمختار پیشنهاد می‌دهند، همگام شویم؟</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/17814" target="_blank">📅 15:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17813">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ1_S1L8i0qh8a3gF52KlkWvusrMq9LI0Yk34SNocwv72ZgH32KyLXMBRP4rmW-4BUQsENJzxI6PSh2e3yhVNs1hbLJI3Lx6hRNlOHidLCyhHreSyEaCbV_tIZBJn8RydvAjkT3gwc7taoACsMQn-awCdxZoO5xol4zhPfwb-e5-cdYClAyGR5iecJcbsSjDBrifhZ381fh4pt6-y6COKl63UOtO76CEoNvYcqipAN9vVOOu41cyPxBvnTnFe6w3up5V7lq2x8449qJbk6A26tfPm21o0wU-Jx5Q9PVJDFIBJRNnYxUK9akdTrYFndK2JkgfdmMau86PKx451KH4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عثمانی ها جوری مهمتچیکلر فوتبالی شان را بدرقه کردند که انگار دیگر نیمه نهایی در جیب شان است!
اکنون با 2 باخت 0 امتیاز دارند و بازی بعدیشان هم با آمریکای جنایتکار بی رحم است!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/17813" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17812">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزیرخارجه فاکستان هنگام استقبال از مهمانان نشست اسلام آباد زمین خورد!</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/17812" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17811">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e024f4add.mp4?token=Iy7_qngPvbB_NVJ98S03P8JbzwVkZ8oy3ooQqdd4VtSFt15jTT9W-dc47Z3R1qKqIZK9huoKGpfUVWIL7T4RpDMZN8zz84T1bu-qtoqORc7alcR1oMX3mXrnBut_8LBnAnch7ba3ht2EYK8iGmSmPJj92v8dttoqMTG8K1xqajXUsl9ufYLNUO1H-K5T9sbtthNRz7HfXEkDji5AnXzRj1xNJL5efKjCxkAd8uXuYSu4r_gzysY4_dlNgpKr4a1sKbWclBmzkozLQcvz_DjWJ2glH0EmEn1NWZe6CJohNlV2jQdjHACRyqXUvNM3AQee_dErZK32X0nZ8r4LodxJqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e024f4add.mp4?token=Iy7_qngPvbB_NVJ98S03P8JbzwVkZ8oy3ooQqdd4VtSFt15jTT9W-dc47Z3R1qKqIZK9huoKGpfUVWIL7T4RpDMZN8zz84T1bu-qtoqORc7alcR1oMX3mXrnBut_8LBnAnch7ba3ht2EYK8iGmSmPJj92v8dttoqMTG8K1xqajXUsl9ufYLNUO1H-K5T9sbtthNRz7HfXEkDji5AnXzRj1xNJL5efKjCxkAd8uXuYSu4r_gzysY4_dlNgpKr4a1sKbWclBmzkozLQcvz_DjWJ2glH0EmEn1NWZe6CJohNlV2jQdjHACRyqXUvNM3AQee_dErZK32X0nZ8r4LodxJqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیرخارجه فاکستان هنگام استقبال از مهمانان نشست اسلام آباد زمین خورد!</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/17811" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17810">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">➡️
استارلینک با مجوز دولت عراق ، بطور رسمی در این کشور فعالیت خودرا آغاز کرد</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17810" target="_blank">📅 11:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17809">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📡
طالبان با دستور مستقيم ملا هبت الله آخندزاده رهبر این گروه در افغانستان ،  استفاده از گوشی های هوشمند را برای تمامی کارکنان نظامی و غیر نظامی خود ، ممنوع کرد</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17809" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17808">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYRyyPIoj6ROgb6RtI-cYvmIlw7OEJfqsJrpVenzdbvrb_nIwcjV-y2evYIhwuh78JjMKpPJyq-_-Qii3sjS_LGBXywJ2EXWTh4WKIeuCZPtLAgUm2TPeNAwMbFlYi9hrJ2dkQa-BlpV-GgvfUKlgbtx3X_b9QrUlmtTPtaQ4tLhqreMRvppVXnuMDfSNNqitYRJe8MOKbJOZ0z-bBGhBuO0VwH1YXi_yybe8DlvBwpKZ8Z6fCLSm8f7nRRXZNL4rjn7qoU0cbtg4GRJoIOYkDisG12BMzPRXpE7-3SkVGR10iG0eYmyHfvBG9clth6ylI6c6HDgF21IST-G9X4A8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ این مردک مجاهد خلق را رهبر اپوزیسیون ایران معرفی کرده!
این همان گهی است که 24 سال پیش برنامه هسته ای ایران را لو داد</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17808" target="_blank">📅 10:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17807">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ: اتحادیه اروپا برنامه‌ریزی برای شراکت استراتژیک در زمینه مواد خام با ایالات متحده علیه چین کرده است  اتحادیه اروپا در نظر دارد با ایالات متحده بر سر نقشه راهی برای شراکت استراتژیک و توافقی درباره مواد معدنی حیاتی به توافق برسد. هدف کاهش قابل توجه نفوذ…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17807" target="_blank">📅 09:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17806">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up5pcD8_MhFpBdcsRklkSMELnGznCtaD_w99EjhPJD8i4GRTQ60NtZEndGcRg8VetkE31w588IA3sj7Wt1DzKeuAV_x12VUvCjpaU53J5qPwiVckyUv5vW7l5zW38XqBv05n__GiT7NZzcYYLQ56gHObeirY2jtEKqAwye_ssS2b4HaF5LhpYYzO2UABIJ-EMZF9ZgPY15xcWXMcFSxjZs37DN_LLZs2r9wFOakCBIrySh4DQM2vEFQwtDtfGvRnXe9iUVZVahvLtAS4U6qhaIElFsbNxw2RuG7UtkyOacoFAc_UUfi93K0eGNvLyl_wbbFn7CiZegbjEaaibasLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای شهر نبطیه اعلام کرد با توجه به خطر احتمال بالای اشغال شهر و شدت درگیری مراسم تاسوعا و عاشورا لغو از شهروندان می‌خواهیم از شهر خارج شوند.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17806" target="_blank">📅 01:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17805">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcjVOC1hBYJEMxD0o1rwzGMVbaAW8BjAGws5iqzixLDsVb-zvh5SQyZhkl_oYfbf5UTWX-3es5pAfIQuy-fhRj2Mm92fRTUAFQNOuv0UJzAIGyFSQpF4YQVLPsENhof6Tj3IvtDmPCLor8Zan1RrL_K7XNNadUOTozJeLqRS08fBtAzhDERtve34Ht_TCSM_0JZVm_Gy28OD7WVh7nGUAMPOWQzbHFXYflRNBrYthhQIh_8psObDqWzNQabXLoNVI-QEgSxZTFtt6-g87H0AQe8jOnER4-G-DbsJzfbPJXmCxJU3wkjxaZBqbNmECMyOzO1WFhmERB5GLajboRjE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی قبل ترامپ در توییتی اعلام کرد که ایرانی ها مسئول سقوط بالگرد آپاچی آمریکایی در تنگه هرمز بوده اند.  او اعلام کرد که ایالات متحده باید به این حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17805" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17804">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محسن رضایی:
به خطای دشمن شدیدتر از آنچه بوده پاسخ می دهیم.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17804" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17803">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جی‌دی ونس درباره پیشنهاد آمریکا به ایران:  «گزینه اول این است که همچنان مانند یک حکومت تروریستی رفتار کنید؛ در این صورت، به‌معنای واقعی کلمه هیچ چیزی به دست نخواهید آورد.  گزینه دوم این است که مانند یک حکومت عادی رفتار کنید؛ در آن صورت، ایالات متحده واقعاً…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17803" target="_blank">📅 22:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17802">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">چقدر این ونس ترنس گه می خورد آخر هفته ای....خفه شو دیگر</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17802" target="_blank">📅 22:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17801">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ:
"ایرانی‌ها، مردم بسیار باهوشی هستند. آن‌ها نوعی نابغه‌ی بدوی هستند، اما باهوش‌اند.
آن‌ها اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت."</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17801" target="_blank">📅 22:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17800">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چقدر این ونس ترنس گه می خورد آخر هفته ای....خفه شو دیگر</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17800" target="_blank">📅 21:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17799">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خود عربها هم گفته بودند
که قرار نیست سرمایه گذاری بکنند</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17799" target="_blank">📅 21:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17798">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">متن توافقنامه به روایت فارین پالیسی:     تفاهم اسلام‌آباد بین ایالات متحده آمریکا و جمهوری اسلامی ایران   ایالات متحده آمریکا و جمهوری اسلامی ایران و متحدان‌شان در جنگ فعلی، با امضای این تفاهم‌نامه، خاتمهٔ فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17798" target="_blank">📅 21:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17797">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این هم‌ در همین راستا است:  — مقامات اسرائیلی از انتقاد تند معاون رئیس‌جمهور ایالات متحده، جی‌دی وانس، از وزرای کابینه اسرائیل و هشدار ظاهری او مبنی بر اینکه حمایت نظامی ایالات متحده از اسرائیل بی‌قید و شرط نیست، شوکه شدند.  رهبران اسرائیلی عمدتاً از پاسخگویی…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17797" target="_blank">📅 21:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پس بند 1 توافقنامه که رفت روی هوا.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17796" target="_blank">📅 20:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حزب الله عملاً دارد سیگنال ادامه حملات به شهرک های شمال اسرائیل را می دهد؛ یعنی اقدامی که پس از آغاز جنگ آغاز کرد.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17795" target="_blank">📅 20:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌  بیانیه کامل  اتاق عملیات حزب‌الله
🔹
رد ادعاهای دشمن اسرائیلی درباره نقض آتش‌بس توسط حزب‌الله، مقاومت اسلامی تأکید می‌کند که دشمن هرگز از ۲۷-۱۱-۲۰۲۴ تا ۱۶-۰۴-۲۰۲۶ و همچنین نتایج تفاهم اخیر ایران و آمریکا که در بند اول آن پایان جنگ در همه جبهه‌ها از جمله…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17794" target="_blank">📅 20:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17793">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
بیانیه کامل  اتاق عملیات حزب‌الله
🔹
رد ادعاهای دشمن اسرائیلی درباره نقض آتش‌بس توسط حزب‌الله، مقاومت اسلامی تأکید می‌کند که دشمن هرگز از ۲۷-۱۱-۲۰۲۴ تا ۱۶-۰۴-۲۰۲۶ و همچنین نتایج تفاهم اخیر ایران و آمریکا که در بند اول آن پایان جنگ در همه جبهه‌ها از جمله لبنان تأکید شده است، به هیچ توافق آتش‌بس پایبند نبوده است.
🔹
بلکه دشمن اسرائیلی در نقض‌های مکرر آتش‌بس افراط کرده و کشتارها و تخریب ساختمان‌های مسکونی و زیرساخت‌های غیرنظامی را مرتکب شده است، و به حملات زمینی خود از طریق تلاش برای نفوذ و کنترل روستاها و مناطقی که پیش از توافق نتوانسته بود به آنها دست یابد، ادامه داده است. تحقیر اسرائیل نسبت به آتش‌بس به حدی رسیده است که رئیس ستاد ارتش دشمن، جنایتکار آیال زامیر، دو هفته پیش اعلام کرد «در لبنان آتش‌بسی وجود ندارد»، و سخنگوی ارتش او دیروز مجدداً بر ادامه فعالیت نیروهای اشغالگر در جنوب لبنان تأکید کرد.
🔹
و طبق عادت خود، دشمن برای جبران ناتوانی در مقابله با مجاهدان مقاومت و پوشاندن شکست‌ها و خساراتش در میدان نبرد، به ارتکاب کشتار علیه غیرنظامیان و هدف قرار دادن روستاهای امن روی می‌آورد، همانطور که امروز پس از مقابله مجاهد دلیر با تلاش پیشروی به سمت تپه علی الطاهر در شب گذشته رخ داد.
🔹
مقاومت اسلامی همیشه آماده مقابله با هر تجاوزی است، مجاهدان آن با شجاعت و روحیه حسینی کربلایی از خاک و مردم خود دفاع می‌کنند و با تیرهای خود ارتش دشمن را به سختی می‌زنند، ده‌ها افسر و سرباز آن را کشته و زخمی می‌کنند و در تجهیزات آن آسیب‌های ویرانگری وارد می‌آورند، و میان ما و آنها روزها و شب‌ها و میدان نبرد ادامه دارد.
-جمعه ۱۹-۰۶-۲۰۲۶‌
-۰۴ محرم ۱۴۴۸ هـ</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17793" target="_blank">📅 20:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17792">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شیخ نعیم قاسم: ما نقشه‌ای بلندمدت طراحی کرده‌ایم و به راه خود ادامه می‌دهیم.  ما تصمیمی حسینی و کربلایی گرفتیم؛ تصمیمی بدون حد و این تصمیم همچنان پابرجاست و هیچ بازگشتی به وضعیت پیش از ۲ مارس وجود ندارد.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17792" target="_blank">📅 20:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17791">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شیخ نعیم قاسم: ما نقشه‌ای بلندمدت طراحی کرده‌ایم و به راه خود ادامه می‌دهیم.
ما تصمیمی حسینی و کربلایی گرفتیم؛ تصمیمی بدون حد و این تصمیم همچنان پابرجاست و هیچ بازگشتی به وضعیت پیش از ۲ مارس وجود ندارد.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17791" target="_blank">📅 20:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اطلاعات آمریکا هشدار داد که اسرائیل احتمالاً توافق هسته‌ای ایران را تضعیف خواهد کرد</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17790" target="_blank">📅 19:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17789">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">در راستای افزایش مخالفت با اسراییل در کشورهای غربی:  آلمان طبق گزارش RIAS، بالاترین تعداد حوادث ضدیهودی را در تاریخ خود ثبت کرد؛ ۸۷۲۵ مورد در یک سال.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17789" target="_blank">📅 18:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17788">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b325ce33.mp4?token=tL5fZJDQ3Wc6EX0sOKukexn6Shc84OU4LZXo0wda-OieqWHkjgtmgUuznI8FLXtWVZ0HJmubt27LTzC2fV5XekpOZ7Efm_4DLpHGcfochaMOKzDVVuBZlEXD_vh2REy_iXSEl9QELzjwiT0z9ujQx-iD0u28bQT2shSQmXOnV59wRtKDUVS2ai1ss9d0FwxTvg7w_RHat7HMjfISzriY0HxEHbkNYXTX6Fb3F28IcWpBg6kMjsWSYpwLsqlPwsrNjP_ZtlFNS5rLt7xnm77wzJRkq6Rmvtnz9Ued6sx6tU3U8lvmOyZCFdticujAObSdUPvD2Vm6U09sz5BsqnT45Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b325ce33.mp4?token=tL5fZJDQ3Wc6EX0sOKukexn6Shc84OU4LZXo0wda-OieqWHkjgtmgUuznI8FLXtWVZ0HJmubt27LTzC2fV5XekpOZ7Efm_4DLpHGcfochaMOKzDVVuBZlEXD_vh2REy_iXSEl9QELzjwiT0z9ujQx-iD0u28bQT2shSQmXOnV59wRtKDUVS2ai1ss9d0FwxTvg7w_RHat7HMjfISzriY0HxEHbkNYXTX6Fb3F28IcWpBg6kMjsWSYpwLsqlPwsrNjP_ZtlFNS5rLt7xnm77wzJRkq6Rmvtnz9Ued6sx6tU3U8lvmOyZCFdticujAObSdUPvD2Vm6U09sz5BsqnT45Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17788" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17787">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مسئول ارشد اسرائیلی:   ما در آتش‌بس هستیم؛ اگر حزب‌الله به ما حمله نکند، پس در زمان جنگ نیستیم اما نیروهای خود را در جنوب لبنان نگه می‌داریم</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17787" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17786">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مسئول ارشد اسرائیلی:
ما در آتش‌بس هستیم؛ اگر حزب‌الله به ما حمله نکند، پس در زمان جنگ نیستیم اما نیروهای خود را در جنوب لبنان نگه می‌داریم</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17786" target="_blank">📅 17:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ظاهرا معنی آتش بس از دید نتانیاهو صرفا توقف جنگ از سوی دشمن است.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17785" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک حمله هوایی اسرائیل حدود ۵ دقیقه پس از آغاز آتش‌بس، منطقه نبطیه الفوقا در جنوب لبنان را هدف قرار داد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17784" target="_blank">📅 16:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک حمله هوایی اسرائیل حدود ۵ دقیقه پس از آغاز آتش‌بس، منطقه نبطیه الفوقا در جنوب لبنان را هدف قرار داد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17783" target="_blank">📅 16:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ:  جنگ ایران را تضعیف کرده است! دیگر نیروی هوایی، نیروی دریایی، تجهیزات پدافند هوایی، رادار یا تقریباً هیچ چیز دیگری ندارد، با این حال دموکرات‌ها می‌گویند که وضعیت ایران اکنون بهتر از چهار ماه پیش است. آیا می‌توانید تصور کنید که با این موضوع کنار بیایید؟…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17782" target="_blank">📅 16:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ:
جنگ ایران را تضعیف کرده است! دیگر نیروی هوایی، نیروی دریایی، تجهیزات پدافند هوایی، رادار یا تقریباً هیچ چیز دیگری ندارد، با این حال دموکرات‌ها می‌گویند که وضعیت ایران اکنون بهتر از چهار ماه پیش است. آیا می‌توانید تصور کنید که با این موضوع کنار بیایید؟ مردم چقدر می‌توانند احمق باشند؟</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17781" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ونس:  برخی عناصر در اسراییل به دنبال ایجاد یک دولت شکست خورده مانند لیبی در ایران هستند!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17780" target="_blank">📅 15:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17779">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43093b929e.mp4?token=fY411e5ohnrdmS9mK_l2cgk07ipHD_hQJnSGBid60qQNb0-l4AJ0mZbpJ_gUPV5vL_215gYN7D-jFp87VFD2K_t8-rXAg5moyYAHawjs_0oMMi01X3FKy6jZleIsqxZHnN3EjYiTZi1z5dGzIWsWWWY0-JGVeGMeA7gKwisd0K_rcO65P3yhpw9VCJ3n6kvBwrZzAHTOGYNaSohHWAPOJUv30AjgPs2FszJYCnyNoXfICSu03-ayp5NdNzzYneHED1Om9YEbX8mA-BVq7Jxzgi2BGxLeSSLr0LhPPiQKN21Rc8tH8aSiRMk5rgo7F0Ll64cnCFRydyGN5gF2WtyazA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43093b929e.mp4?token=fY411e5ohnrdmS9mK_l2cgk07ipHD_hQJnSGBid60qQNb0-l4AJ0mZbpJ_gUPV5vL_215gYN7D-jFp87VFD2K_t8-rXAg5moyYAHawjs_0oMMi01X3FKy6jZleIsqxZHnN3EjYiTZi1z5dGzIWsWWWY0-JGVeGMeA7gKwisd0K_rcO65P3yhpw9VCJ3n6kvBwrZzAHTOGYNaSohHWAPOJUv30AjgPs2FszJYCnyNoXfICSu03-ayp5NdNzzYneHED1Om9YEbX8mA-BVq7Jxzgi2BGxLeSSLr0LhPPiQKN21Rc8tH8aSiRMk5rgo7F0Ll64cnCFRydyGN5gF2WtyazA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر رییسی نژاد استاد تمام عیار ژئوپولیتیک است اما خواننده Secret Box از ۷ ژوئن میدانست متاسفانه استراتژی اسراییلی ها به سمت پلن B یعنی زدن زیرساخت‌ها و ایجاد یک دولت ورشکسته چرخیده است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17779" target="_blank">📅 15:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17778">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سی‌ان‌ان به نقل از منابع آگاه:
آمریکا به ایران اطلاع داده که اسرائیل حملات خود را در لبنان تشدید نخواهد کرد</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17778" target="_blank">📅 15:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17777">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYDSpFYHTQ1unbU14x6xEN7ossImOUBYypjfifGQkjdCtMBDc0W4PLyfmuB_Yy_sJFni9zdKtt98H9K6lGKVZr80KsRgpKZbju8xgwf-EN-78MGVP6H2y_0rAwlAzkXOhSn2OujtcxkQVyzjQMp1K7j8MNjEtJxcNsr_V3yCbZa3cfRxUFPYMSKU4LqHAMywrLv_2zcePUHxbPuov6QIf7btzRXN0L6HTelaxMkgFq8J4RvcF7uYG8KYtN53v9tsEv_uAxIhBis1ajjUFmTnh_wVBj8v9sLYda9TLExI9KqTUoCMS_aD1Nyw5nIXym2iVLTDaJeQEnzbh60k2PBAaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرندی</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17777" target="_blank">📅 14:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17776">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس:   با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17776" target="_blank">📅 14:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17775">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس:   با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17775" target="_blank">📅 14:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17774">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس:
با عنایت به امضای تفاهم‌نامه اسلام‌آباد و ابلاغ دستور مقامات ذیربط، به اطلاع متقاضیان عبور از تنگه هرمز می‌رساند در بازه زمانی اعلام شده، عبور کشتی‌هایی که درخواست عبور خود را با رعایت نکات لازم ارسال نمایند، انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17774" target="_blank">📅 14:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17773">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کلا تا اواخر دهه ۱۹۷۰ میلادی، عمده احزاب اسراییلی مبتنی بر ایده های سکولاریستی و مدرن بوده و اغلب سیاستمدارانشان هم اروپایی تبار بودند .
اصرار زیاد بر جذب مهاجران یهودی خصوصا از خاورمیانه و آفریقا (عراق، ایران، یمن، اتیوپی، مراکش …) باعث شکل گیری جوامع عقب مانده حاشیه نشین در اسراییل شد و حزب لیکود هم بر پایه خواسته های اینان قدرت گرفت.
اکنون این سفاردیم ها به سرعت جمعیتشان از اشکنازی ها در حال پیشی گرفتن است چون زادوولد بیشتری دارند و به نظرم از عوامل خشونت های اخیر در غزه و … همین ها بوده اند.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17773" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17772">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شاید…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17772" target="_blank">📅 14:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17771">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر امنیت ملی اسراییل ، ایتامار بن گویر:  امشب تهران باید بسوزد!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17771" target="_blank">📅 14:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17770">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارشهایی مبنی بر پیشروی سنگین نیروهای اسرائیلی برای محاصره کامل و تصرف نبطیه!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17770" target="_blank">📅 14:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17769">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">در جریان درگیری‌های ۲۴ ساعت اخیر در جنوب‌لبنان تاکنون ۴ سرباز اسراییلی کشته شده و ۱۷ تن دیگر زخمی شده‌اند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17769" target="_blank">📅 14:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17768">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">داداش مسعود الان لابد فهمیده  چرا الان آدم حسابش کرده اند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17768" target="_blank">📅 12:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17767">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شریعتمداری:   مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17767" target="_blank">📅 23:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17766">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شریعتمداری:
مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/17766" target="_blank">📅 22:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17765">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwy0lDrJ5g2kbgE8IhOeC0w9Xt3ndwH53Vp9s7qacTSYOk7F1_XRLdydSbOmYaSDqi74htyyxKaXFbLiD7qSyrrMzJr8xSX8T2hJacOD2JDFW-ONRIUGFAZIKAJl1ZArBsUHEgMMjlZq07sqMKzB4ydrQ6BvmXejv0gG4Zi6XNEgwCjVZa8VSoRVJPy3-FfJq4fWI-7zWxxfEDtNk1tzDEc2hq37sbpIquu46h73ztnXjzDRJjqWruZEl6XCsy2ubHTFaprXhhe7YwVWFMwwRWA0VIPU9RZ6v5Qs3xt_7zHNQXbYtsYp-p8N_mkvfAN-__xT_eMQHrky5eCjAO4W0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر از چکیده پیام رهبری</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/17765" target="_blank">📅 22:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17764">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چه کسی گمان می‌کرد روزی این امضای موزگونه زیر برگه ای بخورد که امضای ابوایوانکا هم روبروش باشد؟!  سبحان الله !</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17764" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17763">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ :  «اگر به نتیجه برسد، من اعتبارش را می‌گیرم. اگر به نتیجه نرسد، جی‌دی را مقصر می‌دانم.»   «بهتر است مراقب باشی، جی‌دی!»  «او هواپیمایش را برمی‌گرداند و از اینجا گم می‌شود.»</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17763" target="_blank">📅 22:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17762">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">متن کامل پیام رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
🔹
بسم‌ الله‌ الرّحمن ‌الرّحیم
ملّت پرشور و باوفای ایران
همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین امر، از سر دلسوزی و با حُسن نظر، تلاش‌های زیادی را به‌عمل آوردند و البته این رئیس‌جمهور آمریکا بود که از روی استیصال، از انواع اهرم‌ها برای این امر استفاده می‌کرد.
🔹
بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت حقوق ملّت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه‌ی آن را صادر نمودم‌. ایشان همچنین تصریح کرده‌اند که اگر طرف آمریکایی بخواهد زیاده‌خواهی کند زیر بار آن نخواهند رفت. از این لحظه، ما یعنی شما ملت سرافراز و این خادم ناچیز، منتظر تحقّق شروط گفته‌شده خواهیم بود. امّا بدیهی است مذاکرات حضوری که در آینده برقرار خواهد شد، به معنی پذیرش نظر دشمن نخواهد بود. امیدواریم که دعای خیر سرورمان عجّل‌الله‌تعالی‌فرجه‌الشّریف انواع نصرت‌ها و فتوحات، برای ملّت باشرف ایران به ارمغان آورد.
🔹
والسّلام علیکم و رحمة الله و برکاته
✍
سید مجتبی حسینی خامنه‌ای
🗓
۲۸/خرداد/۱۴۰۵</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17762" target="_blank">📅 21:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17761">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17761" target="_blank">📅 20:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17760">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده:   ناو‌های نیروی دریایی ایالات متحده برای اطمینان از رعایت تمام مفاد توافق‌نامه در منطقه باقی خواهند ماند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17760" target="_blank">📅 20:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده:
ناو‌های نیروی دریایی ایالات متحده برای اطمینان از رعایت تمام مفاد توافق‌نامه در منطقه باقی خواهند ماند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17759" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17758">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-poll">
<h4>📊 در عصر مدرن، کدام کشور زیرساخت‌های نظامی زیرزمینی را به یک استراتژی ملی تبدیل کرد؟</h4>
<ul>
<li>✓ آلمان</li>
<li>✓ سوییس</li>
<li>✓ کره شمالی</li>
<li>✓ سوئد</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17758" target="_blank">📅 20:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17757">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام بسیار مهم رهبر معظم انقلاب حضرت ایت الله خامنه‌ای مدظله‌العالی درخصوص تفاهم پایان جنگ خطاب به ملت ایران تا ساعتی دیگر منتشر خواهد شد</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17757" target="_blank">📅 20:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17756">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ونس در مورد ایران و موشک‌ها:   ما انتظار داریم که به عنوان بخشی از توافق نهایی، ایران موشک‌هایی که کل جهان را تهدید می‌کنند، نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17756" target="_blank">📅 20:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17755">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ونس در مورد ایران و موشک‌ها:
ما انتظار داریم که به عنوان بخشی از توافق نهایی، ایران موشک‌هایی که کل جهان را تهدید می‌کنند، نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17755" target="_blank">📅 20:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17754">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فایننشال تایمز:
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌ های بلوکه‌ شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17754" target="_blank">📅 20:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آفند زرهی سنگین حاجی فتل به جوان دانشمند بمال صداوسیما
نابودش کرد !</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17753" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17752">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ فاش کرد که حملات و بمباران‌های ایالات متحده بیش از ۱ تریلیون دلار به ایران خسارت وارد کرده است.  «بازسازی آنها ۱۵ تا ۲۰ سال طول می‌کشد. بنابراین باید خودشان رفتار کنند. اگر رفتار خوبی نداشته باشند، دوباره ضربه می‌خورند.»  ترامپ همچنین تأیید کرد که ایالات…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17752" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17751">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBqdktitpSa72oTyb_B8Mgl8dZlW9WF0LNdkOa7uZmDjiFpL_wVdsgXdUEz10YB1aohtAm7rwfLEwNix5vAe798vjJIysQlO-BRc-JP4i5SL6SmkELuvHaNoEqe5dx56vBspyHR5LT5P2_P456yCwlPtouelP70ez2-6vusxmDUqsmDfiMg56_t3tA0JUF5wQvmQAr7eJmZGRR4QbycaLW-av1MwmcMYgBfeU2qKZvFNK_lRC83NdP_BCNHzDIHp1Q1ltcM35ld009X5OAzo_jfHbyQpgs_7RbsGF9l_lkC9qU0x862SI8DjE_utrB9mXdRsZicGuuaIjFweH2_eaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی کانالهای ارزشی این عکس را منتشر کرده اند و نتیجه گرفته اند انتخاب این مدل و رنگ لباس از سوی پزشکیان نمیتواند اتفاقی باشد!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17751" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17750">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وضعیت مسکو پس از حملات سنگین پهپادی اوکراینیها به تاسیسات انرژی</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17750" target="_blank">📅 19:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17749">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نمودارهای برگرفته از سایت شرطبندی Polymarket نشان‌دهنده سقوط چشمگیر شانس‌های انتخاباتی بنیامین نتانیاهو در ماه‌های اخیر است.   خط زرد (احتمال نتانیاهو به عنوان نخست‌وزیر بعدی) از حدود ۵۰-۶۰٪ در فوریه با نوسانات اولیه به اوج می‌رسد، اما از اواخر مارس با شروع…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17749" target="_blank">📅 17:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17748">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/17748" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بی‌بیِ بی‌چاره!   نتانیاهوی بی‌چاره! چی فکر می‌کرد، چی شد! این سزای کسی است که گمان می‌کند با زور اسلحه و کشتار به هر هدفی می‌توان دست یافت! تازه این اول بیچارگی اوست. در انتخابات پاییز امسال شاید حزب او بتواند یکی-دو کرسی نمایندگی بیش از دیگر احزاب در پارلمان…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17748" target="_blank">📅 17:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17747">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">برخی گمان می‌کنند رفتن نتانیاهو یعنی پایان قطعی جنگ اسراییل ضد ایران و محور مقاومت.   توهم محض است. دیدگاهم را در یک صوتی مفصل با شما به اشتراک خواهم گذاشت.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17747" target="_blank">📅 17:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17746">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فیصل بن فرحان آل سعود، وزیر خارجه عربستان:
«حمله ایران به پادشاهی و کشورهای شورای همکاری خلیج فارس، اعتماد متقابل را سلب کرد.
پس از تفاهم پکن و آغاز روند عادی‌سازی روابط، ما در آستانه گشایش همکاری‌های اقتصادی بودیم، اما اکنون عقب‌نشینی کرده‌ایم.
پیش از هر بحثی درباره سرمایه‌گذاری یا همکاری، باید درباره بازسازی اعتماد و رابطه گفتگو کنیم؛ این مسئله برای بسیاری از کشورهای شورای همکاری نیز صادق است.»</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17746" target="_blank">📅 13:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17745">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_tJbgYvXAFlno3RDPYYp7DnPFY5lWnvNgd9OKDATYA80x_CfXU_aXIHBh1DtTKg8EhgB-7Dxiu5TOt1t4Vxou0k4tirG53yrol_shzksN-h_mJc7w-ga4xZ6HC3FZpTJTlC85zwTFJ5-edXWw4PiJ-LpNXlJQgTrj5p29lZl-RMSb_UPnQvuneFyCEcJ-r6fbCZaClnFESGx-w9fmOZ6x-Jaijm2HQDY6iNe68arNiP25cShK1ZYRATZosVXNmUl-5DqNNgZuQvS9rsp4LHPxxnEAM1hQ7-K844mwRiunFCPXdQ6q5LrpPIZOqybkEAMF7o3NxKRDfLxgXTZv8ibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل نقشه منطقه حائل در جنوب لبنان را منتشر کرد
ارتش اسرائیل نقشه‌ای منتشر کرد که نشان می‌دهد منطقه امنیتی آن تقریباً ۱۰ کیلومتر به داخل خاک لبنان گسترش یافته است، جایی که نیروها به عملیات برای حذف تهدیدات و حفاظت از ساکنان شمال اسرائیل ادامه می‌دهند</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17745" target="_blank">📅 13:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17744">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17744" target="_blank">📅 13:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17743">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‎روزنامه اکونومیک تایمز  هند و روسیه توافق کردند تا نسخه پیشرفته تر موشک «Brahmos» را در تیراژ بالا تولید کنند.  در جنگ اخیر هند و پاکستان، این موشک بهترین ابزار هندی ها بود و بر خلاف نبردهای هوایی، مایه جبران مافات برای ارتش هند شد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17743" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17742">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رئیس بانک ملی سوئیس: مشخص نیست کاهش تنش در خاورمیانه دائمی باشد یا خیر</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17742" target="_blank">📅 12:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17741">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رئیس بانک ملی سوئیس: مشخص نیست کاهش تنش در خاورمیانه دائمی باشد یا خیر</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17741" target="_blank">📅 12:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17740">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اینها مواردی است که اسراییل را به سمت یک راهکار نهایی پایدار منطقه ای بوم پایه  — بجای آویزان شدن از غرب (و خصوصا آمریکا) — می برد و کریدور داوود و پیمان موسوم به کوروش و … در چنین بستری معنا می یابد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17740" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17739">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ7bHBwG2_1FYsS2o7u05QkRfawQ9vYE6kZ75Grd9v6L96WJB2QzDbwS43o-eg2phNhXTeNGIBSsqjRGQEbw_YsEhBJmFXjWecyOo9ufCi0_PBjMLJsSLdJr3MIuziNEXFMwbUm3P9joIzK1kohaDqFTabunFdWC-S--o2H-ku7GlGzrEOVOZZcpPzBeKuo739lxGgGg01RgmT54Ehfc6paFvB9-_hb4gUGmD0xtOMMXSijZCw6HDxc_XAA_46RoasZiEwmim3sJ8318BJ1_PJjqb63GukX1TziuU_mbR-vnv3HP-ZTKKQ1TCHEoKJLjxCLxnvt0iOxY6Zf0u74OgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت مسکو پس از حملات سنگین پهپادی اوکراینیها به تاسیسات انرژی</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17739" target="_blank">📅 12:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17738">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ولی انصافا اگر همه این مواردی که قالیباف می‌گوید در توافقنامه با آمریکا از سوی ترامپ امضا شده باشد امتیازات بزرگی برای جمهوری اسلامی ایران است.  بحدی این امتیازات زیاد است که آدم فکر می‌کند یا جمهوری اسلامی سلاح هسته ای دارد یا چند نسخه از فیلم های مستهجن…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17738" target="_blank">📅 12:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17737">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6CGH_a7J8KmTABH-QHQmkkXmFQzGxC9Wefp_0nmRJ7E_cCBRSp17_Rkq00LRhtlABvv8H-8isCedg4yxWS42X8cmfH5Dgyt7-m6-SOXBph2VIHEM6pdDatqUZEgdQNetxg_YvcImUiNAueSJ3xL_GH-WzHoQOx6NguNaywEWqH5AFVN40jp2iRRutLEQOknec7nMu4uCC84sZSuhRmZOVkab0Y7h4Fswq7mKjaU2y-QZBS2A3TdCquracvpeMyxj-4EDoWkUv6xQ5QYgIfO8OkXlGaZVsZUkfep68u7vtGNRlptgQiNiz3_tNp2Wj6Raoz3Ssi93dXNLEw6oJb1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی گمان می‌کرد روزی این امضای موزگونه زیر برگه ای بخورد که امضای ابوایوانکا هم روبروش باشد؟!  سبحان الله !</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17737" target="_blank">📅 11:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17736">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو: اسرائیل به بند لبنان در توافق ایران و آمریکا پایبند نیست!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17736" target="_blank">📅 11:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17735">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17735" target="_blank">📅 11:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17734">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOeOX3SQZj4-E_slkmhps__L-qHV_w3YhJ9ndiN9Ak4520RC2adP1hEoExT83KOfdNrWtw3MsdEHW1TC5cmVJqKI4HaJhsWPeu8aeKTQEdu312Qx7pk64uUrjdTe2GxlKGukP9jfGcEIGLUmsCZC57CrMx9C8OFTizwDzWCu6PaLGaO_yGXKIVwZ1qlGXR6V996i8wbRNrK3aBlojPr6iIMoRIsFL-xS2-gGcTXCC-2kiSg7p-65flCBtpWvK4efY7I6d6jFlStbd7bdtttv8A7uKBzHDWvpsu-VWoWx9VdWFdlz2tJsKF4leTBYhl_CRHejRqzAK63erwanbvgTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پرزیدنت پوزیده مثل موزی است که بخواهد ماهیگیری کند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/17734" target="_blank">📅 07:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17733">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به عنوان بخشی از بند عدم مداخله در امور داخلی ایران، رئیس‌جمهور ترامپ توافق شفاهی داده که دیگر بیانیه‌های حمایتی از «اعتراض‌کنندگان» ایرانی صادر نکند، دستگاه‌های ارتباطی ارسال نکند، یا به آن‌ها سلاح ندهد</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/17733" target="_blank">📅 01:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17732">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ایالات متحده آمریکا متعهد می‌شود که بلافاصله پس از امضای این تفاهم‌نامه تا زمان لغو تحریم‌ها، وزارت خزانه‌داری ایالات متحده معافیت‌های لازم را برای صادرات نفت خام ایران، محصولات نفتی و مشتقات آن و همه خدمات مرتبط شامل معاملات بانکی، بیمه، حمل‌ونقل و غیره صادر کند.
ایالات متحده آمریکا متعهد می‌شود که وجوه و دارایی‌های مسدود یا محدودشدهٔ جمهوری اسلامی ایران را بلافاصله پس از اجرای این تفاهم‌نامه به طور کامل در اختیار قرار دهد.
ایالات متحده آمریکا و جمهوری اسلامی ایران در طول مذاکرات بر رویه‌های مربوط به آزادسازی این وجوه توافق خواهند کرد. این وجوه، چه در حساب اصلی باقی بمانند یا منتقل شوند، باید به طور کامل قابل استفاده برای پرداخت به هر ذی‌نفع نهایی که بانک مرکزی جمهوری اسلامی ایران تعیین می‌کند، باشند. ایالات متحده آمریکا متعهد می‌شود همه مجوزها و اجازه‌های لازم را صادر کند.
ایالات متحده آمریکا و جمهوری اسلامی ایران توافق دارند که یک سازوکار اجرایی برای نظارت بر اجرای موفق این تفاهم‌نامه و رعایت آیندهٔ توافق نهایی ایجاد شود.
پس از امضای این تفاهم‌نامه و مشروط به آغاز اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این تفاهم‌نامه و ادامهٔ اجرای این اقدامات، ایالات متحده آمریکا و جمهوری اسلامی ایران مذاکرات مربوط به توافق نهایی را صرفاً دربارهٔ سایر بندها آغاز خواهند کرد.
توافق نهایی توسط قطعنامهٔ الزام‌آور شورای امنیت سازمان ملل متحد تأیید خواهد شد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17732" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17731">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">متن توافقنامه به روایت فارین پالیسی:
تفاهم اسلام‌آباد بین ایالات متحده آمریکا و جمهوری اسلامی ایران
ایالات متحده آمریکا و جمهوری اسلامی ایران و متحدان‌شان در جنگ فعلی، با امضای این تفاهم‌نامه، خاتمهٔ فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله لبنان، را اعلام می‌کنند و از این لحظه به بعد متعهد می‌شوند که هیچ جنگ یا عملیات نظامی علیه یکدیگر آغاز نکنند، از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین نمایند. توافق نهایی، خاتمهٔ دائمی جنگ در همه جبهه‌ها از جمله لبنان و سایر مفاد این بند را تأیید خواهد کرد.
ایالات متحده آمریکا و جمهوری اسلامی ایران متعهد می‌شوند که حاکمیت و تمامیت ارضی یکدیگر را محترم بشمارند و از دخالت در امور داخلی یکدیگر پرهیز کنند.
ایالات متحده آمریکا و جمهوری اسلامی ایران متعهد می‌شوند که ظرف حداکثر ۶۰ روز (قابل تمدید با توافق متقابل) مذاکره کرده و به توافق نهایی دست یابند.
بلافاصله پس از امضای این تفاهم‌نامه، ایالات متحده آمریکا شروع به برداشتن محاصرهٔ دریایی خود و هرگونه اختلال یا مانع علیه جمهوری اسلامی ایران خواهد کرد و محاصرهٔ دریایی را ظرف ۳۰ روز به طور کامل پایان خواهد داد. در این دوره، تردد کشتی‌ها متناسب با تعداد تردد پیش از جنگ که توسط جمهوری اسلامی ایران بازگردانده می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود نیروهای خود را ظرف ۳۰ روز پس از توافق نهایی از نزدیکی جمهوری اسلامی ایران خارج کند.
پس از امضای این تفاهم‌نامه، جمهوری اسلامی ایران با به‌کارگیری بهترین تلاش‌های خود، تمهیدات لازم را برای عبور ایمن کشتی‌های تجاری بدون دریافت هیچ هزینه‌ای به مدت ۶۰ روز از خلیج فارس به دریای عمان و بالعکس فراهم خواهد کرد. تردد کشتی‌های تجاری فوراً آغاز می‌شود و با توجه به نیاز به رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز به طور کامل برقرار خواهد شد. جمهوری اسلامی ایران با سلطان‌نشین عمان گفتگو خواهد کرد تا ادارهٔ آینده و خدمات دریایی در تنگهٔ هرمز را، با مشورت سایر کشورهای ساحلی خلیج فارس و در چارچوب حقوق بین‌الملل و حقوق حاکمیتی کشورهای ساحلی تنگهٔ هرمز، تعیین نماید.
ایالات متحده آمریکا متعهد می‌شود که همراه با شرکای منطقه‌ای، طرح قطعی و مورد توافق متقابل با حداقل ۳۰۰ میلیارد دلار برای بازسازی و توسعهٔ اقتصادی جمهوری اسلامی ایران تهیه کند. سازوکار اجرای این طرح به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. همه مجوزها، معافیت‌ها و اجازه‌های لازم برای انجام معاملات مالی مرتبط توسط ایالات متحده آمریکا صادر خواهد شد.
ایالات متحده آمریکا متعهد می‌شود که همه انواع تحریم‌ها علیه جمهوری اسلامی ایران شامل قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های هیئت مدیرهٔ آژانس بین‌المللی انرژی اتمی و همه تحریم‌های یک‌جانبهٔ آمریکا (اولیه و ثانویه) را طبق برنامهٔ زمانی مورد توافق، به عنوان بخشی از توافق نهایی لغو کند.
جمهوری اسلامی ایران و ایالات متحده آمریکا اهمیت حیاتی مسئلهٔ لغو تحریم‌های فوق را درک کرده و عزم خود را برای رسیدگی فوری به این موضوعات در مذاکرات به منظور دستیابی به توافق متقابل اعلام می‌دارند.
جمهوری اسلامی ایران مجدداً تأیید می‌کند که سلاح هسته‌ای تولید یا توسعه نخواهد داد.
ایالات متحده آمریکا و جمهوری اسلامی ایران توافق کرده‌اند که وضعیت مواد غنی‌شدهٔ ذخیره‌شده را طبق سازوکاری که به صورت متقابل توافق خواهد شد و مطابق با برنامهٔ زمانی ذکرشده در بند هفت، حل و فصل کنند؛ به‌گونه‌ای که حداقل روش، رقیق‌سازی در محل تحت نظارت آژانس بین‌المللی انرژی اتمی باشد. دو طرف همچنین توافق کرده‌اند که مسئلهٔ غنی‌سازی و سایر موضوعات مورد توافق مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران را بر اساس چارچوب رضایت‌بخشی که در توافق نهایی مورد توافق قرار می‌گیرد، مورد بحث قرار دهند. توافق نهایی مفاد این بند را تأیید خواهد کرد.
ایالات متحده آمریکا و جمهوری اسلامی ایران اهمیت حیاتی مسائل هسته‌ای فوق را درک کرده و قصد خود را برای رسیدگی فوری به این مسائل در مذاکرات ابراز می‌دارند.
تا زمان دستیابی به توافق نهایی، ایالات متحده آمریکا و جمهوری اسلامی ایران توافق دارند که وضعیت موجود را حفظ کنند. جمهوری اسلامی ایران وضعیت فعلی برنامهٔ هسته‌ای خود را حفظ خواهد کرد و ایالات متحده آمریکا هیچ تحریم جدیدی اعمال نخواهد کرد و نیروهای اضافی در منطقه مستقر نخواهد کرد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17731" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
