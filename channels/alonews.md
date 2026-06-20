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
<img src="https://cdn4.telesco.pe/file/U7qvtq72NWbF3y0_-ZK86TGkaJa0r0jGvHfUpRDvlKwJ_7PCf6nBuwVaOkyDPOl77B7Xdvror99B8W0BummUJVxpgwKMoMzZt5g7Y3zHf_MspIdZXxnM7iqXbCyZ01D8jRHjOVpdj29mSQHn5h9UNYEXzWuKd485g5F4ZQCOXtCTVjBrznmJ0ciJcCiT36aSpE3QYEFTGZsBnnkvPaPr6_JtCDptZZGZBJzHzIVihMAluzuIuPd6XDhI5gYC6y23C5t1bU077zL1CYstXH_T0eBiEKNjxw695y6CC4IDBSs9dp0vPkzIVzPLf3WoiO4soPEFN057piWRWF4gQZftmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 958K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 19:42:19</div>
<hr>

<div class="tg-post" id="msg-129410">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfXfjokzo-7Gl1HsvrVcylIV6MvQdfsPmUGNmlXMdOc7-qVk4ovwzSQtil0UX1YrAP1hb0Xshmrzwa6N_f2ufcMXHVjaLqY5gNqfJXGP3bEs4FfuMICQXxBKu_oTIU0uBKUotRoIN0j-7qKDGL7fK5rEKZhIgTQDoPiFnZdUBN2eIUv4uHLcavr6mrVYGkH5vvDGN6fuu5tri-LA9Kqo8oKUYxwsRSPKqB1yzrNpC-u8JFQIgWHelC_OU66MbAh-LaL4DsmxPCtfoOvTNZJl3mpwr65Sf1KxBn08weU7xGUzD-HwZBEgBrBmtlYEXXMr3N3UznZ8TB5hM5gWrazkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخبر: وقتی توافق روی کاغذ بماند، جریان انرژی خاورمیانه هم متوقف می‌ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/alonews/129410" target="_blank">📅 19:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129409">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgSmY2a62QOKV86WeKqUVSN1GodKOc4AryZmEQvujOlHs7Fc7gQNZkKsK7hsu7WBJPMqW7Lbt3iRhc1z8lcY70ULqx5bYvzgMNnRSGpkWq7JIT8AMa_gt8i7EuYlxct7jL3cs5d-VkNI1_3wJFJ3nqHtH_dav_R4ZoVBYbu4R2iu3cPgVw-5gA3CRU0oj_00CiejubZG_h6_zgwozaDCo2YQoq9uNPqn3MAaVwC0dcVo_iZd_KEQNGevFIRi-E5Qmc66SWiDIge2Y7k1gPPktQGKphcHYhV1-W_0bcbEeHfsTL5W-t-ZamJ6AnXHGKVmLfi0ZKzeBZDxdcJNECBp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: تاکنون، خط اعتباری که به تهران اجازه دسترسی به دارایی‌های مسدود شده‌اش را می‌دهد، فعال نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/129409" target="_blank">📅 19:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129408">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd9f0207c.mp4?token=dqF-Ok3YjXYXd6nwZPTMe8i_ZokxqGoxmIXZyP_-Szeo-3RXFG6UogWvadJPJUIjcMSAHWdl41NXdLLqvtSb3HndmZ8fOa5mpxcYa7Xy3WpCQiZofuuT1ifgERSEMMqjEAcSG53FCzi9tTm0dkDL6pKN7OyuLufRBe5XVaxzgphaRflyyDCS9Trubal1Zhu8On_BxFvrMPwot6Eqr38JI73DBMPW_1KqPaQOfMfzEFUQEtCu0aCwCn16UH3XKt4QZWIVEdfQeDtAXP7BqjhjLdqvF-wDTJ3VUXwQNr6A35zWQ3lJ0fCmEPVgr7BQR_fN6tVIF-NI9V2FpfA9aBk1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd9f0207c.mp4?token=dqF-Ok3YjXYXd6nwZPTMe8i_ZokxqGoxmIXZyP_-Szeo-3RXFG6UogWvadJPJUIjcMSAHWdl41NXdLLqvtSb3HndmZ8fOa5mpxcYa7Xy3WpCQiZofuuT1ifgERSEMMqjEAcSG53FCzi9tTm0dkDL6pKN7OyuLufRBe5XVaxzgphaRflyyDCS9Trubal1Zhu8On_BxFvrMPwot6Eqr38JI73DBMPW_1KqPaQOfMfzEFUQEtCu0aCwCn16UH3XKt4QZWIVEdfQeDtAXP7BqjhjLdqvF-wDTJ3VUXwQNr6A35zWQ3lJ0fCmEPVgr7BQR_fN6tVIF-NI9V2FpfA9aBk1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف دل ملت ایران
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/129408" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129407">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
محمد جواد ظریف: از مذاکرات استقبال میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/129407" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129406">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / مقامات ارشد ارتش اسرائیل به کانال 12 اسرائیل اعلام کردند: عملیات نظامی در سراسر جنوب لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/129406" target="_blank">📅 19:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129405">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش ها از اختلال در اکثر همراه بانکها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/129405" target="_blank">📅 19:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129404">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سنتکام بسته شدن تنگه هرمز را تکذیب کرد و اعلام کرد این تنگه همچنان به روی تمام کشتی‌ها باز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/129404" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129403">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
معاون ترامپ: احتمالا طی ۴۸ ساعت آینده به سوئیس خواهم رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/129403" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129402">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: تصمیم نتانیاهو و کاتس برای آتش‌بس در لبنان با هماهنگی ایالات متحده اتخاذ شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129402" target="_blank">📅 18:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129401">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
حمله اسرائیل به غرب خان یونس در غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/129401" target="_blank">📅 18:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129400">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4wZ35UjsuqOjVYobGzT-G8PhjBV2D_I2tHR7m7SNPajuwz-WDNGsCPA1d3wFse6NyXxsfhKy-oW08WWtfAyhxfqkB6Kasntat1M8VkwiMEsSaTdFGf59iJbMA2IIVqJRKLFbTAI7bbBZGdWwzlvm8aPCOw9JrhDYLUoop9r59WglU-lXHQCRHbSgA2XcDeC6KSX-GcRfpcT25zd8RRn_ssI7PX3nrU0pYBtYX3zLScUMcUIzS1hVnPb6EZmjBE-Ema5jvbATC2czIvbtFHG1cDIs9FSv4G2ZIo3MIovIRXY1aVd9Hg6L92j5i71EBnpAIMVoMhiyhVKb6Td_vKCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران‌خودرو: دوباره گران می‌کنیم!
‌
🔴
شرکت ایران‌خودرو اعلام کرد که اصلاحیهٔ قیمت محصولات شرکت که در ۲۸ خرداد منتشر شد تنها تا پایان عرضه دورهٔ سیزدهم اولویت بندی محصولات این شرکت معتبر است.
🔴
‌لذا پس از پایان این دورهٔ ثبت‌نام، قیمت‌های اعلام شده در ۲۷ خرداد ملاک قرار میگیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/129400" target="_blank">📅 18:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129399">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Itdgths6BSy1bTXzyims7f7FLsOkNBtobIlBDzO3TBxg_XD6xQd0GDo0GGLGSmsjurKtz24iqT6_OifLVA7qtMSZVmb847jDNoI4jraFLbxx2puXobuI0ufzzChnYh1wYekdgZVtEHIJCVd_D__dJxgzobg2kLZzdvG2PVN_hrPqNgmnfVclwcc99Aa7Dq9T9it2oZDIrxkQspeXAVXeZ2nrP6VHZ4ljAvp2Q3U-NrJhNJXgAoUvyz-JFvSATKZ_OWQnV4TPDELVt51x303VLbjU-iecqXEWksW4ygEhzsu1_fLSxkwLfotHc5KNKlvIvM-ovP_t31iaGtiKVDK9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای هیئت مذاکره کننده ایرانی در راه زوریخ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/129399" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129398">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سی‌ان‌ان: ونس امروز به سوئیس می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/129398" target="_blank">📅 18:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129397">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: من بسیار مطمئنم که می‌توانیم این آتش‌بس را حفظ کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/129397" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129396">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ عبری : نتانیاهو دستور توقف حملهِ‌ها به لُبنان رو صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/129396" target="_blank">📅 18:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129395">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) انجام دهها حمله هوایی در جنوب لبنان را در طول شب و صبح امروز تایید کرد، اما هرگونه اظهارنظر درباره تهاجم به تپه «علی الطاهر» در نزدیکی «نبطیه» را به طور کامل رد کرده و به جای آن، حملات را به «نقض آتش‌بس» توسط حزب‌الله نسبت می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/129395" target="_blank">📅 18:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129394">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq4UJf7ToEJ79xj7PA0_xwafpQlK3k1WrMH4HZQ_EZxyc0s2UTtIPQiyAaYrp2X5byAM1PISy5quG0_QiCyLGsNHBO7FTkWpW9HG7OQu9GdDSaJ94eg-Ow6Ce9RbtppUQh8t238_VxlStw8UcFrZHf4i2Mn196-khzsa2aVGpdvQFQ01tBKcm0lEMqbUJA7Efra0Xg2d9l3t33V4YaJU-pbRBiE8_e3z5CzyLblKMSu8xiW1TdC5kGu5dCd0MrJa2OVJzhTBV48xEdmSYuOOZgExxZKn24vSE9Z-9z1V3oDwhKonnRNEx4RPqMYJlYgkv6NCi3x4c_Mi0nnKoxV2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129394" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129393">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrwWnmk-hWyVaEDryKmx_QniIoZY_ch5EyAXOQfB5fNaY53EX8D56rEN1-qoXBjSMJu-IBsXT3aItRITBlrJYjZkF5iudri_Droa8SVzxj_LHAt6h0b1aiilRvAaTEbopyUc1ELsPPz7-SXrUwCvDpmXLD2MWgDqH7n7jFlQhdHTd8FozwXqKyuLzAMXsMaqaWrbkz7tBVndEQHoxZ8DSOsIa_Eegtdp5e5kwA6RMLAhuyUb5Exki1R38G6PIXChHZJhYIl6ZCnTgB8jAfpGGySQhuHDxt844ZUGwTYsTL9YIFu0BfcKSRONs2xW2ABijOBm64w1TCFTHx5oBi3ITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ملونی به ترامپ پاسخ داد: رئیس‌جمهور ترامپ، این حملات مداوم و بی‌دلیل بی‌معنی است. در مورد محبوبیتم، دوستی با شما قطعاً کمکی نکرده است و همچنین به رابطه من با شما بستگی ندارد.
🔴
محبوبیتم به توانایی من در دفاع از منافع ملی ایتالیا بستگی دارد، و این دقیقاً همان کاری است که همیشه انجام داده‌ام. این همچنین کاری است که در مورد پایگاه‌های نظامی آمریکا در ایتالیا انجام دادم. استفاده از آن‌ها توسط توافقاتی که همیشه به آن‌ها احترام گذاشته‌ایم، تنظیم می‌شود و تا زمانی که من نخست‌وزیر هستم، نمی‌توان آن‌ها را نقض کرد.
🔴
ایتالیا همچنان یک کشور مستقل است. به هر حال، محبوبیتم به شما مربوط نیست. پیشنهاد می‌کنم روی محبوبیت خودتان تمرکز کنید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129393" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129392">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd8Og7alVTDWzzMUMaUvvSklt9DsqKEj1CudSSZ_tJubLAFCwMrB2gpZJkC-leOisjtWwsPT9WEwIXl3OLEOh4RV-8t3bgQiwZWa3maN4dXi21aQ9YP9e5AiyFjFsdbeqGAzsVYjXKR894V2jzIP4DTsnIeyoCXnOJywyL59RF-alYdHJkslVrkS_OuXSSVq0nvPaKx7TW6udLKb1JbRQVGbQl1yFlgWYl2_dRD-ZgRG7Joq9JJ7cpbZY5HxpkLRy07zYMSa7Ho3fE6GvgPwIib-FxHpVooBBEuWk0gf7KxdqTof37LkHybaQKAXZxouqbVPLceMUIoRoDPyF452_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون تردد بدون مشکل کشتی آمریکایی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129392" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129391">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فکت:
هروقت عراقچی تنها رفته مذاکره، جنگ شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129391" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129390">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
العربیه: قالیباف به ژنو نمی رود؛ عراقچی ریاست هیئت مذاکره‌کننده ایران با آمریکا را بر عهده خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129390" target="_blank">📅 17:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129389">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نیروی دریایی سپاه: شناورها به تنگۀ هرمز نزدیک نشوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129389" target="_blank">📅 17:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129388">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سخنگوی تیم مذاکره‌کننده: آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
🔴
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129388" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129387">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سخنگوی تیم مذاکره‌کننده: طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی
مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129387" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129386">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / ایسنا: هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129386" target="_blank">📅 17:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129385">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری / ایسنا: هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129385" target="_blank">📅 17:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129384">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / الحدث: عراقچی امشب همراه وزیر کشور پاکستان به سوئیس سفر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129384" target="_blank">📅 17:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129383">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / فایننشال‌تایمز: پایان عملیات نظامی اسرائیل در لبنان بعید است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129383" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129382">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فاکس نیوز به نقل از جی دی ونس معاون رئیس جمهور آمریکا: مذاکرات با ایران فردا امکان‌پذیر است و وایومینگ و کوشنر برای انجام این مذاکرات آنجا هستند.
🔴
اوضاع در مذاکرات ایران خوب پیش می‌رود و انتظار دارم به سوئیس بروم.
🔴
به توانایی خود برای حفظ آتش بس اطمینان داریم.
🔴
به مذاکره با ایران فرصتی خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129382" target="_blank">📅 16:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
الاناست که عاصم منیر بیاد تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129381" target="_blank">📅 16:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129379">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قرارگاه خاتم: تنگه رو بستیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129379" target="_blank">📅 16:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129378">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
قرارگاه خاتم: تنگه رو بستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129378" target="_blank">📅 16:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129377">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVUymKUWVFcbq9Wuh48DQU5DQRTQ6zlV_vNB01nPU1CHzLVOm6Izn9jpeKxiaYfnosw_b_wt-JMLQZ1Vvo3HX9QAFh5b_LhszGDL49KyGPtaHeD3RaS0kBiDOrK7s5TqvSl7ufJYCI8qXN6Pe3F6rWB0NvWDBBkOKP0uZTqf-bq7NyHgR9Mk7Kgj5fxLsN7vfTbSe9maIlTBEuEZ5JkapcWFnLd1PikQTzAVUkzwiq_hFoCm-nBpyCnJj1IJPQDiPVJYCj5XJ39owSu0bb6BJjARsphNHAMCXzVBTskEojlfwjR3bGOQPsrKLTfQv8xr1rEXC80OugS_kXthQ_3MOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: از مذاکرات استقبال میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129377" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129376">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سوئیس اعلام کرده است که به ارائه «محیطی محرمانه و قابل اعتماد» در بورگن‌اشتاک برای بحث‌ها درباره اجرای تفاهم‌نامه آمریکا و ایران ادامه می‌دهد و اضافه کرده است که به دلیل محرمانه بودن، هیچ جزئیاتی درباره شرکت‌کنندگان یا محتوای مذاکرات منتشر نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129376" target="_blank">📅 16:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129375">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سیدمحسن نقوی، وزیر کشور پاکستان که امروز وارد تهران شده، با عراقچی دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129375" target="_blank">📅 16:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129374">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خبرگزاری ایرنا : کشتی‌هایی که می‌خوان از تنگه هرمز رد بشن باید با سپاه هماهنگ کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129374" target="_blank">📅 16:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129373">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: نخست‌وزیر ایتالیا در جنگ با ایران همراه ما نبود؛ اکنون می‌خواهد با من عکس بگیرد تا محبوبیتش بالا برود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129373" target="_blank">📅 16:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129372">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رسانه‌های سوئیسی: هیئت‌های مقدماتی ایران، ایالات متحده، پاکستان و قطر از دیروز در اقامتگاه «برگنشتوک» در حال فعالیت برای آماده‌سازی مذاکرات هستند و تاکنون هیچ نشانه‌ای از حضور رؤسای هیئت‌های تهران و واشنگتن دیده نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129372" target="_blank">📅 16:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129371">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dScbv7WDaVqM98mTQ61sJAQ6z1jluo-830TYBwcJ6ByHw-Q3A8PV7v3fdzzFYUhvcAFi-KXH8wiVRxOuO8aw8wMzh_qfOaVtQUAH9dHD001JW9yKGgVTKnWHhSEH5v4TSetT27vmMamFkomF2HC39wEg1c3QSjvuZPeEDEsxH6PQPFaTY8PDBvBqlh1ILuubjiHOj5IHrvDNMaMMyDRZH2mSUGkXHv-J0WBLF0yvcXhYQn3J89ylRxqBWR6vCuMuzvrplrQplgXgT8xnpA0uHvFvv3KLvCWuBl_VRgmDwjeQkn2Vfd1zYb86MMNlOcoaxb7Hi1sVgYUl0885S-bLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «ترامپ برگ‌های برنده را در سرنوشت انتخاباتی متزلزل نتانیاهو در اختیار دارد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129371" target="_blank">📅 16:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129370">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
هم اکنون حملات سنگین به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129370" target="_blank">📅 16:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129369">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx46rqMx-uTuWo6JLr8OqIhsm60LuT7SvPCJyddiATV2P_cNP5cSUiCg6XQMfgyVhfOlt6fUBMPYoE6r5K4AFBDakdLEbC5LQovYUW1bRixR7u_KzDpN96hHATzosfFY4lCO0WGhzHY0SI3_74DWNFIR8lPf_JSoy7ob_HzdsnBm1oOrA2r0Odgf6ey7phxuNSSvctCwWQpbp3rnLSZ87x1REosLY0Ab8C9FoKgsm_aHh1Ag2PUMDBDFtWx4BUjU4UpcMz7CGUpnmmpZYIpzcASK4jSKJHrBZmWHempB0fzBLZYbM4wR2mx0-L4NgeZbHQIxopXLn-JHI2_ReRTarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله پایداری‌ها به فرماندهان سپاه و ارتش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129369" target="_blank">📅 16:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129368">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STs83th69bXpXYIbMEMr0XWOGwehqbr4mJEEZNRKT6J6QSVB59iRj3DPEtNYvl5g2UrWSsS0I7Uf_4HCA6G1t-CoGKF6KBPDIJNXA-n_ZnBkRAivLhusj03LRuIYT9ZqIbbxfCHzVOfjcTVvih3-Zc5gScdjxHAbIUplllrJJXkjp86JblLab2dST8oxcx3BUdAG-kVzAlYWp8ULgiw-_Ci4kfvuSSHwq9pvO9ZDHoh5ssKiFsGz796vQd0MRtZesX-4pFbv07n3XV6pVQyvEU53G4gIvK7S_nP7XzyXM7R04tqi2ob_VvFCoScWK_j6g85TULkFM_NMkc40jtHuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
راکستار: هزینه دیسک بازی GTAVI حدود 70 تا 100 دلار تخمین زده میشه، یعنی برای داشتن این دیسک باید 11 تا 16 میلیون تومن هزینه کنید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129368" target="_blank">📅 16:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129367">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ویتکاف و کوشنر به سوئیس رسیدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129367" target="_blank">📅 15:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129366">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: کسایی که به مراسم تشییع پیکر امام خامنه‌ای بیان، به صورت رایگان تحت پوشش بیمه قرار میگیرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129366" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129365">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR0_iibTyiCOhKIkkgY7CcbnfMX4xtUqBDQhaDESeY3UWFVQ6tjmBLf-7ltJvkRlXZ6wSN6vPIiyn3Vc2oQ-IrFPc9TWfv2GDcwOp6ppVJeQLITzt4UFORVL7ruN79q-Qlpr41Z-QelZ387NVKOKLyQEJl5mY0Mxnom6vvQ_wOup5EqKyL2v3Ja7Gk_UiVz3s8KNQfRt_4UOS9OjveR2hn74UhqTa_06zTMm29PmlgHljAI3s9d_ESG_QlpvTP3i6l4qAZxB8q379el8domS4SrHDLpO4-OAM1N08akIQB-8NoEBR20H41yMI-TdlclBR2jN96HAFGk7Ap-kvdEB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دموکرات‌ها می‌گویند ایران از سه ماه پیش قوی‌تر شده؛ برای همین به آنها می‌گویم «احمق‌ها»
🔴
دونالد ترامپ در اظهاراتی تند علیه دموکرات‌ها گفت:
«جالب است که دموکرات‌ها مدعی هستند ایران امروز نسبت به سه ماه پیش در موقعیت قوی‌تری قرار دارد، در حالی که از نظر نظامی شکست خورده و دیگر نیروی دریایی یا نیروی هوایی مؤثری ندارد.»
او با تمسخر رقبای سیاسی خود افزود:
«به همین دلیل است که به آنها می‌گویم Dumocrats (احمق‌ها)!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129365" target="_blank">📅 15:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129363">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMcFNTWF0o3OGFd5xmDTbVHv4f_5nu9ZIKNvBaS-4Etode7oYFJ5oGWDZgEHTksvhE1eHYDwHRKnW8uWRWDH-n_cPIF9sKN5UPY5xtvdlIfgB5CYGDvsvLYZtKtj1051B_OUcSo1DXn7WAzaJVbbvS9UO0VzcTHJJqFOcM_RBVVle_oDrpsnDAwNamG1TLxk-MAFdXbRYmsbkIitcWTreBgxZO_28fl1lf9Xk_HCUNDzzbubYi19_HP1QgUJF0bqNs-esYIhx9GrrKW-POorjO6Pb5Hjoh_J8Igc1g8e-f1O6EiN2BllVAOoJeRodm6tEa3jslYrs7tvIBal_i_EmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FlRs_d__RvGcbpIYlFc0MOTXVvDHn1E92gCWaD2UL5_XXbxUbpGzmyimFz1CGuyXEp9KtfsQAf5qoeA5-Amx2FZX4lVGto0ZgBrQ0giXw9oC4CHuRN5Vrx9lPdBnXJXdCELw06HZU_5CBEm-3w57uq3rVZHcm02cSX65mGjC_SPUcEi0LPeZCAj9zpySLg28M_klMVzAE6gtcf2dwzRjG6fnUzwF5h9wir5R75Cf83S-nDUkiSXCDmDHuzNlkV8vwTaJ1R4l9HOGdM2Nm6dpmS-MjD9v0PyYwyFjgrxz5cgHFaYqTHY0IvngbXazp1Tt3nqGutYWIE4-1EBUfctjSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ:
بعد از جنگی که ما پیروز شدیم، توی اجلاس گروه ۷، ملونی چندساعت منتظر بود تا با من عکس بگیره تا دوباره محبوب بشه اما من گفتم نه، چونکه نزاشت از باند های فرودگاهای کشورش برای عملیات استفاده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129363" target="_blank">📅 15:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129360">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgYv6gDJKqxctzu45dtDDVQOzk7SxmQRnb_Nn0LCl2FZtyNVRlrmc695p0I-QoR4RdE7dhxcfgCYXtBxJVp-zMI5M_Wy1sGsX50a3FpSH-mzMgsBTmokDt9QgH1x61bmjKqCvRCqhhRuPgHVOgZTF-aUOEQrvDCGTU9e6ah1xHA5niLodfXspT1KAci0ITb2qAibO0WXgvsSbFR_iLDo4mnoxJ0CQXxfGl3ZlyFug0Lju6KQ_go_uSZkTxZx3nHcWd1o7TPrMEflNhqAPEz1jkxwaLvNdlv2rGz_gXypmynyBcAljhGKunCl6gVfdXCwD8WMq0NTI-2xNxkhGBD-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d58ab0066d.mp4?token=vO8pYM5mdu013RtdLlHiY2Lueir_VKZKL4nqeS5DbjtzsYC0jKLe2au3EnffAmk6NYmevmUuH8OMfrbXzHx2e3ECZb3brYF6zl2dN9nIdSWtfX_7Owr9DsTjHYTitNu7CCoapWFcPPqo7nB9dbZdUhHFISsr6PlGfp-TkuteilqYRrWdbXAfW8f3jeQtSK5C7xhN91UY_5IDRW4saNsoqIP15AZJnNGpuVppbqpYhRcpagzjjisgvNbq0Rl6m9w386Cf9-4d-jNafMxlf0N2qAJ4Ho4YsWlnoY3ve6G7hMZkWLT_WkaZyf4kTBStg-y1Yd02dnSHwQtyNXRrlERWew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d58ab0066d.mp4?token=vO8pYM5mdu013RtdLlHiY2Lueir_VKZKL4nqeS5DbjtzsYC0jKLe2au3EnffAmk6NYmevmUuH8OMfrbXzHx2e3ECZb3brYF6zl2dN9nIdSWtfX_7Owr9DsTjHYTitNu7CCoapWFcPPqo7nB9dbZdUhHFISsr6PlGfp-TkuteilqYRrWdbXAfW8f3jeQtSK5C7xhN91UY_5IDRW4saNsoqIP15AZJnNGpuVppbqpYhRcpagzjjisgvNbq0Rl6m9w386Cf9-4d-jNafMxlf0N2qAJ4Ho4YsWlnoY3ve6G7hMZkWLT_WkaZyf4kTBStg-y1Yd02dnSHwQtyNXRrlERWew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در خمین؛ گویا یک انبار دچار حریق شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129360" target="_blank">📅 15:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129359">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c58086350f.mp4?token=UnCEh_qaIFAFi7QfGWoFSErpVIHTdlzt6p5OEOVUk77begv3VTMOSUtmOSsD1NEujms1DDt-r0Glj71NLjjPPhsyj2bz6yQoTot7yhcnhH1ZkjLIGFXeDkPRujSzlZV_2tkIWHFk8Vx_Esxv7AWBC88vFrNVgbR074OLaofprhuMU2ifC0PVI68YMl1a_s293YpjTk_4ha1VSfG_P8S8jEqX0QVRDixiCStZt-dTmBahmaX9ZUq-Rs5CdDdnJiaaw6RMg_7-VDkMCGN6xGTqnOQS2PuHelfRs-4zAB5nBVsPe53KIARoGMWhuVGAKH78-5js71bLKkSq8n6bQJHuAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c58086350f.mp4?token=UnCEh_qaIFAFi7QfGWoFSErpVIHTdlzt6p5OEOVUk77begv3VTMOSUtmOSsD1NEujms1DDt-r0Glj71NLjjPPhsyj2bz6yQoTot7yhcnhH1ZkjLIGFXeDkPRujSzlZV_2tkIWHFk8Vx_Esxv7AWBC88vFrNVgbR074OLaofprhuMU2ifC0PVI68YMl1a_s293YpjTk_4ha1VSfG_P8S8jEqX0QVRDixiCStZt-dTmBahmaX9ZUq-Rs5CdDdnJiaaw6RMg_7-VDkMCGN6xGTqnOQS2PuHelfRs-4zAB5nBVsPe53KIARoGMWhuVGAKH78-5js71bLKkSq8n6bQJHuAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری : درباره امضای تفاهم‌نامه با آمریکا، رهبر گفته بود اگه بالای 75 درصد (سه چهارم) از اعضای شورای عالی امنیت ملی موافق بودن، امضا می‌کنیم که همه (حتی نظامی‌ها) موافقت کردن به جز سعید جلیلی؛
-  پزشکیان، رئیس شعام : موافق
✅
- قالیباف، رئیس مجلس : موافق
✅
- اژه ای، رئیس قوه قضاییه : موافق
✅
- مومنی ،وزیر کشور : موافق
✅
- عراقچی ، وزیر خارجه : موافق
✅
- فردی نامشخص، وزیر اطلاعات : موافق
✅
- فردی نامشخص، رئیس ستاد کل نیروهای مسلح : موافق
✅
-  پورمحمدی ، رئیس سازمان برنامه و بودجه : موافق
✅
- حاتمی ،فرمانده کل ارتش : موافق
✅
- وحیدی ، فرمانده کل سپاه پاسداران: موافق
✅
- ذوالقدر، دبیر و نماینده رهبر تو شعام : موافق
✅
- سعید جلیلی : مخالف
❌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129359" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129356">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99a8244ee2.mp4?token=CrNA7_3LG-oXKhKIzi9wKueEkdE2jbFAwyojpudLKhlD6FU4WLZiwxD_nuCoiVUKPNRC0k9xxSzpl5Wr-KHUA-W1LLBSXehthoi1vPzlN6XjWoRTXPwBeo5AZJ9hHAAnwt5qznyJafrl6u8sGxG0R93a48Bvhd-DpWHOlHcyz1re8GrVZ8SCoOc0fWnCjI08N9_N-RBGCY__oPFS8hVF4XMaMMUlUc7roFT_aMk-hgqlDscDJBQbODd-p3D8QrCBhNbW-58htG0q1H-WAKo_p-Lo5ycDGaNcUGpD8iZJo9fzaLOZn4VsxVH1Qh637mZVwn6aBHoG-wb6uWBljl4SEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99a8244ee2.mp4?token=CrNA7_3LG-oXKhKIzi9wKueEkdE2jbFAwyojpudLKhlD6FU4WLZiwxD_nuCoiVUKPNRC0k9xxSzpl5Wr-KHUA-W1LLBSXehthoi1vPzlN6XjWoRTXPwBeo5AZJ9hHAAnwt5qznyJafrl6u8sGxG0R93a48Bvhd-DpWHOlHcyz1re8GrVZ8SCoOc0fWnCjI08N9_N-RBGCY__oPFS8hVF4XMaMMUlUc7roFT_aMk-hgqlDscDJBQbODd-p3D8QrCBhNbW-58htG0q1H-WAKo_p-Lo5ycDGaNcUGpD8iZJo9fzaLOZn4VsxVH1Qh637mZVwn6aBHoG-wb6uWBljl4SEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تخریبی که تو شهرک قناریت بعد حملهِ ارتش اسرائیل صورت گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129356" target="_blank">📅 14:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129354">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuUrJnIT6O7hRpIpT6seb2i2XszIMjnXdHbhMzdTMWDw_vkhGAXto489ftRpvhHYzDvXF4bi2NXuju4HaMplo2ivq2OryfnYIdN4JnMnm2Bk_MUJaU-_OGnAPocNzoweQDMdszt58JZBOlSZdd-Gr0joDfLLBLxd0VyxROXS1yq25Xd4-clJJrgtR854cZb3tb-fqAXgOF8Oj5yQqmCSAJ9Vfw_tKZPlDZke_3n1KDye2JWeNhjyVaEaCPWYHYz8wEr5Yipm7pEz1yBYSrOvVbi5qTB2da5VGRLhglOTK5zvCZMOQ_k-daPzrV2qxlWhYJaLknTbNL1e8wRoyfEmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbHjJNa8AkdcDACISJw3oCzxkqCi8vAiIzI_kbgNCQpjPX9SvDU-a6qoAZ2yUoe4V6HVykHNcfi57A4Wd2TWmg2xW96Cdwp-vIyjcq1ey-cyG4QmbMUdF2gv61SCM4Cb_8JihCVY7yVL9rK8wOpHjWKS_k0j8EAzX3F7xZ37M5v23kVn5_IBom6-HsYKvBKUotkGNMxjQVSjYsi_rh8YvzMbZ50527P-v67zMtHW3wBRHoTCogIdUDtLytz8bMI7wXG7Vvmq0TwW8QlJb4_F26GzQoQDVA_6xHFgdGjrygqPRMasLi8BU4KTODQE87lYLyCYp_wUcrZvwf8DY1SE5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پزشکیان با تیشرت رفت جلسه و گفت امروز کولر نمیزنیم برا صرفه جویی شماهم باید تیشرت میپوشیدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129354" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129353">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
پیش‌بینی سازمان ملل: جمعیت هند تا ۲۰۵۰ به ۱.۶۸ میلیارد نفر می‌رسد، چین تا پایان قرن به ۶۳۳ میلیون کاهش می‌یابد
🔴
بر اساس پیش‌بینی‌های سازمان ملل، جمعیت هند تا سال ۲۰۵۰ به ۱.۶۸ میلیارد نفر خواهد رسید و سپس تا سال ۲۱۰۰ به تدریج به ۱.۵۱ میلیارد نفر کاهش می‌یابد.
🔴
در مقابل، جمعیت چین از ۱.۲۶ میلیارد نفر در سال ۲۰۵۰ به ۶۳۳ میلیون نفر در پایان قرن کاهش خواهد یافت.
🔴
حدود ۶۵ درصد از جمعیت هند زیر ۳۵ سال سن دارند که یکی از بزرگترین جمعیت‌های در سن کار در جهان را ایجاد کرده است.
🔴
تا سال ۲۰۳۰، تقریباً از هر پنج نفر در سن کار در جهان، یک نفر هندی خواهد بود.
🔴
چین اما با واقعیتی متفاوت روبه‌رو است؛ نرخ پایین باروری، جمعیت سالخورده و کاهش جمعیت در سنین باروری، به کاهش مستمر جمعیت این کشور دامن زده است.
🔴
پیش‌بینی می‌شود تا سال ۲۰۴۰، افراد ۶۰ ساله و مسن‌تر حدود ۲۸ درصد از جمعیت چین را تشکیل دهند.
🔴
این تغییر جمعیتی می‌تواند برای دهه‌ها بر بازارهای کار، رشد اقتصادی، تقاضای مصرف‌کننده و رقابت‌پذیری جهانی تأثیر بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129353" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129352">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a4fb2563.mp4?token=GLlaysg0u1QmJCydd-KgdcSyg6sHThcRTaO8sdhHPlWgFF0tLfoIkyz_OpsX9frqo6NJ-utqPJr-PnXCA6Yf8WLfChsVJTVSpaadmyFOaRcIlx4FZVg3s-UngqhMDuLSm-mOXLQA44Dw610E-sB_sZEhu6wznqtg6bK1OTzqjk3rd-TI-9wUDMgDTLpZSr3isqWYDlwySUYlDIUOfBU6IIWXCci40Ou9sOgsnf7OWvI7JJV6Jefolqop_HyH8QCnxngKJQ5JPVEssiZ8ooHCEiiZemyPmIBrzyDI5qaIuLm3lKdJLrNrafj2B-nBj7G5EH-lW6cneobPD6wZPw29WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a4fb2563.mp4?token=GLlaysg0u1QmJCydd-KgdcSyg6sHThcRTaO8sdhHPlWgFF0tLfoIkyz_OpsX9frqo6NJ-utqPJr-PnXCA6Yf8WLfChsVJTVSpaadmyFOaRcIlx4FZVg3s-UngqhMDuLSm-mOXLQA44Dw610E-sB_sZEhu6wznqtg6bK1OTzqjk3rd-TI-9wUDMgDTLpZSr3isqWYDlwySUYlDIUOfBU6IIWXCci40Ou9sOgsnf7OWvI7JJV6Jefolqop_HyH8QCnxngKJQ5JPVEssiZ8ooHCEiiZemyPmIBrzyDI5qaIuLm3lKdJLrNrafj2B-nBj7G5EH-lW6cneobPD6wZPw29WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پلیس محلی آلمان: دو قطار باری روی پلی در «مونیخ» با یکدیگر برخورد کردند که این حادثه منجر به خروج دو واگن از ریل و سقوط آنها از روی پل شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129352" target="_blank">📅 14:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129351">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFOZZN9sSEcBfDAiXRoWVN4GBP9E3G4ssNNT1mrE3pYNCZcQv4h05Sgjz0l9XQLcce4W3L4scPM15UBgivWlS72Tj-cpQCsNayasDcGjCSnqFgQyCG-W4vX5S9VTpWGWTlagUrypsAhhC96gtAIfe7nxr-1aHWZJ9uHIOeri-BPjUrXpKXDFLmGw4Gd9_OXgfWeXsWjS5CHvK58eZ28ogqwh9hkGjZzdmWjagMjlZU4MLcumUBPCpi4uishbtKW2qAA8IMpylUKx84gJ0V0p9YvJfnfQ2pzQA_KOM2pKmVaafVbpTyyDdxwgUl11REt-SSrv_kTWnUpAydxanfKOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه 12 اسرائیل: ترامپ به دنبال سرنگونی نتانیاهو است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129351" target="_blank">📅 14:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129350">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
منابع پاکستانی: سوئیس ظرف دو روز آینده میزبان مذاکرات ایران و آمریکا خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129350" target="_blank">📅 14:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ظاهرا دیشب دوباره اسرائیل تو جنوب لبنان تلفات داده و حداقل ۱۰ نظامی زخمی و یک نفر کشته شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129349" target="_blank">📅 13:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نیویورک تایمز:  مقامات غربی از نتانیاهو خواسته‌اند حملات به لبنان را متوقف کند تا ایران نتواند خروج از مذاکرات را توجیه کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129348" target="_blank">📅 13:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129347">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
منابع العربیه: وزیر کشور پاکستان پیام‌هایی دربارهٔ مذاکرات مرتبط با لبنان را به تهران منتقل خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129347" target="_blank">📅 13:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129346">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
روزنامه واشنگتن پست با استناد به داده‌های شرکت تحلیل اطلاعاتی کپلر گزارش داد که دست‌کم ۲۵ فروند کشتی پس از امضای تفاهمنامه حل و فصل بین آمریکا و ایران، از تنگه هرمز عبور کرده‌اند.
🔴
طبق گزارش این روزنامه، طی پنج روز گذشته حدود ۱۸ میلیون بشکه نفت از بنادر و اسکله‌های ایران خارج شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129346" target="_blank">📅 13:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129345">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک مقام نظامی اسرائیلی: حزب‌الله لبنان شب گذشته بیش از ۵۰ موشک به سمت نیروهای اسرائیلی در جنوب لبنان شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129345" target="_blank">📅 13:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129344">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از آژانس اطلاعات آمریکا: حملات اسرائیل در لبنان ممکن است توافق صلح بین واشنگتن و تهران را به خطر بیندازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129344" target="_blank">📅 13:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129343">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED17ggJ2Anu_5nDHYpKFHjMn-3l0F1VtAj2bQ9ChVUZpKL4mL803IB2uuIoQg5ox2-Cr8Vrp0XO0OXssoxx4s_Zs2hD3FAEq9CRU5oO6qVJPWJQsAauIA0HCPAGBgqnOsk8at-2SdNsIvg4K2Lep-MYjap-nuMwtlSBrZ-lXpdMnqBn-EWeFHtCKeiQ2vps4KzAX3qRMqFTmcmjvoyUY1B-iW_OSPD25pDTPwTpQaN_pi3E2vFDXPa3bHT1fARbANu3LpIda9z29DWI7l4f5lXS7ZFqROijrx6raiLpi0O0-4wo5x1mNDx8Cw1Hca2ZdZHO_lwOUM980eHpI6Pb2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد تند حمید رسایی به بسته بودن مجلس شورای اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129343" target="_blank">📅 12:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129341">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: اینکه بگوییم صفر تا صد تورم و گرانی‌ها متوجه دولت است، دقیق نیست؛ برخی افزایش قیمت‌ها تبعات شرایط اقتصادی کشور و جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129341" target="_blank">📅 12:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129340">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رئیس سازمان سنجش: کنکور سراسری در ۲۹ و ۳۰ مردادماه برگزار می‌شود و هیچ تغییری در زمان آن وجود ندارد.
🔴
نتایج نهایی کنکور در ٢ سناریو اعلام می‌شود: یا نیمه اول آذرماه بر اساس مصوبه فعلی و يا در نیمه اول آبان ماه اعلام می‌شود.
🔴
ايجاد سهميه براى خسارت ديده‌های جنگ انجام خواهد شد و نتیجه پس از جمع‌بندی به شورای عالی انقلاب فرهنگی ارائه خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129340" target="_blank">📅 12:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129339">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ان‌بی‌سی به نقل از آژانس اطلاعات آمریکا: حملات اسرائیل در لبنان ممکن است توافق صلح بین واشنگتن و تهران را به خطر بیندازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129339" target="_blank">📅 12:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129338">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پزشکیان: حل مسائل مردم مهم‌ترین راهبرد پیشگیری از آسیب‌های اجتماعی است
🔴
شایسته نظام اسلامی نیست که مسائل و مشکلات معیشتی، اجتماعی و درمانی افراد از نگاه مسئولان پنهان بماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129338" target="_blank">📅 12:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129337">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روزنامه‌نگار نیویورک‌تایمز: کانال ۱۴ اسرائیل که بلندگوی رسانه‌ای نتانیاهو است، از زشت‌ترین الفاظ برای ترامپ استفاده می‌کند
🔴
قبلا رویکرد این کانال نسبت به ترامپ چاپلوسانه بود اما با انتشار خبر توافق با ایران همه چیز یک‌شبه دگرگون شد
🔴
این شبکه اکنون، او را «دونالد حسین ترامپ» می‌نامد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129337" target="_blank">📅 12:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129336">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDIveYqByus2Tlzds056rTbdn6ec2ArMRGVoVFPYwt2bxM18FAT6fytIZbgvi8cOim2F8RsZBPzAG5L4uBzAeqQ52cwi_irHFwcI65D9YvlVoNXSW8bK0fsa2HcpEzoLJ61daV66mWsR5uuT00z1gMKJDyqB8qwVPdA1waxPm3qyCLEpDxfpvIie0XEYvGdLuUHa3YgD9YbUVfJW2sg6h6lT0h-9Kf79ydnqozXPwlriSwBuLAh4WhLKugYszdhp6Q_jtKBfAU5YknPH5qtpMmLUbzxHnu0hT4U_dktC_QtzpgD1fyYU3NqDcxWkojq16264Yp5dDhWPCwu1yricvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور پاکستان وارد مشهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129336" target="_blank">📅 12:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129335">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
اینترنشنال: دانش آموزا قیام کردن
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129335" target="_blank">📅 12:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129334">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1e6e4d20.mp4?token=Q7_fwmF-i4bnF-s4OFPZvPtx_vI0dHai54Jyekn-aXOvYe_dDxGg6ee6IGv36qbJFgG5DNY-c_WPYUoJzhZAbBxjlJIcaNpttXl12K0qDtqmcpZ7g2Bk--vTLBM_cFNWAdVx6d_5UDGexLVb6nOGPeb5voHzC6aFGOMLkmcxxltKie7Qe9tuxOKm7PHfd1dqmRkYzToM9qWqCoE4BW3IgDrlzzRnFlj-MI-Rwqdkb9Vy5bTcKqWJNlukdxvcHV64lq1jZou0aqRaLp5M1bOWIEyh5ajlxNYUh78l3yA6fZILmIpRFzQr14p3EDd8T4bPGD4aXT5ueip9wBLdnmyW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1e6e4d20.mp4?token=Q7_fwmF-i4bnF-s4OFPZvPtx_vI0dHai54Jyekn-aXOvYe_dDxGg6ee6IGv36qbJFgG5DNY-c_WPYUoJzhZAbBxjlJIcaNpttXl12K0qDtqmcpZ7g2Bk--vTLBM_cFNWAdVx6d_5UDGexLVb6nOGPeb5voHzC6aFGOMLkmcxxltKie7Qe9tuxOKm7PHfd1dqmRkYzToM9qWqCoE4BW3IgDrlzzRnFlj-MI-Rwqdkb9Vy5bTcKqWJNlukdxvcHV64lq1jZou0aqRaLp5M1bOWIEyh5ajlxNYUh78l3yA6fZILmIpRFzQr14p3EDd8T4bPGD4aXT5ueip9wBLdnmyW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع دانش آموزان شیراز در اعتراض به برنامه فشرده امتحانات نهایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129334" target="_blank">📅 12:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129333">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
تصویری از تجمع دانش‌آموزان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129333" target="_blank">📅 12:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129328">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
یکی نوشته بود بجای کافه رفتن خب درس میخوندید
نظرتون؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129328" target="_blank">📅 12:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129327">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkv3fle2YsAK3aKpG34H_-Xl5Klgqoj8auhWUFa32TlasH1oI294rnAhhOPghGo6_5OriyYCWKoH5-cUkMe2koO_YHH_EF07KVQr-GnRDbRB0VVr3NX8fYY0xTQqYy_01T9JBP4V7sSBLUvnCOgZXee52dyRpdCyZvD1GFYpW6gJm3Y18Z2tpRNm4jX1bbkPld0Mk2U5qupQjualYk70Rx3IE5lWUFL70BoKHcsS7JGVCWcUl-XxAuR4IpNIg3-AVZZlTVhS6c6U_LmOW5UcJnVhsHb3jeqBkdTX2MajobVuMeaMJWXxULGtcMY4ng4GIuB4Hx8DnT3HxPU8WmZ1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تجمع دانش‌آموزان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129327" target="_blank">📅 12:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129322">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eda31ed24.mp4?token=ChXRtaGfeztSQp_ynrKNmjlpvy-KHNX9Ue8OBGnhtdxCivlqWv8GBZWzDkTpYXqWYPXVNpiEV0z5GPJ3pPmhZzYfI_tfHaDy_0AFHMfbiS4gZ-dfDHAzxrcGl-ZHy3cBLnhvWmheMHr4_eFHdkYeYIORduSR2FLzX97NGDkxVOM3HS8aXjLHUOWwmvsl1dpfsWZZFGElRknbp5BPukFvC_Hy0cnVQgkhBHVs9rxjSs2ySq9ouAT_APVlzd0s7RH6Yvumw3VHkG9EupjhmPiNJJQ9v65vYGpJc2aFDG40_wfs-CMI4py6E1IgBix0RMI-etXP3Z-k9Jpup51GL5syKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eda31ed24.mp4?token=ChXRtaGfeztSQp_ynrKNmjlpvy-KHNX9Ue8OBGnhtdxCivlqWv8GBZWzDkTpYXqWYPXVNpiEV0z5GPJ3pPmhZzYfI_tfHaDy_0AFHMfbiS4gZ-dfDHAzxrcGl-ZHy3cBLnhvWmheMHr4_eFHdkYeYIORduSR2FLzX97NGDkxVOM3HS8aXjLHUOWwmvsl1dpfsWZZFGElRknbp5BPukFvC_Hy0cnVQgkhBHVs9rxjSs2ySq9ouAT_APVlzd0s7RH6Yvumw3VHkG9EupjhmPiNJJQ9v65vYGpJc2aFDG40_wfs-CMI4py6E1IgBix0RMI-etXP3Z-k9Jpup51GL5syKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از تجمع دانش آموزان یازدهمی و دوازدهمی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129322" target="_blank">📅 12:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129321">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری / خبرنگار الحدث: یک هیئت عالیرتبه آمریکایی وارد سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129321" target="_blank">📅 12:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129313">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfVB47IwuMV1jayjOQQ_aUpIfP1hCLH2HK08tlSlbbpfTe-7taB5c02MmqRrSGnfqsBqxapDqaVcOWSNYqM1I3EwbgIsgTICvwuLNPOqL-samN8e_L947urCw3MVCpi2WnUSTE0R2g6pamgAegBbYzs5uI7yi9a1W59Vc3mW3avw_BrWik8-TVeF0sMf1FXZJ9kYBlN4ugjwSvp3eVJPUeSHJfeUsEXXc4-BjpvtswdCr9p1XamRV5-qgdd1jqRGAW2zARedjqEqiGM327ZeBAYLdGixeMWYmoLtkY1_JfN_EBzsGLwxCmfCGqxi6tLqhfkhP9Nk8n_ZZvIKywENWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9eE3GW1yxVb4XvG3Txl6alfTHZncndfX9JkTpUQOWlP_Gi74O4b6UyzXQMlr78v4rcNNKMjvtnmhFzPtn8K9wguVmTG6UdtOfwl0Kc6vu4_JLlvOLwUQWkscwaV7g5ZIYJw9v4UGjPl-yGsr8mE1jK9crknZPSTcngHW8FIqRNuFTJJJ3Uo8S02Mh3kFwuNxfyq2I5hshu-N5hCob-T9aBPKl6v4hqcMLRjCSrLI-z-ZK4l8SLFzoV_h_KfIRihmoxqmNQc2HVBCVonYGYtTLtCncQhO9eBs4T7SxJOEq0_paX4hgknKxBxyxN69nA9kEuXXhjFUCRS-oh4otSEgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXbtGNy8MdI1yqslD3LvjR0GW-pXM0aTBvUjv0QNEufqnKvy-xKZ73lBHOCW9SzGiazOiFIxWG6NLiAuGmUJxh4cMtOSLPi4mOxtY7PPHNeltSFY0GqquBYJ1LaJjCYqipYWOkxQn2IHeAz6C6OyiCeZPXK5VuFUK_DEW9Jvv7zoaAlcIBYCP4GUG-KzvTws6zYhzYk6NZmt9YXoVfw2C0-Y7DGnAbhV-QZmDTLVYN_1J-VSG_ApHz7DO-VBk5giqPcsjVuZsv-g7_VQYbDNJGuLawzue3UWO9oH1hK2SmPfVCbTBnlbWptBY2k8cDIcM3I7TcPrMiS5JaOLblKNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwVhuQGK7gjvaeuKiRuNevW0pKGM5Z3gB5BDkOLp5x0GkJbbuGrvjZEk5R2Sfn0I_v7pVJ9ALesN3wV4PDXiB1fdzXmpsf73n1cY_PwToQPeO0Fv4T-KIbLdPiFsR0CgA-7Dk_rH7DV-o7PdeGnnUQjYZ2GVvaI2y20Fzrn1bVx-DD3CaQms1a40HVuDelArSAbfhluNAEL8MO1HqaL_Vkg6Y0UYLpdl0HDfu9wEN8tekbQCXMUZsd1ij5WUrUubQfB5xffXx-QsKllkKDa7KJdUgVkBCGp4A7yyIjI3orSV1Vs5AsElhuD_b0C9vFXxlHvFsN91yRJRQDCmsOPawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdB6jrq9Edgts78om8PAhRuK7-ksWj0fiOmWzfPw0UMjigW7LTtrEb65gqrAac7Hdmpsd1jEy0PxkowLwSghSQEjPAADXTWs6yNgzpdWXPmuN19DbvevmlisUitqznjP20seCvLFtROgFF6fxXbjsiXLGnpwNfIy8SgqNa4TTSQkf_0f3pWfIMqQDK01DHZfr44mavqg6WXBfzeNlck8RXcU9pqPqSSYi1DxwvAE8tmATocgRi7I5nQNY3ShQR_51i_wY7HO4K9vwFhOQzDZMO5a4rvor-BQi-xp1tTuBqkKmG2r4-6JVdjE9BfjzyN4ArSdjoEboMRrEvYB5zhR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qps92g1emyNn7afrrO-PJpTljdGzQRQLPJtDlqQXzxRG_SPhsx1svpO35nMVbG9Vxah7fSAopADzV5rM4QBblS1fgbsZIdG_QBRLZ0U8L29Yq3fJQ4n8r0d31gfcPjfdk45-wPplRD1rx73sCaxwy6KdSKWR0fWDdN63gH5KNwKZJEJVIZ6NKTd-4YH207wkrxsY1dZN6gxvKMoiqrzChRSq3Q3Mhev96H-MhOXrIRTN_jQGIjBZ7GT_HYIQGo4V5zmZP5lvJ6J6KULIGjH8c5JfonHhpYUe9JFhHlPFr72j--WCwJL1IpUshiImVqXctt2VjKu3j8bypaUvGd2plQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJBUL9kVGUmXnFkdr1MkjpKAB9g4BrBbezPnXMfKbuzRsakSOBRqRwibOUi8lxpRmWoRk0NLnXphssJrxj9PPA6wznLSwQVtFNhYu8cKKaDcZmXV4dpWrVcrdnvy14qlouCaipgThMKwH2pB7VsP5MiPWyoba2mZ8jUNveuQ8dOaF1jmtcEX0EK4huLJiEs8xIt5T_134Le9jN93M0m_Tv8ryinf7ow0OsVHE0SE__KJDmAZhe-bqyyUZqYJHBuNdAitW-P7MJZNvxAMBhk3RsbRoHe3w-CsAAYIg_ElrN88VHrhPFISXXbdGoqVC3yKu_qxc--e9SfU_dYhXS2w5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1368546d7.mp4?token=aj2MMYtxGoy6Rl0aBNUQ7SHIz4z2ny6kCqA7a9o0f3cFSrehpdfpjQPyeSkX1Y-aJXmC28G6IUEm6zQQ8b4B3BjFi-8Mk-6LLW5KmSdqdFYvKtZnFXXfCImV3mdN3hKHHqdkJn5TMzpovzcGQU_sGXgrQyZrjZi27Z0q8CLeA_2l27B6lJNkSLGpS8G0y4wu1REAauYD3mlS0s2AGLKlh63j2Z2d5PygfAHW9LY7oSXY40ZyPdhd3v_Fjutchh0WSOAsS0-e0XQ5ligSwaJXdBtS62TpvyqaVgryjMiHQrRcWYoMdUoyQO9GhY19vGA4tgYsfSRCqON9Wx7WoFjviA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1368546d7.mp4?token=aj2MMYtxGoy6Rl0aBNUQ7SHIz4z2ny6kCqA7a9o0f3cFSrehpdfpjQPyeSkX1Y-aJXmC28G6IUEm6zQQ8b4B3BjFi-8Mk-6LLW5KmSdqdFYvKtZnFXXfCImV3mdN3hKHHqdkJn5TMzpovzcGQU_sGXgrQyZrjZi27Z0q8CLeA_2l27B6lJNkSLGpS8G0y4wu1REAauYD3mlS0s2AGLKlh63j2Z2d5PygfAHW9LY7oSXY40ZyPdhd3v_Fjutchh0WSOAsS0-e0XQ5ligSwaJXdBtS62TpvyqaVgryjMiHQrRcWYoMdUoyQO9GhY19vGA4tgYsfSRCqON9Wx7WoFjviA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل بیش از
۱۰۰
هدف، تو جنوب لُبنان رو زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129313" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129312">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3530192cd5.mp4?token=DGMc-14CBlhD27qxupdN3frWJhO86ksB-DyuTBIwjI3T5XNVres-_XHJESgbiGw4v6oYafK-rWZp8pVF5fSeyM9tUi6cOfobFCEA70oQlGi7DStvrfZRI8p8UJIgoy57M_o3yuB6jIZPSvmp8r206QfmDN1pmlGGKNGLWGJ2jrWPLIH7VkMDXM31vOvdzBG0v8kReOOxddtxFgjclL-dKA5CdRhhl-r4XU4jtMBhjghtxvUZ1NEaF_fSz9C2WymxNxxh-55sDMiPK2dw3aVO8-w06fbe_azf1Y6SzM3PmD4qI2OFJcISDUOz4jp_Mljk2IXH764H-xomr6Z1rZbdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3530192cd5.mp4?token=DGMc-14CBlhD27qxupdN3frWJhO86ksB-DyuTBIwjI3T5XNVres-_XHJESgbiGw4v6oYafK-rWZp8pVF5fSeyM9tUi6cOfobFCEA70oQlGi7DStvrfZRI8p8UJIgoy57M_o3yuB6jIZPSvmp8r206QfmDN1pmlGGKNGLWGJ2jrWPLIH7VkMDXM31vOvdzBG0v8kReOOxddtxFgjclL-dKA5CdRhhl-r4XU4jtMBhjghtxvUZ1NEaF_fSz9C2WymxNxxh-55sDMiPK2dw3aVO8-w06fbe_azf1Y6SzM3PmD4qI2OFJcISDUOz4jp_Mljk2IXH764H-xomr6Z1rZbdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به شهر نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129312" target="_blank">📅 11:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129311">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t22f3z0sqnV4EcTNg_pr9xuQUMB-iB-BLaT0xFeVNnyq4Du3g0zK-gl1ql1aRpZUha43hT-m_ZdwaXAwfI3IARSgmoDX0ZrTcRqK5F3-WqeP-gJaRkOHOGifWGp7UakdSERrfg7kPayVEnscmpEHB7OoZxOTbcTOo0vuwFTGdsKuexUDrHg5gFccobXCgtcycBIjWBEB7uBQ9nQ0CWH3QrUMEv2aTcaKjYma4CWXZaRYpX3_k1hWU9ULuKnXQ-thUURSiliFpeCsz2avv7ZJPUkE2SC2eogZh-gSsiRaLLjBlaIWNNK949Uzbr8YHJq6KXMfbGqQswuFzOIWXVZPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با افزایش ۱۸ برابری حجم آب دریاچه ارومیه، آرتمیا دوباره شکوفا شده و فلامینگوها بار دیگر به این زیست‌بوم بازگشته‌اند
🔴
پیش‌بینی می‌شود امسال بیش از ۶ هزار فلامینگو در دریاچه ارومیه و تالاب‌های اطراف آن فرود بیایند؛ برخی از آنها حتی آشیانه‌سازی و جوجه‌آوری را آغاز کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129311" target="_blank">📅 11:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLO0cb7lmLyhF_PqpYBt13p1hKECMEaiCQi7-MQifADicekud7VziGug2W8lM-knbzvt4Sidv4cYxi6Jht2XKFvUfsDMHWRInCZJpupYw5BxdT1ijZVcCGsB33w6Os4pFeEks6J-AYIhb5GRtZevVIH7RXxDog9KiBalNncnd_lV0_S-IMIrOx7kLV8e5UVYMt6YpxKnK4SzJ9jeT3YNC4_uJ1AjNWQdJ3Y1_gNVmQGyRYIr-SFZ0Z395Op60wP4igxgsMmlOzC5LgR-uwnIfxt_9PPMdynKLO1T3cCbao1KWK3UvLmot66yPixY95hte0OIlb-qTGhEov_kLzUXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
قدرت داره از غرب به شرق منتقل میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129310" target="_blank">📅 11:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129309">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
جک کین، مقام سابق نظامی آمریکا:
احتمالا در نهایت با ایران به توافقی دست پیدا نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129309" target="_blank">📅 11:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129308">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">محرم امسال یه فرق بزرگ داره
امسال حدود ۴۰هزار زینب داریم که داغدار قتل عزیزش است
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129308" target="_blank">📅 11:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129307">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دولت عراق به‌طور رسمی مجوز فعالیت استارلینک را صادر کرد تا سرویس اینترنت ماهواره‌ای اسپیس‌ایکس بتواند خدمات خود را در این کشور ارائه دهد
🔴
مقام‌های عراقی این تصمیم را گامی مهم برای توسعه زیرساخت دیجیتال، گسترش اینترنت پرسرعت و پوشش مناطق محروم و دورافتاده عنوان کرده‌اند؛ مناطقی که هنوز دسترسی مناسبی به شبکه‌های ثابت و فیبر نوری ندارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129307" target="_blank">📅 11:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129305">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نتانیاهو: ما در حال محکم‌تر کردن در دست گرفتن حماس در غزه هستیم، جایی که بیش از ۶۰ درصد از قلمرو نوار را در اختیار داریم.
🔴
و در لبنان، ما تهدید یک تهاجم زمینی علیه جوامع ما را پس زدیم و توان موشکی حزب‌الله را شکستیم.
🔴
هنوز کار بیشتری برای انجام دادن در هر دو مکان وجود دارد.
🔴
ما باید منافع امنیتی خود را به قاطعیت حفظ کنیم در حالی که ارتباط مهم با دوستان آمریکایی خود را نیز حفظ می‌کنیم.
🔴
ما ادامه خواهیم داد تا مسیر خود را با خرد و قضاوت سالم طی کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129305" target="_blank">📅 11:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129303">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4e4cf8f9.mp4?token=QWLZiud_0tkv8rkTpaOtlUEp0fe9SsbBsOQ4xAyWydLyVuHgpjzfDRHbyi4UarL8FpGqAMMmCC1EORQPkXLoGVpeRev3o7JvfYFiAJYzTWLNQRo-8CZei-9NGoBOBcB0fCKSaFHllveSMcRqG1Ho7IlI1xDHz1GdA1KyI2DB40B6X9Im2LPEJ1zrqW2dou8GvD0kN-TvXBbLj5Qzt91nZfWePr_W43smhF2B47hGPIKO5qLFtqg7tV43Pk0FuobW13Kya0o3_8dIrYm1oAT7l_kl2TMCk-WFPxZ0UnZyVyeNJIKnaV9j1FX32QwKGxpXR13HBu4f2d028t9t1F98oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4e4cf8f9.mp4?token=QWLZiud_0tkv8rkTpaOtlUEp0fe9SsbBsOQ4xAyWydLyVuHgpjzfDRHbyi4UarL8FpGqAMMmCC1EORQPkXLoGVpeRev3o7JvfYFiAJYzTWLNQRo-8CZei-9NGoBOBcB0fCKSaFHllveSMcRqG1Ho7IlI1xDHz1GdA1KyI2DB40B6X9Im2LPEJ1zrqW2dou8GvD0kN-TvXBbLj5Qzt91nZfWePr_W43smhF2B47hGPIKO5qLFtqg7tV43Pk0FuobW13Kya0o3_8dIrYm1oAT7l_kl2TMCk-WFPxZ0UnZyVyeNJIKnaV9j1FX32QwKGxpXR13HBu4f2d028t9t1F98oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: مسیر ما هزاران سال پیش آغاز شد و با کمک خداوند تا ابد ادامه خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129303" target="_blank">📅 11:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129302">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67043be620.mp4?token=OCc1YKvmDk8ETxWir-nFMsXSagSztn_uBtEM13RbJB85MyBIPllk4lZKrkJmTpxERH89qMs2PcXyHE2HB5jBcge8yVNsLIBJ4xnHbhHtvuKL7SF66n5db1d8I2ZkBzXLE5lyq3QWf30P8_ekS2Mnhq9euyRoffN3DTRNWBpnaueYe0T_IhxB_x9KPyx2YOLOg2uPBG_XtkioY7u3L1GGQjJkLa0igQ1PtQ01ZsRH9m1fTFDX1GesQAvMRKzGMBzkapFepSFAE5_qXereFx2hDzbpNTHzDoFh2F_Kb0uColG95Etk8-o_JnxrHN52A3az6rwzd8PHPx0_Arwx1Latc1mKwhSn0Zd74RRGuxqlOGTw_2oJj8VvlvMNtqHqnQQQsSAjCffyl7JLNozElddYDYuV2nO8qRtohOcJ_u7A9RA4DZuFUdVupBT7Nf3INTArA75xkrhWVsxqyUhXD4OQttI0FocmwAtA5w5iI4Tu8HoqOiiUz8Fm0rhsyWBb5JzWBmIlQw9he9YrMYmTtbC2fjyEjVO4Bm_iDu-ndTyxUlvPqtVC6ceAsCMNWeKQcmj71omDpjActb5Uf0kS7QaTHEG2Ua52dDZc1BJAVhPh8BmIlx7YsFXByqqTRGnD4VqM1qghpNHFlBtas4hpNscjlSPUpgE7QhT9UKhu-QOnP2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67043be620.mp4?token=OCc1YKvmDk8ETxWir-nFMsXSagSztn_uBtEM13RbJB85MyBIPllk4lZKrkJmTpxERH89qMs2PcXyHE2HB5jBcge8yVNsLIBJ4xnHbhHtvuKL7SF66n5db1d8I2ZkBzXLE5lyq3QWf30P8_ekS2Mnhq9euyRoffN3DTRNWBpnaueYe0T_IhxB_x9KPyx2YOLOg2uPBG_XtkioY7u3L1GGQjJkLa0igQ1PtQ01ZsRH9m1fTFDX1GesQAvMRKzGMBzkapFepSFAE5_qXereFx2hDzbpNTHzDoFh2F_Kb0uColG95Etk8-o_JnxrHN52A3az6rwzd8PHPx0_Arwx1Latc1mKwhSn0Zd74RRGuxqlOGTw_2oJj8VvlvMNtqHqnQQQsSAjCffyl7JLNozElddYDYuV2nO8qRtohOcJ_u7A9RA4DZuFUdVupBT7Nf3INTArA75xkrhWVsxqyUhXD4OQttI0FocmwAtA5w5iI4Tu8HoqOiiUz8Fm0rhsyWBb5JzWBmIlQw9he9YrMYmTtbC2fjyEjVO4Bm_iDu-ndTyxUlvPqtVC6ceAsCMNWeKQcmj71omDpjActb5Uf0kS7QaTHEG2Ua52dDZc1BJAVhPh8BmIlx7YsFXByqqTRGnD4VqM1qghpNHFlBtas4hpNscjlSPUpgE7QhT9UKhu-QOnP2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: مردم اسرائیل به خانه بازگشته‌اند و مردم اسرائیل برای همیشه در اینجا خواهند ماند.
🔴
زیرا این سرزمین ماست. متعلق به ماست.
🔴
ما بازگشته‌ایم، به جایی که از آن آمده‌ایم بازگشته‌ایم، به مسیری که پدران ما در آن گام برداشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129302" target="_blank">📅 10:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129301">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرگزاری دولت: وزیر کشور پاکستان برای دیدار با مسئولان بلند پایه ایرانی، عازم‌ تهران شد
🔴
او در این سفر «پیش‌برد مذاکرات» را پیگیری خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129301" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129300">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رئیس‌جمهور ازبکستان خطاب به پزشکیان: یادداشت تفاهم امضا شده، نمادی روشن از اراده برای تعامل سازنده و احترام متقابل است
🔴
این گام مهم موجب کاهش تشنج در منطقه، ایجاد زیر بنای پیشرفت و گسترش همکاری‌های اقتصادی و بازرگانی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129300" target="_blank">📅 10:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129299">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d84fa59c.mp4?token=i8oEzKRhLvcZE5GhWKYj42p1QsHar69OULAhN-mWy23ALABTNtXaFLkyyKp5ExsbVnNTQ9Y4NpFtaEsvppHcNN1CmHlgEZDfAxfLK22roamgdvUMLxNS86KGoyrmcNtmDyIhegxmOYaHQ3OERiot_4JxmMUBsCO1FXZzeyjDRT_vqbg8E4C-TuxkKt3sMQ3MRytHm5qSRXTO-t-imrQY49Cb44VYVe_tToQUEC9pPjxLcr-du1tKXzGbvIdHAOnOpXapq3YLocT-W5FenIMD559Qym472z-aox0xSd3uYKuzPv0w5KKA3ulXrjzpQ6u-Fviv9wcOc-bQ3L9fIsybdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d84fa59c.mp4?token=i8oEzKRhLvcZE5GhWKYj42p1QsHar69OULAhN-mWy23ALABTNtXaFLkyyKp5ExsbVnNTQ9Y4NpFtaEsvppHcNN1CmHlgEZDfAxfLK22roamgdvUMLxNS86KGoyrmcNtmDyIhegxmOYaHQ3OERiot_4JxmMUBsCO1FXZzeyjDRT_vqbg8E4C-TuxkKt3sMQ3MRytHm5qSRXTO-t-imrQY49Cb44VYVe_tToQUEC9pPjxLcr-du1tKXzGbvIdHAOnOpXapq3YLocT-W5FenIMD559Qym472z-aox0xSd3uYKuzPv0w5KKA3ulXrjzpQ6u-Fviv9wcOc-bQ3L9fIsybdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: در سیستم‌های پاکستان و قطر، آن‌ها دقیقاً دارای اصلاحیه اول و آزادی مطبوعات نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129299" target="_blank">📅 10:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129298">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر کشور پاکستان عازم تهران شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129298" target="_blank">📅 10:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129297">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سخنگوی دولت: تفاهم در این مرحله، هنر تبدیل جنگ سخت به نبرد سیاسی و راهبری چالش‌های سخت با مدیریت عقلانی منافع است
🔴
هرجا باب گفت‌وگو گشوده شده، امکان یافتن راه‌حل نیز فراهم آمده
🔴
تفاهم به معنای پایان مسیر نیست؛ بلکه آغاز مرحله‌ای تازه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129297" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129296">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: اوباما تمام پول ما را به مردم بخشید. او صدها میلیارد دلار به ایران بخشید.
🔴
من پولی به ایران نمی‌دهم. من به ایران پولی نمی‌دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/129296" target="_blank">📅 10:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129295">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72466c840.mp4?token=qKb3QsQZqCyL768FKZA3tFedv8g0946RD7fJaxKp4sXa8Q6g9-OuxA8oW6L2WjYm-PwCjTawbeotx1GhlCUsIBXEuVJ9JrcBwlObR1PBJCr3yP_mybdKZ94QpF7rH_6yvpljGU_Z4afy31PtZLHVGYdd2S3tbiGHdFgOGA-JwfzvlH_ZF_vCoWp8L4SDSOYqJTRkwnD2yntsxAzmz1WvwPT3qFPGSQRTEopToLUiFq5q8CVXZGmfgwkzXU7vZC6wYw3gWhne75JikyTwigiF-wUF-Q0-U1Ma2VVwtkilkB4qvzlKBpbcFXz45gEP_hYhDuwri1yOw07nneLHUwklrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72466c840.mp4?token=qKb3QsQZqCyL768FKZA3tFedv8g0946RD7fJaxKp4sXa8Q6g9-OuxA8oW6L2WjYm-PwCjTawbeotx1GhlCUsIBXEuVJ9JrcBwlObR1PBJCr3yP_mybdKZ94QpF7rH_6yvpljGU_Z4afy31PtZLHVGYdd2S3tbiGHdFgOGA-JwfzvlH_ZF_vCoWp8L4SDSOYqJTRkwnD2yntsxAzmz1WvwPT3qFPGSQRTEopToLUiFq5q8CVXZGmfgwkzXU7vZC6wYw3gWhne75JikyTwigiF-wUF-Q0-U1Ma2VVwtkilkB4qvzlKBpbcFXz45gEP_hYhDuwri1yOw07nneLHUwklrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کشتن قاسم سلیمانی: می‌دانید سلیمانی قصد چه کاری را داشت؟ او می‌خواست پنج پایگاه نظامی ما را منفجر کند.
🔴
من او را یک هفته قبل از آن حمله به دست آوردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129295" target="_blank">📅 10:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129294">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20faee2d60.mp4?token=pgrrN3gg8HiTa9U6Y3725ER99rNHRyGnKeamhbYmtj5DIxm4JnKUvxYfIoGA1bVMZ13eX7IUsBLrnYhxKOXJjow6i9oMzjgFNHFOsJl16oDlWWVzPSisHdUZW7MlfRk5iRDGA4omiRGX09mg5ni8UPD4-8rXKeyhF7LlJxmw5V5qyHMpbyXsBSfuS0FkCvXAaqs6J8sPC8TIztgIH5vxu54XSULRtmKjPB7T6sBVBq7xxFhSwvflW-_kT3wvyj5WwWR7ImPcHluTqNuGjngAg_DlfpJxzMJvGja7pcaL4HhiELodNVA9MzNuTWC7oDMra5QkvDoPQe3AzBxvvSwpIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20faee2d60.mp4?token=pgrrN3gg8HiTa9U6Y3725ER99rNHRyGnKeamhbYmtj5DIxm4JnKUvxYfIoGA1bVMZ13eX7IUsBLrnYhxKOXJjow6i9oMzjgFNHFOsJl16oDlWWVzPSisHdUZW7MlfRk5iRDGA4omiRGX09mg5ni8UPD4-8rXKeyhF7LlJxmw5V5qyHMpbyXsBSfuS0FkCvXAaqs6J8sPC8TIztgIH5vxu54XSULRtmKjPB7T6sBVBq7xxFhSwvflW-_kT3wvyj5WwWR7ImPcHluTqNuGjngAg_DlfpJxzMJvGja7pcaL4HhiELodNVA9MzNuTWC7oDMra5QkvDoPQe3AzBxvvSwpIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد کشتن قاسم سلیمانی: کشتن سلیمانی یکی از بزرگترین لحظات در تاریخ خاورمیانه بود، زیرا او ترسناک‌ترین مرد در ۱۰۰ سال گذشته بود.
🔴
حتی آیت‌الله‌ها از سلیمانی می‌ترسیدند. آن‌ها همگی از سلیمانی می‌ترسیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129294" target="_blank">📅 10:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129293">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfaa82c92.mp4?token=tLL-bM1UBDo5V_DzIGLNFe7xW9Neg6cB8iORMrX7JuXIJEN6KaeoOLPGXV4Xsb7M9q1qU9OqWWbv2eDgvw6MuuRpmZGJE1ExpT7BZGIN4hLUMFMbSCM2b5aUNPr5PFxN7N155FtBRBQUaRSXVKS4XAopS4gIRi0qTvAXVTY5ZON1fgV_w92zQH-yGnVtiQzzF2Os2Uo2s_Q-cU65whSM485XSCMFbFEOME1jvGX5Evjik1CNbhHu2bRL8grIYAM3qNWsUE8Z8svAb3nABDHQbWhSxYYPrEW5ymXbl_T-IhNDs33ZIhczKzucozCEfsvC5F6ki537nmw1sYaeR2I9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfaa82c92.mp4?token=tLL-bM1UBDo5V_DzIGLNFe7xW9Neg6cB8iORMrX7JuXIJEN6KaeoOLPGXV4Xsb7M9q1qU9OqWWbv2eDgvw6MuuRpmZGJE1ExpT7BZGIN4hLUMFMbSCM2b5aUNPr5PFxN7N155FtBRBQUaRSXVKS4XAopS4gIRi0qTvAXVTY5ZON1fgV_w92zQH-yGnVtiQzzF2Os2Uo2s_Q-cU65whSM485XSCMFbFEOME1jvGX5Evjik1CNbhHu2bRL8grIYAM3qNWsUE8Z8svAb3nABDHQbWhSxYYPrEW5ymXbl_T-IhNDs33ZIhczKzucozCEfsvC5F6ki537nmw1sYaeR2I9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره قاسم سلیمانی: وقتی سربازانی را می‌بینید که بدون پا، بدون دست و با چهره‌ای نابود شده راه می‌روند، ۹۶.۲ درصد آن‌ها از ایران آمده‌اند.
🔴
از سوی سلیمانی بود. این سلاح مورد علاقه او بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129293" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129292">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
الجزیره: ۴ حمله جدید اسرائیل به جنوب لبنان
🔴
۴ حمله هوایی به شهر النبطیه و شهرک النبطیه الفوقا در جنوب لبنان صورت گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129292" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129291">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ در مورد جنگ اوکراین: وقتی جنگ اوکراین شروع شد، پوتین صدها تانک داشت که در حال حرکت به سمت یک بزرگراه بودند. یک بزرگراه بتنی، بسیار خوب، محکم مثل سنگ، درست به سمت کی‌یف.
🔴
او می‌توانست در سه ساعت آنجا باشد، با سرعت ۵۱ مایل در ساعت که حدود حداکثر سرعت برای یک تانک است. آن خط بزرگ تانک‌ها را به یاد دارید؟
🔴
و آن‌ها ژنرالی داشتند که احتمالاً دیگر در میان ما نیست. او تصمیم گرفت به جای رفتن مستقیم به سمت کی‌یف و پایان دادن به جنگ در روز اول، از طریق زمین‌های کشاورزی و از میان گل و لای عبور کند.
🔴
و چند روز قبل طوفان بارانی بی‌سابقه‌ای رخ داده بود و آن تانک‌ها در آن گل گیر کردند.
🔴
و من به آن‌ها جاویلین‌ها دادم و آن‌ها تانک‌ها را نابود کردند. من این را قبل از وقوع این اتفاق گفتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129291" target="_blank">📅 10:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129290">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap5YModTkdlTP2_iPtmxEST0QHF9JEGWTZdAgqNwuh2ytvH3AUv7eGrzBaGAthcVVN-c-mx3ffI1erjV1l7JaP4bKsf8mHqsNUamTBJQZx9GQvF-54oeZENEshK6ML4xLoyMMdSyqznIQRwYGQ9B9yoEHcrumKt3VYyghGcNjOn-1hoQt5nJ4SRk2ywTjbdKI5cupwKKSYcqJxcPCHSq9a3RcuHtD46jMwUouHc9a7bydmbSNDGPoREred8HvXQUfy5SCBWcEDRlI0SbdMPXThCB02uJTYmoo3j4iIT5dOWRgwgwi_BGX9C1_uRLhOktOWm3OX1X6CQkR3ByYObKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر یادداشت جدید نشریه فارن افرز:
«ایران در جنگ پیروز شد اما ممکن است صلح را ببازد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129290" target="_blank">📅 09:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129289">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKKXttKRtP2YWrBfcc7g-c2j1dVv1qI5PGXNSQrOKSLrmQqfQAkpKK7JJPDQN0EAThdJJnFIA2_Fp1bqSpDyQlCv6_AAMGtufVM7HZUDllHNw27E8GddEq69RdXa6sGvLryNqdZviSpP-HuyUuj1AN4-cvLhiRo1X9yOJDYD3gy4n4tR2K18342p9DqIJocP-LATixD6do4NXsSUucd54ujTYj1PJHeU3Zd_VZs0cAayEuZV2RfW5hlm_JDuqnpnENiOsNbpwyWBXq-mYGaMYvvtkSyDbySwMqBAKOL73szwThpTzN6yC_KzoLYE0S__jir2tJy8HB3QGeIwdEZ6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: یک منبع به من تأیید کرد که تاکنون، خط اعتباری که به تهران اجازه دسترسی به دارایی‌های مسدود شده‌اش را می‌دهد، همانطور که در یادداشت تفاهم تصریح شده است، فعال نشده است.
🔴
ایران معتقد است که ادامه دور بعدی مذاکرات ۶۰ روزه مستلزم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ یادداشت تفاهم است.
🔴
تلاش‌های دیپلماتیک از طریق واسطه‌ها همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129289" target="_blank">📅 09:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129288">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
معاریو:توافق میان ایالات متحده و ایران و اظهارات رئیس‌جمهور آمریکا، دونالد ترامپ، از جمله انتقادهای تند او از نخست‌وزیر بنیامین نتانیاهو و درخواست آمریکا برای خروج از جنوب لبنان، نگرانی‌های جدی‌ای را در میان افکار عمومی اسرائیل برانگیخته است.
🔴
۶۳ درصد از اسرائیلی‌ها در پی تحولات بین‌المللی اخیر مرتبط با این توافق، نسبت به آینده اسرائیل ابراز نگرانی کرده‌اند.
🔴
این نتایج در نظرسنجی‌ای که روزنامه «معاریو» با همکاری مؤسسه «پانل فور آل» به ریاست دکتر مناحیم لازار انجام داده، به دست آمده است.
🔴
این نظرسنجی همچنین نشان می‌دهد که تنها ۳۱ درصد از اسرائیلی‌ها نسبت به آینده کشور نگران نیستند، در حالی که ۶ درصد دیگر در این باره نظری ندارند.
🔴
تحلیل داده‌ها نشان می‌دهد که اکثریت قاطع، یعنی ۷۸ درصد از رأی‌دهندگان احزاب مخالف، درباره آینده اسرائیل نگران هستند.
این درصد شامل رأی‌دهندگان احزاب عربی نیز می‌شود.
🔴
با اینکه اکثریت اندکی از رأی‌دهندگان احزاب ائتلاف حاکم (۵۱ درصد) احساس نگرانی نمی‌کنند، اما بخش قابل‌توجهی از آنان (۴۴ درصد) از آینده اسرائیل هراس دارند. ۷ درصد دیگر نیز موضع مشخصی ندارند.
🔴
دکتر لازار معتقد است که این داده‌ها نشان‌دهنده نگرانی‌های جدی در میان بخش‌های گسترده‌ای از جامعه درباره آینده کشور در پی عملیات «غرش شیر» و پیامدهای آن است.
🔴
به باور او، این نگرانی‌ها احتمالاً در هفته جاری و پس از انتشار چهارده بند توافق هسته‌ای میان آمریکا و ایران افزایش یافته است.
🔴
این موضوع در شرایطی مطرح می‌شود که دونالد ترامپ اعلام کرده است ایران حق دارد موشک‌های بالستیک در اختیار داشته باشد. همچنین معادله جدیدی در لبنان شکل گرفته است؛ وضعیتی که در آن این نگرانی وجود دارد که اسرائیل مجبور شود تا مرزهای بین‌المللی عقب‌نشینی کند، توان بازدارندگی‌اش به‌شدت آسیب ببیند و یک معادله جدید در منطقه ایجاد شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129288" target="_blank">📅 09:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129287">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا و قطر در حال برنامه‌ریزی برای آزادسازی 6 میلیارد دلار از دارایی‌های ایران در قطر جهت خرید کالاهای بشردوستانه هستند، این در حالی است که ایران برای توافق نهایی صلح، خواستار آزادسازی 24 میلیارد دلار از اموال بلوکه‌شده خود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129287" target="_blank">📅 09:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129286">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=C1AdepJJuxo38d5vOqj87fhsJW36VmIHFsOPXUZDkIcpA09YCRuYQnjOMbccvcIc5UDAy_k8q5hkhAAZ_q3H7hINp9PGT5rACNADMLCIwV4Iys_2NHFVO49swC5fOdWK9GAE2w7bnDbf2jIX7MxbkjDjx2jdLyuNgGlPGbjm7bauf0R026Uzn_lmxo52r1KCMdvxkE-mrzyab1KfLC8qSJ2PjCb1vcNyDo1r1Bo3J5fzrQ5btexVhuQpe1ZjNNK8RgnrgLN6Twn5DA3aGIft6IueB9sUrRfx3KMkAX9QQQN_YiYi8CJHw79hhqQ6RtiEHlHB8ME06ni0zeApwx63ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bc3683da.mp4?token=C1AdepJJuxo38d5vOqj87fhsJW36VmIHFsOPXUZDkIcpA09YCRuYQnjOMbccvcIc5UDAy_k8q5hkhAAZ_q3H7hINp9PGT5rACNADMLCIwV4Iys_2NHFVO49swC5fOdWK9GAE2w7bnDbf2jIX7MxbkjDjx2jdLyuNgGlPGbjm7bauf0R026Uzn_lmxo52r1KCMdvxkE-mrzyab1KfLC8qSJ2PjCb1vcNyDo1r1Bo3J5fzrQ5btexVhuQpe1ZjNNK8RgnrgLN6Twn5DA3aGIft6IueB9sUrRfx3KMkAX9QQQN_YiYi8CJHw79hhqQ6RtiEHlHB8ME06ni0zeApwx63ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از شب گذشته تا امروز صبح، ارتش اسرائیل حملات پهپادی و موشکی گسترده‌ای در جنوب لبنان انجام دادن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/129286" target="_blank">📅 09:30 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
