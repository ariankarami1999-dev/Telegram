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
<img src="https://cdn4.telesco.pe/file/aGYe1VXalSvP8XA_AjnJqQwS23WipVc2fl4G2-8PslkMVKFE1sBfjmn38drIWp9tq5XiH-JHrEU_HwSrJ1ft0gRn8MkcBqiiunUiEcsLbgbk9p9oZkyIYJ9WJBMu-TWULiCCea9GOeWygZhhMMdEuet39bRQ2FDuxw6SArRl75f4AgIIKvBQipIuqKdk63Xwfm7jKyyAF86W5BpT5xIxszpvzr0AIy8daF9XpJWp4pP44D6rdXhA74GfOVRHRKH1nRc-8OsN-yIaSZ3_UheqSgMruuIpoMYX_kYjEpoRpL4mEZ4kwo1dgEHFSbqFvQBrCjI212v8dvcCQyhM2KWqdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 12:03:12</div>
<hr>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=E2omNYCWWNVvdvzx930ZXfESi18XeCrDJgnTCPKDMsP4Z9MWUaiMjAElP1bruxkttRDNqcxrPj9bzgh89IJiXDZE7EQlwdh9dB3sY_lZw_kFZVeE8H4QeAEbjeYNunEmbnLsehsZWgOuKadXD3cbNfh3TXG44wA6eTXibJ-SI-uJm2xHUXSZOzsxPUEq2lnpH4CxAJw0vUIhQNhCOHOnJ6c8YYznlIbiEN1hMxmO2RUk0BBlXR9mmn3tOzai5DWGn7V4GDfDTbR8bngSR7BLPvTUSmGaOmzGoVgEZh-PfcAdoRVmWuC6T6AqqFO9BzuqNdFFMoXkTqw8cAIkn_ot-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=E2omNYCWWNVvdvzx930ZXfESi18XeCrDJgnTCPKDMsP4Z9MWUaiMjAElP1bruxkttRDNqcxrPj9bzgh89IJiXDZE7EQlwdh9dB3sY_lZw_kFZVeE8H4QeAEbjeYNunEmbnLsehsZWgOuKadXD3cbNfh3TXG44wA6eTXibJ-SI-uJm2xHUXSZOzsxPUEq2lnpH4CxAJw0vUIhQNhCOHOnJ6c8YYznlIbiEN1hMxmO2RUk0BBlXR9mmn3tOzai5DWGn7V4GDfDTbR8bngSR7BLPvTUSmGaOmzGoVgEZh-PfcAdoRVmWuC6T6AqqFO9BzuqNdFFMoXkTqw8cAIkn_ot-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3k8KY8kGJvAP2AAndTAuIcDP096hiOqHTX4vN__zSrCUG0XWofcZCTx22ov7tmWhSiTc-vF74teZiqGYAFjm1a6DQH801ylGKPGAdqcqOaW6wViYyrTtuOfzifaUmsM0RwwoyV8VKlihrrsyyJpm9f2BD31PYqOQpRtWvIrhxh_Lde-QQMSYONGi7tQt-G9FBVZmySHCZcKOLvhHTdUNu3_NZRaLZeH7F7h5Vn6ufiMYQb7fokh-SNt3LlIBCawziVsp_q95a1wCExGQp_ayPotx57smXhxGaLlpPzT5FPSdrZvIbWTaNpDp-SkTt7fdVRt1PMBIh0ZmVKn11t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwsBSRMMsea8Rh-Jk6A36yJIVd2Vh3LgTWw11UH8i3TDitHOnAV7q4iH_7z9w0o2FB1l23z5s9UJCcy1DnMe_JwKFIBhS0IAlMEL2HnSPJSSEIDTTpD41poQ3z9xA4rR7FqE7zH03J3vxG6FsOTiJ_myZtzB5f2tdMZKCX5fLB2z6_84jpBkG7RrMfHoQW55-ajzkvQQdVX4kIkSlpkHTEY41Zy0yN9AFJbRo_WSGsim13CLiwBJhh8DrtrGjellCD6HETb9tuIdrzSPDD-YBRrN_OUV_huG0ScsuRwh2aMU1kOBD4qovMYzuEVwyEqkcXYtAwi1LWvSCxuJ28ilKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Rb7vOKXYANEkdTdXUwNbKtOg-yTW5f-WxScQdtnNehTCQts1OMRXGiJHXuN-NvzLsoAbMuXaSRGF2nBuc93ChBu9zXRTZNqoy9ZTksUAp7KyDRfB5kjDi92z5gNuHB-5h2tBtgdb-8q2hY1A69K2-ted5wmOLhZR4FTjAn_Apr9ozSJgTRLFO4DCAeHIZuf-kpTCp20N5L36G6wCxcgJbJ5dPD_as9diM04QqAyF-4_kET89Au41qQdY5JLTuu8O8Y4Of5rUkaAMBm3J1fgTxJXIUHQTBPYVoLOwQYpZTJzsvYV1E7jkuKx4VW3oGDfVlPx9bbXLAOkv9_s6AgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsZTJBX_xt5fjVfaMmgI6e-PCbwU7BMBGzhqBWIfRKUg5Pe6O4hRq0o14MLWxccvDcbxAsbX34CSiElzTCO4IaLB1SEPqVIl_EB8V_UNbhkLGlq0AVlrweb5cZ_hACt_00tZHFcUxA82Z6xRngPGVsy2W7_ZLW97xpGgeS8nAnHRpdfLDxDT3CrXKEb9kv9eg33hj_ZTDf-LTzxYslMNK8q_1xM1MYl_ZB0vPlIpejJafllRsaYwLu1kTs_G2j8yyn63ATGbgyhr_0Hgc1Yo7DvQQpmqbbQDqxKme0JbQL2vD_rrVqY-fqI8rfsdDYXDsSMPJCxXckoxQbpAvpw5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ1H0l0U63-k3oVaFUXprFif1I3hz7MLvyLASRAKYVzXwq-YPOuaKaldefYN2HQtfKmPkFSQByphYfBBrHReqUTr6e-UbMTzqk4XexdCWR7nMGpftuH9FKK-9Ku6OKw-tpVepXAaYV5Y9-Ld_wuCiQ_YSRgOZME-vVZQgDF79kV83Wim5N_5ADJUCOcdGZJuZuwpIEeKAOuNYgG1LhEAYu5mRr-MMzbQEmGna9-88hqszGhBjP7lpkiFzycaVBNZeQ6OI6gXHErGhEgcHLj4SzyrU_HeMiI-YN58d0wOaXAUfm_LqDNEM_yZ9avXs2VeAV7RnBFJPHypQ6g9vdV2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISShzcooHJKo9U33ZDXDq_AZ2KJcugA2tOmTTiO3yIcJNhL0K9blPMXeMoSFtCyilTXr_FQJiKOVdCxDjCijfuREznkLlBl8MK9KEF6kmcIm1X6XgoPSHh0Gl9wLuhTN8Z8LfGJEwjRMyU_ZEOshCwKJalP_uQlHcxaNjPSzrbZUCFZL0LnYnkUB61aZ3MW_6H4djUwIG3Wev5aoqbjHx_j_6ZwkRM8S4NUhyET43dTuWRY-LuYhDKy0zmgZYnZBpVxGUhC7X76iytilkP0Y8zDOhLptjA06xJFO4HONcztMPfdIyZXKZp58qo-1Qk41v0cORmtYQQBCnciWHsSZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ndz8D0Yg9Oidr9Rhk9icN6mNFcDL_v0xfLFtOymm6lbQbS6a93goYsighEi4XPyxYpGFnC6oabestYnTW9PLsR7uZ9arktJxpCqhTBnCe19mf19jEZ0SPWAvyp3iIRNnF5J9IMpH0Afec5auV_JNzZEvqtdA7nIheuD98qnGaox6RB6lrl4sjTPm5EsRmYLYnrb5oTjwN9x6gq0e44zavxEzVTzzGs-sBLtTIHhtwA8TYEMSvPZ3pbt5fODXKx36LqGrK-DyTumzJeAcG7FNFKUWF-_SCy2DFSsfft9ckni7XaHl0qpzM7_cRhaKpr_cLMz9297xeD3bsm3Vsq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llyRh8x-y_tU88pcPE92AivwyvMYfH9WYQmbaopIJLzeBh5vX8XJRQ9ZqnOhmEXQzVSKQotZ1bMUgHuXV1fj-HXvjBeO6CWv-MzDaGlvqTHT8r6yTzJTYELbpEVNPCEqWakrXlNHYhvunXZD2ZasHVcOCwbd9b8XtlonOtZBRtIJkSipUdXROYesuYr16WJmthmyaPqNxM9XAGDWVYUAlcn2ocYzxQpkmlRAXxbujIfVuU7BupSyvFktRzRooixKxA4dM3JuqMuLcYq53rsXAptCJyw4l2IAaEWhy8oKM-zUNw_GSIrR9DoKiactF9Ur6Sr007_m0-cS0W6EYz3fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiIZYTURhwybJSbVPdI0kCYcFu71qeoSF_giNmbBnB2U5cVPQMqmWZPTr1D36Ri0ARrAra2X3rjwA3HJRENL8v6f3cBKu7Ox2JSDdUmYNn-X18BPVZJDlMTJCso_p-viqwfr_HCRo6vTh0hromg0SRU3l9RVWAR3oWM0kpgtR2j5Or8cav-cBz4vc6__mykgjeAK36TzYw9FshetEOUtC4s13ECS2nCQS3bo3qyuW09pnUJfEekkxSMkIp6O4WJcFZycRnF3OrbqRTNv-wKA2VFcX0ItpVgWVG2VoXDFHmC7SNsAmnSOgbTJeBvSSeS09j1XI6jwvtuqz0p7bYK7fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPyLKqC2Ab8FwvxcoFYjY2oFfSKAUwkj9D8tyFgarLb6TIsKRE4WMVddSDEp15xwSLMZJNViL-StMs1EO-s2RqN9jYc1L00suXz_KWtIGNsLZcfe03kSP8qQwUdHoYeiapXvPImTB2ownfO3gidRSHxDS5TnQPvpj9v1KWTNRra7deoGLGjfGTWwMSBwUybvPCO7u9AjX40-1uDBxJW1VpxdWisznZZXGvT3jTg2dfH7YQTLilMvasvSeSEj-mtTBt-RaMM1h7FrAaJnmULfj0BG7g2-nETFkGxOLcPvNvJXmaA6tXvWnKC9vH4Z1m5cqp9weB62CJAp-Ru1nLt8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3U90zV_bA9BbOnca6Qm9r9tfpK8CuQ9E6ZfjBvFNbdzGYtF559tvYZIvgODN5UeM0lwK4RfPQg3eKz4zjasuAYQ0m6CmGqtWDjyAZATYYBhuYPMs5Am5w4EjKyu9O6uzGoyWJO6Riv0kQd7aPEyWoFgREsg9WGoeM-mWJ4mcp2h90Z_0MhDCEzHMLUsqYn9nOruQ2t2QCgWbPqIyNY1VCWjvqQqSbuY3jNM7yOHskubRkFS-ZLlbRTrFmXgyNci_bhN39pWeIJ8j2BxjbexIyckXvpCJnwfYHqx-FvE8yvgqUK-1KmRfpRkX7hW75nzla8ecncrMwBQUswV0jJ2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L64VijQjG8pYE3raY3iuxVkV6-1zq3bglPgHVQP50WAkVunbPJyyR3AQqxvSVX1LlDGfUboe_vfpVxZ7c5pBEUd7jdi5yum3Kdy-47EFH4Nl7PRvucPA2i6zqx16agoTcxVdukSRwIjTtGmrnUvu4HZMoX72HfU0UI_4QWy2pxWP6WrBN2cciZ3toBwnzdN5ywegKHQ_FRnNgXMnARo7mfw1m2JqfhkGBEyWOHFzk5nG6QJSsgyJJg7_fDvJkVGZLGukObfNeIkce5oFW3yKakqW-cD7wy43RC3cIJZpYRNT5tFP3zyE9-GS9oBzzQQBUvdpUX9SMzkeipqMJ-Dy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfOG8r9Le797iCT_r1O-6F2tl1IKrJXs0hhcDjwGlX56-Y1VSZjX9DosHSHHmxdD-7WTb2uN5qBfL5GHqSI6RY62CuJAxxTW3WOtrHiOF69Ni6RfArcbx5TD3O9uEWXwsxB2qnvw5lCEJZnqje-nZXdG4YdkYzcaJ3GxibPUFM4LKxQb_b7TZP8xzIR8zeCuL5oY3GhlH6R41k8QBJm3NTYGV2RzgNtpeDmVdzNFO5ODUZ_XdDwc5sxN4ma5TjG4M6Nr9rXx596qMmqnNNdc2RGXTN4HnxHvJQA5_Lun6ez4FZyYfadpFbg5jkH4gyaZkTDqSlLeU0-DreGOFmjkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkjMW9Ripsw_aZUHJ-A-jWeQsQYE8kJP4cxoEDi6jT6uFSus9QmyCwoZxEUs-spIvd6UKIf2vAfCr5jgpLayQ5G-jHlra1wXj6hstdcI_kd8OSDJYZHymty8ogPrjjgqSVp2Bs2HX1pPEUytEpEUGsW7nZuraOVCgRlWozSgvoBFYpll8LVFpFAAYazuvrEjjGf3QJoNcd4pmAETTdisJsd51yfCuwloWS7NTU_CRmh1q6O22-HMj1KJpR_oYFqNk6_hX7b6myJoDqrPY_JTsZIrAZyMgP32FZEKtnNWXZpYTtjNcLhBQkkHZKcLx06-vKYUnAd_jQna9wPNHKNoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbGlsor8b9DpX3qbPIM_nRfRy7TKxbwgL2oiosM2PBrt1cod-MpzJhoQ_jPX0-SjpoO4evpyqaNT4GlNMWP_Y3aO61nKVMwikzNlRwHDTlmHZpC81CnPC1gxY0E-tiSsFIlBYW_H8Dz8aE-3YKnrbzUL7vI65hfvrhN0hC9i_pid88Q89HFDdvyNnb0FD36GaUa5VR-FaAB1dazciXWZzQKhWDoQTLfr6oFnL0rWOupdVXc7Wt-Q0xCteBH6QMjS-ARyZdHbj0T3-3eDHqjkLSvmMS3XNf1Fb95lnXl2kI2ctsuAbv9M6SCCgMvxsYRoFM6YHQTUrg4knxaBN1Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMAkGBrR1Wrrs-8F7EOCnSK_eDHa6IPFemHwWozUNCnPROiCVN-F8kBITQ7eLiAPkAAfll-kqLgM28jHZwsQgngLvKKZG09AZ1kDljgbZomBYyJ3mfBLYbyIC4i_HjjfddbYOpjBEpdPU1BeVm6L2EBr5rYE9XJZ4vCiF6TBFm66zyRGaADSGmvQxR5xKhgS1E09Mbn1JT8CTFqYWxwfL_k_lSuj7CTpMFQ6IWzb3KF3SiYj0mzy4dE54EyFqY4eQT3K2j3eywYWAil30i22CjyyFd9EXoaYjsgi_R3OSWg5wmDdfi3GIfaIyxvcrt3K1ocMCHQEn8rmOOFUfRTlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=j8wIrEsMK0NcG4Ep7pJe1bP2ZIPjmaN0ubYWVudf8fkU-V49fyeqQDYFq5fKjyWofHyEVs2VH3wJ9FaeUXRfJ3sfMxlgjlUt_sDtPL_GflG4acjO7jQeObPFLeBrCjk0L6kY2btJVTrmMJedFMshbgI-2lDJ0BlOp9Yv-QC7nSypZ4yC5fmDmGTrmR0ymIDoG0w4S9jb3m-Ax_6a24I9K02xkSXQIfwWY798tfwoZy3rW6NSDPqSgOSc67aQYkmh9qwtm4SAA2EffcWSEEfmvWKfEwD43U97LdxSvgJv6sfpi0Bfmn-Sy-QaqFhjYWSNAlDOS-h_JWIj2FNwCiI_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=j8wIrEsMK0NcG4Ep7pJe1bP2ZIPjmaN0ubYWVudf8fkU-V49fyeqQDYFq5fKjyWofHyEVs2VH3wJ9FaeUXRfJ3sfMxlgjlUt_sDtPL_GflG4acjO7jQeObPFLeBrCjk0L6kY2btJVTrmMJedFMshbgI-2lDJ0BlOp9Yv-QC7nSypZ4yC5fmDmGTrmR0ymIDoG0w4S9jb3m-Ax_6a24I9K02xkSXQIfwWY798tfwoZy3rW6NSDPqSgOSc67aQYkmh9qwtm4SAA2EffcWSEEfmvWKfEwD43U97LdxSvgJv6sfpi0Bfmn-Sy-QaqFhjYWSNAlDOS-h_JWIj2FNwCiI_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPytO8-dyULnWZQ7ZsqxaKNV1ARG7tzXAtKdwdPNhVRHxp1v273bAWjBif5Cz1fAfDdqWxaolAa4CEx-dytTNp_O4_t8AA4IKuwDJHIVi2hhiKjxhKP-74xUcvnndclF1x27yksEliPSdFN4JFxEGb2UGadck8XPcXYWzBwcqedOYWJGJKm--z3-b4miSTLzUXPd4TxHOUpkCBM4ZpuwHVRC10lAPjg6pi8WZOsEPn475c9Zfl655vt_m8SXkv11R6IJyn_ZTDeeJJu82I198QiXhwif3QiGMEDmnm9dZGdORJq-pMI90rAPm_2qEqsC-tijHcFGEZBWuZq_NduUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=i32OBxMoCygfRsjbnROAQ5dLsVy69q0GMv6wUbkZR4yMpHbJbIwOOoYTUXTSeni0yosTqe3uhGH7zbTNbofM-f6_ASo8eO_k96TpkVJ4VmLCa8HlqvgcJ5BWBhzJhaIvnvGVGbAGLzY6xQRbsGAetJ5LLClKAx5HnuRtvXV4bbqR4EOpGpcIJqJncbWb3bkyhHalC88diPGoyM8qQTousnIuo-EsolinMYT5Oo7tcR2kYLeYOsKbUwx6dchT2NTKCsZCpGtjVZqwNiuMBFbDPVay4MHI4eITUyjnFoNQZiiHw5PlhvyXBA5DVckkGB3MWAAWkJcGYtvRFD0jvVb1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=i32OBxMoCygfRsjbnROAQ5dLsVy69q0GMv6wUbkZR4yMpHbJbIwOOoYTUXTSeni0yosTqe3uhGH7zbTNbofM-f6_ASo8eO_k96TpkVJ4VmLCa8HlqvgcJ5BWBhzJhaIvnvGVGbAGLzY6xQRbsGAetJ5LLClKAx5HnuRtvXV4bbqR4EOpGpcIJqJncbWb3bkyhHalC88diPGoyM8qQTousnIuo-EsolinMYT5Oo7tcR2kYLeYOsKbUwx6dchT2NTKCsZCpGtjVZqwNiuMBFbDPVay4MHI4eITUyjnFoNQZiiHw5PlhvyXBA5DVckkGB3MWAAWkJcGYtvRFD0jvVb1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u25nrom1IJz0Bz5uuAkuPeoPx5hGmOMR1uB5-66yoIJa4RCSqLTboPh0Z5-B1ai-u1cQiZQmAdGeUycTOmmn-9X6cw_iK1WRRYcS0kB9IQv-u1eWQqO0X0GtpcCGdsQzN37ZPDXv-U58vobAj4_S7Al-C7btCf-DA5lf9Sxo-Xf-CMjX2XAM7sKjuUxr4tWh2yBokykLoLGOlgkCr2AiFg7o7sXE2fx9H3JIASXQhpUESwt_H9xzq3AUZUkZu2bNxuEyj9M12sVu-FxZ24trnuslXt9n15MXDIYELIwUBG6aXgutFS_BxBg7CriQIQv7tuOnLpGGysJ7K3fw8ZOiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeBbZAJ-WhGpSt8IeNmbzoiTAuDtoJU7rXtZhLrHtiC_Oa5pkB_hDmn4MWAvczjd9-Hs0FB0Oa1TPAX3BAjjsyOGzBS5FoBEGseWQYpKyYMesu9n9T0UFZNgppiMGuRw-l-DFH1oqV-2DTX_L4laCydPHXZMiWCsNx3XHXp9v5JIYX-fp3Zo5ApcfQAP9Pk_3OGQWdqVY_fSL4tQk0W4_QS1lOls4mkpNO23up9b9tsdCXeY_o2Ham3AeOd1q_mpWl-uB7_cAJi0z1d4gQKogUReN4YDJNXgqpOz1cGpwZe3e8IOCOY83Rv2auwnWsGhdsjdGBbD2-yhXVJV6qXjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9rocoO2BelX_hO6EzE9XiKY3j4obinly_J98vRguSkKDcyirUEbgjtbgLPDVcZyWvjxY4IDJZydvgGaqD7YFaWkjnK28YtYq1p3ic0uYCSZ7tcDCTr97n09vcrrPhEfHfP2i_q1K2zi_8_D5DKeA0zlo0imAQOJ0Pb15evIPp67eGEW1PKZ7afeMfVFt-dWsxU3cPZlRroel21OnHOhlB8O2Ab3P1UXesAVgmSiRcIpRIqeseRnkPPuVkWGIhX9nvvGRYUcw1QtdBvCVCkB-Yg10gj4Jna73esPNSvuv4RpwemzDiIHot9UtvmXhQMtQeiMrROxnks5S4hP6AmsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=PKSpmP4WfuR-Wym2AxC_jaBo5TsVMe9UWTf6k12wR-3Tu8_xazD7pKrB-mnAAUCRy_qLC7F3-Z91zRy6tHn1bZTP2ZXUDxKGUj56lVn8rPayGCsIZ5zP4fZqs2_l1PAyL0t1W_1vLtpRNw2bLFgUnuC1w6XlrbIMfn1ORk0W8cyE9JCwkdy5OuP3g0rFdD-Qky9jm0_LCYFFEtxsiaAxFkOLbtNeVKT7JwU_lmMkhorKbPwLzzwig3Cg0PSOj5TJosFg1JzqAoTbF7SWvkzEhUvLHECAkGupAbQDzVyhFWkA-bD1tjaWStkcZ5wqWXSgywQ67myOIUMkAZPB_8pxbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=PKSpmP4WfuR-Wym2AxC_jaBo5TsVMe9UWTf6k12wR-3Tu8_xazD7pKrB-mnAAUCRy_qLC7F3-Z91zRy6tHn1bZTP2ZXUDxKGUj56lVn8rPayGCsIZ5zP4fZqs2_l1PAyL0t1W_1vLtpRNw2bLFgUnuC1w6XlrbIMfn1ORk0W8cyE9JCwkdy5OuP3g0rFdD-Qky9jm0_LCYFFEtxsiaAxFkOLbtNeVKT7JwU_lmMkhorKbPwLzzwig3Cg0PSOj5TJosFg1JzqAoTbF7SWvkzEhUvLHECAkGupAbQDzVyhFWkA-bD1tjaWStkcZ5wqWXSgywQ67myOIUMkAZPB_8pxbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=GzSfeMzqUA2jcbdd5443tHWpeG_1T-MhSJ-4N30qGNsnYFe8b4bJFcFIciI3LmEFSkOtOq2QVPO1H7ppWL5aOlvXi44fuicdtWUoJkiz1jli3PDxd2n6hT-QFcf77V69G5BY-X8dbKb2IG9yxjlpHsIDxSE6ZNSZENQpKKkWE9d6GOpj1nP2oQZj2GqqqMx_BN_nDcNafaSgU8QP9uNLmGUgQC_6kUSx0wW1yj3JbPsx9WhSbQMajH0968mP2W58M79W7us9YIcM2YPVpqknFzWxOp1jiBW--0Op1PF5dR87u0FfDfW-YnFHvFsIFggR6higdIE31GotJXawvpuQhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=GzSfeMzqUA2jcbdd5443tHWpeG_1T-MhSJ-4N30qGNsnYFe8b4bJFcFIciI3LmEFSkOtOq2QVPO1H7ppWL5aOlvXi44fuicdtWUoJkiz1jli3PDxd2n6hT-QFcf77V69G5BY-X8dbKb2IG9yxjlpHsIDxSE6ZNSZENQpKKkWE9d6GOpj1nP2oQZj2GqqqMx_BN_nDcNafaSgU8QP9uNLmGUgQC_6kUSx0wW1yj3JbPsx9WhSbQMajH0968mP2W58M79W7us9YIcM2YPVpqknFzWxOp1jiBW--0Op1PF5dR87u0FfDfW-YnFHvFsIFggR6higdIE31GotJXawvpuQhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=Zt5cwJ_kRn-innay7V7T-qnY6ThwjvRWCY3cFaCMrdRtiReQhgEfvfZkclmIbtbMjJZjWRthEuNKWDUIXuT0KoxsMX2DMTzs8cvjEfZBD9XsCJqd4l0C4a42IQ1dEaGyKzVCtsklc6rvR7bQ54v0KOE0kpiOgub48s7S1UJPH3K5k6Vp5aCVBjH48eqch-bxKu2S7THQyUg0vEEHv1GDYPYn2ktL2y6yjKI5A96gHPhfsAmQMjEBLgSWvFRBE1zTbF_9XU_kJJI-_auomfFImAum7yQIXY7XkogSs2d8pJ6AYpzrxnka1uI7vffs3Xt02OfoeyT_j8E1eSw_m3wAhiuGQAb3aGNlH-Og9ifU9kPot2zyDtXKmJfrvIXTAc8u2YFW_pU8mMQZDxeSHvJn3OpO8K7ZWML08tOcah_ny4cfLy9qfz4b8S6QCpmXc-I161C4jTfeGSP8RjBZvrduOe9wqU3yP_koKSImPNYKURWksuvwGajHDjlMMGo51UpPXHr_FNVKUyCbRQcCLvD-_qT0L3nWt_8Okw0NRG7h1k2iaac6qz_EOzYfnskrGiecbBpUVkluIocTmu4xCQPzXWUkU9Uq0xFV0zm_ZS3rjqWl9lFfn1IPjdm0kD1r6HxMoo4kQlniJeVmTTt8bl4Fnq9y2JKsv3yBOjaZfqhBOo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=Zt5cwJ_kRn-innay7V7T-qnY6ThwjvRWCY3cFaCMrdRtiReQhgEfvfZkclmIbtbMjJZjWRthEuNKWDUIXuT0KoxsMX2DMTzs8cvjEfZBD9XsCJqd4l0C4a42IQ1dEaGyKzVCtsklc6rvR7bQ54v0KOE0kpiOgub48s7S1UJPH3K5k6Vp5aCVBjH48eqch-bxKu2S7THQyUg0vEEHv1GDYPYn2ktL2y6yjKI5A96gHPhfsAmQMjEBLgSWvFRBE1zTbF_9XU_kJJI-_auomfFImAum7yQIXY7XkogSs2d8pJ6AYpzrxnka1uI7vffs3Xt02OfoeyT_j8E1eSw_m3wAhiuGQAb3aGNlH-Og9ifU9kPot2zyDtXKmJfrvIXTAc8u2YFW_pU8mMQZDxeSHvJn3OpO8K7ZWML08tOcah_ny4cfLy9qfz4b8S6QCpmXc-I161C4jTfeGSP8RjBZvrduOe9wqU3yP_koKSImPNYKURWksuvwGajHDjlMMGo51UpPXHr_FNVKUyCbRQcCLvD-_qT0L3nWt_8Okw0NRG7h1k2iaac6qz_EOzYfnskrGiecbBpUVkluIocTmu4xCQPzXWUkU9Uq0xFV0zm_ZS3rjqWl9lFfn1IPjdm0kD1r6HxMoo4kQlniJeVmTTt8bl4Fnq9y2JKsv3yBOjaZfqhBOo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPyO5MTobZgFw1hx5NAEQmqftwy9Y8uxgvZPo9fqXxLvX3b0vtsPzgdRucXqSrfEfZfivGbtwG7NlMiO22B3xUHwvE2u91NoItI2V0Qsawie4BieYtQQfZepnd3qZXNJRltH-ocddQsHGxeFwdYHIbEBMF4DWvWbch8ZNB5UnvOkcWoes5Lo26TAzChxLQVt8o37f_cyEHt6eW5fKZq0PMiJnAmPzuwmwLpHrQVK05KpceTVKYUcUoWFQU_nGcPnkVyJqUMUIZjuN-m5AlMgw_N2smLqX4ODzhuSonEAx8h3kxb50-ZBBPz87EyTOdRiI5yw3kcI7DBl_w9aKwWn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-SYVqiIKdUWqyaM2ukz7YFCVPhYwhul_GxBplJY9I70SKmdi-n_Ip3FyfYz2Tbxr9Qg9JQE-s8lM7UTEogCLdRoquzqZoYrmkyuqYg12LduFiHiVn6i5SR343OSgksV2Jj7fb4kb6DrDxa4Uk8POTuL1w50H_mTHlWNi5HquY3nIuG7TZqwfxCTMcrhKwKqBpY4wz_UjH5DSh7_WqHQ31awI9R3op8hLe8rfnn4V9ojy-B0jj9nxkiQVW_vCRXhRd6FSDpRzIGrsE9k6-rWilHqvDXEmqVdPymtfkm5OZJ1WqWIZ-6n7eCuSKM5qIdrZezyb4RV5KcyY_goy5gAOOtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-SYVqiIKdUWqyaM2ukz7YFCVPhYwhul_GxBplJY9I70SKmdi-n_Ip3FyfYz2Tbxr9Qg9JQE-s8lM7UTEogCLdRoquzqZoYrmkyuqYg12LduFiHiVn6i5SR343OSgksV2Jj7fb4kb6DrDxa4Uk8POTuL1w50H_mTHlWNi5HquY3nIuG7TZqwfxCTMcrhKwKqBpY4wz_UjH5DSh7_WqHQ31awI9R3op8hLe8rfnn4V9ojy-B0jj9nxkiQVW_vCRXhRd6FSDpRzIGrsE9k6-rWilHqvDXEmqVdPymtfkm5OZJ1WqWIZ-6n7eCuSKM5qIdrZezyb4RV5KcyY_goy5gAOOtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFjOwODOwNF0KHpvvnLE2nBYKiODoPm4NUaj7feRDiy8wNyyRsPB0XgZsfpeScM6IuKI40ztFQkb8Fhdgjoa13F9hug-ErOG5idZe6xPk0nulwezhCy08VNF0I55bQtbERZJcZ7IhErrnO4OOWGcHFQU_wVw4bxFI-bpaSbEKzGp_qK3ql_TWNXhiBJLQPhLzHKgM28uvsbGUBBqqf2jMfKEIB2QGCMcDGRpfrb-7lzV7a0UgBwlF_L-7IikYojSpSukO6hMuD8xgZb5gHpgwvn6lY5wya1uF8Lac6psyQfYY2_xgjRdLWp9zKV_TP24itR66heNiToJc1akRSzHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fj9ctnXkw0-f9mU4FkLNw_0pr7dq0VqQk1iIcADjWD_bYOGyq8p80rB2BietF-z0ljjPPXSW76ndct5YpRcVhfMWTupdi-EfWPjIWJDF7WMIcu3FdhwBU9UYIctyv3UbZL3ZM1h8oXkm2CxajNYvYbc5YSRneW8Rdwg8bafp4KBdXjWXSAbhwkQdb9mRkJbA1I-1Q7Jr6yjCKpZJB6X7LVtU2UqN8UaHwc8_25azr4Jn5FY3hotyrET_1ThEjFHzrhdwkXd3N-VItL8gcesTokzJ4I5owLeQiDvnyUh5G4xgzi9-xRPMap6QAj7zBw9pCEsxdqWqmbC_YBxDNecI0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFKfbxDTMC8ejk6knaNpW4Dok5Tw067mgnIucT0CQRqKE4iPP0fX0H9GU4SfhRJol_5G6mZkpqKDJnKcsEOFAczv1EK8FIHxwnBHL0E9NIUTIdHmO9naWTwePHXBZGxZTJCfCsUkxG5sFWdeiqbE451d-H9W3RzO_y-u0LJr7tpCwBCqTihO6dmKAd3a_h8t1zNKs92jNLCDh8Cu4BEAMHXGEUgT-H4o1qtuap4j3x9INz3wecQVP_I_tfqubNCo01PYgsxN-g95Vtj6An3x8poQ_ugY-EemnK07VljGmpQEUfz6VHqeih8poa_fXcBAW3cRh7JItkGqR8PtU-_Q1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoSff1BLCpVfblTfbWsB12jjRpKA4l5iBFmBVGMg2YKZqT606ZeEFET1U3nHcq3hts6vbYyQM1L08ILDg7tYFWEgCmAy92XApDaCsbbIufjXQk_s2Jhs33B9UV11Wtv7R7J0rrWdovpObWyGf9K9SW-eDa__v_BrmbMpuA7je1UvicU7yoP1O4j6lvJLEaKpXLVdEEL7hzfjlv9Y0GIjeyKfIx3A6S0NS8v4tAivR8B8SvAixWgfApEsD_FsWDWkCck0vpvVjv5yh_AsyAxfY-iOTJ5D_fIz2nqIyXGMxc0JseFoICs90UEsFGxXCBqymcRH-n4qB7v9BjK0eiBVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pucwJSQgsGlaa5F0verQH9LHUQPCz95X62tJ0Vr4KlKZvLn0suRoXNyy4-EWKbjKCQwg3ICvh1fD9eYCYfIdcAoXGRkMPFL-KC6Xl8AbcCCYfSF5WlVJem3UBYKWmIs3uODiGPeN7utVwLLwNAq9v7pz7criD3aZIyzhzLBZLGLTlmRLKftyx7zbXrJevIx09mPzB_GJBF18OGvhpKvx0CmDA0L75YJb_-EMpJDiqbCFj-l6YO6pCPA97awFt6ZSYObXuIMNe-clnZAM01NVTJLfYP54vX7tTCN3mjCZ8QOaAlzquE2DI7L51QWeE9U_zsaqSIX-prn_geQ_IIiPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPeMg6XPN9g8KD5FXfxwPnpcLavKLgy7m9Icf1y3__YCy8rS7U0R78wkYmhpxGrvah3BSlH-o7k3liNFUrVOItO258VAXbMG79OIT4V8kB84A-Suid835asJPR1OAfa8dM6ZuFO90wmwpCFKjvSLfLuSwuoNaEHXA8UqmaozZ_KBbkg_DTnRMw756xdvjoov1yv232AQTKn2a7edwNP4cI0vt9g3mfD35xboVsbcI7SIsY-eUFGYNBcjWiLvx7fcdhZzSas5BhqHf7HsZGOU7kHbJuHWClt_KwEN0p1hFMmtuTl4gGdtAniFFCYTsfOspVSXQmaHxzKmSFat2oLrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=FB5g9AbkUyaPtTc9WESGY5EN1DzDeQiGkNR1y5U_K6XY0O2ezofqAyKVO6YmOG0zyMuFcr_-X2BHMMD6CCE6Tt98DU2rLEaM0Z1ls6tHv2K3NP63b-95nf5wJ9MSIbBlr-1J_Kj0_xy3sNWor5nuP4obhCiTTSUgOgPolEJOdNadJNOtX3UT-kUMXEMXe0hVw8oNMTqzL3Gt2Ss1OomW3xlTpERhjrxfYmxcFruXjghnPCwWm90-y8McjLr3DNGHl4UeCt-XVVliEqMfTy5vQLNUhH0OW-gbUBlb8ht7tkxkAzL1dVczVKDuRwKubz7KtDfsrRE5dR5j1t_caLpY_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=FB5g9AbkUyaPtTc9WESGY5EN1DzDeQiGkNR1y5U_K6XY0O2ezofqAyKVO6YmOG0zyMuFcr_-X2BHMMD6CCE6Tt98DU2rLEaM0Z1ls6tHv2K3NP63b-95nf5wJ9MSIbBlr-1J_Kj0_xy3sNWor5nuP4obhCiTTSUgOgPolEJOdNadJNOtX3UT-kUMXEMXe0hVw8oNMTqzL3Gt2Ss1OomW3xlTpERhjrxfYmxcFruXjghnPCwWm90-y8McjLr3DNGHl4UeCt-XVVliEqMfTy5vQLNUhH0OW-gbUBlb8ht7tkxkAzL1dVczVKDuRwKubz7KtDfsrRE5dR5j1t_caLpY_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrnK_z17-Av2OpTJtZsiZ9naHiT_VXbXCrFDlxXFg6PI6m46TpIRJRTvl9rald6IloTnkpQRHLUaurKLJcov2YnHDdaGhvw9bGuEsMGkCUy6ozC5f3Tl7Mrz73bSU-8GvIR7w-V5FzZSLmwV7qqFjAOnNcTBuNGiG-VMLufWMJgKcuDIq2xmYmB4XsDH7eFLQwRfeO5B0ritfVoMyNIs4YkcuDO0WBd07PiYMmpa74DAV5SSc-Ij4-l77rN8sS8mK4dzkYV3etpqtWq0mLadvJwNfRqYseB8dqDzf7N5Z_uoVV1PSGjOCsu-ZP1qvNGQ-5GYM6WBaJpVZAT13m3Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAh2WdycMgb83QdyaSe-5xdQWq8B_ATNP-73A_YMxO3ohl6_YBW_XLW3avcECxrt4onCaWanOD-AEjvcOwiCDdm3ZEkM8TcvDLWgskFz2YdkmcE9ZmrcAD4qLDfDoZ1KblccjaY2p6RPMb_wwEWvCU47GmIL0Hxrj5EISB2jV6YvPoYYs_63lRPM8Kpzx9jUVujTKeusrEzl9SS8Cze7jA9NVYJZn734pFscjPgSVuUMn68hefqL-OYVz3mrwcw66Pp_DFmHl4lfxoQP2PkMYf-oh7EECBivRoyZoS8AVF8ejWHKIeBmL2YGi33FdJIIGlK4gq6ElwUGAhVxUSrixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n94XM_txSlNnFFqP6u66V-K6p5uKDOoUYFO6agGkpATtchtvjKi8WrcfVs7Z6bmA0dkCRnRdUvsLvHlRlU5umGalbq6Q4BO5f5ojvhPwmhhD5w4yQdHL3XJLfudDPdEkQCy2yhoNuodutOcD6YGIjutQSc0wVoE8ZA6WdqsYlyrMt0faRO8fQkF9KiLWcMvZZk24-BcX2c6HmGpNZofqfUTMXiPVDKMkeRhR_tMUfbW6K_9kDgV309uBsl_Ll8mAjIc5HYjYdEidhUQLKxImWxICjSVn9MXilcsmJi6TNn-w0WI0-10y1A3z2PPRNqoHc-8586nJb2BewSGGLjJfDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=nERFSXUjCj375HSuY-CktqEQjlN73GGaMOma2cID_Kut6mYOiqaDjD3zelbHSSzDo2Ss_uisqFnDG5mBKoZrAoL8Y8hXJXUCKAEoQbBvHk03-u4xyScyvRtxwAo7m4bW8FR75qUKJA1xmrE2PbyFvMdupYxG2a1qUtIOvFZcLFNJFfAFOnQs3EPVAzQuXectQStVke9BeFf0B8qk0EyNEGH3ksz59hPQkyrU36O32OpdNbJuNn4KI-BM7pAAcFxXBD3uHUug-7-jUilHhachz9-lUeQ33f6C53x7KjzPMzNnvto-c_bmDxKIbe7eCDRioQSKHLaz8l-VuhGIWKBxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=nERFSXUjCj375HSuY-CktqEQjlN73GGaMOma2cID_Kut6mYOiqaDjD3zelbHSSzDo2Ss_uisqFnDG5mBKoZrAoL8Y8hXJXUCKAEoQbBvHk03-u4xyScyvRtxwAo7m4bW8FR75qUKJA1xmrE2PbyFvMdupYxG2a1qUtIOvFZcLFNJFfAFOnQs3EPVAzQuXectQStVke9BeFf0B8qk0EyNEGH3ksz59hPQkyrU36O32OpdNbJuNn4KI-BM7pAAcFxXBD3uHUug-7-jUilHhachz9-lUeQ33f6C53x7KjzPMzNnvto-c_bmDxKIbe7eCDRioQSKHLaz8l-VuhGIWKBxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=HAwuwWjcjPVjcT8WM3MaLeEiE2lkj_Qj5j9ZEZ6X-QH4tZPi6b5ZBT0qiWv_CvBBpe22MFPQtADQII0I6D1mSzV1t48WYviwDxWfP7byWlEj7WsFHvusVaByL0nRdsTkDlueOV5maEv-uwb-tgH6cpyw2Qq9S6OxKy_Q1k8gexd9jmL3-g_XGmE_GNgjg54tEkeN5L4D8NjYmneYkZkB1pn4UzN-zRaHuY_8ymQkn0M2SGI2dZnWkpnJzx5lcEeZnT6H8uJ5gmPZsQxO5V1RqQp1h29IZH7nVxreSAjEPd5Ecsu_KyhX6P88m6pa990xuH5GXn-kpPoXnVVfzE-BAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=HAwuwWjcjPVjcT8WM3MaLeEiE2lkj_Qj5j9ZEZ6X-QH4tZPi6b5ZBT0qiWv_CvBBpe22MFPQtADQII0I6D1mSzV1t48WYviwDxWfP7byWlEj7WsFHvusVaByL0nRdsTkDlueOV5maEv-uwb-tgH6cpyw2Qq9S6OxKy_Q1k8gexd9jmL3-g_XGmE_GNgjg54tEkeN5L4D8NjYmneYkZkB1pn4UzN-zRaHuY_8ymQkn0M2SGI2dZnWkpnJzx5lcEeZnT6H8uJ5gmPZsQxO5V1RqQp1h29IZH7nVxreSAjEPd5Ecsu_KyhX6P88m6pa990xuH5GXn-kpPoXnVVfzE-BAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=qOKvC4GqK5XvPYVl9zWkvTrOIq9Nw7d0Dl47Htn7wnlGoArvkhm9uG-gU0xqO4UpjWlw15ulgwSdHyAgsKWDaPm5tmGgrQE6rKOQEwAcyJpHvc-YBcVNKWvR63_NOLk1Nlu0te3iALMgAM_ZBE_vT5edbVVocl0DPupYpoUpn_eLcmG_urMNmAOpRZaEs66Wx0fNxqcC9eYJS6YszX6oUK52UaydpDBaQMzw7Q--oN-wf0qMPu9RxOD4nZhgRE1N3yKfhNxPPYBGIF_r0B1vFPWwFnPTJxX9QT-ia0USWHn-ZVCnjZyeeQruuHyfrXDMpAAD4coK08UD567bOqR1X0bikrKTupUqXU7hQvpEuAsMHl4EOHzt9axErm-CE1hs-1ZVXKqcPRKq-jmjAEG-lSb8iw2yP52ibw_qNpXU0My4StPuFGIMHYaCS0DEt_Og9ps2ccQyzZo9ttQuH7MavAITeb7vHZqnfUpfd54lTwjCRCOFRZWXq3pSJejiFVg7QvsfRNLn-OLP47XUjVvgRvSOYZ58dJ-UYVWZUcr9QTtg8OwuIluoMJQiqVqpwboABhh7DWoidQRd3p3QMOM61FS5kzsCVkIdd-bVsu9I1rc-fJzXHMPDB6bmBThb_BLhYgIyiQskuUupXu3Olw5SFxfLrC46bJGcaWFHLmlC4jI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=qOKvC4GqK5XvPYVl9zWkvTrOIq9Nw7d0Dl47Htn7wnlGoArvkhm9uG-gU0xqO4UpjWlw15ulgwSdHyAgsKWDaPm5tmGgrQE6rKOQEwAcyJpHvc-YBcVNKWvR63_NOLk1Nlu0te3iALMgAM_ZBE_vT5edbVVocl0DPupYpoUpn_eLcmG_urMNmAOpRZaEs66Wx0fNxqcC9eYJS6YszX6oUK52UaydpDBaQMzw7Q--oN-wf0qMPu9RxOD4nZhgRE1N3yKfhNxPPYBGIF_r0B1vFPWwFnPTJxX9QT-ia0USWHn-ZVCnjZyeeQruuHyfrXDMpAAD4coK08UD567bOqR1X0bikrKTupUqXU7hQvpEuAsMHl4EOHzt9axErm-CE1hs-1ZVXKqcPRKq-jmjAEG-lSb8iw2yP52ibw_qNpXU0My4StPuFGIMHYaCS0DEt_Og9ps2ccQyzZo9ttQuH7MavAITeb7vHZqnfUpfd54lTwjCRCOFRZWXq3pSJejiFVg7QvsfRNLn-OLP47XUjVvgRvSOYZ58dJ-UYVWZUcr9QTtg8OwuIluoMJQiqVqpwboABhh7DWoidQRd3p3QMOM61FS5kzsCVkIdd-bVsu9I1rc-fJzXHMPDB6bmBThb_BLhYgIyiQskuUupXu3Olw5SFxfLrC46bJGcaWFHLmlC4jI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijb0wRcXoJSJN6D5wkMl9pCv372JqATnTOJkwgvNzPYcd5LXtLsXgvN0nv8NlXRzpYLTD-fRpuU-CDTdjvMO8-C9ESZ1nz9Z9IG8ngAFVptB_x8YN9YEcIhdu332iebUL8Ds_J9oXmd3rUCwjRoB21AgVSCMI96kGgt6Rn_5DNec2SFt0y64fJyWPTcUkQrW3r2f1HSKwfwnbPMrT2iPrmF3HHFYAfuEuJNjwLzNeiKRC_PqRXwwFBVUx1hPvy8SSpfkKG8fSVn1zdCfq3v3OVUjki5Oxs-foXl87vVVZWdjy3n0ei71boeGqVktW3Dqw--Bw1S7lfkMqNjrOBX7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFUDdUU1g0TRaVEyihdih6AJyrxE8QHVXFDLSEMhVBkoy5ZiSx8ow4wkIq9SH6LBZki6gPTC8vciXKNaD1VmVbp5oIpoNavgrzgLypyunA-1eFVKXG0qyIU7Gte3SeqP79hO-LmC56SRDU1zbKaAKfvHNsxyS1SanZhLfI5PLDWRriqs-P-2PYCcKlHHfgfsOxUjv8PdY8qnrHHwu4fO7wcyiDR5R36Y9ApUudS1bkFRigHpWJ-v9wXJFH0oqWOVjpT1CB-qU-PlDhaw0N8GazzQJD_19Ahtq9lhybW31s1uUws4ay1tUhloMy63OPdRY5Zqak-18cQ05DKxKtDKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=hAF2lfheAhcIg9j1vxVYBL7dk9x3tBzYJyUMhZsMDto1sBZMeVTI0vaIlCfISJ7lsjpyDl1-58lqucLnhkNDJkgcIFUZeWtTGBNt3n28j_KEoWnaAuAtMIAy-jlYWcJ_y1E-yTZvKuDB4uGcUdOW_PtWXfKadgyJcueT8KNcvAhqiEQhvoyOOZBUwazteOyr1q5TFpvG8Vf5QS6q0d2cuFzAWxJoOu0Js8u6QUgo22DWuRiCRCSMsN5uyu9lT-jn8tqjaeIsHO7cOe1h9y-no5vs1t60AhvALSwP6hO5TUoJvZfWuiL3fBKuMCEXse3yX05Sd5KLAM-XLWhZ8_dJgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=hAF2lfheAhcIg9j1vxVYBL7dk9x3tBzYJyUMhZsMDto1sBZMeVTI0vaIlCfISJ7lsjpyDl1-58lqucLnhkNDJkgcIFUZeWtTGBNt3n28j_KEoWnaAuAtMIAy-jlYWcJ_y1E-yTZvKuDB4uGcUdOW_PtWXfKadgyJcueT8KNcvAhqiEQhvoyOOZBUwazteOyr1q5TFpvG8Vf5QS6q0d2cuFzAWxJoOu0Js8u6QUgo22DWuRiCRCSMsN5uyu9lT-jn8tqjaeIsHO7cOe1h9y-no5vs1t60AhvALSwP6hO5TUoJvZfWuiL3fBKuMCEXse3yX05Sd5KLAM-XLWhZ8_dJgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFSPPQ-l0IlDch72nZ1t5eksOzKcPt4lRASObv2FnEdrxj1AOHFB0U2fYKUZ29D-YoQkL-zuqvM3A8JDGJJ-J6gy0a0e9Lhasx-FO0MKGiwla_rGrS6cC5M3iLqg05Wr58P1TKzjViV-UiL8jSw_nm8lnd-joipIRaXHIIUPy6uHomBYCH19rWNEUMMg_GMZwJ2GCVVhqHRXhNc9DkSVPSh5dBHbrjBdYiX3megLpuS5OsfGRLosOSKLlfmRPUi36tA87FGf0TbqpJJ7JP1I156VzIbWoU4P2kqh6dNN8JWeUauONC4V7u5QQWB2GJegv0qdIvbN1f1BRf2Dge0DHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=ebif_aSTKu1NFwmKjV0hhTUMc5A1M2APcKVV5c0Soum8GsZL8pvupPk5xAypynwI9UdktEsHe4NHkVHZY63IfxVdr7ibHAzM2OnsP7AFOBRu63gpOd8sy9WvUvXglkQncwMWiW51NHFI45YgqjvQcxlgLOsotvgunB4poQtpvnP2UKAmPWnK89DUXhFc0k1WJ3mxA0YmX_yVc4WpUqkpzPENYRO6Qz0EUmCMCF62n5mDqg7DflR47-8ao5H0O3oaPZrAznkl-3_3wwNBMilzcMe-J2o7AvvMGms8M__1VGv_VexOUxJlqndQNGWVQOjSPk5P3ELnYbrLGPya-XkiLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=ebif_aSTKu1NFwmKjV0hhTUMc5A1M2APcKVV5c0Soum8GsZL8pvupPk5xAypynwI9UdktEsHe4NHkVHZY63IfxVdr7ibHAzM2OnsP7AFOBRu63gpOd8sy9WvUvXglkQncwMWiW51NHFI45YgqjvQcxlgLOsotvgunB4poQtpvnP2UKAmPWnK89DUXhFc0k1WJ3mxA0YmX_yVc4WpUqkpzPENYRO6Qz0EUmCMCF62n5mDqg7DflR47-8ao5H0O3oaPZrAznkl-3_3wwNBMilzcMe-J2o7AvvMGms8M__1VGv_VexOUxJlqndQNGWVQOjSPk5P3ELnYbrLGPya-XkiLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=koQu5EEVAtsWMT7x86pjUCEQkyLLODBfz0RXpReL3l_ztrn4j9fwdb6TX3adl6tDVGTOxXwDBtfiMlBa0mK372_kgMvyIzrFDPdqYHMFCcUMqcMePoSoTnyKnDDKt2beJ8Yakny_40SvEt9qAijtO9a4Y6lnlQq3kk6dAu3AE0cy4I9z5E_Slxz_bc_A37g9KaGF95gHbOm9vCs7EpnyV-f-fqzPRJ4x2jGmm0sEQd5AD_KADR_EfNDNOgY0gfKiD8lj3TrgnviIrqkfj_xffNs-dy7Knk2_AHE6RbArYbaXC0DfdZW-HvhwzOjsP3E_Z-JsJbbgbPtdUGfIEXIjiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=koQu5EEVAtsWMT7x86pjUCEQkyLLODBfz0RXpReL3l_ztrn4j9fwdb6TX3adl6tDVGTOxXwDBtfiMlBa0mK372_kgMvyIzrFDPdqYHMFCcUMqcMePoSoTnyKnDDKt2beJ8Yakny_40SvEt9qAijtO9a4Y6lnlQq3kk6dAu3AE0cy4I9z5E_Slxz_bc_A37g9KaGF95gHbOm9vCs7EpnyV-f-fqzPRJ4x2jGmm0sEQd5AD_KADR_EfNDNOgY0gfKiD8lj3TrgnviIrqkfj_xffNs-dy7Knk2_AHE6RbArYbaXC0DfdZW-HvhwzOjsP3E_Z-JsJbbgbPtdUGfIEXIjiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=e0DeHvXtNeG5vUnRA9_6V1uXD1YTJ_8WbGxM15Nr2kI-9qUsoxBP8k4mm9lfjtYyxWE4qxfV1Wo285dkCTtvmGYfx6eRUh2OOhUe-UTdQWDF550lCwMbyUzCxM59DBTN764tDWPEzCjslcBsxwHpWpVcP3cEzR354-CHeg8-K6sJ-gituxF551q7ORKhKy_Imcldyn8uPNoZJsTp2tiF9Ce0el2MH57ql8KMh6i1u00jeNy3lqQC7zSOhIL10bFKBvS4nLVgWJeXbzV6pLqReI9ptEJD2MNcpphcqvnUtGdY6iw6_dWUlz44J5XdiuO1yQu_X4Qm_qwUCyk5fLr5jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=e0DeHvXtNeG5vUnRA9_6V1uXD1YTJ_8WbGxM15Nr2kI-9qUsoxBP8k4mm9lfjtYyxWE4qxfV1Wo285dkCTtvmGYfx6eRUh2OOhUe-UTdQWDF550lCwMbyUzCxM59DBTN764tDWPEzCjslcBsxwHpWpVcP3cEzR354-CHeg8-K6sJ-gituxF551q7ORKhKy_Imcldyn8uPNoZJsTp2tiF9Ce0el2MH57ql8KMh6i1u00jeNy3lqQC7zSOhIL10bFKBvS4nLVgWJeXbzV6pLqReI9ptEJD2MNcpphcqvnUtGdY6iw6_dWUlz44J5XdiuO1yQu_X4Qm_qwUCyk5fLr5jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=Mgu9qsSxhmTV837TWffTAaPwa6UoZChwv5eDg9j0HCoU3esjJoDmxnxJNKfxjbeSK3uf8y3GtEJ0sMUfpUsnxi65R1DG6tBpUJa70WwF37sYeKIvJAcCyNPVifRpFlBnitvsXLmxQZna3MQN3gp4SXRlYiFcMMkJctSyFvkfHArW3VHZgDNrzWzmYZUeb-gt7ea_jsw8lkjv1upudvdXavjyMrIJxfAnP9bp--4aifV9Fg_XoaGLJKVKF8o_DLh8mJq4MGS5kNt6B_SYnxODNSBC1RPKtzIJixf6Pp3KkYC9C-2n7hIZKP-CK_b1QMDRTYoaFy4dyhhkP_biel0pTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=Mgu9qsSxhmTV837TWffTAaPwa6UoZChwv5eDg9j0HCoU3esjJoDmxnxJNKfxjbeSK3uf8y3GtEJ0sMUfpUsnxi65R1DG6tBpUJa70WwF37sYeKIvJAcCyNPVifRpFlBnitvsXLmxQZna3MQN3gp4SXRlYiFcMMkJctSyFvkfHArW3VHZgDNrzWzmYZUeb-gt7ea_jsw8lkjv1upudvdXavjyMrIJxfAnP9bp--4aifV9Fg_XoaGLJKVKF8o_DLh8mJq4MGS5kNt6B_SYnxODNSBC1RPKtzIJixf6Pp3KkYC9C-2n7hIZKP-CK_b1QMDRTYoaFy4dyhhkP_biel0pTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVj2_PaM3yT2I1Pxd_j8C6vTdVeZxXRE5glCXAgH7W_EEHXJyYDW8zVE7uH8TkDOEcw9DkXsWJKr9UTvRMoRo1_QCHkPnYHi18ghOi8Auvra5zABKNuRbgZ-unAMx6drI7zbfhzRk-86qVp8C1kVZVl6kGlvnzN6EoJjCnjObOcFeM9f9k909Vdl7tfkf0yIp-wtizEmtJaVgq6O5vycw7mNx7ax1PG_Y6lOVGbVycoc9QL6UujawmMdvCMelExujm2SEVRse61cR5nu5CMxu6aVACgMkZELJKNZ1ksg8CJzVqo0gMoYqVF7N1Qr6A0YMQPAz6BLu8Jishy2nYu9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnMe8JXyojddVBZWkrrSp5OBaPZRKMK6wE8O1u02jhePgIS83JqahDP46ibZJ4sNbgHg7tH_3evdh_yjP0b2PCTDeiekdVxNaANTDsBAecXHc-gb88bOEKX4w8OaOJS_R1aYYyuhlyTmjjt8yzgAMUvr9YtQ_uraFextpKF14S7Gx8H0BXKSaeBKh2kzXhYm1y7nhgEdnz5-4IvFk78zKzqGjPxxi7bgmtmIWPhyr7_3Z_EePzhZmaKBZp9XrnVXvSM1h2YEQ_DzeD8yr62-Ko9dy6G_9bOVOi6efKBDHFaucr3eCnkdkNAn5g_Hq3OhEDORH9ih2xBurkZbwr0gQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8w5pNy-Ek3o3R1oK9XBZGUoz6bE1CuTowCTdnszJPrf7Wa5SQyYPATBNOMdJZeoUGf_M6je6goiTUce9nQgTmELfUhYbXwQpu0r2jVIk6NtHMe8E23B2u_KUW9Ujfy-p8hfzgQT6aZ3ugfl4pdWJBRh_26E8-ayj8g80E5QWQKgpOg2d552HUEVTJpFjEOhGu_FST987xnr_hYfDB39htbHEoVS8opIVqC1hX_yEV7QeMqCgX3TQyc8nbwD3N-Yge5By_Cyp9RpuME0Xb4fLOQJ_msBcdOU2khNI3Vf_xc3K7sp5Ij9R1FHUbVoAsULLl0H3YrL-5JepcsJxW5iGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vb-XckacbBGuBNGtIRyPVa-dSVcTfXgfUXiqlWSjyT28ozo-WO1443Nl5Gq9enKYmw61JTVCWEaxgxxzr9wrwQbxtVToNkT8Yp4pMAA0W43WXx4qbhkwbcHqnu3_G0ZBhzeJDJ_5DWB1Ea87Tv_N18oDpa_vooxFuVcDVleX6VuN_NCro5LQcdJrBmtS0-SNrlizi1M-kknXRRZErt6ZSdku0hkGlvh-CHmZb59AutKao9iz8y_zJ20aVrbYcO_bsWwqiD5DJx1hNw45Wi339bEwz2-wzGe0cXGlzZbuU3fXBNmJNLOCYPFK0A1U1oBh6Z2Prj56oZ0WVU6uF2vnMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqGcpaXp4qL9YKdvERnxtRwr9h5M1JtkQ5TXmK6FnXW2-UTReD2Ab6QOgP-afTSNEEM2vuEKXEno-jplw1_KoOVfoPQZwLo_nHt3ERiZAf0LdwCcStUo3a-cfZIJe5Co69DGCFNq6z7h3k-kkubfGH1Ln9jKYfdckei17rSh73rzlcZ87X23WI64uElrfv7ufuxnly-aUOmmqOPFeUf-cXwMX6SXLONVWj5t92I-AlG8MhDWomF4-6ieYr1qmiKniATXoDb3IdtSkJUPg1MdMMTUqIaw_fHFe_n4-2_Js_LFdMWGmV3hMrt6CDYWWo1Qj8S_Ij1KH6HrDN71gkjE2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6qMzDuSqVjEPyBxWWNvjZEKyAb8sfvhjTWZqahdRk9Pd4YqvxMk4F_73At4NHj98cQ8BDfqsxxXJhdw6SbCTNGI9f6IWQ6g4urMm2sOHkXa6DtpVdFdeblATTRIuY7wW7FdZhGNa1ODvMETInA78HZkwVtbLqD05dHx2Wly-ibruUnvS6uW7HL2x0KMs_eiTEC2xqSBecvm2U6LNGFnfDv1dV2TYN_k-6xBlMmvbwi0QgGHFEkfyceiAdLD0bIV4NSv1Vs05dMKcZF1Z7e4CSmK9R2xQ6WykSTs4RNVZy_quXqK7FQ8Uu6VcWqqLfTobqR3H6rsS0Lbzsb-mwQ3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJ3k1hrsk2veI8qEldRUrIexxc-0mCXZCWtjlc8a9YXB5FehO4yWK-0WQghoo6iVf0ErTG-azpEhwfpt8mF_ozUTH1dRwuhYewQyteGcEqI3kgCs2yzJxBBlEcCaH64NqxQm1gcUkRfpbyp0W_9h92AXimE-NkzBvm2NHLsp0i1wSy4ukUUe02fVeT8GhoYZNew9J3Ii4fsM11PZsCBCTs05Bbga8xi13zA029dNmZmhKB5Omc0lYBks5Stbiv3skGd1D7bTSuHWb53OwLjmZ-p58L-PeSBexDXFlYhSKESNsdBptnYs-W-zNed9GZul-XoFMPR1b6z5z0sgBNEg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=snem8IaaUB2D65MYJTx59P-RgYQW10QY44rEV8B8Su4g9MA7H61EVa-O6cHu70CE3KRuWNOqa2OGLudkmkxWvYmxbvH6ILwvyngzur7bhGE1x4jIMqyz1yXCib1scdN-lTzOcYfA0Q4UxmuoxmPgYGIqouPr_d-jPnjHvZbMEEJQsWnqtTMABUDA9w-rQ2CFiW0KJAfmcZ-RJoBVB8vAqWiUzzBMuvt9nMjxeqT4wcb30R4L2T0xPn29OcgYw4rOBAiWosnUzgp1Z6r1F_Vj6N3MP8yrQI-Ie4vgVRlOhIqJuTpq6DROxGXNg9kKHWKZm5EOCkZT73euzsj5PNeAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=snem8IaaUB2D65MYJTx59P-RgYQW10QY44rEV8B8Su4g9MA7H61EVa-O6cHu70CE3KRuWNOqa2OGLudkmkxWvYmxbvH6ILwvyngzur7bhGE1x4jIMqyz1yXCib1scdN-lTzOcYfA0Q4UxmuoxmPgYGIqouPr_d-jPnjHvZbMEEJQsWnqtTMABUDA9w-rQ2CFiW0KJAfmcZ-RJoBVB8vAqWiUzzBMuvt9nMjxeqT4wcb30R4L2T0xPn29OcgYw4rOBAiWosnUzgp1Z6r1F_Vj6N3MP8yrQI-Ie4vgVRlOhIqJuTpq6DROxGXNg9kKHWKZm5EOCkZT73euzsj5PNeAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq4TvMVvlkbd2lMC0-xEac7CGBu-wXWlw5fmm2cHSgVwyV6zVI53rkpUim3zPU1HSBp_4iYB8MkhVqXKU8FGcX7jXwt4tzVD_-AxPkhXk036eKu3kfrxkjvdUfAvmE8mUIdQt90tteWHEb4qywFu-lqDMDZLi0Z6TOEqfhuqrYSVPR6VJk4BDBCbROifQliaxQo1qOV4ZD8qt9Y7PcvoGELi7Zc4A-XebSeBrCjsTFs14F8yl0auod07B2m_uxK_yV_Y8R_ardNcvNar2pbuaO0SOWctnvdQpIG4YpLkIG1DR9JX8YK6o_p89NKhz5lcV4E8zwd0PgEf7wzVw62neA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm_NWXY7vXs7xjFzIXoR2jmJsoWEQl-4Z4faa9q8QqZHPWziN2CKsmkifFWNlMxkeX-xKOwGpXpe9R9U8C_Om7jSoGbsvbxsWGtuPGJ8GFAaiwO4UkUBfZ3mYOmCHLD9AMzWwSiiX3Ft4vx8JRryMtRm5PBPzXx7hYyEDro7N3oJOO9n_OFrzbRkKQxhQ-yej1IrsnvRoBgMwO073np5GaaC7QhXJ7DBGklXY9AeMkkn_xEppWXFvFkkVONPFDb7SR0BrKBygN89v-qC8T8Osxt1BfhK8KiodgC8Xx-swC9xtmsw7Uar0YTmMQAsUu9MK9iwPU9IsK4mSqMNvRto2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcND1PvZ3LtrdwBn7X8f1Bd2zRrJ9hiedsrs2NNPnALLgZ6y1tUPO6SYP2BSAyBSjr6ddTXHYQmqh0sEM0kQvKV3tNVvIKQ2vUGoT8741pg3L0i1ERuZB_69s-q8MBfFh6MQKTQ0DCytGcMjRMfZli7x27WkPN4JBTZA1OK49Qj8NNOFBsQX5S8ft_Ra5r1-R0krudI0mrQeK61d8s49jgZgv1PdfoJYylERQtIu8Qy0OXcPTAKGxjIAMvoilZsz7PPrZNSmBLgC7j0m2J6lvxLWuEobWmiV3xaI-urXZTDS3to0Tprf6H356TZdzlXsbpp0c32-hHRYReYO6OgOhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPPHpEEHDbBUjjXO4OabKFCA2sibRq5t9Te8NR8314tv4_cfL9h3yPZa7zjrIfInSazYkoHhpyM7K2uT5MlOIBv5qOM9EUB6iYNrzZuEfPpvmWzj97Eg61teicN7pX5IJIYEbfMwX3dFGOpo_m39NmtGPOMHBuXjR1vXfmOhTCJ-PS67qNLyw9oQsyCnqdv_ayAsSpwvKIB5WgYKDihlqDV88918ZZOuuIy_yLqCCTZXZ4gh4wrTtvdrvCN5F2SxuSdEkmML5IsH8B2MJSgDai9eW1zAVb7crFBdsEtWvD0P6CG4rniNsgFFut95uE7QDxsUNHH33sKNJ3jubuoPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBfXhq11RZgvFB_-yIUhjQZ6yzqFce5m_xHFShsHNKnlgAcn5N8Y9Mcn0uFKRx0sWN1wUZ2zFEhsX9shWnIHIMiBl7GynNPRVzyx7yTD2VJNrupuY31ApsUD3am4o9mgLkJvSlDnj0jEhV3clcZJPg23NifRD17fOKRMfIjfDWix37C1zbi4uwXdLLE5VePX3WAAp-z4qBdhgjWVN_OPU3XacNUxrJU7yScKErVTFrEUxUZZOoa03AdWLcEnt2aV30MUUJVXq1_OomGAeNRIUd8t4kiGQCVEFKTvcivkOFr81wSdRP3JUwD0W2Kf4hSWWh44vzGx0TKnlr4L00PP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWZ8th2kpN9NFCm0lfQ2udPYuVivroeRv_EFFi6GdSDzsk7gkQU-Jc7cyInur64UXGvXJBqF10KXJpWyBqtJVjn7v1WqzHa5wVKyUjoHDGQ4B_4KvgDMJ3ooHdApx1aAqn68e2yVlYMFf1ad7-B8f4-HqFgKTmswS-5yHK6U5RXL0mfY_JbrsvwibUmYFbGxZ5e8k5TDZ4h1fDhfV5JsvGMNR_qZ6Vs1awIFnMD_aN66IwVfFe12MZK4RMGx59wcgFQF6Q-w6AAYgF1bih6Bs7ngZSdTWtPKhfbp_LxcUkTrNfp3WZSZ4K2ayTSPcwH0kduT3Ujh9k0gPzYV7t4CtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wx4D-NDatfezZOaxe55QOQV5TLTP0_1YUcO-i9earobo3ugk9IGLgxjyLT40QJZzNMl_AywItnLpuePedZYcWRjyFZlocwVGVtvxsymbgf9Yc790cCPaAq_YYwCyF_jy9y0S3VSho93IfUXHatcx_x-m8Y-bW50OBVH_d7nY7ZIqE7Zj5tFroNh4IZRPlUR8EWMGYuScZNLjbJa401jegy0D2RuVIHsp1VrF-XNC-Lk8Lj2OppI85wE5QAkby8edt18P_jJqVsiizwilbHSR5_WSPEPksQw8i5Y_2oTBystrFNvEd9OzWg5nimsHnccnU5RKDupOFZS-Sik89kBV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmI5wC013V8hVwVitgMLs0BZ43C3X0gdaqzjFLTzlmPeBblJDHsB89cnhhsJexUi5sEKMs1uJtCiDWuIZmb_As3kBsJOIjtupLJ1MMJSMLHPBvUsXGh6EJrPJS7LpM7IHrnSpyZgcQtDHksMpeadQgnSzGfpGeinbv7Z-FEYgMrqxlj2eOupz_C45zos72JaBphEw94l0064aCT1-Rmhrr-uVRCpR7MP-6mmbBgLbVPdAnRIeas3Ws-iKrTcjzHGa5qLn_FC4zmAK-cBmRMAixBuwsbBcI1dxetXb57v4C8QlDAXv3juJ2zPBqSmh_cMxvP-BciaCWz-q11tJ0MSsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=SB0U7m8kj7mHOIJpSS1DNSIWhMw7eRYibv0_ubsZPpYV72V3yt1y4SxBoLMY9-A76RImMogRnzRbzZsK2SuUEDC15MTOftXHQBJXVs6mhP_e8L8EiVRNia0CQJ7y2WadoE8P-hSihtXKsuCUNNiZWVHV0iAFLmOFXdWQ3DW1ReCXaY2WyoeXCZo7_tZCAy3tBVKPZc3xhSSesAreiG98Z_xvjJbi85qMFWzCIQYq-3zo5RxbIY1DNpJEgZZm0TgU9XTo4Q2Jn78Nqu2pDGAvxjfAql6YcBBk5RGvQMm1-PdWuaiGemQOXNwXDC8kAMxVJckP2FMcXn8A_btR_ZeHrBTKq9-9JUHJNwRuYMZcR1gGnPIOgdiy1sBwWG-iVLFPxHc4FyURiRdfXfGOZj7tQyTPxS9koNY1hPwtpzVINtUunBejKzJ1n_I4-j--nU9i2hB5ApYczFypdHO7JwlORUCHZ4wRRaqtvAhtZHif7Dodw34fT5cIcN5L2pD1Wc-51p0MxX-KkjM9lg8PkHwvkS15vHtUvyZS1644uJNQodUUEnLOs_h7sAz1Kz1GEgjwPC62b4di4xFiZJO-5y1ME9Dvp8_ZSl8ctVu21koxcNa9-vl9u76BAHdcOTjO5-sziNOIn7mxFjQOrmEpNpgE0Q8zRRRNGu1xWmslC1-5u1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=SB0U7m8kj7mHOIJpSS1DNSIWhMw7eRYibv0_ubsZPpYV72V3yt1y4SxBoLMY9-A76RImMogRnzRbzZsK2SuUEDC15MTOftXHQBJXVs6mhP_e8L8EiVRNia0CQJ7y2WadoE8P-hSihtXKsuCUNNiZWVHV0iAFLmOFXdWQ3DW1ReCXaY2WyoeXCZo7_tZCAy3tBVKPZc3xhSSesAreiG98Z_xvjJbi85qMFWzCIQYq-3zo5RxbIY1DNpJEgZZm0TgU9XTo4Q2Jn78Nqu2pDGAvxjfAql6YcBBk5RGvQMm1-PdWuaiGemQOXNwXDC8kAMxVJckP2FMcXn8A_btR_ZeHrBTKq9-9JUHJNwRuYMZcR1gGnPIOgdiy1sBwWG-iVLFPxHc4FyURiRdfXfGOZj7tQyTPxS9koNY1hPwtpzVINtUunBejKzJ1n_I4-j--nU9i2hB5ApYczFypdHO7JwlORUCHZ4wRRaqtvAhtZHif7Dodw34fT5cIcN5L2pD1Wc-51p0MxX-KkjM9lg8PkHwvkS15vHtUvyZS1644uJNQodUUEnLOs_h7sAz1Kz1GEgjwPC62b4di4xFiZJO-5y1ME9Dvp8_ZSl8ctVu21koxcNa9-vl9u76BAHdcOTjO5-sziNOIn7mxFjQOrmEpNpgE0Q8zRRRNGu1xWmslC1-5u1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=HWg8HgPHcQojVW9HgGE-kHRk-KpFN58wQMQ9Ib_ZMENQyO2txz_enZQPb_wegpvmD7USZomkVWU44NesUkOSMs4V75Ywu2PDlUqXK9uR6jXDn8BhTHo_Sw_5TP7mMJiupJFp5eKXMoMe9lH0TTDwWz7xr4s68kEsoeVfnbFiu1sZnUFgpCDSOwpHsaqBPVpHn32fMuszO_hnl2KkxuXGe-4EtZw6fbLQ8fDS4TuHr55rPp50XiJczlXAJqjdp41mpY3vpXIwCMNb9ruU_tUmVIbtLH7aH-InWOARdH8_M1cxNpziiBVcVr16IMDeLwF9KOv-bO-Ph4J0RYGM40JC3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=HWg8HgPHcQojVW9HgGE-kHRk-KpFN58wQMQ9Ib_ZMENQyO2txz_enZQPb_wegpvmD7USZomkVWU44NesUkOSMs4V75Ywu2PDlUqXK9uR6jXDn8BhTHo_Sw_5TP7mMJiupJFp5eKXMoMe9lH0TTDwWz7xr4s68kEsoeVfnbFiu1sZnUFgpCDSOwpHsaqBPVpHn32fMuszO_hnl2KkxuXGe-4EtZw6fbLQ8fDS4TuHr55rPp50XiJczlXAJqjdp41mpY3vpXIwCMNb9ruU_tUmVIbtLH7aH-InWOARdH8_M1cxNpziiBVcVr16IMDeLwF9KOv-bO-Ph4J0RYGM40JC3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEISEaKm1sOQN_-8FTacWhh3_1i612lcGytGrJ_I5zzzZ1kVQkfLTM0HS7rvWBUU2dGbwZe0zfaPqobcQb_ceRRDj4ytSMK-dfnJ9CTqMup1fTPcHBbyEON_M7UNQbiUK11jOj39bxcGtYRGRoz7nf6CHWkW1l-Ct00o_73XgyTclK6zvOc6WfUH88v6vfG9TjlR_RPhsgamMNjGTd8YLCKH-ocqaZqUKFRrNKqCyoEQXEoZzJKkR8338Kuc5IeliBrb3wHp7Z07H381UK6RMl5pE8DZmR_D1c6Ib3GvshBUo-xdePKWHKPfgTQZx7mgeXdpC73woxxLc3gL9eJ6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5PZiPmjwdKISPWJua5LiQqaXEDFlyRDUAQYKBWnocNo_WN8McUmWycY6iUHOM9J6tG4wRKm9-ykYMuzq0nuAI7wlMxRPdg9UN4-MlGwY0YmJaR8uci6X-SB9_tLdfK14J3iefvoHHgAXqBoVIk8a-DUszJQ3k4Dmjod3ABi8aIBAr3AeBwbQKb02u5uiTFJL23UuU7V4lwctcDMI4ZMo1Fk3V3jEjGmRpdGQIKo6efSc1RrZfljWh0EpxhkUgwkEdm8APe5rkNjWsMqYlMFDKOiPZ4ujopRP3k20Za9g98G-cJVpbaxNvn54O2RpV58ltv8zqBcCV5To3rj_F1aZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t20Ckxy8-SnG8Q2mS6Dpv_kwe_PhkOcga9PBSe4pyXMzl3z2CPY-f3aHHJV1uqp62uR-fuIs7mtmxHIV5VLK2NGZPIsaEshzlBPnNIjBcNAl-KdAv4WuW-sM8q6LUpzh2AjbozODBR5j1YraJKnwTXte-wS2ehEwFnJBxxdsYNYSLJH3x-ID0V1ptwkqJDFK76QFM8ofR7Dwj0HeIHuhlx65LwDXLam1T_hG0f9EmSEJxwCBKFA_tl80Ijbdr9Wfw7Ss8diixomS4fh6gb8xiFk7WN0JhvYfHfctk0d9oK6tg1fA72GBaO_I0KqrobGQhYyrn7HrQzK9cJKbN2li1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIOaGX0oSEwnSMO7lTX1eMzxG-UdePw9Rf8dDnNNawGQFzXWhSefOtiF18M9c8cn1-oiFtEzOXCbNj78RSaBKoK8TOWgaZB0ioPGoKbcuiMT--nonQ_un3PnwrDZi397zBr3jw-qJpYkoKQ5UTWwbHcr5n2vQ-8sSnnWs7VHyO3h9CsThys_Evqo1z9tVVzcurBCNoLaE5vlzoJMqafcnd-qvaeadIlxUxWO1qXEdSGjoBLkhSqfMAKDgnXhDYyV75i3qj07KRaFmaAe8GorrS7h2CAggsI_1E7maZakfbRnCJzdvzyQNeRaGKSjYUPSVI4ZYAKoyJRZAvmZIzymrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql-CkqEgEzqYmOKWSUatyoMqRvMyPYSgcLzTqIdBSxNX5SHZjDNsdxIynjRycmPB8osex984oZdM6Q-3QQ5jYAowKBtC6g1gS5aqz9RoclaAYS9D4eGW_EiQPT40Tq9ztBn_BdNYFL0LsLlFaDjHGA5B7RqBVMCK9aMPd4BdfIsA-B-uqpmW0ycuoU83uJNNKKD3S0XR2AnYXtZs9-7CB2DtOBRPYhGetP-hg7IeptcI-QZMy5FeAc57Ar63wFnK3lurjs7eVm56kJgM_WDozZj9fLo8bm9QOGJ4-uFRqBtrc34qTGeHTb0EeLQzLNFUwaPaK5yC3AWFFOKRN45DgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuVlOAsR3dSiqSuMNg8_3BPX_tpIRC5WcfW-Gza8Q68x6NVBZxh0YjpaporKuA0nSvlNzm_E1CXY5kh3DIMpklXzv-epKJMK2DlpPC-7uyDxAgZKbX81yhQ7r8DsYBKXv_Gr4A1u1GT3PjiG5_w56rjI-I7cWE2uvsGoi8kMJ6WKIApe49CzwziojVBr_82rOtrwc8RjRC_tG51GvocTxREMYokFsiolQlaaXAgm7zNab8AYPWagdtpDzWhDoI5xXGcPMO13HPM3dk_0UgeGdcgnweO3eB7GCqcFN-NDFc64UThP_pLjCu8v85ERBKxDqnwR8fCuhX1p29kXbPmgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjdSTho4bDDp_4t-Nh1UrkbqlT8-1n1EDO03_iPwPzFL865hJISFO7Z_MU0MTgsY3B-6yzhXRX1A1G3JLOmpKiA6e-y-d71w2WaOePM4359OzkyWSsLRBK3M7IUDfLayrrHSopzUq-BT93aSCJUPgSypXk3cS14KuqQD7oLR5SbgANn5WBISHpiscC3-qsGKz4pyf2h7989Zuyiz_gzIb1rLROX2nDNnMcl9-2htDxBCWgPCIus4XDbsnTT0abDTxXfjMeOq-E7zh4aj7LMGPrfPeBxe3yJs7WJM_DA5R1KmRnYIV9XT5cSsSAIGkqa7tPSH_pDe9tU-Dyrb3Q-mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLzMp2YR2eZYK6uyZwDBNst-Fie6BnoGhXqu1le-kRHZ0zOrdm3D0Xg098G1EpwWcgs5UC33mTdpDMgSxk0C8HnR5o_YaNu3mfox_w8eEUa2pFLy5zS-ZNX8Z6O02JdGzdQJldBDm7wIyZGvhSs5BDv0SXPp-2TIKUw_OC3iu5uLYM8zTm9ERY9cIl4gygIP6quyciI8RimQCgI5vMUCgWBDvK2xoKct5XcdVBwuQqyz80MTzxT9WIKFRFWipPV4SE_3sbJ3V3kuw6rKndiP8WbFjE6l-IMTYnOqecT0sKVmVGphCDppgm7gmzXOzmO8y6s6agSAqJDDNflFp-K6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfPlsdgbHW8-VW4glZ93HuyZbrt3-3InEiLUyvASe2eMUGTWQ-GyZOEeA1z4LNTbDQwAA7VciFypcFgpPr4Jbc_kTRxx8l3FZvlOXb33ZPOhzrKiqUiN3oK3_rLScwQviYPkXvTyNsUzxn-XNk3L-5mixjw2qhGComKFFgTgqzdGUbZ4o8d3jMS3Ukq8meumCUQbFYnUwPnRzSMuHTqtdQjw_571qf37DWPSmL6VwSYk54SOGHRQ1bS1OPLC6R3LlOh_30ItUyvDKgKflpY9kRMadbr3bJavOB0z8I1BXI35RQqRrhkZ3QeSewHwIUpPuU5hoBfhN4WMdsEY8_n9JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
