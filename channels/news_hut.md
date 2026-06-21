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
<img src="https://cdn4.telesco.pe/file/QUWrsBeVcezt6XZnOhlTFVmucaUn_uuqX9SOtZjfU0d2nV4T63JPkL6rIBdEZhcPoo1sgEOEcumFFtCxW_8FnHJ592LHjvefFUog-1ealBabOiyovNxaNCrlUZmek6_LWiAE5LKLfWEUq-tPSwpZiANcXbC2gTX7l6WerGDtrjwYWn0nRU2E02wp5deYHfLqJQorwORxiQDic5Sm1syQLuz_LX_RY1yI_-CqLTG4SXGaWYYIUME0xQxaBCUqp3maLeddz63AurkRTfcYXa4lLkJb-kYs1UjHWbk139AGEoeMGGRyNkqxOvE4SX5RKWrL_6KmWVyiBk9-oBijSxN1WA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 221K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK5cyeWGiIEyH-LgNgm97vXisi8rVISI18k4Q-S5etX2DUVTkZhxyi1TCQXM6NiwgXV7LlyYPuzJSHdPDv6_1CxyHZCcKztY8mqeiCcc9Nmwmro37j03Qq99Deasj2Yi1VN6ejR5equ4Rzb-5c0RIdlaF2xxmRtjKpgcTwvWp5tZ3SBCOKf4K_ilHPlbG8KK7J1KS15d9_aiESCpx3DhNYn-W4YlibJmJCdRRtAVUDgzrVwColqzw4vYdN4Vt6XOxgzu6MXamECy1f_zJdj_iRrbB979bn2dDET1hONU5nZtC1cvuvnJityaAQCLXVl0GhonuRkN3I3H-0gN2PArlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66617">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FOjDuqmYhszQ7H56uoS-oTWhbT8tMBpbnTDq0jII4A11vhNpHJgNlAHBZbnDH0RIpSgdwb62t-Ajo4F2refrbhEhN28gvNoa8B0SoNzDtFfMadah_3S155EzCt64hvtTdVffTcikZuAxsDQLhXWVsHNUp3k83u7OoqLe_pFdg42rxm4bFIuJgeVDwGt7prW0pxt3oZAuqm_4Tktqu0TSywLIYIXUyPprKcJT5tcECjG92HdCYkFJLFhXTCHuQm3qRj94n4JYO_xMQQjB8B6Ru4C9LS8stpZY-6GbNBEsAkRzlPCDRB3dGaOc-YpaurFVn5y9aCmN2-fEwJjJZvC7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FOjDuqmYhszQ7H56uoS-oTWhbT8tMBpbnTDq0jII4A11vhNpHJgNlAHBZbnDH0RIpSgdwb62t-Ajo4F2refrbhEhN28gvNoa8B0SoNzDtFfMadah_3S155EzCt64hvtTdVffTcikZuAxsDQLhXWVsHNUp3k83u7OoqLe_pFdg42rxm4bFIuJgeVDwGt7prW0pxt3oZAuqm_4Tktqu0TSywLIYIXUyPprKcJT5tcECjG92HdCYkFJLFhXTCHuQm3qRj94n4JYO_xMQQjB8B6Ru4C9LS8stpZY-6GbNBEsAkRzlPCDRB3dGaOc-YpaurFVn5y9aCmN2-fEwJjJZvC7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منابع داخلی:
هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/66617" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66616">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd4iysk00rCA48Sd6txXyLOHic0m1OXdnGNgJTydPTd6vCVMzkRZIyOpQPm3rUtUVnNkAIGPS2FsHT5BBM7yrFLAZ-xFfcsIOxyUJbYwtT1RfX8OAoJJQRUv2fZZ3f_Ph0Eu-gjdY9DHN9BojeELorTWyA42g28iwC1cvhGsSLQthU4PS-QnCkEGWom7eQcbOg0Z-8xe-IzKyRE_pJf6pP2elPsDgxjQpxTPC29kOIiCnrB3-8gXAOjFLrhk0-5OnaktWLHCPRAgktzC4J_-MBIW3jZJo-xHJqU8K7YW1d37CA8rr79Va8TUR4sU77rsETlcCXQu1ppCGkbsC6LJJq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd4iysk00rCA48Sd6txXyLOHic0m1OXdnGNgJTydPTd6vCVMzkRZIyOpQPm3rUtUVnNkAIGPS2FsHT5BBM7yrFLAZ-xFfcsIOxyUJbYwtT1RfX8OAoJJQRUv2fZZ3f_Ph0Eu-gjdY9DHN9BojeELorTWyA42g28iwC1cvhGsSLQthU4PS-QnCkEGWom7eQcbOg0Z-8xe-IzKyRE_pJf6pP2elPsDgxjQpxTPC29kOIiCnrB3-8gXAOjFLrhk0-5OnaktWLHCPRAgktzC4J_-MBIW3jZJo-xHJqU8K7YW1d37CA8rr79Va8TUR4sU77rsETlcCXQu1ppCGkbsC6LJJq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/66616" target="_blank">📅 17:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66615">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwipsXxZSz9wF-7dzX3lGY5LShWkhFNDj3uBQzRA8xVP4EdZ0av5ymiWWNxESHTUQbIMVMLJkOwFIPeLEmHtXlBDvOY_-y9s2_qGfyqyiX7wr8cgqo0zTKwSUawoK0XqK2TDZDmi_5M3HFkIpCidN15CtzWZbzyvu2kxLa67LI5IAMQ4ErvhFZv9E53ObatZ0ulFEPqZ2XlRR4obdoiSSNd46cElGWVju6juWN4Drq7udUqhfKWYKQDPyIZihdudIUx_142Err0FCqSc7MsbOxVGt-nJcPpEBe4fKcVu90dF_5PxKIvtM4TJAlBtdoo_dC6La0BPXs-BT05XewuuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66615" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66614">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=Nlg38XvBHwkNq5DMgxD1glhiZ2COszHvkNk500Fgeg6CM1-tSLW3ZQjBr-nnky9wYYReEArES53ihrb8EcpwqTl_LfMoo1X0YMKRifPGFP9iLpa28cXSO3bvMZpUsxgYJyu6KaoN73eurCXxTNfekzmrEpVu9oWBjjSpUkl7bQrvi5T7-NG79i8l8-c-oc8oYBLDG6V0QBd7X3qyaC9jxEkxr6ogz4lN1iMGySgMVvp9GwFUCyElLWYItijZUylW7DtgkPXf3M34ITdEGdXJzv31dWssjtc8JX_TmQQ_D2Qg1LKPTysCXqV9pDsGoW9Ti9B4kXAcgdOV5s-aEXUaLrhI1FYsJuHKxQrDcHKsCrmKnMgcA56Ee965c-HYljie74tkltcoiMrgPru8eji9BXUJfKUwqvDPbgomQAsTVNDltDaHdNOrp5Qjt48J8eoLCKKWkPKFvrWOA7IfbLezqD5N1k8u_I5OiprgY77KVvy9NtR7hBNXPJ38nPhc8mnlUYS6qQ-SSlgfbUjw3TPbMaS5e2tL7sePpz1TWE3M-d1Qjbd8ceEnVgldEc1hv1UjFpHRmn0zgqMMAOuGdcNm92wPuJuutZY-bdjWgihatgK7H5O5tarj8ir7MkquBkxJejm8rgGkgIEllQt9pifj047sQXFow8rYsM3fqHxix-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=Nlg38XvBHwkNq5DMgxD1glhiZ2COszHvkNk500Fgeg6CM1-tSLW3ZQjBr-nnky9wYYReEArES53ihrb8EcpwqTl_LfMoo1X0YMKRifPGFP9iLpa28cXSO3bvMZpUsxgYJyu6KaoN73eurCXxTNfekzmrEpVu9oWBjjSpUkl7bQrvi5T7-NG79i8l8-c-oc8oYBLDG6V0QBd7X3qyaC9jxEkxr6ogz4lN1iMGySgMVvp9GwFUCyElLWYItijZUylW7DtgkPXf3M34ITdEGdXJzv31dWssjtc8JX_TmQQ_D2Qg1LKPTysCXqV9pDsGoW9Ti9B4kXAcgdOV5s-aEXUaLrhI1FYsJuHKxQrDcHKsCrmKnMgcA56Ee965c-HYljie74tkltcoiMrgPru8eji9BXUJfKUwqvDPbgomQAsTVNDltDaHdNOrp5Qjt48J8eoLCKKWkPKFvrWOA7IfbLezqD5N1k8u_I5OiprgY77KVvy9NtR7hBNXPJ38nPhc8mnlUYS6qQ-SSlgfbUjw3TPbMaS5e2tL7sePpz1TWE3M-d1Qjbd8ceEnVgldEc1hv1UjFpHRmn0zgqMMAOuGdcNm92wPuJuutZY-bdjWgihatgK7H5O5tarj8ir7MkquBkxJejm8rgGkgIEllQt9pifj047sQXFow8rYsM3fqHxix-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت
:
بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66614" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66613">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در مورد توافق ایران:
من یک گزینه 60 روزه دارم. بعد از آن گزینه می‌توانم هر کاری که می‌خواهم انجام دهم.دیروز در نتیجه این تفاهم‌نامه با ایرانی‌ها، 19 میلیون بشکه نفت خام از خلیج فارس خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66613" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=RxTl3wXgTP8qh18X6cpsT9sEpHt_Il_jyOHO2uJ02kTeOVsrMpARk3zIVNNQlJ4-RRs2lL0lkj4hy_EWFHMtYer3htBQffjvKboDnjM3E-G-cu-MzaeLzkotgMNDACd0BeqR8dnmBYsXd-0T2oeLkyFIpGHw_6HOEXkiFeoQZ-Ra_iFFZ_KtNL-CUWNr_Arn2SkkVMvlzaJ2MPoyrIuNKug_xjm_uiFAJoxlPIUSox27whCCkFzG40cDJ3x3sd6PxylLpsCkv3su1vdopA8iAMoLgHUMeJ_KiCHS4ZrP_l_SRBHWtD5te4RV7o_2o4Xt3-oZrixpuOEiX5ozKVl_OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=RxTl3wXgTP8qh18X6cpsT9sEpHt_Il_jyOHO2uJ02kTeOVsrMpARk3zIVNNQlJ4-RRs2lL0lkj4hy_EWFHMtYer3htBQffjvKboDnjM3E-G-cu-MzaeLzkotgMNDACd0BeqR8dnmBYsXd-0T2oeLkyFIpGHw_6HOEXkiFeoQZ-Ra_iFFZ_KtNL-CUWNr_Arn2SkkVMvlzaJ2MPoyrIuNKug_xjm_uiFAJoxlPIUSox27whCCkFzG40cDJ3x3sd6PxylLpsCkv3su1vdopA8iAMoLgHUMeJ_KiCHS4ZrP_l_SRBHWtD5te4RV7o_2o4Xt3-oZrixpuOEiX5ozKVl_OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی‌دی‌ونس:
باز شدن تنگه هرمز، پایان دادن به برنامه هسته‌ای ایران - این کارها قبلاً انجام شده‌اند.
سوال این است که اکنون چقدر می‌توانیم با هم به موفقیت برسیم.
آیا می‌توانیم روابط در خاورمیانه را به طور دائم تغییر دهیم، یا به انجام کارها به روش قدیمی برگردیم، که ترجیح ما نیست، اما مطمئناً چیزی است که می‌تواند اتفاق بیفتد
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/66612" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
‏پرزیدنت ترامپ در گفت‌وگو با فاکس‌نیوز:
ایالات متحده می‌تواند به «فرشته نگهبان» تنگه هرمز تبدیل شود و ۲۰ درصد از نفت آن را سهم خود کند. «اگر لازم باشد، کنترل تنگه را در دست می‌گیریم. آن‌ها را به‌شدت در هم می‌کوبیم. اگر به توافق نرسند، از کشتی‌ها عوارض عبور خواهیم گرفت»
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/66611" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=pxe-mMNU3OwZz3F5OlqWf034ADXjuImseVilyGaluVWQYpNlW9T733QA_a47bnIFSunLTT6YiuGlS7kGkFIIiYMMbH2PMaxzoTvCqbTzfEqTsXXxiFArB8s2GNGuYV1fOWpmx9XDGDP-wRSbjOchMcRGAGO46Gxv-0ILEqN2pa_12AcPrYFpcmhRtlT75TyBWl6GEOUzmFR0sg1rzYVQNGxJTsdhmHk5RhXHI11EfpSZJEOGcUZvwAbmdeNLkGLZ7SwoB-zwonX4SjiGJuRcIHRWBrgFbRokDrfrYHQ1vp22cPTswNdDe2B530OBe-iiqeGD3_OUefBuODux43OmIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=pxe-mMNU3OwZz3F5OlqWf034ADXjuImseVilyGaluVWQYpNlW9T733QA_a47bnIFSunLTT6YiuGlS7kGkFIIiYMMbH2PMaxzoTvCqbTzfEqTsXXxiFArB8s2GNGuYV1fOWpmx9XDGDP-wRSbjOchMcRGAGO46Gxv-0ILEqN2pa_12AcPrYFpcmhRtlT75TyBWl6GEOUzmFR0sg1rzYVQNGxJTsdhmHk5RhXHI11EfpSZJEOGcUZvwAbmdeNLkGLZ7SwoB-zwonX4SjiGJuRcIHRWBrgFbRokDrfrYHQ1vp22cPTswNdDe2B530OBe-iiqeGD3_OUefBuODux43OmIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره عاصم منیر :
من احتمالاً در سه ماه گذشته بیش از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
بدون سیاستمداری او ما اینجا نبودیم.
او یک رهبر نظامی است، اما فکر می‌کنم خود را به عنوان یک دیپلمات عالی نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/66610" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=sV7IxxmqogbN7nUX1R2tAbeD5LAPjqdcg90gWy1NPGS0vh4XETihfMDcFpulqkcM5LAd4vb1QelYGM17EgQ9ETYQ7ZAihlFVWDTpVPA_NRIOCsPj8gFZYlTAQmYuaF85ptdxJNXL5ayST0bDphdBZ3SgVtQ8shlANwy56SoGIF7FeRE1sgqzbBBkisjjaiqIe7efJMORHcfsnOUkHOILmIrYMI3LspbIlDJP6Ss9Catjjy51RX_XgSFu4AXQH3TAyDWq9pQSfwv-Gufjfw6dLKM15_fQlFTUrKINSESHYnMSO5CRFl6bKh1zla6NOrJ4ylQemc5ZsZejgi3BCZFAWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=sV7IxxmqogbN7nUX1R2tAbeD5LAPjqdcg90gWy1NPGS0vh4XETihfMDcFpulqkcM5LAd4vb1QelYGM17EgQ9ETYQ7ZAihlFVWDTpVPA_NRIOCsPj8gFZYlTAQmYuaF85ptdxJNXL5ayST0bDphdBZ3SgVtQ8shlANwy56SoGIF7FeRE1sgqzbBBkisjjaiqIe7efJMORHcfsnOUkHOILmIrYMI3LspbIlDJP6Ss9Catjjy51RX_XgSFu4AXQH3TAyDWq9pQSfwv-Gufjfw6dLKM15_fQlFTUrKINSESHYnMSO5CRFl6bKh1zla6NOrJ4ylQemc5ZsZejgi3BCZFAWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان دارد. مسئله اصلی توقف این است.
جی دی ونس: خانم، من فکر می‌کنم ترامپ و ایالات متحده برای توقف درگیری در لبنان بیش از هر دولتی در هر کجای دنیا تلاش کرده‌اند.
صلح هرگز آسان نیست. صلح همیشه به کمی کار نیاز دارد. همیشه به کمی بده بستان نیاز دارد.
اما ترامپ نه تنها به صلح بین ایالات متحده و ایران متعهد است، بلکه به صلح منطقه‌ای نیز متعهد است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/66609" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66608" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/66608" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldhHRenpqVMg03Ru5lK0HkB-uv5qrIh06lexlQWR49j_nr7oJHLyFEUiwAIyaxhRLMiOpT4ZsIoi7OYOjGSMBOqHihKqXZ7Qrwr-mvcbrEI8YHq9hIkr46xb6hSIG7jhV40KKETibYod5BVaGKiqcYQQmSmE05XgOWUxZQr_f8GtC-GY2X4KfebtJZadID6oJfz7SmqpD3h0Cl8y6xxovZg2AZn06U0rs44Yaf9V_oeYthgyHcAlnHPffmwMISiSXrQW3132RK_oOtXdvXbHpFOaUj_HHXoIgmIrDPZqN8pWVQ4ZYxiNJ2UP0lGaFG0mZdhSGdBhOeOHtGWeoOOKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/66607" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66605">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7FPsnAyuwmKYwqqXDz8SKsHHJ10yxr4viSDJkdy7BT3HvExAtkVh5K-zRBuk7q_47qzdlXWulFEkb3UmDbnM4IPUbo1_BsfmcFfaAjK_n_dEaJmE8Qhi8pCN5bkrePy7SSs0X0lvJxDWNbQZfxcyVsIvUkb-E7gYMsx3VjLmtD7ZMkg6hQ_xpa4Hu79mnT0JHmtprXy8bwpaD7S7LaadUemQ01luV9Zfu5HxaxQ8lJXgOmNjAoVSm7wJ94YNac2teplGm6rP20x54enuV4QrndpaB4Ccgs645pqRdTKuHFIxlbxIszadS_pYSpeg58acL-YnnY1fbWiKqeGmSK02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=r-2FZ93cdn9o-sInw91CJsfVhvqC2BDc98Bac2TmQLe3n3pwy_THaFp4tsgdTdOaiA51pBVO69QVBOhh-nmmDn4cB0wmz94GmXmB1K09j7ut8mMxRHZyOve3Q67I01LBHtyq8cqGwfVjEyzho1ymjc8jfCCWMNf0v78-FGdjgj-lvt8VplC2eFRwNFw1YA2o1_5KS1zhaR3mRIU4DT0USG86K-4sSkEQdlwiaY9zBC0uQ84-h4-xlVH07Y038GHEX7JrgFuRHMT2d2rKIUZ6w-bkFHgCosf1vDkXQvfa5NteGNIqdjnIB0pMHTBA1pSyCVm7PN9-Ed9UpLXZXjZ--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=r-2FZ93cdn9o-sInw91CJsfVhvqC2BDc98Bac2TmQLe3n3pwy_THaFp4tsgdTdOaiA51pBVO69QVBOhh-nmmDn4cB0wmz94GmXmB1K09j7ut8mMxRHZyOve3Q67I01LBHtyq8cqGwfVjEyzho1ymjc8jfCCWMNf0v78-FGdjgj-lvt8VplC2eFRwNFw1YA2o1_5KS1zhaR3mRIU4DT0USG86K-4sSkEQdlwiaY9zBC0uQ84-h4-xlVH07Y038GHEX7JrgFuRHMT2d2rKIUZ6w-bkFHgCosf1vDkXQvfa5NteGNIqdjnIB0pMHTBA1pSyCVm7PN9-Ed9UpLXZXjZ--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کریمه در طول شب پس از حمله پهپادهای اوکراینی به بندر و سایر زیرساخت‌های حیاتی
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66605" target="_blank">📅 16:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66604">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kDUo-LjTi5OeC1vuvA5Ovy_eSD4q-n16ip6npUYa89n3tog42MvfdNDDbJ4eqzgKJs5upPYQLsdVin6GUGvd7ZNHEAn04Oa2a0PPXN2gK4p0FzDQNF4KSd1vp3JDpv8-bUbQ7hpBHBoreu2LKIdlBx9zOROcurkrEEs3mrNOc8oc0ps3D7AjWrjPSMUw-cBEeWPxsl1VLa67oSxPZ8P9hzHD_Lo9nq3K9prTiHXl0wlnl0O8SDWF8OK0SPj2sXr5RpIr0cDLTUvoR6X9KjYoZBOC8VHkASB5gWaSxoRYv7G8kUhUL8pCAppG64GBmhuA9EyRN-PTcKSKGbFgwzUznw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kDUo-LjTi5OeC1vuvA5Ovy_eSD4q-n16ip6npUYa89n3tog42MvfdNDDbJ4eqzgKJs5upPYQLsdVin6GUGvd7ZNHEAn04Oa2a0PPXN2gK4p0FzDQNF4KSd1vp3JDpv8-bUbQ7hpBHBoreu2LKIdlBx9zOROcurkrEEs3mrNOc8oc0ps3D7AjWrjPSMUw-cBEeWPxsl1VLa67oSxPZ8P9hzHD_Lo9nq3K9prTiHXl0wlnl0O8SDWF8OK0SPj2sXr5RpIr0cDLTUvoR6X9KjYoZBOC8VHkASB5gWaSxoRYv7G8kUhUL8pCAppG64GBmhuA9EyRN-PTcKSKGbFgwzUznw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیستی که صداوسیما از موافقان موضوع مذاکره با آمریکا منتشر کرده و گفتن که این نفرات به مجتبی خامنه‌ای خیانت کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66604" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
کشور قطر از آغاز مذاکرات میان جمهوری اسلامی و ایالات متحده در سوئیس خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66603" target="_blank">📅 14:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66602">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
خبرنگار صداوسیمای جمهوری اسلامی:
یک دور تبادل پیام با میانجیگری پاکستان میان جمهوری اسلامی و آمریکا انجام شده و هیات جمهوری اسلامی نیز با هیات قطری دیدار کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66602" target="_blank">📅 14:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66601">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5LTuhy8xIJ5vuoEp9jJ4NTt9zI1ll4Y3m2vLMzv08SW0TJF4Kftp5O1YGTkhZhVhp2c-_w9B_ktw63d8xi6utxWoEDqbS6T0twbxDfXQesGDCKsaokO32uW_b7bYZ6IF33jDmB3zsOT7gUOHPusEKMRWRhiXcFy3-TOVIV2zIbedCTpq0KxlGJuCBen_b-IdY881KBJxRehyfYDSjZUeXLv-7_wZ9keteDMXsnclq1dEsvvO8FtUsIsc1Wx7W6Unx-NIcYlklIOWs6fhJslBzXy8ePkwIplw2hEFQQfrDQ-1SGdjU8bipK48yncGP9G2wFuwVsPyfkF3DUbgvXu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است. بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66601" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:هیچ محدودیتی برای سربازان ارتش اسرائیل که برای رفع تهدیدها در لبنان فعالیت می‌کنند، وجود نداشته و در حال حاضر نیز وجود ندارد.»
پس از حمله به نیروهای ما، ارتش اسرائیل با قدرت زیادی پاسخ داد و تعداد زیادی از تروریست‌های حزب‌الله را از بین برد و به زیرساخت‌های تروریستی متعددی حمله کرد.
حفاظت از جان سربازان و شهروندان ما بالاترین و مطلق‌ترین اولویت ماست.
تمام دستاوردهای ارتش اسرائیل در عملیات لبنان حفظ می‌شود و نیروهای ما در منطقه امنیتی در امتداد خط زرد در لبنان مستقر شده و از آنجا علیه تروریست‌ها و زیرساخت‌های تروریستی عملیات انجام می‌دهند.
آتش‌بس اعلام شده دیروز، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که از جوامع شمال اسرائیل محافظت می‌کند، باقی می‌گذارد.
همانطور که من و بنیامین نتانیاهو، نخست‌وزیر، روشن کرده‌ایم: اسرائیل از منطقه امنیتی لبنان عقب‌نشینی نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66595">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Dqu6rmzFtUgsmzumGdT311Uhm_6l728QTlo2dARcW7TSVhhEp2mtnnOsrVNQt74rJPmtlqxbcI9w4A98VO9kBloCiKo2IWRCz-hWPy_vBN5hfwdV9diGKwktVbFhnTzUz8yGtEjItF7r09r0dLLG3iuKTzYqbnxdIzDhLRBsbvLHdr0fUakKrcSNrxkP0lLU95IkVcmrnE7bH6Rn_TnTgtDYEL_lKZA7rg7smGXso2rLUuQ2IkaGAUvPZPvso2Fh20LlxJ7T-4_RAMZPKclcJRSvJLjKQTlnaVptZv-dYsVS7StZ83q2sY6nYD8WqvEkW-XtVKj1i9vTBxJ0S62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند. اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفاده دشمن قرار می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66595" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gor1Vh9vu5RrJ-gAr4gQIaXwJXzbv2VyFUtzhxxP4Mw7WRzt2XosKqNSa2LTIYjpysv2Qp4uRpeByktiFM0ouzWjpOKK_v_gV0fsxiPK1FuYVb3OLcJYWN8Cm4z5wqK5l9aRsZV506pdATZh4_PN60zV_WUfq7GtvHddkNPCnbgOCipFUO02gkC3-otP6HfhBt7YzkA50DbTiuaiytR89yYaYr2FRjxunkh_3f4YSip2Quw9NSaJWjGp2Ndc2I0FfWww414zRuf9u0GKYf4cWX3F1HYTIMmeP_wqPWTt6z3ZwWd7gWTnSa-qmy-QOzxSXX8Oz_CY-H0bEQKk4WK-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qtcG7baG2hK37R25IMR6bV_xQFJ5wGXUbqcf_AJgmlz5fBww3HVDqATsQDEgehyHpLDPxlNVg3MBGMFiEpRRXwjyueM_dWjMRvQVxb09hZyEfU4qfT6sRuhwdWcKV8TgemBGbonx_symwaNBcB9CFDapciLnAbuAoNjDjt3OjoXdxhtmj_b96PM0zOb4o4h00MObXFnvw2OeHpfapSCmNFVMRgKBHn81R6rnQ3E-BdyNhh_SskQz-ATmng_GbqOqI3pEGYN4TZ9gAjoQ2yKfI9vj779f_RGQ__2MZVTxTcPSs5AM-aUGpzSx9kUwD4D7hRoZiRz6O7ytS-ySuaR3fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qtcG7baG2hK37R25IMR6bV_xQFJ5wGXUbqcf_AJgmlz5fBww3HVDqATsQDEgehyHpLDPxlNVg3MBGMFiEpRRXwjyueM_dWjMRvQVxb09hZyEfU4qfT6sRuhwdWcKV8TgemBGbonx_symwaNBcB9CFDapciLnAbuAoNjDjt3OjoXdxhtmj_b96PM0zOb4o4h00MObXFnvw2OeHpfapSCmNFVMRgKBHn81R6rnQ3E-BdyNhh_SskQz-ATmng_GbqOqI3pEGYN4TZ9gAjoQ2yKfI9vj779f_RGQ__2MZVTxTcPSs5AM-aUGpzSx9kUwD4D7hRoZiRz6O7ytS-ySuaR3fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رشته کوه علی طاهر، دژ استراتژیک حزب الله در جنوب لبنان:
طبق نشریات این سازمان، در زیر آن، تأسیسات «عماد ۴» - شبکه ای از تونل ها، انبارهای موشک و مقر جبهه جنوبی حزب الله - قرار دارد.
یک افسر ارشد ارتش اسرائیل فاش کرد که عملیات روز جمعه، افشای یک شبکه زیرزمینی حزب‌الله بود. ارتش اسراییل این تونل را محاصره کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66593" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VauJLf2UYjW6NoVVBHie_-FOVMcjUF6e2SRRjUwOBCgmtNJvLAos1vcCf6lkMIP-dmFwU9x2ykLXDq5_Kjt0S5QWjad1AjtmsWfppNRpqCjMN2Z5WjgrbAO74Rl92hZfUjVXzJyA3g55wVlp8poTtrYw8a6hZmNB3cz0vJqCEVl0BHMMj1drlYnTe4fTchPlibMf9TbE0DSUT5VVzG1VzXcbfxSQl0n9Zaa5nviD3M3vdvNt9Pe5OE_inOBXVP9PDEPIFDPqm4YV7oAESDiEB5NWejGG7GDvbLJRP-UdUMORuSo0Ww6qJMXuyKPSvfRzegHG67m4KcwYRO6o2s_voA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پس از وقفه‌ای بیش از یک ماه، صادرات نفت خام از جزیره خارک از سر گرفته شده است.
تصاویر ماهواره‌ای دو نفتکش بزرگ را در پایانه صادراتی نشان می‌دهد که نشان می‌دهد محموله‌های نفت خام ایران بار دیگر در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66592" target="_blank">📅 11:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxume8HH2NNDee5-mJYJRAFdz5U4f8Y6oguPqhqwKZvxbzrJK4NSY8oGBVTxSMgiv2ToE1GYUnIH3bW-uScpfWB1vaz28lXMdKvYncDjrmvMRPEdiNJR7b1Fc1-tfsSpI3MIp0eVVCP8R8OBPI5H4ES6-aorSIKdDP8SsQzLfoEVPa10-3f5bQP2PLgL1JJ7nv6W4bee-8YOXB2TMwA2TlAzySAqL3dNV2Ipref9zDvpLtYf_U6je_W0evaDbJsyKrKqccig-1JWaPCFhJ_-hwYjfvXsmud2U4iqQ9Y3fSp6n-HNrJBSAgwSV43jroyJikCzunMm2nKZFnk3QzSgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صدا و سیما:
علاوه بر تنگه باید فرودگاه مهرآباد رو هم ببندیم تا مسئولین برا مذاکره نرن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66588" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خودزنی مداح وسط هیئت:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66587" target="_blank">📅 09:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66586" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwMM2R9FSnA5NUe6lrxmXI-lrUvoAFZSFbs_nPx7XKVB2KnpACx4tKBb3qoci3fRs-0QienYf7kZV8CHAA3KvulCMFAau-cswARslfq4oZ0DDXJ4SF09jHc5NC5CNhOQg1zkLF8XjB5GUiWyVuCyVcDQC25qw-CndvktS0-bgbH6V3mj5kbKsdtA0nQmbDd6RDAnHiIEm8buxlgBYvGBoQtdU4X9dDDKFSd8Grmr3HtaFvaaxm1auvuZEWoIz-OguuOreT3ptX6miqmYCMP2ygFugv_53EOKQAppviHBxGgiI9qNIpGCQSKAGA0cNfK_RWcdp-ENj_vm1FaAZXgaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66585" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIsz0qNCVGj1zezJNUfP5mGoSkQvdk6BnjugTRlmJRe-aWlJKDO2733we6LJWH-Vlu-pVpLS8Sk9WT3gvFYTvqtBxJEoStrvysxbmjdt0JXsIVw_uiizJkUY5ff4k7NQO6APTzYazC-XCH2Yyh8oUfu-I-s7FlcpUmnvMmv5FaUFibAftXTipjeuwQjcnouAvCoMFp_Z18hip6I0dtFj4moZOyJXz27d_Ac5CPCqjUnCidzK1gPGMbPvEhUX95MKiclf5_UfvmG4K2-nyGxWfV1S6FdjNo6EtnA_rQQk73ZFv4rC22yywmaxgZRl5_C697Ej0_xuacI4Kx90vAyRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف بعداز ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66584" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=Gmxl597TFI62hi48fnesP2ErIz_ZSkLs_o6HKtemjqsHIyiDzLzJfDA-zxRnft3VtrJpVqBDTrK3OUN660Yxcv4KKs70x7QDk6Uw8rCF8um9mJKa_UmB8OgkyA7lgg2hSmla1JUospphnj61aBAZfx5oksBTWr2cIJUkEbGaHk2XR4TRAltNFRvquqmX3dKzUt8g_oMuSn8IlJXTaluUVplLGgaYF1uSxQ28B-iInpPh936gyOn-vthqzyrYad4FSdfc5jIXSbp0Oh_5mOPq6ygf2Tp1OXK62mBb1Fe29XvC1m5u-H82gEfcjYMh7ETNV1s-YfVxEocc6XCp_4O0UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=Gmxl597TFI62hi48fnesP2ErIz_ZSkLs_o6HKtemjqsHIyiDzLzJfDA-zxRnft3VtrJpVqBDTrK3OUN660Yxcv4KKs70x7QDk6Uw8rCF8um9mJKa_UmB8OgkyA7lgg2hSmla1JUospphnj61aBAZfx5oksBTWr2cIJUkEbGaHk2XR4TRAltNFRvquqmX3dKzUt8g_oMuSn8IlJXTaluUVplLGgaYF1uSxQ28B-iInpPh936gyOn-vthqzyrYad4FSdfc5jIXSbp0Oh_5mOPq6ygf2Tp1OXK62mBb1Fe29XvC1m5u-H82gEfcjYMh7ETNV1s-YfVxEocc6XCp_4O0UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiC5kW2bhN4dh8GgWPEpLgUqPGsNsyHJ4U2GkhEgC_H6Ys9yL6lluPUKbuXF9j7KfmwczQxDoPB1ooCcY_X5Xn7pn2zVKzS_Cv22nHUNz0lIYKD4ed0NRpgCGjxtgUnwZS3QFOwrlfg3YxKuqoLcAliKTHLnzlXXhd4gKWFsAxaTJCO009uxggyFOxbDspU5uQY5Hm4s72WwL1mGODybbVDUoTjLC3L7vo8hJ_-sH-bNtz7BvKqmEH1u0FPndCLb93sXeZcxYkFCjG9DtKaBU6sefJYuUOdcikB90sUtNSOzuUplZhYTFm5MfuuZobHIrM9MTAPyIhIORjoXWyCQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=kTXu2zKliCptBUDxg_WdxZdzC3kv_fy_42p1vQMUi1_7Xl3Og5yKt_w1U5RnZicgiLJiPzo5Qp5XSjifj55LFgcuBvsLTimk7Ts-dZaN5ehDHSg1Y0V5DGBTtdzEDQ9iWH0286k-R7esCcQiCoL_ha8JQeuLzn3jyzqTsXXglRaw5KzHhAScRJ5DhIoF6aXnvDKuf4qCFfr_AYel0ldZBiLSWsRrGGoG2IkHADCunjBjI6AnY2O1v0a8ZBonzdZx4r3Tlnntyw1uACcCeUKFTyWUq82_TzfWo8YkDWybOraHU7QXR_ulxOJCS1faiiXG3C--WH9rhaiY6sCKX2gnbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=kTXu2zKliCptBUDxg_WdxZdzC3kv_fy_42p1vQMUi1_7Xl3Og5yKt_w1U5RnZicgiLJiPzo5Qp5XSjifj55LFgcuBvsLTimk7Ts-dZaN5ehDHSg1Y0V5DGBTtdzEDQ9iWH0286k-R7esCcQiCoL_ha8JQeuLzn3jyzqTsXXglRaw5KzHhAScRJ5DhIoF6aXnvDKuf4qCFfr_AYel0ldZBiLSWsRrGGoG2IkHADCunjBjI6AnY2O1v0a8ZBonzdZx4r3Tlnntyw1uACcCeUKFTyWUq82_TzfWo8YkDWybOraHU7QXR_ulxOJCS1faiiXG3C--WH9rhaiY6sCKX2gnbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود. از توجه شما به این موضوع متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66580" target="_blank">📅 23:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
جدید: مقامات آمریکایی ادعاهای سپاه پاسداران ایران مبنی بر بستن تنگه هرمز به دلیل تنش‌های جاری بین اسرائیل و لبنان را رد می‌کنند.
یک مقام ارشد به فاکس نیوز می‌گوید که ایران نمی‌تواند تنگه هرمز را ببندد زیرا "آنها آن را کنترل نمی‌کنند" و به حجم بالای کشتی‌هایی که اکنون از این آبراه حیاتی عبور می‌کنند اشاره می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=ptSTvsjxsFTmGDVABv_x2s8_TFWFmMePw_FsS4UgP1ThCVLudrM0HMYIOD3nPqxiAmtHbf2BUoKuYjBocPUkKke_-OyGOfhBgn0bp4iBBfkqSFucgW_kSe86ClHTPGuk-WMuOW6miV-xWUkB3YsWxj_-zMGyd9FQrpoHssC_s3pe49Iu9oUuEdckT7QNlp4xgobVuufc52aIKPnTtGzMAMtisDq6RaSyN4Y-b1LDwut3YRPVGYm_OU-SGcrKCXoSlIMdmHh9NX4VmgmTjB9Q8y9bjdJPMVhmsHndjIlLO-D4ApJdK40OOyR-dAdezkcyiF0Ooy9w5ORuDKFfipukEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=ptSTvsjxsFTmGDVABv_x2s8_TFWFmMePw_FsS4UgP1ThCVLudrM0HMYIOD3nPqxiAmtHbf2BUoKuYjBocPUkKke_-OyGOfhBgn0bp4iBBfkqSFucgW_kSe86ClHTPGuk-WMuOW6miV-xWUkB3YsWxj_-zMGyd9FQrpoHssC_s3pe49Iu9oUuEdckT7QNlp4xgobVuufc52aIKPnTtGzMAMtisDq6RaSyN4Y-b1LDwut3YRPVGYm_OU-SGcrKCXoSlIMdmHh9NX4VmgmTjB9Q8y9bjdJPMVhmsHndjIlLO-D4ApJdK40OOyR-dAdezkcyiF0Ooy9w5ORuDKFfipukEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرار موفق یک کامیون روسی از پهباد اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FI1mdzuJclGwBw2v7uWtOkzFfoVLKsK7eAjx5zYgvTSRO4OvKCzV4pJSGNWh0mKBjXY0QrpZcrdH_P32wyfe11XzGgbQE8QgjaaNbmVaUiVRwio72W0-70a_7d0LAocI4mbwpG2VfAZEBdzL8zZAW30iIYsx_Ur3SKbmoJ69oSi-zQwrgFzKgqePgek1mV5WTTwekFQl6Er7c674EKr6Bsrarmvbi9PYctD8lz0DAHSRaELRQv2XhkKobZnoxfVUbEE8XONrT3OhrZYheSz8KLkK8vcaoZtVqkxFelWdg1LdoJcW6jFqU2i85Tu2mwK2nfS9AYXEJueG-FP48nQc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
امروز در شبکه خبر در مورد چرایی مخالفت رهبری با تفاهم یادداشت ایران و آمریکا مشغول بیان دیدگاه رهبری بودم که به صورت ناقص رها شد. بخش مهم آن بررسی متن یادداشت تفاهم بود که علت مخالفت رهبری را بیشتر آشکار می کرده است. انشاالله خداوند ما را در پیروی از رهبری عزیز ثابت قدم نگهدارد.
«ویدیو هم از لحظه ای هست که آنتن از نبویان گرفته شد»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66573">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66573" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66572">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW7KCfz_g1sn15mqhoA8lK-lq49vTxzGUFrZDY6YUSes4L9tfqz45UWacT0idnsrkFXV6jxUnqeP4bP3cMYrGZXVEruVpaWYAfRSyIDGPFXO0V9I6JT0C_LGcAIegRPq4MPjv6S916TdkxAddTYw-3yOLAHFD5TGE9uBpRJCdzHPBXHSaMhZhnEYVxbCX5ynS1eMSVq9TtFSJCisWzNvHHNAmVqa5glskVU-wRz-QvL1_1hGt-DFQ790SwFgLk80hYXRocSd8arMz2iwomQYKdHAHLSgfDetFrWrYUYld9IEpMcQu4QD7LckPN41ufVuv7lOsYy8Mhv05AUkMFFFpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66572" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBwQeke6WcUGJDk-3I6ozpJCYTW8lp8xwx5TT5zSfKvEKPEqQD8P_dzt8nXkzk072fCItvlqCGcEDE-f6zst52qtzvot_8aRTn6mKWPxjsh__go_vw3-IJiYuIwrMxxA_H7SZtqXXCVrq0GX3vZ9jaa_nG3pY3GjZiU1qxcM0okoukvyfpdx-FLFPApfmIfRKq7l7DdqmaWJuU2ncxBxaq9h335HcHMBkj5-5MY7e9NHoDnYca-StczzlgAIyWOZtc_megsOvTQXEvB3QLewIWa-zt4UpM3PceqbfEwg2nf_jRHlXEZPow8dDQ3y8MgqiDZLDEGKS1rOSk-z9xMptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us0xD_S0JzkvNsj9eM3ilhJqSPO1cSlAaxFfXjmSKMBMHzhQhcY9WRUqb5tseAZfCCZ-i9MFU6WqcSi7U_qTQKVwQbTmyHg9a_pZCIoYlt8NTQOTUlEualtWLB1j-XtP-vCnXsuvao0GePLQAgk8UifSgwjlrHS4Q5yj6s4wf0l4zMDk_HYJ7Nta8bFwSKb7CT5a9oX8SGsCZyh4MGMuGM9rEjvl1U9D4ivAN-stWEy0SB3JasmdIwFD3TZI0ew9EKB_65Dxt0xr34O-UxlDRlO5Xf_jM1IPBk_ixvgnSiak8e5CVVJYzz4PztTi1yZlDVnTHglIhuWLxXsd7S5Bpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=S7m73mfCwPps0UOHiTb_QDvAwPn6PiB7oYukvd-gUyMa7dZnJH2PVDAfhHJRjeEwIUXP0fGBKL3jqw-tmt09Roib9C6QXp0xPUxGEg77PbNs-jFc2mMQ347BdPpGFNwThxu1CtXfEaPs2bNFzjIa-EzW-I0MO9xO0ST8HqhmkffuFzMPfXOMpJ5Hse_eaxeCYhSiJWn9es3YklHrKqRTbv0R0gGY9QkXUiIi2Or9O_ZnUzL80RFrZ5FslxafqQ2VqnPr2trYJLUWaT2T0hP8QZ6qj0h7LHPuuSYubZAbmfXmx1YpTR2JVNcsg_rEjiH3XOQhbpk0ikbHmwydpGPEsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=S7m73mfCwPps0UOHiTb_QDvAwPn6PiB7oYukvd-gUyMa7dZnJH2PVDAfhHJRjeEwIUXP0fGBKL3jqw-tmt09Roib9C6QXp0xPUxGEg77PbNs-jFc2mMQ347BdPpGFNwThxu1CtXfEaPs2bNFzjIa-EzW-I0MO9xO0ST8HqhmkffuFzMPfXOMpJ5Hse_eaxeCYhSiJWn9es3YklHrKqRTbv0R0gGY9QkXUiIi2Or9O_ZnUzL80RFrZ5FslxafqQ2VqnPr2trYJLUWaT2T0hP8QZ6qj0h7LHPuuSYubZAbmfXmx1YpTR2JVNcsg_rEjiH3XOQhbpk0ikbHmwydpGPEsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏پهپادهای دوربرد اوکراینی پالایشگاه نفت تیومن (آنتی‌پینسکی) روسیه در غرب سیبری را در فاصله بیش از 2000 کیلومتری از مرز هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS2hSnduyoKcnqI_0hRScIdE2a933Zeqx1PG2qbrCsqJ6rmrT0mev51UaEAFxd90sSflQBD20Z3NKz9u_y6iaqNJ_ODUbkbONpGNdBV6tr0aNakDOsnuwG2UB_k11DbIIX1SFFAhp9NEiURAayxjciiLkMvmlS2vqQbIETiezlrVsKaSgwLvJ6ZL3A4ld9c6-iJRt6RTjb4CpBAcjeZT8YGmUDmFYfYgaecynEVc-dLU5NvRS5QqeO79DWbYxL9VEjqOa-_trJGCk81_g48TBAKOZefys_EjXYYj1DQC-pmNstaDoGfiZvr-QgWX1-i_UAWFGHV0rBEUkR2Iz13FZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ7FZV6oxS2yntSMnelO9EIGSY5UwqWCe1-3ShJ5XJ9nR2p-h04CQpJQAVgteJnkwFj9UOTKJeF_ABz3knv5gk_-B3i0Wk8qq4P77T0eVz3aj9jgEb_O157LXg8jOahxOdJSl3pDX6rlvuHHVr_jScGBTvWNaTZUELi6ePfFB5ld4h3jM7ZQortLvrU__VfTmNjeNtgWFuyiBWT8686ttEC0U3r41WPbGT75HMnpGZkFR7S1h6K9HNVNoKwOZPHv9TlgUyjXB8DCC76XqYz_FHKiIHmsMzO7WHgoq8J87kSIbKozCWtZhR3v0TGE-bgnpfO1BLmYfMR0IWRlnykDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_GB86KH5t6ZqdIZoRpaUOfsaDJtuwalArlbC_ip-AkgOx_0vDsU_JtX1t2ShJC6eLGoTJ3-R2UzA4fRl4c47TYQRYUPw-H_yQlGBdxe9OaQqXZUzSfCTUa1S1a7qumXRHedJha4BfXKPKymmFuyX54YN2s28C6JreB2mFV3KWgqbcXjWWYXWY_5Z-dhlPQpXtFMffNjdGXPQbHJE1jtURf-KiAhsa0aA8hyh8ddOMkY4iqIW44FndyLHE26zZ8miYXJD1OnuVYWLzE6O67Fu63IaGTdbrG4LwiN1BIJo5dSZLEc4hTe6lljNWx560DxvybzGlEIYxTuEiMZxKgP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=ILcAcNJL18uJf_Ym8UQz_VyRqiZLHZ94u0lkHB4gCr5l-_Ct1PJzgxh-J4g7y_SzSnZkDNU22tUDAoFywMN8-hAhr8mTmkB90Mh9fFltQWLwXJ1OUNfJRgFkkzJFakorFKNdVkxo63AFd_jTvJsNJDV33CmsuDE2EUETKX97BOY4bOBynj4XSy7SvHFLMYWx_r0X0BzVqR1yA4R1gDOVJNVm_W6hK27NmlJ0uFLLMWyU3XS8aGK5KsB6LZeBDJFsObO-0OGISlUtuayif1OxoPrnvq4sK4uZHKm5vXXi3IdpRIhf6Yt-9YuhJ6C8XesqhZelSCRKEwt8fc3KtnxK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=ILcAcNJL18uJf_Ym8UQz_VyRqiZLHZ94u0lkHB4gCr5l-_Ct1PJzgxh-J4g7y_SzSnZkDNU22tUDAoFywMN8-hAhr8mTmkB90Mh9fFltQWLwXJ1OUNfJRgFkkzJFakorFKNdVkxo63AFd_jTvJsNJDV33CmsuDE2EUETKX97BOY4bOBynj4XSy7SvHFLMYWx_r0X0BzVqR1yA4R1gDOVJNVm_W6hK27NmlJ0uFLLMWyU3XS8aGK5KsB6LZeBDJFsObO-0OGISlUtuayif1OxoPrnvq4sK4uZHKm5vXXi3IdpRIhf6Yt-9YuhJ6C8XesqhZelSCRKEwt8fc3KtnxK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=IlstdCDsA9kDqg7zNq76PN1si7y_WVuqDU0QS-e01XF9EXi-eQbc8IUto-lr1FN_9gKImimqstjPAXkH5bXaLmkrGfXIJxdA35xcVyfvf4jLh-zllv989i5i3R76J3LfwClSAo6RzrDOvVyF0-vA80qQtbahGmwGpn4xrQHfug-OPpsLJnYo9GN8UHgSdrB1QyNpUYHouLsIV_Mt31jB1bUf_yhMiQ_XNdoI1ZbMkRhvFF7cGmauGQllRGoHNVc3o8v0wOZbMDWOmHvB6U0d2jqFgBqCWooNsFZRnNmgY5Ta7ZxwLKRLbNBa3jFayYhKLN5QFFRA4eWinZZwH2yroQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=IlstdCDsA9kDqg7zNq76PN1si7y_WVuqDU0QS-e01XF9EXi-eQbc8IUto-lr1FN_9gKImimqstjPAXkH5bXaLmkrGfXIJxdA35xcVyfvf4jLh-zllv989i5i3R76J3LfwClSAo6RzrDOvVyF0-vA80qQtbahGmwGpn4xrQHfug-OPpsLJnYo9GN8UHgSdrB1QyNpUYHouLsIV_Mt31jB1bUf_yhMiQ_XNdoI1ZbMkRhvFF7cGmauGQllRGoHNVc3o8v0wOZbMDWOmHvB6U0d2jqFgBqCWooNsFZRnNmgY5Ta7ZxwLKRLbNBa3jFayYhKLN5QFFRA4eWinZZwH2yroQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=KaotGCWSbCYr_3z6ZZJ8_xia0YJ220yJ1E98P9_mDeTbDNh0XCRsB1SLKCqdrhSt0VmoyOTn2xjr1D_QwVwn3EfRQ4Yux4vUFJd6xkR7089tWZwTh4be5sdE-LG4QmmSRsr9jqSV8-URDSn0itJooER-uy9y8vMdo2cb0wY1H3Eoh8-82DnFPeepdcKP4DNbDnpMsWTKC2LE9WAbyxDYFqlPuXEDrs18MxdGEZx_-BhGgRqmZ_9yDdCnT3XAIU8tWkTu8t5FiMTkpB_cluAbjWN3c2vl9NfKMUlxUNd2NXp8rqpDGCeWd6K1HUYnqcDaH3PIcSA8dcjCW8PqbRpovw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=KaotGCWSbCYr_3z6ZZJ8_xia0YJ220yJ1E98P9_mDeTbDNh0XCRsB1SLKCqdrhSt0VmoyOTn2xjr1D_QwVwn3EfRQ4Yux4vUFJd6xkR7089tWZwTh4be5sdE-LG4QmmSRsr9jqSV8-URDSn0itJooER-uy9y8vMdo2cb0wY1H3Eoh8-82DnFPeepdcKP4DNbDnpMsWTKC2LE9WAbyxDYFqlPuXEDrs18MxdGEZx_-BhGgRqmZ_9yDdCnT3XAIU8tWkTu8t5FiMTkpB_cluAbjWN3c2vl9NfKMUlxUNd2NXp8rqpDGCeWd6K1HUYnqcDaH3PIcSA8dcjCW8PqbRpovw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=viMQnF5nlEjSszBQR0Gs1PuLnsxRh_EAph-_IXqD1Vgozg0QYXHPA0WKfwvXfiqal-TmS3sxeeY1JkqTDCf6mRIowst_KKz1GN7c9LdQa_XX0Y6d-6tjaXU3cLE6p1Krt778-OarvNa_kv_A_gYYpgehPMrxAubFdkZ62asuGxPeaG4sl3635A1fVLPjrj1v7turLVgkzlOvbqKpzwf4g_5xELyvpVe_ij6TuhL2ZbeRWVpwGy0_VTgLL_3U03awES1h8ylTVzWyB6sd56I5hYh1A8mvqDttyqrFeesqnOl-zFz5K_cszYzx8fJhQwigMr5LrGrblFDMDAGygBqdNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=viMQnF5nlEjSszBQR0Gs1PuLnsxRh_EAph-_IXqD1Vgozg0QYXHPA0WKfwvXfiqal-TmS3sxeeY1JkqTDCf6mRIowst_KKz1GN7c9LdQa_XX0Y6d-6tjaXU3cLE6p1Krt778-OarvNa_kv_A_gYYpgehPMrxAubFdkZ62asuGxPeaG4sl3635A1fVLPjrj1v7turLVgkzlOvbqKpzwf4g_5xELyvpVe_ij6TuhL2ZbeRWVpwGy0_VTgLL_3U03awES1h8ylTVzWyB6sd56I5hYh1A8mvqDttyqrFeesqnOl-zFz5K_cszYzx8fJhQwigMr5LrGrblFDMDAGygBqdNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCexuoUFBiLp_dx3a8h2kp5QhTXYp_7fhjf3-We6_6Em5Zb6lMJU4fAiWn7zrU6_OQ7VbINjEDmMzTdI3RxU0f9LRtLRNThpUwi0vjVYKmT0MZISYXtG4kdYA3En0wIcEzMO8Ai45pwN3CBNHMu8caoVzcQg6w7fMFjgei6wsv_Zti9zshgv_yso1ZpaqBchtg69wW1iUCIXLzDKjf1Jtnk-hBw4sMDGVyBjeQgHnrTxAr-y5bHOm0UsMFmjktWwZtEiRhptyFr5tVd9wp8zRIfb6mxVWP2-J-rBLtABX7lYUqzjGl2f-mUJi_UmWTKZiZRjA4Sk6otX252CynPQow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUkPxEYOSLRhz4DVNuhHV_zCIF74goqyoEJbJeCk76WUK1jszghuBABnIDG4EM5qt2NGdBRcOkzcHAppI2mlwGskhekqapJ7y-ZwfMAZtAOHtN-9zragYcNafNfctDscR8kp-mJ0Nx8rUanp1GZx-u6391-BLtGsJbIQ1sqkSdhB8_NHG8cukel7oMXqFd01bTMLgtz6mzHfMv0q_h3ZZ7cAyOPySutqNgcGvFVHkiY0z1YTwpS_FeBym74F3LFj6ZN-YE8vpXqC_feEA_2Qg5hzS1buBfj7ribqabdH6djfSXfqRHgYFqEQL4OIwMBeyfgmDNNQnNXY4_M9iuYYbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWod8axILcdjsUfJVWSRmSs8HZ4Ro34OEabxl3vVEKBb6UVCM-rQYlPbrQTlq7Elg5ZsoOZ3Qpn67UmTYdJvGRn7m42CEZfHYxQTlUIIZbCEsPS5LKMHCnMtuXsExdJxd9sHbHpyp7Yr73TxCgXF3UZPMZkn5AqLkmSX_fz-4WfrjWshtYKX1C8IK7-uQ-dsNcQ3KW3Wtd23HqQnXtSaINjguCbA9K9kn3yI9GTAexX8FNh16pbDb5dKkfdIw-QRUtxxo5qN_lcI8MMpC121S9c5bz6PlVaWQ39b2KM-VqjLgtYknM5VHU64opz4E2d2jtmDr4LIsydc_8eKCxGL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFMvHdMF09O9BCWtf8o6A93TKDXieT-RwrmelxD4u2QTvmwD1JfXIkQPu2a38pjgMgUuWHpHyILa6xNzElgeWBnJ0aa9gTvSL9hSIsR9JO4v5osz9tnuSmVH46XiRJAdkIj-A7LxUA6vTm_7cyv1zEVB2FxNLJDygv7_Hr4JKB3lqQK-1oMVx9Dcb5gV-qUGSXvmG2fzvSmmMStR6apO2TbUw9P3PS2YpISqIaWNUNuF7pfY3k1KBYTERZlfkrXX2H4OfXw0MIX3wSsLS3hY8bfsl1SolQPtBL-zAjwimfeie9dJkSQrX4Edp9D5PCV-pbKRDvTOIYBVvUxd2rfv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ_yjat8WQ1RJeniUuoOGJmoTsqsh7SpAwbPoX8NBxflKBPNMo8o1320qOCNQO7BIRZ1_rT4NXQ_ieUM7syYr_Pm_ehB1yHVrty45Zntbe7FplzqI6TjRyLAZnb_6Pvwh_3zcoUCDvbwH_O_AWjqfUrbyqcC35ruLncILQgec5hmQb8RqgFkjcdcynm_fzpn65DfVGB-T7XS5EDTy28Njky_pGkmhB0eLQrU-6Ojnnvu1B-AFfGfjGJLfQcF_uKrq6VxSL5o1gQT0U4tecU61f7mJnZ-CigfVSFL2y2qcc4yFmnA82EN-lpYt-nmOdRpVF0TLEZ-yIHEnF0IQRKA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsJpfek6dwYSDwbv79ld67CMXWBzQ_I4B7xSJMtVTDUksTQlcJq-mOU34YfhRM1YmPkCUpvszfHXZHW9bASP9IC7zr2vcU_Ud-rLM3EGRMYyVPMWiCb0iQ1F-FVFc-G8SAm21HGT5q8ENm7NKsM_tjrqNu9gHXGvJTzYNn6bQD_rJ-zFJarSYg_h3Ro468dMIOd88NVuhaNJzwuyOd-7_xWA5-WxySWutPBGe_XzZNDhKWGa4PCs-r1gp3RfqAYrdUGUXACMnh991-ntQL8vaFgQrQjDJG5eGG6tkadcaHOMwwuq--DI_pCKytV8J0kehC1woEvAqBmisorsGwO-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-INA6htehVhIT5--ktsV_G4pWMIfd-Y8oyWvfnUed41AQ-GBri1H0unOubpG3wcZR0PopHZg0DjQqEykjKZIO8Cc8jY_R94LUrsCA3rBxbuS_keDrKK1RN0k7hqO3jhuzXy2GiYSsMe68e0m0QKhKOlPJdSi9YY6C0_wPzy4Dgepxsk79lc3imoy3FiEYyQ15g2is5eCZ67-N3ra423Fi2izHEG9kit1zbIBuDfnzsnmb1Ucdba6OEAVTNGVZ_mTtEQc-9xjC6DaSHf4BL0na4xPY2VlqN7G7DyNYWck8AE1ogqYMae1XLPdxs0Br0w4YVMsxI5ACmhpui12qlDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=FqDwAU1t-tl1MwtUuhnshxvwlfd19IhT2SqBcLP4h4Zrd8TrajD81sklEbx-cSc3-4LJcJ5cjxPDY51GGI1akgNQh2kC5047Ui1h9A96SZllJnk2NW5dQKE6yGmmGFtSN5s23rBYCjidpsXe1l5pNvkTpL-hmplJchVsSGvNfHVJawCOrY0ksqgnFVvf7R770jxOrhJ3RadTvselpB9Uk4kxziwbqdVB51s4yhd05nWnk2bHvJLLIYSi2h4x-0LpKISMq1tSj_nnC9mnPCNGRRikYdaP4bWX4w6ejKxK8qhlfV3cv4q8opbYNTAWhLPJHeLZm5PqK35d8nAkX1J0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=FqDwAU1t-tl1MwtUuhnshxvwlfd19IhT2SqBcLP4h4Zrd8TrajD81sklEbx-cSc3-4LJcJ5cjxPDY51GGI1akgNQh2kC5047Ui1h9A96SZllJnk2NW5dQKE6yGmmGFtSN5s23rBYCjidpsXe1l5pNvkTpL-hmplJchVsSGvNfHVJawCOrY0ksqgnFVvf7R770jxOrhJ3RadTvselpB9Uk4kxziwbqdVB51s4yhd05nWnk2bHvJLLIYSi2h4x-0LpKISMq1tSj_nnC9mnPCNGRRikYdaP4bWX4w6ejKxK8qhlfV3cv4q8opbYNTAWhLPJHeLZm5PqK35d8nAkX1J0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=sPI9OJqWmNqhXBvHZCuE-AljdKvgEFrFK4-vh36c_wLt7TDIVQ11eH1rvsUNxRWBV5CAWHtcLkNOSwSHTzbvMJiUBKqON3KGmLmvJwjobVEEKLjqaZ3brIVLBiGNIgN_V-9BADw470yGIqZz2nAn7-j9WTLL0wkHoyyZTLiwXycbvXr4NxdMBy3SqN6RY2lfwcdjpb-WgxdZA_E7xAVJHBKRTdFQ-QLZeZXQ38y2drKRWjOP4uzxYbrg4vk0ikP2Bzmw1umXCu8r8mFj0_ArDa9ZZ9CbrjKYsBXRScgkShL5IhejF3cGdif-5gcGar6a8_dVDUN4dHrY_KvgD7ODhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=sPI9OJqWmNqhXBvHZCuE-AljdKvgEFrFK4-vh36c_wLt7TDIVQ11eH1rvsUNxRWBV5CAWHtcLkNOSwSHTzbvMJiUBKqON3KGmLmvJwjobVEEKLjqaZ3brIVLBiGNIgN_V-9BADw470yGIqZz2nAn7-j9WTLL0wkHoyyZTLiwXycbvXr4NxdMBy3SqN6RY2lfwcdjpb-WgxdZA_E7xAVJHBKRTdFQ-QLZeZXQ38y2drKRWjOP4uzxYbrg4vk0ikP2Bzmw1umXCu8r8mFj0_ArDa9ZZ9CbrjKYsBXRScgkShL5IhejF3cGdif-5gcGar6a8_dVDUN4dHrY_KvgD7ODhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=d2EOKeWpcnOCSdH982HW_UzBeFzvcyWl6ttFYEyqe5Sn650-wqtpp3nq9ypCBTRCwzakZVhijiPRSZtc0D-auixEPZUZ0iP8bdkhoOUxrAFEKeNiTwQ80XyJIuLjV6dUcAdIcHLONi28nhk3gJsy6ga-oM6plzi3-Q2ST19YXDtpdBWEPSDBbCng2d162_Os12SL9TonpE9vXbTDTJUWEl5lrl42o3_WlwryrzINISoP6UYTz4uvyAqImMry4-xn4CiRfq29GkV9M8OY_1fOdbHPX-ec_2b6QjSKt1D2rT74U8VJ0WA6UPtiNenPSsb3LHPew_xk4af5Q04_qRK7ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=d2EOKeWpcnOCSdH982HW_UzBeFzvcyWl6ttFYEyqe5Sn650-wqtpp3nq9ypCBTRCwzakZVhijiPRSZtc0D-auixEPZUZ0iP8bdkhoOUxrAFEKeNiTwQ80XyJIuLjV6dUcAdIcHLONi28nhk3gJsy6ga-oM6plzi3-Q2ST19YXDtpdBWEPSDBbCng2d162_Os12SL9TonpE9vXbTDTJUWEl5lrl42o3_WlwryrzINISoP6UYTz4uvyAqImMry4-xn4CiRfq29GkV9M8OY_1fOdbHPX-ec_2b6QjSKt1D2rT74U8VJ0WA6UPtiNenPSsb3LHPew_xk4af5Q04_qRK7ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=BDpmdHLGjbuAwp2PBpr4W0JfK7fyY-kDBXRCs9TCLndN7e9K64QlCioXP0wFB-yyDyWXa36FknF3DK4ePcXwCnveg2-ylCoutEct_s8e0a0e2giQYxhG3Yf7ek16kz88SFvrm467xo4BEcr8onC-D8gtgaN3fc_l7qVxPEtkGw-aMD3Jj8ElOzK16bB7fkTo6lsKp9Rv78kutbjcWJyEZzxmGmfbYEmI9Nx4bptQTRwYM5ZfQpPU4CE_hkYU_fqE4dQ05wKaoXRXcsLF4U0I5SVe_sfRMu0CNO5RGeBqVDif57AazuJzHmsAGzTOimYDwK0MnfyG6LsgBBqf52mqQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=BDpmdHLGjbuAwp2PBpr4W0JfK7fyY-kDBXRCs9TCLndN7e9K64QlCioXP0wFB-yyDyWXa36FknF3DK4ePcXwCnveg2-ylCoutEct_s8e0a0e2giQYxhG3Yf7ek16kz88SFvrm467xo4BEcr8onC-D8gtgaN3fc_l7qVxPEtkGw-aMD3Jj8ElOzK16bB7fkTo6lsKp9Rv78kutbjcWJyEZzxmGmfbYEmI9Nx4bptQTRwYM5ZfQpPU4CE_hkYU_fqE4dQ05wKaoXRXcsLF4U0I5SVe_sfRMu0CNO5RGeBqVDif57AazuJzHmsAGzTOimYDwK0MnfyG6LsgBBqf52mqQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=l-0vwlzjtaP4JG0BmDT26rzy1PKPiDbgs_NSYLkmCSJvvqDKy75Qg91-nmKQ-65cX4LMc_f357vnxzN1RUA_2abxpJFnJqlkhWO8mF4i6RBHYsuDXy5gGxgHJ0ZO22SsKmLyzaGgb5ihylGaKCmIFtAqnW6lo47L_-bwE5Lu0Ef28HHazrweA5q__2iOGyOxr7JxhD8JL0Eu6xLuzPpJGR8nNakH55nZK9x6aQwdVRUXeyxrTjT4gm8lftFYAx1_iifPYrgcxqjsV4VUYRHjjYGgWlRx_AQsOSB6c83cUkaxE8_rK7madSdA1AuJxX51EaxmeRxDvqash-xyqfXI2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=l-0vwlzjtaP4JG0BmDT26rzy1PKPiDbgs_NSYLkmCSJvvqDKy75Qg91-nmKQ-65cX4LMc_f357vnxzN1RUA_2abxpJFnJqlkhWO8mF4i6RBHYsuDXy5gGxgHJ0ZO22SsKmLyzaGgb5ihylGaKCmIFtAqnW6lo47L_-bwE5Lu0Ef28HHazrweA5q__2iOGyOxr7JxhD8JL0Eu6xLuzPpJGR8nNakH55nZK9x6aQwdVRUXeyxrTjT4gm8lftFYAx1_iifPYrgcxqjsV4VUYRHjjYGgWlRx_AQsOSB6c83cUkaxE8_rK7madSdA1AuJxX51EaxmeRxDvqash-xyqfXI2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=BUGVvsPs4ObaNg7ipcBiMxjnQM3EUUWEZKHOp2dbcwPQ2LbZZ4TRp4MtJs0_Vjc-e5XXPCb00Un1tLZDewDowiRlgg4BvbClYM01Q4Fzxjq0MhwMAIvE3ck0pYGmwuuyjS6LD6TmGczuLQ2pYiEpbcaucwMevmlDil8aY0gaEXfditYplyk0ZjjCGYDeaBbt8vZDLE9J4H3fRA44I9bstadDmnRC7UJ19iORB73yvwfuCK0LHUwikJq754c6R15IyF7luodDkCjwr4jPYvo7tf3voK6Z7_7Vc32O03AWgZRSqwTL764HyqbAizWIyVrElTlZrFfXD8amcGYDus5YHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=BUGVvsPs4ObaNg7ipcBiMxjnQM3EUUWEZKHOp2dbcwPQ2LbZZ4TRp4MtJs0_Vjc-e5XXPCb00Un1tLZDewDowiRlgg4BvbClYM01Q4Fzxjq0MhwMAIvE3ck0pYGmwuuyjS6LD6TmGczuLQ2pYiEpbcaucwMevmlDil8aY0gaEXfditYplyk0ZjjCGYDeaBbt8vZDLE9J4H3fRA44I9bstadDmnRC7UJ19iORB73yvwfuCK0LHUwikJq754c6R15IyF7luodDkCjwr4jPYvo7tf3voK6Z7_7Vc32O03AWgZRSqwTL764HyqbAizWIyVrElTlZrFfXD8amcGYDus5YHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=VR55SREhCVZD8Ttw5JEMAIADJoweoo1cYKhO6_jlOfh7CjVqb3G1GX0aS-ItVrfjie2Yw8P0NDfke_LfpsORfbrLW_jzQ4ZCCM2U7pqzl26ZD2f4N_sP6vbrou8ejnHtjYaDd1qEN39fIGP0tKPkDg9p5wlVjebZECS5CQOR_zuYW80_YCg1eXRYnf_bLf8meyfGGKVoaXERq7Rz6piCvLhBevaeWQ2IDard2AfLhW4tBdJXbhuYC1yeniiBXq_9J7CLUPgLTNEcamoKgv0A1oaKn4arVswfJdW2d8t70hHQ-9UBa2zuBSmKhZl-nlBKv8Ejk9Okh_b4TvgwQpdSKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=VR55SREhCVZD8Ttw5JEMAIADJoweoo1cYKhO6_jlOfh7CjVqb3G1GX0aS-ItVrfjie2Yw8P0NDfke_LfpsORfbrLW_jzQ4ZCCM2U7pqzl26ZD2f4N_sP6vbrou8ejnHtjYaDd1qEN39fIGP0tKPkDg9p5wlVjebZECS5CQOR_zuYW80_YCg1eXRYnf_bLf8meyfGGKVoaXERq7Rz6piCvLhBevaeWQ2IDard2AfLhW4tBdJXbhuYC1yeniiBXq_9J7CLUPgLTNEcamoKgv0A1oaKn4arVswfJdW2d8t70hHQ-9UBa2zuBSmKhZl-nlBKv8Ejk9Okh_b4TvgwQpdSKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2s76Wq0N8ao2RFE5DO9wiOdfXE-xdO3RP60lhAZFN3jrtQwXXWoz6Hp4VRQUouElQFJ8-RBtD3AvHusqDHbZJr5PL87xD_b-X51tSuiuF_dmvCFMe0gtBx5lKMwFi1hRuMZNgpVxLl68gsCFTETAwb1rydUxtEDKlnQlughmuwwnDfw6y4GRg_u8qyGXDVRcnp8eOdQGpZpiauXABYtARXbJQfQ0-ai3Mim3wjn7AEXmNKrVrh3GqpWkfH0pb6eJi6K6k-U91g8llr5T9XWqVAqo3FABxQbQeWRuWtBHNn0gsx_8jhKI2XK2DP2rJa6T2Y-CijywrUceaMLtZTOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=nmk9Me1viuK8vI2L4ALQekIGaTuRNTJ1L9nI5Gapmfm6fkS7eXx4NuxEfvK5qbLDIAPvW0CBWigmjPcDb0djQvbwXnVzXtCdsxO-d5pkguQC8gHZ-1LvqG7F3FwFjAQM9L17N7X8ex9Q7gKbCVOAvuxg0OgS5HEY9zRy95DRRcPGFVTtyb5yLtLVXJBfXTPCn2WC-OF7s_vgFet9I1JV78FOCERBMyNM9xns--dDOoRW7RoypfP7KQQZRhWKv52797DSeRnCWpL9Xk1c0-nYj34tw-ZTD3f4c9TshosjkF8ZXj2PK8_1Em52P3EuYRy4bTs9IwM-rqez8UNTxU4CYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=nmk9Me1viuK8vI2L4ALQekIGaTuRNTJ1L9nI5Gapmfm6fkS7eXx4NuxEfvK5qbLDIAPvW0CBWigmjPcDb0djQvbwXnVzXtCdsxO-d5pkguQC8gHZ-1LvqG7F3FwFjAQM9L17N7X8ex9Q7gKbCVOAvuxg0OgS5HEY9zRy95DRRcPGFVTtyb5yLtLVXJBfXTPCn2WC-OF7s_vgFet9I1JV78FOCERBMyNM9xns--dDOoRW7RoypfP7KQQZRhWKv52797DSeRnCWpL9Xk1c0-nYj34tw-ZTD3f4c9TshosjkF8ZXj2PK8_1Em52P3EuYRy4bTs9IwM-rqez8UNTxU4CYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=YvwkcFBvSJXt7bB5fj8z3gm_Aj9B8LVhhyLGaZNe-8V4vBRFqyhlfy9DhxSHzXUVtfjcFvU6mf9-NBFa8l-vyXhjgwhO63sqNvl43fJsHU79gwMaF_nOUJkUHH8iEkOu0JyEk6oACatcig2SYB_OHGNo4118b5NaLuOKFztqb-sGCvdgh6yW3Xous40tiZLv9B1sm2xwBEH4zi6gmjvLGKro8SHvQUUjP74XDDb7iAvyAO-nS-lRefOmKjstrt9Hi0LiH5i4f1hWJe9-N9xRoiAnjFgU_G5LA29M5uHWTJWbSC5rpPc5CgmFNxjf_8mz5i-_YFbv-SXFOVNU9PTmdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=YvwkcFBvSJXt7bB5fj8z3gm_Aj9B8LVhhyLGaZNe-8V4vBRFqyhlfy9DhxSHzXUVtfjcFvU6mf9-NBFa8l-vyXhjgwhO63sqNvl43fJsHU79gwMaF_nOUJkUHH8iEkOu0JyEk6oACatcig2SYB_OHGNo4118b5NaLuOKFztqb-sGCvdgh6yW3Xous40tiZLv9B1sm2xwBEH4zi6gmjvLGKro8SHvQUUjP74XDDb7iAvyAO-nS-lRefOmKjstrt9Hi0LiH5i4f1hWJe9-N9xRoiAnjFgU_G5LA29M5uHWTJWbSC5rpPc5CgmFNxjf_8mz5i-_YFbv-SXFOVNU9PTmdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=DdeqEdHOkqs-ibIrzN4OxrPC4HIQhSoIgSSSppD7Za5ZAYulfhd_fp0nPnaeO-SL30iHCEzrMhqD5-WB5Bc5daKi0fiKlw6yqHL1Ir5k-FFYHSnp9ziu-T1IcIdHHP_8mFrk_8mSGYOslTz9sAL8hw96CLbp2SfzigQROSXcd-r4Fh2V5u5krbGGGyHX0ET2x6na2KhjKZylvnxjPW1hy_YLnQfGhwPpRnLEWdInP-_nPFEKJwcWXhXV1z7Kq-d_OiCE7PwEE2LZSP6hEVc6qW6N_BnYZAnZx_FZqO7NRVt_eqTAe2vb4I55vdJd3QrU1biakifhnBi6-_ZWnM-MHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=DdeqEdHOkqs-ibIrzN4OxrPC4HIQhSoIgSSSppD7Za5ZAYulfhd_fp0nPnaeO-SL30iHCEzrMhqD5-WB5Bc5daKi0fiKlw6yqHL1Ir5k-FFYHSnp9ziu-T1IcIdHHP_8mFrk_8mSGYOslTz9sAL8hw96CLbp2SfzigQROSXcd-r4Fh2V5u5krbGGGyHX0ET2x6na2KhjKZylvnxjPW1hy_YLnQfGhwPpRnLEWdInP-_nPFEKJwcWXhXV1z7Kq-d_OiCE7PwEE2LZSP6hEVc6qW6N_BnYZAnZx_FZqO7NRVt_eqTAe2vb4I55vdJd3QrU1biakifhnBi6-_ZWnM-MHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=hu9RlYGckvT8_f7-HkCdCt7mTmBzpurhHvWlcg7vdTxUYlJ418XzYCMEbh7GcBWwE5IyXL7vSNLUMlmAqx2kNrldOB3I1YcI5z32wdR1oIC0UbsI-ZXlD6ryofaMlrzm6Q2zZGnNNWuyMgT1_PrVy0xrn9s0IPF6BSyzNncQ31t4sD7Hi3RkGXUcY68Rr0HEv5xOkIjDaIhqogMvotbY-jtJ-pHpZUMVhB7OvoUlHlDUYe8vy_lPQUhHBMK1bt8STZ4-VytC-v7uhCIQhEr1pHABn-2qj34-ZxTq5DDrEnb9ba1Vr1MmRzHfYLJ6w7A5-yQv9kMfs1cwTOHcV9CkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=hu9RlYGckvT8_f7-HkCdCt7mTmBzpurhHvWlcg7vdTxUYlJ418XzYCMEbh7GcBWwE5IyXL7vSNLUMlmAqx2kNrldOB3I1YcI5z32wdR1oIC0UbsI-ZXlD6ryofaMlrzm6Q2zZGnNNWuyMgT1_PrVy0xrn9s0IPF6BSyzNncQ31t4sD7Hi3RkGXUcY68Rr0HEv5xOkIjDaIhqogMvotbY-jtJ-pHpZUMVhB7OvoUlHlDUYe8vy_lPQUhHBMK1bt8STZ4-VytC-v7uhCIQhEr1pHABn-2qj34-ZxTq5DDrEnb9ba1Vr1MmRzHfYLJ6w7A5-yQv9kMfs1cwTOHcV9CkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=dcC_WXC7ISO06LttaVl7tSr0DNvw8sOjbJv91Mh8llVMUTmO2XXJQNllOm2X6mq5V03wBLlm-vkGEokVtON2zUZlLlCd_UYUeHuOHK0RMIodEwP5EDACWa-IjfOYrZAhrlaIS9f8mfkpmrJlK67X4mfxk00KQV4rjK7e7HtpHfIqjkV0RCvthGg7-3glexuqnyHXN-cxlijCxS2EJAt9dHoTJXEvAL8LSoPBCwEfwjhXLpuKg_mnF_O-urt1g0q3waaKFiEeVx1wIS0idopCcwc1LNicU0gmmqLosQkoS1L3v5RTZHVLU79TNUyAmbBFs8pkc8zJb7FPyCavlGiF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=dcC_WXC7ISO06LttaVl7tSr0DNvw8sOjbJv91Mh8llVMUTmO2XXJQNllOm2X6mq5V03wBLlm-vkGEokVtON2zUZlLlCd_UYUeHuOHK0RMIodEwP5EDACWa-IjfOYrZAhrlaIS9f8mfkpmrJlK67X4mfxk00KQV4rjK7e7HtpHfIqjkV0RCvthGg7-3glexuqnyHXN-cxlijCxS2EJAt9dHoTJXEvAL8LSoPBCwEfwjhXLpuKg_mnF_O-urt1g0q3waaKFiEeVx1wIS0idopCcwc1LNicU0gmmqLosQkoS1L3v5RTZHVLU79TNUyAmbBFs8pkc8zJb7FPyCavlGiF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=sWSd7bRc95n9h2DUUf_JsR-sCH-nKQB0MU0Nv7peyZGv27Snvu7wh8-2ohu_WBNPrA1kg65CrzO9GmEqTCnpwzVPTFMEK2icB-5BBS6K8Mmlt8dMkLOcJ417cRLXujqPGrn8153qARMSIRygv_B3XkbhVIy5DtCUSLVkT2x2iNzchtj2gqbyMLWwm3Zkbut1b41n7Ms24hesvMvbH_87gvtNeE_vk9T-BsIzR1TpLqjaDo9QzybDDgsZrKXHQbgNlVCiTXBSg5NLoxwwFT9PEACtAKRqp3S63RrX6TmSgaiwW3Ngjooudk95ys5ZOdVNcQ2N5pCR8V83GCn0TvjGLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=sWSd7bRc95n9h2DUUf_JsR-sCH-nKQB0MU0Nv7peyZGv27Snvu7wh8-2ohu_WBNPrA1kg65CrzO9GmEqTCnpwzVPTFMEK2icB-5BBS6K8Mmlt8dMkLOcJ417cRLXujqPGrn8153qARMSIRygv_B3XkbhVIy5DtCUSLVkT2x2iNzchtj2gqbyMLWwm3Zkbut1b41n7Ms24hesvMvbH_87gvtNeE_vk9T-BsIzR1TpLqjaDo9QzybDDgsZrKXHQbgNlVCiTXBSg5NLoxwwFT9PEACtAKRqp3S63RrX6TmSgaiwW3Ngjooudk95ys5ZOdVNcQ2N5pCR8V83GCn0TvjGLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=magyiOr60gZ8hYm6QFmU8ionBJ2iDE8AOqkD14dzynWy_NxhehsFZfOs9C3v9ujOLjRD34B7G8-4-4yXrlv-4qwtBLYpiRVECfvskkw0ENcmioWSGv-c2yv7m5comE07xwFBKsKRsTjZ-gej0uxoAfJcb2pjEB105qdHQPNKXZxpVGKSvZCSY5qoh1CGxbtsPoWi3q3RXr_Whj60toxRuEYuxyyjj_pER4pQYAcBD8qKaP-6XN_dmZDKRr_LZd56oacv4aYhS1YCpQpvVfjH3ydQ5vT2NKZvaDKZ2KREVFEG6vP8QUYaDs4QvI9tKpynxFx1eMn0qGs_NKknXmHKog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=magyiOr60gZ8hYm6QFmU8ionBJ2iDE8AOqkD14dzynWy_NxhehsFZfOs9C3v9ujOLjRD34B7G8-4-4yXrlv-4qwtBLYpiRVECfvskkw0ENcmioWSGv-c2yv7m5comE07xwFBKsKRsTjZ-gej0uxoAfJcb2pjEB105qdHQPNKXZxpVGKSvZCSY5qoh1CGxbtsPoWi3q3RXr_Whj60toxRuEYuxyyjj_pER4pQYAcBD8qKaP-6XN_dmZDKRr_LZd56oacv4aYhS1YCpQpvVfjH3ydQ5vT2NKZvaDKZ2KREVFEG6vP8QUYaDs4QvI9tKpynxFx1eMn0qGs_NKknXmHKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=s8Yn-D8lFczz-SFyM8HOCB4LlbB3Q-KtsrB3EpD37gU26TkZelbQY5O3-BKEk0I5F7Wb-oBiVbozIa7nrS3DuLT_afg7__WakO4mmoWTmA4ZyS7kWiPgYa-UM7qOkxY4r7aD36qUary-RgjRneXYlB7ariMWbxuXQDghfTaEUwn_c4KfNtGxp1niX80G4VSVHuHsSW84rxHTFpjXaLkyl1RC0vQB1xX8a_hlPjYxN7GDxl5s2cx3Vv8sDFt1tA4kxFEIdCT7J9GB3Os9ap_0VlC65nzZDvLqxBiUYIfMfF2HoLje90OZSSybX7ab7ISHeSXqsUqmikHcks--I0AJu0zUwF4UpAZdCBLhWy4nvxMh6l7SIMPx99mS_avvVBNE-VsPSrgz6hdgBEoWiFWEqQ8M4BACg7XLHo15srV3B00EDUtm0hU4TTqzo9lXMEFFiAdCTerWlaWdVmekSctyv2vp5MWwPkxs5s4C2QEcCW-IZBJ-4oI-ov2vWeD2LvtyF8ft5f8mtkATC8xdt3EPYXCQmz-WQ52Up5D7A9GF7gVVrmuiC9wYIL0bgOrDP2FrNSD1rc5AI2uIzQvNVhIMg2psqMQBImTxZSqHQghmBXS2J1VYKRUzycAqxlxb-KsLoi-fPy54fo4IS7CK9Uy3zPWc9h-VxDyrgI04ONDMWy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=s8Yn-D8lFczz-SFyM8HOCB4LlbB3Q-KtsrB3EpD37gU26TkZelbQY5O3-BKEk0I5F7Wb-oBiVbozIa7nrS3DuLT_afg7__WakO4mmoWTmA4ZyS7kWiPgYa-UM7qOkxY4r7aD36qUary-RgjRneXYlB7ariMWbxuXQDghfTaEUwn_c4KfNtGxp1niX80G4VSVHuHsSW84rxHTFpjXaLkyl1RC0vQB1xX8a_hlPjYxN7GDxl5s2cx3Vv8sDFt1tA4kxFEIdCT7J9GB3Os9ap_0VlC65nzZDvLqxBiUYIfMfF2HoLje90OZSSybX7ab7ISHeSXqsUqmikHcks--I0AJu0zUwF4UpAZdCBLhWy4nvxMh6l7SIMPx99mS_avvVBNE-VsPSrgz6hdgBEoWiFWEqQ8M4BACg7XLHo15srV3B00EDUtm0hU4TTqzo9lXMEFFiAdCTerWlaWdVmekSctyv2vp5MWwPkxs5s4C2QEcCW-IZBJ-4oI-ov2vWeD2LvtyF8ft5f8mtkATC8xdt3EPYXCQmz-WQ52Up5D7A9GF7gVVrmuiC9wYIL0bgOrDP2FrNSD1rc5AI2uIzQvNVhIMg2psqMQBImTxZSqHQghmBXS2J1VYKRUzycAqxlxb-KsLoi-fPy54fo4IS7CK9Uy3zPWc9h-VxDyrgI04ONDMWy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=bBUTOPiX_jHPDyyFXGzaF9ll9Dwl1V2MTaSfmN9n2jE_U3xpyM7yAWoRbVmJRGaQvUIz_hR32CW8w2WyLLqUe6RLPIGTxwS4hN1xx810Y8Lr8wCTU75IxV4kouixgZzD5YhTcSXAbMq0je58ACmyQfaV3IGLhbdeqk9u-62unV2uTkq7OmlSdU0MmVX0Vk-Y8YnSz34RJoNjUqxwmMsf1n4uCn5WeKjAEvEQ5M3RR_gEbguXZB1qoBYYNFN1AMz6GAIGJdMg3LeZs7A77wepRKLlrXiAwYVDsVQfKfn7nOJ3ds3n_vQIeftCuNSo-s8kIz2iJODELkKC44hk6QZzew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=bBUTOPiX_jHPDyyFXGzaF9ll9Dwl1V2MTaSfmN9n2jE_U3xpyM7yAWoRbVmJRGaQvUIz_hR32CW8w2WyLLqUe6RLPIGTxwS4hN1xx810Y8Lr8wCTU75IxV4kouixgZzD5YhTcSXAbMq0je58ACmyQfaV3IGLhbdeqk9u-62unV2uTkq7OmlSdU0MmVX0Vk-Y8YnSz34RJoNjUqxwmMsf1n4uCn5WeKjAEvEQ5M3RR_gEbguXZB1qoBYYNFN1AMz6GAIGJdMg3LeZs7A77wepRKLlrXiAwYVDsVQfKfn7nOJ3ds3n_vQIeftCuNSo-s8kIz2iJODELkKC44hk6QZzew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=lgXZNjrK_xep0RmDSyAmhl-MM4S1VSIrf7X-1-fxbN9f0U9sPo-HPva5AAi00mTrUzzcLJRxb0ftDTrM8qd9HhPcKkKp1ZC8et2Y4DQYjpmIM0JaQUOfsiCTzfv42Zi0Z5Lj0ovOKXok-NjRNKme4KtKNvlrU46H28admABiXdOlLtBuptlA3nE6DyAZs9P-CX30W7MmL2YKbXz2xIBhUX7BkDE2d6JFdDu2MdcNHNcEzz93UAbWvDVNxqRU-yxpEkv1sxBxAcW_MBgG1gE9w_WooV2ddeUq-DKKpHmpdzdvlICibZwhlvcGoZV8TtzB09adyTRsM83JwtDBxwMJaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=lgXZNjrK_xep0RmDSyAmhl-MM4S1VSIrf7X-1-fxbN9f0U9sPo-HPva5AAi00mTrUzzcLJRxb0ftDTrM8qd9HhPcKkKp1ZC8et2Y4DQYjpmIM0JaQUOfsiCTzfv42Zi0Z5Lj0ovOKXok-NjRNKme4KtKNvlrU46H28admABiXdOlLtBuptlA3nE6DyAZs9P-CX30W7MmL2YKbXz2xIBhUX7BkDE2d6JFdDu2MdcNHNcEzz93UAbWvDVNxqRU-yxpEkv1sxBxAcW_MBgG1gE9w_WooV2ddeUq-DKKpHmpdzdvlICibZwhlvcGoZV8TtzB09adyTRsM83JwtDBxwMJaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=H-Iq7n6puZBNlU-VzIKrfi_BEDvUT-zsP-UHerL9GN6dJTxtJQFLSgz9QDOipX69d_aXDqUK5ZmKB66GCqeJfQvT6gjcfSNKdPF3WbyrR-Fccn_GDPSJzLnzM3N9XN8I7EmCcKoWY_b4oH_qLYRYKfvhybsNo-r6_zQLIp4yFKL2wnN4tQk-We8jQ3hi7p_emkLGUDmR89nJOUBWQXWREXPDaLRESlhIbWEcsJjUyATfuS1LmMO039ItOBzsmbo1Frvdl-pJtR2cvJJcdxiMGkUFD1gZThdfEV1E9RTdc0zAcTAJb8StmXYH3vnrAi4f_tzwIQli3JpPSiB4fvnOhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=H-Iq7n6puZBNlU-VzIKrfi_BEDvUT-zsP-UHerL9GN6dJTxtJQFLSgz9QDOipX69d_aXDqUK5ZmKB66GCqeJfQvT6gjcfSNKdPF3WbyrR-Fccn_GDPSJzLnzM3N9XN8I7EmCcKoWY_b4oH_qLYRYKfvhybsNo-r6_zQLIp4yFKL2wnN4tQk-We8jQ3hi7p_emkLGUDmR89nJOUBWQXWREXPDaLRESlhIbWEcsJjUyATfuS1LmMO039ItOBzsmbo1Frvdl-pJtR2cvJJcdxiMGkUFD1gZThdfEV1E9RTdc0zAcTAJb8StmXYH3vnrAi4f_tzwIQli3JpPSiB4fvnOhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=qWihbmQj9hV0NfU-vGt5UknribgbK2q3UAglh4OVop9FHRE9zn81s1qHr3Z4knO8N5VbEmCaNs7txSZRiUgpJhwm-7_M9CNgvrm1KZmaFR8L7C1sXI2I8fSeaDv-lkB4d017m50Sp9LVqsntT4JM3XjQ-FHJBKq5C-CmgZKUfVShj-C4mSY3MrQTTHHoVjGCGfk8pcKTt9tP2jS2QFBRSYKONqV2bKZqIEf1IYHwT-Ppv2mqvuf1Cn7MhJp9aC-47QaSFbbo9C2POmSt-tTSTEnfjYPb3LXNF4dnGbqFMwKTU54_KbAx94Kdi3EljlDcKFhpo80h9FJgFSSXZ1TPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=qWihbmQj9hV0NfU-vGt5UknribgbK2q3UAglh4OVop9FHRE9zn81s1qHr3Z4knO8N5VbEmCaNs7txSZRiUgpJhwm-7_M9CNgvrm1KZmaFR8L7C1sXI2I8fSeaDv-lkB4d017m50Sp9LVqsntT4JM3XjQ-FHJBKq5C-CmgZKUfVShj-C4mSY3MrQTTHHoVjGCGfk8pcKTt9tP2jS2QFBRSYKONqV2bKZqIEf1IYHwT-Ppv2mqvuf1Cn7MhJp9aC-47QaSFbbo9C2POmSt-tTSTEnfjYPb3LXNF4dnGbqFMwKTU54_KbAx94Kdi3EljlDcKFhpo80h9FJgFSSXZ1TPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=U_LBrIs_2QvRu1JtQ93TpwPyjNOIJSbObJN4TyTbXJBn0ZoRrCLw97rc5h7V4O0eFw8tFZWLRKRFo27tmP-UjYk0WBebKE6-MFsl3QxOKNnzL2ntv0bB9Ab72gtU-jZoimzlVA7XufHFvFn-Q0oOqS8uEyaJkpALresrJD_q32LV7nBpJXYMJ1XmYlmS14tJbrAg_yUuHaSEd88PV7FNwCoN74OFz5c_SAsHUskPLZ5YRnqM3JbL0ZJ1SSd5U-Ve-7_abLzlC3vhAH6To2aSmY5XgFhDzDgX43Td-u6CktACtjg36M13omt0_Wp27LN72BW21y5VUZF3saUXJE9-cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=U_LBrIs_2QvRu1JtQ93TpwPyjNOIJSbObJN4TyTbXJBn0ZoRrCLw97rc5h7V4O0eFw8tFZWLRKRFo27tmP-UjYk0WBebKE6-MFsl3QxOKNnzL2ntv0bB9Ab72gtU-jZoimzlVA7XufHFvFn-Q0oOqS8uEyaJkpALresrJD_q32LV7nBpJXYMJ1XmYlmS14tJbrAg_yUuHaSEd88PV7FNwCoN74OFz5c_SAsHUskPLZ5YRnqM3JbL0ZJ1SSd5U-Ve-7_abLzlC3vhAH6To2aSmY5XgFhDzDgX43Td-u6CktACtjg36M13omt0_Wp27LN72BW21y5VUZF3saUXJE9-cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFIAA9rzMVQgJDEih4LBlerLmPsah_TWCglqVv3GWklyiPGijojY0ydxfncjbxrJ6A45_gZG9go0vIxrpnqBOxOzbH-3lv2qNRTN6272R-0x-k-eP3qNonhyV18ZUDM5WYI5ZFUUzsGp7T-ajjaAW5AwwULPxGR5Al7cvbEWR3Zg2kXSlUecytIvVYGWyvEuyDIkLheHYzGGIE_KU768C4R9m7sjyBly6yPFZWn7M0cO7wWrjHak1OXlhHZpKxnEMK51eJn9l2PJsybc8nENPvx7MMWKyms249Q47oWzSgepfKoFDlXJ7cYWbluldQpZXbdsFG0ucsXPlMM0qzaQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
