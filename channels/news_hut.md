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
<img src="https://cdn4.telesco.pe/file/QrvxPEjXiB2H_zBMRtR_LJlirnrMhl3U5xR96ve-ivnlP77LXSdtOBsS3DqJTdwQjTSJ6dSehNhGDdtBTLq0v_4hlvw775mlqgSackhzhMQww7rjKhLhRFNF8Kg9-01IxlLWWhcE7r23s3MeQLa3VXZGGTgkoqxpgOEmlX-THh1GSqFA35SPOO6oYSMOEgJfgYcOMRoB_a_SsRTPl7YbUxWCkmRIEaNlJVA1xDZBNrsj01VolEWxDcNsW22fOwI3F4ToC7ioNuJk67YJIQhJ8sGXhthXqMFyOKhsNM8fnipTWz5dLAr7xJ4BHUrf0-Tylk5Wd1sM2Z5VMzNe-2g36w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BupSD1V0Sg2x4ZGsllBrHLS88oGyGMitiK5GQ0d4ESQPgXMOGZS9pNS7juVvvxhTWp5nDkfC-LWvY-puVmyQk1lcMUnZjpAAVehnRrZJKmIkfo4NZU8yvI4WE2-VUXmJ2TITK8Qi3_RwT14sW9bp13syHXZe9cPDrxi02lmkRSQJ1-HCU9hVji_8w-OCrhEdtReeAt3mx5yPDj7CE_8ht4AyEfQ7Els8aOxOhVG7iGWREGvZZX4Il4KSePvLU7U62Ab9TBmPVJuDawei84JTxTTVYTUt8NNRTm817n1ePHsJw4wPzMwFoRYuM7RWBhnw1rM5XwjIoqYqL3vUVecqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4svIsG0l_KaI6or_AEgGqGLx2t8H4LgBntmzDtqupgWeUFSzQH4HuP_RYuQVD_qETEi8QQ-2HcvdmG58iLeoVQJ65WnizFDQT5P8rgwcDcf4nFXyi8AtXouD23m_TUQYD8zmWFAH85cEsuq7tXLuQE0scjhNM_tL5mKCx7MWC5BcSiDuow5N2NWUDihgxnhgx7SHX8zfVoi--SPEHVea2rdoRcSJcJ3G9_RAvFSmWEl9TQUgRs-u_04boUKnbwEghFctVgxAmbhqwblJ1holDtUfccnYCgVY41UfZ5ykkHfdantEnC_eJ_VKdSZeWSUVOYjTF9n7yHCxl6cH9kacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG_3E5E6kkFsTF9Fgx77inZMi3CQawzXc_8K7KRPbdfm3tLzd7XpIdo5iQPasGnquVsPRzPjUcJYJL8KNAsoriHINFLU9xD4oISqX7FjotiFXdheuKIeXcGOkMICbbpz6BXeEaCP-egrExJZ4-Ds0PkLhojSMF0CIQj2fx920-abWaDC_XwaFZhW-UBlXaQLdvYkvrMKHa4T6doBCR29m0wGIdtWX37ExjGk6RihxeIwNxnf9mniSj0rftFewXcGKVGuKHNLTNkDFEyfSbAgj6m38HVMefQzqhB95Db597-3stbtjpso79j_VklR5QCrvucmywbodciRJdohPz9Xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=m1riKDHtRzEgexk_Hx6XRfKYuCvNJGV3vwA9DrTeJhOV4efkjP-U1G2HCrsCk2WrNfHWXWkvf6MytFExG26G7RjjdjgKVNMONSZltmtGQ2hGc097vDA4EZl80k9nKpCCy-JFoJrmSQyJcDoTnG0OvlNSmbhAX-ZuZMen0BsmXnObGQijhVjCM2ybvv5zJh7IYiRPs6KSxrxPcE3GjT1enxCkOr2L2oIqLG2nEjhC6aDhk_outcRdAPv_PkiujJWZsfKG_wDrCBSwo-OoWTjb9FX0SV-_HDmTgr7MxgZLUjYEqsqS3ha20W9TIYtdWwQANiCDqF4GmhY5FK_rMhHhkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=m1riKDHtRzEgexk_Hx6XRfKYuCvNJGV3vwA9DrTeJhOV4efkjP-U1G2HCrsCk2WrNfHWXWkvf6MytFExG26G7RjjdjgKVNMONSZltmtGQ2hGc097vDA4EZl80k9nKpCCy-JFoJrmSQyJcDoTnG0OvlNSmbhAX-ZuZMen0BsmXnObGQijhVjCM2ybvv5zJh7IYiRPs6KSxrxPcE3GjT1enxCkOr2L2oIqLG2nEjhC6aDhk_outcRdAPv_PkiujJWZsfKG_wDrCBSwo-OoWTjb9FX0SV-_HDmTgr7MxgZLUjYEqsqS3ha20W9TIYtdWwQANiCDqF4GmhY5FK_rMhHhkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ov92E4FJRmetJQbnzxJOXdumaajhRVyJJCTbOdLvNBgRj5hBRWye7ibs9hxD28O8THKHci0hzNBd6qy3nMz2CZXvKS4-bB9K40IsM4i8O-uGJehfjI5mjsx0mdakFSLLorf3FDsco4DCbvmv3QdH8xH0_m1ysisGtW7vmLY5tynTXw2_oi5pcLqJvve58i_syPy-koAetSdzdxD9YZBq5McQSADVNvd62aggF4mojiuVfpDtlRQUPqODxyJeEc2vYaBm0ZAHeBDtAiWQfQ2vz9ut7v2w_hTUzVr-eRRjhfBj6647P0ADiZH4TT65aV_S42UDSbHpS9yV_3jDJ6VAdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Ov92E4FJRmetJQbnzxJOXdumaajhRVyJJCTbOdLvNBgRj5hBRWye7ibs9hxD28O8THKHci0hzNBd6qy3nMz2CZXvKS4-bB9K40IsM4i8O-uGJehfjI5mjsx0mdakFSLLorf3FDsco4DCbvmv3QdH8xH0_m1ysisGtW7vmLY5tynTXw2_oi5pcLqJvve58i_syPy-koAetSdzdxD9YZBq5McQSADVNvd62aggF4mojiuVfpDtlRQUPqODxyJeEc2vYaBm0ZAHeBDtAiWQfQ2vz9ut7v2w_hTUzVr-eRRjhfBj6647P0ADiZH4TT65aV_S42UDSbHpS9yV_3jDJ6VAdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhNJxy7cNeIWAeEPKA32rQVOaESp1kSWduLeXzNLHoiEDoD5CQqb1VnL-X6_e4c4FnapdIJ7xzW76U4XX0S3g_VR_zqXYqkBfShCClFnNy7VtFhWY6BNvfOt6LNpvuxtQ_DniK-ybAq_Wl0zbPvEqs6sd0gBr1PQE9oWFAHVr15atwLtQPe_7L8DXJEY5fP6xKFUxsOePSEDNjcqa1cTmhhg3NJCdWN2NS9b7fU-9HVBsBIzpRtOc2qYS4baUZ3DrL3kHJSxo3fA5ReZB56W7vVW36n0r4tequjT4mYnKgedfm7L7rNiGA1vLyYewaESXi4lC7e_e_s-Q-HfXxP_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky0ZBQZ0T5YPMfVc2fyJp4kbFRQHO_DZAw2Yb3HJLh7Ocn93TEK1oyXkHEr2DfouNaUe8x-um0ibBJgdZFzQlBHt1ocRsyPmWcOjLRTS2YCDA6J3mPwYCHRGaMzjVs-FtdQTqB0EGRKSK99_L46q1G3i5ynMpVGdLbZT3rGvcEqHZmwCf2uwNHWarNZkhhUm8pslgboBK-Vk4VIovXaVi0xCQJikkihm3YIX-WXzkL-OXtcjd6F5Hln12Y3cjmkRuxbF9n4vxjsX6_7GEvnV2J2MnF51eE_s9yxuBbn1MtBiWtA62OD-6zTjrLdpU6Kl6qHfUshoHL4JGvoZu7M0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd69e2wBFFcmBb1oEjAIWkk9VvvWfyncVAIZQWjSs2PckiofFvH3_nicQdnWT47lNrpxnA3OVrxbOFnA0Wk9Lk2Iyk77xlJiOyByPm3hWgZ0t69br99_WEI8sav1i6I9FVJDr9xtZFEn9LnEdZu1XLetIHnVSSCjvaxof6MYP_rHk1vYkmJlau2Zdbs1Drs2ziLlRuvQraepRlgDiG4CPh_YYtdM16SpMxXqvohevC_oq9k4uUL_EyFYvLnESm9OZxWiZu31uyYBrd0OuYztfTdQzYCyGg406rclC8qoG5JUqZMZ6wvz0msPphPqITd-JbrR01-LYm7SSExKf2AXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=Ae5PT8gUezxTIk5pw6H-_Npx8BT5WKK-EnKuYF0o_rqwwBaxx2UtmYvwtS5PZ8h0AMAh5GXaIOMZIipyx65TpaDA7gH_FMUpE7z7v-B684_394M5JuTDZUny9o7EkAjL6i_bH2A-nGMjjxCZ-AIdLy9P2Pfl0_8LAcxhfz8E8IR_I9_w7jyuWp6cziwbHuiq9dfedqVp1IrFhKY3pEqw3ruqayrgrGcb4L2OGSsCmgZ7T6lmtMmH2UtFcQ93W9YIOtcT_xSAgQGxeXzT3NUnOF805g05q6-10GYNDJAKopc5ZmSYZ4swNkZw23vDuVsr5DOnqyrstw7ivdJRgVs1F1jcM-umYkB1cQjeZa_YjekvmwEUUijaLEkZwEpEQfAjVO3Mz3ZW_e6G75eN0VnjoY_Z-nJs3WnkBye-f9lqyKoZb2mwSvfAbXdr4TY_iUaeiFkjUUd4yT1atTnfqsHinFjWZ_r7G8cu3MEDoqJcSBy9_FBrvGpA5_6UQWJzx9sXAf5vhHGa06-XQAa5T6XL72ZR-SoZYgL1_4ajmBwsr3iVL5KHvzMxIB1ATLSmiBy-L2tRa7RmCtvolUZYn3qZ_4IZaIX_PJWsz_m0CVnt4ldS7UtER6phJ-m58vg0Cy-3kWv5chCwUCJVLJmGIkYVsCM2qJOGjr9L5nfnNCKn5s4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW2Q3N56kec2IOBIner8y4HmSmILluGaNwHntKycY871xHOSeKYBAj1a4UB9le8XQ8_yyGghMSGI5msmM-mo1zYYOjg4IGac7jfc3UMqQDTrd2tqXtsT9YLmfWhUQDPuf5DH_6hUKJKgjQx_hRIsVAW-uZ1B15mlPyXGBBeRcSBCqMX9XXd0KZM6h5FzYxKaxXGcYwgCEJalraEkq0LZrnxMpVEk5LK5lGSwJTwJITdWXzP-odFvY1zri6gd7EyuI2TjxBptNNoQGADP07yWOR7LtwhpRipmdNqLfWUxGXVff0be67C3Qv1JKV0YhgzEksMLClPV2ywEuF87K_UX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Qo8wqHHlw8u9Qdl5VMeTpTbsKwQwMdhyEZGbywzXzvt7gyvrVJsshrH4lnmZbXhkfA5-7ca5IJUcoD-E65xpnkhmUxtdhs2J_2EIHHcIpbwWqIqSjDtaUiO6g-mHSoErhgsF3VtoQwo1n5W4DtmgXWDgxoG1rRnEBw1kBlkJ1zw3tl3XDFXXsWI0NuCg9IAggR-q6YT-ufCnMEoQ3HEw1fn8cqPWZ35BZ_lgCnfP9PLONhAEzEzymt_gTsGEdcxZSMER3jf-aayQTLJS2qaON09bKsc1gwGoHQmbosHZJI6jh6wjQk8KfrGPetvGOyd1EqOeVnqgfaNUQvoD_xDCwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFNKrBPP-FwnkbjxgYubi1zoHJ5rozCxD0KjuL923o3lCeLhkjJIBksUKbwJtlIRBAxAopvfOHFr__kdt208UT2m42-MqERjO_gaKT3nRAsGWujuMPuD-dDQ0r9VfsjoM0ByBzTNaNW6NTAHIel7zgILVm8TMVvv0zbNCUl1OLgv_p9Hrd5BH02OJvPBY6NL7mH4JS8Ucl4CiwaWpDCq2N78fgTBup34O4rgp-k5mYJkm4voijkxmK8oK1QYw0pTHXv-SBgN4mNZeoDhpnzOMkb7EH968AKp8k4bNSvO6tS7ak-RU7l-BJArhs05eMalzqWoKeoeX-vl243_zEDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h-mny9qaFlhJ7Jn8ao8wFQ9ifyQzjt7-lnHjOn7WOAG32fb_NzPxwe7t3DGZcep-QV7T2xZve0MKiuSfLo2Vt6s2N9sCbZy6EIIjHmyV5TzWTideKlMU5GaEV1P7N8LIi2Eq2bE1Uu3etq6R0ZaAb7wRyEF5AnX1XLyzKlUw581S3bxNqQzefnmCZr9tn15tZFKncjgdYABOTUx7Co87G19pfQTKwvkwb1vaOSOz_1OC0DwZSIpy4WtlgRKlPBhrWriTpFmBBmCjUiOccizTIFD8XslDKENJvohxUd3Af_QSsuNUu7FEZqTC4oE2AXcV27SUXbA97J0P8uCFKd1NIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p1sCX9o0tHaU37cU8Is6ijgJUtN6Q3PcYmGYIpFUXr0d1E_aqN0P1NE97-xSQ3pnh5txY0Sv5ifuMvm_8pZbX0xs_w1SGpWRCJHt9JxwjRmyD_TZNuboouU0VBQGj8lfbTF7GQ1U7dWdh31n9aBjNmJy1mHXbfNSqr4_buQRiQOllG8i1_HbD8tIBiGJEryIR1Jhrj3Zr8uhmRaEH4etfu01NAcuSmfwM7RtyGqOwdNQ6mV6lPm_Wgg0oqBRwuQn90DmihB4MRijc-R5SevYv1e3UV9IdVTC8Yw_4YHqAtruFrSVPp1Ew35NeeLsP93LXjFXTBMSOWbuQu6WeAtfXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sdm5MygwAxl-V8q-q9x850WIvECrnRVaCJIFTF4eVCoFSx46jg047Lm_KFQ6d-1Bus6oSZp9ae9f4ygwbqhGYo-INmbe9CQuiPMx7YWgnHyx3jZqMS627jLej4FC-QRvD2NenRwMFbm4wD5jj0GYZ306-1cjgSCcS2P7hl8n_XWVscRM12HT1gNEk8I2-WfATblP15mbQ4_hnvYM8_8dwHjSa-TA6j5HeziF1fyxcMD6Q5N9hHetYOmtdcFnY9acF_OeMXmHYKKUuvqkRM7q9Hlixzeu4yz5T5Y0xdihadve3A4vOURcBfPplTXMt7V5wqoSb1hSoyi3OhGoskCeuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5y1a2KLuM15rJ58ws0N-_7TNYsk8hCVtYvu_WTpN4bvuVqVm1exC9lGsq0FVYID1hqr3pT_5kGWC6ZaHulBhKarW2ge-g1sIw8e0Gm3XtL0Hs-jBkCOT_PL2aYoEcHQMb1xdb6p5fJGKI728c4v_pc-dvWYU3fQc7fgMws_4nxP6SzcThO4xL_nymww-yjZoZXpnyGuVwT9sVICG_VmgzEr_Nq4vpRh5BtENJV8cRLnIkhWIc82zj6y2f274w27ovyTNJ8sO67jNjfIQtEr0kGEuH995rTwqI30S5qG92F9CRPF8QGVkLSl3SD-7iHCmXI4RJPxLRBQKyA-8eGyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUOvCvOioHaohVvdQUwqFVFlrf9mDr8052V9KwPk7siJ1p6Yu42xkKfaBWY2u2yr1mXYqnxTTZN8bDEaWtxpA2UmX__c_AnWVHhS68vJRvl-7oIa8YXIm9A98w6o63JsE4dYknj1zAf-KQAjqO7CG7iM7GNxkSCXFerdG6oiNR0Vk04qWUu8J9uz5_St0aE6PRvfmzHiyWxjJlBUMIkxcAVvT2VlxKI3U-2u-BU5nSoBV2rpJc8VgbCQO7K4r78UG0lxlbJDha9JqQz1QjcE3CgXffTXvO7kPX7iJhZGU0HVz7wX2G0i9AWboE2SJINersqSNqEJmHgDBQiyz5g-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgZcUJMDArRCPqeXjlSfET_edqJu3z4afyLPYNIpGkh2_thGVRpqRe14LBtueso0GWWvIxuIJkxIrwMaC5tiPNxD16zFr4insxcIJAzdUwFfKVjuJ7XwMOOegpYykTOFATgYVRL_8DyPYHzjo1idSnSbIBVTPe2awEq6RrFnE--gwWBWpNz3jnvcIx5cFvxro7YHppHE2ZnbsZ6kzP8Kw8Atirw4OwyotPs-NhpP-PkbB0U79beK26X8dU6RL6DYq-8FwVjhiWVF0jR5mOz2v15Ntw4wAiP75gXV5KTHIqEUxG6b6GDBKxAKYx65oerLstJ3TtmLqqjVTBz-innbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4IDF5MfaAsL3mBVM5LmhPufq8qGtSl-eGxdKhMkOeil95u5q3W_JDOmJ9d9Kj2Nl0swaQa0CdpuqXWwH3UJ2grY_bAA8KXPtiQFFlASt05r4aPa8Iah4PqM38ckyFPc2EW1mnKw2QVuvPL8TjCXRKf_FokH619kmbe1UAHmc5L4QAX61WGkoYBHfg9GBZ7Bq87bIvrF0gAgSsNeTEIhuPfQeLcREhbOzkXif_EBo0x-mMzmdsru6dBMVChFgcDX7_7CUoO2JCFCNTfIaWxVUw3gmt8yf0Z5zT2L4zTk8aDG72KV8ouqLlqcAff4RSDruaOT2e38g0iTvjUnzN7dBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqOlAIiuW8o_6zzZgpLQaTdSjFL5jWS3fwresLgSnCo93_4gnoeoAZomwPz0G02__UnE7A1l2y8MqosSDqGwOozDkgh8T9NxOu8P0Ll66kqoRbeVwqK42YWVseYLk3BoCoPyN0mU9F4GnslQ4_lthrYWC77sJYqhVaFV4reyGsGRgbWmBmARw4rkVjEQ3uYQt9FsXJTuHav4xK5avZrlqDRTafvXVwQ25hWt05kceGbPFZzkS_8ou98t5Z32Gc0vc9monFtE56V3a9SLgxzcgAW5D5wyQR5Rjq75u2egtHZP15HkxVfF-iUcoW1t0jJIE2wxUnJ1sfuXxl4HSlJwdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szbtJ1tjQc3JoTjJ3F2ci02dT-_HvVRGs0mVu0lZHewOVJ0t3iT_l8kVD4td8xX7Hl3uhjRna-eqVQAUobsrzC4Q-6_APyvQ14DXz2dj9VFtOTOXTYQfzo1LqQ_fg1ssf2Ufh_mKYu4jd0_hBU3joGZfrk83fZ306Zo1Wm9fydc6O65Rdu5wABsq3mN26Oyy7kqQ0ra52TCY_mkOinEIB8qQZi_lcwjdN9YEZmCSJ4HqHwzB6vEqHXthCI0V5Vp_IIip6DM_z6u1zwK11wUXF4vrOljyOpfGvjIZIh7mxfV7crgSPa_HM9SpqZyZilDBYS6Fsb_ffoHkedBfVFKWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEfjkWzaccIT_q1H5sf82LOnW7aPrNWcKg-Mp-xmqqeo9qpyP8e9Bv0hRjsNf68NAVIP5acdkAsCOIGZrynotwi-foG35iwJi8fWxj2nCe20sM3eJtXYjVgEj5exqetp1aEpQghZkXWXoEOAH6bXwW6kzwUN2N9rFlbxzkNn6I8S2kUWNcWI97sFm5E1_woNrZWAaguJihln59tkKzx2TBp1ud--w7OhWAXrhat62_kM9ixsrucy9XvMQYRx3LJAGA1Oi4sK967TD5-mM5mFxySrilWu17mdVdffeot1-SgZHDdIRhfC05laWo-vyKptcKC33i0jBQxrTnl3nJQ2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMdPDQ2MOKaYjvWGOftjlD1gPutQHY9pph4ryU8ZJv2TC27VVa2c_bRbjGeXRdwzKoqP-Kp4yZF3ZCn6oVJKueWqdlGTX8V-vhGBOG5lZt2k4AY4DzmYqbrDlHfh15so6dQT5__wYRwrYy73TAZc8BdTfMVfSqsvIvAJS29G60-GGJCyVNKIglA_XtRzY_LssjaaBJR60ELDEIv3beRxJUWF8PkRQGGDCPmuG2jmQrMgXo0UubRSQIHekRgcSsRGfvk3ls3gP4DhPCATvDYUN0MH0ApUmC1bDIDJVnBonQ18QPJjz8PwwQJfoq5OEPP8irRqChMUgzB7nN861Obsyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEV8tS_ovPD5jKVoKP_hMCL8_B0lF2EK_xzdM_iGCs1mxxm52jzJyYswyRJmB2ZuvJXNp78uhyGx4qSGAiCmjBLI91RqYnyIgiZwU8no6WlloNul9O9pmn2SZ6y6s8epog8Ec09ztEFPygmiUlCcULb34tQ9ZCDKV_UD5KMvopKCaZaGK_QqYBImVQVilUUiQzCydT58iNgLPL53nFyO_qDy_5_1QLdgFM9Fds5w8YyR-uqBdONbDTr2emKvndxWA6EEaS6OxeqAlJ5pWR16YLEjP7OvkPq0ol0BhWzpraAT-6Ngo4RXl5mJNj7pki1eRyvJ3ENpxkc46LZ3GrOC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbWVzPSe37HF7cjlr89CADWW_n_BXpqH0-SiAmfUZiMPOAPq790zncnml3Ij2LGSKBbokD0E3EagWI_r6ahQT1lh4rjJOIyadb8UgVWmA5AZoUfG6rr9OaNgAmmZrbKIYazZJpMpO67O9bv-3nA8zytohzTUX5Y-F1Po8lRGONTzW3iJWAJfJl1WdB6wmznQcv7-sAOp1BsVTG-eldnanAXjBFRV0sxwtcudcdaAGkWRLhdC_NXwolX7iIOWob7WVHwQjsWw1J_M9jsp7pSDCAoKUqEtWVSuD4r_BassqzLVEhDtRlJJiRizmFI914ww9ch30hv4SfX6x3JkRoWkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrRU61lGw-zkW5pcsc-0BIqanImbeCwaTZTdPn9RaPpGPgaiGwy3YKSbKQ5CG4hYZ680N1LELguCNcl_UzzrF4-SsAfeHlb5i28vzScmKgF38082Dm1E0ek_3MqhapQVQXohvNdzM8-R0B0gvGBfoW9SNb8YfbQpYN9JkqW5i6_8UDY-b2OCG4EKzTwXEvSozrVZsnOXJGogeZq9K-9GbxOe1BRdZhIJatsT8fmn8-mkxM4we3GLVgqzucNKrSzTdYMwC_2eQ5DqyoBq90g0VbTiER_cv2JoxXwQckpBVqDWXWXR32gfSiLwFnDwlEsDxD-A05Bh1A4SZ1zNQ_YX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4SdFZioMgPaQGTAF7vSRL55Ph1eAvFR2HlsNFtP0gHkO-363z18Idg6Ti7XC0sNRK8eGQ9t-eAueGLd4ImGEMWmrLDkV5cQ1qkZTnWCU3TSVAtD_GluZEqWjzgfbbotTw2FPRqf6spuWGPBfpwzvnh70TSaMhDQpMMg40DKrYlXiqHsFJS5UA7wS_uN4y5AZztVI6cHUy55_AIndbKi5hPn5sxR2TSn5cJAe3oJeSh7Cn7Ius1XdK1Tu5VUuFLglGZ8K3Vn3jO_VGcaotdgQ0M5VZ4yI4ZbyUKICBUYKvJSnnQbEpR3W8DslwQq9aGMWMu5RvVrLoGbTracOhDpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n1sBQkbSUmKUPh2m-JI1w5fObld7W0KPBeZ03pIw7q-69jNhe_3qBnYGtu4czBPcmndUwvXbk-LglrBY7pe8kEQ9PKDxKDG8-4ruI-RcBCe4y1nPbYOU51xwZ2429YERLm0omBj6T_kaaD9Vmfr5vDsjwcBbkymbHYawgjv6KMZHS_7zoj-x8mR1j9cRUcq7apQnCU97yKT_nNPcyjmwg0vBkqsLl8bLFkg4IuIk6dTFLBKTn-mDXQYohUnckVy9MFSHUwHkrXfk41OpCymZHv9LhkoscrtyCwUELqDfdTemZyFhqqQKNFIM7kQ8UOZu_jKKCsTdZNTybzcCBv0Dxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMQqW7DcEkW92ACtpGKotf9ZoiNiFd9GEUEyVdOzfn0GfdFBvmjGSnRZTsRgFvM4KFtkkgUbL3RGo8d4DL-BNGr4P9snDlOqlTCYEokkVPODaUwOTLDlbGdWgZedFaKraRTdpZWNM8rMR00KGgrTznEWl9YKznY7pE7FGH-QLM0gIw0MT3ZEegB8GcV9mI-3kxsANBGFBrpE_1qEpdBsEe-99YgYNI6oTdhgyW6rcNWMTr3mDPYWeoTJYixqWeZswtMmptI6jFndOUBujHbVJ8ArwRFEuCupjna16e9NxTiaNwHRaEuCAzgevH9MABQ6CD2jck5CXxDNss-LPsVn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=Wq0e_zqvJJ-CXnGk3h7_kvC4zPPn7oVA23KIByoRFGCuCOGeSuNyEcyQ7FDNeQQWeixfwYZlgyDlmfVyAN_hJ0o_dH_08XS3TlgAzuEmQ23v2zF50E57OMh_Rlb5AWtFeU1cscP0S09hKhS5_gyMh9d7xxH6fTq953AI1Nsy0QGCabs2dJAGZfZJ0GmJdVaIlRu2X14jc5MaiIUGnMlkw2Lv72qkVWV0B3a6Kocm4UljmB0Eck7knhNOdPdy2eBlBUUJm71s4z0_fK11dPqqX2-tlSF2En1NCCkKENsKgfBZVIRLyabSEuIO-Zm7XhlWd5f80E8S8-OZmKzK_aMaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=Wq0e_zqvJJ-CXnGk3h7_kvC4zPPn7oVA23KIByoRFGCuCOGeSuNyEcyQ7FDNeQQWeixfwYZlgyDlmfVyAN_hJ0o_dH_08XS3TlgAzuEmQ23v2zF50E57OMh_Rlb5AWtFeU1cscP0S09hKhS5_gyMh9d7xxH6fTq953AI1Nsy0QGCabs2dJAGZfZJ0GmJdVaIlRu2X14jc5MaiIUGnMlkw2Lv72qkVWV0B3a6Kocm4UljmB0Eck7knhNOdPdy2eBlBUUJm71s4z0_fK11dPqqX2-tlSF2En1NCCkKENsKgfBZVIRLyabSEuIO-Zm7XhlWd5f80E8S8-OZmKzK_aMaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGhugLW1r-1Lu5J8FptG4XVWrSScGkjXUBB6KvK5IOijdMrScLurQhVFPuJRt7EUE2ymaOEOklb6uAud3ifL9nhnqqEsw73MP39vBpIFMRrlEV6-dx2nZZRhFqWBvCZPV9KWHTUStqFgyOt1xl5u-0smx7XcW5UZgcZL0YGEjUeg-PBaP9-NwhKVLINBgz_cIt5VVX9U80wFgRywRewNrs5TM4Nq-MPKXJPLcWqsLWdUsAX5IoPyRFUMzQOyofpu1Baj2aAIQ1_gjC7MFvshMTWvS00_AhSTxliMF2skK7RI233xM_LXmSuZbgEnp2xaX_4-wp3JQ6IbyIG0Fzo12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omdzGOOTmCZdRULEM0WIvUM6DoX5-FKeLX9hYWGS-ldzjYer6pu3DMJJJ2gjhgQotQy1KYuDbn8T5jg5M9YFKaiFS6yEahgrp1ij6v6UxUqCXHEUTgLcSWDAX9HeNLO0MwIo-9TNbDHo9CbkHh7yXOP5HHv40otLlqXMu-JWpg3nKbvT-lTALjhgPlc_hgtKqHuTrl5l8tymWXjrAwmyPYybJc7Ex9dMjUgfeLkWnNkTuM0I237kj-YbM6e-J8zboDxOZsBLQejHfk_UUGTJBCfKSdFlS_wVn_LJ1qDYFOfOJsI6O7b0Gyl3pB7-dPQzz7c5aGaocx0_kbhfgn2c-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4iwMT24Mhchjn-5Lnkan__cx6azimlBZg9hubQq00jEIL0oMvqal0esgXXVAy-Dt4-PVAxD9k7iaea3lReq6VzmS8Ff-QOteQopCsjpENAWFxZ6-7v1xesYctOTco98COVndYrPL0WoxZ_tnJ_9vxNidoW7FHryOP4YzDrWoPv6lSJa9BVT6qLwiqKa30tXtaFq97dM7onOKKTiA0QSp2EP1tOnb9UAhgxmPrWR8M3QOSn9JdpNj8VpbfPCjVUmZkblU5yIn0Hv6DN6jTAp6pJ2zTrnCllgeRa_Mdo-gIKCFVeStvCPxwSvUy91GLsdydp0UW8vGm0sLPl5_aIohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIOZWQtnCcEcddBE26mGmr_Yf8LEBujSb8TJdh6IR6S5ubQYkXdaJ6JbFqzCdMDb7uC1yt_lbRgdP78YJnd8HVDQqPQ7xjPsAUcCqQ3oErn7mT8Wi7IGDH7r45WaBJLBHccuXqBr29GLKzDVbEKNOiYkhYe-XA1jRCYoOLSgRs5Iv0JBWkaEv6S1-wPB2wjuRksJp1TTtJvOKb5fwobZQvsbah4xcBozm2Yvdp-3nR_91Q2mr7j8VJhLQe6d6Ub-i7OCO6T2mhn7OCrGAqkGi_HZ4TIv1xX_pHiS94dHdiDnL2ekXcPFjAEAgLQ4dy1sfTfPCIQjglp9drJ7Y0e3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=H1ssLJXGGj-DxgBioYPaLDJa-NVbD7V8b39y98cZOolTTq-atUCYrncX_RQ6PMKQiap1GVOXNhBouRW9h219VEYrQunIu4eaUMJwlzSlD98gZStKUX9Nn0ORw3q87dwIKuhYSpzF3IvbLhSL4CSohTLQcQiwPG3N75w1FDvM6RlzF3ujVAwk0ctfNRkaRcnPxfzCVNAO_x_AtyT4pZVVqC1NKV7Pu8b9l4U65joODG_GKQqi7KzXyE0IENLu2hjpjbAbdPxucm0ug56Rj_y_3A_KHrYZxpFthaDJZGOAqoIdk5njICgqRJOIU9Qenjum0rYLgi1QeRU4hxhgnxWL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=H1ssLJXGGj-DxgBioYPaLDJa-NVbD7V8b39y98cZOolTTq-atUCYrncX_RQ6PMKQiap1GVOXNhBouRW9h219VEYrQunIu4eaUMJwlzSlD98gZStKUX9Nn0ORw3q87dwIKuhYSpzF3IvbLhSL4CSohTLQcQiwPG3N75w1FDvM6RlzF3ujVAwk0ctfNRkaRcnPxfzCVNAO_x_AtyT4pZVVqC1NKV7Pu8b9l4U65joODG_GKQqi7KzXyE0IENLu2hjpjbAbdPxucm0ug56Rj_y_3A_KHrYZxpFthaDJZGOAqoIdk5njICgqRJOIU9Qenjum0rYLgi1QeRU4hxhgnxWL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=JCM16uhNZUFZ3MLXIAnsgCY0gLROB_BRPPjmK2twFsjQOU4nbas2QrNXevedl2vbRztT7SkPsumFgFXTixZZ0Ohc2P5CRRrFzOTScqXmQv9Azpw18hzlaCpQlMwdYHIVAmETNOWrVa-rdZ7y58pNCPxPQo_8r48ogrvO8uWa8_N_w9UyeKgzzbkDk0aHn8RFDTMb2_AiTlKHSoN3POGC7batIAUoyRtvgh0_83gfTrxr4ajviohjsCa1GITa5yb43ZnMFSzThpJdjrrwAth0yEGspSihNx_QXmAPFeu65ZumAAwyljiriQKuLYbe3ckkzK95n_LRDtq7h97IwKrHjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=JCM16uhNZUFZ3MLXIAnsgCY0gLROB_BRPPjmK2twFsjQOU4nbas2QrNXevedl2vbRztT7SkPsumFgFXTixZZ0Ohc2P5CRRrFzOTScqXmQv9Azpw18hzlaCpQlMwdYHIVAmETNOWrVa-rdZ7y58pNCPxPQo_8r48ogrvO8uWa8_N_w9UyeKgzzbkDk0aHn8RFDTMb2_AiTlKHSoN3POGC7batIAUoyRtvgh0_83gfTrxr4ajviohjsCa1GITa5yb43ZnMFSzThpJdjrrwAth0yEGspSihNx_QXmAPFeu65ZumAAwyljiriQKuLYbe3ckkzK95n_LRDtq7h97IwKrHjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=YQ310374SmuB6DDSJunKlsErhJbo1JI-FFk1y2Pjo-VWhGnlcvhOMguMBcuNiTI1isrWB7K8lmCsMKPzN7NnHZ4SNcRoQr_Qn-vBI305kz63pccEb-BMxpSfkQNqm6qJok4Hs9GibVVcuscU5M_iqysdBC10F82qDcJ01BFquej995-x8vf6Xxpt6QZ6WG0KA3QPu0nLbUpqNHImNUEWgg-rB5jtEXhh1H-eC3BlxwOGFGauTQxpDhjGCQMOJUYzX2T5g1U_V6ps9ODJD__8IIthD6UK0rpzuk1gHZOpvSHpc29kftXqstt-9Db6q0adUQObL1rRU4C9pX13fyZsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=YQ310374SmuB6DDSJunKlsErhJbo1JI-FFk1y2Pjo-VWhGnlcvhOMguMBcuNiTI1isrWB7K8lmCsMKPzN7NnHZ4SNcRoQr_Qn-vBI305kz63pccEb-BMxpSfkQNqm6qJok4Hs9GibVVcuscU5M_iqysdBC10F82qDcJ01BFquej995-x8vf6Xxpt6QZ6WG0KA3QPu0nLbUpqNHImNUEWgg-rB5jtEXhh1H-eC3BlxwOGFGauTQxpDhjGCQMOJUYzX2T5g1U_V6ps9ODJD__8IIthD6UK0rpzuk1gHZOpvSHpc29kftXqstt-9Db6q0adUQObL1rRU4C9pX13fyZsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpNhJmCd_OEd5XbHNcPA-VQjBiahCqc3EqN0fPhl4mruNt1uLV_8aIaueYg_U2f70TaVrvUdOPHW0yGtJurAqIMYSfaCuzTFG5cLS3U3At5LIa3DFrT3QOA8Ev-414RS5yxoR6V7VT0D0YaPPHRIIrbtqbUCPRwFRQcadh53FsD0IcwvHJtqX1dtAnDpS5y97RAMtjs-yg-nKaa2fkVbF-JwU5PzTcR_Kl5vdFz4Wup6uCWsN8hkWHAGP7QlKOxZpyVU46WMfY_IsFXB9TBGAdpeuMfXbQTPWbSZUFrI5ArXIYmXrTCRnse3vRbOgMHLPLcvmNjEo54tNR72bWFfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=jwAOfCCy-fK7IGd0Hji85A7xTiHFuP3AuL6WTsgY09Rm57iW4-U26xcPND4r6Y3WBrRbzbJkGrufsweV-2NkF_NEHpsQBXxA74v-tVEsiee6fQWmE-TdfD4t_ml_B1Uuy1vsvBW4KntIqu7TiCsXU3I4YLqj3a_3YCrPhzZj36US9WUqQlkmEiqRcN0lSYkNzcBgV4m7Q-ygVaPD8K_y56UbGYsj5mohlBT9FLMTTdbA97eTaH5lsCWV_O2P-LgRZYNOWrH9lUk3Xh6vhFQ5zD9tp-FjF_JpnV7N8alRm2zXwALFdeMI3zpOid31vDGEwOk99gTMF3URcIvMVPOdWTyVtw3YZuk75TQZ46a-wV1P9QwIVBHdN_21QA6t20srVnHFhA4Aoy2m4M-K8IzvGyhVtCIKVPySQH8trmS1BoJOA368eX69FyDA4wW8U2fZm0juK4RQhN98ORrKjVe1HVP5mBBUaFcYUPc4fHWEH6TJSNAM-fIQpGadlmQelQ7qaguFTp3aS4RwTRRQE9yGhkxKnvTjIzvdXYrYPZqtQBlqFpgDF56WUNGwxLwlps7tnfk84hBgUfTPPFB5Fv7oiHYdVlx4o5GdNN90YRThQneFN4UOd1DkWg-SG6_UmE30x_RLnNQnZAOwi2Zl7A7DlXH6E6AaqutwO3cejjoYztU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=jwAOfCCy-fK7IGd0Hji85A7xTiHFuP3AuL6WTsgY09Rm57iW4-U26xcPND4r6Y3WBrRbzbJkGrufsweV-2NkF_NEHpsQBXxA74v-tVEsiee6fQWmE-TdfD4t_ml_B1Uuy1vsvBW4KntIqu7TiCsXU3I4YLqj3a_3YCrPhzZj36US9WUqQlkmEiqRcN0lSYkNzcBgV4m7Q-ygVaPD8K_y56UbGYsj5mohlBT9FLMTTdbA97eTaH5lsCWV_O2P-LgRZYNOWrH9lUk3Xh6vhFQ5zD9tp-FjF_JpnV7N8alRm2zXwALFdeMI3zpOid31vDGEwOk99gTMF3URcIvMVPOdWTyVtw3YZuk75TQZ46a-wV1P9QwIVBHdN_21QA6t20srVnHFhA4Aoy2m4M-K8IzvGyhVtCIKVPySQH8trmS1BoJOA368eX69FyDA4wW8U2fZm0juK4RQhN98ORrKjVe1HVP5mBBUaFcYUPc4fHWEH6TJSNAM-fIQpGadlmQelQ7qaguFTp3aS4RwTRRQE9yGhkxKnvTjIzvdXYrYPZqtQBlqFpgDF56WUNGwxLwlps7tnfk84hBgUfTPPFB5Fv7oiHYdVlx4o5GdNN90YRThQneFN4UOd1DkWg-SG6_UmE30x_RLnNQnZAOwi2Zl7A7DlXH6E6AaqutwO3cejjoYztU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=c8FRpnnfMoRK2EJpAhFqjnz7FRbhEXTjg58MS-u0ZhraXKygIpPlpskj4QMAbUyc3FAtBEEE81WVtOICNH4Rcp_R9jYhjC6tCOXwiDP2vnM59NnRrX8atyZ0eFBsWQ6V0WyRXXn6K6bBAbSXSSxFpUDYpW3_ljEC5aQ3rE0PXaGyRNMCcPk_d2qk-5tYY7cc5xcHiSwvLKqVNIqnypiJbhSQVoJ5jXazQedsmDT3bs4Ez03GzPPCyZKBJcoyIafdvutP5t3tlgUcu4L1wYMVVYQfNv1sAsudJdoT7zvSjdLfEyUg2RTpoF8YR1wdsmFFcRX33jZ-bWZg9dxs_WvIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=c8FRpnnfMoRK2EJpAhFqjnz7FRbhEXTjg58MS-u0ZhraXKygIpPlpskj4QMAbUyc3FAtBEEE81WVtOICNH4Rcp_R9jYhjC6tCOXwiDP2vnM59NnRrX8atyZ0eFBsWQ6V0WyRXXn6K6bBAbSXSSxFpUDYpW3_ljEC5aQ3rE0PXaGyRNMCcPk_d2qk-5tYY7cc5xcHiSwvLKqVNIqnypiJbhSQVoJ5jXazQedsmDT3bs4Ez03GzPPCyZKBJcoyIafdvutP5t3tlgUcu4L1wYMVVYQfNv1sAsudJdoT7zvSjdLfEyUg2RTpoF8YR1wdsmFFcRX33jZ-bWZg9dxs_WvIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Pf2W3trp7fBtFubSDwUGoP-KaHXISBKW8cpL6x6mWypWoe33XHQgEEauTdm0gDfUYANXM10QzqNCI5ZLnotAB1TnWCyp1gVWjplm7Zb_C9VwLf2GtWipIsjUNNl6LSeHI-7bOMmO2sDNoix7CFeDXjugI2QIdAzg7YlVn7aqK0yoY73qf7NRwNNXixoo2aqT4sHs5gDTezsdpRP_FRCLWfpfJpf1P1AdmYJoaTFsudVJL9jVSdPscaOer9ByLEA3_N8T_O1FfvP_cJezR2JinuAdKPnODpASnWhbAmIXk1LwuzsfUiEYmDOXMlx7bnLWz86mk3STlcUJ6s83nJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUBO1A0yvN3UkqmTRftJOQKd4vTubgr5KmkvRNdUsRwmyI556CYIX1CpIWHCx970hxGVWQ0N54UAGcnbjn8hKZ-4e3DMRSuMh04UvQJfNRU9KoueFJacbfxfyiN-i176Y1M1xZ22FK95sTr_QQORYz9rWTAUX5q9n2KBber3LdI8BInKK8qMo-kHYVxSsNkahYWBlKIFGxyDvB8oZ24cftF33-9hcUOeMK2FbSuBRii4HVbCroi4QQREQn2Cq1jRSIKmfJj22l2eMyApepMp32dkI04foR9l31G-7RY5BWXI5U4N7JiRybejfHBNcjiHEITPskbdoDMgS2uoXqhk-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=SrG9UFAp61TLNpWweujqqdebX2E85Qt3R7RgewIc7a5hCI2TZ-dkqwIy3pqdI_D80st4C-w7cc33zaJeTjCvGBVGKtq2uGWz0a8HoGknwaeE033Ey1IkJhgO8iF3Cc8QrQVpT6vCe659WAX-BFqHzhtnwXEn4-pi_7cVkcZcaaQJHUCbHFWc2Fn32cCUFHuvlYGIHY3DlYwHipOdQGk0NNbST07tHF2D4urLtAirNEI_5OOLjKG6Oj3vr8Ukc4ZlA8Z3nnAER2TY3dCyQeU3PIyh8JzPLPUOzhO7MBgndW-luCqaaZBmVrtJ8panbs9jrC28pPup0ww8Jpihn9TvyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=SrG9UFAp61TLNpWweujqqdebX2E85Qt3R7RgewIc7a5hCI2TZ-dkqwIy3pqdI_D80st4C-w7cc33zaJeTjCvGBVGKtq2uGWz0a8HoGknwaeE033Ey1IkJhgO8iF3Cc8QrQVpT6vCe659WAX-BFqHzhtnwXEn4-pi_7cVkcZcaaQJHUCbHFWc2Fn32cCUFHuvlYGIHY3DlYwHipOdQGk0NNbST07tHF2D4urLtAirNEI_5OOLjKG6Oj3vr8Ukc4ZlA8Z3nnAER2TY3dCyQeU3PIyh8JzPLPUOzhO7MBgndW-luCqaaZBmVrtJ8panbs9jrC28pPup0ww8Jpihn9TvyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JLp9NmV8g-vCGzadsvWtpHXQ3pmUXRlAg_M5ZK2neBMDFRzVUCoLxxGqwCcfYl5DsM8Q1nGNxvjbb-C-sprhByT_0Q7rG-LJvqFKXmtcU0vymUPShPHxh7QhvlEYP8CZcEKLmpvTFaHd_3jAImZtJ7xnQ0_-NIoCl-NikW4mAz46Z6JP-VvkO3DoOuYGwnq4ncrrC8zMgx7bNVb1boBjL504vZ0z45p5crqietnmmXprAuhQiHKN1oLbM3jV6cpkkaJDrV1MV67hca_jB_xyx7LmawKX8frfaY74HWx4GcbDUoRMevTQYgs23uuPAQOUzD9Km9nCNZ798ytwCQq6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bFB1zxwY4rPrbWLCgnIlgL7yzQp9o7C_-IydR9CrBs8cchRZS5Thu-rFgraoM6R71yzl7HPaltBwTVYz74CLmqXrV0ElbhM0pnpn3mcHIu7QlD50Pq6iVA2pR02TmAKxLHIkT1Ensg8n4MryRXtP20Kx45z33OykGwCasYegaWwWEhjbJ1tEG2RektpSIxEhtTRXt5vXVQZwkqTr2AbHPnxljvrzsMWUp67jHCAXwVjgE4eIk7smEzAFo0LTe7nwuiiVBG0lFIY7V4Tugar7W9xXCtgw0ySVFmes82pKYCeMhUcY3d4kkIQ1idcUpcxevP_32nLHzo-0U_xvzrGX4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=JzbvEYMpwa9HLp1pqWxC0-aJqh1AwjFsJG2ZTK_O1m1O33DFTb_E5VMbHrHITLu9ZCFRgNiQ4_ysY_ONOuThY7iHoiMuJlvPzWyj0xUGT334h3GU1IGFGKf0DE6dEAMXwy-okzXHC4YSlCsKhdDvIvV4DUkd-085wa82VK_0LT5LVyVN0tVk94XcD8vgDZf-0XTemyTMaMDMTI-Dyxv3800DJ4dzCi-aamiUj6hKm-xWuIhct2I4Sl3M0FKoPEU7CbXMUgTaieOD3T2rElr7wZqKI9AQzmYzX2pzLtIcHZt0Mz4-YBtPXKg0rEbR9Hxpa0MaGogJ-1gnFIp9j3u61g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=JzbvEYMpwa9HLp1pqWxC0-aJqh1AwjFsJG2ZTK_O1m1O33DFTb_E5VMbHrHITLu9ZCFRgNiQ4_ysY_ONOuThY7iHoiMuJlvPzWyj0xUGT334h3GU1IGFGKf0DE6dEAMXwy-okzXHC4YSlCsKhdDvIvV4DUkd-085wa82VK_0LT5LVyVN0tVk94XcD8vgDZf-0XTemyTMaMDMTI-Dyxv3800DJ4dzCi-aamiUj6hKm-xWuIhct2I4Sl3M0FKoPEU7CbXMUgTaieOD3T2rElr7wZqKI9AQzmYzX2pzLtIcHZt0Mz4-YBtPXKg0rEbR9Hxpa0MaGogJ-1gnFIp9j3u61g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=UNLfZjdwDxTy2zUTcVNsC7K80LShDAqi4SRljN_fR5TCGw9q8QchDQrJbD3cjbRxBlYQscNbYjyKgcIY6xv0wznV_NzmwcxY_x6e3sa7pArsdeaI7VmJPZLtwGgYy1b4Qc9L7ViY6pGIhhwQsh8qHHKYstmGqDCTCWZRbl6__LvaEuamXb9XC4Xn9Bz7ZVOKQfTJxepK52wBB6gtbqX9am7bdhXPt4yTgAh7s4I419lwmzn-a6vVPP6Dr6zv2lAXtFWFpZMePEKQY5A8lbd8h7435WiVvyzwtgUI6xOm1AxlSbg5P92OlSRClkE_Q5c8nj-XprM4rhcUiKlx2-qNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=UNLfZjdwDxTy2zUTcVNsC7K80LShDAqi4SRljN_fR5TCGw9q8QchDQrJbD3cjbRxBlYQscNbYjyKgcIY6xv0wznV_NzmwcxY_x6e3sa7pArsdeaI7VmJPZLtwGgYy1b4Qc9L7ViY6pGIhhwQsh8qHHKYstmGqDCTCWZRbl6__LvaEuamXb9XC4Xn9Bz7ZVOKQfTJxepK52wBB6gtbqX9am7bdhXPt4yTgAh7s4I419lwmzn-a6vVPP6Dr6zv2lAXtFWFpZMePEKQY5A8lbd8h7435WiVvyzwtgUI6xOm1AxlSbg5P92OlSRClkE_Q5c8nj-XprM4rhcUiKlx2-qNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=uHgwmlrZhrHtixB7EnGnSoxLBxuEH4p7XYu0BtMsfaUa76mTEGjvtjBSO58AVHvKAlvTGvN0n4AZm_iTTIVlOOO_YKxmBlwHsNx5vgTFU5Vr_PmV2ltLrqpaL3w9AQS7aJzZ9XORUejJzsMMArVpR1am10VigfJ4SOvVsPfvdNACsR2Uiv5WlYqXzirfgPVLADtNN43AZ_R79-ZTKGcdab7WHvxBz8CZYlo0KDluJBRksHq7HxFAO0IkIn39lbzzjJqKMHSQIQdJP2vAGznHNR1iHzlwD4iyfcT6u9rb8ysaDuybyb20jaN4gleZOyqeCISF18j56cACJHj_hP1yhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=uHgwmlrZhrHtixB7EnGnSoxLBxuEH4p7XYu0BtMsfaUa76mTEGjvtjBSO58AVHvKAlvTGvN0n4AZm_iTTIVlOOO_YKxmBlwHsNx5vgTFU5Vr_PmV2ltLrqpaL3w9AQS7aJzZ9XORUejJzsMMArVpR1am10VigfJ4SOvVsPfvdNACsR2Uiv5WlYqXzirfgPVLADtNN43AZ_R79-ZTKGcdab7WHvxBz8CZYlo0KDluJBRksHq7HxFAO0IkIn39lbzzjJqKMHSQIQdJP2vAGznHNR1iHzlwD4iyfcT6u9rb8ysaDuybyb20jaN4gleZOyqeCISF18j56cACJHj_hP1yhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNN0vsqWFr4IVPzDkEtAb-eS0spl7H281lC4veP1j0RgrdicHu-hr4Lepx78zJ2I2h0Hb8qbo9T2Lvjm81sanVurQa4o3yvgv0cphVIjCHsP5a9yux7V1yrggkwQufyrf6w0bYoK2VGGC2e9pw0LMbByr0O2dwqKAulR85hGvebZGBoDevzgFR6As9d-vQckOpDqw4F5YZIXNgRt08HZxo4aXK6GIqLHYngPC1I4dj-dCJTrTiM3TeqKvGDjrye_5njEdtIhdbxMusOVWkwK42a7L5LD2jTIvbhQ-rOjqpwuNvAHaVdd4NAOBm880KbIFO5EWMvr2hyAHamRsk_SJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU-ImU3Ab5u-lB35qdkTTNelcv9vylanvlf2cdjbvFiYWFe75eJGh4ehd-YpRRgOB53O2X51SCw9jM-dhIDR9wO8R5-Vw-ynHhuW9di_I8GY3WWnHsp3-tpqrECouNdck3-0b6eNV3HdA4w8o_R1CuDTyv1HJiwf1hJ7nwkvPutsRNHM1-WHHz2D-MdAGRI5W_mizXKvjT5jSZFYUZwazEJeq8NiWZHxwbG78kXpR6JhXzseX6EZljZ315G33wGIcbKJLvS3aECLQqGtXwBqO2rKOBL6CnJTTFnLdsXAnqcNfeb0nRGZoW5XfKjkudkIuxB57Yzo6SQwEc5EVPnpug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=EmUFrZDgObMzv-iY1TdT-YhR1WR3eX_JqQMnqeV43reeH2C6hS0BStL2ylClENJuIg71WnqeoXD_gQrdMLpo694NwEyQSWMsrzqKra074-jMBqF7xy-OEzdsnR4bArXjfrKRaU47ctTWkW6A76MIrP_V90Ylaf7YFYrW9R_iifM-z39f-1LywrnFcZGiy2Eens57989aIz2PYL1iVnl3ktJk0to8Fo960n4fV8mgDJvRLUWD0W322tfUtBxpyhhzAi2bRYb5cunlmpETg11_wQpefb8VxOzX38TS7t4IpDAWmstPxEflP7Q2wC9bgIIOEEn-DSCGqvli6UmxVuY8-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=EmUFrZDgObMzv-iY1TdT-YhR1WR3eX_JqQMnqeV43reeH2C6hS0BStL2ylClENJuIg71WnqeoXD_gQrdMLpo694NwEyQSWMsrzqKra074-jMBqF7xy-OEzdsnR4bArXjfrKRaU47ctTWkW6A76MIrP_V90Ylaf7YFYrW9R_iifM-z39f-1LywrnFcZGiy2Eens57989aIz2PYL1iVnl3ktJk0to8Fo960n4fV8mgDJvRLUWD0W322tfUtBxpyhhzAi2bRYb5cunlmpETg11_wQpefb8VxOzX38TS7t4IpDAWmstPxEflP7Q2wC9bgIIOEEn-DSCGqvli6UmxVuY8-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=UwuR_ohVqN3ttOJISVqga28v3TBFI98kZyBxgF5-2C8fqFNyTWiRqIxkq9_WuLFCa4aVsc_6xlB7LfnnVpWRra_3JoWISU1wDc3Soy5u5SXx_PmvJ5aey7SHEnL6ZicnAqBtjL3I-i0fAY-xTgtyZmRWzk-mUjJeUR20EeGj6jSKFc1_7Myh1CiWpp-xvkTO8KwAnWL5g4Xdkj1FLBC1MY0OBJDfw78OldPCVNXn3n9_lNCSPA9z5UsSsYxa4KbbszysFzjFxTV2ZDIpM3zHk961C8uAGqJGBbSCOu3i3WgmTDVLugSr-yj9uLKHpPyjCGYvae73LyXuIpIFl_NK7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=UwuR_ohVqN3ttOJISVqga28v3TBFI98kZyBxgF5-2C8fqFNyTWiRqIxkq9_WuLFCa4aVsc_6xlB7LfnnVpWRra_3JoWISU1wDc3Soy5u5SXx_PmvJ5aey7SHEnL6ZicnAqBtjL3I-i0fAY-xTgtyZmRWzk-mUjJeUR20EeGj6jSKFc1_7Myh1CiWpp-xvkTO8KwAnWL5g4Xdkj1FLBC1MY0OBJDfw78OldPCVNXn3n9_lNCSPA9z5UsSsYxa4KbbszysFzjFxTV2ZDIpM3zHk961C8uAGqJGBbSCOu3i3WgmTDVLugSr-yj9uLKHpPyjCGYvae73LyXuIpIFl_NK7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVJ61gKjNjceemFOD2sIOaPUaG1OYbZdeONSUQ71Yn1GTkafc5iA39hWfDbJrv8XLdsntHaBCyz9W09JQMbOHkpfHbV2SuEHcvXX4FxCSlc7moxHtemwotJm3GHeMHw8J3r3jezGR9oFSuFV27-OyLyrj5BHfmRQ5JX_hZnR3DeUnsxfnWQ8sAtmnHp8Grrg_KoVqoedTxvIpKx_nHXfzY1Ko1zEF1iZZsI2NPNiNYuL2B8OjZOQ7wIosiaI_n1uxwvP5SNHdx4IFEDg1UzhnT7v-03WbzSfVK_IEmpRt7vwcEEFPyLSv6uQKl2zcyANMMXRx9oT1jDRq19lxgDbJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=TZiu3wgf0NafJaRE1KXgpsvi_ZPmuT7uoDvEpDIvRz6UuMFgB5S8QlpO6seGZalOhyDfHCFmChNTwbsg6ieMTj9b9SxISr8iFGs0Y8foV6j-5Wt7C1nnL3jwak-TPRwYuZISyLLZRmk0wcKTCwBnQpbnSZ5V7F0SplTToGUJiu9Vgo-8ZXmev0k__ykWAaIFyxLbdQWOuEbr0ofkN2nkLQVdhaDnY4GQo5EcoHGQiUcnB_DcDUrE5qIMVBEw6j0kbwsLLu1CzNZULEeKO8ejR8IkULR-KTq4whEniiDvIM0h-f3Et7L_Klo5jP8BzyyybrANH6NgsuKzidBxoLOm5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=TZiu3wgf0NafJaRE1KXgpsvi_ZPmuT7uoDvEpDIvRz6UuMFgB5S8QlpO6seGZalOhyDfHCFmChNTwbsg6ieMTj9b9SxISr8iFGs0Y8foV6j-5Wt7C1nnL3jwak-TPRwYuZISyLLZRmk0wcKTCwBnQpbnSZ5V7F0SplTToGUJiu9Vgo-8ZXmev0k__ykWAaIFyxLbdQWOuEbr0ofkN2nkLQVdhaDnY4GQo5EcoHGQiUcnB_DcDUrE5qIMVBEw6j0kbwsLLu1CzNZULEeKO8ejR8IkULR-KTq4whEniiDvIM0h-f3Et7L_Klo5jP8BzyyybrANH6NgsuKzidBxoLOm5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJnXDzbcn2cHlUR50mjGAt60XGZvi2_smUAsixATC8kbrb3d5_DAinINokURuoZc5KmxYnJIqW9nNztEhoVHGgaWEEvQbUkYT-j7iSyK80FVPNq5H_uqtr7vSOPVbQHooFquGUQJrGLOINaWebQPf1yh34sd9v0jQUq3c8IaifEHIPH5Ahg8DRcx8HtIMJTjSvljsSg5tqGHRyM97DSHNkY0fxhGa7vnfVwT9F83iNVPkmQT4Q7ISRPzY1ZkiU1sv6hlpKIPLjrKyef7qRxir1B6ysrxT4gMDSKD-Ro7N7hES2Dj7SqA6Vdu-HL2Cc7rORrFIEbEagN4Oe5OL7OWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP33mXGwDBA9muxP2V2EC-gXyUbOzT3ZP6fHaw3KYLqj5oplAHiKDv7lS577hki-brOJkDfaz4fwfSZj_RWVxu-SPkqFqfjEo_PDfk1_8_2mzWPbbImuYQ0Xq915Tn4fGZuaA0ofSMZy087gu6G2GKfDwzAk9BP2S9llvU9VsR2eUaF-WU_FlBdjEDJSyZAlAqBebEYSNbzz94sYFaiSuHeZqI_QDrmt9yjiHUezK8wOx34pXnrt30YilHCguDad5lHw6vleaXYV6S9MLcAisNhMZLXC53nl-yJb4fq7OoGjD-17DaxtO26bx4FrNxeqGhUCbO6ZryXjGF6D-UFxoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKy6aRDx8KvHtrlzNnGYYTREpNYwvLEGfYnt0bmsAAGV1kFrgGs0Jb7n4JqLaK66gypL2PNQfHTkWeF1j5qBK4B0nGs-ahlBLWGBPSpJi_s4hyDeLEZlVkrah5nXph22mee5ZUH4mbzM9R-LtOzlP3IyoZI5toLN74uYPlHQuWTj5QqZbYS8f667LY4FqtkfOpmEQnNuzQqLr8lK1SoY7ic-ukm2axscmVdUQ6pH-yzYMA6zd7ex9KH6JeR4pq8cLBzEe7hhgMHGMi_l5D_S5tEUvEwOf0rGgFeJY8SVVK-QivFJFvOjx5xh61BqMlPsrKsf8ONvCx8QboSNX-pKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=B6BRR2ByE1McV-T0XgfWy2hph8Z8vCH295yUdz2sKMxXEO8mlhOZAgF4AvNu9_pCtzaXnHyUCrLN8E6rksr8ydz56_eo1f8-nF6j-mhyAIoKA9t1Qr1PHgh-A9q1YH_USvxTyURFA2kGlTqyxgtg-Fqo8BJ05CG47T1yN8PBMZQV_3cXr0Xjm2VH2-XZjOqtVtlhMsNduq8vP06npbDLXnnf1osRc9de60Pm1H-isStsQoJ7SpHtkvajYdJV_mKBu0Mx6M6Olah8-s2jBwjal-Pir_9bGau3JitX_DAEt5V986VSLR8pBek48HB3MNkMEfrNHvrT-vhKjpj50PhkrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=B6BRR2ByE1McV-T0XgfWy2hph8Z8vCH295yUdz2sKMxXEO8mlhOZAgF4AvNu9_pCtzaXnHyUCrLN8E6rksr8ydz56_eo1f8-nF6j-mhyAIoKA9t1Qr1PHgh-A9q1YH_USvxTyURFA2kGlTqyxgtg-Fqo8BJ05CG47T1yN8PBMZQV_3cXr0Xjm2VH2-XZjOqtVtlhMsNduq8vP06npbDLXnnf1osRc9de60Pm1H-isStsQoJ7SpHtkvajYdJV_mKBu0Mx6M6Olah8-s2jBwjal-Pir_9bGau3JitX_DAEt5V986VSLR8pBek48HB3MNkMEfrNHvrT-vhKjpj50PhkrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuEKhZdyBdPrQZg38VaM0H54c6Xyrca-tUW6kpD9A5g5CB_SReqd1gyPi5R3Xz4zkk64Vas2IjybkqTbstosNold9VsU48N8Lc5w4ty0Er4czxFd-Z8LcpqdPqa3iG6rw5gZozaPkGiPvj8ZXRrEC3RfdKxn2Dm0Py6H17HlYkZMrUIu6_D0oL6xeLx9chVPJgdpQav-qy_mAFpfJnc3xshAcSgQxAd7umG3jQKTCguBHDQYdWPiX_KpXGKKH3mPs0Wen7a2_XBex7KTY7hlCxJ1emnS167JG4x7qPdj1DU4FTSA1PwWe3pATh5i5b0bNtZRlEssO8BiKx8ZBOmRhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=lV_6z0IXsrBWd1Fe34-YH9c86I5Ah8IQ88yfVUpahqYIEAGPfWvmYEMvikRX42V6csAeldYr0pR05nZiEBvOIemR0ggvKy0g_YoKLjR-DO8p_t1s1BuN4BhGi02FJ4jDYsxHxAe9ikEhS3Yp86wszZ2DxWL-IG0qC2FgKxaV_LkEW1OSrnrL6LuFZhr1THYzP5MC5z-iHPyW--7gonRHitwZTmz6IDG-965hv1saiCEdpfLJJUwg20k_RY-MlXZNMuKBp4V2ytKK6JZDlN3c1kwGIEAfefozZdIgT19zQR4zKqjONn2uE51_JJQ9iIin5vEvqBnGqkax-6P70vJHIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=lV_6z0IXsrBWd1Fe34-YH9c86I5Ah8IQ88yfVUpahqYIEAGPfWvmYEMvikRX42V6csAeldYr0pR05nZiEBvOIemR0ggvKy0g_YoKLjR-DO8p_t1s1BuN4BhGi02FJ4jDYsxHxAe9ikEhS3Yp86wszZ2DxWL-IG0qC2FgKxaV_LkEW1OSrnrL6LuFZhr1THYzP5MC5z-iHPyW--7gonRHitwZTmz6IDG-965hv1saiCEdpfLJJUwg20k_RY-MlXZNMuKBp4V2ytKK6JZDlN3c1kwGIEAfefozZdIgT19zQR4zKqjONn2uE51_JJQ9iIin5vEvqBnGqkax-6P70vJHIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=q2b69k0PICFT5YNzRAp0Z9YrXcvFtjIefU1FjyoX99dNhBr2S9pBjRoP6bYCnBVcBP3b1Bcpe71c_ELGAX2vBblboTPJzf6IPrqyrQtyCYjFNS1XHLqIZqkvxBtrOzrFhw4moZ0bv0MIZpnQ9WVKBES6EDAbKJ0p6uzUHM9SodEPmTMQOE5-uRu8FB8JXTuaPsYIxfNspguDzI8O7CxMfpYJ1XphVx4EaT4Th-0rh4FWMUzjqu_5Z4dyrSg9K7VxkoMmUUWaRh92Pkx7w-oBb-u2G-Ku69hleivgDbwzgjqRttyut1ULOC_f1rQJgq4wlzwKzG9cynB_eNws8iWOvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=q2b69k0PICFT5YNzRAp0Z9YrXcvFtjIefU1FjyoX99dNhBr2S9pBjRoP6bYCnBVcBP3b1Bcpe71c_ELGAX2vBblboTPJzf6IPrqyrQtyCYjFNS1XHLqIZqkvxBtrOzrFhw4moZ0bv0MIZpnQ9WVKBES6EDAbKJ0p6uzUHM9SodEPmTMQOE5-uRu8FB8JXTuaPsYIxfNspguDzI8O7CxMfpYJ1XphVx4EaT4Th-0rh4FWMUzjqu_5Z4dyrSg9K7VxkoMmUUWaRh92Pkx7w-oBb-u2G-Ku69hleivgDbwzgjqRttyut1ULOC_f1rQJgq4wlzwKzG9cynB_eNws8iWOvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRAq5WoHwQ4v3KlpCLJjEJkCF5ptXxVp-omsokY3NHq90c7IuBdUXoH4_p0p4HRpinToqHFcx9jkx_TpOrPahbCt91a96AUk61eKNkT0SIvXWrVSDTBEGI8Sx5TTrouQ5dZAM0OhUCXyNSu2gUl1Z0uOm0NdNOOzrILHR2tjZFyLKSptQQxUP_UOPCVulg96FzrlcrbE9Daty9zbyeYYip6YlPM9aXBb1MH7c8KIRY2KjMLIaZpeYqYSkvJhh_pIR3ppAgW-Ihu6GW0eKZb7mVK65Mto5Xr91iXFdyHQ5OgB_cIKwMbqV4rlfbD5Ya9MVpCz4gpckzOuIhMYDB7XaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=WhqRs3GbxK0ODrkAZdhrkr7YlAoQz-M5OqwZWH1xoKzhHF6q-OkI_Zn_WTW3JwTFRguqGilzs3iNzR54fSdHgvUDhvo07doV8LCxNvHMWsmIcEhu5SP2XgX9ABsa33A7Q03YHB5Kvo0PVg9Q6alz2jSi4EYAWcKGF74v9atzf3kScUTewnUNNu3SCEAPTkt9HRP10aZZk3-KvrR4EBztns116KP1x6c56zVBm-4TPy9lRmvoXGXnVH89sN94BbQmkMhaQYcAZIybdZ1n_hSSyacdq6EC8T-cIkDxnMpessBw4I3QEr1-N_NxJRTQZdUXTj8cBKTj86TH0O1ALEhXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=WhqRs3GbxK0ODrkAZdhrkr7YlAoQz-M5OqwZWH1xoKzhHF6q-OkI_Zn_WTW3JwTFRguqGilzs3iNzR54fSdHgvUDhvo07doV8LCxNvHMWsmIcEhu5SP2XgX9ABsa33A7Q03YHB5Kvo0PVg9Q6alz2jSi4EYAWcKGF74v9atzf3kScUTewnUNNu3SCEAPTkt9HRP10aZZk3-KvrR4EBztns116KP1x6c56zVBm-4TPy9lRmvoXGXnVH89sN94BbQmkMhaQYcAZIybdZ1n_hSSyacdq6EC8T-cIkDxnMpessBw4I3QEr1-N_NxJRTQZdUXTj8cBKTj86TH0O1ALEhXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=c9VXIL8M9M2HlJGDP-aoP6JQO901gs7y0SlmRjNxIN_WMg4E-4lK72Ac_POR9ugQ_UUfE9Wqq5fMmPOXc3G-8U55X7Qar4wJ7h38eAr_2U3IWiXgUeXT_xEcAAmNtXwVhOlW_DmfhtBfrwPp2Iww5eT4z0VRjMVd_-D2tJ6qX9yerNv8sFYOgn3aJZYfJaustGMvGDtUNtT_yKkpmVMc-aGVldo1A_hiwr9Toznmz10UWrPcZ-y9tmMJKytMinqXmWociAAzgmkwi_7SWZJTzGHqsfeCeG-GjXE6BxqTvJ2Ql2EjNwADI0OY6WLBS-L0KtFNXgM3YlKGNum1c-NTrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=c9VXIL8M9M2HlJGDP-aoP6JQO901gs7y0SlmRjNxIN_WMg4E-4lK72Ac_POR9ugQ_UUfE9Wqq5fMmPOXc3G-8U55X7Qar4wJ7h38eAr_2U3IWiXgUeXT_xEcAAmNtXwVhOlW_DmfhtBfrwPp2Iww5eT4z0VRjMVd_-D2tJ6qX9yerNv8sFYOgn3aJZYfJaustGMvGDtUNtT_yKkpmVMc-aGVldo1A_hiwr9Toznmz10UWrPcZ-y9tmMJKytMinqXmWociAAzgmkwi_7SWZJTzGHqsfeCeG-GjXE6BxqTvJ2Ql2EjNwADI0OY6WLBS-L0KtFNXgM3YlKGNum1c-NTrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=LSI-Hog42foZpYqywim6kTeEgisa9uJlRL0TMUBnol4uvAXFkxsYvYem0JoRBF4ERE-9aHFdBr90ZfLr-KhUzneqjA3Xy-0NSihD18cljQ6aSmIF5vXvWQQN6gAYRS_mPpvtaCnB34NHam1xnQgLjrsa4OtW6rgqTlxWdcpk_00IkvPwV8UjbFk42yddtIz5SyRSpjR3hNJYP7T1OkS7eypLD3xviahcOr5m5crVooYPE8NwuhG8IhApbpVbLYgIomev8iA29fTD8SQTER-3Ff_Jh4N-C8ERaeh3Jgx_cc0WexjEVMqqHkX3IC-OQ6TqbgyWA6Sse0ulSJPw6YbbWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=LSI-Hog42foZpYqywim6kTeEgisa9uJlRL0TMUBnol4uvAXFkxsYvYem0JoRBF4ERE-9aHFdBr90ZfLr-KhUzneqjA3Xy-0NSihD18cljQ6aSmIF5vXvWQQN6gAYRS_mPpvtaCnB34NHam1xnQgLjrsa4OtW6rgqTlxWdcpk_00IkvPwV8UjbFk42yddtIz5SyRSpjR3hNJYP7T1OkS7eypLD3xviahcOr5m5crVooYPE8NwuhG8IhApbpVbLYgIomev8iA29fTD8SQTER-3Ff_Jh4N-C8ERaeh3Jgx_cc0WexjEVMqqHkX3IC-OQ6TqbgyWA6Sse0ulSJPw6YbbWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=iJkhdKxwD5a-H2sh5sLpovSrGjzG3omeLBgN6V90Dk8dViEbGa_RZyte3CrGUHPcL7vW45_zDvPBDJUt3Blgn_yib8-tzW19AufIeGaoLqbFw6CNXOqCB-iHyGDebAV9sDqCFJlslS_lLNknqcBnOWj9uJtJL_qnapa93SgqK_EZ4dbqh8kd01czaRIVtXAo1RAwCQwW40pB9xkcmFDEy9nXQourZjcxg2WctIf7BbrULuw3yIjWHdA2IKAlJXLP8Zwqc8eCfo2CCiuh-Tdx3VoyzbmoXz9M5qIloVf32CKlLsM9mZ-d16ReqHWXU1uh5XuoWPhmJNkJqAulaqJA-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=iJkhdKxwD5a-H2sh5sLpovSrGjzG3omeLBgN6V90Dk8dViEbGa_RZyte3CrGUHPcL7vW45_zDvPBDJUt3Blgn_yib8-tzW19AufIeGaoLqbFw6CNXOqCB-iHyGDebAV9sDqCFJlslS_lLNknqcBnOWj9uJtJL_qnapa93SgqK_EZ4dbqh8kd01czaRIVtXAo1RAwCQwW40pB9xkcmFDEy9nXQourZjcxg2WctIf7BbrULuw3yIjWHdA2IKAlJXLP8Zwqc8eCfo2CCiuh-Tdx3VoyzbmoXz9M5qIloVf32CKlLsM9mZ-d16ReqHWXU1uh5XuoWPhmJNkJqAulaqJA-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=k0DdEbWeJFkyo4enzoaO9OdhpE0XXG1mukDCW4rPJ66iKXwP9TztPcdZ1xUYCwwFeTpIz17IRAvd47w0BVWnejSELHUoNdwLjHsDK2HshX-FkUj5fHxoF6Ck2pZw0NO6kM-mtNv4B5lOaNI0p0_3mUM4cQ2py2cdgxW_mNxJg8JCfiF8f6r0_9iCwtHow8jdYQCOd6--CkOrw4UiAhwwzKlETYNsdaap2oNQ77Q67vMYkQvWdRv2wxCcj4RPlYwKphektBR_hXeWwhobCcyct5CdKfVmUxnE7VPuWgCyi7qZ_-i32IDQIY-7wT8H5fW_f1uEGgta2l2ph_zqMf9uOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=k0DdEbWeJFkyo4enzoaO9OdhpE0XXG1mukDCW4rPJ66iKXwP9TztPcdZ1xUYCwwFeTpIz17IRAvd47w0BVWnejSELHUoNdwLjHsDK2HshX-FkUj5fHxoF6Ck2pZw0NO6kM-mtNv4B5lOaNI0p0_3mUM4cQ2py2cdgxW_mNxJg8JCfiF8f6r0_9iCwtHow8jdYQCOd6--CkOrw4UiAhwwzKlETYNsdaap2oNQ77Q67vMYkQvWdRv2wxCcj4RPlYwKphektBR_hXeWwhobCcyct5CdKfVmUxnE7VPuWgCyi7qZ_-i32IDQIY-7wT8H5fW_f1uEGgta2l2ph_zqMf9uOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5KL46pQXUnjbm5pScpV5tu3jTL6iX_4sIvrI4RebN8ckG5-yWytOPf0dP38duYaeJzzZj437wHiPUCM44F0duNNmgrDUJRwaFLw92dygstsCFZ6xsMyqVrsZzmtU11fxPfG8T0Q6IxkRvwcL-MtmbUtbW_oOyG5eLdoOxdLptjt2lEH-fbn9N6f2VE5GNybyrPsJj2TKFf7q1V-7hothxqeQFOBRMxr7D5z6-LDaPRpk8PL1Twr1NKh-xRMkCQG2kVXc0lYTbH18xdvxtbrPPBul97p2QkuKlU1tvwNfVmEMkadEmlbgSG-g5hOSQ4hh4sdwr0KC97fJfRJU_uXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=ZVqMmkMYKGedaguoKPNekKgA3zfS7j_tgLQ4D5cbHjIwYdB_B1OJ5yAryYysfWcruPfBuQT1-gJSIsHOCP60xvH6a557or_ge6F0LhoPeBDC8YkqaXBMSudkIQfZFKmMXs-QiMRzOMKHwhdDP2dVUO4fetY7Nl8c2FfMbG3I3WF7Rps9DoYeK7wH37ZgfPQimWnMWnsBGLIzSNhYarz0vWxQ99DATLg6bJG-utp5PBGnfqzIDnF8zCa7KTfzX4a4iRHI_MpRB5RClCT0kAQSoq5nZYVy0U4YIHbwxAbkP_7AuY6f-CS9hYqRx9hkq7P0maunokJi1yB1_ar5jmICTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=ZVqMmkMYKGedaguoKPNekKgA3zfS7j_tgLQ4D5cbHjIwYdB_B1OJ5yAryYysfWcruPfBuQT1-gJSIsHOCP60xvH6a557or_ge6F0LhoPeBDC8YkqaXBMSudkIQfZFKmMXs-QiMRzOMKHwhdDP2dVUO4fetY7Nl8c2FfMbG3I3WF7Rps9DoYeK7wH37ZgfPQimWnMWnsBGLIzSNhYarz0vWxQ99DATLg6bJG-utp5PBGnfqzIDnF8zCa7KTfzX4a4iRHI_MpRB5RClCT0kAQSoq5nZYVy0U4YIHbwxAbkP_7AuY6f-CS9hYqRx9hkq7P0maunokJi1yB1_ar5jmICTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKwG9l10VLvS-uLrcjyk-yjpjYU-DO4Opz-6MJjkQto4bzAEd6ziXZrBAbQ5hsf_AXTxRK9KbO6zVLcOzbLQlPoOU1vOG49ZcsC5sCQHbOn7TRQWBH7S0MVkC95xJY0J7I4LX73Rij0qovnid61dIl4xymrHan7q5U_KfbnibXsyJR6ER2KCT17-6TVJYeaKuAQZgjpPGgW3rusaxkj_GYLxvA_UZJpbEQMt-0KoKgRWyYj6TuSQ2tsaRfEYicaVp-dxSorQx8BNCF0dMKWpglEstEr41eZWfyPpDULRgPGy2X-FEYKmPepSKplX6DZsVJ_dih-RFQtc4lLe680MHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=FIP1bHV-wBjmwNquxObI1hg0llpOyadmRigsO0t4tKa4xcHOdInvv2g_HOULVFLX4356HfHalwKEcWOKgny6FAhS5LuIV9bqMk_nq9jTLte3rejEHw-Z6zXKl9VioJgRWgtXXW75syXMBjfnV2PoxKoIfDeBo5tqqrNO7WDMeoHbB1PcP67g7Eu6UuZ8RhrmBadA-te4w8zasTzvGrkS8lfHyW8kDbfhzfWm-QOm8tQJSanoOf7DbYcvv6hvKyVC5L-0z1EyxJBLVd-XPGvk6ClFNKqcKdBnLoOCgHNPTRSxQt3QsH1gv5AOGtGOPVPCNYGmzvq7UY_sU3ROS0evRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=FIP1bHV-wBjmwNquxObI1hg0llpOyadmRigsO0t4tKa4xcHOdInvv2g_HOULVFLX4356HfHalwKEcWOKgny6FAhS5LuIV9bqMk_nq9jTLte3rejEHw-Z6zXKl9VioJgRWgtXXW75syXMBjfnV2PoxKoIfDeBo5tqqrNO7WDMeoHbB1PcP67g7Eu6UuZ8RhrmBadA-te4w8zasTzvGrkS8lfHyW8kDbfhzfWm-QOm8tQJSanoOf7DbYcvv6hvKyVC5L-0z1EyxJBLVd-XPGvk6ClFNKqcKdBnLoOCgHNPTRSxQt3QsH1gv5AOGtGOPVPCNYGmzvq7UY_sU3ROS0evRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dGGjx1VthvnV6fNKTTvhnBQzt8HOfvxEWbdt2FBJZbDMqv_2wnk52NM3serUYYIwTTYk-uJHycGtJjN5YsSQCqS3BHree_SJ61t3LxCYnSolYq4WUnTLaUgz4K32jyg7y62c-bd3FqfdfP8oEc1WJnq-i1-PNOD-dPE9PJ6oRf3sWWM8LsFlot-je58azR2HuHwjjOK-9HZjE3TB2x19rIkSzteNIgeB-ZeqQFR-ObpNnpWVrTeifeaHagcBZq9roMmOSsn2ypcIHd5RNYFzXvHpzyEWJrpoYuEHkj80WPxl7L3hcZhM9-aUh4p01I5HJMvqF37mf-sruoP7Ex9F9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dGGjx1VthvnV6fNKTTvhnBQzt8HOfvxEWbdt2FBJZbDMqv_2wnk52NM3serUYYIwTTYk-uJHycGtJjN5YsSQCqS3BHree_SJ61t3LxCYnSolYq4WUnTLaUgz4K32jyg7y62c-bd3FqfdfP8oEc1WJnq-i1-PNOD-dPE9PJ6oRf3sWWM8LsFlot-je58azR2HuHwjjOK-9HZjE3TB2x19rIkSzteNIgeB-ZeqQFR-ObpNnpWVrTeifeaHagcBZq9roMmOSsn2ypcIHd5RNYFzXvHpzyEWJrpoYuEHkj80WPxl7L3hcZhM9-aUh4p01I5HJMvqF37mf-sruoP7Ex9F9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=BdGQgSLLbZSnIcsuk_yEYokcubxiszQxEYEgFf_YWAbVly23vARjiDnBjmrGhpdIuKM3W0N4K60k4ZMLmyWNqXFX6dXUuhPeiKqU8z66MdumqxTKrRT1KLHGbRmVUviaiUSSJnzbb7jnK3mEsUu8Edyplb8shBtgadmb5mV_GtyEtgO8xB_NROe92sJFx-RzknU95eYirBy305ZaWv7AmPbr7SoiwPEhXW68XJSJN9RCcRSd2Rz_DbEX-FoxSdw7WvokUiF_DtX8EdMy8ik1c719_yHXho-DzhItMR3DN95R4ymc-0f_oK3NQl2u5Zn8MvCpw27RM8HnotNw3Dhm_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=BdGQgSLLbZSnIcsuk_yEYokcubxiszQxEYEgFf_YWAbVly23vARjiDnBjmrGhpdIuKM3W0N4K60k4ZMLmyWNqXFX6dXUuhPeiKqU8z66MdumqxTKrRT1KLHGbRmVUviaiUSSJnzbb7jnK3mEsUu8Edyplb8shBtgadmb5mV_GtyEtgO8xB_NROe92sJFx-RzknU95eYirBy305ZaWv7AmPbr7SoiwPEhXW68XJSJN9RCcRSd2Rz_DbEX-FoxSdw7WvokUiF_DtX8EdMy8ik1c719_yHXho-DzhItMR3DN95R4ymc-0f_oK3NQl2u5Zn8MvCpw27RM8HnotNw3Dhm_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=fwrAW_v8vj7e5ExXLYSMPYbLYAbV7h7f8iwM965s0g5SSBOo9bl76qgvRxNSlOgpxGZGSIchde5q0miQCPITa4VXPUcD8o2dTOE3jPABrd42WT1NgreCSBmaZfEfJ9jZTFqxlfKTEkHI1yu0R3SUEyWAoKJJbKKk0B9Eemrrvhx8n-jLssvu5IcfUpN4KLeZZ48DUX5zefvBjGzhCHbGaSB9ekxAL7KYxFowHRJqGn6SQUVbAhr2NdafjnaCusGyoN1Y9jSS3gt4FXWS5jld6vrXbb4g3uznxSOKR0l2hdHtGbtoS1NHCObS1N3Xwwdf6ofmZgE2WAPR6JXfGpzyoJhYw3tAY2lxmZ0CrlmKbft6f5s6gpDxPUbFv9y9ozwxBf8F02lw1ou25prJQWRyt0VWnApiLAq4PGXNcBiiivsGX2OeDRRSlFeJosSSZlFMtV6MxmZdNfkf0B2U5p47KjX9h2XpoohcsNiuz7p1TwJMOBiZymxnX_woJnluz0j-ZcqIwKjV2rrZa4xOU4ZNreU1M6vSWE2OQIJF2Ubc-bHArnsQIoIAjp3-b_cNqMWQ4jEKCXR4t2vxdqagqef5KLAZ-YDfNuStjma2E8DrX2FIBN6hUgXBBQuVpu7JGRrOVhp3ZcPUlCp0OlYAq5otagjVeVgsGjWynOtiLXr160c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=fwrAW_v8vj7e5ExXLYSMPYbLYAbV7h7f8iwM965s0g5SSBOo9bl76qgvRxNSlOgpxGZGSIchde5q0miQCPITa4VXPUcD8o2dTOE3jPABrd42WT1NgreCSBmaZfEfJ9jZTFqxlfKTEkHI1yu0R3SUEyWAoKJJbKKk0B9Eemrrvhx8n-jLssvu5IcfUpN4KLeZZ48DUX5zefvBjGzhCHbGaSB9ekxAL7KYxFowHRJqGn6SQUVbAhr2NdafjnaCusGyoN1Y9jSS3gt4FXWS5jld6vrXbb4g3uznxSOKR0l2hdHtGbtoS1NHCObS1N3Xwwdf6ofmZgE2WAPR6JXfGpzyoJhYw3tAY2lxmZ0CrlmKbft6f5s6gpDxPUbFv9y9ozwxBf8F02lw1ou25prJQWRyt0VWnApiLAq4PGXNcBiiivsGX2OeDRRSlFeJosSSZlFMtV6MxmZdNfkf0B2U5p47KjX9h2XpoohcsNiuz7p1TwJMOBiZymxnX_woJnluz0j-ZcqIwKjV2rrZa4xOU4ZNreU1M6vSWE2OQIJF2Ubc-bHArnsQIoIAjp3-b_cNqMWQ4jEKCXR4t2vxdqagqef5KLAZ-YDfNuStjma2E8DrX2FIBN6hUgXBBQuVpu7JGRrOVhp3ZcPUlCp0OlYAq5otagjVeVgsGjWynOtiLXr160c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdywkBdBdOXRRnKNQqhnoMwzP94OXY68cVCJCQvqXTZXgL6MUUtZyYkuw4nT5gtmJb3_nCiWIYXiD0LxIEOlVq7v3uFWuO6mzJ6zvN-aAqgVLQf3tdmZ5Q6Uh4Id07RcNWVdqpmoEYuCyOguwD32luievh44mZE0dY7eCM4ZXH1oBUSe1IM2lZZa-nbu4H6_hV7Zl_nGY-ZU8kvrLg4RMrAEYIX28mXtHio43nefuyQnk33XbIPRzxgMFRRZS-xVYzcPSOBcubwahw-1r7aDXQclqN74toIIqFYCF-fyXpd--SB-IrsaD3ESPpQaYBOCqY-YNBr6GPgHEzL952XWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=a6YuEwFWqdaRjRQFVJqtz4NvxeBU-ERC3ICQ19zsMY_VhMR63hNUM5jLLT9T30JTxnYMGILsuf0S2Q3kswwANRZIutnrkBAE4Elll_If5ijt2GKAmyrgaKKVFb8P0lTUlrWIrhb5iaeytHEyM-S-1FXknBX7MvG2wFKuOuPUkTGKBys6JMolBslI08hmpUs1ttJTcrSeBstRPpNqgWJBIGMJR-XwqDOWSQEvut3m3qvyHJ7iO_IgIkSyDc7qQ6CG_9SJIxFO1V7n3QS6SP21FTmijh8wvm7sX5XxLuFhnSyoqPhxNdOKDx44V6FI-XJNdpAQGr9HdDeYyVHZWE8J4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=a6YuEwFWqdaRjRQFVJqtz4NvxeBU-ERC3ICQ19zsMY_VhMR63hNUM5jLLT9T30JTxnYMGILsuf0S2Q3kswwANRZIutnrkBAE4Elll_If5ijt2GKAmyrgaKKVFb8P0lTUlrWIrhb5iaeytHEyM-S-1FXknBX7MvG2wFKuOuPUkTGKBys6JMolBslI08hmpUs1ttJTcrSeBstRPpNqgWJBIGMJR-XwqDOWSQEvut3m3qvyHJ7iO_IgIkSyDc7qQ6CG_9SJIxFO1V7n3QS6SP21FTmijh8wvm7sX5XxLuFhnSyoqPhxNdOKDx44V6FI-XJNdpAQGr9HdDeYyVHZWE8J4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4h7dix8y8-ooBaUq-vydzRwGha6WqGQqm62Yd4_AnmNrCDz9m813MYuBgjp6k8KprAcfmsgbMCH9k2hUQu6XDZ-AuSTodX3aTC2gGiwL7XQvLPR0Kp7BCaDkOL2kkajRyW4fZXW9f1AM6pT47sSF8NMmOsKplK51gbDBfeTOzsF-ykSrT2QBcQ2Spq5QfsdjrRAboKFe04DEGmrAGcA_CNaSgmBlZt1ox8_34Pa6qJkkTqr2gfZQC3nMWTOAYsOZA0kXQxAf5QyOR-5hfma3CMK2IhkbiMmQLruUafrB4F-hCsDL2igfJYCicGXYYWdztuoKdEbi-j_Cs1EIvFCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0wuoppqPtWrAU5JDMFbjcz_is47p6q77G_lF92fT9Oohs6630Ukh43diCQrKAVZM-ARlxH0Ksfxp9D5LDtwaqbjFQrdXHe4GlhJfVXNN_fuSukBFomBHT-_0t-jlpRadTP990IW4wW_bUjVqPqfrGEOHYOvrfaCA4aLKFFFxsghldWxPELwos-MR5tgQyIGyxz9mlLjs36Ivedec9FfAUQa62a2wtlIEz6uD5a-PoY3tPI2GXZBU7uMXVXGB19-6s_uX-GaOQ9lFjYPcvP53q2nOlzu6f268hKpRZVP-n1v_TKHjumevMIFD5m5G2EsC_s3PSfs8bOeClLHprh27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE6uRQekg6eGCQAhLIZy7FG45ObUdIN0iU9Wlg13etGL5VpMwaZI0pLvo2_3lF9HPLZJsDnyfUyPLZnq08DjqdCVdLGKRUgpJpY8j_KFaMBmy8tBfydqJbVuQTHwmEq2D9pKNb_cTDIQi0CLuyyGucCXOPYoToq0JZ25cooUnLs6jxRqCXI1nvnlT95ErDAe4cpIun4f09LofxkR4cCJTQOY3VZOV9Kwfx2LWTMtOvCj7RJSusKEdBiaZLRq7hFtHiwLdfXveKjSu9E04xJYdeSopdTgOuk6lCFsaiFKi8OY7_njUlfESIMZHIrwfSVj023hk45vrD3e9ux3uM-YNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3Lh3UortG0psWY2R6Z8-6ElvR6FI8KHIdYy6odJXB7q39vXJRxolzCNEGARuHWrCZit23KNYDLghNOelLFwzv2qJHMVkDlEFLdHrMvSe4ouVd4bfM8DojtlnqZ8vpZ55ILLCKZ-truIqGveXrytzy2RjWU0JjBR8N0uKHMNO4qAk8_Xa6Roi0hwxDkCwOqfNZYP6F6oD8xIxvhYhd0G4WOdxPeiakp82Q7-c9foFu9oAil5mVQr9N8vi9OsfhbLaVmaQ9AVJ9V-LueYcKWkN15Tx_3ki9GybCo-KqKa5yOHDhnzv0y4Pb1SWbeovaekuBj0sNdW9lksv6C720ju3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyklQe2OUH95sHWm7iZREn6dBtQPgvcZtkDUo46w5N-KxU2YXK4apPHRENlTiOtw5D5hFHFIQdqV3THkPm71qhQzsYO_lpXcq0rX6-LFy_INgwoFa80hE9HiJkfsEntwzwtiQXRM8FRmz4rZDke7jz4DSMg-BoUtkzbQBaMkJsWH9Pq9dMJkPTlwiLabMS3EpCievToZB9vmgWbq-ECxCj9sogpwzApGTuILgUPIxu41dsfkRl-OBMIZo9cpjnRWTMThf42tfieXWMxrN8WW35htaHuaeLfMbRMkK8yiuGnxtm9Q6fDrfQ9MDvlAghhbhDVlIomRfySl1y8sqXOgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8VQitHO-7gZQR0ZSDcH7FLJVm8tMz73vK2eYQxceyNdl3FAY9EIQfmyNtHSHn7QsP4Wu27crDH8zu0_L-NW1mPfNifwvpMmFOryUPKfWI3vMr3YwUU07yFcJsWdpQO-dneGDW-lMzpefmQRZWBv0Sj1APwVgjaM8Fjdhem4dlBd2FR4yHzq8FBqAqpeTRIeZnIY1Ng_JlmAfwOKhCpDYAd5HojIxaS9Dc1El9f5xhm5UTTPv2IgPvMNbpYLP0OG3O-gSPqwbC820GOZI04eum0z8mi2_QJB6mF28GHhAlVpF-wJ-8aCzBpM7BESn6wWG7PBHu4ZUNEG9jThatKmgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=LM4l9IR2H5B55_8wbfEM3AWNtdK4DMPZezHutTuvF1RC2J4cDsLGduHaSzgfOrED7jPAJ3cpiKhGFhbMyTaKe9YtyES0Ix10xdl8AlFqm9t8a0qG5KUMDTT7XKgwo3lraGX8rd3_6U9iVuoqZaPES61c5QBvswkGQzvltLypSxBSuXhp5doWq2iTCx7ypd-RrxyTy-Yae_OvY6LN2IH71kls4fZfwR6H_-gFCo7WOik0GF80Wt-Leyd03Ps4PWGR3PniMw4rlOTcnEsFUmEgUoaGxuOsWBTSGUc8_mM1ymdzb1mxmtf6EyZWXkVwDA1Me8zfuNOF-hm9SW2s7jBLMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=LM4l9IR2H5B55_8wbfEM3AWNtdK4DMPZezHutTuvF1RC2J4cDsLGduHaSzgfOrED7jPAJ3cpiKhGFhbMyTaKe9YtyES0Ix10xdl8AlFqm9t8a0qG5KUMDTT7XKgwo3lraGX8rd3_6U9iVuoqZaPES61c5QBvswkGQzvltLypSxBSuXhp5doWq2iTCx7ypd-RrxyTy-Yae_OvY6LN2IH71kls4fZfwR6H_-gFCo7WOik0GF80Wt-Leyd03Ps4PWGR3PniMw4rlOTcnEsFUmEgUoaGxuOsWBTSGUc8_mM1ymdzb1mxmtf6EyZWXkVwDA1Me8zfuNOF-hm9SW2s7jBLMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=gxQUx4emlonsmzSsarOEQYY9OVYugssU_F-uOgLTVOHydMaG3NAuM9vOzdrpa_W5klV0D77PCzdJC8-lyopT2VM7pIjc7Sirz3fDrNVM_jdVjuQBxC8RzsnFprvx3MzcEmpWoiAa4bDkX4i5iaWGxi9gXiWXbwWKX8lsUYmRbJWDX5vhWcLa7c8AY9h9kG5Py4JDoVrhVtCprbugtL6TemiqgcPD13_v75vhGpDxbgN3gbqb0RKC2TRAAm-iMZcfuU6dJJxcZ-jzFgaX2ej0xEyr6A3y0-8eLUw_YRyb1fpD3LoS8xj_gzqXg1-eIY3Lu1S5Doz96kA7pZ17XOFq2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=gxQUx4emlonsmzSsarOEQYY9OVYugssU_F-uOgLTVOHydMaG3NAuM9vOzdrpa_W5klV0D77PCzdJC8-lyopT2VM7pIjc7Sirz3fDrNVM_jdVjuQBxC8RzsnFprvx3MzcEmpWoiAa4bDkX4i5iaWGxi9gXiWXbwWKX8lsUYmRbJWDX5vhWcLa7c8AY9h9kG5Py4JDoVrhVtCprbugtL6TemiqgcPD13_v75vhGpDxbgN3gbqb0RKC2TRAAm-iMZcfuU6dJJxcZ-jzFgaX2ej0xEyr6A3y0-8eLUw_YRyb1fpD3LoS8xj_gzqXg1-eIY3Lu1S5Doz96kA7pZ17XOFq2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=Zmdvffqcxd17ve95VSOijQWulTpZ4A2KGtW8YL6paa1wbXMWRdX6MC86xDFuW1BDMBZ16kWLyZaxaTw5kM-GTejTYvq3UVJSag2ym-3LqwfNeEoFF73efHwrbseYWWiP9KGUsxNq8_6_WvDfhChNeaMuEd8-Ef5c0ZSHd2mZjBQK8PWo8D8vYu6iK-QQlTGOOE0soGQxpHDVnNJtfdrI7Zf-JPLpIYHYEzHFolNDVLK676B5VfGDvoAAF3A81iByQh7gAneyoer7czZxYZ_4MRKDmm8QNUy0qLG-fc_2hgTZXOqCEijKksw3Jc4BiiokdqN3uPAUieinwAFistI1qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=Zmdvffqcxd17ve95VSOijQWulTpZ4A2KGtW8YL6paa1wbXMWRdX6MC86xDFuW1BDMBZ16kWLyZaxaTw5kM-GTejTYvq3UVJSag2ym-3LqwfNeEoFF73efHwrbseYWWiP9KGUsxNq8_6_WvDfhChNeaMuEd8-Ef5c0ZSHd2mZjBQK8PWo8D8vYu6iK-QQlTGOOE0soGQxpHDVnNJtfdrI7Zf-JPLpIYHYEzHFolNDVLK676B5VfGDvoAAF3A81iByQh7gAneyoer7czZxYZ_4MRKDmm8QNUy0qLG-fc_2hgTZXOqCEijKksw3Jc4BiiokdqN3uPAUieinwAFistI1qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=bWT8TWN4d5GVtU3Z4EeYvQc9QAmuCelhQvRoJBoCK9hdSv_mxWULaXJ4CaSMu9YZ9nX6Z4CPdYY-O6SFKUFJJoNehWyah-4YTI4F-KCcwjTedlxyxBYnFY3c14dvqHi8lp7cbYUGeYd8nmwrGzFQq3xCZYSc404dwo54fCUJpqFBu6xDF7UpZWSOCX1Oi1weTkj3ui0mwZsXv_uxMeyg15_zzYSKmGGeD0IRcnDocPVBOq9WTyPzmomPb679N_7oA4VuvCc_WkeuplXea-PCiSVwpj3hyw9RHDviNGkA8ENVaejegR2bBfF8HWpBa3Ke7iB7hbYPZ8ZHLYV7TKBHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=bWT8TWN4d5GVtU3Z4EeYvQc9QAmuCelhQvRoJBoCK9hdSv_mxWULaXJ4CaSMu9YZ9nX6Z4CPdYY-O6SFKUFJJoNehWyah-4YTI4F-KCcwjTedlxyxBYnFY3c14dvqHi8lp7cbYUGeYd8nmwrGzFQq3xCZYSc404dwo54fCUJpqFBu6xDF7UpZWSOCX1Oi1weTkj3ui0mwZsXv_uxMeyg15_zzYSKmGGeD0IRcnDocPVBOq9WTyPzmomPb679N_7oA4VuvCc_WkeuplXea-PCiSVwpj3hyw9RHDviNGkA8ENVaejegR2bBfF8HWpBa3Ke7iB7hbYPZ8ZHLYV7TKBHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=H6oTutejc3cV0wyUe86amqz_oeOvHzFVpaeO_fEse0G4hNIWu8vB_LjzF_04CyW2n04b7nCMhGgQU7ZlITx0zA3cw-H_13ZHXHhsMEHIKh9asOb1W1ZEg0ohW-e2K_ygq87H0yiGNm0UuV9I1dlZoT6xFk3mK2pxJWIBbE77chzILTPHccJvL3Gd2IC3wVoF0X5IQSETMJTfIeoKkHPKNICw3OaFdib2V0eZTazn749Q4hyfvla9EutTYotPuzv67MB_CulBqafih5TfiorD6AYUNtU_0xGCOFiGmYcPvAX0YxXg7NWIHatY8VzD43HA4Dm_LLrCE6JrFViNbLpUug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=H6oTutejc3cV0wyUe86amqz_oeOvHzFVpaeO_fEse0G4hNIWu8vB_LjzF_04CyW2n04b7nCMhGgQU7ZlITx0zA3cw-H_13ZHXHhsMEHIKh9asOb1W1ZEg0ohW-e2K_ygq87H0yiGNm0UuV9I1dlZoT6xFk3mK2pxJWIBbE77chzILTPHccJvL3Gd2IC3wVoF0X5IQSETMJTfIeoKkHPKNICw3OaFdib2V0eZTazn749Q4hyfvla9EutTYotPuzv67MB_CulBqafih5TfiorD6AYUNtU_0xGCOFiGmYcPvAX0YxXg7NWIHatY8VzD43HA4Dm_LLrCE6JrFViNbLpUug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=s6D9gB2IcqKhrHlfXvyu2FuafGvzsvA8Xt4BmXLLJbkcMo58n7Vju5AgV0LPKh3MralgLTsl2__VQgOAZsVRlvDWDWzNt4_N1KczWRksAODT5wOO9dfWrMWtdHei1-gwssfSK6hnS4Cgrd0gx60q5eTP-YEX7o4CP3E6OYmzbOokwkMOYxgAoC0S1yH3j8EPJB_nvBRq-gPZLYwwLQ-lIC97wJQWEJ7t39oSLGLdwoWMWFVEADlwyta0cZKtmq3962I4TRJcapjXPD0GkFJcu7VWeV_2uMv5az0gXOY4380TvTpZ0AbUBmPWVQsyty89n0BJe40nwaJAdN6B0CWgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=s6D9gB2IcqKhrHlfXvyu2FuafGvzsvA8Xt4BmXLLJbkcMo58n7Vju5AgV0LPKh3MralgLTsl2__VQgOAZsVRlvDWDWzNt4_N1KczWRksAODT5wOO9dfWrMWtdHei1-gwssfSK6hnS4Cgrd0gx60q5eTP-YEX7o4CP3E6OYmzbOokwkMOYxgAoC0S1yH3j8EPJB_nvBRq-gPZLYwwLQ-lIC97wJQWEJ7t39oSLGLdwoWMWFVEADlwyta0cZKtmq3962I4TRJcapjXPD0GkFJcu7VWeV_2uMv5az0gXOY4380TvTpZ0AbUBmPWVQsyty89n0BJe40nwaJAdN6B0CWgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpbYgtrpQ9WfgTkaXt8Hi3lJ6BQfO30zTXUYiXxHBW_x5c5bLeF_uOlx7FZ22Ol1tPHcfqToi2HtbWFNLGOWykDYvx5PH5pjBv4ztM72VW1n3Yhv6JUNTp3OxLBfXYlLnU9cYPe06AoEYR1hQWvCXR2WX8S5qxmtm2TcaKigq9aj4WCM91Xja9nb_TSyGoPDORQ8ZpRlfUAKyiWH1fOp9eFEeWuqc26xy4-btohtDV0pWRnyaxlTDu3C9p20-C_MyfZ7wJ1BPRyIzjk7wl41DD_s4LyBdJD2-fbwJ0M0kqFP7b_WyifIw5XhQ_iRTO2TbO7Bnw9CH_y-mgRIh8h3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8_X1SkhNsjJJLE_C7JBE00YyLum8pPZCi-1JZqnElvV1MScAStFub92nJZATuf1dTKbrx5VRIWvRG5lncQgPZVL0__ZEeyldIJXMCIknbeXQzBTSNGqSVQ2CyttHco0Cb6j7YHSR4h6BU6ehHrgFYILG7OWvag8yqW-UcT3MdzNFjrl_EOivmRhwleiitcvuoY7cuamRRq7SgZIgu22EtzPVQm8poZenrPJrpTzfl4a-SYXnRRdXIapC4nEO58e3NRARFXGJpAjdPEq5HsJEYBaR-q4Q7QOdMehUyHI3H7qPO_OcUW9qoDFRxmAVJAHbWrGh079lEuK-nj6--DKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht8M5IpmmDFwqqusiRwNU3mNcPjgCwTsRDs8axWpLReZdv_4DoM-PNtyl7qUHYlbvtmI66c4yTqDV7ILsgCeDncjARFmNXt0i2iXIGjYn865xsT-5pb7nGbEAW9F-nv9mfrVCSCX8j3t_TXD9wvkzKGnj6jbK8WLANINjjsfZMkTEtolJ_wIrUbueH1lL1IhSc32O2iYc8xCiZvi35WA_ktJmrcDRTwpkP0aFl51YVwhS0LKm7dTyHrLX8zkanLriC_pLfgALUTWR8ATegDILrnKlv6J-QWF7caAroFLpyQzq9oxAPwg5zxjfU-69Kn8AlE5CNb3b1f9ukVjRMksRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=W_N3H39e3919aXE_aSHVJbR6mQpcy9DMxhSPsonQcmo9SSqhhnehh_AIwT4N1DtZRMVQ1Ohc9z-F-1ILOWBeEkFpyvZ8IqWJWxOON_UV24RF6KmmoIWTonx21gY_HqojLCGjR29fgGUH0GxX145qLQN_Jt17-53wK5PXjvmMUQHosbd6-aca2_MUPfTn7bqqrB3HU0zzjsT__7PDPB7_p9eNVfQ81YEBHKJBP22D3cXhOKNzXWReAyL8A9Qs-GSaISzNL1POpSNltZu5xJ_iaqJF_X1FTilJmdJVZ2vU_PnD-a1aM0Ketn0Kfi5HTC3ThwDFYSHYoT6zPzSs8RC-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=W_N3H39e3919aXE_aSHVJbR6mQpcy9DMxhSPsonQcmo9SSqhhnehh_AIwT4N1DtZRMVQ1Ohc9z-F-1ILOWBeEkFpyvZ8IqWJWxOON_UV24RF6KmmoIWTonx21gY_HqojLCGjR29fgGUH0GxX145qLQN_Jt17-53wK5PXjvmMUQHosbd6-aca2_MUPfTn7bqqrB3HU0zzjsT__7PDPB7_p9eNVfQ81YEBHKJBP22D3cXhOKNzXWReAyL8A9Qs-GSaISzNL1POpSNltZu5xJ_iaqJF_X1FTilJmdJVZ2vU_PnD-a1aM0Ketn0Kfi5HTC3ThwDFYSHYoT6zPzSs8RC-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca9MdKfrAl34xCkWDstZTVZvxUUDFc2XQMQeFLK95m8tQcIerdsJ6BpswQ4ZBxDw_8cav-Wn8CZha0KcU9h_RuyNwLKgyMbXiHcjwzPqp3PR-h9w4KdiVJKA7eZOAVv6H04lSrVAvN7sCGPeqix2Yw7ESW66CxgBbxAH_6ocfFg4wlxYcxi8HZENSP2f6OnKD7SnrbC-zfbEw7nx2KTImpt3gupuYJRsnrPylR9s2lXbx326WNl6odPv3i9Brq5t4-_ZxiIMikBad2zaygaOH1wrRwMRMAVVcaPivSnW_F9WKKHBk5IbJ-O3URZKogscxRg9AwN_KSa-QthHrfX_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi-_59nSMgyCjA4P1Bs8z84K_7dGOjP1UX7M5QAwFtVV0deMnGtqVVSr9HVuthxnEIT7EQcrCdMW8JnFdkV0PENeXZdNGLmeVtIXUrITZ8LV_mJqgyom6wQrq79Fo4ruK7ZzLt7DcCNvuTr-tTmPNZRKRAjQiz7eFqY3NwVwAIgFKi0UNDi_EdWeJjlHgQqGWFwP3Bn03fmn-4RYVbdCdccMHrv2RzVBOKPtIZgzz2YyU6n24dsztf5FubnwdGKCM_2LZNtn1IG-a0jJ6Tzx9r268CnKLz0WdNkXMN-PsaFXLZYHgiKfU0x-uuNpansh_0wK8ygPWa5nfs4FiVwtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=TSpoCXb4xempz6pUENBXJaun6_vH-mioU3Ymv6WKFLBxjRsD88KbOQr9MriY3kYpsi84JUYF-nGUnrdvaXa5ATaa8moBUb03cIhuaYMkgEHeLxQvP-QUTCO2StTA-pLODxHC06Xcg9UPEN_-1Y9uDPvXkwhIMz58D5V5ssnn077rlI3SXEa7x73MNUI4DX_qGffXHww_Dj6FdfvyzEoaNGNJo8kMeTm5_mPtdh606KKkpbsJjoit1ZyLCwcsXNW0bc1CZm8BvonfGr9IaDK1o01pasYJ2CdZgGJHRfJ47Yz9Ux0DebUAux4TiecYoIu2IbSowyqb03HUFcDU_KMy2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=TSpoCXb4xempz6pUENBXJaun6_vH-mioU3Ymv6WKFLBxjRsD88KbOQr9MriY3kYpsi84JUYF-nGUnrdvaXa5ATaa8moBUb03cIhuaYMkgEHeLxQvP-QUTCO2StTA-pLODxHC06Xcg9UPEN_-1Y9uDPvXkwhIMz58D5V5ssnn077rlI3SXEa7x73MNUI4DX_qGffXHww_Dj6FdfvyzEoaNGNJo8kMeTm5_mPtdh606KKkpbsJjoit1ZyLCwcsXNW0bc1CZm8BvonfGr9IaDK1o01pasYJ2CdZgGJHRfJ47Yz9Ux0DebUAux4TiecYoIu2IbSowyqb03HUFcDU_KMy2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiS55IzMn9_VPOEsfKws573ZFY6Zo6uiZJ3X-VFMyR3Twqyb8oAXLKFzGNOoHM1PL1qLpap7y1JCym7pBklJZ-yTkGMb4dEdJUYs3w57xKTcJ__ev9Z0xALl89Azstmh3DnrMYQDjcA4OOvJEq12fmpy5ZcgoPs1eCrX5uSakKs-wHZr6CtaIheYlgfnfKvnZRsj4Zo794a3wbSMg16ZhKYoJHkFMHdGC9S_blm0PrfqUzL2hyEbrFhWI986fwcY0glwBmOGkcf9EZBCBKGGXFqtK_CmdWlSgZYhVviPqSeLspgDozW9a0HjTXHAE0ekh5bJovCvqx4JD49M7T7j4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
