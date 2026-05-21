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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8fuiwl9SurRB_3zT4JZT56EJvvFoFy3q9ChJf1Pu__vtXqs05Esp1HZxrWkuT1j2wZZJfGsoo6YoBeFdBINpAZbyfhY3q7ZxeMzs3JYRDtgQ8mXewdgUDSVgGvxKqCkQ4u4Na1B9xArpK63m0BswcwavfMLyh4AFdQQ24LUL6Jjcf9TMJ-Wz51tSTztXUfHsFiY1-Y2DEsNxU4SZetF9D6nX4gWLes_fVclwDfCyMUoZce-DY6nYsX6rZF1Tb-p-vQ3iaCqeAEiNgjIaw7raprW4fce_bzDp499DTJREtJzPKXooBrjrYvaee2B-eci79ZJ_8LQQ_ZcJmFXajLHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rkskz-j4x3cRiKbTbaJyCtRUeRPGIeCeNrQ1Obnz3JVvkXpUbNkI-T_R59PmwohAwW5eYJbiy1bEhhkfbZJwEZmIY0eHhUV1Fl2YD1dGh8C9BaFABG3iSziU8k1Yergh8d7oz-ugdwsMuEKdX0dfpEmeBi69Xns-aLDMcr8rbK215B91_aO7ZnmewjYbTWqdcgYtC5_fHgWrXyeJ04hA2GQOtrKWRfr3KV66MKqygqKiwXjlCaVQNAaO07lw_VlgR3vzlyEL2sH59Ypqr6HfC9VULLxSSmaTeHhIOASjallhQ-DGZ53QgqyPECJkptIKXYoJfHFWmcELkYbdwPT0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdO-yK9iD8JWb9aY2Rvs1tKK1QpXbpoFBn9AVJoq5qfeTqvql6x02inQJ9nBW88Gd9INR_vSZITiZQy2Iepif_Rgj-jgCybasdbvdK7O8GEpWzrd-XBdFQIWfWw0P8tEwNjZ4CI7ZH_q7vVZ-mfMaGjEodjTztEaiGy4Hs6RoB8GcnZNZsIzHaoBWg05AVtk7P6r56rb71xZJDtCcrwzfK7da2ZthrHJnbklsq_1dCWtSZxnX_fz-MMqLKBJZ4LEppefDY1s8R9S6lOg2oLVq68CUdmKGfq7Pgu4y56VHni1ION6sBPxDH2NtoIhnmVUJc2k-M7-t9_XzEXChQnwGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPv5GkEQVcnSp45AAGsFzLhN_tkDGRUVNW8sIAcBu1M44BCj69DPb86zLvShUitjBcBLvJD4dxhN5qnHlTAkV4774riaDNet3cOoTcgMINkass7dkauR5mqXC4L_SO20-tgZdiw55uzBoWDw5O8u9pUGQvaVBVj0DxNHROkrP8JfCk4OixJAuSJGDxUgUfqXBPxhSV9EEw5IvyXuzose4jHBg_CN6wU7Nt1-n1jvixP7nyR6KS2mQbZICOK9zsDRVyQ_CbS-gi6Qj9VwMrZBohutafHmLfZUd2Ql3bGnmXbztnY1RWgIg16lthapuqZIouUyivS9xv07nD_2nreapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOO_Ch2O41oMd8_ZH-fIuJr279uVNr1geQBDkag_x_cMw8Wa6Xy4Wd23I7yRhC0-VdiItF12TDj_-fylXBWqSUMSsK-bbdjU6Mhg9yadOh3i_UThadQQnj3C47x6wiTIy1xk6sR6Fa0AlN6djlMCw6W_APBi4W74NCzJ2CP8ZdxKe-EgMtxCl2H6NuUy2xy5ky6ssaS2UjIBo30eZpAm-3hDCO7wZNStL5pY54P2YG7mnmjpzasl_qScILJjPIg_6D8FRsFkD_h_wG5uMvu_cAKo8EN1SzVhwyqt5LhmzSksrsW1CEsGcBAOicfG7ZneYlZ1gfB5GBoa7Uzn1Wi0BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJIF-yZq6Rcd4UV_HIz63iWF1sxbIH5Z00m11DDYdL94ibfDyT74G6qyS5aPPjgw9vtUocI1Nef4OBWrW45kzj81KHwXqw5uE_JAI6mOz_cLLyN8kvBbP2NnLzNP3tRGCZl_5Ar9VRE9feGkHo2YuNbktTFlq6EoYBtE5GXCiCB2RPVUrEPvGJkfKGgzSqWwdHrh2jmf-MKy5X-A_gJMEKLcDhLPRI8QD1Zb3p9ZDDl_2TaxCcCFx1XQBhC_t8vV04tG_cughwr7oa_EQKGxLadx6ABEjLP61PZg_qTOFeSuSQuIv8YensLMO9XzmIbjmYq6MLyRBvU2aEryv_vVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTdMCp6ASlvixsDDZm16b8ebykhP89RPuk6WUz5dOKa9RiPj95vrnuvFgqlR8WJVFL-uIoNXSuF2rSEKsWVFDyckcLP7ydSknO8F89zqUZ8-ahRzMFqIhLkNXOpkzjeQBNYY31UKUYKbOTYjP9zBhSoV6bsu065750eScbiUu6trJSCHwAIYhYvuMWX8NGBlqUD3W-NCiwYQBYoATeMiJvZOGsjT5UJ6vjjFHazZD2NP3ltVP6C7Eia1rQ0u5qD6Ee_QLk3CDtSEMQP3LmoPMvqG-uirCdN8ZMcsr8FxyeB98jj-8HMHTtkbWZ-ovvYpcDnya95SYA__Lk70pdmAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkvWrEYqg3DH_dtMrb8-6DZYsXSIE7B8MyTsYaytvk0ho42CzEbi5yFS-mQsyZumS7QdQnnD5Kjkxhq0LWVbXS-rDMOoduaquG-PJMrKnH7yYKhb3hkS2tW-QhbLJ_I6Y3Od5l_27qmX2432TCChj-Yis-XRFZU73Zqd6pgzJYOdxqvLch7Bkedk2XUK44MpwDijVNODRmq0I5Wv_Ks8WQa0eItKKRTRd9sTix0FPUc9Kbgfoamq0BnBQpt24DeoMnokfYDFzeJCz4VqfGqFOiXVSi1Y5TKY3DY1LyR2f7nNggSi7NIDIIHntOn5eQtqMg9JMdkiP2RkxTNqRddr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRBplwyQa4mkRVszeIGTApQA6mpApsl2BMLEJgFmPqzbHFTVDu0yYEc2PuU4-0buJ1ZA_u2XvUxF7gKkK_tBBdhjFySn2Cvrk_8dW2Uj7vv_cLTUlHsIVa_5UtEJok6OB-KWF2SOFig8f9ZS2VWmlhwC-TuO6dd0HiNaJczGqoyo0Wjq3C89zI0zl3YfrvqwpajDSO2KuLYsJGgioUlwk0IeWKpL2eAizaSepkhqtpnWDnuRGY1E3k6o-wNXMtiQgUVbsVtBGBYZGDLEGw7K83ezsIzqU8VjWGIRH9DogeLZ40bTpJRAGkx37SJLhAPK4Q4VQMizmUxHkGuESPdgUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=Zws80HSkvfXuIVXltp5t_YXvU9JdL3Baez7fQXsblvVowleLhg1YkYaYaU5BZE8DraIsN6MeXAQiWdrqkYZKMq7dklc36sFPhggKbgGmpx-61LQ9jtc9vAsVmszp001XGFBsIbFqfsOpP2D5pDxxaj3wgIesmu8_AORvuCqJBK5RkXe0hl8j1XwdPXJw4dFlHhLp-A6uuri_fV7AjwmuSeon4cXTK4rK0iRt8RvPM3PWpdd09KpQAnjj7GQIhY1DuHsuIqEG2LG6LyxpANYYYdseW6kFbwkGW2FrHfmCReH2l8__nEAljEypH2apkacH5CiXeL-dLqcdlsXJoLtWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=Zws80HSkvfXuIVXltp5t_YXvU9JdL3Baez7fQXsblvVowleLhg1YkYaYaU5BZE8DraIsN6MeXAQiWdrqkYZKMq7dklc36sFPhggKbgGmpx-61LQ9jtc9vAsVmszp001XGFBsIbFqfsOpP2D5pDxxaj3wgIesmu8_AORvuCqJBK5RkXe0hl8j1XwdPXJw4dFlHhLp-A6uuri_fV7AjwmuSeon4cXTK4rK0iRt8RvPM3PWpdd09KpQAnjj7GQIhY1DuHsuIqEG2LG6LyxpANYYYdseW6kFbwkGW2FrHfmCReH2l8__nEAljEypH2apkacH5CiXeL-dLqcdlsXJoLtWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEW1hzSVrainpPjRISZkwfBFxw1gtgmKEGpM8qPB2OUj1KF15suiMrvzuw8QPaw3t0GL78txQXSd7FElNJMsbtKLNVkHl9BUsowfd2krJne5WMVzdYiY5e5delR-lowIK5ZNSrj5N_ho6I9ephK4X5MxV38F9Si7-FqeSqngB30JG6GFmANsLJa-4z9pT_K0QK5uy2Qd643igKn4skCYWKM9GDuDedqSzTnzRwf53Uy6uKq3NcnecEEsZD8PcI2xFmZUDI5WGksNghi1gJmzphVvF5Uee44MDqRYF5TdmQdLH60m4_7l2RRddyvTzS2bMYG0y1C8ZEMY9dIFKbf5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzH1tyfUw46WZr1DAgJQa26xRsLQWKkA_4oM_NPqPWDowtk21iUBq0qLavekePI6FUQZJWrVVq6MAo_M8LvQJK1fhxwpzhVgd0A7vbyZZ2-qtVhLDV4NwoyIgfmWV0elvUL254ZjA07f6qXkikuwoF3qxrtg0EUH1UKGQHPAEzJ9L51iIOG6iv-8U2r3RzMyj0lekTN6_KhStEE5nXzke-7MjNRXun-vy10VaB_9tMMvuEvuu2zlsMLXx1fF3Ob05dRDzpEVyXs5s3H33RlqVCIswc2DR8KueMmggCdxiDo9s5jLdVay4GN_emvwjPf2TnAP9pOOJRJoHV2AglEIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVac5PgSWUjLm2W_zhQ2qFPDDpzRel758FVablwx7Kv4A968D_xdtPrxCiNrigJexHqn2ElmudmVHOvmQv8TZ9-EpdcGAR3IhsYGPzr2d0S5_orGzh2KIbez-6H4mU3g4hpVbjC69JehbdK2K0IY0aKPOKrNPFp6c4yl9Fjgq1tRFj2JWNwtlWaDsUUjul-bexXFDjTkTtb1Q_Mye5xIQPlyAEWmqbUf5MmkHhj_RenglZaQXruXIpTfdEJILU1OxDUtWfp4pu-HulrBcUwV8lzScQCcDmMQEv9ty03DFeCqSPKUdK8Vq5JlNWtE8hnOAfcer3DZd2mPAZ4s1RlZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhRBsI0nETuwpMhGodXiOvZnh8WIATdC1ut53sFYiw3CsHR-9bZqkiSUi47Pl7Nz8cCpSkVTSnNOGw0n-HHfgEDlAsYP8KoZWthGmV-IrweJmekgO6B_puOLNYJlveEOzglrxEb2n8psq8aOm92tKKcZb9K00E3yw4gChoL2LQkHCOIudjJ4LS4Ik6_Y3aeteEkZfzn1FaNpr7D8LbPK5pToLCy0Nse6AUvcCnGEDZKlGHyuuui9tUFbAB0uTxHi5cLdgCeJJebA1yq1eLVSrQk51foWBwYQnAEHg--bqC9LW9assj_qmH7jBr1GzcbVyd_jOuo4CZBNanhvIjmu1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=IxHfztgl6B6pKTm6ACmu3C-jKM6o0t_AJb2eFC2YzsgHoeFLn3u9k_wRNqhZBcgDbNnJLgGVJbaNEb-KCgd4NUey8uXk30GKojFq3KcZDCDdvQb6b6LckpiJ0SiVN1ce9vnkwuuwyVTa-BWFQFoFKXSmdIjx1rJjvmk9kzRUB16BDxHuwAcSg0TrqSIfhFIx72SrsmPTQ8_RHo_L0E0sIuJYAT308wEyZhxQr_09GnOCsWDD1eeSRdh--ru4LRUR7gYb6XXLgeWASFegTJs1a7_39Y3Z8v4MBzLUznYSjKrl_XJHgP13m2gcw3n7VBB5TXerJqBQkwI5rfCTVeXyDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=IxHfztgl6B6pKTm6ACmu3C-jKM6o0t_AJb2eFC2YzsgHoeFLn3u9k_wRNqhZBcgDbNnJLgGVJbaNEb-KCgd4NUey8uXk30GKojFq3KcZDCDdvQb6b6LckpiJ0SiVN1ce9vnkwuuwyVTa-BWFQFoFKXSmdIjx1rJjvmk9kzRUB16BDxHuwAcSg0TrqSIfhFIx72SrsmPTQ8_RHo_L0E0sIuJYAT308wEyZhxQr_09GnOCsWDD1eeSRdh--ru4LRUR7gYb6XXLgeWASFegTJs1a7_39Y3Z8v4MBzLUznYSjKrl_XJHgP13m2gcw3n7VBB5TXerJqBQkwI5rfCTVeXyDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcgQMJXD3zBkmcDwJUpsULXaLirpVIH0vkt-jEPaOLU6vBBdb7EupZhZVZxZOSVuiVztfzrO7E1Gw2OCngAb4oi2E8UnEKKYKJ3_A8XrDg8y26zwCTJTA6ECl9vKLvfJPd9laSjBiWdLWeO9PJTe0xweutvdZSX6J7xQrd8VtrJ5W6bJuqNDqJOOmm9AiPArJnJGf5Dn83dxIzvJ-MftEJUzKQKBvBqujtl4BxxJN6q4I8rSJ7FRj5UDgsG94UhdbKvIPXggPAbC5OWTVCj_ELpo6BK2nvz3VvA6hG3qsCh2iSurPf4flNa6cvydIwEb1uChX0dwq4ijap8ft4V7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_7Ro3d7cA6d81t5wfmysH4xs6BhW5wuG4PI3-ckL11lRoRS-FXYDp-8m1-LWXXgWSayEh7YiWzjcZXEMWv31wykqNk7cj8FOeHCHHJ8sqmqPttpRTIkA4gH2P8oF7rq3XqtQtD6e0uuNSBNxu2823ZAd9iclqQ8H1kinsjT6kiaXUeNC1disgAUf2n4lu2R1kxX-NM9tezxlyjKI0TQlGB70Mg9pzTjqXs3ltn6pwRQnVreado6IJwqQ9zM1Xj3x24nhsB_ZXJR5LH6A8RfhOkOBKEOV1VnXFzflBIurY52pVJbBQtgBcGlRc0wM6WnMM3FKdqHFpUiVKfgxLBMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8R00NVzXo11V7RjqJxB2mXz6OMhbTrU0C_MoNtX0Hxu6K3MhJqVhqjlvZj7S0DDddO9c-VRzCATh2Rf1rGnjFQhNZX8g-2CgA-bO3bILtU-CxZHGq3362xCU663wnKDLBJCY6G3YdtIwz_cqKLi2rSWWAZyCCK0nOETv2J5PkK-tqu1hgIv8cpNYK-2n1GzFlwJtGcyyev0AyQX_W-lh2omAFn-FGgxcNEiNmumLdintV1nPCFPEUrz86SYZrdaB4xgrnn3dHo98dalGnI9MmEwE8oT3quV1OfDUGIBHUux-Vayc2kSR4nF4fmDraIjJ_Oz2NqmMBEODZDcVb-eRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFDvbC_6kPrNaM5ssB6qKSl4JJLMclrmqiT15kR_13F75g95nNhpj1pfM0sFE50cqwIFn09FWceZ_DdG2Rl7OiCJBHBVITrjDShw441rE4LI15RroypGZ8bbKIN1-kCkXOs_hY6D5ljThGPVxSaPFnNgA5aJt5tCF8eZ-JLB3g8IDnuA_E1WHlMO00QLCUzgtrzpf_Fti5YYgGg7z0UOXMUS2IO6sJm_Zac_97LZ7w-mxm3do72UeNht9JZE_XFTns0QXCHftGWubwijnZStOJtoB-GydPGZVk1FkhlqolInHW2gFqSECL2z9wScoHE-qAKtiCT1tXcwwQut7W3fYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OrYxFCRCnIWFIXcwtXDSQUMlCFSJHVV_BMZrDFPfs0drcQN9OEoOUg8eHEhcW2ceeVTPK5r5qJmOjyNiUMhpY4EGQ2mIW--eP8kfvE5BZgtzB_gBP5DimZKFmBFUXrCrtRTyn1IFpXpZiE_KwC8bXkYSe2FuuykQ-RHhkspPB3oogxJ_LdiexEY1wNGhvtWmf4edaabsUYEFPqXn5Yflq6wf6y5pNQjNBURTnBc6UHN1zve62QdfQ_fQrDT1DI-dxR5CSRl5aEK5I3mJmycbi9LxWGcxMaYc7ryeWR-hikSAOcuBVN_Qk8YTaulH3pmYL3YcMIbklfGt57kk3HIyow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OrYxFCRCnIWFIXcwtXDSQUMlCFSJHVV_BMZrDFPfs0drcQN9OEoOUg8eHEhcW2ceeVTPK5r5qJmOjyNiUMhpY4EGQ2mIW--eP8kfvE5BZgtzB_gBP5DimZKFmBFUXrCrtRTyn1IFpXpZiE_KwC8bXkYSe2FuuykQ-RHhkspPB3oogxJ_LdiexEY1wNGhvtWmf4edaabsUYEFPqXn5Yflq6wf6y5pNQjNBURTnBc6UHN1zve62QdfQ_fQrDT1DI-dxR5CSRl5aEK5I3mJmycbi9LxWGcxMaYc7ryeWR-hikSAOcuBVN_Qk8YTaulH3pmYL3YcMIbklfGt57kk3HIyow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=vYbxGtnjZ1BZ1oZw84CO3s5i4o12ZvQ-RtvfXaDpP-9KMkwaIunCqTRod-UxyFSkhT5lu13zO9-2kVcIWLCU-wVDa_bHJcBSibx4E_VA9v4pLfI3dSMfvGnmQed_vOw3Rw1xSrft7irGdWOumcsaNq2lko-u9pnfRpsjBPk4gW0Ferxx_pfjhvaKzC8NMddT9KuELo_ofwuBZK3t5O9Bx521iMRSWkbk2rF-_hTJHpi3vCkSgpbCPj7tpGGR1p746nvDF_Y64gsXAv4XWefHVpt5f7Oxcy7M271c8V-6Pz9X4SaXiWhEJCTrV8isSJ2LedMK3qJwfzA1li6LEP_4Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=vYbxGtnjZ1BZ1oZw84CO3s5i4o12ZvQ-RtvfXaDpP-9KMkwaIunCqTRod-UxyFSkhT5lu13zO9-2kVcIWLCU-wVDa_bHJcBSibx4E_VA9v4pLfI3dSMfvGnmQed_vOw3Rw1xSrft7irGdWOumcsaNq2lko-u9pnfRpsjBPk4gW0Ferxx_pfjhvaKzC8NMddT9KuELo_ofwuBZK3t5O9Bx521iMRSWkbk2rF-_hTJHpi3vCkSgpbCPj7tpGGR1p746nvDF_Y64gsXAv4XWefHVpt5f7Oxcy7M271c8V-6Pz9X4SaXiWhEJCTrV8isSJ2LedMK3qJwfzA1li6LEP_4Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzEJw6ZotcSW4Uas_9LDQAb2VjHRBAIuspOXv-bmCRb9t9xr_TXpkoeDF7PTx8_Lme9T-fY1bjqTabg38IW9OX3hbiNJEUea3pjkAiAVCZWAEnxlmSwAvnMdtnlPhJSHe9tkqZokOU0qGZNW9Bzh3mLb-QDgXqEgJt5xON0Lg2A_vY4kPU6mLhikN8qda_GSzC2ge4i7lkq_p5CJoF-EG_RRJ0DG4HuEu9bMMCkehMewTdqy8hXdpIVGtEslGXe6WYZvOV2rHMhOUPqRlIOhe09LernZKhbxFJj3IChLWnfCIrxFXjzy3B-WWMBtx_2Cn071RSqd3wHoVGlYrpUZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2yDXHDbWdFQgbH4a1pKHpQdh_56LJOHy1tOg_6nCa0kY9DCtc5hEdCh0-A4rpOUnyNdjEtIxnsR9NTezrTVT3ipgAGlJUshw-iALe0DDhwQksI7R-4Gki6E6GF4SiMk9qw_bBQoa8uHcYjLVB-ey0GcNKdme_-SQuq60vAi36fVYOOaKEt3T7DEUPAaNjO-Bk36_yL-xsKyuBq54-C94GC7uiUnlCv_CK3n_Iau3V6VRvpNEsRiVZ2YVroscREwN0tuf94kdDBoibST2oqxrnaeCxxcmiOp3we-D0P4_GjRj_nw8OVSOs7HqyS7lH1hayubpmBaIPf_RCW7d-IVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtjnloDKs3g_kedR4cCJ55pOsl5m0050kqw31a5Q-ggYSUxTktFIshlk-LkRDe5Vjzfz0p9CSnxvMZ_oh7mGi0-gCSH5yUWEtr3PhBmFKGjdLDbDmSncfC5k8EhxBIIaf5fg9rvDaXLvX-51CCYGGYQIpR7Yj8AVFUnjomCW9KvqfGkVQDOIKEfB8hSn8I3HzGfYPL0YL_Cynn0lNumzNALLMiTCv_cDgqJoRLrlxWPNnKiNOrJ-cIEvrMpamHuJLCbA83RNYaVtC9N4ajIQh1sX1dIXHvk6ZF4y4usUtpfIlqC6XVfTGoBsWlySKJCDJFlQt0lKOFEM1QKpaMtsNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msJJfC9y8e9dcszkXVMaU7IkCdu7QwxZLGSFhxC_AMK8p1jiI1GDgaickK4M-1INBW6ndnD4pSMZMUn6Kqg7lva9fxBR_haZVR-DJudUumX8wUVqvLgNdOcgo40FBqdnex5-j1nb1Qo2O-3Um8F7xBxrjQxcBtvsPpvdnApK_V7hagykyXH_mz013mdLr0WO1UCohEkHjDdGxSFJC8JWIqD_7SMZmmEB-6fcWBcRtFVEp4nOF1qeFY0okp2SgdmD6VuvWE33dYZUbgTjVyq9b6NnnlXLbbEWmucM6pIiUIkLXpIVHkoSX5uL4mUnwvsT4id57bi1jLWrwJt6V4NWyA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=DLqaNz_bgjGsdF2m1ioSRkG_9MmIG0ERfrW7lIbMTYxwW_QshBdpXuZ1yBZNfW51-c1poPcF-Y4UKdAG4mxzsJKS2EPwEsYgFrpjLW2DFzIhDUaoc6Y_C_GatLAZVD9pBMv96eMZdjRZfw69ft-FvwO-UmGkeGhLPXQcR84H9TeYB23IUPDEZSomidQLXgTVyhF3nThxzC9G6ATb7GXYYpSrOnlV2G8BkmmR7a_1LO5XcwxqfuOFvs_jMAO15ku_NJCkkxZdJdHAPAeiIWdCxIsE50fCKmcam58VPvNLph6sYcoEGOij_BW0AlLeY9qceQcVXO0maHaWI6O-Y23VlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=DLqaNz_bgjGsdF2m1ioSRkG_9MmIG0ERfrW7lIbMTYxwW_QshBdpXuZ1yBZNfW51-c1poPcF-Y4UKdAG4mxzsJKS2EPwEsYgFrpjLW2DFzIhDUaoc6Y_C_GatLAZVD9pBMv96eMZdjRZfw69ft-FvwO-UmGkeGhLPXQcR84H9TeYB23IUPDEZSomidQLXgTVyhF3nThxzC9G6ATb7GXYYpSrOnlV2G8BkmmR7a_1LO5XcwxqfuOFvs_jMAO15ku_NJCkkxZdJdHAPAeiIWdCxIsE50fCKmcam58VPvNLph6sYcoEGOij_BW0AlLeY9qceQcVXO0maHaWI6O-Y23VlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=NThwzig7tR8U5n8uHVJAACjSL72qrX8bhHGRI0F3B4XDiqRiJPOu8L8xzXBQZi0YwrGXoQoarZMxzBMwBuhKpIcR5AxSgNookVgU-e959TenPMgZDkeRFWETx2yh-61gotXs_yA8gnCD-GGtSL0OcYQjYRE6sdYiyFBS7Bx8fhWjsoFwMOO1FEXZrB-pSN1nLs60NAI7rKHMqX-d5sYF5p2n_vsQ67X4Mp4Qxk3BzW0uZSOXyXufgxxc4-Zfx41EK7VOilpB4gYuLJ4xrnPZItZ-ML97A51OQHK9vdGC05hcdAA-DvVMI3QrdxJr9_sNV9NcwF7mt09GIHF_Iv9w6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=NThwzig7tR8U5n8uHVJAACjSL72qrX8bhHGRI0F3B4XDiqRiJPOu8L8xzXBQZi0YwrGXoQoarZMxzBMwBuhKpIcR5AxSgNookVgU-e959TenPMgZDkeRFWETx2yh-61gotXs_yA8gnCD-GGtSL0OcYQjYRE6sdYiyFBS7Bx8fhWjsoFwMOO1FEXZrB-pSN1nLs60NAI7rKHMqX-d5sYF5p2n_vsQ67X4Mp4Qxk3BzW0uZSOXyXufgxxc4-Zfx41EK7VOilpB4gYuLJ4xrnPZItZ-ML97A51OQHK9vdGC05hcdAA-DvVMI3QrdxJr9_sNV9NcwF7mt09GIHF_Iv9w6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSgWJ8P1zr_IYYxIsokFdH5YpNAr0e_KE6-hzW1lJAsyjdvUP1od08_bKwvBdH34vSoycKmFEZMCXJt5h9BM8rmIV5GUsS7tNEF999vBKfVQiH9o5yzQP6qPL1AX6z8zQ1j1yHr-UIdW1t_97ryGQxBx_oytPu81U8axCkF-C83BvJKfynuKMqE2cix9ZeAlahukevTPaVeaU9UMhoaO9qc-iCcj13H9L4MHW7tR5NEpxlDfd9B8_M-SCGLH-QHO6YukCZq8GuY-Uf28dsDjEWwDo4ntzPGXd1LfTlc06zbkMiqcdgtypGDCliHSevkLv7dUphoam8e09anW6xTQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCzvbwRFyPnJuCXSRFvI4-y77RjswXeIkKjq6C8MdYbFkFb2kZPYBs6T0eC4Q3yyQrA_zwfCWHWTudJ092ZL-0C61b_oHRqCrfnzXTw935svhASEETaagG53gHpqbxx229en-TnMMnvPAoOdH7NgID-8jA4sXkVAr5yif-fUstnJ0tibRxzwAovzPRU3mkC-nvcddoWoqHqhn3Fd-L0YsUnqtNmKqXTnF6RgrGDpGZEEAQggIEroXGnpnbGlKGCsyE-HeJ7EJRulnGi8NKhDvEiseZZojdHeSIupzpeICBv-aBzD9eHunlhXEREiWygSdSPaRNofQy6xNe3_e7Efng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKFzc_1-pNkGV2okXvMQ7UScgT74yyz6L58CELE3UxDmQegOGKVJK7GWfLWmYyaxxh4o2siY4j2SGGMgl_0idXOPB1vP2TgZ753T023Cm5OCINrcK7lmxp7qR4MwVQ32z1WtV-woO9L0n4QWDyXnD_MtIeGmYLGloIT10zA7k8zzVUy3vfJKMrqsrQqI-0-joQs5jt3biqVDjmL4eN64UhYIyUQ6xnMq__5BVUo5fcimxC5ppKN6v18kOffLfA07mGQ-2TLXlECztb1wkUW41yvphYnG59vw_ZPsKKhYPXKZHll2quPwBEP6fqrIrnZMAlSTY6IdCEvhVyspWPebVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHk6cuW7QKgFsrMe1wTelj5_Owk0rh5yE83AluiCzFXmlupIeBrswfmj8qOCjdMFoADYhPgCOiQ6dQTKJ_vz5EizQNcRB0JCLry_u5dEvY739jtvyDeibC_L07d6cs2nF4sqnS7eLJ465iKOMnpwsb-Oi6901anz522j9nk4UjuPa4DhEeoy2FvMv9pLilZKi9_upyNgaZRBC7JiJDjImLF0oSAa5f-V7AKtaf1im_gLLVNy8YO-UbtjWsj1bnJ28xWpU0nbv0DEYMIQtS83rBcKhnaRGoV6Ixh4Oy7H2E1fSO9VtC4IVZCRyp-4Ceom_tZZ4C2zMlTARgjCEed47A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=STQvpZmbitH2yOhoED0ASVxD6y3EhXEB4WsPiYIb2ysm1gzt5in5UEkLqMMUHx39j_Zc8G0wAWhnkmOrFDKk6UwesOozoU9MQKdCp4EJQZiHUR1ARP__yIzn0IPQeL2WKpHH3zCAZA6TYtGRcfes4z3H3_rCv8VqwfAdbt3LGWIVqLFWFm_6Ij-0hmM4c75Lga9AYBXHC4hhqSH9gIto9G1W7-NAq1qoZ-01vOJ5-Sln2QC9IY76LiC-YbsoEEvqS4fVZgU_bEqFX8jWyYp0vErzHSFnh4N_YPutjBRXhm-6CSNHSyNKTKDoPYDOynsZNQrU64OADlc_aWmfv3qQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=STQvpZmbitH2yOhoED0ASVxD6y3EhXEB4WsPiYIb2ysm1gzt5in5UEkLqMMUHx39j_Zc8G0wAWhnkmOrFDKk6UwesOozoU9MQKdCp4EJQZiHUR1ARP__yIzn0IPQeL2WKpHH3zCAZA6TYtGRcfes4z3H3_rCv8VqwfAdbt3LGWIVqLFWFm_6Ij-0hmM4c75Lga9AYBXHC4hhqSH9gIto9G1W7-NAq1qoZ-01vOJ5-Sln2QC9IY76LiC-YbsoEEvqS4fVZgU_bEqFX8jWyYp0vErzHSFnh4N_YPutjBRXhm-6CSNHSyNKTKDoPYDOynsZNQrU64OADlc_aWmfv3qQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egvGyGb_XZeXzg2K1J98j6gdpc3dSBvMSZproSdOGDN5nW197UaOq8377FjOmZgpEd0nhClqmRNTG92gg5JiQZPFDn6BacRUBfP_3XdlVcsyBdvVfFbD28rOhV-IPj-xcAx9ebGjQwBTx2jgK2QzH3Sc86kN9ZaZ_8gqFZ6jzW3LhUtemNk-6KSd9J2M0EWYxNNZP0Vvk6HnuS33_s-dAiEfDDSOryvCkPwV6rkFts1r5nR3QiJnbBXD20rQgzOmyAeaiE4aPE0z1RLVaskxeluJm7rS4esI36GWc70HrxDMoDh3FW0zwuDCPjjJv0F4I5UHSQTTGz_X1iJ8wuW7yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orjRnQiv1m8UF6iXOHmMLEGoSmrAeZKOliB6RGcS1Zhqx1ar8zq8PKVrIdKa-nirDKJfEn2iPDr14q18yAeunw5_fwrVdhkrz6cHktImVpdU75nlgB2jgPpUxNs5LJtVEm-xj_qqkg0svv4qEpvUc5WCuK4edUzOrDYpENgviF0YipQi73BG5szP8oYfELgHJTN70FF2ccc2D1NSzIKxkAeaGkox-l62eH3GvsZ1Svh65830WOpfjUcJelDRuh0io9p6G8KsYPafdkL_A6q19eqM41qHBkGsQK8ZsfrUX6vz4HdHw7crABwCdv6i-GaQbRVdYpDwRo0h0PzFcxGShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=tpPInHvJck7xbIPvyrkb6yF1io2xkqBxH2x1CLz97dvJP7Hb503jmlQmt1m1Jo2AFFkVbfHDLTRmZDObZ57Zy797Ro6MRt-s5CZvY6pWNlknx3l2q4YpTdR7LN8-WHjAJ9JUUk4eOj5UXxeBRO0LXYx2ticNize3NKDZ316GQO4eYMtrPi8DJZnqyDpLBORrjYzNH-nR47Px8WnVwF-ZCWOsmyHwwUzNMPU3FekyddMWRrr-W6zwEzoywUq156dFAXwgpzgEYPXa8Wyux_5tgULQEEq4TWsBbau4v4kl1s12rNZPsQXVRAIwXA9_14NuYIuq6nNaBRqBBC6CrP4Jtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=tpPInHvJck7xbIPvyrkb6yF1io2xkqBxH2x1CLz97dvJP7Hb503jmlQmt1m1Jo2AFFkVbfHDLTRmZDObZ57Zy797Ro6MRt-s5CZvY6pWNlknx3l2q4YpTdR7LN8-WHjAJ9JUUk4eOj5UXxeBRO0LXYx2ticNize3NKDZ316GQO4eYMtrPi8DJZnqyDpLBORrjYzNH-nR47Px8WnVwF-ZCWOsmyHwwUzNMPU3FekyddMWRrr-W6zwEzoywUq156dFAXwgpzgEYPXa8Wyux_5tgULQEEq4TWsBbau4v4kl1s12rNZPsQXVRAIwXA9_14NuYIuq6nNaBRqBBC6CrP4Jtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na4Ur8K7D3kwJCCJMhCDNEleorpnlDk8C5fOrLDJdo3nowVYSxwYOhQx0MGYUUTAZRDiU2QkAD2lh5e6AeOyFfLZfocgEHJlPz7OjN6ziPS_6Bg3oKgj4Tcd6A4u8uXkI1CgxCguth_5WRCwzwijiF61BxGursX5RSRB44PiOJLoIVsKDHzKbgPDnnktnJrXC3jI67JwiO9WjL7c1Qe2xIfXWtm2TZSYRAV7r5-J2SmeBbP7hV1WCrW18ObLYRlbsvH6bgR1Y4ATGWdl2RpLe86-9xNfQ37zQNbezpwwlWr9247IYPwPqEfYy655pILv50vfeucVJULr2NmDIkEWSw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=mIipxQ3o1kAo6Hu2z1_lTumJVfTx3zy0F7FoaOHOX4BH0eClUVy_vCrphlxm64-34aUvaHl31nC30_tHr9lIoe4JSpxvvJ048Q5sIOBLlQ063GgXCccgx082Oq-jFJAGjQVsTXd2o4Jf0okZlxCR62xw1YhGr0YfwVe4n13UXq_D4SsCE9vyJrqaInOUJjBa-Hw4g0ACRRy_7KrHlkyAM5bbm2RnMmaq5aC9Rh8D9UYhsezSgaCNMJnE-MjCovpZUOQu7_0FiH9w8uX79jpZ1-qZQn1Ctq6JWR5L10jNRUkFwId4mAXZa88ws-obUpxLzNQqebaJBbgJbN94Bv8f7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=mIipxQ3o1kAo6Hu2z1_lTumJVfTx3zy0F7FoaOHOX4BH0eClUVy_vCrphlxm64-34aUvaHl31nC30_tHr9lIoe4JSpxvvJ048Q5sIOBLlQ063GgXCccgx082Oq-jFJAGjQVsTXd2o4Jf0okZlxCR62xw1YhGr0YfwVe4n13UXq_D4SsCE9vyJrqaInOUJjBa-Hw4g0ACRRy_7KrHlkyAM5bbm2RnMmaq5aC9Rh8D9UYhsezSgaCNMJnE-MjCovpZUOQu7_0FiH9w8uX79jpZ1-qZQn1Ctq6JWR5L10jNRUkFwId4mAXZa88ws-obUpxLzNQqebaJBbgJbN94Bv8f7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=FbqT4PAvasZaFX9gCLEt_g1z0ZcrWfleFNhDJ_LiVuAIXUSTx34pbo0XOQrOpHQqpVJHv413aUyilekIZ98qmNyRVuPRM9JuCWkYiqOQQZ4qwrW5adqVsFE0ML5lV12uEfhxOqyZGBE6VO9mZcflb_OzLzUFSaUWe06fbLp3dHbxjsBzNalYjecA81ZThuRuWVL-48nhCduP1nnn1Q_3CZdcBz-Gdt4wwYNg5VLmpkWuabRjcNmlhVkua3z0Vd8GKhV3aDi9OEF45K1avQ5gZx9ip9EPP29Pj0EmfT4aDLO1DK2-cVXRnmdurjfi8-E00RRimzuLtPwBK9jBJfZ6kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=FbqT4PAvasZaFX9gCLEt_g1z0ZcrWfleFNhDJ_LiVuAIXUSTx34pbo0XOQrOpHQqpVJHv413aUyilekIZ98qmNyRVuPRM9JuCWkYiqOQQZ4qwrW5adqVsFE0ML5lV12uEfhxOqyZGBE6VO9mZcflb_OzLzUFSaUWe06fbLp3dHbxjsBzNalYjecA81ZThuRuWVL-48nhCduP1nnn1Q_3CZdcBz-Gdt4wwYNg5VLmpkWuabRjcNmlhVkua3z0Vd8GKhV3aDi9OEF45K1avQ5gZx9ip9EPP29Pj0EmfT4aDLO1DK2-cVXRnmdurjfi8-E00RRimzuLtPwBK9jBJfZ6kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=A1pP379DnBMVLvFlmg1lqhNdhHLlo0kxhU7ghEzYvIcPyXNLOZvGaB2WsrUEo8lm3TNusTVRDBXXBBWRRQINkQusA3uLDg5OwfMTVBVudTlA9b6qNXIUseAXPSHg2K5y9UK1hmQyb9zDkKlpPqybgRNVKEwzakrOBr_imKLYfhYLnNeqNhrpxfaJ9ItCg5U0UItvNUkcTFJ8MjX-7MEUmWUxYALwWrecVLlbtIt4B0vwLaEFi78HI-wILhPZjSqHj2V137kw-0COllplkGGl_xQAR5k7hCCv-KbbmvfVjJLeLbox7coP7hhcYhy7J6f3YtApLlA_PWwgPQWBqVkqqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=A1pP379DnBMVLvFlmg1lqhNdhHLlo0kxhU7ghEzYvIcPyXNLOZvGaB2WsrUEo8lm3TNusTVRDBXXBBWRRQINkQusA3uLDg5OwfMTVBVudTlA9b6qNXIUseAXPSHg2K5y9UK1hmQyb9zDkKlpPqybgRNVKEwzakrOBr_imKLYfhYLnNeqNhrpxfaJ9ItCg5U0UItvNUkcTFJ8MjX-7MEUmWUxYALwWrecVLlbtIt4B0vwLaEFi78HI-wILhPZjSqHj2V137kw-0COllplkGGl_xQAR5k7hCCv-KbbmvfVjJLeLbox7coP7hhcYhy7J6f3YtApLlA_PWwgPQWBqVkqqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=DU_xt9yTAvCEI7wQj3fvUe4CaojrFrKVDepx4tmvU78EzSz_6767sX4Ar-NsMHQnwjDxPSABoE2dNSAMexKVJDEdhcikLH8jiDYxJVMeLYuBiGOYW-LgxiCuuf-iwj08xZcDMYrKakHigv495PXyjmrzCKUcKTr46cFxRQkoudM4bpmdbNGsoEBPV6LsmYFK5lwYirQdMj7QSYkLJ5b8D4AjJ7mr_bmLdBACG5vuFZKFJnhNA0RstPbrwLG-hWtbBnyJ6hG8rIIhr0fPoG4vyR45Ov-lyscMU-qvrMxcIp7lqSHMjzSl-py-dQl90-kD4K3lJDyzLqNkYGBuf2D3sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=DU_xt9yTAvCEI7wQj3fvUe4CaojrFrKVDepx4tmvU78EzSz_6767sX4Ar-NsMHQnwjDxPSABoE2dNSAMexKVJDEdhcikLH8jiDYxJVMeLYuBiGOYW-LgxiCuuf-iwj08xZcDMYrKakHigv495PXyjmrzCKUcKTr46cFxRQkoudM4bpmdbNGsoEBPV6LsmYFK5lwYirQdMj7QSYkLJ5b8D4AjJ7mr_bmLdBACG5vuFZKFJnhNA0RstPbrwLG-hWtbBnyJ6hG8rIIhr0fPoG4vyR45Ov-lyscMU-qvrMxcIp7lqSHMjzSl-py-dQl90-kD4K3lJDyzLqNkYGBuf2D3sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=UIxBGduo3BnjN42UoGkdgfy2-nlgUgFkDhExbyfDmTpV55gM6JjYBKyI8HCIZM9cDEQMUrEjWrNBwpzgAaU6ObIJcR2okP29LkOOIsUqwp1GOYu2HbvDkbR59odjvo75BBkEcsDrlTUX9PFnCZl1ClMC6nTRtMP_8bbZs4lvo3odXr0q1E-CrfebehfPCci8qx43Tp9bNqmj4VxX5fXnIld33nd_WEXp45qOybwNuCAC18h1DlaYF1axNCTI6Xa2KhLP7QTRF-vSOSjCKKG0cEyu4nlDwJKM2vjd10j2yps8_alIAkBN60VlDHRodY2F-BmTrmpsDn1TwDOYR3hogg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=UIxBGduo3BnjN42UoGkdgfy2-nlgUgFkDhExbyfDmTpV55gM6JjYBKyI8HCIZM9cDEQMUrEjWrNBwpzgAaU6ObIJcR2okP29LkOOIsUqwp1GOYu2HbvDkbR59odjvo75BBkEcsDrlTUX9PFnCZl1ClMC6nTRtMP_8bbZs4lvo3odXr0q1E-CrfebehfPCci8qx43Tp9bNqmj4VxX5fXnIld33nd_WEXp45qOybwNuCAC18h1DlaYF1axNCTI6Xa2KhLP7QTRF-vSOSjCKKG0cEyu4nlDwJKM2vjd10j2yps8_alIAkBN60VlDHRodY2F-BmTrmpsDn1TwDOYR3hogg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJtTaBOK56cKzl0dTEI037Cy6xfOw40hV4MCaOOMfPCX3W8QeLS0_aouqMPlSXuHpkdgCXN7tLqZpcH7cQTjmx6KXS-5prUxYykibDdUq-Yq-OWg1nJMWwf5GgYg_3hM1eYn8rpJ17K9odvR79LbgY7rEuXbwQnbFFaxoB0QfaJEM1rpHleFSqNAjh-jpTOnXk-sodILfqo409kiGNb7agbs3yGFx1cPuXXBUrxEFnnQHlKA-O_v4zikZ3IVxHBFXONMEol1cvlo3gbQhYtuyAAT17aLvcGKZDuwje-vCG8pAkCWAjrd53PTSWQn0sTxjmgwk2INDJPDGI6QVLFLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhIA93sWvmNggUTZ_uPxoWXSkImueie4Z7EcPbVoXQxcQQtEDrOxoVHkqQs71sAO3b4tkFKIm7UxBeWDU5GDZLpmmwlxB-ldTqReUSXCYR-NEFgWDrNsXY5t5DCUlPT7DIXzxxXNWU9lKY64p0kXo8TKz0rGBwBORO96cssvzgfKe-uW5b8QOmB74nDXN7dtyBnoY2N717IMiSCIX3fu5oh6itAQSZvOtOQZTqBzRNptXWmKTEUP3xn5cSOaevX3XaGWUUR_piImTd6MnE_pE7DTMJSGEXzKB6mlNypivwtom6D6Dogd89E9pzWpwc2auTbkR3iKbxHOV1nv4gz1vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dw1ur5RkG5QN6BYCzm2w5kJpM3nT3r-B_99NxL6q6CPqj8ZzISbrhQ67uvGeMjC4WxF72Zg-ljE-OeWzLnU54g6v44F0Ah_wO9GIqfF-OjGzSXVnHvOJwiF3EH9exFMWhGczfnF2IFaULn6pn9g7TBJ1bcXK2CW4LSdkP_qx5g9aM_sFQmg6ErnQBVNpTZCEJyse-b2vEw9kKA0lEykQY94RT9ahnysQxYVqEpSWaPjtR6jjpTniPZQWLgDyw6ChSJhxta24pUgwqsH07h7bUMhQJbq2iy2BmxlG9wrt9xvJuqisTU8FoSNQ5wCOFGmdbRNCTBJVvu2a1K2kHxfV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZIXyHquqq56HGBZ9CD5ayOOVZ_hBkwG8LWk1AadRfrLwnp0d0QWDfOUExeh5VOLXolkPl1P92SyG2J6RBEwpMJU_1-rEaK24ftD1BFzK5wG3KAnERiKw39hopfNR0cIpvO6500d3mIakLNnNHy4sc_1h30MtuMAyr2iwPR1L94fsT0ZMzYGRieCBKmKFamXX39sg0bD-9kjgjGp6fdrSQgxN1vK0jNigNIzuMHZlb3UPCPtUjUeAJ5F8Ew4lUuBYidUTRkXOGjvYdDXSnERQYA2TNyBCN3FBnHauzwrwTPIim_TVtRWQwIL23ZzN180gcMvu7EVVpv1gtQc7nwCNA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=sCVyuEvS-qZLRzjZGntcArDqgfw108vNa9ZDiMV8rMRHtFDvCbULepNXXClo76hVwFbT8u2dLEsWIcbD9XJchm7qCmHQqwkuk7LQ2KeRmnZuXHb7nZZZG1_rQoK8gpg7I84i6wDHdChomf6-fcdVtZP0s6KjBEj2dbXkXtUmPnqnNghQcMUikneaJvmksxx9kgKNHoe7pTVqJ8w6495y979LBVh-rL4Qfd9WEm6XFwxgUMFwQYGpNKtbu6WXTcxylrQws0X2XKfxBMbdIYh7XvF87N95TaSrlyTjOWpFIBarhGA-VNwkEejQJU9ayUUuNk1k4kuImLbrw7C3TdLvZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=sCVyuEvS-qZLRzjZGntcArDqgfw108vNa9ZDiMV8rMRHtFDvCbULepNXXClo76hVwFbT8u2dLEsWIcbD9XJchm7qCmHQqwkuk7LQ2KeRmnZuXHb7nZZZG1_rQoK8gpg7I84i6wDHdChomf6-fcdVtZP0s6KjBEj2dbXkXtUmPnqnNghQcMUikneaJvmksxx9kgKNHoe7pTVqJ8w6495y979LBVh-rL4Qfd9WEm6XFwxgUMFwQYGpNKtbu6WXTcxylrQws0X2XKfxBMbdIYh7XvF87N95TaSrlyTjOWpFIBarhGA-VNwkEejQJU9ayUUuNk1k4kuImLbrw7C3TdLvZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=H1sg41y1oz9bbswiQ9NrY-FxXCY-fSWTFwj8vZGR1CK1m3MBob_q752nJKJDg3zYyhkAo-tpUq-7gEYkzo-XzDamGm-ftNFtDf7FawPhOdpBs4vg54EcrovBGHnPX8RGDQgellxal6Z7E5QjCDUErDn8kgYDrOlay0ig33cMlIcVbvnZrWxbPcyiNBZ33kPPiBJFKTsceGxiRoBrEeARldzXoPYCQRBicGjF4uyIh2KPkWg0nsyQE3WWPxVVWafVQbQhRoTupoYIml1w4tqMnEya1ZIm3Iqbc3saoEK2m2EV3a6JEOakpowZRW9TCpU8bHo3qe7jZvryy4DtrtNWtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=H1sg41y1oz9bbswiQ9NrY-FxXCY-fSWTFwj8vZGR1CK1m3MBob_q752nJKJDg3zYyhkAo-tpUq-7gEYkzo-XzDamGm-ftNFtDf7FawPhOdpBs4vg54EcrovBGHnPX8RGDQgellxal6Z7E5QjCDUErDn8kgYDrOlay0ig33cMlIcVbvnZrWxbPcyiNBZ33kPPiBJFKTsceGxiRoBrEeARldzXoPYCQRBicGjF4uyIh2KPkWg0nsyQE3WWPxVVWafVQbQhRoTupoYIml1w4tqMnEya1ZIm3Iqbc3saoEK2m2EV3a6JEOakpowZRW9TCpU8bHo3qe7jZvryy4DtrtNWtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=MXMHtjc14elohzsVSJ7XIOgSPXUsvJGAOMmu0_p8IzXlIv220V0EmxMzXFMNZnErmPk4EcO2byFn_zIYEehj4pEajF4CrGd0K75kc2jTIBgzxEj2hZSE6sxsU7wMwK8wgYpREqN6KLlDr44z3AaTDCfTeYfsNKVoIjjtayP61yvj1xwpXkCkJi4jlhmNis6RcJvf8r5YhKSGnuikX1IInlwCnIQyJCa_8yKllzRneISdbgAD2V1qyNP5byJZVwIjdwuWm8AnkG9d3ngo4RytfY_1RALvfhKB2K-6vy6NLENX-IjmCRP-QEu2zasVSu_Z5BFR4LvBXa951HV7mQaNJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=MXMHtjc14elohzsVSJ7XIOgSPXUsvJGAOMmu0_p8IzXlIv220V0EmxMzXFMNZnErmPk4EcO2byFn_zIYEehj4pEajF4CrGd0K75kc2jTIBgzxEj2hZSE6sxsU7wMwK8wgYpREqN6KLlDr44z3AaTDCfTeYfsNKVoIjjtayP61yvj1xwpXkCkJi4jlhmNis6RcJvf8r5YhKSGnuikX1IInlwCnIQyJCa_8yKllzRneISdbgAD2V1qyNP5byJZVwIjdwuWm8AnkG9d3ngo4RytfY_1RALvfhKB2K-6vy6NLENX-IjmCRP-QEu2zasVSu_Z5BFR4LvBXa951HV7mQaNJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQJYzmXMRECfXf1UTGy0kDVi-4pktsKAHNGNpc-GD0gwnTZpOFwCf87nr_wnkEMsjf9Hq_-wLM_xREe51unysorsowMWh1imeivC4qRDoo9X1GfV3UWLCB_Te4H-nXZTTu-1EsIBiSec4R3aGDS_XJ0CEaImYZc2MR2fkeKMFtd3EoO_enq_9FFoQwvejflBgINKPGNmrYiQRFpakbbpKnbZrCXkz062oO8gCEL6DM4-mKgCPwS8f9nKQYSxYg5cp3yohs8fRl9q2BwJK5hE8IDqh9rpKTK51F8JOE-DQOq4f9BV4HwY9Ol6tn3UwlqK9QWBgtyignBHCfQCJDzAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=K4tUch5SrdPWTj12GlH87c5_clxMFU4L8SHtbbz7oLFrJpCzHVPcr6nHxq_FaBmIQBoxQ4aBan-xem2raJzjrruRvtyBtPnzfx-D9hWHfs6HpJTANmhk6Aj_eYE4nWZ2Sb8G1OHtaChQEG2Pxl3NmEs9pZo5DbqgJMldTaEJBKearjNGruI8ZIZftI-fb6930mHGVpe-q-j4LJHexqcQ4DPT_U2S7Eeg7SLeyjamK5OH3IZmgx31jNRu7neiz5d-kLL5d4XRF3csOArU6xVzLGntw3hhmJa-8vIF6tSr9FAEMYKYzYH0DpNaOy6QvE0eyYXcihNr2c3fYNuom61AlXeAb918eUgLLtFLJDWceLej57zk2cvEQtN0Yr_5EP8nq0kB0KmQss5XpTiKjcKcvvAExxvan0c-xHLE6VxAQUPdj4icxLwnvfoYdG2PfpoPL2bkqtep9AXrgb5Ipbt4tLo3JMcOqHgEDjvso8qxTF8jaDK0d2SuTrPys-jlmtgbTlKSroswQhT14acC9C8gjHRR5WpuTI_wyBwgFHvvEZ8PqbtcvSxaVPMsXkDSgJ0AdUrHNQu8JFgUgVI5QSNhnRwK0Uu2eTUH_fjdYD3gXx8KcVsNCOi9kU3H8sb_lZWtKebfWf5GxgGxOMkWrNyTnPj-Q_PnEeAT1s_JcAN7ZTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=K4tUch5SrdPWTj12GlH87c5_clxMFU4L8SHtbbz7oLFrJpCzHVPcr6nHxq_FaBmIQBoxQ4aBan-xem2raJzjrruRvtyBtPnzfx-D9hWHfs6HpJTANmhk6Aj_eYE4nWZ2Sb8G1OHtaChQEG2Pxl3NmEs9pZo5DbqgJMldTaEJBKearjNGruI8ZIZftI-fb6930mHGVpe-q-j4LJHexqcQ4DPT_U2S7Eeg7SLeyjamK5OH3IZmgx31jNRu7neiz5d-kLL5d4XRF3csOArU6xVzLGntw3hhmJa-8vIF6tSr9FAEMYKYzYH0DpNaOy6QvE0eyYXcihNr2c3fYNuom61AlXeAb918eUgLLtFLJDWceLej57zk2cvEQtN0Yr_5EP8nq0kB0KmQss5XpTiKjcKcvvAExxvan0c-xHLE6VxAQUPdj4icxLwnvfoYdG2PfpoPL2bkqtep9AXrgb5Ipbt4tLo3JMcOqHgEDjvso8qxTF8jaDK0d2SuTrPys-jlmtgbTlKSroswQhT14acC9C8gjHRR5WpuTI_wyBwgFHvvEZ8PqbtcvSxaVPMsXkDSgJ0AdUrHNQu8JFgUgVI5QSNhnRwK0Uu2eTUH_fjdYD3gXx8KcVsNCOi9kU3H8sb_lZWtKebfWf5GxgGxOMkWrNyTnPj-Q_PnEeAT1s_JcAN7ZTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBZDlGF8ORmrx-gA1nQYVZNXzXsu9uBM2DSVBpKZDIkrencZTC27PGvyu9Q3K1AykIv3H2uJ2gf4CozBiTSJrPvUEn8A-Dh4yPODcsvj81YfAaq_4dVW80E9vv0ID3eSm9MWzfR5lRnYJPkWLysfA3hbbGMe81bgvnZKaFUKld7aveTRwsk4KLNAUqgw-4y3I_dWUUBt0QcrmOKJOSvs627nPpwB-nsfI00c6oHMOn_Uxwvq5nnPxZsZ94ra2nnkOyzX_s223fBX_l6xSomy8y9D-a0mWb4WUOe_nzyQ4pVfBLFEMGY947Hl2-n4hux2Xs-kk6tY6ItJHmRUJWUDYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=A-cF0OP5gWZWUpX2h5sRoQKcn423M1JHugutmYIW5KdNgk7HEeFriptV6ktTTTkQB0NtsPQc0ehBNK_62_iF8uGLhyLu1v9n1W1u-Qeqh7jLnVqtP77GMzQoz2MAFnvGdbGM9NdSkSmo4atng9fpi2qPm3ba2shmgGMtKix7ILf2ElTQ3vWVmuuAcHiZnV0hzTPM1LHgm-lCf2X0XRV0qmHoc5snIRmzDQUbBdlwd7JIoUy5CsXMtwgGb6kUhHHoHJRRifmcvgR0gb_ahitfsoLCL0kBikgatx-Mok6tHc9q4PAW74cOttc_pZmlFOwqtk02-QLRMTHHGRzFolA3Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=A-cF0OP5gWZWUpX2h5sRoQKcn423M1JHugutmYIW5KdNgk7HEeFriptV6ktTTTkQB0NtsPQc0ehBNK_62_iF8uGLhyLu1v9n1W1u-Qeqh7jLnVqtP77GMzQoz2MAFnvGdbGM9NdSkSmo4atng9fpi2qPm3ba2shmgGMtKix7ILf2ElTQ3vWVmuuAcHiZnV0hzTPM1LHgm-lCf2X0XRV0qmHoc5snIRmzDQUbBdlwd7JIoUy5CsXMtwgGb6kUhHHoHJRRifmcvgR0gb_ahitfsoLCL0kBikgatx-Mok6tHc9q4PAW74cOttc_pZmlFOwqtk02-QLRMTHHGRzFolA3Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzBmzuoZ1QXQjIUdcl7BvrOw-TOjgir5H4TvNXXZfY3DOoGyJ4_Qi6cpp0DJwXElwUX10ItdviPM9CbF_4-7aR-_wcUL-2vFUjWOwTAflf1tmfErzHhH87At1r_LwLp6TEljJZr5PlqWAzAUUkpWSz9z6E6d_c7JFPDzTP3ntkJZ8hbXsmQhq7z2WjZSfoFm2NQ1rLHIXr6j4vvpvdFMOZq0UzB0qxSa5Z-Spx3JvDC2UUv8KEw8GZvTkBUHb4z2AKXZiGqPDGsdlonieBpf7a5PjN2GlSYTKb59iSQAMniQDlugKUuvHXa8AD-nZc46rqzNk5KzU-EBq0Jj0xkEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzm_dXuuBnoQGjZudk32hK__yl1fFPGfcSJ_IrKY6T3r4ADA7Fuql8IZMRQg3a8w8PHgtleCpmkfkBQIB9Q_mLi_eq-RstThJcHMA9a5TXYG9fzZpsiiX6S32JpD2DOZTWimcAvHrL31x38IDYgI_Bq1JDiL8r7gILp55ErZCUHgnC4jfSxLbGo1HlqRIksbtTWJqL1V718tNL2PoM4EYltpT6y9uvCFbyIAgUlGCGsO1Y4Ln4PuppotdxdIfgAxMXJRykkOOivCPxM7a6SsuDUUl2jxUGqdjSmQIBK2F7QZhHfOBuVvAuJAfdaXxkBJHly9AHJURm4ZSJ83B2k0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2TeRNsefjXbJzuk1-fBDJMX92bcwEwQFgyg-TTiVLY7OdX4HxWNqzkr4tFWLFXjbSEflk4XnI-yu5taVfpKfthsjTD8XJlMaYdHB3eCY3b0hUWCRu4xThoMPpDII8D4VdrkPGwRAcVb4sJI906G_TiQ5hGWSLDDCORakcbEM2EGlGJSveP-8DaWzwCJ9XAY4uevE0R8Pd9h-ksIwt5w8K_JidaVRPt4AXm_UgygzWvvz8wup3WwGoPtc4fAjXM4ZSnsxDXo85aZCkeiUsuhlW_SWmCo8IXDU5oDff9ay8eom93HjmzN-o_sCgWe9jabTVqI5LWNRXgR6tg_nFky4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDKAHv6YdsMAWuSx25P5eGthM7Q5DgWJxwidRhEGk8sGFsSom6fDQMNKOdDy4HfmhMaFiF87LeUXYBMhpm7Ox7S_Hma5FV00GvBfj9hVU7_qfu3Qlmls_vKM0VI0OrQrAdstn5Kkl_bOCXgokAHaxOcgweZ0GW02ZuvqqdYI7qof6PPxQjsVngp8oP85NPkZvuZ-JSV6Tx5IPv75UtOCkMnmQd0UTcqM_TX-jf7-JyYWgPuAf_QVO0RNyCXdYo8LhyDivHlWyK1aZy1570ibmxGFoNLcPUogfKEF1ZmuqT6RRLiy7lhg9YsyT-cgJGk6xRzmUv2CFmfdURjJDYv2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Welcv8CFRJj5JiYMg7asvtp1lzWpPWF5cXfp31eS5nC8t-v5f8NGikO4-iqYwWNl0QaCxuFhcxNBbqQgwd11qJr7_XcteUjXLPgQ0V1xWKOQQQgwkHioEQy4dVytajqiC0Ix4Y0ztRnd-fDfb63sknkqaoGYrdmfTjnvqY0Ta6bRvgBifewY4Wz-Cf5LPsmxHyRy2RJeckYAWP_7LhYwSHd86y9K0zgS7HqFTZ201I5DYzOlBKzZl67ak33CHycdlKV5D2sY6rVnQZLaaxkBBV2RiEH0MNHZT9FSkMCKMErI4byxEEmbgCZZdT5MmZz618PGx9INASnW5wJrhFIzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp1FtqPIsz7VukLPwMaSUGBF6tmqmY0hugjMYB1niQ7dZFt2O0k66sLNH53HGcn91b_y3OuHxjRR5BHWI67KuK8mpZgzI4YQagIKmuBAKQRmvQ0R65BfUJhd447NTUBbrU9U0biituyFt46ta6yczv-MM44N-4bNQ9vAtTwDuTKihjx-OyEUCXgQEMFmJDA-UjGyLXYA7o7GQmxh8ajF0l4cYgb_KaLiwU49vpcRpNc3dcIZ43dn5oZDBCiFJ47icBjCEUEU7wcAMrcfFWtwX0qyPSYse1XNunfcCGOB5vDLcaohalUYB0K1eZfKwTa6ZDS9mPHg8IYNTAhkAwzpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S57TNgJ-gHVaSI9HAWTaWhsDWhMgD5ajMb-zhwja9qXMgJGJ6u34LPG-dvYT6PAEw5wGHTKrVvAwJgL3gdebt8JRMAzPHcroRYabMFEz4s4kzlkwPOPqdX-3dkbk23yl4EnexQoOm3jr_XLKNc_Ktj9BQ0kw3-rzzcoZPgOI0kM6s_lTgEXqpUUuvK-YtWjuZ7B8erEzwcBGChDsrpmY9mJkr59ln_M05n9QmlKCYabPt19eotkq_nQYfKwCl5wB2INqOzAni5lmyTl1pgxcURnfTIaBNLaJp83VvTqPYWkRKE59pGLVYlkyLoMUOTdYaqSMRFm8K4IWMmKTWwYLKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=PFZiefb_7nAdO-ZzpZ9DvUEWmnPhVgVEV9JaOM3yi61SvJJV9x0q-bOy1SdRKtT3onrgmuNw0a66kcUXit6iGxmoEJjrTYCLdVEmifaIaaSJo43Tw-orMs8adxvf9PZ8hya_ju-pRBSPHLO9nAtUEudmESmJghG7iS6IUz7uBzkrDytbB8aFj-AIjxGzyOPE1Y5fE8mHtb14MXrJSnhei4tk5iYK7chq80mdgs90gR8SxVzh08IgMgzoiZpzRwMXjoCsTBSfNj9p8CqGgX21vgsYzUDcMz7BJ2A2PTzCxmWESD1nBX5YiE0lxPVAZusMgeRPw0cHjwXt-c3jc0v3Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=PFZiefb_7nAdO-ZzpZ9DvUEWmnPhVgVEV9JaOM3yi61SvJJV9x0q-bOy1SdRKtT3onrgmuNw0a66kcUXit6iGxmoEJjrTYCLdVEmifaIaaSJo43Tw-orMs8adxvf9PZ8hya_ju-pRBSPHLO9nAtUEudmESmJghG7iS6IUz7uBzkrDytbB8aFj-AIjxGzyOPE1Y5fE8mHtb14MXrJSnhei4tk5iYK7chq80mdgs90gR8SxVzh08IgMgzoiZpzRwMXjoCsTBSfNj9p8CqGgX21vgsYzUDcMz7BJ2A2PTzCxmWESD1nBX5YiE0lxPVAZusMgeRPw0cHjwXt-c3jc0v3Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWphbZ7rC0wfVv07JyfvCA0AFH0wNXCPy233fkAQ2PRGqTy715W4VBjGHIuQuLpjOhfC3PeswHGtSw48MBEqOtnV2G5NppLvOyNna3mDtA9CdtD3YFpzoPsV_1RJ4kQiFH0osd9jXYD_RItYa9uQd0eahiRo3izgSfAW1J5J4wPqt_TNuCg6SBlhb55I3SZ9mDS3Jvfiuz6Sayecy64UQomPi198Rl1SC5Rm6EeE1rPg8PpjkpnJWbEZaMuig7R7R2r_AEHUCREFluZVpAV4ylxppdAondjUmRIgm-9OHtJsVlwfz0eF9mqe2Vw6gYcQcDfSnL4WYaAly4LI1o6_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0z-G0V_NNRt6vmJSB7Cc077wiZj_c797badPqGBC-nRHzkS3UtyxwmLXyJt4gIUp2pUYGI66EVYYt_ZnFYMRPc4s3eqGKVFTeYDdCwA3ByJN72vFzVu4trZDFeZZBaaEpw7yj2ogU3EBytyGkR4FQwBeSMNVI9chcrLgKAbTajnPezWgTzMwusM2JtC4yJP5DT4yibwuMT2BRX8RI5Ze-zj6Se4sOuYSyn9LmA82M7eO0v4zd6U_IIsPGjtVbsPsWB8EkwlzaEIC4HJ3rFarm6hnyoukwtN15dJ4_zdPWfyiue9HZJqKSsYniQdOsHEKPme2mrmw94cesXZbWrOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=UvQ2bZBWuqUtyJFitrljYKa9-hBh-pZaR1UAnByAny7Yo1lEvIHbLa4PZ5OFsQKpa0KjlcAZpTIjxzWrWv7tlZiYAMrNmPcY13bSu0HT97VEuD-0TsJl-wndC0rmJ3NxDNCl4mERVqXVX7jB0zel9C7YOBzTm1DoyWjkd2G-DQK-mkhvP1xkD2HBNhIV2mqihqYD3HKFF5o4MWg7bWYmlyFRIafPGz_gQUmj5QCQKu5ueqrYRY0OecA0EvdAO4LNqTFl1r2PGeB_vRJPCd4iOXltF_yvujuI6UUrVhXBDS3sQG6LSfGspa5yX6R0AagxJzBfiZ38v__7S2wRthJ7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=UvQ2bZBWuqUtyJFitrljYKa9-hBh-pZaR1UAnByAny7Yo1lEvIHbLa4PZ5OFsQKpa0KjlcAZpTIjxzWrWv7tlZiYAMrNmPcY13bSu0HT97VEuD-0TsJl-wndC0rmJ3NxDNCl4mERVqXVX7jB0zel9C7YOBzTm1DoyWjkd2G-DQK-mkhvP1xkD2HBNhIV2mqihqYD3HKFF5o4MWg7bWYmlyFRIafPGz_gQUmj5QCQKu5ueqrYRY0OecA0EvdAO4LNqTFl1r2PGeB_vRJPCd4iOXltF_yvujuI6UUrVhXBDS3sQG6LSfGspa5yX6R0AagxJzBfiZ38v__7S2wRthJ7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=bbaXgd8RbF_-DrSFoHvgKdzK5Beg2xIT_XyLhbxU2rQpGZ9K9wCNCXKH_Vt4AtB7r0sswgBzboXoKO4g-VSEGl9mTCiC3cKFJYREUOZxsVCfBgiREkAg-qXwujq7auN3tiVaXpHNm-XFKS2aYhieVdV5t2DEbILU5ELq9zVq8_HXfmf7AsLjavMdhWiQyACdhLkhp-blP7xyBxMhQOGoB44GW2c-ZcXCeh6C5yFeigjo-IiaazLW3cGx3B2uOvWJlyY-KTCfv8O4Np4AIPpK1B-tfuEb6JrgFDLTKPZ5cEL8FH2j30fRrs7vbEqqm8LC1ukY2eM5oAZNCYxdqpko_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=bbaXgd8RbF_-DrSFoHvgKdzK5Beg2xIT_XyLhbxU2rQpGZ9K9wCNCXKH_Vt4AtB7r0sswgBzboXoKO4g-VSEGl9mTCiC3cKFJYREUOZxsVCfBgiREkAg-qXwujq7auN3tiVaXpHNm-XFKS2aYhieVdV5t2DEbILU5ELq9zVq8_HXfmf7AsLjavMdhWiQyACdhLkhp-blP7xyBxMhQOGoB44GW2c-ZcXCeh6C5yFeigjo-IiaazLW3cGx3B2uOvWJlyY-KTCfv8O4Np4AIPpK1B-tfuEb6JrgFDLTKPZ5cEL8FH2j30fRrs7vbEqqm8LC1ukY2eM5oAZNCYxdqpko_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJgCWm_KZommaMNsroFpi5SG-KZLHEqJyePhWQXRPZxPYSP8Aj-fSARe_TDtK2JGSYPyplvQtMqjGRkNGv16FMzb_-E3uvw0gkDiwFHY6jWrb9ugM4xzfbp4dCTiF0b9k455gEXa5Q60yucmgKfrk48SzV1zgrvYjzsNMRCA8dJjaSxvIg3mu7VNi8gLSBo-YNEJlf-dxsbUGToSi4Zm1Aj1sroJFIZD-jAHSwLzcPdLxQbbf68aUDq1eu1xNSO0vPQh5eB4DlXQGqMdLyuZgXgbGvfZ1Sjvncg2xcsJJXa8bI18qUcEGZnMMDsqA9rSsGl2yWlllAmLcnXANNxWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=BwjwrIHAdywJLfC0tJBkKYVwwa-sUPA1cgf6EWMZJEgSY9K_pNlw20nQUP6sleBPCv7LSBO5N4LrxhjnqDGJeTqfHpwjKXOjaf2Z6ozFmMb5sEEa5H73YI2CMkr2bL5avtcRAoWLD3cqeZL_mGWPELSeHBGQIrg7mcjhgIUucgpxu1KuHMLXiQfTuQyMAKvTvJAPxyP4eNcOcQdL2qr9AOWIcoLdy_VIl44rTleGE_medRYbyYTb3rtNZcYmY2cD2ISv7rKVw_3KQSp6lZi5rPHUzTqyZcKXfqKtHtcbuYvpfJAddf-6yml_QT2IvJKm_TuEsCmvGP_8UzrtY0SRfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=BwjwrIHAdywJLfC0tJBkKYVwwa-sUPA1cgf6EWMZJEgSY9K_pNlw20nQUP6sleBPCv7LSBO5N4LrxhjnqDGJeTqfHpwjKXOjaf2Z6ozFmMb5sEEa5H73YI2CMkr2bL5avtcRAoWLD3cqeZL_mGWPELSeHBGQIrg7mcjhgIUucgpxu1KuHMLXiQfTuQyMAKvTvJAPxyP4eNcOcQdL2qr9AOWIcoLdy_VIl44rTleGE_medRYbyYTb3rtNZcYmY2cD2ISv7rKVw_3KQSp6lZi5rPHUzTqyZcKXfqKtHtcbuYvpfJAddf-6yml_QT2IvJKm_TuEsCmvGP_8UzrtY0SRfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=ahHJnP6OhYFyHkmj0fZ1HjQZyI9nxiI_qgko2q9KkEpW4puc4wwb_iZlKPXqjU_tgHr7kpPbP_h5hADW7nAoD1PbS92qPb7zYXntFJyV-jzAX4OXckYxWDjak18xXO4k8t6FWz4KU_85see7ntfQM_sRcOz1J12uWTW0SRyPZ-8R6HNjVUbrb3fRByO4aWfBTTNj1yQAIVXuvz-Okzo4TLB7bZmo5TWkN8354HbaaMNXOs8evaLpaKpvVKO0uzhK-t6QxDGDR_W4SQBt0VifaZktUf4jIGaZPhtU6-_sIwQDw0oOC-8f45N-5mmtHe0Jw2W453KDIN3glK7WhAcStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=ahHJnP6OhYFyHkmj0fZ1HjQZyI9nxiI_qgko2q9KkEpW4puc4wwb_iZlKPXqjU_tgHr7kpPbP_h5hADW7nAoD1PbS92qPb7zYXntFJyV-jzAX4OXckYxWDjak18xXO4k8t6FWz4KU_85see7ntfQM_sRcOz1J12uWTW0SRyPZ-8R6HNjVUbrb3fRByO4aWfBTTNj1yQAIVXuvz-Okzo4TLB7bZmo5TWkN8354HbaaMNXOs8evaLpaKpvVKO0uzhK-t6QxDGDR_W4SQBt0VifaZktUf4jIGaZPhtU6-_sIwQDw0oOC-8f45N-5mmtHe0Jw2W453KDIN3glK7WhAcStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTy3K0OEdVSg-xc_1y_Wc4OGGHIwkc7C4XN5cfU_Y6To0LFhneGG5zg0CYW3doU7ftfQY_iUFIdNb4ZU31UGlM6_vvVzLaMgL9yoiUFprf4bliNcBCJdwPr-iIS_pzstKMwPsfbqcR8Cj1N43NLaji7Eu5UmUq0PP2YGXxcieVtmaNokncg6iKEfoKUTJ1tehsMjoLlsBRcoNnOXhZSuc8q96XueEgME83IAjLCMdUBgJETHDcX5jGS9LN6wpx_mbefsigmiyWiM_a79GHtz_rPP_GrGviS2G_f07_9q2nMNhFAsWvgs-Uii6jbcC3uIy-Vjw25HbWlDo_AlIo0xmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQuQauah41vRbC5W-dFtpuMv6R_0emabICo1J8fYG_-MpKd_MNDKtxXLzJhEaombt8SwN2YJwvnhSeamtLIiBr7SsU__RIiBVR-x58SYZWA3f3Zus6hIEqVqaJXxJP9UvWrK3ouFqXrJKXe7O5qbKlPTJnEpafmggCcr2MXGCR23YRpmrNFRVPpstRsZZp2tlLDsckv4esUmDW1JOhsCYu0YFQGZB2_pGLNI_x54osIhGfiKo20ZJ6KewhNcnigFn5jSSUyrs6vebo3yOEoMN8Ia9IUgmYQ6GHhKKWbmLIjzpwl9WjqsjXAEP9hMIEyYAmfSIlz8H_rA3jvK1E-XRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
