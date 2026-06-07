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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 14:32:08</div>
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
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3k8KY8kGJvAP2AAndTAuIcDP096hiOqHTX4vN__zSrCUG0XWofcZCTx22ov7tmWhSiTc-vF74teZiqGYAFjm1a6DQH801ylGKPGAdqcqOaW6wViYyrTtuOfzifaUmsM0RwwoyV8VKlihrrsyyJpm9f2BD31PYqOQpRtWvIrhxh_Lde-QQMSYONGi7tQt-G9FBVZmySHCZcKOLvhHTdUNu3_NZRaLZeH7F7h5Vn6ufiMYQb7fokh-SNt3LlIBCawziVsp_q95a1wCExGQp_ayPotx57smXhxGaLlpPzT5FPSdrZvIbWTaNpDp-SkTt7fdVRt1PMBIh0ZmVKn11t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwsBSRMMsea8Rh-Jk6A36yJIVd2Vh3LgTWw11UH8i3TDitHOnAV7q4iH_7z9w0o2FB1l23z5s9UJCcy1DnMe_JwKFIBhS0IAlMEL2HnSPJSSEIDTTpD41poQ3z9xA4rR7FqE7zH03J3vxG6FsOTiJ_myZtzB5f2tdMZKCX5fLB2z6_84jpBkG7RrMfHoQW55-ajzkvQQdVX4kIkSlpkHTEY41Zy0yN9AFJbRo_WSGsim13CLiwBJhh8DrtrGjellCD6HETb9tuIdrzSPDD-YBRrN_OUV_huG0ScsuRwh2aMU1kOBD4qovMYzuEVwyEqkcXYtAwi1LWvSCxuJ28ilKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Rb7vOKXYANEkdTdXUwNbKtOg-yTW5f-WxScQdtnNehTCQts1OMRXGiJHXuN-NvzLsoAbMuXaSRGF2nBuc93ChBu9zXRTZNqoy9ZTksUAp7KyDRfB5kjDi92z5gNuHB-5h2tBtgdb-8q2hY1A69K2-ted5wmOLhZR4FTjAn_Apr9ozSJgTRLFO4DCAeHIZuf-kpTCp20N5L36G6wCxcgJbJ5dPD_as9diM04QqAyF-4_kET89Au41qQdY5JLTuu8O8Y4Of5rUkaAMBm3J1fgTxJXIUHQTBPYVoLOwQYpZTJzsvYV1E7jkuKx4VW3oGDfVlPx9bbXLAOkv9_s6AgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ1H0l0U63-k3oVaFUXprFif1I3hz7MLvyLASRAKYVzXwq-YPOuaKaldefYN2HQtfKmPkFSQByphYfBBrHReqUTr6e-UbMTzqk4XexdCWR7nMGpftuH9FKK-9Ku6OKw-tpVepXAaYV5Y9-Ld_wuCiQ_YSRgOZME-vVZQgDF79kV83Wim5N_5ADJUCOcdGZJuZuwpIEeKAOuNYgG1LhEAYu5mRr-MMzbQEmGna9-88hqszGhBjP7lpkiFzycaVBNZeQ6OI6gXHErGhEgcHLj4SzyrU_HeMiI-YN58d0wOaXAUfm_LqDNEM_yZ9avXs2VeAV7RnBFJPHypQ6g9vdV2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc9qTT9iwE9OJXleQEMWUtY1qGHNtmCLOcWYPRHcsYRu7u6r9zaFQ-G3-9m78YIDR7mhZ-zySI7UjkXz3a_N0UnsS6TIpMV2CXfQ9t8JHSU2ECFyXGad95KzuceoFbW9SjOd_hKUq2oAnQd7ABPsMVckLpPDUnCJI0R3Ym0lkRTm6ogj2rGHyO3sTBX1OOdYuGbY_Nu-SmMrSFABC-Li93cJ9ceecqg71gVmxkacUgC6AHgmMvVLT1EmyIXY73QkjpHol-PMMpwbNh58dBLC_nm9NkySo77YQt9TEGTd0h0HeJqfIznBHia001WN1rktoWu49TIxexstxvYXbNPd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2-CH53y7F_vB2Ipzbb-_kx-yUx90nTzaAgkj_mPOg7jpzZuVr5JNg6oI7fYN6NX797OgnnFVK51IRE2uLLXzljI5DPojkO2SGrpuQTp_Md6fXhzm-ODV519YHFmM0ygZ3qV6ZG_yXjh1CZ0w0kFk79O_XwdXBdNvrys-8vmgclYHkvLQEH8PWTlDiHxpuEoxyFbrcZmgV05zkv6RLcSXkQFkXMB4zEd93XCZdqprGSy4FXpYZdt5-VStEJLxG9KBQYPt3ahG1Hr-nmJG10TiyUX53mXct2GYmnTO2iTcGokTPAyE78nfhbgQfXr5Ff0MjuOifpzMmn3Y0mxJuF1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4QEcS3xjni5SEku-2iaq67tOSDaTgNo-Ih2OM8i-rVly9gCm05hn_Vr6aYB9BE2htzUZgkwYwNSg4B_m6ZSZzeDzeCiMoP-pNt55EJSqG1L4MIbw7YeTqhXkw6iSI1pQpthOm8fM2yVoWZR_R6_AuvSAbaoDfGBseT8g1taGppzjPntwFgIL4pSh7XVj-sNkKoFPEgcyO_tp6qg2f39m_RBCe4zBoGck2yINP9Q7oq4rWSHuTE3loI4q4wtcdwEfVSSrdalq2iU6N-cwihbt9zz7Yx9lQ3iGaOHzu3htNbCz6Ne3QNJueCDOT9fH_XylwIe6KwQXNe2J7PGPP562A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=EPjMA6yHVd3aKreada0HI87dnW2IrHl_zGauMhPAysYpWw6xdh_pynFAlmFBuSClG8qWaBdnh3y6BsF8Lkc5Pk491OBojbQBuWtf6_N8OApkHUtCZxqSROePP5lPPc61tq9yT-Cm09G6qhBHukGAK-36LKdz8RNw752dcRaY6yjM_e_ksoUKP442DEArjU4FWnxFNz6Ed0at3xgk7EjBMPSAOA-1QLDLzTs1sxv2bg-jar5k31iuZ98zIN-rG0hwHnyAtAeB962cMpQJrMi4wfPq5bOS83pXd6E1Y7qJecmIBd2Nx28iCtScxJQBnp_4HGGJLR1Io1zQ1tpOFjOLEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=EPjMA6yHVd3aKreada0HI87dnW2IrHl_zGauMhPAysYpWw6xdh_pynFAlmFBuSClG8qWaBdnh3y6BsF8Lkc5Pk491OBojbQBuWtf6_N8OApkHUtCZxqSROePP5lPPc61tq9yT-Cm09G6qhBHukGAK-36LKdz8RNw752dcRaY6yjM_e_ksoUKP442DEArjU4FWnxFNz6Ed0at3xgk7EjBMPSAOA-1QLDLzTs1sxv2bg-jar5k31iuZ98zIN-rG0hwHnyAtAeB962cMpQJrMi4wfPq5bOS83pXd6E1Y7qJecmIBd2Nx28iCtScxJQBnp_4HGGJLR1Io1zQ1tpOFjOLEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBVfIULZOIfx4AP_oTjhQwzDdG6_zIC71Mxwen2igIMqEdp4mAPkmUkvSN4q6P_VXh-t-B6nWy3LKSf-tLmWhE0VKWqg9dDHcv6x5jkvJnCo64NBD88pYIj80vVDwtSb2z8fvNNdEonAMOoA0xg7Et_AM9RbjM1SSXDuB_ty80Z8xutV0Y23mGzQImhRn0kL_FVYqWlLVyHB2UFHTSsAk4S3WtsBe4hfxDjW1D6WlORLcQEl6o5St9SHzs0tNtNTFbWVtO1oZa5Cb09kEkcGHvgxzxFwoeyGJwAOSVbETSXWPvyRM1UhYOGfodOHpOzS9lezsgv1Utwmh6cUpGF2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPZ-Ae_e7BxP4fZ-IGjUY6pm83wPtVF-48HLTiOx5G-12Kd4PYz7AgVWiPo6dyXrYYBzTgLDxq8CjqVRbmdg96sOovZWHW5fIeH1vEorRBMbcj-3aNw7QCIFE0qRF3TzKF94nKBy70GkXCyQ432aPcPtR464_yW_e5ADAPCu7Q2E-1nY3wT9rygVKw2ATJb72A2jiFXih6v7BO_c6Lm34GN04kfLuI8Cj-moky0YPzoDZtmER985-agPOCl37feHvZ9lI6GabPm4my3nO6BagU-8IROK-M3964wrbF5tqfsdkcwF-VubIO95hawqPjQP8jchhlegG6sf3xB_K4Pblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZhR3O7v_RQ9zKgihwm4sogIqmFVNp2QI0c_OscIWwCK0cd50eqDSvChwe_mW20kheUyyL6A4pkxYt4S4DaFTX12cGDGLDYSXUxPTnR3AEOnqUo8IVxF4NkVeMP9NBpTDtM9GMQ5xSUmiyAD8lkGPJGd0jn_6bhWiaLyVzSZb3bCfAlI6HH-utVIfd-UL-QYFuzN45ifEx0MgxyRrZ5wKZydRhnAmQL-s0j1bxhOdH2_JqK8SbmvOAsj4GDkqE4hczwgIJ04OG6_6pFbVInGBB7LyijJecNvsKCf5h3UnXXBOvaR_1TLxu-ZyjF0LT9E2ToLP00pcgfN-2o8aI3Y5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pgq3JuLphxKIpF5rNcaT02SmRKnpKDbbvl6vItTNVexWmmkf_p47agpoDxliUoE3HlJQcnS31WmQVjJDfiz93cuGYTCw6WQp8X2bGWwyPeE80ryhPgNokjTsLhANvQIUIV3ach36XNIy6DQcL-s2SaVRcXegQMJDA3O9fxb7Ppb7ikkcdo1AubM04OWlj1Mubhx98sNXK1nbkFyu24q1wl3mDH7pMxM-uQP2pIhOB1XJEkxvTOlVZ0X4qBVPp1otOYmB0UNbZfbDNgKr8-JgkxezYHhnUxxAC0oKpAdwJNQF8__HLEeCHhe373iRRGi2ntcSheLdDQMHwnVV4_O1nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=kO7YicSG4Y30DplEtfZtjzEnHTK4US7wwgdjm1S5bkufUvDXbm6uAdpjFdrcjvh_O6_9q_Cp1VujrBtSWnRG0aTJlFWw8-XPKMCyFq4ldshfxxleAMTIOjjaVSIvQu8DH3buFMAIQ57m_Nf2l2xVKfxtXej-sJDHowV6qUUFQy9T1pf3CSyv1sfQ-5zla4hVSc8iDHOW7S6s9HyiY9jMLAOjiHlcDkFENZeqSOhl8ZMIYiYHM40lbK7Rurt0P0twszLRjI6ulCmJ58T_7ouUBE5Wfs636IBFN2SocP0jtNfY-25Wzcf238__Ack9WnzujYZsOhmxkAqWwL63eLuwwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=kO7YicSG4Y30DplEtfZtjzEnHTK4US7wwgdjm1S5bkufUvDXbm6uAdpjFdrcjvh_O6_9q_Cp1VujrBtSWnRG0aTJlFWw8-XPKMCyFq4ldshfxxleAMTIOjjaVSIvQu8DH3buFMAIQ57m_Nf2l2xVKfxtXej-sJDHowV6qUUFQy9T1pf3CSyv1sfQ-5zla4hVSc8iDHOW7S6s9HyiY9jMLAOjiHlcDkFENZeqSOhl8ZMIYiYHM40lbK7Rurt0P0twszLRjI6ulCmJ58T_7ouUBE5Wfs636IBFN2SocP0jtNfY-25Wzcf238__Ack9WnzujYZsOhmxkAqWwL63eLuwwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhLjyLnRTezM3KNsfR9eL8jwJQ6H_R_QBfswrT4k_1laRKpHBQKAJxOwkEewjo4nZSB2iS-Ei6doX89BWceVWlV8StAzIktMztGamxHjZywaBXaH1BMC-k2VRLR_iD8gIjUAAdxjQzGoMXAOwW5yipX7osclvMkMLmBThBIMQKsHWEsnSRlYVLx82tjOnVuLWu2fwqaAYqGpU8z7iU3l8q5xX64ZehaMoWIkJ9vuzyFHMAilQQWd6NNv8G_c0Flc4eO5eSZT8BNlRfdiKOqFJjYmCT3SblGPoBPk3VHh6oovjdxgYVjYkpjK0y8R1NRhEmJlWDpZ_9hmuesw1RXN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=o-PP1xDI7zuqqIPNYKPYInvTPiQOCmyT-Vs2ehLAV-wXs4KZc_BiH7aJQLfd2n8sNttRq6x2NBE8BftzzI6tpJfq1hcqzWN5HCwBSgYrTbzbprXxZ30KGo9IWntnR2NqI238SqPnsLY8EB5WKbmQZBhRhehqlOZ8dv26GtodkBm9DOKhSQVhaO5bC1gfpNIClH4oLrtqUahO5fky8mlGdw9_fFCY7tIFhrv-Jwz_8SL-Na0ot63Va1y1zwXqul3VsFh7GqzvndnUCMXJa2Y9mI54Ti8_TDgvaqCyuZ2EYKI7kONbvzmb2rUnVl8Vlj4GSVMynCdAnCzR_dxkGS4OPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=o-PP1xDI7zuqqIPNYKPYInvTPiQOCmyT-Vs2ehLAV-wXs4KZc_BiH7aJQLfd2n8sNttRq6x2NBE8BftzzI6tpJfq1hcqzWN5HCwBSgYrTbzbprXxZ30KGo9IWntnR2NqI238SqPnsLY8EB5WKbmQZBhRhehqlOZ8dv26GtodkBm9DOKhSQVhaO5bC1gfpNIClH4oLrtqUahO5fky8mlGdw9_fFCY7tIFhrv-Jwz_8SL-Na0ot63Va1y1zwXqul3VsFh7GqzvndnUCMXJa2Y9mI54Ti8_TDgvaqCyuZ2EYKI7kONbvzmb2rUnVl8Vlj4GSVMynCdAnCzR_dxkGS4OPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbggUWtdqvAo_YFiuingfUwyt5b_PO3TGNgyQf3coWFSiPpg8q4QvDyNWd47BOKynS586NhW1mRxSVjn_wK1uSLbWBWakWxaGfQRIE84p99aN638wvdBC0nOSSws9Eq2Lch2-ucsufyPKigYGflp_TtNM1kbiiQ504sRawyp-rtcOB-wI2xpzD_F9kauq4gFdJvU9ybQP6Qv_gl89emKCSSsHruGjhuGvtZtEuWOqDH4_k2phUPUy1jJHTCpmK2S66JRtkjvTxnx-jfPLhzxRYSKEp6cFNwjvz8G0wNb4b-l51NgXVQJjhSiRxPql00xMZ4bYhHcrvAEn54AIgqBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVz7hUJFOGVilY0ThVu-w2-d2H5VORV2X-IurDdvR8u56hnA1KAc0k4AWZZnskgfujJqk9YehqyEMrtIXpLCL3GuKAUWtDDb5q5Akiynk9M3ocoaMIh3jMhjfiHjcwGGebsviJHmhWT57U1olNdv7hljZe5iEg1flGtF3ZAQzeEHcHkSQ5Uv_I-vac2Ica0qMyh18IKEmTdFuIhLZgrJu-VUbOh3MhWn0ZqnvJNEyxFhu512wYeuK0BP8vcoSIhLYW6-THvWYsl2Rf4K2RtcB9vMAg6x4EG62rv3gWSgvkOA0wQb_Tx9_uAu08csSwGLvAMR3KK6xo3Ua8ijDDi9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=qMUQmx6ihyBYarmgxxzySoRhypbnB00Pn-EVtIPDdI03a-zHblULtwAE26IzfhJ7-rP0DAP4FmKF5ZdpHLeZmkJ_EztqaSCqPxieGcdH_MVVGQMsbJWUgE5P2nWe5BaNc2UzAfp4wuYxWNMzYuDMi4Z5Zlgybs8fy9JaCVcMGkGyo0cE9Bs7rAFRpyIyyxzNWwUdXpVQlHA-5jc72On9AB4qpiG_CKnDcc62v9sROL2JSr43PK3xc8VHLA14ZfzHWhMdosv_F9aRZgBRHvt_xDC8zDdwRVuKJBY7X-QRX9P8-GxCViCPFNfa7uS-yWhEUvgTuD8UIXQqgeMN-83zeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=qMUQmx6ihyBYarmgxxzySoRhypbnB00Pn-EVtIPDdI03a-zHblULtwAE26IzfhJ7-rP0DAP4FmKF5ZdpHLeZmkJ_EztqaSCqPxieGcdH_MVVGQMsbJWUgE5P2nWe5BaNc2UzAfp4wuYxWNMzYuDMi4Z5Zlgybs8fy9JaCVcMGkGyo0cE9Bs7rAFRpyIyyxzNWwUdXpVQlHA-5jc72On9AB4qpiG_CKnDcc62v9sROL2JSr43PK3xc8VHLA14ZfzHWhMdosv_F9aRZgBRHvt_xDC8zDdwRVuKJBY7X-QRX9P8-GxCViCPFNfa7uS-yWhEUvgTuD8UIXQqgeMN-83zeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcqvbSQbRS1Otmu4FM3dJeUdV_KUECumkJQI6asc1gM9EkCzb5j_orsJjOXLM5xPTNNAeSK1z-tGKgRTb2OB37W53TBMkMgihpPWN5hTKji_bziFrCLiCe3HpAw0WZn7BgWnv2KNcCWt4mEt70TmjYml0604sS4mCwpjZsTkCv3qFRqaxkKfPkjZEWNwiy-mx2iRG8jZ4WH3zr7KYOCYEXRhxpB13dN1pExkTFJICAJj3JwNGrBUuZvlkgMYGNGV2FmGohZ6HOln0iLRydrlKQmQeJkpaHb_JMKLM-zyBcxLe7w3KHo4blEqzsZ6aCG8v2p0-vLgL1MJs6bnlDIbWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=fnlxdz9H7gNrUCOLkReFG0lYENP1DIqR_pKPKwO0XK8TYDsqaXpMuC-B8qCuNzCm0t0RWUKykdW-InnZ2rZBP0QdSu1X-jzLht5754rY-l4ZaR9B8O2GuLSG1jDCUip1ULarMBdVKLQHxq6PQYx2EJVB-8SZSZCNNIh16M9JqJfe2KUgyJojZtlAiJteBcro7nMwtjkWSYmBHLCAi3lY3FUZaHtWOPtRmgp6dfG4edjmc91iIVKN3rAy2IHHrpMoauWvhbt8f-xCj0oC_fP8NZVq1BqeenpG12yN46LlvQikWlx3IWejIpljoS7uNNI_kkXfEc4ofVN2tv3nOMdvHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=fnlxdz9H7gNrUCOLkReFG0lYENP1DIqR_pKPKwO0XK8TYDsqaXpMuC-B8qCuNzCm0t0RWUKykdW-InnZ2rZBP0QdSu1X-jzLht5754rY-l4ZaR9B8O2GuLSG1jDCUip1ULarMBdVKLQHxq6PQYx2EJVB-8SZSZCNNIh16M9JqJfe2KUgyJojZtlAiJteBcro7nMwtjkWSYmBHLCAi3lY3FUZaHtWOPtRmgp6dfG4edjmc91iIVKN3rAy2IHHrpMoauWvhbt8f-xCj0oC_fP8NZVq1BqeenpG12yN46LlvQikWlx3IWejIpljoS7uNNI_kkXfEc4ofVN2tv3nOMdvHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u25nrom1IJz0Bz5uuAkuPeoPx5hGmOMR1uB5-66yoIJa4RCSqLTboPh0Z5-B1ai-u1cQiZQmAdGeUycTOmmn-9X6cw_iK1WRRYcS0kB9IQv-u1eWQqO0X0GtpcCGdsQzN37ZPDXv-U58vobAj4_S7Al-C7btCf-DA5lf9Sxo-Xf-CMjX2XAM7sKjuUxr4tWh2yBokykLoLGOlgkCr2AiFg7o7sXE2fx9H3JIASXQhpUESwt_H9xzq3AUZUkZu2bNxuEyj9M12sVu-FxZ24trnuslXt9n15MXDIYELIwUBG6aXgutFS_BxBg7CriQIQv7tuOnLpGGysJ7K3fw8ZOiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCo7yGayvhWFum21U0pVZ9xwFS-cXWGhKR9dOpqJnA5R3DlSvA3hXTgwlihuDO5FMTms5QbHDByIKsKVS0a8LdenLf6s60R_4WTzyJpnFVbpNUHjky225gE-U5ZJknl4VfbISGn2B9mBJFH9PirsO8m3Fg7POdfGHyeUWsLvgK3DiXleVUNrftALXROFKd3snmZONA-mcDjPC59Ln0RM1vw81O2j8u4vG-TAtk68VhtDzA9uLvVqM4GHRuX680rJ6BDXStNEJoQExnIwpce4LyklRu_wY5ofBxMlo7HoWNSEXmI5ojiwWQjG61XGhdnKlyDoJ2bZDMvM4vtKufFnCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGSk8Hko_feuWxjvSyqKkTc10jGni5REGH79-5YJ4FI0RJSqaMCUY2p2QKd_KzqPSPSA27rWteV2VGo0gnnwr8Mue1xMgCCTMOK3fgb73zXAo4kIZdopCkFfQ8wJVA5DmzI8hX4hMSoiD9HuCFHLR5kBmIXyNNqfEm96bTGrb35BVEtCGrAGesqXxwSvl3Bx5FOHqW7Fi8HSQONJdEswrRwesZYU116diuQWAwXABT98anoDJFy-Hx2VS8wTM6Ee-TTYjZiFaBk8W7v6ZK4OcH3efaLtp_LZizbWdjHTgOJ7l1ACjutq0CfxTcfHlXpT1R8xjy251h0jRX8Y6FOGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=iXyax6ox4IwoYQhCaJadwwWPvzCNC7uNK-elEyrZpfvLTPTCzfUyNqvDc6rUisSZYk1MN19WlR0lp9fCH6Vfz5B1U2s8mOLpbAN_QGKM8W8S3Y4ugHCFmgaNYi5Ybn0k6TM_kRGTJpQaf65oqLbp8kVy6hIYyQed1PYqBxOippsUZH7skUTwLQlh18mOC98E5HxfVsv-KtyW4Hg5wuWOvkujLEtJEkChRh3Z8vobADdAcoOm1RLjhc7WHI-wqbkD9ZbnFoALoH7ueAdMr-n8xvYM436yh8Vty87wMK9kEyIbPUGs5shqFhOY_NMfNJPEf0CGmg261486rhGWhkU5wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=iXyax6ox4IwoYQhCaJadwwWPvzCNC7uNK-elEyrZpfvLTPTCzfUyNqvDc6rUisSZYk1MN19WlR0lp9fCH6Vfz5B1U2s8mOLpbAN_QGKM8W8S3Y4ugHCFmgaNYi5Ybn0k6TM_kRGTJpQaf65oqLbp8kVy6hIYyQed1PYqBxOippsUZH7skUTwLQlh18mOC98E5HxfVsv-KtyW4Hg5wuWOvkujLEtJEkChRh3Z8vobADdAcoOm1RLjhc7WHI-wqbkD9ZbnFoALoH7ueAdMr-n8xvYM436yh8Vty87wMK9kEyIbPUGs5shqFhOY_NMfNJPEf0CGmg261486rhGWhkU5wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=Vfm9DvI6-AERp5smk49j0g5Ejk37yHVfsZ04LSYEDOBrxbcwzRdSfiVsnOD34gND4rT7Ytui5hbspS9bTkgAyfbdfpla03MbjjV502cETtPTJJo4eUjyLlqoxyBvpM-ldoZruZ6Brhu0OmaJD5SF09HbiNlFDLGP7_YY7h_SJTUI6SsYgI-PhIqL9Hti_nCP7MlQZB-vZCej6_moNGi1NE6c-UELFER-KneEB_gkPImHI7IHXcCBefcFT9DlWbFNHVlaPZUX9WJPA06DyCOBNQII_uXYLPECBjneoQt8afGgGquCGVx1DFUjR9xBNruDmpW48lyFTD4DS2JDsBg1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=Vfm9DvI6-AERp5smk49j0g5Ejk37yHVfsZ04LSYEDOBrxbcwzRdSfiVsnOD34gND4rT7Ytui5hbspS9bTkgAyfbdfpla03MbjjV502cETtPTJJo4eUjyLlqoxyBvpM-ldoZruZ6Brhu0OmaJD5SF09HbiNlFDLGP7_YY7h_SJTUI6SsYgI-PhIqL9Hti_nCP7MlQZB-vZCej6_moNGi1NE6c-UELFER-KneEB_gkPImHI7IHXcCBefcFT9DlWbFNHVlaPZUX9WJPA06DyCOBNQII_uXYLPECBjneoQt8afGgGquCGVx1DFUjR9xBNruDmpW48lyFTD4DS2JDsBg1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=dybhlFT6wIEAFYa4KfUBJRxKM2dkITbQDTR5F2CZWUD7EG7SY8gMYMSqQOd6UGu8H99uPHrwfgpevUfTxNhIW7CixB6SIb7kb5sOKPIVRsLYVSt2Q8cffW46KkVRaNx6Gp9H2z_AMfirOxYhrhwBGrW9d9O-bd8QDpxrD8LvGH3mRSp8h1oZ1uUekiMSQvYBzV6902pvtiEdlJP4o8pW4QBYGR_3rPZ1BhZ29opFE1Z02HuOjJOw1A6P18-2SJ1yvdux5ZTPPSQYMgo2G_gSoVZbZhaHE6me-62vTdcLdVfYU7h7kw1jWOA_l82NT7gYOcXIKmUvX9ocFC-_ZCorzgXueexSpXUT1ZdpDaT_5WtwA3v2HXuFiu8m-WjB4icfaZLOlnWmH9fmdAA4T6Lb5a9K01XMpDRDVo_X-4tfd1CkdVE742DkJw5HuXT43aVVoZ5EhEO__3E9k_egrrk_T0ktm8uKKCkSZZ_-0yhkw_LC8-iw8DJrNntjt9feV4vZcaDPX6QMhwvI6r_OrkhCtBOAUByBKgsDLHZ0_av5q5537KY8rH2I7Bmj8FyLIBX-lcCyFmCyngn-aDXwgA4vWxO399FTx5PXj3p1BcM59H7tJkdMtbInAaFWEMPvLFmKIXCGIiQxA9fjlFr9o2pYhiqgSIPlkkw5yVWKHUYr9l0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=dybhlFT6wIEAFYa4KfUBJRxKM2dkITbQDTR5F2CZWUD7EG7SY8gMYMSqQOd6UGu8H99uPHrwfgpevUfTxNhIW7CixB6SIb7kb5sOKPIVRsLYVSt2Q8cffW46KkVRaNx6Gp9H2z_AMfirOxYhrhwBGrW9d9O-bd8QDpxrD8LvGH3mRSp8h1oZ1uUekiMSQvYBzV6902pvtiEdlJP4o8pW4QBYGR_3rPZ1BhZ29opFE1Z02HuOjJOw1A6P18-2SJ1yvdux5ZTPPSQYMgo2G_gSoVZbZhaHE6me-62vTdcLdVfYU7h7kw1jWOA_l82NT7gYOcXIKmUvX9ocFC-_ZCorzgXueexSpXUT1ZdpDaT_5WtwA3v2HXuFiu8m-WjB4icfaZLOlnWmH9fmdAA4T6Lb5a9K01XMpDRDVo_X-4tfd1CkdVE742DkJw5HuXT43aVVoZ5EhEO__3E9k_egrrk_T0ktm8uKKCkSZZ_-0yhkw_LC8-iw8DJrNntjt9feV4vZcaDPX6QMhwvI6r_OrkhCtBOAUByBKgsDLHZ0_av5q5537KY8rH2I7Bmj8FyLIBX-lcCyFmCyngn-aDXwgA4vWxO399FTx5PXj3p1BcM59H7tJkdMtbInAaFWEMPvLFmKIXCGIiQxA9fjlFr9o2pYhiqgSIPlkkw5yVWKHUYr9l0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okHNe6v6xet2X7BJE4wJ8TDZMJf8k2O3iI0ZJ-ctHTw5LYMwzowJGiV0fV-_7CEJcQkCURL3l22-nF6FS0x5RrgRtlI7PuWVtCBktH_oTsCEJeezB27q6_GKGqO8WN4pWDdeXg8mfBt3rLAKjLzpNms-pCdSBqXPuhI02z0tNeF9PlPHzJ_a5ddqdhO3M3hpfdwAL-r8wKpSahmlBEUSNdyUEmgne3F6cFTqGJ4t8ZUsjAOqeiYa304a_VontVqK8AePGjDzOhUQL1va2XKf4oXmwfsnLdLuRvW3feXGTWztrO5BNUu7Jj1V1303E50_uEekgoKpg9bJCDGKRowHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-Q8s0CoETaw73f0UjIJy2G7Xy85KukoJ4RqG0yYm28ik2OX5N9cb2vzZ2DOcrUT0XNREQa9_jwR-Uq0kEM9BKFAV_u4nHso-12flZd1XkJp5uFhoMKDyHo7d1pfp7y5uGgDuMMS1KZ8KiK-TtqoKmZLp9idKRknjs9bLhh99AjRSkY0-k67KRupwzITtYKeUI46ibP4ztaHysBzRxbECjl9NVqkEPh36HXX5V4iW5KZgtGKrIc6vP3zcw52zVWC8kJ6iKiQe6neZqUTKJP3Oj7aerJNzi1EOPcRod-t-lbrEzc2dDtPhBox3-SoOSkxv4FBjT9HxP-wf1eWCswGm4Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-Q8s0CoETaw73f0UjIJy2G7Xy85KukoJ4RqG0yYm28ik2OX5N9cb2vzZ2DOcrUT0XNREQa9_jwR-Uq0kEM9BKFAV_u4nHso-12flZd1XkJp5uFhoMKDyHo7d1pfp7y5uGgDuMMS1KZ8KiK-TtqoKmZLp9idKRknjs9bLhh99AjRSkY0-k67KRupwzITtYKeUI46ibP4ztaHysBzRxbECjl9NVqkEPh36HXX5V4iW5KZgtGKrIc6vP3zcw52zVWC8kJ6iKiQe6neZqUTKJP3Oj7aerJNzi1EOPcRod-t-lbrEzc2dDtPhBox3-SoOSkxv4FBjT9HxP-wf1eWCswGm4Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH1ru8vRCr3nptCyBumfR5IDX8ASmMm5Ql6me2v1X11d97842FDvHyEPcFwF3jmrbd1DXWSfhu4G3xmi0v3GeJocWLH9qVYNJMN7P8uemaIVOoqwnEFYP-uraTWEOv0G44YD6r8YSiYUxPhlBjeeoGrvLcjOnBsllrvm_iKwYsDQ-n5CuqkJbzsvEroAuiGmg5o_KB88bd0qhd5NDfNujoPNvICteNrjXzjJD5uTUahJY5eVkd0VDJ0yDltSb7GZbOFVibkz_jNR31hpGk2zm2zgvGieHZhzh89gIf-lrCMbMyYTHT-mUA2CBlfJNpdobsTkPnkoAVsEQqAamoWfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTFFmi16xugRxNb0g96NjmAq2CQENzprNMKr24tUUhyF7m9ofZ9d82PQwNboc9krcZbs871ASdG4CSf5vqdgHQMDtrEiVzDdljXPoqnfplM9QEtQxgoK8ocGdzIkLySpDrmeTLxThftDJc2LZYO7ZTL570O-dCEZxrrkw4__4xaxfa-6jHGinRFWSRGhwfj_4jWVRqOxd5mDw51ES8yGqHEjXpzlsPgyhmZ0DxiD5c2u9QfLDVS1yd4YccbnTxaD-_wjYvZjh6VNSDaYtmWnUZaV1Wd6Ptkxstgec6SZ9mpUcjUMvkIzHy2kE-O87qeFOmD-HQqMrITJH27ybAHqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AatE7RpMQ9x74rNAp_L6vSktWC0iyrdfsemtA_GXBxcURzDcw3SRqe9QMrjPNZRPvGU4ZxzytKBhlEhkQsFee1M9nmjVg4r_b8I_Qd74JvC5OP6JuE2B9ljk0h4OImZuo-c38tYD3o3-msUnEyHoBZTUoAQGnptsVCgRQjLyf2uAK3Xii834kF6vXbw3EBlkpJdNUcSo3JgmOsCJGKB1T7H82T6D5V6M_Bsnk7Bp9E6nEoWGPb_oL5FMmVTMUcsI0NIequdfwUgZK84NsWRSR0PwaawjGDvqxyfIAeutEcFIsa6KJipGqYiKT88HMFiNbnOO_CDN-RUNl0RnZY_Qaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEADwnTz2tw8vps4LXpRYsbuqSVydg7OJXMDDZfE3tqgwBFFHJlLWzkxcOpiR6NpLuH660N9wncaD-QTXvc7nQNxZ5-VcmTb9U1tyrJOOOLNhbvxmAyo87qF39DV-RYRSuMFdn9G_-HC3KHBI_xQSzy97TSNpxFlxscZD_6VD-UAO-96ZXOFQMikn96dcWY133HdmdrfpxPzhRxx64WXSW-exyHzyFNrp1-SY6Mo7Dc2VoYElZMe9gXiOUuFb2U5p--WO_y23t6ZTq3ihD0e1HwY97EC8RVI13zyXpAP81GR04r6mjxwth7GH22wMJvDK5PcbdrvLCu77usCKGI4_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzd9mP9VHJUfiJWEIJ1ycfalPZ1xhO0sPSFxDs8fnwDFoIc8hoh4UxzCg8JRTqKajgh6u5U5_YVN4NKmDiZ_aGem1RHf2PnCApl34gIBDvrHMkNghVXyRlxjPQDed60WBi92j0Lu5tcmo2YPL2tTZvq8GfWvwHOYLAbOOgUNUU18hjCDHQYSguRIleTVZcApzfaJr2mpYy8MJt7pqdUUWSgw5fEjCfCUx2bNAkK-e7TBW6NyRlHHIwXZT3hsoKxSiWaZCtJHsUa-_mJZH0t9XysxYE41UMFAOW57x0sjsL6CAM73LkftRG_rZ73GVsPBMNvtYlyXgZpJXo1-wrBCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bH-aYjjnTkhLpkXmAQIS9n7VKfOoGCcQqN1S_YbGTSgUm8aKz-uaCrKIGdnQuUJb8MoN62IZhPKFgwwutxa8BLrW_HIR8ctC4ipV_XpLQqs8vOJ0tDr1oO_eZBPE8WHyw8ahqq51jrAhctmuLvP9fxa_CAUVBQFfEFhf7lxJlOnIsxz9hHFFZSEmIdE4Zqq4wbrKYWlVoq91oYXSO2mAGkv5EPQOdkwXUH1n9KfeKkJ8QpI5vFVJ8FWMxi7Va3ogwa7WV7q2ydjFyR6p_2FY8VfKnL2tyWTMy05TvvRDhAIsWedLO3GnKzuGJq3g1LvKx4ZAxpohuGZyWVsL2v3QsA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=Mb1KOWff-grFoSNO79qGH0kV-6StScAp8QSXpJ3W_hIscAdL8AgIO_7zrRAGLtZymBRuUOicYf2PBQjKRaWGTgTi9dQ7dcmlNP0Mpr2iynMi7uaSZcf_QgenpGebeORN5Y3-3jDwc4ntmebpn47sfqaP5dZPApoDEVmUmo6eRqAVdpEqnzeAL_rQnp1ltliPYM_j5iG7IVkqpm2sbIP27xlMgnNiiiRBhdQQ_qXTZ2revLQNb7RnwLuPxaQRwDd-BjhLXsU_WBUbLtWVYDGXn0MuaYOxxvkY6sc4XqNeTI6O3S1-mvvW4o0fIcZk-tAjpdgtDWHU10Tc2ZNTaCexjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=Mb1KOWff-grFoSNO79qGH0kV-6StScAp8QSXpJ3W_hIscAdL8AgIO_7zrRAGLtZymBRuUOicYf2PBQjKRaWGTgTi9dQ7dcmlNP0Mpr2iynMi7uaSZcf_QgenpGebeORN5Y3-3jDwc4ntmebpn47sfqaP5dZPApoDEVmUmo6eRqAVdpEqnzeAL_rQnp1ltliPYM_j5iG7IVkqpm2sbIP27xlMgnNiiiRBhdQQ_qXTZ2revLQNb7RnwLuPxaQRwDd-BjhLXsU_WBUbLtWVYDGXn0MuaYOxxvkY6sc4XqNeTI6O3S1-mvvW4o0fIcZk-tAjpdgtDWHU10Tc2ZNTaCexjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhd3mHSQdq9q3TWulcauiw1Uz6e1vddDECOYiVHuLRwrOYglG9ceWb1JbHMy18UdeK8WmDuTm9fTMCZcg_0727i6KtfL8WLzGHLftAON6NTJ-fK5CHiVMjSNjEbPiIaprch9pSGoa-PCRLEr9M9RprhvCqJVe_055fj9MYUIzeRe6ED7-gaTGLtZ_s6WfW7ICFcn_AMzTDnNzbKGqWgUchxcQ6mgVB36CnNZi5f5za_ji6nnNFq1VSBJNA7tz40ZS4wQQvUNnS8Sl5rYBeYrVVktPohWzxwccUkc4OLlVLIZByFHsNlreUiikLu35LMn-ze4SteooN_E5xuVTt9hmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOxOHIQ3IGu2okJSxxAOS3dmXhG_9GKdYGBbii1LWRUl3mvXytYXbfsXNZ8HnPKtxGULcnvzKYDckSXlwIuSiN_JQmEZf08CJOtrM628zDVYU0Qu22i_wDfez-h8WQssJqIOUCWnEK2YgVI_lrbARguc81IPBIDfBPX98nVmRK3q6eXdMVAcWSL9IoNI0cVHmtKQxoCp1uWMzUt4-CJVrCs33L-jxeERBmXANEgSb2ZMoJsfsGwTL8KzLnSu7K30CuqGIQA1bm09VUZeXZZCozHcMh90GoIzYk4E3DeDuF5uG-LboJeK1mDm1BWuqzhSfyHGkOj87l-ODaM-gX2Dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wfuj0OwGwxi0W6yOLHVXHRbogG4V_wVkS5bLzQuOxdM5zv1H_8HOT7S-luSn1OJzEI1B5GiP2Le0KhujB4P7hSl-Ca4e3XPQ279S3_VCh4k037wVIOff_ES6nlf2Hf47pmQ5CSmWzFtWIM3U1ebvYkVF8JSgZ25uqX6fRu5m0MUt2Ndu5N0lDq_a0YG4pOyf-kcOzbN2DY_zj31GtzfT_WCHhwUC2Q15o0ddvD12oe4gfAJv0xWSLyXff07NNYLxcKOWBhoA2eawr6b5WbGbDwUTAsuQwMopgXcS2a4ZSetjh5j08FGdg3tvA2mf0GGi2u8F4OJk1rEsNMlmy0UXtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=Y8J0CPiiufEkqSKgNEUK8yc-dYKEHxJt7FnJTX4TksGKEa0RPNVkODaFSoVf-VAN-zRR5k-4a_tUjvZtpTD_qFuqanq279RhYZyiE7a29pQJj4WCs22SzHIFxIE-w86bWm5cRNyTXFbAxNcuOVbwGVdBU--iYcjWA3KcWa4Uwn0fq1Gry3W0pAblgWK0-Xl6eCmsoxWXqwXtl-Gx7K4XrMYuf18XuFVDgICpC5rza1AxFOIs5-TDWhQgrHXPXxXUlBobCcDlxeaz71MX-2rdwHrkgoxb_kqWljYEihZEyn3diLfm89ditOfOtNJhTmDvNXHSkLSWPl_taqI4lZBKsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=Y8J0CPiiufEkqSKgNEUK8yc-dYKEHxJt7FnJTX4TksGKEa0RPNVkODaFSoVf-VAN-zRR5k-4a_tUjvZtpTD_qFuqanq279RhYZyiE7a29pQJj4WCs22SzHIFxIE-w86bWm5cRNyTXFbAxNcuOVbwGVdBU--iYcjWA3KcWa4Uwn0fq1Gry3W0pAblgWK0-Xl6eCmsoxWXqwXtl-Gx7K4XrMYuf18XuFVDgICpC5rza1AxFOIs5-TDWhQgrHXPXxXUlBobCcDlxeaz71MX-2rdwHrkgoxb_kqWljYEihZEyn3diLfm89ditOfOtNJhTmDvNXHSkLSWPl_taqI4lZBKsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=Gyx7rwy2GcL0vIiPLiTJQVQZVJw2DP14xQlpwQJGgApO6GwO_wPSNGlg9HZDTj7r3nKdqmisy5mdnjqtVqSwvq-wC24oEvdOR1u2l3Aa9XMJlOVsOzcC5dB1XMUEi9GbF3VzC3nUwd--dDbznth_R_sD2ULqgQereTCDuLZNkH91beEoYo5WyB31FDLEoX2b05wbCTukzn1rFXYTENVtMZMcTpaks9SG1yUIEsT0gLciNUEc8EKKMiRS2zqrJkLG00R9omtvnK6Qxnxa--AKXGOHGEWNSbWH7byeJ3cZIIcAaIXHKDl9KwkJECaP11lo1MyerOY3saqACUR-O9gZVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=Gyx7rwy2GcL0vIiPLiTJQVQZVJw2DP14xQlpwQJGgApO6GwO_wPSNGlg9HZDTj7r3nKdqmisy5mdnjqtVqSwvq-wC24oEvdOR1u2l3Aa9XMJlOVsOzcC5dB1XMUEi9GbF3VzC3nUwd--dDbznth_R_sD2ULqgQereTCDuLZNkH91beEoYo5WyB31FDLEoX2b05wbCTukzn1rFXYTENVtMZMcTpaks9SG1yUIEsT0gLciNUEc8EKKMiRS2zqrJkLG00R9omtvnK6Qxnxa--AKXGOHGEWNSbWH7byeJ3cZIIcAaIXHKDl9KwkJECaP11lo1MyerOY3saqACUR-O9gZVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxE3JGVHTC6M_F4N8baEcoR-ZOP9jV7qGLF9OtNmE8Aqa5kgm4fQEaC9niwRurUEu3iXv2Y4jcZtiQ9Txl-UJgLmMaFWaKvdGRaW6CCThlyR6pc43tJ56fA7kqczUY_3nc-L3tn9Nh1P2olZK_K5Fx-R2g-6_ClyOI24lI3qfOAuLokUF2Q2sILoOp6ia6cROAgxqybYCGElieSWQPqMJTMRJqQIZWpTIWFwGiKtNgnivUxnFk4gT3gmL8g3GCnRg0QaPueJOx7f5oMtmzSIkTTqA8y0qZTXMuKpjwKv_tlFnRFaR75--VDD8qzb3TiUx1hFVLRf_71EylxkSGpwEKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxE3JGVHTC6M_F4N8baEcoR-ZOP9jV7qGLF9OtNmE8Aqa5kgm4fQEaC9niwRurUEu3iXv2Y4jcZtiQ9Txl-UJgLmMaFWaKvdGRaW6CCThlyR6pc43tJ56fA7kqczUY_3nc-L3tn9Nh1P2olZK_K5Fx-R2g-6_ClyOI24lI3qfOAuLokUF2Q2sILoOp6ia6cROAgxqybYCGElieSWQPqMJTMRJqQIZWpTIWFwGiKtNgnivUxnFk4gT3gmL8g3GCnRg0QaPueJOx7f5oMtmzSIkTTqA8y0qZTXMuKpjwKv_tlFnRFaR75--VDD8qzb3TiUx1hFVLRf_71EylxkSGpwEKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0wMamPg9FDFfAQmk7hYWP_mHDuR17OWhYbd0HE97PXLlkkxUzKmT96HWu_92IfjoGftCO3vXUHRnmspqw4ALI--_8h07QYXu_MXtbnZ4hLZWi6ZGlEFHkMbVYEryJcQqfGvZvY7nV9zs77Ur3-jZml2s62NdZUg39nSbELH9v5PD72TXuTtwQTnLei1ZGz1fA49A-OIql5jTsoatKCrk5Qv36RBeMRazzTV8uJS5PoZ9CV2XnGGaWZDAkW0hj4uneAhVQid87e3wpPM1zqauYy55SvPc7GVgfDpM2yT_VPgH5szB0ifcsjza6eIX6cYsDzlcyqVciSfH1IHZrn8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFIxVQ5TBJNF8a95R7mJhEbPyaKSjLHP_FdxHQUC19XwBpZFbw_Dqz1cay8If3jncfqw52OrFMU6vJvKcVwH-ReaQ2es6jgFj4UTPY32vsY168BdejB40wXlRvYpb7pmO_bsG1-dP7KlwxizeVIqz_bO2MoFeXxwbVmI9PPFWVnWM46Ai7GxtPovciySjX55NVfKIfD2ti-CFkq4RaBMRHhQ7LMsYIvTPjy1avjv0OV95MdGArZVzm4gVX6Q0nHuaavqRYu0yzF9sp1f-aaTFw-SON7c6jn2Errj9_rXuod3T2pOa9Cu1JfZcSVd5TPX79BMxdZFT5JyHuYIpQlQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=II7IF-8tJ42Pg7wSIb3Cg-BGxznGuclypfJcydKgjefuViEUqvonnU2SzRgATzJNVNmkYnAR1AMZfUSo834EUYchQEq0djX-t8P81BPU2lSPVchFS17stle0edIu1JWyuma8b1o-BtnPIfUrejlYTNYYaAJC2kgpyS4SF69_tr2BQkTl75TyqNMEoX6_M-vokjjrIM4PTvLLEQ_euS_oLhusKFPIT8dZiZnpWwY5EUWHXSa5yvzkdQzjdntMBXymzouhUSvCIKYeoC550_ZeTjPQQm6EeXIrXfMRztcUH0U6V6AXbz6CAOlqKnGMOnhfklftATD3tLR0f_X9XdN_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=II7IF-8tJ42Pg7wSIb3Cg-BGxznGuclypfJcydKgjefuViEUqvonnU2SzRgATzJNVNmkYnAR1AMZfUSo834EUYchQEq0djX-t8P81BPU2lSPVchFS17stle0edIu1JWyuma8b1o-BtnPIfUrejlYTNYYaAJC2kgpyS4SF69_tr2BQkTl75TyqNMEoX6_M-vokjjrIM4PTvLLEQ_euS_oLhusKFPIT8dZiZnpWwY5EUWHXSa5yvzkdQzjdntMBXymzouhUSvCIKYeoC550_ZeTjPQQm6EeXIrXfMRztcUH0U6V6AXbz6CAOlqKnGMOnhfklftATD3tLR0f_X9XdN_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWYPqwC_5SkNoJgvyP_hOSA5QQGkiJ82qKT-sNrU6Uin2gL_IONKTdd4jGHm49KSKvDIYEKyQeKpRKBx4x4mJevhzUB2S5fo2OGcLR2fCqlgM8Dm_z_PXYVRpstLRCFLwnB-LCpIrM6MVM9CPgUTNnpxOEokDy0heZjcsaZBMSDFWZ7NrqprTfmqnEkBBZZlf4k7TdMYMdJv1wS0D-1deaOJPeagKfwYxXXfB4d_D04VMb9SQuyxAZFClXnIcIeneVXKcY4Ex2zPBMEiuqRfeLJtYowVqibvEHRXZ0nNJDMiw_rVAeQynozNM3dXgD0AOJRBbjNkzXfhUk-cPtPxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=vS9GobYJna71TawFxk5EIDvUtF4S6sCZ5sjRCicINvcSyjcdhfr7paj7a238dpUwM3kdHOW2wm2LMOcHRcEEnbraFM2oT9DByIB0McdApDI_kS7Q34o58LLOrDSQAhHB0OK1RlSjzOpVfj6dbCy3ZBIEPp50KGC6RYWxTbkBt2a6ppNdUnfzm0s2cehXKTnfNr1tp7anjUeNXw6d5QVx4voROPcy_tQODi9n291lFelFfk43BtwrhCEFv-xIi9QJ7AUbL2PokvZxacnT7Ia6RuW5BzkXhnWhEErqsYIE3VnSfDzPKlJACzpNRAUJc2O2EUHojqRJOY6s-8RCs7u9sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=vS9GobYJna71TawFxk5EIDvUtF4S6sCZ5sjRCicINvcSyjcdhfr7paj7a238dpUwM3kdHOW2wm2LMOcHRcEEnbraFM2oT9DByIB0McdApDI_kS7Q34o58LLOrDSQAhHB0OK1RlSjzOpVfj6dbCy3ZBIEPp50KGC6RYWxTbkBt2a6ppNdUnfzm0s2cehXKTnfNr1tp7anjUeNXw6d5QVx4voROPcy_tQODi9n291lFelFfk43BtwrhCEFv-xIi9QJ7AUbL2PokvZxacnT7Ia6RuW5BzkXhnWhEErqsYIE3VnSfDzPKlJACzpNRAUJc2O2EUHojqRJOY6s-8RCs7u9sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=bwptCm9ahUbMEeZLZJsL1BU09ubLmB2nFRkooajO4kS5Bgg7VV_Eanic_aYyCLUmRGX_lG12gNkVAzj30a6LLxcSFEd8Kb_ZeTmwLxbgRhdx8KDu6xLIA7jqVMnPtkpYeWXYsKApx9s4bRZ02WS_PukyhD_vwjuYfGvoWV9MmK6l29Hi8oeBj-NLffk42Esgw6uivX-TisO463KjkUZyUcAsXnsTihT5QEf94aPupZw6X1lsw2dWJ8zgPLuU23DtFFHaKNX8LCSqWI4PTDGw053E2t3RL43s3NL6q9834uV7ytPFdCeN4y77c9OTdlF77jmSExO3u0S2eeoKmoLmfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=bwptCm9ahUbMEeZLZJsL1BU09ubLmB2nFRkooajO4kS5Bgg7VV_Eanic_aYyCLUmRGX_lG12gNkVAzj30a6LLxcSFEd8Kb_ZeTmwLxbgRhdx8KDu6xLIA7jqVMnPtkpYeWXYsKApx9s4bRZ02WS_PukyhD_vwjuYfGvoWV9MmK6l29Hi8oeBj-NLffk42Esgw6uivX-TisO463KjkUZyUcAsXnsTihT5QEf94aPupZw6X1lsw2dWJ8zgPLuU23DtFFHaKNX8LCSqWI4PTDGw053E2t3RL43s3NL6q9834uV7ytPFdCeN4y77c9OTdlF77jmSExO3u0S2eeoKmoLmfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=RwXwSv5sCDr8CTmf1-AjZfMN_9gee92K4yWGGfbcL1yptx0QRmA9cQkD4yqBEcu6oujr2EtAatyp05sPi0vXygVw-Ja3G4t-gqraakNtswSMeABHl_P-W8njOYEGYpW9dmXSmoyYrt2iDSQCe6Y3ExtIxtdzFVl4zPy7Kiig1-LtaMvwFwtl5LmTeA-IOEJNvkkFuvbqOUWhyg-S2jH9_fAzL92328jzSxrFRtQKjE4Mr06DtI_XJcSgSCjzZO_xQBB-SlhGAXhUQhUw7KGihf390smA-gbfDV8XQHE6ChqBHWelAOiflvpSPKATjIj0mmnDk_pUuaRNxG62pKoIXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=RwXwSv5sCDr8CTmf1-AjZfMN_9gee92K4yWGGfbcL1yptx0QRmA9cQkD4yqBEcu6oujr2EtAatyp05sPi0vXygVw-Ja3G4t-gqraakNtswSMeABHl_P-W8njOYEGYpW9dmXSmoyYrt2iDSQCe6Y3ExtIxtdzFVl4zPy7Kiig1-LtaMvwFwtl5LmTeA-IOEJNvkkFuvbqOUWhyg-S2jH9_fAzL92328jzSxrFRtQKjE4Mr06DtI_XJcSgSCjzZO_xQBB-SlhGAXhUQhUw7KGihf390smA-gbfDV8XQHE6ChqBHWelAOiflvpSPKATjIj0mmnDk_pUuaRNxG62pKoIXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=Xk7TK2y5wPNbDE_VAw7Padyim6VitJA1RiEsmG7-h2_7Fi_-nGDkOOOLvrV2nEHNzCNjlHIKoQtDDrpApEMEtATvA2qPFy42igZYBTsb5CouP3jJAruAvjq2nw_Z78llWyVIrTKDM_1qUzG1EQ4ZmpyiUW1Nu0x1gdAZPL7gi3l2vuHGtqY_I7Ax582SQZoQf2vxg67OfnpBsPEceqhPW6QKFtuQcqd6Kt4Q3MLJ7376BBTReoocyTY4DA6U9jS41WnXpZkdc0W_TJFKEFmTQMSR5xOQYFDQVLvPL3fWfqJlA7an5PT2pJkhV4HC0rGNCPymkcdOrZAb6CwIS8pbLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=Xk7TK2y5wPNbDE_VAw7Padyim6VitJA1RiEsmG7-h2_7Fi_-nGDkOOOLvrV2nEHNzCNjlHIKoQtDDrpApEMEtATvA2qPFy42igZYBTsb5CouP3jJAruAvjq2nw_Z78llWyVIrTKDM_1qUzG1EQ4ZmpyiUW1Nu0x1gdAZPL7gi3l2vuHGtqY_I7Ax582SQZoQf2vxg67OfnpBsPEceqhPW6QKFtuQcqd6Kt4Q3MLJ7376BBTReoocyTY4DA6U9jS41WnXpZkdc0W_TJFKEFmTQMSR5xOQYFDQVLvPL3fWfqJlA7an5PT2pJkhV4HC0rGNCPymkcdOrZAb6CwIS8pbLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXHjMB0cI_d2QY6cjp2LCt73gXuBthqpk2uF5e3qqfaHXIPKWBvN-KqAMjCMX7JYzrqzXSaagVpf3LBYMfmNLTMCcmW3O2o47WqJJGs370kEYaboy9oUbeEDrI_PxvRWBxGMtPisS4sDX8gcudj9-JruTdiWFiqEFxmyCOa9zp34iAxZakkPiNMVnlBP83VsB6h3PkJjL5VSymHIGTy3MgAc3VzBN5BKZ7zt7Fij0mV9wzbbdq15u8lmh-DCQlWRPTqvr3yz-x_HK5w-nQBpUL6CySAWsIho_x5Kuv6Z407aijaHWYYfbFOeORnMv8H4WqKFJWbtbQI7u7j1vkaMOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkJRCYPzO_ukS58XAYwgCP-Yt6mWvLwOWCd2Hj_JUEIDP1U7F8Kubpl1lfc7eQml6ONZEGnkzXhNr5PDuDd7iPom68DjfqcZBDB48ELToVgp9Bsnym_QQnzJyS86TSVpb3rgh1lG0Q4ZT_3W8u51B_EARtUQuJfLRQuumDwBwypv-apCfe3NzehTVQNRjqCeF6hh9aonwR3MG4ic3p-N7wELn5rRMmHkXN8K687FVjUhDLNCevK9K8hSGn4btnTClIvLqxwvEPq18-1-xwLe3fy83_wFeyNjDT7wPqMIis9EmlyGl1QSTqUMTZhBbsGnr1ApK0JKT_0nWyN406bCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1HE1qABqTyRgrp9IhnLozxm1SDvanFcMUZEkBZRyxQJKZjCS1Db3fyTJ2OeAz-AjgD1q26TjbPNNsrWDVej8whfHANIpeDX5Ys3MFFhkuFfrgticfJ6M7mtQO0RNdPD-6GZ4NDmdIM1YitnFwSALhXOTE5Qo4eXqpnkO00uTkr7_ubbTRrMUYFbnlOqpAP7X8yVm302tiL9LRLdboGxU183zQylK1kgVYCOGEp4WviMexfsnpF_S0FpBTzID6v0dcW_f5kOOEhlTyyd8I2XGlalVma2LfszmkaxkDbf8NQWw5lSLXlthHFsDN1glp-Zhx9VDLsHMjPFuHrTYMmqUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOrxns7cZWDA8oKfBMCRnEalVfRopqpB9leAGT57tj_-37gRXG-lwQMrwQMou0GjoncEWdYWuLrE1C1pZ6wNFrrfomdsdbtc0Mr3O1GISSTA7UsSjnu6ypERKXwAR-7WCL4HbHMaN4Yg1ZntVQ63_dgnfwXW1jVeOyyT2mqrTBExodFdwkmMz8KTnn019MB1sUeoC_tBX12ITa7SdKKV_qHyMQJjIHtda2aH8M16JVGGZJrr_nQueY6s6EVG-czGbjDuiS8uBrnyOw_C3T15_fM6C4M_nYa-knzjgLgQ4m3jfzqxRRWydnBrMRTQUuyEaoph3hwr3MqWoEb3w7of0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg_Iv36wxdmyyYPIhycp8kOO2j8_ax6HsHIPvAzkHd_y2dTZ5pPU7mQ0xiXKDHUzoStLuORX7Mb_uSRLqq3oqhotKRYc7k94D5l8BGI_w1UY-z2x2FbZqzogratO9jLRL8Oh2_Rqlto1gFSpeKLXrhD6nn0pFcNAtwQPNbhhcsmjiHCBjas3BS1T0JmmC42Q4CyDRFbzmxddHkM6DaWvVr2joUk9rsAZum-yeNGPi1fwlj67wWwfYCbue4I8PaBLwiFVk0MauGctgfsjlIIgNfo01dYpbcOCYaopZBdDQF6zr3hGK-XiH88aGRcZ14r7wZfikFYXHHYSmJh2Nre-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQh7Ewuc55xEnEqDQP3vAbB26FqQgxfezBrQmaWOBM3mG-S2LM8OF42GPMLYsObZ6tlWHUvOD0EQYiiDT9H-eMfpuUWYAMxh9h7UL_n6Dr6Glk2_I5QSaKvVaZ3Kjg-Hf5XHGqRyOciTNStnu9hAUxOVEw0cXTc4Vz1XqeXwq7sHRA2ZOZwKQ2yeUgUbgTJcciRkcQ9pSvQMXgTTXzYCqdU6JrHatJH3XPTtWqrIOyvamssDSbngXakC5O9dD2LQl2B7RUK_VB_Ia7qKOKY1qikZkG-nPrewLeahG30OdmpVo1YikryUGVP7dFsi1TUfi0XQ3_J5o13T1jawrC-Z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf0hx6YIpP3cEK9tDcNjgCbI5ZU3EKRymQTS5jpY91Dzpkc_DvjRDVmNySOBH6RbnEthkGHJzgaCOgP8B7SijMvIXrpnfrIlhZcCvn780yjqD3e1zlX16ZuVcTSohjOSIyrxxxpQqOVWdQdat8TkbbxnjpbVC7iTNMsSvCzTulFN2htQ24p6V4eZCZhpw1wOMRFGj4AlaY-9-QRSAUkxlloC-2EeEr6D31eSRdSvUtWxWDJHlTLzhnF4hYWFQLHOB9_IbCdXJ_lITdCDjzEbT7vL9BHhTJWpl523qhacfPUixOJV7SnhDj1om6xMjMQlV4VyG0BQzgArYeHhcmEg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=S6KGu6hUPLC1iXqONdpwMnzwbetdHwxLMrAyJtsqxaGMs1rdAaetXt-U_ZUpbixRmr-xfMfMrtlUN8ioIb3x2uF_8WIX-JJGqdirJzwyVGOrg89sO-N0stJ_FiPZbkVS7s7H9Df8fax6dJTIO8bbpCZ83fncmPT5Q_r-Wp8SmOEaL_UKbLCBXYPKJiRGDjaNq6T48HqmbXF-KqYExk3HP-_Z3VXBrsTrgv7rI_RS22EMUvAZjy-TL5PN2JHyR5bvQ1RtqWeZK2P3VMUuQgZwStTFsE5FeftIasIy4-lkSeTrpPwsLoHMjFjrfOA0LNOop2m3eUOcGvPIRDr3qfqhaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=S6KGu6hUPLC1iXqONdpwMnzwbetdHwxLMrAyJtsqxaGMs1rdAaetXt-U_ZUpbixRmr-xfMfMrtlUN8ioIb3x2uF_8WIX-JJGqdirJzwyVGOrg89sO-N0stJ_FiPZbkVS7s7H9Df8fax6dJTIO8bbpCZ83fncmPT5Q_r-Wp8SmOEaL_UKbLCBXYPKJiRGDjaNq6T48HqmbXF-KqYExk3HP-_Z3VXBrsTrgv7rI_RS22EMUvAZjy-TL5PN2JHyR5bvQ1RtqWeZK2P3VMUuQgZwStTFsE5FeftIasIy4-lkSeTrpPwsLoHMjFjrfOA0LNOop2m3eUOcGvPIRDr3qfqhaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aA_KAcaRjFeQRLxHIz3A_s8nEfQg6aGMnEyjVpYLaz5x-NcTtsZw5M_42ucaRvBOk0cjZI2H4gZkqjq8uZ7rQteti5u1XTSkqA29gNQbxcmROiUygJ3-uZgtNPsIdD9ss5vzPtQTtaMcDIQ5vjuCrN2ouYMsTxbujF21D_KqS25ObIqcgTonP3TcDsLeMTIVQNMtjogJW7nah1s2IGzZydVDUYJBkMUwhkiJAp30xrOC6ziuxbnSTzwZ5KZFftfFze1bIYnD1rO_f4bj9c7w7C6DqdnIcbTg714JqjVER215JW6K8U_hsTCWb0xbPkIk3svzFixtgsXG3wE3jFCJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQGHPPK4mhHqg4ZrEauCgiQNXSTjpSBvVl88Xe0kDbWBuiyQAMlr-z9ywIRkaaSt-Qx9FGKNGQJJB1USNJ1KcjxQA-gVKt2jcoi4mHeRxwvdrBMMP8oVgZ6LCUxkXjI7tUSRebjZNVySWiy6kF5bKbJk4bGJy7iWFE2NrU33wsc4XP-5alJ9l0h5bWTYzNnEY-Qls4BzKmA0DvnHlysCe2bMH03YCkvQq3PkSO0D-qUxpFcIzTa6FOwv_zPUt-6FsC9f0VMN6Xal3iJfTNbpHshUg2hV7ASc1t67tb0hm98knsXSHZnQX-LkeIx3VL34d9a_xJYqxOU4o6BWUrMFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dlWe_88ii9J97szjVOxwrfX1PMiHPQr6eHWAp9uxZisf6JkoxiyQ81E-Yi-S2BAxa172GC9xZTRLRXg_LG3pZrlfHKRvvqM7U7B6CSccm_yvdmLaj7eYTts_ceIHGVtW686Y789kCdVZmDXeV4Le_so7VOZcil0DKgu9IEggkjA2Cp3t5BY1-_AqZtk3TMsf0mlgql_cfrxJ3SHZih7J1XGUCpA8GSp3U4HBNFIiUvPXipBSYS9fjXHsr_TJncuEsqv20jX71kF2b13BBobdX9F9KU4t_i6SSWDgfC9nJAee34Vfbh1uEu6VAD3ealEbtC7d4p5O-zzm6W7k6YN64Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfbOIoPCQ7_0aGEwqniUdxk-AgYXx-aMg9CIlT7y1Q0mmCy5XEAGb_1uPuNd-V7lEYmjhCqiZCAAxWZkAU1Pmufhns8VQWesZ9cubpAryx1OXcRrEJnt79UQp0tWoo5t0jSaalQv2sftnMyWQX0Oy36_vVa0iK_JCLjf59VM59x8xQRskyNhF4kOu1N5sqoHkLrPS-qFQRjunlsVWSU6PJJ_BnsFnZDSc6WZVA74SV-BqHH6S41vHEhcv7tGTscmyFC51ldpZvQnf6Sj2xOvOFuNyILhyi04LEqUM0MxLem3YyJ9Oc3llU4YPrUen0kgQMq_cB2VI-yKOUffrPHRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XkVuwymlFZUdxd2uzP4g7u4dK5ISLrEJiNm9xiDXWEMqQhTh1KviFrTBuzmGMLKW2k9IfCQXYMRUPc2-9vUavg7kZisP2qWWRYRxIp8iGBO_7hSOa4GWQhuJaWlGFtzSxUQmHfAI6fuBwdOcuyat1JOV1nd4n7cVOg7PV86ZAAylScnknO0DyzucasSnsprpbCtPOo8lEK3cliYHG4BFy1NEoAKs1xGzl7L-heJGBHnxc2h-EQlJPlP4frDVq6MYCM6dH10ehD1qAjpvrW6sh5PhzpTl6COWQfSGpa2Ze9G6x0MMhqj6LTfdqL_1EDEM_FJf6Ek316c7A8Rv57t2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGGxf17e8COvm6WZHKcgGeDt1uMS-WwbFqxqWblEc8r3hhAwroeBihr5bVcfPGMSHx_JkGIH4WZY9-4Ielxv7RCc5XJ0o3_p1q_sCvHUWlrghpbUueqdLFPAI9TJs_cbKsEHhvjfpzRug2uCArRlB-MLIHPvKOOSK2vb8uAtnpzWoLi2FA6xw7Ie2I-WBjUvS1PRX041M-6GEtX6JxyEUj0Wqsk3ZVvDeAciPjznaglhkGDpdnQHrpCdbR39V-IFHjIrLvGXZB-PnujbJuqfDL-Ii2hqmjL4o90xOcs1cAsLjmFT2BVGLW3Je0zWdCjF4FQK3sQcdSDgmYNQ99s8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1aZ0Z67IZiKD87jNfCBPKPsUjS15-SddxvBztCkheq044t4oDEgoHsuT6BRqdLqd4uEfrkyOyryhoKYpDt8FFvg3sFODa0t__AesFCvU4_utW1WrMiugWQdakvD1Z16dK25BGCXo0VcEID4HwfO09TDAHVajBn8JI3esSYn86Js6DTiO7qpJCCmCqWNLb5SVWi9b7EJINGoj4xPbJDkCLxi2IyqUHVhpigalAzGoKEI6OTJgUlRDsIuHrhq7Q4Hxf1REwxHk3metToIOaa5GbsWpA3HmB16Lp4aIHuucbj6szhjv7TSpar1tpoSxv_bBX5QFYhzn9nQfYZEQZlU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLtJb2WtLPBHkOfwHOjWvRv07idTSOT1SbMLhWe-0N7pblloDq6xRo4lSuxqiwLzQzCoF0XzZiVch5BGQ3_2OpPRUJPdgx3Ej1zgMhir50wUE-D3-Hudafj3CDr30GiIHdcQtD235BbJ5keQG4jclfKr60LPl7NjbGg5GSEEXFsVMcVfQcf_KhofW_YSAhpqfyZxVlPrsapojAfY30su_54PAisdYm9TX3nBN8HDMaeT-ZRb6nJ0yCqfWZlDpC8m8g9q8vPO1cLQ_hGkMQ8L_bjc5qjVtH7mPBHRh8-q0MW3aW9yzEJ2hiwnf8VsAxs_qk57c44VLXaChsI_DEfjUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=g75ytCaShff-9Arw0GfN54fcssyjU3Jp-v2bJ4rpB994_w0ciYg-3E4Qb4XQ3w1pXyhVUaMz9BZQ6byWS_VJzMeslfCskUzhjHX5rtyG0qnEEBnMnXxF5j8V2qzrPPQzTWnE8kb_Zn38RLIhmijqdz3g5FICQXYNAs3GtG_a2T4u3TRoxa8aIZDivZInBSmr45SHTY7sEF11hMxUlF15hULfaCTRiDtTzAycZlWdfdmea9T1VoWVRK7FaTWeEMc1-spiC9mpH1AVCl0Q7J17jbC0vpgw80GxNzOx6eV5QErSd99-InFvfbeuTfosavkvq9dj8thhLx2tdIk1mgaSbmcfyA6vj32ZXUInxlsAnXwKjbDQj3e8TCzRCLMbM-ZcI5LWB9ISt-h_kfidHhycHwkv939RJu3goiq2--dg--cXfhuaBmgFl9vuTkW_bgA0voMuuUopAx-HebvAc5DdMjFgQbw8bXixDtBDhGYH7wDMbNz82nwgkiXwIg1ZYev4rw4uTy_BKFRvTUK0oZ3-TwTDCK_o97AljKr3tJVhFC_xz84oHKAs2N35bb6g_cYEbua-d-mnrkZ7qmyn6MeT5yR8e6P0RvHURESpF6mvfYIEE4qPfXIZMNi_8M1wDGEuAXZuX5HeeaYsuJyXyz0ChWmde2HVjOcaqOSwGYl0l7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=g75ytCaShff-9Arw0GfN54fcssyjU3Jp-v2bJ4rpB994_w0ciYg-3E4Qb4XQ3w1pXyhVUaMz9BZQ6byWS_VJzMeslfCskUzhjHX5rtyG0qnEEBnMnXxF5j8V2qzrPPQzTWnE8kb_Zn38RLIhmijqdz3g5FICQXYNAs3GtG_a2T4u3TRoxa8aIZDivZInBSmr45SHTY7sEF11hMxUlF15hULfaCTRiDtTzAycZlWdfdmea9T1VoWVRK7FaTWeEMc1-spiC9mpH1AVCl0Q7J17jbC0vpgw80GxNzOx6eV5QErSd99-InFvfbeuTfosavkvq9dj8thhLx2tdIk1mgaSbmcfyA6vj32ZXUInxlsAnXwKjbDQj3e8TCzRCLMbM-ZcI5LWB9ISt-h_kfidHhycHwkv939RJu3goiq2--dg--cXfhuaBmgFl9vuTkW_bgA0voMuuUopAx-HebvAc5DdMjFgQbw8bXixDtBDhGYH7wDMbNz82nwgkiXwIg1ZYev4rw4uTy_BKFRvTUK0oZ3-TwTDCK_o97AljKr3tJVhFC_xz84oHKAs2N35bb6g_cYEbua-d-mnrkZ7qmyn6MeT5yR8e6P0RvHURESpF6mvfYIEE4qPfXIZMNi_8M1wDGEuAXZuX5HeeaYsuJyXyz0ChWmde2HVjOcaqOSwGYl0l7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=nR15KWGYNTIFYiyjkOaFRupQ5dpTEmTUH8iRHtTuXRJ5CFHS08smPuTc1kqTTFUO3HAYmpUh19f_G7Fvq3oSyVFOoz4DzYzVxO0RHEB4vi-9zXB6pR1WICfoQSvczD1z8MpICBkUvE-aY85zjE3_CVecDUck6rOSSyt4nDkTDKzMG9vrxIRK1CbkE10HCGx-BfMhvgro4v2McLMN7hCDaQM2JomfVkWuH1jztWcTdyjx2l7RfOUCTQ3wiiz--ZkuRARD07o8EjgwQws1_aHwwcPdzHimSPmD1Sgs0Q6a4F-FQHzp6k_L5HmkQq3gNgkMeDi5IBYLjnoofjOlQHivLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=nR15KWGYNTIFYiyjkOaFRupQ5dpTEmTUH8iRHtTuXRJ5CFHS08smPuTc1kqTTFUO3HAYmpUh19f_G7Fvq3oSyVFOoz4DzYzVxO0RHEB4vi-9zXB6pR1WICfoQSvczD1z8MpICBkUvE-aY85zjE3_CVecDUck6rOSSyt4nDkTDKzMG9vrxIRK1CbkE10HCGx-BfMhvgro4v2McLMN7hCDaQM2JomfVkWuH1jztWcTdyjx2l7RfOUCTQ3wiiz--ZkuRARD07o8EjgwQws1_aHwwcPdzHimSPmD1Sgs0Q6a4F-FQHzp6k_L5HmkQq3gNgkMeDi5IBYLjnoofjOlQHivLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLobyLLgOnVJzVPtyJG6sVyk3-EoLaSCsGzZ6oP_P05YGVSoBdQFXE9LqXZvclbPW1j8_PhbWEuTSpMG14sfhLwdjkmYY3fMRMJnB72eGVTIkDpYhCsziiHFsevbytEZkKgpoRQwk2e2JLZnbXNtQpZEwa0Cvcvzyi5iyBamBuJjXXZ6Xo3-mSud1CXa6x3ftD0hp_ctqvHI3iAk9N3e3fFZHDxRLRAW_4pzxHYxLBfGtmVLlu6VcgVpho_wpKIlf6KHWK1j6yLWaRFVn9159LliAxobLdNkqKuitCCm4yab6KBN-rzyaaujl2YTxnZVOgSkgujyU_33JtZIHqR0ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiTU7IhVYFMreuC8J_3v4xTDqcuU8xQrg_WDtCqrPNKXmKfhxpJyuCqwKeZJDA8yuf_noTurd_qIXa-QOjI1S2JmnNQjspMMW5KHh-rFX32-Irm0XwX2EoIPQz6ck_xDB1xJxZuHV1RXKH24WjPtleOKm08Y9mq7ee2UZ94crBT3YXIMLp0ny50kxJk6woefu9eBAAsOOUuv3noaUGBXy6lCc-LXNsVKrfjzLDqSTT6Lg3OvKwomGcXaETXHwlAWigYAjmRhfl5OE5s57QgvXfR4wbMESn5JMvWONy2cBMUcVQWwBSQRQLP7MM0szDxcr4TonkCb-R2NpHEBqF5FKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiFO37ngwSpc1P5skroKK_gkma7wfaxyWlccygfxBKKkNm4kSwc--0TzYKuCJuEPa-qkEZOkBchjLTj_EvkrVGWA1dqo19QfBYScB58JavGPXVRJ_UnV895AqZJ8tj_kPIEXpoeEd5cB8xHWNQdMsK4t1aSjTPYkDpiY3Vi0eIeoA2QSq0T8LzS9NgFUFg4CykcuEuu1YcZXxid5DlE09x_Zl5_NpgWPg7Wm5q_UUq9fJr10bfUGfHNoMSxZWiVDgDsiU_54q8FtfDcDjyKKFEmZURu18mcCYbaar82FODCRzMlHl-p1G4CpZuUmTsOaLtoTwD5k1ZZIbeIl-bplSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG_E0eyhTyu3ijyCKbaRUfC31mWGykH64okshut00A5r2eo0gBE0f5BBWjNSQNf-5W9MukXMPgu0IHrX06ZYVKGZtqA7eiyLj98D3mlWC5-Is4YaBN7k2At8Id32FWAsLzJfxvEHvtiI9FCYRPMAcCbsY1RdZ7niGMFLN-RZ1T821spaFMyuuccoG8xwE5nw91t-vlzxZz9ctO_Td9c8a7DOtBwpsGZh3RLgdxSsi5noQCKxP3rgXQ2Ie35kG8Q8VK8e7CkpBkmKyrX2lOpOMuHCPCOSdaowIY3K1y4TeMC2bpzP2St0AD4wCIWW6-8aI15MHZFk_bnEZpYRubNoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f49nGcJ20E1i6JaqTr7GcvquRDmye5UzmVdcdko2BVdcYr0Hqq2p-tzS35gOGDuVp0RVQP5OF1h5JPNI8slTSp5gtz280YdKvEAqn8VDLWx3n1od7VbiMOEsPc-_TEPlpPAnp_T9GBsivaDK8XjG-1xa_cuDEcrYkKFglbSHAALPW_0b2cYjwh-s5iIHGR3-V0zBIlW40Mnt3_RyAIpgXWfFZYV4VQv-qVnwx4F6OLXAAM6Sy3hp9D5n5hz_uGPWrictGbS_kDcP1132O4JrlObPO7HCrQdl9DpJL2jtczcjGhNNg_nd-eUVoSdiYHXIpFntbLPPk7VvAVCClLdtKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmUBxjiohmAkaSckW01lxZpF4Z2ef_sqHkBCHiP4t3rK_YL2zzl2equ65mMUnQ_G8oS5jN6i6Qn71XWLjFct5_U6yNJhIOH0sIqbRq6gpWzsfHi6upk04mKBCF7IrIOfmiiP2cDRzfxO27bg2nhad5vvkCwoimg3sw-4HMFHmgM2FZSrxmqL17vHYtxqv92UQK7nHqVXh-uZ_IcJmcaV4wH9OcTABmDqdZw-zQNv_1mU0qPW8fOpLJ7reU1L1EoMpC3NTLUNEUImP5VxUtOoG-aKkwtoF0-2tvZqMZAdBPg7xmPAMfAI3SGZqHlrmFlfjw_6yOm13XQ552TuN-3W3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5BT5z_GiLx48PrP8iHBxzc_awzjtPedbi4Wk34i_-sYq93-zDDG-GMW46jZ1VuPy-912vosIGqmsX7ovOVxofxYveiPTRTaB1G2L9BV0LQGsCY__zTVIKAlYvryCsrY0CxhZCjiDBTU6lqDFKFix7CmicBDznbTKEjTtFuisM-exvMbfuBHLm9393DiuJVOvV-i7BuydVtBKuZzX5BZIdxQrgJhq-6lSMktHNOoigLgvdJCbzXwuK9tkhG6_QaZv1qvzHn0LqPbXxddU_2yDmUWpWRgeO32j0jYYh8-nkhC85Uo2NuJi1LWlGTthg1V-IwxlyEGCzdsJE3_muNZPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKxJYEriFRwLUiDmD1yJRhP7rc2Cwc7P7fu_55wQSchnziio0c9-7MoQqX0_rEjCn_iVgU4wHXVCR7C3Aff7AtQ2qzM9QWIKJ_nfD9LB6k8gHwivJSmSHMkWX10s6Zu3DCd7_AFTvCJBskS_WaToYq_MBGuALYdF05v_hwrZkY2zhIAKrjSzs92rVDKJx-Eys4EJuZH2wf08gaOGQFRE5BeLEeN1v9_9yC6m-X_Otn0jm7flCPtDr15ucuAGdxMtOBp2HtRTzaAHc_2Hp9sIFMhgnDCeBhN9c8NsV9ubxiOnUbQSJqRKAI8AjUCQg_14YpnLv4X8XCYrT-SIGY7tcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJp24I9W4xCHy0GpQK0khrxh2jQu1adE8GahFM3TFd3mlfAFEGtXJuigEZ6ME1gABFCXg7erDPuZPolPMCalRZPeYz6OIYgBnlXJoL8rsBuAZAmuN9XNy_apzgWsYP4pX2U2c1YmJhIXSnjEG96b8K_RYR4pI2WI0XrU0vYot2uLrw3i44ZL9vjaYWK-ucZCu8Hcx-wNl3UnWVNOn4oR9_yoyMYrlwdmWm1SkLAlpK6lQnRlzVkEMzdKkti_nIn4tZmJnPohrG9VLmolfDNJ7vF-Cq0zAIEW3OVVVz1o5uoXBlCpTXj24Wso9C6-BVZcyyyrvvew6GjdXvYlI9Vfbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
