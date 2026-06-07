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
<img src="https://cdn4.telesco.pe/file/QpcFfaDThY3BvG0_KwCOuHz9pZtTikXOiYxM-puMw20t6md_vRPfnobrcl-M5z1_MYzllKTKz6sAkzkn9PQ6ORlIaXBxscpZEubJDqiSp_6Q-28PEAzeOoCGpdsL_a4T_uApOu-DOmzXqBOwGck8QtPQ2TSqJHPTKlZ7VaOyskyXZC0KWagLESW5BfOWWC6u1fdoxH9w30jeCFE74CTnuJwPkPmuw6IN4eLCYRwe2EfQOz1sePf-MA000DiQLeJvhg5AwySM0QU1Whoa55pJBKdhemf_u3fkKOBwsi2AinWlw6Kq9zUWOfXW6MbuZgF5UXOAbg3fEomt1ljXgnLaPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 16:26:06</div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3k8KY8kGJvAP2AAndTAuIcDP096hiOqHTX4vN__zSrCUG0XWofcZCTx22ov7tmWhSiTc-vF74teZiqGYAFjm1a6DQH801ylGKPGAdqcqOaW6wViYyrTtuOfzifaUmsM0RwwoyV8VKlihrrsyyJpm9f2BD31PYqOQpRtWvIrhxh_Lde-QQMSYONGi7tQt-G9FBVZmySHCZcKOLvhHTdUNu3_NZRaLZeH7F7h5Vn6ufiMYQb7fokh-SNt3LlIBCawziVsp_q95a1wCExGQp_ayPotx57smXhxGaLlpPzT5FPSdrZvIbWTaNpDp-SkTt7fdVRt1PMBIh0ZmVKn11t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwsBSRMMsea8Rh-Jk6A36yJIVd2Vh3LgTWw11UH8i3TDitHOnAV7q4iH_7z9w0o2FB1l23z5s9UJCcy1DnMe_JwKFIBhS0IAlMEL2HnSPJSSEIDTTpD41poQ3z9xA4rR7FqE7zH03J3vxG6FsOTiJ_myZtzB5f2tdMZKCX5fLB2z6_84jpBkG7RrMfHoQW55-ajzkvQQdVX4kIkSlpkHTEY41Zy0yN9AFJbRo_WSGsim13CLiwBJhh8DrtrGjellCD6HETb9tuIdrzSPDD-YBRrN_OUV_huG0ScsuRwh2aMU1kOBD4qovMYzuEVwyEqkcXYtAwi1LWvSCxuJ28ilKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Rb7vOKXYANEkdTdXUwNbKtOg-yTW5f-WxScQdtnNehTCQts1OMRXGiJHXuN-NvzLsoAbMuXaSRGF2nBuc93ChBu9zXRTZNqoy9ZTksUAp7KyDRfB5kjDi92z5gNuHB-5h2tBtgdb-8q2hY1A69K2-ted5wmOLhZR4FTjAn_Apr9ozSJgTRLFO4DCAeHIZuf-kpTCp20N5L36G6wCxcgJbJ5dPD_as9diM04QqAyF-4_kET89Au41qQdY5JLTuu8O8Y4Of5rUkaAMBm3J1fgTxJXIUHQTBPYVoLOwQYpZTJzsvYV1E7jkuKx4VW3oGDfVlPx9bbXLAOkv9_s6AgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ1H0l0U63-k3oVaFUXprFif1I3hz7MLvyLASRAKYVzXwq-YPOuaKaldefYN2HQtfKmPkFSQByphYfBBrHReqUTr6e-UbMTzqk4XexdCWR7nMGpftuH9FKK-9Ku6OKw-tpVepXAaYV5Y9-Ld_wuCiQ_YSRgOZME-vVZQgDF79kV83Wim5N_5ADJUCOcdGZJuZuwpIEeKAOuNYgG1LhEAYu5mRr-MMzbQEmGna9-88hqszGhBjP7lpkiFzycaVBNZeQ6OI6gXHErGhEgcHLj4SzyrU_HeMiI-YN58d0wOaXAUfm_LqDNEM_yZ9avXs2VeAV7RnBFJPHypQ6g9vdV2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc9qTT9iwE9OJXleQEMWUtY1qGHNtmCLOcWYPRHcsYRu7u6r9zaFQ-G3-9m78YIDR7mhZ-zySI7UjkXz3a_N0UnsS6TIpMV2CXfQ9t8JHSU2ECFyXGad95KzuceoFbW9SjOd_hKUq2oAnQd7ABPsMVckLpPDUnCJI0R3Ym0lkRTm6ogj2rGHyO3sTBX1OOdYuGbY_Nu-SmMrSFABC-Li93cJ9ceecqg71gVmxkacUgC6AHgmMvVLT1EmyIXY73QkjpHol-PMMpwbNh58dBLC_nm9NkySo77YQt9TEGTd0h0HeJqfIznBHia001WN1rktoWu49TIxexstxvYXbNPd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2-CH53y7F_vB2Ipzbb-_kx-yUx90nTzaAgkj_mPOg7jpzZuVr5JNg6oI7fYN6NX797OgnnFVK51IRE2uLLXzljI5DPojkO2SGrpuQTp_Md6fXhzm-ODV519YHFmM0ygZ3qV6ZG_yXjh1CZ0w0kFk79O_XwdXBdNvrys-8vmgclYHkvLQEH8PWTlDiHxpuEoxyFbrcZmgV05zkv6RLcSXkQFkXMB4zEd93XCZdqprGSy4FXpYZdt5-VStEJLxG9KBQYPt3ahG1Hr-nmJG10TiyUX53mXct2GYmnTO2iTcGokTPAyE78nfhbgQfXr5Ff0MjuOifpzMmn3Y0mxJuF1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4QEcS3xjni5SEku-2iaq67tOSDaTgNo-Ih2OM8i-rVly9gCm05hn_Vr6aYB9BE2htzUZgkwYwNSg4B_m6ZSZzeDzeCiMoP-pNt55EJSqG1L4MIbw7YeTqhXkw6iSI1pQpthOm8fM2yVoWZR_R6_AuvSAbaoDfGBseT8g1taGppzjPntwFgIL4pSh7XVj-sNkKoFPEgcyO_tp6qg2f39m_RBCe4zBoGck2yINP9Q7oq4rWSHuTE3loI4q4wtcdwEfVSSrdalq2iU6N-cwihbt9zz7Yx9lQ3iGaOHzu3htNbCz6Ne3QNJueCDOT9fH_XylwIe6KwQXNe2J7PGPP562A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=kABsRBvyj8Mx-HPt2siouwlpR1spi6DcaOADhUPH0cPyIAyUFxZplX4rwzM44He0m6mhKMh3BL9HEU9Gxp9IdqGoENJ-JylA-grAcmHn1Un3wsyM148lU0Xp_9H4jqsVYJLTbisCB_RWYRNaAK54gRri-cUDfmrkEiBx4-83Q7Fimfv-p_HCP8weyAhNuM-C6j__dpr04LbGmv1ucLex0efEfMPQAGlxyrGeWfCQEtmbqgLslVhRbCJ9tdVgt2HeVoAeZrbCsAS5GylE2zMzDW5oMYwAZwQ4D2O6cFDtbiZAE7U1191xs7YoeORYsAt8ayuAA5P6KBUUlA31NTkKyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=kABsRBvyj8Mx-HPt2siouwlpR1spi6DcaOADhUPH0cPyIAyUFxZplX4rwzM44He0m6mhKMh3BL9HEU9Gxp9IdqGoENJ-JylA-grAcmHn1Un3wsyM148lU0Xp_9H4jqsVYJLTbisCB_RWYRNaAK54gRri-cUDfmrkEiBx4-83Q7Fimfv-p_HCP8weyAhNuM-C6j__dpr04LbGmv1ucLex0efEfMPQAGlxyrGeWfCQEtmbqgLslVhRbCJ9tdVgt2HeVoAeZrbCsAS5GylE2zMzDW5oMYwAZwQ4D2O6cFDtbiZAE7U1191xs7YoeORYsAt8ayuAA5P6KBUUlA31NTkKyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hexRiiJMZ0ukApaZQ617IsFdjyeBE4FB5QboMMDNDOChmuVtVEERZ-B8G_OgYzqKQiy3mDc8-cKxVnWt0KV23KS0pzEhOVVmxh2ooC7l_p-iw-RjssL8VbhyGW8tGjZ4evGAAJfclh1TsjKpwcHWSGo_nSHCbdLBt-rE0ytZncmT9yh4iS59hYJYEQPbFN9FuWPtjrXMRAkwmehI2Z5prQ7L3WbTKxIS3U-PX4OgpwXH7V60JHcWQs8hvC4T_rbbzFf1ZgVjMuAOP89sBt9FwV3FXNRqnI29NVd5wE5FRKwdTWEwFtMGnHSw7hhZDMlUtHeIpFuT2NrtQZzOVV7KOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=r-4hK-LFnJcl-4EiqRqCPV3OmDYxnfN41f12zxpadp5aSEqwW56_Wmi-azDNhRsLGaplP6oiluRux0wAsZ0J_0e3r1UmaVQZR50oxDY5HnbUkvE38_l951jqKzRKWZad6zJOF4BcJA_THYMJ53WJsar2Cr7mGXYUbtHuBXUVUKfZS4ZBKJnMkdOjUShCT5bNj_AJMyu5rJd7ApALj2l82A-u-rGbGwPMj_MeDpD_OhKbjGJLP_qqvVQ_FGK8vfEcw1sBU0YRp1ZCMgcmnx2woKG-TLhZKjeYgyTbG_yANccHN981ngoS7ciAKmzr64wn5iedZ-embvss1ZW6kBYPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=r-4hK-LFnJcl-4EiqRqCPV3OmDYxnfN41f12zxpadp5aSEqwW56_Wmi-azDNhRsLGaplP6oiluRux0wAsZ0J_0e3r1UmaVQZR50oxDY5HnbUkvE38_l951jqKzRKWZad6zJOF4BcJA_THYMJ53WJsar2Cr7mGXYUbtHuBXUVUKfZS4ZBKJnMkdOjUShCT5bNj_AJMyu5rJd7ApALj2l82A-u-rGbGwPMj_MeDpD_OhKbjGJLP_qqvVQ_FGK8vfEcw1sBU0YRp1ZCMgcmnx2woKG-TLhZKjeYgyTbG_yANccHN981ngoS7ciAKmzr64wn5iedZ-embvss1ZW6kBYPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DscLiWZKfnhdVf12hP96UtRo1FinCGegFuazWpKT8FUu5WkaKWDo3FL8eyzOKgGjfC6rNbheTHBtdjQqVA25tgvFN9SpSSUMuSAjwxdmV_9byhFx9kxZQaJe_DXQBC1PYAbIAiVkryWcMPmUL87E-x9O77S2FkhsTnLfm5cZqB36t-JB2iPkRz3_MSj--ExN8H0sbg5-m7gy2rNQh72JWvPCfTlYPEkccUzpO8fFnc99OU69i1VTuYRmdaMgFS-EI7W7CFf0UOUgSq09paZ5gxhkF-joOebee4V2DTevGMQkEGSAziUtMXzzhX6de-_RNvWyAZdAPBCSqJOnfyCj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfz_n6pdRHUcjKTHM3XeE1gt_3K3byRuPdIGOLkAO1w1cVBTexjfyQQlkoc2G0M2gCO7HSiJP4ES0tbsM1abrSkokBUewzxq7wUAbokncB78Y4h_0Or_Mkl-rxssxflE5ostPozEkK2w9zNY9fhmwr1cAZVTw6yUpN36zR5xD_6t0EyYrG3wlKYM4xvST4tDdqTqI1nPQJKOuIBE0kUpDCfEJGcSGnTIiBa61dSQydsceSfspzm9fgCAE8CZxULlgEfyXpsRZuNZwhECEHdc2BY0WoOr3y5I8VzFAGeCF7ri3VWuOhCj6TVgZXNzTssxSp4UiHOZDxY4641h-b7cYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=tYBIfzRe9i_cyV6ZdmJCT0RbnO66XtJA22UJbG5_QFD9mWfnb-sPntj-XUlGHCYmx3eFAwFfJGdchC3tGNOTQ0N0hL-Bq_l-aLRBYvIOJy_V9J2zGYmm36UgRskegPjKlTHxPNDgPcXeXZVYX2eYNAkCtUuGGCUMdsFNR1N5kBIpexiQwmrcEXu7GZMhn5CF8aYhrxcHlJ6SoTFoZSNX_IQXve-4el45MHRGLE5LOuEjmxIdXOe5lgbLMkjU1ItWsJS70XYD1Na2JJW1sUwf25HP_u81HudS4zLPO6RAmdF_GxLfpIawpovjUzJUWggojv77nfzEsflDXBRP4FB4cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=tYBIfzRe9i_cyV6ZdmJCT0RbnO66XtJA22UJbG5_QFD9mWfnb-sPntj-XUlGHCYmx3eFAwFfJGdchC3tGNOTQ0N0hL-Bq_l-aLRBYvIOJy_V9J2zGYmm36UgRskegPjKlTHxPNDgPcXeXZVYX2eYNAkCtUuGGCUMdsFNR1N5kBIpexiQwmrcEXu7GZMhn5CF8aYhrxcHlJ6SoTFoZSNX_IQXve-4el45MHRGLE5LOuEjmxIdXOe5lgbLMkjU1ItWsJS70XYD1Na2JJW1sUwf25HP_u81HudS4zLPO6RAmdF_GxLfpIawpovjUzJUWggojv77nfzEsflDXBRP4FB4cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trePdwDhoM-T6tYseMKD15WeDM5wLAKmJ0phdNaY_AbqnFx3l1fPjTAIwwnouQ0P7PPwoTuexV70mrDT9B-J_cY-ptxfoVPQsglWzGIt5_QDsmj2fM96BPb4AQZR5jxtMAF2MRdvtnCFBKLByOkvuJi-m1-WIOjMQyODX3XQJWsqDTvZnUd2Y7CM6x8SdbiYMhS57qpG8U-xRgshUjEs0L2NxOW1YPNp99-vnKyTaqXEnHMQaZeLNqxcmxGS54Lyy2ZD8Zl4a3Gbj6tu7lgbOFGmx1PSA_TCiBcg-j4jGbSdSUPk6qPMcKqMq8MCNJYny8Qx4ft18j4NttifRNos_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=pQhNk62GoDzTHCqN4LoxEUpWp9aKJs02Q55z9yATz7J_sG-iUtD0_tM7skiRcwsVatz4yNCiSAC7DuDhCZU4aNAhoqW6jjyB8-0nOQSjHHVQuE7wpLktQS0ThjQcHC0w-x-mFhVdJPCYlt_ctnrqOqjIyEvIEHe2aMx5xQpgpDB1O0ztJMf4ksJdRqs56EYlyZa6M29tvG2v-SznOxFwFvKgGdW8mYyHmYUCLFV3Wo8J4yh2whIbWJDXqv1Ti5JiS1CAvdnGj8pWFjLMjksYUB6rUDgfALQXiOSXdZvmYkxhx-uzNXd-2p-ifi8EDpTiAMTw5Ry05hYfw3VKt666qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=pQhNk62GoDzTHCqN4LoxEUpWp9aKJs02Q55z9yATz7J_sG-iUtD0_tM7skiRcwsVatz4yNCiSAC7DuDhCZU4aNAhoqW6jjyB8-0nOQSjHHVQuE7wpLktQS0ThjQcHC0w-x-mFhVdJPCYlt_ctnrqOqjIyEvIEHe2aMx5xQpgpDB1O0ztJMf4ksJdRqs56EYlyZa6M29tvG2v-SznOxFwFvKgGdW8mYyHmYUCLFV3Wo8J4yh2whIbWJDXqv1Ti5JiS1CAvdnGj8pWFjLMjksYUB6rUDgfALQXiOSXdZvmYkxhx-uzNXd-2p-ifi8EDpTiAMTw5Ry05hYfw3VKt666qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMt9vvmUNF7QVyIQ5Z1RDwzlveY42bXNrxQcI2iSyssy9J4JoeNQGfXdLO0DkZDI88r1oKy-yNTCEM8yC18fuBPy9d48CMwBltKDYwCEIzKn3I1RZ5GaBokZMQngXsQio-XxRGa9luHp512DmSENpvtePGOWxtrrYkcHEvkvJq_JgWifkkqY4BIwPX2GlAuLSn3COm7HK2s7Lw90xf6TY140gtysODclGmgWMMUmtdXl60brZZNLPSYXYD7Td6o_vYJ2LNW_w2L8ryXC97RVLaCRkN03IiWXJIclwt-Ld1xn9jhR1EWB7oWCz6icDaLCOb-Dnzu0-pyWQ_dfTPfjfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usNtxu-BSeRHvJl2__WwXv6FNWEQrCpcIohdk52j4xo8ZFemvPgPmYPcA2jzW-c5tUarFEz7JxxMSE1kWM3Kk1Z2HvTZuRCddIQEd-G5u2qqlG16isLcIOF0XKtE7sH7YQBZA3DyMti6xkUvY5P0zcnB3lmki-RCigeKgXm-eZNvGtpAaJYPjkq02TgUxAPT4TCyc9F4XNEOHQ3eMbwjg3FlRm50LAGa6PCJFAI51tGqm6mmcBa5b0uKXwsb-yTphljzIjMdPYUEyBGWgZMXcbzeNSPLIrla3eqFIQrYbYi3mZ9I2Nxnjlhv9yCQ8E_GJGS2ySwdfLkI3ttUyy3b_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQZlT1_uLetK0VMzAxOt9FdeWpRpHo3ZIvqSaSMLdZQVr8LsS40WXhuopamdRnFq8nwrFu2Qzq1PFsj7wikSzA3LxdFMZEmmHnxu4DXptrl36snGJHSl0b0EUG6HUsRytO26hNcDpmy_3MePPVeNCRZJPSq4OxTMBwhA5lLXreNi2irFAUWF5K1j5UWjNXEKC8Ce9s2Irfjgb_BQTzZ2PVmhv-eDSGB8Juy4XDS7aQ5txYcUrzHpfmMtCQgHsjMmnr-K3MAg7FDl9d6sf6wfoayQJS5a2jfh-9pwcKOtifVLndEL4PDgF19vR9_pqRo-L9jlkBqsvCRevklxOIgflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=SK5Ckq_XulD8K9Cq8w_6JLhrjSuyEa1nCahUSp2Wj2DLSgYB3FelThJYfMJ6KpZjIBX1_AyBvtwB_NVa4vEJU9l8-ZWN0mGbHalObalgR_tdwOQkQFlcY9_ttVNOMVVoR6iONf43o3IMJuFiHmUbVnEiZ8bAKM--OWZFpyQb8VrGTOgjZzPa8mQIMivPd6JBIMqZvmWW-F98_P9jbjYrUrHWAJJidgGgNFAttFP_MpOiVnAoPmcy8NdhCnd5a7lpmSyBq1-u5edHxHCgIqNfh2Oj002xjFyISdCbonPefL-wdoo2-86tQn7zR5vX-wvEB6WyVQq7e3Ht1kv17LsmUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=SK5Ckq_XulD8K9Cq8w_6JLhrjSuyEa1nCahUSp2Wj2DLSgYB3FelThJYfMJ6KpZjIBX1_AyBvtwB_NVa4vEJU9l8-ZWN0mGbHalObalgR_tdwOQkQFlcY9_ttVNOMVVoR6iONf43o3IMJuFiHmUbVnEiZ8bAKM--OWZFpyQb8VrGTOgjZzPa8mQIMivPd6JBIMqZvmWW-F98_P9jbjYrUrHWAJJidgGgNFAttFP_MpOiVnAoPmcy8NdhCnd5a7lpmSyBq1-u5edHxHCgIqNfh2Oj002xjFyISdCbonPefL-wdoo2-86tQn7zR5vX-wvEB6WyVQq7e3Ht1kv17LsmUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jtb6EiJYrAlCmo173iwrsRUL8TiZoBqfnHElVojIs_a3htWY9Q-aZP6vSQqM6o-oPafY6Z8se71qr_WPBtUJH-GrUyCbt4wU7D27n6q-ZxPJFjjOte12XlwHLbGTa6se81sEKJ1bvxU37A6Jxel0EOIo7oi-Lb9lHvt2OCUhU4KFo21_c8jnDMQCmgQ64msMvs5eG6S6bRbxFXWlPxp18tV2mr9j4NcS0oHRyz8CDLBDS1I3mbHwDwNS2S52VjWRLUV0zNNr-vw1W9jxajpmkTv5Wn46BC7yt5apMKm0LrREOKXrdn_92hnOoP64Yij77xg3Ov2uemPWDNhEXTOPXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jtb6EiJYrAlCmo173iwrsRUL8TiZoBqfnHElVojIs_a3htWY9Q-aZP6vSQqM6o-oPafY6Z8se71qr_WPBtUJH-GrUyCbt4wU7D27n6q-ZxPJFjjOte12XlwHLbGTa6se81sEKJ1bvxU37A6Jxel0EOIo7oi-Lb9lHvt2OCUhU4KFo21_c8jnDMQCmgQ64msMvs5eG6S6bRbxFXWlPxp18tV2mr9j4NcS0oHRyz8CDLBDS1I3mbHwDwNS2S52VjWRLUV0zNNr-vw1W9jxajpmkTv5Wn46BC7yt5apMKm0LrREOKXrdn_92hnOoP64Yij77xg3Ov2uemPWDNhEXTOPXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=DBOPmuiS8pxlPMqd8ksdnVaV1iFfH62BKGvQPycGgMhjVKlgCBzMQDRTjexkF9-xTwjuwfatsYjAnYeyBZHorm0vBhq97MHauEj_8dFXWk6XJi2GY2sYb0dZ8BDV87nxihOr0EOynSUeU-TNXZ4s69Dnzz9AOaqZEty7CCTGdVxaBkduW5YieWsMJFi3ZV6K5kgxGdrepCmeN9chhfS7DoZHESEea8aiRiyHx8_EI-T0a9nVXQ_L5pViL7uleyqHs88Nf9UVFH83fanGOAqrBe29HU0DwkeDeJjF_fgHMn3bEkaAWTK97LIGKpJpcUmKoB6pIpZtua261zO3zu1XNklXgaCs_XhIFoyqGlgIFYXeXPAF5WKQSigwrb_gtTXqVmeOySYL3REUmSrsS2owAdssuqRQ0Anx53QdX8EfGlBKeXFP-X503GfEZgs4uLTL7-TRMPwWenntUuuc4QS6gaDp1DSBbjuZujfVlyrN7Ew5hLtlT7PVpGEQruvruRGoQmRYOUdTWXQDb9HJuLglbPBNp3Vey7f04oYOulH1fW9x1QCy7e1NtKW1bw0dDR4DQGI-IwZXw8ohWePmwFvljsFOr34Vj9dMt_db7zsOR3g2e1aDQcr7dFVWWwW08USLkBCs-wGmYVCNve5pY9JyUcTPVBAkHZ7bQdGF-iANVKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=DBOPmuiS8pxlPMqd8ksdnVaV1iFfH62BKGvQPycGgMhjVKlgCBzMQDRTjexkF9-xTwjuwfatsYjAnYeyBZHorm0vBhq97MHauEj_8dFXWk6XJi2GY2sYb0dZ8BDV87nxihOr0EOynSUeU-TNXZ4s69Dnzz9AOaqZEty7CCTGdVxaBkduW5YieWsMJFi3ZV6K5kgxGdrepCmeN9chhfS7DoZHESEea8aiRiyHx8_EI-T0a9nVXQ_L5pViL7uleyqHs88Nf9UVFH83fanGOAqrBe29HU0DwkeDeJjF_fgHMn3bEkaAWTK97LIGKpJpcUmKoB6pIpZtua261zO3zu1XNklXgaCs_XhIFoyqGlgIFYXeXPAF5WKQSigwrb_gtTXqVmeOySYL3REUmSrsS2owAdssuqRQ0Anx53QdX8EfGlBKeXFP-X503GfEZgs4uLTL7-TRMPwWenntUuuc4QS6gaDp1DSBbjuZujfVlyrN7Ew5hLtlT7PVpGEQruvruRGoQmRYOUdTWXQDb9HJuLglbPBNp3Vey7f04oYOulH1fW9x1QCy7e1NtKW1bw0dDR4DQGI-IwZXw8ohWePmwFvljsFOr34Vj9dMt_db7zsOR3g2e1aDQcr7dFVWWwW08USLkBCs-wGmYVCNve5pY9JyUcTPVBAkHZ7bQdGF-iANVKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xkh31paHpwzrQWLD6ORyqZvCF5TtHYGl3qF4oZFPKhXbTWkZxxAfmJdZrjyN5dCNn-Pxb6YIMct5h5qf6S-z365gOhb7prlv3B-NTD--I_qIJ50MObxyl3OJs7zEpe4eI4fnbQGWTS4YPIODc0o79QXZlE658ObmITsX2ItKlRXM1ZOuTct-J2WhV4frbQhyjwKdR1kxyLynhKFKz5fgWhbKbcFuksIWG5UIXHO0FV0Wn7Ba9YskYSBoTRAI6-kt6wpmVxQaK0_QDv9ZErmetSHxATn9sa8o0xGIo1bUlLYAvKkzIKODy57FynclqA8LtMJuNEOCEOq03SfAgkHy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-ZkTspksCL9mGs2N-h-xRf9mPEvHOQCGLr29tUAT4xdzU6kumxIopFX1a2Z8yvXoYJByvTiX7qMrzdkN21GHepNNToZMErW350RJA2Guvbj0VokeBCvm7a1PKIw4oliGOHcYHkPQppeU0RcCQcN7hQlxJdN7ltx7iOKZZ844eoYwg7ldOVYCzKzTfMikzzFHHNy6N9B86QqwzVGXrNgUkVy0452VJZd5kkYJ17L7LWevOX9dJeMtAjlrFwrL7XaFEr0dpVJulHTbosVz3411D-B1rrXBhFWZYG39rMpTqjlg-23OTpHSQu-qzJLgz4A0xZMcRnXKT5gHuR7IjZyUcaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-ZkTspksCL9mGs2N-h-xRf9mPEvHOQCGLr29tUAT4xdzU6kumxIopFX1a2Z8yvXoYJByvTiX7qMrzdkN21GHepNNToZMErW350RJA2Guvbj0VokeBCvm7a1PKIw4oliGOHcYHkPQppeU0RcCQcN7hQlxJdN7ltx7iOKZZ844eoYwg7ldOVYCzKzTfMikzzFHHNy6N9B86QqwzVGXrNgUkVy0452VJZd5kkYJ17L7LWevOX9dJeMtAjlrFwrL7XaFEr0dpVJulHTbosVz3411D-B1rrXBhFWZYG39rMpTqjlg-23OTpHSQu-qzJLgz4A0xZMcRnXKT5gHuR7IjZyUcaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGf8B3lf3bL4pxh8BhVMDDcRKZeUjyQ2QEx6IXApMwGnYoTxXgTEYuIV-H-6Gp6Odjhzl-jm507vva65KAIRXHiNrbRjfyS6gVx69rsuXx7uJe9c3_nGw9IMETDZwfuilmxtpy12BVrO8rCnyCGr-iCaaAF37hqbpmpwQRQ0y9bNsTRHgtky5D9kUllNg5MiJrcq3pkQPmrYP9AWIh_SiJ6E4S8vAqWKlwaNq4PSEKrLjNEC8qn3UFaHL0txkGsXSb72UX9mlVMg9pIzCs0bU-cHxuRnqTlJ-pYdWJbZi8iiNLHid9d_4YvVHPNIuDanzu6mTNvXMue9eoaTDwh7iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oB2cErM18xO5vSh4LlrxW44PhQJ9TqNaOdI1TpWliC-OAm09EVGRtuFNfzGdmjJd5_DWA8DbNB_42mefNlqHE00b2Lbiv0Ks01etuR1gTFIGLcu-XwRV-nPCibXlkmtoMOQe0Vavb6xfBg__XWBREhnKXXLMCDQ43ysBDDmOmDFhxNqLU3b0mF8uCdP753uD6qIu0GzH8J9ZI-r0AN0NasR6munpKNLyhRNMTC3vhE_LiW5Vk96kFrAYXRoAHrMKI0DhV2g2zqRhozAVaSqqx_Vfz5sgfKWNYVQh4u9RsHsoB0BIUU6yJE5P5LWnku4KmbPgvc1uCBcu7NSuvWnTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qacKi-P_Tlapqj-OUOrd8A-4JUAUVX73hTQfk2XjENCJQ21bdqmwkSJ5WE6MtzWjdWa-USzibEkeXBPgNjNdyerfS8Mtf5ztBvjlZnji8kONpvbuOWIWyNhAHj58VFp_ZUJTDoVSyAWOHYHGQN6hEbO2oHxQQphmUhmPEgHZuHj2LEjBMX5Fls-M6A9rJm1YZkahWo4R4ZtkX9RxLgd4_gWD1B14kbMhGkC_GhUjavvK2L9-Xw_tx4La1mUAsI1qkqcNP9G6TSQe3az4PXKPoqxWFVX-pjppIyjqnrOM-DRiZ05WTtQVSjRil7CtXh0WOZoAKMPPRcJb5V4pUFIfpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hka7DQLP4afKA2NgkSL3ORxTIdamldIDxPRPBuft9QDlm6BsmESePQ2wPP6vUbMLrhIe3tvRPyxeXR0AsCrpGYF1DQj1WlUgd8hCyOMe9VtcNAhJou3dWEk5BFxD9Z_vpZ1sqkxb7RzdpdPFI55ESBewY6u12SbacEFNHbK8EG6ZNIWX1kdRo5YW71PCbP97k8kYk9g9buvFwKohmXGXE-6V8Bk4JlaGELMkA3nQThBjfOvxSH6ituGQOn4Eor4AvR6x20H7IYiuaLPudXxp4fnMOuheh-VZcosPMZoU8G7mOzRomRMEfngLU5QlG6dyAyR6qcGqwvFXzeGzu8Y0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaDPkbnszrrK3Fa6HC5JxZ8kQba1rexqutGmc_aZbjwocDftsqdk5EMgOQW12yfZzi6cyPAWj3jHlf7aomeMjQPdb8SipA6S3Si2gaHVyDmxlq0iMbAX5ssUPhk1ZluN9w_pc07SNyygScqizkFDZmMcvW7Q_wsb9CaNxvBCRCuty-bD5maZ0uPfC2lUi7UkS6w1mwXf7xkGhFtw7oGjPU7rxzTKbforLBr78nL0dzH9HvK3Avay0RK_fxxNR1_rm7M-Ea3jtddvPAw-0YFrAIVNTtFufMN2UlnqLshyk-w-FfAQqN5wCs-L0aeloeL_FhzrISCEW6YxqJrywSTVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZmv9jIPP-Y5bI5iXZnLz67H7eg6vevVnDcUYnss46G4jygVlWd3S2WzsprOQfWR47UdzzfpMIRMeg59Z3bHpqJoB4K2pqZprcCxwXFeJItK2ZWRE2T3g4DI-CPyhhz0bYp_Ky3Rq-hB1iQk1vOleuoZb4QZ2o8MEkVjlxlii334XL5mCZgF_GWv8GYx9QfDFiQr-9yrqfKk1uipo3emBmj6IHLwZKnyImJAgtuubscr3sybKTRL9wb5INNait9GjqIb5Rrnt1Zc8GcJ06cpHmCcdNpOY1Rbqab0-4qnnRXFcB70AuggR3Ym2FU6jYnMRw69gbrThSUthLa2ST8vcQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=V-QKcB-Rgn94oSp5wpqV7H51Bpsu6-qdkztAhpVgg8zlt0qsgj8K8lhzZwm8iPqa3RjeF9oGPODT-Yd1zE8IbqgwKGEu00QosE-OXZ5QqipC8r1XiG9Rx_uuz6w5KmQ7nPYGeh75NP8OY0z6X3vgQRMBesys5CxdIxY0VYtJnfQH_lDU7T9bdS-qbSclMpC8NbBWl_gDXCv-WmdlkAiBWjdirD-Y3S71t9e-zW2DWxmfAKsETKg_u5dVyvzv6NRSI25UAUuixvnJ9BFQSUMlSgaawga8x8qYGXyyWFHeTEB_Mg4DgviWIfc1DQDUfOt-ZahD3Vqq3nc6020YlgxlsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=V-QKcB-Rgn94oSp5wpqV7H51Bpsu6-qdkztAhpVgg8zlt0qsgj8K8lhzZwm8iPqa3RjeF9oGPODT-Yd1zE8IbqgwKGEu00QosE-OXZ5QqipC8r1XiG9Rx_uuz6w5KmQ7nPYGeh75NP8OY0z6X3vgQRMBesys5CxdIxY0VYtJnfQH_lDU7T9bdS-qbSclMpC8NbBWl_gDXCv-WmdlkAiBWjdirD-Y3S71t9e-zW2DWxmfAKsETKg_u5dVyvzv6NRSI25UAUuixvnJ9BFQSUMlSgaawga8x8qYGXyyWFHeTEB_Mg4DgviWIfc1DQDUfOt-ZahD3Vqq3nc6020YlgxlsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBsZKNoim2N17srnVepLKVVGraCO1-ipg8MwvSXPh6Ct0Wy9THOU20zOwy-NTw_rVrQQe4xEoWwMJzuxcvqAMS7UVRUGOY8OuJU41M3bz_uA__FLvwvSi6BoqZZGoR-vAJBFgHiVTy40z3s8Qz5dMwfSA2dAuCRfIA-W9VX6yMstdVzitvsLoBoNg3rfYJVKX7Merio3ONXjza5rnO0WymviYrhCsZie2ipbe-mg1ka0yD75IiSEw4ZetBiBfiR9cSCQmLcenssyz7nDYIzodOOLnmvo-UsQXb4awg99BKkjFL_UohFz-LZ5iBpvfoVXJsnflzAb9lZRCT7PAXWGAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bm5HIQGbqk1GEnr5pgRW6qdpF8-Dn3Cbeyu3GAH5hm9B9IMfPPiNMp1dtNS9IjQJMpHJje0xCwUUnQrje_Aw-nAt-2BQSSDTLwaB93kkDTRc4yjDo1N3fA0aVy3r-hAXocH9ShDuWbQ-QOkOSeAxlI1ORH8hR0wyERTxwmFY1uSQjPcfTDtBGk_qMLWKgNPXwu-BNkr2WR87ibP7q-_Dosvp7g6vyYS_mcXuQp-hzO1xA3h_rnZNMrH-ytCqb8W1OWcRRi2NPqJrfANozTFLKJzP3hy3IDXCjLErEf1zQzkM67SvkybDM2Suep7azsOeDtpjRbGuNPm63qDb6zAafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnDE4Oqx5k0cBYVpShTe_Vi2FEwGYdhCDEXJM7TB_1iF6AlPCjIjXQDhLoFEXelicXPRoEWuauV_BZo5G5CxYDGynrs87MuVoLKcCyPafmdJGRE66NtATpGsatHkgsU-0UDXzwANJp95ECc169HC3yA_NEqaY57TdXTW1ee8gFpB_CzyGfHaZOP4rzlQZypww9yxPIMe1W2WBeRQ5jsKr-uVW45UbSHth3Z5rEYL9vOfWrMACzSXmK4BaXdqHqzeNUEU9-9FRfMpZ4LnAQmkZeV1qqJaPVPqdNxwm2X3iaJoZOqsFNVTqQRPGEBtunpr5krBtBefFcF7OXkGR9ah6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=eu_a4fJQlQXsjxmnlzENuAm4NBgpL2MaUP87iQUjkDeHJBXTHZU-utNieppTITDoXhbEDcVegnTaBon9595W7q7eI4MHcWKuR3w1Ga15fvq1HHpatomZ_qn-lJgDQZbmE1QynWGFZsN7PAD3ca1MKQP3MKESqeGqJU5lYl5Yfex6ThJmFyK5E8G5ddOq7QAv9e_yAP3nLdf1gtlx3zYEBX_cVN4GKdtwo1y2nPOxah2yq-Kmp3ZoYNgbZwTtuMxSH_fa8kDuX5BzsSaGzUI2BKWe1Fuw2TKZdoniU1nAld0WlTguivhbYulA0eIOpZ2jff2P6kK8pP3uxpFF991BDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=eu_a4fJQlQXsjxmnlzENuAm4NBgpL2MaUP87iQUjkDeHJBXTHZU-utNieppTITDoXhbEDcVegnTaBon9595W7q7eI4MHcWKuR3w1Ga15fvq1HHpatomZ_qn-lJgDQZbmE1QynWGFZsN7PAD3ca1MKQP3MKESqeGqJU5lYl5Yfex6ThJmFyK5E8G5ddOq7QAv9e_yAP3nLdf1gtlx3zYEBX_cVN4GKdtwo1y2nPOxah2yq-Kmp3ZoYNgbZwTtuMxSH_fa8kDuX5BzsSaGzUI2BKWe1Fuw2TKZdoniU1nAld0WlTguivhbYulA0eIOpZ2jff2P6kK8pP3uxpFF991BDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=Z3Ir_b1ytDDcz1BkGVdoEvNGOoKOUDW2Ngf0OsFUbt-ZR8b2RPwQlhuzJZbENdemEhteqR4cE1aTkxd4Oq2kfrgfJwv47CSqLu0hmqpzyKOwBkmUysJcaIk-1eoMBkB2DhnKhys1U0nZ3kBE8wYb6iF7AFU4Z749cbtb--rFGp-aukh1C1TOO9NJKXAnMkmE3IMX_pPuTeqkqmEyEU8roe0rEkVzYcMqPw0HJ4YQi3T58A_zLSUpbh05juKGbEqiQoAeh55aODFOKSQ7WIFxwJRi25Mz-rpQnuQn7lCk8959jxAiK3o3c5aQ6tGcDZRTjm2gIQ9q_TTkhaclNg09eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=Z3Ir_b1ytDDcz1BkGVdoEvNGOoKOUDW2Ngf0OsFUbt-ZR8b2RPwQlhuzJZbENdemEhteqR4cE1aTkxd4Oq2kfrgfJwv47CSqLu0hmqpzyKOwBkmUysJcaIk-1eoMBkB2DhnKhys1U0nZ3kBE8wYb6iF7AFU4Z749cbtb--rFGp-aukh1C1TOO9NJKXAnMkmE3IMX_pPuTeqkqmEyEU8roe0rEkVzYcMqPw0HJ4YQi3T58A_zLSUpbh05juKGbEqiQoAeh55aODFOKSQ7WIFxwJRi25Mz-rpQnuQn7lCk8959jxAiK3o3c5aQ6tGcDZRTjm2gIQ9q_TTkhaclNg09eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxGUHy1S-VC0mLoCXID5uvqi9VZ5At5QDfx5JzP_Es8jCvcXdNpEYbFGmi6KBJ8BeoB9wnMas6dYmC1WHDX_wL4E439OFbSNLwythz88ky0_-X63rmw7YVKnfTdUIG5rSl3usH3Mz4pVeeiFU2-bbFgTyAy50qzsJRPA95bE7q4BxvuoGeygar6BiR3ty1D3_fLPaSJLZK6gjtAK71tcPyFmeSpY95AB97ZTOnEagyUxiCVMh4Ps5A6M1XVIXUI5APSXUPLzfDR_OR1bqqPWb7tpDgp2yUT1YTstLqm_4HaeKzypdjtVEih5n9i1UaDhWZ0wSTucgJHCiG9ufr0KAtZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxGUHy1S-VC0mLoCXID5uvqi9VZ5At5QDfx5JzP_Es8jCvcXdNpEYbFGmi6KBJ8BeoB9wnMas6dYmC1WHDX_wL4E439OFbSNLwythz88ky0_-X63rmw7YVKnfTdUIG5rSl3usH3Mz4pVeeiFU2-bbFgTyAy50qzsJRPA95bE7q4BxvuoGeygar6BiR3ty1D3_fLPaSJLZK6gjtAK71tcPyFmeSpY95AB97ZTOnEagyUxiCVMh4Ps5A6M1XVIXUI5APSXUPLzfDR_OR1bqqPWb7tpDgp2yUT1YTstLqm_4HaeKzypdjtVEih5n9i1UaDhWZ0wSTucgJHCiG9ufr0KAtZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3bhjRDxF5GBVD_urrpbRnVKuFzvAqdInvKKgaNtqQrabkEP42O6xGRJGuvOuMQIBh8WvE_FKO7bElWKvJnT0zfQg57hxTA7_SFw0iDyaXjxcfBP2GBDn2FDGcUvBw61ZyN11lvBPM0jfHu1kEI8Zaq7dMmLTZPX6Kx01tElRYf10BwBYW-bobbOmTmG1-KC0wmMRY1EXzxhScxKZwX64uB2zJ3WEthYMHds0cA0XUxMtlPjiJYdBQKDPsfFvD7kU7LTOBWDX_RzpaaefmhyTzJJG0YQ6q5J4o9CVs7sj9vcJx_ysWmWio7GMeCKtbySk26Yzktrf0pZr-knsb0fvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vElpLv_T3QMF9XCt27Tn-NVD3y_mIG9t_HcVIEaFbXKtEJfa3OjtyfbfF2oRfldR-JrchTuKok8e4hm_J6_8EBoqfW_BAIObYW-RZ_bidvIho1Cy45hjh0s1oWOQfLr8_vt1kN9B9iRR8t-ICrg9l_u850zP1ZHvC9CZPMd6znd5uAX_ZCirI1Q7LtUnRkk_rjvowXoSwH0uE9-iU7b7RVOnMxDmKdssRTB0QRJEcSGcRraN5rmHKvb68YbgpLkXB6IlkBpzbr6wBCOK9tJYYlgTKi_zXejMWnKCx8dELjGjPOlk4M65ex3hJiCWEuW5Qb6YaLn3xMn4uqd1DNDYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=iPyPR8eoEkGYGjBVfapJ1MT_pnrov3W5bmtZjDJyVjmSWFp1Z9FoaCNGkpX9BE1QdVHX6wcF76UaDu2hUGaw2AKDsXqQ5xHUcZtMy93gUvrLwuVn8u0U_GR0jNSqSu75P3Sbqn5Qy151wzAEes6RBurtqtpWQzvQZaFWKlAElDCk1_k5C1EIauYiyuN06A1PdC47a205r5c2uZ7E0_zS83aS0kMG1lt861GPGtDpYtLVkh_lLswfMlOxwI4azW-mBQlWhKrrPgzo4VtWTZuakRL4zcbOeXB_8P306anXfc75ubIuWEA1A4IeuVloRFhaaAOygxht9baKFaFIgWkgIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=iPyPR8eoEkGYGjBVfapJ1MT_pnrov3W5bmtZjDJyVjmSWFp1Z9FoaCNGkpX9BE1QdVHX6wcF76UaDu2hUGaw2AKDsXqQ5xHUcZtMy93gUvrLwuVn8u0U_GR0jNSqSu75P3Sbqn5Qy151wzAEes6RBurtqtpWQzvQZaFWKlAElDCk1_k5C1EIauYiyuN06A1PdC47a205r5c2uZ7E0_zS83aS0kMG1lt861GPGtDpYtLVkh_lLswfMlOxwI4azW-mBQlWhKrrPgzo4VtWTZuakRL4zcbOeXB_8P306anXfc75ubIuWEA1A4IeuVloRFhaaAOygxht9baKFaFIgWkgIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPrREBNeORDOGN-Y-2TPXBS6bYon5Gv7P62dYFy6r8-bSDaT3WmFes0PXHGdIDY_-jnjHixflmzeBIebbe5AuaiOfhIB9xpNNOugZUFbiA7qMnAYOIT11AcDwnDbE5h9dih1m8GIbA7bAfMGgA7sDNJ5CnGwamb3jMiGgdUSENmyK8YC55rj_Lebd1XenYKLJ5OBzrxXMXfAgvVApXQbUNai12o-yNZXaOF_zRDqDyCdncw7OvfkOC8ouGr8WCcRKg1jwrTeCzZ1v-0Z0qfLRi2lX3v3gBFC8etHIJIc_J7v0EF6xqmzBjML9MYPKXNUt9c7kOxiACcA7We4cx34bQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=rd41czIf4UvBjTBOJgBKiP5_Ow6wQWwH0R5L21K0Aj1R0toFer2--sH0CGm52UmCFpBwRTWkRFHh_aenpBJmbkPnkMfCf-TK8ZQ9oA79kjAdSbWLAYSYf8F2xUOpJgRxDfifaTLznfRdQUdpbUU2HPj3-EgX1LWmUhM49PLLA5c8m5i7wlfsQlgHhzT1-IdtyEGBn7H8UIFg5na-ZYKMxDYlUgBMOpMf91Lc4SmsbWIagHc1-wk6dyjkaosLBykRVfjvbACB12BFb8X2NqUrYH3KYPKgruGYjGXVsGdwiDA-XdQcU-UxdYZg3vtoRnfSdR5MojWEz7Tuv0KmKWe0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=rd41czIf4UvBjTBOJgBKiP5_Ow6wQWwH0R5L21K0Aj1R0toFer2--sH0CGm52UmCFpBwRTWkRFHh_aenpBJmbkPnkMfCf-TK8ZQ9oA79kjAdSbWLAYSYf8F2xUOpJgRxDfifaTLznfRdQUdpbUU2HPj3-EgX1LWmUhM49PLLA5c8m5i7wlfsQlgHhzT1-IdtyEGBn7H8UIFg5na-ZYKMxDYlUgBMOpMf91Lc4SmsbWIagHc1-wk6dyjkaosLBykRVfjvbACB12BFb8X2NqUrYH3KYPKgruGYjGXVsGdwiDA-XdQcU-UxdYZg3vtoRnfSdR5MojWEz7Tuv0KmKWe0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=QTdaVb8y0yMAFEhTtNiav_H8W71sizAPYutX87UAdc794T2Wxqo5NX6pC1Sazas7xmhPRSUXApjwhx980MZSYOYspKU0_tXHtH2EFEV6jvbFJJqEEJx7e-XKkD6bFTjdH0jdh9QuPLo5iU0phHn1xZ5qHLjd5pbyXYHiGRZaTLundPQ0fIODxpvGxM6RR9M_fABMCsZ5X_f3PXWhnRpOF-sjtaSkzsUNfTlhXG5_VrpXne1MBToCfBsanXAPGunehhHGBcDpZsQMlaI15QrDr9kJvw96hcpGqbOPhvy8wozVKj1t0qB-S0bcDAbf7nu5gCSAKuOfdmye4_oRr38YRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=QTdaVb8y0yMAFEhTtNiav_H8W71sizAPYutX87UAdc794T2Wxqo5NX6pC1Sazas7xmhPRSUXApjwhx980MZSYOYspKU0_tXHtH2EFEV6jvbFJJqEEJx7e-XKkD6bFTjdH0jdh9QuPLo5iU0phHn1xZ5qHLjd5pbyXYHiGRZaTLundPQ0fIODxpvGxM6RR9M_fABMCsZ5X_f3PXWhnRpOF-sjtaSkzsUNfTlhXG5_VrpXne1MBToCfBsanXAPGunehhHGBcDpZsQMlaI15QrDr9kJvw96hcpGqbOPhvy8wozVKj1t0qB-S0bcDAbf7nu5gCSAKuOfdmye4_oRr38YRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=brf8DbmF_D8cCzjb_ueEVR8DSjWMPp7B4TgRQWgasEnSLmDDtsPVTMRV_fAdfbNI06KApruAkWcRN6rnToFU7dZt2K4lYarOZH5vYtAzaCvBMm56XMjAggRtLbzEvx_mznVBNpkhPS69FaTqSn8pABc4vwPsUpm-sIPuGQFgUPedaUfZ5U_JsW7FOSPdnkl8lnaWwAAnk8_0a2jj5Y8eFtLNxAd5OON1NMennX04DDXMfmToZAN1qEWqdF4INMK7_d6EnAPzqy3yBwOog3tOvWrnR6Qdkw_qPPuuE45hwZF0OY7OcB2zflhKbWuY_MtA345RUC7QiYSbn8DMHeBx0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=brf8DbmF_D8cCzjb_ueEVR8DSjWMPp7B4TgRQWgasEnSLmDDtsPVTMRV_fAdfbNI06KApruAkWcRN6rnToFU7dZt2K4lYarOZH5vYtAzaCvBMm56XMjAggRtLbzEvx_mznVBNpkhPS69FaTqSn8pABc4vwPsUpm-sIPuGQFgUPedaUfZ5U_JsW7FOSPdnkl8lnaWwAAnk8_0a2jj5Y8eFtLNxAd5OON1NMennX04DDXMfmToZAN1qEWqdF4INMK7_d6EnAPzqy3yBwOog3tOvWrnR6Qdkw_qPPuuE45hwZF0OY7OcB2zflhKbWuY_MtA345RUC7QiYSbn8DMHeBx0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=C4upDkMpYLo4j11xrClUZGfkhV6s7kGhk8mz-J7J0q1k9B8Jp1sjoZH5DtjIknuVqLrkEukAfIsXbLTjePucgVNsTi5TJWtul1HY2DurWDYwcf9C_SW8iu45rSaQbaPOmv2T9x1TaF3u59whkvfbuyWYSNIXxNVPzC5pFPlfvbJBYpTtVi5zAT7xGN5XW5dTDz810rcNIqMJKEJq_ZpROPTe2xU2uVD2BbIzWnEYNWWLssh_Hjo_4-5N_1QzvDme-GSJCy7dMLCJ9EeS1jeOdsrXG5nLSTDZSo0DAoYzdWGeI6wClQfzcIB68pg0C-oXERzKVDgh0GpQiVARi7ey1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=C4upDkMpYLo4j11xrClUZGfkhV6s7kGhk8mz-J7J0q1k9B8Jp1sjoZH5DtjIknuVqLrkEukAfIsXbLTjePucgVNsTi5TJWtul1HY2DurWDYwcf9C_SW8iu45rSaQbaPOmv2T9x1TaF3u59whkvfbuyWYSNIXxNVPzC5pFPlfvbJBYpTtVi5zAT7xGN5XW5dTDz810rcNIqMJKEJq_ZpROPTe2xU2uVD2BbIzWnEYNWWLssh_Hjo_4-5N_1QzvDme-GSJCy7dMLCJ9EeS1jeOdsrXG5nLSTDZSo0DAoYzdWGeI6wClQfzcIB68pg0C-oXERzKVDgh0GpQiVARi7ey1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdmHSjgtvrZXn4pFWHU-RoyQ7kQj9N11QioV4XJ8lw480C6t5Fl2N8Y7DAyI0B8i9ccteqCN-XS1Pg-OnXCmOTSWyY5TojYlt4WUGpaywIJn4lwceHc_U5Kq1kQa19L8XXZ3YrvqBhYWHwbQ3dzVVzGDv5I6z6YVGJOfk1QStHuymmci5zdJVhmrR_PYrPPeEBAK_uqAFEtGJaBVM6VKc_dgyNAb8ZNobf2mOb6HrtBI0wGuphA3QAKjcqVAJ5LBRlo-dVhkzZqlyrMpUEsFoUcchZgVm17jcmLrFYs5po8PqWCBV4PWocmC9XKIb8_Gnivesxrt9-zWAlJzL2uP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVLRUnpDfYe09HG-dvU0YJb-uFg7eBVFje5BZ4HI_MYh8NrQDg8hDEscG9trNXaW1YB5DpWUvyJTg4LRpdZmGYcevTMR5YcIfpDjxcpOcVh7DMyDV4U9EJJsYOCUyoJ1vQWy8q6X5Jc9xvkqIP51L1arZmplMJF_HpgN9bs_oHCZFuSG3pQxYquw5IO6U2LedviFKc9VvBp0iH6J4K4PIm0TS60l-Wz5Gpcpu3alv6Z8F8WMDcqIhLtKtTqHjo-BBNl9FlaQ8awHhsrHdN8OEUdk6tgmm__aRkGW23Kd54LlH5a92ZsWGfkYNCjVM0-1byuK8BrrjRsiR4onNCRP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLJ3gnLf_YMU6uVSacsM4pExmLbl5gHKbYNgNnqJMpMNsnACaImL-7TW4EC_b304l6Cy1YiPPmXCjp2uncQH9fOj9P79DtlV5le12pPiwUzBpUb6L9ZCLD78gb7hSXAqkrvxaz1lxEXhb7g2rP14UJCfZHROFooNzjETFVtthjUW1sGEigCoQMlIhIH6Dpmm3nfw2QP8RP1kf3PjQT5z2Hh6cXnHZVKjQ2CGJoct1bTny2BCj00E51EyMFxJ0_F_Yb-I8ulktE0fjMd9bW5r3MP0oe8raEgmJOAV75Qn0XKoPx9oNmX88reaxEm7WF6vT-A-4P2RvhhDrewqObEqjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctq5dsuK_LrA5-AQoAQqLGHL4G8TPQq68lI2n7doqcgeXE74yPxJXMx2EaaGmW96bjq4C02-ny-TWaAP9NJeokKuA0EswkczanlGvba9xH1LlU5dHc4imuHF_JwKV8kvI-LPvkMKYrmPofoEt0xozCGEh40_8Z3vceo59yYBeUHK_UVgRVeE3hV3NwmcsHFtc4qt5iJDy8dgekadhcYZsB8dWIVGslqPQi6Z1Mmz2cQY6cNzwBuQoXeR_0gNBRKo2CbPtayK5xxPAwAW9cj6IPlLsHKXlqn6My4XPboc_6vlu1rTSPsLg0DKaQ6W6MZn_bpjlkAMwkDHs4AfrOYWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pa5c7d_8x-5oRVk7h5koNYIchi2sMszOEzrRWXyYNx83yMWsCL8ow9DJ2UB3pDqVIZMUKFCupVRTLNf0ov22aPnbkE6vk7v3IlfAcAoq1HEITVYmPI3HKLsZDMAoqvrq4yUg9bMSD4bITaIa0lDSrWVP1VwyM6NKgBJFY2DWzOesbaenLUD4WqlV4vHt2Lz0P-40J0QMYWkz8yrD9n3mq9i29OkTReRs2tDiA0FFyczGt8eX4ewQJekTUSzkNtGvm9kTpjN45pclu8xLesUF78TP5VnjrfrWokCblhVxMlsGHSjzPZBX5c2JbiKfoyYGC0-wLbfYJvYlyfHLxYPtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMxYtNMR2EU8GisSbVuytkfvgUv9uOx3Mki8y_qSV80APQufF5SGA8eJu8J0_Q8x-45WO5PjWUwJdA6Bb6o-Nu-dn7NUdBTcMNVkl_WRHLFJxWr-giwCewn6QEPkRCuuO9EE7fRSdvHpulwmwQ9D-D2x43hYQgaoZF9f_3CfFf40gyiA3dcBjR3O2r8Kxa7S28I-zWAfs5Q1qxfHorAgkuJm1KXjoBx5UZ-ex6XJGbOiiT-INT3dWeYlcBKcmadat7buWbJysHckpQHKg9dFWj6ns500DNhdsf1qT7qv8Z0qqS7HWN6SovL_wRk2JGzif04FpfSPj1Y7qJxJeKwdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sohGh7L0hDDdUeSYP_guGmryQrt8Ct3OcyXThfO8Yq1hgtiYB7vjols1TZDGal-lQsBjIWDcP7A4UtisLLemBVYw-xMVXgV0u9I9Cf1_ET0OHHAj5Y9FACSJc5CVKRL6i1-L8-kuAvWsruqTMdFkTbuUdCZ1uWW9w9r_QaK9tX-xB4XfzihXX_UcdmL-6lr_e3VEDiODkDWjsGnLk9QanQdS6_GtRh5eFIUs94kHhJqXjuFnkGpcl9ngzWINoUgBBJBQgIhW5sjiTt0pl3eqhXNLIebSRuLNG6g0DaQ2FG_jTAPdNe2AFtjNz5IKVnavXsMC3N9LmVNAsI9kVhT72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=QXKevFYeRZgodwZh0CzIBlxG-y_CZopTb0sh69qka9FLo6YyJrPPd3zg0hrMvABimHcc9gffesIiOobisJpCCAneYl5AWxGjTMAJt0-EbsMIPz69z-uCFtqhGefgkAszwKj8oGVbyaRK7_90GuD-Tx-kT_kcKOZhYMke2BmuIJbht7bRpH66MCslKG9AjhxOIS0Ppoa8SBP8zDPQhB6SCPruMVF5dlbHCxHzqhIlCNPKFOzkz6Is78FS46JDSTkQFzR3t6BzffjoT9KaxqVexcDtCzy9G-c5o5y-oeyWIfwAAXW58JoPts2n2IbVL0WBo4mkc_BnUHQkIaDxQ33aYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=QXKevFYeRZgodwZh0CzIBlxG-y_CZopTb0sh69qka9FLo6YyJrPPd3zg0hrMvABimHcc9gffesIiOobisJpCCAneYl5AWxGjTMAJt0-EbsMIPz69z-uCFtqhGefgkAszwKj8oGVbyaRK7_90GuD-Tx-kT_kcKOZhYMke2BmuIJbht7bRpH66MCslKG9AjhxOIS0Ppoa8SBP8zDPQhB6SCPruMVF5dlbHCxHzqhIlCNPKFOzkz6Is78FS46JDSTkQFzR3t6BzffjoT9KaxqVexcDtCzy9G-c5o5y-oeyWIfwAAXW58JoPts2n2IbVL0WBo4mkc_BnUHQkIaDxQ33aYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkvdOpkDNlNQfGCfvHg4WjEypAj7jzY_cQ3GFjzrz_kRlve2mTFudCa5Et5Y_9HxXZj_W1YYh4UhME8cGtPpPIPL3FqZnfMsx1OROYeB2N9bZAL5fy6QJpRHvE5f_AQaeceEEi_Dilef5z8SsKsNyooalsbhKrJ_f4E8WG7Vf9UWHVm6jIIKMnXywAGBKQ3P-vzjVH7uuptTNVc7nPxWcNx94YImSHjdkkX2XW9e723m1VAtT15Xcfr6t9Kein7iC7LXpdEvUkxOa7dLq2sDPoh5gO93EHsNHL-p30qXFJDRTJr9VM_fCbRH90Z5km2Dd_5R7VprAvXvTMHR2WL1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukSz5mJEBWVKvTz6J-9tqG_ysrC8Y5KmDn3jPXLBHtQvXAg1oqy-5ZTO0yJtXgtxjou78hlA_rMoqqcvVgjbfkZieUGMoEoLGAsg8aFmxP0dKYSiM12hTnIldI7kSeU4LAndNcxG2w0Vu0BAzE0fjbR7uHm-oEskFCR_a6n2rEd-hG5Y49Jv_z-ekcoR1MYZi2WLeKCSVJqBcQsgTrWazU-h9-vGI1EltuwVnr9GIg6YgfKhixmFYZDu1Ey5eijIhVvYIGkf9083vn8b5U5AqcOBKtNQx2iZFNfWudIQdstz21Itiz1epxSFP6UQXwwFe1TcCRrNQ5SijeWRVGDWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSCRKWLEL1-co5W99OI6RHaCQhQP5e1pq39jBB8Veh9E7fPZ-DLEo86KY4AEne7wxvlHXkcdoq9g0DQuNQj5KuZgG4GUW1wHd__kKJv_oyYKgyARtESJgNr8dqn4wK7QtM0RLFxIGqCuMc0t-FHbdSfi8ZgsPma7MTPSMYMlygFUKcSalt8rji22dtbk-eXHlqDndGowAoAJpi_bCn1og9OR9jZvhFhz1rA3EP7fz_LpAu5umVGnZ4aarB1AQ_ufgtLVTjFxZHakTdaEOVviW1CAc5vvANaht9rrxUh0hJoDEEyK6OMCU_3BaZLIHhI9YaNJ6CqwIq5cvJRsbvwJ_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkFlAG5EUoGilwn6i1uTwChYqcF0QghFa1dzdRYcCllEMdBROMio3ikwVrEqr2i6oOrqA_NfaWe6TAbVKX3FdNTAXW8lDx-w__f4_i4iOGt4TivgU6C5-5gsW3gxxfYxSnWEbpIwbqbUs9_x1T2NJ892umFofUn9xL3DAKM4EioOQbYG2hjVs9rO4tg_YFzlzcV74d-HfBds51gEzyoRsyx8u_TQBUJNh74O1r1YKOKCbj_Ta48qf_i1aNg-Es1o6AKs-iRsL4jGuwiMJRLWIQTnhRvJC_YOhBCxHXsmPjpAQVhrx8LxzMotnE5HYZ-HIOfxSYLya4PbWWOKcpzgzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFBXWRAVK5rU-0iMuQmO2M-E_ryLDbn5WyZUwfKQZ29qdEmYsJFnxV0wh0URXxQt6BZw8ykwpVxd1oTM60YZYT4KGlf1eqlGmCAsPoSoXAaJMf-KvAPNnnrWHdn-g84vP7ulACgdX9B6t-KGYjNk-jLUm-1d5A-wfufzH-eIUApQ_d6th-d-2J8AAdMJerDQ6d3XFtQWcNWdxO48EVzzVpAM3RXgXmo7c4Nm23qGpIzuXZQdl8GhFrYhGKVBajigdiwKSlQU1caAFa_Bb92VpGv9vX0qCl_inKjTWEnw2GGHvAzejlengH0ciz84EPF1l9_ReqNeS3tyqtY34p4aIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npiagxglP6BfFMG3MkTnlGmJmGa5fjMOKCLn3pyviR8e9RrKLNQFfYUQqw01N24qc7XtHzHiuH5DcsH7rWVUatYJTvsRemvYK0Uq1AsqVDPuKDyRNz4YV2iDVylGR_EEyagD8fBV5FU5U0g6lXSiL7KApIG3XMQCDaQVv-vtspQUOBzZfNkryG3h3vebsBMO6tegEB1pDpZqQg3tjO9i-jLP44G5g3k5vz10VGMA4kEYloFAeHCm4mOSWZSt-PlIjK_L6jlf-Y6F2F-jv-dVLCXIfDKchBkOwQZwG32MG_ucB9QMN8upi02a80e3-oSK9p0P3Y_OGHBl4Jr_1u9HEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwQNzh9RFqY7JQQu58QVIcMXnLazUuTjBMC1NVX5FatYisWbv_x0OI6mslsSibHgLontHADWn-UIt0JOzZZC5SEUPr0NfKrGUSAdK-M_pwooEFe2_HubAAnAZxATuupeyvIg4TZIby7hr0QWQU8977sCssprWduCLweiQK5GE8GlXctZJZQi0uNRbDN4MLPcO3rS1ZZPLFGqEUHiEUf0TDl6EYShFgsLdf_354MmzaelMwhbI8GtjZBwKVVS0-s6JZ2E4vSBBHxs_3Jlnow04H_qXcmn3Eb9AzkywfsArUMqLGQcNfvdikOi5Vbk9Tbj99l-GPDZpQ41W3ODFA26pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrwwfqEVhr7QKsSHiuc-j6Wzo7gtmhBhdlsPEc62hGknvjkWnfY6s0y48C-SukcQRaN8ioQP0SzDtd_1oY-2WPa5UB8CBDWI8qq3apDr-LDfZj8gaYg6zZWjtizOgOdoz9kqmbmNZJiEUmcAj83AIt2lEq1stavb8Y5GPtVvMuLfXYmK5bJdoiOSt-6eh4KLQKFjZwT7eGxzbffMDHXU_0tism-90N9kLr2HtVWzsaOad7K-mOpzpNFgzZsjwTVLdByvPMVHautdR9LbNzXVe3zRHkwwnunhNFF57skgJezDw2QXSQ9KqyLqPlBh-p5ylr2FwLXnvDUT8CZyZTUXgQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=hhAs68PbMxSDpwZsMVqbo_FYX_qx1_dF_LT7iO3I7NLpRD9Ia1jJcPq6tVXmNaFjJZVLHsmBL24qMaOmBIqmuyP2BQh6Iyq8fkhpzO2wesm9kcYP_D4c12Z5o0aM8vxEvUnsYMs-RMCta7e_Sx3yzolvNr1b55JukWXceHjy6eui6TkmIaChd7PyJfwikmVcJakmJgyKMRwYDfrNHwHxRJCKQVOwTtfsYpDR3tWgUNnB-qbHO6ra9k5FjMkS-nVIWvZOhvhoqjosSVheU9SFcS07XByC6nIknIuI1ec0QiXu7baaY2FfJaiiSaIfpN_LHHlxA7snmb2yuEdk7OYnNlA55746ebj8qEpobTKAHEeOGAhD-EjO1QtV728xtdCFzO3A9fWB9RMZ6xnnpgYRDYR9nM1n82oYa4yzZ-iuAYgKt60Gjd9NPwHqac8qC1BM-a3D7p-uya92PFJBb5MtrC7lipVkopV4MZClu7nIFCJbaLZkNZXcMXq9FnWOxtGwTP5WtE57-uV1uc875A38EwjZuC1_FCZEmjNU0dy2-fgcjgSeAjl8MydhidPzLmyiZ8FbFAF1CoURNo21Rcoq_CT_pMt8lwTRuNPOyW1dSsOtxVsSCE_y7DxlHUo06VkqeFg0rB-i3RyC0mcGadHfUrXty7jjpr53U2Lw3Uy1qW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=hhAs68PbMxSDpwZsMVqbo_FYX_qx1_dF_LT7iO3I7NLpRD9Ia1jJcPq6tVXmNaFjJZVLHsmBL24qMaOmBIqmuyP2BQh6Iyq8fkhpzO2wesm9kcYP_D4c12Z5o0aM8vxEvUnsYMs-RMCta7e_Sx3yzolvNr1b55JukWXceHjy6eui6TkmIaChd7PyJfwikmVcJakmJgyKMRwYDfrNHwHxRJCKQVOwTtfsYpDR3tWgUNnB-qbHO6ra9k5FjMkS-nVIWvZOhvhoqjosSVheU9SFcS07XByC6nIknIuI1ec0QiXu7baaY2FfJaiiSaIfpN_LHHlxA7snmb2yuEdk7OYnNlA55746ebj8qEpobTKAHEeOGAhD-EjO1QtV728xtdCFzO3A9fWB9RMZ6xnnpgYRDYR9nM1n82oYa4yzZ-iuAYgKt60Gjd9NPwHqac8qC1BM-a3D7p-uya92PFJBb5MtrC7lipVkopV4MZClu7nIFCJbaLZkNZXcMXq9FnWOxtGwTP5WtE57-uV1uc875A38EwjZuC1_FCZEmjNU0dy2-fgcjgSeAjl8MydhidPzLmyiZ8FbFAF1CoURNo21Rcoq_CT_pMt8lwTRuNPOyW1dSsOtxVsSCE_y7DxlHUo06VkqeFg0rB-i3RyC0mcGadHfUrXty7jjpr53U2Lw3Uy1qW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=gIVkbomJe1YVK0JdxM1LC2Ejb0LeHBgqQxkPBRCNuhoyIgG3G15WJefWSgc35hNQGiUjiLWTqbz9ByQLYFdic-B8mWk-nBiiRw87DIKnAvl4g_DYcyiT_OvAihQGQqYwu_YfB0UPGtwL0uZO6rQ1LA0jA-pZ640nwgmhj-HGep06H8LGii7vb6dqgYk-ZQSckZOe1pnGxwoirzzPEoCVe8NuK-0czF5de3wFXdSu7aaYlxwwiCYz2OMc1x0v5HSwOTVfHFp2hg2tH0nYRn4oUWIhTKXm8gvb3D3m4YsqKtYTw_w-OAvQLZDpEPnULLE8CLEbI9CxJSSmJ0YDz_5SpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=gIVkbomJe1YVK0JdxM1LC2Ejb0LeHBgqQxkPBRCNuhoyIgG3G15WJefWSgc35hNQGiUjiLWTqbz9ByQLYFdic-B8mWk-nBiiRw87DIKnAvl4g_DYcyiT_OvAihQGQqYwu_YfB0UPGtwL0uZO6rQ1LA0jA-pZ640nwgmhj-HGep06H8LGii7vb6dqgYk-ZQSckZOe1pnGxwoirzzPEoCVe8NuK-0czF5de3wFXdSu7aaYlxwwiCYz2OMc1x0v5HSwOTVfHFp2hg2tH0nYRn4oUWIhTKXm8gvb3D3m4YsqKtYTw_w-OAvQLZDpEPnULLE8CLEbI9CxJSSmJ0YDz_5SpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMs2S6GI7xjPqKtdDNUfzAxWvEJsi9l4KeOMzjN8gudme5RnCE_3sBwsRVzFLJQ_LzBcgiI6kQuEYtLpw6cZtVk26D6fEXrhTLY6VklEiarUfL_Tkn-YbG4QtEGKgdg5mxdCKKDz7Jf2_0e4NRP--KF2DzM__3LHo1sZ6hJaFFKQP57pi_E3c81LxgJhmjGUDloZxNjTgqNzn_16MD49tsVa6DT2Cz5Dq0y13O23pi_5ezwrJaXLvULI9dY5utAMIGQWYEXOGjn22QcDZV7NUZtra6hbi39WDIVoiglQIDoTuYWCVpZGHAM-SickoHjWBjGJI8ePpY2aLEpvwGrvGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owyml4feFLbFuBAvCEoAmAR4kOl1x0g1V7g8QUVF5oHD39DCZv3Z-c4ymchUktAp3YBwWb3zgSkduJ6FSe0WHt9tcgFsth-qJWsRp0Z1zLqpWL64UHjNZ9do4_aJjszF7N60-xARo1tdwutT5D_5epM0vM8rFoItUCkQ1FTFOZrwL1p3vK18UtzCh-6jDF1eha1MntycQg4CQxPBm_V8L5swU9i2yE6hDhRW-c-rx0SCE6yGl_wfcgqw7gmf61k1uDde-SzsBAfOqxODCjb0EIRq_qvg-Cg2Gj-uvZQWkffsDjDsBUG4TctU-EIoQxx94sLJYlCypkozi1kxfmH2Kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbJW6zBmqFzfEjnE_mJGVbKcsQpE11w_VGCG_sQA6rp1rPzrjtXq6VsNeJD3MDG19rrW4nUM7KA2dzI2coVzsELElDBWT-JkkQj0fZz42OoVow6XRkQWxTNQEvQSF6Yb8JjZ-YcoqNaTjeQeAN_0z1bBc3JK2-ayJ832fEVnEkkn184BoDC7GUeoBLy5hO2oWgLRUe68lueNnwnDC8gFVIMtp76RTYXJJcRQdDMfXhh4z5HaiAwiAl18T9ovKttNDTis8jXIhsTU9N-4JD57Tsb1Zk66uPomlf-7MIAMRVAEx4zuauTd6gDVjj0huQoOj5NRBgCOcA0eX1eS10_tIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0CJH6bvXYEBQFi05s9A5rSfsOjcUDDX6yvaSU09Pop9Q4DpjOxxG-dBMXSHCr8q_7dzgmBNP8VoyCcyfArqroaikY8DhuQVHO8bq67N4LD87B61Zu1Kyvb7in82WtPSZF3EhIHaJzzewWzkCP_xjQNK__h2gI3F120rhuz6uUTHA21hrREFzZCRqupwG5XqXwge5HyQPg2ZVkRZe3UEKslu8mPZ9vRzt6zvN7SOL7LtsOY4tjpCjdYDhKWBele7gF88KjWNUVMEUZrt8NZxJxCP54yh9orvHYsyZe5IEM630-9-9F2bnk02TgG_I5IahB18LOnNjh_5mr_aBdE-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3nxdyHNRPnDoskgIYqjZVnbTZACgA3a6QrPDjurMc3FPwG1ix2K7sw_VI_qCvVCet-XjpNkEPUmthhbLysWAG6AT15RbwaHpCsWzXmVSo3yLZB7FWLHPEx_Eghwi-c-2Azv8xI9DS-ukwzqAmFOCW7dth42eUHVTdPwb4h__9OjAskv3SRJAAGuRiADSeSVj3h04zaB8WeYXLoUgx1ukcpxCOUA8e7gYzD_J09kDMgKx0w28saST5NphoDq6C9BIq5zInMzusTX_Oej0ky4fqHeU3JD1Tqd5yzujYuX5jDwSCDbGXMXoyHvQnUiNFD-6Mr4R5I5FHGKroHYTijj6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrDsE8W3UWUiOOmlwh7KXM9oAUaaAdu44agWr6mK_yCA9sCNuxMVV9OAbSaaUcYYmV93XbVP1dI-UbqjrLahHbfKi1yEsi-f-fLNWXn58cAn-msVoiC0StBNOyc5aiijD_uTON1Ckilui35TOkLIJf3sMo09EMp9p_ISfo7-IxApT_90wr7YdiuFv-O1yS2f_dMnRyXrMkgvVEJFhzbxs8A5jUI8VVWsDEWfZFcI_tUw2hpQ9bQWmZkREj6WjZk6_JPjCQPBLomgvyg0xs2KgacjfZrJ-Q9pbafam1oYbpTbPExMiMd5tU62XSeP1pv8W3Lj-BnfkgmbGz-BRsUd_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbwQqpiJXN0ocHGgao7zFla0YivjPT-QRhwCntWCOMHe4NEbRGqFz6f76lxwWTcno08IQNZWfoyvhT2PtX9VPcA6KzLOnlwbKQAh9MwsCZTle1fOLcQ0NP_7JCJneoQ2W2rB26v2bZvKOuyj0Wu2JBv7lMVScSrfs7uPnp2nejQ734UGcDqpj-1mw-kIJpZ4oTIQ45pBgaHJJSKBWMOjX8q2PZuaCgyc_fiHQdJkemCUxoLefxTbGQP06JHs5KKOxB2a9mkbjuY0-uLgkex-rRwowlsvqha-PkL-8_jFdPwgAFQdeoDeqjrqfdJZI569mX0dJ-S8p3i2sOOdFfgFlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7dqdGW76K5V3RtKM4A4qrNK3kCX8KE3rgKxI1hnfFR3Uvmu2KsON74gfRjtIE3cfBB0uSey6FU5eljFireFgzaMelo39fjmGGc13tRfewNn4d2Vk4yRzqCvMM7PruGK4Zdy9Jd25hRowEytbmdgUYaAwhD6j46Ks4dhRMsbECrS0OgNnQ09tcUfQEe4MEKCDfJpXMaY1G0Mmi-BNG_fWQzv4SYuEqGudY-IsLE4RQtVeTNPvx92w4Ux600ifSqLLTcvWZOaP9eKLs3H5cq_pb7es6pasWeLWKobC7f0Ju-jM-B8RkDqL141loNXiFoy1jH_bOyP7q9VIREjyFv4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gxu6_JmPVUbaANEWoLZ4uphrCSOSEhhhPJkLcaFjSVwfqfOV2w5HUMvYH67yd0kykYF-dFYshm--fCwL8ZzJxTn3LtOT5uk91F_cCyFGHbH85sI9tnkzW1AYEBBeBR5lwpJj6O7oI1FO1RDl7l4YwJpKEYMRMu5aEOrUK2DwWyGeXtUNbZxfUeWemJcqpiMzaxr_ig2kUVDEE_uf9SdVnqGp5HVyTMfSanoiGxo_OiCCtCQVhDB5zZ76S9G-4FXXpH8bKTbW-uAjj1mAJdj1BmZYDLLVdlLF5pDTDuT6uxIAMQrLYN3HB_vlhmAfg2iP7v8xJmQeOYqum4-ZxbgGoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
