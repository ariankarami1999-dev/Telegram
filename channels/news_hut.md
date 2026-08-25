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
<img src="https://cdn4.telesco.pe/file/S0XfLlck0c-D_ZVDr-NWQxq-SraW7gxxAH33KyHt3868vT0HyuMIfigUTxsIJXYFo1CGROLmTF1dN-YrxTBP4CWyxScK0E8UoaqYpB8NRRjY2apw0K_1l8H58eqOl2wbYibbv3r9aaBXPnAwY_KJoaoPDGjeHBmqWjoQbC1NG961TAevw6kiGk73GX54Ll9zOgSSM-GUioYIrfqknuC-9wsqVKzZ9mX2UofpLOtJLy7uRWozpiU2leTDlo50BB2qI9Jr2D1WcCMpgShoKaqudNqi1FP7oYg1lxyyN8RrvJMBGbPqJh7aLs5sEe2Z2afQnzKlYoeIYLPupuBiQbisNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 118K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 22:36:47</div>
<hr>

<div class="tg-post" id="msg-70585">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=EHrELH1e-9bb4h7MNfWdlsEitbw2G6GtKjt1n6JkkkGY_frQrTySEiebfh3LtPUcGgpKtcPZqM1UOkNSvpZD3YCaiM1fJMWbOJYR8ou-9EZLD6pKmgEohDGTFOu8cleZWzjaxdcddc-5aysxWZfm-g2HaevKKJPbGQ25LAm6hM68U5yTa98-fKIGD9IpJY1efn0WmWzgJjLncgSfFcme9TOMHILnERA5YEahWWX3tOf2WDQ8pEl_AB3xJySqJkcEtpoodjyagNA9369Pi7UGDGpik9mEIjZSqRuLjnMPqN9U7S8AWgFeoKiywB0MDRp48u49hcf7uAUlnLXhsheSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=EHrELH1e-9bb4h7MNfWdlsEitbw2G6GtKjt1n6JkkkGY_frQrTySEiebfh3LtPUcGgpKtcPZqM1UOkNSvpZD3YCaiM1fJMWbOJYR8ou-9EZLD6pKmgEohDGTFOu8cleZWzjaxdcddc-5aysxWZfm-g2HaevKKJPbGQ25LAm6hM68U5yTa98-fKIGD9IpJY1efn0WmWzgJjLncgSfFcme9TOMHILnERA5YEahWWX3tOf2WDQ8pEl_AB3xJySqJkcEtpoodjyagNA9369Pi7UGDGpik9mEIjZSqRuLjnMPqN9U7S8AWgFeoKiywB0MDRp48u49hcf7uAUlnLXhsheSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به پالایشگاه نفت آفپسکی در منطقه کراسنودار روسیه حمله کردند.
در پی این حمله، آتش‌سوزی در پالایشگاه مشاهده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/news_hut/70585" target="_blank">📅 22:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70584">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=gnlMYgw3RRcRWs9SzIULv0Fpc8FVjrlvUpVi62sN4ZYmrxvxXUTvSPLicIEXyv9nZoetrJjmCRpJNAciCTkIExQ6EEV7T9aFuPX-zu6vRDF-b3ZDYzY3d0jkT70_VaFezu5uJlsJVzHOCZ4q12yO9ppUjhaPybni2rV7DMnYW1hOgETllqlQhXIZQYYiGnF-tVlpVT9ZpA7swws9zhVnNAT7qXz-TPq5x0FczmGHMx0NFUWFY_VwLLxLO9wyOFLxMqybktXN6EwK670xLzxeoGDVRonG_rtgJzS0-MU9SBIlL1_StApvFRGMUUbkqdXacZcuo2g3urtEMrEbH-v1IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=gnlMYgw3RRcRWs9SzIULv0Fpc8FVjrlvUpVi62sN4ZYmrxvxXUTvSPLicIEXyv9nZoetrJjmCRpJNAciCTkIExQ6EEV7T9aFuPX-zu6vRDF-b3ZDYzY3d0jkT70_VaFezu5uJlsJVzHOCZ4q12yO9ppUjhaPybni2rV7DMnYW1hOgETllqlQhXIZQYYiGnF-tVlpVT9ZpA7swws9zhVnNAT7qXz-TPq5x0FczmGHMx0NFUWFY_VwLLxLO9wyOFLxMqybktXN6EwK670xLzxeoGDVRonG_rtgJzS0-MU9SBIlL1_StApvFRGMUUbkqdXacZcuo2g3urtEMrEbH-v1IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مستر‌بیست(یوتیوبر معروف) یه چالش خفن اجرا کرده که باید خودش و دوستاش از دست 100 تا نیروی پلیس به مدت 12 ساعت فرار میکردن؛
برای اجرای این چالش ماه‌ها زمان صرف آماده‌سازی تله‌ها، دوربینا و مسیرهای مخفی شد و حتی یک شهر رو به‌صورت کامل اجاره کردن.
خود جیمی (مستر بیست) و دوستاش به مدت چندماه تو یه شهرک نظامی، آموزش‌های نظامی و امدادی دیدن و جالبی این موضوع اینه که مستر بیست برای خودش 50 تا بدل درست کرده بود تا پلیس‌هارو کصخل کنه.
این ویدیو یکی از پرهزینه‌ترین و پرچالش‌ترین ویدئوهای یوتیوب مستر بیست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/news_hut/70584" target="_blank">📅 21:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70583">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=bZrwU0vT6zP2cIj-yJdFZ3tyxC-NuX4-sfXWKMjnWeiBwhWbdBc9gqLQT0ezOsk_dutkpmoM3tPv3bHXHo68EatuFmHxhMe92JoKwliqq-crXB1wJjx6VXRDoQPIf_y0R7-FNz2ijOnkgpbONv3EPGQCr5owfthPqHCwWOw_SAKPNEetxh8Dj-S1N4kJ-g1YNFUVVDT4U6YLmzkn1cRL3P8mZN1i9FcDK_Zl4gT4Ya-dCDqYsgI1rUUXrzIjTjckQnYpmxemETq9GD5vXepXGfuCZCj3wCgclrE-f34XqP8zHq1IQG36yTIfVx0wNM0Bq3OoL1P7RxqJudyVm5KHfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=bZrwU0vT6zP2cIj-yJdFZ3tyxC-NuX4-sfXWKMjnWeiBwhWbdBc9gqLQT0ezOsk_dutkpmoM3tPv3bHXHo68EatuFmHxhMe92JoKwliqq-crXB1wJjx6VXRDoQPIf_y0R7-FNz2ijOnkgpbONv3EPGQCr5owfthPqHCwWOw_SAKPNEetxh8Dj-S1N4kJ-g1YNFUVVDT4U6YLmzkn1cRL3P8mZN1i9FcDK_Zl4gT4Ya-dCDqYsgI1rUUXrzIjTjckQnYpmxemETq9GD5vXepXGfuCZCj3wCgclrE-f34XqP8zHq1IQG36yTIfVx0wNM0Bq3OoL1P7RxqJudyVm5KHfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سوال خبرنگار از شاهنشاه آریامهر:
فکر می‌کنید در کشور شما کدام‌یک تاثیر بیشتری روی زندگی مردم داره؟مذهب یا پادشاهی؟
@News_Hut</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/news_hut/70583" target="_blank">📅 21:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70580">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMVe-Cxo_ELVkxVdXGJnPrruYKHZzh7EehwXE9vdKSI33K3oBGtOmj1m2cd8wQGw8uDcF9HVx7mDTUIWMESEeBuTC-O8t4pKQdSlML6aa5tZ50Nty5ppz_EyJiYVo8Blyv4zoaymwuIMWLJzV8jcKHph38Vp0f2D4otXn-unH-i4Y0X0gh6xIlpjGruQ_bAokqVPjOT2MVLfZ7sfvMiD8kHBMa6AY45Imu4RfFGr6tCygADNxwu15VnT9NyVEZyCkMo78d0oMtQEEh_SaoS411rjD7Z5gqm9ZUEl_IM59rArTwHii5vx0ef6synLHq39n554SdmzfJcnsyuLiZR3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VndmRhUbRQPf7KdVm-Z3J9ar3X_qGD1jooVmgvLiU-RY2SMzMbMAmV1noV59kyKECUJ0_Z5OF0RAwhz_7embX2But3ypb2cEMrKXrPWX0bAsr83i8bV5TlQSzo98qciDkStiwTfeV1hUMxzGeLJTfT4zvlOXFSMmklSYRYV8TACtnYC9zRSU_2YRLsB27JqTzgO2GhXT0YFGt-v1CR2J8PGt1sIm77uYKzivN2ltoZ0KYhHWxBjMJwzf54kWLNL3GNmmki--ICB8memgGWTCfAVqZf-EwGupQGQB1sTybA16h0oCYuRjHJ0xrrPZqC4XXsMqGC8yyqRyF5itz-UwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAbPSAyE6wCIivBPbRIWplB_xdWuKg5M5aEluYX_kIKFla7gdGAV9L_qr_nbTvEiLETVEa4qMCjrIylZsqFNM4t_ezLTqPnM1GuOklr_UmYVe85bmOLkJE-got6UJEhcNQtbWwn-VsfT8-kl-0qsGcXBRernIFVn37wnR9cTxR8AeunpuH5AuV-PFk_enD-t5U_eknPFVhVHEMV2gB435WM4E5-CXWIWrxxkO0gSR99oZ99v-ww70oj2vZnBik9WTUC2BbQeOD9gIbkymasIrRRGOtlTcrlVUJK7YyywQB5pcKhed-VNf_APcW0NVdmjpha-8aQhNzwrRrf1CtY9rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
〰️
🇺🇸
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
🔴
رهبری ایران به واقعیتی اذعان می‌کند که اکنون برای جهانیان آشکار است:
فشارها کارساز واقع شده‌اند.
🇮🇷
مسعود پزشکیان، رئیس‌جمهور ایران، ضمن اذعان به کمبودهای اقتصادی کشور، اظهار داشت: «جنگ باید بالاخره روزی به پایان برسد.»
🇮🇷
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر سخن گفت: «هر چقدر هم که قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و خبری از گردش مالی، رشد اقتصادی و تولید داخلی نباشد، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری همچنان به قطع تمامی شریان‌های حیاتی اقتصادی که این رژیم را سرپا نگه داشته‌اند، ادامه خواهد داد تا زمانی که تهران کاملاً منزوی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/70580" target="_blank">📅 20:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70579">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfomaLXFewvRnBn-L2yNFknKbAmQeRJ0bPWxlEBNkemoF5LUrXO4eHlpYh7rJNsjGRi1oI7dmmr74pc5Nf5Xf9vnS4sTjkcDlR_v5AZF4f52H_7a1gaiQHMdmkHo3s2bortazUNoUefQ45qTzPcGsz0e_IqabPdq-aBEFNvSwq2HPlMHnfn8HRbLW5Ptgk_agzLjGMmAIkdRZf7y3GmkM1-_r0yHbyuTn5pWU8SUz6Vdj9uClvIkHtWrqL5xKNr4_7zN18mNJVEJrOD10yNpfg3nB9ANoWSlPpR90h--K14ypOXeyd-rOoPMmxxwexSUsy5lY6UeFUprOhcyysbZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
اکانت رسمی تلگرام در پلتفرم ایکس :
امروز به کراشت پیام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/70579" target="_blank">📅 20:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=gcoFnAETh1yg3v88XPtQQpLTC5r-fp0PARKw3pvCbYG-KSg40JS1KiDDOTwM1fHJzeG8OSRosEPUq6YYf_SwVvg0tM8BaYwqm_96Cmj4UmxSBPRLnaiaBxyPcBp-Pi3b3mySqNQM27LtIJZt-JHQijQ8XCCgn1XbpWm5HrmTopkg_QEuvOlTWRERH5cGezKN5sVcoS03QnXhB2gRbTJbn9niSsKmmLWmCQxCrde_hsfQTd5bNeZs3uZ5BlDgzpZ_nhZAXvtbpkQ4hLTVcOL-nfMC6Uv6cDQRCXRnxFiRcOcDzyVRxH72YkqGMqnX1A6i--oktLg_g_sMw1EmGHWxFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=gcoFnAETh1yg3v88XPtQQpLTC5r-fp0PARKw3pvCbYG-KSg40JS1KiDDOTwM1fHJzeG8OSRosEPUq6YYf_SwVvg0tM8BaYwqm_96Cmj4UmxSBPRLnaiaBxyPcBp-Pi3b3mySqNQM27LtIJZt-JHQijQ8XCCgn1XbpWm5HrmTopkg_QEuvOlTWRERH5cGezKN5sVcoS03QnXhB2gRbTJbn9niSsKmmLWmCQxCrde_hsfQTd5bNeZs3uZ5BlDgzpZ_nhZAXvtbpkQ4hLTVcOL-nfMC6Uv6cDQRCXRnxFiRcOcDzyVRxH72YkqGMqnX1A6i--oktLg_g_sMw1EmGHWxFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر ۱۶ ساله رونالدو و دوست دختر خوشگلش:
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/70577" target="_blank">📅 19:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=pGVoA35UV8ilqQWzP4pP5b8NkEY8lXtuVByMq3H5YjIR6y4Ip6T7qRaJVazVJ7_IRt3ORyxFTJDToW9n-T29z9Dny1VSz5X4lm_B5jewzaPY5aq2ohaa4VEy-PbOD3YExZMWDkMMewoKkjrS7c1X2qLmm7zvD8zs8MwQFheohAI1DB5P-BonDO0eMaX977dDMGbV-1IOalLGhNA_f73MNiAsFvWwKgrz_ak6qiDrXsIa94Bp03pnIGQmIPkU8qzL5BAwQn2DplOlyZa-gbneMZcDBIsx0jMQxYv4mY6gLfEmvJ3XE6DziNWph0SqcAKpfypokFco6yQzI_dkWduwZhDX0_qhiBgymxijUlGnoy_9OD9A0mglN7cOYTXVtCxSlnmIr3iLAK83xxe-xyECFqi5CSlw1KGwHIZek89G67O4IXwfYVejqW6AgVeSwv14a8cUpvikxRG6rKsaMlbUf4JFloDnsg9kL3m-NPMe4oPWXSaab395HnHe608jzjjEpj1bZeLbZ3b74_Wy4xR-Q3-oKEfTBzTBO_IUFiim-tKcnLMvI8z893p7uoPgEDSajudEmMfoO3qEZr9lNFrVmL42iX5PR0LPBSW7digdpUtwLxzKQ8UEHAy0AP39eUklUDWlCKtVC8m8MSnj-Xv64XSVLgwaWaSvE1p5lnDPk4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=pGVoA35UV8ilqQWzP4pP5b8NkEY8lXtuVByMq3H5YjIR6y4Ip6T7qRaJVazVJ7_IRt3ORyxFTJDToW9n-T29z9Dny1VSz5X4lm_B5jewzaPY5aq2ohaa4VEy-PbOD3YExZMWDkMMewoKkjrS7c1X2qLmm7zvD8zs8MwQFheohAI1DB5P-BonDO0eMaX977dDMGbV-1IOalLGhNA_f73MNiAsFvWwKgrz_ak6qiDrXsIa94Bp03pnIGQmIPkU8qzL5BAwQn2DplOlyZa-gbneMZcDBIsx0jMQxYv4mY6gLfEmvJ3XE6DziNWph0SqcAKpfypokFco6yQzI_dkWduwZhDX0_qhiBgymxijUlGnoy_9OD9A0mglN7cOYTXVtCxSlnmIr3iLAK83xxe-xyECFqi5CSlw1KGwHIZek89G67O4IXwfYVejqW6AgVeSwv14a8cUpvikxRG6rKsaMlbUf4JFloDnsg9kL3m-NPMe4oPWXSaab395HnHe608jzjjEpj1bZeLbZ3b74_Wy4xR-Q3-oKEfTBzTBO_IUFiim-tKcnLMvI8z893p7uoPgEDSajudEmMfoO3qEZr9lNFrVmL42iX5PR0LPBSW7digdpUtwLxzKQ8UEHAy0AP39eUklUDWlCKtVC8m8MSnj-Xv64XSVLgwaWaSvE1p5lnDPk4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صادق خرازی:
به آمریکا در افغانستان کمک کردم و حتی فرودگاه در اختیارشان گذاشتیم اما جرج بوش ایران را محور شرارت نامید!
بیشترین خدمات را به آمریکایی ها دادیم و حتی خون دادیم
این نشان میدهد یک جایی در پشت پرده محاسبات دو کشور نمیخواهد رابطه ایران و آمریکا به جایی برسد
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/70576" target="_blank">📅 18:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=nhCYvLX6M7CVZTucSSYCEQSUK_bBlSDGbt5M02mEeHNx36iXeVisDQBI1MKFRSZWxStbq6_O6kTbaK8D87tQqLYykQkHPbN4Q2qXYBbZJHuBE2Eh-CZNft5NUQAHmkic7CfDVV4WL3koD8FuYsVIQ5YTSaLuYzTwtf45xxvGcY8T-wXsIaSVSh0FZRVYAT-SxEjCmeC35Agf7Xp_uy2OxZ93hqNeLPpGMmQzd0FUOhmft8-9nLMh4g0YjNC6a9ruLlB_Y9BwF7uQNek1eMZuBQdemHdgv9Oq6g3EPl1QlxaG5sBHgZ22cjBwpQ82KyQFHgG5tMCcbivXkJnBecWAqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=nhCYvLX6M7CVZTucSSYCEQSUK_bBlSDGbt5M02mEeHNx36iXeVisDQBI1MKFRSZWxStbq6_O6kTbaK8D87tQqLYykQkHPbN4Q2qXYBbZJHuBE2Eh-CZNft5NUQAHmkic7CfDVV4WL3koD8FuYsVIQ5YTSaLuYzTwtf45xxvGcY8T-wXsIaSVSh0FZRVYAT-SxEjCmeC35Agf7Xp_uy2OxZ93hqNeLPpGMmQzd0FUOhmft8-9nLMh4g0YjNC6a9ruLlB_Y9BwF7uQNek1eMZuBQdemHdgv9Oq6g3EPl1QlxaG5sBHgZ22cjBwpQ82KyQFHgG5tMCcbivXkJnBecWAqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
نگاه هویدا به یکی از بی‌شعورترین و بی‌سوادترین مخلوقات زمین
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/70575" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/70574" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOApMNfEI9-OVwvyNXA0bNZz_gbB9BU5jLZBkXyyJh-RAuo34n0avsqbf1TU_hlSs8unh_WNsPg5Alkf-ah1PD0mTjdUCawrYrlop15VCibV2mKPxh8FFyhP7K8GTIyoBgMoSlAeT5tVSJXHgwceWPN5kMZ2KvOEIihUkebfj_zOEKlPLNeEZzBwd91Un4O9XoBB11OB-YXQRSFQjiXcO7Sklxp7Q56EAjwyX9ruvgRQ1KNW86PqtPCBXXYRVof13oL-_1Zddkc6p7ocYb7_jb0TUCOq_H_spMKNgRgmjMsXLmm3OSoQo5lD0ZDMGm-ewKtvdyGKSya0dVYHoq86p36bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOApMNfEI9-OVwvyNXA0bNZz_gbB9BU5jLZBkXyyJh-RAuo34n0avsqbf1TU_hlSs8unh_WNsPg5Alkf-ah1PD0mTjdUCawrYrlop15VCibV2mKPxh8FFyhP7K8GTIyoBgMoSlAeT5tVSJXHgwceWPN5kMZ2KvOEIihUkebfj_zOEKlPLNeEZzBwd91Un4O9XoBB11OB-YXQRSFQjiXcO7Sklxp7Q56EAjwyX9ruvgRQ1KNW86PqtPCBXXYRVof13oL-_1Zddkc6p7ocYb7_jb0TUCOq_H_spMKNgRgmjMsXLmm3OSoQo5lD0ZDMGm-ewKtvdyGKSya0dVYHoq86p36bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g3
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/70573" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8T40UbdSe71WEuw_8tPwVCcApZUnS1I_FVcplmcqlhpjGVYZebMEYI_z_WFxKdTMHuWrgMW6G6J_DqyN1VfBl-tT32QG-3Cj9YhPort7q3fO17-38W-mQCi6EMAaCWdX2bSql_VEqzHJqbugeNyRWwesVKxOYj2hSeKebXlNyRkEWXb6yNURNUo9beqGaPARONVqGWcnQ_cKfePW9X7DCDas-dVo_geG2eNdVBUwYgyaK55m8XYnbHt5D3Hp84DxmT87o3ij9kUva1Eni8xCgAMG3M-G8l8XroueLpfcmlBlSqDnZL4CdyAjxryubpETK_ADP2MzetofHWUhpaFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
نیروی دریایی ایالات متحده به من اطلاع داده است که تمام مین‌ها از داخل آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدیدی را در آن کار بگذارد، فوراً و به طور سیستماتیک منهدم خواهد شد.
ما از طریق نیروی فضایی، هر اینچ مربع از تنگه را زیر نظر داریم، همانطور که در مورد کوه پیکاکس و سه سایت هسته‌ای دیگر که قبلاً نابود شده‌اند نیز همین کار را می‌کنیم.
سیاست عدم تحمل در مورد مین‌گذاری با تمام قوا و به طور مؤثر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/70572" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=WlKMzwwKqIPTB2YivH4GdeUpHl7k4SbjujewE1nej_SiGNXqyP6VhYsgmtS63-cVLpD1KQalr2y0TaZztPi-GJspqnjiI-zGC4Dj3XOfg0rMvyulPjzJErcNWXNr4jmQsXkf9ERtgsH0AdWBFB7YLvpxF6hVoQVBgALdd9muZ-nBG6JyeRZkuVqEsQpRWuTES8l_X8206aBBS5QciTs_upuWwwJL210c4MRqKrD6jVqcP2cxA5dhgkirzTTm1yvpFSHvG97Pzet7TWzN3_y6-AYMDgVu8ng4t9kDVx3amxQRdfygInVo5kOfc4VlKBTLICbNQ_N-61IHkRl6_O6ZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=WlKMzwwKqIPTB2YivH4GdeUpHl7k4SbjujewE1nej_SiGNXqyP6VhYsgmtS63-cVLpD1KQalr2y0TaZztPi-GJspqnjiI-zGC4Dj3XOfg0rMvyulPjzJErcNWXNr4jmQsXkf9ERtgsH0AdWBFB7YLvpxF6hVoQVBgALdd9muZ-nBG6JyeRZkuVqEsQpRWuTES8l_X8206aBBS5QciTs_upuWwwJL210c4MRqKrD6jVqcP2cxA5dhgkirzTTm1yvpFSHvG97Pzet7TWzN3_y6-AYMDgVu8ng4t9kDVx3amxQRdfygInVo5kOfc4VlKBTLICbNQ_N-61IHkRl6_O6ZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید باورتون نشه ولی ایشون بخاطر اینکه آلت تناسلی بزرگی که داره، گریه میکنه! میگه تا میخوام با دخترا رابطه برقرار کنم، جیغ میزنن وای هیولا، چه مار بزرگی و فرار میکنن
😢
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/70571" target="_blank">📅 17:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70570">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=mVm1TVYJB57ZEfBbhBjeRJSK_Mk2c3TvIVHEsVBdHYDdQJVyJErlxguvGY20txMunVLtYJVzOo53t_jNpuJo9kp75HHAeL1r4wpLulkScbSpOWgrrmHkFUIz9KySA4mLKjfjWEEesNumnG0WrxeLUX9Q_Q2mHAdMr8lBiFKJlGaXbCaH-YsgWT2OVJVQHaMlDrtXkaQgsFQxEZfjiAu5iGNN9YuzWKtWGltqVJgyyqUyi9d7K_1wowHzuVrbIys0sGdvicEao0wuuHMbf9s7_MpAhU_b-3J7hjNW_aX6k9I5LzHEYLzkv5H9SXCCSYwlIbZp2r3OJaKPMk7yL-bwUofulMZVBKm1UOLhRXN_eFKzQklt6ESBk5cl8HqXpqPYm8nJDm_JigzxO81LW2FA2CHm4lf-f-Q0jpEj-WFJj8VP-ARCQ724E5T6DWQAnhItTt2-_XRjUhRpYl6YXYL_JD-139J3Tt_J2Uhfy6RjIiK8F2OfMpnqa4YD2u1eRTvHGFTnSdoJjCNvBWuV_OpKkEPu9OFAf8zuhELhnoEKtvfwLpTWgn036hXz6kTFW9okzWtdGtoDlGLzFuuJuUnqzD1MR6tGhcVCR39ZV1tK0GkXIfviEcGAfGqKt4O6FWlgPlXYOCN7jQ8okYtzISo7xnDvpxPnp3H-n5ZYyT_CH_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=mVm1TVYJB57ZEfBbhBjeRJSK_Mk2c3TvIVHEsVBdHYDdQJVyJErlxguvGY20txMunVLtYJVzOo53t_jNpuJo9kp75HHAeL1r4wpLulkScbSpOWgrrmHkFUIz9KySA4mLKjfjWEEesNumnG0WrxeLUX9Q_Q2mHAdMr8lBiFKJlGaXbCaH-YsgWT2OVJVQHaMlDrtXkaQgsFQxEZfjiAu5iGNN9YuzWKtWGltqVJgyyqUyi9d7K_1wowHzuVrbIys0sGdvicEao0wuuHMbf9s7_MpAhU_b-3J7hjNW_aX6k9I5LzHEYLzkv5H9SXCCSYwlIbZp2r3OJaKPMk7yL-bwUofulMZVBKm1UOLhRXN_eFKzQklt6ESBk5cl8HqXpqPYm8nJDm_JigzxO81LW2FA2CHm4lf-f-Q0jpEj-WFJj8VP-ARCQ724E5T6DWQAnhItTt2-_XRjUhRpYl6YXYL_JD-139J3Tt_J2Uhfy6RjIiK8F2OfMpnqa4YD2u1eRTvHGFTnSdoJjCNvBWuV_OpKkEPu9OFAf8zuhELhnoEKtvfwLpTWgn036hXz6kTFW9okzWtdGtoDlGLzFuuJuUnqzD1MR6tGhcVCR39ZV1tK0GkXIfviEcGAfGqKt4O6FWlgPlXYOCN7jQ8okYtzISo7xnDvpxPnp3H-n5ZYyT_CH_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ارزش پول مملکت رقابت شدیدی با گوه داره؛
یه مادربزرگی گوشی نوه‌ش خراب میشه و میاد این پولارو میده به طرف که گوشی جدید واسه نوه خودش بخره.
به گفته‌ی خودش این پولا حاصل 6,7 سال پس‌اندازه. از دو هزاری بگیر تا ده هزاری جمع کرده که تا موقع نیاز ازشون استفاده کنه.
حالا طرف اومده پولا شمرده و مبلغی که به دست اومده خیلی جالبه‌:
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70570" target="_blank">📅 17:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70569">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439a914edd.mp4?token=bD9HDiAf4eNS314ROwvjXRnjoDSxNEUC6HoHhNFI5Xi-z8FlPruPL6-ljPdeyrQnhV3s0S4TRyeXjt7AGW2BMwzaS63CZaHlOMYqbLjpvuN-1xvknZCH8gZlxBb00ziYi7TJR6zt0tKBHuIJMU0c6rww1blUNSZKGpLSDw6pY8kjEjqex7sU2B_RSLWA2ks97ZWH6kqbCnMu_LsCM7qON1_XGWv6N4V_utTIk0J5hLM4tbZX98AdCZsQv2NyCSHBjRwjXOJlpyNDZ_T4ufxP3PowojzW6ousd_fRVEiWz9p6HD1gnT7gDH8VlIhke2RuVwiP84b6GKzZlG5f30a6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439a914edd.mp4?token=bD9HDiAf4eNS314ROwvjXRnjoDSxNEUC6HoHhNFI5Xi-z8FlPruPL6-ljPdeyrQnhV3s0S4TRyeXjt7AGW2BMwzaS63CZaHlOMYqbLjpvuN-1xvknZCH8gZlxBb00ziYi7TJR6zt0tKBHuIJMU0c6rww1blUNSZKGpLSDw6pY8kjEjqex7sU2B_RSLWA2ks97ZWH6kqbCnMu_LsCM7qON1_XGWv6N4V_utTIk0J5hLM4tbZX98AdCZsQv2NyCSHBjRwjXOJlpyNDZ_T4ufxP3PowojzW6ousd_fRVEiWz9p6HD1gnT7gDH8VlIhke2RuVwiP84b6GKzZlG5f30a6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70569" target="_blank">📅 16:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70566">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BB9lvkHXoeLIiVjn7JMCrqmFuvrQ5up7wunEdHIGV9p_lyA_Ch0FnunLx27XJBDbXjLSZYI6VhajpsKodP--rDEM9UfHJNxHmsG5N0Vm2uHFdoQBP_5a39D5CS-kwaSICIdlgSwoz9jaY8ek3GM5JdVqT0Wfs_j9nLmeKOJyl-WyIFFrOLVp1bQ-EinzV4IjK0fRoEdiOlQ4x7QUnhiUYbEFGuRAgEGjXuFpSF4Fse0PeLlaXjHa0TBN_EKyoe2gWttR9_Lku6tsD4hvuXS8f4C1nu92h3lMgLT2STIMAg9Tegj1Gpo4hXMLq5gE7iakSBdcJTxw079yTVDlQt8KVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fVtorTMPzXXEwJ19tUR81VKTumDjCeSyh_Zo1wulYOVjIGe5rS-5vFOAtTgDtMmpT4dlM7H43RiRKxkIGAnYyPxX6_Ry9lD7BYsKFyNmGSWgmMzhSg2W3BdWe1wGm97AUAo7oxcmrH4G03aCQ8V8l9lwYnaQMccTBi9_4Rz20NTs1uwQwZEpX3I-BdTMaZ2zVa09hJqbA3KziAwrj-f_b7u8crkNo1nkNzHnS_k9WgeH19abc7lTocJfaE8xgeNXzbkvvteEGwmirbt2jwVBoV9S0n3WmE1p0-grz2t2uNaQW_RvaL3mFjYRGSlfm-WaHdqJ_E5tKGTTCgdQGfum6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmVWhkov93jwlW8SsNOwqkrLRDq34OzXk1zADDpfJ_IcwMLxODVKfLXtMmKTFmpK3DcF7Q_GfxlKTj-_AaTcvCnKlLQWaWFT5Lkbp5MzHt3HY2WVFE42_DyIOcI9YY-8xNExR9SkkYy2FePToBhfNyZXoqaUKAlxMHIh4rR4r_LMn_bFVVy1x-CCj5dAQIzaAAuTKHri4fjWCDj7YLT1xPSxcs8c1sEIr02x20R-1c37c3XHJMjffpuTfeVFUEd2dRgU9STz5NrGyJz-qx-Xth9KigaNEEzhhUsMEuu7OrChqxIWQp9kSlYbByRdIzRHpEdsPnyKroaIVLwGTTVn8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇴🇲
🇮🇷
وزیر امور خارجه عمان، بدر البوسعیدی، با عباس عراقچی در تهران دیدار و گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70566" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70565">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCh1ZR4-a05kZ-7PXxaPWmy8GMhk8F0karhsgGwlMfV1h2dLe4Q_JcP1tY6rgHH9_bHDibS3IJHp7HalHyVpPwhB1zgpTZ18hS84UkH3Dh644ZqsZIU9-_iH1dYvh1h01lThxj4Go71kUQLQtKwgFcFEMrY638RjpAHx4BVP0UFqivGLiQ6mZcqCtaH7f2X5ZkeAN5ZqW0fhbIbhhX6s87dnoUtqk5T4NC4nInYamKH9B5TiXl8yWC0YX0qkJKsfq3De1oc4IFJnBZOXYik-GnG523IfuhX4mXtNuvvPXBqmmnNq5b4HgRg8iyCcDcWMn7rp_TcyjI5ESsPesPS1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
بانک ملی ایران در سال ۲۰۱۸ به دلیل حمایت از تروریسم توسط وزارت خزانه‌داری آمریکا تحریم شد، با این حال همچنان در سراسر جهان شعبه دارد. اسکات بسنت (SecScottBessent) وزیر خزانه‌داری آمریکا به‌تازگی اعلام کرد که تمامی این شعب باید تعطیل شوند.
🚫
مکان شعب بانک ملی به شرح زیر است:
۱. امارات متحده عربی — ۷ شعبه (دبی [۲ شعبه]، شارجه، رأس‌الخیمه، فجیره، ابوظبی، العین)
۲. عراق — ۳ شعبه (بغداد، نجف، بصره)
۳. عمان — ۱ شعبه (مسقط)
۴. آذربایجان — ۱ شعبه (باکو)
۵. آلمان — ۱ شعبه (هامبورگ)
۶. فرانسه — ۱ شعبه (پاریس)
🚫
بانک‌های تابعه / سرمایه‌گذاری مشترک (در ۴ حوزه قضایی)
۷. بریتانیا — بانک ملی پی‌ال‌سی (لندن)
۸. هنگ‌کنگ — شعبه بانک ملی پی‌ال‌سی
۹. روسیه — بانک میر بیزینس (مسکو، کازان، آستراخان)
۱۰. افغانستان — بانک آرین (کابل؛ سرمایه‌گذاری مشترک با بانک صادرات؛ وضعیت تأییدنشده)
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70565" target="_blank">📅 15:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70564">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJ_l4ePDhOdbHQDCDyAsrlOkaTSLR9ZyOC7fHrfl_pYIm7gxwTSiasWQ99XfXKj8xjwfiy9wB7B2L5wP-yk80XfGhfk7hgQJGYX7YoE7D8inMUFw_Hg436ak3Dnjjq9MM8V07irq6Gx7W5wmpunzdgUsnsrlAtlc6b48xjEm1KeE2hLN7PQ7jJ4bwGqH2aqxbRkX0_xIjvjwlDevL-cLDbgACDoEfwIPfTqZtUPL-tuvcIlM-DW1VMw_rxyJfGhp9kvqLaIEeF__a36CwGR1PjHkiQeM7x7nnTK6Q-TDj073HVJE6kPm4Fro6w4IV6bzj5Envbd4Ugu2pgZz7_Mp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی ایران که در حال فروپاشی است، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را — حتی زمانی که مشغول اعتراض نیستند — با شدتی بی‌سابقه به قتل می‌رساند. این یک بحران انسانی با ابعادی عظیم است و باید همین حالا متوقف شود. رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70564" target="_blank">📅 14:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70563">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=co3v8SmY-55xKlHrqRnBk8p6G7qIzAZ3bgwy6cTsxG5b17TZbZnRtDA2X4LYgvhBr1aBukQach200zmxOitdsPAN62OwCTcDQg3979RZRmFsBPykbgPzkE60OUYnzw7XEx9sDfnzYnWg4k8HOg5ZXWRhYKEbqXMhjWAB6rw-o985-z5B7uNfTZzqsG7XBpIaKheN51cpbAhAHS5KZr4jysmJQAvZeG2HkBLjy1kgEThmgNY7MEIIKvDrc3sEuUfN4auvVzmJrxdqxjuLaOVzMiXWYpERKhAtMJrvEy__G6ReLQHfCihNd4wp0yDHWJD_DRh_lfv19lbwFJLaCuzXoyCQyLnp43D5b2T6U8O34oXEYVn0fii9uruvKKMoR2oPZzRf9uFqVTBhdhKHz_tEmhqvKfmF2W0wCQqZmFF5Xnj4njhCYWwv405UurKdU-4CPMIj3RrFJlv_CF5tWRHP89AwVeOmdeTIdQ2xTD9t9MeR0wbLUdG-6HWws7bvqp_Rg-7R-54YgjoHYvsbFEtnmJ1fBhhkRq5iNtISswQtcD9qNb6c-6muRdDelh-NLUp41yaHkN7pPoD7D5OepQgFDn6Y4-7dqc8YzeUSz3QD7TgZCuStnuxWwhwO1I5uyJXzNhzeot0ME8Eo0mRLgDwpvX-_9Xcc6CdLakVpd0nBeDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=co3v8SmY-55xKlHrqRnBk8p6G7qIzAZ3bgwy6cTsxG5b17TZbZnRtDA2X4LYgvhBr1aBukQach200zmxOitdsPAN62OwCTcDQg3979RZRmFsBPykbgPzkE60OUYnzw7XEx9sDfnzYnWg4k8HOg5ZXWRhYKEbqXMhjWAB6rw-o985-z5B7uNfTZzqsG7XBpIaKheN51cpbAhAHS5KZr4jysmJQAvZeG2HkBLjy1kgEThmgNY7MEIIKvDrc3sEuUfN4auvVzmJrxdqxjuLaOVzMiXWYpERKhAtMJrvEy__G6ReLQHfCihNd4wp0yDHWJD_DRh_lfv19lbwFJLaCuzXoyCQyLnp43D5b2T6U8O34oXEYVn0fii9uruvKKMoR2oPZzRf9uFqVTBhdhKHz_tEmhqvKfmF2W0wCQqZmFF5Xnj4njhCYWwv405UurKdU-4CPMIj3RrFJlv_CF5tWRHP89AwVeOmdeTIdQ2xTD9t9MeR0wbLUdG-6HWws7bvqp_Rg-7R-54YgjoHYvsbFEtnmJ1fBhhkRq5iNtISswQtcD9qNb6c-6muRdDelh-NLUp41yaHkN7pPoD7D5OepQgFDn6Y4-7dqc8YzeUSz3QD7TgZCuStnuxWwhwO1I5uyJXzNhzeot0ME8Eo0mRLgDwpvX-_9Xcc6CdLakVpd0nBeDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر اقتصاد:
تفاهم‌نامۀ اسلام‌آباد روی کاغذ نکات مثبتی برای ما داشت اما اسرائیل و تندروهای آمریکا نتوانستند آن را تحمل کنند
امید داریم همان تفاهم‌نامه یا بهتر از آن احیا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70563" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70562">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGAvkhDOzhZPcKnB64PM9n641dh40kDuZG8woa1t5cyeemzyfmqQbxkXGjdas8QNWPzx54OFJBiBTdYb65_w0h-659geORgtP8VM6ulpXNJdcWHwn2Kl0cyty7dqhc7rkl7DD95U2EvZFZeOBhrCeSNqJ9IE6yKcIVYOUNdffLLzEVEIqb-rdR_RXh7sljFqGJhQwUxqjl35_Hp54Gnj5V_Ijh-TgwfBHyFzj08EfXdNntuodtJkO6XMslrks7dzy4kuJUZLUlt-zPIEjRU07WRjqLt8tWRAa6rtoUxLOXLMG7VJSJ-54ahK-q3n_RNp_bOnX7uUW1fGZIIhyupdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
حساب اسرائیل به فارسی:
درباره ماجرای دایناسور خراسان، احتمالا فردا امام جمعه مشهد می‌گوید: «این دایناسور از برکات نظام و نشانه پایداری ما از عصر تیرانوزاروس تا کنون است!»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70562" target="_blank">📅 13:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70561">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
📰
اکسیوس:۵ نشونه فروپاشی اقتصاد ایران زیر فشارهای ترامپ:
⚪️
سقوط ریال؛ دلار به حدود ۲۰۲ هزار تومن رسیده
⚪️
تورم شدید؛ پیش‌بینی تورم ۲۰۲۶ به حدود ۶۹٪ رسیده.
⚪️
فشار معیشتی؛ گرونی و افت ارزش پول، خرید مایحتاج روزمره رو برای مردم سخت‌تر کرده.
⚪️
سقوط صادرات نفت؛ محاصره و فشار آمریکا درآمد نفتی ایران رو به‌شدت کاهش داده.
⚪️
رکود و بیکاری؛ فعالیت اقتصادی و اشتغال افت کرده و پیش‌بینی میشه اقتصاد ایران امسال حدود ۵.۴٪ کوچک‌تر بشه.
با این حال تهران قصد تسلیم شدن نداره و ممکنه دست به اقدام نظامی بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70561" target="_blank">📅 13:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70560">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=VEATMgT2e-gyIaBaev29VchOR9Pt9HrWceuWOu4AGYI1WrYN0jyCl7aeHdE8kNYVKPnDeGzPcfvUFS_tM6dTpn9UJeowQnMWMDZe9DKr2kiLjGBVsjI9f66sLaTaP35wg_ktpEkY5T64g0-TDLFuDl8YObnM6-tQlfyfWKKBz9Fcw1ak13C9SM6eP_pltdJUGUJbNooIJT78wSvoQ31TbA0ZxDqVqljp2XYGZzUsvlClzi7AQSOsnUagbz6rtLcsdpt_Obgo3RqkVU36hisobkz6Pp0gqsGEIWgFn5wFCEl4p43-x3VuZStsvbBap41wtVAUH2RQ2vOxMTjt-zJQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=VEATMgT2e-gyIaBaev29VchOR9Pt9HrWceuWOu4AGYI1WrYN0jyCl7aeHdE8kNYVKPnDeGzPcfvUFS_tM6dTpn9UJeowQnMWMDZe9DKr2kiLjGBVsjI9f66sLaTaP35wg_ktpEkY5T64g0-TDLFuDl8YObnM6-tQlfyfWKKBz9Fcw1ak13C9SM6eP_pltdJUGUJbNooIJT78wSvoQ31TbA0ZxDqVqljp2XYGZzUsvlClzi7AQSOsnUagbz6rtLcsdpt_Obgo3RqkVU36hisobkz6Pp0gqsGEIWgFn5wFCEl4p43-x3VuZStsvbBap41wtVAUH2RQ2vOxMTjt-zJQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما یه ویدیوی جدید با هوش مصنوعی درباره پسر ترامپ ساخته و اونو تهدید به ترور کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70560" target="_blank">📅 12:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70559">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/377055b126.mp4?token=JWjGjFR6wYDpvtC8HjiRQjzmb4r4Kc07drEMFpc9dsLGzmNcXOJ0UcihFla7NGRfwNLVEz6JEHNvM6_wxT6USneh6TR6MA1caQ721rJW2pHXFEq5GCNpssGo2zNV3tDiNWgYV5du0S8SOFibJ-DPgGSiHAW-YkjAy5UQx7qwoPKIoV0FWS6KvplP7mdi2zfu3Pgq2GmXqSEH1vCOJkAmZ-BFgkLfqYfTw_YwUeu2dUhHZfLpWhjQf6bXoKbILYKLVIq_8TUwLnsAfK9L4qPBNjU8kkPPmNc8Px7-V5hFeNGM1YbY0qggo4Vrdg0DNulkrd65j6mYwykQ9bI1fjTeHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/377055b126.mp4?token=JWjGjFR6wYDpvtC8HjiRQjzmb4r4Kc07drEMFpc9dsLGzmNcXOJ0UcihFla7NGRfwNLVEz6JEHNvM6_wxT6USneh6TR6MA1caQ721rJW2pHXFEq5GCNpssGo2zNV3tDiNWgYV5du0S8SOFibJ-DPgGSiHAW-YkjAy5UQx7qwoPKIoV0FWS6KvplP7mdi2zfu3Pgq2GmXqSEH1vCOJkAmZ-BFgkLfqYfTw_YwUeu2dUhHZfLpWhjQf6bXoKbILYKLVIq_8TUwLnsAfK9L4qPBNjU8kkPPmNc8Px7-V5hFeNGM1YbY0qggo4Vrdg0DNulkrd65j6mYwykQ9bI1fjTeHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این شما و این برج زنبق واقع در منطقه ۱ تهران:
۲۸۰۰ متر پارک و فضای سبز اختصاصی.
هلیپد برای هلیکوپترِ اختصاصی شما.
بیلیارد، سینما، سالن اسکواش، باشگاه، مجموعه آبی، کنسول PS5 و سالن ماساژ.
اتاق بازی کودکان، فضای اختصاصی برای جلسات کاری، غذاخوری و...
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70559" target="_blank">📅 12:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=Inp7h2FYH-LsmrJqD8LxkSQ1TzofHuUtH8dPYgNwqr0d4VfMHh3mLkcLKjs2OWsHnob6V0sguJGlBkbcROQffKECF4_F-f1BmjtNReAV9IWpbZLu6crbt879z4ItFN0GnvuexUxn30giXvJP3w6VKZ_bpXdq3e63xt8cjToHJn7m_Tua1aSWMJ2JwqOj3fJYTn4mWFyLHIz0U369QXLfp0XWhXMys5nDyR3wInY0gFETo4vY1ekkRDo72kMRGf99hgXvvPO461GilxvVsmAIFeIRh51EEhl7050McysPi9Q5X6swCf8n1BfZ8vTF3PMOJWHPlUWnmYtRK0_OrxvqDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=Inp7h2FYH-LsmrJqD8LxkSQ1TzofHuUtH8dPYgNwqr0d4VfMHh3mLkcLKjs2OWsHnob6V0sguJGlBkbcROQffKECF4_F-f1BmjtNReAV9IWpbZLu6crbt879z4ItFN0GnvuexUxn30giXvJP3w6VKZ_bpXdq3e63xt8cjToHJn7m_Tua1aSWMJ2JwqOj3fJYTn4mWFyLHIz0U369QXLfp0XWhXMys5nDyR3wInY0gFETo4vY1ekkRDo72kMRGf99hgXvvPO461GilxvVsmAIFeIRh51EEhl7050McysPi9Q5X6swCf8n1BfZ8vTF3PMOJWHPlUWnmYtRK0_OrxvqDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه دختر برای پارتنرش شرط گذاشته که هر بار دعوا کردیم، برای اینکه باهات آشتی کنم، باید برام طلا و سکه بخری و پول بدی.
بعد از یه مدت رابطه، این صحنه خلق شده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70558" target="_blank">📅 11:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8lpbKDO6N3UZasPxtVAdnY1b-W1jNQPlQWgpvRMchIXl6SUzPLNu1axAx-usZPW7u0SU3B7PstCzFmevpIhNFKYUoYtupatF8zj3JrcyFkoT_Y9tNjrkYGHV7jjTOT84QZU_TArCBkr9oICCjxS8iXrI1UimimWSEGZXOY1_gLXro68N40U_scMB1ePWdFgsZ45_f_KlRlfLkkVo3Sfvgmt05-p_2UtFnyakNNdpdGE-sVUIjyZWtEYl4gCAkfaVsnCy48heNPLjF48RmCly46OJRUUMhI5Ouu5UdmqCgIHl8kVLgxKJlOz7KFicXN1doqSqlcgvHSMgvsShdKyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی از زمان دلار ۳٠ تومن تا امروز که هر دلار بیش از ۲٠٠ تومن رد کرده به آینده اقتصاد خوشیبینه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70557" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70554">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=vJXZxog-2f3-YrUP5qjCHQKQ9F_UXe_v8-WwuCeGcyoHR586Xg3mdLMLDBUR_N62NUA3Uh2rVOROGwBPoB6UEZSnq-tT2AXgt27ucROcYWQ1b65TtXEbCHCWWw7Qs6MEiBMbXi3SiFxDeDTQQ9S7eMefj1Io-3KHJ0o1lVV32gO62lK-H7ZVM_w8k458P7Pf1AvUEohgjy4znSl9UJ9rWe0yXc47UHWFEWw1bZjc-qmXEfPwYyRhlUxB06PsuzJCKBINqn0wRNzIjODEYQKvGuID3g0IoQ6d2rLGpBE3lxnWKOhgkyw2jQicm_viDrwG3k3_p7hpBkqTmrvUjAXP_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=vJXZxog-2f3-YrUP5qjCHQKQ9F_UXe_v8-WwuCeGcyoHR586Xg3mdLMLDBUR_N62NUA3Uh2rVOROGwBPoB6UEZSnq-tT2AXgt27ucROcYWQ1b65TtXEbCHCWWw7Qs6MEiBMbXi3SiFxDeDTQQ9S7eMefj1Io-3KHJ0o1lVV32gO62lK-H7ZVM_w8k458P7Pf1AvUEohgjy4znSl9UJ9rWe0yXc47UHWFEWw1bZjc-qmXEfPwYyRhlUxB06PsuzJCKBINqn0wRNzIjODEYQKvGuID3g0IoQ6d2rLGpBE3lxnWKOhgkyw2jQicm_viDrwG3k3_p7hpBkqTmrvUjAXP_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی در طول شب سه مرکز لجستیکی اوزون را در سراسر روسیه هدف قرار دادند و تأسیساتی در آدیجیا، استان استاوروپل و داغستان تحت تأثیر قرار گرفتند.
این حملات در میان مجموعه‌ای گسترده‌تر از حملات به مراکز توزیع بزرگ روسیه، از جمله سایت‌هایی که توسط اوزون و رقیب آن، ویلدربری‌ز، اداره می‌شوند، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70554" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70553">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70553" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70553" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70552">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qra0YbDiNbb35b68D3rpAPxWpEu0yIlvZMIYV8FI35BkwwWAeLqYOgV8e5KnlUdtizQ8IE3BgMWiEFI9-jxZRRwrL_wMd7QUsPbTRy24j81Z6t2cNNZCWcfoc1eokuCpESm0P8Q4a3uHbceBQyJwOeBLU2EpGm5J1s90T0vn-Lr3vPngYfibz8Auly67fxlhQY8Aet3MywWVWXt3o9j3PNqrlfxIKYbvmhihDpoTU-uy2vXMadRQtW9yEJJuu_IMXQgkYLVMiElTQYU0WsEpsMl3yoXdxTXWFVRPhxiYrYW3Oa93p7EgVQj9vJ9cxCFjVs6M6XJhZjVC19MOQ8FycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r3
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70552" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70551">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇵🇰
وزیر کشور پاکستان: پیشرفت قابل توجهی در گفتگوها با ایران حاصل شد
⏺
📰
خبرگزاری رویترز به نقل از وزیر کشور پاکستان:
پیشرفت قابل توجهی در گفتگوها با رهبری ایران حاصل شده است.
ما در حال گفتگو با ایران برای فعال‌سازی مجدد «تفاهم‌نامه اسلام‌آباد» جهت حل و فصل اختلافات هستیم.
محور گفتگوها با ایران، تمرکز بر تنش‌های منطقه خاورمیانه(غرب آسیا) و یافتن راه‌هایی برای گشودن مسیر صلح است.
دیدار با رئیس‌جمهور ایران با نتایج بسیار مثبت به پایان رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70551" target="_blank">📅 10:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70550">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b422bdb1ee.mp4?token=ChZT3FhD6pRdgy_i-M30KI2-AIfCiSBezvIchO0sY-mjZC4Xsg3VuV3ArZ6RBZUpV0MB8MqzeWP0Rl0Ea9chlxoCQkDd0-GYdDSR2sPKWZL1DP-5GAWpkm5HPy4CSlMmz3aFKAN9MbBvjzddt8G0DZavaOjfdEGmBFGnOPabG-mybF-luOXBS14tgHxpzkrMCulPYBj2qnv9M4C2_qUv6eTaiAbstu1hWaIrNCrjxjqVGxazQA1C7BSwv_uwzHxdjA6O2URy2qjWsZ5UeNu5rKf9B-xqg_FqloU8QFQwNhoZHNjUjNFNnMwHwKta0LmkIcqiJL3yvbLUWYj-MLsQ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b422bdb1ee.mp4?token=ChZT3FhD6pRdgy_i-M30KI2-AIfCiSBezvIchO0sY-mjZC4Xsg3VuV3ArZ6RBZUpV0MB8MqzeWP0Rl0Ea9chlxoCQkDd0-GYdDSR2sPKWZL1DP-5GAWpkm5HPy4CSlMmz3aFKAN9MbBvjzddt8G0DZavaOjfdEGmBFGnOPabG-mybF-luOXBS14tgHxpzkrMCulPYBj2qnv9M4C2_qUv6eTaiAbstu1hWaIrNCrjxjqVGxazQA1C7BSwv_uwzHxdjA6O2URy2qjWsZ5UeNu5rKf9B-xqg_FqloU8QFQwNhoZHNjUjNFNnMwHwKta0LmkIcqiJL3yvbLUWYj-MLsQ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو به تازگی وایرال شده از یک گروهی که رفتن کرمان و در مکانی بنام قلعه دختر مثلا جن احضار کردن
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70550" target="_blank">📅 10:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70549">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a52e52e69f.mp4?token=mlFZT7GtsBdfuoacxyAOhgejgeTJ9-xicFTlMYm0sW8Mcy9IO98AnwIEUqyLgZMie9f1K7x-Cd98ubM2h8OB8hLFzfeufwX_UDwsJFx_3qWJes0v7q5yuEZCLgJa7lFyYaaRVGBswz_HxMfBvFNL_IWgetoGTBJ0qZ5T235rT-FHJzGsd1ebIS1W4dt-vJTJn0IaR8Dd8N5cKIZzKJ8J_t5SIqTr_CF8LSDxTgJGOTuYumKuOFb7l8zSj8dptt6KGMZ0ncktdgo5eURNzXMKbqGjFYD5nmKnXVyBm9KXNdTtco0azGoyNMuo1xa7Rw9D8OTOguynbnfjRLVCDpiLy66LgYIHmFQbAEBxLDAYaa5mxyt3WL3TR33v_pB-UJjAZG73bGr7j2LD1CFijtiJ2x2TjSLtIGEbX3R5UWxEXgyQtcERHW6y5oKVqItu50sV0RmEEwvtrcOEw0QJiawwP8LdY7qNnGu2sZhnpn4OnOpDrKCq-3lGERW75VGksu6Lw-_1lZkpUheO0PkigTeIuqh8X5K1idoYGRGqzoOblQV5VpzVMI-_wl8ncseC-erbIl-C7y6JvK-ez-g35ghyOfmlAmcQS-4hFpsl_A5Fl8snTHPTQfpsRm2cwfnoKubKvftjUTl9l0s5x5PWoJeEERpms33WGOWUFnQl4DIaDY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a52e52e69f.mp4?token=mlFZT7GtsBdfuoacxyAOhgejgeTJ9-xicFTlMYm0sW8Mcy9IO98AnwIEUqyLgZMie9f1K7x-Cd98ubM2h8OB8hLFzfeufwX_UDwsJFx_3qWJes0v7q5yuEZCLgJa7lFyYaaRVGBswz_HxMfBvFNL_IWgetoGTBJ0qZ5T235rT-FHJzGsd1ebIS1W4dt-vJTJn0IaR8Dd8N5cKIZzKJ8J_t5SIqTr_CF8LSDxTgJGOTuYumKuOFb7l8zSj8dptt6KGMZ0ncktdgo5eURNzXMKbqGjFYD5nmKnXVyBm9KXNdTtco0azGoyNMuo1xa7Rw9D8OTOguynbnfjRLVCDpiLy66LgYIHmFQbAEBxLDAYaa5mxyt3WL3TR33v_pB-UJjAZG73bGr7j2LD1CFijtiJ2x2TjSLtIGEbX3R5UWxEXgyQtcERHW6y5oKVqItu50sV0RmEEwvtrcOEw0QJiawwP8LdY7qNnGu2sZhnpn4OnOpDrKCq-3lGERW75VGksu6Lw-_1lZkpUheO0PkigTeIuqh8X5K1idoYGRGqzoOblQV5VpzVMI-_wl8ncseC-erbIl-C7y6JvK-ez-g35ghyOfmlAmcQS-4hFpsl_A5Fl8snTHPTQfpsRm2cwfnoKubKvftjUTl9l0s5x5PWoJeEERpms33WGOWUFnQl4DIaDY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوی جدید از حمله هوایی و پشم ریزون آمریکا و اسراییل به خرم آباد در جنگ ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70549" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70548">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10dcd43f2.mp4?token=hmJYhUxdLBnvSzJSSy-fpnQWefMrDw1bAhD5uMhHbSzS5BdRV4WGeMdm_ZgkPdpiGNuVPehk8O7roiFD0SYhvObY_7q7xvy58hCrKNMkTXXVrpEWbG_hl_HpjYT8JLwokpxQm6DkKyu1A1KKpmD5vAOcvVJHDtjw8VWVHpabPBaMbULgtlqAMl5BpPACqo7v_kA_SX-8h8262eQAfUWFIhflE4XLGYvjEJXTJWARt0s_0Jk9nR-98Fr3i7lvxKi2idmbiXFrSBI62gWqSqBoNd-7U7Ah3K1K8pwwaBeecbo4s_hTS55IRVdeoHLeZfPcHi2EMWMD0hfNLdB72NAlOJgfwKr9P_TsW-ejzHUG-i32z2R17RBZ4k1AoxBE8P3M7f0LBZI1j2-hdov4ItSHQEccmxbCwqZJ2ywdfMC684sjbAAvtcax3HtbASzWEWxsu3B9bqJbkDOSXrNNe8VH4aJaGsm4-QeW4rvoSau03UHZ82_kvBw9CLwY5-4dXG6U1eWxB80EKCj-DmLJowEr5o_RNcpBqIev-ZMKgmjRYbN15PBvfaWaOLCZUDURZsROpsivXuLQZ0ATanefy1d7KBTCPAtrZHJAyXay3UYekKzWIFWxvCfK8FdSM8ryjWAOoqckxCGWMLglsyr0ESn4PvpSLBmWAZUUduN6GectGpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10dcd43f2.mp4?token=hmJYhUxdLBnvSzJSSy-fpnQWefMrDw1bAhD5uMhHbSzS5BdRV4WGeMdm_ZgkPdpiGNuVPehk8O7roiFD0SYhvObY_7q7xvy58hCrKNMkTXXVrpEWbG_hl_HpjYT8JLwokpxQm6DkKyu1A1KKpmD5vAOcvVJHDtjw8VWVHpabPBaMbULgtlqAMl5BpPACqo7v_kA_SX-8h8262eQAfUWFIhflE4XLGYvjEJXTJWARt0s_0Jk9nR-98Fr3i7lvxKi2idmbiXFrSBI62gWqSqBoNd-7U7Ah3K1K8pwwaBeecbo4s_hTS55IRVdeoHLeZfPcHi2EMWMD0hfNLdB72NAlOJgfwKr9P_TsW-ejzHUG-i32z2R17RBZ4k1AoxBE8P3M7f0LBZI1j2-hdov4ItSHQEccmxbCwqZJ2ywdfMC684sjbAAvtcax3HtbASzWEWxsu3B9bqJbkDOSXrNNe8VH4aJaGsm4-QeW4rvoSau03UHZ82_kvBw9CLwY5-4dXG6U1eWxB80EKCj-DmLJowEr5o_RNcpBqIev-ZMKgmjRYbN15PBvfaWaOLCZUDURZsROpsivXuLQZ0ATanefy1d7KBTCPAtrZHJAyXay3UYekKzWIFWxvCfK8FdSM8ryjWAOoqckxCGWMLglsyr0ESn4PvpSLBmWAZUUduN6GectGpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان تحلیل‌گر ارشد سیاسی در مورد فشار اقتصادی آمریکا؛
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70548" target="_blank">📅 09:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70547">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70547" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70546">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAkJaXwEMNKff3J6OoEyk4PQjGdJuTI0nZZNxHAcjtG_BW-67CViCm6_N7bodvzf-qcaRUPFWyMbjXD6qXvah9Wz-4HumO2LqO6W4mYtXnYWcG5SCRNXtyAucHzxnYOflu9B376NWpKJrbUjXni3hO1spncV29J9LGK5qpLpaiPXcaWX7L1TFk-NiKewvCOX1xGVBblv4Oywt9dy9ZNlouLy-2JQgMxN6ItaeSwva8bT_cINcFFOMwt4E45SJZ-V39v1Wwp0tMAaGVeylKzh8SIozBh2nHjW6WRdwIgmuYqiv3Y7tyhkdOR5L3PRSoOAeUbpiVcv-KW4fvcwF0KCxBg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAkJaXwEMNKff3J6OoEyk4PQjGdJuTI0nZZNxHAcjtG_BW-67CViCm6_N7bodvzf-qcaRUPFWyMbjXD6qXvah9Wz-4HumO2LqO6W4mYtXnYWcG5SCRNXtyAucHzxnYOflu9B376NWpKJrbUjXni3hO1spncV29J9LGK5qpLpaiPXcaWX7L1TFk-NiKewvCOX1xGVBblv4Oywt9dy9ZNlouLy-2JQgMxN6ItaeSwva8bT_cINcFFOMwt4E45SJZ-V39v1Wwp0tMAaGVeylKzh8SIozBh2nHjW6WRdwIgmuYqiv3Y7tyhkdOR5L3PRSoOAeUbpiVcv-KW4fvcwF0KCxBg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
⭐
کانال اطلاع رسانی سایت:a2
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70546" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70544">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rsfGYcdPwrc6qah3QD-RuO5pTHFIttzSolZYe50IUSJ1CvlBuEWmts-PEwsxl4tL9LeJXrfuX_lWK-DbDkgB-mqAQoBf4dGV2xSTlGGfo8Aa3I9PhZhdsvXLKPO14btBfKfv9V-9tnZAWfkti969IY93pXZCOjSTSd6S-no2T2FfsDvCdLzmm3I4TEkAIDm99aD_E5UbIesj_N83tHos6CqeGFsiRTadU7MWyvTG9fR-TsvfKgPUcrYH0IFloSsfAXMT1J5fDTwkbUGqoAQVg2lN6TAo2ElpGveUCcwHrjGvtpsspy9TxMXrCnaCQAeAKH9RA021DIyB_rC6YqKbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5fWVYfMRjoNqqBRNbC__hG3jM6Lyw4B9fFBkwc_kieUqWovncxZppgkuMfRH4MDHNw3Ac_xYmKIr_DNOCtrkFIj26sOaNmZ7zkkldE57LAkbrdwVmS2WchJhsp3TZDT7OJ1H7BTMFmPnSH3i7KdrZsenDMO8iCowwgAMfrEksGs1KS_0Im_3yw1qLVNE8I-3whgqbdtcwH3irFQ5_VoaalBSfLIGKoHWuKGRXva_G76p-gPfQioLMESjFJBuo9uIa8Yk0JIyNA7sRYJmlJ1Q3hqMZPkWvGaA8vK-28ODGXl5czCIxm1QzkA5baeS92KCyzU9JG0zdK8HnMlgPkN5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
#فوری
؛وزارت امور خارجه ایالات متحده:ده میلیون دلار برای کسی که اطلاعاتی درباره رهبران سپاه پاسداران انقلاب اسلامی ایران ارائه می دهد
احمد وحیدی/ فرمانده سپاه پاسداران
علی عبدالله/ فرمانده نیروهای مسلح (خاتم‌الانبیاء)
سعید آقاجانی/ فرمانده واحد پهپادها در ستاد هوافضای سپاه پاسداران
حامد لشگریان/ فرمانده واحد سایبری در سپاه پاسداران
مجید خادمی/ فرمانده اطلاعات سپاه پاسداران
⭕️
خبر واقعاً دوباره در ۲۴ اوت ۲۰۲۶ در حساب (Rewards for Justice)منتشر شده است اما تصویر قدیمی است و بروز نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70544" target="_blank">📅 02:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70541">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=RkGRlQitW4uZbZGzWCAGMQlLJhSRSbZG3BKefCM3G0nc7y3mtHxP-ffgY3uaUq1g4jMTKveQNsPd10S4Hg2m4PfkR0_TXbis6H-jFV6AxS3ZAe44nXX9Ip46Fu93PllONj5-LlQVsr-4wIjsQJ8hjYM3OJr06-tjCjl6bt0nosIZyrXZbAqeApCIzdX7qS8oVjfLu0JyLqLym4UNpYgFegYY9TEeQLib8cXm9eRgZpxpzifyhDbLCEnFAMuAcc03IpRwWufTH-RzmqT49dhB0nl6hSBqgfn2o2-UacoMvDzjfw3OMnAqkEF6zzdqEO4QkIFMkAH7OjgL_hOaqo1yLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=RkGRlQitW4uZbZGzWCAGMQlLJhSRSbZG3BKefCM3G0nc7y3mtHxP-ffgY3uaUq1g4jMTKveQNsPd10S4Hg2m4PfkR0_TXbis6H-jFV6AxS3ZAe44nXX9Ip46Fu93PllONj5-LlQVsr-4wIjsQJ8hjYM3OJr06-tjCjl6bt0nosIZyrXZbAqeApCIzdX7qS8oVjfLu0JyLqLym4UNpYgFegYY9TEeQLib8cXm9eRgZpxpzifyhDbLCEnFAMuAcc03IpRwWufTH-RzmqT49dhB0nl6hSBqgfn2o2-UacoMvDzjfw3OMnAqkEF6zzdqEO4QkIFMkAH7OjgL_hOaqo1yLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم تکون دادن ترامپ در رویداد «Freedom 250 Grand Prix» در واشنگتن دی‌سی، برای آغاز مسابقه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70541" target="_blank">📅 02:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70540">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kik2-bqtZcARdXH1IQCDX1VBkRl4qCnj9pnFkA27qh1wAKYANuUjcenBwviB2pCmMJBy1zKB4FVGPQOVAy071z1kx5QfVqkRYdxxZmTRroGBM2hENyOCzsZM7wKS9uUyrrFFuFwqtQejtSrul_37AjsvnWa1ctESk4NLJ0bU3kKIUOuRplY8daxliVZhgJ1LcxgVsAgXYb7e8PiLNxKiLW148j_A6Eeh_Fqtf5Yr3LaiVcNU1r1K0oY4ifVdLIHy9Z-i-fgXGVjtTQcAnQ8_VoA1CqGiSHpBQs8bThMQkjammOxay3Ixyn0wtz23Ym_CRUrBWezPkounuKoyjD61kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا:
ما گزارشی درباره وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرق منطقه الشیشه در عمان دریافت کرده‌ایم.
یک نفتکش مورد اصابت پرتابه ای ناشناس قرار گرفته، بخش موتور آسیب دیده و کشتی از کار افتاده.
خدمه سالم هستند و تاکنون میزان تاثیرات زیست محیطی این اتفاق مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70540" target="_blank">📅 02:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6611759db.mp4?token=kAuDvBqAi85HudRTKUsv1kpZ16VlC1fHFkAY3HTAWbQKete1SD3FS1cZJKmRBUTZU4ruEcZst4lH3hvqbY9-INxtdkX78dlQiDq4F9BccvWtlJkPEUMZtvO6H4uHJGjCrX8MvtQCD6N2y-7HdWASQnhKbk-ohJuiWH66UWbYyAVKIEDi_xts_iIak0vJ5k_fHSkVF6gOgXKVCOnKLavqjyZuBR9kJ9Y5errAdigEjWTsjmTFWO0ZdeHjHM9NgQGzmrS2EKu8PC01YOnjep9kNnJputUu2G4_Ik9039k1zc5A2Kf6keL7zgVvuAE2dXmp5PVXjS8ybEDxUuT-l3CIaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6611759db.mp4?token=kAuDvBqAi85HudRTKUsv1kpZ16VlC1fHFkAY3HTAWbQKete1SD3FS1cZJKmRBUTZU4ruEcZst4lH3hvqbY9-INxtdkX78dlQiDq4F9BccvWtlJkPEUMZtvO6H4uHJGjCrX8MvtQCD6N2y-7HdWASQnhKbk-ohJuiWH66UWbYyAVKIEDi_xts_iIak0vJ5k_fHSkVF6gOgXKVCOnKLavqjyZuBR9kJ9Y5errAdigEjWTsjmTFWO0ZdeHjHM9NgQGzmrS2EKu8PC01YOnjep9kNnJputUu2G4_Ik9039k1zc5A2Kf6keL7zgVvuAE2dXmp5PVXjS8ybEDxUuT-l3CIaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
برخی از کاربران فضای مجازی مدعی شدن امروز برای اولین‌ بار جایگاه های بنزین تهران با کمبود بنزین مواجه شدن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70538" target="_blank">📅 00:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK23w5zRf1tlNLx2C1ErXZl-5ua4eIO5M6l_nGhoBpZVbNOaPgIEUZ7o__RXpEwjgRQVcn6yfZXBk1P-wz6AW1_8llgknnKn7hvfe9BShDrDCbhsdWoWbnxi7VVG4pewT4cUhXU4nBLbcy0GFPDPDiOgpIWbsXR42CYgMLMSzj_g2vDoHABISma1J43L5f5DkSJCZT-troRFeoLq8lQYAevCA3vodLMXq6g-iv66aP40g2cHvO9hYz1150I2TEqACt7Q8nvMNHHUOYur5sXSu4fpSToobshiGl7p2rFtozBFaqxVxsWy_gWDAL-d5gOcvY1pbmy3D-mOTN-wgPaRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=o5vIqMA5ugdGHFVik30OIbLhAvGU5iRud1dhlUrjNMGz5cE2SIFaKMHqRfPmknhAbLVW1dRM5xd77_6ULf5yDzg7Z7nUyDwHPXg4PgZbowWYYdn4db-EsvsjILyzE7X31OTf7_4zK4ihCubZwONp33n5y0LGxZyUyOibkJI4WUZ3ibDKvZqwRf0UpYEw-AY2tmEGiRd5qqcw7WinXyScp9EQ4aEEmEIsXEGG_oMuRDJ_L3XwNM6LbQFHantUaJABMuRozmTyMOAOLAxW-YChaB_ShjNB-M6Q_L3kczhAVleS8avW85Th7CCaFnBYvkPcVZhTL3xJP9orvDRpWrXnsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=o5vIqMA5ugdGHFVik30OIbLhAvGU5iRud1dhlUrjNMGz5cE2SIFaKMHqRfPmknhAbLVW1dRM5xd77_6ULf5yDzg7Z7nUyDwHPXg4PgZbowWYYdn4db-EsvsjILyzE7X31OTf7_4zK4ihCubZwONp33n5y0LGxZyUyOibkJI4WUZ3ibDKvZqwRf0UpYEw-AY2tmEGiRd5qqcw7WinXyScp9EQ4aEEmEIsXEGG_oMuRDJ_L3XwNM6LbQFHantUaJABMuRozmTyMOAOLAxW-YChaB_ShjNB-M6Q_L3kczhAVleS8avW85Th7CCaFnBYvkPcVZhTL3xJP9orvDRpWrXnsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خرسی که وایرال شده بود مهمون سفره کوهنوردا میشه
متاسفانه رئیس محیط زیست مشکین‌شهر از شکار شدن این خرس خبر داد
💔
شکارچی هم همراه ۴ لاشه از حیوانات کوهی دیگه دستیگر شده
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70534" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaOswemOIouSiW3BfjvPQpm6MOIXAsMeAuf-PRWjeg8rylu6ABAi6MHAO-G9RjUOPCKqSlO9hVQ9B36Q1_-FBSj0VtZOIK551mI4agvmr17XdeQoTRXn7PWgPYU9TQxDTzLy77_ZMKJpEfVwz_Fc1aAmdt0FRYbre09HKxDdSAkrMtbtvbGewg1r1skqh5D2ObvFUXy-qpMClXzkOAmBq2kW8hctIMW51yj0on17zGjc9l1yBPOE_KJtZp1R7pjY4xK49gOnn9R6JVw2BYFTQeHPqvpxR9ylYpH2i37xRWyqEy2vUKMZDatosT-SJ5QG0bVLjGZQYb68TJcPHb1pCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
به دونالد ترامپ، رئیس‌جمهور آمریکا، و اسکات بسنت، وزیر خزانه‌داری آمریکا، بابت تحریم‌های جدید علیه جمهوری اسلامی تبریک میگم.
شما کاملاً حق دارید از این دیکتاتوری سرکوبگر و کسانی که به ادامه اقدامات تهاجمی اون کمک می‌کنن، هزینه سنگینی بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70533" target="_blank">📅 23:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=SyzfBPnTuoFt7bcbrvbrduhUQy9e_5-Gtbbim4dLKUS2239YnZ4Kmg32NlLyUD9tx5zW6U1WEvBmJXSncieTlujjZogq7dIADtmihS_8PCwXfrlAaUk_7c7C62Q-rMMkKOwUcR_7vfgJuGbsmhhgJhXSIYNcyyk8cKCx5LtWxxhU04JX-NPfj8mrhvZdke-roUcKKSJCl-pD09Ajrkqjwg3W8c8nMCoIQLsCCMlEliKvvkgxX_y1kFUyP4CHQ2BBk862jekgkfbtqsNXvH5y7PEiuJ_qeIBzBRuLB2lGWNKqqs_wFFKrUQuUMnkP1Qr4RqhNvJH8TmDBHEeu7SNfdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=SyzfBPnTuoFt7bcbrvbrduhUQy9e_5-Gtbbim4dLKUS2239YnZ4Kmg32NlLyUD9tx5zW6U1WEvBmJXSncieTlujjZogq7dIADtmihS_8PCwXfrlAaUk_7c7C62Q-rMMkKOwUcR_7vfgJuGbsmhhgJhXSIYNcyyk8cKCx5LtWxxhU04JX-NPfj8mrhvZdke-roUcKKSJCl-pD09Ajrkqjwg3W8c8nMCoIQLsCCMlEliKvvkgxX_y1kFUyP4CHQ2BBk862jekgkfbtqsNXvH5y7PEiuJ_qeIBzBRuLB2lGWNKqqs_wFFKrUQuUMnkP1Qr4RqhNvJH8TmDBHEeu7SNfdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اوستاد خوش‌چشم :
جنگ بعدی تو آبان و آذر با بمب باران شدید آمریکا شروع می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70532" target="_blank">📅 22:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">با این کیر شق شده‌ای که من از اسکات بسنت و ترامپ می‌بینم، مطمئنم خیلی زود دلمون برا دلار 200 هزار تومنی هم تنگ می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70531" target="_blank">📅 22:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=eRDa04v43AXkfQkwo8F7uv7KWHq0xZL7yQsFlglELqeOg92V9OAIEGbrzZLIycZMT-y-EffTxYVC5wdTGReVghrjp7mmSFzDyr2xKYGcdpQNr86_GUapQdt2oKSBwttyEBdaa4qyiK15XotQOxIYLcrDK0e_Db3Mu3NIWOUCjMebj1vRyZYDUARw63Lkbbg3vhjidO326Ccj8zyiu01c8uHBI-HYe9HufMKOoy_Gvqnogdk7J9iGCkqMRx550oM8PhPM2S2D_8gwZTQOPIDxNhOyvuOLc-g37M6I26vGOmXXSvcjZ1-MCCUU1LkDBCQVob6_YWEvpp9DvW1JXzbLtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=eRDa04v43AXkfQkwo8F7uv7KWHq0xZL7yQsFlglELqeOg92V9OAIEGbrzZLIycZMT-y-EffTxYVC5wdTGReVghrjp7mmSFzDyr2xKYGcdpQNr86_GUapQdt2oKSBwttyEBdaa4qyiK15XotQOxIYLcrDK0e_Db3Mu3NIWOUCjMebj1vRyZYDUARw63Lkbbg3vhjidO326Ccj8zyiu01c8uHBI-HYe9HufMKOoy_Gvqnogdk7J9iGCkqMRx550oM8PhPM2S2D_8gwZTQOPIDxNhOyvuOLc-g37M6I26vGOmXXSvcjZ1-MCCUU1LkDBCQVob6_YWEvpp9DvW1JXzbLtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیوی وایرال شده از یه پیرمردِ حامی حکومت که به طرز سنگین و عجیبی داره پرچم تکون میده:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70530" target="_blank">📅 21:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9839729319.mp4?token=owRLGUwQC4wggMmuk35MtxzNzXdCLDJF8c9JHOSwQfEHlJKdmLk6Octft5_wM93Mitiwz_uOIoYuozWrdFt5heTL7X2O0luRO1-4L8WbS3ZkTdJm6AVLsGnVJutDjVibGpXueFYerGgR54kJG4MmuPh6-L2qWJC-ELcXHFwW9seR_ya67zYCScXZ693uKglVEvw-SgvumodT0mZaNR6OEEtv0uo8jsL50AQm5_W0kh2voHZeXt-Sn4Zu0hNlidCIrdKi5HyWpEK3fUU4pwAKfNrKtvHbHPn6oJ-raPSm6BOpczuDr-5LvEE_Az4V-9-JZBcXQdu5qNMaqone2ZAbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9839729319.mp4?token=owRLGUwQC4wggMmuk35MtxzNzXdCLDJF8c9JHOSwQfEHlJKdmLk6Octft5_wM93Mitiwz_uOIoYuozWrdFt5heTL7X2O0luRO1-4L8WbS3ZkTdJm6AVLsGnVJutDjVibGpXueFYerGgR54kJG4MmuPh6-L2qWJC-ELcXHFwW9seR_ya67zYCScXZ693uKglVEvw-SgvumodT0mZaNR6OEEtv0uo8jsL50AQm5_W0kh2voHZeXt-Sn4Zu0hNlidCIrdKi5HyWpEK3fUU4pwAKfNrKtvHbHPn6oJ-raPSm6BOpczuDr-5LvEE_Az4V-9-JZBcXQdu5qNMaqone2ZAbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
«بِسِنت» درباره ایران:
کشورهای حوزه خلیج فارس در طول سال‌ها از سیاست مماشات با ایران چه چیزی به دست آورده‌اند؟
زمانی که ما ایران را بمباران می‌کردیم، ایران کشورهای حوزه خلیج فارس را بمباران می‌کرد.
سیاست مماشات در قبال این رژیم کارساز نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70529" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=GgkC9dej4eP5sN69jTMJIkgUt6kvKJjDEk_Lpv970v7ZZICCWayafqOYnHz5QnW8lrGFQmPbHJYF1a2v9Iqn5lEgOn6QsmO7tyLf0ebtYYAcPEsya_QFzIAUVKuGzeHSBJybWwEhr_32yfEuf1WUYXhE-dQI4YpQ-WS-ntLdR_zRLasZWdLWilcI0f6Cspv51FOjLo5uNYlxufZWChwMSqPVcZFKJWjxgunVZIZAAfINnNqmD_6VYt2Mdwefbjk3ljsYyclFEivZKPvbaJ_iFtzCSwkYVLiaJafcBzQSCrg6GvRnUoeqt0J6d7MVrPfhVc0MaGAvZpDYaSmHWxlOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=GgkC9dej4eP5sN69jTMJIkgUt6kvKJjDEk_Lpv970v7ZZICCWayafqOYnHz5QnW8lrGFQmPbHJYF1a2v9Iqn5lEgOn6QsmO7tyLf0ebtYYAcPEsya_QFzIAUVKuGzeHSBJybWwEhr_32yfEuf1WUYXhE-dQI4YpQ-WS-ntLdR_zRLasZWdLWilcI0f6Cspv51FOjLo5uNYlxufZWChwMSqPVcZFKJWjxgunVZIZAAfINnNqmD_6VYt2Mdwefbjk3ljsYyclFEivZKPvbaJ_iFtzCSwkYVLiaJafcBzQSCrg6GvRnUoeqt0J6d7MVrPfhVc0MaGAvZpDYaSmHWxlOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
بِسِنت درباره ایران:
کسانی که در کنار ایالات متحده می‌ایستند، از مزایای شراکت ما بهره‌مند خواهند شد.
تمام شعبه‌های بانک ملی(ایران) باید تعطیل شوند.
🎙
خبرنگار:
گفتید ترامپ با رهبران جهان تماس می‌گیرد. او با چه کسانی تماس می‌گیرد؟
🇺🇸
بِسِنت:
ما نامی از افراد نخواهیم برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70528" target="_blank">📅 21:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=vGYqnXMLm3XJuf1DuRajFOFPAeqkQKgkN6Pv8_5eWe1GiXW5BNoV_ZXuCt9T_1MTTcW3URK65cqa1Qz2nseAzrnjX8BJ9fgIckqSmK2N6jJnVHRlU1BebTdQbSoLcvtyUwGCqMDAHBrinssz0Iira_BJg322thIbtRNUnA-mCRPNCaXnCmmcU7FGhZrCIeBJHYzCwhWdbMQnOBy0hpvPnZlifFU6huAYx4Svex5QQUdbFR3WzH9AYJXhqxZ5WehC8voyJv-CCaGN8akA-8uzDX4v6ew1JZ3zJ_HlTjkU3U0mlDDX2FyTKeaGMI66-LOLI7YrQ8RPbdMqq44jbPm8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=vGYqnXMLm3XJuf1DuRajFOFPAeqkQKgkN6Pv8_5eWe1GiXW5BNoV_ZXuCt9T_1MTTcW3URK65cqa1Qz2nseAzrnjX8BJ9fgIckqSmK2N6jJnVHRlU1BebTdQbSoLcvtyUwGCqMDAHBrinssz0Iira_BJg322thIbtRNUnA-mCRPNCaXnCmmcU7FGhZrCIeBJHYzCwhWdbMQnOBy0hpvPnZlifFU6huAYx4Svex5QQUdbFR3WzH9AYJXhqxZ5WehC8voyJv-CCaGN8akA-8uzDX4v6ew1JZ3zJ_HlTjkU3U0mlDDX2FyTKeaGMI66-LOLI7YrQ8RPbdMqq44jbPm8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات «بِسِنت» درباره چین و ایران:
امروز می‌خواهیم به صراحت اعلام کنیم که هیچ‌کس از دسترس تحریم‌های ایالات متحده مصون نیست.
اگر آن‌ها تراکنش‌هایی را تسهیل کنند و بخشی از آن چرخه‌ای باشند که نفت ایران را به پول و ابزار سرکوب تبدیل می‌کند، هدف تحریم‌ها قرار خواهند گرفت.
⭕️
اکنون زمان آن فرا رسیده است که رهبران جهان میان آمریکا و ایران تصمیم بگیرند.
انتظار دارم تا پایان همین هفته شاهد اعلام خبر مهمی مبنی بر اعمال تحریم علیه یک مؤسسه مالی باشید.
🎙
خبرنگار:
شما این وضعیت را یک «روز دی» (D-Day) اقتصادی توصیف می‌کنید، اما «روز دی» صرفاً تهدید به تهاجم نبود و ایالات متحده هم برای آلمان ضرب‌الاجل تعیین نکرد. چرا تحریم‌ها همین امروز اعمال نمی‌شوند؟
🇺🇸
بِسِنت:
چرا باید بخواهم نظام مالی جهانی را منفجر کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70527" target="_blank">📅 21:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=OSlSMChp0AEHnrqammOVsoaWZI-fJs_uxPI-ZiHDK2PktBc9sPjEpHewqsjudA88j7tSJwG2U-Bze6IYwEt9QdWNSmXotcPEuEbs2YNcRJCZ5POtCMbstPdDxTVwWym_1NWAnDX2wn9GQIvgvPNdi06QqbSTjgSlGHiLJxXkky6SBuAFR4cmExaxsaS_XHAyJuzPo2RINdLpfo7yxAyKSsdiu095AOZGtu_6xzWW7sACvOlDdaN_B4YFD761TXwvI72kY1WgV6MDSYJvkJWW4A0QW6hu7qP4P8NQJEj1gjkrtj0DmYyUYCIj9Q6noayHTFVAh2J88-gixewr0KtnDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=OSlSMChp0AEHnrqammOVsoaWZI-fJs_uxPI-ZiHDK2PktBc9sPjEpHewqsjudA88j7tSJwG2U-Bze6IYwEt9QdWNSmXotcPEuEbs2YNcRJCZ5POtCMbstPdDxTVwWym_1NWAnDX2wn9GQIvgvPNdi06QqbSTjgSlGHiLJxXkky6SBuAFR4cmExaxsaS_XHAyJuzPo2RINdLpfo7yxAyKSsdiu095AOZGtu_6xzWW7sACvOlDdaN_B4YFD761TXwvI72kY1WgV6MDSYJvkJWW4A0QW6hu7qP4P8NQJEj1gjkrtj0DmYyUYCIj9Q6noayHTFVAh2J88-gixewr0KtnDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
«بِسِنت» درباره ایران:
⭕️
خطاب به سربازان عادی حامی این رژیم:
در شرایطی که پرداخت حقوق‌هایتان بیش از پیش متوقف شده یا به بهانه تأخیر به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشور را به سوی پیروزی می‌برند یا نابودی؛ و به یاد داشته باشید که دیوار برلین زمانی فرو ریخت که سربازان عادی تصمیم گرفتند به سوی مردم خود شلیک نکنند.
⭕️
و خطاب به کسانی که راه را برای تهران هموار کردند:
بهای آزمودن عزم و اراده واشنگتن را دست‌کم نگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70526" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70525">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=Zobqe673AHLdBkI691QYRPNw1RlblKm1KDKpFlYuRvB9QGNc_WOoJDNyA6gxhf96AOjR2OKkv-xNcgrx4uNkTOpI3vtBFeTgMun7XV2fnZLMwa7YTLb_bY_BvMaGqOmlykyETrwOrK4SKvLs7EMqxHmo_q5bpob-dTjA90g5He_-WCHsKxiH-8DD4RE2LDUIyBMeoR-u-nwp6wWqbl0QAFomrcsAYGEgw0c66KQOpFhuCovvLea0rT6-YxOs--tAMIip_X6tP0y-c2vVc33YN50lt8nr027ZKtYRSYiUiP8dkRXJl45ioaEjSvig84uhemMmPEQ6RSb1qdWnOs5hQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=Zobqe673AHLdBkI691QYRPNw1RlblKm1KDKpFlYuRvB9QGNc_WOoJDNyA6gxhf96AOjR2OKkv-xNcgrx4uNkTOpI3vtBFeTgMun7XV2fnZLMwa7YTLb_bY_BvMaGqOmlykyETrwOrK4SKvLs7EMqxHmo_q5bpob-dTjA90g5He_-WCHsKxiH-8DD4RE2LDUIyBMeoR-u-nwp6wWqbl0QAFomrcsAYGEgw0c66KQOpFhuCovvLea0rT6-YxOs--tAMIip_X6tP0y-c2vVc33YN50lt8nr027ZKtYRSYiUiP8dkRXJl45ioaEjSvig84uhemMmPEQ6RSb1qdWnOs5hQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات بسنت درباره ایران:
از امروز، حلقه محاصره را تنگ‌تر خواهیم کرد و تمامی منابع درآمدی احتمالی را که بودجه سپاه پاسداران و رژیم ایران را تأمین می‌کنند، مسدود خواهیم ساخت.
ما رویکردی را با هدف جلوگیری از هرگونه نشت (دور زدن تحریم‌ها) به اجرا می‌گذاریم.
ترامپ با رهبران جهان تماس می‌گیرد و مشخصاً از آن‌ها می‌خواهد که تعاملات خود را با رژیم ایران متوقف کنند.
هر نهادی که به نمایندگی از ایران پولشویی را تسهیل کند، از سیستم دلار آمریکا حذف خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70525" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70524">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75070defdc.mp4?token=Kci_MmMmxUbKNGPie34aw-Y1tmwrGJhu4PxrT4lLDK4RoEz-zX95iF0HNyfV0cxahfk2jKA-BJVx610VkWdqTIikTnpJo0i8HOG7mWgTyHpIGJAW3HpVOM4kzVCcShY4zTXjkgAF88WyKx4yTfA7c3pqGSdfMCRmTaUpfiesmeu3qmlf9EPLPIHInCtXJaoVOV4OccireDzbTr9QfGmQlQNgMP4jtYkOMfUOJChSzUdiISJEx9M9aqn16BCd0HZ-w-xTrjZWDzA8A84qAFPcbOaXjVEirNeC_WGRn8_iayQ6hk9818F6y0DUVSLFV23AIJ4jXy6VtA_dVXaQKvt5aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75070defdc.mp4?token=Kci_MmMmxUbKNGPie34aw-Y1tmwrGJhu4PxrT4lLDK4RoEz-zX95iF0HNyfV0cxahfk2jKA-BJVx610VkWdqTIikTnpJo0i8HOG7mWgTyHpIGJAW3HpVOM4kzVCcShY4zTXjkgAF88WyKx4yTfA7c3pqGSdfMCRmTaUpfiesmeu3qmlf9EPLPIHInCtXJaoVOV4OccireDzbTr9QfGmQlQNgMP4jtYkOMfUOJChSzUdiISJEx9M9aqn16BCd0HZ-w-xTrjZWDzA8A84qAFPcbOaXjVEirNeC_WGRn8_iayQ6hk9818F6y0DUVSLFV23AIJ4jXy6VtA_dVXaQKvt5aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
اسکات بِسِنت:
ما در حال آغاز یورش اقتصادی علیه پیوندهای مالی ایران در سراسر جهان هستیم.
هدف ما قطع تمامی شریان‌های حیاتی اقتصادی است که این رژیم ستمگر را سرپا نگه داشته‌اند؛ تا زمانی که تهران کاملاً تنها بماند.
🔴
در دوران ترامپ، آمریکا دیگر صرفاً تهدید ایران را مدیریت نمی‌کند.
ما در حال پایان دادن به آن هستیم.
ایران دو مسیر پیش رو دارد: انزوای کامل جهانی یا مسیری به سوی بازگشت به وضعیت عادی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70524" target="_blank">📅 20:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70523">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=WnVq8hD2cs8SR5eKhd-XMF3xtXeURlea8FerYyDkMh8iaV4uCRXF1UhMC6PMsqcxFX8kf4X3DfiD6Om3NQ6lSX8-gy3jTP7WfwXrbP1YV7zaPnQ0CVmjyEAHDYRI0ziyUVakp6OF1M7gXtEzn2jyLuQtMUUzLrN8uxYs8Y_3t31MuPp59WSE3kGCyO1Wew7eAYbpp-Pijj87gHaWHyY_9E7mSEDcDGkhzWMJQeNSiflDkuW408v6UTjFn3am6OA2x7mDrcU8cFmX8U8QOPOzQsI_jAx7R1bVnscfK5U9Kr11zx6UvvlBS3w9OWh6dJgUBY49_wSmqQcK0lQETNwW_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=WnVq8hD2cs8SR5eKhd-XMF3xtXeURlea8FerYyDkMh8iaV4uCRXF1UhMC6PMsqcxFX8kf4X3DfiD6Om3NQ6lSX8-gy3jTP7WfwXrbP1YV7zaPnQ0CVmjyEAHDYRI0ziyUVakp6OF1M7gXtEzn2jyLuQtMUUzLrN8uxYs8Y_3t31MuPp59WSE3kGCyO1Wew7eAYbpp-Pijj87gHaWHyY_9E7mSEDcDGkhzWMJQeNSiflDkuW408v6UTjFn3am6OA2x7mDrcU8cFmX8U8QOPOzQsI_jAx7R1bVnscfK5U9Kr11zx6UvvlBS3w9OWh6dJgUBY49_wSmqQcK0lQETNwW_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
اسکات بِسِنت وزیر خزانه‌داری آمریکا:
امروز، وزارت خزانه‌داری ایالات متحده «عملیات طرد اقتصادی» را آغاز کرد؛ کارزاری بی‌سابقه علیه جمهوری اسلامی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70523" target="_blank">📅 20:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70522">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhgBs3Oh7QLI4D_yTmrA-kljnc0JJjQ8fgPaEkrpdzho2WV6aAR53Tv-aQSmuoHiJrUULbAQ_y_UF6jfuD2t7V6hSKP_VtbIa9g7hEcJ6K7GUSeaxuSarm5DGGqILqqj4Le19xZuLSrd4KUFKfylA_PjFGTXvQ3qmjFjddBMxH_3NZ_AnDyrjlFfLlhmmcfiE_qqrBWY9FbbKLs6zm_OpSqO_7keegINA9Zi1p2C16QOh--ueIMk3riqe1ZFLN0BcJe4F1GwRMzIfgzID75G9iyJNm1BVLgL3L8xysyO4D9ILYCePfUvga8CN8034DnLuiKFGOoIi7wuGrSm7oHvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو:
ایران تلاش کرد یکی از پسرانم را ترور کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70522" target="_blank">📅 20:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70521">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Smkz8Ob1lEcp0Frz_bKnLb2Ga5XwRZRGRXzAG_sGzEvdrp4l4YMYJ4kGkO7EAqvouP52R7wbnH0-pcNFd7LJVaRBXPK_C3wG49fIuwnbEs4IERB_koCLrPyZjZz-tvXibadeNw5SzaA1DkoGLH_fs0aQA-f6LUMgve5xOO0nEI4Jy-JtotHeCnGX7ouUYZSSsLYv_9QQogdzOjnE69Cgqq7tJpHusxR8RQmjnrWQHzU_x4RsxDQhVKZH5ey7A5Ce1dKXembcDiCcnUMZvXLsHfWoDc307umCpQmH07fr0CK01teDKo5uGnpSBBykYw9Ep47FFuRUpH_ZnNV9L9V-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دموکرات‌های چپ‌گرای افراطی با انتشار نظرسنجی‌های ساختگی، دیوانه‌وار عمل می‌کنند. آن‌ها این نظرسنجی‌ها را در سطحی بی‌سابقه منتشر می‌سازند. این اقدامات «عملیات تضعیف روحیه» نامیده می‌شوند؛ تلاشی برای دلسرد کردن جمهوری‌خواهان تا پای صندوق‌های رأی نروند.
اما واقعیت نظرسنجی‌ها عالی است و روحیه مردم کشورمان در بالاترین سطح خود قرار دارد.
⏺
ما در حال پیروزی بر همگان هستیم، از جمله ایران؛ کشوری که در گرداب مرگبار اقتصادی و نظامی گرفتار شده است.
از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70521" target="_blank">📅 19:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70520">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDB7zOKOF67tVDjQ27lSyedg19st9ZVK4WCySIoYeNHG9X2ARlUKCSgC6MPuI-y4mgZ8Lx-F0oCoQk45iXFda3tiVnWYNn6dQ5zYOqYwJf-wBhqVLwwtXTaouxJYuNogpkALciohE1z32HjEjwtOSC7ZqoQCQXC2BuRFf_SsA7mDMeANx4o3_EtSCzeu64pxkAs-bgsg2QZiCWJoWkPc2OjqbUBxVsnibX_AbDfO4C35_d5dbgroAfVTZiyNY4uksZMoiXSUCHve15jEIBUpniWS0MOncNVMk-pGyj4W_MZpHF3pcV9hieZHAPb_aIcoELFludBvEGtWG1gEesMyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
قالیباف در دیدار با عاصم منیر:
تعهدات طرفین در یادداشت تفاهم روشن است و این آمریکا بود که با بدعهدی مانع برقراری ثبات در منطقه شد و دلیل دیگری برای بی اعتمادی به این کشور ایجاد کرد
رئیس هیات مذاکره کننده ایرانی، ضمن رد تاثیر پذیری جمهوری اسلامی از فشارها، تاکید کرد: ما پیگیر اجرای شروط یادداشت تفاهم هستیم و این امریکاست که باید به تعهدات اش بر اساس تفاهم نامه پایبند باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70520" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235f69fa4b.mp4?token=bd8q4SWnI_OJLo_yS2Dpv95Cvf6YHif-3fV_OU8zxLD6A6MARNfEmCgxUaH9Vte3p2BeN8JERJITggAijOxtf97Okbq_NLpGdX7E-4Bt-BKqK6kX9p77J5Q0pmphWny8Ku0p7OlDYND0BOvEG5HVwSY6Dj2V46DHC5cK_xOfn78yNzYxO9vvCspNS7UYZbXS5KY4HV-tG1V6Phwlk_EcGp4y_d58GPy0_medRh53HeEqTRAcSxC6wmDK2TdtiMKtbqK2yvBYOUWSTPCjy99NKQJS1fTELM6XlI1HzUecDcXr-djW1zzVRXJO7xo68Vgzg2Xk6wFq2g5gbnxRvCN8mjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235f69fa4b.mp4?token=bd8q4SWnI_OJLo_yS2Dpv95Cvf6YHif-3fV_OU8zxLD6A6MARNfEmCgxUaH9Vte3p2BeN8JERJITggAijOxtf97Okbq_NLpGdX7E-4Bt-BKqK6kX9p77J5Q0pmphWny8Ku0p7OlDYND0BOvEG5HVwSY6Dj2V46DHC5cK_xOfn78yNzYxO9vvCspNS7UYZbXS5KY4HV-tG1V6Phwlk_EcGp4y_d58GPy0_medRh53HeEqTRAcSxC6wmDK2TdtiMKtbqK2yvBYOUWSTPCjy99NKQJS1fTELM6XlI1HzUecDcXr-djW1zzVRXJO7xo68Vgzg2Xk6wFq2g5gbnxRvCN8mjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🟥
فاکس‌نیوز:
در حالی که ارزش پول ملی ایران به پایین‌ترین حد تاریخی خود رسیده و تورم همچنان رو به افزایش است، کاخ سفید آماده می‌شود تا آنچه اسکات بسنت، وزیر خزانه‌داری، «سخت‌ترین تحریم‌های تاریخ علیه ایران» می‌نامد را رونمایی کند.
ایران تهدید کرده است که علیه کشورهای حامی تحریم‌های آمریکا دست به اقدام تلافی‌جویانه خواهد زد؛ این در حالی است که فرمانده ارتش پاکستان برای تلاش در جهت احیای گفتگوها و میانجی‌گری برای دستیابی به توافق صلح، عازم تهران است.
همچنین انتظار می‌رود وزیر امور خارجه عمان برای انجام گفتگوهایی با هدف کاهش تنش‌ها پیرامون تنگه هرمز، به ایران سفر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70519" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بزرگترین کانال پیشبینی فوتبال در ایران
🔥
g2
فرم های ما رو از دست ندید...
⚽
@Tabanii_Mafia
@Tabanii_Mafia
⚽
@Tabanii_Mafia
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70518" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4mPGXTG32kP82k132HA0QmeRACtDAzwueNSkGGzQqYzgSySTjf8eTF-KiNBr6OiX5lbveeyz9xC6R7_748UCNb6SuWeVEm026Mo0apywMNts5XShVQcSZ6uprWh-qlJNSwlAkTgbocztjmZWbA9Vye9Hyw2SarU5bhBR5Eb3pog81QtlA4Yl_aqEj6f_W67YyMnz7oArVBMivsyZCd4YS8Q5XZb8m1HFIWGYLPOkDVKiHGC3TH1qo1I3y3R44r_1DTmGQqcJXXjilL-aeMzUPzAMTYYNxJh6EjMq5VlWPddrzBJynccCzBKULMfdoofME01gGaIwEL6vTb9sF54Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70517" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384afb6ff9.mp4?token=NO5toEvZblxHmQ977itH6Zwk1xrBTPd-jS_I0Aljzw8mGRfMFFNAXJLQWKO3J6sjNhkdGe3kXhnNk3n5fJNpdMYvo-GeKSDNfhh5C9_efSqxUCUrqs38CERQD0Dqlxjs4VQMlKlLiEYgKziRJmAoUA5h2txiUWo8Bq9IYMgVE6UU1oNxnFiPULJBp1Jnb2E4mAw70ly4jR74XPkXzqS5DvqjIPPkbm_sdtFXCBqL7wJfMSjS-_CgUOHxKpfO7iGMPBLu4fLX1KtwgnzutyYokKeOl5xLN11_9vMvtHjwtL4NVfp5w5nUMLnbzS4GCkWiW8ikAcj48a3XyTK0WHbgrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384afb6ff9.mp4?token=NO5toEvZblxHmQ977itH6Zwk1xrBTPd-jS_I0Aljzw8mGRfMFFNAXJLQWKO3J6sjNhkdGe3kXhnNk3n5fJNpdMYvo-GeKSDNfhh5C9_efSqxUCUrqs38CERQD0Dqlxjs4VQMlKlLiEYgKziRJmAoUA5h2txiUWo8Bq9IYMgVE6UU1oNxnFiPULJBp1Jnb2E4mAw70ly4jR74XPkXzqS5DvqjIPPkbm_sdtFXCBqL7wJfMSjS-_CgUOHxKpfO7iGMPBLu4fLX1KtwgnzutyYokKeOl5xLN11_9vMvtHjwtL4NVfp5w5nUMLnbzS4GCkWiW8ikAcj48a3XyTK0WHbgrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن حاجی‌میرزایی، رییس دفتر مسعود پزشکیان رییس دولت جمهوری اسلامی، از قطعی بودن کاهش سهمیه‌های بنزین خبر داد و گفت: «افرادی که بیش از سهمیه تعیین‌شده بنزین بخواهند، باید آن را با قیمت بالاتری خریداری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70516" target="_blank">📅 18:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70515">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a8609222.mp4?token=OXlV0xC_0iBWixc_hhNjkkl49susOQ_7A7ys-s6f7WoiYVJTW2IrfHbQQPEzqMs-yzANS1wGLJh__xOCcsC1zzXCS6JqNaCD2lHiWEtzefo1QE3A0-aMEF0k0jvt1aa2XMC6oInX5yi1SFCU-uIJDK5mABvccNKX8q-hgplYx58y8o0ekNmHgHKlxwF4fG4FrjHPJLz7hUOqFeDvpkIz1GQXdd23EpSaOXbb8yBWHIVzfW9c2svNye14uyN56twLZSepb3bnWwr-BaWu2bdhqW-a77xnZWPLgjF2jw9cVp8NWy7nyWlEu54I4rOQcPIAzy0hvvJ-p5SgU1SxFF-Ztg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a8609222.mp4?token=OXlV0xC_0iBWixc_hhNjkkl49susOQ_7A7ys-s6f7WoiYVJTW2IrfHbQQPEzqMs-yzANS1wGLJh__xOCcsC1zzXCS6JqNaCD2lHiWEtzefo1QE3A0-aMEF0k0jvt1aa2XMC6oInX5yi1SFCU-uIJDK5mABvccNKX8q-hgplYx58y8o0ekNmHgHKlxwF4fG4FrjHPJLz7hUOqFeDvpkIz1GQXdd23EpSaOXbb8yBWHIVzfW9c2svNye14uyN56twLZSepb3bnWwr-BaWu2bdhqW-a77xnZWPLgjF2jw9cVp8NWy7nyWlEu54I4rOQcPIAzy0hvvJ-p5SgU1SxFF-Ztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو ماهیگیر جنوبی موتور قایق‌شون خراب شده بود و چندین روز بود که وسط دریا گیر کرده بودن و دیگه جونای آخرشون بود
که ماهیگیرای عمانی دیروز دیدنشون و جونشون رو نجات دادن
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70515" target="_blank">📅 18:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=nbKwZii_H7bi9xg_gD1vyLiOHfhZYXXGtmUeQ8OfKwdfRnNkQawiBqLReU5T9srWSgieCLL4t425ARClzPYgZxyXUzxDqvoSOJ4ZeKPdoFqv3JWvMddmqmCtDDPMPooOgMz7inHUnKQWjmd6VCR8483at3sSV0ckQryX94-eS42rr_Lka45Ug7RDlJeUlO0zJFm8DQ0IaB5QYQq0IJLtQi_Aa4hh_FQdN-2vZZ8FIOVMiCLiLuTfIQvpvbzmin6xfAYoT6s0_xmAVOGBT45NhG7gUuKru8ONOyI4BMgvZjsyVm2ix0AlhJixGm53pC9Lg9s1pKGmFmy8HXNhlH_lUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=nbKwZii_H7bi9xg_gD1vyLiOHfhZYXXGtmUeQ8OfKwdfRnNkQawiBqLReU5T9srWSgieCLL4t425ARClzPYgZxyXUzxDqvoSOJ4ZeKPdoFqv3JWvMddmqmCtDDPMPooOgMz7inHUnKQWjmd6VCR8483at3sSV0ckQryX94-eS42rr_Lka45Ug7RDlJeUlO0zJFm8DQ0IaB5QYQq0IJLtQi_Aa4hh_FQdN-2vZZ8FIOVMiCLiLuTfIQvpvbzmin6xfAYoT6s0_xmAVOGBT45NhG7gUuKru8ONOyI4BMgvZjsyVm2ix0AlhJixGm53pC9Lg9s1pKGmFmy8HXNhlH_lUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به تازگی توی بالاشهر تهران، یه رستوران ساختن مخصوص شوگر مامیا.
خانمای میانسال جا افتاده و پولدار اینجا جمع میشن و پسرای جوون و خوشتیپ هم میرن اینجا، تا برا خودشون شوگرمامی پیدا کنن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70514" target="_blank">📅 17:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CXlcm839mE_7oXPWD_ZAFXhhenAQmJm8aY30PseWB-Rx4Ec_tcVqwwL6b8mCfzpRm2ddPBmXlgHLb8bM8iQQHqvwfkeDeNdjsFCynDu46BtcCl2xjWLBZqV6jdAyEqJafhYRur-MYOCgdczn3X5BDfOGZ3kRVifSi3EWCW7K0lhJYTgUIJ9J4Tq5VCQHRDyKaK8BWDO2X8oKunygkp1TX3O88zx8bFLeIH13EiDNEDag5tTSSN334gGqiaAasusUtwj8M2HZBCVHMwF4WmZ9ofgDmIXnOAttf2NoUoTAEr2qLV_DCsn0IGM4gMEG70M66PNWRiOoX20677DzsLZp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قطع برق کمیسیون انرژی مجلس،هنگام بررسی علل خاموشی‌های اخیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70513" target="_blank">📅 17:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX_0qksqb4AzSTs2wUQpWwRu6MSukXVe-eNmPMEW4oadOJh-UxkEpi8sjozQgynv5Wq_H1kVR2eUG2-Raxh2UC1yxsQ5DZPbdDj90Xk-UvHpTCG1JY6KHom30sNk_bVQang7iMlZEvKmcOvZLjpwi28npTJwe8mdn_KA2SufqqRJKGCvk0LkSkIOZViSbttc6P8xD7TgHkrrze-6jOCYw_BTzfqoYd_wKWUzIZ8sLd0qLQz1UNRPzIicdck3OYPTIyD9YFC6aHbJGiCUGN5toanX44IRRsZSfXgnz3hou-evnH3r6YaKBqmzJ1Y5DDDnWVQfXeSKd4SsvE_2WuhDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ
:
ایران به طور کامل در حال فروپاشی است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70512" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70511">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98f13e516e.mp4?token=ax4NTl50WKrayxH1WGmWaDruLSYzBAYoqtPqFOvHrScvEffzevabf1ddAUcGm_i82fK3qjdIdmI4vSIxpf4lXVLVTekVYKUM52oleCQi1PwDu52p8F85-Bf8FcjtlUJ1BnCAPDixgPg1l8VNVJrBvciX8UdnsJZyfNpvndnBbc4it-niR7K8KPPQdsesp8oRVfd6WzhB-EO1hTNxIs-0zhNs9mrNcGsjUkrzpXX19zZ7IjKEunsANnaeni7yotL_U558BBd90LA8HHRQkprBIqi8QmlPeF9-g3CaeMVVd8pXJsKzHfuxI8DTsDXbcrZobatZ2_Afr82D_ptiIRH6LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98f13e516e.mp4?token=ax4NTl50WKrayxH1WGmWaDruLSYzBAYoqtPqFOvHrScvEffzevabf1ddAUcGm_i82fK3qjdIdmI4vSIxpf4lXVLVTekVYKUM52oleCQi1PwDu52p8F85-Bf8FcjtlUJ1BnCAPDixgPg1l8VNVJrBvciX8UdnsJZyfNpvndnBbc4it-niR7K8KPPQdsesp8oRVfd6WzhB-EO1hTNxIs-0zhNs9mrNcGsjUkrzpXX19zZ7IjKEunsANnaeni7yotL_U558BBd90LA8HHRQkprBIqi8QmlPeF9-g3CaeMVVd8pXJsKzHfuxI8DTsDXbcrZobatZ2_Afr82D_ptiIRH6LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه واحد 131 متری تو ولنجکِ تهران :
131 میلیارد تومن
🇫🇷
یه خونه ویلایی استخردار 1080 متری تو فرانسه :
130 میلیارد تومن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70511" target="_blank">📅 16:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70510">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/685fbb8085.mp4?token=nCkQTKI7N-ZGURZDnw3QbrtsWlpCl0SKz27xNU-CbDme9ibOcNQ4Wb6bXKgTs4eFb2apM6exichy19C2fVZ5FmE3PyBFIczhRLEdgjvOG0LsLTb2N6qh2Z_J432tWBC9DhTyT5YxHY-exfQES9q1i1ysatcjYgkyk5d1E-KD0-iOufCYHR_eWBQcpod3BY1ZbyaxLWEVxLv-PH1XnDts4DU8wtSphTNnFu4dbzhFpkhP1t1rZY3VwPgqQfumBxrCWUePZJIDaggrakApXX4lih2Q3SHWP4eLYLzfNLvkXMCNCqnZ4UKySSUISUQNNZ25Pf7vMYkrcdxuM6mTRimg2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/685fbb8085.mp4?token=nCkQTKI7N-ZGURZDnw3QbrtsWlpCl0SKz27xNU-CbDme9ibOcNQ4Wb6bXKgTs4eFb2apM6exichy19C2fVZ5FmE3PyBFIczhRLEdgjvOG0LsLTb2N6qh2Z_J432tWBC9DhTyT5YxHY-exfQES9q1i1ysatcjYgkyk5d1E-KD0-iOufCYHR_eWBQcpod3BY1ZbyaxLWEVxLv-PH1XnDts4DU8wtSphTNnFu4dbzhFpkhP1t1rZY3VwPgqQfumBxrCWUePZJIDaggrakApXX4lih2Q3SHWP4eLYLzfNLvkXMCNCqnZ4UKySSUISUQNNZ25Pf7vMYkrcdxuM6mTRimg2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
ما از قدیم شطرنج باز بوده‌ایم، در سال‌های اخیر پوکر باز هم شده‌ایم.
الان هم مدتی‌ است که ترکیبی بازی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70510" target="_blank">📅 15:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70509">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9pYzEMjfiDC1c0kVnQWESvI8WoGHRXrTZB_-KMeRVlcwKMRY1atyitIO--Yy99MG7XHAM0Tv0U91y9g3YYiZ2PNfQeIpqeznal1zQYBHPxrE0rnMMgmYjjSYX-tFYDbPkt0h8zA15HGF4q_9WphxuKqTI8KUfcMYE1kJavD5_V5gViZrFOo-F3ImwKioHWyO-aW66LdSo5WbVoJDsaCuYN5Qsa663jblHR9ODAVJAgD7gpz7bRDZtMmI_fj9QKZN8FYGTi_Q_VAUJ5d4UphOtwWzdZnfLpi7-7g9OcDtnjhqTBYUvIzR4v63TYJvgwPUfKJEiuWKh9x_Z9Oh68Fsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇷
ترامپ در تروث؛از قول رئیس مجلس ایران: «گرسنه‌ایم، نمی‌توانیم دوام بیاوریم»  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70509" target="_blank">📅 14:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70507">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8XWnj-MeMsHRwmJbagCVl2FiU_6Z6Hnhh2_mmfJ2-83hY2KL0sLulf2SxWh5HLh0Q9ehWh-Ix3VK94ArSy33um8odxSoAUEYyr-2h2et4z_RGSRFr-d6_ElhEeXHAk0-ZaZZqVnx7aJctYNTfjXVD-XVsz6W3j3Nhl7N971hOmIRWMmcagzeLzAkE6gzG-y4GXoqObVk0EiqjBJ4L4GN9DpDfg6yL8m76ZEv8dapV-CXhnFetfBNjMpO27gmynIeultSwEbrhpDudkqT6H6Z1yr8CNJg-pMeug8afeGiN5DpHjm45YrRx6zZMdrCJ8xqg7BD1UUy6Q-uHCQxKPm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7684c0f69a.mp4?token=lsT9wOHu2T_wEPX76gMKoblAgzgA_apZWl12natfVYslH2P2YXfnWwRkngTyIFyOXu3tFulvizH5C0Ok87-7EmJoKvbc0fnINCHgBNE9zd73fjOSphTU2L8FWmObf7_5JdfpYOMUkc0FNWdeipbso0gflKU9EgnvK4Br6pu3X3gY8II6cbHEDlHQAv8fMi3s4xvKkHCtpH5wyOFGHRn5WadxrQr2i3VjyhN7swlpFVgpj57663j6OeCYgq0Nrs91TZPjSnqv9eWOcBrPkb5U_BWglh8xE7AjXe_I80MPqeSAYV5bbYJ3RkrO6bSoJi8Us7pFxDxb-M90RPo6Sct8Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7684c0f69a.mp4?token=lsT9wOHu2T_wEPX76gMKoblAgzgA_apZWl12natfVYslH2P2YXfnWwRkngTyIFyOXu3tFulvizH5C0Ok87-7EmJoKvbc0fnINCHgBNE9zd73fjOSphTU2L8FWmObf7_5JdfpYOMUkc0FNWdeipbso0gflKU9EgnvK4Br6pu3X3gY8II6cbHEDlHQAv8fMi3s4xvKkHCtpH5wyOFGHRn5WadxrQr2i3VjyhN7swlpFVgpj57663j6OeCYgq0Nrs91TZPjSnqv9eWOcBrPkb5U_BWglh8xE7AjXe_I80MPqeSAYV5bbYJ3RkrO6bSoJi8Us7pFxDxb-M90RPo6Sct8Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💲
❤️
ثابت نگه داشتن قیمت دلار درطول ۲۶ سال حکمرانی شاهنشاه فقید ایران
💵
قیمت‌دلار
زمانیکه تحویل گرفتند: ۷۰ ریال
امروز بیش از ۲/۰۰۰/۰۰۰ ریال
یعنی ۲۸/۵۷۱ برابر!)
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70507" target="_blank">📅 14:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70506">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3317e927b3.mp4?token=hHUCoGnw2ocznQM6hW9rW0fBJhRvtFOcg3i3RLwBJRaZkYXrEmitNsO7K_nGgVHHikLD1_MN6SgBFQzuB5fvpOjp-OFaYGP6Wbx9_qd4A22JwMfIuE9IqRuMeE_8c4l9TOtpkAMTIoIaPITE-vQbkSLCRRXYXZ7cld4_awwWigcq1OepKjrkxUHbXzyS9i7ClzWxkCpcb6dy3gEkfTJDnQm9UTmXrbSjdh5NLjBn27LKr2eLDsasDBqbz3WxFV_jXVTPA7klwNaeX7L7HHnbUcPnmJRmP0U9D-Kf4c32v5X4iHgJorbKfTnd7IYPdrbSupymu3tHPPkPLbO6B2D61g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3317e927b3.mp4?token=hHUCoGnw2ocznQM6hW9rW0fBJhRvtFOcg3i3RLwBJRaZkYXrEmitNsO7K_nGgVHHikLD1_MN6SgBFQzuB5fvpOjp-OFaYGP6Wbx9_qd4A22JwMfIuE9IqRuMeE_8c4l9TOtpkAMTIoIaPITE-vQbkSLCRRXYXZ7cld4_awwWigcq1OepKjrkxUHbXzyS9i7ClzWxkCpcb6dy3gEkfTJDnQm9UTmXrbSjdh5NLjBn27LKr2eLDsasDBqbz3WxFV_jXVTPA7klwNaeX7L7HHnbUcPnmJRmP0U9D-Kf4c32v5X4iHgJorbKfTnd7IYPdrbSupymu3tHPPkPLbO6B2D61g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدحسین عادلی، رئیس اسبق بانک مرکزی و دیپلمات سابق:
بر فرض که در آمریکا، صف بنزین تشکیل شود، چی گیر شما می‌آید؟
اگر فکر می‌کنید در آمریکا صف بنزین تشکیل می‌شود، باید بگویم که نمی‌شود
چه خواسته‌ای داریم غیر از موارد موجود در یادداشت تفاهم؟ کاخ سفید را حسینیه کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70506" target="_blank">📅 13:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4e1f5587.mp4?token=chNYCp7tZY27bMXAYxUVHWbijBSkLefjFKXjk5hIb_SyfpAXE7Gdspx40PiKQOgSbYrblKLI0bSuaeuM-ZyW9I5BjEdUxt7wI7AjVg3ZwQHxdhMdQjj7NbbrVZIo9tdupir2RGJbnsHYGYIRI8_DBbwRT1oSmfInBc8IkNw2ylSq0wt8UkY6QdMCSMnbC50PHydx4bl4dyDRO2fgswyP_dnMzF63wEzSV8Jt0YldFAikuMn5k7vmKQr_twMao4v22JkA-m_vKCtbhhPWi1BCntTAuGid7iH-coCsCo1G0sF5HmbGkpns-xS5RJXPmXHAmlOg5ep5QHX7u92rNoj4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4e1f5587.mp4?token=chNYCp7tZY27bMXAYxUVHWbijBSkLefjFKXjk5hIb_SyfpAXE7Gdspx40PiKQOgSbYrblKLI0bSuaeuM-ZyW9I5BjEdUxt7wI7AjVg3ZwQHxdhMdQjj7NbbrVZIo9tdupir2RGJbnsHYGYIRI8_DBbwRT1oSmfInBc8IkNw2ylSq0wt8UkY6QdMCSMnbC50PHydx4bl4dyDRO2fgswyP_dnMzF63wEzSV8Jt0YldFAikuMn5k7vmKQr_twMao4v22JkA-m_vKCtbhhPWi1BCntTAuGid7iH-coCsCo1G0sF5HmbGkpns-xS5RJXPmXHAmlOg5ep5QHX7u92rNoj4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو از کنترل خارق‌العاده با سر و گیتار زدن تو ارتفاع دو جوان ایرانی، حسابی تو فضای مجازیِ وطنی و خارجی وایرال‌ شده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70505" target="_blank">📅 13:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70504">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⏺
🇮🇷
🇵🇰
تسنیم:
عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشور وارد تهران شد.
عاصم منیر پیش از سفر به تهران با ترامپ رئیس جمهور آمریکا گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70504" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d7db3b25.mp4?token=PzfgYzESVPTNeSiQKyJJfiUMm66oleem4JbF0PkZiEXai27_DB3yoR581jMqsx7ye8gTs9N7RbI5jzFcdDKIbTtGCjgl1e_Yv-DerwDh-UWHee1CWvHbh79YHQGKT1vGrImbVndXBq86AR56JrSp3QAAtkOql_4ZJ0vdw1x5QSg1ZDN5Ng5HtTOPYQv47kN1s9E95cikVJK69vSZWPDwir-Jlaehf36zcnhtsmZ06LnuHR__ZLeUB1oZvVBv1hCwenRO4bjmDiL3UHebLthONsHaOgfTpGLcckqYf3uKhhUFvGU44_bgKNrtuSLWzBQ6QWjLwmJbefKcasGGuip3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d7db3b25.mp4?token=PzfgYzESVPTNeSiQKyJJfiUMm66oleem4JbF0PkZiEXai27_DB3yoR581jMqsx7ye8gTs9N7RbI5jzFcdDKIbTtGCjgl1e_Yv-DerwDh-UWHee1CWvHbh79YHQGKT1vGrImbVndXBq86AR56JrSp3QAAtkOql_4ZJ0vdw1x5QSg1ZDN5Ng5HtTOPYQv47kN1s9E95cikVJK69vSZWPDwir-Jlaehf36zcnhtsmZ06LnuHR__ZLeUB1oZvVBv1hCwenRO4bjmDiL3UHebLthONsHaOgfTpGLcckqYf3uKhhUFvGU44_bgKNrtuSLWzBQ6QWjLwmJbefKcasGGuip3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی نزدیک از ظاهر موشک تاد و پاتریوت؛
موشک THAAD: طول ۶.۲ متر | قطر ۴۰ سانتی‌متر | وزن ۶۶۲ کیلوگرم | سرعت بیش از ۸.۲۴ ماخ | ارتفاع درگیری: ۱۵۰ کیلومتر| ارتفاع درگیری داخل و خارج جو | پیشران سوخت جامد | روش انهدام Hit-to-Kill | هدف: موشک‌های بالستیک.
موشک Patriot PAC-3 MSE: طول حدود ۵.۲ متر | قطر حدود ۲۵ سانتی‌متر | وزن حدود ۳۱۲ کیلوگرم | سرعت: ۵ ماخ | ارتفاع درگیری ۴۰ کیلومتر | پیشران سوخت جامد دوپالسه | روش انهدام Hit-to-Kill | هدف: موشک‌های بالستیک، کروز و هواگردها.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70503" target="_blank">📅 11:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70502">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7ee8a017.mp4?token=LqCOVuEvWqT4ZUPArrIYsWob6xVm9zaFnewvSgNE68zG0JaE0rsyaJ9Lqi04HFcJHLErn6ir3LJ3bfIqRt_rcgHeOTCwyQ6gCrn7ywtHNw69hpoXKMn67yxQtUyQMGGWqga_Jt9M8wDl-rGpEssGnZ6-PNChRBsucx3x8Iyt-Lk0S6rWL5UF7Y-kNm_y6kx0jw2dLD726J5NLrkJ4kjaRyQsZkX1Hm-Mj-nCbdw_VkNE5CUDRDn_4kewo402c85yLfEHNfoAE8UIMGvsd0OdTFmyFGCAzSuH67oB7IkXXzmNaiYjXODZ6ckC9asxo16236deVSjtOmH1kpK_OmpUdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7ee8a017.mp4?token=LqCOVuEvWqT4ZUPArrIYsWob6xVm9zaFnewvSgNE68zG0JaE0rsyaJ9Lqi04HFcJHLErn6ir3LJ3bfIqRt_rcgHeOTCwyQ6gCrn7ywtHNw69hpoXKMn67yxQtUyQMGGWqga_Jt9M8wDl-rGpEssGnZ6-PNChRBsucx3x8Iyt-Lk0S6rWL5UF7Y-kNm_y6kx0jw2dLD726J5NLrkJ4kjaRyQsZkX1Hm-Mj-nCbdw_VkNE5CUDRDn_4kewo402c85yLfEHNfoAE8UIMGvsd0OdTFmyFGCAzSuH67oB7IkXXzmNaiYjXODZ6ckC9asxo16236deVSjtOmH1kpK_OmpUdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محیایی، معاون هماهنگی امور عمرانی استانداری گلستان:
تو استان‌های خراسان شمالی، مازندران و گلستان توی فصل سرما، قطعا بین 60 تا 90 روز قطعی گاز داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70502" target="_blank">📅 11:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70501">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70501" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70501" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70500">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqQNVzuV5CLzfjvKBt9HUjg2iZaVZsNBJ3Huj7QjmvxOZPmgj8uJWv5a9QwROiyOXK1ATjfDFFNpPqjxRzq-e14zGLHnBjZA7BYIMCAvRPYaE5gAJKJJy49TuioETZOPbVWK6EmuYgBP_4mbD2Idxi9GhEMtkEZR3kr0pVBc28CfEqCFA5o6jhEheJOjd4n44opanzMLXbyoZZ8jgMTILKNKd-IWKtwWyI70fTf_O1kjM4fNJ819eoeh4oMN8FqvsVpkgY8dQhpkVWYmnHU3WbvchiO_X3Dm91V_ubjPpRwwWCDuDnBquVgkcfFiJrkRlDHzNzZjEmrC-CrPsQHCyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r2
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70500" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70499">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDzPG_KO--PvQPKx8YoPpndg_ckmeDvo7F-H_2Cn5-2oqVBKZvWkKts8KHfoZsX1-S-azMa3X10EEdQuRvkU6E4dCoIvuwh4AFhpYaZkZ1-67rPK2Wr9PZCJNLEVAaMjGgnhMaaokdCjycX6IhBzirEl3rAd6A6bQDM6S3NQP5nAGB65vC5hN9iK73NQDDEHRpPuxDNnBhndexR7Ss5_08L0T7PbPLdP2MUtM0HAVo1ZwPJy8Jr0gL3B4xpqNV_Sxmuj1QDfyrJzg2eNsZBHiWQH5hQ8bdLDVZwTZlhZjAIKv8i-uJF4wKYYNJpnRps3wUqLjJ4xUslEzFwxRYHSEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇷
ترامپ در تروث؛از قول رئیس مجلس ایران: «گرسنه‌ایم، نمی‌توانیم دوام بیاوریم»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70499" target="_blank">📅 11:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70496">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJq7SuT4AeOuhFhYZd9FzcLQ6xzQCIIEVSdilw9TN-adxOiG0jJjpDfBACgpC7sXKez-423tAXueU3Cg4Lm7Thh80KtegCEb_6dSXEhS6f5Anu-WdeqkjWe_F07mio7YmTBlml1ybxdzM5PGB51bgUjfxCQkjCN_QFyx1PCpEwOC517sFVK3VBDvgcUSjURq2c9Cg9x1ybcXwE2zk79udkwmAdCeJ2Y_lYezW1oYcMVDV8jwB7eIqS7Ja5p3Zs2uSe_VLUNwaUJ1n_8srZHzvMFIVkBHnB8PnkYp3fNZLNxcj3t9vxkc4cXl59uYx0Miv8uGV_bljvqh4HYeMKnkYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swNF2ldtva5nh4bjewUx5XM8jwXQ0N6KQ_12Fa3-cRTR_2omM8mFKZBhqsTKhMctZlRbVaif5YXLUeG60oK4aZJaMcCamjewOYcyokaqg4MQHp1o_rG505rsosLRkIqYEPE7JnPw8ov7tSuA4ZhFxf51HUBRBXvJB6zoqYuClvSo8ILHXcu5C1JMCPDjDZ_x4iA8pm4YfTZj_wRKHRRZefl2xyIpl4ks02q18BcQIEvzjpWih1U3R_gA0EeNJDQ-TcObW0q2bn6RDZ-cw9K_7HnZ5ce2eG_mPPDmq--_Pu5o7cvKQUHv0RsDrWp_IGNITZ-oOyd5wss96HvNG9-Kjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73af71539f.mp4?token=KtUvu2Ai-j2lo9zOjeH5YZcSvnxCw-lCwQQkVq0Cv1bysF_KNljjPW4YXb6xE2J9vYJe7IToHSPk3JmaG9UiuLrMXzu4dviIi_LnENJLjTaZpIEmngEJeipbD57fN2Ag4Zh_WenyrKhOVg5hwsVykwOnkAhnwj0w3X-gzUCvrto6MzZJw4kCPKFRdAAmaEx67J5olpj2DyZi3y1TnAfZj9b_i-S_cyP3ajpk_4eXWWQp7NKW3_0DsvDelijYeoRb897hr6c5cqKnLehNY2NedCW0bn6Mz2DK5vQD_umbF_ec0uub8rg7fMOBg7r7XO-YdPVjhRFy-M4SVa79oYkLBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73af71539f.mp4?token=KtUvu2Ai-j2lo9zOjeH5YZcSvnxCw-lCwQQkVq0Cv1bysF_KNljjPW4YXb6xE2J9vYJe7IToHSPk3JmaG9UiuLrMXzu4dviIi_LnENJLjTaZpIEmngEJeipbD57fN2Ag4Zh_WenyrKhOVg5hwsVykwOnkAhnwj0w3X-gzUCvrto6MzZJw4kCPKFRdAAmaEx67J5olpj2DyZi3y1TnAfZj9b_i-S_cyP3ajpk_4eXWWQp7NKW3_0DsvDelijYeoRb897hr6c5cqKnLehNY2NedCW0bn6Mz2DK5vQD_umbF_ec0uub8rg7fMOBg7r7XO-YdPVjhRFy-M4SVa79oYkLBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوالات کنکور زبان امسال رو بردن گذاشتن جلوی یه آمریکاییِ باسواد؛
طرف پشماش ریخته که اگه اینا به زبون ماست، چرا من نشنیدمشون تاحالا؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70496" target="_blank">📅 11:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70495">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⏺
📰
ایران اینترنشنال:
قیمت دلار در حالی از ۲۰۰ هزار تومان گذشت که پزشکیان گفت کشور در وضعیت جنگی تمام‌عیار قرار گرفته. همزمان، محسن رضایی به نمایندگی از مجتبی خامنه‌ای کشورهای منطقه را تهدید کرد در صورت همراهی با آمریکا در جنگ اقتصادی علیه تهران، هدف حمله قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70495" target="_blank">📅 10:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70494">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=SKN1CUgXX2_JroV1GBqYXacXudRnJr-8u0Ea5Z6mXw1TUkVtOmb7Q09oipZVkjkM4caDXPG7GY2OjdeDKJOK9Vj1ysyiCHDGDDC8-2hT1ryVlKjrkCOpFNh9GRfr-gxQ2BQRvtHxAQ6XRsoI5-xoWsfEFsFoTHIq6h67soYwqQq-l8tNuL_9s5Mv3NddsLmNI3wod9aHgYUBfr3HgYaMmnkexEbGZb9WE8zTqT_-dboVcF6JBaibwX_T4TzLg3Cdk91-b65HYJCShEmboAuA3rD5bOC41sqtq1m8LRuWeHbRe_HbhBSP_VOg_JGyLvkhOUHr9OvS5OUrgfSI2O-nJ0KWEfVBJcKs2v84XUBBc5F_VIpqGKsBEl4XARHrAKPhWBpggdVRMt1G-osXJBazAQwTp-mpccn_i4FgiNO2uu-sr5bYAAzYLOuw1Z45uKHdDbW04PyKyI31YxR-sFRPQPx2blvS-BEq9ml9TKHp9Pp4HmCWb7EFFb16HIRnJySOJ1UIbkh9g8gJzgIiOpPo4SNm5EwYNtIvMCUya-3ZUrjZqMm3yo12wDXZNYMWFw4th5dbEH2MTFns2yzkeoMRu-7JNbjHI7f4_RgJx8e_a8dQv1tTcZb87gvDPaoPrtDMj0xDhvPlJTut5tiSRLBbAa8UpWjeuXzZO65f99kLf_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=SKN1CUgXX2_JroV1GBqYXacXudRnJr-8u0Ea5Z6mXw1TUkVtOmb7Q09oipZVkjkM4caDXPG7GY2OjdeDKJOK9Vj1ysyiCHDGDDC8-2hT1ryVlKjrkCOpFNh9GRfr-gxQ2BQRvtHxAQ6XRsoI5-xoWsfEFsFoTHIq6h67soYwqQq-l8tNuL_9s5Mv3NddsLmNI3wod9aHgYUBfr3HgYaMmnkexEbGZb9WE8zTqT_-dboVcF6JBaibwX_T4TzLg3Cdk91-b65HYJCShEmboAuA3rD5bOC41sqtq1m8LRuWeHbRe_HbhBSP_VOg_JGyLvkhOUHr9OvS5OUrgfSI2O-nJ0KWEfVBJcKs2v84XUBBc5F_VIpqGKsBEl4XARHrAKPhWBpggdVRMt1G-osXJBazAQwTp-mpccn_i4FgiNO2uu-sr5bYAAzYLOuw1Z45uKHdDbW04PyKyI31YxR-sFRPQPx2blvS-BEq9ml9TKHp9Pp4HmCWb7EFFb16HIRnJySOJ1UIbkh9g8gJzgIiOpPo4SNm5EwYNtIvMCUya-3ZUrjZqMm3yo12wDXZNYMWFw4th5dbEH2MTFns2yzkeoMRu-7JNbjHI7f4_RgJx8e_a8dQv1tTcZb87gvDPaoPrtDMj0xDhvPlJTut5tiSRLBbAa8UpWjeuXzZO65f99kLf_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدئوی وایرال شده از دعوایی که  تو گیلان رخ داده؛
یه مرده به بهونه‌ی دفاع از زنش، دو خانم دیگه رو کتک میزنه
!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70494" target="_blank">📅 10:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536dc396b0.mp4?token=bCho9rjfDeOqp8WrP_DhOzFBc4JXoduI4xoxtA5nxmZrRaWY6kJ7Du36If2RM0ol21pSok1Daw0T_DdB7vc-xJeTe2IEcck3yaz_G1eZemWsdPZCQYGipbeBr1jfMf_koNwtvan_FWtomp-jpZruywLhjKY34J1Pk4mjbNNmi4IjghqXDj5P0HNyesFC5pFxM4RSQbLh04fdYgNSt2ZkaR5mvzXDOODtmNoxGw1dG7OQ8DBI5pplVmK-uGTuzZfEhQrH8gNQ3vNl2rHyxWAp6VY_oaYc8ZsZZ0Cy2FyNu9Xob4RLclgUUJWstnAg3pZ9KBiz_TYp3Q7oCCfjI8R6YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536dc396b0.mp4?token=bCho9rjfDeOqp8WrP_DhOzFBc4JXoduI4xoxtA5nxmZrRaWY6kJ7Du36If2RM0ol21pSok1Daw0T_DdB7vc-xJeTe2IEcck3yaz_G1eZemWsdPZCQYGipbeBr1jfMf_koNwtvan_FWtomp-jpZruywLhjKY34J1Pk4mjbNNmi4IjghqXDj5P0HNyesFC5pFxM4RSQbLh04fdYgNSt2ZkaR5mvzXDOODtmNoxGw1dG7OQ8DBI5pplVmK-uGTuzZfEhQrH8gNQ3vNl2rHyxWAp6VY_oaYc8ZsZZ0Cy2FyNu9Xob4RLclgUUJWstnAg3pZ9KBiz_TYp3Q7oCCfjI8R6YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
هلیکوپترهای CH-47 شینوک، UH-60 بلک هاوک و AH-64 آپاچی ارتش آمریکا، در کنار AH-1Z وایپر تفنگداران دریایی آمریکا، در یک نمایش هوایی ویژه مسابقات Freedom 250 Grand Prix در واشنگتن دی‌سی به پرواز درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70492" target="_blank">📅 09:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=qrI-UpSPuceWMdygbHwClc2gzcBQB0SGdaOqDYjui04aaqXMZKnqoipBUJDu0IT8B9m7LtbJXJtzO6mJg2TVxCe0Udl5TyixlnsPBmU32ouixe60AIGvEbqyl2BnrE7gUk36SPZoo1JlMTteipe0Ox_D-eHlfblUTJdSYqHuGXKXbj2SW4w2SPHFHLG1019ThCMwc8_nPeCHBgCwf9qKTo8RFiFhXEP1P4wOevawwFuopChk87B8-cimFFMd1H9016YYpOBcZll3QY9KJUj0qfnOTLlPO22Zr2rl-WbVgijjLja9jcPEJc9I3oaQEik0SeCXY425Z3FswZpMY3iKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6f5402ef.mp4?token=qrI-UpSPuceWMdygbHwClc2gzcBQB0SGdaOqDYjui04aaqXMZKnqoipBUJDu0IT8B9m7LtbJXJtzO6mJg2TVxCe0Udl5TyixlnsPBmU32ouixe60AIGvEbqyl2BnrE7gUk36SPZoo1JlMTteipe0Ox_D-eHlfblUTJdSYqHuGXKXbj2SW4w2SPHFHLG1019ThCMwc8_nPeCHBgCwf9qKTo8RFiFhXEP1P4wOevawwFuopChk87B8-cimFFMd1H9016YYpOBcZll3QY9KJUj0qfnOTLlPO22Zr2rl-WbVgijjLja9jcPEJc9I3oaQEik0SeCXY425Z3FswZpMY3iKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
متکی، نماینده مجلس:
۹۰ روز آینده روز‌های بسیار مهمی هستن، ترامپ ایران رو مشغول تفاهم اسلام آباد کرد تا انتخابات میان دوره رو پیروز بشه و بعدش قراره تازه بیاد سراغ ما.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70491" target="_blank">📅 09:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70490" target="_blank">📅 02:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6kykairQVd_e2Zla4TiK-AB1T6nH1pH4KsCpdfARJa7K8BbYkzc-v7UG12fE8yWcUvjFVvBYw3Nq3M5IYPfdW5zrPyTEJLpEWzb9UluVkzNSX4RN0nEnCCv8Y7TeDEL2rVen2hnHE3Zs-O9WZig1kEY-Mlj0iH1zGZnrzrlME8EdRHOywyha8h82ks2oVWMTXiEeQhNKBadxaiKWgIzaP7aXJ_noIO1zdwyXLzYv6jqepFCdc5xHjhVO7RIwQ1hhJo2NX5q_1RQsaCVS79ekrORSS_wTmE2ZK0WNC1iT14v3EpdRywodI-GZ5E4r557yu5UOrmDyaGtpe8A9Ollqfm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6kykairQVd_e2Zla4TiK-AB1T6nH1pH4KsCpdfARJa7K8BbYkzc-v7UG12fE8yWcUvjFVvBYw3Nq3M5IYPfdW5zrPyTEJLpEWzb9UluVkzNSX4RN0nEnCCv8Y7TeDEL2rVen2hnHE3Zs-O9WZig1kEY-Mlj0iH1zGZnrzrlME8EdRHOywyha8h82ks2oVWMTXiEeQhNKBadxaiKWgIzaP7aXJ_noIO1zdwyXLzYv6jqepFCdc5xHjhVO7RIwQ1hhJo2NX5q_1RQsaCVS79ekrORSS_wTmE2ZK0WNC1iT14v3EpdRywodI-GZ5E4r557yu5UOrmDyaGtpe8A9Ollqfm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
a1
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70489" target="_blank">📅 02:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛وزیر خزانه‌داری آمریکا، اسکات بسنت:
«ایالات متحده در حال آغاز بزرگ‌ترین تهاجم مالی‌ای است که تاکنون علیه یک دشمن به کار گرفته شده است.»
او هشدار داده کشورهایی که به تجارت با ایران ادامه دهند، به «منفوران در عرصه جهانی» تبدیل خواهند شد.
🔴
به نظر می‌رسد فردا روز مهمی خواهد بود…
بسنت آغاز فشار اقتصادی جدید علیه ایران را به «D-Day اقتصادی» تشبیه کرده است.
هدف آمریکا، به گفته او، قطع شریان‌های مالی و تجاری ایران و منزوی کردن اقتصاد کشور است.
او به کشورهایی که با ایران تجارت می‌کنند، نفت ایران را می‌خرند یا در انتقال پول آن نقش دارند، هشدار به اعمال فشار و تحریم داده است.
بسنت معتقد است فشار اقتصادی می‌تواند حکومت ایران را وادار به تغییر رفتار کند.
او همچنین هشدار داده اگر ایران به نیروهای آمریکایی یا کشورهای خلیج فارس حمله کند، پاسخ آمریکا سریع و قاطع خواهد بود.
هدف این تهاجم اقتصادی وادار کردن رژیم به فروپاشی یا تسلیم در برابر فشار است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70488" target="_blank">📅 02:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f407bb9f5.mp4?token=urDQLQGVGKlJ9T4Gt9F2s1n0Xo4QC7kIc-VagNKA23Z46pLZFCQT1NhYTp9-oiY9o1tTvZ3nQ9O8HQtx01f_Vfmtoj3tsyhZWHpq_Pc_51hjuYfxuEDE4z55qdk9iZ3U1bvV3ZHvNbT47PgdpCF4GBqz71xqg-zo_TzYlngpuXx05Gfk6bO-zFzm0ROCXO47xONciaTrwielMD-LQrYRRjACgcdy7EDhoy3mDq_GCQ4cLq8kNBGy-LvT90Rpzkw4ED9Fd2o5JCiYGa4yiMUHfbB0ka1CoWvatuy44MKJPR81PzhlbpP-PD7OlG72UMLdJd74OOw4u97hUfBvFdY3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f407bb9f5.mp4?token=urDQLQGVGKlJ9T4Gt9F2s1n0Xo4QC7kIc-VagNKA23Z46pLZFCQT1NhYTp9-oiY9o1tTvZ3nQ9O8HQtx01f_Vfmtoj3tsyhZWHpq_Pc_51hjuYfxuEDE4z55qdk9iZ3U1bvV3ZHvNbT47PgdpCF4GBqz71xqg-zo_TzYlngpuXx05Gfk6bO-zFzm0ROCXO47xONciaTrwielMD-LQrYRRjACgcdy7EDhoy3mDq_GCQ4cLq8kNBGy-LvT90Rpzkw4ED9Fd2o5JCiYGa4yiMUHfbB0ka1CoWvatuy44MKJPR81PzhlbpP-PD7OlG72UMLdJd74OOw4u97hUfBvFdY3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
راغفر :
رئیس جمهور مطرح کرد
گران کردیم که مردم نتوانند بخرند و اینگونه مانع قحطی می‌شویم!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70485" target="_blank">📅 00:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70482">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dzypo_AEBjzp00V6_B2LfioIKdJkHW5-Xdt3OMHIYu8W_ITYGsooKNRZ2FXRBmdDKipgWNPXzSVP7TPXbvndFPKznKdObc0BWbTPGyj0lliHSIa3MVcNi-FbtrTkGaI7pwc368eu06qEGmunIUgZFav8EyDsBI8ELNh86VgX9CO820nkepEmueNu0DlO4GqE-cHoWSkCYpdz9mPK2O9M4mMou7F5eyGMwocgxf5465dKTn7Sz--CTu-viP4Ct2p780PMIrDFjMcMWOid3fc7pm-gS-S2Xi2btxjncRQneJAptkMISZnEaBRCAquVxK6LPN7cgDX7p-_gd_6RgT_pGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0qSSGnwhIldDUobYIcCOc1UhVvsHpXakb8oZn51DcZKmi5MO1XuY1m4ZdJcZbKi51d5bC60iT0v9u75Relp-if4F9twVwm2C8Tgi1yem5KgEWd_HKB0IdNYzcLLlS4UtDX1rBIoiRbLdh5bXo0H6ytqIkFWJuEizij50QvOkQM1flmytiQgfk_p2dmcPfVJEZ5Krwbk6nuTl1PhMcxfQeHF9VagZwYMVwxFjrnax1E1Yf8IN12YJTzNBvOxnQ07T4VKu6OjF-xDPibcG5gVNxtranZ8EFDgIxAHD2eoHcc-VX4DWW2ZwFQZZliSM3N8oYOPuCC-IQ6AdgCIZ_To_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی امروز صبح منطقه آرخانگلسک در روسیه را مورد حمله قرار دادند. این منطقه در فاصله ۱۸۰۰ تا ۱۹۰۰ کیلومتری مرز اوکراین واقع شده است و این اولین باری است که پهپادها به این منطقه دسترسی پیدا می‌کنند.
بر اساس گزارش‌های اولیه، پایگاه فضایی پلستسک هدف این حمله قرار گرفته است. پلستسک یکی از مهم‌ترین پایگاه‌های فضایی نظامی روسیه است که از پرتاب ماهواره‌های نظامی، آزمایش موشک‌های بالستیک بین قاره‌ای و سایر عملیات‌های فضایی استراتژیک پشتیبانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70482" target="_blank">📅 23:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70481">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=ajFbR5v6Lr8yOSDb8SHZnl8gH6kEfzM8qeRHIxsGU4VivveKN-jQjy8MlVhVXYdpZEfuWVQMZmmEUmVpU_1v5hVCWP1gUipzqFz5m1v9HDk1pTk4IO98LrwWZ7RgtEfnrXiJahId27iluEOLhUn_SqLBwI7fLuqVJ70tXMngjf-FHAw4ZouXj2Nrf7dPvy66HJFEeWlBE7wu3ssLY9RGH1sOULlzu1uJGln_VmJ5hhDcUqU8NZoPZVAUHSFHxFaVUmauwZ_f-l0n4VF1XhrksQVuy11_rSWHDsKg-JyKMtPN3l-Ej6dpqNJganh7Fx8wb7EqCvC6hOUay7l2uKwjTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=ajFbR5v6Lr8yOSDb8SHZnl8gH6kEfzM8qeRHIxsGU4VivveKN-jQjy8MlVhVXYdpZEfuWVQMZmmEUmVpU_1v5hVCWP1gUipzqFz5m1v9HDk1pTk4IO98LrwWZ7RgtEfnrXiJahId27iluEOLhUn_SqLBwI7fLuqVJ70tXMngjf-FHAw4ZouXj2Nrf7dPvy66HJFEeWlBE7wu3ssLY9RGH1sOULlzu1uJGln_VmJ5hhDcUqU8NZoPZVAUHSFHxFaVUmauwZ_f-l0n4VF1XhrksQVuy11_rSWHDsKg-JyKMtPN3l-Ej6dpqNJganh7Fx8wb7EqCvC6hOUay7l2uKwjTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رئیس دفتر پزشکیان:
قرار است جانفداها به سراغ ۵ میلیون مشترک پرمصرف برق بروند و بگویند صرفه‌جویی کنن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70481" target="_blank">📅 23:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70480">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZoRWPl6YyhNjxmzoC01EUxcJhE69N3cZTH0NmjfT2D4ABFZbSPJi1PdmGRmq84n8taEGkp593MbOLRAjO4Wzi2qS_vqkb741gy0laENTbh0iczcTkfnQoko3raW6F780FHTNXajMI7KSUB8cGBI3fQuse3qk7voTBCbpduw84l1GOInAiC-bYzA5hklDb0fyoU8GQCAYXOPGFKhT_BjIMX2m_N2Y3xHTwdECeL_VoDP8fgc3pbaOMnyOCC45y9z5izuN6JbLpymXC1SjQjOlT_aYGxfEMJvvuGTXsotCKcchz1apKvbULzP2inuF_7ZypPuQ3d2tTWT6Tvv9AaiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی:
اگر جنگ اقتصادی ادامه یابد، حتی یک قطره نفت صادر نخواهد شد؛ نه از طریق تنگه هرمز و نه از هیچ نقطه دیگری در خلیج فارس.
ایران مشارکت یا حمایت هر کشوری از جنگ اقتصادی آمریکا علیه ملت ایران را به منزله اقدام جنگی تلقی خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70480" target="_blank">📅 23:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70479">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB177cSs3hdawusfwQphPN8TXcK1H4kkj_gZ6NWyrHXXEtT0PXXi9eOG9h1MAWn9K4_6X4j1HGGLvWXGVjyVUPUHTVg97oImgHyNcL6z9hPUfzPHSByuzKRK-KlLc5jO8WWa-BwgSbf23A6H9OFf4huOiKqHqt8m2mQHBHDdmIOw20iR42fn6vqTTUPRTcBciDPsd-QhzNCJRE93rFu4Y2xtkotH-h9qYX5UueoJjYw_7JQs6YRgG7G8o3WFTSJ1BUztWBIPDbCQWLPLpXyz7rtzP5ZGVGxGfuETWsOlZWrqDn-vS_mWHcRWtQ871GjG2NX7PNYhKappU3hrhE-n0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گسترش فرصت‌های سرمایه‌گذاری در وال‌گلد؛ نقره به میدان آمد!
💎
تنوع، کلید موفقیت در بازارهای مالی است. پلتفرم «وال‌گلد» در گام جدید خود این امکان را فراهم کرده است تا کاربران بتوانند در کنار طلا، روی «نقره» هم سرمایه‌گذاری کنند.
🔸
روند یک سال اخیر نشان می‌دهد نقره بازدهی‌های چشمگیری در بازار سرمایه داشته است.
🔸
با این امکان جدید، سرمایه‌گذاران می‌توانند با ترکیب طلا و نقره، یک سبد مطمئن‌تر، کلاسیک و پربازده بسازند.
ورود به بازار جذاب نقره
ورود به بازار جذاب نقره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70479" target="_blank">📅 23:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vj26pEQ5lLMd96NdQRbc1BxghQOuZMybVioAHaEhoeEZbJX5SzbDua5RjgGE-E1j_rJj56sxZ2-_FSk34WFczZtfT3OUoVMcFMhfZyNM4W-YXyrAzvrc4QPggPxJ8QuWBF00CcAnkfk4wdOMahEiRtNKDinOAPQgWsBdTAs0DCWeXNy7UhqAbJipt1KVDZWdMCod0wL2m_WJFCJ5gUZ2yBSPPaJYtQkww2bUQRxi-FMTDGcOFT63Ht7b63BHOgtrLdJoAUZkvLpyrwgmfYSIbdw7cF3u38k3p_ZIq03BtI2MbjQWGH3YjYFTBTI8mOI2SillhQWxvj_Q_4K4KLQdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تا ۲۰۰ میلیون وام بگیر فوری!
🔥
‼️
با اسنپ‌پی می‌تونی بدون نیاز به ضامن و فقط با یه برگ چک صیادی تا ۲۰۰ میلیون تومن وام بگیری و تو اقساط بلند مدت تا ۲۴ ماه پرداخت کنی
😎
تا ۶ شهریور ۲۰٪ هم تخفیف اشتراک داری
🤩
پس همین حالا از لینک زیر وامت رو بگیر:
👇🏻
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70478" target="_blank">📅 23:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇷
توقیف و مصادره در انتظار شناورهای متخلف در تنگهٔ هرمز؛
🔴
نهاد مدیریت آبراه خلیج فارس اعلام کرد شناورهایی که از ترتیبات اعلام‌شدهٔ ایران برای تردد از تنگهٔ هرمز تخلف کنند، در ترددهای بعدی با محدودیت‌هایی از جمله جریمه، توقیف یا مصادره مواجه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70477" target="_blank">📅 22:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70476">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d4jgPJIZaHJ8pQmoYJjqE6vhlsIDT7hSzwtO2mioWVr3QvaFxxzNqEQzF9mB8D2OXBQzffAluppha2dUH4Q5Kkc_JPYwX6B2XAZ_PP_dfPKYEcFmU8fVjfmcCDIE3N1fj_fL_nT1_xcwMejTmsYDmeQ1WZoRiJ8rLUI0HR4JpELfQ5oGS5ds3NDe4TsrthSCAIyZZjZH9Cg2MSykTyk1yDcIjBtPPxH0BxqA7BcUa4vcpaWGvAumPuq6c_CMVp2CuFU-oLX0TRgLTMx65535Gwmy41piGl_5Pl2FQs2t27Ks6Q4WKzxsLjLJZlD7b6_BgL3yXxnT_bX5UObB5y-Ydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجری عراقی با انتشار این تصویر نوشت به این جنجال پایان دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70476" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70475">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44391ebe9.mp4?token=KA1Ac9mudC1Ze5KpgZ48XHEne3F1P6nn3A-hPFQMGB3sDtMQVVslrgz1wHiIrfRTBkPdE-89TjQtqjySWuJ-pj0u7gAawDB6k8xWmLq2Pvi8nwO0u53AQi32Wa7ekaucPfwtIUzVLSVZcnxmnQpy11lVYELWswwBvg3gj5AFivJJ5nfzqluGGP5HXB8iTVDzc_d0bg1zGaFM440PNNJXjPqlfIdDTSXMnS1a5KzS1we5ZrMhxg06IhPsN_7XrYAv6iH72k59ij2wXdRy-TLziWBaZc9x2OUjtGkhYEpJRWL4MTzPZ5fVaALmRSlFzLpOGOfyWZMhMeVyo_Vgr9rQpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44391ebe9.mp4?token=KA1Ac9mudC1Ze5KpgZ48XHEne3F1P6nn3A-hPFQMGB3sDtMQVVslrgz1wHiIrfRTBkPdE-89TjQtqjySWuJ-pj0u7gAawDB6k8xWmLq2Pvi8nwO0u53AQi32Wa7ekaucPfwtIUzVLSVZcnxmnQpy11lVYELWswwBvg3gj5AFivJJ5nfzqluGGP5HXB8iTVDzc_d0bg1zGaFM440PNNJXjPqlfIdDTSXMnS1a5KzS1we5ZrMhxg06IhPsN_7XrYAv6iH72k59ij2wXdRy-TLziWBaZc9x2OUjtGkhYEpJRWL4MTzPZ5fVaALmRSlFzLpOGOfyWZMhMeVyo_Vgr9rQpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سعادت آباد تهران دو تا گروه تیم‌کشی کرده بودن برای دعوا و این شکلی با بیل، چوب، سنگ و هر چی دم دستشون بود، افتاده به جون همدیگه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70475" target="_blank">📅 21:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30c15be54e.mp4?token=awhOdDtXOw6i0pKOPi0wniyn7bfZrXiiSzXdLX05_ZS7UWyl_TMjRe932p7UvkSSkGoOdGVQFbC8AqaAhKq3oy6ogN_QkEuBDWzJn_dTEbHGvUkdlpWb-xKSJJsJ3bo4sgv-m6-8BL2sJIDhvz2QNQRcJrkv09f-uesCPmL0lJX4J6JvlEwwua_8QI6XuRKRsFPAxLAeQUaqFtfrtGPLyUL69EmeuVj8Dmq6V4WGdpqlmPrcv26ShcGIOy8LRQohKaO6PHHRTfxbL5M3PBSVAeOSG-cBRXnnZICV5xGWBIA4l11Hs_GgjxbWP0S0-sFSs7HiEs8-xtNgd7eyKI1ABlDceLnejPerk3sliLYU_dxwRR22wRFmQHNxMY2IgnXYXuSqUouqVcf8CYkLAmgu9SursPtq8YeLd4k18V3_bZuDA7mlFuJQceoAxH1YYyFmI3lvhKJCaTZLjYs-OaUPn_pstX3uXmt7nBIoJriAah46spPEqoS2xVgHqhEM700O2n0STztaWfwBXlk9tza25gN3L4GSAVsmRTLrZ3DPazt8cA08moZD76E13CbeLDeeHrQxxXLDu2X0ZDuSxmtqys399MFgXSOnmpWwHWOudg3Lm-calmwjCVsE-KjtbYFYxmmMzY3sGCnXrqi2YWOHygBVUteY45k7zWVgr1YtvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30c15be54e.mp4?token=awhOdDtXOw6i0pKOPi0wniyn7bfZrXiiSzXdLX05_ZS7UWyl_TMjRe932p7UvkSSkGoOdGVQFbC8AqaAhKq3oy6ogN_QkEuBDWzJn_dTEbHGvUkdlpWb-xKSJJsJ3bo4sgv-m6-8BL2sJIDhvz2QNQRcJrkv09f-uesCPmL0lJX4J6JvlEwwua_8QI6XuRKRsFPAxLAeQUaqFtfrtGPLyUL69EmeuVj8Dmq6V4WGdpqlmPrcv26ShcGIOy8LRQohKaO6PHHRTfxbL5M3PBSVAeOSG-cBRXnnZICV5xGWBIA4l11Hs_GgjxbWP0S0-sFSs7HiEs8-xtNgd7eyKI1ABlDceLnejPerk3sliLYU_dxwRR22wRFmQHNxMY2IgnXYXuSqUouqVcf8CYkLAmgu9SursPtq8YeLd4k18V3_bZuDA7mlFuJQceoAxH1YYyFmI3lvhKJCaTZLjYs-OaUPn_pstX3uXmt7nBIoJriAah46spPEqoS2xVgHqhEM700O2n0STztaWfwBXlk9tza25gN3L4GSAVsmRTLrZ3DPazt8cA08moZD76E13CbeLDeeHrQxxXLDu2X0ZDuSxmtqys399MFgXSOnmpWwHWOudg3Lm-calmwjCVsE-KjtbYFYxmmMzY3sGCnXrqi2YWOHygBVUteY45k7zWVgr1YtvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🇺🇸
هواپیماهای B-1 Lancer، B-2 Spirit و B-52 Stratofortress و چهار فروند جنگنده F-35 نیروی هوایی ایالات متحده، پیش از آغاز مسابقات «گرند پری Freedom 250» در واشنگتن دی‌سی، بر فراز محل مسابقه پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70473" target="_blank">📅 21:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=LZ9_TYonUfQ1ff7MlaOoOOaUUZ5sf9jAc0hhPikYxLzKguQV_X0VvKOKn-mE_NDGtEV2Wkn-RkSoOay13yMcAj0fFEfYYlTSTbQ3dWxlRFiZpcDb1bQguW8OJheTdzJ2dZyAxl1XATQ6vQaK-XP9MXMY78CTb4CLKaFZavzYihHcDWT6rD41IYcHO884F_VBhMqoBAQdDyqEi0dC7Xk3kThQfuB3R7PhPQFHMK0jLotFAKT9Re5DKuPJAMDkssoLPla3yvnXddPcHB-zpCNC7q0qU4V9hi8j2zMlF2E90SW3-R7sXXL3_JNrf1Wwd5FP12vnMBw3R2HH7uKqazVQGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63aefba4cc.mp4?token=LZ9_TYonUfQ1ff7MlaOoOOaUUZ5sf9jAc0hhPikYxLzKguQV_X0VvKOKn-mE_NDGtEV2Wkn-RkSoOay13yMcAj0fFEfYYlTSTbQ3dWxlRFiZpcDb1bQguW8OJheTdzJ2dZyAxl1XATQ6vQaK-XP9MXMY78CTb4CLKaFZavzYihHcDWT6rD41IYcHO884F_VBhMqoBAQdDyqEi0dC7Xk3kThQfuB3R7PhPQFHMK0jLotFAKT9Re5DKuPJAMDkssoLPla3yvnXddPcHB-zpCNC7q0qU4V9hi8j2zMlF2E90SW3-R7sXXL3_JNrf1Wwd5FP12vnMBw3R2HH7uKqazVQGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وزیر نفت: ۷.۵ تریلیون گاز در جنوب فارس کشف شد.
بیش‌از هفت‌ونیم TCF یا به عبارت بهتر ۷۵۰۰ میلیارد فوت مکعب گاز کشف شده که با احتساب ضریب بازیافت حدود بیش از ۷۲ درصد امکان حدوداً ۵۷۰۰ میلیارد فوت مکعب استحصال گاز وجود دارد.
این میزان گاز معادل این هست که یک فاز پارس‌جنوبی به‌مدت ۱۵ سال بتواند تامین این حجم عظیم گاز را بکند.
این گاز خوشبختانه از یک ویژگی خاصی برخوردار هست و آن اینکه اصطلاحاً شیرین است؛ این شیرین بودن گاز باعث می‌شود که هم هزینه‌های عملیات توسعه‌ای کاهش پیدا بکند و هم هزینه‌های عملیات بهره‌برداری.
در کنار این حجم گاز، حجم عظیمی میعانات گازی را ما داریم که مجموعاً ده‌ها میلیارد دلار به‌علاوه ارزش ذاتی آن گاز برای کشور ثروت جدید به بار آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70472" target="_blank">📅 20:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IT5jYiaMrIrq_20eCqfOD4fce0aLakNSavJ4JVH1aa7ejmkF7a39wmSRNMT3FmeCuKjIz210Ppij92w-l4wVbPYaDGx7DX60kx1sQ6jLZyEILtSWNdLDFOcqDXRVeMBVp9-YtTWgr-jz2zGx-VslPPB_m9Dp6Q79CZEzaHFQZkrImdj4HJKK36jabL3mFkpcm7C6hVEcm0K3xuIQk71luxJaqLZ5rKDCJOAelIrR_QDQC55WWv5_DQRHHW4K00pFCy8-pI35fBJASm1gTls5S4BgFpZLDbj92JCSntrajXB-q_QaahK2Qt1exKUBCWzMAcO8b3ho2S_pOEhUpnpqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف در مورد سیاست های آمریکا:
واردات گوشت منجمد برای مهار قیمت گوشت؛ خب، شاید این راهکار جواب بدهد.
اما برنامه برای اوراق قرضه چیست؟ واردات بازدهی‌های منجمد؟ خریداران مسکنِ منجمد؟ یا حقوق و دستمزدهای منجمد؟
سیاست خارجیِ منجمد، اقتصادی منجمد به بار می‌آورد.
تنها چیزی که همچنان در حرکت است؟ بومرنگِ ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70471" target="_blank">📅 19:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd998e89b.mp4?token=l2YzglTp8e6fb4_LYaDZFXpmOvZSdEQFKnaoy1udq4qq8zMmNG7sjd8zqgaEBTBA5rjDmEkz69BSx67nrDm39fDcdatNeoGWEis2ukBT-1QaoLWzCr51L1nDLxRuy_qDc2ViK2Mg0U90DHbZdbX9fFYPwPjZhHJKRrk3abj7KjiYgy8njSP7-Cn8LbVlBhbunxudccRekbY5xUUuh4PgFvBTBUZFAxBid-eBekZiNReBNguYghimGOYORLyB5CUvzJbNuL0ykEXtqBtd48qtyQt8EmDVIWAmnEgYTus27gv8S1d8clrr2giINI2cXeTT1ayqJAQ730jvQqzqrUZjPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd998e89b.mp4?token=l2YzglTp8e6fb4_LYaDZFXpmOvZSdEQFKnaoy1udq4qq8zMmNG7sjd8zqgaEBTBA5rjDmEkz69BSx67nrDm39fDcdatNeoGWEis2ukBT-1QaoLWzCr51L1nDLxRuy_qDc2ViK2Mg0U90DHbZdbX9fFYPwPjZhHJKRrk3abj7KjiYgy8njSP7-Cn8LbVlBhbunxudccRekbY5xUUuh4PgFvBTBUZFAxBid-eBekZiNReBNguYghimGOYORLyB5CUvzJbNuL0ykEXtqBtd48qtyQt8EmDVIWAmnEgYTus27gv8S1d8clrr2giINI2cXeTT1ayqJAQ730jvQqzqrUZjPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
❌
🇮🇱
نتانیاهو و ترامپ در میدان انقلاب تهران اعدام شدند
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70470" target="_blank">📅 19:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70469" target="_blank">📅 19:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70468">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqCpwE9I8Xf2GKnlddSVlX7MaJ6r-6szD9Wx6vJTpfxTxq7Yqcl_aaGS1jRVazF1O3gKCrThcAl6c2xm88ShMQEib0QQkxUPwhYPTNC5acSlTupbyC-pgEQ-x3neO5mSf3pQ4ifAs9JXdw_Pmk9-EBnXWwtuTw_-OWmnMG4dYXPVEv7EhvSjEvjmk5qWuqchp91-pUmoZjo1UzEodRa2d2Js6y0JrCCElJOzSzMy_bp62pNs9klj9BuetUJ2KubVxb6XDAoneDbsitpxOcw0CREO1ud9Y4UtqkO6EgJZi-d0mpe7hCHxShqZIRDb-CdquJWn_gvq2Zpb-CFW7QXCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70468" target="_blank">📅 19:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70467">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f7dd3a967.mp4?token=GpzThtKVqz-80TdAk58kopdGS2hwXf0vIsROKl_xDczOKmlSEQH-1cbtkUvCO6vU1bshl82Y1-GNNDS-U3QoA31cMtb_HnpiNamONFajrFQqtMD91kRM6beukSxp3Z2kBkaXbqorPYho9MjE1M40GJl1zO6np_JVpn6AOBSMMhLQZBvytmwlPXWKPsnoEsT0TNmn1srnQIyEazQL9SRExHY9eFQf_wKDmXD9bZ-Ss60131s7l8zwlyeJ4lLORPZsJjYSt3zbBCnhb45ys3oEZOyOFO1oLSbK82dcQ7it8MjxxagGnJpH7fumcQnlu3D9KVJCgvw-CYJiDJUyaxtXYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f7dd3a967.mp4?token=GpzThtKVqz-80TdAk58kopdGS2hwXf0vIsROKl_xDczOKmlSEQH-1cbtkUvCO6vU1bshl82Y1-GNNDS-U3QoA31cMtb_HnpiNamONFajrFQqtMD91kRM6beukSxp3Z2kBkaXbqorPYho9MjE1M40GJl1zO6np_JVpn6AOBSMMhLQZBvytmwlPXWKPsnoEsT0TNmn1srnQIyEazQL9SRExHY9eFQf_wKDmXD9bZ-Ss60131s7l8zwlyeJ4lLORPZsJjYSt3zbBCnhb45ys3oEZOyOFO1oLSbK82dcQ7it8MjxxagGnJpH7fumcQnlu3D9KVJCgvw-CYJiDJUyaxtXYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی مشهد طرفداران حکومت که علیه قالیباف شعار می‌دادن و خواهان انتقام خامنه‌ای بودن برخورد شد و متفرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70467" target="_blank">📅 19:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51d98cde4.mp4?token=SpHQ6iLDr4oXyqxlNEKau1i_AI6c7ZrQNzWTu3hw6-sGBDUF_opxWndGfbEfJHEHm11-A1JWgbPztaGpAAADDIuG06_D47GTCn3iYlSl_b8VanCA9-b7esQDkphhNr-ht4gdMVUL_RpoxlZSwNn5EUgxr-_44j4D3ZG4AGiLs-p9TeW4hV7zJ5LFOFOlW2XN9XKnDhr2W3Ngz8xO6JsBgb-Nrr8EjzDr9v7MyFhRDjH0nhIlqNP9nLA3drUsYy_JHUiKAsM5nOfNZM8_tCq5iAm0yE6HAmYA14e_BBrMa2rB6Pw4S4UmY868tBvipGZEnnXkIePQzVAkrNRdccpHcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51d98cde4.mp4?token=SpHQ6iLDr4oXyqxlNEKau1i_AI6c7ZrQNzWTu3hw6-sGBDUF_opxWndGfbEfJHEHm11-A1JWgbPztaGpAAADDIuG06_D47GTCn3iYlSl_b8VanCA9-b7esQDkphhNr-ht4gdMVUL_RpoxlZSwNn5EUgxr-_44j4D3ZG4AGiLs-p9TeW4hV7zJ5LFOFOlW2XN9XKnDhr2W3Ngz8xO6JsBgb-Nrr8EjzDr9v7MyFhRDjH0nhIlqNP9nLA3drUsYy_JHUiKAsM5nOfNZM8_tCq5iAm0yE6HAmYA14e_BBrMa2rB6Pw4S4UmY868tBvipGZEnnXkIePQzVAkrNRdccpHcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
علی خامنه‌ای، بهمن ۱۳۸۹:
زمان شاه حکومت وراثتی بود. مردم هیچ نقشی نداشتند..
🇮🇷
صداوسیما ۱۸ اسفند ۱۴۰۴:
مجتبی خامنه‌ای فرزند علی خامنه‌ای بعنوان رهبر سوم ج.ا انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70466" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70465">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e23c4e23a.mp4?token=uJdfJlZ76QnCsQOpp9Q4sbptHWXoTlopEbjl8uDJxbQqSEMlmCg2Lxc_8tBwpeJ2eG8uZnanDdd6ecEKIEd-tmaS3Kph0xITp_WVmsP5e2oeKKPGgl14fH6cXfTTwGE5Bq25L8GlzTJRJJsEQ9BddWKcVJbehKMWmJXjIyNZYBfivA1cY5AIvOR953OEe_7I6yeslDIJ2qkdPD2BQSdoNFklUEgKUwZ-1lLT1YFqIg4e0llSjbjHqjZf5vE0Y2Tf5LA7oinKYj6VVidT6ns8FXIUGh4JloSUfWjTL3tPH2sTf1tMF_L1tPWgw50Wi-dUz4Vl_lKESJkSwpsXkBPVkWsAQZ7CsBKVJJKZ3IfLT8hbbCTnZWSFGF51gNFM2nKqD9F3JEq6zhIDOoZxeTjp1JN50Y3mtdRcMSRJG2WvPVj_TQZtR1D54cBQPOznttOfsAtqp58OpyNE9aq3xoJTeHksb-9LdHFGpf6b5LUr_ykojFaO3N7CQ9JUzPNHIX-xQE9_QWRZt6cBZOCXTEnUIVXWTLdM2ZasNgnIYGy7gvkZdICYPrE1c6fmgXbAHkSYN9A40_3TNExAVTUJkLjrHYIGrsls03JMJkwLLd_UjD33Ac-4bwhCQJXsyXS_xfboT_BE0FvfHpawebf1SmKlpFPIUarq9_0PrGIx_UT5V4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e23c4e23a.mp4?token=uJdfJlZ76QnCsQOpp9Q4sbptHWXoTlopEbjl8uDJxbQqSEMlmCg2Lxc_8tBwpeJ2eG8uZnanDdd6ecEKIEd-tmaS3Kph0xITp_WVmsP5e2oeKKPGgl14fH6cXfTTwGE5Bq25L8GlzTJRJJsEQ9BddWKcVJbehKMWmJXjIyNZYBfivA1cY5AIvOR953OEe_7I6yeslDIJ2qkdPD2BQSdoNFklUEgKUwZ-1lLT1YFqIg4e0llSjbjHqjZf5vE0Y2Tf5LA7oinKYj6VVidT6ns8FXIUGh4JloSUfWjTL3tPH2sTf1tMF_L1tPWgw50Wi-dUz4Vl_lKESJkSwpsXkBPVkWsAQZ7CsBKVJJKZ3IfLT8hbbCTnZWSFGF51gNFM2nKqD9F3JEq6zhIDOoZxeTjp1JN50Y3mtdRcMSRJG2WvPVj_TQZtR1D54cBQPOznttOfsAtqp58OpyNE9aq3xoJTeHksb-9LdHFGpf6b5LUr_ykojFaO3N7CQ9JUzPNHIX-xQE9_QWRZt6cBZOCXTEnUIVXWTLdM2ZasNgnIYGy7gvkZdICYPrE1c6fmgXbAHkSYN9A40_3TNExAVTUJkLjrHYIGrsls03JMJkwLLd_UjD33Ac-4bwhCQJXsyXS_xfboT_BE0FvfHpawebf1SmKlpFPIUarq9_0PrGIx_UT5V4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قرار آخرشب خوانندگان پروین ملکوتی و حمید قنبری محصول سال ۱۳۴۹:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70465" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70464">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=WeIFHFEQ9Uc90WGrumcI0EmkeYu31CrxSYxnveR8Iejjrx9wIBcWysxe3_byDbSnqFUa1Cwd-0fjqPxWSB0f5sZj-LLxhN9QxYwXdlH1B7UpuDal2u54okptjBqzlxEbICwKTSw0vjSriXehPsO0mkBDgPHITQTES_qAnOHX35dZMmYg6seoZFtT807G_yti1k84xe3ZJPsdMOEob1xelVi4X1wk0GynTW7kMBziYSsgcC_ZBV_INIFFCDxHfNHGiJ09fbPGvxPhZF-3WrBrHExEZArQFF7YD2gqBk54sSXPV2APYBaRpUSa5PXEUwBPkH58PkOTDbfYDMiMfw0K_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=WeIFHFEQ9Uc90WGrumcI0EmkeYu31CrxSYxnveR8Iejjrx9wIBcWysxe3_byDbSnqFUa1Cwd-0fjqPxWSB0f5sZj-LLxhN9QxYwXdlH1B7UpuDal2u54okptjBqzlxEbICwKTSw0vjSriXehPsO0mkBDgPHITQTES_qAnOHX35dZMmYg6seoZFtT807G_yti1k84xe3ZJPsdMOEob1xelVi4X1wk0GynTW7kMBziYSsgcC_ZBV_INIFFCDxHfNHGiJ09fbPGvxPhZF-3WrBrHExEZArQFF7YD2gqBk54sSXPV2APYBaRpUSa5PXEUwBPkH58PkOTDbfYDMiMfw0K_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس این ویدیو رو با عنوان «تغییر مهمی که در پدافند ایران رخ داد» منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70464" target="_blank">📅 17:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70463">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a699022499.mp4?token=SPIm9iYGMD1A9v-PRFfQoKOGlpib56it0TmcvDXt0mQyUP4McIHS1MI7XZJqMEt3t09AyNQ5elEeKm-bMiMPaLKiTOUzaI0L3PEzzXFdFJq8ZQlqsrFVeOpDgOFE3UHoMM6Zh0C4XlhykjrUpwffMdeM38jVTkgZ6zBbSxkiUCAqSNqnB8Jn6EQs871VOQIu0PFZ4cswqHk4LkqQGBnb1Jy9RWU2ZngKcTGxefyIyd2MpuoE9io9h5FSVzms1caRGej7FH-2bqTY5C96e_aSSxYkksFGyhtNdZ-0VI9IOXcsG_UpKZI7MxZ5_gAesQPkuKSlU1Fz89D5TNiXbWtFjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a699022499.mp4?token=SPIm9iYGMD1A9v-PRFfQoKOGlpib56it0TmcvDXt0mQyUP4McIHS1MI7XZJqMEt3t09AyNQ5elEeKm-bMiMPaLKiTOUzaI0L3PEzzXFdFJq8ZQlqsrFVeOpDgOFE3UHoMM6Zh0C4XlhykjrUpwffMdeM38jVTkgZ6zBbSxkiUCAqSNqnB8Jn6EQs871VOQIu0PFZ4cswqHk4LkqQGBnb1Jy9RWU2ZngKcTGxefyIyd2MpuoE9io9h5FSVzms1caRGej7FH-2bqTY5C96e_aSSxYkksFGyhtNdZ-0VI9IOXcsG_UpKZI7MxZ5_gAesQPkuKSlU1Fz89D5TNiXbWtFjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی برزیل یه مرد همجنسگرا رو مجبورش کردن برای اولین بار یه زن رو در آغوش بگیره! اونم از شدت ناراحتی بیهوش شد و از حال رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70463" target="_blank">📅 16:45 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
