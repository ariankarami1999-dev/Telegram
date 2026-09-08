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
<img src="https://cdn4.telesco.pe/file/afKLmoGvCp62j475DquBz5TFPkWJ3Ds62RT2JbG7yiCwIjyBGedNI4i2lh1-Ne5nNUvDYXHaUgFrCg-LE11o6X4hSzA32PABk9XG16L_UK0NlXWv7z2WniEpZqGUUv4is-EOfchDBmt46PgpBNXknUmNeyRhv_tNGQiwq3i1jlSVl8f0uAqjogfzje299xUj7Yk7YVOg1EpiENK_fEeQUOjUhnyl3oFscU41Nbe1jQzqlty4tBj_CTKKuaSEyX7YpPBKTljDf4IeCY8CnDTEtxS52sSjNl-bfQfc-2SniAnY2SRzjlnNe9hpy1WwBaSJTm00daFGuqEm7eSO3K-exA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
<hr>

<div class="tg-post" id="msg-71275">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo1PZwMl6sciPATxoUl-K73zx6kzp1tWgKJRlCoCIGc2fv7kxeJQIAx3fOUd5FjQwHjKpwqEjc1LCoVzX6ZnjOVbfPYcnIYlq1gpTwNSk-KNK4Rf2wxcXw9Y4YQbF3gGEBZ93WDXiPnBFj08Uo9RU36CfEn8fyDOhKPndelKDOx-iLy76z8gM64Wp0W2vaBqpv8CZR8s0j46mt_YN7EQ7GulOsz-cuYGXooa9Awz9Op9p_YVigFEBsg3dCfMIrnPGmFywQfpw8pPFcknxk2vG7S0acsx5itqpS1W9nnFvdhG_MIrHKwHS3U3M8J8pKFq7DbJieysMVKbLf3CghVYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است.
اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/news_hut/71275" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71272">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LbhQKvLJt4bUL2hV_qdnlYTMPBqbs6jOYsfVlf3yO4LiDk0-3knNMYhaMvH9zuKcsm_HQ1FkFCNc3Ksmu8I-9EV0pJ6bR1ih56z1kdqQNW8cfSRQJkpR8nSgBn0fNR51BH8WbFoYRueVuLwoPI_tkeMIDx2pv9WFp5U7NemKaWutIk2SRG1WJzx_RQzW5slsfVRrR-sn5PrGRJAs4E0WE17wj_u_3nMq8Kv-RpiwFZ7XDF8jSnUecjLDBNP6X0jgCCI7fqTlBdcxJrjbWboX83c35Ghu3eeXt8huBTxdvI7gJ5ayz2av9oLw8tFdob-PISAkGYReAHQWvsfpBfyyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8833895957.mp4?token=Cwqq6tYAGGludgiFuzKZWM02pNhmkNyvEe0YY6BGloxWmaiELuxsGEsHVM-kt4FULghQsitc2y6ByEbItvLRcJKSrC-7nkgTm4_9IgpmxJhKiCCYx25HWKdsMNrhHhhMr4LiQ8SWir22Jp0QcEl5eN_psufU3QF3Weeef9P-fF4dBMfnZVkwmzBIF7hjH2Rbsq3hs2PImik5Zn4d0YrZsQK1QOnqeIJmKlY8VYULNkfUjoKWXyVDd4G3RV2qk_rcl4Siy4MfYOdSyG98p3Ch-8nVlXX5BQd8lLHjYdPRiu8KYpHDfk2LHDc9jt1rDIDFSkcRRDYtSrR5-xUOEfqp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8833895957.mp4?token=Cwqq6tYAGGludgiFuzKZWM02pNhmkNyvEe0YY6BGloxWmaiELuxsGEsHVM-kt4FULghQsitc2y6ByEbItvLRcJKSrC-7nkgTm4_9IgpmxJhKiCCYx25HWKdsMNrhHhhMr4LiQ8SWir22Jp0QcEl5eN_psufU3QF3Weeef9P-fF4dBMfnZVkwmzBIF7hjH2Rbsq3hs2PImik5Zn4d0YrZsQK1QOnqeIJmKlY8VYULNkfUjoKWXyVDd4G3RV2qk_rcl4Siy4MfYOdSyG98p3Ch-8nVlXX5BQd8lLHjYdPRiu8KYpHDfk2LHDc9jt1rDIDFSkcRRDYtSrR5-xUOEfqp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌧
بارش شدید باران دیشب در رشت که منجر به وقوع سیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/news_hut/71272" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpx8DXPSQWHpgP-SRMh9Rj6wc5foCq5yT6x4uYrSVnIuOvYFsqoUAc020kF_26iWckTFK_Wxl1BCrO7Xo3KsloRDZHWPFV1ucEbFtq4cduLZF12Pk7zYWNSbL0spb3KEqhV2dJEDO-fN3y8KgQh8uNPN1WToAYtu0L0Pa3aQ7L650r-P7UsqNa-8Mq5UzLopEMhcBJexyuLVh9JJb6iKVKJWmIjilI16NHCZOyQydpHpHCCbASsUXaWm5jbta81k2VoW7wJXIhullC-cIe1UjJF-zS0z__EChOh8J3pZqFpybKOqdAiHMUo7nXFVfhfdnCUbBbYhSRxxGbt9etx5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=r-lRlHreGCYQasMQjkcgsrRNENaiGw5LDdwW8zBY_RMLVyU34UoweBUK9gfyBuAvIopyIf48zkax2MXwR4RQvs8VuqeDvhDbU5rx337LFVw98Okal0RxIxVyxmQ2N8HtY3w9sGPVspbpXHJFmuifmSt-opZwNnUlI-nR9xqIfurpZpbpxqjd2JUtqkR-sCgSryhySBBPr9R6455cCpf9kAy_P8Kk_9a6ufRhXcwiIolRoWOzrZerqqs4J5fkfvL9rXYkmo52wtQIao8Eg8TYOCIl5dSfPd-4jd-nKe0dTirInTbjLTjb5JZhqSIDZ8QQ2-7QE1kuocA9CvyDn40wwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=r-lRlHreGCYQasMQjkcgsrRNENaiGw5LDdwW8zBY_RMLVyU34UoweBUK9gfyBuAvIopyIf48zkax2MXwR4RQvs8VuqeDvhDbU5rx337LFVw98Okal0RxIxVyxmQ2N8HtY3w9sGPVspbpXHJFmuifmSt-opZwNnUlI-nR9xqIfurpZpbpxqjd2JUtqkR-sCgSryhySBBPr9R6455cCpf9kAy_P8Kk_9a6ufRhXcwiIolRoWOzrZerqqs4J5fkfvL9rXYkmo52wtQIao8Eg8TYOCIl5dSfPd-4jd-nKe0dTirInTbjLTjb5JZhqSIDZ8QQ2-7QE1kuocA9CvyDn40wwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپاد اوکراینی به یک ساختمان مسکونی در پرم، روسیه، تقریباً در ۱۶۰۰ کیلومتری قلمرو تحت کنترل اوکراین برخورد کرد و یک نفر را کشت و چهار نفر را زخمی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/news_hut/71270" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/news_hut/71269" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzwhRA9rA8lO50hRbQmjsWpG0kQdHlr42tUi9JbKbM1eRVmu4xnD4dLv0XllumgfK65MwjgIX7tUmjuXJjBM_qtcFWUtfisfaqhb3VUeuLsko02oNyXNDzbqAJTl7-zMYsB-5JQZzgmEppJmcaBmMz3JQeF9imwsPuobnZsYrUETFJfwSfNB8RJ1FV7BrKGKjFWE-kysEtQikFHFm4GYYjiiHE62apvb9re0t-I-TX0Am2nwUug6SK26892q4meby3xsPFAvqd5OfXcNjZG7w0f_j4bAPz2EMq512NuHo7dS1OTyRSZIqodyt5tnFONC1V2rjGonrhC8-gu9O-rFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/news_hut/71268" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=htCAcAera6tCxLv7SMi3KoSbB8HIscP7NZb0TDVRULP_Qh4CqXWrMRCokV4uHLDomGIi3GvO2yCH0C36u33nFNIuU4YQ9bam-C5nhttivrmRgK1TmMfKmvmnpybdlZb8dpGWNr-0UZFD61FVSQGqcC720l19CWblQ9-ERiWiS37asBQfgnJOC8uMckft5FolQPABKxSkZqdKfU2l4WWeXAp38k8wLeDR6xadRVUSHdUsjh1SZN42fDp3KSX7POlBwKvXtSsh_UVTclyaXowQAzx5CtQSD_Srdk-DtZVpZSGCy_cQ1Cx_G_ROJpoHDAl8YfTh8HNuuIjI14AMm6qT0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=htCAcAera6tCxLv7SMi3KoSbB8HIscP7NZb0TDVRULP_Qh4CqXWrMRCokV4uHLDomGIi3GvO2yCH0C36u33nFNIuU4YQ9bam-C5nhttivrmRgK1TmMfKmvmnpybdlZb8dpGWNr-0UZFD61FVSQGqcC720l19CWblQ9-ERiWiS37asBQfgnJOC8uMckft5FolQPABKxSkZqdKfU2l4WWeXAp38k8wLeDR6xadRVUSHdUsjh1SZN42fDp3KSX7POlBwKvXtSsh_UVTclyaXowQAzx5CtQSD_Srdk-DtZVpZSGCy_cQ1Cx_G_ROJpoHDAl8YfTh8HNuuIjI14AMm6qT0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
حساب کاخ سفید در پلتفرم ایکس:
در روشن‌ترین روز و تاریک‌ترین شب، هیچ شرارتی از نگاه من در امان نخواهد ماند.
آن‌هایی که قدرت شر را می‌پرستند
از توان من برحذر باشند..نور فانوس سبز!
@News_Hut</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/news_hut/71267" target="_blank">📅 12:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71265">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=lLcPkYsv1O0bPiprKpFDcLJUUF37BpDzC6Rd26QnJ94T-gekCKRylVWo5nJYwhaeXy9MdppyxjzM0Ua5ts8KvOFob6yxZdIIRgqM_81o3hNZkQ1MfdGEz6NkgTL1CkbjWWTe1O1XioWSw3oWypmVl2UgCF9jgISm9HXlq0EFplSctYw9_2B7iGo1WQxnbicA9ONlF0oXIpQg34x12RxXOfm1KUxRtyFcdi1Cm1unrl_iw8k2Uxt6iWIraNfyjUmlILBEDKA56Eu1rGPYDffQaK-usflMcbC2vTM9S3DMKqmplgJCaYcvt5W9bOCNRLhm81XT6fJZ_MrT4YKLxQPtQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=lLcPkYsv1O0bPiprKpFDcLJUUF37BpDzC6Rd26QnJ94T-gekCKRylVWo5nJYwhaeXy9MdppyxjzM0Ua5ts8KvOFob6yxZdIIRgqM_81o3hNZkQ1MfdGEz6NkgTL1CkbjWWTe1O1XioWSw3oWypmVl2UgCF9jgISm9HXlq0EFplSctYw9_2B7iGo1WQxnbicA9ONlF0oXIpQg34x12RxXOfm1KUxRtyFcdi1Cm1unrl_iw8k2Uxt6iWIraNfyjUmlILBEDKA56Eu1rGPYDffQaK-usflMcbC2vTM9S3DMKqmplgJCaYcvt5W9bOCNRLhm81XT6fJZ_MrT4YKLxQPtQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یکی‌ از مراسم های تولد در بالاشهر تهران
@News_Hut</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/news_hut/71265" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71264">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=O8Hq1R1vYSaZpSYOe986qrMlAZIPeW6NDzgTLQlLifhhOWLvApbcTBa3p95f7xngtwba9mMPrVhce-l2_WEfh2r2bU2FivJKnay4hKJp2WxnvPJeLf1fGl_Y9GKAfc2TFpfDugl4rMt2sqg2ax4Ocatz9wMyC1GxhFVP2OQARVhmthhphBfAiW3ibIfmTLqfxrqw1XcFoWu_9MSS9AWXkY_X7IwaAddYA0jGWAyBsZkdWm59vUw_kFO-dH7tapOdU3blUOZcsKp6jmfH5PV7cd7FlUtlZZJhHtu-BMFeMRHOSaGxkY2Kmg5H3zk9kuDQX9W_LSvplGcpX6v_dB6LkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=O8Hq1R1vYSaZpSYOe986qrMlAZIPeW6NDzgTLQlLifhhOWLvApbcTBa3p95f7xngtwba9mMPrVhce-l2_WEfh2r2bU2FivJKnay4hKJp2WxnvPJeLf1fGl_Y9GKAfc2TFpfDugl4rMt2sqg2ax4Ocatz9wMyC1GxhFVP2OQARVhmthhphBfAiW3ibIfmTLqfxrqw1XcFoWu_9MSS9AWXkY_X7IwaAddYA0jGWAyBsZkdWm59vUw_kFO-dH7tapOdU3blUOZcsKp6jmfH5PV7cd7FlUtlZZJhHtu-BMFeMRHOSaGxkY2Kmg5H3zk9kuDQX9W_LSvplGcpX6v_dB6LkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یک پهپاد اوکراینی در طول شب، بمب‌افکن تاکتیکی سو-۲۴ روسیه را در پایگاه هوایی ساکی در کریمه با موفقیت هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/71264" target="_blank">📅 11:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=vRGvnHENY1KuFwpc-6s9WT6QovUNvG5fd1HqSeAt1-egLaUYjWTJ4jpCkrMyi2wB3Ne6YensTS5I04f9yNzaA4_JYtiwfE1W6Yh6ajYD5C1QSjuGk1AdtYchkG0Wi9bpnsuZszNOZMoMVzXx_cVpF2iHIx1lpNeB42zfWXrGuh1LOzvimVBpWVK0tODYmUmKg5bXzg1MihZ8p3e_vcoIHqs7ueQtocOR45MhcZ4ak_n-fXa8FlOMeDNvM006sgAIjGHbSTDq2SAAXThYVIipD-3P-C-1iJRR2_-oKsioq22cCJ7u-2T_4n8-mBkaFdpKVwNkhcI81lUbmJ9zjIhxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=vRGvnHENY1KuFwpc-6s9WT6QovUNvG5fd1HqSeAt1-egLaUYjWTJ4jpCkrMyi2wB3Ne6YensTS5I04f9yNzaA4_JYtiwfE1W6Yh6ajYD5C1QSjuGk1AdtYchkG0Wi9bpnsuZszNOZMoMVzXx_cVpF2iHIx1lpNeB42zfWXrGuh1LOzvimVBpWVK0tODYmUmKg5bXzg1MihZ8p3e_vcoIHqs7ueQtocOR45MhcZ4ak_n-fXa8FlOMeDNvM006sgAIjGHbSTDq2SAAXThYVIipD-3P-C-1iJRR2_-oKsioq22cCJ7u-2T_4n8-mBkaFdpKVwNkhcI81lUbmJ9zjIhxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تهران، بیت رهبری، ۹اسفند ساعت ۹:۴۰دقیقه صبح
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/71263" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71262">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=tmXAti8-G9Q-vPZjvrauGG9mXf4xc71SnR4S1XCABYVe4IQYqTh7AIlDxoIUnIEKS5OWJVoUSobkL_2ommE9L2y-QPVuzpy-QDQrrF_d3saeFB6hR9bJdZKFYIhZVWHga_wM3I2crDm_9Xjz68L-FuduhMUX9GOrnFNnXoSIIIaj9B9Yccw5storvuVUJetM_oHK-vATrH5R314PUu_8LyM91LqVa1GPPZ8Dv7YIUzfdNQJIKGof8huWwEMiulDLm3_O4cb8WoZ8h3EE6GnMsd_JmMFx2bl1Dix9YAf4kltQkRp6NfjM6Ksjwh5igimwsXG70rp7wvyaP64aE-luxXtzEjD18e8dUP1MYYWXwDAEerQBobJc-vUM5pEbW9UKwqtC75Y_28CJXhWBJ2MwTf9rAjW4YrIvj5m4UfA6Py20ps0vxuuSadngsGAFtD8Q8JvGsaO6C35IxkSqNgk3O4Fe4D_kOoNnhSxCrROnakx5h1qCJ1EIZBPAZ5Lg8QKrIFgr4Bpp27A8aGMz4hY05udCVqRse0PiwBwMBXVKaP7J9GUZX_aOMkwniGp-jVVg6Izw2-8eQJ0FFyE1_45NMt-4bRA3UBANV-i2qWzqj05MrdvTM00XnRRE14v4Gy2IVGaYs1LCpVqK9JtGPBzSNWh222DOgy89Sf5sJ40HLBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=tmXAti8-G9Q-vPZjvrauGG9mXf4xc71SnR4S1XCABYVe4IQYqTh7AIlDxoIUnIEKS5OWJVoUSobkL_2ommE9L2y-QPVuzpy-QDQrrF_d3saeFB6hR9bJdZKFYIhZVWHga_wM3I2crDm_9Xjz68L-FuduhMUX9GOrnFNnXoSIIIaj9B9Yccw5storvuVUJetM_oHK-vATrH5R314PUu_8LyM91LqVa1GPPZ8Dv7YIUzfdNQJIKGof8huWwEMiulDLm3_O4cb8WoZ8h3EE6GnMsd_JmMFx2bl1Dix9YAf4kltQkRp6NfjM6Ksjwh5igimwsXG70rp7wvyaP64aE-luxXtzEjD18e8dUP1MYYWXwDAEerQBobJc-vUM5pEbW9UKwqtC75Y_28CJXhWBJ2MwTf9rAjW4YrIvj5m4UfA6Py20ps0vxuuSadngsGAFtD8Q8JvGsaO6C35IxkSqNgk3O4Fe4D_kOoNnhSxCrROnakx5h1qCJ1EIZBPAZ5Lg8QKrIFgr4Bpp27A8aGMz4hY05udCVqRse0PiwBwMBXVKaP7J9GUZX_aOMkwniGp-jVVg6Izw2-8eQJ0FFyE1_45NMt-4bRA3UBANV-i2qWzqj05MrdvTM00XnRRE14v4Gy2IVGaYs1LCpVqK9JtGPBzSNWh222DOgy89Sf5sJ40HLBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🔞
وایرال شده از رقص و شادی سربازان ناو آبراهام لینکلن توی کلوب شبانه توی پاتایا تایلند
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71262" target="_blank">📅 10:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71261">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b860e39243.mp4?token=J5tNOuVnGxwQHRKuFpIIJOgGfsKWQuiVAYEigOpZAPWgMPV6jMW3gOvNXuCcIMs9-S7DkBVXRCR-ImF9EzAlX6JblsgWO7bmxAQzJDWiVl-Z-E0IRo3nnaSWnXdGOY83zh8vp3E1J-Qfhmt1BNTeCm6ITE01YALTM68AfwQow_EpKlkjSOGl7q-M4XGrZd19yySP15amaGRuAxr_sB1Cg3-w_hlmZmUrXAbCs1pRtdECc5rOh6YRmajv2Vqs2_959_5UXhO1kNQqct4Jw_m7D61CD1f3pqr4yjpyvoB0LsN_pqm7A9nsdfgSLqxbS5S2hEJFst-GCS3ZgYzo4L6yig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b860e39243.mp4?token=J5tNOuVnGxwQHRKuFpIIJOgGfsKWQuiVAYEigOpZAPWgMPV6jMW3gOvNXuCcIMs9-S7DkBVXRCR-ImF9EzAlX6JblsgWO7bmxAQzJDWiVl-Z-E0IRo3nnaSWnXdGOY83zh8vp3E1J-Qfhmt1BNTeCm6ITE01YALTM68AfwQow_EpKlkjSOGl7q-M4XGrZd19yySP15amaGRuAxr_sB1Cg3-w_hlmZmUrXAbCs1pRtdECc5rOh6YRmajv2Vqs2_959_5UXhO1kNQqct4Jw_m7D61CD1f3pqr4yjpyvoB0LsN_pqm7A9nsdfgSLqxbS5S2hEJFst-GCS3ZgYzo4L6yig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم ترسناک منتشر شده از یه بیمارستان روان‌پزشکی و رفتار یه بیمار ساعت ۳ صبح بخاطر مصرف مواد مخدر شیشه، گل و...
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71261" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71260">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=v4b8DFla_VEBAs96aO67SimiJoX0dAV1Kmm1xdBH6O3VRKiVNIwOHi4HPOtPuWk9WowWlSuF1vo-mSTWfNGpuFN57JHD-l1rUR7W_Mch_Ch2ZSzpfQdLrUZpsX9ivcBnNJBJwnk8XU6dvcnz1MxUYHmHhAgz58yZ7WmlfGK8PfbORVVcw5ybZodpOSDUdtq_S6Fgje6ThKTWgmVPKQSZNLYl_C652jzVim0HfL258EVe_SfMQqb4vxdtLNzIujKspN_7dglvvOVuTC8XXBVusz1Yz9x9GlgdQlrj19snEc-xK-_5HW_5vT6z_5wp_dGJCUd0OlQNYZwkphYMydPo4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=v4b8DFla_VEBAs96aO67SimiJoX0dAV1Kmm1xdBH6O3VRKiVNIwOHi4HPOtPuWk9WowWlSuF1vo-mSTWfNGpuFN57JHD-l1rUR7W_Mch_Ch2ZSzpfQdLrUZpsX9ivcBnNJBJwnk8XU6dvcnz1MxUYHmHhAgz58yZ7WmlfGK8PfbORVVcw5ybZodpOSDUdtq_S6Fgje6ThKTWgmVPKQSZNLYl_C652jzVim0HfL258EVe_SfMQqb4vxdtLNzIujKspN_7dglvvOVuTC8XXBVusz1Yz9x9GlgdQlrj19snEc-xK-_5HW_5vT6z_5wp_dGJCUd0OlQNYZwkphYMydPo4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
⭕️
گزارش‌هایی از تماس‌های ناشناس با ساکنان جنوب ایران؛
درخواست برای خودداری از حمایت از سپاه در درگیری‌های احتمالی آینده
بر اساس گزارش‌های منتشرشده، اخیرا تماس‌هایی از مبدأ نامشخص با شماری از ساکنان بومی جنوب ایران برقرار شده و از آنان خواسته شده در صورت وقوع درگیری‌های آینده از سپاه پاسداران حمایت نکنند.
گفته می‌شود این تماس‌ها با کد کشوری سوریه برقرار شده‌اند، اما هویت و وابستگی تماس‌گیرندگان تاکنون مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71260" target="_blank">📅 09:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71259">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71259" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71258">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gERIJoMigZZIAwkv5NfrfWaGAbf5PobOxHFcJkvOobIadaPXWiNhiI6zPfDIeACEVBxYDedbGNdR1_DP-NsV3f9DZwv3qiuAz08__SayShjtbeZZ8jkryM7F0n4PbCRT7etK4pd2myles9ZtPzt_gZ-MntT6_UDPtV4sLUmjZ2l2Fe0QGVLWQiYVypnCN5c-7p-OeVfdupNZHRcPbLQL-Z-0K8RT76TZLAAx0yA1_eAqo-FpjXqSnOA7lE4IijFet_NFSUBqM8KB8vedTNZC2uG7f4NJPO-Lsmd9vEt13dMjK-5_xz5kLc3MAilGKSRTYDsKW4v70svEH0-OErHfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71258" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71257">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⭕️
⭕️
از دقایقی قبل نرخ سوم بنزین به 10هزار تومان افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71257" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71256">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a780504.mp4?token=LmLH-rg4tglwZJY5T-kIfu1LF5eYkQbD5NjXs6sWuHWuYqh65e5boicciz8d_NXbeLusoPLV4TyXvvBvcVSfdoVLJnLbEi1w_jVzJETwu-8z3kHq7UrkiqOH8_tHhkqfzX69ROy2u8HaBewY2Lt7ONScCx30rWXjAlL9IYgEcyUwzCx-VV7xCimGKS09ZBZMzH6Mps9WeG6GVTpb14pRgzMHR2SRQM_Le5LNaIRSsbvUlhQAQWlXidkspMiX2NZQqQ-L2iynvO2rocVBy2ack9NVWKrs4zLETkancT1HgrrAu6PnK4k0KSdg7A-QCWkuf6AwshOPntkyTIj86oM4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a780504.mp4?token=LmLH-rg4tglwZJY5T-kIfu1LF5eYkQbD5NjXs6sWuHWuYqh65e5boicciz8d_NXbeLusoPLV4TyXvvBvcVSfdoVLJnLbEi1w_jVzJETwu-8z3kHq7UrkiqOH8_tHhkqfzX69ROy2u8HaBewY2Lt7ONScCx30rWXjAlL9IYgEcyUwzCx-VV7xCimGKS09ZBZMzH6Mps9WeG6GVTpb14pRgzMHR2SRQM_Le5LNaIRSsbvUlhQAQWlXidkspMiX2NZQqQ-L2iynvO2rocVBy2ack9NVWKrs4zLETkancT1HgrrAu6PnK4k0KSdg7A-QCWkuf6AwshOPntkyTIj86oM4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
عادی‌سازی سقوط تپه علی‌الطاهر توسط طرفداران قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71256" target="_blank">📅 23:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71255">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ci3TjndQERCcSAq3WvCxvLiYu3i7AERhqMSjNRk8uuFgaoq1PlnMdNUa7JdaIKJ0k7lsyxrXo1K7tuxKCW_isjx3OIcfLtaEwtHCbBK8A4BDjljl9SNfSieG1pM_eihVLzGBZe1UJsaH-tGA6KGL3qwe38eNlk5yxnKIoyseqd_Il27PS0vOg2NAieLd9-D6N8jc5dZR6k3J1KY_bBh9M9RH3MefJKm0ECATjIgYagk1bm6HypfHHsOfsQGFLr-w627ukqnd7Fgawpe_nKPqjprgBZVXL-JvFgAnFpJGc_Nc3tJjiEmlwsO4F1GZro2Jbj5ytFBlYg_7-G1Zyjj8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ci3TjndQERCcSAq3WvCxvLiYu3i7AERhqMSjNRk8uuFgaoq1PlnMdNUa7JdaIKJ0k7lsyxrXo1K7tuxKCW_isjx3OIcfLtaEwtHCbBK8A4BDjljl9SNfSieG1pM_eihVLzGBZe1UJsaH-tGA6KGL3qwe38eNlk5yxnKIoyseqd_Il27PS0vOg2NAieLd9-D6N8jc5dZR6k3J1KY_bBh9M9RH3MefJKm0ECATjIgYagk1bm6HypfHHsOfsQGFLr-w627ukqnd7Fgawpe_nKPqjprgBZVXL-JvFgAnFpJGc_Nc3tJjiEmlwsO4F1GZro2Jbj5ytFBlYg_7-G1Zyjj8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یادی کنیم از اوستاااااد خانعلی‌زاده که در دوره جنگ 12 روزه معتقد بود جنگنده های اسرائیلی هرگز وارد آسمان تهران نمیشن چون باید چندصد کیلومتر داخل ایران بیان و برن و این کار ممکن نیست  و اینا همه شایعات مجازی هست!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71255" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71254">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71254" target="_blank">📅 22:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71253">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
⭕️
دقایقی پیش صدای چندین انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71253" target="_blank">📅 21:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71252">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead429175.mp4?token=eOdKFzwbcWeAdCaNs3AB0iODX846pwUC1k3kcREaD9nVj3W5bxKiIAkGoJyjPFgIyPHqRAx3kFPLf68DGDibw_bzzYXLEKGH0VEHiTsrnE80wsAeIc-ROFQy3VG0S-_yP8ZZX8nF2A_fU5m_teXmQbLH_MUsYc-mLuTEWPzoqPfJ9DTViwRFK6M_ZGJIt1AHfao1LcFwlsmqbZzl_CGprQnApCh7_X5xFOpvWUR0kB3QCAWNz_6rpoPWXSBgDKh94oh6ze7GfLK4mpEIDImxIsHsGUiw98Tm87yRhfPCTM4bESTPaEI4mtM6VEcwmPOh_cdK_ZRoq23-oGp5XjX4qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead429175.mp4?token=eOdKFzwbcWeAdCaNs3AB0iODX846pwUC1k3kcREaD9nVj3W5bxKiIAkGoJyjPFgIyPHqRAx3kFPLf68DGDibw_bzzYXLEKGH0VEHiTsrnE80wsAeIc-ROFQy3VG0S-_yP8ZZX8nF2A_fU5m_teXmQbLH_MUsYc-mLuTEWPzoqPfJ9DTViwRFK6M_ZGJIt1AHfao1LcFwlsmqbZzl_CGprQnApCh7_X5xFOpvWUR0kB3QCAWNz_6rpoPWXSBgDKh94oh6ze7GfLK4mpEIDImxIsHsGUiw98Tm87yRhfPCTM4bESTPaEI4mtM6VEcwmPOh_cdK_ZRoq23-oGp5XjX4qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
دیشب خبرنگار لبنانی داشت توی نبطیه گزارش تهیه میکرد که همون لحظه به شکل پشم‌ریزونی اسرائیل حمله کرد به اونجا و همچی قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71252" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71251">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=RpO1CxxFbZ7pB_DbG7QVdtw2-arfS7ZMWEGsz7QSzVDwKcDTD_dLjF4r12A-S1uHetO97Gh16kYqYfpYkgqHRHWtQ_g1mqG9NBCpfV3I7MnYDMTxvj2GWBca76TwwVHQ6fw7dvZ4oKCylcS7z-xsQfS1eV1lgVhEbU1M4hMSRXVjDsYk0ZTv-FcBFSmTaFeaoNTo_lhIk8eqZWIfIppzTVH5HR5eJMemOMyNYqWKRkC_AjE9j7z08yu2egFbUrRc_memo3KnDIaSBCb33TAIlBaPAj2ncfuXWPzSEhkZJgVukysbu2j_-FbZt961ggtVv12aYPLZC24zoA3gEx1IAAYNoe5DoRy5p3O0rD8LZ-moaFRcl1hd7zT5xUJce9XA1H_CcR8Vx0KPqXV9_0NwZK5AkNsoatM97h_fAIb20dkpGeZKvdSDFylsnIHJN9O1vtiKmP7d1AU3LwFkoLE3NBGExI--c3wpVPQJoD75WBluH3IcaytMb1hoN2-x9u6nY8xlKpoClrKL6j2EWf_iYPlmbw4Ftadf0xuwt_-SY5CHCeIw6MJuuNq87FqI4ORAd526S-T8BJg6EG7XpFF7yX1YAItB5HQKLtvgkv8TjJusXF7kFN_EH3OaJ6AKhVaPSBKvpSC2-IpAYb_9XCMBD6RVdWtd-LLqjCm8AbDplX8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=RpO1CxxFbZ7pB_DbG7QVdtw2-arfS7ZMWEGsz7QSzVDwKcDTD_dLjF4r12A-S1uHetO97Gh16kYqYfpYkgqHRHWtQ_g1mqG9NBCpfV3I7MnYDMTxvj2GWBca76TwwVHQ6fw7dvZ4oKCylcS7z-xsQfS1eV1lgVhEbU1M4hMSRXVjDsYk0ZTv-FcBFSmTaFeaoNTo_lhIk8eqZWIfIppzTVH5HR5eJMemOMyNYqWKRkC_AjE9j7z08yu2egFbUrRc_memo3KnDIaSBCb33TAIlBaPAj2ncfuXWPzSEhkZJgVukysbu2j_-FbZt961ggtVv12aYPLZC24zoA3gEx1IAAYNoe5DoRy5p3O0rD8LZ-moaFRcl1hd7zT5xUJce9XA1H_CcR8Vx0KPqXV9_0NwZK5AkNsoatM97h_fAIb20dkpGeZKvdSDFylsnIHJN9O1vtiKmP7d1AU3LwFkoLE3NBGExI--c3wpVPQJoD75WBluH3IcaytMb1hoN2-x9u6nY8xlKpoClrKL6j2EWf_iYPlmbw4Ftadf0xuwt_-SY5CHCeIw6MJuuNq87FqI4ORAd526S-T8BJg6EG7XpFF7yX1YAItB5HQKLtvgkv8TjJusXF7kFN_EH3OaJ6AKhVaPSBKvpSC2-IpAYb_9XCMBD6RVdWtd-LLqjCm8AbDplX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمودی بعد مصرف یک بَست:
موشک رستاخیز ایران می‌تواند در لحظه اصابت ۸۰ کیلومتر مربع را نابود کند
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71251" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71250">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVVqDhP_ozVdC7RuN_qkpNJEkhgtzu6AYGnfs738l9UG4vxUbuZhQ51Q3n-5tuLW2ID_Voq8DhXDsbd6fKP0BF-WCqARWDpKrZ4z8uulAJkdi948ajNrZ7krcAoQx9xwHXZ6u2tbLwzFShZZPp9vyj2wkTUwzkn-Hcn-Io7RhjFDe2SsuQQkFj9j3Nbl4-zBx3K99hEGAhtISVZO1nlo8ccxfFPynZ97yIfQ5R7AVFLmWMSYjWB6rwwTnkqwUZ9WsP3yAde92gyUyu2uNC5U1ob3luwhvA45cUxLov72Jeyxha6HkNhsKTXXIYxd9IwZClQ_y7pJFLiWwXNfHHElCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
🇺🇸
ترامپ بازنشر کرد:
سیاستمداران ارشد ایران خواستار پایان دادن به جنگ هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71250" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71249">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=Eo8H6C9C7b71TDDnIVLsRsFzHTVJc-tKEF8Y4Cn4EXyVvYHZtRo47qGBSyv1eEZ-PgfWiFEmiHS0EhiJOvmAjmQSH51n6X5rQu9gt9s7u4P5y8miZ-zkC2XxJXvZLb1nWiof1LseR5H7gOIJGJ1NSR3jkZk05WuAox14WWoe1RQTYuokGTmxLBJWMhzhIfLShkK8TWzp5jrl5ZcCW0jdU3gXWhw04IAeHOWp8L1tqykgwbrusSbDcxBR8QJOt5TObp2rnzqdIkl7Aty4fJkRXBKkKGj0x3s4gHhLc7PXoIXMgk0b0u446-0l9FDfBg6DDPcwmxUMuCXhbSFrIEGDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=Eo8H6C9C7b71TDDnIVLsRsFzHTVJc-tKEF8Y4Cn4EXyVvYHZtRo47qGBSyv1eEZ-PgfWiFEmiHS0EhiJOvmAjmQSH51n6X5rQu9gt9s7u4P5y8miZ-zkC2XxJXvZLb1nWiof1LseR5H7gOIJGJ1NSR3jkZk05WuAox14WWoe1RQTYuokGTmxLBJWMhzhIfLShkK8TWzp5jrl5ZcCW0jdU3gXWhw04IAeHOWp8L1tqykgwbrusSbDcxBR8QJOt5TObp2rnzqdIkl7Aty4fJkRXBKkKGj0x3s4gHhLc7PXoIXMgk0b0u446-0l9FDfBg6DDPcwmxUMuCXhbSFrIEGDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
به تازگی یه چیزی مُد شده به اسم «جوجه پارتی» ، تو این پارتی، پسرا رفیقای دوس دخترشون رو به همراه رفیق سینگلشون به این پارتی میارن، تا برای همدیگه جوجه بکشن و از سینگلی در بیان.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71249" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71248">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7Fsbt5DhlEU0CQnt0liXa0TExIFRd3H4cSre3bpHnzfol1hTnGnMMbc7xgICEOUoqnSBX8O2hDt_h4HhFveJGWVCYnA2dpQbQOj8HSawF331MVUG4NyOf4LIRsuTnqFdpQeFVQC9ZKQZ2Eko9ECCnJ21xJIddOg2dOnALg2sBDIpxc-57_EMwglJQQ5YNuanBZ-2j_5QPWUzqBykLWucjolJQEcz_cF5q2jQuDNlzNR1XlBc6rIKj01Mzr959fqQGYOrJU0W6pqixFlifvRmP3ySvOgBcxUnQGe3IkSlM5dZ2Sd2hWQJLkK9vrtC0GtiGp957ge2T5PlbodFuOswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71248" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71247">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71247" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71247" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71246">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9O_z4L2kLBpxHvcnS4uXdONI7YaDYJYeu6cjjJCRl8pRCFPsSYfRqk-V8plpgMHnLFHUjmOWtPOpsdHGxPU1ZSFPxuckLnxNfbGQ_mJDPOVAHDyy6Pk3yr-E2q-uRaM6SCQVJ272k5F-fAdQzPek-O39uspOMuJkQylEkM4vrCaMWH8D7coGbUhrtD3As7D3TiD0g8nlVVkHi270bmdnL6eZDD0KlcjRjPcw2QkdcfpBPtWy77j3esCdynMcqTcpzfwCxZNcbiwReqOe0FgnR9MMoJ_w3yVo2S3Bne_MATQh3XhBxsWDZEl5tcA9_Ff3En5xVzqQXYUtcv0MdQI9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71246" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71245">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">▶️
🇱🇧
🇱🇧
این ویدیو رونمایی شهر موشکی عماد است که مو به مو طبق شهرهای موشکی و پهپادی سپاه پاسداران ساخته شده؛
دو سال پیش حزب‌الله لبنان از این شهر موشکی زیر کوه‌های علی الطاهر رونمایی کرد.
جمهوری اسلامی بیشتر از خود حزب‌الله لبنان خرکیف شده بود؛
از برنامه ثریا تا اخبار سراسری صداوسیما تماماً افتتاح شهر موشکی عماد با ۴۸ کیلومتر تونل بود که مدعی بودند ساختش چندین سال طول کشیده و اکنون تسخیرناپذیر و نفوذناپذیرترین دژ عالم است.
این شهر پس از سه ماه محاصره توسط ارتش اسرائیل سه شب پیش در سکوت خبری تمام رسانه‌های جمهوری اسلامی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71245" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71244">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=BkVvp0DMCbonYMbCXQEdB3JFc7lFvjEMi54HCXya7b4hFFufmiUf0HX6VEnvn8h6FH5Ox0UYbh93PEcPBhkBEYPJNrYo0VZkCHT3w7FYKTFR0yI1p9I0K-L_pNy3EGCn8w80k61R7R8QpnxzySuGO1jph6Mb1fZYay_9xY_i8pq9Jz6BQHQ6gK0bhJTLtq3kpCqXEF0l-S5BSmTpIFornnnwhHBbHGFsdIYlUCuHMz8cX5Y6whYXCrd-IjCgTQEYzjpFPLpXhx7UVSiOiigqhqy8bcqNigt4dUOJa2vPvCyOrx6UkbjzlPerthtwD3QvsA-kgd_1wS4bfpGMwUP72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=BkVvp0DMCbonYMbCXQEdB3JFc7lFvjEMi54HCXya7b4hFFufmiUf0HX6VEnvn8h6FH5Ox0UYbh93PEcPBhkBEYPJNrYo0VZkCHT3w7FYKTFR0yI1p9I0K-L_pNy3EGCn8w80k61R7R8QpnxzySuGO1jph6Mb1fZYay_9xY_i8pq9Jz6BQHQ6gK0bhJTLtq3kpCqXEF0l-S5BSmTpIFornnnwhHBbHGFsdIYlUCuHMz8cX5Y6whYXCrd-IjCgTQEYzjpFPLpXhx7UVSiOiigqhqy8bcqNigt4dUOJa2vPvCyOrx6UkbjzlPerthtwD3QvsA-kgd_1wS4bfpGMwUP72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از لحظه فاجعه انفجار تانکر حمل سوخت در سنندج که باعث مرگ 11 نفر شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71244" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71243">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=KUT1qVj9hwa3ro5Ss35ZSFd_w-kUs-zEsrIvGWKFeDI-gkNTNN3u7fFFN5__6YHUr5ha-TjgsEo8wsC2BLX1QxK7lME4E6jzNkiOkgqIWEYosMOLXNSNdVqO1Ejx9NrWN_HPe52pWdlroo0THb2HPjsnDZWgA9u2sjKOdPh2UUVmvUW2FnLF6YRVL7Z8d8-vUczDX_i-KCCgN6k5uzgoKH2UkGTMhM6oNYwF4qaFoszp2nJiapy09gkkErdmA9SxDD6_NIgSuraDW3JV_gAKEXRdRji2ILsSSzMDStZbVhUQ3lkTn2lMQkPylNml0AIA1KmFamvh-KL1OQXFvKqNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=KUT1qVj9hwa3ro5Ss35ZSFd_w-kUs-zEsrIvGWKFeDI-gkNTNN3u7fFFN5__6YHUr5ha-TjgsEo8wsC2BLX1QxK7lME4E6jzNkiOkgqIWEYosMOLXNSNdVqO1Ejx9NrWN_HPe52pWdlroo0THb2HPjsnDZWgA9u2sjKOdPh2UUVmvUW2FnLF6YRVL7Z8d8-vUczDX_i-KCCgN6k5uzgoKH2UkGTMhM6oNYwF4qaFoszp2nJiapy09gkkErdmA9SxDD6_NIgSuraDW3JV_gAKEXRdRji2ILsSSzMDStZbVhUQ3lkTn2lMQkPylNml0AIA1KmFamvh-KL1OQXFvKqNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
طبق قانون، استیکر و گیف خنده داری که از رفیقت میسازی جرمه...
و میتونه ازتون شکایت کنه و تا 1 سال حبس و 5 تا 33 میلیون جریمه نقدی داره.
اینکه شوخی بوده هم هیچ تاثیری تو مجازاتش نداره
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71243" target="_blank">📅 17:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71242">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06303045.mp4?token=JiGMMNlfp7FFrz64ht1VkR0j13hgsnUyC1xeB1C8whKiu8a3ykHc46ix8MaJpSl5Z8EphQQKMdpG3lmvqdpAAJAQo98r385dPUEaFkECVT_4KK4uijrWFS-Zw1v9dl-j549DxSM3jLYIFMSNUOmH18Uwn62KojQmEfFAaG9m_1pMTwy2fKdFUrXt4nZ582pqFKFW5658mDBHN7nR6l-ZiSZUi072gDGkUeFDp-1YUFvzMgjI5oDnsLmfUdQcmLdr8rN8ZJ5pYcuCti7hT706g-QsZVuOUrnhdjUToVgtbrZpB4TM8pY40cM2M43WcKCpsKRW2IyJEufDhrVKaE-MAUsludXfpdi16wEYRBHOm4IWyM33FJmTK2_6jSFk39FrYoUjYEapD2RhzB6Bp3uyArDn07U_UsfyfY8-QLLf3-Gtk0bEdRF5-JAidFE1CQFpDzQ_6-vI-Ema0047yOrFRANmBgdaDLIRZ_-9DMyZwjhEpiQR-qhA_758GkGDCDP8L6e3j1RFOBDIxKVIl4-UlxIMEfoJIzt2HhEVu0fpEyN9C3zGt4DR89KiJmgEypdbQVcoZfSAaxaRA2rJIxfoVupJrhmJ-QyTf-kCzc9O2RFIXKTwjlMxslsWWUmVShP_DIiXGSzExT4-W1JQDggVN0u62W5TkpJtSf7lxIZ4NkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06303045.mp4?token=JiGMMNlfp7FFrz64ht1VkR0j13hgsnUyC1xeB1C8whKiu8a3ykHc46ix8MaJpSl5Z8EphQQKMdpG3lmvqdpAAJAQo98r385dPUEaFkECVT_4KK4uijrWFS-Zw1v9dl-j549DxSM3jLYIFMSNUOmH18Uwn62KojQmEfFAaG9m_1pMTwy2fKdFUrXt4nZ582pqFKFW5658mDBHN7nR6l-ZiSZUi072gDGkUeFDp-1YUFvzMgjI5oDnsLmfUdQcmLdr8rN8ZJ5pYcuCti7hT706g-QsZVuOUrnhdjUToVgtbrZpB4TM8pY40cM2M43WcKCpsKRW2IyJEufDhrVKaE-MAUsludXfpdi16wEYRBHOm4IWyM33FJmTK2_6jSFk39FrYoUjYEapD2RhzB6Bp3uyArDn07U_UsfyfY8-QLLf3-Gtk0bEdRF5-JAidFE1CQFpDzQ_6-vI-Ema0047yOrFRANmBgdaDLIRZ_-9DMyZwjhEpiQR-qhA_758GkGDCDP8L6e3j1RFOBDIxKVIl4-UlxIMEfoJIzt2HhEVu0fpEyN9C3zGt4DR89KiJmgEypdbQVcoZfSAaxaRA2rJIxfoVupJrhmJ-QyTf-kCzc9O2RFIXKTwjlMxslsWWUmVShP_DIiXGSzExT4-W1JQDggVN0u62W5TkpJtSf7lxIZ4NkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
🇰🇵
روسیه و کره شمالی یک پل جدید را در امتداد رودخانه تومن افتتاح کردند. این پل دو کشور را به هم متصل می‌کند و با گسترش همکاری‌های نظامی و اقتصادی این دو کشور، اهمیت این اتصال نیز افزایش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71242" target="_blank">📅 17:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71241">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=mKxyLRE9V4th-pN-3TZciGbjvVBwBXZYU93gYXmTDRKl6wDwuTh7XMP3js2H874bQp64fHSilxBhZFmwT8_pr8VQDjRpPiDvlvA6y8mtWJUEpJbG0dckkPBn8PzKtPzim7GAW8D0-1GQ4xfvJJFC2lNkwXKmh4F-GlP6Y_VFidsPlwKyMb1uOikrYO5vCpXeZjIJaUCY9aoMnXZNFO5_7I3iQl5xbfqR-W4EpPzHVGe3AdZy3hYM1FTKqTWm-Wl_ponN2NDCeO_DMawBOkO2dPahotMS0msNfQCMQfc7-IoBZ_HjnrzgJRCkr1R8bOLGekj6JojZ1_yvTXwmBMgJHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=mKxyLRE9V4th-pN-3TZciGbjvVBwBXZYU93gYXmTDRKl6wDwuTh7XMP3js2H874bQp64fHSilxBhZFmwT8_pr8VQDjRpPiDvlvA6y8mtWJUEpJbG0dckkPBn8PzKtPzim7GAW8D0-1GQ4xfvJJFC2lNkwXKmh4F-GlP6Y_VFidsPlwKyMb1uOikrYO5vCpXeZjIJaUCY9aoMnXZNFO5_7I3iQl5xbfqR-W4EpPzHVGe3AdZy3hYM1FTKqTWm-Wl_ponN2NDCeO_DMawBOkO2dPahotMS0msNfQCMQfc7-IoBZ_HjnrzgJRCkr1R8bOLGekj6JojZ1_yvTXwmBMgJHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
معاون وزارت ارتباطات :
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی باید ادامه داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71241" target="_blank">📅 16:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71240">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=f0_VPEkIvuKgWfX-UzLOP_x1rhsOUSg8KOqJ1z1eYP8OAheNfNEMf-7HKoul764q_F2D8WDHmykubhnPEypc4Wb5-adOdjhArBVeuNk0N3ynJEuAOJTY2l96ogo_5ZPRdsakTVg7irPwjxt86mqIrcgdFYm82raLVWWK-EzSJmPdWEDblgt-ZTG9o9oaNGN9dOI_nDFmaQ6KBpF3EaOSd3uV0RPHH8jPa2mWb_iHeTpE12jr-VTk4dLxMitnHstC88q73syEoRzu3pLi97dAYtsqsL5cgfbJivJKpbWS-USC48GOW9QcrpiHZP1g27CSDUsqj-NdQ-usZyG4EZhbOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=f0_VPEkIvuKgWfX-UzLOP_x1rhsOUSg8KOqJ1z1eYP8OAheNfNEMf-7HKoul764q_F2D8WDHmykubhnPEypc4Wb5-adOdjhArBVeuNk0N3ynJEuAOJTY2l96ogo_5ZPRdsakTVg7irPwjxt86mqIrcgdFYm82raLVWWK-EzSJmPdWEDblgt-ZTG9o9oaNGN9dOI_nDFmaQ6KBpF3EaOSd3uV0RPHH8jPa2mWb_iHeTpE12jr-VTk4dLxMitnHstC88q73syEoRzu3pLi97dAYtsqsL5cgfbJivJKpbWS-USC48GOW9QcrpiHZP1g27CSDUsqj-NdQ-usZyG4EZhbOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آخوند قاسمیان:
برادران یوسف 11/11 وحدت کردن یوسف رو انداختن تو چاه، این که وحدت نیست، وحدت باید حول محور رهبری باشه..
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71240" target="_blank">📅 16:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71239">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/98f065761f.mp4?token=t-IdbYISai0m4y8ycimrKy2SiuW3hACJRUkywyboRLCz4Fm7j8MpU34H81czkkgOBaHOFuZeaY6O4ii1ht9RnUm8n0noygPVqj3gsE1CfO_Zm5iMOgsln6-W6ug5FUBY4xMElyeD-rJUGd4qzg5QCpWj8HBBDef2ASAqQFxMZHOpGIOaOsIdos6HexPuqJQ5Wp_HpuvlLEOzQUmRb07uHuLhAex8mF32YgekHmxCh8dzKditvz4vOehNmj6fZTkw2rkq73goauqWHP58sDCvQ_mOPxr0bwaJqZmdk5mjMA-zI0naWdmZBhCFmEimrnOMZNLodjlfXVBdUq227oOhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/98f065761f.mp4?token=t-IdbYISai0m4y8ycimrKy2SiuW3hACJRUkywyboRLCz4Fm7j8MpU34H81czkkgOBaHOFuZeaY6O4ii1ht9RnUm8n0noygPVqj3gsE1CfO_Zm5iMOgsln6-W6ug5FUBY4xMElyeD-rJUGd4qzg5QCpWj8HBBDef2ASAqQFxMZHOpGIOaOsIdos6HexPuqJQ5Wp_HpuvlLEOzQUmRb07uHuLhAex8mF32YgekHmxCh8dzKditvz4vOehNmj6fZTkw2rkq73goauqWHP58sDCvQ_mOPxr0bwaJqZmdk5mjMA-zI0naWdmZBhCFmEimrnOMZNLodjlfXVBdUq227oOhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رو آورده بودن موقع زایمان پیش زنش باشه و بهش روحیه بده، آخرش دکترا مجبور شدن خودشو درمان کنن
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71239" target="_blank">📅 15:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71238">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f53489458.mp4?token=pJYVHrmZtduj0mc7eMHCS67-r37Yfzcx9efSO-R6Ir3apt-rhOyVBrJjlJqlhjZeaK-uj-dQGZ-hd6gwqWkBOz2Jykp5shOf9_aGnU_xGziy-Pz0skFG_-0AoQV24o6eMPbNLedgYsv5BNCB67082H8Uf88s7m6HgYjgmpciyEurUr9x3A59z2l9WrEBecMRfRylqhQf21tVd-Sy4qlO1W9wYT0ahVgQiW0d2snu4RRFL5Dqp12kM46K1vt4ratgM9tT3TMGCG0SLeqmlNteJopvUiwFh8kGBc79vLAi4t1frGsPH6_yaNmXrHek3gGyBbbnXnX4dioS01QFl_mJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f53489458.mp4?token=pJYVHrmZtduj0mc7eMHCS67-r37Yfzcx9efSO-R6Ir3apt-rhOyVBrJjlJqlhjZeaK-uj-dQGZ-hd6gwqWkBOz2Jykp5shOf9_aGnU_xGziy-Pz0skFG_-0AoQV24o6eMPbNLedgYsv5BNCB67082H8Uf88s7m6HgYjgmpciyEurUr9x3A59z2l9WrEBecMRfRylqhQf21tVd-Sy4qlO1W9wYT0ahVgQiW0d2snu4RRFL5Dqp12kM46K1vt4ratgM9tT3TMGCG0SLeqmlNteJopvUiwFh8kGBc79vLAi4t1frGsPH6_yaNmXrHek3gGyBbbnXnX4dioS01QFl_mJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویدیو وایرال شده از یکی از معلم‌های مملکت :
اگه مدارس امسال مجازی بشه، از گوشیِ شخصی‌ام نمی‌تونم استفاده کنم.
چون پارسال 4 تومن گذاشتم رو حقوقِ 14 تومنیم و این گوشیِ 18 میلیونی رو خریدم.
امسال همین گوشی 70 میلیون تومن شده!
حقوق من چقدر شده بعد ده سال تدریس؟ 20 میلیون تومن...
اگه این گوشی من خراب بشه، دیگه نمی‌تونم گوشی بخرم.
آموزش و پرورش باید به فکر تهیه وسایل آموزشی (گوشی و لپ‌تاب) واسه معلم‌ها باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71238" target="_blank">📅 15:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71237">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
این خانم ادعا می‌کنه که در جزیره اپستین بوده؛
صداوسیما هم صحبتاش رو پخش کرده.
ادعا کرده که به کل جزیره تجاوز کردن و شرایط بدی بوده.
بعد میگه خداروشکر فقط خودم مصون موندم و بهم تجاوز نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71237" target="_blank">📅 14:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71236">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c603211e44.mp4?token=lXa-pwoS_92uroKOT0YwmTpBNXi3dWIhJ3m6Yqsia5-M5oUVI52q5J1Q0DhL36m_rWDePI_2g-YEiYGvav68xHgNC2ATxE1-ZVJQX_RxX1d6MUNysoSJOQ1Qa5eFTlZBSO-ftwmdsfKFeA2gyINxfPGjj-ix3TWUfyBy88rQw4xWeqSekxRbY-0Ct8shmFcTHSmzheQoZNI2Fz5mUm1kDTrHqT3-IFqzvQ4p7LSRjAAk_rzjlUbCbGOLBlKhx9OCZri90YZoNajKj_ptbv8_xIDWnZntNFNAZYJ9rfzOHnU81YgVl9DDYiyqXVyRdqSpUzPnHch2Qj_J0avEIb6Sqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c603211e44.mp4?token=lXa-pwoS_92uroKOT0YwmTpBNXi3dWIhJ3m6Yqsia5-M5oUVI52q5J1Q0DhL36m_rWDePI_2g-YEiYGvav68xHgNC2ATxE1-ZVJQX_RxX1d6MUNysoSJOQ1Qa5eFTlZBSO-ftwmdsfKFeA2gyINxfPGjj-ix3TWUfyBy88rQw4xWeqSekxRbY-0Ct8shmFcTHSmzheQoZNI2Fz5mUm1kDTrHqT3-IFqzvQ4p7LSRjAAk_rzjlUbCbGOLBlKhx9OCZri90YZoNajKj_ptbv8_xIDWnZntNFNAZYJ9rfzOHnU81YgVl9DDYiyqXVyRdqSpUzPnHch2Qj_J0avEIb6Sqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی
:
چهل‌هشت ساعت پیش اولین موشک ناوشکن خودمون رو بالای سر یه ناو آمریکا تست کردیم
واقعاً یک جهنمی به وجود اومد.
🎙
مجری:
موشک بالستیک؟
🇮🇷
محسن رضایی:
موشک خاص حالاااا. موشک خاص
😟
ناوها فرار کردن.
حادثه آنقدر بزرگی هست که سنتکام هم نتونسته نفی بکنه. اعتراف کرده به این
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71236" target="_blank">📅 13:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71235">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhrHH3l7fcD1Omz1CSxbXKJiDscGAaczEQH2xTi6tTUGhVx50EPG_SCTK-s3ubDAX-Bxvs9hSo1r88zVH6iynZXfR-zNrZ8r8jZrg5bYj8edJ2LRuAPlcUHdeDXfOuFljjVrYtP6nhwaQDLWO1nMiZ27Zk9E3pI4B-4Pozk7hZPxJetpeOcVH2OomBkgCxOtNAC8zvCBWMqSZXeXhzKZ20LXm20WSYs1GqG2VFAyrguHjrvfQQAFncyAwQyda0KzXRej-2_HADGY27dRsV_vamJVy7RXTDrye6YwuXkh2o7ZvvqmowTQfOEGBBzKbgVsVd52TD5Trk3OnEQFXPb4YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
⭕️
🇺🇸
👀
افزایش شمار هواپیماهای سوخت‌رسان آمریکا در شبکه مرتبط با عملیات ایران
بر اساس نقشه OSINT منتشرشده توسط DefenceGeek در ۷ سپتامبر ۲۰۲۶، مجموعاً ۱۹۵ فروند هواپیمای سوخت‌رسان KC-135 و KC-46 در شبکه مورد بررسی این نقشه ثبت شده‌اند.
⭕️
جزئیات این آمار:
۱۶۶ فروند KC-135
۲۹ فروند KC-46
مجموع: ۱۹۵ فروند
این نقشه پایگاه‌ها و نقاط مورد استفاده برای مأموریت‌های تانکر در مناطق تحت پوشش CENTCOM و EUCOM را نشان می‌دهد و علاوه بر پایگاه‌های فعلی، برخی پایگاه‌های مورد استفاده قبلی و مسیرهای ترانزیتی را نیز دربر می‌گیرد.
در نسخه فعلی، تعداد KC-135 نسبت به آپدیت قبلی(3 اوت۲۰۲۶ منتشر شده) ۷ فروند و تعداد KC-46 ۲ فروند افزایش نشان داده شده است؛ بنابراین مجموع ثبت‌شده ۹ فروند افزایش داشته است.
منابع مستقل نیز در سال ۲۰۲۶ از به‌کارگیری گسترده تانکرهای KC-135 و KC-46 برای عملیات مرتبط با ایران گزارش داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71235" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71234">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbuloFpsI9XkRgnt7muu3pz25WcDKvo3E4IhYya1qrrvf6dv9pmrC8oCQ1WAzbMhUZee1m2sb4j7I5ohVKO2nfMlm8HpR0iTM0qLczvAHy71qD4OBixHcTcLvB01aHFgDi420tjFeH4BiO1sz-guMNaMqVVSqZOPyqFr7WI4NCesyzmU9YLdNSz3jtlEZf6ebBUGZvqUIXVChadKUYSvtINNOl6Xjk85XHAi1kN9ibVA68gNKgOz71AiG-9nTns4OGrUZsgSI2YBCXyMBH1HIJxQDHE0uWUSclqbJEU6uCFlklJnvnEs4l4LrAH_eBfjtjMj5TGuicOw2hqCTrapYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
موضوع ساده است: زنجیره تولید نفت و گاز در اینجا گسترده، در دسترس و آسیب‌پذیر است.
شرکت‌های نفت و گاز آمریکایی که در این آب‌ها و تأسیسات حضور دارند نیز در معرض همین آسیب‌پذیری قرار دارند.
به دارایی‌های ما حمله کنید، ضربه خواهید خورد. ما پیش‌تر این را ثابت کرده‌ایم؛ از پایگاه‌هایی بپرسید که دیگر کارایی ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71234" target="_blank">📅 12:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=os3evVwDLce1NAmmFjOXZrTCIHL5xENM-9QBCVyKqUXnI8CCT3yneponu-8aWDSMNS5IwaqnzbrBRDYAsn1GVLXvb8p8KKhiSV5zpDBEaXAv1NOVHySWTtVIpa-BfpVTzUcq6E1mbCyRyONaA9t5LQqZ0aaWnOMcJXPzd6y7pcoGBpzPRoPHkFLv1XX9JyeQkuvMxTWc8bgZmbnDr-e7wbT5RpPpUYj6-v0B-Zws1rIiBqJkMqYXp85hy_wsvVApFU2ysbkVjsuPHXXWSFeyRb1Unk4Ka6Etug_GlPn5JTgLjVMVrh5pgmBLfXYByv_H9w2YjSBcm_8Ylu1bFONgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=os3evVwDLce1NAmmFjOXZrTCIHL5xENM-9QBCVyKqUXnI8CCT3yneponu-8aWDSMNS5IwaqnzbrBRDYAsn1GVLXvb8p8KKhiSV5zpDBEaXAv1NOVHySWTtVIpa-BfpVTzUcq6E1mbCyRyONaA9t5LQqZ0aaWnOMcJXPzd6y7pcoGBpzPRoPHkFLv1XX9JyeQkuvMxTWc8bgZmbnDr-e7wbT5RpPpUYj6-v0B-Zws1rIiBqJkMqYXp85hy_wsvVApFU2ysbkVjsuPHXXWSFeyRb1Unk4Ka6Etug_GlPn5JTgLjVMVrh5pgmBLfXYByv_H9w2YjSBcm_8Ylu1bFONgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بمباران آخرالزمانی پادگان فتح خوش‌نام کرج توسط جنگنده های اسرائیلی در جنگ ۴۰روزه
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71233" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71232">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71232" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71231">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riPOA9hKNqHnryQqCCB9nJNfNdXFhp5MP4AJ2lMXggKHJL-GEuyklzve0sg7mezLGwvogdtgld3K17qLzzSayaNlX23xxqb022Ex9NjoUPzThUxVZ6ftQ7C9M5LsXFfcoNFVT0Mz_uS-ymLxzUeuoaEjNbAwo9WVRrItk6yB0r-0wa8QdVZ60_hNDYJclIENPgn_TEyk-E0GNdJ37Ux8Ct7_EVKF9Ca4GLePvsLrs4xAa61XkqntM5fHriyBViTY-VfGDPRhhOkAGS9eGaNgGGwPuSR6j3GZHBT6B-xzELplF5EiSnaLEC_RyGy3U11NTCIfYJn81c2srY6vtMSXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71231" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71228">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=BQw6z_Lt1KeVb3w0iJQiYu8Tvq3G3LWJuI19bd9B7FMIaTsYK6EWnzF3n91w0vy5HDf6FYO3_bsGUA2Edeni5acWdFU3ZeRYWLcHJW3Sw9ZO6HaJsbzqELlsdIU82LsYasnHAXSXH3Qjgsqg9gsjMzqvyOMi89yzWvpUCvbYZftioGKOUvpd5e26p_yVI28ERAxEbXbNaJlRZ4eT5aLKoLI6RAeH_x7lgtWLijUJIjbYbTvzF6gGRovMFyusl53HW2BpH0KgSFGQD3PGz3ZaSRyf9iAvk83rREzzGFBLDiX82B6BbOPlxGET7zIydnySOZ7DciGUzbW_LAycfByFCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=BQw6z_Lt1KeVb3w0iJQiYu8Tvq3G3LWJuI19bd9B7FMIaTsYK6EWnzF3n91w0vy5HDf6FYO3_bsGUA2Edeni5acWdFU3ZeRYWLcHJW3Sw9ZO6HaJsbzqELlsdIU82LsYasnHAXSXH3Qjgsqg9gsjMzqvyOMi89yzWvpUCvbYZftioGKOUvpd5e26p_yVI28ERAxEbXbNaJlRZ4eT5aLKoLI6RAeH_x7lgtWLijUJIjbYbTvzF6gGRovMFyusl53HW2BpH0KgSFGQD3PGz3ZaSRyf9iAvk83rREzzGFBLDiX82B6BbOPlxGET7zIydnySOZ7DciGUzbW_LAycfByFCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇶
#فوری
؛ بیش از ۱۵۰ ایرانی به دانشجویان عراقی در سمنان حمله کردند.
🎙
به نوشته خبرنگار بغداد الیوم در سمنان:
گروهی که این رسانه تعدادشان را بیش از ۱۵۰ نفر اعلام کرده، به محل اسکان دانشجویان عراقی در دانشگاه سمنان حمله کرده‌اند.
گزارش ادعا می‌کند پلیس پس از اطلاع از حادثه به دانشگاه رسیده، اما هیچ‌یک از مهاجمان را بازداشت نکرده و صرفاً تلاش کرده درگیری را متوقف کند.
طبق این گزارش، مهاجمان وارد محوطه محل اقامت دانشجویان شده و تعدادی از دانشجویان را به‌شدت مورد ضرب‌وشتم قرار داده‌اند و در نتیجه، شماری از آنها زخمی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71228" target="_blank">📅 11:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71227">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=cIuOd_1cQrizM1Wu5JQFQYTgw4ki7EjQK6lVKSXeWkXjWmM4T7NUnkGg84o-IV3TVtYG2Aqfz-RL0Owu6xuJ04RCmEwOSXM5tyI6W6VcWYLv_yLO_lhkiAi4asKbmBYn7lB1Ldw9dy0Lx4JWr2bvn1_M8SHWO0mv1A2w4uno8GrTv7caH_ZfAWmW8blxJn_9518uCbT1H1xsovpnnt-rTAN1ELCwcZe_7RUXaJT--BtFSNZnb3SZXeTsb6bYzez7o8DFo97xxCxDw7ziBA15yYoXPB5oNP-jtlMY5OaoRwWydjRdVe5DRqnbdv-A1bUWLfQclj3ufa4vPWeJU3lVaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=cIuOd_1cQrizM1Wu5JQFQYTgw4ki7EjQK6lVKSXeWkXjWmM4T7NUnkGg84o-IV3TVtYG2Aqfz-RL0Owu6xuJ04RCmEwOSXM5tyI6W6VcWYLv_yLO_lhkiAi4asKbmBYn7lB1Ldw9dy0Lx4JWr2bvn1_M8SHWO0mv1A2w4uno8GrTv7caH_ZfAWmW8blxJn_9518uCbT1H1xsovpnnt-rTAN1ELCwcZe_7RUXaJT--BtFSNZnb3SZXeTsb6bYzez7o8DFo97xxCxDw7ziBA15yYoXPB5oNP-jtlMY5OaoRwWydjRdVe5DRqnbdv-A1bUWLfQclj3ufa4vPWeJU3lVaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از روز انتخابات دانش‌آموزان پایه هفتم آمریکا که این پسره ادای ترامپ درمیاره و مثل ترامپ وعده میده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71227" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71226">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc74mCnqzdFwsyGxzwbohcryx3vbtsPLVM8UG5ZtpNdIPL3b7Acdn530RqBKwyibUw7q_ag-A5r4u-mbhuV83ZipdklVBhqmPwI7a53Tmr-1IF09ejcJfaycNRS9pAws1R0VEQco6KTod_s-wm7PFUmMnf6OR1IuMP6Kb0VSGw8mvz4W_IqDtbYJ8-klK3BB45Hgh-LnOATCA-QHjkt6Szh8IP5cBohH_ijykfntmOqRUATbwHfeflJiN0l1EpwWF9Jo9M5e9md_VFNh4YEliGsdKk8xyCLG-Ss21rTqrLkRm0LWO9DYHLcBbhNwdwZ00xgumxQ-8zp5dMYDImCxA4n6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc74mCnqzdFwsyGxzwbohcryx3vbtsPLVM8UG5ZtpNdIPL3b7Acdn530RqBKwyibUw7q_ag-A5r4u-mbhuV83ZipdklVBhqmPwI7a53Tmr-1IF09ejcJfaycNRS9pAws1R0VEQco6KTod_s-wm7PFUmMnf6OR1IuMP6Kb0VSGw8mvz4W_IqDtbYJ8-klK3BB45Hgh-LnOATCA-QHjkt6Szh8IP5cBohH_ijykfntmOqRUATbwHfeflJiN0l1EpwWF9Jo9M5e9md_VFNh4YEliGsdKk8xyCLG-Ss21rTqrLkRm0LWO9DYHLcBbhNwdwZ00xgumxQ-8zp5dMYDImCxA4n6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرفداران حکومت یه بازی ساختن که برگرفته از بازی مافیاست و فقط نام نقش ها فرق میکنه.
در این دور از بازیا ترامپ برنده میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71226" target="_blank">📅 11:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=jQsCYgoUwyjqzivWH-3jS5-ot2dsivV75sVTVdcuRBBeoUAjJb0xnIMXCwldsH6701aHPssM2_lsRN4kMwyylPvOJUZEHnGnOtAf7F3Z28c0DqxKiR4hrj45Sem0c-IOXZiC2jd0s7zjubip1gfNqZBeNgrZFAqcSsoVKdrbyRsYa96hZojLH5CaL48LcVUVcdxI1xm2_yruCvGjmWceOeO0vx0bG9ipocXe3OelBLiHfK-7E8tJiFrMKDT6nyYCSe3MFxOeZUfj5Zho1GDAGxwRz_Vdh3O-nzpecLE229kUw8jM0kebOoP5XEmm7OVCXxKWRaqQIgr86z6rRYGorg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=jQsCYgoUwyjqzivWH-3jS5-ot2dsivV75sVTVdcuRBBeoUAjJb0xnIMXCwldsH6701aHPssM2_lsRN4kMwyylPvOJUZEHnGnOtAf7F3Z28c0DqxKiR4hrj45Sem0c-IOXZiC2jd0s7zjubip1gfNqZBeNgrZFAqcSsoVKdrbyRsYa96hZojLH5CaL48LcVUVcdxI1xm2_yruCvGjmWceOeO0vx0bG9ipocXe3OelBLiHfK-7E8tJiFrMKDT6nyYCSe3MFxOeZUfj5Zho1GDAGxwRz_Vdh3O-nzpecLE229kUw8jM0kebOoP5XEmm7OVCXxKWRaqQIgr86z6rRYGorg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای عجیب یه آفریقاییِ سیاه‌پوستِ ساکن ایران:
خیلی از کاکولدها به پیجم دایرکت میدن و اصرار میکنن که بیا وارد رابطه‌مون بشو و با زنم بخواب!
حتی یکی‌شون می‌گفت هرچقدر پول بخوای بهت میدیم تو فقط بیا..
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71225" target="_blank">📅 10:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71224">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0R12UJdAOXOEH2OIiExy9r0MH4wK9stqwgFHWVSFEZ0bbJBLLa9jt1xngPdJuMJcmdNNQmvXakSRtsIrE7swnABzaLSb7PHCugxCw18DLgwzpTIS27-8zjcjEzqxJfxri7zrb4-8C_7l2PJl7F-h7fnbqrMFnyrexxZFa7ysETIRFA-ra9e5bUD6FIvS-85Z4UpnmGb2N0K0LCKelqhzYLLyuEGgAnTCXp5HObnqQ_fVnCMrYo0tFg5FURPp-P7gWOIe86rpiOm2MaLx2mOPpC0KnyhsS6vkkM3GC9-dRLo5xXBV7P1bF7AYdhEvXjgKO4loqEW0vx9BM2jT6GriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
شاهزاده رضا پهلوی:
هم‌میهنان،
جمهوری اسلامی بار دیگر با افزایش قیمت بنزین، هزینه بی‌کفایتی، فساد و جنگ‌افروزی خود را بر دوش مردم ایران گذاشت.
همان‌گونه که در پیام ۳۱ مرداد گفتم، گران کردن سوخت در شرایطی که مردم زیر فشار سنگین اقتصادی قرار دارند، اقدامی ظالمانه و خیانت به ملت ایران است.
به رژیم ضحاکی و رهبر مفقودش می‌گویم: فقر و فشار اقتصادی که بر مردم ایران تحمیل کرده‌اید، نتیجه مستقیم سیاست‌های ویرانگر شماست. منابع کشور متعلق به مردم ایران است؛ نه برای پر کردن جیب مافیاها و نه برای تأمین مالی تروریسم و جنگ‌افروزی. اموال غارت‌شده ملت را بازگردانید و حمایت از تروریست‌ها را قطع کنید.
گمان نکنید با کشتار ده‌ها هزار میهن‌پرست توانسته‌اید اراده ملت را درهم بشکنید. آتش خشم و اعتراض مردم خاموش نشده است. ملتی که برای آزادی، رفاه و آینده‌ای بهتر ایستاده است، در برابر سرکوب، فساد، بی‌کفایتی و تحمیل فقر سکوت نخواهد کرد.
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71224" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71223">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIfwpndiktSsg_QcVjeJ8enVHhHhDkxBf4yfj3WhW98NEjEAUOsavJ8prc0LxKuoi6ry6_hq0xc4tdh8U_Ym6s_FjOg0EnwioQp4RFPN6BChogS7l4hkYIwcqBi8DHGuliXS7-2GIQeqqMrqu64XT7-Hbl83-25NhHLfrYC4o_rnaCA5azqFgC19Oa0N4GnzCktunuzxVdwqNy3F8NsvuuX05JBWHm7FG0umnEGgr9TY26ip1hm1TcW6mvn8K_jBRLAYo2EmtpJ3jQdcWn-qYmZf63C8uAC0R7UC5BTPlqJ18pCdkTUPUpmmx4k1Zh2wTD6mHaBRh8avBiZm_loOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71223" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=EtewSsRQGyD2lgXhnuz8fNVW6pdGjNBuvm2vT-NWDw8c77IVXRCEl8VGfyYlh0HL5JvlVLhf-chbajBY4gyVK0ksomYa6PxzljYw3dgidtQOco0tlbI3IR4xo-lRCz6WvP9ETnWUlIQRCLClWiRk8-seffdoqsdHUmvT7CtYC2MePg3k9IPqvWvjbH53oaXOT8cWOkHZtHNOIw_kXEGaGQdJBZ1kk76e-FpVaWutzJ-p9HyV4Ges1fI9WdjkpBk_6JkXa3ZOmKG_vGjAkE2AkoE5iz6J3YiwI4jYB9yWiYfGUdEjKxWfklQMNIuGokb1Gh5lI5G0-gYE1sshBCCIXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=EtewSsRQGyD2lgXhnuz8fNVW6pdGjNBuvm2vT-NWDw8c77IVXRCEl8VGfyYlh0HL5JvlVLhf-chbajBY4gyVK0ksomYa6PxzljYw3dgidtQOco0tlbI3IR4xo-lRCz6WvP9ETnWUlIQRCLClWiRk8-seffdoqsdHUmvT7CtYC2MePg3k9IPqvWvjbH53oaXOT8cWOkHZtHNOIw_kXEGaGQdJBZ1kk76e-FpVaWutzJ-p9HyV4Ges1fI9WdjkpBk_6JkXa3ZOmKG_vGjAkE2AkoE5iz6J3YiwI4jYB9yWiYfGUdEjKxWfklQMNIuGokb1Gh5lI5G0-gYE1sshBCCIXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک سرهنگ ارتش :
از فرمانده‌ی کل ارتش ایران تقاضا دارم، یه قایق پر از بمب با جلیقه انتحاری در اختیار من قرار دهد تا خودم را به ناو آمریکایی بزنم و منفجرشان کنم
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71222" target="_blank">📅 09:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=TZ_grNtz53sKbLuuoPT-XTHI-0Yh-9d2UvguoSzBFFbUd-0o70WHtxSuketPBLq6TNbbccCeFMtFWR_ul34XBF1L6EzmFahUin4416RA2b8cL2gKN4EtxiR0y5oUKkuh6hRvRtE1dqS5SRKW1FMisJx23RSgNpLv9D1vvdVQeB3Mk2Ozh8HWBHVkaF3C5CkB1_OLf_-Ubypc_fKa49K4E1UnrF8q28JSMVwNW4QghBV0hkZyUiTxVZL1GR69SsP8JCBwW7oImAD7QWD2E-W9retSesHUr8oPW9lAGUrbIWPljDOCL1SRoDkRKqNSsCKnrnlfHX0PM1_UDL1T3qdQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=TZ_grNtz53sKbLuuoPT-XTHI-0Yh-9d2UvguoSzBFFbUd-0o70WHtxSuketPBLq6TNbbccCeFMtFWR_ul34XBF1L6EzmFahUin4416RA2b8cL2gKN4EtxiR0y5oUKkuh6hRvRtE1dqS5SRKW1FMisJx23RSgNpLv9D1vvdVQeB3Mk2Ozh8HWBHVkaF3C5CkB1_OLf_-Ubypc_fKa49K4E1UnrF8q28JSMVwNW4QghBV0hkZyUiTxVZL1GR69SsP8JCBwW7oImAD7QWD2E-W9retSesHUr8oPW9lAGUrbIWPljDOCL1SRoDkRKqNSsCKnrnlfHX0PM1_UDL1T3qdQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان زمان انتخابات:
خیلی‌ها میگن من اگه رئیس‌جمهور بشم میخوام بنزین رو گرون کنم، ولی من بارها گفتم بنزین رو گرون نخواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71221" target="_blank">📅 09:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71220" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71220" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abWfHCMSngtYcXsFc2iAC1hEd9XaYyw259dy124FhVK5hx8bdS9TcPEVBkQ9kpjDBXvo5YwMj2gNCDkVb87YrAps0XYwvitcH46AOLXCdiLBxV7lWiBvisTCfKgsP8rOV3pnMRcvytXYiDf77eTnRoS4T9otEKRcOl1tfsJm8gEuR1LNp36hKWZK6sjYFO-ph0n0QXV2t7oa6BE0D_NGHWRldJfKNxYgPm2WReL1N7QrBGUy6Ke3CcdCJNpVZ7WuJ0tBKzh66XY_5PUy9n4xAbyakO_xM33B9zRbbJQ0h-SbdcxwOfYqRyj8_Z3gMx7R_fUL78EQjmFXdlju4iMuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71219" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71214">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0E4xZPkAc6aZT3ZofH1g_ie-1A0jh5qbj4O08C9KZV0OZ6jFQgjiD6d5SmJqfEB92JrYXIez55N6xI4oeHdeFCUGTZuFQr-XKqX4mPvE1lVOIOZrXfYPzHSq4Upsoa2DnapzDHdsJhj3_oQU3j-dQNiftgxll9G4lGEaTGPfiogPX7y_BwllJIdE_N6u1Z22z6_DqUfFxIsqffF7S3M8ceIz741cwZzP4mATohotkIqiJswXn1MxcrPWiHjTO41UqRG1uKdqHIDzptFLFYxR3OYuum9wN9i6XuP6oQqOSUNU0pY5Maa7ZkPkehp01FA6SRkHpAM_wy8ikP5cf2pgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjnSiCh9XFlg9pCkg7xn-wHcRQsXyOh4ULbOzqcSd1Rw2T_p5vgRgN59s-0UuVfFT04OuURnTtQeD6HPD-yrfOR1oWRizc1JkT0X1DV2Smw0OeLokl3VoVT3Q7AEjJyeeKRgQ-oeKnLoHOF0Ij8RWbgTdxK2HjmsUy4tHKLgihPMsqJYOgt2bzCFJAyPV9y0_Mx1ON_8ZrlZT59xdzVbReHf-Xxoy2z_W6rBg1wBRNqLelnG2-vNLBxsk2BUyDUWqj1qMS_McQjKLJncQd0lQt1Wyhd2upU_w1S969XYy4CsRYpnorNQW-RQvcobivPuwTwr0G7iZPU7lZsguW0lEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9zTAgICxK6ne7zMlyWPhAEwUHmUAD_uGm1fSc81e7pRVZSqwSXx4WTDCh_WHWdnVed62vn_-_keD4lHlqvQ3VCOnBnsvXDMquFS2_IhMysCKX3keR4OsAjDEIPLRMB8ram_x5GtlnipSOqU7A2tUwINlQEnbEipSK37TSlhrcW_jEznubCeJTY2r1f29S07s-EFAxWnnxcfZeMslAb5JAc49fdZ8pykdI-YrS5bfL3klG85xATT5IOCptUo0vbXNezhuWkCjRJJH0kIo9semjpvlLBpPd8jRgFLiQP56P0PN_amB8l2yXVHp7DbAcyY3e9xUWRofjrCWrhGlC7j7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhY0N0_-hSTOIG5IeSPqwwlaTHKv4oxqzUz8o_-_VqRs4RxhytnXNQF2Wxvx2VzXf1WL9TIMMXt6nuxhxr3WuIySnpk6SCzShT8Jg7Zkkaf-9ldSuy1gDBT7Z-TSVS3bZy2WmOaNCV3ciC5bAQZSm5x1awnMAZz56Imh3mCBVJojQkxY-7xdsZn5qP10ndCOPm2GHsNGKvT0TuanHORfJkrZImwpeOMQknlsMQ3plLwayLZdqayW6BIA408rRvp9pOE_xK0SLNXaY7PjRObQMkJrnzBhf5wwpnESs_MAsI8lU93Pn5pyR5gi9PyZhrVnictqDpfJmv-SabDdz-MJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoYHUb-4FFm8B-cx34VISggXutLcwvZU3y0Wptq3bCU7rgJVQaHYLpKemkTqot_Uh_V9ore6mLwedWir1aoOocInRVaGxzVhO-Pgo_Lc8uESkt9O0q7D_Gyo1mU6lbC-Pzmad-47U7aggfiytTde19xa0LbDIxoLL9YjpmiOBspgEEXj4YxDJ1ozKND_KFzg4e6icSY6v9ZuvQgJ-nFAbzwC0bUmHDVeLBDaLr9jzomfK0O2hZvhB87EtOL0QDwnfDyIT1SEe9gUMJdR22Vf4UXufTL0eEUwZRj7_cdeo5N0-yMqD9NY6QfWarMuWQdBE-4Ftu4S_YT6zEb4tmKV4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ:
۱_ایران کشوری در حال فروپاشی‌ست.
۲_خداحافظ جزیره خارک.
۳_ارزش پول ایران از بین رفته است.
۴_صادرات نفت ایران به شدت در حال سقوط است.
۵_ حجم‌های نفت هرمز به سطح قبلی بازگشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71214" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71210">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUzHzQVto53Di7K_nZNNiX4Y_ageeh1jmnoElFKaWwMa5jAuVk0IeT_5jTjsnS9aGEX1PbeFXxNcvFtZeQRf52ykxt6qPETT3K_02ehDKSs--r9IGOyF5tvxWPzKo1GKuzrPBYv2OHLPGyUW2YRf8rnoJES_WxvmJfpdRFGqP2x2EkPbj1i7Yb3QF2R7nDCuASKQF_B6cAgs6L-Uj9bpLDV8h8xh3TpocMtVrsLExFMWEQZojCbzxNxRcxlV89cCiYG5FIkyghwxgeZpytWIIfh4oGEOKAckzvW4Sa_GLiyHwFpZhZu2NbejyNoAE3dsPOBag2EPqg0S-Ju4QLhQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rw2-HnXlHP_ZUen8-4x-cGA-cmAQQP7SIQnlLZJzTtsMVsJx6RnsOCA_OCbSiPggCF7QiR6y8kpFdEexr91Us-MK7OOIK3lp-XQcHHaDzS8ttkiK2s_W5FP1HZJEGKMtME_vY7c-4N3LFuUlsFeDGfLxqDuwsPnxzbB9oelQziFWR_yt5KaRmEqXbOddkzpGhjXIkSrix6iZsAgwXCsQe7BKKAeJ2niO51ccymrlyfyZpI_1OZm5BAiuo6Ff_3Fr5fBB6vr6ppNkFdt3CUrj157ZDYx1zsy_R9ssxVoaDGBTV0POk3XvB_z2lpQbK2wsCAodKkhuQ8LN1ALobtDULQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ در تروث سوشال منتشر کرده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71210" target="_blank">📅 00:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71209">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=D9KXzmJGynOXAfDoPJA1Vde7JiWmeP7C6B8014lxWsDgwV6rU1rL04KkkUiBTbELvizQgiPRd06me61J0RVYenjXpR0z6IwN9KIrXYlHBX17K6_Zkm0-GYVQ4xaitqpl386a4kZEKC6ZZwzmS99xIa2SykKxt5qeDXeEd51ptzdRoBSivq6r9LkZ4aDPTdwrm1YFpPecUexiiRNjFE2P33KfaMHJkUEtt2P2c7BLTD1mjkCtM9jGckgOV5JRSI8tNYiSPq1EY6PttbBu6QWVz8LupOy_e_eXkXdru1HE2fdAWx9x-nRcthxU-d-SrfjXScKKJeIxqjJWGu5o-A0FWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=D9KXzmJGynOXAfDoPJA1Vde7JiWmeP7C6B8014lxWsDgwV6rU1rL04KkkUiBTbELvizQgiPRd06me61J0RVYenjXpR0z6IwN9KIrXYlHBX17K6_Zkm0-GYVQ4xaitqpl386a4kZEKC6ZZwzmS99xIa2SykKxt5qeDXeEd51ptzdRoBSivq6r9LkZ4aDPTdwrm1YFpPecUexiiRNjFE2P33KfaMHJkUEtt2P2c7BLTD1mjkCtM9jGckgOV5JRSI8tNYiSPq1EY6PttbBu6QWVz8LupOy_e_eXkXdru1HE2fdAWx9x-nRcthxU-d-SrfjXScKKJeIxqjJWGu5o-A0FWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دو عدد سیب زمینی 100 هزار تومان؛ اینکه قیمت یه دونه سیب زمینی بزرگ‌ به ۵۰ هزار تومن رسیده‌؛ یعنی فاجعه اقتصادی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71209" target="_blank">📅 23:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71208">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=a6S3oyIInm6T2swhh3VcQJpgy1GnmZTxilsiEpCmW8KWnIKtt3QonXjPnJH2nh2ouzkksJlI7VYQ1knnioaVrNF0x8iRkOrKzSMB4Sx5P1HinjgYw-oZ5taps7SZOIZIbAc3BaXZ97ooR33vLEf1Du4Dyepfm32iOnleslHaxORwS3iV2lBEvsiAgK6ArvwjRWpx4BTcNndDhSYDcuqPbfQu-cEZcdqbxySAq0u3qwDWPETI4njsouHnkdsdYLxRenYZpGnXkmszpBVENBrKS8f-y1-CsuguotxbTtXFH8qfhRTZS5uicVtWBFknb9ii8WFrlEAd51rpzgNMRilQGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=a6S3oyIInm6T2swhh3VcQJpgy1GnmZTxilsiEpCmW8KWnIKtt3QonXjPnJH2nh2ouzkksJlI7VYQ1knnioaVrNF0x8iRkOrKzSMB4Sx5P1HinjgYw-oZ5taps7SZOIZIbAc3BaXZ97ooR33vLEf1Du4Dyepfm32iOnleslHaxORwS3iV2lBEvsiAgK6ArvwjRWpx4BTcNndDhSYDcuqPbfQu-cEZcdqbxySAq0u3qwDWPETI4njsouHnkdsdYLxRenYZpGnXkmszpBVENBrKS8f-y1-CsuguotxbTtXFH8qfhRTZS5uicVtWBFknb9ii8WFrlEAd51rpzgNMRilQGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سعید لیلاز، اقتصاددان و کارشناس اقتصادی:
«کشور با تذبذب و دودلی، مس‌مس کردن و فس‌فس کردن  اداره نمی‌شود و حکومت باید تصمیم‌های قاطع بگیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71208" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71207">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQwqT-5mZKUoKGPNpvxpUtvzYUGDcRLUSGxvz_yvDA_q8tiJQ-VssuURW8cJTu6b2R2_OQ7zmBDe3kaBXZQqhW1w_bXrvRVr15YmR7pPPPXpusxFXhchDQW78m11wF9Hp2AeLSxL_X4O1OTu5Tuwb7JBfI7XTljZzaO7q2YhkDtPe3fuGiwH7hOLzOd8ORwSNWHmcorVEJNrCcbixcSquXftGRw2In98HGSoFxkUD3N07u6clljF3gTEADYXI4rc6bOQInDBXMjLhyRGY45dQsmCTIQ9Z-2Y5zHyyf-QmkYdWSdN4WfKuNM_8ovhdDcAv70sL6_tsG9-o_SFfXnGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث که اومده کلشو جای نقشه ایران گذاشته
😟
😟
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71207" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71206">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=O1xyQHC-Np2WgRJ4ICJY5XW3HyHZEzCzKJWtVkE7lwowQk9Y_-Rej-R9aJKPCKf6-2_apZyW7R_ht9OAJklWU8oSy3yCoY20IIIOg5REjyYyVSkCJwNaeSUCx6tHuZwuDDyE-rodAV5VFv-aSxdSMaOLRPS8z5LhOg4rd-xaAhXd2ZaYn6-EiL9rzDereGE25PnTZXjChiVTv8IEssZnw_74IpgEmHLcOemhSB1sRToCe-qbJvUpnc3ng58AwjW8hdFqDb2kvmbNHq_Yn6qbpVhXiZgfXwjAQYBdTsNOxWQW86UM8l8dceNfJUwh0gG8o_SwCPAz3egn7O_WzVih3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=O1xyQHC-Np2WgRJ4ICJY5XW3HyHZEzCzKJWtVkE7lwowQk9Y_-Rej-R9aJKPCKf6-2_apZyW7R_ht9OAJklWU8oSy3yCoY20IIIOg5REjyYyVSkCJwNaeSUCx6tHuZwuDDyE-rodAV5VFv-aSxdSMaOLRPS8z5LhOg4rd-xaAhXd2ZaYn6-EiL9rzDereGE25PnTZXjChiVTv8IEssZnw_74IpgEmHLcOemhSB1sRToCe-qbJvUpnc3ng58AwjW8hdFqDb2kvmbNHq_Yn6qbpVhXiZgfXwjAQYBdTsNOxWQW86UM8l8dceNfJUwh0gG8o_SwCPAz3egn7O_WzVih3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مجری لبنانی:
مجتبی خامنه‌ای، رهبر عالی و ولی‌فقیه، اگر به بیروت بیاید باید بداند که هویت ما عربی است، نه فارسی.
بگذارید این را به روشنی دریابد: اینجا بیروت است، نه تهران؛
اینجا پایتختی عربی و آزاد است و هرگز به پایتختی فارسی بدل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71206" target="_blank">📅 21:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71205">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
⭕️
#فوری
؛ نرخ سوم بنزین تغییر کرد
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71205" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71201">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTD2WHOB7FUmO3vVM7kjXVpVSvDZuyeMFGqCDWCEF-e4f7dXUg1h3gZkX_Npy2NIp2BtCNCf8YBI3ksvBymajT-NcqlmcWcgpg20CRWBbFmBpwKeWoX--ywy_DGVy55SvRevtUOU678oOUz-eXgcBieDY7cqIbfCDs6ESINbhq7j_33hCOyYkX9Uyp52v0Gpefa-HR7LYxeG5krD0pqYnm_iVjgVo7K0VBbfOe0DCrhYxpF1WAVcgkmEECr1rxshbSQYNvHC4tgpgVMomMw7OrUq2uXiUsai8IawRtSSS8aDLe6wp01RhdA_aqMltum29swT6NJfEUiW7mgTSQwZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhjO_2ccvWUuA8-bf_kSnqWOsau72mJV0haiIp7RyedPgs7TRTOyh-6JBA1iSlNMAn9rRSlfXLunln4oSWPa_l7h6WKUh8gBUd58m-0mfRkarsde7W_eijRKNbDZmMMGxP_TKqvvySXSPNo8Hs6cSUp8oer-K_RoI9Jrn7bvPrlMpXrtNyRJlzGu2wYDnaWp4TFYtvt84aK0QX6-Ct1M4BCW2znIwbo7dFTOi9yooNrdv9SCG4EFXnnam8haWQKAnGwJPaML_ZpBiUxITimuE1H6JSgUFTfc5ffx0Lhe4B3N_DTXDCNfEpMPNexvlidWLP5XSPZT4bDQYOikXbWkaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=bwQCQ-7mPH_grdRBBDJCsEnRuEuts-PZbr3E2SEx_Lby_bTxfgtDha7yAbw3y8asY68y_K9vE53Vkpqe8Hk_zSvSUM3zqXA1U5XdDgjoz1OoAeoVxsydAPFXEs7Nw347ocwhaN5DSV09jU__PA_WULI6PkACCC0uK1c61S054TSFu_c2rACgEwisgFbtGTdFZrYA67AwX84P7qp4tnJGzezkP-1IhhSRziZkwn4J-mrUdvcQR38Wo8umREzQ078LpXgEhA7-98FVsXG9_opV4YWS0ik_rzCRaOX9EpiPg_ThXxjR4BQ03vnoafOFXYzLGiOfK2MBDInrfTaI_1ydYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=bwQCQ-7mPH_grdRBBDJCsEnRuEuts-PZbr3E2SEx_Lby_bTxfgtDha7yAbw3y8asY68y_K9vE53Vkpqe8Hk_zSvSUM3zqXA1U5XdDgjoz1OoAeoVxsydAPFXEs7Nw347ocwhaN5DSV09jU__PA_WULI6PkACCC0uK1c61S054TSFu_c2rACgEwisgFbtGTdFZrYA67AwX84P7qp4tnJGzezkP-1IhhSRziZkwn4J-mrUdvcQR38Wo8umREzQ078LpXgEhA7-98FVsXG9_opV4YWS0ik_rzCRaOX9EpiPg_ThXxjR4BQ03vnoafOFXYzLGiOfK2MBDInrfTaI_1ydYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
حملات شبانه جنگنده های اسرائیلی به ارتفاعات علی الطاهر و نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71200">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a237cee509.mp4?token=HlHYvW5vdNguWxxGXwEc5KxY0-Syxc3KQSR11RzJHjmAN0JMqzagb7l_0DhiH0kGewMa8LiwycJPLeM3AUahAaPFRGqyzYUrDzbiCb08UYG3ttF_6Otk8Iw6VD07RF5tN7H4s0lfEIf4u1suu8VaA7y7q0eEg_Nj2S37OevRAAV4L2rHyf4dr5krPJiaV7HsnfVadc30D1VutEJzELRRtp3M6knoDzA5KcssNEUrnSSsK4_Rlb1-BmApmjZQENQ6usN-jg8HOXWCZkGGx4Zv9eRtUk2Kv1UAHjsKc81UK1giV8CovLqIVgvq3EXEEF8umtaKNQgafWdrDBJWqigJCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a237cee509.mp4?token=HlHYvW5vdNguWxxGXwEc5KxY0-Syxc3KQSR11RzJHjmAN0JMqzagb7l_0DhiH0kGewMa8LiwycJPLeM3AUahAaPFRGqyzYUrDzbiCb08UYG3ttF_6Otk8Iw6VD07RF5tN7H4s0lfEIf4u1suu8VaA7y7q0eEg_Nj2S37OevRAAV4L2rHyf4dr5krPJiaV7HsnfVadc30D1VutEJzELRRtp3M6knoDzA5KcssNEUrnSSsK4_Rlb1-BmApmjZQENQ6usN-jg8HOXWCZkGGx4Zv9eRtUk2Kv1UAHjsKc81UK1giV8CovLqIVgvq3EXEEF8umtaKNQgafWdrDBJWqigJCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زاکانی:از وصیت‌نامه علی خامنه‌ای خبری نیست، احتمالا در بمباران از بین رفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71200" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71199">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90305378ee.mp4?token=qj5d7UlM4CwEMDWEMji62EEGHMcUZNiYkSb8nw48gfk3pK_GEOwn6_WxgzHbBoCC6JPJXumgDIRsIsL37cEpeCUy8sOh3s69K0bO7bOJaIKqhR-8i6vgkfD5EmKZIxtDhJgSx838o0HQUOC2Se6FUqREGQydGvI5a7_A7fnYwRH8MrdBS5EjzsKb8yhS4njDZzm-zWLG8xOWVXFpoxG0GYoVi_5m6VFzpxG0YzbnmCmdilZfSMXS-Nxrjn5bsmTgNadovyOi8vDeMSPsQMx9CVdp3sC38seZKj_KmEiokIRlZJxQZl5Qf2Ceet6BE6IjpIF07HimpUchCSTMFlNhaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90305378ee.mp4?token=qj5d7UlM4CwEMDWEMji62EEGHMcUZNiYkSb8nw48gfk3pK_GEOwn6_WxgzHbBoCC6JPJXumgDIRsIsL37cEpeCUy8sOh3s69K0bO7bOJaIKqhR-8i6vgkfD5EmKZIxtDhJgSx838o0HQUOC2Se6FUqREGQydGvI5a7_A7fnYwRH8MrdBS5EjzsKb8yhS4njDZzm-zWLG8xOWVXFpoxG0GYoVi_5m6VFzpxG0YzbnmCmdilZfSMXS-Nxrjn5bsmTgNadovyOi8vDeMSPsQMx9CVdp3sC38seZKj_KmEiokIRlZJxQZl5Qf2Ceet6BE6IjpIF07HimpUchCSTMFlNhaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇵🇰
بلاتکلیفی بیش از یک‌هفته‌ای صدها راننده ترانزیت ایرانی در نقطه صفر مرزی پاکستان
این سنگین‌سواران ١۴ شهریور در ویدیویی گفتند که بی آب، غذا و امکانات بهداشتی به حال خود رها شده‌اند. با اتمام سوخت یخچال‌ها، بارهای فاسدشدنی در آستانه نابودی است و گمرک هیچ‌یک از دو کشور پاسخگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71199" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71198">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بیناموسا مگه نگفتین از امروز برق نمی‌ره؟ رفت که
#hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71198" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71197">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=QJhpPjFBXPH-gOQ2abL5N2S83ipEqwC-YT5bsuuVgUDscsiY6umnxU5QYpBlm-tFaLPoJFpHi8dkrKMJjMak_v8IbJ3DZPs4LxKZlgzWj3A-E1B9JnH1CFFSljI_wtqVDxwdZD5uHPKNplSkOjV8XiDkJXy5EZWYx0Ien5RxKaUTjP-XgQYvHePKL74bzJlewaD9bnJ-j9Z1jgNHCb6zlEByok8sv_Ttn4VUFppVYS1CNmSgyVcLHyvESaMSUYS7RAEghmgU8illxJAMSXCcWdmEEyywFDUmQP4xzGZQLj4ZiR_96hvirwThsG6-cKGsD_2IBIHwDj3qJPxKfdl64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=QJhpPjFBXPH-gOQ2abL5N2S83ipEqwC-YT5bsuuVgUDscsiY6umnxU5QYpBlm-tFaLPoJFpHi8dkrKMJjMak_v8IbJ3DZPs4LxKZlgzWj3A-E1B9JnH1CFFSljI_wtqVDxwdZD5uHPKNplSkOjV8XiDkJXy5EZWYx0Ien5RxKaUTjP-XgQYvHePKL74bzJlewaD9bnJ-j9Z1jgNHCb6zlEByok8sv_Ttn4VUFppVYS1CNmSgyVcLHyvESaMSUYS7RAEghmgU8illxJAMSXCcWdmEEyywFDUmQP4xzGZQLj4ZiR_96hvirwThsG6-cKGsD_2IBIHwDj3qJPxKfdl64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
پایان این رژیم در ایران نزدیک است.
این رژیم ضعیف است، برای بقای خود می‌جنگد، متزلزل شده است و هنوز مأموریتی ناتمام باقی مانده که ما مصمم به انجام آن هستیم.
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71197" target="_blank">📅 19:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71196">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPxauPNQT7ahOsJvfUIZrUKp1EsnrsnWXqROquQIEm09ljYEEnOcI8bPEyTT4SvkXXGhYgf9ze9YDX4zGLzjObO7fdxYJSs97T0mnLN6CVV5Ld76KTs7VmB-OjlhGij1JY_J6delq8f7l8s-FiI5ESmzz0TEnxk8DLMB8fXiVLyVpwWhcq9Yi4xHDwtZ3aawAeHfKTk7toT_lRH_kdFhH0r9td0Fpcx6lmL0mNMAln3vJJa2knvsDlEro616x_ek7eWZI-BeCl664Q8F3OQlTiJG1C1VX3I4cU_IcfXO3IYf69CcYspcsg-OfsDs_wdkqUhVg4MvkK8EAswWSr5NGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیس قالیباف به بسنت:
چرخ‌ها آماده. گرم کردن قبل از پرتاب:
دیزل ATH: فروش فوری
بزرگترین طلبکار شما: موفق باشید با Yentervention++
80میلیارد دلار کاهش می‌دهد: نام نروژ را به Americaway تغییر دهید
استخدام کم: بدهی به خدمات با DO[Israel's]W، طبق گفته عروسک‌گردان‌های شما
اوه. طرح نقطه‌ای فدرال رزرو قرمز چشمک می‌زند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71196" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71195">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srXiaPbUFCn2XX5Eu-vjqxXkE98NbVPIqjc7xsngKM9436cxVlcQrJ_bxm1rTR1QZ3TKaMziAblKeOdaVQ38Nx8bVUD9N0PoreaSRo5pAv9DD8UNb5CxtFOSp1xeIRN6ggAPkam3LYLtoFRUR3bisNZaht_7RhJv11q-Pupp3ZQPKIGXVD16-FWUHCfnNst2fwWoueeWqqKbIu0S9EtwTsY2KSfbXkH9uJnl2K7PTWMOo61wsz2oyUM4yeUP676f6lDrbgMbaB_M81vfaIUqzlOPthEO1ABQQDUe8k0XZcyJjQbnIO_Y7PhkXeTJAIU3Z6yg8LJJJuXkucGpCn4_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
گویا املاکی موهاشو رنگ کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71195" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71193">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoR4kyuTmFdlZfDvx4JzGKCTTD4-RTOViSG5w8biKUX-XKrvzy2K7b2TRBTcAyiIC2b6BSkTDKW7lwFL5QzrTT04u3MG3MbwlHy-ujg_OvS5GNwXh4HV1aS-blnwXu-xBf0oyRMnWQzmGs7DLDOJiUWXoDizwMKjpn3AfU3QbXztIqOvHJyBKWnm54gbvtnR30rnP0mICtV4beoLXmZb5Vm_kGl_h8Cm6tVewrwvktoMBRKLRM2IUuan_0vQpHIKq4dhYeZRPTeybwjj9Uk_L0K6lvD78_TRemDi1VwPsT6t6kxFUtc6clsPX7q5qd9AKm5F5tzpap9K4PB7n3sQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=Qpwy_pOEwOLrSPgInlK8vh9-lUWHtD6de2w-peVTINRZKYsxkOPAVFTD4zsjT0dqqVfIcDYRjw_Pb_78vu1DekRSJd0uWjV8ShSMLCoKgolnYlN0cBhCKGgdB65J5R0cQoaXqoFxgSrAZ2Mw7nRPo0zZRpu3_wcvB8HsSbPxWRPicQO6J7XJG7uHR2gBQdSsIzYFIPa7W9WeFCbDNskeBl_Tw8qZMlC3jwgBmSGddopCEDJ-43X5qICWM23W2mWhIDR22ht2vt1UWDgHlclf2nc4li_ORXrk9ttWOQzHN3NsQciCWMnLlgVWWEIzEqyrd5dKbxxZz8j7cHnkGjaO2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=Qpwy_pOEwOLrSPgInlK8vh9-lUWHtD6de2w-peVTINRZKYsxkOPAVFTD4zsjT0dqqVfIcDYRjw_Pb_78vu1DekRSJd0uWjV8ShSMLCoKgolnYlN0cBhCKGgdB65J5R0cQoaXqoFxgSrAZ2Mw7nRPo0zZRpu3_wcvB8HsSbPxWRPicQO6J7XJG7uHR2gBQdSsIzYFIPa7W9WeFCbDNskeBl_Tw8qZMlC3jwgBmSGddopCEDJ-43X5qICWM23W2mWhIDR22ht2vt1UWDgHlclf2nc4li_ORXrk9ttWOQzHN3NsQciCWMnLlgVWWEIzEqyrd5dKbxxZz8j7cHnkGjaO2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
تو همه جای جهان هوش مصنوعی داره جای آدما رو میگیره ولی تو ایران برعکسه
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71193" target="_blank">📅 18:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71192">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=NTYczLc5F9imu_IcwfedcEJzldifUXxpmPdwijUYeD27AF57w00COdZuZzUi_GiATugLty_0YGS3KWAno3QXZyHv3-VQzE5rZg9IflPftAeyiYioMgMs2IPCoFe8hzT5BwtVZRB5w8-_emxt8t-Qnc5KqYyt-zQqjCfi3njG2jTIA7xOObej3Q3ge9-S4Z_wsanPb69v3k4sm_cTY6d8kL2xccX57WFzcT-xi3BWajbmfqIJpo831XuBttGqqSwFm4ODoOJSMH-gZi36bN-F2MTBiJ8Q541u_Dm2VEut4uYyjqUG2NfXCsGoTrX51-Q9yFCKBj0jEf9oU8UvxmxBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=NTYczLc5F9imu_IcwfedcEJzldifUXxpmPdwijUYeD27AF57w00COdZuZzUi_GiATugLty_0YGS3KWAno3QXZyHv3-VQzE5rZg9IflPftAeyiYioMgMs2IPCoFe8hzT5BwtVZRB5w8-_emxt8t-Qnc5KqYyt-zQqjCfi3njG2jTIA7xOObej3Q3ge9-S4Z_wsanPb69v3k4sm_cTY6d8kL2xccX57WFzcT-xi3BWajbmfqIJpo831XuBttGqqSwFm4ODoOJSMH-gZi36bN-F2MTBiJ8Q541u_Dm2VEut4uYyjqUG2NfXCsGoTrX51-Q9yFCKBj0jEf9oU8UvxmxBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای دو تا ترنس تو پارک لاله تهران!
فقط آخرش
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71192" target="_blank">📅 17:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71191">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=qg7xXpLsLtwoPpQI_poHGTUnGhlwZ7v3_iW444RvSm8EVAqwRUfwh-oP4X7ytkj2t9uxNr1WoGvgldohmcJFvpEbAyDsopDMHdE45bLS1DuuN0xDDwHOAdZS9IUgC9gFR-ZHYK2jQeMUphAprqNM4lJm5XV3cfuV19A_KOkOOsJFccrWjIhdhx3cOO_g9InyhXwj0Ss2labz-nZAxwer69gRiGyUYzdfjEp6IgBPxWTZDD30SkEx9tpcGQSvhaF6qb6gDCMWhYr4-9ot6cUbgKS56SpFJqj2D5XXZdXKe_RKix388vbRJaPVc2gQeAZRBHWWk2tJBcT1btAOvVPJ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=qg7xXpLsLtwoPpQI_poHGTUnGhlwZ7v3_iW444RvSm8EVAqwRUfwh-oP4X7ytkj2t9uxNr1WoGvgldohmcJFvpEbAyDsopDMHdE45bLS1DuuN0xDDwHOAdZS9IUgC9gFR-ZHYK2jQeMUphAprqNM4lJm5XV3cfuV19A_KOkOOsJFccrWjIhdhx3cOO_g9InyhXwj0Ss2labz-nZAxwer69gRiGyUYzdfjEp6IgBPxWTZDD30SkEx9tpcGQSvhaF6qb6gDCMWhYr4-9ot6cUbgKS56SpFJqj2D5XXZdXKe_RKix388vbRJaPVc2gQeAZRBHWWk2tJBcT1btAOvVPJ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71191" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=t5tLUbag1mZPKba7_wl3I8fxvf-rHrzbJV_KZ6uk9TLVul4BecSJxmjwuyz_jhgQHom2y1JgXriUHZ8-SJDG6r05iDF9qdpEj_ZMXtzxgKN5U4_VzSJB6c9vwIc4IDH1CHVvS41Vn3eyGJBy3mW8ncebyzX0H5CscpYjqc_QuwB7o_Qo_TmxOw9HWws0cFzhhGSYQSjniLOOWdHIKh_-fds8POaPi6QU8UZzJo-i9OhKRYbtLBS6a-CzY7FDmmv22qTB3XHNp3rHeHZk7fhC9u_J1oevc5Ub81KG1SvmaLkYcQusumj1iN_cEajKvaLp1aDHHva01_tHEv673WYErg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=t5tLUbag1mZPKba7_wl3I8fxvf-rHrzbJV_KZ6uk9TLVul4BecSJxmjwuyz_jhgQHom2y1JgXriUHZ8-SJDG6r05iDF9qdpEj_ZMXtzxgKN5U4_VzSJB6c9vwIc4IDH1CHVvS41Vn3eyGJBy3mW8ncebyzX0H5CscpYjqc_QuwB7o_Qo_TmxOw9HWws0cFzhhGSYQSjniLOOWdHIKh_-fds8POaPi6QU8UZzJo-i9OhKRYbtLBS6a-CzY7FDmmv22qTB3XHNp3rHeHZk7fhC9u_J1oevc5Ub81KG1SvmaLkYcQusumj1iN_cEajKvaLp1aDHHva01_tHEv673WYErg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
راننده ای که چند شب پیش در مشهد طرفداران حکومت رو زیر گرفت:
عمدی نبود تعادل نداشتم به یکی برخورد کردم تشنج کردم جای ترمز گاز دادم و یهویی زیر گرفتم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71190" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71189" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8EACAfxADTirZpdXlogNmjfiGq32iM7-X-XiJLImOpAnxlQD4M29XJ49zz1n_zOKc7YUZ_htKyQfmgJHMedG7lPcXNPozK5fau2ZsNokTuP6EoL4ABAeg5SvG3tLpH5qA7SUebR7Vn_bvdHHR3K-wEp1B06mp7troUpoDXtG1MHY-zbw33mQwBzxLL28Z2M9Poe39i1x_hzQHAsdYyqvCgP0W9Loi7Upatiwf49hfu9zhQ6dlFoPZYm8ZdUmhFLbkqVyBU6Om6-YMjVzDVH5GFIk3N0Mh3lD1Zn7HE1ZLjNWtVCKnq8IqgvA8AjUotJTGRTZAjZD2Vx-PDiauDHvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71188" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFiIjk8U7hyLlu674xpmUHsg-n7YSNwiAzWHsWacB5Fdixu9p92Mo6bbq40hftLgxbW34T0nBWU3RvNMXe_pXoEq9qZAprm_ojgs-mQgniHwgsBdX9LrdQMFwnQ9wdNHnWNVrZ48qh063L3wPkvCY6DE3yUqYrxxgaxR7w-FV8fEYEYEuz0lLI194iCZw8endy5FVZRvIw5L1OnKuqdI244A0IRaRjrPR-eLNLM1juMQVmmqnyt3gWwd-BkwJRxSeM0Wh-df2XbyRCP_urnkeYYVGboQDVc-EUq_KoRbO8Mgwr8FkLlHHvJEBRTlWF-e-zfySyFFJp9wMXcGX6pmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇵🇰
پارلمان پاکستان برای نخستین بار در تاریخ این کشور، فرماندهی قانونی هر سه شاخه نیروهای مسلح — شامل نیروی زمینی، نیروی دریایی و نیروی هوایی — را به «عاصم منیر»، فرمانده ارتش، واگذار کرده است.
او می‌تواند بدون نیاز به تصویب کابینه، کارکنان این نیروها را بازنشسته یا اخراج کند و یا در خدمت نگه دارد.
دوره پنج‌ساله مسئولیت او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت.
او با دریافت درجه «فیلد مارشال»، این درجه و مصونیت قانونی را مادام‌العمر حفظ خواهد کرد و برکناری‌اش مستلزم کسب رأی دو‌سوم نمایندگان پارلمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71187" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=P3Z7Ij5HOXNR6k5Wt1ovSnkVbJUnfoFtATiXC846oPogSDge8coxLRyIyAkjjh7jZDZ2vWZ7-furPT3WTDZDD9bxnHApo4el63Z_LG6oYryr5VthmoLU_iqwrwrX6eLeOYSPZPUSQAFyiM8Vce56fZg5J8TnjxEnReIY2Ku8RxVDcXSDGEr3K4LbcygO3RZbpNG_PQ0c4kIyGXgmTqgnOBhjoaKShbYIk1V9_jXEJ1QTzYQVxRyy6vKMig_nF0q8hwdvYCqw_A0cDQpEjhO_g0SGKCcNpzoMyv3QC_INh7kYpoXkS3RkUQgSy5nvnqoh3c4agmKoiPZDr3bbytd1FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=P3Z7Ij5HOXNR6k5Wt1ovSnkVbJUnfoFtATiXC846oPogSDge8coxLRyIyAkjjh7jZDZ2vWZ7-furPT3WTDZDD9bxnHApo4el63Z_LG6oYryr5VthmoLU_iqwrwrX6eLeOYSPZPUSQAFyiM8Vce56fZg5J8TnjxEnReIY2Ku8RxVDcXSDGEr3K4LbcygO3RZbpNG_PQ0c4kIyGXgmTqgnOBhjoaKShbYIk1V9_jXEJ1QTzYQVxRyy6vKMig_nF0q8hwdvYCqw_A0cDQpEjhO_g0SGKCcNpzoMyv3QC_INh7kYpoXkS3RkUQgSy5nvnqoh3c4agmKoiPZDr3bbytd1FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMp8EK6EQ62LlIYXQkOVNLberCzxZNnr2CI5GnE-VCsbfYz3G3L6H09VPY-jbPBhxwzM0EZ8JP15GP-U7Fcru3PT5lMFXUb5UeGmOhwsqQewk8TbBKn8lABpkLIfnPS3uyjyfBwDNJLrgf0SkGfjY5ODDbL6JXaaZ4jBipTLS13eoLm_91KSn-3V9CIua-FlIteMzMRD-KN-uuFvck2_urSRKdM743UfGog7JpR5AsR3zcP-Dt8k2yM4laxkC_dfT5F_-fzVxNgwOKuZchRTNGnEGaiKsGBBD2dVGE184P7kCZ6XpqBgoN8MH9zXBeH7ZlTR8jklG5j9ayJdez50pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=LwX44Dh4eHcY3N13M3JT5nMrx1RmZ8GX3IXU474PbXUrb5EwFUngWorCdkgbfQreRW-w-iBcadQ0_5yYEbUonZrCPOkOFjwzB_nsMwAMDyIw6wzPhGTuVWDGKEtNbFoRde79-ybv_kNsNe-hcmQa4mbnSPGdv_jfxTKZElxrYn_4Qgrhjz8mll1bSCsyA__Y0HDjuHrupOcXfmCtJswh9x56AqxEZVqGQZGv-qVyCLurlCMqYACmezmDGMRc6w4p6cwZIO70RPW-MWxPUyjnf5mIW2-8hbxhU0kW20wMamRLOfhC82dBvKTTvEInonZBJXm6kWZcP0lhU3n6GF9hEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=LwX44Dh4eHcY3N13M3JT5nMrx1RmZ8GX3IXU474PbXUrb5EwFUngWorCdkgbfQreRW-w-iBcadQ0_5yYEbUonZrCPOkOFjwzB_nsMwAMDyIw6wzPhGTuVWDGKEtNbFoRde79-ybv_kNsNe-hcmQa4mbnSPGdv_jfxTKZElxrYn_4Qgrhjz8mll1bSCsyA__Y0HDjuHrupOcXfmCtJswh9x56AqxEZVqGQZGv-qVyCLurlCMqYACmezmDGMRc6w4p6cwZIO70RPW-MWxPUyjnf5mIW2-8hbxhU0kW20wMamRLOfhC82dBvKTTvEInonZBJXm6kWZcP0lhU3n6GF9hEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=sCMSzlyn2V3imc4XPmMRoazf-uzUhCpoGnrS8ufpNXxVRTQvZsnnLmhoudcyMekCH79t2AMHbV_pgWgQAxSY_v0pRBnUiu6s2k8BeNUlNcqliW_kuvy2oCnZIiq40wzc_uVX6jVtiiWWN9HsMbtraA7uxxec7xxa3GZTIDMR4andsyvROVXv7Oogjk6att8iYHv0SxvMI4wHbkHeSmFJK3rp5cOqjrj4UrHFkAQpvgcrGfY9lk5VvAQrtUjNObXo92a2p2wkvjGRXNqwL_ZnWyjexhdOnOjz85E5DwjKD8mevNaA7Lxne4dT2r4xcZ2x3GFxhMs4H1K8i1oxZa5g5oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=sCMSzlyn2V3imc4XPmMRoazf-uzUhCpoGnrS8ufpNXxVRTQvZsnnLmhoudcyMekCH79t2AMHbV_pgWgQAxSY_v0pRBnUiu6s2k8BeNUlNcqliW_kuvy2oCnZIiq40wzc_uVX6jVtiiWWN9HsMbtraA7uxxec7xxa3GZTIDMR4andsyvROVXv7Oogjk6att8iYHv0SxvMI4wHbkHeSmFJK3rp5cOqjrj4UrHFkAQpvgcrGfY9lk5VvAQrtUjNObXo92a2p2wkvjGRXNqwL_ZnWyjexhdOnOjz85E5DwjKD8mevNaA7Lxne4dT2r4xcZ2x3GFxhMs4H1K8i1oxZa5g5oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=OkPZhaGsvrJY9WcunEPw76XCMT-4vCGcv8dcshU85eBi5GDb621jqvXmIRWyaUIEPuAdKnd4YvEOl_Veif021dbpBeQ-YBIfnWGhngrt_AwztTPz4de5zH0sOppPnvuFnPr_qqnWZvYNU-2AmRdnkWTRLnNhVj6MRa31TS5xn41MqXLHNBGnSYxnjsiw1Ygt7X_OuXEH4SDpeJ76YU_j60eTnt3dV29NGLaJ5F2aMEWrwEu3Xp0u8YQjxx1GWy_mRZkaYhp8r03nu6ZAVMkE5IJ-424uQjX8uu2YU95qt_EUuAe4Dfux9KyvUFnE6D0Oj5Gqd8hq92SEPmeZpc_6tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=OkPZhaGsvrJY9WcunEPw76XCMT-4vCGcv8dcshU85eBi5GDb621jqvXmIRWyaUIEPuAdKnd4YvEOl_Veif021dbpBeQ-YBIfnWGhngrt_AwztTPz4de5zH0sOppPnvuFnPr_qqnWZvYNU-2AmRdnkWTRLnNhVj6MRa31TS5xn41MqXLHNBGnSYxnjsiw1Ygt7X_OuXEH4SDpeJ76YU_j60eTnt3dV29NGLaJ5F2aMEWrwEu3Xp0u8YQjxx1GWy_mRZkaYhp8r03nu6ZAVMkE5IJ-424uQjX8uu2YU95qt_EUuAe4Dfux9KyvUFnE6D0Oj5Gqd8hq92SEPmeZpc_6tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=GPCWB7Y4IOCxoGPtXoTXOD64sOib8HDfK4YAOfhBPHfOcv-gYMpcb5LlfVu-bAEHNhfHLXpOq5UE7bOx-zpyZNXmhHyBnPza-fe2DgA2iXa-G8io4h9-O3mgVU2rKmhyjtAa7dwgsX6TzcKiu7dchGrU9R6wnGwJB3b1OCqMsE_OZLXYqWhalIsCGezdgL1UH1tJwwRWIKjcYyM_JFc6WOBYJzD5Yxhee30Mh8UjQdk_N4-BWB4HnH5iT4z1AAjDD8L3HlQZaY6KvSN2DPb578wdPBkxsYmRoXfChRwtgFUp6HU0N7IEhfGJDElrrZbukizO-9Vdx-aHuoqtBZHxug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=GPCWB7Y4IOCxoGPtXoTXOD64sOib8HDfK4YAOfhBPHfOcv-gYMpcb5LlfVu-bAEHNhfHLXpOq5UE7bOx-zpyZNXmhHyBnPza-fe2DgA2iXa-G8io4h9-O3mgVU2rKmhyjtAa7dwgsX6TzcKiu7dchGrU9R6wnGwJB3b1OCqMsE_OZLXYqWhalIsCGezdgL1UH1tJwwRWIKjcYyM_JFc6WOBYJzD5Yxhee30Mh8UjQdk_N4-BWB4HnH5iT4z1AAjDD8L3HlQZaY6KvSN2DPb578wdPBkxsYmRoXfChRwtgFUp6HU0N7IEhfGJDElrrZbukizO-9Vdx-aHuoqtBZHxug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jybZ0hKEYvWAwU5Ic1bPV27w8ruvqf9EzrkMJlZFU8BUF8dcOgOKblnXYHxNogA5F-gum1G29IWee3P8OJPEe4TTsSYB20CvUmrRmSzjyQJhWBfPODQQoYd9E7YLpMoReeguF6hPGmJrCO3SJ_chgn5ukNTQSAzDlhYLIH8v9DxLQTUTm_DHXyx334zoJyGZesOs8VhsLqk7H7AlipcHzgg0sfx7-cNVuO-YybWR8EalQ0TrSOeIjtW_lp_2v7a9QIy5ItD3unPOXOfYbzEnu3s5jfNczJTFcqgp59UmF8vzCWk-jtDqyK5BYdutkLNbrfIW_bO2OxJkXix6yNrvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71177">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=PrkExif217XxWt2UrKAcHdza4XCSEGS_2VOfcmrw1KRC4etRQjxs5zQN7iXg7kqt5H2kHcDM_0GZ6-XTLErkjIvW3grS_U4jJT9pwuNOXjGuGuLy5WR5c-uWSrBehjTnvbMzAMBir3hRZE3CQ2odr4i2RnjhFyu_eeKYDmQJWsJCh5dNF7f_l3gTTmC6ZekameCd3K8UInglw64H-DKf_6JTr8dIq7rE9nJVXXku9Nx_mMo9v-40eAl7ka0ceqUeOJVwjLTXhkUzb2S3J2Q7qBtqZ9jBykoDRitM8MV2vorsDaXuVNLd6rgWTyGJJ0NgVgIpu1j2w_fvIV1R8q65oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=PrkExif217XxWt2UrKAcHdza4XCSEGS_2VOfcmrw1KRC4etRQjxs5zQN7iXg7kqt5H2kHcDM_0GZ6-XTLErkjIvW3grS_U4jJT9pwuNOXjGuGuLy5WR5c-uWSrBehjTnvbMzAMBir3hRZE3CQ2odr4i2RnjhFyu_eeKYDmQJWsJCh5dNF7f_l3gTTmC6ZekameCd3K8UInglw64H-DKf_6JTr8dIq7rE9nJVXXku9Nx_mMo9v-40eAl7ka0ceqUeOJVwjLTXhkUzb2S3J2Q7qBtqZ9jBykoDRitM8MV2vorsDaXuVNLd6rgWTyGJJ0NgVgIpu1j2w_fvIV1R8q65oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام ویدئو غرق شدن نفتکش ایرانی در دریای عمان را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71177" target="_blank">📅 13:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71176">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
آمریکایی‌ها باید دریافته باشند که دوران «پاسخ‌های متناسب» به سر آمده است.
حملات ما به پایگاه‌های متجاوزان تنها یک آغاز بود.
قواعد بازی تغییر کرده است.
از این پس، هرگونه تجاوز به منافع ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر در پی خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71176" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71175">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=hV-2-h80rwyH7Ap-4oFJvEbwX8d2BiCGRjxPE-Yycj4Fyl3qde9bSu3BDJFbMNFW1p3_XOQWvdMO1-ESA6tF2_-LeIWogu9QK482oV5aYb-n38o1C1wxxat9SiXViZvrKiUFSdL0lbfz7Gc_pBvuT2mztI_t6YfpCQzQyN4viUev3tSdVcACIc5Rc-iFv4k-oKjvyn1S-nYahslmBBRMVREozqEewClk2AK5YyxuG5s00hBJpHSMQmps3_mx9TWSs2kbjDWXXL-NkbB9xom8ECjIM2IMWVjPLRu1gudzFg9Ug28NUow6015_hD3Lw3zpKUb2euNF6PWMVEIb0idVmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=hV-2-h80rwyH7Ap-4oFJvEbwX8d2BiCGRjxPE-Yycj4Fyl3qde9bSu3BDJFbMNFW1p3_XOQWvdMO1-ESA6tF2_-LeIWogu9QK482oV5aYb-n38o1C1wxxat9SiXViZvrKiUFSdL0lbfz7Gc_pBvuT2mztI_t6YfpCQzQyN4viUev3tSdVcACIc5Rc-iFv4k-oKjvyn1S-nYahslmBBRMVREozqEewClk2AK5YyxuG5s00hBJpHSMQmps3_mx9TWSs2kbjDWXXL-NkbB9xom8ECjIM2IMWVjPLRu1gudzFg9Ug28NUow6015_hD3Lw3zpKUb2euNF6PWMVEIb0idVmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:بستن تنگه هرمز به ضرر ایران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71175" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71174">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=aIsrDVJeSkt0L5eQE94lACQF5x-2xUTz3EPZFRMwXpUUa6-L838CWTSrKRoX2COvStBfapUvzp06zRLXSpigupg2FpqXCkA8Etp2y2AzfRnLUyCdBiNwq-5uXRM6VaDdmIJZ2za5ofwE9tvdWBMTkMwM5YciUE_CHjU1cWRaJXUnzzos1YVBD9XZcSMg828MWghG2IlTLOVVih0Ku4PIc4oOEQrRKY4i9YTrVaQ8qVzk3N8OO6j9oRrUqKrBSIjaOCZyaJzv4DbW52yRCpEmCv7PnWYs9DIpCO2vVSC7Y-DcuOFtREpY2NS9N88zOVLyC-QNTJzxiIJTfpvCHXYphQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=aIsrDVJeSkt0L5eQE94lACQF5x-2xUTz3EPZFRMwXpUUa6-L838CWTSrKRoX2COvStBfapUvzp06zRLXSpigupg2FpqXCkA8Etp2y2AzfRnLUyCdBiNwq-5uXRM6VaDdmIJZ2za5ofwE9tvdWBMTkMwM5YciUE_CHjU1cWRaJXUnzzos1YVBD9XZcSMg828MWghG2IlTLOVVih0Ku4PIc4oOEQrRKY4i9YTrVaQ8qVzk3N8OO6j9oRrUqKrBSIjaOCZyaJzv4DbW52yRCpEmCv7PnWYs9DIpCO2vVSC7Y-DcuOFtREpY2NS9N88zOVLyC-QNTJzxiIJTfpvCHXYphQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
ویدیویی که در توییتر فارسی به شدت در حال وایرال شدنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71174" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71173">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=P_-zZnBzIXhNpQZp7mD2zxgDwzbgnz0FXrt0zp7rYLvAevAHjrulN0rvLKPvST1EKC6O0qbd2IdIRifGBXdBDCpxCttbnpkptYtprYRJVhn3zcv2u6lyLTg8caqxt5hsdxyJCl5z4nj9LWGiMGqLmz6y9Pl5NAO2F_4rfaj_5XSAVkq3VAaEIpNL4TCxrCESyx417S2UB2Ue8MGqOmDx3WryLZLrNGGD04czatPKdVeidJg7E_BRK7oTAEs-4PTGZNI3s7s2-_AR1k6GBAB_gMFhujufXOYez7QkVJElvTB-4xVJhNfsYRJfQ9vh2OCKA5v_dNxcOuo9P_HWE50sgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=P_-zZnBzIXhNpQZp7mD2zxgDwzbgnz0FXrt0zp7rYLvAevAHjrulN0rvLKPvST1EKC6O0qbd2IdIRifGBXdBDCpxCttbnpkptYtprYRJVhn3zcv2u6lyLTg8caqxt5hsdxyJCl5z4nj9LWGiMGqLmz6y9Pl5NAO2F_4rfaj_5XSAVkq3VAaEIpNL4TCxrCESyx417S2UB2Ue8MGqOmDx3WryLZLrNGGD04czatPKdVeidJg7E_BRK7oTAEs-4PTGZNI3s7s2-_AR1k6GBAB_gMFhujufXOYez7QkVJElvTB-4xVJhNfsYRJfQ9vh2OCKA5v_dNxcOuo9P_HWE50sgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به گفته آقای دکتر اگه می‌خوای سرطان پروستات نگیری، باید ماهی ۲۱ بار سکس کنی...!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71173" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71172">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b321711db4.mp4?token=OdLyg0HwYtC9oRbffM8fcPGu4EId9qE6DovNLNIs7tLQFfaOJ04sJm0Q8rETrYi5JHG4_97X2pSFBz3iRKj_tyssmTYTZHDUYbFWGh_QtgUrMdKME7mg0QN0PHmUjneKB8hxL03Cc1LH3F1awekeprk_b22bM9lZls-66lc2kGknA3KqHOEEj_8BquAID2UjQX-0B1BTACmt0Gc54Z5y-ls7OweZ_hRhTgFYosf-8ypkuNHWJR-yzo_Tk9WDgmPHBFGfIDA6fZmEEpczvZImZ6o6GOe9HbxyzfLzWRjRJRqcLY2OOGzMlV1ME-V-gJ-qPRBTKrURq_j_6pHcLjxSwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b321711db4.mp4?token=OdLyg0HwYtC9oRbffM8fcPGu4EId9qE6DovNLNIs7tLQFfaOJ04sJm0Q8rETrYi5JHG4_97X2pSFBz3iRKj_tyssmTYTZHDUYbFWGh_QtgUrMdKME7mg0QN0PHmUjneKB8hxL03Cc1LH3F1awekeprk_b22bM9lZls-66lc2kGknA3KqHOEEj_8BquAID2UjQX-0B1BTACmt0Gc54Z5y-ls7OweZ_hRhTgFYosf-8ypkuNHWJR-yzo_Tk9WDgmPHBFGfIDA6fZmEEpczvZImZ6o6GOe9HbxyzfLzWRjRJRqcLY2OOGzMlV1ME-V-gJ-qPRBTKrURq_j_6pHcLjxSwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇹🇷
این پسر بچه ارومیه ای که چند وقت پیش با ویدیوش که در حال آهنگ خوندن بود توی اینستاگرام به شدت وایرال شد حالا یه کمپانی بزرگ از ترکیه اومده و باهاش قرارداد همکاری بسته؛
فعلا این قرارداد واسه اجرای کنسرت های مختلف تو ترکیه‌ست
رئیس کمپانی میگه که این تازه اول راهه و قراره بزودی تو سراسر جهان کنسرت برگزار کنیم...
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71172" target="_blank">📅 10:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71171">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e529d142.mp4?token=RjilQo2UquTHWJvn74Sil8siBQxvEmVH_ESXgDdXprU8xvnxDbXP_zyWrKJGvweoz8fdfCmr_n1uajbFbM_HivBh15fayV-pdIFrBrR7kxqwQTZLBkaO2b0b3MNg6k3IKuJntdjXpykS2WqRwylTwZx1xXFXu2OgCo_cGNB4qQBVoHHI9edmSL8GDN35h1sP7bP1q_b6Zj2uX2dyXssiiGcpI0ngEDRjtn9Sg6Yurawi_NO-OWo8u641WgNXXhQ-MJ8O-nT8wB9tD2gMlya9P9IDIL2Mqw1grT1PdOYcm669G_sg9bnw_HZB_CEWEcARcgwuc_Oe5n-IaVosdZ_b2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e529d142.mp4?token=RjilQo2UquTHWJvn74Sil8siBQxvEmVH_ESXgDdXprU8xvnxDbXP_zyWrKJGvweoz8fdfCmr_n1uajbFbM_HivBh15fayV-pdIFrBrR7kxqwQTZLBkaO2b0b3MNg6k3IKuJntdjXpykS2WqRwylTwZx1xXFXu2OgCo_cGNB4qQBVoHHI9edmSL8GDN35h1sP7bP1q_b6Zj2uX2dyXssiiGcpI0ngEDRjtn9Sg6Yurawi_NO-OWo8u641WgNXXhQ-MJ8O-nT8wB9tD2gMlya9P9IDIL2Mqw1grT1PdOYcm669G_sg9bnw_HZB_CEWEcARcgwuc_Oe5n-IaVosdZ_b2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
خبرنگار جمهوری اسلامی در لبنان:
اعضای سپاه پاسداران در تپه‌های علی‌الطاهر، به دلیل محاصره اسرائیل، در شرایط عاشورایی قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71171" target="_blank">📅 10:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71170">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a662811c73.mp4?token=WxqRS78o4j008rPwBBxGKlz-5Xa850nT6vPYucqdN0AzQZtnuRBsS5tM3SncAuRsk-LHu4KaXdxeNGte6whKgsEFGmgG951bk0w7v_hRFl97t-GKs3kXrcCDcyiUMYNUigeYB9GnBesVpZhvSriyXj40DcDREtT3_8RYPKALtAn3sOvfPDQeF4hlZgVi8Q5NXALosk51ptoKcLX8nu6FZOeMg7AIwAFUCpqIv4sMXLXYkIEomeUpq_hlYSXezLcMsz28iTrQOelsGZUMIO6ae-KKWDxjdbqVA9JKwdKog6bCVnzGIZ443_QxNNNXTxe0H2TnQoSv92D1JNOQvmpmSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a662811c73.mp4?token=WxqRS78o4j008rPwBBxGKlz-5Xa850nT6vPYucqdN0AzQZtnuRBsS5tM3SncAuRsk-LHu4KaXdxeNGte6whKgsEFGmgG951bk0w7v_hRFl97t-GKs3kXrcCDcyiUMYNUigeYB9GnBesVpZhvSriyXj40DcDREtT3_8RYPKALtAn3sOvfPDQeF4hlZgVi8Q5NXALosk51ptoKcLX8nu6FZOeMg7AIwAFUCpqIv4sMXLXYkIEomeUpq_hlYSXezLcMsz28iTrQOelsGZUMIO6ae-KKWDxjdbqVA9JKwdKog6bCVnzGIZ443_QxNNNXTxe0H2TnQoSv92D1JNOQvmpmSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شاهین نجفی:
هرکسی رضا پهلوی رو مورد انتقادهای عجیب غریب قرار میده و میزنتش یه سرش وصل میشه به جمهوری اسلامی
اینا جوگیر شدن چهارتا شعار دادن و حرف زدن بعد دیدن اینجا خبری از سهم دهی به کسی نیست مسیرشون رو عوض کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71170" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71169">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=GTV5PlGw6-HfHA0m8quAxXs5ZpI7uhU3kNKYijo69kCJhvXLcGK1uS7agwO0S25k_hIQjrKNDB37bfSUqHfannSvmQLwl7CZhhWIS0hdrEY-Rzd47hSImwOo2PTL18PpnNtmME7I1FBJkqbYZorW4lRknZ-igblqWJdNKyMdHwdl1ihRrg5oWZuSAMX6HARnnlcXe0aoWe3r2mK-DZXchnbrK7aGnS9snV3qErksNRsQ1LR4sLjpY5zg9ydPirwzH9cu4jV6grT6jwDL5Vx91h65ZsCiQyQW9sADH3lHFk9VooM2iPD_nN0hL-a_ieNqIERzmQA031FfVcgDlqVTWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=GTV5PlGw6-HfHA0m8quAxXs5ZpI7uhU3kNKYijo69kCJhvXLcGK1uS7agwO0S25k_hIQjrKNDB37bfSUqHfannSvmQLwl7CZhhWIS0hdrEY-Rzd47hSImwOo2PTL18PpnNtmME7I1FBJkqbYZorW4lRknZ-igblqWJdNKyMdHwdl1ihRrg5oWZuSAMX6HARnnlcXe0aoWe3r2mK-DZXchnbrK7aGnS9snV3qErksNRsQ1LR4sLjpY5zg9ydPirwzH9cu4jV6grT6jwDL5Vx91h65ZsCiQyQW9sADH3lHFk9VooM2iPD_nN0hL-a_ieNqIERzmQA031FfVcgDlqVTWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما آمار رسمی کشته شدگان اسرائیل تو سه روز اول جنگ رو منتشر کرد:
۶عدد ژنرال ارشد اسرائیلی
۳۲ نفر مامور موساد و ۷۸ نفر مامور شین بت
یازده دانشمند هسته‌ای
۱۹۸ نفر افسر نیروی هوایی
۴۶۲ سرباز و ۴۲۳ نیروی ذخیره ارتش اسرائیل کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71169" target="_blank">📅 09:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71168">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
سپاه پاسداران انقلاب اسلامی ساعاتی قبل در بیانیه ای مدعی حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی شد و اعلام کرد که پس از این حمله اونا خسارت دیدن، ترسیدن و از منطقه فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71168" target="_blank">📅 08:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71167">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71167" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71167" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71166">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEGFGNpJx1wJqxLX3XEqjfdPrxT94KcK5ege85d5MHGInm8seHJZSAX09fz-7Q1AKZOQFlssG0F5fgW30WfYl7EirJK0zbMiXgL1VY3HCM5u6wyH11vKqncGx_zoP45Rg9uY0WaSK2kN6Z9nR55KxH8sr1IOgtuZQGs0MBx_Tp1r6ncUCpM92bOaOjWikQvu2sbAp2B4fiKu4q-Ux6TwSQq1c_M_epTsDI46FQCigUt3WwGYu05rKfvTn5h9n1C-k0FNkLUPEPCxdL6Vxho5KYu7xInRCHeaHHkgEGBU3aW2zX7_-tqBq7J2lNBN7h4JI1sdCabBVfbaagMH7L26BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/71166" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71165">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/news_hut/71165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/71165" target="_blank">📅 01:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71163">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=bRU0XszKQOu2cJulxBkpaQPAEvO-1MRqwGjk7PhUPzlRXV3_KfujLHuo1w68u5ufSFXR_gDToERfPxIWXdimCKFAVPyRVnfBIf_i9t3XqMAXXBHMDm_RG0qWdtH7tU4C5ZiJRvxtRWbdTZkb9zWwRpwdZKFALAITKQNMakZzwo8U9FqYUfgULNmqdoWtyZUqubsLJlLk3S7o3TeCnBWCxOdKgxaFH9MzQS4SXjL5f81CQ4yXqP_X-LRFtdHxP6WtNmouJUq5XEDA3ugOikb0vZXfC-vqBvd5axzQrD8_g2IshNARUnk7kdHugNKKkwJ-wbz3m7aEKj8v72t8sJTPjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=bRU0XszKQOu2cJulxBkpaQPAEvO-1MRqwGjk7PhUPzlRXV3_KfujLHuo1w68u5ufSFXR_gDToERfPxIWXdimCKFAVPyRVnfBIf_i9t3XqMAXXBHMDm_RG0qWdtH7tU4C5ZiJRvxtRWbdTZkb9zWwRpwdZKFALAITKQNMakZzwo8U9FqYUfgULNmqdoWtyZUqubsLJlLk3S7o3TeCnBWCxOdKgxaFH9MzQS4SXjL5f81CQ4yXqP_X-LRFtdHxP6WtNmouJUq5XEDA3ugOikb0vZXfC-vqBvd5axzQrD8_g2IshNARUnk7kdHugNKKkwJ-wbz3m7aEKj8v72t8sJTPjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاه پاسداران تصاویری از «رصد و رهگیری شناورهای متخلف» در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/71163" target="_blank">📅 00:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71162">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=P-wphfcgTeOR0164NlCeDEWi2VDaGFB3W-3_WV611_7bIfMda8-gBsev-bzocLQ5XgcHsXpGK4baHcDXninx8FZoxoYXGdjtZgaxEuiRSTYe5ZHPeZKF0H6QYh5i7RPZNm54SyEjBiCthUu0akNz3cLg9Vvy-bDWP_I0E4jVRV3G0zb2mhQnjgSEOMPVIr1uDgEAEmBh9GmYdwCWiM7ioW0qmB7gFnh_fju03U9laxDwUxW1IKJu1T9-C0rhnVMwxusdEz5gdkkavXYthskGq_YnhPihHTBLYXocjI2Ndkx0Km3nshrlQFeWNHBTIekRW16ZXb1WsK2UF8JhW2Ubbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=P-wphfcgTeOR0164NlCeDEWi2VDaGFB3W-3_WV611_7bIfMda8-gBsev-bzocLQ5XgcHsXpGK4baHcDXninx8FZoxoYXGdjtZgaxEuiRSTYe5ZHPeZKF0H6QYh5i7RPZNm54SyEjBiCthUu0akNz3cLg9Vvy-bDWP_I0E4jVRV3G0zb2mhQnjgSEOMPVIr1uDgEAEmBh9GmYdwCWiM7ioW0qmB7gFnh_fju03U9laxDwUxW1IKJu1T9-C0rhnVMwxusdEz5gdkkavXYthskGq_YnhPihHTBLYXocjI2Ndkx0Km3nshrlQFeWNHBTIekRW16ZXb1WsK2UF8JhW2Ubbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
یک فروند جنگنده F-4 فانتوم نیروی هوایی یونان در جریان رویداد «هفته پرواز آتن» در پایگاه هوایی تاناگرا سقوط کرد و دو خلبان این جنگنده کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71162" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71161">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=bJtchC4P5tSitmSnsZBk4889ZZoXHWE6HG_RqQpLFQ1Afeu4dqo494TcI7UoWHyV54Johh5i9xVREiok-9I3PSeIna5QTMbPEtgDc22RhATGqDsBWjSNihH8gvQHuUM61JYNpmA5P67z_yENQDHFaZyAsxVur7hAzyCLWzRtT2BKaq1qU-vmeMSN94yyn9lrWPHX5BPvTATr_uj_EPoLHTicdISdwbPdlAURujxwIdnVxlnWResD1u2zAt8nyuwBqETcDkxliUPhQ1uW3LyQ9bKY0-5ZmzF-i2kfajPNN7NlBW9gqGqKJCssQL1XDiSbsidMOl_9D7sLQxqeEln0_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=bJtchC4P5tSitmSnsZBk4889ZZoXHWE6HG_RqQpLFQ1Afeu4dqo494TcI7UoWHyV54Johh5i9xVREiok-9I3PSeIna5QTMbPEtgDc22RhATGqDsBWjSNihH8gvQHuUM61JYNpmA5P67z_yENQDHFaZyAsxVur7hAzyCLWzRtT2BKaq1qU-vmeMSN94yyn9lrWPHX5BPvTATr_uj_EPoLHTicdISdwbPdlAURujxwIdnVxlnWResD1u2zAt8nyuwBqETcDkxliUPhQ1uW3LyQ9bKY0-5ZmzF-i2kfajPNN7NlBW9gqGqKJCssQL1XDiSbsidMOl_9D7sLQxqeEln0_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه خانم درباره اقتصاد:
چرا مردم هر چی گرون میشه از زاویه ی آدمای متوسط بهش نگاه می‌کنن؟
خونه از ۵ میلیارد شده ۵۰ میلیارد.
گوشت از ۵۰۰ تومن شده ۴ میلیون.
سود شما چند برابر شده.
مردم از گرونیا دارن سود میکنن، مردم باید دیدگاهشون از آدمای متوسط جامعه تغییر بدن و بگن هر چی گرون میشه خب ما هم سودمونو داریم میبریم
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/71161" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71160">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=qYTa0ZRjYHGw2VaWpyqXaDW1rmlUtAYt_cMHDuUw_KpKBb2VKXh0ePMm-_J5hUS-EdWPKc-b0AMJWeeNiDRUU8bcQ8-dVamAn1RpEgYk8qZzCgmEBcykcSR6jxwNFzzMShWFvmANteyNJUibpKZmXw4DRtba-rF6UNrw3ER50XtPhUHknx5WVIRVV-G2Vt5p5x9y2FVXDJVxw3WNS0zyOkzd6VMD2fHXHCTT0qO9U-qoXZhS3Tr1Z3DgaG2X_IwG5I5kr9uHFWl7PiVfXcPhC60lbIcutBpfU2zcrOWkeIEnz5HPQCP3yySTDoCMiCygEBu-Vu5yS8c3QLA0eHRU6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=qYTa0ZRjYHGw2VaWpyqXaDW1rmlUtAYt_cMHDuUw_KpKBb2VKXh0ePMm-_J5hUS-EdWPKc-b0AMJWeeNiDRUU8bcQ8-dVamAn1RpEgYk8qZzCgmEBcykcSR6jxwNFzzMShWFvmANteyNJUibpKZmXw4DRtba-rF6UNrw3ER50XtPhUHknx5WVIRVV-G2Vt5p5x9y2FVXDJVxw3WNS0zyOkzd6VMD2fHXHCTT0qO9U-qoXZhS3Tr1Z3DgaG2X_IwG5I5kr9uHFWl7PiVfXcPhC60lbIcutBpfU2zcrOWkeIEnz5HPQCP3yySTDoCMiCygEBu-Vu5yS8c3QLA0eHRU6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جانفدای رندوم و حرکات جالبش
😃
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/71160" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71159">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=u-e9TutaLa1s9CggHSs6NQjix8CG_-BPLm7_Pe6Sd5wM9Mkuziibc1k1KWRRBvactIYHINfcb3jJYcReWSMnlkqOHK0SKqSnP3xPASCbcYnhqu9VA03GFSVzbgdd3s3GeTq5bsa0FFTSbqh4R9A1_XpQ8NpBHVZzug3JNRFnx-8Da7xTFxvAzWZE-sHJyoDH0q7uu4Vy3iL4ghB_Z33tP2IFQupl_DWCNFqYSQQfs43lIx6XsE2J3Sqw9Y-eHiI81EPw7MfUm5yiw1xhvS_AgXQB0ONiaR4BU0eCLUIdGbF-7U9vPsGiICpxXp9PqJWBmXJ_nemqNC6-E2U2ciBk-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=u-e9TutaLa1s9CggHSs6NQjix8CG_-BPLm7_Pe6Sd5wM9Mkuziibc1k1KWRRBvactIYHINfcb3jJYcReWSMnlkqOHK0SKqSnP3xPASCbcYnhqu9VA03GFSVzbgdd3s3GeTq5bsa0FFTSbqh4R9A1_XpQ8NpBHVZzug3JNRFnx-8Da7xTFxvAzWZE-sHJyoDH0q7uu4Vy3iL4ghB_Z33tP2IFQupl_DWCNFqYSQQfs43lIx6XsE2J3Sqw9Y-eHiI81EPw7MfUm5yiw1xhvS_AgXQB0ONiaR4BU0eCLUIdGbF-7U9vPsGiICpxXp9PqJWBmXJ_nemqNC6-E2U2ciBk-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7  جونشون رو از دست دادن...
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71159" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71158">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=L9jVFTl7oQm7glOaTvBDFvEj2K5qDUwVGf84K7Gq1BDNvQtmpLqSfX0FBCWN8_M4_JWIQmKBMP_xei7jjrTzg5Hou-_qq8DNXXjGz5UKbHqa_RzulfxzeK6Z7P-mvunl9se-4Ck3S7ANecv7z5XCytamhTZYv8JQOl0LpFGxyFmEaDRmJhjazFBKZArz7XUk95mzbix9W82GBaplom-YDLttobHW-nzreHRKultlF093rVO5-QzABtdxy9QwOI_AWtyJTRpkuTl1hdoo82JkNHfyBo0IEM8YQlkL5yLpiAQWK83yyHw33_O_9mSVcJ-dCIRpi-9Tm05h5xQnPsPx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=L9jVFTl7oQm7glOaTvBDFvEj2K5qDUwVGf84K7Gq1BDNvQtmpLqSfX0FBCWN8_M4_JWIQmKBMP_xei7jjrTzg5Hou-_qq8DNXXjGz5UKbHqa_RzulfxzeK6Z7P-mvunl9se-4Ck3S7ANecv7z5XCytamhTZYv8JQOl0LpFGxyFmEaDRmJhjazFBKZArz7XUk95mzbix9W82GBaplom-YDLttobHW-nzreHRKultlF093rVO5-QzABtdxy9QwOI_AWtyJTRpkuTl1hdoo82JkNHfyBo0IEM8YQlkL5yLpiAQWK83yyHw33_O_9mSVcJ-dCIRpi-9Tm05h5xQnPsPx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر نیرو:
دیگر قطعی برق برنامه‌ریزی‌شده نداریم
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71158" target="_blank">📅 21:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71157">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=bwauOkyrX8ZigVruuOpbvVcjpK7KPkWsnxlIbubU-frBwQjucaTAx30ZTT09mdGStFPbZCME9NveuIfBUGCYxIRhaGsU0ZMwYjwbtY1Aw3Oaql-9pSfOh9y2VwEa1-UvH-JOPNwFxLZQw7jdJ39pW1tdShjDzm9huTWWjajx_4sy-t7HSXsehI2lKxOLGIcEdMA0QNwENSJqYYT2NVbBuWi6yoPPVZX5yHVJb7SQshxwyqqGhWQNABNQollG36M72TdMNdmLEknvxXd1ttvAVjjqci-1S3Uq6qX4jzvHHF1XueiWSSBBy78lLB3eMFJNuQnLesQu53qbJUtEwfhY_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=bwauOkyrX8ZigVruuOpbvVcjpK7KPkWsnxlIbubU-frBwQjucaTAx30ZTT09mdGStFPbZCME9NveuIfBUGCYxIRhaGsU0ZMwYjwbtY1Aw3Oaql-9pSfOh9y2VwEa1-UvH-JOPNwFxLZQw7jdJ39pW1tdShjDzm9huTWWjajx_4sy-t7HSXsehI2lKxOLGIcEdMA0QNwENSJqYYT2NVbBuWi6yoPPVZX5yHVJb7SQshxwyqqGhWQNABNQollG36M72TdMNdmLEknvxXd1ttvAVjjqci-1S3Uq6qX4jzvHHF1XueiWSSBBy78lLB3eMFJNuQnLesQu53qbJUtEwfhY_Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
جان بولتون دیپلمات آمریکایی درباره ایران:
من معتقدم — و دهه‌هاست که چنین نظری دارم — که تنها راه دستیابی به صلح و امنیت واقعی و پایدار در خاورمیانه، خلاص شدن از شر رژیم تهران است.
به گمانم حملات آمریکا و اسرائیل آسیب قابل‌توجهی به این رژیم وارد کرد.
بی‌شک ما اشتباهات زیادی مرتکب شدیم.
اما اگر اراده کنیم که درباره چگونگی انجام آن به‌درستی بیندیشیم، این هدف همچنان قابل‌تحقق است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71157" target="_blank">📅 21:19 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
