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
<img src="https://cdn4.telesco.pe/file/KQYllhrq5fquFtHCl-q3zQgK6mHyFRITxhPfTjZAVFfEZxjL5smCcAsz8EuTtYbMnZoqBTW9beNEJdLakE6fiB2sox75YXmlda737VXHmtfPUH1khrPvscjX6W5fIxMnXHtaszLHO_QSeMSxyPpnaA7ThK6IdDznx9KKY3E87D3kIbWk2dhgeDXuo1Dd6qWtUjqfXa_Fj9O2vHHdraHj7EKGhZRLgCKNQLvMAJNJDK1g8YOIrVCjTXVph6WRw0BVEoA4CHwCvtKlT6F-UQwbJe2BG1Bg18qrPDNY3gGYWeWmiNT9Sje-6VnaYHNd2t7tZBzDg6iTNDj8aEN2Lh3-Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 345K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 00:35:10</div>
<hr>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1fPT7yDGUnY6o3ShR3ce5V0F0yxQ6SKBG5J0ZOQVxaqJks46A_PGLm1DrQ_Y4YxItzpUy4B0AU5Z3w82eXElwnnWWwFmAnZB1UAhMAmxdy3edoQZrmqQbe8OuvKyVnONd3uyj1vS2XVFC4v8fwfn85envznfD4R6snCiYEHnvMo7ULBZu26hGAf1a2AHY3X20Pp-b9wHDXF38WB5gZd8c5nLWOrDUH3pbZ-n5OdouqUE5Nfr3MvR7ImuoyAYtyhj8uiTIm_u_mt0gcMAMn_IscztFZLWea0iluOLT2vrmOHI-npwNQBpFdGKhongJ0YuCBEV47Es9mGXXpUvhYB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxTtbtuFQI_UypHu_5Ems8_AT9h3IyAyWl87gciFKwpYXbu8SlqUglopvbME9Hpo6sRkUbaZqIP3DarfPDHzzPQsV7r1jjtVhIjJxWQ8FjILmSpqST39Qk1cFDnNqbv55j8azVxSOJTOMNIDgMC0KjTkGM4lI_Mht2upmY0f52mA90x2vkM_5CTjUiEu0cpjkbH_s5Ykd5gvSkmcZe_uEb9BjHrw0e1Cn9bK20BBXRV1G0tGyQ493hr_swoU9YKAWg6xXEZRN99zOUHPpCn0oCMrbpDeUTS3TPLqZZ_-Ck1mzK5_NHzP6ATMLIaQg1xGMw6T0_scei5Z53gE23VIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=NzCp9n_sVKErlLWxk4GuQNWbzog15Boh192swVWDSx3RR2QqkTb9gF5IBOjnnx2CupBB2ILMP_7Vb-PRATXxoFe5SoH0_t5hNrQ1mB1uSHxgNGnmrEmMQJ1dBEkXjmtj5iup6VRl7QR08jbmzOpLu2rLFHUStFbCSgzLRnzblm2DuU4tVsS2pV4AgpDmYHNVyFZ4CigOqPQHX53XkSByos-nSec9_2dLzbIOmo5C3j9IM5IuzsidxNKvx2_c1VGeN_melrNJ_q8YO2dwiDzX1PxYrtWcVgQIoh3a6Iv0bF_yBMkr0h4baTXfx-0ovAZj80rrCkRpeVgWjM3fNQuMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=NzCp9n_sVKErlLWxk4GuQNWbzog15Boh192swVWDSx3RR2QqkTb9gF5IBOjnnx2CupBB2ILMP_7Vb-PRATXxoFe5SoH0_t5hNrQ1mB1uSHxgNGnmrEmMQJ1dBEkXjmtj5iup6VRl7QR08jbmzOpLu2rLFHUStFbCSgzLRnzblm2DuU4tVsS2pV4AgpDmYHNVyFZ4CigOqPQHX53XkSByos-nSec9_2dLzbIOmo5C3j9IM5IuzsidxNKvx2_c1VGeN_melrNJ_q8YO2dwiDzX1PxYrtWcVgQIoh3a6Iv0bF_yBMkr0h4baTXfx-0ovAZj80rrCkRpeVgWjM3fNQuMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwnHnd08GaXtjpIv2G33spMKvafNQmPbxNC3ZjNgwis5lZovY2peaCcVmtYhk6xBiu_wpp78H7GyhEzsizcYrVZCjYMmtQERgWE2R70fzxjTbUTHCwJqb0cVM8lCcP46P0XxMGEkWGj3okwiYZkOIPjvN7GLs0uzJVt1x1LrdrEviRe0EdaT2OvZH3F60Ap46CDfIIlX91TlpiuANxlCxT3HaRIXWMQcF6cTYzrJtzLqfzOsFcQkmJlOUHek_fdV3o9SMJUyIbWgFGIunKg8USyfMTyTK66udbUZ85T0q8JobDq97RPHucg4muwKq7OzKTb-l6TBgZtnWQXyV3rYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls_1P_wySArlWWGht1jsb7lYY58QnwWEsuYyQg2tFmrh17T87puLJmhzZc2BQ_KeqlCbnwn0B-fGQReV0tIxJEaOGObR7Atg9BrUNIuLVAFwcTjAhm8ODo8jkPErIhWjRfyqscVFHXZtXKD9rxz4_gKSQ6Bx6fT9wSHbXSDKgQOfBxloGc2V4wSaJEBmSctD7Ms4jvf3uzVa05OmDGg2hSkD-OAL9632U4eqlK9kFxUjus6B24qwkqK6GPwhkw_xJSpvHKXbmXVjeZw5gG2RKpp06vbtS3ydpo7x55mBDa8u0i6DAuwHlwJOGLeGPDYZRujcH9KdVJ9pO3i3nG7OJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_Ip5fwjosYmVO57UJWi11kjLWZKVsV25QEno5k3mehcgpa95K8tp0y5pzfHmbmdLSpm3NiNdNJUbXI8gWF9H6v6oz-TbbmMjIEZdpw-42GXaQkv_o7MKHNLKM0EB0-h28Hv9Lmvp6-ZvDJRaFQIcs5cAOuRoKKAEFZ0SkYRLMME9zuZnb3dVSCMqrqpa6ZheJo4rvdAEkiXoTDKhq-2ho77OmADVDwTpJubeZOpCI7CGi-RIcEJxkD1gJ-FtJOqCSEN_NOWn4cdubRruuAOOGT5LjDQP1KC_0JMVDV3_UxUfm7KEhWH0XUEDN0mZIYHxq6cCtVpqBBnq6TW94fVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK8h2PYEHCb16ee2k2p08lBTCU_petDL1Jj_mn_m7HSzigVrHWOCGb8BMkHCs-bo5IeBodEfQh9YBP4GjUCHVN4g74P_Rb6Egzle6HsdJxVkHDZgbLMDisyxJYppGRrh7bcRngnIpDbY4etDQ7vYOXx6ocsnwkj1cz_5tkVTWpVGeMtNCP2pZ_DzRzWYeU2r6n-YqMFEJkWr0lsVJJy3OVeMXlACtcMWXpU4M40wtzMi2DGQ7qUonaF0roI2vdPiV1oDeeDsHUSsoooSacd2FMQwensfO1YFNYqLkytxlNKMyzPHZwD9mwYE7OQNlNgRIOJ7LRmqwgLuqvIvfA5KeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtdPFfzG0Roi2f4pJmU-wqjIzG0QJbFSOyzg4esMF5pSfuWEE1u_ml-toIG8AGRT6Xtkm3m9R2e5BDeTHFz5dtVCwhNIDiMWYqKDg3CWrmT6XMsgrlzTQrW1s_OXCPvBulOeqBeDm-X8p3CBzcrRxKadHpwV_hp7qhwsgUjAt4PGE4_Y2XgfUtN-XPkTUPeE8swz261l40PGTcZJiajy_zldmYpQmMxmOaf7Nv--PQM7ZXkzocJnOHUjC7aLcXHHGmtjhUbQ7yQqae9hZNFvnUf7MdOXzgEqeHZQa08_7B_GEQ54YezNQ-TkNx2qwqkHHvf4q-0wVJn8zF28PPXo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🆚
🇲🇦
🗓️
۹ تیر
⏰
۰۴:۳۰
هلند
🆚
مراکش
📌
هلند یا شگفتی دوباره مراکش؟
⚽
🔥
هلندِ که به عنوان صدرنشین صعود کرده برای ادامه مسیر قهرمانی به میدان می‌آید، اما مراکش با انگیزه تکرار شگفتی‌هایش، حذف یکی دیگر از مدعیان را هدف گرفته است.
👀
⚡️
لاله‌های نارنجی صعود می‌کنند یا مراکش همه را غافلگیر خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/24634" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3KfqEW3b0AQvdNjZ7uQH3g4lfek0rqHM9H-ZqHod1J0R9eAmziyaUQlmzMg4EB8HDBJ5r6PDFfnryeR8bFBuyzMGnRqdebNhiKPIRXCtlUN2VkPv7O86I-sWnZkgrFJ7e4S3oiNUFxOs3CQgaUVzhmoCVX4sW38s62diZOArINdmbaHmqvez8FuNeiT28a5fy3mN2N3JJRnQL77086G45PUIHvnnBr-jK49Bum_Bm5aCNrj22zeKYI9vGKXRghqfHiCDzaPbElfZer0z6Ir61IR42-fFzwzB4oJn8YSewbf22WAU27iSew-0sV0FsX7SQgwb0KA37YXraZtmiwa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbGpqMY_LQwwcLH5WmlJXHAkBTORebXz-R93-RlM_7O0OEBLZrN6nHzCy_efHeUQzurilg9igh8_v6kNri842rKs5kz3S7mKZn92ULRMHlse0FQjEIku7Hvn5bjuCnPJzymTUgfUZ1bF4cR-Q3_E2BuSn0O2sFNSwMU48FSM03mF5nPQda1Gk7K_6bnbmg_TYBnykUw9CXwbaAVX7GEDeG532q64qQYC4iV19JxTwC8UeVVjml3ygMvvf3NeuOshJqXxHrncgQiULn0zU8z6zDF5IgOF_WgzBZJ9bZwjZLX75OrBGnBxa6VzyjiDaz64aeVyoCSEIpM0gzmqxqXGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=HN3aZjjgIKa-M0zLrgtQK1ImjxUTuOKW4A8tpskhRlbajo7oeIPjy_yMH2o0uKpG5HHytD6cTJRP4oSTv1GuUsKII89eNT9gregXNEWuuM68HElpqdtWouEu6D5fZf21pQkvfgeUDeKq9DmaTXzf_EfAxO76g2shXFDdUnvAWS-tlS0E3DwOydpAyEX1sNBZLAqZ3-FAVW2mNBsiDbuO45ufR9J83srUHzLMZMz0egTrm4RBU5C0a3BfZdzOb_VHyQPSQ5MbBwgpBl7u3d7ERKs1JB4enuuKhcLDPqPqGrMUBnvpUUredgK3t-Jq6hSklilHmjVfbAhGfAT2Df-PfFZjlKETJGWknj2Up8yIGNC5gW3my7015BVoqAM8IOlch9wxhZg1qO6uj35lGQckxCxs8jXvc204woJc8XdbniI1d2OOG5EVVAC4UWSSYyX_ZDLQS4d92DXkcc315rTqQ3GVr3WCw7vAiyajqz-LjHvph5gg0ho184OAWGWYG8XOqBpJNHIY1ZmyON_bQBP_1P8diFChJ_spLh54CHmBoPzVJGKfnTMDTQj9RJlUsLaicBIBfDDBwZtBLX7V-3VjF59ocFP1TZJ1J6nWtTKJHiOztRnbq-Bfd8C13RV0wY0UqXiQXCbD6t7Dc0K8M7-WwgifwQA9IT_08bSk1kdIIgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=HN3aZjjgIKa-M0zLrgtQK1ImjxUTuOKW4A8tpskhRlbajo7oeIPjy_yMH2o0uKpG5HHytD6cTJRP4oSTv1GuUsKII89eNT9gregXNEWuuM68HElpqdtWouEu6D5fZf21pQkvfgeUDeKq9DmaTXzf_EfAxO76g2shXFDdUnvAWS-tlS0E3DwOydpAyEX1sNBZLAqZ3-FAVW2mNBsiDbuO45ufR9J83srUHzLMZMz0egTrm4RBU5C0a3BfZdzOb_VHyQPSQ5MbBwgpBl7u3d7ERKs1JB4enuuKhcLDPqPqGrMUBnvpUUredgK3t-Jq6hSklilHmjVfbAhGfAT2Df-PfFZjlKETJGWknj2Up8yIGNC5gW3my7015BVoqAM8IOlch9wxhZg1qO6uj35lGQckxCxs8jXvc204woJc8XdbniI1d2OOG5EVVAC4UWSSYyX_ZDLQS4d92DXkcc315rTqQ3GVr3WCw7vAiyajqz-LjHvph5gg0ho184OAWGWYG8XOqBpJNHIY1ZmyON_bQBP_1P8diFChJ_spLh54CHmBoPzVJGKfnTMDTQj9RJlUsLaicBIBfDDBwZtBLX7V-3VjF59ocFP1TZJ1J6nWtTKJHiOztRnbq-Bfd8C13RV0wY0UqXiQXCbD6t7Dc0K8M7-WwgifwQA9IT_08bSk1kdIIgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZdohz2TApj49LC5iZPm72kpMdzwWCQl0X7TEqq5J-4AaOerzczm2ZGzT3jquEoUd9EboDoAi0mu7iknISglPiKgzK80Y20HBzb94tAfHnvwJPHpOsmEh6co7BS3CFfEwa47M-J9NManNuqRJ2Yoc4GJ4NbYVtGBeiifIvokamy9dgaWfCMwQS9IeX16IMnIuJtV7hkCIUqhxBy60ROer2BW7yuRFATLr30wdDnUvUMZ7JQv1rJ77NkFCJxEkiz-BpvNY2VmvpuD2UPtMwXQvmBN5fXsH62RvMkdp1Xg9lwT5q-V28BOAHG5M-5znF83QSvWWf_iVL4NEgL09vyBFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=STtO8qA9kJ7GI8F7T-uBEx204hVTHAwyAoX03DmB0HqtsETPPgHpEM5-lFobHfClA5hR_40L3F5KH5SGkrITOqhes7AINEeBj-AblXAmS0Mre_PFLJ3ENz0HYwjb3btoaX2SK1HDmfvdtP5ISgHkKJ9Re1JEJVj9kSYKAcf80voQqtB9GgYF1mss_A81m4AU7lSYWdm6K55Lb5lRK_36tIJT6az7RnnEJh5f3kpRehBLIwfUOMnHYK4Xoj--HMJVWG-5WoDnWWRmQqbeKS1HyOvU6xGGgCtQek5w9BTk0cjSP9SWh5ludmoCebiREoENWNp2C_gfAprM5pg-91Kq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=STtO8qA9kJ7GI8F7T-uBEx204hVTHAwyAoX03DmB0HqtsETPPgHpEM5-lFobHfClA5hR_40L3F5KH5SGkrITOqhes7AINEeBj-AblXAmS0Mre_PFLJ3ENz0HYwjb3btoaX2SK1HDmfvdtP5ISgHkKJ9Re1JEJVj9kSYKAcf80voQqtB9GgYF1mss_A81m4AU7lSYWdm6K55Lb5lRK_36tIJT6az7RnnEJh5f3kpRehBLIwfUOMnHYK4Xoj--HMJVWG-5WoDnWWRmQqbeKS1HyOvU6xGGgCtQek5w9BTk0cjSP9SWh5ludmoCebiREoENWNp2C_gfAprM5pg-91Kq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24627">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سورپرایز پامپ با جایزه یک کیلویی والگلد
بعد از پامپ ۱ و ۲ با قیاسی، برنامه جیمی جام با ابوطالب ترکونده
اگه میخوای از یک کیلوطلا سهم ببری کافیه تو پامپ ثبت نام کنی و هر چقدر بیشتر بازی کنی سهمت بیشتر میشه
فرصت رو از دست نده
اینم لینک :
👇
👇
👇
ثبت نام رایگان و دریافت طلا
کانال تلگرام پامپ:
@pump_vod</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/24627" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=bq3K7mGH6cMCvZ3hyaJqciyy2qwBB2fsSN-VUexWrHxUw5WmPPlw4wFrjJiP2evdwT-5DNNlhoIWDl3ZfuWfp9gYAht0Po_RXbNZji16uB-W9dV8JJPR7_Tgo8VnPzeiRQCgKbKAk_X27Ms0ZlXkHsY9N3o28er9ZmKujffnik9xonX5pZ24boTbfsf0dLuF83kgxUSh8X4KM0PMVWLZAQdtn-cJbmrBkQupkSom3Rc6egZdaXbA41Ra4FP9_CwMOgUjb51RCumjoFoeyWgPe-kpb2T9lCX_zV-Ek_nZpGIYStUCBXZS1pT7sr3YWWrEh7lD5hK7CWGYeqNi9_dTe0oBBofg7ZLAO0lVpVVyO5j7iQhsGq79sG7eK0i6mSAQSsBQep1EmFJjRQevAweq0-U2gQ94mnsrBiTR_Omrw7XjaMoEGp9bGhwit2sFgz9P9dePgMn-VKrpc78DNdYnZZg0p-deO5LiK9fgZ7-5T9CoJxKGBqP0Tn5XUvgVgaj3-4HSN-kREksvPz_IedIRCjS3vhVoelJ4SLoh8CQe615oREjHOL7iK8QJrGdOdLbgRV1GZb_NH_Vrq6C8x7SWjU3hjjSsSUTZTCREtixTTGvEiJ987cj4oAksjo7xLxSfD28GGGMnddfVG7OMGkZvhtNjsk7VAiF3NbI_EXPLpVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=bq3K7mGH6cMCvZ3hyaJqciyy2qwBB2fsSN-VUexWrHxUw5WmPPlw4wFrjJiP2evdwT-5DNNlhoIWDl3ZfuWfp9gYAht0Po_RXbNZji16uB-W9dV8JJPR7_Tgo8VnPzeiRQCgKbKAk_X27Ms0ZlXkHsY9N3o28er9ZmKujffnik9xonX5pZ24boTbfsf0dLuF83kgxUSh8X4KM0PMVWLZAQdtn-cJbmrBkQupkSom3Rc6egZdaXbA41Ra4FP9_CwMOgUjb51RCumjoFoeyWgPe-kpb2T9lCX_zV-Ek_nZpGIYStUCBXZS1pT7sr3YWWrEh7lD5hK7CWGYeqNi9_dTe0oBBofg7ZLAO0lVpVVyO5j7iQhsGq79sG7eK0i6mSAQSsBQep1EmFJjRQevAweq0-U2gQ94mnsrBiTR_Omrw7XjaMoEGp9bGhwit2sFgz9P9dePgMn-VKrpc78DNdYnZZg0p-deO5LiK9fgZ7-5T9CoJxKGBqP0Tn5XUvgVgaj3-4HSN-kREksvPz_IedIRCjS3vhVoelJ4SLoh8CQe615oREjHOL7iK8QJrGdOdLbgRV1GZb_NH_Vrq6C8x7SWjU3hjjSsSUTZTCREtixTTGvEiJ987cj4oAksjo7xLxSfD28GGGMnddfVG7OMGkZvhtNjsk7VAiF3NbI_EXPLpVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8A5E75KdTy_NAA5GPYx4mo7IlcPz-9PvboPem23rXXiRIvEpgFx7Op3hjmgDbhaE38otYoIFDjIEAr3mIIUfFP0fuq57ZtdkbOLheDi4PumrsHb4UNjRcEipCM7YnE4QtegIBQfJZ8lmcax3WiTEEP_xyym_hlH_HUmmnDTb9ii208wP7AkANy-UqJr-kcRpFHHTlOaERzg8SHikRJDao5f7C1HDVNVY8JNaRwmbiutWAT9hN1C7_56eTXeIlLv_C6aMBOHFGWmqhyY35mEpywUtIGMz4jvA3f1UoxKhzg4YbNf7ZhGbFEKe8k-Hq47zs-yvD-0vWb9K5XchRktGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=XJrXqclN13soqQT_0fo0ApG9TO_VPwjcO_Ky4A0Uf_8psrIMhsuzxuJRV_uDY5vSgHsIFSm7wXMU9-HQLtl_d9Qa6_f3p6867eSJ7RgPe_hNZ-KyN5VAIkXM_yYhT0gE-rgoPrYSKWKLxxJgL3bK48BzcpxJaSLjGwi6y6m40GvOBkwu60U8GMzQmYo5eC53HFIAITAsaT00Hu51GXMk8DZQPxAS3jEK_a262jj0-wrn5lWYlgeYVMy8dv-qX-4vxCfnSbT2PcV7N43WJQHnh9ycUJILvSRmD4W21BE1n-Mut3trKupiSyjG_FKcRBrFi8nyL1fyTcPPLpC5a8VD5avR-OXLirvxz8ndwv75k0ZBqxMjS87A651YlMM-UCKbOu70zLpF2lWoYhysQhVLwnLjJcZviJke7yjYO6R-HO0vlpOBAS-DDWKPhejZUjuEK6nZi6PFT7MKWlRMlQEO0Q41D5hrozWLAU1kcO-wWpriyeC2BM0BP9GEjCOFwpldHx6JNfth4FsJCZ6w9ao7Zq0Ep_TnOVir-YBDJ5dDS2U0CLVoY2H_IfZp5BNN8okd66E0hm0hs3TARmt1qhTH0t_TEoCivLttJpDlWh-NjidSCWsSNkLfIHEhVfUqfK4-d4hCi5PjpUGgRDL_rtXLj9AE0LTIr7g0IFaatv36-54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=XJrXqclN13soqQT_0fo0ApG9TO_VPwjcO_Ky4A0Uf_8psrIMhsuzxuJRV_uDY5vSgHsIFSm7wXMU9-HQLtl_d9Qa6_f3p6867eSJ7RgPe_hNZ-KyN5VAIkXM_yYhT0gE-rgoPrYSKWKLxxJgL3bK48BzcpxJaSLjGwi6y6m40GvOBkwu60U8GMzQmYo5eC53HFIAITAsaT00Hu51GXMk8DZQPxAS3jEK_a262jj0-wrn5lWYlgeYVMy8dv-qX-4vxCfnSbT2PcV7N43WJQHnh9ycUJILvSRmD4W21BE1n-Mut3trKupiSyjG_FKcRBrFi8nyL1fyTcPPLpC5a8VD5avR-OXLirvxz8ndwv75k0ZBqxMjS87A651YlMM-UCKbOu70zLpF2lWoYhysQhVLwnLjJcZviJke7yjYO6R-HO0vlpOBAS-DDWKPhejZUjuEK6nZi6PFT7MKWlRMlQEO0Q41D5hrozWLAU1kcO-wWpriyeC2BM0BP9GEjCOFwpldHx6JNfth4FsJCZ6w9ao7Zq0Ep_TnOVir-YBDJ5dDS2U0CLVoY2H_IfZp5BNN8okd66E0hm0hs3TARmt1qhTH0t_TEoCivLttJpDlWh-NjidSCWsSNkLfIHEhVfUqfK4-d4hCi5PjpUGgRDL_rtXLj9AE0LTIr7g0IFaatv36-54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufmRqLNLDeJlqFYpsADBdn0_RezOR3lGimo9wXNDPgTvIvbamzXAlVb20lR0wEEcXRhhpLBgSj_H1NdJKhcW78qfZLOPIVsPhfqGU6GKaHUafNichqXhF2V-wvUkuQC1n-wLsyxNYTDUAB2kIhMszaOdsEnyW3WPPmEDimz9k4pIcdwybLN-IQ6wO2N9Izt6L99Ej-MUq1sD1fRfEDqaDGnD6jVzNqAgzIlRSK0mLYEzSCIzyOwp_-jBmk_f4V8Bi9Iatg8Mbd276u3_TR4rm6p_FEP5kqd-6y88IHgjx0Cq1Xkn1u8puf4mTM4hvnJJmtchcHo_02Ehp4KZXUr8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmSRFaKSRNz3TsWZ2HEO3qH6ZDhrCrdLFTVilXHYSCWDy9mARSSsY9_4QRLUrTy_UHVWdKSvC8ETOFYZ_2Ey8hdGYIfr9MG5CSz53EBJHo62sMHuNzPD8GKKoa_lCP2j_UuO2ze2yeX9xQrIGwBTJBnT2t9gUD2c9__NPQ5BO8AA8UH6JCWtgZt-9gHzI6GEfIeyfpLcFVLLgKZRcrw5YJ58wMsRCgFrwXG7sp4z2oZdKHcLYi01xgMykx_MKnpgvxlE89Co8_EhFnHiq7co1MwSzg9Rqd3PnyoPMiiAETS6wUggGBS5uMgdyGtqAZdzAoiXXj-rnUoLvzY8QJjR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZFn6PvIKjH6YZQ6HLPS01OmOjxx0vr56v16UFNp9F2wpVauMqh9ekAZ3fN1yUWCxiLqrH2gvmlrsbi6bfKe-Ukyjm98hOrNT90GDcI9DgOUcW1i8zymZwYGQwvyKn3VX5ea4o_uscI5T2t0xSgsPkwTLuBmq907FNbQ0Bd4eAeYJ8AmxKGNPRCACVCZkyc44YU9TaTb6-7vvnfFvHrzuD8YjflW2lg6lZlFxQYanzbbFpc-hjpy9lOzcNG8ZVRoPhfeNFNgeX9z8RKCevtg4QiZtTeKPXXE6JPCrsnux0loXrHd7zlhieaUhogqkjTxie_m0ZfBmnOVpUQoKiMy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/givv9g2lmwSCgvhOJveNTQeS8tsFKkGcmWj6BBsqnCYZsDIv_sfw7AiY1knUrW5ZyDgUAHrIP6bEK9p2uoBsEGqSOxOvinJlqpvXpFBc0jopYou2MaKm072UKgDIBRNrojBtycFuMVb_iJqxQbbqv4pzPqg_31fe8SrTEs3B3h0dGQjlc9pKkSUtpIylM9Uja6HIZYuiNGCNasm-GUPkAi9AhaPJPNFjowVSbSJtbA8qvPDRZNVIa-UOpSWjwzpsvMJP7STjjxb4iTCMS0PDWLMoq4o7Jaom0Jp_526jaV1ElXE4JEwkRabyyIroexDAqlbjJDlDH2TzYgUi70JYGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ6sgMqG4FCjjw0QEtylPseHHICwGhLs5sTnFYJ_70iNqy5dTbHdQaD3eWXowIjFMpCBXS72KLV0PBM74EHT1gphC9nk1cCdFjx4aJi6iQRlDGKPdsHevyA3GsEYUTkZ0JKC1Ok36NBEUQEJSce7vPEyPYZ5zRejyMUeQilIlfB8VmSoklveKWTht7BgfKmZ5UJQY7C2uy3k0ye0jd6t9f57e8VEwK0kT-tL9ehP16JX6-tfU9HM1188BSVqnsbcpNFHLD9yym4zlaeD0LQycZRFWzm248ZZ0IIeyM5_xLYwxIE28M5mApU0KOnSTp2yJ6gsqXfrR0zDo51CQ1JP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehIAdH421tpeiex6J_JmQmLB76NToUFFfQTFcPqJ5lZ1-2eGstZcKp3_oZ8KA3Z4IPBXowvlL3t20B7MRxhmC_5rEJV2NhtjuTbQG70845v2WjToW_hJp-qCGBHy88CnQPIaHInmkektf-XC9aRat9laAvHUPSKW1u81mHrhVRNkgu2KoaQMX5LuZ__zYlJD6bbwve--0N7HH7gqtfHOgrRcZdnXJLxHaEA6X1e77uVfhpyVD0Jt4aBgGeaVXXAKuHXrWUVHP-5oJcMG0SPI6OIKiWZh-Xpp1vmLCrIMAN9k2w7oQsBn15xtdRk2t19829kX02sKWC8qkUa5YJH0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیازجمع‌کنید و برای سهمی از جایزه بزرگ ۲.۵
#میلیارد
تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود 8:
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24618" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5MtM3bfRJwtNK5uxkVlkuCWSoYzxlGojjknEUHCYkARpBibcf3Uwh15I0s6Moap3tQKz4jWhb8CanOH7Pa4JZtkT1kTr81OlrDUNslyL3ppxl6h6MVUOCIszkCP0FdK9ULZEQ0_laqqZtjqYgWk9N5uBzZ1iN3Xe-xi_7ukBYMVyOmVWeRU5CO4LhYSgNTlKc7S58EuOaj1fsre9PRwfxVLfU3QZbDu9JnkOUMGYwjtNkasiE81m6IxmO7fVfPQW8u1U68JnTil-12C4tCWH2R5J7U6T5yr9voktv7nkU6FT273BTxjISCS75auycbjGn8ZKeZEBD09xZaKN1aH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbiK8N5-22NJgp4V9iZ-oK_EyXyPGU7LEdfb13z0au4AjPq8ATvsT63hgGPyxf1fUdHBuxZ1BLWO5rXgRrRYQ8o1qZO1ukFvrs5VbDfCtGGHR9QbZ8byhRZV0Kql1w1nLw88s1KMdqEfzqtsb0sI1tcjtZX96l2Kluzbfn3i0VlCgiL8Jv0D1hQcP47L6U7ftZqfoqNsCQocsoCgaNdu-C4bqaGYOjbPLoMip8tCaCu1XBynw_m9V7xFcZy0cFcLmxpS4-0WyPRWumqz2tKlaZbgK_JiTksVElN_ZS_syo_WXzEcZ_IWmK9pnSf7wofBCoM7p7sWfsm_nJfcHi6goA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItemiFf93oweiHl3qf6TLRmHtxhuW2J0OFLTmoidaEEHaG9d-s2oETJHdbnAuBWd_EDLNOJ0zpyLtYUPA8wOi-yxUQHAD9raCnu9fJdLaoy9y5kfuJ5XKXiZJ4MAQjp9ZHP_LDLMidAZR4pilcqeV0Qd4EPoUQ2HYIv6gmwYXdPpDHpcjKLArJDeb7-qrydzHqWYZXF2Xq6IZD-wmcORxPtgpOipbzXPq4u-f5GGyVQgjUqVzFcOXTq4Ms3XplogQNPkJZ84DqlYE_WH-z99JX9t7MYzpaI30tkTQQxSM8QXGdshDAxp-LLMrOmapLcc1wlEW4LeLx7gqRGCsLyI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1ecOWSbOcQ6kXIjndACDuuOifidFZtagJNBmb_6scZflJRy5o9uYTqxWA5KXBIZ0vMz4pVTqHHm2FDlKJmIDWd7ArFvYRKIH5Bn0-e-zvpGJaUNlU-nLfETpHQMywK1nm0mq0yi_mGnyetLuG3kfBx6K3XeOsXZuCcBp5aJTd02w8LrryK4SaLX9dO_OleX3QOn6DhhRH-t5z7kX8xjefZjK_t2E0gctL1p0sPI0icVIwR2XnocZkwNyquNmevRvmVkJqDd3xDHaPPMUUPBG_GfD5Us0FbvDHT9FXSpKUEbX30KTiKSw0AB9dpCgqaVHdxXnC_Ckq_8HHfaDgkjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJGeW6hqEZfrzvElaGceKJ9QLFH1fJ30ya0TtOaUJS56aU8B6u_HQIxLubdfENl4QcK92LAL3v0cBMTb1Gxczn4wBOHeVPsP-urvQ7Ex-B3llhFSa1IvXLVYo-7P-78Cn2rpitC1RQ_rTzPDJuNMXfbRB9C07MGTxW0jFyZ-D6kCqWnpQzrJf6QAJEYXaTc9NQf6DT6W3ojBRzGzu7qNz_Sdx9H25Yf7g9zWk-hA1umL9Ncw4SIT4SBB1QCxtdFB5_P7Caaz_uGzQUq6-dx87EBNdA0IWBjqAEuaF-FhkDAEeACw_3gTGit6u5bHERY4z_B2j3ahWGM0XFnPqB4MJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9BcLJDYjDEieQCSTxXMquzIDqkYtckUrxar7W173a42EykiWxHARE_qrATRyE0abowfh7Z4XINWJRi-V8KoLDBp5RH8ynjrOLmZ9BNbeHqMweMXZNV3ge02rXlG4NoO3MrRtzeailSAgyF_9OnFsYFYp-kSvJ6k8I4SwuaAIqk4QSlJq81EhKSCDDnKqSDdIYAibtiW8Z6-zWaMVvQvtlFB4-WtTKsqMo0pAr4Y1GMiBQO9S3UOb1OluoOUKmJOVTJ3OVn7ixcdywynBOPGooQAJa9CuGI6zXQvQWdqqPSwzRCjMwFF6QHct0GVW0suAAFbjazh8Wq6MW07ESZEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1ZHR-5gMaCoxeXF8mklDYviycgsLvLg6YJWQLWd2hVqK-lDdIAb8k9k5l5v0Rl4dPWx88E-79WJR2hzAdULOoFnRfRa1Qvnt5hPddEaTFbYOFzjHs6Rw7mjoPeB5TH9yRfl6ICrl30OzB-thqX4XyRf0xiZXBgi0aNir4_1XpZI1I0JCm8nJfrAi1GaxOD7Af5ovSnjy5NHCLsjztl06mXg6NjuhZaJjyNFzbZZMjQ_36J1ljgTjbcl9MlNfbsQhbhEnrV8wTX2cWpZt5U2xxRQAZPOUJifPjmyINoJfGoTJfPeMbdGTrqwpzeNLSAAtFcxJXEJwc54ulW6-jY4Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=K-iWMRPj7bg7oSWv4HeaXi-JLLD8Lhyrs5gqOpfOjjSOjxUF11SDCrs3JDysQqVRII9-YBgeMILuFFxUQZIvQQBal0vwE7B5vRDkBoXsx_X_GQvCh8VmraVks93Wk8cA7XTpC_Q3W9YJZHJ3FaeadiJ1qfIzlCZzv0Bv3RT03e_e9Z1wKNtRMgYODiCX2BcuJvEh3HcRmIaezOBXNBYMT8tths5t2QsXRZzJ6y_b1Vg9E9-AJphY74O9f_S7Qawxm31xs-riGIaVzYO9B7Qf_IaLFLk2SiRqSphHU14GsgxUCHTwNfKNsH3wXk_ybuFUatxjK66EDKPVAxc7LIptfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=K-iWMRPj7bg7oSWv4HeaXi-JLLD8Lhyrs5gqOpfOjjSOjxUF11SDCrs3JDysQqVRII9-YBgeMILuFFxUQZIvQQBal0vwE7B5vRDkBoXsx_X_GQvCh8VmraVks93Wk8cA7XTpC_Q3W9YJZHJ3FaeadiJ1qfIzlCZzv0Bv3RT03e_e9Z1wKNtRMgYODiCX2BcuJvEh3HcRmIaezOBXNBYMT8tths5t2QsXRZzJ6y_b1Vg9E9-AJphY74O9f_S7Qawxm31xs-riGIaVzYO9B7Qf_IaLFLk2SiRqSphHU14GsgxUCHTwNfKNsH3wXk_ybuFUatxjK66EDKPVAxc7LIptfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltS7sTZEBRP2ZX0jC7L30bS3B-zPIjrgi2Z0fjE9OrdU5ZagIOjEqh5QcSGaP21Y89pbOZHALZ1rUei7ps3omN_r0qB-VBWBeGIGgd9ICnMdoYcKLxFV264ZP8KjtebJQn5CnZYQ9KTgASI-5sqyVcknvcnCMWDqkfEM_Ju7Ld1AT4qBVkfevSsFTW4qh1T272Ulq9ERtfxNTV0SCUB31gA9HLpswWK856RGyA3i_i8RUs_UW_mF2b4eDkPprqdbZEa7fL8jVhOKRj20NmZMfdvCOl2hqEl9kV3YbMEddGLIZ6O_R7k2VOswXFWCj1dgPbxqGT5R2ILW2AwJ_mUhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StNKi_lr58ssQj_t_CCJLlInmck0b8OUIs9spA-ltoikFNBIrCNCit2355W1ew2a6tFFUrvlPDQ9UfEPGFQPJxj5MYmQl0WSNHGVXem80jFol2bQh6yocCexQmSIuTU-ZHPnC8K8SHgnZgEtoDcHJQqtXJCYemI2r0bticY6XEStpG3C6c3fRhdKNM4RXzoi_8AlELBNfbVmEMuZ5-4Lr_Lq-gkmdKa3vho3nhNZWNSH4hpj7S6Zdf1mHyg5VUzjFYl5ulLQv_eQfFizrmpChCc28iTvXBG_FDG0ZFzhysU5pqCTvue6QOe0xrI8VROBDE5e7qGYQX3UHXhAlZFTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9B3XddPyny6cl7Shd8XH1vjG2ZcMaADfSU4OBHs9QSrVnR9ydIjWcbnDda_yxZ96h-5dzHD6ILmU91bLsVSHYojKxUqI8EmJnMyIPZyGO05e9LAk-NRno5RyvL5OPhRUPKhaGBYvFpGbWAbXdWccLCl3ixzVoYzoA7hL4T5DBHuLQFsD8z-3vHSyJO2jyCT4Tqj74q49tYjLs_-7U0g0b6vLwJVgVy0TQL0JY3R4Q1a-ocCAZOvx7ywo-HiiFn-HeXjwAu2f5qKtx8-pK3yW7A_BWlJ3-myjvsFncvqcNhupkYSVisiEiXy3PYsVcD8o6HHnvVP99f-PpiAsr6pQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH_xrRV_DcAfx1kb9MJVexiwvQmgykLNCL19XaPbRc8Dq5AYEU7tFderDi4F08jdm1hTsKVhBCp14Epb2YPGCcxTehR3m9z2IoeURiTTp0-XHWNKU_E2viZrz8UkoodWWhRwXGehD7dFjGoAg66NZTeIsZE6EldsC2r2yenfHcXvCeCgAnc1HezFaO0AECiW26uRe3LHk8WFv-ZEBuUIv0TdbQkiVrVk8Dmg_X7-26c-h1IpEoMBKqL76hvXsGzbOtGRHOc4RQtsJ3tdeCLg1OcSNz-_pm4myF3PvBnGFP4cIP6bi527lX2ttYK_wwgy4wPSbZLNMdKxLcdKSxUqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1g3Fd2oypYZkK2Z3oDQGHjB7ua_d1XddmMq3ARMAA3vwviUZ2xAg2G_jLm1nF53JM8KDtOxo8Wl8BnUBnFu4IqtmV1wf_GXaDjULF5wZuv_iNxYmdanF-rFuDznyHZO7TDCfGp8vSHQzcbRXGs79EtvtlXA431YgaFENwFaRMzaW2rJ1hs_gcLex1J35hSPX1PcRdXOa0JDwJrmpqULd6-B5FdEupzv4rUCDsKLpj7Jn234OPiSTHzFnWuCr04aiDWlmZhHYfKR1gtHNvvyr2z0wEJs48DXiatuOSNXKXMuLenLKsk-ji40Nw2NGowaRtZpdraZYYU1_fBGjrYLtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVjphSL9hkSh3N-c6My3jgVC2A9xgeHwwsPdxlvxrV6sZe8g53d7cJAOQpgl-SScDFd0z3Gw2fx2FkPrPpAZarX__N70YY1QNxml1PKQt2bYJV-BoT22R533K0rljXGtB_k24dhzB_7wjd0sBQf1R9j_8cvhwDaZKV8k89utkAGHqZIBDURYa1S85ooxTADE7r0ob_wj4TWLDscSMMYpXpGUNC-tF5D4JT6px8KLwrpTTw8ZswFoVZgfMWA_WQi46mLfKW2Tyz8GzK2WkD96YeiqwoFkUpWkAItG6dJ7AHygabyBEnFZT2JkDDDVpFO91cpYrugT6mYP0quZ891JMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=NhSv307Hy951b7wkGbHr9XvtPPRdH6Y7FEeP-YoNszCX2R3wlY8ZlxgEY9sr_vdIC6GTQP2_XeliAVNGEsgZZmNUcK06C5idAfOos_t-2EMHVtcTXHs47SSulIKLfZxhybjIN3iKrT9VMBB6A55MzmnNuJ0IZn8d2nJpd1qC7HK8L89NYyjRKR8LuTuEGHP-qhyUTZPevX53zX5gvfbS9MFSOSl427QGlf_SlW_Pjc4nZ7X8u9cHweeRH6wQIa5F3_9BDLrpIp7TPL0a9I9OxxtxXT8bHDfEDH8sEzUC1etrmwGD7LF0ycVbd1DZEOP8d3owpF5vNi46kF1f0TZ7em2YKEu5vpnbkM1DSIm8zs5seyNLnkxC1dnzYCSyt66EMMCrA1bPRooz0DDu4K1qOf-OGC3NzZBFpunWA2WBsddpdPkjgH1VDbrTD9stBNvsvymRqrHHMkwgcTNOXhXx0rnQr_spA7KyY70NDXr3rtxY4A3_2V-wlZP2ef_bJQehjwDxNtkGbE6pSCe6-BsGVDTsH4FoPfdcUK7LO-52V806PYteWvKwqH6k6NGuhJebGIzdLiglUakdqUGs3uJYr_caB6Ln1xgwVbfbGzls792U4KLB0IOFN_fGz0GXdxklWRagVyU7yCI5FmlBFjdP_v2cjSbFpjcGhDbH8Oz55NU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=NhSv307Hy951b7wkGbHr9XvtPPRdH6Y7FEeP-YoNszCX2R3wlY8ZlxgEY9sr_vdIC6GTQP2_XeliAVNGEsgZZmNUcK06C5idAfOos_t-2EMHVtcTXHs47SSulIKLfZxhybjIN3iKrT9VMBB6A55MzmnNuJ0IZn8d2nJpd1qC7HK8L89NYyjRKR8LuTuEGHP-qhyUTZPevX53zX5gvfbS9MFSOSl427QGlf_SlW_Pjc4nZ7X8u9cHweeRH6wQIa5F3_9BDLrpIp7TPL0a9I9OxxtxXT8bHDfEDH8sEzUC1etrmwGD7LF0ycVbd1DZEOP8d3owpF5vNi46kF1f0TZ7em2YKEu5vpnbkM1DSIm8zs5seyNLnkxC1dnzYCSyt66EMMCrA1bPRooz0DDu4K1qOf-OGC3NzZBFpunWA2WBsddpdPkjgH1VDbrTD9stBNvsvymRqrHHMkwgcTNOXhXx0rnQr_spA7KyY70NDXr3rtxY4A3_2V-wlZP2ef_bJQehjwDxNtkGbE6pSCe6-BsGVDTsH4FoPfdcUK7LO-52V806PYteWvKwqH6k6NGuhJebGIzdLiglUakdqUGs3uJYr_caB6Ln1xgwVbfbGzls792U4KLB0IOFN_fGz0GXdxklWRagVyU7yCI5FmlBFjdP_v2cjSbFpjcGhDbH8Oz55NU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-aq73S6LvJksv0Ba6jBWXJgm8ApzXqMrwgCOWGZ4K4ZK7VYU38zs003X2e1NDLLP6-jt8reZHAtBGFlxZGerR7-Gco01nJszowApBHoO2QrZ-t1RlBdvd7MlryuZhQAQPmXmc8g9Q8YN79NdSR8-C3c-UVZ5JnkoO3tiXSPqKoV7WBouh6mA0FkVwtUEx12iWnznNNmgYj5pDHNXAcn_bq4KkqcIqetpm6OwM6TbeExy00-lgCS46PWFLbIVKWyggZ77roHOrp_fE5YMfVPssuI5wlMVvDve6Q_M-6gpYSaGURMJHbHyajdE5wMmuxX8YTygAuIlI8KDzKgtJcOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=AvYJtyD37DOMH9gXTPsOn8U4YDW9PT3aZ2YCzJpYEXhn9m65B0XZOVoa4-kg-_2143kkKl1Ca9PXqZi92Z4JsNUOyBeKliyDjBfgqhpQGumSyYJNUWanWRuxtrzajCL_FP1m1o__rDThQEzbEXn8QjltyvJjkFWzQq22a96GhB17nHfeNXDxTKGH6VXAwaFo-wXzIH5B8rNxtVTI033tuD8tgevHVQWjsf-WGtawDDQqzp6vLwkZRn1HxmNs4Vr7KF06hMv9YWTOnuilPdIeR2dMrJxpO9Qc5va2Uu5V_h6IaUpGQHhUf0aRHqLOuEmIsm-gVfLDSrsAYPfZuVdCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=AvYJtyD37DOMH9gXTPsOn8U4YDW9PT3aZ2YCzJpYEXhn9m65B0XZOVoa4-kg-_2143kkKl1Ca9PXqZi92Z4JsNUOyBeKliyDjBfgqhpQGumSyYJNUWanWRuxtrzajCL_FP1m1o__rDThQEzbEXn8QjltyvJjkFWzQq22a96GhB17nHfeNXDxTKGH6VXAwaFo-wXzIH5B8rNxtVTI033tuD8tgevHVQWjsf-WGtawDDQqzp6vLwkZRn1HxmNs4Vr7KF06hMv9YWTOnuilPdIeR2dMrJxpO9Qc5va2Uu5V_h6IaUpGQHhUf0aRHqLOuEmIsm-gVfLDSrsAYPfZuVdCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8nmKOmsmZXfUe-sOh94nngF-jJBB-5Pylmy54F9d2mlZi4jnnM_U0gDiGk-xK-efl8KZUDK5Qm0dOVR3Q514PusY8mjoZPPHDZBrACSTAa5j8vcDOoQrQVLqqXWYkN7zUSOM-pt-U1ZkfUf_CCoCi2PkVwzJlPnLfIJn5k09buwiRlpFLZrmu4KV75VWUW65DUjBGCI-vZBc2t2HhZv9TVM30itjoDNQE8raewuQx6AWQ_J7WJkZFTQEQGrafFKme0yCatIaGpRh7SV7F3-cFVT9ooStBwFQOCNuj0AD8vIQsXkTdRuoeCt_L4s9dIVyKnCdBgQMTJeGxzmH-M14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRCpz2OVxeFaR_W0lG2_G1TMLslAuP6HMeJf-mHbr_EIvGSnBhRtMqOgF9LhbswKLzeOTsDrz9kxiG-j5Nr-itf92dU2sozwvrHfP2RSYExAOKYiQ81vVyrLE9W_bVo7mbs0rWrub9ULHJ70NMAjuByHm5yASpIlWQf2HErmcnMZKkF7JpJDGGPpX6jbXDEPcwODTpx3z0hBd9-ngS0W6v5tm6mrdVskcegahzKQcDH84JPklJyopp6rRDHM7r61_E6frTZeeG0eW-KrDwExVxCPmoOiXeeVic-eelJecgKInNCaVokuVIMMJkDOjUlQ919D2irjHtZl6epetusGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVHStaALUgTmVi2n4JQvsJ86dNPFeD4lLfyITcUPy9L6GawOajWCw9aMI_J3DHqhBlsoScErXK7h00Q5bY6bsZjmvjRU-Um0KrV3id5iwk_uPpuWJ8KivVOILap6aPL-ebQExRjoyNMtxggotDULygaJ-rI6k2w7uEgjkWTo9n_qOcuaEWwjqGXLjKSKjpN0XENOjTn17cHzkWRm810gWPVadqVe6VnfwctCWcmWRtNVZl1RluebzsVYAEx5YjDlO3XWL_Y3CsH3waLWZjb7x6c2JE-2mDQWjEeN9m80dmcV4iaxsBz_qpawnaqV2pI77i9PbsCUJTbSt45X5Y2j_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1UnNdStfMHmWlaH0wyorUqmQE2A1LVJygZWU7qJA9Xpz-ii6DGkiVVabKzq_iPNH9KD3Ny58cuSxbflo3u1M2WiYeCPpzO0QlnBWta3QpGeiBos-oWk5UeShECrHNej8SLbtUnRIDEcEoUXv84-6zW9UBnvv9Nu1GvTzQbC68AmKHWjnngk3C6xeNTpp7TpQKlw6mUMTgdB87LZPb0egCk7fpyzDSdoXKar_qH0AqJLkLWEIsa-FhJ6T2ZhxLcvPWTfohM63QgzsFO_jt7BGkbwK5ta81Liglf6uzwIDG9vePPHxNPQ7X8x53FlHtTb7_Qsna7GqLrMr43tfej7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKRA_QlrzYl29vAqG9oLHmxUW3YsUZIwfQuWrc_yKsJt3_YyMlvVZGPq4BihieNN49HHI6k3xMXrsJkJZRyxSzT_dDjLB-iCUnMURWUpqNs3LsjvLpvduPqOsB_UTlxRje4UeUVDLKNNV_00B5uJcRzmQDJ5b5Tx61tlt4fSh2mH8Bc8oJfXKRAUNB81_YVB1PK94mvRAND6sZuYis41k_rYZBxPIfAYawNStj3RrPZRIl9MNOKlroYOl1H4EXGZGkAXBwSa-wIxRrIGeGGj5LFTE9d_8XVtju_S3xhb1urtU9wlVWOkFoce28qPXciJNrC13WBw7tX1uIMPkkzQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4YziYpvrCnwFIHRw8OKHHet_TBakyN6-WcBQnTsIP2No3EKegAuB491Zru9-1159qt1xj3QNRGOP5nHSpQbPfVrS3b7hFFEhY0Uix8a9wUxcf1UjHc16IZHJLJGDZQea4NIkRGX2-8b0BicE6o4xPthQoK1uWPI0ppRhD_20lwsU_Zzm-Qwcg4TPechNv2rkFY3yqQ-7-fi_kvaBE9WAzAQoU0Ps7I-EVd3yxY2escFHjMTVe3Lo8JrNrYbqKJbn0C1EATglbXIShhSFeboILw2dPBtdVl6Lj_UR5UunW975v_4k8YZexoVVSqmNNfu9I9Rv56jwuevv3wwceWzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=O2rnsbsHgTXtR0w-UILTQ7ZPukY7FycM_GnpYrXG1csd_bz36ZZ8DZBhuQtuOnrUQaFPehMffVOiLz-VYs1tATCgd3Dige3IjKVYypALOhMdnK5XvV3JqbTQPiDWAIs5iK4tsgQJVevQJp2xoyQhjMlRfiPgGpjXZ_iVKpGoiIeGATfW6l1fuol8mRL-2RjUkJ3h908wYzHQ7hzdYtS0906YwRsQb4-jvRxigKoDqAom32yksd_rKAxrTU5ZxQCkBFnvQWSyVTofZqVHUMlbJYukfRL6a1ND0rbVYLy11u93gUYhYJhsYmYYwHX4h5duoHVqWRgHIGpn-fYfqpjvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=O2rnsbsHgTXtR0w-UILTQ7ZPukY7FycM_GnpYrXG1csd_bz36ZZ8DZBhuQtuOnrUQaFPehMffVOiLz-VYs1tATCgd3Dige3IjKVYypALOhMdnK5XvV3JqbTQPiDWAIs5iK4tsgQJVevQJp2xoyQhjMlRfiPgGpjXZ_iVKpGoiIeGATfW6l1fuol8mRL-2RjUkJ3h908wYzHQ7hzdYtS0906YwRsQb4-jvRxigKoDqAom32yksd_rKAxrTU5ZxQCkBFnvQWSyVTofZqVHUMlbJYukfRL6a1ND0rbVYLy11u93gUYhYJhsYmYYwHX4h5duoHVqWRgHIGpn-fYfqpjvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24591">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXYCwj7bHu6G4szPc7y-1CYtv2W_r3ltDeqLutwYimim6RsP0EHs5cNYhGgYRkoJ0alhSF4vsqa4tT6OKr6fFrwmKZUzCWVkCULafWhkP2E86WEsAkbwmYoLIXoVrgRLne7n7EmtrVCs04OknEoOvIzmSzIQe6Dd8e5_eKk9YEOmJBijnRUzXZxdYdtn8L3WMO82J-3Pdbn3MRmcuTbMPl9RzulyeUv73ftwsD7lmlJN2wLIA4_397gh4NAVTirmWcGG3627IE7OoBgzTcOgkwa7uH5_E3KZBZl2YY8Yoz77p8D02XpmXWIfqo8rlV64m-ZROGSJSzDTJ0lD5tUTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r8
@betinjabet</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24591" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_scAyQoWpo3hXe8oQszGCCgvUiS_KeFyu8AOYhCVqKlqWmvyUIiUpWDTHEVU5kL95aqpqeHApo4h3HZqlxA8eXqcMfrZO7HmMdMMhagRXXAcsEwoUWu4emfqk4RwnVzjSHtbhyZsY4nkpd3GJYuni56moc7njHZiBOEbCF3lH87uJWUZ4ZOXHK1trdpmo8feHHqDu0tmlZ-30AY1H1H8Y5dsi9nhjEQnhorGU1lvcV2C5vHrFVB5jamJv1xcgh0JkMbupK08_xh3GgHdEn7y6Nx2qt1cYAnIXpcgVVwZLVIGxfLbjU1FyS0l0Db-YlJCz6btelwmmN0q6Dj-qsdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HErctmAGXINgy85PYOUWD0T1icO3t0I2mVfLawyRevz2VkDA_yAp9gNi3XXDKf162Upwvle5aOUgESL3PrIhxfSwGFhVAXIdvkG1VFB8gMPtK0bOfNvegCcT-r0Qlh06N-UNOwaCMHu130i1U_bCpQFoDlD5Q8skbBNW-Tmc2s_o5ccXs4KI_q7OLlGOT5tlF8P0p9Z2fWyF8WgpahoAl9w_QWg6OiE9GQqSdhZR72g6mEb10cVK15JvG4tEWHQqcxyCpopc2RcUaRvw5DUy3uaZjyynKg9b7nbU5ifCw3yp9yT-o1QS3A6tXE2pRyLz2jYd0fh_XgQ5pttSPkdVrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=Z51QMwsWVtYZd5Vud1SiSzilivoRwVV-ASJdGztAEWmLmZrUguiV4r-HTH1doRJUOtkgL3pWkQbbHyOVxPFtCULNZwyAUfFIgvD-97CmT-Q5FHwB6ww1Nhr0--zMHNujOsKQBB1Gj5XzDLJuhEJvAXJJ3QJMM5tGA7P5nXErctWZm8VLYjf9-wGEvVr9ICIMW8wccQBexVWrsPKW3HQ68zaQ5-IsLdbC53a1HmzFIjoU4JHzzIT5lyTO3JLj65iXiqXj0Zqd-WMIRdlc1fTEk-4iJ5QebN4YtHEHmNrllI8V6dWSY2be2QzvjhKvupAzJL_j14KLEBIHZz4hOPYrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=Z51QMwsWVtYZd5Vud1SiSzilivoRwVV-ASJdGztAEWmLmZrUguiV4r-HTH1doRJUOtkgL3pWkQbbHyOVxPFtCULNZwyAUfFIgvD-97CmT-Q5FHwB6ww1Nhr0--zMHNujOsKQBB1Gj5XzDLJuhEJvAXJJ3QJMM5tGA7P5nXErctWZm8VLYjf9-wGEvVr9ICIMW8wccQBexVWrsPKW3HQ68zaQ5-IsLdbC53a1HmzFIjoU4JHzzIT5lyTO3JLj65iXiqXj0Zqd-WMIRdlc1fTEk-4iJ5QebN4YtHEHmNrllI8V6dWSY2be2QzvjhKvupAzJL_j14KLEBIHZz4hOPYrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=rT7TnvEU9mB734NwCZhOUizl65WXk_0mESQKm0B0wKoVfDAqU8kspe29iOEYVOOUoJi7ga59xG00FJULdlcD4YBNZax4H_XnGcQzxm-dCacGg2C6FmwMvIs5Hv5rTbt8riM9mTRUdypKtnh8ldnqhwNvFiD7A9jFAORKba-jxznB1s6Y6io7hfIGlM0cLNoUSy_A23trl86NWKuy-_1FBCTwJORGp_GxILdIeQ0AG2VAkB_uKIRXa2IoNy5oEX5SvJRtTWYR59jsueM513HBcmaBuJzRXPmET_0aCgSMzCkzSHxhd2pYpcgKBt-epGQEmFOXrQDaPZCm-8mSplRioDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=rT7TnvEU9mB734NwCZhOUizl65WXk_0mESQKm0B0wKoVfDAqU8kspe29iOEYVOOUoJi7ga59xG00FJULdlcD4YBNZax4H_XnGcQzxm-dCacGg2C6FmwMvIs5Hv5rTbt8riM9mTRUdypKtnh8ldnqhwNvFiD7A9jFAORKba-jxznB1s6Y6io7hfIGlM0cLNoUSy_A23trl86NWKuy-_1FBCTwJORGp_GxILdIeQ0AG2VAkB_uKIRXa2IoNy5oEX5SvJRtTWYR59jsueM513HBcmaBuJzRXPmET_0aCgSMzCkzSHxhd2pYpcgKBt-epGQEmFOXrQDaPZCm-8mSplRioDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=N1q6UMyZ0r0999gLh5Do2XumDRmyZgjGe9icufFBPJ-J94S_BbkQ6E5d2cpxbgTwOTOPP_zwB7l7-lKWSFrJoaT0ArUakPrhIX7EblP0ti_fuj7qRzKdJFkUJ4l1nRN3Eet3T2Bmf5hY6nQXmXM0hA0X40vkBoLWs-ol9UWOFaSLwTavHcEsZXFXBaIadOA1R4gKCheYtDPGIUHhMHXslamVvexsOHn55VD7x1Ole6JqPiuXbYXVs5pVXv-ukoX9r0hd56CNp29VLxm_FPc9INjSza5LBowzo3Evsts1pytDykQ6RYhjnG8EyIUmb4MDO9F36IaJMPKLfJtDmbJEHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=N1q6UMyZ0r0999gLh5Do2XumDRmyZgjGe9icufFBPJ-J94S_BbkQ6E5d2cpxbgTwOTOPP_zwB7l7-lKWSFrJoaT0ArUakPrhIX7EblP0ti_fuj7qRzKdJFkUJ4l1nRN3Eet3T2Bmf5hY6nQXmXM0hA0X40vkBoLWs-ol9UWOFaSLwTavHcEsZXFXBaIadOA1R4gKCheYtDPGIUHhMHXslamVvexsOHn55VD7x1Ole6JqPiuXbYXVs5pVXv-ukoX9r0hd56CNp29VLxm_FPc9INjSza5LBowzo3Evsts1pytDykQ6RYhjnG8EyIUmb4MDO9F36IaJMPKLfJtDmbJEHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi5fRU7AfVkRY5hJ1auyVKNzGnP0kccls8-PFg7rVSVR_qP9DvgQqK1Mim3R7QT6bN-_tOiR3KCIQaZ-k7seKIJXfYXl_qxIyqgHiq71CNfcwAD9gRpwgMMRvYNF65BaQzjhjG5Z-83FG1s536iSW3pA2JTzdcXNCzw5NbLK_RpDwF5Qy4mgj90R8lVPgTmj3SsQ4A-dEG5R8ykZWColTBVBOiblvs7uENrJbi3Uhx674QkVujZ10VhkYD9q3lZITRjqAnutRK9sHM5v1Gpzh6fnFHRIMwRgli0fXPzncRZ9pXMGkuEDaOZaemhXmJOP-b03Q9e3N_DmzLP88MgQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7dpqKVvSc3fb_D9fWmWAlQyeWKdcFLRRtnwF8D_AONda0uZ-0giKYGE9HYLiFr0pwIb8RCrlqzS7ark9fpMvVvPT4jo0paDXQ-mntDwK-P4_oIyW04BttDZh1LEz0ul_TOMXHJ4oKezjhr-Z4xCsrsoTpnumpUGxfZ2Q5QzABmwn0ytIPAkzccPHsZcawhA1_iGQzVBha14zwNuRxpWdYf2__3d_zg_9RZLo6eQzfBE4JLmz9pv2Nxmn4eb9j_2BKp29VtuqqSwvvmFrm23fn3onjlbi-xRStJ7nKso-D7L-lId2ec7iptkSQNzzC8mRuGuPUwqRsWi4vfzZQbxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdv07CsGVc4gQW6Bl74qZ_tWRKnavcHyp27LEF8LyRHRG4wnkf2eJOvsnUxBDRb-0xhXUDI_qS7SI7TZGs11gUZWI1-FkxQgVSsV6k-PhL2tQBN343b5yZ3obrA5e0FBAjXWIBa_gOuE97VUyAr2qs2PgQDuHz82frRCshl7p70Tg8vqf3EYNxb4t6pFIGMsgqGSqAzNiU68tRS9D74pAHaeMg55RnNSDRz8cJBMNIZ6wlY0pgSdjhA-H6nr2Pr-SdUXjlZcNaAS1ymi5-s-3ARPDEqi2FcNaY2ztM2ntbOkt5W5eDL0fbtVycApFg5CP7EtHFaJEMYPUkglDqVY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPMcExbxY7nabPMUxNI6BZKdT1aFvMVCcnZFmWnhzIK7ujaiG2hvP6oeV4t0H2V-4BYleTIEaVoFFPdpW53YZQ7C-tEOgCfH8rPCeZJ5eZbmq01BkBfgKl7-tBYiXWFgc6n23AwnKsXx4LsUt2VsUZ9OPt71pRIhZWVRs_7kv70drM8_xbnWhwFugunWe38t3y8aQ39mRETMOPZ737Ks_LmB22m9vCAARVWNsiDAzftAhb9D67u1nFIIKOAS2Ko50FblhCa9G2TUAWJU1qticBKKPfwcPefPfdlDWy_VRwFWAMNXw7vbZPwzvb2OoBbRTB48ieAJ2A0d9dO4jMFSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPMvz5IggeqZEsqS_t_fg24pbPZ0BRC0D8tyRdD7TI5jNoKrx3cnavtBXUSKpObPKdymxv5MSaTMI9tNIq3oT6vkTYlxhgdHvmZ-wGgxYjXWQiMfKanS-mryEOTi008pKPNaT4gnsCqtOMxjfj9LS6SuzhIJVihOtORePED1drz1TETxs8NmqALf9hz11rcUmIN4LhYjTZrHEMaIrAnZPqZY7eZK09xibc_EhWyoSRaxEvgi8VgUTQbdriXr8MvxYTj7_LTYcYV8rT_nrGS6QAgz4tHevBwAm5XFtyQTttgY789koYIraWntHCv35HkhQ8aycoSpB_lMK_ZCf62RqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7uSiBwjSk0yI_f7ogDxA9Xz5P494OqLbIrm1QalEGzn62zrpR3WHLCyznQyDfGaAfnPkYeD2QSZI8SshtY1m7ZexfeM19o_APcvu-xdlIEm5TtXzy-1CPE01GcnzT25bfIFBnzRem5mabm6uRfYzqb3tf50QhEnpMYSg7nIx9EdUxb7SSjo9RY1oy0YacnyXo3ycJSWXOODeF5xs7xI4FDGi39pEcRfTnKjS7WTz9GDQKhCrvtlEU1ngZfQdQa9eAoYXrE2rhldYTpJF6pzyxIWk27TycJAvhYk0iz83Ko7MKhv2p5e_ZJHUuIevMXuJbYbJFvVBz8sr1EJtMsRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIxWmVlUuaENM1Z0bkneV1AY-PlAPNptzIbrsz2PmVIWF_NRZHebUcm-DDyUPgAf1BQjMCPpeoCTzp5OQm7tme6cvre91_vtRswrOVayklqfptdpQ5KXjkVwFfINl8N4Wslu3rCnZQtcMF_QlofwO7WNg42VoRePlddWyd6xIxx4ABjNITxSvlwfnNwup7mzti5GtZqkw2W7t7yBttmDHSJiXKwfGK82Z8tFl-JHp637fXcJ63UZN0M1eR-QRd9HmG3gbSZekviHHvLskgRXBCN7A_lh36Lj5DUyDtVnE1Ei-QKq-yJQz3kNxYgTrQ9Tf2SsJ9cahdnam6dSpHCkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=L3z_4EbB14CAMd5QigNINZICSOJFxzCmwP9ojFsaeG9RAAsfzSxe-nS_epU3GPphPvYWY8cxO16EYOcDTnJydFU8bOZHcdmLfeHrFqJwecdo55afHgb6cUXilVY32HEFItztjSal7TufoAKpYd2ilp0RDvKGp9RAvGWvQoGHDkxvjpCG285OL_9pI0yVG-zlNxxkrkPcw6mlWdWf4dw-7eTH3in8EyEc-FijtMTlrURFhQWzLE6z2PHYpmj1MOOVwMMWTvT9cwAdm-J7RzYRwGCQmrQ121mtcwTPwKmsn34132YDp0l3MqU5N5pSAJromrC8Unp07X-7UU1N96IxyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=L3z_4EbB14CAMd5QigNINZICSOJFxzCmwP9ojFsaeG9RAAsfzSxe-nS_epU3GPphPvYWY8cxO16EYOcDTnJydFU8bOZHcdmLfeHrFqJwecdo55afHgb6cUXilVY32HEFItztjSal7TufoAKpYd2ilp0RDvKGp9RAvGWvQoGHDkxvjpCG285OL_9pI0yVG-zlNxxkrkPcw6mlWdWf4dw-7eTH3in8EyEc-FijtMTlrURFhQWzLE6z2PHYpmj1MOOVwMMWTvT9cwAdm-J7RzYRwGCQmrQ121mtcwTPwKmsn34132YDp0l3MqU5N5pSAJromrC8Unp07X-7UU1N96IxyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBr0hkVyMmwaxc7ILPQjIEPGmiYVwGdagSz7HzDVIb76BbmCUP8ygd7eKsJ730NsdCq2UhjAi-0RagvwjqAufbPOXa-xPto6ES4QqQV_OPpTdaKuFWsFvrufeu4eYpjseLns_170hhR5FhxcbbF3BHQJfTKk3JnzqGMBVG2vJ58KUSaFZO0RBmjMRglcebQCkzr0leSTyq54EgjrfCuhqRgqFJK_wJvCauPZ3j-YSkKqMpOSJh-TiRHfn4-J25CBd4GNLs_32gNd61uI52EwHFO2gUmLU40wAvLdTKgypu_7bL0pecuoZ0SvXI1NLksUafDSE0_U9OLOgP2SPCyexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV5LxfsOegvbLtJZCzfpsAEY85S-u4tSqS10_xKT17bmYNpLZdJUvUNU1Vy5C8XyJI7fOvYQXWHvORZ249koi3u5cZRxUQh9NsslM4z-N_lQ-7mpE1VW967Mm2-e4Kh7ToHpBhbEDfUgsrBBGT9idYlly00_y4P9Y2Uelgzy7J7M1qKkLlX-M0zDk9EgVxa3gG_joWKJU80-vxnW7zOScFIWDGd-NBHmlTIMWm6JcvNNvT5_mJvifKXKwHJrN20ONIBq5VHEmu8YHedKtzEJlAVPqbTkn58tRB7i68sjNzmhl_fu_H-opBG9yiUx7POuA4acx0dRrL2e66JXlolgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=hmmZCsBd4edfb4EZfjFaFvWHXrhe7m52boG5ByqUvRuC9AyH3FNjj8tU24Nz8yX7cAg1e9yDYElQKRR7DU5-ziAUKCU308xqfN-WlVbHrq60876Jd-3UZRgdWvCDopErnrfvKj8bwN08FNrSTDJCjmpOxtRmhr5qErYfpSd8dJkdJ7rUb8smRfHyadXU9kUAynywLxD0NtzsaqftjqiFyjELbVHs-0YClYobeUCk9QAxf0XPz-DSH9iIrwpIpg2GVa39GgWeyVDFiZVMPWbbRTbPXffozAUMrHBYYsdDdnyvaWxUD7e1_9x-Ix1XsvjEZClPSHSdimF174A9LGPAGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=hmmZCsBd4edfb4EZfjFaFvWHXrhe7m52boG5ByqUvRuC9AyH3FNjj8tU24Nz8yX7cAg1e9yDYElQKRR7DU5-ziAUKCU308xqfN-WlVbHrq60876Jd-3UZRgdWvCDopErnrfvKj8bwN08FNrSTDJCjmpOxtRmhr5qErYfpSd8dJkdJ7rUb8smRfHyadXU9kUAynywLxD0NtzsaqftjqiFyjELbVHs-0YClYobeUCk9QAxf0XPz-DSH9iIrwpIpg2GVa39GgWeyVDFiZVMPWbbRTbPXffozAUMrHBYYsdDdnyvaWxUD7e1_9x-Ix1XsvjEZClPSHSdimF174A9LGPAGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب ابوطالب حسینی درباره حذف شاگردان امیر قلعه نویی از جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=sAMGpx5fa5MHmJ5RUtaIR2vyshkZ3IZHYk6net-oYT9BeSwyW4qH3Eqa3MZWITzqtjF_U_XVUN_xgHkP9OLfV8cdwn856PkGpfF7V0eYNV2IWcB0vd2Gg96oYQ5sDd49_x3ghBnr50NSjIyOKUq1lCghUYhYsA16Kem8Igqzs-k1CqsHpbdBF3sqnWojoliYkPec9dVVujJ-yO5xFQ65chCsHD3y12uh6cHGV1SkSSDtw_B8ScVDIsc9Fi85GT_tpm-hOW_oH_7sXg0rc3mn6gpI1RJkNRhs49l9HKidCs1HGkJCuhq9vjcAdfqtGhPtkBFoIJ7bnkAX4pRiDeqSoiXfId0wEO8Z89Mdh8OHFE7YJqHHwxg-V75el92NQcH4SYb9apfs7I7jGmXK13YRRsQEuFLKkY8Ep8bBHqnw4_DcqUnMR6YIy5Ohvg3VgmJ1HqZrFvGhJHpgPnSEW3f1sg8zrwaI7CPw4MA0I-th25Nne6Igoqe2pJG-8nyxEIqYs3paxnnZmMW9-gTWLaYYg3CSJVSv1o-SB3S6R9CY0lyB9uGJnt3EFFbNrfnabJGUvgiUmSLIrVLwQUzSl0wYQEr2TVscMW4HPq5byik7Gn-WNl3SBRrNyBaZv1DrqhtdyEGHEsOk5xQ6UPty_trfWgp8RMTul_UNxunuSutcZyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=sAMGpx5fa5MHmJ5RUtaIR2vyshkZ3IZHYk6net-oYT9BeSwyW4qH3Eqa3MZWITzqtjF_U_XVUN_xgHkP9OLfV8cdwn856PkGpfF7V0eYNV2IWcB0vd2Gg96oYQ5sDd49_x3ghBnr50NSjIyOKUq1lCghUYhYsA16Kem8Igqzs-k1CqsHpbdBF3sqnWojoliYkPec9dVVujJ-yO5xFQ65chCsHD3y12uh6cHGV1SkSSDtw_B8ScVDIsc9Fi85GT_tpm-hOW_oH_7sXg0rc3mn6gpI1RJkNRhs49l9HKidCs1HGkJCuhq9vjcAdfqtGhPtkBFoIJ7bnkAX4pRiDeqSoiXfId0wEO8Z89Mdh8OHFE7YJqHHwxg-V75el92NQcH4SYb9apfs7I7jGmXK13YRRsQEuFLKkY8Ep8bBHqnw4_DcqUnMR6YIy5Ohvg3VgmJ1HqZrFvGhJHpgPnSEW3f1sg8zrwaI7CPw4MA0I-th25Nne6Igoqe2pJG-8nyxEIqYs3paxnnZmMW9-gTWLaYYg3CSJVSv1o-SB3S6R9CY0lyB9uGJnt3EFFbNrfnabJGUvgiUmSLIrVLwQUzSl0wYQEr2TVscMW4HPq5byik7Gn-WNl3SBRrNyBaZv1DrqhtdyEGHEsOk5xQ6UPty_trfWgp8RMTul_UNxunuSutcZyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPJh7nkqfEG3isW8-THu06xj9cjcbi-2MV0FuCaX6ZQARyA-OfXmLWsplZPfbonX-1rg9kzEPpWu7Rto_q30sO0r3mDHPEbx-02M9BKpl0IY8CrU-NikuVb9rCQcmxTA4ZArbU_jqNeHNSmiPQYdc-rEJ9GwuSxbZidPe5MIpPu7LIflyx1hpoRNNxlEcTkWeWn7Lg0Mz8QaT0yk-di7iJO-PeI4IIleUxKIg6iF-GjiF91stYInYxsrOMe46BkLAs3mpBX5q5NBtaOpKX6hRJTIy9uSscqnUPHl6k7-UknkyWAF7qfPo538s0AfUBwQZbhldEtoXlRbsyjwxPlJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=sFZ-CIBluoCz-VwEhiWZVkF2rThQl_mUfPyrCzxXkf6Nx5M8p5nn4JLhGtLFdWg7Sz4EOqeMUcYQjOYNJXDw-WL86yuY6UY4Uok3JYE-mHNdjxOomD7LNeDyN9rVFLd9vTC29WBRWqYMGMprazG-gikFGUHvhuV4PxV1DQmz3-D9rYG5sL_-JcIDE0aF-0FMOn4eIxsRuqjQN5UrXzK-KdDKVpnTJeQPbvm6iHLPQKJnAxD9zN5w7u16caToYkZnp2TB-pyCSZlTggh9NCx5LFQhmdUKepgJ8ioXGt3HNrvJVu4PJCr4vtpjkMrUpn9qOGIb6v5fA9mYV5qTf2IXMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=sFZ-CIBluoCz-VwEhiWZVkF2rThQl_mUfPyrCzxXkf6Nx5M8p5nn4JLhGtLFdWg7Sz4EOqeMUcYQjOYNJXDw-WL86yuY6UY4Uok3JYE-mHNdjxOomD7LNeDyN9rVFLd9vTC29WBRWqYMGMprazG-gikFGUHvhuV4PxV1DQmz3-D9rYG5sL_-JcIDE0aF-0FMOn4eIxsRuqjQN5UrXzK-KdDKVpnTJeQPbvm6iHLPQKJnAxD9zN5w7u16caToYkZnp2TB-pyCSZlTggh9NCx5LFQhmdUKepgJ8ioXGt3HNrvJVu4PJCr4vtpjkMrUpn9qOGIb6v5fA9mYV5qTf2IXMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcJNe-1TUEdN3uqFZe8waXAznd3mxjgrqQ8_3clj7DR4fxj8sKCeh_YOOmiWw-sc4rRDemiGfTcwEZdk5-e9DNpzqEvSuy6i1E6gsfK8Zp8HBkUBP2ArqiddaXm9ulJbIM6f8BvURn5ii3_SpqiIDSGkcWabHZ2IK42QncLd3_42xVqCTDp-hrEhDFc5Q9GGGYY6O17ua0F2P91isOa2YHOmQ3AoE9ATzxqH4ZDLhbSKf7Q9gsSmLoBwg2EXwyE77nUmMd-OS19XsWGQYsExLQhxPGQEm-88n7vgAmfcsn8mQTwBsEHzAYFNWXDZ181qCC9Bct0UmpKeReomhdFD0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=U8oea618scFFreQ5VRvMmbP8LPOO6qRRu9nkchDY-Ovugvhc_eu0cw4kmOeBvq1MEyLOy9bHrK89euo3DpYIZ6_cLbOrCee2Ej9FfMhWZptW_vQb2m7R7SBslnYHSdpVPAgH_wdsc0Lr73b_hqWrLfl3uhr_0-cpy_d1sZclHO_Yy2xHdiJ3jS8WSAdwLU4MBuNBYG_9HRYfbOiast9dzagM85A9ZnCxOrRuk7NvnMqOeW0Hx9VxDtb6JgSy7O5UpeoNqzQZi4tinP7imYluh-cInLVsr9eTh6NfMTCbdAnQMvilMBAZ_Dra_ogkXcdgfGQfwWHbJWQfI2r0HIkVwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=U8oea618scFFreQ5VRvMmbP8LPOO6qRRu9nkchDY-Ovugvhc_eu0cw4kmOeBvq1MEyLOy9bHrK89euo3DpYIZ6_cLbOrCee2Ej9FfMhWZptW_vQb2m7R7SBslnYHSdpVPAgH_wdsc0Lr73b_hqWrLfl3uhr_0-cpy_d1sZclHO_Yy2xHdiJ3jS8WSAdwLU4MBuNBYG_9HRYfbOiast9dzagM85A9ZnCxOrRuk7NvnMqOeW0Hx9VxDtb6JgSy7O5UpeoNqzQZi4tinP7imYluh-cInLVsr9eTh6NfMTCbdAnQMvilMBAZ_Dra_ogkXcdgfGQfwWHbJWQfI2r0HIkVwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=fS--ZoKCsGwRYKrg67Z7VyGKd9lgqh4Neb92OEaYUt2u2qDbEYvwY9v38R7b-9jgK8R4yZu45tWjWEa5I2Bomix2dIoiiVy1s1-pC0-s4A3vudCEPGDEmMrhSY8Hz2EsLYsQOfJv89uqTV20goowkwIFpH24RsHaPdQ_qU78zWirENPvC5d08jJw3BxIC7dsxIb51EdRuA34MA5QBBeHVf2Y14Y3_729vYNgOzhIveLeDkwN8N9CyOuNormrvKVr1OquTI2AeetUoSJC_Wy0ypJMYVCgnnvo72A3hJG3QVzWm2uY439G6PkDEsv8cnP2XzuaoVWY7QDv58S1Tv0_EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=fS--ZoKCsGwRYKrg67Z7VyGKd9lgqh4Neb92OEaYUt2u2qDbEYvwY9v38R7b-9jgK8R4yZu45tWjWEa5I2Bomix2dIoiiVy1s1-pC0-s4A3vudCEPGDEmMrhSY8Hz2EsLYsQOfJv89uqTV20goowkwIFpH24RsHaPdQ_qU78zWirENPvC5d08jJw3BxIC7dsxIb51EdRuA34MA5QBBeHVf2Y14Y3_729vYNgOzhIveLeDkwN8N9CyOuNormrvKVr1OquTI2AeetUoSJC_Wy0ypJMYVCgnnvo72A3hJG3QVzWm2uY439G6PkDEsv8cnP2XzuaoVWY7QDv58S1Tv0_EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=bQjzaZLVreOS6Pv6zczjwE3XMTgLiH2dyHcNh9uf1DyrMyJaIGdby81U_FRvTFLe5jnE9odhnKVB9-dyicRjonQrO6GvuYwJB8NewWRLRfz7iYuFJay5AjZUF2ZjBbEhgrXX4UtlNAo7TXmcIKO1MfweoLFxw2asOi91lgqj9YPLe88mgxDWQT5sGfyrh2V2a-xL8A6B33COz0sWdwrxxKlnP-b3YaVwzCCtWtbP_D_vytAlZ_MzwacJn0sJsgaWdDps1poJj8JcrF019P6YXsCvc82x5bBSDWg0E3XI6HrD_tH3McZCL95D7w_Nio4RC5koJ03MtoH2B20sNqPulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=bQjzaZLVreOS6Pv6zczjwE3XMTgLiH2dyHcNh9uf1DyrMyJaIGdby81U_FRvTFLe5jnE9odhnKVB9-dyicRjonQrO6GvuYwJB8NewWRLRfz7iYuFJay5AjZUF2ZjBbEhgrXX4UtlNAo7TXmcIKO1MfweoLFxw2asOi91lgqj9YPLe88mgxDWQT5sGfyrh2V2a-xL8A6B33COz0sWdwrxxKlnP-b3YaVwzCCtWtbP_D_vytAlZ_MzwacJn0sJsgaWdDps1poJj8JcrF019P6YXsCvc82x5bBSDWg0E3XI6HrD_tH3McZCL95D7w_Nio4RC5koJ03MtoH2B20sNqPulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌ های تامل برانگیز آیسان اسلامی درباره باخت شاگردان امیرقلعه‌نویی از جام جهانی 2026
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=RzxPG_u3d4L9LcWk80XTJ853KD_WxsHjtq2QEHxpwPwnbTI8IEMcOZENNvkPkWacQ2RcMrqkFE_Fkph0WlkVUlXm5aGQYnPk9TK3XZ7964790Wowue7926v8wKPCqoEQdnRXGhejCxJQQDB_IP1xFs2jnHFutTiObSZYFXNNeqjcMi-Gjugc_I9osH5qy7KGl79QTWyOchXMQmG0KSQjqBqcFVrchxudXaxJOdi8OYvMZbaUx8YbNfTwjfcEuT7Gy_CGbQSLS9KMugprWZ_gMmWptj7dJOVtMigeY7IJGflaWNld3ytodt58DguwrKm4YLqfmFWjZBcULcbLYBBwtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=RzxPG_u3d4L9LcWk80XTJ853KD_WxsHjtq2QEHxpwPwnbTI8IEMcOZENNvkPkWacQ2RcMrqkFE_Fkph0WlkVUlXm5aGQYnPk9TK3XZ7964790Wowue7926v8wKPCqoEQdnRXGhejCxJQQDB_IP1xFs2jnHFutTiObSZYFXNNeqjcMi-Gjugc_I9osH5qy7KGl79QTWyOchXMQmG0KSQjqBqcFVrchxudXaxJOdi8OYvMZbaUx8YbNfTwjfcEuT7Gy_CGbQSLS9KMugprWZ_gMmWptj7dJOVtMigeY7IJGflaWNld3ytodt58DguwrKm4YLqfmFWjZBcULcbLYBBwtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یادی کنیم از این ناگفته های عادل فردوسی پور بعد از تعطیلی برنامه دوست داشتنی و محبوب نود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1Mfjsjy0xvsWmqSvZWrE87s8qOJBwWYPGNpR6485FsxukPR4LjjKasMCLJkKy6DaoRXeW7aU7-j-EFhkWEpC_U1s5vto9IuSKsCy2oxH2PIqVTd4EXftJjxVosyCXVc8tiDoQuFBy7bTBQIbQhJ4cHl7DP-VTgMz9QrH9metluR3oHZf9RLGFnEQpS3i7mLh1uJv1-C0vjYsM_PZRExr97c4EzcNQyX9s7C-pmI71DPflZIuUNuu4bvtZbKGju09Lp9FpECIHbvSi8QGTU5PWZjgSPes0Dz7ZH8kohRw7E6VG_ZIWm795tJKS1fmNXzgbzJ0_Ogp0gpdBE9p4dVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD9Kc-WsGiYbxkfWRRgkKMJlvfM_bZ1xGKNjzGPL_JFaUR91licjXST6qXgz2L9KTiOsVZXTTRrXtfO2JeCHDbLsvTtpcg8QnHaJQQE_FBIA-p1iXhwrGT-dG7ylifntBxdvxbXQnWrGMJJFOJo7KxyO4ijoqKik6HlA8LvhKqhw1YIhMB9kwenSQNaTtDcdVW6hs6_7IeK9gTpZH200xJZ3ufC0zNY56wU6n5ZLV_QQkMJ3SGLGLX-Beh-eCuOmWZ-sdiPYssykyosLpLAV3g7PJf8NU6xanqofTSnWHpnT_qleLaYZXm-CZxjhgXnDWryeIiG-N0_GD51XyDXu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-lMUqkyOXERclw5ZEGcBAYsxacYNu9oHk88FI_aYCPT596mpT7v7NWm1V_xsClFKgKehKb9ASE9vplqZ78Ujvkth4A1qbnb-ifNDyKiDeWBwz4yXg8YRTyAEUA_N4P2DyHucsNRvVDol19ZcNKJhjG69ff7BJ8PGTZ9cnj31mdOHMfxOvw6MuLLY2xfUcEq03pRTCo6kyXcWYWDWrcybvDGuP_yKH2wuXu8j5G4O8HGYDfWANATyEFekMAe0aDRjydoXii0Kw6W6ykYo205Ha8jTb8Hpi-6OQeye39XJ5bTcWYoJyzXpPMTkAzfvpsehJkHJZqEI8eibkww2w-g1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0l1nc7EspagIoyAB0xikcV_QBKWm0uVXKiPlj6VOgdCnXJA1v1thVQfc3OMKo_uRUgXs2XnKufIEVLwSKjxQHrktBd2fUWlR-VJ4ruka5uv7B4iQokFCp-Pgkn2M0yvatApKNneD-CwLdcy8NEuvTDp6fUfgtAUZc2hqnR-f3NApT-BeIDehzV8Zlyzd6GHjwSY4_r9t1KB7V7xyNJte91Nj2bmLPTDE0arllnJpg5Gdicr8mFf0bFqaqY2h2KT1jVmwzcwW2CAh0C52t_ybk57Jy81W5YUDijfSeb9eafhS-LwzcRcpt1bwzCMuQUg099hdJ6zFA5XZkOEpETsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=rDDfUDw4ty6rcDh4jzzcFUnyCv29BPC-KcItTHdN_rBKIMXymcAJsit3zdAuc4K1BpzNbWly8rGHDjKvg_YEDBjB5YsYLGAAp1tVLxiAbFm81yJQTe8lIPmbdvZYkIIZfifd25GJ1gVQi2c8wMeROZTIwJLZ5q1ONWXYKfQyQPnnzV5dFEJO1LwTbtqyKVywSKLqzyubNSPX6pQ5ecPaDmRQz9wP8__ZPabwJDlfC9lGRdkYsix3Y_p-cABcYSMLZ6qxivDUJLI809j692gJRPDxT2qmR-F7AgdqwVkRnEoECxa264LM5uTnihM4LnNdhhVaKYTEw133kFSYJHVo9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=rDDfUDw4ty6rcDh4jzzcFUnyCv29BPC-KcItTHdN_rBKIMXymcAJsit3zdAuc4K1BpzNbWly8rGHDjKvg_YEDBjB5YsYLGAAp1tVLxiAbFm81yJQTe8lIPmbdvZYkIIZfifd25GJ1gVQi2c8wMeROZTIwJLZ5q1ONWXYKfQyQPnnzV5dFEJO1LwTbtqyKVywSKLqzyubNSPX6pQ5ecPaDmRQz9wP8__ZPabwJDlfC9lGRdkYsix3Y_p-cABcYSMLZ6qxivDUJLI809j692gJRPDxT2qmR-F7AgdqwVkRnEoECxa264LM5uTnihM4LnNdhhVaKYTEw133kFSYJHVo9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=kYWV9c_6Vgutcx6v6K0HmoBzUewiGgiBAjrPqaZZbBIc3jFCx6qdFaQp_IdYo443lPGFahB5VDQZsrIVmrWwQ6AhLRND-SLMO1fX8hlihIX7yKmCdBiEs3XVs_3WsaLw4mVTqDu6XDlT0nY6SM7X6wfLuuhMa6Vv7ii6lUnRbny-LQo1SH4ng6LuS7rmnmPAsmocMruXHRrzcx8O296WSXbZx1Xx_ykY-m1DIAmy3VPHbCwhUY0VI5Ddyth6a_WSyvE4VY68IxAogg1FNOFzH3mpZ5kNyBd69czWAvxvymMww-PvlqaO8bO2dc-_De7B8R6-5vpdbL3uecl7RMg84w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=kYWV9c_6Vgutcx6v6K0HmoBzUewiGgiBAjrPqaZZbBIc3jFCx6qdFaQp_IdYo443lPGFahB5VDQZsrIVmrWwQ6AhLRND-SLMO1fX8hlihIX7yKmCdBiEs3XVs_3WsaLw4mVTqDu6XDlT0nY6SM7X6wfLuuhMa6Vv7ii6lUnRbny-LQo1SH4ng6LuS7rmnmPAsmocMruXHRrzcx8O296WSXbZx1Xx_ykY-m1DIAmy3VPHbCwhUY0VI5Ddyth6a_WSyvE4VY68IxAogg1FNOFzH3mpZ5kNyBd69czWAvxvymMww-PvlqaO8bO2dc-_De7B8R6-5vpdbL3uecl7RMg84w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-QYusc3gJzBsQFiq2vDc9r0meTRSEoxzVzP5rb23sqpVkkwpqTv9Gw7M6HkU2fUipsSuic0V2z7yFeVWhrxG--ciSa4b7fq2hjzHdIPeYiTarrClBS-kXMJh8bO-40fQ38KnV-IEJecbhswIJDFLFT4BfnIBrQWMCKLXa-78Rzy8elXqD98uVBaD0W7vXsYagSla13mbCx9cfCDn69LKhTQOSLYaB2yQGAxXlQiT4-0ULhLYhe9LZxps0Qsbz_c6JirBLkBtMfA3U3CTkelucgeKIkuTkDpCGKcwtn1kJE49eBYk2GanLI5TDjBgYbzjDqYETp4vrNuYr5r5g6r6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=CgdYUHqVleRX_aNInTVYposLgP5lWlZ9nufFBjaSvNfYF1O-cHZ-ybnAXUiDtKqLXq3ntXkY7ZqNsywhbOVZ14L05NoauHCqYMm3ROAD7nSr-edAxe3iUg2hEbGF-A_BDiwwqRlP5CzjoQFXtk1-xvG2XSHOp9kRUTQTeenIV86g4Hy2wuGOk_TSc7Am_jPyqjcRssb6X6HFWNIrrVhe8avP8VQdyrxMCrYD2njmrjgjJEUUdsQ88FoYDIR6Ukz0eCtqah-Z1fJ-NO-DxZz61pe_Nabz8mIjI_0kuUAXhx0QhKItZQbUrGuwqeAj8Wav4GPpSkAIv0lEgtUCaXIcxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=CgdYUHqVleRX_aNInTVYposLgP5lWlZ9nufFBjaSvNfYF1O-cHZ-ybnAXUiDtKqLXq3ntXkY7ZqNsywhbOVZ14L05NoauHCqYMm3ROAD7nSr-edAxe3iUg2hEbGF-A_BDiwwqRlP5CzjoQFXtk1-xvG2XSHOp9kRUTQTeenIV86g4Hy2wuGOk_TSc7Am_jPyqjcRssb6X6HFWNIrrVhe8avP8VQdyrxMCrYD2njmrjgjJEUUdsQ88FoYDIR6Ukz0eCtqah-Z1fJ-NO-DxZz61pe_Nabz8mIjI_0kuUAXhx0QhKItZQbUrGuwqeAj8Wav4GPpSkAIv0lEgtUCaXIcxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=DN8KTOHDTzWnhIrTDtKQ_Yg81pbQnB-QH2wogeHb0-HTB7A5jlcSUEPkocQUMw941ThRq1sLFwx_ht5osvvNFCgsBKIU2T_xztbq5ETiVWoJZtTiKr1Ye8wlxfGqeZWVBInm9dmTyHBC-Y-PXWYqR5KgzU8zkk2WoQFZ-20dRXh1caWZC8OuaKBSEB2jAuiMEi8N05G2gtVYqLasl5RcagyWDamwo7vuL-50KWMbucSE8paRmz-ZzRAqdTjqHX2BYiBArVJFgzqDb1bGba_4HoeLafe4sfc9N5qiqHobNC8E0JhyOzjBJ98ThF-aTbP1H7dG4YMCyMpNKviBVhci-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=DN8KTOHDTzWnhIrTDtKQ_Yg81pbQnB-QH2wogeHb0-HTB7A5jlcSUEPkocQUMw941ThRq1sLFwx_ht5osvvNFCgsBKIU2T_xztbq5ETiVWoJZtTiKr1Ye8wlxfGqeZWVBInm9dmTyHBC-Y-PXWYqR5KgzU8zkk2WoQFZ-20dRXh1caWZC8OuaKBSEB2jAuiMEi8N05G2gtVYqLasl5RcagyWDamwo7vuL-50KWMbucSE8paRmz-ZzRAqdTjqHX2BYiBArVJFgzqDb1bGba_4HoeLafe4sfc9N5qiqHobNC8E0JhyOzjBJ98ThF-aTbP1H7dG4YMCyMpNKviBVhci-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnzqYSdPF8BinHAA1ECTs1MQTfsb3NrSfDf8_wnrOFe0s6b8hVKELMx-6xjQke-z07qTbiWhNUXPqjneXc_R-q75A8iXrutngRWh9WPT--vnIg5avk36FVqn7f57oE5-OjT-Xk_qIw6UuHVOaxRrocw-lKX3DMROHtnmzt9BU_dWhCSmyrodLemzgBbMbLNEthFa1qUy2EgaYRZopIPydcYkcqixGuReQiafhbwDMsdYd7Y-rRDfMHFeXfR-sd6mhfrXk30g8WMfl7wxcghpW6AFdYr9qe0HRKnyyTzvXvja6TU_osy36DlOVdQtf-F1hqK7QvMyxZtGKPwf_dRBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ykfui3St3wUIChu66Hql9tu7haXSbAvr1zTWV6gBxKtzsohEsj-bOkqx1uS2HuMss7ig3z-wZz6Bp7Ts85r5z_4e2Xu224UkSWxQobUq175UXfburV0rnZuEOXZo1QcJJEWyyAG2dLgwREwyFld3J6Ya3W9Ykk9QCzgpXKCfsskC5JI2oGCScIkWOArcvYSyoi-bw3imiYvW_ocQsm9RUzYzKVvTm8sQF_Daztzh5LUul-HimODh4ii2_Mci70t5q6q38ZfUBBUQb8FORW0H8ER_Rb_Lb_VR4UJI-dMbzFbS8WFfRZ78jkVFKVat86kQ5J71uByzGx44zP9tKJgrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2-cbqoZcbPEUCe_fMTXvlfi4EXsDENqdR7Amg3NADr3hkzcq0qSs82AuHnMTt8r36u-RK_7GllsKvyGa-2Rk9eX3Dl_27Jhz8CONO2bZ3Tlu4qZLEdhBmDCZ3dpo8BAiIErYonb7d1ke6UFV42SbsYURkVWgt74qT3z1Ei2J-xy6MvqOEP8zdiy45HmBMmH90389x5SuCAp8ffpxUT-sUGLXl7STdLwA12Dpfvin87iYnobxKVLnnt1gN_qVofJmKQ6wvIroANU-3T4lSKzLRKPP6lauT5FPU8yoL3IdpIKzqoaObtrxZSqNnzArbuXss2UJwfuKZIZ6UzTwSvJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=kqdLWbxWuoOyfHmnIUSyYpmHaWAS1hRGDIVak8IN6_57BelwDNiN80pdfPxsyq8Y4SKQoNrv4kxgwTAwJfyRymdcJpGjHXQxn5hl_GibylrwUxAHuDorKbiWtahx4wlq5K5FRFJan304lGBCS9Xe-YryheVKncC2eyALGxgHxCPvYM5GSpow4-xd3mIBew956xRJSWPkMd0NX9fvBl004diLucsA9yf34gWlFaxZ6DN3EnDoxAPSRW3s-E3lRyE3doQzK3jSUSDJtEWa7AK0VU6wxhMDJ3qjBmmsLanjZNq3a9iX6HOLQ8JQdbStOe9H56QsY7vJKsgkEUZOc5U7UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=kqdLWbxWuoOyfHmnIUSyYpmHaWAS1hRGDIVak8IN6_57BelwDNiN80pdfPxsyq8Y4SKQoNrv4kxgwTAwJfyRymdcJpGjHXQxn5hl_GibylrwUxAHuDorKbiWtahx4wlq5K5FRFJan304lGBCS9Xe-YryheVKncC2eyALGxgHxCPvYM5GSpow4-xd3mIBew956xRJSWPkMd0NX9fvBl004diLucsA9yf34gWlFaxZ6DN3EnDoxAPSRW3s-E3lRyE3doQzK3jSUSDJtEWa7AK0VU6wxhMDJ3qjBmmsLanjZNq3a9iX6HOLQ8JQdbStOe9H56QsY7vJKsgkEUZOc5U7UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpgUnb_3liHSCfZRUfTfCaAKzXekAyQcPocHjwWIDRbVcOSGVHDHo54a6Omxc8HaBKrmHKQr1inblzZWSviltbvc4xudZQju5TIZz0wBIcbIOmQaUB2KGNaFr00RGL0qLHUHtK9fnEb0PtJZar-tiBAPY7zcOZR_hsvr6nZ_bNb-z_-QtPqPUJVxSC2Y6OcWfI0D1PQHtOCMrHCd-x-PA2Kfi2dwL34FeXrXJYdkUFYslIO_y5xDx_ooXtouM7ywuQQJBPKF-nXh6PyxjtNawv1QNJ8OFwF5lmStOKyxwobG5wVSfnjA24Dh-RrdAHJDUFIoCSj09pKMxZqByGZ4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekf6u9_rK36fCkeMme6oehNq3JUf_BmOL0l8Z4wcXmTYe8K4gO4zPmcqfRS22sxaffaQOBs8Ezbs6pjjQMv9M_DUq9VBUZsBr6WFKYwLXjtxzxuhVIjO22CEclLHt2491_BIbZ11gnyRcuPnsY-mKYMUQ8GU_gb5A8Le-3RA0fYGe7KjZ0T3uXiXK_GOKOPJxjoroF1jwXnbQCkHGfD9fbGFPtdvBq8vPmFipsM8Tnhwvw3gQD_l9BxoeNR8POnJmIOCHEyQppvuLIKm3fLXHhPRvLUDT4WcjdHgVFCta42lFxB4KxVhWBIoPawrmsDPwGOucwSMf45a8OXP0cA1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0Ilw26sI0WFHkV8ofH2qctDRY4nwLsvNesHMX3xCZ8dZaWw2WXaql3MAVfUFAL2j_WomB7P2_6JXjUiGEnYmzbYg0WveULCZVseXjTSPXBa1dePV9q8OhHGfzuqByXPa7yRQs3Tz2ioUHCt4ugpONyq4qiT-SGsC9WaAH7fMRB6zGhYSf5GxfWYv-uueSrgziAtM1PaAHdanq12Ls7NWuS6xIE16DQEGKmAir_2swBgyRrQpqlzWuQSeGBr1zcJGibfpm7of92TlUTzupC8Chb-nEt1kn8zjjYv3iLjBFtXYArJGoycU2JFyjideKp9Ejeqth7c1x-ukZwXWigwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBaXFvWB4AXvmgbQ7UCe3aSmki1Wq0LNJWOlM7D0rT6EvdPEGOWAvzXUNngTYz77-RZEoCdXyujyvg3_A2z1ApejyPMrrhytkszXgJu0pNSD8Pr9GTOGOENEAMgESabcDH1BO01x766V9azpyjzAHPVuiTWwTRaurNo6F8afkRSDgTnyo1NkbvODeB9QZt4D-0s1OjtN1W4M7xfVvpQ7CRjE1SuaDyFbyQHJrJHwWnlogv7yU2JKe2qBZA3lRclQH3pi8ctJt7r2FhNMKS2jAcGbNRjJGgxftKIKo43h3Uj4uV_4OQYx3eFN5-kysxes8L2VsjUw--h9vkt97szjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBbyeu5n3N3jYcdEK8Jbb8QROkj6zRv6lCoCq3luB2eCMoiA_11Fh0eo6UtB9q7PpVcPgo9-RIqllpgnurctAvqUH97AclcqbJUEf2d2bLmIptVjgR8ovOnS7cKwtha-WDaj-RcXAnqE4wlth7UompdFEIas6_PmbDECpDCI2U5mnivgxvlcmEE8Q-dnDxZ6DwAkijmeXr7FlPQc0iGLNCc7gSVKCIOoa2hKqfG3GncCYyxn1RwnjBvL2ojugLtqrRNyiH7OARo7y93hpOQTzYOwDdCXmqY_z7e_Tg52P1IduNINDqRGYsMwfs1Pi7qTzv_6USSV-XJjZWpzJP9Xqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE05K4cmXg_kTT1D8NKcK95cIWgJK3oqzG039Q47LHaoQo-Od9_3b0ZB-pBXTwL53FYgGcsDkC_MCaGi6F1dsrWi53yTxWLhE45Q2PVD7dxk-hGQKI-ase1q7YgzjWFP-iuIF9gNhNFT1gcCrqXvxnDY1i3Yg9hBh4PtXQaZGnUxntJk4e4fUrFezJuybHMGAwL5sCXDmoA0OoQWuF9HsJ3fiK1HcAzMedEkPhi_2PeTBhFsHrzyCYByhUuXLReqJ2sLIAnUFlTiFb3TlfLhuYILwKQMrCBr89vo_yE1J0haXZQXTj--OXnEBf-8biKEyWwv8wNbnY0qy2th_4zCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1L1-emSYzR8_p3B11kL2CmJTtsdi5TVfcc9FmyytukiE9G91oO3xUpQtU10tTwzzLp8762YMibUq5Q1h2rt81T7JVt_U5w-w6IHHJqfet6VkuCgX5hWa4Z7LEcl1rY_DVZok680Y81xdjDaXwlr2r-t5Ws1C1YbyI9qqfnrPdsIaLJ6tI338_ixlgWOEddfUp_DzeLZ9YkhZ7EPiWVrXAdzsB6NLGmmvJSBJ5A5PRZhmq8bL30sJj4P0ENYoqk9D1mZ3Afim3p5FWPeHfPlYsmABhU89CL3bQ1ldBT4984IVJS5oSiQhUAtUg44MjMPMQZyUx9RbEI8YMVIxjupBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBtoouRs_3v35AxhHRpCdrzxaIqDzMZ_Mme8VSxg125r-Vj1UHxhrZqJuyMxxA396DwT8PkA5fRvXyMRQK3KaMkcr-97NviRO-6FTz4583rxLHqBkc9W7WrJoIQKOxx3CxPTxsQAKMJGlBYD0Ha_HMvMjpEy4YGWDy1qEQIFMZLBesvIET2XD0U6T85OfWgQFRi0y3ki5I2mrdRPR_87-yilDhiSC3in0AWfC_rmKCK3mQbAdCjkvtb1AB9v3aSnKIuEv3BtExlCBiaYYM8nZSMNRwhAbmlTvlihccttTS7bz0p2I64duG26BtmSdkyfW4UTb-Qm_RU0jH7cl8NREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=UejKM_894uub04m0OlgnxM0P7VZMCxIgilhvGYpcMXtgVakIQRZWsDKsrY7dYO5PlM65yJeiiExOpDiLKf8ICEF27vPuAtVdebROssfgBOyoLFRrX2ElB1CZCqR3VV52zlIx1f42k6mNKIHdhsWx-GydghWkYJfQo6VxgKGus1IiNSWHyT3not9dkiBW-bM5dUOrfF_HT-wrFFcKCL_3uGI-KlTFqOuztdT11yv4sEfYaLKPv92NxZ6Pd-FHb8766WXKiTsoKXigtrMnIKv0lJM9F_zCxVONmZ5wdDXZ4AitFHmimEIVPfxuZCd-J8qVqCHZEu0u3WYibVEfaO0JLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=UejKM_894uub04m0OlgnxM0P7VZMCxIgilhvGYpcMXtgVakIQRZWsDKsrY7dYO5PlM65yJeiiExOpDiLKf8ICEF27vPuAtVdebROssfgBOyoLFRrX2ElB1CZCqR3VV52zlIx1f42k6mNKIHdhsWx-GydghWkYJfQo6VxgKGus1IiNSWHyT3not9dkiBW-bM5dUOrfF_HT-wrFFcKCL_3uGI-KlTFqOuztdT11yv4sEfYaLKPv92NxZ6Pd-FHb8766WXKiTsoKXigtrMnIKv0lJM9F_zCxVONmZ5wdDXZ4AitFHmimEIVPfxuZCd-J8qVqCHZEu0u3WYibVEfaO0JLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vo-FsQUHlJiBTu9wt_edstRVPdIFTIlYOVxy67rFtppWKLreEmaDeErZI6iVRJjt6ZxcMNEILup6FyPU4Bgt0x2WXtgpiWxqaRmomf-ye9aj7-0bepJW6zyy7qRZpe9PTSTpo8xwbFvtWLH9z2dg7_pC1oq4loK4oEmlX6-XE7DYH5xAAv_AGtABDfkO1OVm2T7z1r89kxkUhx7aUvS24cMsIuYl6dBxzCn2ePPL6dqBVTIV6_yZTks8U6WFnRs5hCK46M9cZAkMG9sZOBJ8NdW_pLmijEH1zUYWroePV-OVE6g5Ej40jlXhxxjpLrpdOWGyjr8RE8B8PKuEMJfi8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY5wpxs0nsFZMzoBoUX7DqPulkZvbqnfJ62jzHcaamYR0eRcMLR6xBeKbnJ8E8O4MWaKCBGAPyuk-IkhHn1Lf3V2jS41QQhcZS2c-c6XLwNcQFcu0NHhagwBZ7bcEE4XxVgmiHn78RW4cavpKIJwPp-4Xmg8jHN8ZVKDCL2NSjQqYP1wK2xpoMHr-zg6SWTcjb9SiZcHnqe8fCLu6g5RCuQb0n2D-Z_GkpgDZ__4ZdyVSzUP0OctuVsHnqHD5E37zATwYaa3-tCw5pyYaYZ1JT-2Onq9bz0ZZ85eviPtGkkbqzDf5OU5CDXzjTvf9HcXSNF7N9NWkIaZT_XbNZTPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXxBXevkY7TjhtHAIKANIPyCHCeGgmFdqLlo2clsOF51JEP3sNjSm0P_MwZ64j44ikZxb7PT9suz-_gP_vCdWtFU2m3_AY0F3UFEorG5UdMhmUX-uO-UCOWy_0VUNJsQgi6xNAFjyf1nQf4Z8yL_U-TfVem1xdsIDFO8zp2qT8Qjo2Oq55YgAXRajrXoOJkgnyR9E0rC7wW5_siTJEi8q_hA6J-IcefOdd9DDh0KeQP74yKGVswOdDtk17HsNqcXGSphg2C8M6MqmRMLTedKS2Xhg_eyA20iwh8KIogk680P8-yygi0CvZ6hC7UxRgmUMtXPVbihV1hxA9w3xqLoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPei-oMhDEDbt1dwgsrwuAtfuW0B5sf_Jpj9bB5bbs0YQwDZyYwznNdD3A6gir9nnPJCxdc6HRV4PYMZyEmrDD8xZ0KZ2IfbZBLQsaFyyALVzYHx8Z_yJSk-iImGJohjM1cSpbl6A0pXM0xKkYZM6to9lcnNgQz8AFDIJIvr-9mNtVyC6w8JwQ4tZxhqbhrh2je9IiKWwAlhJ4LlllWKBPdjFJJe5G97IVaXlR2MjecHKle8D9SjRIGiim8ndmOgHziD3D8PwbDRsOyty1Hx51vpp8Fqb9cvU8B25WV63KuJgdSP1Md7W-_M8mhYAButIa4_E_A9PfIMmV3xZ4XdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=WOjZ0EM5nP1sqOa-WAGRansYtk1vFLatSWXcbwwb3PpQyUp1viOxXecE1-qc_PSu_xIjXg78MbkkQ63x7M-w_EkjnGseB0toivH1NX0xwihtMezl0DCLCnACtlMc4GZC9FNa2D9a57-ClyPrb9piGKrleKttEhPBPJfPyJHe5necBktGEZg6Ij_AwY0JrVg11fP7FMotHD0bqCMtX-K1eygPrWsqi2U5AWP8u-mVcIIqtk0G8836iKM3xxg4WqVe7ZACkRnRKUmw77QfeKl7o-91y5bEiSSJKmg3C0wg8W5sDUKNySHfaRGm1SWn_rbJJ2G5ei08QZOuvqV2P1TMow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=WOjZ0EM5nP1sqOa-WAGRansYtk1vFLatSWXcbwwb3PpQyUp1viOxXecE1-qc_PSu_xIjXg78MbkkQ63x7M-w_EkjnGseB0toivH1NX0xwihtMezl0DCLCnACtlMc4GZC9FNa2D9a57-ClyPrb9piGKrleKttEhPBPJfPyJHe5necBktGEZg6Ij_AwY0JrVg11fP7FMotHD0bqCMtX-K1eygPrWsqi2U5AWP8u-mVcIIqtk0G8836iKM3xxg4WqVe7ZACkRnRKUmw77QfeKl7o-91y5bEiSSJKmg3C0wg8W5sDUKNySHfaRGm1SWn_rbJJ2G5ei08QZOuvqV2P1TMow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
