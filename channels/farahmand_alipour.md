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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 21:15:03</div>
<hr>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH6yrJdGXD9hgPYCMzg8JrSghM6SX5mk0I0iq7ffQmyjln6dBObrTO2icOW0cwxmGi-nx45x0TCzTDc7QGbeA5NYYVM3uuV8mQjl5oX_MV2A1Udo1ejksNGz77HSO5Pq5jQGoxlZC9y8ddiO3aqeUrFBXBa63YFvg2V1zzLZ0Qnf_OLVHOGsTMAV1upVxZwXvQsMonYJ_x3DSDF0F8eQ1Q8seRGHgaWqLaCIYPY7CI3MVNSarxtJPkvBsHG0ptQ4QmBSaoKZZWHLfeebZLQtb3I7TwIBv1NsdVZN41lf9PHQPSne1eQHsBarogJsrIb5dYbBo8OwBmQfiQN5EbqjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8D6xoVzq6om_kzaBAPJOjFiSt6SsLtMo7qEujscJ3E6-ZtICWfKjZ4aSKCGm7XbWBId7elHZwqaYv-DvNsN3XlBbac_IZKL0AOmr-R5NNrab3PEQk0s_nIxuF0TRb54fILxeMeoqAe2EbxUXvLglOJOiygdwvh1ssBLkP0ffzKk5odXzPaDuUj43TtJZOhltLZRoHCqqRu7J4WXNh0RV7lhtD_N3_nYlC8t-0gM_EKBlQaBj71sBNEYFq0_DjxQW3Fc5-f0ubWPzil_d-k2jkapEyixVixI_mysPwM1YN18K6sNORfkKX5G5IlPpYWYZXcTnM5V7V43EZGDGG3EqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucbQr7JsN_P1dZ3G5yxDVBNHcB7tJn5PBy42cO4n1l3zJi876RJ__qCQTAfJBpk16JKmH1D0rPp1JkGorFu9_3a-9_caMnosRrnIF93oY4nI1byQJzhrDIMMP1Hx80kknCCqIESFuHrAmQEEIzmsPYotl0wnA8av94TY5NBE4Chvpxuz903t72ZQbNd5LJ4H-IU9EPvcZjIgcpF2A_7vXGYQ8xNRlirsevsJBEhJTrsWCl7J76NPaea8ZUi4CDyk0TfeBEfF4n_hSIQqEbPQWG_JsEtDMVx_yIXH467FwPIazH53PPeTA40gotqsa_50E8eD8WBPxivkzUCXh8lT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=NTT5KlDGyP1BqdKtMdELcIqk1MrZkrF_OXESmrNpC3CBMTqYFmsDRZJOz-yMro73IcvMuhrIAvGNgzMl6IV-ExYKL03_pLLgR-3IB6L4jgkmu7cySZq2DEqbfSt1voF2_KBJS612Pwb27mH8xkhJ9ywEpdeyTdxmnzANWzaIBJzzoaRw_hURGbqQUHCN8JwO9l6RRTISUPWsO4eo75h0RHKLeapPbD5KWY50BRDeoy1c8C0yD47ZmMuPpG8dqNhfjpK-TtPKlrpvPjAD0us_AYMh3yxP0nvN9ywJ3xzQrb5qQHSEr0ehaOXGvKJ7idz6zxeDmJelYGHWGCmhlVM4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=NTT5KlDGyP1BqdKtMdELcIqk1MrZkrF_OXESmrNpC3CBMTqYFmsDRZJOz-yMro73IcvMuhrIAvGNgzMl6IV-ExYKL03_pLLgR-3IB6L4jgkmu7cySZq2DEqbfSt1voF2_KBJS612Pwb27mH8xkhJ9ywEpdeyTdxmnzANWzaIBJzzoaRw_hURGbqQUHCN8JwO9l6RRTISUPWsO4eo75h0RHKLeapPbD5KWY50BRDeoy1c8C0yD47ZmMuPpG8dqNhfjpK-TtPKlrpvPjAD0us_AYMh3yxP0nvN9ywJ3xzQrb5qQHSEr0ehaOXGvKJ7idz6zxeDmJelYGHWGCmhlVM4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3k8KY8kGJvAP2AAndTAuIcDP096hiOqHTX4vN__zSrCUG0XWofcZCTx22ov7tmWhSiTc-vF74teZiqGYAFjm1a6DQH801ylGKPGAdqcqOaW6wViYyrTtuOfzifaUmsM0RwwoyV8VKlihrrsyyJpm9f2BD31PYqOQpRtWvIrhxh_Lde-QQMSYONGi7tQt-G9FBVZmySHCZcKOLvhHTdUNu3_NZRaLZeH7F7h5Vn6ufiMYQb7fokh-SNt3LlIBCawziVsp_q95a1wCExGQp_ayPotx57smXhxGaLlpPzT5FPSdrZvIbWTaNpDp-SkTt7fdVRt1PMBIh0ZmVKn11t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwsBSRMMsea8Rh-Jk6A36yJIVd2Vh3LgTWw11UH8i3TDitHOnAV7q4iH_7z9w0o2FB1l23z5s9UJCcy1DnMe_JwKFIBhS0IAlMEL2HnSPJSSEIDTTpD41poQ3z9xA4rR7FqE7zH03J3vxG6FsOTiJ_myZtzB5f2tdMZKCX5fLB2z6_84jpBkG7RrMfHoQW55-ajzkvQQdVX4kIkSlpkHTEY41Zy0yN9AFJbRo_WSGsim13CLiwBJhh8DrtrGjellCD6HETb9tuIdrzSPDD-YBRrN_OUV_huG0ScsuRwh2aMU1kOBD4qovMYzuEVwyEqkcXYtAwi1LWvSCxuJ28ilKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Rb7vOKXYANEkdTdXUwNbKtOg-yTW5f-WxScQdtnNehTCQts1OMRXGiJHXuN-NvzLsoAbMuXaSRGF2nBuc93ChBu9zXRTZNqoy9ZTksUAp7KyDRfB5kjDi92z5gNuHB-5h2tBtgdb-8q2hY1A69K2-ted5wmOLhZR4FTjAn_Apr9ozSJgTRLFO4DCAeHIZuf-kpTCp20N5L36G6wCxcgJbJ5dPD_as9diM04QqAyF-4_kET89Au41qQdY5JLTuu8O8Y4Of5rUkaAMBm3J1fgTxJXIUHQTBPYVoLOwQYpZTJzsvYV1E7jkuKx4VW3oGDfVlPx9bbXLAOkv9_s6AgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT1HP5i73BrF0rHXYPbRhvCwCCumQYuZRCouCsjRwTE9oUYOTje-d1Nb794nIcCKWPaAj4PhYi9gVXG3AIMTc1TsZGuT-riYOZzYUog_eFH7PFDGByqQ6Pa4yw3lXxRyRqcgybU76tjAg42P-Y4-fnprQ3YCQ-B_FGviFtb_lYluBuR6tiIBNEvZN-ibKDp8uzwXGaLiE1lrbsQAgA1QscyzS3GUQU7_KKaKnF9JLoXSLihkp61V-MIGMzmvb-Rpa-vNBSjkeN3Qn55zeXy9xC9NN0PtCRlvfEQHH4KlXGQLJ6G-ySbJRXUEQke_4hT5MWCsHnbPocMsy82x3kun3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIHLbjKs0ssRziTkRTyQVS9g4bfVEU7EgdxfAge9Tw3ccVZDVxII0qKxt7HCr3564hrH3kjngdih8mthqx2pwg8Kid-SDxLzYIQRrSzjeepzXdSlWhCVG6wDawT_IaMVdjRECSWoDOWxSyhlPe5nfjgRsBN16SlsABMXpC-aE0qrP1DbcPsHw4VuV_WrHnzlNsH_DredIKg2sBuu63wzZScz6CxhFQbap-HevmzEh9c9XGYcu-Yyk956cE6sI3vWu6a6coh_nh7iVE7oflRnovPOLfRcV4QGBYFy_dBe6X94c2QrEuRH9cWHTKewMQj1esQd-4qAm4UVKpIYV9c17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9leVI_CaN5tmNIWiUgSumsdnV4nuK3H33lzg2RkplOyACuV8CgIfgr2fq8-Nn04WrXADnrSm6MFGZGi4l5LeQBxZypCZJA0aIReoH8yJJwbQHqTsAyQiusguwPLlUdm7GlEZbQj5cEy1HITl0iWL1GI7k_cXmBKoQ1kMIb-uJRjhDgzlNMpypgYP2nyuAd94ZABiXZM8EJijE0pTPspuF9wI8AEp5YKWgB0fwZfpG76g3S4zCeyyQGNEPUZI9aM_lU_eS2_ntEudumovxgwChQea5hGcZcHQ-BSLkPag-7NqlftRhlhZ51jsMRodm3umkcEQVtkz7_iTR0YqOEBkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc9qTT9iwE9OJXleQEMWUtY1qGHNtmCLOcWYPRHcsYRu7u6r9zaFQ-G3-9m78YIDR7mhZ-zySI7UjkXz3a_N0UnsS6TIpMV2CXfQ9t8JHSU2ECFyXGad95KzuceoFbW9SjOd_hKUq2oAnQd7ABPsMVckLpPDUnCJI0R3Ym0lkRTm6ogj2rGHyO3sTBX1OOdYuGbY_Nu-SmMrSFABC-Li93cJ9ceecqg71gVmxkacUgC6AHgmMvVLT1EmyIXY73QkjpHol-PMMpwbNh58dBLC_nm9NkySo77YQt9TEGTd0h0HeJqfIznBHia001WN1rktoWu49TIxexstxvYXbNPd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2-CH53y7F_vB2Ipzbb-_kx-yUx90nTzaAgkj_mPOg7jpzZuVr5JNg6oI7fYN6NX797OgnnFVK51IRE2uLLXzljI5DPojkO2SGrpuQTp_Md6fXhzm-ODV519YHFmM0ygZ3qV6ZG_yXjh1CZ0w0kFk79O_XwdXBdNvrys-8vmgclYHkvLQEH8PWTlDiHxpuEoxyFbrcZmgV05zkv6RLcSXkQFkXMB4zEd93XCZdqprGSy4FXpYZdt5-VStEJLxG9KBQYPt3ahG1Hr-nmJG10TiyUX53mXct2GYmnTO2iTcGokTPAyE78nfhbgQfXr5Ff0MjuOifpzMmn3Y0mxJuF1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4QEcS3xjni5SEku-2iaq67tOSDaTgNo-Ih2OM8i-rVly9gCm05hn_Vr6aYB9BE2htzUZgkwYwNSg4B_m6ZSZzeDzeCiMoP-pNt55EJSqG1L4MIbw7YeTqhXkw6iSI1pQpthOm8fM2yVoWZR_R6_AuvSAbaoDfGBseT8g1taGppzjPntwFgIL4pSh7XVj-sNkKoFPEgcyO_tp6qg2f39m_RBCe4zBoGck2yINP9Q7oq4rWSHuTE3loI4q4wtcdwEfVSSrdalq2iU6N-cwihbt9zz7Yx9lQ3iGaOHzu3htNbCz6Ne3QNJueCDOT9fH_XylwIe6KwQXNe2J7PGPP562A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=EPjMA6yHVd3aKreada0HI87dnW2IrHl_zGauMhPAysYpWw6xdh_pynFAlmFBuSClG8qWaBdnh3y6BsF8Lkc5Pk491OBojbQBuWtf6_N8OApkHUtCZxqSROePP5lPPc61tq9yT-Cm09G6qhBHukGAK-36LKdz8RNw752dcRaY6yjM_e_ksoUKP442DEArjU4FWnxFNz6Ed0at3xgk7EjBMPSAOA-1QLDLzTs1sxv2bg-jar5k31iuZ98zIN-rG0hwHnyAtAeB962cMpQJrMi4wfPq5bOS83pXd6E1Y7qJecmIBd2Nx28iCtScxJQBnp_4HGGJLR1Io1zQ1tpOFjOLEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=EPjMA6yHVd3aKreada0HI87dnW2IrHl_zGauMhPAysYpWw6xdh_pynFAlmFBuSClG8qWaBdnh3y6BsF8Lkc5Pk491OBojbQBuWtf6_N8OApkHUtCZxqSROePP5lPPc61tq9yT-Cm09G6qhBHukGAK-36LKdz8RNw752dcRaY6yjM_e_ksoUKP442DEArjU4FWnxFNz6Ed0at3xgk7EjBMPSAOA-1QLDLzTs1sxv2bg-jar5k31iuZ98zIN-rG0hwHnyAtAeB962cMpQJrMi4wfPq5bOS83pXd6E1Y7qJecmIBd2Nx28iCtScxJQBnp_4HGGJLR1Io1zQ1tpOFjOLEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arAhadIAQ0Dw08SQsSmK2MBBrJVrLHvSWs3OJWjeG_zUsWVDv0S1KYi7xzPZ-nGDR5eq3LwEgwKIX8ur0_pc8H-WgQpxFhxoE-km9O4UNg56XM1_prxzCgXgrRYxDrRzFwKrvoX94TWLAIm0VusFnMMbSZN93EjVtiNxOAhf3HKEkdmLotc3RB6WrQjVDHjEk8VBqGVj5pA5Ef3DdY5oZJ2Vj5griM16ggvm5dPboHBQOOMDCTLKVJpJv3M2jZVIF9M8JDh0iyftsXy8nOCoEteqRE7a_a_AtniA5AzMhS4hHJYmEpZwWCE4uTaMn8DVCTNBNa8pbt-WdurJ0hPEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJkm75bNKZCpadq_4Qs10n_JDOMZB8qerZjVCu8vEj_pkV6f6QTvNKlHUjwf4qKiM6l6hIkVcqeK2-ev3lovlFiKoymhS11z91xg26F5j7L9CJZqc9VlLBeqQozCUcDDExC1-rCan2qrPmztE5ovk-WbuWIPwodCLEBNMj4yfFBrtmpixna3OpFdF7uA2amc4VDiHzW0MvTsmbeY7mVbywqjyzHsfmbo2-qAu2d9edm5DgFgE36zrj9tcQfmjWIzglkRfWLcKyrgE1nYuFch3b777nVvnv1E5PMCL_6o9TpkdWUrss1etV0LZY5O21bgFUNLoA_1WNZ8uU1UxWi-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYBGdXKtROP63cmmZTRsmpJxDLx3ZcyUpeI5vfoR2ijVrjGAHdDXZP_u-EWRB4WjwYJykEcuGKV8FQbaTyNvUhfevJOUntQtX_SjmBT8zwLmIb2AN5apZ7PSu98-HuArgOYyKpdrNtX-JtIgCerxwaCxUHza5xVRMRvVNCJBULTxGHP5IDeQA551c6c5PSWitNXNl-RTWFRosELuI-I0v85a-4Xi-HZZJi_kPKT7GwPulS6o3Lf_2f9-hrqC7hEzqH03kEt4RVsMFDDe0c-klUAHwzznBV5IuWTs3utqo5XHX6QsFFW_XcoeoXD_tZilncZpQoQXM4a0Hocbh3ODcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFrwbECOqEK5iiQEljCLRq3d3-ySvVSFfTt8GwXr5KUJvPKeYmdhw063lcd5MArweQScoNfVFR1MGJPaO1uJ0skRciTy3eibvIIeJ9pwMg-_gDOwWScesjh1nHxS4iUGaSfQLKOLhK0_Z1KwYpv-AHUBNq6zXQipcRpbjPdjhPwImdzjtkJof-kf4POACPdD1QrFOn4xJLKfYFjR7VaKdgwrzhh3X8BruzkPpzUWWOcsyf6RafTRCe46Nm5wYt7PwJFiRwv6gSxBKGc4AmFyA27Ctof6LiPRYIZ7oiYd3UsbXVYqLyNdJv941VUDcMTk1Sg76Y2brvPGQrbrNi6Bvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=h0zGgzAKTYENf5U5nZ_KsRLe4Dc1okm8cEQqWnzsTLsjCSdNw0AHAlUZx1y3NDYoG1cmlj0WoTETfBkQW_UtZhMgSR35JXH9c2sd3u68yEogvEa-K1gsulkFNMvSbQGhXEAHnf5RmaaxWXftYwt0NM3EuY1kQ-B9EjaK6aIovolb3_Mzc9OHtM2DE-BtTYpy51pJNHJ_fs-Uvfp3Dym2N0of4qpgbqk51cCHY4egAZZb8JOU2N20NnBeoaEbBWNj2Cz6bxFy4fNREm4wzAsFIlmsPKj6mm9PisOvLatdXVzpuauEUeL72MDuq9uwe7XRXqENbVdVBIt9_lyU408oqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=h0zGgzAKTYENf5U5nZ_KsRLe4Dc1okm8cEQqWnzsTLsjCSdNw0AHAlUZx1y3NDYoG1cmlj0WoTETfBkQW_UtZhMgSR35JXH9c2sd3u68yEogvEa-K1gsulkFNMvSbQGhXEAHnf5RmaaxWXftYwt0NM3EuY1kQ-B9EjaK6aIovolb3_Mzc9OHtM2DE-BtTYpy51pJNHJ_fs-Uvfp3Dym2N0of4qpgbqk51cCHY4egAZZb8JOU2N20NnBeoaEbBWNj2Cz6bxFy4fNREm4wzAsFIlmsPKj6mm9PisOvLatdXVzpuauEUeL72MDuq9uwe7XRXqENbVdVBIt9_lyU408oqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8MMMSL_bukzilLui7ZbaQBlQg9Pp6nf0W_hClw6k_38KzgkD_6NQwDE8QAC0HN4M7NxhlHr7V_zXrqKQFMvR_cI4YHcZNnk_rL1miPn_bMZfZhmSXN0qcjerCUZa0BkBrPNFGLFwixqLhqdZOfsl0MCiItzaffaj0gQqY6CLHGUJXe0zxqOguWa1mqbnUvat-My3AG1Pf3IUTns20YxIkscDbjrVnJATZxQeVZk_KQInjC41nRRHKRYwm0vU4SX6AvHsa2sWEFJ-lkP1jE_rtjegiOMelQFaVtp7SQCmz15NgcFlZ_jbNeu-QpB34s__z35-ZhvfmHpgX6P_oskTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=oYtM6_rNFh0Pszdpy0ReMJWgqBWS9T0f3GboEqHOLXL4BD2FN9Q6OcY9W7yIB0Bve6IDjqxfqtAxA05o-ZMk70i8OwAKIPN4WPmwa4yAR2hsH9eMJEL8jTiTyNTAyyQYzb63uFUq-zJxaydVjOtZSQV1oxajVMvW_UP3aRHuxRBe1BvOUPHKJIYDNjdwQmHOjDgDqyfURgovPC4dnn1hoGVIKSNH-2WmFBPgaJIvIlYONoEn4dl0ID-P-zXgqtJO4H-2_O8EB0JfZLf0Kz6PkPY2Wu9c8tkofMu7sHQPz1P0K9dyeDzxRdNrHZFTiPNjDRz3aZ10sETy8trHIwDoYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=oYtM6_rNFh0Pszdpy0ReMJWgqBWS9T0f3GboEqHOLXL4BD2FN9Q6OcY9W7yIB0Bve6IDjqxfqtAxA05o-ZMk70i8OwAKIPN4WPmwa4yAR2hsH9eMJEL8jTiTyNTAyyQYzb63uFUq-zJxaydVjOtZSQV1oxajVMvW_UP3aRHuxRBe1BvOUPHKJIYDNjdwQmHOjDgDqyfURgovPC4dnn1hoGVIKSNH-2WmFBPgaJIvIlYONoEn4dl0ID-P-zXgqtJO4H-2_O8EB0JfZLf0Kz6PkPY2Wu9c8tkofMu7sHQPz1P0K9dyeDzxRdNrHZFTiPNjDRz3aZ10sETy8trHIwDoYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg8w0RhBqqqt-2hzYrxgCBsPMHyD8jpC7swnwKshj0YJwtQYlNGuMDG8JiYj-BD9y8J8V0cJuzq2_amm2OWBvK2ae2afzUQmWQc1uySQBmahh-9smjw3XJSuAkV_eBAm4GQ4h6gw17j70asnPHqAG0lgHA07UBatp9hT8KuqxaTASvIZh-sDpCUCidz1U7juElYzPdBrHlvROnboFWCz9js7HaMK6v46FATOAaXlQ8bNdKtsdXenQXmtW0B6gKewmnC5z4Oy14ObJcUFXXx-18c_yvmup7l8F-q4G7vURULUPAwIJoqIIhU-QwWd5kD0qhxKAxGTplWTUwMgNqwIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIYfR2ghgfHFML9NsroMjh7GeT46YL4_1QDbemtFHqS0dmTpwkZ4-6aJdup6N-HUVeXKyxmuHMAZT7Vi5lDgvXVvUqd2eEz6MEJSlrsK3wBQS1Qw8z3IlmuMLptJsoxHlUDXnV2CPtW8uZMl-WNUc-6G1LE3PwQuVLmUoPL96cQ5CAZMylTBu0e_ca0K75CV-nv3DlYYcNYhOFBF5443WkxguP-mBAFLT7pYW1pHma1uzjX90dT4f_D1P7FxwkKXqjzpOH3u3sQLExgk6tUeh3mkj1lWQTCwpdnSSCL0BrEnaMKHxa1-FVLJU3VTOP1lX7bBG1GxpIOnb082oYTXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=YZMZ0xXFzWPTU0bnov1AR0_OgF7ht_5jWPOK9CWHntN6jfANn5OSaY8geIttoLD13d6QDHjqzqA_7j_-0cqhIuTLUn8OI6XxSItWEdHSSOz5UYlKh1ShHr8-hhShvv2nDNIDg80vU-mGhTwIAvLf7PpUnBnDCN4GeYELcmNNNGtfmofhmT7VhxGS25JgeYdlf2HU2rdT-tSTK5js9gkTTEXVmDK2AGWuRAuZcc5Ra9IJ5XLrQR5cqnvSrOIpfEK36-0xpxSGhU0Oi19Y0HDooVjrPvA0nekQJy-D5Uq_rClyl6m7r1XaC-A6tJC49NK4N0N1sJxl49nZiK7k6qzd-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=YZMZ0xXFzWPTU0bnov1AR0_OgF7ht_5jWPOK9CWHntN6jfANn5OSaY8geIttoLD13d6QDHjqzqA_7j_-0cqhIuTLUn8OI6XxSItWEdHSSOz5UYlKh1ShHr8-hhShvv2nDNIDg80vU-mGhTwIAvLf7PpUnBnDCN4GeYELcmNNNGtfmofhmT7VhxGS25JgeYdlf2HU2rdT-tSTK5js9gkTTEXVmDK2AGWuRAuZcc5Ra9IJ5XLrQR5cqnvSrOIpfEK36-0xpxSGhU0Oi19Y0HDooVjrPvA0nekQJy-D5Uq_rClyl6m7r1XaC-A6tJC49NK4N0N1sJxl49nZiK7k6qzd-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWj7mxC5WFo-Ed7FAcYChg2Q3Gj8ApX5gH6d98FiiBVRH-BiNmwy_SnXMgU80wIgfOYBgFp6vRB21nR2cGbgeKblpSuJAtdFIZNVYtAB45TnWnaDf0ufGvBEvZR_0qwFFdKprT8a9eDEW3-5gAu57O0jgiD8bfZbO2D30qvimQ1tOYAkCExAF5BLiyEP9wstLJ4Y9BYIiZmpCOiULopaFzKv6LOzOMcFZfg7ZqZUAykdov7BF9NboABF2MSFumKoa-Om7JtPW1PysTY2JLlM40qQARF1CPqEPqS4oM0YiEkggD319nw3hAsebXpcUpIf15517nTSNkluxfsFaywalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=lQKJLRwj7rbr3vD7_hMI5zuXjyD9fTwKlHgDfapffLlwGeag-FUcBrtfa3ZXIh4EMC3Ma-q1B-8xQprTqUsT0d5acuhc2XTxfP2o-hGx0nEIhuZq4nkKIaox4HmmWhKvWXwgKMrU-eUVjIiQFndTZKLL-bE2j3LZ6w_DHiYjggYHiOpjW5JwS9GDFxTCZEDz2yfNrWYi1nT6j9ES5xNu5r4yQhYMjPxPckm-JoQkPG3TtLB5JhSOXpY_AeC5Z6EDtmaAPhKhAmkcbBO2ZXadRd6gnTPcqlys5NRzRZ6NI51MGKyQoGgjriHMzTs3_39bjif01iljAiziJSz2JD5jSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=lQKJLRwj7rbr3vD7_hMI5zuXjyD9fTwKlHgDfapffLlwGeag-FUcBrtfa3ZXIh4EMC3Ma-q1B-8xQprTqUsT0d5acuhc2XTxfP2o-hGx0nEIhuZq4nkKIaox4HmmWhKvWXwgKMrU-eUVjIiQFndTZKLL-bE2j3LZ6w_DHiYjggYHiOpjW5JwS9GDFxTCZEDz2yfNrWYi1nT6j9ES5xNu5r4yQhYMjPxPckm-JoQkPG3TtLB5JhSOXpY_AeC5Z6EDtmaAPhKhAmkcbBO2ZXadRd6gnTPcqlys5NRzRZ6NI51MGKyQoGgjriHMzTs3_39bjif01iljAiziJSz2JD5jSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6l3vPUIJ-QJuaYYfzKkv2duoDNlKa6Znh85kPYVXQ30I3qksr4JjX3k5jyh37IYyQfYr7CJ2qUTMqlQxY5nsjOW8WovScwwrCLPNNo3-afm2deNjn_T5Cfsa5ygkMn20SzEs6OK4rhiBbTJ2m_nuX9z3DvlazAltB0IB-k-ub7eOXfVD0KNdOmk7H90wuqy-FsM-JERaqhtPmxvnC8ynVYznd4ghQ6noY88k3bEKKBwjayACeeNreaRFKyJQUaaZC7kp0INBnq1kOssfDnAcgg21VzQRP6ZCQzWl1cMQqn--HkcPQ9FRY0WxAUVxfKe3B757BLczCfDK58yYQSQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbZ2R4gM2fZMROcQP-RoxKKR_38t2q1C2MmHPmXtIewOHtumbm062rwvRNRjzi5v4JXTQ7HADKEWHLFvmwUE2Rto_zuE7KNchIomtGBOc3zMV1YJSkviubtPjp1Zd8MqAfSEVyK4_3I7DOUveMufUiQvaT2FGFrEqvc0QDMJK1s02UiMzd9WBlNx5DfP2l1rINVzl9qcAcuE8jyLr9bqAxda1owaGQ3U32ns6DtTj1g61NI-RGDQvBAVENTcK2JAGvfZn4G--imIzJkL-dB0GTn0vo3gU8SSaKXkHxtz0Xxp1F6dvAHOZGtajzJtStFA8WWbaXXb1B9lt-IH5Nl-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfAAMHoBIF5AAgab2t4umzt66i0MAvFUDmap1uAkiXeBCghahm2s0bpChU6SsgswB4wc-RcT0zWcAdLBC_C1CNsajTmGeaeZmRqxMQNFdE1pyiQfzzNok1cPEmSf9Gc7FXx72h2GeIGQ-yA4mGcoO-ctfYGDmIe8h8lclZgco_-ZplHBNf69ourxbkbYqNuzhuj_iVCmCR6H2shtwEXHWU6T2wsAM6rj0c7VULOlEg_UFMW9EKCY1BGcdXArx1qDoqnLi-VJuidKkVAOmKXUmt8qG9VWudzO48YJkHmd8wgpnw4vh-2nWVl9_RmAG7IvZsmyqPqlT5X8olW1JKsM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=N5HmUCyVEcC6xxUjc7RCkM8Dz_opdZy7Gx8sU2PL5iG3D0PHnWxih3N2OsvV32dBGvs-fmPVQnr_pgDMIMQkWM9n6U_JgKRa_djVh_nLEUvWp2zxNSdZQBzVF_bPCxh10lAuhd1gDHuiHXnWXzBN9EHS33PFiEiXTm7Zz6UX1Xe27boR4semQ3Sng3rmPOIN-FUgPenFZ-aI7zpKQBu8uuT5v5Y07QekZHNXXbcZosv_IZYk96NESNm9rN2we2cDLMAaZJuVlldTfX3ovWaSTB7Mq7sFTnY3qdSq61_6C3VwHLVpgggLn3mfD5aYS_1GLF0dXjJbUMKdcLd1Cff1vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=N5HmUCyVEcC6xxUjc7RCkM8Dz_opdZy7Gx8sU2PL5iG3D0PHnWxih3N2OsvV32dBGvs-fmPVQnr_pgDMIMQkWM9n6U_JgKRa_djVh_nLEUvWp2zxNSdZQBzVF_bPCxh10lAuhd1gDHuiHXnWXzBN9EHS33PFiEiXTm7Zz6UX1Xe27boR4semQ3Sng3rmPOIN-FUgPenFZ-aI7zpKQBu8uuT5v5Y07QekZHNXXbcZosv_IZYk96NESNm9rN2we2cDLMAaZJuVlldTfX3ovWaSTB7Mq7sFTnY3qdSq61_6C3VwHLVpgggLn3mfD5aYS_1GLF0dXjJbUMKdcLd1Cff1vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=McYijrpSFdz5loCBQyffL9_kXm1ppDKoWudZ9sqzrnvoBx7UmYEB9SCJfP5KsDcQi9EmsaJKskaua_WsHucTQIse-kHsO7auvKluVmxsUFgHH7lvGlOjDbOlGap0dPjzRXkL1gEXcECVIO_Md-ZVjpTOFOlQXGdTxTsk70xRicbCrBQH-CeE-A4k-VusLMOUwWf7QwItHUQsz71H-SJqdzKM7ttX4kGUgX-clZWFCXDWCERvrEspzwuXys8Z3O7dm3DejqJp-RTCHlrk5OpT4e-PLEbxYBQcvInX9HO_GHxEKR0jiCDZ9-6UlTY0L_y3zdullDNtrcAde7Q7PGEpzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=McYijrpSFdz5loCBQyffL9_kXm1ppDKoWudZ9sqzrnvoBx7UmYEB9SCJfP5KsDcQi9EmsaJKskaua_WsHucTQIse-kHsO7auvKluVmxsUFgHH7lvGlOjDbOlGap0dPjzRXkL1gEXcECVIO_Md-ZVjpTOFOlQXGdTxTsk70xRicbCrBQH-CeE-A4k-VusLMOUwWf7QwItHUQsz71H-SJqdzKM7ttX4kGUgX-clZWFCXDWCERvrEspzwuXys8Z3O7dm3DejqJp-RTCHlrk5OpT4e-PLEbxYBQcvInX9HO_GHxEKR0jiCDZ9-6UlTY0L_y3zdullDNtrcAde7Q7PGEpzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=VpEsqL3DjeAaGaPuGUvUKFU-hF_BMuOTBc8IWrQhYUOBvlNPRTbL9ZJ-a3jpfV80nLCUZ72A6pWe1TqTFPy1XrNluWiIaYwWmNYIS2CYjhq9aaS15anw86z_8xmNloHr_O_c4Y9jYJerRf2XucZGyGROvY4_r3wXIb1x72vnk3DbFEjpDjGh5pc5ySMKJK2jHhVqDh-3VntwLOCOYmf4_IrtwcY7Bsaqmd7Ued3Dy_5jpMEA7NSAz16LCC1kTUKWeBp5sqUd0t3YWvBnJqq-A1-gARKEGBY1QbCC_cvNIaw44-GNW5sjsfCVLaEvphCe6T5VHKHLrUljbfTEnoSKryvGoREFaMzNIPrfYdgVm6TliDR81ULWV_IDZ2KgilOHFqcydteK1hx_8aJv5Q0xuOte3hzv7SJIGCAVmq4oRNChJ8hCvwPC7DfmQ84fs1xwNGBUap1nz8xuI_eoytCwqA4LPaow9VHSNphZnJbVYhHCqRBa0AGDuofpc7FlsP6oHNIujOnC7NLmffaQsCjhRmuSBZgWn48GC66pKPSfCFaU8xNS03J0WZRhZKxgnCASO6Znix2_ECXaEOfkP1678FFNXYOVd-_aHH4HEVNer4fch-fcIAiR5FwN1sF6-BGY8XLpnO_anNys1oqW04vxvpVv6aDjp88hvTfpvxU9nwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=VpEsqL3DjeAaGaPuGUvUKFU-hF_BMuOTBc8IWrQhYUOBvlNPRTbL9ZJ-a3jpfV80nLCUZ72A6pWe1TqTFPy1XrNluWiIaYwWmNYIS2CYjhq9aaS15anw86z_8xmNloHr_O_c4Y9jYJerRf2XucZGyGROvY4_r3wXIb1x72vnk3DbFEjpDjGh5pc5ySMKJK2jHhVqDh-3VntwLOCOYmf4_IrtwcY7Bsaqmd7Ued3Dy_5jpMEA7NSAz16LCC1kTUKWeBp5sqUd0t3YWvBnJqq-A1-gARKEGBY1QbCC_cvNIaw44-GNW5sjsfCVLaEvphCe6T5VHKHLrUljbfTEnoSKryvGoREFaMzNIPrfYdgVm6TliDR81ULWV_IDZ2KgilOHFqcydteK1hx_8aJv5Q0xuOte3hzv7SJIGCAVmq4oRNChJ8hCvwPC7DfmQ84fs1xwNGBUap1nz8xuI_eoytCwqA4LPaow9VHSNphZnJbVYhHCqRBa0AGDuofpc7FlsP6oHNIujOnC7NLmffaQsCjhRmuSBZgWn48GC66pKPSfCFaU8xNS03J0WZRhZKxgnCASO6Znix2_ECXaEOfkP1678FFNXYOVd-_aHH4HEVNer4fch-fcIAiR5FwN1sF6-BGY8XLpnO_anNys1oqW04vxvpVv6aDjp88hvTfpvxU9nwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t04S4C8k-tHx3LWAaO6_ZjZSKImnd5T5aPlBlXj3Y68AdryU9FEADe1XpdRs5YsICyobbEAga5aBG8mhXVZnwp794mApIhoKIO2ly-1tgQCb7R4x2ME9Y495x76gHMnLpc31HQ729tMqS4mrsB1PC17bpegyBBW03BNWIuUVXoboaDzOHMhx9npSFQNZRlfFwJHGuVpEyNcckVH7FPZdBaaOdNOUxAoBZcLdFKcwVCgkcKijyKOy4nX7G9ahTaQYPS2Nf5UUAqnskQzKnQpormFqGtuWHMSBP2M7zOZ4uga0XfL6nLutqpL8HW_FMritZCnLsZkGE23Mek-Zq7Y_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-adBREbqaqFjV0HqYg-GvmufY53YxzTbGMuUw0uMaLZheFU7CMBhjK0iY8uSkp3tNSVpc62b8VScHUimDsUw1xb3tLNGqJZ9m4li2M6ho-oMJGsmbvmft8-0i8XLWFi8c2SgFZvs7PrLyQ_89XDtP5wi8m7hSnrj8qi0I61FRWN39sRXlzExlgItocnW7_Cn3DjKg5EosZvaY9Illt0mEdIYohzAdNh93b0pjoj9yhgH-E2xDTjhc6KEQIRQukeUQxpVPCO2gYaa-Q6RmwG6L8WaYjwPjZPwlvxSU25LZ_67phpZiIJewy6JRZGEyRAJ3RnJ9c9qXR2wOICknhsIXho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-adBREbqaqFjV0HqYg-GvmufY53YxzTbGMuUw0uMaLZheFU7CMBhjK0iY8uSkp3tNSVpc62b8VScHUimDsUw1xb3tLNGqJZ9m4li2M6ho-oMJGsmbvmft8-0i8XLWFi8c2SgFZvs7PrLyQ_89XDtP5wi8m7hSnrj8qi0I61FRWN39sRXlzExlgItocnW7_Cn3DjKg5EosZvaY9Illt0mEdIYohzAdNh93b0pjoj9yhgH-E2xDTjhc6KEQIRQukeUQxpVPCO2gYaa-Q6RmwG6L8WaYjwPjZPwlvxSU25LZ_67phpZiIJewy6JRZGEyRAJ3RnJ9c9qXR2wOICknhsIXho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-z9Y_wG-4G-Jx62AF22N91swfF5Fj6fXq3VBxJCRkiTOkbWA2azidSHwuxYpd9oGBZGUQTCI2lnN1gni3MO0HzNcJzOCg3ue1b7m3YGFpylO0CixfvAw12YS6faYBEfLK3OR2Gi_P7sPkLz5T2D1yw3ptcvHyYHnp3AZkLmro07iE0VqZBhZGMV0mRmQBCGfUzJ98yPT-zoW-crgmJmJCH9TxZx19sQgxkBNgGjn4onFEeyvdR9JOpu-Uu_IWqa6z6Yn0KHJRQ3qY6H-xHqdMEN3cF-UibGECgbHrW4jKtr8syMxanbTGA4FIUaePxc46PpciIF_FlOTyLZ7uVoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAWo8d3-qT3cqrM__3eBL0_KCFAjPenZpL_2wVqObcMnBEfx5IIJ-7cps9qj77bxTA4M5--1JLnul1Va4rMYq9mwSImFEWJ7rpQLiGOxU5JaGUM5Y3g-xo_HuwNWWxvD4QZui3v4zbrFhK-MHCFSurMHRpnEqithpxfRzOfwjQWA2gv5jzIKgyTWIYXurdtD7LsROHPAebcqgBL3ChBjRPsy4vY5IRgVABZbTfZnlOPzS4OiSY_JvkzAdUEMGZKtKPm0_XVpOVVJfA8FH8OhrDHffaFduPkxiaa4GcZh-7a4ZUG0amjyS-TQB4iAyKpIQ5XKZvBd_OlQ5gc0wOo-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heKN4CM0WdTSvc3CU9AspEanTyi37vm7mfbF6iA2woHNR8l8OInIveTkkaUpYt0pklp0TzAXMY87BCb3XJgQ2uvkykAOPGRVpd7uPTKgdqA1F1EdPa0KQ5Ebw1P7wCaJM7CoOZP-uyItS4TQCEAaG3JbWD6qfrYE3szIJwx-cUJL77OwWqkJvewmJeCmF6jmo6F20hx6bXb6i63JXm2RlmtbwNwE95qneO7UINJJgZCZmm0pttbLr6Siktgte0haqbBXds-yVU7vbnRBya_6SlUX426UgGDegIuX2UsONxC4bJ_q-M6x2AlHcg2RXctbz0rq9D2d4IdJpvEjMTPvjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0nlt5CKV1IryL5W2M10QKqq1p0HzXtg1zr8-lv8NzEdFt6oVj106PVhpDb8DPhoXLO_bSTA58yjJOeUbqHkr9rrM2ZDYIXlOasY-7z7y10M7JevK35g0pZ_nWUERIVkZQRKdGOs_2RI5Qdt-IOFKrPtuLAJXhB3EysI7BiMUWiOvj1mS1ji7msUTpdwAh-94JuDRDE5VvThI34Hdeo54yiutp_FWeJp8f_yUiZRwbRb2FGNHYugohtTm_u09uZTUsl0fz4k6AB6qvuXn2bS_5bLYbPPRtxpL8gvDbpwKtwh7AbwSrhciZu2PQlrbqAePPoP6oKgLwc8gCEGfYtPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-k9PSqYODo38ZEnMYFVx9nem9fwjyfCVoclmNSYvQnxmduio_txdctYwTfDbMMeP2FTvQTWrD7a48KnbMlrdJflNhZMbJ8aYZTKj6nNLlWXVs-0qtgwlYweVfOwETz4dRwohyRfO2oBLGIXZllCKp_Tvbx3QBmdu16IDiuywoYSmFebWrWm7yk1RlFkk4oX5EXP2wGpinntsK0AVz1HVQOXEHvbQRWu15Lr8GLG5nqvJ1Q03VD64P0Uy6NaY0liAuvKWrbnfC0eujV28J4eiXZZiSKy7ZLVpIQFR0iP1iorLoiDse10ChhM6kV6vb_gVhqYX8GkKkKU_fDzXHosug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFy52oRm59NEcXTtZg3Kb_i1EV80SfdyHNBX6yPVdeVEB7d7FMXkRGsqPdNUEobstW6Tl7FK4P6nJgqzZNObFc2yL2WHE3EqA125aEvk2i_07IOye0QYFzHnb4kexm3rYuk9XU9f4C2SXbn62yNd6Nw77trJfKM1cpg37FnSSyNMNAho4Wnk-PepAkDj_qxthEhIAEleRZO011w_ejOFP0QxazxJa4QXv6fWGNkvyFZs7oO6lRci1qX-S-wvuaza-keOscohoXfv91oWUI5fuwXOqKMM4FjX7aQ9kW7hWLFDuud0cPRCysDYLxhqsbpHrZHRN69hSIQ1oLhttDpVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=QBtT0dlbprfwXasy1GnvQT1syWKHy3zY-oTMN2v6omkuT8B2M4WrWJAHSkGokijHves5CXBnDJX9vP1JgWiVBETXXZFexhR8KwGRmia6_zrXJRLcc9jS-olg9RXfRMWzmaGaXObwEiKRhRPy7o507d0YiukRma1XfijA-5MF3W3kqJQQMilyOpEW9xQNEIZpDpUBjIEi-x7MgyCgadHMrFaExRP35q_SW483aoPr0jYJJ72ogv7tebZiyaZTxoNt3bZlrBLmecAiavvtS7qm8Yh883tcZM6ReDkitXtqoWok8eK2JH-U4D7hrgICYYoss0RtFgsF7YIv1n9ONhj18A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=QBtT0dlbprfwXasy1GnvQT1syWKHy3zY-oTMN2v6omkuT8B2M4WrWJAHSkGokijHves5CXBnDJX9vP1JgWiVBETXXZFexhR8KwGRmia6_zrXJRLcc9jS-olg9RXfRMWzmaGaXObwEiKRhRPy7o507d0YiukRma1XfijA-5MF3W3kqJQQMilyOpEW9xQNEIZpDpUBjIEi-x7MgyCgadHMrFaExRP35q_SW483aoPr0jYJJ72ogv7tebZiyaZTxoNt3bZlrBLmecAiavvtS7qm8Yh883tcZM6ReDkitXtqoWok8eK2JH-U4D7hrgICYYoss0RtFgsF7YIv1n9ONhj18A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8YcppmeiqreWGBjDwX6oJDtWd8iZX2QleWB6R0MmXWuUYpJa0RBoGddMHUzhp2AX11yj87Tyls6cMmCe3CJOH-6glU4Ioha3amr4wMrIxfWjjxxwgf2BsE3qAh3-iyYwcylBlQW3lxm7PgA7DGJ1ii6H6MrRzauTTtccQ4I_v_E8kBHpq2sTUpppamdhk36S8kqflktfU1reRzHH9y07W3yueiFh59uSXAqBP6Qwt2sFaNeIC_at2ohWY6zSPStB6aqrZXsRC0GaEwR5l5rxxZPCYYDohd_gvnFYSgGXuuLTdz25Mz6tvqBy-HFx7w8ZRCJLGcpPRuic8rYOgRM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhsfNYciv0XkWllofY-xsKlIwlnTcpn5hHkG9XaaCqUDzxtXpKCIb7-B14MdlQd_ghyyPMy_7Ed2BgSUbGPeUU1JfG1ImhI3cLZMxLrz0mTidzXiyDzV6_OLKlFgIa5OjqrrIPfVlXll3RR4U18L_CsCCSaEs-mUF22J2t4EJCCwYIDsX5DcAhdRiFt5Obxdi7Pfhl5wwYKvZjwBoQ9mEvaiQ3sqcmNlb5mLs65n0b7IF9Ll1bxjMsBVnVHvMNW_uunzkmRe1IqW76aPorNvIdv5JXYiF8Ok8rH9YreF4TxqNEalBaCejZWg_X2iQ-AXPWuaBnw7cJmdpZAb_Fd4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-9xA6SpJo4mn02-0_8hBE3lMCVtN0tPYfltamN03r51FP7e1touFMiVBNuCMiOOU9bQJHlKBJV8B_Z7r1TSDNDRk4oOxoL8uvKlHjPKQMb-pdauMSRWsvnIcdH4d9mUnZ4k66OuH06_HNK0dPHxXSFgmFufjHhsgx_vC2EhagWIhEqyVBmSiOvXfy5WXX-osjDC7TTPJoxrdEIdAZvAy-yITq_p1QDDLgHZTn9mCqjfDb9bfHEF361KdObgrlVxGmll3isx_iVGaf6Qrc5nycOnM_BbnxPkpOHpDbHes1oelPpp5saQL2HBuniKp2G4mhzqg14IzXWzqVZjlbVuWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=JKT4o0Q4Q5jLtTjVWDIe3xTRc3crYFEVRpMWnPafbDkrDK2lnXsbAUSE7EHR72sgbRuTAe4A8tWrm-b_4nfWyh1blOb20kkkHRmE6N3gqGted7roq9bGZXUJ3V0cGR2YRwJXT5hpeYQWzy0Vp-xWk3blMOOWtLsymHMyXV_J9tn_EX1dCGesnX_LyxM22X6yj1GheBunTXe6-AqZ20LsWTxGnJ1QcVV2VfDEURiJ6gguv6CaKzU8RT5ymnSTfiLdNeP1UcoPdNq26yTbmbFJhZXSkTDQRDO-tEbFVSjqaF02LOeRsgc6qKb-J1KalWUCX1cXvv9WCPOtABtbklpesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=JKT4o0Q4Q5jLtTjVWDIe3xTRc3crYFEVRpMWnPafbDkrDK2lnXsbAUSE7EHR72sgbRuTAe4A8tWrm-b_4nfWyh1blOb20kkkHRmE6N3gqGted7roq9bGZXUJ3V0cGR2YRwJXT5hpeYQWzy0Vp-xWk3blMOOWtLsymHMyXV_J9tn_EX1dCGesnX_LyxM22X6yj1GheBunTXe6-AqZ20LsWTxGnJ1QcVV2VfDEURiJ6gguv6CaKzU8RT5ymnSTfiLdNeP1UcoPdNq26yTbmbFJhZXSkTDQRDO-tEbFVSjqaF02LOeRsgc6qKb-J1KalWUCX1cXvv9WCPOtABtbklpesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=Zg6Yn1HtetrVqLpykGtYPhvOewxNFZXeu8KhJjDEu6zsWXOWuLXT7I9rQYoxYzXTBKc3l1MbjEjUwVQ8ILHIsvoGN3tgnluxm5uFSvwFLm-sje5S_xdEhz3kg_4WU7oxvuLqsZymzPLznFtg8g3x4kcTM6wtPOqW5xQszUzeATOQMZXCH4mCmLl8-rVVsuagb8iRR6NYn4D1_mSBK2dIWM5dM6FVjpz7Dt9KE_ODPkq_FYPq4QKQaQOC2Ju_4-gaz5zk6ZwBdGZEb6madAIlF9BI9K6pnQjRYL___VEVrNfENcyDtTdSfQaEs2V3TPrUSqRg4i4mpE3xZYR9SqvELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=Zg6Yn1HtetrVqLpykGtYPhvOewxNFZXeu8KhJjDEu6zsWXOWuLXT7I9rQYoxYzXTBKc3l1MbjEjUwVQ8ILHIsvoGN3tgnluxm5uFSvwFLm-sje5S_xdEhz3kg_4WU7oxvuLqsZymzPLznFtg8g3x4kcTM6wtPOqW5xQszUzeATOQMZXCH4mCmLl8-rVVsuagb8iRR6NYn4D1_mSBK2dIWM5dM6FVjpz7Dt9KE_ODPkq_FYPq4QKQaQOC2Ju_4-gaz5zk6ZwBdGZEb6madAIlF9BI9K6pnQjRYL___VEVrNfENcyDtTdSfQaEs2V3TPrUSqRg4i4mpE3xZYR9SqvELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJC_YrBt1x-SNDeWfQDvWO-Tc3greqwyhcOPFLwCV518eOOjXD0A0vsBV1PA4TeRHwJyTUUwiydYNQcY2g8cThlZapFhsOTiqFidaS5SOToSCyqySCP7p8sDyMhgbOWrD3NBcXNREo1nwMzPrL27bmMh6jVCTGUYOV1AeWkgKAfF-VhnKAr_gf8Qs0qd8eoPBNezc3pDOoUOFj3qNH5bB1b0wDXOEnBwqXX3YknbN0es2L_l5fEFriS8N7_0UmCrmrQ7nYqQuRMQZjkMNFhr0QX60zQISSI6kXvr6gCjiDTzu0ZgTMsGCSV-0kbVcHOJJ5hHq_YPAwV87O4NZ4uNjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJC_YrBt1x-SNDeWfQDvWO-Tc3greqwyhcOPFLwCV518eOOjXD0A0vsBV1PA4TeRHwJyTUUwiydYNQcY2g8cThlZapFhsOTiqFidaS5SOToSCyqySCP7p8sDyMhgbOWrD3NBcXNREo1nwMzPrL27bmMh6jVCTGUYOV1AeWkgKAfF-VhnKAr_gf8Qs0qd8eoPBNezc3pDOoUOFj3qNH5bB1b0wDXOEnBwqXX3YknbN0es2L_l5fEFriS8N7_0UmCrmrQ7nYqQuRMQZjkMNFhr0QX60zQISSI6kXvr6gCjiDTzu0ZgTMsGCSV-0kbVcHOJJ5hHq_YPAwV87O4NZ4uNjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfWAm1mrfw7SttQdgt0-T1ZQEwN6_9cerwoZOyeEjCE45Z6zv67-vm1NM28JMZRSy970fejy8r2N6VWf4YVfKyrJ548u4wfWACr6YnHhMDinNpBCsnIMVo4NRI4WgYqH7mcGkJPwAnDjJDhqt8QHp8LBuyFC8GKeZlMQX_lQ2h8plmjKAHBgjoo1acLI669_yhWFmEFNkEnR7Dl-u2qUGFUViII6MSawWbXOlcglbYPdtz9PtYCyPvxWUZRU7BzLgWA0uXy0anl41HGNf0Nrt0HtXEakkt8pzoPSGi3uE9dl7ESzvvORgihK4ylnfkMG3cGAa4HZK2i02mbf4EK2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5fz-6fQklZvBzevLDTT4UGT3mDbNktqT0nZt8fiHLtBK6rkD29DslPgvbh-7JivGR4AU4SaKnYnPZk2cUTTQz_8iNKll_SARzR_yPK2vGriy3oZvuDT2JYDKlspn_vze5UGexM2RsPs6UDhbWm3ADFNm-D4I8SKfb4HL5JGksDOujWVxGFhHmzO0iJU7-uvgoEj_BvwZ3qdl0v3M9x-Fz4uUk5-mmQOcuHviGYeEUeinO_r2TKVYjjLjsFRM-AjLmtlKXFVTfMVeKfL35BzRJBv-tiUuQdVFDHQw1Uz4l7tGnyZvfkh-0edaFLHCnhCdLSkgP7I-RvOmzOVLIbhKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=v-j1UkglR9SpLLG9hgVb8WJaCabiT8vPu43p2M2soU5eZ4RkcXenP52AG8l2PI33ArPDWnreZtCEYMFhCKsiCzMjoVUeeKSeSk2igZLeEBmR9BgAh9DYzwr8eoWI4ZssHa4DTtdgtWpZ7JvKO5u8gYeeUXaUxAau4tEaulGPdYjmZlfspN5yfFRDgwQrRhmksE_maXl_LftjGiT9XJ41NAxt5FeaTnQg6ZcB8-hTIPvbpJpKOQtJaoehVfIsLIGP5kYsfKM28sI6AXsNNVAahiiTktMxaPxYlttUpQccaG-OXSjuTbtHjcj8PVYPEeOPsv3gq85-7pXucB0IChOsjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=v-j1UkglR9SpLLG9hgVb8WJaCabiT8vPu43p2M2soU5eZ4RkcXenP52AG8l2PI33ArPDWnreZtCEYMFhCKsiCzMjoVUeeKSeSk2igZLeEBmR9BgAh9DYzwr8eoWI4ZssHa4DTtdgtWpZ7JvKO5u8gYeeUXaUxAau4tEaulGPdYjmZlfspN5yfFRDgwQrRhmksE_maXl_LftjGiT9XJ41NAxt5FeaTnQg6ZcB8-hTIPvbpJpKOQtJaoehVfIsLIGP5kYsfKM28sI6AXsNNVAahiiTktMxaPxYlttUpQccaG-OXSjuTbtHjcj8PVYPEeOPsv3gq85-7pXucB0IChOsjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3nqI1CoaKPrvIRluxE8NTM1ybHGkXBNWRLflIuE6i-rF5h8rwlsWmmmuzppWmVZDVo2V812QX-y-N-X9c2oZPb-ZmBVu3NpdkLLCwH09m6A8QWeCDkRoBU-79nttFgqIT247_Z3Tn05YuXXU7FnKKUjzo5oWUJe_SH-Z4HYxEDjqNn1nzlUI58qGXvA9AmwrvUalwI7i0WBMfwDHkMAQ8P-eO3x3aeNPIuNsyANSTjqHs5ap_tTnintTc0mFHHzBbzhtf9nZL2xX1AMar_3d51M0Kb9I58CXJWir5aCCAzaoNMvePfiFvdNnI8xFVXzLM9uD9lTa9De_6BOShTDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=P1tWtRBKH1gQqiD2mcE3Dn3oXje0Bv1ulO4np1YMjoNiRPdiunAerf5mCiTHyfYCy52wAz6xsWPQiNyazqeMtonwNSbxqF8OA1ios4YK0msdnA787ftgDdFtbJFreCtd1eUG-0HEuD3YW7CsyulG8ylqHW9wYYbUUhZ-Vzj6c6JjPaSXaKxH_AIS_HpWbteOjYIaFVl0D3kK2R8HNoEJ_16_UXP--AKgaHl4cvgOf394rQZXV-BmS_7NmczIy_F_ytYnH_GejzNvVJZQqnRZMO6QL6dPh2wXBXvJx21lxVYMqwrzeX-6SCAT_p2tO37fqjaDdSgKphk4hIEueYi7KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=P1tWtRBKH1gQqiD2mcE3Dn3oXje0Bv1ulO4np1YMjoNiRPdiunAerf5mCiTHyfYCy52wAz6xsWPQiNyazqeMtonwNSbxqF8OA1ios4YK0msdnA787ftgDdFtbJFreCtd1eUG-0HEuD3YW7CsyulG8ylqHW9wYYbUUhZ-Vzj6c6JjPaSXaKxH_AIS_HpWbteOjYIaFVl0D3kK2R8HNoEJ_16_UXP--AKgaHl4cvgOf394rQZXV-BmS_7NmczIy_F_ytYnH_GejzNvVJZQqnRZMO6QL6dPh2wXBXvJx21lxVYMqwrzeX-6SCAT_p2tO37fqjaDdSgKphk4hIEueYi7KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=NROLiBigbIJEqfCoDjmUHGKkiycicqFQh9tyPaFtClT5YRj5J4QXkDMhlvJdO5VNrxaJ71dXMro5_H0sFq9iWmMg_dRF7aEqG0Y1s8vWoPYmH8_i5tqiAnGJnsGtwBVwWXCcgHVdBnkc48CkUgjMYeVcQL9955TdDihLlTxDe1663wszQ4I3lDJgeYhBbf-3GHY2K4IxmJMoqytsq8rXa4R7wiiDhGWZTkMb0gdVkb2szpz_l1F1He9vtOpqO7ujsjODzgCAPWJnrH2w9-CcVNNDBz52fQbQWwjlyWmtUvh_MbgR6c1QSn03ZHtJdbZd1j3cXKmFQ_A8MuQ3tDoQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=NROLiBigbIJEqfCoDjmUHGKkiycicqFQh9tyPaFtClT5YRj5J4QXkDMhlvJdO5VNrxaJ71dXMro5_H0sFq9iWmMg_dRF7aEqG0Y1s8vWoPYmH8_i5tqiAnGJnsGtwBVwWXCcgHVdBnkc48CkUgjMYeVcQL9955TdDihLlTxDe1663wszQ4I3lDJgeYhBbf-3GHY2K4IxmJMoqytsq8rXa4R7wiiDhGWZTkMb0gdVkb2szpz_l1F1He9vtOpqO7ujsjODzgCAPWJnrH2w9-CcVNNDBz52fQbQWwjlyWmtUvh_MbgR6c1QSn03ZHtJdbZd1j3cXKmFQ_A8MuQ3tDoQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=d1m5yW5_ckvSnBghIM7WF-X1CZLtIh-VaZqioVGWVURQOu3AF2afUU_zpTYC6DhA6CE4YKZD2m5_U714e8PHPtXMI7rggiSbOsdIeJeWPpJcqheTKsopRkVwgtkfq9z51t7lre7OzIEbSMUVfJUkTHAOrz-0jR1n8NhhIBcwBkHR5PjV6YdWYF429HzE6GdtnYUaA3MJXtBNW7gfvgaloxONVf9HQWwoYWq-VRruKKu25k02CvDlryErJptcUZQskuieyqWQ4hs47OjLlcrOzME-OOuozx26fRblDoMyUOwdz8f72-GpGGdN9-2xH73GNgZUmc9yidvDhYmqZ3aunw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=d1m5yW5_ckvSnBghIM7WF-X1CZLtIh-VaZqioVGWVURQOu3AF2afUU_zpTYC6DhA6CE4YKZD2m5_U714e8PHPtXMI7rggiSbOsdIeJeWPpJcqheTKsopRkVwgtkfq9z51t7lre7OzIEbSMUVfJUkTHAOrz-0jR1n8NhhIBcwBkHR5PjV6YdWYF429HzE6GdtnYUaA3MJXtBNW7gfvgaloxONVf9HQWwoYWq-VRruKKu25k02CvDlryErJptcUZQskuieyqWQ4hs47OjLlcrOzME-OOuozx26fRblDoMyUOwdz8f72-GpGGdN9-2xH73GNgZUmc9yidvDhYmqZ3aunw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=MAT3syaUO3GbOPMS2V1RGiQt3ud0-6oCAnh_w-0jMaUDFhrRc3RaVYvEQrT1lCHvI-dvUqNZ3-oiCX8dizHkIAL6pFCPpMIWYd4yvfZP30fReDtjvYt3LM0T5SvKfH6yC72KVRHx0W245I_fkEWMKu086NJtBJUJPl-vwgkaN4PsidSgAKzj8wQzuwmmIXh0hxmclh6fhPZjRch4wqVCtgKq5ELCNi7q1WM1u5a6ybd670GDk4HFzNm71plaXSM8tvaPyq8klCR3R8QlhhdEExliHka9PgPu_vuZZD2JisJ2BRTP0X1sKYnbGrkNETFUVwCiptCBv9JbdqFxFDAAow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=MAT3syaUO3GbOPMS2V1RGiQt3ud0-6oCAnh_w-0jMaUDFhrRc3RaVYvEQrT1lCHvI-dvUqNZ3-oiCX8dizHkIAL6pFCPpMIWYd4yvfZP30fReDtjvYt3LM0T5SvKfH6yC72KVRHx0W245I_fkEWMKu086NJtBJUJPl-vwgkaN4PsidSgAKzj8wQzuwmmIXh0hxmclh6fhPZjRch4wqVCtgKq5ELCNi7q1WM1u5a6ybd670GDk4HFzNm71plaXSM8tvaPyq8klCR3R8QlhhdEExliHka9PgPu_vuZZD2JisJ2BRTP0X1sKYnbGrkNETFUVwCiptCBv9JbdqFxFDAAow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnU553jx0Dk-LIFiRRWFKBRw8f94h00agbT0FGJ_q28_IEwjk65xnIJu84AxFHvM_TNv4jfRpRI46NdGI0nhggSChUQhL9s1inAnOTdewZL2rjx6FcwJhcm0jfCCD3TuiFPMxRVOlR-VxcWesasTmlT8ojA0WbMl9F8CDi_DO2_-nrUioNr3ZEgtYWPSp6HRwAjc3m3cP21dYXiOwD9HZqdi-5RC2dnuvJSeEdVva1J3MjGKlSO5vxRjmBOorzMocLUhmvBODoylNX1ebp_V0KiA0KcJy4QIF9dEOPlF2o2UzDU8uCYQ6REfJjgT6Xza1Nz8GnlyM7EXBNvq3cUuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ourr3wtjrVXG5Fs27lDMZaC9GoRvjLOLcMhxCEo6KNFLVxgqQv9I-9MXGAnlfcKlq6V-PJjuySpHbcdhq-vPVCoYeV11RaroRv7xLdowj3L5T9a2zq9D32tdlCXVxxifSKw5tqC7IT3ZDBP8z7iAQP9w1yHO25LD4oIunEmZeurdM2_5I0ORGxgDDgTrELz60oPsuYGsnfBKLFgCKCk7gV_lQoio4QvkDtHq4FVC_MQArXfnxUDnLgNfIsE2uErSOyVjIV_mvb0tyCx2KS3D9lNi0Z_SUYmJDovVUn3P-_X5Ald9SIR64RhRgIskkb2kN0ATHimPQiG4Uzt5kosFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYjweKHuIfTpuJChuSjn44zDYv0cHL4buL6iyRbZC5i4sqvNTnBtOomcsQCrqAExH-Jwqp7hXuWrgYH4ZwrWoPvs864GpDZ9AxlHiI5Mx6l3HvUYtsCFRozsc2UAg7V2hwUgmLMHtOtaZVirwnYIQFvUN_m9B4ABoHvzi63FXA7mxFW2r2ang_2V1Y4OAnUcyL-gp4EdasZtgykcZdAs32IwkC6jOmN54Z9s8Li_yLx3ReFf4KYQdzCvOE2Oek6Gmxo_AG5K7oOFfK-xqsqa7NtHUVySoE-P29RVwrS-N1LdGQIfoDK5OKR4rZDet8R2tm67J2Dv55e22UPdD65MLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kagDR53YQxhNG264zpuWPFu_y0M6-ZFnLjcLUZbq6PdLjQRa6QV3jsDlBEchCq5WdvMawb4ipjyOeZn-cwrjSbaib-afCZvghY5qHQ3CnM9d2LT5wUKI4CtUJD48XmjTNZNItH1U3Rvv253S9repzNtAQBoE07Q19EgzcrbgBPrAapmE1w3Zc56j5FMjCDMo7uvnHHuDAMAbjJvrEX0Yxji9X3siTIN6Y3ZkEnaYmWuVhwB8sXWRISw-zp83Z9Jq8iR16OC1VKPxYbw888IluJ2_DAh63aSd5kkzO9exWXLEDOX8NUEdf-h9O8VVgtR6uxrdhqBW2HyoZsqoLW8gDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sh-G3Fd9ced71Nh_QOE4DTGP8PTJhwEiPzGpX6fPgnMUlFVSZk1ehZGQoS6vahzxF4GsL24Jycexm25zqr0Drt7klAqV69h7wcOcleimhAs4slFOTq5aCyJEmL6GWcbBMur6HZqJjn1dlV76tmiDefTMgJdY5oipLmzgVRaDOlrws1xqOZNInIHMJxHWU0cwZyrOqGGBshhxi2iS6WNQ5h30tMl5Sg4xsfY295bElTpMxAR7OlYxKV6bYn56N6LOOx2fiTYaKzphVAKXJhgFafrbvdBgJxiF_Y9FNYhxLA2Hr7XL2o5kzZp3axNb4SgYvOMyxgPhJud_QA9oCpEX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4Nhlyt_YTwyzPMJFXJfWgYoABvKQLu0cIMS-PoU6pTEhFR7eL_boqmO52Qp-JwD_E5Kzk95WbSblbeH9TPRxAd54pKMpJ85cluvTNcowEXkWDl_oghvZnJWy2ZutrkflCNMPlFcGajIJohxKi0-2ruYGM8XlE2q0f9qJ3oIxM3igEEyYciAcMLmocEFIDh7l_O7-c9PF1qBsRG1D6ZxmF1GLvhmtNsgWpMWl20ug74IkRbfG8DaUA2LGg6IJKH68ZrpESdMU4osx4BrsfoHLgu-6hv3zC7C8MK0E8uQE2BhMA_MRkwaUA5zixhQsmrz4HuAbmBvRmgxibh3IiHA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-wcdmpgWjPk7MbDeesqgaXbiomrqLiXMedvnAOQ90sLox4RxBm9XbRgeTz76MItk-8DsmXFGzUf5y_iL0Hy9zbaHKX3-bhAHjgqVOnoDmXLSEc7uxkiqjI77yuauOVzzVED3sg4_bR4qaNikOQ_9wtGUQDhbiR-ukEMXPZ0XuwpoDaK6obQ5iW1-Ha_7vnIRbHB21tVI8teYbu_J8b-ZXGqto7wsu7oEeyKU8mfWZlcOIWzbSZHG5N-Q7mKwBzJPpna6D_q51oSNPD5Qse-W-O2NEYyhncnmkKHXAD9SDQjW1sKhibDShMML73AmC-LNoc0y97dOUVrlqzRrZ3JWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ahVAqSMcRceqwP5PvHeoy_-m6zIfnTRDfFqnFTloRdJIvmR0ltMahCuityJMdFOOc5Mjl4KFp6HHqKVpV3NUOuvjcFKKKKTwJT839SN1KVwz3wz5J47o8qNliGI51EMqLsatX76PsbspZMQjORG8JX42UGmx1SDYwrUJjyGwpGa7eImRLsuXWL4V9IPUF40YWVKg6c29P45YB0lGP_5cKgh577GcFjaf2QDLZEwhVT7pO9S2wnuuOc7uq09ANHoM30W7gBDrAw_XxSTe6HCaPVXqaycdIu4Li0_VlYTmUS29AaXUklTF1AwDrTXxzHyQQRbyMxP7gfUsXQmIFj71MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=ahVAqSMcRceqwP5PvHeoy_-m6zIfnTRDfFqnFTloRdJIvmR0ltMahCuityJMdFOOc5Mjl4KFp6HHqKVpV3NUOuvjcFKKKKTwJT839SN1KVwz3wz5J47o8qNliGI51EMqLsatX76PsbspZMQjORG8JX42UGmx1SDYwrUJjyGwpGa7eImRLsuXWL4V9IPUF40YWVKg6c29P45YB0lGP_5cKgh577GcFjaf2QDLZEwhVT7pO9S2wnuuOc7uq09ANHoM30W7gBDrAw_XxSTe6HCaPVXqaycdIu4Li0_VlYTmUS29AaXUklTF1AwDrTXxzHyQQRbyMxP7gfUsXQmIFj71MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2tYkV-WI8MItj7WR2Y1ghel8yZOqoMdvlS6rvWZ06K6LUnq1tekadeu-mugSvZnCAxAz8Mt322dheSJTRAGRX8B17IHdIa_PRxsQmLOYb2V1xFUgeTKI-UQ2CqEAuvX-aicf3bZY48xIG7NQkk7NvkUx6wZS7XrCHRCYMjPzPSLYkKQl1F1-YmGVefqp-EXob6RapvLRzfDKy6e_I_KuZ0cliY_kX2KSsLmSastvXZL8AgcFmwnKV4oQ7IlH9l6cBGj84YzM0NWVyA36bjvVI-PAw2IGlD7fcWce0jDQR0_d11-r7FVzywaYkBRPr-sM2M8SFDxu72hcqXk5MUU4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dj668W0RJZjDocqyLgFz1LBKdgTYQdRg8QwSNr1YEA68pMABgDZ06xrV0FCy_2Ddej1oYg2Dgy6NMymlVQLa4xofkr6lTEyQphEQkgVGV3pDneUYKtcTR0Q5Jz0hLGO-fWtypMHfwr4Ct2N2bUOMZ2N18kskqDa0BBzWUCycFXCJAJuc2Mw2j2Wd9r6W82DbgQB7nEK6G2ewF_IDtH-tige6cudoNigUpDbCD0UT7mtk5rLZ1MtylhWtUq8DCdD2NTp0n5tJ07HQFjrfulhlpHODcqxjDdXCQmRFxln9GhBuYprw7yV9E9KkY0DiAgGVZKhdfHbaM_CYL3B74BBa4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NH0zuJe0g-gO05-DTc7o07sI2FqntQY2wkZl1rjETMYHMRO4PDbBkBHXTIcaXsl5woPEtuO9Q6nHUfudWjqoLtyGDwaVkiQcd2y7-8s7JLVvhQvsAXk1kSiKYHmLC8PgKA7d837wuQFvKrQDqMzQjyY-9V_ZXCj35vvuEZ6apA1kRnEj7hCIb1Pp4eL_8UaLTVUD1SnC3bip2PbKisT3MDoO28ZGJBmxhXVOgIqTe2oVsoXGWy3MgUVaP2SHRBvKeaUfRstIujTz7PfdaKguCy4jeNOqQVl0ozwiOJUtmfRhKdyybUyq2bHYXvQ9lTXJG9aLAOsOaMdrFkmTyK-VhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjdUGlyAzAMndZzeKL0QvnqrC5nHtQuQYD9u3PpDGK09FjKAKo3y3cowXJZSpYmYzUPzEA8sjKvT5Tsezid2Idg8Rt-ks8TZQCepv-TY1jiH9yRgym9EUkx3ZCGHdWw9ZVKeADrTRwTIu5yLvl3ercHpjMNtsBdvM5K62-nkYQh5KIkH5Ice3cXnhuHt90fj8bNKidLYQJ9mP-K4mFRLIuaDxZkuNvEng0wWGnA2sbCX8dzPUjVkz8NgSppwEcCLIWa9AiEzFgEuTAef83iqiU__PZmbQbVvGnCxM-CaAkDT0NOIJ472ao6cR-PlULJGjryYGDzNcYJYj8MbVIx1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9d136PrlWc8HZUDlztrrtjc2pwl8BCyh1JsGhiH67A4PWGjx_cX8i7Y67dSnb6RU0KYc1enyoRg1wymq1XxgbCGsGpjNhgzQWUlJKtA-AE_mcNISoq-rsSVsMLwJV80oJ3F8Roj7GD9GBoCFN5EG4GNAPkLjL7d8N6krbKzgVlt95TJ-TRjP-hSlS2d7dmoJZwRM2HFpyWLMETDiE2PiSLtQ8U3mfy_UMNVFZmcU8lvi7pCbGg-3I0ff3sOZTh4KB-U4uqegFYvPgm_MqrbYyK85plPKjyvX988myuGtfbcKXMdSdBAk9yYdpiPXSSz0rEX1DtJ-hvNr1amXfFcOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C30KogQ2qRlWsDgp7xxgiINmX5L7lSXz-tSuUjZGyeqVyKzIyKcfglQ-uAA95bj3hqeOTi6CYVjDPQWDKcRkGJlYG4mNnsYxASWHG8ecY7ZIN_q1fJbSt1djk5oQtvgOIoFRlxPhONRFRaJXVNxnZcdsNyOiPPfH-XcjLiA-q2z9AuOr86A0am4n42tWzsOPkS23N4j9yScnf7hu2iRAP5sW7GDUvS-EZPX09N8kimHlYbF0oGxd4rc9XV2mb4ypqyqJB79UgZ-4VR5NtSlnL8t_R2fDyKD1JpuK7BvwBgXEPTtndhZ7j9GneFDPj2jRTzQVm5_08za0CI8pwksTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmgjraIpy4LQ9cjX4AvLQTNWlsHR9uQU_Ux_cLZLevKOBSq_II6YKF3KbJGtrEtBkAdz0owPbip1eYrInmOqkX3ET2IemRcUAOjjiE3zeiqzuPKxngva0wxNf9emXQYbsVhdg8J0OEHTKBigWPVbB1sJWUbj0OCs5ccCOXYQaw59yB2qPXDe4kBr3Bbgr-OBLJB_AeJq4FVrXEERaScv09TZH6hP-wSYBDNRvv6j1dfx-QOIGHjSAgHg-GRp_Od-V6UqomPA_HyXA0AyakIdeQc-ZikSeq_ayrioYyF1O2gK6nfQHjdPwmhIudd6BEXd2Lvp9ItN0vSv5V-_FEOCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2rIc66EuVRgCJxe7ykJx5y0ulOmdQPBz9A669bLcy0E3OpZkOIp9Yjf1gMLxe5RAGKvnLORwfDXgy3xrKIIGNe1gKKNl0uhKlbem7bAQ8AxHqhSVYbCieBMu_rkcgcueF6NfE9pZISj5vKD81rvv98Rk9fQ1-I8VJi2lPVy4zoGR3TtnewUq5S1EkAZWSAKINtT7m4gaeeZWdcnuBKMyzrF47gaXNRsZ_eAqhHCPDnKIEubZYso1ihISE6YezCJB8jV0wncGfyg_BnDY_FM6Zb6tJXDR36jSuTv9KumM6Mp6ZzVhBd_9Gl66TqGYDNn9Fa9ixA7iGPr9zQY37tw9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=nrtj5EPYdKjddPAw-gB5TkdQagZPA6rBj_HEcB0M1A6UUaMYc-D3wqx_1jeiUp3QTeZArgWnE3enXHy_YvU3wwRFmQaZe_helxQNlD64L20Jymo2mVPBNmdGMxiNS1Ug5TG0RbIE1RMCSMmv5vWQJRvH3sSXwa_E91NDNALw9p0wzs9kQx2NS30lg_JAy6oQJ7EPB22eN7CWk5En-1YZJ9c02RIAaT4dQdppuIgcSyNoVAsJ60p0m6FmwlAj7qNbDgbTLl-CplPq6fcCcXb0JagKjVCcCbvKhAUy01P0QHBga8qYb6TsNUtYSxbfqNkBSgaJDjtVB3IbX5piScvklGfcHkLGtRhGxF86v4mXB2VFYYj8i7KUAy8Qp5KcOslSWgW7MpsRORLs5JfbYTNLTHapYj_DQBl_C1M_jvvIEZ6vw1FF0pFiFRiz1Zg25smKTqGE_Txd7BVdcXsuGOtE7YIq3FFjeHNpTpFrzv9gTl_PcW7Cg0sOGDQrqx3m3wLVRAf1w5Lw7rvL7Ayek9j6ay3tRUk4RFy9OGwNyxGbfu0CSeEvPdu4flSOnT6AdNnVb3zHLlkbMmKrlgAVKOON0EhnwSiXZ8MvAnCoR83wLyROo4ZZq9GdlaY5eOuwyIDeJsA5UC4bCZjFGYuKW7D9jPPf2rL3gRhAX4YGvnxicQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=nrtj5EPYdKjddPAw-gB5TkdQagZPA6rBj_HEcB0M1A6UUaMYc-D3wqx_1jeiUp3QTeZArgWnE3enXHy_YvU3wwRFmQaZe_helxQNlD64L20Jymo2mVPBNmdGMxiNS1Ug5TG0RbIE1RMCSMmv5vWQJRvH3sSXwa_E91NDNALw9p0wzs9kQx2NS30lg_JAy6oQJ7EPB22eN7CWk5En-1YZJ9c02RIAaT4dQdppuIgcSyNoVAsJ60p0m6FmwlAj7qNbDgbTLl-CplPq6fcCcXb0JagKjVCcCbvKhAUy01P0QHBga8qYb6TsNUtYSxbfqNkBSgaJDjtVB3IbX5piScvklGfcHkLGtRhGxF86v4mXB2VFYYj8i7KUAy8Qp5KcOslSWgW7MpsRORLs5JfbYTNLTHapYj_DQBl_C1M_jvvIEZ6vw1FF0pFiFRiz1Zg25smKTqGE_Txd7BVdcXsuGOtE7YIq3FFjeHNpTpFrzv9gTl_PcW7Cg0sOGDQrqx3m3wLVRAf1w5Lw7rvL7Ayek9j6ay3tRUk4RFy9OGwNyxGbfu0CSeEvPdu4flSOnT6AdNnVb3zHLlkbMmKrlgAVKOON0EhnwSiXZ8MvAnCoR83wLyROo4ZZq9GdlaY5eOuwyIDeJsA5UC4bCZjFGYuKW7D9jPPf2rL3gRhAX4YGvnxicQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=bP9G3HjUda0wDN4rrJgQnITRu126dh2yFEJq7aDRaD3tHB481hyq8sJFEC-YJY8gPff3UXOs4T1ImocfXRupSh61--rvSZhXrk4b4fPQdBoFth47zxUyvNB2a38M1EQN-cRCbDna8YhDLxbWh4rTn-e7M8ihqZWWpSnTQR-ELD3RWJlCgDPUvo3o3-LKHDwCLQkVxLFmJBYjF65CuauKohENeAWXLd6-eduCRNfXaTWBYTGHqod91_xPG61pWG4CcCbHCeqKHJJ6hc2xzFffTScEsxBXeiYsEekk9GMFZziwGw2XDQ58y0wp173TwItIyP7vPlrM_-7zXaV5Xf3xyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=bP9G3HjUda0wDN4rrJgQnITRu126dh2yFEJq7aDRaD3tHB481hyq8sJFEC-YJY8gPff3UXOs4T1ImocfXRupSh61--rvSZhXrk4b4fPQdBoFth47zxUyvNB2a38M1EQN-cRCbDna8YhDLxbWh4rTn-e7M8ihqZWWpSnTQR-ELD3RWJlCgDPUvo3o3-LKHDwCLQkVxLFmJBYjF65CuauKohENeAWXLd6-eduCRNfXaTWBYTGHqod91_xPG61pWG4CcCbHCeqKHJJ6hc2xzFffTScEsxBXeiYsEekk9GMFZziwGw2XDQ58y0wp173TwItIyP7vPlrM_-7zXaV5Xf3xyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb2mbbQjYMfOkI4dj0GPBiLnInp5Boo4OR96glMmc6lloD9MhvsxjO9uSmRZlMlkU1Nf1swaqt0-WiHPCeNQZ_mDnB5DNkLN6LChahNgpIFHe3Mn5ZCs4rFp3xBba3-Q4gRH4Zhk07VkOvFCp4pDwXTLdGxv1Aw9BhhRObgJtM06Rxf5lEnW4CH7fgnz8yOeN71eoDBHiXZQjjOBin25KpUJujhmNJ27PHWhrPSYkolZ5qmry3eWSIxmIsXuQ7g5UgWXJHf-Runx9FvuUdqJRP_F10fZDCrNk20SoubxNN8jkHNJq-VhFlRhzAd9dEWycZf0Q_WHWm0kW_LwLxE_ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiUB70GkCDl7a6txG-nskPYq18OKCbluK5ibofPy7hjzRziMfFEZG1cBchhUwosxSkk-ZkwiNp8wX2Hu02R-zmD7CFyqCpOI4KIc8Da_Iy2C8jsJAoniOakgI0Vs7vBfETR2gQqor6WY7ADXhCoMGwOpZd2KnHdrrGyYQFvjOw5LFr-y0_n2ji7BC4427H6H9xrJYqMRUPLR0ZFL_ArhO1vYR0JHNRLq6acsacevYX37e4WrDOmBfnBCrL67VRt08Nn4OJdX1UsBn13Wu9lyaRK7DlzMJNZDacOTpo60gtyPFyvT2xRqzvXdKfD92vPkhEAK70gPTJ5i77Bp1s-gJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
