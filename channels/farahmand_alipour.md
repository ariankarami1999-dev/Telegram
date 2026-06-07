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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 19:37:35</div>
<hr>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH6yrJdGXD9hgPYCMzg8JrSghM6SX5mk0I0iq7ffQmyjln6dBObrTO2icOW0cwxmGi-nx45x0TCzTDc7QGbeA5NYYVM3uuV8mQjl5oX_MV2A1Udo1ejksNGz77HSO5Pq5jQGoxlZC9y8ddiO3aqeUrFBXBa63YFvg2V1zzLZ0Qnf_OLVHOGsTMAV1upVxZwXvQsMonYJ_x3DSDF0F8eQ1Q8seRGHgaWqLaCIYPY7CI3MVNSarxtJPkvBsHG0ptQ4QmBSaoKZZWHLfeebZLQtb3I7TwIBv1NsdVZN41lf9PHQPSne1eQHsBarogJsrIb5dYbBo8OwBmQfiQN5EbqjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8D6xoVzq6om_kzaBAPJOjFiSt6SsLtMo7qEujscJ3E6-ZtICWfKjZ4aSKCGm7XbWBId7elHZwqaYv-DvNsN3XlBbac_IZKL0AOmr-R5NNrab3PEQk0s_nIxuF0TRb54fILxeMeoqAe2EbxUXvLglOJOiygdwvh1ssBLkP0ffzKk5odXzPaDuUj43TtJZOhltLZRoHCqqRu7J4WXNh0RV7lhtD_N3_nYlC8t-0gM_EKBlQaBj71sBNEYFq0_DjxQW3Fc5-f0ubWPzil_d-k2jkapEyixVixI_mysPwM1YN18K6sNORfkKX5G5IlPpYWYZXcTnM5V7V43EZGDGG3EqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucbQr7JsN_P1dZ3G5yxDVBNHcB7tJn5PBy42cO4n1l3zJi876RJ__qCQTAfJBpk16JKmH1D0rPp1JkGorFu9_3a-9_caMnosRrnIF93oY4nI1byQJzhrDIMMP1Hx80kknCCqIESFuHrAmQEEIzmsPYotl0wnA8av94TY5NBE4Chvpxuz903t72ZQbNd5LJ4H-IU9EPvcZjIgcpF2A_7vXGYQ8xNRlirsevsJBEhJTrsWCl7J76NPaea8ZUi4CDyk0TfeBEfF4n_hSIQqEbPQWG_JsEtDMVx_yIXH467FwPIazH53PPeTA40gotqsa_50E8eD8WBPxivkzUCXh8lT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3k8KY8kGJvAP2AAndTAuIcDP096hiOqHTX4vN__zSrCUG0XWofcZCTx22ov7tmWhSiTc-vF74teZiqGYAFjm1a6DQH801ylGKPGAdqcqOaW6wViYyrTtuOfzifaUmsM0RwwoyV8VKlihrrsyyJpm9f2BD31PYqOQpRtWvIrhxh_Lde-QQMSYONGi7tQt-G9FBVZmySHCZcKOLvhHTdUNu3_NZRaLZeH7F7h5Vn6ufiMYQb7fokh-SNt3LlIBCawziVsp_q95a1wCExGQp_ayPotx57smXhxGaLlpPzT5FPSdrZvIbWTaNpDp-SkTt7fdVRt1PMBIh0ZmVKn11t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwsBSRMMsea8Rh-Jk6A36yJIVd2Vh3LgTWw11UH8i3TDitHOnAV7q4iH_7z9w0o2FB1l23z5s9UJCcy1DnMe_JwKFIBhS0IAlMEL2HnSPJSSEIDTTpD41poQ3z9xA4rR7FqE7zH03J3vxG6FsOTiJ_myZtzB5f2tdMZKCX5fLB2z6_84jpBkG7RrMfHoQW55-ajzkvQQdVX4kIkSlpkHTEY41Zy0yN9AFJbRo_WSGsim13CLiwBJhh8DrtrGjellCD6HETb9tuIdrzSPDD-YBRrN_OUV_huG0ScsuRwh2aMU1kOBD4qovMYzuEVwyEqkcXYtAwi1LWvSCxuJ28ilKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Rb7vOKXYANEkdTdXUwNbKtOg-yTW5f-WxScQdtnNehTCQts1OMRXGiJHXuN-NvzLsoAbMuXaSRGF2nBuc93ChBu9zXRTZNqoy9ZTksUAp7KyDRfB5kjDi92z5gNuHB-5h2tBtgdb-8q2hY1A69K2-ted5wmOLhZR4FTjAn_Apr9ozSJgTRLFO4DCAeHIZuf-kpTCp20N5L36G6wCxcgJbJ5dPD_as9diM04QqAyF-4_kET89Au41qQdY5JLTuu8O8Y4Of5rUkaAMBm3J1fgTxJXIUHQTBPYVoLOwQYpZTJzsvYV1E7jkuKx4VW3oGDfVlPx9bbXLAOkv9_s6AgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT1HP5i73BrF0rHXYPbRhvCwCCumQYuZRCouCsjRwTE9oUYOTje-d1Nb794nIcCKWPaAj4PhYi9gVXG3AIMTc1TsZGuT-riYOZzYUog_eFH7PFDGByqQ6Pa4yw3lXxRyRqcgybU76tjAg42P-Y4-fnprQ3YCQ-B_FGviFtb_lYluBuR6tiIBNEvZN-ibKDp8uzwXGaLiE1lrbsQAgA1QscyzS3GUQU7_KKaKnF9JLoXSLihkp61V-MIGMzmvb-Rpa-vNBSjkeN3Qn55zeXy9xC9NN0PtCRlvfEQHH4KlXGQLJ6G-ySbJRXUEQke_4hT5MWCsHnbPocMsy82x3kun3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIHLbjKs0ssRziTkRTyQVS9g4bfVEU7EgdxfAge9Tw3ccVZDVxII0qKxt7HCr3564hrH3kjngdih8mthqx2pwg8Kid-SDxLzYIQRrSzjeepzXdSlWhCVG6wDawT_IaMVdjRECSWoDOWxSyhlPe5nfjgRsBN16SlsABMXpC-aE0qrP1DbcPsHw4VuV_WrHnzlNsH_DredIKg2sBuu63wzZScz6CxhFQbap-HevmzEh9c9XGYcu-Yyk956cE6sI3vWu6a6coh_nh7iVE7oflRnovPOLfRcV4QGBYFy_dBe6X94c2QrEuRH9cWHTKewMQj1esQd-4qAm4UVKpIYV9c17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc9qTT9iwE9OJXleQEMWUtY1qGHNtmCLOcWYPRHcsYRu7u6r9zaFQ-G3-9m78YIDR7mhZ-zySI7UjkXz3a_N0UnsS6TIpMV2CXfQ9t8JHSU2ECFyXGad95KzuceoFbW9SjOd_hKUq2oAnQd7ABPsMVckLpPDUnCJI0R3Ym0lkRTm6ogj2rGHyO3sTBX1OOdYuGbY_Nu-SmMrSFABC-Li93cJ9ceecqg71gVmxkacUgC6AHgmMvVLT1EmyIXY73QkjpHol-PMMpwbNh58dBLC_nm9NkySo77YQt9TEGTd0h0HeJqfIznBHia001WN1rktoWu49TIxexstxvYXbNPd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2-CH53y7F_vB2Ipzbb-_kx-yUx90nTzaAgkj_mPOg7jpzZuVr5JNg6oI7fYN6NX797OgnnFVK51IRE2uLLXzljI5DPojkO2SGrpuQTp_Md6fXhzm-ODV519YHFmM0ygZ3qV6ZG_yXjh1CZ0w0kFk79O_XwdXBdNvrys-8vmgclYHkvLQEH8PWTlDiHxpuEoxyFbrcZmgV05zkv6RLcSXkQFkXMB4zEd93XCZdqprGSy4FXpYZdt5-VStEJLxG9KBQYPt3ahG1Hr-nmJG10TiyUX53mXct2GYmnTO2iTcGokTPAyE78nfhbgQfXr5Ff0MjuOifpzMmn3Y0mxJuF1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4QEcS3xjni5SEku-2iaq67tOSDaTgNo-Ih2OM8i-rVly9gCm05hn_Vr6aYB9BE2htzUZgkwYwNSg4B_m6ZSZzeDzeCiMoP-pNt55EJSqG1L4MIbw7YeTqhXkw6iSI1pQpthOm8fM2yVoWZR_R6_AuvSAbaoDfGBseT8g1taGppzjPntwFgIL4pSh7XVj-sNkKoFPEgcyO_tp6qg2f39m_RBCe4zBoGck2yINP9Q7oq4rWSHuTE3loI4q4wtcdwEfVSSrdalq2iU6N-cwihbt9zz7Yx9lQ3iGaOHzu3htNbCz6Ne3QNJueCDOT9fH_XylwIe6KwQXNe2J7PGPP562A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=EPjMA6yHVd3aKreada0HI87dnW2IrHl_zGauMhPAysYpWw6xdh_pynFAlmFBuSClG8qWaBdnh3y6BsF8Lkc5Pk491OBojbQBuWtf6_N8OApkHUtCZxqSROePP5lPPc61tq9yT-Cm09G6qhBHukGAK-36LKdz8RNw752dcRaY6yjM_e_ksoUKP442DEArjU4FWnxFNz6Ed0at3xgk7EjBMPSAOA-1QLDLzTs1sxv2bg-jar5k31iuZ98zIN-rG0hwHnyAtAeB962cMpQJrMi4wfPq5bOS83pXd6E1Y7qJecmIBd2Nx28iCtScxJQBnp_4HGGJLR1Io1zQ1tpOFjOLEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=EPjMA6yHVd3aKreada0HI87dnW2IrHl_zGauMhPAysYpWw6xdh_pynFAlmFBuSClG8qWaBdnh3y6BsF8Lkc5Pk491OBojbQBuWtf6_N8OApkHUtCZxqSROePP5lPPc61tq9yT-Cm09G6qhBHukGAK-36LKdz8RNw752dcRaY6yjM_e_ksoUKP442DEArjU4FWnxFNz6Ed0at3xgk7EjBMPSAOA-1QLDLzTs1sxv2bg-jar5k31iuZ98zIN-rG0hwHnyAtAeB962cMpQJrMi4wfPq5bOS83pXd6E1Y7qJecmIBd2Nx28iCtScxJQBnp_4HGGJLR1Io1zQ1tpOFjOLEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBVfIULZOIfx4AP_oTjhQwzDdG6_zIC71Mxwen2igIMqEdp4mAPkmUkvSN4q6P_VXh-t-B6nWy3LKSf-tLmWhE0VKWqg9dDHcv6x5jkvJnCo64NBD88pYIj80vVDwtSb2z8fvNNdEonAMOoA0xg7Et_AM9RbjM1SSXDuB_ty80Z8xutV0Y23mGzQImhRn0kL_FVYqWlLVyHB2UFHTSsAk4S3WtsBe4hfxDjW1D6WlORLcQEl6o5St9SHzs0tNtNTFbWVtO1oZa5Cb09kEkcGHvgxzxFwoeyGJwAOSVbETSXWPvyRM1UhYOGfodOHpOzS9lezsgv1Utwmh6cUpGF2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPZ-Ae_e7BxP4fZ-IGjUY6pm83wPtVF-48HLTiOx5G-12Kd4PYz7AgVWiPo6dyXrYYBzTgLDxq8CjqVRbmdg96sOovZWHW5fIeH1vEorRBMbcj-3aNw7QCIFE0qRF3TzKF94nKBy70GkXCyQ432aPcPtR464_yW_e5ADAPCu7Q2E-1nY3wT9rygVKw2ATJb72A2jiFXih6v7BO_c6Lm34GN04kfLuI8Cj-moky0YPzoDZtmER985-agPOCl37feHvZ9lI6GabPm4my3nO6BagU-8IROK-M3964wrbF5tqfsdkcwF-VubIO95hawqPjQP8jchhlegG6sf3xB_K4Pblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZhR3O7v_RQ9zKgihwm4sogIqmFVNp2QI0c_OscIWwCK0cd50eqDSvChwe_mW20kheUyyL6A4pkxYt4S4DaFTX12cGDGLDYSXUxPTnR3AEOnqUo8IVxF4NkVeMP9NBpTDtM9GMQ5xSUmiyAD8lkGPJGd0jn_6bhWiaLyVzSZb3bCfAlI6HH-utVIfd-UL-QYFuzN45ifEx0MgxyRrZ5wKZydRhnAmQL-s0j1bxhOdH2_JqK8SbmvOAsj4GDkqE4hczwgIJ04OG6_6pFbVInGBB7LyijJecNvsKCf5h3UnXXBOvaR_1TLxu-ZyjF0LT9E2ToLP00pcgfN-2o8aI3Y5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pgq3JuLphxKIpF5rNcaT02SmRKnpKDbbvl6vItTNVexWmmkf_p47agpoDxliUoE3HlJQcnS31WmQVjJDfiz93cuGYTCw6WQp8X2bGWwyPeE80ryhPgNokjTsLhANvQIUIV3ach36XNIy6DQcL-s2SaVRcXegQMJDA3O9fxb7Ppb7ikkcdo1AubM04OWlj1Mubhx98sNXK1nbkFyu24q1wl3mDH7pMxM-uQP2pIhOB1XJEkxvTOlVZ0X4qBVPp1otOYmB0UNbZfbDNgKr8-JgkxezYHhnUxxAC0oKpAdwJNQF8__HLEeCHhe373iRRGi2ntcSheLdDQMHwnVV4_O1nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=NWgi386g97g2XQhFRZUfP7-GJvpEtXoiaJcMNRq2y6guHay1JZHmG6dkHOXVZjAANsNGN_FlSE8kY6Gijrf6ULwFbjW8AHLLDRHugw9Z3j5MifCho44kd1xa8OR09RinC8SW4emz_TruDrN7-JwiAKBpe1LmPXY6P40Z_2DIyq72yuTqn_eiaoJ2XXJusjH6lYQ1RnCMp0zC573_OMZFEb0XaoWTwqxTzrF1zTrx7FcCqdoIu8WJYwYyh8ttEmj2awrFWOmqkjAV19G0GoJ8q3L-NYBdDQsbEpgZGR8ENCmcEHvqeBaCTWzRTeaqF9K6bblYdZG7rMp71uzJrGZdkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=NWgi386g97g2XQhFRZUfP7-GJvpEtXoiaJcMNRq2y6guHay1JZHmG6dkHOXVZjAANsNGN_FlSE8kY6Gijrf6ULwFbjW8AHLLDRHugw9Z3j5MifCho44kd1xa8OR09RinC8SW4emz_TruDrN7-JwiAKBpe1LmPXY6P40Z_2DIyq72yuTqn_eiaoJ2XXJusjH6lYQ1RnCMp0zC573_OMZFEb0XaoWTwqxTzrF1zTrx7FcCqdoIu8WJYwYyh8ttEmj2awrFWOmqkjAV19G0GoJ8q3L-NYBdDQsbEpgZGR8ENCmcEHvqeBaCTWzRTeaqF9K6bblYdZG7rMp71uzJrGZdkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1_l5LEcdRo-MJaQQDSVflFFey3eP0_MZBp7TEzy5fKjw4-TLNjdCEuLwwunvAMtmqfsLgWAsJo5pqYLIvtM1Zhd-e6GmQHkhF0f5QKrEwa8CRRI4V_CONZOSlRu0EB6m9gUnn50tYTP1x7Gl5TZeyBDU-rvCpAOJ3Bi6AjOQj9JTWIt23ON6gQZKi13ZUM3xhECuoAxm7KSWxZySrAWaWX5LYS_WXePece0eSyyod3u3Oe42fYP5rn5mqAtsoIeDawYxw0Eo03Pt_7JSkbG1gCNFKTrDfSxFbzx7hTYHHNCEqE2SH0rqASWdNaJO31-2YdgFZQ9WpS5cpPYV0lpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=VoEGR1-hG6EstDHQqcDTGgJIGmgYwkLsaTZmD-L7FvBJ2RPcyWggA1YRL-Q444EjE0L5qzPUdm1VNviFdl-fS2GvPfVB_3wR-k3szzWYKLoH-XMCA0tx8SbsRo89WiBWuG5EwGzMHaEgFiYjfMzKz5Ok0vB64vJ3SKSQBWXqF9wUmqTDh01GF0TgnQVe4K5rR839is0OZHEEw8tHlqjIMlsEUkHQW8_7i01465ELBPCsMBDnInB7BxrwYplic_ngvcucUIe79elBPnAICGefGjh7w-n2dHp4fzpIpRI36bk7ij1SU6AmsCgvGaRYBW5euBNEGf2vxCU7Zne4wPSajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=VoEGR1-hG6EstDHQqcDTGgJIGmgYwkLsaTZmD-L7FvBJ2RPcyWggA1YRL-Q444EjE0L5qzPUdm1VNviFdl-fS2GvPfVB_3wR-k3szzWYKLoH-XMCA0tx8SbsRo89WiBWuG5EwGzMHaEgFiYjfMzKz5Ok0vB64vJ3SKSQBWXqF9wUmqTDh01GF0TgnQVe4K5rR839is0OZHEEw8tHlqjIMlsEUkHQW8_7i01465ELBPCsMBDnInB7BxrwYplic_ngvcucUIe79elBPnAICGefGjh7w-n2dHp4fzpIpRI36bk7ij1SU6AmsCgvGaRYBW5euBNEGf2vxCU7Zne4wPSajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPpYD5Sq44s3NAGHH_-0nkFzBrpcXzwMOqj940uVadJLiMWu8Fyq13-7SoLGxaRTjmMilLlNMfJam9vWzjuwrVhpF5O1FO2FZOp9uVPN5_7PkTJGOxoS_TkDSezlGZqTJGL1TmucXLuAC05hntl1noiNtb8c45wU5t2qOcK6AmBJxaYnW5C-X4hHAI9jToV5Z8S1JpBkrpbWeQgX15D5kmHY4i_9iowkCHIFvWJtfPrM-zlywL-tuiBKIrMrLsbx54TVhA0_pNULNkNsTg1301_eRQ0Y1TBLhl_D5jyfSIftVzo-ig226p99YeMlrljy6ytdK8c7koioeeCn5n-Thw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCsR5lpX_YyMzTU-HbUoO-Zqfe95nsb2BkBLIaGy5S2vgBW9_IGIx_e89nWXaxlua6O_g1xG2gEArG4I4AEsM6psZWrWCYOghZ8EjtTEDjoeXqj5c9TX0pGhvXnvGRdmPrXNqh8HPnKDmRem_Q7bCcNJQFG4BPjrY9tcKmL24kQTdJ6MoDdY6AmivlMcWmuXuHN8I4NboCwC9S0OOLC_L0LgtrtJQFvwJGfFRaHqw3LUsj2imukMuX4T8u44fPh_npCsViRdXFwueF0_C5Bv7BpgZg2kUUjXqRbP8n_zutjiQ0Fr22rQZAAUsKi5hAfIXK0yn83VWQ-EVWBbB206_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=QQEWdLyY6iecNLksFlZwh9fpB4wYv9pN7Yx6xvpio7B0HgmfVMETSYfg1ahCR4M8OUgNyCZe5Lu5X2yFagXgyAu2QnBL60ehc7q_MRFof7JjLbli3gybOLSU24c3mnQ5afaeU3B4lErue_eIWNQt7jLWYu1TYVMiBMwGZUg5b7mbSrR3fyWZIufXAk4oqx3JW7ER09Qv2_TLKLA005UqQ1ECy1Ggg44-0rrzUJQdkZAA8NO15IbEul5CZ4BUaUVu2hEXknyMjKEzedUYjCzyY4_KerkqmyqLuDtQWyJbe44HvzJincQl3TRGnG6b0oF7ZrOWn_KbZkYqAAP5M7qdxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=QQEWdLyY6iecNLksFlZwh9fpB4wYv9pN7Yx6xvpio7B0HgmfVMETSYfg1ahCR4M8OUgNyCZe5Lu5X2yFagXgyAu2QnBL60ehc7q_MRFof7JjLbli3gybOLSU24c3mnQ5afaeU3B4lErue_eIWNQt7jLWYu1TYVMiBMwGZUg5b7mbSrR3fyWZIufXAk4oqx3JW7ER09Qv2_TLKLA005UqQ1ECy1Ggg44-0rrzUJQdkZAA8NO15IbEul5CZ4BUaUVu2hEXknyMjKEzedUYjCzyY4_KerkqmyqLuDtQWyJbe44HvzJincQl3TRGnG6b0oF7ZrOWn_KbZkYqAAP5M7qdxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIIMsWzhuqS_QnC5HpawmAEN4_6dxkFtTSyjIrVDz52YNPKRr4e_Pk0rCW-9osWezfJIUVgZjp3r-6_xItqwgipKZTcYdpnNguJ0AH0rZKr5-vpyBCSudT_hp3IdZbinkaZ0HfmIWWs7gCK1ISv9J5oekDPKWDo34kGUZ7FoHjJX8gxYcf0EhcREPTkCnoRpiCAECPlKpmyG97PuxOPoxCyEOuNyzZFYY6zt3Row9XjV034NRFXCrECtAtr4wT1cnd915YsN-Q5rDrYU4gx4CmRt7Bf27uJuRk9-LFNHgaIYK75Y47ZspP6yLNZwlbBxhWIDjaIa8RYdi6C0ZxBKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=lZdDDiza5PExS_DJCZL5KnRsU2DJ7e709XPvN-vGEDWVvCE_IECDmQtK0cWgd9wtt11aj9WHXbyy-VaKfz2kOOBMqCAtzxJk7z9d6dXpn-NmI5Mts1sv-FYXi2y5nIIt1_lPj49mK0FGFpPcMr8kA3iS9D6mKj4l2_aoPJB4AblMaDCT0Ti5PSGV95TdHHFCZ0SvzOOiMz_qztpmN2Tu3Wyg6P2btiS1EathDCFzQPUpVebD7OfSWW9Jb7Lb3YZR0VK9eCIRgwpMCwoLFQIQVTnouV7zK07Bl0ipKHKLRuiFeT-LnegLb01evwAQhD_OWeRc11-QZEmV6cPpbogbcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=lZdDDiza5PExS_DJCZL5KnRsU2DJ7e709XPvN-vGEDWVvCE_IECDmQtK0cWgd9wtt11aj9WHXbyy-VaKfz2kOOBMqCAtzxJk7z9d6dXpn-NmI5Mts1sv-FYXi2y5nIIt1_lPj49mK0FGFpPcMr8kA3iS9D6mKj4l2_aoPJB4AblMaDCT0Ti5PSGV95TdHHFCZ0SvzOOiMz_qztpmN2Tu3Wyg6P2btiS1EathDCFzQPUpVebD7OfSWW9Jb7Lb3YZR0VK9eCIRgwpMCwoLFQIQVTnouV7zK07Bl0ipKHKLRuiFeT-LnegLb01evwAQhD_OWeRc11-QZEmV6cPpbogbcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eyc6kr8RZ96t4UbjJEPW14vnWyrXDRXjm8sQsg6cnpwukdG8MobME0mm8OwXSxZ7_3ZGB8enb92dW27VTweoF5lOjFd9LZsSM5ASaMvrfGNCaQhIWxCEau_7SFZ4O0fCBLS2eCs2YHIVynXWM15GbUtZQlGLsHnboZ-sjueKNkeWteTH2VwpcChViRSDKi7LA2ZaJ3m4ttS2j0z4iX1zadtPSoqrIpvsmvPsvrKHcCXzRCQ7uneG2WjHZRVXoAax5VdEmMoUwpRuqmmjuL0RvS52kbjwX5q_VXIRPbLj4t3fPdUcS_2YsJMGng6o9bGjJmS0iRYnPPNwzcr06R0i_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3LIXBJJgS-qGPJu_LOuJgpKtOZqNY7I4gcioWDsik1BWojpv0UPUMT7HBmu0Txh5mJ0hSH8IitLyLAm0j-lSEuNKhyuEmzIzQDoF6DnuziotKMIIn2VMfMwcgrCqt5GAai1tQ8-2FdqvLJCi89rt_dyzwcIKm7a4lI3z2ysIjHgqj7d1PzAZQJlQv-g8mXYqICh52itkS4ltpmYVtssRIeRK2TJdwpxctzMAHcGETxNzvfhVUaVl21WAy9QfXN3gd2vP4Z4sSWESIs7zJ2OJSTIwl1ju7gIX4Ybl9HvW1eD3TrV-7NRYQ-2IggViztOy7kvqppumi8vZRppjnam5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmcSKUr6yllWUkhH5lYmKM04PUAI-BUXYP8aL7oQvhJ1soikh8MM6vZSBDSoZzBb_c6kCuSWxgpNpYwHglwVl4WqeIWFBSG1-bnaJQYs5PflmTLJqDmtnrnQd4QUb3UoDfRzyycIQbfhzIUQrne5UT6Zm_Gx16CRD1YRJ3ZvdNc-8Ab0Tdie0AwHbfDqVqObvWwGJQshm9Tr1NcezepDEfCgy5RCJdYIzR1oahbwzz7Mb_x_OcT_BMZHixE7-NbyMFzYMX34_ZpDsu9xYj_kplwcUjgRcxvZ5yEyVWGQsMi9swt7zF0jVXG_erjTpl3KtXFVYSegtAUgZ8iYB0u3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=qicbFsICMdO7H3FGQQlcGWHppi3mgylHfeptWi8VTwh1n_2yc2drUF_6Umb6x0ZOsSOCJzJ8ObJKdxrKPGot5JXwjwyLeniTyLIzdf0eUUrLuKSKGmmI8q63ehywv23PSAMHRIJeoy1lcwt-0zqH9ubkjsgRzVUQi1KTtx6HduGSuw8y_Cv-cs2ve6uW2_1S1pVKml2E9UfDREE2v5uL0mrtjtq4z_34xrE5nAce6v9ZhAI3QM2w49UvSbbMb5NSg_PvVm1jJfAFnvhK2TWjBGK3zKgOUDxFX6yXVQN9Xk-aYEL1Q43DZGeKNnEXNNls2Gq_RS6H5H5wN3dZJFK9lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=qicbFsICMdO7H3FGQQlcGWHppi3mgylHfeptWi8VTwh1n_2yc2drUF_6Umb6x0ZOsSOCJzJ8ObJKdxrKPGot5JXwjwyLeniTyLIzdf0eUUrLuKSKGmmI8q63ehywv23PSAMHRIJeoy1lcwt-0zqH9ubkjsgRzVUQi1KTtx6HduGSuw8y_Cv-cs2ve6uW2_1S1pVKml2E9UfDREE2v5uL0mrtjtq4z_34xrE5nAce6v9ZhAI3QM2w49UvSbbMb5NSg_PvVm1jJfAFnvhK2TWjBGK3zKgOUDxFX6yXVQN9Xk-aYEL1Q43DZGeKNnEXNNls2Gq_RS6H5H5wN3dZJFK9lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=lxB5lDbFIMFO-05usi4cjyrp1-HQM0rRca9RNe8X-zKIrh_aSGRSTa-lVux_8D2LLqfZdfft2KiGKZmT9MlZCKWp6j0Nl5ckGk1zqo23xyLo6pp7c48f_CGvKcj6syNQ3zMzZIasBvaQAgdgscMQkboIvh4MLQiP_sMZGubbh9FFJS6oX6lwJOYB0oIPKb3e5dz9bAH4nh-uYWl0Fmc7mmB2UCU0qgXV3Ploudh5Ou0qGnGDj7HCrg3Ru4Vfu4YeRvDTjl-VUjEWykOixo-HybTEHBFDrN3_EsxEDtFUjZmKG3dfSMAKWOkjAQ4qOeUHJ4jVgltEMXBK5rX1s_zltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=lxB5lDbFIMFO-05usi4cjyrp1-HQM0rRca9RNe8X-zKIrh_aSGRSTa-lVux_8D2LLqfZdfft2KiGKZmT9MlZCKWp6j0Nl5ckGk1zqo23xyLo6pp7c48f_CGvKcj6syNQ3zMzZIasBvaQAgdgscMQkboIvh4MLQiP_sMZGubbh9FFJS6oX6lwJOYB0oIPKb3e5dz9bAH4nh-uYWl0Fmc7mmB2UCU0qgXV3Ploudh5Ou0qGnGDj7HCrg3Ru4Vfu4YeRvDTjl-VUjEWykOixo-HybTEHBFDrN3_EsxEDtFUjZmKG3dfSMAKWOkjAQ4qOeUHJ4jVgltEMXBK5rX1s_zltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=EGTFFhvvKM2ErlXsNgVfpNhboo8hv2RRem_dELY0yYiDpNdet3zD0QydstYrdXS7OL0ISx73XKEe5-KqZKyzlc8WoEgVErgEToERklnFPSslGZXddEEs0TVLcnxbqNTUsajdCWbsCXgWNUS-zBgiTveonfkAhJFO4lmAUXBNFU3ROGdqZlBRyhUS_vlICXvutcv3-FsEoBEbvPG3xXBjPKmD1PMCXT3fpreKFHNcL3TL-0Kupw77WVmsPv1p-zLJ-ASuHqzTqmdiau2X3-5sdDw8zMLB19msVOPNqOZwdGmJIBzjC5LYV-LDFUeFayiDjOwbu9XFMOpRcICj7wlqLTDSgL22Bz4AIJgxvsPlMevHTEJm6IfDq4A6kbrefnTOV1Ys51SZCmphcANSDzjiYRt1J4NBiwtplrJhVuzaefQ-_3OuE9qara66I5Zy-7LH_0mNUkKG0V2-V_mbMXQ7cEEJMnxmyWqPW_f0Pl-dSGSWul3IBKFOOw0BlXylGc6NEUmfy-0tO2CWPQ9ZeNV00ogPtwZFmu8MGzZTi7sKKH2LYLzYHjrjacaWGi-u7xrAfrqBAnfrRLWtt5L-EpL8EYiNbgD5cFVVvIlPLWjKg-vCXDhnnKwavqMZHYB_RSh8lTzv37QbrpW-8pKUQyx-jEAGNdRYF_JTaKFH-0nMoYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=EGTFFhvvKM2ErlXsNgVfpNhboo8hv2RRem_dELY0yYiDpNdet3zD0QydstYrdXS7OL0ISx73XKEe5-KqZKyzlc8WoEgVErgEToERklnFPSslGZXddEEs0TVLcnxbqNTUsajdCWbsCXgWNUS-zBgiTveonfkAhJFO4lmAUXBNFU3ROGdqZlBRyhUS_vlICXvutcv3-FsEoBEbvPG3xXBjPKmD1PMCXT3fpreKFHNcL3TL-0Kupw77WVmsPv1p-zLJ-ASuHqzTqmdiau2X3-5sdDw8zMLB19msVOPNqOZwdGmJIBzjC5LYV-LDFUeFayiDjOwbu9XFMOpRcICj7wlqLTDSgL22Bz4AIJgxvsPlMevHTEJm6IfDq4A6kbrefnTOV1Ys51SZCmphcANSDzjiYRt1J4NBiwtplrJhVuzaefQ-_3OuE9qara66I5Zy-7LH_0mNUkKG0V2-V_mbMXQ7cEEJMnxmyWqPW_f0Pl-dSGSWul3IBKFOOw0BlXylGc6NEUmfy-0tO2CWPQ9ZeNV00ogPtwZFmu8MGzZTi7sKKH2LYLzYHjrjacaWGi-u7xrAfrqBAnfrRLWtt5L-EpL8EYiNbgD5cFVVvIlPLWjKg-vCXDhnnKwavqMZHYB_RSh8lTzv37QbrpW-8pKUQyx-jEAGNdRYF_JTaKFH-0nMoYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8XyHoHSjkW8TlfPBl4cScbHe2aGaqDi69cZrIyk_YwZsS6WtGiguyK-la8nFSRmrNW76dWoyM-8Vo1jMQHyKUtvo4VnrRkavqJwYk2gA0GD9XpUUqPPuVf4AfkhFK-9pFg2aj_tOlrJ6cUnqqUA4o5_W2szVbxRQxig_lT2gy5pXWBPvKycPLbqo5kpdFhyKJwZl9Tp-0erUDDzB7IHLtAevsH0XzuOHc6hdpoLbLjvBXdRiz9ZoVjUR0Czv-B_vriKidSNzMU-nZmwwjPdl7qF7VR6OdFGYFxMAGZwT2_0sDppnEsERDkyM3so6ZyLHRm8_ssmUeCNjkjL7bGsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-W08I2nbeFXOpTZ0cjb871hZQkWVTZYk9UAu3mcwD8e1CatCpWXGlbVtM6bqPhdilS92XkUWgwaPmGkX1faHVFhxFt1w-J7ORawAwdNn29OyWIIs1AcR4Wo3hKCrM4uUB_4rAm3xBk-E5AqALgFcxyLUzSANkScio9vryJoHN_OWDILjwcnGodzcsLxqLHCFGaY5LPnmTcCKejjU3yriqHoAgknltYTyuhTqZNVhJeWOzB0Tp3uP7S4IBEkpeBSim_Gf1Dm4SY0k1NpZwEsZG0JqvqIk1KeJe7dzgK8xctKe-9132wtxWc5ke-jj6tv1pel2ox_mngsfgCs4V6xpUnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-W08I2nbeFXOpTZ0cjb871hZQkWVTZYk9UAu3mcwD8e1CatCpWXGlbVtM6bqPhdilS92XkUWgwaPmGkX1faHVFhxFt1w-J7ORawAwdNn29OyWIIs1AcR4Wo3hKCrM4uUB_4rAm3xBk-E5AqALgFcxyLUzSANkScio9vryJoHN_OWDILjwcnGodzcsLxqLHCFGaY5LPnmTcCKejjU3yriqHoAgknltYTyuhTqZNVhJeWOzB0Tp3uP7S4IBEkpeBSim_Gf1Dm4SY0k1NpZwEsZG0JqvqIk1KeJe7dzgK8xctKe-9132wtxWc5ke-jj6tv1pel2ox_mngsfgCs4V6xpUnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRYiTHPsG9vNAThKw4JTzi-F-_ZFptf-gJVJOSTqmBXfMJ46YXLA3pj99GN3sCLUBdPbzNcjGwwX7DXny-EqgagUO2-agrl8mxZuakd8W0vKCI7GELyQKIIjSFLXObB5GH9_Kw-S-MwGmhxrxE7PQ03y3q9kLloD6kVc9Qmk8z4gRDlKtw1V1z5Mnjha-dxUXGZSzUjtJbk2iqSkszQK7fpzF9-cSpTrhoFzaNhITLF9BsT2CiYcbdyWOd_yMzkOPYIOSpG6qbysOxCDQTAhrmXUPHhoNkfQWkI2j9MtLEpNoz5OiWYRWb1CBqvqHVCbid7nmi-vMb2p_kFLC2qu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnBkcH-wZEAO5390wwaB7Zr1YTLG0PzIxQxZPE-3kxNhfOknAQ2aziVOZ8lYdO5_OiEd0YGqDAw2KaACAFPw9wYdn0sJp38jkUyhEiqVJNYc1W9a2nY1Z57-852-wR1RLAzd0z2F_aJFW9in_dwjFw04bCeB-hj7VdT2XHIyNki_INY9UXvpQZjJZypo1ubW0CBXZu3fxNUN9voUb_rNA8QoqftYBcAFutrg-KH1vRC2PJNZ2jXOMEeBh6SKRU7bx6JzT5AySDtCpXNZ6pcCCqj1nr7lbLfUTuAh98tJ8pJtGQ-RpJ-edHIEjoLceUVg9IpsUKOT62jW8QoDbSvUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO7C6AP6bY3RJCe6NTjGrGxB5HVBdhbUHL50CSGJhtwgplFadffpPf789fOYLOl6R80PpYIHktaqxcPsnXFbMt0bosrzcpLAptCknaNoF3LeowzTJSR3qNdmRVa3elA8Op02nbCKVuqdJnG1pzvBj7CzQcnnqDo-NOWEWcjIyuwIfwX1V5Vklcqu5c4vc50XRdhSzw35MV2WntTvemWKE-xI79L1rOiYGJ83Q2T8v9m-4T8a6vbLkzWBOLg0gxFtE8DQHMenTPTna6O1C-4wPwwIzHA3dV0I2aZR4V6V3oEWs4-2P0pAGx75OS08M4CJsyFRoY-70SwpbK6oFVpnkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7taBqpdSbTakC37cRqfhaH-MOc4rs96cwoZmg4dy9KUCo5_BKquPTkIGqNKJ2ofJroF3uY8lyAO1nIAsV1fs8fC9AMEgNv_kib9RZ5kKt9yzxykxK-c-c_b-n2a6Aua80d9zZzVH9QeYEXD2dvPC2nb8751jvOekCFVW90wZE05-Ye9WiLlsn_QsvuMAkhO46yv70_quBY7L2BQQeXRH7Vm7TSwdhoy4_RsbzvigGxZjsvPUu_BRn1cu4YOi1EUqO_yG5cLQoJG6HDz1K79-xQbqgZ1glK7tBunNnGCVhV98zkEFyXo9-lAp5wuxRaJ9x8RpK2_Kbey7xkKQwHusQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwXMP5sc2KfAHjGsIBBUxsLtfT8rWO4XKkZfUdb0g3i3sqxNUfOtfLOVSu04ZFliYwvtapLKjAf1bOq9viCOJWzoHUTNz7gpFyEwjj0Tz0YtbqqUiqxV3DVR0KSeY46O8AVoR3RZenVIXU6aNlmLyCbQNGf1EF0sbXHJd6iVf9F93saJcaAbtd2kHv-Zgrgasd36wZ8VeZVobAPJ0phIdNoeVuoP_25eVr0nVLFQQtYPa-pTlQ5vI5O4_l5GKr-JyWpmeeWPXgi-boSMffICzK7CfoF7_HCX5TYtzNBiKVuHUo1jxO1jOTVeNs8GNT4Tby8nsksejnaOqI15XRu4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBILNI-DSeetLav1jRna8QqQgZuZjt7ENmZr-cGlw2Qv_7q5CIG2sfykEiM4-jcjPPRQmv82WVpWpao9K42tw386nxoub9Mo712-7xITAay1CPzUFv2E-SD7y1MP-BuyG_ho91lWLY62MDAphnAtSOi2qk8-c-tiia6u4p-pMJQ9NJy_TqtiN7yRCfMt2d4N4xPog2QtvCOgTxYqJK3-HK35MnMx194FXK0YjyPHdEdIlIBbZ9rmEvbC0PJrcPWSZ7zBNM6xwc7oZ1sy6qfeFCfwEzdZZMUZeWcsUFG_P_BObBR9je-onIlU4XupXobDmOxr99rIfI0LB9peP7AQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=hYfJfeIvonh6ZV5O8KgwBdu81qyJlstX6NBSobLEFPKs_aFjvBfuIVmi6asreVjJngu_xKyZ9xV1U9RrxHWgsEzUDTujVWiw-9hZhDuhLQCtZtFFDx9eFqsuvTqS455-V2AOpscQNTJhRuzTV0C7zI1hUBM6ryZa6avlbIrhAKfj-AG7odUUs0tPXEqb05ggdaFNG52DTx8la5TOpnY7ZoVngScnNEtn419sE5JRKSAHLoeA-g4yzL05qbxEBXoQIqm4XXAeA7oUF_MBVQsB19iCfNOwJYWIkw_X27BnLPyhL7NKPxU-zYKjoh860z7yTSrPfR2EOzIr8lPH8YVFqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=hYfJfeIvonh6ZV5O8KgwBdu81qyJlstX6NBSobLEFPKs_aFjvBfuIVmi6asreVjJngu_xKyZ9xV1U9RrxHWgsEzUDTujVWiw-9hZhDuhLQCtZtFFDx9eFqsuvTqS455-V2AOpscQNTJhRuzTV0C7zI1hUBM6ryZa6avlbIrhAKfj-AG7odUUs0tPXEqb05ggdaFNG52DTx8la5TOpnY7ZoVngScnNEtn419sE5JRKSAHLoeA-g4yzL05qbxEBXoQIqm4XXAeA7oUF_MBVQsB19iCfNOwJYWIkw_X27BnLPyhL7NKPxU-zYKjoh860z7yTSrPfR2EOzIr8lPH8YVFqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ebWpuk1HJFDAzMBieLQsdH158509Of6-_kmyKy6O3DCMG5nmF9-hTmma6dU49ivLGO09SFcIrpXYwjCyjdd4MuZXu4E5Hjpe4xJrFkl7djx5kOXZ1YqfCiSzkLm7OsuzeVtrZv0Ll92eq2_e6nYYdf5BCo9kCgTzXJfC1uPlG_ylB8aDoqYTcgYOIyqUkosGAGQ3-q0yExqsiC_v_YHALFdxlgei1yZy5NLi9zf8VnH6o4WMXV3WX64DYAsscRSWdRO8t6xwjG4gBxmz-k-yKELDz43pymJwBuaFic-yaLuys8o3LG7UFQv_IOpqsZoOa7JJrRLOYF-hpnSaTjT1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KclBLMXxDcV2okb-BmadJQevKyccxIVArFxaojLMEuPLg32gAId4DhgAppp7cVXMN-wjL-crsApivc-w-39GAGk-EBdqu-lv6Po6Bh7Gt6jc39lEt6hQG1JnKRpqTE7HxUcBHm5oredgQVojRTsiad3x1nBV0sKbOxaneWLMIEuPvhxVSjM6IRHO35FhekID3nIM_eKVIlGIFwPKJnBpNbqwUFeSOi9VNm17MzjaK7cNo1mUeyo527ZMNjckuZ7893047sfDD8ICo03XSS-hTSYTviwxMIifqTwfX8jja1_n_N-jxRvSPajz44ZchaGGxfzpnDnoAmrDirfTyW1TRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3vyVXK7q3ybMHPH4V64WF8W-Nkr8bmY5J2R_y2UrEynlt8rPIwqULY4eHtuTXzJ80iXZGslFU1TSZmQRF53GCQk076c4uF7CUkWP-8ISuR1Z8mqyxyx4coUtZvJDGXJ6LwRQY84zGouN5PfsVhNC852EW6LPPSXfVwLKk5d6dGPbaVoQbRZM7IxLVki3oAFL1vyAu59sPiwuQ03kd0YPMS8FVkwy63j8oqAzI4Gx72lKOMT0XMfv_Zg11m5ty6jvtUTCz-jj8lXTZXEsQ1Kp5Kf4y-A9yCar2hzhoxaQAx37Dd69kEtcsyGS7e3s20c9PmcUFgar8FqXZ_TI7W3cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=d7spOjKuDIL0gqO3YpAjOKwkjtdOt_F2jYBEGVhQEw8OZR-fpah4SHlUTM-XU13lekeJrnQWZHjmXh2vmHjagZnjWwDhpFTLwj3uPlxhQ39IoAvvSzLXAWu8AhsCct3U5M6t7MJQFYPu4OEHpL6A_Fhe4jm2LPnjlJiVIgfBiSwnKLOlekptg1o3kWW9ros2W6aC0-GKe8TDW3RkCv4_yEe310j9nOvhVGPnILxZGHXqol09xkyXBzyEskQaR0WuZDa5Jr6wIUHQfQ3ma2L-LyqOHsOhhbBUen8J5pRATsDNBrp7XHeNOUk5olT_IGq2WpoQjXHmUG3CmX8r1ewP0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=d7spOjKuDIL0gqO3YpAjOKwkjtdOt_F2jYBEGVhQEw8OZR-fpah4SHlUTM-XU13lekeJrnQWZHjmXh2vmHjagZnjWwDhpFTLwj3uPlxhQ39IoAvvSzLXAWu8AhsCct3U5M6t7MJQFYPu4OEHpL6A_Fhe4jm2LPnjlJiVIgfBiSwnKLOlekptg1o3kWW9ros2W6aC0-GKe8TDW3RkCv4_yEe310j9nOvhVGPnILxZGHXqol09xkyXBzyEskQaR0WuZDa5Jr6wIUHQfQ3ma2L-LyqOHsOhhbBUen8J5pRATsDNBrp7XHeNOUk5olT_IGq2WpoQjXHmUG3CmX8r1ewP0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=t5hFlenhoHWVLo0-l9T6HMyZo1LS9spMY9BbhwnQkPjBGxbVDoKmmx8RUAjL_ud4hL2NlYFPaIPuslv8PpDf98T42ejSRdIngpo0ubJR4C1taMCMeK3_PNWoGUjy4ajJ_ynyEVA-Aq_dA_h0p87FuPMQ-ochX7Aa5yleWEocNx-q1KRIfdSvWqmcvNpl5L2RcclmjbQwtnbor1tv_r7VrCWcZgca3x44Ndg6e_Oo8fXgXHAu6ebLdBl-4Fk0fXQnUyDDb2ePZhfJHnGYYwAhO13pA-RaF9haC7-4Owsd4wdY7nfiUaN0IvpVE8DgPPFB2HGw47rHHuAJ1Wy6NbVKiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=t5hFlenhoHWVLo0-l9T6HMyZo1LS9spMY9BbhwnQkPjBGxbVDoKmmx8RUAjL_ud4hL2NlYFPaIPuslv8PpDf98T42ejSRdIngpo0ubJR4C1taMCMeK3_PNWoGUjy4ajJ_ynyEVA-Aq_dA_h0p87FuPMQ-ochX7Aa5yleWEocNx-q1KRIfdSvWqmcvNpl5L2RcclmjbQwtnbor1tv_r7VrCWcZgca3x44Ndg6e_Oo8fXgXHAu6ebLdBl-4Fk0fXQnUyDDb2ePZhfJHnGYYwAhO13pA-RaF9haC7-4Owsd4wdY7nfiUaN0IvpVE8DgPPFB2HGw47rHHuAJ1Wy6NbVKiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxGV6bGzI2aEWUaDCACHiTfRFNi0-vew_BVUkg-k3-izrhRjV0vADXj372_-b0WDT1q9g0TDckfPXkMsEoVCLFkcXBJw4sKDhP7qc6QAgrgsNm6xMp4j0c2nBAK915kR31Q0rvoDpWxJgDLteYRZimlOb4NLoh0FSANmTwy7buEg2AHZ5DURz_KCo7yeSGp-FVMOakhj6ujosKEpg4AsXoznuujmgetdCGWNPj6hdW9genuVqZ1ojk3FcVxFA7z-lmHY66zXtnHqsMynj1GQgZjL-DO0k0tlLJluvjrwmwlYGpNrX7hdPCYsrfxRItbrki7WPu8FGzfx3ZaA6nPGgLDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxGV6bGzI2aEWUaDCACHiTfRFNi0-vew_BVUkg-k3-izrhRjV0vADXj372_-b0WDT1q9g0TDckfPXkMsEoVCLFkcXBJw4sKDhP7qc6QAgrgsNm6xMp4j0c2nBAK915kR31Q0rvoDpWxJgDLteYRZimlOb4NLoh0FSANmTwy7buEg2AHZ5DURz_KCo7yeSGp-FVMOakhj6ujosKEpg4AsXoznuujmgetdCGWNPj6hdW9genuVqZ1ojk3FcVxFA7z-lmHY66zXtnHqsMynj1GQgZjL-DO0k0tlLJluvjrwmwlYGpNrX7hdPCYsrfxRItbrki7WPu8FGzfx3ZaA6nPGgLDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fReEThDOkZd-YhFmZLxHj1oML_DpC6BURF7nZrxtJk0110Y2YZtDU2AfNKcSLGAnskr4Lsf1TBR01Ktls2iQPJFMj-o7iVvK6t3FO7BX6cCxKpqhdMcLD7Kvv_lOOKj2TX1eSHyt-lv0aqgYYdd7Ystu8nsu9tqPfiV1OMEa-o98v_1H2gGVat99djwzuwcnWGApPtF-yBuwZ6S8N3q7SNoehDzu73suNwWkRS3zzCxtW3Bp2yLMrhMLjTdoVAlWeSb7tSPS8wTjRyqkAxv1Frb7vt0h9zY_Q9qw-BlrdqQRkX2PkOek2p1_83F2wvXmXXIhzTAZHFpRJH2qJhOGKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS9oj8Til5DsROAQF7i2L9yUSwoGUWgZ54Bp68wzatk5l2w0UWbbt_b-z2s-3WlKeMlVoJ1r3bJRqpHfPHe6nnDGtvfT2qcrcqe1Uu27akekaOlbLZFIybIW7AIqt6F4yqN5mj02Ka2vvi1HikrqPir4J_Ze-B9nU_gB-RtlLG25LTLtOeNxbtR_i2eHwyPSo4wBTITEz2nFBeTXriSzuAwV9J9FNkt4WeTPTGpz4z8d6RElmPYpnU0gVT6IbMOSoMUtiMjCqxlRLmjiHnMpx8nVGqrqnVq1pu--_4B9rz6I4nOkinsznEbqFI2xcOvJ9BSdOB4uEin6plmpNepDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=sV4q83EjNgttZnY_5F-YZOh_yhdTXNem_XH1IjuJ8VSv5i2xeHA9QPdYRfCKvXFszBX6v6DoCCinBAr6BiIiwJq8dlz1httbfW-jaZfuD5SfYYZvlJ_v0BE7dYkIwMb48JMoZsTVA4sCGd31wH_G4JCGyN4h7ftgAdkxoLTui6q3MXSs0Qti6A7edcqM5zhCT_1l9w73WNK-uN5KpWXo8ZEOsLyDpCpaadBRLwwrZsp3En0M9pOI1fj5rEtqbPAgGEBZK1T7gG45X7IiE0tUI0fiIdAGc3M-mdfTDE9mErc3LIMTMcJrn_kaPFbYpy3b96_XBNr4MyoufAqG6oI8EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=sV4q83EjNgttZnY_5F-YZOh_yhdTXNem_XH1IjuJ8VSv5i2xeHA9QPdYRfCKvXFszBX6v6DoCCinBAr6BiIiwJq8dlz1httbfW-jaZfuD5SfYYZvlJ_v0BE7dYkIwMb48JMoZsTVA4sCGd31wH_G4JCGyN4h7ftgAdkxoLTui6q3MXSs0Qti6A7edcqM5zhCT_1l9w73WNK-uN5KpWXo8ZEOsLyDpCpaadBRLwwrZsp3En0M9pOI1fj5rEtqbPAgGEBZK1T7gG45X7IiE0tUI0fiIdAGc3M-mdfTDE9mErc3LIMTMcJrn_kaPFbYpy3b96_XBNr4MyoufAqG6oI8EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vv99d0WJ_Fy6jB9xJQ9AwXkcDiT8r2iE41HGMmAcatnumioUMBJKO5D4GXqaiZuSll45ENuG08appqR5xIoKJypNhFELEXYvoj2Je6qmEuvlP5oYysjDi133lHuiN5-Zb0vwFMqYa-rcy53nVKLNH9vS0t-ZqAwizgBk7z19NFB3ih_1S9y7msv5ORrYCKiEgR0dpKjKyP9sFussI8D1Tqf_vv54jjboqtagpxXB8DCQwgzUpk8VpnwuTqD95MSX2_IJM1eUkDqGeH2V7GFX_FGAZgBVxmvVb94Stc0P8GEpqUjzd0UDx9AHvwRNsoZmUAzglO62r6ywYG0U3FUHfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Wj3-RUYbJI_TQjAH2hh6jDxuycGJQoZfkEg9IIn6LSEEzplEH6o08j_Yl6WRtvK1_y0d46V2RNNUmJ2jnjElAh8yuxp_NktTAxIEW8OIuzfHfvaPLtboQW1YHSx3ebjowNyIptsW6wgwASrZGiJ9oZaUNImFZAS8Vq9qRl8zdLS90jFNdOyAnCu2AK0HBMd2dkpel4gksEuexk74lxo-2J1rtmw7wQMP0TM3-4MS-dr31PltSSBMgE3FxeFuU9c4LNmBMn0NtNGzuhosZGjAOdu3rYgpwwE6I1qcOuPd2roMbtQ52lDXpd1_38ZzLRLNs14-sjVzEim4qokCy7aOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=Wj3-RUYbJI_TQjAH2hh6jDxuycGJQoZfkEg9IIn6LSEEzplEH6o08j_Yl6WRtvK1_y0d46V2RNNUmJ2jnjElAh8yuxp_NktTAxIEW8OIuzfHfvaPLtboQW1YHSx3ebjowNyIptsW6wgwASrZGiJ9oZaUNImFZAS8Vq9qRl8zdLS90jFNdOyAnCu2AK0HBMd2dkpel4gksEuexk74lxo-2J1rtmw7wQMP0TM3-4MS-dr31PltSSBMgE3FxeFuU9c4LNmBMn0NtNGzuhosZGjAOdu3rYgpwwE6I1qcOuPd2roMbtQ52lDXpd1_38ZzLRLNs14-sjVzEim4qokCy7aOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=kpYkbj_VIOHIhaNJylXAya7ltoIb8aHsbGeNl50yq3lDSCXevxTYPQENlQOW89s3mkuaCb6EPHARWSi7Rq5bAe2lp4cOiOmDHc77NARJsUOrHWcJFAK7YY0YNxrEPmMC2S6LicqIDzzfItVMo0kmdgvEEC-05mHkVAcj7BkMSBqyHA3_hIY3SU5KpVNS2K8p5DwcDO21CN0sYs3gV5nfJnMhSkLv3rjJAtfwSq9Aw5ov2s1DR9_6Ri_Pjbo33n59RtUOkwJNcqvJEbh0Ih8turiyBCqNVOiQNAZNia2tlvDybP6qwTFKYXrBApg_OpArm8M0nHSV1l5N0I5mYdy7Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=kpYkbj_VIOHIhaNJylXAya7ltoIb8aHsbGeNl50yq3lDSCXevxTYPQENlQOW89s3mkuaCb6EPHARWSi7Rq5bAe2lp4cOiOmDHc77NARJsUOrHWcJFAK7YY0YNxrEPmMC2S6LicqIDzzfItVMo0kmdgvEEC-05mHkVAcj7BkMSBqyHA3_hIY3SU5KpVNS2K8p5DwcDO21CN0sYs3gV5nfJnMhSkLv3rjJAtfwSq9Aw5ov2s1DR9_6Ri_Pjbo33n59RtUOkwJNcqvJEbh0Ih8turiyBCqNVOiQNAZNia2tlvDybP6qwTFKYXrBApg_OpArm8M0nHSV1l5N0I5mYdy7Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=vlWU660rsBhkt5mk_KgOPmll3ciQacgQh_D2R2nyIFjp1ayUp6FwqASxMNa3XqiOGM432PdeNApxpVHtGq0YF_me-W4Gb7367BazcQkeCHmmR4BO05zyF0SC-PYRAh2TwHVr6h48fTixxx8cLz9BhJOUdRfW-fBTmrDFBoNLT1RoDeLpFsAIL_Uw1yuyflSjhcxZc-aVfY-EWzU1bQ0W8vIGqvf0GOBIuL6HPuuIeXec4lMNOt4U0Kdn2BwejSogREmbvXjihXyeCI9GBkb-waoaDKWuwtcSOYz7ggrg18hmXlzcOjfLA4Lgqt_EtvWkvokNBTvN18K6t4WlXD-C8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=vlWU660rsBhkt5mk_KgOPmll3ciQacgQh_D2R2nyIFjp1ayUp6FwqASxMNa3XqiOGM432PdeNApxpVHtGq0YF_me-W4Gb7367BazcQkeCHmmR4BO05zyF0SC-PYRAh2TwHVr6h48fTixxx8cLz9BhJOUdRfW-fBTmrDFBoNLT1RoDeLpFsAIL_Uw1yuyflSjhcxZc-aVfY-EWzU1bQ0W8vIGqvf0GOBIuL6HPuuIeXec4lMNOt4U0Kdn2BwejSogREmbvXjihXyeCI9GBkb-waoaDKWuwtcSOYz7ggrg18hmXlzcOjfLA4Lgqt_EtvWkvokNBTvN18K6t4WlXD-C8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=OJkpjUER0oP-4QFBYlG6SuDr5_ni-cqKc_ehR1MQ-cVaqgqkwxYYhK4ixyBKENAjVqAz6hvRHPOaJBQA1bQRh0GM_R_g_sFsfBIesqnVhxNbv9jNNjAuUNrTPbkcXBAzkHwyobcnXs2ZreC6gBtWpqQKu3mh-EDH1LpcaPiXT_HVLbqF3DowOnuMXFVgxJgIOIRT9bzk2zZ2RzVJkPZJ6-QCS6tG_xcQ80BBr3ajESz3BaaDbls4_UNKD4vC0-9A5vtMIQ0186jOT4JdNVQeF3d712CAJfXvIO2VJqj1KSs-SsftjscixixkmSqmDEicULZqz1r0saZNnyTFRkiOvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=OJkpjUER0oP-4QFBYlG6SuDr5_ni-cqKc_ehR1MQ-cVaqgqkwxYYhK4ixyBKENAjVqAz6hvRHPOaJBQA1bQRh0GM_R_g_sFsfBIesqnVhxNbv9jNNjAuUNrTPbkcXBAzkHwyobcnXs2ZreC6gBtWpqQKu3mh-EDH1LpcaPiXT_HVLbqF3DowOnuMXFVgxJgIOIRT9bzk2zZ2RzVJkPZJ6-QCS6tG_xcQ80BBr3ajESz3BaaDbls4_UNKD4vC0-9A5vtMIQ0186jOT4JdNVQeF3d712CAJfXvIO2VJqj1KSs-SsftjscixixkmSqmDEicULZqz1r0saZNnyTFRkiOvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KisRnpvPAzWxxDHgoLpn5CrctdM8yURctu2aC91xX-9wHX-6T3GX0Ih-Xcq3416qNkwlGDawaCA7PG-X0bBzP0K6t4izakdA4K6EIZJ4y0CDlrzvAH5LHJvnL0-KS0-SBVB5ok8VNr0WPwPVuz21xGQGGual457L4fJOdIIZbTrVvEzH60YJNmNW8XxLxdURZ9fXPt3bbaEMpHWOg5j2A5-9NU1GyT1HYfvZx1wi_OBtXMiVDD9eNHOJekeVmF_peizt6j-pKJO9qjdEmFWZd5w6TC1XyO4ERCG3pj2asLDcOsf3jTScz50ljtu7nEQY_DgIOz47TtnxwBZYi4EIFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQxe2ITLSiUkHRzYejIM99WGLlVD8k8ImkeaIeYP95teVb2QAZ-dWiDxp8C7Lo7OwkGzup6-uuMxUqFmpC8KCrhHHIzWUzOQLUgG0UiEOEaAcleaW0PkPgsbpwhhd7s1i3hqqV5ysrTtlvpYazxbHSKD_q99zWIoeKFydM8Y6u7cC6owsPh8ERAoXtgDAzdKy_IHuvdoi60Pn1S12xd2OKPOg-hf9hKwd5TBZLFSc85CoM468OPLtrGYmyRYPNea3kfEzVz_3b-qi5dskRJIxNhe1AhapMW-PpgJjvh6lUs0N9suRIlNSqaOHUQrpZxQ7hFMqEnWoFrhKa5GMkmjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrlZqKBUuxxSAH8PK8OBmFsJsRMOm0DGQU8LeBuFDvBe5aA_N20TOaDZxmGzc-_g2439j_NEHpN76u0uGRwcY-VVx7sUW4OycLsR6Goq1igKeDKU1h0F1T-6Huf5ATPLcQB4CTEJna3Hzork-fqnmsTrW-CCE2OosAwpBZNOm7QFd9Yv3qDuQvXYn-AbnvgENw7OZsV6deGRAj1sWb7Z11qfeOnZqk7Cmwu3CEtbynhUHjCaWze5I_4P1Qvmo_iLkwqJQgPsz3TJn1bre39bItuL6oBgM9SvXz9jIpfuiA69cWtn1bP_H4hcqlmOg02JtgFRldUl7rbrvptUPOGPng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X06o8HB6uVaMX3bP-UJIh9ThwfefiqqHwr9Xbtys38AyPZOb7uueOLHe-_K7QIBdXD2IDwdlxyQ9eahjJAwNyqsgGTWMOLZ41KlaAHb7HWFeQhdnVh440YwJ1mIQtxUdH7K2nEFT2qAHX5FGKDav--jSoAkmKVjdxDRQpmblLS6Lf_BkynouXF9jacXyb1S_1rfKKU-GqaM9mqCdmtzKSR7PSRIdNvPCku0KcGXSeVYd7oaNQWHfYkLavdZxUHfRmp8uSFC4u4cmHXjasDVO0bp92gi_ruZEriT0m9vghTLkdQZAMNVxwduhmiVzFsrnJm8L_-MqKm6uJEDeWNNpfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAmIhkLqJm99RMV7X9ZQgwEe13mSIFRGPoi7F88DZkEL9doTQmBiKLzIk6ubAlBPLk67EVHUdVY3lNoRgrME6Ub0dabsr7S4WTjF8iU5nJ_1lUO5Y7xA0mHVbZXyz0q66mPwKRYD45EfHe5yz20Zv0qve1KjFkQdWSzuMUBIWDX48pT7pRh3fnvp5P5uc-uqE8MXwnMJfxJrrD7S7a9GarJyRPw5O7GgVzD7gkoAG0lBlSYU5k85bkqjlmFhL825MIWKgsVsLBTl3PW-NecekV16S6l49dfqnGhzmvHQstPDZF-TKDwgwngJkUUrcpjhETG5criuE3viO-WptOV_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLGSKARZwzud-OCAq3md1PXcNVjc6qxrC6B5QpMTaj9TjPvEtFZVSYBfkgzLdlM5Gz-oEmyeACnCB00HSHVjjYFPDTR0t_Gl-wiwGa7OeYwp0nUGOnq_pE66lRS3Xlc89tGWo9fbPKvYg9WZEe8x6QV4q9WYp15xwv5Rs6Xho3oTVHUuc20x39_NEvDZAoWOKiGTHcc4wF63w0uRLRyyUQgKDg_ZmDrz0Di0SMqXrfHu2TtJsuzeUqZgSvR2mnSQxPdZWRTaZb-JWUeY5eZWX8LVIYZLAaIr7SLwZuU2uyFgSNnNwhNFj12cmdKhLO8dyz1XMyf3xcuo8TvW3CQtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_zVKrTuLlTTKmkyyPywI4I7xz_fd9NRBbB3VqGqFvHKtpPve7Hcgh77rxNDFILpQekYkPJBcF-VfmdRwlnZuFlBDvtiR72eScL9tExsDXNsUMy4cDiTVQ-mWMRczfZqt3cjTHD3XN3O4V9_wgazjR6zCD2wwZo0-9tBCrgJsdcC-Sp7LarcT1cEaolI0AQTviteoh2RARg25aDkEwte52xcOOWxz7tjMKdEnQ8L76edkJKcmh4RrodTcbGw5rqxd1AwN1JPhKbKFEau36o3sLQOreT7H4R_a41q1blF_ybwY9XkMyDcfB6lATvh_R2JF_DwONHeuDKnuDNRVDcjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=Xudp2yLZSgP9LykuloJ-NLQPVxgDLqAOqcNdAfCg4ShJxiU0gJDx7tjNainxL2w5piXliM2l1HGdoYMl5_LNyd4IkSadPfUU6sP-Vu8LmWy2srhavwSjkVGVkEdRCQX8wdQWpFfqKPr0NIj8Oeclkh1QJx0Xif1072_-huaG8v9R0TVS5PtCkejT6CQkdc7-r-UmXm6Bj1vjrTBtZQgo02nXt9NX3BqGK0f_4OitdMMATgNP_80JM2bBZtldK2HD_Yx3wD2GHISxmuKTxfXzCUc9MDDVhi6O1TDtcwIwfVJipSYSbr05KD_caFSO2lD1If2lwYj3ln75X5m-vBlEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=Xudp2yLZSgP9LykuloJ-NLQPVxgDLqAOqcNdAfCg4ShJxiU0gJDx7tjNainxL2w5piXliM2l1HGdoYMl5_LNyd4IkSadPfUU6sP-Vu8LmWy2srhavwSjkVGVkEdRCQX8wdQWpFfqKPr0NIj8Oeclkh1QJx0Xif1072_-huaG8v9R0TVS5PtCkejT6CQkdc7-r-UmXm6Bj1vjrTBtZQgo02nXt9NX3BqGK0f_4OitdMMATgNP_80JM2bBZtldK2HD_Yx3wD2GHISxmuKTxfXzCUc9MDDVhi6O1TDtcwIwfVJipSYSbr05KD_caFSO2lD1If2lwYj3ln75X5m-vBlEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwr-sGYsI67U7Pos-OfNdf6Rab5nJXPtSKrfFqJxL7YTOEqwcwE0KCCqx6LNno99VsSHjMPr9diHoUM_sQ2Ww6s2PWObkyX_MOOc16uJLZh1ibwJIJOhuk1wuReGwBrrkTeGCIO2nTg3A_fm3qsMJwCawRkJbAId-DDPlDNCyctQ2wNsdMrvo_AF5pp3s21J1P3d1FApwpoeDdsGmfFdIIrK9B6p32ehjw2FRB__Nkwkpc-DwMCNBc7nRNJ2PwT8t12lzAhBJD3W246WF2A-dbTOdsQqEtTuby1GmEY_FHS85quq7ZLj4PcAX9IDsZkhE8xc7ppS44l41lLqv8mE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwXiozdkL4I4R2pt0zQjWV-MGuNHcTs7cEgZDED2yUpe-Jyeml55eNTqZbMYcpZyuOcJ1XqzfTkv6kwahowgHMiyorg0eGjLBGc4WoymXzMG0WAPzz7IJW-2rphYljUp6dRN0ySMh47fplL24Zt2XkZx3TOK_h8dut95JynBAG2KXAiuPobRJufoH-Kbq91fZBgUcxA00YysdY4Xv_COXY3eewjT4S9YdafMZTIvHrngZDNrSgmh8uxtToE9Nd8wXnxvIXA9_CdoSUSO6S6q_ZxPY3nBX_j7Lu-XyZCmHDH6OyFwA-gXERNKpcmqCMjQkx5V5lJmfZ8A7QR95LqBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIGM5OCq8_AWL2F0ULc1T1Bcjai10Vsjx0AWQLa9mXC4-ssBPTAG-PbylN-nJtFsQtZAf0BLbfyfswNXrtoZpW9Laip28pmA8ahn4JfCFNmAj004QVB4yHMit7XLAsQV-BBJ_Af-ULM1Tl69ruDfWT0XmjkDkk-QsIBqwQqht3QfOOTwC8ArUuQCCrR4ybplwWUQCPKdOwHMUE8bHyVe287PuECqGmSUMzKGhGVp82KRPKWpIDm11vBDdfGXZNQR40PiIzBCXD6sNxLHLsolBI-C2LeTBtgnnQrCIzEY5ZpiGixXFOoDcxQ7095NHckuhq8EEdYWPRWnWR-NrxfMcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5dNTI_Etig4qNHEfc3zwbdE33giieKnk8yskFtc_QVg4iBsbMRmpiRdHetuHz_HuIsOkcJ6GIO_9pqHnjp2TLog8JheOn-Xe03Gue4QJu1hszAsaPbnJZJ0OXJn9rUVS65tG7tOZ2o9arsKaYdI51p84UPF9kkf_WgOfAC-IW32QVwsM2Hmk-F-9wDfs6nh1CTZ5NE6tKnSHpWOR5W3YvK9TVVWQKIjCxUKjwIbzjQp_k_L24xZQEo79DL7vcAzT0RBmNS3XurjBMgrliZxbFEKaE8b1gNlOwPEjV7ICsGllxvgRyaG4FQbcSAU1sPs8ez2q8bCPZMRY0-DeWBKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsS08OL-RVX2wh2ouqx4k7gBXOCws9ItHeTc7YbxGEi3aw9SCGHrag30R_aMNc5KnoC3bDGHldlOi9H8w29Qftqsm6B2xquCRIq6AumEn6-EJkEyNc1GQGksQmS-zIdhBRNTzWi1-rYJ5A7idJpjNxOnCSvRZKDamK23j9jjJm_qPgsdIpAogLepKHHzq2chMq4elngFIntIzkpQx89Da33Pr_OAeRFnn4lau0AKMo3p0KoYw75rGHEJ5FcmUQXaickLwhO-7qhrKaN6y92TvtnwyazM-bx83szLQnZeC4krfV-jsptaPGLNnuNNzbwFMD741ygp0IhP-SBx2o2YVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRkQXVKDrSUqBkLD1YS_nl9LCYlegQwfACYbtWipPHgmc_LaY0vERMU3IIQkRZQoWEES-_S-cPOUfPN1NLPhPNQF3fcUMJ2ca7gIzMq4K_1GTAw2LPck4jKvvRSOPl3WHk5C1fzXUvssimCcrSsY6Jv5jPFpfLHV3K3SGStRuZcjofvhMsfw13u2WzbWiOvNzfKj-737lxeAlLy4kx2yUivZ9T2ytkh3wBGu1WuHxnp67iwYuKQpZcuHJxPLnP5hGIPqAUPONql7XSqgAurxG5UveQIte3wsRdm68Dy04DmYeGrHMYN51yKAnEwKymz7xWsNjXHgyIgrEdMMI9rc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFwCIur1J9jGZXG43ZQJgpzQW4LHyT22SUMoz2p11lwQKdK4vinVQ_ncffQysueQSQDHQunR74IZln4fww6X9tKuIYfyt1OoLiLxGOOCdailcfumVK2jak1FvFEv2ZP4NmBwCqULVVT7BZitiRVk3qNu8bbXY1ObShQtSwSrJ98eAbmGlmD0P3wKqZpf6JvFuNHexgTIQSp-mz0ZBk_clHhzJZOfrDJ5WsBKnzZPm8705SEX8_LX9b-yqSWpXazMzN90ic8uy9k09h0o9V0tZz2tANR3ubJ2MnI7gXM58CQRQq5WTMwfYGy0D11xfLiM6m3sMdaxJcMnrLaieR6gPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj1hyxJLvp6gY5-9icVNSlE90e7cYvYPg8m5hFionX1-7bksl91Tz_7iSgTYGnydgP4qBIq9ehEYpTk1qFzL4nKvfwGFqO0rNoNIjiH-CzbA4eI5ST4ZHAfgtMeFGMRB8Je3-fXZ5lQaUYMCk-yoqwti4U3KrqzZzyLrQefBJxf0ZdQOpTrTWSwuj3jXK4LMNjdwwNiV4HjeYkim67ipuNReu3aTRjiOTZchjId6m8yiy_CYDHSgMTdUyU_ze2AqvhKbuEuC6pEjnJKE0n4QPRUv0JBcUzZ5xeiRJNPezO9EiZHhI_BUfV_iVS57vQiUNq-I8Bjfpbn64nYWaQTb7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=pGKTJl-6xT8ZQzpGxyoXFwJErETjO2a2IHepRH316jCoV94kH4XjXN0vvzl2herI24TBNovuiy4eH9eKl7zB02U8-4hp_xdbyoWgV-GQtF19_fBUXD5HkIy6sr-j3b0SAZa3wGlNu-CGbRboMjwKvNQ2CT7juyGMJgfOpxqnf4sUpST51wbVQk81iWjq8hJ5Yod7_3PM2fEJspBMZ8LhcoTGtPNNwHxnAkwtvTIpWFQoE-lbV0IXBVu-6zMaxs74c1zDLW_e9YtAwef3-736nNQLoUcfxXWJVmzmy7IN1RahxFY0Rv_4UlDKw4yabMSJ2VFCOlOtOY-0svxensmWeaThCVWX-kVc7te5xRTktuHp6bHrYacMhNhgjDrIB1oNcHtJtqKXY9wRVV9sCRHC26KdqiU4v6TC6fJ7VLQI-pyiIWYGCI3lS9OOo4IKqwaQqch3i0domrRCexZF3UUR6CTfsA6FFe719wCqYBcVNwIuxgXoG-zveRvenP6nouzyzz1FgOTSkY_l4C5bjqWQXjaFAp_Cg2nBs_-qrIlQ0fAyqZAgM2NRMqGLlp1MjAX2ShdbwTTL5bDxdr8vYhofjHOBEuDNClSSt-F-AsmRatpnopV6GYs_yNwX0z5cwWDpzi7S8cs0RT_U67ikBIIvlBuyoa1Wzj9j7u7JQrfOA3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=pGKTJl-6xT8ZQzpGxyoXFwJErETjO2a2IHepRH316jCoV94kH4XjXN0vvzl2herI24TBNovuiy4eH9eKl7zB02U8-4hp_xdbyoWgV-GQtF19_fBUXD5HkIy6sr-j3b0SAZa3wGlNu-CGbRboMjwKvNQ2CT7juyGMJgfOpxqnf4sUpST51wbVQk81iWjq8hJ5Yod7_3PM2fEJspBMZ8LhcoTGtPNNwHxnAkwtvTIpWFQoE-lbV0IXBVu-6zMaxs74c1zDLW_e9YtAwef3-736nNQLoUcfxXWJVmzmy7IN1RahxFY0Rv_4UlDKw4yabMSJ2VFCOlOtOY-0svxensmWeaThCVWX-kVc7te5xRTktuHp6bHrYacMhNhgjDrIB1oNcHtJtqKXY9wRVV9sCRHC26KdqiU4v6TC6fJ7VLQI-pyiIWYGCI3lS9OOo4IKqwaQqch3i0domrRCexZF3UUR6CTfsA6FFe719wCqYBcVNwIuxgXoG-zveRvenP6nouzyzz1FgOTSkY_l4C5bjqWQXjaFAp_Cg2nBs_-qrIlQ0fAyqZAgM2NRMqGLlp1MjAX2ShdbwTTL5bDxdr8vYhofjHOBEuDNClSSt-F-AsmRatpnopV6GYs_yNwX0z5cwWDpzi7S8cs0RT_U67ikBIIvlBuyoa1Wzj9j7u7JQrfOA3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=TjSsuMUdUXFvujJk7PoNh1ADjOuIHHY9RfUealhQlm9EPFldVsZf7pciSGBzdZB9JltoECav0UtorAQg7ck27W0wVetQ52mJ0tfNG3tQ_LQBtr39OokxZ0aGJJeEyKkQfV-PNuaYuoX1vRPK3TcjClyFEwJxlE391qYnayypiptvQgTwve1QdDuZv30mN6ANG5Mk23g8EAQQMZ1IEPsYPFhWmd0Ig-JWB11lFk8ICICFlHEePE1QIvC5cl6vxLcJsXu-tPJ7BQtatIMjaXjJzgFtCEOOLsiUY9M7KAzxoZBu9b3GwAYyUwK9BqsZJFdO2jwclgwoBrl7tKwKCeINPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=TjSsuMUdUXFvujJk7PoNh1ADjOuIHHY9RfUealhQlm9EPFldVsZf7pciSGBzdZB9JltoECav0UtorAQg7ck27W0wVetQ52mJ0tfNG3tQ_LQBtr39OokxZ0aGJJeEyKkQfV-PNuaYuoX1vRPK3TcjClyFEwJxlE391qYnayypiptvQgTwve1QdDuZv30mN6ANG5Mk23g8EAQQMZ1IEPsYPFhWmd0Ig-JWB11lFk8ICICFlHEePE1QIvC5cl6vxLcJsXu-tPJ7BQtatIMjaXjJzgFtCEOOLsiUY9M7KAzxoZBu9b3GwAYyUwK9BqsZJFdO2jwclgwoBrl7tKwKCeINPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1wvyEkflC7PlnwXWKxdBeQVjLs6STWY1ewGHz3eOkPKQ0_LEGMqrX95UxHmA8SO9dmyq8wyKJJL4Ut54Xx33mHLhzOOXQvpnVLjskmJYBNV4TlYdNZJz_Zg75fIswSAJDyX8Q30PO6MtVbbzJcUGVeau0LqhPiHRD598CBAbiwx4l11K6qRkz_AjVgGCwCUFuBFql_72lCAf1co3Pzpt8nzbWmLpjQtmWdts7P3TzNX3XMGt14gFOC-n8yu3oAazM3aILr_oKYCb5eAUetilRmOG1xH0Dq4XVosre7E1IX2XG5cEzSKyHbM4-tpGS06o2L9ir_reHBXsAL5gELypw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YliSdHxqM7csBYPrY1avMRqijFtRQdKa8ohRK-JwwHIvCK2-LttzPnXnCHRsYw_nLj2_b0mPxVPVdBhopqd8FHOhfeKkPkn1M5RMKPK1RO0bUvfTmB16GW1yQhseMMDGfdmoNGMAyfvN3oVQPwiiJhMPjeoq-RJbvF8s1phZbwuytJ-q_C0sf-WlWZYKSNRDJkxQMHG17QM4OZCB7BBDTUX2g3Z31kHR7WEOb0myZ09ypUvuZJ3c1CqFdzWM7r22LXRqrmldj6uFk-EsBHcRhVfgy3zWmM5hO4MJR6J_NPmyF5PZzbs9U8-a1StG7vXm4-q7LX3scXRpiWb6nj17IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpgbocJUgMEdKhG7ydnp9-4U7pQ7KdN2aQESV1kMtomkHa-xC6YTtTsXA15o8Ke8M6zr-BIStx27fb3jdUliIIUchBZDUQoHb6gIBzMRrDzHzZZGP6catvP6ZqL0s0Ouhmf3M0xRo8inyN8DqK-6-cGgmk3pG4rojHgxfRFdZr4JW5JsUtEu0xWixZSE-TVticvfY-4RuOX7j-LtsiT_rO45nACESWBKPLuOd0koi5-NCj1_ppB-1r767MJcN2C4nL1pIR4uKnhTjahxBDhs4-l0LhBgtRKH-_VsTaduffHiULjGWbFDxucim9ydLHJLf4m_ZOvoaY4H8a7MBADg-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmTVZXLGG3B3-35xiJJurZ5QyQGrHL6rsiLOjGsngq-5P_w_Kyiw_2m3Ey8xdVcQ3tbJkUHYCiqS6ARxRjmdyxu0jIVrCFePrViC0sW8d1GDXsTj3GrXySE5Ad6ihjLDhvSHLWtBxMkvXe0bpMICmKTBwZiGm_ATgzHyqBe6w013E5tTmYUM6TyPlyWv9GhBNVLPXSRxxCEr-h7UVhWu3lCsK79_S7JWCcYMLvNRx2Pp6lb1soUe28g9SKZgTg8Rl3jm6feR6BYh1M54E3-zmtrZ_EwCKkXDvIuQ478RMbh7WCUvqqO-4yC1WUOxDTMvI_JWwVxVdJtCS0IA0ZBWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9OQS3ZfAp_ku0fgEv0-PY9udJmKajqMXI6KdXdIS7Q13m00QLBTkxn7z0BEFK6gv1duCWbckMuEdjQ4FH_jJJCgnhDQ7a5WKe_rHQTDyY9lnPQ2NDKuXnPfmFgPiYND658WCFgl5A3csp_op_NHVwo2WVKag6gcJjQrT7kNSHiSlIzyTqE6rgUMX3aiJ78soj-fHyT04XVcn1TYx_dHDDY3co-pdsXZNVy7W8Hb7wpNorLZ1Kxekxd2WeECF7f_xCLSvObDD5XrtLr0t872gmwE6TzNhIkIASNdYAWeexN2DY3UmlsUqxJ5mryHdi477MCk00opB09-cdGT0NvlAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
