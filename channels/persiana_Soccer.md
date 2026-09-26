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
<img src="https://cdn4.telesco.pe/file/D1YSc4QyUKLklhC20sbDWv_i2pa16qmPt4GYYyagysRe0IoQ8KtpKeTMelgNiGB-9kZi1Z5ZH1a5f6wy0D6oVLaOi8kUrcZxBeKPeN8ow4YKzi5ZQAQR5rqzJyLuhwH0zPqyIPI3bVqKKNjanr8G8so55RIUCQjZWfCEFQ247M644ixQn3692bSmlemN4J5a4c6XwDJSRW_luFHLPG4grZKUZUNWYMpG6oM7SPBaapAdLGfJ6pSSgiEviXYErblEoJnT99rSwTsPY7GEe64IBNJzyZokj1vR3W3g7ew9ri5eU3Fg5ppDDfNNwsjaQ3bANHPl7zcyS5orM5qQ1eJW2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 447K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 11:38:34</div>
<hr>

<div class="tg-post" id="msg-30467">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارده‌مهرماه شاید یکی از آخرین شب‌هایی باشدکه مسی را باپیراهن‌آرژانتین می‌بینیم. شماره ۱۰ بعدِسال‌هاافتخار، جام و خاطره، حالا به‌آخرین فصل‌ های دوران فوتبالی‌اش‌نزدیک‌شده؛ جایی‌که شاید هر بازی، آخرین قاب از حضور او در زمین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 916 · <a href="https://t.me/persiana_Soccer/30467" target="_blank">📅 11:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل‌های کیلیان امباپه برای رئال مادرید در دو فصل گذشته بعد از پیوستن به به این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/persiana_Soccer/30464" target="_blank">📅 11:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30462">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoQIDkzcTAB5A3Ezn4z_od1C92uvyQhvk2gqFUgH_NACKu8-A89KXj0ImZT1xv0dDtkuzurl8Y5NaFB-sRse1yxUR2Z0-ELdz7xyiiz7cMl38cFFuzNv6mzwm9Y7LHCkovpOtY-hinrCgxF-Sm7anjfLOSyapbGkuNVnTEJuIsARHJlO7-j8C2empbpRBQeKC4KM3c87n5Lrj9IjKePTH34hzwE9zDCjLZ57kcZmcqYzuRyjQ7iNtEEwvyu-3AFL_m61-2ucv4mvUieGzJ5yreLQdRIxCktE63hyVeZaQR0K6EaC2XEeYxhEj3Fhl8p9T2w3FX1ejCezMM2csDcM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0TplsJ27ZIn23ScXfZ9FirUCYIUBRJgzftVAViqKRGYG6Frt5bUJDRSh2Z0YPWfBpMzq9KdFpLkZvh3AR54JHMJXJu3xVv7bII3ilefxGu2zYItGi8K-2x4uehZ_NCVJmVaunhjUywEmUh-OE4iBDIfxS01ZHSEYdtKKyrmNOpA6LP4y0pqRmxEqFDx-agKQ7L8BXQs4CGbTjcX-vx5NvF8Utkl5Na3wvE7AHeVBuwjc7vjJh1I6--V2efPCsSxDrU08C4Hkhh-qJAmEWUbzPUcgQIc3FoMo1G-fs6FH1dZiaJBEAshyozgsSGYrE_4mcnUWsICLZ9eb1-ImnN1NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/30462" target="_blank">📅 11:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30461">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌استقلال تاپایان‌هفته جاری 400 هزاردلار به فابیو کاریله پرداخت‌خواهد کرد و پرونده این سرمربی درفیفا بسته خواهد شد. نظری جویباری پیش از عقدقرارداد با ساپینتو با این سرمربی برزیلی قرارداد امضا کرده بود و حالا بدون اینکه پاش رو تو خاک‌ ایران…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/30461" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30459">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6160de2528.mp4?token=maB3GFcto_cL4mLuA7xCQyMkBvZvF9uuVAhyMFSZ-s_VNJuUSNbM9X2L2J24x16gahNTVYAq5gQC9sdNSH6sTKI1UK0rkTPaWUft5SFVyG35jgXCeaO78MaJSQcy7rJzJ6EQt4SMLR1gK5UkqP7wF08gERZj1q93Jtidw5iRZOfztgl8IGScE1yXl7w81E2MJFOFaOizaeG4LcP-1OFlKPelzavnBYaMlMhsIzkBEa7MPRXoDti2lgwHbF113E_8z8ekEdjFw3VJcbxCoREIpKzamq0o0IXeJcqGiNUj0w5NHlkb4Xty3WUv_ojoj0mJwfzcKI-vzkwhTdq9VTn4rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6160de2528.mp4?token=maB3GFcto_cL4mLuA7xCQyMkBvZvF9uuVAhyMFSZ-s_VNJuUSNbM9X2L2J24x16gahNTVYAq5gQC9sdNSH6sTKI1UK0rkTPaWUft5SFVyG35jgXCeaO78MaJSQcy7rJzJ6EQt4SMLR1gK5UkqP7wF08gERZj1q93Jtidw5iRZOfztgl8IGScE1yXl7w81E2MJFOFaOizaeG4LcP-1OFlKPelzavnBYaMlMhsIzkBEa7MPRXoDti2lgwHbF113E_8z8ekEdjFw3VJcbxCoREIpKzamq0o0IXeJcqGiNUj0w5NHlkb4Xty3WUv_ojoj0mJwfzcKI-vzkwhTdq9VTn4rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آلیشالمن بازیکن‌تیم‌بانوان‌کوموایتالیا با انجام این فری‌ استایل در اینستاگرام کریسمس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/30459" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30458">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT2vXESX6hIBByGJNd95TeErOTTcmiNKU3E0AuzuL4zjj6tQuV28jIpsroM8FY3OA4cSAKTIl3QX-jnLzKEt3IiFbIYY_6jH9hrakpfzPXIisee7YMufIiZ2AYO1Qo5DkGZBaNvJqj8KGQjzO6mvGmlGDdL5RawOoR5hJN_a_ou-e8uJTmSiqg3m5xIu3QOvxqM2eNYqxjdd7hlvNFT-_SDOC7JXl_3lfPr4fj5TamHeto02KT5tfG0YVlrp2gfkuQVS1OHFMfI7XB7Z9cAEw63T4k-vIX23eg2hvAPsol4sg3SFV0O6zswvH96c0aaUpiUWm17mNPlYkuSLy6Gxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال مذاکرات مثبتی با فابیو کاریله برای تسویه حساب و بسته‌شدن‌پرونده او پیش از شکایت به فیفا داشته و بزودی با پرداختی مبلغی این پرونده بسته میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/30458" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30457">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLxhnGwp036NgmvRXDacvaZGdgIt73PCaRmFA_VNge7yXRrmR6TmYzHo1jk5Qcrl0g0iVF8jDu0inv9UwiCdScd8YVO_-0MQFwhwcYtJ0eGvSBw-phK4Cye3Zczm-tSsR-GarWDdOoaJWzFOuvJWvXIO8pQ6-kXY-aAHsongQecHXZLbLfmy1BngKoJH8iYBfFGgV4lzmHsoCXQPb8dg7JCI7eUl8PTOrKKt9Me16hXsn78LdFj9WG2Dh43fLDDYEYXEhRRhOA5rE5kxmDpqSw_q9S2C3JkXBMQdb_JbBp1oL4N4n5B9TGu79vAHWhi0qAmQVUz7N6p1PjD1XoHOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/30457" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30456">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30456" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
جدید ترین نسخه
اپلیکیشن بدون فیلتر wepari
ثبت نام آسان
✅
📝
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا و یوونتوس
🇮🇹
🎁
بانس 100درصدی  اولین واریز
💵
Promo Code
:
sport100</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/30456" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30455">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPepFWcOaVkU6spaqFmB159X3LtsYyVmUgHPFGpzWVQ9hguiFlMvGqJRvHIuU8lRF667bmTWuD3jIdXdTfs8dusW4AdhahkwZ7rWAKs1PSGUXy9QdHf0c54gIFcdUJbLzqYAz9IlMJv29HK6W2oIDgLtQEYdaiYbL1Q2IWS5pwLQRV48_Zf9QL2BeSHTJ2RYWCmHdsi37b5siEwX_hBZ3naC6gvgTmXLKHaMVgeQbCadXwmyQOdGHtrnyXMUS5etNCSNvB_dbTHMzNiK2oGw_hcbiKDInfqi-JTWdiroFQxUkgardcoyccOdn6YhRZDhiM1v-rSPdPOchUhgL_FGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی های مهم امروز را با آپشن های تخصصی
در
wepari
پیشبینی کنید
👍
💵
امکان شارژ یو ووچر پرمیوم ووچر_ترون تتر درگاه مستقیم بانکی و...
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🎁
بونوس ۱۰۰ درصدی اولین واریز
🎁
هر یکشنبه تا سقف ۱۰۰ دلار بونوس هدیه دریافت کنید
📱
کاملترین برنامه موبایل
🇮🇷
پشتیبانی از زبان فارسی
‼️
لیمیت نکردن اعضا در هر شرایطی
برای ورود به سایت
فیلترشکن
خود را
خاموش
کنید!
🔑
❤️
🖥
Wepari.com
🖥
Wepari.com</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/30455" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30454">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=lymRA_YQKC8WaRZR9j5fTNxtnWaM6qAV3S2ddM7yLuwokUOvh-e3fQpyrioW2h5Drt9ZmiDtgRR01jNMoXWSlQy9Qp-VXak-6Nw7Qhj0skPdvR_CNl30z6WEVRRliXo_vpd0lqDwa6nM6Ecs7qNR8XhDcZYH9WSIUz8r5M2NgMcWhPV2FAAN5tiJ2qR-KkViJS6HnTugSZIPOrKkaVXo2yOQIkTYHcmjNz5zHCIeUVvkheUow45Lb3CAzlPCEI36aDScgUK1UxZ_bJSsO-RqNTd4_lfiPURrjgVytnaMJ5_2OWwJtZmS6xZ5u836sPNgfYf0cODlEY9fSS6tCW3AqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=lymRA_YQKC8WaRZR9j5fTNxtnWaM6qAV3S2ddM7yLuwokUOvh-e3fQpyrioW2h5Drt9ZmiDtgRR01jNMoXWSlQy9Qp-VXak-6Nw7Qhj0skPdvR_CNl30z6WEVRRliXo_vpd0lqDwa6nM6Ecs7qNR8XhDcZYH9WSIUz8r5M2NgMcWhPV2FAAN5tiJ2qR-KkViJS6HnTugSZIPOrKkaVXo2yOQIkTYHcmjNz5zHCIeUVvkheUow45Lb3CAzlPCEI36aDScgUK1UxZ_bJSsO-RqNTd4_lfiPURrjgVytnaMJ5_2OWwJtZmS6xZ5u836sPNgfYf0cODlEY9fSS6tCW3AqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز ستاره انگلیسی تیم چلسی:
کریستیانو رونالدو بازیکن مورد علاقه منه اما من در نیمه‌ نهایی جام‌ جهانی در برابر لیونل مسی ۳۹ ساله بازی کردم و باور نکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/30454" target="_blank">📅 10:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30453">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZUdpl-ywkNOidpqHcBPKjPR9KlSap_JgeHYX2CXTIkeC813MiAYDGZrMXzLi-1a5o239I9GDk_3xbdN1ilpKOpoup-LiSBi-eN64Cu2tlnHIFCA58g1dfXMjr_TY2H1RpTUG4dTZ2rf-7s31wLNFI6OiSgujV79-vWafwhT-rbdgTBgXPtNE6qGaaVUmqZ4OWNVoTOOMD26WI4TuxwMlmxV5RhUGI1aCydygcwnyloXUfSDoXslLu8DPTmUPl00vRLwVCjJU-ukDGhM00hj1xXk3WuJeCM0VaHJqaO5FIt6bvU8AvXfnSvT9uaSnIH0mQvn-HX8uiGfXAZpKUD-kFfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZUdpl-ywkNOidpqHcBPKjPR9KlSap_JgeHYX2CXTIkeC813MiAYDGZrMXzLi-1a5o239I9GDk_3xbdN1ilpKOpoup-LiSBi-eN64Cu2tlnHIFCA58g1dfXMjr_TY2H1RpTUG4dTZ2rf-7s31wLNFI6OiSgujV79-vWafwhT-rbdgTBgXPtNE6qGaaVUmqZ4OWNVoTOOMD26WI4TuxwMlmxV5RhUGI1aCydygcwnyloXUfSDoXslLu8DPTmUPl00vRLwVCjJU-ukDGhM00hj1xXk3WuJeCM0VaHJqaO5FIt6bvU8AvXfnSvT9uaSnIH0mQvn-HX8uiGfXAZpKUD-kFfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این چالش عبور توپ از اشیا؛
هیچ کدومشون نتونستن کامل توپ رو رد کنند تا بالاخره نوبت به اسطوره تاریخ باشگاه رئال مادرید رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/30453" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30452">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCU214jxXWl7iCIjNCEBMkFwLcm7aKdVxayiB-0j78mKSyoM9YQMerSZSYYT0BOlhks2JpktECTIGfOHNTFhQF0rxiPtJT8u6WZKsJF02EW60Ia92YAmnfhKn7q0w8blZMEAHJRiXVGP_beJa0JObaFc95TuR8ZEhYef79HREkuWGOFcguGbz_pH3kdfNnf4c8Pv8qiAHS4vpB4sGxlZ9F3Pj_b8k5oulORVJ7JTEwTxMH8Y9OL_JxJ5xghr9hMQpqhYL0AsR4B7nIqdnvLH7qka3ZT68PpzDcS6u13C_mTWqX8wlfoXTCfU3qWQXgyCtoJIle2Aq7DBRgOFAzpB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/30452" target="_blank">📅 09:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30451">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNukQke0NqFndyNE9AEqbQgJYOkS_Vf9t5eVQEQoHhu33xMHiHD1j0cek0xjtseua5Z8R6poNngfYX0jow153AsAWEzRgKiA1HYzTpnkxQaWVrjltyp0h9EEZXPAB9I-F-GCACqtB_QDA88w4jI6A6IW6hi_T0yZoQqPA6_4JlD7T_9QH6evx0EFR1oz4cDO_Qqlsw-wyDjUJ7E4LPyGOSn3SmzHOmLH_w_kRBBGkqUJBTf3VmP5yJOU2vavfspLYhLV2qmfuu0bgeFNIelfJdmAkIC73d2I2NBJvXDm81CCbIT-tWLwCshG7mlffOMbpeFt7n_p6KpE-ywXX--L7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
رسانه‌ های بارسایی در حال مانور دادن خبر انتقال ارلینگ‌هالند به‌بارسا درتابستون سال بعد هستن و قصد دارند بافشار به‌مدیریت این انتقال در تابستون 2027 نهایی شود. از نگاه اونا پرونده انتقال آلوارز به بارسا تموم شده و این انتقال هرگز رخ نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/30451" target="_blank">📅 09:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30450">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS9-Pz7bqzOvju75GxKYXhJeXg_fg_PAcpvcwDEXz2-GrpmsfX4hXz8j9dGzlRYsi8lfxBuVSUKQGoNlJ5gEcqqFfIoWnHTT53Snv6-GwVCSPZwjiHPiXEq0gJonmYPFB8uQl-etZfDVBnvry6v1pH3FD3GGWRqM4Hvc6qivHv3-pIk4oF3KzpBAV0Z7NJmTT8MAd2qCM-3nruJRuRkGLFZNYthPgeJHD6N5BfU5I4iPDAt5HZLWfs6NJa52UeUqWce2CWY2giyuRU7ME553nct8DcijvzL2E4gf50VAoDXvipRu4WGORwQPP-VslnewmOswkwDSACrqz0essRwvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30450" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30449">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=XYCzFuGxjjkYcSL7rxD2MVCvyaICf11BfCgwcuV4PCgar_ew9LP8jMT7L91L4y3Jqn7_2vlHf-1WuF287HTEhF18OG6wNn11EfaCk_ZmAaJOb-XVGWdXgO35W2c1ZKRQT-4geA2QnbtSFJRG1hFORwlrvJ2-yRAVAV32rxc4-zl5triWY4sxQlRD90ifxCdqs5aAWFWzUbh-vaAOJQTH-3LwmlXYWF1FXXK0zV6_RnxHz15bVuvLJk5sh0TEG5lpWwADOeZEc5IieQgoo7X3mtsYa_7egLxzrWvvmT-JEzaoLt0IFuOnUbbUrqpFSiTiJUNOw9WweQgysxFdv67zWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=XYCzFuGxjjkYcSL7rxD2MVCvyaICf11BfCgwcuV4PCgar_ew9LP8jMT7L91L4y3Jqn7_2vlHf-1WuF287HTEhF18OG6wNn11EfaCk_ZmAaJOb-XVGWdXgO35W2c1ZKRQT-4geA2QnbtSFJRG1hFORwlrvJ2-yRAVAV32rxc4-zl5triWY4sxQlRD90ifxCdqs5aAWFWzUbh-vaAOJQTH-3LwmlXYWF1FXXK0zV6_RnxHz15bVuvLJk5sh0TEG5lpWwADOeZEc5IieQgoo7X3mtsYa_7egLxzrWvvmT-JEzaoLt0IFuOnUbbUrqpFSiTiJUNOw9WweQgysxFdv67zWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش بازیکن شماره سه تیم ملی کبدی بانوان ایران بعد این اتفاق خیلی خوبه. اول برگاش ریخت بعدش رفت ازش عذر خواهی کرد بلندش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/30449" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30448">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDWNJ1TInT5TNsAIh8nVQV1344v43w9kWurgBLbRmx8DQ7KseZKjdO9g5O1UiAOB3KNH2jsllrQWTB9oniqFPP10D6RkJYK3rws-GteApKbe8QW3GDMAVF-T4jRnAJIwY-FgHYbGIE0onXUpchuw_gbaZ7givBbKzi2hR21UqbK-C177lzUJcuTJbJpnRwuMduwILMwRYRmLnjTmWPmmUuM36vDQbnrTUOHu4cAXw4Qwem_G3aArBT7snZfoU4DvF-QDK97LlUG0USQkrSBZvsAJX9rWXjANxRVnhASHhwFZtmcEJYD6ON1bRhdjEuc4KPKkSWma2pGXSRJtLo80Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛تاکیدچندین‌باره سهراب بختیاری‌زاده به مدیریت باشگاه استقلال: بین مامه تیام و فابیو آبرئو یکی رو در نقل و انتقالات نیم فصل جذب کنید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/30448" target="_blank">📅 01:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30447">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWc4vcKNxiJqjoRVlU4JroPPdjBqYDvGV-wM3ZureU3Tia66qrhpjMrE2wS2FfiPsM0T7q6-z8VfGeffWpPkXRaR58IPNBnIYkOmrwwxBGSl-Kaa2pJvMRzL7OEBIFbD8p5phQdQHwwFZo0wHfD44nbsKIPfjTgWowzS5hfUMdT_BZqJIrtRbcCuDAdqCdTKGBLAHHBqdpGSQ65keRheEiWLKEBKrUb1MMnJHxSIBSXPuAhzhjFYoS2xZEz2GNETWGxz6ZhYiFqYWRsm6XDTo9534NuI8j5AsKlqKyZ1rcaTDB4x_xstfeaLMeza1TPiUYH021NWAo597MTtChs71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ تکرار فینال یورو 2024 با تقابل تماشایی یاران هری‌کین و یامال در ومبلی لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30447" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30446">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj4Uz6NLyT9QBIghdlOdLHZoCKa9CSy8of5jKMFeQt0V5mMRe_jVDIK2IwA1siKJ4SYAylwuL8V2oUbVQsbIFosl80nv8t-oldWMYu5z_dpyB3DeKEjbnL8XdpzPLr9SUKO_48cxQtfqBo1gXOP79A02qJRaifVoQskLLvjKEDMlmRZESN_XoUndrASd62B3xQDkonEgm_1nO0c_fJ-ujefFgf45jBfQt8gnN9VCGcD7M8V9JLW4xd92aknjoBAeWqhRn6FT_lchidLwru26HNtJUBBmElzT6H8ELaiMozRGjORPfbjwdXXYRJhxjeMv5BxQuL2eJtbqWkzSJ5X08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد فرانسوی‌ها و شکست ایتالیایی‌ها دراولین تجربه زیدان و بازگشت مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/30446" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30444">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srf51yGUHDLeP92dwCOEtLEl9EYQUyaytlajP3g3CgVxl7PDDozvg2fvl9DKHEGzmB38JkNlG9SaF08wJXGV-EASydKyE1ShTV45EBNIuwNEgXQVF3S9J1jpco1pY6gdhiTQ4By9WGSdrtXSuL3sGqvsNiN-VFF68MmZSmA1lMfW-idSKZf-EYYNsJ-UZ6K9Em97gb26ZGlUGusxRcNTjlG5B1Md8Y1x3HWiEUrFILdGvUk26vBfHoXwXg745qO2GWnDMp4zUXHyWu_Swj344F4D-LbUm6OLCEAYfd2PAZKH-ZvDGWfQY2i_O9WKqIacFQ6hJNZP8KuvDqiuXEcyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازیای امشب هفته اول لیگ ملت‌های اروپا؛ مانچینی با شکست استارت زد؛ زیدان با برد. سوئد با درخشش گیوکرش و ایساک سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/30444" target="_blank">📅 00:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRvKICMWw_EpAQ2LwKfaIU1M4-Jqw95DwCvY6pUKUPXYXCFFU8j8qVhtHhneurD7jTsol_qow7Exuvon81wkVlGyYLFK7P7LqTJ0-ifs4jqLgweljuQU8hiCL4dpSxmFIkWSwY0Ye6tveqLjyfUSYbLW7EUpHp1S3LSPr6I69nh8_T9WWjn184FBvHQLZgMhUzRsGE2VOvcdOQwxAY3BnqymGU3G68zVQVNXZIPjvPvpYT8N2xCbMvx4CCUIziNQ4f7EI4M2aXJs0u-dUTPdUJe5wlKwJ7NdQyQPEfmDO_tjWrIuKg8j2YtEpxXyhtTjiOkbHZcQemeMfYu-ii4t3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30443" target="_blank">📅 00:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30442">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H95lNf2fCk4lxft6rsXiW_Ef690wPr_AmuYTF-HePvx2mQbI2C7szHFE65SFIiP_cYjyyQBiuN-fkrZcy4eaojxrtCnuKaY4LymK5ZaqlHknydTuIJJzr5I2Wd6ux73b2aCYveY_n7QS9_6yz-fOcozfAYEe-X8z-iLyTHDk4tKGJlv0XkKIUibEotIIcyS8b0CCv4VH8cqIDRmf_hJy7as0VA5mVkXOgULUVT-LxybRHsiF6TzWhaBzj5dDSbwuWWzHaLQio7zg1pIluMRkNudyFy6QpkZ3lLGgQ5aCA81CA04EV3b3drDAWWlMGEHN3js9nxZ3z9yWhTCAtM5jGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قرارداد مامه تیام با تیم چوروم اسپور ترکیه تا پایان فصل جاریه اما هر باشگاهی که او رو میخواهد با پرداخت 300 هزار دلار میتواند رضایت نامه این بازیکن رو از باشگاه ترکیه‌ای دریافت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30442" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30441">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nptYs_YOGGuBwK_rlCSL3E0XVMd-uLuCVetKT2M86bZYTY0cC-1jJ_hhzyJElgTILdulF2tKHo3KgAhBzmJPPg3zgk-GPBj6DRnqj1ToHAKcnApkZl9NoIDuCBQE1v9Bu4oFwJTpvzwPImVe-84kLhbzru2wdNbGmGkjbXwfyy8_GwhBnboM5Ckym0CPCbVLN7Z_USPpP7RptPAcV39-_PBap2PM6i2qsYLaXX6rblF10dc2MXoJkSwwQiId11NpYoGGNzl2CAbXlBsNNrQjKlnDuPm9LnlGs4u82XWw_je0o-MiVSZHVEm0JxhEyhxUG1M55XZkPrW7RC2_Vhxhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30441" target="_blank">📅 23:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30440">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jli9nvZGfJe-WkqX6PQhO8njeVLHZrr273jvGfGmVI6X1EzIb0mw0b8YmZtMEf2kLvsvy5chcPPNX5vJr6OS2vkewhl8I32BpOYrZoMb4fVFkFr-PbdV9Qp8J6LIBQ32J4p2z7ot-KEOjj9iasGDbIzSRiZlT5opRwJloiPJPBkdL3VHmQfoysf6kAn4qtWJTxSE1njE9q-JDlzOh3U6rXcApD366IE0F33MP-NGE68IBq2ddFrD9uPTjz3tCZrEVf7spvlfrgOM6syt0GwBnMmjAltw1V0PXIKdkCd62kswlULXM9VyPC3iSRCa2SZJysLW_0OcRRGddg3uQW2cMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30440" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30439">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔵
👤
مهدی توتونچی مجری شبکه ورزش خطاب به حسین گودرزی مدافع‌چپ تیم استقلال: مطمئنی استقلالی هستی؟ فردا روزی مثل جلالی نری داخل یه‌برنامه دیگه بگی نه من نگفتم استقلالی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30439" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30438">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsnSkZgZxpg4Svha_9sApbK08AVAY2doH97HBXp2jfBCHqyPa_82ezS-Su6zMTIf1fmKZxNtTegVormRXl9ZgQ9BABHs-sRIDW4n2z3NeN4_DbTvsyqdOO_10u3lY5LO649NiGkoRiOZlAvQLXgh9Ppvt_cV5Zpj-U_1IHKTIpw_JCaP72_Zq1ZInBOkIcNeghPU4YNjpHK5Td0O9Q2Yk5G7-AAyKdLyh-ms8w9olYnKZJFncMIaT2AYj3dd9qFaXfTtSJP-ZnscJhfMuqVwGxclg3TeqHdxf8YFL3HxDCW4Ysg8P9q0bd0IludCZhiZ5pkn-UDQOe72mgqnM2ZAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30438" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vl1G4sk41ri4oDz_FVBiUugirjfaXKTWbhu9ivuqjDQSh7cSqkxW5p9fL5253W2p7tgBTI_KDDCXOW-5TxPwsVkTrzAnMvayBfW04scgsZPdW77LveNbX_NGrz7lml_Aty0WJCl8C7UxHyCMRwZeYJAz0dBYbmCebV2bsJW2x297gDTKcY7brzMV9R06KAgv6NP_vkj7-83SghiqLmqT5mo0SBXRFMnOCG8ot0HhVFCW2sp2e2rl6xoIX25vF4DxDu_mK1PZgKaHeM2w_6C8UK0qQouWKsq8lu7-xPLvmFakJ4mG5YKW3_y8fLabQVAWHQh5fuj-1UQPz6Y5pfmfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30437" target="_blank">📅 22:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30435">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bs-PvUSnOilEq81L9DI-saMRgJVMmw0uv3ERbx53Qdhjies1aB6wbcImK9Lp-yvw0IxyydF3O4fzYV7idlOKhNFfekUTji7qipXwSLAVHvUKSDZHmcLVPdQhjX3IRUIZoXrbaQKjUuz25GSEpzNluYAu3pW1wzFJsLWaOIqXqzhD4oITsjMTFQYBFnPq5LTXhBeOk06GtqDIVMKGDAZ0uBgP7qYHVvHGuTiJDd4UpUHYQZpdFQaKOQUa6Jiytg3wlgBqrhOlPWdR8YDmOqbV9rzGFKG6_y3uHJUOF1uUPA1okvjDovq-pqvSKVfCM9unrp51BPEWFcxZ0CsPoRej7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKTByJsWcyN6DdOHG_DsD_nYE2a01gA1P6kttY006p9sQTB7uex2rFIxqpe682y5HClkM4djQtpKkh4pXxlaNHQTjZhCxnfv0BkZbI_5otq36W5cI_CfYEuDRuhAx51AcgO5NMh6dHoxiQF-_0O8gZQUT906gz8DG0Ux-IrM3rRAypGDGOUwTC_UXg-v5oXQIJL50zcW6BXGZui1IRICjTrrUkvMZlBX63eOly3YQjW3BHBUivShWD97-yHkBQ_RAS25GN91BRaJ_jOUYuEbM67msjxo1LG0qjGr0tmO4IC042-FZbiBWJhcLn65mv56Q700yTXTdmVAHjc2Z1fcXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛
ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30435" target="_blank">📅 21:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30434">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cf909039.mp4?token=ungUb1xKBKeYf37A1t1ZTkARD2LloXTT5Y4opOH78vJp7qnTJZrN_NAQ84jISmXLeftmWgajpSQjagKRXTB5n0oKBVfttaStFyZnfTeP5ynyzc38qWRBdKZ8H8fcqBD-6oybvjELsA-hj-gjuJj1aQaGAvkgjDcGkRs_R8ha8IZZqANWacXjL6j7Rhkuh6RpCO6h1J1XQ_ETJFT2svDU7bCZSvp_RljKGAArtR9v6Yv19Ofca5tskqbhOExqq4wNoy7e9GjgWEsTq5Zg0C0hEoSNydRqz9PMFTYEVU4chxNtRw7dR_CXQ6mXSnL2F4U9XbBbH9IXLtfv-bRCbH0A8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cf909039.mp4?token=ungUb1xKBKeYf37A1t1ZTkARD2LloXTT5Y4opOH78vJp7qnTJZrN_NAQ84jISmXLeftmWgajpSQjagKRXTB5n0oKBVfttaStFyZnfTeP5ynyzc38qWRBdKZ8H8fcqBD-6oybvjELsA-hj-gjuJj1aQaGAvkgjDcGkRs_R8ha8IZZqANWacXjL6j7Rhkuh6RpCO6h1J1XQ_ETJFT2svDU7bCZSvp_RljKGAArtR9v6Yv19Ofca5tskqbhOExqq4wNoy7e9GjgWEsTq5Zg0C0hEoSNydRqz9PMFTYEVU4chxNtRw7dR_CXQ6mXSnL2F4U9XbBbH9IXLtfv-bRCbH0A8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30434" target="_blank">📅 21:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30433">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJOMRgcj0FSEbv-KqLUQCdyXLbmqabbsGTc9-oTUaTpS1WhfF6otYqgOR-WHVKTczvM_aW0RKX0X2y7i-Chju8yPBLUGpH1njMtKz4-g6Z7a3LbzTmsYoyvhokSwameM19HkX0Yjq0R4y3W0ypiCN4LeOllq28VcfKe0AmrzbqNIS6xzwd2TD_5rMKRC6jnO2nVv4nWqz-TS5oNhb491-owKFSCXCMdGqweLf92ck5SCqKPtQCU1ygfsHYzlvCfHMrf-nOVpuIlnMqmfDKeFZoktP4zBQzNLVDg5Sg_eYnY5ntNNgVw4MTWDU22VEwNBA4QaUW92WjAEaEj2LfjLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت فصل جدید لیگ‌ملت‌های‌اروپا؛ نگاهی بیندازیم به پر افتخارترین تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30433" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30432">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwzeCgz_iEj59qi3qk7DaSaFe5rpXlzPtPEkg2HhTBSSJIvUdCyydTPqug1SyZZBnbW67cU8BtcdICQjTUgFd5EIS6saUHBIdGIluMBtWuX-XkD5bcepYzcNr3cxS25eVMVdjTDE1__-1K9OsvRYY4WPyXAtRgVoAGbHsrvOxz6PWfk5n7nNuw1D8MhlcexGc86L-CBU2-HehO9kNWfRqV3VPFGixPBimxidoUiTHjTGCGE_JmYhFeO6NI13sMsvxDAQs8OqaDiDYj32EdhTAGbITS6ORny1dZifgeJsXQ6WdzG3w7fydU4CA-VBuyqJNwzilFDpCMRNfC8AsYw9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30432" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30430">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=cRuWiumXJxdOFzI0z-BpZ7ttz6zs1fcmmGn5YJXJQEBfJtoT_ltB8vEp9mRZt1aVa30QPU6P8XW-tcLQd4vIyS-gMe2D9BZ6Bzfzt5WZ8N3h2-haP5Ze4GYsOgo6xdWTN2_2LBDjf283S4YAtrIe4yW9sRmq8EkmCWsAHFGUWDdvZt_8xK3tLZ7bCyMEYJDQ57yRI3pcyBfqdS6LcVqKajeg8TcZnfr2ePVMpHJdqiphYMiDFvgC7kMAh5H_FtPqF4ftuxB1SGoKY3Qb0Z6_agB9ok47rbXrwOUJH3kT6Lj9FHMq848d0twO3RdGZwxj7hrKRSdQECo8A1HD_yWmDRTyFimi6GSq5SQOF404FSs3s_eFDul_-BtgglbjkCz4u5MJJxY5df1J_nM7Aw-_IrexDn0YZD-xOuOmS-gaQ88-S43IjtQph_vskmKa3deCAzr-xUk44Ln_4g38TYzNgvPdLC7m1-WqmJ9Um9YhPqW_Tk1NH0XdHWlmhN7XBrfVG4sJ6mTbhQs-WB99LQOnm3oN3pHYa1DE7tLajMJDA6oGg4GHnQqecjoUN6SB4AvTjQtQjYvW8BOUhzhJhHMOCD7cl6_YotWkgeOL5N81DRANp7RkYkW54G_l82uAUmomQnZVrdW_8-T3aMHJVIre_mvM4Ku7ZT_Myr_oQKWfeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=cRuWiumXJxdOFzI0z-BpZ7ttz6zs1fcmmGn5YJXJQEBfJtoT_ltB8vEp9mRZt1aVa30QPU6P8XW-tcLQd4vIyS-gMe2D9BZ6Bzfzt5WZ8N3h2-haP5Ze4GYsOgo6xdWTN2_2LBDjf283S4YAtrIe4yW9sRmq8EkmCWsAHFGUWDdvZt_8xK3tLZ7bCyMEYJDQ57yRI3pcyBfqdS6LcVqKajeg8TcZnfr2ePVMpHJdqiphYMiDFvgC7kMAh5H_FtPqF4ftuxB1SGoKY3Qb0Z6_agB9ok47rbXrwOUJH3kT6Lj9FHMq848d0twO3RdGZwxj7hrKRSdQECo8A1HD_yWmDRTyFimi6GSq5SQOF404FSs3s_eFDul_-BtgglbjkCz4u5MJJxY5df1J_nM7Aw-_IrexDn0YZD-xOuOmS-gaQ88-S43IjtQph_vskmKa3deCAzr-xUk44Ln_4g38TYzNgvPdLC7m1-WqmJ9Um9YhPqW_Tk1NH0XdHWlmhN7XBrfVG4sJ6mTbhQs-WB99LQOnm3oN3pHYa1DE7tLajMJDA6oGg4GHnQqecjoUN6SB4AvTjQtQjYvW8BOUhzhJhHMOCD7cl6_YotWkgeOL5N81DRANp7RkYkW54G_l82uAUmomQnZVrdW_8-T3aMHJVIre_mvM4Ku7ZT_Myr_oQKWfeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده: من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30430" target="_blank">📅 20:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30429">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH5aP9jO9j08BvDJUCvBygQj1lMHnTMG7P-0P_OD7lCsjMpFbdjxYxDH1pjhGIp2SWLGxYu1J_P_fgS3piaWxT6-dTah1VrACM8Ko09SG6FuFBmIlU0Bsxkt2uz767aV-Qo_ASmmhAxPKCX0SVZKcT3uF2X57uqpDwrOcbnJceLh5ln2F3qM9GflRYfZJixf_qxmMhGVSWfWYUkgp_0Wm-g3Z8cwKYcaFvhVLi3hICDj6JKoQP-imxZM9-ti7qTsSVkkPdXbVpjpyDKSP5fmp1vdGKZJkC1EYED_Ph9X7R5mFfpGqKLidkfr7JHaaKSNfGHCUUqyUCYWfU5VgoEQog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30429" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30428">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEJHaFtFd7S8gDkJgECdzn63PaL8ope9Hc8mJPLrFnxbzu9kmlTekIUQIpXmzAk3RHb1VRy17rW0jFYBBr6dVdUDZwrjqE3hOdfXRy_PSDGP-axP3ZmI0PAxwKSIgjs0sbGkrHkVzRPaEYvlCb2QxGd9tWYFmmLeuX7p77jJS__TyKk3w9bzDb32MjqnFMUbzr-ompiUajrWp2forLB3-qR3caPXvNg3O4cAUchlNjsn3ktqPxHE0iqZp5JiP6uzHZeGtevdOJablC7U3SOYE2PGMwz5rj0DSTWWpgnZrj25m_fLe9oeOJvGAnDXH3tCaj1iCoXmIk0HqhPqzjsTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30428" target="_blank">📅 19:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30427">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ROpXu-lf4aDNJD8Jojca7ZJJx-6ahO2Z-i0DLrDVbyswK8QHnarLw8wXdbNV92K7V9aP5Q8RJw8_zYs7-xuEArYv1Sk_OupfQnVuXbQZoFiUaJPDnosOLzB945fzvsWf8FL8UsGMAO0vVALp30hGUS-SSouFIGPWQR9I5k6xhkCEMjIcLP206vE9MzdfI-x9wHMhiSaOOXvvWwKEPfS5osovtxQQPfSWm3o55MgMosxLiiVI1ehxBoW-yq_dYsBPAkWeBHDtGACWkkV14KhefPG_dmN1wj9P5qEa4cdDW2xJhC7u4jo-8kqlWw04RN5UL_-wlwzCCurktBvV60qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30427" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30426">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXwNEXBLlZe0j6mlpcRT1p5QDY1coFF0EiONaWiDv5lWeBeLaXs3Bisf8VNbzQmmXLnc-bz6Imi0k1y-3nJo5o6aq4Y21JT1IHDrVHJX7w4CeTYCfAqJ6ph8ynq9hLkOhMGPhNjx3PBvZsmoA1QMqhDhKXd8aq9-mUmweKovXCz4hm6p5R_AZlKPDWUaebMiuigLAnOfc-WXh76wV7sjDfrxE9v_NZQdj4fpVRSgSIuZlq3nzGICmcpORIQyN4TXLL0p2CicwjBv1fXmqui_5UvgM_CWIHp5GcwDvMtqNgGQbcbZAF3qRk-PJ7TC--SYFg90dHtXWQJIb8kZ09xCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ظاهر جدید وین رونی اسطوره باشگاه منچستر یونایتد با کم‌کردن 40 کیلو از وزنش در تنها دو سال. درکنار کاهش وزن رونی اخیرا یک عمل رینوپلاستی "عمل بینی" انجام داده که باعث شده همچون قبل خروپف نکنه و راحت کنار خانومش بخوابه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30426" target="_blank">📅 18:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30425">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JENQ3pB03LMSSf2xIpcX7eRtsNobkrIcldVMvkhdiaFuroMjB-CnCebFi8-lZDlrj86l5q3IHg4IdcCF8Df5_9cvQqFnJN4j56gv8_aDOXyQpfsCsRa4N1ijfGUyRLMOhaC5ReP0HNB-B5C2aGLRT2UOc7pb55cJYPZzUM9-t_OEpGp3m9EMHUrIiNE65DsS-4jkGuiN2DhihzXKaE8moRnM1qyKbVWhMGzyu1zzyALkKbb8aUNBUp8B_G3HD9-UkaN0SRy9Y6pgFwTtHXxbnHoDK3z5-iKwKK80C7sdwojPam7rrUuYRShYk3aeu2XSLgay7dUbyMx1KRwo6R06lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
بعداز تمدید قرارداد اوستون اورونوف؛ باشگاه‌پرسپولیس قرارداد پیام نیازمند رو هم 3 ساله تمدیدخواهدکرد. تمام توافقات لازم انجام شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30425" target="_blank">📅 18:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30424">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsdd1UiIxBfBUqfQBJZ6Q8NjnKJkK2rMCdUBHj2RbA82tWHMNbOzlLtGAsHOpmORB19wz8enTRMBvq1UDUl8d-_KDjZ_Ojt9MBkhBlrJq7D4j8XNkZ8RVWbJITA4xAjtf3o1NX2UfFsZNIdObEAC2U_WjqDIDaPPd_qS6tmmBnT1pCs2-_77obFB1cGuu0eAJaJT2DGlkQidUweouexWhVlHGC3rw8_hbpuNIiDEOODY50OU-jW6JlOdgQiS7W22a1za5E3lc3LJ_pFHFcT5jNI52u4sZfA8rfhlMsb8LDWMSfJmPsjoKFs4DikifJsi_PgEp2kS56_2hMZW0YRmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛
آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30424" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30423">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMPtFiIYi8F38879yMvDq_U0yQKx7gdniKKsUNJgLi4yy2us2VU4JVT2j3rQFeQNLbA2iIj03uQ5P_LiCHRn40vOTs7Sz4FoRRlQNmkTWGiVL-beIGqNo1Ic--xq51XIqhKKg29P7KoWwfqOhSU6LXNaH5eBT26H2ZUjTAH6c9vu-nhD4Ea6S1T-i3fJMuC0aHv9l8bTSW6X8rlHYUX9vZvA96kf21NhXwHe1f4EBLSVshFVuljPd-3-VuakgZGwUfljJEeIRavaEGlXT8NTVzYm24Gkexk_YDpj2FmjvYKf2J7tBv0nPC9WcIbistLjR8-pOFVGSPUfEhrvUFUGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه: امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30423" target="_blank">📅 18:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30422">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtbeP2rrF6poLsHX1MGUpZD-NfPfFgcdePhMudax8AYQz6-b-0_Z8io-fJetpJsQGymtOVlKPpYKJTqp1k898rnfmNfNepnVqajYIx13Z81Xp_aoHoGeZyawI4gnp5kIvh9Dc-BCX3uWJa_WqFhVSqpzlf-hl0ARNsT4IaffN2H0bEs9MG5P4z-_7sK9Kv-weNkfb6soxBLnO2PT4zBFuXceA_xbMC4R5AA8V4ElxuK80In4wpeAI4adzv_QGb7niP5fkkDBODNmlOriDmsQckx0oHKfhEm6__4VkaKu-B5oEnbQpZ9irs4jte-1Nf7CJni73QxDu5AUPrqXZ_eKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین: من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...! هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30422" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30421">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0nz_BMv1i5Snz1Vu_nLq9KOQsY3x721Yy0ULNE-opnCDiZB4MihlxX-aT1K0CsHhpMDC5lt5T_xxnpNhDCaAAokoTQb462C5WCd9BLDqq2vOTHaC-dGFe6_BE6X3hmID3UackPwnSCFkanVaiRrHZLciQKajJKnlmVZg_SPt4GlasphMqFbbspHAbRWvez3sFrIn4F7vVB4jRBPfG0xceVJOTZJFviBtykD5P-9Lf4hIio0UvyRDVPZhRNpZKwdCseb8IdlRImGK5d4oQGJPohXyocNBvVIDMM-nyIyjc5jDxR8Ecyc5Vg_DwYP6pI2zALHWRDYcBm74Va_BFNnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین:
من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...!
هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از رقابت‌های لیگ باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30421" target="_blank">📅 17:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30420">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGLJ-N5Y4cPKhd2bjIPebOHXGyR-chZ-Wy9oYvuBtEvxQNCaH7Q4oiGPDcdxO-foXj2L2jquklXxL3BLCUajWt934Su_kCC-qRL0oqelSGyWiNhDCTV_hUEs_CVLWHlQKEWbkDD5al-X1Ui8cq26B-JisYDfjHhqx024-qzi5QGgNFIZhyM6n0dNznrGqy9b84BU2u7o9xMuH94p8Q-KvUvqSHZ91gTG-E9B6KpzvnMB521LAPqFH96PuHRpv-K80hIXJCZac8_tcuzg_0aurbVeYF8gcsTy5KhvtLX1YzOTehIVtGFMVwnzRl-ihRTgyzvm0AXGtAtl8DkpC5f3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه:
امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30420" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30419">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlT_kEJ5nr4h8r-4GsUncZ9vqEj4z7kQzHAtxulz6W1oimPN9_IIhflhyIQAt1H5G4c2yXSllPlSYODhqZeJsYpJGR1JQcXgzdfNhDUtyK5imcrfdXh_i52g3k6ss84ehKFEuHwW3YywSjgsa2p9eYo8ofYYgG8H6euNW01kEwJ6oiqvyDTX5APK1J8_vc320cLqySnqikC_-kpBIq13bPICm3vVWbRR_Bz_MQP1cFewD-yEj4zRizX2azWJXYP_x9Bws49U-WUsNO1uQFtEx1tTDycutS_e0--gyfL6QSGqNgGJvngWBahZ6UP4B8XWzdWD-awHFvG09TmIXLaiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاثیر نادر محمدی بر فوتبال روسیه؛ گل عجیب با پرتاب اوتِ آکروباتیک! الکساندر کوزمین، مهاجم بالتیکا، بایک‌پرتاب اوت همراه با پشتک حرکتی شبیه نادر محمدی انجام داد و توپ وارد دروازه روتور شد. دروازه‌بان روتور نیز بالمس‌توپ در ثبت این گل نقش داشت؛ اگر توپ بدون…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30419" target="_blank">📅 17:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30418">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=X0vVx6Y28h4nFXfxMZfFG09Lb9d10oLjW4zPzU3Dv8u3raxMxD-FFR37cC93ZkzPX3uwUaEgTkiOlM2VVDxm6iqZ6MXDV9yI2FqmXE5miIE9DWwAOqmGYNwE4jNp2FVxjUfWcy2xkd8L5ZV2-jlBBBef9YjFiHMC6mF8QLgn_Hw3Pb96gx3kInFF1DGblCp400Cx_FHG5MeVTdiWCuBy8Ps6Xqe08jYEvYGgOTdeH7yaSY_xp10s0J87GdpQO9BBeIvRG6vKWmEuy9typ_54ravrRC1haDy2CbrwQUip_Q3DHjbMDpQEgJboMLAGfZBx241bnLkVxqbjVU-HqsEM_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=X0vVx6Y28h4nFXfxMZfFG09Lb9d10oLjW4zPzU3Dv8u3raxMxD-FFR37cC93ZkzPX3uwUaEgTkiOlM2VVDxm6iqZ6MXDV9yI2FqmXE5miIE9DWwAOqmGYNwE4jNp2FVxjUfWcy2xkd8L5ZV2-jlBBBef9YjFiHMC6mF8QLgn_Hw3Pb96gx3kInFF1DGblCp400Cx_FHG5MeVTdiWCuBy8Ps6Xqe08jYEvYGgOTdeH7yaSY_xp10s0J87GdpQO9BBeIvRG6vKWmEuy9typ_54ravrRC1haDy2CbrwQUip_Q3DHjbMDpQEgJboMLAGfZBx241bnLkVxqbjVU-HqsEM_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بعد درخشش نادر محمدی درلیگ روسیه با پرتاب اوت‌هاش؛ حالا تو تمرین‌ماخاچ‌قلعه کادر فنی یه توپ دست محمد جواد حسین نژاد دادن و میگن هرچقدر میتونی پرتابش کن به سبک نادر محمدی. انگار فکر میکنن همه ایرانی پرتاب دستشون زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30418" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e769a610.mp4?token=cUSME8yactxxTEimJkkhWb7ZWkLChe1crAN33vyE0pgSjz4h20OhEQqMsOhQ17OdnNvFJLuXiMijqKL2sFzZDrKfVOQgcwzjQR665RHORxYDYBJakzB2NJntHBdYo7zmQ6iaS7ew6C1W_gTmIv_Iu_tOwUhVha_4nx4RPxwR6_anqU4rXjNUJvVf5XInv1zkaUNRQlfSp-f3-7U-fvZ4aNYtERXLt46YJrFxg2yYCpzE37P_aKZtPgD_Xf0fKEvF-BWYC7PHntMxCqh_DsfF0KxYjJB2hTkq3BY4y5icgRtoGmUBZleg9hsg57VB0X5RjGp4OcIz4YISjGZos3eCxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e769a610.mp4?token=cUSME8yactxxTEimJkkhWb7ZWkLChe1crAN33vyE0pgSjz4h20OhEQqMsOhQ17OdnNvFJLuXiMijqKL2sFzZDrKfVOQgcwzjQR665RHORxYDYBJakzB2NJntHBdYo7zmQ6iaS7ew6C1W_gTmIv_Iu_tOwUhVha_4nx4RPxwR6_anqU4rXjNUJvVf5XInv1zkaUNRQlfSp-f3-7U-fvZ4aNYtERXLt46YJrFxg2yYCpzE37P_aKZtPgD_Xf0fKEvF-BWYC7PHntMxCqh_DsfF0KxYjJB2hTkq3BY4y5icgRtoGmUBZleg9hsg57VB0X5RjGp4OcIz4YISjGZos3eCxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ساعت13:30 تیم‌ملی‌برزیلِ کارلو آنچلوتی با این ترکیب در دیداری دوستانه به مصاف استرالیا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30417" target="_blank">📅 15:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30415">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf0jUM2TZJlD3JTlTh6F5qMG-axZltrXQuhSvNRQW2MHHyU-hBYAyF1UI_Lr8IVGVngNRnvHXVmCX-KoRRfTPO_A_-s4UjWEysj-LqU4rghQsiSiT0rA6LjHC-otvaY4xdB10n_-_3vr5PAalE5u_77Ui8dfO5zPxELXBFzzrdyM2fO0BWhMT1DsrECDqV9yxKVtrZTlMqUISsm6F90OdtX-Z8hiDrBoGsW6IxP_8Rh0Iw-ORWKIvVg5vCOYOEd9R4E5zPpCeC5wHBgFGWheNTMGDh8zsMcocIfIt3uElDFltU3YpFqoCpC2X4_o4DHu87idYu34P1SO8DOpixxZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bo5B9eTq_r_h093rrW8sWxz06OleqakoyVnmczs4dnCHeRtAvAMARRqLx-Gyy7itIlc2ebh-u8YVkkS04K5dQrZFg-c65qHo-v9jY6bcaFmpEN--brw96CfmtFYICJZGeNdq9gjEN0IJ8tdtZIqhIXGlUagccMeMCdCK5MTdCQQJodxv_7ZoRAxAlQCXEExFUFTyIb5rWsuqUQN4oXoCAh7FIbNozUv7Bms3yYvstAUIiiOcp9_qW_UALGJRVYyaRUI8iI76gvCUvwk_J7RSoNthzjhkaAIMFaGWUyC_Wb2awlvvjTBQtm8O9leHqVaMFBYLlgxvV8hv8UEUQdv-Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
انتقال سهمیه بنزین به کارت بانکی از فردا؛ نحو اتصال کارت سوخت به کارت بانکی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30415" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30414">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30414" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30413">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=KspUyXRPcPbXpvyLsizwh21oIkhqlgZKWxuDHAq9EjRtQVEsjvrkW8Esx8oSHjIsoGnKIsMUfBv85mmVMIQbMPyy6hhiVdMOCB3bEmqW-LNPZ8ltfDZ0fH0LxA_Z1g_vvkjs2llKzKOc4CB9Xi6aLrR7Exkg7NtqEd_VVVa4Sjhl-AhpJaViiR4zFFzP7uOZNZjHHnoxCzUpfAu-Nf7ixrF3h0yM2kEo5iq3qnVQnnOXvjR3aBB0EV2of91J_fbFfzk4wpgFIjeIn0mtT-Y1Wt2AptAdImomD0VWWpwblnuOk-k9ABSogVvND2_M_Spp6WL87Aa5ThkP9no9yyiGSpDDebSFt-yxnGcdsYXwtP8Lqh-K-8KXiH4XJXwBIIW58wvhEhS5IAUfYkL2A8asSMuCA7iwXpOU9qhbrG2cF7nfdvejpdKhrlIpD4osCBp5TaZRVf5-NKLZeoUBbYh8RTbN8UmMN005qBxawmCpaD6NBbY34nxObIpc_AXkAikLjuKO54EBJilrRalZIR0Ipgs8A1Vc65R1Y6dCpKIs5S3jsUg8U7I9T0fwcA76KO4vFkmhJnMB7JMhJM5X8AqIFfFK2pWiV1xU7AUwjB_LJzOLxQAvDdRc538SZ4BfsRqO-V2HPcb9fvpaisgljrjyDFfMxkvhw-yf1Zr1Wdk03Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=KspUyXRPcPbXpvyLsizwh21oIkhqlgZKWxuDHAq9EjRtQVEsjvrkW8Esx8oSHjIsoGnKIsMUfBv85mmVMIQbMPyy6hhiVdMOCB3bEmqW-LNPZ8ltfDZ0fH0LxA_Z1g_vvkjs2llKzKOc4CB9Xi6aLrR7Exkg7NtqEd_VVVa4Sjhl-AhpJaViiR4zFFzP7uOZNZjHHnoxCzUpfAu-Nf7ixrF3h0yM2kEo5iq3qnVQnnOXvjR3aBB0EV2of91J_fbFfzk4wpgFIjeIn0mtT-Y1Wt2AptAdImomD0VWWpwblnuOk-k9ABSogVvND2_M_Spp6WL87Aa5ThkP9no9yyiGSpDDebSFt-yxnGcdsYXwtP8Lqh-K-8KXiH4XJXwBIIW58wvhEhS5IAUfYkL2A8asSMuCA7iwXpOU9qhbrG2cF7nfdvejpdKhrlIpD4osCBp5TaZRVf5-NKLZeoUBbYh8RTbN8UmMN005qBxawmCpaD6NBbY34nxObIpc_AXkAikLjuKO54EBJilrRalZIR0Ipgs8A1Vc65R1Y6dCpKIs5S3jsUg8U7I9T0fwcA76KO4vFkmhJnMB7JMhJM5X8AqIFfFK2pWiV1xU7AUwjB_LJzOLxQAvDdRc538SZ4BfsRqO-V2HPcb9fvpaisgljrjyDFfMxkvhw-yf1Zr1Wdk03Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های پیمان یوسفی روی آنتن زنده درباره حواشی امیرقلعه‌نویی و دعوت نکردن مهدی قایدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30413" target="_blank">📅 14:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30412">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guvKtqm4QrBVuTRw5iVfgRaLK8cD2BLtWSTtcHAVGy11LX-i3ZX9ZzoiNU9PCy67XcQTVNpPCDsPeMlS0qn4kBGqBlwnNrQw1CIGoyMmP2qu7do5HnjSfcNHvvSvtZhBx4mCA4V_tw8AeLRzOEQD_DXAmnhA5aAhn5vsrSx4aoz6MhIFOxVfu6AuxfN5VwNw_2Mo1lFkXb7Pi4K-AoOC_2NvPP76ZYK-EF3gwQYgGQlcN3kWQigJ8NX07QOrykcUTA9f9-gvRYohH4fTzkj4qutszZCusFb2zRVR0oMv6G9XJYCEZxf03qSuaTZTbyPIyzbPV86WlCZznS6Oj0AWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30412" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30411">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlgxSV9UAuhnxzRuBEknW-ujqgIx40Sg4_-zGKVMYKqTRpvsUzudHcXAhYxMMi2mLu1p-CFzKOLClsNHifMdE4pMMiGFy4lYhdTA_S3pQ3Ukkyd8L7Lfjw7unEPpf2aS8dn1_eM6jGTaqppziivrO2rtxEaUF3WL6J5eH650DfduNrFyFwOSGGO9cuzI3iIOQkCU-1y3B1lG-rppjyRdTWR3K2vUwu5shqiB-C0qfK2n79yS6TTjgz1WiJVqf8eVxN61LFNqIG4feAsTc2rLYOqAa-Of1sOe0eA9hqIdU_IWzkPiFZnJzyq3EyOiadD_S25ay2mhHKE7tom1sLkbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه سپاهان قصد داره درصورت جدایی مارکو باکیچ از تیم پرسپولیس درنیم‌فصل او رو با قراردادی 1.5 ساله جذب‌کنه‌. مهدی تارتار علاقه‌ای به‌سبک بازی باکیچ نداره و بلافاصله بعداز فسخ‌قراردادش با سرخ ها با باشگاه سپاهان قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30411" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30410">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVPXnbEyWXJukJkSUvnptTP1BmbdnsIkID2UHRWGqKYK562P5XCbMnw2uXdDegtbC5A5g5hl5szvtV9MuQIz63kMyrlCwT48Vi7j7Yt1PgG0sgWySzwZ8qDWCXxm5PJWR6aR-Sx8dFKCYTnE-oOHH3wrEcUrAjxyvIit3QCybzWTvLyajwxZjIsQQhFbPAyPG1cCHx4glvjVA3glhcg_1p2mIulOGCnMD29fRd8WYwbbFxmKMk0nBsamDcukNl3I4kbMTlKr3L9-AC6Zpnb9Brc9x44FEMg_HGVjSl9aWIROlvhfUh74p35r7Sj8K3ryXQu8ingSEKXSNbCvQUEFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 4 دیدارمهم‌امشب هفته اول لیگ ملت‌های اروپا؛ از پیروزی خفیف پرتغال با گلزنی ژائو فلیکس تا توقف شاگردان ژاوی مقابل آلمانِ یورگن کلوپ و پیروزی شیرین نروژ با درخشش ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30410" target="_blank">📅 13:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30409">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyxrXvq08QWydoMzFTCpI4jdIfKQBpb8u7JSIHHQhS64VGKMY0lY7VUK8SzEQk4slM49L7X4BkPq3QVQ1iS4OOdWsC9oa_l8fmH2wvd57W3uLTHaCJ7p0oumedh5soQBGyfyvKC5XKuywmBwh4zHcs6AUA5L87ZvoRjHJdZEJmAq9aLSYluPNTtzUUxeIn6o8lg18JHWufn2kwyH5WlMIMjr-Hcl8sl8u0orqwORZia5RHGWtr0IVflrdHf6c1v_q_Rq0l12sJdnvBypzWKA7Ictd2IDDfQiIsA-7Ny0L7hh5H1V5aqOjl1pyItLs6_GSmIXu5aHyFapf8kXmFW9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30409" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30407">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIh7sztruuzbr6w9J_cJ0pSsgI-ngRurhTGn5V1GM3jsapViesGwiD2RNRWN-DVQS6XQMOnDulr4TunftojczKA8YPzTu-VW-xM4pyGbBJEW1jp4iW1BDzqHBnWZ8m2YQl44-YwazsYFqo_hKr0W4VVgFRK_lltYPcSNT5Ep3tI1ubeqsisu2OAxuoSMRbDTLViJkFmw64iOCD0otOhw1ldDvesE8t-Yn-8OGnJK8LlrEcML3vMXBajfqvAg4VAsGV26L3oPCBHFLtJnYNaCIENIZzDl33uzkHpdEfSzEbeaQ_xstQEjaptLGr1YUm4C6Z2sagJS0qo0wk6QQfw_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30407" target="_blank">📅 12:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30406">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVmpyo2uMECPdinpApZUbFw0YipI_v601Epz39UrYfsFD6rBuHXT3tjb9awlg_LEqkIEXNUlufAHT6mwTVw4VBUBgl52pu6BiPEk6Jrj77v2XqulSrX2-0pAIfkDZK_Py8i4jcLqlZwLiheI55NagUOq3bC8fHrmc2UZe9DMkTPnSUcjXhja2bTxgCBDGs_ZtAUUrtbHZ4r_zRaCxVDKbc1lm9ugbynYuhwhsAdLNvlbWQxhej09QdhWt9DwPOvyziHUCfJjZlSEpRZ-0x7d7DAJ_ebxVDAfah5twZB44B619n5qzQ99b25hFKvigbPQH6cafo7BHQ-rKG9-IjxgLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30406" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30405">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gswMSqz__7e01rfpwCadACuJvO0-jOPVCVHp_7Vk1nMYS06XiC12K-odalcHN2_v8ky9JPb889F-N2ShIZ1b1JzryuCU5IcPZzKUqDN8l3pPi-TF8CCCmiVNMCWJZkySmuKyLvu6sp1l4k7WTi9gEmDR-jZO-vjHQtpBN7ckkPab3s99El0T2rcx9Rrj2ICVwt5614WH2cjq38udLpmsA-Flrd3H_ZlvepaFJkqUnR1I1UAuxTbA4h9Lv1zI2SVBbopuPUT5-54PPHCNAru5ZK2Hp48DVkHP6I1v2ttzsXtoUgtmbtd0DQqSwXC-Skm6lE_BCuJgNJjVLc1s1JtWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ دستمزدسالانه مامه تیام درسوپرلیگ ترکیه 750 هزار دلارامضاشده و دستمزد فابیو آبرئو آقای‌گل سوپرلیگ چین 950 هزار لار درسال ثبت‌شده. جفتشون‌هم 33 سالشونه. آبرئو در نیم فصل بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30405" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30404">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1blkMaZ8TpGDx5__s0w_hXf8_nFW03CpsSG9-UXkhOqDNsP2R3C9qN-4VCpTSqrJb4iZNUu1lNAShBfIPK7q8VgEhrSYMSIsUUiPYEwvs0k0qdKkCRZ00v3eg7heiPbgLkIV_UgtG9cLZc8-zHijH7Fuxb6nodtG6sUblK0uzeG8ft56dyoNqx_PYpmAF2PCecEfmt0jFom3XBODdvPQeF_lcBWNDQgW9BEfJyNZr4zH-9Fy_X4FBeEY7Ev2M0FEhO_wPeb3LXjXmb2ucANZC5aD258W0rFhJIbXCAWcSvvLKKdyzdwofmjC6iJ3goy0WnE1zO8kimllwKwGQED_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلیشا لمن ستاره‌تیم‌بانوان‌لسترسیتی: بارها گفتم بازم میگم نباید تفاوت زیادی بین دستمزد بازیکنان در لیگ مردان و زنان باشه. الان همونطور که لیونل مسی و کریس رونالدو در فوتبال آقایون میدرخشن من هم درفوتبال بانوان فوق العاده بازی میکنم بنابراین نباید حقوق ما…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30404" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30402">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciky19wKEdCsH4otU3zgKEqyxP5k4Y11tqWgSkRBP1YItwNq0PtJkpv1zXHf_MqIwrKb0nW5J5C5pCvOL-4gfprjQIGFljHKVBVNh6ctL1nf-a3NoHQaObcrB1fonxBSqLM0xjuu2BJnuO_re02jtSgfiFE9lPjyt9eojqwNHyU6pjmK1B2Avmwf7PJ87bF_Da2ndfO3NtKQU8Y49cXzUMUxdr9rnoO4N6GTUVwpcOPBbGCGrG2XLWZJt92jKgCrUcBuVb9e-JyZ8V3x6Onxk5O4xgKLQFyizCilHznlbcHLL38ByJSuayockq0Hr27WFHRqlW1imCct6k4PlOjEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30402" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30401">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638f1de447.mp4?token=vX7K8QMvi8bNzNRWawrw6yHZRBfVoqb68G9L1IP8L9KdxSZOlug0jyVcmc4coW-265B_tnhm_u_NyB2LwERxbZYerQu2u4N8MqDhhdKxvEfqCnccbla0n4YELp1SRGvCA0vuMB17XpWMTXeWSgXa5Yua11oqKMyVlq12tnF-jpd8UVlrWO2nJ6TyIEKYG_BxT7UfszORfUlLyZvA7P8j6HbhvASMUNx78z6397m3wodEWkckupvNmFzIJ0xcBidlBMXoj0GL8jlxLORAbvMW8QpEMCmEAZ9o47G8hkKxVb9p7bGfZ2s3x7fMkc9Vi7CLUbtJJaU04yYTlVy0icLJYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638f1de447.mp4?token=vX7K8QMvi8bNzNRWawrw6yHZRBfVoqb68G9L1IP8L9KdxSZOlug0jyVcmc4coW-265B_tnhm_u_NyB2LwERxbZYerQu2u4N8MqDhhdKxvEfqCnccbla0n4YELp1SRGvCA0vuMB17XpWMTXeWSgXa5Yua11oqKMyVlq12tnF-jpd8UVlrWO2nJ6TyIEKYG_BxT7UfszORfUlLyZvA7P8j6HbhvASMUNx78z6397m3wodEWkckupvNmFzIJ0xcBidlBMXoj0GL8jlxLORAbvMW8QpEMCmEAZ9o47G8hkKxVb9p7bGfZ2s3x7fMkc9Vi7CLUbtJJaU04yYTlVy0icLJYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا
؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30401" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30400">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5kFklbVfIuRJGwsFrikrc9B7u_h_cS1mP6G1G0mhzYoBt_RCNXPL7LHV1rNfduMsjKfXdoIT6IeDX1UbnvjfPv_0Qqer2rW4scxws0FSk0-N0dQmKS5INol22-e9XdfTmDH_l7feT0TvBj_b0BDN6BZind60aojbHI1D92aiU3gO0p2cPlms-Wq1mCLJMSpolKaqRUzX5OMbrp47rgYDYpkN1Rjx9hKpWnwiTpf_f8lb9RDlVEKfAaJ6a0D5_DbZJOiXXqPbYheLzsrEqwGoLuBwG0fX0XwfrqTQ4XpLLjsSqg1AogKdh3q55zHAYSfPZ1hgLvJcGpTgBdPNco51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیویی‌کوتاه از تکنیک و مهارت‌های خیره کننده جیجی‌ گابریل 15 ساله‌که‌ بزدی یه راهی بارسا میشه یا رئال مادرید؛ هایلایت کامل عملکردش رو تو کانال دوم گذاشتیم. پسن ریپلای شده رو نگاه کنید.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30400" target="_blank">📅 11:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30399">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649db87b28.mp4?token=Q9jMIn-xgKGgGPAkHGw7sOMT68CaA-B5urGXnvaRQlsLKukRvpQEEMdHkkvFcUCc6t0aE8puM5GvjeLeNeQmDi3VfrD2fT4ThOGL4WaoZEjZFnChmOhXGVa335iuzmBU7hxJttad-gaEyxVX37_BX-QHvxvIxnFULlG3FFZBpxeG9i2era0pZlu8jnZTmR-UJ7ZwgSPXPojXW8POnpXb0Uoguv6GGWTJk9gOET_SoZyxVkMC-UTMZPDScDAgkc14NXJ-F7yslJ9eZ1bBKKloGvbho8oFA9EPzfdE2jXDn0GsKrktmSmaymG2Eq98Mf0cvtmCOQR0hbca1G39NmN7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649db87b28.mp4?token=Q9jMIn-xgKGgGPAkHGw7sOMT68CaA-B5urGXnvaRQlsLKukRvpQEEMdHkkvFcUCc6t0aE8puM5GvjeLeNeQmDi3VfrD2fT4ThOGL4WaoZEjZFnChmOhXGVa335iuzmBU7hxJttad-gaEyxVX37_BX-QHvxvIxnFULlG3FFZBpxeG9i2era0pZlu8jnZTmR-UJ7ZwgSPXPojXW8POnpXb0Uoguv6GGWTJk9gOET_SoZyxVkMC-UTMZPDScDAgkc14NXJ-F7yslJ9eZ1bBKKloGvbho8oFA9EPzfdE2jXDn0GsKrktmSmaymG2Eq98Mf0cvtmCOQR0hbca1G39NmN7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30399" target="_blank">📅 10:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30398">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBD8uitY966YfUIhNvECUNbbP0ilthmMEDf7mVH9OMWcMaFh8aG3yhTxWKOmYCboCLlam9aehlEW8yoUsVjWPteHiiV15TsjzIEarFUajI3CWemusr9m0ZlsBUYk_KKb1EZ-XbznpSSKFEKjAtZpa_FXqT8fTKUNbfZrwlEhkeUXzA4xZI7SDfyO9t4OgLj_dY63GvBp9GfsgJ5AmatSuZyfL6TDWzS1qdZrWIun1Mh_hM6aueXjVWgN4r36z1JWUrG4wqqRIvUgroXWyteXaL0btOORNMLhwTgfd94ZT4ANhfi0jsVDwT470D3CrLt2BAarN8lovvMSRat8oZhClQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30398" target="_blank">📅 10:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30397">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=tbKWp5Y5olzC29hvYT7QExGN4FbST7iqdcmseY71IIa-ITe6VUaR00v7Y-0vbzTIeI97hmE2ywSVFpnyij0hHUo3JcIh1hxS_tr7yg0a2E78aYifFpqDdyD7kyxx9c36ad6hgelXC8k6pKUBl56e8XLBrSSJQdUGyruq5zUxWnzXyssyWZjJ79_gT08-uJgyE2J6t7vegrkjRq8smZYVlibMXv9D02YdrX2zQshCuDtkTuAuPZC3rjdzYRBh-dl4lxLlnPPLwJrVCqiV2AIZ0xGWEqJmtUKKn3U7hnKpnnne5iVo_Ma345QQkmx0mzqvSkNpoqrXHXUAWh-Uhhj1Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=tbKWp5Y5olzC29hvYT7QExGN4FbST7iqdcmseY71IIa-ITe6VUaR00v7Y-0vbzTIeI97hmE2ywSVFpnyij0hHUo3JcIh1hxS_tr7yg0a2E78aYifFpqDdyD7kyxx9c36ad6hgelXC8k6pKUBl56e8XLBrSSJQdUGyruq5zUxWnzXyssyWZjJ79_gT08-uJgyE2J6t7vegrkjRq8smZYVlibMXv9D02YdrX2zQshCuDtkTuAuPZC3rjdzYRBh-dl4lxLlnPPLwJrVCqiV2AIZ0xGWEqJmtUKKn3U7hnKpnnne5iVo_Ma345QQkmx0mzqvSkNpoqrXHXUAWh-Uhhj1Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30397" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30396">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5ZJ0f4FWRM9CU21MaKpYfeiRQstgKbFo9mv1wfs2Lv3aRH3_smIyuHiktymnIqd0DoPmXQE-BF4y5UB7rPq-DE8rpI7Kf-y1XtUaEm_1gGg5bPPTcyJ4wSAGJJ0OcUDvGLCxLm8fGC-jhWPBhhYeyI58cQ_VEEyZicGTU4DtCdqntHJgdf9x2-BuT69t7KPMp7ysHPAj6aKbwYdXDif-95Z2RSUkc_sL3WtNGSGB72cjsaX_fhxcZXNUVLtL5vHAe2M3co0-OIRByQ2gXFzOBozZtfkP9t5u3x7ob118Rg2NP0hQcbrAFHzacV7IFChYTd23B68X9aPwcEnUf--DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30396" target="_blank">📅 09:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30395">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpEIA_HSktP64JmlYBvIY0txNqloHJNXOqCXRPz_HqotIsffY4V_8a--Ypv1EkfMer5Bv6ZO_Tk2yk08SBrQCji-Aaw3ho9Ndl9txGKikd0BK2UfgRcQyXVZagoaE-hvxz7TSkx5mG3vppG2PfapqpvtnFEmZ4Gizd92dipr1kae97-RddK1-bmp2ygYUwXv9aXrDgkDvltz_39CnUTXdbCDvH6H71xCbvlvDF1defic3wHCMdn6_zPDGDYmtp78aTI-byfr5Sm9nhWHnKbnsyG55ntlUHDNutyG_fHJdZojWKZtKPmh1R8Tn1TQ_0YB4MbJXHJogqgnEEEgwwYee160" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpEIA_HSktP64JmlYBvIY0txNqloHJNXOqCXRPz_HqotIsffY4V_8a--Ypv1EkfMer5Bv6ZO_Tk2yk08SBrQCji-Aaw3ho9Ndl9txGKikd0BK2UfgRcQyXVZagoaE-hvxz7TSkx5mG3vppG2PfapqpvtnFEmZ4Gizd92dipr1kae97-RddK1-bmp2ygYUwXv9aXrDgkDvltz_39CnUTXdbCDvH6H71xCbvlvDF1defic3wHCMdn6_zPDGDYmtp78aTI-byfr5Sm9nhWHnKbnsyG55ntlUHDNutyG_fHJdZojWKZtKPmh1R8Tn1TQ_0YB4MbJXHJogqgnEEEgwwYee160" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30395" target="_blank">📅 09:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30394">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeHXsvC1krS8ECiCOdwF4VXxxeJDlp10rDdkqK7UiyQxBE1zgtbzIu9QLoBZ3oLPg0sGyr959AlqDsEIuiabwMOQIt1PvcG67NONpSJv4KXSU2KScwdd5n5nH588ha3u5Kn_QTEeJOTaXz0FeK8yfXTFp2FM63awu814sD8oRCjf_VYkUyr_5J7v_LVGGeBhqlGJmG6RyM4adXaaY5muTqe2zwD2dWYwrOERLF04O1XidkCuOtWDQz5fpwOecdqah2osRN0cL3cL9HCCsGEW7RMYh46CVNDX8xnJuyIB72gFofv2o_tmehuA-Cf6jizMTGGskQCp4adsScC15Nv3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30394" target="_blank">📅 08:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30393">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng2kCW4TbwJpbJi0qWembrtUf__4lG6LTfeOHKOXJp2EAo2H-zw4UC0I9bGd8NtzhiPQbyPPAwLrUVUxyYBPaUBZfa2BVbXPN7h4ZQpPh8W40rXwzNC6bDo0zvx_82g86MKMzgO-9IntbfmwEQHViTQOOp7rHLC2r2ReJixAvYMvxfr-Yjz2Pzr3laOYD5Tfwy1-MIQKFtXuTDFnOAqjMOPdR5H7IRr19J2ySvmCOnRWp9G4UgU2HXDbvb615Dta_ce-7wyUoYQmb6X0VRr9V_8kgL5B6eYSA2-UiuC6rn2E4KGGSfU2fi_ZsDuVoDsyNuvmHKWRliOI_IucuX4hwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه بدونید ازبکستان بعد از 6 بازی و 5 ماه بالاخره طعم پیروزی در یک مسابقه رو چشید. این‌بازی‌های‌دوستانه تاثیر زیادی رورنکینگ بندی فیفا داره. باتوجه به برد قاطع‌کره و ژاپن‌به‌احتمال فراوان در رنکینگ جدید چند پله سقوط خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/30393" target="_blank">📅 01:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=kIOfdHCwCBIADHXBa3vlQrKO8IAiBdZd7NmXY3c0YEYFahc-WthzdVJ3MZcpFD4flabF0NVuyc7ltU6VTmdOu8Q3rS_Knh5F_Bl2kNvgrTRQpb-olARgBDfdbGW6EKLrfymwO13fG_InMZFVrpKo2LknkQ-quV-UEn2YH_gEdk-KpLbAN99xPDaPMfMvR9NNDS2fADGK1pGFUGbbdDh6n9aT7BYm9xpok5dC2HSIdXiUQ50ag8k26CpagdFU4wB7-HfNc9oa_jUnDmP6mFyPnvrLRRdjlyGggg5I9lu11UpduxIfbUdo4i9JedGeA3cSLXDgMUjQiUZOwvBA4FY4YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=kIOfdHCwCBIADHXBa3vlQrKO8IAiBdZd7NmXY3c0YEYFahc-WthzdVJ3MZcpFD4flabF0NVuyc7ltU6VTmdOu8Q3rS_Knh5F_Bl2kNvgrTRQpb-olARgBDfdbGW6EKLrfymwO13fG_InMZFVrpKo2LknkQ-quV-UEn2YH_gEdk-KpLbAN99xPDaPMfMvR9NNDS2fADGK1pGFUGbbdDh6n9aT7BYm9xpok5dC2HSIdXiUQ50ag8k26CpagdFU4wB7-HfNc9oa_jUnDmP6mFyPnvrLRRdjlyGggg5I9lu11UpduxIfbUdo4i9JedGeA3cSLXDgMUjQiUZOwvBA4FY4YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/30392" target="_blank">📅 01:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30390">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_bNehtIAZAelhj8h_Jab1jLJdAvc4B9ye6rFRvRfBd7N5bgyPmjICoMX3XK2HlSUnGCftdrOM0l3fanhNeY6x4Cn-8NphtxJU63IkSjbjqiBSkY7nOIwqxp8zn91Ww7GZBDGNaTJPoRgVm_AaMRpo_wjr19fa2qnTheSE0NScCUIg1HuonzdfQXMSqEqyquQ9aieH_BZFP68FZy-O8Cwy_Sbxqo4vrTGTqbrL05KVDulW-rwhLyKdH4M_7IIVJDZAc6IGCX94i5s_aMwViE-oobuDpptZxc9AMJU2Zf9H_t0Bt4BGyhyw1Y0DYY8QYsoIs_DE3neEA0WxDy0c96dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/30390" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30389">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGP1i5o5VC39FiiM-zZfpTwXVXLd2jYuF5zhR3XEOfMNlcDziOiTmw98AnP0W_Ryk9XyS3ah0kcjHsumr-uDfHkP6ueD96SjBSB40R064eA0kuJhTFu_2O_tqa-P61lAaqgylo80h2Tr2hYdapiL2s9wsXlqQ7ai2s2Jvc1zlIhhLD_-XRyO6vSLUNiDccDYME9ScnAxW5FoAsPFuDgObGh6Mn21a0dqH3I4UEwArHtW3_NHQfSUILhd-NR6A2CEPrnAK_fVLFyOa8QCrXglKn-xEaYoAZ8d8HdEkhk-JHtPPZADCQ35YTZWctaRbisiP31JKtT0cA0Dx5t89OQu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
ازتقسیم‌امتیازات در تقابل هلند و آلمان تا برد سه‌گله ژاپن و کره جنوبی در شب شکست سه‌گله شاگردان امیر قلعه‌نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/30389" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30387">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDQj3xUkcdVyRIq5XtywFFSKfqsY8EMoDuCv89FGEBr8hUUlZT3zg6Wz49vXz85eUhiJ_Pt8Pd7jYRswxDZI9LRANPalrUB_cm0unAhXaI68ZCabU9VW8JRwRuSybF1S-QIv0B8KlmrnFoJF555Y_uWGsRxN-nb4mjq-SLhXhrBMz6-r6mJHHSYw1qLLiVWuDCk5qhYSzZWhFv9W9qAN6_aMx9DRHFcd1GEhfguUX5DlDWT5Nr3JU_Pn_bMSLgTMmzRdFS2kAvXzUHVIfGbnxhMjTlwEN1jZYEgc0W8srJvFyFpIm5OA87P7jr7G-WtHNc_6PN3sWQRN7JAy1Yo73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق‌شنیده‌های رسانه پرشیانا؛ دو ایجنت نزدیک به علی تاجرنیا رئیس هیات مدیره تیم استقلال از صبح امروز تماس‌های خود را با مامه تیام ستاره 33 ساله سابق آبی‌ها آغازکرده‌‌اند تا در صورت عدم موافقت فابیو آبرئو برای‌اومدن‌به‌ایران بلافاصله مامه تیام رو…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30387" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30386">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEIhbqKbHfOHU4pBjLw1On2WQa2gy7GQYyt6aFKtSb6-N-4u6O4iVZ59i6X2H5MF0nIuXq5YvTSs5J3NV_uzHPZWE1zzI09mH8ZqVyVSaKM9ta8V4Vrth5IbSfFnOi8aIM_2SXW5cYnSemrLs_04q_3untGuaLWErJPr8wi9dUwKxRNSREQgPvrqOLE9m8w_rN5kSVYiyISZ8kHwwWC39GPm2SSKBath8Apl14UnX3K4qj_KlTnni-rMqlH5iAj_RRePe8hhKgKSqGqPkZLXRo8UorCDZ7P4Yynq4ybJgpk3ehM16Qn3Mq0jVi2sWqUdMOCVV8k7KEXMNnbzYnfj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30386" target="_blank">📅 00:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30385">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBqjQoYRhX4mjY6LURP3wrYQPb5z0bFoGmMqCHKjmwlscpkDU_UCB62HK_qPi98uImTK4ZkRwJfRkSqxeEhweOh6KNrElBOCqsMoJs4dFAbUB7qHkwl12-YuOcZFFM4_P2W12Pi-gvg1IQCLrUoXbAPMj7gYByFGhv9rC49DktUCSmGlUNvs_bDmx7Cj5HZxlY9pWR_ZrekenelvswVU1KZx34qrODw8IAgOzRvEiPI5Ngv4ZPBhFzgJeVhSdfpDRVwqo9Gzre7vjvglvoW8XXvich6nHI5Kjuc2Uh378zJHz3yrnO8kgMLuPobDEBdO5ESqiYoGfdz9W2UvQpXs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30385" target="_blank">📅 00:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30384">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVoGQnWc-vaQxffVXJmA4i5JdO3Ds6zNBtL3fDLZypXnoQ5xrXOUQCu2gaTUNklmCSALoKGFlwK8xIwhKAt1oRtAfuTbB-DbTq0cABP4pK5SRR4u2oswWaTJtHjPtFLCWv74Ahz3Rcf8NnYyI7ut7SXdmDnFG_0z4mCIBWtzBSEQeYD8fJorj8HezpRN6WG6XVLjh7B77h7tIbbOFsmDEj8DFbg9ileoA8_CCGiNMUIA1oWHMozNuGABLYuXq_wsKRuJ5t-MYHmKuSUS4bjXyVgq6AwMjkg8ihrEcrEGxvoY7E9DhiLSMcI6LUqQ2n3s8OfLv0EZTI_QVaU-ytGWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30384" target="_blank">📅 00:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30383">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYJx5p-eCA-sRla8s1fPHJGpgZclL7bsojlYfLb5syycP-zBqRAWuj_2x9Y5qzyvB1gYeLw--YotW-_NoysVKZrsiCRBK4amlnYc72XLj9wjVyXN_6IX15ycd-niLZ_D_M_0hQ181JZLm7xOoF1G5vp83_93U25EEA7pkNQoGZm8720hf7yXOjVfr7ohh4iIeIOx9Ij9Nx8YEJE2Pxm-R9ovf67iE_soFyrljvaUbsoTA_g87ujjZWzVNDo5Ag91RABW2jaG5MAtY3P7_MWWEUHu3KlFsjs4IMf7ucSsLkQ9S0wjPg1BGIFYogb6_dw15ntOkqHRdiJgsuPZQCUieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30383" target="_blank">📅 23:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30381">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=WQBlLjDdyXcDieY5ID1EJY8B_yA9Kj8S4YPgGbBz3HFhlq-JnSbPyH1P3uktjICvhKMypyZdGDchrnD9lN9ve93vdQSCHKjCQfFjFuQkg-friEwR1JVZyuuF4auOLJ1w-KkgQpdgHw4KtDaKaoePoGvHCeWGn3dxoafbpcoEiBD1_un9gYTuD93-VHe8fBr269KbkjFE6l0hO-859Ad6Wr1YQHaDoW3FdOlfrmmss2iB4uB-pvvibdpA2I86jQjZ61G_AXAJA4Bua8TkcWX0QBA_bmomSKnBRvZk56In6TvZBQtxc2txwXEmJYBK1o47VsEshI9jPVne9I_tfFmo3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=WQBlLjDdyXcDieY5ID1EJY8B_yA9Kj8S4YPgGbBz3HFhlq-JnSbPyH1P3uktjICvhKMypyZdGDchrnD9lN9ve93vdQSCHKjCQfFjFuQkg-friEwR1JVZyuuF4auOLJ1w-KkgQpdgHw4KtDaKaoePoGvHCeWGn3dxoafbpcoEiBD1_un9gYTuD93-VHe8fBr269KbkjFE6l0hO-859Ad6Wr1YQHaDoW3FdOlfrmmss2iB4uB-pvvibdpA2I86jQjZ61G_AXAJA4Bua8TkcWX0QBA_bmomSKnBRvZk56In6TvZBQtxc2txwXEmJYBK1o47VsEshI9jPVne9I_tfFmo3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30381" target="_blank">📅 23:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30380">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCfEKV6i-4SVkQygnf06_AE8CPpf2BBjIVM0in5Z4t6K9Mv5OifIxB4PRM_8sxv28W4-wnjyK9ia1A3qlDuSW_pdm4pYn32zgvroxBqkoaGdpLFsvy-QQsfu49MclS8kmRQquGVXdZEYsffSL1YzTOVoWWWqs9LI9-Ejj1hP8PWRWjtQpWGsaMv3LhDEwIUme45xxyyuBYPTZK2YBV15lmLc9nBK_lBjSE1ZIc4O6wHpzfa4XGGLqZLDNWqYh_T6N9VWsXRYMo0wy7Izs_rGdsvwvSjMDBknT0ojQbFCmszVEihc0D023DqjdrerdyfDMO4r-721rvjYpX0lvzmYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع میانی رئال مادرید از ناحیه رباط زانوی دچار مصدومیت شده و ممکنه چند هفته روبه دلیل مصدومیت از دست بده. مدافعان تیم رئال مادرید در حال حاضر: هویسن، آسنسیو و رودیگر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30380" target="_blank">📅 23:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30379">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcbNRzm_f40aP47mNvCydAiEM8emCVfb-WeITn9MOop7jSyNq4b2hHrjcs_AsUPqqOytLEkQMWD3_4TCI2WmEgcZWMJusMCDt2lRv1AvVMh8tuGQ6mvw9zJEK8xKxKOuI5yirUR0PTvODxaShgTFVqpwQ_04YNoh0YzZaNCbfhHy0g-9vimYJ9MqJI-p40sbvYB2wgXPZYQoSq3ob_-rbxWgr0HDcEBvkB3g5YI_EuyQh6ttDlRHctQlUQE0KcUXtTab_-KwPdntPxK2LpXc7kNmU2VHCDL_gOayvWjKFvdxsw5zUQRvgYmRgzejnW9Y2jPx396DGCK9n-EGarTf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اختلاف برگ ریزون دستمزد مردان و زنان در مستطیل سبز؛ دستمزد کریس رونالدو در النصر 142 برابر بیشتر از گرانقیمت ترین بازیکن دز لیگ بانوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30379" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30378">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7pUZXPx1CjpKTEnxYnJpwPYrzJS9XNrHlrQv4bB4r_HjklXvgCfLh8buANdGJRFNMpnRTvHvp0MEF9fy-hrhHrqP_tL8tFhZHsV-EE35MHaGuVU2Ob7L0tHfDSoNyRP32SsIOIn13iXUxmiwdk1Gtsihtx_VPJS_kspRoDWxE1QpXK5vr4MHy8KeEmrqLydJOeUV-3-iTwVlBm4o1N20yF0xRdmJBQ6e0HEMWYV5utSSqbgVTuCCCO7JkjFjninHuKrgR43WPvHtUcOPP7W5b0_qDkaLR4xiRWQUjtzZzwRs70Mfgo3QYktlWRkdKDcx85QY-bXIONDBqNNj0ZylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30378" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30377">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LS_v0frEIJWoy0D1h7fS8sncelrenGnRPnuYzIf8qS11kcQklY6HViNp6Vu1p1Xg-OzMebZIM5eqeneI_xLH1eBI-53Qu4n5IgeYbOH5L_AoUHsiMSSdUd73kAtXN5J_jjuYGoKx6JJnI32oIRZ2S6YyIW8lo4GxfRVlUA1VlHbQB6pMC3yp9WQhTVsG0mBEJO9W_yWCMhej0ElcPuyjQ42RuR09nRQFKxiwg7_GjWiIlvvzYeWh8OWBglFcoStiRhJNFr8dMQCjjivLjI7VDLfj8RTaJo0TDhzGI-EYMki4QrCoyCFwaL1yjOvK9HPV6dPlz24fVc0JVEl_WT_u0t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LS_v0frEIJWoy0D1h7fS8sncelrenGnRPnuYzIf8qS11kcQklY6HViNp6Vu1p1Xg-OzMebZIM5eqeneI_xLH1eBI-53Qu4n5IgeYbOH5L_AoUHsiMSSdUd73kAtXN5J_jjuYGoKx6JJnI32oIRZ2S6YyIW8lo4GxfRVlUA1VlHbQB6pMC3yp9WQhTVsG0mBEJO9W_yWCMhej0ElcPuyjQ42RuR09nRQFKxiwg7_GjWiIlvvzYeWh8OWBglFcoStiRhJNFr8dMQCjjivLjI7VDLfj8RTaJo0TDhzGI-EYMki4QrCoyCFwaL1yjOvK9HPV6dPlz24fVc0JVEl_WT_u0t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30377" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuQaArC7Sv_ksnSdZnXUWNL_GG1UlkfzoSAlVoqaQww4zo9NyZly1ZYcY1QnhooZr5AuNZwe_hMB1Rc-VXbS0QJOE-kfeI6nbUPM6s-CYEdPUduLyq18AEQDwJ7C6sW5M6xMNmYOgn3u9hNDWbQh81rOceZQLhYwVaSi5DNfG_LpRtMgBZ8M108KRdrilQZWgzCXB1Qg2YSgp9gIuJL2GtatZ4As4XsrUBHW72Se2l-EBzVH_UfWVx0Y3nowPVQPu3B0-DQnyJ2ZpZJp3-zuInyKy2i5JBOvUl2CNko5voKpzVscaYjI9pn9TgTv1KxnYpVyxKQzheqwF1Rxw2EtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mzwr5ZiPbCsC0daGTEqSDVKT9iigy3zMO8StlL-7vbX1V8yoKx1U4ykD__OJnLd-XHcSh7IHjF5mTfrClWrodktcQ-EcUdl4JAO0bny8MebrVt2R3K5_yF7cPrTtgQlim3FPSNqyJtvH6-MgaeXsOjBxQqDHoFwTgb9IMKwyzDfKu1FgCSizdEzjwAJj7cGj0G9YlkE0--HJsfWRjaGh61nQHQ8DhuA9-NOVN6DRfk0cwHWFB2aNHLadqgxqhpbau0tlqgouRITUwt6YTYnXU9cIfit2_tv1GMHUwcNMMHCFy5BdEK5U9etTGm3_LJoWBbyw473IzkHWPtQ5xyvUGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30375" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxcibcPWsgHmVBrHPNsAuoa3eBdhgV24gLYal6dRyExLj37XAsQ1iZ-EnGCZJyqdHdVNtAaqKSyZCBBCYOn22U5titW0IQp3mlv5IfhuXnfMsltPFTDBB8tBkz3Cl3LzRIYo5wuzG2zBFG7PXPZM5am8RubcAmsh9jjma9q5isdO4bsOr10NF4usCHsPrwxUsTvmKVr1qdNHPZAUDJ_Yr2Z1iv1mBMtSiLlVXJ1Mz4nliVIBWIusT8a53DwOVR0fjQu2tswMsXF5EWp08u32fhZZW--D6mBnHznXXo7kbwwiki4PcZTUoQ398wfLjIGtxwGAXWGurg6u0wj30rvqVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گزینه اول باشگاه استقلال برای تقویت خط‌حمله‌آبی‌ها فابیو آبرئو33ساله است اما درصورت عدم‌موافقت فابیوبرای‌اومدن به ایران در این شرایط خاص؛ گزینه‌مدیریت‌مامه تیام است که‌رابطه نزدیکی با حمید مریخ ایجنت یاسر آسانی نیز داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30374" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30373">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWoXIClakIaZ8KTonmLSKnMV32kRnBzM5lnBlCItGWJymue8YrxCb8N2zazJkKXUfBuYgXT2DFjAFMHh6z2AuddfUcs8hdbWxFK_tumuniYL02Fz_AFgGjvNzj3S5vM3RNOK2d8lO7w2nKl6cbDlVSqAhyaiXyxKDdBUPoHg7L1RxrMwL0nqRC1wgdT2ylimL9I5D2YnBsjLYUEX9zygiSLXEqrokkyTwytawHwG4YMjkHqKM4amXjgARVNdVtKLdwu9xxRGzaUnF9lUa609UUjxg6TFBJh0mWr6r_vb0-1hoA9hn3C9O1zqYwAYrlDzrQ9fR0Hl00eBMFm3qXK_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جذاب‌ترین‌مسابقات‌ملی دراین فیفادی؛ به هیچ عنوان این هشت مسابقه دیدنی رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30373" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30372">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏀
پرتاب‌های دیدنی مژده نظری ستاره تیم بستکبال بانوان ایران؛ با دوستاش شرط بست 200 دلار برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30372" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30371">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30371" target="_blank">📅 21:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30370">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
گل‌های تیم ملی ازبکستان در بازی امشب مقابل تیم‌ایران به این شکل زده شد؛
گل اول روی پاس گل دیدنی احسان‌ حاج‌صفی37ساله، گل‌دوم پنالتی دادن بیرانوند34ساله، گل سوم فضای خالی شجاع خلیل زاده 37 ساله به بازیکنان تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30370" target="_blank">📅 20:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30369">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6fDKooivwB-HB8lv_ZpXYWDn-hc3WlmQRRdj3hGLiEW4VMb-vbZMGHM5izxObNySbtRsZuyKB96gcPIbJJanYyG8Wb4jdusfJBDwQTQqMDrtFgpctD2R-0qhb6dHuhsbHpt3uJUfRjqiOXEg-aKB1Un-p2e2f-aStw1P0GwDvOSz-By0W1OM7b87m2UNTGUAY2gB8Mb1oeHGN0eSi-1-Q75x2ju7VtckCfV-OyjACMfiwWaHVcxtyKSPIDFpJu-suPGN3GcWQKp1vcDUu1vWirAm3TzxhPUC30L3YKtsWc4vH80uCJLwKeQ3e5qtU9i-Z7W_5IlY203XmTGjcEBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در روز پیروزی ژاپن و کره مقابل حریفان خود؛ شاگردان قلعه سه تا از ازبکستان خوردند. این نتایج بازی‌های دوستانه تاثیر زیادی رو رنکینگ بندی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30369" target="_blank">📅 20:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30368">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30368" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30367">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQcjpsR7wz0HxH6fdoztg1gpdMY2bwVaHjMvR_EWjcXc27wHR9wP7X93lc-wCYIb7Hu5BkiYPiLEW8WHfZPrcfOs2KWToo3Fz4ZwiYfLZ6McJ5JfaI5Gql6rtVMfrx9-W556lVFngTh78FQowtKaNxJ6dHRMnqOIppinfQvLX3Ce-XDHchZUDyh2dDCO5Bv2OP15dxZPcdrNljtlCqKdO-bPfavjHRXYUf60MW-uyLIypUK47aLus4yPdFQgn2ztXqQ2U58aWjD35qphcd7XcpQURsJks5G2D2To71GwItWHV2ELHXkSJMnjJdrz-kxtUupwVUUxbUfmn-rycG7AIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30367" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30366">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEFe-oJ3WMJsJSWyoMHfdNUXEAEwkZoy0GADWaZxLI9VyM8kfgIFreKxeJimZhRC8eirxu9sDZsZe_eiyvl2DKW8uE9FpNdJvEK1jgmi1ggcHlj5b-eq7y5dbk7X_dcvsQA7aoR0G34b8WHpjTo1V3Ag6v4qvNGowuAuSIpsVdJXHM6A64pJgQMI7cZYvaPj0R66TcaPWxoHNYsTiDWVoqa3ltNRcub84-YD1oTwXDKksYmmnrkdTFUhgzsN_AGa2OdyawKBC8S-2fqylOLHWTcTBwBMhR6U8QYAZWvfiU7Z2S0qb8y0-odkUAgNCT4sWS6NVh1GVo4BihqBkk_Wzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30366" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30364">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfuOgmqrX3pOmm0cVUqVEuNpSZ125G7GKD9ZFaeLo4kH_BOh4yUEoRJu2LPh1lxSQKoxqX-_IxDIQzuvec8iVlI9ewCUZeRxz5UQ7nsP6xFKdwnjTpg7LW9yBW0pMYVDOXOQoolW1fk700zqLsnra1XELan0gklslNdBJjQAXmots7_IGQ4aJAVAdOvA1VN6_090qJLCeiYAIbJbSUcLR4bgS8IZBKqX88fiK3lBg_G5_wXdWpFv24ZgTfUoMVLF6GM0BGTM0asqrR1hoNdpv-3E89sUyW-I_pWu67VaEZXWrbl7Ujuj6F3RjjRL7z3b1QAc4YE-iOo58RrEfzpRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
حسرت ژنرال در پیروزی برابر ازبک‌ها؛ گل سوم ازبکستان به ایران توسط نورچائف در دقیقه 95
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30364" target="_blank">📅 19:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30363">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=goBtxFKldw-p8eMUgU6jkv0xR5wAFsAS-gbMXxIwhwz83Yta4Qfz35trH6p37TEiL4lcZU9NngGSErJ1yeF7-Q5Wo-3TxxUMQFtisRsuUWGipnXUETAfaK3ITbmONtIDZinUqYW4_l-4Rh_LqNJWFBCFGOPG6TaQZBB3_XvYc6qeUFgiWEDAHN3ogdPpl0HdwFsB4L8UEdfJn7tHJynr79OvrydPmxjK9vF3mA9XLvXreyQOwTBNPza5Zm7Eda_r3rHNwoYz8p01M9RAv2sQqjzb9oUmMoQUHUiFVuxRuUJ44serCcBkG3jyWjst7eN0iNqf691Rw4HhtDyCIVsqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=goBtxFKldw-p8eMUgU6jkv0xR5wAFsAS-gbMXxIwhwz83Yta4Qfz35trH6p37TEiL4lcZU9NngGSErJ1yeF7-Q5Wo-3TxxUMQFtisRsuUWGipnXUETAfaK3ITbmONtIDZinUqYW4_l-4Rh_LqNJWFBCFGOPG6TaQZBB3_XvYc6qeUFgiWEDAHN3ogdPpl0HdwFsB4L8UEdfJn7tHJynr79OvrydPmxjK9vF3mA9XLvXreyQOwTBNPza5Zm7Eda_r3rHNwoYz8p01M9RAv2sQqjzb9oUmMoQUHUiFVuxRuUJ44serCcBkG3jyWjst7eN0iNqf691Rw4HhtDyCIVsqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
🇺🇿
شاگردان قلعه نویی دومی رو خوردند؛ گل دوم ایران به ازبکستان شومورودوف در دقیقه 58
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30363" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30362">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdT1ifimwEyiMX76gFJbcFK_x79-59TmniP2eJulQSMmzxClie0UCQPQgD04uWV05dC--A22SRwLY-LvoIgPxkBo_6LFzCOY8pka64KPtUcxT5zol76M7EccENGbL6VzlYi9VDlAJj4M_MQpanf43Chtm5P6modljTH_eaHHdGinVBod80gZTAZ98d4EPzD4GGiok8KcTXUI1TiC4lKgZh_vwBd8hZCqs-Ud_omq95dnnHJcVRVz56Vp9p6NgNJG_gP8vpoMmhfCCMLFYudJo4k6abexfKAZD-hHQnplqkpMdvvjDcUMqvGLx1XXomProCWcZOI8H6ndBTXZwwdIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30362" target="_blank">📅 19:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30361">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401621b710.mp4?token=iknlnxuYHw-4zZ-CvGN0PSlH8kFRwbEpNZeIgZuMc0OdKNjO_c_8_UlL13B_ysZopA69DNeL4aclTNi3PAosmKxz8cRx3SUheOcNgD1DKfdJuDEAQf3wqVQRHnew54FceIniw0yfvWOP_-qaWzlsXh5LmED-JNBMiDhCDoUFjic1U2zSk6sEHFS9QRhlmcxbEVqnaXZhV0zIDquKkoSF4ushhvOje51teQLRh5EneWlMVsZ-ZN6WuwWIHKgxjzVxxu3x0ukdL1mOQi-fxCaGxWL8fYow26kC4KaJz_QhziGL1yj6VklkIQKjpkz98u37A1XUmrHF2b3ZY_3fNSIM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401621b710.mp4?token=iknlnxuYHw-4zZ-CvGN0PSlH8kFRwbEpNZeIgZuMc0OdKNjO_c_8_UlL13B_ysZopA69DNeL4aclTNi3PAosmKxz8cRx3SUheOcNgD1DKfdJuDEAQf3wqVQRHnew54FceIniw0yfvWOP_-qaWzlsXh5LmED-JNBMiDhCDoUFjic1U2zSk6sEHFS9QRhlmcxbEVqnaXZhV0zIDquKkoSF4ushhvOje51teQLRh5EneWlMVsZ-ZN6WuwWIHKgxjzVxxu3x0ukdL1mOQi-fxCaGxWL8fYow26kC4KaJz_QhziGL1yj6VklkIQKjpkz98u37A1XUmrHF2b3ZY_3fNSIM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
کاشته دیدنی ستاره 36 ساله ایران؛ گل اول تیم ملی ایران به ازبکستان توسط رامین رضاییان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30361" target="_blank">📅 18:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30360">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=Yl4DsbBkjgdI8kikt6_pWc1EuEpmiw6W8mLQHOzKa3G6EOqoN_JMZpdDt0QfPYYRjl2PztZNkjfAlE_TvYZvfBipKtyh3hsc8tpljCGOcdn04bQeM-6_jpHFJ7ZAeijxPyZtxvGiGRhgaOpQpB7q7HR7C9EDrpzcTsitp4bzc3XV15qaMnxehD6SkzTbyToielfZeDbonpaoadif1V6vE0b7xo__kJrZCRMnA3dyOD-LYZeQQTpudAeiz-ZRzVhxl3a_wx0se90kYZ6DBj5UYqp871ciemuQl_K29vmOp-j4Qx9oEb-Lmnb7oisofgyL0Q958hgkWEUcAkM4wpJB_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=Yl4DsbBkjgdI8kikt6_pWc1EuEpmiw6W8mLQHOzKa3G6EOqoN_JMZpdDt0QfPYYRjl2PztZNkjfAlE_TvYZvfBipKtyh3hsc8tpljCGOcdn04bQeM-6_jpHFJ7ZAeijxPyZtxvGiGRhgaOpQpB7q7HR7C9EDrpzcTsitp4bzc3XV15qaMnxehD6SkzTbyToielfZeDbonpaoadif1V6vE0b7xo__kJrZCRMnA3dyOD-LYZeQQTpudAeiz-ZRzVhxl3a_wx0se90kYZ6DBj5UYqp871ciemuQl_K29vmOp-j4Qx9oEb-Lmnb7oisofgyL0Q958hgkWEUcAkM4wpJB_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30360" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30359">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRjkgzFm5shUIIMRyzOX4ZVrwL6VvS6cXoM_6HiGQOF65UliQ0XO_Jyi62cVDl06y9XJr0Qc5l8fx3fURmSgdoUnBL69Wkh3mqdhRzlG0ib6I10V6fikB1yqhge7p2HG2ukaRc32lKdMOTZg_VYmLjwkCahgaDqL-xo-gXwiZgIpWALmExaU5qv9uqt86283Z1GkUOtRtrd0wCvV765TDpuZtHgj7zSMWsWL7uj4Rnqwc-UuQdY95QoazUOyLAFR_PwhtV7GxhQX8s43yCqa3KIyyIPzyBl34ceABnzq0QRNsTx2Cfn7sGdrMwQGNh5aSpW1y1vb1U4rVo7yxoWhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30359" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30358">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=twU-QSO1tD0H2CyanOkwW1rMHRtT8zRuKn72QDosZSuMyA5EZIkjuY8SVzgV7OhmsamwTfeNUImEPsh5RBTdXeZsWtplg-wSSzwa36e7tCMpguhYX3aFHQYDo88LTwULcgLeBsaoZPk3pC-ZAHAVuKpjCvGw_h3qbGyClYxafC2wqkl-ZMKtFaUaifz_JM12PxU-uVLoOzxSMRl0BpEczkVE9pfVEDD6xEHfo6rgtuAFNY1lJvQ5a01t_BVE0KQJJVR9K5NaYGFczMJRCIilDr6RFLYQINHA_EYHSVQKhCYFRreGWyRuO4xHIhy79hYVDkcK8kfz9R210IuNQrRugQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=twU-QSO1tD0H2CyanOkwW1rMHRtT8zRuKn72QDosZSuMyA5EZIkjuY8SVzgV7OhmsamwTfeNUImEPsh5RBTdXeZsWtplg-wSSzwa36e7tCMpguhYX3aFHQYDo88LTwULcgLeBsaoZPk3pC-ZAHAVuKpjCvGw_h3qbGyClYxafC2wqkl-ZMKtFaUaifz_JM12PxU-uVLoOzxSMRl0BpEczkVE9pfVEDD6xEHfo6rgtuAFNY1lJvQ5a01t_BVE0KQJJVR9K5NaYGFczMJRCIilDr6RFLYQINHA_EYHSVQKhCYFRreGWyRuO4xHIhy79hYVDkcK8kfz9R210IuNQrRugQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30358" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30357">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=KK8EBkAM43YkT7DsUF1wf6dqAAvAxa9kJE7eNUCZDYPod_F2Z5T6rBBYWUPe5x-SAkyWqqlBzpHqB6dxmNamKJm5G9rnGHZFIQVOLNgC5VSA1kHnYNUmI-JF_7pH2UdlZNciqu3WCSvjMnIUWORbqX-12_r6ANThq3QN9z7RP0wgWVgGqDPjM068TZlKTXm_XL-CHH7pwj_XLYvyhJNXcIGAxtforvCizjntJZ8bS4CY2ZBCqEXZ5Wo1EDv9W_EGeaIeR4uRf859AwmyDeO3cdykFrxKPAyMliNSVhq1hMYPGhSZ9J54WLo_3JYdqcDz0mEbTyDvM3KnNmk5_C9V6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=KK8EBkAM43YkT7DsUF1wf6dqAAvAxa9kJE7eNUCZDYPod_F2Z5T6rBBYWUPe5x-SAkyWqqlBzpHqB6dxmNamKJm5G9rnGHZFIQVOLNgC5VSA1kHnYNUmI-JF_7pH2UdlZNciqu3WCSvjMnIUWORbqX-12_r6ANThq3QN9z7RP0wgWVgGqDPjM068TZlKTXm_XL-CHH7pwj_XLYvyhJNXcIGAxtforvCizjntJZ8bS4CY2ZBCqEXZ5Wo1EDv9W_EGeaIeR4uRf859AwmyDeO3cdykFrxKPAyMliNSVhq1hMYPGhSZ9J54WLo_3JYdqcDz0mEbTyDvM3KnNmk5_C9V6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های‌ بامزه عادل‌ فردوسی‌پور با لهجه های مختلف اللهیارصیادمنش‌فوق‌ستاره‌ایرانی لخ پوزنان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30357" target="_blank">📅 16:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30356">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMAI3wj8UCvPGp74KPISoL73TkmcDx9Pkk-xz6u7gZeElSsdvNsep3P4CRB2hLBeHefMnBqUZc2pFoj9bJCh5zljnrO3KR6Njjml030rxQYLeEQZHfOyTAS4dDkwgRug0esajyz_KkmizhVVtnC1aO7ye9YrnCSv8sKIhLKJq5uZFiqUWTPlncFtbBX3Usf22eSH2ZM3HeSd4gGrgUiRYaGooodJiRxFV8OCDZ5QeRY3cqlc7LTbnTJ7eX6If_1HEwDenwRSQpATBjQ1YVDNtkwWfBWqK6f2i5HfgCqXY8LegWbJQqDm3C4wmx1fLwQ6gR-IcnRJbjZ5dSFITts9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال قصدداره که برای پایان دادن به حواشی پیوستن بیرانوند به‌این‌تیم؛ قرارداد حبیب فرعباسی گلر28ساله خود را در نیم فصل به مدت دو فصل دیگرتمدیدکند. محمد خلیفه دیگر دروازه‌بان 22 ساله نیم فصل به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30356" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30355">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko0h_WcLKO9jzRAXBIt9ACujZoCp2vh8gC9HEVsc_sEJdug-VnAddZyyOszp4QAAfqck1ZJjK03_2nmFKPRyhUgZSjC3zEQh2ga5j-08bcaxQwhuszgAs8o4d83w4J0bspJuLYwSFDGSRd_E33IfAPjvGSuKNJ0mT3_1foRND8-L0_y1nY-W_YXr4sOPusWIpDQRY6IrqRBk6ZW_gmir1jqnUknBuB6zRIqReLA5LxWYj35M4DGqVwELeZ6AJIyunGkhz6drMZWSaAx8PZ4hzP_sBNeN5-4X0GmMi_D-GgFH9263AWvvLDEKz5t8gHVBFiLZst-PKKjhiK_m3QI6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30355" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30354">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=dEm1TI-JzyUHwwjzoZX6WuS4Zs8XWEMZhCsm89fgYgKtwOnwF6HDytG36o1vflyxOK0ez0ln3QwsxDSz5-6L2URhnS4gjPdT-EWomUTsmOPWEuw6z8gX-FRcRLe9ViSlrEQKkJ1o_lwZbUiEFXdAzaHLb2y3XH3almeOJa3H84M7gIoJRcV7K3e_h0MAeblPwFyHbAqmAbKeBFUN5PfJZQXjDyLFwyvfzaBPfM74rF_drU0wPFyECYa8XFi5ENlLKPZBtie662hiJ8t7npopgiGugBotrGSGiPg7gdPKqqpXzmtju1e6_AqHe3UroR_DcwxojdR7njGTHLx27dGVzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=dEm1TI-JzyUHwwjzoZX6WuS4Zs8XWEMZhCsm89fgYgKtwOnwF6HDytG36o1vflyxOK0ez0ln3QwsxDSz5-6L2URhnS4gjPdT-EWomUTsmOPWEuw6z8gX-FRcRLe9ViSlrEQKkJ1o_lwZbUiEFXdAzaHLb2y3XH3almeOJa3H84M7gIoJRcV7K3e_h0MAeblPwFyHbAqmAbKeBFUN5PfJZQXjDyLFwyvfzaBPfM74rF_drU0wPFyECYa8XFi5ENlLKPZBtie662hiJ8t7npopgiGugBotrGSGiPg7gdPKqqpXzmtju1e6_AqHe3UroR_DcwxojdR7njGTHLx27dGVzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛ خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30354" target="_blank">📅 16:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30353">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30353" target="_blank">📅 16:12 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
