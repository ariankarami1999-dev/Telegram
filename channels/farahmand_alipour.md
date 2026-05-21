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
<img src="https://cdn4.telesco.pe/file/Bqts-PwZnxJ9QlbJ67L8oIDIo2vRmJD05MP6hwYgUE37HQAyNQ2j4wUIg2bPK78xgIBooHyrV0UBcjLMEq99moXcP2574sWykJ-4Q5XHmWjU1bWsqZskCbSEpGZRVd_L5je93S5pbfg49b-SDxoy6yilrCBqChw-EUjeSAUFIeWTb6AdR9ViNyTQy8qHd9ImhN-M3EJ1IAUZ0M0Ri8PTEAaxMcbOJRUkYwpRBHH8rIEFQGrn1UUa9Y_wnwEm1K2hVB2af_vhSIjOE4oUczZxmozppS7UZe0F1xOHZ8FeHK12aflg5pAowqTyEPitzDX8W-J-d8TkN5VOYevgC-TZZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 14:03:13</div>
<hr>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8fuiwl9SurRB_3zT4JZT56EJvvFoFy3q9ChJf1Pu__vtXqs05Esp1HZxrWkuT1j2wZZJfGsoo6YoBeFdBINpAZbyfhY3q7ZxeMzs3JYRDtgQ8mXewdgUDSVgGvxKqCkQ4u4Na1B9xArpK63m0BswcwavfMLyh4AFdQQ24LUL6Jjcf9TMJ-Wz51tSTztXUfHsFiY1-Y2DEsNxU4SZetF9D6nX4gWLes_fVclwDfCyMUoZce-DY6nYsX6rZF1Tb-p-vQ3iaCqeAEiNgjIaw7raprW4fce_bzDp499DTJREtJzPKXooBrjrYvaee2B-eci79ZJ_8LQQ_ZcJmFXajLHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6e80wzT9j9TOTj_9CSMgFXs3zL-KqGB-0SU29efo2HDop4HRm3QsDRlOFzK3my0B-Od6BLOo1dgU4Ch4VE_Li9ksYAQRDa8734iLCTw3LM5xu23w6WvgROpQC8RGSO2BKKVXGCyosisphONyhYzwfU-YTChfBQFhHsHCmv6B_M3uwVsEWzF2plL4fb3JYqfd6pOkYnBZr9lpG8oTjnVjK5KL6rpcNCs9kAzE_h5YqMAIMlO-PVPhavnEhCBZCnVNkX7Xik2TS3Hn2kIhavRKnsWzNkqa78Auc2CECRao1nATnK-CCr0gtCVt-XXmIt-euvrm8M7WJTZ76e9MBn5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1iwg92upy5UfaJRVxU6qfOzIRtdnYdX-ZnbHhd0m8TFTweKak0wbqNi7EP9mQj6iXINA01pItR7jkXZXl3afaPrEmfk9-m_8dK7CzyMWz6Fg3H6o2g_PKdgCdYnFjraoJr3LuOyvH-cKCuPdaC0z0vBgkKfRC_MbjM-B1nNjzehkHjhXmei4U7jgOG82oqzjJKfPtYAo6kFqe7nWlKM4tY1ma9f8zLS82KxT6WM1V3ln_R-1DsyJ15o-YgTjbSWfaUbo57TV__7CcdDKXtLMtQnV-wj2UqXJ9g_r9ACUymg-W7p274nppjHswIGArTJ9r_-HkLfJOaplNaL7KbbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUNOsJbXPFG7H-EisUNfekXVutEgiYAJBSPaCxFK8kBaBxqpZMg01-aTh-gHG1Pf-1AgxR8oUvpa3mcqATqproUmUokMd0oMjRfZwuqTVo48oozkeBtQxChg2qfKygB-Q3BxjF5kYYTqcBsNFB5ZnlJg5e5a9nt7TfuCundlqyCn5o0R1qBO8W5N3NoyrZPev3libRQ1MIJ6j0gVztZvhcZVEJXSYyKJPsZJSL0EkumR6lufZ1z0FCxvvihP6aVBO1bCzdc8Ra9ODVjk7XGJ8BMAVWxjFnBIVbbs04UV_6AIRpWkP00HjGWHiAJl4js8QGrVOP6KSXRt33kXVccI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLX1C8ljrMnTRMmGioQUkd9mpbZ61FY1XQifzdzEHpZcyOyuwDVWlsbu0hqZdxZotflSG5sr36SZsXL0RKxSRdYcDe0E94v6PIc8t4rTVXmIkgBcdqmnS4LeA_u3TkdwAJXTN3fF98WxUdXBJ4r-rDerRmOUTpaUcj7-hztn7IZ5FQNDktSJ0iyYleYLBBnBLWNVbqIE1L5x7MCbe3s1ZgNkJSgHeyyaHNpz_33lvHlqisQ-dwHdi0krhHQMXy7RYw4FTt5oYA1LmOvA8vRlxuGp7wrqKNOKn2kl6QcSdljFLe-ZCYlbAoNj2qLKK3JTOHJc9B2bXV6ZdtXJgsOEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqdFlHv2uZB-J7MgoVBpyjZ2UHL6kwAlCkdFYl4EKmi0Nly2-QNzMGZJXpkOKLogwIqCfLK3GaK87oYsw4vhpgpdI_WHk9BB4KG2w01BivihXY55GOPSirxkrs39CLajUO81CcZYU3eSmKa40pi0ObaIgKZ79uYEj8xmdsBZNKXLr3r-B4ufjl71G_MHdaqnc3nowQMKyNE02h1ZvM5GjwYr3KdLzw09U4bfdVUuSarAhYORl9C1C0wHpBdyoRdYaxffFHo57Odzzr9oBeIpTYklUnruizHE8jYLzWtgVfH-SSgxzgMhcKxKJ74k7xr61aSMPwX5xcisFT1WEap0IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOTYsevyGtmFKtoqvpHrydIBgK23eh3YZGs-fl0vh51YZ8tAsYAdN3OEfcT0sDz1E1vHR-1I-TxK1ucHsbopdqh8OvER2Tt2KaynGQwqjhbfQUwtN4YBLueDh72yoGgc9sc73zNaxdCI6RGuiGknnzhUmAOGBX_xDq04-DyRi4qLUaLD6Tef2ANHs3u-FlF10PzCW8OkkToyFOmBRYTa4YMC5iQWrMUpdc_mc7IEZPcIlMd8uSrnEb5vJGSlA65gd6BGCcKGAXTnUu2elJTsdLKr0MPcCpdkcqYPpKzLnuO1s-6geN3PznYdj3ceIeHqRlrnnHdNyd3dKQ9dQmknxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=GeihqbxXuwEAUI9jgoLY03KEbZpdkqeI65tNDxSP74zUTz7ovGsBxH5OuVilvGSrGU6nEF1d9xy9NdXiemSu_oxe_Nhshtsycrc8xF6Ra34AECmzxRSOeT7iyUFhmBiwMrcRWno07jFWgchoIpcoigA8TR2XD63a8e-GZu2_a_jn-3c3Jmy_AjTQuhbS-pEm_JyfiE0Gkuu0C1iCojUWCjaGEIpRKWrVIEtEg4Gl8C3jTQNxW_0FZ2Iqk-pj-84bJcH_0afAhnJfd2obYbSZ_RLa9H7cqUeFftkioTTSbXEA8dgJc7pP88ekEycoSHDImZWxQdemRPLNfnVcfghCHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=GeihqbxXuwEAUI9jgoLY03KEbZpdkqeI65tNDxSP74zUTz7ovGsBxH5OuVilvGSrGU6nEF1d9xy9NdXiemSu_oxe_Nhshtsycrc8xF6Ra34AECmzxRSOeT7iyUFhmBiwMrcRWno07jFWgchoIpcoigA8TR2XD63a8e-GZu2_a_jn-3c3Jmy_AjTQuhbS-pEm_JyfiE0Gkuu0C1iCojUWCjaGEIpRKWrVIEtEg4Gl8C3jTQNxW_0FZ2Iqk-pj-84bJcH_0afAhnJfd2obYbSZ_RLa9H7cqUeFftkioTTSbXEA8dgJc7pP88ekEycoSHDImZWxQdemRPLNfnVcfghCHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=iLg3aorlcDRwlA3NrOOaMbQWz1sqmHg1nhrcsSXMf8PVhq8xz4s-xmLvxuEZTAQYkR9Im-qkSYdmAYY-WZRzhSqvaXt25tH5CjWtEvA_XDPtpfL8OSFXO3xDcBgoL8dOASBC_XLujQJy_hFaOOBB6LtlOb6NWTwIHiUIebYM8AGGA_ql_7iERk9ujyRcMhY7-xnEAzPUJb1Gte2smGA85Z5o0Tr7SXsjMkJazjlJRPYI6o0iTnQWbvFMS0Z-5NYOW3-FN1fWIeaNVOD9uAaPPieONusaxhBgHhMMsNVebEIcB7cziCGtm6uvIgEh7aRDNr9wy9Go1QZoCjgJwph9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=iLg3aorlcDRwlA3NrOOaMbQWz1sqmHg1nhrcsSXMf8PVhq8xz4s-xmLvxuEZTAQYkR9Im-qkSYdmAYY-WZRzhSqvaXt25tH5CjWtEvA_XDPtpfL8OSFXO3xDcBgoL8dOASBC_XLujQJy_hFaOOBB6LtlOb6NWTwIHiUIebYM8AGGA_ql_7iERk9ujyRcMhY7-xnEAzPUJb1Gte2smGA85Z5o0Tr7SXsjMkJazjlJRPYI6o0iTnQWbvFMS0Z-5NYOW3-FN1fWIeaNVOD9uAaPPieONusaxhBgHhMMsNVebEIcB7cziCGtm6uvIgEh7aRDNr9wy9Go1QZoCjgJwph9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=M2XJ-CFxXvdTufFAOfQYhlRxHmFxut-mysbLd5z6bYEi3YvmypNJJei2F4uGwJsmA2mpQZOYy2xyYGkZcLCEHsR7nK6i9GTqfSuS6qfYWFLaUOQAQwqTd5jAbPz-R5NvhsyNv6jKu6YjX-rA_tUsnLYKVu5BbQhldk3rWDLmOa6iH5F1D4I30GdNdCLKgaZfEChxNQvnB4mR0QeXqyx8sMT367j_wlftvsEjnFm3eCdTCjf9SIY8k8KbkDbtRdAdrZgrTcxnKXYCSoGYP56LhJCkU2l1WTeCQvRswoWmbqw-9f0w0Y-YCSjjXpHhSpKlPfbIA0FYPjDrSaJCFXZ2EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=M2XJ-CFxXvdTufFAOfQYhlRxHmFxut-mysbLd5z6bYEi3YvmypNJJei2F4uGwJsmA2mpQZOYy2xyYGkZcLCEHsR7nK6i9GTqfSuS6qfYWFLaUOQAQwqTd5jAbPz-R5NvhsyNv6jKu6YjX-rA_tUsnLYKVu5BbQhldk3rWDLmOa6iH5F1D4I30GdNdCLKgaZfEChxNQvnB4mR0QeXqyx8sMT367j_wlftvsEjnFm3eCdTCjf9SIY8k8KbkDbtRdAdrZgrTcxnKXYCSoGYP56LhJCkU2l1WTeCQvRswoWmbqw-9f0w0Y-YCSjjXpHhSpKlPfbIA0FYPjDrSaJCFXZ2EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rkskz-j4x3cRiKbTbaJyCtRUeRPGIeCeNrQ1Obnz3JVvkXpUbNkI-T_R59PmwohAwW5eYJbiy1bEhhkfbZJwEZmIY0eHhUV1Fl2YD1dGh8C9BaFABG3iSziU8k1Yergh8d7oz-ugdwsMuEKdX0dfpEmeBi69Xns-aLDMcr8rbK215B91_aO7ZnmewjYbTWqdcgYtC5_fHgWrXyeJ04hA2GQOtrKWRfr3KV66MKqygqKiwXjlCaVQNAaO07lw_VlgR3vzlyEL2sH59Ypqr6HfC9VULLxSSmaTeHhIOASjallhQ-DGZ53QgqyPECJkptIKXYoJfHFWmcELkYbdwPT0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=X-bE8Z5NK5ymRfbSigJSVBH_gDHuCOxbOe5tq8NsUjYBzdOjnjiboN5PEU-3xEJ6yT-E90mdVJc0JwOesTunZTPr-JUQpgcX8PEPEgQ75kjde2tN6EDH6B2rv2mbZ0nPSvS9goK20qiatn2-5W74BZhfizUQtFl3hytv037yzH4HZoAFt4tWuOk65qYesL8vnsRx8L-9ciHYf6tPtrvojHZSVAoN8d4pshxbW3L1rOUYwcNIELq1BW-YeZm6ENjAAG_rU-ANUSS46RXMM4xmmw-CwFZ4T1DLqAM2Ripvn-NkmvrWw9KFrQ-cEZwBbAWxDj53OeCP5ntJxz_Iwc1Q2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=X-bE8Z5NK5ymRfbSigJSVBH_gDHuCOxbOe5tq8NsUjYBzdOjnjiboN5PEU-3xEJ6yT-E90mdVJc0JwOesTunZTPr-JUQpgcX8PEPEgQ75kjde2tN6EDH6B2rv2mbZ0nPSvS9goK20qiatn2-5W74BZhfizUQtFl3hytv037yzH4HZoAFt4tWuOk65qYesL8vnsRx8L-9ciHYf6tPtrvojHZSVAoN8d4pshxbW3L1rOUYwcNIELq1BW-YeZm6ENjAAG_rU-ANUSS46RXMM4xmmw-CwFZ4T1DLqAM2Ripvn-NkmvrWw9KFrQ-cEZwBbAWxDj53OeCP5ntJxz_Iwc1Q2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=hE6U-cWVPxbSljVXkGPnAusHXe-NsIGjfyHO3kbNk5q8PqmasMPkwq2yuoqYcmbdxUeS9V6q3aj756bchTN-xWS52CkZWyz6LhD4a9FxdA5KnPDFCefKPCxHEybA4KKXGX0PsybxUowE_sN3LCZIPOKVMPcW7rIW92N8GRUipJlGZe-Q8DDQ9OuKmYy1L2o2biR0DkZJJWyLUFGaberYjeIRlK4mB_mAUimJR6-mOqwxyQfD13UjhtQP-ieIh9vW_-DOc8lpe2lZs_hxv3bZ31ZGtmHuQDxGxcJl0PKu_yft5ebatlLLpUKnpYSrKFRI3i1W2sn42okQhSrgh-ig1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=hE6U-cWVPxbSljVXkGPnAusHXe-NsIGjfyHO3kbNk5q8PqmasMPkwq2yuoqYcmbdxUeS9V6q3aj756bchTN-xWS52CkZWyz6LhD4a9FxdA5KnPDFCefKPCxHEybA4KKXGX0PsybxUowE_sN3LCZIPOKVMPcW7rIW92N8GRUipJlGZe-Q8DDQ9OuKmYy1L2o2biR0DkZJJWyLUFGaberYjeIRlK4mB_mAUimJR6-mOqwxyQfD13UjhtQP-ieIh9vW_-DOc8lpe2lZs_hxv3bZ31ZGtmHuQDxGxcJl0PKu_yft5ebatlLLpUKnpYSrKFRI3i1W2sn42okQhSrgh-ig1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkVkzyC_uRz7k4O9z7HFCLYPdU8GRwMxGMq71CuV2Mq1FMMpneLMpqm8pIJ5rFeugE5Y0RsPBuGr1EtR8Pto9BDB18r4lStNGhDuOcklYiI7qVnEQ5BG7XXFcUabOdYK1z625KXo-jabWy0VpSUxfqC8asJtthCwWRDYQSVBwZ8CxfAQlnYwkxFu5aamDZzgy3B6425krwk9waSE9b0C4euubzDrRPbNM8YobE_-gH-r9Lrb2cENUfyHB6oOrSxt2ZIl_ajYKyTN_XlYGzQUsGA9pC4s8PI1zoyLfzfVceSyn0z1T2K_wwu91lGBUuKjXZzgzOw46gj9iplJp187Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mojd_uSfnUIwgPDRcOr_UVtCA9PlKYVeaYLokT3u-y2zQt7PVO07R6OMQjOAvVFjSNUvr3ruJxJY1FnSzTrqnzML-3vSZjxk436zK4muaGBYxw7t68ICA0fHfPHnYAe4wCaDeXEmItOqMfnk4Zo2gND8SXZpye9gj9RsE6PWNNtxe6cLb_--lN9KVuZmUpH-QTRvjyZb7ytCY4g5Zubj83IU0hvBFcIiudKz67jrw_v4FkR3WX9pxSDgbZnm8RK0u-Y0dcXAk4__lNfxLA9EoziA3SF8OG6RGR8EUiR1lLgMIpYfAxIuiK2uMhd15W72iRpUyZvzXQYXgYJVfG9cwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaTgHig_NM_evYGn0jGMUSBAazx7GyzfV3b3Dxz43Mhk6RZOHKntsffD0-0RGJhkbkNApKz4JJnJFOa7uWpm3DhDrki5Cw6M0W7SaK8hx2xMVAioJkegTp8cTtnM6-XpKpzBwO5nK67s2Y1BpFqUMCyDqSyqVpnrINgjlj4bse-6ILsm_oEldiEZzWTwBQlplKw4vMVPpJbrRH6043UsJPNMebCRuYEKS6MTATEg0n3xwhtMnEHzqAxipWjy_dVLOqSwgma2YlgG6Ou4ZdGdDb0kcJbWFaNCUsdHxfEwhostvkkRQ3gOVoLvU8AYQUaXo0hoqQNHQKIZSjeEJ7Tcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGdevHg2Duarke-Ki2EdL56kZOyy1GnTL3STQKzYjUxRdLkRK5wcrdUV6UuVA4ZrH0LJVTJoOXHW8GT_zYoC7pCPshpIDekhDTid4n0tYP-sBJqJdX3dHR_25NiotOPdJ_We1bTYHgG1dkwSCQQES3noJiXINwqw6RCtqJbnAEOakW3TcI0o9ObUCsdrtogIOKdc6-zh9hNDXd8PknQVEqDYFzouIpjeR1pQ0SHSzjxPqM3Srhbebyo_eoRmDWyt_u6u6Vih0QefUOi9G_DP4IjKiSn4akx0b_GeiZsysBcvlo-lp1pwTqi9TMkWmWYO0yOmDmRG5d0wZs6UTooFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voSaj_XHIKxwXKJbpoqlkKABMHIp7dUoXyL8KEI_vpZ4w4BpVZc6NvGGQTiDM4pOq_8klvDzdOffnjzhThlDdrHMVEeBh7j-901QCtUarQzF3iSoox56DYltIOa4Zg168N9i9XPGDzBKFKvybYzq1Tw4WO9hqlV58r1h8jzFCILh1H_S49k_-mXffavVNqk3jUr7IgZ5s50QdPhxmKOz2tD7DPsVO17VxhBoroh54q8zqNnsjaEgkxlGCsnjxtH3UbrE2o8_3sCfwJjf6EBW0aYfX1J74eBh7z220UNwwdsj9z6Tjkqr4ajB3OfRBGP5ECcmp2GY3eiHfgaJmpvCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBgQrmWL3dcjgPvunfJESUJBXHAWC4jgyE66VH9xWa4zkH11tw5le-8zIn0zRiANKjGOZw5b-4GK5UaozjcDNlHQLALXSm_364AG_MZS8iUDyrhN-wE1cFR0USzBZn73eRDtBwcNX0zc2_s7b5GhuET3uGe9wO-8TBAMO4-03fZKtTdNMyInlmdkhUZ89XhsKOK7O_lhKJ7Y0pviQXLiDFIPejgfxo2YM16M-esEKJoC3RcpQOGqw0JaadyFmu1aLOIaahpPjLV-5ienWwSspI9ywTcAcjnBq9Y8pkllh0nhi7u6lI5igHhoe0CmunkPo-Bm0unCeoOTqMianM3EgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRBplwyQa4mkRVszeIGTApQA6mpApsl2BMLEJgFmPqzbHFTVDu0yYEc2PuU4-0buJ1ZA_u2XvUxF7gKkK_tBBdhjFySn2Cvrk_8dW2Uj7vv_cLTUlHsIVa_5UtEJok6OB-KWF2SOFig8f9ZS2VWmlhwC-TuO6dd0HiNaJczGqoyo0Wjq3C89zI0zl3YfrvqwpajDSO2KuLYsJGgioUlwk0IeWKpL2eAizaSepkhqtpnWDnuRGY1E3k6o-wNXMtiQgUVbsVtBGBYZGDLEGw7K83ezsIzqU8VjWGIRH9DogeLZ40bTpJRAGkx37SJLhAPK4Q4VQMizmUxHkGuESPdgUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=FPvQM9Ppfg8VpWgpcxPvAAD2G3OFSxx-zyQ866n_kH8zxuemggj6hZ-8pgEWr40VYJYhN9QzajxAh5Y0boawiEnFJCahfHod782iniN6Bphl72mxvT2kkge9ZF3FALgYHosbR3P3wZx1kvXR19a6E9ljXJwrQKAI6oVKnScCtJ03hBZ1RreDQz8k16QT4UAfro-SR5vSOynqf56bFUdnrfYYUgI-83cgiu9wgvuM7D84u7SMvSi_VtFlI7vzioJrOssCxGK0Agg93mYeGHRcNQfcNK4raIyrGaHbxl9Mi9gw9jnevR4TsFPp-kNmRkAroAW3QMzo3CS_r0Zu4Dx2tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=FPvQM9Ppfg8VpWgpcxPvAAD2G3OFSxx-zyQ866n_kH8zxuemggj6hZ-8pgEWr40VYJYhN9QzajxAh5Y0boawiEnFJCahfHod782iniN6Bphl72mxvT2kkge9ZF3FALgYHosbR3P3wZx1kvXR19a6E9ljXJwrQKAI6oVKnScCtJ03hBZ1RreDQz8k16QT4UAfro-SR5vSOynqf56bFUdnrfYYUgI-83cgiu9wgvuM7D84u7SMvSi_VtFlI7vzioJrOssCxGK0Agg93mYeGHRcNQfcNK4raIyrGaHbxl9Mi9gw9jnevR4TsFPp-kNmRkAroAW3QMzo3CS_r0Zu4Dx2tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEW1hzSVrainpPjRISZkwfBFxw1gtgmKEGpM8qPB2OUj1KF15suiMrvzuw8QPaw3t0GL78txQXSd7FElNJMsbtKLNVkHl9BUsowfd2krJne5WMVzdYiY5e5delR-lowIK5ZNSrj5N_ho6I9ephK4X5MxV38F9Si7-FqeSqngB30JG6GFmANsLJa-4z9pT_K0QK5uy2Qd643igKn4skCYWKM9GDuDedqSzTnzRwf53Uy6uKq3NcnecEEsZD8PcI2xFmZUDI5WGksNghi1gJmzphVvF5Uee44MDqRYF5TdmQdLH60m4_7l2RRddyvTzS2bMYG0y1C8ZEMY9dIFKbf5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEIzza4_9lXqdHUmQAK29B72M_ohaGg_yeype30dn_JTt3ZcpJUtN3NXYFeCeLx63N3sWsj5-fwD-fyfATyVrO2F4OBUC33T_q4jkpXtP4tOtymQEIiNUdHjKaC-cwYPebZumgmz8XEdsvmwQamHNx-ED5xh16g-cSRFh2N6M6C57chn7J7iQf5nKew8NWzxedQ3Mu8CHw4VaJdnfkGf9sBHonhFOHzwOS_eo0qSjbknSynBnKSOFQjerW82M4zZ75odeBvUTq17JEq2717f9_AbTx9Gn92cqvOszTrNET8sFjS1ugnxdBPmCewOYH4_F4jL_k6p7SA_mgA__OkUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS02juw4EyFNCWKPCl6Pbi6GLO0L3O4kxClw2c78wCfMHe6O49fnHy-VEiYr1U6sXq7TedmZRFcsN-zKrp7_rrSD_CNZbNF--UZTnxJ1CNlrDL0g-FGGjsTG5sBWyYhx_qJL7ZfZJDSpJ0Pt0OWSQwPggbU9ikHdlrPj9uVQso07iyca7x2pnRGF0kplxBIQmrtbknaWFfCxiA1Hpsy6uDks2h1Oe9Ti6FyrLUmxnuMwFwlovsLo11MK_38LoEs8n6Ph6fxRRmJXu4vNVBgQado5-1uMyNryMCnzYtfrkDuHt4RyLIaKg_txKPTNorrQEVuZlAh6xsdqNkZ47mDOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBbjJ4TecumRUvtyyBztL1iMhxlzMn3iPRVw8H0Tz3lyYVDHuD6l7lIHMvGeY-137OlLy8vG5eNr7X5bQfvkZScfdxIuP5LyVHkCypTAHGeaF-ID3Aohp6ht3OR0PZvulNaqAVrtlkT6aRPu0vwW6oVeBDdU4jwwd3obn-hvX2l2Obrp3nz9-TFSUORyI6ljpj8e2-rBzI83JYFU1DlLCBH_qBuYu2nmA16L_u0SRCNIBJKqfwqI4A2Y0eYMLdJvjuILKUBrroS4IEYH9CoZC-SI2XZsClpsIYx7sPQ3ee9r6uS0y0CsrJJnH-jy4q5ZdS9WHqwlflE8r74sVpPceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=SV4k64h-WansMo9TZOu-lXWKDMCwxuGZ0xkYX41z-Tqr5XHHAkRdDuCahQf0un0hUNq2tNxKFHe9K8f5PDEkHzhh-sVU6L_OmPP2DSDT0LMJrXX6JZkVGkclzdcHRZHzdugP9JAR-CCDG5nE3euwqHJr32Ey4Nd33AxvjUyc4ZoGKzcOVQIIzQWQesCD4VnVfptIR9EP8W8E9xgBt29RCbKyubPsBrtD3nPjnriJh3uAmIlZvEw_ANh7PfJiElnr4ubosQEvFS8F7ydZa-r_gHaHtt3Kaf65LGS_3DD1mMY3kbn-HPrxhX4QiVofyCDRKq1i8gJDcglkHL-HmHa9pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=SV4k64h-WansMo9TZOu-lXWKDMCwxuGZ0xkYX41z-Tqr5XHHAkRdDuCahQf0un0hUNq2tNxKFHe9K8f5PDEkHzhh-sVU6L_OmPP2DSDT0LMJrXX6JZkVGkclzdcHRZHzdugP9JAR-CCDG5nE3euwqHJr32Ey4Nd33AxvjUyc4ZoGKzcOVQIIzQWQesCD4VnVfptIR9EP8W8E9xgBt29RCbKyubPsBrtD3nPjnriJh3uAmIlZvEw_ANh7PfJiElnr4ubosQEvFS8F7ydZa-r_gHaHtt3Kaf65LGS_3DD1mMY3kbn-HPrxhX4QiVofyCDRKq1i8gJDcglkHL-HmHa9pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLugSfjbH4EePKjqkQxjI50X8KX8XVKj4uQ1Dzi6OAc-KDCXHT9GpZTgfZKBjhSlyWCOXgoSDDm4nnS3o4wuB7sT3EUxExR9j2mPTUlt4Mdk-No18ADkR3CdIxudHHkdk_2cxHRE8y2pB2hssmkux9yIbhnK5ORnpu_2J7O7abr6aftDUJsSOIwgeVO31cHvWGSnYU1KyOeLmr4UD5wIH93xeshi9KdqinhfaqfYs7L4IHvV-LMjqZOCnodEnj6SSgRSHJU-geuelAwlj8I2edFTmAqaYVHIat-teCzflNVmChVGcjegJM3STtxXgi4hltiiBIGwSsy09Ypbdk_7Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZWK2dR_d-HgtrGjihpErUnhp0v3jCv0LDy05vYKdv97j3CQKFgOf4qsYI09QEX3O34Z27GE14t9Vh2SPXt3urSxXdac6xUDydYNWA4pICo8P_wNxR8ekb0DJmnDIngxfAtXixWL-RRp73ktCxcC0LKh6i9Pm1Cyb0WpErmV6EsVW-i7jhSwhCPNvXdvcO4n6tP7X_EYcjkFe3t9DPvzzFg47gN9xckzVXmqNaet-c9uXhIPYr4USjj9cuj3TARsPNNJlqZjpf-VLtWBNIpzuN-KAd11ezml49M1gGBwbjSYhqCJ9395NmzyyFRNAnsCF7RIvfxegVZ4svma5Hi7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ox3gyCI8cA338qbfLjT0DySx3OXsQtxmPVwpKkOvlfHG7y16itYGXI2gAuGP41a0qc5bYShBxyFo7NnGBmuD-tE6XFNHf2ctNvJzbyE_epb9Pr0OGzeIRAOxBd9RAM1yTIZSe62o9TEFzCIYJWd2DbtFdsNGqKcP10XDGqbJdKsGtULV4FMQJORJoTdVCi_wicL4GAuAl7YM9MzgGL_O6CfAGr0iokX1s81G0syTqKSq-hGhY4dRROuSY-VXNif3tOACyn5w9O0kUJBqZq_I_6PogeWZA2uumbYL5bGqRlPWM-utrtBxPZpN82gpva0xFYSNDtMkj0jba3B3U2wYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxSW4wkYNTWwk0QeBI_T84y-iWNf-VxtTFR3g0A_VOTYA6NUqJDQsOHwcULsYOAKkQ1Koy3PQltWM-p9fB6u0gQrHVm0vMe-ov_asZIFrPNEDiwYq7JDHI88_LyC2y2SzyyOoMFNNJBo7mc9SXosswv5HqL_etatY6uiFQ0WQOmopzwze-2wr_5zBaBqVHbXFfrA9Leb1TM5cLXyUVaUefZ-23FTyJNe-ZyJComNSniXa9OAn-K5EqOI2JX39WLNw8Sel3afnBeZd4C-lP73rxrnvqyWpTUnRHaULK3TBC0zaAI_NxF601zFJGtlD1F-8PH6XkKKYN9phTHWmPreTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm4ETxy3Z69OMuXLpE-uiude7CrDx4XzOcQI646TOBVynk4PeDmcmB6FmoDycYmH6QkJvn4JCDi2XKfMbbOVe68Zqrxeyjk4rKGoNBwrqv-f_x3T1Da8ybJofFjf3Ken_vxyZ1bda-o4EoLVG7pLP96DUvMChOb_v4Lhjbhc6XfoDsi7_Y--EzYFUsWJFZXKlllZ9R9E-r6Af2NxVI-PBJLK86xzZBtT6gVSIK94BsuSnOn7Q3jwtChcyYM5uRvscsYX0MpgEHtixzUkPCt9O7a9TrrlIduXX7mgZ9gkX2dGh_P6vDyi9QUC4nJdo86fbeuzbGOGSA0z3tjz8INtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=GnUOoKBP8t1XdQsQ45T_oHA_EI3GP8aZ_wQe3Yqw28YrlLsMcwhLwShdM8URJhcTumaEv-SI0aY-2AC3S_3PNPjsOe7DnHXpU9_F1GyzF01rhTg6XvPCbU9KOThjDLXmT6Ok6HTi75rvR5DlSBxy-_lmPT-XW_piKVXHkpn_ygvGp9WeDzwqiNabumUyMmdkKdLA6J03tLEjRwOErYn9vNGXS7KglNS8gnZMovy8W5MYtfVmbPajSwYFDZTzoGk59e-Sgz3sbV2TR1lcKzxjBbpmoEaJ1BcGla8LmaZmXy6sOMndD2c-jlz6dyFQ3iG0zqtTFkvXdhBqaPySwEANeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=GnUOoKBP8t1XdQsQ45T_oHA_EI3GP8aZ_wQe3Yqw28YrlLsMcwhLwShdM8URJhcTumaEv-SI0aY-2AC3S_3PNPjsOe7DnHXpU9_F1GyzF01rhTg6XvPCbU9KOThjDLXmT6Ok6HTi75rvR5DlSBxy-_lmPT-XW_piKVXHkpn_ygvGp9WeDzwqiNabumUyMmdkKdLA6J03tLEjRwOErYn9vNGXS7KglNS8gnZMovy8W5MYtfVmbPajSwYFDZTzoGk59e-Sgz3sbV2TR1lcKzxjBbpmoEaJ1BcGla8LmaZmXy6sOMndD2c-jlz6dyFQ3iG0zqtTFkvXdhBqaPySwEANeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مقامات پاکستانی هر ۱۰-۱۵ دقیقه یکبار میگن به دستیابی به توافق بین ایران و آمریکا خوش‌بین هستن.
موضوعی که نشون میده وضعیت برخلاف حرفهای مقامات پاکستانی اصلا خوب نیست.
🔺
یک : پاکستان در کنار بنگلادش یکی از متضررترین کشورها از بسته شدن تنگه هرمز بوده. اقتصادش دچار ضربه بسیار سنگینی شده و باز شدن این تنگه برای پاکستان و اقتصادش، به یک «ضرورت» تبدیل شده.
پاکستان فقط برای یک ژست در سطح جهانی در پی رسیدن ایران و آمریکا به توافق نیست!  بلکه برای نجات اقتصاد کشورش دست و پا می‌زنه.
🔺
دو : پاکستان قرارداد امنیتی دوجانبه با عربستان داره و در صورتی که جنگی بین ایران و عربستان رخ بده، وضعیت پاکستان بسیار دشوار خواهد شد چون بر اساس این قرارداد باید مشارکت پیدا کنه در دفاع از عربستان، همین امروز هم ۸ هزار سرباز و یک اسکادران جنگنده در عربستان مستقر کرد و البته سیستم‌های دفاع موشکی،
پیامی به عربستان که در کنارت هستیم و پیامی به ایران!
اما وقوع جنگ بین ایران و عربستان، برای پاکستان یک کابوسه! خصوصا اینکه جمهوری اسلامی در پاکستان نفوذ زیادی داره، اما ارتش، دولت و نهادهای امینتی همه با عربستان رابطه بسیار گرم دارند.
🔺
در روزهای اخیر خبرهایی منتشر شده بود که پاکستان مواضع ایران را به طور مثبت‌تری به آمریکا منتقل می‌کند و همین باعث سوتفاهم‌هایی شده بود.
بهرصورت اینکه پاکستان امروز دائم تاکید میکنه که همه چی خوبه، میشه حدس زد، وضعیت وخیمه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=bPJ3_vxVqbwmnPIlRAr5B8TdHyOF8mUzWszH_6q8T0pQiuMjuW-44f4edZZWwTEFJ6Fz1bCe8hK0tBGDQ3Ui3Hf9MXkwPKBIf1hGu1eIYYdauE2m902-huGesffIHIk255N5dZTLvTPVsSbYqhXKLN2n26RL3U7e1bb2XKB_KPRFWk6h2ekeYIuvUUw62343RcAbjxhsdrzkditZzUQ36yRqbSbD4Xmy0R1yD46U4sJBhSHkGV2F83JzLc9w-fgP9ExnI1ARoa6F_jGRm5zu-FzGRpZZV5LPEX3FcsgoipxANdHxTClqzyCLapaDwB1Yme__Wxy-O09XUfNpOCbOig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=bPJ3_vxVqbwmnPIlRAr5B8TdHyOF8mUzWszH_6q8T0pQiuMjuW-44f4edZZWwTEFJ6Fz1bCe8hK0tBGDQ3Ui3Hf9MXkwPKBIf1hGu1eIYYdauE2m902-huGesffIHIk255N5dZTLvTPVsSbYqhXKLN2n26RL3U7e1bb2XKB_KPRFWk6h2ekeYIuvUUw62343RcAbjxhsdrzkditZzUQ36yRqbSbD4Xmy0R1yD46U4sJBhSHkGV2F83JzLc9w-fgP9ExnI1ARoa6F_jGRm5zu-FzGRpZZV5LPEX3FcsgoipxANdHxTClqzyCLapaDwB1Yme__Wxy-O09XUfNpOCbOig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPbMoezMPvQCmfFLuNYTo4aMiQ3Sc9pBiJWOb1v58YOYEEcGU-1sw1_ndv0bO-Oknho2EPtxBt9t7JVuwu8pfbWfKErQMZRXpmyIjSLBHRfL9xv8-odCeRSdXgemNnXqDybGJKQAIBabPVZBddkJo_DIEVXym4Au879R7uabErObiEXUmF0bpTRSnNeBrVHU5ZxMwrHP0iQ4Jj7oJtzrzhvs51N8adC6CkuC7DDw8fr1rx84q0iCmb40BPLkAux1VUXrlzyRYf1wQCR2dDRtdSUT9ws3N82gt59qTzc5NzRXWo6FPmEhpPUgRJDVoQyUJrRVSWY4aswkLbyNPMl2nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aq6UGvCMvLiTvBMgYKUq6GNFcR4lnQBpi5NJY_GpaI-XXo1e5EY3uuj4F-rSAz19lwzlYfxugMPZM6tTvWRZLKLFi5KFM5RWadA9kRQqqqsiK5Nl3TEZJMocRvr0rlTFaL70fMsHhmGjuUZ3yh6dRcoYtGMh6TuKpxxXOg-O5hBpemosygsrbX_Lw7nX4iU68KDaNOfp9oCdeqcZF-QZDIfR_ogJboIxfhTvTQOhOmHOhGGvpKRCQkpqH0VetABruWu8dTmmdrTNQdaRWH7GwyU-l0mCkoCVR7OTUgk7j1uWjHEiuc4IpNBFfLppUJMeFjltq_Uah9bGvXPJREXHug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbYaoJsH7E5Y5qFzH6bLmdLz-BeTZTyznOW9cpkZl4e3sjmceWOtxTlAguaY7JcQy1EZ2lsTIuFFYzIjLryJz_byBK1Aa4WRO7uSKDczMkgxSOFaloIwNicgdpDud5PsR28CLtFIJIaUijU-7ia3IYOCrFTgIC5nLXMxKbdNtzsfCTWSOgcQ5huLzM1yU3RXCA679mb1SGQli8lW-MTRx83j4NB2ElGiKLbO64T5li_0w1Wgehx__u-ORnm0-QA11_PaKl2R-SV9-xTeFOfUdo6jk2c2Zm47HBJDBAoq1oODblgnPWrzEZ4K7JL_9e0rQxGtDWBvMttUF9i2g1isFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1FENqP1vCHUTCXPpZbnyMO49zIGisEmgd4fi-o_Q-omhSkhKH8YJgF9bQ0SLy2j1HtAR0jdCwOyQCk2CkHJpH9KCCnJ-PZbBASzgVrX1ipgFgGQTaCaZqx-o65hGzZp6Vf_DQ7749Eer4TYIiY-EIbS1pNx77wVLaeQkC-s5zBjeoMOgzlwk4_D_bz23oUBhAvcvWKRaNtIPsVwz2f1AR6bXSNOUDp-E5ORy6C2DV0FWKxjRkDn1eNTT8mrvctSsifTLUAtmhCiD245nPH2agq0FKDkWv9j2R_Khef82BXDJyT9Pulyyt5ZxVXU6FCdC3tlDvaEkUCEfjPghYGmUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=VZZs5XKnw8wezBn5qZeV6V_-nR7FdCr1HJCWmYKFOGgAFx9kok9MdlKLefbL_7QbX063cmsCWSH_m5q6pgg4C13Fx3J0zupAMtO6ei2qIX_4WdqQnK2S6RpzMiJEhYwKqK_ZfRYlFzTrPN1V2_IojK-lt6cDW-5AhGUKIFKZngjODC8aFwmmOFx8kfAt9YmDAPCkam-7fyhxTOPLlfJCpW4yUgj-15psnp9meTreRkyhrnekp5rK3EYwBu1LAySDHZquI8p3D0GPbx2HSuawyN-z5uMsUjJAURJXzPVTZmV3sKkDopHAgiYjkoJscbTSOh1GR7q-t3ZRtaIFsxjC4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=VZZs5XKnw8wezBn5qZeV6V_-nR7FdCr1HJCWmYKFOGgAFx9kok9MdlKLefbL_7QbX063cmsCWSH_m5q6pgg4C13Fx3J0zupAMtO6ei2qIX_4WdqQnK2S6RpzMiJEhYwKqK_ZfRYlFzTrPN1V2_IojK-lt6cDW-5AhGUKIFKZngjODC8aFwmmOFx8kfAt9YmDAPCkam-7fyhxTOPLlfJCpW4yUgj-15psnp9meTreRkyhrnekp5rK3EYwBu1LAySDHZquI8p3D0GPbx2HSuawyN-z5uMsUjJAURJXzPVTZmV3sKkDopHAgiYjkoJscbTSOh1GR7q-t3ZRtaIFsxjC4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=ZPPwvzvFYViWS2EghhUcw3bc_wZwbWmN7FY5pvX7pswH-lOdmp6qZZs_yo5ctW8hDwABU4Sc6IUzbTn5YAD-bPM_tFJqUtN0vu30s25Z8Y2FpmRXxPWO9DgdN-OI2PCRuS6ujON6sl2J7AiFfIrpT39-impy24kqAORbKoVIUkjM4qWzYCGokksq_XjDlVam3G8607KxflfsCFbaQ4YdtAiR0M--lAcuJgQ3HjzcRQq4HQnrRg7LpKtNIjNHsfKK6yMDaaS3IpL5X0K14sI-FuiEuX7hEugiU155cJH4D2o7jRKFgvcqbqD4MLB0rZFA9AkGyX6y8OS8urmGUpmTSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=ZPPwvzvFYViWS2EghhUcw3bc_wZwbWmN7FY5pvX7pswH-lOdmp6qZZs_yo5ctW8hDwABU4Sc6IUzbTn5YAD-bPM_tFJqUtN0vu30s25Z8Y2FpmRXxPWO9DgdN-OI2PCRuS6ujON6sl2J7AiFfIrpT39-impy24kqAORbKoVIUkjM4qWzYCGokksq_XjDlVam3G8607KxflfsCFbaQ4YdtAiR0M--lAcuJgQ3HjzcRQq4HQnrRg7LpKtNIjNHsfKK6yMDaaS3IpL5X0K14sI-FuiEuX7hEugiU155cJH4D2o7jRKFgvcqbqD4MLB0rZFA9AkGyX6y8OS8urmGUpmTSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR0sKUh-qiXI-4OeBkUK8UsNAmD63jN0XDGIPRp3ciCGFESVVO-cOIr2bDeHCfK8k8m4gPM2UlI-zTep-kK1T2TqQyjkR31ZzvhZkz0m2TxgOO6SfaXojWZmoHe2ML01_0dFYixepVzxggJqdMuDcFXh9pgiS4apbnlMNoinE5KSnoSZ33x_SmP6Ow6H53Jhq3YnvEFWdpbkEJ7OJJFk_RZcQOtCPCJu4CU2eLAZMQ_xEdplb-kbAAt1rEZcoXbPxw1RNE2gPTK6NEzZP49m2AYpno8EOGnA5PNBndwGMo6o_SF71V47UwZdVYHN2N6MlgmSFvXH4KCD7E3VF-b41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuYBf9vCWHs0A_9tg9bqutnAOqaQ2ntWdt5WjN5g_bGIxCSDT-IXx0JNwdTHv6948aeK_bWyiKQ3BS_h2YXGBFzwS_0xtTgLhlvWRKx3Dxz9iVLWUaLoM39SoSZJiWwGcHtK1xddOOBXHu91Z4iFfKyLgOVCFG_Au7_via8wTSdcxDpcn5cny5mi9ScsRMJIlevuB16sIjhw6ClH_56FY9jU_rM8YNdmohGFbKXFe12Qi6qrktJ4SVtG25AmV8EsNxzcy_rN0iLM59G8bx-U9TeKo9U6EVPhKbdoXMyF5dvlPREPiwOwqwg4hjz5Yti8O6ANhMKM3gtC_bSkY6G7BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShxOR8ZlAoWtpFlKpmWg5mkbMaLjOnEmvtnbe2CVkLXmc-8zn03v7yEZ9nZNL_7EXZ8FH7GE5I2UFPham5oji2tFbiAIX6KanS61cfgvPWkk305vXJ_DScMXGLfNKw9fe7-Mx_DcjLTe0MS3MNZDoEjsg9hyYqce9xVNcaYZc009B3TRV9dBDIRJRwPz5fc3vHky8CfRG6QfpsRGLz8E129Ca52JHMaboOMxFm4YP485RP4aagnZFWclSoKqYSsMuDRTG_L2SQnKLDDgm4N_K9i0gRmgsnJ6ZHifV3I7i6wUnNxnw6qg0CzaxqQdcb0gKXtpRr4QxyIb1e3ooefH2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwnNbQGOFYu5mZun4QgJwpst4OPllguIbRB9L4ej4tLUPmEqDnOex1w1HH5JwNtH0jRkxcpfLETvpQYZ_lXE4j2qWRXbgsOfHzuRzAqJUrGAnhdZPX6SE-fSdScG3ljsjWYq0gAZaA-x8w4Tn4NDDkpLGmKo-DS3EW112_KE75mPS_vHhBpsNsbNQS0mTLpiqF6xhxFQCAqz3F88Bm1_iyn0Q7I13uMv4poQ_BGZS1P1wEIwO6UmHxIiKmwG3vv6sVkm-YlcxBLtCU6CASgF6xWfhgqfi4vOlBw6QI7svaP295Y5A8or6cI9yhGx9a63k5RXrBrRImUn3toTsi1_Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=T5tRu2GscgY4mityj8qPh4oA7nVXcNgB68ghS1-CMX37FR-F19Xel_34--vjSZN51iGfkgCDc7wqwipmCs6HkLItCh5-Z031wiLhMTDUM3z5R6EeiEhambC0kB0mZ_UYZH-Hw8JZkZ7T1PPyra0DyXqQHpkZixpiHvyUbrii6v0OSilpD2EPEKJK0gWdHu4XNOJWaFu_wD7t0ObYYdsqlLmvdfV7WU9_GqIMafTRjS8xVWY0UoDbMyTcGMMvA6CrEu22kpPSwrzx7pR8jLWM8fW_snB9wHqm3XngQkZY3uoj-craIjNYvdA8KBUM3Mr5ohmVbqUJMKl2QA7e0DJWxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=T5tRu2GscgY4mityj8qPh4oA7nVXcNgB68ghS1-CMX37FR-F19Xel_34--vjSZN51iGfkgCDc7wqwipmCs6HkLItCh5-Z031wiLhMTDUM3z5R6EeiEhambC0kB0mZ_UYZH-Hw8JZkZ7T1PPyra0DyXqQHpkZixpiHvyUbrii6v0OSilpD2EPEKJK0gWdHu4XNOJWaFu_wD7t0ObYYdsqlLmvdfV7WU9_GqIMafTRjS8xVWY0UoDbMyTcGMMvA6CrEu22kpPSwrzx7pR8jLWM8fW_snB9wHqm3XngQkZY3uoj-craIjNYvdA8KBUM3Mr5ohmVbqUJMKl2QA7e0DJWxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-1OwDZUcdDO_NXp0DowCnACa0XJas-m2Q9q8AaRjLTHIfUTTWh_Mw5VnQ5qiMYy3064TcL-6Oqg02s3k5BjXAig1MdyyKQAXNU8X4CO1BGyzWlZy-fnYy0xxv4zqBLOvRJvZSH5O7Qz0azuMbgOoA2auE5dA7ApIxFQmzwtyobhWHa3miVQIogH32lfnk54nQB9dlderFEl-QGTEixamt3oJKJZK9X3JKuJOknRQnChowZoGYXCBZMGGnXRuom-_IqVF0Y4OfMzRDZZJN0W-LnmIeRx_kr4l9N5grQqqS3akqVPAT4o73lYxa8GU5upv30EnS8IVQHk7JXBggYEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfXyHoBToj86_R0gTqaCqJcgB1RZ04GqOITzOTfZ0DZECym57LlGv7u2D54rZ62xL-LrlkvToy3Efha3xTVqDuRs21lSLNlZjRe8J9o_bjpvK32EkkRLfyBD6YZu8ifmvCdvBJj_Xz0dkk9hp23_u-dUHvKX_RgzdK765EifQSuSu9Ig3AGR6PXi7N-ynJhaZuCD3NhW9FTR5oyS9alOMKruFOKJoZSfo2MsOm1qsCizVhH4Iz3VhOBb8pKS3Yn1bA7cceNns0zfItF8qxD-XQ5dtTp1QkzNDijw0XJLThWy2hqa0JwzKFedSfxT2CccFseKIxBQUhYe8tFn1bpGvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=uau_oek3LHMLDPRHJfECoJ5qhEy_GLCv0tjWCeFmU5uAiy020NqdRgaWW-3OtViVua4y6jTjNIHCZT0DEZQtufS3vwo_x_Ee3N9cB8m3T2v2VHnEOVI0lOfASbCuB6RM8WT9_k5qo9sWXbKEDSMP603BxEsqhTuOCttUt_swvmnNuL8AlIZf2omk6DysyLdDvyRRKSv2LwrjbnVqbh2LxW7NXWx47HUILKNOm2B2HdJTjVstJ0PbiGQ2MpTRH9kb4GQibkBoy3_Z6kev8BP-DAu4o988nvzNUi_FVU182T7LyEimIKF3xaHKlPvIt-uVVsa90k_k2Zkd32jKDD30rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=uau_oek3LHMLDPRHJfECoJ5qhEy_GLCv0tjWCeFmU5uAiy020NqdRgaWW-3OtViVua4y6jTjNIHCZT0DEZQtufS3vwo_x_Ee3N9cB8m3T2v2VHnEOVI0lOfASbCuB6RM8WT9_k5qo9sWXbKEDSMP603BxEsqhTuOCttUt_swvmnNuL8AlIZf2omk6DysyLdDvyRRKSv2LwrjbnVqbh2LxW7NXWx47HUILKNOm2B2HdJTjVstJ0PbiGQ2MpTRH9kb4GQibkBoy3_Z6kev8BP-DAu4o988nvzNUi_FVU182T7LyEimIKF3xaHKlPvIt-uVVsa90k_k2Zkd32jKDD30rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطیب نماز جمعه دره سن‌گابریل - کالیفرنیا:
تغییرات بزرگی در آمریکا در حال رخ دادن است،
و اسلام و مسلمین نقش مهمی خواهد داشت
وقت دعوت به اسلام فرا رسیده.
مردم آمریکا «باید» به سمت ما بیایند!
باید بیایند!  باید، چرا؟  چون ما «راه حل »
را داریم! خدا راه حل‌ها را به ما داده!
قرآن و سنت داریم!  اینهاست  که
آمریکا را نجات خواهند داد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaDau9XrscyYkWle4m1JClAup0f3rTySqSugB_cMkBHeE3akNmogrncA8vqHvaNsoAg2-dKtzu_tlY-xLcALRTCNEPcsD1rniL2InX271GLFNOprSqev-QmnuXFo4Wf9zrLF5kyUoOrijuFsQZu4fJyNPMl_XTfS5_3TibBukQ8D3ZNwfwWAtnyIjjVubw8o7gPy9x3PeyOSy_FsbUdOTKbpavTTL2T2cIjvBMCz_B5o10mGjUSBcolIU-2qxMLLbsGEPNTGtRWbU9-ZSLpOU4g1VnAaPyHJ78vEsj6PJTxw5lNV4mcwk5tC0uRFMNNXLMRBHQONH3s13aa0mBC6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=daiQUnnWtb9C48VbjsHNkttu-A54RuNCe1qjoGhiNMyNRPc3JQUFIXkSVEuFEztQPH6BWs19LEYzqfMUHgIYAJm2g-I2hVzhTAdrayFi-9fvhRcISX2sXnjNr8Ntt-9GDBgK2jPMpLJUes8r6jXDwqPC3oM6fwamzbSRrmGKDsdJh5W8zNFDnYS1yjaRWTxVgR-swNL9wMTyM_aow-KWsIm9DbivXNr8koEkIsKIYdfyjwcNaJmA4DBzO-7vHE49fgI7Ugp_eU542u6QbOvkhbni1J2XMXlQsAqDmvbNUpwXagU4LMQsdveqAK9_nmP4OFgAxWdTHKgsns-Bq-lsew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=daiQUnnWtb9C48VbjsHNkttu-A54RuNCe1qjoGhiNMyNRPc3JQUFIXkSVEuFEztQPH6BWs19LEYzqfMUHgIYAJm2g-I2hVzhTAdrayFi-9fvhRcISX2sXnjNr8Ntt-9GDBgK2jPMpLJUes8r6jXDwqPC3oM6fwamzbSRrmGKDsdJh5W8zNFDnYS1yjaRWTxVgR-swNL9wMTyM_aow-KWsIm9DbivXNr8koEkIsKIYdfyjwcNaJmA4DBzO-7vHE49fgI7Ugp_eU542u6QbOvkhbni1J2XMXlQsAqDmvbNUpwXagU4LMQsdveqAK9_nmP4OFgAxWdTHKgsns-Bq-lsew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=KBc1JTSFkQUPe-wgABeYaJ7wxmJun716v3ZOF4FrlGYcLryvozxcNBA6WG75UtwuIAtjZwxQORImlxCxyO4Zv7QP-wBQt65qtm5mwd7-DjNhKGO_Eb6Xy7xjqfIUnnKg9DO7cQyJoEOdIut-q-HRz0IkVxzRT0ZSYPXIuAMrUndp0-BXvIUyAchy1FlKvfHEo6PFhfDkdsZxzefF8c5oBtdWtwyKwKoFSrq_Io8B1hVPvmhaLHUxAqIyEkpnQyId6Zx-4GymJtafpqqACwsR6ZmiQcJpTX_aGfZ4iaru-eEQb0y2qkjbKViP1ObNjfv35eRmk_1E8J0ksWd7HuYbng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=KBc1JTSFkQUPe-wgABeYaJ7wxmJun716v3ZOF4FrlGYcLryvozxcNBA6WG75UtwuIAtjZwxQORImlxCxyO4Zv7QP-wBQt65qtm5mwd7-DjNhKGO_Eb6Xy7xjqfIUnnKg9DO7cQyJoEOdIut-q-HRz0IkVxzRT0ZSYPXIuAMrUndp0-BXvIUyAchy1FlKvfHEo6PFhfDkdsZxzefF8c5oBtdWtwyKwKoFSrq_Io8B1hVPvmhaLHUxAqIyEkpnQyId6Zx-4GymJtafpqqACwsR6ZmiQcJpTX_aGfZ4iaru-eEQb0y2qkjbKViP1ObNjfv35eRmk_1E8J0ksWd7HuYbng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=gk9TgC0fgIDHKrCtKGOqa9IOv23jCQ26Tw6HFkxK5Y1NekJXmJgdCxbVNkjdMYENgrXCmb5CATQC3glvydwBsSmeVrC-R2tOauO8a-yxNrcSrcNC8Xy7sgS4grJ4zMnNIneCB9vsAxEKAbY5CLaQsOSGUMcfeVL_z4L6kIe1FopW5BcbqdzsQkvfMXtr6nyAb4y0pZxUk4ueHhhuunzKkyx4BI1X14FXh4pYGUea887Yky1Hc9t0iaNMiZCzCsryfEy2CgX15tsu1ugDXVtxYRraFRlcW0bLawPuXQbw7fj1h3ZysK7BZbzbyibYdg6tlmyQmm4zxopD5HXV5FUE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=gk9TgC0fgIDHKrCtKGOqa9IOv23jCQ26Tw6HFkxK5Y1NekJXmJgdCxbVNkjdMYENgrXCmb5CATQC3glvydwBsSmeVrC-R2tOauO8a-yxNrcSrcNC8Xy7sgS4grJ4zMnNIneCB9vsAxEKAbY5CLaQsOSGUMcfeVL_z4L6kIe1FopW5BcbqdzsQkvfMXtr6nyAb4y0pZxUk4ueHhhuunzKkyx4BI1X14FXh4pYGUea887Yky1Hc9t0iaNMiZCzCsryfEy2CgX15tsu1ugDXVtxYRraFRlcW0bLawPuXQbw7fj1h3ZysK7BZbzbyibYdg6tlmyQmm4zxopD5HXV5FUE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=c_T-zc4Ek6XmbScGcDIL_7n1_AR2XeXxsH-p7Kmk-ivLtn0xN13COoCZWSq19LiYiO7kSpLbTfUWI8yJnjA9HJXTzF3i0I_5nYA07snukXP54U6rm4oLJNr8uxAvpppuD_LIAd3Jzy53HWjA_ftTyg8GBpDKTgAGz0bHkxjvvN-ie-qhIOzRC3vrQsn5Npjtg3Y1_i5EePwdWDL4Z7pu9Z76mnSUKITL6hgJ4ODdve6wRSaWGv9nOgK2VD6HK5vSyENJtcXQsEYXmN2TEd9ZFPaWHwoLALhALzHziDCtgEKQc3PkHCyDBRLqqJy2FXzJ67uCSY1FK_EtYUfYOaPSDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=c_T-zc4Ek6XmbScGcDIL_7n1_AR2XeXxsH-p7Kmk-ivLtn0xN13COoCZWSq19LiYiO7kSpLbTfUWI8yJnjA9HJXTzF3i0I_5nYA07snukXP54U6rm4oLJNr8uxAvpppuD_LIAd3Jzy53HWjA_ftTyg8GBpDKTgAGz0bHkxjvvN-ie-qhIOzRC3vrQsn5Npjtg3Y1_i5EePwdWDL4Z7pu9Z76mnSUKITL6hgJ4ODdve6wRSaWGv9nOgK2VD6HK5vSyENJtcXQsEYXmN2TEd9ZFPaWHwoLALhALzHziDCtgEKQc3PkHCyDBRLqqJy2FXzJ67uCSY1FK_EtYUfYOaPSDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=L29F3eivfQ1Nb2SLaKHK4sd2JOQxdpMf8DoLoVqAYWzikIJzDHF5HQ8Jt-mhr2rw1YjAvf5JtmvSTqWZ65X0Xd5x-hzHsLDRamVCXANNJvqVSCBlPnt4T_YILsH_louQ_pv1bvtc9m90WIbY3YScrbjog_gOcTeiB4XUE-OoFdqEt2a6P3PXetjof8glIFeoKfo_WYeyqCHHaWIwiIoTKya7bR_8q1UManbRJY0C6V900oCC0VCsTDIC-aY7VGEqI9oyTuHMr5RWIbo0z0aEPZd7FSzz596S_X_c_FlmyfVl9-8VPlAvsUHTV8NdMKp7n3RexxDUMK4fb84rT8YTSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=L29F3eivfQ1Nb2SLaKHK4sd2JOQxdpMf8DoLoVqAYWzikIJzDHF5HQ8Jt-mhr2rw1YjAvf5JtmvSTqWZ65X0Xd5x-hzHsLDRamVCXANNJvqVSCBlPnt4T_YILsH_louQ_pv1bvtc9m90WIbY3YScrbjog_gOcTeiB4XUE-OoFdqEt2a6P3PXetjof8glIFeoKfo_WYeyqCHHaWIwiIoTKya7bR_8q1UManbRJY0C6V900oCC0VCsTDIC-aY7VGEqI9oyTuHMr5RWIbo0z0aEPZd7FSzz596S_X_c_FlmyfVl9-8VPlAvsUHTV8NdMKp7n3RexxDUMK4fb84rT8YTSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtkErK6CdvCn0ieztt7Fy5hbLQlwgcNSuuZqHbXdj7_nsikxns2J5MuC0YQvIzQXYYu1jBLXA8MRz1uAE-1ryZKFb3lmQogt09ltlcymy4OHSedunMgJdUcau8fiMWZJ0zjPW2t2XyQKKOHwSmL2f8KwJWc-fRB3iD7ouA8MxfbLj-IyBQKR0i9PXNi7sfu9EiqVOnPRThnH6GFT2DBShMiRpdprRistXGXyxNukodbLAB_Gdoyj_AYcsenOEyvFGpn-QoCrGjw-bKBzd31JSL0qRN6WgLvlrM5JQb_R5uEdV0IIUmLF6pcKjhNTlhnLdXrst2DgMvPzd7tA83LJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ju1W27xaQzQoR70-yQH8wFz_44yXGMf8mygxKvVPVV65NxXmLEGX_SKLpgjlCBVXEl-w1Zijl35gMu7tjajatm0ppyXUWvWlyJzRIomj2TqHq01Ttq4nDdyhCWAicSRB5mOIlFcqWhEwvslmZGgZmA8PlwxpqftsNVF-QyP4_1hcYHG02zv75_sU8yA04q_sMNx-EcMCGIqcjDsiOiDIU3SJkSHP597S3vsJoBwWPrCFriH3ok3RBUYM_jUEUSu1SHY3guq_LVl7yn7_QGLvnLGxSgosffou6Sw-Z8L1cRlWzZLKlx3ShNjkRiEMovW1fhoDPIku9kBtHXu97FCviw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnP9vv869fy4UCxe8FVFCZXrQ_HYuVd4YUWMIR7RJO_LbIVS8wvBlXn_5mHlN0LXGZiUhnbNeOqFevUJSMgSjEhZwsf5wGsK-kFuvG4yfhElCAuhFWLtPFWTUrKjCkD1EmFsOmN9gKh_X-ME6UTTl0D3t5Bxovoj_ejGkVTeOYd_P_69YOaOGGJZBcVxOy3yh6t6wBjzuXbez9HwSxGm_ADn-Qu6B9bnNE4la9p41TmHnt41A4DPJeGEz0m6JnMd-Bi3tRLOi2Fn4x5E_JY8u1yHgowZCZUV-atilNEhKd8znVLC0dwOlCx_PlavM5FpIjaaS4nvza60hcoA_I5kWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGHGHSr1zO2tDXkrQMavM72j0xjSSDC1zRKhpchitgHqTRlx5sb-rmIhTOpEWTiV1K76wUOewxjNsQwXplmr4UIqLGizHj1lpeiKA_qnQ5I5LHZUZmBe3vTKgfqdPIuggJcJgvsRl0wy6zR-2joBHXL_AvwnQsiPpQce4PjNdSGCNPEz6e6FgUUHXFI8S8q6CbJS7FzzlOgBy12CXYanTOGIM3F8rZHvVu9v8g-rOHap244ZAwXyaLjV1ZozbO4IK4QkLjfn7iHkGYhpjw2RoHWJ0SfSkN2CQKbFo_wUoS1qvFsAVJwpqYnh9hj3mYNaVB8nt-bTZww411I9i6qm2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=faqpUuxKue3tLBXmVZNRWw9t5j8A-0r5QcXyPmNYrQYOcx36M020AmDScjJ1loNVzoEgV_nkiSdWkfNJdPjE2O5aRTAucp9H3H2oeaJEbMy9kjgAu0a2jJzOHNzfMJnGtSdKr0n0BiThgSQc42H1Pt-F8hsIuhl0rFNzhj1G0g8GNyQk6o_4scfmy8Kv_TgyT6QkM47r-5QpUSWlLtzKeX9eB9h3f_Dpc_aKhLEdCBJF8mlyjkndQtwEaGOQEf51P7mw35wreiyUGfjLdsWUmpEZasgYrQyB8Fth3xpQvyt7FzrPyQYw4aDj8-K0FsPpO9VItAPc1zCe_iu73vdwzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=faqpUuxKue3tLBXmVZNRWw9t5j8A-0r5QcXyPmNYrQYOcx36M020AmDScjJ1loNVzoEgV_nkiSdWkfNJdPjE2O5aRTAucp9H3H2oeaJEbMy9kjgAu0a2jJzOHNzfMJnGtSdKr0n0BiThgSQc42H1Pt-F8hsIuhl0rFNzhj1G0g8GNyQk6o_4scfmy8Kv_TgyT6QkM47r-5QpUSWlLtzKeX9eB9h3f_Dpc_aKhLEdCBJF8mlyjkndQtwEaGOQEf51P7mw35wreiyUGfjLdsWUmpEZasgYrQyB8Fth3xpQvyt7FzrPyQYw4aDj8-K0FsPpO9VItAPc1zCe_iu73vdwzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=NcoXh7D5GGuBkln9d0IX2QmgeHzufyHJrluBTOE7-ta5qDa61IYeGb27Ch_rWzK9LDxdccFqmhimSsHdyPtW-YlL20_dO0z4zXkROlPbrwxahxo_rwWYCiThZL2L8_qzAOFw9bHGmjdAoMTGKJfvrpWqaPaiaXALbM5fb2NIu7iBrDiy5uZ_yU9I6VwMXbITmglsBqb3Cyc4WXVtIJmbpLkfi1C1WR_J21CTAy_bPj-UlH4cSnBRPD3vk3CJ2EH_VxAnaonZyql457ljsIEbmRXVYtBc4TaY_Vw8qw5Pzn45wb01mPTcBQ52UuWjz566nGOXZNW5Ngh5rDvp6cfmmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=NcoXh7D5GGuBkln9d0IX2QmgeHzufyHJrluBTOE7-ta5qDa61IYeGb27Ch_rWzK9LDxdccFqmhimSsHdyPtW-YlL20_dO0z4zXkROlPbrwxahxo_rwWYCiThZL2L8_qzAOFw9bHGmjdAoMTGKJfvrpWqaPaiaXALbM5fb2NIu7iBrDiy5uZ_yU9I6VwMXbITmglsBqb3Cyc4WXVtIJmbpLkfi1C1WR_J21CTAy_bPj-UlH4cSnBRPD3vk3CJ2EH_VxAnaonZyql457ljsIEbmRXVYtBc4TaY_Vw8qw5Pzn45wb01mPTcBQ52UuWjz566nGOXZNW5Ngh5rDvp6cfmmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=CajpGbEw6ujymreNHP7erApv1SP2A9uTj87RPyZCRovhkyaKKUKe2U_sXHQVG3zdObopl8YncbkNue6rTIyd9_oil9h46rt6CeengZ0op77jirn369MWQq2T7nslrle7pwh27QdcHsUm3NQgeZccXgtw8cRydMHKsMcwWJpsnbT398n5-73xq8GavwVsukETzWul1eYkd65Rzm6siTiFtNLviGzkZ0YIcsKle4nj5HRsJJ4v68GHEEodZIm7Zjv0seJb1x9t2ORUHjI3G97QiPhdsfwPv9hVLeNpiJ4h3irMkFQlTZGOkBw922FxXVmgy7fkVd0LlyaYmeBP7yoivw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=CajpGbEw6ujymreNHP7erApv1SP2A9uTj87RPyZCRovhkyaKKUKe2U_sXHQVG3zdObopl8YncbkNue6rTIyd9_oil9h46rt6CeengZ0op77jirn369MWQq2T7nslrle7pwh27QdcHsUm3NQgeZccXgtw8cRydMHKsMcwWJpsnbT398n5-73xq8GavwVsukETzWul1eYkd65Rzm6siTiFtNLviGzkZ0YIcsKle4nj5HRsJJ4v68GHEEodZIm7Zjv0seJb1x9t2ORUHjI3G97QiPhdsfwPv9hVLeNpiJ4h3irMkFQlTZGOkBw922FxXVmgy7fkVd0LlyaYmeBP7yoivw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXYiMpAC0ZoglqdgH_kUTWXhfspwm886tvHLduhP2v4pwjj0z1lo-6xLyjF8gNaB8LewfCDn_lClnRWFSCxQ1sDa5aBdh6GZgPJUhJP4ZGDepjJk00XcIX-_KLZ9fC_G4J0bFY2XY0in6-55KeH4bZCj90Ja-9k3VpkmVjt9HshEy7jxXKdkxwfzVxjitO4d2A8wTraKJj0rcDmtPaMnWRxSrgWlRoINKaCCY2ABiQG-UomvenRwWos_H5LHlJhR_oaZM3REKXA7lHctomGf78OpVXfdQpVfaNnIsQWEJLmAHSE0SEu829Qknp83yjXjNGiA8cOttXiO0LBNCH6wSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=eGBrjDPnfP6sOBEr4BeaUPA75e--95qPODYL8ucM2kO2xMVOtivbirMoWK-_2J0tSOEqzrvT0-N80ywOD-6jK4UqhPIYoz49ZZjg0B7XiPWo5WHUxufLH45pehVkJvQyXE9b0DkWyttlKn5yTXI1wGjZCnrqq8j0jjdWfgmR5IMMzugcTn7lii7brNwZUn_auuJlIlRJvoWc1uGKO_7vigAndXR2YJfwDOpcOhlfOgStHWM5o9wvq5vVwbLlwtt1BYoRJwAZpeO0OIAD-lWxOjaW0BG5VTDN6K4SiuptOQ23MRSJpQBMxxRNpYr44tBfhOzE-_gMJfCKHUi4mP_W51rgrjIqZfhVmU3QDxwg_bvjTbxVPwBtErV8MVmB2fRk6oQYGOXMvLRWY2R5YLSwJCQ8v2QKme-TXgFkcBmrVavruDASgDsUWnr17XQZpykYG3a1ThvtKoTI9GAgyRnHA_xW8pVIVllzjh-mNSC8A54zRKdZ9VSyjmfnGI9jnAFy2VbmAhSyx0PET4M2cYpwi1TmEK-ccm9NJXQH3ndU9IeKSNR7LEPbpL3VPfJmHxF7cLRUKsF9FzkMFpqp-Yls4j1kWKq6d9pVG4zbwIEtLI0eP8EgB9OGB1pOiTHnknL0p3fPrvt53XGMsj31MtmhmuK8senbxPKrsvIL1NukuxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=eGBrjDPnfP6sOBEr4BeaUPA75e--95qPODYL8ucM2kO2xMVOtivbirMoWK-_2J0tSOEqzrvT0-N80ywOD-6jK4UqhPIYoz49ZZjg0B7XiPWo5WHUxufLH45pehVkJvQyXE9b0DkWyttlKn5yTXI1wGjZCnrqq8j0jjdWfgmR5IMMzugcTn7lii7brNwZUn_auuJlIlRJvoWc1uGKO_7vigAndXR2YJfwDOpcOhlfOgStHWM5o9wvq5vVwbLlwtt1BYoRJwAZpeO0OIAD-lWxOjaW0BG5VTDN6K4SiuptOQ23MRSJpQBMxxRNpYr44tBfhOzE-_gMJfCKHUi4mP_W51rgrjIqZfhVmU3QDxwg_bvjTbxVPwBtErV8MVmB2fRk6oQYGOXMvLRWY2R5YLSwJCQ8v2QKme-TXgFkcBmrVavruDASgDsUWnr17XQZpykYG3a1ThvtKoTI9GAgyRnHA_xW8pVIVllzjh-mNSC8A54zRKdZ9VSyjmfnGI9jnAFy2VbmAhSyx0PET4M2cYpwi1TmEK-ccm9NJXQH3ndU9IeKSNR7LEPbpL3VPfJmHxF7cLRUKsF9FzkMFpqp-Yls4j1kWKq6d9pVG4zbwIEtLI0eP8EgB9OGB1pOiTHnknL0p3fPrvt53XGMsj31MtmhmuK8senbxPKrsvIL1NukuxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHGun3EHjehKW6jj_mYCXzXtCbfb24ZvEIH_DBXMTCJ5l-lYluzAgw2mPpxO_wwB8M2H39yfVfsO_QY2aA1idlTfgHANCwR0VL-aFE04Rz-g6B433m6Av0Y4_9uspqPAv8iC45SOJIcM8E91eXUsCtzEgTHeWHfBDxIZoJfvqoXEKtahgEAG4tT9DkXwQU1gSoY7yffFzPuaAgihkKBx2_yYo6IGj4VYuuJ2JsQXXr8Y5j9wsFV1g47805Y6UyYAPm5k2fmm-lXSYkGXQ28MSyH4GlQV3jzmIs3Yry-ODeBilPQwkQ7HN9ImQcUQICFoTOo9K-eYUtMbslMgw7niLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=v4WvTAgpehxuY7ljk1eR75yr4F_PLfzDjyZaNyQ6d-lfVFjuboMKi9cEAn8_P2t8kLzcs8cJ-t5QJYrR6lBTh3_3lzKk94x3Kr8dwJm4M46kDLHtIRVDigIG6lAcLfEeG5Nd4CN4a_QbXAC0eJd9mnzmBQYnf7OGCxRPcdf2c8Ri0cVdMbWBQj-2l7mXjAGJuAeqt1bjoXAX8-anpIYALOoyyCX0gUo-Bg7ind6Yi-HPVrDCdOqAHdBVdIE8YSgmbY4CkyXOhOn0DDdrhhuHfETQjA53Ap3tk3aaIjrenhENL0_CYhkje7_ivsXYKzbQ7uEtk3DxbRAGziuBCDLZlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=v4WvTAgpehxuY7ljk1eR75yr4F_PLfzDjyZaNyQ6d-lfVFjuboMKi9cEAn8_P2t8kLzcs8cJ-t5QJYrR6lBTh3_3lzKk94x3Kr8dwJm4M46kDLHtIRVDigIG6lAcLfEeG5Nd4CN4a_QbXAC0eJd9mnzmBQYnf7OGCxRPcdf2c8Ri0cVdMbWBQj-2l7mXjAGJuAeqt1bjoXAX8-anpIYALOoyyCX0gUo-Bg7ind6Yi-HPVrDCdOqAHdBVdIE8YSgmbY4CkyXOhOn0DDdrhhuHfETQjA53Ap3tk3aaIjrenhENL0_CYhkje7_ivsXYKzbQ7uEtk3DxbRAGziuBCDLZlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBUU8KRvatut381JZw0frM5A2q7PTy-R3LvmoB4XtLgEmv8ijhJ_4WEslj2IiSdl8RCmexx2E2sIX8_OLuqviFZUbJXTn6AeU3FRUa7OikcQjhU85sWESK46vhKkIL0MTit3bBSAwI_XvHOAI7-WXUUBn84ZxADbUmwP9YcD0ZL5Lqesa3GJ0e-NSuNNIV9O8EsfXS8Bq6dfEU7SMsYrCcWgjmVyl_8Yxd0AFdjqTOhwgcZIn7ZijyvUD7pF-Ih1QP9wOPqBlamzF6s9Pp3x5PPlHo-PWMEWI07u4xTOq2WZtHSup_eeaJ0HDGsSgHAr8-pRZ1n4HWgvkGnCbCmYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnkDVtob2KScl0WBt5H4CVGmwgYpDssEWGjjHLqjMWR32B5g6dDIfXKPA6P0oEnx_39HMI4Xi0TIULGMo6silJy6YgfykGeBRtCCjQr0FOQf2nOu0sI4LxQA7kPtVlfg4I5Zz-6IZkbpGeUjbu1MrrfuZo5y6DVrx_rGBtoVsJtfALZ06oV1jibYEwwln9jYY6IIXALTVZyiy38bC5lTFJsbbK2RDDpvA0kva6SbLcjxSSMAbCCPzMdbr7EAMOhhs1GCIlzywV9f3cqVVxscsBURiuIs5h05ERLBUlCX0YblJvwyjWEnN-DimzaLcYqllcdxiidIDTCiOlgbkDyyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8pXmW8gSbyJlZwN_2p-IYpxz3p1LE5oBR4H8UCjmZXOaKrNjHYqlfEK9nf2-Z_AUsmrehxzFqmWdy7XzCqU1RBSc6vZ72QQRmRBzyyKBUk69NozXzfndnGz-VPAaCMIYmgMLZP32sp0r5ZekLeV1zRY5WRp04snUdDPtPQU7-SPNwdK7GhGYOOY9-wZrcwO-Ipid8ItzPth_XxhFyxEVwplzxIGZy953KUXPUiu-gQjQUbeYpNiiScZuTkgL57FsXc1lRFVfjVzKYjhVoNkjSnOM_TsHckHX1VGEFltkG82Ji4JguejxJm59uv64l3x9oLicDQtCcWcTY2WhNO7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n02nr14DE2F7I8bil8ZmjW8EeKAwy2VbSkE2x-nHRH1c-WoNertmiiFoMo_XFCwKP6fxPwOqHk2OUKqUbzzfcHQ_3qEGnxu_QpMPDIhzle_0qs7fMhyiSrhvHAjU86ouXzcCD6pqIig-2rmYu2njifLw0Lfvb2Ago6jbTaQqqPGXPTOn80chov1LXS15m8_3eWzceLkPBrl7dKMbah2DS92rXNgqo3emnN0GHJfc0bIISrpIM3yhnZ-EUQYGecRF1uarVh5k4AP7xcJYLc0lqaUH14fIX-Y2_-Sf3TEBpRMxZHl7aMu-Q3S-vqslIbjHcy-dZEk9pmjIyzvVxd6DkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAX6t5NU_KpqC06s6t2W3Wo5PSIJbfdm_oSXxNdbtHEhB7DDpkONdp_ljylMrEGcgfhpcfYSjdfUUsI0jGaRcCryHEVydrYaF_3O4ZSXP9K0QS3e4OrdY7_NjPkUZr0D1eIjujuwWywCZ_N0eDDXaOxm0LMqkEHyiGZcep_5FWf1kPoBRYZNmCIGaIeEVaRa45DDuldiQjCJ8WWqIcXrqN2O9DiEt_swYFx3AnLM-hpi4VhVgRRuFeDxtgHS22WQpK0ZQ3UKs41gaPeIiw3ovmkayOea1xPxlITQ8rV3yCsoBxyrffnKpwm7A5Y6EpPNxl9Y3ZISW9c92IBqPT_qCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWF030HCgVVgU6qxL5bGOSSjf6qeTh-k0nlUZpLvlHdUlCVFBOMCZs1_zmyylEES6NkjTQMC0abjoK3AcsmpxNcSOCPlmlP-4YDmarhdvk_q3zc09ET6zhzr3BxOx0KzeIsEXhojVTFchA1JG9SnZw-QplROgzEMFx4iBgVkKOpaCeosZ7-x8VeWGRUjq2-lKemwq5159B-FJmHMBnB2SmDgiEHEqmDyDgXE479tcQ4LShugANq2Mm5NMwCrCsoW8eNn-NPz7LEm46gjhgcJlCOZk3Y75v5gESVxrryrvK9kiZTt3RqK9Shk1Bin4QFlicQFbNw3X1I0pDYuWNh_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmeng3qE3zad4M_uPhtO70d8rRDBVIxeyz-HGrxPo36RuWZgAr-Bb4nhI5YzqICLSGtcmrjAPwnOQJZg33avxq-3dodYMZtvdLmLfvi9cWnGMzl_miJ5BDJDUEwkFlkEgtHYOvl_hdGK-nK_MrRiCTIPAGYnqNt5HS_RAnFF9ceqi6pPoCD9882a9vEeT3Ng5QDKG1B_TlzYQ8fli6zA9NnBWaBQqR2kYSw3BkRUrNHn-mD_3N-Ov7W-AUa72Y7pC1CRIs631y87VT099aC8aqji9nP4DJtvYA90_PTXLZ_zR3yzeGgdiCOyR-qJ2g1zXOs04gPUlaXTRk2KzL_nYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=DGGsincRQPxEC3Ms1R3NWVbRqvLt3YxAGcOnhxt68IpX2repmMZdHXM3CXC94WN-aYGan0RsQAdWsXWRU6IdpGUK1EjRprQTHr8g5JZRs05rSfoo9LNBuN0SgCrdoTJCe-to4GCpX1jptLUn0DhZmpiVl_LHD8yDJ4MfkGk9KvUQfpmnlGaF0peWGRgmGh4Emq3DLGi_XECwK-7rIiF-ze9CxkonywONZf8MilrtjmpX-f-lHH_3kQCcyNtrsPuI01s1eE54wOVQyiL6qT-QF2dA2h3sCmZfFOOLKqmd7kWCnMbv3U54mw4pXUHXs6vgoj9K1JIHMvvcXDaE135vsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=DGGsincRQPxEC3Ms1R3NWVbRqvLt3YxAGcOnhxt68IpX2repmMZdHXM3CXC94WN-aYGan0RsQAdWsXWRU6IdpGUK1EjRprQTHr8g5JZRs05rSfoo9LNBuN0SgCrdoTJCe-to4GCpX1jptLUn0DhZmpiVl_LHD8yDJ4MfkGk9KvUQfpmnlGaF0peWGRgmGh4Emq3DLGi_XECwK-7rIiF-ze9CxkonywONZf8MilrtjmpX-f-lHH_3kQCcyNtrsPuI01s1eE54wOVQyiL6qT-QF2dA2h3sCmZfFOOLKqmd7kWCnMbv3U54mw4pXUHXs6vgoj9K1JIHMvvcXDaE135vsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل کلینتون :
به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.
اما قبول نکردند و طرح رو رد کردند.
حماس به دنبال ایجاد یک کشور و یک میهن برای فلسطینی‌ها‌ نیست. فقط به دنبال کشتار اسرائیلی‌هاست.
🔺
بعد از عملیات ۷ اکتبر ۲۰۲۳ ، اسرائیل ۶۰٪ از خاک غزه را نیز تحت کنترل خود درآورد.
در تاریخ ۷۰_۸۰ ساله اخیر، هر بار جنگی راه انداختن تا با جنگ، سرزمین بیشتری بگیرند، بیشتر باختند.
🔺
امروزه در دنیا، نه آمریکا و نه کشورهای عرب، هیچ کس هیچ فشاری به اسرائیل نمیاره و دیگه سرزمینی به فلسطینی‌ها تعارف نمیزنن! هر بار بهشون تعارف زدن گفتن کمه، جنگ کردن، بیشتر واگذار کردن!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTzmSMbogNOhSf_vKFJ2eZ3QBlc_ANeS0YnOx4kriq2Zszn1x5TBwR8vcg7kYzxfoLLcaAnEram4nLBrJvBwf1r0hfH2dv54ga3K6GSlOo8jBwBDf5sUgjbJOaHZXSRP2xC_Wap1MREs-ffzdFnXHImzfi-vZVl660HNVuDR7YyNlSzpG5TVpfZNctJYw5CRMOi4Hs3rCdF7nopnVPqdjAU3l52kGGNJLttjjdNVvyhGEUtMCyyRVcCHxEpReeVIy4rcXHBNL2gf-7pRBcpcwk3WzHx1vfX8oOWNNHGh-1QRZuQIgMQ3GUkNVdCCfCHlxUkAd75IiFVFqcA51nCafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns8t7e43Ho32IgzpwsLUwMA3rlEVJGNw09ml-moCMl1dh1W_Za5rkcqpoXhfNzh17twf6OkxjDAOjrldt_opmTXIf9liaisOkFxxFx9vq2mparLr59ESTT0kSlfF17KQ2AwL9ca3RPzH9nmUHyFQjMlRrrRg31m2WHpGaToHjtPrV-vC_GbU7yoc5SqT4VeHzyGoQT74402ASLNximH14QSqjeJIFoGsYvw17-pbPUYZFz_pxrK8sRAhoOvF2Pzu9-g0LsSkWJkHAair14aGiOjhPUbdZvcjiXoxYa0DMPnIlm4Z8p5X-7RDm5h31_S_vx9fjgEexWz93Z8ZnUz7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=I-eQeVhweP_ua60qXoLaGk9uXzeCMvG5CMdUquySPDn9NPbrfJXirobjRrPG87rNrGFnHZoGXsMQFR5KP9FDvh1NxqLHJTVU2cwJO-R2v6EQ9N_qCs-zcsN_CP4iIhHR4OTEBksP5g7ylZ1M5iXptdi8lpqJBMEiKtO8Zvs_n2DFt-nathB1zLy4R8zk5qmeYnlgUY2uV5US73BDKFFzHuOYWqKthawmoZuw9tVSwebE89A7Gt4Tt30Cb6NeiKDN3S7s3-JhWnW8PBTQzu7PkIg3e7kDI_Qvg8Xuj4MyJeLi9o-DMa-gss1EmuuFR01E8MSkFXDtV8OBZ3uUKGA2Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=I-eQeVhweP_ua60qXoLaGk9uXzeCMvG5CMdUquySPDn9NPbrfJXirobjRrPG87rNrGFnHZoGXsMQFR5KP9FDvh1NxqLHJTVU2cwJO-R2v6EQ9N_qCs-zcsN_CP4iIhHR4OTEBksP5g7ylZ1M5iXptdi8lpqJBMEiKtO8Zvs_n2DFt-nathB1zLy4R8zk5qmeYnlgUY2uV5US73BDKFFzHuOYWqKthawmoZuw9tVSwebE89A7Gt4Tt30Cb6NeiKDN3S7s3-JhWnW8PBTQzu7PkIg3e7kDI_Qvg8Xuj4MyJeLi9o-DMa-gss1EmuuFR01E8MSkFXDtV8OBZ3uUKGA2Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=siUh8aho6_BWq8YDdEu4AAGo4_s-Zf5MwV8Z9IGSlKfs0c0ou5shpaCxiaZEvE4SUw4-CncQgdn1N3WzVk7QGXHJWJijtYIQ4pZT0S8o-rXTGLKnHclBdCJ7NmPlqOV_NWJVUZqYTAjIvn3H8pCqHJVJc1BmVGSIv_PA9jX6bZRm7DDrjMWGxd2QFN5oVUiRNT8WO1NIlDFCuN1jG1Im57QGReb2AHWTnKMWcRlrjVr1NO-htbyUeWEMmu8BabullSwY8GWmx2K7m4FvVlRSw3UrvJSYmqaKRvtpolc_nm9sIqWEE1RSpdycSORcPnnTlt8CAtMQubnL2nymlfLakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=siUh8aho6_BWq8YDdEu4AAGo4_s-Zf5MwV8Z9IGSlKfs0c0ou5shpaCxiaZEvE4SUw4-CncQgdn1N3WzVk7QGXHJWJijtYIQ4pZT0S8o-rXTGLKnHclBdCJ7NmPlqOV_NWJVUZqYTAjIvn3H8pCqHJVJc1BmVGSIv_PA9jX6bZRm7DDrjMWGxd2QFN5oVUiRNT8WO1NIlDFCuN1jG1Im57QGReb2AHWTnKMWcRlrjVr1NO-htbyUeWEMmu8BabullSwY8GWmx2K7m4FvVlRSw3UrvJSYmqaKRvtpolc_nm9sIqWEE1RSpdycSORcPnnTlt8CAtMQubnL2nymlfLakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaVJ8XhupYknrZW9eZ-bhtS0wdqTTCS0bAeBPPpgkGOwphamf_prrIMK4jSlaFVvzIGmMOifI6mtbtoIxhCO2ByS13toNOspzfZXZBNG8YrAe9wjkvxtAHcegTeSzWqtqRZy0ayxqoE1zpD-UUWhsfuh2-df5yuyrYNUrfen6r025DoVACo_KTa82pzCi9bjj4tgn-BlL50QjXQWv9245xRzXW4eSPbBd4wvGM7ZAC73UNiHMPoEf_oULLl_BHam-YIfQhgP4TCAFvZNuA84mkJC_l75sxLNH_ch9bCjg6lLf-F1vwR9nKEuOSVwwk7DuxXXQzvswUNbguwLbVJS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=VDmB0GwLrTASlySluNn-ApBGbB8k_lLLwRx-BhD-OwPfWxvjTU_8yTWuQFIfq3Ds9yg_5djrQiZw1D37nS31JC8T7XfjUjv4OIv66JrJI6uw80qpZbKgVJK3F8OkMVaAP4BsRpew7o-Rj1iNgi3kR9FGUVwNH12H4zPt0peJbOiiRVf4jgmcVwrBAW-H51EelOTY99p-RTMFc623yVZTTfMCA0bg8UREG5kOpGD0X75kd3bJvRspgUQusSDa09xwl4XpVwBr6W2xHcsOlWn2lLPmpKNFz2pVHZ_clie9v753Eh7Cq0wX0t-h57dUJztGSAfE2eqebg5ZLIWBmxclbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=VDmB0GwLrTASlySluNn-ApBGbB8k_lLLwRx-BhD-OwPfWxvjTU_8yTWuQFIfq3Ds9yg_5djrQiZw1D37nS31JC8T7XfjUjv4OIv66JrJI6uw80qpZbKgVJK3F8OkMVaAP4BsRpew7o-Rj1iNgi3kR9FGUVwNH12H4zPt0peJbOiiRVf4jgmcVwrBAW-H51EelOTY99p-RTMFc623yVZTTfMCA0bg8UREG5kOpGD0X75kd3bJvRspgUQusSDa09xwl4XpVwBr6W2xHcsOlWn2lLPmpKNFz2pVHZ_clie9v753Eh7Cq0wX0t-h57dUJztGSAfE2eqebg5ZLIWBmxclbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=uhOLHj3127KZmDhGl_4O0PHLN2YvSu8twvrz5rm4XYff-Gmy6IkW2ygXkbYaBdj2-Q4761W0O-JOQ4zk75TKZ3NIttNPHJ7FQo9Bu1ZyiOVfPZuNgR9vkymXklgudU95n6O2Gofj_SIZF48O1yo2ykUiXltGPJ566kb4RGZwIYwQkgD5nlBxs4ZjCencW68SYtd_B3rCkxPi7ZZ4RaT2PCpGVYBcHWAy3grFKcYFa6SEzF7mkGNWCiaKocaiGpYiaRJkTSxd40pFYV8aDyJlXjRU-xHXjMsFcgY3RSsic91enJdZ9U6RobVJLS532l5B8MdgiM96-CGPQVqFnuQhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=uhOLHj3127KZmDhGl_4O0PHLN2YvSu8twvrz5rm4XYff-Gmy6IkW2ygXkbYaBdj2-Q4761W0O-JOQ4zk75TKZ3NIttNPHJ7FQo9Bu1ZyiOVfPZuNgR9vkymXklgudU95n6O2Gofj_SIZF48O1yo2ykUiXltGPJ566kb4RGZwIYwQkgD5nlBxs4ZjCencW68SYtd_B3rCkxPi7ZZ4RaT2PCpGVYBcHWAy3grFKcYFa6SEzF7mkGNWCiaKocaiGpYiaRJkTSxd40pFYV8aDyJlXjRU-xHXjMsFcgY3RSsic91enJdZ9U6RobVJLS532l5B8MdgiM96-CGPQVqFnuQhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۷ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۷ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqKoLXyHC0LubAKQO1NjTheGlmW4d_PCZA-v6QHiUUYdCbIwd5PtmAx5tbzrTkviuVKU7CidO0T7G-eYOg6ZYZq_CB13Fk8jIQC01dtnV2qc_5TkzFwa0zx525sDohPrDJPU99DXZ7jou2S0SXsbkspBuuXBkohUKJygEv2x7tcxI4WetHnoKTexHZqtNaBjZRTHLNyhLOdTi8je0hPk8Mf1-3q-vW7GjZfJc5hJc4YfdOTTFrLNlmyy5x8bnp9uteO4f1KenfGBuqUVhyYqACZYfn74YEIJj1sPDmjj7N18N_85Xert4-fsRZT3nSPh0248bEnFT6xWwrIozt9dKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISIZYjYhTrGpb1Ycz9p9BngNPBYFADtvVGwQzY7Za4B2cMJxVCgv3DvRvV85wnphDZOenM0mGINgVm8_AggCfmIpfPAJCmUKK9TDxfRUqBcCmlNCm5ojr5iBk30k8PjueZPp7lVPlTkb7Eo1pQtWyWEaKwxQPUgUXLf7BmiITRennQcb4P_T5k-hx9BemARNwA9LKd3pXhZKGqkRrZGhtdTF9j35e9lhJcucevNmXLl7lxQvUpUYdFOTBes5hFenKy0Oz7tJ9FaAuBn1MdQTYjslRjyvJ2Cs-ODE6vxYm8Nj9FCTTGdWG1EDsDw9Mr5Pez8acPmMLSWPV-TQQmofTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
