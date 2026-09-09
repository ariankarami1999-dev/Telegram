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
<img src="https://cdn4.telesco.pe/file/v86Oc6utbMeeY0UQf6ZixNb1XZ5qEeJoSvUnyi_2q889zebKEI5GeWFesJ5Tn0PNL1Zu8wMPsqOsCbj4Q5zHcPRE9JN7igugiS6-GgPzE9-dqnIKbXU-7wUHoGol2WjLWabd0uys01_5AyyhV_4MVNjv4xoBYWLujSJooPlb3z2uvHrJlLeSIoR_IeidmoBTYgNFTeaedtQLnptNy5Qya12DCn6U06EJ8fivA5g9WZC3YArLl0IX7O6bbsIyu9x59X5OyciGB4CmgiVgcvvAbjZ0pVlqxMzBEP4HbU8FfJ3VppybWlrNjAUIQbQ4jYXxCLiqyefi1Ffcsh1Xe5KbRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 02:55:58</div>
<hr>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YiP3scPygf7TtU9kkNSQkddHBf1yDJYvsBCv0hQGxNsEGNGUuuJF685kUBOzbWBISeBbQamnWaJHrtzN4IZUNFyeZNkb0LE5K2Xcs4b_tdq0ycQbPs2Mu6_B918eQoeaWu3n_l6uwYL1JrQdivGT90AzOir71qES1VMe3dNKmYHH4asiPxJm87KDRsPCG_89hZdgh8BHilOOeuf1JJYIgD3gAtdmd9piBXKa4CNgXBPzDAoiItMzkglo7fWAZnHzICQLxhj-yvz_yOJWGz9zBd3lhCZF39U1TImM3M17FTzLt9VtvRB2RGpX9koEISGd0t29RqjNYoa4tQxQ0Io4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3GLnIoprc-PEsnPW8108z5-34U6TYToSnRAhgEed-nHb68QgGdGaFELLcaaXirR7cS78WxmJgEiKooxSAD9r2mU_v0oi25FHBjW9C4x4YKv4z4QZiv-I45qZSS7KbHHQFDRYCzIPzzgrMQe5PAOqxocq9gtFLYMS_jJ0McAH-gV1qqp4IT9xdQE5Kt9NTFTtDfaGD_Nbcm8BcA8cC_jpOJmLIX5QV2jK80tmHYT-HA0btxR2mg1uyoRraqMM9PiaZQKt53mga5LHfMVC6SffVu4q69g5chp1qJyvcqAjpXkiYM9WEaJb8hKW9uLQ0-lFJkBfrWtYy5mW6kL5_WThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X61ZyTFZj0tHRTiFRoaiW7SDYNLofDncnxZmEanK5mrpZVQaIrIAq7_3xLEN9Q-9JVWHlq7fmHKW0BEfb3xmHJQBpgRFRCcWjCM7ODkXZXgaTL7lvmlsRjoWI44kceWdhQAZUc-ndtXaubfLR2m6FXaGyIvYZ-2OyUDMU6Zkj8vYK-fPTokE8aTolHIjnk-6mZE3EiARA5yvDyVQ-3f2sLnUAQ-7Q2vIIbEYENQGIBaaIPlQ5xOuvlR4n81loJTWpoFj9P_P-HKTN08FN9BRZ64UtD6dSEejw0xrzqRl73tDXgSoTwqJI23Zzgduh1TnXxF7arGLCKoSyJUWRAauKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=mncAUwasxpijFZP2k1NL2iK-_RL5EiJuO6NWNrtlgqr3G9cFGX6uIFA2AT5FNnaTQzFu1hF-pMtj3jrXaYvK4jO6b2H5czBjzg5qKxT56QpWyhkUYicQGc5SqoOxe3689FAzXSBTrn3ggXgI00G0HIXHT0yJJ-sKa7ejdG1kWPpONjFEdbztRwtSWvN4CmhDYMkBNtRBvo3v9rwcv3kwtyIDmyW1uXqBJmWT8nEoOR0-TbFzDGGFlykEvmWMeA-p1nK9dAwWounPXGJNM_qG0hpyB-ZgNmNGj4Gpx49Xk9noxu0jmJNadqmE2d2JIzpxA-ecduXffD1LhQgwNItpIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=mncAUwasxpijFZP2k1NL2iK-_RL5EiJuO6NWNrtlgqr3G9cFGX6uIFA2AT5FNnaTQzFu1hF-pMtj3jrXaYvK4jO6b2H5czBjzg5qKxT56QpWyhkUYicQGc5SqoOxe3689FAzXSBTrn3ggXgI00G0HIXHT0yJJ-sKa7ejdG1kWPpONjFEdbztRwtSWvN4CmhDYMkBNtRBvo3v9rwcv3kwtyIDmyW1uXqBJmWT8nEoOR0-TbFzDGGFlykEvmWMeA-p1nK9dAwWounPXGJNM_qG0hpyB-ZgNmNGj4Gpx49Xk9noxu0jmJNadqmE2d2JIzpxA-ecduXffD1LhQgwNItpIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=NZCbj1jercCy7eNirCDNVjryrESWXS2ARQIz0C02V-xCzY50ljmC8rtjmrBp8z9ABUUZyVXoGVXCy01EsNuiYe7Sdn18CqwBID7lZwr4Jj9rYZHC_el8lwGK_v1MkHkbYfNbv-qJBjz61DQ-1gwjQh-broksJQGTOpFVMkH2aE9IRguD1hpfMJNM0dSsZQZkWF1LKpRQkPnXE7DwU-fvM-xLA1ze8sLvmc0goKaacxarNzxpTAQiINPArskGjeDcyQhU7HazB49QfmPo2el9rpPbSam_w9AsbqOQCpFV8BzR1zLrfLbF1wta25Pa5C7GR4Fx1wZNSqDCO8iHx0k7-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=NZCbj1jercCy7eNirCDNVjryrESWXS2ARQIz0C02V-xCzY50ljmC8rtjmrBp8z9ABUUZyVXoGVXCy01EsNuiYe7Sdn18CqwBID7lZwr4Jj9rYZHC_el8lwGK_v1MkHkbYfNbv-qJBjz61DQ-1gwjQh-broksJQGTOpFVMkH2aE9IRguD1hpfMJNM0dSsZQZkWF1LKpRQkPnXE7DwU-fvM-xLA1ze8sLvmc0goKaacxarNzxpTAQiINPArskGjeDcyQhU7HazB49QfmPo2el9rpPbSam_w9AsbqOQCpFV8BzR1zLrfLbF1wta25Pa5C7GR4Fx1wZNSqDCO8iHx0k7-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
پرزیدنت ترامپ:
انجام کاری بسیار فراتر از توافق هسته‌ای.
چیزهای بسیار بیشتری از هسته‌ای وجود دارد.
ما به توافق هسته‌ای خواهیم رسید، این ۹۹.۹ است، اما چیزهای بسیار دیگری روی میز خواهد بود که سه ماه پیش روی میز نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ6FHYFn7bhLUUj43QjrUvzxkCB6igxZFz6-VhMihqSLYs3tfF4FJwTa0UpLnO4hqdTg6TPVhrSbNFbSWO-qG2xrEVG-pyXt7DpKHcb1Fb4DkSBT2nPfy4T7jq1pd1RB2IXV_Y2V_VfPVSxqUv1ZKTrJ9QfXVfovrdupf3z-Ovrawxf8zf5tlaVfZpdLOBOKrG3WldBDUWmd3oRUSh9vqwoiWnbGq87LmPQFdntnGn3hzqsIeYlZCxJLaqH0ANUGIgQU01zwZqJgJu6G6ESqolwyHVf5z_TkIGT16kZRg9YNgkUFTUNCOxb0qDJ7b8T1r3_TlRjJm9KV64sMKGk36zeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=TdbaI533OtqtZ84qRBSYHNyIeVbKmZR1fM-MGeYofKr2UdShWdCWAb-mJvgXBydC-Bt9lWncUCp0eN0VrD3OXzesKeQ_V5DBdvYNZP_7l348CEMXWe20Tpi_cP7ve60EiadWdzZERe7mQ-SusXvaDd-nM4J7Ewg_3NeWAQxMdxh-WHiO-rEHhVrvAETeKex2SwC9b-ts4oKGWo0ZYjeaQ9vBVhYRmN5EZ8KbSt1EelH4uaSRQ73UvydPbg1QvDJo_nfADJjF_JWyA79BKJZFfXaID7sKxTe6uQaonf46_ObGQraBBBp2Y-D20962gsSvdQ_X4jm0wNKZiiy9LjwUJ6FHYFn7bhLUUj43QjrUvzxkCB6igxZFz6-VhMihqSLYs3tfF4FJwTa0UpLnO4hqdTg6TPVhrSbNFbSWO-qG2xrEVG-pyXt7DpKHcb1Fb4DkSBT2nPfy4T7jq1pd1RB2IXV_Y2V_VfPVSxqUv1ZKTrJ9QfXVfovrdupf3z-Ovrawxf8zf5tlaVfZpdLOBOKrG3WldBDUWmd3oRUSh9vqwoiWnbGq87LmPQFdntnGn3hzqsIeYlZCxJLaqH0ANUGIgQU01zwZqJgJu6G6ESqolwyHVf5z_TkIGT16kZRg9YNgkUFTUNCOxb0qDJ7b8T1r3_TlRjJm9KV64sMKGk36zeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
در مورد ایران؛ آیا انتظار دارید که [چنین روندی/مذاکره] زمانی آغاز شود؟
🇺🇸
ترامپ:
راستش را بخواهید، جف، ما به دنبال چنین چیزی نیستیم.
در ابتدا می‌خواستم به توافقی برسم، اما اکنون کار از آن مرحله خیلی گذشته است.
در حال حاضر چیز زیادی از کشورشان باقی نمانده، بنابراین ما به دنبال آن نیستیم.
بله، شاید مذاکره‌ای صورت بگیرد، اما این چیزی نیست که ما در پی آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما پایان خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtkHESg6lEmmg5Zmdt7Bs71EEsBoYb_zUPlfGHafNze8pDvdZGR5VHlmpO0_G1IPJKkbjy3ilxoP0C0DPQpECLQ5GDYZCJ3RqM1skWnxvWa0mHrAjyYUzU6Qw6at2cAoHd3u7_Tcu6hqBSTtf0CCosv62RDWIe6KriYkSicdgW9DjITU3h7v-5ETqWweSCaRu1Di8jx8Bwy3fcms_fh5TnompUbEVZHhsxw1JZk7MlVZ78mDqWT0CkCsiRqUgA1LUS3adx2mOSUYWGBYcWvC1lqlIzGTRVO0GFK9ERRdDdjUfV9jwMFdrnrJoZAhon9pzaOMxyffOW7Wq26OLeD1POlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtkHESg6lEmmg5Zmdt7Bs71EEsBoYb_zUPlfGHafNze8pDvdZGR5VHlmpO0_G1IPJKkbjy3ilxoP0C0DPQpECLQ5GDYZCJ3RqM1skWnxvWa0mHrAjyYUzU6Qw6at2cAoHd3u7_Tcu6hqBSTtf0CCosv62RDWIe6KriYkSicdgW9DjITU3h7v-5ETqWweSCaRu1Di8jx8Bwy3fcms_fh5TnompUbEVZHhsxw1JZk7MlVZ78mDqWT0CkCsiRqUgA1LUS3adx2mOSUYWGBYcWvC1lqlIzGTRVO0GFK9ERRdDdjUfV9jwMFdrnrJoZAhon9pzaOMxyffOW7Wq26OLeD1POlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owkasB1Lyo07PASVBFJOlmFXWKe3z9haj__PtuwdaKZBtXomIHr4LlnJVA5ZaJFUa9VmEHVH_OnwHz6YzTu_TsirqpVpjjoEaf4FNxkjAOolpgBj-m-QIpKse0SeeaUNvzLlAo4P_0_O9TS68TuPAzXaszez5ecF1jN9fpVQlLRPcs36O6vUh38jAKSd0yhPXYFWTz3eXEZ0HXyDxgDQ53YTEBUHlVMNpGDEXOQzZAfX15EY079OH79x0wG2iDbZcd8XP8QoMnZsZGz70aWzWlEV5H4mdcv-KWGjdTPxsjXGQikyqqbLXHIclv6IbGoWXgA7XMMRm6LgpmU_reB44IdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام می‌شود.
دلیلش چیست؟
چون دیگر نمی‌توانند دوام بیاورند.
آن‌ها به‌شدت تلاش می‌کنند بر انتخابات تأثیر بگذارند تا گروهی ضعیف و مطلوبِ خودشان سر کار بیاید؛ کسانی که کاری به کارشان نداشته باشند و بگذارند به سلاح هسته‌ای‌شان برسند
تمام خواسته‌ی آن‌ها سلاح هسته‌ای است، و اگر به آن دست یابند، کل دنیا دچار دردسری بزرگ خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=i5UAizQFPg6V6KN7djTZ9BQrpMUIxCyACEaAwp28EdmTrdLzhtMbNxlnZo_y1HvWM-10C8PJ-BLQITHjL315GmXxIdJpGKq3i3yQuKaQSOIwkXt71Hso4Ea5Ax0QfTsEMXiXkviQS5JsnZs4MjQdM8fVASwQyK2lXHmYxC2G8K1Vq-dTyVnH8W33dfeXROfE2KJIowu1CCirAhEWE5ovXAO89uLBXp5vaD6zzL3KkJ7H7tEhzm8KQXRfj6XD62uO3cMBJNjY2r5kNgGw-I2ftjGB7teFLkuNkoAIzm7uq8-MivRX1p4sQq7IsODb6Mq1AKfeFfyHMZ6cjj-uSOOElg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=i5UAizQFPg6V6KN7djTZ9BQrpMUIxCyACEaAwp28EdmTrdLzhtMbNxlnZo_y1HvWM-10C8PJ-BLQITHjL315GmXxIdJpGKq3i3yQuKaQSOIwkXt71Hso4Ea5Ax0QfTsEMXiXkviQS5JsnZs4MjQdM8fVASwQyK2lXHmYxC2G8K1Vq-dTyVnH8W33dfeXROfE2KJIowu1CCirAhEWE5ovXAO89uLBXp5vaD6zzL3KkJ7H7tEhzm8KQXRfj6XD62uO3cMBJNjY2r5kNgGw-I2ftjGB7teFLkuNkoAIzm7uq8-MivRX1p4sQq7IsODb6Mq1AKfeFfyHMZ6cjj-uSOOElg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=BYj5ZDcfcslyuQXV_tY2NHd7ME7UMGefEPksdh_MjCJWgf5UYJb75I7zQp9nKHUXS74xIADWhSz0229SQBeNCpSxXgg_GRHsTfildTm9o7MQ7_AfnwU3d-VydE_Cz6zI5z5Df0vcioIG3oIuKyqcZjXbritf215UNwIqprszhggvdbXaBoy2Zg-TwIiFfY5n926DrWVNClhOVq8QPwkUC0NFT6Dm3ifX8u4BvOrWdkoYnBbiBH2TFZu1WparJD881Q9OkCs93W9hJGcjJ_HUjS0Y09KLcnkhU4c157SbQokapbykpEeAn6eX5IxxN_US9NuxEUlqZ9qWyzFiXQYL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=BYj5ZDcfcslyuQXV_tY2NHd7ME7UMGefEPksdh_MjCJWgf5UYJb75I7zQp9nKHUXS74xIADWhSz0229SQBeNCpSxXgg_GRHsTfildTm9o7MQ7_AfnwU3d-VydE_Cz6zI5z5Df0vcioIG3oIuKyqcZjXbritf215UNwIqprszhggvdbXaBoy2Zg-TwIiFfY5n926DrWVNClhOVq8QPwkUC0NFT6Dm3ifX8u4BvOrWdkoYnBbiBH2TFZu1WparJD881Q9OkCs93W9hJGcjJ_HUjS0Y09KLcnkhU4c157SbQokapbykpEeAn6eX5IxxN_US9NuxEUlqZ9qWyzFiXQYL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGBjchYjTo1VsigFjIPPFjAZAndno88yVrHfL9EinoHefCoWAUEfAfGrzpZzZuefo-f7GiQcdsAkxqlFsPkiQRv6pL9qWflMkuIhuNOx7ENoVqxeB-rDfQAcAl28iCKtk7vMGbygr8ccbFFMNXfAIJVtvI5_dHhsNjHWQuwGJ3_5UnWhhoBHsw0WH1NjrsW5dgcQ6r0zxUUUVR78Ty0m-S6hC33MvQRej0_eXbdH8Ef7nDGJsuj4ATA35Wl8HqsoUbiLTROR_7Y3sho-Z1gw0D-Fo2UwtHyooqRTRvJuOmYP8TnqH_WFDTYuKXF5Ki38u-7m7VwikZfG_vianrHj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=c--xFjwwPjfI7-nKX6w09apkVJ3R-tf5EJpbNfJdk2IlpieoZxnIlez5hG5ulUkr9VpnuI9Cdt2VmEzFkGdASSdMskkrb7xkxOnB1_L125P9EabAx6Oe0aY4vlFUZd95i_lC3Gb1bP5CTduco4VAz0JqjU5lOKrinQZdprWZCk4_nfx4jXAhpJ9Q507Xx3EwCTGud4hLUeJDUERrurSpPucwdltL-ssigFVs8UnTPODsEKFsdwqVrHgU1g6wMU-t4BAcpCnJaI0g4NVnk0zO7UVd8--aQR8-Mtc1T-XpQZH7PgE06eb46TtBTWnOoynJGvqiYRihkxYkwghHZur9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=c--xFjwwPjfI7-nKX6w09apkVJ3R-tf5EJpbNfJdk2IlpieoZxnIlez5hG5ulUkr9VpnuI9Cdt2VmEzFkGdASSdMskkrb7xkxOnB1_L125P9EabAx6Oe0aY4vlFUZd95i_lC3Gb1bP5CTduco4VAz0JqjU5lOKrinQZdprWZCk4_nfx4jXAhpJ9Q507Xx3EwCTGud4hLUeJDUERrurSpPucwdltL-ssigFVs8UnTPODsEKFsdwqVrHgU1g6wMU-t4BAcpCnJaI0g4NVnk0zO7UVd8--aQR8-Mtc1T-XpQZH7PgE06eb46TtBTWnOoynJGvqiYRihkxYkwghHZur9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNOiIN7V-TVXvn0P-7r_pAQ_g4R1viyxVnoX3Z7c-zA0_RLjhJ5DgLzyPpAflCN4BpQGcotdMoh5Bw7H40w6YCf3JsXu5e5C_IkGW47A7A1Z0w4iJGXnYzH_AOkwWQE8cNk78D01dLSPoyxz0BqVlZUrlzfXSvQcTwKUJibH6lBQE4P_NQHozAiwhPdRGzQrBvBFXz-yEfmrSXA_HmRWgkFV3bk2Z2KtOzXqOhKupwuvlICCp0C1F_JdfNFo0DLDo_lY1DBRrFKVJU60KoGc1OKYjtMyieRh9HHAisSw0NEssvmOlCK93HsXqwR5Y1imZ-wqiW49TMouvVy7_sp6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=A8aVUNQCSIB7c9l5MXtXcf2JTvPF2HYGbgBJrYQK6xYSWi-1tlHrxBzuUQmsfpXVXHgnIwhikAUguxFwkWvuNhxLXw9yAQnab6iZjJmEfeK85mDZQG-k-FSvLRISOxvTr8TMNJoBcSi49L6k4gvfzM_sjcMHeQrJPEZ9DyvCz_iGKOhU3B2cHcGDyKiWufMtbgQxYq_h1PPDpzxuAntanECiyiThtNx4zeOhED1snx6JezhhwyMRKEP6Hone4rrmEKcTi8t2DzKxpcFnZNNoIQJmZZ3WAa4LW6fGjhhPLa0Soe1gAmrRrhwfFwCPgN-f4dk3xqWHdaQhC-FTfikuBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=A8aVUNQCSIB7c9l5MXtXcf2JTvPF2HYGbgBJrYQK6xYSWi-1tlHrxBzuUQmsfpXVXHgnIwhikAUguxFwkWvuNhxLXw9yAQnab6iZjJmEfeK85mDZQG-k-FSvLRISOxvTr8TMNJoBcSi49L6k4gvfzM_sjcMHeQrJPEZ9DyvCz_iGKOhU3B2cHcGDyKiWufMtbgQxYq_h1PPDpzxuAntanECiyiThtNx4zeOhED1snx6JezhhwyMRKEP6Hone4rrmEKcTi8t2DzKxpcFnZNNoIQJmZZ3WAa4LW6fGjhhPLa0Soe1gAmrRrhwfFwCPgN-f4dk3xqWHdaQhC-FTfikuBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCrMBgiod3AAtxGHnbsryD4SYpptlUHSFRa-V4eusO2gWJ5zmVQkXtKk598FWyhcjiKI8xeuJYQXCN74ixaiUqzTG4vapo1m24_HDaLh3wY802KwzJppVwBZvhy3RYZSjRjDqJ4mIFLz2wtb828r5AsantxirbwjN_ZEua6FxsLRr0nXjSdfH_HUNAbvusccorzWJMM7kb4daWcd55XPvOa-GKIIxMEQVE8bXRx1Dg1y_Bf7s_rXWXEGHoI_m_dkxg51qyNqkxsDxT81JjOMX_2yW01Rxpksj4yxxY6jnLaNRsLVif4_VqZKHK1b2MpAUEyD_hGONBO5vBViXNFnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as6w2wIf2m3RlcQvoIHR7VI0mNPz1-liWmG17TY5haVDDzppgN6MbuOU9Hv5XgIRMJ0O1Lcjv7W5xMcK69mYKPqXjPFLosBFHr-CshWtBhbpI6phNuNfTc9y8ImmnSiP38LSi35z3-87uTdclg5Fae-_4ocuZ6fgWjooMSpmS65vCy7q1VXHcXMNczsuDb3Y0CgBusRiRJ-32t8_RVVGQKVoSRc0-AAkaU8vQ1YurkK0Or9rjsvqZkxZarCQwlq6cqw3Lj3P2savsbQPClY1BfE4iZip5b8l7NYp02Tl7FE2OmIzOxTcjtxcM5s85pE_ATTh-CETE7M1GjSiD-hohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
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
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBtC34mpGmiSxrADZdiCRA7mlUCVprzJhM0v5MdCyhQJR077Y67jlCo2TiC1zj9UaFIHKSYm_XAKc6C5mXHytuw3sxtEQDgaAxPyJXsepDi52XveqQQilP6EI0sfC6KW-UC8hbBqftH0COTD5gNdPQNs9rvcABZ-CKW_eC8pouCrUh6EeKctjjPVkCXARaHr3AUSVm-GdcFD7RldCwQimjLvjO9kvclVmLKViZYglQ_aehhEIX7rXP8146mmZkVS5ihnBi97J5dOZWYgo-QRRJD_PngKwCaBpWIf7tHA7kmu_wLnbl9BpD9N5vWfbymnuFoW6MqeaUfVg69_Dfcn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=KcWKoQoWr4ew_7unSKXl7y1Sv-nXp5wVfXM6hvaSadjglhFT10oQjdUk3NoT7qFFpR8hXxB9eCj-rT3gWld8nA7jPeJ8A0C5RBPN6iEgs6AvNge4Z0_GBYCnILhS0z7gWesLUIg2en-Tw42tVYHXL6xuZbHrcDT0OmUMiZ5NbkQkc96lUnW81EJTfeZ2Nr9NKghuDntk2sNsAhvHLhlMg27Bm_fKtxKwqOs0im7F-P35LWV9XiK5lDD1uqpf4PqQXP9D0dmDYKIQdP_9M6LwwXFFxO3fe80HBdP836-QxJSP0DJWgHP0bXHkZ5pyO1soEaWkpgARwPzjozsmPDJAMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=KcWKoQoWr4ew_7unSKXl7y1Sv-nXp5wVfXM6hvaSadjglhFT10oQjdUk3NoT7qFFpR8hXxB9eCj-rT3gWld8nA7jPeJ8A0C5RBPN6iEgs6AvNge4Z0_GBYCnILhS0z7gWesLUIg2en-Tw42tVYHXL6xuZbHrcDT0OmUMiZ5NbkQkc96lUnW81EJTfeZ2Nr9NKghuDntk2sNsAhvHLhlMg27Bm_fKtxKwqOs0im7F-P35LWV9XiK5lDD1uqpf4PqQXP9D0dmDYKIQdP_9M6LwwXFFxO3fe80HBdP836-QxJSP0DJWgHP0bXHkZ5pyO1soEaWkpgARwPzjozsmPDJAMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkMRUfCZ0NjpH3ZHmpJcesmPf4lzqkGaGmB_kUMuzYBXT8NvmmPccQJl91Rj2JzAca89OoCvWhTcRtfLL6TyIVDrhjGZUZtvBDOiS1HdXc3lKPWBDuBJFIX-fEg7uFGhe4x2s8-OJ9Tn94aXyxgI3txEpwtVJ6I0hTCAO0YMmTPWlkKE34CUEuDGyPr7aM2gK4e9lHx-5S9sOaYqkTrTWR434YwSULc2mMBHGfGnH9kX5qoMLHOKGVGbLJnlcLzrPPMt_P3RCAoktrId7amkiTFKBXBxb5L_xCqQG0Kjjk9tEMS5nAckcdYySoZzsAFunOZVf8UlEaOo5uHUmKjbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcr65FOwbCxhzQVRrAcmP_0IOd8HTk5KfWwe7ohcHFZDiBib5ehqzNlhSqZCgc25jgex4iFVuIvgZlLonv_nNSqrSElD38AwCESofdqZE0n_pwTmPZJrWS3so3Y0Gv9e01BpQrdHwrSpv_lhCSEsZCvwjHet9KDHWbMwtt828YyJcMlA7hb3G6KUkUEfVcYng9UmY-YPuP4T6G8IY_B2yQk4tS0IimHESO6iRknIFzmIWtZrBu2xO6bhxIvOsDCuUGmP8xv9oBhTLv2lqHgM5u26MLPhjUPBPHy-DP2EZSD4QcSfJg78wdZ0LIMqL4TVtHEvd9j9nExWsUUlAKyUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSdfg8Qu9dSXOwWqX3AVZfo3crxjIvhn8afjoW_l7uHJuBn4daj1c82xef_d7D8YVjew5v5qnAAfMliK4Rqez9LD--slCQKajxMtruSbffem_sIPIdQv8VsDdJNw-uywpR2vStjuoXPZHugmNLEYv60MtwKsUmzNQooi1PenjrPXiNoVZ6pcvonQ71b2cJDiKFDvJaB3EoPaTqxosshXUtbBp1CnQ1LOKeAs1ddB_HjZbDd8BpH4WgBSgxglmMatDkqZuTChs70BU9Bb_X8LLRFPKuBZTCLrYyTDwJwQ0FbhjXqLJMzhxlOSeOMTr2G8pZ7YSQCqtFCz2WDqjv3oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7Lh59d7Su-5iqq_Feit-_dCQvSkzY7IT02pGP10ww20yzjefM6qb68RP3yHh9B4cISbb7rGNpBJnWU7j2s2c4jkPD_bIMyOeIdbWCtit9xjVOgU8yoTNnMCcbNMYUrQI1fSHXIClPm8WD5MxFW-lT-0ilRfSuy6xW4l_M_DWVkltxeeOwGYiwe5vmmGZelJdGfi-VhDWzp6i9HjFwK1LxWwZCGqYyA1aVEYL_Gywl8Vj3BOi-S2RUcTHRg0uSaF34_xk4b4p2Ae1ylr62izOMtGE-z0AU28_3PYOV9V3gHQoJVMakclsub-S0Bn0nD7UYH4s4nwVE-eqB2xU4s6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
پرسنل نظامی جمهوری اسلامی:
رفتم یه شونه تخم‌مرغ رو گرفتم با یک کیلو میوه شده یه میلیون تومن. حالا نمی‌دونم بیست‌وشش و خورده‌ای هم دریافتیمه.
مثلاً بیست هفت هشت تومن سر ماه به ماه میدن به ما. مردم چکار کنن؟ خب دیگه یارو میاد بیرون حق داره اعتراض کنه دیگه. به جز این که اصلاً راهی نیست. بعد هزاری انگ هم می‌چسبونن که آقا یارو تروریسته، فلانه، بسانه.
مرد حسابی مردم گرسنه‌اند. خودتو زدی به اون راه. من با این لباس دیگه قشنگ با این لباس نیروی انتظامی ناراضیم. وای به حال مردم. یعنی قشنگ میری بیرون خشم و نفرتو تو چهره مردم می‌بینی.
می‌خوان جرت بدن منتها نمیتونن. یعنی همین الان میری بیرون اصن یه جوری‌ان نگاه نفرت‌انگیزشون نسبت به این لباس قشنگ معلومه.
حالا یه عده خودشونو به خواب خیال زدن. بابا دیگه خجالت بکشین. بی‌شرفی یه حدی داره. مثلاً انقدر. شما دیگه رسیدین به اون سقف. یه کم خجالت بکشین. یعنی اصلاً من نیروی ناراضی‌ام. وای به حال مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jciHwHbu0mjZ1DU61jWT25o0fPAdkqbbXtUJyMcaAzNEGvss-fpWpCGOztBfWhDAoqQQ1e4KpDvEhl2Xrg6tkt8LWvYa8UW-lxjteDs25OZxyphMeD2NldqKHFcwqjtejSHchZ8NcBnOtoMpnQgdoHylvHXicEQa_VTZWY3wVDhlGPEQ8-vRtKeDEEmxk8TWLzLvM8FD8VlaUmZCTncq3FypIiUsXgSfqBAo-LicBxI17DHwMu_EttpKx4nv-X75xFvYVwbIW7mrlmwSNANfNcsk72kztiiNiDDoudnhC-_tWu99HlYfU6mM-pYWdGhP1u06o3PcPvqUxwoy9oIXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdRiaQFtXkCJyTqbtUCwZRDWosCk5qlKBXC2puc6prqoIzj8BCW7EKLTfNecLvm9hz9s-e2i8GVZSV46_aLbxyzHp9dYztlMovzOw75_qztQkehUU0TJofWjNA4JK9K1uygDW9CAnCkK_aoG-KYG-OMYc8gBDGsWdf5AWNzpDPYbGZXxCQPD33JITJJqjeuh_QtWHohbq7YvOUoXRyaRNYgNxHDCxCVHP4g48I0TPVddgODAMnfswvv2jtRl0ORty8YtbTkdacBUqotMP3MOZ9ro5eY-J8ypArVtDXIEdz67zy_JBwCahC-vWKD3t188ZT522IVnxvohsxJd2P89MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5Ady4c7H3JQbgOZ_Kk_WptbtRepiRj2bOnixZSoyPtdcOJZXDpbzEVNAYA-Y9StHrTGfrGpL2z3ScWrB1Rdh0YRMZ1f7clKtfueSgJeSDgifvPNoAe4s39Muc8YyYkiIt6JDPqJGAdrpHJNOpuKkiAXAHkdRdP5tWb6zPmxEhkp6E5YcSrA5LI5zvhoR3mzcMA4uJxEFVIg96w3q8iPahlgbNqv3lt6r4gyHSP1IO2dC0w9kEi-z2HUUxOrvmA-_mhjgrtPo1izASTo_otX-647PVnDGiC74c52Sraz7YIiPeqpep6uFKhN1AJSzgROK8WavIWHl6BU6mL2F09HwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDVI5wtTCvhd6ooG8hv_rVSLJdwJcqIuAXcetNyaGNl0AoRgwyxnwhYukMiv_iTbgysUauELEGbNc2_W2vYW-qoGMcoRS3AOnk_arKd4kA-dPgTGYxebxzr0xS_5eXk94fds3nTIGSWq8aotXIFq1_MOl6LNw8r49lP83uZKu6K5ADV5fC-AtbKdyXxsCkvIwiCBEX_YKk1XfuIkShVCbVMrkJvEBy1w5dChIqd05AC_gNsc2Br1hcH3rKRANZ4Bzp0epYXKfZy29qUuIF3Y1YWN6E-Ue3vZv31BiziSRbxVrGdFxYhzPv4UFTZ3pqOAVOnKIg0P3AcylIouFCSOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دختر یکی از پشم ریزون ترین خودکشی هارو داشته:
دو روز پیش "پایال دِوی" داشت اولین فتوشاتشو برای یک مجله تو حرفه‌ی مدلینگش انجام میداد که یهو وسط عکس برداری تصمیم میگیره بی دلیل خودش رو تو رودخونه پرت کنه.
ویدیوش خیلی عجیبه و بعضیا میگن امکان نداره این خودکشی بوده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71347">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032667483d.mp4?token=IPTzEU06gmJUfT1zBCbwFIpdSIGmE_-lx7lZ7TPXev0VrzKox-EfeLYkyrJx5IqMKRQYjtneEFFk9-8O6yoet9elIBTwdkG9vPx_DWFYNiTyhFJWWEeGRD8n_Y1lcnoleTgKLPPZcGjguP2aErgecleoKqiaNSvG7jvXGJVZSF2mluKUu7-uwzlgXqo5A3KZvbwbdQLHkAeJZoYPk1-4mGjv_R5ZUKByPwMGtGpXpREX10KWV5mnPzdB0yV9f_CgD4O9uCM6tP6YIdwdNLOW_pCEb1UmgSghoKMFcUZPII5s7_k5BtPIDpLtby4vIOej4w2g_N4pGLuwfpK8w5b8xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032667483d.mp4?token=IPTzEU06gmJUfT1zBCbwFIpdSIGmE_-lx7lZ7TPXev0VrzKox-EfeLYkyrJx5IqMKRQYjtneEFFk9-8O6yoet9elIBTwdkG9vPx_DWFYNiTyhFJWWEeGRD8n_Y1lcnoleTgKLPPZcGjguP2aErgecleoKqiaNSvG7jvXGJVZSF2mluKUu7-uwzlgXqo5A3KZvbwbdQLHkAeJZoYPk1-4mGjv_R5ZUKByPwMGtGpXpREX10KWV5mnPzdB0yV9f_CgD4O9uCM6tP6YIdwdNLOW_pCEb1UmgSghoKMFcUZPII5s7_k5BtPIDpLtby4vIOej4w2g_N4pGLuwfpK8w5b8xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا طبق فتوای جدید حضور نداشتن تو اجتماعات شبانه، غضب الهی رو در پی خواهد داشت و تو زندگیتون ذلت و خواری میاره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71347" target="_blank">📅 11:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71346">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhMxEOb8mzaKNll-38wZIi0jlOYJLgKPo1eB8V1tN_I5XIxhagzoV6rD5sOafqewupset-ieVH2di9B2Cl-bq-OgpVXgRMMLOcG7Q7KF5uVnweMLdZb1toMPmkLYo3Au2K46skuZBjuC99I3vNn9QiH4e3u4fyJU0gOByppRbS3CppQlY2cbJa3f_KlEx9m2M4CUHyOoKfcNiNMXyJpgS3rL_4hYKlyM2gJLOZuFloMSauLKodSnTjrW4eDq3IDXOJBNxtdL0ipSmdNOI_ZOXNzeM3Q6sNVSZ_0jj7WProxN_qOOT25EfstPiWfNXYmsu-zFsOdztpS63kPbmnYHvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
دوازده کشور با صدور بیانیه‌ای مشترک، ممنوعیت‌های ملی تجارت کالا از شهرک‌های غیرقانونی اسرائیل را اعلام کردند؛
🇫🇷
فرانسه
🇬🇧
بریتانیا
🇨🇦
کانادا
🇩🇰
دانمارک
🇪🇸
اسپانیا
🇫🇮
فنلاند
🇮🇪
ایرلند
🇮🇸
ایسلند
🇳🇴
نروژ
🇵🇱
لهستان
🇵🇹
پرتغال
🇸🇪
سوئد
مکرون، نخست وزیر بریتانیا برنهام، و نخست وزیر کانادا، کارنی، توافق کردند که وضعیت با خشونت «بی‌سابقه» شهرک‌نشینان و گسترش شهرک‌سازی رو به وخامت است و به طور خاص پروژه E1 را «غیرقابل قبول» خواندند.
آنها از اقداماتی که قبلاً توسط ایرلند، اسپانیا، هلند، نروژ و بلژیک انجام شده است، تقدیر می‌کنند.
این بیانیه از اسرائیل می‌خواهد که فوراً گسترش شهرک‌سازی را متوقف کند، شهرک‌نشینان خشونت‌طلب را پاسخگو قرار دهد و اتهامات علیه نیروهای اسرائیلی را بررسی کند.
آنها «قاطعانه با هرگونه اقدامی که منجر به الحاق سرزمین‌های فلسطینی یا آوارگی اجباری شود، مخالفند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71346" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71345">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
سنتکام:
کشتی «ریسکو» (M/T Riesco) در تاریخ ۸ سپتامبر در خلیج عمان غرق شد؛ این کشتی پس از تلاش سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی ایالات متحده، توسط نیروهای سنتکام (CENTCOM) منهدم شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71345" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71344">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=uL3pH__qTtoZ9d4qQtpNn_rS123iul2jo0qIp40GezjVvJJtcQxtwnPG5AJAhJCGLfW4xWDbbPruhedlLyd-en_b6GGGbXGvWyzbNM6BHxS07pkGS191fb-lOLSyJMf8f01QOIAL6GYLn0tz-03BJEOADm0PswMAoQj-HN2Ts4ED1Ha5R_FE2h8Y02Yk-QBrj9iGV0Yi5aRXVtkCNmUCctkF0WXg-c2pxwBuuucgFSkW5WkbZrUyEmiRYguWMMtduccuEu6fT6goTJTSEiPuMma3H0BJSYwSKkMCEBCaCtRx3xiMb38M7AAZLBNsGAFS2idBST1_d46eh-lM_qtXmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=uL3pH__qTtoZ9d4qQtpNn_rS123iul2jo0qIp40GezjVvJJtcQxtwnPG5AJAhJCGLfW4xWDbbPruhedlLyd-en_b6GGGbXGvWyzbNM6BHxS07pkGS191fb-lOLSyJMf8f01QOIAL6GYLn0tz-03BJEOADm0PswMAoQj-HN2Ts4ED1Ha5R_FE2h8Y02Yk-QBrj9iGV0Yi5aRXVtkCNmUCctkF0WXg-c2pxwBuuucgFSkW5WkbZrUyEmiRYguWMMtduccuEu6fT6goTJTSEiPuMma3H0BJSYwSKkMCEBCaCtRx3xiMb38M7AAZLBNsGAFS2idBST1_d46eh-lM_qtXmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
مهران رجبی:
اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71344" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71343">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=roo7IUFXboKFZ-szS7a3y-Vz0e4NyO7Z4C2ilyfbXrxt_caypGKxFfdtCkI7j-oiBT-75h6MEYyhjdLayPLYN4riuqrC1cVmdnaELEga25TUpxAKThZpCb9Wg6ji-mC-gQ0ojAqdtp7JOI9uAB-YiNbQavOaiUrZ_4DNMbwAsf53dZbF-4Bw0V2vZy6_-pXSqU-k9UT3vynlOycK7s8yVX9iAIwm1Cnr23f5733xSz6tXtLZJUskP2NaR2PoK9cQTe6XzQeSB07FJ0H6X83w8U61bgyHWOMupz8O0nE2TGDV4rFmLLb6fijObJzOc2TS-hi5Bqzpbu8p-I56TAjdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=roo7IUFXboKFZ-szS7a3y-Vz0e4NyO7Z4C2ilyfbXrxt_caypGKxFfdtCkI7j-oiBT-75h6MEYyhjdLayPLYN4riuqrC1cVmdnaELEga25TUpxAKThZpCb9Wg6ji-mC-gQ0ojAqdtp7JOI9uAB-YiNbQavOaiUrZ_4DNMbwAsf53dZbF-4Bw0V2vZy6_-pXSqU-k9UT3vynlOycK7s8yVX9iAIwm1Cnr23f5733xSz6tXtLZJUskP2NaR2PoK9cQTe6XzQeSB07FJ0H6X83w8U61bgyHWOMupz8O0nE2TGDV4rFmLLb6fijObJzOc2TS-hi5Bqzpbu8p-I56TAjdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از طویله مجلس
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71343" target="_blank">📅 09:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71338">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gv1YBgJMLhclOyuDsz55CcaK8wf1-eYffpnFeT2zMmaKyNd3hKzTO45qQGe6TgAxJi9H8gNsN2_7NHtSQNxSIZRmMYwAZ0wRqwx8DQql0_9GwSUyUVgwUENAYNyhP0O9KgoX8RASqecnWpIwf_sL1IoIb8rbZftpmmez2TVc_RFaEcXjhsjKy2bsSVe3ZfJLNcAZjsvut--KWBhbyL2tcsn2OBn4pwJ3Np0oLxxF6yBmgdGbfTCzGcLZ4veAdi3dMf1c9eKLRmDbtn1FvCRWM9bZFMoGEK9_ZwgIJn_VsGAe4QGZ2hF4jd9gn-ukLPb-XG4jhtLpv2AGbGZAl_WSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKTf5QWMu-PbG2i6Ja2Yf8wQfTq9SxKR7dt8kstYASx6c-SNTJkChqM7kvCIUppAlKUDBaktTwS9glybdLSuDtfjC-TC43-7-sAjBKfgi4cM2_eWcqy6RYTmy96f3LgCW9hv2Txn3X-bEQfYlEON3cFjb6mJfJrQy_RwJD4letQgKizEhma_yY8DMHkKaRoTRE971u79sfTHbhR-myY6M0J3-a9H6kz-Jhj7__4DLTznLvXEiZXAzxh8GmRV-NLNymKGw_JnurtbWhxNJrfboH__p9Bx7aNEd8E9Ek2TuEIhVyEOOeEDe97hpKa6vHldhXQhj77mmCHo2RKhS6F6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoJvK-dMyxGQOVVL8pkzFHPaRqMkoqw2-5pOYDTifQBqv-lhHUTxM5DT8-qgoLGN0qYj4CrPTM4Wp1eIbLAHk_veSbfrh3wKD20TjitH0g_FGcvDMwZwj_I-1eYFUQGqOXDD8ydGjwyTV-pZm0iGG5K08AaClXSHxCf-Uo5V1oa226lnaW2KRQv9LK1VBkyMHYBfTe6n1lqSqvBLg3MgLT4WmwEhtK4elyrvCtfRAzyhEEslrd1SIVjQ6yBWO3WCrGqidsOeHfBUlwuX2Ceh2rAVse1fq2rGMv_VfzO9PNV0I0OjCzBaQjjRZmNyxVej2FvdfrOsgW6bIWeDazpoDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDZWP9RgZXtrTdaM42Ow3gq88boM330LbCFZO-THvTXe4japXQDeHZCQ1IragfziNFkbjS1Tdt4eV2MhJcKXVfctDqu1dWRGCin2eqXxgs0ltEIdHE8tN-okLlolfu_D0qJAVV2URrokV2uUGPBHoNr6WDVZUPVsN7Nn4h5D1W0pGks2cfmc7vWcDxO41f-hj1txzYdlYIF-DgcWLrSKYxnodBOskzbYxquiLf8hSxnvufPPzly_ElcWm0Vy6vZqA_bwrUN8WTGCFBs3VXMP8L2GKJx4jQGhemFrH_c0FI5SM2Uugh3WxxnTCCmOs7e8HHQwDVAGs3YjxGGZjw5y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzvCsm2kq9jBWh3Mh0TGPrnPmrrISRYpszN2I3pl1-yUdgI6Hegjr23zX2Cqvfm6guGQaBuYqdoTlS9G3GUYNNKOxzcLjIdtL6AVj8O1ndDVr8DU5fSgH2kHuqsvRIXzOTexLcTnc8UqjbLrBeTOc7XMQhQDMzy9Mv_zYYWhGFg1B6MW7V0eeYF1vHuvUjVzKmlEP6bofVahXteUX4aZxGr0O2ARvVSqB8gq8gFh4gEAiSYjf-YpBqhpouLMFNx9XE6vOaEzK8ROxOdDY_VngmrxdywwNkHNW1GRtSiVnYmoKY9K23s6FOaVjImx6_KGyyTTkMr3q6I4jPcAYgEelg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه پاسداران تصاویری از زیردریایی‌ بدون سرنشین آمریکایی که به عنوان غنیمت گرفته منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71338" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdyWZSZQh_x4yr30siG58ryRi2vv-GqnbB-JcFf9eeWKh2tRVDB4VsaMH7-y6riFmJf75WfWkrUbEQEQiR2xk9_GVlGHmTD8LxNtUarIw1mqIZoJPRj42h4RpGr1n3T1sFpngC7vHShEWw-cuOwpQlv6pSsWfezFUMNNYui1IzVN47WhwF_TA2Vt1vc9usBUWhdl57rOWoeeOAGvkG-LJEMtGJKaxLg9fr_mEBsOhyWdrW8rYWPTrWsFSuQqIDo2fEZwtyCw1KAsK7pWU0dQM6Otv8S_c6FAA8Rq3X2RItWmvy04g2pAUp43Oflf2DJCEp7sA4W8bLNcWyomYxoTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
〰️
#فوری
؛سنتکام:
نیروهای سنتکام در تاریخ ۸ سپتامبر پنج شناور حمل نفت خام ایران را منهدم کردند؛ این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی طی دو روز گذشته، دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد.
کشتی جنگی آمریکا با موفقیت از حملات تلاش‌شدۀ ایران گریخت و به گشت‌زنی در آب‌های منطقه ادامه داد.
هیچ‌یک از پرسنل آمریکایی آسیب ندیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=dIuajY6Nlb96G4EODBlWmKtragLQ6qusfALC2K15V4ScqgLQ_lTPub_bMdLIDJ3plGQx_a4trm1w2xGUwvt1pH6CpOubA-du30_6vt5C6-VFOoY9mqt5cV3f3VDw8OK9h90TVNcuDPHoHvkpgGK-q0Sxm2S1sRzEccUoGlpiN70ZVaYUPn87hUiYv2ltXWP7_1S-craPYjOJ3osBt_MuCMJX0dhlQVcNaHiFAseMnqFhu7snI4j9lM4clrGkdUhQNQEVejboRPTuWGuEQzMKSts49Nw8FbT9XV3bux-d_EJbnEXF9BdoH44znGlXtcNBpf2xvCBQa7A-M81f7xtMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=dIuajY6Nlb96G4EODBlWmKtragLQ6qusfALC2K15V4ScqgLQ_lTPub_bMdLIDJ3plGQx_a4trm1w2xGUwvt1pH6CpOubA-du30_6vt5C6-VFOoY9mqt5cV3f3VDw8OK9h90TVNcuDPHoHvkpgGK-q0Sxm2S1sRzEccUoGlpiN70ZVaYUPn87hUiYv2ltXWP7_1S-craPYjOJ3osBt_MuCMJX0dhlQVcNaHiFAseMnqFhu7snI4j9lM4clrGkdUhQNQEVejboRPTuWGuEQzMKSts49Nw8FbT9XV3bux-d_EJbnEXF9BdoH44znGlXtcNBpf2xvCBQa7A-M81f7xtMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=LH7KQ1JO3ENJryebBNX7IeqdfPuWkkB5N4eRAAKUpNGK4bWESs52JKm-InEHMNLYUSiSYoc_FBM-s9k-DYjP_XcjWOQWh8-r2fb9ulscPNtqzqj_hs33OIWxrq0IoD3ylmMMSmAPc1oIq3WmWL6H8N1fLGLci7BSyF3I1XiLfCMMJFyDIcWZHUj853eDPLNLOURcY0SgWL976PA7R7IAiWBa9tx1niJAAOwjTQ6h_ZNcS5ACYjC6RHaocg9vYL-_fING3YFyJhp8tp7X21bekahy3iH9VdQBbupBTYcyt2HniPz_wnic1S3jhMftHvl3gFcHAHU4D9ypn46_1AmBXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=LH7KQ1JO3ENJryebBNX7IeqdfPuWkkB5N4eRAAKUpNGK4bWESs52JKm-InEHMNLYUSiSYoc_FBM-s9k-DYjP_XcjWOQWh8-r2fb9ulscPNtqzqj_hs33OIWxrq0IoD3ylmMMSmAPc1oIq3WmWL6H8N1fLGLci7BSyF3I1XiLfCMMJFyDIcWZHUj853eDPLNLOURcY0SgWL976PA7R7IAiWBa9tx1niJAAOwjTQ6h_ZNcS5ACYjC6RHaocg9vYL-_fING3YFyJhp8tp7X21bekahy3iH9VdQBbupBTYcyt2HniPz_wnic1S3jhMftHvl3gFcHAHU4D9ypn46_1AmBXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=XCYNvrLecJXdLuKmWYY0gjbW8mdIpcF0itpPTSbAl3BIQ1bSsYmhOO5rSQS96PDPNvyYkqAKNDE_R915o_Vv4YfqIV4GTZqwjyzD0TdConQPBdfO54_wdz16eValls1nWJkin-dN8kZjbLQWiAQ-WMtXShUJNqXXxM-0ljD8iHjOhn63q1zsc2LkEawRRjkUhcGvoY2t5GzvMt9t2vYhEzXrKDMDZhfRS4SsjELSlywfnM2iIzV-BKnfKHh3nJnJfWVNoXjYsI0fYVtkPrBsjK7mokww752FUYnS_kZZ_jsq1F6gHW8Idhyf1teJev1fu5249YotY8ev5WHviUOsfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=XCYNvrLecJXdLuKmWYY0gjbW8mdIpcF0itpPTSbAl3BIQ1bSsYmhOO5rSQS96PDPNvyYkqAKNDE_R915o_Vv4YfqIV4GTZqwjyzD0TdConQPBdfO54_wdz16eValls1nWJkin-dN8kZjbLQWiAQ-WMtXShUJNqXXxM-0ljD8iHjOhn63q1zsc2LkEawRRjkUhcGvoY2t5GzvMt9t2vYhEzXrKDMDZhfRS4SsjELSlywfnM2iIzV-BKnfKHh3nJnJfWVNoXjYsI0fYVtkPrBsjK7mokww752FUYnS_kZZ_jsq1F6gHW8Idhyf1teJev1fu5249YotY8ev5WHviUOsfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=t9GlZnL2YXPNumWhjrjQbr_Iqrx2hkcO1xY6qQA_9UrhNRquQCjH6_msUtzB5oeGUj_bxSdHW8NkSCpXKTFmBTgTfXYiWvdf2xob0Px6XPPkCthvTVBUQmyjLOdWhdpiXs4XV58da_mYJPWPxZeDT4SDO9Aebhol0vRtXh_puvJLFPyv-sO7fJqmrlhOXv9INYHTNCHakkhhM6CP5QZKXxE4Co_3j_xg5SGg93JjILCu5Zfi_qv666heoCFNhEs_rbxOYxIwRqLsc057loLQRISUTDofCtOTRbxAX07-3r11z4tuJcqFrdxMkM1IHrGJMK8e1eLacVp2W_na601g6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=t9GlZnL2YXPNumWhjrjQbr_Iqrx2hkcO1xY6qQA_9UrhNRquQCjH6_msUtzB5oeGUj_bxSdHW8NkSCpXKTFmBTgTfXYiWvdf2xob0Px6XPPkCthvTVBUQmyjLOdWhdpiXs4XV58da_mYJPWPxZeDT4SDO9Aebhol0vRtXh_puvJLFPyv-sO7fJqmrlhOXv9INYHTNCHakkhhM6CP5QZKXxE4Co_3j_xg5SGg93JjILCu5Zfi_qv666heoCFNhEs_rbxOYxIwRqLsc057loLQRISUTDofCtOTRbxAX07-3r11z4tuJcqFrdxMkM1IHrGJMK8e1eLacVp2W_na601g6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=Zw0DScmJQBe-DBIMECrxtKFYT-FbfMldtCoEUWITDQ_ngJcBodoT60VQs5iKPmim9v7qFkXKkOdEnarZYPzp-yQKY5L9UxBRA6tqveMhJ3Dpr0jMcVG5BGomCjDcRvCPeVlFUyAwZkZTEXKp7Skv7Y79KVZqY3cynly3_vIIpr5GfROKE6UXpKlkUTVTNP3mt92YyFnStL0VpfEXtKVgVKRvXPgpfZpMaXfbDW33IQvQWaYWbDDeuQ7QQed2OhDFzKKJ9vBpE42pSD4RiDUK26ord2k1EcgXSy-n3-RSgdOsRbOPek8ivTAErndifywIQKBu1C0Aov93AFzMTpeTuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=Zw0DScmJQBe-DBIMECrxtKFYT-FbfMldtCoEUWITDQ_ngJcBodoT60VQs5iKPmim9v7qFkXKkOdEnarZYPzp-yQKY5L9UxBRA6tqveMhJ3Dpr0jMcVG5BGomCjDcRvCPeVlFUyAwZkZTEXKp7Skv7Y79KVZqY3cynly3_vIIpr5GfROKE6UXpKlkUTVTNP3mt92YyFnStL0VpfEXtKVgVKRvXPgpfZpMaXfbDW33IQvQWaYWbDDeuQ7QQed2OhDFzKKJ9vBpE42pSD4RiDUK26ord2k1EcgXSy-n3-RSgdOsRbOPek8ivTAErndifywIQKBu1C0Aov93AFzMTpeTuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=u_Adm060uHnyJFGJ3h4Ve09VmP70V1jH6nK-N05nlvj40F251n3-X2AJwG66J0017hSYx_B6_5LRvIgOr3DHJ4ytNjmbKw5n8McpUG5VNqsEKwbhsYrRI7j6UkfFylTdPshbT-4VwMqdIR2EGPyQjBaSAUJMMupCRwCKk8UKqk7takF0hwyLICg0nZT2-e_cs9yoj164F_iEWQpG3_2Fl6A6u5z-hMD8JcrphEaLEaa7Dmzg8QOKaMdhRdwYEkVpt9B72Zw1XnMv-nzMvTSDeBop-L-dsS9BF51Tflje-qIpbcltC9PnsaKzR3NHx61S9ZDpmD2kMmoooC43B-8CcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=u_Adm060uHnyJFGJ3h4Ve09VmP70V1jH6nK-N05nlvj40F251n3-X2AJwG66J0017hSYx_B6_5LRvIgOr3DHJ4ytNjmbKw5n8McpUG5VNqsEKwbhsYrRI7j6UkfFylTdPshbT-4VwMqdIR2EGPyQjBaSAUJMMupCRwCKk8UKqk7takF0hwyLICg0nZT2-e_cs9yoj164F_iEWQpG3_2Fl6A6u5z-hMD8JcrphEaLEaa7Dmzg8QOKaMdhRdwYEkVpt9B72Zw1XnMv-nzMvTSDeBop-L-dsS9BF51Tflje-qIpbcltC9PnsaKzR3NHx61S9ZDpmD2kMmoooC43B-8CcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNypJInmYBdLg6XHcPj9rDtgEaqa6D7FIU5t2ILya3srzvIR2MZb2yllsNz77zkYk6dBbqCGaPaxBBaxRld-0zqIuofZT-Xrq2ebNrYwPjIvYd0BFNN62jiCOwFv5wI_QwbD5OaOaqsCU_Ce0th78lp5Fzjw9IQRTjPo4fcl_Jah43cGnXiaNa-o3vZmm8Q5_-vY1Onj7zhzG23egggKIENeW7Hl627vMTvGkikX_zHIr5KiyT_-relHZ5zivz6m5Thwhnm_LN1EC5vw5MYDsLamAvIlmD-5M9Oo9BM4EwYZB23wT_7sPhsZ8PZdN9722LR1lmJAr2VhnMiMekTptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=FyLQpNUjp07s8dRfMHmGw4zoaU1crox4fXPgFcIwAoKUQgbnw5PeMu2q9uTDBCuR4NyKphgMIs7P61na8Mme8iGfiYL9pJO4Wl_lxoK78gdOy1OyY4eItyoSnUsE26_JYbFtumbWGKacTFltDhlv66c5gWPsUv77nlVsrpoLaIfwQV4EUb5Atj6SF_LcQpZ3yfXxhJi5jxFCsvGLcZY4jKA9rpJw9jemRS-EGu7IftYXRSe1a0TyHTGlZ14YqDjkdyXYOxsDe2KMJ2PoO0nqdCX3qSJSYWU1DSAJ9UKz7zG4y_T9WgYFq3piwzeFm8yu0RAPM5xgXr3GFLTJhqOz4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=FyLQpNUjp07s8dRfMHmGw4zoaU1crox4fXPgFcIwAoKUQgbnw5PeMu2q9uTDBCuR4NyKphgMIs7P61na8Mme8iGfiYL9pJO4Wl_lxoK78gdOy1OyY4eItyoSnUsE26_JYbFtumbWGKacTFltDhlv66c5gWPsUv77nlVsrpoLaIfwQV4EUb5Atj6SF_LcQpZ3yfXxhJi5jxFCsvGLcZY4jKA9rpJw9jemRS-EGu7IftYXRSe1a0TyHTGlZ14YqDjkdyXYOxsDe2KMJ2PoO0nqdCX3qSJSYWU1DSAJ9UKz7zG4y_T9WgYFq3piwzeFm8yu0RAPM5xgXr3GFLTJhqOz4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=sdIhJGPWNhji4CwFR8nc0FTItTH6PeXesoC3wRxwA4C0SwA_WQkxZ7H1g0Q7gn18AhIuDV35O8OiV-K1oN5m1QzmJm4fRUjSkEWqCXu4VJvzm_LfVMzJ7racW9WSVS-NbTfhQ4p8utbNOdiEBqg05mYGKQoW1CxMwp3B9OMDbagYrhQvqIReCDRAySJfeDVsgHr2kPZccgIG300J3HXK6JmpjyQAj75bdk7HsM00S-cvX_8Zf0uBKUpVS9F76DdX84I1to6j78a4TZ3uafp8P4ADVCsQsxGpslQoZJZMx-OkIzbi5Upa7oGcekY6AJaFk5wq8aElX38nWdGwmnxbkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=sdIhJGPWNhji4CwFR8nc0FTItTH6PeXesoC3wRxwA4C0SwA_WQkxZ7H1g0Q7gn18AhIuDV35O8OiV-K1oN5m1QzmJm4fRUjSkEWqCXu4VJvzm_LfVMzJ7racW9WSVS-NbTfhQ4p8utbNOdiEBqg05mYGKQoW1CxMwp3B9OMDbagYrhQvqIReCDRAySJfeDVsgHr2kPZccgIG300J3HXK6JmpjyQAj75bdk7HsM00S-cvX_8Zf0uBKUpVS9F76DdX84I1to6j78a4TZ3uafp8P4ADVCsQsxGpslQoZJZMx-OkIzbi5Upa7oGcekY6AJaFk5wq8aElX38nWdGwmnxbkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71318">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ارسالی از تبریز:
همین الان از تبریز موشک زدن
سایت موشکی امند
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71318" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71317">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
چندین گزارش از خرم‌آباد اومد که صدای انفجار شنیدن./احتمالا پرتاب موشک
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71317" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71316">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ارسالی از بروجرد:
سلام بروجرد هم فرستاد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71316" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71315">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
گزارش ارسالی از اصفهان:
هفت تیر مبارکه اصفهان موشک بلند شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71315" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71314">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXyN29GIgn9U60cOEFc5slgx6bwB1itIJMXG4DoV3VdAWv-fUksLBiyG6FUgNoE50nkgKtuZSVmCbbvPRGJtyKnjTbxiDJWMcB2vGbOpW5mjSYXdJBV1oy0uyWWaqtFSzI2MhJAmq-cXJi9RNazVq_If2Yu_F1VlAmZ4M1D8-61d1bI3fJSNKTOZCiyisQNQHFusxRc4XzrEbLSUP4hbPdUauQoHgTIg7nGxKag3eYuw8vAnQEYucWB1LZXym7GUVF5cMulqIaV190kHqww8-qe_gi2xOLMAYhh4ThbfpSGTq1i-QxYLUkADjTuYm8SBaH8B5tZEQUVIpAZ6eU1HUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71314" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71313">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
گزارش ارسالی از یزد:
از یزدم موشک زدن همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71313" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
گزارش از اصفهان:
اصفهان الان زدن موشک نمیدونم شهر رضا بود یا نجف اباد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71312" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
گزارش ممبرا:
۱۵ خرداد اصفهان شلیک ۲ تا موشک همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71311" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛صداوسیما:
دقایقی قبل نیروهای آمریکایی به یک فروند شناور تجاری در آب‌های ساحلی شهرستان جاسک حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71310" target="_blank">📅 00:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZhrKu2qlekIEWUGFn4gMs9iwuwvxac2HatJOyIRcs_Cw6usVmGs0ZVxhmOgLKTQtMKMN7Mu4BOVi5BC4BoumihCmt5zGvPzoPR3G0T_kPVSQfHmLvBf4ndMA-pRJrarrScweCCY2IuiQMNQhkJ10hrGY80bfEP3RdLAYnKBwBQ27koXnWB7D4mbtXnI4fosdJcD7RkGXCzDjVcjm9lzz8H52sFLjA8NK69R4E3ciulUbiyCBTKaG9OoaDoklVDYajGPNryZapD4Xx-oiDysgIMFzDK6Q7pBf8TLsyVL7RV3wU5R5Avis1f5Or8PFoEjkPHyk-Shgiu9Np1hLHWK_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:ایران ظرف سه روز، دومین موج حملات موشکی را علیه کشتی‌های نیروی دریایی آمریکا انجام داد، اما هیچ‌یک از شناورهای آمریکایی هدف قرار نگرفتند.
این حملات موجب نگرانی واشنگتن شده است، زیرا به نظر می‌رسد ایران از موشک‌های پیشرفته‌تری استفاده می‌کند که قادر به هدف قرار دادن کشتی‌های در حال حرکت هستند.
مقامات آمریکایی همچنین در حال بررسی این موضوع هستند که آیا چین یا روسیه ممکن است در شناسایی موقعیت ناوهای جنگی آمریکا به ایران کمک کنند یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71309" target="_blank">📅 00:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYkHKVmAPvWGW7b03AZ0u6wG32QBKWrpvVGdbgl8KgvHgsoxDE3MSBMKWEbrwM20AgHpaNY9YLQB-Z6EW7uavS7Q_-r7Sp7e9c6Bavfosv_3ikDCgsgO3qGLPryHgyHt8nd5re0zQcuLaz6cxih_B2MKj8LLr5Rxdu-8_ZVB7KOfaHoeVlpyIFOXMY1YAs8oWpMBWtNrC_ZztRvtXe6fICrSCfyd0kziouYUSe85gP-wy9D_rb7xWKK58xWgW3nBr1c2bFhFVwGVxf_OFrLFOHaVKIPs2vPTBGAq_jdMqOfE0cFaJrhaO1noe45jUaEqtl3j_PxbanhHmhkGw9TRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
به تمامی خدمه نفت‌کش‌ها در بنادر و لنگرگاه‌های کویت و بحرین هشدار می‌دهیم که فوراً شناورهای خود را ترک کنند، زیرا این شناورها هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71308" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9XMI8q-vpbFZWFV5XPYhZd1fBrHT7Pz78rea934XLAt-IZRp3xRaTzovkLNLp2GyI-sV9Zd7vh2fEpj2jPrbH8GqPVHiZh8qoLiJ8LItYbVH-njhsmMpGtcoZN2KbZyjsHe3rRteyj9RSQff62yg_sjh1-hAzVDyzw0o7b3YUbckslHWLlEx6ABWhbz5fxXKrxC1HoqnP6Nef6MV71yIzQlQuclXDDCgsAjWbGaxwezpiXnbI48vh8LbOs-yqJt7tkxncvzE-9PxYi6XP_6LHSKAE5raTjpMZoM32aVrABX2fVyj_UtY8cAkDef0uz_5Anc-po6Mjx9LqVd5x-kCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
مصطفی نجف زاده:
آمریکا با هدف قرار دادن نفتکش‌ها در سواحل ایران و مشخصا خارک، علاوه بر اینکه می‌خواهد بازدارندگی معتبر در برابر رویکرد تهاجمی اخیر ایران در حمله به ناوگان دریایی آمریکا ایجاد کند، ممکن است گام تازه‌ای در راهبرد محاصره نیز باشد که براساس آن، قصد دارد حلقه فشار را از مسیرهای انتقال نفت به مبدأ حرکت نفتکش‌ها منتقل کند و صادرات انرژی ایران را از نقطه آغاز با اختلال جدی مواجه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71307" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71306" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=aQCdqM5gwJ6bqzweT9FPUDZUmdn8qCa7pFAIFLXHQLG3AP1jlUdlgsekh_EfS3z6n0Y4x1qaBlcwK-4ZdaUB2WxUkyb_FlAPR8ieFYMltlCBksQklXeOzQTwgN1HriOvkAaq75R_kpwTmno37FO2aSaZeaz2ZI_xw2FbiX-MKXDEqeMKzV2vpNkiXv-KvClOaFoUp1Y819oO9KfOTgRDGkHyJs4D6WNz9OaKueygOUl1SPRYuFxYYeKGje27dRfs_N0nExR3TiVkhnabTw9qwOMl3fbm_HjSD6ltbCwv6U5wlPQCxxoGALME-QNwkeRSs7rGB5BG5Ii3W8F_T59bAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=aQCdqM5gwJ6bqzweT9FPUDZUmdn8qCa7pFAIFLXHQLG3AP1jlUdlgsekh_EfS3z6n0Y4x1qaBlcwK-4ZdaUB2WxUkyb_FlAPR8ieFYMltlCBksQklXeOzQTwgN1HriOvkAaq75R_kpwTmno37FO2aSaZeaz2ZI_xw2FbiX-MKXDEqeMKzV2vpNkiXv-KvClOaFoUp1Y819oO9KfOTgRDGkHyJs4D6WNz9OaKueygOUl1SPRYuFxYYeKGje27dRfs_N0nExR3TiVkhnabTw9qwOMl3fbm_HjSD6ltbCwv6U5wlPQCxxoGALME-QNwkeRSs7rGB5BG5Ii3W8F_T59bAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این فیلم‌ لحظه‌ای را نشان می‌دهند که هواپیمای باربری آمازون در روز یکشنبه در فرودگاه بین‌المللی میامی از باند فرود خارج شد و متاسفانه ۵ نفر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71305" target="_blank">📅 23:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=dZCFs3gGDtbp-BHaDyaTKx2Mv-uVLvlzlbhNKqffD7HNeq09vKkbAui4fKm4pk0-ToGediVe81ADom5gTgu_d16ZedZgKSFSkDzKxjTfq0oIXkGQos4GxxqmQLicgILltIpl4ojDUoXZ-gykh3t7g0Rd-UKvkIfLJa6IDhMz8mAA7DDtaYh5x3jdTjaimpylGeYdlvO0JjIUCt5Uv6EB3v1emV3ANwd0BTOelFGx-X6jInox_Jy7_TSnSh2qLSYtTcgaGHT_6p-iuDB3af7zV1gcpgUkOh48OKOzqWLejuMmkxvTdTf51KaH2kenrIBXLdfB0nu8yTe1GrrbZPLnug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=dZCFs3gGDtbp-BHaDyaTKx2Mv-uVLvlzlbhNKqffD7HNeq09vKkbAui4fKm4pk0-ToGediVe81ADom5gTgu_d16ZedZgKSFSkDzKxjTfq0oIXkGQos4GxxqmQLicgILltIpl4ojDUoXZ-gykh3t7g0Rd-UKvkIfLJa6IDhMz8mAA7DDtaYh5x3jdTjaimpylGeYdlvO0JjIUCt5Uv6EB3v1emV3ANwd0BTOelFGx-X6jInox_Jy7_TSnSh2qLSYtTcgaGHT_6p-iuDB3af7zV1gcpgUkOh48OKOzqWLejuMmkxvTdTf51KaH2kenrIBXLdfB0nu8yTe1GrrbZPLnug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آیت‌الله بی‌بی‌سی از لندن فرمودن بنزین(۱۰ هزار تومنی) در ایران تقریبا مجانیه. این دقیقا عین جمله‌ایه که آیت الله بی‌بی‌سی برای مردم ایران پخش کرد!
تا حالا شده بی‌بی‌سی فارسی حقوق کارگران در ایران رو هم به دلار حساب کنه و نتیجه بگیره مجانی کار می کنن؟!
یا تورم رو حساب کنه و مقایسش  کنه با حقوق کارگر؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71304" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=YaHZ3RrLuuXEYx4pu_kjASc8fnoMxWF2WMx-O-U41Tx6AlJ5YtLGh0C9uJMY8ujRh5db62OyhNUdhKrdiiV_FZ5AKUgV51vXdBgYRwZo1oIzqLoskfk_jWRlPlwvtEtiM5-6x6FGXuquExMzJtXEO4nSqg_ASnYwKkYRgLqIAZ6xalQoWTfAhcaytknF20h_mUUMu00Zg6-KfoHvWyH6YlBezYXBvCxMlR3IW4R2ez49GoWJR1mHXCU87wRWp9v2LQ_GoC4HE2OE7FZfRwUqP0AQjW9Lc9GYdvZ4IMsh6_Sd0lcmVpiFSpvmqFZbAhAG2zJD-xqgIN7krm2RCIzRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=YaHZ3RrLuuXEYx4pu_kjASc8fnoMxWF2WMx-O-U41Tx6AlJ5YtLGh0C9uJMY8ujRh5db62OyhNUdhKrdiiV_FZ5AKUgV51vXdBgYRwZo1oIzqLoskfk_jWRlPlwvtEtiM5-6x6FGXuquExMzJtXEO4nSqg_ASnYwKkYRgLqIAZ6xalQoWTfAhcaytknF20h_mUUMu00Zg6-KfoHvWyH6YlBezYXBvCxMlR3IW4R2ez49GoWJR1mHXCU87wRWp9v2LQ_GoC4HE2OE7FZfRwUqP0AQjW9Lc9GYdvZ4IMsh6_Sd0lcmVpiFSpvmqFZbAhAG2zJD-xqgIN7krm2RCIzRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این روزا تور مدیتیشن و استراحت مد شده و طرفدارای زیادی داره
:
اونایی که مشکل روحی روانی دارن میرن درخت بغل میکنن و گریه میکنن
یا با حشرات توی جنگل و حیواناش اینا حرف میزنن حرف میزنن حالشون خوب میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71303" target="_blank">📅 22:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=YCNz-Tipt5NzkmNcBlEh9nD5ANPv3-ZTcu7Dls6DXqqzpQT7GAxGvB-jnnFppDWWlfZ-S_E2XqBB-EK6bUEcnQaO1HQI_FmzMOodgtZBbXXrNKLSYVfUoP-CiQc5lcpOKnmQGWCuM2_ZEUZLA3NDvJB9dBpLyfSCBMj_TvvT1VgIvQs0CELa1vDgedkBc4rfQqr-1z8CT_2fIFsipY0H4kwg_NINVlDE4FT2TtaBzJqBYLjpjNqcGqRG4DAwlaVENHnfixJOQyiogi4McW1C-Zxpp8kO4bE_iyBfKXR5q3eWOxt-MJogbXe8JRTK2-NiiJyRwjtKMKQbk27525OH6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=YCNz-Tipt5NzkmNcBlEh9nD5ANPv3-ZTcu7Dls6DXqqzpQT7GAxGvB-jnnFppDWWlfZ-S_E2XqBB-EK6bUEcnQaO1HQI_FmzMOodgtZBbXXrNKLSYVfUoP-CiQc5lcpOKnmQGWCuM2_ZEUZLA3NDvJB9dBpLyfSCBMj_TvvT1VgIvQs0CELa1vDgedkBc4rfQqr-1z8CT_2fIFsipY0H4kwg_NINVlDE4FT2TtaBzJqBYLjpjNqcGqRG4DAwlaVENHnfixJOQyiogi4McW1C-Zxpp8kO4bE_iyBfKXR5q3eWOxt-MJogbXe8JRTK2-NiiJyRwjtKMKQbk27525OH6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
زمانی که بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود.
گاهی مارهای سمی زیادی در حیاط پیدا می‌شد.
وقتی سر مار را قطع می‌کردید، مار می‌مرد، اما خودش نمی‌دانست که مرده است؛ بنابراین باید مراقب می‌بودید، چون سرِ جداشده هنوز می‌توانست شما را نیش بزند و دُم مار هم ممکن بود تا زمان غروب خورشید تکان بخورد.
اما وقتی خورشید غروب می‌کرد و هوا خنک می‌شد، تکان خوردن دُم هم متوقف می‌شد.
🔴
حالا مار ایرانی — یعنی همان رهبری — هم هنوز نمی‌داند که مرده است، اما در واقع مرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71302" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=tDb12_e2HrGAL-duPzBLHR6DF_ncuDXi_whYj7mQl5XOmO-4Tcmg23_1sT-cT21xhJ7Z3Gj_SZ388UA2IJlGgS6UvLtpQ51AJ6GABOjQHrpg2tThk3hLgXZg7vJIQzUuXntXW30dZxAOurT5vt-J1UujQdDCFlWqdvtV0GVDdTpf_XYNJK7XoQOM1VdXK5EbRmcYfjfQtvHb4TLwzvojhixJ66enlrtjrAaj72Ev0rXRW0XAZWR58ZbZ3nPfLzaMeJ5wtGGjtS6IlvqVB_Db0DyLO0VUTH9Jl-F9C2AsWL7poYpcKvawa0ctktT9MLyuFCSy0w630lcOZgTGhegoUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=tDb12_e2HrGAL-duPzBLHR6DF_ncuDXi_whYj7mQl5XOmO-4Tcmg23_1sT-cT21xhJ7Z3Gj_SZ388UA2IJlGgS6UvLtpQ51AJ6GABOjQHrpg2tThk3hLgXZg7vJIQzUuXntXW30dZxAOurT5vt-J1UujQdDCFlWqdvtV0GVDdTpf_XYNJK7XoQOM1VdXK5EbRmcYfjfQtvHb4TLwzvojhixJ66enlrtjrAaj72Ev0rXRW0XAZWR58ZbZ3nPfLzaMeJ5wtGGjtS6IlvqVB_Db0DyLO0VUTH9Jl-F9C2AsWL7poYpcKvawa0ctktT9MLyuFCSy0w630lcOZgTGhegoUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقتدار به روایت تصویر؛
🇮🇷
مقام جمهوری اسلامی:پمپ های قدیمی جا برای بنزین ده هزار تومانی نداشتند؛
یک صفر دستی اضافه کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71301" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">از دیشب تا همین الاناست که مسلمونا افتادن به جون هم، شیعه های یمن، سنی های عربستان رو دارن با موشک و پهپاد می‌زنن، یعنی کشوری که خانه خدا اونجاست
عقل
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71300" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtoJpuvgDDhifsA_9aCKsKKA4ixUIU6z5vwG98EGbQyrIzNmwbczyLABNAOm8MHope_XLutTiIdyMEBBceI9HW50ESiNMTlo8tVm9vgy9nFO6jSYRmvlxt5cY-Fg297bgRzaMWmkzz9dWQjVG8wVVOTy50TY_NQ3fBrldp6HYP1jK44lyrvf1f1dJK7rSyA5-vkBQUWAeZmcfeT3Ut1a34lftylHbINLsOIm1tP8XW4Vn9_k4LXl_5rlYuimp_wRe9TXSHiZCvkI2IYfTe8RE4icyb6fxa4b909pcP8u6wliUC1ABS9NfLYwp69NDdyhguWK3zUvCkKcDtmCcbMd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
وزارت خزانه‌داری ایالات متحده تحریم‌های گسترده‌ای را علیه بخش هوانوردی تجاری باقی‌مانده ایران تحت عنوان «عملیات اقتصادی مطرود» اعمال کرده است که ۳۶ نهاد را به دلیل حمایت از خطوط هوایی ایران، دور زدن تحریم‌ها و شبکه‌های تهیه هواپیما هدف قرار می‌دهد.
دفتر کنترل دارایی‌های خارجی (OFAC) ۲۷ شرکت هواپیمایی فعال ایرانی، از جمله ایران ایر تور، هواپیمایی آسمان ایران، هواپیمایی کیش، هواپیمایی قشم ایر و هواپیمایی زاگرس را تحریم کرد.
وزارت خزانه‌داری همچنین چندین مجوز هوانوردی، از جمله مقرراتی که پروازهای خاصی را مجاز می‌دانست و به شرکت‌های هواپیمایی غیرآمریکایی اجازه پرواز هواپیماهای آمریکایی یا تحت کنترل آمریکا را به ایران می‌داد، به حالت تعلیق درآورد.
این تحریم‌ها همچنین شرکت‌ها و افرادی را در امارات متحده عربی، ترکیه، بریتانیا، مالزی و قزاقستان که متهم به حمایت از ماهان ایر هستند، هدف قرار می‌دهد. وزارت خزانه‌داری اعلام کرد که برخی از آنها انتقال حداقل سه هواپیمای بوئینگ ۷۷۷ به ماهان ایر را از طریق امارات متحده عربی و عمان در تابستان ۲۰۲۶ تسهیل کردند، در حالی که برخی دیگر محموله‌هایی از جمله قطعات پهپاد، تجهیزات صنعتی و قطعات هواپیماهای ساخت آمریکا را جابجا می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71299" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jGa6ZV0Y2KBPZj04d1tAg0uQ6MB1SkdCCv_BkV8UuksnqZWRp_wjvEgA0HmsM6OGrd46_JZeP_iThBOfkIjho2HapnRJ09lPQryDyGPBDb7eFUMLdsd8_wmwfhTvRFtbx7QzTk8Aysdd5fjTtRhudnGPrensSh8LouqKB5WKqG9OQYl_5lNqCCNv3o8A1_aCLepYOAtWXzdf80iY4zfyfGleidYnW406pkY0rJAnZJr_9uhoxurMJvELGzOK_yGSClLPZ2Xj3z1JZEMBqjVLg7zaxjwujP99lXZUxDA7M1QENiVIwlD_3ScHsCYvNJVQMwRvFq_bgmv7zyJkb3so7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d307bda604.mp4?token=aJsFZHKjE3eZbHWmEf87pRe7HipQAA9G_BL-OuZVb5xSm6zo5WGQ3avp8o5cV6KWlW4NUyC9gMmSPFcF2DouDYX1ULW_EiHquK0th06jjMtywlQD5A0x25EKKKwyrg8YP2BaFPG36Kl96cqtWqIeEumx--i7W6AjG2WRkUvoh1KMBzk8gvABfJyxn1H9Go0C3Jj44k1rjdkqTOOBe-JcN9y6zEwAuDtH3Rtc9Xz51AViI3VcJO8qVEJEpuwD4JPU97x0r5j_1yZkzA81lBwRVrwB1EUWGfAIQmutSBk3WatfqOJRizy7qyyVh-cvy1yRRpX-I-Wg5aHntNQ7watxTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d307bda604.mp4?token=aJsFZHKjE3eZbHWmEf87pRe7HipQAA9G_BL-OuZVb5xSm6zo5WGQ3avp8o5cV6KWlW4NUyC9gMmSPFcF2DouDYX1ULW_EiHquK0th06jjMtywlQD5A0x25EKKKwyrg8YP2BaFPG36Kl96cqtWqIeEumx--i7W6AjG2WRkUvoh1KMBzk8gvABfJyxn1H9Go0C3Jj44k1rjdkqTOOBe-JcN9y6zEwAuDtH3Rtc9Xz51AViI3VcJO8qVEJEpuwD4JPU97x0r5j_1yZkzA81lBwRVrwB1EUWGfAIQmutSBk3WatfqOJRizy7qyyVh-cvy1yRRpX-I-Wg5aHntNQ7watxTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌂
امروز صبح رسما شمال کشور رو سیل برد!
به حدی بارون شدید بود، که حتی آب توی خونه‌ها نفوذ کرده و تبدیل به استخر شدن.
ماشینا وسط خیابون تبدیل به قایق شدن و برق اکثر مناطق قطع شده.
باد و طوفان شدید باعث شد کلی درخت و... شکسته بشن و بیفتن روی ماشین، خونه و مغازه مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71295" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNb4Tf1Qrr4qhKJiNQDeYaIeS6EAN8BA2TI-D2Xn092EIbJSjqk70T7Aq0Km76ZQQjfBJPk46thW2PwWk9zN-l3EVA2WdMsCiCQ5LUQ0bx-G2TW2QZC_1bKLjqwpAt9LSdBpZmv9Vw-z6cepzQ-Gvp-M40_ic798-Ndw65kp-DWA-XMrduaszAFoKPvDT1tswRZJXZ28ZiW6wLUifK6DqsuV_rGVvWI3C5uiL65LXsmPKNGTlF-6PmL9EHJSC6oXSYEwK0W3TnVfV3p7GS63tuKE-rEUgTAn06p0QtXu3u_-u83cwWWRfPWdmHbGziNFfin4dF5nJigdoMAeBXLcbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران انقلاب اسلامی:
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی‌های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند.
این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخور دار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
گفتنی است این زیر سطحی اکنون به غنیمت گرفته شده و طی ساعات دیگر تصاویری از آن منتشر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71294" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⏺
🤩
تسنیم:
تا دقایقی دیگر خبری مهم از شکار رزمندگان نیروی دریایی سپاه در تنگه هرمز منتشر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71293" target="_blank">📅 18:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71292">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=elkkdM1dvfqBguEvkzwYj2Mm5XdizNHzlDPVpbLqgsrNW-w0ZCmOgNpySWDUB2mYg75YTELuJjSHYhA1XUsem4wjQIQiQSQpW0wD4U5J3FRrsYdiQZCb529ZN8AVTnrJXq20koKYMVonV92hdU2g4kmkumHWGFjfew0-zHKRCOlE1uJn1pb7-ElZgEUCAYrMAsxrmSok92WbW8BhBZmugoq8oxz6IrWsxKrfvIaWL2-QJoIIeAkM_rgiKQeutrSil8SMSIbdbc9HMwwv-iQd3pynaDK3nyyUuOAbZZU7km02J4H9Ag8hOLxoFouGBUBemQfH3ee03iWIr_JyX2ppJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=elkkdM1dvfqBguEvkzwYj2Mm5XdizNHzlDPVpbLqgsrNW-w0ZCmOgNpySWDUB2mYg75YTELuJjSHYhA1XUsem4wjQIQiQSQpW0wD4U5J3FRrsYdiQZCb529ZN8AVTnrJXq20koKYMVonV92hdU2g4kmkumHWGFjfew0-zHKRCOlE1uJn1pb7-ElZgEUCAYrMAsxrmSok92WbW8BhBZmugoq8oxz6IrWsxKrfvIaWL2-QJoIIeAkM_rgiKQeutrSil8SMSIbdbc9HMwwv-iQd3pynaDK3nyyUuOAbZZU7km02J4H9Ag8hOLxoFouGBUBemQfH3ee03iWIr_JyX2ppJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
⚠️
🇺🇸
افسر نیروی هوایی ایالات متحده که در ماه آوریل پس از سرنگونی هواپیمایش بر فراز ایران، دو روز زنده ماند، برای نخستین بار در برنامه «۶۰ دقیقه» (60 Minutes) — که قرار است روز یکشنبه پخش شود — به بیان ماجرا می‌پردازد.
این افسرِ مسئولِ سامانه‌های تسلیحاتی که نام عملیاتی‌اش «دود ۴۴ براوو» (Dude 44 Bravo) بود، یکی از دو سرنشین جنگنده «اف-۱۵ ای» (F-15E) به شمار می‌رفت.
در حالی که خلبان ظرف چند ساعت نجات یافت، «براوو» به مدت دو روز در مناطق کوهستانی ایران، در حالی که مجروح و تنها بود، از دست نیروهای ایرانی پنهان ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71292" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71291">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71291" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71290">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ_h8xRoY2SeAZwnlKmky87wuoeHEAb__usBh1bhjv1OJ_99aBwuDclZRVVbGoar9LTBwentfv3g91V9aLQYulSfem3iJO-bpavdabfjr77ehfdW2L78a0W02xS4Igr5ZwjN7nXyVM04tmsYbwzYqM0SZP0VQS2dYc8MPtcczO3Pxe3pmig1X5h_FZ3SPiu7oyHmfPnm7fl48SkOxHiuI3-0_BYtjcrUKR4GqvLLoH_wYeReBK8LILMnD8v1-PLPuKGmb0CbFX2kdFGlkLFw9qnRTONWRVWJO-cWAnPRwv7yAbxyGDHtwC-b4ySMPEeEdQKxEGF3K1kXrQlReDlpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71290" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71289">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
دقایقی قبل صدای سه انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71289" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71288">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=hyvz-En5ZZI-9ixeAf84dGa7ibSeIcsNha22v89vCnB3Wf3StRTbuXh1580ICpBmPXtfWLGVPsReUcCcxoStFsiQbGd1-C5tUziGtJZ1kxuuM4k3z1ytsv0RVi-HeD4qXH03i9ztnHzl1HPL9Xq9QjBMMpTL35fYBhPsanURUuUOlSSNnwS8Ic8wt1DFVWcfKYLysWteNa4Kelc-T3Y10RGPhNdDi-p0e5VduzzPovAnNXr62Xagx9iYHlY4tlm3WBEuk_9c1natxWgD2pIRgxzofbio1HHdSAVv-5L8Y4hsr8JHLaCFfn3zLRBXTZj0fqfJUdNoKTen9_NBbudz87-19JQdzlA-Q1S9PkDUiztqUUUK8b1G-e6O8xNIL8iYKNZN8YEmQxFfVqFPqQjVGaDC1CotsU167lWglUQju9Uj9wFzahAxKjWFBC5ttNy8pc2hF8zikgL2N8j4IgZSQ3RqrlNIBVzyoqcUuvcUK7ShP_6r9m2d_0ErwcAtjU8vo61n6BfJ3pPkaEs8IH57uq_gw2W_m__2LpA_KxjuhpYU53UH9R1zIvnV-guyE_R1LCjmovN7dbKGtVKldZ1VYPU3DJG1J2yuaKGGOsI6bWtIj1uCS0--rrj69tsdZHdPcl3sFjBjU22zCeg9PpcC51PCDoHKiHgxaUQaJtIXWdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=hyvz-En5ZZI-9ixeAf84dGa7ibSeIcsNha22v89vCnB3Wf3StRTbuXh1580ICpBmPXtfWLGVPsReUcCcxoStFsiQbGd1-C5tUziGtJZ1kxuuM4k3z1ytsv0RVi-HeD4qXH03i9ztnHzl1HPL9Xq9QjBMMpTL35fYBhPsanURUuUOlSSNnwS8Ic8wt1DFVWcfKYLysWteNa4Kelc-T3Y10RGPhNdDi-p0e5VduzzPovAnNXr62Xagx9iYHlY4tlm3WBEuk_9c1natxWgD2pIRgxzofbio1HHdSAVv-5L8Y4hsr8JHLaCFfn3zLRBXTZj0fqfJUdNoKTen9_NBbudz87-19JQdzlA-Q1S9PkDUiztqUUUK8b1G-e6O8xNIL8iYKNZN8YEmQxFfVqFPqQjVGaDC1CotsU167lWglUQju9Uj9wFzahAxKjWFBC5ttNy8pc2hF8zikgL2N8j4IgZSQ3RqrlNIBVzyoqcUuvcUK7ShP_6r9m2d_0ErwcAtjU8vo61n6BfJ3pPkaEs8IH57uq_gw2W_m__2LpA_KxjuhpYU53UH9R1zIvnV-guyE_R1LCjmovN7dbKGtVKldZ1VYPU3DJG1J2yuaKGGOsI6bWtIj1uCS0--rrj69tsdZHdPcl3sFjBjU22zCeg9PpcC51PCDoHKiHgxaUQaJtIXWdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇬🇧
⭕️
#فوری
؛اد میلیبند، وزیر امور خارجه بریتانیا:
ایران هرگز نباید به سلاح هسته‌ای دست یابد؛
از این رو، ما نیز در این هفته همگام با متحدانمان اقدام به ارجاع پرونده ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات هسته‌ای‌اش می‌کنیم.
همچنین امروز می‌توانم اعلام کنم که ما در هماهنگی با اتحادیه اروپا و ایالات متحده، تحریم‌های اقتصادی عمده‌ای را علیه ایران مجدداً اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71288" target="_blank">📅 17:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71283">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645274372a.mp4?token=fmll6oDN6X2gE5Ftz97t41S5esGVN5bFZWkTFOoT_dXMx06lAGXsD9c8AeiUTmwb_stD0PKtrvK0nKQPRxOGnnfJI_P-5DWZvFCvVlMZFwhJPUZXObyGP1z6Sp30MvnQz_rqbbVttzGVGMB4d7YEarTwW62LIwtXQt6lew85OccmaDad0m4Z580OGhPxHZzRrAGNI5h_nRP4JllbfuVRIRZgHI2Mt5gVK1ZU_cRdisZDEPUzRyqXTH2zjelJiT3FQ5gGCrWQwTtpm8YpmYWKsfn44UCYOemiefZiXY98bPvIONoqZVwkC2RfamSQDmJ03C8nHvXTz4u7p5s5ZqZ90A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645274372a.mp4?token=fmll6oDN6X2gE5Ftz97t41S5esGVN5bFZWkTFOoT_dXMx06lAGXsD9c8AeiUTmwb_stD0PKtrvK0nKQPRxOGnnfJI_P-5DWZvFCvVlMZFwhJPUZXObyGP1z6Sp30MvnQz_rqbbVttzGVGMB4d7YEarTwW62LIwtXQt6lew85OccmaDad0m4Z580OGhPxHZzRrAGNI5h_nRP4JllbfuVRIRZgHI2Mt5gVK1ZU_cRdisZDEPUzRyqXTH2zjelJiT3FQ5gGCrWQwTtpm8YpmYWKsfn44UCYOemiefZiXY98bPvIONoqZVwkC2RfamSQDmJ03C8nHvXTz4u7p5s5ZqZ90A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
نیروهای «شورای رهبری ریاست‌جمهوری» (PLC) تحت حمایت عربستان سعودی به همراه جنگجویان قبایلی، شهر «الیتمه» در استان الجوف را از کنترل حوثی‌ها (انصارالله) بازپس گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71283" target="_blank">📅 16:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71282">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⏺
فارس:
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق ارتش جمهوری اسلامی ایران شناسایی شد و هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71282" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71281">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de453ade.mp4?token=rE4YazDeGUW8R7FsePSxcCLiTwfeoDfL3Uz5OXRiE8EA6baMqc3SHNzBrNN6QXQZKHspKKlXwSB0OHMf5ocImrCuj9H5_z33qz1ZHFbBh00Pi364wqRX70b-5KYMQe8klKUY_5_RcimwVT_es4YGn6Ho785-21CKwqU32TjEJwnUym_6eYLIU0_3VXJlnWDwHT7gGQY5RJ1PcsdT-dGW-JYIFqDPm3wtJDGETesGxwGVPw-_YkI0SmY-3dI7q1KGEjBxTr7--7BQqS313QGaB49ED9AkF707BSKDRUjEnU8aWAE7hmP632iLMrHGSKT6R3IVRUXXBc9KHiwL02KQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de453ade.mp4?token=rE4YazDeGUW8R7FsePSxcCLiTwfeoDfL3Uz5OXRiE8EA6baMqc3SHNzBrNN6QXQZKHspKKlXwSB0OHMf5ocImrCuj9H5_z33qz1ZHFbBh00Pi364wqRX70b-5KYMQe8klKUY_5_RcimwVT_es4YGn6Ho785-21CKwqU32TjEJwnUym_6eYLIU0_3VXJlnWDwHT7gGQY5RJ1PcsdT-dGW-JYIFqDPm3wtJDGETesGxwGVPw-_YkI0SmY-3dI7q1KGEjBxTr7--7BQqS313QGaB49ED9AkF707BSKDRUjEnU8aWAE7hmP632iLMrHGSKT6R3IVRUXXBc9KHiwL02KQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنازه و تابوت ترامپ و نتانیاهو زیر پای طرفداران حکومت برای بار هزارم له شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71281" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71280">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=k4Qvz9mExUm-Po_YvBpIXrRMObhRj01iy7KKuHSy2_22v5bpeomIOPM_xHgVU4bW7_FFqF-YRSLjZuTSmVhuG93KMkILrccOasdFm776979-WRA3QTI3VpH37PMoJyxZA6yQK-EEpDajO9FACKE3drKjOCytf7QvM3hzprkKwvh5WGBNAnKoiwfEYsrNa_yIqC2TUqZcgp1Bn0l5O6YromI7BiNLP51g8TQVy6jIeVwlHy6a09ZnynMDmj93ExBm3MKvWxVdNg2Trw5890IiY8-6w9wZ8JzfN0U9LSKJpy9tX6FdOLp-qzOuEqXD2JocBFD6SQIc1aeqaJ4ChXfKD0_-nFRFc5FM58yevy0943PSxkPJGTyEp52KHiZad4PfiWyKtlLPPSBhcLn5yXYg8K-4gOgIcZyXxIWpP7QK4_3emJoQbizW9tVx63c-5NCG8zZtKQjcdQngwqu9dC_E9zYPY88liroMGG7VF9SZKyWcrmf7gVLzH5XN8OUtgBCn674w9AiMcyoJNZr2VcRzjx6YpnQyhSJOaxCGF-ylTpC6s8UEzBjVnZ8_BHawCrM7pD5mJiWGjYK3ymehDD1iKhpNyygUTrNFkX4yKiZl-zphxGam-V4EZ7KS7ndDhC2VL-QY9mVbR6MHCLf44Qc0voM-R3qX0eBBwcBIOmxhWE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=k4Qvz9mExUm-Po_YvBpIXrRMObhRj01iy7KKuHSy2_22v5bpeomIOPM_xHgVU4bW7_FFqF-YRSLjZuTSmVhuG93KMkILrccOasdFm776979-WRA3QTI3VpH37PMoJyxZA6yQK-EEpDajO9FACKE3drKjOCytf7QvM3hzprkKwvh5WGBNAnKoiwfEYsrNa_yIqC2TUqZcgp1Bn0l5O6YromI7BiNLP51g8TQVy6jIeVwlHy6a09ZnynMDmj93ExBm3MKvWxVdNg2Trw5890IiY8-6w9wZ8JzfN0U9LSKJpy9tX6FdOLp-qzOuEqXD2JocBFD6SQIc1aeqaJ4ChXfKD0_-nFRFc5FM58yevy0943PSxkPJGTyEp52KHiZad4PfiWyKtlLPPSBhcLn5yXYg8K-4gOgIcZyXxIWpP7QK4_3emJoQbizW9tVx63c-5NCG8zZtKQjcdQngwqu9dC_E9zYPY88liroMGG7VF9SZKyWcrmf7gVLzH5XN8OUtgBCn674w9AiMcyoJNZr2VcRzjx6YpnQyhSJOaxCGF-ylTpC6s8UEzBjVnZ8_BHawCrM7pD5mJiWGjYK3ymehDD1iKhpNyygUTrNFkX4yKiZl-zphxGam-V4EZ7KS7ndDhC2VL-QY9mVbR6MHCLf44Qc0voM-R3qX0eBBwcBIOmxhWE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چنتا دختر با کیسه زباله خودشونو شبیه لاکپشت های نینجا میکنن میرن تو خیابون...
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71280" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71279">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=lEgHWMJ3CzWe_A5MWwsHIMwYQsqNU8PkiUWwIxICt9CmTAp9PQTltuAvNtgtdBWQ9IvzR2yohNPtS4AMgqUJV0LO1p52PPGnG3yT_TbUwHaZ5c3e1ZERokEBOxdWZNcXtntiehZTSE_AvebMCHt7bhaGCGuLlOH0-HEq1xvGEY5NSBqgXOEujgFLV4FwliXCDlLTjx9vzaTGF7VF3GiwuCz6dOEWVqGk39pE2pJp5-K3iptsc_PnsgmRlIP1m63BcwS5fXBOp2otkk3Xmqu9tI8KZvjT3Y_7zG0YoYvO-m9GRF8VDwmhFmfr2JSk5TUZuiAwP12r3OIsCOLMFW6jMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=lEgHWMJ3CzWe_A5MWwsHIMwYQsqNU8PkiUWwIxICt9CmTAp9PQTltuAvNtgtdBWQ9IvzR2yohNPtS4AMgqUJV0LO1p52PPGnG3yT_TbUwHaZ5c3e1ZERokEBOxdWZNcXtntiehZTSE_AvebMCHt7bhaGCGuLlOH0-HEq1xvGEY5NSBqgXOEujgFLV4FwliXCDlLTjx9vzaTGF7VF3GiwuCz6dOEWVqGk39pE2pJp5-K3iptsc_PnsgmRlIP1m63BcwS5fXBOp2otkk3Xmqu9tI8KZvjT3Y_7zG0YoYvO-m9GRF8VDwmhFmfr2JSk5TUZuiAwP12r3OIsCOLMFW6jMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
آتش‌سوزی در تاسیسات آرامکو عربستان سعودی در پی حملات حوثی های یمن
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71279" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71278">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=O_bT_rdUsl-2TOp0A2kL_M5YzXKV_NgRVwTVmjphYrmO7PP6ZKuEGwg0OozMW2_SZgEyJBVXKsqMDVWRnGlkHn_fn4WZyXU_uFiGoPc6mYKSch7tXeINRqhXVepfCJVjCYxk-NhkLzOwiGVCQtgF1Nxe8ZpXUd2zpMLOSS_9NwVJ5sm-S91pssmGwQ_YAwn7qmdyLqTG_q0p56WZdUPc-blWFsF6J-bRIjaQoAXAjO6A3yzpz5bht5UajjgSqa2ZHaIs1TmUOIPQyUXSqAv7HY4t7vkNy14q87g-kW8xaiT3HtM3mjqMlSBNq7rIP6lmZTGGWqAO6po1XSvfiw5_8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=O_bT_rdUsl-2TOp0A2kL_M5YzXKV_NgRVwTVmjphYrmO7PP6ZKuEGwg0OozMW2_SZgEyJBVXKsqMDVWRnGlkHn_fn4WZyXU_uFiGoPc6mYKSch7tXeINRqhXVepfCJVjCYxk-NhkLzOwiGVCQtgF1Nxe8ZpXUd2zpMLOSS_9NwVJ5sm-S91pssmGwQ_YAwn7qmdyLqTG_q0p56WZdUPc-blWFsF6J-bRIjaQoAXAjO6A3yzpz5bht5UajjgSqa2ZHaIs1TmUOIPQyUXSqAv7HY4t7vkNy14q87g-kW8xaiT3HtM3mjqMlSBNq7rIP6lmZTGGWqAO6po1XSvfiw5_8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در سمنان برای دومین شب پیاپی میان مردم و دانشجویان عراقی وابسته به حشدالشعبی درگیری شد.
این درگیری روبه‌روی خوابگاه عراقی‌ها در باغ‌فردوس اتفاق افتاد.
ماجرا مربوط به متلک‌پرانی و مزاحمت آنها برای زنان و دختران است که بارها اتفاق افتاده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71278" target="_blank">📅 15:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71277">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U4guxSM89R6y62BI-uZfcnvNX_eBN_ymjHCjOts9qi-g7-j74oqstwGuwReNgnf1qsvZ0MhhgFYYafLqL8KOrP2aKHVkAORWOocYGtLb-DWeM-y95HXnS5e67ija969KOPF6w2OAMNg_GJGvCNJ5NLVmId6wQL8x6r4WhJzYI6mGTxN-9YyaWzYGy_mOGbH7zdXg97Rle5rjVt3cIsgAlE-7-M5NjlN646sS1JUyTYt4IW2ceCB8DVs9GlllOXfRJlHENj5zADuTnToJUR5XGRHXyr5VkISqXVbQInTYyUjN_1RL9MYbfubyOX9XKtx257BSxkCSQ0yJwVs5qQAmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
امروز ۱۷ شهریور، تولد مجتبی خامنه‌ایه و ۵۷ ساله شد.
اگه زنده ای شمع هارو فوت کن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71277" target="_blank">📅 14:33 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
