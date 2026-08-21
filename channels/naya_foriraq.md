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
<img src="https://cdn4.telesco.pe/file/RLovN9bx0Kx2TI5-A3z1IMIA4i_RKi4HkXiFmIusM7AgT7A--7K4DN8l1wA6YwpFEV8YSYvKilDnOD70eM45ImOU1C-vSO6H51QlMrNeFaepijOcLd8P3uuFo5WxYnhzD-yAi782mvP-edJ1C7dVOZiAxkkusTnBV9cOj14TJ9Dz4a2Blz71TqF619ft6siOhCexnfAR3EW7Fv1F1YilBIOFjGhVJ48Uh2wUrb_Sf1jZQxWgnSwVu1oQ30oE1G3V-GmiR53fq4J89HOI6SdbRpgecNs35f9GLpMkuJ1Hy_0nhky90yXE0k1o7B9IVFlI_eiGORJb3O2gHOZVt-PAVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 17:34:59</div>
<hr>

<div class="tg-post" id="msg-88278">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اندلاع حريق في قسم الخدج في مستشفى النعمان ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/naya_foriraq/88278" target="_blank">📅 17:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88277">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اندلاع حريق في قسم الخدج في مستشفى النعمان ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/naya_foriraq/88277" target="_blank">📅 17:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq0cph5___I688UR7cyorEoP0DNbX0uuIVe1PVJtxcSbai1Q_EJ3rmyqeUlt-7zVlcECb4fwa2HppYsN8Pw5rZAbgEPhZUPPv3pe4FYp69WPcjtkM__f0uLHxxUZt1bQBPc37el1uWavXCUuLqwPiOa62yGQ9NeyRPuJonK2B9lzf0LQUlzHqWo8_Z7G3LYChuVCURD21UwdaPpekOhWBCH6hvO8azVX8ES0lL4XjRU1b4Ugvgcn0bEkpg4DopUkJc8Y9p0VX9AZd5ImV7kYhvDsCFhUeWIcl6UHpZGxt6ELugjgn57yV74Bxl9dUf3Jn0ZAEZkJwdvI9yLZC6uGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاقمار الصناعية:
لا تزال حوالي 3-4 طائرات تزويد بالوقود جواً تابعة لسلاح الجو الأمريكي مرئية في قاعدة العديد الجوية في قطر في صور الأقمار الصناعية التي تم التقاطها اليوم. كما عادت خمس طائرات نقل جوي من طراز C-17 غلوب ماستر تابعة للقوات الجوية الأميرية القطرية إلى القاعدة لأول مرة منذ 12 يوليو.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/naya_foriraq/88276" target="_blank">📅 17:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية: مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/naya_foriraq/88275" target="_blank">📅 17:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c39f9d48.mp4?token=IUdwXvNgLghaRde6oSojcafzfxdsehpeujsGBxYm9-IDOZmzDrokecNSXyMpVkiZFeZ17GaM16KgMFKq79OMC22TS9EfWK3iuWKnxt6FJoePxt9rXjmFPfT0CEDmr2i6dWBFwz9Cic5N7E16GHzsqUR_NLUCh3Y_3h60S9R0DrtBRuY8ZDMw59F2QtaUqzDCsPAYRP3_ZtJkBGmGDe_luu36wt62iy-qekD-D0IMmDyau0skfcJZP5A6uMP9QvYT5SYf1eqLECYBOYdgrrz1XiJDOF_XAEzWhAkhoPSkV-vqbTHd_sPd_-9N2lwqNXlmrDMm2Rt2cu4qmAHvrWeljA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c39f9d48.mp4?token=IUdwXvNgLghaRde6oSojcafzfxdsehpeujsGBxYm9-IDOZmzDrokecNSXyMpVkiZFeZ17GaM16KgMFKq79OMC22TS9EfWK3iuWKnxt6FJoePxt9rXjmFPfT0CEDmr2i6dWBFwz9Cic5N7E16GHzsqUR_NLUCh3Y_3h60S9R0DrtBRuY8ZDMw59F2QtaUqzDCsPAYRP3_ZtJkBGmGDe_luu36wt62iy-qekD-D0IMmDyau0skfcJZP5A6uMP9QvYT5SYf1eqLECYBOYdgrrz1XiJDOF_XAEzWhAkhoPSkV-vqbTHd_sPd_-9N2lwqNXlmrDMm2Rt2cu4qmAHvrWeljA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تزحفلي تزحفلي وفاتح ايدك</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/naya_foriraq/88274" target="_blank">📅 16:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99c8dd0e3.mp4?token=MNQaKF2zhWtXtNZpnDaMANksrU0JjYMdVSM5LfkqVvVfXwyxq9GSNtkBNUq0VUbH11OM7Q08YmrwlE2PT8UKpZmvZKlRTGW7pQAvVyr-IjMqdNBb--Y7-nd6w3uOTd_O6aEccJ2-EotsC1zhLOmTosnkyBHB1eZbtHqt-nma5fnrEAjV6QvR3ykgRMeVQQuLRjGuIBbiRNutKUMWtReSdBCNX07_K1CW8N09-E09JtQd2Dm5RU0XpYiwVx6NOzcrWAyMG4owSfcLzaIBERJp8PpIuLi8n3bYBmxR8Ozh6tb6Qj3lUdvgGqqs0MiUIzq7ZqtiJTBxjKV372bLHtFCLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99c8dd0e3.mp4?token=MNQaKF2zhWtXtNZpnDaMANksrU0JjYMdVSM5LfkqVvVfXwyxq9GSNtkBNUq0VUbH11OM7Q08YmrwlE2PT8UKpZmvZKlRTGW7pQAvVyr-IjMqdNBb--Y7-nd6w3uOTd_O6aEccJ2-EotsC1zhLOmTosnkyBHB1eZbtHqt-nma5fnrEAjV6QvR3ykgRMeVQQuLRjGuIBbiRNutKUMWtReSdBCNX07_K1CW8N09-E09JtQd2Dm5RU0XpYiwVx6NOzcrWAyMG4owSfcLzaIBERJp8PpIuLi8n3bYBmxR8Ozh6tb6Qj3lUdvgGqqs0MiUIzq7ZqtiJTBxjKV372bLHtFCLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية: مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/naya_foriraq/88273" target="_blank">📅 16:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/88272" target="_blank">📅 16:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88262">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/colVTOysFV-__hRt6OUbXQfRNyMOBfIBo2XvuHAixsyw4F01usEMh4tNo3h23dEPnhG0Fbv1QVq30oBGxIpvZUywoc-bT_OeQ5fImHdLi-l2fVUuJ0k2v86qE2yQNkdRy6__S89uVZbFeoW7UjdKLki2AW0SgB_2F1ynlsmrLocHTHeOCPTrkdHRH9Mz7sB1xRqG2dLUI3LMDue7P88x6nNml2Pj113vGakycNfuf0FSKegGIaMZX0KpwAMCj58CQcH7zTsrxvngXrfUWhjyrptOpL48lJ3WLQ27QAcnWELjHrr1ku9pr3ZzE2nlRfGdqbEME_9xSe4TTsei-YD1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqzC4CdzxBhv7jDTIOu6hpiaAFJWPGiasIDWCYZaE-UamdVH2QmE7xtSILcWiROLPMrs36WXHo-D3AjQb86CnkL2i_mK-qZncHbSmSCZr9g92luyK4YPZf4CXZX42uhS7nOPSDUU9q2F9NokDb3JWnuxQWIBlc0lb4tR3Wpm4U4e8D4wZcR0YqJ9NlpcnBvFQYnbMLfgqO3HsFRZCj4rQwRZY2rPU1mdR1n3JJ5CBYbW-z1RvghRG-VWP8Xg9AqBKCSrgVC8mVKbMs8i-EO8WHs3_3qiDEZi8ZFeD34nIuXb-WZW2RXuX4kuDr0NHcQJ_VklxW7tsqnjuQchWSilLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azeb4QOEDdbXrZ5GeA6LuhQPfaZ4R92pF96YYIu94GISI0ZKbjXnbpUObOlZi9ZapJSbjSGWEXKlpwNn3Ua9qqZCpNluW-AYXds7I7c1QLomewFuUA0FZNP7MecDEyx9omcq77ZVuPOwfruMzNCDf1aimjDIRVrb9rirFlhM7o3jyq2Jzon83GkhWUqungbqxX7DSbRNGlXkti_8Wygwz7ccQeHSgWEHVEppkSl6NEar5-6L9HABVP19ttGOCr5hpa5xLrW3QSXvJMzE7D3wnr4lcpz3HyS2VmFV3DNahmnv4AqDzD4NLTYiqKN2DacbgERWjRCQwcvj6dXyCiQ0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgTI0FT-9-k2I8MNWIYoXEN9sdEbVFUoxbHrFyq5EfVqN6dBwIZfCj_FS3gME2GWDah_Bv7k8m1_QQ5fdED01KzWv0JOY-tQWoo498dLVLO4B8xrE7MqBwFfnpx1392QUwXZlupNzP7lInXUs3bHm-KrX5ueby7f_ZHhc0Z_XS8HTPRz6zMDMWjerxd0bHzEbwsYj12meXJArqcxBGW6tW7Q9CGddffTQDo3yj2OcH0hx2gVh_8gHZqim-wwi-LJgXNuLTTaVMPU0D92KeS6SASy2iJyGB9qPGpCaWGSr9hz6R3eblZNQ51yP_Pkebws7hNDjOxj1OFGgdqX3mRCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QCFp-xM0kPUoI1nz3xOazHhpteNXVdLDJ3_QZKCPZGXvE7RPPqX7Ny2TL69C660hI521U28Q_LNpeY17yrMyfb5gZgY5ghYW4kQXCpWcUJs0DPL9dDLcwkvTVRK0PYrIQ2AX30uZVX18XG5IM0DrvtMl0k176Nqwn-PCOp-cqGGS0f-hsBhhnKqtQDUhACvClQAgMS9Z1B1uaEf74Pmez0R2iVSOWd40ejrW0BYkua242OKkDU8th1mf41Gm4H6W-AfWRrK6DzqzVTB3YbxpHVb6ZgAi1SfP7LFyTfixibHRsfm2WBRXBYF2Z2GvDZMoc3MDZP0THck3guahY8tUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_dRzw82YKAC4yeqyB7CYTtBxXbq3rAUiOUrkp5md57HZdJrbQoGaKVGfEtjcoba6661g5Z_g9WrKw0g8ZizXhZBQQky9IMuxOt5WPkCzmar-i5whBWluJhC3XKnrcqXNcmQKoJCfKRaMFGL4wTU5b3rUC8qXbjnRbjhB80d_2pR0OKWwUkI0pYJmEOKFK9WF0nT6l1aXDdrdSMYj_W3djAIi3_QmAzv6Uf3M0vPfzZoJ8oRzDWCAINvVQ2sp0ZOcPTcrRzuERDnRadU1ELg1UWkyW0z27PG4j5dhgZdyWMZXyPqRF14E2zjF7y-RwMBMJNCooTa4yZFR5JuiYzRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jl_ulylkBIvmj4aR4NcC0d5LV7YPx9d8h-iRUGb1D8kyOBjbpJuH9qNBK1KPw5Yki2a7Dkvvj-YUh-3gcG4VdlVOw-JQ_QGYVF1CnHxX18fR9dDfzjOlqMZrT2j2v-IJHBVGk-tudJ5TH4_SU-AwMNWWAoWn6POizz_ICbm8IGJKMzwO5RNWZbLbiE7UkgOzhbhqpAWAnwjGkMyxI68Kb_WLXY7CnGHhsMHNXI96n69ZnwA69kieGjLrbgqvXMEbnEhG7117XdzKUlCu15-wq-OhPXIQwVGv-t25s9aeqM7rS2SL4x--uipnykl4psc_NKMVBaOT3h1jCJFFY_kdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFGR2NkhVxdFZxnBIv5ljJE4blOf8OBDXRWCgQq0NZTOb33JWxCY9guhkIhLw08CaR8LQe2Uv98hnE3TH2bxbIyh-M2ckXz5gsnmFqUcLVOAZM-ArzTw2GBasa5OrSQpfpp8rWiwkea26jD1r8H9RmUUZuwP7xtcLh89uXczvV62fuQcyLHA3m_Yro3TyXJFSy96k6JYPFzal3gCHEiWp89LAPN0o1DhiEO_oyY-huJId8QohQkLu72sQ-1iurlfQTymfEPULQ4mV3SjNm8F4jvPvPZzcf9uRfVIfIrGpW7aDk7_5QAB4kY4_5yG3njefIQvnwzXKokh2bAQF8nHyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5BjmvCwpFox-zdMsQnXWT5TmyI0ifDjfQCu2I-1HfB7C9sa4FSVu0gG9wJ8enO_Z_0e0jte9zIdBvC9FiudfOO0oSCEOFPUtWMGALTmU4wJxJ_T7wHFa8FR-LdTEj-5QG0UX1eFcGGJbaV_cAmiuS-QRSZ--NrcmL-xuqKlefXq9zUCH6RkLJCaXViJ1gy4UTqsN4L4S07lLDaE9j08ib9i0noU9qx5JY0XxyOqmQf-m98QzR-FVexZihvs8UEH2ETVoRdy5taiXhVEPejKVTXGQrASKkOHJMMtM0xB18a1gcRCGSIyvg3fjCoobluxmRJU_NVeybRTtapt8L-Lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rHm_X4UGFVWUgYRNa5WDo1-YF6JtLSSjD86g_yUZVl57Vv42UWZ2ePsQmkVvkKEbKddavdNQ6f4b6qYPblVr7Mz29SM8PAZATXm8P0WohGqIULXYPkMX5xWhTLf6cLyRM6NEHOtR6azeF89cO1U-sgLUtwVkLQghzwpDa0XZHR67jaY8xX97Mk3slyPBh487NyORJFeKB3Q-d9TRcqG9JyoOTLBT1OFP5h2VuBxTfeMRCvsy5ETC7zi23xssc_Fyg2J_2S08QT5x5sYma3nD0WTLU0FDrCju151Czaz6YI5cNtvSKKRwNGbpiV_SAXCfoixHBuX2ScTdPQvwciJkVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات المسلحة اليمنية:
صور من استهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/naya_foriraq/88262" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88261">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULQBNRIQKlLWxpfVXvh820uQVqADILx0VYlWxr12qoJ3hJ3uGiEZHnvUc5vXOPPQMH4XdDFYGAVXTPWk4xSCuJ3xbomV6jvBIjMx11BbHiVA9Uxni5O8ybe4ezcQqhcxMsHGfn9f0r1Bd8S_zUE7UHfGf6VmDAxophnJ2BYTvcQafqEfjJTJzYF1rJ-_7X_9UB6N3J1kos9epUHe87Oq0yY8g-rHpTWOIcbHA7C-YTjZ9hB-SgV6TmfWNHuRnmn6Xn139678ohQCkCxTFtfUytqJxqbOBR5hJUQk5crRWi8J0AS9MnkdEKxOTF8uGmgBfGEXW0OU25F-JSH9qwyWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اندلاع حريق هائل في مستودع بالمملكة العربية السعودية قرب الرياض منذ أيام، ويبدو أنه يتسع نطاقه باستمرار، حيث تجاوزت قوته 200 ميغاواط. ويحرق الحريق بشكل رئيسي الأخشاب ومواد أخرى.</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/naya_foriraq/88261" target="_blank">📅 16:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88260">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98553c859a.mp4?token=Xmpm4m3-xiUB6QL0uu8DoE0aYXSO_8MVyxBJ2jh78GodNQ_InWObA3wq0zGIEgmvTN3Y3WlJxDQ-ZK-1ExW38u4fgoxBZjjKWZI0iJqfprhy7PJ-RF_1vEmmdzsKDkdHxLEOt6ea0VGkTNELnMXsbBlv-AZ7smJEy-9z4BBGKFnZbanKYLo0GzEWDXWQiwvs6XiA1NYzXGajuIUF9CJ8nKD4eSPI9abpAtVvsS_NlhNhyNvYz_U-fqT-UtNDQcejZcEoJxnFp3llpjTdRg_Fs6vPzJBLYf1nr0dgqT8QgYxycrO7KLLeVLUTN7hSsrlJvja-CRduZKj9SjG41lPqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98553c859a.mp4?token=Xmpm4m3-xiUB6QL0uu8DoE0aYXSO_8MVyxBJ2jh78GodNQ_InWObA3wq0zGIEgmvTN3Y3WlJxDQ-ZK-1ExW38u4fgoxBZjjKWZI0iJqfprhy7PJ-RF_1vEmmdzsKDkdHxLEOt6ea0VGkTNELnMXsbBlv-AZ7smJEy-9z4BBGKFnZbanKYLo0GzEWDXWQiwvs6XiA1NYzXGajuIUF9CJ8nKD4eSPI9abpAtVvsS_NlhNhyNvYz_U-fqT-UtNDQcejZcEoJxnFp3llpjTdRg_Fs6vPzJBLYf1nr0dgqT8QgYxycrO7KLLeVLUTN7hSsrlJvja-CRduZKj9SjG41lPqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر أضرار جديدة في مصفاة جازان النفطية جنوب السعودية، وذلك عقب غارة جوية شنّها انصار الله بطائرة مسيّرة في أغسطس/آب. وتؤكد صور الأقمار الصناعية الجديدة أن خزاناً نفطياً ضخماً يقع عند خط عرض قد استُهدف، ما أدى إلى اشتعال النيران فيه.</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/naya_foriraq/88260" target="_blank">📅 16:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88259">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا
تعرض موكب ابن السيد خضير المطروحي، قائد عملــيات نينوى في هيئة الحــشــد الشـــعبــي، إلى حـادث سير على طريق بغداد</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/naya_foriraq/88259" target="_blank">📅 15:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88258">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">في اول رد تركي على القصف قرب الحدود التركية.. ‏تركيا تصدر مذكرة توقيف دولية ضد نتنياهو بشأن أسطول غزة.
رد مزلزل</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/naya_foriraq/88258" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88257">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
بيان صادر عن حزب الله
:
خرجت علينا الإدارة الأميركية يوم أمس، عبر وزارة الخزانة ووزارة الخارجية الأميركية، بادعاء أن حزب الله خاضع لسيطرة فيلق القدس، لتبرر من خلاله سبب إعادة إدراجه على لائحة العقوبات، في قرار ليس في حقيقته سوى حلقة ضمن سياسات الإدارات الأميركية المستمرة لاستهداف المقاومة ومجتمعها وبيئتها ومناصريها ومحاصرتهم والضغط عليهم سياسيًا وماليًا وأمنيًا، بهدف حماية أمن العدو الإسرائيلي وترسيخ احتلاله لجنوب لبنان وفتح الطريق أمامه لتنفيذ مشاريعه وأطماعه التوسعية في المنطقة.
إن هذا القرار القديم الجديد الصادر عن الخزانة الأميركية، يؤكد أن الإدارة الأميركية التي اعتادت استخدام العقوبات وسيلة لفرض سطوتها وإرادتها  على الدول والشعوب، ما زالت تتعامل مع لبنان من موقع الوصاية، وهي بدل أن تذهب إلى إلزام العدو الإسرائيلي بالانسحاب من جنوب لبنان ووقف اعتداءاته وتفجيره للمنازل وجرفه للحقول وقتل اللبنانيين، تذهب إلى حصار اللبنانيين وتعمل على تجريد لبنان من كل مرتكزات القوة، وهي بذلك تسعى إلى إحداث اضطرابات داخل لبنان وتحويل مسار المواجهة مع العدو الإسرائيلي إلى اتجاه آخر.
إن حزب الله لا ينتظر شهادةً على لبنانيته ووطنيته من أحد، فتضحيات آلاف الشهداء الذين قدموا أرواحهم من أجل لبنان وشعبه، والتاريخ الطويل من المقاومة ومواجهة الاحتلال والدفاع عن الأرض والسيادة، هي الشهادة الحقيقية على لبنانيته. وإن علاقتنا الوثيقة والأخوية بالجمهورية الإسلامية الإيرانية هي علاقة نعتز ونفتخر بها، لأنها وقفت مع لبنان ودعمته وآزرته لتحرير أرضه واستعادت سيادته وحقوقه، وبقيت إلى جانبه في كل المحطات والأزمات، وكانت من أولى الدول التي ساهمت في إعادة إعمار ما دمره العدوان الصهيوني إبان حرب تموز ٢٠٠٦.
إن الإدارة الأميركية لا تملك أي أهلية أخلاقية أو قانونية لتصنيف الآخرين ولتوزيع شهادات الوطنية عليهم، فسجلها الدموي الاجرامي من فيتنام إلى أفغانسان والعراق، ودعمها اللامتناهي للإبادة الجماعية في غزة، وتغطية جرائم العدو الإسرائيلي وما يرتكبه من قتل وتدمير في لبنان واليمن وسوريا، وعدوانها على الجمهورية الإسلامية الإيرانية، ودوسها كل القوانين والمواثيق الدولية، وضربها بعرض الحائط كل القيم الإنسانية والأخلاقية، وتحويلها العالم إلى شريعة غابة ينهش فيها القوي الضعيف، يجعلها في موقع أم الإرهاب في العالم، وينزع عنها أي حق في أن تنصب نفسها حكمًا على العالم وشعوبه.
إن كل تلك العقوبات والتصنيفات الظالمة لن تثنينا عن التمسك بخيار المقاومة وبحق لبنان واللبنانيين في الدفاع عن أرضهم وسيادتهم وثرواتهم، ولن تغيّر من حقيقة أن المقاومة كانت وما زالت وستبقى جزءًا أصيلًا من تاريخ لبنان وحاضره ومستقبله.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/88257" target="_blank">📅 15:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88256">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
🇾🇪
الإعلام الحربي اليمني:
ترقبوا الساعة الرابعة عصرا مشاهد نوعية لاستهداف القوات المسلحة تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيّرة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/88256" target="_blank">📅 14:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88255">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">استهداف منزل ضابط في وزارة الداخلية العراقية رفيع المستوى في منطقه الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88255" target="_blank">📅 14:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88253">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:  إغلاق مضيق هرمز يمثل تحدياً كبيراً.  العراق يمر بفترة عصيبة ولدينا أكثر من حل للمشكلات الاقتصادية.  جميع القوى السياسية متفقة تماما على المضي في حصر السلاح بيد الدولة وجار العمل على آليات تسليم السلاح وإنهاء هذه الحالة تماماً.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88253" target="_blank">📅 11:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88252">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
إغلاق مضيق هرمز يمثل تحدياً كبيراً.
العراق يمر بفترة عصيبة ولدينا أكثر من حل للمشكلات الاقتصادية.
جميع القوى السياسية متفقة تماما على المضي في حصر السلاح بيد الدولة وجار العمل على آليات تسليم السلاح وإنهاء هذه الحالة تماماً.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88252" target="_blank">📅 11:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88251">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
مؤسسة "سي آي إس":
أن الولايات المتحدة قد استهلكت حوالي نصف مخزونها من أنظمة الدفاع الصاروخي قبل الحرب، وأنها تمتلك الآن ما يقرب من 800 نظام "باتريوت"، بينما تنتج روسيا وحدها أكثر من 100 صاروخ باليستي في الشهر.
يتزايد تساؤل الحلفاء في أوروبا وآسيا والخليج عما إذا كانت واشنطن تمتلك القدرة والإرادة السياسية للدفاع عنهم في وقت واحد، وخاصة تايوان وحلف شمال الأطلسي.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88251" target="_blank">📅 10:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88250">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
قائد هيئة الأركان العامة للقوات المسلحة الإيرانية "اللواء عبداللهي":
القوات المسلحة في الجمهورية الإسلامية الإيرانية، بفضل استعدادها الشامل والحديث في جميع المجالات البرية والبحرية والجوية والدفاع الجوي والفضاء والسيبرانية، ستواجه أي أخطاء حسابية وتهديدات تقليدية وجديدة من الأعداء بردود ثورية ومؤلمة ومدمرة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/88250" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88249">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23d5a7c74.mp4?token=jKivgvTZKGvu6oa0HasIHln8Q8FuSIqTtIpuiwedgY2zIX8P7rTOG7bwY9N2va2ccqrGpaO5zHWrR4CaqM2vhRgjX35VtOMmiYcVPNFV5Fj2n5Fl1GrzbbLiJGzCYUuTy10RGY6EM1w-_kToEq8g1Wuz_L3Q-Bh1iWDKaDB3A6UXFn2JGhprZjhU5xi2L10DElvCALNQcNFDtOTwnDw2soMdQzo89N_Pcc78bbykohshpzWIl2hqjZ8WBbPoMkMmNKVgji9og42cUpsgy25kVC-38cq_j1BYzfObggWaeqWkX7D0WETx7jyhxUbcFKV0h-2LU6Xl07YBffGhyj6Rsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23d5a7c74.mp4?token=jKivgvTZKGvu6oa0HasIHln8Q8FuSIqTtIpuiwedgY2zIX8P7rTOG7bwY9N2va2ccqrGpaO5zHWrR4CaqM2vhRgjX35VtOMmiYcVPNFV5Fj2n5Fl1GrzbbLiJGzCYUuTy10RGY6EM1w-_kToEq8g1Wuz_L3Q-Bh1iWDKaDB3A6UXFn2JGhprZjhU5xi2L10DElvCALNQcNFDtOTwnDw2soMdQzo89N_Pcc78bbykohshpzWIl2hqjZ8WBbPoMkMmNKVgji9og42cUpsgy25kVC-38cq_j1BYzfObggWaeqWkX7D0WETx7jyhxUbcFKV0h-2LU6Xl07YBffGhyj6Rsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس البرلمان الإيراني خلال زيارته لمرقد الشهيد القائد أبومهدي المهندس، يكرّم عوائل الشهداء الذين ارتقوا نتيجة العدوان السعودي الأميركي الغاشم على مقرات الحشدالشعبي.  #أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88249" target="_blank">📅 10:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88248">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
🇮🇷
حضور رئيس البرلمان الإيراني محمد باقر قالیباف عند مرقد الشهيد أبو مهدي المهندس في النجف الأشرف.  #أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88248" target="_blank">📅 10:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88247">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
🇮🇷
حضور رئيس البرلمان الإيراني محمد باقر قالیباف عند مرقد الشهيد أبو مهدي المهندس في النجف الأشرف.
#أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88247" target="_blank">📅 10:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88246">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0ca47031.mp4?token=GmkfLj2f3YBT1Cm2v8qcv_ZOt2cjuPgUOWtcl4KdFkwYUzXQ1zHjWhBIYSjYSPC24rfObOZo75Pa-63dBNFyeSl5jgH4uuH7eEOR8vbRY80AGinpD4BGwAJk7mhd458CF0FqXV90UQMtSFrns500h5RdEovUxTX89OJhvlFUiDBtd02fqxM5Vzhb34_xoNy6kWZb_Ru1_f-W7Qv5mRFC3_85xC5zeN_qSzI9-OYELfy0o4mY1AGp1X6HtytqDsrhNeB83T2NWsOQw13ev491D02vpCmXbVQEj6OpbBGWgDYlVfCtD3KMDsr3RrhjyyMaqNqkQ8OF1bn_nfLc_H72uLgCe2iDee1FZPV8OulS47-tTHACUvU1D8gIUNod8t-opIT9SvCB_WXYPvLeba65steuviGGVZDUXYP88uKBDDUdS5Dclw0Nz2Antk2JeReYrn9fYVH0uIcn1AXABcYMwY04cIwoyRmrsfxRMAdPiSjEfQhGM3bCtsqXmZYOzNfch-bCB8vau4qZhF8udrDxREaMRGM9ChBaQJxLprGVxlK9Ak-3Vn2mzq7NRs6tbfuz8r2dkbHB6BUy7dUi7XtALazJz1yQ5W5MPYW_VmU2vqrpJ9ZnD2RqPg1bdiFfZHC1iBM5a6ENinCVHkj1P6lxuD1eX9coyfylv9M0QteJiW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0ca47031.mp4?token=GmkfLj2f3YBT1Cm2v8qcv_ZOt2cjuPgUOWtcl4KdFkwYUzXQ1zHjWhBIYSjYSPC24rfObOZo75Pa-63dBNFyeSl5jgH4uuH7eEOR8vbRY80AGinpD4BGwAJk7mhd458CF0FqXV90UQMtSFrns500h5RdEovUxTX89OJhvlFUiDBtd02fqxM5Vzhb34_xoNy6kWZb_Ru1_f-W7Qv5mRFC3_85xC5zeN_qSzI9-OYELfy0o4mY1AGp1X6HtytqDsrhNeB83T2NWsOQw13ev491D02vpCmXbVQEj6OpbBGWgDYlVfCtD3KMDsr3RrhjyyMaqNqkQ8OF1bn_nfLc_H72uLgCe2iDee1FZPV8OulS47-tTHACUvU1D8gIUNod8t-opIT9SvCB_WXYPvLeba65steuviGGVZDUXYP88uKBDDUdS5Dclw0Nz2Antk2JeReYrn9fYVH0uIcn1AXABcYMwY04cIwoyRmrsfxRMAdPiSjEfQhGM3bCtsqXmZYOzNfch-bCB8vau4qZhF8udrDxREaMRGM9ChBaQJxLprGVxlK9Ak-3Vn2mzq7NRs6tbfuz8r2dkbHB6BUy7dUi7XtALazJz1yQ5W5MPYW_VmU2vqrpJ9ZnD2RqPg1bdiFfZHC1iBM5a6ENinCVHkj1P6lxuD1eX9coyfylv9M0QteJiW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
جرف النصر للموت ما ننطيها
لقطات قليلة التداول تنشر لاول مرة تظهر جانب من استبسال كتائب حزب الله وسرايا الدفاع الشعبي في العراق بعمليات تحرير الناحية ومنطقة عزيز ويس والفاضلية بعد فتح ساتر ياحسين باتجاه قلب المنطقة .. اللقطات تظهر استخدام الصواريخ الارتجالية الأشتر وصواريخ ال 107 ما تعرف بالكاتيوشا و ضربات ايضا بصواريخ ال SPG 9 و ال 106 إلى جانب اشتباكات من مسافة صفر بالبنادق الخفيفة والمتوسطة .</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88246" target="_blank">📅 09:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88244">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
ترمب
: لو كانت إيران قد امتلكت سلاحا نوويا لكانت استعملته ولقضت على إسرائيل وكل الشرق الأوسط ، لدى إيران بعض الصواريخ والمسيرات لكن قدرتهم على تصنيعها منخفضة للغاية مقارنة بما كانت عليه قبل 5 أشهر، إيران تحولت إلى قوة متسلطة في الشرق الأوسط تتنمر على الجميع.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88244" target="_blank">📅 02:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9042a34cec.mp4?token=TUZ_Lq1rP2bWbhZQoleUMqTaiA_G190UYLW4aWtHNWIm3XhRz6-Rl_A3wYhG7rOC2vfV-thexpalAFiCSI0lF3sB5tpf1JeT_ecFSJvEn0txHbhIhsv0nFM31Z9SKhAjD688uBq_zyHzorr1mT1OTfKVOWuR-eq7s3YxofuUwR1d99OHKN2QPar8gff6H_P59rF1AJqNpupE6kzYHusirQCQtMX-U-JTDj3x9iMeNKocwj1xwgmUaLIMcoHfjQxJ1K4nClb501eMLfjYecRo-YdHOkMHaVuGzrnBDgPrbYE6-VLx7dKL1PUli5-30-TJXRknwvuTLGUlpk4dW9uhmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9042a34cec.mp4?token=TUZ_Lq1rP2bWbhZQoleUMqTaiA_G190UYLW4aWtHNWIm3XhRz6-Rl_A3wYhG7rOC2vfV-thexpalAFiCSI0lF3sB5tpf1JeT_ecFSJvEn0txHbhIhsv0nFM31Z9SKhAjD688uBq_zyHzorr1mT1OTfKVOWuR-eq7s3YxofuUwR1d99OHKN2QPar8gff6H_P59rF1AJqNpupE6kzYHusirQCQtMX-U-JTDj3x9iMeNKocwj1xwgmUaLIMcoHfjQxJ1K4nClb501eMLfjYecRo-YdHOkMHaVuGzrnBDgPrbYE6-VLx7dKL1PUli5-30-TJXRknwvuTLGUlpk4dW9uhmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
سفير بريطانيا  لدى العراق عرفان صديق
▫️
‏نوجه رسالة الى الفصائل سلموا سلاحكم وستكونون أصدقائنا مثل احمد الشرع.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88243" target="_blank">📅 00:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88242">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ربما يسمح بالنشر ..
🇮🇶
🇸🇾
🇸🇾</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/88242" target="_blank">📅 00:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88241">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3XTtdrAuV11QMnztqx89P900WPbS5ubv0WDX8vD9Tzj62FNzOQ2W3HOHpiwSkxLbdXgEDZI3KWy9biTjkguW2Ijb8wYeZ7MUnWq187q2JifbQmLJeor4s3jJRuxPFi8pKQ4PnpvNJmBDaTUXBqFRwJAKgEvTFhHiMlCy5xCFqEqv-4_x0_MjYXauuP-SUmhAPu0cJ4Edpe-qLdyxpRt0_2KEDJ4QLV64RYVYwsXM0XT4NlaDRKmx6PnR3v_jzpqKsDkDEnMVnwWia-V0SyIP_0Qsgj3qxPLr_zlXuqE9DS8JRJOLULj34ODV3BKUwI5vFdd1f_5JEYaf-3ygw-r6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
صور اقمار صناعية تظهر تضرر بشكل كبير في مصنع مواد بترو كيميائية في دبي بفعل احد ضربات الصاروخية الايرانية.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/88241" target="_blank">📅 23:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88240">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg5uHwCRi3te_fuVny7HrpLAgaAIEmdZlqsPDHGgsCs2UHidIWHjxJtQB03fRciIu2hLv5YLEUN_F7KkulNB-g0-IwD8IxWrNa2GzPo6sLBIeO0oa5dv9F4GrK7zh51N5eauh2PDYAkidyHA40l2MSoO3v-7nSF0f2ROQZEiXpWm2EMXXS_fsDBjHQXTuxYWBUzHpqPYknyCWcG3CFuTvPW99m1ZdHF5IL1yHydlEp304_RkrVn7XTx2F19UqhUoycIxUPs8WznCn7C6Kuxn81aaP-lvZ93N5vL-r5q2FFKMor3MNhdj7utfItWxURMZWQiYloQ5nntiz9VlKksEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
مشکل، به‌طور خلاصه، تفاوت در سطح فرهنگی و علمی بود
پس از آن‌که آمریکا دموکراسی را برای عراق به ارمغان آورد، عراق بر مبنای قومیت و مذهب تقسیم شد؛ نتیجه‌ای طبیعی از سیاست استعماریِ «تفرقه بینداز و حکومت کن» و نوعی الگوبرداری از وضعیت لبنان. با این تفاوت که در عراق، رئیس‌جمهور کُرد است، نخست‌وزیر شیعه و رئیس پارلمان عربِ سنی.
مصیبت بزرگ‌تر این است که طبق آنچه گفته و نقل می‌شود، رئیس پارلمان رانندهٔ کامیون تریلی در مسیر الانبار–اردن بوده است. یعنی در همان زمانی که قالیباف هواپیماهای مسافربری را هدایت می‌کرد، این شخص مشغول رانندگی، تعویض روغن خودرو و تخلیهٔ بار بوده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/88240" target="_blank">📅 23:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88239">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WULiWnGltQVJ9eSap8IafzMiXWYcyL_GPdz-lnCeRFXaGi4zDjjcXbVnujTyFonDxFvwaUCYTG-4KAsSBKpsXjsZviTWZ5Nr6xyF4eqn2OoMe6sxs_AffcdkNKQYEAnGxd3NUAvx1IBJq9I9Gt4MG7wp8tfv5XuutYF8VBLMFCHngardHj2S_JhFnhVFg-ohTsxXc5Jx_PRwt0-oDhRQcMzRhK7wGemExgXSRIJC_CZY6CZ2rOiDzRnoonZ1ZJCeIZQJc6BdFEtJlkR0ha_VwNnEz-7nFMm_mi0mXfTuEQXcq9q9NZ3Xhf6T1Qgz0LWGy5jOkWUSWVjB16oP4rVO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربما يسمح بالنشر ..
🇮🇶
🇸🇾
🇸🇾</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88239" target="_blank">📅 23:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88238">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba39abc2c2.mp4?token=Z8J331tjziEI4p8wwz_OsEQSh6NlihU9ztfcCRnqFNNfZz7gBTOCSyDw6Dc-oFZIwNvAJzqdPYb8VFYT_75S9Wsw8W6MlRYpC3ncjwjkFivpCmKmIWwwr5yC-iVLT6e_KzetPqA6GnVkILytb3Sp_Pu54xCD32XvuSaLs0BVozX36NxQP9wBBL8fI60hTJRbwWQ07BvE6cDbimwKvleHblUMOIx8D4xlRp4MUVpOT33GoFtjRIsAXJLu_upHrvbmtuhFtHZQIWrAtVrmQBYVBUVY5YU84zyfSWMwsUwrUKHjHlPqtHWZu6B7Fz3j2vr6NpHAc4npEG5IIf-CxSfYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba39abc2c2.mp4?token=Z8J331tjziEI4p8wwz_OsEQSh6NlihU9ztfcCRnqFNNfZz7gBTOCSyDw6Dc-oFZIwNvAJzqdPYb8VFYT_75S9Wsw8W6MlRYpC3ncjwjkFivpCmKmIWwwr5yC-iVLT6e_KzetPqA6GnVkILytb3Sp_Pu54xCD32XvuSaLs0BVozX36NxQP9wBBL8fI60hTJRbwWQ07BvE6cDbimwKvleHblUMOIx8D4xlRp4MUVpOT33GoFtjRIsAXJLu_upHrvbmtuhFtHZQIWrAtVrmQBYVBUVY5YU84zyfSWMwsUwrUKHjHlPqtHWZu6B7Fz3j2vr6NpHAc4npEG5IIf-CxSfYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ملانيا زوجة ترامب تظهر:
سمعت أنكم اشتقتم إليّ. ها أنا ذا.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88238" target="_blank">📅 23:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88237">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660318801d.mp4?token=bE5EjiFqT5qkLmL-JTsFiu3tHq30CZzoJ9CMRHhmILgi7UyFd-jo212OBq_y0pJN8rKwjvjuh5azYb_N4-UXOdQI8QdijO51PJVuG4S5vJpFfQ7OFqhX7yNziOj6QKSOLmGxpT9VNi_Chq-Wn_Sb-5DxWciiJ3UgRlTVWbNzcoVhw2rJJuRI9Y75x-KvnFm4Ucn9dCqoBKezhHoD-PQjOU7LHB2MGZGFdsA4nPoOJYvfELbN3MDnOUD40UAwwKVspe9_ApJXm5wEhMsqPadk7kjrMFR7GDUSO3HGt95MfqotN2l_dB3WUQTDHK3omg-TcRJQJwXMI12cqo2lRv4MkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660318801d.mp4?token=bE5EjiFqT5qkLmL-JTsFiu3tHq30CZzoJ9CMRHhmILgi7UyFd-jo212OBq_y0pJN8rKwjvjuh5azYb_N4-UXOdQI8QdijO51PJVuG4S5vJpFfQ7OFqhX7yNziOj6QKSOLmGxpT9VNi_Chq-Wn_Sb-5DxWciiJ3UgRlTVWbNzcoVhw2rJJuRI9Y75x-KvnFm4Ucn9dCqoBKezhHoD-PQjOU7LHB2MGZGFdsA4nPoOJYvfELbN3MDnOUD40UAwwKVspe9_ApJXm5wEhMsqPadk7kjrMFR7GDUSO3HGt95MfqotN2l_dB3WUQTDHK3omg-TcRJQJwXMI12cqo2lRv4MkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حدث امني خطير في امريكا   اعتقال امرأة للاشتباه في تخطيطها لتفجير قنبلة في مبنى الكابيتول بولاية نيويورك .</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88237" target="_blank">📅 23:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88236">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🫡
أنا تحت راية أبا الفضل العباس
We will never forget Ya Abu Fathel</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88236" target="_blank">📅 22:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88235">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رويترز : قال مسؤولون كبار إن القوى الإقليمية لكرة القدم في العالم تناقش إمكانية طرح اقتراح بحجب الثقة عن رئيس الفيفا جياني إنفانتينو بعد أن أغضبهم بخططه لبيع حصة في كأس العالم لمستثمرين من القطاع الخاص</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88235" target="_blank">📅 22:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا
اشتباكات عنيفة شرق العاصمة بغداد في محاولة اعتقال احد قيادات جيش المهدي " ابو درع اللامي " .</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88234" target="_blank">📅 22:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زلزال قوي يضرب بيرو بدرجة ٦٫٨.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/88233" target="_blank">📅 21:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
حدث امني خطير في امريكا
اعتقال امرأة للاشتباه في تخطيطها لتفجير قنبلة في مبنى الكابيتول بولاية نيويورك .</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88232" target="_blank">📅 21:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇱
🇹🇷
الاعلام العبري:
المستوى الأمني أوصى بالتهدئة مع تركيا وعدم فتح جبهة إضافية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88231" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88229">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8d4d95c8.mp4?token=o22zrfB_dNofX0MpDM6rm8NNukecjgg9U6c9jYPz0t3q1P40lOzYZDveXRIAtGSxmIK0OGCqUNiFNahNxf6xcf9gQuLK3JHJArmxpOsSzF38u6ubJHSmjMlJ-ciCnQKB4jAS1dA05UuFGfmCJoCXX8Rkb0-sitVAX3cbWHRf1qr0uPrE6IDAWTs0NwxZFna0YuY8tLICpdb1SYtXOUwGTaKXx39EYBGpznwKjlqcbNiOyfJHQ344ZKQnSUXHiCrcJXLoUzx5nX38SXmOc0lAlDc0KDo0-9n4MXFNdmB9XLchviLvDjjCibAaPHGkkBOOX9A_RM8G4q-KVhbx4C6T0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8d4d95c8.mp4?token=o22zrfB_dNofX0MpDM6rm8NNukecjgg9U6c9jYPz0t3q1P40lOzYZDveXRIAtGSxmIK0OGCqUNiFNahNxf6xcf9gQuLK3JHJArmxpOsSzF38u6ubJHSmjMlJ-ciCnQKB4jAS1dA05UuFGfmCJoCXX8Rkb0-sitVAX3cbWHRf1qr0uPrE6IDAWTs0NwxZFna0YuY8tLICpdb1SYtXOUwGTaKXx39EYBGpznwKjlqcbNiOyfJHQ344ZKQnSUXHiCrcJXLoUzx5nX38SXmOc0lAlDc0KDo0-9n4MXFNdmB9XLchviLvDjjCibAaPHGkkBOOX9A_RM8G4q-KVhbx4C6T0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كثيف للقوات العسكرية على سريع القناة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88229" target="_blank">📅 21:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88228">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9276455e9f.mp4?token=lhNpNYCmGA1Nu7PKB2QvEyLCryX9_T2VbMAEuPeE71CLLabELYlx2JdnMC2LGqxUS7f8CwRqWFhWAjUmRrdZYKXL9_steQvwevZ3OAEx7p7_iLeuHIE1eI17Y1OxUPO4lG90nup39CKKQqtV3vayPGUB3X12XyTv-n7PPw4ECqCahapVDo6bULYsoggm1a3w3wgW7nhGNrE2B2jXV1eN31fNueI_nDI9URYvERLeLNpCYFKICSx-OgsYveYJCvfMkTkAMzLACrbGpJ0a6dWENhLVOt12gaYkN10gdPf2EZX5MgFspzoGBhVZVFJcecTvrm2cYp89185Y5ENOqbytCYyv91oT-C_y8Cee_p9LJsGS-Qwj160FrLstTQIpyLrQXwsxixHVvVgyM0Ew8LHu4LXNStQY4sZyjkkVFmSmKbR7i21KpxLQ75JLzX8REAHwdgz6MuSzHGWC07hS4hnsi4yoOM9ty4bPGIDpesJsZCYzTecMBQq7ND4axv8-WG0hgXB27VHgTeREEWJN9RMQO4SWvyhgbnkMTn7C9fWMKn1H_JrXdPQ0JQ8FdrYQyGd7wRJonsHG-xQVCXbBsh4TD1ZdqDMS4TXoPWTZeCyXW0ljp_miYK85LK7lftR7RSthCiZb5Ne3gkKYKTBbCtZ8_42wTGfK0NFj9LYY715Q5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9276455e9f.mp4?token=lhNpNYCmGA1Nu7PKB2QvEyLCryX9_T2VbMAEuPeE71CLLabELYlx2JdnMC2LGqxUS7f8CwRqWFhWAjUmRrdZYKXL9_steQvwevZ3OAEx7p7_iLeuHIE1eI17Y1OxUPO4lG90nup39CKKQqtV3vayPGUB3X12XyTv-n7PPw4ECqCahapVDo6bULYsoggm1a3w3wgW7nhGNrE2B2jXV1eN31fNueI_nDI9URYvERLeLNpCYFKICSx-OgsYveYJCvfMkTkAMzLACrbGpJ0a6dWENhLVOt12gaYkN10gdPf2EZX5MgFspzoGBhVZVFJcecTvrm2cYp89185Y5ENOqbytCYyv91oT-C_y8Cee_p9LJsGS-Qwj160FrLstTQIpyLrQXwsxixHVvVgyM0Ew8LHu4LXNStQY4sZyjkkVFmSmKbR7i21KpxLQ75JLzX8REAHwdgz6MuSzHGWC07hS4hnsi4yoOM9ty4bPGIDpesJsZCYzTecMBQq7ND4axv8-WG0hgXB27VHgTeREEWJN9RMQO4SWvyhgbnkMTn7C9fWMKn1H_JrXdPQ0JQ8FdrYQyGd7wRJonsHG-xQVCXbBsh4TD1ZdqDMS4TXoPWTZeCyXW0ljp_miYK85LK7lftR7RSthCiZb5Ne3gkKYKTBbCtZ8_42wTGfK0NFj9LYY715Q5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
نتائج الحرب على إيران.. النفط يصل إلى 94 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88228" target="_blank">📅 20:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88227">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-_Kq70Aov4GhXOOfdRY5Q6Ju2cLe-PCWpyZkY0bO32YFoWWVrft3Y81yZS76GVnm-3PWnaWVnfIGJDECq5mAf86vvruRVcqwAEm1kjaXQpHCo3J6eIGjrLguSvscdkBzdYuJTFHO_Q4-NQg0e13AOvBwVPsfQpHFHZRvLiLu6quNQlnOFKy35wsTHUqMjWRLgdxabAOeihlE3sB62iJKwh4AEnGUfffYJX6wl0EOnMPmvbGFCc1R6N8zCsPcxRhKxTimOa_afAVupYEQ_1S_JCcNeki2kv_a34YfsemrEynhqXin3AXkzBLFsURH-E3FtGDdkbocvVPrulFt1eh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المحور الإماراتي في العراق يرد على زيارة قاليباف بصورة فوتوشوب  من تجيب قاليباف من كبيسة</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88227" target="_blank">📅 20:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88226">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الخزانة الأمريكي بيسنت بشأن إيران
: سنفرض أشد العقوبات في التاريخ، وسنسقط هذا النظام.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88226" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88225">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
🇮🇷
محمد باقر
قاليباف:
- كنا مع العراقيين أخوة وأصدقاء في أصعب الظروف.
- عمق الروابط بين العراق وإيران متجذرة في التاريخ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88225" target="_blank">📅 18:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88223">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4VuWeh0zXogkChqksQAnsJcG1PaewAEFlXpaycrSyo0Iz4ZN7C59suRQRdV-1BYAAplb8vlyXBdAoD4f4yBKTs3p6NRyuBa2xCFHY7NXIQ6AOM3vgRpxso2ytPWFRsh47nZf8Q9XSGfjiylHXl2GNws8WhcvP3vF-eblZvbH60dWNfvxGyoEjziH67AZkMsX_T71b89GYugMFZu1IYjDXoHv3HBOx7qmFFVM3qFzQcgKac8rdmk3Sq-dxE9bEVdLF5CGiEoOElXtNFnmZjHO2XZW6ve74smFzSwoCmFIP61xvTFYUQb9Z6epV9Gw69NnF3SiD6YDfATm5bdX_Kn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية:
تزامناً مع ذكرى انقلاب 28 مرداد 1332، أقدمت الحكومة الأمريكية على فرض عقوبات اقتصادية وتجارية واسعة النطاق على الشعب الإيراني. ويُعد هذا الإجراء دليلاً آخر على استمرار العداء والخصومة التي ينتهجها صانعو السياسات الأمريكيون تجاه الشعب الإيراني منذ 73 عاماً، كما يثبت الطبيعة المعادية للإنسانية والمخالفة للقانون والاستكبارية للحكومة الأمريكية.
ولا شك أن العقوبات الاقتصادية الأمريكية على إيران، والتي استهدفت الحقوق الإنسانية الأساسية للمواطنين الإيرانيين، تمثل مصداقاً لـ«الإرهاب الاقتصادي» و«الجريمة ضد الإنسانية»، وإن مرتكبي هذه العقوبات والآمرين بها يستحقون المحاكمة والعقاب بسبب ارتكابهم مثل هذه الجرائم الشنيعة.
إن هذه العقوبات، التي تأتي عقب الحروب المفروضة التي استمرت عاماً ونصف العام، وكذلك الحرب التي استمرت 12 يوماً مؤخراً بين الولايات المتحدة والكيان الصهيوني ضد إيران، وبعد فشلهم في تحقيق أهدافهم المتمثلة بإجبار الشعب الإيراني على الاستسلام أمام مطامعهم غير القانونية واللاإنسانية، تستهدف الجمهورية الإسلامية الإيرانية، لكنها لن تُحدث أدنى تأثير في عزم الإيرانيين على حماية استقلال إيران وعزتها وسيادتها الوطنية.
إن فرض العقوبات والضغط الاقتصادي هو الوجه الآخر للحرب والعدوان العسكري، وإدمان الولايات المتحدة المرضي على هذين الأسلوبين لم يعرّض السلام والأمن العالميين للتهديد فحسب، بل تسبب أيضاً في انحطاط أخلاقي غير مسبوق للحضارة الإنسانية. وبناءً على ذلك، فإن أي دولة تؤمن بمبادئ وأهداف ميثاق الأمم المتحدة، ومن بينها مبدأ احترام السيادة الوطنية للدول، لا يمكنها أن تبقى غير مبالية إزاء استمرار خرق الولايات المتحدة للقانون وممارستها العدوانية العلنية تجاه القواعد الأساسية للنظام الدولي.
إن إقدام الولايات المتحدة على الإعلان المثير عن العقوبات الجديدة، رغم أنه يُعد اعترافاً صريحاً بارتكاب جريمة ضد الإنسانية، يمثل استمراراً لسياسة سبق اختبارها وفشلت، وإن إعادة اختبارها مجدداً لن تؤدي بالتأكيد إلا إلى تكرار إخفاقات الماضي وفضيحة مصممي هذه السياسة ومنفذيها. وبطبيعة الحال، ستقع مسؤولية نتائج هذه السياسة وتبعاتها على عاتق الحكومة الأمريكية ومصمميها ومنفذيها.
وتؤكد وزارة الخارجية، مع إدانتها الشديدة لإقدام الولايات المتحدة على تشديد العقوبات غير القانونية والمعادية للإنسانية ضد الشعب الإيراني، أن الجمهورية الإسلامية الإيرانية ثابتة ومصممة على الدفاع عن أمنها ومصالحها الوطنية ومواجهة الهجمات والضغوط العسكرية والاقتصادية والسياسية والنفسية الأمريكية.
وستواصل الجمهورية الإسلامية الإيرانية، بالاعتماد على قدراتها المحلية، وبالنظر إلى تجارب سبعة عقود من المقاومة الشاملة في مواجهة سياسة الضغط الأقصى والعدوان العسكري والإرهاب الحكومي الأمريكي ضد إيران، استخدام جميع الأدوات والقدرات المتاحة لردع شرور العدو الأمريكي-الصهيوني وحماية المصالح الوطنية الإيرانية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88223" target="_blank">📅 18:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88222">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نايا-NAYA</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/88222" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
مناشدة عبر بوت نايا:  نحن مجموعة من صناع المحتوى نناشد الهنود والباكستانيين بالانتقال من الرياض الى نجران. نحن من بعد الله نعتمد عليكم في توثيق الانفجارات والدك اليمني على رؤوس ال سعود ومصالحهم الاقتصادية. نرجو منكم النزوح الى نجران والجنوب خلال الفترة المقبلة…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88222" target="_blank">📅 18:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88221">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇱
اعلام العدو:
يراقب المسؤولون الأمنيون الإسرائيليون الأتراك ليس فقط على البر، بل في المجال البحري أيضاً. ووفقاً للمصادر، تُرسل تركيا سفناً حربية إلى مناطق في الشرق الأوسط لم تتواجد فيها من قبل، وذلك لإظهار وجودها، وفي بعض الحالات على مقربة من السفن الحربية الإسرائيلية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88221" target="_blank">📅 18:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88220">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">القوات المسلحة اليمنية تنفذ عمليتين عسكريتين بطائرتين مسيرتين الأولى استهدفت هدفاً حساساً للعدو السعودي في مطار نجران والأخرى استهدفت أرامكو نجران وقد حققت العمليتان هدفيهما بنجاح ردا على انتهاك العدو السعودي لأجواء محافظة صعدة بطيرانه المسير</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88220" target="_blank">📅 17:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88219">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88219" target="_blank">📅 17:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88218">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/88218" target="_blank">📅 17:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDye8s4aFQW9NTkjVmA4sEFDhxLbCQkjqQfTG7MtshkxH-3C-hTfyY0GZQCz7Qrna2dFFTpFPGY8EATszrBTToLbLMEFES9bZmlFEh23iiysNUSCXB1v9JrJgSl5gpxRH43ett9iojLTti5r9yAIaUs3QafD3_HGtNXUUCbqH6496Hz7C2Bnp1a4j2VbkWk00f8UNgZq7_VFzk8ELPuVDzVnxxsHpqX8ZhiQV-QLpVBW0wyOufMi1xMLxCm4P4_ndEUxitYWk8SbvenL5ayNdZ0U9Y-ARB6bQhbhgRn7DJhXpA9utTZi6KzKVSeBJotnI0G6-ZKU21c9OADbnMAN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية تغلق الموقع الرئيس لشركة كورك في العاصمة بغداد وثلاثة مراكز مبيعات أخرى.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88217" target="_blank">📅 17:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88216">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وصول رئيس مجلس الشورى في الجمهورية الإسلامية الإيرانية السيد محمد باقر قاليباف والوفد المرافق له الى محافظة كربلاء المقدسة
🇮🇶
اخوتنا قدوتنا
🇮🇷</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88216" target="_blank">📅 16:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88215">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
قوة امنية تداهم مصرف الرافدين الحكومي فرع السعدون وسط العاصمة بغداد واعتقال موظفة كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88215" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88214">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKPlDQwFJoPZ20sGT7enlGYB0rTjsCD5VdckuB3dka2FMuvS3RuX9cEX_yKjmLOpz0LNMow9qNpZNFQn4Ue-WLWytqnrgqW5YWn5-YsfUIjvEBv_XxRR6U721DYScFqZoRTudrKHx3L5b8mfVvF6nZgONk7tsT-6iCZO8EmrX_w896QascwVnB-O3Hm1BkSu289ZJVxo_6vkAxUXOuSNHE0_mmEUY3IKIFV9Tv41K8a5l7pskvfU5Yp40CgONr6wN58LWY49LQlhxIG1mdgLGBURSSGj7CvsmRMgKpzm0xPeFiZQFyr2dnGuZi10GiMulUiR444StlRU99RuHKv5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المحور الإماراتي في العراق يرد على زيارة قاليباف بصورة فوتوشوب
من تجيب قاليباف من كبيسة</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88214" target="_blank">📅 13:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88213">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">السلام على أبا الفضل العباس</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88213" target="_blank">📅 13:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88212">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/88212" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88212" target="_blank">📅 13:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=MSaFCQh1bHoBIX5Zv5psLPf2w2Eo6KkOuXuoPg68vX8S8EVwgkdaUA65QAvNHeniVwoPBtWjnsiWtl1rgn89OzlT9V0kMUOkyVCziMrJMH0pYb9CiVpgZ04WYeTYDi4VT0HIjkdonl9tAeeoQ2ns1eb7vSubUHd5AFnTad3YQas1UfHGxegLXZ022d0J0tn8n08SwZ6i1W-Ssb9EGXNEEM9OatfbIjWbcoeR_JObj8ER-lX6pY96n_jvTBLzg2PNw_LgWn2Lr1LDN3lyyEPyVz1rUvXXf7UQjX_ya6Z1zLPCOLnRQ_qsOISiCE0B2A_Hk92l1nHqebTPnE9YT9OFNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=MSaFCQh1bHoBIX5Zv5psLPf2w2Eo6KkOuXuoPg68vX8S8EVwgkdaUA65QAvNHeniVwoPBtWjnsiWtl1rgn89OzlT9V0kMUOkyVCziMrJMH0pYb9CiVpgZ04WYeTYDi4VT0HIjkdonl9tAeeoQ2ns1eb7vSubUHd5AFnTad3YQas1UfHGxegLXZ022d0J0tn8n08SwZ6i1W-Ssb9EGXNEEM9OatfbIjWbcoeR_JObj8ER-lX6pY96n_jvTBLzg2PNw_LgWn2Lr1LDN3lyyEPyVz1rUvXXf7UQjX_ya6Z1zLPCOLnRQ_qsOISiCE0B2A_Hk92l1nHqebTPnE9YT9OFNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88211" target="_blank">📅 13:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbpKjSNi7_SKwYP6ykCM6pxdoZUh8n_GEg0RfbyTZiE0uUUe0Xcu8pwxPh8pkSmEglE8MzeNykfyBSzDscEy7y5vfCZcncW0VVna_h4Ld_Es0skZ2q4qD1d6qm_8NLdph9GMK5i0VWut0a0hRPAoDnknpS8_3MumT8gbCPSdldBnOMjpq-cGkVJeMZtI2v_k8gMyRQ49BMlRDXi9Jzi7a3R5zEOgxJW24l3ifMzA1KoL8TbtrPQ2y9BFBbBe2hWSah3c0ID-VUZ0AAwgnydJgPmwie9qUh_sQ4VMlX_6zQp__kAAKM_hNhTzkVZOFmThPOhF2lKuYsoFteHGSJM34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
فالح الفياض: تغريدة المتحدث الامني باسم الكتـائب هي "رسائل خشنة"</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88210" target="_blank">📅 13:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryT8sW8F96T8WvIJiujAbdvB-J4nW9vELZ2yp8N9llgbWxxX2WXAE7OZhwvUbMkneaRgJeV226OQ1GZ_E2SmpNwpBJjB7y0Kscr5gpLUsuFaxEDY8agU5NEO2EuVyhiRGA1uBaMGyln8-n-CCVbB6c79dznwLg-1Grt7dHVUoUJh9Q3Dklpq1AzjhXwZ-2Qe-BpR66Ww-tw2XVr4gjO5u7NVVJ8Zae0w1efWGp7At72aS0wHB78TFmtJNfKN87Y_5OEpS0xJZx4XtfKHLU8R4-TyJzeaR6XdsjxxQ8N3sN42Ty57U62hEyuoC2mRxy3Em-f4v5dc8VnvHQPnnq8LWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حدث امني قبالة السواحل اليمنية..
سفن صغيرة تقترب من حاملة نفط شرق المكلا في اليمن والأخيرة تطلق نداء إستغاثة.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88209" target="_blank">📅 13:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLoMFzPhIMGPW2hWPDiHRC8bIMkaSkZ3px-LXuXdwjdgWuUQYxRfJHmWxrQnqknAUg7e3DOE7KhFM3ap7WUABbBiH9ibV2lxIueYTwUvZJ_q6EcVhbLDHA4edXYElfjsZeKtknEUMvOo6TaSmvFqeb3Iv4ZRooq0CbVc5tQx23iszRZ8UTLSFKw0JBodTinHVoS0hmQn62_f_4LvuF-UvpL3kLUnQn-c_IU1Lyg_YOvh31SKao4eJSfwxpl_Scm357JutLUZ831gd3ME7ZtutgHo_G_X4LYTRvYrH29fMh-jYdGCsOHBvVYZuQpF7G3CjcZj5vAAdyCG8HgpBdwC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إبراهيم عزيزي:
تحركاتكم تخضع لمراقبتنا الدقيقة.
أي خطأ في الحساب أو خطأ متكرر ستكون له عواقب وخيمة عليكم أكثر من ذي قبل.
أنهوا وجودكم المشؤوم في المنطقة قبل فوات الأوان، واستسلموا للنظام الإيراني الجديد في المنطقة.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88208" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88207">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
وزير الخارجية العماني: المرور الآمن عبر مضيق هرمز لا يمكن فصله عن استقرار أمن المنطقة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88207" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88206">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
مع إستمرار التوتر في المنطقة وسيطرة إيران على مضيق هرمز.. أسعار النفط العالمية تحلق نحو 93 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88206" target="_blank">📅 12:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88205">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇹🇷
‏
الدفاع التركية:
لم يكن أي وفد عسكري تركي في مطار أبو الظهور قبل أو أثناء القصف الإسرائيلي.
على إسرائيل وقف الهجمات المتهورة والالتزام بالقانون الدولي من أجل الاستقرار في المنطقة.
تركيا تتعهد حماية سيادة سوريا وسلامة أراضيها.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88205" target="_blank">📅 12:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88204">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1579180dfb.mp4?token=K2_YWAWGgVT1E_najN-kqbxFbwXdMIjKcNKTctViXXLZemDBX6NMlGPlL5Ec0H6wXSvsL0rhlbiEJDqOsNwgZEKJWy-calDJYF9STtrR6f9vg6xjLY96WoSRKe9wy9_AJ5P05rxd-71h-1zlHZcl7drAWVd0cqzqOrA47YHkUPplN0BPGPyvlgpRjbCDxgWOkFRSolCIZZUfU_Of9fl2Txj2J_LkpDlmfXhQaJYqF5mPHmoiteCcENung7r20c7Vd1k0Ge2CTVW7A-BBHHHpElMtWoyemsv1c6Uv8nV_0-uML94XDDCtBoFR6ScvM2mk5CyikEVohtSbgLSHHU1n8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1579180dfb.mp4?token=K2_YWAWGgVT1E_najN-kqbxFbwXdMIjKcNKTctViXXLZemDBX6NMlGPlL5Ec0H6wXSvsL0rhlbiEJDqOsNwgZEKJWy-calDJYF9STtrR6f9vg6xjLY96WoSRKe9wy9_AJ5P05rxd-71h-1zlHZcl7drAWVd0cqzqOrA47YHkUPplN0BPGPyvlgpRjbCDxgWOkFRSolCIZZUfU_Of9fl2Txj2J_LkpDlmfXhQaJYqF5mPHmoiteCcENung7r20c7Vd1k0Ge2CTVW7A-BBHHHpElMtWoyemsv1c6Uv8nV_0-uML94XDDCtBoFR6ScvM2mk5CyikEVohtSbgLSHHU1n8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
العلاقات العامة لمصفاة النفط في طهران:
اعمدة الدخان في سماء طهران ناتجة عن حريق طال صهريجين لتعبئة ونقل المنتجات النفطية داخل محيط مصفاة النفط بالعاصمة طهران، ولايوجد أي حريق داخل المصفاة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88204" target="_blank">📅 11:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88203">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
الإعلام البريطاني:
قام مرتزق مدعوم من الإمارات العربية المتحدة، واسمه أبراهام غولان، بتنفيذ عملية مراقبة سرية في لندن عام 2016، استهدفت الناشط البريطاني العراقي أنس التكريتي، الذي كانت أبو ظبي تعتبره مرتبطًا بالإخوان المسلمين من خلال مؤسسته البحثية، مؤسسة قرطبة.
قام غولان، الذي نفذ سابقًا عمليات اغتيال في اليمن لصالح الإمارات العربية المتحدة، بجمع معلومات تفصيلية عن منزل التكريتي ومكانه للعمل وتحركاته، وناقش احتمال قتله.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88203" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88202">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atJcekQ-7mlDcLaGusOSRuzuhgi1brIixPDHhCwui-RDMxZJX5ShfP58RfNN8rvHWf1TEdLa3KTpiCXakZckbV0w1C8WNwPmkGt0Pz_RT8iPLWE4AfN8m3iTces-YmfpLVrtHTreunTbi72gGDVrtnKrh4NPUtGxZPF2icJrVTebSnAc5TY3Tdu4Nj_rTDKBGpblwLZ6AE_dREZvSpyhgDuCiYXqCECpzdy_n-3bFI7GMGWlQl73cVtWdcKMezyM8TNz-qd2YL3gnPLTRnMpqAnMfjqkjuHp7ZtSnI93yeWRutLVlCQfIfMOcQ-YO93wskgnp9KiIKQIDeNNIPhBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مع إستمرار التوتر في المنطقة وسيطرة إيران على مضيق هرمز..
أسعار النفط العالمية تحلق نحو 93 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88202" target="_blank">📅 10:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88201">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLEA3kC5PESHNl_0LWqhidsWwk11N-z2rsVXY_oKuyFWNEIwEF59aKd2-TF3C4YFCQksEr_zURhwemyJa4h-l2bm2aAy1nuUIxQ-JY6t7ZzoYQhqJVOUZ49AGIPmqGTqj9I3pdzq1E8q3pufuOWbzxZPBRfUX2Famh063dgR5FB7pDtAFB-KODBzP1DaPL4kCQbJzVleCCzeIQqqQFEtVSUfiVrPo1-aba7x9sWPYahIGPZIkW8NxNzL1VEz0yRzFRKeKuJ5FckxAIzQbGT64UpXu5SKAghB5PsB6cnUjk-LZ8R-lVYEjDhKNOdJQ68LksKULc1tP5FC92hH9KpvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس القضاء الأعلى القاضي فائق زيدان يستقبل رئيس مجلس الشورى الإسلامي الإيراني محمد باقر قاليباف.
#أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88201" target="_blank">📅 09:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMtUXxN5NKAXOcmIFtd2rXreC-eTUFa9_6vm7aE-lEZ8CgDtKQgG-_0k563Yi-0FXxdajwvpvv-u2__pNXPtc94TEs9bglarU0WoDVm83CviEfBoXIgE5Xfw9EdzDhUNaLecGQ0nQrgcilxnkwm6FUvqrsmCmNqIHXoNfFzL2VWBaEjxho4G4Xq2eAxZDYlGkg_dybkUCf4Yjd0kXbGKDYq-r0WAQloU9gTMXSOx12tb3L9UvBaR683RjMrBDqqJ2SPIqomPaJSUK0kCCm20IG-U-_047zPUicTyqPnwgZvKaGiatzO05cFpMg1CcEjR0VXUOxQTmjc_dmJlnXBI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: لم يمنح أحد جمهورية إيران الإسلامية فرصة أكبر مني لعقد صفقة. وللأسف، فقد فشلوا في اغتنامها. لذلك، أعلن اليوم عن العملية الاقتصادية الأكثر سحقًا على الإطلاق ضد أي دولة! ستكون هذه حربًا اقتصادية وعزلة على نطاق غير مسبوق. لقد دُمر أسطولهم البحري، وقُضي…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88200" target="_blank">📅 09:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRBX0zB-KB2RtqUESI12zDn709wAu29x3kCF03HekAbCi_UuvbT95Qsy7FaUNYxw8Gu7xwuEV0-reuV_cJkH8biawqEVizx9Pk0ApleEWzQNWgDeAFNcRRKchbqRfx0Er-cAzCZ3XhWpFx9n3y1s2u32brA2Z-itaf2cuz7e2bNLBU5FQY74m6Suk2GfQwd2CH2SFH64Hp5VBy6UcqeyjpXsPfIoxraZXMDxgp7iviLhMcVIyeVZ8uLcG602r6SpsTcTkWpvjh7zoJoV8GPG5T7wN5ClyKGvX2107S_C0XUhV4raJTsp89MrRjU542LO9JlbLslLIhdotuzB35Ihlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇹🇷
وزير الحرب الإسرائيلي "يسرائيل كاتس":
أردوغان يجر تركيا إلى مغامرات خطيرة في سوريا. لن تسمح إسرائيل لأي طرف بتهديد أمنها.
سيكون من الأفضل لأردوغان أن يواصل إلقاء خطابات جوفاء وخيالية ضد إسرائيل في البرلمان التركي، بدلاً من اختبار عزيمة إسرائيل على الدفاع عن نفسها.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88199" target="_blank">📅 08:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامب: لم يمنح أحد جمهورية إيران الإسلامية فرصة أكبر مني لعقد صفقة. وللأسف، فقد فشلوا في اغتنامها. لذلك، أعلن اليوم عن العملية الاقتصادية الأكثر سحقًا على الإطلاق ضد أي دولة! ستكون هذه حربًا اقتصادية وعزلة على نطاق غير مسبوق. لقد دُمر أسطولهم البحري، وقُضي…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/88198" target="_blank">📅 02:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUd2pttvN3bPSQ4ycQF6tB91Io6ga1v_PprLnH0xSzowIeE80Yg85fx8SBJTUrvjkXlPMip6mP66etkIdPGf8l5IuopZMrHlSdyQ1NppfAIu0UfZZ7ZMGuEbRcar0oG8N1mh4QCs9y1SSONR15nIrKCHK-iSlps1cRj8uBSmPDj5aLdNfl1EGC1UnocqkNQ41f64s5cG8kTA70FKN_lHvRjzPJSBoxMzKXrtkPskSnCeDNy6u-D4dzpS9vbglk1sUTf3oTVxHhaOhO9ODCXrv774G59WA_IYNq9xsJ27JUBHxeQ2LExopDo8mRdIovvmh4Lato20oHdBIRueFsoIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
لم يمنح أحد جمهورية إيران الإسلامية فرصة أكبر مني لعقد صفقة. وللأسف، فقد فشلوا في اغتنامها. لذلك، أعلن اليوم عن العملية الاقتصادية الأكثر سحقًا على الإطلاق ضد أي دولة! ستكون هذه حربًا اقتصادية وعزلة على نطاق غير مسبوق. لقد دُمر أسطولهم البحري، وقُضي على قواتهم الجوية، وأصبحت مصانعهم العسكرية ركامًا، وعملتهم لا قيمة لها، وبلادهم على وشك الانهيار. كما أعلن اليوم أن أي دولة تسمح لمؤسساتها المالية أو شركاتها أو مطاراتها أو كياناتها الحكومية بتقديم أي نوع من الدعم لإيران ستواجه عواقب اقتصادية وخيمة. تهريب النفط، وخطوط المقايضة، والتحويلات النقدية، ومكاتب الصرافة، وسجلات السفن، والشركات الوهمية - يجب أن يتوقف كل هذا الآن أنتم تعرفون أنفسكم. سيكون هذا يومًا حاسمًا اقتصاديًا، ونحن بحاجة إلى وقوف جميع حلفائنا إلى جانب الولايات المتحدة الأمريكية لعزل التهديد الإيراني وهزيمته. هؤلاء المجانين على وشك الانهيار، وهذه الإجراءات التاريخية ستشلّهم وتقضي على قدرتهم على بثّ الرعب في جميع أنحاء العالم. لن تمتلك إيران أبدًا سلاحًا نوويًا. شكرًا لكم على اهتمامكم بهذا الأمر</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/88197" target="_blank">📅 02:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇸🇾
تحليق طيران حربي وتفعيل دفاعات جوية في أجواء قاعدة كويرس العسكرية بمحافظة حلب السورية.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/88196" target="_blank">📅 01:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BG7RsI4RlDtQftYUDb7TWYd6UuMBCoIPRpTY7i8xbZSNqrgILoHC7411Ty0MawtWHx4FueqQQ-jkiSg38ARP-PH_Zx_rruGMNO02N0yVa_jIlGWyiQu0Iq-RahLlnXAlH-rIlmT0KvQxrZsEVHEteMjOr09LyyiZ63qtD1pnKTogILi_LhrfmGJFfgdWvWvPsYJMJ-bRsfPSohu5ERLEfVgK7lN8I0pPOBgg9aKA0UelSe2LdtujbsJfs-ajp4z4wI5CPz3V5IBThCIatDbxnYSfAChuPx-4drLPyeioytuyKWAqsFH0kz8_eeq0D9q2DMFw19Db8kj19EG_Zwfrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
اتفاقية منتصف المدة قادمة إلى دالاس، تكساس، في 9 و10 سبتمبر. سيكون تجمعا لم يسبق له مثيل - لا يصدق!
لأول مرة على الإطلاق، سيجتمع الجمهوريون من جميع أنحاء بلدنا العظيم في مؤتمر منتصف المدة للاحتفال بانتصاراتنا الهائلة ونجاحنا، وعرض مرشحينا المذهلين، والاستعداد لأهم انتخابات منتصف المدة في التاريخ. حركتنا أكبر وأفضل وأقوى من أي وقت مضى. لقد جعلنا أمريكا عظيمة مرة أخرى، وسنحتفل بهذا النجاح الهائل وغير المسبوق تماما! يحاول المجنون اليساري الراديكالي تدمير بلدنا، لكنهم فشلوا، ولن ينجحوا أبدا، ما لم نسمح بحدوث ذلك - ولن نفعل ذلك!
سنفوز بجوائز منتصف المدة، ونحمي بلدنا ونعتز به، ونجعله أعظم من أي وقت مضى. كن هناك، 9 و10 سبتمبر - لن يكون مثل أي شيء آخر. ستكون الموسيقى والإثارة وأهمية هذه الأمسية في مستويات لم يسبق لها مثيل في مؤتمر أو حدث سياسي. سأكون معك في كلتا الليلتين، وسأذهب. أراك في دالاس!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/88195" target="_blank">📅 01:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88193">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇱
‏بريطانيا تستدعي القائم بالأعمال الإسرائيلي بسبب المشروع الاستيطاني E1، وتعلن أنها ستفرض عقوبات ردا على التوسع الاستيطاني الإسرائيلي.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/88193" target="_blank">📅 01:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇸🇾
‏
وزير خارجية الجولاني:
لم تكن هناك نية لإنشاء قاعدة تركية في مطار أبو الظهور.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/88192" target="_blank">📅 01:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88191">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
رئيس هيئة الحشد الشعبي السيد فالح الفياض:  المنطقة تواجه حالة من عدم الاستقرار واقتصاد سيء جراء الحرب الأمريكية الصهيونية، والجمهورية الإسلامية تعرضت لحرب شبه عالمية واستطاعت التماسك في مواجهة التحديات،تم استهداف الحشد الشعبي كوسيلة ضغط على فصائل المقاومة،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/88191" target="_blank">📅 00:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88190">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
رئيس هيئة الحشد الشعبي السيد فالح الفياض:
المنطقة تواجه حالة من عدم الاستقرار واقتصاد سيء جراء الحرب الأمريكية الصهيونية، والجمهورية الإسلامية تعرضت لحرب شبه عالمية واستطاعت التماسك في مواجهة التحديات،تم استهداف الحشد الشعبي كوسيلة ضغط على فصائل المقاومة، الحشد الشعبي موجود في كل المناطق الحساسة والخطرة، وهو عامل اطمئنان للجميع، الحشد الشعبي وحد العراقيين وأجهض الطائفية من خلال منح الجميع فرصة الدفاع عن مناطقهم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/88190" target="_blank">📅 00:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88189">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇦
🇷🇺
عمدة كييف:
"انفجارات في العاصمة. كييف تتعرض لهجوم باليستي.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/88189" target="_blank">📅 00:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88188">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
الخزانة الاميركية: ‏
تجاوز الدين الفيدرالي الأمريكي 40 تريليون دولار في 19 أغسطس/آب، مع توقعات بأن يتجاوز الإنفاق الحكومي الإيرادات بأكثر من تريليوني دولار هذا العام، وأن تتجاوز مدفوعات الفائدة السنوية تريليون دولار. وتُعدّ الفائدة الآن ثاني أكبر بند إنفاق حكومي، بعد الضمان الاجتماعي فقط.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88188" target="_blank">📅 00:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88187">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
مدير مديرية الإعلام الحربي في هيئة الحشد الشعبي مهند العقابي:  ٣٠ أيلول هو يوم سيادي للعراق كون المقرر فيه إنهاء الوجود الأجنبي في العراق  هناك ماكنة ثالثة قد تكون إعلامية أو ثقافية أو سياسية تحاول التشويش على هذه المناسبة  هناك دعايات تحاول التشويش على…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88187" target="_blank">📅 00:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTGbNJF81pLNqHZtmOvXsZS5r5R3pic4NPFE9OvwUTTPEvTwBfu5xAqLWPPG9hC7c-cEewnP9lzWFBbqYS-Cl4djvdAxpxAthSK6G4IDXcaOGGDX-mS68VIVCG5s_ae3QUWo51n-jlOjZFQ65PeJ5MFinvOhgZJrAzHJpnlIh8PtqMyyocXgfS5Ue2-UPgDSy4RwoiHIDqKXBKe3eFpYhZel3n_7sO9ZofyF8VreBF6GgY3a2CS22reXuxMnj0r-EZL_jRTizS_SMOFFo2NVkWbed2eTBPsrGNssJo1f-9GpuGoDyvicGf-Ida5RCSTy6WYRsHKpur4nZtmhUV8gnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
حصيلة عمليات القوات المسلحة اليمنية منذ إعلان قرار حظر الملاحة البحرية على العدو السعودي في ٢٠ يوليو حتى ١٩ أغسطس.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88186" target="_blank">📅 23:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88185">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
مدير مديرية الإعلام الحربي في هيئة الحشد الشعبي مهند العقابي:
٣٠ أيلول هو يوم سيادي للعراق كون المقرر فيه إنهاء الوجود الأجنبي في العراق
هناك ماكنة ثالثة قد تكون إعلامية أو ثقافية أو سياسية تحاول التشويش على هذه المناسبة
هناك دعايات تحاول التشويش على هذه المناسبة الكبيرة للعراق
30 أيلول حدث تاريخي ومنجز اشتركت فيه العديد من الأطراف
ما ينعم به البلد حالياً من أمن واستقرار هو بفضل الأجهزة الأمنية العراقية
هناك من يحاول خلط الأوراق بشأن ملف حصر السلاح بيد الدولة
يفترض بالعراقيين أن يحتفلوا في يوم 30 أيلول لأنه يوم سيادة وفرح
الحشد الشعبي يتقدم يومياً ويصبح أكثر قوة من ناحية العدد والتدريب والتنظيم والتسليح والتجهيز
الحشد الشعبي سندٌ للقوات الأمنية
نأمل إقرار قانون الحشد الشعبي في الأيام المقبلة
فصائل المقاومة حريصة على النظام السياسي
هناك أطراف تحاول تأزيم الموقف بشأن حصر السلاح
نستغرب الحديث عن وقوع مواجهات أو صدامات بعد 30 أيلول
لن يصل العراقيون إلى مرحلة الصدام فيما بينهم
نحرص على إدامة الاستقرار الذي يشهده العراق</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88185" target="_blank">📅 23:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88184">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
‏ترمب: التفاوض مع الإيرانيين حاليا مضيعة للوقت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88184" target="_blank">📅 23:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88183">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">س: ما هي الإجراءات الأخرى التي يمكن فرضها على إيران؟  ترامب: حسنًا، لدينا إجراءات يمكننا فرضها. لدينا عقوبات قاسية جدًا، وسنرى ما سيحدث الآن. الممر المائي مفتوح، وهناك العديد من السفن التي تمر عبره. لكن الناس لا يبلغون عن ذلك. وقد يؤدي ذلك إلى إبطاء الأمور...</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88183" target="_blank">📅 23:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88182">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f05a9fd75c.mp4?token=RrSe9QxgsFlHL8ZRJCFn7Vn9Diwczlxaa5DRFmS6X9EVqH8lL7b1si8HCvsDMc3IHfrMFookDjq6c2ToNi6wdMy4tEfmZHd-1tnOVp27EVhz4Fir8a2DTInXAe2us4FIPK-z3-uvsSRWCbsiUEU8V_nDb8wqiFMVqodiEBMznDceRod_cde2WIc4Yj9OPodEOSCcEJ4lr4o_LbyXat3EfgbU6M8P38uQBJ5SbzCWGTdRNoE27wnpq8-ExMn-x9hU5tzT_srTB_sq3sro77cyvv58Qa2y0hOIhquPCu1E_tUZ4GyU2SdxTCvBFWYqcckLyiW8v26JKyfug7K2c5b_0znxFTRnKPkEREhDUrAUMMHzSeDWFerCqAsGH51iTnVUIbfGGhtuBh_Fz5VF-VY1KdWMyVGkDTmuBiKcGHOyQFZqIkDSWpaubHxf0_KPzjUDhrAPdPdCqQDm8rZ0mmX7fK_ziqLZq1Cpih0xkB_h8he5DB39AXh32v0X6q47rkG6ZAPGjymllPQ_4BNEFCXDFeGteZXT4yDVwrhZUSNPWBVqzH5wMgC9OIPBpE99VHwHSSBHk0BpueQ6jU3wfBYizVtfXdQjB6inLzvv05QFeJdpZ0h4SoboBSacRhgJYgCC2eR_nW5b2ePz60Uz7pjhYoCsIV1WIMxM4jT8XGVcd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f05a9fd75c.mp4?token=RrSe9QxgsFlHL8ZRJCFn7Vn9Diwczlxaa5DRFmS6X9EVqH8lL7b1si8HCvsDMc3IHfrMFookDjq6c2ToNi6wdMy4tEfmZHd-1tnOVp27EVhz4Fir8a2DTInXAe2us4FIPK-z3-uvsSRWCbsiUEU8V_nDb8wqiFMVqodiEBMznDceRod_cde2WIc4Yj9OPodEOSCcEJ4lr4o_LbyXat3EfgbU6M8P38uQBJ5SbzCWGTdRNoE27wnpq8-ExMn-x9hU5tzT_srTB_sq3sro77cyvv58Qa2y0hOIhquPCu1E_tUZ4GyU2SdxTCvBFWYqcckLyiW8v26JKyfug7K2c5b_0znxFTRnKPkEREhDUrAUMMHzSeDWFerCqAsGH51iTnVUIbfGGhtuBh_Fz5VF-VY1KdWMyVGkDTmuBiKcGHOyQFZqIkDSWpaubHxf0_KPzjUDhrAPdPdCqQDm8rZ0mmX7fK_ziqLZq1Cpih0xkB_h8he5DB39AXh32v0X6q47rkG6ZAPGjymllPQ_4BNEFCXDFeGteZXT4yDVwrhZUSNPWBVqzH5wMgC9OIPBpE99VHwHSSBHk0BpueQ6jU3wfBYizVtfXdQjB6inLzvv05QFeJdpZ0h4SoboBSacRhgJYgCC2eR_nW5b2ePz60Uz7pjhYoCsIV1WIMxM4jT8XGVcd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: لم تكن الصفقة مع إيران كما قالوا، ولن يكون مضيق هرمز بنفس الأهمية التي كان عليها في الماضي.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88182" target="_blank">📅 23:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88181">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce1c50722f.mp4?token=gULQ1aXCSRlZPilhndLJPXKH78aRJBI1zzYLul5IgND14Zex58Fa3YAUYJPB0VHZRpJu8MqivgES_M8EMN_wR7NPXbt-6nMEoteWIV7n-lbW5nc3Yu4zxT5OdsIsEvkh0AfzhvRpT1HCVwFEB6Pod0Rx9BEABq4MpFW8fIasTsKEZCqrseDg6Du5zLAG68T6x8SbiyPlBGKYzJpR0v9cv4aGtQtp6vXLj0dOuBDQucPiCKZUlyg14E5pcSI2hs78Y_n9LjJuECy3qpHg-jgDMf6gmwoqqmV3P2CNtFQESXTkVlfLQ4ms3ShbDwzTf-wZRl0EYMoCLYtvKJhMZQJXsqhcRrHT4n8lu0u42BOEdXuBan4EiN0eadSTUaKhomnOsiSctVC2B95wrReI5Q7JpwAOOQra5aRapU0DkpIJ4O9TWMHgdCNj8s9D1uq6xCo8K40iR_RdYOr6lv_mWtpGgI5fI3nsuR0CSlixTEcjP15nmYyuW4Cnbw7_uFYXCN5u5Is95snxHrcscIAFgWIC_TZQArqXxSRZnktELf6cEAT3ms2mne9xsIcin81uSlbN61_CJfyC8hjMnsql-GwsGtdM-1Qz9DsF_cE9VWaW72cqQyLaZGDCVHDZJODZf0IipEPz4Drb_NtKkGByTwmz5_yKDbZ6f3HSYSvCY-ORl4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce1c50722f.mp4?token=gULQ1aXCSRlZPilhndLJPXKH78aRJBI1zzYLul5IgND14Zex58Fa3YAUYJPB0VHZRpJu8MqivgES_M8EMN_wR7NPXbt-6nMEoteWIV7n-lbW5nc3Yu4zxT5OdsIsEvkh0AfzhvRpT1HCVwFEB6Pod0Rx9BEABq4MpFW8fIasTsKEZCqrseDg6Du5zLAG68T6x8SbiyPlBGKYzJpR0v9cv4aGtQtp6vXLj0dOuBDQucPiCKZUlyg14E5pcSI2hs78Y_n9LjJuECy3qpHg-jgDMf6gmwoqqmV3P2CNtFQESXTkVlfLQ4ms3ShbDwzTf-wZRl0EYMoCLYtvKJhMZQJXsqhcRrHT4n8lu0u42BOEdXuBan4EiN0eadSTUaKhomnOsiSctVC2B95wrReI5Q7JpwAOOQra5aRapU0DkpIJ4O9TWMHgdCNj8s9D1uq6xCo8K40iR_RdYOr6lv_mWtpGgI5fI3nsuR0CSlixTEcjP15nmYyuW4Cnbw7_uFYXCN5u5Is95snxHrcscIAFgWIC_TZQArqXxSRZnktELf6cEAT3ms2mne9xsIcin81uSlbN61_CJfyC8hjMnsql-GwsGtdM-1Qz9DsF_cE9VWaW72cqQyLaZGDCVHDZJODZf0IipEPz4Drb_NtKkGByTwmz5_yKDbZ6f3HSYSvCY-ORl4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب
: لم تكن الصفقة مع إيران كما قالوا، ولن يكون مضيق هرمز بنفس الأهمية التي كان عليها في الماضي.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88181" target="_blank">📅 23:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88180">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الولايات المتحدة تجري عملية سرية لنقل النفط عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88180" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88178">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-poll">
<h4>📊 كمواطن عراقي ماذا يهمك اكثر ؟!🇮🇶</h4>
<ul>
<li>✓ نزع السلاح</li>
<li>✓ توفير بانزين وكاز في المحطات</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88178" target="_blank">📅 22:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88177">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB4K-w_McDV--mCQLNigLOS5Zc6lzXqu508I1skUhBYIp-3trsm-OlLT1P9HAS0ArTTcxzEBOsygwaxO7z1B1K2H8hmvl7g0-crNscZDSi2lf8hVvXnQoY7dsHXy_T_QFWW4RU0gG0unbwfqxBbURg_rIm-EZqYN5fpJuFnyFKofKXLe8lQ2MthH08zXyU1xw3A8unwUQ-1CYPbCOavuyzl_pYbOU_Q8KzvCgXMK0lvm7uEuuF00tVIKIxuEheWMNYtjGQdLuw2wzvaiLc6DaDh1TMd7_k9PR2CYGze2AxgR-bfhOcIubJ9cemqL9jl42RgT19DYY_x91-Ibxuc1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية تقرر منع سجاد سالم من الظهور لمدة 90 يوم</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88177" target="_blank">📅 21:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88176">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
🇺🇸
بسبب هزيمتهم النفسية من ايران
إعلام أمريكي : ‏تقدم وحدة تابعة للجيش الأمريكي في ولاية جورجيا لجنودها تصريحًا لمدة أربعة أيام للعب لعبة GTA 6 كحافز لإعادة التجنيد. وقد اختار عشرون جنديًا هذا الحافز بالفعل .</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88176" target="_blank">📅 21:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88175">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
نتن ياهو:
لن نتسامح مع وجود عسكري تركي في سوريا يهدد إسرائيل. لقد أوضحنا الرسالة بشكل جليّ: لا تفعل. يبدو أنهم لم يسمعوا ذلك بوضوح كافٍ، لذلك تأكدنا من أنهم فهموه بشكل أفضل.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88175" target="_blank">📅 20:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88174">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
جهاز الأمن الوطني العراقي في قضاء الشرقاط ضمن محافظة صلاح الدين شمالي البلاد يلقي القبض على شخص قام بوضع مادة سامة في خزان ماء الطبخ في احدى المطاعم الامر الذي تسبب بـ(250) حالة تسمم.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88174" target="_blank">📅 20:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88173">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇱
🇸🇾
رويترز:
رئيس الموساد الإسرائيلي رومان جوفمان أجرى مكالمة هاتفية مع وزير الخارجية السوري أسعد الشيباني في 14 أغسطس وناقش الوجود التركي في سوريا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88173" target="_blank">📅 20:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88172">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية تصدر حزمة عقوبات بحق قناة الفلوجة:  - إيقاف بث برنامج حوار التاسعة لمدة (10) أيام تبدأ من تاريخ صدور قرارنا هذا المخالفته لائحة قواعد البث الإعلامي  - منع الظهور الإعلامي بحق مقدم البرنامج السيد (علي فرحان) لمدة (10) أيام…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88172" target="_blank">📅 19:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88171">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e275d7a197.mp4?token=GqBXrOSF_C1sgvPuJnjbCUoy-cKHFGCircOwvcQw9pl4ESSCC7B08yn1_ke36n5NovuciURyPSvKFtzh8v9P3oX47ttyZte_55Bz26lH-ntMuiewyxRjO1BBTJpftWHdR2bGMuL9jslq6OwRB24W0rDjomCaV9tQsrZHttKod0lkBg1Iqq7iWY5BTvlKpFcVl-RISppZe6xPdyVKlPVI_sttk0Y3EVy7GkIQ_dJjwQJUN4SH5b2MfnYjzQLFXv8lVf9tVoS2XeHZkPiT3zL0kSzHwNgOVD-tElHbOcXAPsWwVT2VjulZhIv1-y79rGNgdvvBIN5SCw0SyJmpx60fuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e275d7a197.mp4?token=GqBXrOSF_C1sgvPuJnjbCUoy-cKHFGCircOwvcQw9pl4ESSCC7B08yn1_ke36n5NovuciURyPSvKFtzh8v9P3oX47ttyZte_55Bz26lH-ntMuiewyxRjO1BBTJpftWHdR2bGMuL9jslq6OwRB24W0rDjomCaV9tQsrZHttKod0lkBg1Iqq7iWY5BTvlKpFcVl-RISppZe6xPdyVKlPVI_sttk0Y3EVy7GkIQ_dJjwQJUN4SH5b2MfnYjzQLFXv8lVf9tVoS2XeHZkPiT3zL0kSzHwNgOVD-tElHbOcXAPsWwVT2VjulZhIv1-y79rGNgdvvBIN5SCw0SyJmpx60fuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏يزعم ترامب أن الولايات المتحدة "تمتلك" مضيق هرمز</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88171" target="_blank">📅 19:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88170">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeefd4da47.mp4?token=Cvw7gQ-0ItA7sst5TNw_WhO-Vb22rAcRvh-eduHqlprtdKcDbyDGxaiOuhzOcTvPUrs-QoyVLDWqJtIlWdB_zGzDj5nKVIMC2yi_eeJslo3PZlAivNrFihaEBiL2I4sn2BStotvSUbUaRvDL9eDIr6bSMY-CgorwQ3_B_RivhFkqjaFkwAbL3XKGoNnFsPJ-DFLp-4z1bVHHuS54KCh35q-b4icZNvELW2rlw8s4j-Bwf7r7MTaBaWfI09YloANzWtA5LCwFKkkVRVs1BRS7CTy22y5Ssmpq5Ws6_tLMWjc_r9MLhXELYkreRYCfSJcmwOswI3S0GSBU7CPCuROITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeefd4da47.mp4?token=Cvw7gQ-0ItA7sst5TNw_WhO-Vb22rAcRvh-eduHqlprtdKcDbyDGxaiOuhzOcTvPUrs-QoyVLDWqJtIlWdB_zGzDj5nKVIMC2yi_eeJslo3PZlAivNrFihaEBiL2I4sn2BStotvSUbUaRvDL9eDIr6bSMY-CgorwQ3_B_RivhFkqjaFkwAbL3XKGoNnFsPJ-DFLp-4z1bVHHuS54KCh35q-b4icZNvELW2rlw8s4j-Bwf7r7MTaBaWfI09YloANzWtA5LCwFKkkVRVs1BRS7CTy22y5Ssmpq5Ws6_tLMWjc_r9MLhXELYkreRYCfSJcmwOswI3S0GSBU7CPCuROITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: هل تتبادلون الرسائل المكتوبة مع كيم جونغ أون؟  ‏ترامب: لا أستطيع أن أخبركم بذلك. لكن علاقتي به ممتازة. لديه 57 سلاحاً نووياً بالغ القوة. سيكون بخير.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88170" target="_blank">📅 19:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88169">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0db0a5c6.mp4?token=o80Zl35i-JLrsE8IM7G0aMJLiXAaFwlD_KF_9qLRgcaUBWyd14nvK2MDA1wnWCw9RmQvfijC4CBKD8-511q1hipGnYIyLHoq1G4pvz_vPmrocOScPU5y_hWM83uUu259PHmCrR_1dhMbmZ-AYZc0wp930u9YyNiOl5yh6cZ8hz0WnHLXzsH3s-pn0YSNjXoh_IEb0R4z1aTUMdqAqI_UzzZ-k9cZ7RWsErlmX4KJUNopukFxBZEBIlC1rC9cL2uon7l5uB7JgIA6y-HOz-shLDY0X4SgkgE8swnD3rcSu8w1o1SASxRz7A4khjkevrkP8HFHZfhQcO3c8Jd5j0y4AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0db0a5c6.mp4?token=o80Zl35i-JLrsE8IM7G0aMJLiXAaFwlD_KF_9qLRgcaUBWyd14nvK2MDA1wnWCw9RmQvfijC4CBKD8-511q1hipGnYIyLHoq1G4pvz_vPmrocOScPU5y_hWM83uUu259PHmCrR_1dhMbmZ-AYZc0wp930u9YyNiOl5yh6cZ8hz0WnHLXzsH3s-pn0YSNjXoh_IEb0R4z1aTUMdqAqI_UzzZ-k9cZ7RWsErlmX4KJUNopukFxBZEBIlC1rC9cL2uon7l5uB7JgIA6y-HOz-shLDY0X4SgkgE8swnD3rcSu8w1o1SASxRz7A4khjkevrkP8HFHZfhQcO3c8Jd5j0y4AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: تدفق النفط عبر مضيق هرمز لن يكون مثاليا، والمفاوضات قد تبدأ في وقت ما.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88169" target="_blank">📅 19:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88168">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
‏ترامب: لقد توصلنا إلى اتفاق مع كندا.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88168" target="_blank">📅 19:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88167">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
ترامب عن قاعة الاحتفالات الخاصة به: "سيكون لها سقف مقاوم للطائرات المسيّرة. وسيكون فوق السقف العديد من الطائرات المسيّرة، والتي ستحمي واشنطن العاصمة والبيت الأبيض. أمر في غاية الأهمية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88167" target="_blank">📅 18:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88166">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd7a4575d.mp4?token=Ga0dvf2NAum0QNZBSKXZwbnFxYVyDNem9VRr8I8DMwwdPHihBCPbGchPUPzJJmjdsB-Or2PlYyObOymU__t96q_he_0ZzLBaPS1As8IzDMYDvpJkah9_CcEKKZyX7uSYxy0LmOgXGnl6nSUmPOVwP8DJ8CrLIWN99aIMC9Nuw__keTWoE4RmMrJUmC7jI3QedUjEZzFvfcSQfpL1YZH71kuANUnS-RUlUzaJhOi1szczSbVjrEysaOhOcBN5hhFH0Yxo_Qg1tgTPnAb0_ZQHVzT_bqyDlfg5Vl7BHBlxiELM-mp80hBNwsxiblybBjWQ4yQ_KXpr6InH7-TcnHnbkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd7a4575d.mp4?token=Ga0dvf2NAum0QNZBSKXZwbnFxYVyDNem9VRr8I8DMwwdPHihBCPbGchPUPzJJmjdsB-Or2PlYyObOymU__t96q_he_0ZzLBaPS1As8IzDMYDvpJkah9_CcEKKZyX7uSYxy0LmOgXGnl6nSUmPOVwP8DJ8CrLIWN99aIMC9Nuw__keTWoE4RmMrJUmC7jI3QedUjEZzFvfcSQfpL1YZH71kuANUnS-RUlUzaJhOi1szczSbVjrEysaOhOcBN5hhFH0Yxo_Qg1tgTPnAb0_ZQHVzT_bqyDlfg5Vl7BHBlxiELM-mp80hBNwsxiblybBjWQ4yQ_KXpr6InH7-TcnHnbkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن قاعة الاحتفالات الخاصة به: "سيكون لها سقف مقاوم للطائرات المسيّرة. وسيكون فوق السقف العديد من الطائرات المسيّرة، والتي ستحمي واشنطن العاصمة والبيت الأبيض. أمر في غاية الأهمية.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88166" target="_blank">📅 18:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88165">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇪🇬
🇮🇷
وزير خارجية مصر:
هناك اتصالات مع إيران تتعلق بجهود خفض التصعيد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88165" target="_blank">📅 18:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88164">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
‏
ترامب
: بناء مهبط طائرات الهليكوبتر في البيت الأبيض تبرعت به شركة سيكورسكي.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88164" target="_blank">📅 18:28 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
