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
<img src="https://cdn4.telesco.pe/file/R1HZZNtyKhHoULqsmat5ydJQJDdZTvK5WwR_8l6rx-IOAF1Ba2DaAdFmwp0NXGhMZX_fwIhCPeKKIBNeBGUCu2jkdGdItxRfHZVTaP8lHTN1gz8jBF9M-evlkrbTUBbq5hMc4VEY_cdmGagwpjk8ODfAUptwJArX9pYlSDAW_eKr1p15nYFlVVw6aePmrRqjWTToNCnND9Hn8yCTiFs8TVELx-dES1p99KoJMNfrOA20r83RBiAT0y8DRoITbbk-sUdTOOegtsO_1bhu8y49lp-FVuke4uwdRVfkB2PN48kfMX8X7wJecVmCtlV1HYLv4gRiUwUiYZubc9OX4_I7cQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 113K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-70999">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcFUN7YKD6yVwVtOMJ22MF5fYbGtcQXXKYbD5qhAAAfV0FXJ0GCFRBnpafGYvpDOag1VKIVR0-YqX19t1RsHgtxHaI7R3dU4xDRutuLqLwKIQi4JzdekPc1q67N1xSPstZDnVcytOOkEI2F_QqPm7JlkSWWNxJ2q5M6SD5ckdiRrMd55lBzwnkE21qJ5F0f0WzAuaGx7K6isVSRLVhXnnCW98H-_Rr5NKqJo8kddoxsMF1xJvxAp4Jag5ON7u-uZutpyrpU_ANdqAyDwCo5ynxUjdJRzwejOEYV2DVDmWFpjtmWe5b5chaKZ7KOENpOKV2IW2qo0e_9O7o3VshNT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/news_hut/70999" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70998">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bqt2X-v4QV3z3uq0j2VIC0EwVKd0cG3UvghSvnaJ3XItPuOAi5idLImmcpTxLBfcz9VQ98QJssGPTBYBV6JxJA3Dpmf682j_R57e7_SQWT6_16gcMgsNPcPadx2todzYzKMpt7fguY7wMNKCgY5xPC82PPBexRVTU9oxnDKQItIMPCPe7xBaOD0AzmEulXI54hbtVOn9qnRc9DBAd383I18Hj5dsucKohYID6NVHJTD5FgZUV4SGnxMlFkS-rEpLBAT-siFE40tOiwkYIN6S8bSsgr60dtx-o0ZHeWts01JGYNqfzeO6C9iuQv_H_dzrMjchivbrdMywAs0biZ8m1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
فیلد مارشال محسن رضایی:
با این دست‌وپازدن‌ها، نه تنها در بیرون آمدن از آن ورطه هولناکی که برای خود رقم زده‌اید ناکام خواهید ماند، بلکه به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، بنیان‌های شما را درهم خواهد کوبید.
@News_Hut</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/news_hut/70998" target="_blank">📅 14:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70997">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13235e9918.mp4?token=vDSs8U-iF_5uPHE8GUOGLm-raejao0Ny_AM4-7VNKiPnVX7PJijsPHpExi9GwPrOQ9IRQc4xWVp8XK6Dyu0J-pXIkbzk5M76eZRJLljH-9yrS39GBNU9p5fkv0a3f4GIKwsPI02nbDECp7YBp8aEZODWc0zj7hRpHbWMhXx14c4IWCeu6Z6Ze8_PBVs5Odt-6DvoOnLq__gVe8hzhmwBn5J88ZpI6z7R5JiAmXlCjct1F3Vi_9eEkBDWGi920D0nbRWwHOx8vVg-wDQiCKKEQg-cUHouwxj3KNFxG6g9V9DYH2Adb7a9QSxaqucin-F9TcOqsv1Tqz0t6tnseDRKPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13235e9918.mp4?token=vDSs8U-iF_5uPHE8GUOGLm-raejao0Ny_AM4-7VNKiPnVX7PJijsPHpExi9GwPrOQ9IRQc4xWVp8XK6Dyu0J-pXIkbzk5M76eZRJLljH-9yrS39GBNU9p5fkv0a3f4GIKwsPI02nbDECp7YBp8aEZODWc0zj7hRpHbWMhXx14c4IWCeu6Z6Ze8_PBVs5Odt-6DvoOnLq__gVe8hzhmwBn5J88ZpI6z7R5JiAmXlCjct1F3Vi_9eEkBDWGi920D0nbRWwHOx8vVg-wDQiCKKEQg-cUHouwxj3KNFxG6g9V9DYH2Adb7a9QSxaqucin-F9TcOqsv1Tqz0t6tnseDRKPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
پوتین خطاب به پزشکیان:
تو این شرایط سخت، داریم سعی می‌کنیم هر کمکی که لازم دارید، بهتون برسونیم
.
قبلاً هم دربارش با هم صحبت کردیم و داریم کالاها و اقلام موردنیازتون رو تأمین می‌کنیم.
با وجود شرایط نظامی و سیاسی فعلی، همکاری‌های تجاری و اقتصادی‌مون رو با همون روند و قدرت سال گذشته ادامه می‌دیم.
همون‌طور که بارها گفتم، ما تو روسیه کنار مردم ایران هستیم و باهاشون اعلام همبستگی می‌کنیم. شجاعت و مقاومت شما واسه دفاع از منافع ملی‌تون واقعاً قابل تحسینه.
لطفاً سلام من و حمایت صمیمانه‌ام رو هم به رهبر جمهوری اسلامی، مجتبی خامنه‌ای برسونید.
@News_Hut</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/news_hut/70997" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70996">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان   @News_Hut</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/news_hut/70996" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=T9BVyJeWBrWUCKUVOreqsVgCG2mxNYTDgXHC0YkmOWs4oCyKeqEy_qRAkKaXYAp7W2l3W3gzmx9aILK5h56vzbYuFSW5pTSzMhsyiZ4KrFoHWFXxqHKzqUs9Xq7UZFRT9SFa-QsU3AjGBWABChXlxtb2lQpn0oaZxzFUvVCCN3P_gqqGYoGPXlXPVCgML0kNBVSqOtlzu0ueA5g_-C-RpkCWYcPGgyTNNB0Eeqs3HFRWaidDI8QdULP_4YtQDgCPAbZiMDwiDxmEIYZzHk41MWAVNfjLJMF6KheT8uh7DuWNSCz6sLXFQUO-jgdkmbfgihrYnuFaShyZtn8y5TFmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=T9BVyJeWBrWUCKUVOreqsVgCG2mxNYTDgXHC0YkmOWs4oCyKeqEy_qRAkKaXYAp7W2l3W3gzmx9aILK5h56vzbYuFSW5pTSzMhsyiZ4KrFoHWFXxqHKzqUs9Xq7UZFRT9SFa-QsU3AjGBWABChXlxtb2lQpn0oaZxzFUvVCCN3P_gqqGYoGPXlXPVCgML0kNBVSqOtlzu0ueA5g_-C-RpkCWYcPGgyTNNB0Eeqs3HFRWaidDI8QdULP_4YtQDgCPAbZiMDwiDxmEIYZzHk41MWAVNfjLJMF6KheT8uh7DuWNSCz6sLXFQUO-jgdkmbfgihrYnuFaShyZtn8y5TFmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
ناو «یو‌اس‌اس آبراهام لینکلن» در تاریخ ۲ سپتامبر و پس از ۲۸۶ روز حضور بی‌وقفه در دریا — که رکوردی مدرن برای نیروی دریایی ایالات متحده محسوب می‌شود — وارد بندر «لائم چابانگ» تایلند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/70994" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70993">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل درباره ایران:
هم‌زمان با افزایش فشارها بر آن‌ها، تشدید تنش‌ها و تنگ‌تر شدن حلقه محاصره — آن فشار اقتصادی خفقان‌آوری که رژیم افراطی بر مردم خود تحمیل کرده است — احتمال دارد که آن‌ها واقعاً دست به حمله بزنند.
چرا؟ زیرا ممکن است برای رهایی از دوراهیِ میان «خفقان» و «جنگ»، گزینه دوم را انتخاب کنند. ما از نظر دفاعی برای چنین وضعیتی آمادگی داریم.
اکنون در ایام تعطیلات هستیم و آن‌ها معمولاً در تعطیلات یهودیان دست به حمله می‌زنند؛ هرچه باشد، آن‌ها از یهودیان بیزارند.
اما ما — هم در حوزه دفاعی و هم تهاجمی — و با هماهنگی ایالات متحده در این جبهه آماده‌ایم. بله، در همین جبهه.
با این وجود، سناریوهایی وجود دارد — مانند حمله به اسرائیل — که ما به هیچ وجه آن‌ را تحمل نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70993" target="_blank">📅 13:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70992">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=oN684zzEGkagynSgoHvl-PSFbhx4z69RHxUxQsjT4m-KlkxEvYxW4wa396fSqe_Kx_WfNrvJiYNwHC9knko3tcQYPWOiPSZI9UiM1RzttsC2Oq-uG3ZhcxJwpbyVFQcqWgfdiFIynoxGpOT21Aw7EB4f-ju6-mM02TljaP75kpFHjOoFHFD5kJCg_N1RxyHavXeEpc03sUZPBy6EnkgBGMQpmp67VnNehHhejRJbS8jTM6MjW_owLQN_W7WxHJ031B2q5Bq6GSIGW7vfqtuyR7xDaPSiYaon1omGdIhLLt9WIaRzX1AHVOSAlnvXse49_i7VeN1okAls7lzE_w-mqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=oN684zzEGkagynSgoHvl-PSFbhx4z69RHxUxQsjT4m-KlkxEvYxW4wa396fSqe_Kx_WfNrvJiYNwHC9knko3tcQYPWOiPSZI9UiM1RzttsC2Oq-uG3ZhcxJwpbyVFQcqWgfdiFIynoxGpOT21Aw7EB4f-ju6-mM02TljaP75kpFHjOoFHFD5kJCg_N1RxyHavXeEpc03sUZPBy6EnkgBGMQpmp67VnNehHhejRJbS8jTM6MjW_owLQN_W7WxHJ031B2q5Bq6GSIGW7vfqtuyR7xDaPSiYaon1omGdIhLLt9WIaRzX1AHVOSAlnvXse49_i7VeN1okAls7lzE_w-mqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از فروش طلا، به دلایل کاملا نامعلومی بیش از 5 میلیون بازدید داشته!
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/70992" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70991">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/70991" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70990">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0_TbRrE_WbbIRsAd5cDYdt1HZh6FBd3QBJsYkZasQFuDyF05g0ZL_YnABVoeTHn9QXnAt9G-Nm4uVIB5Dectfd2q6ACviCAOCuXEALeL7X7fOFhGf-A0qE6GQJx3GqA2wY7t-McPqPKklXn2VgRBcjpTStuQqg1VYy2fZEnKZ-_EAvWl91vz16QX-XcGYDt5ub1G3izSWWOdIBA5Ye9xuA8Z8HCLXVXw5rqxN5uHTKawdaOgaB-7WwknuPU5CV6j57k-2fTRVbnVsR_toEMXMlxGbvLVshGo3CXspnQz_Kc4QpRiaWqd8ckJ1-BIlxO4ChSn6zGAJJWb-PGGZOmPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/70990" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70989">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1829295007.mp4?token=iLpRTRdb7jw8FTRWjJgJgVTcpsIqTqOeQfcO2f4zGyNVCdGamSdUuhjR5FsqAkGoefs3CNySVq-65LVNjgcX3__Kfmg4wn-b5XxV1AOlv5Qby9fuCSCpH9dPjcSnuxVN6AZEs-148xZF1TRV75c0fZlXsTg1jFT4-Q4_ThHAxws2khTmD9CZ_WrYcQ3rg1vyvOiog_9408qPVVZlh2EIxqv6Ac1x9MQM90Xib0toJQ_fREyBSTT0GZNQrZ7cQKxyaNocNW0UNJIFQ-J4xe6m03FjxNUKi7hHxdkUw_S7B5evYVoCa5BpeIyvCwSB0SrJkXHtHvzBOO5bqfgv3XFt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1829295007.mp4?token=iLpRTRdb7jw8FTRWjJgJgVTcpsIqTqOeQfcO2f4zGyNVCdGamSdUuhjR5FsqAkGoefs3CNySVq-65LVNjgcX3__Kfmg4wn-b5XxV1AOlv5Qby9fuCSCpH9dPjcSnuxVN6AZEs-148xZF1TRV75c0fZlXsTg1jFT4-Q4_ThHAxws2khTmD9CZ_WrYcQ3rg1vyvOiog_9408qPVVZlh2EIxqv6Ac1x9MQM90Xib0toJQ_fREyBSTT0GZNQrZ7cQKxyaNocNW0UNJIFQ-J4xe6m03FjxNUKi7hHxdkUw_S7B5evYVoCa5BpeIyvCwSB0SrJkXHtHvzBOO5bqfgv3XFt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇨🇳
⭕️
حسین مرعشی دبیرکل حزب کارگزاران:
🍆
چین سفر قالیباف به چین (و گسترش روابط تهران-پکن) را مشروط به موارد زیر کرده است:
۱- باز کردن تنگه توسط ایران
۲- دریافت نکردن هیچ‌گونه عوارضی
۳- پایان دادن به اختلافات خود با عربستان
۴- پایان دادن به اختلافات خود با آمریکا!
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/70989" target="_blank">📅 12:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70988">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعاتی پیش دو فروند کشتی نفتکش که با تحریک ارتش آمریکا خدمۀ خود را پیاده کرده و برای گذر از مسیر غیرقانونی در اختیار عوامل آمریکا قرار گرفته بودند، با رفتن روی مین منفجر و متوقف شدند و در آتش می سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/70988" target="_blank">📅 11:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70987">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtky5z1WrJU09CkmnFZBrwM3AmN17EIkDdRr0wDPODMh3hhHmFyHAWGKtQBdUd86GS_4iLuSwzQzcrTbyRB5RkJ8bJlIetc5N0j5dtthrl_p61hQUVVIB5xUg1CUHdDIbpkXFF-qJc9vIBLmpGcrC5VzZJgmNJL-ot29rR2lDQLGtNwNEWOBvyCko4I2mIoGf23rj4lCJ46fIe9HiM7lbyk-bCArLQjHBv8TuoIl9_fLY0L_hhRqTctKKpTKjHx5_XT9HrV_Jpe7BGxpQPOe4ZOfLo4umd_1vaiW3f0NWs8eiSbzovNNQ35m_Uea_wSSYWQQ6HQHoOuv5GHhlqtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
من برخلاف گزارش «ای‌بی‌سی نیوز» (که اخبار جعلی منتشر می‌کند)، سعی ندارم ایران را به پای میز مذاکره بکشانم. برایم کوچک‌ترین اهمیتی ندارد که آن‌ها توافقی را امضا کنند که از نظر خودشان بی‌ارزش است.
وضعیت فعلی ما را بسیار بیشتر می‌پسندم؛ چرا که تقریباً کنترل کامل تنگه هرمز را در دست داریم و اقتصاد آن‌ها نیز در حال فروپاشی کامل است. آن‌ها صرفاً دارند زمان را سپری می‌کنند تا با سرنوشت اجتناب‌ناپذیر خود روبرو شوند.
مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70987" target="_blank">📅 11:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70986">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=nLC-kWYNcJCoVUt4AmqBz2poCJ9l9mwNYwXTJkE04VyqshK2gigQIzbtmh8OkPr6rNlXElxl-GzrAPQAllkNi1zhotH2R4mho1jAPyQOcR-XIGmN4Eacmp55gVqe1Z5YaxZLie8X2FopXttGHp3lNtc2eHErbqvjNCj3Pg_BtDepIlR08O9TQOct_WiVuJYG_jvdh35xYntTrY3Tx3W-4HGerXEtqao_5fTL7eCBjweD30skv9T7QZSGkjPKKqCqTDLMZngFKk-aAVwbenACAlbzv8S4LX-BFttjNygZZSdgqoz2qnGfmmPa0tnFsgEJKAToWc04SlqUHuuXEoqfaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=nLC-kWYNcJCoVUt4AmqBz2poCJ9l9mwNYwXTJkE04VyqshK2gigQIzbtmh8OkPr6rNlXElxl-GzrAPQAllkNi1zhotH2R4mho1jAPyQOcR-XIGmN4Eacmp55gVqe1Z5YaxZLie8X2FopXttGHp3lNtc2eHErbqvjNCj3Pg_BtDepIlR08O9TQOct_WiVuJYG_jvdh35xYntTrY3Tx3W-4HGerXEtqao_5fTL7eCBjweD30skv9T7QZSGkjPKKqCqTDLMZngFKk-aAVwbenACAlbzv8S4LX-BFttjNygZZSdgqoz2qnGfmmPa0tnFsgEJKAToWc04SlqUHuuXEoqfaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عطریانفر، عضو شورای اطلاع‌رسانی دولت:
پزشکیان اول توسط شورای نگهبان برای شرکت تو انتخابات ریاست‌جمهوری رد صلاحیت شد ولی شخص علی خامنه‌ای صلاحیتش رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70986" target="_blank">📅 11:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70984">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EodhnD-DGysUWNu2JKgxJWhQxt7Sf62drKC01s0yYQa-enQexTcKwDWR6siEd7g7qVaoFnyHa6UrdpQaIWM2fFqb8aJG08Nz1V4FjMF9qS875vDPe3Y-woHiIphLzFaO3wkpyX0qQDoRTj5W7LpoflNdprl8zJIsmfzE0Jv6jpNhKEQU08DhFR-gBUN8MCwSC7X8LEON9Ejih8qCVPBcBk6lx25GJnE-AD-e3UTDkMICTN8IZ-R5NwCEmMmmjELtFdQmAXHHlJkmumYHGiMD8Goc0w4FxzEEFAMQkWOPXS6JsdoVBXXuQSJCjMfQN593YZEhdomy_LWwSzkCy98jWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=IeoIt4sxbMmqXogEAGHh29oO2ZN03ElfCtGPPaFSChrmfq5lDY3aA2LSIzUVEz7_VfZ64s656zXJVTh2LKsdRHnbvGufBZpa1yHAVYoylAlu4YIRHf8xmtNOc7q2kTjiwLY1eRJ4tNwwnl7pMkdDoN2bClCFgOIafh26zDc2Zdtr8qwXfji1ny4Z-v_dAaae1fewesW8090lxjo0UzxnmldYHVGRb9usO_Um9Ord-wzcizi5ZpjZ5sc7-WIKKHj6exz7EiU26PgTAz3_0ACf-hCxpSi2QpNpRM-d0BPC07tQSc2yNZl0244NeohX_CLmr9Czz9YK6mOkesKd-ZjdgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=IeoIt4sxbMmqXogEAGHh29oO2ZN03ElfCtGPPaFSChrmfq5lDY3aA2LSIzUVEz7_VfZ64s656zXJVTh2LKsdRHnbvGufBZpa1yHAVYoylAlu4YIRHf8xmtNOc7q2kTjiwLY1eRJ4tNwwnl7pMkdDoN2bClCFgOIafh26zDc2Zdtr8qwXfji1ny4Z-v_dAaae1fewesW8090lxjo0UzxnmldYHVGRb9usO_Um9Ord-wzcizi5ZpjZ5sc7-WIKKHj6exz7EiU26PgTAz3_0ACf-hCxpSi2QpNpRM-d0BPC07tQSc2yNZl0244NeohX_CLmr9Czz9YK6mOkesKd-ZjdgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
🇮🇷
پوتین در دیدار با پزشکیان:
خواهش میکنم سلام گرم من رو به آیت الله سید مجتبی خامنه ای برسونید
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70984" target="_blank">📅 10:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70983">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=axQuvNryNzx10VlwQnDpLxOPkV4AiMPtEQPSEZgBib_QTZ_5MObaqTaN9cO7Slz9sZwfurdlGaMvccmBZuG8QT6vd8YwE2BdKDXoQ3P0IAPNVaorHbsuai1WrGXxcOQpyU_cBjWefp124LlJaKyo2T61RI6ZDD9BBT1Ccs3aFRRExHYblPZpEBBi-D1-oPQCU_hBhXJ0mI3wQ6gIVmuZsFEPRw612MqMfnB2FgqtZLncNuyncyAjB-ZWLlc2g5GDb9PAX64LaBoZ0CW4kcFcqL5lMVvLyD2L16OMzud6X8YCPTwPNmj9-4bFWyHh-WaHHMcvrSZW2-WXNoQeU7tfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=axQuvNryNzx10VlwQnDpLxOPkV4AiMPtEQPSEZgBib_QTZ_5MObaqTaN9cO7Slz9sZwfurdlGaMvccmBZuG8QT6vd8YwE2BdKDXoQ3P0IAPNVaorHbsuai1WrGXxcOQpyU_cBjWefp124LlJaKyo2T61RI6ZDD9BBT1Ccs3aFRRExHYblPZpEBBi-D1-oPQCU_hBhXJ0mI3wQ6gIVmuZsFEPRw612MqMfnB2FgqtZLncNuyncyAjB-ZWLlc2g5GDb9PAX64LaBoZ0CW4kcFcqL5lMVvLyD2L16OMzud6X8YCPTwPNmj9-4bFWyHh-WaHHMcvrSZW2-WXNoQeU7tfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رکورد دار عمل زیبایی بین آقایونه و تا حالا بیش از 300 عمل زیبایی انجام داده!
پسری که عمل زیبایی نکنه اسکله، تا حالا 200 میلیون خرج ابروم کردم، 150 میلیون خرج لبام شده
😶
استایلم فقط 400 میلیونه، 500 میلیون دادم که خط سینه بندازم. پسر باید به خودش برسه.
هزینه روزمره‌ام روزی 100-150 میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70983" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70982">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⏺
🇮🇱
نخست‌وزیر نتانیاهو:
آیت‌الله‌ها می‌خواهند من در انتخابات شکست بخورم؛ حزب‌الله و حماس هم همین‌طور؛ و البته ترکیه نیز خواهان شکست من است. آن‌ها این را آشکارا بیان می‌کنند.
صادقانه از خود بپرسید: دشمنان اسرائیل می‌خواهند چه کسی در این انتخابات پیروز شود؟ به شما می‌گویم: آن‌ها نمی‌خواهند من پیروز شوم.
ما برای کل جهان آزاد می‌جنگیم. آن‌ها این را می‌دانند و به همین دلیل است که می‌خواهند ما شکست بخوریم.
ما اجازه نخواهیم داد آن‌ها پیروز شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70982" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70981">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=rnTZ7ccg0Kvkw4CsQxuIDo3yEfrimqOZUwBywnKFETWdooxYetq8yK9JYb7xQAlnin8EcXaf1JovNdRyUl835j7BzuvJetOFGz_YH0BIRST4mflyRQyWZnzfoa8jxtqyaNl9FFWKKWGQwhC5ppmzrNUFNARTKFUv3moAGau_pUKhBF9wTiVTwiE1CjsZa_uQv62vT6ro7dNYVAZ6FlHkHhNqpLu-2AlHgZ4wOnGHn-3FdB5U0vGMR4VhS-wKDEPVdl2sBP3mhubsSCGbgdVpX9qIFxxTqjIOqEIr_1xxqjPh-CzYkOhAEpqTJBzj47UkkouZnThc0Xl6N02XYpDo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=rnTZ7ccg0Kvkw4CsQxuIDo3yEfrimqOZUwBywnKFETWdooxYetq8yK9JYb7xQAlnin8EcXaf1JovNdRyUl835j7BzuvJetOFGz_YH0BIRST4mflyRQyWZnzfoa8jxtqyaNl9FFWKKWGQwhC5ppmzrNUFNARTKFUv3moAGau_pUKhBF9wTiVTwiE1CjsZa_uQv62vT6ro7dNYVAZ6FlHkHhNqpLu-2AlHgZ4wOnGHn-3FdB5U0vGMR4VhS-wKDEPVdl2sBP3mhubsSCGbgdVpX9qIFxxTqjIOqEIr_1xxqjPh-CzYkOhAEpqTJBzj47UkkouZnThc0Xl6N02XYpDo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
سنتکام ویدیویی را از حملات به ایران منتشر کرد؛
سنت‌کام، فرماندهی مرکزی آمریکا اعلام کرد نیروهای آمریکایی در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
بر اساس این بیانیه، مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، زیرساخت‌های مرتبط با مین‌گذاری و مراکز ارتباطی سپاه پاسداران هدف قرار گرفتند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70981" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70980" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70980" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR-oWidxX8FJ5h-3VYMT_PKscKHmVK_iduQx_1Zr5IlnGTv-p_EDtA67E9lRRi13JXJOx12fUxiWSQYdrE0HJMJyu2Z2H6IhkqK_RH2ZR7MroCTssCSHIAN67C66Je_ImXzpP80k5UJgBC7fcNcNMcJcbPP6lxJbo6NgWmxNwTOIPNR_WZ8XwjCAMc5E91387nWx-6iS7RLHTtuVkrOqJ-yfwNqmpiYK6b3AgbenznyFy_U1x8Lifd_ctaGPR5ZFy30ZS9NZANB645B1vfohryNFadHwzjOCfO2s71OURp74wS0PDkhRQAJh-zw_XieijrxGDf5SBfS8mpUKNyMZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
سایت جهانی
TrexBet
می‌برتت وسط
جنگ
بزرگ!
⚽️
استقلال
🆚
پرسپولیس
⚽️
اینجا فقط فوتبال نیست… دربی‌ـه!
۹۰ دقیقه جنگ، کری‌خونی و هیجان تا آخرین سوت!
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70979" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70978">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در کویت و بحرین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70978" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70977">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUVVpqrVrUV1Rv9Ys0ZsO-Y8MBxTveRdLIRkeyh9Gf9md0l1yv2K_JJ5fte4SGMrNP0yGyitG_SH56rZ5nSFWvZH_Biwdtc7XgxfjRJ2WzOeSfgxVzq8p74Vn_wtj0ZGYcZ80ixxPNwpvu0jAZvi7LJv_CsPzlYY8pVSjO_rBEdUJT8s9XL3e201L0MWkZQOCg6sMKCcgVFP87nXlFtE3eR7Dk9JurfGTqhgMkzqbMBi5NeGUTeVgJjTedCpLaZTuBbfYqWPq6FUR-x4p5YGwFIaRHdcmR_Ao78cAGTR_C1mq-iWbqtpWFfdXzAGfocFHmALVNSM58CO3geEm4vYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70977" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70974">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⏺
🇯🇴
نیروهای مسلح اردن:
پدافند هوایی کشور ۱۳ موشک بالستیک را که وارد حریم هوایی پادشاهی شده بودند، رهگیری کرده است.
به گفته ارتش، ۱۰ موشک رهگیری و منهدم شدند و سه موشک دیگر در مناطقی دور از مراکز جمعیتی سقوط کردند.
در این حمله هیچ‌گونه تلفات جانی یا مجروحی گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70974" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70970">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kFkoqOvXLYEP8dqy9Fye9j866PrTZPwmI7sDPJA8dih0zesHLSa3wrWd9ON0VdzNnTIahltJLDv19u8f-LAOxA3ovooMxg1cXjWPI1YBKD7QuB3b1Honk1BROuIskc8uORBJKhh3eXgf6aAT8LPmbKrZ95x7tI0bj8YyoKRAxPCeN2MNys5SwOqLh9Mlb21NfE9Wy6CkNCiJXqGohZ8Bi7zYKCQJey4IjfggeolKJWwOn-OkhQ6YWYuMDFtC03U3eUfgnHuWjcJnF259lTsL-8rsCksYV7r3QHHTGGQC6IfWHAx4CkUGUfSB2CH4TxytHyKj8-9k-3NkfoMq6mKpvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/703c34050b.mp4?token=o6cJbPWqDKCfl-3DqaEvIvnpIUQ4WZMZ6N9CJrESOnhaLwEtZwjh5u30VxkP-ut22rPRWgc68x-RUbswFJVN0DCGqS3v70KlwUzG3pN-n939j4Y2SVzyZdoBgZ46CSkEkk0hwDlnk_5RWbHRwecX6LzWwmvSSlL1op9S2tkO8y188lrkY57qONX6DwNv9uicN7vkMGJWYdiXhHl0Vd78mlsB06lMD8HHsUPKUrHpmNktA7ABlqEy9Iit0Y7JjcCKHfGyREpzpUlW_EZr6YNc9k8qn-HUySmOIqn_26c8pjrpHW4CkJdrpHlP8C417KLeskrHHYOY5aVI_7A4pezZug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/703c34050b.mp4?token=o6cJbPWqDKCfl-3DqaEvIvnpIUQ4WZMZ6N9CJrESOnhaLwEtZwjh5u30VxkP-ut22rPRWgc68x-RUbswFJVN0DCGqS3v70KlwUzG3pN-n939j4Y2SVzyZdoBgZ46CSkEkk0hwDlnk_5RWbHRwecX6LzWwmvSSlL1op9S2tkO8y188lrkY57qONX6DwNv9uicN7vkMGJWYdiXhHl0Vd78mlsB06lMD8HHsUPKUrHpmNktA7ABlqEy9Iit0Y7JjcCKHfGyREpzpUlW_EZr6YNc9k8qn-HUySmOIqn_26c8pjrpHW4CkJdrpHlP8C417KLeskrHHYOY5aVI_7A4pezZug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
امشب از نقاط مختلف کشور به سمت مواضع آمریکا موشک شلیک شده؛
🤩
تسنیم:
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70970" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70969">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
⏺
روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)" با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
عملیات انتقامی نیروهای اسلام ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70969" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70966">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peKQo_eXlBD-0ZkN9CCpn1GvJvDttMhlqG72g3Bs6MftG1uWS7f07lucRw22548CAIWEnanGuhit4bQIO8EFA5yEa9mo0au9piVFWuaspCf33tJvjgmaW-uF2cyU76lR4Vmky72HFD14yhzKorpKNjpILdHK4ziNL9R5pq9Pdkh_ZxrUSwSBoK5ihHEKYuiDPYE4tA5snW7A2CgGv2iA-7ceqslVmuYQxB3pI2MLssOZ-9EbkIe-jkfzHeFi_znJQfAaWfRBfNX4KbIFqQs7G7s3D5g1IPwG3q_n7wKhKX_GjIT2xnVTd_Qy2PFtvl2GMd8NiyRtk8nUBdpor-eMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=H8tpHMshtmeqR6KuD47RsIFYxJ1E8qIcV6I242QSNHhHqwRdsPvUgaJf4rp4o4mh3ZJIdOK02MtFKb3d9DJdp7ihxH-mWybgZ-ZmFbv_prQACRJyyfJdoEhfZaPN-GuKWxeVbsBBY0MOW8LYTe2ixEgnWpz4UdhTKnqCguSYRxs9itWyLWYozNFPypKTRJUXalR5XbyS7UJO5CWOA0F2ynCOXLMaJErzy7D7TT6ndNBw2iptqQMLdqTwrEDBgBTY-6HRSQlLfpsLB-T4YtXWiKk47xWxIa9egJVTed6_zUPzE6GXaabeqr9YJvAjVscVqnAbqGEMhnMbWwKUtZjZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=H8tpHMshtmeqR6KuD47RsIFYxJ1E8qIcV6I242QSNHhHqwRdsPvUgaJf4rp4o4mh3ZJIdOK02MtFKb3d9DJdp7ihxH-mWybgZ-ZmFbv_prQACRJyyfJdoEhfZaPN-GuKWxeVbsBBY0MOW8LYTe2ixEgnWpz4UdhTKnqCguSYRxs9itWyLWYozNFPypKTRJUXalR5XbyS7UJO5CWOA0F2ynCOXLMaJErzy7D7TT6ndNBw2iptqQMLdqTwrEDBgBTY-6HRSQlLfpsLB-T4YtXWiKk47xWxIa9egJVTed6_zUPzE6GXaabeqr9YJvAjVscVqnAbqGEMhnMbWwKUtZjZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه امشب یه خبر بد هم داریم، در طی حملات آمریکا تو بندر کوهستک حوالی سیریک، ترکش حملات می‌خوره تو یه مراسم عروسی و چهارنفر جونشون رو از دست می‌دن
🖤
#hjAly‌
@HutNewsPlus</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70966" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70965">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxhZLVfqMfnAGYd5Tm2hIyKrXZQ2nKbLgwGst9HkSLEILdII1LN-e4bvGgiyS4Qv8eeexdiOpILqQYkPBNyhUw4Qgq1Pyr9xB_4ueMbsVpbfcPDiAf_DFrVzuTMeCzUj7IhWK5BCq58fbrYuUCIj7P0Xw_8oUwNVrosbDEuxkpIsS3YCMrouvXupdnA5idcDxLAcmgX25j1NrKYTAaB6gcIGARbtaMCvHxWGsvimWy1ugCrXkD8S7EqO5alVHaK8imqlkzlVw2WbN-6QIo9e9dCU9Ne-DqzEYMltCJxVCbM4_J8sUiUmyCjXKWvqzAq22xjcx8TRm2aogbi26RIR-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.  @News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70965" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70962">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=FfHgzOVAndAaI6WgNsZmwjEW1Bj1Xl1rZvwv3mFgiJQ7IiprPODMQqDTjVKyQqHBddJqkuVEAGdiRDLG2ONWzFoi3kfUYTCInVCxxpEqRCuMPzjOuYVrfVKqzXiijUsoGDn-x085UL8P4qON8LtgEks1_dfIfChxV669EGdary6BjtXMGIjVzFh4ZsPQfi6MZrB8kx31nXH1KdwZK6d9EEV8szbd9q_Kkr3N4NHnhq1y4E4mJZz6_0tv6-FzclxHBvzrEPS7c9deat_pK6WORcsHs9AZz5RZUxWFNZLConM-wtSAd25pJlYFHX-BgbuhDE5Sw9y3N_e9ER11rzviCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=FfHgzOVAndAaI6WgNsZmwjEW1Bj1Xl1rZvwv3mFgiJQ7IiprPODMQqDTjVKyQqHBddJqkuVEAGdiRDLG2ONWzFoi3kfUYTCInVCxxpEqRCuMPzjOuYVrfVKqzXiijUsoGDn-x085UL8P4qON8LtgEks1_dfIfChxV669EGdary6BjtXMGIjVzFh4ZsPQfi6MZrB8kx31nXH1KdwZK6d9EEV8szbd9q_Kkr3N4NHnhq1y4E4mJZz6_0tv6-FzclxHBvzrEPS7c9deat_pK6WORcsHs9AZz5RZUxWFNZLConM-wtSAd25pJlYFHX-BgbuhDE5Sw9y3N_e9ER11rzviCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تو وکیل آباد مشهد یه ماشین به تجمعات زده ٢٠ نفر کشته و زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/70962" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70960">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IheemEU9hD3xHqqE4kS1y_DwGGmsNOrsqyKCLDoAzbUUSLHgAXpUZpyzq7xQTFa_2CPCNk2pk0v1Q4F9kvcWH5PH9N6eklrcqQ1uxyL6ss2QFQNwTBR-1nyKMt9Md13rQ2trxCnW9sEyVTTwOV_IkcYNPKgbvxNk_wriecVVpx1dqTprNFB4E1Z0QMXleh-7v2O2GjtxmrHLRQzokX-Biad8kbzpeHDpHtVHJ_5F2w5a6PZ0dyNiKDcMxg7MvKDxz6h_oGMFq4iE15Rcf3iK_N-hTb5rLdoVc68SUVjCrssPTn_UTiOHpBmiLmL5P-Vj9RBRshNGnsFjs8yLhjGKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=JsFSPkmu81aqBdoH5cnH6olURY0awFSmwNCteNLNEQUQA-EzSfCIFMKhyXeaY5tWo7njjylvVVBOBLy044h6FU0yhw7gdUaPPQ91AEJwt69JrLpXy8vg6Q4G0WjoPIalYVbgSOotOBwI8GLIYXZlFw2UgZphpzwi6bAKSbcMm77RE0JrmeKS4YrJoqaBCFTndQx_QAnu8kpPOiVWUDyykOfItq2iXRAHJz19BduZtnWwthxBOcNbOs_ET43PFNYnxTxJYSB9b6bLqoyBsgF2VC1TXXw3BJ4ijwXOF5dXMNwfwvwSIgVnh79gJF-1och3q-A2BrBNc0wrefWVQIFf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=JsFSPkmu81aqBdoH5cnH6olURY0awFSmwNCteNLNEQUQA-EzSfCIFMKhyXeaY5tWo7njjylvVVBOBLy044h6FU0yhw7gdUaPPQ91AEJwt69JrLpXy8vg6Q4G0WjoPIalYVbgSOotOBwI8GLIYXZlFw2UgZphpzwi6bAKSbcMm77RE0JrmeKS4YrJoqaBCFTndQx_QAnu8kpPOiVWUDyykOfItq2iXRAHJz19BduZtnWwthxBOcNbOs_ET43PFNYnxTxJYSB9b6bLqoyBsgF2VC1TXXw3BJ4ijwXOF5dXMNwfwvwSIgVnh79gJF-1och3q-A2BrBNc0wrefWVQIFf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به دکل سیریک که با پهپادهای انتحاری لوکاس(کپی شاهد) انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70960" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70959">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541d79e411.mp4?token=tABDNBKZQJjCtWSZwcDymkQKGV8YRSc77A_6rLxRpNt5WTrdadslcML9Ikzk6TkoWv_Y5oqTTvq5D73EgBO68v0yvsPg3pWerrC3oUR3EKtsoVtflqit5Gh8bF-6mA-w4Tky7-Y0kY4vFvg8lcQZLo9BqBO6Kmbugb02HfZIs2pyWeQy-ijqEarFZM0tnYtkH67aUtAHqy4d2oIi3XJdL7pJ3fxRqjUlm4Ks-X7PXlmGEG55t3LoVwQngUQonco79eERaN8K6sBicdhVr5hdITT_aIFwJ8UhvJsfxIFGKwNTLGtpLkbpjcYpK9l1MHsQ-SeZZaPPc4KG-Tm7LdnXJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541d79e411.mp4?token=tABDNBKZQJjCtWSZwcDymkQKGV8YRSc77A_6rLxRpNt5WTrdadslcML9Ikzk6TkoWv_Y5oqTTvq5D73EgBO68v0yvsPg3pWerrC3oUR3EKtsoVtflqit5Gh8bF-6mA-w4Tky7-Y0kY4vFvg8lcQZLo9BqBO6Kmbugb02HfZIs2pyWeQy-ijqEarFZM0tnYtkH67aUtAHqy4d2oIi3XJdL7pJ3fxRqjUlm4Ks-X7PXlmGEG55t3LoVwQngUQonco79eERaN8K6sBicdhVr5hdITT_aIFwJ8UhvJsfxIFGKwNTLGtpLkbpjcYpK9l1MHsQ-SeZZaPPc4KG-Tm7LdnXJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
اصابت موشک های سپاه در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70959" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70958">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
‼️
وضعیت دکل مخابراتی کوهستک سیریک که امشب بهش حمله شد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70958" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70957">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خود ترامپ، هگزت و بسنت هم پشماشون از این حجم از کله‌خری سپاهیا ریخته
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70957" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70956">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
از بیدگنه هم دوتا موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70956" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70955">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
شلیک دور جدید موشک های سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70955" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70954">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">من فکر نمی‌کنم ترامپ قبل انتخابات دست به حمله‌ی گسترده‌ای بزنه، سنا تو تصویب بودجه برای جنگ نقش اصلی رو داره نباید بیفته دست دموکرات ها
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70954" target="_blank">📅 23:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70953">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=XW1OTUDDtvcHDnR8MP-H7T25kHo9TiP7CQwouUUTuZdoDKJUw5iKVcIh231NXXx-D3bd6WKWgGsaa32zHlBCu0oFpLe52jLGneRG6YRCRZcKnUEXXzSbBl6y_SjaKJWzom1i385-TgKYSNRMa8tB8vmQb996HyCUl25AeVhVodEjAAUQcddaGIy9UiAPU0iwX-nVScBF0ysgTWK2Wmc4f5naLTYxRAIK_yncXmN1Wg_3plDp57AZ6Efeo-DVhejSdL3N_W_RRrVVA9Kj1v4oJYuBckT86fjXrX5T19B-vuHWB631NsX6aXT3mjlBUvrKPxYb9Pw7iKvAcebfirRHag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=XW1OTUDDtvcHDnR8MP-H7T25kHo9TiP7CQwouUUTuZdoDKJUw5iKVcIh231NXXx-D3bd6WKWgGsaa32zHlBCu0oFpLe52jLGneRG6YRCRZcKnUEXXzSbBl6y_SjaKJWzom1i385-TgKYSNRMa8tB8vmQb996HyCUl25AeVhVodEjAAUQcddaGIy9UiAPU0iwX-nVScBF0ysgTWK2Wmc4f5naLTYxRAIK_yncXmN1Wg_3plDp57AZ6Efeo-DVhejSdL3N_W_RRrVVA9Kj1v4oJYuBckT86fjXrX5T19B-vuHWB631NsX6aXT3mjlBUvrKPxYb9Pw7iKvAcebfirRHag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم‌اکنون حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70953" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70952">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=Kba92_2vGNGlgF9ur4oXh1bwkkRJlwy37o5y1IA8350hEcgHMVN1FTlv2iwtByafJF4QHSM28r3_xwFTmmNNbaCzwXdZAS-mSQhF9Z_TpQoxUvk0oVX_4CIyAyWH5qlpqmmqivGgG4_nPCoYrLshR3X1djohopUN-E22Td8NuVAkPcQJx6GzTg9VwNQmOsP1ur1GBjg8BLimivKJgnA5THMIZVrVXyZYf7Po0qsoCFhrJUxC6GHBY8ERc_tj0Vw2bUpTqTGQ3oemwiVCYlLq2s3E-GYE3KC1O8YYfEdXGz7-HFZLMJhkl3_dqjpwkmvPIkAXKM58ExcN-f0msP5HAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=Kba92_2vGNGlgF9ur4oXh1bwkkRJlwy37o5y1IA8350hEcgHMVN1FTlv2iwtByafJF4QHSM28r3_xwFTmmNNbaCzwXdZAS-mSQhF9Z_TpQoxUvk0oVX_4CIyAyWH5qlpqmmqivGgG4_nPCoYrLshR3X1djohopUN-E22Td8NuVAkPcQJx6GzTg9VwNQmOsP1ur1GBjg8BLimivKJgnA5THMIZVrVXyZYf7Po0qsoCFhrJUxC6GHBY8ERc_tj0Vw2bUpTqTGQ3oemwiVCYlLq2s3E-GYE3KC1O8YYfEdXGz7-HFZLMJhkl3_dqjpwkmvPIkAXKM58ExcN-f0msP5HAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70952" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70951">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رسانه های حکومت: آمریکا یه مراسم عروسی تو سیریک رو زده و چن نفر کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70951" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70950">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">همچنان هیچ ویدیویی از موشک های سپاه تو آسمون کشور های منطقه، منتشر نشده
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70950" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70949">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  اگر ایران پاسخ دهد، انها از بین خواهند رفت  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70949" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70948">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70948" target="_blank">📅 22:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70947">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=HL41QcGzc8nKEFcVHSB83fA-W5Cls3_XpmVhhfadUFHzs2UpQJT6KxFTu8zZAmgqdhEMNfPkVH4MrG3u_iLsMet7b27z4iqPHLUrAgu968nWrEBaMrTzxffvBVC5CoSDpZ9Gv74qnouxDpMdYX7ME57mmlYuFYSHmlvBHHCeK-Twb1kIItUl4cQ2e2Oh66zTY5GP0YiZNcN2dq3dwkRkW-r5sv-OTTGJ4TaxHC7AlwWtuph5XX658zPumW-ycJ4OIkLSqJOzF4b4-mHnAxSmlpoLHfNKFWWc0vcT1ysWelPiH8lPa_ZXcx4r2NvbO1OCUfzBjvQ0o9EGgJWsZAdNDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=HL41QcGzc8nKEFcVHSB83fA-W5Cls3_XpmVhhfadUFHzs2UpQJT6KxFTu8zZAmgqdhEMNfPkVH4MrG3u_iLsMet7b27z4iqPHLUrAgu968nWrEBaMrTzxffvBVC5CoSDpZ9Gv74qnouxDpMdYX7ME57mmlYuFYSHmlvBHHCeK-Twb1kIItUl4cQ2e2Oh66zTY5GP0YiZNcN2dq3dwkRkW-r5sv-OTTGJ4TaxHC7AlwWtuph5XX658zPumW-ycJ4OIkLSqJOzF4b4-mHnAxSmlpoLHfNKFWWc0vcT1ysWelPiH8lPa_ZXcx4r2NvbO1OCUfzBjvQ0o9EGgJWsZAdNDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب ناموفق موشک سپاه تو خمین
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/70947" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70946">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».  رئیس جمهور گفت که این حملات سیستم‌های…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70946" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70945">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=Zri3MsPR4BBH6AgpVxHSP9VFzHyk5wrfdqj69Ccs-kncmks7gpFj0LggRjAu1HpnEunLDwNadXgO8uwO-Tq7He7IK7kr7OPTmEKaueyuobqYzqBmbb9-Munk3pKdRBq_pvMgKyklQrkMaOyyoL6cmaoeRVHMaKj3U6YAv_GzIzyaVGKsHwrpNoDsEDV-Va9W_N5LozacVYlnj98P_n4Rkd_jwzQ0czYPx_j-o7Xrjzqygb5QeOdy8UCOE7cuzpTL1TRlgU8MvXjcBL-jzn5ZMByvEePNnKmttlgy5OzSed_ABTnrQ4BbtKIHwTumLJiQ5bS-5MtBqDIhERUA8ZM0qGjvpQo-xGTdHppA2a8QCoQvrhk4sVGI4aO_f0SIpoD3fjsT89LmMITIjkbYzkReDzVFPGJZY_DNrSVSuKeZeSakpVj1OIqn2fQsvATVr7kTdXDaUF_4nhp_DIQzwfVnaUFjupcNhghYkOxEo2ylZ3Gyp2IhiZ-UqEA5G8bSR3RSywanAcjZONvalHrgZBtqKAP8_dyWR6Q5kcPcErOc5wKBh9ppmDvvMj-wbY0BNAzMQmst3T683fT2_bsweXuq6gHqBPd2ymcTOWPNIkMZ2QLwEGKjFvs-qefUC9dQqZvs0wJ0v8GZPSp8W9-2dzh1Zii1tol1WNHptDOELWwZ4Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=Zri3MsPR4BBH6AgpVxHSP9VFzHyk5wrfdqj69Ccs-kncmks7gpFj0LggRjAu1HpnEunLDwNadXgO8uwO-Tq7He7IK7kr7OPTmEKaueyuobqYzqBmbb9-Munk3pKdRBq_pvMgKyklQrkMaOyyoL6cmaoeRVHMaKj3U6YAv_GzIzyaVGKsHwrpNoDsEDV-Va9W_N5LozacVYlnj98P_n4Rkd_jwzQ0czYPx_j-o7Xrjzqygb5QeOdy8UCOE7cuzpTL1TRlgU8MvXjcBL-jzn5ZMByvEePNnKmttlgy5OzSed_ABTnrQ4BbtKIHwTumLJiQ5bS-5MtBqDIhERUA8ZM0qGjvpQo-xGTdHppA2a8QCoQvrhk4sVGI4aO_f0SIpoD3fjsT89LmMITIjkbYzkReDzVFPGJZY_DNrSVSuKeZeSakpVj1OIqn2fQsvATVr7kTdXDaUF_4nhp_DIQzwfVnaUFjupcNhghYkOxEo2ylZ3Gyp2IhiZ-UqEA5G8bSR3RSywanAcjZONvalHrgZBtqKAP8_dyWR6Q5kcPcErOc5wKBh9ppmDvvMj-wbY0BNAzMQmst3T683fT2_bsweXuq6gHqBPd2ymcTOWPNIkMZ2QLwEGKjFvs-qefUC9dQqZvs0wJ0v8GZPSp8W9-2dzh1Zii1tol1WNHptDOELWwZ4Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».
رئیس جمهور گفت که این حملات سیستم‌های راداری در جنوب غربی ایران در نزدیکی تنگه هرمز را که در حال بازسازی بودند، هدف قرار داده است و افزود که ناو هواپیمابر جورج واشنگتن کاملاً مجهز است تا در صورت نیاز به عملیات خود ادامه دهد.
ترامپ همچنین احتمال توافق جدید با ایران را رد کرد و گفت تلاش‌های دیپلماتیک قبلی شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70945" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70944">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس از آغاز حملات موشکی سپاه به مواضع آمریکا در منطقه خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70944" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70943">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
"اگر آنها تلافی کنند، ضربه بسیار سخت‌تری خواهند خورد. و اگر دوباره این کار را انجام دهند، دیگر نخواهند بود."
"آنها متوقف نمی‌شوند. آنها دیوانه و احمق هستند."
"آنها سعی کردند رادار خود را بازسازی کنند زیرا نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و سپس به آن ضربه زدیم."
"من فکر می‌کنم توافق با آنها ارزش کاغذی را که روی آن نوشته شده است، ندارد. ما به آنها فرصت‌های زیادی دادیم."
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70943" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70942">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در گفتگو با فاکس‌نیوز:
اگر ایران به حملات آمریکا واکنش‌های مکرر نشان دهد، ممکن است «به‌عنوان یک کشور کاملاً نابود شود».
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70942" target="_blank">📅 21:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70941">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=Lc6AjCfCsDEMF093PTLz_LTIoL--kbbIeWTwKgw_BsQALbv0b0ergFJ3HDidwSqe90Sb7tniNUwsYwkcEyJAKKpAMtEUIk1k433hasV-yGTPZs-ENOGLvXf3FAjhO3-g_YIDcAtmC3OQkhux1cH-SEDAjEwrv38nKAURJulkLy9Yo2pDfNwlj-oQsgkb8RVHxqTC7kQ7A7pJI-058kkXWC97pMSDoWpEw5ouR8K_vu1bjjWNR9Lb7j1HTN1wFOB9S2S3pgymMRNUgzTg41c9UwcxH4yHEwQ6aAYGjTzSLEvTLyrbdSAiVFcHaluhoa1Y8ymjvbDCP_kNczY0e1LulQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=Lc6AjCfCsDEMF093PTLz_LTIoL--kbbIeWTwKgw_BsQALbv0b0ergFJ3HDidwSqe90Sb7tniNUwsYwkcEyJAKKpAMtEUIk1k433hasV-yGTPZs-ENOGLvXf3FAjhO3-g_YIDcAtmC3OQkhux1cH-SEDAjEwrv38nKAURJulkLy9Yo2pDfNwlj-oQsgkb8RVHxqTC7kQ7A7pJI-058kkXWC97pMSDoWpEw5ouR8K_vu1bjjWNR9Lb7j1HTN1wFOB9S2S3pgymMRNUgzTg41c9UwcxH4yHEwQ6aAYGjTzSLEvTLyrbdSAiVFcHaluhoa1Y8ymjvbDCP_kNczY0e1LulQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیویی دیگر از موشک سپاه که در خمین سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70941" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70940">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=b0fnYeV_5yS2i2bsnlAN2PSsbmA56BIEXeb8Pgjax7L_DGlVfT7XBLmQ3WK1SazBjOythsxZwo9wFQogRTj4JOd5lYwWxnnpAbVpLIu-ZI9ig2cOSZ6QWxlTkghyF7m-V01mx_APpsRciUcnEttorFdKD_Wqt0vC_HoNp7KfhQHCsXJG2kiLY4FfZ3WvMvcTKH7yhM0YL9uGWskbsOjuEiMYh9uzpZ4Y_dqWlLjIVQDUntUpsYHGhU_nAtvKI1m9jfV22LC-BMi4Oka_JHNuZiY8EhJ6vCpzx3IZtXbFtFdc3lTyjucytKiBl5PXoX5Kh33PYIC8pkUQ1uKFXu4naQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=b0fnYeV_5yS2i2bsnlAN2PSsbmA56BIEXeb8Pgjax7L_DGlVfT7XBLmQ3WK1SazBjOythsxZwo9wFQogRTj4JOd5lYwWxnnpAbVpLIu-ZI9ig2cOSZ6QWxlTkghyF7m-V01mx_APpsRciUcnEttorFdKD_Wqt0vC_HoNp7KfhQHCsXJG2kiLY4FfZ3WvMvcTKH7yhM0YL9uGWskbsOjuEiMYh9uzpZ4Y_dqWlLjIVQDUntUpsYHGhU_nAtvKI1m9jfV22LC-BMi4Oka_JHNuZiY8EhJ6vCpzx3IZtXbFtFdc3lTyjucytKiBl5PXoX5Kh33PYIC8pkUQ1uKFXu4naQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نقص فنی موشک بالستیک سپاه پاسداران در آسمان خمین
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70940" target="_blank">📅 21:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70939">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRi0guUhbppDIk4DwP_q9g5sjGOKVklBQf8tBlvh2azbkvb8RgnY3wziqOCiumDNva1GYtwmIzyvENBx_WiXD99nOOZVSrIp23fwCHCCG98xlRuvsNfvMhwqyivEj-U1DSbwRVf_ozfAoK8RCdDXHhMaAqiX1gZSpe7KnBlkyVT0qNwz0xCeEiBPecR0eFb19z3AIEY7k2wKFHJs2DYMVkY03L11SHutwZHhxTv8MShi2JGcG6lLQylacTEHw2ATGqPlU9gSDvq0FvbtfG2l-wDB9uhat8PpKunNhBZ9PPZYEZTpGHZOGKNfulvfFK4tqZiTL3wh--P1AKvmgNpDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ستاد کل نیروهای مسلح: هزینه سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔴
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا:
در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان و بلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
بارها اعلام نموده ایم و اراده کرده ایم تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70939" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70938">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
گزارش انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70938" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70937">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD0ckog6NXCmQ_kWRyhSnn5SpWSZ8zOmrzeASzkfM5EPcL_w1FukIOQvYKN08VItCFhTNlHvu_C00HfcWO2DKynfCO9-0SFDJd5z_kMGefMpwVbuAAbZJ_Ga5rf9oU6NZ5fUhEVPWa3N9V3jcNOGqCi_zZ_iYly-gb2feZfYKUFYRIlSv4Gg2otniWom4dDlpQ13frbvMt4gZdQRyWOYjtArhwWb0EhKKuGUQ5GidNiC0qZ7z3NmGE7vVSr-PhC0VBEeI2eiOJYiXVPjG6rp51b31UA9f86xqiRbGOQ5Sr4K1k7J7GpNNdNFBp1wL8hpJLz4YejaRH-8cJyY1vGjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:ایالات متحده همین حالا در حال هدف قرار دادن مواضع ایران در نزدیکی تنگه هرمز است.
🔴
این حملات گسترده و سهمگین هستند و در واکنش به دو اقدام صورت می‌گیرد:
نخست، تلاش نافرجام ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه‌ای که در حال حاضر فاقد هرگونه مین است (مین‌ها کاملاً پاکسازی یا منهدم شده‌اند!)؛
و دوم، شلیک هشت موشک از سوی ایران به سمت پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر ایرانِ شکست‌خورده بخواهد به این حمله کاملاً موجه پاسخ دهد، بار دیگر با ضرباتی بسیار شدیدتر و سنگین‌تر مواجه خواهد شد؛
🔴
اما آن حمله، بزرگترینِ حملات نخواهد بود، چرا که حمله اصلی در کمین است و پس از پایان آن، چیز زیادی از جمهوری اسلامی ایران باقی نخواهد ماند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70937" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70936">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⏺
معاون امنیتی و انتظامی استاندار سیستان و بلوچستان از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70936" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70935">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBKfzUABv-c62-MyrDzbc1wpt0E30Vj_LWodbNgLUeS-sGFSk9gZM1QlPCSo9u9NhVUB-zZtTAZFQVhH-IXmKvjNjZluhGf3MR7X8Hb-zyyURGbHgI-BS4d2jrEuQBWnrjoW8cXpWTysoztasRiUSNDlXQn3JVgjMo3v0Gus7qCGlgPvEESF4HXlZToG7KPrTWCyc078Ww9lwMsNZupe3awEIPTUc2KXpZbcdw3-ZrZaySh9neM6M9wAuiPLSrT29KzxD3RrW2H0dymzLffWv1f49c0TM1eRq1x98R5adBZbCccR7arMCaQV7GL-AOWzAIjBxPwcIGl2X7rDxlcOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70935" target="_blank">📅 20:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70934">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
تا اینجا در چابهار، جزیره قشم، بندرعباس، کنارک، جزیره لارَک و سیریک انفجار گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70934" target="_blank">📅 20:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-jI8cuq1dtAXMauYkKfiidN-DpBmmzxvv1oEWPmho_cFWDzcJysLEfq88Q7aWxYn7y_B9z_7ZTEwAJBm38AqwrF-Kas6K1RYhgUZrDh7TlJZ8BhwCX62RzL-yUAYtdfSlt1JWFUk50846faQ0vq1uF-BqAoZvgYccseIK_FSTlK6rWma9JTs6b7GzJjqq_4rYxPVEOvXzEqr_IPy4VB6kDV0hdaYCmXgUmkfTjR5DVFQxwqgvM2_1aQSr_jsP7K6wOPi_oDeo_dFWy4VnMHrFTVOPaDX9tRaqWT9wQZlQPj9EuyevlCSoSM4rRrLUppYJiL7SsONURdpgK3grcuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
〰️
#فوری
؛سنت‌کام:
امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده حملات خود را به اهداف سپاه پاسداران انقلاب اسلامی در ایران آغاز کردند. این حملات در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین نیروهای نظامی آمریکایی مستقر در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70933" target="_blank">📅 20:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70932">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70932" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70931">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RGFscfKPzyDQPmw5q2URN7fUg3ZbSNpWiKPxzWUJ3_G22CA9JZjR8y20JtZcFpsTZb6za3NCaR-78vgFFxpLiLR2NnqjZY0TQwZWL72bNqEydc4zlUMShxgCpau3aLZURmCPZtJu6iVgtzSKUZEo3I63RJXHsJ8FYAFiePUroKUMWs4ZkzL2stsh-ibH0VYfV-wOoKQ-FDGCfxGU3XdgwOSIy3D0Kw63RY-2A4QAq9zxEcH4R_mUAh9PnRa9Pftg-kJhIg7zIlB5MFNnMq8I-oTWwFOVrqNtqDAH8Jg91rstBLc_uS3CTjglXrz2PNsHpUk0uF1MiUxpjNdy8ViaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70931" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70930">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
گزارشات از صدای سه انفجار  در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70930" target="_blank">📅 19:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70929">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=cx0bK7H6xEZHwqgO--OpiVve5efSxq_BSA1MTMuKPiBBN4FH60M1tONPLDOH0gVGYRu_N8_evMdVQI7gi-Z9r30_Za2BpkHwjRxSsHilI6RzpEEEqC42csX1ulHtsD3MrrwrYQHnG6dR1FDBZRGL9Ger2FIRY0c3doXY4-f1lBvAPFyg_P82vcdDojP_MIaoSNpxrYO4PaBDwOXCBIgaWLny0T9i-DXsBldQL7r_O_iEymo-6HlV6LrrW1a63QFmxqzoO4wswHJgVd0ZrfzufA9tjTR5CvaniYitLgAc1QgOqT6L3jiQPRsdxQUebGSXN2mHR6WvMmtBqixnW_2nYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=cx0bK7H6xEZHwqgO--OpiVve5efSxq_BSA1MTMuKPiBBN4FH60M1tONPLDOH0gVGYRu_N8_evMdVQI7gi-Z9r30_Za2BpkHwjRxSsHilI6RzpEEEqC42csX1ulHtsD3MrrwrYQHnG6dR1FDBZRGL9Ger2FIRY0c3doXY4-f1lBvAPFyg_P82vcdDojP_MIaoSNpxrYO4PaBDwOXCBIgaWLny0T9i-DXsBldQL7r_O_iEymo-6HlV6LrrW1a63QFmxqzoO4wswHJgVd0ZrfzufA9tjTR5CvaniYitLgAc1QgOqT6L3jiQPRsdxQUebGSXN2mHR6WvMmtBqixnW_2nYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇳
دیروز تو دیدار پزشکیان و نخست وزیر هند، مسئولین به پزشکیان میگن پروتکل رو رعایت کن؛
🇮🇷
پزشکیان میگه :
بابا ول کن این پروتلکو
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70929" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70928">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=Dsv1Zawyj9l7CG6g0qsjnFPz_pVbWSPujzEsJkSAFTO0u0XYip_UAK24zfZ4gDvry6HRF86y-ce7fE-PDJeDWn2nE75F9rodxbwGJ5yxIK5G9UHRlosaVF_UuOMLUnMeETjYHQBSlMNLvRLfOWhfQNQNPg4mEO1hAuNCZ3j5k8dult_A8tgf8cDrVhJWGouNs4tzF-nvsqeQzWT5Rbp38Ieehr9D5RIo9xniDSz5yMvLA1Sgg6efUZdcRERBokHtTnxI3vEzD96yZG9yYhGnWqU15TmvIJsCoI_GkO7gIEhqPonVSdt-GAGpffhrA3FRpYfEgVREiT8SYhv4H6HtXFw0Tm1g1GJgwpQUb2jB47gZM1T6qYqxwVdum592VFpKhuJUUrHpfbJg-mNvMhQNowoAtmupXpim11It5_sQYT5lz0D6Sw1lIWOmeFexV-j3CPISgekTGzbfpjb0Md3g3qtZZWiipz84OZy1qulR6iBnDrUBb9M1slHSx3sqJv4vNMNQPiQzC2nrOnEZpOaVQCWKKyCCqdm2VfDOVs55uOqfgtIHj_MNPFzzfAF5rwclu0sXLGg3Mb0w_CsrgU6fiJHwtohWNNP36NbxXi4kMDg2h3Fka_769BjxjMjNM-bZyAnGs1Uuf9PwkFN7IW7eHUZ7mAIa4g0Fe-_13x_iyuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=Dsv1Zawyj9l7CG6g0qsjnFPz_pVbWSPujzEsJkSAFTO0u0XYip_UAK24zfZ4gDvry6HRF86y-ce7fE-PDJeDWn2nE75F9rodxbwGJ5yxIK5G9UHRlosaVF_UuOMLUnMeETjYHQBSlMNLvRLfOWhfQNQNPg4mEO1hAuNCZ3j5k8dult_A8tgf8cDrVhJWGouNs4tzF-nvsqeQzWT5Rbp38Ieehr9D5RIo9xniDSz5yMvLA1Sgg6efUZdcRERBokHtTnxI3vEzD96yZG9yYhGnWqU15TmvIJsCoI_GkO7gIEhqPonVSdt-GAGpffhrA3FRpYfEgVREiT8SYhv4H6HtXFw0Tm1g1GJgwpQUb2jB47gZM1T6qYqxwVdum592VFpKhuJUUrHpfbJg-mNvMhQNowoAtmupXpim11It5_sQYT5lz0D6Sw1lIWOmeFexV-j3CPISgekTGzbfpjb0Md3g3qtZZWiipz84OZy1qulR6iBnDrUBb9M1slHSx3sqJv4vNMNQPiQzC2nrOnEZpOaVQCWKKyCCqdm2VfDOVs55uOqfgtIHj_MNPFzzfAF5rwclu0sXLGg3Mb0w_CsrgU6fiJHwtohWNNP36NbxXi4kMDg2h3Fka_769BjxjMjNM-bZyAnGs1Uuf9PwkFN7IW7eHUZ7mAIa4g0Fe-_13x_iyuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
بسنت درباره ایران:
ما داریم سرِ مارِ ایران را زیر خاک می‌کنیم. این مار هنوز نمی‌داند که مرده است، اما وقتی خورشید غروب کند، دیگر تکان نخواهد خورد.
کارِ رژیم ایران تمام است.
و آن‌ها هم متوجه این موضوع خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70928" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70927">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgW4qoRrNPDV1TrqJ3uw4W7DKa07WW0Sx6QZQ7iRl1iza_1wn-qf_1zInOrTrUYLyucDLhWAgHIbKFUNn0FZGp0XNsYMLqOZTXxtSQa7nbl275Jstjz-EwERPFDf4EhLLItuVmkmFWvm-cPVMsc0kPy5oeVq0nWhHuKwNeU3NubI9GnfuIm6eaO5xEL-6fpDrQ7tXmENhD2HqfK30TnXuyAOeONtTbK_dPPnYZQSeCnJ0cGUXBT5Eu3zQaitX0ISv8NAG8fQelM_o1idsQmmZOjXVHstsehlbxHrAaoAJNG69fPMlM4bSUr9EuSVE5Mdpw4aIPDPLecb2gsEG-YGWkxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgW4qoRrNPDV1TrqJ3uw4W7DKa07WW0Sx6QZQ7iRl1iza_1wn-qf_1zInOrTrUYLyucDLhWAgHIbKFUNn0FZGp0XNsYMLqOZTXxtSQa7nbl275Jstjz-EwERPFDf4EhLLItuVmkmFWvm-cPVMsc0kPy5oeVq0nWhHuKwNeU3NubI9GnfuIm6eaO5xEL-6fpDrQ7tXmENhD2HqfK30TnXuyAOeONtTbK_dPPnYZQSeCnJ0cGUXBT5Eu3zQaitX0ISv8NAG8fQelM_o1idsQmmZOjXVHstsehlbxHrAaoAJNG69fPMlM4bSUr9EuSVE5Mdpw4aIPDPLecb2gsEG-YGWkxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت درباره ایران:
ترامپ می‌خواهد یک‌بار برای همیشه به این وضعیت پایان دهد.
مردم ایران ملتی بزرگ هستند و این فرصت را دارند که به نظام [بین‌الملل] بازگردند؛ آن‌ها تحت سرکوب قرار دارند.
نمی‌توان انتظار داشت که گروهی کوچک برای همیشه قدرت را در دست داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70927" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70926">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPC7pGDnzhQM0j4DAwkgps_DMJ2dHtyc89K9oLfbi8iw5QW1ZL2lnfmyc1qrHuaQOQIpGMrLDTMiMWsD-jWEmEZyzxcT3UVdbSy45b9QHRvuE00Oina-8wdQaPHoyiRL879jbS7WqWsn89S-I8aR5Pwk1Mt4lrHCkqZ3hwC4qwDZyltdyoLy0ybyQv5u5EiG4bYmRFYm_g5u3pWqsVXxPXPeOGI5IwmUvp9BTBQ6aNQIJ9mQbzVBRGaq8KVIV0gvrU4xCE0PQIjZn_rjM88QXRWn4LAVoFkSDzPiHLsK_tqQ4KRB07_eXSnw_LlxMjbwEfmOGqv6Qh1-z6JU5tsORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
از زمان تشدید محاصره بنادر ایران، نیروهای آمریکایی مسیر ۸۴ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70926" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70925">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70925" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70925" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70924">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clL-5K6MyvebuTLh-s0tC0_Tb0FGOvWYj0RH3pvvGdUcMt6mqwoRcFI2T7K3ZcZNol4INKxZM8cwxCNsWxHXgQDB6sIGB4Z3Wk1EIZb09oRu1nSc-g5zkZS7sig3eQq7hKU36YwRb5P0LZXuDQ3dQPqOL5nT4cTq0xO6wuHWkwq96qr75EOFpNtCbFIoXBO7k1WdZbjQGvLEkxJSzTWTRUDBRkZC8JfZpKd0-1SlCYt8GhMFZNUSAwAopA8egEPDHV5QPSTlxtLpc8WWMfn5g7zLF9MTAIeV9t3xgn4hg6m68plOYEM-SdcRJ07z-N8IjIDy2WqI_4KvfZ82IaeeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70924" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70923">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=ffBW0ECVE7AKX87Q_BI6KI3YETwAGImHIL0rBqWcja0UTXp1JAkq_VWPKnmc6s0hjProW5I8Xe5CWZMH1EelGdANwD8RMPoDrodTfBWISMX38OQ3E0FfjpNjRSYkHPuzfUbdeOblMKbFlfvu2Jn-whYb1IX8MAcu_863TmOZJEAx1ymg8137NuavJjVzDsi-r2cQg6dEUiEaIlUJVBi4SysOESVvP12-tf9ydFRBodeiPEIepUfja0-RdHB7KV0dGz_EKE-oLDH1GBAYoHYms4cv4U1iZFcLBPqpub1by3qZSm3QQc4boTROJ_WdS8jC0hyebLodmbWs_KSISELZrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=ffBW0ECVE7AKX87Q_BI6KI3YETwAGImHIL0rBqWcja0UTXp1JAkq_VWPKnmc6s0hjProW5I8Xe5CWZMH1EelGdANwD8RMPoDrodTfBWISMX38OQ3E0FfjpNjRSYkHPuzfUbdeOblMKbFlfvu2Jn-whYb1IX8MAcu_863TmOZJEAx1ymg8137NuavJjVzDsi-r2cQg6dEUiEaIlUJVBi4SysOESVvP12-tf9ydFRBodeiPEIepUfja0-RdHB7KV0dGz_EKE-oLDH1GBAYoHYms4cv4U1iZFcLBPqpub1by3qZSm3QQc4boTROJ_WdS8jC0hyebLodmbWs_KSISELZrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت وزیر خزانه‌داری آمریکا:
می‌بینیم که — باورکردنی نیست — این رژیم در کشوری که احتمالاً سومین ذخایر بزرگ انرژی جهان را دارد... بنزین وارد می‌کند. بله، بنزین وارد می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70923" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70922">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=cjHRR2Ghfm9SlAugTyUi-rsLUizO2DXqwZ9mRnsObeiVKQ4uy5pcJtpkIIGA8lE7V-KQ6gbJCpHGj0Fea8xmri6hlLubc7cjWXpHp7UFsoebBrhUT5gBIdAJFcxm-SmDtM2vV2A5Q5FbMmb5BkyfvT7nx0OmYFZxyegGISsyW5N_4GC3-GIgy7dA8xe6byMZkz5wQDnJN99YPOGTesuVVKm6A8S63Z7BW2WLCDcQnEaVgTTXkot7uvkh70n5pAdpcmalRJWd0cN1BH1VSqOOpR2TgCn9CKuKOtaeacsDHydqb5JpOyEF4Yp0DD3ts-kKM60hszoN1pgU158TeutVcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=cjHRR2Ghfm9SlAugTyUi-rsLUizO2DXqwZ9mRnsObeiVKQ4uy5pcJtpkIIGA8lE7V-KQ6gbJCpHGj0Fea8xmri6hlLubc7cjWXpHp7UFsoebBrhUT5gBIdAJFcxm-SmDtM2vV2A5Q5FbMmb5BkyfvT7nx0OmYFZxyegGISsyW5N_4GC3-GIgy7dA8xe6byMZkz5wQDnJN99YPOGTesuVVKm6A8S63Z7BW2WLCDcQnEaVgTTXkot7uvkh70n5pAdpcmalRJWd0cN1BH1VSqOOpR2TgCn9CKuKOtaeacsDHydqb5JpOyEF4Yp0DD3ts-kKM60hszoN1pgU158TeutVcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
متأسفانه شعبه‌ای از یک بانک مصری در دبی وجود داشت که بیش از ۱.۸ میلیارد دلار را به سوی رژیم سرازیر کرده بود.
ما از اختیارات قانونیِ «قانون میهن‌پرستی» (Patriot Act) — که پیش‌تر از آن استفاده نکرده بودیم — بهره بردیم و در حال تعطیل کردن فعالیت‌های آن شعبه هستیم.
ما آن‌ها را مستقیماً تحریم نکردیم، زیرا نمی‌خواستیم کار به بانک مادر در مصر کشیده شود؛ اما همه باید بدانند که ما هویت آن‌ها را می‌شناسیم و خودشان هم می‌دانند که چه کسانی هستند.
احتمالاً همین هفته تحریم‌هایی را علیه یک بانک اعلام خواهیم کرد و هفته بعد نیز تحریم دیگری را اعلام می‌کنیم.
ما با متحدانمان در اینجا در حال گفتگو هستیم؛ آن‌ها همگی پای کار آمده‌اند و شاهد حمایت‌های گسترده‌ای بوده‌ایم — چه از سوی اتحادیه اروپا، بانک مرکزی اروپا، بریتانیا، امارات متحده عربی و چه از جانب بحرین.
ما قصد داریم این رژیم را از نظر اقتصادی خفه کنیم.
و همان‌طور که رئیس‌جمهور ترامپ گفت، دلیل بی‌نتیجه ماندن آن تفاهم‌نامه (MoU) این بود که آن‌ها آمادگی دستیابی به توافق را نداشتند.
وظیفه من این است که اطمینان حاصل کنم آن‌ها خواهان توافق باشند؛ و قطعاً هم خواهان آن خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70922" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70921">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=vJ6yZGR96qGxaVA1u7N-y4ZhYk_vMWUbMotNeRcS_xFkeVKNocV8sJ2BUjP2iJ1-LVLbffeo26j_s1T5YI4jMKUC2DHa8_XNm3xWLUPZM-wejzTcPz91AkHt0mERN1-fLsjMGwslJDKSryUsSHtp5oJwqs6Z1-ek6UwSbei3EhFGyAlGtJ9lZk10ALHg7tri922ZwKzTtbz6f9R7ezrFTPbV52aWppXKg1pXMb9jS8p8OjNehp9C6qYLG2590iy2bTAr6lXdIqZMi8ZF0YXQCaaEm-krtqW-HfS1fyDEn2Dnc80Har79GBYXbAcPOZuXvtDX3ZSbOe1J_Jw5DBpniA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=vJ6yZGR96qGxaVA1u7N-y4ZhYk_vMWUbMotNeRcS_xFkeVKNocV8sJ2BUjP2iJ1-LVLbffeo26j_s1T5YI4jMKUC2DHa8_XNm3xWLUPZM-wejzTcPz91AkHt0mERN1-fLsjMGwslJDKSryUsSHtp5oJwqs6Z1-ek6UwSbei3EhFGyAlGtJ9lZk10ALHg7tri922ZwKzTtbz6f9R7ezrFTPbV52aWppXKg1pXMb9jS8p8OjNehp9C6qYLG2590iy2bTAr6lXdIqZMi8ZF0YXQCaaEm-krtqW-HfS1fyDEn2Dnc80Har79GBYXbAcPOZuXvtDX3ZSbOe1J_Jw5DBpniA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکا قصد دارد با نقض تفاهم‌نامه، از مسیر جنوبی تنگه هرمز عبور کند و ما اجازه چنین کاری را نخواهیم داد.
پیش از جنگ، روزانه دست‌کم ۱۲۰ کشتی از تنگه هرمز عبور می‌کردند.
حتی اگر اکنون یک یا دو کشتی موفق به عبور از تنگه شوند، این وضعیت به هیچ‌وجه با شرایط پیش از جنگ قابل مقایسه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70921" target="_blank">📅 17:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70920">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
ما در ۱۵ ماه گذشته، در حوزه نظامی به اندازه یک دهه پیشرفت داشته‌ایم.
در هر دوره از درگیری، عملکرد و نحوه نبرد ما نسبت به دوره‌های پیشین بهتر بوده است.
نیروهای مسلح در هر دو حوزه توانمندی‌های تهاجمی و تدافعی، به مؤثرترین شکل ممکن در حال بازسازی و تقویت هستند.
این اقدامات مرهون آن است که فناوری ما بومی است و جوانانمان این کار را انجام می‌دهند؛ از این رو، نیازی به روی آوردن به دشمن نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70920" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70919">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=tU7ykufC3GN2cA5gmatC9K_g3QfoRUkNXavwSmamgddf_tOjk5iWA2l2BJU02EiR_s3j4iTyHtDCoad_rR6U3VzNRf7DoQC3w3B_xAT9AV7qfp8DxVmnI0kDnts_I3f6q4A10J8AVvTq0GUHnILtNtmGEe_fEN2Bj1pKpdPEXsI8i7XZW3pnU40hOv7lQY2SVKo8t5-tH9XXWdHUsHyhT022-0f8tCfpBNjW0iHolMKTcqj6Lj-OViZE_RqG88roiqu_I70f3UvmBQs_o4mpIU4Z2kKLpmnZMrkIULxIRaflK_Iqijd6E_lHGPJnPE8fARCIoC2ffbR5bq2Iva9vKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=tU7ykufC3GN2cA5gmatC9K_g3QfoRUkNXavwSmamgddf_tOjk5iWA2l2BJU02EiR_s3j4iTyHtDCoad_rR6U3VzNRf7DoQC3w3B_xAT9AV7qfp8DxVmnI0kDnts_I3f6q4A10J8AVvTq0GUHnILtNtmGEe_fEN2Bj1pKpdPEXsI8i7XZW3pnU40hOv7lQY2SVKo8t5-tH9XXWdHUsHyhT022-0f8tCfpBNjW0iHolMKTcqj6Lj-OViZE_RqG88roiqu_I70f3UvmBQs_o4mpIU4Z2kKLpmnZMrkIULxIRaflK_Iqijd6E_lHGPJnPE8fARCIoC2ffbR5bq2Iva9vKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خانم بخاطر اینکه شوهرش دائم بهش اسپنک میزده، ماهیتابه می‌بنده دور باسنش تا این دفعه شوهرش ادب بشه!
اما همچین صحنه‌ای رقم میخوره و یه شاهکار خلق میشه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70919" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70918">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f47777b.mp4?token=bTXzGvnTqDK-TpVeuE7vxZtWYD4c1p0ditdqK8VxtHAZBzg2qEh6ODM4HTD_8eNnKk0KYscDIkeVNYpuFWDVc4QCEpQohOts624-UpnVNUCNX6NevLrTMZZrvCrKR48uUGho6QEFccQ2afsu242VBDD_eVYMqItIZnhsynhX0kcvGsjhwQ2ih6et49S2RXaNowNnIgw86cqy1u5HBpew1AyMUYwPXweVfZ7GeL26MGRrShlL1itnduRmcaG1R8CH4paNd_OQzjXBvYdOVUQyt1UwCPxPbMWLsJJQuLFbJ3Gpt7Isciw_fTo_4Cv33LtlqE2Yyqij1NnIrDgar7Rtmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f47777b.mp4?token=bTXzGvnTqDK-TpVeuE7vxZtWYD4c1p0ditdqK8VxtHAZBzg2qEh6ODM4HTD_8eNnKk0KYscDIkeVNYpuFWDVc4QCEpQohOts624-UpnVNUCNX6NevLrTMZZrvCrKR48uUGho6QEFccQ2afsu242VBDD_eVYMqItIZnhsynhX0kcvGsjhwQ2ih6et49S2RXaNowNnIgw86cqy1u5HBpew1AyMUYwPXweVfZ7GeL26MGRrShlL1itnduRmcaG1R8CH4paNd_OQzjXBvYdOVUQyt1UwCPxPbMWLsJJQuLFbJ3Gpt7Isciw_fTo_4Cv33LtlqE2Yyqij1NnIrDgar7Rtmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره اندام های تناسلی  حضرت آدم و حوا:
حضرت آدم وقتی اومد به زمین دید لای پاش یه گوشت اضافه هست و میخواست اونو بِبُره
چون حس میکرد بدرد نخوره و فقط تکون میخوره
که یهو حضرت حوا از آسمون ظاهر میشه به آدم میگه نکنه میخوای مارو بدبخت بیچاره کنی؟
حضرت حوا بهش میگه جریانو و اون منصرف میشه
آخرشم میگه حضرت آدم وقتی حوا رو دید اون گوشت دراز مانند لای پاش دید یهو تکون میخوره که فهمید نه مثل اینکه بدرد بخوره و منصرف شد از بریدنش
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70918" target="_blank">📅 16:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70917">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=CMD80h3vEidO7QlooBYC2DsgJVRwQgddIskPBQ94Nr2pHYprMkqQFcyz7w2PchWVRWTmDJJf_85gZJilz_7zn4uvBoC5os4WrqvKyvgUhHnK3Iid-Qs59NbTRkkXP7ALVuWQOGoVZOOjgvgfVGAEgYJnsFZtb1ITLtAYvpynbR5BWXBRkg04HjKrBGYjI9R2ZmCp3jCTpoNL1TEXdUKPMbxqokE7n12q_buBYCouG_ky-pnIYByf-_Onu8pA1PVPtGrP9D-ZWs3z4HGv4JsHpavcGIqUzn_ff9YQfgCEm6vPCEF-DaQubC6Rlx0KvsQQv-7WF7r1-R0KSTr0whnDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=CMD80h3vEidO7QlooBYC2DsgJVRwQgddIskPBQ94Nr2pHYprMkqQFcyz7w2PchWVRWTmDJJf_85gZJilz_7zn4uvBoC5os4WrqvKyvgUhHnK3Iid-Qs59NbTRkkXP7ALVuWQOGoVZOOjgvgfVGAEgYJnsFZtb1ITLtAYvpynbR5BWXBRkg04HjKrBGYjI9R2ZmCp3jCTpoNL1TEXdUKPMbxqokE7n12q_buBYCouG_ky-pnIYByf-_Onu8pA1PVPtGrP9D-ZWs3z4HGv4JsHpavcGIqUzn_ff9YQfgCEm6vPCEF-DaQubC6Rlx0KvsQQv-7WF7r1-R0KSTr0whnDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر روز عجیب تر از دیروز
😳
جدیدا یه عده میرن به این شکلی که می‌بینید، یه مداد دستشون میگیرن، رو زمین میخوابن، میچرخن و نقاشی میکشن!
اسمشم گذاشتن " نقاشی با بدن..."
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70917" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70916">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=FeORnHoYYvVzYsIcA5rxvmBhVov108G0585Ymrzh-8advytO4cUOzRAbnD_Ho1o7It6-FR6-MeOQQMiJ5KfqtZf6zmruIYMd6cCXlW9EnVZp1mxg59sv56aToAER3z934uQv-WD0vdW6vR-rOwb9YlFBiebsMb0naVXR2UGsw4zTwSauwj0DqElZ1SWegznZ47oLmj_JwW3pTuDntH6R4AM1cDy3Pt3Xu2w4SI25Z6cqTl2dZ8nDRpcX50PXjgpoWp1hHJPs5t-YNhqk7QguNVKFTQeK8x-NTIbya_x_DLhXKLw2DPXSV9XSKja_Vgh6nwu9_JLlXq2GsiSk6R2tVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=FeORnHoYYvVzYsIcA5rxvmBhVov108G0585Ymrzh-8advytO4cUOzRAbnD_Ho1o7It6-FR6-MeOQQMiJ5KfqtZf6zmruIYMd6cCXlW9EnVZp1mxg59sv56aToAER3z934uQv-WD0vdW6vR-rOwb9YlFBiebsMb0naVXR2UGsw4zTwSauwj0DqElZ1SWegznZ47oLmj_JwW3pTuDntH6R4AM1cDy3Pt3Xu2w4SI25Z6cqTl2dZ8nDRpcX50PXjgpoWp1hHJPs5t-YNhqk7QguNVKFTQeK8x-NTIbya_x_DLhXKLw2DPXSV9XSKja_Vgh6nwu9_JLlXq2GsiSk6R2tVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⏺
فرماندار ماکو:
آیا دولت مقصر گرونی هست؟؟؟ خیر ما مردم مقصریم باید به خودمون رحم بکنیم
قیمت ها خیابون به خیابون فرق میکنه تقصیر ملت هست که تو ذهن هاشون فکر بدی دارن
یه عده گوشی و قلم گرفتن بر علیه دولت مینویسن نه آقا ملت به خودش رحم نمیکنه و خودمون باعث گرونی هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70916" target="_blank">📅 15:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70913">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3J2lMe8L3fuTBhLPsboaZlMQ4zcLgLxd5WSeROpQjnHKoAQncUcjca-iFiGFqVQfEWQ51LOOLfnPsJUpfsvYxt2JWLrg0688cMkyBsBhZSBROJg8OkFpdPmUJsItv8yX7ZV8CTTqWSVBBhBJ0NU4Lpend1v7YOvI3fPAqjkoHRgsFjcZrZL-KqldFrXAHiFW70VgRQIjPSA7XJTo7-upKTUtZPR9vu8RcqFsljMVzVgUVs4ySaWKsw3XIdch8TddBTf34Ks1nXlqNn8qUwHhcAM_QceCYrmp5GLbCiHoYPb5ve8o7mRPnEFylc-6pFuHOEg_IclMe8RNwCRu6NaZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0LpMVVAw2Uw7-hsr7S4pEiLh9uljxqSJa83voB-1U0-692L9hAyl96d6HndJt3aIvCxWlbcL94JJDGGr7TdGnIWiZIx77hnjiSYaHjD8DSsV1uYE2fGSWO4uuCWmKGSdJyEikwy_SYcCAwYiONJ5YhG0n5mlhfqcj5H2oy250Qyj4gs9rVyd-EGWBl8raydYMmgZD-ZT78i6QBtLPEMWsKCxFoDqhRflLBHJ8FmSQrdivLG98Knda3UNvVUKizXA7KMfdVdNgfCxHW8LAZ768xvhZMm2RZnCZbepmy-Opf3uebSj1SSZNucbKkloTGeKvyVbSLLxDEMJ6A5hOMkDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f05211278.mp4?token=PTslPuqVxZXSorFmw-ubJIMireAB4SsAw5kHTSTjMcsvDvGZ5e8DYvXFiUojX4HO1hfHHiR9EajjnQE1nrn49pXo4kaQlEEmQeWMrx9rEs5Fi9CGnLaJ6PvQMAQpdiInM3yZl4Yzh5PS2deSnb_k0Q6fc2cCE9rtBnUywc-9Z7nws9qhne4jRG-rjrJ4XVif3kyGSppkSNQ0UCDktLqussOZpmTZQhAVW0P4NU_AQXmU1PxdPgQ12_DAlxBHMeyDWbxXBlMThYZ5YSBTmLIHlviwU4U7n7FOngYY8zcFkblHv4lIg1yZCTsU--1mGkG4sFlHXQ2570eJnPLXQFzEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f05211278.mp4?token=PTslPuqVxZXSorFmw-ubJIMireAB4SsAw5kHTSTjMcsvDvGZ5e8DYvXFiUojX4HO1hfHHiR9EajjnQE1nrn49pXo4kaQlEEmQeWMrx9rEs5Fi9CGnLaJ6PvQMAQpdiInM3yZl4Yzh5PS2deSnb_k0Q6fc2cCE9rtBnUywc-9Z7nws9qhne4jRG-rjrJ4XVif3kyGSppkSNQ0UCDktLqussOZpmTZQhAVW0P4NU_AQXmU1PxdPgQ12_DAlxBHMeyDWbxXBlMThYZ5YSBTmLIHlviwU4U7n7FOngYY8zcFkblHv4lIg1yZCTsU--1mGkG4sFlHXQ2570eJnPLXQFzEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ز غوغای جهان فارغ!
شمال تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70913" target="_blank">📅 15:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70912">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983da46010.mp4?token=KA6rULAijF17y3fTWkQYJBEAmfSyAAzrCtXsdCuLB47r8Z3hsq-mxH2cfUoYVp1Lx-RWPFrXTYVcis6z-cZbcfQa3PKUv1G_f0cC3H1dwF5py9_Oo1T4thTx4Cuv1GKx0yzMzb3dw7teTDZ_2J4NOfoP5z7PZE2-GpmvS_4SQTWx3E2iGyd8b_fuU-4Hdmdy6zzYRVEEDj9FZAfTbCBHVFFlWTGu7MANvWzdUOL6U96DT2Dfx9vlQ2f4_Y4ZlLS7d2BccPBFngeV1pJ0Y1gDC1hIyFsDVvIn1Rjhzh38e81TCMDIOjZzy-bvBN2iWm8sVW7uevp-WmLJ5alRRxsXDJ-HwnP4jDxgenoXurL21trjJldFhMoIsUk38c29LbnlT60IGMLxOOVM1KEMzMTnROdBF4Sm9nP1Lap-dyQg-LwoWoP5OLYzJkBnFqo1uvV8qHqBUhxzBBwqChb5M3QQKsug-y0dMCoJ6BsrgBW6wQYHjJRN3SIKYs5mAxduiP5tIYGgwfd-iZ4roPoLfdgZnQaKuOpum0y33-zOJ1uUuXijBg4KABhBBb66Sg_SND_7ejJDE2pKwY-xiAHU5bOtVSY-vbnZhXQM50YQqQbDLbS2oqd3iTrAeBajkZqZDbpOCcA3jwKc4beTD9hRYZuGGPAvy5xNi7zkpPznB5ybAOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983da46010.mp4?token=KA6rULAijF17y3fTWkQYJBEAmfSyAAzrCtXsdCuLB47r8Z3hsq-mxH2cfUoYVp1Lx-RWPFrXTYVcis6z-cZbcfQa3PKUv1G_f0cC3H1dwF5py9_Oo1T4thTx4Cuv1GKx0yzMzb3dw7teTDZ_2J4NOfoP5z7PZE2-GpmvS_4SQTWx3E2iGyd8b_fuU-4Hdmdy6zzYRVEEDj9FZAfTbCBHVFFlWTGu7MANvWzdUOL6U96DT2Dfx9vlQ2f4_Y4ZlLS7d2BccPBFngeV1pJ0Y1gDC1hIyFsDVvIn1Rjhzh38e81TCMDIOjZzy-bvBN2iWm8sVW7uevp-WmLJ5alRRxsXDJ-HwnP4jDxgenoXurL21trjJldFhMoIsUk38c29LbnlT60IGMLxOOVM1KEMzMTnROdBF4Sm9nP1Lap-dyQg-LwoWoP5OLYzJkBnFqo1uvV8qHqBUhxzBBwqChb5M3QQKsug-y0dMCoJ6BsrgBW6wQYHjJRN3SIKYs5mAxduiP5tIYGgwfd-iZ4roPoLfdgZnQaKuOpum0y33-zOJ1uUuXijBg4KABhBBb66Sg_SND_7ejJDE2pKwY-xiAHU5bOtVSY-vbnZhXQM50YQqQbDLbS2oqd3iTrAeBajkZqZDbpOCcA3jwKc4beTD9hRYZuGGPAvy5xNi7zkpPznB5ybAOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
اژه‌ای، رئیس قوه قضاییه:جمهوری اسلامی از هر وقت دیگه‌ای، بیشتر آماده‌ست!
کسایی که تو ایران هستن، همگی درمورد امنیت ایران یک‌صدا هستن.
اگه باز محاسبه غلطی بخوان بکنن که آشوبی یا اغتشاشی تو‌ ایران راه بندازن، مطمئن باشن که پاسخ نیروهای انتظامی، امنیتی، اطلاعاتی و قوه‌قضائیه از قبل هم قاطع‌تر خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70912" target="_blank">📅 14:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70911">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htbBYr-Vp1fkzkj0A5mjV-e5rA7HWQhfmMjx1CvPfWMNJ12CJzcqWzdGJjlpDnO24rumWQOHZgxtaD1AmqsXl0Lc_z3qZUHFerlzYFAd_EG8r_K9PAnylxpQBBJAvPoOg_xHjdP0lii82kgioc6BwKmQG1E0madYDCS-qQUq0CCgQGPexY6CoXcPawKBY9EYUJwQWJkYOLVvpfTB-8Qr7ZpOoEWJJYIbQj8FyuO-r2KVYJhKyueibjbWBtefGeYMazSdbpIzi_VNLfcisb6wEacZLwR-d9A9T4iftERsXSs7rnk-0Q4tigteT-0NXc2O06Ux3tixWpb_6XQSf-4sPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
ترامپ یک مطلب از Breitbart News را در تروث سوشال بازنشر کرد.
⏺
تیتر مطلب؛
ترامپ پس از نخستین تبادل آتش با ایران طی هفته‌های اخیر، وعده داد که «سخت» پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70911" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70910">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=uUkW30G9_8210b8zdBa310p05AxfPktpGuiTIuvycPSxwIJGUgzqjZw3Hyrx7340uRMs86_biRcdfOZvwShMdwHJ-dvFpUlATS8nScJI7mwtE_rXzsarJR9LRA4xcidbOUY6GKuWUYg0rt27W04Nc6emAwvIb_V_P0OJ2xZw7tPAPsulRMqEsDJtWr5sUg8hen6q89phYC88S5j4uSZKn9rYssShUIBZ5RgYJYaFENuikp6JEYc6pjDnHcwh8dUM9E3r5u8MKkD2RipD8l9Z7UVpLBUJELzn_fD1pYyGPidh-elT1TbWXC7p1jGjDKWGIqAc_7R2OdjuxCxmlySapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=uUkW30G9_8210b8zdBa310p05AxfPktpGuiTIuvycPSxwIJGUgzqjZw3Hyrx7340uRMs86_biRcdfOZvwShMdwHJ-dvFpUlATS8nScJI7mwtE_rXzsarJR9LRA4xcidbOUY6GKuWUYg0rt27W04Nc6emAwvIb_V_P0OJ2xZw7tPAPsulRMqEsDJtWr5sUg8hen6q89phYC88S5j4uSZKn9rYssShUIBZ5RgYJYaFENuikp6JEYc6pjDnHcwh8dUM9E3r5u8MKkD2RipD8l9Z7UVpLBUJELzn_fD1pYyGPidh-elT1TbWXC7p1jGjDKWGIqAc_7R2OdjuxCxmlySapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کسبه پاساژ پایتخت بورس کامپیوتر تهران می‌گویند مشتری نیست و سابقه نداشته که پاساژ تا این حد خلوت باشد. یکی از آنها صراحتا اشاره کرد، گرخیدیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70910" target="_blank">📅 13:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70909">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=mml5SxF1F4WJ1F0VXNPAla17gP72buOv9o4dFCtYpVstYsp1RxgWKXpQ_OrOxHOQLmrwBxyKJb8stBFWTgPbaYPRDBkw3P4Ml6NpbxnPQITrARz0UG1UJ3lwb7ehLUWL5EnnhQv9jfH1il3BFdoJQpNwwkqBvr9wzsExw3ZT-N8_CitEriyWMvdvNEO0Rcpt5zXRXurZE77DMCmbqEQ_MNKRVJu6g-V-Op7zH5cHEx83p1bnV-bwxJUHmqIKVi_76lfaILo_EJB1sF95Pfp1LkaQi_qcqUdrFbAJZmBRuj_ev5i0EzXcDOD1pWb_ZOtMATwLrWaY01MUk-cT0gWc2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=mml5SxF1F4WJ1F0VXNPAla17gP72buOv9o4dFCtYpVstYsp1RxgWKXpQ_OrOxHOQLmrwBxyKJb8stBFWTgPbaYPRDBkw3P4Ml6NpbxnPQITrARz0UG1UJ3lwb7ehLUWL5EnnhQv9jfH1il3BFdoJQpNwwkqBvr9wzsExw3ZT-N8_CitEriyWMvdvNEO0Rcpt5zXRXurZE77DMCmbqEQ_MNKRVJu6g-V-Op7zH5cHEx83p1bnV-bwxJUHmqIKVi_76lfaILo_EJB1sF95Pfp1LkaQi_qcqUdrFbAJZmBRuj_ev5i0EzXcDOD1pWb_ZOtMATwLrWaY01MUk-cT0gWc2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دندونپزشک‌ها میرن میپرسن کدوم کار زیبایی تو دندونپزشکی رو نمیذاری بچه خودت انجام بده؟
به طرز عجیبی تقریبا همشون میگن کامپوزیت و لمینیت!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70909" target="_blank">📅 12:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70908">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=pPxtIO0AwXkvOivEQjDv6aQqd2oEno6qxO4lZ8RLcUCwpM9bLnSlmbSBOCRtMs-ivmS6v5qzOsdcZ2aga4W1wDhxE4ZhpV-dxbX3mOF74H5dETPfH1eY6mkgiha4uk4Ldk5xJqu6_BI1w_B811cV_seYNDPVIKt-MEArBUQg15k_T7Es56cpzGzqU1wdAi6a1ovhMCLaJrNhLR-RMzR6azTIw6QUAflKYOvbZX6TEITYedH3PD3nvXcWPVkfpzjVLnokEQxbVOcxVQJY1ZLkJNnAmuOPrVegDzUHswFeEMxQiX6rP0HBoPVEyq7aK6vrF656jP_QV-mgGRocdHE9cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=pPxtIO0AwXkvOivEQjDv6aQqd2oEno6qxO4lZ8RLcUCwpM9bLnSlmbSBOCRtMs-ivmS6v5qzOsdcZ2aga4W1wDhxE4ZhpV-dxbX3mOF74H5dETPfH1eY6mkgiha4uk4Ldk5xJqu6_BI1w_B811cV_seYNDPVIKt-MEArBUQg15k_T7Es56cpzGzqU1wdAi6a1ovhMCLaJrNhLR-RMzR6azTIw6QUAflKYOvbZX6TEITYedH3PD3nvXcWPVkfpzjVLnokEQxbVOcxVQJY1ZLkJNnAmuOPrVegDzUHswFeEMxQiX6rP0HBoPVEyq7aK6vrF656jP_QV-mgGRocdHE9cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
غیرحضوری شدن مدارس امسال شایعه است؛ برنامه دولت به حضوری بودن مدارس است مگر اینکه اتفاقی بیافتد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70908" target="_blank">📅 12:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70907">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70907" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70906">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6YhgWsr8opHp0ZNsagi68b2_5Rr_dWKsmNm3We0VejOz-0RwV6xitefCeVQvlcMlMBkH0Oy2r_uQMl6MiNOlpiPQVdAHVn3Zke2Tval0x0gBGF66b2uvsNaPVME6FS6BGq6lJWgARe4wYXP3d8frgUi_ywbThQrSBkKcvRaUcL9DDQ74XakCytzOFqbaWOe_ske6ddP284DthXKMmSaB-CpZO_qjwP7iktS9cxw5BP5PLSwXyorwCckwANBCYhwsmhjWMXfWyDlM5sLPWLg8lRaqqHFGAghAVfSr7Jn3VoZhbXUId-FAD-csMiqBwhpL4EPCWvRyyxOk_M01rT70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70906" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70905">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=AUSywvwBl2RaJhLZOwUaSml7Bz577QpiPWErT2YkSKPB8l6LX8vpVB8i6qf7a_IDvA1PNpFHCxb6r8R3U11eOxhVK01dwmwKUYctA4Ph1i_bFJ5yvxErZ9asKC3OxYx6efm7OIrAeiAtzKFhNRTeEAF5U9emOthSCP4a4yzWIrED9myvOawDEiDVb9_rtS8s-YCuqzWHUoIyrPZDvwb4TNm6EiBkO_bjKUcg9sVO5ZeGdmFS06dEpTsA9QO15Zfs1dmcYO3MsqlazCWjJkJTwMR22fjjdXNTrrayEeFbl0LjZoq7Nq7Uc1n91tA469VXsBO0RNlYvqCVkRLJ7bje7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=AUSywvwBl2RaJhLZOwUaSml7Bz577QpiPWErT2YkSKPB8l6LX8vpVB8i6qf7a_IDvA1PNpFHCxb6r8R3U11eOxhVK01dwmwKUYctA4Ph1i_bFJ5yvxErZ9asKC3OxYx6efm7OIrAeiAtzKFhNRTeEAF5U9emOthSCP4a4yzWIrED9myvOawDEiDVb9_rtS8s-YCuqzWHUoIyrPZDvwb4TNm6EiBkO_bjKUcg9sVO5ZeGdmFS06dEpTsA9QO15Zfs1dmcYO3MsqlazCWjJkJTwMR22fjjdXNTrrayEeFbl0LjZoq7Nq7Uc1n91tA469VXsBO0RNlYvqCVkRLJ7bje7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ترفند یه آقا برای فروش بیشتر:
برا اینکه فروشتون بیشتر بشه پای مشتری رو بخورید
😟
اگه پاشو نداد که بخوری بپرس ازش ببین کجا رو دوس داره بخور براش.
بازار خرابه مجبورش کنید اعتماد کنه بهتون.
بعد خوردن جنستو براش معرفی کن و اگه نخرید بازم براش بخورید.
بعد مشتری میگه هروقت بیام همیشه اینجوری سرویس میدی و اینجوریه که فروشتون میره بالا
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70905" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70904">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=Nai44fpDjBuEWarVODR7geU0edxMeEhGGU_FbUpjLX3RdNwSs6RQ8wLau89cZCwb05v_C2fTBB6Jvf3AuDzR3Km9ZjN1Jhgt-02sBlqBrbS00z-ky0JICtutlC3ZYpsuyGtNyI1rwCmthMQoeV75XOVhuRaw-JRBmxe9ybGcy9eCr7dITR4O6FmBeNypZHl9eICb_oMIRaP1yqY7qvFyiSxyd1MlDvo47VSskxx29Mnj8ffPvuS-a7sypdXuiMJjcfNv4YAOj9f9XvULfL7IKBVNCoYHTOGfJHg_Z3WgKVQTjNeXGhjZky8WiAILLSj1xUkqfnWl--7SrS5hdaa9Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=Nai44fpDjBuEWarVODR7geU0edxMeEhGGU_FbUpjLX3RdNwSs6RQ8wLau89cZCwb05v_C2fTBB6Jvf3AuDzR3Km9ZjN1Jhgt-02sBlqBrbS00z-ky0JICtutlC3ZYpsuyGtNyI1rwCmthMQoeV75XOVhuRaw-JRBmxe9ybGcy9eCr7dITR4O6FmBeNypZHl9eICb_oMIRaP1yqY7qvFyiSxyd1MlDvo47VSskxx29Mnj8ffPvuS-a7sypdXuiMJjcfNv4YAOj9f9XvULfL7IKBVNCoYHTOGfJHg_Z3WgKVQTjNeXGhjZky8WiAILLSj1xUkqfnWl--7SrS5hdaa9Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبرانِ ایران مهمه اینه که سرشون به گردنشون چسبیده بمونه [ زنده بمونن ].
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70904" target="_blank">📅 11:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70903">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=KNUgLWubQxCjeURHPGEY4-hT4r7MU5eo0e913UJo61iJ0bdePPteorVbOlU_7sdlnZgOtSHfAsyAFOz_9MV_yBviJ_cpnfZCaQnsSG1NURl6mF41am6XnxfeR8FNIfXTpvt6Nrg87j9JQToGtKdsps0VoIiQ9lk0t9Xebwx3eTC5egixqu6lUifHJgUcIbVyp76DmmDYVt52Rn2ZSUothrivfJQWUZ3ABArrJmsSXZicbOkP3PZCtfUEV-JXVBDIrhOxFeXqqMy--niKlcZEHe2rPPOBp5WrLOXoGExi3-bumS6xDzyqHDpPK5ogzdulhJk7YHzEtlBwMllylO64iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=KNUgLWubQxCjeURHPGEY4-hT4r7MU5eo0e913UJo61iJ0bdePPteorVbOlU_7sdlnZgOtSHfAsyAFOz_9MV_yBviJ_cpnfZCaQnsSG1NURl6mF41am6XnxfeR8FNIfXTpvt6Nrg87j9JQToGtKdsps0VoIiQ9lk0t9Xebwx3eTC5egixqu6lUifHJgUcIbVyp76DmmDYVt52Rn2ZSUothrivfJQWUZ3ABArrJmsSXZicbOkP3PZCtfUEV-JXVBDIrhOxFeXqqMy--niKlcZEHe2rPPOBp5WrLOXoGExi3-bumS6xDzyqHDpPK5ogzdulhJk7YHzEtlBwMllylO64iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حمید رسایی:
هم‌راستایی من با اسرائیل در مسائل مهم کشور(جنگ و مذاکره) مثل داستان دویدن یوسف و زلیخا به سمت در است.
زلیخا برای گناه می‌دوید، یوسف برای دوری از گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70903" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70902">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=PtkVtEghOBFU_JeaA3m9-Q9AxUxctXVwDxx0hW7ry8kmYU-05NdpAROPhd1xuIChzPjqKQoPzC5_UrLPcc6S_X7vdf-tjDnW-z8K5QUD8b6iH_QHayfVqOTqlzO9Z9HA9NQTpKFfVqrKHhbRV-57G1yH-MgqgMJNSaK44ILr2SbmaGOcb4iVbxLsiKaGMIb6tV-g8hPpJdysCoN-pxrHHee0a0KHNbdeI8_ZhCBdnd1Qn2qqch2cjev9TCkXMLzk9gY9u1zI6WSrQumNGG1SS4FIeVcYxwJMxnWBgI4Udd7Vz5MIu_kf80puzLg6r6ci-hPcERIEjSN0XK5m-o9kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=PtkVtEghOBFU_JeaA3m9-Q9AxUxctXVwDxx0hW7ry8kmYU-05NdpAROPhd1xuIChzPjqKQoPzC5_UrLPcc6S_X7vdf-tjDnW-z8K5QUD8b6iH_QHayfVqOTqlzO9Z9HA9NQTpKFfVqrKHhbRV-57G1yH-MgqgMJNSaK44ILr2SbmaGOcb4iVbxLsiKaGMIb6tV-g8hPpJdysCoN-pxrHHee0a0KHNbdeI8_ZhCBdnd1Qn2qqch2cjev9TCkXMLzk9gY9u1zI6WSrQumNGG1SS4FIeVcYxwJMxnWBgI4Udd7Vz5MIu_kf80puzLg6r6ci-hPcERIEjSN0XK5m-o9kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجددا در سراسر کشور، حجاب‌بان و گشت ارشاد راه اندازی شده، توی بازار تهران حجاب‌بان گذاشتن و هر کس بی‌حجاب باشه، بهش گیر میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70902" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70901">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=irDPRsXb8V4lZtCahV8pmB0PcEO4jwQBB2V9oTTkdHw12NhS0Gh7vEaWga0HMTtp1zKcZ6NdFLOEVZ0UEKIgd0LQePZD7fJPWUZx1FAFRE2uTUxl-SJ78nbWmqAOq6eA5NjG7au8Gj5rF8GV7xxF8D8lPhQ1gpWrpSYuOf9R93lnTNdYXnSlYW6bidbY11s6cu3H606Hfkoni173XIllJb2F_xJdKTzVETgYPyjrgGFPBuS8wtZs0FyKjcD6Ts4hLt2oqzdZcWabbbySfnnFM5agGggvm-A_Op2f_CZ43UVTrYhkn79uvz4t2Cf4f8nxOxZegXNETl5V6lMqDl7PiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=irDPRsXb8V4lZtCahV8pmB0PcEO4jwQBB2V9oTTkdHw12NhS0Gh7vEaWga0HMTtp1zKcZ6NdFLOEVZ0UEKIgd0LQePZD7fJPWUZx1FAFRE2uTUxl-SJ78nbWmqAOq6eA5NjG7au8Gj5rF8GV7xxF8D8lPhQ1gpWrpSYuOf9R93lnTNdYXnSlYW6bidbY11s6cu3H606Hfkoni173XIllJb2F_xJdKTzVETgYPyjrgGFPBuS8wtZs0FyKjcD6Ts4hLt2oqzdZcWabbbySfnnFM5agGggvm-A_Op2f_CZ43UVTrYhkn79uvz4t2Cf4f8nxOxZegXNETl5V6lMqDl7PiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر ماشینش رو داده بود دست دوس دخترش و داشت بهش آموزش میداد که این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70901" target="_blank">📅 10:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70900">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=t-6WMwrKZ4Ql9U4XQsgc70jJqwoTB1RYMSoOm1GNMcmKHPur8GCZXJf3FmN48-In9t4uTiXSjqIjCIeEFhQpl_ut40SLs2a4T4PkmJstENnYtmWr5No3bNJYUAQLe7bayV31hmWa0wRNfIu2xTPdElZ4Du9u6qGqrZyym2jFtR3a2VbkAF_lbGpptKFz0yOhjIPyft8D5YoisLR4YPmdmTP1YqMK2hGJV_9RdVDsHpka3JPZsK9_dSz_JQGWG_U02494UZAPur_OzBFsWga0lZwPVLtZ2nMLRm2tt0Kef2aRcC05Gv8p2fqi-e9Cq3z0Nw5W14jneL0PsiqChSybtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=t-6WMwrKZ4Ql9U4XQsgc70jJqwoTB1RYMSoOm1GNMcmKHPur8GCZXJf3FmN48-In9t4uTiXSjqIjCIeEFhQpl_ut40SLs2a4T4PkmJstENnYtmWr5No3bNJYUAQLe7bayV31hmWa0wRNfIu2xTPdElZ4Du9u6qGqrZyym2jFtR3a2VbkAF_lbGpptKFz0yOhjIPyft8D5YoisLR4YPmdmTP1YqMK2hGJV_9RdVDsHpka3JPZsK9_dSz_JQGWG_U02494UZAPur_OzBFsWga0lZwPVLtZ2nMLRm2tt0Kef2aRcC05Gv8p2fqi-e9Cq3z0Nw5W14jneL0PsiqChSybtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇳
خب، این آقا سانت رامپال، رهبر یه گروه تو هنده که پیروهاش اونو خدا می‌دونن
.
این آقا برای خودش یه اتاق شیشه‌ای مجهز به کولر درست کرده تا وقتی اعضای فرقه میان پیشش و پاش رو می‌بوسن، آقا گرمش نشه و عرق نکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70900" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70899">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=LEaXylCKSwlJeHMZyqTzGJx33Mv_IoykWkDIZXFp6IlqzGX7kz2Sf8RrLBFTIKLZLLRTU9yLG8FhNwTK6O1cO4ywmF4HFNRFWC1VkNPnG8jerJsFvTpeyUTvCXZygh7AveNER1UaNeqQr3sv947Z0a_1layuY3jy7ILN1XDlTSIRdP8z5k0BssigAHNDEWxPacZ9O1JbITayq4v4WSCQcOmBQ5F-qCxY6oeHbu-JQsiq_ywYqbBLDcZUBrnFp1h6bDFBU74E2_Tx9F1oaStAytom1EyRSIqNLdIR5nRDxrxKuBCfVQ1eNdLcAO9hW6cEvvIAh2_5BCqdF7lM2ikpLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=LEaXylCKSwlJeHMZyqTzGJx33Mv_IoykWkDIZXFp6IlqzGX7kz2Sf8RrLBFTIKLZLLRTU9yLG8FhNwTK6O1cO4ywmF4HFNRFWC1VkNPnG8jerJsFvTpeyUTvCXZygh7AveNER1UaNeqQr3sv947Z0a_1layuY3jy7ILN1XDlTSIRdP8z5k0BssigAHNDEWxPacZ9O1JbITayq4v4WSCQcOmBQ5F-qCxY6oeHbu-JQsiq_ywYqbBLDcZUBrnFp1h6bDFBU74E2_Tx9F1oaStAytom1EyRSIqNLdIR5nRDxrxKuBCfVQ1eNdLcAO9hW6cEvvIAh2_5BCqdF7lM2ikpLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی تبدیل به حکومتی شده که نه فقط مشکلات مردم رو که وظیفه یه حکومته حل نمی‌کنه، بلکه خودش تبدیل به یک کارخونه تولید مشکل برای مردم شده.
تقریباً اون ده پونزده وظیفه اصلی که حکومت‌ها انجام میدن در ایران انجام نمی‌شه.
و بر خلاف اونا حکومت جمهوری اسلامی تبدیل شده به یه جایی که روزانه برای مردم تولید مشکل می‌کنه. شده کارخونه مشکل‌سازی. شده حکومتی که مشکل‌ساز است نه مشکل‌گشا.
مهم‌ترین دلیلی هم که مردم ایران از این حکومت متنفرند و می‌خوان سریع‌تر سرنگونش کنن همینه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70899" target="_blank">📅 09:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70898">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKVCNAJs2DeahXLW4Dy8mh6HNgahqIXQd_8pOj1X_6LGYqAMPxuHf5RDicTVbiex-Q7fjsE7R1JC3Ad1lV-V2z5XvXnmI4xyf6iaGLEJv4AcirUxaRBLcA9K2uQAMQEqPRDXrQWnvRctcLEVWeRK6ohGR91L1m6wVCThcs0f3pR_3PNXbEpYpPdRMpkiyHb8IrhDJomgZCh1EB0GSsFZ6KnAjNDAKQVhV8LTvBXS87P-dCHoFsMT69Y8Y70q77m9BnDeU9ucIcCqBd_RPO8XYrU9i_8Uc3oocfil92v3oXVyNO9xLWNfLtYdMHZM_ArSQsQqNP3JOq_cjiTz7asr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.  @News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70898" target="_blank">📅 08:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70896" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghLIT_uXeLk1rwXA73-Kc4lLPEBfdr1hxw_v9AXj4IaRQYHw3Dkp2YqBu4KllauVW0KWGUuiolJvJAbqtLTgI3KgfSe3Y9DwGW2x8g9Mf-6I62OhYQkaI8Z_TrozBTcfHzexm9YOA1mnwAe915wc88zU62Gwh38sXLzv0DLPu4NoXayFLmEQhFb7Tjzg-I9I-XgWUrr7AqixtRFK0I4gcw-0_tqwY3VFLqFt8Ng5zq_bxCwVuuWDqUH1mKLCL_5IddPmpMNTpDaZUmXGqMaWJcEopYjjf38XZnVBHqoxuRlQ1VcoOng0I8MetIo-e2yCNLRF3lpiXBfA3zNNujo5HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/70895" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70894" target="_blank">📅 00:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70893">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):  گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است. به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70893" target="_blank">📅 00:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70892">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXz1-OBgHsKPirgm2b5GpastSIdYPNfW0l3cMsCQ5ZYsiVrhysxV_NHjIS530lwf6SHKcSMByE2B-vihhRWkixEV4RgztNKEtNtrw3zB358j7-zmWGHB-fVNu9wrtQ03W6x8vzV7erF21lJM8I_5YndmqFfSjxF1uIpZYOtUB50T6GD1s7CybVP7bqHqKxRLn0aNqY3IWuTdlUpy68GXHJEp3A_74a805cC1z89_WpNyDXhabcNDsGN1oU6v34jndi52f7YxSfGjz6bfuiHAzsI2_snO1w2hSNuze2GWGPqGR-FpyqZ8qC8BXwSuv_hfIbPS7zhrQDArICOg1iP4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
:
گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است.
به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار باشند. مقامات ذی‌ربط در جریان موضوع قرار گرفته‌اند و تحقیقات در این خصوص ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/70892" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70891">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=me60UGG-g3CPEydcYbf0rz2i6bia137mtfQxGtYvBkxAPFKLNzH0tdJv0fNJacIhrtWqOUe1-YPY_WN8lRKBJf2xTohNt59hwfif_grBtnj74nWiv1QHFZhQ6omnGk-Zip8IF9cdsnIzPBE857A_7U5czr20WGznLDY54T234wwj_8ULsFhS7S5IVp1OtupXRu47Q1AQ1saoG31IRI6KDgC7eR0dMBfpqnkeZxREn1akcJw3k4UnX9IFJJ1E2s74uBoYPn9PWE-myKaRpkuRtYawu5Hc1hdXvjkXRGEm1jn9k_qHMjBxPEZ_VXjR7nLx72AmFOIdng6jLHCExNxD5icrmK3AAaoH_NiV0fTiJO0x5OCMkBaCJ1eG_O4lvFRbzwcsQDAPmFNluz8iiMiAfCB_r358VZn11nTg-ZgOrg5NtVeUrir0HCX25J1aQOHUA0Fpw_7Meqwfe2MkcF10t5WwHekH4-lt_t50PILkHe7jIq0Zpqv3Xn8idwVOO18UVdSId9_WTVFgavu8f0dr7CjbtbWOzoVRWWDZUGYKechE8BkMGWcp1PxB4z-ZKMNVUAhySC5uarJOPLJ0LvuzoINBKSagW9NyaK7GBtvz3ZWQFumvu6Gkg1HLjXpHeDCj30lrlFTSccOkJKLIsxYYnbhIA0u5Zmgakp1y0Vj3HYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=me60UGG-g3CPEydcYbf0rz2i6bia137mtfQxGtYvBkxAPFKLNzH0tdJv0fNJacIhrtWqOUe1-YPY_WN8lRKBJf2xTohNt59hwfif_grBtnj74nWiv1QHFZhQ6omnGk-Zip8IF9cdsnIzPBE857A_7U5czr20WGznLDY54T234wwj_8ULsFhS7S5IVp1OtupXRu47Q1AQ1saoG31IRI6KDgC7eR0dMBfpqnkeZxREn1akcJw3k4UnX9IFJJ1E2s74uBoYPn9PWE-myKaRpkuRtYawu5Hc1hdXvjkXRGEm1jn9k_qHMjBxPEZ_VXjR7nLx72AmFOIdng6jLHCExNxD5icrmK3AAaoH_NiV0fTiJO0x5OCMkBaCJ1eG_O4lvFRbzwcsQDAPmFNluz8iiMiAfCB_r358VZn11nTg-ZgOrg5NtVeUrir0HCX25J1aQOHUA0Fpw_7Meqwfe2MkcF10t5WwHekH4-lt_t50PILkHe7jIq0Zpqv3Xn8idwVOO18UVdSId9_WTVFgavu8f0dr7CjbtbWOzoVRWWDZUGYKechE8BkMGWcp1PxB4z-ZKMNVUAhySC5uarJOPLJ0LvuzoINBKSagW9NyaK7GBtvz3ZWQFumvu6Gkg1HLjXpHeDCj30lrlFTSccOkJKLIsxYYnbhIA0u5Zmgakp1y0Vj3HYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی دانسته‌اید؟
🇺🇸
ترامپ:
من هرگز چنین حرفی نمی‌زنم، اما پاسخ «بله» است. هیچ دلیلی برای آن وجود ندارد. چه سوال احمقانه‌ای. آن‌ها از نظر نظامی کاملاً شکست خورده‌اند.
من آن‌ها را شکست داده‌ام، آن‌وقت باید علاوه بر آن از سلاح هسته‌ای هم استفاده کنم؟ چه سوال احمقانه‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70891" target="_blank">📅 23:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70890">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcGcIvQwEtJijYzElGlMr_YzvSIr5EelXAWcDtZRLWW9GzaratfN99BPpoq4uv-aZl2NJ2f9tqYGHKatn72juM78xsIRxDdPQlu6FXTtWmkyd7IKaI7NsEnkmfYFC5UEJDIU5q-57zDApMDZpESP7vwPqm0JG15WafebS1mXwTJ7PyhZLa72qkfFGzwoU85OVPVTzdOC1n52SR7MoSbprCnLUhrYMOG_55pE-Jr5rcKLVqqUTgfBSJfBcdD89JVI_rnmFVXBs07UeaclXeCRzWrW8drVNWvO9tmPI5RQOo_XM12RpRO6x_D6yS1zXssn_naid9IGhldwhYMxQEtL91gk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcGcIvQwEtJijYzElGlMr_YzvSIr5EelXAWcDtZRLWW9GzaratfN99BPpoq4uv-aZl2NJ2f9tqYGHKatn72juM78xsIRxDdPQlu6FXTtWmkyd7IKaI7NsEnkmfYFC5UEJDIU5q-57zDApMDZpESP7vwPqm0JG15WafebS1mXwTJ7PyhZLa72qkfFGzwoU85OVPVTzdOC1n52SR7MoSbprCnLUhrYMOG_55pE-Jr5rcKLVqqUTgfBSJfBcdD89JVI_rnmFVXBs07UeaclXeCRzWrW8drVNWvO9tmPI5RQOo_XM12RpRO6x_D6yS1zXssn_naid9IGhldwhYMxQEtL91gk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شرایط وحشتناک بازار با قیمت بالای دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70890" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70888">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laEIC4RCocFJYtQh3m31MQ0FAYG9Giesl8XNkctbeABwDdre92w2PVCPJ1I7Gp61okOdEMfPjl2fqCO42iq6k5Qvb5Xhuy1B0w1oA6Fm2WYPbR9v6QuSxogTz6se4_EJnFG_Ta0J4XqWVQIF3Py5S20dFA0LM_49s2t8NW3snra2r0s9A9K8SfUttCX3aNsgk0zpFmw7KS2L0oTs5hlndQoi2VYXchfUnyIH6ctgjGC5S4gcpvKiBx2rbBfhurU-HQ9XdfvvP2A4T3b7oeLD3inC5VwiThZ6TBMfGvG7lw_8vCT03f8oT31wRgkBAfE0yZpSzEPFHPrx7EJhqcuHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbFedcl6lbpIBiGYmyDTfrltIn4lG_FnPITahWoQA10g1Pkdr0edq7if9nPp68AExSD0wOba_D8u9C_DaVDi2Yn15C8K-dd4k18oB1qC1vnv9zgeYMnoQ9JgDKdtfw65dDTlDK52_Lsz20-mnM0hlUzI6Ysy9Rw2ebXZYsWMC1tRFzOL0zAQcFxe8hDJvfch_TgareTrkMlSxarR5qLN3WN3YGFA1ldWvfGR6KnnPjbgn_vKIC_MpypiC0bWpUYGs6WPOyIeRQPM_h-jmyf8okvib9ggXUhJge07jE50rOOeVQgMv7naGKqbVgrg-MvGpqEL306Mk145RduIai3lHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سلنا گومز و همسرش:
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70888" target="_blank">📅 23:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70887">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=TzFNMt5-YU_yFTi9wodDiGLEi--mo9sXKzHDye-gkL-AXEhsOxJDTZu20OvTjzYdQfAZlD1P5BRM45hUoG1RglbFtdAfnmVpRtQy3pSqu7O4Eo5v8tRhMToK3Pwvp4qROTEAbNzzPFagc7Ku7j_vyu90lK3dz3VeH_Y841ivg_V7eoSE_CCCE-3clxfGRcuagTUmVY9glFFlcGu234I6RE2LwlQF2jKGEBstQ88jHXc8JW2kfRwfkFQmybIwTNBS_8CFrFphjBCIM1XE-9AqOKlwhc_Yf3LLMgmpWnflEUZI6VbMINxwMo8Kb9Nlvgc3UDKtRKMeH1i1bgrxb21TSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=TzFNMt5-YU_yFTi9wodDiGLEi--mo9sXKzHDye-gkL-AXEhsOxJDTZu20OvTjzYdQfAZlD1P5BRM45hUoG1RglbFtdAfnmVpRtQy3pSqu7O4Eo5v8tRhMToK3Pwvp4qROTEAbNzzPFagc7Ku7j_vyu90lK3dz3VeH_Y841ivg_V7eoSE_CCCE-3clxfGRcuagTUmVY9glFFlcGu234I6RE2LwlQF2jKGEBstQ88jHXc8JW2kfRwfkFQmybIwTNBS_8CFrFphjBCIM1XE-9AqOKlwhc_Yf3LLMgmpWnflEUZI6VbMINxwMo8Kb9Nlvgc3UDKtRKMeH1i1bgrxb21TSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنسرت محسن نامجو در پاریس، ۷ آذر ۱۳۹۱
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70887" target="_blank">📅 22:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70886">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=GrIJAVEqHE1CSFU-2azcOJAlGxphNuDLB3MgYmGM5sJHWxIBflwW55drc4QhIWiuR2_h6rR9hzDQO3rku4Xg2WGyMRSPJTFlaZAomBmUXvV0l_Rm-S9oqnmRxu9ABcZaT2a_FEeSoigyk6mcLm366FGXhaJY1nmSYqZIq1Up-6FnrVTYZwussC0tXXpIeNXdlaxYVnKhZbe8S6ooozvNyEZGJWl4KQldadX_L-z90Q0dOksRrPn5LhsfEeCVOPt6669WN3qbneMkDRqKFES-F73bs1A7EtnfCm6uyGtOnFqlrioE04C8w8njpfpbiACb-rWqzsGcj9_i-CHFWjJLmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=GrIJAVEqHE1CSFU-2azcOJAlGxphNuDLB3MgYmGM5sJHWxIBflwW55drc4QhIWiuR2_h6rR9hzDQO3rku4Xg2WGyMRSPJTFlaZAomBmUXvV0l_Rm-S9oqnmRxu9ABcZaT2a_FEeSoigyk6mcLm366FGXhaJY1nmSYqZIq1Up-6FnrVTYZwussC0tXXpIeNXdlaxYVnKhZbe8S6ooozvNyEZGJWl4KQldadX_L-z90Q0dOksRrPn5LhsfEeCVOPt6669WN3qbneMkDRqKFES-F73bs1A7EtnfCm6uyGtOnFqlrioE04C8w8njpfpbiACb-rWqzsGcj9_i-CHFWjJLmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای بدل ایرانی آنجلینا جولی:
تا حالا یک دفعه هیچکی دست رد رو به من نزده.
به هر مردی میگم با من ازدواج بکن نه نمیاره.
از هر جای دنیا باشه سریع خودشو میرسونه پیش من.
بعد دوستام میگن تو مهره مار داری دعانویست رو بده به ما.
علتی که اون هم قبول میکرد این بود که چون من شبیه آنجلینا جولی بودم، او میخواست این وجود رو در کنار خودش داشته باشه که مثلا مهمونی میره، پیش دوستاش میره پز بده.
من حتی بیماری‌های مشترک با خانم آنجلینا جولی دارم. هم قلشون هستم. ما ژنتیکمون مثل همه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70886" target="_blank">📅 21:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70885">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
📰
اکسیوس:
ترامپ طرحی را برای حملات محدود علیه ایران در نزدیکی تنگه هرمز بررسی کرد.
وزیر جنگ از طرح «حملات محدود» علیه ایران که ترامپ در حال بررسی آن است، حمایت می‌کند.
طرح «حملات محدود آمریکا» علیه ایران هنوز تصویب نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/70885" target="_blank">📅 20:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70884">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⏺
🚀
فارس:انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70884" target="_blank">📅 19:59 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
