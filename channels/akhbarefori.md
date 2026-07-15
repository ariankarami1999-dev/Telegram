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
<img src="https://cdn4.telesco.pe/file/lFrN6vs2N8L2eKLbjCUVHztZ18qDw2l2LF2EwNurIJ63TcJWTpSmsyrcGSvydeVDd6FSZtgNUanLezaRCf_lvjRHViJDeMxQAyNXaU-Z6EQhV-WNqrBdosWID43fd533KHYGjtWghF5iMQRZYkryFgZ5BX9cu20WWdkf_J_zO111LXUvGYcnA_EuYYTzR7mZFxpaH_PtNTUpOsDTM99pBJsqOkgZFI9AgLpZrn05x8NFVwiYIsvsFWUXXwZMt7H8zKRJeyTI1Qa3wMrB7bCQmHq5YHb7Rwix7Lt20IVKmJbtfrzJgmVaOSAs4dzBr0gIggHc1qpg0_YdKbl9-vvH1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.39M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 12:35:10</div>
<hr>

<div class="tg-post" id="msg-671340">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
شهادت ۷ نفر از کارکنان پایور و وظیفه نیروی زمینی ارتش در بمپور
🔹
ارتش: پاسخ تجاوز ارتش تروریستی آمریکا به ایرانشهر را خواهیم داد.   #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/akhbarefori/671340" target="_blank">📅 12:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671339">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
منبع امنیتی عراقی به الجزیره: یک پهپاد ناشناس در نزدیکی بندر فاو در جنوب عراق سقوط کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/671339" target="_blank">📅 12:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671338">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
مسدودسازی ۱۳۰ میلیون دلار دارایی رمزارزی ایران توسط آمریکا
🔹
وزارت خزانه‌داری آمریکا ۱۳۰ میلیون دلار تتر متعلق به بانک مرکزی ایران را مسدود کرد؛ مجموع دارایی‌های مسدودشده منتسب به ایران توسط شرکت تتر از مارس ۲۰۲۵ به یک میلیارد دلار رسیده است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/671338" target="_blank">📅 12:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671337">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1f21ab0c.mp4?token=qbwOfXsnEzoxc6x69J8hAlWAnqfZNxpImIiSILKbNwh5xeg4dHrYqIK1rUwWC9MCkRrttmJ4Hb-hvUvrn0sZ45_qlwwVhLLBeE43zKS8ZYIHBw1rNxqQP94Fw62JO1wcqakFlD7mK2uLqvv8z1Pk7BImw1YMmh9Qb0-V4jry5YsT6b9AXLeCLixfgOpMmuYDVAopu2x7mfUDPeW2oIB0HTuWP5ZuZAdcoVpw4GydynrDplAxfylPhYxUVOay31QTCCw-ZoGszGHdi1Uop9Impy-WAn7iBI7ldosJtUQy309sX-5OVFVFLd4Inzqgzxj9ON0IazRWPqjiZrFcUeAfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1f21ab0c.mp4?token=qbwOfXsnEzoxc6x69J8hAlWAnqfZNxpImIiSILKbNwh5xeg4dHrYqIK1rUwWC9MCkRrttmJ4Hb-hvUvrn0sZ45_qlwwVhLLBeE43zKS8ZYIHBw1rNxqQP94Fw62JO1wcqakFlD7mK2uLqvv8z1Pk7BImw1YMmh9Qb0-V4jry5YsT6b9AXLeCLixfgOpMmuYDVAopu2x7mfUDPeW2oIB0HTuWP5ZuZAdcoVpw4GydynrDplAxfylPhYxUVOay31QTCCw-ZoGszGHdi1Uop9Impy-WAn7iBI7ldosJtUQy309sX-5OVFVFLd4Inzqgzxj9ON0IazRWPqjiZrFcUeAfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمو پورنگ وقتی اینارو گفت نمی‌دونست مادرش این برنامه رو هیچوقت نمیبینه...
❤️‍🩹
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/671337" target="_blank">📅 12:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671327">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwwcxXn852-ah8fPGSFBgLwbq04f731lci9SD-YLI78R39QUm7qGmpScc4TpU0TC91iONb9qDa9ULcBW8SC7dLK8rnQHIOsv3K6coau78H2lsK6v5olNmGGJlLxtXeLGdgHgzporhcYi5UjowV6raaGxtaTLabw4Z8re9Q79x1P47v1mwFgEsglP9TTbUaIWEj87hfeRkCLKEYBOUu22C9oW3aEGU8RAcQ6ELM0hkn4R_0Jmfe597MZ0f-3Ybmusa5Yhl-b8mrVZVUXc9jCF52nA1DHi37s-LpyemtfBbUsQA1CkAqHnxO32C1lFOqMLj6PbIN4Zk-0F1yt6p2aPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsmuT0hVFMzCcd53plhuZkcDVEbWb8wGosgDXpADI7OViDg65lX6JHJOF4j29HhwmhCEnZzDAV1CRLY2sdUairJpluFZYGhncR68JPFQzQ65RCGfPDppba__Sy6tp87Lg_7eevRxS4nw4qfkLMrJTmUBrZzcH44eo3Vfar3NCVQKXtxf8Pz_cWKGzWJ7N9AuKTTYAZsqMlmvtH6T58PHhWcYSWxE5uRSfVAk_tfACGHBytdiPT5xw3WkH4tRCUriq2M06RVaLEmlX0646seXa5elX-xjX-D9nVyiTTYmPPdf4l3dYtVrj1kLHmAesWlqIdhXEfLO9Dc8ET6KI74wqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcPhUonx0Fc0xBBtYI-7avZsAFD_UAw8Hl186RFMx0VZgIj5MLdb-OioATvqt0DONPmndA6ftMj2CDAdHAVB1sk6asT-fuVJqU1hSRTKkBRxORunfts9a25KIGtkei3Iahhqe1x6XdS_PG51EZTc35oczjEtO5rul8WNdH9O08UrSye9s8igwOwaYoFJKfkEX2u4x7CNu7hunsUV2F8yVWwff-km2X-Y7Io0M8SUSL2C0Qqo9FGYlPCdxJeUk_V7tFZOGujJOoRx1-JwqmCs-skkrSCaJ9Hds-4ZHhdIsOsr6W5iloJhquHh4SiozI9mUfZoqCkXght8NbBuUkEJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCYw3OTwTwdvnuUHN48zuNbmb5DAwJpvCEj3sjYmRmtWM0UzYzhQ3_a2LubJL3TeYq7cgF0ouueQlKJT3NqxsuWnPoHjbettBhONQzfAtP6nqdT2m5skj_tKUvka_z1-YRR9tCRXG4gG14-r9k8D1E3yspD01hsXHJj2zsnhUgp7h7_PXFuAMKhKBIY48vkSutruhGcQEtxbGvdFtKQMEiWvjbi-Cm_6i15PWxe6Ed20XjAowPAVBIBhuFVhZ9hfAbC9hzUU4-fwxB7zlR4Cnb3p2b-uwkHIcfp5LOm_oso_cLjTphJfB5LIJXr1aMzcOcUVSxdUKajcpVHqe2HH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRILQbGvPmzKilgnBub7chRLq7dh_CutptQb7dbsFR6RBmneX_gEynMf6pwXpJ1x8wd4K86z4-Mp_T7CSG9elZPnb4qbzYhyu9-E3rDz7OAsX3KzbbE9nquptA9jgiW0XWy3cnlNf17gADVIC4e1tRVNyWGIDlj6-230nelFRcAJEBuhNPxrWqZooGMbjiI43P5Yl2YIZDPsiCoooxHcTqqPxlrY1W364QiDW_Gvksz4-lvH97PRbeoO2XngtL4IjjgpWSEV8SxhL0RQKmNgLpHPBYmc0mawZME_TWENrZmZLc70gJpf2uiV7UcabSEmgh0UCVQTHzCx2y44lrUYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRU0bsGloPqpWw2MU_AgQyTCU9PY5cmM4Kl7NV4kgom0XahbLyQbbCKl5Hav0RgqPC8Flr51Iv2LwwrYLOsdFoKT2H1A2lvK908uB1Wnsb-qqKLFkYzjDQLb1BmYfPWm4EiLG2hLOu_BvMkA9Um6XZFeCxosPTcwcvsBl3Xs2vsyizB1aUmI5k1TuM8ihZY6US1Nac1frMGOr2PKyWLWGK3i2o0uJKjG2JLY7uoM3Bu_lFS-WIV5Np6-BZLSYQUuoVhPCgdvCGeP3e2TmbAJL8mqn7m3BshEQJESELXiCaSds2hzNYhEDXQO7o_jlXNGyfA5vrgLHB6glhsdzUqL2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-X0dF2UigedfME9Bue5dYu4eJaAWSf6MTtzuskH-IhQL-DgccbgZyr9fMkhdKEc-qqrU5Yp3yMgsI2YUjuWQAH7fCJlTTjVH7GbOKwXQEsLxYYJdtR4HjMvlSZTDG4HJQw8Zs4EaggZJ0XRa1h09QkPdzhbiqaGPKZrz75BtNxcW4BM1jiU5hBrg4pt_Ixyg_gxGo-oyuJ2g-4LFVI4ozkss0w6azTJO1GMdxpwsF4Mjbu-JBvGIo524KLF9DX8IxgThHv11gEogTnA3CKDgO5NMaetFovJ78as8J9chZkMB4A92NwweOhUJS-Es6jVFHSvQevx2AYxaP5XRsIfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4fRYdBuh15bLKtl1EpXK4k-H-Vxmy9JLjAl4ILB3riFlIYD74mM-4a_Idf_vc-y-bfw3yELiFl2yKchUYqyFvSP9LOBDZMU3gRcOFM6YO24kt66R8L8YaQ5hnpUEkxVA2kz1FtKv0WGNiE3Nos8cDeymQLaDp2E-aN_b5rnAXZewA8AFrkzN58508Tu0_nbzFB2aXJZO0QJisDphnZl-LYUBHjYUqLNwbYPpgmyu6s-Yy9cve8UXA1Vm2M7GhvEVqZqE38a2gsOowNmtcSsscVOqLH-fArceyZDsfilLT0bajqkN2E2bTSHgtW7s08-WFypN7sIJoGybmEkHe6Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGIfU6VhkP-vAkIwcpvBLUb5FdSd8bFHCQi-YbDXxwDiwfK5O_vZUiRZxyb4i2zmOiF-mU-q_l8s8FKuNA4bhBuPW5lkNYsTTyXmj4o6B3wjIR6HQ1h_gwQVW1T18S39iO-3ymkqirI_3IXnkpWQxrZrM2xh3EFE_LOLxPyDGNh2r1BESwiN_mOxi5g8ZEpCfbjEr1V8Dm7jmjdbOp_rtSMNvHS24DH3pAZlLBbyOdJqBOcbwAn-mBsCrdUPiA8iRdjA0bQtxyiEY78scpIrPJCPn1k83RawNYsI7pkUm9W75MnHpGYRpnDFGa1ZAEi4BBuFmdJU-oIfwsK5suVL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBN6HEkgGjMRDZe-xsHDqh5eJSpoPtGK4RufVrNg3RoR0qoRBrkZmQaCs6sW1WLnRK9f2u7W62zrJFLbWlh5d9DyCPN1DDxCnl0VSL9yimswe9bhUrBz_MDEcUThvpvhxCImEqLn3teUKPZWIPWntXHeVK4xxAuFkFKUmc8qGqH72_m0ld6vUHy8vETj2RUPKD5MWusK7UUR11MIh8h3jcIRIq50uVj8CVKXjAilIF22U42rk4rrqHtCXZ6dpeXTER6M27QizUBShxWAPRAlx2Uw5W6aWM4J1bETAfcaBLU2OMsIMo6raDhFZfQJj9SPVXxLrTsmkv15CFoZ3cNVbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت مخاطبان خبرفوری از قطعی برق در ساعاتی غیر از زمان‌بندی اعلام‌شده
🔸
اگر شما هم چنین تجربه‌ای داشته‌اید، از طریق الوفوری با ما در میان بگذارید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/671327" target="_blank">📅 12:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671325">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f635ba3.mp4?token=eAHUOgBwrkdO_TCL_INp6-OAi4VlA2fnHVUBBeJVayWMamNLKXq5_78-rOpDbFR0M9hTb-PSAPvc2aNp7yonIuAJJNgwIii3zMkYL_2xjgacsagUmUEckvGiMZPPswyFxQBTnLhDsISC_VSMWovGnN-prEqnU5aDAZ42PytUdEPrI6e8DxZoe7fdLRRlazIgdwduTkY_LKy2f39Co36MZvfmK-OTLxgQPorbFbw18LpPzji7FialQTugxZeagIrmBrth7OmA_XvngGL75mamwnOGoBss9dDrYRM2ZPbPp0ZC2Oi3fvrpsWZSQEnElcgAZfVRdWHhcBdjwkkIrr_-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f635ba3.mp4?token=eAHUOgBwrkdO_TCL_INp6-OAi4VlA2fnHVUBBeJVayWMamNLKXq5_78-rOpDbFR0M9hTb-PSAPvc2aNp7yonIuAJJNgwIii3zMkYL_2xjgacsagUmUEckvGiMZPPswyFxQBTnLhDsISC_VSMWovGnN-prEqnU5aDAZ42PytUdEPrI6e8DxZoe7fdLRRlazIgdwduTkY_LKy2f39Co36MZvfmK-OTLxgQPorbFbw18LpPzji7FialQTugxZeagIrmBrth7OmA_XvngGL75mamwnOGoBss9dDrYRM2ZPbPp0ZC2Oi3fvrpsWZSQEnElcgAZfVRdWHhcBdjwkkIrr_-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایش بی‌نقص اسپانیا، پایان رؤیای فرانسه؛ فینال منتظر آخرین مهمان است
▪️
قسمت چهاردهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/671325" target="_blank">📅 12:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671324">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بحرین: ما تحت حمله هوایی سنگین هستیم
نیروی دفاعی بحرین:
🔹
ما امروز صبح حملات هوایی ایران را رهگیری کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/671324" target="_blank">📅 12:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671323">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
محکومیت ۵ ساله نظامی صهیونیست به جرم ارتباط با ایران
🔹
دادگاه نظامی رژیم صهیونیستی یک نظامی صهیونیست را پس از اثبات جرم در برقراری ارتباط با یک عامل ایرانی، به ۵ سال زندان محکوم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/671323" target="_blank">📅 12:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671322">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8da24524.mp4?token=htoJBxaqXZS3CjgstVhg9SCJ7Gk-icFWOe7iY-fwEdE93Qu7C8pCRxC7ylEMKT4CWTkwMrZD4ObJBoZOKvB8D_ZBsNPpvJzqebdTslAuBEr5jtXdpnY0IEPcMpQBimNukuPynIytDwnGUpjPt2nq6NOPgVJrA3IrRnBGqt7aS2bUDHVOxL4mswNj1UZahdwJ9Gz09GUQGzJrNguqmn2yPcXlL1aj2P0LxBs7xzFXFGoUB-pK5csx0INPC5nCkbvOM1vlrD4hMdqwCwOMIfOnid1qJ2pOPP0CKQyTNPWPNJwACIHQcmzA4SCKIBFKrMJpbJg-1DnwDcjoOFMt-ChtGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8da24524.mp4?token=htoJBxaqXZS3CjgstVhg9SCJ7Gk-icFWOe7iY-fwEdE93Qu7C8pCRxC7ylEMKT4CWTkwMrZD4ObJBoZOKvB8D_ZBsNPpvJzqebdTslAuBEr5jtXdpnY0IEPcMpQBimNukuPynIytDwnGUpjPt2nq6NOPgVJrA3IrRnBGqt7aS2bUDHVOxL4mswNj1UZahdwJ9Gz09GUQGzJrNguqmn2yPcXlL1aj2P0LxBs7xzFXFGoUB-pK5csx0INPC5nCkbvOM1vlrD4hMdqwCwOMIfOnid1qJ2pOPP0CKQyTNPWPNJwACIHQcmzA4SCKIBFKrMJpbJg-1DnwDcjoOFMt-ChtGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نشانه‌های تروما‌های حل نشده چیه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/671322" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671321">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muWuwceaRlHwAM_qrt_Oc9OoLvqhiWLmJKxuOHMmJ-vajLGLJ3RiNtbMFALhnDhBkUVBX9UD4ue7pBrLTBJGXh5BKXa5mdfzcNN1n-ahR49Sy8raFCO2Lts5NutPdp_evuMFYz3jcIgs2Jze4E1a7wWm7bi7Y5iChOXaO9jheMuLCs5WsDrMj7hXP_a1_41YG5w5e7St2wTa48AnJwqMUdmWw3qbdximOqNF7W-vQ1cKHtCaaZbDAswureMPm2uW3mqTEwFRzvas6Sq1wonJWUBNz_cwXo5U-vpdwVGcYEghB0LelPkmjbQL6-JhLGLRQxXjxWJjizOVGwRZ9J7guQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی تدریجی با پول نقد
🔸
بیش از ۹۸ درصد از تعداد تراکنش‌های شبکه پرداخت در خرداد ۱۴۰۵ به خرید کالا و خدمات اختصاص داشته است.
🔸
حدود ۹۰.۳ درصد از ارزش این تراکنش‌ها نیز مربوط به خرید کالا و خدمات بوده است.
@amarfact</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/671321" target="_blank">📅 12:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671320">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cb57b80e.mp4?token=FeCuDId5_k6JOT_tyjty0KdOXnJd1OT6ZbulFv14-7zDJWVgPV1gV2A1EbPiKc3D5OZI0X-ZtjBo84NaUpoi-75ccLOry4bpk5mBL6qWGUPvLj9gh_Tz36k1SOvup424z5uAQEOjHvBm6xl5CdFUgX19uNh38rJgPi_yxhcEY-It_wGY3eT_8JZe8MAFQ5MfG8iDMZ5zjOYSrU3uDMgiaGyGmne8Tw-zt3QtjW5DHbAb1W-yYWDv9DCjcHABGobAy3ivFujQvUPsuxZxh2gKHIPa56St1KYOr4dgBc0gZdctdU5_XStRjCQrC4Di_l3l_kfmGppkWAkb9eXGP92R6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cb57b80e.mp4?token=FeCuDId5_k6JOT_tyjty0KdOXnJd1OT6ZbulFv14-7zDJWVgPV1gV2A1EbPiKc3D5OZI0X-ZtjBo84NaUpoi-75ccLOry4bpk5mBL6qWGUPvLj9gh_Tz36k1SOvup424z5uAQEOjHvBm6xl5CdFUgX19uNh38rJgPi_yxhcEY-It_wGY3eT_8JZe8MAFQ5MfG8iDMZ5zjOYSrU3uDMgiaGyGmne8Tw-zt3QtjW5DHbAb1W-yYWDv9DCjcHABGobAy3ivFujQvUPsuxZxh2gKHIPa56St1KYOr4dgBc0gZdctdU5_XStRjCQrC4Di_l3l_kfmGppkWAkb9eXGP92R6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله با انگیزه نفرت مذهبی در آمریکا: کارمند مسلمان در یوتا هدف ۱۵ ضربه چاقو قرار گرفت
پلیس ایالت یوتا:
🔹
فردی ۴۸ ساله در مرکز خریدی در سالت‌لیک‌سیتی، یک کارمند مسلمان را با انگیزه مذهبی و با ۱۵ ضربه چاقو به شدت مجروح کرد.
🔹
قربانی که تحت عمل جراحی قرار گرفته، در وضعیت پایدار است و ضارب توسط حاضران در محل دستگیر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/671320" target="_blank">📅 12:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671316">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNLZc0NbOeYi9CvokCoDzgfoZsfQ-iauWqp4YEdXX1b-p2mXOmUUGbd0lsTXME3SQYOEp2MGOYcs6MRctC8Ksw7KliKLhDa6KSYEslq9YkjRzyyYXZsn-0OQ5KMeWgWPZ3hnbNnmHx8Awehr3so6bBGYP7b9YmxRoG74Mqs71uHplK-S6Kz-4Hy6U1_vB2n2wSQNiZQ5lk2WUdb7jf9GYRxQjjr41W5bHvM1C0TZfDJbY8glG1Rp2qPEALk_bkuDp3zOmhIQ_xkNkadmDi-TeAwR4e_0IJPv8l3O87vKZglp650eW9pkD8MLa8XvZYv0A4vjE4yCm4VpVspFMUK-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrV6bxAMqVOjn1IBYxMoCLFzbdv84ie8o7f8F1zt_s5kG-bj0vxE3S4YPY2esGZ3Z2gWetvyRZcsx7oEE-Tux46SGFBlU1Caxtg3qRBaEUNIihwnBYfzFqcvvNfVSfgEUrL7JgDXiXUpY-3JprMo4L0-SPmSAPHvzeuLlEhMnW8GxnAJvcqYuhhf5kCIITaMwnZWodYFBby5KljpfM19NuVD_AcRwWQB28MbQqGOrI0LWE5WoD6wDpeE3vnC_r-DQibFPoaijPwmCGczHAUWTEzFXnFk1rulV-ajh1rmynDn7VSvV6H3GQ5M2ANC0Slq7If6ZR8K7HePw7cif74snQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrkTNdm70ZYmAdsqm9QQFhYQ3_5hED1QmPF0h4L2QaHqvaFHuweNdcF5bzm8zPapRr7uVMerGn5TU0hUbZxqo1OVx8oPNH_KOmiuOO_rd5l9EaG8FG7hmN9u9KwB7p2ieA9lTM13zJH4qH87KhmAuejbc2iIVd7u0dvLXwjE0c33DOfA28gfvohOkGKRQaBI8eL8yzUqyxsZAEsjXttfq5G5ylKd8Htsv9uu0nKS3TuDiLJeipMStyeZIW7pdx6q577ZZn-tW-hwHRTb3NDBV0abPiMlR_1IuDVAhDOJzyJ0FsVON_5fooYbARzA0wmAVr0nd0QF7YNNtPJpEkM34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cP6sX_U_vJFm1_dxJDv965v2Ekd3FgoIr-hQqImaiME2Ga-Xjf95_FmNExdOyxJeUZkTpTP0lQbTfSjwYl7WatUNM_7H0vzHthHs3AhjrRINwagIXCJGCvXSlnIFMSUQaBI4JArEfp8R_0b9vaRCTTUu2Dct8Fn53MCaJg7-qktI5oJLcpP-6b2gI0g9b9SM5mJLJaXKlHx89D9s91ldVkn2E-vjcwuUNHk61wNAp4LHccWdP2nf0Np1cjmzp4H6FvfumrgWup2nOi-hW3W4uTV6IxrukSM-bkhonFljnD_QmtEKwkttLV05c3OB9H17_EBwqUuxKK3TnTYjIuhjyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شکوه خیره‌کننده جنگل‌های هیرکانی
🔹
مجتبی صابری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/671316" target="_blank">📅 11:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671315">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تغییر مسیر استراتژیک نفتکش‌های ایرانی به سمت پاکستان
بلومبرگ:
🔹
دو نفتکش «رانی» و «آمیل» با مجموع بار یک میلیون بشکه نفت خام، مقصد خود را به بندر کراچی پاکستان تغییر داده‌اند.
🔹
این اقدام غیرمعمول، به نظر تلاشی برای یافتن پناهگاهی امن جهت توقف و انتظار، همزمان با تشدید محاصره دریایی ایالات متحده علیه ناوگان نفتی ایران ارزیابی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/671315" target="_blank">📅 11:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671314">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
آمار وزارت بهداشت از حملات اخیر: ۲۶۰ مجروح و ۲ شهید زن
🔹
در موج حملات اخیر بیش از ۲۶۰ تن مجروح شده‌اند که ۲۲۲ نفر از آنان تاکنون بهبود یافته و ترخیص شده‌اند؛ همچنین شمار شهدا شامل ۲ زن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/671314" target="_blank">📅 11:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671313">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a7487a4d.mp4?token=eU59q0zl1aIM-EEK0V-mc4LNL_z1mAGa7bzm6OahBaTLrhj_3rGXZIcXdgPldOZH1FvbuUw-p9hBYrH7qLSfrLpfJmPuO7sdZdF7eQdupcB2L8yEXw-cQxnUZodNyIQKcozaZbCVUL67mPB5awnDR1Bkg-U6A3Gjgvvno_eAMyxasooWhYfvfkQ5RogNdjEEbJCVTJnUNuUBFoiJb2G_6r_cNSGoGpxLNasrpQ2H0MEA8HiZfaAvfImOaDEaL7vMI_u4Ay3siP0Dei148KTr9-xS7WkefvREhlOthpEN41BU82sTP_Nlpvd2daQ_HzjSvkE3QgqXHKJsXVUpJu68sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a7487a4d.mp4?token=eU59q0zl1aIM-EEK0V-mc4LNL_z1mAGa7bzm6OahBaTLrhj_3rGXZIcXdgPldOZH1FvbuUw-p9hBYrH7qLSfrLpfJmPuO7sdZdF7eQdupcB2L8yEXw-cQxnUZodNyIQKcozaZbCVUL67mPB5awnDR1Bkg-U6A3Gjgvvno_eAMyxasooWhYfvfkQ5RogNdjEEbJCVTJnUNuUBFoiJb2G_6r_cNSGoGpxLNasrpQ2H0MEA8HiZfaAvfImOaDEaL7vMI_u4Ay3siP0Dei148KTr9-xS7WkefvREhlOthpEN41BU82sTP_Nlpvd2daQ_HzjSvkE3QgqXHKJsXVUpJu68sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله بوفالو در پارک یلوستون به پدربزرگ و نوه‌ای که قصد عکاسی داشتند، آن‌ها را با جراحات شدید راهی بیمارستان کرد
🦬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/671313" target="_blank">📅 11:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWNtybIXePrl1byoiIRPbBkVQqSumlD_iV5cPzxUss7bKhZouiJ1dVCydiiZt8AvP97BU0tSBG84FxxpC5WT8gSH2fiP9j2RcFiCRtAVWU08SFuIApEtC_vzPElKLykHNzhg_pebCLc6hTjfPUT5nkBAwGOCXmK49ih_1dbQse_Uzwnpg3JwFRH5hIRi9iqmZwBrgel4KfS3Hnq06aY9Ly83PexqIIcNwojyImWKjjqLOtmdm4SHGCEYNTuRnt6JO75YBKYu1-BWq_phqKWLOiezsH9F_aj79Rc9V8cJleL5XtiR9uE0meXRXyzVl3YVCfrLwWMQwo0PHTcl9HykPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهندس نظامی شرکت صهیونیستی رافائل بر اثر حملات ایران به هلاکت رسید
🔹
رسانه‌های صهیونیستی اذعان کردند که مایکل کاتز، مهندس نظامی شرکت تسلیحاتی صهیونیستی رافائل، بر اثر «جراحت‌های واردشده در حملات موشکی ایران به حیفا» در عملیات وعدهٔ صادق ۴ به هلاکت رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/671312" target="_blank">📅 11:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
آب تهران جیره‌بندی نمی‌شود
مدیرعامل شرکت آب و فاضلاب استان تهران:
🔹
تاکنون هیچ برنامه‌ای برای نوبت‌بندی قطع آب نداریم.
🔹
پیش بینی می‌کنیم با همکاری مردم در ماه‌های پیش رو مشکلی در تامین آب وجود نداشته باشد.
🔹
آمار مشترکان خوش مصرف در سه ماهه ابتدایی امسال نسبت به سال قبل، از ۲۹ درصد به ۵۴ درصد و مشترکان بسیار پرمصرف از ۸ درصد به ۲ درصد رسیده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/671311" target="_blank">📅 11:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671310">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb36b6e79.mp4?token=XOV45Z3IyQkIdYyxw_4ClfxJjeMk54ieyzWGwF_qw9bhvaL1RQc1vkRIXeO5i62ghsZDjEq5X9d2agLPoFDO_g_fyAmtWepo6BLzAD5dVUvXn5D4Q8XhyanfmEPk3eE1bD5_ng0MAYIFnwmu5jzK-CF4ZA-heUIO7Xm9LfuiEIZic2SqVq1TK-Vyc3a1kCqA5ZGnEtXx0p070mC2uOt2cCyWgJvht-VNiKV7Ch5do-fJ5lr_vbAnMVj0DBVZSaJFPGi-Wl5Xmo25UNAM-vVb9LZplp2Dmj5MTx46OttJ9ObSDWf6Jf9RTAOyUM6pfb7huej4STN8NnQc2FW-XONnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb36b6e79.mp4?token=XOV45Z3IyQkIdYyxw_4ClfxJjeMk54ieyzWGwF_qw9bhvaL1RQc1vkRIXeO5i62ghsZDjEq5X9d2agLPoFDO_g_fyAmtWepo6BLzAD5dVUvXn5D4Q8XhyanfmEPk3eE1bD5_ng0MAYIFnwmu5jzK-CF4ZA-heUIO7Xm9LfuiEIZic2SqVq1TK-Vyc3a1kCqA5ZGnEtXx0p070mC2uOt2cCyWgJvht-VNiKV7Ch5do-fJ5lr_vbAnMVj0DBVZSaJFPGi-Wl5Xmo25UNAM-vVb9LZplp2Dmj5MTx46OttJ9ObSDWf6Jf9RTAOyUM6pfb7huej4STN8NnQc2FW-XONnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آهوهای زیبا جزیره خارک که از ترس صداهای انفجار به خیابان‌ها و کنار مردم آمده‌اند
🥺
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/671310" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671309">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
بندر فجیره خاموش شد/ ۶ میلیون بشکه نفت از بازار حذف می‌شود
موسسه HFI:
🔹
بندر فجیره امارات که مهم‌ترین مرکز جابه‌جایی نفتکش‌ها در منطقه بود، پس از حمله موشکی سپاه به دو نفتکش(VLCC) از چرخه فعالیت خارج شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/671309" target="_blank">📅 11:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671308">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
الجولانی: اسرائیل با درج واژه عقب‌نشینی در هر توافقی مخالف است
رئیس موقت سوریه:
🔹
تل‌آویو با درج واژه عقب‌نشینی در هر توافقی مخالفت کرده و هنگامی که سوریه این موضوع را پیشنهاد داد، مذاکرات را متوقف کرد و حال که اسرائیل از عقب‌نشینی سر باز می‌زند، چرا باید با آن توافق‌نامه‌ای امضا کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/671308" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671307">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFDWZsRmYdzGKe1CTEbkIkKVuKl5awJFK7BRl3oN9k75GJvp9WLBqA0LhT1iITDOxTnZxdUxHrp54HL1ZUncNJuwuvN4cZQH-9oZR_05N1-nKrezvKVIhKzQfpfFOuNgluJtiVYrCqWyhXYbeGk0biEpEk65gpCap2Ma_vM1Hx7uk7fARhIUxprP_-L6URiPIudOCyLmr8DYH4uUcOpGYYGifF2QPsR59h25xdOvYcjio8tQZgqo-GS8Q3LRvmTt4qqKITil9vRjfkMYWLmUFzV74Xpdgw_8ITw3xcreW2HMnG_6HnL4i8rhax2oFIlkLceyHCcZUHqk5tKe5ceoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس فاش کرد؛ ترامپ در اتاق وضعیت برای حمله گسترده‌تر به ایران چه تصمیمی گرفت؟
🔹
همزمان با ورود جنگ ایران و آمریکا به مرحله‌ای تازه، دونالد ترامپ با برگزاری نشستی محرمانه در اتاق وضعیت کاخ سفید، سناریوی گسترش عملیات نظامی علیه ایران را با عالی‌ترین مقام‌های امنیتی و نظامی دولت خود بررسی کرد.
گزارش آکسیوس درباره تصمیمات خطرناک این جلسه را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230476</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/671307" target="_blank">📅 11:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671306">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تغییر زمان برگزاری ۳۸ آزمون به دلیل قطع ناگهانی برق
دانشگاه صنعتی شریف:
🔹
در پی قطع ناگهانی برق در روز دوشنبه ۲۲ تیرماه و خاموشی تمامی سرورهای دانشگاه از جمله بسترهای برگزاری امتحانات مجازی، زمان برگزاری ۳۸ آزمون دانشگاه که مربوط به روز ۲۳ تیرماه ۱۴۰۵ بود، به ۴ مردادماه ۱۴۰۵ تغییر یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/671306" target="_blank">📅 11:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671305">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
محکومیت ۵ ساله نظامی اسرائیلی به جرم ارتباط با ایران
🔹
دادگاه نظامی رژیم صهیونیستی یک سرباز اسرائیلی را پس از اثبات جرم در برقراری ارتباط با یک عامل ایرانی، به ۵ سال زندان محکوم کرد/ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/671305" target="_blank">📅 11:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671304">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX49HXaha9raM85hYX6kL_BxJtFYM01P1LNKH7ZACKfgK-2cUmG7WRHj3Yo9xzTddqfXqMz0KODxmvPPRHIBXxEtsj7xBSpnh1jqRujS0R0BETPd8A8vZS643OOD0GOgLORKAtoaXGrHnvPNRjXUknd68Z6-wjj0N501PQWbs8pmXmZkyTwsne05SFRvww89NT_-B3a45TBmbtaS62DZKtEkuJvDhkLedAstMBoAu-FfDfbaHKq5PHC-cElD_caCreMxxa4_XHY2vBsqVwZeek6tXQ0eQ4u2_N_QJ4oOHZYHUSlt7LCjoFe77RvN_9WrKAB-gRGorLM43UBsrPhQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسئولان با پشتوانه ملت، باید اصلی‌ترین مطالبه مردم، یعنی خونخواهی را در اولویت تصمیمات خود قرار دهند
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/671304" target="_blank">📅 11:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671303">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba0bed2bc.mp4?token=fv9jb9-s0IUjkjJHULp4Ov7Hc-N8g1Qjsxv-xbwQOdMF5CsFw-cFX6r54ULN8GA6e_RlEERzXqymHvsgz88lThWSQCskL0in5qEWYHIBKggqFmZkHtXDOQsdXa1vlCpGK1A_BmjWlJQLjvAe8lH7X56-LFjQ-KUex7D9tHpiwYGAIU4yk7Wl3wzsq9EuhrVcr4b7ar1HpVVvfD-v4HGmqwwfMGEFQCEkxlLx3eEG3oOoHyj0Y-e8RqoXyghgeS-MQGrTF7FielUKLpmUQdzoQ66ZdjuwQIUUv0b7TaYGVi_J6-NenGeEx7QtgvSktbUgaTPy-Z6YkN6Io4R4G8D0yjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba0bed2bc.mp4?token=fv9jb9-s0IUjkjJHULp4Ov7Hc-N8g1Qjsxv-xbwQOdMF5CsFw-cFX6r54ULN8GA6e_RlEERzXqymHvsgz88lThWSQCskL0in5qEWYHIBKggqFmZkHtXDOQsdXa1vlCpGK1A_BmjWlJQLjvAe8lH7X56-LFjQ-KUex7D9tHpiwYGAIU4yk7Wl3wzsq9EuhrVcr4b7ar1HpVVvfD-v4HGmqwwfMGEFQCEkxlLx3eEG3oOoHyj0Y-e8RqoXyghgeS-MQGrTF7FielUKLpmUQdzoQ66ZdjuwQIUUv0b7TaYGVi_J6-NenGeEx7QtgvSktbUgaTPy-Z6YkN6Io4R4G8D0yjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف تحلیلگران بی‌بی‌سی:
آمریکا با تشدید محاصره دریایی ایران، به اهداف خود نخواهد رسید؛ بعید است جمهوری اسلامی ایران دست از تنگه هرمز بردارد چراکه این کنترل، مبنای مادی هژمونی منطقه‌ای ایران را تامین خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/671303" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671302">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نمایندگان: مجلس طرح مدیریت تنگه هرمز را تصویب خواهد کرد.
🔹
قوه قضائیه: محمد امینی دهاقانی، عامل آتش‌زدن فرمانداری و کلانتری شهرستان دهاقان به دار مجازات آویخته شد.
🔹
رئیس سازمان فضایی ایران: اولین ماهواره راداری ساخت داخل با نام راد به زودی رونمایی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/671302" target="_blank">📅 10:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671301">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fd68a7fa.mp4?token=ZQ9Ku4m4sJrrE4qYpA5nKoijpICMpywPPCH0qNKUJ1c6f7BviXijqZc8V7DlR8IVH7nYh1brxdrjYxGHtUIgczCjOjqYcq91Pbadqy9FIPoGskR-L_JLjGYpfbggQfY8SL4W5A2RgNquAu-StlMYxCQeW6i9y70O-0MwZuxJIVP4ZB7ShEQQSwzMqLDrCNN-H-suPO2aV5UmwZgVDmRVMOC28pgu3n-8RaiG2-XtbZpQFeODfQcPTMBbUyJmmzsBrN6prJZwrftCnhwJxygD_1--Tiy5IKQW6k-o_aL2san_kMZlsEQKSELrh3u0gri3-RQQ9oneRdq1VpI9ysHeGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fd68a7fa.mp4?token=ZQ9Ku4m4sJrrE4qYpA5nKoijpICMpywPPCH0qNKUJ1c6f7BviXijqZc8V7DlR8IVH7nYh1brxdrjYxGHtUIgczCjOjqYcq91Pbadqy9FIPoGskR-L_JLjGYpfbggQfY8SL4W5A2RgNquAu-StlMYxCQeW6i9y70O-0MwZuxJIVP4ZB7ShEQQSwzMqLDrCNN-H-suPO2aV5UmwZgVDmRVMOC28pgu3n-8RaiG2-XtbZpQFeODfQcPTMBbUyJmmzsBrN6prJZwrftCnhwJxygD_1--Tiy5IKQW6k-o_aL2san_kMZlsEQKSELrh3u0gri3-RQQ9oneRdq1VpI9ysHeGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابستان امسال گرمتر از حد نرمال خود خواهد بود
رئیس مرکز ملی تغییر اقلیم هواشناسی:
🔹
با گسترش پدیده النینو در اقیانوس آرام در پاییز و زمستان امسال بارش‌های خوبی خواهیم داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/671301" target="_blank">📅 10:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671300">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
استانداری اصفهان: صدای انفجارهای احتمالی امروز در جنوب اصفهان، بهارستان و صفه ناشی از انفجارهای کنترل‌شده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/671300" target="_blank">📅 10:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671299">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmGUuy91IKpbsxcxppxVPjk1s43oFdM0EjAfCKrHmXxvYUly4Y5rAOI0z6hSEESRKqeN313ROjSLq8rH7ljJhWYq41KQyQigax8GmNn872RdW8KUdISdn6RZWrt8wVsIuHODYCvNqu0En_1uLZ04MEZz3xhyNbnwQf6sLcvcXIUtcIy1LH5CKpj8DFSbA27tyVsmAE8BfbuP8Ja-MGxLXHG929Vs4xT7iUnlmo0Ei1ePQ_tFZ9Jo-yYBQXEk11pgs4kPszj6nXvHJrLUgYVKQkYlHadUU_QhvyUUFQUTi4i13DrnptKDiORkh4ek3dqEpN9vHwjjx8LEvNytclr-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امارات سهم خود را گرفت
وال‌استریت ژورنال:
🔹
امارات پس از کمک به آمریکا در جنگ علیه ایران، از جمله مشارکت در اجرای ده‌ها حمله هوایی علیه ایران، در ازای آن به دسترسی گسترده‌تر به تراشه‌های هوش مصنوعی آمریکا و امتیازات ویژه دست یافته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671299" target="_blank">📅 10:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671298">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8lZRiQeM31Qo1ceVZrmhDEB6TuBJxcszCuml3meoXT34fENGJ1aM9MFw5nGDvlVsPvoeATOJ-SRgr5bM5SYnO6L44nYVIgWHWh6pOclNECUApDCUDzxXVdTQ9vDdYvlkiiz8p-25gR_vcLRu3z7m3C-_lu7crHCjD9T1LlK5YF6BFpmG-wFJrawHPigu3aU5m6k526T0Zmb45k07tr0UMFokTzI25x2B-_VMbKnptVdUxBtyXXa7MXRhomJvAbvaub6tzHo6B3wrQFFVcMdw4gd2bBuMKCRspiI7qcvkwlcVp7izJ2EWx6ekNpb-eI3IAixgUbINzO_-mh5isPWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضا صادقی، خواننده در واکنش به حمله وحشیانه آمریکا به جنوب ایران نوشت: اینجا خاک اجدادیِ منه، با جون نشد، با خون نگهش می‌داریم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671298" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671297">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYgAkUusUAJFBfRk-Im4u-iDCRLHb45GlNXOk4fhPk8_5cQhbBhqwEyQ8TBuhZ8SFmGrEOUr6XHEqjDdoNFBS7Om4Wa9FgIBVN6LC2tRhujCurtZO614RPuKefNqv7tfzjNYu4qyidblRYB6kruvYgb_w06qQdr6tnL1puic08LUr7nk8oVwiLshEIVS-eALfg_SNJNpZ2sm1eWlMaMEgeXUCkTHu8r02n2yWNYrrfzDmNQM8q8RGz2h6W0kv_K9DWMZKP4p7ztzUfLT-1ZMJ1lL4e7hVwh3rz_4-Xzg2bnCZt7vSTQjmKiqWgZD28Bg9_vUsoX8tzQIizdzd4so2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا لیندسی گراهام توسط رژیم صهیونیستی کشته شد تا ابزاری برای تهدید ترامپ برای ادامه جنگ با ایران باشد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671297" target="_blank">📅 10:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671296">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏆
حذف مدعی اول قهرمانی مقابل اسپانیا/ فرانسه با انبوهی از ستارگان به فینال نرسید
🇪🇸
2️⃣
🏆
0️⃣
🇫🇷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/671296" target="_blank">📅 10:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671295">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به پادگان ارتش در بمپور/ هنوز آمار دقیقی از خسارات و تلفات در بمپور در دست نیست
🔹
حدود ۳۰ الی ۳۵ دقیقه قبل بود که صدای چندین انفجار از این منطقه شنیده شد و حکایت از این داشت که جنگنده‌های کشور آمریکا به پادگان ارتش حمله کرده بودند. ظاهرا…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671295" target="_blank">📅 10:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671293">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
قسمت اول آموزش سلاح جنگی کلاشینکف
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671293" target="_blank">📅 10:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671291">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0GA5zfrNjoKH_2HUORy3xHVslB6gaGYW_5oIh6qaHsSXktJ-bXBxMNyjPARrwaj7Nx1TT6umehxEVpeszidZ2bhxUqs2OCDH9-ssvP4tiGSc9OkFMjZkwCXTJkvD9CTY7XNsJzEVVWoksgSTbJXQ9vvBwHIpKbsEI2EcXouru_hrpcv7xnAC-hEB-ZQOzMXevKkE57fWvsTwK6yrLxQqJHfnaaQvUOFM1iIJ7bqdHea0ruEftpY6-rXQFNKkpwpYqHwJs3Y5xyPyMEMD3AXu2jdQZtMRDNBVNgiD_HIva8XjzObQylyULq_NJdEZKqyAWQjeE_Z6jA8b3B0Y_DncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حذف‌شدگان جام جهانی
/
نفر بعدی مسی یا هری کین؟؟؟
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/671291" target="_blank">📅 10:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c819d1fb6.mp4?token=CIduZK8MvAq32yEeTUN4Tteyn2fffaIvhzSiLBfCou9svOBhDJ4gsHhjLGv_-uHIqSYroj3HvuKsZDHIBHU24nBWVaZeGZWEp28o0-6T2QqB11iCB0e5PtYLhXswVZ40xv1ui9krbefEBoSebkp7zvdyw0V0KrCe5YRxJjtSs0whnR02bHLrrlRwm_5D0ZqeMj2IbG_FIEc3tSkQLGWnKbQNL1phq2M2uQg2AaRmzuA_sfZ760rxvk3YdAoRQwjQmpG0_DN0VAh-J0MNYBp2k3t39Nq7U3_tN4SiudalAI-LpCR62gjKXvOinmaxSjrTYRTv7om964QTvCF8rXqz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c819d1fb6.mp4?token=CIduZK8MvAq32yEeTUN4Tteyn2fffaIvhzSiLBfCou9svOBhDJ4gsHhjLGv_-uHIqSYroj3HvuKsZDHIBHU24nBWVaZeGZWEp28o0-6T2QqB11iCB0e5PtYLhXswVZ40xv1ui9krbefEBoSebkp7zvdyw0V0KrCe5YRxJjtSs0whnR02bHLrrlRwm_5D0ZqeMj2IbG_FIEc3tSkQLGWnKbQNL1phq2M2uQg2AaRmzuA_sfZ760rxvk3YdAoRQwjQmpG0_DN0VAh-J0MNYBp2k3t39Nq7U3_tN4SiudalAI-LpCR62gjKXvOinmaxSjrTYRTv7om964QTvCF8rXqz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر اسبق ایران در روسیه:
مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد/ کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/671289" target="_blank">📅 10:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa6c6c7f0.mp4?token=Ee-iXpa7pDcH9wNbYaJDaiQzW8h8cXBeoTKOI3tz91-sdEkFgS_xagI_Zi0mLvywWIuIecn5SAnCCSGn0Jklz4e1gjfTm414w2oBVjq6zmYCYOZ2dzjsYKSmyKaWZpmy3_fVef_A0RgzA3JjIGKsQKAbBss3tyHiaLqsbyiDhzh45MCIQK8IKDuOHM40MDiWVbY4WchwO0_R7e_7EXE62v8YHGdhjSUV7_BitUqs4SW5kMSQ5z9D5iq9DUT-dEHwXaMlUhm6PTnQiplo-BzHu80VEX6H4dOOrY39lw0yuXqKJ7m_TKXHJTr0Inpj_xulE7N9rsSM7Wyo6SrUYdCmug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa6c6c7f0.mp4?token=Ee-iXpa7pDcH9wNbYaJDaiQzW8h8cXBeoTKOI3tz91-sdEkFgS_xagI_Zi0mLvywWIuIecn5SAnCCSGn0Jklz4e1gjfTm414w2oBVjq6zmYCYOZ2dzjsYKSmyKaWZpmy3_fVef_A0RgzA3JjIGKsQKAbBss3tyHiaLqsbyiDhzh45MCIQK8IKDuOHM40MDiWVbY4WchwO0_R7e_7EXE62v8YHGdhjSUV7_BitUqs4SW5kMSQ5z9D5iq9DUT-dEHwXaMlUhm6PTnQiplo-BzHu80VEX6H4dOOrY39lw0yuXqKJ7m_TKXHJTr0Inpj_xulE7N9rsSM7Wyo6SrUYdCmug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۹ مدل ساندویچ فوری و پرطرفدار برای روزهایی که زمان آشپزی نداری
🌭
#آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/671288" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671286">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شارژ کالابرگ کدهای ملی ۷، ۸ و ۹ از فردا
🔹
تمامی سرپرستان خانوار، از فردا می‌توانند با مراجعه به فروشگاه‌های طرف قرارداد، از اعتبار کالابرگ تیرماه خود استفاده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/671286" target="_blank">📅 09:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaauKcP3_KMlbKlSIHSrYIWMqGV4aKCFsFmipZp00lcx0uym9n6NXyMatTVS6b62Zkao7PuC9WGrR8TUqV-ipGcfmzeQQfBSD0jUbFG6eV7t2TC_kfcKkBq2DG18vsEIelunD8mg__36skO_-1Tpz9TTRIbos5DzukqWRtruFWZjD9cY2EPvEZqsOD3E0vNjfRXrM_oSeKxR3u97Qm6nWxINqdGcKz2YMThQoOei7ToePX8Dae3RdEnDOBmy8pExi4PTKX-YrzNF1o6pElJ1Q4XbMrVvW0RM6FDHBZPyXRYD_-k64O1u_cFA4cIgaZG2e6z5xnuE08TYBYV8D9y1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آپدیت جدید تلگرام با قابلیت Community و ویرایشگر پیشرفته متن منتشر شد
🔹
اولین ویژگی بزرگ، ویرایشگر متن پیشرفته (Rich Text Editor) برای کاربران پریمیوم است که اجازه نگارش مقالات طولانی تا بیش از ۳۲ هزار کاراکتر را همراه با جدول، لیست، نمودار و ابزارهای هوش مصنوعی می‌دهد. قابلیت دوم «جامعه» (Community) نام دارد که به کاربران اجازه می‌دهد چندین گروه، کانال و ربات مرتبط را در یک بخش واحد کنار هم قرار دهند و مدیریت بهتری روی دسترسی اعضا داشته باشند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/671284" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671283">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPJfXxatoDDYAVQfknJltvnWeBs7DVfu9sa2aqhXFu5hVPyHBQ0J-tF-7l3W34qJZUlldbaBK4nfaozFA2hLtRKbMnLTLbZV2i8ICcgmKHdcb_pN_A1OvHnzoKVqdnUyw1UHwObSCO29JbkEhYB0-rEC9VJ7MyLH_uKCE-9WTJ96ygMbJQsKfIRElV0cZXQiMBGY_n-JOXBzru9-zNZaIVuSZZD5Bw3ghoYHjOG4Idyh_RRrdD8jD5YheXGis9UNLPv64-BgrSfFXnTyLtqA0kW7UnZz1i9KZ3qENAGwZi9rio3zQbH_HE3N_NrLcONyh4x1WXG3o4hwJBkjpdbuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از کنار
این علائم ساده رد نشو!
🔹
بعضی از بیماری‌ها سال‌ها بدون اینکه متوجه بشیم، آروم‌آروم به بدن آسیب می‌زنند. اگر این نشانه‌ها رو به صورت مداوم تجربه می‌کنید، بهتره برای بررسی بیشتر به پزشک مراجعه کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/671283" target="_blank">📅 09:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671282">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
دقایقی پیش اهالی چابهار و کنارک از شنیده شدن ۶ انفجار شدید در این مناطق خبر دادند
🔹
هنوز محل این انفجارها مشخص نیست و نیروهای امنیتی در حال بررسی این موضوع هستند./ تسنیم  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671282" target="_blank">📅 09:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671281">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYci3H_kAfiIIFabk-Yuq_90K3_YkzfO-x_G0Z7xwgWe-1wvJv1ZqKxdFhaHC1l_cWS2PrXf6EOmrSYvN4m5Xsim38sw97O3yfDMmZ0-YE0CVbXqSEipnHFke96FoAIkFfGtWC-GJTjo1wLOv0XjLAiQjolrXb2z9wMiNG_haW_OMpZ8j2jxThVQ-fVVwtE7LjMIQVnJOEm0ybJPeDRm1tTx9BKdVpgVVH19z0FDgK9olcW2mNtjvugwGPyf5-_k06tX0rRnNBvvQlKT7LOkkmcqg6AhFLYVw1qqXVmJOXk2MaH03m5VVRas26CDZYehG1LXj5eE1PIXZQGjXHhprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام فدراسیون فوتبال فرانسه، زیدان رسما سرمربی تیم ملی این کشور شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/671281" target="_blank">📅 09:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671280">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842ffd17fd.mp4?token=qXOx2k1LDrg83uEGY59QtnYNQ_FlYdOitQk8eV45AYXPYDK9lvJqUCxCaZXn3wQ5Oxm0z5sPCTTDjHPJhxktbJOomSFNqhZ_yRyLu65JJrcx0H5UV-OaseZ6hGof9c93Kg23ixu3eo3dHj_PVKu3dyiGiP3FuaSbYmOru28HaffW504fSnW-bMwLn-PmsXishmIkGBKnttMNuz2X_GupxQuU86YCpfTCFbuBqGYrHJeQfHy1_KTJR9mpWKeLBmtz-iOZSTNJvnFoSQ53tz69bgABrzSfO4Mtp74qBGfWPuqBxCoGCxpa2JZssvjwOXC4xhqEKDyBBmauWISjQtaWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842ffd17fd.mp4?token=qXOx2k1LDrg83uEGY59QtnYNQ_FlYdOitQk8eV45AYXPYDK9lvJqUCxCaZXn3wQ5Oxm0z5sPCTTDjHPJhxktbJOomSFNqhZ_yRyLu65JJrcx0H5UV-OaseZ6hGof9c93Kg23ixu3eo3dHj_PVKu3dyiGiP3FuaSbYmOru28HaffW504fSnW-bMwLn-PmsXishmIkGBKnttMNuz2X_GupxQuU86YCpfTCFbuBqGYrHJeQfHy1_KTJR9mpWKeLBmtz-iOZSTNJvnFoSQ53tz69bgABrzSfO4Mtp74qBGfWPuqBxCoGCxpa2JZssvjwOXC4xhqEKDyBBmauWISjQtaWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم فلسطین در جشن صعود اسپانیا به فینال جام جهانی
🔹
هواداران تیم ملی اسپانیا پس از پیروزی برابر فرانسه و صعود به فینال جام جهانی، در جریان جشن‌های خیابانی پرچم فلسطین را به اهتزاز درآوردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/671280" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671278">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
مرشایمر: جنگ با ایران وارد مرحله «اقدام در برابر اقدام» شده است
استاد روابط بین‌الملل دانشگاه شیکاگو:
🔹
اگر از نردبان تشدید تنش بالاتر برویم، به نظر من این ایران است که دست بالا را خواهد داشت، نه ما. این فقط یکی از دلایلی بود که باعث شد پس از چهل روز، جنگ هوایی را متوقف کنیم.
🔹
تا این لحظه باید برای حامیان بازگشت به جنگ کاملا روشن شده باشد که ایران توان تحمل حجم عظیمی از فشار را دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/671278" target="_blank">📅 08:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671276">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTXx3qyxlWjEmCdjoF3kSKV-PUTdeYagk1k8zTps7fL8iUjcl6AsUXcgfUj7fMja5vdqvOmN-SKsACEEM9_T5052I1j_QkWYBpRKivrR53IP6yEwEcy6e6d_kBZeyaCb-V3j7VG9YuXyqCfUJwphMiXemL9nhZMFQAU_Auh9MCaVX6QAQRq6yJaKkhO2x45Tebu9c3sHtkMgNTzkeSKZk8WtXYlJpkm5Ar-C4dCkQWmTFsbV1DBWaapWENstGlPVXZYRC-sYTtQsCnzKMtelpCGJPE-Rht0rGhvYIsPV3uNfFIzxehRFt1D_IeHHAHUWohs-4vmEy2eRs-vFrO_LRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7yB9p9JtobnG2ejJok25YCduXXCEHXI5HDHBLmaVbwnGujpzhMP2wc9iJhsZrgV33tPOtdIZZlD4Se4fRBKWz17GHUVcUaYxyDm9yrvzifXwSoSpE2oTJzFXOJF-DuAkbFZITiF3eSjq_HsFf0mV8mTlxPWSsoYE701mzXWIKDd8bz4sueRl0TDekutp56JtQIM7rL-Z7gqlLtFkAcJd_SyAV23YLJU1xrng_vfd8FAnO2BHxWAKWLuBwILAxLCk8iKtIJGnUAvMYf5sYCn-m-E2J-VcSl1IClF18ZBQssKQlTOtEHT7rcmS5t1pyc-0XSz0oTAAochitU4FF2ARQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای از یک انبار متعلق به شرکت «کویت و گلف لینک هلدینگ» (KGL) در منطقه «مینا عبدالله» که مورد هدف قرار گرفته و به طور کامل تخریب شده است
🔹
این انبار، مرکز اصلی لجستیک و پشتیبانی ارتش ایالات متحده در غرب آسیا بوده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/671276" target="_blank">📅 08:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671275">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdRRZioz8kbLGgqJMhdYm1VcFkiI5FbKFMlPwjDXsE6b4bI967PKEey-pkMUM10KSOAnL-d2FYxv4RupI5_s9FTQ7AEPiw2__pVC--4Hu70vwHlpx0YOa5moaxSGrdASQKnaJiatnkN6Qv_ALVPoeYWWVLzB37dw9OtHXx5omtLeDpxo4DcIOSW03Z8uKPfAY5bYWzvuT4h17nwdy_chSBj4sH8gDlq9ayrP8M7AiVHe9KcBAuKt3zdcxiVHSwrVTROQj79Cff14aW3z3aW03fV1vbhZpjlDZaCFrlQcXsS59AGJy9iBOLFtpiykCQsU_Z5RvokQAsfaqe0D47cW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه‌های ساختمان با کیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/671275" target="_blank">📅 08:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671271">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dad1458dc.mp4?token=UkyHCSYD_MFgRqd5T6yAVv-I0VkG90SUPcpBBOFP8HI7YwR1pxDJxozoePqxJy_E07BgA8RIqT8iFA7aIWGwB648avV18svbhfI6y69hHkvgtBavvJiDffgswazdWj-MbUE5ANsAD1Hx4YURI8u00M4oORy9siepcEx4_F7x7QG74rAEsCYEBFS6pGVEIM2wp95vsMKYaARhYwNL0yrH5DF73noPPk6xyn8Cj2XW2DUEnHjNp7CsVkbEWUNprHS4aCeqWKYLDAiPIZeImupfSjJsHgdigfEyDVcSDZzerU9JrpD-2Rpa1A2ipmgTbkvlzlqQ4hMl0k9KMoeoypnmfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dad1458dc.mp4?token=UkyHCSYD_MFgRqd5T6yAVv-I0VkG90SUPcpBBOFP8HI7YwR1pxDJxozoePqxJy_E07BgA8RIqT8iFA7aIWGwB648avV18svbhfI6y69hHkvgtBavvJiDffgswazdWj-MbUE5ANsAD1Hx4YURI8u00M4oORy9siepcEx4_F7x7QG74rAEsCYEBFS6pGVEIM2wp95vsMKYaARhYwNL0yrH5DF73noPPk6xyn8Cj2XW2DUEnHjNp7CsVkbEWUNprHS4aCeqWKYLDAiPIZeImupfSjJsHgdigfEyDVcSDZzerU9JrpD-2Rpa1A2ipmgTbkvlzlqQ4hMl0k9KMoeoypnmfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه قدرت و استقامت پاهات کمه این تمرین هارو انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/671271" target="_blank">📅 08:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671270">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRokcArFZmfgZa9AMHRrb7zEL47_HH8fBsKIe1jEh2J0mckaisipCJ7go_fjdLluoETtdUnah-8RzkPr-v1a4SCvq3mn7__PiYtIbyYpT0_brKOZlbL_eaxi-qVBO0BwwCSq6fU4k6i6AmERpgNhcQTV6GTfE0l6rDoGWDOeWEK5L6xTHpB7-st2KULMZ9SAxvid7-cfEZRWEz68Wbn7CvGAwlYSyG2m4t1zE3f7fwGhMjSLsynpxaudzUtyS595wpGdENiaqPEijsh9mkrWp-fzFqIivpCGjaiYqPYIqwlmW1V4WVTuTcCIMX_qPRheaTqmTZ72zcc1XVc3i1bLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس پنتاگون برای عراق شرط و شروط گذاشت: یا ایران یا آمریکا!
🔹
وزیر جنگ آمریکا همکاری‌های تجاری و دفاعی آتی با عراق را منوط به تثبیت حاکمیت این کشور و خلع سلاح گروههای مقاومت تحت حمایت ایران دانست و از بغداد خواست میان این گروه‌ها و گسترش روابط با واشنگتن، یکی را انتخاب کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/671270" target="_blank">📅 07:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671269">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is-uB0zPWtgWs8UvtDR7nb-PXQJ1FrsJPiKh045zdkScriJS_PGGG1Rj-tENg5fstcY2O19kdY-4I2A1PSJ51VOnHeYnhC8FMDRrLxDkczcn1XNhGr-ZSgIBMmBR3d97X9Gn3WCoSLSdC15MPSOO4Y1HAFMA29WuLgYwBp9sXBeVv70tIknAWCqYZJTZWTABJotBaePaq0QSyUuY343__E1H3QwX85-xXfL1ivOEppII3zbbx2OXYZAyeGg-epKGvlMNgCiLQotexIchQ_zUrGUFbP7_y8iCaQpfZ-zU4W76tpNE91amU1C4FlGa6f17NImYA1gvDY6NjlT5L-xWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لامین یامال در هر رقابتی که با کیلیان امباپه روبرو شده، او را شکست داده است
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/671269" target="_blank">📅 07:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671268">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIk2yi0HbRRLDdKGCgXYXv8Kv1EfyDAufiZjsarFQoIEcTq8HSIbFBxdMYT2GckSFVcF-205K15WJLp14Nw2E5fB4TqfdHl22ROcNkwkYVjahtPeoyVelyYTgmfC7sim15VkJ4QFNkJKq8SkGD5E8m1ve6_4uRS0CYtE2A2TT7oJON7Aiz3YybKC1qwXUZFs626CgT_YCZ-a2jCjBOQPznNXHLHiLT1B_NW7tA7AwDFX-jv3UnM5dmwcDTBu-AtibdfeUEVfUsqNlZk1dbx6Ng3ZyEUxf0MJ0XGVGdyrb97CP1Qk5Qo-yC2Nkz9QWrS-eOzkDZgYgfnJ_WnfnIAMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار افزایش تابش فرابنفش در روزهای گرم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/671268" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671267">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست‌ کافئین| فصل‌دو،قسمت‌هفت</div>
  <div class="tg-doc-extra">زکریا رازی</div>
</div>
<a href="https://t.me/akhbarefori/671267" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
🔹
محمد بن زکریای رازی
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «فرار از تله‌ی تقلید در بازار» و پرداختِ «هزینه‌ی متفاوت اندیشیدن در سیستم‌های سنتی» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/671267" target="_blank">📅 07:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671266">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ec242e86.mp4?token=h3ab3FIo65bDKFtIG-fFcWOmpZWUpzhNKxhCn1DzUC7cpJlHkSVwA-dOdWT3hICFivBetNaZUv_HMnINAp0pl8FhTUIeREuSSLW0yi1NqWmNMaumPsfiQNL1pCzX-noL2kUZuJ6qHqCo1iXsiloQnz-8DJzziVxhO7HoKhlujuUQJ3MZM7xsxuo2k_X5rKqPugW_4M-aKg1aJnN5eUlGvZFMpQ8foLUbjVpm5d2LZpEAceHOrgeiBmRjSLmR-Vpg3tvZ--gRNHK0vwDqm2v94I82URs-jvAXnHMzUqe4RCH8LjnTcPYjXp9Fo_QiRwcEc3YnACyBct-Y7Ib5aczw9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ec242e86.mp4?token=h3ab3FIo65bDKFtIG-fFcWOmpZWUpzhNKxhCn1DzUC7cpJlHkSVwA-dOdWT3hICFivBetNaZUv_HMnINAp0pl8FhTUIeREuSSLW0yi1NqWmNMaumPsfiQNL1pCzX-noL2kUZuJ6qHqCo1iXsiloQnz-8DJzziVxhO7HoKhlujuUQJ3MZM7xsxuo2k_X5rKqPugW_4M-aKg1aJnN5eUlGvZFMpQ8foLUbjVpm5d2LZpEAceHOrgeiBmRjSLmR-Vpg3tvZ--gRNHK0vwDqm2v94I82URs-jvAXnHMzUqe4RCH8LjnTcPYjXp9Fo_QiRwcEc3YnACyBct-Y7Ib5aczw9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زکریای رازی و پرداخت هزینه متفاوت بودن
#پادکست_کافئین
| فصل‌ دو، قسمت‌ نه
☕️
🔹
ابرکاشفی که نشان داد چطور یک متخصصِ تراز اول، می‌تواند با زیرِ سؤال بردنِ پیش‌فرض‌هایِ صلبِ گذشتگان و اتکا به دکترینِ «تست و داتایِ تجربی»، انحصارهای علمی جهان را بشکند و فرمول‌های جدید خلق کند.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/_pAcf2fyVaU
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/671266" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671265">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J70BLF9BukfGuzyA8fonerFLDM4TFk0LqA4MDvqMzv63AtKBu9xxf6aL24YR7MFmnDlaqFVuBCUcxZRA1WAtlhlsulqlSU9vfjVqTkmB0fRiXnGFNu6P1jrUNYLfX5qs8NvxXtbmwi9whXEWXulcaME7Sp5oeDVW6O-SYIbD8iSJF1TASjNqhS95X4SFaQpzOWn9BXXHUEtGU5Xi6bGLqB2DI5bbsEdQgN1NHeWdGHH7V8S2hOydDrtqVtD3Jz-ptoLkpgRSQh50z8OyA5TzKmleys9-yYTqmAHyuPODQnggdVqcYVEO09KmKgk1jJqb9MiUQd4opA2to2pN6k3azw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۴ تیر ماه
۳۰ محرم ۱۴۴۸
۱۵ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/671265" target="_blank">📅 07:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671262">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
حوزه‌های امتحانی نزدیک مراکز نظامی جابه‌جا شدند
آموزش و پرورش:
🔹
تمام حوزه‌هایی که در مجاورت مراکز حساس یا نظامی قرار داشتند، شناسایی و به مکان‌های امن‌تر همچون حسینیه‌ها و مراکز عمومی منتقل شدند تا محیطی کاملا ایمن فراهم شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/671262" target="_blank">📅 07:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671261">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۴/ پیام مهم سپاه به مردم کویت؛ مرکز ارتباطات ماهواره ای، رادار دفاع موشکی و هوایی، مجتمع پدافند هوایی پاتریوت و آمادگاه پایگاه نظامی آمریکا و سکوهای پرتاب موشک های‌مارس در کویت منهدم شدند  روابط عمومی سپاه:
🔹
مردم شریف و کریم کویت؛ شما به…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/671261" target="_blank">📅 07:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671260">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2c6ad201.mp4?token=J6G2HZ5zRIoa4NcIQTsdoBeb6LeTtnkbheps-FxTWQFqCDXacXFKZBFgKNwvRC2Nq1uY6Eiwwm6Uwojey55teENYM4fFDgNngm1HcqO55eq_jJJnZ2KRLAAID_JrH16j6IoU1CZY8ctIuzimBlpqWFhOCtxIk4M3JLRXN9Wh8719uFh0STIuH6CKNRF8ZjOQpQB7pl3Rz1-_sHuiUBXs4YJ3qTjCRdcaxKxPCKbq7d2MU-8HVDxrmxJDRlU-8heR_G9MH5sJDMi4c_7PEvnuCWT0VuVSflyMtIIObqxFP111fhGXd1AE-RSq5Kcufu2szCO0hEXt3axDb3ovJpiD9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2c6ad201.mp4?token=J6G2HZ5zRIoa4NcIQTsdoBeb6LeTtnkbheps-FxTWQFqCDXacXFKZBFgKNwvRC2Nq1uY6Eiwwm6Uwojey55teENYM4fFDgNngm1HcqO55eq_jJJnZ2KRLAAID_JrH16j6IoU1CZY8ctIuzimBlpqWFhOCtxIk4M3JLRXN9Wh8719uFh0STIuH6CKNRF8ZjOQpQB7pl3Rz1-_sHuiUBXs4YJ3qTjCRdcaxKxPCKbq7d2MU-8HVDxrmxJDRlU-8heR_G9MH5sJDMi4c_7PEvnuCWT0VuVSflyMtIIObqxFP111fhGXd1AE-RSq5Kcufu2szCO0hEXt3axDb3ovJpiD9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارات وارده به مرکز تعمیر و نگهداری هواپیماهای جنگی در پایگاه هوایی العديد قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/671260" target="_blank">📅 07:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
صدای دوبارۀ انفجار در کویت و اردن
🔹
منابع عربی از شنیده شدن مجدد صدای انفجار در کویت و اردن خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/671259" target="_blank">📅 06:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671258">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
استانداری خوزستان : دو انبار غلات و آرد گندم در دشت آزادگان و هویزه مورد اصابت پرتابه های آمریکایی قرار گرفته است
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/671258" target="_blank">📅 06:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671256">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۳ سپاه/ پیام مهم سپاه خطاب به مردم اردن؛ آشیانه جنگنده‌های اف ۱۵، ۱۶ و ۳۵ و تعدادی از پهپادهای راهبردی MQ9 آمریکا در پایگاه الازرق اردن در هم کوبیده شدند
🔹
سرزمین مقدس اردن قدمگاه انبیاست و جای اشغالگران و جنایتکاران بین المللی نیست، انتظار…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/671256" target="_blank">📅 06:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۲/ مرکز مدیریت ان اس آی، مرکز کنترل فرماندهی ، انبارهای بزرگ قطعات و تجهیزات نظامی و مخازن سوخت ناوگان پنجم دریایی آمریکا در بحرین درهم کوبیده شد
🔹
مردم قهرمان و تاریخ ساز ایران اسلامی، ارتش کودک‌کش و رژیم عهد شکن آمریکا شب گذشته با انتشار…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/671255" target="_blank">📅 06:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سنتکام از پایان تازه‌ترین دور حملات خود در ایران خبر داد
فرماندهی مرکزی آمریکا:
🔹
این حملات هم‌زمان با ازسرگیری اجرای محاصره دریایی از سوی نیروهای آمریکایی انجام شده و هفت ساعت به طول انجامیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/671254" target="_blank">📅 05:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۱ / KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در مینا عبدالله کویت به آتش کشیده شد  روابط عمومی سپاه:
🔹
دشمن آمریکایی که شب های گذشته به بهانه اصابت کشتی‌های متخلف به پایگاه‌های ما حمله می‌کرد، دیشب هم که هیچ کشتی جرات تخلف و همراهی…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/671253" target="_blank">📅 05:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
تکذیب سفر نتانیاهو به واشنگتن
🔹
کاخ سفید بامداد چهارشنبه گفت که برنامه‌ای برای سفر نخست‌وزیر رژیم صهیونیستی به آمریکا تدوین نشده است.
🔹
پیش از این رسانه‌های صهیونیستی گفته بودند که نتانیاهو قصد دارد برای گفتگو درباره موضوعات مهم به کاخ سفید برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/671252" target="_blank">📅 05:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۱ / KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در مینا عبدالله کویت به آتش کشیده شد
روابط عمومی سپاه:
🔹
دشمن آمریکایی که شب های گذشته به بهانه اصابت کشتی‌های متخلف به پایگاه‌های ما حمله می‌کرد، دیشب هم که هیچ کشتی جرات تخلف و همراهی با آمریکا را نکرد و طبیعتا اصابتی هم نبود، برای پنهان کردن شکست و ناتوانی خود تعدادی از پایگاه‌های ساحلی و نقاطی در استان‌های جنوبی کشور را هدف موشک‌های کروز و بمب جنگنده‌های خود قرار داد که رزمندگان مقتدر اسلام با پاسخ‌های کوبنده متجاوزان را تنبیه و سرکوب کردند.
🔹
در موج چهارم عملیات نصر۲ با رمز مبارک یا اباعبدالحسین (ع)، KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در مینا عبدالله کویت به آتش کشیده و منهدم گردید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/671251" target="_blank">📅 05:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8196a05790.mp4?token=TpruVTcPPsUoXlt-iaxtIWnrx6m_6Q9rBgDFqrgeZYou6TjWb3_lc-S3eWqabADLRwaaWVn7dklHcYBPAkaPIiTS3hroqpCQlRApxT3QDeGfEn_EsDRurKYtq_Ws8fHh7YiEGrVzCf6JUSFCMHPjh5oZAL417vldbSTmkzfuzHVYQArVtIhFtjZH7l5BLnGpj9J0xwshYbc1FabzDrnFPlqdQK9SFZWc2kyNBqcVrF11u3vUUZ577Ee2AUWYwoO07QIuxB1xK0QzRe_DJbYIcUMucVuwxern_A9nqoDZiKkqUV95tORXkJRfrmkQeenfvQdJ3x24SaVJRqjyEMVr8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8196a05790.mp4?token=TpruVTcPPsUoXlt-iaxtIWnrx6m_6Q9rBgDFqrgeZYou6TjWb3_lc-S3eWqabADLRwaaWVn7dklHcYBPAkaPIiTS3hroqpCQlRApxT3QDeGfEn_EsDRurKYtq_Ws8fHh7YiEGrVzCf6JUSFCMHPjh5oZAL417vldbSTmkzfuzHVYQArVtIhFtjZH7l5BLnGpj9J0xwshYbc1FabzDrnFPlqdQK9SFZWc2kyNBqcVrF11u3vUUZ577Ee2AUWYwoO07QIuxB1xK0QzRe_DJbYIcUMucVuwxern_A9nqoDZiKkqUV95tORXkJRfrmkQeenfvQdJ3x24SaVJRqjyEMVr8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله هشتم عملیات صاعقه ارتش؛ ادامه حملات پهپادی ارتش به پایگاه‌ آمریکا در اردن
روابط عمومی ارتش:
🔹
به دنبال  تکرار حملات وحشیانه دشمن بد عهد،  بامداد امروز، مرحله هشتم عملیات صاعقه با موج جدیدی از حملات پهپادی ارتش جمهوری اسلامی ایران علیه پایگاه‌های آمریکا در منطقه اجرا شد و محل استقرار جنگنده‌های اف ۱۸ و سوله های بزرگ تجهیزاتی ارتش تروریستی آمریکا در پایگاه الازرق اردن، برای دومین بار، هدف حملات پهپادهای انهدامی قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/671250" target="_blank">📅 05:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8efU9wFNN0lTy-aL35Pq_LMw_ILCJaYFBzLJa8vxKp5_Qy40BBtVsBqCGzjR0if1Luy8havLUBtiHr7pwc0OT6kIbli1mxYk0a-I4eK6-8lzBLbint9Lq9ui_1BJCIR_Fza6bxeSMJDjd1aBiwwuJsyi5L7QLTcbFKQFEGex0ZyDvSDIxR4iEC6W3pcR9jwCzbV1Uf2BN4ZUR3DRpyVxV1NlbhPxZZJ94rQeJBw8UpzxlXrSyb-UjOWUgdizv0Gv6YipvsVqvKgR8b_MOJCB7WYukyuvKQsCdYWR2mAiLcIt4u9CDUyPJxZqzkCFSp_qMZsS1qg8LoGfhV5CCGIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت پهپاد ایرانی به منافع آمریکا در کویت
🔹
رسانه‌های عربی با انتشار ویدیویی مدعی اصابت دقیق پهپاد به تأسیسات آمریکایی در بندر «عبدالله» در کویت شدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/671249" target="_blank">📅 04:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7f2f24fb.mp4?token=giHEVblp_8rvuaHad0KvcVszWrKDsBLWmeX4PZyDvpxagmmfL1vwIjq8id-mRxMbTkwa8ea0tZ4DDb91SzTxjOlSJwJnDhbeyno8hr_m3Y-mh8tGeQiH6Q73A3VKYJBUvFEYcpSRlwl92pqLr8Mm5j60idYkVyebPBt2sK_sB-7rulWArU-N-fg4mq2X8f3alIEQNqiXboTzFlukEItHPKq2JhQOafZWty9_zoZfSQoSr_Ycj9CWfG9jSVJZYSZ_A57mMxsAiwFSk7tdrrufohcAyv6hCFrcj8uVQj6cRPbpi2wuW2Ca5uwTfmQCFmFavQ9LmMpk-r6rZYNIfeI_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7f2f24fb.mp4?token=giHEVblp_8rvuaHad0KvcVszWrKDsBLWmeX4PZyDvpxagmmfL1vwIjq8id-mRxMbTkwa8ea0tZ4DDb91SzTxjOlSJwJnDhbeyno8hr_m3Y-mh8tGeQiH6Q73A3VKYJBUvFEYcpSRlwl92pqLr8Mm5j60idYkVyebPBt2sK_sB-7rulWArU-N-fg4mq2X8f3alIEQNqiXboTzFlukEItHPKq2JhQOafZWty9_zoZfSQoSr_Ycj9CWfG9jSVJZYSZ_A57mMxsAiwFSk7tdrrufohcAyv6hCFrcj8uVQj6cRPbpi2wuW2Ca5uwTfmQCFmFavQ9LmMpk-r6rZYNIfeI_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌کس نمی‌داند ایران چقدر موشک دارد
🔹
مجری: به نظر شما ایران چند موشک باقی گذاشته است؟
🔹
ترامپ: آنها تعدادی دارند...
🔹
مجری: صدها؟ هزاران؟
🔹
ترامپ: نمی‌خواهم بگویم. هیچ‌کس نمی‌داند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/671248" target="_blank">📅 04:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
وزارت کشور بحرین اعلام کرد که بار دیگر آژیرهای خطر فعال شده‌اند و شهروندان و اتباع مقیم با حفظ خونسردی و آرامش، خود را به نزدیک‌ترین مکان امن برسانند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/671247" target="_blank">📅 04:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=XvAPvso1qkIQfSw0DsYnIDeVDuKS6rQYpQy6rpZHKjLj3MquZUlA7oJ3s4iS8ZSLy6-h2lvj5tRJjhg_xhejlI3CuW799JoSvdU5s_N3ytGur3W1hJ74kppb0b0dQ1K3lrMQb23Goz10jFes-AQxoZ_2jUNcLVcWaGBWeYA-Q9bnw1gFeGvhw91XVxwtmdmtpye3Xuh9l7VxKCVs9Qk4Uh67Ir52R7b8L3rGmswtVTNh2H_yv0m5mY9K8ZS5nLxHy3TpgNUq482gZtLzBK-Se8xPj9hWqSpCB74yQEPGOSc8vIDF8EqsB36ZzRqMdVn6c9ICcWlC5Dlf6w-Dk9MoXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=XvAPvso1qkIQfSw0DsYnIDeVDuKS6rQYpQy6rpZHKjLj3MquZUlA7oJ3s4iS8ZSLy6-h2lvj5tRJjhg_xhejlI3CuW799JoSvdU5s_N3ytGur3W1hJ74kppb0b0dQ1K3lrMQb23Goz10jFes-AQxoZ_2jUNcLVcWaGBWeYA-Q9bnw1gFeGvhw91XVxwtmdmtpye3Xuh9l7VxKCVs9Qk4Uh67Ir52R7b8L3rGmswtVTNh2H_yv0m5mY9K8ZS5nLxHy3TpgNUq482gZtLzBK-Se8xPj9hWqSpCB74yQEPGOSc8vIDF8EqsB36ZzRqMdVn6c9ICcWlC5Dlf6w-Dk9MoXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت موشک‌های ایرانی به اهداف آمریکایی در بحرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/671246" target="_blank">📅 03:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
پهپادهای ایرانی به کویت رسیدند
🔹
ارتش کویت از فعال شدن پدافندی هوایی این کشور برای مقابله با پهپادهای از سمت ایران خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/671245" target="_blank">📅 03:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba861f0f8.mp4?token=dnsSYal6-iUvSndKee4XIty83d-8zgjz1bvnk-ol-94iLMR_ZU7rHRNGkK5-EjjH0Vbo7Z_oXE6UgfGeSfsMMzHEalnGqpIgwFzDRxru8qn3xGZRJUXRVlYSArsqUp69g4Ude4AEKtpQS0_63sbJ_msmQmUC8x5C9Xcx09E688fMoIl32A-rolDWlDjpehDqKYV7pI9aVb1Nq_02rEG2mMYB70nQiYhzGgvd6akpEmFQXxr_7jJoSrVNFFrlUR2rOplScgkqt7Q6hmFPlTR1CfWKw-6ZsV-7POlTTsPsyA1znwGaBr3Z2V8Ip-nJUj0qM1aHWpnJctEdWhfU_SU8pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba861f0f8.mp4?token=dnsSYal6-iUvSndKee4XIty83d-8zgjz1bvnk-ol-94iLMR_ZU7rHRNGkK5-EjjH0Vbo7Z_oXE6UgfGeSfsMMzHEalnGqpIgwFzDRxru8qn3xGZRJUXRVlYSArsqUp69g4Ude4AEKtpQS0_63sbJ_msmQmUC8x5C9Xcx09E688fMoIl32A-rolDWlDjpehDqKYV7pI9aVb1Nq_02rEG2mMYB70nQiYhzGgvd6akpEmFQXxr_7jJoSrVNFFrlUR2rOplScgkqt7Q6hmFPlTR1CfWKw-6ZsV-7POlTTsPsyA1znwGaBr3Z2V8Ip-nJUj0qM1aHWpnJctEdWhfU_SU8pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس صداوسیما: آقای خاتمی می‌گوید طرف‌داران جنگ و انتقام، اسرائیلی نیستند اما حرف اسرائیلی‌ها می‌زنند، ما هم نمی‌گوییم که آقای خاتمی اسرائیلی است اما ایشان دقیقا دارد حرف اسرائیلی‌ها را می‌زند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/671244" target="_blank">📅 03:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599c252863.mp4?token=DB0Kr9XSghJK3B6t2cuxuTV-pCzmXTIXUtm80my1HCCc4fbYiVIMqCMkf_sE0P6ajM6TN-YJ2afQirwod7fTvaSWyFUIMqRZkCMtXbkJAPhoaoteRswYjc1S1X2f66T6pLIrMXarMnKER7BZ6LsfrrTx77fmjcvOYxN3GdMc0jHZlKoWmWYWXme76G2HKH6I84GTCldujrxjLELCmic9rdfOBD19s1i8nf9sRpf4h3RIRMrkW7eEzftUbM_c6A2nWCkp4phlzwiG4fTzJHf5irDR6purzsoBWS2zYi79BtXUNFq4tYuFx_aAHEcUNvfXq2VvFeaJ_vAaLqMuZm-CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599c252863.mp4?token=DB0Kr9XSghJK3B6t2cuxuTV-pCzmXTIXUtm80my1HCCc4fbYiVIMqCMkf_sE0P6ajM6TN-YJ2afQirwod7fTvaSWyFUIMqRZkCMtXbkJAPhoaoteRswYjc1S1X2f66T6pLIrMXarMnKER7BZ6LsfrrTx77fmjcvOYxN3GdMc0jHZlKoWmWYWXme76G2HKH6I84GTCldujrxjLELCmic9rdfOBD19s1i8nf9sRpf4h3RIRMrkW7eEzftUbM_c6A2nWCkp4phlzwiG4fTzJHf5irDR6purzsoBWS2zYi79BtXUNFq4tYuFx_aAHEcUNvfXq2VvFeaJ_vAaLqMuZm-CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به پادگان ارتش در بمپور/ هنوز آمار دقیقی از خسارات و تلفات در بمپور در دست نیست
🔹
حدود ۳۰ الی ۳۵ دقیقه قبل بود که صدای چندین انفجار از این منطقه شنیده شد و حکایت از این داشت که جنگنده‌های کشور آمریکا به پادگان ارتش حمله کرده بودند. ظاهرا شلیک‌ها به سمت آسایشگاه سربازها بوده که در حال استراحت بودند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/671243" target="_blank">📅 03:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند
🔹
گفته می‌شود این انفجارات در اثر شلیک موشک‌ها به‌سوی پایگاه‌های آمریکایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/671242" target="_blank">📅 03:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6d169a6b.mp4?token=BvLsG4JL8PUq8wn40SPZop3G5KG28yzyFgV9s4wjMl2ZYKKnCbFiwq1BU1yC65KDYryg1ygNFDFz0ZB7tX6mxVeq8n1Vb9Oth_lv64jpw9UnFiXPtca30AmvjN8SWSnqOga_GWT7xu6oWfOFzKoqGWro7wgdreHQkBNAOuKbOI3U8b9OTpiHvBUKbntUejL0PdCCl9H3jnFKYfXYLdJZR4BZ9cMgjhqdxyJ6TbcgN2OzmrMyremUh5-Wc_788Lw0kOcbe1bwUY-cJuZulLhMuvzS-naM0J9tGNwJa8Ul7tlOsF7Y7a73pZ1zFGLDaCUwwIVHRMlc_nKZmXq-li3vOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6d169a6b.mp4?token=BvLsG4JL8PUq8wn40SPZop3G5KG28yzyFgV9s4wjMl2ZYKKnCbFiwq1BU1yC65KDYryg1ygNFDFz0ZB7tX6mxVeq8n1Vb9Oth_lv64jpw9UnFiXPtca30AmvjN8SWSnqOga_GWT7xu6oWfOFzKoqGWro7wgdreHQkBNAOuKbOI3U8b9OTpiHvBUKbntUejL0PdCCl9H3jnFKYfXYLdJZR4BZ9cMgjhqdxyJ6TbcgN2OzmrMyremUh5-Wc_788Lw0kOcbe1bwUY-cJuZulLhMuvzS-naM0J9tGNwJa8Ul7tlOsF7Y7a73pZ1zFGLDaCUwwIVHRMlc_nKZmXq-li3vOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت پهپاد ایرانی به منافع آمریکا در کویت
🔹
رسانه‌های عربی با انتشار ویدیویی مدعی اصابت دقیق پهپاد به تأسیسات آمریکایی در بندر «عبدالله» در کویت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/671241" target="_blank">📅 03:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c595e8a6.mp4?token=Ffo_058_JFvQOEFcssFZbQfkmtOwZOtFUyLER0MP6wbQi5lHgHuuognUAHZim3iHuLfzzX6mhf35kKN5pHWJA8YeAl7FSx4qYXPg8c3jq_K_FSp-1-C-xqN1ebx1dGu6MfhE-9anivOmHiUbF2hEPpTK-GJqkuPfT1nKcVqIHbM3pXPJhkANMVOKf9I3zztpzFTP006OUMgSjJVBShi-6YCTKsYq2ToBPpTZ1138sUiATzyJSrKNwY10ZyUG-XKqjuL9ZGh61FikyXoyGncMtWoEPNuYQ2pcZCay5iqnJ5QDZDsC0KSPzNQZ-EDD0SNDMaZriQPw2l-4jwM7OrHEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c595e8a6.mp4?token=Ffo_058_JFvQOEFcssFZbQfkmtOwZOtFUyLER0MP6wbQi5lHgHuuognUAHZim3iHuLfzzX6mhf35kKN5pHWJA8YeAl7FSx4qYXPg8c3jq_K_FSp-1-C-xqN1ebx1dGu6MfhE-9anivOmHiUbF2hEPpTK-GJqkuPfT1nKcVqIHbM3pXPJhkANMVOKf9I3zztpzFTP006OUMgSjJVBShi-6YCTKsYq2ToBPpTZ1138sUiATzyJSrKNwY10ZyUG-XKqjuL9ZGh61FikyXoyGncMtWoEPNuYQ2pcZCay5iqnJ5QDZDsC0KSPzNQZ-EDD0SNDMaZriQPw2l-4jwM7OrHEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی دیگر از عبور موشک‌های بارشی ایران از پدافند آمریکایی در اردن و اصابت مستقیم به پایگاه آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/671240" target="_blank">📅 03:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/078c717ca6.mp4?token=UjWpqYOs5bXBoH8sAU2AEA14SuH9Qt3xpKDfZZiUFMWdF8ECT1V7wyhM37aLWNepWyskax1pO5_mb9oPSv975U0LrfPkRveS-1m8PUgksbBhLe_2SPmi7oVKOTkmZOc4KUqNYndfit0t99lqpIzpvQVXA9FbRYCUsGQq7LkUzU-l5vo8Mfe6AmdpIj6OXo5CjR3Qwr2hG8qg27_KTvvAIJrgB4D0BleqsYq0D3oHptVe-umBqkiOC3HOE-Dcvy2iusuTttZfOozLIQzWbYIPNU1LRSwCyUZGHgCddx5bhSM6A9_DbP0dg-IgsG6Pnr-r81gkTb3V97DscCwJiw_HBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/078c717ca6.mp4?token=UjWpqYOs5bXBoH8sAU2AEA14SuH9Qt3xpKDfZZiUFMWdF8ECT1V7wyhM37aLWNepWyskax1pO5_mb9oPSv975U0LrfPkRveS-1m8PUgksbBhLe_2SPmi7oVKOTkmZOc4KUqNYndfit0t99lqpIzpvQVXA9FbRYCUsGQq7LkUzU-l5vo8Mfe6AmdpIj6OXo5CjR3Qwr2hG8qg27_KTvvAIJrgB4D0BleqsYq0D3oHptVe-umBqkiOC3HOE-Dcvy2iusuTttZfOozLIQzWbYIPNU1LRSwCyUZGHgCddx5bhSM6A9_DbP0dg-IgsG6Pnr-r81gkTb3V97DscCwJiw_HBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار نتانیاهو از کنست در پی شعارهای نمایندگان مخالف
🔹
نتانیاهو که همزمان با جلسه رای‌گیری درباره لایحه معافیت یهودیان حریدی در کنست حضور پیدا کرده بود با اعتراض شدید نمایندگان روبرو شد.
🔹
نمایندگان مخالف با شعارهای «گم شو، گم شو» و «ننگ برتو» نتانیاهو را وادار به خروج از ساختمان کنست کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/671239" target="_blank">📅 03:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
خبرگزاری رویترز: دموکرات‌های سنا به دلیل مخالفت با جنگ ایران، لایحه ۱/۵ تریلیون دلاری بودجه دفاعی آمریکا را متوقف کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/671238" target="_blank">📅 03:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671236">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25d764910.mp4?token=LRSb1WCDb0ifDZrssz29Ef4rMqvdVSJs3XGljSKSh052I38rz4nZ-x2V_CmGFiVtZvHfj09mDv-9CrD2Od1YqXpaf7mMdG5XiWAgaRE2dUvo1GnTaJnYZ28_uqu8TBU1OxZEU_a6KWMlEJAsn7c9YwKrRW_qMemx_IyhTLF9anE5wpWPk2Axb1h3emhgn_odKWJh7tSFRUMyZmgsEkYjBeHxVRd40JNgd6GzwS1XeubLQ-RujxRG3HbQJaxDpkX1FsiGSwYKdv19nTaauWJf5GtgsiDJxHgVdePWivIqUg4pPXjpYtpLqg17e1ZXeSNIaIxpzMdkn0b0oioRDcKcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25d764910.mp4?token=LRSb1WCDb0ifDZrssz29Ef4rMqvdVSJs3XGljSKSh052I38rz4nZ-x2V_CmGFiVtZvHfj09mDv-9CrD2Od1YqXpaf7mMdG5XiWAgaRE2dUvo1GnTaJnYZ28_uqu8TBU1OxZEU_a6KWMlEJAsn7c9YwKrRW_qMemx_IyhTLF9anE5wpWPk2Axb1h3emhgn_odKWJh7tSFRUMyZmgsEkYjBeHxVRd40JNgd6GzwS1XeubLQ-RujxRG3HbQJaxDpkX1FsiGSwYKdv19nTaauWJf5GtgsiDJxHgVdePWivIqUg4pPXjpYtpLqg17e1ZXeSNIaIxpzMdkn0b0oioRDcKcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شیرجه و اصابت دقیق موشک ایرانی در پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/671236" target="_blank">📅 03:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671235">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
یک واحد تولید آب معدنی در اطراف روستایی در بخش موسیان در ایلام هدف ۳ پرتابه دشمن دشمن قرار گرفت
/ ایرنا
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/671235" target="_blank">📅 02:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671233">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2jC0ePusLNN9UZZU8D0pekDL2E_8m777MhaQbrnyuVtWeBOHiw4wSHXos1Nu19juNQD-7T5BWkJG-lxpM_JR9FEPzBWyMLMWQgGcUIlFVo2PkjjkP6NzOo5A5F3VLhXfcmdqm3sDkWTZqp5ysZUQeI7LShy7kSjDx-7QEZZu-6-U5AvQQY_iEHhKTiaMhCq97lhbaPeGq6t6hD86Us4TV61wCRmB3ESRsH1fUK3bGyhnelQwOovAEzH35UXjfUuASDmPw-WvgMwVLgkqxEPgMIpPJU0ul9uxWc_rnT9R-dShpwrz5GYsVP1G184TCHFawmzrElTccPZnizsnvCnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت موشک ایرانی در شمال اردن
🔹
تصویری که رسانه عراقی از اصابت موشک ایرانی به پایگاه تروریست‌های آمریکایی در شمال شرقی اردن منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/671233" target="_blank">📅 02:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671232">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a59ef456c.mp4?token=R_ebk8f7vlkjQZd56m4v-EgRn4xzcZGHiwo9t3lfWJ47KPxQsXyB096CKF0yc1PBgqwzHy3gDmayRcj5eumdq8n-lmLRK7hi8A1ZmwWylqsMtZRXYPR2q-9DkwSEQNmmpn-Xcw5RwRYSQ2ufhNtUANTcOWsgrFFVqmJ1oWl98ARzyp3X1J0zIGielEPkhsf2kijZDqg9C6Sd_SQDc97NP4pWUc4yy5u_1wmvbWAUughWoCpag3zIUwYes-03r7sOmAmLE6138ZmTugXtLspy59wHA86mstdI3B8E4B7AWbWfpRKJTgwPh3ykUbmhoA98alBJlvE_EvnEab9j-P3ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a59ef456c.mp4?token=R_ebk8f7vlkjQZd56m4v-EgRn4xzcZGHiwo9t3lfWJ47KPxQsXyB096CKF0yc1PBgqwzHy3gDmayRcj5eumdq8n-lmLRK7hi8A1ZmwWylqsMtZRXYPR2q-9DkwSEQNmmpn-Xcw5RwRYSQ2ufhNtUANTcOWsgrFFVqmJ1oWl98ARzyp3X1J0zIGielEPkhsf2kijZDqg9C6Sd_SQDc97NP4pWUc4yy5u_1wmvbWAUughWoCpag3zIUwYes-03r7sOmAmLE6138ZmTugXtLspy59wHA86mstdI3B8E4B7AWbWfpRKJTgwPh3ykUbmhoA98alBJlvE_EvnEab9j-P3ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش سامانه پاتریوت در اردن برای مقابله با موشک بالستیک ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/671232" target="_blank">📅 02:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671231">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
وقوع انفجار در پایگاه‌های آمریکا در اردن
🔹
منابع عربی بامداد چهارشنبه از هدف قرار گرفتن پایگاه‌های محل استقرار نظامیان آمریکایی در اردن توسط موشک‌های ایرانی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/671231" target="_blank">📅 02:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
بیانیه سنتکام درباره عملیات‌های ایران علیه پایگاه‌های آمریکا
🔹
«برد کوپر» فرمانده سازمان تروریستی سنتکام بامداد چهارشنبه مدعی شد که ایران طی یک هفته گذشته، به ۷ کشتی تجاری حمله کرده و همچنین تعداد زیادی موشک و پهپاد به سمت پایگاه‌های آمریکا در منطقه شلیک کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/671230" target="_blank">📅 02:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671229">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
حملۀ آمریکا به دهلران
🔹
دقایقی قبل، یک نقطه در شهرستان دهلران مورد تهاجم و اصابت پرتابه های دشمن آمریکایی قرار گرفت. هنوز از محل دقیق انفجارها و میزان خسارت‌های احتمالی خبری در دست نیست./ فارس
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/671229" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671228">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
خوک نجس: ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم
🔹
ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند.…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/671228" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671224">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f4c90a8b.mp4?token=gzFC5C0u7ItP_E0pM3qLhX7imKt2lN4sBnwXpv_fuHeJmTEad7bWT12KxysjEqvJUrZa2D55vwfm_6z6Ah3hHYEBHftuBNmqTe7cMctNfCASGo4n1Rt29xtQ9omkLPGGm8Q5odQHxmaMy_awVsWnmfCk7h8p_upmv3uaFDmXDBeM4tdClqizslFpDoYitWF0RNft21KaWPx7-_-u9QoxdRl5DSIDu_hvPMUEQHDwM-BX80mhNMnI_iweExoZGdk3-f4JxmiVkq2fXl_fhRSXAlZ1lEYKCJC7vfYhzkz4nGI_xNScJcLpam8p8y-3F1E9tvbBLULOUO0TVbgUD8-e0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f4c90a8b.mp4?token=gzFC5C0u7ItP_E0pM3qLhX7imKt2lN4sBnwXpv_fuHeJmTEad7bWT12KxysjEqvJUrZa2D55vwfm_6z6Ah3hHYEBHftuBNmqTe7cMctNfCASGo4n1Rt29xtQ9omkLPGGm8Q5odQHxmaMy_awVsWnmfCk7h8p_upmv3uaFDmXDBeM4tdClqizslFpDoYitWF0RNft21KaWPx7-_-u9QoxdRl5DSIDu_hvPMUEQHDwM-BX80mhNMnI_iweExoZGdk3-f4JxmiVkq2fXl_fhRSXAlZ1lEYKCJC7vfYhzkz4nGI_xNScJcLpam8p8y-3F1E9tvbBLULOUO0TVbgUD8-e0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایران در راه پایگاه‌های آمریکا در سراسر منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/671224" target="_blank">📅 02:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671223">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
آغاز موشک‌باران پایگاه‌های آمریکا در منطقه
🔹
منابع خبری از شلیک موج تازه موشک‌های بالستیک به سمت پایگاه‌های آمریکا در منطقه خبر می‌دهند. در این میان آژیرهای هشدار در اردن به صدا درآمده و پدافند موشکی مستقر در پایگاه‌های آمریکا برای مقابله با موشک‌های ایرانی فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/671223" target="_blank">📅 02:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671221">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dacf0d7f3.mp4?token=d-fJCjFa8Tz0tvZ3MJ88fun2kVTJptI2unUZD2H01Mt88KOgANTrFE4Z9bTQ-BEKDDpWh4nLuN2d-5YoteuolY4r834j-XRg4Mi2DHX3H1hWMd1zaSeyc_hvSb9vz_wA-wYTWYlhzDcJIYHDcF3e2rFxOu5xVvnPSDteV6d36V79rw4EiI91Af8DGxv2I_OT5GYxAySLnPkBjqFNl7gvDtnbU_qffiDlxyGG3VqDZzt7bGe3HdEAEzuLf1hPwqkrWoTUvKFWXWF2os2Bn3i4jAvbPLwzaAPB01zftYNpByCT9CRUgFu3U6noMYEjlTZRJU1Pql2l136edpPwOR7kUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dacf0d7f3.mp4?token=d-fJCjFa8Tz0tvZ3MJ88fun2kVTJptI2unUZD2H01Mt88KOgANTrFE4Z9bTQ-BEKDDpWh4nLuN2d-5YoteuolY4r834j-XRg4Mi2DHX3H1hWMd1zaSeyc_hvSb9vz_wA-wYTWYlhzDcJIYHDcF3e2rFxOu5xVvnPSDteV6d36V79rw4EiI91Af8DGxv2I_OT5GYxAySLnPkBjqFNl7gvDtnbU_qffiDlxyGG3VqDZzt7bGe3HdEAEzuLf1hPwqkrWoTUvKFWXWF2os2Bn3i4jAvbPLwzaAPB01zftYNpByCT9CRUgFu3U6noMYEjlTZRJU1Pql2l136edpPwOR7kUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به احترام جنوب...
💔
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/671221" target="_blank">📅 02:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671219">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uj9lSbtj1Uq_6DAlYnhfc-MdU9knCRLWN-Ch7plUjk8UCg2JpVJQLsF3z5LMyjuEBz4bgQ6iYPfxPrzQmIrKQBwL3gvkA-GEYyCCeXeYnO7xMEGVokUPcz96JL2ljJR5EOT8Q39zFy4X8AlwN9bcBIYHcwAnbphVGUOw7J-miXnSzMYPD7TapUlW82QK7q_wpA_KixELNMB-CpPSVOgF620-_mi034HfMQzATKHpeRv9wSOHBe2tVI6eEuakf6boEowZNRTLEv3cUiNhleQ4LlgQ8YrIQX6zY3v-2EYZQf6W6yLJ20mE20JtnVr86vJSmtVzENryqcG3K6F9cpQg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5FdoTJ1F3nx_MbIhxEj1asvDSSAeDKOmENY9_qB_wNd6SQjwc4nLV9F7b3L_U5I5rLF6rj36nwXcWig_LHcdXN-bN_LU5jRg7mB-p12Xs8iTJc4DF1auK_xtTirkpHtGDRO9DteLzesvLLzuakAivfkZs0kLpp80WjtWQgw_amnA7qsNGi8-K8wdMpQwdVbxtwXj7ivZ-NW8vmfMn5uMxghlqVCCW8qhcikUVEv1vr5gPejXyf7O6fJaR5ryfsFyXuZv9z9o6DvL2K110VS6UT6HNhLSDPSTZEUXngdV86mGxWKiBXBtwcNnmRBih9UQWt2hklgzfqgig0a7ObL8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری جالب از پزشکیان در مراسم مصلای تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/671219" target="_blank">📅 02:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671217">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0021e2c0f.mp4?token=AC8O7-pL2See3LJfu9GS8ncH3GtwJ2pzznCnM_bouYDc2e5-tO7sJjSDLDAK86JfMftzrRFhd9h5pcwljd0zaa_v0aC9csUBSXRfENuTulye-dPoEDEwgHQKGMBduBmeAL-IRcFgkfgk_LzDmNwG74_2QQWs5ioB-JQN2VCVnNHUh3VzXaVN80O4Y387bVylbVKZ2_FzCizMYdn0b4xQsa7QcENshpa7Z85AATh00CumtvlGV0q_f5n2h7-RM7kreKk5m0TLsB_fzvD9tXLr0qzKvSzln4aKd6qUG5phh_cX871l5xZ1D9nx90BlQYWXRGEj_goFva36n0Rl1-0uCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0021e2c0f.mp4?token=AC8O7-pL2See3LJfu9GS8ncH3GtwJ2pzznCnM_bouYDc2e5-tO7sJjSDLDAK86JfMftzrRFhd9h5pcwljd0zaa_v0aC9csUBSXRfENuTulye-dPoEDEwgHQKGMBduBmeAL-IRcFgkfgk_LzDmNwG74_2QQWs5ioB-JQN2VCVnNHUh3VzXaVN80O4Y387bVylbVKZ2_FzCizMYdn0b4xQsa7QcENshpa7Z85AATh00CumtvlGV0q_f5n2h7-RM7kreKk5m0TLsB_fzvD9tXLr0qzKvSzln4aKd6qUG5phh_cX871l5xZ1D9nx90BlQYWXRGEj_goFva36n0Rl1-0uCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس: ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم
🔹
ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/671217" target="_blank">📅 02:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671215">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de4c546ec0.mp4?token=TgGkKibkfsg_KKXIhm-7b-eKb48NveSROzBPQ8Pc2OFIB8NcqggfT1Dtjl-nXhNqdMpsd7VHpi1T4JSl7Hqe6La-eUrilCCQdAwPTefbFUUMWjfY_qoyRKM-45NCSMikAKo-8socJjr8EiCHvEBLtejtwn_VD2xNiiJlpuiahT1_zeXRkg0dQhWoW1VXeSc5AodXCWN1ifag1ldJczs3Y6voTTuSfXE09Pna0d6Jb7_IMO4yu88-4LTgrTO91Hsfx0f0xDzD_NdxEagm-9PA42RwiVYY62sc3VBZ_kI-3vbuhH2DTW1pEvr22YH1j0Mp0soZVNt4iWlrAk8z_qzKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de4c546ec0.mp4?token=TgGkKibkfsg_KKXIhm-7b-eKb48NveSROzBPQ8Pc2OFIB8NcqggfT1Dtjl-nXhNqdMpsd7VHpi1T4JSl7Hqe6La-eUrilCCQdAwPTefbFUUMWjfY_qoyRKM-45NCSMikAKo-8socJjr8EiCHvEBLtejtwn_VD2xNiiJlpuiahT1_zeXRkg0dQhWoW1VXeSc5AodXCWN1ifag1ldJczs3Y6voTTuSfXE09Pna0d6Jb7_IMO4yu88-4LTgrTO91Hsfx0f0xDzD_NdxEagm-9PA42RwiVYY62sc3VBZ_kI-3vbuhH2DTW1pEvr22YH1j0Mp0soZVNt4iWlrAk8z_qzKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دروغ ارتش اردن در رهگیری موشک‌های ایرانی؛ موشک‌هایی که به هدف خوردند اما اردنی‌ها نخواستند ببینند
🔹
ارتش اردن امروز اعلام کرده بود ۴ موشک بالستیک ایرانی را که به سمت این کشور پرتاب شده بودند، رهگیری کرده است!
🔹
ویدیو منتشرشده از پایگاه ملک فیصل در جنوب اردن که ظاهرا هدف حمله بوده نشان می‌دهد سامانه پاتریوت مستقر در پایگاه در رهگیری موشک‌ها ناکام بوده و تقریبا همه کلاهک‌ها به هدف اصابت کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/671215" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای شیطان زرد: نمایندگان من یک ساعت پیش با ایرانی‌ها صحبت کردند  #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/671212" target="_blank">📅 02:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای شیطان زرد: نمایندگان من یک ساعت پیش با ایرانی‌ها صحبت کردند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/671211" target="_blank">📅 01:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
اصابت پرتابه به نقطه‌ای در حوالی شهر حاجی‌آباد
🔹
بامداد چهارشنبه، نقطه‌ای در حوالی شهرستان حاجی‌آباد هدف اصابت پرتابه دشمن آمریکایی قرار گرفت. این خبر توسط استانداری هرمزگان تأیید شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/671210" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671207">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
فاکس نیوز: آیا همچنان قصد دارید جزیره خارک را تصرف کنید؟
🔹
ادعای خوک هار: «نمی‌توانم این را به شما بگویم، چون اگر بگویم، کار احمقانه‌ای خواهد بود.» #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/671207" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671206">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
اراجیف تکراری شیطان زرد: اگر ایران به میز مذاکره برنگردد، تمام پل‌هایشان را هدف قرار می‌دهیم
🔹
امشب، فردا و پس‌فردا به ایران حمله سختی خواهیم کرد و در مرحله آخر نیروگاه‌ها و پل‌ها را هدف قرار خواهیم داد. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/671206" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671205">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d78523d3.mp4?token=Qs8tNw55TIW5BlAg-JQshn3IqFWupotly1aWX1aVKiZY16u5jpE-CW4c8oVqbX6h2B2iK3vf-w4pNjqtA9jfceQltYu_rbi8XhnC3069uL8ClvI-rXmlavSfwY4jB8K1zJuuvMG_WXltTntJxiw3_3p2nby-HS4F2Tzu_GRCsz5ZbNOHLuIVDpHoODqzUiG5f6OL9PoOuc0LevMt1RmDQSlW_ASSn0S-iDepf4vhDPaKnOfmXC4BhLUbFeu041QeazJ5CbuaPkfVDF9gG3ZIGj1aWrcaQXZ1b8lzbNZ7KDWEs_UmVUF0qti2FBUsrhkGD7Gn15Uc1dC53H3RYoV9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d78523d3.mp4?token=Qs8tNw55TIW5BlAg-JQshn3IqFWupotly1aWX1aVKiZY16u5jpE-CW4c8oVqbX6h2B2iK3vf-w4pNjqtA9jfceQltYu_rbi8XhnC3069uL8ClvI-rXmlavSfwY4jB8K1zJuuvMG_WXltTntJxiw3_3p2nby-HS4F2Tzu_GRCsz5ZbNOHLuIVDpHoODqzUiG5f6OL9PoOuc0LevMt1RmDQSlW_ASSn0S-iDepf4vhDPaKnOfmXC4BhLUbFeu041QeazJ5CbuaPkfVDF9gG3ZIGj1aWrcaQXZ1b8lzbNZ7KDWEs_UmVUF0qti2FBUsrhkGD7Gn15Uc1dC53H3RYoV9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد به فاکس نیوز: حملات به ایران تا زمانی که من بگویم دیگر کافی است، ادامه خواهد داشت/ ضربات بسیار سختی به ایران وارد خواهد شد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/671205" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671204">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شیطان زرد به فاکس نیوز: حملات به ایران تا زمانی که من بگویم دیگر کافی است، ادامه خواهد داشت/ ضربات بسیار سختی به ایران وارد خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/671204" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671201">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
درگیری و تبادل آتش در تنگه هرمز
استانداری هرمزگان:
🔹
صداهایی که هر از چندگاهی در بندرعباس، شهرستان‌های ساحلی و جزایر خلیج‌فارس شنیده می‌شود مرتبط با درگیری در تنگه هرمز است‌. در حال حاضر درگیری در دریا برقرار است و تبادل آتش وجود دارد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/671201" target="_blank">📅 01:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=OWsKXJs6suQc-VLsT4ZSyplSYSbMa6YmnG0sS4uOOiyO3nMhZsK5KCJ1s5MvYaOm3vbFbR85EVEbui4JotD81HXKLR0JHRQHtdvkp_EQRGSzb6pirwoAaWtM-tpURM8PLsYKnFOUv3jZTAeWB9U8UGOzT83ekcYwybUDqFoZqQ8f64kYfTZQUkzNnjhwJW3yDAFh85rO3lxeHrduHXyo6KIoi44gdvTSI9PaOKYB5MbIaMz9l4HOxP6XOc99_oSgE0iIowQJUmVniPa5zs0shOg_9dt09HNBOML9OsJxkAv4snoqmBs6yjYCbY4nVsv5qUwhMwMeG6iwOlH-y_1uLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=OWsKXJs6suQc-VLsT4ZSyplSYSbMa6YmnG0sS4uOOiyO3nMhZsK5KCJ1s5MvYaOm3vbFbR85EVEbui4JotD81HXKLR0JHRQHtdvkp_EQRGSzb6pirwoAaWtM-tpURM8PLsYKnFOUv3jZTAeWB9U8UGOzT83ekcYwybUDqFoZqQ8f64kYfTZQUkzNnjhwJW3yDAFh85rO3lxeHrduHXyo6KIoi44gdvTSI9PaOKYB5MbIaMz9l4HOxP6XOc99_oSgE0iIowQJUmVniPa5zs0shOg_9dt09HNBOML9OsJxkAv4snoqmBs6yjYCbY4nVsv5qUwhMwMeG6iwOlH-y_1uLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناوبان جانباز کنارک: موشک دشمن را دیدیم اما لحظه‌ای عقب نرفتیم
🔹
ناوبان جانباز تهاجم آمریکا به کنارک، در روایت خود از دقایق پیش از اصابت موشک تا آخرین لحظه مأموریت می‌گوید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/671200" target="_blank">📅 01:25 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
