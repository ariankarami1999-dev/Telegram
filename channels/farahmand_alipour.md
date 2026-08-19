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
<img src="https://cdn4.telesco.pe/file/FRnvbX7Y7jFBh5Q_manEaQFbNcJ2jqVqzNMxsqej9A5EH0zuDFUmfS2-7U26Ptq4A1LLFa3rfUA2Z6h8CINd45ZUoNcM3pQql30D9lBc1Qpxot5MlMMMwu_-t7r4Mawvm28wW0nytAinWM20-zr5Xn1hPxkuJsgTJiZd-OUsb4ZQAclGaqzA9MeIJoLR-nhbMPEoKfc0-PR7zfuqK8KnILeIoBIe5cTZY12-Jd3L0zydbb_pGNG0vL6Cr9dxXKuJROeAY4TuPG_Jz8DNWDxsVuLoRXbkpMKPkxPlQcH4FJKDm7hhbgfaGuCvjdnk5sUzbPeWCVpdpfIqwyYZmaSvJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 15:56:47</div>
<hr>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeleeHglJHuehzqhfmzx_QU1mj6riUtYSarbZAMG1LXaRQh_ARFD9MWZio2VDiy9PREK2o7_Ufu8UK0QA_Ug6MNCyvYcMDWQlXi1NfYJhKAJNAHtlqF8taEU8zeUGt3NxgRZ_CDID9PMh_kNZE5tEUeRWIgiTzKvI3i4em3FMMo0CLLaTyLwjmZjEPymPOHIOAquEkTrNna7d_JjB5roKf3kFVA4S25uREzVLC_LwSZy66xfuuTcDDEbSjQqr6jXQdQt4BWzZYD3TMlM3xgevCjRLRAW3bKG0QXs3pCgDCZdh2_guz6E4HV4zmeCXjknq813hlSZnr2J8nG9eroF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPc4Us0wQsN5OhxN_nWggkIM5M1Nvsf2lm6x7dz_1aRlET5fFBmUQ3ffTBH3Vk27JyJREzCeqTf-CFt2PuN0HbvVRMmNJRxpGQ3i1Cy3B7uzbnaSF0fpWOF_3jLWv2wk2IJd6ST33rf6cnCrKxPUYvT38qaKMQBG9UJQq0a9Js9qNBD3qSgjzY-gR1Udbq1OyMtAlSFGqhNfe1YEl7CltGduuWCPWEOsOk6wHTpNSe_tOob9GKt3T4dlT5HZ-ax08sLbppnfZ0pCzzYD7lX0RgfxbRyrHFw7zxzJQ2rZ2zJt2m2fy9PhncQG083ZErtG3Jp4IqfKykjAIneds6gdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5-QeAbjVfqaw8o5LgIyjAXLC-FwyOJ70JE9L5rXnOWg5gflKZ8zekADG_jR4CK4LOP8YDu6by91ksjZXY4Xifjip_jBtveV9KJtmybXt6Q6G_SSNS4qIIhWdUPShVipKhaIm1PVBxyoxKFcFEl9X5AE3oAH2pZkwbxBSGf5tj5mzrsHVZ0n-Fa-w9xFkdEwS70wtInrVmGu1Oxut7CM3zLRRN1t1NYx17LGeaBemoTpEfmz5L8J2--NvM0CjM2pCRx8BHWE_OLSl8fhyR1xTTN1EOkZqECiNim__esf6jliFMGeXixwqzb_A8j8N3lsBhMX2aeDFGjrVwvT-MbHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtGqgba6BruaRmSJepIvRJRBDNhozFiB1a11Btu4xaqdm6eWBv9GY5hKN_rJgc2XxwFWPogFFXB30uNuoFELzmx6R3qh45NU06-3MGNHvcbSw7a9l4roNgqR_5Ef8DAzg8ScW_KYlzq0H164aKwHP5AxHQLOsDo4IBfJLZhK0_YivhYlvfwAOrG0VsXyrRSNtywEwUjY-hI5VjBnXK0i9So6w_kMkabxRMsAyRR178fooYdYeq87cP1HsI2aoil3jFXZYrWpDWyOYo7DpFcsBbBsDgEYHW9QEvUMWBfG9g8CYZChaD3H2Rbz2Q0kKZkh3WU-uA5dMnvsIME5-GQ9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWERXL2rRj42YX_Gchastqdd1kG9E56WPi_7paSbFhLCBCULI8zBP6uSBe0gsYqOzcpkynkwMUTAQmjYJGbTsYmYY8UBbRf-FzFJxh6TM4MBRXSkEW7qxkWafNGbddA2xmUBvd4WwqBaWf1_AlFnEwaUGGqCBCKbzrBODOSTRIDyRTewiXaSgUHGACGsbiTTAMeRSKH47707Gv9_Xqs7tsOhLeGIcHt2iMs1IzlPih0Kbx-5raUWZv3TormlZokyqyuNGdAlledlsYkIFlnXoNncxcazgYMm5jMA04raPXobO-P_LwVHppHi4fkMSguRTysIItHHXEbXQovWZl8w-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrEWMmpPKG8KUf5AwHOo_70eZ8sfSdOzxjifoXzvGmmV4NwYFKUPG-AnGIjABx6PcjDhyJUVCp_a-WmAh12aIujzi3gpWeLQdR3kAH_ILwgIyoKfWf5dr2tJnONrZfs_C8y60BAK0oKTX3HPuQ6pw-iAXICGFgVzyImYaT1DqxInAXVBP70xfHltvg1KbH5k4QLJXXCxVAfysUZazMxpEvgJ-xP4jiI73jjSSVYfv8Fn_kBXTWeyHYJs92E3PgzRwcEdQk-XE_kiRrgAOS5Q9LlB8trxfUOG5iGzYQQITgobIikPxxl2943hR-vmYHw60M_VPjpcyRUnWO_BxlBoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTa3smGv5aP9_vJ2GqQDm5Ms6iwvSCtVBUeXkkKSV-Lk_TEfvaiaWa3LHyZUr8vQxiP5jFuOmdBgl0I3pZlTuI1Vwvoqwlh7cS5y202vLU9QTS1xy9NXBZ4TJ77uYu3dOdRQCXGQIriY3gswbLlWnsjoyB2QE4QI3ulENEG58fEYwGDiqV_RHvtKr-U_vPSvcdXao8H66ycbWA-1OQl-0k4dEv6Hah7jK4YNjJEPN835GFP9QOmY4vwzyY7iRqvIAmWsElz7Z5-nACMiU6u0mJrTDpakaF65Pe3drFAtX-A8CIBLp911jf6VeK4nuPDBGa1Qv2l6zAcWw0v2iCPlQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHS-fyMoAv3AITT3WpY3hgOjnkHk_wmX20wPykt-S9PB874v5ZKqYYXLL4gmhfXZHbhMQxxtCQHulnU7gdnmoFjBVKLEGohsTnEiQ2MBborOhdQq_0vyOgSCWeoNayqCWxVlRS65wt3QSx-feoWbQIgkCXmeMeUIQQbH7GwMssczA1gAM9J8rxE-TTysnMFVNu-c6VYcOohWESnt7ydcC7oChcPXP9D5tUq7owlJSxO0IbEhnHuXud1OmoIPsyvrE_RCkL-AkeWbkiYEU-ovVzXTcqjxYc9S4bzfxhoz9hrbGmhC1eqdNCF2Pydu_rlnVMbResjipF4rLGxDb8zHzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUZq6NeLqBt8GfP3PyI-u4zo1ky0lHw_TGl7Sa0IMHqCQDB-yV-uq4cZ6M5p73ev47gq7dMKx4mXPFu50Mo1qvuynjYpVw-JkX9Iq1PczxUisNYuiuYGwnxIys2kvBNbV_RkKpHTOm4x04u7I5LEa81CIafFvGmIPS3JXeIgUMwa4qXxLyCk4NDdtmsMjLjj6vwDHxWz_TP2W5-rXciF8RoxCsVKMYyLnl3i_fD7AxU5PHC6PCF_oAx175M0huqhckdqxX0jNGwuUemc7auo8HNdVoQMUIl0okgCKxciZrwfv9GrYRlQT71GeBKmNyoyk9bzQFIVLE6XMRB5_GvBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY3yW0v-Pgks9oDGstGbQPlsJ9eB-iPb1emBmNWvgedDtAo8MzkERO1lgP8UXm-kTEHCDQ4LscafKoxBAF31XA-Sgq45rOWYx-rEPOD4yVZvVq-R9Hwloyyrc2-Qo7y6nC6EpA7LtUq2dXSryYn26on-J59eETatBrJCJ9E9I-4kSabHhMVXJkKOg2lICzEd3K62AlxEB__YKTITq6eWhVPgzIVevJZNsBqqeqESUUF6T3a7-2e9ixcM63cVvHU4YOzfvvTlvoMqxaRRtxOEE7nPXXgJ3iqOrz5yxGehx4McgbIc6qtQAehmxpaVGgtKSVkSVPjBwjdvEGSlA4LF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG988_vDqkJSFgzh23yDgTYGDA-WQ2QDpXJOvDmaDxEDQwOZ_O-w04Bwa8gaDcpYjVukcF5fBn9ccYC7rwcT-LbWh_i_zBcAGHZNWOvvaOwyhnKeHnG8P0QP5wQHRiie3yJDTvKeE4x0HNMztdYqraRif1_Dzbj5raIPzh8z2vuRfsI676-RmH3VorWYSMI0lIP2eOG5p7PqYpVstx96nTafNKP1BbO31hVKtkhbpKJ9VgMqGYBuNtMSSMVbLLjwhQYgWUgAeyiyugboHMdH57fbSSni6D9whvhnyrwYj7EC66ataQDgXr7BESdvWpreFN05gix1_SYbPfCVRNPKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQnuvEqO9_M6NSgPhNn2pGS1r4V7liV6zVWhmWBSBywZiGyPF_K1MD5Fv7W_0MmQHWhJqTssX3NFC_-rguKeEzdgxZn3DCMqC6_-o6G6aMemtWq2n1AiTyBqzmkq1tyvPoqzrrX0t8onXzWZJUqJspF9afz5NoPFPUgxAFzJ-8xqnGu4u62F5jR5DI-X1OV9XptvoK5kVYd9eOOXKGUsmlt3ejtjd62n0trHOBaspQ0w1fVpkqs1F0kVRfzFKRFJHGKVuUZDfjZsBKvYriOG4N4WlwyKNlM_kfEjFiBlrHQM2wiCP6CZOto3HYJg_ou23esVk5fk8I67IiefIjSBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4pBZ94kA2NkKwKlwNNxkHHuYvMqJasnpHUEhA4wqDTo7rRxPdRxEXh1pBOK8JGEAa4IwYgoSHAR4jD6gGZHNxe3GPsz8Flg8R8GDRAn658CL5gNZlYubV5NiV5-kPQrknfpwc43WC2D6Xn24vl6jsfIFkHmVCkWiEBq6JjdXlCLNRmS2Ly72BQ5cPZ7Nap7IVMGwtyEg9xN89R_WfrDQY5Uz7ImIYZIh4upag6hZXgXTg9g3CjG4vZmf1YqRZkulBON9FYphW0f21WaicS6FaofOs513nrVB0Zw-BLEjGUPdwGaDFTr2mQ29n5DJQqTtcAsIi9KdklCfZeFf9C-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY0SgegUIrXJ7wWYUr3oh3FZajoN0CKbNgjrsdU5sR9dwUmBUPQionOi_Ap0RoOksm3Gc_emf4DDplTPWLmXft66pFbytNuBaWM96VxvtjOJo_gdCDw984E8l8666qLQkTnn8d9KIbha3T9pPoPZ620VoUSB40dn_ZbZp1Fj7pxE9T-rSrqC98CiTjaR87CDR_hfPJAVv-tndvRRpjJorhA9srfRSVUm_SQBbO77RbnP3Ak0D1dH24K3uBByZ8CyaRGhN4AOPwqXfUv_62eWgYG0oW4HvUhvjCd3Q_-jScSa_j7R2EJdqHDKvihMj05GdK_XBKCm4MSQII0API0Mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVHtMuLQRyeUvBf0p8_wMNPs02uCaYrukIZ2S3-b64rXrzfEFvK0S8Ij0TpYpRkQkj-pJycOnlKIhUObTnMXC137rQPI2EJFCca4qjdNKPdS7hwH6V01FEgPLw9vBhpZbGOgICip9dkRhPBsrFYUCxv1hZQfNqQgkEO-0xQtd6VEdanwUZfUrUY_EV98pCCPIIIniFrEXAiswRpktPbW5BabSLP08Gb4uJP0NI1JkmQhxwq0UwvWhWCHJRYPwdEMtxDQCFIBAdj50bk3Vx9dUmSVB7Q-micoAscyJmqDbPayNe1UAxkhUM98db-cSVo3g1Qud0NHL4EwcQsKc2HWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FT2KKyX5jbpPPsP5kENhpEzY51O0tfYcEFKspWmYkdT7KJ3102jPxtpd2Rv5djVUvJr3jjBV66vMyHXNNHXsd5TMfKNC9ymHvBWrkWo79AQS4m_6ffMSvwi2HTC6nHWOyg0psHeQUM0ZUm49bkF0GCzfnfnUYFFeQlZcomoo5fei-Jw8MLm2fuGXYkW5omuaOZ5VeTYTLPllT27GNrdI7OJM9fzxUldTUDQnqRaemH3h_6oU4u7RJWz7PWgEki_Ih8tc6YaDngwqwMJ9N8s7_usR0Euj5GrqR6ApRk_2lhTfFlZQAtQ069kkIXjTHATxzfqOZFE8oB4ofAha01Rpgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIH3WQVePWAY-KtJX0_gpiHkMWgUyvtRP3NGPG8l4phD5VEuOlhv1EzBSjXx1lDaTWz4CNcPUEzXOFD9mNCJrTCV9XgrW4D8UwhQWbVQBcS9cZjXz0WxuZ-AHszKvwzAu_3rMO0ViKAK0fntUHpX1Gj90UU00G_W5WcmG__IMr13q5Y5xouBJc4EDepPnyjWic15XzVZpxuqvdGjgTo9ifD1yJEZNGx1JOgj6v9VK1BcOL_dZxxlXMmNWfk_ICoo_eI-2eXJ87fBzxN9T05Y9kib-vyAhieQEcdZUyMglZ9FxNhHWWL-fZxkXKvxZpZFueUKSqXkMQvrzatrnrfA4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1tCVKxpbnlK75vTL2q2sbXBQhyC8XpaXcUSJdWNOXsZEtpw-kT9dBqAePAjcJ-wnebabdJVY8GWZqao7vTBtfQDG_CPyTC9gKTX37byIi3VSeSPQyBDlQe9AsMyJgTACixT2RNHpeZH_nyUB0A9sI7OVLDqvQ73xuklMLGX7AWjL67OiKaLUPNbYT1e9ceSsyuAjyMsJzcbbYdayEHVoryjFLCpSqGsx7kPjT5_M7cDXh7MCi4D-m7xk5MLL3TGy7us9C8TpaEfgOSmighiIpLRys2Rvv-4EpLuSA62M7uCV9a5BC8qpS198P5SBi7W5AUlwf5x_D9J692TH1zhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We3EpHU4GAOe4ekHcgcljHky9aSHv18sK1CPngbaGdt_Wz9d4olec7nkrBERDHacQK5MpaLOF6sqArXFjpcAaHhSzmo4_1Ltq7vBl957COFwmBI0M_N_jecOIAYzmKrAE10hp2IPJh4KvXDAZKcXHL76tq6FpBa7ub9RsNBXq3haxVHsRiZNGbNix132YWZQrJcBSO2a8TesFOUqmFAEtywc7etyTKubF0xUb6vnK6yId6KsRuHA0a_EZ_b3XcbZJE4Aa7hQT7hZ6cqWttSRzC0SAVPqbtTgnfNoMfQzBswUUsI-TBnA_azJO_3PkPVOmajqrzK73gMU1cfI3e-Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhqm7Am1lGNT0qLeqpQTVkw2ScYVVDN6xQ9yuegIeTbjXgJVeHVbwGgtaODg0dzYJiOKW-yVCjSkUZjxMtRKD4VXIkM1DAC3mv_Af5su_81ga9TsuNQDjZYZZvBcXuw9PAA1pIfLwjDauwncjA464Gf-FNl20we-ch9tIWDy9gwCTpa1Lab0ExegBNS8xrUJ4zI-NvvheqwWnFkO-uOYEfyQ_HB_Jy7w06IXchAcqT-rS_H-4-uC5Ku98JyJxaxFIzftK6-eQG932Do3e1rk-lY0iFvRcaNvj1YDZEzsIIIFsEeXV4S9kFF0iKbfeZAb-OhOuwaE9cNAifv9nWwCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkcvHNl1-iT3UOf23uTuiHTA11cL2J91BGRMdAC0a0B6ZfbigKjhzJvUVXhwbOQaiPivsQQLwv0gxH3vi0rWlEIbagXjxz3YGN5l2SykWpLZUYQKVSmLtzi2BWLmsWdwNzBxGsQs5glc6wAj7tw4foHD7zvqUdF8RcyCEwlmy5Nuf4NY8dwwnwXVCjGvPRyBk36wNBUSxwN0MXGUPkxLhzT3a9unhSDcQO8Q5Y1mlwBDrYdbrrGD9Ak9wOX-X2EdlBqgJ1tiyl4zVybHPvuLYjrKtvPChW_QoFSduXhJ295Qru0-uH9lU3hUXCqiDp23WZ5ug-2yqyGx2bT8iTkfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPj9Nrn1hGcCQ2BN-ua5BFjEEqsJ3rP0dFclLm-kLjhwJidpOu7tkBHkuH2O9Gow5NDTIkcnLxd7enw4cpfslgKgfTF4dV7tv5YggdTdhbQVO41g6moHBUSGXjUEg4HFSLf8llQ2pR4hSZFxIxzrb0hT7sdYwhLxBY4MOQ8Gmm66VzqfAMzcmasqgDe3QOWOMuA6DTFPO76njwGKsPKihkCUloRa91__oYSD4rnNPYFLq2v0O-QTq1G8Ii_BOwdLj2gwLPW2SKnKn6levx2ePkmfq3SCd8MOPb-8bC0U1MLPAc41-_hwfFnCdif7fKyVdxCSrxleTa8TviF5G12QUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMF8lV4RggGwgiWHJjewHvfWI9-PE2r9XqHKgqNhyNf69GF9hI3s_mTHEbQL_FeFwGrlPCVHP5NrqJD6nSjd1d5p0CGJukthxS1g3__jOIQ3gBpyGwyHWPT8wBEahd-RmR9mlMyxcO0No3rheq5djvS3YjXeVC3I2YO0b3YBgEcgd8LHjkbHgZ4l8waUI7UCuozIO_LTjNiLFvp7dF0H24_J_bdV5RI4ej2LQETElucLK6787qoXflmY4PjMDoqqi38nd8XN2Tj19ST1uH8dL33jjmoJxkLH_nFuQ-uzGbfm4F1NjvxU1gyFMYDD1ApqDsmkvcki9yVyC9vqgF8J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa7R0ukvkhKS6re4AdRFR7LmLp-APE24pQ0YFHEN9-FHWd0dke21HssCs0GQ0CObWri0N_GdVSQbqi8u88KN3OK-IycWvoToNayjsnM3TH1_yZSvaGO6xCRqKq0vTiic1KDOvzjzHk6LKOpCvFfzxKv5jc3L5URGm1QrnvaStyfP_vMzzg5lYLzNpmgHPMY_JiZowSvZojvh1uYHdZYwVs4PW-zte3ARopyAJXX0HZ1Tf_EKG9Fd8nNWHJHMrxvG7Ragak-kJHMOAYmg-JOEina4vc2YIJXHuYLVqfLiCV0osVqjwQVnel7nRwNlF9ImmzWwQViHrFSYc_dT8ii80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=DZXTSIWMHTBlFob5pVOJq_5cncHrZWZ-VtrkgRjTZDHEBVmEWAGQoQe7hoD6hTuLU-WwonJimojiM2S62hpDEM4jS_zJ4d_J84mJrazsqLeK6XYkcHBF0mopkbf-2RYawMzOjr-jW9N7sgR8kAkg8UbGCzlgm4sSKMa-6YnYUH7WQ5-Ng_exTqbm5le8bwRUBXG_E6TJuySHs8Ki-2PVUi0jIhFEmsNh2nXgO5xffuVyJtj1Js1icIdjDXsJOZ8hPI8U21eMznIovD4_Pz8YiaTotaGMakQsCPOOiCk5Q4SpEG-czWpzRkogxjJEXbejY1pxKuBIFv2-gcgrpbQVIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=DZXTSIWMHTBlFob5pVOJq_5cncHrZWZ-VtrkgRjTZDHEBVmEWAGQoQe7hoD6hTuLU-WwonJimojiM2S62hpDEM4jS_zJ4d_J84mJrazsqLeK6XYkcHBF0mopkbf-2RYawMzOjr-jW9N7sgR8kAkg8UbGCzlgm4sSKMa-6YnYUH7WQ5-Ng_exTqbm5le8bwRUBXG_E6TJuySHs8Ki-2PVUi0jIhFEmsNh2nXgO5xffuVyJtj1Js1icIdjDXsJOZ8hPI8U21eMznIovD4_Pz8YiaTotaGMakQsCPOOiCk5Q4SpEG-czWpzRkogxjJEXbejY1pxKuBIFv2-gcgrpbQVIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuWxjldwN2vQDsjZ_FkGEZJ9RBquZm7XqcImVnLFI2HhQ9t30UmI93jHNtmW7VFUKJf8qdmb9TPPOk5H6v_ltF0M6loZxbYYlpq1TGGtOO1Ilo1JESqeRMtIR45HRLku8aCmD5O_SH2PQo-vVesv7nsN-zIISvHfdC6sQ4mdvBrZdO4oylLv6F9QJfozBKltrgbJLbSs31pdGbuz58xWUK9TtL58PiBVCsEqRqu1gJ3uwH_0Vd1EshvTth6t5Zpqk5bHxQVBl75Qo64PfTmw6XDloq3AUk8N-e741GQN4ADvbPxIIkW2qLClXl0AZXVwP3wgKBLZuH90IuTAg3pl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=nUC72VVXKJepXnBHEQZoXRNlKrfvjqj-E9tcgp4WyYP_1a9y2g3W2qIOY2gaRNEhHAL0iqOCpUS9qY9mBl2agTlMlw_0nWF0w81MXfVqHYK1lICF2_1if40uFs4YfqZ2iDUKxLl9MaAO7NHMZqDBv9YnTXrt6u9wvkTCafRmWwIRpIW8Rdv2WWUTTeSMORvMXpERu5IT4HgsrqWEdjLihiYl_R8ffLh-UltDSMVGtCRiULkSidyG4LRA9xyeG71r119w2qhaP-zdBoh0pRGsebGym7CCX7orOtvVLe2Q_KVbvqKTjJxSHby5fgZt9oadPoKU4qx9d0U_p-00oroeUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=nUC72VVXKJepXnBHEQZoXRNlKrfvjqj-E9tcgp4WyYP_1a9y2g3W2qIOY2gaRNEhHAL0iqOCpUS9qY9mBl2agTlMlw_0nWF0w81MXfVqHYK1lICF2_1if40uFs4YfqZ2iDUKxLl9MaAO7NHMZqDBv9YnTXrt6u9wvkTCafRmWwIRpIW8Rdv2WWUTTeSMORvMXpERu5IT4HgsrqWEdjLihiYl_R8ffLh-UltDSMVGtCRiULkSidyG4LRA9xyeG71r119w2qhaP-zdBoh0pRGsebGym7CCX7orOtvVLe2Q_KVbvqKTjJxSHby5fgZt9oadPoKU4qx9d0U_p-00oroeUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlhhjaU-u7PfsW7-v8Q6P_NB4njaa1GM7ys2WiBYnnQpk7vvMCtd8q_2nX3qqgT3f1LOJhYLKsm_wz7ejWW_Hi7NCMmd1Jz3I8IdacW80qzjAmYiXRKxNubETldMNw2yqRhiNsoIQf6XhVJS7T9QJ8GEz6nOBlI9fnFpI_ab452rGIaKH12_i5x3B_lQNHuiqGl0cJvUC91Xs5IvqWZbH-qmBDg0fdqGqydkcKQy4r2sGlMbXv-_jLkxeEpL1zph9g03Bd2Y6MlQE6tNBXhZaxCLD03yc1ww8XH9GGMv77ZgCqMNU0GTdmI-RFCSvNcBfvSJpheJ0q1_WbT-mVBr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2f9DFsniY-tgnsVlrWnATPt6GNcAduRSl5Ed8UtOLs1tiIL6neAECYVu19cP0wR0oPmi6o9r4bB0DQSTRYMbz1qKn513AG4mINTnoMJpkgRSqh_rqHLUPhKk6UU6xXLsPRXTXkL6WSvM6ezSn7sxbH3361ogqHw7I1-MB5t1bN_S1aqMkAJodrnXbXROET9XXhv_CJJheistMK-5JtnN3sbnf4AvWyiSg7T0zWfOZoVK-zhBoFjWlnKfQHn3X3Qnt5EyD_em3pkSiYS_EcRjS1Q9FWEiT59X85kwSXS7RXU81b4nw2rgU-aHg5JFMd-6CKABGHezbHeMlhaHY9eEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=RFG74MZhz2CvGZDZ7I3_cgWKmnET7d_f9UGKhswJMoUTCSVnYKq9qJ70Oybxo4OP4Rl_t6fKek-Aa0vRPuuUwRORuWQeeOuDMAXAZSfkgCwArpD3Di1AqrxHeWzYpI487-cpQKZPObZ3lHEBzqfuO8VpHCA7mvEqMVA2OOka34t84LsZtgnNXX1IzmH-7HShjmrFq58KJVmBIY22o8rknvsw3FlBYmVvPUFC6Fj6Y2-6JVzZVRla6L8REhNSHuw0RSM546KgsDh2KDwoJKFA-1-0BXKTnQuMHg_BHg3tWqT4aOz13JxUwyzHRcyGFdj_bltzchKC-JKbyRe7eCbEiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=RFG74MZhz2CvGZDZ7I3_cgWKmnET7d_f9UGKhswJMoUTCSVnYKq9qJ70Oybxo4OP4Rl_t6fKek-Aa0vRPuuUwRORuWQeeOuDMAXAZSfkgCwArpD3Di1AqrxHeWzYpI487-cpQKZPObZ3lHEBzqfuO8VpHCA7mvEqMVA2OOka34t84LsZtgnNXX1IzmH-7HShjmrFq58KJVmBIY22o8rknvsw3FlBYmVvPUFC6Fj6Y2-6JVzZVRla6L8REhNSHuw0RSM546KgsDh2KDwoJKFA-1-0BXKTnQuMHg_BHg3tWqT4aOz13JxUwyzHRcyGFdj_bltzchKC-JKbyRe7eCbEiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8Qf1PsVYJJGoCiHpUHHSkuVsgYorM4Tb162msxF-CzzX2kABzhoRxLTby-BWrNehOtmkGpiZabpO992CJswecgxgPO1t-77ORVjQUla2p6ef6PrTJPcLNtfPTB-rRmRn1hQaKJpaBHnHqDm-H_AFAH6q6P9NeIUC7GkuaQ41ZkOp2j8IJEAF1hhvSUh7X2ZKqH0cmWpl_q3PocUIO9-vkZQJrmzzk1nT5bv7zStMJVPwqfxRXeKzJoz6FR-kGw7MqnXZsQ7LxSRPC5VdlCT0aqCdffd744UCEGeRojK4-SoZAc11QuvfcCoBZcANNKytG_Ii0a4tS-YaXLXm6EJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjAzoawrSEGEJl3cN8yh2YQEU9_FVOQ1f72Lv4n7XXUj32GoDNoSyI7cF0iGOH3Lau8i4VAzCUK6FG1S-vRXHDJIArahRFdn8iEuJ29h-qNULCY09mY6SuqI61wnXUKizWJzUfMj6wT4WpmMaR56FH5tFEo11obY8NQwCOdzipDGt7YZoPlq3MLExGWGZR-NwTXDc0x5GFbPbskYT92wKKeOLKU5UYjJKtpdkHWUCnUb9Whvt-8JcsGQSP0ewp5KJXk5QXMeK-gDk4pgI-lO9lQadBJemP-G0Zl8Corw145l1tUZ9hWXEx0E9IpEy6VRitW8Rq3VYxR0vs0jKXJgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXMxBV9Y25BmYTHNGsK896dtP0fNJzzA5UBX75LkQ2hGMbvEoHeszdjAPrqRuaOiiB1CR3XpeRZJOEmyd87N_3p7LlBnMpOtpr41xULHrxiKa-b8naTfkV_1ZM8yRdv87PFJOsq6Dv5gIntjKqdSzqOaTGnVotC9JN6G6BtwLKStStKp4_D65IGvbcn-SdvlqXVhgB9jcWeQ63YBIIJFn4XTKzYrKYFWVxLAQZ2Q_-e3BQp2NhjwKhV4d2oBG_YESpzuNn3BIS6bKHFKanJxcUD0BR8cRSYzIpq8kJ2AvjrrrmKZUaxcu2TPGksOlV4J4rWlmUYNkGW5QsPVB0JLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=ptIFf2sKzLxyg_taVWLIPK0VjVrBQhfUwTSuo4_c0o9FY9zEOOceYxTUQPLyWYFZDRqpx4VOEC7gX7FieLyF-j0YhulYd5ecNzsFsVE7uYvGq8Rth3z-JUpU1vrDoUgerRsw-59DCrAcTp1XfFuiZkbfjVIzefe6HTDS8HjfmgDIaqsMqkyTuckGV-bSnZv-wg8cVknMScprpXDuwlJIXwWWlrrpLf9u5KSzON46_ijrp7_OxBocUAxlw2IY5fwOoyexwHhtvFelgyjpQ-wytbhiJhjePL5k0klP0qzZIK48XwI9Nz7qE2Ud2tIpXhMOcIsHb20G6tyopOpCyxOSMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=ptIFf2sKzLxyg_taVWLIPK0VjVrBQhfUwTSuo4_c0o9FY9zEOOceYxTUQPLyWYFZDRqpx4VOEC7gX7FieLyF-j0YhulYd5ecNzsFsVE7uYvGq8Rth3z-JUpU1vrDoUgerRsw-59DCrAcTp1XfFuiZkbfjVIzefe6HTDS8HjfmgDIaqsMqkyTuckGV-bSnZv-wg8cVknMScprpXDuwlJIXwWWlrrpLf9u5KSzON46_ijrp7_OxBocUAxlw2IY5fwOoyexwHhtvFelgyjpQ-wytbhiJhjePL5k0klP0qzZIK48XwI9Nz7qE2Ud2tIpXhMOcIsHb20G6tyopOpCyxOSMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=slfbCTrKY47Jbms-z1LlI0ErH6QSgPSFTscL6YY1IiAO-F1nP8Z85E4Oh-QOCMGLBbGkN75SZHq6rgMfSvPvu8UjabIIWNScBEEAhnJedy8Sbw5xJbEwyEspjJzvrdoylYqF2wrmM1_dA5OqB8kgsycvXX8jy3tvk12os3fGxNN2xshiMtrTppeaB_1qbJqrtc5xAm7sIwprQXfvf6smWT1NtT8zmPcJ8hV4h1ucPKpQm4Hr9gAOpxIIS_PdRjeEw1d_9lrkbeiNmPmtRy6p7cSr1l9rKgc-YWFf8FblXIKO-DvgiVdzs_TsD5bXiTpUzUJGQTg0sE1Kz3Y8Thh3hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=slfbCTrKY47Jbms-z1LlI0ErH6QSgPSFTscL6YY1IiAO-F1nP8Z85E4Oh-QOCMGLBbGkN75SZHq6rgMfSvPvu8UjabIIWNScBEEAhnJedy8Sbw5xJbEwyEspjJzvrdoylYqF2wrmM1_dA5OqB8kgsycvXX8jy3tvk12os3fGxNN2xshiMtrTppeaB_1qbJqrtc5xAm7sIwprQXfvf6smWT1NtT8zmPcJ8hV4h1ucPKpQm4Hr9gAOpxIIS_PdRjeEw1d_9lrkbeiNmPmtRy6p7cSr1l9rKgc-YWFf8FblXIKO-DvgiVdzs_TsD5bXiTpUzUJGQTg0sE1Kz3Y8Thh3hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOZsCUSsvRFPoDuwV9u9cd8pIGxrtxyFeZnh2CNb_2snDVk8dCXmuSrmEuidRIZnZ13BI5tLZl9nNeMDtYqxZARGAiXpbxKb7AgLBC3ahFNdmpFzKe4da1jqrH6EGP2btTWWoOGp2udP2B9YtyPk1GTYyIwf-bY9_8Y9QA_bNq8qSDBMMFHgmF6h-75HBY9esoZsSoF0YwqceqcmjI1WbH6HoV1BBITw5uEReSOohXCyESlWrG9wXsKM48n41bMP2x9RLl2MGggmDc0NJDAL5LuK2ZgsDx_mgYuByWyZT9zOIviA9Goq48v_8rg-2q2ZGybKwweAhctjDa13B_Fn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3xfMzpopt13cXuuH0VX5fHlOP6UPzWTMB63FguoR_z9G0fBsxGOFI1WwBOmx6HDXIQf-QRZiyob5nL95sCvPeW72HFhOI5SINW6fud8aAOcpKv0EQgSijfzNKSL6vcfIvcv4E8TL25gn_sNA8yLHIlO7zLXDBofL0uixd6VbUScGmacABPpGfLsWc1cpg8l23qeYPybt8mXJCrk8Vc47j_78MD06hqxK-3_g295FTGyW4nmRkWMHUz516Czb9C1rQ07d7FrlAhiurfGCDPUVSklgNeI5NcwDuaZBw2yTqAnVp-2OFhtmmGWtxbcV3mIyxP61qwkRaZKZJxq0YCiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnSlC5HkG0mw6iy7FlAfcTM78xbta4wCW_ZFbzT0PT1_GT_ohwgT1m1VQsejaKNjIZCEOo_LBIRt2eE9VdIo3n2OmPzfm93yo2NxxhDunXFq26j9DAQQ_Wvfyq_i9K-fiWixTXcLhgsG6xVnlo6pwZG24qhHa1agLGMX-Ot-yRmdlNuE-SNhieSTTDGDcOGaOU6hA3eMNbOLy7nglovKss1XePDIan8qAqfm-P95_Sz9foT_hG9EzMKYRfRJDUR6SjiBK_hoPU9oBHHPmVvf2DnILdLCxOEq0lM-tU7ifN8hmNIsnEiE_4ZjZLVRXqGwIItzG01wilP3Z8kwjLZ37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8BlUI2xbLKi9zxyoKUmhjB_nikGamjh84AF8Jg0YmF5Yyvf1oLznApi_Qi9CwJrnwb7yfI2VNqA7010LhAAXGoZKrkJdp5_GVZ8OUleLEERTH5c06045cUeqrgup0vwXkJysByIqfR2mW27IlPypP1k-MHe9NhUxFwvKdADv5Odmx0mkpOKUelNRhNxL4ZGLcXj9uq7AwmYa7d2hoxfvQINwqmDnrCWIpaM6puTGBeR1PMna6Ks-fBNf8qILaiArj_Wf0YYWMR5KLkuzb8iBIDhoildAfWtyAWtJapOCCkxb5M_JlAecjaujpIJmLsJXAAnGy4WjlaNhYAY6Rou3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hbl6UCfnNN7l8tosSWmZJsbaQckXLU89imzdw9R31HV1wRXdPzGI_TBxk9PdEPVInjeg2tIx7WxAh0kX_O0LE44zSBktVnkP-hT8el6glAO6Cw5Bp6NEpMbVoKyhG1WNy-YWMCkG-sHn9fnfMhSyL5ABxSkinVmHl24WlNRFR9gTd3sEWW8mXPz_fGD4K4VEfKuE_l9FMLbl9sqidZgVW6FrrqvbTh2zoXyfKOxGZRS1rfOSbnNNkNGKI7SWO1qhL6bKDzAkXWYGzcs1eUvepPwvpxMZof5Yj8lJtcAHsEA0W-4QLFeFAXDAMUsVomhJXPXGEBn3o-c6VkcEh8_SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFThwjSueGpfXao9_oIRu4bBv09wDim5kACn_r91kYmreCTezgBKJe6mI6M9-nQT-iIZBWjP0iojGhNyCx_m4BnQjImllL7vfXFyUgwE2AKcUCrV_YttZCuPoyOYrMcvVzxrWBxiLC8lP9nzDh6qb3wRYz6l5p4978xzA57QxxaCX39pCmVUMKhzG822B8vJoUQV3SZox5V59ILMxfyKh-BWftb-lwF6ees6kWrgPNLIDesEdgcTj3IRlixm-I1z-9Mzs4x3dUk4lLJGmjV-C3mDaBspZNRJJLcvhhz-XmE7dHfRLo9xG7fuslMlFS04nswKs67qiBvj5Gm3YuUbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exutxbYYGiLu9DeyAsVGFcT2GNUYEwn_nNgLhf4FtHa75EMyIQLElI3UKE844snJcdFpmT3cA4s0A0tjJo1L7YVuCij1K7sAIHnMbkdXz-_ybE9aLtS9_2r3_vLZ965mMZ5U-94ayfAuqnHQQDzrzmBIZDITY3MpU4c4OSWiupe8mrOkuB2a5mnRl3KIPvgOovePmZ6PkSBDXYqJxdzALm2zhKno5jcddU85yF9B8F6SkqW3oeL13vMYsLnB47JAvKY9RahWMZD4tHIDxHhSoPBiNy8yBVRPIB2oPUNCl9LYnhRfQEsRCkc8_wtLalwyBrFb4u05l2AciEWmn1GDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=wCJ-zPeHa46LYD37t1rwmdFuw8b8TZBy3e27yePR4GPUxAQw13RiRdd7wOx8grqDOMiztsDk4bGN7THNxUsGAuHAuolTVxPloMIZ37haI9kbTN1h_Ys__PleTUItmZ_GU8uvmC-Y_Ov8W2yjftiivwhvHCXo9SZd8ADMGkg6ys0AALLnNhlYaDg3uuslLgMHWWnRjhFBJjsylNO5c9Rytjt6RBRl1sDzk07L2iWC5Chx8B6Z0VwJKEjUZMFmhdxWwnk-m7sBwb2k4h0ok9xZv07SXJKmP9G1CijKz_1RVC65UR7I0X7Sxk9EClQwqvwiyvqLv7KXF7It24UYZK0igQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=wCJ-zPeHa46LYD37t1rwmdFuw8b8TZBy3e27yePR4GPUxAQw13RiRdd7wOx8grqDOMiztsDk4bGN7THNxUsGAuHAuolTVxPloMIZ37haI9kbTN1h_Ys__PleTUItmZ_GU8uvmC-Y_Ov8W2yjftiivwhvHCXo9SZd8ADMGkg6ys0AALLnNhlYaDg3uuslLgMHWWnRjhFBJjsylNO5c9Rytjt6RBRl1sDzk07L2iWC5Chx8B6Z0VwJKEjUZMFmhdxWwnk-m7sBwb2k4h0ok9xZv07SXJKmP9G1CijKz_1RVC65UR7I0X7Sxk9EClQwqvwiyvqLv7KXF7It24UYZK0igQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=Hs8yBwbRQzZbf46tx2d4DZyMaB_wxVDI7ByVt-OoH2dTOZ-C0vEb1p3tqPCLQ3ASXb-wLOX2JPVsJBkockUQX8ZbTBKlZZ5jQZco5WWFdjIk_hWNa7zgANfn7aQJdz6jZMdZcgXgDq0yuG5eL1FdUw7iIRsH6LlFtF9EznS_n4wiZa6sJ-W-OwJan1NQwmmlDk8UEq8S8ytDiDblMUAMRung2IzUtXJ-KcTj0OwVDsGRJJfsodjp59Ifdg4_1QEB6K8UBmNSMWfxtrCe685OXbOiqRZto4nwXtwjWIgUW8M5AfHoayuxLFCcjECJkeodZlMacXXhtGoF_RS_EsQo4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=Hs8yBwbRQzZbf46tx2d4DZyMaB_wxVDI7ByVt-OoH2dTOZ-C0vEb1p3tqPCLQ3ASXb-wLOX2JPVsJBkockUQX8ZbTBKlZZ5jQZco5WWFdjIk_hWNa7zgANfn7aQJdz6jZMdZcgXgDq0yuG5eL1FdUw7iIRsH6LlFtF9EznS_n4wiZa6sJ-W-OwJan1NQwmmlDk8UEq8S8ytDiDblMUAMRung2IzUtXJ-KcTj0OwVDsGRJJfsodjp59Ifdg4_1QEB6K8UBmNSMWfxtrCe685OXbOiqRZto4nwXtwjWIgUW8M5AfHoayuxLFCcjECJkeodZlMacXXhtGoF_RS_EsQo4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=oyQYt9KWqxelg1TrixIV2YRv9PNu2DichtOt5q3csZ0Gkq140Nf6q6VfOl7XXCx5yEisMSnRnl_BejVX_UFjXGROWqPRHATvk6H3HhE8bmgLBwIoD5zTjvUhkV6rdW3pyA5en93m3ZEDrU_vyKM8d6bpY2etW1qCBFMHllWsD0jMJ8GAjoZ5BW7EE-Vz6RlkH4JyfrZG13k_Bsarm9Muwo4N6DRhzNDlIIWfqL5sdVuVoU6UBG5JBHzzsU-q5amlvZbyYS_PLJU_mSKDWSluTCDjLbpwiuzR3zEZpmrRXbdYBZxYpVLi9qX7KqGr3HvqOeFbDk-u1H55YxDAzurokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=oyQYt9KWqxelg1TrixIV2YRv9PNu2DichtOt5q3csZ0Gkq140Nf6q6VfOl7XXCx5yEisMSnRnl_BejVX_UFjXGROWqPRHATvk6H3HhE8bmgLBwIoD5zTjvUhkV6rdW3pyA5en93m3ZEDrU_vyKM8d6bpY2etW1qCBFMHllWsD0jMJ8GAjoZ5BW7EE-Vz6RlkH4JyfrZG13k_Bsarm9Muwo4N6DRhzNDlIIWfqL5sdVuVoU6UBG5JBHzzsU-q5amlvZbyYS_PLJU_mSKDWSluTCDjLbpwiuzR3zEZpmrRXbdYBZxYpVLi9qX7KqGr3HvqOeFbDk-u1H55YxDAzurokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=KDQWnJu7rLu9FJGT2Lh72Fg2CpkPagheqfiTGydD6i2L79rcX_M1-cnx3s3NxoB22m0MsL6FCKmwczb8CuqdzLSjy36T3PjJ9SOM8Qq0KJkvkTMNp3r34L8t7EAqKQ4WlHO70mD7ORyZ8a42hl-5cxBfyiZwH3W_ekua4U54-5HK9oe0S4u2JubNLkGihJ-zZuBAi3C__1URVNuHJQ_Ay8jP8WYbDTVw6Zz7RrfMKdViPVtXSmUdrSHKqvwa9YSS65m07674o1ot3a4NKUB-MW7ca9DfokPHAAiS3mTQVJem8LLQKhwwVChCG_dwLVsfci3C1WxSCsgmXF7e_g0eTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=KDQWnJu7rLu9FJGT2Lh72Fg2CpkPagheqfiTGydD6i2L79rcX_M1-cnx3s3NxoB22m0MsL6FCKmwczb8CuqdzLSjy36T3PjJ9SOM8Qq0KJkvkTMNp3r34L8t7EAqKQ4WlHO70mD7ORyZ8a42hl-5cxBfyiZwH3W_ekua4U54-5HK9oe0S4u2JubNLkGihJ-zZuBAi3C__1URVNuHJQ_Ay8jP8WYbDTVw6Zz7RrfMKdViPVtXSmUdrSHKqvwa9YSS65m07674o1ot3a4NKUB-MW7ca9DfokPHAAiS3mTQVJem8LLQKhwwVChCG_dwLVsfci3C1WxSCsgmXF7e_g0eTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=BRphRYOnsYp5ajtEaS2DHBE_QlmepLOq3_jwvaN-81eUqx2_obhEMOShA8-DD00UnlXw--Rck4cIt4dIHrbFgGtx_XYzjADF7qa3kBcwcRzieWHk1-xuetjPw7a97qo8IwNVQ1Roi4KcNSR6XwbNPqUnwSkwUUrZ19cefMa3WvYrqFaKS9rNg59g8V4JNqvwYFs99F9ZoGQv7Wo8K_deKAdLE-4FuY0rpTE2Wv3VaCIdlZlggK7mKwGA13jorgMuxeKqhDGRBeamVSBf-nr-4oirQmJJpHGru_XfNtoTcmovJSLBtbU4oyag_U6_zTtUZH1zqfQKtmr-Y4XLX2RJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=BRphRYOnsYp5ajtEaS2DHBE_QlmepLOq3_jwvaN-81eUqx2_obhEMOShA8-DD00UnlXw--Rck4cIt4dIHrbFgGtx_XYzjADF7qa3kBcwcRzieWHk1-xuetjPw7a97qo8IwNVQ1Roi4KcNSR6XwbNPqUnwSkwUUrZ19cefMa3WvYrqFaKS9rNg59g8V4JNqvwYFs99F9ZoGQv7Wo8K_deKAdLE-4FuY0rpTE2Wv3VaCIdlZlggK7mKwGA13jorgMuxeKqhDGRBeamVSBf-nr-4oirQmJJpHGru_XfNtoTcmovJSLBtbU4oyag_U6_zTtUZH1zqfQKtmr-Y4XLX2RJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=BQ-dUyOG4AS4DtsA13y89wbGHueGpSqIG3qAdHA6Zajfb8ms6Bg0mcJbhBd4D-3Ezq4KKzxbnYGsdd5fhWQspX4qeiWcVT_O2gDjEACGIExtDco4bz5EpUvAOszD1evBwdUDb94QH9CTeL2bFaf2A_OKLPcdTXWOgpE8xXGmLh5LE_MsHdi0w0zUCuePLy45nQ960zORnrgHwtdRapEM1rH5QB4dNElOs8IJt70ucyAK_u6NWQE_6RoZ4zhLBpr-7YDiHzlW7qeo6IaUR1_O1_GG78lo61Hr1CuW5C8ASGSceyyqsQMgw1fsavQBYMmuHM7HEs8UsJRVOlkN9HAS3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=BQ-dUyOG4AS4DtsA13y89wbGHueGpSqIG3qAdHA6Zajfb8ms6Bg0mcJbhBd4D-3Ezq4KKzxbnYGsdd5fhWQspX4qeiWcVT_O2gDjEACGIExtDco4bz5EpUvAOszD1evBwdUDb94QH9CTeL2bFaf2A_OKLPcdTXWOgpE8xXGmLh5LE_MsHdi0w0zUCuePLy45nQ960zORnrgHwtdRapEM1rH5QB4dNElOs8IJt70ucyAK_u6NWQE_6RoZ4zhLBpr-7YDiHzlW7qeo6IaUR1_O1_GG78lo61Hr1CuW5C8ASGSceyyqsQMgw1fsavQBYMmuHM7HEs8UsJRVOlkN9HAS3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=L_WPSCqTnz86-T81Um2hXn48oyhSMz0szfgBwetzBy3IY66UV4NQLPg7zUDo-sl231GslF-9WohozqAMDsB8XYr4kj0lKAyhxQDgyiMWt8KXoFdqWd3Qr0JbuPNJrW1_fy_1Qp4Scm_MCrhLVWtoNuHR1Ng9u8PacD2FFUIKXaV0VfWG6vx9wns0kV-inkYstvheVDR79fEEVX8nz2MfcSJj0gZj1K7f0Rdw_fMcnytSE-W0ubN4UYm7AjI6Jdx42B1idn1cp2WG3VT_SEripWu1WQkKMr9RX5CgepwQ8vf24js8Ysd0evjsGy2CeIf7QjGvsvhfFtou6-IlyYtMrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=L_WPSCqTnz86-T81Um2hXn48oyhSMz0szfgBwetzBy3IY66UV4NQLPg7zUDo-sl231GslF-9WohozqAMDsB8XYr4kj0lKAyhxQDgyiMWt8KXoFdqWd3Qr0JbuPNJrW1_fy_1Qp4Scm_MCrhLVWtoNuHR1Ng9u8PacD2FFUIKXaV0VfWG6vx9wns0kV-inkYstvheVDR79fEEVX8nz2MfcSJj0gZj1K7f0Rdw_fMcnytSE-W0ubN4UYm7AjI6Jdx42B1idn1cp2WG3VT_SEripWu1WQkKMr9RX5CgepwQ8vf24js8Ysd0evjsGy2CeIf7QjGvsvhfFtou6-IlyYtMrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-6n17tDkmhhX22OMpfPApb7XyRmyJl7E1wCQcXqTEI3e1tw3S-sLLU9kGzL0uXRc4xnQe1QYZhI_xf37v-jXYneHkIPUDKbxESqbYCdBonZVQ5qyUYAuieNW1wThxZJ19RKwmPdDS4xE9SkNngTXHbnGCwzlXA9rl9g_9S7-7DZQLw4Z_44mx2jJuWU8-bCH7dcholPa2e8PBviERvzjMpuB7cB9iqKlFF9RV_lmELbvorU732oxcTzowusmuUTFHEAkn7gyq6ZiEo2JI-bDeurjE4WBUIOIhALwmwLKgIqYc3t9ixJLk9HIYRIzbfmxzsSc7bd-U0mP2dKpgA51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=B7djouq-QjA87mTZAsZZQVc4Xl58zMupGghZNOw9kifyvkg3TTOotNLb3yEEgrunYjADePDCAn-UofkfkqP0iPP-p0sg2C6blAk8SXPHIf4hEceam6CWWljSei_Li43TKB-DEZohPtQP36jGPZNXCJR_nh4MyafyVliyrJvt9jnoTnFFpVQgCiIXuFmT9tvng1EKvuw2inXZrD3jUFWwhTe0h0yQjRX20KfEw74qoUo9oVCCgR3f91bLAkmLOP0xcDqD6qRWXucnOr7ovX0nw_j5X2nZffI-KRbzmn3qTs7mY-FZSEyXYmgAP9vqSEruVW2TU4wWoQXmzlwUUi78WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=B7djouq-QjA87mTZAsZZQVc4Xl58zMupGghZNOw9kifyvkg3TTOotNLb3yEEgrunYjADePDCAn-UofkfkqP0iPP-p0sg2C6blAk8SXPHIf4hEceam6CWWljSei_Li43TKB-DEZohPtQP36jGPZNXCJR_nh4MyafyVliyrJvt9jnoTnFFpVQgCiIXuFmT9tvng1EKvuw2inXZrD3jUFWwhTe0h0yQjRX20KfEw74qoUo9oVCCgR3f91bLAkmLOP0xcDqD6qRWXucnOr7ovX0nw_j5X2nZffI-KRbzmn3qTs7mY-FZSEyXYmgAP9vqSEruVW2TU4wWoQXmzlwUUi78WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOzFKnHVNYcdX3q7oJIHDWerxOJSGDg3HgENnlLuZD65tvpR2k4OiSuBZtKqPx3hTawB0BBZ6huf4n_Gigwx1CmCOmA0UnW4RaQt0CWkaYlh_V_kueaY5ql4S2OIx887oqNl3rcUVZS3uFxS50YcmhMDblonazRmTn9oyLPuULNAZ4yfj_-y6zddwu1VXII10kc0LdlCIvmzYZCw5XN7LeBtT2cezE9XNytj6gvoQtNceTFjw-GOdFgkmnLhSn_yncv8ZvLVdc1vCsXLVhd0V15ptW-gs1Zh6Y30e7DVhXydQ9U1UisKvh074t2OZ275STPn1CpAb8rmNhQmPoUaMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7kxRqsRnfC7vQBuZsmsGYsNF14RiCSAhM2oPZBQ4oKx6Gb-R-I57msr83UOTe-2Phu5ezZO6DE1fSq6ewKcmLOEkwHqUrlT2SUWsuT8QxPhBzASFOjciyjNveOMKltaHpwcL1nYgmm_tnH9DmBlFdj2X1wpYvBo87MuVvSNznmSdUqg0ASW4ya-3-qshlgw_0pBYPQrL1g08jg5T0QB-qfKMF8ku52XK_LC3xa70NIcNhJsMo0LWabGvBkzBWjR5P39Jy4Nhpc5f7VkTvwbsd3Bp2741YeiHHVAPlWZTVchjILuSvWi2-PAibDTqn_gTc_PfEcPH_4d5bl_yqrBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMsuG4cxAd7jgY89FXbCSGWpEsJYjIlQzUtMW1gYeW1_eLrPCGzyoAfn7C2mxdIz3UsyanPdSna4GY_cATraqj8XCFyuKsk4epiia4hXjYa9avKHEsS-BH-6kfI-ptv2qatMSSayl3Lx2XfI051d3Y42oDCidCsSNCS_fEIAAhjvLnsmhHR83emwZnUX6smwsTlnnp7rrJeZh3KLVG44MECwCvtgULRQQMrBIN7gmqZYabuyI_iTAJfkhOpmdSSXbA5NT95sV_FEjmxnQRsvcpDJMtqKL_g-pY2kXF1FP4upadlzPOTQBfxSLsGqiKwa3Y_3Y3GLnRTXDtYKNB1BpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k06oR4RqWoEken-wasSM1Tm6dzTd8lxds7YaY6tgRKEfiqSEr8XNNE1wP2t7vBvzkD8p6qD3Y4vNfjS9JfE4ZrlhOp6jWGfQJJx6I9pgNYrVpPv7wlkt6NYUDX7JKhpuEyOK20_xXLddYjIGYM2IWE2PCYitQm3Dotax4vOGvKV6bLfH5MqRXOt7-tWn3dkMmeGfFJ3TgRJ3wB_8R9kg2EM_IiLAyG-IUg67meWclhXAdY6yZY02E9EmyzjSBZXV5kRXNTX9G5PSwrqtFyyBc0GIcoINMQhAPf5X21xxIXoh0xACUYt70C9pvvaJyqaZq5MSOi-ZyEyEERiCIU0s5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=i3bAgwsr5jH8yGsr5-AhmZmfd1eTPN_lf_3il8-khKXQniA76r27Vn2KsqnRKENyC_6-ocVYk4L6YW5hMds0sHlIlog5_wWudm1yuYvJrPThcJd08Aj3vz6TJJpRHKOWxvMvl0CxEzjp1_scQ9jlWSrbWwG1VosP8g6NLAZxnTq6yFZziMixiEN7yCaWm-707ivX9DgA20p7vA34iFJMZfIEumzdyMCWqHqckT5IbLIMDLKj5b0ivj2k0YxfDcZLSiaKvuPQaitSrNZUNYLzt7OWmOohCKidvj9AM1NYp1bc4kdVhjh3orfigp9htApa7CM16Ian4XqmyAFVx47qFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=i3bAgwsr5jH8yGsr5-AhmZmfd1eTPN_lf_3il8-khKXQniA76r27Vn2KsqnRKENyC_6-ocVYk4L6YW5hMds0sHlIlog5_wWudm1yuYvJrPThcJd08Aj3vz6TJJpRHKOWxvMvl0CxEzjp1_scQ9jlWSrbWwG1VosP8g6NLAZxnTq6yFZziMixiEN7yCaWm-707ivX9DgA20p7vA34iFJMZfIEumzdyMCWqHqckT5IbLIMDLKj5b0ivj2k0YxfDcZLSiaKvuPQaitSrNZUNYLzt7OWmOohCKidvj9AM1NYp1bc4kdVhjh3orfigp9htApa7CM16Ian4XqmyAFVx47qFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOuXhHbq_tR_j9lf-VvDYVUA10Z4s_AVQ0-lHUlA4PfFRk3m8FKKU9GagdUi36e6kr3VtqtPHhl7Z-kwh-YrcJLUEYXMDcSihrY6FeRVWnt7OVErjuRhsKHvjI2uwq-Y5n_-jPvBkru6ioaszvi1PJH29CtnHWm_ynfZWwiN5hS4CUGcWzDg8ZJRDO9dphRVzGAPOSREcjTkWqJQqjhpsNmT7U6x4-8mAtPRpLT-Fk2W_7sIVhEMBVgdcDDobgOAmp6o-_DuYMwG-rU9-cXRSOt5vP88TPAoC268gP2Fmu1bP4bfVMeuEx5vxjcVu6z3FsQEHlUoqhe02-zBHr1P1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Rj_ZHNWTS_UCC_E0xCS-kBZTLn9gPgCbw_b8nFvGepRmZHvXimeEa18GpuXHW-er7JV7uq3GcecoLXnTB_KjLb0mfNVEhg9XAVRqGumvnlfXVpTjkiftmBE9VlWBXqlbutmsPkDveuAN7l9wk1sZrv51Fg46341eX5kUrbCUf2J8adu5GSlXVm2oKkFs4tTLnk4EI2Yv5DPx8RQnhNdI3mM2PcKblx7rtz4YWi8zM2suUsfvoOxM589nrE7serw_j7fV7NLJfi0ehyHiQbYE4c8japK15UgUd1h9uaO3pAx1-TuUKM86xwFFDnVAS2EsOlfS919l45JdTAWdDq6rXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Rj_ZHNWTS_UCC_E0xCS-kBZTLn9gPgCbw_b8nFvGepRmZHvXimeEa18GpuXHW-er7JV7uq3GcecoLXnTB_KjLb0mfNVEhg9XAVRqGumvnlfXVpTjkiftmBE9VlWBXqlbutmsPkDveuAN7l9wk1sZrv51Fg46341eX5kUrbCUf2J8adu5GSlXVm2oKkFs4tTLnk4EI2Yv5DPx8RQnhNdI3mM2PcKblx7rtz4YWi8zM2suUsfvoOxM589nrE7serw_j7fV7NLJfi0ehyHiQbYE4c8japK15UgUd1h9uaO3pAx1-TuUKM86xwFFDnVAS2EsOlfS919l45JdTAWdDq6rXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=r-9ZRve3lve1HaS5LPOMtlXlE-lZQqgyE1oAaxkWhZh47tSXhit7fICJ4o2yfompdsEWyICD2khWdLj0q2E5ag_6m7vHxyogty6P16lmXIlbTuRhv2xcziuaQaIeajtE9_queXmjlhw0P0HCRwLHlZAHsVsH1zzqlp8h1irNfcn58K20T-_rTkcrYQNHtXCF1bWLFd-JQqeUSTHh2E9BSBndtUxO5AajoDBhtfGVKurrGN5u3Db8-SVCM-2OkycVvBoEhVCs7-MmSL-DrMe_wQmi_4HU9x1EepsqHp2WQ5SSHnV2iPy4r7_kpfsy8gKKQ5Ab20n-nL8abiDgS6-QTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=r-9ZRve3lve1HaS5LPOMtlXlE-lZQqgyE1oAaxkWhZh47tSXhit7fICJ4o2yfompdsEWyICD2khWdLj0q2E5ag_6m7vHxyogty6P16lmXIlbTuRhv2xcziuaQaIeajtE9_queXmjlhw0P0HCRwLHlZAHsVsH1zzqlp8h1irNfcn58K20T-_rTkcrYQNHtXCF1bWLFd-JQqeUSTHh2E9BSBndtUxO5AajoDBhtfGVKurrGN5u3Db8-SVCM-2OkycVvBoEhVCs7-MmSL-DrMe_wQmi_4HU9x1EepsqHp2WQ5SSHnV2iPy4r7_kpfsy8gKKQ5Ab20n-nL8abiDgS6-QTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vREGxdXJlwxJQ-EVB_nylfCBrTG_Kp6WGnY2XlOYXbl4eCDinWiXMjo72WggcT4HUIapgro3j8T4JtJctPj6V3rtHbWaE7gGW7kIEHsmhGa8hFAtjtjr6fMrurmX9SNz3InxJzKKIFbzJ3oypM5mfKCdAW2kMeWfdF8Zgv81iZRMndI8Zw1M3G43zSp5hBsw7lWyqd5CyggxzNjiwIRDDruDjEaOA2Prb_S6x9OSPWPICTddQf_631rkLQNPTJlFOn7yRHd5ZfStJ7tZb67aKrqcMVcwSP01CSGh30LFSVbFL2Mb8EUg47a5iJFrn4RWc5f35fT43yXTzZC4rqs0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk96xz4D768htGsPOoxaWJ-FxtAi_OGEpfdSyTPLcLR82LCHHDBCfPA40-GfubKZ3eDdF0NcSruT4mki_OZi1j9Xpg-WGQh5bjKMOBWYKATRw_n_B9twtVLcwhqdAGjQMGjXxlRFhq3lukZCGP6ep15OY8nGYr-rMdbIasstcLXzeR2l8oKYqV3jV4mGLKFQ1l_zvC70JAPJSdnsdO1W6uOT0NjNGm7PWldiOemCiv_jCCsXN6o5Jqg6GfTbZ5JtfPQKtU2DP8T5ZPOoNzH1GJuAv6HqY5gn4Q7f81BezFHBeMs5DvdFo-kktPry_0bmYf2vE7Rm2i7fTG_Y4UfrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAh4PCbhnYOlKALR3xMavFvjVfuMY38AEbEAHOJZja7xBvfUZYogCHkokrVV3ZISIA-XloG6O_EZH1LKJbf87ffActzbK98ZTbS021yXuKVQ8Tr00Q1iiispUIin9sBw85pbxeFfVHgOty5IXaXy1fpXcaeOqKJBRmM3mmBxghxSsZ3NSeeYhcDI-hUkXrIZ-0e6rN4QWoV5wke5JyL8DTolTzm-_Tr0IsHGDPRCr4d7sl3V4jan7hHluoxzX3XWAJJleTLEhyrLwBw-GScvKV8JPZgpJ5sq20OVpUhOlx77Mjo5txrP5qkGFvVggAwtts85hj2Qx3D9c9IoyOKhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=QlhmJ4MBrBZlL-aQdip-6OEm8LYvS3PG51GbE86kUy6iUiAFs4Gs3-jxb_GLoSRYLGPbCV9Sj77NgXIbfQcyCRk728bvd9IQTQEHez1Kn6kCOcdbhSguGFh-uLF0agsBOW3cg-iX-DGhCLEprfpYFxBM3YcZR61IfCBeV7rmv7p5ER2otqRarLhAIt7N8hmkYq5Zu876VFkj_8WcITWIZm8wLS7bccleDoEXAF6PlA9RbuMxKhHdUWX-MY_FUjCgsoVAPDj4lR6hyAaaL7lK_ZJU59IeXJmkef7VOdMlAzJTg_0PHNdllPIQcY6h17Y23i_zeiq8FtaWXiYQFNpbYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=QlhmJ4MBrBZlL-aQdip-6OEm8LYvS3PG51GbE86kUy6iUiAFs4Gs3-jxb_GLoSRYLGPbCV9Sj77NgXIbfQcyCRk728bvd9IQTQEHez1Kn6kCOcdbhSguGFh-uLF0agsBOW3cg-iX-DGhCLEprfpYFxBM3YcZR61IfCBeV7rmv7p5ER2otqRarLhAIt7N8hmkYq5Zu876VFkj_8WcITWIZm8wLS7bccleDoEXAF6PlA9RbuMxKhHdUWX-MY_FUjCgsoVAPDj4lR6hyAaaL7lK_ZJU59IeXJmkef7VOdMlAzJTg_0PHNdllPIQcY6h17Y23i_zeiq8FtaWXiYQFNpbYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=q_vj81OioORTKvaEJ1_sc8-Aiy0Uzwb0VOXLkiZfSQJvs0fXgP1hACeKBpQfn1S1n0hJ84m1IuYaglBX5LXc1bQGofzR-14OAnJ8wVHG0CU22Ht_NFThGcbRWUL3N3PaEgaF9YZvlzpvCK7wY6pKywrL0yER8PVw4Z6qUNU6_1oiE2S481uv1UM5jmO5Vt7snFwVVjbjeahH-Eg44lazm1N9jtYQvACwVL_eXB11MYx5qmoBlqWyn6Esw2npSanic5EprL1kSF420LM86IJuLecv-YV6X9xDjMEDSnBO23dWR1JO7iq0MdQuD_O-t1sftxNdBJYv1iVXVqhvJ0042A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=q_vj81OioORTKvaEJ1_sc8-Aiy0Uzwb0VOXLkiZfSQJvs0fXgP1hACeKBpQfn1S1n0hJ84m1IuYaglBX5LXc1bQGofzR-14OAnJ8wVHG0CU22Ht_NFThGcbRWUL3N3PaEgaF9YZvlzpvCK7wY6pKywrL0yER8PVw4Z6qUNU6_1oiE2S481uv1UM5jmO5Vt7snFwVVjbjeahH-Eg44lazm1N9jtYQvACwVL_eXB11MYx5qmoBlqWyn6Esw2npSanic5EprL1kSF420LM86IJuLecv-YV6X9xDjMEDSnBO23dWR1JO7iq0MdQuD_O-t1sftxNdBJYv1iVXVqhvJ0042A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUWGikyGAapoyy6BZGvVgDOLS0DlfQp5Tjyy8iG0Fjflo8G6y7mvlFlvBWLXzxWoS9bqueEZClkkMB1tSjH-KnwOALeBBUQ4YuO9FSf5dJO4RWxZIn_2fgCA3S1DpGbGwYnHmaGyGxRCbcrYTBFvXPIDSbGbfhsNy4anUnesNpcEcf28GSKtQav73R6a1WuHQJgD-3ZkDnQR2-AdOrig1KjG1v_JpJqCGqZHAv5fiTfIqwC1kF1MPWkKJvgmnJpLunnx72aN7604hJycXyy74t6XFJADOFltzWlBTuLhE9ul7WiBKksbXU0wbs5rKyd2Jz-WhxOVPD8FD1I4MJWTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdabZvyqevqWwJLwWvjvC7bdGITlNwPa9fDYTBdZ0ASXcCIQmoe6qEPQsAFXm2K_3O0urlM8T0wXcjsW5Lk06ejHwHn_9nWWOkeZJCEnlDyEVKsH2jBBamQFkpeSl_wJkn8eNogAWZ_eVTYywiUR2qHunJSAdToUGzuP_3sKTtmaQyaiQkWvao7WIFVMt0FsfBfMuSmyE3OvSDzCJ3C1ZFqeCGivXY_w1py4Iceudg4lnrrqrW9A7GhLREIWY2yTGgBtukW0Le8OpFeXLkQVUfoxQ-7JSZMwEy_tnxtpf_WZCrkQU8P1z3UrowFT1uPTr9HqKZfWEOV78vEKJlZvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMJJHw7N4M6_luazOx24IO1d5KS4EN1PVXJr9I0trMdD6Uo58Yy1krVtwSnfAPG9sH6fPrrbW1kjbw2OXQGeBPzocZVlAB4xz1HSFdBOQOIl2xVoIqXiRmDNAt8iAbe6dyPOW3hlQtxzspSBTTCQGc3FvsM8jz7E9GpT8PeSaK-ct3igl1LIhhaumpbMiATh8kvStDhg-IqKcww-Y5UN6CxlHs_0rtBIg46EI2bHT8wTFQft7KDezpdY9FLOwUXqUFXevS8qR6N330TxgOy_8bkNyKYPEgfIr2rpSYVdjYouE4IB2EGsZCav3JqOEalk5_nSie3URm1ZlYAP_Z45jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y75hywGxE38vOzvm8C4CYvovhMR7Wi7aV-rCo2pFVAe48u6-1RpJ0zMm7A7y1bAvl_J2ydBCIYWKMsxmfjCNrjucztRoDjzsCumpAbJP8jBlMHUqOBjwxOf1OhcdEjSvNf3dqlN6OXt6LeHdizk36qg63byE55qIeImE9HUocx1556ceww9DR82UYNeTPZGlL-bXsM0aFiEL-keAnQW57hL_jWn7YqXr0uJ3jwh8bba8U1M41anE24ennCDnDZysIHFbl_abSk-Fh8Fga1KqZDcYWqMJAd8gKuqepIdZ3tcxpz8lHsGC0-s-TnCOIR4ivblXTxLavSR3MbXvT9K18A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVn41h50Ipn3u4jDKLUYR8HGd5F8TYo3KlzJrdxIIKjbiIckMBon73VBAScAdqq5vy_fdkPNHVd_rJJYdoti__CY8-vMLL5grnjHlUzBRkjA5PzHoRIFTDVFKICr5JVVQQaewV5gnY20-STOfll9VU_GFRu_UBR-RzUc_CWTqCGV-NaGlXREXmEeIqT12jIGNjaE-5GKGT0f25yUXVepKFJhB13Bw-Pok1KdWDeVLyVGxX-gfA7L9-o0P7ykH6xsTYKEis-FvQoou6vg4ys3DtKAuypgPdCjvOukUZCPRbMBxUwC0uk9GcDqJeKrW9YPK_88N67tafvAld9gbRTaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCVj8EAhbsnSpyox7L4Rj8-VCFyHE_pWi3Ypwt7zvjRD77c8lbVD5WBuJN2WrdaZHJq2EzmIZZVZANS3DvC8qnOZn7sV7bhi6PcQaUqrUtrcVHRhFMFf26QrUkHwOJnYmQjZm0lHlXx3m_rRgpm_4g-xfIYMarF0IBHmZAD0M6tBCT4a1D4Yx5YckYtP4APd6oeEhLvzXTAsud2Jo833xqd1EdU99wAYKdqEbRjeo4uH_yorMR7G16-zMdD1-HQIGX8BbR5zrvIWSYxuLPfvpOHJmHIn1XUB52AF3r-O0Tv7dVUpE7OONzb6-ysDhcF_X5VxbC5DvOh0qYafwURYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfbPZPoEhy1s5UNCVopUfnys5dMkQgjN470r30L4aUIyV4OuL6IK3uGlgREwXZDZHWzTEJMk-WNeNuDAScQRiNt8iDcZq8Rzzqal_B12o8vVS7rm0KgXwT2UlAUIuaRDPsqFA3LGL1rfHaPYq_sp_k_NHVbfE_vRIj8a-agZ3IjA2xpNTkpvbk9W1TiNxvxhS8Is1kdO1FOMLDSJHg8yT_hEKWwbLeXKX1x_SPfqAjpJPU_PDs2o3yD2EAu_Ni5B5CUTDgky30xuAkW6-x6ytI6r4W6okU6Q5p3M8x6N2_tMVHC7l9E_V2VyyGGsEy8QE9_FTh-93kOH0oErcHSROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oh7SUl8TEO83CB2MYckfWm2pMMXATsRSbQdLlmHKfg6BuhY5aPK7X7vda-e9jXla8MkZ-av9NJ8r9MShV6gkZVKhPJqOoztsdTDPOZ28_kqsEcSmAXtW_s5A0wQr9oywb1fyTEYPOP-xKs6EJVSTNPSD8SPACWz2agFimZF8ZD0jDr5UXUEq2z22KFPNOwN1iC0X_YDOJnb9b-MDYt-O7p56ZyukbAkNePCPNBsR16JmhRou8vm6np89G9sWPI464QI2jHKh0UK5vB-ZNfM2_po_PoclY51R2udf3XDY338W0JKK8fdPtXzdaKnsHnzuEsfcmIgd41HcZGj-8OiQZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdMx30Rqb0TQlJ4MUfpDyztNPI6wTEzHn62dNvcprG60kGoxcHcu3Yq3ZUcfxrKmIVeGZ8ko66wUrKVMZMCStb_QMzeE862ncB6LKjx6XKSHbcRTOozg_UjXysrSZQQ-x_lCl_Qd57CeHpWCoussmjFOGljnRKdgNqg_UMvGB-CqrMiAQSglFIJUownfdgZWGcwARA1fiQsC7jqpDoMucUNZBcbn2vy8If06tXbVTeUyZcX2osHdpMMYnRiI3g80suBktEJtlWrVcnFfN3pYiX7gox5a8kuEwazn7c0SeRYdOsufKG5Dd7nJ5f0dV-8EEgtS8-YYlaWLJUzq_uJj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=Tg9aqAUbofrZw0KNL_JnxG-BhgFAR4Vc5CvkTtfx7rijwjMkfI4rH_RGw05miZR9GU1-Y8Kz0ZYDUG9WvAtgL6RoySToiaGr-B6URLgMuRdEEz7KerBV0YCeugv5fhPTApqcQAtsSq5vfyRdUCw-w2sTfMKXXJeTNdUKCZi8nXws1pj09NPf6SQBwFKwduVGXoyNn6b8qv1MXy8kNEM4XIL7xkyFW9PD9nwcNDuAlRipg9CftylL3coD8R7ML-iH0WTTOKFOV3LWA4bZ4OS6aWz6Gqo2b_cdGbojlquZCG8veqUZ9QINsBJ3-hmrelM6GKpW8QF5KI28FyblYPrh8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=Tg9aqAUbofrZw0KNL_JnxG-BhgFAR4Vc5CvkTtfx7rijwjMkfI4rH_RGw05miZR9GU1-Y8Kz0ZYDUG9WvAtgL6RoySToiaGr-B6URLgMuRdEEz7KerBV0YCeugv5fhPTApqcQAtsSq5vfyRdUCw-w2sTfMKXXJeTNdUKCZi8nXws1pj09NPf6SQBwFKwduVGXoyNn6b8qv1MXy8kNEM4XIL7xkyFW9PD9nwcNDuAlRipg9CftylL3coD8R7ML-iH0WTTOKFOV3LWA4bZ4OS6aWz6Gqo2b_cdGbojlquZCG8veqUZ9QINsBJ3-hmrelM6GKpW8QF5KI28FyblYPrh8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH8k-cIRWtUoAI_HP4nY3PX8_YaHKILHVYLi5qpoMYYksQwFZlWqXmkOlsyxCIGJa_Y0Cknd2E3ZhQuCPuizNC2Mxkzl6yVIR4hgFYAczrkQBICAv04RTRkVSBBsyPoFaQrHryZaUwX1bh5mKTrlpUsaRsKnj4_jXJPQY5CdXZEt-oBDIqET4f-mv0Yd4T45KW6UQvgMHV4wRt-0MsoaOP0oxFyK9Vn-3g6dByMCr4K5ioEgR4HdHG7GfVdthlENdjToxlo_av2lnMzC7OYxPBF3tiAXl2GYjLNjXw5_bFQYmOkUQDPvIi875xpSZc1jHnqbS9J920YukjugS3WZXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt05UVos_W3E-aA4_MDym32aJHmq9-W6ZDzoT812NNXbNH1qhuDxVl6eRRGfMTjknUAvZX3RXpmIo7T_YkV5UQjuwqYsY47i7MvaCEemqWRsv80dglgLWqrin3VIX3DBz2xlqBa_9uyMDt0OpZP2Ns3neSvnJ2xTATDOdekZzAgOtOzuIIBnEIgpC3A1ODOLt2f3Pty45Nr7-h1c_07o71f7sSh90N2zLq5U3D3pImCkO7L2vI2elUvWLX2Bio7-VYH_Zia7fbddC0bXfZZTt-uAjockoH0Rivc0d5yimMH273GNip10I68aru7theCPnY_cdTfYMn6wQ97eXF7AhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahQbwWEbrX_0pDXldfYsumrNIiaDl5BwW1wgxaT2SFi4kXjWCLL9mxdHz5m-ftREQC7P4nz2l3cigs3Uyl741KIE2JKfhybM8RKzuIVn313pUxr-ZDJhrL2YymVz1RAcFuEQGO8tRftL8bm_rtoXI53nZyYn0GvBlbSk0TVNLUai_p0WoX8WF1OE-1rIeDpMZbaTOqD24YEKitW1_m6UtLd3l2HJw21Tfsoo5hBZM-zeiWibCgmsFR6DtLZc9LoImGiiMygTdt6HlorpXwHRKS0W67uofPe8uzfqkTQvGasDa-JzjJfM4jebp3b-_kB7qQ4OLAGu5skI--wkRfMjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1__5ShB2JTN8_TBhL1gKfo7qmI2JsZGkxDg1n4AXv51e4TqoRonxY_6XQbHWGIcmFcxKmpmFqX9X2u5AvX9h5be_8UyFsX-cVy7EEJ4ysuN7xD91F4CBBt6BS4cL1Tc_tK-MhJ1av6PYuAkYKfh7a5w12gQLY0lsNokD3gAaxR0NrpcVR4FhRMnE5Kx8m-LItWZ1cJOGK-zvfv17GNJJL6ok8xu2Waw3K74o14u7WxLPOrmXkP5XIoxb2lgv4J3_bNqORSHZSyWynlZgGYMrQmLGmK8koAMQzoMiPyqdHJTf1MqWXAN_M0N5lfqv-24j_HDZW-XNxJzdzc0q2V8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4fgzz6AuEK9C6MK531xVAVZ2sXiw-kVYX3RcpKs02wZiy4mSSX21gnUiJxKsg0H971pdBp5EsYLTOpgZoGJ7sW00nqWA0r8wXudocav1_aXPOiaOoG_rvvAgdyOiAAp7DtusQDjh5vTZHW6HULrOMfC8hwQ39Zv02sdeCU85Ts7VvH6Ukr14aLimyF5_t8ba9HQIrDLHyoq859ILEzRIvVYt1PgAnycUcdFJX0BCZBV1p1zx6Yyr3XYGfxrRpeJap9mKcxXr7REFRCbL1i7VSAMQY2O7SpYHX0HN1UquDjIgnQLghwkOKsPnEwyV8PGZa5YT3UbZ57ts_YMsPlJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVGX38i5wJj860tmk0oUqVGewHUBOYYaQLOBsBFHAxf42PDnnPelJnfkloEBCF8cc_R2ZynpabaYPIGE65o1BHpk-nSbL0Zj88O0giGyO9J3mYFDFf2AOmjxtZeMi4W_cQZ17XzUhD7T4z8Gq-oTN1TXLQlLBffhIgmYToCJ6liXxLT0g7tBl37UwWnkAYqEI4qVgagL16dHmGDBiv3kCkZtKa74jLqvXSpjRgDcEUcJNToBz8KU2P9leUkonvWN5uUjYzlPeCREP0d5unLct0GqcNYMXEeB1-TSl_OlY-iLBrZb86p7awsmUO7gUHQfrKg1e-XoK4FdgWvrbxhr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QeRLY1mz3CMz0PNLEJUn7hvviC0DzGfhxJdtc4Z97Y6tERWGqLo7YuS-Zz6U1z0o3jb06bqpsvwqgniD_aYwfQQbvwZcaxNVntBvQgGJnovoQ1bPRJ2I5S5gZQLH-aV8Iv5Di48B8qxZYbgHqsq6W8RI8kBkrsXMEBkMvtzY9ffoZ5fcBRXMeb6edziN9TRxgNl1TRa3f35ytudXCK5x46IPYwnimdYnwFGaCba_Dwlwzl_ba0KJE4uWX4rsz-K5UyVyzMKtQjF_vfQa8sm4cGqI7EnSco9B4XfLDtnlvHaucpx_yA2cRrMi2ajIaVRTIY5nlkzc0d1YoiMZ9UNj9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=oguIUnaLeR9anqpsfhob8QLmLKQzRIgVBv1-C-8WVmOKb_yToPKCsvZu-VnP7aMrRU7A_qAg8M5JfAlhw1fuvm23STNUhjTOOIyquSw7sga-WSPOjCG3CNFKnXc7oZi2tQR7-S1ukSYCW2Wq9_9u2nwKoI3HaXyuOTUlhcSDqs9dE5ffHXe6bA_dsAJdk5knzEmPTA35qda3u9eIN6v742u0XkN5y0ECVaziFOSCrSKVIGXqgTRfgNfgJWVMuZoG5xEsBipgd4dYS2l-TY4DCLRugpqso6k7JrDpW0p2QaOn7MgZA8yOpRqjB0KaO-M0mZPbXtr750DlIByRgoorNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=oguIUnaLeR9anqpsfhob8QLmLKQzRIgVBv1-C-8WVmOKb_yToPKCsvZu-VnP7aMrRU7A_qAg8M5JfAlhw1fuvm23STNUhjTOOIyquSw7sga-WSPOjCG3CNFKnXc7oZi2tQR7-S1ukSYCW2Wq9_9u2nwKoI3HaXyuOTUlhcSDqs9dE5ffHXe6bA_dsAJdk5knzEmPTA35qda3u9eIN6v742u0XkN5y0ECVaziFOSCrSKVIGXqgTRfgNfgJWVMuZoG5xEsBipgd4dYS2l-TY4DCLRugpqso6k7JrDpW0p2QaOn7MgZA8yOpRqjB0KaO-M0mZPbXtr750DlIByRgoorNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=gxmee-IDGJfqzVZnPg1s_hnwKee55V0RbDFRFoch6edsJDoR_A34RZH_y2UQzkeHBKkiUI5z5IdXT9L7UxUyUjeMsqGPJLqoS6VBnk1f2Sn2Y_5IuMSNSJKA-TpxhgQU0kz896E1qBCMpS3qDBqSD0q7JFq9Qgt14RUJ1rqfP06-1BJBme-_F-O1ts2wy0_-X7ZcV9cnZzoC84Ak71GQjwxi4emFoSHgYm7l8IFYG10xT0gCkkgb3FeeSYncR8N8CUpkwmJsKZZj01Vf94FHg-xu8bvS9R5TZUPRz6Geul8rsOl_UT4QOsqGwzKg7ds5cJaR7e1WmzF9FDrK77pzww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=gxmee-IDGJfqzVZnPg1s_hnwKee55V0RbDFRFoch6edsJDoR_A34RZH_y2UQzkeHBKkiUI5z5IdXT9L7UxUyUjeMsqGPJLqoS6VBnk1f2Sn2Y_5IuMSNSJKA-TpxhgQU0kz896E1qBCMpS3qDBqSD0q7JFq9Qgt14RUJ1rqfP06-1BJBme-_F-O1ts2wy0_-X7ZcV9cnZzoC84Ak71GQjwxi4emFoSHgYm7l8IFYG10xT0gCkkgb3FeeSYncR8N8CUpkwmJsKZZj01Vf94FHg-xu8bvS9R5TZUPRz6Geul8rsOl_UT4QOsqGwzKg7ds5cJaR7e1WmzF9FDrK77pzww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
